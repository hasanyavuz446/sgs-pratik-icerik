#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Menkul Kiymetler — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.  FM cok adimli tur. 50 soru korundu; 8 TFRS 9 sorusu ve 2 ezber sorusu cikarildi. Yerine gercek sinav kalibinda 10 soru: komisyonlu hisse satisi, stopajli hazine bonosu ve finansman bonosu vade tahsili, stopajli tahvil kuponu, satis zarari (655), deger dusuklugu karsiligi hesabi, bedelsiz hisse sonrasi birim maliyet, olumsuz ve oncullu sorular. Yontemi tartismali kayitlardan (karsilik ayrilmis menkulun satisi, komisyonun kara netlenmesi, gecici yatirim temettusu) kacinildi. Kor ogrenci %22. Duzeltme: cozumlerdeki '**X yanlistir**' harf atiflari kaldirildi (yeniden harflendirmede yanlis sikki gosteriyordu).

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: VUK m. 279 · KDVK m. 17/4-g · Tekduzen Hesap Plani 11, 119, 193, 642, 645, 654, 655 · 1 Sira No'lu MSUGT
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/finansal_muhasebe/menkul_kiymetler.json"
STYLE_REF = 'SGS Finansal Muhasebe (çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "finmuh-menkul-gen-"


def patch(stem, options, answer, solution, ref='VUK m. 279; Tekduzen Hesap Plani 11'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Tekdüzen Hesap Planı'nda '11 Menkul Kıymetler' grubu ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Faiz geliri veya kısa vadede fiyat artışından kâr sağlamak amacıyla geçici olarak elde tutulan menkul değerleri izler.',
            'B': 'İşletmenin esas faaliyet konusu olan, satmak amacıyla elde tuttuğu ticari mal ve mamul stoklarını izleyen bir gruptur.',
            'C': 'İşletmenin uzun vadeli ortaklık ve yönetime katılma amacıyla edindiği pay senetlerini ve bağlı menkul kıymetleri izleyen bir gruptur.',
            'D': 'İşletmenin üretimde veya faaliyette bir yıldan uzun süre kullanmak amacıyla edindiği maddi duran varlıkları izleyen bir gruptur.',
            'E': 'İşletmenin mal ve hizmet alımından doğan, satıcılara olan kısa ve uzun vadeli ticari borçlarının tamamını izleyen bir gruptur.',
        },
        'A',
        "**11 Menkul Kıymetler** grubu; faiz/temettü geliri ya da kısa vadede değer artışından kâr elde etmek amacıyla **geçici olarak** elde tutulan hisse senedi, tahvil, bono vb. değerleri izler (dönen varlık). Uzun vadeli ortaklık amaçlı paylar 24 İştirakler/Bağlı Ortaklıklar'dadır.",
        "1 Sıra No'lu MSUGT - Menkul Kıymetler (11)",
    ),
    # düzey 3
    '0002': patch(
        "Nakit fazlasını değerlendirmek isteyen bir ticaret işletmesi 1 kilogram külçe altın satın almış ve VUK kayıtlarında 2.000.000 ₺ değerle izlemektedir. Altın dönem sonunda işletmenin kasasında bulunmaktadır; değerleme günündeki kıymetli madenler borsası rayici 2.300.000 ₺'dir.\n\nVUK 274/A'ya göre dönem sonu değeri ve değerleme farkı sırasıyla kaç ₺'dir?",
        {
            'A': '300.000 ₺ ve 2.000.000 ₺ gelir',
            'B': '2.000.000 ₺ ve 0 ₺',
            'C': '2.300.000 ₺ ve 2.300.000 ₺ gelir',
            'D': '2.300.000 ₺ ve 300.000 ₺ gelir',
            'E': '2.000.000 ₺ ve 300.000 ₺ zarar',
        },
        'D',
        'VUK 274/A uyarınca altın borsa rayiciyle değerlenir. Dönem sonu değer **2.300.000 ₺**, kayıtlı değere göre olumlu fark 2.300.000 − 2.000.000 = **300.000 ₺ gelir**dir.',
        '213 sayılı VUK md. 274/A (7524 sayılı Kanun, yürürlük 02.08.2024)',
    ),
    # düzey 2
    '0003': patch(
        'İşletmenin elinde bulundurduğu tahvillerden dönem içinde 8.000 ₺ faiz (kupon) geliri tahsil edilmiştir (stopaj ihmal). Bu gelir hangi hesaba alacak yazılır?',
        {
            'A': '645 Menkul Kıymet Satış Kârları',
            'B': '642 Faiz Gelirleri',
            'C': '600 Yurt İçi Satışlar',
            'D': '640 İştiraklerden Temettü Gelirleri',
            'E': '649 Diğer Olağan Gelir ve Kârlar',
        },
        'B',
        'Tahvil/bono gibi borçlanma araçlarından elde edilen faiz (kupon) geliri **642 Faiz Gelirleri**ne alacak yazılır: 100/102 (borç) / 642 Faiz Gelirleri (alacak).',
        "1 Sıra No'lu MSUGT - 642 Faiz Gelirleri",
    ),
    # düzey 2
    '0004': patch(
        "Bir holding şirketi dönem içinde iki ayrı hisse senedi alımı yapmıştır: bir şirketin sermayesinin %25'ini uzun vadede ortak olup yönetimine katılmak (önemli etki) amacıyla edinmiş, borsada işlem gören başka bir şirketin hisselerini ise birkaç ay içinde fiyat artışından yararlanıp satmak amacıyla almıştır.\n\nBu hisse senetleri sırasıyla hangi hesaplarda izlenir?",
        {
            'A': '242 İştirakler – 110 Hisse Senetleri',
            'B': '120 Alıcılar – 110 Hisse Senetleri',
            'C': '110 Hisse Senetleri – 242 İştirakler',
            'D': '110 Hisse Senetleri – 110 Hisse Senetleri',
            'E': '242 İştirakler – 245 Bağlı Ortaklıklar',
        },
        'A',
        'Uzun vadeli ortaklık/etkinlik amaçlı paylar **242 İştirakler** (Duran Varlıklar); kısa vadeli kâr amaçlı hisse senetleri ise **110 Hisse Senetleri** (Menkul Kıymetler) hesabında izlenir. Amaç ve süre ayrımı esastır.',
        "1 Sıra No'lu MSUGT - 110 / 242",
    ),
    # düzey 2
    '0005': patch(
        "İşletmenin kısa vadeli kâr amacıyla elde tuttuğu iki farklı hisse senedi bulunmaktadır. X A.Ş. hisselerinin maliyeti 80.000 ₺, dönem sonu borsa değeri 70.000 ₺; Y A.Ş. hisselerinin maliyeti 50.000 ₺, dönem sonu borsa değeri 62.000 ₺'dir. Önceki dönemde X A.Ş. hisseleri için 4.000 ₺ değer düşüklüğü karşılığı ayrılmıştır. İşletme karşılığı her menkul kıymet için ayrı ayrı belirlemektedir.\n\nBuna göre dönem sonunda ayrılacak ek karşılık ve menkul kıymetlerin bilançodaki net tutarı aşağıdakilerden hangisidir?",
        {
            'A': '10.000 ₺ ek karşılık; net tutar 120.000 ₺',
            'B': 'Karşılık gerekmez; net tutar 130.000 ₺',
            'C': '6.000 ₺ ek karşılık; net tutar 120.000 ₺',
            'D': '6.000 ₺ ek karşılık; net tutar 132.000 ₺',
            'E': '2.000 ₺ karşılık iptali; net tutar 132.000 ₺',
        },
        'C',
        "Karşılık kalem bazında belirlendiğinden Y A.Ş. hisselerindeki değer artışı X A.Ş.'deki düşüşle dengelenmez ve kayda alınmaz. X için gereken karşılık 80.000 − 70.000 = 10.000 ₺; mevcut 4.000 ₺ olduğundan 6.000 ₺ ek karşılık ayrılır (654 borç / 119 alacak). Net tutar = (80.000 + 50.000) − 10.000 = 120.000 ₺.",
        "1 Sıra No'lu MSUGT - 11/119 net gösterim",
    ),
    # düzey 2
    '0006': patch(
        "İşletme yıl içinde borsada işlem gören hisse senetlerini kısa vadeli kâr amacıyla 50.000 ₺'ye satın almıştır. Dönem sonunda hisselerin borsa değeri 62.000 ₺, üzerlerinde yazılı nominal değer 20.000 ₺'dir ve hisseler henüz satılmamıştır.\n\nVergi Usul Kanunu'na göre bu hisse senetleri dönem sonunda hangi değerle değerlenir?",
        {
            'A': 'Tasfiye değeri',
            'B': 'Alış bedeli',
            'C': 'Emsal bedel',
            'D': 'İtibari (nominal) değer',
            'E': 'Borsa rayici',
        },
        'B',
        "VUK md. 279'a göre **hisse senetleri** ile (belirli koşullardaki) yatırım fonu katılma belgeleri **alış bedeli** ile değerlenir. Bunlar dışındaki menkul kıymetler (devlet tahvili, hazine bonosu vb.) borsa rayici / kıst getiri ile değerlenir.",
        'VUK md. 279 (menkul kıymet değerlemesi)',
    ),
    # düzey 2
    '0007': patch(
        "İşletme, kısa vadeli değerlendirme amacıyla özel bir şirketin çıkardığı 60.000 ₺'lik tahvili peşin (banka) satın almıştır. Bu işlemin kaydı aşağıdakilerden hangisidir?",
        {
            'A': '110 Hisse Senetleri (borç) 60.000 / 102 Bankalar (alacak) 60.000',
            'B': '102 Bankalar (borç) 60.000 / 111 Özel Kesim Tahvil, Senet ve Bonoları (alacak) 60.000',
            'C': '112 Kamu Kesimi Tahvil, Senet ve Bonoları (borç) 60.000 / 102 Bankalar (alacak) 60.000',
            'D': '111 Özel Kesim Tahvil, Senet ve Bonoları (borç) 60.000 / 102 Bankalar (alacak) 60.000',
            'E': '321 Borç Senetleri (borç) 60.000 / 102 Bankalar (alacak) 60.000',
        },
        'D',
        'Özel sektör tahvili **111 Özel Kesim Tahvil, Senet ve Bonoları** hesabına alınır: 111 (borç) 60.000 / 102 Bankalar (alacak) 60.000. (Kamu tahvili olsaydı 112 kullanılırdı.)',
        "1 Sıra No'lu MSUGT - 111",
    ),
    # düzey 2
    '0008': patch(
        "İşletmenin kısa vadeli amaçla elde tuttuğu ve maliyeti 80.000 ₺ olan hisselerinin borsa değeri dönem sonunda 68.000 ₺'ye düşmüştür. İşletme hisseleri satmadığı hâlde aradaki 12.000 ₺ için karşılık ayırıp gider yazmış; aynı dönemde değeri maliyetinin üzerine çıkan başka hisseleri için ise herhangi bir gelir kaydetmemiştir.\n\nBu uygulama hangi temel muhasebe kavramıyla açıklanır?",
        {
            'A': 'Parayla Ölçülme',
            'B': 'İhtiyatlılık',
            'C': 'Süreklilik',
            'D': 'Sosyal Sorumluluk',
            'E': 'Kişilik',
        },
        'B',
        'Değeri düşen menkul kıymet için muhtemel zararın önceden gider yazılması **İhtiyatlılık Kavramı**nın gereğidir; varlıkların ve kârın olduğundan yüksek gösterilmesini engeller.',
        "1 Sıra No'lu MSUGT - İhtiyatlılık; 119",
    ),
    # düzey 2
    '0009': patch(
        "İşletme 1 Ekim'de, kısa vadeli değerlendirme amacıyla 200.000 ₺ nominal değerli, yıllık %24 faizli ve kuponları 1 Nisan ile 1 Ekim'de ödenen bir şirket tahvilini, kupon ödemesinin yapıldığı gün satın almıştır. 31 Aralık'ta dönemsellik gereği üç aylık faiz tahakkuk ettirilmiştir. İzleyen yıl 1 Nisan'da altı aylık kupon, soruda kullanılacak %10 oranında stopaj kesilerek banka hesabına geçmiştir.\n\n1 Nisan'daki kupon tahsilatı kaydında aşağıdaki hesaplardan hangisinin kullanımı doğrudur?",
        {
            'A': '642 Faiz Gelirleri hesabı 24.000 ₺ alacaklandırılır',
            'B': '181 Gelir Tahakkukları hesabı 12.000 ₺ borçlandırılır',
            'C': '102 Bankalar hesabı 24.000 ₺ borçlandırılır',
            'D': '642 Faiz Gelirleri hesabı 12.000 ₺ alacaklandırılır',
            'E': '193 Peşin Ödenen Vergiler ve Fonlar 1.200 ₺ borçlandırılır',
        },
        'D',
        "Altı aylık kupon 200.000 × %24 × 6/12 = 24.000 ₺. Ekim–Aralık'a ait 12.000 ₺ geçen yıl 181'e tahakkuk ettirilmişti; cari yıla ait kısım 12.000 ₺'dir. Stopaj 24.000 × %10 = 2.400 ₺. Kayıt: 102 Bankalar 21.600 ₺ ve 193 Peşin Ödenen Vergiler ve Fonlar 2.400 ₺ borç / 181 Gelir Tahakkukları 12.000 ₺ ve 642 Faiz Gelirleri 12.000 ₺ alacak.",
        "1 Sıra No'lu MSUGT - 642/640",
    ),
    # düzey 3
    '0010': patch(
        'Menkul kıymetler grubu ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Uzun vadeli ortaklık amaçlı hisse senetleri de bu grupta izlenir.',
            'B': 'Bilançoda dönen varlıklar içinde gösterilir.',
            'C': '119 Menkul Kıymetler Değer Düşüklüğü Karşılığı aktifi düzenleyici bir hesaptır.',
            'D': 'Hisse senedi satış kârı 645, satış zararı 655 hesabında izlenir.',
            'E': 'Kısa vadeli kâr/gelir amacıyla elde tutulan menkul değerleri kapsar.',
        },
        'A',
        'Uzun vadeli ortaklık/etkinlik amaçlı hisse senetleri menkul kıymetler (11) değil, **24 Mali Duran Varlıklar** (İştirakler/Bağlı Ortaklıklar) grubunda izlenir. Diğer ifadeler doğrudur.',
        "1 Sıra No'lu MSUGT - 11 / 24",
    ),
    # düzey 2
    '0011': patch(
        "Bir ticaret işletmesinin bankada 100 gram gümüş cinsinden vadeli mevduatı vardır. Mevduat gümüş cinsinden faiz getirmekte olup değerleme gününe kadar 5 gram gümüş faiz tahakkuk etmiştir. Değerleme gününde gümüşün borsa rayici gram başına 30 ₺'dir.\n\nVUK 274/A'ya göre faiz dâhil mevduatın değerleme tutarı kaç ₺'dir?",
        {
            'A': '3.100 ₺',
            'B': '3.500 ₺',
            'C': '3.150 ₺',
            'D': '3.000 ₺',
            'E': '150 ₺',
        },
        'C',
        'Kıymetli maden mevduatları değerleme gününe kadar hesaplanan faizleriyle birlikte dikkate alınır. Toplam 100 + 5 = **105 gram**, değer 105 × 30 = **3.150 ₺**dir.',
        '213 sayılı VUK md. 274/A',
    ),
    # düzey 3
    '0012': patch(
        "Hisse senetlerini hareketli ağırlıklı ortalama maliyetle izleyen işletme, aynı şirketin hisselerinden önce 100 adedi 40 ₺'den, sonra 200 adedi 46 ₺'den almıştır. Ardından 150 adedi 50 ₺'den satmış, 100 adet daha 52 ₺'den almış ve son olarak 120 adedi 55 ₺'den satmıştır. Komisyon ve vergiler ihmal edilecektir.\n\nBuna göre iki satış nedeniyle '645 Menkul Kıymet Satış Kârları' hesabına yazılan toplam tutar kaç ₺'dir?",
        {
            'A': '2.100',
            'B': '900',
            'C': '1.560',
            'D': '2.236',
            'E': '1.836',
        },
        'E',
        "İlk ortalama: (4.000 + 9.200) ÷ 300 = 44 ₺; ilk satış kârı 150 × (50 − 44) = 900 ₺. Kalan 150 adede 100 adet 52 ₺'den eklenince yeni ortalama (6.600 + 5.200) ÷ 250 = 47,20 ₺; ikinci satış kârı 120 × (55 − 47,20) = 936 ₺. Toplam 1.836 ₺.",
        "1 Sıra No'lu MSUGT - 110 (ortalama maliyet)",
    ),
    # düzey 2
    '0013': patch(
        'İşletmenin elindeki tahvile dönem sonu itibarıyla 5.000 ₺ faiz tahakkuk etmiş; ancak faiz izleyen dönemde tahsil edilecektir. Dönemsellik gereği yapılacak kayıt aşağıdakilerden hangisidir?',
        {
            'A': '112 Kamu Kesimi Tahvil, Senet ve Bonoları (borç) 5.000 / 642 Faiz Gelirleri (alacak) 5.000',
            'B': '642 Faiz Gelirleri (borç) 5.000 / 181 Gelir Tahakkukları (alacak) 5.000',
            'C': '102 Bankalar (borç) 5.000 / 642 Faiz Gelirleri (alacak) 5.000',
            'D': '181 Gelir Tahakkukları (borç) 5.000 / 642 Faiz Gelirleri (alacak) 5.000',
            'E': '642 Faiz Gelirleri (borç) 5.000 / 102 Bankalar (alacak) 5.000',
        },
        'D',
        'Döneme ait olup henüz tahsil edilmemiş faiz geliri tahakkuk ettirilir: **181 Gelir Tahakkukları (borç) 5.000 / 642 Faiz Gelirleri (alacak) 5.000**. Faiz izleyen dönemde tahsil edilince 181 kapatılır.',
        "1 Sıra No'lu MSUGT - 181 Gelir Tahakkukları; Dönemsellik",
    ),
    # düzey 2
    '0014': patch(
        'Menkul kıymet satış kârı ve satış zararının gelir tablosunda gösterilmesi ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Satış kârı ve satış zararının ikisi de brüt satış kârına eklenerek gösterilir.',
            'B': 'Satış kârı ve satış zararının ikisi de gelir tablosunda değil, bilançoda yer alır.',
            'C': 'Satış kârı (645) gelir, satış zararı (655) gider olarak ayrı ayrı gösterilir.',
            'D': 'Satış kârı ile satış zararı netleştirilip tek bir tutar olarak gösterilir.',
            'E': 'Satış kârı (645) gelir yazılır; satış zararı (655) gösterilmez.',
        },
        'C',
        'Menkul kıymet satış **kârı (645)** bir gelir, satış **zararı (655)** ise bir gider olup gelir tablosunun ilgili bölümlerinde **ayrı ayrı** gösterilir; netleştirilmez.',
        "1 Sıra No'lu MSUGT - 645/655",
    ),
    # düzey 2
    '0015': patch(
        'İşletme, satışa hazır ticari mallar (stok) ile kısa vadeli kâr amaçlı hisse senetlerini karıştırmamalıdır. Bu iki kalem arasındaki temel fark aşağıdakilerden hangisidir?',
        {
            'A': 'Ticari mallar esas faaliyet konusu (alım-satım) stoklardır (15 grubu); hisse senetleri ise atıl fonların değerlendirildiği menkul kıymetlerdir (11 grubu).',
            'B': "Ticari mallar da hisse senetleri de aynı '15 Stoklar' grubunda ve aynı hesapta izlenir; aralarında hesap planı bakımından herhangi bir ayrım yapılmaz.",
            'C': 'Ticari mallar da hisse senetleri de bir yıldan uzun süre elde tutulan duran varlıklardır; ikisi de bilançonun duran varlıklar bölümünde raporlanır.',
            'D': 'Ticari mallar bir menkul kıymet (11 grubu), hisse senetleri ise satmak için elde tutulan bir stok (15 grubu) olup ikisinin grubu birbiriyle tam ters şekilde belirlenir.',
            'E': 'Ticari mallar da hisse senetleri de işletmenin ödemekle yükümlü olduğu birer kaynak (pasif) hesabıdır; ikisi de bilançonun pasifinde borçlar arasında yer alır.',
        },
        'A',
        '**Ticari mallar** işletmenin esas faaliyet konusu olan, satmak için elde tuttuğu **stoklardır (15)**. **Hisse senetleri** ise esas faaliyet dışı, atıl fonların değerlendirildiği **menkul kıymetlerdir (11)**.',
        "1 Sıra No'lu MSUGT - 11 / 15 ayrımı",
    ),
    # düzey 3
    '0016': patch(
        "Bir işletme kısa vadeli değerlendirme amacıyla 40.000 ₺'ye aldığı borsada işlem gören hisse senetleri için, dönem sonunda borsa değerinin düşmesi nedeniyle 6.000 ₺ değer düşüklüğü karşılığı ayırmıştır. İzleyen dönemde bu hisselerin tamamı 37.000 ₺'ye satılmış ve bedel bankaya yatırılmıştır.\n\nSatış anında ayrılan karşılık ne olur? (Karşılık iptali ayrıca yapılacaktır.)",
        {
            'A': "Ayrılan 6.000 ₺'lik karşılık 654 Karşılık Giderleri hesabına yeniden gider yazılır; satış kâr/zararı ise satış bedeli ile nominal değer farkından bulunur.",
            'B': 'Karşılık (119) konusu kalmadığından iptal edilir (119 / 644); satış kâr/zararı ise satış (37.000) ile kayıtlı maliyet (40.000) farkından belirlenir.',
            'C': "Ayrılan 6.000 ₺'lik karşılık satış bedeline eklenir; böylece hisseler 37.000 ₺ yerine 43.000 ₺'ye satılmış gibi kaydedilerek satış hasılatı artırılmış olur.",
            'D': "Ayrılan 6.000 ₺'lik karşılık işleme tabi tutulmadan bilançoda kalmaya devam eder; satıştan doğan zarar 655 hesabında izlenmez.",
            'E': "Ayrılan 6.000 ₺'lik karşılık 110 Hisse Senetleri hesabına eklenerek menkul kıymetin kayıtlı maliyeti 46.000 ₺'ye yükseltilir ve satış bu tutar üzerinden kaydedilir.",
        },
        'B',
        "Menkul kıymet satılınca ona ait değer düşüklüğü karşılığının (119) konusu kalmaz; **119 / 644 Konusu Kalmayan Karşılıklar** ile iptal edilir. Satış zararı ise kayıtlı maliyet (40.000) − satış (37.000) = 3.000 ₺ olarak 655'te ayrıca izlenir.",
        "1 Sıra No'lu MSUGT - 119/644; 655",
    ),
    # düzey 3
    '0017': patch(
        "İşletme kısa vadeli kâr amacıyla adedini 60 ₺'den aldığı hisse senetlerinden 1.000 adedini banka aracılığıyla adedi 75 ₺'den satmıştır. Banka satış tutarı üzerinden %2 komisyon kestikten sonra kalan tutarı işletmenin hesabına aktarmıştır. Buna göre satış kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '110 Hisse Senetleri hesabı 73.500 ₺ alacaklandırılır',
            'B': '645 Menkul Kıymet Satış Kârları hesabı 75.000 ₺ alacaklandırılır',
            'C': '110 Hisse Senetleri hesabı 60.000 ₺ alacaklandırılır',
            'D': '110 Hisse Senetleri hesabı 75.000 ₺ alacaklandırılır',
            'E': '102 Bankalar hesabı 75.000 ₺ borçlandırılır',
        },
        'C',
        "Satılan hisseler kayıtlı maliyetle çıkar: **110 (alacak) 60.000**. Banka 75.000 × %98 = 73.500 ₺ aktarır; komisyon 1.500 ₺'dir. Satış kârı satış bedeli ile maliyet arasındaki farktan doğar.",
        'THP 110, 102, 645, 653',
    ),
    # düzey 2
    '0018': patch(
        'Bir işletme kısa vadeli menkul kıymetlerinde dönem sonunda değer düşüklüğü tespit etmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Değer düşüklüğü 110 alacaklandırılarak doğrudan maliyetten düşülür',
            'B': 'Değer düşüklüğü karşılığı ihtiyatlılık kavramının gereğidir',
            'C': "Karşılık 654'ün borcuna, 119'un alacağına yazılır",
            'D': "İzleyen dönemde değer artarsa karşılık 644'e gelir yazılarak iptal edilir",
            'E': 'Menkul kıymetler bilançoda karşılık düşülerek gösterilir',
        },
        'A',
        'Değer düşüklüğü menkul kıymet hesabından doğrudan düşülmez; düzenleyici **119 Menkul Kıymetler Değer Düşüklüğü Karşılığı** hesabında izlenir (654 borç / 119 alacak). 110 maliyetle kalır.',
        "1 Sıra No'lu MSUGT; THP 119, 654, 644",
    ),
    # düzey 3
    '0019': patch(
        "Bir işletme kısa vadeli kâr amacıyla 90.000 ₺'ye aldığı ve değer düşüklüğü karşılığı ayırmadığı borsada işlem gören hisse senetlerinin tamamını, fiyatların düşmeye devam edeceği beklentisiyle 82.000 ₺'ye satmıştır; bedel aracı kurum tarafından banka hesabına aktarılmıştır.\n\nBuna göre satış kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '655 Menkul Kıymet Satış Zararları hesabı 8.000 ₺ alacaklandırılır',
            'B': '689 Diğer Olağandışı Gider ve Zararlar hesabı 8.000 ₺ borçlandırılır',
            'C': '102 Bankalar hesabı 90.000 ₺ borçlandırılır',
            'D': '655 Menkul Kıymet Satış Zararları hesabı 8.000 ₺ borçlandırılır',
            'E': '110 Hisse Senetleri hesabı 82.000 ₺ alacaklandırılır',
        },
        'D',
        "Kayıt: 102 (borç) 82.000 + **655 (borç) 8.000** / 110 (alacak) 90.000. Menkul kıymet satış zararı olağan faaliyetlerden doğan gider olarak 655'te izlenir.",
        'THP 110, 102, 655',
    ),
    # düzey 3
    '0020': patch(
        "İşletme kısa vadeli kâr amacıyla adedini 10 ₺'den 1.000 adet hisse senedi almıştır. Dönem sonunda hisselerin borsa değeri adet başına 8,5 ₺'ye düşmüştür ve işletme değer düşüklüğü karşılığı ayırmaya karar vermiştir. Buna göre karşılık tutarı ve kaydı aşağıdakilerden hangisidir?",
        {
            'A': '1.500 ₺; 655 borç / 110 alacak',
            'B': '1.500 ₺; 654 borç / 119 alacak',
            'C': '8.500 ₺; 654 borç / 119 alacak',
            'D': '10.000 ₺; 654 borç / 119 alacak',
            'E': '1.500 ₺; 119 borç / 644 alacak',
        },
        'B',
        'Karşılık = 1.000 × (10 − 8,5) = **1.500 ₺**. Kayıt: 654 Karşılık Giderleri (borç) / 119 Menkul Kıymetler Değer Düşüklüğü Karşılığı (alacak). Hisseler satılmadığı için 655 kullanılmaz.',
        "1 Sıra No'lu MSUGT; THP 110, 119, 654",
    ),
    # düzey 2
    '0021': patch(
        "İşletme dönem içinde şu menkul kıymetleri satın almıştır:\n\n(1) Borsada kısa sürede satmak amacıyla X A.Ş. hisseleri, 120.000 ₺.\n\n(2) Yönetimde söz sahibi olmak amacıyla Y A.Ş.'nin sermayesinin %30'unu temsil eden hisseler, 900.000 ₺.\n\n(3) Z A.Ş.'nin sermayesinin %60'ını temsil eden hisseler, 2.000.000 ₺.\n\n(4) Vadesine kadar elde tutulacak üç yıl vadeli bir şirket tahvili, 150.000 ₺.\n\n(5) Fon fazlasını kısa süre değerlendirmek için alınan altı ay vadeli devlet tahvili, 80.000 ₺.\n\nBuna göre bu alımlardan '11 Menkul Kıymetler' grubuna kaydedilen toplam tutar kaç ₺'dir?",
        {
            'A': '350.000',
            'B': '230.000',
            'C': '1.100.000',
            'D': '270.000',
            'E': '200.000',
        },
        'E',
        "11 grubunda kısa vadeli (geçici yatırım) amaçla edinilen menkul kıymetler izlenir: X A.Ş. hisseleri (110) 120.000 ₺ ve altı ay vadeli devlet tahvili (112) 80.000 ₺; toplam 200.000 ₺. Yönetime katılma amaçlı %30'luk pay 242 İştirakler, %60'lık pay 245 Bağlı Ortaklıklar, vadeye kadar elde tutulacak üç yıllık tahvil 240 Bağlı Menkul Kıymetler hesabında izlenir.",
        "1 Sıra No'lu MSUGT - 110 Hisse Senetleri",
    ),
    # düzey 2
    '0022': patch(
        "İşletmenin maliyeti 500.000 ₺ olan platin mevcudu için değerleme gününde güvenilir bir kıymetli madenler borsası rayici bulunmamaktadır. VUK 274/A'ya göre hangi değer esas alınır?",
        {
            'A': '500.000 ₺ maliyet bedeli',
            'B': 'Sıfır değer',
            'C': 'İşletme yönetiminin belirlediği tahmini satış değeri',
            'D': 'Nominal değer',
            'E': 'Tasfiye değeri',
        },
        'A',
        "VUK 274/A'ya göre kıymetli maden borsa rayiciyle değerlenir; borsa rayici yoksa veya muvazaalı oluşmuşsa **maliyet bedeli** esas alınır. Bu nedenle değer **500.000 ₺**dir.",
        '213 sayılı VUK md. 274/A',
    ),
    # düzey 2
    '0023': patch(
        "'119 Menkul Kıymetler Değer Düşüklüğü Karşılığı (-)' hesabıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Aktifi düzenleyici nitelikte bir hesaptır',
            'B': 'Kural olarak alacak kalanı verir',
            'C': 'Bilançoda menkul kıymetlerden (-) olarak düşülür',
            'D': 'Değer düşüklüğü ortadan kalkınca 644 ile kapatılır',
            'E': 'Menkul kıymetler grubunda borç kalanı veren bir hesaptır',
        },
        'E',
        '119 Menkul Kıymetler Değer Düşüklüğü Karşılığı aktifi düzenleyici (kontr aktif) bir hesaptır; alacak kalanı verir ve bilançoda menkul kıymetlerden (-) düşülür. Karşılık konusu kalmadığında 644 Konusu Kalmayan Karşılıklar ile kapatılır.',
        "1 Sıra No'lu MSUGT - 119",
    ),
    # düzey 2
    '0024': patch(
        "Katma Değer Vergisi Kanunu'na göre hisse senedi ve tahvil teslimleriyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Bu teslimler KDV'den istisnadır",
            'B': 'Bu teslimlerde %20 oranında KDV hesaplanır',
            'C': 'Satış belgesinde KDV hesaplanmaz',
            'D': 'İstisna, satış kazancının gelir veya kurumlar vergisini kaldırmaz',
            'E': 'Hisse senedi ve tahvil teslimleri aynı istisna hükmüne tabidir',
        },
        'B',
        "KDVK m. 17/4-g'ye göre hisse senedi ve tahvil teslimleri KDV'den istisnadır; KDV hesaplanmaz. İstisna yalnız KDV bakımındandır; satıştan doğan kazanç gelir veya kurumlar vergisine tabi olmaya devam eder.",
        '3065 s. KDVK md. 17/4-g (menkul kıymet istisnası)',
    ),
    # düzey 2
    '0025': patch(
        "Bir işletme, sermayesinin %30'una sahip olduğu ve uzun vadeli olarak elde tuttuğu X A.Ş.'nin genel kurul kararıyla dağıttığı 120.000 ₺ kâr payından payına düşen 36.000 ₺'yi banka hesabına tahsil etmiştir. İşletme X A.Ş.'nin yönetiminde temsil edilmekte, ancak kontrol gücüne sahip bulunmamaktadır.\n\nBu kâr payı geliri hangi hesaba alacak yazılır?",
        {
            'A': '600 Yurt İçi Satışlar',
            'B': '645 Menkul Kıymet Satış Kârları',
            'C': '640 İştiraklerden Temettü Gelirleri',
            'D': '642 Faiz Gelirleri',
            'E': '679 Diğer Olağandışı Gelir ve Kârlar',
        },
        'C',
        "İştiraklerden elde edilen temettü (kâr payı) **640 İştiraklerden Temettü Gelirleri** hesabına alacak yazılır. Faiz geliri 642, menkul kıymet satış kârı ise 645'tedir.",
        "1 Sıra No'lu MSUGT - 640 İştiraklerden Temettü Gelirleri",
    ),
    # düzey 2
    '0026': patch(
        "Vergi Usul Kanunu'na göre borsa rayici bulunmayan devlet tahvili ve hazine bonoları dönem sonunda hangi ölçüyle değerlenir?",
        {
            'A': 'İtibari (nominal) değer (üzerinde yazılı değer esas alınır, işlemiş faiz dikkate alınmaz)',
            'B': 'Tasfiye değeri (menkul kıymetin zorunlu satışında elde edilebilecek net tutar esas alınır)',
            'C': 'Emsal bedel (benzer menkul kıymetlerin piyasadaki ortalama değeri esas alınarak belirlenir)',
            'D': 'Kıst getiri (elde etme ile değerleme günü arasında işlemiş getiri, alış bedeline eklenir)',
            'E': 'Alış bedeli (ödenen tutarla değerlenir, işlemiş getiri eklenmez)',
        },
        'D',
        'Borsa rayici olmayan devlet tahvili/hazine bonoları, **kıst getiri** esasına göre değerlenir: alış bedeline, elde etme tarihinden değerleme gününe kadar işlemiş getiri (faiz) eklenir.',
        'VUK md. 279 (kıst getiri)',
    ),
    # düzey 2
    '0027': patch(
        "İşletmenin uzun vadeli elde tutma amacıyla edindiği ve iştirak/bağlı ortaklık niteliği taşımayan menkul kıymetler Tekdüzen Hesap Planı'nda hangi hesapta izlenir?",
        {
            'A': '110 Hisse Senetleri',
            'B': '240 Bağlı Menkul Kıymetler',
            'C': '153 Ticari Mallar',
            'D': '120 Alıcılar',
            'E': '108 Diğer Hazır Değerler',
        },
        'B',
        "Uzun vadeli elde tutulan, iştirak/bağlı ortaklık niteliği taşımayan menkul kıymetler **240 Bağlı Menkul Kıymetler** (24 Mali Duran Varlıklar) hesabında izlenir. Kısa vadeliler ise 110/111/112'dedir.",
        "1 Sıra No'lu MSUGT - 240 Bağlı Menkul Kıymetler",
    ),
    # düzey 3
    '0028': patch(
        "İşletme, 1 Temmuz'da vadesinde 100.000 ₺ ödenecek kuponsuz devlet bonosunu 90.000 ₺'ye almıştır. Vade 30 Haziran izleyen yıldır ve doğrusal kıst getiri varsayılacaktır. Borsa rayici bulunmadığına göre VUK 279 uyarınca 31 Aralık değerleme tutarı kaç ₺'dir?",
        {
            'A': '90.000 ₺',
            'B': '105.000 ₺',
            'C': '110.000 ₺',
            'D': '100.000 ₺',
            'E': '95.000 ₺',
        },
        'E',
        'Toplam 10.000 ₺ getiri on iki aylık süreye aittir. İlk altı aya düşen kıst getiri 10.000 × 6/12 = **5.000 ₺**dir. Değerleme tutarı 90.000 + 5.000 = **95.000 ₺** olur.',
        '213 sayılı VUK md. 279',
    ),
    # düzey 2
    '0029': patch(
        "İşletme, daha önce 119 Menkul Kıymetler Değer Düşüklüğü Karşılığı'nda 9.000 ₺ karşılık ayırdığı hisse senetlerinin tamamını satmıştır. Satış işlemi yapılırken ayrılan bu karşılık ne olur?",
        {
            'A': 'Ayrılan karşılık 645 Menkul Kıymet Satış Kârları hesabına borç kaydedilerek düşülür.',
            'B': 'Ayrılan karşılık tutarı 110 Hisse Senetleri hesabına eklenerek maliyeti artırılır.',
            'C': 'Menkul kıymet elden çıktığı için karşılığın da (119) kapatılması/iptal edilmesi gerekir.',
            'D': 'Ayrılan karşılık tutarı iki katına çıkarılarak, satış anında dönem gideri olarak yeniden kaydedilir.',
            'E': 'Ayrılan karşılık işleme tabi tutulmadan bilançoda aynen kalmaya devam eder.',
        },
        'C',
        'Menkul kıymet elden çıkınca ona ait değer düşüklüğü karşılığının (119) da **konusu kalmaz**; karşılık iptal edilir (ör. 119 / 644 Konusu Kalmayan Karşılıklar). Satış kâr/zararı ayrıca kayıtlı (maliyet) değere göre belirlenir.',
        "1 Sıra No'lu MSUGT - 119/644",
    ),
    # düzey 3
    '0030': patch(
        "İşletme, 30.000 ₺'lik hisse senedini kısa vadeli kâr amacıyla peşin almış; ancak muhasebeci bunu yanlışlıkla '242 İştirakler' hesabına kaydetmiştir. Bu kayıt hangi bakımdan hatalıdır?",
        {
            'A': 'Kısa vadeli kâr amacıyla alınan hisse senedinin bir varlık değil, dönem içinde katlanılan bir gider olarak sonuç hesaplarına aktarılması gerektiğinden kaydın hatalı olması',
            'B': 'Kısa vadeli kâr amacıyla alınan hisse senedinin bir varlık değil, işletmenin ödemekle yükümlü olduğu bir kaynak (pasif) hesabı olarak kaydedilmesi gerektiğinden kaydın hatalı olması',
            'C': 'Kısa vadeli kâr amacıyla alınan hisse senedinin menkul kıymet değil ticari mal sayılması ve 153 hesapta izlenmesi gerekmesi',
            'D': 'Kısa vadeli kâr amacıyla alınan hisse senedinin tesliminde katma değer vergisi hesaplanması ve bu verginin ayrıca 191 İndirilecek KDV hesabında izlenmesi gerekmesi',
            'E': 'Kısa vadeli kâr amacıyla alınan hisse senedinin dönen varlık (110 Hisse Senetleri) olarak izlenmesi gerekirken, uzun vadeli mali duran varlık (242) olarak kaydedilmesi',
        },
        'E',
        'Kısa vadeli kâr amacıyla alınan hisse senedi **110 Hisse Senetleri** (dönen varlık) olarak izlenmelidir. 242 İştirakler ise uzun vadeli ortaklık/etkinlik amaçlı paylar içindir; amaç-süre uyuşmadığından kayıt hatalıdır.',
        "1 Sıra No'lu MSUGT - 110 / 242",
    ),
    # düzey 3
    '0031': patch(
        'Menkul kıymetlerin değerlemesi ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Hisse senetleri alış bedeliyle değerlenir.\n\nII. Borsa rayici olmayan devlet tahvili kıst getiri ile değerlenir.\n\nIII. Değeri maliyetin altına düşen menkul kıymetler için değer düşüklüğü karşılığı ayrılabilir.\n\nIV. Menkul kıymetler her zaman satış fiyatıyla değerlenir.',
        {
            'A': 'II ve IV',
            'B': 'Yalnız I',
            'C': 'I, II, III ve IV',
            'D': 'I, II ve III',
            'E': 'I ve IV',
        },
        'D',
        '**I, II ve III doğrudur** (VUK 279 + ihtiyatlılık gereği karşılık). **IV yanlıştır:** menkul kıymetler satış fiyatıyla değil, türüne göre alış bedeli/borsa rayici/kıst getiri ile değerlenir.',
        "VUK md. 279; 1 Sıra No'lu MSUGT - 119",
    ),
    # düzey 2
    '0032': patch(
        'İşletmenin elinde bulundurduğu hisse senetlerini çıkaran şirket, bedelsiz (iç kaynaklardan) sermaye artırımı yapmış ve işletmeye bedelsiz hisse senedi vermiştir. Bu durumun işletmenin hisse senedi maliyeti üzerindeki etkisi ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Toplam maliyet değişmez; hisse adedi arttığı için birim maliyet düşer.',
            'B': 'Bedelsiz hisseler 645 Menkul Kıymet Satış Kârları hesabına gelir yazılır.',
            'C': 'Toplam maliyet, edinilen bedelsiz hisselerin nominal değeri kadar artırılır.',
            'D': 'Toplam maliyet sıfırlanır; hisseler nominal değeri üzerinden kaydedilir.',
            'E': 'Bedelsiz hisselerin değeri 654 Karşılık Giderleri hesabına gider yazılır.',
        },
        'A',
        'Bedelsiz hisse senedi alımında işletme yeni bir bedel ödemez; **toplam maliyet değişmez**, ancak hisse adedi arttığından **birim maliyet düşer**. Bedelsiz hisseler doğrudan gelir/gider yazılmaz.',
        "1 Sıra No'lu MSUGT - 110 (bedelsiz hisse)",
    ),
    # düzey 2
    '0033': patch(
        "İşletme kısa vadeli kâr amacıyla adedini 45 ₺'den 1.200 adet hisse senedi almıştır. Daha sonra bu hisselerin 800 adedini aracı kurum kanalıyla adedi 58 ₺'den satmış; aracı kurum satış tutarı üzerinden %0,25 komisyon keserek kalanı işletmenin banka hesabına aktarmıştır. İşletme komisyonu ayrı bir gider hesabında izlemektedir.\n\nBuna göre '645 Menkul Kıymet Satış Kârları' hesabına alacak kaydedilecek tutar kaç ₺'dir?",
        {
            'A': '15.600',
            'B': '10.400',
            'C': '46.400',
            'D': '12.400',
            'E': '10.284',
        },
        'B',
        "Satış tutarı 800 × 58 = 46.400 ₺; satılan hisselerin maliyeti 800 × 45 = 36.000 ₺; satış kârı 10.400 ₺ (645 alacak). Komisyon 46.400 × %0,25 = 116 ₺ ayrı gider olarak 653 Komisyon Giderleri'ne yazılır; kayıt: 102 Bankalar 46.284 ₺ ve 653 116 ₺ borç / 110 Hisse Senetleri 36.000 ₺ ve 645 10.400 ₺ alacak.",
        "1 Sıra No'lu MSUGT - 645",
    ),
    # düzey 2
    '0034': patch(
        "VUK 279'a göre işletmenin elindeki pay senetlerinin dönem sonu borsa değerinin alış bedelinin üzerine çıkması durumunda vergi değerlemesinde ne yapılır?",
        {
            'A': 'Gerçekleşmemiş değer artışı gelir olarak kaydedilmez; menkul kıymet maliyetle izlenmeye devam eder (ihtiyatlılık).',
            'B': 'Gerçekleşmemiş değer artışı, 645 Menkul Kıymet Satış Kârları hesabına gelir yazılarak dönem kârına doğrudan eklenir.',
            'C': 'Menkul kıymet dönem sonu borsa değerine yükseltilir ve aradaki olumlu fark doğrudan kâr olarak kaydedilir.',
            'D': 'Gerçekleşmemiş değer artışı, elde edilen bir faiz getirisi sayılıp 642 Faiz Gelirleri hesabına gelir yazılır.',
            'E': 'Değer arttığı için 654 Karşılık Giderleri karşılığında 119 Değer Düşüklüğü Karşılığı hesabı ayrıca ayrılır.',
        },
        'A',
        'VUK 279 uyarınca pay senetleri **alış bedeliyle** değerlenir. Bu nedenle dönem sonundaki gerçekleşmemiş borsa değeri artışı vergi değerlemesinde gelir yazılmaz; fark, satış gerçekleşirse satış kazancı olarak ortaya çıkar. TFRS 9 kapsamındaki gerçeğe uygun değer uygulaması ayrı bir finansal raporlama çerçevesidir.',
        '213 sayılı VUK md. 279',
    ),
    # düzey 3
    '0035': patch(
        'Menkul kıymetlerle ilgili aşağıdaki hesap–açıklama eşleştirmelerinden hangisi yanlıştır?',
        {
            'A': '112 Kamu Kesimi Tahvil, Senet ve Bonoları → Devlet tahvili, hazine bonosu',
            'B': '645 Menkul Kıymet Satış Kârları → Menkul kıymet satışından doğan kâr',
            'C': '110 Hisse Senetleri → Kısa vadeli kâr amaçlı ortaklık payları',
            'D': '119 Menkul Kıymetler Değer Düşüklüğü Karşılığı (-) → Aktifi düzenleyici',
            'E': '642 Faiz Gelirleri → Hisse senedi satış kârı',
        },
        'E',
        'Hisse senedi satış kârı **645 Menkul Kıymet Satış Kârları**nda izlenir; 642 Faiz Gelirleri ise tahvil/mevduat gibi faiz getiren kalemlerin geliri içindir. Diğer eşleştirmeler doğrudur.',
        "1 Sıra No'lu MSUGT - Menkul kıymet hesapları",
    ),
    # düzey 2
    '0036': patch(
        "Bir işletmenin dönem içinde elde ettiği menkul kıymet sonuçları şöyledir: elde tuttuğu tahvillerden 18.000 ₺ kupon faizi, kısa vadeli hisse satışından 12.000 ₺ kâr, başka bir hisse satışından 5.000 ₺ zarar, %25 payına sahip olduğu iştirakinden 20.000 ₺ ve %70 payına sahip olduğu bağlı ortaklığından 30.000 ₺ kâr payı.\n\nBuna göre bu sonuçlar nedeniyle gelir tablosunun '64 Diğer Faaliyetlerden Olağan Gelir ve Kârlar' grubuna yazılacak toplam tutar kaç ₺'dir?",
        {
            'A': '75.000',
            'B': '30.000',
            'C': '80.000',
            'D': '50.000',
            'E': '85.000',
        },
        'C',
        '64 grubu: tahvil faizi 18.000 ₺ (642), hisse satış kârı 12.000 ₺ (645), iştirak kâr payı 20.000 ₺ (640), bağlı ortaklık kâr payı 30.000 ₺ (641); toplam 80.000 ₺. Hisse satış zararı 65 grubunda (655) ayrıca gösterilir; gelirlerle netleştirilmez.',
        "1 Sıra No'lu MSUGT - 645/642/640",
    ),
    # düzey 2
    '0037': patch(
        "İşletme dönem içinde kısa vadeli menkul kıymetlerinden şu satışları yapmıştır: maliyeti 40.000 ₺ olan X A.Ş. hisselerini 46.000 ₺'ye, maliyeti 30.000 ₺ olan ve karşılık ayrılmamış Y A.Ş. hisselerini 27.000 ₺'ye, maliyeti 20.000 ₺ olan bir şirket tahvilini 19.000 ₺'ye. Satışların tamamı peşindir; vergi ve komisyon ihmal edilecektir.\n\nBuna göre bu satışlar sonucunda gelir tablosu hesaplarına kaydedilecek tutarlar aşağıdakilerden hangisidir?",
        {
            'A': '645: 2.000 ₺; 655 hesabı kullanılmaz',
            'B': '645: 6.000 ₺; 655: 3.000 ₺',
            'C': '645: 7.000 ₺; 655: 3.000 ₺',
            'D': '642: 6.000 ₺; 655: 4.000 ₺',
            'E': '645: 6.000 ₺; 655: 4.000 ₺',
        },
        'E',
        "Her satışın sonucu ayrı belirlenir ve kâr ile zarar netleştirilmez. X A.Ş.: 46.000 − 40.000 = 6.000 ₺ kâr (645). Y A.Ş.: 27.000 − 30.000 = 3.000 ₺ zarar; tahvil: 19.000 − 20.000 = 1.000 ₺ zarar; ikisi 655 Menkul Kıymet Satış Zararları'na toplam 4.000 ₺ yazılır. Satış kârı faiz geliri değildir; 642 kullanılmaz.",
        "1 Sıra No'lu MSUGT - 655",
    ),
    # düzey 3
    '0038': patch(
        "İşletme geçici yatırım amacıyla adedi 100 ₺ nominal değerli 5.000 adet hazine bonosunu adedi 90 ₺'den almıştır. Vade sonunda nominal değer banka aracılığıyla tahsil edilmiş, faiz geliri üzerinden %10 gelir vergisi kesintisi yapılmıştır. Buna göre tahsil kaydında aşağıdakilerden hangisi yer almaz?",
        {
            'A': '642 Faiz Gelirleri hesabı 50.000 ₺ alacaklandırılır',
            'B': '193 Peşin Ödenen Vergiler ve Fonlar hesabı 5.000 ₺ borçlandırılır',
            'C': '102 Bankalar hesabı 495.000 ₺ borçlandırılır',
            'D': '645 Menkul Kıymet Satış Kârları hesabı 50.000 ₺ alacaklandırılır',
            'E': '112 Kamu Kesimi Tahvil, Senet ve Bonoları hesabı 450.000 ₺ alacaklandırılır',
        },
        'D',
        'Faiz = nominal − alış = 500.000 − 450.000 = 50.000 ₺; stopaj 5.000 ₺. Kayıt: 102 (borç) 495.000 + 193 (borç) 5.000 / 112 (alacak) 450.000 + 642 (alacak) 50.000. Vadede itfa bir satış değil faiz getirisidir; 645 kullanılmaz.',
        'THP 112, 102, 193, 642',
    ),
    # düzey 3
    '0039': patch(
        'İşletmenin geçici yatırım amacıyla elinde tuttuğu tahvillerin 12.000 ₺ tutarındaki faiz kuponu tahsil edilmiştir. Faiz üzerinden %10 gelir vergisi kesintisi yapılmış, kalan tutar banka hesabına geçmiştir. Buna göre tahsil kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '193 Peşin Ödenen Vergiler ve Fonlar hesabı 1.200 ₺ borçlandırılır',
            'B': '193 Peşin Ödenen Vergiler ve Fonlar hesabı 1.200 ₺ alacaklandırılır',
            'C': '770 Genel Yönetim Giderleri hesabı 1.200 ₺ borçlandırılır',
            'D': '360 Ödenecek Vergi ve Fonlar hesabı 1.200 ₺ alacaklandırılır',
            'E': '642 Faiz Gelirleri hesabı 10.800 ₺ alacaklandırılır',
        },
        'A',
        'Kayıt: 102 (borç) 10.800 + **193 (borç) 1.200** / 642 (alacak) 12.000. Faiz geliri brüt yazılır; kesilen vergi işletmenin mahsup edeceği peşin vergidir.',
        'THP 102, 193, 642',
    ),
    # düzey 2
    '0040': patch(
        "Menkul kıymetlerle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Hisse senetleri VUK'a göre dönem sonunda borsa rayiciyle değerlenir.\n\nII. Hisse senedi ve tahvil teslimleri KDV'den istisnadır.\n\nIII. Menkul kıymet satış kârı 645 hesabında izlenir.",
        {
            'A': 'I ve III',
            'B': 'Yalnız II',
            'C': 'II ve III',
            'D': 'Yalnız III',
            'E': 'I ve II',
        },
        'C',
        'II ve III doğrudur. I yanlıştır: VUK m. 279 uyarınca hisse senetleri **alış bedeliyle** değerlenir; borsa değerindeki artış gelir yazılmaz.',
        'VUK m. 279; KDVK m. 17/4-g',
    ),
    # düzey 2
    '0041': patch(
        "İşletme, kısa vadeli kâr amacıyla 50.000 ₺'lik hisse senedini peşin (nakit) satın almıştır (komisyon ihmal edilecektir). Bu işlemin kaydı aşağıdakilerden hangisidir?",
        {
            'A': '153 Ticari Mallar (borç) 50.000 / 100 Kasa (alacak) 50.000',
            'B': '242 İştirakler (borç) 50.000 / 100 Kasa (alacak) 50.000',
            'C': '100 Kasa (borç) 50.000 / 110 Hisse Senetleri (alacak) 50.000',
            'D': '110 Hisse Senetleri (borç) 50.000 / 100 Kasa (alacak) 50.000',
            'E': '110 Hisse Senetleri (borç) 50.000 / 600 Yurt İçi Satışlar (alacak) 50.000',
        },
        'D',
        "Menkul kıymet (varlık) artar → **110 Hisse Senetleri (borç) 50.000**; nakit çıkışı → **100 Kasa (alacak) 50.000**. Kısa vadeli kâr amacı olduğundan 110'da (menkul kıymet) izlenir, iştirak (242) değil.",
        "1 Sıra No'lu MSUGT - 110 Hisse Senetleri",
    ),
    # düzey 2
    '0042': patch(
        'Nakit fazlası bulunan bir işletme, kısa vadeli değerlendirme amacıyla 100.000 ₺ nominal bedelli ve 9 ay vadeli devlet tahvilini banka aracılığıyla nominal bedelle peşin satın almıştır (komisyon ihmal). Tahvil vadesinde faiziyle birlikte itfa edilecektir.\n\nBu işlemin kaydı aşağıdakilerden hangisidir?',
        {
            'A': '112 Kamu Kesimi Tahvil, Senet ve Bonoları (borç) 100.000 / 642 Faiz Gelirleri (alacak) 100.000',
            'B': '112 Kamu Kesimi Tahvil, Senet ve Bonoları (borç) 100.000 / 102 Bankalar (alacak) 100.000',
            'C': '102 Bankalar (borç) 100.000 / 112 Kamu Kesimi Tahvil, Senet ve Bonoları (alacak) 100.000',
            'D': '242 İştirakler (borç) 100.000 / 102 Bankalar (alacak) 100.000',
            'E': '110 Hisse Senetleri (borç) 100.000 / 102 Bankalar (alacak) 100.000',
        },
        'B',
        'Devlet tahvili menkul kıymet olarak alınır: **112 Kamu Kesimi Tahvil, Senet ve Bonoları (borç) 100.000 / 102 Bankalar (alacak) 100.000**. Banka mevduatı azalır.',
        "1 Sıra No'lu MSUGT - 112",
    ),
    # düzey 2
    '0043': patch(
        'İşletmenin elindeki hisse senetlerinin borsa değeri, maliyet bedelinin 9.000 ₺ altına düşmüştür. Bu değer düşüklüğü için karşılık ayrılmasına ilişkin kayıt aşağıdakilerden hangisidir?',
        {
            'A': '655 Menkul Kıymet Satış Zararları (borç) 9.000 / 110 Hisse Senetleri (alacak) 9.000',
            'B': '119 Menkul Kıymetler Değer Düşüklüğü Karşılığı (borç) 9.000 / 654 Karşılık Giderleri (alacak) 9.000',
            'C': '654 Karşılık Giderleri (borç) 9.000 / 110 Hisse Senetleri (alacak) 9.000',
            'D': '110 Hisse Senetleri (borç) 9.000 / 645 Menkul Kıymet Satış Kârları (alacak) 9.000',
            'E': '654 Karşılık Giderleri (borç) 9.000 / 119 Menkul Kıymetler Değer Düşüklüğü Karşılığı (alacak) 9.000',
        },
        'E',
        'Değer düşüklüğü için gider tahakkuk ettirilip karşılık ayrılır: **654 Karşılık Giderleri (borç) 9.000 / 119 Menkul Kıymetler Değer Düşüklüğü Karşılığı (-) (alacak) 9.000**. Menkul kıymetin maliyet kaydı doğrudan azaltılmaz.',
        "1 Sıra No'lu MSUGT - 654/119",
    ),
    # düzey 3
    '0044': patch(
        "Bir kuyum toptancısına mal satan bir işletmenin, müşterisinden 100 gram altın cinsinden senetsiz alacağı bulunmakta ve bu alacak kayıtlarda 300.000 ₺ ile izlenmektedir. Değerleme gününde altının borsa rayici gram başına 3.200 ₺'dir.\n\nVUK 274/A'ya göre alacağın dönem sonu değeri ve olumlu değerleme farkı sırasıyla kaç ₺'dir?",
        {
            'A': '300.000 ₺ ve 0 ₺',
            'B': '20.000 ₺ ve 300.000 ₺',
            'C': '320.000 ₺ ve 320.000 ₺',
            'D': '320.000 ₺ ve 20.000 ₺',
            'E': '280.000 ₺ ve 20.000 ₺',
        },
        'D',
        'VUK 274/A, kıymetli maden cinsinden senetli ve senetsiz alacaklara da uygulanır. Değer 100 × 3.200 = **320.000 ₺**, olumlu fark 320.000 − 300.000 = **20.000 ₺**dir.',
        '213 sayılı VUK md. 274/A',
    ),
    # düzey 2
    '0045': patch(
        "Aşağıdaki hesaplardan hangisi '11 Menkul Kıymetler' grubunda yer almaz?",
        {
            'A': '112 Kamu Kesimi Tahvil, Senet ve Bonoları',
            'B': '118 Diğer Menkul Kıymetler',
            'C': '111 Özel Kesim Tahvil, Senet ve Bonoları',
            'D': '110 Hisse Senetleri',
            'E': '120 Alıcılar',
        },
        'E',
        "**120 Alıcılar**, '12 Ticari Alacaklar' grubundadır; menkul kıymet değildir. Diğerleri (110, 111, 112, 118) 11 Menkul Kıymetler grubundadır.",
        "1 Sıra No'lu MSUGT - 11 Menkul Kıymetler",
    ),
    # düzey 2
    '0046': patch(
        "Menkul kıymetlerin '11 Menkul Kıymetler' (dönen varlık) grubunda mı yoksa '24 Mali Duran Varlıklar' grubunda mı izleneceğini belirleyen temel ölçüt aşağıdakilerden hangisidir?",
        {
            'A': 'Menkul kıymetin peşin mi yoksa vadeli mi satın alındığı (peşin alım → 11; vadeli alım → 24)',
            'B': 'İşlemin gerçekleştirildiği aracı kurum veya bankanın niteliği (yurt içi banka → 11; yurt dışı banka → 24)',
            'C': 'İşletmenin elde tutma amacı ve süresi (kısa vadeli kâr amacı → 11; uzun vadeli ortaklık/etkinlik amacı → 24)',
            'D': 'Menkul kıymeti çıkaran kurumun türü (özel şirket ihraç ederse → 11; kamu kurumu ihraç ederse → 24)',
            'E': 'Menkul kıymetin üzerinde yazılı olan nominal (itibari) değerinin büyüklüğü (yüksek nominal → 11; düşük nominal → 24)',
        },
        'C',
        'Belirleyici ölçüt **elde tutma amacı ve süresidir**: kısa vadeli kâr/gelir amacıyla tutulanlar **11 Menkul Kıymetler** (dönen varlık); uzun vadeli ortaklık/etkinlik amacıyla tutulanlar **24 Mali Duran Varlıklar** (İştirakler/Bağlı Ortaklıklar) grubunda izlenir.',
        "1 Sıra No'lu MSUGT - 11 / 24 ayrımı",
    ),
    # düzey 2
    '0047': patch(
        'Önceki dönemde menkul kıymetleri için 9.000 ₺ değer düşüklüğü karşılığı ayıran işletme, bu dönem menkul kıymetlerin değerinin geri yükseldiğini ve karşılığın konusunun kalmadığını tespit etmiştir. Karşılığın iptaline ilişkin kayıt aşağıdakilerden hangisidir?',
        {
            'A': '654 Karşılık Giderleri (borç) 9.000 / 119 Menkul Kıymetler Değer Düşüklüğü Karşılığı (alacak) 9.000',
            'B': '119 Menkul Kıymetler Değer Düşüklüğü Karşılığı (borç) 9.000 / 644 Konusu Kalmayan Karşılıklar (alacak) 9.000',
            'C': '644 Konusu Kalmayan Karşılıklar (borç) 9.000 / 119 Menkul Kıymetler Değer Düşüklüğü Karşılığı (alacak) 9.000',
            'D': '110 Hisse Senetleri (borç) 9.000 / 645 Menkul Kıymet Satış Kârları (alacak) 9.000',
            'E': '119 Menkul Kıymetler Değer Düşüklüğü Karşılığı (borç) 9.000 / 110 Hisse Senetleri (alacak) 9.000',
        },
        'B',
        'Konusu kalmayan karşılık gelir yazılarak iptal edilir: **119 Menkul Kıymetler Değer Düşüklüğü Karşılığı (borç) 9.000 / 644 Konusu Kalmayan Karşılıklar (alacak) 9.000**. 644 bir gelir hesabıdır.',
        "1 Sıra No'lu MSUGT - 119/644",
    ),
    # düzey 2
    '0048': patch(
        "Bir işletme nakit fazlasını değerlendirmek için kısa vadeli olarak bir portföy yönetim şirketinin kurduğu yatırım fonuna ait katılma belgelerini satın almıştır. Fonun portföyünün önemli bölümü Türkiye'de kurulmuş şirketlerin hisse senetlerinden oluşmaktadır.\n\nBu katılma belgeleri hangi hesapta izlenir?",
        {
            'A': '118 Diğer Menkul Kıymetler',
            'B': '112 Kamu Kesimi Tahvil, Senet ve Bonoları',
            'C': '153 Ticari Mallar',
            'D': '110 Hisse Senetleri',
            'E': '120 Alıcılar',
        },
        'A',
        "Yatırım fonu katılma belgeleri, 110/111/112'ye girmeyen menkul kıymetler olarak **118 Diğer Menkul Kıymetler** hesabında izlenir.",
        "1 Sıra No'lu MSUGT - 118 Diğer Menkul Kıymetler",
    ),
    # düzey 2
    '0049': patch(
        "Bilançoda '11 Menkul Kıymetler' grubu genellikle hangi grubun hemen ardından, ikinci en likit kalem olarak yer alır?",
        {
            'A': 'Kısa Vadeli Yabancı Kaynaklar',
            'B': 'Stoklar',
            'C': 'Maddi Duran Varlıklar',
            'D': 'Hazır Değerler',
            'E': 'Özkaynaklar',
        },
        'D',
        'Bilanço aktifi likidite esasına göre sıralanır; **Hazır Değerler** den (en likit) sonra, kolayca paraya çevrilebildikleri için **Menkul Kıymetler** gelir. İkisi de dönen varlıkların başında yer alır.',
        "1 Sıra No'lu MSUGT - Bilanço likidite sıralaması",
    ),
    # düzey 3
    '0050': patch(
        "Bir işletmenin dönem sonu mizanında 110 Hisse Senetleri 200.000 ₺, 112 Kamu Kesimi Tahvil, Senet ve Bonoları 100.000 ₺ ve 119 Menkul Kıymetler Değer Düşüklüğü Karşılığı 15.000 ₺ kalanları bulunmaktadır. Karşılık, borsa değeri maliyetinin altına düşen hisse senetleri için ayrılmıştır.\n\nMenkul kıymetlerin bilançodaki net tutarı kaç ₺'dir?",
        {
            'A': '185.000',
            'B': '315.000',
            'C': '300.000',
            'D': '215.000',
            'E': '285.000',
        },
        'E',
        'Net menkul kıymetler = (110 + 112) − 119 = (200.000 + 100.000) − 15.000 = **285.000 ₺**. 119 aktifi düzenleyici olduğundan düşülür.',
        "1 Sıra No'lu MSUGT - 11/119 net gösterim",
    ),
    # düzey 3
    '0051': patch(
        "Alım satım amacıyla alınan borsaya kayıtlı bir pay senedinin alış bedeli 100.000 ₺, dönem sonu gerçeğe uygun değeri 130.000 ₺'dir. VUK 279 ile TFRS 9'un gerçeğe uygun değer farkı kâr veya zarara yansıtılan sınıfı karşılaştırıldığında dönem sonu değerleri hangisidir?",
        {
            'A': 'Her iki çerçevede 130.000 ₺ ancak fark gelir yazılmaz.',
            'B': "VUK 100.000 ₺; TFRS 130.000 ₺ ve TFRS'de 30.000 ₺ değerleme kazancı",
            'C': 'VUK 130.000 ₺; TFRS 100.000 ₺',
            'D': 'Her iki çerçevede 100.000 ₺',
            'E': 'VUK 30.000 ₺; TFRS 130.000 ₺',
        },
        'B',
        "VUK 279 uyarınca pay senedi **alış bedeli 100.000 ₺** ile kalır. TFRS 9'da alım satım amaçlı pay senedi gerçeğe uygun değer farkı kâr veya zarara yansıtılan sınıftadır; **130.000 ₺** ölçülür ve **30.000 ₺ kazanç** kâr veya zarara alınır.",
        '213 sayılı VUK md. 279; TFRS 9 par. 5.7.1',
    ),
    # düzey 2
    '0052': patch(
        "İştiraklerden elde edilen temettü '640 İştiraklerden Temettü Gelirleri'nde izlenir. Bağlı ortaklıklardan elde edilen temettü ise hangi hesapta izlenir?",
        {
            'A': '640 İştiraklerden Temettü Gelirleri',
            'B': '645 Menkul Kıymet Satış Kârları',
            'C': '641 Bağlı Ortaklıklardan Temettü Gelirleri',
            'D': '642 Faiz Gelirleri',
            'E': '600 Yurt İçi Satışlar',
        },
        'C',
        "Bağlı ortaklıklardan elde edilen temettü **641 Bağlı Ortaklıklardan Temettü Gelirleri** hesabında izlenir. İştiraklerden olan temettü ise 640'tadır; ikisi ayrı gelir hesaplarıdır.",
        "1 Sıra No'lu MSUGT - 640/641",
    ),
    # düzey 3
    '0053': patch(
        'Bir işletmenin menkul kıymet alım-satımı, ana faaliyet konusu (esas faaliyeti) değildir. Bu nedenle menkul kıymet satışından doğan kâr/zarar aşağıdakilerden hangisiyle gösterilir?',
        {
            'A': '645 Menkul Kıymet Satış Kârları / 655 Menkul Kıymet Satış Zararları (diğer faaliyetlerden olağan)',
            'B': '600 Yurt İçi Satışlar / 621 Satılan Ticari Malların Maliyeti (brüt satış kârı içinde gösterilir)',
            'C': '649 Diğer Olağan Gelir ve Kârlar / 659 Diğer Olağan Gider ve Zararlar (diğer olağan bölümde)',
            'D': '642 Faiz Gelirleri / 660 Kısa Vadeli Borçlanma Giderleri (finansman gelir-gider bölümünde)',
            'E': '679 Diğer Olağandışı Gelir ve Kârlar / 689 Diğer Olağandışı Gider ve Zararlar (olağandışı bölümde)',
        },
        'A',
        'Menkul kıymet alım-satımı esas faaliyet olmadığından, satış kâr/zararı **645 / 655** hesaplarında, gelir tablosunun **Diğer Faaliyetlerden Olağan Gelir-Gider** bölümünde gösterilir; brüt satış kârı (600/621) içinde yer almaz.',
        "1 Sıra No'lu MSUGT - 645/655",
    ),
    # düzey 2
    '0054': patch(
        "Mevsimsel satış yapan bir işletmenin yaz aylarında elinde biriken ve sonbahara kadar ihtiyaç duymayacağı 2.000.000 ₺ nakdi vardır. İşletme bu tutarın bir kısmıyla altı ay vadeli devlet tahvili, bir kısmıyla da borsada işlem gören hisse senetleri almış ve bunları '11 Menkul Kıymetler' grubunda izlemiştir.\n\nMenkul kıymetler grubunu (11) elde bulundurmanın işletme açısından temel amacı aşağıdakilerden hangisidir?",
        {
            'A': 'İşletmenin üretim faaliyetinde doğrudan hammadde ve yardımcı malzeme olarak tüketmek üzere stok bulundurmak',
            'B': 'İşletmenin personeline ait ücret, prim ve yasal kesintileri zamanında ödeyerek yükümlülüklerini yerine getirmek',
            'C': 'İşletmenin satıcılara olan kısa vadeli ticari borçlarını vadesinde kapatarak cari yükümlülüklerini azaltmak',
            'D': 'İşletmenin faaliyetinde bir yıldan uzun süre kullanılacak bina, makine ve taşıt gibi maddi duran varlıklar edinmek',
            'E': 'Atıl (kısa vadede ihtiyaç duyulmayan) fonları değerlendirerek faiz/temettü geliri veya değer artış kârı elde etmek',
        },
        'E',
        'Menkul kıymetler; işletmenin kısa vadede ihtiyaç duymadığı **atıl fonlarını değerlendirerek** faiz/temettü geliri veya kısa vadeli değer artış kârı elde etmek amacıyla elde tutulur.',
        "1 Sıra No'lu MSUGT - 11 Menkul Kıymetler (amaç)",
    ),
    # düzey 2
    '0055': patch(
        "'118 Diğer Menkul Kıymetler' hesabında izlenmeye en uygun kalem aşağıdakilerden hangisidir?",
        {
            'A': 'İşletmenin faaliyetinde bir yıldan uzun süre kullanmak üzere edindiği bina, makine ve taşıt gibi varlıklar',
            'B': 'İşletmenin mal ve hizmet alımından doğan, satıcılara olan kısa ve uzun vadeli ticari borçlarının tamamı',
            'C': 'İşletmenin kasasında ve bankada bulunan, henüz herhangi bir menkul kıymete bağlanmamış nakit mevcutları',
            'D': 'İşletmenin esas faaliyet konusu olan, satmak amacıyla depoda elde tuttuğu ticari mal ve mamul stokları',
            'E': "110, 111 ve 112'ye girmeyen yatırım fonu katılma belgesi, gelir ortaklığı senedi gibi menkul kıymetler",
        },
        'E',
        '**118 Diğer Menkul Kıymetler**, hisse senedi (110), özel/kamu tahvil-senet-bonoları (111/112) dışında kalan yatırım fonu katılma belgesi, gelir ortaklığı senedi vb. menkul kıymetleri izler.',
        "1 Sıra No'lu MSUGT - 118 Diğer Menkul Kıymetler",
    ),
    # düzey 2
    '0056': patch(
        "Bir menkul kıymetin 'nominal (itibari) değeri' ile 'alış bedeli' ile ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Nominal değer, menkul kıymetin üzerinde yazılı değeridir',
            'B': 'Alış bedeli ile nominal değer farklı olabilir',
            'C': 'Nominal değer, menkul kıymeti edinmek için fiilen ödenen tutardır',
            'D': 'Menkul kıymetler kayıtlara alış bedeliyle alınır',
            'E': 'Tahvil nominal değerinin altında da satın alınabilir',
        },
        'C',
        'Nominal değer menkul kıymetin üzerinde yazılı değeridir; fiilen ödenen tutar alış bedelidir ve ikisi farklı olabilir (ör. iskontolu tahvil alımı). Menkul kıymetler kayıtlara alış bedeliyle alınır.',
        "1 Sıra No'lu MSUGT / VUK - nominal değer vs alış bedeli",
    ),
    # düzey 3
    '0057': patch(
        "İşletme, 80.000 ₺'ye aldığı hisse senetlerinin yarısını (maliyeti 40.000 ₺ olan kısmını) 52.000 ₺'ye peşin satmıştır. Bu satışa ilişkin aşağıdakilerden hangisi doğrudur?",
        {
            'A': '655 Menkul Kıymet Satış Zararları 12.000 ₺ borçlandırılır; 110 Hisse Senetleri 52.000 ₺ alacaklandırılır.',
            'B': '600 Yurt İçi Satışlar 52.000 ₺ alacaklandırılır; 621 Satılan Ticari Malların Maliyeti 40.000 ₺ borçlandırılır.',
            'C': '645 Menkul Kıymet Satış Kârları 12.000 ₺ alacaklandırılır; 110 Hisse Senetleri 40.000 ₺ alacaklandırılır.',
            'D': '110 Hisse Senetleri satılan kısım için 52.000 ₺ alacaklandırılır; satıştan herhangi bir kâr veya zarar doğmaz.',
            'E': '645 Menkul Kıymet Satış Kârları 52.000 ₺ alacaklandırılır; 110 Hisse Senetleri hesabına kayıt yapılmaz.',
        },
        'C',
        "Satılan kısmın maliyeti 40.000 ₺, satış 52.000 ₺ → kâr 12.000 ₺. Kayıt: 100 Kasa (borç) 52.000 / **110 Hisse Senetleri (alacak) 40.000** (satılan kısmın maliyeti) + **645 Menkul Kıymet Satış Kârları (alacak) 12.000**. Kalan 40.000 ₺'lik hisse 110'da izlenmeye devam eder.",
        "1 Sıra No'lu MSUGT - 110/645 (kısmi satış)",
    ),
    # düzey 3
    '0058': patch(
        "İşletme geçici yatırım amacıyla üç ay vadeli 240.000 ₺ nominal değerli bir finansman bonosunu 225.000 ₺'ye satın almıştır. Vade sonunda nominal değer banka hesabına tahsil edilmiştir (stopaj ihmal). Buna göre vade sonu kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '102 Bankalar hesabı 225.000 ₺ borçlandırılır',
            'B': '642 Faiz Gelirleri hesabı 240.000 ₺ alacaklandırılır',
            'C': '645 Menkul Kıymet Satış Kârları hesabı 15.000 ₺ alacaklandırılır',
            'D': '111 Özel Kesim Tahvil, Senet ve Bonoları hesabı 225.000 ₺ alacaklandırılır',
            'E': '111 Özel Kesim Tahvil, Senet ve Bonoları hesabı 240.000 ₺ alacaklandırılır',
        },
        'D',
        'Kayıt: 102 (borç) 240.000 / **111 (alacak) 225.000** + 642 (alacak) 15.000. Bono alış bedeliyle kayıtlıdır; nominal değerle aradaki fark faiz gelirdir.',
        'THP 111, 102, 642',
    ),
    # düzey 2
    '0059': patch(
        "Menkul kıymetlerle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kısa vadeli kâr amacıyla alınan hisse senetleri 110 Hisse Senetleri hesabında izlenir.\n\nII. Uzun vadeli olarak yönetimde söz sahibi olmak amacıyla alınan hisseler 110'da izlenir.\n\nIII. Özel sektör şirketlerinin çıkardığı tahviller 111 hesabında izlenir.",
        {
            'A': 'I ve III',
            'B': 'Yalnız I',
            'C': 'II ve III',
            'D': 'Yalnız III',
            'E': 'I ve II',
        },
        'A',
        'I ve III doğrudur. II yanlıştır: yönetimde söz sahibi olmak amacıyla uzun vadeli alınan hisseler **24 Mali Duran Varlıklar** grubunda (ör. 242 İştirakler) izlenir.',
        'THP 110, 111, 242',
    ),
    # düzey 3
    '0060': patch(
        "İşletme adedini 12 ₺'den aldığı 1.000 adet hisse senediyle portföyünde izlemektedir. Hisseleri çıkaran şirket iç kaynaklardan %50 oranında bedelsiz sermaye artırımı yapmış ve işletmeye bedelsiz hisse vermiştir. Buna göre işletmenin elindeki hisselerin yeni birim maliyeti kaç ₺'dir?",
        {
            'A': '18 ₺',
            'B': '8 ₺',
            'C': '10 ₺',
            'D': '12 ₺',
            'E': '6 ₺',
        },
        'B',
        "Bedelsiz hisse yeni bir maliyet doğurmaz; toplam maliyet 12.000 ₺ olarak kalır, hisse sayısı 1.500'e çıkar. Yeni birim maliyet 12.000 / 1.500 = **8 ₺**.",
        'VUK m. 279; hisse maliyeti',
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
    print(f"1 paket / {len(PATCHES)} soru ('Menkul Kiymetler' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
