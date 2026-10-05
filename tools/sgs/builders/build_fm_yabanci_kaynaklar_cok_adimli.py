#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yabanci Kaynaklar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

FM cok adimli tur. 47 soru korundu; 6 TMS 1/19/37/finansal yukumluluk sorusu ve 7 'hangi hesapta izlenir' ezberi cikarildi. Yerine gercek sinav kalibinda 13 soru: ayrintili ucret tahakkuku (SGK isci/isveren paylari, 360/361 ayrimi), dosya masrafli kredi kullanimi, tahakkuklu kredi geri odemesi, kredi faizi tahakkuku, satici borcunun kendi senedi ve ciroyla kapatilmasi, karsiligi yetersiz kidem tazminati odemesi, uzun vadeli alinan depozito (426), kisa vadeli yabanci kaynak toplami, siparis iptali, olumsuz/oncullu siniflandirma. Kor ogrenci %21.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Tekduzen Hesap Plani 3-4 Yabanci Kaynaklar, 335, 360, 361, 381, 472, 780 · 1 Sira No'lu MSUGT
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/finansal_muhasebe/yabanci_kaynaklar.json"
STYLE_REF = 'SGS Finansal Muhasebe (çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "finmuh-yk-gen-"


def patch(stem, options, answer, solution, ref='Tekduzen Hesap Plani 3-4 Yabanci Kaynaklar'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        'Aşağıdakilerden hangisi bir yabancı kaynak (borç) değildir?',
        {
            'A': '321 Borç Senetleri',
            'B': '300 Banka Kredileri',
            'C': '320 Satıcılar',
            'D': '500 Sermaye',
            'E': '360 Ödenecek Vergi ve Fonlar',
        },
        'D',
        '**500 Sermaye** bir **özkaynak** hesabıdır (işletme sahiplerinin hakkı), yabancı kaynak değildir. Diğerleri üçüncü kişilere olan borçlardır (yabancı kaynak).',
        "1 Sıra No'lu MSUGT - 3/4 vs 5 grupları",
    ),
    # düzey 2
    '0002': patch(
        "İşletmenin sorumlu sıfatıyla ödeyeceği KDV, gelir/kurumlar vergisi stopajı, damga vergisi gibi vergi borçları Tekdüzen Hesap Planı'nda hangi hesapta izlenir?",
        {
            'A': '361 Ödenecek Sosyal Güvenlik Kesintileri',
            'B': '320 Satıcılar',
            'C': '360 Ödenecek Vergi ve Fonlar',
            'D': '370 Dönem Kârı Vergi ve Diğer Yasal Yükümlülük Karşılıkları',
            'E': '193 Peşin Ödenen Vergiler ve Fonlar',
        },
        'C',
        'Ödenecek KDV, vergi stopajları, damga vergisi gibi vergi ve fon borçları **360 Ödenecek Vergi ve Fonlar** hesabında izlenir.',
        "1 Sıra No'lu MSUGT - 360",
    ),
    # düzey 2
    '0003': patch(
        "İşletme 1 Mart'ta, 18 ay sonra teslim edeceği özel üretim makine için müşteriden avans almış ve tutarı 440 Alınan Sipariş Avansları hesabına kaydetmiştir. 31 Aralık'ta teslimata dokuz ay kalmıştır. Tekdüzen Hesap Planı'na göre hangi aktarma yapılır?",
        {
            'A': '102 Bankalar borçlandırılır, 340 Alınan Sipariş Avansları alacaklandırılır.',
            'B': '340 Alınan Sipariş Avansları borçlandırılır, 440 Alınan Sipariş Avansları alacaklandırılır.',
            'C': 'Avansın ilk kaydı uzun vadeli yapıldığı için vadesi kısalsa da hesaplar arası aktarma yapılmaz.',
            'D': '440 Alınan Sipariş Avansları borçlandırılır, 600 Yurt İçi Satışlar alacaklandırılır.',
            'E': '440 Alınan Sipariş Avansları borçlandırılır, 340 Alınan Sipariş Avansları alacaklandırılır.',
        },
        'E',
        'Teslimata kalan süre bir yılın altına indiği için uzun vadeli **440** hesabı borçlandırılarak kapatılır ve kısa vadeli **340 Alınan Sipariş Avansları** hesabı alacaklandırılır. Mal teslim edilmediğinden henüz satış geliri oluşmaz.',
        "1 Sıra No'lu MSUGT - 340/440",
    ),
    # düzey 2
    '0004': patch(
        'Aşağıdakilerden hangisi kısa vadeli yabancı kaynaklar (3) grubunda yer alır?',
        {
            'A': '320 Satıcılar',
            'B': '400 Banka Kredileri',
            'C': '405 Çıkarılmış Tahviller',
            'D': '420 Satıcılar',
            'E': '472 Kıdem Tazminatı Karşılıkları',
        },
        'A',
        '**320 Satıcılar**, kısa vadeli (3) yabancı kaynaklar grubundadır. Diğerleri (400, 405, 420, 472) uzun vadeli (4) yabancı kaynaklardır.',
        "1 Sıra No'lu MSUGT - 3 / 4 grupları",
    ),
    # düzey 2
    '0005': patch(
        "İşletme 1 Ekim'de yıllık %24 faizli 400.000 ₺ banka kredisi kullanmıştır. Faiz vade sonunda ödenecektir. 31 Aralık'ta yapılacak üç aylık faiz tahakkuku kaydı hangisidir?",
        {
            'A': '780 Finansman Giderleri 96.000 borç; 381 Gider Tahakkukları 96.000 alacak',
            'B': '381 Gider Tahakkukları 24.000 borç; 780 Finansman Giderleri 24.000 alacak',
            'C': '780 Finansman Giderleri 24.000 borç; 381 Gider Tahakkukları 24.000 alacak',
            'D': '180 Gelecek Aylara Ait Giderler 24.000 borç; 102 Bankalar 24.000 alacak',
            'E': '300 Banka Kredileri 24.000 borç; 642 Faiz Gelirleri 24.000 alacak',
        },
        'C',
        'Üç aylık faiz 400.000 × %24 × 3/12 = **24.000 ₺**dir. Faiz dönemin gideri olduğundan **780 Finansman Giderleri** borç; henüz ödenmediği için **381 Gider Tahakkukları** alacak çalışır.',
        "1 Sıra No'lu MSUGT - 780/381; dönemsellik",
    ),
    # düzey 2
    '0006': patch(
        'Nominal değeri 150.000 ₺ olan borç senedinin dönem sonundaki tasarruf değeri 138.000 ₺ olarak hesaplanmıştır. Borç senedi reeskontu kaydı hangisidir?',
        {
            'A': '322 Borç Senetleri Reeskontu 12.000 borç; 647 Reeskont Faiz Gelirleri 12.000 alacak',
            'B': '321 Borç Senetleri 12.000 borç; 647 Reeskont Faiz Gelirleri 12.000 alacak',
            'C': '322 Borç Senetleri Reeskontu 138.000 borç; 647 Reeskont Faiz Gelirleri 138.000 alacak',
            'D': '657 Reeskont Faiz Giderleri 12.000 borç; 322 Borç Senetleri Reeskontu 12.000 alacak',
            'E': '647 Reeskont Faiz Gelirleri 12.000 borç; 322 Borç Senetleri Reeskontu 12.000 alacak',
        },
        'A',
        'Reeskont 150.000 − 138.000 = **12.000 ₺**dir. Borcu bugünkü değerine indiren pasifi düzenleyici **322 Borç Senetleri Reeskontu** borç; işletme lehine oluşan **647 Reeskont Faiz Gelirleri** alacak kaydedilir.',
        "VUK m. 285; 1 Sıra No'lu MSUGT - 322/647",
    ),
    # düzey 3
    '0007': patch(
        'Dönem sonunda 391 Hesaplanan KDV hesabı 80.000 ₺, 191 İndirilecek KDV hesabı 50.000 ₺ ve önceki dönemden devreden 190 Devreden KDV hesabı 10.000 ₺ borç bakiyesi vermektedir. Mahsup kaydı hangisidir?',
        {
            'A': '391 Hesaplanan KDV 80.000 borç; 191 İndirilecek KDV 50.000, 190 Devreden KDV 10.000 ve 360 Ödenecek Vergi ve Fonlar 20.000 alacak',
            'B': '360 Ödenecek Vergi ve Fonlar 20.000 borç; 391 Hesaplanan KDV 80.000 ve 191 İndirilecek KDV 60.000 alacak',
            'C': '391 Hesaplanan KDV 80.000 borç; 190 Devreden KDV 30.000 ve 360 Ödenecek Vergi ve Fonlar 50.000 alacak',
            'D': '191 İndirilecek KDV 50.000 ve 190 Devreden KDV 10.000 borç; 391 Hesaplanan KDV 60.000 alacak',
            'E': '391 Hesaplanan KDV 80.000 borç; 191 İndirilecek KDV 50.000 ve 360 Ödenecek Vergi ve Fonlar 30.000 alacak',
        },
        'A',
        "Hesaplanan KDV'den cari dönemin indirilecek KDV'si ve önceki dönemden devreden KDV düşülür: 80.000 − 50.000 − 10.000 = **20.000 ₺** ödenecek KDV doğar. 391 borçlandırılarak; 191, 190 ve 360 alacaklandırılarak kapatılır.",
        "1 Sıra No'lu MSUGT - 190/191/360/391",
    ),
    # düzey 2
    '0008': patch(
        "İşletmenin vergi öncesi dönem kârı 500.000 ₺, soruda uygulanacağı belirtilen vergi oranı %25 ve yıl içinde peşin ödediği vergi 70.000 ₺'dir. Dönem sonu kayıtlarından sonra finansal durum tablosunda net vergi karşılığı kaç ₺ görünür?",
        {
            'A': '70.000 ₺; peşin ödenen vergiler yükümlülük sayılır.',
            'B': '0 ₺; peşin vergi ödendiğinde dönem kârı için karşılık ayrılmaz.',
            'C': '125.000 ₺; peşin ödenen vergiler karşılıktan indirilmez.',
            'D': '195.000 ₺; vergi karşılığı ile peşin ödeme toplanır.',
            'E': '55.000 ₺; 370 hesabındaki 125.000 ₺ karşılık, 371 hesabındaki 70.000 ₺ ile netleştirilir.',
        },
        'E',
        "Vergi karşılığı 500.000 × %25 = **125.000 ₺**dir ve 370 hesabında izlenir. Peşin ödenen 70.000 ₺, 371 hesabına aktarılarak 370'i düzenler. Finansal durum tablosunda net yükümlülük 125.000 − 70.000 = **55.000 ₺**dir.",
        "1 Sıra No'lu MSUGT - 370/371/691",
    ),
    # düzey 2
    '0009': patch(
        'İşletmenin daha önce ihraç ettiği 300.000 ₺ nominal değerli hisse senedine dönüştürülebilir tahvillerin tamamı, sözleşme koşullarına uygun olarak sermaye payına dönüştürülmüştür. Basitleştirilmiş Tekdüzen Hesap Planı kaydı hangisidir?',
        {
            'A': '500 Sermaye 300.000 borç; 405 Çıkarılmış Tahviller 300.000 alacak',
            'B': '405 Çıkarılmış Tahviller 300.000 borç; 500 Sermaye 300.000 alacak',
            'C': '102 Bankalar 300.000 borç; 405 Çıkarılmış Tahviller 300.000 alacak',
            'D': '111 Özel Kesim Tahvil, Senet ve Bonoları 300.000 borç; 500 Sermaye 300.000 alacak',
            'E': '405 Çıkarılmış Tahviller 300.000 borç; 102 Bankalar 300.000 alacak',
        },
        'B',
        'Dönüşümle tahvil borcu sona erdiğinden **405 Çıkarılmış Tahviller borçlandırılır**. Karşılığında işletmenin sermayesi arttığı için **500 Sermaye alacaklandırılır**. İşletmeye yeni bir nakit girişi olmaz.',
        "1 Sıra No'lu MSUGT - 405/500",
    ),
    # düzey 2
    '0010': patch(
        "İşletmenin ticari borç, ortak, personel ve vergi/SGK kapsamına girmeyen diğer çeşitli kısa vadeli borçları Tekdüzen Hesap Planı'nda hangi hesapta izlenir?",
        {
            'A': '320 Satıcılar',
            'B': '335 Personele Borçlar',
            'C': '360 Ödenecek Vergi ve Fonlar',
            'D': '336 Diğer Çeşitli Borçlar',
            'E': '331 Ortaklara Borçlar',
        },
        'D',
        'Diğer hesapların kapsamına girmeyen çeşitli kısa vadeli borçlar **336 Diğer Çeşitli Borçlar** hesabında izlenir.',
        "1 Sıra No'lu MSUGT - 336",
    ),
    # düzey 3
    '0011': patch(
        'Aşağıdaki hesaplardan hangileri uzun vadeli yabancı kaynaklar (4) grubunda yer alır?\n\nI. 320 Satıcılar\n\nII. 400 Banka Kredileri\n\nIII. 405 Çıkarılmış Tahviller',
        {
            'A': 'Yalnız II',
            'B': 'I, II ve III',
            'C': 'I ve II',
            'D': 'Yalnız I',
            'E': 'II ve III',
        },
        'E',
        '**II (400 Banka Kredileri)** ve **III (405 Çıkarılmış Tahviller)** uzun vadeli (4) yabancı kaynaklardır. **I (320 Satıcılar)** ise kısa vadeli (3) yabancı kaynaktır. Doğru cevap **II ve III**.',
        "1 Sıra No'lu MSUGT - 3 / 4 grupları",
    ),
    # düzey 2
    '0012': patch(
        'Nominal değeri 200.000 ₺ olan borç senedi önceki dönem sonunda 10.000 ₺ reeskonta tabi tutulmuştur. Yeni dönem başında reeskont ters çevrilmiş, senet vadesinde bankadan ödenmiştir. Vade ödeme kaydıyla ilgili hangisi doğrudur?',
        {
            'A': '321 Borç Senetleri tasarruf değeri olan 190.000 ₺ kadar borçlandırılır.',
            'B': '322 Borç Senetleri Reeskontu 10.000 borçlandırılır; 102 Bankalar 10.000 alacaklandırılır.',
            'C': '321 Borç Senetleri 200.000 borçlandırılır; 102 Bankalar 200.000 alacaklandırılır.',
            'D': '647 Reeskont Faiz Gelirleri 10.000 borçlandırılır; 321 Borç Senetleri 10.000 alacaklandırılır.',
            'E': '657 Reeskont Faiz Giderleri 200.000 borçlandırılır; 102 Bankalar 200.000 alacaklandırılır.',
        },
        'C',
        'Reeskont yeni dönem başında 657/322 ters kaydıyla zaten kapatılmıştır. Vade tarihinde nominal borç ödenir: **321 Borç Senetleri 200.000 ₺ borç**, **102 Bankalar 200.000 ₺ alacak** kaydedilir.',
        "1 Sıra No'lu MSUGT - 321/322/657/102",
    ),
    # düzey 3
    '0013': patch(
        'Aşağıdaki işlemlerden hangileri borçlanma nedeniyle finansman maliyeti doğurur?\n\nI. Yabancı para banka kredisinde işletme aleyhine kur farkı oluşması\n\nII. Banka kredisine dönem sonu faiz tahakkuk etmesi\n\nIII. Tahvillerin nominal değerinin altında ihraç edilmesi\n\nIV. Hisse senetlerinin nominal değerinin üzerinde ihraç edilmesi\n\nV. Satıcıdan erken ödeme iskontosu kazanılması',
        {
            'A': 'I, II ve III',
            'B': 'II, III ve IV',
            'C': 'Yalnız I ve II',
            'D': 'I, II, III, IV ve V',
            'E': 'I, III, IV ve V',
        },
        'A',
        'Yabancı para borçta olumsuz kur farkı, kredi faizi ve tahvil ihraç iskontosunun dönemlere düşen kısmı finansman maliyetidir. Hisse senedi ihraç primi özkaynak unsurudur; satıcıdan kazanılan erken ödeme iskontosu ise işletme lehine bir indirimdir.',
        "1 Sıra No'lu MSUGT - 408/656/780; TFRS 9 etkin faiz",
    ),
    # düzey 3
    '0014': patch(
        'İşletme 100.000 ₺ + 20.000 ₺ KDV tutarındaki malı müşteriye teslim etmiştir. Müşteriden daha önce alınan 30.000 ₺ avans mahsup edilmiş, kalan 90.000 ₺ banka yoluyla tahsil edilmiştir. Satış kaydı hangisidir?',
        {
            'A': '340 Alınan Sipariş Avansları 30.000 borç; 600 Yurt İçi Satışlar 30.000 alacak',
            'B': '340 Alınan Sipariş Avansları 30.000 ve 102 Bankalar 90.000 borç; 600 Yurt İçi Satışlar 100.000 ve 391 Hesaplanan KDV 20.000 alacak',
            'C': '102 Bankalar 90.000 ve 120 Alıcılar 30.000 borç; 600 Yurt İçi Satışlar 120.000 alacak',
            'D': '340 Alınan Sipariş Avansları 30.000 ve 102 Bankalar 90.000 borç; 600 Yurt İçi Satışlar 120.000 alacak',
            'E': '102 Bankalar 120.000 borç; 600 Yurt İçi Satışlar 100.000 ve 391 Hesaplanan KDV 20.000 alacak',
        },
        'B',
        'Teslimle 30.000 ₺ avans yükümlülüğü **340 hesabı borçlandırılarak** kapatılır ve kalan 90.000 ₺ bankaya girer. Satış bedeli **600 hesaba 100.000 ₺**, hesaplanan KDV ise **391 hesaba 20.000 ₺ alacak** kaydedilir.',
        "1 Sıra No'lu MSUGT - 340/102/600/391",
    ),
    # düzey 2
    '0015': patch(
        "İşletme, daha önce aldığı 15.000 ₺'lik depozitoyu (326 Alınan Depozito ve Teminatlar) karşı tarafa banka aracılığıyla iade etmiştir. Bu işlemin kaydı aşağıdakilerden hangisidir?",
        {
            'A': '770 Genel Yönetim Giderleri (borç) 15.000 / 102 Bankalar (alacak) 15.000',
            'B': '326 Alınan Depozito ve Teminatlar (borç) 15.000 / 102 Bankalar (alacak) 15.000',
            'C': '102 Bankalar (borç) 15.000 / 326 Alınan Depozito ve Teminatlar (alacak) 15.000',
            'D': '126 Verilen Depozito ve Teminatlar (borç) 15.000 / 102 Bankalar (alacak) 15.000',
            'E': '326 Alınan Depozito ve Teminatlar (borç) 15.000 / 600 Yurt İçi Satışlar (alacak) 15.000',
        },
        'B',
        'Alınan depozito iade edildiğinde borç azalır → **326 Alınan Depozito ve Teminatlar (borç) 15.000**; banka çıkışı → **102 Bankalar (alacak) 15.000**.',
        "1 Sıra No'lu MSUGT - 326 / 102",
    ),
    # düzey 3
    '0016': patch(
        "Bir personelin brüt ücreti 50.000 ₺, ücretinden kesilen SGK işçi payı 7.500 ₺, gelir ve damga vergisi toplamı 5.000 ₺, işletmenin SGK işveren payı 10.000 ₺'dir. Ücret tahakkukunda doğru hesap tutarları hangisidir?",
        {
            'A': '335 Personele Borçlar 27.500; 360 Ödenecek Vergi ve Fonlar 5.000; 361 Ödenecek Sosyal Güvenlik Kesintileri 27.500',
            'B': '335 Personele Borçlar 37.500; 360 Ödenecek Vergi ve Fonlar 12.500; 361 Ödenecek Sosyal Güvenlik Kesintileri 10.000',
            'C': '335 Personele Borçlar 42.500; 360 Ödenecek Vergi ve Fonlar 7.500; 361 Ödenecek Sosyal Güvenlik Kesintileri 10.000',
            'D': '335 Personele Borçlar 37.500; 360 Ödenecek Vergi ve Fonlar 5.000; 361 Ödenecek Sosyal Güvenlik Kesintileri 17.500',
            'E': '335 Personele Borçlar 50.000; 360 Ödenecek Vergi ve Fonlar 5.000; 361 Ödenecek Sosyal Güvenlik Kesintileri 7.500',
        },
        'D',
        'Net ücret 50.000 − 7.500 − 5.000 = **37.500 ₺**dir. 360 hesabında vergi kesintileri **5.000 ₺**, 361 hesabında ise işçi ve işveren SGK paylarının toplamı 7.500 + 10.000 = **17.500 ₺** izlenir. İşveren payıyla toplam personel maliyeti 60.000 ₺ olur.',
        "1 Sıra No'lu MSUGT - 335/360/361",
    ),
    # düzey 3
    '0017': patch(
        'İşletme bankadan bir yıl vadeli 500.000 ₺ kredi kullanmıştır. Banka 2.000 ₺ dosya masrafını keserek kalan tutarı işletmenin vadesiz hesabına aktarmıştır. Buna göre kredi kullanım kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '300 Banka Kredileri hesabı 498.000 ₺ alacaklandırılır',
            'B': '102 Bankalar hesabı 500.000 ₺ borçlandırılır',
            'C': '300 Banka Kredileri hesabı 500.000 ₺ alacaklandırılır',
            'D': '780 Finansman Giderleri hesabı 2.000 ₺ alacaklandırılır',
            'E': '400 Banka Kredileri hesabı 500.000 ₺ alacaklandırılır',
        },
        'C',
        "Kayıt: 102 (borç) 498.000 + 780 (borç) 2.000 / **300 (alacak) 500.000**. Geri ödenecek anapara 500.000 ₺'dir; masraf finansman gideridir. Vade bir yıl olduğu için kısa vadeli 300 kullanılır.",
        'THP 300, 102, 780',
    ),
    # düzey 3
    '0018': patch(
        "İşletme satıcısına olan 30.000 ₺ senetsiz borcunu kapatmak için 12.000 ₺'lik bir bono düzenleyip vermiş, kalan 18.000 ₺ için de portföyündeki bir müşteri senedini ciro etmiştir. Buna göre yapılacak kayıt aşağıdakilerden hangisidir?",
        {
            'A': '320 (borç) 30.000 / 121 (alacak) 12.000 + 321 (alacak) 18.000',
            'B': '320 (borç) 30.000 / 103 (alacak) 12.000 + 121 (alacak) 18.000',
            'C': '320 (borç) 30.000 / 321 (alacak) 30.000',
            'D': '320 (borç) 30.000 / 321 (alacak) 12.000 + 121 (alacak) 18.000',
            'E': '321 (borç) 12.000 + 121 (borç) 18.000 / 320 (alacak) 30.000',
        },
        'D',
        "Senetsiz borç (320) kapanır; işletmenin düzenlediği bono 321 Borç Senetleri'ne, ciro edilen müşteri senedi 121'in alacağına yazılır. 103 işletmenin kendi çekleri içindir.",
        'THP 320, 321, 121',
    ),
    # düzey 2
    '0019': patch(
        'Bir işletme müşterilerinden sipariş avansı almaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Avans 340'ın alacağına yazılır",
            'B': "Teslim bir yıldan sonra olacaksa avans 440'ta izlenir",
            'C': 'Teslimde 340 borçlandırılarak kapatılır',
            'D': 'Avans, mal teslim edilene kadar bir yükümlülüktür',
            'E': 'Alınan sipariş avansı alındığı anda hasılat olarak kaydedilir',
        },
        'E',
        "Sipariş avansı mal teslim edilene kadar bir **yükümlülüktür**; hasılat teslimde doğar. Avans 340'ta (teslim bir yıldan sonra ise 440'ta) izlenir ve teslimde borçlandırılarak kapatılır.",
        'THP 340, 440, 600',
    ),
    # düzey 3
    '0020': patch(
        "İşletme 1 Mart 2025'te bankadan bir yıl vadeli, yıllık %36 basit faizli 600.000 ₺ kredi kullanmıştır. Faiz ve anapara vade sonunda ödenecektir. Buna göre 31 Aralık 2025'te tahakkuk ettirilecek faiz gideri kaç ₺'dir?",
        {
            'A': '180.000 ₺',
            'B': '216.000 ₺',
            'C': '234.000 ₺',
            'D': '198.000 ₺',
            'E': '324.000 ₺',
        },
        'A',
        "Mart-Aralık 10 aylık faiz 2025'e aittir: 600.000 × %36 × 10/12 = **180.000 ₺**. Kayıt: 780 (borç) / 381 Gider Tahakkukları (alacak). Kalan 2 aylık faiz 2026'nın gideridir.",
        'Dönemsellik; THP 780, 381',
    ),
    # düzey 3
    '0021': patch(
        "İşletme 120.000 ₺ tutarında ticari mal satın almış, 24.000 ₺ KDV hesaplanmıştır. Toplam bedelin 44.000 ₺'si bankadan ödenmiş, kalan tutar için satıcıya senet verilmiştir. Doğru kayıt hangisidir?",
        {
            'A': '153 Ticari Mallar 144.000 borç; 102 Bankalar 44.000 ve 321 Borç Senetleri 100.000 alacak',
            'B': '102 Bankalar 44.000 ve 321 Borç Senetleri 100.000 borç; 153 Ticari Mallar 120.000 ve 391 Hesaplanan KDV 24.000 alacak',
            'C': '153 Ticari Mallar 100.000 ve 191 İndirilecek KDV 20.000 borç; 102 Bankalar 20.000 ve 321 Borç Senetleri 100.000 alacak',
            'D': '153 Ticari Mallar 120.000 ve 191 İndirilecek KDV 24.000 borç; 102 Bankalar 44.000 ve 321 Borç Senetleri 100.000 alacak',
            'E': '153 Ticari Mallar 120.000 ve 191 İndirilecek KDV 24.000 borç; 102 Bankalar 44.000 ve 320 Satıcılar 100.000 alacak',
        },
        'D',
        "Mal maliyeti **153** hesabına, alış KDV'si **191** hesabına borç kaydedilir. Bankadan ödenen 44.000 ₺ **102** hesabına, senede bağlanan 144.000 − 44.000 = **100.000 ₺** ise **321 Borç Senetleri** hesabına alacak yazılır.",
        "1 Sıra No'lu MSUGT - 153/191/102/321",
    ),
    # düzey 2
    '0022': patch(
        "İşletmenin personelin ücretinden kestiği ve kendi işveren payıyla birlikte SGK'ya ödeyeceği sigorta primleri Tekdüzen Hesap Planı'nda hangi hesapta izlenir?",
        {
            'A': '770 Genel Yönetim Giderleri (dönem gideri)',
            'B': '331 Ortaklara Borçlar (ortaklara olan borç)',
            'C': '361 Ödenecek Sosyal Güvenlik Kesintileri',
            'D': '335 Personele Borçlar (ödenecek net ücret)',
            'E': '360 Ödenecek Vergi ve Fonlar (vergi dairesine)',
        },
        'C',
        "SGK'ya ödenecek (işçi + işveren payı) sigorta primleri **361 Ödenecek Sosyal Güvenlik Kesintileri** hesabında izlenir.",
        "1 Sıra No'lu MSUGT - 361",
    ),
    # düzey 2
    '0023': patch(
        "İşletme beş yıl vadeli ve 500.000 ₺ nominal değerli tahvilleri %4 iskontolu olarak banka aracılığıyla ihraç etmiştir. Tekdüzen Hesap Planı'na göre ihraç kaydı hangisidir?",
        {
            'A': '102 Bankalar 480.000 borç; 405 Çıkarılmış Tahviller 480.000 alacak',
            'B': '102 Bankalar 480.000 ve 408 Menkul Kıymetler İhraç Farkları 20.000 borç; 405 Çıkarılmış Tahviller 500.000 alacak',
            'C': '102 Bankalar 500.000 borç; 405 Çıkarılmış Tahviller 480.000 ve 408 Menkul Kıymetler İhraç Farkları 20.000 alacak',
            'D': '102 Bankalar 480.000 ve 780 Finansman Giderleri 20.000 borç; 405 Çıkarılmış Tahviller 500.000 alacak',
            'E': '111 Özel Kesim Tahvil, Senet ve Bonoları 500.000 borç; 102 Bankalar 480.000 ve 408 Menkul Kıymetler İhraç Farkları 20.000 alacak',
        },
        'B',
        "İskonto 500.000 × %4 = **20.000 ₺**, bankaya giren tutar 480.000 ₺'dir. Uzun vadeli tahvil borcu nominal değerle **405** hesabına alacak; ihraç farkı ise pasifi düzenleyen **408** hesabına borç kaydedilir.",
        "1 Sıra No'lu MSUGT - 405/408/102",
    ),
    # düzey 2
    '0024': patch(
        'Aşağıdakilerden hangisi uzun vadeli yabancı kaynaklar (4) grubunda yer alır?',
        {
            'A': '320 Satıcılar',
            'B': '360 Ödenecek Vergi ve Fonlar',
            'C': '300 Banka Kredileri',
            'D': '321 Borç Senetleri',
            'E': '405 Çıkarılmış Tahviller',
        },
        'E',
        '**405 Çıkarılmış Tahviller**, uzun vadeli (4) yabancı kaynaklar grubundadır. Diğerleri (320, 300, 321, 360) kısa vadeli (3) yabancı kaynaklardır.',
        "1 Sıra No'lu MSUGT - 3 / 4 grupları",
    ),
    # düzey 2
    '0025': patch(
        "İşletmenin kullandığı banka kredisine ilişkin ödediği/tahakkuk eden faizler Tekdüzen Hesap Planı'nda hangi hesapta izlenir?",
        {
            'A': '780 Finansman Giderleri',
            'B': '642 Faiz Gelirleri',
            'C': '647 Reeskont Faiz Gelirleri',
            'D': '300 Banka Kredileri',
            'E': '320 Satıcılar',
        },
        'A',
        "Kredi faizleri bir finansman gideridir → **780 Finansman Giderleri** hesabında izlenir. Anapara ise 300/400 Banka Kredileri'nde izlenir.",
        "1 Sıra No'lu MSUGT - 780 Finansman Giderleri",
    ),
    # düzey 2
    '0026': patch(
        'Banker ve sigorta şirketi olmayan bir işletme, VUK kapsamında vadesi gelmemiş senetli alacaklarını dönem sonunda tasarruf değeriyle değerlemeyi seçmiştir. Aynı nitelikte vadesi gelmemiş borç senetleri de bulunmaktadır. Hangisi doğrudur?',
        {
            'A': 'Borç senetleri reeskontu uygulanırsa alacak senetlerinde reeskont yapılması yasaktır.',
            'B': 'Senette faiz oranı yazmıyorsa işletmenin tahmin ettiği herhangi bir oran kullanılabilir.',
            'C': 'Alacak senetlerinde reeskont uygulanmışsa borç senetleri de aynı şekilde reeskonta tabi tutulmalıdır.',
            'D': 'Reeskont alacak senetlerine uygulanabilir; borç senetleri nominal değerle kalır.',
            'E': 'Reeskont seçimi yapıldığında senetsiz bütün ticari borçlar da zorunlu olarak indirgenir.',
        },
        'C',
        "VUK'ta banker ve sigorta şirketleri dışındaki mükellefler için senetli alacakları reeskonta tabi tutmak seçimliktir. Ancak bu seçim kullanıldığında **vadesi gelmemiş borç senetlerinin de reeskonta tabi tutulması zorunludur**. Senetsiz borçlar bu kurala girmez.",
        'VUK m. 281 ve 285',
    ),
    # düzey 2
    '0027': patch(
        "İşletme, 320 Satıcılar hesabındaki 40.000 ₺'lik borcunu banka havalesiyle ödemiştir. Bu işlemin kaydı aşağıdakilerden hangisidir?",
        {
            'A': '153 Ticari Mallar (borç) 40.000 / 320 Satıcılar (alacak) 40.000',
            'B': '320 Satıcılar (borç) 40.000 / 600 Yurt İçi Satışlar (alacak) 40.000',
            'C': '320 Satıcılar (borç) 40.000 / 102 Bankalar (alacak) 40.000',
            'D': '780 Finansman Giderleri (borç) 40.000 / 102 Bankalar (alacak) 40.000',
            'E': '102 Bankalar (borç) 40.000 / 320 Satıcılar (alacak) 40.000',
        },
        'C',
        'Borç ödendiğinde borç hesabı azalır → **320 Satıcılar (borç) 40.000**; banka çıkışı → **102 Bankalar (alacak) 40.000**.',
        "1 Sıra No'lu MSUGT - 320 / 102",
    ),
    # düzey 2
    '0028': patch(
        'Aralık ayında tüketilen ve tutarı güvenilir biçimde 18.000 ₺ olarak belirlenen yönetim binası elektriğinin faturası ocak ayında gelecektir. Dönem sonunda doğru kayıt hangisidir?',
        {
            'A': '770 Genel Yönetim Giderleri 18.000 borç; 480 Gelecek Yıllara Ait Gelirler 18.000 alacak',
            'B': '770 Genel Yönetim Giderleri 18.000 borç; 381 Gider Tahakkukları 18.000 alacak',
            'C': '381 Gider Tahakkukları 18.000 borç; 770 Genel Yönetim Giderleri 18.000 alacak',
            'D': '770 Genel Yönetim Giderleri 18.000 borç; 320 Satıcılar 18.000 alacak',
            'E': '180 Gelecek Aylara Ait Giderler 18.000 borç; 102 Bankalar 18.000 alacak',
        },
        'B',
        'Elektrik aralık ayında tüketildiği için gider **dönemsellik gereği aralık dönemine** aittir. Fatura ve ödeme sonraki dönemde olacağından 770 Genel Yönetim Giderleri borç, **381 Gider Tahakkukları** alacak kaydedilir.',
        "1 Sıra No'lu MSUGT - 770/381; dönemsellik",
    ),
    # düzey 2
    '0029': patch(
        "İşletme, 321 Borç Senetleri hesabındaki 60.000 ₺'lik senedi vadesinde banka aracılığıyla ödemiştir. Bu işlemin kaydı aşağıdakilerden hangisidir?",
        {
            'A': '321 Borç Senetleri (borç) 60.000 / 102 Bankalar (alacak) 60.000',
            'B': '121 Alacak Senetleri (borç) 60.000 / 102 Bankalar (alacak) 60.000',
            'C': '102 Bankalar (borç) 60.000 / 321 Borç Senetleri (alacak) 60.000',
            'D': '320 Satıcılar (borç) 60.000 / 321 Borç Senetleri (alacak) 60.000',
            'E': '321 Borç Senetleri (borç) 60.000 / 600 Yurt İçi Satışlar (alacak) 60.000',
        },
        'A',
        'Senetli borç ödendiğinde borç azalır → **321 Borç Senetleri (borç) 60.000**; banka çıkışı → **102 Bankalar (alacak) 60.000**.',
        "1 Sıra No'lu MSUGT - 321 / 102",
    ),
    # düzey 3
    '0030': patch(
        'Dönem sonunda 12.000 ₺ borç senedi reeskontu için 322 Borç Senetleri Reeskontu borçlandırılmış ve 647 Reeskont Faiz Gelirleri alacaklandırılmıştır. İzleyen dönem başındaki ters kayıt hangisidir?',
        {
            'A': '647 Reeskont Faiz Gelirleri 12.000 borç; 321 Borç Senetleri 12.000 alacak',
            'B': '657 Reeskont Faiz Giderleri 12.000 borç; 322 Borç Senetleri Reeskontu 12.000 alacak',
            'C': '321 Borç Senetleri 12.000 borç; 322 Borç Senetleri Reeskontu 12.000 alacak',
            'D': '322 Borç Senetleri Reeskontu 12.000 borç; 647 Reeskont Faiz Gelirleri 12.000 alacak',
            'E': '322 Borç Senetleri Reeskontu 12.000 borç; 657 Reeskont Faiz Giderleri 12.000 alacak',
        },
        'B',
        'Dönem sonu reeskontu yeni dönemin başında ters çevrilir: **657 Reeskont Faiz Giderleri borçlandırılır**, pasifi düzenleyici **322 Borç Senetleri Reeskontu alacaklandırılarak** kapatılır.',
        "1 Sıra No'lu MSUGT - 322/657",
    ),
    # düzey 2
    '0031': patch(
        'İşletme aynı hesap döneminde 50.000 ABD doları banka kredisi kullanmış; işlem tarihinde kur 36 ₺ iken krediyi 5.000 ABD doları faizle birlikte kurun 40 ₺ olduğu tarihte kapatmıştır. Önceden kur değerlemesi yapılmamıştır. Doğru kayıt bileşimi hangisidir?',
        {
            'A': '300 Banka Kredileri 1.800.000 ve 642 Faiz Gelirleri 400.000 borç; 102 Bankalar 2.200.000 alacak',
            'B': '300 Banka Kredileri 2.000.000 ve 780 Finansman Giderleri 200.000 borç; 102 Bankalar 2.200.000 alacak',
            'C': '300 Banka Kredileri 1.800.000 ve 656 Kambiyo Zararları 400.000 borç; 102 Bankalar 2.200.000 alacak',
            'D': '102 Bankalar 2.200.000 borç; 300 Banka Kredileri 1.800.000, 646 Kambiyo Kârları 200.000 ve 642 Faiz Gelirleri 200.000 alacak',
            'E': '300 Banka Kredileri 1.800.000, 656 Kambiyo Zararları 200.000 ve 780 Finansman Giderleri 200.000 borç; 102 Bankalar 2.200.000 alacak',
        },
        'E',
        'Kredi ilk kayıtta 50.000 × 36 = **1.800.000 ₺**dir. Anaparanın ödeme değerindeki artış 50.000 × (40−36) = **200.000 ₺ kambiyo zararı**, faiz ise 5.000 × 40 = **200.000 ₺ finansman gideri**dir. Bankadan toplam 55.000 × 40 = **2.200.000 ₺** çıkar.',
        "TMS 21, par. 28; 1 Sıra No'lu MSUGT - 300/656/780/102",
    ),
    # düzey 3
    '0032': patch(
        "Aşağıdaki borçlardan hangileri 'ticari borç' niteliğindedir?\n\nI. 320 Satıcılar\n\nII. 300 Banka Kredileri\n\nIII. 321 Borç Senetleri",
        {
            'A': 'I ve III',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'Yalnız I',
        },
        'A',
        '**I (320 Satıcılar)** ve **III (321 Borç Senetleri)** mal/hizmet alımından doğan **ticari borçlardır**. **II (300 Banka Kredileri)** ise mali (finansal) bir borçtur. Doğru cevap **I ve III**.',
        "1 Sıra No'lu MSUGT - 320 / 321 / 300",
    ),
    # düzey 3
    '0033': patch(
        'Aşağıdaki hesaplardan hangileri yabancı kaynak (borç) niteliğindedir?\n\nI. 320 Satıcılar\n\nII. 360 Ödenecek Vergi ve Fonlar\n\nIII. 500 Sermaye',
        {
            'A': 'II ve III',
            'B': 'Yalnız II',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'D',
        '**I (320 Satıcılar)** ve **II (360 Ödenecek Vergi ve Fonlar)** üçüncü kişilere olan borçlardır (yabancı kaynak). **III (500 Sermaye)** ise özkaynaktır. Doğru cevap **I ve II**.',
        "1 Sıra No'lu MSUGT - 3/4 vs 5",
    ),
    # düzey 3
    '0034': patch(
        "İşletmenin bilançosunda 300 Banka Kredileri 150.000 ₺, 320 Satıcılar 80.000 ₺ ve 360 Ödenecek Vergi ve Fonlar 20.000 ₺ olarak yer almaktadır. Başka borç bulunmadığına göre işletmenin toplam yabancı kaynağı (borcu) kaç ₺'dir?",
        {
            'A': '250.000',
            'B': '100.000',
            'C': '50.000',
            'D': '230.000',
            'E': '150.000',
        },
        'A',
        'Toplam yabancı kaynak = 150.000 + 80.000 + 20.000 = **250.000 ₺** (üç hesap da borç/yabancı kaynak niteliğindedir).',
        "1 Sıra No'lu MSUGT - 3 grubu",
    ),
    # düzey 2
    '0035': patch(
        "Tekdüzen Hesap Planı'ndaki 408 Menkul Kıymetler İhraç Farkları hesabıyla ilgili hangisi doğrudur?",
        {
            'A': 'Tahviller nominal değerinin üzerinde ihraç edildiğinde oluşan geliri gösteren bir özkaynak hesabıdır.',
            'B': 'Hisse senedi ihraç primlerini izleyen sermaye yedeği hesabıdır.',
            'C': 'Nominal değer ile ihraç bedeli arasındaki iskonto farkını izleyen pasifi düzenleyici hesaptır; dönemsel kısmı itfa edilerek finansman giderine aktarılır.',
            'D': 'İşletmenin yatırım amacıyla satın aldığı tahvilleri izleyen aktif menkul kıymet hesabıdır.',
            'E': 'Çıkarılmış tahvillerin anapara ödemesini izleyen banka hesabıdır.',
        },
        'C',
        '**408 Menkul Kıymetler İhraç Farkları**, tahvil ve benzeri borçlanma araçlarının nominal değerinden daha düşük bedelle ihracında oluşan farkı izleyen pasifi düzenleyici hesaptır. Farkın döneme düşen kısmı itfa edilerek finansman giderlerine aktarılır.',
        "1 Sıra No'lu MSUGT - 408/780",
    ),
    # düzey 3
    '0036': patch(
        "Yabancı kaynaklarla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. TMS 1'e göre normal faaliyet döngüsü içinde ödenecek ticari borç, döngü on iki aydan uzun olsa bile kısa vadeli sınıflandırılabilir.\n\nII. TMS 37'ye göre koşullu borç finansal tablolara yükümlülük olarak alınmaz; kaynak çıkışı ihtimali uzak değilse dipnotta açıklanır.\n\nIII. VUK kapsamında senetli alacaklarını reeskonta tabi tutan işletme, vadesi gelmemiş borç senetlerini de aynı işleme tabi tutar.",
        {
            'A': 'Yalnız I',
            'B': 'I, II ve III',
            'C': 'Yalnız II',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'B',
        "Üç ifade de doğrudur. TMS 1 faaliyet döngüsünü sınıflamada dikkate alır. TMS 37'de koşullu borç kayda alınmaz; çıkış ihtimali uzak değilse açıklanır. VUK'ta alacak senedi reeskontu seçildiğinde vadesi gelmemiş borç senetleri için de reeskont zorunludur.",
        'TMS 1, par. 69-70; TMS 37, par. 27-28; VUK m. 281 ve 285',
    ),
    # düzey 3
    '0037': patch(
        "Yönetim personelinin brüt ücreti 40.000 ₺'dir. Kesintiler: SGK işçi payı 5.600 ₺, işsizlik işçi payı 400 ₺, gelir vergisi 3.000 ₺, damga vergisi 300 ₺. İşveren payları: SGK 6.200 ₺, işsizlik 800 ₺. Buna göre ücret tahakkuk kaydında aşağıdakilerden hangisi yer almaz?",
        {
            'A': '361 Ödenecek Sosyal Güvenlik Kesintileri hesabı 13.000 ₺ alacaklandırılır',
            'B': '335 Personele Borçlar hesabı 30.700 ₺ alacaklandırılır',
            'C': '360 Ödenecek Vergi ve Fonlar hesabı 13.000 ₺ alacaklandırılır',
            'D': '770 Genel Yönetim Giderleri hesabı 47.000 ₺ borçlandırılır',
            'E': '360 Ödenecek Vergi ve Fonlar hesabı 3.300 ₺ alacaklandırılır',
        },
        'C',
        "Kayıt: 770 (borç) 47.000 / 335 (alacak) 30.700 + 360 (alacak) 3.300 + 361 (alacak) 13.000. Sigorta primleri 361'e, vergiler 360'a yazılır; 360'a prim tutarı yazılmaz.",
        'THP 335, 360, 361, 770',
    ),
    # düzey 3
    '0038': patch(
        'Yönetim personelinden biri için 472 Kıdem Tazminatı Karşılığı hesabında 80.000 ₺ karşılık bulunmaktadır. Personel emeklilik nedeniyle ayrılmış ve kendisine 100.000 ₺ kıdem tazminatı bankadan ödenmiştir (kesintiler ihmal). Buna göre ödeme kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '770 Genel Yönetim Giderleri hesabı 100.000 ₺ borçlandırılır',
            'B': '472 Kıdem Tazminatı Karşılığı hesabı 80.000 ₺ borçlandırılır',
            'C': '654 Karşılık Giderleri hesabı 20.000 ₺ borçlandırılır',
            'D': '335 Personele Borçlar hesabı 100.000 ₺ borçlandırılır',
            'E': '472 Kıdem Tazminatı Karşılığı hesabı 100.000 ₺ borçlandırılır',
        },
        'B',
        'Kayıt: **472 (borç) 80.000** + 770 (borç) 20.000 / 102 (alacak) 100.000. Önceden ayrılan karşılık kullanılır; karşılığı aşan 20.000 ₺ ödeme yılında personel gideri olarak yazılır.',
        'THP 472, 770, 102',
    ),
    # düzey 2
    '0039': patch(
        'Yabancı kaynaklarla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Senetsiz ticari borçlar 321 Borç Senetleri hesabında izlenir.\n\nII. Vadesi bir yılı aşan banka kredileri 400 Banka Kredileri hesabında izlenir.\n\nIII. Personele ödenecek net ücret 361 hesabında izlenir.',
        {
            'A': 'Yalnız II',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'II ve III',
        },
        'A',
        "Yalnız II doğrudur. Senetsiz ticari borçlar **320 Satıcılar**'da, personele ödenecek net ücret **335 Personele Borçlar**'da izlenir; 361 sosyal güvenlik kesintileri içindir.",
        'THP 320, 400, 335',
    ),
    # düzey 2
    '0040': patch(
        'Müşteri, daha önce işletmeye 30.000 ₺ avans ödediği siparişini iptal etmiş ve işletme avansı banka havalesiyle iade etmiştir. Buna göre iade kaydı aşağıdakilerden hangisidir?',
        {
            'A': '600 (borç) 30.000 / 102 (alacak) 30.000',
            'B': '340 (borç) 30.000 / 649 (alacak) 30.000',
            'C': '102 (borç) 30.000 / 340 (alacak) 30.000',
            'D': '340 (borç) 30.000 / 102 (alacak) 30.000',
            'E': '159 (borç) 30.000 / 102 (alacak) 30.000',
        },
        'D',
        "Alınan avans bir yükümlülük olarak 340'ta durmaktadır; iade edildiğinde yükümlülük kapanır: **340 (borç) / 102 (alacak)**. Satış gerçekleşmediği için hasılat hesabı kullanılmaz; 159 verilen avanslar içindir.",
        'THP 340, 102',
    ),
    # düzey 2
    '0041': patch(
        "İşletme 10.000 ABD doları tutarındaki banka kredisini işlem tarihindeki 1 ABD doları = 32 ₺ kuruyla kaydetmiştir. Raporlama tarihinde kur 34 ₺'dir. Ödeme yapılmamış ve korunma muhasebesi uygulanmamıştır. TMS 21'e göre dönem sonu işlemi hangisidir?",
        {
            'A': "Kredi 300.000 ₺'ye indirilir ve 20.000 ₺ kambiyo kârı muhasebeleştirilir.",
            'B': "Kredi 340.000 ₺'ye çıkarılır; 20.000 ₺ fark 780 Finansman Giderlerine değil 102 Bankalara kaydedilir.",
            'C': "Kredi 340.000 ₺'ye çıkarılır; 656 Kambiyo Zararları 20.000 borç, ilgili kredi hesabı 20.000 alacak kaydedilir.",
            'D': "Kredi 340.000 ₺'ye çıkarılır ve 20.000 ₺ kur farkı doğrudan özkaynağa kaydedilir.",
            'E': "Kredi 320.000 ₺'de bırakılır; kur değişimi ödeme tarihinde dikkate alınır.",
        },
        'C',
        'Yabancı para cinsinden kredi **parasal kalemdir** ve raporlama tarihinde kapanış kuruyla çevrilir: 10.000 × 34 = **340.000 ₺**. Başlangıçtaki 320.000 ₺ ile fark olan **20.000 ₺ kambiyo zararı**, korunma istisnası bulunmadığından kâr veya zararda muhasebeleştirilir.',
        "TMS 21 Kur Değişiminin Etkileri, par. 23 ve 28; 1 Sıra No'lu MSUGT - 656",
    ),
    # düzey 2
    '0042': patch(
        "İşletmenin ortaklarına olan (sermaye dışındaki) borçları Tekdüzen Hesap Planı'nda hangi hesapta izlenir?",
        {
            'A': '500 Sermaye',
            'B': '335 Personele Borçlar',
            'C': '331 Ortaklara Borçlar',
            'D': '320 Satıcılar',
            'E': '131 Ortaklardan Alacaklar',
        },
        'C',
        'İşletmenin ortaklarına olan (sermaye taahhüdü dışındaki) borçları **331 Ortaklara Borçlar** hesabında izlenir. (131 Ortaklardan Alacaklar ise tersidir, aktiftedir.)',
        "1 Sıra No'lu MSUGT - 331",
    ),
    # düzey 2
    '0043': patch(
        'İşletmenin 100.000 ₺ nominal değerli borç senedinin vadesi gelmiştir. Alacaklıyla anlaşarak borç üç ay vadeli yeni bir senede bağlanmış, 5.000 ₺ finansman faizi yeni senedin tutarına eklenmiştir. Doğru kayıt hangisidir?',
        {
            'A': '321 Borç Senetleri 105.000 borç; 100 Kasa 5.000 ve 321 Borç Senetleri 100.000 alacak',
            'B': '320 Satıcılar 100.000 ve 780 Finansman Giderleri 5.000 borç; 321 Borç Senetleri 105.000 alacak',
            'C': '321 Borç Senetleri 100.000 borç; 322 Borç Senetleri Reeskontu 5.000 ve 321 Borç Senetleri 95.000 alacak',
            'D': '321 Borç Senetleri 100.000 borç; 642 Faiz Gelirleri 5.000 ve 321 Borç Senetleri 95.000 alacak',
            'E': '321 Borç Senetleri 100.000 ve 780 Finansman Giderleri 5.000 borç; 321 Borç Senetleri 105.000 alacak',
        },
        'E',
        "Eski 100.000 ₺'lik senet borcu **321 hesabı borçlandırılarak** kapatılır. Yeni finansman için doğan 5.000 ₺ **780 Finansman Giderleri**ne borç, toplam 105.000 ₺'lik yeni senet ise **321 hesabına alacak** kaydedilir.",
        "1 Sıra No'lu MSUGT - 321/780",
    ),
    # düzey 2
    '0044': patch(
        'İşletme 300.000 ₺ tutarındaki ticari malı iki yıl vadeli borçlanarak satın almıştır. KDV ve vade farkı ihmal edilirse işlem anında temel muhasebe eşitliğinde nasıl bir değişim olur?',
        {
            'A': 'Yabancı kaynaklar 300.000 ₺ azalır, özkaynak aynı tutarda artar.',
            'B': 'Varlıklar ve yabancı kaynaklar 300.000 ₺ azalır.',
            'C': 'Duran varlıklar artar; pasif toplamı değişmez.',
            'D': 'Varlıklar 300.000 ₺ artar, özkaynak 300.000 ₺ azalır; borç değişmez.',
            'E': 'Varlıklar ve yabancı kaynaklar 300.000 ₺ artar; özkaynak değişmez.',
        },
        'E',
        'Kredili mal alımında stok varlığı **300.000 ₺ artar**; ödeme yapılmadığı için aynı tutarda uzun vadeli ticari borç doğar. İşlem gelir veya gider yaratmadığından özkaynak değişmez ve eşitlik korunur.',
        "Temel muhasebe eşitliği; 1 Sıra No'lu MSUGT - 153/420",
    ),
    # düzey 2
    '0045': patch(
        "Dönem sonunda uzun vadeli banka kredisinin 100.000 ₺ anapara taksidinin izleyen hesap döneminde ödeneceği belirlenmiştir. Tekdüzen Hesap Planı'na göre aktarma kaydı hangisidir?",
        {
            'A': '400 Banka Kredileri 100.000 borç; 303 Uzun Vadeli Kredilerin Anapara Taksitleri ve Faizleri 100.000 alacak',
            'B': '400 Banka Kredileri 100.000 borç; 300 Banka Kredileri 100.000 alacak',
            'C': '303 Uzun Vadeli Kredilerin Anapara Taksitleri ve Faizleri 100.000 borç; 400 Banka Kredileri 100.000 alacak',
            'D': '780 Finansman Giderleri 100.000 borç; 303 Uzun Vadeli Kredilerin Anapara Taksitleri ve Faizleri 100.000 alacak',
            'E': '400 Banka Kredileri 100.000 borç; 320 Satıcılar 100.000 alacak',
        },
        'A',
        'Uzun vadeli kredinin bir yıl içinde ödenecek anapara taksidi, **400 Banka Kredileri borçlandırılarak** uzun vadeden çıkarılır; kısa vadeli **303 Uzun Vadeli Kredilerin Anapara Taksitleri ve Faizleri** hesabına alacak kaydedilir.',
        "1 Sıra No'lu MSUGT - 400/303",
    ),
    # düzey 3
    '0046': patch(
        "Bir dönemde işletmenin hesapladığı KDV (391 Hesaplanan KDV) 50.000 ₺, indirilecek KDV'si (191 İndirilecek KDV) 30.000 ₺'dir. Dönem sonunda mahsuplaşma sonucu vergi dairesine ödenecek KDV kaç ₺'dir?",
        {
            'A': '50.000',
            'B': '30.000',
            'C': '80.000',
            'D': '20.000',
            'E': '0',
        },
        'D',
        "Ödenecek KDV = Hesaplanan KDV − İndirilecek KDV = 50.000 − 30.000 = **20.000 ₺** → 360 Ödenecek Vergi ve Fonlar'a aktarılır.",
        "3065 s. KDVK; 1 Sıra No'lu MSUGT - 391/191/360",
    ),
    # düzey 2
    '0047': patch(
        'İşletme, ileride teslim edeceği mal için müşterisinden 30.000 ₺ avansı nakit tahsil etmiştir. Bu işlemin kaydı aşağıdakilerden hangisidir?',
        {
            'A': '340 Alınan Sipariş Avansları (borç) 30.000 / 100 Kasa (alacak) 30.000',
            'B': '100 Kasa (borç) 30.000 / 340 Alınan Sipariş Avansları (alacak) 30.000',
            'C': '159 Verilen Sipariş Avansları (borç) 30.000 / 100 Kasa (alacak) 30.000',
            'D': '120 Alıcılar (borç) 30.000 / 340 Alınan Sipariş Avansları (alacak) 30.000',
            'E': '100 Kasa (borç) 30.000 / 600 Yurt İçi Satışlar (alacak) 30.000',
        },
        'B',
        'Nakit girişi → **100 Kasa (borç) 30.000**; teslim edilmemiş mal için alınan avans bir borçtur → **340 Alınan Sipariş Avansları (alacak) 30.000**. Mal teslim edilince avans gelire dönüşür.',
        "1 Sıra No'lu MSUGT - 340 / 100",
    ),
    # düzey 3
    '0048': patch(
        "Bir personelin aylık brüt ücreti 30.000 ₺'dir. Bu ücretten toplam 7.500 ₺ yasal kesinti (SGK işçi payı + gelir vergisi + damga vb.) yapılmıştır. Personele ödenecek net ücret (335 Personele Borçlar) kaç ₺'dir?",
        {
            'A': '15.000',
            'B': '37.500',
            'C': '7.500',
            'D': '22.500',
            'E': '30.000',
        },
        'D',
        "Net ücret = Brüt − Yasal kesintiler = 30.000 − 7.500 = **22.500 ₺** → 335 Personele Borçlar. Kesintiler ise 360 ve 361'de izlenir.",
        "1 Sıra No'lu MSUGT - 335 / 360 / 361",
    ),
    # düzey 2
    '0049': patch(
        "İşletme, 360 Ödenecek Vergi ve Fonlar hesabındaki 20.000 ₺'lik vergi borcunu banka aracılığıyla vergi dairesine ödemiştir. Bu işlemin kaydı aşağıdakilerden hangisidir?",
        {
            'A': '360 Ödenecek Vergi ve Fonlar (borç) 20.000 / 102 Bankalar (alacak) 20.000',
            'B': '360 Ödenecek Vergi ve Fonlar (borç) 20.000 / 391 Hesaplanan KDV (alacak) 20.000',
            'C': '193 Peşin Ödenen Vergiler (borç) 20.000 / 102 Bankalar (alacak) 20.000',
            'D': '770 Genel Yönetim Giderleri (borç) 20.000 / 102 Bankalar (alacak) 20.000',
            'E': '102 Bankalar (borç) 20.000 / 360 Ödenecek Vergi ve Fonlar (alacak) 20.000',
        },
        'A',
        'Vergi borcu ödendiğinde borç azalır → **360 Ödenecek Vergi ve Fonlar (borç) 20.000**; banka çıkışı → **102 Bankalar (alacak) 20.000**.',
        "1 Sıra No'lu MSUGT - 360 / 102",
    ),
    # düzey 2
    '0050': patch(
        "'320 Satıcılar' hesabının işleyişi ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Bir gelir hesabıdır; dönem içinde alacaklandırılır, dönem sonunda 690 Dönem Kârı veya Zararı hesabına devredilerek kapatılır.',
            'B': 'Bir aktif (varlık) hesabıdır; borç doğduğunda borçlandırılır, tahsil edildiğinde alacaklandırılır ve normalde borç kalanı verir.',
            'C': 'Bir gider hesabıdır; oluştukça borçlandırılır, dönem sonunda sonuç hesaplarına aktarılarak kapatıldığından bilançoda kalan vermez.',
            'D': 'Bir pasif (kaynak) hesabıdır; borç doğduğunda alacaklandırılır, ödendiğinde borçlandırılır ve alacak kalanı verir.',
            'E': 'Bir nazım (kayıt dışı) hesaptır; bilanço toplamına dahil edilmez, izleme amacıyla çift taraflı çalıştırılır.',
        },
        'D',
        '**320 Satıcılar** bir **pasif (kaynak)** hesabıdır; ticari borç doğduğunda **alacaklandırılır (alacak)**, borç ödendiğinde **borçlandırılır (borç)** ve normalde **alacak kalanı** verir.',
        "1 Sıra No'lu MSUGT - 320",
    ),
    # düzey 3
    '0051': patch(
        "Bir dönemde 391 Hesaplanan KDV 80.000 ₺, 191 İndirilecek KDV 50.000 ₺'dir. Dönem sonu mahsuplaşma sonucu vergi dairesine ödenecek KDV kaç ₺'dir?",
        {
            'A': '50.000',
            'B': '80.000',
            'C': '30.000',
            'D': '0',
            'E': '130.000',
        },
        'C',
        'Ödenecek KDV = 80.000 − 50.000 = **30.000 ₺** → 360 Ödenecek Vergi ve Fonlar.',
        "3065 s. KDVK; 1 Sıra No'lu MSUGT - 391/191/360",
    ),
    # düzey 3
    '0052': patch(
        "Bir personelin aylık brüt ücreti 40.000 ₺'dir. Toplam yasal kesintiler 10.000 ₺ olduğuna göre, '335 Personele Borçlar' hesabına yazılacak net ücret kaç ₺'dir?",
        {
            'A': '20.000',
            'B': '10.000',
            'C': '40.000',
            'D': '50.000',
            'E': '30.000',
        },
        'E',
        'Net ücret = Brüt − Yasal kesintiler = 40.000 − 10.000 = **30.000 ₺** → 335 Personele Borçlar.',
        "1 Sıra No'lu MSUGT - 335 / 360 / 361",
    ),
    # düzey 2
    '0053': patch(
        'İşletme, üç ay sonra teslim edeceği ürün için müşteriden 60.000 ₺ tahsil etmiştir. Ürün henüz teslim edilmemiş ve gelir için edim yükümlülüğü yerine getirilmemiştir. En uygun değerlendirme hangisidir?',
        {
            'A': 'Nakit tahsil edildiği anda 600 Yurt İçi Satışlar hesabına gelir yazılır ve borç doğmaz.',
            'B': 'Tahsilat 340 Alınan Sipariş Avanslarında bir yükümlülük olarak izlenir; teslimden önce satış geliri kaydedilmez.',
            'C': 'Ürün teslim edilmediği için banka veya kasa girişi de muhasebeleştirilmez.',
            'D': 'Tahsilat 159 Verilen Sipariş Avansları hesabına borç kaydedilir.',
            'E': 'Tutar müşterinin işletmeye sermaye katkısı sayılarak 500 Sermaye hesabına alınır.',
        },
        'B',
        'Müşteri bedeli ödemiş olsa da ürün teslim edilmediğinden işletmenin edim yükümlülüğü sürer. Tutar **340 Alınan Sipariş Avansları** hesabında yabancı kaynak olarak izlenir; teslim gerçekleşmeden satış geliri kaydedilmez.',
        "1 Sıra No'lu MSUGT - 340; TFRS 15, par. 106",
    ),
    # düzey 3
    '0054': patch(
        'Vergi beyannamesinin verilmesi sırasında 370 Dönem Kârı Vergi ve Diğer Yasal Yükümlülük Karşılıkları hesabında 150.000 ₺, bunu düzenleyen 371 hesabında 110.000 ₺ bulunmaktadır. Net vergi borcunun 360 hesaba aktarım kaydı hangisidir?',
        {
            'A': '370 hesabı 150.000 borç; 371 hesabı 110.000 ve 360 hesabı 40.000 alacak',
            'B': '193 hesabı 110.000 borç; 360 hesabı 110.000 alacak',
            'C': '370 hesabı 40.000 borç; 360 hesabı 40.000 alacak, 371 hesabı açık bırakılır',
            'D': '371 hesabı 110.000 ve 360 hesabı 40.000 borç; 370 hesabı 150.000 alacak',
            'E': '360 hesabı 150.000 borç; 370 hesabı 150.000 alacak',
        },
        'A',
        'Kesinleşen vergi borcu aktarılırken **370 hesabı 150.000 ₺ borçlandırılarak** kapatılır. Peşin ödemeleri temsil eden **371 hesabı 110.000 ₺ alacaklandırılır**; kalan 40.000 ₺ net borç **360 Ödenecek Vergi ve Fonlar** hesabına alacak kaydedilir.',
        "1 Sıra No'lu MSUGT - 370/371/360",
    ),
    # düzey 2
    '0055': patch(
        'İşletme çalıştırdığı personel için ücret tahakkuku yaparken, personelin ücretinden kestiği gelir vergisi ve damga vergisini hangi hesapta izler?',
        {
            'A': '193 Peşin Ödenen Vergiler ve Fonlar',
            'B': '770 Genel Yönetim Giderleri',
            'C': '335 Personele Borçlar',
            'D': '361 Ödenecek Sosyal Güvenlik Kesintileri',
            'E': '360 Ödenecek Vergi ve Fonlar',
        },
        'E',
        "Ücretten kesilen gelir vergisi (stopaj) ve damga vergisi, işletmenin vergi dairesine ödeyeceği borç olduğundan **360 Ödenecek Vergi ve Fonlar** hesabında izlenir. SGK kesintileri ise 361'de izlenir.",
        "1 Sıra No'lu MSUGT - 360 / 361",
    ),
    # düzey 3
    '0056': patch(
        "Yönetim personelinin aylık brüt ücreti 60.000 ₺'dir. Ücretten SGK işçi payı 8.400 ₺, işsizlik sigortası işçi payı 600 ₺, gelir vergisi 5.000 ₺ ve damga vergisi 400 ₺ kesilmiştir. İşveren SGK payı 9.300 ₺, işsizlik sigortası işveren payı 1.200 ₺'dir. Buna göre ücret tahakkuk kaydında 361 Ödenecek Sosyal Güvenlik Kesintileri hesabına alacak yazılacak tutar kaç ₺'dir?",
        {
            'A': '9.000 ₺',
            'B': '19.500 ₺',
            'C': '14.400 ₺',
            'D': '10.500 ₺',
            'E': '24.900 ₺',
        },
        'B',
        "361'e işçi ve işveren payları birlikte yazılır: 8.400 + 600 + 9.300 + 1.200 = **19.500 ₺**. Gelir ve damga vergisi (5.400 ₺) 360'a, net ücret (45.600 ₺) 335'e yazılır; işveren payları ayrıca 770'e gider olarak kaydedilir.",
        'THP 335, 360, 361, 770',
    ),
    # düzey 3
    '0057': patch(
        "İşletme vadesi gelen 200.000 ₺ banka kredisini 18.000 ₺ faiziyle birlikte bankadan ödemiştir. Faizin 12.000 ₺'lik kısmı önceki dönem sonunda 381 Gider Tahakkukları hesabına alınmıştı. Buna göre ödeme kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '300 Banka Kredileri hesabı 218.000 ₺ borçlandırılır',
            'B': '381 Gider Tahakkukları hesabı 18.000 ₺ borçlandırılır',
            'C': '780 Finansman Giderleri hesabı 18.000 ₺ borçlandırılır',
            'D': '381 Gider Tahakkukları hesabı 12.000 ₺ alacaklandırılır',
            'E': '780 Finansman Giderleri hesabı 6.000 ₺ borçlandırılır',
        },
        'E',
        'Kayıt: 300 (borç) 200.000 + 381 (borç) 12.000 + **780 (borç) 6.000** / 102 (alacak) 218.000. Önceki döneme ait faiz tahakkuk kaydıyla gider yazılmıştır; bu dönem yalnız kalan 6.000 ₺ giderdir.',
        'THP 300, 381, 780, 102',
    ),
    # düzey 2
    '0058': patch(
        "İşletme kiraya verdiği depo için kiracıdan, kira süresinin sonunda (üç yıl sonra) iade edilmek üzere 60.000 ₺ depozito almıştır. Bu depozito Tekdüzen Hesap Planı'nda hangi hesapta izlenir?",
        {
            'A': '649 Diğer Olağan Gelir ve Kârlar',
            'B': '226 Verilen Depozito ve Teminatlar',
            'C': '340 Alınan Sipariş Avansları',
            'D': '426 Alınan Depozito ve Teminatlar',
            'E': '326 Alınan Depozito ve Teminatlar',
        },
        'D',
        "Alınan depozito bir yükümlülüktür; iade süresi bir yılı aştığı için uzun vadeli **426**'da izlenir. İade tarihi bir yıl içine girdiğinde 326'ya aktarılır. 226 verilen depozitolar içindir.",
        'THP 326, 426',
    ),
    # düzey 3
    '0059': patch(
        "Bir işletmenin dönem sonu mizanında şu kalanlar vardır: 300 Banka Kredileri 150.000 ₺, 320 Satıcılar 80.000 ₺, 321 Borç Senetleri 60.000 ₺, 322 Borç Senetleri Reeskontu 5.000 ₺, 340 Alınan Sipariş Avansları 40.000 ₺, 360 Ödenecek Vergi ve Fonlar 20.000 ₺ ve 400 Banka Kredileri 300.000 ₺. Buna göre bilançodaki kısa vadeli yabancı kaynaklar toplamı kaç ₺'dir?",
        {
            'A': '495.000 ₺',
            'B': '355.000 ₺',
            'C': '345.000 ₺',
            'D': '385.000 ₺',
            'E': '645.000 ₺',
        },
        'C',
        '150.000 + 80.000 + 60.000 − 5.000 (322 pasifi düzenleyicidir) + 40.000 + 20.000 = **345.000 ₺**. 400 uzun vadelidir.',
        'THP 3 Kısa Vadeli Yabancı Kaynaklar',
    ),
    # düzey 2
    '0060': patch(
        'Bir işletmenin yabancı kaynakları sınıflandırılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "İzleyen yıl ödenecek uzun vadeli kredi taksitleri 303'e aktarılır",
            'B': "Ödenecek vergiler 360'ta izlenir",
            'C': "Üç yıl sonra iade edilecek alınan depozito 426'da izlenir",
            'D': "Çıkarılan tahviller 405'te izlenir",
            'E': "Vadesi 18 ay olan banka kredisi 300 Banka Kredileri'nde izlenir",
        },
        'E',
        "Vadesi bir yılı aşan banka kredisi **400 Banka Kredileri**'nde (uzun vadeli) izlenir; izleyen yıl ödenecek taksitleri 303 Uzun Vadeli Kredilerin Anapara Taksitleri ve Faizleri'ne aktarılır.",
        'THP 3-4 Yabancı Kaynaklar',
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
    print(f"1 paket / {len(PATCHES)} soru ('Yabanci Kaynaklar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
