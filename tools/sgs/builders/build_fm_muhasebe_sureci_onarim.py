#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Muhasebe Sureci ve Hesap Plani — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

FM cok adimli tur (hafif). Kavram/surec agirlikli 60 soru korundu (gercek sinavdaki kavram payina karsilik gelir). 19 mutlak ifadeli sik dogruluk degeri korunarak onarildi; cozumlerdeki '**X yanlistir**' harf atiflari kaldirildi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 1 Sira No'lu MSUGT · Tekduzen Hesap Plani
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/finansal_muhasebe/muhasebe_sureci_hesap_plani.json"
STYLE_REF = 'SGS Finansal Muhasebe (uygulama; sınav stiline kalibre)'
ONEK = "finmuh-surec-gen-"


def patch(stem, options, answer, solution, ref="1 Sira No'lu MSUGT - Hesaplarin isleyisi"):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Bir işletmenin 320 Satıcılar hesabı mart ayı başında 85.000 ₺ alacak kalanı vermektedir. Ay içinde satıcılarla ilgili şu işlemler yapılmıştır:\n\n(1) 40.000 ₺ + %20 KDV tutarında ticari mal veresiye alınmıştır.\n\n(2) Bir satıcıya 30.000 ₺ banka havalesi yapılmıştır.\n\n(3) Bir satıcıya olan senetsiz borcun 20.000 ₺'lik kısmı için bono düzenlenip verilmiştir.\n\n(4) Veresiye alınan mallardan 6.000 ₺ + %20 KDV tutarındaki kısım kusurlu olduğu için satıcıya iade edilmiştir.\n\nBuna göre 320 Satıcılar hesabı mart ayı sonunda kaç ₺ alacak kalanı verir?",
        {
            'A': '83.000',
            'B': '67.800',
            'C': '75.800',
            'D': '95.800',
            'E': '77.000',
        },
        'C',
        "320 Satıcılar, senetsiz ticari borçları izleyen pasif hesaptır; borç doğunca alacaklandırılır, azalınca borçlandırılır. Alış KDV dâhil 48.000 ₺ alacağa yazılır; havale (30.000 ₺), bono verilmesi (borç 321'e aktarılır, 20.000 ₺) ve KDV dâhil iade (7.200 ₺) borca yazılır. Kalan = 85.000 + 48.000 − 30.000 − 20.000 − 7.200 = 75.800 ₺ alacak.",
        "1 Sıra No'lu MSUGT - Hesapların işleyişi",
    ),
    # düzey 3
    '0002': patch(
        'Genel geçici mizan ve genel kesin mizan ile ilgili aşağıdaki ifadelerden hangileri yanlıştır?\n\nI. Genel geçici mizan, dönem sonu envanter ve düzeltme kayıtlarından sonra düzenlenir.\n\nII. Genel kesin mizanın kalanlar sütunu, dönem sonu bilançosu ve gelir tablosu verilerini oluşturur.\n\nIII. Mizanda borç kalanları toplamı ile alacak kalanları toplamı eşit olmalıdır.\n\nIV. Aylık mizanlar dönem içinde hesapların kontrolü amacıyla düzenlenebilir.',
        {
            'A': 'Yalnız I',
            'B': 'II ve III',
            'C': 'I, II ve IV',
            'D': 'III ve IV',
            'E': 'I ve II',
        },
        'A',
        '**Yalnız I yanlıştır:** genel geçici mizan, envanter ve düzeltme kayıtlarından **önce** düzenlenir; envanter sonrası düzenlenen **kesin mizan**dır. II, III ve IV doğrudur.',
        "1 Sıra No'lu MSUGT - Mizan türleri; dönem sonu işlemleri",
    ),
    # düzey 2
    '0003': patch(
        'Bir işletmenin dönem sonu kesin mizanından alınan kalanlar şöyledir: 100 Kasa 40.000 ₺, 102 Bankalar 160.000 ₺, 103 Verilen Çekler ve Ödeme Emirleri 20.000 ₺, 120 Alıcılar 250.000 ₺, 129 Şüpheli Ticari Alacaklar Karşılığı 30.000 ₺, 153 Ticari Mallar 300.000 ₺, 254 Taşıtlar 400.000 ₺, 257 Birikmiş Amortismanlar 150.000 ₺, 320 Satıcılar 220.000 ₺.\n\nBuna göre işletmenin bilançosunda dönen varlıklar toplamı kaç ₺ olur?',
        {
            'A': '750.000',
            'B': '700.000',
            'C': '720.000',
            'D': '950.000',
            'E': '730.000',
        },
        'B',
        '103 Verilen Çekler ve Ödeme Emirleri hazır değerleri, 129 Şüpheli Ticari Alacaklar Karşılığı ticari alacakları düzenleyen (alacak kalanı veren) aktif düzenleyici hesaplardır ve dönen varlıklardan düşülür. Dönen varlıklar = 40.000 + 160.000 − 20.000 + 250.000 − 30.000 + 300.000 = 700.000 ₺. 254 Taşıtlar ile 257 Birikmiş Amortismanlar duran varlık grubundadır; 320 Satıcılar ise kısa vadeli yabancı kaynaktır.',
        "1 Sıra No'lu MSUGT - Aktifi düzenleyici hesaplar",
    ),
    # düzey 2
    '0004': patch(
        "Tekdüzen Hesap Planı'nda gelir tablosu hesapları (6 sınıfı) ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Gelir hesapları alacak, gider hesapları borç kalanı verir ve dönem sonunda 690'a devredilir.",
            'B': "Tüm 6'lı hesaplar dönem sonunda kapatılmayıp kalanlarıyla bilançoya devredilir.",
            'C': 'Gelir hesapları borç, gider hesapları alacak kalanı verir; her ikisi de dönem sonunda bilançoda gösterilir.',
            'D': "6'lı sınıftaki tüm hesaplar nazım hesaplarla birlikte çalışan hesaplardır.",
            'E': "6'lı hesaplar aktifi düzenleyici hesaplar olup ilgili varlığın altında (-) gösterilir.",
        },
        'A',
        "6'lı sınıfta **gelir/hasılat hesapları alacak**, **gider hesapları borç** kalanı verir. Dönem sonunda bu hesaplar **690 Dönem Kârı veya Zararı**na devredilerek kapatılır; kalanları bilançoya değil gelir tablosuna yansır.",
        "1 Sıra No'lu MSUGT - Gelir tablosu hesapları",
    ),
    # düzey 2
    '0005': patch(
        "İşletme, satıcısına olan 90.000 ₺ senetsiz ticari borcunu şu şekilde kapatmıştır: 30.000 ₺'yi bankadan havale etmiş, 40.000 ₺ için üç ay vadeli bir bono düzenleyip vermiş, kalan tutar için de portföyündeki bir müşteri çekini ciro ederek satıcıya teslim etmiştir.\n\nBu işlemin yevmiye kaydında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '320 Satıcılar hesabı 70.000 ₺ borçlandırılır',
            'B': '321 Borç Senetleri hesabı 40.000 ₺ alacaklandırılır',
            'C': '101 Alınan Çekler hesabı 20.000 ₺ borçlandırılır',
            'D': '103 Verilen Çekler ve Ödeme Emirleri hesabı 20.000 ₺ alacaklandırılır',
            'E': '102 Bankalar hesabı 30.000 ₺ borçlandırılır',
        },
        'B',
        "Kayıt: 320 Satıcılar 90.000 ₺ borç; 102 Bankalar 30.000 ₺, 321 Borç Senetleri 40.000 ₺ ve 101 Alınan Çekler 20.000 ₺ alacak. Ciro edilen çek işletmenin kendi çeki olmadığından 103 değil 101 hesabından çıkar; bankadan yapılan ödeme 102'yi azaltır (alacak).",
        "1 Sıra No'lu MSUGT - 320/321 (ticari borçlar)",
    ),
    # düzey 3
    '0006': patch(
        'Muhasebe döngüsünde aşağıdaki işlemlerin doğru sıralaması hangisidir?\n\nI. Mali tabloların düzenlenmesi\n\nII. Yevmiye defterine kayıt\n\nIII. Defter-i kebire aktarma\n\nIV. Genel geçici mizan düzenleme\nV. Dönem sonu envanter ve düzeltme kayıtları',
        {
            'A': 'II → IV → III → V → I',
            'B': 'III → II → IV → V → I',
            'C': 'II → III → V → IV → I',
            'D': 'IV → III → II → V → I',
            'E': 'II → III → IV → V → I',
        },
        'E',
        'Doğru akış: **Yevmiye (II) → Defter-i kebir (III) → Genel geçici mizan (IV) → Envanter ve düzeltme kayıtları (V) → Mali tablolar (I)**. Envanter/düzeltmeler geçici mizandan sonra, mali tablolardan öncedir.',
        "1 Sıra No'lu MSUGT - Muhasebe süreci",
    ),
    # düzey 2
    '0007': patch(
        "Dönem başında varlıkları 900.000 ₺, yabancı kaynakları 350.000 ₺ olan bir işletmede dönem içinde şu işlemler yapılmıştır (KDV ihmal edilecektir):\n\n(1) 120.000 ₺'lik ticari mal veresiye alınmıştır.\n\n(2) Maliyeti 80.000 ₺ olan ticari mal 110.000 ₺'ye peşin satılmıştır.\n\n(3) 50.000 ₺ banka kredisi anaparası geri ödenmiştir.\n\n(4) İşletme sahibi kişisel ihtiyacı için kasadan 60.000 ₺ çekmiştir.\n\n(5) Döneme ait 25.000 ₺ kira gideri nakden ödenmiştir.\n\nBuna göre işletmenin dönem sonu özkaynak tutarı kaç ₺'dir?",
        {
            'A': '445.000',
            'B': '520.000',
            'C': '495.000',
            'D': '465.000',
            'E': '415.000',
        },
        'C',
        'Başlangıç özkaynağı = 900.000 − 350.000 = 550.000 ₺. Veresiye alış ve kredi ödemesi varlık ile yabancı kaynağı birlikte değiştirir, özkaynağı etkilemez. Satış kârı (110.000 − 80.000 = 30.000 ₺) özkaynağı artırır; sahibin çektiği 60.000 ₺ ve 25.000 ₺ kira gideri azaltır. Dönem sonu özkaynak = 550.000 + 30.000 − 60.000 − 25.000 = 495.000 ₺ (kontrol: varlıklar 915.000 − yabancı kaynaklar 420.000).',
        "1 Sıra No'lu MSUGT - Bilanço eşitliği",
    ),
    # düzey 2
    '0008': patch(
        'Malın bir yerden başka bir yere taşınması (sevki) sırasında düzenlenen ve malın yanında bulunması gereken belge aşağıdakilerden hangisidir?',
        {
            'A': 'Ödeme kaydedici cihaz fişi',
            'B': 'Fatura',
            'C': 'Serbest meslek makbuzu',
            'D': 'Sevk irsaliyesi',
            'E': 'Gider pusulası',
        },
        'D',
        '**Sevk irsaliyesi**, malın sevki/taşınması sırasında düzenlenir ve malın yanında bulunur; malın hareketini belgeler (VUK md. 230).',
        'VUK md. 230 (sevk irsaliyesi)',
    ),
    # düzey 2
    '0009': patch(
        'Serbest meslek erbabının (avukat, mali müşavir, doktor vb.) mesleki faaliyeti karşılığında yaptığı tahsilatlar için düzenlediği belge aşağıdakilerden hangisidir?',
        {
            'A': 'Serbest meslek makbuzu',
            'B': 'Fatura',
            'C': 'Gider pusulası',
            'D': 'Müstahsil makbuzu',
            'E': 'Sevk irsaliyesi',
        },
        'A',
        '**Serbest meslek makbuzu**, serbest meslek erbabının mesleki faaliyeti karşılığı yaptığı tahsilatlar için düzenlediği belgedir (VUK md. 236).',
        'VUK md. 236 (serbest meslek makbuzu)',
    ),
    # düzey 2
    '0010': patch(
        'Üç ortak, her birinin payı eşit olmak üzere 900.000 ₺ sermayeli bir anonim şirket kurmuştur. Ortak A payını tamamen nakit olarak bankaya yatırmış, ortak B payı karşılığında 300.000 ₺ değerindeki bir taşıtı şirkete devretmiş, ortak C ise nakit payının yarısını tescilden önce bankaya yatırmış, kalanını yirmi dört ay içinde ödemeyi taahhüt etmiştir.\n\nTaahhüt ve ödeme kayıtları yapıldıktan sonra aşağıdakilerden hangisi doğrudur?',
        {
            'A': '500 Sermaye hesabı 750.000 ₺ alacaklandırılmıştır',
            'B': '254 Taşıtlar hesabı 150.000 ₺ borçlandırılmıştır',
            'C': '102 Bankalar hesabı 600.000 ₺ borçlandırılmıştır',
            'D': '501 Ödenmemiş Sermaye hesabı 900.000 ₺ alacaklandırılmıştır',
            'E': '501 Ödenmemiş Sermaye hesabı 150.000 ₺ borç kalanı verir',
        },
        'E',
        "Taahhüt kaydı: 501 Ödenmemiş Sermaye 900.000 ₺ borç / 500 Sermaye 900.000 ₺ alacak. Ödemeler: 102 Bankalar 450.000 ₺ (A'nın 300.000 + C'nin 150.000) ve 254 Taşıtlar 300.000 ₺ borç / 501 Ödenmemiş Sermaye 750.000 ₺ alacak. 501, özkaynakları düzenleyen borç kalanlı hesaptır; C'nin ödenmemiş 150.000 ₺'si borç kalanı olarak kalır. TTK m. 344'e göre nakdî payların en az dörtte biri tescilden önce ödenir.",
        "1 Sıra No'lu MSUGT - 500 Sermaye",
    ),
    # düzey 3
    '0011': patch(
        'Bir ticaret işletmesinin dönem sonunda gelir tablosu hesaplarının kalanları şöyledir: 600 Yurt İçi Satışlar 900.000 ₺ alacak, 610 Satıştan İadeler 40.000 ₺ borç, 621 Satılan Ticari Mallar Maliyeti 500.000 ₺ borç, 632 Genel Yönetim Giderleri 90.000 ₺ borç, 642 Faiz Gelirleri 15.000 ₺ alacak, 689 Diğer Olağandışı Gider ve Zararlar 5.000 ₺ borç.\n\nBu hesapların 690 Dönem Kârı veya Zararı hesabına aktarılmasıyla ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': '600 hesabı 900.000 ₺ borçlandırılarak kapatılır',
            'B': '610 hesabı 40.000 ₺ alacaklandırılarak kapatılır',
            'C': '621 hesabının kalanı 690 hesabının borcuna aktarılır',
            'D': 'Aktarmalardan sonra 690, 230.000 ₺ alacak kalanı verir',
            'E': '642 hesabının kalanı 690 hesabının alacağına aktarılır',
        },
        'D',
        "Gelir hesapları (600, 642) borçlandırılıp 690'ın alacağına, gider ve indirim hesapları (610, 621, 632, 689) alacaklandırılıp 690'ın borcuna aktarılır. 690 alacak toplamı 915.000 ₺, borç toplamı 635.000 ₺'dir; hesap 280.000 ₺ alacak kalanı (dönem kârı) verir.",
        "1 Sıra No'lu MSUGT - Gelir tablosu hesapları",
    ),
    # düzey 2
    '0012': patch(
        "'T hesabı' düzeniyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Hesabın adı T'nin üst çizgisine yazılır",
            'B': 'Sol taraf alacak, sağ taraf borç tarafıdır',
            'C': 'Her işlem tutarı hesabın ilgili tarafına yazılır',
            'D': 'Aktif hesaplardaki artışlar borç tarafına yazılır',
            'E': 'Pasif hesaplardaki artışlar alacak tarafına yazılır',
        },
        'B',
        'T hesabında hesabın adı üst çizgiye yazılır; sol taraf BORÇ, sağ taraf ALACAK tarafıdır. Aktif hesaplar artışlarda borçlandırılır, pasif hesaplar artışlarda alacaklandırılır.',
        "1 Sıra No'lu MSUGT - Hesap kavramı (T hesabı)",
    ),
    # düzey 2
    '0013': patch(
        "Tekdüzen Hesap Planı'ndaki 253 TESİS, MAKİNE VE CİHAZLAR hesabının kod yapısıyla ilgili aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': 'İlk rakam muavin hesabı, son rakam hesap sınıfını gösterir.',
            'B': '25 kodu gelir tablosu hesap sınıfını gösterir.',
            'C': 'İlk rakam olan 2 hesap sınıfını, ilk iki rakam olan 25 hesap grubunu, 253 ise büyük defter hesabını gösterir.',
            'D': '253 nazım hesaplarda kullanılan boş bir koddur.',
            'E': 'Hesap kodundaki rakamların sınıf, grup ve hesap bakımından herhangi bir anlamı yoktur.',
        },
        'C',
        'Tekdüzen Hesap Planı hiyerarşiktir: **2 Duran Varlıklar** hesap sınıfını, **25 Maddi Duran Varlıklar** hesap grubunu, **253 Tesis, Makine ve Cihazlar** ise büyük defter hesabını gösterir.',
        "1 Sıra No'lu MSUGT - Tekdüzen Hesap Çerçevesi ve Hesap Planı",
    ),
    # düzey 2
    '0014': patch(
        "Sürekli envanter yöntemini uygulayan işletme, liste fiyatı 80.000 ₺ olan ticari malı %10 ticari iskontoyla ve %20 KDV ile satın almıştır. KDV dâhil bedelin 30.000 ₺'si peşin ödenmiş, kalanı veresiyedir. Malın işletmenin deposuna taşınması için nakliyeciye ayrıca 2.000 ₺ + %20 KDV nakit ödenmiştir.\n\nBu işlemlerin kayıtlarında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '320 Satıcılar hesabı 86.400 ₺ alacaklandırılır',
            'B': '153 Ticari Mallar hesabı toplam 74.000 ₺ borçlandırılır',
            'C': '191 İndirilecek KDV hesabı 16.000 ₺ borçlandırılır',
            'D': '760 Pazarlama Satış ve Dağıtım Giderleri 2.000 ₺ borçlandırılır',
            'E': '100 Kasa hesabı toplam 30.000 ₺ alacaklandırılır',
        },
        'B',
        'Ticari iskonto faturada düşülür: mal bedeli 72.000 ₺, KDV 14.400 ₺. Alış nakliyesi malın maliyetine eklenir: 153 = 72.000 + 2.000 = 74.000 ₺; 191 = 14.400 + 400 = 14.800 ₺. Kasadan çıkan 30.000 + 2.400 = 32.400 ₺; 320 Satıcılar = 86.400 − 30.000 = 56.400 ₺ alacak.',
        '3065 s. KDVK; 191 İndirilecek KDV; 2026 KDV %20',
    ),
    # düzey 2
    '0015': patch(
        'İşletme, portföyündeki 60.000 ₺ nominal değerli müşteri senedini vadesinde tahsil edilmek üzere bankaya vermiştir. Banka senedi vadesinde tahsil etmiş, 300 ₺ tahsil komisyonunu keserek kalan tutarı işletmenin vadesiz hesabına aktarmış ve dekontu göndermiştir.\n\nTahsilat kaydında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?',
        {
            'A': '102 Bankalar hesabı 60.000 ₺ borçlandırılır',
            'B': '121 Alacak Senetleri hesabı 59.700 ₺ alacaklandırılır',
            'C': '780 Finansman Giderleri hesabı 300 ₺ borçlandırılır',
            'D': '653 Komisyon Giderleri hesabı 300 ₺ borçlandırılır',
            'E': '120 Alıcılar hesabı 60.000 ₺ alacaklandırılır',
        },
        'D',
        "Kayıt: 102 Bankalar 59.700 ₺ ve 653 Komisyon Giderleri 300 ₺ borç / 121 Alacak Senetleri 60.000 ₺ alacak. Senet nominal değeriyle 121'den çıkar; bankanın kestiği tahsil komisyonu bir finansman maliyeti değil, diğer olağan gider niteliğindeki komisyon gideridir.",
        "1 Sıra No'lu MSUGT - 121 Alacak Senetleri",
    ),
    # düzey 2
    '0016': patch(
        "Bir anonim şirketin dönem sonu bilançosuna esas kalanlar şöyledir: 500 Sermaye 1.000.000 ₺, 501 Ödenmemiş Sermaye 200.000 ₺, 520 Hisse Senedi İhraç Primleri 30.000 ₺, 540 Yasal Yedekler 80.000 ₺, 580 Geçmiş Yıllar Zararları 120.000 ₺, 590 Dönem Net Kârı 90.000 ₺. Ayrıca 320 Satıcılar hesabının 150.000 ₺ alacak kalanı bulunmaktadır.\n\nBuna göre şirketin özkaynak toplamı kaç ₺'dir?",
        {
            'A': '760.000',
            'B': '850.000',
            'C': '700.000',
            'D': '800.000',
            'E': '880.000',
        },
        'E',
        '501 Ödenmemiş Sermaye ve 580 Geçmiş Yıllar Zararları özkaynakları düzenleyen, borç kalanı veren hesaplardır ve (−) olarak gösterilir. Özkaynak = 1.000.000 − 200.000 + 30.000 + 80.000 − 120.000 + 90.000 = 880.000 ₺. 320 Satıcılar yabancı kaynaktır.',
        "1 Sıra No'lu MSUGT - 501 Ödenmemiş Sermaye",
    ),
    # düzey 2
    '0017': patch(
        "Bir işletmenin önceki dönem kapanış bilançosunda şu kalemler yer almaktadır: Kasa 20.000 ₺, Alıcılar 80.000 ₺, Ticari Mallar 150.000 ₺, Demirbaşlar 100.000 ₺, Birikmiş Amortismanlar 30.000 ₺, Satıcılar 70.000 ₺, Banka Kredileri 50.000 ₺, Sermaye 200.000 ₺. İşletme yeni dönemin ilk günü bu kalanları yevmiye defterine açılış kaydıyla aktarmaktadır.\n\nBuna göre açılış kaydının borç tarafının toplamı kaç ₺'dir?",
        {
            'A': '350.000',
            'B': '380.000',
            'C': '420.000',
            'D': '400.000',
            'E': '370.000',
        },
        'A',
        'Açılış kaydında borç kalanı veren aktif hesaplar borca, alacak kalanı veren hesaplar alacağa yazılır. Birikmiş Amortismanlar aktifi düzenleyen ve alacak kalanı veren bir hesap olduğundan alacak tarafındadır. Borç: 20.000 + 80.000 + 150.000 + 100.000 = 350.000 ₺; alacak: 30.000 + 70.000 + 50.000 + 200.000 = 350.000 ₺.',
        "1 Sıra No'lu MSUGT - Açılış kaydı",
    ),
    # düzey 2
    '0018': patch(
        "Tekdüzen Muhasebe Sistemi'nin (MSUGT) temel amaçlarından biri aşağıdakilerden hangisidir?",
        {
            'A': 'İşletmelerin yasal yollarla daha az vergi ödemesini sağlayarak vergi yükünü en aza indirmek',
            'B': 'İşletmeleri mali tablo düzenleme yükümlülüğünden kurtararak raporlama yükünü kaldırmak',
            'C': 'Muhasebe bilgilerinin tekdüze, tutarlı ve karşılaştırılabilir biçimde üretilmesini sağlamak',
            'D': 'Büyük ölçekli işletmelerin muhasebe tutmasını sağlayıp küçük işletmeleri kapsam dışı bırakmak',
            'E': 'Her işletmeye kendi belirlediği hesap kodlarını kullandırarak ortak bir plandan vazgeçmek',
        },
        'C',
        "Tekdüzen Muhasebe Sistemi'nin amacı; muhasebe bilgilerinin **tekdüze, tutarlı, gerçeğe uygun ve karşılaştırılabilir** biçimde üretilip sunulmasını sağlamaktır (ortak hesap planı ve ilkeler).",
        "1 Sıra No'lu MSUGT - Sistemin amaçları",
    ),
    # düzey 3
    '0019': patch(
        'Bir işletmenin yevmiye defterindeki bir maddede 153 Ticari Mallar hesabına 40.000 ₺ ve 191 İndirilecek KDV hesabına 8.000 ₺ borç; 159 Verilen Sipariş Avansları hesabına 18.000 ₺ ve 320 Satıcılar hesabına 30.000 ₺ alacak kaydedilmiştir.\n\nBu yevmiye maddesi aşağıdaki işlemlerden hangisine aittir?',
        {
            'A': "Satıcıya 48.000 ₺ sipariş avansı verilmesi, bunun 18.000 ₺'sinin peşin ödenmesi",
            'B': "Müşteriden 18.000 ₺ avans alınarak 40.000 ₺'lik mal satılması",
            'C': 'Satıcıya iade edilen malın bedelinin avanstan düşülmesi',
            'D': "Avansın 30.000 ₺'lik kısmının satıcıdan geri alınması",
            'E': 'Avans verilen malın teslim alınması, kalan bedelin veresiye bırakılması',
        },
        'E',
        "Borçta 153 ve 191'in bulunması KDV'li bir mal alışını gösterir: KDV dâhil bedel 48.000 ₺. Bunun 18.000 ₺'si daha önce verilen sipariş avansından mahsup edilmiş (159 alacak), kalan 30.000 ₺ satıcıya borç yazılmıştır (320 alacak). Avans alınması 340 hesabını, mal satışı 600 ve 391 hesaplarını çalıştırırdı.",
        "1 Sıra No'lu MSUGT - 131 Ortaklardan Alacaklar",
    ),
    # düzey 2
    '0020': patch(
        'Muhasebe bilgi sisteminde her kaydın belge numarası, kaydı oluşturan kullanıcı, tarih-saat bilgisi ve sonradan yapılan değişiklikleri saklanmaktadır.\n\nBu bilgilerin birlikte tutulması aşağıdakilerden hangisini sağlar?',
        {
            'A': 'Her işlemin sözlü beyana dayanarak kaydedilmesi',
            'B': 'Borç ve alacak eşitliği aranmadan tek taraflı kayıt yapılması',
            'C': 'Kaynak belgelerin sistemden bağımsız olarak yok edilmesi',
            'D': 'Kayıtların kaynağından mali tablolara ve geriye doğru izlenebilmesini sağlayan denetim izi',
            'E': 'Kullanıcıların geçmiş kayıtları iz bırakmadan değiştirebilmesi',
        },
        'D',
        'Belge numarası, kullanıcı, zaman damgası ve değişiklik geçmişi; işlemin kaynağından rapora, rapordan kaynak belgeye kadar izlenmesini sağlar. Bu kayıt zinciri **denetim izi (audit trail)** olarak adlandırılır.',
        'Muhasebe Bilgi Sistemleri - işlem kayıtları ve denetim izi',
    ),
    # düzey 3
    '0021': patch(
        'Bir işletmenin yevmiye defterindeki bir maddede 100 Kasa hesabına 36.000 ₺ ve 121 Alacak Senetleri hesabına 84.000 ₺ borç; 600 Yurt İçi Satışlar hesabına 100.000 ₺ ve 391 Hesaplanan KDV hesabına 20.000 ₺ alacak kaydedilmiştir.\n\nBu yevmiye maddesi aşağıdaki işlemlerden hangisine aittir?',
        {
            'A': "120.000 ₺'lik mal alınıp bedelin bir kısmının senetle ödenmesi",
            'B': "Müşteriden 84.000 ₺'lik senet ve 36.000 ₺ nakit tahsil edilmesi",
            'C': 'Mal satışı; KDV dâhil bedelin bir kısmı peşin, kalanı senetle',
            'D': 'Senetli satışta müşteriye 20.000 ₺ iskonto yapılması',
            'E': "Müşteriden alınan 100.000 ₺'lik avansın satışla mahsup edilmesi",
        },
        'C',
        "600 ve 391'in alacaklandırılması KDV'li bir satışı gösterir: matrah 100.000 ₺, KDV 20.000 ₺, toplam 120.000 ₺. Bedelin 36.000 ₺'si nakit (100 borç), 84.000 ₺'si için alacak senedi alınmıştır (121 borç). Yalnız alacak tahsili gelir hesabı çalıştırmaz; iskonto 611'i, avans mahsubu 340'ı borçlandırırdı.",
        "1 Sıra No'lu MSUGT; 3065 s. KDVK (peşin satış kaydı)",
    ),
    # düzey 2
    '0022': patch(
        "Verdiği çekleri 103 Verilen Çekler ve Ödeme Emirleri hesabında izleyen bir işletmenin 102 Bankalar hesabı ay başında 120.000 ₺ borç kalanı vermektedir. Ay içindeki işlemler:\n\n(1) Bir müşteri 85.000 ₺ borcunu havale ile ödemiştir.\n\n(2) Bir satıcıya 60.000 ₺ havale yapılmıştır.\n\n(3) Bankadan 100.000 ₺ kredi kullanılmış; banka 1.500 ₺ dosya masrafını keserek kalanı hesaba aktarmıştır.\n\n(4) Geçen ay bir satıcıya verilen 25.000 ₺'lik çek bankaya ibraz edilerek hesaptan ödenmiştir.\n\n(5) Kasadaki paranın 15.000 ₺'si bankaya yatırılmıştır.\n\nBuna göre 102 Bankalar hesabı ay sonunda kaç ₺ borç kalanı verir?",
        {
            'A': '233.500',
            'B': '258.500',
            'C': '235.000',
            'D': '218.500',
            'E': '208.500',
        },
        'A',
        "Bankaya giren tutarlar borca, çıkanlar alacağa yazılır: 120.000 + 85.000 − 60.000 + 98.500 − 25.000 + 15.000 = 233.500 ₺ borç kalanı. Kredide hesaba net 98.500 ₺ girer. Verilen çek, verildiği gün 103'e alacak yazılmıştı; bankaya ibraz edilip ödendiğinde 103 borç / 102 alacak kaydı yapılır.",
        "1 Sıra No'lu MSUGT - Hesap kalanı",
    ),
    # düzey 2
    '0023': patch(
        'Kasayı ilgilendirmeyen (nakit giriş-çıkışı olmayan) muhasebe işlemleri için düzenlenen fiş türü aşağıdakilerden hangisidir?',
        {
            'A': 'Tahsil Fişi',
            'B': 'Tediye Fişi',
            'C': 'Gider Pusulası',
            'D': 'Mahsup Fişi',
            'E': 'İrsaliye',
        },
        'D',
        'Kasadan tahsilat için **tahsil fişi**, kasadan ödeme için **tediye fişi**, kasayı ilgilendirmeyen (ör. senetli mal alışı) işlemler için ise **mahsup fişi** düzenlenir.',
        'Muhasebe fiş düzeni (tahsil/tediye/mahsup)',
    ),
    # düzey 3
    '0024': patch(
        'Çift taraflı kayıt yöntemi ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Yöntem, hesapların borç ve alacak taraflarının birlikte kullanılmasına dayanır.',
            'B': 'Bir işlemde borç tutarları toplamı, alacak tutarları toplamına eşittir.',
            'C': 'Bilanço eşitliğinin korunmasını sağlar.',
            'D': 'Her işlem en az iki hesabı etkiler.',
            'E': 'Her işlem tek bir hesaba tek taraflı kaydedilir.',
        },
        'E',
        'Çift taraflı kayıtta her işlem en az iki hesabı etkiler ve borç = alacak eşitliği korunur; tek hesaba tek taraflı kayıt yapılmaz. Diğer ifadeler doğrudur.',
        "1 Sıra No'lu MSUGT - Çift taraflı kayıt",
    ),
    # düzey 2
    '0025': patch(
        "Tekdüzen Hesap Planı'nda '7 - Maliyet Hesapları' sınıfı ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İşletmenin uzun vadeli banka kredilerini ve çıkardığı tahvil borçlarını dönem boyunca ayrıntılı biçimde izleyen sınıftır.',
            'B': 'Ticaret işletmelerinde kullanılır; üretim yapan sanayi işletmelerinde açılmaz.',
            'C': 'Giderlerin çeşit (7/A) veya yerlerine göre izlenip mamul/hizmet maliyetlerine yüklenmesini sağlar.',
            'D': 'İşletmenin özkaynak hareketlerini, sermaye artış ve azalışlarını izlemek için kullanılır.',
            'E': 'Nazım hesaplarla aynı işlevi görür; mali tablo dengesini etkilemez.',
        },
        'C',
        '**7 Maliyet Hesapları**, giderlerin çeşitlerine (7/A) veya gider yerlerine göre izlenip mamul/hizmet maliyetlerine yüklenmesi içindir. İşletmeler 7/A veya 7/B seçeneğinden birini uygular.',
        "1 Sıra No'lu MSUGT - Maliyet hesapları (7/A-7/B)",
    ),
    # düzey 2
    '0026': patch(
        "Tekdüzen Hesap Planı'nda '9 - Nazım Hesaplar' ile ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Teminat ve emanet gibi bilgileri izler',
            'B': 'Varlık ve kaynak yapısını doğrudan etkileyen işlemleri izler',
            'C': 'Kendi içinde borç–alacak dengesi kurulur',
            'D': 'İşletmenin bilanço büyüklüğünü değiştirmez',
            'E': "Hesap Planı'nda 9 numaralı sınıfta yer alır",
        },
        'B',
        'Nazım hesaplar (9. sınıf), işletmenin varlık ve kaynak yapısını etkilemeyen ancak izlenmesi gereken teminat, emanet vb. bilgileri kaydeder; kendi içinde borç–alacak dengesi kurulur ve bilanço büyüklüğünü değiştirmez.',
        "1 Sıra No'lu MSUGT - Nazım hesaplar",
    ),
    # düzey 3
    '0027': patch(
        "Genel kesin mizanla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kalanlar sütunundaki bilanço hesaplarının kalanları dönem sonu bilançosunu oluşturur.\n\nII. Gelir ve gider (6'lı) hesapların kalanları gelir tablosuna aktarılır.\n\nIII. Düzenleyici (aktifi/pasifi düzenleyici) hesaplar kesin mizanda hiçbir zaman kalan vermez.\n\nIV. Kesin mizanda borç kalanları toplamı ile alacak kalanları toplamı eşit olmalıdır.",
        {
            'A': 'II ve III',
            'B': 'I, II, III ve IV',
            'C': 'I ve II',
            'D': 'I, II ve IV',
            'E': 'Yalnız I',
        },
        'D',
        "Yanlış ifade **III**'tür. Düzenleyici hesaplar (ör. 257 Birikmiş Amortismanlar (-), 122 Alacak Senetleri Reeskontu (-), 103 Verilen Çekler ve Ödeme Emirleri (-)) kesin mizanda **kalan verir** ve bilançoda ilgili varlık/kaynağı düzenleyici (-) olarak gösterir; 'hiçbir zaman kalan vermez' yanlıştır. **I** bilanço hesaplarının kalanları bilançoyu, **II** 6'lı hesapların kalanları gelir tablosunu besler; **IV** kesin mizanda borç kalanları toplamı = alacak kalanları toplamıdır. Doğru cevap **I, II ve IV**.",
        "1 Sıra No'lu MSUGT - Genel kesin mizan",
    ),
    # düzey 2
    '0028': patch(
        'Satılan mal veya yapılan iş karşılığında, satıcının alıcıya verdiği; miktar, tutar ve tarafların bilgilerini gösteren ticari belge aşağıdakilerden hangisidir?',
        {
            'A': 'Fatura',
            'B': 'Müstahsil makbuzu',
            'C': 'Gider pusulası',
            'D': 'Sevk irsaliyesi',
            'E': 'Serbest meslek makbuzu',
        },
        'A',
        '**Fatura**, satılan mal/hizmet karşılığında satıcının alıcıya verdiği; tutar ve tarafların bilgilerini içeren temel ticari belgedir (VUK md. 229).',
        'VUK md. 229-232 (fatura)',
    ),
    # düzey 2
    '0029': patch(
        'Defter tutmayan çiftçilerden satın alınan zirai ürünler için düzenlenen belge aşağıdakilerden hangisidir?',
        {
            'A': 'Sevk irsaliyesi',
            'B': 'Gider pusulası',
            'C': 'Müstahsil makbuzu',
            'D': 'Serbest meslek makbuzu',
            'E': 'Fatura',
        },
        'C',
        '**Müstahsil makbuzu**, defter tutmayan çiftçilerden (müstahsil) satın alınan zirai ürünler için alıcı tarafından düzenlenir (VUK md. 235).',
        'VUK md. 235 (müstahsil makbuzu)',
    ),
    # düzey 2
    '0030': patch(
        "7/A seçeneğini uygulayan işletme 1 Kasım'da bankadan altı ay vadeli 300.000 ₺ kredi kullanmıştır. Banka, kredinin 18.000 ₺ faizini peşin, 1.200 ₺ dosya masrafını da keserek kalan tutarı işletmenin hesabına aktarmıştır. İşletme peşin ödenen faizi dönemsellik gereği önce gelecek aylara ait gider olarak izlemektedir.\n\nKredi kullanım kaydında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '300 Banka Kredileri hesabı 280.800 ₺ alacaklandırılır',
            'B': '180 Gelecek Aylara Ait Giderler hesabı 18.000 ₺ borçlandırılır',
            'C': '102 Bankalar hesabı kredi tutarı olan 300.000 ₺ borçlandırılır',
            'D': '780 Finansman Giderleri hesabı 19.200 ₺ borçlandırılır',
            'E': '400 Banka Kredileri hesabı 300.000 ₺ alacaklandırılır',
        },
        'B',
        "Kayıt: 102 Bankalar 280.800 ₺, 180 Gelecek Aylara Ait Giderler 18.000 ₺ ve 780 Finansman Giderleri 1.200 ₺ borç / 300 Banka Kredileri 300.000 ₺ alacak. Kredi anapara tutarıyla ve vadesi bir yılı aşmadığından 300'de izlenir; peşin faiz döneme düşen kısmı kadar sonradan gidere aktarılır.",
        "1 Sıra No'lu MSUGT - 300 Banka Kredileri",
    ),
    # düzey 2
    '0031': patch(
        "İşletme, bir müşterisinden olan 90.000 ₺ senetsiz ticari alacağın 40.000 ₺'si için müşterinin çekini, 30.000 ₺'si için iki ay vadeli bir bono almış; kalan tutar müşteri tarafından işletmenin banka hesabına havale edilmiştir.\n\nBu işlemin yevmiye kaydıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': '101 Alınan Çekler hesabı 40.000 ₺ borçlandırılır',
            'B': '121 Alacak Senetleri hesabı 30.000 ₺ borçlandırılır',
            'C': '102 Bankalar hesabı 20.000 ₺ borçlandırılır',
            'D': '120 Alıcılar hesabı 90.000 ₺ alacaklandırılır',
            'E': '103 Verilen Çekler hesabı 40.000 ₺ borçlandırılır',
        },
        'E',
        "Kayıt: 101 Alınan Çekler 40.000 ₺, 121 Alacak Senetleri 30.000 ₺ ve 102 Bankalar 20.000 ₺ borç / 120 Alıcılar 90.000 ₺ alacak. Müşteriden alınan çek 101'de izlenir; 103 işletmenin kendi düzenleyip verdiği çekler içindir.",
        "1 Sıra No'lu MSUGT - 120 Alıcılar / 100 Kasa",
    ),
    # düzey 2
    '0032': patch(
        "Bir işletmenin ay sonu geçici mizanında borç toplamı 2.480.000 ₺, alacak toplamı 2.450.000 ₺'dir. İnceleme sonunda şu hatalar bulunmuştur:\n\n(1) Bir müşteriden yapılan 30.000 ₺'lik nakit tahsilat 100 Kasa hesabına borç yazılmış, 120 Alıcılar hesabına alacak kaydı unutulmuştur.\n\n(2) 12.000 ₺'lik veresiye bir hizmet alımı hiç kaydedilmemiştir.\n\n(3) 8.000 ₺'lik bir yönetim gideri 770 yerine 760 hesabına kaydedilmiştir.\n\nHatalar düzeltildikten sonra mizanın borç ve alacak toplamları kaçar ₺ olur?",
        {
            'A': '2.480.000',
            'B': '2.492.000',
            'C': '2.504.000',
            'D': '2.510.000',
            'E': '2.522.000',
        },
        'B',
        '(1) Tek taraflı kayıt eksikliği alacak toplamını 30.000 ₺ eksik bırakmıştır. (2) Hiç kaydedilmeyen işlem iki tarafı da 12.000 ₺ eksik bırakır; mizan eşitliğini bozmaz ama toplamları etkiler. (3) Yanlış hesaba kayıt toplamları değiştirmez. Düzeltilmiş borç = 2.480.000 + 12.000 = 2.492.000 ₺; alacak = 2.450.000 + 30.000 + 12.000 = 2.492.000 ₺.',
        "1 Sıra No'lu MSUGT - Muhasebe Süreci ve Mizan",
    ),
    # düzey 2
    '0033': patch(
        "Bir anonim şirketin genel kurulu, 590 Dönem Net Kârı hesabındaki 500.000 ₺'nin %5'inin birinci tertip yasal yedek olarak ayrılmasına, 100.000 ₺'nin ortaklara nakit kâr payı olarak dağıtılmasına ve kalanın olağanüstü yedeklere aktarılmasına karar vermiştir. Kâr payı henüz ödenmemiştir; stopaj ihmal edilecektir.\n\nKâr dağıtım kaydında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '540 Yasal Yedekler hesabı 25.000 ₺ alacaklandırılır',
            'B': '331 Ortaklara Borçlar hesabı 125.000 ₺ alacaklandırılır',
            'C': '590 Dönem Net Kârı hesabı 500.000 ₺ alacaklandırılır',
            'D': '542 Olağanüstü Yedekler hesabı 400.000 ₺ alacaklandırılır',
            'E': '500 Sermaye hesabı 100.000 ₺ alacaklandırılır',
        },
        'A',
        'Kayıt: 590 Dönem Net Kârı 500.000 ₺ borç / 540 Yasal Yedekler 25.000 ₺, 331 Ortaklara Borçlar 100.000 ₺ ve 542 Olağanüstü Yedekler 375.000 ₺ alacak. Dağıtılan kâr, ödeninceye kadar ortaklara borç olarak izlenir; 590 dağıtımla kapatılacağı için borçlandırılır.',
        "1 Sıra No'lu MSUGT - 331 Ortaklara Borçlar",
    ),
    # düzey 2
    '0034': patch(
        'Bir satış faturası sisteme bir kez girildiğinde satış geliri, ticari alacak ve stok kayıtları yetkiler çerçevesinde otomatik olarak güncellenmektedir. Aynı verinin farklı birimlerde yeniden girilmesi gerekmemektedir.\n\nBu yapı muhasebe bilgi sistemi açısından öncelikle hangi yararı sağlar?',
        {
            'A': 'Satış işlemlerinin finansal tablolara aktarılmasını engeller.',
            'B': 'Muhasebe kayıtlarının dönem sonunda topluca yapılmasını gerektirir.',
            'C': 'Belge ve kullanıcı kontrollerine ihtiyaç bırakmadan bütün kayıtları doğru kabul eder.',
            'D': 'Tekrarlı veri girişini azaltır; kayıtlar arasındaki bütünlük ve tutarlılığı destekler.',
            'E': 'Her birimin aynı işlemi bağımsız ve farklı tutarlarla kaydetmesini sağlar.',
        },
        'D',
        'Bir işlemin kaynağında bir kez kaydedilip ilgili alt sistemlere aktarılması, tekrarlı veri girişini ve aktarım hatalarını azaltır. Entegrasyon böylece **veri bütünlüğünü ve kayıtlar arası tutarlılığı** destekler; yetkilendirme ve diğer kontroller yine gereklidir.',
        'Muhasebe Bilgi Sistemleri - bütünleşik işlem işleme ve veri bütünlüğü',
    ),
    # düzey 2
    '0035': patch(
        'İşletme, yönetim katında kullanılmak üzere 40.000 ₺ + %20 KDV bedelle büro mobilyası satın almıştır. KDV dâhil bedelin yarısı için işletmenin kendi banka hesabına bağlı bir çek düzenlenip verilmiş, kalan yarısı için de iki ay vadeli bir bono düzenlenmiştir. İşletme verdiği çekleri 103 hesabında izlemektedir.\n\nBu işlemin yevmiye kaydında aşağıdakilerden hangisi yer almaz?',
        {
            'A': '255 Demirbaşlar hesabına 40.000 ₺ borç',
            'B': '191 İndirilecek KDV hesabına 8.000 ₺ borç',
            'C': '103 Verilen Çekler ve Ödeme Emirleri hesabına 24.000 ₺ alacak',
            'D': '770 Genel Yönetim Giderleri hesabına 40.000 ₺ borç',
            'E': '321 Borç Senetleri hesabına 24.000 ₺ alacak',
        },
        'D',
        'Büro mobilyası birden fazla dönem kullanılacağı için gider değil 255 Demirbaşlar hesabına aktifleştirilir. Kayıt: 255 Demirbaşlar 40.000 ₺ ve 191 İndirilecek KDV 8.000 ₺ borç / 103 Verilen Çekler ve Ödeme Emirleri 24.000 ₺ ve 321 Borç Senetleri 24.000 ₺ alacak. Yönetim gideri ancak amortisman yoluyla oluşur.',
        "1 Sıra No'lu MSUGT - 255 Demirbaşlar; 3065 s. KDVK",
    ),
    # düzey 2
    '0036': patch(
        'Dönem sonunda kâr/zararın belirlenmesi sürecinde aşağıdaki hesapların doğru akış sırası hangisidir?',
        {
            'A': '690 Dönem Kârı veya Zararı → 691 Dönem Kârı Vergi ve Diğer Yasal Yükümlülük Karşılıkları (-) → 692 Dönem Net Kârı veya Zararı',
            'B': '692 Dönem Net Kârı veya Zararı → 690 Dönem Kârı veya Zararı → 691 Dönem Kârı Vergi Karşılıkları (-) biçiminde tamamlanır',
            'C': '690 Dönem Kârı veya Zararı → 692 Dönem Net Kârı veya Zararı → 691 Dönem Kârı Vergi Karşılıkları (-) sırasıyla ilerler',
            'D': '691 Dönem Kârı Vergi ve Diğer Yasal Yükümlülük Karşılıkları (-) → 690 Dönem Kârı veya Zararı → 692 Dönem Net Kârı veya Zararı',
            'E': '692 Dönem Net Kârı veya Zararı → 691 Dönem Kârı Vergi ve Diğer Yasal Yükümlülük Karşılıkları (-) → 690 Dönem Kârı veya Zararı',
        },
        'A',
        'Önce gelir-giderler **690 Dönem Kârı veya Zararı**nda toplanır; hesaplanan vergi vb. yükümlülük **691 (-)** ile ayrılır; net sonuç **692 Dönem Net Kârı veya Zararı**na aktarılır.',
        "1 Sıra No'lu MSUGT - 690/691/692",
    ),
    # düzey 2
    '0037': patch(
        'Bir işletme veresiye ve kısmen peşin mal alışını yevmiye defterine şu şekilde kaydetmiştir: 153 Ticari Mallar hesabına 50.000 ₺ ve 191 İndirilecek KDV hesabına 10.000 ₺ borç; 100 Kasa hesabına 20.000 ₺ ve 320 Satıcılar hesabına 40.000 ₺ alacak.\n\nBirden fazla borçlu ve birden fazla alacaklı hesabın yer aldığı bu tür yevmiye maddesine ne ad verilir?',
        {
            'A': 'Bileşik madde',
            'B': 'Basit madde',
            'C': 'Ters kayıt',
            'D': 'Açılış kaydı',
            'E': 'Düzeltme kaydı',
        },
        'A',
        "Yalnız bir borçlu ve bir alacaklı hesaptan oluşan maddeye basit madde, birden fazla borçlu ya da alacaklı hesabın yer aldığı maddeye bileşik madde denir. Bu maddede iki borçlu (153, 191) ve iki alacaklı (100, 320) hesap vardır; toplamlar 60.000 ₺'de eşittir.",
        "1 Sıra No'lu MSUGT - Yevmiye maddesi türleri",
    ),
    # düzey 3
    '0038': patch(
        'Aşağıdakilerden hangisi fatura yerine geçen (perakende satış) belgelerinden biri değildir?',
        {
            'A': 'Ödeme kaydedici cihaz (yazar kasa) fişi',
            'B': 'Perakende satış vesikası',
            'C': 'Sevk irsaliyesi',
            'D': 'Perakende satış fişi',
            'E': 'Giriş ve yolcu taşıma bileti',
        },
        'C',
        'Perakende satışlarda fatura yerine; **perakende satış fişi**, **yazar kasa fişi**, **giriş/yolcu taşıma bileti** düzenlenebilir (VUK md. 233). **Sevk irsaliyesi** ise bir satış belgesi değil, malın sevkini belgeleyen belgedir.',
        'VUK md. 233 (perakende satış vesikaları)',
    ),
    # düzey 2
    '0039': patch(
        "Aralıklı envanter yöntemini uygulayan işletme, daha önce 50.000 ₺ + %20 KDV ile veresiye sattığı malın 10.000 ₺'lik kısmını kusurlu olduğu için geri almıştır. Kalan alacak için müşteriye KDV hariç tutar üzerinden %2 erken ödeme iskontosu yapılmış (iskonto KDV'yi de düzeltmektedir) ve kalan bedel banka havalesiyle tahsil edilmiştir.\n\nBu işlemlerin kayıtlarında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '610 Satıştan İadeler hesabı 12.000 ₺ borçlandırılır',
            'B': '611 Satış İskontoları hesabı 960 ₺ borçlandırılır',
            'C': '120 Alıcılar hesabı iade nedeniyle 12.000 ₺ borçlandırılır',
            'D': '102 Bankalar hesabı tahsilatta 47.040 ₺ borçlandırılır',
            'E': '391 Hesaplanan KDV hesabı iade nedeniyle 2.000 ₺ alacaklandırılır',
        },
        'D',
        'İade: 610 Satıştan İadeler 10.000 ₺ ve 391 Hesaplanan KDV 2.000 ₺ borç / 120 Alıcılar 12.000 ₺ alacak. Kalan alacak 48.000 ₺ (40.000 + 8.000 KDV). İskonto 40.000 × %2 = 800 ₺, KDV düzeltmesi 160 ₺. Tahsilat: 102 Bankalar 47.040 ₺, 611 Satış İskontoları 800 ₺ ve 391 Hesaplanan KDV 160 ₺ borç / 120 Alıcılar 48.000 ₺ alacak.',
        "1 Sıra No'lu MSUGT - 121 Alacak Senetleri; 3065 s. KDVK",
    ),
    # düzey 2
    '0040': patch(
        "Dönem başında aktif toplamı 2.000.000 ₺ olan bir işletmede dönem içinde şu işlemler yapılmıştır (KDV ihmal edilecektir):\n\n(1) 300.000 ₺'lik bir makine alınmış, bedelin 100.000 ₺'si bankadan ödenmiş, kalanı veresiyedir.\n\n(2) Müşterilerden 80.000 ₺ alacak tahsil edilmiştir.\n\n(3) Satıcılara 50.000 ₺ borç ödenmiştir.\n\n(4) Ortaklar 200.000 ₺ nakit sermaye artırımında bulunmuştur.\n\n(5) Maliyeti 60.000 ₺ olan ticari mal 90.000 ₺'ye veresiye satılmıştır.\n\nBuna göre işletmenin dönem sonu aktif toplamı kaç ₺'dir?",
        {
            'A': '2.380.000',
            'B': '2.430.000',
            'C': '2.460.000',
            'D': '2.480.000',
            'E': '2.440.000',
        },
        'A',
        '(1) Makine +300.000, banka −100.000: net +200.000. (2) Alacak tahsili aktif içi değişimdir: 0. (3) Borç ödemesi aktifi 50.000 azaltır. (4) Sermaye artırımı aktifi 200.000 artırır. (5) Stok −60.000, alacak +90.000: net +30.000. Aktif toplamı = 2.000.000 + 200.000 − 50.000 + 200.000 + 30.000 = 2.380.000 ₺.',
        "1 Sıra No'lu MSUGT - temel muhasebe eşitliği ve hesapların işleyişi",
    ),
    # düzey 2
    '0041': patch(
        'Muhasebe döngüsünde işlemlerin tarih sırasıyla ve ilk olarak kaydedildiği defter aşağıdakilerden hangisidir?',
        {
            'A': 'Karar Defteri',
            'B': 'Mizan',
            'C': 'Yevmiye Defteri (Günlük Defter)',
            'D': 'Envanter Defteri',
            'E': 'Defter-i Kebir (Büyük Defter)',
        },
        'C',
        'İşlemler önce **Yevmiye (Günlük) Defteri**ne tarih sırasıyla kaydedilir; oradan **Defter-i Kebir**e aktarılır. Mizan bir defter değil, hesap kalanlarının kontrol tablosudur.',
        'VUK md. 183-184; TTK md. 64 vd. (ticari defterler)',
    ),
    # düzey 3
    '0042': patch(
        "Tekdüzen Hesap Planı'na göre aşağıdaki hesaplardan hangisi ait olduğu hesap sınıfıyla yanlış eşleştirilmiştir?",
        {
            'A': '320 Satıcılar → 3 Kısa Vadeli Yabancı Kaynaklar',
            'B': '600 Yurt İçi Satışlar → 6 Gelir Tablosu Hesapları',
            'C': '153 Ticari Mallar → 2 Duran Varlıklar',
            'D': '500 Sermaye → 5 Özkaynaklar',
            'E': '255 Demirbaşlar → 2 Duran Varlıklar',
        },
        'C',
        '**153 Ticari Mallar**, kodun ilk rakamı **1** olduğundan **Dönen Varlıklar** sınıfındadır (Stoklar grubu), Duran Varlıklar değil. Bu nedenle bu ifade yanlıştır. Diğer eşleştirmeler doğrudur.',
        "1 Sıra No'lu MSUGT - Hesap sınıfları",
    ),
    # düzey 2
    '0043': patch(
        "İşletme ay başında ortağı A'ya 50.000 ₺ nakit borç para vermiştir. Ay ortasında A bu borcun 20.000 ₺'sini nakden geri ödemiştir. Ay sonunda işletmenin nakit ihtiyacı nedeniyle ortağı B, sermaye taahhüdü dışında işletmeye 30.000 ₺ borç vermiş ve tutar banka hesabına yatırılmıştır. Ay başında bu hesapların kalanı yoktur.\n\nAy sonunda ilgili hesapların kalanlarıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '131 Ortaklardan Alacaklar 50.000 ₺; 331 Ortaklara Borçlar 30.000 ₺',
            'B': '131 Ortaklardan Alacaklar 30.000 ₺ alacak; 331 Ortaklara Borçlar 30.000 ₺ borç',
            'C': '131 Ortaklardan Alacaklar 30.000 ₺; 500 Sermaye 30.000 ₺ artmıştır',
            'D': '131 Ortaklardan Alacaklar 20.000 ₺; 331 Ortaklara Borçlar 30.000 ₺',
            'E': '131 Ortaklardan Alacaklar 30.000 ₺ borç; 331 Ortaklara Borçlar 30.000 ₺ alacak',
        },
        'E',
        "A'ya verilen borç 131 Ortaklardan Alacaklar hesabına 50.000 ₺ borç yazılır; geri ödenen 20.000 ₺ alacağa yazılır, kalan 30.000 ₺ borç kalanıdır. B'nin sermaye dışında verdiği borç 331 Ortaklara Borçlar hesabına 30.000 ₺ alacak yazılır. Alacak ve borç farklı ortaklara ait olduğundan netleştirilmez; sermaye taahhüdü olmadığından 500 değişmez.",
        "1 Sıra No'lu MSUGT - 131 Ortaklardan Alacaklar",
    ),
    # düzey 2
    '0044': patch(
        "Dönem başında aktif toplamı 1.500.000 ₺ olan bir işletmede aşağıdaki işlemlerden yalnız biri gerçekleşmiş ve bunun sonucunda aktif toplamı da pasif toplamı da 1.560.000 ₺'ye yükselmiştir. KDV ihmal edilecektir.\n\nGerçekleşen işlem aşağıdakilerden hangisidir?",
        {
            'A': "60.000 ₺'lik senetsiz alacağın nakden tahsil edilmesi",
            'B': "60.000 ₺'lik ticari malın veresiye satın alınması",
            'C': 'Bankadaki mevduattan kasaya 60.000 ₺ çekilmesi',
            'D': "60.000 ₺'lik satıcı borcunun bankadan ödenmesi",
            'E': "60.000 ₺'lik bir makinenin peşin satın alınması",
        },
        'B',
        'Veresiye mal alışı varlıkları (153) ve yabancı kaynakları (320) aynı tutarda artırır; iki toplam 1.560.000 ₺ olur. Alacak tahsili, bankadan kasaya para çekme ve peşin makine alımı aktif içinde değişimdir, toplamı değiştirmez; borç ödemesi iki toplamı da azaltır.',
        "1 Sıra No'lu MSUGT - Bilanço eşitliği; işlem etkileri",
    ),
    # düzey 2
    '0045': patch(
        "Bir işletmenin dönem sonu kalanlarından bazıları şöyledir: 300 Banka Kredileri 150.000 ₺, 320 Satıcılar 210.000 ₺, 321 Borç Senetleri 90.000 ₺, 322 Borç Senetleri Reeskontu 6.000 ₺, 340 Alınan Sipariş Avansları 40.000 ₺, 381 Gider Tahakkukları 12.000 ₺, 159 Verilen Sipariş Avansları 30.000 ₺, 400 Banka Kredileri 500.000 ₺. Uzun vadeli kredilerden izleyen yıl ödenecek taksit bulunmamaktadır.\n\nBuna göre kısa vadeli yabancı kaynaklar toplamı kaç ₺'dir?",
        {
            'A': '456.000',
            'B': '484.000',
            'C': '496.000',
            'D': '406.000',
            'E': '490.000',
        },
        'C',
        'Kısa vadeli yabancı kaynaklar: 300 + 320 + 321 + 340 + 381 = 502.000 ₺; 322 Borç Senetleri Reeskontu borç senetlerini düzenleyen, borç kalanı veren hesaptır ve düşülür: 502.000 − 6.000 = 496.000 ₺. 159 Verilen Sipariş Avansları dönen varlıktır; 400 Banka Kredileri uzun vadeli yabancı kaynaktır.',
        "1 Sıra No'lu MSUGT - Hesap sınıfları",
    ),
    # düzey 3
    '0046': patch(
        "Bir kurumun dönem sonu aktarmalarından sonra 690 Dönem Kârı veya Zararı hesabı 400.000 ₺ alacak kalanı vermektedir. Dönem kârının hesaplanmasında 20.000 ₺ kanunen kabul edilmeyen gider dikkate alınmış, ayrıca 40.000 ₺ vergiden istisna iştirak kazancı elde edilmiştir. Kurum yıl içinde 70.000 ₺ geçici vergi ödemiştir. Soruda kullanılacak kurumlar vergisi oranı %25'tir.\n\nBuna göre 692 Dönem Net Kârı veya Zararı hesabına aktarılacak dönem net kârı kaç ₺'dir?",
        {
            'A': '300.000',
            'B': '375.000',
            'C': '235.000',
            'D': '285.000',
            'E': '305.000',
        },
        'E',
        "Mali kâr = 400.000 + 20.000 − 40.000 = 380.000 ₺; vergi karşılığı = 380.000 × %25 = 95.000 ₺ (691 borç / 370 alacak). Dönem net kârı = 400.000 − 95.000 = 305.000 ₺. Geçici vergi 371 hesabıyla 370'ten mahsup edilir; dönem net kârını etkilemez.",
        "1 Sıra No'lu MSUGT - Gelir hesaplarının kapatılması (690)",
    ),
    # düzey 2
    '0047': patch(
        'Muhasebenin temel fonksiyonları ile ilgili aşağıdaki sıralamalardan hangisi doğrudur?',
        {
            'A': 'Özetleme → Kaydetme → Sınıflandırma → Raporlama',
            'B': 'Raporlama → Kaydetme → Sınıflandırma → Özetleme',
            'C': 'Sınıflandırma → Kaydetme → Raporlama → Özetleme',
            'D': 'Kaydetme → Sınıflandırma → Özetleme → Raporlama ve yorumlama',
            'E': 'Yorumlama → Özetleme → Kaydetme → Sınıflandırma',
        },
        'D',
        'Muhasebe süreci; işlemlerin **kaydedilmesi**, benzer işlemlerin **sınıflandırılması**, dönem sonunda **özetlenmesi** ve mali tabloların **raporlanıp yorumlanması** biçiminde işler.',
        'Muhasebenin fonksiyonları',
    ),
    # düzey 2
    '0048': patch(
        'Vergiden muaf esnaftan veya belge düzenleme zorunluluğu bulunmayan kişilerden yapılan alımlar/ödemeler için, alıcı tarafından düzenlenen belge aşağıdakilerden hangisidir?',
        {
            'A': 'Gider pusulası',
            'B': 'Sevk irsaliyesi',
            'C': 'Fatura',
            'D': 'Müstahsil makbuzu',
            'E': 'Serbest meslek makbuzu',
        },
        'A',
        '**Gider pusulası**, belge veremeyen (vergiden muaf esnaf vb.) kişilerden yapılan alım/giderlerde, alan tarafından düzenlenen belgedir (VUK md. 234).',
        'VUK md. 234 (gider pusulası)',
    ),
    # düzey 2
    '0049': patch(
        'Dönem başı ve dönem sonu envanter bilgileri ile bilançonun kaydedildiği, tasdike tabi defter aşağıdakilerden hangisidir?',
        {
            'A': 'Karar defteri',
            'B': 'Envanter defteri',
            'C': 'Defter-i kebir',
            'D': 'Damga vergisi defteri',
            'E': 'Yevmiye defteri',
        },
        'B',
        '**Envanter defteri**, dönem başı ve dönem sonu envanter (varlık-borç sayım/değerleme) bilgileri ile bilançonun kaydedildiği defterdir (VUK md. 185).',
        'VUK md. 185 (envanter defteri)',
    ),
    # düzey 3
    '0050': patch(
        "Bir satıcıya banka hesabından yapılan 40.000 ₺'lik havale, muhasebe servisince yanlışlıkla 120 Alıcılar hesabına borç, 100 Kasa hesabına alacak olarak kaydedilmiştir. Hata, ters kayıt yapılmadan tek bir düzeltme maddesiyle giderilecektir.\n\nDüzeltme kaydında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '320 Satıcılar hesabı 40.000 ₺ borçlandırılır',
            'B': '120 Alıcılar hesabı 40.000 ₺ borçlandırılır',
            'C': '100 Kasa hesabı 40.000 ₺ alacaklandırılır',
            'D': '102 Bankalar hesabı 40.000 ₺ borçlandırılır',
            'E': '320 Satıcılar hesabı 40.000 ₺ alacaklandırılır',
        },
        'A',
        'Doğru kayıt 320 Satıcılar borç / 102 Bankalar alacak olmalıydı. Düzeltme maddesi: 320 Satıcılar 40.000 ₺ ve 100 Kasa 40.000 ₺ borç / 120 Alıcılar 40.000 ₺ ve 102 Bankalar 40.000 ₺ alacak. Yanlış çalışan hesaplar ters yönde, çalışması gereken hesaplar doğru yönde kaydedilir.',
        "1 Sıra No'lu MSUGT - 320 Satıcılar / 100 Kasa",
    ),
    # düzey 2
    '0051': patch(
        'İşletmenin 400 BANKA KREDİLERİ hesabında izlenen uzun vadeli kredisinin 90.000 ₺ tutarındaki anapara taksiti, bilanço tarihinden itibaren gelecek on iki ay içinde ödenecektir. Dönem sonundaki vade aktarımı için aşağıdaki kayıtlardan hangisi uygundur?',
        {
            'A': '400 Banka Kredileri (borç) 90.000 / 102 Bankalar (alacak) 90.000',
            'B': '780 Finansman Giderleri (borç) 90.000 / 400 Banka Kredileri (alacak) 90.000',
            'C': '300 Banka Kredileri (borç) 90.000 / 400 Banka Kredileri (alacak) 90.000',
            'D': '400 Banka Kredileri (borç) 90.000 / 303 Uzun Vadeli Kredilerin Anapara Taksitleri ve Faizleri (alacak) 90.000',
            'E': '303 Uzun Vadeli Kredilerin Anapara Taksitleri ve Faizleri (borç) 90.000 / 400 Banka Kredileri (alacak) 90.000',
        },
        'D',
        'Gelecek on iki ayda ödenecek uzun vadeli kredi taksiti artık kısa vadeli yabancı kaynak niteliğindedir. Bu nedenle **400 Banka Kredileri borçlandırılarak azaltılır**, **303 Uzun Vadeli Kredilerin Anapara Taksitleri ve Faizleri alacaklandırılarak artırılır**. Henüz ödeme yapılmadığı için 102 Bankalar kullanılmaz.',
        "1 Sıra No'lu MSUGT - Tekdüzen Hesap Planı (303 ve 400 hesapları)",
    ),
    # düzey 2
    '0052': patch(
        'Dönem sonunda gelir ve gider hesaplarının devredilerek dönem faaliyet sonucunun (kâr/zarar) belirlendiği hesap aşağıdakilerden hangisidir?',
        {
            'A': '570 Geçmiş Yıllar Kârları',
            'B': '690 Dönem Kârı veya Zararı',
            'C': '590 Dönem Net Kârı',
            'D': '500 Sermaye',
            'E': '331 Ortaklara Borçlar',
        },
        'B',
        "Dönem sonunda gelir hesapları (6'lı) ve gider/maliyet hesapları **690 Dönem Kârı veya Zararı**na devredilir; bu hesabın kalanı dönem faaliyet sonucunu (kâr ya da zarar) gösterir.",
        "1 Sıra No'lu MSUGT - 690 Dönem Kârı veya Zararı",
    ),
    # düzey 2
    '0053': patch(
        "Tek düzen hesap planında 'hesap çerçevesi', 'hesap grubu' ve 'hesap' kavramlarıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Hesap kodunun ilk rakamı hesabın muavinini, son rakamı ise hesap sınıfını göstermektedir.',
            'B': 'Tekdüzen hesap planı gelir tablosu hesaplarını kapsar; bilanço hesaplarını içermez.',
            'C': 'Hesap çerçevesi, hesapların en ayrıntılı düzeyi olan muavin (yardımcı) hesapları ifade eder.',
            'D': 'Her hesap grubu tek bir ana hesaptan oluşur; alt hesaplara ayrılamaz.',
            'E': 'Hesap sınıfları (1-9) en genel düzeydir; hesap grupları ve hesaplar giderek ayrıntılanır.',
        },
        'E',
        "TDHP'de en genel düzey **hesap sınıflarıdır (1-9)**; bunlar **hesap gruplarına**, gruplar da **ana hesaplara** ve **alt (muavin) hesaplara** ayrılarak giderek ayrıntılanır.",
        "1 Sıra No'lu MSUGT - Hesap çerçevesi ve kodlama",
    ),
    # düzey 2
    '0054': patch(
        "7/A seçeneğini uygulayan ve bilanço esasına göre defter tutan işletme, 1 Temmuz'da yönetim biriminde kullanılmak üzere 120.000 ₺'ye büro mobilyası almıştır. Mobilyanın faydalı ömrü 5 yıl olup normal (doğrusal) amortisman yöntemi uygulanmaktadır ve birikmiş amortisman hesabı kullanılmaktadır.\n\nDönem sonu amortisman kaydında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '257 Birikmiş Amortismanlar hesabı 12.000 ₺ alacaklandırılır',
            'B': '255 Demirbaşlar hesabı 24.000 ₺ alacaklandırılır',
            'C': '770 Genel Yönetim Giderleri hesabı 24.000 ₺ borçlandırılır',
            'D': '730 Genel Üretim Giderleri hesabı 24.000 ₺ borçlandırılır',
            'E': '257 Birikmiş Amortismanlar hesabı 24.000 ₺ borçlandırılır',
        },
        'C',
        "Amortisman oranı 1/5 = %20; yıllık amortisman 120.000 × %20 = 24.000 ₺. VUK'a göre kıst amortisman yalnız binek otomobillerinde uygulandığından yıl ortasında alınan mobilya için tam yıllık amortisman ayrılır. Kayıt: 770 Genel Yönetim Giderleri 24.000 ₺ borç / 257 Birikmiş Amortismanlar 24.000 ₺ alacak; dolaylı yöntemde 255 hesabı değişmez.",
        "1 Sıra No'lu MSUGT - 255, 257 ve 770 hesaplarının işleyişi",
    ),
    # düzey 3
    '0055': patch(
        'Aşağıdaki hesaplardan hangileri bilanço hesabıdır?\n\nI. 100 Kasa\n\nII. 600 Yurt İçi Satışlar\n\nIII. 320 Satıcılar\n\nIV. 255 Demirbaşlar',
        {
            'A': 'I ve II',
            'B': 'II ve IV',
            'C': 'I, II, III ve IV',
            'D': 'I, III ve IV',
            'E': 'Yalnız I',
        },
        'D',
        "**I (Kasa), III (Satıcılar), IV (Demirbaşlar)** bilanço hesaplarıdır (varlık/kaynak). **II (Yurt İçi Satışlar)** bir gelir tablosu (6'lı) hesabıdır; dönem sonunda 690'a devredilir, bilançoya girmez.",
        "1 Sıra No'lu MSUGT - Bilanço/gelir tablosu hesapları",
    ),
    # düzey 2
    '0056': patch(
        "Tekdüzen Hesap Planı'nda bir varlığın 'dönen' mi yoksa 'duran' varlık mı olduğunun belirlenmesiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Bir yıl içinde paraya çevrilmesi beklenen varlıklar dönendir',
            'B': 'Temel ölçüt, varlığın edinme maliyetinin büyüklüğüdür',
            'C': 'Faaliyet dönemi bir yılı aşan işletmelerde bu dönem esas alınabilir',
            'D': 'Bir yıldan uzun süre kullanılacak makineler duran varlıktır',
            'E': 'Vadesi bir yılı aşan alacaklar duran varlıklarda izlenir',
        },
        'B',
        'Dönen–duran ayrımının ölçütü, varlığın bir yıl (veya bir yılı aşan normal faaliyet dönemi) içinde paraya çevrilmesinin ya da tüketilmesinin beklenip beklenmemesidir. Tutarın büyüklüğü bir ölçüt değildir.',
        "1 Sıra No'lu MSUGT - Dönen/Duran varlık ayrımı",
    ),
    # düzey 2
    '0057': patch(
        'Varlık ve kaynakların fiilî durumunun sayım, tartım ve değerleme yoluyla belirlenmesi işlemine ne ad verilir?',
        {
            'A': 'Mizan',
            'B': 'Muhasebe dışı envanter',
            'C': 'Konsolidasyon',
            'D': 'Muhasebe içi envanter',
            'E': 'Kapanış kaydı',
        },
        'B',
        '**Muhasebe dışı envanter**, varlık ve borçların fiilî durumunun sayım/tartım/değerleme ile tespitidir. Bu fiilî sonuçların kayıtlarla karşılaştırılıp düzeltilmesi ise **muhasebe içi envanter**tir.',
        "1 Sıra No'lu MSUGT - Envanter işlemleri; VUK md. 186",
    ),
    # düzey 2
    '0058': patch(
        'İşletme 120 Alıcılar hesabını müşteri bazında ayrı ayrı izlemektedir. Dönem sonunda bu ayrıntı hesaplarda A Ltd. 30.000 ₺ borç, B A.Ş. 45.000 ₺ borç ve fazla ödeme yaptığı için C Ltd. 5.000 ₺ alacak kalanı vermektedir.\n\nBuna göre bu hesaplarla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ana hesap 80.000 ₺ borç kalanı verir',
            'B': 'Ayrıntı hesaplar nazım hesaplardır; ana hesaba katılmaz',
            'C': "C Ltd.'nin kalanı ana hesaba eklenir: 85.000 ₺ borç",
            'D': 'Ayrıntı hesaplar büyük defter hesaplarıdır; ana hesap tutulmaz',
            'E': 'Muavin hesaplardır; ana hesap 70.000 ₺ borç kalanı verir',
        },
        'E',
        'Bir ana hesabın ayrıntılarının izlendiği hesaplar muavin (yardımcı) hesaplardır ve kalanlarının toplamı ana hesabın kalanına eşittir: 30.000 + 45.000 − 5.000 = 70.000 ₺ borç. Alacak kalanı veren müşteri, ana hesabın kalanını azaltır.',
        "1 Sıra No'lu MSUGT - Muavin hesaplar",
    ),
    # düzey 2
    '0059': patch(
        'Bir işletmede aynı kullanıcı yeni satıcı kartı açabilmekte, bu satıcı adına faturayı sisteme girebilmekte ve ödemeyi de tek başına onaylayabilmektedir.\n\nBu durumdaki temel iç kontrol zayıflığı aşağıdakilerden hangisidir?',
        {
            'A': 'Görevlerin ayrılığı ilkesine uyulmaması',
            'B': 'Hesap planında muavin hesap açılması',
            'C': 'Çift taraflı kayıt yönteminin kullanılması',
            'D': 'Dönemsellik kavramının uygulanması',
            'E': 'Numaralandırılmış belge kullanılmaması',
        },
        'A',
        'Satıcı tanımlama, borç kaydı oluşturma ve ödeme onayı görevlerinin aynı kişide birleşmesi, sahte satıcı ve yetkisiz ödeme riskini artırır. Yetki ve sorumlulukların farklı kişilere dağıtılması **görevlerin ayrılığı** kontrolüdür.',
        'Muhasebe Bilgi Sistemleri - erişim kontrolleri ve görevlerin ayrılığı',
    ),
    # düzey 3
    '0060': patch(
        'Muhasebe bilgilerinin kullanıcıları ile ilgili aşağıdaki eşleştirmelerden hangisi yanlıştır?',
        {
            'A': 'Dış kullanıcı → Devlet (vergi idaresi)',
            'B': 'Dış kullanıcı → Yatırımcılar',
            'C': 'İç kullanıcı → İşletme yönetimi',
            'D': 'İç kullanıcı → İşletmeyle ilişkisi olmayan üçüncü kişiler',
            'E': 'Dış kullanıcı → Kredi veren kuruluşlar (bankalar)',
        },
        'D',
        "İşletme yönetimi **iç kullanıcı**dır; yatırımcı, kredi kuruluşu, devlet, çalışanlar vb. **dış kullanıcı**dır. İşletmeyle ilişkisi olmayan üçüncü kişileri 'iç kullanıcı' saymak yanlıştır; bu nedenle bu ifade yanlıştır.",
        'Muhasebe bilgi kullanıcıları (iç/dış)',
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
    print(f"1 paket / {len(PATCHES)} soru ('Muhasebe Sureci ve Hesap Plani' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
