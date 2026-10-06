#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hazir Degerler — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.  FM cok adimli tur. 45 soru korundu; 5 TMS 7 sorusu ve 10 tek adimli kayit/ezber sorusu cikarildi. Icerik hatasi duzeltildi: is icin verilen avans 196 Personel Avanslari'na yaziliyordu, dogrusu 195 Is Avanslari (0035 duzeltildi, 0030 degistirildi). Yerine gercek sinav kalibinda 15 soru: nakit+kredi karti+cekle satis ve kredi karti tahsilati, banka mutabakatinda hatali kayit duzeltmesi, dovizde bozdurma ve degerleme kari, dovizle satici odemesi, mevduat faizinde stopaj (193), is avansinin kapatilmasi, ucret avansi ve maasta mahsubu, karsiliksiz cekten senede, hazir degerler toplami, onculler. Kor ogrenci %20. Duzeltme: cozumlerdeki '**X yanlistir**' harf atiflari kaldirildi (yeniden harflendirmede yanlis sikki gosteriyordu).

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: VUK m. 280 · Tekduzen Hesap Plani 10 Hazir Degerler, 195, 196, 335, 193, 646, 656 · 1 Sira No'lu MSUGT
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/finansal_muhasebe/hazir_degerler.json"
STYLE_REF = 'SGS Finansal Muhasebe (çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "finmuh-hazirdeg-gen-"


