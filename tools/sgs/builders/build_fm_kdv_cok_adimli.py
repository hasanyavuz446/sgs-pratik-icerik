#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KDV Muhasebesi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

FM cok adimli tur. 36 soru korundu; birbirini tekrarlayan 24 tek satirlik alis/satis kaydi, tek adimli mahsup ve tanim sorusu cikarildi. Yerine KDV'nin gomulu oldugu gercek sinav kalibinda 24 soru: surekli/aralikli envanterde satis ve alis iadeleri, satis sonrasi iskonto (611), alis iskontosu, verilen/alinan siparis avansiyla alis ve satis, ozel maliyetler (264/268; VUK 327) ilk yil itfasi ve erken tahliye, vade farki faturasi, ciro edilen senetle demirbas alimi, farkli oranli ve iadeli mahsup, KDV dahil tutardan matrah, indirilemeyen KDV (binek otomobil, KDVK 30/b), vergiyi doguran olay (KDVK 10). Kor ogrenci %24.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 3065 sayili KDVK m. 10, 20, 24, 29-30, 35 · VUK m. 262, 327 · Tekduzen Hesap Plani 190, 191, 391, 360, 159, 340, 264, 268, 611
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/finansal_muhasebe/kdv_muhasebesi.json"
STYLE_REF = 'SGS Finansal Muhasebe (çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "finmuh-kdv-gen-"


