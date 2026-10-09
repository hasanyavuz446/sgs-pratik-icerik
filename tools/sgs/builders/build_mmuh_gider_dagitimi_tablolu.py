#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gider Dagitimi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Maliyet turu (gerçek sınav 57-64 bloğu ölçüldü: gider dağıtımı ve GÜG yüklemesi maliyet sorularının ~%30'u). Paket baştan yazıldı; eski paketteki tekrar eden veri seti (Bakım 10.000 / Kantin 17.000) kaldırıldı, her hesaplı soru kendi veri setini taşır. Kapsam: tek ve iki anahtarlı birinci dağıtım; doğrudan, kademeli ve matematiksel (karşılıklı denklemli) ikinci dağıtım; denklem kurma ve denklem okuma (olumsuz kök); makine saati ve DİG esaslı yükleme oranıyla birim maliyet; tahmini oranla eksik/fazla yükleme (dönem ve sipariş bazında); normal maliyette kapasite kullanım oranı; kullanılmayan kapasite maliyeti; 7/A akışı (730-731-151) ve farkın kapatılması. Tutarlar Fraction ile hesaplandı; yuvarlanmış tutar yalnız çeldiricide kabul edildi ve kesin alanlarda bulunmadığı denetlendi. Tablolar en çok 4 sütun (360 dp). Sayısal şıklarda doğru cevabın büyüklük sırası dengelendi (ortanca değer tell'i).

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Maliyet muhasebesi - gider yerleri ve gider dagitimi · Tekduzen Hesap Plani 7/A
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/maliyet_muhasebesi/gider_dagitimi.json"
STYLE_REF = 'SGS Maliyet Muhasebesi (tablolu çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "mmuh-dagitim-gen-"


