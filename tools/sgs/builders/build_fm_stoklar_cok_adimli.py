#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stoklar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

FM cok adimli tur. 42 soru korundu; tms_2 paketiyle cakisan 11 TMS 2 sorusu, bir kopya soru ve ezber sorulari cikarildi. Yerine gercek sinav kalibinda 18 soru: alis gideri, iade ve iskontolarla SMM, brut kar marjiyla donem sonu stok tahmini, FIFO / hareketli ortalama / donemsel agirlikli ortalama, cek+senet+nakitle satista aralikli ve surekli envanter kayitlari, 153 hesap toplamlarindan SMM, alis ve satis nakliyesinin ayrimi, sigortali stok kaybi, brut satis kari. Bagimsiz aritmetik dogrulama bir tasarim hatasini yakaladi (agirlikli ortalama 9.125 -> 8.875). Kor ogrenci %20.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: VUK m. 262, 274 · 1 Sira No'lu MSUGT (stoklar) · Tekduzen Hesap Plani 15, 60-62, 197, 689, 760
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/finansal_muhasebe/stoklar.json"
STYLE_REF = 'SGS Finansal Muhasebe (çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "finmuh-stok-gen-"


def patch(stem, options, answer, solution, ref="1 Sira No'lu MSUGT - Stoklar"):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Aralıklı (dönemsel) envanter yöntemi ile sürekli envanter yöntemi arasındaki fark ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sürekli envanterde her satışta hem satış hasılatı hem de satılan malın maliyeti kaydedilir.',
            'B': "Aralıklı envanterde dönem içinde '153 Ticari Mallar' hesabı kullanılmaz.",
            'C': "Aralıklı envanterde her satışta '621 Satılan Ticari Malların Maliyeti' çalıştırılır.",
            'D': 'Sürekli envanterde satış anında satılan malın maliyeti kaydedilmez.',
            'E': 'İki yöntem de dönem sonunda aynı defter kayıt sayısını üretir.',
        },
        'A',
        '**Sürekli envanter** yönteminde her satışta iki kayıt yapılır: (1) hasılat kaydı, (2) satılan malın maliyeti kaydı (**621 (borç) / 153 (alacak)**). **Aralıklı** yöntemde ise satılan malın maliyeti dönem sonunda toplu olarak hesaplanır (DBM + Alışlar − DSM).',
        "1 Sıra No'lu MSUGT - Stok maliyetleme yöntemleri",
    ),
    # düzey 2
    '0002': patch(
        "Bir ticari mal kaleminin dönem hareketleri şöyledir:\n\n| Tarih | İşlem | Miktar | Birim Maliyet |\n|---|---|---|---|\n| 01.03 | Dönem başı | 200 br | 20 ₺ |\n| 10.03 | Alış | 300 br | 24 ₺ |\n| 20.03 | Satış | 350 br | — |\n\nİlk giren ilk çıkar (FIFO) yöntemine göre 20.03 satışının maliyeti kaç ₺'dir?",
        {
            'A': '11.200',
            'B': '7.840',
            'C': '7.600',
            'D': '8.400',
            'E': '8.200',
        },
        'C',
        "FIFO'da önce giren stok önce satılır. 350 birimin maliyeti: 200 × 20 = 4.000 ve kalan 150 × 24 = 3.600 → **4.000 + 3.600 = 7.600 ₺**. Dönem sonu stok = 150 × 24 = 3.600 ₺.",
        "TMS 2 Stoklar; 1 Sıra No'lu MSUGT - FIFO",
    ),
    # düzey 2
    '0003': patch(
        "İşletme liste fiyatı 100.000 ₺ olan ticari malı üç ay vadeyle 106.000 ₺'ye satın almıştır. Mal için ayrıca 2.000 ₺ nakliye, 500 ₺ taşıma sigortası ve 800 ₺ yükleme-boşaltma ücreti ödenmiştir.\n\nAşağıdakilerden hangisi satın alınan ticari malın stok maliyetine dâhil edilmez?",
        {
            'A': 'Alışa ilişkin yükleme-boşaltma giderleri',
            'B': 'Malın alış bedeli',
            'C': 'İşletmeye taşıma (navlun) gideri',
            'D': 'Sigorta ve gümrük vergisi gibi alışla doğrudan ilgili giderler',
            'E': 'Vadeli alıştan kaynaklanan finansman (vade farkı) gideri',
        },
        'E',
        'Stok maliyetine; alış bedeli, navlun, sigorta, gümrük ve alışla doğrudan ilgili giderler **dâhildir**. Ancak **vadeli alıştan doğan finansman (vade farkı) gideri** stok maliyetine alınmaz; finansman gideri olarak sonuç hesaplarına yansıtılır (TMS 2).',
        'TMS 2 Stoklar; VUK md. 274 (stok maliyeti unsurları)',
    ),
    # düzey 2
    '0004': patch(
        "İşletmenin dönem sonunda üç stok kalemi bulunmaktadır: X malının maliyeti 50.000 ₺, net gerçekleşebilir değeri 44.000 ₺; Y malının maliyeti 30.000 ₺, net gerçekleşebilir değeri 33.000 ₺; Z malının maliyeti 40.000 ₺, net gerçekleşebilir değeri 35.000 ₺'dir. Önceki dönemde X ve Z malları için toplam 4.000 ₺ stok değer düşüklüğü karşılığı ayrılmıştır ve mallar hâlâ eldedir. Karşılık kalem bazında belirlenmektedir.\n\nBuna göre dönem sonunda yapılacak kayıt aşağıdakilerden hangisidir?",
        {
            'A': '654 Karşılık Giderleri (borç) 11.000 / 158 Stok Değer Düşüklüğü Karşılığı (alacak) 11.000',
            'B': '654 Karşılık Giderleri (borç) 7.000 / 158 Stok Değer Düşüklüğü Karşılığı (alacak) 7.000',
            'C': '654 Karşılık Giderleri (borç) 4.000 / 158 Stok Değer Düşüklüğü Karşılığı (alacak) 4.000',
            'D': '158 Stok Değer Düşüklüğü Karşılığı (borç) 7.000 / 644 Konusu Kalmayan Karşılıklar (alacak) 7.000',
            'E': '654 Karşılık Giderleri (borç) 7.000 / 153 Ticari Mallar (alacak) 7.000',
        },
        'B',
        "Kalem bazında gereken karşılık: X 6.000 ₺, Z 5.000 ₺, toplam 11.000 ₺; Y'nin NGD'si maliyetin üzerinde olduğundan artış dikkate alınmaz ve düşüşlerle netleştirilmez. Mevcut karşılık 4.000 ₺ olduğundan 7.000 ₺ ek karşılık ayrılır: 654 borç / 158 alacak.",
        "TMS 2 Stoklar; 1 Sıra No'lu MSUGT - 158 / 654",
    ),
    # düzey 2
    '0005': patch(
        'Üretim işletmesinin stoklarıyla ilgili aşağıdaki hesap eşleştirmelerinden hangisi yanlıştır?',
        {
            'A': '151 Yarı Mamuller — Üretim — henüz tamamlanmamış üretim',
            'B': '152 Mamuller — üretilip satışa hazır ürünler',
            'C': '153 Ticari Mallar — üretilmeden alınıp satılan mallar',
            'D': '157 Diğer Stoklar — işletmenin ürettiği ana mamul',
            'E': '150 İlk Madde ve Malzeme — üretimde kullanılacak hammadde',
        },
        'D',
        '**157 Diğer Stoklar**, yukarıdaki gruplara girmeyen (hurda, artık vb.) stoklar içindir; işletmenin ürettiği **ana mamul 152 Mamuller** hesabında izlenir. Diğer eşleştirmeler doğrudur.',
        "1 Sıra No'lu MSUGT - Stoklar grubu (15) hesapları",
    ),
    # düzey 2
    '0006': patch(
        "Stok maliyet akış yöntemlerinden 'hareketli ağırlıklı ortalama' yöntemiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Her yeni alıştan sonra ortalama birim maliyet yeniden hesaplanır',
            'B': 'Ortalama birim maliyet dönem sonunda bir kez hesaplanır',
            'C': 'Satışlar o anki ortalama birim maliyetle maliyetlendirilir',
            'D': 'Yöntem sürekli envanter sistemiyle birlikte uygulanır',
            'E': 'Ortalama, alışların miktar ve tutar ağırlığını dikkate alır',
        },
        'B',
        'Hareketli ağırlıklı ortalama yönteminde her yeni alıştan sonra ortalama birim maliyet yeniden hesaplanır ve satışlar o anki ortalamayla maliyetlendirilir; bu nedenle sürekli envanter sistemiyle uygulanır. Dönem sonunda tek bir ortalama hesaplanması (dönemsel) tartılı ortalama yöntemidir.',
        'TMS 2 Stoklar; ağırlıklı ortalama yöntemleri',
    ),
    # düzey 2
    '0007': patch(
        "Bir ticari mal kaleminin hareketleri şöyledir:\n\n| Tarih | İşlem | Miktar | Birim Maliyet |\n|---|---|---|---|\n| 01.05 | Dönem başı | 100 br | 15 ₺ |\n| 09.05 | Alış | 200 br | 18 ₺ |\n| 17.05 | Alış | 100 br | 20 ₺ |\n| 24.05 | Satış | 250 br | — |\n\nİlk giren ilk çıkar (FIFO) yöntemine göre dönem sonu stok mevcudunun değeri kaç ₺'dir?",
        {
            'A': '2.900',
            'B': '4.200',
            'C': '3.300',
            'D': '7.100',
            'E': '3.000',
        },
        'A',
        "Toplam mevcut 400 br, maliyet 1.500 + 3.600 + 2.000 = 7.100 ₺. FIFO'da 250 br satılır (100×15 + 150×18). Kalan 150 br: 50×18 + 100×20 = 900 + 2.000 = **2.900 ₺**.",
        'TMS 2 Stoklar - FIFO',
    ),
    # düzey 2
    '0008': patch(
        'İşletmenin deposunda çıkan yangın sonucu, sigortasız olan 30.000 ₺ maliyetli ticari mal tamamen kullanılamaz hâle gelmiştir. Bu anormal zayi ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Stok değer düşüklüğü karşılığı ayrılır; ilgili malın stok çıkışı ise yapılmaz.',
            'B': 'Herhangi bir gider yazılmadan doğrudan dönem kârına eklenerek kapatılır.',
            'C': 'Zayi olan malın maliyeti dönemin satılan malın maliyetine eklenerek sonuca aktarılır.',
            'D': 'Olağandışı gider/zarar (ör. 689) olarak sonuç hesaplarına yansıtılır ve stok azaltılır.',
            'E': 'Kalan sağlam stokların birim maliyetine dağıtılır ve ayrıca sonuç hesaplarına yansıtılmaz.',
        },
        'D',
        'Yangın gibi **anormal (olağandışı) zayi**, faaliyetin normal sonucu değildir; kalan stoka dağıtılmaz. İlgili stok çıkarılır ve tutar **olağandışı gider/zarar** olarak (ör. 689) sonuç hesaplarına yansıtılır (sigorta varsa tazminat ayrıca dikkate alınır).',
        "TMS 2; 1 Sıra No'lu MSUGT - anormal zayi",
    ),
    # düzey 2
    '0009': patch(
        "Sürekli envanter ve FIFO yöntemini uygulayan işletmenin bir ticari mal kalemindeki hareketler şöyledir: dönem başı stok 200 birim × 20 ₺; 5 Mart'ta 300 birim × 24 ₺ alış; 10 Nisan'da 350 birim satış; 20 Mayıs'ta 400 birim × 27 ₺ alış; 15 Haziran'da 20 Mayıs alışından 50 birimin kusurlu olduğu için satıcıya iadesi; 1 Ekim'de 300 birim satış.\n\nBuna göre dönem sonu stokunun maliyeti kaç ₺'dir?",
        {
            'A': '5.200',
            'B': '4.800',
            'C': '5.400',
            'D': '6.750',
            'E': '5.000',
        },
        'C',
        '10 Nisan satışı: 200 × 20 + 150 × 24 = 7.600 ₺; elde 150 birim × 24 ₺ kalır. 20 Mayıs alışından 50 birim iade edilince bu katman 350 birim × 27 ₺ olur. 1 Ekim satışı: 150 × 24 + 150 × 27 = 7.650 ₺. Dönem sonunda 200 birim × 27 ₺ = 5.400 ₺ kalır.',
        'TMS 2 Stoklar - FIFO',
    ),
    # düzey 2
    '0010': patch(
        'Bir işletmenin dönem sonu stokları 18.000 ₺ fazla sayılmıştır. Alışlar ve satışlar doğru kaydedilmiş, hata izleyen dönemde tekrarlanmamıştır.\n\nBu hatanın etkileriyle ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Cari dönemin satılan mal maliyeti 18.000 ₺ eksik hesaplanır',
            'B': 'Cari dönem kârı 18.000 ₺ fazla hesaplanır',
            'C': 'İzleyen dönemin dönem başı stoku 18.000 ₺ fazla olur',
            'D': 'İzleyen dönem kârı 18.000 ₺ eksik hesaplanır',
            'E': 'İki dönemin toplam kârı 18.000 ₺ fazla hesaplanır',
        },
        'E',
        "Dönem sonu stok fazlalığı cari dönemde SMM'yi 18.000 ₺ azaltır, kârı 18.000 ₺ artırır. Bu stok izleyen dönemin dönem başı stoku olduğundan izleyen dönemde SMM 18.000 ₺ fazla, kâr 18.000 ₺ eksik çıkar. Hata kendiliğinden dengelenir; iki dönemin toplam kârı doğrudur.",
        'Muhasebe Süreci - dönem başı stok + alışlar - dönem sonu stok eşitliği',
    ),
    # düzey 2
    '0011': patch(
        '7/A seçeneğini uygulayan bir üretim işletmesinde, üretim bölümünün malzeme istek fişiyle ambardan 80.000 ₺ tutarında hammadde üretime sevk edilmiştir.\n\nİlk madde ve malzemenin ambardan üretime sevk edilmesiyle ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '600 Yurt İçi Satışlar hesabı alacaklandırılır; 150 İlk Madde ve Malzeme hesabı borçlandırılır.',
            'B': '150 İlk Madde ve Malzeme hesabı borçlandırılır; ilgili gider/maliyet hesabı alacaklandırılır.',
            'C': '150 İlk Madde ve Malzeme hesabı alacaklandırılır; ilgili gider/maliyet hesabı borçlandırılır.',
            'D': 'Sevk miktar olarak izlenir; bu aşamada yevmiye kaydı yapılmaz.',
            'E': '153 Ticari Mallar hesabı borçlandırılır; 150 İlk Madde ve Malzeme hesabı alacaklandırılır.',
        },
        'C',
        'Malzeme üretime verildiğinde stoktan çıkar: **150 İlk Madde ve Malzeme alacaklandırılır**; tutar ilgili maliyet/gider hesabına (ör. 710 Direkt İlk Madde ve Malzeme Giderleri) borç yazılır. Böylece hammadde maliyetlere aktarılır.',
        "1 Sıra No'lu MSUGT - 150 / 710 (7/A)",
    ),
    # düzey 2
    '0012': patch(
        'İşletme, ileride teslim alacağı ticari mallar için satıcısına 40.000 ₺ sipariş avansını banka yoluyla ödemiştir (mallar henüz teslim alınmamıştır).\n\nBu işlemle ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ödeme gününde 153 Ticari Mallar hesabı 40.000 ₺ borçlandırılır',
            'B': '159 Verilen Sipariş Avansları hesabı 40.000 ₺ borçlandırılır',
            'C': '102 Bankalar hesabı 40.000 ₺ alacaklandırılır',
            'D': 'Mallar teslim alındığında 159 hesabı alacaklandırılır',
            'E': 'Verilen avans bilançoda stoklar grubunda yer alır',
        },
        'A',
        'Mallar teslim alınmadan ödenen avans 159 Verilen Sipariş Avansları hesabına borç, 102 Bankalar hesabına alacak yazılır; 159 stoklar grubunda (15) yer alır. Mallar teslim alındığında 153 borçlandırılır, 159 kapatılır. Ödeme gününde 153 çalışmaz.',
        "1 Sıra No'lu MSUGT - 159 Verilen Sipariş Avansları",
    ),
    # düzey 2
    '0013': patch(
        "Aralıklı envanter ve dönemsel tartılı ortalama maliyet yöntemini uygulayan işletmenin bir ticari mal kaleminde dönem başı stoku 200 birim × 25 ₺'dir. Dönem içinde 300 birim × 30 ₺ ve 500 birim × 33 ₺ olmak üzere iki alış yapılmış, toplam 700 birim satılmıştır.\n\nBuna göre dönem sonu stok mevcudunun değeri kaç ₺'dir?",
        {
            'A': '9.900',
            'B': '9.150',
            'C': '8.000',
            'D': '8.700',
            'E': '9.300',
        },
        'B',
        'Satışa hazır mal: 1.000 birim, 5.000 + 9.000 + 16.500 = 30.500 ₺; tartılı ortalama birim maliyet 30,50 ₺. Dönem sonu mevcut 1.000 − 700 = 300 birim; değeri 300 × 30,50 = 9.150 ₺.',
        'TMS 2 Stoklar - ağırlıklı ortalama',
    ),
    # düzey 2
    '0014': patch(
        "Sürekli envanter yöntemini kullanan işletmede '153 Ticari Mallar' hesabının kaydi kalanı 60.000 ₺ iken, dönem sonu fiilî sayımda 63.000 ₺ mal tespit edilmiş ve fazlalığın nedeni belirlenememiştir.\n\nBuna göre yapılacak kayıt aşağıdakilerden hangisidir?",
        {
            'A': '397 Sayım ve Tesellüm Fazlaları (borç) 3.000 / 153 Ticari Mallar (alacak) 3.000',
            'B': '197 Sayım ve Tesellüm Noksanları (borç) 3.000 / 153 Ticari Mallar (alacak) 3.000',
            'C': '621 Satılan Ticari Malların Maliyeti (borç) 3.000 / 153 Ticari Mallar (alacak) 3.000',
            'D': '153 Ticari Mallar (borç) 63.000 / 600 Yurt İçi Satışlar (alacak) 63.000',
            'E': '153 Ticari Mallar (borç) 3.000 / 397 Sayım ve Tesellüm Fazlaları (alacak) 3.000',
        },
        'E',
        'Fiilî mevcut (63.000) kaydi mevcuttan (60.000) **3.000 ₺ fazladır**; stok fazlası vardır. Nedeni bulunana kadar: **153 Ticari Mallar (borç) 3.000 / 397 Sayım ve Tesellüm Fazlaları (alacak) 3.000**. Neden belirlenince 397 kapatılır.',
        "1 Sıra No'lu MSUGT - 397 Sayım ve Tesellüm Fazlaları",
    ),
    # düzey 3
    '0015': patch(
        "Stoklarını aralıklı envanter yöntemiyle izleyen ve fire bulunmayan bir işletmenin dönem bilgileri şöyledir: dönem başı ticari mal 210.000 ₺, dönem içi alışlar 790.000 ₺, alış giderleri 50.000 ₺, alış iadeleri 150.000 ₺, alış iskontoları 20.000 ₺, satış iadeleri 60.000 ₺ ve dönem sonu sayımla belirlenen ticari mal 400.000 ₺. Buna göre satılan ticari malların maliyeti kaç ₺'dir?",
        {
            'A': '420.000 ₺',
            'B': '430.000 ₺',
            'C': '500.000 ₺',
            'D': '480.000 ₺',
            'E': '780.000 ₺',
        },
        'D',
        'SMM = dönem başı + alışlar + alış giderleri − alış iadeleri − alış iskontoları − dönem sonu = 210.000 + 790.000 + 50.000 − 150.000 − 20.000 − 400.000 = **480.000 ₺**. Satış iadeleri hasılatı düzelttiği için SMM hesabına girmez.',
        'Aralıklı envanter; THP 153, 621',
    ),
    # düzey 3
    '0016': patch(
        "Bilgisayar satışı yapan ve stoklarını sürekli envanter yöntemiyle izleyen işletme, satış amacıyla aldığı ve maliyeti 12.000 ₺ olan bir dizüstü bilgisayarı, muhasebe biriminde demirbaş olarak kullanmak üzere stoktan ayırmıştır. Bilgisayarın aynı tarihteki satış fiyatı 15.000 ₺'dir ve alışında yüklenilen KDV indirim konusu yapılmıştır.\n\nBu işlemin kaydı aşağıdakilerden hangisidir?",
        {
            'A': '255 Demirbaşlar 15.000 ₺ borç / 153 Ticari Mallar 15.000 ₺ alacak',
            'B': '770 Genel Yönetim Giderleri 12.000 ₺ borç / 153 Ticari Mallar 12.000 ₺ alacak',
            'C': '255 Demirbaşlar 12.000 ₺ ve 191 İndirilecek KDV 2.400 ₺ borç / 153 Ticari Mallar 14.400 ₺ alacak',
            'D': '621 Satılan Ticari Mallar Maliyeti 12.000 ₺ borç / 153 Ticari Mallar 12.000 ₺ alacak',
            'E': '255 Demirbaşlar 12.000 ₺ borç / 153 Ticari Mallar 12.000 ₺ alacak',
        },
        'E',
        'Ticari malın işletmede birden fazla dönem kullanılmak üzere demirbaşa aktarılması bir satış değildir; mal maliyet bedeliyle stoktan çıkarılıp duran varlığa alınır: 255 borç / 153 alacak 12.000 ₺. İşletmenin kendi faaliyetinde kullanılması teslim sayılmadığından hesaplanan KDV doğmaz; bilgisayar bundan sonra amortismana tabi tutulur.',
        "1 Sıra No'lu MSUGT; hareketli ağırlıklı ortalama",
    ),
    # düzey 3
    '0017': patch(
        "İşletme liste fiyatı 400.000 ₺ olan ticari malı fatura üzerinde %5 iskontoyla satın almıştır. Mal depoya gelinceye kadar 12.000 ₺ nakliye, 3.000 ₺ yolda sigorta ödenmiş ve alımda aracılık eden kişiye 4.000 ₺ komisyon verilmiştir. Mal depoya girdikten sonra satılana kadar 5.000 ₺ depolama gideri oluşmuştur (KDV ihmal). Buna göre ticari malın maliyet bedeli kaç ₺'dir?",
        {
            'A': '419.000 ₺',
            'B': '394.000 ₺',
            'C': '478.800 ₺',
            'D': '399.000 ₺',
            'E': '395.000 ₺',
        },
        'D',
        'Alış bedeli 400.000 × %95 = 380.000 ₺; depoya girişe kadarki nakliye, sigorta ve alım komisyonu eklenir: **399.000 ₺**. Depoya girdikten sonraki depolama gideri dönem gideridir.',
        "VUK m. 262, 274; 1 Sıra No'lu MSUGT",
    ),
    # düzey 3
    '0018': patch(
        'Stoklarla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Aralıklı envanter yönteminde satılan malın maliyeti dönem sonunda bulunur.\n\nII. Sürekli envanter yönteminde satış iadesinde 153 Ticari Mallar borçlandırılır.\n\nIII. Alış iskontosu stok maliyetini artırır.',
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'Yalnız II',
            'D': 'I ve III',
            'E': 'II ve III',
        },
        'A',
        'I ve II doğrudur. III yanlıştır: alış iskontosu **stok maliyetini azaltır**.',
        'Stok yöntemleri; THP 153, 621',
    ),
    # düzey 3
    '0019': patch(
        "Bir işletmenin dönem bilgileri şöyledir: yurt içi satışlar 900.000 ₺, satıştan iadeler 40.000 ₺, satış iskontoları 20.000 ₺, satılan ticari mallar maliyeti 520.000 ₺ ve genel yönetim giderleri 70.000 ₺. Buna göre brüt satış kârı kaç ₺'dir?",
        {
            'A': '300.000 ₺',
            'B': '320.000 ₺',
            'C': '250.000 ₺',
            'D': '260.000 ₺',
            'E': '840.000 ₺',
        },
        'B',
        'Net satışlar 900.000 − 40.000 − 20.000 = 840.000 ₺; brüt satış kârı 840.000 − 520.000 = **320.000 ₺**. Genel yönetim giderleri faaliyet giderleridir; brüt satış kârından sonra düşülür.',
        'Gelir tablosu; THP 60, 61, 62',
    ),
    # düzey 2
    '0020': patch(
        'Bir ticaret işletmesinin ticari mal alımı ve satışı sırasında yaptığı harcamalar şunlardır: alış nakliyesi, yolda sigorta, gümrük vergisi, alım komisyonu ve satılan malın müşteriye taşınması. Buna göre aşağıdakilerden hangisi ticari malın maliyetine eklenmez?',
        {
            'A': 'Alım komisyonu',
            'B': 'Yolda sigorta',
            'C': 'Satılan malın müşteriye taşınması',
            'D': 'Alış nakliyesi',
            'E': 'Gümrük vergisi',
        },
        'C',
        'Malın depoya girişine kadarki alış nakliyesi, yolda sigorta, gümrük vergisi ve alım komisyonu maliyete eklenir. Satılan malın müşteriye taşınması **satış gideridir** (760).',
        "VUK m. 262; 1 Sıra No'lu MSUGT",
    ),
    # düzey 2
    '0021': patch(
        "Aralıklı envanter yöntemini kullanan bir işletmenin dönem başı ticari mal mevcudu 40.000 ₺, dönem içi ticari mal alışları toplamı 260.000 ₺ ve fiilî sayımla belirlenen dönem sonu ticari mal mevcudu 55.000 ₺'dir.\n\nBuna göre dönemde satılan ticari malların maliyeti (SMM) kaç ₺'dir?",
        {
            'A': '245.000',
            'B': '135.000',
            'C': '190.000',
            'D': '215.000',
            'E': '260.000',
        },
        'A',
        'SMM = Dönem Başı Mevcut + Dönem Alışları − Dönem Sonu Mevcut = 40.000 + 260.000 − 55.000 = **245.000 ₺**. Aralıklı yöntemde bu tutar dönem sonunda **621 (borç) / 153 (alacak)** kaydıyla maliyete alınır.',
        "1 Sıra No'lu MSUGT - SMM hesaplaması (aralıklı envanter)",
    ),
    # düzey 2
    '0022': patch(
        "Bir sanat galerisi, maliyetleri sırasıyla 18.000 ₺, 22.000 ₺, 27.000 ₺ ve 33.000 ₺ olan ve her biri ayrı seri numarasıyla izlenen dört eserden 22.000 ₺ ve 33.000 ₺ maliyetli olanları satmıştır. TMS 2'deki gerçek parti maliyeti (özel maliyet) yöntemine göre satılan eserlerin maliyeti kaç ₺'dir?",
        {
            'A': '60.000 ₺',
            'B': '49.000 ₺',
            'C': '45.000 ₺',
            'D': '55.000 ₺',
            'E': '40.000 ₺',
        },
        'D',
        'Birbirinin yerine kullanılamayan ve ayrı ayrı izlenebilen stoklarda maliyet, satılan belirli birimlerle eşleştirilir. Satılan iki eserin maliyeti 22.000 + 33.000 = **55.000 ₺**dir; diğer eserlerin ortalaması kullanılmaz.',
        'TMS 2 Stoklar, par. 23',
    ),
    # düzey 2
    '0023': patch(
        "Sürekli envanter yöntemini kullanan işletme tanesi 1.000 ₺ liste fiyatlı 50 adet ticari malı, faturada gösterilen %10 ticari iskonto ve %20 KDV ile veresiye satın almıştır. Malların depoya taşınması için nakliyeciye 2.000 ₺ + %20 KDV ödenmiştir. Ertesi gün 5 adet malın kusurlu olduğu anlaşılmış ve bunlar satıcıya iade edilmiştir; nakliye bedeli iade edilmemiştir.\n\nBuna göre bu işlemlerden sonra '153 Ticari Mallar' hesabının bu mallara ilişkin kalanı kaç ₺'dir?",
        {
            'A': '45.000',
            'B': '42.500',
            'C': '47.000',
            'D': '42.700',
            'E': '40.500',
        },
        'B',
        'Alış: 50 × 1.000 × 0,90 = 45.000 ₺; alış nakliyesi maliyete eklenir: +2.000 ₺. İade edilen 5 adet iskontolu bedelle çıkarılır: 5 × 900 = 4.500 ₺ (320 borç / 153 ve 191 alacak). 153 kalanı = 45.000 + 2.000 − 4.500 = 42.500 ₺.',
        '3065 s. KDV Kanunu; 191 İndirilecek KDV; 2026 KDV %20',
    ),
    # düzey 2
    '0024': patch(
        "Sürekli envanter yöntemini uygulayan işletmede '153 Ticari Mallar' hesabının borç kalanı 90.000 ₺ iken, dönem sonu fiilî sayımda mevcut 84.000 ₺ olarak belirlenmiş ve noksanlığın nedeni araştırılmaya karar verilmiştir.\n\nNedeni henüz belirlenmemişken yapılması gereken kayıt aşağıdakilerden hangisidir?",
        {
            'A': '158 Stok Değer Düşüklüğü Karşılığı (borç) 6.000 / 153 Ticari Mallar (alacak) 6.000',
            'B': '621 Satılan Ticari Malların Maliyeti (borç) 6.000 / 153 Ticari Mallar (alacak) 6.000',
            'C': '197 Sayım ve Tesellüm Noksanları (borç) 6.000 / 153 Ticari Mallar (alacak) 6.000',
            'D': '689 Diğer Olağandışı Gider (borç) 84.000 / 153 Ticari Mallar (alacak) 84.000',
            'E': '153 Ticari Mallar (borç) 6.000 / 397 Sayım ve Tesellüm Fazlaları (alacak) 6.000',
        },
        'C',
        'Kaydi mevcut (90.000) fiilî mevcuttan (84.000) **6.000 ₺ fazladır**; stok noksanı vardır. Nedeni bulunana kadar **197 Sayım ve Tesellüm Noksanları (borç) 6.000 / 153 Ticari Mallar (alacak) 6.000** kaydıyla stok fiili duruma indirilir; neden belirlenince 197 kapatılır.',
        "1 Sıra No'lu MSUGT - 197 Sayım ve Tesellüm Noksanları",
    ),
    # düzey 2
    '0025': patch(
        "Bir işletme, liste fiyatı 200.000 ₺ olan ticari malı 10.000 ₺ ticari iskonto sonrası satın almıştır. Malın işletme stoklarına girdiği tarihe kadar 8.000 ₺ nakliye, 2.000 ₺ sigorta ve bu alımın finansmanında kullanılan krediye ilişkin 4.000 ₺ faiz gideri oluşmuştur. İndirilebilir KDV dikkate alınmayacaktır.\n\nVUK'un güncel 262 ve 274'üncü maddelerine göre emtianın maliyet bedeli kaç ₺'dir?",
        {
            'A': '198.000 ₺',
            'B': '200.000 ₺',
            'C': '214.000 ₺',
            'D': '190.000 ₺',
            'E': '204.000 ₺',
        },
        'E',
        "Net alış bedeli 200.000 − 10.000 = 190.000 ₺'dir. VUK 262 uyarınca emtianın stoklara girdiği tarihe kadarki nakliye, sigorta ve kredi faizi maliyete dâhildir: 190.000 + 8.000 + 2.000 + 4.000 = **204.000 ₺**. Bu vergi değerlemesi, TMS 2'deki vadeli satın alma finansman unsurundan ayrı değerlendirilir.",
        '213 sayılı VUK md. 262 ve 274 (7338 sayılı Kanun sonrası güncel metin)',
    ),
    # düzey 2
    '0026': patch(
        "Sürekli envanter yönteminde dönem sonunda '153 Ticari Mallar' hesabının kaydi kalanı ile fiilî sayım sonucu birbirine eşitse, bu durumla ilgili aşağıdakilerden hangisi söylenebilir?",
        {
            'A': 'Aradaki farka bakılmaksızın mutlaka stok değer düşüklüğü karşılığı ayrılır.',
            'B': 'Sayım noksanı/fazlası kaydı (197 veya 397) yapılmasına gerek yoktur.',
            'C': "'621 Satılan Ticari Malların Maliyeti' hesabı ters kayıtla kapatılmalıdır.",
            'D': 'Dönem içinde yapılan tüm satış kayıtlarının hatalı olduğu kabul edilir.',
            'E': 'Ticari mallar bilançoda maliyet yerine güncel satış fiyatıyla gösterilir.',
        },
        'B',
        'Kaydi kalan ile fiilî mevcut eşitse stok farkı yoktur; bu nedenle **sayım noksanı (197) veya fazlası (397) kaydına gerek yoktur**. Değer düşüklüğü ise ayrı bir değerleme konusudur ve yalnızca NGD maliyetin altındaysa gündeme gelir.',
        "1 Sıra No'lu MSUGT - Sürekli envanterde dönem sonu kontrol",
    ),
    # düzey 2
    '0027': patch(
        "İşletme dönem içinde 200.000 ₺'lik ticari mal satın almış; bu mallar için 6.000 ₺ nakliye (navlun) gideri ödemiş ve satın aldığı malların 10.000 ₺'lik kısmını satıcıya iade etmiştir.\n\nBuna göre stok maliyetine giren net alış tutarı kaç ₺'dir?",
        {
            'A': '196.000',
            'B': '200.000',
            'C': '190.000',
            'D': '216.000',
            'E': '206.000',
        },
        'A',
        'Navlun stok maliyetine eklenir, iade düşülür: 200.000 + 6.000 − 10.000 = **196.000 ₺**.',
        'TMS 2; VUK md. 274 (stok maliyet unsurları)',
    ),
    # düzey 2
    '0028': patch(
        'Önceki dönemde stokları için 16.000 ₺ değer düşüklüğü karşılığı ayıran işletme, bu dönem söz konusu stokların net gerçekleşebilir değerinin maliyetin üzerine çıktığını belirlemiş ve ayrılan karşılığın konusu kalmamıştır.\n\nKarşılığın iptaline ilişkin kayıt aşağıdakilerden hangisidir?',
        {
            'A': '689 Diğer Olağandışı Gider (borç) 16.000 / 153 Ticari Mallar (alacak) 16.000',
            'B': '654 Karşılık Giderleri (borç) 16.000 / 158 Stok Değer Düşüklüğü Karşılığı (alacak) 16.000',
            'C': '158 Stok Değer Düşüklüğü Karşılığı (borç) 16.000 / 153 Ticari Mallar (alacak) 16.000',
            'D': '158 Stok Değer Düşüklüğü Karşılığı (borç) 16.000 / 644 Konusu Kalmayan Karşılıklar (alacak) 16.000',
            'E': '153 Ticari Mallar (borç) 16.000 / 600 Yurt İçi Satışlar (alacak) 16.000',
        },
        'D',
        'Konusu kalmayan karşılık, bir gelir olarak iptal edilir: **158 Stok Değer Düşüklüğü Karşılığı (borç) 16.000 / 644 Konusu Kalmayan Karşılıklar (alacak) 16.000**. 644 bir gelir hesabıdır.',
        "1 Sıra No'lu MSUGT - 644 Konusu Kalmayan Karşılıklar",
    ),
    # düzey 2
    '0029': patch(
        'Aşağıdakilerden hangileri satın alınan ticari malın stok maliyetine dâhil edilir?\n\nI. İşletmenin genel yönetim giderleri\n\nII. Alışa ilişkin navlun ve sigorta giderleri\n\nIII. Satış ve pazarlama giderleri\n\nIV. İthalatta ödenen gümrük vergisi',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'I, II, III ve IV',
            'E': 'II ve IV',
        },
        'E',
        'Alışla **doğrudan** ilgili navlun, sigorta (II) ve gümrük vergisi (IV) stok maliyetine girer. **Genel yönetim giderleri (I)** ve **satış/pazarlama giderleri (III)** stok maliyetine alınmaz; dönem gideri yazılır (TMS 2).',
        'TMS 2 Stoklar - maliyete girmeyen giderler',
    ),
    # düzey 2
    '0030': patch(
        'Bir ticari mal kaleminde dönem başı mevcut 400 birimdir. Dönem içinde 1.200 birim alınmış, 1.300 birim satılmış, satılan mallardan 50 birim müşterilerce iade edilmiş, alınan mallardan 30 birim satıcıya iade edilmiş ve 20 birim normal fire olarak kayıtlardan çıkarılmıştır. Dönem sonu fiilî sayımda 290 birim mal bulunmuştur.\n\nBuna göre kayıtlara göre olması gereken mevcut ve sayım farkı aşağıdakilerden hangisidir?',
        {
            'A': '320 birim olmalı; 30 birim sayım noksanı vardır',
            'B': '270 birim olmalı; 20 birim sayım fazlası vardır',
            'C': '250 birim olmalı; 40 birim sayım fazlası vardır',
            'D': '300 birim olmalı; 10 birim sayım noksanı vardır',
            'E': '300 birim olmalı; 10 birim sayım fazlası vardır',
        },
        'D',
        "Olması gereken mevcut = 400 + 1.200 − 1.300 + 50 (satış iadesi) − 30 (alış iadesi) − 20 (fire) = 300 birim. Sayımda 290 birim bulunduğundan 10 birimlik sayım noksanı vardır; nedeni araştırılıncaya kadar 197 Sayım ve Tesellüm Noksanları'nda izlenir.",
        "1 Sıra No'lu MSUGT - Stok miktar dengesi",
    ),
    # düzey 2
    '0031': patch(
        "Satıcı, 28 Aralık'ta malları FOB varış (teslim) noktası koşuluyla müşteriye göndermiştir. Mallar 31 Aralık'ta hâlâ yolda olup müşteriye 3 Ocak'ta teslim edilmiştir. Dönem sonu stok kesimi bakımından en uygun işlem hangisidir?",
        {
            'A': 'Mallar taşıma süresince iki işletmenin stokunda da gösterilmez.',
            'B': "Teslim 3 Ocak'ta gerçekleştiğinden mallar 31 Aralık'ta satıcının stoklarında kalır.",
            'C': 'Malların yarısı satıcının, yarısı müşterinin stokunda gösterilir.',
            'D': 'Nakliye işletmesi malları kendi ticari malı olarak kaydeder.',
            'E': "Mallar 28 Aralık'ta müşterinin stoklarına alınır; satıcı stoktan çıkarır.",
        },
        'B',
        "FOB **varış noktası** koşulunda kontrol, risk ve mülkiyet teslim noktasına ulaşılıncaya kadar satıcıda kalır. Mallar 31 Aralık'ta henüz teslim edilmediği için satıcının dönem sonu stoklarına dâhil edilir; müşteri 3 Ocak'ta kaydeder.",
        'Dönemsellik ve stok sayımı - FOB varış noktası teslim koşulu',
    ),
    # düzey 2
    '0032': patch(
        "Bir mal, satıcı işletmenin deposundan 'FOB yükleme (teslim) noktası' koşuluyla sevk edilmiş ve dönem sonunda hâlâ yoldadır. Bu yoldaki mal, dönem sonu stok sayımında kimin stoğuna dâhil edilir?",
        {
            'A': 'Satıcının stoğuna',
            'B': 'Her ikisinin stoğuna yarı yarıya',
            'C': 'Nakliye firmasının stoğuna',
            'D': 'Hiçbirinin stoğuna',
            'E': 'Alıcının stoğuna',
        },
        'E',
        '**FOB yükleme (teslim) noktası** koşulunda mülkiyet ve riskler malın yüklendiği anda **alıcıya** geçer. Bu nedenle yoldaki mal, dönem sonunda **alıcının** stoklarına dâhil edilir (özün önceliği).',
        'TMS 2; teslim koşulları (FOB) ve mülkiyet',
    ),
    # düzey 2
    '0033': patch(
        "Dönem başı ticari mal stoku 60.000 ₺, net alışlar 340.000 ₺ ve net satışlar 500.000 ₺'dir. İşletmenin satışlar üzerinden brüt kâr oranı %30'dur. Brüt kâr yöntemine göre tahmini dönem sonu stok tutarı kaç ₺'dir?",
        {
            'A': '50.000 ₺',
            'B': '350.000 ₺',
            'C': '400.000 ₺',
            'D': '90.000 ₺',
            'E': '150.000 ₺',
        },
        'A',
        'Tahmini brüt kâr 500.000 × %30 = 150.000 ₺; tahmini satılan malın maliyeti 500.000 − 150.000 = **350.000 ₺**dir. Satışa hazır mallar 60.000 + 340.000 = 400.000 ₺ olduğundan dönem sonu stok 400.000 − 350.000 = **50.000 ₺**dir.',
        'Stok Envanteri - brüt kâr yöntemiyle tahmini stok hesabı',
    ),
    # düzey 2
    '0034': patch(
        'İşletme, veresiye sattığı 5.000 ₺ + %20 KDV tutarındaki malın müşteri tarafından iade edilmesini kabul etmiştir. Bu iadenin hasılat (satış) yönünü ilgilendiren kaydı aşağıdakilerden hangisidir?',
        {
            'A': '600 Yurt İçi Satışlar (borç) 6.000 / 120 Alıcılar (alacak) 6.000',
            'B': '610 Satıştan İadeler (borç) 5.000 + 191 İndirilecek KDV (borç) 1.000 / 120 Alıcılar (alacak) 6.000',
            'C': '610 Satıştan İadeler (borç) 6.000 / 100 Kasa (alacak) 6.000',
            'D': '610 Satıştan İadeler (borç) 5.000 + 391 Hesaplanan KDV (borç) 1.000 / 120 Alıcılar (alacak) 6.000',
            'E': '120 Alıcılar (borç) 6.000 / 610 Satıştan İadeler (alacak) 5.000 + 391 Hesaplanan KDV (alacak) 1.000',
        },
        'D',
        'Satıştan iadede satış geri alınır: **610 Satıştan İadeler (borç) 5.000** ve daha önce hesaplanan KDV düzeltilir **391 Hesaplanan KDV (borç) 1.000**; alıcının borcu azalır **120 Alıcılar (alacak) 6.000**. (Sürekli envanterde maliyet de ayrıca geri alınır: 153/621.)',
        "1 Sıra No'lu MSUGT - 610 Satıştan İadeler; 3065 s. KDVK",
    ),
    # düzey 3
    '0035': patch(
        "Bir işletmenin dönem başı ticari mal stoku 120.000 ₺, dönem içi alışları 300.000 ₺, satışları (satış fiyatıyla) 400.000 ₺ ve satıştan iadeleri (satış fiyatıyla) 50.000 ₺'dir. İşletme satış fiyatı üzerinden %20 brüt kâr marjıyla çalışmaktadır. Buna göre dönem sonu ticari mal stokunun tahmini maliyeti kaç ₺'dir?",
        {
            'A': '100.000 ₺',
            'B': '60.000 ₺',
            'C': '140.000 ₺',
            'D': '20.000 ₺',
            'E': '70.000 ₺',
        },
        'C',
        'Net satış 400.000 − 50.000 = 350.000 ₺; SMM = 350.000 × %80 = 280.000 ₺. Satışa hazır mal 120.000 + 300.000 = 420.000 ₺; dönem sonu stok 420.000 − 280.000 = **140.000 ₺**.',
        'Aralıklı envanter; brüt kâr marjı',
    ),
    # düzey 3
    '0036': patch(
        "Stoklarını aralıklı envanter yöntemiyle izleyen işletme, alış maliyeti 60.000 ₺ olan ticari malları 100.000 ₺ + %20 KDV bedelle satmıştır. Karşılığında 50.000 ₺'lik çek ve 40.000 ₺'lik senet almış, kalanı nakit tahsil etmiştir. Buna göre satış kaydında aşağıdakilerden hangisi yer almaz?",
        {
            'A': '391 Hesaplanan KDV hesabı 20.000 ₺ alacaklandırılır',
            'B': '121 Alacak Senetleri hesabı 40.000 ₺ borçlandırılır',
            'C': '101 Alınan Çekler hesabı 50.000 ₺ borçlandırılır',
            'D': '100 Kasa hesabı 30.000 ₺ borçlandırılır',
            'E': '621 Satılan Ticari Mallar Maliyeti hesabı 60.000 ₺ borçlandırılır',
        },
        'E',
        'Kayıt: 101 (borç) 50.000 + 121 (borç) 40.000 + 100 (borç) 30.000 / 600 (alacak) 100.000 + 391 (alacak) 20.000. **Aralıklı envanterde satış anında maliyet kaydı yapılmaz**; SMM dönem sonunda hesaplanır.',
        'Aralıklı envanter; THP 101, 121, 100, 600, 391',
    ),
    # düzey 2
    '0037': patch(
        'Bir işletme stoklarını aralıklı envanter yöntemiyle izlemektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Her satışta 153 alacaklandırılıp 621 borçlandırılır',
            'B': 'Satışta hasılat kaydedilir, maliyet kaydı yapılmaz',
            'C': "Alışlar 153 Ticari Mallar'ın borcuna yazılır",
            'D': 'Dönem sonu stok fiilî sayımla belirlenir',
            'E': 'Satılan malın maliyeti dönem sonunda hesaplanır',
        },
        'A',
        'Aralıklı envanterde satış anında maliyet kaydı yapılmaz; SMM dönem sonunda (dönem başı + net alışlar − sayımla bulunan dönem sonu) hesaplanır. Her satışta 153/621 kaydı **sürekli envanterin** özelliğidir.',
        'Aralıklı envanter; THP 153, 621',
    ),
    # düzey 3
    '0038': patch(
        "Aralıklı envanter yöntemini kullanan bir işletmenin 153 Ticari Mallar hesabının dönem sonundaki borç toplamı 1.800.000 ₺ (dönem başı mevcut 250.000 ₺ dâhil), alacak toplamı 100.000 ₺'dir. Dönem sonu sayımla belirlenen mal mevcudu 600.000 ₺'dir. Buna göre satılan ticari malların maliyeti kaç ₺'dir?",
        {
            'A': '1.350.000 ₺',
            'B': '1.700.000 ₺',
            'C': '850.000 ₺',
            'D': '1.100.000 ₺',
            'E': '1.200.000 ₺',
        },
        'D',
        "153'ün kalanı (1.800.000 − 100.000 = 1.700.000 ₺) satışa hazır malları gösterir; dönem başı mevcut borç toplamında zaten vardır. SMM = 1.700.000 − 600.000 = **1.100.000 ₺**.",
        'Aralıklı envanter; THP 153, 621',
    ),
    # düzey 3
    '0039': patch(
        'Bir ticaret işletmesi sattığı malların müşterinin deposuna teslimi için nakliye firmasına kendi hesabına 5.000 ₺ + %20 KDV nakit ödemiştir. Buna göre bu ödemenin kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '760 Pazarlama Satış ve Dağıtım Giderleri hesabı 6.000 ₺ borçlandırılır',
            'B': '760 Pazarlama Satış ve Dağıtım Giderleri hesabı 5.000 ₺ borçlandırılır',
            'C': '153 Ticari Mallar hesabı 5.000 ₺ borçlandırılır',
            'D': '621 Satılan Ticari Mallar Maliyeti hesabı 5.000 ₺ borçlandırılır',
            'E': '391 Hesaplanan KDV hesabı 1.000 ₺ alacaklandırılır',
        },
        'B',
        'Satış sırasında satıcının üstlendiği taşıma bir **satış gideridir**: 760 (borç) 5.000 + 191 (borç) 1.000 / 100 (alacak) 6.000. Stok maliyetine yalnız alış sırasındaki taşıma eklenir.',
        'THP 760, 191, 100',
    ),
    # düzey 3
    '0040': patch(
        "Aralıklı envanter yöntemini kullanan bir işletmede bir ticari mal kaleminin dönem başı stoku 200 birim × 30 ₺, dönem içi alışları 300 birim × 35 ₺ ve 500 birim × 38 ₺'dir. Dönem sonunda 250 birim stok sayılmıştır. İşletme dönemsel ağırlıklı ortalama yöntemini kullanmaktadır. Buna göre dönem sonu stok maliyeti kaç ₺'dir?",
        {
            'A': '9.125 ₺',
            'B': '9.500 ₺',
            'C': '8.875 ₺',
            'D': '9.000 ₺',
            'E': '7.750 ₺',
        },
        'C',
        "Toplam maliyet 200 × 30 + 300 × 35 + 500 × 38 = 6.000 + 10.500 + 19.000 = 35.500 ₺; 1.000 birim. Ortalama birim maliyet 35,5 ₺; dönem sonu stok **250 × 35,5 = 8.875 ₺**. FIFO'da (son alıştan) 250 × 38 = 9.500 ₺ olurdu.",
        "1 Sıra No'lu MSUGT; dönemsel ağırlıklı ortalama",
    ),
    # düzey 2
    '0041': patch(
        'Sürekli envanter yöntemini uygulayan işletme, maliyeti 18.000 ₺ olan ticari malı 25.000 ₺ + %20 KDV bedelle veresiye satmıştır.\n\nBuna göre satışın maliyetine ilişkin yapılması gereken kayıt aşağıdakilerden hangisidir?',
        {
            'A': '600 Yurt İçi Satışlar (borç) 25.000 / 153 Ticari Mallar (alacak) 25.000',
            'B': '621 Satılan Ticari Malların Maliyeti (borç) 25.000 / 153 Ticari Mallar (alacak) 25.000',
            'C': '153 Ticari Mallar (borç) 18.000 / 621 Satılan Ticari Malların Maliyeti (alacak) 18.000',
            'D': '621 Satılan Ticari Malların Maliyeti (borç) 18.000 / 153 Ticari Mallar (alacak) 18.000',
            'E': '621 Satılan Ticari Malların Maliyeti (borç) 30.000 / 153 Ticari Mallar (alacak) 30.000',
        },
        'D',
        'Sürekli envanterde satış maliyeti, malın **maliyet bedeli** (18.000 ₺) üzerinden kaydedilir: **621 (borç) 18.000 / 153 (alacak) 18.000**. Satış bedeli (25.000) ve KDV, ayrı hasılat kaydında (120/600/391) işlenir; maliyet kaydını etkilemez.',
        "1 Sıra No'lu MSUGT - 621 / 153 (sürekli envanter)",
    ),
    # düzey 2
    '0042': patch(
        'Birim alış fiyatlarının sürekli yükseldiği (enflasyonist) bir dönemde, FIFO yöntemi tartılı ortalama yöntemine kıyasla dönem sonuçlarını nasıl etkiler?',
        {
            'A': 'Dönem kârını ve stok değerini etkilemez; hesaplanan KDV tutarını değiştirir',
            'B': 'Satılan malın maliyeti, dönem kârı ve dönem sonu stok değeri her iki yöntemde de tamamen aynı çıkar',
            'C': 'Daha yüksek satılan malın maliyeti, daha düşük dönem kârı ve daha düşük dönem sonu stok değeri',
            'D': 'Daha yüksek satılan malın maliyeti ile birlikte daha düşük dönem sonu stok değeri ortaya çıkar',
            'E': 'Daha düşük satılan malın maliyeti, daha yüksek dönem kârı ve daha yüksek dönem sonu stok değeri',
        },
        'E',
        "Fiyatlar yükselirken FIFO'da satılan mallar **eski ve daha düşük maliyetli** birimlerden oluşur; bu nedenle ağırlıklı ortalamaya göre satılan malın maliyeti daha düşük, dönem kârı daha yüksek çıkar. Dönem sonu stok ise daha yeni ve pahalı birimlerden oluştuğu için daha yüksek değerlenir.",
        'TMS 2 Stoklar - maliyet akış varsayımlarının etkisi',
    ),
    # düzey 2
    '0043': patch(
        "Sürekli envanter yöntemini kullanan işletme, daha önce %20 KDV ile veresiye aldığı 8.000 ₺'lik (KDV hariç) ticari malı satıcısına iade etmiş; tutar borcundan düşülmüştür.\n\nBu iade işleminin kaydı aşağıdakilerden hangisidir?",
        {
            'A': '320 Satıcılar (borç) 9.600 / 153 Ticari Mallar (alacak) 8.000 + 191 İndirilecek KDV (alacak) 1.600',
            'B': '320 Satıcılar (borç) 8.000 / 153 Ticari Mallar (alacak) 8.000',
            'C': '621 Satılan Ticari Malların Maliyeti (borç) 9.600 / 320 Satıcılar (alacak) 9.600',
            'D': '610 Satıştan İadeler (borç) 8.000 / 320 Satıcılar (alacak) 8.000',
            'E': '153 Ticari Mallar (borç) 8.000 + 191 İndirilecek KDV (borç) 1.600 / 320 Satıcılar (alacak) 9.600',
        },
        'A',
        'Alış iadesinde ilk alış kaydı ters çevrilir: borç azaldığı için **320 Satıcılar (borç) 9.600**; stok çıktığı için **153 (alacak) 8.000** ve daha önce indirilen KDV düzeltildiği için **191 İndirilecek KDV (alacak) 1.600**.',
        "1 Sıra No'lu MSUGT - Alış iadesi (sürekli envanter); 3065 s. KDVK",
    ),
    # düzey 2
    '0044': patch(
        'Bir işletme, satılmak üzere kendisine bırakılan (konsinye) malları satıcı işletme adına elinde bulundurmaktadır.\n\nBu konsinye mallarla ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Mülkiyet, mallar satılıncaya kadar gönderende kalır',
            'B': 'Konsinye alan işletme malları nazım hesaplarda izleyebilir',
            'C': 'Mallar, konsinye alan işletmenin stoklarına dâhil edilir',
            'D': 'Mal satıldığında hasılatı gönderen işletme kaydeder',
            'E': 'Konsinye alan işletme satıştan komisyon elde eder',
        },
        'C',
        'Konsinye mallarda mülkiyet devredilmediğinden mallar gönderenin (konsinyatör) stoklarında kalır; konsinye alan işletme bunları kendi stoklarına almaz, nazım hesaplarda izleyebilir. Mal üçüncü kişiye satıldığında hasılat gönderende doğar, konsinye alan komisyon geliri elde eder.',
        'TMS 2 Stoklar; TTK - konsinye satış (mülkiyet)',
    ),
    # düzey 2
    '0045': patch(
        "Aralıklı envanter yöntemini kullanan işletme dönem içi alışlarını '153 Ticari Mallar' hesabının borcunda izlemektedir. Dönem sonunda satılan malın maliyetini belirlemek için yapılan işlem aşağıdakilerden hangisidir?",
        {
            'A': "'153 Ticari Mallar' hesabı dönem içinde kullanılmaz; alışlar doğrudan gider olarak sonuç hesaplarına yazılır.",
            'B': "Dönem sonu fiilî sayımla belirlenen mevcut esas alınarak satılan malın maliyeti hesaplanır ve '621 (borç) / 153 (alacak)' kaydı yapılır.",
            'C': 'Dönem sonu mevcut, maliyet bedeliyle değil güncel satış fiyatıyla değerlenir ve aradaki fark doğrudan gelir olarak yazılır.',
            'D': "Satılan malın maliyeti hesaplanmaz; tutar doğrudan '600 Yurt İçi Satışlar' hesabından indirilerek dönem sonucuna aktarılır.",
            'E': "Dönem içinde her satış anında satılan malın maliyeti '621 Satılan Ticari Malların Maliyeti (borç) / 153 (alacak)' kaydıyla ayrı ayrı işlenir.",
        },
        'B',
        'Aralıklı yöntemde satılan malın maliyeti dönem sonunda **fiilî sayımla** belirlenen mevcuda göre hesaplanır (DBM + Alışlar − DSM) ve tek kayıtla maliyete alınır: **621 (borç) / 153 (alacak)**. Dönem içi her satışta ayrı maliyet kaydı yapılmaz.',
        "1 Sıra No'lu MSUGT - Aralıklı envanterde dönem sonu maliyet kaydı",
    ),
    # düzey 2
    '0046': patch(
        "Hareketli ağırlıklı ortalama maliyet yöntemini kullanan işletmenin bir ticari mal kalemine ilişkin hareketleri şöyledir:\n\n| Tarih | İşlem | Miktar | Birim Maliyet |\n|---|---|---|---|\n| 01.04 | Dönem başı | 100 br | 20 ₺ |\n| 08.04 | Alış | 300 br | 24 ₺ |\n| 15.04 | Satış | 150 br | — |\n\nBuna göre 15.04 satışının maliyeti kaç ₺'dir?",
        {
            'A': '3.450',
            'B': '3.000',
            'C': '3.600',
            'D': '5.750',
            'E': '9.200',
        },
        'A',
        '08.04 alışından sonra güncel ortalama birim maliyet = (100 × 20 + 300 × 24) ÷ 400 = 9.200 ÷ 400 = **23 ₺**. 15.04 satışının maliyeti = 150 × 23 = **3.450 ₺**. Hareketli ortalamada her alıştan sonra ortalama güncellenir.',
        'TMS 2 Stoklar; hareketli ağırlıklı ortalama',
    ),
    # düzey 2
    '0047': patch(
        'Sürekli envanter yöntemini uygulayan işletmeye, daha önce sattığı maliyeti 4.000 ₺ olan mal müşteri tarafından iade edilmiştir. Bu iadenin maliyet yönünü ilgilendiren kaydı aşağıdakilerden hangisidir?',
        {
            'A': '153 Ticari Mallar (borç) 4.000 / 600 Yurt İçi Satışlar (alacak) 4.000',
            'B': '621 Satılan Ticari Malların Maliyeti (borç) 4.000 / 620 Satılan Mamuller Maliyeti (alacak) 4.000',
            'C': '153 Ticari Mallar (borç) 4.000 / 621 Satılan Ticari Malların Maliyeti (alacak) 4.000',
            'D': '621 Satılan Ticari Malların Maliyeti (borç) 4.000 / 153 Ticari Mallar (alacak) 4.000',
            'E': '610 Satıştan İadeler (borç) 4.000 / 153 Ticari Mallar (alacak) 4.000',
        },
        'C',
        'Satıştan iadede mal stoğa geri döner ve satıştaki maliyet kaydı ters çevrilir: **153 Ticari Mallar (borç) 4.000 / 621 Satılan Ticari Malların Maliyeti (alacak) 4.000**. (Hasılat tarafında ayrıca 610 Satıştan İadeler çalışır.)',
        "1 Sıra No'lu MSUGT - Satıştan iade (sürekli envanter)",
    ),
    # düzey 2
    '0048': patch(
        "Tartılı (ağırlıklı) ortalama maliyet yöntemini kullanan işletmenin hareketleri:\n\n| İşlem | Miktar | Birim Maliyet |\n|---|---|---|\n| Dönem başı | 100 br | 10 ₺ |\n| Alış | 200 br | 13 ₺ |\n| Alış | 100 br | 16 ₺ |\n\nDönemde 250 birim satılmıştır. Satılan malın maliyeti kaç ₺'dir?",
        {
            'A': '2.950',
            'B': '3.250',
            'C': '2.500',
            'D': '5.200',
            'E': '3.900',
        },
        'B',
        'Ortalama birim maliyet = (100×10 + 200×13 + 100×16) ÷ 400 = (1.000 + 2.600 + 1.600) ÷ 400 = 5.200 ÷ 400 = **13 ₺**. Satılan malın maliyeti = 250 × 13 = **3.250 ₺**.',
        'TMS 2 Stoklar - ağırlıklı ortalama',
    ),
    # düzey 2
    '0049': patch(
        "İşletmenin dönem sonunda depoda bulunan ve maliyeti 400.000 ₺ olan ticari mallarının piyasa satış fiyatı 460.000 ₺'ye yükselmiştir; mallar henüz satılmamıştır.\n\nVergi Usul Kanunu'na göre satın alınan emtia (ticari mal) hangi değerleme ölçüsü ile değerlenir?",
        {
            'A': 'Tasfiye değeri',
            'B': 'İtibari değer',
            'C': 'Emsal bedel',
            'D': 'Net gerçekleşebilir değer',
            'E': 'Maliyet bedeli',
        },
        'E',
        "VUK md. 274'e göre satın alınan emtia **maliyet bedeli** ile değerlenir. Kıymeti düşen mallar ise emsal bedeliyle değerlenebilir (md. 278).",
        'VUK md. 274 ve 278',
    ),
    # düzey 2
    '0050': patch(
        "İşletme, peşin fiyatı 100.000 ₺ olan bir ticari malı, 12 ay vade ile toplam 112.000 ₺'ye satın almıştır. Aradaki 12.000 ₺ vade farkıdır.\n\nTMS 2'ye göre bu malın stok maliyeti kaç ₺'dir?",
        {
            'A': '88.000',
            'B': '106.000',
            'C': '112.000',
            'D': '100.000',
            'E': '124.000',
        },
        'D',
        "TMS 2'ye göre vade farkı (finansman unsuru) stok maliyetine alınmaz; stok **peşin fiyatla** kaydedilir → **100.000 ₺**. 12.000 ₺ vade farkı, finansman gideri olarak ilgili dönemlere yansıtılır.",
        'TMS 2 Stoklar - vade farkı (finansman unsuru)',
    ),
    # düzey 2
    '0051': patch(
        'İşletme, liste fiyatı 100.000 ₺ olan ticari malı %10 ticari iskonto ve %20 KDV ile veresiye satın almıştır. KDV indirilebilir niteliktedir. Sürekli envanter yönteminde alış kaydı hangisidir?',
        {
            'A': '153 Ticari Mallar (borç) 100.000 + 191 İndirilecek KDV (borç) 20.000 / 320 Satıcılar (alacak) 120.000',
            'B': '320 Satıcılar (borç) 108.000 / 153 Ticari Mallar (alacak) 90.000 + 391 Hesaplanan KDV (alacak) 18.000',
            'C': '153 Ticari Mallar (borç) 90.000 + 191 İndirilecek KDV (borç) 18.000 / 320 Satıcılar (alacak) 108.000',
            'D': '153 Ticari Mallar (borç) 90.000 + 191 İndirilecek KDV (borç) 20.000 / 320 Satıcılar (alacak) 110.000',
            'E': '153 Ticari Mallar (borç) 108.000 / 320 Satıcılar (alacak) 108.000',
        },
        'C',
        "Ticari iskonto alış fiyatından düşülür: 100.000 × %90 = **90.000 ₺** stok maliyeti. İndirilecek KDV 90.000 × %20 = **18.000 ₺**, satıcıya borç 108.000 ₺'dir. Kayıt: 153 (borç) 90.000 + 191 (borç) 18.000 / 320 (alacak) 108.000.",
        "TMS 2 Stoklar, par. 11; 1 Sıra No'lu MSUGT - 153, 191 ve 320 hesapları",
    ),
    # düzey 2
    '0052': patch(
        'Bir üretim işletmesinin imal ettiği mamulün stok maliyetine aşağıdakilerden hangileri dâhil edilir?\n\nI. Direkt ilk madde ve malzeme giderleri\n\nII. Direkt işçilik giderleri\n\nIII. Üretimle ilgili genel üretim giderleri\n\nIV. Satış ve pazarlama giderleri',
        {
            'A': 'I, II ve III',
            'B': 'I ve II',
            'C': 'II ve IV',
            'D': 'Yalnız I',
            'E': 'I, II, III ve IV',
        },
        'A',
        'İmal edilen emtianın maliyetine **direkt ilk madde/malzeme (I)**, **direkt işçilik (II)** ve **genel üretim giderleri (III)** girer. **Satış ve pazarlama giderleri (IV)** üretim maliyetine alınmaz; dönem gideri yazılır (TMS 2; VUK md. 275).',
        'VUK md. 275; TMS 2 - imalat maliyet unsurları',
    ),
    # düzey 2
    '0053': patch(
        'Kozmetik toptancısı bir işletme, katıldığı fuarda ürünlerini tanıtmak amacıyla stoklarındaki maliyeti 12.000 ₺ olan numune ürünleri ziyaretçilere bedelsiz dağıtmıştır.\n\nİşletme, satışlarını artırmak amacıyla müşterilere bedelsiz dağıttığı bu malların maliyetini hangi hesaba yansıtır?',
        {
            'A': '689 Diğer Olağandışı Gider ve Zararlar',
            'B': '153 Ticari Mallar',
            'C': '621 Satılan Ticari Malların Maliyeti',
            'D': '770 Genel Yönetim Giderleri',
            'E': '760 Pazarlama, Satış ve Dağıtım Giderleri',
        },
        'E',
        'Satışı artırma amaçlı bedelsiz dağıtılan promosyon mallarının maliyeti bir **pazarlama gideridir**: **760 Pazarlama, Satış ve Dağıtım Giderleri**ne yazılır ve mal stoktan (153) çıkarılır (teslim KDV yönünden ayrıca değerlendirilir).',
        "1 Sıra No'lu MSUGT - 760 Pazarlama Satış Dağıtım Giderleri",
    ),
    # düzey 2
    '0054': patch(
        "Dönem sonunda net gerçekleşebilir değeri maliyetinin altına düşen ticari mallar için 20.000 ₺ stok değer düşüklüğü karşılığı ayrılmış; gider '654 Karşılık Giderleri' hesabına yazılmıştır.\n\nBu karşılık gideri gelir tablosunda hangi bölümde raporlanır?",
        {
            'A': 'Brüt satış kârının hesaplanmasında satış hasılatına eklenerek',
            'B': 'Finansman giderleri bölümünde',
            'C': 'Olağandışı gelir ve kârlar bölümünde',
            'D': 'Diğer faaliyetlerden olağan gider ve zararlar bölümünde',
            'E': 'Satılan malın maliyeti (SMM) satırında',
        },
        'D',
        "**654 Karşılık Giderleri**, gelir tablosunda **Diğer Faaliyetlerden Olağan Gider ve Zararlar** bölümünde raporlanır. SMM'ye dâhil edilmez; ayrı bir olağan faaliyet gideridir.",
        "1 Sıra No'lu MSUGT - Gelir tablosu; 654 Karşılık Giderleri",
    ),
    # düzey 3
    '0055': patch(
        "Bir ticari mal kaleminin dönem hareketleri sırasıyla şöyledir: dönem başı 100 birim × 20 ₺; alış 300 birim × 24 ₺; satış 250 birim; alış 150 birim × 27 ₺; satış 200 birim. İşletme ilk giren ilk çıkar (FIFO) yöntemini kullanmaktadır. Buna göre satılan ticari malların maliyeti kaç ₺'dir?",
        {
            'A': '10.750 ₺',
            'B': '10.550 ₺',
            'C': '11.250 ₺',
            'D': '13.250 ₺',
            'E': '2.700 ₺',
        },
        'B',
        "Toplam maliyet 2.000 + 7.200 + 4.050 = 13.250 ₺; toplam 550 birimden 450'si satılmıştır. FIFO'da kalan 100 birim en son alıştandır: 100 × 27 = 2.700 ₺. SMM 13.250 − 2.700 = **10.550 ₺** (hareketli ortalamada 10.750 ₺).",
        "1 Sıra No'lu MSUGT; VUK m. 274 (maliyet akışı)",
    ),
    # düzey 3
    '0056': patch(
        "Stoklarını sürekli envanter yöntemiyle izleyen işletme, maliyeti 75.000 ₺ olan ticari malı maliyet üzerinden %20 kârla ve %20 KDV'li olarak kredili satmıştır. Buna göre satışa ilişkin kayıtlarla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '600 Yurt İçi Satışlar hesabı 108.000 ₺ alacaklandırılır',
            'B': '153 Ticari Mallar hesabı 90.000 ₺ alacaklandırılır',
            'C': '621 Satılan Ticari Mallar Maliyeti hesabı 75.000 ₺ alacaklandırılır',
            'D': '621 Satılan Ticari Mallar Maliyeti hesabı 90.000 ₺ borçlandırılır',
            'E': '153 Ticari Mallar hesabı 75.000 ₺ alacaklandırılır',
        },
        'E',
        'Satış bedeli 75.000 × 1,20 = 90.000 ₺. Hasılat: 120 (borç) 108.000 / 600 (alacak) 90.000 + 391 (alacak) 18.000. Maliyet: 621 (borç) / **153 (alacak) 75.000**.',
        'Sürekli envanter; THP 153, 621',
    ),
    # düzey 3
    '0057': patch(
        "Sürekli envanter yöntemini kullanan işletmede 153 Ticari Mallar hesabının kaydi kalanı 90.000 ₺, dönem sonu sayımında belirlenen mevcut 84.000 ₺'dir. Farkın nedeninin araştırılmasına karar verilmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': '153 hesabı 6.000 ₺ borçlandırılır',
            'B': "Nedeni bulunamayan fark dönem sonunda 689'a aktarılır",
            'C': '197 hesabı 6.000 ₺ borçlandırılır',
            'D': '153 hesabı 6.000 ₺ alacaklandırılır',
            'E': 'Stokun kaydi değeri sayım sonucuna eşitlenir',
        },
        'A',
        "Sayım noksanında kayıtlı stok fiilî duruma indirilir: 197 Sayım ve Tesellüm Noksanları (borç) / **153 (alacak)** 6.000. Nedeni dönem sonuna kadar bulunamazsa 689'a aktarılır.",
        'THP 153, 197, 689',
    ),
    # düzey 2
    '0058': patch(
        "Stoklarla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Konsinye olarak satılmak üzere gönderilen mallar, satılana kadar gönderen işletmenin stokudur.\n\nII. FOB yükleme noktası koşuluyla gönderilip yolda olan mallar satıcının stokudur.\n\nIII. İşletmenin kendi kullandığı büro malzemeleri 153 Ticari Mallar'da izlenir.",
        {
            'A': 'I ve III',
            'B': 'I ve II',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'Yalnız II',
        },
        'C',
        "Yalnız I doğrudur. FOB yükleme noktasında mülkiyet yüklemeyle alıcıya geçer; yoldaki mal **alıcının** stokudur. Satış amacı taşımayan büro malzemeleri 153'te izlenmez.",
        'Stokların mülkiyeti; THP 153',
    ),
    # düzey 3
    '0059': patch(
        "Stoklarını sürekli envanter yöntemiyle izleyen işletme, satın aldığı ticari malların deposuna taşınması için nakliye firmasına 8.000 ₺ + %20 KDV'yi bankadan ödemiştir. Buna göre ödeme kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '153 Ticari Mallar hesabı 9.600 ₺ borçlandırılır',
            'B': '153 Ticari Mallar hesabı 8.000 ₺ borçlandırılır',
            'C': '760 Pazarlama Satış ve Dağıtım Giderleri hesabı 8.000 ₺ borçlandırılır',
            'D': '770 Genel Yönetim Giderleri hesabı 8.000 ₺ borçlandırılır',
            'E': '621 Satılan Ticari Mallar Maliyeti hesabı 8.000 ₺ borçlandırılır',
        },
        'B',
        'Alış sırasında malın depoya getirilmesi için yapılan taşıma **maliyet unsurudur**: 153 (borç) 8.000 + 191 (borç) 1.600 / 102 (alacak) 9.600. İndirilecek KDV maliyete eklenmez.',
        'VUK m. 262; THP 153, 191, 102',
    ),
    # düzey 3
    '0060': patch(
        'Stoklarını sürekli envanter yöntemiyle izleyen işletmenin deposundaki maliyeti 50.000 ₺ olan ticari mallar yangında tamamen kullanılamaz hâle gelmiştir. Sigorta şirketi 35.000 ₺ tazminat ödeyeceğini bildirmiştir. Buna göre yapılacak kayıtla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '136 Diğer Çeşitli Alacaklar hesabı 50.000 ₺ borçlandırılır',
            'B': '689 Diğer Olağandışı Gider ve Zararlar hesabı 50.000 ₺ borçlandırılır',
            'C': '153 Ticari Mallar hesabı 35.000 ₺ alacaklandırılır',
            'D': '689 Diğer Olağandışı Gider ve Zararlar hesabı 15.000 ₺ borçlandırılır',
            'E': '621 Satılan Ticari Mallar Maliyeti hesabı 50.000 ₺ borçlandırılır',
        },
        'D',
        'Kayıt: 136 (borç) 35.000 + **689 (borç) 15.000** / 153 (alacak) 50.000. Tazminatla karşılanmayan kısım olağandışı zarardır; mal satılmadığı için 621 kullanılmaz.',
        'THP 136, 689, 153',
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
    print(f"1 paket / {len(PATCHES)} soru ('Stoklar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