def patch(stem, options, answer, solution, ref='3065 sayili KDVK m. 29'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'İşletme, 40.000 ₺ tutarındaki ticari malı %20 KDV ile satın almış ve karşılığında satıcıya senet vermiştir. Bu alışın yevmiye kaydında aşağıdakilerden hangisi yer alır?',
        {
            'A': '153 Ticari Mallar (borç) 40.000 ve 191 İndirilecek KDV (borç) 8.000; 320 Satıcılar (alacak) 48.000',
            'B': '153 Ticari Mallar (borç) 40.000 ve 191 İndirilecek KDV (borç) 8.000; 321 Borç Senetleri (alacak) 48.000',
            'C': '153 Ticari Mallar (borç) 48.000; 321 Borç Senetleri (alacak) 48.000',
            'D': '153 Ticari Mallar (borç) 40.000 ve 391 Hesaplanan KDV (borç) 8.000; 321 Borç Senetleri (alacak) 48.000',
            'E': '153 Ticari Mallar (borç) 40.000 ve 191 İndirilecek KDV (borç) 8.000; 103 Verilen Çekler (alacak) 48.000',
        },
        'B',
        'Senet karşılığı alışta borç açık hesap (320) değil **321 Borç Senetleri** ile izlenir. Mal maliyeti 153 (borç) 40.000 ₺, yüklenilen KDV 191 (borç) 40.000 × %20 = 8.000 ₺; senet borcu 321 (alacak) 48.000 ₺. Alışta 391 değil 191 çalışır; KDV maliyete eklenmez.',
        "3065 sayılı KDVK md 29; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 153/191/321",
    ),
    # düzey 2
    '0002': patch(
        "İşletme 50.000 ₺ tutarındaki ticari malı satın alırken, malın işletmeye taşınması için 5.000 ₺ nakliye bedeli de aynı faturada yer almıştır. İşlemin tamamı %20 KDV'ye tabi olup veresiye gerçekleşmiştir. Doğru kayıt hangisidir?",
        {
            'A': '153 Ticari Mallar (borç) 55.000 ve 191 İndirilecek KDV (borç) 11.000; 320 Satıcılar (alacak) 66.000',
            'B': '153 Ticari Mallar (borç) 50.000 ve 770 Genel Yönetim Giderleri (borç) 5.000 ve 191 İndirilecek KDV (borç) 10.000; 320 Satıcılar (alacak) 65.000',
            'C': '153 Ticari Mallar (borç) 55.000 ve 391 Hesaplanan KDV (borç) 11.000; 320 Satıcılar (alacak) 66.000',
            'D': '153 Ticari Mallar (borç) 55.000; 320 Satıcılar (alacak) 55.000',
            'E': '153 Ticari Mallar (borç) 50.000 ve 191 İndirilecek KDV (borç) 11.000; 320 Satıcılar (alacak) 61.000',
        },
        'A',
        'Malın işletmeye getirilmesi için ödenen nakliye, malın **maliyetine** eklenir: 153 (borç) 50.000 + 5.000 = 55.000 ₺. KDV toplam matrah üzerinden: (50.000 + 5.000) × %20 = 11.000 ₺ → 191 (borç). Veresiye borç 320 (alacak) 66.000 ₺. Nakliye ayrı gidere (770) atılmaz; alışta 391 değil 191 çalışır.',
        "3065 sayılı KDVK md 29; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 153/191/320",
    ),
    # düzey 2
    '0003': patch(
        'İşletme, genel yönetimle ilgili bir dava için serbest meslek erbabı bir avukattan 20.000 ₺ + %20 KDV tutarında hizmet almış ve serbest meslek makbuzunu kayıtlarına almıştır. Avukatlık ücreti üzerinden soruda kullanılacak %20 oranında gelir vergisi stopajı yapılmış; kalan tutar henüz ödenmemiştir. KDV tevkifatı yoktur.\n\nBu hizmet alımının kaydında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?',
        {
            'A': '191 İndirilecek KDV hesabı 3.200 ₺ borçlandırılır',
            'B': '360 Ödenecek Vergi ve Fonlar hesabı 4.000 ₺ alacaklandırılır',
            'C': '770 Genel Yönetim Giderleri hesabı KDV dâhil 24.000 ₺ borçlandırılır',
            'D': '320 Satıcılar hesabı 24.000 ₺ alacaklandırılır',
            'E': '391 Hesaplanan KDV hesabı 4.000 ₺ alacaklandırılır',
        },
        'B',
        "Gider brüt ücret üzerinden yazılır: 770 20.000 ₺; KDV 4.000 ₺ indirilecek KDV'dir (191). Stopaj 20.000 × %20 = 4.000 ₺ işletmenin sorumlu sıfatıyla ödeyeceği vergidir (360 alacak). Avukata ödenecek tutar 20.000 + 4.000 − 4.000 = 20.000 ₺ (320 veya 336 alacak).",
        '3065 s. KDVK md 29 / TDHP 770-191-320',
    ),
    # düzey 2
    '0004': patch(
        "Bir perakende işletme, gün içinde yazar kasa fişleriyle KDV dahil toplam 96.000 ₺ tutarında (%20 KDV'ye tabi) mal satmış ve bedeli nakden tahsil etmiştir. Bu satışın hasılat kaydında aşağıdakilerden hangisi yer alır?",
        {
            'A': '100 Kasa (borç) 115.200; 600 Yurtiçi Satışlar (alacak) 96.000 ve 391 Hesaplanan KDV (alacak) 19.200',
            'B': '100 Kasa (borç) 96.000; 600 Yurtiçi Satışlar (alacak) 80.000 ve 191 İndirilecek KDV (alacak) 16.000',
            'C': '100 Kasa (borç) 96.000; 600 Yurtiçi Satışlar (alacak) 80.000 ve 391 Hesaplanan KDV (alacak) 16.000',
            'D': '100 Kasa (borç) 96.000; 600 Yurtiçi Satışlar (alacak) 96.000',
            'E': '100 Kasa (borç) 96.000; 600 Yurtiçi Satışlar (alacak) 76.800 ve 391 Hesaplanan KDV (alacak) 19.200',
        },
        'C',
        "KDV dahil tahsilat 100 Kasa (borç) 96.000 ₺. Matrah = dahil ÷ 1,20 = 80.000 ₺ → 600 (alacak); hesaplanan KDV = 96.000 − 80.000 = 16.000 ₺ → 391 (alacak). KDV'yi dahil tutar × %20 (19.200) ile bulmak yanlıştır; satışta 191 değil 391 çalışır.",
        "3065 sayılı KDVK md 20; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 100/600/391",
    ),
    # düzey 2
    '0005': patch(
        'Aşağıdaki KDV kayıtlarından hangisi YANLIŞTIR?',
        {
            'A': "Mal alışında yüklenilen KDV 191 İndirilecek KDV'nin borcuna yazılır.",
            'B': "Mal satışında hesaplanan KDV 391 Hesaplanan KDV'nin alacağına yazılır.",
            'C': "Satıştan iade alınan mala ilişkin KDV, 191 İndirilecek KDV'nin borcuna yazılarak düzeltilir.",
            'D': "Ay sonu ödenecek net KDV 360 Ödenecek Vergi ve Fonlar'ın alacağına yazılır.",
            'E': "Alıştan iade edilen mala ilişkin KDV, 191 İndirilecek KDV'nin alacağına yazılarak düzeltilir.",
        },
        'C',
        "Satış iadesinde daha önce **satışta hesaplanan** KDV azaltılır; bu, 391 Hesaplanan KDV'nin **borcuna** yazılarak yapılır — 191 kullanılmaz. Alış iadesinde ise 191 alacaklandırılır. Bu nedenle satış iadesini 191'e yazan ifade yanlıştır; diğer kayıtlar doğrudur.",
        "3065 sayılı KDVK md 35; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 191/391",
    ),
    # düzey 2
    '0006': patch(
        "Bir ticaret işletmesinin ay içindeki alışları şöyledir: 40.000 ₺ + %20 KDV ticari mal, 30.000 ₺ + %10 KDV ticari mal, 25.000 ₺ + %20 KDV büro mobilyası ve işyeri olarak kullanılan dükkân için 10.000 ₺ + %20 KDV kira. Ay sonunda %20 KDV'li mallardan 5.000 ₺'lik kısım kusurlu olduğu için satıcıya iade edilmiştir. Önceki aydan devreden KDV yoktur ve tüm belgeler usulüne uygundur.\n\nBuna göre ay sonunda '191 İndirilecek KDV' hesabının borç kalanı kaç ₺'dir?",
        {
            'A': '18.000',
            'B': '13.000',
            'C': '21.000',
            'D': '16.000',
            'E': '17.000',
        },
        'E',
        "Yüklenilen KDV: 8.000 + 3.000 + 5.000 + 2.000 = 18.000 ₺. Alış iadesinde iade edilen malın KDV'si 191'den çıkarılır: 5.000 × %20 = 1.000 ₺ (320 borç / 153 ve 191 alacak). 191 borç kalanı = 18.000 − 1.000 = 17.000 ₺. Demirbaş ve işyeri kirasının KDV'si de indirilebilir.",
        "3065 sayılı KDVK md 28; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 191",
    ),
    # düzey 2
    '0007': patch(
        "Ev eşyası satan bir mağaza, KDV dâhil etiket fiyatı 108.000 ₺ olan bir mutfak takımını bir müşterisine satmış ve bedeli kredi kartıyla tahsil etmiştir. Ürün %20 oranında KDV'ye tabidir.\n\nBu satış nedeniyle 391 Hesaplanan KDV hesabına yazılacak tutar kaç ₺'dir?",
        {
            'A': '18.000 ₺',
            'B': '20.000 ₺',
            'C': '90.000 ₺',
            'D': '21.600 ₺',
            'E': '108.000 ₺',
        },
        'A',
        "Bedel KDV dahil olduğundan matrah = 108.000 ÷ 1,20 = 90.000 ₺; hesaplanan KDV = 108.000 − 90.000 = **18.000 ₺** (391). KDV'yi dahil tutar × %20 (21.600) ile bulmak yaygın hatadır; matrah × %20 olmalıdır.",
        "3065 sayılı KDVK md 20; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 391",
    ),
    # düzey 2
    '0008': patch(
        'Ay sonu mahsup sonrası 360 Ödenecek Vergi ve Fonlar hesabında 9.000 ₺ KDV borcu bulunmaktadır. Bu borç için vergi dairesine banka üzerinden ödeme yapılmıştır. Ödeme kaydı aşağıdakilerden hangisidir?',
        {
            'A': '360 Ödenecek Vergi ve Fonlar (borç) 9.000; 191 İndirilecek KDV (alacak) 9.000',
            'B': '770 Genel Yönetim Giderleri (borç) 9.000; 102 Bankalar (alacak) 9.000',
            'C': '391 Hesaplanan KDV (borç) 9.000; 102 Bankalar (alacak) 9.000',
            'D': '360 Ödenecek Vergi ve Fonlar (borç) 9.000; 102 Bankalar (alacak) 9.000',
            'E': '102 Bankalar (borç) 9.000; 360 Ödenecek Vergi ve Fonlar (alacak) 9.000',
        },
        'D',
        'Vergi borcunun ödenmesi pasifi (360) azaltır: 360 (borç) 9.000 ₺ / 102 (alacak) 9.000 ₺. Ay sonu tahakkukta 360 alacaklandırılmıştı; ödemede borçlandırılarak kapanır. Ödeme bir gider (770) değildir; 391/191 bu aşamada çalışmaz.',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 360/102",
    ),
    # düzey 2
    '0009': patch(
        "Önceki aydan 10.000 ₺ devreden KDV'si bulunan işletmenin ay içindeki işlemleri şöyledir: 150.000 ₺ + %20 KDV ve 40.000 ₺ + %10 KDV satış; %20 oranlı satışlardan 10.000 ₺ + KDV tutarındaki malın müşteri tarafından iadesi; 120.000 ₺ + %20 KDV ve 30.000 ₺ + %10 KDV alış.\n\nBuna göre ay sonu mahsubundan sonra izleyen aya devreden KDV kaç ₺'dir?",
        {
            'A': '3.000',
            'B': '2.000',
            'C': '5.000',
            'D': '15.000',
            'E': '1.000',
        },
        'C',
        "Hesaplanan KDV = 30.000 + 4.000 − 2.000 (satış iadesi 391'e borç) = 32.000 ₺. İndirilecek KDV = 24.000 + 3.000 = 27.000 ₺. İndirim toplamı 27.000 + 10.000 = 37.000 ₺ hesaplanan KDV'yi 5.000 ₺ aştığından ödenecek KDV çıkmaz; 5.000 ₺ izleyen aya devreder.",
        '3065 s. KDVK md 29/2 / TDHP 190',
    ),
    # düzey 2
    '0010': patch(
        'Peşin satılan maldan 10.000 ₺ + %20 KDV tutarındaki kısım müşteri tarafından iade edilmiş, bedel kasadan ödenmiştir (satış iadesi). Doğru kayıt hangisidir?',
        {
            'A': '100 KASA 12.000 ₺ (borç) / 610 SATIŞTAN İADELER 10.000 ₺ (alacak) / 391 HESAPLANAN KDV 2.000 ₺ (alacak)',
            'B': '610 SATIŞTAN İADELER 10.000 ₺ (borç) / 191 İNDİRİLECEK KDV 2.000 ₺ (borç) / 100 KASA 12.000 ₺ (alacak)',
            'C': '153 TİCARİ MALLAR 10.000 ₺ (borç) / 191 İND. KDV 2.000 ₺ (borç) / 100 KASA 12.000 ₺ (alacak)',
            'D': '610 SATIŞTAN İADELER 10.000 ₺ (borç) / 391 HESAPLANAN KDV 2.000 ₺ (borç) / 100 KASA 12.000 ₺ (alacak)',
            'E': '600 YURTİÇİ SATIŞLAR 10.000 ₺ (borç) / 391 HESAPLANAN KDV 2.000 ₺ (borç) / 100 KASA 12.000 ₺ (alacak)',
        },
        'D',
        "Satış iadesi **610 SATIŞTAN İADELER (borç) 10.000 ₺** (hasılatı düzelten (–) hesap) ile izlenir; daha önce hesaplanan KDV geri verilir **391 (borç) 2.000 ₺**; ödenen bedel **100 (alacak) 12.000 ₺**. İade 600'ün borcuna yazılmaz, 610 kullanılır.",
        '3065 s. KDVK md 35 / TDHP 610-391-100',
    ),
    # düzey 2
    '0011': patch(
        "İşletme, yönetim binasının temizliği için bir firmadan 50.000 ₺ + %20 KDV tutarında hizmet almıştır. Hizmet kısmi tevkifat kapsamındadır ve soruda kullanılacak tevkifat oranı 9/10'dur; işletme tevkif ettiği KDV'yi sorumlu sıfatıyla beyan edip ödeyecektir. Bedel henüz satıcıya ödenmemiştir.\n\nHizmet alımının kaydında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '191 İndirilecek KDV hesabı 1.000 ₺ borçlandırılır',
            'B': '320 Satıcılar hesabı 60.000 ₺ alacaklandırılır',
            'C': '391 Hesaplanan KDV hesabı tevkifat için 9.000 ₺ alacaklandırılır',
            'D': '320 Satıcılar hesabı 50.000 ₺ alacaklandırılır',
            'E': '360 Ödenecek Vergi ve Fonlar hesabı 9.000 ₺ alacaklandırılır',
        },
        'E',
        "Hesaplanan KDV 10.000 ₺; bunun 9/10'u (9.000 ₺) alıcı tarafından tevkif edilir ve sorumlu sıfatıyla ödeneceğinden 360'a alacak yazılır. Satıcıya 50.000 + 1.000 = 51.000 ₺ borçlanılır. Yüklenilen KDV'nin tamamı (10.000 ₺) 191'e alınır. Kayıt: 770 50.000 ₺ ve 191 10.000 ₺ borç / 320 51.000 ₺ ve 360 9.000 ₺ alacak.",
        '3065 s. KDVK md 29 (katma değer)',
    ),
    # düzey 2
    '0012': patch(
        "İşletme 12.000 ₺ + %20 KDV bedelle danışmanlık hizmeti almış, bedeli banka ile ödemiştir (tevkifat yoktur). 191 İNDİRİLECEK KDV'ye alınacak tutar kaç ₺'dir?",
        {
            'A': '2.800 ₺',
            'B': '2.400 ₺',
            'C': '14.400 ₺',
            'D': '12.000 ₺',
            'E': '3.600 ₺',
        },
        'B',
        "Yüklenilen KDV = matrah × oran = 12.000 × %20 = **2.400 ₺** (191'in borcuna). 14.400 ₺ KDV dahil ödenen toplamdır.",
        '3065 s. KDVK md 4 (hizmet), md 29',
    ),
    # düzey 3
    '0013': patch(
        'Stoklarını sürekli envanter yöntemiyle izleyen ve maliyet üzerinden %25 kârla satış yapan bir işletme, daha önce kredili sattığı ticari malların KDV hariç 15.000 ₺ tutarındaki kısmını aynı dönemde iade almıştır (KDV %20). İade bedeli müşterinin borcundan düşülmüştür. Buna göre iade kayıtlarıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '153 Ticari Mallar hesabı 15.000 ₺ borçlandırılır',
            'B': '120 Alıcılar hesabı 15.000 ₺ alacaklandırılır',
            'C': '621 Satılan Ticari Mallar Maliyeti hesabı 12.000 ₺ alacaklandırılır',
            'D': '391 Hesaplanan KDV hesabı 3.000 ₺ alacaklandırılır',
            'E': '621 Satılan Ticari Mallar Maliyeti hesabı 15.000 ₺ alacaklandırılır',
        },
        'C',
        "Hasılat düzeltmesi: 610 Satıştan İadeler (borç) 15.000 + 391 (borç) 3.000 / 120 (alacak) 18.000. Maliyet düzeltmesi: 153 (borç) / **621 (alacak) 12.000**; maliyet 15.000 / 1,25 = 12.000 ₺'dir.",
        'THP 610, 391, 120, 153, 621',
    ),
    # düzey 3
    '0014': patch(
        'Stoklarını sürekli envanter yöntemiyle izleyen işletme, kredili aldığı 30.000 ₺ + %20 KDV tutarındaki ticari malın hepsi stoktayken satıcıdan 3.000 ₺ + %20 KDV tutarında iskonto faturası almış, tutar satıcıya olan borcundan düşülmüştür. Buna göre iskonto kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '649 Diğer Olağan Gelir ve Kârlar hesabı 3.000 ₺ alacaklandırılır',
            'B': '320 Satıcılar hesabı 3.000 ₺ borçlandırılır',
            'C': '191 İndirilecek KDV hesabı 600 ₺ borçlandırılır',
            'D': '153 Ticari Mallar hesabı 3.600 ₺ alacaklandırılır',
            'E': '191 İndirilecek KDV hesabı 600 ₺ alacaklandırılır',
        },
        'E',
        "Kayıt: 320 (borç) 3.600 / 153 (alacak) 3.000 + **191 (alacak) 600**. Mal stokta olduğundan alış iskontosu stok maliyetini azaltır; alışta indirilen KDV'nin iskontoya düşen kısmı geri alınır.",
        'THP 320, 153, 191',
    ),
    # düzey 3
    '0015': patch(
        'İşletme beş yıllığına kiraladığı yönetim binasına 100.000 ₺ + %20 KDV tutarında sabit havalandırma tesisatı yaptırmış, bedeli bankadan ödemiş ve harcamayı aktifleştirmiştir. Buna göre harcama kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '264 Özel Maliyetler hesabı 120.000 ₺ borçlandırılır',
            'B': '191 İndirilecek KDV hesabı 20.000 ₺ alacaklandırılır',
            'C': '770 Genel Yönetim Giderleri hesabı 100.000 ₺ borçlandırılır',
            'D': '264 Özel Maliyetler hesabı 100.000 ₺ borçlandırılır',
            'E': '252 Binalar hesabı 100.000 ₺ borçlandırılır',
        },
        'D',
        'Kiralanan gayrimenkule yapılan ve kira süresi sonunda mal sahibine kalacak harcamalar **264 Özel Maliyetler** (maddi olmayan duran varlık) hesabında aktifleştirilir: 264 (borç) 100.000 + 191 (borç) 20.000 / 102 (alacak) 120.000. Bina işletmenin olmadığı için 252 kullanılmaz.',
        'VUK m. 327; THP 264, 191, 102',
    ),
    # düzey 3
    '0016': patch(
        "Bir işletmenin ay içindeki işlemleri şöyledir: %20 KDV'ye tabi 300.000 ₺ ve %10 KDV'ye tabi 100.000 ₺ satış; %20 KDV'ye tabi satışlardan 20.000 ₺'lik iade alınması; %20 KDV'ye tabi 200.000 ₺ ve %1 KDV'ye tabi 50.000 ₺ alış. Önceki aydan devreden KDV 7.000 ₺'dir. Buna göre bu ay ödenecek KDV kaç ₺'dir?",
        {
            'A': '11.500 ₺',
            'B': '25.500 ₺',
            'C': '19.000 ₺',
            'D': '18.500 ₺',
            'E': '22.500 ₺',
        },
        'D',
        'Hesaplanan: 60.000 + 10.000 − iade 4.000 = 66.000 ₺. İndirilecek: 40.000 + 500 = 40.500 ₺. Ödenecek: 66.000 − 40.500 − devreden 7.000 = **18.500 ₺**.',
        '3065 sayılı KDVK m. 29, 35; THP 191, 391, 190, 360',
    ),
    # düzey 3
    '0017': patch(
        "Bir işletme ay içinde %10 KDV'ye tabi malları KDV dâhil 110.000 ₺'ye, %20 KDV'ye tabi malları KDV dâhil 60.000 ₺'ye satmıştır. Buna göre bu satışlar nedeniyle 391 Hesaplanan KDV hesabına yazılacak toplam tutar kaç ₺'dir?",
        {
            'A': '34.000 ₺',
            'B': '16.000 ₺',
            'C': '20.000 ₺',
            'D': '15.000 ₺',
            'E': '17.000 ₺',
        },
        'C',
        'KDV dâhil tutardan KDV = tutar × oran / (1 + oran): 110.000 × 10/110 = 10.000 ₺; 60.000 × 20/120 = 10.000 ₺. Toplam **20.000 ₺**. KDV dâhil tutara doğrudan oran uygulamak hatalıdır.',
        '3065 sayılı KDVK m. 20; THP 391',
    ),
    # düzey 2
    '0018': patch(
        "KDV ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. 190 Devreden KDV aktif bir hesaptır ve sonraki dönemlerde indirilir.\n\nII. 391 Hesaplanan KDV dönem sonunda 690 hesabına devredilir.\n\nIII. KDV dâhil tutardan matrah, tutarın (1 + oran)'a bölünmesiyle bulunur.",
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'I ve III',
            'E': 'Yalnız III',
        },
        'D',
        "I ve III doğrudur. II yanlıştır: 391 bir sonuç hesabı değil, ay sonunda 191 ile mahsup edilen **bilanço** (yabancı kaynak) hesabıdır; 690'a devredilmez.",
        '3065 sayılı KDVK m. 29-30; THP 190, 391',
    ),
    # düzey 3
    '0019': patch(
        'Stoklarını aralıklı envanter yöntemiyle izleyen bir işletme, daha önce kredili sattığı malların 20.000 ₺ + %20 KDV tutarındaki kısmını iade almış ve tutarı müşterinin borcundan düşmüştür. Buna göre iade kaydında aşağıdakilerden hangisi yer almaz?',
        {
            'A': '120 Alıcılar hesabı 24.000 ₺ alacaklandırılır',
            'B': '391 Hesaplanan KDV hesabı 4.000 ₺ borçlandırılır',
            'C': '610 Satıştan İadeler hesabı 20.000 ₺ borçlandırılır',
            'D': '621 Satılan Ticari Mallar Maliyeti hesabı kullanılmaz',
            'E': '153 Ticari Mallar hesabı 16.000 ₺ borçlandırılır',
        },
        'E',
        'Aralıklı envanterde satışlarda maliyet kaydı yapılmadığından iadede de **stok ve maliyet düzeltmesi yapılmaz**; yalnız hasılat ve KDV düzeltilir: 610 (borç) 20.000 + 391 (borç) 4.000 / 120 (alacak) 24.000. Stok dönem sonunda sayımla belirlenir.',
        'THP 610, 391, 120',
    ),
    # düzey 2
    '0020': patch(
        "Esas faaliyeti ticaret olan bir işletmenin ay içindeki alışları değerlendirilmektedir. Buna göre aşağıdaki alışlardan hangisinin KDV'si indirim konusu yapılamaz?",
        {
            'A': 'Yöneticiler için binek otomobil alımı',
            'B': 'Satılmak üzere ticari mal alımı',
            'C': 'Büro için demirbaş alımı',
            'D': 'Yönetim danışmanlığı hizmeti alımı',
            'E': 'İthal edilen ticari mal için gümrükte ödenen KDV',
        },
        'A',
        "KDVK m. 30/b uyarınca faaliyeti kiralama veya satış olmayan işletmelerin **binek otomobil** alımlarında yüklendikleri KDV indirilemez; maliyete eklenir. Diğer alımlar vergiye tabi işlemlerde kullanıldığından KDV'leri indirilir.",
        '3065 sayılı KDVK m. 29-30',
    ),
    # düzey 2
    '0021': patch(
        'İndirilemeyen KDV ile ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İndirilemeyen KDV, indirilecek KDV hesabına alınmaz.',
            'B': 'Kanunen indirimi kabul edilmeyen KDV 191 hesabında bekletilip sonraki dönemlerde indirilir.',
            'C': 'Belgeye (faturaya) dayanmayan KDV indirim konusu yapılamaz.',
            'D': "Gelir/kurumlar vergisi açısından gider kabul edilmeyen harcamaların KDV'si de indirilemez.",
            'E': 'İndirim hakkı tanınmayan KDV, ilgili mal/hizmetin maliyetine veya gidere eklenebilir.',
        },
        'B',
        "İndirim hakkı tanınmayan KDV **191'e alınıp sürekli bekletilerek indirilemez**; maliyete/gidere aktarılır (indirilemez kalır). Belgesiz KDV ve KKEG niteliğindeki harcamaların KDV'si indirilemez — diğer öncüller doğrudur.",
        '3065 s. KDVK md 30 / md 34',
    ),
    # düzey 2
    '0022': patch(
        '7/A seçeneğini uygulayan bir üretim işletmesi, fabrikadaki üretim makineleri için 15.000 ₺ + %20 KDV, yönetim binasındaki iklimlendirme sistemi için 5.000 ₺ + %20 KDV tutarında dışarıdan bakım-onarım hizmeti almış ve bedellerin tamamını kasadan peşin ödemiştir.\n\nBu işlemin yevmiye kaydında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?',
        {
            'A': '770 Genel Yönetim Giderleri hesabı 20.000 ₺ borçlandırılır',
            'B': '391 Hesaplanan KDV hesabı 4.000 ₺ borçlandırılır',
            'C': '730 Genel Üretim Giderleri hesabı 15.000 ₺ borçlandırılır',
            'D': '100 Kasa hesabı 20.000 ₺ alacaklandırılır',
            'E': '153 Ticari Mallar hesabı 15.000 ₺ borçlandırılır',
        },
        'C',
        "7/A'da gider oluştuğu yere göre izlenir: üretim makinelerinin bakımı 730 Genel Üretim Giderleri (15.000 ₺), yönetim binasındaki bakım 770 Genel Yönetim Giderleri (5.000 ₺). Yüklenilen KDV 191'e alınır (4.000 ₺); kasadan çıkan toplam 24.000 ₺. Kayıt: 730 15.000 ₺, 770 5.000 ₺ ve 191 4.000 ₺ borç / 100 Kasa 24.000 ₺ alacak.",
        "3065 sayılı KDVK md 29; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 770/191/100",
    ),
    # düzey 2
    '0023': patch(
        'İşletme malı veresiye (senet karşılığı) teslim etmiştir; bedel senedin vadesinde tahsil edilecektir. Bu satışta hesaplanan KDV bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Veresiye teslimde KDV doğmaz; peşin satışlarda hesaplanan KDV doğar.',
            'B': 'KDV, senet tutarının tamamı üzerinden vade farkı hariç tutularak hesaplanmaz.',
            'C': 'KDV teslim döneminde hesaplanıp beyan edilir; senedin tahsili beklenmez.',
            'D': 'KDV senedin vadesinde tahsilat yapıldığında hesaplanır ve o dönem beyan edilir.',
            'E': 'KDV doğar ancak 391 yerine 190 Devreden KDV hesabında izlenir.',
        },
        'C',
        "KDV'de vergiyi doğuran olay kural olarak **teslim/hizmet** anıdır; tahsilat (senet vadesi) beklenmez. Mal teslim edildiği dönemde KDV hesaplanır (391) ve o dönem beyan edilir. Veresiye olması KDV'yi ertelemez.",
        '3065 sayılı KDVK md 10',
    ),
    # düzey 2
    '0024': patch(
        'İşletmenin daha önce satın alıp henüz satmadığı mal için satıcı, 4.000 ₺ + %20 KDV tutarında lehine fiyat farkı faturası düzenlemiştir (borç veresiye). Alıcı işletmede bu fiyat farkının kaydı aşağıdakilerden hangisidir?',
        {
            'A': '153 Ticari Mallar (borç) 4.000 ve 391 Hesaplanan KDV (borç) 800; 320 Satıcılar (alacak) 4.800',
            'B': '770 Genel Yönetim Giderleri (borç) 4.000 ve 191 İndirilecek KDV (borç) 800; 320 Satıcılar (alacak) 4.800',
            'C': '320 Satıcılar (borç) 4.800; 153 Ticari Mallar (alacak) 4.000 ve 191 İndirilecek KDV (alacak) 800',
            'D': '153 Ticari Mallar (borç) 4.800; 320 Satıcılar (alacak) 4.800',
            'E': '153 Ticari Mallar (borç) 4.000 ve 191 İndirilecek KDV (borç) 800; 320 Satıcılar (alacak) 4.800',
        },
        'E',
        'Fiyat farkı, malın maliyetini artıran ek bir matrahtır; mal henüz stoktayken 153 (borç) 4.000 ₺, ek yüklenilen KDV 191 (borç) 4.000 × %20 = 800 ₺, borç 320 (alacak) 4.800 ₺. Fiyat farkı gider (770) değil maliyettir; alıcı için 391 değil 191 çalışır.',
        "3065 sayılı KDVK md 35; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 153/191/320",
    ),
    # düzey 2
    '0025': patch(
        "İşletme bir ayda 90.000 ₺ (%20) tutarında satış yapmış; ancak bu satışların 15.000 ₺'lik (%20) kısmı müşteri tarafından iade edilmiştir. İade sonrası bu ay net hesaplanan KDV kaç ₺'dir?",
        {
            'A': '15.000 ₺',
            'B': '18.000 ₺',
            'C': '12.000 ₺',
            'D': '3.000 ₺',
            'E': '21.000 ₺',
        },
        'A',
        "Satıştan hesaplanan KDV = 90.000 × %20 = 18.000 ₺. İade edilen kısmın KDV'si = 15.000 × %20 = 3.000 ₺ geri alınır (391 borçlandırılır). Net hesaplanan KDV = 18.000 − 3.000 = **15.000 ₺**. İade, satış KDV'sini azaltır.",
        "3065 sayılı KDVK md 35; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 391/610",
    ),
    # düzey 2
    '0026': patch(
        "Bir işletmenin ay içindeki satışları 60.000 ₺ + %20 KDV ve 50.000 ₺ + %10 KDV'dir. Ay içinde %20 oranlı satışlardan 5.000 ₺'lik mal iade alınmış, %10 oranlı satış için müşteriye sonradan 2.000 ₺ iskonto yapılmış ve %20 oranlı vadeli satış için müşteriye 3.000 ₺ vade farkı faturası düzenlenmiştir. İade ve iskontolarda KDV de düzeltilmektedir.\n\nBuna göre ay sonunda '391 Hesaplanan KDV' hesabının alacak kalanı kaç ₺'dir?",
        {
            'A': '14.800',
            'B': '16.400',
            'C': '17.400',
            'D': '15.800',
            'E': '16.000',
        },
        'B',
        "Satışlar: 12.000 + 5.000 = 17.000 ₺. Satış iadesi 5.000 × %20 = 1.000 ₺ ve sonradan iskonto 2.000 × %10 = 200 ₺ KDV'yi azaltır (391 borç). Vade farkı satılan malın oranıyla KDV'ye tabidir: 3.000 × %20 = 600 ₺ (391 alacak). Kalan = 17.000 − 1.000 − 200 + 600 = 16.400 ₺.",
        "3065 sayılı KDVK md 28; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 391",
    ),
    # düzey 2
    '0027': patch(
        "İşletme, gelir/kurumlar vergisi açısından kanunen kabul edilmeyen bir harcama için 10.000 ₺ + %20 KDV ödemiştir (bedel bankadan). Bu harcamanın KDV'si indirilemediğine göre doğru kayıt hangisidir?",
        {
            'A': '689 Diğer Olağandışı Gider ve Zararlar (borç) 12.000; 102 Bankalar (alacak) 12.000',
            'B': '689 Diğer Olağandışı Gider ve Zararlar (borç) 10.000 ve 391 Hesaplanan KDV (alacak) 2.000; 102 Bankalar (alacak) 8.000',
            'C': '153 Ticari Mallar (borç) 12.000; 102 Bankalar (alacak) 12.000',
            'D': '191 İndirilecek KDV (borç) 2.000; 102 Bankalar (alacak) 2.000',
            'E': '689 Diğer Olağandışı Gider ve Zararlar (borç) 10.000 ve 191 İndirilecek KDV (borç) 2.000; 102 Bankalar (alacak) 12.000',
        },
        'A',
        "Kanunen kabul edilmeyen harcamanın KDV'si indirilemez (md 30); ayrı 191'e alınmaz, harcamayla birlikte gidere eklenir. Gider + indirilemeyen KDV = 10.000 + 2.000 = 12.000 ₺ → 689 (borç) / 102 (alacak) 12.000 ₺. İndirilemeyen KDV maliyet/gider unsuru olur.",
        "3065 sayılı KDVK md 30; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 689/102",
    ),
    # düzey 2
    '0028': patch(
        'Bir işletmenin ay sonu mizanında 391 Hesaplanan KDV hesabı 20.000 ₺ alacak, 191 İndirilecek KDV hesabı 23.000 ₺ borç ve önceki aydan gelen 190 Devreden KDV hesabı 4.000 ₺ borç kalanı vermektedir. İşletme ay sonunda KDV hesaplarını mahsup etmektedir.\n\nMahsup kaydında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?',
        {
            'A': '360 Ödenecek Vergi ve Fonlar hesabı 7.000 ₺ alacaklandırılır',
            'B': '391 Hesaplanan KDV hesabı 20.000 ₺ alacaklandırılır',
            'C': '190 Devreden KDV hesabı 7.000 ₺ olarak borçlandırılır',
            'D': '191 İndirilecek KDV hesabı 23.000 ₺ borçlandırılır',
            'E': '190 Devreden KDV hesabı net fark olan 3.000 ₺ borçlandırılır',
        },
        'C',
        "İndirim toplamı 23.000 + 4.000 = 27.000 ₺, hesaplanan KDV 20.000 ₺'den büyük olduğundan ödenecek KDV yoktur; 7.000 ₺ izleyen aya devreder. Kayıt: 391 20.000 ₺ ve 190 (yeni devir) 7.000 ₺ borç / 191 23.000 ₺ ve 190 (eski devir) 4.000 ₺ alacak.",
        "3065 sayılı KDVK md 29/2; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 360/190",
    ),
    # düzey 2
    '0029': patch(
        'İthal edilen bir malda KDV matrahının belirlenmesi bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Matrah malın yurt dışı satış bedelidir; gümrük vergisi matraha eklenmez.',
            'B': 'İthalatta KDV matrahı sıfırdır; gümrük vergisi ödenir.',
            'C': 'İthalatta KDV, malın maliyetine eklenip ayrıca matrah hesaplanmaz.',
            'D': 'Gümrük vergisi ve ithalat harçları da KDV matrahına dahil edilir.',
            'E': 'Matrah, malın yurt içinde satılacağı perakende fiyattır.',
        },
        'D',
        "İthalatta KDV matrahı, malın gümrük kıymetine gümrük vergisi ve diğer ithalat vergi/harçları ile masrafların eklenmesiyle bulunur; KDV bu genişletilmiş matrah üzerinden hesaplanır (md 21). Ödenen KDV 191'e alınıp indirilir.",
        '3065 sayılı KDVK md 21',
    ),
    # düzey 2
    '0030': patch(
        'Bir işletmenin ay sonu 360 Ödenecek Vergi ve Fonlar hesabında 12.000 ₺ KDV ve 3.000 ₺ muhtasar (stopaj) olmak üzere toplam 15.000 ₺ borç birikmiştir. Tamamı bankadan ödendiğine göre kayıt aşağıdakilerden hangisidir?',
        {
            'A': '360 Ödenecek Vergi ve Fonlar (borç) 15.000; 102 Bankalar (alacak) 15.000',
            'B': '102 Bankalar (borç) 15.000; 360 Ödenecek Vergi ve Fonlar (alacak) 15.000',
            'C': '770 Genel Yönetim Giderleri (borç) 15.000; 102 Bankalar (alacak) 15.000',
            'D': '360 Ödenecek Vergi ve Fonlar (borç) 12.000; 102 Bankalar (alacak) 12.000',
            'E': '191 İndirilecek KDV (borç) 15.000; 102 Bankalar (alacak) 15.000',
        },
        'A',
        "360 hesabı hem ödenecek KDV'yi hem stopajı topluca izler; tahakkukta alacaklandırılmış tutarın tamamı ödemede borçlandırılarak kapanır: 360 (borç) 12.000 + 3.000 = 15.000 ₺ / 102 (alacak) 15.000 ₺. Yalnız KDV kısmını ödemek borcu tümüyle kapatmaz.",
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 360/102",
    ),
    # düzey 2
    '0031': patch(
        'Yurt dışından ithal edilen ticari mal için gümrükte ödenen KDV ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İthalatta yüklenilen KDV ancak ihracat yapılırsa indirilebilir.',
            'B': 'İthalatta KDV doğmaz; gümrük vergisi ödenir.',
            'C': 'Gümrükte ödenen KDV doğrudan malın satış fiyatına eklenir, ayrıca kaydedilmez.',
            'D': "Gümrükte ödenen KDV 391 HESAPLANAN KDV'ye alacak yazılır.",
            'E': "Gümrükte ödenen KDV 191'e alınıp hesaplanan KDV'den indirilir.",
        },
        'E',
        "Mal ithali KDV'nin konusuna girer; gümrükte ödenen KDV belgeye dayanarak **191 İNDİRİLECEK KDV**'ye alınır ve genel esaslara göre hesaplanan KDV'den indirilir. İthalatta 391 değil 191 çalışır.",
        '3065 s. KDVK md 1/2, md 29',
    ),
    # düzey 2
    '0032': patch(
        "KDV'nin indirilebilmesinin şekil şartlarıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'KDV fatura veya benzeri belgede ayrıca gösterilmelidir',
            'B': 'Belge kanuni defterlere kaydedilmelidir',
            'C': "Defter kaydı yeterlidir; KDV'nin belgede gösterilmesi gerekmez",
            'D': 'Gerçek bir işleme dayanmayan belgedeki KDV indirilemez',
            'E': 'İndirilecek KDV 191 hesabında izlenir',
        },
        'C',
        "KDVK m. 29/3'e göre indirim hakkı, KDV'nin fatura veya benzeri vesikalarda ayrıca gösterilmesi ve bu belgelerin kanuni defterlere kaydedilmesi şartıyla kullanılabilir. Gerçek bir işleme dayanmayan belgedeki KDV indirilemez; indirilecek KDV 191 hesabında izlenir.",
        "3065 sayılı KDVK md 34; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 191",
    ),
    # düzey 3
    '0033': patch(
        'İşletme 25.000 ₺ + %20 KDV tutarındaki ticari malı kredili satmıştır. Alıcı, malların istenen özellikte olmadığını bildirerek iskonto istemiş; işletme %10 iskonto kabul ederek iskonto faturası düzenlemiş ve tutarı alıcının borcundan düşmüştür. Buna göre iskonto kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '120 Alıcılar hesabı 2.500 ₺ alacaklandırılır',
            'B': '610 Satıştan İadeler hesabı 2.500 ₺ borçlandırılır',
            'C': '611 Satış İskontoları hesabı 3.000 ₺ borçlandırılır',
            'D': '611 Satış İskontoları hesabı 2.500 ₺ borçlandırılır',
            'E': '391 Hesaplanan KDV hesabı 500 ₺ alacaklandırılır',
        },
        'D',
        "Kayıt: **611 (borç) 2.500** + 391 (borç) 500 / 120 (alacak) 3.000. Satış sonrası iskonto brüt satışı azaltan indirim hesabına, KDV hariç tutarla yazılır; iskontoya düşen KDV hesaplanan KDV'den geri alınır.",
        'THP 611, 391, 120',
    ),
    # düzey 3
    '0034': patch(
        'İşletme ticari mal siparişi için satıcıya daha önce 5.000 ₺ avans ödemiş ve 159 Verilen Sipariş Avansları hesabına kaydetmiştir. Mallar 20.000 ₺ + %20 KDV faturayla teslim alınmış, avans mahsup edilmiş, kalan tutar satıcıya borç olarak kaydedilmiştir. Buna göre teslim kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '320 Satıcılar hesabı 24.000 ₺ alacaklandırılır',
            'B': '320 Satıcılar hesabı 15.000 ₺ alacaklandırılır',
            'C': '191 İndirilecek KDV hesabı 4.000 ₺ alacaklandırılır',
            'D': '159 Verilen Sipariş Avansları hesabı 5.000 ₺ borçlandırılır',
            'E': '320 Satıcılar hesabı 19.000 ₺ alacaklandırılır',
        },
        'E',
        'Kayıt: 153 (borç) 20.000 + 191 (borç) 4.000 / 159 (alacak) 5.000 + **320 (alacak) 19.000**. Avans KDV dâhil toplamdan düşülür: 24.000 − 5.000.',
        'THP 159, 153, 191, 320',
    ),
    # düzey 3
    '0035': patch(
        'İşletme beş yıllığına kiraladığı yönetim binası için yaptığı 100.000 ₺ tutarındaki özel maliyeti kira süresine göre itfa etmektedir. Buna göre ilk yılın sonunda yapılacak itfa kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '264 Özel Maliyetler hesabı 20.000 ₺ alacaklandırılır',
            'B': '268 Birikmiş Amortismanlar hesabı 20.000 ₺ alacaklandırılır',
            'C': '257 Birikmiş Amortismanlar hesabı 20.000 ₺ alacaklandırılır',
            'D': '268 Birikmiş Amortismanlar hesabı 24.000 ₺ alacaklandırılır',
            'E': '770 Genel Yönetim Giderleri hesabı 20.000 ₺ alacaklandırılır',
        },
        'B',
        "VUK m. 327 uyarınca özel maliyet bedelleri kira süresi içinde eşit olarak itfa edilir: 100.000 / 5 = 20.000 ₺. Kayıt: 770 (borç) / **268 Birikmiş Amortismanlar (alacak) 20.000**. 26 grubunun düzenleyici hesabı 268'dir; 257 maddi duran varlıklara aittir.",
        'VUK m. 327; THP 268, 770',
    ),
    # düzey 2
    '0036': patch(
        'Bir işletmenin ay içindeki işlemleri incelenmektedir. Buna göre aşağıdaki işlemlerden hangisi 391 Hesaplanan KDV hesabının borçlandırılmasını gerektirmez?',
        {
            'A': 'Ay sonu KDV mahsubu yapılması',
            'B': 'Peşin mal satışı yapılması',
            'C': 'Satılan malların iade alınması',
            'D': 'Kesilmiş bir satış faturasının iptal edilmesi',
            'E': 'Satış sonrası iskonto faturası düzenlenmesi',
        },
        'B',
        "Satışta hesaplanan KDV 391'in **alacağına** yazılır. İade, sonradan iskonto ve fatura iptali daha önce hesaplanan KDV'yi azalttığından, ay sonu mahsubu ise hesabı kapattığından 391 borçlandırılır.",
        'THP 391',
    ),
    # düzey 3
    '0037': patch(
        'Bir işletmenin yevmiye defterinde şu kayıt yer almaktadır: 153 Ticari Mallar (borç) 50.000 + 191 İndirilecek KDV (borç) 10.000 / 121 Alacak Senetleri (alacak) 60.000. Buna göre bu kayıt aşağıdaki işlemlerden hangisine aittir?',
        {
            'A': 'Müşteriden alınan senedin vadesinde tahsil edilmesi',
            'B': 'Satıcıya borç senedi verilerek ticari mal alınması',
            'C': 'Ticari mal satışında müşteriden senet alınması',
            'D': 'Ticari mal alış bedelinin müşteri senedi ciro edilerek ödenmesi',
            'E': 'Alış iadesi karşılığında satıcıdan senet alınması',
        },
        'D',
        "Borçta ticari mal ve indirilecek KDV bulunduğu için işlem bir **alıştır**. 121 Alacak Senetleri'nin alacaklandırılması, portföydeki müşteri senedinin satıcıya ciro edildiğini gösterir. Borç senedi verilseydi 321 Borç Senetleri alacaklandırılırdı.",
        'THP 153, 191, 121',
    ),
    # düzey 3
    '0038': patch(
        'İşletme vadeli sattığı mal için alıcıya 2.000 ₺ + %20 KDV tutarında vade farkı faturası düzenlemiş ve tutarı alıcının cari hesabına borç kaydetmiştir. Buna göre kayıtla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '642 Faiz Gelirleri hesabı 2.000 ₺ alacaklandırılır',
            'B': '120 Alıcılar hesabı 2.000 ₺ borçlandırılır',
            'C': '600 Yurt İçi Satışlar hesabı 2.000 ₺ alacaklandırılır',
            'D': '649 Diğer Olağan Gelir ve Kârlar hesabı 2.400 ₺ alacaklandırılır',
            'E': '391 Hesaplanan KDV hesabı 400 ₺ borçlandırılır',
        },
        'A',
        'Vade farkı bir finansman gelirdir ve KDV matrahına girer: 120 (borç) 2.400 / **642 Faiz Gelirleri (alacak) 2.000** + 391 (alacak) 400.',
        '3065 sayılı KDVK m. 24; THP 120, 642, 391',
    ),
    # düzey 2
    '0039': patch(
        'KDV ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İthalatta gümrükte ödenen KDV malın maliyetine eklenir.\n\nII. Esas faaliyeti kiralama veya satış olmayan işletmenin binek otomobil alımında ödediği KDV indirilemez.\n\nIII. Satış iadesinde 391 Hesaplanan KDV hesabı alacaklandırılır.',
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'Yalnız II',
            'D': 'I, II ve III',
            'E': 'I ve II',
        },
        'C',
        "Yalnız II doğrudur (KDVK m. 30/b; KDV maliyete eklenir). İthalatta ödenen KDV 191'e alınıp indirilir; satış iadesinde daha önce hesaplanan KDV geri alındığı için 391 **borçlandırılır**.",
        '3065 sayılı KDVK m. 30/b; THP 191, 254',
    ),
    # düzey 3
    '0040': patch(
        "İşletme liste fiyatı 80.000 ₺ olan ticari malı, fatura üzerinde %5 iskontoyla satın almıştır. Satıcı aynı faturada 2.000 ₺ nakliye bedeli de göstermiştir. Tüm tutarlar %20 KDV'ye tabidir. Buna göre satıcıya ödenecek toplam tutar kaç ₺'dir?",
        {
            'A': '93.600 ₺',
            'B': '98.400 ₺',
            'C': '91.200 ₺',
            'D': '93.200 ₺',
            'E': '78.000 ₺',
        },
        'A',
        "Matrah: 80.000 × %95 + 2.000 = 78.000 ₺ (fatura üzerindeki iskonto matrahtan düşülür, nakliye matraha eklenir). KDV 15.600 ₺; toplam **93.600 ₺**. Stok maliyeti 78.000 ₺'dir.",
        '3065 sayılı KDVK m. 20, 24; VUK m. 262',
    ),
    # düzey 2
    '0041': patch(
        'İşletme, maliyeti kayıtlı ticari malı 60.000 ₺ + %20 KDV bedelle satmış ve karşılığında müşteriden senet almıştır. Satış hasılatı kaydında (maliyet kaydı hariç) aşağıdakilerden hangisi yer alır?',
        {
            'A': '121 Alacak Senetleri (borç) 72.000; 600 Yurtiçi Satışlar (alacak) 72.000',
            'B': '121 Alacak Senetleri (borç) 72.000; 600 Yurtiçi Satışlar (alacak) 60.000 ve 191 İndirilecek KDV (alacak) 12.000',
            'C': '121 Alacak Senetleri (borç) 60.000 ve 191 İndirilecek KDV (borç) 12.000; 600 Yurtiçi Satışlar (alacak) 72.000',
            'D': '120 Alıcılar (borç) 72.000; 600 Yurtiçi Satışlar (alacak) 60.000 ve 391 Hesaplanan KDV (alacak) 12.000',
            'E': '121 Alacak Senetleri (borç) 72.000; 600 Yurtiçi Satışlar (alacak) 60.000 ve 391 Hesaplanan KDV (alacak) 12.000',
        },
        'E',
        "Senet karşılığı satışta alacak **121 Alacak Senetleri** ile izlenir (açık hesap 120 değil). Senet 121 (borç) 72.000 ₺; hasılat 600 (alacak) 60.000 ₺; satış KDV'si 391 (alacak) 60.000 × %20 = 12.000 ₺. Satışta 191 değil 391 çalışır.",
        "3065 sayılı KDVK md 20; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 121/600/391",
    ),
    # düzey 2
    '0042': patch(
        "İşletme yurt dışından 100.000 ₺ gümrük kıymetiyle ticari mal ithal etmiş; ithalatta hesaplanan %20 KDV gümrükte bankadan ödenmiştir (malın kendi bedeli ayrıca kaydedilmiştir). Yalnızca gümrükte ödenen KDV'nin kaydı aşağıdakilerden hangisidir?",
        {
            'A': '191 İndirilecek KDV (borç) 20.000; 102 Bankalar (alacak) 20.000',
            'B': '191 İndirilecek KDV (borç) 20.000; 391 Hesaplanan KDV (alacak) 20.000',
            'C': '153 Ticari Mallar (borç) 20.000; 102 Bankalar (alacak) 20.000',
            'D': '391 Hesaplanan KDV (borç) 20.000; 102 Bankalar (alacak) 20.000',
            'E': '770 Genel Yönetim Giderleri (borç) 20.000; 102 Bankalar (alacak) 20.000',
        },
        'A',
        "Mal ithali KDV'nin konusuna girer; gümrükte ödenen KDV belgeye dayanarak **191 İndirilecek KDV**'ye alınır ve genel esaslara göre indirilir: 100.000 × %20 = 20.000 ₺ → 191 (borç) / 102 (alacak). İthalatta 391 çalışmaz; KDV malın maliyetine (153) eklenmez, indirilebilir.",
        "3065 sayılı KDVK md 1/2; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 191/102",
    ),
    # düzey 2
    '0043': patch(
        'Faaliyeti araç kiralama olmayan bir işletme 400.000 ₺ + %20 KDV bedelle binek otomobil almıştır (bedel bankadan ödenmiştir). 3065 sayılı Kanun md 30 uyarınca doğru kayıt hangisidir?',
        {
            'A': '153 TİCARİ MALLAR 400.000 ₺ (borç) / 191 İNDİRİLECEK KDV 80.000 ₺ (borç) / 102 BANKALAR 480.000 ₺ (alacak)',
            'B': '254 TAŞITLAR 400.000 ₺ (borç) / 391 HESAPLANAN KDV 80.000 ₺ (alacak) / 102 BANKALAR 400.000 ₺ (alacak)',
            'C': '254 TAŞITLAR 480.000 ₺ (borç) / 102 BANKALAR 480.000 ₺ (alacak)',
            'D': '770 GENEL YÖNETİM GİD. 80.000 ₺ (borç) / 254 TAŞITLAR 400.000 ₺ (borç) / 102 BANKALAR 480.000 ₺ (alacak)',
            'E': '254 TAŞITLAR 400.000 ₺ (borç) / 191 İNDİRİLECEK KDV 80.000 ₺ (borç) / 102 BANKALAR 480.000 ₺ (alacak)',
        },
        'C',
        "Binek oto alış KDV'si indirilemediğinden (md 30/b) **taşıtın maliyetine eklenir**: 254 TAŞITLAR (borç) 480.000 ₺ / 102 (alacak) 480.000 ₺. KDV ayrı 191'e alınıp indirilmez; alışta 391 çalışmaz.",
        '3065 s. KDVK md 30/b / TDHP 254',
    ),
    # düzey 2
    '0044': patch(
        'İşletme, vadeli sattığı mal için müşteriye ayrıca vade farkı faturası düzenlemiştir. Bu vade farkının KDV karşısındaki durumu bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Vade farkı matraha dahildir; malın oranı üzerinden KDV hesaplanır.',
            'B': 'Vade farkı gelir vergisine tabidir; KDV kapsamı dışındadır.',
            'C': 'Vade farkı satış iadesi gibi kabul edilip 391 borçlandırılır.',
            'D': 'Vade farkı üzerinden %20 KDV hesaplanır; malın oranı dikkate alınmaz.',
            'E': "Vade farkı bir finansman geliri olduğundan KDV'ye tabi değildir.",
        },
        'A',
        'Teslim/hizmet bedeliyle ilgili vade farkı, matrahın bir unsuru sayılır; **teslimin tabi olduğu KDV oranı** üzerinden hesaplanır (md 24). Her durumda %20 uygulanmaz; malın oranı esas alınır. Vade farkı iade değildir.',
        '3065 sayılı KDVK md 24',
    ),
    # düzey 2
    '0045': patch(
        "Bir giyim mağazasının gün sonu ödeme kaydedici cihaz raporunda, tamamı %20 KDV'ye tabi ürünlerden oluşan KDV dâhil 36.000 ₺ nakit hasılat yer almaktadır.\n\nBu hasılat nedeniyle 600 YURTİÇİ SATIŞLAR'a yazılacak tutar (matrah) kaç ₺'dir?",
        {
            'A': '36.000 ₺',
            'B': '43.200 ₺',
            'C': '7.200 ₺',
            'D': '6.000 ₺',
            'E': '30.000 ₺',
        },
        'E',
        "KDV dahil tutar (1 + oran)'a bölünür: 36.000 ₺ ÷ 1,20 = **30.000 ₺** (matrah = 600'e yazılır). Hesaplanan KDV = 36.000 ₺ − 30.000 ₺ = 6.000 ₺ (391).",
        '3065 s. KDVK md 20 (iç yüzde)',
    ),
    # düzey 2
    '0046': patch(
        "İşletme bir ayda 200.000 ₺ (%20) tutarında satış ve 150.000 ₺ (%20) ile 40.000 ₺ (%10) tutarında iki alış yapmıştır. Önceki dönemden devir yoktur. Bu ay ödenecek KDV kaç ₺'dir?",
        {
            'A': '40.000 ₺',
            'B': '10.000 ₺',
            'C': '34.000 ₺',
            'D': '6.000 ₺',
            'E': '5.000 ₺',
        },
        'D',
        "Hesaplanan KDV = 200.000 × %20 = 40.000 ₺. İndirilecek KDV = (150.000 × %20) + (40.000 × %10) = 30.000 + 4.000 = 34.000 ₺. Ödenecek = 40.000 − 34.000 = **6.000 ₺**. İkinci alışı da %20 saymak indirilecek KDV'yi ve sonucu değiştirir.",
        "3065 sayılı KDVK md 29; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 391/191/360",
    ),
    # düzey 2
    '0047': patch(
        "Ay sonu itibarıyla 391 Hesaplanan KDV 30.000 ₺, 191 İndirilecek KDV 18.000 ₺'dir. Ayrıca önceki dönemden devreden 190 Devreden KDV 5.000 ₺ bulunmaktadır. Bu ayın KDV mahsup (tahakkuk) kaydı aşağıdakilerden hangisidir?",
        {
            'A': '391 Hesaplanan KDV (borç) 30.000; 191 İndirilecek KDV (alacak) 18.000 ve 360 Ödenecek Vergi ve Fonlar (alacak) 12.000',
            'B': '391 Hesaplanan KDV (borç) 30.000; 191 İndirilecek KDV (alacak) 18.000 ve 190 Devreden KDV (alacak) 5.000 ve 360 Ödenecek Vergi ve Fonlar (alacak) 7.000',
            'C': '360 Ödenecek Vergi ve Fonlar (borç) 12.000; 391 Hesaplanan KDV (alacak) 12.000',
            'D': '391 Hesaplanan KDV (borç) 30.000; 191 İndirilecek KDV (alacak) 23.000 ve 360 Ödenecek Vergi ve Fonlar (alacak) 7.000',
            'E': '391 Hesaplanan KDV (borç) 30.000 ve 190 Devreden KDV (borç) 5.000; 191 İndirilecek KDV (alacak) 18.000 ve 360 Ödenecek Vergi ve Fonlar (alacak) 17.000',
        },
        'B',
        "Önceki dönem devreden KDV (190), bu ayın indirilecekleri gibi hesaplanan KDV'den düşülür. Mahsupta 391 (borç) 30.000 kapatılır; 191 (alacak) 18.000 ve önceki 190 (alacak) 5.000 kullanılır; kalan ödenecek 30.000 − 18.000 − 5.000 = 7.000 ₺ → 360 (alacak). Borç 30.000 = alacak (18.000 + 5.000 + 7.000). Devreden ihmal edilirse ödenecek 12.000 ₺ sanılır.",
        "3065 sayılı KDVK md 29/2; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 391/191/190/360",
    ),
    # düzey 2
    '0048': patch(
        "İşletmenin bir ay içinde 191 İndirilecek KDV hesabının borcuna toplam 24.000 ₺ yazılmıştır. Aynı ay, daha önce alınan bir maldan yapılan alış iadesi nedeniyle 191 hesabının alacağına 4.000 ₺ kaydedilmiştir. Ay sonunda (mahsup öncesi) 191 İndirilecek KDV hesabının borç kalanı kaç ₺'dir?",
        {
            'A': '20.000 ₺',
            'B': '24.000 ₺',
            'C': '4.000 ₺',
            'D': '0 ₺',
            'E': '28.000 ₺',
        },
        'A',
        "Alış iadesinde 191 alacaklandırılarak azaltılır. Borç kalanı = borç toplamı − alacak toplamı = 24.000 − 4.000 = **20.000 ₺**. İade tutarını eklemek (28.000) yön hatasıdır; iade indirilecek KDV'yi düşürür.",
        "3065 sayılı KDVK md 35; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 191",
    ),
    # düzey 2
    '0049': patch(
        'Daha önce veresiye alınan maldan 5.000 ₺ + %20 KDV tutarındaki kısım satıcıya iade edilmiştir (alış iadesi). Doğru kayıt hangisidir?',
        {
            'A': '610 SATIŞTAN İADELER 5.000 ₺ (borç) / 191 İND. KDV 1.000 ₺ (borç) / 320 SATICILAR 6.000 ₺ (alacak)',
            'B': '320 SATICILAR 6.000 ₺ (borç) / 153 TİCARİ MALLAR 5.000 ₺ (alacak) / 391 HESAPLANAN KDV 1.000 ₺ (alacak)',
            'C': '153 TİCARİ MALLAR 5.000 ₺ (borç) / 191 İNDİRİLECEK KDV 1.000 ₺ (borç) / 320 SATICILAR 6.000 ₺ (alacak)',
            'D': '320 SATICILAR 5.000 ₺ (borç) / 153 TİCARİ MALLAR 6.000 ₺ (alacak)',
            'E': '320 SATICILAR 6.000 ₺ (borç) / 153 TİCARİ MALLAR 5.000 ₺ (alacak) / 191 İNDİRİLECEK KDV 1.000 ₺ (alacak)',
        },
        'E',
        'Alış iadesi ilk kaydı ters çevirir: borç azaldığından **320 (borç) 6.000 ₺**; mal çıkışı **153 (alacak) 5.000 ₺**; daha önce yüklenilen KDV geri alınır **191 (alacak) 1.000 ₺**. Alış iadesinde 391 değil 191 ters çalışır.',
        '3065 s. KDVK md 35 (matrahta değişiklik) / TDHP 320-153-191',
    ),
    # düzey 2
    '0050': patch(
        "İndirilebilen KDV'nin malın maliyetine eklenmemesiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'İndirilebilen KDV 191 hesabında izlenir',
            'B': 'İndirilebilen KDV malın nihai maliyetinin bir parçasıdır',
            'C': "İndirilecek KDV hesaplanan KDV'den mahsup edilir",
            'D': 'İndirimi mümkün olmayan KDV maliyete eklenebilir',
            'E': "KDV'nin yükü kural olarak nihai tüketiciye aittir",
        },
        'B',
        "İndirilebilen KDV işletme için nihai bir maliyet değildir; 191'de izlenir ve hesaplanan KDV'den indirilir. Vergi yükü nihai tüketiciye aittir. İndirimi mümkün olmayan KDV (KDVK m. 30) ise maliyete veya gidere eklenebilir.",
        '3065 s. KDVK md 29/58',
    ),
    # düzey 2
    '0051': patch(
        "Mart ayı sonunda indirilecek KDV hesaplanan KDV'yi aştığı için işletmenin 190 Devreden KDV hesabında 12.000 ₺ kalmıştır. Nisan ayında ise hesaplanan KDV, indirimleri aştığından 8.000 ₺ ödenecek KDV 360 Ödenecek Vergi ve Fonlar hesabına aktarılmıştır.\n\n190 Devreden KDV ile 360 Ödenecek Vergi ve Fonlar hesaplarının niteliği bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İkisi de pasif hesaptır ve vergi dairesine olan borcu gösterir.',
            'B': 'İkisi de gelir tablosu hesabıdır ve dönem kârını doğrudan etkiler.',
            'C': '190 pasif, 360 aktif bir hesaptır.',
            'D': '190 aktif, 360 ise pasif karakterli bir hesaptır.',
            'E': 'İkisi de aktif hesaptır ve vergi dairesinden alacağı gösterir.',
        },
        'D',
        "İndirilecek KDV hesaplanan KDV'yi aştığında fark **190 Devreden KDV** (aktif) olur; hesaplanan indirilecekten fazlaysa fark **360 Ödenecek Vergi ve Fonlar** (pasif) olur. Aynı dönemde ikisi birden doğmaz; her ikisi de bilanço hesabıdır.",
        "3065 sayılı KDVK md 29; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 190/360",
    ),
    # düzey 2
    '0052': patch(
        "Önceki aydan 3.000 ₺ devreden KDV'si bulunan işletme ay içinde CIF değeri 100.000 ₺ olan bir ticari malı ithal etmiş; ithalat sırasında 10.000 ₺ gümrük vergisi ödenmiş ve KDV gümrükte ödenmiştir. Ayrıca yurt içinden 50.000 ₺ + %20 KDV mal alınmış, 200.000 ₺ + %20 KDV satış yapılmıştır. Tüm işlemler %20 KDV'ye tabidir.\n\nBuna göre ay sonunda ödenecek KDV kaç ₺'dir?",
        {
            'A': '7.000',
            'B': '5.000',
            'C': '8.000',
            'D': '27.000',
            'E': '2.000',
        },
        'B',
        "İthalatta KDV matrahı CIF değer ile gümrük vergisinin toplamıdır: (100.000 + 10.000) × %20 = 22.000 ₺; gümrükte ödenen KDV 191'e alınır. Hesaplanan KDV 40.000 ₺; indirimler 22.000 + 10.000 + 3.000 = 35.000 ₺; ödenecek KDV 5.000 ₺.",
        "3065 sayılı KDVK md 29/2; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 190",
    ),
    # düzey 3
    '0053': patch(
        'Stoklarını aralıklı envanter yöntemiyle izleyen işletme, kredili aldığı ticari malların 12.000 ₺ + %20 KDV tutarındaki kısmını satıcıya iade etmiş ve tutar satıcıya olan borcundan düşülmüştür. Buna göre iade kaydında aşağıdakilerden hangisi yer almaz?',
        {
            'A': 'Kaydın borç ve alacak toplamları 14.400 ₺ olarak eşitlenir',
            'B': '320 Satıcılar hesabı 14.400 ₺ borçlandırılır',
            'C': '191 İndirilecek KDV hesabı 2.400 ₺ borçlandırılır',
            'D': '153 Ticari Mallar hesabı 12.000 ₺ alacaklandırılır',
            'E': '191 İndirilecek KDV hesabı 2.400 ₺ alacaklandırılır',
        },
        'C',
        "Kayıt: 320 (borç) 14.400 / 153 (alacak) 12.000 + 191 (alacak) 2.400. Alışta indirilecek KDV'ye yazılan tutar iadede geri alınır; 191 **alacaklandırılır**.",
        'THP 320, 153, 191',
    ),
    # düzey 3
    '0054': patch(
        'İşletme müşterisinden bir sipariş için 30.000 ₺ avans almış ve 340 Alınan Sipariş Avansları hesabına kaydetmiştir. Mallar 150.000 ₺ + %20 KDV bedelle teslim edilmiş, avans mahsup edilmiş, kalan tutar için müşteriden çek alınmıştır. Buna göre teslim kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '101 Alınan Çekler hesabı 180.000 ₺ borçlandırılır',
            'B': '600 Yurt İçi Satışlar hesabı 180.000 ₺ alacaklandırılır',
            'C': '391 Hesaplanan KDV hesabı 30.000 ₺ borçlandırılır',
            'D': '340 Alınan Sipariş Avansları hesabı 30.000 ₺ alacaklandırılır',
            'E': '101 Alınan Çekler hesabı 150.000 ₺ borçlandırılır',
        },
        'E',
        "Kayıt: 340 (borç) 30.000 + **101 (borç) 150.000** / 600 (alacak) 150.000 + 391 (alacak) 30.000. Alınan avans teslimde 340'ın borcuna yazılarak kapatılır; KDV teslim üzerinden hesaplanır.",
        'THP 340, 101, 600, 391',
    ),
    # düzey 3
    '0055': patch(
        'İşletme beş yıllığına kiraladığı mağazaya 150.000 ₺ (KDV hariç) özel maliyet harcaması yapmış ve iki yıl boyunca kira süresine göre itfa etmiştir. Üçüncü yılın başında kira süresi dolmadan mağazayı tahliye etmiştir. Buna göre tahliye kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '689 Diğer Olağandışı Gider ve Zararlar hesabı 150.000 ₺ borçlandırılır',
            'B': '689 Diğer Olağandışı Gider ve Zararlar hesabı 90.000 ₺ borçlandırılır',
            'C': '257 Birikmiş Amortismanlar hesabı 60.000 ₺ borçlandırılır',
            'D': '264 Özel Maliyetler hesabı 90.000 ₺ alacaklandırılır',
            'E': '268 Birikmiş Amortismanlar hesabı 90.000 ₺ borçlandırılır',
        },
        'B',
        'İki yılda 60.000 ₺ itfa edilmiştir; kalan 90.000 ₺ tahliyeyle gider olur. Kayıt: 268 (borç) 60.000 + **689 (borç) 90.000** / 264 (alacak) 150.000.',
        'VUK m. 327; THP 264, 268, 689',
    ),
    # düzey 3
    '0056': patch(
        "Ay sonunda 391 Hesaplanan KDV hesabının alacak kalanı 78.000 ₺, 191 İndirilecek KDV hesabının borç kalanı 75.000 ₺'dir. Önceki aydan 190 Devreden KDV hesabında 7.000 ₺ bulunmaktadır. Ay sonu mahsup kaydıyla ilgilire aşağıdakilerden hangisi yanlıştır?",
        {
            'A': '360 Ödenecek Vergi ve Fonlar hesabı 3.000 ₺ alacaklandırılır',
            'B': '191 İndirilecek KDV hesabı 75.000 ₺ alacaklandırılır',
            'C': 'Mahsup sonrasında sonraki aya devreden KDV 4.000 ₺ olur',
            'D': '190 Devreden KDV hesabı 3.000 ₺ alacaklandırılır',
            'E': '391 Hesaplanan KDV hesabı 78.000 ₺ borçlandırılır',
        },
        'A',
        "Hesaplanan KDV indirilecek KDV'yi 3.000 ₺ aşmaktadır; bu fark önce devreden KDV'den mahsup edilir: 391 (borç) 78.000 / 191 (alacak) 75.000 + 190 (alacak) 3.000. Devreden 7.000 ₺ farkı karşıladığından **ödenecek KDV doğmaz**; 360 kullanılmaz, 4.000 ₺ sonraki aya devreder.",
        '3065 sayılı KDVK m. 29; THP 391, 191, 190, 360',
    ),
    # düzey 3
    '0057': patch(
        "İşletme yönetim katında kullanmak üzere %20 KDV dâhil 72.000 ₺'ye toplantı masası takımı almıştır. Bedelin 30.000 ₺'si için portföydeki bir müşteri senedi ciro edilmiş, kalanı bankadan havale edilmiştir. Buna göre yapılacak kayıtla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '191 İndirilecek KDV hesabı 12.000 ₺ alacaklandırılır',
            'B': '255 Demirbaşlar hesabı 72.000 ₺ borçlandırılır',
            'C': '102 Bankalar hesabı 36.000 ₺ alacaklandırılır',
            'D': '255 Demirbaşlar hesabı 60.000 ₺ borçlandırılır',
            'E': '121 Alacak Senetleri hesabı 36.000 ₺ alacaklandırılır',
        },
        'D',
        'KDV dâhil tutardan matrah: 72.000 / 1,20 = 60.000 ₺; KDV 12.000 ₺. Kayıt: **255 (borç) 60.000** + 191 (borç) 12.000 / 121 (alacak) 30.000 + 102 (alacak) 42.000.',
        'THP 255, 191, 121, 102',
    ),
    # düzey 2
    '0058': patch(
        "Bir işletme müşterisine mal teslim etmeden önce satış faturasını düzenlemiştir. Buna göre KDV'de vergiyi doğuran olayla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Fatura tarihinde, faturada gösterilen tutarla sınırlı olarak doğar',
            'B': 'Satış bedelinin tamamının tahsil edildiği tarihte doğar',
            'C': 'Malın teslim edildiği tarihte doğar',
            'D': 'Ay sonu KDV mahsubunun yapıldığı tarihte doğar',
            'E': 'Beyannamenin verildiği tarihte doğar',
        },
        'A',
        'KDVK m. 10 uyarınca teslimden önce fatura düzenlenirse vergiyi doğuran olay **fatura tarihinde**, faturada gösterilen miktarla sınırlı olarak meydana gelir.',
        '3065 sayılı KDVK m. 10',
    ),
    # düzey 3
    '0059': patch(
        "Esas faaliyeti ticaret olan bir işletme ay içinde şu alışları yapmıştır: 80.000 ₺ + %20 KDV ticari mal, 30.000 ₺ + %20 KDV demirbaş ve 200.000 ₺ + %20 KDV binek otomobil. Ayrıca aynı ay aldığı ticari malların 10.000 ₺ + %20 KDV'lik kısmını iade etmiştir. Buna göre ay sonunda 191 İndirilecek KDV hesabının borç kalanı kaç ₺'dir?",
        {
            'A': '14.000 ₺',
            'B': '24.000 ₺',
            'C': '60.000 ₺',
            'D': '22.000 ₺',
            'E': '20.000 ₺',
        },
        'E',
        "Binek otomobil KDV'si indirilemez, otomobilin maliyetine eklenir. 191: (80.000 + 30.000) × %20 − iade 2.000 = **20.000 ₺**.",
        '3065 sayılı KDVK m. 29-30; THP 191',
    ),
    # düzey 3
    '0060': patch(
        "İhracat da yapan bir ticaret işletmesinin ay içindeki işlemleri şöyledir: yurt dışındaki bir alıcıya 500.000 ₺ tutarında mal ihraç edilmiştir (KDV'den istisna), yurt içinde 100.000 ₺ + %20 KDV mal satılmıştır, 300.000 ₺ + %20 KDV ticari mal alınmıştır. Önceki aydan devreden KDV yoktur ve işletme bu ay KDV iadesi talep etmeyecektir.\n\nBuna göre ay sonu mahsubundan sonra izleyen aya devreden KDV kaç ₺'dir?",
        {
            'A': '20.000',
            'B': '60.000',
            'C': '80.000',
            'D': '100.000',
            'E': '40.000',
        },
        'E',
        "İhracat KDV'den istisnadır; hesaplanan KDV yalnız yurt içi satıştan doğar: 20.000 ₺. İstisnalı işlemlere ait yüklenilen KDV de indirilebilir; indirilecek KDV 60.000 ₺. 60.000 − 20.000 = 40.000 ₺ izleyen aya devreder (iade talep edilmediği için).",
        '3065 sayılı KDVK m. 29; THP 391, 191, 190',
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
    print(f"1 paket / {len(PATCHES)} soru ('KDV Muhasebesi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
