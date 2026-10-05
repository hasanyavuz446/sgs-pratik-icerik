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
        'Aşağıdaki hesaplardan hangisinin bakiyesi artırılırken hesabın alacak tarafına kayıt yapılır?',
        {
            'A': '255 Demirbaşlar',
            'B': '153 Ticari Mallar',
            'C': '320 Satıcılar',
            'D': '100 Kasa',
            'E': '120 Alıcılar',
        },
        'C',
        '**320 Satıcılar** bir kaynak (pasif) hesabıdır; pasif hesaplarda artışlar **alacak** tarafına yazılır. Diğer şıklar aktif (varlık) hesaptır ve artışları borç tarafına kaydedilir.',
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
        'Aşağıdaki hesaplardan hangisi bir aktifi düzenleyici (kontr aktif) hesaptır ve normalde alacak kalanı verir?',
        {
            'A': '100 Kasa; borç kalanı verir',
            'B': '257 Birikmiş Amortismanlar (-)',
            'C': '600 Yurt İçi Satışlar; gider hesabı',
            'D': '320 Satıcılar; borç kalanlı varlık',
            'E': '153 Ticari Mallar; aktif hesaptır',
        },
        'B',
        '**257 Birikmiş Amortismanlar (-)** aktifi düzenleyici bir hesaptır; bilançoda duran varlığın altında eksi (-) gösterilir ve **alacak kalanı** verir; ilgili varlığın net defter değerini düşürür.',
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
        "İşletme, satıcısına olan 30.000 ₺'lik senetsiz ticari borcuna karşılık bir borç senedi (bono) düzenleyip vermiştir. Bu işlemin kaydı aşağıdakilerden hangisidir?",
        {
            'A': '321 Borç Senetleri (borç) 30.000 / 320 Satıcılar (alacak) 30.000',
            'B': '320 Satıcılar (borç) 30.000 / 321 Borç Senetleri (alacak) 30.000',
            'C': '120 Alıcılar (borç) 30.000 / 121 Alacak Senetleri (alacak) 30.000',
            'D': '320 Satıcılar (borç) 30.000 / 100 Kasa (alacak) 30.000',
            'E': '321 Borç Senetleri (borç) 30.000 / 100 Kasa (alacak) 30.000',
        },
        'B',
        'Senetsiz borç (320 Satıcılar) senetli borca (321 Borç Senetleri) dönüşür. Borç aynı kalır, yalnızca niteliği değişir: **320 Satıcılar (borç) 30.000 / 321 Borç Senetleri (alacak) 30.000**. Nakit çıkışı yoktur (mahsup işlemi).',
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
        'Temel muhasebe (bilanço) eşitliği aşağıdakilerden hangisidir?',
        {
            'A': 'Borçlar = Varlıklar + Özkaynaklar',
            'B': 'Varlıklar = Gelirler − Giderler',
            'C': 'Varlıklar = Yabancı Kaynaklar + Özkaynaklar',
            'D': 'Özkaynaklar = Varlıklar + Borçlar',
            'E': 'Gelirler = Varlıklar + Özkaynaklar',
        },
        'C',
        "Bilanço eşitliği **Varlıklar = Kaynaklar**, yani **Aktif = Yabancı Kaynaklar + Özkaynaklar**'dır. İşletmenin sahip olduğu varlıklar, bu varlıkların finansman kaynağına eşittir.",
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
        'İşletme sahibi, işletmeye kuruluş sermayesi olarak 500.000 ₺ nakit koymuş ve tutar işletme kasasına girmiştir. Bu işlemin kaydı aşağıdakilerden hangisidir?',
        {
            'A': '100 Kasa (borç) 500.000 / 600 Yurt İçi Satışlar (alacak) 500.000',
            'B': '100 Kasa (borç) 500.000 / 300 Banka Kredileri (alacak) 500.000',
            'C': '500 Sermaye (borç) 500.000 / 100 Kasa (alacak) 500.000',
            'D': '131 Ortaklardan Alacaklar (borç) 500.000 / 100 Kasa (alacak) 500.000',
            'E': '100 Kasa (borç) 500.000 / 500 Sermaye (alacak) 500.000',
        },
        'E',
        'Kasa (varlık) artar → **100 Kasa (borç)**; işletmenin sahibine karşı sermaye kaynağı doğar → **500 Sermaye (alacak)**. Kayıt: 100 Kasa (borç) 500.000 / 500 Sermaye (alacak) 500.000.',
        "1 Sıra No'lu MSUGT - 500 Sermaye",
    ),
    # düzey 3
    '0011': patch(
        "Aşağıdaki hesaplardan hangisi bir gelir tablosu (6'lı sınıf) hesabı değildir?",
        {
            'A': '621 Satılan Ticari Malların Maliyeti',
            'B': '600 Yurt İçi Satışlar',
            'C': '642 Faiz Gelirleri',
            'D': '320 Satıcılar',
            'E': '660 Kısa Vadeli Borçlanma Giderleri',
        },
        'D',
        "**320 Satıcılar**, kodun ilk rakamı **3** olan bir bilanço (Kısa Vadeli Yabancı Kaynaklar) hesabıdır; gelir tablosu hesabı değildir. Diğerleri 6'lı sınıf (gelir tablosu) hesaplarıdır.",
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
        "İşletme, %20 KDV ile 60.000 ₺'lik (KDV hariç) ticari malı veresiye satın almıştır. Bu işlemin kaydı aşağıdakilerden hangisidir?",
        {
            'A': '153 Ticari Mallar (borç) 60.000 + 391 Hesaplanan KDV (borç) 12.000 / 320 Satıcılar (alacak) 72.000',
            'B': '153 Ticari Mallar (borç) 60.000 + 191 İndirilecek KDV (borç) 12.000 / 320 Satıcılar (alacak) 72.000',
            'C': '153 Ticari Mallar (borç) 48.000 + 191 İndirilecek KDV (borç) 12.000 / 320 Satıcılar (alacak) 60.000',
            'D': '320 Satıcılar (borç) 72.000 / 153 Ticari Mallar (alacak) 60.000 + 191 İndirilecek KDV (alacak) 12.000',
            'E': '153 Ticari Mallar (borç) 72.000 / 320 Satıcılar (alacak) 72.000',
        },
        'B',
        'KDV = 60.000 × %20 = 12.000 ₺ (alışta **191 İndirilecek KDV**, borç). Kayıt: 153 Ticari Mallar (borç) 60.000 + 191 İndirilecek KDV (borç) 12.000 / 320 Satıcılar (alacak) 72.000.',
        '3065 s. KDVK; 191 İndirilecek KDV; 2026 KDV %20',
    ),
    # düzey 2
    '0015': patch(
        'İşletme, elindeki 25.000 ₺ nominal değerli bir alacak senedini vadesinde nakden tahsil etmiştir. Bu işlemin kaydı aşağıdakilerden hangisidir?',
        {
            'A': '121 Alacak Senetleri (borç) 25.000 / 100 Kasa (alacak) 25.000',
            'B': '100 Kasa (borç) 25.000 / 600 Yurt İçi Satışlar (alacak) 25.000',
            'C': '321 Borç Senetleri (borç) 25.000 / 100 Kasa (alacak) 25.000',
            'D': '100 Kasa (borç) 25.000 / 121 Alacak Senetleri (alacak) 25.000',
            'E': '100 Kasa (borç) 25.000 / 120 Alıcılar (alacak) 25.000',
        },
        'D',
        'Kasa (varlık) artar → **100 Kasa (borç)**; eldeki alacak senedi (varlık) tahsille çıkar → **121 Alacak Senetleri (alacak)**. Kayıt: 100 Kasa (borç) 25.000 / 121 Alacak Senetleri (alacak) 25.000.',
        "1 Sıra No'lu MSUGT - 121 Alacak Senetleri",
    ),
    # düzey 2
    '0016': patch(
        'Aşağıdakilerden hangisi bir özkaynak düzenleyici (kontr özkaynak) hesaptır ve normalde borç kalanı vererek özkaynaklardan (-) düşülür?',
        {
            'A': '600 Yurt İçi Satışlar',
            'B': '320 Satıcılar',
            'C': '103 Verilen Çekler ve Ödeme Emirleri (-)',
            'D': '257 Birikmiş Amortismanlar (-)',
            'E': '501 Ödenmemiş Sermaye (-)',
        },
        'E',
        "**501 Ödenmemiş Sermaye (-)**, taahhüt edilip henüz ödenmemiş sermayeyi gösterir; **borç kalanı** verir ve özkaynaklar içinde 500 Sermaye'den **(-)** düşülür. 257 ve 103 ise aktifi düzenleyici hesaplardır.",
        "1 Sıra No'lu MSUGT - 501 Ödenmemiş Sermaye",
    ),
    # düzey 2
    '0017': patch(
        'Bir hesap dönemi başında, önceki dönemden devreden bilanço kalemlerinin yevmiye defterine kaydedilmesi işlemine ne ad verilir?',
        {
            'A': 'Açılış kaydı',
            'B': 'Mahsup kaydı',
            'C': 'Virman kaydı',
            'D': 'Kapanış kaydı',
            'E': 'Düzeltme kaydı',
        },
        'A',
        'Dönem başında, önceki dönem sonu bilançosundaki varlık ve kaynakların yevmiyeye aktarılmasına **açılış kaydı** denir. Aktif kalemler borç, pasif kalemler alacak tarafında yer alır.',
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
        'Bir işletmede aşağıdaki yevmiye kaydı yapılmıştır:\n\n| Hesap | Borç | Alacak |\n|---|---|---|\n| 100 Kasa | 50.000 | |\n| 131 Ortaklardan Alacaklar | | 50.000 |\n\nBu kayıt aşağıdaki işlemlerden hangisine aittir?',
        {
            'A': 'Ortağa işletme kasasından nakit borç para verilmesi işlemidir',
            'B': 'Ortağın işletmeye nakit sermaye koyması (sermaye artışı)',
            'C': 'İşletmenin bankadan nakit kredi kullanması işlemidir',
            'D': 'İşletmenin ortağına nakit olarak kâr payı dağıtması işlemi',
            'E': 'Ortağın işletmeye olan borcunu nakden ödemesi (tahsilat)',
        },
        'E',
        'Kasaya nakit girişi (100 borç) ve ortaklardan alacağın azalması (131 alacak), **ortağın işletmeye olan borcunu nakden ödemesi** (işletmenin tahsilatı) anlamına gelir.',
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
        'Bir işletmede aşağıdaki yevmiye kaydı yapılmıştır:\n\n| Hesap | Borç | Alacak |\n|---|---|---|\n| 100 Kasa | 24.000 | |\n| 600 Yurt İçi Satışlar | | 20.000 |\n| 391 Hesaplanan KDV | | 4.000 |\n\nBu kayıt aşağıdaki işlemlerden hangisine aittir? (KDV %20)',
        {
            'A': 'Veresiye mal satışı',
            'B': 'Peşin mal alışı',
            'C': 'Peşin (nakit) mal satışı',
            'D': 'Alacak senedinin tahsili',
            'E': 'Banka kredisi kullanımı',
        },
        'C',
        "Kasanın borçlanması nakit girişini, 600 ve 391'in alacaklanması ise satış hasılatı + hesaplanan KDV'yi gösterir. 20.000 × %20 = 4.000 KDV ile toplam 24.000 ₺ **nakit (peşin) satış** yapılmıştır.",
        "1 Sıra No'lu MSUGT; 3065 s. KDVK (peşin satış kaydı)",
    ),
    # düzey 2
    '0022': patch(
        "Bir hesabın dönem içi borç toplamı 45.000 ₺, alacak toplamı 32.000 ₺'dir. Bu hesabın kalanı ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '13.000 ₺ borç kalanı',
            'B': '13.000 ₺ alacak kalanı',
            'C': '32.000 ₺ borç kalanı',
            'D': 'Kalan vermez (kapalı hesap)',
            'E': '77.000 ₺ borç kalanı',
        },
        'A',
        'Kalan = Borç toplamı − Alacak toplamı = 45.000 − 32.000 = **13.000 ₺**. Borç tarafı büyük olduğundan hesap **13.000 ₺ borç kalanı** verir.',
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
        'İşletme, bankadan 150.000 ₺ nakit kredi kullanmış ve tutar banka hesabına geçmiştir. Bu işlemin kaydı aşağıdakilerden hangisidir?',
        {
            'A': '300 Banka Kredileri (borç) 150.000 / 600 Yurt İçi Satışlar (alacak) 150.000',
            'B': '102 Bankalar (borç) 150.000 / 300 Banka Kredileri (alacak) 150.000',
            'C': '102 Bankalar (borç) 150.000 / 500 Sermaye (alacak) 150.000',
            'D': '300 Banka Kredileri (borç) 150.000 / 102 Bankalar (alacak) 150.000',
            'E': '100 Kasa (borç) 150.000 / 300 Banka Kredileri (alacak) 150.000',
        },
        'B',
        'Banka mevduatı (varlık) artar → **102 Bankalar (borç)**; kredi borcu (kaynak) doğar → **300 Banka Kredileri (alacak)**. Kayıt: 102 (borç) 150.000 / 300 (alacak) 150.000.',
        "1 Sıra No'lu MSUGT - 300 Banka Kredileri",
    ),
    # düzey 2
    '0031': patch(
        'İşletme, müşterisinden olan senetsiz ticari alacağını nakden tahsil etmiştir. Bu işlemin kaydı aşağıdakilerden hangisidir?',
        {
            'A': '121 Alacak Senetleri (borç) / 120 Alıcılar (alacak)',
            'B': '120 Alıcılar (borç) / 100 Kasa (alacak)',
            'C': '100 Kasa (borç) / 320 Satıcılar (alacak)',
            'D': '100 Kasa (borç) / 600 Yurt İçi Satışlar (alacak)',
            'E': '100 Kasa (borç) / 120 Alıcılar (alacak)',
        },
        'E',
        'Kasa (varlık) artar → **100 Kasa (borç)**; alıcılardan olan alacak (varlık) azalır → **120 Alıcılar (alacak)**. Kayıt: 100 Kasa (borç) / 120 Alıcılar (alacak). Satış hasılatı bu aşamada tekrar kaydedilmez.',
        "1 Sıra No'lu MSUGT - 120 Alıcılar / 100 Kasa",
    ),
    # düzey 2
    '0032': patch(
        'Bir alış işlemi yevmiye defterine hiç kaydedilmemiştir. İşlemin hem borç hem alacak tarafı birlikte eksik kaldığından dönem sonunda düzenlenen mizanın borç ve alacak toplamları yine eşit çıkmıştır.\n\nBu durum mizan kontrolü bakımından neyi gösterir?',
        {
            'A': 'Mizan eşitse bütün işlemlerin eksiksiz kaydedildiği kesinleşir.',
            'B': 'İki tarafı birlikte etkileyen eksiklikler eşitliği bozmayabilir; mizan tek başına tam doğruluk kanıtı değildir.',
            'C': 'Borç ve alacak toplamlarının eşit olması muhasebe sisteminde hata bulunduğunu gösterir.',
            'D': 'Mizan kasa hesabındaki hataları ortaya çıkarır, diğer hataları göstermez.',
            'E': 'Eşitlik, her hesabın doğru hesap koduyla kullanıldığını kanıtlar.',
        },
        'B',
        'Bir işlem tamamen atlanırsa borç ve alacak tarafları aynı tutarda eksik kalır; bu nedenle mizan eşitliği bozulmayabilir. Mizan, aritmetik eşitliği sınar ancak **işlem atlama, yanlış hesap kullanma veya iki tarafı eşit etkileyen hataları tek başına ortaya çıkaramaz**.',
        "1 Sıra No'lu MSUGT - Muhasebe Süreci ve Mizan",
    ),
    # düzey 2
    '0033': patch(
        'İşletmenin sahip veya ortaklarına dağıtmayı kararlaştırdığı kâr payı için doğan borç aşağıdaki hesaplardan hangisinde izlenir?',
        {
            'A': '331 Ortaklara Borçlar',
            'B': '500 Sermaye',
            'C': '770 Genel Yönetim Giderleri',
            'D': '131 Ortaklardan Alacaklar',
            'E': '120 Alıcılar',
        },
        'A',
        'İşletmenin ortaklarına olan borçları (dağıtılacak kâr payı, ortakların işletmeye verdiği borçlar vb.) **331 Ortaklara Borçlar** hesabında izlenir. 131 ise tersine, ortaklardan olan alacaklardır.',
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
        'İşletme yönetim biriminde kullanmak üzere 20.000 ₺ + %20 KDV bedelle peşin (nakit) demirbaş satın almıştır. Bu işlemin kaydı aşağıdakilerden hangisidir?',
        {
            'A': '255 Demirbaşlar (borç) 20.000 + 391 Hesaplanan KDV (borç) 4.000 / 100 Kasa (alacak) 24.000',
            'B': '770 Genel Yönetim Giderleri (borç) 24.000 / 100 Kasa (alacak) 24.000',
            'C': '153 Ticari Mallar (borç) 20.000 + 191 İndirilecek KDV (borç) 4.000 / 100 Kasa (alacak) 24.000',
            'D': '255 Demirbaşlar (borç) 20.000 + 191 İndirilecek KDV (borç) 4.000 / 100 Kasa (alacak) 24.000',
            'E': '255 Demirbaşlar (borç) 24.000 / 100 Kasa (alacak) 24.000',
        },
        'D',
        'Demirbaş bir duran varlıktır → **255 Demirbaşlar (borç) 20.000**; alışta KDV **191 İndirilecek KDV (borç) 4.000** (20.000×%20); nakit çıkışı **100 Kasa (alacak) 24.000**. Ticari mal (153) değildir; satış amacıyla değil kullanım amacıyla alınmıştır.',
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
        'Bir borç ve birden fazla alacak (ya da birden fazla borç ve bir alacak) hesabından oluşan yevmiye maddesine ne ad verilir?',
        {
            'A': 'Bileşik madde',
            'B': 'Açılış maddesi',
            'C': 'Basit madde',
            'D': 'Karma madde',
            'E': 'Nazım madde',
        },
        'A',
        'Bir tarafta tek, diğer tarafta birden fazla hesap bulunan yevmiye maddesi **bileşik madde**dir. Bir borç–bir alacaktan oluşan madde ise **basit madde**dir.',
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
        'İşletme, 30.000 ₺ + %20 KDV tutarındaki ticari malı, karşılığında müşteriden alacak senedi alarak (senetli) satmıştır. Bu satışın kaydında borçlandırılacak hesap aşağıdakilerden hangisidir?',
        {
            'A': '600 Yurt İçi Satışlar',
            'B': '321 Borç Senetleri',
            'C': '100 Kasa',
            'D': '121 Alacak Senetleri',
            'E': '120 Alıcılar',
        },
        'D',
        'Senet karşılığı satışta işletmenin senetli alacağı doğar → **121 Alacak Senetleri (borç) 36.000**. Karşılığında 600 Yurt İçi Satışlar (alacak) 30.000 ve 391 Hesaplanan KDV (alacak) 6.000 alacaklanır.',
        "1 Sıra No'lu MSUGT - 121 Alacak Senetleri; 3065 s. KDVK",
    ),
    # düzey 2
    '0040': patch(
        "İşletme 120.000 ₺ tutarındaki bir makineyi satın almış; bedelin 40.000 ₺'sini bankadan ödemiş, kalan 80.000 ₺ için satıcıya borçlanmıştır. KDV ihmal edilecektir.\n\nBu işlemin temel muhasebe eşitliğine etkisi hangisidir?",
        {
            'A': 'Varlıklar net 80.000 ₺, yabancı kaynaklar 80.000 ₺ artar; özkaynaklar değişmez.',
            'B': 'Varlıklar 40.000 ₺ azalır, borçlar 80.000 ₺ artar; özkaynaklar 120.000 ₺ azalır.',
            'C': 'Varlıkların bileşimi değişir; toplam varlık ve borçlar değişmez.',
            'D': 'Varlıklar ve borçlar 120.000 ₺ artar; banka hesabındaki azalış dikkate alınmaz.',
            'E': 'Varlıklar 120.000 ₺, özkaynaklar 120.000 ₺ artar; borçlar değişmez.',
        },
        'A',
        'Makine 120.000 ₺ artarken banka 40.000 ₺ azalır; varlıklardaki **net artış 80.000 ₺**dir. Satıcıya 80.000 ₺ borç doğduğundan yabancı kaynaklar da 80.000 ₺ artar. İşlem gelir veya gider yaratmadığı için özkaynak değişmez.',
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
        "İşletme, ortağı Ayşe Yıldız'a işletmeden 50.000 ₺ nakit borç para vermiştir. Bu işlemin yevmiye kaydı aşağıdakilerden hangisidir?",
        {
            'A': '770 Genel Yönetim Giderleri (borç) 50.000 / 100 Kasa (alacak) 50.000',
            'B': '500 Sermaye (borç) 50.000 / 100 Kasa (alacak) 50.000',
            'C': '100 Kasa (borç) 50.000 / 131 Ortaklardan Alacaklar (alacak) 50.000',
            'D': '331 Ortaklara Borçlar (borç) 50.000 / 100 Kasa (alacak) 50.000',
            'E': '131 Ortaklardan Alacaklar (borç) 50.000 / 100 Kasa (alacak) 50.000',
        },
        'E',
        'İşletmenin ortağından alacağı doğar → **131 Ortaklardan Alacaklar** borçlanır; nakit çıktığı için **100 Kasa** alacaklanır. Ortağa borç para verme, gider ya da sermaye azalışı değildir.',
        "1 Sıra No'lu MSUGT - 131 Ortaklardan Alacaklar",
    ),
    # düzey 2
    '0044': patch(
        'İşletme bankadaki mevduatından 20.000 ₺ çekerek kasasına koymuştur. Bu işlemin bilanço büyüklüğüne (aktif toplamına) etkisi nedir?',
        {
            'A': 'Pasif toplamı 20.000 ₺ artar, çünkü yeni bir kaynak doğmuştur',
            'B': 'Aktif toplamı değişmez, varlık bileşimi değişir',
            'C': 'Aktif toplamı 20.000 ₺ artar, çünkü kasaya nakit girmiştir',
            'D': 'Özkaynaklar 20.000 ₺ artar, çünkü işletmeye değer eklenmiştir',
            'E': 'Aktif toplamı 20.000 ₺ azalır, çünkü bankadan para çıkmıştır',
        },
        'B',
        "Kayıt **100 Kasa (borç) 20.000 / 102 Bankalar (alacak) 20.000**'dir. Bir varlık artarken eşit tutarda başka bir varlık azaldığından **aktif toplamı değişmez**; yalnızca varlıkların bileşimi değişir.",
        "1 Sıra No'lu MSUGT - Bilanço eşitliği; işlem etkileri",
    ),
    # düzey 2
    '0045': patch(
        "Aşağıdaki hesaplardan hangisi Tekdüzen Hesap Planı'nda '3 - Kısa Vadeli Yabancı Kaynaklar' sınıfında yer alır?",
        {
            'A': '153 Ticari Mallar',
            'B': '500 Sermaye',
            'C': '300 Banka Kredileri',
            'D': '120 Alıcılar',
            'E': '255 Demirbaşlar',
        },
        'C',
        '**300 Banka Kredileri**, kodun ilk rakamı **3** olduğundan Kısa Vadeli Yabancı Kaynaklar sınıfındadır (bir yıl içinde ödenecek kredi borcu). 120 ve 153 aktif, 500 özkaynak, 255 duran varlıktır.',
        "1 Sıra No'lu MSUGT - Hesap sınıfları",
    ),
    # düzey 3
    '0046': patch(
        'Aşağıdaki yevmiye kaydı bir işletmenin dönem sonu işlemlerine aittir:\n\n| Hesap | Borç | Alacak |\n|---|---|---|\n| 600 Yurt İçi Satışlar | 500.000 | |\n| 690 DÖNEM KÂRI VEYA ZARARI | | 500.000 |\n\nBu kayıt aşağıdaki işlemlerden hangisine aittir?',
        {
            'A': 'Peşin mal satışının kasa hesabı borçlandırılarak kaydedilmesi işlemidir',
            'B': 'Satılan malın maliyetinin 621 hesabına aktarılması işlemidir',
            'C': 'Satıştan iadenin 610 hesabı kullanılarak kaydedilmesi işlemidir',
            'D': 'Ortaklara dağıtılacak kâr payının 331 hesabında izlenmesidir',
            'E': 'Gelir hesabının dönem sonunda 690 hesabına devredilerek kapatılması',
        },
        'E',
        "Bir gelir hesabı olan **600 Yurt İçi Satışlar** (alacak kalanı verir) dönem sonunda **borçlandırılarak** 690'a **devredilir** ve kapatılır. Bu, gelir hesaplarının dönem sonunda sonuç hesabına aktarılması işlemidir.",
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
        'Bir işletmede aşağıdaki yevmiye kaydı yapılmıştır:\n\n| Hesap | Borç | Alacak |\n|---|---|---|\n| 320 Satıcılar | 40.000 | |\n| 100 Kasa | | 40.000 |\n\nBu kayıt aşağıdaki işlemlerden hangisine aittir?',
        {
            'A': 'Satıcıya olan borcun nakit ödenmesi',
            'B': 'Satıcıdan veresiye mal alınması',
            'C': 'Müşteriden tahsilat yapılması',
            'D': 'Banka kredisi kullanılması',
            'E': 'Peşin mal satışı',
        },
        'A',
        'Satıcılara olan borcun azalması (320 borç) ve kasadan nakit çıkışı (100 alacak), **satıcıya olan borcun nakit olarak ödenmesi**ni gösterir.',
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
        'İşletme, yönetim biriminde kullanılan bir demirbaş için dönem sonunda 8.000 ₺ amortisman ayırmıştır. Birikmiş amortisman hesabının kullanıldığı yönteme ve gider yerine göre bu işlemin kaydı aşağıdakilerden hangisidir?',
        {
            'A': '255 Demirbaşlar (borç) 8.000 / 770 Genel Yönetim Giderleri (alacak) 8.000',
            'B': '770 Genel Yönetim Giderleri (borç) 8.000 / 255 Demirbaşlar (alacak) 8.000',
            'C': '770 Genel Yönetim Giderleri (borç) 8.000 / 257 Birikmiş Amortismanlar (alacak) 8.000',
            'D': '257 Birikmiş Amortismanlar (borç) 8.000 / 770 Genel Yönetim Giderleri (alacak) 8.000',
            'E': '689 Diğer Olağandışı Gider (borç) 8.000 / 257 Birikmiş Amortismanlar (alacak) 8.000',
        },
        'C',
        'Amortisman bir giderdir → **770 Genel Yönetim Giderleri (borç)**; varlığın değeri doğrudan azaltılmaz, düzenleyici hesap çalışır → **257 Birikmiş Amortismanlar (alacak)**. Kayıt: 770 (borç) 8.000 / 257 (alacak) 8.000.',
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
        'Bir ana hesabın ayrıntılarının (ör. her bir müşteri, her bir satıcı) ayrı ayrı izlendiği hesaplara ne ad verilir?',
        {
            'A': 'Sonuç (kâr/zarar) hesapları',
            'B': 'Geçici (asma) hesaplar',
            'C': 'Düzenleyici (kontr) hesaplar',
            'D': 'Nazım (izleme) hesapları',
            'E': 'Muavin (yardımcı) hesaplar',
        },
        'E',
        'Bir ana hesabın ayrıntısını gösteren (ör. 120 Alıcılar altında her müşteri) hesaplar **muavin (yardımcı) hesaplar**dır; ana hesap bakiyesi, muavin hesapların toplamına eşittir.',
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