def patch(stem, options, answer, solution, ref='Tekduzen Hesap Plani 10 Hazir Degerler'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Ay sonu kasa sayımında 100 Kasa hesabının kayıtlı mevcudu 48.300 ₺, fiilî mevcudu 47.100 ₺ bulunmuştur. İncelemede, satılan malların müşterilere gönderimi için kargo firmasına nakden ödenen 900 ₺'nin belgesi bulunduğu hâlde kayda alınmadığı anlaşılmış; kalan farkın nedeni ise belirlenememiştir. KDV ihmal edilecektir.\n\nBuna göre yapılacak kayıtlarda aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '197 Sayım ve Tesellüm Noksanları hesabı 1.200 ₺ borçlandırılır',
            'B': '760 Pazarlama Satış ve Dağıtım Giderleri hesabı 900 ₺ alacaklandırılır',
            'C': '197 Sayım ve Tesellüm Noksanları hesabı 300 ₺ borçlandırılır',
            'D': '100 Kasa hesabı 300 ₺ borçlandırılır',
            'E': '689 Diğer Olağandışı Gider ve Zararlar hesabı 1.200 ₺ borçlandırılır',
        },
        'C',
        "Kasa noksanı 48.300 − 47.100 = 1.200 ₺'dir. Nedeni belli olan 900 ₺ satış gönderim gideri olarak kaydedilir: 760 borç / 100 alacak. Nedeni bilinmeyen 300 ₺ araştırma sonuçlanıncaya kadar 197 Sayım ve Tesellüm Noksanları'nda izlenir: 197 borç / 100 alacak.",
        "1 Sıra No'lu MSUGT - 197 Sayım ve Tesellüm Noksanları",
    ),
    # düzey 2
    '0002': patch(
        "'103 Verilen Çekler ve Ödeme Emirleri (-)' hesabının niteliği ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Bilanço ve gelir tablosu dışında sadece nazım hesaplarda izlenen ve mizanda yer almayan bir hesaptır.',
            'B': 'Aktifi düzenleyici (kontr aktif) bir hesaptır; alacak kalanı verir ve bilançoda hazır değerlerden (-) düşülür.',
            'C': 'Bilançonun pasifinde yer alan bir kaynak (borç) hesabıdır; borç kalanı verir ve kısa vadeli yabancı kaynaklar içinde gösterilir.',
            'D': 'Üretilen mamullere yüklenen çek ödemelerini toplayan bir maliyet hesabıdır; borç kalanı verir ve stok maliyetine eklenir.',
            'E': 'Dönem içinde ödenen çek tutarlarını izleyen bir gider hesabıdır; borç kalanı verir ve gelir tablosuna aktarılır.',
        },
        'B',
        '103, dönen varlıklar içinde yer alan **aktifi düzenleyici** bir hesaptır; **alacak kalanı** verir ve bilançoda hazır değerler tutarından **eksi (-)** gösterilir; henüz bankadan ödenmemiş çek tutarını temsil eder.',
        "1 Sıra No'lu MSUGT - Aktifi düzenleyici hesaplar",
    ),
    # düzey 2
    '0003': patch(
        "Vergi Usul Kanunu'na göre değerleme ölçüleri ile ilgili aşağıdaki eşleştirmelerden hangisi doğrudur?",
        {
            'A': 'Kasadaki Türk Lirası → itibari (nominal) değer; yabancı paralar → borsa rayici/Maliye Bakanlığı kuru',
            'B': 'Kasadaki yabancı paralar → itibari (nominal) değer; Türk Lirası kasa mevcudu → borsa rayici ile değerlenir',
            'C': 'Kasadaki Türk Lirası → maliyet bedeli; kasadaki yabancı paralar → emsal bedel ile değerlenir',
            'D': 'Kasadaki Türk Lirası → borsa rayici; kasadaki yabancı paralar → itibari (nominal) değer ile değerlenir',
            'E': 'Kasadaki yabancı paralar → tasfiye değeri; Türk Lirası kasa mevcudu → rayiç bedel ile değerlenir',
        },
        'A',
        "VUK'a göre Türk Lirası kasa mevcudu **itibari (nominal) değer** (md. 284) ile; yabancı paralar **borsa rayici**, yoksa **Maliye Bakanlığı'nca tespit edilen kur** (md. 280) ile değerlenir.",
        'VUK md. 280 ve 284',
    ),
    # düzey 2
    '0004': patch(
        "İşletme, müşterisinden aldığı ve keşide tarihine 60 gün bulunan 50.000 ₺'lik bir çeki nakit ihtiyacı nedeniyle bankada iskonto ettirmiştir. Banka 1.500 ₺ iskonto faizi ile 50 ₺ işlem masrafını keserek kalan tutarı işletmenin vadesiz hesabına aktarmıştır. İşletme 7/A seçeneğini uygulamaktadır.\n\nBu işlemin kaydında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '101 Alınan Çekler hesabı 48.450 ₺ alacaklandırılır',
            'B': '780 Finansman Giderleri hesabı 1.500 ₺ borçlandırılır',
            'C': '656 Kambiyo Zararları hesabı 1.500 ₺ borçlandırılır',
            'D': '121 Alacak Senetleri hesabı 50.000 ₺ alacaklandırılır',
            'E': '102 Bankalar hesabı 50.000 ₺ borçlandırılır',
        },
        'B',
        'Çek nominal değeriyle portföyden çıkar (101 alacak 50.000 ₺). Bankanın kestiği iskonto faizi finansman maliyetidir (780 borç 1.500 ₺), işlem masrafı komisyon gideridir (653 borç 50 ₺). Hesaba geçen 48.450 ₺ (102 borç).',
        "1 Sıra No'lu MSUGT - 101 Alınan Çekler (ciro)",
    ),
    # düzey 3
    '0005': patch(
        "'100 Kasa' hesabının işleyişi ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
        {
            'A': 'Nakit girişleri hesabın borç tarafına kaydedilir.',
            'B': 'Nakit çıkışları hesabın alacak tarafına kaydedilir.',
            'C': 'Bir aktif (varlık) hesabıdır.',
            'D': "Hesap alacak kalanı vererek 'eksi kasa' durumu gösterebilir.",
            'E': 'Hesap normalde borç kalanı verir.',
        },
        'D',
        'Kasa hesabı **alacak kalanı veremez** (olmayan para ödenemez). Kaydi kasanın fiiliden yüksek olması genelde belgesiz/örtülü işlem işaretidir, ancak hesabın kendisi eksi kalan gösteremez. Diğer ifadeler doğrudur.',
        "1 Sıra No'lu MSUGT - 100 Kasa; kasa denetimi",
    ),
    # düzey 2
    '0006': patch(
        'İşletme, 10.000 ₺ + %20 KDV tutarındaki malı kredi kartıyla satmıştır. Tutar henüz banka hesabına geçmemiş, kredi kartından alacak olarak izlenmektedir. Bu satışta borçlandırılacak hazır değer hesabı ve tutarı aşağıdakilerden hangisidir?',
        {
            'A': '108 Diğer Hazır Değerler — 12.000 ₺',
            'B': '101 Alınan Çekler — 12.000 ₺',
            'C': '120 Alıcılar — 12.000 ₺',
            'D': '102 Bankalar — 10.000 ₺',
            'E': '100 Kasa — 12.000 ₺',
        },
        'A',
        'Kredi kartı satışında tutar banka hesabına geçene kadar **108 Diğer Hazır Değerler (Kredi Kartından Alacaklar)** hesabında izlenir: 108 (borç) 12.000 / 600 (alacak) 10.000 + 391 (alacak) 2.000. Banka ödeyince 102/108 çalışır.',
        "1 Sıra No'lu MSUGT - 108 Diğer Hazır Değerler; 3065 s. KDVK",
    ),
    # düzey 3
    '0007': patch(
        "İşletmenin dönem başı nakit mevcudu 80.000 ₺, dönem içi nakit tahsilatları 270.000 ₺ ve nakit ödemeleri 310.000 ₺'dir. İşletme dönem sonunda en az 60.000 ₺ nakit bulundurmak istemektedir. Başka bir finansman işlemi olmadığına göre ihtiyaç duyulan kısa vadeli borçlanma kaç ₺'dir?",
        {
            'A': '0 ₺',
            'B': '60.000 ₺',
            'C': '20.000 ₺',
            'D': '40.000 ₺',
            'E': '10.000 ₺',
        },
        'C',
        "Finansman öncesi dönem sonu nakit mevcudu 80.000 + 270.000 − 310.000 = **40.000 ₺**dir. Hedeflenen asgari 60.000 ₺'ye ulaşmak için 60.000 − 40.000 = **20.000 ₺** kısa vadeli borçlanma gerekir.",
        'Nakit Yönetimi - dönem sonu nakit ihtiyacının belirlenmesi',
    ),
    # düzey 2
    '0008': patch(
        'İşletmenin bankası, ay sonu dekontuyla vadesiz hesaptan 300 ₺ hesap işletim ücreti ve 200 ₺ EFT masrafı olmak üzere toplam 500 ₺ kestiğini bildirmiştir. Masraflar işletmenin esas faaliyeti dışındaki banka hizmetleri için alınmıştır.\n\nBu banka masrafının kaydı aşağıdakilerden hangisidir?',
        {
            'A': '102 Bankalar (borç) 500 / 600 Yurt İçi Satışlar (alacak) 500',
            'B': '642 Faiz Gelirleri (borç) 500 / 102 Bankalar (alacak) 500',
            'C': '770 Genel Yönetim Giderleri (borç) 500 / 100 Kasa (alacak) 500',
            'D': '653 Komisyon Giderleri (borç) 500 / 102 Bankalar (alacak) 500',
            'E': '102 Bankalar (borç) 500 / 653 Komisyon Giderleri (alacak) 500',
        },
        'D',
        'Banka masrafı/komisyonu bir olağan giderdir: **653 Komisyon Giderleri (borç) 500 / 102 Bankalar (alacak) 500**. Banka mevduatı azalır.',
        "1 Sıra No'lu MSUGT - 653 Komisyon Giderleri",
    ),
    # düzey 2
    '0009': patch(
        "İşletmenin kasasında 30 ₺/USD kurundan kayıtlı 2.000 USD efektif, bankadaki döviz tevdiat hesabında ise 40 ₺/EUR kurundan kayıtlı 3.000 EUR bulunmaktadır. Değerleme gününde T.C. Merkez Bankası efektif alış kuru 32 ₺/USD, döviz alış kuru 38 ₺/EUR'dur.\n\nVUK'a göre yapılacak değerleme kayıtlarında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '100 Kasa hesabı 4.000 ₺ alacaklandırılır',
            'B': '646 Kambiyo Kârları hesabı net 2.000 ₺ alacaklandırılır',
            'C': '102 Bankalar hesabı 6.000 ₺ borçlandırılır',
            'D': '646 Kambiyo Kârları hesabı 10.000 ₺ alacaklandırılır',
            'E': '656 Kambiyo Zararları hesabı 6.000 ₺ borçlandırılır',
        },
        'E',
        'Efektif: 2.000 × (32 − 30) = 4.000 ₺ artış → 100 Kasa borç / 646 Kambiyo Kârları alacak. Döviz mevduatı: 3.000 × (38 − 40) = 6.000 ₺ azalış → 656 Kambiyo Zararları borç / 102 Bankalar alacak. Her kalem ayrı değerlenir; kâr ile zarar netleştirilmez.',
        'VUK md. 280; 646 Kambiyo Kârları',
    ),
    # düzey 2
    '0010': patch(
        "Hafta sonu işyerine giren hırsızlar kasadaki 5.000 ₺'yi çalmıştır. Polis tutanağı düzenlenmiş, kasa için sigorta bulunmadığı ve faillerden tahsil imkânı olmadığı anlaşılmıştır; kayıp herhangi bir çalışanın sorumluluğunda değildir.\n\nBu kaybın kaydı aşağıdakilerden hangisidir?",
        {
            'A': '100 Kasa (borç) 5.000 / 679 Diğer Olağandışı Gelir (alacak) 5.000',
            'B': '100 Kasa (borç) 5.000 / 689 Diğer Olağandışı Gider ve Zararlar (alacak) 5.000',
            'C': '689 Diğer Olağandışı Gider ve Zararlar (borç) 5.000 / 100 Kasa (alacak) 5.000',
            'D': '135 Personelden Alacaklar (borç) 5.000 / 100 Kasa (alacak) 5.000',
            'E': '770 Genel Yönetim Giderleri (borç) 5.000 / 397 Sayım ve Tesellüm Fazlaları (alacak) 5.000',
        },
        'C',
        'Hırsızlık olağandışı bir zarardır ve tazmin edilemiyorsa: **689 Diğer Olağandışı Gider ve Zararlar (borç) 5.000 / 100 Kasa (alacak) 5.000**. Kasa mevcudu fiilî duruma indirilir.',
        "1 Sıra No'lu MSUGT - 689 Diğer Olağandışı Gider ve Zararlar",
    ),
    # düzey 2
    '0011': patch(
        'Kredi kartıyla yapılan satışta, bankanın hizmet karşılığında kestiği komisyon gideri (tutar banka hesabına net geçmiştir) aşağıdaki hesaplardan hangisine borç yazılır?',
        {
            'A': '102 Bankalar',
            'B': '653 Komisyon Giderleri',
            'C': '108 Diğer Hazır Değerler',
            'D': '600 Yurt İçi Satışlar',
            'E': '642 Faiz Gelirleri',
        },
        'B',
        'Kredi kartı (POS) işlemlerinde bankanın kestiği komisyon bir olağan giderdir ve **653 Komisyon Giderleri**ne borç yazılır; kalan net tutar bankaya/hazır değerlere geçer.',
        "1 Sıra No'lu MSUGT - 653 Komisyon Giderleri (POS)",
    ),
    # düzey 2
    '0012': patch(
        "İşletme, müşterisinden aldığı 15.000 ₺'lik çeki satıcısına olan borcuna karşılık ciro etmiş ve kaydını yapmıştır. Satıcı çeki bankaya ibraz ettiğinde çek karşılıksız çıkmış; satıcı çeki işletmeye iade ederek alacağını yeniden talep etmiş, işletme de çek bedelini müşterisinden tahsil etmek üzere alacak olarak izlemeye karar vermiştir.\n\nÇekin iadesine ilişkin kayıt aşağıdakilerden hangisidir?",
        {
            'A': '120 Alıcılar 15.000 ₺ borç / 320 Satıcılar 15.000 ₺ alacak',
            'B': '101 Alınan Çekler 15.000 ₺ borç / 320 Satıcılar 15.000 ₺ alacak',
            'C': '320 Satıcılar 15.000 ₺ borç / 101 Alınan Çekler 15.000 ₺ alacak',
            'D': '120 Alıcılar 15.000 ₺ borç / 101 Alınan Çekler 15.000 ₺ alacak',
            'E': '320 Satıcılar 15.000 ₺ borç / 120 Alıcılar 15.000 ₺ alacak',
        },
        'A',
        'Ciro sırasında 320 Satıcılar borç / 101 Alınan Çekler alacak kaydı yapılmış, çek portföyden çıkmıştı. Karşılıksız çek iade edilince satıcıya olan borç yeniden doğar (320 alacak) ve çek bedeli müşteriden alacak olarak izlenir (120 borç). Çek portföyde olmadığından 101 yeniden çalışmaz.',
        "1 Sıra No'lu MSUGT - 101 Alınan Çekler (karşılıksız çek)",
    ),
    # düzey 2
    '0013': patch(
        "İşletme, kasasındaki 1.000 USD'yi (30 ₺/USD kurundan kayıtlı) bankaya 33 ₺/USD kurundan bozdurmuş ve TL karşılığı banka hesabına geçmiştir. Bu işlemin kaydı aşağıdakilerden hangisidir?",
        {
            'A': '102 Bankalar (borç) 30.000 / 100 Kasa (alacak) 27.000 + 646 Kambiyo Kârları (alacak) 3.000',
            'B': '102 Bankalar (borç) 33.000 / 100 Kasa (alacak) 30.000 + 642 Faiz Gelirleri (alacak) 3.000',
            'C': '100 Kasa (borç) 33.000 / 102 Bankalar (alacak) 30.000 + 646 Kambiyo Kârları (alacak) 3.000',
            'D': '102 Bankalar (borç) 33.000 / 100 Kasa (alacak) 30.000 + 646 Kambiyo Kârları (alacak) 3.000',
            'E': '656 Kambiyo Zararları (borç) 3.000 + 100 Kasa (borç) 30.000 / 102 Bankalar (alacak) 33.000',
        },
        'D',
        'Banka hesabına 1.000 × 33 = 33.000 ₺ girer; kasadan çıkan YP kayıtlı değeri 1.000 × 30 = 30.000 ₺; aradaki 3.000 ₺ lehte kur farkıdır: **102 Bankalar (borç) 33.000 / 100 Kasa (alacak) 30.000 + 646 Kambiyo Kârları (alacak) 3.000**.',
        'VUK md. 280; 646 Kambiyo Kârları',
    ),
    # düzey 2
    '0014': patch(
        'İşletme aynı gün satıcısına 12.000 ₺ EFT yapmış, banka bunun için hesaptan ayrıca 100 ₺ masraf kesmiştir. Yine aynı gün bir müşteri 8.500 ₺ borcunu havale etmiş, banka gelen havale için 50 ₺ masraf keserek kalan tutarı hesaba geçirmiştir. Masraflara ilişkin vergiler ihmal edilecektir.\n\nBu işlemlerin kayıtlarında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?',
        {
            'A': '653 Komisyon Giderleri hesabı toplam 150 ₺ borçlandırılır',
            'B': '102 Bankalar hesabı EFT için toplam 12.100 ₺ borçlandırılır',
            'C': '320 Satıcılar hesabı 12.100 ₺ borçlandırılır',
            'D': '120 Alıcılar hesabı 8.450 ₺ alacaklandırılır',
            'E': '780 Finansman Giderleri hesabı 150 ₺ borçlandırılır',
        },
        'A',
        'EFT: 320 Satıcılar 12.000 ₺ ve 653 Komisyon Giderleri 100 ₺ borç / 102 Bankalar 12.100 ₺ alacak. Gelen havale: 102 Bankalar 8.450 ₺ ve 653 50 ₺ borç / 120 Alıcılar 8.500 ₺ alacak. Müşterinin borcu tam tutarıyla kapanır; banka masrafları toplam 150 ₺ komisyon gideridir, kredi faizi gibi bir finansman gideri değildir.',
        "1 Sıra No'lu MSUGT - 653 Komisyon Giderleri",
    ),
    # düzey 3
    '0015': patch(
        'Bir işletmede aşağıdaki yevmiye kaydı yapılmıştır:\n\n| Hesap | Borç | Alacak |\n|---|---|---|\n| 100 KASA | 7.000 | |\n| 101 ALINAN ÇEKLER | | 7.000 |\n\nBu kayıt aşağıdaki işlemlerden hangisine aittir?',
        {
            'A': 'Tahsile verilen bir çekin karşılıksız çıkarak geri dönmesi işlemi',
            'B': 'Bir mal satışı karşılığında müşteriden çek alınması işleminin kaydı',
            'C': 'Elde bulunan bir çekin nakden (kasa) tahsil edilmesi',
            'D': 'İşletmenin borcuna karşılık kendi çekini düzenleyip satıcısına vermesi',
            'E': 'Elde bulunan çekin bir satıcıya borç karşılığı ciro edilerek devredilmesi',
        },
        'C',
        'Kasaya nakit girişi (100 borç) ve elde tutulan çekin (101 alacak) azalması, **elde bulunan bir çekin nakden tahsil edilmesi**ni gösterir (ör. keşidecinin işletmeye nakit ödemesi).',
        "1 Sıra No'lu MSUGT - 101 Alınan Çekler / 100 Kasa",
    ),
    # düzey 3
    '0016': patch(
        "Stoklarını aralıklı envanter yöntemiyle izleyen işletme 80.000 ₺ + %20 KDV tutarındaki ticari malı satmıştır. Bedelin 20.000 ₺'si nakit, 30.000 ₺'si müşterinin kredi kartından (tutar birkaç gün sonra bankaya geçecektir) tahsil edilmiş, kalanı için müşteri çeki alınmıştır. Buna göre satış kaydında aşağıdakilerden hangisi yer almaz?",
        {
            'A': '391 Hesaplanan KDV hesabı 16.000 ₺ alacaklandırılır',
            'B': '108 Diğer Hazır Değerler hesabı 30.000 ₺ borçlandırılır',
            'C': '100 Kasa hesabı 20.000 ₺ borçlandırılır',
            'D': '120 Alıcılar hesabı 30.000 ₺ borçlandırılır',
            'E': '101 Alınan Çekler hesabı 46.000 ₺ borçlandırılır',
        },
        'D',
        "Kayıt: 100 (borç) 20.000 + 108 (borç) 30.000 + 101 (borç) 46.000 / 600 (alacak) 80.000 + 391 (alacak) 16.000. Kredi kartı slipi bankaya geçinceye kadar 108 Diğer Hazır Değerler'de izlenir; bedel tahsil edildiğinden senetsiz alacak (120) doğmaz.",
        'THP 100, 101, 108, 600, 391',
    ),
    # düzey 3
    '0017': patch(
        "İşletmenin kasasında 1 € = 36 ₺ kuruyla kaydedilmiş 3.000 € bulunmaktadır. Yıl içinde bunun 1.000 €'su 1 € = 38 ₺'den bozdurularak Türk lirası olarak kasaya alınmıştır. Dönem sonunda kalan dövizler 1 € = 39 ₺ kuruyla değerlenmiştir. Buna göre bu işlemlerden doğan toplam kambiyo kârı kaç ₺'dir?",
        {
            'A': '4.000 ₺',
            'B': '7.000 ₺',
            'C': '2.000 ₺',
            'D': '6.000 ₺',
            'E': '8.000 ₺',
        },
        'E',
        'Bozdurma: 1.000 × (38 − 36) = 2.000 ₺. Değerleme: kalan 2.000 € × (39 − 36) = 6.000 ₺. Toplam **8.000 ₺** (646 Kambiyo Kârları).',
        'VUK m. 280; THP 100, 646',
    ),
    # düzey 2
    '0018': patch(
        "Hazır değerlerle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. 103 Verilen Çekler ve Ödeme Emirleri aktifi düzenleyici bir hesaptır.\n\nII. Kredi kartıyla yapılan satışın bedeli bankaya geçinceye kadar 108'de izlenir.\n\nIII. Karşılıksız çıkan müşteri çeki 101 Alınan Çekler hesabında kalmaya devam eder.",
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'Yalnız II',
            'E': 'I ve III',
        },
        'B',
        'I ve II doğrudur. III yanlıştır: karşılıksız çıkan çek hazır değer olmaktan çıkar; alacak yeniden müşteri hesabına (120) aktarılır.',
        'THP 101, 103, 108',
    ),
    # düzey 3
    '0019': patch(
        'İşletme bir personeline fuar hazırlığı için 5.000 ₺ iş avansı vermiştir. Personel 3.000 ₺ + %20 KDV tutarında yönetim gideri niteliğinde harcama belgesi getirmiş ve artan tutarı kasaya iade etmiştir. Buna göre avansın kapatılma kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '195 İş Avansları hesabı 5.000 ₺ alacaklandırılır',
            'B': '770 Genel Yönetim Giderleri hesabı 3.600 ₺ borçlandırılır',
            'C': '100 Kasa hesabı 1.400 ₺ alacaklandırılır',
            'D': '191 İndirilecek KDV hesabı 600 ₺ alacaklandırılır',
            'E': '196 Personel Avansları hesabı 5.000 ₺ alacaklandırılır',
        },
        'A',
        "Kayıt: 770 (borç) 3.000 + 191 (borç) 600 + 100 (borç) 1.400 / **195 İş Avansları (alacak) 5.000**. İş için verilen avans 195'te izlenir; 196 ücrete mahsuben verilen avanslar içindir.",
        'THP 195, 770, 191, 100',
    ),
    # düzey 3
    '0020': patch(
        "Müşteriden alınan 15.000 ₺'lik çek bankaya ibraz edildiğinde karşılıksız çıkmıştır. Bir hafta sonra müşteri bu borcu için işletmeye aynı tutarda senet vermiştir. Buna göre bu iki olaya ilişkin kayıtlar sırasıyla aşağıdakilerden hangisidir?",
        {
            'A': '101 (borç) / 120 (alacak); 121 (borç) / 101 (alacak)',
            'B': '128 (borç) / 101 (alacak); 121 (borç) / 128 (alacak)',
            'C': '120 (borç) / 102 (alacak); 121 (borç) / 120 (alacak)',
            'D': '120 (borç) / 101 (alacak); 121 (borç) / 120 (alacak)',
            'E': '689 (borç) / 101 (alacak); 121 (borç) / 689 (alacak)',
        },
        'D',
        'Karşılıksız çıkan çek hazır değer olmaktan çıkar ve alacak yeniden müşteri hesabına alınır: 120 (borç) / 101 (alacak). Müşteri senet verince senetsiz alacak senetli alacağa dönüşür: 121 (borç) / 120 (alacak).',
        'THP 101, 120, 121',
    ),
    # düzey 2
    '0021': patch(
        "Bir işletmenin dönem sonu kesin mizanından alınan kalanlar şöyledir: 100 Kasa 12.000 ₺, 101 Alınan Çekler 30.000 ₺, 102 Bankalar 180.000 ₺ (80.000 ₺ vadesiz, 100.000 ₺ üç ay vadeli mevduat), 103 Verilen Çekler ve Ödeme Emirleri 25.000 ₺, 108 Diğer Hazır Değerler 15.000 ₺, 110 Hisse Senetleri 20.000 ₺, 121 Alacak Senetleri 50.000 ₺, 196 Personel Avansları 4.000 ₺.\n\nBuna göre bilançoda '10 Hazır Değerler' grubunun net tutarı kaç ₺'dir?",
        {
            'A': '237.000',
            'B': '212.000',
            'C': '262.000',
            'D': '112.000',
            'E': '232.000',
        },
        'B',
        "Hazır değerler: 100 12.000 + 101 30.000 + 102 180.000 (vadeli mevduat da 102'de izlenir) − 103 25.000 (düzenleyici) + 108 15.000 = 212.000 ₺. 110 Hisse Senetleri menkul kıymetler (11), 121 Alacak Senetleri ticari alacaklar (12), 196 Personel Avansları diğer dönen varlıklar (19) grubundadır.",
        'VUK md. 280 (YP değerleme); 646 Kambiyo Kârları',
    ),
    # düzey 2
    '0022': patch(
        "İşletme, yurt dışı seyahatlerde kullanılmak üzere TL vadesiz hesabından bankanın efektif satış kuru olan 37,00 ₺/EUR üzerinden 2.000 EUR efektif satın alarak kasasına koymuştur. Dönem sonuna kadar bu efektif kullanılmamıştır. Dönem sonunda T.C. Merkez Bankası efektif alış kuru 36,00 ₺/EUR'dur.\n\nDönem sonu değerleme kaydı aşağıdakilerden hangisidir?",
        {
            'A': '656 Kambiyo Zararları 4.000 ₺ borç / 100 Kasa 4.000 ₺ alacak',
            'B': '100 Kasa 2.000 ₺ borç / 646 Kambiyo Kârları 2.000 ₺ alacak',
            'C': '656 Kambiyo Zararları 2.000 ₺ borç / 100 Kasa 2.000 ₺ alacak',
            'D': "Değerleme farkı doğmaz; kasa 74.000 ₺'de kalır",
            'E': '656 Kambiyo Zararları 2.000 ₺ borç / 102 Bankalar 2.000 ₺ alacak',
        },
        'C',
        "Efektif, ödenen tutarla (2.000 × 37,00 = 74.000 ₺) kasaya alınır. Dönem sonunda VUK m. 280'e göre MB efektif alış kuruyla değerlenir: 2.000 × 36,00 = 72.000 ₺. Aradaki 2.000 ₺ kambiyo zararıdır: 656 borç / 100 Kasa alacak.",
        'VUK md. 280; 656 Kambiyo Zararları',
    ),
    # düzey 2
    '0023': patch(
        "İşletme daha önce satıcısına verdiği 8.000 ₺'lik çek, satıcı tarafından bankaya ibraz edilerek işletmenin banka hesabından ödenmiştir.\n\nBu işlemin kaydı aşağıdakilerden hangisidir?",
        {
            'A': '103 Verilen Çekler ve Ödeme Emirleri (borç) 8.000 / 320 Satıcılar (alacak) 8.000',
            'B': '320 Satıcılar (borç) 8.000 / 102 Bankalar (alacak) 8.000',
            'C': '102 Bankalar (borç) 8.000 / 103 Verilen Çekler ve Ödeme Emirleri (alacak) 8.000',
            'D': '101 Alınan Çekler (borç) 8.000 / 100 Kasa (alacak) 8.000',
            'E': '103 Verilen Çekler ve Ödeme Emirleri (borç) 8.000 / 102 Bankalar (alacak) 8.000',
        },
        'E',
        'Çek verildiğinde 103 alacaklanmıştı. Çek bankadan **ödenince** düzenleyici hesap kapatılır: **103 Verilen Çekler ve Ödeme Emirleri (borç) 8.000 / 102 Bankalar (alacak) 8.000**; banka mevduatı azalır.',
        "1 Sıra No'lu MSUGT - 103 / 102",
    ),
    # düzey 2
    '0024': patch(
        'Ay sonu kasa sayımında 100 Kasa hesabının kayıtlı mevcudu 12.300 ₺, fiilî mevcudu 13.100 ₺ bulunmuştur. Gün içindeki tahsilat ve ödeme belgeleri incelenmiş, farkın nedeni belirlenememiştir.\n\nBuna göre yapılacak kayıt aşağıdakilerden hangisidir?',
        {
            'A': '197 Sayım ve Tesellüm Noksanları (borç) 800 / 100 Kasa (alacak) 800',
            'B': '100 Kasa (borç) 800 / 679 Diğer Olağandışı Gelir (alacak) 800',
            'C': '397 Sayım ve Tesellüm Fazlaları (borç) 800 / 100 Kasa (alacak) 800',
            'D': '100 Kasa (borç) 800 / 397 Sayım ve Tesellüm Fazlaları (alacak) 800',
            'E': '100 Kasa (borç) 800 / 642 Faiz Gelirleri (alacak) 800',
        },
        'D',
        'Kasa fazlasında Kasa borçlanır, nedeni bulunana kadar **397 Sayım ve Tesellüm Fazlaları** alacaklanır: **100 Kasa (borç) 800 / 397 (alacak) 800**. Neden belirlenince 397 ilgili hesaba devredilir.',
        "1 Sıra No'lu MSUGT - 397 Sayım ve Tesellüm Fazlaları",
    ),
    # düzey 3
    '0025': patch(
        'Bir işletmede aşağıdaki yevmiye kaydı yapılmıştır:\n\n| Hesap | Borç | Alacak |\n|---|---|---|\n| 335 PERSONELE BORÇLAR | 12.000 | |\n| 100 KASA | | 12.000 |\n\nBu kayıt aşağıdaki işlemlerden hangisine aittir?',
        {
            'A': 'Dönem içinde personele ait ücretin gider olarak tahakkuk ettirilmesi işleminin kaydı',
            'B': 'Personele iş avansı verilerek işletmenin ondan alacaklı duruma gelmesi kaydı',
            'C': 'Bir tahsilat sonucu işletmenin kasasına nakit para girişi olması işlemi',
            'D': 'Personel ücretlerine ilişkin sigorta priminin işveren payının tahakkuk ettirilmesi',
            'E': 'Daha önce tahakkuk ettirilmiş net ücretin personele nakden ödenmesi',
        },
        'E',
        'Kasadan nakit çıkışı (100 alacak) ve personele olan borcun azalması (335 borç), daha önce tahakkuk ettirilmiş **net ücretin personele nakden ödenmesi**ni gösterir. Gider tahakkuku önceden yapıldığından burada gider hesabı çalışmaz.',
        "1 Sıra No'lu MSUGT - 335 Personele Borçlar / 100 Kasa",
    ),
    # düzey 3
    '0026': patch(
        "İşletmenin 102 Bankalar hesabı bakiyesi 248.000 ₺'dir. Banka, işletme adına 12.000 ₺ müşteri borcu ile 1.000 ₺ mevduat faizi tahsil etmiş; ayrıca 1.200 ₺ hesap işletim ücreti kesmiştir. Bu üç işlem işletmece henüz kaydedilmemiştir. Yoldaki mevduat ve ödenmemiş çeklerin banka tarafında düzeltileceği dikkate alındığında, işletmenin düzeltilmiş defter bakiyesi kaç ₺'dir?",
        {
            'A': '261.200 ₺',
            'B': '247.800 ₺',
            'C': '259.800 ₺',
            'D': '258.000 ₺',
            'E': '234.800 ₺',
        },
        'C',
        'İşletmenin defter bakiyesi; bankanın doğrudan tahsil ettiği 12.000 ₺ ve faiz geliri 1.000 ₺ kadar artırılır, 1.200 ₺ banka masrafı kadar azaltılır: 248.000 + 12.000 + 1.000 − 1.200 = **259.800 ₺**. Yoldaki mevduat ve ödenmemiş çekler banka hesap özeti tarafının düzeltmeleridir.',
        "1 Sıra No'lu MSUGT - 102 Bankalar, 642 Faiz Gelirleri ve 653 Komisyon Giderleri",
    ),
    # düzey 2
    '0027': patch(
        "Kasa sayımında belirlenen 2.000 ₺'lik noksanlığın, kasadan sorumlu veznedarın dikkatsizliğinden kaynaklandığı ve kendisinden tahsil edileceği tespit edilmiştir. Daha önce '197 Sayım ve Tesellüm Noksanları'nda izlenen bu tutarın kapatılmasına ilişkin kayıt aşağıdakilerden hangisidir?",
        {
            'A': '135 Personelden Alacaklar (borç) 2.000 / 197 Sayım ve Tesellüm Noksanları (alacak) 2.000',
            'B': '689 Diğer Olağandışı Gider (borç) 2.000 / 135 Personelden Alacaklar (alacak) 2.000',
            'C': '197 Sayım ve Tesellüm Noksanları (borç) 2.000 / 135 Personelden Alacaklar (alacak) 2.000',
            'D': '770 Genel Yönetim Giderleri (borç) 2.000 / 197 Sayım ve Tesellüm Noksanları (alacak) 2.000',
            'E': '100 Kasa (borç) 2.000 / 197 Sayım ve Tesellüm Noksanları (alacak) 2.000',
        },
        'A',
        'Noksanlık sorumluya yükleneceğinden ondan alacak doğar → **135 Personelden Alacaklar (borç) 2.000**; geçici hesap kapatılır → **197 Sayım ve Tesellüm Noksanları (alacak) 2.000**.',
        "1 Sıra No'lu MSUGT - 135 Personelden Alacaklar / 197",
    ),
    # düzey 2
    '0028': patch(
        "Perakende satış yapan işletmenin gün sonu ödeme kaydedici cihaz (Z) raporuna göre KDV dâhil hasılat 19.900 ₺'dir. Hasılatın 14.400 ₺'si %20, 5.500 ₺'si %10 oranlı mallara aittir. Tahsilatın 7.900 ₺'si kredi kartıyla yapılmış olup tutarlar henüz banka hesabına geçmemiştir; kalanı nakittir.\n\nGün sonu hasılat kaydında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '600 Yurt İçi Satışlar hesabı 19.900 ₺ alacaklandırılır',
            'B': '391 Hesaplanan KDV hesabı 2.900 ₺ alacaklandırılır',
            'C': '100 Kasa hesabı 19.900 ₺ borçlandırılır',
            'D': '108 Diğer Hazır Değerler hesabı 7.900 ₺ alacaklandırılır',
            'E': '391 Hesaplanan KDV hesabı 3.980 ₺ alacaklandırılır',
        },
        'B',
        "%20'li hasılat: matrah 14.400 / 1,20 = 12.000 ₺, KDV 2.400 ₺; %10'lu hasılat: matrah 5.500 / 1,10 = 5.000 ₺, KDV 500 ₺. Kayıt: 100 Kasa 12.000 ₺ ve 108 Diğer Hazır Değerler 7.900 ₺ borç / 600 Yurt İçi Satışlar 17.000 ₺ ve 391 Hesaplanan KDV 2.900 ₺ alacak.",
        "1 Sıra No'lu MSUGT; VUK md. 233 (ÖKC fişi)",
    ),
    # düzey 2
    '0029': patch(
        "İşletme, personeline verdiği 3.000 ₺'lik iş avansının tamamının genel yönetim gideri niteliğindeki bir harcamayla belgelendirildiğini tespit etmiştir. Avansın kapatılmasına ilişkin kayıt aşağıdakilerden hangisidir? (KDV ihmal edilecektir.)",
        {
            'A': '195 İş Avansları (borç) 3.000 / 770 Genel Yönetim Giderleri (alacak) 3.000',
            'B': '195 İş Avansları (borç) 3.000 / 100 Kasa (alacak) 3.000',
            'C': '770 Genel Yönetim Giderleri (borç) 3.000 / 196 Personel Avansları (alacak) 3.000',
            'D': '770 Genel Yönetim Giderleri (borç) 3.000 / 100 Kasa (alacak) 3.000',
            'E': '770 Genel Yönetim Giderleri (borç) 3.000 / 195 İş Avansları (alacak) 3.000',
        },
        'E',
        'Avans harcanıp belgelenince ilgili gider hesabına aktarılır ve iş avansı hesabı kapatılır; 196 Personel Avansları ücrete mahsuben verilen avanslar içindir: **770 Genel Yönetim Giderleri (borç) 3.000 / 195 İş Avansları (alacak) 3.000**.',
        "1 Sıra No'lu MSUGT - 195 İş Avansları",
    ),
    # düzey 2
    '0030': patch(
        'İşletme, kullandığı banka kredisine ilişkin 4.000 ₺ faizi banka hesabından ödemiştir. Bu faiz giderinin kaydı aşağıdakilerden hangisidir? (Dönemsellik/tahakkuk ayrımı ihmal edilecektir.)',
        {
            'A': '780 Finansman Giderleri (borç) 4.000 / 102 Bankalar (alacak) 4.000',
            'B': '653 Komisyon Giderleri (borç) 4.000 / 100 Kasa (alacak) 4.000',
            'C': '102 Bankalar (borç) 4.000 / 780 Finansman Giderleri (alacak) 4.000',
            'D': '300 Banka Kredileri (borç) 4.000 / 102 Bankalar (alacak) 4.000',
            'E': '642 Faiz Gelirleri (borç) 4.000 / 102 Bankalar (alacak) 4.000',
        },
        'A',
        "Kredi faizi bir finansman gideridir: **780 Finansman Giderleri (borç) 4.000 / 102 Bankalar (alacak) 4.000**. Anapara geri ödemesi ise 300 Banka Kredileri'ni ilgilendirir.",
        "1 Sıra No'lu MSUGT - 780 Finansman Giderleri",
    ),
    # düzey 2
    '0031': patch(
        "İşletme 30,00 ₺/USD kurundan kayıtlı 10.000 USD'yi bankada üç ay vadeli döviz mevduatına yatırmıştır. Vade sonunda banka 150 USD faizi anaparaya ekleyerek 10.150 USD'yi işletmenin vadesiz döviz hesabına aktarmıştır; vade günü kur 32,00 ₺/USD'dir. Faiz tahakkuku yapılmamış, stopaj ihmal edilecektir. Arada bir dönem sonu değerlemesi yapılmamıştır.\n\nVade sonu kaydında 646 Kambiyo Kârları ve 642 Faiz Gelirleri hesaplarına yazılacak tutarlar aşağıdakilerden hangisidir?",
        {
            'A': '646: 24.800 ₺; 642 hesabı kullanılmaz',
            'B': '642: 24.800 ₺; 646 hesabı kullanılmaz',
            'C': '646: 20.000 ₺; 642: 4.500 ₺',
            'D': '646: 20.000 ₺; 642: 4.800 ₺',
            'E': '646: 20.300 ₺; 642: 4.500 ₺',
        },
        'D',
        "Anapara 30,00'dan kayıtlıdır; vade günü değeri 10.000 × 32,00 = 320.000 ₺; fark 20.000 ₺ kambiyo kârı (646). Faiz geliri tahsil günü kuruyla ölçülür: 150 × 32,00 = 4.800 ₺ (642). Kayıt: 102 (vadesiz döviz) 324.800 ₺ borç / 102 (vadeli döviz) 300.000 ₺, 646 20.000 ₺ ve 642 4.800 ₺ alacak.",
        'VUK md. 280; 656 Kambiyo Zararları',
    ),
    # düzey 2
    '0032': patch(
        'Çek ve senet (bono) ile ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Çek görüldüğünde ödenir',
            'B': 'Bono belirli bir vadede ödenmek üzere düzenlenir',
            'C': 'Çek bir kredi aracı, bono ise bir ödeme aracıdır',
            'D': 'Alınan çekler 101 Alınan Çekler hesabında izlenir',
            'E': 'Senetli ticari alacaklar 121 hesabında izlenir',
        },
        'C',
        'Çek esas olarak bir ödeme aracıdır ve görüldüğünde ödenir; bono (senet) ise belirli bir vadede ödenmek üzere düzenlenen bir kredi aracıdır. Alınan çekler 101, senetli ticari alacaklar 121 hesabında izlenir.',
        'Kıymetli evrak - çek/bono ayrımı',
    ),
    # düzey 3
    '0033': patch(
        'İşletme, bankadan ödenen bir çeki kendi kayıtlarına yanlışlıkla 9.800 ₺ olarak geçirmiştir. Banka hesap özetinde çekin doğru tutarı olan 8.900 ₺ yer almaktadır. Başka hata olmadığına göre banka mutabakatında işletmenin defter bakiyesi nasıl düzeltilmelidir?',
        {
            'A': 'İşletme kaydı banka bakiyesini etkilemediği için düzeltme yapılmamalıdır.',
            'B': '900 ₺ artırılmalıdır.',
            'C': '900 ₺ azaltılmalıdır.',
            'D': '8.900 ₺ artırılmalıdır.',
            'E': '9.800 ₺ azaltılmalıdır.',
        },
        'B',
        'İşletme 8.900 ₺ yerine 9.800 ₺ çıkış kaydederek banka hesabını **900 ₺ fazla azaltmıştır**. Defter bakiyesini doğru tutara getirmek için 102 Bankalar hesabı **900 ₺ artırılmalıdır**.',
        'Muhasebe Süreci - 102 Bankalar hesabı ve banka mutabakatı',
    ),
    # düzey 2
    '0034': patch(
        'İşletmenin vadeli mevduatına dönem sonu itibarıyla 4.000 ₺ faiz tahakkuk etmiş ancak henüz hesaba geçmemiştir (vade sonraki dönemdedir). Dönemsellik gereği yapılacak kayıt aşağıdakilerden hangisidir?',
        {
            'A': '102 Bankalar (borç) 4.000 / 642 Faiz Gelirleri (alacak) 4.000',
            'B': '642 Faiz Gelirleri (borç) 4.000 / 102 Bankalar (alacak) 4.000',
            'C': '642 Faiz Gelirleri (borç) 4.000 / 181 Gelir Tahakkukları (alacak) 4.000',
            'D': '181 Gelir Tahakkukları (borç) 4.000 / 642 Faiz Gelirleri (alacak) 4.000',
            'E': '180 Gelecek Aylara Ait Giderler (borç) 4.000 / 642 Faiz Gelirleri (alacak) 4.000',
        },
        'D',
        'Döneme ait olup henüz tahsil edilmemiş gelir tahakkuk ettirilir: **181 Gelir Tahakkukları (borç) 4.000 / 642 Faiz Gelirleri (alacak) 4.000**. Faiz sonraki dönemde tahsil edilince 181 kapatılır.',
        "1 Sıra No'lu MSUGT - 181 Gelir Tahakkukları; Dönemsellik",
    ),
    # düzey 2
    '0035': patch(
        "İşletme 1 Kasım'da bankada 200.000 ₺ tutarında, yıllık %30 faizli ve altı ay vadeli bir vadeli mevduat hesabı açmıştır. 31 Aralık'ta dönemsellik gereği iki aylık faiz tahakkuk ettirilmiştir. 30 Nisan'da vade dolmuş; anapara ile faiz, faiz üzerinden %15 stopaj kesilerek vadesiz hesaba aktarılmıştır. Faiz basit faiz yöntemiyle hesaplanacaktır.\n\nVade sonu kaydında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '642 Faiz Gelirleri hesabı 30.000 ₺ alacaklandırılır',
            'B': '181 Gelir Tahakkukları hesabı 10.000 ₺ borçlandırılır',
            'C': '642 Faiz Gelirleri hesabı 20.000 ₺ alacaklandırılır',
            'D': '193 Peşin Ödenen Vergiler ve Fonlar 3.000 ₺ borçlandırılır',
            'E': '102 Bankalar hesabı vadesiz hesaba 230.000 ₺ borçlandırılır',
        },
        'C',
        'Toplam faiz 200.000 × %30 × 6/12 = 30.000 ₺; geçen yıl tahakkuk eden iki aylık kısım 10.000 ₺, cari yıla düşen kısım 20.000 ₺. Stopaj 30.000 × %15 = 4.500 ₺. Kayıt: 102 Bankalar (vadesiz) 225.500 ₺ ve 193 Peşin Ödenen Vergiler ve Fonlar 4.500 ₺ borç / 102 Bankalar (vadeli) 200.000 ₺, 181 Gelir Tahakkukları 10.000 ₺ ve 642 Faiz Gelirleri 20.000 ₺ alacak.',
        "1 Sıra No'lu MSUGT - 642 Faiz Gelirleri",
    ),
    # düzey 3
    '0036': patch(
        'İşletmenin 108 Diğer Hazır Değerler hesabında izlenen 30.000 ₺ tutarındaki kredi kartı satış tahsilatı için banka %2 komisyon keserek kalan tutarı işletmenin vadesiz hesabına aktarmıştır. Buna göre yapılacak kayıtla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '108 Diğer Hazır Değerler hesabı 29.400 ₺ alacaklandırılır',
            'B': '100 Kasa hesabı 29.400 ₺ borçlandırılır',
            'C': '120 Alıcılar hesabı 30.000 ₺ alacaklandırılır',
            'D': '102 Bankalar hesabı 30.000 ₺ borçlandırılır',
            'E': '108 Diğer Hazır Değerler hesabı 30.000 ₺ alacaklandırılır',
        },
        'E',
        'Kayıt: 102 (borç) 29.400 + 653 Komisyon Giderleri (borç) 600 / **108 (alacak) 30.000**. 108 hesabı tahsilatın tamamıyla kapanır; komisyon ayrıca gider yazılır.',
        'THP 108, 102, 653',
    ),
    # düzey 3
    '0037': patch(
        'İşletmenin 200.000 ₺ tutarındaki vadeli mevduatının vadesi dolmuş, 12.000 ₺ brüt faiz tahakkuk etmiştir. Banka faiz üzerinden %15 gelir vergisi stopajı keserek anapara ve net faizi işletmenin vadesiz hesabına aktarmıştır (önceden tahakkuk kaydı yapılmamıştır). Buna göre kayıtla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '642 Faiz Gelirleri hesabı 10.200 ₺ alacaklandırılır',
            'B': '193 Peşin Ödenen Vergiler ve Fonlar hesabı 1.800 ₺ borçlandırılır',
            'C': '360 Ödenecek Vergi ve Fonlar hesabı 1.800 ₺ alacaklandırılır',
            'D': '770 Genel Yönetim Giderleri hesabı 1.800 ₺ borçlandırılır',
            'E': '193 Peşin Ödenen Vergiler ve Fonlar hesabı 1.800 ₺ alacaklandırılır',
        },
        'B',
        'Kayıt: 102 vadesiz (borç) 210.200 + **193 (borç) 1.800** / 102 vadeli (alacak) 200.000 + 642 (alacak) 12.000. Faiz geliri brüt tutarla yazılır; kesilen stopaj işletmenin vergisinden mahsup edilecek peşin vergidir.',
        'THP 102, 193, 642 (stopaj oranı senaryoda verilmiştir)',
    ),
    # düzey 3
    '0038': patch(
        "Bir işletmenin dönem sonu mizanında şu kalanlar vardır: 100 Kasa 12.000 ₺, 101 Alınan Çekler 30.000 ₺, 102 Bankalar 150.000 ₺, 103 Verilen Çekler ve Ödeme Emirleri 25.000 ₺, 108 Diğer Hazır Değerler 8.000 ₺ ve 110 Hisse Senetleri 40.000 ₺. Buna göre bilançoda gösterilecek hazır değerler toplamı kaç ₺'dir?",
        {
            'A': '175.000 ₺',
            'B': '225.000 ₺',
            'C': '145.000 ₺',
            'D': '200.000 ₺',
            'E': '215.000 ₺',
        },
        'A',
        '12.000 + 30.000 + 150.000 − 25.000 (103 aktifi düzenleyicidir) + 8.000 = **175.000 ₺**. 110 Hisse Senetleri 11 Menkul Kıymetler grubundadır.',
        'THP 10 Hazır Değerler',
    ),
    # düzey 2
    '0039': patch(
        "İşletme bir personeline, ay sonunda ödenecek ücretinden düşülmek üzere 4.000 ₺ nakit avans vermiştir. Bu avans Tekdüzen Hesap Planı'nda hangi hesapta izlenir?",
        {
            'A': '770 Genel Yönetim Giderleri',
            'B': '195 İş Avansları',
            'C': '135 Personelden Alacaklar',
            'D': '335 Personele Borçlar',
            'E': '196 Personel Avansları',
        },
        'E',
        "Ücrete mahsuben verilen avanslar **196 Personel Avansları**'nda, bir iş için verilen avanslar 195 İş Avansları'nda izlenir. 335 ödenecek ücretler içindir.",
        'THP 195, 196',
    ),
    # düzey 2
    '0040': patch(
        'Bir işletmenin varlıkları sınıflandırılmaktadır. Buna göre aşağıdaki hesaplardan hangisi 10 Hazır Değerler grubunda yer almaz?',
        {
            'A': '102 Bankalar',
            'B': '101 Alınan Çekler',
            'C': '108 Diğer Hazır Değerler',
            'D': '126 Verilen Depozito ve Teminatlar',
            'E': '100 Kasa',
        },
        'D',
        '126 Verilen Depozito ve Teminatlar 12 Ticari Alacaklar grubundadır. 100, 101, 102 ve 108 hazır değerlerdir.',
        'THP 10 Hazır Değerler',
    ),
    # düzey 3
    '0041': patch(
        'Bir işletmede aşağıdaki yevmiye kaydı yapılmıştır:\n\n| Hesap | Borç | Alacak |\n|---|---|---|\n| 102 BANKALAR | 10.000 | |\n| 101 ALINAN ÇEKLER | | 10.000 |\n\nBu kayıt aşağıdaki işlemlerden hangisine aittir?',
        {
            'A': 'İşletmenin kasasındaki nakdin bankadaki mevduat hesabına yatırılması',
            'B': 'İşletmenin satıcısına olan borcuna karşılık kendi çekini düzenleyip vermesi',
            'C': 'Daha önce alınan çekin bankada tahsil edilmesi',
            'D': 'Bir mal satışı karşılığında müşteriden çek alınması işleminin kaydı',
            'E': 'İşletmenin bankadan kısa vadeli nakit kredi kullanması işlemi',
        },
        'C',
        'Banka mevduatının artması (102 borç) ve elde tutulan çek varlığının azalması (101 alacak), daha önce **alınan çekin bankada tahsil edilmesi**ni gösterir. Çek alınırken 101 borçlanırdı; tahsilde ters yönde kapanır.',
        "1 Sıra No'lu MSUGT - 101 Alınan Çekler / 102 Bankalar",
    ),
    # düzey 2
    '0042': patch(
        "İşletme satıcısına olan 25.000 ₺'lik senetsiz borcu için, banka hesabına bağlı çek karnesinden keşide tarihi on gün sonra olan bir çek yazarak satıcıya teslim etmiştir. Çek henüz bankaya ibraz edilmemiştir.\n\nBu işlemle ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Çek verildiği anda nakit çıkışı olduğundan 100 Kasa hesabı doğrudan alacaklandırılır.',
            'B': '103 Verilen Çekler ve Ödeme Emirleri (-) hesabı alacaklandırılır.',
            'C': 'Müşteriden alınmış bir çek gibi 101 Alınan Çekler hesabı borç yerine alacaklandırılır.',
            'D': 'Borç ödenmeyip arttığından karşı taraf olarak 320 Satıcılar hesabı alacaklandırılır.',
            'E': 'Bedel banka hesabından hemen düşeceği için 102 Bankalar hesabı doğrudan alacaklandırılır.',
        },
        'B',
        'İşletmenin düzenleyip verdiği çekler **103 Verilen Çekler ve Ödeme Emirleri (-)** hesabında izlenir. Çek verildiğinde: 320 Satıcılar (borç) / **103 (alacak)**. Çek bankadan ödendiğinde 103 borçlanır, 102 Bankalar alacaklanır.',
        "1 Sıra No'lu MSUGT - 103 Verilen Çekler ve Ödeme Emirleri (-)",
    ),
    # düzey 2
    '0043': patch(
        "İşletme 1 Mart'ta altı ay vadeli ve yıllık %40 faizli bir vadeli hesaba 300.000 ₺ yatırmıştır. Nakit ihtiyacı nedeniyle hesap 1 Temmuz'da vadesinden önce bozulmuş; sözleşme gereği banka, geçen dört ay için yalnız yıllık %5 vadesiz faiz oranını uygulayarak anapara ile faizi vadesiz hesaba aktarmıştır. Faiz basit faizle hesaplanır, stopaj ihmal edilecektir. Daha önce faiz tahakkuku yapılmamıştır.\n\nBu işlemin kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '642 Faiz Gelirleri hesabı 5.000 ₺ alacaklandırılır',
            'B': '642 Faiz Gelirleri hesabı 40.000 ₺ alacaklandırılır',
            'C': '181 Gelir Tahakkukları hesabı 5.000 ₺ borçlandırılır',
            'D': '102 Bankalar (vadeli) 305.000 ₺ alacaklandırılır',
            'E': '642 Faiz Gelirleri hesabı 60.000 ₺ alacaklandırılır',
        },
        'A',
        'Vade bozulduğu için sözleşmedeki %40 değil %5 uygulanır: 300.000 × %5 × 4/12 = 5.000 ₺. Kayıt: 102 Bankalar (vadesiz) 305.000 ₺ borç / 102 Bankalar (vadeli) 300.000 ₺ ve 642 Faiz Gelirleri 5.000 ₺ alacak. Önceden tahakkuk yapılmadığından 181 çalışmaz.',
        "1 Sıra No'lu MSUGT - 642 Faiz Gelirleri",
    ),
    # düzey 2
    '0044': patch(
        "Aşağıdakilerden hangisi '108 Diğer Hazır Değerler' hesabında izlenmeye en uygun kalemdir?",
        {
            'A': 'Ortaklardan olan ve 131 Ortaklardan Alacaklar hesabında izlenen ticari olmayan alacaklar',
            'B': 'Satıcılara olan ve 320 Satıcılar hesabında izlenen kısa vadeli ticari borçlar',
            'C': 'Satılmak üzere depoda bekleyen ve 153 Ticari Mallar hesabında izlenen stoklar',
            'D': 'Vadesi gelmiş kuponlar ile bankaca tahsil için gönderilmiş posta/banka havaleleri',
            'E': 'İşletmenin kasasında bulunan ve 100 Kasa hesabında izlenen nakit Türk Lirası mevcudu',
        },
        'D',
        '**108 Diğer Hazır Değerler**, niteliği itibarıyla hazır değer sayılan ancak 100-103 hesaplarına girmeyen kalemleri (vadesi gelmiş kuponlar, tahsile gönderilen havaleler vb.) izler.',
        "1 Sıra No'lu MSUGT - 108 Diğer Hazır Değerler",
    ),
    # düzey 3
    '0045': patch(
        "İşletmede 10.000 ₺ tutarında sabit kasa avansı oluşturulmuştur. Dönem sonundaki sayımda kasada 2.300 ₺ nakit ve toplam 7.500 ₺ tutarında geçerli harcama belgesi bulunmuştur. Fonun yeniden 10.000 ₺'ye tamamlanması istenmektedir.\n\nBuna göre kasa noksanı ve kasaya konulacak tamamlama tutarı sırasıyla kaç ₺'dir?",
        {
            'A': 'Noksan veya fazla yok; 7.500 ₺ tamamlama',
            'B': '200 ₺ fazla; 7.500 ₺ tamamlama',
            'C': '200 ₺ noksan; 7.700 ₺ tamamlama',
            'D': '7.500 ₺ noksan; 2.300 ₺ tamamlama',
            'E': '2.300 ₺ noksan; 10.000 ₺ tamamlama',
        },
        'C',
        "Nakit ve belgeler toplamı 2.300 + 7.500 = **9.800 ₺** olduğundan 10.000 − 9.800 = **200 ₺ kasa noksanı** vardır. Kasayı yeniden 10.000 ₺'ye çıkarmak için 10.000 − 2.300 = **7.700 ₺** konulmalıdır. Bu tutarın 7.500 ₺'si belgeli giderleri, 200 ₺'si noksanı karşılar.",
        "1 Sıra No'lu MSUGT - 100 Kasa ve kasa sayım işlemleri",
    ),
    # düzey 2
    '0046': patch(
        'Banka mutabakatıyla ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Mutabakatın amacı iki bakiye arasındaki farkları açıklamaktır',
            'B': 'Bankanın kestiği ancak işletmenin bilmediği masraf işletme kaydına işlenir',
            'C': 'Bankanın tahsil ettiği ancak işletmenin bilmediği tutar işletme kaydına eklenir',
            'D': 'Hatalı kayıtlar ilgili tarafın bakiyesinde düzeltilir',
            'E': 'Yoldaki mevduat banka bakiyesinden düşülür, ödenmemiş çekler eklenir',
        },
        'E',
        'Banka mutabakatında yoldaki mevduat banka hesap özeti bakiyesine EKLENİR, ödenmemiş çekler bu bakiyeden DÜŞÜLÜR. İşletmenin henüz bilmediği banka masrafları ve tahsilatlar işletme kayıtlarına işlenir; hatalar ilgili tarafın bakiyesinde düzeltilir.',
        'Muhasebe Süreci - 102 Bankalar hesabı ve banka mutabakatı',
    ),
    # düzey 2
    '0047': patch(
        "Kasa sayımında belirlenen 6.000 ₺'lik fazlalığın, kaydı unutulmuş peşin bir mal satışından (KDV dâhil) kaynaklandığı anlaşılmıştır (KDV %20). '397 Sayım ve Tesellüm Fazlaları'nda izlenen tutarın kapatılmasına ilişkin kayıt aşağıdakilerden hangisidir?",
        {
            'A': '397 Sayım ve Tesellüm Fazlaları (borç) 6.000 / 600 Yurt İçi Satışlar (alacak) 6.000 (KDV ayrıştırılmaz)',
            'B': '397 Sayım ve Tesellüm Fazlaları (borç) 6.000 / 600 Yurt İçi Satışlar (alacak) 5.000 + 391 Hesaplanan KDV (alacak) 1.000',
            'C': '397 Sayım ve Tesellüm Fazlaları (borç) 6.000 / 679 Diğer Olağandışı Gelir ve Kârlar (alacak) 6.000',
            'D': '600 Yurt İçi Satışlar (borç) 5.000 + 391 Hesaplanan KDV (borç) 1.000 / 397 Sayım ve Tesellüm Fazlaları (alacak) 6.000',
            'E': '191 İndirilecek KDV (borç) 1.000 / 600 Yurt İçi Satışlar (alacak) 1.000 (KDV kısmı düzeltilir)',
        },
        'B',
        'Fazlalığın nedeni kaydı unutulan satıştır (6.000 = 5.000 satış + 1.000 KDV). Geçici hesap kapatılır: **397 (borç) 6.000 / 600 Yurt İçi Satışlar (alacak) 5.000 + 391 Hesaplanan KDV (alacak) 1.000**.',
        "1 Sıra No'lu MSUGT - 397; 3065 s. KDVK",
    ),
    # düzey 2
    '0048': patch(
        "'135 Personelden Alacaklar' hesabıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Pasif bir hesaptır; personele olan borçları izler',
            'B': 'Personele verilen borç paraları izler',
            'C': 'Dönen varlıklar arasında yer alır',
            'D': 'Personelden tahsil edildiğinde alacaklandırılır',
            'E': 'Personelin kasa ve sayım açıkları da burada izlenebilir',
        },
        'A',
        '135 Personelden Alacaklar, personele verilen borç paralar ile personelin zimmet, kasa ve sayım açıkları gibi alacakları izleyen bir dönen varlık hesabıdır; borç kalanı verir, tahsilde alacaklandırılır. Personele olan borçlar 335 Personele Borçlar hesabında izlenir.',
        "1 Sıra No'lu MSUGT - 135 Personelden Alacaklar",
    ),
    # düzey 2
    '0049': patch(
        "7/A seçeneğini uygulayan bir üretim işletmesinin banka hesabından, otomatik ödeme talimatı gereği 6.000 ₺ + %20 KDV tutarındaki elektrik faturası ödenmiştir. Ölçümlere göre tüketimin %70'i fabrikada, %30'u yönetim binasında gerçekleşmiştir.\n\nBu ödemenin kaydında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '770 Genel Yönetim Giderleri hesabı 6.000 ₺ borçlandırılır',
            'B': '730 Genel Üretim Giderleri hesabı 4.200 ₺ borçlandırılır',
            'C': '191 İndirilecek KDV hesabı 1.440 ₺ borçlandırılır',
            'D': '102 Bankalar hesabı 6.000 ₺ alacaklandırılır',
            'E': '760 Pazarlama Satış ve Dağıtım Giderleri 1.800 ₺ borçlandırılır',
        },
        'B',
        'Gider, oluştuğu yere göre dağıtılır: fabrika payı 6.000 × %70 = 4.200 ₺ (730), yönetim payı 6.000 × %30 = 1.800 ₺ (770). Kayıt: 730 4.200 ₺, 770 1.800 ₺ ve 191 İndirilecek KDV 1.200 ₺ borç / 102 Bankalar 7.200 ₺ alacak.',
        "1 Sıra No'lu MSUGT - 102 Bankalar / gider hesabı",
    ),
    # düzey 2
    '0050': patch(
        'Küçük bir işletmede tahsilat ve ödemeleri yapan kasa sorumlusu, kasa defterini ve muhasebe kayıtlarını da kendisi tutmaktadır. Kasa sayımı yalnız yıl sonunda yapılmakta, ortaya çıkan küçük fazlalar kaydedilmeden kasada bırakılmaktadır. İşletme yönetimi bu yapıyı düzeltmek istemektedir.\n\nEtkin bir kasa iç kontrolü için aşağıdakilerden hangisi en uygun uygulamadır?',
        {
            'A': 'Zaman kaybını önlemek amacıyla dönem içinde ve dönem sonunda fiili kasa sayımı yapılmaması',
            'B': 'Kayıtları sade tutmak için kasa fazlalarının kaydedilmeyip veznedarın uhdesinde bırakılması',
            'C': 'Kasa işlemlerini yürüten kişi ile bu işlemleri muhasebeleştiren/kontrol eden kişinin farklı olması (görevler ayrılığı)',
            'D': 'Sorumluluğu tek elde toplamak amacıyla tüm kasa, tahsilat, ödeme ve muhasebeleştirme işlemlerinin tek bir yetkili kişide birleştirilmesi',
            'E': 'Hız kazanmak için ödemelerin belge aranmaksızın yapılması ve sonradan da belgelenmemesi',
        },
        'C',
        'İç kontrolün temel ilkelerinden biri **görevler ayrılığı**dır: kasayı yürüten kişi ile kaydı yapan/kontrol eden kişi ayrı olmalıdır. Böylece hata ve suistimal riski azalır; düzenli kasa sayımı da yapılır.',
        'İç kontrol - görevler ayrılığı (kasa)',
    ),
    # düzey 2
    '0051': patch(
        'İşletme, elindeki bir alacak senedini vadesinden önce paraya çevirmek için bankaya iskonto (kırdırma) ettirmiştir. Banka, senet tutarından faiz (iskonto) keserek kalanı işletmenin hesabına geçirmiştir. Bu işlemde bankanın kestiği iskonto tutarı işletme açısından hangi hesaba yazılır?',
        {
            'A': '646 Kambiyo Kârları',
            'B': '102 Bankalar',
            'C': '600 Yurt İçi Satışlar',
            'D': '780 Finansman Giderleri',
            'E': '642 Faiz Gelirleri',
        },
        'D',
        'Senedin vadesinden önce kırdırılmasında bankanın kestiği iskonto (faiz) işletme için bir **finansman gideridir**: **780 Finansman Giderleri**ne borç yazılır. 102 Bankalar net tutarla, 121 Alacak Senetleri nominal tutarla çalışır.',
        "1 Sıra No'lu MSUGT - 780 Finansman Giderleri (senet iskontosu)",
    ),
    # düzey 2
    '0052': patch(
        "İşletmenin kasasında ihracat müşterisinden nakden alınan ve Türkiye'de borsada işlem görmeyen bir yabancı para bulunmaktadır. Dönem sonu değerlemesinde bu para için borsa rayici bulunmadığı belirlenmiştir.\n\nVergi Usul Kanunu'na göre yabancı paralar değerlenirken borsa rayici yoksa hangi kur esas alınır?",
        {
            'A': 'Bir önceki hesap döneminin on iki aylık ortalama döviz kuru',
            'B': 'Dövizin edinildiği faturada satıcı tarafından gösterilen işlem kuru',
            'C': 'Değerleme günü serbest piyasada oluşan en yüksek döviz satış kuru',
            'D': 'İşletmenin kendi muhasebe politikasına göre belirlediği kur',
            'E': "Maliye Bakanlığı'nca tespit ve ilan edilen kur",
        },
        'E',
        "VUK md. 280'e göre yabancı paralar **borsa rayici** ile; borsa rayici yoksa **Maliye Bakanlığı'nca tespit ve ilan edilen kur** ile değerlenir.",
        'VUK md. 280 (yabancı para değerlemesi)',
    ),
    # düzey 2
    '0053': patch(
        'İşletme, elindeki 20.000 ₺ nominal değerli alacak çekini bankaya tahsile vermiş; banka 200 ₺ tahsil komisyonu keserek kalanı hesaba geçirmiştir. Bu işlemin kaydı aşağıdakilerden hangisidir?',
        {
            'A': '102 Bankalar (borç) 19.800 + 653 Komisyon Giderleri (borç) 200 / 101 Alınan Çekler (alacak) 20.000',
            'B': '102 Bankalar (borç) 20.200 / 101 Alınan Çekler (alacak) 20.000 + 642 Faiz Gelirleri (alacak) 200',
            'C': '101 Alınan Çekler (borç) 20.000 / 102 Bankalar (alacak) 19.800 + 653 Komisyon Giderleri (alacak) 200',
            'D': '100 Kasa (borç) 19.800 + 653 Komisyon Giderleri (borç) 200 / 101 Alınan Çekler (alacak) 20.000',
            'E': '102 Bankalar (borç) 20.000 / 101 Alınan Çekler (alacak) 20.000',
        },
        'A',
        'Çek tahsil edilince portföyden çıkar (101 alacak 20.000); bankaya net 19.800 girer, 200 ₺ komisyon gider yazılır: **102 Bankalar (borç) 19.800 + 653 Komisyon Giderleri (borç) 200 / 101 Alınan Çekler (alacak) 20.000**.',
        "1 Sıra No'lu MSUGT - 101 Alınan Çekler / 653 Komisyon Giderleri",
    ),
    # düzey 3
    '0054': patch(
        "'102 Bankalar' hesabı ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
        {
            'A': 'Bankaya para yatırıldığında borçlandırılır.',
            'B': 'Normalde borç kalanı verir.',
            'C': 'Bir kaynak (pasif) hesabı olup alacak kalanı verir.',
            'D': 'Bankadan para çekildiğinde/ödeme yapıldığında alacaklandırılır.',
            'E': 'Bir dönen varlık (aktif) hesabıdır.',
        },
        'C',
        '102 Bankalar bir **aktif (dönen varlık)** hesabıdır; para yatırılınca borçlanır, çekilince alacaklanır ve normalde **borç kalanı** verir. Kaynak (pasif) hesabı değildir.',
        "1 Sıra No'lu MSUGT - 102 Bankalar",
    ),
    # düzey 3
    '0055': patch(
        "Tekdüzen Hesap Planı'nda '10 Hazır Değerler' grubunda yer alan hesaplarla ilgili aşağıdaki eşleştirmelerden hangisi yanlıştır?",
        {
            'A': '112 Kamu Kesimi Tahvil, Senet ve Bonoları → hazır değer',
            'B': '100 Kasa → nakit mevcudu',
            'C': '102 Bankalar → banka mevduatı',
            'D': '101 Alınan Çekler → tahsil için elde tutulan çekler',
            'E': '103 Verilen Çekler ve Ödeme Emirleri (-) → aktifi düzenleyici',
        },
        'A',
        "**112 Kamu Kesimi Tahvil, Senet ve Bonoları**, '11 Menkul Kıymetler' grubundadır; hazır değer değildir. Bu nedenle bu ifade yanlıştır. Hazır Değerler grubu 100, 101, 102, 103 ve 108 hesaplarından oluşur.",
        "1 Sıra No'lu MSUGT - Hazır Değerler / Menkul Kıymetler",
    ),
    # düzey 3
    '0056': patch(
        "İşletmenin 102 Bankalar hesabının borç kalanı 150.000 ₺'dir. Banka hesap özetiyle karşılaştırmada şu durumlar tespit edilmiştir: banka işletme adına 12.000 ₺'lik bir müşteri senedini tahsil etmiş, 300 ₺ hesap işletim ücreti kesmiştir; bu iki işlem kayıtlara geçmemiştir. Ayrıca işletme bir satıcıya yaptığı 1.800 ₺'lik havaleyi kayıtlarına 18.000 ₺ olarak geçirmiştir. Buna göre düzeltmelerden sonra 102 Bankalar hesabının kalanı kaç ₺ olur?",
        {
            'A': '145.500 ₺',
            'B': '162.000 ₺',
            'C': '178.200 ₺',
            'D': '161.700 ₺',
            'E': '177.900 ₺',
        },
        'E',
        'Tahsil edilen senet +12.000, işletim ücreti −300; havale fazla düşüldüğü için +16.200 ₺ geri eklenir: 150.000 + 12.000 − 300 + 16.200 = **177.900 ₺**.',
        'Banka mutabakatı; THP 102, 121, 653',
    ),
    # düzey 2
    '0057': patch(
        'Bir işletmede kasa sayım farklarının muhasebeleştirilmesi değerlendirilmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Kasa noksanı 197'nin borcuna yazılır",
            'B': "Sorumlu personelden tahsil edilecek noksan 135'e aktarılır",
            'C': "Kasa fazlası 397'nin alacağına yazılır",
            'D': 'Kasa fazlası 197 hesabında izlenir',
            'E': "Nedeni bulunamayan kasa fazlası dönem sonunda 679'a aktarılır",
        },
        'D',
        "Kasa **noksanı** 197 Sayım ve Tesellüm Noksanları'nda, kasa **fazlası** 397 Sayım ve Tesellüm Fazlaları'nda izlenir. Nedeni bulunamayan fazla 679'a, noksan 689'a aktarılır; personelden tahsil edilecek noksan 135'e alınır.",
        'THP 100, 197, 397, 135, 679',
    ),
    # düzey 3
    '0058': patch(
        "İşletmenin kasasında 1 $ = 38 ₺ kuruyla kaydedilmiş 2.000 $ bulunmaktadır. Satıcıya olan ve 1 $ = 37 ₺ kuruyla kaydedilmiş 2.000 $'lık borç, kasadaki dövizle ödenmiştir; ödeme günü kur 1 $ = 39 ₺'dir. Buna göre ödeme kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '656 Kambiyo Zararları hesabı 4.000 ₺ borçlandırılır',
            'B': '320 Satıcılar hesabı 76.000 ₺ borçlandırılır',
            'C': '100 Kasa hesabı 78.000 ₺ alacaklandırılır',
            'D': '646 Kambiyo Kârları hesabı 2.000 ₺ alacaklandırılır',
            'E': '656 Kambiyo Zararları hesabı 2.000 ₺ borçlandırılır',
        },
        'E',
        'Kasa kayıtlı değeriyle çıkar (2.000 × 38 = 76.000 ₺), borç kayıtlı değeriyle kapanır (2.000 × 37 = 74.000 ₺). Aradaki 2.000 ₺ kambiyo zararıdır: 320 (borç) 74.000 + **656 (borç) 2.000** / 100 (alacak) 76.000. Ödeme günü kuruyla her iki tarafı değerlemek de aynı net sonucu verir.',
        'VUK m. 280; THP 100, 320, 656',
    ),
    # düzey 2
    '0059': patch(
        'Hazır değerlerle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. 100 Kasa hesabı alacak kalanı verebilir.\n\nII. Yabancı paralar değerleme gününde borsa rayiciyle değerlenir.\n\nIII. Vadesiz ve vadeli mevduatlar 102 Bankalar hesabında izlenir.',
        {
            'A': 'I ve III',
            'B': 'II ve III',
            'C': 'Yalnız II',
            'D': 'I ve II',
            'E': 'Yalnız III',
        },
        'B',
        'II ve III doğrudur. I yanlıştır: kasadan mevcudu aşan ödeme yapılamayacağı için 100 Kasa **alacak kalanı veremez**; böyle bir durum kayıt hatasını gösterir.',
        'VUK m. 280; THP 100, 102',
    ),
    # düzey 3
    '0060': patch(
        'Personele ödenecek net ücret olarak 335 Personele Borçlar hesabına 30.000 ₺ tahakkuk ettirilmiştir. Personelin ay içinde aldığı 4.000 ₺ ücret avansı mahsup edilmiş, kalan tutar banka hesabından ödenmiştir. Buna göre ödeme kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '102 Bankalar hesabı 30.000 ₺ alacaklandırılır',
            'B': '335 Personele Borçlar hesabı 26.000 ₺ borçlandırılır',
            'C': '195 İş Avansları hesabı 4.000 ₺ alacaklandırılır',
            'D': '196 Personel Avansları hesabı 4.000 ₺ borçlandırılır',
            'E': '196 Personel Avansları hesabı 4.000 ₺ alacaklandırılır',
        },
        'E',
        'Kayıt: 335 (borç) 30.000 / **196 (alacak) 4.000** + 102 (alacak) 26.000. Borcun tamamı kapanır; avans mahsupla, kalan bankadan ödenir.',
        'THP 335, 196, 102',
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
    print(f"1 paket / {len(PATCHES)} soru ('Hazir Degerler' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
