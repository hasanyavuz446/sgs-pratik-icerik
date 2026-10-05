#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ticari Alacaklar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.  FM cok adimli tur. 47 soru korundu; standart paketlerine ait 7 TFRS 9/15 sorusu ve birbirini tekrarlayan 6 reeskont sorusu cikarildi (reeskont donem sonu paketinde de isleniyor). Yerine gercek sinav kalibinda 13 soru: police kesidesi ve cevrimi, bankada senet iskontosu (kayit ve dis iskonto tutari), kismen pesin kismen senetli satis, ciro edilmis bononun alinmasi, vade farki ve KDV ile senet yenileme, protesto edilip icraya konan senet, erken odeme iskontosu (611), 120 hesabinin donem hareketlerinden kalan, cekin tahsili, onculler. Kor ogrenci %21. Duzeltme: cozumlerdeki '**X yanlistir**' harf atiflari kaldirildi (yeniden harflendirmede yanlis sikki gosteriyordu).

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: VUK m. 281, 323 · 6102 sayili TTK (police, bono, ciro) · 3065 sayili KDVK m. 24 · Tekduzen Hesap Plani 12, 101, 611, 642, 780
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/finansal_muhasebe/ticari_alacaklar.json"
STYLE_REF = 'SGS Finansal Muhasebe (çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "finmuh-ticalacak-gen-"


