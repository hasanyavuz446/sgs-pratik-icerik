#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kur Farklari — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

FM cok adimli tur (hafif). Olay ve hesap agirlikli 60 soru korundu (sinavda seyrek konu, ~3 soru). 17 mutlak ifadeli sik dogruluk degeri korunarak onarildi; oncullu sorulardan biri 'Yalniz I' olacak sekilde yeniden kurgulandi (hicbir oncullude 'Yalniz X' yoktu).

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: VUK m. 280 · Tekduzen Hesap Plani 646, 656 · 1 Sira No'lu MSUGT
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/finansal_muhasebe/kur_farklari.json"
STYLE_REF = 'SGS Finansal Muhasebe (mevzuat-çeldirici; sınav stiline kalibre)'
ONEK = "finmuh-kur-gen-"


def patch(stem, options, answer, solution, ref='VUK md. 280 (yabanci paralarin degerlemesi)'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Dönem sonunda, yabancı para cinsinden kasa mevcudu ile döviz cinsinden alacak ve borçların değerlemesinde Vergi Usul Kanunu'na göre kural olarak hangi kur esas alınır?",
        {
            'A': 'İşlem gününde geçerli olan serbest piyasa döviz satış kuru esas alınır',
            'B': 'Bankalararası döviz piyasasında oluşan günlük kapanış satış kuru',
            'C': 'Bir önceki hesap döneminin yıllık ortalama döviz alış kuru esas alınır',
            'D': 'T.C. Merkez Bankası döviz satış kuru (kasadaki efektifler için efektif satış kuru)',
            'E': 'T.C. Merkez Bankası döviz alış kuru (kasadaki efektifler için efektif alış kuru)',
        },
        'E',
        'VUK md. 280 uyarınca dönem sonu değerlemede kural olarak **T.C. Merkez Bankası döviz ALIŞ kuru** kullanılır (kasadaki efektifler için efektif alış kuru). Satış kuru değil alış kuru esas alınır — sık yapılan hata budur.',
        'VUK md. 280 (yabancı paraların değerlemesi)',
    ),
    # düzey 2
    '0002': patch(
        "İşletmenin kasasında 30,00 ₺/USD kurundan kayıtlı 5.000 USD efektif bulunmaktadır. İşletme bu efektifin tamamıyla, daha önce 31,00 ₺/USD kurundan kaydettiği 5.000 USD tutarındaki satıcı borcunu ödemiştir. Ödeme günü kur 32,00 ₺/USD'dir. İşletme kasadaki efektifi ve borcu ödeme günü kuruna göre ayrı ayrı değerleyerek kaydetmektedir.\n\nBuna göre bu işlem nedeniyle kambiyo hesaplarına yazılacak tutarlar aşağıdakilerden hangisidir?",
        {
            'A': '646: 10.000 ₺; 656: 5.000 ₺',
            'B': '646: 5.000 ₺ (net); 656 kullanılmaz',
            'C': '656: 5.000 ₺; 646 kullanılmaz',
            'D': '646: 15.000 ₺; 656: 5.000 ₺',
            'E': 'Aynı döviz kullanıldığından kur farkı doğmaz',
        },
        'A',
        "Efektif 30,00'dan kayıtlıdır; ödeme günü değeri 32,00 olduğundan 5.000 × 2,00 = 10.000 ₺ kambiyo kârı (646). Borç 31,00'den kayıtlıdır; 32,00'den ödendiğinden 5.000 × 1,00 = 5.000 ₺ kambiyo zararı (656). Kalemler ayrı değerlenir; 320 160.000 ₺ borç / 100 160.000 ₺ alacak kaydıyla ödeme tamamlanır.",
        "1 Sıra No'lu MSUGT - 646; VUK md. 280",
    ),
    # düzey 3
    '0003': patch(
        "Tuna Makine Ltd. Şti.'nin 30.000 EUR tutarındaki döviz borcu, işlem günü kuru 35,00 ₺/EUR iken kaydedilmiştir. Borcun 12.000 EUR'luk kısmı, kurun 36,50 ₺/EUR olduğu gün banka aracılığıyla ödenmiştir. Bu kısmi ödemede oluşan kur farkı ve hesabı aşağıdakilerden hangisidir?",
        {
            'A': '1,50 ₺ zarar — 656 Kambiyo Zararları',
            'B': '45.000 ₺ zarar — 656 Kambiyo Zararları',
            'C': '18.000 ₺ zarar — 656 Kambiyo Zararları',
            'D': '18.000 ₺ zarar — 780 Finansman Giderleri',
            'E': '18.000 ₺ kâr — 646 Kambiyo Kârları',
        },
        'C',
        'Kısmi ödeme yalnız ödenen 12.000 EUR için kur farkı doğurur: 12.000 × (36,50 − 35,00) = 12.000 × 1,50 = **18.000 ₺**. Borç + kur yükselişi → borcun TL karşılığı arttığından **zarar (656)**. Borcun tamamı (30.000 EUR) üzerinden 45.000 ₺ hesaplamak yanlıştır; bu bir kambiyo zararıdır, finansman gideri (780) değildir.',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 656; 213 sayılı VUK md. 280",
    ),
    # düzey 3
    '0004': patch(
        'Kayıtlı değeri 600.000 ₺ (20.000 USD × 30,00) olan bir alacak, kurun 32,50 ₺/USD olduğu gün banka aracılığıyla tahsil edilmiştir. Bu tahsilatın kaydında aşağıdakilerden hangisi yer alır?',
        {
            'A': '102 Bankalar (borç) 650.000; 120 Alıcılar (alacak) 650.000',
            'B': '102 Bankalar (borç) 650.000; 120 Alıcılar (alacak) 600.000 ve 646 Kambiyo Kârları (alacak) 50.000',
            'C': '120 Alıcılar (borç) 650.000; 102 Bankalar (alacak) 600.000 ve 646 Kambiyo Kârları (alacak) 50.000',
            'D': '102 Bankalar (borç) 600.000; 120 Alıcılar (alacak) 600.000',
            'E': '102 Bankalar (borç) 650.000; 120 Alıcılar (alacak) 600.000 ve 656 Kambiyo Zararları (alacak) 50.000',
        },
        'B',
        'Tahsil edilen = 20.000 × 32,50 = 650.000 ₺ → **102 Bankalar (borç) 650.000**; kapanan alacak **120 Alıcılar (alacak) 600.000**; aradaki lehte fark **646 Kambiyo Kârları (alacak) 50.000**.',
        "1 Sıra No'lu MSUGT - 102/120/646",
    ),
    # düzey 3
    '0005': patch(
        "Ege Tekstil A.Ş. 50.000 USD tutarında ihracat faturası düzenlemiştir (fatura ve mal çıkış günü kuru 30,00 ₺/USD). Dönem sonunda alacak MB döviz alış kuru 31,00 ₺/USD ile değerlenmiş; izleyen dönemde kur 33,50 ₺/USD iken tahsil edilmiştir. Bu alacaktan iki dönem toplamında doğan kur farkı kârı kaç ₺'dir?",
        {
            'A': '210.000',
            'B': '125.000',
            'C': '175.000',
            'D': '50.000',
            'E': '165.000',
        },
        'C',
        'İki dönemin toplam kur farkı, ilk kayıt kuru (30,00) ile tahsilat kuru (33,50) arasındaki değişimdir: 50.000 × (33,50 − 30,00) = 50.000 × 3,50 = **175.000 ₺**. (Birinci dönem 50.000 × 1,00 = 50.000 ₺ değerleme kârı, ikinci dönem 50.000 × 2,50 = 125.000 ₺ tahsilat kârı olarak yazılır.)',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 646",
    ),
    # düzey 2
    '0006': patch(
        "Kur farklarında 'gerçekleşmiş (realize)' ile 'gerçekleşmemiş (değerleme)' kur farkı ayrımıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Gerçekleşmiş kur farkı, döviz kaleminin tahsil ya da ödenmesiyle doğar',
            'B': 'Gerçekleşmemiş kur farkı, tahsilat veya ödeme anında ortaya çıkan farktır',
            'C': 'Kapanmamış döviz kalemlerinin dönem sonu değerlemesi gerçekleşmemiş fark doğurur',
            'D': 'Her iki tür fark da 646 veya 656 hesaplarında izlenir',
            'E': 'Her iki tür fark da dönemin kâr veya zararını etkiler',
        },
        'B',
        "Gerçekleşmiş kur farkı döviz kaleminin kapanışında (tahsilat/ödeme) doğar; gerçekleşmemiş kur farkı ise henüz kapanmamış döviz kalemlerinin dönem sonunda VUK m. 280'e göre değerlenmesiyle ortaya çıkar. İkisi de 646 Kambiyo Kârları veya 656 Kambiyo Zararları hesaplarında izlenir ve dönem sonucunu etkiler. B şıkkı gerçekleşmiş kur farkının tanımını gerçekleşmemiş için vermektedir.",
        "VUK md. 280; 1 Sıra No'lu MSUGT - 646/656",
    ),
    # düzey 3
    '0007': patch(
        'İhracat ve ithalat yapan bir işletmenin dönem içinde döviz cinsinden alacakları, borçları ve kasasında döviz mevcudu bulunmaktadır. Yönetim, kur hareketlerinin dönem sonucuna etkisini değerlendirmek için aşağıdaki durumları incelemektedir:\n\nI. Döviz cinsi alacak varken kurun yükselmesi\n\nII. Döviz cinsi borç varken kurun yükselmesi\n\nIII. Döviz cinsi alacak varken kurun düşmesi\n\nBu durumlardan hangilerinde işletme lehine (kambiyo kârı, 646) kur farkı doğar?',
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'I ve III',
            'D': 'Yalnız I',
            'E': 'I, II ve III',
        },
        'D',
        "**I** alacak + kur↑ → kâr (646). **II** borç + kur↑ → zarar (656); **III** alacak + kur↓ → zarar (656). Lehte kur farkı yalnız **I**'de doğar.",
        "1 Sıra No'lu MSUGT - 646/656",
    ),
    # düzey 2
    '0008': patch(
        "Bengi Kimya A.Ş. 1 Mart'ta TL hesabındaki parayla 30,00 ₺/USD kurundan 15.000 USD satın alarak döviz tevdiat hesabına yatırmıştır. 1 Haziran'da bu dövizin 5.000 USD'sini 31,00 ₺/USD kurundan bozdurarak TL hesabına aktarmış ve kur farkını kaydetmiştir. Dönem sonunda T.C. Merkez Bankası döviz alış kuru 31,20 ₺/USD'dir.\n\nDönem sonu değerleme kaydı aşağıdakilerden hangisidir?",
        {
            'A': '102 Bankalar (borç) 18.000; 646 Kambiyo Kârları (alacak) 18.000',
            'B': '102 Bankalar (borç) 12.000; 646 Kambiyo Kârları (alacak) 12.000',
            'C': '646 Kambiyo Kârları (borç) 12.000; 102 Bankalar (alacak) 12.000',
            'D': '102 Bankalar (borç) 17.000; 646 Kambiyo Kârları (alacak) 17.000',
            'E': '102 Bankalar (borç) 2.000; 646 Kambiyo Kârları (alacak) 2.000',
        },
        'B',
        "Döviz satın alınması kur farkı doğurmaz. Haziran'da bozdurulan 5.000 USD için 5.000 × (31,00 − 30,00) = 5.000 ₺ kâr o tarihte kaydedilmiştir. Dönem sonunda hesapta kalan 10.000 USD, 30,00 ₺'den kayıtlıdır: 10.000 × (31,20 − 30,00) = 12.000 ₺ değer artışı → 102 borç / 646 alacak.",
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 102/646",
    ),
    # düzey 2
    '0009': patch(
        "Efe Denizcilik A.Ş. dönem sonunda 30.000 USD döviz alacağı ve bir miktar USD döviz borcu taşımaktadır (ikisi de aynı kur değişimine tabidir). Dönem sonunda USD kuru 2,00 ₺ yükselmiş ve kur farklarının dönem sonucuna net etkisi 20.000 ₺ kâr olmuştur. Buna göre döviz borcunun tutarı kaç USD'dir?",
        {
            'A': '10.000',
            'B': '40.000',
            'C': '30.000',
            'D': '50.000',
            'E': '20.000',
        },
        'E',
        'Alacaktan (varlık, kur↑) doğan kâr = 30.000 × 2,00 = 60.000 ₺. Net kâr 20.000 ₺ olduğuna göre borçtan doğan zarar = 60.000 − 20.000 = 40.000 ₺. Borç zararı = tutar × 2,00 olduğundan tutar = 40.000 ÷ 2,00 = **20.000 USD**. (Borçta kur yükselişi zarar doğurur; alacak kârını azaltır.)',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 646/656",
    ),
    # düzey 3
    '0010': patch(
        'Dış ticaretle uğraşan bir işletmenin muhasebe müdürü, dönem sonu değerlemesinden önce döviz cinsi kalemlerin kur değişimlerinden nasıl etkileneceğini aşağıdaki durumlar üzerinden incelemektedir:\n\nI. Kasadaki döviz mevcudu varken kurun yükselmesi\n\nII. Döviz cinsi alacak varken kurun düşmesi\n\nIII. Döviz cinsi borç varken kurun yükselmesi\n\nBu durumlardan hangilerinde işletme aleyhine (kambiyo zararı, 656) kur farkı doğar?',
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'I, II ve III',
            'D': 'I ve II',
            'E': 'I ve III',
        },
        'A',
        "**II** alacak + kur↓ → zarar; **III** borç + kur↑ → zarar; **I** döviz mevcudu (varlık) + kur↑ → KÂR (646). Aleyhte kur farkı yalnızca **II ve III**'de doğar.",
        "1 Sıra No'lu MSUGT - 646/656",
    ),
    # düzey 3
    '0011': patch(
        'İşletmenin 15.000 USD alacağı işlem günü 30,00 ₺/USD ile kaydedilmiş; birinci dönem sonu MB alış kuru 31,00 ₺/USD ile değerlenmiştir. İkinci dönemde alacak, kur 29,00 ₺/USD iken tahsil edilmiştir. İKİNCİ dönemde oluşan kur farkı ve niteliği aşağıdakilerden hangisidir?',
        {
            'A': '15.000 ₺ zarar (656)',
            'B': '45.000 ₺ zarar (656)',
            'C': '30.000 ₺ kâr (646)',
            'D': '30.000 ₺ zarar (656)',
            'E': '15.000 ₺ kâr (646)',
        },
        'D',
        'İkinci dönemin kur farkı, o dönemin BAŞ değeri (birinci dönem sonu 31,00) ile tahsilat kuru (29,00) arasındaki farktan hesaplanır: 15.000 × (29,00 − 31,00) = **−30.000 ₺ zarar (656)**. (Birinci dönemde 15.000 ₺ kâr yazılmıştı; iki dönem birlikte net 15.000 ₺ zarar = 30→29.)',
        "VUK md. 280; 1 Sıra No'lu MSUGT - 656",
    ),
    # düzey 2
    '0012': patch(
        "Hera Kozmetik A.Ş. yurt dışındaki tedarikçisinden 8.000 USD tutarında ticari mal ithal etmiştir. Fatura tarihinde ve malların depoya girdiği gün kur 30,00 ₺/USD'dir; bedel 60 gün vadelidir. Borç, aynı hesap dönemi içinde vadesinde, kurun 31,25 ₺/USD olduğu gün bankadan ödenmiştir (gümrük vergisi ve KDV ihmal).\n\n'153 Ticari Mallar' maliyeti ile ödeme sırasında oluşan kur farkı sırasıyla kaç ₺'dir?",
        {
            'A': '250.000 ₺ maliyet — 10.000 ₺ zarar',
            'B': '240.000 ₺ maliyet — 10.000 ₺ kâr',
            'C': '240.000 ₺ maliyet — 250.000 ₺ zarar',
            'D': '250.000 ₺ maliyet — kur farkı doğmaz',
            'E': '240.000 ₺ maliyet — 10.000 ₺ zarar',
        },
        'E',
        'Mal, giriş günü kuruyla stoklara alınır: 8.000 × 30,00 = **240.000 ₺** (153 Ticari Mallar). Ödeme mal girişinden sonra yapıldığından ödeme kur farkı maliyete eklenmez: 8.000 × (31,25 − 30,00) = 8.000 × 1,25 = **10.000 ₺**; borç + kur yükselişi → **zarar (656)**.',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 153/656",
    ),
    # düzey 2
    '0013': patch(
        "Bengisu Lojistik A.Ş.'nin dönem sonu değerlemesinde döviz cinsi alacağı için 40.000 ₺ kambiyo kârı, döviz cinsi borcu için 25.000 ₺ kambiyo zararı tahakkuk ettirilmiştir. Bu gerçekleşmemiş (değerleme) kur farklarının dönemin gelir tablosuna etkisi nedir?",
        {
            'A': '25.000 ₺ net azalış',
            'B': '15.000 ₺ net artış',
            'C': 'Etkisi yoktur; gerçekleşmediği için sonuç hesaplarına yansımaz.',
            'D': '15.000 ₺ net azalış',
            'E': '65.000 ₺ net artış',
        },
        'B',
        "Değerleme (gerçekleşmemiş) kur farkları da 646/656 sonuç hesaplarında izlenir ve dönem kâr/zararına yansır. Net etki = 40.000 (kâr) − 25.000 (zarar) = **15.000 ₺ net artış**. 'Gerçekleşmedi diye gelir tablosunu etkilemez' görüşü yanlıştır; tahsilat/ödemeyi beklemeden dönem sonucuna girer.",
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 646/656",
    ),
    # düzey 2
    '0014': patch(
        "Ege Tekstil A.Ş. bir ihracat müşterisinden olan 50.000 USD tutarındaki alacağını işlem günü kuru 28,00 ₺/USD ile kaydetmiştir. Birinci dönem sonunda alacak MB döviz alış kuru 30,00 ₺/USD ile değerlenmiştir. Alacak, ikinci dönemin Mart ayında kur 31,50 ₺/USD iken bankaya tahsil edilmiştir.\n\nİkinci dönemde oluşan kur farkı kârı kaç ₺'dir?",
        {
            'A': '75.000',
            'B': '100.000',
            'C': '150.000',
            'D': '175.000',
            'E': '25.000',
        },
        'A',
        'İkinci dönem kur farkı, dönem başı değeri (30,00) ile tahsilat kuru (31,50) arasından: 50.000 × (31,50 − 30,00) = 50.000 × 1,50 = **75.000 ₺ kâr**. (Birinci dönemde 50.000 × 2,00 = 100.000 ₺ kâr ayrıca yazılmıştı.)',
        "VUK md. 280; 1 Sıra No'lu MSUGT - 646",
    ),
    # düzey 2
    '0015': patch(
        "Nazar Gıda A.Ş. yurt dışından aldığı hammadde nedeniyle 25.000 USD tutarında döviz borcu kaydetmiştir (işlem günü kuru 30,00 ₺/USD). Aynı dönem içinde borcun 15.000 USD'lik kısmı kur 32,00 ₺/USD iken banka aracılığıyla ödenmiş, kalan 10.000 USD'nin vadesi izleyen aydadır.\n\nBu kısmi ödemenin yevmiye kaydında aşağıdakilerden hangisi yer alır?",
        {
            'A': '320 Satıcılar (borç) 750.000 ve 656 Kambiyo Zararları (borç) 50.000; 102 Bankalar (alacak) 800.000',
            'B': '102 Bankalar (borç) 480.000; 320 Satıcılar (alacak) 450.000 ve 656 Kambiyo Zararları (alacak) 30.000',
            'C': '320 Satıcılar (borç) 480.000; 102 Bankalar (alacak) 480.000',
            'D': '320 Satıcılar (borç) 450.000 ve 656 Kambiyo Zararları (borç) 30.000; 102 Bankalar (alacak) 480.000',
            'E': '320 Satıcılar (borç) 450.000 ve 646 Kambiyo Kârları (borç) 30.000; 102 Bankalar (alacak) 480.000',
        },
        'D',
        'Ödenen 15.000 × 32,00 = 480.000 ₺ → 102 Bankalar (alacak). Kapanan borç 15.000 × 30,00 = 450.000 ₺ → 320 Satıcılar (borç). Aradaki 15.000 × 2,00 = **30.000 ₺** borç + kur yükselişi → 656 Kambiyo Zararları (borç). Yalnız ödenen kısım işleme girer; borcun tamamı (25.000) üzerinden hesaplamak yanlıştır.',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 320/656/102",
    ),
    # düzey 2
    '0016': patch(
        'İşletme yıl içinde döviz cinsinden bir alacağın tahsilinde 18.000 ₺ lehte kur farkı elde etmiş, kısa vadeli amaçla elde tuttuğu hisse senetlerini de maliyetinin 12.000 ₺ üzerinde bir bedelle satmıştır.\n\nBu sonuçların izlendiği kambiyo kârı (646) ile menkul kıymet satış kârı (645) arasındaki farkla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '646 bir gider, 645 ise bir gelir hesabı olduğundan biri kambiyo zararını diğeri menkul kıymet satış kârını gösterir ve netleştirilir.',
            'B': '645 döviz kurundaki değişimden doğan kur farkını, 646 ise menkul kıymet satış kârını ifade eden birbirine bağlı iki hesaptır.',
            'C': '646 menkul kıymetlerin satış bedeli ile kayıtlı değeri arasındaki farktan; 645 ise döviz kalemlerinin kur değişiminden doğan, kaynakları yer değiştirmiş kavramlardır.',
            'D': '646 da 645 de döviz kurundaki değişimden kaynaklanır; ikisi de olağandışı gelir (67) grubunda birlikte izlenen eşdeğer hesaplardır.',
            'E': '646 döviz cinsi kalemlerin kur değişiminden; 645 ise menkul kıymetlerin (hisse senedi/tahvil) satış bedeli ile kayıtlı değeri arasındaki olumlu farktan doğar.',
        },
        'E',
        '**646 Kambiyo Kârları** döviz kalemlerinin **kur değişiminden**; **645 Menkul Kıymet Satış Kârları** ise menkul kıymetin **satış bedeli − kayıtlı değer** olumlu farkından doğar. İkisi de 64 grubunda ama kaynağı farklıdır.',
        "1 Sıra No'lu MSUGT - 645/646",
    ),
    # düzey 3
    '0017': patch(
        "Pınar Tekstil A.Ş.'nin 30.000 USD tutarındaki borcu 30,00 ₺/USD ile kayıtlıdır. Borcun 10.000 USD'lik kısmı kur 31,00 ₺/USD iken ödenmiş; dönem sonunda kalan borç MB döviz alış kuru 32,00 ₺/USD ile değerlenmiştir. Yalnız dönem sonu değerlemesinde (kalan borç için) oluşan kur farkı kaç ₺'dir?",
        {
            'A': '10.000 ₺ zarar',
            'B': '40.000 ₺ kâr',
            'C': '40.000 ₺ zarar',
            'D': '20.000 ₺ zarar',
            'E': '60.000 ₺ zarar',
        },
        'C',
        "Ödemeden sonra kalan borç 30.000 − 10.000 = 20.000 USD'dir. Bu kalan borç kayıtlı 30,00'dan dönem sonu 32,00'a değerlenir: 20.000 × (32,00 − 30,00) = **40.000 ₺**. Borç + kur yükselişi → **zarar (656)**. Ödenen 10.000 USD'nin farkı ayrıca ödeme gününde hesaplanır; dönem sonu değerlemesine girmez.",
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 656",
    ),
    # düzey 3
    '0018': patch(
        'Aşağıdaki kalemlerden hangileri dönem sonu değerlemesinde kur farkı doğurabilir?\n\nI. Döviz cinsi alıcılar (döviz alacağı)\n\nII. TL cinsi satıcılar (TL borcu)\n\nIII. Bankadaki döviz tevdiat hesabı',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'I ve III',
            'E': 'II ve III',
        },
        'D',
        'Kur farkı yalnızca **döviz (yabancı para) cinsi** kalemlerde doğar: **I** döviz alacağı ve **III** döviz mevduatı. **II** TL cinsi borç olduğundan kur farkı doğurmaz. Doğru cevap **I ve III**.',
        'VUK md. 280',
    ),
    # düzey 2
    '0019': patch(
        "Umut Ambalaj A.Ş.'nin bir ihracat müşterisinden olan döviz cinsi alacağı dönem sonunda MB döviz alış kuruyla değerlenmiştir. Değerleme sonucunda 27.000 ₺ kambiyo zararı doğmuş; alacağın kayıtlı kuru ile değerleme kuru arasındaki fark 1,80 ₺ olarak hesaplanmıştır.\n\nBuna göre alacağın döviz tutarı kaç USD'dir ve kur ne yönde değişmiştir?",
        {
            'A': '15.000 USD — kur düşmüştür',
            'B': '15.000 USD — kur değişmemiştir',
            'C': '15.000 USD — kur yükselmiştir',
            'D': '21.600 USD — kur düşmüştür',
            'E': '48.600 USD — kur düşmüştür',
        },
        'A',
        'Döviz tutarı = 27.000 ÷ 1,80 = **15.000 USD**. Alacakta (varlık) **zarar**, kurun **düşmesiyle** oluşur (alacağın TL karşılığı azalır). Dolayısıyla kur düşmüştür. (Borçta zarar için kurun yükselmesi gerekirdi.)',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 656",
    ),
    # düzey 3
    '0020': patch(
        'Kur farklarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Döviz cinsi borçta kur yükselirse kambiyo kârı (646) doğar.\n\nII. Kambiyo kârı ve zararı gelir tablosunda diğer faaliyetlerden olağan gelir/gider (64/65) grubundadır.\n\nIII. TL cinsi alacak ve borçlarda kur farkı doğmaz.',
        {
            'A': 'I ve II',
            'B': 'I ve III',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'D',
        "Yanlış ifade **I**'dir. Döviz cinsi **borçta kur yükselirse** borcun TL karşılığı artacağından işletme aleyhine **kambiyo zararı (656)** doğar; kambiyo kârı (646) ise kur **düştüğünde** doğar. **II** kambiyo kâr/zararı 646/656 ile 64/65 (diğer faaliyetlerden olağan gelir/gider) grubundadır; **III** kur farkı yalnızca döviz (yabancı para) kalemlerde doğar, TL kalemlerde doğmaz. Doğru cevap **II ve III**.",
        "VUK md. 280; 1 Sıra No'lu MSUGT - 646/656",
    ),
    # düzey 2
    '0021': patch(
        "İşletme yurt içindeki bir müşterisine 10.000 USD + %20 KDV tutarında mal satmıştır; fatura günü kur 30,00 ₺/USD'dir ve faturadaki KDV Türk lirası olarak tahsil edilmiştir. Mal bedeli 10.000 USD, kurun 32,00 ₺/USD olduğu gün tahsil edilmiş; işletme lehine oluşan kur farkı için müşteriye kur farkı faturası düzenlenmiştir.\n\nBuna göre kur farkı faturası nedeniyle '391 Hesaplanan KDV' hesabına yazılacak tutar kaç ₺'dir?",
        {
            'A': '24.000',
            'B': '4.000',
            'C': '6.000',
            'D': '20.000',
            'E': '2.000',
        },
        'B',
        'Tahsilde 10.000 × (32,00 − 30,00) = 20.000 ₺ kur farkı geliri doğar (646). Satıcı lehine oluşan kur farkı KDV matrahına eklenir ve fatura düzenlenir: 20.000 × %20 = 4.000 ₺ hesaplanan KDV (120 borç / 391 alacak).',
        "1 Sıra No'lu MSUGT - 646",
    ),
    # düzey 2
    '0022': patch(
        "İşletme 1 Temmuz'da 30,00 ₺/USD kurundan 20.000 USD, bir yıl vadeli ve yıllık %6 faizli kredi kullanmıştır; faiz ve anapara vade sonunda ödenecektir. 31 Aralık'ta kredi ve altı aylık faiz tahakkuku (600 USD) MB döviz alış kuru 32,00 ₺/USD üzerinden kayıtlara alınmıştır. Ertesi yıl 1 Temmuz'da anapara ile bir yıllık faiz, kurun 33,00 ₺/USD olduğu gün bankadan ödenmiştir.\n\nÖdeme kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '780 Finansman Giderleri hesabı 39.600 ₺ borçlandırılır',
            'B': '656 Kambiyo Zararları hesabı 20.000 ₺ borçlandırılır',
            'C': '300 Banka Kredileri hesabı 660.000 ₺ borçlandırılır',
            'D': '102 Bankalar hesabı 680.400 ₺ alacaklandırılır',
            'E': '656 Kambiyo Zararları hesabı 20.600 ₺ borçlandırılır',
        },
        'E',
        "Kredi 640.000 ₺, faiz tahakkuku 19.200 ₺ ile kayıtlıdır. Ödemede anapara 20.000 × 33 = 660.000 ₺, toplam faiz 1.200 × 33 = 39.600 ₺, bankadan çıkış 699.600 ₺'dir. Kur farkı: anapara 20.000 × 1 = 20.000 ₺ ve tahakkuk etmiş faiz 600 × 1 = 600 ₺, toplam 20.600 ₺ (656). İkinci altı aylık faiz 600 × 33 = 19.800 ₺ (780). Kayıt: 300 640.000 ₺, 381 19.200 ₺, 656 20.600 ₺ ve 780 19.800 ₺ borç / 102 699.600 ₺ alacak.",
        "1 Sıra No'lu MSUGT - 656; VUK md. 280",
    ),
    # düzey 3
    '0023': patch(
        "Deniz İthalat A.Ş.'nin 20.000 USD tutarındaki borcu işlem günü kuru 31,00 ₺/USD iken kaydedilmiş; birinci dönem sonunda MB döviz alış kuru 33,00 ₺/USD ile değerlenmiştir. Borç, ikinci dönemde kur 32,00 ₺/USD iken ödenmiştir. İKİNCİ dönemde oluşan kur farkı ve niteliği aşağıdakilerden hangisidir?",
        {
            'A': '20.000 ₺ kâr — 646 Kambiyo Kârları',
            'B': '40.000 ₺ zarar — 656 Kambiyo Zararları',
            'C': '20.000 ₺ zarar — 656 Kambiyo Zararları',
            'D': '60.000 ₺ zarar — 656 Kambiyo Zararları',
            'E': 'Kur farkı doğmaz',
        },
        'A',
        'İkinci dönemin kur farkı, o dönemin başlangıç değeri (birinci dönem sonu 33,00) ile ödeme kuru (32,00) arasından hesaplanır: 20.000 × (33,00 − 32,00) = **20.000 ₺**. Borç + kur düşüşü → borç daha az TL ile kapanır → **kâr (646)**. Birinci dönemde 20.000 × 2,00 = 40.000 ₺ zarar ayrıca yazılmıştı.',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 646",
    ),
    # düzey 3
    '0024': patch(
        'İşletme yurt dışından aldığı ticari mal için 15.000 EUR satıcı borcunu, malın girişindeki 35,00 ₺/EUR kurundan kaydetmiştir. Borç ilk dönem sonunda MB döviz alış kuru 36,20 ₺/EUR üzerinden değerlenmiştir. İzleyen dönemde kurun 37,00 ₺/EUR olduğu gün borç banka aracılığıyla ödenmiştir.\n\nÖdeme kaydında aşağıdakilerden hangisi yer alır?',
        {
            'A': '320 Satıcılar (borç) 525.000 ve 656 Kambiyo Zararları (borç) 30.000; 102 Bankalar (alacak) 555.000',
            'B': '320 Satıcılar (borç) 543.000 ve 656 Kambiyo Zararları (borç) 12.000; 102 Bankalar (alacak) 555.000',
            'C': '320 Satıcılar (borç) 555.000; 102 Bankalar (alacak) 555.000',
            'D': '320 Satıcılar (borç) 543.000; 102 Bankalar (alacak) 543.000',
            'E': '320 Satıcılar (borç) 525.000 ve 656 Kambiyo Zararları (borç) 18.000; 102 Bankalar (alacak) 543.000',
        },
        'B',
        "İlk dönem sonunda borç 15.000 × 36,20 = 543.000 ₺'ye çıkarılmış, 18.000 ₺ o dönemin kambiyo zararı olmuştur. Ödemede borç bu kayıtlı değerle kapanır; bankadan 15.000 × 37,00 = 555.000 ₺ çıkar, aradaki 12.000 ₺ ödeme döneminin kambiyo zararıdır (656).",
        "1 Sıra No'lu MSUGT - 320/656/102",
    ),
    # düzey 3
    '0025': patch(
        "Poyraz Ticaret A.Ş., daha önce 300.000 ₺ (10.000 USD × 30,00) olarak '320 Satıcılar'a kaydettiği ve malı işletmeye girmiş olan ithalat borcunu, kurun 31,50 ₺/USD olduğu gün banka aracılığıyla ödemiştir. Bu ödemenin yevmiye kaydında aşağıdakilerden hangisi yer alır?",
        {
            'A': '320 Satıcılar (borç) 300.000 ve 153 Ticari Mallar (borç) 15.000; 102 Bankalar (alacak) 315.000',
            'B': '320 Satıcılar (borç) 315.000; 102 Bankalar (alacak) 300.000 ve 646 Kambiyo Kârları (alacak) 15.000',
            'C': '320 Satıcılar (borç) 315.000; 102 Bankalar (alacak) 315.000',
            'D': '320 Satıcılar (borç) 300.000 ve 656 Kambiyo Zararları (borç) 15.000; 102 Bankalar (alacak) 315.000',
            'E': '320 Satıcılar (borç) 300.000 ve 780 Finansman Giderleri (borç) 15.000; 102 Bankalar (alacak) 315.000',
        },
        'D',
        "Ödenen tutar 10.000 × 31,50 = 315.000 ₺, kayıtlı borç 300.000 ₺; aradaki 10.000 × 1,50 = **15.000 ₺** borç + kur yükselişi olduğundan **kambiyo zararıdır**. Mal işletmeye girmiş (stok maliyeti kesinleşmiş) olduğundan fark 153 Ticari Mallar'a eklenmez; 320 Satıcılar (borç) 300.000 ve 656 Kambiyo Zararları (borç) 15.000 karşılığında 102 Bankalar (alacak) 315.000 yazılır.",
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 320/656/102; 213 sayılı VUK md. 280",
    ),
    # düzey 2
    '0026': patch(
        "İşletmenin kasasında yurt dışı seyahatlerden artan 3.000 GBP efektif bulunmaktadır. Değerleme gününde T.C. Merkez Bankası'nın ilan ettiği efektif alış, efektif satış, döviz alış ve döviz satış kurları birbirinden farklıdır.\n\nKasadaki efektif (nakit döviz) mevcudu dönem sonunda değerlenirken hangi kur kullanılır?",
        {
            'A': 'MB efektif alış kuru',
            'B': 'MB döviz satış kuru',
            'C': 'Serbest piyasa satış kuru',
            'D': 'İşlem günü kuru (değerleme yapılmaz)',
            'E': 'MB döviz satış kurunun iki katı',
        },
        'A',
        'Kasadaki **efektif (nakit döviz)** mevcudu dönem sonunda **MB efektif alış kuru** ile değerlenir. (Banka mevduatı/alacak-borç için döviz alış kuru; efektif kasa için efektif alış kuru esas alınır.)',
        'VUK md. 280 (efektif alış kuru)',
    ),
    # düzey 2
    '0027': patch(
        'Kambiyo kârları (646) ve kambiyo zararları (656) gelir tablosunda hangi bölümde yer alır?',
        {
            'A': 'Diğer faaliyetlerden olağan gelir ve kârlar (64) / gider ve zararlar (65) içinde',
            'B': 'Faaliyet giderleri (63) ile satışların maliyeti (62) grubu içinde yer alır',
            'C': 'Olağandışı gelir ve kârlar (67) ile olağandışı gider ve zararlar (68) grubu içinde',
            'D': 'Finansman giderleri (66) ile brüt satışlardan indirimler (61) grubu içinde',
            'E': 'Net satışlar (60) ile satış indirimleri kaleminde netleştirilerek gösterilir',
        },
        'A',
        'Kambiyo kârları **646** → 64 Diğer Faaliyetlerden Olağan Gelir ve Kârlar; kambiyo zararları **656** → 65 Diğer Faaliyetlerden Olağan Gider ve Zararlar. Finansman gideri (66) veya olağandışı (67/68) değildir.',
        "1 Sıra No'lu MSUGT - 64/65",
    ),
    # düzey 3
    '0028': patch(
        'Çınar Mobilya A.Ş. dönem sonunda 20.000 USD tutarında döviz alacağı (kayıt 30,00 ₺/USD; dönem sonu 31,50 ₺/USD) ve 10.000 EUR tutarında döviz borcu (kayıt 35,00 ₺/EUR; dönem sonu 36,00 ₺/EUR) taşımaktadır. Kur farklarının dönem sonucuna NET etkisi nedir?',
        {
            'A': '20.000 ₺ net zarar',
            'B': '30.000 ₺ net kâr',
            'C': '20.000 ₺ net kâr',
            'D': '10.000 ₺ net zarar',
            'E': '40.000 ₺ net kâr',
        },
        'C',
        'Her kalem kendi para birimiyle ayrı değerlenir. Alacak (USD, varlık): 20.000 × (31,50 − 30,00) = 30.000 ₺ **kâr**. Borç (EUR): 10.000 × (36,00 − 35,00) = 10.000 ₺ **zarar**. Net etki = 30.000 − 10.000 = **20.000 ₺ net kâr**. Kalemler farklı dövizde olsa da kayıtları ayrıdır; yalnız dönem sonucuna etkileri netleşir.',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 646/656",
    ),
    # düzey 3
    '0029': patch(
        "Gökçe Tarım A.Ş.'nin 40.000 USD tutarındaki alacağı işlem günü 30,00 ₺/USD ile kaydedilmiş; birinci dönem sonunda MB döviz alış kuru 31,00 ₺/USD ile değerlenmiştir. İkinci dönemde alacağın 25.000 USD'lik kısmı, kur 32,00 ₺/USD iken tahsil edilmiştir. Bu kısmi tahsilatta (ikinci dönemde) oluşan kur farkı kârı kaç ₺'dir?",
        {
            'A': '75.000',
            'B': '30.000',
            'C': '50.000',
            'D': '40.000',
            'E': '25.000',
        },
        'E',
        'İkinci dönemin kur farkı, tahsil edilen kısım için dönem başı değeri (31,00) ile tahsilat kuru (32,00) arasından hesaplanır: 25.000 × (32,00 − 31,00) = **25.000 ₺ kâr**. Birinci dönemde 40.000 × 1,00 = 40.000 ₺ değerleme kârı ayrıca yazılmıştı; kalan 15.000 USD için tahsilat henüz yoktur.',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 646",
    ),
    # düzey 2
    '0030': patch(
        'Bir işletme yurt dışından alacağı bir üretim makinesini döviz cinsi yatırım kredisiyle finanse etmiştir. Makine montaj ve deneme çalışmalarından sonra Haziran ayında kullanıma hazır hâle gelmiş ve aktifleştirilmiştir; kredinin geri ödemesi üç yıl sürecektir ve kur bu süre içinde yükselmeye devam etmektedir.\n\nAktifleştirmeden sonra kredinin döviz kurundaki artıştan doğan kur farklarıyla ilgili genel uygulama aşağıdakilerden hangisidir?',
        {
            'A': 'Bu kur farkları sonuç hesaplarına yansıtılmaz; sermaye yedekleri içinde bilançoda bekletilir.',
            'B': 'Aktifleştirmeden sonraki dönemlerde de kur farkları, makinenin (253) maliyetine kesintisiz olarak eklenmeye devam edilir ve amortismana tabi tutulur.',
            'C': 'Aktifleştirmeden sonraki döneme ait kur farkları, maliyete eklenmeyip dönemin kambiyo gideri/geliri (656/646) olarak yazılabilir.',
            'D': 'Sonraki dönem kur farkları doğrudan 257 Birikmiş Amortismanlar hesabına eklenerek amortisman tutarını azaltır.',
            'E': 'Aktifleştirme sonrası kur farklarının tamamı 280 Gelecek Yıllara Ait Giderler hesabına aktarılır.',
        },
        'C',
        'Kur farkları yalnızca **aktifleştirmeye kadar** maliyete eklenir. Aktifleştirmeden **sonraki** dönemlere ait kur farkları, maliyete eklenmeyip **kambiyo gideri/geliri (656/646)** olarak yazılabilir. Belirleyici olan zamanlamadır.',
        'VUK md. 280; MDV kur farkı',
    ),
    # düzey 2
    '0031': patch(
        'İşletme, bankadaki TL hesabından 10.000 USD satın alıp döviz tevdiat (banka döviz) hesabına aktarmıştır (kur 31,00 ₺/USD). Bu işlemin niteliği ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşlem gelir tablosunu doğrudan etkiler; alınan dövizin TL karşılığı 646 Kambiyo Kârları hesabına gelir olarak kaydedilir.',
            'B': 'Satın alınan döviz bir varlık değil gider sayıldığından, ödenen TL tutarı 656 Kambiyo Zararları hesabına gider yazılır.',
            'C': 'Bir varlık (TL) başka bir varlığa (döviz) dönüşür; alım anında kur farkı doğmaz, kur farkı sonraki değerleme/elden çıkarmada oluşur.',
            'D': 'Döviz alımı anında, alış kuru ile satış kuru arasındaki fark kadar mutlaka kambiyo kârı ya da zararı doğar ve tutar 646 veya 656 hesabına kaydedilir.',
            'E': 'Döviz alım işlemi bir varlık dönüşümü olmadığından kaydedilmez; muhasebe kaydı dövizin bozdurulduğu anda yapılır.',
        },
        'C',
        'Döviz alımında sadece **varlık dönüşümü** olur (102 TL hesabı azalır, 102/108 döviz hesabı artar). Alım anında kur farkı **doğmaz**; kur farkı ancak dövizin **sonraki değerleme/elden çıkarılmasında** oluşur.',
        "VUK md. 280; 1 Sıra No'lu MSUGT - 102/108",
    ),
    # düzey 2
    '0032': patch(
        "İşletme, yurt dışından 10.000 USD tutarında ticari mal ithal etmiş (fatura günü kuru 30,00 ₺/USD, mal aynı gün işletmeye girmiştir). Borç, malın girişinden SONRA kurun 31,20 ₺/USD olduğu gün ödenmiştir. Ödeme sırasında oluşan 12.000 ₺'lik kur farkı nasıl muhasebeleştirilir?",
        {
            'A': "Ödeme yapılana kadar 320 Satıcılar'da bekletilir, sonuç hesabına yansımaz.",
            'B': "Lehte fark sayılıp 646 Kambiyo Kârları'na gelir olarak kaydedilir.",
            'C': "Mal işletmeye girmiş olsa da bu fark 153 Ticari Mallar'ın maliyetine eklenir.",
            'D': 'İthalata ilişkin olduğu için 191 İndirilecek KDV hesabına eklenir.',
            'E': "Malın girişinden sonra doğduğu için 656 Kambiyo Zararları'na gider yazılır.",
        },
        'E',
        "Kur farkı = 10.000 × (31,20 − 30,00) = 12.000 ₺. Mal zaten işletmeye **girmiş** olduğundan (stok maliyeti kesinleşmiş), sonraki ödeme kur farkı **maliyete eklenmez**; borç + kur↑ olduğundan **656 Kambiyo Zararları**'na yazılır.",
        'VUK md. 280; stok kur farkı',
    ),
    # düzey 3
    '0033': patch(
        'Dönem sonu döviz değerlemesiyle ilgili aşağıdaki ifadelerden hangisi YANLIŞTIR?',
        {
            'A': 'TL cinsi alacak ve borçlarda kur farkı doğmaz.',
            'B': 'Döviz cinsi kalemler dönem sonunda MB döviz satış kuruyla değerlenir.',
            'C': 'Kasadaki efektif döviz, MB efektif alış kuruyla değerlenir.',
            'D': 'Değerleme farkı lehteyse 646, aleyhteyse 656 hesabına yazılır.',
            'E': 'Döviz cinsi alacak ve borçlar kural olarak MB döviz alış kuruyla değerlenir.',
        },
        'B',
        'VUK md. 280 uyarınca dövizler, borsa rayici yoksa kural olarak **Merkez Bankası döviz ALIŞ kuruyla** değerlenir; satış kuru esas alınmaz. Bu nedenle satış kurundan söz eden ifade yanlıştır. Kasadaki efektifte efektif alış kuru, lehte/aleyhte farkta 646/656 kullanılması ve TL kalemlerde kur farkı doğmaması doğrudur.',
        '213 sayılı VUK md. 280',
    ),
    # düzey 2
    '0034': patch(
        "İşletme, üretim makinesini 40.000 USD'ye döviz kredisiyle almıştır (fatura günü kuru 30,00 ₺/USD). Makine, kurun 30,50 ₺/USD olduğu gün kullanıma hazır hâle gelmiş (aktifleştirilmiş)tir. Aktifleştirmeye kadar oluşan kur farkı maliyete eklendiğine göre, makinenin '253' hesabındaki toplam maliyeti kaç ₺'dir?",
        {
            'A': '1.200.000',
            'B': '20.000',
            'C': '1.240.000',
            'D': '1.220.000',
            'E': '1.180.000',
        },
        'D',
        'İlk maliyet = 40.000 × 30,00 = 1.200.000 ₺. Aktifleştirmeye kadar kur farkı = 40.000 × (30,50 − 30,00) = 20.000 ₺ (maliyete eklenir). Toplam maliyet = 1.200.000 + 20.000 = **1.220.000 ₺**.',
        "VUK md. 280; 1 Sıra No'lu MSUGT - 253",
    ),
    # düzey 3
    '0035': patch(
        "Dış ticaret yapan bir işletmenin dönem sonunda müşterilerinden 20.000 USD alacağı, satıcılarına 8.000 USD borcu ve kasasında 5.000 USD efektifi vardır; hepsi 30,00 ₺/USD kurla kayıtlıdır. Dönem sonunda MB döviz alış kuru ve efektif alış kuru 31,00 ₺/USD'dir.\n\nKur farklarının dönem sonucuna net etkisi nedir?",
        {
            'A': '25.000 ₺ net kâr',
            'B': '33.000 ₺ net kâr',
            'C': '17.000 ₺ net zarar',
            'D': '8.000 ₺ net zarar',
            'E': '17.000 ₺ net kâr',
        },
        'E',
        'Kur artışı 1,00 ₺. Alacak: 20.000 KÂR. Kasa döviz (varlık): 5.000 KÂR. Borç: 8.000 ZARAR. Net = (20.000 + 5.000) − 8.000 = **17.000 ₺ net kâr**. Varlıklarda kur↑ → kâr, borçta kur↑ → zarar.',
        "1 Sıra No'lu MSUGT - 646/656",
    ),
    # düzey 2
    '0036': patch(
        "Orkun Madencilik A.Ş. döviz cinsi bir borcunu öderken 33.000 ₺ kambiyo zararı ile karşılaşmış; bu sırada kur 1,50 ₺ değişmiştir. Borcun döviz tutarı kaç USD'dir ve kur ne yönde değişmiştir?",
        {
            'A': '22.000 USD — kur yükselmiştir',
            'B': '49.500 USD — kur yükselmiştir',
            'C': '14.667 USD — kur yükselmiştir',
            'D': '22.000 USD — kur değişmemiştir',
            'E': '22.000 USD — kur düşmüştür',
        },
        'A',
        'Döviz tutarı = kur farkı ÷ birim kur değişimi = 33.000 ÷ 1,50 = **22.000 USD**. Borçta **zarar**, ancak kurun **yükselmesiyle** oluşur (borcun TL karşılığı artar). Dolayısıyla kur yükselmiştir. (Alacakta zarar için kurun düşmesi gerekirdi — yön çeldiricisi.)',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 656",
    ),
    # düzey 2
    '0037': patch(
        "30.000 USD alacak işlem günü 30,00 ₺/USD ile kaydedilmiş; birinci dönem sonu 31,00 ₺/USD ile değerlenip kur farkı kârı yazılmıştır. İkinci dönemde alacak, kur 32,00 ₺/USD iken tahsil edilmiştir. İkinci dönemde ek olarak yazılacak kambiyo kârı kaç ₺'dir?",
        {
            'A': '0',
            'B': '90.000',
            'C': '30.000',
            'D': '15.000',
            'E': '60.000',
        },
        'C',
        'Birinci dönemde 30→31 için 30.000 ₺ kâr yazıldı. İkinci dönemde ek kâr = dönem başı 31,00 ile tahsilat 32,00 arasından: 30.000 × (32,00 − 31,00) = **30.000 ₺**. (Toplam iki dönem 60.000 ₺.)',
        "VUK md. 280; 1 Sıra No'lu MSUGT - 646",
    ),
    # düzey 2
    '0038': patch(
        "Rüzgar Otomotiv A.Ş. yurt dışındaki bir bayisine yaptığı yedek parça ihracatından doğan 20.000 USD tutarındaki alacağını 32,00 ₺/USD ile kaydetmiştir. Dönem sonuna kadar tahsilat yapılmamış; dönem sonunda MB döviz alış kuru 30,50 ₺/USD'ye gerilemiştir.\n\nBu değerlemenin yevmiye kaydında aşağıdakilerden hangisi yer alır?",
        {
            'A': '120 Alıcılar (borç) 30.000; 656 Kambiyo Zararları (alacak) 30.000',
            'B': '656 Kambiyo Zararları (borç) 30.000; 642 Faiz Gelirleri (alacak) 30.000',
            'C': '120 Alıcılar (borç) 30.000; 646 Kambiyo Kârları (alacak) 30.000',
            'D': '656 Kambiyo Zararları (borç) 610.000; 120 Alıcılar (alacak) 610.000',
            'E': '656 Kambiyo Zararları (borç) 30.000; 120 Alıcılar (alacak) 30.000',
        },
        'E',
        'Kur farkı = 20.000 × (32,00 − 30,50) = 20.000 × 1,50 = **30.000 ₺**. Alacak (varlık) + kur düşüşü → alacağın TL değeri azalır: 656 Kambiyo Zararları (borç) 30.000 / 120 Alıcılar (alacak) 30.000. Alacak alacaklandırılarak azaltılır; kaydedilen yalnız fark tutarıdır (610.000 değil).',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 120/656",
    ),
    # düzey 3
    '0039': patch(
        'Bir işletmenin dönem sonunda 30.000 USD döviz borcu (kayıt 30,00 ₺/USD) ve 30.000 USD döviz alacağı (kayıt 30,00 ₺/USD) vardır. Dönem sonu kur 32,00 ₺/USD olduğunda kur farklarının net etkisi nedir?',
        {
            'A': 'Net 32.000 ₺ zarardır (dönem sonu kur esas alınır)',
            'B': 'Net etki sıfırdır (alacak kârı ile borç zararı eşit)',
            'C': 'Net 120.000 ₺ kârdır (alacak ve borç toplanır)',
            'D': 'Net 60.000 ₺ zarardır (borç dikkate alınır, alacak alınmaz)',
            'E': 'Net 60.000 ₺ kârdır (alacak dikkate alınır, borç alınmaz)',
        },
        'B',
        'Alacak: 30.000 × 2,00 = 60.000 ₺ KÂR. Borç: 30.000 × 2,00 = 60.000 ₺ ZARAR. Eşit tutarda döviz alacak ve borç aynı kur değişimine maruz kaldığından net etki = 60.000 − 60.000 = **0 (birbirini götürür)**.',
        "1 Sıra No'lu MSUGT - 646/656",
    ),
    # düzey 2
    '0040': patch(
        'Bir ithalatçı, yurt dışındaki tedarikçisine olan 25.000 USD tutarındaki ticari borcunu işlem günü 30,00 ₺/USD kuruyla kaydetmiştir. Aynı ay içinde, kurun yine 30,00 ₺/USD olduğu bir günde borcun tamamı bankadan ödenmiştir; arada dönem sonu değerlemesi yapılmamıştır.\n\nBu durumda kur farkı ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ödenen tutar üzerinden 656 Kambiyo Zararları çalışır.',
            'B': 'Kayıtlı borç tutarı kadar 646 Kambiyo Kârları yazılır.',
            'C': 'Değişmese de kambiyo kârı tahakkuk eder.',
            'D': 'Kur değişmediği için kur farkı doğmaz; 646/656 çalışmaz.',
            'E': 'Borcun tamamı için 780 Finansman Giderleri kaydedilir.',
        },
        'D',
        'İşlem ve ödeme kuru aynı (30,00) olduğundan **kur farkı doğmaz**; borç kayıtlı değeriyle (750.000 ₺) kapanır, 646/656 çalışmaz. Kur farkı ancak kur DEĞİŞİRSE doğar.',
        'VUK md. 280',
    ),
    # düzey 2
    '0041': patch(
        "İşletme bir müşterisinden 35,00 ₺/EUR kurundan kaydettiği 8.000 EUR'luk bir alacak senedi almıştır. Senedin 3.000 EUR'luk kısmı kurun 36,50 ₺/EUR olduğu gün nakden tahsil edilmiş, kalan 5.000 EUR için yeni bir senet düzenlenmeden mevcut senet portföyde tutulmuştur. Dönem sonunda MB döviz alış kuru 37,00 ₺/EUR'dur.\n\nBuna göre bu senet nedeniyle dönem içinde '646 Kambiyo Kârları' hesabına yazılan toplam tutar kaç ₺'dir?",
        {
            'A': '16.000',
            'B': '14.500',
            'C': '10.000',
            'D': '4.500',
            'E': '12.000',
        },
        'B',
        "Kısmi tahsil: 3.000 × (36,50 − 35,00) = 4.500 ₺ kâr. Dönem sonunda kalan 5.000 EUR 37,00'den değerlenir: 5.000 × (37,00 − 35,00) = 10.000 ₺ kâr. Toplam 14.500 ₺; döviz cinsi senetler de VUK m. 280'e göre MB döviz alış kuruyla değerlenir.",
        "1 Sıra No'lu MSUGT - 656",
    ),
    # düzey 3
    '0042': patch(
        "Ferhat Dış Ticaret A.Ş.'nin 40.000 USD tutarındaki döviz alacağı, işlem günü kuru 30,00 ₺/USD iken kaydedilmiştir. Alacağın yalnız 25.000 USD'lik kısmı, kurun 32,20 ₺/USD olduğu gün banka aracılığıyla tahsil edilmiştir. Bu kısmi tahsilatta oluşan kur farkı ve niteliği aşağıdakilerden hangisidir?",
        {
            'A': '2,20 ₺ kâr — 646 Kambiyo Kârları',
            'B': '33.000 ₺ kâr — 646 Kambiyo Kârları',
            'C': '55.000 ₺ kâr — 646 Kambiyo Kârları',
            'D': '55.000 ₺ zarar — 656 Kambiyo Zararları',
            'E': '88.000 ₺ kâr — 646 Kambiyo Kârları',
        },
        'C',
        'Kısmi tahsilat yalnız tahsil edilen tutar için kur farkı doğurur: 25.000 × (32,20 − 30,00) = 25.000 × 2,20 = **55.000 ₺**. Alacak + kur yükselişi → lehte **kâr (646)**. Kalan 15.000 USD henüz kapanmadığı için bu tutara girmez (40.000 üzerinden 88.000 ₺ hesaplamak yanlıştır).',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 646; 213 sayılı VUK md. 280",
    ),
    # düzey 3
    '0043': patch(
        "Kuzey Enerji A.Ş. dönem sonunda kasasında 5.000 USD efektif (nakit döviz) ve bankada 5.000 USD döviz mevduatı tutmaktadır; ikisi de 30,00 ₺/USD ile kayıtlıdır. Dönem sonunda MB döviz alış kuru 32,00 ₺/USD, MB efektif alış kuru 31,60 ₺/USD'dir. İki kalemin değerlemesinden doğan toplam kur farkı kaç ₺'dir?",
        {
            'A': '8.000 ₺ kâr',
            'B': '10.000 ₺ zarar',
            'C': '16.000 ₺ kâr',
            'D': '20.000 ₺ kâr',
            'E': '18.000 ₺ kâr',
        },
        'E',
        'Kasadaki efektif **efektif alış kuruyla**, bankadaki döviz mevduatı **döviz alış kuruyla** değerlenir. Efektif: 5.000 × (31,60 − 30,00) = 8.000 ₺; mevduat: 5.000 × (32,00 − 30,00) = 10.000 ₺. Toplam = 8.000 + 10.000 = **18.000 ₺ kâr**. İki kaleme tek kur uygulamak (20.000 veya 16.000) yanlıştır.',
        '213 sayılı VUK md. 280',
    ),
    # düzey 2
    '0044': patch(
        'Bir işletme 18.000 USD tutarındaki alacağını tahsil ettiğinde 45.000 ₺ kur farkı kârı elde etmiştir. Buna göre, işlem tarihinden tahsil tarihine kadar USD kuru kaç ₺ artmıştır?',
        {
            'A': '2,50',
            'B': '0,40',
            'C': '0,25',
            'D': '25,00',
            'E': '4,00',
        },
        'A',
        'Kur artışı = Kur farkı ÷ Döviz tutarı = 45.000 ÷ 18.000 = **2,50 ₺**. (Ters/reverse soru: sonuçtan birim kur değişimine ulaşılır.)',
        "1 Sıra No'lu MSUGT - 646",
    ),
    # düzey 2
    '0045': patch(
        'Arda Otomotiv A.Ş., üretim makinesini kullanıma hazır hâle getirip (aktifleştirip) kayıtlarına aldıktan SONRA, makine için 20.000 USD tutarındaki döviz satıcı borcunu ödemiştir. Borç işlem günü 30,00 ₺/USD ile kaydedilmiş, ödeme günü kur 32,00 ₺/USD olmuştur. Aktifleştirmeden sonra doğan bu kur farkı ne tutarda ve nasıl muhasebeleştirilir?',
        {
            'A': "40.000 ₺ — 646 Kambiyo Kârları'na gelir yazılır",
            'B': 'Kur farkı doğmaz; borç kayıtlı değeriyle kapanır',
            'C': "40.000 ₺ — 257 Birikmiş Amortismanlar'a eklenir",
            'D': "40.000 ₺ — 656 Kambiyo Zararları'na gider yazılır",
            'E': "40.000 ₺ — 253 Tesis, Makine ve Cihazlar'ın maliyetine eklenir",
        },
        'D',
        "Kur farkı = 20.000 × (32,00 − 30,00) = **40.000 ₺**. Varlık **aktifleştirildikten sonra** doğan kur farkları maliyete (253) eklenmez; dönemin kambiyo gider/geliri olarak izlenir. Borç + kur yükselişi olduğundan **656 Kambiyo Zararları**'na gider yazılır. (Aktifleştirmeden önce olsaydı maliyete eklenirdi.)",
        "213 sayılı VUK md. 280; 163 Sıra No'lu VUK Genel Tebliği (MDV kur farkı)",
    ),
    # düzey 3
    '0046': patch(
        "İşletme, üretimde kullanacağı bir makineyi 50.000 USD'ye almış; işlem (fatura) günü kuru 30,00 ₺/USD'dir. Makine henüz aktifleştirilmeden (kullanıma hazır olmadan) önce, kurun 30,60 ₺/USD olduğu gün bedel ödenmiştir. Aradaki 30.000 ₺'lik kur farkı nasıl muhasebeleştirilir?",
        {
            'A': 'Tutarı önemsiz sayılıp kaydedilmez; makine fatura günü kuruyla değerlenir.',
            'B': "253 Tesis, Makine ve Cihazlar'ın maliyetine eklenir (aktifleştirmeden önceki dönem kur farkı).",
            'C': '257 Birikmiş Amortismanlar hesabına eklenerek amortisman yoluyla itfa edilir.',
            'D': '656 Kambiyo Zararları hesabına doğrudan gider yazılır ve makinenin maliyetiyle ilişkilendirilmez.',
            'E': '780 Finansman Giderleri hesabına yazılıp dönem sonunda gelir tablosuna aktarılır.',
        },
        'B',
        "Kur farkı = 50.000 × (30,60 − 30,00) = 30.000 ₺. MDV'de, varlığın **aktifleştirildiği döneme kadar** oluşan kur farkları **maliyete eklenir** (253). Sonraki dönem kur farkları ise kambiyo gider/geliri yazılır. (VUK md. 280/163 s. Tebliğ.)",
        'VUK md. 280; MDV kur farkı',
    ),
    # düzey 3
    '0047': patch(
        "Selen Gıda A.Ş. yurt dışına sattığı kuru meyveler nedeniyle 30.000 USD tutarında döviz alacağı kaydetmiştir (işlem günü kuru 30,00 ₺/USD). Aynı dönem içinde alacağın 18.000 USD'lik kısmı, kurun 31,50 ₺/USD olduğu gün banka aracılığıyla TL olarak tahsil edilmiş, kalan kısmın vadesi izleyen aydadır.\n\nBu kısmi tahsilatın yevmiye kaydında aşağıdakilerden hangisi yer alır?",
        {
            'A': '120 Alıcılar (borç) 567.000; 102 Bankalar (alacak) 540.000 ve 646 Kambiyo Kârları (alacak) 27.000',
            'B': '102 Bankalar (borç) 540.000; 120 Alıcılar (alacak) 540.000',
            'C': '102 Bankalar (borç) 567.000; 120 Alıcılar (alacak) 540.000 ve 656 Kambiyo Zararları (alacak) 27.000',
            'D': '102 Bankalar (borç) 567.000; 120 Alıcılar (alacak) 567.000',
            'E': '102 Bankalar (borç) 567.000; 120 Alıcılar (alacak) 540.000 ve 646 Kambiyo Kârları (alacak) 27.000',
        },
        'E',
        "Tahsil edilen 18.000 × 31,50 = 567.000 ₺ → 102 Bankalar (borç). Kapanan alacak 18.000 × 30,00 = 540.000 ₺ → 120 Alıcılar (alacak). Aradaki 18.000 × 1,50 = **27.000 ₺** lehte fark → 646 Kambiyo Kârları (alacak). Kalan 12.000 USD 120 Alıcılar'da izlenmeye devam eder.",
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 102/120/646",
    ),
    # düzey 2
    '0048': patch(
        'Doruk Elektronik A.Ş., yurt dışı fuar dönüşü kasasında kalan 6.000 USD efektifi (kayıtlı kur 30,00 ₺/USD) aynı dönem içinde, kurun 31,80 ₺/USD olduğu gün bankaya bozdurarak TL vadesiz hesabına yatırmıştır (masraf ihmal).\n\nBu işlemin muhasebeleştirilmesiyle ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': '102 Bankalar hesabı 190.800 ₺ borçlandırılır',
            'B': '100 Kasa hesabı 180.000 ₺ alacaklandırılır',
            'C': '646 Kambiyo Kârları hesabı 10.800 ₺ alacaklandırılır',
            'D': '656 Kambiyo Zararları hesabı 10.800 ₺ borçlandırılır',
            'E': 'Kasadan çıkan efektif kayıtlı değeriyle alacaklandırılır',
        },
        'D',
        "TL girişi 6.000 × 31,80 = 190.800 ₺ (102 borç); kasadan çıkan efektif kayıtlı değeriyle 6.000 × 30,00 = 180.000 ₺ (100 alacak); aradaki 10.800 ₺ lehte farktır ve 646 Kambiyo Kârları'na alacak yazılır. Kur yükseldiği için zarar doğmaz; 656 çalışmaz.",
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 100/102/646",
    ),
    # düzey 3
    '0049': patch(
        "Bir işletmenin dönem sonunda 30,00 ₺/USD kurundan kayıtlı 10.000 USD alacağı, 35,00 ₺/EUR kurundan kayıtlı 6.000 EUR satıcı borcu ve kasasında 40,00 ₺/GBP kurundan kayıtlı 2.000 GBP efektifi vardır. Değerleme gününde MB döviz alış kurları 32,00 ₺/USD ve 36,50 ₺/EUR, efektif alış kuru 39,00 ₺/GBP'dir.\n\nBuna göre dönem sonu değerlemesinin dönem sonucuna net etkisi aşağıdakilerden hangisidir?",
        {
            'A': '20.000 ₺ net kâr',
            'B': '9.000 ₺ net kâr',
            'C': '7.000 ₺ net kâr',
            'D': '31.000 ₺ net kâr',
            'E': '13.000 ₺ net kâr',
        },
        'B',
        'USD alacak: 10.000 × 2,00 = 20.000 ₺ kâr (646). EUR borç: kur yükseldiği için 6.000 × 1,50 = 9.000 ₺ zarar (656). GBP efektif: kur düştüğü için 2.000 × 1,00 = 2.000 ₺ zarar (656). Kalemler ayrı kaydedilir; dönem sonucuna net etki 20.000 − 9.000 − 2.000 = 9.000 ₺ kârdır.',
        "1 Sıra No'lu MSUGT - 646/656",
    ),
    # düzey 2
    '0050': patch(
        'Kur farkı ile reeskont arasındaki farkla ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Reeskont, döviz cinsi kalemlerin kur değişiminden doğar ve 646/656'da izlenir",
            'B': 'Kur farkı, döviz cinsi kalemlerin kur değişiminden doğar',
            'C': 'Reeskont, senetli alacak ve borçlardaki faiz unsurunu ayıklar',
            'D': "Alacak senetleri reeskontu 657 Reeskont Faiz Giderleri'ne yazılır",
            'E': "Borç senetleri reeskontu 647 Reeskont Faiz Gelirleri'ne yazılır",
        },
        'A',
        "Kur farkı döviz cinsi kalemlerin kur değişiminden doğar ve 646/656'da izlenir. Reeskont ise senetli alacak ve borçların vade (faiz) unsurunun bugünkü değere indirgenmesidir: alacak senetleri reeskontu 657 Reeskont Faiz Giderleri'ne, borç senetleri reeskontu 647 Reeskont Faiz Gelirleri'ne yazılır. A şıkkı kur farkının tanımını reeskonta yüklemektedir.",
        "VUK md. 280-281; 1 Sıra No'lu MSUGT",
    ),
    # düzey 2
    '0051': patch(
        "Işık Ambalaj A.Ş.'nin dönem sonunda kasasında 12.000 USD efektif bulunmakta, ayrıca yurt dışındaki bir hammadde tedarikçisine 12.000 USD tutarında satıcı borcu vardır. İki kalem de aynı kurla kayıtlıdır ve dönem içinde kur yükselmiştir.\n\nBu iki kalemin muhasebeleştirilmesiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Döviz kasası dönem sonunda efektif alış kuruyla değerlenir',
            'B': 'Satıcı borcu dönem sonunda MB döviz alış kuruyla değerlenir',
            'C': 'Tutarlar eşit olduğundan iki kalem netleştirilir ve değerlenmez',
            'D': 'Döviz kasası ile döviz borcu bilançoda ayrı kalemlerde yer alır',
            'E': 'Kur değişiminin etkisi her kalem için ayrı hesaplanır',
        },
        'C',
        "Varlık ve kaynak kalemleri netleştirilmez (brüt esas). Döviz kasası VUK m. 280'e göre MB efektif alış kuruyla, döviz cinsi borç MB döviz alış kuruyla ayrı ayrı değerlenir; her kalemin kur farkı ayrı hesaplanır ve bilançoda ayrı kalemlerde gösterilir.",
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 100/320",
    ),
    # düzey 2
    '0052': patch(
        'İşletme yurt dışındaki bir satıcıya olan 20.000 USD tutarındaki borcunu ödediğinde 30.000 ₺ kambiyo kârı kaydetmiştir. Borç ödeme gününe kadar değerlemeye tabi tutulmamıştır.\n\nBuna göre işlem gününden ödeme gününe kadar döviz kuru ne yönde değişmiştir?',
        {
            'A': 'Yönü belirlenemez',
            'B': 'Düşmüştür',
            'C': 'Yükselmiştir',
            'D': 'Değişmemiştir',
            'E': 'Önce yükselip sonra aynı kalmıştır',
        },
        'B',
        'Borçta kâr, ancak kurun **düşmesiyle** oluşur (borç daha az TL ile kapanır). Dolayısıyla kur **düşmüştür**. (Alacakta ise kâr için kurun yükselmesi gerekirdi — yön çeldiricisi.)',
        "1 Sıra No'lu MSUGT - 646",
    ),
    # düzey 2
    '0053': patch(
        "Lale İnşaat A.Ş.'nin kasasında 36,00 ₺/EUR kurundan kayıtlı 8.000 EUR efektif bulunmaktadır. Yıl içinde bu efektifin 3.000 EUR'su 35,00 ₺/EUR kurundan bankaya bozdurularak TL hesabına alınmıştır. Dönem sonunda MB efektif alış kuru 34,50 ₺/EUR'dur.\n\nBuna göre bu efektifle ilgili olarak dönem içinde '656 Kambiyo Zararları' hesabına borç yazılan toplam tutar kaç ₺'dir?",
        {
            'A': '12.000',
            'B': '7.500',
            'C': '13.500',
            'D': '10.500',
            'E': '15.000',
        },
        'D',
        "Bozdurma: 3.000 × (36,00 − 35,00) = 3.000 ₺ zarar. Kalan 5.000 EUR dönem sonunda 34,50'den değerlenir: 5.000 × (36,00 − 34,50) = 7.500 ₺ zarar. 656'ya yazılan toplam 10.500 ₺.",
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 100/656",
    ),
    # düzey 3
    '0054': patch(
        'Kur farklarının muhasebeleştirilmesiyle ilgili aşağıdaki ifadelerden hangisi YANLIŞTIR?',
        {
            'A': 'Döviz cinsi borçta kur yükselirse kambiyo kârı doğar.',
            'B': 'Döviz cinsi alacakta kur yükselirse kambiyo kârı doğar.',
            'C': 'MDV alımında aktifleştirmeye kadar oluşan kur farkı maliyete eklenir.',
            'D': 'Lehte kur farkı 646, aleyhte kur farkı 656 hesabında izlenir.',
            'E': 'Dönem sonu değerlemede kural olarak MB döviz alış kuru kullanılır.',
        },
        'A',
        "**YANLIŞ olan D'dir:** Döviz cinsi BORÇTA kur yükselirse borcun TL karşılığı artar → kambiyo **ZARARI (656)** doğar, kâr değil. Diğer ifadeler doğrudur.",
        "VUK md. 280; 1 Sıra No'lu MSUGT - 646/656",
    ),
    # düzey 2
    '0055': patch(
        'Maya Turizm A.Ş., bankadaki TL hesabından 20.000 USD satın alarak döviz mevduat hesabına aktarmıştır (işlem kuru 31,00 ₺/USD). Bu işlemin yevmiye kaydında aşağıdakilerden hangisi yer alır?',
        {
            'A': '102 Bankalar-Döviz (borç) 620.000; 102 Bankalar-TL (alacak) 600.000 ve 646 Kambiyo Kârları (alacak) 20.000',
            'B': '102 Bankalar-Döviz (borç) 620.000; 102 Bankalar-TL (alacak) 620.000',
            'C': '102 Bankalar-TL (borç) 620.000; 102 Bankalar-Döviz (alacak) 620.000',
            'D': '102 Bankalar-Döviz (borç) 620.000; 646 Kambiyo Kârları (alacak) 620.000',
            'E': '656 Kambiyo Zararları (borç) 620.000; 102 Bankalar-TL (alacak) 620.000',
        },
        'B',
        'Döviz alımı yalnızca bir varlığın (TL) başka bir varlığa (döviz) dönüşmesidir; alım anında kur farkı **doğmaz**. TL hesabından 20.000 × 31,00 = 620.000 ₺ çıkar, döviz mevduatına aynı tutar girer: 102 Bankalar-Döviz (borç) 620.000 / 102 Bankalar-TL (alacak) 620.000. Kur farkı ancak sonraki değerleme veya elden çıkarmada oluşur.',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 102",
    ),
    # düzey 3
    '0056': patch(
        'Kur farklarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Döviz cinsi alacakta kur yükselirse kambiyo kârı (646) doğar.\n\nII. MDV alımında aktifleştirmeden sonraki kur farkları maliyete eklenmeyip kambiyo gider/geliri yazılabilir.\n\nIII. Dönem sonu değerlemede kural olarak MB döviz satış kuru esas alınır.',
        {
            'A': 'I ve II',
            'B': 'I ve III',
            'C': 'II ve III',
            'D': 'I, II ve III',
            'E': 'Yalnız I',
        },
        'A',
        '**III yanlıştır:** VUK md. 280 uyarınca dövizler, borsa rayici yoksa **Merkez Bankası döviz alış kuru** ile değerlenir; satış kuru esas alınmaz. **I** alacakta kur yükselince lehe fark 646 kambiyo kârı doğar; **II** aktifleştirmeden sonraki kur farkları maliyete eklenmeyip kambiyo gider/geliri (656/646) yazılabilir. Doğru cevap **I ve II**.',
        "VUK md. 280; 1 Sıra No'lu MSUGT - 646/656",
    ),
    # düzey 2
    '0057': patch(
        "Bir işletmede döviz kurundaki artış nedeniyle 40.000 ₺ kambiyo KÂRI doğmuştur ve ilgili döviz tutarı 20.000 USD'dir. Buna göre bu kâr aşağıdaki hangi kalemden kaynaklanıyor olabilir?",
        {
            'A': 'Döviz cinsi bir borçtan (kurun yükselmesi nedeniyle)',
            'B': 'TL cinsi bir borçtan (ödeme kolaylaştığı için)',
            'C': 'Bir dönem gideri tahakkukundan (kur etkisiyle)',
            'D': 'TL cinsi bir alacaktan (kur farkı doğmasa da)',
            'E': 'Döviz cinsi bir alacaktan (veya döviz mevcudundan)',
        },
        'E',
        'Kur ARTMIŞ ve KÂR doğmuşsa, kalem bir **döviz alacağı veya döviz mevcudu** (varlık) olmalıdır (varlık + kur↑ → kâr). Borçta kur↑ zarar doğururdu; TL kalemlerde kur farkı doğmaz. (Birim kur = 40.000/20.000 = 2,00 ₺ artış.)',
        "1 Sıra No'lu MSUGT - 646",
    ),
    # düzey 3
    '0058': patch(
        'Sıla Elektronik A.Ş. dönem sonunda 15.000 USD döviz alacağı, 15.000 USD döviz borcu ve kasasında 5.000 USD efektif taşımaktadır (hepsi 30,00 ₺/USD ile kayıtlı). Dönem sonu MB döviz alış kuru 32,00 ₺/USD olduğunda kur farklarının dönem sonucuna net etkisi nedir?',
        {
            'A': '10.000 ₺ net zarar',
            'B': '40.000 ₺ net kâr',
            'C': '10.000 ₺ net kâr',
            'D': '70.000 ₺ net kâr',
            'E': 'Net etki sıfırdır',
        },
        'C',
        'Kur artışı 2,00 ₺. Varlıklar kâr, borç zarar doğurur: alacak 15.000 × 2,00 = 30.000 ₺ kâr; efektif kasa 5.000 × 2,00 = 10.000 ₺ kâr; borç 15.000 × 2,00 = 30.000 ₺ zarar. Net = (30.000 + 10.000) − 30.000 = **10.000 ₺ net kâr**. Alacak ile borç eşit olduğundan birbirini götürür; net etkiyi kasa yaratır.',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 646/656",
    ),
    # düzey 2
    '0059': patch(
        "Toros Mermer A.Ş. ihracat bedellerini döviz tevdiat hesabında tutmaktadır. Bu hesapta 30,00 ₺/USD ile izlenen 20.000 USD'nin tamamı, vergi ödemeleri için kurun 31,90 ₺/USD olduğu gün bozdurularak TL vadesiz hesaba aktarılmıştır (masraf ihmal).\n\nBu işlemde oluşan kambiyo kârı ile TL girişi sırasıyla kaç ₺'dir?",
        {
            'A': '380.000 ₺ kâr — 638.000 ₺ giriş',
            'B': '38.000 ₺ kâr — 600.000 ₺ giriş',
            'C': '38.000 ₺ zarar — 638.000 ₺ giriş',
            'D': '38.000 ₺ kâr — 638.000 ₺ giriş',
            'E': '1,90 ₺ kâr — 638.000 ₺ giriş',
        },
        'D',
        'TL girişi = 20.000 × 31,90 = **638.000 ₺**. Kayıtlı değer 20.000 × 30,00 = 600.000 ₺. Kambiyo kârı = 638.000 − 600.000 = 20.000 × 1,90 = **38.000 ₺**. Döviz elden çıkarılırken kur yükseldiği için kâr doğar (646).',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 102/646",
    ),
    # düzey 2
    '0060': patch(
        "İşletme 10.000 USD tutarında ticari malı ithal etmiştir; malın gümrükten çekilip işletmeye girdiği gün kur 30,00 ₺/USD'dir. İthalat sırasında 15.000 ₺ gümrük vergisi ödenmiş, malın gümrükten depoya taşınması için nakliyeciye 3.000 ₺ ödenmiştir. Satıcıya olan döviz borcu sonraki döneme bırakılmıştır. KDV ihmal edilecektir.\n\nBuna göre '153 Ticari Mallar' hesabına kaydedilecek maliyet kaç ₺'dir?",
        {
            'A': '300.000',
            'B': '303.000',
            'C': '318.000',
            'D': '315.000',
            'E': '330.000',
        },
        'C',
        'İthal edilen malın maliyeti, malın işletmeye girdiği günkü kurla hesaplanan bedel ile malı kullanıma hazır hâle getiren giderlerden oluşur: 10.000 × 30,00 = 300.000 ₺ + gümrük vergisi 15.000 ₺ + nakliye 3.000 ₺ = 318.000 ₺.',
        "VUK md. 280; 1 Sıra No'lu MSUGT - 153",
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
    print(f"1 paket / {len(PATCHES)} soru ('Kur Farklari' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