def patch(stem, options, answer, solution, ref='Maliyet muhasebesi - gider yerleri'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        'Zirve Otomotiv işletmesi 210.000 ₺ tutarındaki fabrika kira giderini gider yerlerine kapladıkları alana göre dağıtmaktadır.\n\n| Gider yeri | Alan (m²) |\n|---|---|\n| Kalıp | 240 |\n| Pres | 180 |\n| Bakım | 60 |\n| Depo | 120 |\n\nBu dağıtımla ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Bakım'a 21.000 ₺ pay düşer",
            'B': 'Metrekare başına 350 ₺ düşer',
            'C': "Pres'e 63.000 ₺ pay düşer",
            'D': "Kalıp'a 84.000 ₺ pay düşer",
            'E': "Depo'ya 49.000 ₺ pay düşer",
        },
        'E',
        "Metrekare başına 210.000 ₺ / 600 = 350 ₺ düşer. Depo'nun payı 350 ₺ × 120 = 42.000 ₺'dir.",
    ),
    # düzey 2
    '0002': patch(
        "Sarp Kauçuk işletmesinin Kalıp esas üretim gider yerinde gelecek yıl için tahmini genel üretim gideri 320.000 ₺, tahmini faaliyet hacmi 16.000 makine saati olarak bütçelenmiştir. Dönem içinde Kalıp'ta üretilen bir mamul partisi 400 makine saati kullanmıştır.\n\nBu partiye yüklenecek genel üretim gideri kaç ₺'dir?",
        {
            'A': '4.000 ₺',
            'B': '8.800 ₺',
            'C': '8.000 ₺',
            'D': '9.000 ₺',
            'E': '16.000 ₺',
        },
        'C',
        'Tahmini yükleme oranı 320.000 ₺ / 16.000 = 20 ₺/makine. Partiye 20 ₺ × 400 = 8.000 ₺ yüklenir.',
    ),
    # düzey 2
    '0003': patch(
        "Tekdüzen Hesap Planı'nın 7/A seçeneğini kullanan bir işletmede dönem sonunda mamullere yüklenen genel üretim giderleri yansıtma hesabı aracılığıyla aktarılmaktadır.\n\nBu aktarımda borçlandırılan hesap aşağıdakilerden hangisidir?",
        {
            'A': '151 Yarı Mamuller – Üretim',
            'B': '152 Mamuller',
            'C': '620 Satılan Mamuller Maliyeti',
            'D': '731 Genel Üretim Giderleri Yansıtma',
            'E': '770 Genel Yönetim Giderleri',
        },
        'A',
        '7/A seçeneğinde 730 hesapta toplanan giderler 731 Genel Üretim Giderleri Yansıtma hesabına alacak kaydedilerek 151 Yarı Mamuller – Üretim hesabına borç kaydedilir; 731 dönem sonunda 730 ile kapatılır.',
    ),
    # düzey 3
    '0004': patch(
        'I. Doğrudan yöntem\nII. Kademeli (basamaklı) yöntem\nIII. Matematiksel (karşılıklı) yöntem\n\nYukarıdaki ikinci dağıtım yöntemlerinden hangileri yardımcı gider yerlerinin birbirine verdiği hizmeti en az kısmen dikkate alır?',
        {
            'A': 'I, II ve III',
            'B': 'I ve II',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'Yalnız II',
        },
        'D',
        'Kademeli yöntem yardımcı gider yerleri arasındaki hizmeti tek yönlü, matematiksel yöntem karşılıklı olarak dikkate alır. Doğrudan yöntem bu hizmeti hiç dikkate almaz.',
    ),
    # düzey 2
    '0005': patch(
        'Normal maliyet sistemini uygulayan bir işletmede dönem sonunda fiili genel üretim giderleri, yüklenen genel üretim giderlerinden fazla çıkmıştır.\n\nBu durumla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tahmini oran fiili orandan düşük değildir',
            'B': 'Eksik yükleme söz konusudur',
            'C': 'Fark direkt işçilik giderlerine eklenir',
            'D': 'Yükleme farkı oluşmamıştır',
            'E': 'Fazla yükleme söz konusudur',
        },
        'B',
        'Yüklenen tutar fiili giderden az kaldığında eksik yükleme oluşur; fark dönem sonunda satılan mamul maliyetine ya da stoklara ve satılan mamul maliyetine dağıtılarak kapatılır.',
    ),
    # düzey 3
    '0006': patch(
        "Sipariş maliyet sistemini uygulayan Atlas Makine işletmesinde dönemde iki sipariş üretilmiştir:\n\n|  | S-21 | S-22 |\n|---|---|---|\n| DİMM (₺) | 12.000 | 18.000 |\n| DİG (₺) | 15.000 | 20.000 |\n| Makine saati | 500 | 700 |\n\nDönem içinde genel üretim giderleri her siparişe direkt işçilik giderinin %60'ı oranında tahmini olarak yüklenmiştir. Dönem sonunda fiili genel üretim gideri 24.000 ₺ olarak gerçekleşmiş ve bu tutar siparişlere makine saatine göre dağıtılmıştır.\n\nBuna göre S-21 için genel üretim gideri yükleme farkı aşağıdakilerden hangisidir?",
        {
            'A': '3.000 ₺ eksik yükleme',
            'B': '2.000 ₺ eksik yükleme',
            'C': '1.000 ₺ eksik yükleme',
            'D': '1.000 ₺ fazla yükleme',
            'E': '3.000 ₺ fazla yükleme',
        },
        'C',
        "S-21'e tahmini olarak 9.000 ₺ yüklenmiştir. Fiili payı 24.000 ₺ × 500 / 1.200 = 10.000 ₺'dir. Fark 1.000 ₺; yüklenen tutar fiiliden az olduğundan eksik yükleme vardır.",
    ),
    # düzey 3
    '0007': patch(
        "Ege Tekstil işletmesinde dönemin 240.000 ₺ tutarındaki fabrika binası kira gideri, gider yerlerine kapladıkları alana göre dağıtılmaktadır.\n\n| Gider yeri | Alan (m²) |\n|---|---|\n| Dokuma | 500 |\n| Boya | 300 |\n| Bakım | 150 |\n| Yemekhane | 50 |\n\nBirinci dağıtımda Boya gider yerine düşen kira payı kaç ₺'dir?",
        {
            'A': '144.000 ₺',
            'B': '90.000 ₺',
            'C': '120.000 ₺',
            'D': '168.000 ₺',
            'E': '72.000 ₺',
        },
        'E',
        "Dağıtım anahtarı alan (m²) toplamı 1.000'dir. Boya gider yerinin payı 240.000 ₺ × 300 / 1.000 = 72.000 ₺.",
    ),
    # düzey 3
    '0008': patch(
        "Doğan Otomotiv işletmesi ikinci dağıtımda kademeli yöntemi kullanmaktadır. Önce Kantin çalışan sayısına göre (Bakım dahil), ardından Bakım bakım saatine göre dağıtılmaktadır. Birinci dağıtım toplamları (₺) ve ölçüler şöyledir:\n\n| Gider yeri | I. dağıtım | Çalışan | Bakım saati |\n|---|---|---|---|\n| Kantin | 30.000 | — | — |\n| Bakım | 45.000 | 10 | — |\n| Pres | 160.000 | 50 | 300 |\n| Kaynak | 110.000 | 40 | 200 |\n\nBuna göre ikinci dağıtımdan sonra Pres gider yerinde toplanan genel üretim gideri kaç ₺'dir?",
        {
            'A': '206.800 ₺',
            'B': '203.800 ₺',
            'C': '245.000 ₺',
            'D': '208.800 ₺',
            'E': '225.000 ₺',
        },
        'B',
        "Kantin'den Bakım'a 30.000 ₺ × 10 / 100 = 3.000 ₺ pay düşer; Bakım'ın dağıtılacak toplamı 48.000 ₺ olur. Pres gider yerinin toplamı: birinci dağıtım + Kantin payı + Bakım payı = 203.800 ₺.",
    ),
    # düzey 3
    '0009': patch(
        'I. Normal kapasite, işletmenin uzun dönemde ortalama olarak çalışmayı beklediği kapasitedir.\nII. Sabit genel üretim giderlerinin birim başına payı üretim arttıkça azalır.\nIII. Kullanılmayan kapasite maliyeti stokların maliyetine dahil edilir.\n\nYukarıdaki ifadelerden hangileri doğrudur?',
        {
            'A': 'I ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'C',
        'Normal kapasite uzun dönemli ortalama kapasitedir; sabit giderlerin birim payı üretim arttıkça azalır. Kullanılmayan kapasite maliyeti stoklara değil dönem giderlerine aktarılır.',
    ),
    # düzey 3
    '0010': patch(
        "Akdeniz Gıda işletmesinde dönemin 150.000 ₺ tutarındaki kira gideri alana, 200.000 ₺ tutarındaki makine amortismanı ise makinelerin değerine göre gider yerlerine dağıtılmaktadır.\n\n| Gider yeri | Alan (m²) | Makine (bin ₺) |\n|---|---|---|\n| Hazırlık | 400 | 600 |\n| Paketleme | 400 | 300 |\n| Bakım | 200 | 100 |\n\nBu iki ortak giderden Hazırlık gider yerine düşen toplam pay kaç ₺'dir?",
        {
            'A': '116.670 ₺',
            'B': '120.000 ₺',
            'C': '60.000 ₺',
            'D': '140.000 ₺',
            'E': '180.000 ₺',
        },
        'E',
        "Kira payı 150.000 ₺ × 400 / 1.000, amortisman payı 200.000 ₺ × 600 / 1.000'dir. Toplam 180.000 ₺.",
    ),
    # düzey 2
    '0011': patch(
        'Normal maliyet sisteminde genel üretim giderlerinin mamullere tahmini yükleme oranıyla yüklenmesinin temel nedeni aşağıdakilerden hangisi değildir?',
        {
            'A': 'Satış fiyatı kararlarının zamanında verilebilmesi',
            'B': 'Fiili giderlerin vergi matrahından düşülememesi',
            'C': 'Fiili giderlerin dönem sonunda kesinleşmesi',
            'D': 'Birim maliyetlerin dönem içinde hesaplanabilmesi',
            'E': 'Mevsimsel dalgalanmaların birim maliyeti bozmasının önlenmesi',
        },
        'B',
        'Tahmini yükleme; fiili giderler dönem sonunda kesinleştiği için birim maliyetin dönem içinde bulunabilmesi, mevsimsel dalgalanmaların etkisinin giderilmesi ve fiyatlama kararlarının zamanında verilmesi amacıyla yapılır.',
    ),
    # düzey 3
    '0012': patch(
        'Ulus Döküm işletmesi genel üretim giderlerini dönem içinde tahmini yükleme oranıyla mamullere yüklemektedir. Yıl başında tahmini genel üretim gideri 480.000 ₺, tahmini faaliyet hacmi 24.000 makine saati olarak belirlenmiştir. Dönemde fiilen 22.000 makine saati çalışılmış ve 455.000 ₺ genel üretim gideri gerçekleşmiştir.\n\nBuna göre dönem sonunda ortaya çıkan yükleme farkı aşağıdakilerden hangisidir?',
        {
            'A': '40.000 ₺ fazla yükleme',
            'B': '25.000 ₺ eksik yükleme',
            'C': '15.000 ₺ fazla yükleme',
            'D': '15.000 ₺ eksik yükleme',
            'E': '30.000 ₺ eksik yükleme',
        },
        'D',
        "Tahmini yükleme oranı 480.000 ₺ / 24.000 = 20 ₺. Yüklenen GÜG 20 ₺ × 22.000 = 440.000 ₺. Fiili GÜG 455.000 ₺ olduğundan fark 15.000 ₺'dir; yüklenen tutar fiiliden az olduğu için eksik yükleme söz konusudur.",
    ),
    # düzey 3
    '0013': patch(
        'Kartal Makine işletmesi genel üretim giderlerinin ikinci dağıtımında matematiksel yöntemi kullanmaktadır. Y ve Z yardımcı gider yerleri için şu denklemler kurulmuştur:\n\nY = 25.000 + 0,10Z\nZ = 30.000 + 0,15Y\n\nBu denklemlere göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Y'nin birinci dağıtım toplamı 25.000 ₺'dir",
            'B': "Z, Y'nin hizmetinin %10'unu alır",
            'C': "Z, Y'nin hizmetinin %15'ini alır",
            'D': "Z'nin birinci dağıtım toplamı 30.000 ₺'dir",
            'E': "Y, Z'nin hizmetinin %10'unu alır",
        },
        'B',
        "Y denklemindeki 0,10 katsayısı Y'nin Z'den aldığı payı, Z denklemindeki 0,15 katsayısı Z'nin Y'den aldığı payı gösterir. Bu nedenle Z, Y'nin hizmetinin %15'ini alır.",
    ),
    # düzey 3
    '0014': patch(
        "Arı Elektronik işletmesinde Kantin yardımcı gider yerinin birinci dağıtım toplamı 24.000 ₺, Bakım yardımcı gider yerininki 30.000 ₺'dir. Kantin giderleri çalışan sayısına göre dağıtılmaktadır; işletmede toplam 116 çalışan bulunmakta olup bunların 12'si Bakım'da, 20'si Kantin'de çalışmaktadır.\n\nKademeli yöntemde Kantin önce dağıtıldığına göre Bakım'ın dağıtacağı toplam tutar kaç ₺'dir?",
        {
            'A': '33.000 ₺',
            'B': '29.000 ₺',
            'C': '3.000 ₺',
            'D': '30.000 ₺',
            'E': '32.480 ₺',
        },
        'A',
        "Kantin kendi çalışanlarına pay vermez; dağıtımda 116 − 20 = 96 çalışan esas alınır. Bakım'a 24.000 ₺ × 12 / 96 = 3.000 ₺ pay düşer; toplam 33.000 ₺ olur.",
    ),
    # düzey 2
    '0015': patch(
        'Normal maliyet sistemini uygulayan bir işletmede dönem sonunda tutarı önemsiz bir eksik yükleme farkı ortaya çıkmıştır ve dönemde üretilen mamullerin tamamı satılmıştır.\n\nBu farkın kapatılmasıyla ilgili en uygun uygulama aşağıdakilerden hangisidir?',
        {
            'A': 'Sermaye hesabından mahsup edilmesi',
            'B': 'Olağan dışı gider olarak kaydedilmesi',
            'C': 'Direkt işçilik giderlerine eklenmesi',
            'D': 'Satılan mamuller maliyetine eklenmesi',
            'E': 'Gelecek dönemin giderlerine aktarılması',
        },
        'D',
        'Önemsiz yükleme farkları doğrudan satılan mamuller maliyetine aktarılır. Fark önemliyse ve mamullerin bir kısmı stoktaysa yarı mamul, mamul ve satılan mamul maliyeti arasında oransal dağıtılır.',
    ),
    # düzey 2
    '0016': patch(
        'Aşağıdakilerden hangisi sabit genel üretim giderlerine örnek değildir?',
        {
            'A': 'Fabrika binasının amortismanı',
            'B': 'Fabrika binasının kira gideri',
            'C': 'Üretim müdürüne ödenen aylık ücret',
            'D': 'Makineler için ödenen yıllık sigorta primi',
            'E': 'Üretilen birim başına ödenen ambalaj gideri',
        },
        'E',
        'Birim başına ödenen ambalaj gideri üretim miktarıyla birlikte değişir; değişken giderdir. Amortisman, kira, aylık ücret ve sigorta primi üretim hacminden bağımsız sabit giderlerdir.',
    ),
    # düzey 2
    '0017': patch(
        'Bir işletmede direkt ilk madde ve malzeme ile direkt işçilik giderleri doğrudan mamullere yüklenirken bina amortismanı, aydınlatma ve kira gibi giderler önce gider yerlerine dağıtılmaktadır.\n\nBu uygulamanın temel nedeni aşağıdakilerden hangisidir?',
        {
            'A': 'Bu giderlerin tutarlarının direkt giderlere göre düşük olması',
            'B': 'Vergi mevzuatının bu sıralamayı açıkça zorunlu kılması',
            'C': 'Bu giderlerin mamullerle doğrudan ilişkilendirilememesi',
            'D': 'Bu giderlerin dönem gideri sayılması',
            'E': 'Direkt giderlerin tahmini olarak hesaplanması',
        },
        'C',
        'Genel üretim giderleri birden çok mamule ya da gider yerine ortak hizmet ettiğinden mamullerle doğrudan ilişkilendirilemez; bu nedenle önce gider yerlerine dağıtılıp oradan yükleme oranlarıyla mamullere yüklenir.',
    ),
    # düzey 2
    '0018': patch(
        'Kademeli (basamaklı) dağıtım yönteminde yardımcı gider yerlerinin dağıtım sırası belirlenirken genellikle hangi ölçüt esas alınır?',
        {
            'A': 'Alfabetik sıraya göre dağıtım yapılması',
            'B': 'Esas üretim gider yerlerinin önce dağıtılması',
            'C': 'En çok gider yerine hizmet verenin önce dağıtılması',
            'D': 'Çalışan sayısı en az olanın önce dağıtılması',
            'E': 'Birinci dağıtım toplamı en küçük olanın önce dağıtılması',
        },
        'C',
        'Kademeli yöntemde diğer gider yerlerine en çok hizmet veren yardımcı gider yeri önce dağıtılır; sonra dağıtılan gider yeri, kendisinden önce dağıtılanlara pay vermez.',
    ),
    # düzey 3
    '0019': patch(
        "Yamaç Çelik işletmesinin yıllık sabit genel üretim gideri 600.000 ₺, normal kapasitesi 30.000 makine saatidir. İşletme sabit genel üretim giderlerini normal kapasiteye göre yüklemektedir. Dönemde talep düşüklüğü nedeniyle 24.000 makine saati çalışılabilmiştir.\n\nBuna göre dönemin kullanılmayan kapasite maliyeti kaç ₺'dir?",
        {
            'A': '120.000 ₺',
            'B': '540.000 ₺',
            'C': '480.000 ₺',
            'D': '108.000 ₺',
            'E': '96.000 ₺',
        },
        'A',
        'Sabit GÜG yükleme oranı 600.000 ₺ / 30.000 = 20 ₺/saat. Kullanılmayan 6.000 saatin maliyeti 20 ₺ × 6.000 = 120.000 ₺; bu tutar mamul maliyetine yüklenmez, dönem gideri olarak izlenir.',
    ),
    # düzey 3
    '0020': patch(
        "Bora Kauçuk işletmesinde Kantin giderleri kademeli yöntemle ilk sırada, çalışan sayısına göre dağıtılmaktadır. Kantin'in birinci dağıtım toplamı 36.000 ₺'dir.\n\n| Gider yeri | Çalışan |\n|---|---|\n| Kantin | 10 |\n| Bakım | 9 |\n| Kesim | 45 |\n| Pres | 36 |\n\nBuna göre Kantin'den Kesim gider yerine aktarılan tutar kaç ₺'dir?",
        {
            'A': '14.400 ₺',
            'B': '16.200 ₺',
            'C': '20.000 ₺',
            'D': '12.000 ₺',
            'E': '18.000 ₺',
        },
        'E',
        "Kantin kendi çalışanlarına pay vermez; dağıtım 9 + 45 + 36 = 90 çalışana yapılır ve Bakım da pay alır. Kesim'in payı 36.000 × 45 / 90 = 18.000 ₺'dir.",
    ),
    # düzey 2
    '0021': patch(
        'Yardımcı gider yerlerinin ikinci dağıtımında doğrudan yöntem ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Karşılıklı hizmetler denklem sistemiyle çözülür',
            'B': 'Esas üretim gider yerleri birbirine pay verir',
            'C': 'Yardımcı gider yerleri arasındaki hizmetler dikkate alınmaz',
            'D': 'Yardımcı gider yerleri belirli bir sırayla birbirine pay verir',
            'E': 'Dağıtım sonunda yardımcı gider yerlerinde bakiye kalır',
        },
        'C',
        'Doğrudan yöntemde yardımcı gider yerlerinin giderleri yalnız esas üretim gider yerlerine dağıtılır; aralarındaki karşılıklı hizmet göz ardı edilir.',
    ),
    # düzey 3
    '0022': patch(
        "Lale Gıda işletmesinde Y ve Z yardımcı gider yerleri birbirine hizmet vermektedir. Birinci dağıtım toplamları (₺) ve birbirlerine verdikleri hizmet payları şöyledir:\n\n| Gider yeri | I. dağıtım | Hizmet payı |\n|---|---|---|\n| Y | 64.000 | Z'ye %15 |\n| Z | 52.000 | Y'ye %20 |\n\nMatematiksel dağıtım yöntemi için Y yardımcı gider yerine ilişkin yazılacak denklem aşağıdakilerden hangisidir?",
        {
            'A': 'Y = 52.000 + 0,20Z',
            'B': 'Y = 64.000 + 0,20Z',
            'C': 'Y = 64.000 + 0,15Z',
            'D': 'Z = 64.000 + 0,15Y',
            'E': 'Z = 52.000 + 0,20Y',
        },
        'B',
        "Her yardımcı gider yerinin toplamı, kendi birinci dağıtım tutarı ile diğerinden aldığı payın toplamıdır. Y, Z'nin hizmetinin %20'sini aldığından Y = 64.000 + 0,20Z yazılır.",
    ),
    # düzey 3
    '0023': patch(
        "İnci Kozmetik işletmesinin yıllık sabit genel üretim gideri 360.000 ₺, normal kapasitesi 18.000 makine saatidir. İşletme sabit genel üretim giderlerini normal kapasiteye göre yüklemektedir. Dönemde talep düşüklüğü nedeniyle 15.300 makine saati çalışılabilmiştir.\n\nBuna göre dönemin kullanılmayan kapasite maliyeti kaç ₺'dir?",
        {
            'A': '306.000 ₺',
            'B': '333.000 ₺',
            'C': '108.000 ₺',
            'D': '54.000 ₺',
            'E': '360.000 ₺',
        },
        'D',
        'Sabit GÜG yükleme oranı 360.000 ₺ / 18.000 = 20 ₺/saat. Kullanılmayan 2.700 saatin maliyeti 20 ₺ × 2.700 = 54.000 ₺; bu tutar mamul maliyetine yüklenmez, dönem gideri olarak izlenir.',
    ),
    # düzey 2
    '0024': patch(
        'Bir işletmede aşağıdaki ortak giderlerin gider yerlerine dağıtımı için dağıtım anahtarları belirlenmiştir.\n\nAşağıdaki gider–dağıtım anahtarı eşleştirmelerinden hangisi en az uygundur?',
        {
            'A': 'Bina kirası – Kapladığı alan',
            'B': 'Elektrik gideri – Tüketilen kWh',
            'C': 'Yemekhane gideri – Çalışan sayısı',
            'D': 'Makine sigortası – Makine değeri',
            'E': 'Bina kirası – Çalışan sayısı',
        },
        'E',
        'Bina kirası binanın kullanımına bağlıdır; uygun anahtar kapladığı alandır. Çalışan sayısı yemekhane, sosyal sigorta gibi personele bağlı giderler için uygundur.',
    ),
    # düzey 3
    '0025': patch(
        "Sipariş maliyet sistemini uygulayan Nehir Mobilya işletmesinde dönemde iki sipariş üretilmiştir:\n\n|  | S-07 | S-08 |\n|---|---|---|\n| DİMM (₺) | 9.000 | 14.000 |\n| DİG (₺) | 10.000 | 25.000 |\n| Makine saati | 300 | 500 |\n\nDönem içinde genel üretim giderleri her siparişe direkt işçilik giderinin %80'i oranında tahmini olarak yüklenmiştir. Dönem sonunda fiili genel üretim gideri 28.800 ₺ olarak gerçekleşmiş ve bu tutar siparişlere makine saatine göre dağıtılmıştır.\n\nBuna göre S-08 için genel üretim gideri yükleme farkı aşağıdakilerden hangisidir?",
        {
            'A': '800 ₺ fazla yükleme',
            'B': '2.000 ₺ fazla yükleme',
            'C': '2.000 ₺ eksik yükleme',
            'D': '2.800 ₺ fazla yükleme',
            'E': '3.000 ₺ fazla yükleme',
        },
        'B',
        "S-08'e tahmini olarak 20.000 ₺ yüklenmiştir. Fiili payı 28.800 ₺ × 500 / 800 = 18.000 ₺'dir. Fark 2.000 ₺; yüklenen tutar fiiliden fazla olduğundan fazla yükleme vardır.",
    ),
    # düzey 3
    '0026': patch(
        "Kaya Mobilya işletmesinde Kesim gider yerinde genel üretim gideri makine saati başına 20 ₺, Montaj gider yerinde ise direkt işçilik giderinin %60'ı oranında yüklenmektedir. D mamulünden 500 adet üretilmiş; mamul Kesim'de 1.500 makine saati çalışmış, Montaj'da 40.000 ₺ direkt işçilik gideri almıştır. Mamulün toplam direkt ilk madde ve malzeme gideri 70.000 ₺, toplam direkt işçilik gideri 65.000 ₺'dir.\n\nD mamulünün birim üretim maliyeti kaç ₺'dir?",
        {
            'A': '398 ₺',
            'B': '330 ₺',
            'C': '270 ₺',
            'D': '378 ₺',
            'E': '341 ₺',
        },
        'D',
        "Kesim'den 20 ₺ × 1.500 = 30.000 ₺, Montaj'dan 40.000 ₺ × %60 = 24.000 ₺ GÜG yüklenir; toplam 54.000 ₺. Birim maliyet (70.000 ₺ + 65.000 ₺ + 54.000 ₺) / 500 = 378 ₺.",
    ),
    # düzey 3
    '0027': patch(
        "Pınar Seramik işletmesinde Bakım yardımcı gider yerinin birinci dağıtım toplamı 72.000 ₺'dir. Dönemde Bakım; Şekillendirme gider yerine 120, Fırın gider yerine 60, Kantin yardımcı gider yerine 40 ve Depo yardımcı gider yerine 20 saat hizmet vermiştir.\n\nİşletme doğrudan dağıtım yöntemini kullandığına göre Bakım'dan Şekillendirme gider yerine aktarılan tutar kaç ₺'dir?",
        {
            'A': '53.000 ₺',
            'B': '48.000 ₺',
            'C': '55.200 ₺',
            'D': '58.000 ₺',
            'E': '39.270 ₺',
        },
        'B',
        'Doğrudan yöntemde diğer yardımcı gider yerlerine verilen saatler dikkate alınmaz; yalnız esas üretim gider yerlerinin saatleri (120 + 60) kullanılır: 72.000 ₺ × 120 / 180 = 48.000 ₺.',
    ),
    # düzey 2
    '0028': patch(
        'Sabit genel üretim giderlerinin normal kapasiteye göre mamullere yüklendiği bir işletmede fiili üretim normal kapasitenin altında kalmıştır.\n\nKullanılmayan kapasiteye düşen sabit gider payı ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Dönem gideri olarak kaydedilir',
            'B': 'Gelecek döneme ertelenerek aktarılır',
            'C': 'Mamul maliyetine eklenir',
            'D': 'Stokların maliyetine dağıtılır',
            'E': 'Direkt işçilik gideri sayılır',
        },
        'A',
        'Normal kapasitenin kullanılmayan kısmına düşen sabit genel üretim giderleri mamul maliyetine yüklenmez; dönem gideri olarak sonuç hesaplarına aktarılır.',
    ),
    # düzey 3
    '0029': patch(
        "Mavi Tekstil'de yardımcı gider yerlerinin ikinci dağıtımı için şu denklemler kurulmuştur:\n\nY = 21.000 + 0,25Z\nZ = 72.000 + 0,10Y\n\nY'nin hizmetlerinin %60'ı A, %30'u B esas üretim gider yerine; Z'nin hizmetlerinin %40'ı A, %35'i B gider yerine verilmektedir.\n\nBuna göre ikinci dağıtımda B gider yerine aktarılan toplam tutar kaç ₺'dir?",
        {
            'A': '31.500 ₺',
            'B': '54.400 ₺',
            'C': '38.600 ₺',
            'D': '40.600 ₺',
            'E': '26.600 ₺',
        },
        'C',
        "İkinci denklem birinciye yerleştirilir: Y = 21.000 + 0,25 × (72.000 + 0,10Y) → 0,975Y = 39.000 → Y = 40.000 ₺, Z = 76.000 ₺. B'ye aktarılan: 0,30 × 40.000 + 0,35 × 76.000 = 12.000 + 26.600 = 38.600 ₺.",
    ),
    # düzey 3
    '0030': patch(
        "Çınar Mobilya işletmesinde dönemin 120.000 ₺ tutarındaki kira gideri alana, 90.000 ₺ tutarındaki makine amortismanı ise makinelerin değerine göre gider yerlerine dağıtılmaktadır.\n\n| Gider yeri | Alan (m²) | Makine (bin ₺) |\n|---|---|---|\n| Kesim | 300 | 450 |\n| Cila | 200 | 150 |\n| Atölye | 100 | 300 |\n\nBu iki ortak giderden Cila gider yerine düşen toplam pay kaç ₺'dir?",
        {
            'A': '40.000 ₺',
            'B': '15.000 ₺',
            'C': '55.000 ₺',
            'D': '70.000 ₺',
            'E': '95.000 ₺',
        },
        'C',
        "Kira payı 120.000 ₺ × 200 / 600, amortisman payı 90.000 ₺ × 150 / 900'dir. Toplam 55.000 ₺.",
    ),
    # düzey 3
    '0031': patch(
        "Ova Konserve işletmesi ikinci dağıtımda kademeli yöntemi kullanmaktadır. Önce Kantin çalışan sayısına göre (Bakım dahil), ardından Bakım bakım saatine göre dağıtılmaktadır. Birinci dağıtım toplamları (₺) ve ölçüler şöyledir:\n\n| Gider yeri | I. dağıtım | Çalışan | Bakım saati |\n|---|---|---|---|\n| Kantin | 44.000 | — | — |\n| Bakım | 36.000 | 10 | — |\n| Haşlama | 130.000 | 50 | 150 |\n| Dolum | 90.000 | 40 | 250 |\n\nBuna göre ikinci dağıtımdan sonra Dolum gider yerinde toplanan genel üretim gideri kaç ₺'dir?",
        {
            'A': '137.250 ₺',
            'B': '130.100 ₺',
            'C': '137.850 ₺',
            'D': '147.000 ₺',
            'E': '132.850 ₺',
        },
        'E',
        "Kantin'den Bakım'a 44.000 ₺ × 10 / 100 = 4.400 ₺ pay düşer; Bakım'ın dağıtılacak toplamı 40.400 ₺ olur. Dolum gider yerinin toplamı: birinci dağıtım + Kantin payı + Bakım payı = 132.850 ₺.",
    ),
    # düzey 3
    '0032': patch(
        'Güneş Ambalaj işletmesi genel üretim giderlerini dönem içinde tahmini yükleme oranıyla mamullere yüklemektedir. Yıl başında tahmini genel üretim gideri 540.000 ₺, tahmini faaliyet hacmi 18.000 makine saati olarak belirlenmiştir. Dönemde fiilen 17.000 makine saati çalışılmış ve 498.000 ₺ genel üretim gideri gerçekleşmiştir.\n\nBuna göre dönem sonunda ortaya çıkan yükleme farkı aşağıdakilerden hangisidir?',
        {
            'A': '12.000 ₺ eksik yükleme',
            'B': '30.000 ₺ eksik yükleme',
            'C': '42.000 ₺ fazla yükleme',
            'D': '12.000 ₺ fazla yükleme',
            'E': '24.000 ₺ fazla yükleme',
        },
        'D',
        "Tahmini yükleme oranı 540.000 ₺ / 18.000 = 30 ₺. Yüklenen GÜG 30 ₺ × 17.000 = 510.000 ₺. Fiili GÜG 498.000 ₺ olduğundan fark 12.000 ₺'dir; yüklenen tutar fiiliden fazla olduğu için fazla yükleme söz konusudur.",
    ),
    # düzey 2
    '0033': patch(
        'Genel üretim giderlerinin mamullere yüklenmesinde kullanılacak ölçü (faaliyet hacmi) seçilirken aşağıdakilerden hangisi esas alınır?',
        {
            'A': 'Ölçünün her dönem sabit kalması',
            'B': 'Ölçünün satış hasılatıyla aynı yönde değişmemesi',
            'C': 'Gider ile ölçü arasında neden-sonuç ilişkisi olması',
            'D': 'Ölçünün vergi mevzuatında tanımlanmış bir büyüklük olması',
            'E': 'Ölçünün en küçük sayısal değeri vermesi ve kolay hesaplanması',
        },
        'C',
        'Yükleme ölçüsü, gider yerindeki giderlerin oluşmasına neden olan faaliyeti en iyi yansıtan ölçü olmalıdır; makine yoğun gider yerinde makine saati, emek yoğun gider yerinde direkt işçilik saati ya da gideri seçilir.',
    ),
    # düzey 3
    '0034': patch(
        "Toros Çimento işletmesi yardımcı gider yerlerini doğrudan dağıtım yöntemiyle dağıtmaktadır. Bakım saatleri ve enerji tüketimi (kWh) aşağıda verilmiştir (tutarlar ₺).\n\n| Gider yeri | I. dağıtım | Bakım ölçüsü | Enerji ölçüsü |\n|---|---|---|---|\n| Kırma | 90.000 | 300 | 6.000 |\n| Pişirme | 150.000 | 200 | 4.000 |\n| Bakım | 40.000 | — | — |\n| Enerji | 60.000 | — | — |\n\nBuna göre ikinci dağıtımdan sonra Kırma gider yerinde toplanan genel üretim gideri kaç ₺'dir?",
        {
            'A': '165.000 ₺',
            'B': '190.000 ₺',
            'C': '152.000 ₺',
            'D': '180.000 ₺',
            'E': '150.000 ₺',
        },
        'E',
        "Doğrudan yöntemde yardımcı gider yerleri birbirine pay vermez; giderleri yalnız esas üretim gider yerlerine ölçülere göre dağıtılır. Kırma gider yerinde toplanan tutar 150.000 ₺'dir.",
    ),
    # düzey 3
    '0035': patch(
        'I. Birinci dağıtımda özel giderler ilgili gider yerine doğrudan yüklenir.\nII. İkinci dağıtımda yardımcı gider yerlerinin giderleri esas üretim gider yerlerine aktarılır.\nIII. Üçüncü dağıtımda esas üretim gider yerlerindeki giderler mamullere yüklenir.\n\nGider dağıtımının aşamalarıyla ilgili yukarıdaki ifadelerden hangileri doğrudur?',
        {
            'A': 'I, II ve III',
            'B': 'I ve III',
            'C': 'I ve II',
            'D': 'Yalnız I',
            'E': 'II ve III',
        },
        'A',
        'Birinci dağıtımda giderler gider yerlerine, ikinci dağıtımda yardımcı gider yerlerinden esas üretim gider yerlerine, üçüncü dağıtımda esas üretim gider yerlerinden mamullere aktarılır.',
    ),
    # düzey 3
    '0036': patch(
        "Selin Ambalaj işletmesi ikinci dağıtımda kademeli yöntemi kullanmaktadır. Önce Kantin çalışan sayısına göre (Bakım dahil), ardından Bakım bakım saatine göre dağıtılmaktadır. Birinci dağıtım toplamları (₺) ve ölçüler şöyledir:\n\n| Gider yeri | I. dağıtım | Çalışan | Bakım saati |\n|---|---|---|---|\n| Kantin | 18.000 | — | — |\n| Bakım | 27.000 | 10 | — |\n| Baskı | 95.000 | 35 | 120 |\n| Kesim | 70.000 | 15 | 80 |\n\nBuna göre Bakım yardımcı gider yerinin ikinci aşamada dağıtacağı toplam tutar kaç ₺'dir?",
        {
            'A': '24.000 ₺',
            'B': '27.000 ₺',
            'C': '3.000 ₺',
            'D': '30.000 ₺',
            'E': '30.600 ₺',
        },
        'D',
        "Kademeli yöntemde önce dağıtılan Kantin, Bakım'a da pay verir: 18.000 ₺ × 10 / 60 = 3.000 ₺. Bakım'ın dağıtacağı toplam 27.000 ₺ + 3.000 ₺ = 30.000 ₺.",
    ),
    # düzey 3
    '0037': patch(
        "Toprak Seramik işletmesi genel üretim giderlerini direkt işçilik gideri esasına göre yüklemektedir. Dönemde gider yerinde toplanan genel üretim gideri 225.000 ₺, bu gider yerindeki toplam direkt işçilik gideri 450.000 ₺'dir. S mamulünden üretilen 1.250 adet için 95.000 ₺ direkt ilk madde ve malzeme ile 60.000 ₺ direkt işçilik gideri yapılmıştır.\n\nS mamulünün birim üretim maliyeti kaç ₺'dir?",
        {
            'A': '148 ₺',
            'B': '153 ₺',
            'C': '176 ₺',
            'D': '162 ₺',
            'E': '304 ₺',
        },
        'A',
        "Yükleme oranı 225.000 ₺ / 450.000 ₺ = %50. S'ye yüklenen GÜG 60.000 ₺ × %50 = 30.000 ₺. Birim maliyet (95.000 ₺ + 60.000 ₺ + 30.000 ₺) / 1.250 = 148 ₺.",
    ),
    # düzey 3
    '0038': patch(
        "Asya Döküm işletmesinin Montaj esas üretim gider yerinde ikinci dağıtım sonrası 360.000 ₺ genel üretim gideri toplanmış ve dönemde 12.000 makine saati çalışılmıştır. Bu gider yerinde üretilen K mamulünden 1.000 adet için 3.000 makine saati kullanılmış, 210.000 ₺ direkt ilk madde ve malzeme ile 120.000 ₺ direkt işçilik gideri yapılmıştır.\n\nBuna göre K mamulünün birim üretim maliyeti kaç ₺'dir?",
        {
            'A': '378 ₺',
            'B': '330 ₺',
            'C': '336 ₺',
            'D': '90 ₺',
            'E': '420 ₺',
        },
        'E',
        "Yükleme oranı 360.000 ₺ / 12.000 = 30 ₺/makine; K'ye yüklenen GÜG 30 ₺ × 3.000 = 90.000 ₺. Birim maliyet (210.000 ₺ + 120.000 ₺ + 90.000 ₺) / 1.000 = 420 ₺.",
    ),
    # düzey 3
    '0039': patch(
        "Gökçe Cam normal maliyet sistemini uygulamakta ve dönemde kapasitesinin %60'ını kullanmaktadır. 10.000 adet üretim yapılan dönemde 180.000 ₺ direkt ilk madde ve malzeme, 70.000 ₺ direkt işçilik, 250.000 ₺ genel üretim gideri, 40.000 ₺ pazarlama-satış ve 55.000 ₺ genel yönetim gideri oluşmuştur. Genel üretim giderlerinin %40'ı değişken, kalanı sabit niteliktedir.\n\nBuna göre birim üretim maliyeti kaç ₺'dir?",
        {
            'A': '40 ₺',
            'B': '35 ₺',
            'C': '44 ₺',
            'D': '46 ₺',
            'E': '50 ₺',
        },
        'C',
        "Pazarlama ve yönetim giderleri üretim maliyetine girmez. Değişken GÜG 100.000 ₺, sabit GÜG 150.000 ₺'dir; sabit giderin yalnız kullanılan kapasiteye düşen %60'ı (90.000 ₺) maliyete yüklenir. Birim maliyet (180.000 + 70.000 + 100.000 + 90.000) / 10.000 = 44 ₺.",
    ),
    # düzey 2
    '0040': patch(
        'Gider dağıtımında birinci dağıtım ile ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Özel giderler doğrudan ilgili gider yerine yüklenir',
            'B': 'Dağıtım sonunda toplam gider tutarı değişmez',
            'C': 'Esas ve yardımcı gider yerlerinin tamamına yapılır',
            'D': 'Yalnız yardımcı gider yerlerine yapılır',
            'E': 'Ortak giderler uygun anahtarlarla dağıtılır',
        },
        'D',
        'Birinci dağıtımda gider çeşitleri; özel giderler doğrudan, ortak giderler anahtarlarla olmak üzere esas, yardımcı ve hizmet gider yerlerinin tamamına dağıtılır.',
    ),
    # düzey 3
    '0041': patch(
        "Sedef Cam işletmesinde Y ve Z yardımcı gider yerlerinin birinci dağıtım toplamları sırasıyla 22.000 ₺ ve 74.000 ₺'dir. Yardımcı gider yerlerinin birbirine ve A, B esas üretim gider yerlerine verdikleri hizmet oranları şöyledir:\n\n| Hizmet veren | Y'ye (%) | Z'ye (%) | A'ya / B'ye (%) |\n|---|---|---|---|\n| Y | — | 20 | 50 / 30 |\n| Z | 10 | — | 60 / 30 |\n\nİşletme matematiksel dağıtım yöntemini kullandığına göre ikinci dağıtımda A esas üretim gider yerine yardımcı gider yerlerinden aktarılan toplam tutar kaç ₺'dir?",
        {
            'A': '63.000 ₺',
            'B': '82.000 ₺',
            'C': '76.000 ₺',
            'D': '65.000 ₺',
            'E': '70.000 ₺',
        },
        'A',
        "Y = 22.000 + 0,10Z ve Z = 74.000 + 0,20Y denklemleri çözülünce Y = 30.000 ₺, Z = 80.000 ₺ bulunur. A'ya aktarılan: %50 × 30.000 ₺ + %60 × 80.000 ₺ = 63.000 ₺.",
    ),
    # düzey 3
    '0042': patch(
        "Normal maliyet sistemini uygulayan Demir Profil işletmesinin 20.000 adet üretim yaptığı döneme ilişkin giderleri şöyledir:\n\n| Gider | Tutar (₺) |\n|---|---|\n| Direkt ilk madde | 300.000 |\n| Pazarlama-satış | 60.000 |\n| Genel üretim | 400.000 |\n| Genel yönetim | 90.000 |\n| Direkt işçilik | 120.000 |\n\nGenel üretim giderlerinin 1/4'ü değişken niteliktedir. Dönemin birim üretim maliyeti 38 ₺ olarak hesaplandığına göre işletmenin kapasite kullanım oranı yüzde kaçtır?",
        {
            'A': '%70',
            'B': '%80',
            'C': '%72',
            'D': '%56',
            'E': '%64',
        },
        'B',
        "Pazarlama ve yönetim giderleri üretim maliyetine girmez. Değişken GÜG 100.000 ₺, sabit GÜG 300.000 ₺'dir. Toplam üretim maliyeti 20.000 × 38 ₺ = 760.000 ₺; 300.000 ₺ + 120.000 ₺ + 100.000 ₺ + 300.000 ₺ × r = 760.000 ₺ eşitliğinden r = %80 bulunur.",
    ),
    # düzey 3
    '0043': patch(
        "Fırat Tekstil'de yıllık bütçeye göre genel üretim giderleri makine saati başına 20 ₺ oranında mamullere yüklenmiştir. Yıl içinde 23.000 makine saati çalışılmış, yıl sonunda yapılan karşılaştırmada 11.000 ₺ eksik yükleme olduğu anlaşılmıştır.\n\nBuna göre işletmenin dönemde fiilen gerçekleşen genel üretim gideri kaç ₺'dir?",
        {
            'A': '482.000 ₺',
            'B': '420.000 ₺',
            'C': '449.000 ₺',
            'D': '460.000 ₺',
            'E': '471.000 ₺',
        },
        'E',
        "Yüklenen GÜG 20 ₺ × 23.000 = 460.000 ₺'dir. Eksik yükleme, fiili giderin yüklenenden fazla olduğunu gösterir: 460.000 + 11.000 = 471.000 ₺.",
    ),
    # düzey 3
    '0044': patch(
        "Sahil Boya işletmesinde Depo giderleri depolanan alan (m²) esasına, Analiz biriminin giderleri yapılan analiz sayısına göre esas üretim gider yerlerine doğrudan yöntemle dağıtılmaktadır (tutarlar ₺).\n\n| Gider yeri | I. dağıtım | Depo ölçüsü | Analiz ölçüsü |\n|---|---|---|---|\n| Kazan | 175.000 | 400 | 50 |\n| Dolum | 95.000 | 600 | 30 |\n| Depo | 35.000 | — | — |\n| Analiz | 24.000 | — | — |\n\nBuna göre Dolum gider yerinde ikinci dağıtımdan sonra toplanan genel üretim gideri kaç ₺'dir?",
        {
            'A': '124.500 ₺',
            'B': '95.000 ₺',
            'C': '107.500 ₺',
            'D': '125.000 ₺',
            'E': '112.000 ₺',
        },
        'D',
        "Doğrudan yöntemde yardımcı gider yerleri birbirine pay vermez; giderleri yalnız esas üretim gider yerlerine ölçülere göre dağıtılır. Dolum gider yerinde toplanan tutar 125.000 ₺'dir.",
    ),
    # düzey 3
    '0045': patch(
        "Ilgaz Tekstil işletmesi genel üretim giderlerini direkt işçilik gideri esasına göre yüklemektedir. Dönemde gider yerinde toplanan genel üretim gideri 180.000 ₺, bu gider yerindeki toplam direkt işçilik gideri 300.000 ₺'dir. M mamulünden üretilen 2.000 adet için 160.000 ₺ direkt ilk madde ve malzeme ile 90.000 ₺ direkt işçilik gideri yapılmıştır.\n\nM mamulünün birim üretim maliyeti kaç ₺'dir?",
        {
            'A': '147 ₺',
            'B': '152 ₺',
            'C': '125 ₺',
            'D': '158 ₺',
            'E': '27 ₺',
        },
        'B',
        "Yükleme oranı 180.000 ₺ / 300.000 ₺ = %60. M'ye yüklenen GÜG 90.000 ₺ × %60 = 54.000 ₺. Birim maliyet (160.000 ₺ + 90.000 ₺ + 54.000 ₺) / 2.000 = 152 ₺.",
    ),
    # düzey 3
    '0046': patch(
        "Marmara Kâğıt işletmesinin birinci dağıtım toplamları ve yardımcı gider yerlerinin dağıtım ölçüleri (çalışan sayısı ve bakım saati) şöyledir (tutarlar ₺):\n\n| Gider yeri | I. dağıtım | Kantin ölçüsü | Bakım ölçüsü |\n|---|---|---|---|\n| Hamur | 210.000 | 30 | 120 |\n| Kurutma | 130.000 | 20 | 80 |\n| Kantin | 25.000 | — | — |\n| Bakım | 50.000 | — | — |\n\nYardımcı gider yerleri doğrudan yöntemle dağıtıldığına göre Kurutma gider yerinin ikinci dağıtım sonrası toplamı kaç ₺'dir?",
        {
            'A': '160.000 ₺',
            'B': '128.000 ₺',
            'C': '147.500 ₺',
            'D': '130.000 ₺',
            'E': '144.000 ₺',
        },
        'A',
        "Doğrudan yöntemde yardımcı gider yerleri birbirine pay vermez; giderleri yalnız esas üretim gider yerlerine ölçülere göre dağıtılır. Kurutma gider yerinde toplanan tutar 160.000 ₺'dir.",
    ),
    # düzey 2
    '0047': patch(
        'Aşağıdakilerden hangisi yardımcı üretim gider yerine örnek değildir?',
        {
            'A': 'Kalite kontrol birimi',
            'B': 'Modelhane',
            'C': 'Montaj atölyesi',
            'D': 'Bakım-onarım atölyesi',
            'E': 'Buhar ve enerji santrali',
        },
        'C',
        'Montaj atölyesinde mamul üzerinde doğrudan üretim işlemi yapıldığından esas üretim gider yeridir. Bakım, enerji, kalite kontrol ve modelhane esas üretim gider yerlerine hizmet veren yardımcı gider yerleridir.',
    ),
    # düzey 3
    '0048': patch(
        "Delta Kimya işletmesinde Y ve Z yardımcı gider yerlerinin birinci dağıtım toplamları sırasıyla 21.000 ₺ ve 47.000 ₺'dir. Yardımcı gider yerlerinin birbirine ve A, B esas üretim gider yerlerine verdikleri hizmet oranları şöyledir:\n\n| Hizmet veren | Y'ye (%) | Z'ye (%) | A'ya / B'ye (%) |\n|---|---|---|---|\n| Y | — | 25 | 45 / 30 |\n| Z | 20 | — | 50 / 30 |\n\nİşletme matematiksel dağıtım yöntemini kullandığına göre Y yardımcı gider yerinin dağıtılacak toplam tutarı kaç ₺'dir?",
        {
            'A': '55.000 ₺',
            'B': '21.000 ₺',
            'C': '30.400 ₺',
            'D': '32.000 ₺',
            'E': '68.000 ₺',
        },
        'D',
        'Denklemler Y = 21.000 + 0,20Z ve Z = 47.000 + 0,25Y biçimindedir. İkinci denklem birinciye yerleştirilince Y = 32.000 ₺, Z = 55.000 ₺ bulunur.',
    ),
    # düzey 3
    '0049': patch(
        'Batı Konfeksiyon işletmesi genel üretim giderlerini dönem içinde tahmini yükleme oranıyla mamullere yüklemektedir. Yıl başında tahmini genel üretim gideri 300.000 ₺, tahmini faaliyet hacmi 15.000 direkt işçilik saati olarak belirlenmiştir. Dönemde fiilen 16.500 direkt işçilik saati çalışılmış ve 318.000 ₺ genel üretim gideri gerçekleşmiştir.\n\nBuna göre dönem sonunda ortaya çıkan yükleme farkı aşağıdakilerden hangisidir?',
        {
            'A': '12.000 ₺ fazla yükleme',
            'B': '24.000 ₺ fazla yükleme',
            'C': '12.000 ₺ eksik yükleme',
            'D': '30.000 ₺ eksik yükleme',
            'E': '18.000 ₺ fazla yükleme',
        },
        'A',
        "Tahmini yükleme oranı 300.000 ₺ / 15.000 = 20 ₺. Yüklenen GÜG 20 ₺ × 16.500 = 330.000 ₺. Fiili GÜG 318.000 ₺ olduğundan fark 12.000 ₺'dir; yüklenen tutar fiiliden fazla olduğu için fazla yükleme söz konusudur.",
    ),
    # düzey 3
    '0050': patch(
        "Gündoğdu Mobilya işletmesinde Y ve Z yardımcı gider yerleri birbirine hizmet vermektedir. Birinci dağıtım toplamları (₺) ve birbirlerine verdikleri hizmet payları şöyledir:\n\n| Gider yeri | I. dağıtım | Hizmet payı |\n|---|---|---|\n| Y | 120.000 | Z'ye %5 |\n| Z | 100.000 | Y'ye %10 |\n\nMatematiksel dağıtım yöntemi için Y yardımcı gider yerine ilişkin yazılacak denklem aşağıdakilerden hangisidir?",
        {
            'A': 'Z = 120.000 + 0,05Y',
            'B': 'Z = 100.000 + 0,10Y',
            'C': 'Y = 120.000 + 0,05Z',
            'D': 'Y = 120.000 + 0,10Z',
            'E': 'Y = 100.000 + 0,10Z',
        },
        'D',
        "Her yardımcı gider yerinin toplamı, kendi birinci dağıtım tutarı ile diğerinden aldığı payın toplamıdır. Y, Z'nin hizmetinin %10'unu aldığından Y = 120.000 + 0,10Z yazılır.",
    ),
    # düzey 3
    '0051': patch(
        "Ekin Makine işletmesi kademeli yöntemle önce Kantin'i çalışan sayısına, sonra Bakım'ı bakım saatine göre dağıtmaktadır. Birinci dağıtım toplamları (₺) ve ölçüler şöyledir:\n\n| Gider yeri | I. dağıtım | Çalışan | Bakım saati |\n|---|---|---|---|\n| Kantin | 20.000 | — | — |\n| Bakım | 33.000 | 10 | — |\n| Torna | 150.000 | 60 | 180 |\n| Freze | 100.000 | 30 | 120 |\n\nBuna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Esas gider yerlerinin toplamı 303.000 ₺ olur',
            'B': "Bakım, Kantin'e pay vermez",
            'C': "Torna'nın toplamı 186.000 ₺ olur",
            'D': "Bakım'ın dağıtacağı toplam 35.000 ₺'dir",
            'E': "Kantin'den Bakım'a 2.000 ₺ pay düşer",
        },
        'C',
        "Kantin'den Bakım'a 2.000 ₺, Torna'ya 12.000 ₺ pay düşer; Bakım toplamı 35.000 ₺'dir ve Torna'ya 21.000 ₺ aktarılır. Torna'nın toplamı 183.000 ₺'dir. Kademeli yöntemde sonra dağıtılan gider yeri öncekine pay vermez; toplam gider 303.000 ₺ olarak korunur.",
    ),
    # düzey 2
    '0052': patch(
        'Yardımcı gider yerleri arasında karşılıklı hizmet ilişkisinin yoğun olduğu bir işletmede ikinci dağıtımda en doğru sonucu veren yöntem aşağıdakilerden hangisidir?',
        {
            'A': 'Eşit dağıtım yöntemi',
            'B': 'Kademeli yöntem',
            'C': 'Satış hasılatına göre dağıtım',
            'D': 'Doğrudan yöntem',
            'E': 'Matematiksel yöntem',
        },
        'E',
        'Matematiksel (karşılıklı) yöntem yardımcı gider yerleri arasındaki hizmetleri iki yönlü olarak dikkate aldığından teorik olarak en doğru sonucu verir.',
    ),
    # düzey 2
    '0053': patch(
        'Kademeli dağıtım yöntemiyle ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yardımcı gider yerleri belirli bir sırayla dağıtılır',
            'B': 'Sonra dağıtılan gider yeri öncekine de pay verir',
            'C': 'Önce dağıtılan gider yeri sonrakilere de pay verir',
            'D': 'Dağıtımdan sonra yardımcı gider yerlerinde bakiye kalmaz',
            'E': 'Hizmet ilişkisi tek yönlü dikkate alınır',
        },
        'B',
        'Kademeli yöntemde hizmet tek yönlü dikkate alınır; önce dağıtılan yardımcı gider yeri sonrakilere pay verir, sonra dağıtılan ise önceki gider yerlerine pay vermez.',
    ),
    # düzey 3
    '0054': patch(
        "Rüzgâr Plastik işletmesinin Montaj esas üretim gider yerinde ikinci dağıtım sonrası 240.000 ₺ genel üretim gideri toplanmış ve dönemde 8.000 makine saati çalışılmıştır. Bu gider yerinde üretilen P mamulünden 2.500 adet için 2.500 makine saati kullanılmış, 145.000 ₺ direkt ilk madde ve malzeme ile 80.000 ₺ direkt işçilik gideri yapılmıştır.\n\nBuna göre P mamulünün birim üretim maliyeti kaç ₺'dir?",
        {
            'A': '150 ₺',
            'B': '90 ₺',
            'C': '186 ₺',
            'D': '240 ₺',
            'E': '120 ₺',
        },
        'E',
        "Yükleme oranı 240.000 ₺ / 8.000 = 30 ₺/makine; P'ye yüklenen GÜG 30 ₺ × 2.500 = 75.000 ₺. Birim maliyet (145.000 ₺ + 80.000 ₺ + 75.000 ₺) / 2.500 = 120 ₺.",
    ),
    # düzey 3
    '0055': patch(
        "Altın Döküm işletmesinde Bakım yardımcı gider yerinin birinci dağıtım toplamı 56.000 ₺'dir. Dönemde Bakım; Kalıp gider yerine 90, Temizleme gider yerine 50, Kantin yardımcı gider yerine 30 ve Depo yardımcı gider yerine 30 saat hizmet vermiştir.\n\nİşletme doğrudan dağıtım yöntemini kullandığına göre Bakım'dan Kalıp gider yerine aktarılan tutar kaç ₺'dir?",
        {
            'A': '20.000 ₺',
            'B': '36.000 ₺',
            'C': '29.650 ₺',
            'D': '28.000 ₺',
            'E': '41.600 ₺',
        },
        'B',
        'Doğrudan yöntemde diğer yardımcı gider yerlerine verilen saatler dikkate alınmaz; yalnız esas üretim gider yerlerinin saatleri (90 + 50) kullanılır: 56.000 ₺ × 90 / 140 = 36.000 ₺.',
    ),
    # düzey 3
    '0056': patch(
        "Yıldız Metal işletmesinde 180.000 ₺ tutarındaki sosyal sigorta işveren payı ortak gider niteliğinde olup gider yerlerine çalışan sayısına göre dağıtılmaktadır.\n\n| Gider yeri | Çalışan |\n|---|---|\n| Döküm | 45 |\n| İşleme | 30 |\n| Bakım | 10 |\n| Kantin | 5 |\n\nBu gidere ilişkin olarak İşleme gider yerine düşen pay kaç ₺'dir?",
        {
            'A': '90.000 ₺',
            'B': '45.000 ₺',
            'C': '10.000 ₺',
            'D': '20.000 ₺',
            'E': '60.000 ₺',
        },
        'E',
        "Dağıtım anahtarı çalışan toplamı 90'dir. İşleme gider yerinin payı 180.000 ₺ × 30 / 90 = 60.000 ₺.",
    ),
    # düzey 2
    '0057': patch(
        'Aşağıdakilerden hangisi genel üretim gideri kapsamında yer almaz?',
        {
            'A': 'Satış elemanlarının prim giderleri',
            'B': 'Üretim yöneticisinin ücreti',
            'C': 'Fabrika binasının amortismanı',
            'D': 'Üretimde kullanılan işletme malzemesi',
            'E': 'Makinelerin bakım ve onarım gideri',
        },
        'A',
        'Satış elemanlarının primleri pazarlama, satış ve dağıtım giderleridir. Üretim yöneticisinin ücreti, fabrika amortismanı, işletme malzemesi ve makine bakımı genel üretim gideridir.',
    ),
    # düzey 2
    '0058': patch(
        "Tekdüzen Hesap Planı'nın 7/A seçeneğinde dönem içinde yapılan genel üretim giderleri hangi hesapta izlenir?",
        {
            'A': '720 Direkt İşçilik Giderleri',
            'B': '710 Direkt İlk Madde ve Malzeme Giderleri',
            'C': '740 Hizmet Üretim Maliyeti',
            'D': '730 Genel Üretim Giderleri',
            'E': '760 Pazarlama, Satış ve Dağıtım Giderleri',
        },
        'D',
        '7/A seçeneğinde genel üretim giderleri 730 Genel Üretim Giderleri hesabında toplanır, dönem sonunda yansıtma hesabı aracılığıyla 151 Yarı Mamuller – Üretim hesabına aktarılır.',
    ),
    # düzey 2
    '0059': patch(
        'Matematiksel (karşılıklı) dağıtım yöntemi ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tek yardımcı gider yeri bulunan işletmeler için geliştirilmiştir',
            'B': 'Karşılıklı hizmetler denklem sistemiyle dikkate alınır',
            'C': 'Yardımcı gider yerleri belirli bir sırayla ve tek yönlü dağıtılır',
            'D': 'Esas üretim gider yerlerinin birbirine verdiği hizmeti dikkate alır',
            'E': 'Yardımcı gider yerleri arasındaki hizmet göz ardı edilerek dağıtılır',
        },
        'B',
        'Matematiksel yöntemde her yardımcı gider yerinin toplamı, kendi birinci dağıtım tutarı ile diğer yardımcı gider yerinden aldığı payın toplamı olarak yazılır ve denklem sistemi çözülür.',
    ),
    # düzey 3
    '0060': patch(
        "Kuzey Plastik işletmesinin dönem elektrik faturası 96.000 ₺'dir ve sayaç ölçümlerine göre dağıtılmaktadır.\n\n| Gider yeri | Tüketim (kWh) |\n|---|---|\n| Kalıp | 6.000 |\n| Montaj | 3.000 |\n| Enerji | 2.000 |\n| Depo | 1.000 |\n\nElektrik giderinin birinci dağıtımında Montaj gider yerinin payı kaç ₺'dir?",
        {
            'A': '48.000 ₺',
            'B': '32.000 ₺',
            'C': '24.000 ₺',
            'D': '72.000 ₺',
            'E': '16.000 ₺',
        },
        'C',
        "Dağıtım anahtarı tüketim (kWh) toplamı 12.000'dir. Montaj gider yerinin payı 96.000 ₺ × 3.000 / 12.000 = 24.000 ₺.",
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
    print(f"1 paket / {len(PATCHES)} soru ('Gider Dagitimi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