def patch(stem, options, answer, solution, ref='VUK m. 323; Tekduzen Hesap Plani 12'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Tekdüzen Hesap Planı'nda '12 Ticari Alacaklar' grubu ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İşletmenin bir yıldan uzun sürede kullanacağı maddi duran varlıklarını ve bunların amortismanını izleyen bir aktif grubudur.',
            'B': 'İşletmenin bankalardaki vadesiz ve vadeli mevduatı ile kasadaki nakit mevcudunu izleyen hazır değerler grubudur.',
            'C': 'İşletmenin ana faaliyet konusuyla (mal/hizmet satışı) ilgili, bir yıl içinde tahsil edilecek alacaklarını izler.',
            'D': 'İşletmenin ortaklarından ve iştiraklerinden olan, esas faaliyet dışı alacaklarını izleyen bir gruptur.',
            'E': 'İşletmenin esas faaliyetiyle ilgili satıcılara olan senetli ve senetsiz borçlarını izleyen bir kaynak (pasif) grubudur.',
        },
        'C',
        '**12 Ticari Alacaklar** grubu, işletmenin esas faaliyeti (mal/hizmet satışı) nedeniyle doğan ve bir yıl içinde tahsil edilecek alacaklarını (120 Alıcılar, 121 Alacak Senetleri vb.) izler.',
        "1 Sıra No'lu MSUGT - Ticari Alacaklar (12)",
    ),
    # düzey 2
    '0002': patch(
        "İşletme, KDV hariç 50.000 ₺'lik malı %20 KDV ile veresiye (senetsiz) satmıştır. Bu satıştan doğan ve '120 Alıcılar' hesabına yazılacak alacak tutarı kaç ₺'dir?",
        {
            'A': '10.000',
            'B': '60.000',
            'C': '70.000',
            'D': '50.000',
            'E': '40.000',
        },
        'B',
        'Alıcının borcu KDV dâhil toplamdır: 50.000 + (50.000 × %20 = 10.000) = **60.000 ₺**. Kayıt: 120 Alıcılar (borç) 60.000 / 600 Yurt İçi Satışlar (alacak) 50.000 + 391 Hesaplanan KDV (alacak) 10.000.',
        "1 Sıra No'lu MSUGT - 120 Alıcılar; 3065 s. KDVK",
    ),
    # düzey 2
    '0003': patch(
        "'129 Şüpheli Ticari Alacaklar Karşılığı (-)' hesabının niteliği ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Konusu kalmayan karşılıkların iptalinde kullanılan, alacak kalanı veren ve dönem kârını artıran bir gelir hesabıdır.',
            'B': 'Bilanço dışında izlenen, borç ve alacak dengesi tutulan bir nazım hesaptır.',
            'C': 'Şüpheli alacakların takibi için katlanılan giderleri izleyen bir maliyet hesabıdır.',
            'D': 'Aktifi düzenleyici (kontr aktif) bir hesaptır; alacak kalanı verir ve şüpheli alacaklardan (-) düşülür.',
            'E': 'İşletmenin senetli borçlarını izleyen bir kaynak (pasif) hesabı olup alacak kalanı verir.',
        },
        'D',
        "**129 Şüpheli Ticari Alacaklar Karşılığı (-)**, aktifi düzenleyici bir hesaptır; **alacak kalanı** verir ve bilançoda 128 Şüpheli Ticari Alacaklar'dan **(-)** düşülerek tahsili beklenen net tutarı gösterir.",
        "1 Sıra No'lu MSUGT - 129 Şüpheli Ticari Alacaklar Karşılığı",
    ),
    # düzey 2
    '0004': patch(
        "İşletme 1 Ekim'de, nominal değeri 120.000 ₺ olan ve yıllık %30 faiz taşıyan bir alacak senedi almıştır. Senedin anaparası ve faizi altı ay sonra birlikte tahsil edilecektir. 31 Aralık'ta üç aylık döneme ait tahakkuk etmiş faiz geliri kaç ₺'dir?",
        {
            'A': '9.000 ₺',
            'B': '15.000 ₺',
            'C': '36.000 ₺',
            'D': '18.000 ₺',
            'E': '12.000 ₺',
        },
        'A',
        "Üç aylık faiz 120.000 × %30 × 3/12 = **9.000 ₺**dir. Dönemsellik gereği bu tutar 31 Aralık'ta faiz geliri olarak tahakkuk ettirilir; kalan üç aylık faiz izleyen döneme aittir.",
        "Dönemsellik Kavramı; 1 Sıra No'lu MSUGT - 181 Gelir Tahakkukları ve 642 Faiz Gelirleri",
    ),
    # düzey 2
    '0005': patch(
        "İşletme, vadesi gelen 20.000 ₺'lik alacak senedini tahsil için bankaya vermiştir; senet henüz tahsil edilmemiştir. Tahsile verilen bu senetlerin izlenmesiyle ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Senet tahsile verilmekle işletmenin varlığı olmaktan çıkar; nominal tutarı üzerinden doğrudan 780 Finansman Giderleri hesabına borç yazılarak dönem gideri olarak kayıtlardan çıkarılır.',
            'B': 'Senet, tahsili bankaya bırakıldığından artık bir ticari borç niteliği kazanır ve 320 Satıcılar hesabına aktarılarak vade sonuna kadar bu hesapta takip edilir.',
            'C': "Senet hâlâ işletmenin alacağıdır; genellikle 121 Alacak Senetleri altında 'Tahsildeki Senetler' gibi bir alt hesapta izlenir, tahsil edilince 102 Bankalar'a aktarılır.",
            'D': 'Senet tahsile verildiği anda bilanço hesaplarından çıkarılıp nazım hesaplarda izlenir; dönem sonu bilançosunda bu alacak görünmez.',
            'E': 'Senet, işletmenin bankaya olan bir borcuna dönüştüğü için 103 Verilen Çekler ve Ödeme Emirleri hesabına aktarılır ve banka tahsil edene kadar bu kaynak hesapta izlenir.',
        },
        'C',
        "Tahsile verilen senet hâlâ işletmenin **alacağıdır**; portföyden çıkıp genellikle 121'in bir alt hesabında (Tahsildeki Senetler) izlenir. Banka tahsil edince tutar **102 Bankalar**'a geçer.",
        "1 Sıra No'lu MSUGT - 121 Alacak Senetleri (tahsildeki senetler)",
    ),
    # düzey 2
    '0006': patch(
        "VUK'a göre vadesi gelmemiş bir alacak senedinin reeskontunda kullanılacak faiz oranıyla ilgili aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': 'Senette faiz oranı açıklanmışsa bu oran, açıklanmamışsa Türkiye Cumhuriyet Merkez Bankasının resmî iskonto oranı kullanılır.',
            'B': 'Senette yazılı oran dikkate alınmaz; enflasyon oranı kullanılır.',
            'C': 'Faiz oranı bulunmayan senetlere reeskont uygulanamaz.',
            'D': 'Senette oran yazsa bile işletmenin banka kredi faizi kullanılır.',
            'E': 'Alacaklının kendi belirlediği oran kullanılır.',
        },
        'A',
        'VUK 281 uyarınca senette faiz oranı açıklanmışsa **senetteki oran** esas alınır. Oran açıklanmamışsa değerleme gününde geçerli **TCMB resmî iskonto oranı** kullanılır.',
        '213 sayılı VUK md. 281',
    ),
    # düzey 3
    '0007': patch(
        "Vergi Usul Kanunu'na göre bir ticari alacağın 'şüpheli alacak' sayılıp karşılık ayrılabilmesi için aşağıdaki koşullardan hangisi gerekli değildir?",
        {
            'A': 'Alacağın belirli (tahakkuk etmiş) bir alacak olması',
            'B': 'Alacağın teminatsız (teminata bağlanmamış) kısmının bulunması',
            'C': 'Alacağın dava veya icra safhasında olması ya da protesto edilmiş/yazıyla birden fazla istenmiş olması',
            'D': 'Borçlunun iflas etmiş ve alacağın tahsilinin imkânsız hâle gelmiş olması',
            'E': 'Alacağın ticari veya zirai kazancın elde edilmesiyle ilgili olması',
        },
        'D',
        "Şüpheli alacakta tahsilin **kesin imkânsızlığı aranmaz** — henüz belirsizlik/şüphe yeterlidir (dava/icra safhası vb.). Kesin olarak tahsili imkânsız hâle gelen alacak ise 'değersiz alacak'tır (VUK 322).",
        'VUK md. 323 (şüpheli alacak koşulları)',
    ),
    # düzey 2
    '0008': patch(
        "Daha önce şüpheli hâle gelip '128 Şüpheli Ticari Alacaklar'da izlenen ve tamamına karşılık ayrılan 24.000 ₺'lik alacak, beklenmedik biçimde borçlusundan nakden tahsil edilmiştir. Bu tahsilata ilişkin (alacağın kapatılması) kayıt aşağıdakilerden hangisidir?",
        {
            'A': '100 Kasa (borç) 24.000 / 644 Konusu Kalmayan Karşılıklar (alacak) 24.000',
            'B': '100 Kasa (borç) 24.000 / 128 Şüpheli Ticari Alacaklar (alacak) 24.000',
            'C': '100 Kasa (borç) 24.000 / 120 Alıcılar (alacak) 24.000',
            'D': '128 Şüpheli Ticari Alacaklar (borç) 24.000 / 100 Kasa (alacak) 24.000',
            'E': '129 Şüpheli Ticari Alacaklar Karşılığı (borç) 24.000 / 100 Kasa (alacak) 24.000',
        },
        'B',
        'Tahsilatla şüpheli alacak kapanır: **100 Kasa (borç) 24.000 / 128 Şüpheli Ticari Alacaklar (alacak) 24.000**. Ayrıca konusu kalmayan karşılık, ayrı bir kayıtla (129 / 644) gelir yazılarak iptal edilir.',
        "1 Sıra No'lu MSUGT - 128 / 100",
    ),
    # düzey 2
    '0009': patch(
        "Vergi Usul Kanunu'na göre 'değersiz alacak' ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İşletmenin ortaklarına ve iştiraklerine olan, esas faaliyet dışı nitelikteki senetsiz borcudur.',
            'B': 'Dava veya icra safhasında bulunan ve bu nedenle tahsili şüpheli hâle gelmiş ticari alacaktır.',
            'C': 'Satış anında bedeli peşin tahsil edildiği için senede veya vadeye bağlanmamış alacaktır.',
            'D': 'Vadesi henüz gelmemiş, tahsilinde bir sorun görülmeyen ve reeskonta tabi tutulan senetli alacaktır.',
            'E': 'Kazai bir hükme veya kanaat verici bir vesikaya göre tahsiline artık imkân kalmayan alacaktır.',
        },
        'E',
        "**Değersiz alacak** (VUK 322), kazai bir hükme veya kanaat verici bir vesikaya göre **tahsiline artık imkân kalmayan** alacaktır; değersizleştiği dönemde zarar yazılır. Dava/icra safhasındaki alacak ise 'şüpheli' alacaktır.",
        'VUK md. 322 (değersiz alacak)',
    ),
    # düzey 2
    '0010': patch(
        "Nominal değeri 300.000 ₺, vadesine 80 gün kalan bir alacak senedi için yıllık %50 faiz oranıyla iç iskonto yöntemine göre reeskont tutarı kaç ₺'dir?\n\n(Reeskont = Nominal × Faiz × Gün ÷ [36.000 + (Faiz × Gün)])",
        {
            'A': '46.500',
            'B': '30.000',
            'C': '34.500',
            'D': '33.000',
            'E': '36.000',
        },
        'B',
        'Faiz × Gün = 50 × 80 = 4.000. Reeskont = 300.000 × 4.000 ÷ (36.000 + 4.000) = 300.000 × 4.000 ÷ 40.000 = 300.000 × 0,1 = **30.000 ₺**. Peşin değer = 270.000 ₺.',
        'VUK md. 281 - iç iskonto formülü',
    ),
    # düzey 3
    '0011': patch(
        "Nominal değeri 240.000 ₺, vadesine 200 gün kalan bir alacak senedi için yıllık %36 faiz oranıyla iç iskonto yöntemine göre reeskont tutarı kaç ₺'dir?\n\n(Reeskont = Nominal × Faiz × Gün ÷ [36.000 + (Faiz × Gün)])",
        {
            'A': '40.000',
            'B': '43.200',
            'C': '20.000',
            'D': '48.000',
            'E': '36.000',
        },
        'A',
        'Faiz × Gün = 36 × 200 = 7.200. Reeskont = 240.000 × 7.200 ÷ (36.000 + 7.200) = 240.000 × 7.200 ÷ 43.200 = 240.000 ÷ 6 = **40.000 ₺**. Peşin değer = 200.000 ₺.',
        'VUK md. 281 - iç iskonto formülü',
    ),
    # düzey 2
    '0012': patch(
        'Bir işletmenin şüpheli hâle gelen alacağı için ayıracağı karşılık tutarı ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Karşılık, senetli alacaklar için ayrılabilir, senetsizler için ayrılamaz.',
            'B': 'Karşılık, satış hasılatı üzerinden ayrılır.',
            'C': 'Karşılık, alacağın KDV hariç kısmı üzerinden ayrılır.',
            'D': 'Karşılık, tahsil edilemeyen alacağın (KDV dâhil) değeri üzerinden ayrılabilir.',
            'E': 'Karşılık, alacağın iki katı üzerinden ayrılır.',
        },
        'D',
        'Tahsil edilemeyen alacak **KDV dâhil** tutardır (müşteri KDV dâhil borçludur); bu nedenle şüpheli alacak karşılığı KDV dâhil değer üzerinden ayrılabilir.',
        'VUK md. 323; 3065 s. KDVK',
    ),
    # düzey 3
    '0013': patch(
        'Aşağıdaki uygulamalardan hangileri şüpheli alacak karşılığı ayrılmasını gerektirir?\n\nI. Hakkında icra takibi başlatılmış ticari alacak\n\nII. Dava safhasına gelmiş ticari alacak\n\nIII. Vadesi henüz gelmemiş ve tahsilinde sorun görülmeyen alacak\n\nIV. Protesto edilmiş ancak dava/icraya değmeyecek kadar küçük, birden fazla yazıyla istenmiş alacak',
        {
            'A': 'III ve IV',
            'B': 'Yalnız I',
            'C': 'I, II ve IV',
            'D': 'I ve II',
            'E': 'I, II, III ve IV',
        },
        'C',
        "**I, II ve IV** VUK'taki şüpheli alacak koşullarını karşılar (dava/icra safhası ya da protesto/yazıyla birden fazla isteme). **III** (vadesi gelmemiş, sorunsuz alacak) şüpheli değildir; karşılık gerektirmez.",
        'VUK md. 323 (şüpheli alacak koşulları)',
    ),
    # düzey 2
    '0014': patch(
        "İşletme, daha önce tamamına 24.000 ₺ karşılık ayırdığı şüpheli alacağının 24.000 ₺'sini tahsil etmiştir. Bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Tahsil edilen alacak, kapatılmak yerine yeniden 120 Alıcılar hesabına aktarılarak izlenmeye devam edilir.',
            'B': 'Tahsilat nedeniyle 654 Karşılık Giderleri yeniden borçlandırılıp 129 hesabı yükseltilerek kayıt tamamlanır.',
            'C': 'Tahsil kaydı (100/128) yapılır; daha önce ayrılan karşılık hesabına dokunulmaz.',
            'D': 'Hem alacak tahsil kaydı (100/128) yapılır hem de konusu kalmayan karşılık gelir yazılarak iptal edilir (129/644).',
            'E': '654 Karşılık Giderleri borçlandırılarak ayrılan karşılık tutarı bir kat daha artırılır.',
        },
        'D',
        'Tahsilatla iki kayıt yapılır: **100 Kasa/102 (borç) / 128 (alacak)** (alacak kapanır) ve **129 (borç) / 644 Konusu Kalmayan Karşılıklar (alacak)** (karşılık gelir yazılarak iptal edilir).',
        "1 Sıra No'lu MSUGT - 128/129/644",
    ),
    # düzey 2
    '0015': patch(
        "Vadesi gelen 60.000 ₺ nominal değerli alacak senedi, borçluyla yapılan anlaşma sonucu 6.000 ₺ vade farkı eklenerek yeni bir senetle değiştirilmiştir. Yeni senedin nominal değeri ve yenileme tarihinde muhasebeleştirilecek finansman geliri sırasıyla kaç ₺'dir?",
        {
            'A': '54.000 ₺ ve 6.000 ₺',
            'B': '60.000 ₺ ve 0 ₺',
            'C': '66.000 ₺ ve 60.000 ₺',
            'D': '60.000 ₺ ve 6.000 ₺',
            'E': '66.000 ₺ ve 6.000 ₺',
        },
        'E',
        'Eski 60.000 ₺ senet kapatılır; anapara ile 6.000 ₺ finansman gelirini içeren **66.000 ₺ nominal değerli yeni senet** alınır. Kayıt özünde yeni 121 (borç) 66.000 / eski 121 (alacak) 60.000 + ilgili finansman geliri (alacak) 6.000 şeklindedir.',
        "1 Sıra No'lu MSUGT - 121 Alacak Senetleri ve finansman gelirleri",
    ),
    # düzey 3
    '0016': patch(
        "A İşletmesi, satıcısı B İşletmesine olan 40.000 ₺ senetsiz borcuna karşılık, kendisine 40.000 ₺ senetsiz borcu bulunan müşterisi C adına bir poliçe düzenlemiştir. C poliçeyi kabul etmiş ve poliçe B'ye teslim edilmiştir. Buna göre A İşletmesinin yapacağı kayıt aşağıdakilerden hangisidir?",
        {
            'A': '320 (borç) 40.000 / 321 (alacak) 40.000',
            'B': '121 (borç) 40.000 / 120 (alacak) 40.000',
            'C': '320 (borç) 40.000 / 120 (alacak) 40.000',
            'D': '120 (borç) 40.000 / 320 (alacak) 40.000',
            'E': '320 (borç) 40.000 / 121 (alacak) 40.000',
        },
        'C',
        "Poliçeyle A'nın C'den olan alacağı B'ye aktarılır: A'nın satıcıya borcu (320) ve müşteriden alacağı (120) aynı anda kapanır. Senet A'nın portföyüne girmediği için 121 kullanılmaz; A borç senedi vermediği için 321 de kullanılmaz. Poliçeyi alan B ise 121'i borçlandırır.",
        '6102 sayılı TTK m. 671 vd. (poliçe); THP 120, 320',
    ),
    # düzey 3
    '0017': patch(
        "İşletme 60.000 ₺ + %20 KDV tutarındaki ticari malı satmıştır. KDV ile birlikte satış bedelinin 12.000 ₺'si kasaya nakden tahsil edilmiş, kalan tutar için müşteriden senet alınmıştır. Buna göre satış kaydında aşağıdakilerden hangisi yer almaz?",
        {
            'A': '121 Alacak Senetleri hesabı 48.000 ₺ borçlandırılır',
            'B': '120 Alıcılar hesabı 48.000 ₺ borçlandırılır',
            'C': '100 Kasa hesabı 24.000 ₺ borçlandırılır',
            'D': '600 Yurt İçi Satışlar hesabı 60.000 ₺ alacaklandırılır',
            'E': '391 Hesaplanan KDV hesabı 12.000 ₺ alacaklandırılır',
        },
        'B',
        'Nakit tahsilat KDV (12.000 ₺) + 12.000 = 24.000 ₺. Kayıt: 100 (borç) 24.000 + 121 (borç) 48.000 / 600 (alacak) 60.000 + 391 (alacak) 12.000. Kalan tutar senede bağlandığı için senetsiz alacak hesabı 120 kullanılmaz.',
        'THP 100, 121, 600, 391',
    ),
    # düzey 2
    '0018': patch(
        'Bir işletme portföyündeki müşteri senedini satıcısına olan borcuna karşılık ciro etmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ciro edilen senet işletmenin aktifinde kalmaya devam eder',
            'B': 'Ciro kaydında 121 Alacak Senetleri alacaklandırılır',
            'C': 'Senet satıcıya olan borca karşılık verilebilir',
            'D': 'Senet vadesinde ödenmezse ciro eden işletmeye başvurulabilir',
            'E': 'Ciro, işletmenin borç senedi düzenlemesi demek değildir',
        },
        'A',
        'Ciroyla senet portföyden çıkar: 320 (borç) / 121 (alacak). Ciro eden işletme senet ödenmezse başvuru sorumluluğu taşır (bu risk nazım hesaplarda izlenebilir); ancak senet **aktifte kalmaz**.',
        '6102 sayılı TTK (ciro); THP 121',
    ),
    # düzey 3
    '0019': patch(
        "Bir işletmenin 120 Alıcılar hesabının dönem başı borç kalanı 80.000 ₺'dir. Dönem içinde KDV dâhil 360.000 ₺ kredili satış yapılmış, KDV dâhil 24.000 ₺'lik mal iade alınmış, müşterilerden 250.000 ₺ tahsilat yapılmış ve 30.000 ₺'lik senetsiz alacak için müşteriden senet alınmıştır. Buna göre 120 Alıcılar hesabının dönem sonu kalanı kaç ₺'dir?",
        {
            'A': '160.000 ₺',
            'B': '136.000 ₺',
            'C': '184.000 ₺',
            'D': '166.000 ₺',
            'E': '56.000 ₺',
        },
        'B',
        "80.000 + 360.000 − 24.000 − 250.000 − 30.000 = **136.000 ₺**. İade ve tahsilat alacağı azaltır; senet alınan kısım 121'e aktarıldığı için 120'den düşülür.",
        'THP 120',
    ),
    # düzey 2
    '0020': patch(
        'Ticari alacaklarla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Esas faaliyetten doğan senetsiz alacaklar 120 Alıcılar hesabında izlenir.\n\nII. Vadesi bir yıldan uzun olan senetli ticari alacaklar 121 Alacak Senetleri hesabında izlenir.\n\nIII. Personelden olan alacaklar 12 Ticari Alacaklar grubunda izlenir.',
        {
            'A': 'I ve III',
            'B': 'II ve III',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'Yalnız II',
        },
        'C',
        "Yalnız I doğrudur. Vadesi bir yıldan uzun senetli ticari alacaklar **221 Alacak Senetleri**'nde (uzun vadeli), personelden alacaklar 13 Diğer Alacaklar grubunda (135) izlenir.",
        'THP 12 Ticari Alacaklar',
    ),
    # düzey 2
    '0021': patch(
        'İşletmenin esas faaliyetinden doğan, herhangi bir senede bağlanmamış (senetsiz) ticari alacakları hangi hesapta izlenir?',
        {
            'A': '101 Alınan Çekler',
            'B': '136 Diğer Çeşitli Alacaklar',
            'C': '320 Satıcılar',
            'D': '121 Alacak Senetleri',
            'E': '120 Alıcılar',
        },
        'E',
        "Senede bağlanmamış ticari alacaklar **120 Alıcılar** hesabında izlenir. Senede bağlananlar 121 Alacak Senetleri'nde takip edilir.",
        "1 Sıra No'lu MSUGT - 120 Alıcılar",
    ),
    # düzey 2
    '0022': patch(
        "İşletme, sekiz ay sonra geri alınacak 30.000 ₺ kira depozitosu ile üç yıl sonra geri alınacak 80.000 ₺ teminat vermiştir. Tekdüzen Hesap Planı'na göre bu tutarlar sırasıyla hangi hesaplarda izlenir?",
        {
            'A': '126 Verilen Depozito ve Teminatlar ve 226 Verilen Depozito ve Teminatlar',
            'B': '136 Diğer Çeşitli Alacaklar ve 236 Diğer Çeşitli Alacaklar',
            'C': '226 Verilen Depozito ve Teminatlar ve 126 Verilen Depozito ve Teminatlar',
            'D': '126 Verilen Depozito ve Teminatlar ve 126 Verilen Depozito ve Teminatlar',
            'E': '120 Alıcılar ve 220 Alıcılar',
        },
        'A',
        'Bir yıl içinde geri alınacak depozito **126 Verilen Depozito ve Teminatlar** hesabında dönen varlık; bir yıldan uzun vadeli olan ise **226 Verilen Depozito ve Teminatlar** hesabında duran varlık olarak izlenir.',
        "1 Sıra No'lu MSUGT - 126 ve 226 Verilen Depozito ve Teminatlar",
    ),
    # düzey 2
    '0023': patch(
        'İşletmenin, esas faaliyeti dışındaki işlemlerden (ör. iştirak/personel dışı üçüncü kişilerden) doğan ve senede bağlı olmayan çeşitli alacakları öncelikle hangi grupta izlenir?',
        {
            'A': '15 Stoklar',
            'B': '32 Ticari Borçlar',
            'C': '12 Ticari Alacaklar',
            'D': '13 Diğer Alacaklar',
            'E': '25 Maddi Duran Varlıklar',
        },
        'D',
        "Esas faaliyet dışı işlemlerden doğan alacaklar **13 Diğer Alacaklar** grubunda (ör. 136 Diğer Çeşitli Alacaklar) izlenir. Esas faaliyetten (mal/hizmet satışı) doğanlar ise 12 Ticari Alacaklar'dadır.",
        "1 Sıra No'lu MSUGT - Ticari/Diğer Alacaklar ayrımı",
    ),
    # düzey 2
    '0024': patch(
        'Bir müşteri, senetsiz ticari borcuna karşılık işletmeye bir çek vermiştir. İşletme açısından bu çek hangi hesapta izlenir ve bu hesap hangi gruptadır?',
        {
            'A': '108 Diğer Hazır Değerler — Hazır Değerler',
            'B': '101 Alınan Çekler — Hazır Değerler',
            'C': '121 Alacak Senetleri — Ticari Alacaklar',
            'D': '103 Verilen Çekler ve Ödeme Emirleri — Hazır Değerler',
            'E': '120 Alıcılar — Ticari Alacaklar',
        },
        'B',
        'Alınan çekler **101 Alınan Çekler** hesabında ve **10 Hazır Değerler** grubunda izlenir (çek bir ödeme aracıdır). Senet ise 121 Alacak Senetleri (Ticari Alacaklar) grubundadır; ikisi karıştırılmamalıdır.',
        "1 Sıra No'lu MSUGT - 101 Alınan Çekler / 121 Alacak Senetleri",
    ),
    # düzey 2
    '0025': patch(
        "Aşağıdaki hesaplardan hangisi '12 Ticari Alacaklar' grubunda yer almaz?",
        {
            'A': '128 Şüpheli Ticari Alacaklar',
            'B': '126 Verilen Depozito ve Teminatlar',
            'C': '120 Alıcılar',
            'D': '131 Ortaklardan Alacaklar',
            'E': '121 Alacak Senetleri',
        },
        'D',
        "**131 Ortaklardan Alacaklar**, '13 Diğer Alacaklar' grubundadır; esas faaliyetten doğmadığı için Ticari Alacaklar değildir. Diğerleri 12 Ticari Alacaklar grubundadır.",
        "1 Sıra No'lu MSUGT - 12/13 grupları",
    ),
    # düzey 3
    '0026': patch(
        "Nominal değeri 200.000 ₺, vadesine 100 gün kalan bir alacak senedi için yıllık %40 faiz oranıyla iç iskonto yöntemine göre reeskont tutarı kaç ₺'dir?\n\n(İç iskonto: Reeskont = Nominal × Faiz × Gün ÷ [36.000 + (Faiz × Gün)])",
        {
            'A': '16.000',
            'B': '8.000',
            'C': '18.000',
            'D': '14.000',
            'E': '20.000',
        },
        'E',
        'Reeskont = 200.000 × 40 × 100 ÷ [36.000 + (40 × 100)] = 200.000 × 4.000 ÷ 40.000 = **20.000 ₺**. Senedin peşin (tasarruf) değeri = 200.000 − 20.000 = 180.000 ₺.',
        'VUK md. 281 - iç iskonto (reeskont) formülü',
    ),
    # düzey 2
    '0027': patch(
        "İşletmenin 120 Alıcılar hesabında izlenen 24.000 ₺'lik (KDV dâhil) alacağı, borçlu hakkında icra takibi başlatılmasıyla şüpheli hâle gelmiştir. Alacağın şüpheli hesaba alınmasına ilişkin kayıt aşağıdakilerden hangisidir?",
        {
            'A': '654 Karşılık Giderleri (borç) 24.000 / 129 Şüpheli Ticari Alacaklar Karşılığı (alacak) 24.000',
            'B': '128 Şüpheli Ticari Alacaklar (borç) 24.000 / 129 Şüpheli Ticari Alacaklar Karşılığı (alacak) 24.000',
            'C': '128 Şüpheli Ticari Alacaklar (borç) 24.000 / 120 Alıcılar (alacak) 24.000',
            'D': '689 Diğer Olağandışı Gider (borç) 24.000 / 120 Alıcılar (alacak) 24.000',
            'E': '120 Alıcılar (borç) 24.000 / 128 Şüpheli Ticari Alacaklar (alacak) 24.000',
        },
        'C',
        'Alacak önce şüpheli hesaba alınır: **128 Şüpheli Ticari Alacaklar (borç) 24.000 / 120 Alıcılar (alacak) 24.000**. Karşılık ayırma (654/129) bundan sonraki ayrı bir kayıttır.',
        "1 Sıra No'lu MSUGT - 128; VUK md. 323",
    ),
    # düzey 2
    '0028': patch(
        "Tamamı için karşılık ayrılmış 24.000 ₺ tutarındaki şüpheli ticari alacağın 9.000 ₺'si banka yoluyla tahsil edilmiştir. Kalan alacağın şüpheli niteliği sürmektedir. Tahsilat ve karşılık bakımından en uygun işlem hangisidir?",
        {
            'A': "102/128 kaydıyla 9.000 ₺ alacak kapatılır; aynı tutardaki karşılık 129/644 kaydıyla iptal edilir, kalan 15.000 ₺ 128 ve 129'da izlenir.",
            'B': '102 Bankalar borçlandırılır; 128 ve 129 hesapları değiştirilmez.',
            'C': 'Kalan 15.000 ₺ de tahsil edilmiş sayılarak bütün hesaplar kapatılır.',
            'D': 'Karşılığın tamamı 24.000 ₺ gelir yazılarak iptal edilir; 128 hesabı değiştirilmez.',
            'E': 'Tahsil edilen 9.000 ₺ için yeniden 654 Karşılık Giderleri borçlandırılır.',
        },
        'A',
        'Tahsil edilen bölüm için **102 Bankalar (borç) 9.000 / 128 Şüpheli Ticari Alacaklar (alacak) 9.000** kaydı yapılır. Bu bölüme ait karşılık da **129 (borç) 9.000 / 644 (alacak) 9.000** ile iptal edilir. Tahsil edilmeyen ve şüpheli niteliği süren 15.000 ₺ hem 128 hem 129 hesaplarında kalır.',
        "1 Sıra No'lu MSUGT - 128, 129 ve 644 hesaplarının işleyişi",
    ),
    # düzey 2
    '0029': patch(
        "İşletmenin 120 Alıcılar'da izlenen 10.000 ₺'lik alacağı, borçlunun kanaat verici bir vesikayla tahsilinin imkânsız olduğu anlaşıldığından değersiz hâle gelmiştir. Alacak için daha önce karşılık ayrılmamıştır. Bu değersiz alacağın kaydı aşağıdakilerden hangisidir?",
        {
            'A': '120 Alıcılar (borç) 10.000 / 689 Diğer Olağandışı Gider ve Zararlar (alacak) 10.000',
            'B': '689 Diğer Olağandışı Gider ve Zararlar (borç) 10.000 / 120 Alıcılar (alacak) 10.000',
            'C': '129 Şüpheli Ticari Alacaklar Karşılığı (borç) 10.000 / 120 Alıcılar (alacak) 10.000',
            'D': '128 Şüpheli Ticari Alacaklar (borç) 10.000 / 120 Alıcılar (alacak) 10.000',
            'E': '644 Konusu Kalmayan Karşılıklar (borç) 10.000 / 120 Alıcılar (alacak) 10.000',
        },
        'B',
        'Karşılık ayrılmamış değersiz alacak doğrudan zarar yazılır: **689 Diğer Olağandışı Gider ve Zararlar (borç) 10.000 / 120 Alıcılar (alacak) 10.000**. (Karşılık ayrılmış olsaydı 129 kullanılırdı.)',
        "VUK md. 322; 1 Sıra No'lu MSUGT - 689",
    ),
    # düzey 2
    '0030': patch(
        'İşletme, 40.000 ₺ + %20 KDV tutarındaki malı, karşılığında alıcıdan senet alarak (senetli) satmıştır. Bu satışın kaydı aşağıdakilerden hangisidir?',
        {
            'A': '121 Alacak Senetleri (borç) 48.000 / 600 Yurt İçi Satışlar (alacak) 40.000 + 391 Hesaplanan KDV (alacak) 8.000',
            'B': '121 Alacak Senetleri (borç) 40.000 / 600 Yurt İçi Satışlar (alacak) 40.000',
            'C': '600 Yurt İçi Satışlar (borç) 48.000 / 121 Alacak Senetleri (alacak) 48.000',
            'D': '120 Alıcılar (borç) 48.000 / 600 Yurt İçi Satışlar (alacak) 40.000 + 391 Hesaplanan KDV (alacak) 8.000',
            'E': '121 Alacak Senetleri (borç) 48.000 / 600 Yurt İçi Satışlar (alacak) 48.000',
        },
        'A',
        'Senet karşılığı satışta senetli alacak KDV dâhil doğar: **121 Alacak Senetleri (borç) 48.000** (40.000 + %20 KDV 8.000) / 600 Yurt İçi Satışlar (alacak) 40.000 + 391 Hesaplanan KDV (alacak) 8.000.',
        "1 Sıra No'lu MSUGT - 121; 3065 s. KDVK",
    ),
    # düzey 2
    '0031': patch(
        "Vergi Usul Kanunu'na göre teminata (rehin, ipotek vb.) bağlanmış bir ticari alacak için şüpheli alacak karşılığı nasıl ayrılır?",
        {
            'A': 'Teminatlı olsun olmasın alacağın tamamı için, KDV dâhil tutar üzerinden karşılık ayrılır.',
            'B': 'Karşılık, açık kalan kısım için değil, alınan teminatın tutarı kadar bir tutar için ayrılır.',
            'C': 'Teminatlı alacaklarda tahsil riski yüksek sayıldığından karşılık, açık kısmın iki katı ayrılır.',
            'D': 'Karşılık, alacağın teminatla karşılanamayan (açık) kısmı için ayrılabilir.',
            'E': 'Teminata bağlanmış alacaklar için şüpheli alacak karşılığı ayrılamaz.',
        },
        'D',
        'Teminata bağlı alacaklarda karşılık, alacağın **teminatla karşılanamayan (açık) kısmı** için ayrılabilir; teminatlı kısım tahsil güvencesi altında sayıldığından o kısma karşılık ayrılmaz.',
        'VUK md. 323 (teminatlı alacaklarda karşılık)',
    ),
    # düzey 3
    '0032': patch(
        "İşletme, bilanço tarihinde 128 Şüpheli Ticari Alacaklar hesabında 50.000 ₺, 129 Şüpheli Ticari Alacaklar Karşılığı hesabında 50.000 ₺ tutar bulunmaktadır. Bu şüpheli alacakların bilançoda gösterileceği net tutar kaç ₺'dir?",
        {
            'A': 'Bilançoda gösterilmez',
            'B': '50.000',
            'C': '25.000',
            'D': '100.000',
            'E': '0',
        },
        'E',
        'Şüpheli alacaklar bilançoda **128 − 129** (net) gösterilir: 50.000 − 50.000 = **0 ₺**. Tamamına karşılık ayrıldığından net tahsili beklenen tutar sıfırdır (ihtiyatlılık).',
        "1 Sıra No'lu MSUGT - 128/129 net gösterim",
    ),
    # düzey 2
    '0033': patch(
        "İşletme, elindeki 50.000 ₺'lik alacak senedinin 20.000 ₺'lik kısmını borçludan nakden kısmen tahsil etmiş, kalan için yeni senet düzenlenmemiştir (senedin bir kısmı ödenmiştir). Yalnızca tahsil edilen kısma ilişkin kayıt aşağıdakilerden hangisidir?",
        {
            'A': '128 Şüpheli Ticari Alacaklar (borç) 20.000 / 121 Alacak Senetleri (alacak) 20.000',
            'B': '121 Alacak Senetleri (borç) 20.000 / 100 Kasa (alacak) 20.000',
            'C': '100 Kasa (borç) 20.000 / 121 Alacak Senetleri (alacak) 20.000',
            'D': '100 Kasa (borç) 50.000 / 121 Alacak Senetleri (alacak) 50.000',
            'E': '100 Kasa (borç) 20.000 / 120 Alıcılar (alacak) 20.000',
        },
        'C',
        'Tahsil edilen kısım kadar senetli alacak azalır: **100 Kasa (borç) 20.000 / 121 Alacak Senetleri (alacak) 20.000**. Kalan 30.000 ₺ senetli alacak olarak izlenmeye devam eder.',
        "1 Sıra No'lu MSUGT - 121 Alacak Senetleri",
    ),
    # düzey 2
    '0034': patch(
        'Ticari alacaklarda tahsilat riskini azaltmaya yönelik en uygun iç kontrol bileşimi hangisidir?',
        {
            'A': 'Satış temsilcisinin kredi limiti belirleme, sevkiyat ve tahsilat kayıtlarını tek başına yürütmesi',
            'B': 'Müşteri limitlerinin satış gerçekleştikten sonra belgesiz biçimde artırılması',
            'C': 'Vadesi geçen alacakların yaşlandırma raporundan çıkarılması',
            'D': 'Alacak mutabakatlarının kaydı yapan personelce hazırlanması ve farkların araştırılmaması',
            'E': 'Kredi onayının satıştan ayrılması, müşteri limitlerinin sistemde izlenmesi, yaşlandırma raporlarının incelenmesi ve hesap ekstrelerinin müşterilere gönderilmesi',
        },
        'E',
        'Kredi onayının satış işlevinden ayrılması, tanımlı limitlerin sistemce izlenmesi, gecikmelerin yaşlandırma raporuyla takip edilmesi ve müşteri mutabakatı; hem yetkisiz satış hem de tahsil edilememe riskini azaltan birbirini tamamlayıcı kontrollerdir.',
        'Muhasebe Bilgi Sistemleri - satış ve alacak döngüsü kontrolleri',
    ),
    # düzey 2
    '0035': patch(
        'Karşılık ayrılmamış bir alacağın değersiz hâle gelmesi durumunda, doğrudan zarar yazılması işletmenin dönem sonucunu nasıl etkiler?',
        {
            'A': 'Dönem kârını azaltır (gider/zarar yazıldığı için).',
            'B': 'Dönem sonucunu etkilemez; bir bilanço aktarımıdır.',
            'C': 'Hesaplanan KDV tutarını artırır, kârı etkilemez.',
            'D': 'Kârı etkilemeden özkaynakları doğrudan artırır.',
            'E': 'Dönem kârını artırır (gelir olarak yazıldığı için).',
        },
        'A',
        'Karşılık ayrılmamış değersiz alacak doğrudan **gider/zarar** (689) yazıldığından dönem kârını **azaltır**. (Karşılık daha önce ayrılmış olsaydı, zarar önceki dönemde tahakkuk etmiş olurdu.)',
        'VUK md. 322; değersiz alacağın sonuca etkisi',
    ),
    # düzey 3
    '0036': patch(
        'Ticari alacaklarla ilgili aşağıdaki hesap–açıklama eşleştirmelerinden hangisi yanlıştır?',
        {
            'A': '128 Şüpheli Ticari Alacaklar → Tahsili şüpheli hâle gelen alacaklar',
            'B': '120 Alıcılar → Senetsiz ticari alacaklar',
            'C': '122 Alacak Senetleri Reeskontu (-) → Bir gelir hesabı',
            'D': '129 Şüpheli Ticari Alacaklar Karşılığı (-) → Aktifi düzenleyici hesap',
            'E': '121 Alacak Senetleri → Senetli ticari alacaklar',
        },
        'C',
        "122 Alacak Senetleri Reeskontu (-) bir gelir hesabı değil, **aktifi düzenleyici** bir hesaptır (alacak senetlerinden düşülür). Reeskontun gelir/gider yönü 647/657'de izlenir.",
        "1 Sıra No'lu MSUGT - Ticari Alacaklar hesapları",
    ),
    # düzey 3
    '0037': patch(
        'İşletme vadesine 45 gün kalan 300.000 ₺ nominal değerli bir müşteri senedini bankada iskonto ettirmiştir. Banka 9.000 ₺ iskonto tutarını kesmiş, kalanı işletmenin hesabına aktarmıştır. Buna göre yapılacak kayıtla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '102 Bankalar hesabı 300.000 ₺ borçlandırılır',
            'B': '122 Alacak Senetleri Reeskontu hesabı 9.000 ₺ alacaklandırılır',
            'C': '657 Reeskont Faiz Giderleri hesabı 9.000 ₺ borçlandırılır',
            'D': '780 Finansman Giderleri hesabı 9.000 ₺ borçlandırılır',
            'E': '121 Alacak Senetleri hesabı 291.000 ₺ alacaklandırılır',
        },
        'D',
        'Kayıt: 102 (borç) 291.000 + **780 (borç) 9.000** / 121 (alacak) 300.000. Senet nominal değerle portföyden çıkar; bankanın kestiği iskonto finansman gideridir. 657 dönem sonu reeskontu içindir.',
        'THP 102, 121, 780',
    ),
    # düzey 3
    '0038': patch(
        'İşletme, müşterisinin 45.000 ₺ tutarındaki senetsiz borcuna karşılık, müşterinin başka bir firmadan aldığı ve işletmeye ciro ettiği 45.000 ₺ nominal değerli bir bonoyu kabul etmiştir. Buna göre işletmenin kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '120 Alıcılar hesabı 45.000 ₺ borçlandırılır',
            'B': '121 Alacak Senetleri hesabı 45.000 ₺ borçlandırılır',
            'C': '121 Alacak Senetleri hesabı 45.000 ₺ alacaklandırılır',
            'D': '101 Alınan Çekler hesabı 45.000 ₺ borçlandırılır',
            'E': '321 Borç Senetleri hesabı 45.000 ₺ alacaklandırılır',
        },
        'B',
        'Ciro yoluyla alınan bono işletmenin portföyüne girer: **121 (borç) 45.000** / 120 (alacak) 45.000. Senedi düzenleyenin başkası olması kaydı değiştirmez; bono çek değildir.',
        'THP 121, 120',
    ),
    # düzey 3
    '0039': patch(
        'İşletme 50.000 ₺ + %20 KDV tutarındaki ticari malı kredili satmıştır. Müşteri borcunu vadesinden önce ödediği için KDV hariç tutar üzerinden %2 iskonto yapılmış, iskontoya ilişkin fatura düzenlenmiş ve kalan tutar banka hesabına tahsil edilmiştir. Buna göre tahsil kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '120 Alıcılar hesabı 58.800 ₺ alacaklandırılır',
            'B': '780 Finansman Giderleri hesabı 1.000 ₺ borçlandırılır',
            'C': '391 Hesaplanan KDV hesabı 200 ₺ alacaklandırılır',
            'D': '611 Satış İskontoları hesabı 1.200 ₺ borçlandırılır',
            'E': '611 Satış İskontoları hesabı 1.000 ₺ borçlandırılır',
        },
        'E',
        "İskonto 50.000 × %2 = 1.000 ₺, KDV'si 200 ₺. Kayıt: 102 (borç) 58.800 + **611 (borç) 1.000** + 391 (borç) 200 / 120 (alacak) 60.000. Alacağın tamamı kapanır; iskontoya düşen KDV geri alınır.",
        'THP 102, 611, 391, 120',
    ),
    # düzey 3
    '0040': patch(
        "Alacak senetleriyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Ciro edilen senet için 121 Alacak Senetleri alacaklandırılır.\n\nII. Bankada iskonto ettirilen senette kesilen iskonto finansman gideridir.\n\nIII. Protesto edilip icra takibine konan senet 128 Şüpheli Ticari Alacaklar'a aktarılabilir.",
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'I ve III',
            'D': 'I, II ve III',
            'E': 'Yalnız I',
        },
        'D',
        "Üç ifade de doğrudur. Ciro ve iskontoda senet portföyden çıkar (121 alacak); iskonto 780 Finansman Giderleri'ne yazılır; dava veya icra safhasındaki alacaklar VUK m. 323 uyarınca şüpheli alacaktır.",
        'THP 121, 780, 128; VUK m. 323',
    ),
    # düzey 2
    '0041': patch(
        "İşletme, elindeki 40.000 ₺'lik alacak senedini satıcısına olan borcuna karşılık ciro etmiştir. Bu işlemin kaydı aşağıdakilerden hangisidir?",
        {
            'A': '320 Satıcılar (borç) 40.000 / 100 Kasa (alacak) 40.000',
            'B': '121 Alacak Senetleri (borç) 40.000 / 100 Kasa (alacak) 40.000',
            'C': '320 Satıcılar (borç) 40.000 / 121 Alacak Senetleri (alacak) 40.000',
            'D': '321 Borç Senetleri (borç) 40.000 / 121 Alacak Senetleri (alacak) 40.000',
            'E': '121 Alacak Senetleri (borç) 40.000 / 320 Satıcılar (alacak) 40.000',
        },
        'C',
        'Ciro ile senetli alacak çıkar → **121 Alacak Senetleri (alacak)**; satıcıya olan borç azalır → **320 Satıcılar (borç)**. Kayıt: 320 Satıcılar (borç) 40.000 / 121 Alacak Senetleri (alacak) 40.000.',
        "1 Sıra No'lu MSUGT - 121 Alacak Senetleri (ciro)",
    ),
    # düzey 2
    '0042': patch(
        "'128 Şüpheli Ticari Alacaklar' hesabının niteliği ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Şüpheli alacaktan tahsil edilen tutarları izleyen bir gelir tablosu hesabıdır.',
            'B': 'Tahsili şüpheli hâle gelmiş ticari alacakların izlendiği bir aktif hesaptır.',
            'C': 'İşletmenin senetli borçlarını izleyen, alacak kalanı veren bir kaynak hesabıdır.',
            'D': 'Aktifi düzenleyici bir hesaptır; alacak kalanı verir ve şüpheli alacaklardan düşülür.',
            'E': 'Bir yıldan uzun vadeli senetli alacakları izleyen bir duran varlık hesabıdır.',
        },
        'B',
        "**128 Şüpheli Ticari Alacaklar**, tahsili şüpheli hâle gelen ticari alacakların izlendiği bir **aktif** hesaptır; borç kalanı verir. Karşılığı ise 129'da (aktifi düzenleyici) takip edilir.",
        "1 Sıra No'lu MSUGT - 128 Şüpheli Ticari Alacaklar",
    ),
    # düzey 2
    '0043': patch(
        "Vadesine bir yıldan uzun süre kalan senetli ticari alacaklar Tekdüzen Hesap Planı'nda hangi hesapta izlenir?",
        {
            'A': '221 Alacak Senetleri',
            'B': '136 Diğer Çeşitli Alacaklar',
            'C': '126 Verilen Depozito ve Teminatlar',
            'D': '321 Borç Senetleri',
            'E': '121 Alacak Senetleri',
        },
        'A',
        "Vadesi bir yıldan uzun senetli ticari alacaklar **221 Alacak Senetleri** (Uzun Vadeli/22 Ticari Alacaklar) hesabında izlenir. Bir yıl içindekiler ise 121'dedir.",
        "1 Sıra No'lu MSUGT - 22 Ticari Alacaklar (221)",
    ),
    # düzey 2
    '0044': patch(
        'İşletmenin bilançosunda senetli ticari alacakların net tutarı nasıl gösterilir?',
        {
            'A': '121 Alacak Senetleri + 122 Alacak Senetleri Reeskontu',
            'B': '120 Alıcılar − 121 Alacak Senetleri',
            'C': '121 Alacak Senetleri + 129 Şüpheli Ticari Alacaklar Karşılığı',
            'D': '122 Alacak Senetleri Reeskontu tek başına',
            'E': '121 Alacak Senetleri − 122 Alacak Senetleri Reeskontu (-)',
        },
        'E',
        'Senetli alacaklar bilançoda **121 Alacak Senetleri − 122 Alacak Senetleri Reeskontu (-)** biçiminde net (peşin/tasarruf değeriyle) gösterilir. 122 aktifi düzenleyici olduğundan (-) düşülür.',
        "1 Sıra No'lu MSUGT - 121/122",
    ),
    # düzey 2
    '0045': patch(
        'İşletme, kiraladığı işyeri için mal sahibine geri alınmak üzere 15.000 ₺ depozito ödemiştir. Bu işlemin kaydı aşağıdakilerden hangisidir?',
        {
            'A': '126 Verilen Depozito ve Teminatlar (borç) 15.000 / 100 Kasa (alacak) 15.000',
            'B': '770 Genel Yönetim Giderleri (borç) 15.000 / 100 Kasa (alacak) 15.000',
            'C': '320 Satıcılar (borç) 15.000 / 100 Kasa (alacak) 15.000',
            'D': '336 Diğer Çeşitli Borçlar (borç) 15.000 / 100 Kasa (alacak) 15.000',
            'E': '100 Kasa (borç) 15.000 / 126 Verilen Depozito ve Teminatlar (alacak) 15.000',
        },
        'A',
        'Geri alınmak üzere verilen depozito bir alacaktır: **126 Verilen Depozito ve Teminatlar (borç) 15.000 / 100 Kasa (alacak) 15.000**. Gider değildir; sözleşme sonunda geri alınır.',
        "1 Sıra No'lu MSUGT - 126 Verilen Depozito ve Teminatlar",
    ),
    # düzey 3
    '0046': patch(
        "VUK 323'teki diğer koşulların oluştuğu 180.000 ₺ tutarındaki ticari alacağın 120.000 ₺'lik kısmı tahsil kabiliyeti bulunan ipotekle güvence altındadır. Buna göre ayrılabilecek azami şüpheli alacak karşılığı kaç ₺'dir?",
        {
            'A': 'Karşılık ayrılamaz',
            'B': '120.000 ₺',
            'C': '300.000 ₺',
            'D': '60.000 ₺',
            'E': '180.000 ₺',
        },
        'D',
        'Teminatlı alacaklarda şüpheli alacak karşılığı yalnız teminatla karşılanmayan kısım için ayrılır. Açık kısım 180.000 − 120.000 = **60.000 ₺**dir.',
        '213 sayılı VUK md. 323',
    ),
    # düzey 2
    '0047': patch(
        "Şüpheli hâle gelen ve '128 Şüpheli Ticari Alacaklar'a alınan 24.000 ₺'lik alacağın tamamı için karşılık ayrılmasına ilişkin kayıt aşağıdakilerden hangisidir?",
        {
            'A': '129 Şüpheli Ticari Alacaklar Karşılığı (borç) 24.000 / 654 Karşılık Giderleri (alacak) 24.000',
            'B': '689 Diğer Olağandışı Gider (borç) 24.000 / 129 Şüpheli Ticari Alacaklar Karşılığı (alacak) 24.000',
            'C': '654 Karşılık Giderleri (borç) 24.000 / 129 Şüpheli Ticari Alacaklar Karşılığı (alacak) 24.000',
            'D': '654 Karşılık Giderleri (borç) 24.000 / 128 Şüpheli Ticari Alacaklar (alacak) 24.000',
            'E': '128 Şüpheli Ticari Alacaklar (borç) 24.000 / 129 Şüpheli Ticari Alacaklar Karşılığı (alacak) 24.000',
        },
        'C',
        "Karşılık, gider tahakkuk ettirilerek ayrılır: **654 Karşılık Giderleri (borç) 24.000 / 129 Şüpheli Ticari Alacaklar Karşılığı (-) (alacak) 24.000**. 129 aktifi düzenleyici olup 128'den düşülür.",
        "1 Sıra No'lu MSUGT - 654/129",
    ),
    # düzey 2
    '0048': patch(
        'Şüpheli hâle gelip tamamına 24.000 ₺ karşılık ayrılan bir alacağın, sonunda tahsilinin kesin olarak imkânsız (değersiz) hâle geldiği anlaşılmıştır. Daha önce ayrılan karşılığın kullanılarak alacağın kapatılmasına ilişkin kayıt aşağıdakilerden hangisidir?',
        {
            'A': '644 Konusu Kalmayan Karşılıklar (borç) 24.000 / 128 Şüpheli Ticari Alacaklar (alacak) 24.000',
            'B': '129 Şüpheli Ticari Alacaklar Karşılığı (borç) 24.000 / 128 Şüpheli Ticari Alacaklar (alacak) 24.000',
            'C': '128 Şüpheli Ticari Alacaklar (borç) 24.000 / 129 Şüpheli Ticari Alacaklar Karşılığı (alacak) 24.000',
            'D': '689 Diğer Olağandışı Gider (borç) 24.000 / 129 Şüpheli Ticari Alacaklar Karşılığı (alacak) 24.000',
            'E': '654 Karşılık Giderleri (borç) 24.000 / 128 Şüpheli Ticari Alacaklar (alacak) 24.000',
        },
        'B',
        'Karşılık daha önce ayrıldığından, alacak değersizleşince karşılık **kullanılır**: **129 Şüpheli Ticari Alacaklar Karşılığı (borç) 24.000 / 128 Şüpheli Ticari Alacaklar (alacak) 24.000**. Böylece hem şüpheli alacak hem karşılık kapanır; ek gider yazılmaz.',
        "1 Sıra No'lu MSUGT - 129/128 (karşılık kullanımı)",
    ),
    # düzey 2
    '0049': patch(
        'Şüpheli alacak, değersiz alacak ve vazgeçilen alacak kavramları ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Şüpheli alacak, tahsili imkânsız hâle gelmiş ve zarar yazılan alacaktır.',
            'B': 'Vazgeçilen alacak, işletmenin borçlusundan tamamını nakden tahsil ettiği alacaktır.',
            'C': 'Şüpheli alacak için karşılık ayrılabilir; değersiz alacak ise doğrudan zarar yazılır.',
            'D': 'Değersiz alacak, henüz dava veya icra safhasında olan ve karşılık ayrılabilen alacaktır.',
            'E': 'Şüpheli, değersiz ve vazgeçilen alacak kavramları aynı anlama gelir ve aynı kaydı gerektirir.',
        },
        'C',
        '**Şüpheli alacak** (tahsili belirsiz) için **karşılık** ayrılır; **değersiz alacak** (tahsili kesin imkânsız) ise doğrudan **zarar** yazılır. Vazgeçilen alacak ise alacaklının hukuken vazgeçtiği alacaktır.',
        'VUK md. 322-324 (değersiz/şüpheli/vazgeçilen alacak)',
    ),
    # düzey 3
    '0050': patch(
        'İşletmenin dava/icra safhasına gelmeksizin sadece bir kez sözlü olarak istediği, ancak henüz protesto edilmemiş veya yazıyla birden fazla istenmemiş bir alacağı için şüpheli alacak karşılığı ayırması aşağıdakilerden hangisi bakımından uygun değildir?',
        {
            'A': "Vergi Usul Kanunu'ndaki şüpheli alacak koşullarının henüz oluşmamış olması",
            'B': 'Alacağın satış anında bedelinin peşin olarak tahsil edilmiş olması nedeniyle',
            'C': 'Alacağın esas faaliyetle ilgisi olmayan, ticari nitelik taşımayan bir alacak olması',
            'D': 'Alacağın müşteriden değil, işletmenin ortaklarından olan bir alacak olması',
            'E': 'Alacağın bir dönen varlık değil, uzun vadeli bir duran varlık olması nedeniyle',
        },
        'A',
        "VUK'a göre şüpheli alacak için ya **dava/icra safhası** ya da **protesto/yazıyla birden fazla isteme** koşulu aranır. Sadece bir kez sözlü isteme bu koşulları karşılamaz; bu nedenle karşılık ayrılması uygun değildir.",
        'VUK md. 323 (şüpheli alacak koşulları)',
    ),
    # düzey 2
    '0051': patch(
        'İşletmenin elindeki bir alacak senedi vadesinde ödenmemiş ve protesto edilmiştir. Bu durum aşağıdakilerden hangisi bakımından önem taşır?',
        {
            'A': 'Senedin protestoyla birlikte 101 Alınan Çekler benzeri bir hazır değere dönüşerek işletmenin kasa ve banka mevcudunu artırması',
            'B': 'Senedin protesto edildiği anda peşin satılmış sayılıp doğrudan gelir olarak sonuç hesaplarına aktarılması',
            'C': "Vadeli satıştan hesaplanan KDV'nin, senedin ödenmemesi nedeniyle işletmeye geri iade edilmesi",
            'D': 'Alacağın tahsilinin şüpheli hâle gelmesine ve (koşullar oluşursa) şüpheli alacak sürecine geçilmesine zemin hazırlaması',
            'E': 'Protesto ile senedin nominal değerinin vade farkı kadar artması ve bilançoda yükseltilmesi',
        },
        'D',
        'Protesto, senedin vadesinde ödenmediğinin resmen belgelenmesidir; alacağın tahsilini **şüpheli** hâle getirir ve VUK koşulları oluşursa 128 Şüpheli Ticari Alacaklar sürecine geçilir (protestolu senetler ayrı izlenebilir).',
        "VUK md. 323; 1 Sıra No'lu MSUGT - protestolu senetler",
    ),
    # düzey 2
    '0052': patch(
        "İşletmenin elindeki 60.000 ₺'lik alacak senedinin, borçlunun talebiyle vadesi uzatılarak yeni bir senetle değiştirilmesi işleminde (faizsiz varsayımıyla) aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Eski senet vadesi uzatılırken değersizleşmiş sayılır ve doğrudan 689 hesabına gider yazılır.',
            'B': 'Vade uzatıldığı için işlem 100 Kasa hesabını 60.000 ₺ borçlandırıp nakit girişi olarak kaydedilir.',
            'C': 'Senet yenileme bir borç işlemi olduğundan 320 Satıcılar hesabını borçlandıran bir kayıt gerektirir.',
            'D': 'Senet yenilendiği için işlem sonucu 600 Yurt İçi Satışlar hesabı yeni senet tutarı 60.000 ₺ ile yeniden alacaklandırılır.',
            'E': 'Eski senet (121) alacaklandırılıp yeni senet (121) borçlandırılarak senet yenilenir; alacak tutarı değişmez.',
        },
        'E',
        'Senet yenilemede (faizsiz) eski senet çıkar, yeni senet girer: **121 (yeni) borç / 121 (eski) alacak**; alacağın senetli niteliği ve tutarı korunur. (Faiz eklenirse ayrıca faiz geliri kaydedilir.)',
        "1 Sıra No'lu MSUGT - 121 Alacak Senetleri (yenileme)",
    ),
    # düzey 2
    '0053': patch(
        'İşletmenin, esas faaliyeti dışındaki bir işlemden doğan ve personelinden olan (ticari olmayan) senetsiz alacağı hangi hesapta izlenir?',
        {
            'A': '320 Satıcılar',
            'B': '135 Personelden Alacaklar',
            'C': '120 Alıcılar',
            'D': '128 Şüpheli Ticari Alacaklar',
            'E': '121 Alacak Senetleri',
        },
        'B',
        'Personelden olan ticari olmayan alacaklar **135 Personelden Alacaklar** (13 Diğer Alacaklar grubu) hesabında izlenir; 120 Alıcılar esas faaliyetten (satıştan) doğan ticari alacaklar içindir.',
        "1 Sıra No'lu MSUGT - 135 Personelden Alacaklar",
    ),
    # düzey 2
    '0054': patch(
        'Vadeli (kredili) bir mal satışında satış bedeline eklenen vade farkının, satışın finansman unsuru olarak ayrıştırılıp değerlendirilmesi öncelikle hangi kavramla ilişkilendirilir?',
        {
            'A': 'Sosyal Sorumluluk',
            'B': 'Süreklilik',
            'C': 'Kişilik',
            'D': 'Parayla Ölçülme',
            'E': 'Özün Önceliği',
        },
        'E',
        'Vadeli satıştaki vade farkı biçimen satış bedeline dâhil görünse de özü itibarıyla bir **finansman** unsurudur; bunun ayrıştırılıp buna göre değerlendirilmesi **Özün Önceliği** kavramıyla ilişkilidir.',
        "1 Sıra No'lu MSUGT - Özün Önceliği; TMS/TFRS (vade farkı)",
    ),
    # düzey 2
    '0055': patch(
        "İşletme, alıcısından olan 12.000 ₺'lik senetsiz alacağını, alıcının işletmeye keşide ettiği bir çekle tahsil etmiştir. Bu işlemin kaydı aşağıdakilerden hangisidir?",
        {
            'A': '103 Verilen Çekler ve Ödeme Emirleri (borç) 12.000 / 120 Alıcılar (alacak) 12.000',
            'B': '100 Kasa (borç) 12.000 / 120 Alıcılar (alacak) 12.000',
            'C': '120 Alıcılar (borç) 12.000 / 101 Alınan Çekler (alacak) 12.000',
            'D': '101 Alınan Çekler (borç) 12.000 / 120 Alıcılar (alacak) 12.000',
            'E': '121 Alacak Senetleri (borç) 12.000 / 120 Alıcılar (alacak) 12.000',
        },
        'D',
        "Alınan çek 101 Alınan Çekler'e (hazır değer) girer, senetsiz alacak kapanır: **101 Alınan Çekler (borç) 12.000 / 120 Alıcılar (alacak) 12.000**. Çek senet değildir; 121 kullanılmaz.",
        "1 Sıra No'lu MSUGT - 101 Alınan Çekler / 120 Alıcılar",
    ),
    # düzey 3
    '0056': patch(
        "Bir işletmenin dönem sonu itibarıyla 120 Alıcılar 400.000 ₺, 121 Alacak Senetleri 300.000 ₺, 122 Alacak Senetleri Reeskontu 30.000 ₺, 128 Şüpheli Ticari Alacaklar 50.000 ₺ ve 129 Şüpheli Ticari Alacaklar Karşılığı 50.000 ₺'dir. Bu verilere göre kısa vadeli ticari alacakların bilançodaki net tutarı kaç ₺'dir?",
        {
            'A': '700.000',
            'B': '720.000',
            'C': '670.000',
            'D': '780.000',
            'E': '630.000',
        },
        'C',
        'Net ticari alacaklar = 120 (400.000) + 121 (300.000) − 122 (30.000) + 128 (50.000) − 129 (50.000) = 400.000 + 300.000 − 30.000 + 0 = **670.000 ₺**. Düzenleyici hesaplar (122, 129) düşülür.',
        "1 Sıra No'lu MSUGT - Ticari alacakların net gösterimi",
    ),
    # düzey 3
    '0057': patch(
        "İşletme vadesine 90 gün kalan 200.000 ₺ nominal değerli bir müşteri senedini bankada iskonto ettirmiştir. Banka yıllık %40 oranı ve 360 gün esasıyla dış iskonto uygulamaktadır (başka kesinti yoktur). Buna göre işletmenin hesabına geçecek tutar kaç ₺'dir?",
        {
            'A': '180.000 ₺',
            'B': '160.000 ₺',
            'C': '20.000 ₺',
            'D': '200.000 ₺',
            'E': '181.818 ₺',
        },
        'A',
        'Dış iskonto nominal değer üzerinden hesaplanır: 200.000 × 0,40 × 90/360 = 20.000 ₺. Hesaba geçen tutar 200.000 − 20.000 = **180.000 ₺**. 181.818 ₺ iç iskonto sonucudur; bankalar senet iskontosunda dış iskonto uygular.',
        'Dış iskonto; THP 102, 121, 780',
    ),
    # düzey 3
    '0058': patch(
        'Vadesi gelen 60.000 ₺ nominal değerli müşteri senedi, borçlunun talebiyle 6.000 ₺ vade farkı ve bu tutar üzerinden %20 KDV eklenerek düzenlenen yeni bir senetle değiştirilmiştir. Buna göre yapılacak kayıtla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '121 Alacak Senetleri hesabı 60.000 ₺ borçlandırılır',
            'B': '642 Faiz Gelirleri hesabı 6.000 ₺ alacaklandırılır',
            'C': '649 Diğer Olağan Gelir ve Kârlar hesabı 7.200 ₺ alacaklandırılır',
            'D': '121 Alacak Senetleri hesabı 6.000 ₺ alacaklandırılır',
            'E': '391 Hesaplanan KDV hesabı 1.200 ₺ borçlandırılır',
        },
        'B',
        'Yeni senet 60.000 + 6.000 + 1.200 = 67.200 ₺. Kayıt: 121 (borç) 67.200 / 121 (alacak) 60.000 + **642 (alacak) 6.000** + 391 (alacak) 1.200. Vade farkı finansman gelirdir ve KDV matrahına girer.',
        '3065 sayılı KDVK m. 24; THP 121, 642, 391',
    ),
    # düzey 3
    '0059': patch(
        'Vadesinde ödenmeyen 30.000 ₺ nominal değerli müşteri senedi protesto edilmiş ve borçlu hakkında icra takibi başlatılmıştır. Dönem sonunda alacağın tamamı için karşılık ayrılmasına karar verilmiştir. Buna göre yapılacak kayıtlarda aşağıdakilerden hangisi yer almaz?',
        {
            'A': '121 Alacak Senetleri hesabı 30.000 ₺ alacaklandırılır',
            'B': '654 Karşılık Giderleri hesabı 30.000 ₺ borçlandırılır',
            'C': '128 Şüpheli Ticari Alacaklar hesabı 30.000 ₺ borçlandırılır',
            'D': '129 Şüpheli Ticari Alacaklar Karşılığı hesabı 30.000 ₺ alacaklandırılır',
            'E': '120 Alıcılar hesabı 30.000 ₺ alacaklandırılır',
        },
        'E',
        'İcra takibine konan senetli alacak şüpheli alacağa aktarılır: 128 (borç) / **121 (alacak)** 30.000; karşılık: 654 (borç) / 129 (alacak) 30.000. Alacak senede bağlı olduğu için 120 kullanılmaz.',
        'VUK m. 323; THP 121, 128, 129, 654',
    ),
    # düzey 2
    '0060': patch(
        'İşletme, müşterisinden aldığı 25.000 ₺ tutarındaki çeki tahsil için bankaya vermiş; banka çeki tahsil ederek tutarı işletmenin hesabına aktarmıştır. Buna göre tahsil kaydı aşağıdakilerden hangisidir?',
        {
            'A': '101 (borç) 25.000 / 102 (alacak) 25.000',
            'B': '102 (borç) 25.000 / 103 (alacak) 25.000',
            'C': '102 (borç) 25.000 / 121 (alacak) 25.000',
            'D': '102 (borç) 25.000 / 120 (alacak) 25.000',
            'E': '102 (borç) 25.000 / 101 (alacak) 25.000',
        },
        'E',
        "Müşteri çeki alındığında 101 Alınan Çekler'e kaydedilmiştir; tahsilde banka hesabı artar, 101 kapatılır: **102 (borç) / 101 (alacak)**. 103 işletmenin kendi keşide ettiği çekler içindir.",
        'THP 101, 102',
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
    print(f"1 paket / {len(PATCHES)} soru ('Ticari Alacaklar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
