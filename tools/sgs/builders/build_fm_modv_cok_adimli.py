#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Maddi Olmayan Duran Varliklar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

FM cok adimli tur. 47 soru korundu; tms_38 paketiyle en cok cakisan 13 TMS 38 sorusu cikarildi, ilk turdan kalan 26 mutlak ifadeli sik dogruluk degeri korunarak onarildi. Yerine THP/VUK kalibinda 13 soru: ozel maliyetin kira suresine gore itfasi, net degeri ve erken tahliye, hak satisinda kar kaydi (268), patent maliyeti, isletme devrinde serefiye hesabi ve kaydi, yazilim lisansi alimi, itfa payinin uretim/yonetime dagitimi, olumsuz ve oncullu sorular. Kor ogrenci %21.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: VUK m. 262, 270, 327 · Tekduzen Hesap Plani 26 Maddi Olmayan Duran Varliklar, 268, 689 · 1 Sira No'lu MSUGT
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/finansal_muhasebe/maddi_olmayan_duran_varliklar.json"
STYLE_REF = 'SGS Finansal Muhasebe (çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "finmuh-modv-gen-"


def patch(stem, options, answer, solution, ref='VUK m. 327; Tekduzen Hesap Plani 26'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Bir işletmenin dönem sonu kayıtlarında şu kalemler bulunmaktadır: satın alınan patent 90.000 ₺, aktifleştirilen araştırma ve geliştirme gideri 60.000 ₺, kiralanan mağazaya yapılan özel maliyet 45.000 ₺, kayıtlarda izlenen şerefiye 100.000 ₺, bir yazılım lisansının alımı için satıcıya verilen avans 20.000 ₺, maddi olmayan duran varlıklar için ayrılmış birikmiş itfa payları 40.000 ₺, yeni bir makinenin alımı için verilen avans 25.000 ₺ ve bilgisayar donanımı 50.000 ₺.\n\nBuna göre bilançoda '26 Maddi Olmayan Duran Varlıklar' grubunun net tutarı kaç ₺ olur?",
        {
            'A': '275.000',
            'B': '300.000',
            'C': '255.000',
            'D': '315.000',
            'E': '325.000',
        },
        'A',
        '26 grubu: 260 Haklar 90.000 + 263 Araştırma ve Geliştirme Giderleri 60.000 + 264 Özel Maliyetler 45.000 + 261 Şerefiye 100.000 + 269 Verilen Avanslar 20.000 − 268 Birikmiş Amortismanlar 40.000 = 275.000 ₺. Makine alımı için verilen avans 259 Verilen Avanslar (25 grubu), bilgisayar donanımı 255 Demirbaşlar hesabında izlenir.',
        "1 Sıra No'lu MSUGT - 26 Maddi Olmayan Duran Varlıklar",
    ),
    # düzey 2
    '0002': patch(
        "İşletmenin kurulması, yeni bir şubenin açılması veya işlerin sürekli olarak genişletilmesi için yapılan ve gelecek yıllara yayılan giderler Tekdüzen Hesap Planı'nda hangi hesapta izlenir?",
        {
            'A': '264 Özel Maliyetler',
            'B': '262 Kuruluş ve Örgütlenme Giderleri',
            'C': '260 Haklar',
            'D': '770 Genel Yönetim Giderleri',
            'E': '261 Şerefiye',
        },
        'B',
        'İşletmenin kurulması/örgütlenmesi veya işlerin sürekli genişletilmesi için yapılıp aktifleştirilen giderler **262 Kuruluş ve Örgütlenme Giderleri** hesabında izlenir ve genellikle 5 yılda eşit tutarlarla itfa edilir.',
        "1 Sıra No'lu MSUGT - 262; VUK md. 326",
    ),
    # düzey 2
    '0003': patch(
        'İşletme, üretiminde kullanmak üzere bir patenti 100.000 ₺ + %20 KDV bedelle peşin (nakit) satın almıştır. Bu işlemin kaydı aşağıdakilerden hangisidir?',
        {
            'A': '261 Şerefiye (borç) 100.000 + 191 İndirilecek KDV (borç) 20.000 / 100 Kasa (alacak) 120.000',
            'B': '260 Haklar (borç) 100.000 + 391 Hesaplanan KDV (borç) 20.000 / 100 Kasa (alacak) 120.000',
            'C': '260 Haklar (borç) 100.000 + 191 İndirilecek KDV (borç) 20.000 / 100 Kasa (alacak) 120.000',
            'D': '770 Genel Yönetim Giderleri (borç) 100.000 + 191 İndirilecek KDV (borç) 20.000 / 100 Kasa (alacak) 120.000',
            'E': '260 Haklar (borç) 120.000 / 100 Kasa (alacak) 120.000',
        },
        'C',
        'Patent bir haktır → **260 Haklar (borç) 100.000**; alışta KDV **191 İndirilecek KDV (borç) 20.000**; nakit çıkışı **100 Kasa (alacak) 120.000**. KDV maliyete eklenmez, ayrı izlenir.',
        "1 Sıra No'lu MSUGT - 260; 3065 s. KDVK",
    ),
    # düzey 2
    '0004': patch(
        "İşletme bir restoran zincirinin franchise (bayilik) hakkını beş yıllığına edinmiş ve 500.000 ₺ giriş bedelini peşin ödemiştir. Sözleşmeye göre ayrıca her yıl net satışların %3'ü oranında kullanım ücreti (royalti) ödenecektir. İlk yılın net satışları 2.000.000 ₺'dir. Hak yıl başında edinilmiş olup süresi boyunca eşit tutarlarla itfa edilmektedir.\n\nBuna göre bu sözleşme nedeniyle ilk yılın sonucuna yansıyan toplam gider kaç ₺'dir?",
        {
            'A': '100.000',
            'B': '60.000',
            'C': '560.000',
            'D': '500.000',
            'E': '160.000',
        },
        'E',
        'Peşin ödenen giriş bedeli 260 Haklar hesabında aktifleştirilir ve beş yılda itfa edilir: 500.000 / 5 = 100.000 ₺. Satışa bağlı royalti dönemin gideridir: 2.000.000 × %3 = 60.000 ₺. İlk yılın toplam gideri 160.000 ₺.',
        'VUK md. 327',
    ),
    # düzey 2
    '0005': patch(
        'İşletme, kiraladığı iş yerine yaptığı 50.000 ₺ + %20 KDV tutarındaki kalıcı değer artırıcı harcamayı nakit ödemiştir. Bu harcamanın kaydı aşağıdakilerden hangisidir?',
        {
            'A': '252 Binalar (borç) 50.000 + 191 İndirilecek KDV (borç) 10.000 / 100 Kasa (alacak) 60.000',
            'B': '260 Haklar (borç) 50.000 + 191 İndirilecek KDV (borç) 10.000 / 100 Kasa (alacak) 60.000',
            'C': '264 Özel Maliyetler (borç) 60.000 / 100 Kasa (alacak) 60.000',
            'D': '264 Özel Maliyetler (borç) 50.000 + 191 İndirilecek KDV (borç) 10.000 / 100 Kasa (alacak) 60.000',
            'E': '770 Genel Yönetim Giderleri (borç) 60.000 / 100 Kasa (alacak) 60.000',
        },
        'D',
        'Kiralanan yere yapılan kalıcı değer artırıcı harcama **264 Özel Maliyetler (borç) 50.000**; KDV **191 İndirilecek KDV (borç) 10.000**; nakit **100 Kasa (alacak) 60.000**. Bina işletmenin mülkü olmadığından 252 kullanılmaz.',
        "1 Sıra No'lu MSUGT - 264; VUK md. 272",
    ),
    # düzey 3
    '0006': patch(
        "İşletme içi bir yazılım projesinde araştırma safhasında 100.000 ₺, geliştirme safhasında aktifleştirme koşulları sağlanmadan önce 40.000 ₺ ve koşulların tamamı sağlandıktan sonra 160.000 ₺ harcanmıştır. TMS 38'e göre aktifleştirilecek tutar kaç ₺'dir?",
        {
            'A': '140.000',
            'B': '160.000',
            'C': '40.000',
            'D': '120.000',
            'E': '300.000',
        },
        'B',
        'Araştırma harcamaları ve geliştirme aşamasında ölçütler sağlanmadan önce oluşan tutarlar giderdir. Maliyet, muhasebeleştirme ölçütlerinin **ilk sağlandığı tarihten itibaren** birikir. Bu nedenle yalnız sonraki **160.000 ₺** aktifleştirilir.',
        'TMS 38, par. 54, 57 ve 65',
    ),
    # düzey 2
    '0007': patch(
        'TMS 38 uygulayan işletmenin yeni şube açılışı için yaptığı personel eğitimi, reklam ve açılış organizasyonu harcamaları nasıl muhasebeleştirilir?',
        {
            'A': 'Şube kâr ederse aktifleştirilerek, zarar ederse gider yazılarak',
            'B': 'Maddi duran varlık maliyetinde',
            'C': 'Tanımlanabilir bir varlık oluşturmadıklarından hizmet alındığında gider olarak',
            'D': 'Şerefiye hesabında',
            'E': 'Gelecek dönemlerde şubenin satışlarını artırması beklendiğinden eğitim, reklam ve açılış organizasyonu harcamalarının tamamı sınırsız yararlı ömürlü tek bir maddi olmayan duran varlık olarak',
        },
        'C',
        "Kuruluş ve açılış öncesi maliyetleri, eğitim ile reklam ve promosyon harcamaları TMS 38'de ayrıca tanımlanabilir bir varlık oluşturmadıklarından **gerçekleştikleri veya hizmet alındığı anda gider** olarak muhasebeleştirilir.",
        'TMS 38, par. 69(a)-(c)',
    ),
    # düzey 2
    '0008': patch(
        "Bir yazılımın dönem başı defter değeri 180.000 ₺, kalıntı değeri sıfırdır. Teknolojik gelişmeler nedeniyle kalan yararlı ömür 3 yıl olarak revize edilmiştir. TMS 38 ve TMS 8'e göre cari yıl itfa payı kaç ₺ olur ve değişiklik nasıl uygulanır?",
        {
            'A': '180.000 ₺; geçmiş dönemlere geriye dönük',
            'B': '90.000 ₺; geçmiş yıllar düzeltilerek',
            'C': '30.000 ₺; dipnotta açıklanır, kayda alınmaz',
            'D': 'İtfa ayrılmaz; ilk muhasebeleştirmede belirlenen yararlı ömür değiştirilemez ve yeni teknolojik bilgiler dipnotta açıklanır.',
            'E': '60.000 ₺; cari ve gelecek dönemlere ileriye yönelik',
        },
        'E',
        'Yararlı ömür değişikliği muhasebe tahmini değişikliğidir ve **ileriye yönelik** uygulanır. Yeni yıllık itfa payı 180.000 ÷ 3 = **60.000 ₺**dir; önceki dönem finansal tabloları geriye dönük düzeltilmez.',
        'TMS 38, par. 104; TMS 8',
    ),
    # düzey 2
    '0009': patch(
        "Aktifleştirilen 40.000 ₺ tutarındaki araştırma-geliştirme gideri (263), VUK'a göre 5 yılda eşit tutarlarla itfa edilecektir. Yıllık itfa payı kaç ₺'dir?",
        {
            'A': '20.000',
            'B': '10.000',
            'C': '4.000',
            'D': '8.000',
            'E': '40.000',
        },
        'D',
        'Yıllık itfa payı = 40.000 ÷ 5 = **8.000 ₺**. Aktifleştirilen AR-GE giderleri (263) genellikle 5 yılda eşit tutarlarla itfa edilir.',
        "VUK md. 326; 1 Sıra No'lu MSUGT - 263",
    ),
    # düzey 2
    '0010': patch(
        "İşletme, 4 yıllığına kiraladığı depoya 80.000 ₺'lik özel maliyet niteliğinde harcama yapmıştır. Kira süresi boyunca eşit itfa edildiğine göre yıllık itfa payı kaç ₺'dir?",
        {
            'A': '20.000',
            'B': '13.333',
            'C': '10.000',
            'D': '80.000',
            'E': '16.000',
        },
        'A',
        'Özel maliyet kira süresi boyunca itfa edilir: 80.000 ÷ 4 = **20.000 ₺/yıl**.',
        'VUK md. 327',
    ),
    # düzey 2
    '0011': patch(
        "TMS/TFRS'ye göre satın alınan (devralmadan doğan) şerefiyenin sonraki dönemlerde muhasebeleştirilmesi ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Şerefiye her dönem sonunda rayiç değeriyle yeniden ölçülür ve değerindeki artış dönem geliri olarak yazılır.',
            'B': 'Şerefiye tahsil edilecek bir tutar sayıldığından doğrudan özkaynaklara eklenir ve orada izlenir.',
            'C': 'Şerefiye, VUK uygulamasında olduğu gibi her yıl eşit tutarlarla ve 5 yılda tamamen itfa edilerek giderleştirilir.',
            'D': 'Şerefiye bir yıl içinde ödenecek nitelikte kabul edilerek kısa vadeli yabancı kaynaklar içinde sınıflandırılır.',
            'E': 'İtfa edilmez; bunun yerine her yıl (ve belirti varsa daha sık) değer düşüklüğü (impairment) testine tabi tutulur.',
        },
        'E',
        "TMS/TFRS'ye göre şerefiye **itfa edilmez**; her yıl **değer düşüklüğü testine** tabi tutulur ve gerekiyorsa değer düşüklüğü zararı yazılır. (VUK uygulamasında ise şerefiye 5 yılda itfa edilebilir — bu iki düzenleme farklıdır.)",
        'TMS 36/TFRS 3 (şerefiye itfa edilmez, değer düşüklüğü)',
    ),
    # düzey 3
    '0012': patch(
        "İşletme muhasebe biriminde kullanmak üzere 60.000 ₺'ye bir bilgisayar sunucusu satın almıştır. Sunucunun çalışması için zorunlu olan ve onunla birlikte faturalanan işletim sistemi 6.000 ₺'dir. Ayrıca sunucudan bağımsız olarak lisanslanan ve başka bilgisayarlara da kurulabilen bir muhasebe paket programı 24.000 ₺'ye alınmıştır. KDV ihmal edilecektir.\n\nBuna göre bu kalemler hangi hesaplara hangi tutarlarla kaydedilir?",
        {
            'A': '255 Demirbaşlar 60.000 ₺; 260 Haklar 30.000 ₺',
            'B': '255 Demirbaşlar 66.000 ₺; 260 Haklar 24.000 ₺',
            'C': '255 Demirbaşlar 90.000 ₺; 260 Haklar hesabı çalışmaz',
            'D': '255 Demirbaşlar 60.000 ₺; 263 Araştırma ve Geliştirme 30.000 ₺',
            'E': '253 Tesis, Makine ve Cihazlar 66.000 ₺; 260 Haklar 24.000 ₺',
        },
        'B',
        'Donanımın ayrılmaz parçası olan ve o olmadan donanımın çalışamadığı işletim sistemi donanımla birlikte maddi duran varlık olarak kaydedilir: 255 Demirbaşlar 66.000 ₺ (büro donanımı). Donanımdan bağımsız kullanılabilen paket program maddi olmayan duran varlıktır: 260 Haklar 24.000 ₺ (TMS 38.4 ile aynı yaklaşım).',
        "1 Sıra No'lu MSUGT - 24 / 26 grupları",
    ),
    # düzey 2
    '0013': patch(
        "TMS 38'e göre raporlama yapan bir işletme 1 Nisan'da 240.000 ₺'ye bir üretim planlama yazılımı satın almıştır. Yazılım, işletmenin sistemlerine uyarlanarak 1 Temmuz'da yönetimin amaçladığı biçimde kullanılabilir hâle gelmiş ve aynı tarihte kullanılmaya başlanmıştır. Yararlı ömrü 5 yıl, kalıntı değeri sıfırdır ve doğrusal itfa uygulanmaktadır.\n\nBuna göre cari yılda ayrılacak itfa payı kaç ₺'dir?",
        {
            'A': '36.000',
            'B': '48.000',
            'C': '24.000',
            'D': '30.000',
            'E': '40.000',
        },
        'C',
        'TMS 38.97: sınırlı yararlı ömürlü bir varlığın itfası, varlık kullanıma hazır olduğunda (yönetimin amaçladığı biçimde çalışabilir duruma geldiğinde) başlar; satın alma tarihi belirleyici değildir. Yıllık itfa 240.000 / 5 = 48.000 ₺; 1 Temmuz–31 Aralık için 48.000 × 6/12 = 24.000 ₺.',
        'VUK md. 326; TMS 38 (itfanın başlangıcı)',
    ),
    # düzey 2
    '0014': patch(
        "Kiracı işletme, sekiz yıllığına kiraladığı ofis katında şu harcamaları yapmıştır: kira süresi sonunda mal sahibine kalacak bir asansör tesisatı 80.000 ₺, taşınırken sökülüp götürülebilecek büro mobilyası 30.000 ₺, olağan bakım niteliğindeki boya-badana 6.000 ₺ ve binaya kalıcı olarak eklenen bölme duvarlar 24.000 ₺. KDV ihmal edilecektir.\n\nBuna göre '264 Özel Maliyetler' hesabına kaydedilecek toplam tutar kaç ₺'dir?",
        {
            'A': '110.000',
            'B': '134.000',
            'C': '80.000',
            'D': '104.000',
            'E': '24.000',
        },
        'D',
        "Özel maliyet, kiralanan gayrimenkule kiracının yaptığı ve kira süresi sonunda mal sahibine kalan kalıcı nitelikteki harcamalardır: asansör tesisatı ve bölme duvarlar, 80.000 + 24.000 = 104.000 ₺. Sökülüp götürülebilen mobilya 255 Demirbaşlar'da izlenir; olağan bakım niteliğindeki boya-badana dönem gideridir.",
        "1 Sıra No'lu MSUGT - 264; VUK md. 272",
    ),
    # düzey 2
    '0015': patch(
        "'262 Kuruluş ve Örgütlenme Giderleri' ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': "İşletme bu giderleri aktifleştirmeyi seçerse 262'de izler ve genellikle 5 yılda eşit tutarlarla itfa eder; aktifleştirmezse doğrudan dönem gideri yazabilir.",
            'B': 'Kuruluş ve örgütlenme giderleri aktifleştirilemez; yapıldıkları dönemde tamamı istisnasız biçimde zorunlu olarak dönem gideri yazılarak sonuç hesaplarına aktarılır.',
            'C': 'Kuruluş ve örgütlenme giderleri, işletmeye üstünlük sağladığından 261 Şerefiye hesabında izlenir ve itfa edilmeyip her yıl değer düşüklüğü testine tabi tutulur.',
            'D': 'Kuruluş ve örgütlenme giderleri, bir yıl içinde paraya çevrilecek dönen varlık kabul edilerek stoklar grubunda gösterilir ve satış anında maliyet yazılır.',
            'E': 'Kuruluş ve örgütlenme giderleri aktifleştirildiğinde, faaliyet koşullarına bağlı olmaksızın 10 yıla yayılarak eşit tutarlarla itfa edilir.',
        },
        'A',
        "Kuruluş ve örgütlenme giderlerinin aktifleştirilmesi **ihtiyaridir**: işletme aktifleştirirse **262**'de izleyip genellikle **5 yılda** eşit tutarlarla itfa eder; dilerse doğrudan dönem gideri de yazabilir.",
        "VUK md. 282/326; 1 Sıra No'lu MSUGT - 262",
    ),
    # düzey 3
    '0016': patch(
        'Maddi olmayan duran varlıklarla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Maddi olmayan duran varlıkların fiziki bir varlığı yoktur; bir hak veya üstünlük sağlarlar.\n\nII. İşletmenin kendi bünyesinde yarattığı (içsel) şerefiye de 261 Şerefiye hesabında aktifleştirilir.\n\nIII. Özel maliyetler (264), ilke olarak kira süresi boyunca itfa edilir.',
        {
            'A': 'II ve III',
            'B': 'I ve III',
            'C': 'I, II ve III',
            'D': 'Yalnız I',
            'E': 'I ve II',
        },
        'B',
        "Yanlış ifade **II**'dir. **İçsel (işletme içinde yaratılan) şerefiye** muhasebeleştirilmez; yalnızca bir işletme devralınırken **bir bedel ödenerek edinilen (satın alınan) şerefiye** 261 Şerefiye hesabında aktifleştirilir. **I** MODV'lerin fiziki varlığı yoktur, bir hak/üstünlük sağlar; **III** özel maliyetler (264) kira süresi boyunca (süre belli değilse 5 yılda) itfa edilir. Doğru cevap **I ve III**.",
        "1 Sıra No'lu MSUGT - 26 grubu; VUK md. 326-327; TMS 38",
    ),
    # düzey 3
    '0017': patch(
        'İşletme altı yıllığına kiraladığı mağazaya 180.000 ₺ özel maliyet harcaması yapmış ve üç yıl boyunca kira süresine göre itfa etmiştir. Dördüncü yılın başında mağaza tahliye edilmiştir. Buna göre tahliye kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '689 Diğer Olağandışı Gider ve Zararlar hesabı 180.000 ₺ borçlandırılır',
            'B': '264 Özel Maliyetler hesabı 90.000 ₺ alacaklandırılır',
            'C': '268 Birikmiş Amortismanlar hesabı 90.000 ₺ borçlandırılır',
            'D': '689 Diğer Olağandışı Gider ve Zararlar hesabı 90.000 ₺ borçlandırılır',
            'E': '770 Genel Yönetim Giderleri hesabı 90.000 ₺ borçlandırılır',
        },
        'D',
        'Üç yılda 90.000 ₺ itfa edilmiştir. Kayıt: 268 (borç) 90.000 + **689 (borç) 90.000** / 264 (alacak) 180.000. İtfa edilmemiş kalan tahliyeyle gider yazılır.',
        'VUK m. 327; THP 264, 268, 689',
    ),
    # düzey 3
    '0018': patch(
        "İşletme bir başka işletmeyi 260.000 ₺'ye banka havalesiyle satın almıştır. Devralınan işletmenin bilançosu şöyledir: Kasa 40.000 ₺, Alacak Senetleri 60.000 ₺, Ticari Mallar 150.000 ₺, Demirbaşlar 200.000 ₺, Birikmiş Amortismanlar 80.000 ₺, Satıcılar 70.000 ₺, Banka Kredileri 100.000 ₺. Kayıtlı değerlerin gerçeğe uygun olduğu varsayılmaktadır. Buna göre devir kaydında 261 Şerefiye hesabı kaç ₺ borçlandırılır?",
        {
            'A': '200.000 ₺',
            'B': '80.000 ₺',
            'C': '60.000 ₺',
            'D': '260.000 ₺',
            'E': '160.000 ₺',
        },
        'C',
        'Net varlık: 40.000 + 60.000 + 150.000 + 200.000 − 80.000 − 70.000 − 100.000 = 200.000 ₺. Şerefiye 260.000 − 200.000 = **60.000 ₺**. Birikmiş amortisman düzenleyici hesap olduğundan net varlıktan düşülür.',
        'THP 261; işletme devri',
    ),
    # düzey 2
    '0019': patch(
        'Maddi olmayan duran varlıklarla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Özel maliyet bedelleri kira süresi içinde itfa edilir.\n\nII. İşletme içinde yaratılan marka aktifleştirilir.\n\nIII. İşletme devralınırken ödenen şerefiye 262 hesabında izlenir.',
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'Yalnız III',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'D',
        'Yalnız I doğrudur. II yanlıştır: işletme içinde yaratılan marka, maliyeti güvenilir biçimde ayrıştırılamadığı için **aktifleştirilmez**. III yanlıştır: şerefiye **261 Şerefiye** hesabında izlenir; 262 kuruluş ve örgütlenme giderleri içindir.',
        'VUK m. 327; THP 261, 264',
    ),
    # düzey 2
    '0020': patch(
        'Bir işletme kiraladığı gayrimenkule yaptığı özel maliyet harcamalarını muhasebeleştirmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kira süresi dolmadan tahliyede kalan tutarın itfasına devam edilir',
            'B': 'Harcamalar 264 Özel Maliyetler hesabında izlenir',
            'C': "İtfa payları 268 Birikmiş Amortismanlar'da birikir",
            'D': 'Bedel kira süresi içinde eşit olarak itfa edilir',
            'E': 'Tahliyede itfa edilmemiş kısım gider yazılır',
        },
        'A',
        'Kira süresi dolmadan tahliye edildiğinde işletme artık o yeri kullanmadığından **itfa edilmemiş kalan tutar tahliye yılında gider** yazılır; itfaya devam edilmez.',
        'VUK m. 327; THP 264, 268, 689',
    ),
    # düzey 2
    '0021': patch(
        "Aşağıdaki hesaplardan hangisi '26 Maddi Olmayan Duran Varlıklar' grubunda yer almaz?",
        {
            'A': '264 Özel Maliyetler',
            'B': '263 Araştırma ve Geliştirme Giderleri',
            'C': '260 Haklar',
            'D': '253 Tesis, Makine ve Cihazlar',
            'E': '261 Şerefiye',
        },
        'D',
        "**253 Tesis, Makine ve Cihazlar**, fiziki bir varlık olduğundan '25 Maddi Duran Varlıklar' grubundadır. Diğerleri (260, 261, 263, 264) '26 Maddi Olmayan Duran Varlıklar' grubunda yer alır.",
        "1 Sıra No'lu MSUGT - 26 grubu",
    ),
    # düzey 2
    '0022': patch(
        "İşletme, kendi markasının tanınırlığını artırmak için 400.000 ₺ reklam harcaması yapmış ve marka değerinin yükseldiğini güvenilir bir değerleme raporuyla ileri sürmüştür. TMS 38'e göre nasıl işlem yapılır?",
        {
            'A': 'Aktif piyasa bulunup bulunmadığı araştırılmadan, değerleme raporundaki tahmini marka artışının tamamı diğer kapsamlı gelire ve özkaynağa alınır.',
            'B': 'İşletme içi yaratılan marka aktifleştirilmez; reklam harcaması gerçekleştiğinde gider yazılır.',
            'C': 'Tutar 261 Şerefiye hesabında süresiz taşınır.',
            'D': '400.000 ₺ 260 Haklar hesabına aktifleştirilir.',
            'E': 'Marka değeri her dönem satış hasılatına eklenir.',
        },
        'B',
        'İşletme içi yaratılan markalar, bunlara ilişkin harcamalar işletmenin bütününü geliştirme harcamalarından ayrıştırılamadığı için maddi olmayan duran varlık olarak muhasebeleştirilmez. Reklam harcaması da hizmet alındığında **gider** yazılır.',
        'TMS 38, par. 63-64 ve 69(c)',
    ),
    # düzey 2
    '0023': patch(
        "'268 Birikmiş Amortismanlar (-)' hesabının niteliği ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Maddi olmayan duran varlıkların itfa paylarını izleyen, aktifi düzenleyici (kontr aktif) bir hesaptır; alacak kalanı verir.',
            'B': 'İşletmenin kasasındaki nakit mevcudunu izleyen, tahsilatla artıp ödemeyle azalan ve borç kalanı veren bir hazır değerler (aktif) hesabıdır.',
            'C': 'Dönem içinde elde edilen faiz, kira ve benzeri olağan gelirleri toplayan, alacak kalanı veren bir gelir hesabıdır.',
            'D': 'Uzun vadeli yabancı kaynaklar grubunda yer alan, ileride ödenecek bir yükümlülüğü gösteren ve borç kalanı veren bir pasif hesaptır.',
            'E': 'Üretim giderlerini dönem boyunca toplayarak mamul maliyetine aktaran, dönem sonunda kapanan ve borç kalanı veren bir maliyet hesabıdır.',
        },
        'A',
        "**268 Birikmiş Amortismanlar (-)**, maddi olmayan duran varlıklar için ayrılan **itfa paylarını** biriktirir; aktifi düzenleyici bir hesaptır, **alacak kalanı** verir ve MODV'lerden (-) düşülerek net değeri gösterir.",
        "1 Sıra No'lu MSUGT - 268",
    ),
    # düzey 2
    '0024': patch(
        "'264 Özel Maliyetler' hesabında izlenen harcamalar hangi süre içinde itfa edilir?",
        {
            'A': 'Kiralanan varlık işletmenin öz mülkü olmadığından itfaya tabi tutulmaz',
            'B': 'Kira süresine bakılmaksızın 10 yıla yayılarak eşit tutarlarla itfa edilir',
            'C': 'Kira süresi boyunca eşit yüzdelerle; kira süresi belli değilse 5 yılda eşit tutarlarla',
            'D': 'Kira süresi ve sözleşme koşulları ne olursa olsun 5 yılda eşit tutarlarla itfa edilir',
            'E': 'Harcamanın yapıldığı ilk yıl içinde bir defada tamamı gider yazılarak sonuç hesaplarına aktarılır',
        },
        'C',
        'Özel maliyetler, kiralanan varlığın **kira süresi boyunca eşit yüzdelerle** itfa edilir; kira süresi belli değilse **5 yılda** eşit tutarlarla itfa edilir (VUK md. 327).',
        'VUK md. 327 (özel maliyet itfası)',
    ),
    # düzey 2
    '0025': patch(
        "İşletme, satın aldığı benzersiz bir markayı dönem sonunda bağımsız değerleme raporundaki gerçeğe uygun değerine yükseltmek istemektedir. Marka için aktif piyasa bulunmamaktadır. TMS 38'e göre doğru işlem hangisidir?",
        {
            'A': 'Marka finansal tablo dışı bırakılır.',
            'B': 'Artış 261 Şerefiye hesabına aktarılır.',
            'C': 'Bağımsız değerleme raporu gerçeğe uygun değeri tek başına kanıtladığından, aktif piyasa bulunmasa bile artış doğrudan satış geliri olarak muhasebeleştirilir.',
            'D': 'Marka her yıl zorunlu olarak rayiç değere yükseltilir.',
            'E': 'Aktif piyasa bulunmadığından yeniden değerleme modeli uygulanamaz; marka maliyet modelinde izlenir.',
        },
        'E',
        "TMS 38'de yeniden değerleme için gerçeğe uygun değerin **aktif bir piyasa** referans alınarak ölçülmesi gerekir. Benzersiz marka ve patentler için aktif piyasa bulunması olağan değildir; yalnız değerleme raporu yeniden değerleme modeli için yeterli değildir.",
        'TMS 38, par. 75 ve 78',
    ),
    # düzey 2
    '0026': patch(
        "İşletme, kira süresi belirli olmayan bir sözleşme kapsamında kiraladığı yere 45.000 ₺'lik özel maliyet niteliğinde harcama yapmıştır. VUK'a göre bu harcama için yıllık itfa payı kaç ₺'dir?",
        {
            'A': '15.000',
            'B': '4.500',
            'C': '45.000',
            'D': '9.000',
            'E': '22.500',
        },
        'D',
        'Kira süresi belli değilse özel maliyet **5 yılda** eşit tutarlarla itfa edilir (VUK md. 327): 45.000 ÷ 5 = **9.000 ₺/yıl**.',
        'VUK md. 327 (kira süresi belli değilse 5 yıl)',
    ),
    # düzey 2
    '0027': patch(
        'İşletmenin, kendi mülkiyetindeki (kiralanmamış) binasına yaptığı kalıcı değer artırıcı harcama nasıl muhasebeleştirilir?',
        {
            'A': 'Harcama işletmeye bir hak sağladığından 260 Haklar hesabına kaydedilir ve yasal koruma süresi boyunca eşit tutarlarla itfa edilir.',
            'B': "Değer artışı işletmeye üstünlük sağladığından 261 Şerefiye hesabına kaydedilir ve VUK'a göre 5 yılda eşit tutarlarla itfa edilir.",
            'C': 'İlgili maddi duran varlık hesabına (252 Binalar) eklenir; 264 Özel Maliyetler kiralanan varlıklar için kullanılır.',
            'D': "Harcamanın tutarı ve niteliği ne olursa olsun tamamı, yapıldığı dönemde doğrudan 770 Genel Yönetim Giderleri'ne yazılır.",
            'E': 'Bina işletmenin kendi mülkü olsa dahi yapılan değer artırıcı harcama 264 Özel Maliyetler hesabına kaydedilir ve kira süresince itfa edilir.',
        },
        'C',
        '**264 Özel Maliyetler** yalnızca **kiralanan** varlıklara yapılan harcamalar içindir. İşletmenin **kendi** binasına yaptığı değer artırıcı harcama ilgili MDV hesabına (**252 Binalar**) eklenir (aktifleştirilir).',
        "VUK md. 272; 1 Sıra No'lu MSUGT - 264 / 252",
    ),
    # düzey 2
    '0028': patch(
        "İşletme, aktif piyasası bulunan üretim kotalarında yeniden değerleme modelini uygulamaktadır. Aynı sınıftaki yalnız değeri yükselen iki kotayı yeniden değerlemek istemektedir. TMS 38'e göre doğru işlem hangisidir?",
        {
            'A': 'Seçici uygulama yapılamaz; aktif piyasası bulunan ilgili sınıftaki varlıklar aynı yöntemle ve eş zamanlı değerlenir.',
            'B': 'Bütün kotalar stok hesabına aktarılır.',
            'C': 'Maddi olmayan duran varlıklar benzersiz kabul edildiğinden aktif piyasa bulunsa bile yeniden değerlenemez; sınıf maliyet modelinde tutulur.',
            'D': 'Değeri yükselen kotalar yeniden değerlenir, diğerleri maliyette kalır.',
            'E': 'Yeniden değerleme şerefiyeye özgüdür.',
        },
        'A',
        'Yeniden değerleme modeli aktif piyasa koşuluyla uygulanabilir. Bir sınıfın içinden yalnız değer artışı olan kalemleri seçmek farklı tarihlere ait tutarların birlikte sunulmasına yol açacağından, ilgili sınıf **aynı yöntemle ve eş zamanlı** yeniden değerlenir.',
        'TMS 38, par. 72-75',
    ),
    # düzey 2
    '0029': patch(
        "TMS 38'e göre raporlama yapan işletme, dört yıl kullanmayı planladığı bir yayın lisansını 500.000 ₺'ye satın almıştır. Bağımsız bir yayın kuruluşu, dört yılın sonunda lisansı 100.000 ₺'ye satın almayı yazılı olarak taahhüt etmiştir. İşletme doğrusal itfa yöntemini uygulamaktadır.\n\nBuna göre lisans için ayrılacak yıllık itfa payı kaç ₺'dir?",
        {
            'A': '75.000',
            'B': '80.000',
            'C': '62.500',
            'D': '50.000',
            'E': '100.000',
        },
        'E',
        'TMS 38.100: sınırlı ömürlü maddi olmayan varlığın kalıntı değeri kural olarak sıfırdır; ancak yararlı ömür sonunda varlığı satın almak için üçüncü bir tarafın taahhüdü varsa kalıntı değer dikkate alınır. Yıllık itfa = (500.000 − 100.000) / 4 = 100.000 ₺.',
        'VUK md. 326; TMS 38',
    ),
    # düzey 3
    '0030': patch(
        'Aşağıdakilerden hangileri maddi olmayan duran varlık niteliğindedir?\n\nI. Patent\n\nII. Satın alınan şerefiye\n\nIII. İşletmenin kamyonu',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'B',
        '**Patent (I)** ve **satın alınan şerefiye (II)** fiziki varlığı olmayan haklar/üstünlükler olduğundan maddi olmayan duran varlıktır. **Kamyon (III)** ise fiziki bir varlıktır → 254 Taşıtlar (MDV). Doğru cevap **I ve II**.',
        "1 Sıra No'lu MSUGT - 25/26 ayrımı",
    ),
    # düzey 2
    '0031': patch(
        "İşletmenin sahip olduğu bir hakkın (260 Haklar) net defter değerinin üzerinde bir bedelle satılması sonucu doğan kâr, Tekdüzen Hesap Planı'nda hangi hesaba kaydedilir?",
        {
            'A': '689 Diğer Olağandışı Gider ve Zararlar',
            'B': '600 Yurt İçi Satışlar',
            'C': '649 Diğer Olağan Gelir ve Kârlar',
            'D': '679 Diğer Olağandışı Gelir ve Kârlar',
            'E': '602 Diğer Gelirler',
        },
        'D',
        "Maddi olmayan duran varlık (hak) satış **kârı**, maddi duran varlık satışında olduğu gibi **679 Diğer Olağandışı Gelir ve Kârlar** hesabına alacak kaydedilir (satış zararı ise 689'a).",
        "1 Sıra No'lu MSUGT - 679",
    ),
    # düzey 2
    '0032': patch(
        "İşletme, kendi pazarlama faaliyetleriyle oluşturduğu müşteri listesinin gelecekte gelir sağlayacağını öngörmektedir. Liste sözleşmeye veya devredilebilir bir hakka dayanmamaktadır. TMS 38'e göre nasıl işlem yapılır?",
        {
            'A': 'Yönetim kurulu gelecekteki müşteri gelirlerini güvenilir bir bütçeyle tahmin ettiği anda, ayrılabilirlik veya kontrol koşulu aranmaksızın bu tahmini tutarla aktifleştirilir.',
            'B': 'İşletme içi yaratılan müşteri listesi maddi olmayan duran varlık olarak muhasebeleştirilmez.',
            'C': 'Liste 261 Şerefiye hesabında aktifleştirilir.',
            'D': 'Tahmini gelirlerin tamamı varlık kaydedilir.',
            'E': 'Müşteri sayısı kadar nominal değerle kaydedilir.',
        },
        'B',
        'İşletme içi yaratılan müşteri listeleriyle ilgili harcamalar, işin bütününü geliştiren harcamalardan ayrıştırılamadığından TMS 38 kapsamında maddi olmayan duran varlık olarak muhasebeleştirilmez; ilgili harcamalar gider yazılır.',
        'TMS 38, par. 63-64',
    ),
    # düzey 3
    '0033': patch(
        "İşletme bir yazılım lisansı için 100.000 ₺ liste fiyatı üzerinden 10.000 ₺ ticari iskonto almış; lisansı kullanıma hazır hâle getiren hukuki danışmanlık için 5.000 ₺, çalışma testi için 3.000 ₺ ve kullanıcı eğitimi için 8.000 ₺ ödemiştir. TMS 38'e göre yazılımın maliyeti kaç ₺'dir?",
        {
            'A': '98.000',
            'B': '88.000',
            'C': '116.000',
            'D': '90.000',
            'E': '86.000',
        },
        'A',
        'Maliyet; iskontolu satın alma fiyatı 90.000 ₺ ile kullanıma hazırlamaya doğrudan bağlı danışmanlık 5.000 ₺ ve test 3.000 ₺ toplamıdır: **98.000 ₺**. Kullanıcı eğitimi varlığı çalışabilir duruma getiren maliyet değildir ve gider yazılır.',
        'TMS 38, par. 27-29',
    ),
    # düzey 2
    '0034': patch(
        "İşletme, çalışanlarına verdiği yoğun eğitim sayesinde gelecekte önemli ekonomik fayda beklemektedir; ancak çalışanların işletmede kalmasını veya becerilerini yalnız işletme yararına kullanmasını sağlayan bir hakkı yoktur. TMS 38'e göre eğitim harcaması nasıl muhasebeleştirilir?",
        {
            'A': 'Eğitim çalışanların bilgi düzeyini artırdığı için hukuki kontrole bakılmadan varlıklaştırılır, çalışan ayrılırsa gider yazılır',
            'B': '261 Şerefiye hesabında',
            'C': 'Gelecekteki yararlar üzerinde yeterli kontrol bulunmadığından gider olarak',
            'D': '260 Haklar hesabında süresiz olarak',
            'E': 'Çalışan sayısına göre maddi duran varlık olarak',
        },
        'C',
        'İşletme, çalışanların becerilerinden yarar beklese de genellikle çalışanların işletmede kalmasını ve bu yararlara başkalarının erişimini kısıtlayamaz. Bu nedenle kontrol ölçütü sağlanmaz; **eğitim harcaması gider** olarak muhasebeleştirilir.',
        'TMS 38, par. 13-15 ve 69(b)',
    ),
    # düzey 2
    '0035': patch(
        'İşletme, aktifindeki bir marka (260 Haklar) için üretimle ilgili olarak dönem sonunda 25.000 ₺ itfa payı ayırmıştır. Bu işlemin dönem sonuçlarına etkisi ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ayrılan itfa payı gider yazılmayıp 261 Şerefiye hesabına 25.000 ₺ borç kaydedilerek varlığın maliyet bedeline eklenir ve izleyen dönemlere aktarılır.',
            'B': 'Gider yazılmadan 260 Haklar hesabı 25.000 ₺ tutarında doğrudan alacaklandırılarak varlığın kayıtlı değeri azaltılır; düzenleyici hesap çalıştırılmaz.',
            'C': 'İşlem bir satış gibi değerlendirilerek 391 Hesaplanan KDV hesabına 25.000 ₺ eklenir ve bu tutar dönem sonunda vergi dairesine beyan edilerek ödenir.',
            'D': 'İtfa payı bir gelir hesabı sayıldığından 649 Diğer Olağan Gelir ve Kârlar hesabına 25.000 ₺ alacak yazılır, 260 Haklar borçlandırılır ve dönem kârı artar.',
            'E': 'İlgili gider hesabına (ör. 730 Genel Üretim Giderleri) 25.000 ₺ gider yazılır, 268 Birikmiş Amortismanlar 25.000 ₺ alacaklandırılır; dönem kârı azalır.',
        },
        'E',
        'İtfa payı giderdir → gider yeri üretimle ilgiliyse **730 Genel Üretim Giderleri (borç) 25.000**; düzenleyici hesap **268 Birikmiş Amortismanlar (alacak) 25.000**. Gider yazıldığından dönem kârı **azalır**; varlık doğrudan azaltılmaz.',
        "1 Sıra No'lu MSUGT - 268 / gider hesapları",
    ),
    # düzey 3
    '0036': patch(
        "İşletme sekiz yıllığına kiraladığı fabrika binasına, kira süresi sonunda mal sahibine kalacak 240.000 ₺ tutarında kalıcı tesisat harcaması yapmış ve 264 Özel Maliyetler hesabında aktifleştirmiştir. Buna göre yıllık itfa payı kaç ₺'dir?",
        {
            'A': '48.000 ₺',
            'B': '30.000 ₺',
            'C': '60.000 ₺',
            'D': '240.000 ₺',
            'E': '24.000 ₺',
        },
        'B',
        "VUK m. 327 uyarınca özel maliyet bedelleri **kira süresi** içinde eşit olarak itfa edilir: 240.000 / 8 = **30.000 ₺**. İtfa 268 Birikmiş Amortismanlar'da birikir.",
        'VUK m. 327; THP 264, 268',
    ),
    # düzey 3
    '0037': patch(
        'Kayıtlı değeri 120.000 ₺, birikmiş itfa payı 72.000 ₺ olan bir işletme hakkı 70.000 ₺ + %20 KDV bedelle peşin satılmıştır. Buna göre satış kaydında aşağıdakilerden hangisi yer almaz?',
        {
            'A': '257 Birikmiş Amortismanlar hesabı 72.000 ₺ borçlandırılır',
            'B': '260 Haklar hesabı 120.000 ₺ alacaklandırılır',
            'C': '100 Kasa hesabı 84.000 ₺ borçlandırılır',
            'D': '268 Birikmiş Amortismanlar hesabı 72.000 ₺ borçlandırılır',
            'E': '679 Diğer Olağandışı Gelir ve Kârlar hesabı 22.000 ₺ alacaklandırılır',
        },
        'A',
        "Kayıt: 100 (borç) 84.000 + 268 (borç) 72.000 / 260 (alacak) 120.000 + 391 (alacak) 14.000 + 679 (alacak) 22.000. Maddi olmayan duran varlıkların itfası **268**'de birikir; 257 maddi duran varlıklara aittir.",
        'THP 260, 268, 100, 391, 679',
    ),
    # düzey 3
    '0038': patch(
        "İşletme faaliyetini genişletmek için başka bir işletmeyi bütün varlık ve borçlarıyla 750.000 ₺ ödeyerek devralmıştır. Devralınan işletmenin varlıklarının toplam değeri 900.000 ₺, borçlarının toplamı 300.000 ₺'dir. Buna göre devralma kaydında 261 Şerefiye hesabına yazılacak tutar kaç ₺'dir?",
        {
            'A': '600.000 ₺',
            'B': '450.000 ₺',
            'C': '150.000 ₺',
            'D': '900.000 ₺',
            'E': '750.000 ₺',
        },
        'C',
        'Net varlık 900.000 − 300.000 = 600.000 ₺. Ödenen bedel net varlığı 150.000 ₺ aştığından fark **şerefiyedir** (261, borç).',
        'THP 261 Şerefiye',
    ),
    # düzey 2
    '0039': patch(
        'İşletme muhasebe biriminde kullanmak üzere bir yazılımın üç yıllık kullanım lisansını 90.000 ₺ + %20 KDV bedelle banka havalesiyle satın almıştır. Buna göre alış kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '770 Genel Yönetim Giderleri hesabı 90.000 ₺ borçlandırılır',
            'B': '260 Haklar hesabı 108.000 ₺ borçlandırılır',
            'C': '264 Özel Maliyetler hesabı 90.000 ₺ borçlandırılır',
            'D': '260 Haklar hesabı 90.000 ₺ borçlandırılır',
            'E': '255 Demirbaşlar hesabı 90.000 ₺ borçlandırılır',
        },
        'D',
        'Satın alınan yazılım kullanım hakkı bir haktır: **260 Haklar (borç) 90.000** + 191 (borç) 18.000 / 102 (alacak) 108.000. KDV maliyete eklenmez.',
        'THP 260, 191',
    ),
    # düzey 3
    '0040': patch(
        "İşletmenin kiraladığı binaya yaptığı özel maliyetin yıllık itfa payı 50.000 ₺'dir. Binanın %70'i üretimde, %30'u yönetim işlerinde kullanılmaktadır (7/A seçeneği). Buna göre itfa kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '257 Birikmiş Amortismanlar hesabı 50.000 ₺ alacaklandırılır',
            'B': '730 Genel Üretim Giderleri hesabı 50.000 ₺ borçlandırılır',
            'C': '770 Genel Yönetim Giderleri hesabı 35.000 ₺ borçlandırılır',
            'D': '268 Birikmiş Amortismanlar hesabı 35.000 ₺ alacaklandırılır',
            'E': '730 Genel Üretim Giderleri hesabı 35.000 ₺ borçlandırılır',
        },
        'E',
        "Kayıt: **730 (borç) 35.000** + 770 (borç) 15.000 / 268 (alacak) 50.000. İtfa payı kullanım yerine göre dağıtılır; karşılık hesabı 268'dir.",
        'THP 264, 268, 730, 770',
    ),
    # düzey 2
    '0041': patch(
        "Tekdüzen Hesap Planı'nda '261 Şerefiye' hesabı ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İşletmenin kendi faaliyetleriyle içsel olarak oluşturduğu markanın tahmini değerini, her dönem sonunda yeniden hesaplayarak bulunan tutarla bilançoya alır ve orada izler.',
            'B': 'Ortakların işletmeye getirmeyi taahhüt ettikleri ancak henüz nakden ya da ayni olarak ödemedikleri sermaye tutarlarını ayrıntılı olarak izler.',
            'C': 'İşletmenin dönem içinde satmak amacıyla elde tuttuğu ticari mallar ile ürettiği mamullerin maliyet bedellerini, stoklar grubu altında ayrıntılı olarak izler.',
            'D': 'Bir işletmenin devralınması sırasında, katlanılan maliyet ile devralınan net varlıkların gerçeğe uygun (rayiç) değeri arasındaki olumlu farkı (satın alınan şerefiye) izler.',
            'E': 'İşletmenin bankalar nezdinde açtırdığı vadeli ve vadesiz mevduat hesaplarındaki nakit mevcudunu ayrıntılı olarak izler.',
        },
        'D',
        '**261 Şerefiye (peştamallık)**, bir işletme devralınırken **ödenen bedel ile devralınan net varlıkların rayiç değeri arasındaki olumlu farkı** izler. Yalnızca bir bedel ödenerek **satın alınan** şerefiye kaydedilir.',
        "1 Sıra No'lu MSUGT - 261 Şerefiye; VUK md. 282",
    ),
    # düzey 2
    '0042': patch(
        "İşletme beş yıl kullanma hakkı veren bir yazılım lisansını 250.000 ₺'ye almış ve iki yıl boyunca doğrusal yöntemle itfa etmiştir. Üçüncü yılın başında lisansı veren firma faaliyetini durdurmuş, lisans artık kullanılamaz ve devredilemez hâle gelmiştir. İşletme varlığı kayıtlardan çıkarmaya karar vermiştir.\n\nBu işleme ilişkin kayıt (hesap kodlarıyla) aşağıdakilerden hangisidir?",
        {
            'A': '689 250.000 ₺ borç / 260 250.000 ₺ alacak',
            'B': '770 150.000 ₺ borç / 268 150.000 ₺ alacak',
            'C': '268 150.000 ₺ borç / 260 150.000 ₺ alacak',
            'D': '260 250.000 ₺ borç / 268 100.000 ₺ ve 689 150.000 ₺ alacak',
            'E': '268 100.000 ₺ ve 689 150.000 ₺ borç / 260 250.000 ₺ alacak',
        },
        'E',
        "İki yıllık itfa 250.000 / 5 × 2 = 100.000 ₺ 268'de birikmiştir; kalan net değer 150.000 ₺'dir. Kullanılamaz hâle gelen hak kayıtlardan çıkarılırken birikmiş itfa kapatılır ve kalan değer olağandışı zarar yazılır: 268 100.000 ₺ ve 689 150.000 ₺ borç / 260 250.000 ₺ alacak.",
        "1 Sıra No'lu MSUGT - 264; VUK md. 272/327",
    ),
    # düzey 2
    '0043': patch(
        "7/A seçeneğini uygulayan işletmenin haklar hesabında üç varlık bulunmaktadır: üretimde kullanılan ve 10 yıl itfa edilen 300.000 ₺'lik patent, satış bölümünce kullanılan ve kalan sözleşme süresi 5 yıl olan 120.000 ₺'lik bayilik hakkı, yönetim biriminde kullanılan ve 3 yılda itfa edilen 60.000 ₺'lik yazılım lisansı. Varlıkların tamamı dönem başında aktifleştirilmiştir ve itfa doğrusal olarak yapılmaktadır.\n\nDönem sonu itfa kaydında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '730 Genel Üretim Giderleri hesabı 30.000 ₺ borçlandırılır',
            'B': '760 Pazarlama Satış ve Dağıtım Giderleri 20.000 ₺ borçlandırılır',
            'C': '770 Genel Yönetim Giderleri hesabı 30.000 ₺ borçlandırılır',
            'D': '257 Birikmiş Amortismanlar hesabı 74.000 ₺ alacaklandırılır',
            'E': '268 Birikmiş Amortismanlar hesabı 74.000 ₺ borçlandırılır',
        },
        'A',
        "İtfa payları: patent 300.000 / 10 = 30.000 ₺ (730), bayilik hakkı 120.000 / 5 = 24.000 ₺ (760), yazılım 60.000 / 3 = 20.000 ₺ (770). Kayıt: 730 30.000 ₺, 760 24.000 ₺ ve 770 20.000 ₺ borç / 268 Birikmiş Amortismanlar 74.000 ₺ alacak. Maddi olmayan varlıkların itfası 257'de değil 268'de birikir.",
        "1 Sıra No'lu MSUGT - 268 / gider hesapları",
    ),
    # düzey 2
    '0044': patch(
        "Bir işletmenin devralınması sırasında oluşan ve '261 Şerefiye' hesabına kaydedilen 150.000 ₺'lik şerefiye, VUK'a göre 5 yılda eşit tutarlarla itfa edilmektedir. Yıllık itfa payı kaç ₺'dir?",
        {
            'A': '50.000',
            'B': '150.000',
            'C': '30.000',
            'D': '15.000',
            'E': '75.000',
        },
        'C',
        "Şerefiye VUK'a göre 5 yılda eşit tutarlarla itfa edilebilir: 150.000 ÷ 5 = **30.000 ₺/yıl** (yıllık %20).",
        'VUK md. 326 (şerefiye 5 yılda itfa)',
    ),
    # düzey 2
    '0045': patch(
        "Yeni kurulan bir anonim şirket, aktifleştirmeyi seçtiği 50.000 ₺ kuruluş ve örgütlenme giderini VUK'a göre beş yılda eşit tutarlarla itfa etmektedir. Şirket aynı tarihte kalan koruma süresi altı yıl olan bir patenti 60.000 ₺'ye satın almış ve bu süre boyunca eşit tutarlarla itfa etmektedir. İki varlık da ilk yılın başında aktifleştirilmiştir.\n\nBuna göre üçüncü yılın sonunda bu iki varlığın net defter değerleri toplamı kaç ₺'dir?",
        {
            'A': '70.000',
            'B': '50.000',
            'C': '30.000',
            'D': '20.000',
            'E': '44.000',
        },
        'B',
        'Kuruluş gideri: yıllık 50.000 / 5 = 10.000 ₺; üç yıl sonunda kalan 50.000 − 30.000 = 20.000 ₺. Patent: yıllık 60.000 / 6 = 10.000 ₺; üç yıl sonunda kalan 60.000 − 30.000 = 30.000 ₺. Toplam net defter değeri 20.000 + 30.000 = 50.000 ₺.',
        "VUK md. 326; 1 Sıra No'lu MSUGT - 262",
    ),
    # düzey 2
    '0046': patch(
        "Bir proje için geçen yıl araştırma safhasında yapılan 80.000 ₺ harcama gider yazılmıştır. Bu yıl proje geliştirme ölçütlerini sağlamış ve başarı beklentisi yükselmiştir. TMS 38'e göre geçen yıl gider yazılan 80.000 ₺ için ne yapılır?",
        {
            'A': 'Geçmişte gider yazılan tutar sonradan varlık maliyetine geri alınamaz.',
            'B': 'Projenin geliştirme aşamasında başarılı olması geçmişteki araştırma harcamasının niteliğini değiştirir; tutar önce dönem geliri yazılıp ardından yeni varlığın maliyetine aktarılır.',
            'C': 'Yarısı aktifleştirilir, yarısı gider kalır.',
            'D': 'Tamamı bu yıl 263 hesabına aktarılır.',
            'E': 'Şerefiye hesabına alınır.',
        },
        'A',
        'Başlangıçta gider olarak muhasebeleştirilen maddi olmayan duran varlıkla ilgili harcama, sonraki bir tarihte ölçütler sağlansa bile varlık maliyetine **geri alınamaz**. Yalnız ölçütlerin sağlandığı tarihten sonraki uygun harcamalar aktifleştirilebilir.',
        'TMS 38, par. 65 ve 71',
    ),
    # düzey 2
    '0047': patch(
        "TMS 38'e göre raporlama yapan işletmenin 400.000 ₺'ye aldığı yayın lisansı on yıllıktır; ancak lisans önemli bir maliyete katlanmadan sınırsız sayıda yenilenebilmekte ve işletmenin yenileme niyeti ile imkânı bulunmaktadır. Yönetim varlığın nakit akışı sağlayacağı sürenin öngörülebilir bir sınırı olmadığını değerlendirmiştir. Dönem sonunda lisansın geri kazanılabilir tutarı 360.000 ₺ olarak hesaplanmıştır.\n\nBuna göre dönem sonu muhasebeleştirmeyle ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '40.000 ₺ itfa payı ayrılır; değer düşüklüğü testi yapılmaz',
            'B': 'Değer düşüklüğü testi belirti olmadıkça yapılmaz, itfa ayrılmaz',
            'C': 'İtfa ayrılmaz; değer kaybı olsa da kayıt yapılmaz',
            'D': 'İtfa ayrılmaz; 40.000 ₺ değer düşüklüğü zararı kaydedilir',
            'E': '40.000 ₺ itfa ve 40.000 ₺ değer düşüklüğü zararı kaydedilir',
        },
        'D',
        'TMS 38.88-90 ve 94-96: önemli maliyet olmadan yenilenebilen ve nakit akışı süresinin öngörülebilir sınırı olmayan lisansın yararlı ömrü sınırsızdır; itfa edilmez. TMS 38.108 ve TMS 36: sınırsız ömürlü varlık her yıl ve belirti olduğunda değer düşüklüğü testine tabidir. Defter değeri 400.000 ₺, geri kazanılabilir tutar 360.000 ₺ olduğundan 40.000 ₺ değer düşüklüğü zararı muhasebeleştirilir.',
        'TMS 38, par. 107-109; TMS 36',
    ),
    # düzey 2
    '0048': patch(
        'İşletme, kuruluş aşamasında katlandığı ve aktifleştirmeye karar verdiği 30.000 ₺ tutarındaki noter, tescil ve ilan giderlerini hangi hesaba kaydeder?',
        {
            'A': '263 Araştırma ve Geliştirme Giderleri',
            'B': '770 Genel Yönetim Giderleri',
            'C': '260 Haklar (İmtiyaz) Hesabı',
            'D': '261 Şerefiye (Peştamallık) Hesabı',
            'E': '262 Kuruluş ve Örgütlenme Giderleri',
        },
        'E',
        'İşletmenin kurulması için katlanılıp aktifleştirilen giderler **262 Kuruluş ve Örgütlenme Giderleri** hesabına kaydedilir ve genellikle 5 yılda itfa edilir.',
        "1 Sıra No'lu MSUGT - 262; VUK md. 326",
    ),
    # düzey 2
    '0049': patch(
        "Özel maliyet bedeli itfa edilirken, kiralama süresi dolmadan kiralanan yerin (gayrimenkulün) boşaltılması durumunda VUK'a göre ne yapılır?",
        {
            'A': 'Henüz itfa edilmemiş kalan tutar itfa durdurularak bilançoda beklemeye ve kalmaya devam eder.',
            'B': 'Henüz itfa edilmemiş kalan tutar, boşaltmanın gerçekleştiği yılda bir defada gider yazılır.',
            'C': 'Henüz itfa edilmemiş kalan tutar, boşaltmanın gerçekleştiği yılda dönem geliri olarak kaydedilir.',
            'D': 'Henüz itfa edilmemiş kalan tutar doğrudan sermayeye eklenir ve özkaynaklar içinde gösterilir.',
            'E': 'Henüz itfa edilmemiş kalan tutar 261 Şerefiye hesabına aktarılarak burada izlenmeye devam edilir.',
        },
        'B',
        "VUK md. 327'ye göre, kira süresi dolmadan kiralanan yer boşaltılırsa özel maliyetin **henüz itfa edilmemiş kalan kısmı, boşaltma yılında bir defada gider** yazılır.",
        'VUK md. 327 (erken boşaltma)',
    ),
    # düzey 2
    '0050': patch(
        "TMS 38'e göre maddi olmayan duran varlıkların itfasında hasılata dayalı yöntem kullanılmasıyla ilgili genel yaklaşım hangisidir?",
        {
            'A': 'Hasılat tüketim biçimini doğrudan yansıttığından sınırlı yararlı ömürlü maddi olmayan duran varlıklarda kullanılması gereken yöntemdir.',
            'B': 'Hasılat değiştikçe yararlı ömür sınırsız hâle gelir.',
            'C': 'Genellikle uygun olmadığı yönünde aksi ispat edilebilir bir karine vardır; sınırlı koşullarda kullanılabilir.',
            'D': 'Hasılata dayalı yöntem araştırma giderlerine özgüdür.',
            'E': 'Maliyet modelinde uygulanması gereken yöntemdir.',
        },
        'C',
        'Hasılat satış fiyatı, diğer girdiler ve enflasyon gibi varlığın ekonomik yararlarının tüketiminden bağımsız unsurlardan etkilenebilir. Bu nedenle hasılata dayalı itfanın uygun olmadığı yönünde **aksi ispat edilebilir bir karine** vardır; TMS 38 yalnız sınırlı istisnalar tanır.',
        'TMS 38, par. 98A-98C',
    ),
    # düzey 3
    '0051': patch(
        "Kayıtlı maliyeti 100.000 ₺, birikmiş itfası (268) 60.000 ₺ olan bir hak 55.000 ₺'ye satılmıştır. Bu satıştan doğan kâr veya zarar kaç ₺'dir?",
        {
            'A': '15.000 ₺ kâr',
            'B': '15.000 ₺ zarar',
            'C': '40.000 ₺ kâr',
            'D': '45.000 ₺ kâr',
            'E': '5.000 ₺ zarar',
        },
        'A',
        'Net defter değeri = 100.000 − 60.000 = 40.000 ₺. Satış 55.000 ₺ > NDD 40.000 ₺ → **15.000 ₺ kâr** (679 Diğer Olağandışı Gelir ve Kârlar).',
        "1 Sıra No'lu MSUGT - 260/268/679",
    ),
    # düzey 2
    '0052': patch(
        "İşletme, 5 yıllığına kiraladığı bir mağazaya 100.000 ₺'lik özel maliyet harcaması yapmış ve kira süresi boyunca eşit itfa etmektedir. 2 tam yıl itfa ayrıldıktan sonra '264 Özel Maliyetler'in net defter değeri kaç ₺'dir?",
        {
            'A': '20.000',
            'B': '80.000',
            'C': '60.000',
            'D': '100.000',
            'E': '40.000',
        },
        'C',
        'Yıllık itfa = 100.000 ÷ 5 = 20.000 ₺. 2 yıl → birikmiş = 40.000 ₺. Net defter değeri = 100.000 − 40.000 = **60.000 ₺**.',
        "VUK md. 327; 1 Sıra No'lu MSUGT - 264/268",
    ),
    # düzey 2
    '0053': patch(
        "TMS 38'e göre raporlama yapan bir taksi işletmesi, aktif bir piyasada alınıp satılan taksi plakalarını (lisans) yeniden değerleme modeliyle ölçmektedir. Daha önce hiç yeniden değerlenmemiş ve itfa edilmeyen bir plakanın defter değeri 800.000 ₺'dir. Dönem sonunda aktif piyasadaki fiyatı 1.000.000 ₺'dir.\n\nBuna göre yeniden değerlemeyle ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '200.000 ₺ artış dönemin kâr veya zararına gelir olarak yazılır',
            'B': '200.000 ₺ diğer kapsamlı gelire alınıp özkaynakta birikir',
            'C': 'Artış, varlık satılıncaya kadar kayıtlara alınmaz',
            'D': "Plakanın defter değeri 1.000.000 ₺'ye çıkarılmaz; artış dipnotta açıklanır",
            'E': '200.000 ₺ artış şerefiye hesabına eklenir',
        },
        'B',
        'TMS 38.75 ve 85: yeniden değerleme modelinde gerçeğe uygun değer aktif piyasaya göre belirlenir. Defter değerindeki artış, daha önce kâr veya zararda muhasebeleştirilmiş bir azalışı tersine çevirmiyorsa diğer kapsamlı gelirde muhasebeleştirilir ve özkaynakta yeniden değerleme artışı adı altında birikir: 1.000.000 − 800.000 = 200.000 ₺.',
        'TMS 38, par. 100',
    ),
    # düzey 3
    '0054': patch(
        'Aşağıdakilerden hangisi maddi olmayan duran varlıkların ortak özelliklerinden biri değildir?',
        {
            'A': 'Faydalı ömürleri boyunca genellikle itfaya (amortismana) tabi tutulurlar.',
            'B': 'Elle tutulup gözle görülebilen fiziki bir varlıkları yoktur; bir hak niteliği taşırlar.',
            'C': 'Bir yıldan uzun süre işletme faaliyetlerinde kullanılmak üzere elde tutulurlar.',
            'D': 'İşletmeye bir hak veya üstünlük sağlayarak ekonomik fayda edinilmesine imkân tanır.',
            'E': 'İşletmenin bir yıl içinde nakde çevirmek için elde tuttuğu dönen varlıklardır.',
        },
        'E',
        "Maddi olmayan duran varlıklar **duran (uzun vadeli) varlıklardır**; bir yıl içinde nakde çevrilmek üzere tutulan dönen varlık değildir. Diğer seçenekler MODV'lerin ortak özellikleridir.",
        "1 Sıra No'lu MSUGT - 26 grubu",
    ),
    # düzey 3
    '0055': patch(
        "Maliyeti 120.000 ₺, kalıntı değeri sıfır olan bir yazılımdan yararlı ömrü boyunca 240.000 işlem gerçekleştirilmesi beklenmektedir. Cari dönemde 60.000 işlem yapıldığına göre üretim birimleri yönteminde itfa payı kaç ₺'dir?",
        {
            'A': '120.000',
            'B': '20.000',
            'C': '60.000',
            'D': '30.000',
            'E': '15.000',
        },
        'D',
        "Cari dönemde toplam beklenen kullanımın 60.000/240.000 = **%25'i** gerçekleşmiştir. Üretim birimleri yöntemine göre itfa payı 120.000 × %25 = **30.000 ₺**dir.",
        'TMS 38, par. 97-98',
    ),
    # düzey 2
    '0056': patch(
        'Bir işletme, belediyenin açtığı ihaleyi kazanarak bir kamu otoparkını on yıl süreyle işletme hakkını (imtiyaz) 500.000 ₺ bedelle edinmiş ve bedeli banka havalesiyle ödemiştir. Hak, işletmeye on yıl boyunca otopark gelirlerini elde etme imkânı vermektedir. KDV ihmal edilecektir.\n\nHakkın edinilmesine ilişkin kayıtta aşağıdaki hesaplardan hangisinin kullanımı doğrudur?',
        {
            'A': '260 Haklar hesabı hak bedeli olan 500.000 ₺ borçlandırılır',
            'B': '264 Özel Maliyetler hesabı 500.000 ₺ borçlandırılır',
            'C': '280 Gelecek Yıllara Ait Giderler 500.000 ₺ borçlandırılır',
            'D': '770 Genel Yönetim Giderleri hesabı 500.000 ₺ borçlandırılır',
            'E': '262 Kuruluş ve Örgütlenme Giderleri 500.000 ₺ borçlandırılır',
        },
        'A',
        'Bedel ödenerek edinilen işletme (imtiyaz) hakkı, birden fazla dönem ekonomik yarar sağlayan maddi olmayan duran varlıktır ve 260 Haklar hesabında izlenir: 260 Haklar 500.000 ₺ borç / 102 Bankalar 500.000 ₺ alacak. Hak süresi boyunca (on yıl) itfa edilir.',
        "1 Sıra No'lu MSUGT - 260 Haklar",
    ),
    # düzey 3
    '0057': patch(
        "İşletme bir üretim teknolojisinin patentini 200.000 ₺'ye satın almıştır. Devir için 8.000 ₺ tescil harcı ve patent vekiline 12.000 ₺ ücret ödenmiş; ürünün tanıtımı için ayrıca 15.000 ₺ reklam harcaması yapılmıştır (KDV ihmal). Buna göre patentin maliyet bedeli kaç ₺'dir?",
        {
            'A': '208.000 ₺',
            'B': '220.000 ₺',
            'C': '205.000 ₺',
            'D': '200.000 ₺',
            'E': '176.000 ₺',
        },
        'B',
        'Hakkın edinilmesi için katlanılan tescil harcı ve vekil ücreti maliyete eklenir: 200.000 + 8.000 + 12.000 = **220.000 ₺** (260 Haklar). Reklam harcaması hakkı edinmeye değil satışa yöneliktir; gider yazılır.',
        'VUK m. 262, 270; THP 260',
    ),
    # düzey 2
    '0058': patch(
        'Bir işletmenin maddi olmayan duran varlıkları sınıflandırılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Aktifleştirilen kuruluş giderleri 262'de izlenir",
            'B': "Devralmadan doğan şerefiye 261'de izlenir",
            'C': "Kiralanan binaya yapılan kalıcı harcamalar 252 Binalar'da izlenir",
            'D': "Satın alınan patent 260 Haklar'da izlenir",
            'E': "Bu varlıkların itfası 268'de birikir",
        },
        'C',
        "Kiralanan (işletmenin mülkiyetinde olmayan) gayrimenkule yapılan kalıcı harcamalar **264 Özel Maliyetler**'de izlenir; 252 işletmenin kendi binaları içindir.",
        'THP 26 Maddi Olmayan Duran Varlıklar',
    ),
    # düzey 2
    '0059': patch(
        "Maddi olmayan duran varlıklarla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Maddi olmayan duran varlıkların itfası 257 Birikmiş Amortismanlar'a yazılır.\n\nII. Bir hakkın net değerinin üzerinde satılmasından doğan kâr 679'da izlenir.\n\nIII. Aktifleştirilen kuruluş giderleri 262 hesabında izlenir.",
        {
            'A': 'I ve II',
            'B': 'Yalnız III',
            'C': 'Yalnız II',
            'D': 'I ve III',
            'E': 'II ve III',
        },
        'E',
        "II ve III doğrudur. I yanlıştır: maddi olmayan duran varlıkların itfası **268 Birikmiş Amortismanlar**'da birikir.",
        'THP 262, 268, 679',
    ),
    # düzey 3
    '0060': patch(
        "TMS 38'e göre raporlama yapan işletme kendi kullanımı için bir yazılım geliştirmektedir. Ocak–Mart döneminde araştırma safhasında 90.000 ₺ harcanmıştır. 1 Nisan'da teknik uygulanabilirlik dâhil aktifleştirme koşullarının tamamı sağlanmış; Nisan–Eylül döneminde projede çalışan personelin ücretleri 240.000 ₺, dışarıdan alınan danışmanlık 60.000 ₺, genel yönetim giderlerinden ayrılan pay 30.000 ₺ ve kullanıcı eğitimi 10.000 ₺ olmuştur. Yazılım 1 Ekim'de kullanıma hazır hâle gelmiştir; yararlı ömrü 5 yıl, kalıntı değeri sıfırdır.\n\nBuna göre yazılımın yıl sonundaki net defter değeri kaç ₺'dir?",
        {
            'A': '300.000',
            'B': '240.000',
            'C': '313.500',
            'D': '370.500',
            'E': '285.000',
        },
        'E',
        'Araştırma harcamaları gider yazılır. Geliştirme safhasında doğrudan ilişkilendirilebilen personel ücretleri ve danışmanlık aktifleştirilir: 240.000 + 60.000 = 300.000 ₺; genel yönetim payı ve eğitim aktifleştirilmez. İtfa kullanıma hazır olunca başlar: 300.000 / 5 × 3/12 = 15.000 ₺. Net defter değeri 285.000 ₺.',
        'VUK m. 327; THP 264, 268',
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
    print(f"1 paket / {len(PATCHES)} soru ('Maddi Olmayan Duran Varliklar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
