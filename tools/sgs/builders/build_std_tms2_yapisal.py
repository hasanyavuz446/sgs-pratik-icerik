#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TMS 2 Stoklar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gercek sinav profiliyle yeniden yazim (senaryo kok + kisa tutar/terim sik). Gercek sinavda en sik sorulan standart: NGD hesaplari (tamamlanma ve satis maliyetleri, kalem bazinda degerleme, dovizli stok, sozlesmeli satis, hammadde istisnasi), dusuk/yuksek uretimde sabit GUG dagitimi, perakende yontemi, kapsam ve aciklamalar farkli tutar ve yapilarla islendi. Ayrica satin alma ve donusturme maliyeti, maliyete girmeyen kalemler, vadeli alim, birlesik ve yan urunler, hasat edilen urunler, FIFO/agirlikli ortalama/ozel tanimlama, LIFO yasagi, deger dusuklugu iptali ve gider olarak tanima. Eski surum 43 mutlak ifadeli celdirici tasiyordu (kor %38). 29 hesap sorusu modulde hesaplandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: TMS 2 Stoklar (KGK); TMS 10, TMS 21, TMS 23, TMS 34, TMS 41 ilgili paragraflar
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/tms_2_stoklar.json"
STYLE_REF = 'SGS Muhasebe Standartlari (gercek sinav profiline kalibre: senaryo kok + kisa sik)'
ONEK = "std-tms2-gen-"


def patch(stem, options, answer, solution, ref='TMS 2 Stoklar'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Bir holdingin şirketlerinde şu kalemler bulunmaktadır: perakende şirketinde satılmak üzere alınan giysiler, üretim şirketinde yarı mamuller, gayrimenkul şirketinde satmak için inşa edilen konutlar, tarım şirketinde hasat noktasına kadar canlı olan meyve ağaçları ve hizmet şirketinde kullanılacak yedek malzemeler. Bunlardan hangisi TMS 2'nin kapsamı dışındadır?",
        {
            'A': 'Satmak için inşa edilen konutlar',
            'B': 'Canlı meyve ağaçları',
            'C': 'Yarı mamuller',
            'D': 'Yedek malzemeler',
            'E': 'Satılmak üzere alınan giysiler',
        },
        'B',
        "TMS 2 p. 2(c)'ye göre **tarımsal faaliyetle ilgili biyolojik varlıklar** ve hasat noktasındaki tarımsal ürünler TMS 41 kapsamındadır; hasattan sonraki ürünler TMS 2'ye girer. Satmak için inşa edilen konutlar gayrimenkul şirketinin stokudur.",
        'TMS 2 p. 2-3',
    ),
    # düzey 3
    '0002': patch(
        "Normal üretim kapasitesi 15.000 adet olan bir işletme, talep daralması nedeniyle dönemde 10.000 adet üretmiştir. Dönemin maliyetleri: direkt malzeme 120.000 ₺, direkt işçilik 90.000 ₺, değişken GÜG 60.000 ₺, sabit GÜG 150.000 ₺. TMS 2'ye göre mamullerin birim maliyeti kaç ₺'dir?",
        {
            'A': '28',
            'B': '37',
            'C': '32',
            'D': '27',
            'E': '15',
        },
        'B',
        "TMS 2 p. 13'e göre sabit genel üretim giderleri **normal kapasiteye** göre dağıtılır; düşük üretim nedeniyle birim başına dağıtılan sabit gider artırılmaz, dağıtılmayan kısım gider yazılır. Birim maliyet: (120.000 + 90.000 + 60.000) / 10.000 + 150.000 / 15.000 = **37 ₺**.",
        'TMS 2 p. 13',
    ),
    # düzey 3
    '0003': patch(
        "Bir üretim işletmesinin dönem giderleri arasında şunlar vardır: anormal miktarda fire 30.000 ₺, üretim sürecinin bir aşaması olmayan mamul depolama maliyeti 12.000 ₺, genel yönetim giderleri 45.000 ₺, satış giderleri 25.000 ₺ ve üretim sırasında normal olarak ortaya çıkan fire 8.000 ₺. Bunlardan kaç ₺'si stok maliyetine dâhil edilir?",
        {
            'A': '0',
            'B': '120.000',
            'C': '38.000',
            'D': '20.000',
            'E': '8.000',
        },
        'E',
        "TMS 2 p. 16'ya göre **anormal fireler, üretim sürecinde gerekli olmayan depolama maliyetleri, stokları mevcut konum ve durumuna getirmeye katkısı olmayan genel yönetim giderleri ve satış maliyetleri** stok maliyetine dâhil edilmez. Normal fire üretim maliyetinin parçasıdır: **8.000 ₺**.",
        'TMS 2 p. 16',
    ),
    # düzey 3
    '0004': patch(
        "Bir işletmenin dönem başı stoku 1.000 birim × 10 ₺'dir. Dönemde 2.000 birim 10 ₺'den ve 1.000 birim 12 ₺'den alınmış, 2.500 birim satılmıştır. Dönem sonunda tek seferde hesaplanan ağırlıklı ortalama maliyet yöntemine göre satışların maliyeti kaç ₺'dir?",
        {
            'A': '27.500',
            'B': '26.250',
            'C': '30.000',
            'D': '42.000',
            'E': '27.000',
        },
        'B',
        'Ağırlıklı ortalama birim maliyet: 42.000 / 4.000 = 10,50 ₺. Satışların maliyeti 2.500 × 10,50 = **26.250 ₺**.',
        'TMS 2 p. 27',
    ),
    # düzey 2
    '0005': patch(
        "Bir mücevher üreticisi, her biri müşteriye özel tasarlanan ve birbirinin yerine kullanılamayan kolyeler üretmektedir. TMS 2'ye göre bu stokların maliyeti hangi yöntemle belirlenir?",
        {
            'A': 'FIFO',
            'B': 'Özel tanımlama',
            'C': 'Standart maliyet',
            'D': 'Perakende yöntemi',
            'E': 'Ağırlıklı ortalama',
        },
        'B',
        "TMS 2 p. 23'e göre **normalde birbirinin yerine geçemeyen** stok kalemlerinin ve belirli projeler için üretilip ayrılmış mal ve hizmetlerin maliyeti, **özel tanımlama** yoluyla belirlenir.",
        'TMS 2 p. 23-24',
    ),
    # düzey 2
    '0006': patch(
        "Bir işletme, normal malzeme, işçilik, verimlilik ve kapasite kullanım düzeylerini dikkate alan standart maliyet yöntemini kullanmaktadır. Bu yöntemin TMS 2'ye göre kullanılabilmesinin koşulu hangisidir?",
        {
            'A': 'Stok miktarının az olması',
            'B': 'Denetçinin önceden onayı',
            'C': 'Sonuçların fiilî maliyete yakın olması',
            'D': 'Satış fiyatlarının sabit olması',
            'E': 'Vergi idaresinin onayı',
        },
        'C',
        "TMS 2 p. 21'e göre standart maliyet yöntemi ve perakende yöntemi gibi ölçüm teknikleri, **sonuçları maliyete yakın** olduğu sürece kolaylık amacıyla kullanılabilir; standartlar düzenli olarak gözden geçirilir.",
        'TMS 2 p. 21',
    ),
    # düzey 3
    '0007': patch(
        'Bir işletmenin birbirinden farklı üç ürününe ilişkin dönem sonu bilgileri şöyledir: A ürünü 200 adet, birim maliyet 300 ₺, birim NGD 250 ₺; B ürünü 100 adet, birim maliyet 400 ₺, birim NGD 450 ₺; C ürünü 50 adet, birim maliyet 600 ₺, birim NGD 580 ₺. Stoklar kalem bazında değerlendiğinde finansal durum tablosunda kaç ₺ ile gösterilir?',
        {
            'A': '134.000',
            'B': '130.000',
            'C': '124.000',
            'D': '125.000',
            'E': '119.000',
        },
        'E',
        "TMS 2 p. 29'a göre stoklar maliyet veya NGD'den düşük olanına **genellikle kalem bazında** indirilir; toplam bazda karşılaştırma yapılmaz: A 200 × 250 + B 100 × 400 + C 50 × 580 = **119.000 ₺**.",
        'TMS 2 p. 29',
    ),
    # düzey 3
    '0008': patch(
        "Bir üretim işletmesinin elinde maliyeti 90.000 ₺ olan hammadde vardır; hammaddenin yenileme maliyeti 70.000 ₺'ye inmiştir. Bu hammaddenin kullanılacağı mamullerin tahmini maliyeti 300.000 ₺, tahmini NGD'si 280.000 ₺'dir. TMS 2'ye göre hammaddenin NGD'sinin en iyi ölçüsü olabilecek tutar kaç ₺'dir?",
        {
            'A': '70.000',
            'B': '280.000',
            'C': '90.000',
            'D': '120.000',
            'E': '100.000',
        },
        'A',
        "TMS 2 p. 32'ye göre hammadde fiyatındaki düşüş mamullerin **maliyetin altında satılacağını** gösteriyorsa hammaddeler NGD'ye indirilir; bu durumda **yenileme maliyeti** hammaddenin NGD'sinin en uygun ölçüsü olabilir: **70.000 ₺**.",
        'TMS 2 p. 32',
    ),
    # düzey 3
    '0009': patch(
        "Bir işletme geçen yıl maliyeti 100.000 ₺ olan stoklar için 20.000 ₺ değer düşüklüğü karşılığı ayırmıştır. Stoklar bu yıl sonunda da elde olup koşulların değişmesi nedeniyle NGD 95.000 ₺'ye yükselmiştir. Bu yıl iptal edilecek karşılık kaç ₺'dir ve nereye yansır?",
        {
            'A': 'İptal edilmez',
            'B': '15.000 ₺, satışların maliyetini azaltır',
            'C': '20.000 ₺, geçmiş yıllar kârlarına',
            'D': "15.000 ₺, DKG'ye",
            'E': '20.000 ₺, satışların maliyetini azaltır',
        },
        'B',
        "TMS 2 p. 33-34'e göre değer düşüklüğüne neden olan koşullar ortadan kalktığında veya NGD arttığında **önceki değer düşüklüğü tutarıyla sınırlı** olmak üzere iptal yapılır ve yeni defter değeri maliyet ile NGD'nin düşüğü olur: yeni karşılık 5.000 ₺, iptal **15.000 ₺**; iptal, iptalin olduğu dönemde gider olarak tanınan stok tutarını azaltır.",
        'TMS 2 p. 33-34',
    ),
    # düzey 2
    '0010': patch(
        'Bir işletme ara dönem (çeyreklik) finansal tablolarını hazırlamaktadır. Çeyrek sonunda ürettiği maskelerin satış fiyatı, geçici bir talep düşüşüyle maliyetin altına inmiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Değer düşüklüğü ara dönemde tanınabilir',
            'B': 'Sonraki ara dönemde koşullar düzelirse iptal yapılabilir',
            'C': 'Ara dönemde de yıllık tablolarla aynı ilkeler uygulanır',
            'D': "Stoklar maliyet ile NGD'nin düşüğüyle ölçülür",
            'E': "Ara dönemde stoklar NGD'ye indirilmez, yıl sonu beklenir",
        },
        'E',
        "TMS 2 p. 9 ve TMS 34'e göre stoklar ara dönem tablolarında da **maliyet ile NGD'nin düşüğüyle** ölçülür; ara dönemde tanınan değer düşüklüğü sonraki ara dönemde koşullar değişirse iptal edilebilir.",
        'TMS 2 p. 9; TMS 34',
    ),
    # düzey 2
    '0011': patch(
        "Bir ticari işletmenin dönem başı stoku 150.000 ₺, dönem içi net alışları 900.000 ₺, dönem sonu stoku maliyet ve NGD karşılaştırmasından sonra 180.000 ₺'dir; dönem sonu stoklarda değer düşüklüğü yoktur. Satışların maliyeti kaç ₺'dir?",
        {
            'A': '900.000',
            'B': '1.050.000',
            'C': '1.230.000',
            'D': '870.000',
            'E': '1.020.000',
        },
        'D',
        "TMS 2 p. 34'e göre satılan stokların defter değeri hasılatın tanındığı dönemde gider yazılır: 150.000 + 900.000 − 180.000 = **870.000 ₺**.",
        'TMS 2 p. 34',
    ),
    # düzey 3
    '0012': patch(
        "Bir işletmenin elinde birim maliyeti 820 ₺ olan 500 adet ürün vardır. Tahmini birim satış fiyatı 900 ₺'dir; satış fiyatı üzerinden %5 komisyon ödenecek ve müşteriye teslim için birim başına 20 ₺ nakliye yapılacaktır. Ürünlerin toplam NGD'si kaç ₺'dir?",
        {
            'A': '417.500',
            'B': '427.500',
            'C': '440.000',
            'D': '410.000',
            'E': '450.000',
        },
        'A',
        "TMS 2 p. 6'ya göre NGD, tahmini satış fiyatından satış için gerekli tahmini maliyetler düşülerek bulunur ve p. 7'ye göre **işletmeye özgüdür**: birim 900 − 45 − 20 = 835 ₺; toplam 500 × 835 = **417.500 ₺**.",
        'TMS 2 p. 6-7',
    ),
    # düzey 3
    '0013': patch(
        "Bir işletme ortak bir üretim sürecinde A ve B birleşik ürünlerini üretmektedir. Ayrılma noktasına kadar ortak maliyet 400.000 ₺'dir; A'nın satış değeri 300.000 ₺, B'nin satış değeri 200.000 ₺'dir. İşletme ortak maliyeti göreli satış değerlerine göre dağıtmaktadır. A ürününe dağıtılacak maliyet kaç ₺'dir?",
        {
            'A': '400.000',
            'B': '300.000',
            'C': '200.000',
            'D': '240.000',
            'E': '160.000',
        },
        'D',
        "TMS 2 p. 14'e göre birleşik ürünlerin dönüştürme maliyetleri ayrı ayrı belirlenemiyorsa **akılcı ve tutarlı bir esasla**, örneğin ayrılma noktasındaki **göreli satış değerlerine** göre dağıtılır: 400.000 × 300.000 / 500.000 = **240.000 ₺**.",
        'TMS 2 p. 14',
    ),
    # düzey 2
    '0014': patch(
        "Bir işletme değişken genel üretim giderlerini stoklara dağıtmaktadır. TMS 2'ye göre değişken genel üretim giderleri hangi esasa göre dağıtılır?",
        {
            'A': 'Teorik kapasiteye göre',
            'B': 'Bütçe tutarına göre',
            'C': 'Normal kapasiteye göre',
            'D': 'Fiilî üretim kullanımına göre',
            'E': 'Satış miktarına göre',
        },
        'D',
        "TMS 2 p. 13'e göre değişken genel üretim giderleri, üretim tesislerinin **fiilî kullanımı** esas alınarak her bir üretim birimine dağıtılır; sabit giderler ise normal kapasiteye göre dağıtılır.",
        'TMS 2 p. 13',
    ),
    # düzey 2
    '0015': patch(
        'Alış fiyatlarının dönem boyunca sürekli arttığı bir ortamda, diğer koşullar aynıyken aşağıdaki maliyet formüllerinden hangisi dönem sonu stokunu daha yüksek gösterir?',
        {
            'A': 'Perakende yöntemi',
            'B': 'Özel tanımlama olmaksızın ortalama',
            'C': 'Standart maliyet',
            'D': 'Ağırlıklı ortalama',
            'E': 'FIFO',
        },
        'E',
        "Fiyatların arttığı dönemde **FIFO**'da dönem sonu stoku en son (yüksek fiyatlı) alışlardan oluşur; ağırlıklı ortalamada eski ve yeni fiyatlar ortalandığından stok daha düşük değerlenir.",
        'TMS 2 p. 25-27',
    ),
    # düzey 3
    '0016': patch(
        'Bir peynir üreticisi, peynirlerin satılabilir hâle gelmesi için üretimin zorunlu bir aşaması olarak 6 ay soğuk depoda olgunlaşmasını sağlamaktadır. Bu olgunlaştırma deposunun maliyetleri hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Dönem gideri yazılır',
            'B': 'Satış giderine eklenir',
            'C': 'Stok maliyetine dâhil edilir',
            'D': 'Genel yönetim giderine eklenir',
            'E': 'Özkaynaktan düşülür',
        },
        'C',
        "TMS 2 p. 16(b)'ye göre depolama maliyetleri kural olarak stok maliyetine dâhil edilmez; ancak **üretim sürecinde bir sonraki üretim aşamasından önce gerekli olan** depolama maliyetleri bu kuralın istisnasıdır ve maliyete girer.",
        'TMS 2 p. 16(b)',
    ),
    # düzey 1
    '0017': patch(
        "İşletmenin olağan faaliyet akışında satış amacıyla elde tutulan, bu satışa yönelik olarak üretim sürecinde bulunan veya üretimde ya da hizmet sunumunda kullanılacak ilk madde ve malzeme şeklindeki varlıklar TMS 2'de nasıl adlandırılır?",
        {
            'A': 'Satış amaçlı duran varlıklar',
            'B': 'Stoklar',
            'C': 'Maddi duran varlıklar',
            'D': 'Yatırım amaçlı gayrimenkuller',
            'E': 'Finansal varlıklar',
        },
        'B',
        "TMS 2 p. 6'daki tanıma göre bu varlıklar **stoklardır**.",
        'TMS 2 p. 6',
    ),
    # düzey 3
    '0018': patch(
        "Perakende yöntemini kullanan bir mağaza, sezon sonunda bazı ürünlerin satış fiyatlarını ilk fiyatlarının altına indirmiştir. TMS 2'ye göre kullanılan brüt kâr marjı yüzdesi hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İndirimler dikkate alınmaz',
            'B': 'Marj geçen yılın ortalamasıdır',
            'C': 'Marj her ürün için sabit tutulur',
            'D': 'Marj vergi mevzuatına göre belirlenir',
            'E': 'İndirimli stoklar dikkate alınır',
        },
        'E',
        "TMS 2 p. 22'ye göre perakende yönteminde kullanılan yüzde, **satış fiyatı ilk satış fiyatının altına indirilmiş stokları dikkate alır**; çoğunlukla her perakende bölümü için ortalama bir yüzde kullanılır.",
        'TMS 2 p. 22',
    ),
    # düzey 2
    '0019': patch(
        'Aşağıdakilerden hangileri stokların maliyetine dâhil edilir?\n\nI. İthalat sırasında ödenen gümrük vergisi\n\nII. Satış bölümünün personel giderleri\n\nIII. Stokların işletme deposuna taşınma maliyeti',
        {
            'A': 'Yalnız III',
            'B': 'Yalnız I',
            'C': 'I ve III',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'C',
        "TMS 2 p. 11'e göre ithalat vergileri (I) ve nakliye (III) satın alma maliyetine girer. p. 16'ya göre **satış maliyetleri** stok maliyetine dâhil edilmez (II).",
        'TMS 2 p. 11, 16',
    ),
    # düzey 3
    '0020': patch(
        'Aşağıdakilerden hangileri doğrudur?\n\nI. Vadeli alımdaki finansman unsuru faiz gideri olarak tanınır\n\nII. Değer düşüklüğü iptali önceki değer düşüklüğü tutarını aşabilir\n\nIII. Stoklardaki kayıplar oluştuğu dönemde gider yazılır',
        {
            'A': 'I ve III',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'Yalnız I',
            'E': 'Yalnız III',
        },
        'A',
        "TMS 2 p. 18'e göre finansman unsuru faiz gideridir (I); p. 34'e göre kayıplar oluştuğu dönemde gider yazılır (III). p. 33'e göre iptal **önceki değer düşüklüğü tutarıyla sınırlıdır** (II yanlış).",
        'TMS 2 p. 18, 33-34',
    ),
    # düzey 2
    '0021': patch(
        'Bir emtia komisyoncu-tüccarı, kısa vadede fiyat dalgalanmalarından kâr elde etmek için buğday alıp satmaktadır. Stoklarını satış maliyetleri düşülmüş gerçeğe uygun değerle ölçmektedir. Bu stokların ölçümü hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': "TMS 41'e göre ölçülür",
            'B': "Maliyet ile NGD'nin düşüğüyle ölçülür",
            'C': 'Maliyetle ölçülmelidir',
            'D': "TMS 2'nin ölçüm hükümleri dışındadır",
            'E': "TFRS 9'a göre ölçülür",
        },
        'D',
        "TMS 2 p. 3(b) ve 5'e göre stoklarını **satış maliyetleri düşülmüş gerçeğe uygun değerle** ölçen emtia komisyoncu-tüccarları TMS 2'nin ölçüm hükümlerinin kapsamı dışındadır; değer değişimleri kâr veya zarara yansıtılır.",
        'TMS 2 p. 3(b), 5',
    ),
    # düzey 3
    '0022': patch(
        "Normal kapasitesi 15.000 adet olan bir işletme dönemde 10.000 adet üretmiş ve 150.000 ₺ sabit genel üretim gideri katlanmıştır. Stok maliyetine dağıtılmayıp dönemin gideri olarak tanınacak sabit GÜG kaç ₺'dir?",
        {
            'A': '50.000',
            'B': '100.000',
            'C': '150.000',
            'D': '0',
            'E': '15',
        },
        'A',
        "TMS 2 p. 13'e göre birim başına sabit GÜG normal kapasiteye göre belirlenir: 150.000 / 15.000 = 10 ₺; üretime dağıtılan 100.000 ₺'dir. **Dağıtılmayan 50.000 ₺** oluştuğu dönemde gider yazılır.",
        'TMS 2 p. 13',
    ),
    # düzey 2
    '0023': patch(
        'Bir içki üreticisi, satılabilir hâle gelmesi için 5 yıl mahzende olgunlaşması gereken şaraplar üretmektedir; bu stoklar kullanıma veya satışa hazır hâle gelmesi uzun süre gerektiren özellikli varlıklardır. Bu stokların finansmanı için kullanılan kredinin faizi hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Satış giderine eklenir',
            'B': 'Gider olarak yazılır',
            'C': 'Özkaynaktan düşülür',
            'D': "TMS 23'e göre aktifleştirilebilir",
            'E': 'Stoklardan düşülür',
        },
        'D',
        "TMS 2 p. 17'ye göre stok maliyetine borçlanma maliyetlerinin dâhil edilebildiği sınırlı durumlar **TMS 23**'te belirlenmiştir; özellikli varlık niteliğindeki stoklarda borçlanma maliyetleri aktifleştirilebilir.",
        'TMS 2 p. 17; TMS 23',
    ),
    # düzey 3
    '0024': patch(
        "Bir işletmenin dönem başı stoku 1.000 birim × 10 ₺'dir. Dönemde önce 2.000 birim 10 ₺'den, sonra 1.000 birim 12 ₺'den alış yapılmış; 2.500 birim satılmıştır. FIFO yöntemine göre dönem sonu stok maliyeti kaç ₺'dir?",
        {
            'A': '15.750',
            'B': '15.000',
            'C': '17.000',
            'D': '19.000',
            'E': '12.000',
        },
        'C',
        "Dönem sonunda 1.500 birim kalır. FIFO'da ilk giren ilk çıktığından kalan birimler **en son alışlardan** oluşur: 1.500 × 12 = **17.000 ₺**.",
        'TMS 2 p. 25-27',
    ),
    # düzey 2
    '0025': patch(
        "Bir grup şirketinin Türkiye'deki ve Almanya'daki bağlı ortaklıklarında aynı nitelikte ve aynı amaçla kullanılan hammaddeler bulunmaktadır. Türkiye'deki şirket FIFO, Almanya'daki şirket ağırlıklı ortalama kullanmak istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Bu durumda tutarlı formül uygulanmalıdır',
            'B': "FIFO ve ağırlıklı ortalama TMS 2'de izin verilen formüllerdir",
            'C': 'Benzer nitelik ve kullanımdaki stoklar için aynı formül kullanılır',
            'D': 'Coğrafi konum farkı farklı formül için yeterli gerekçedir',
            'E': 'Farklı nitelik veya kullanımdaki stoklar için farklı formül haklı olabilir',
        },
        'D',
        "TMS 2 p. 25-26'ya göre işletme **benzer niteliği ve kullanımı olan bütün stoklar için aynı maliyet formülünü** kullanır; farklı nitelik veya kullanım farklı formülü haklı kılabilir, ancak **coğrafi konumdaki farklılık tek başına** farklı formül kullanmayı haklı kılmaz.",
        'TMS 2 p. 25-26',
    ),
    # düzey 3
    '0026': patch(
        "Hızlı değişen çok sayıda stok kalemi olan bir perakendeci, stok maliyetini ölçmek için perakende yöntemini kullanmaktadır. Dönem sonu stokların satış fiyatları toplamı 800.000 ₺, uygun brüt kâr marjı %30'dur. Stokların maliyeti kaç ₺'dir?",
        {
            'A': '615.385',
            'B': '560.000',
            'C': '240.000',
            'D': '1.040.000',
            'E': '800.000',
        },
        'B',
        "TMS 2 p. 22'ye göre perakende yönteminde stokların maliyeti, **satış fiyatından uygun brüt kâr marjı yüzdesi düşülerek** belirlenir: 800.000 × %70 = **560.000 ₺**.",
        'TMS 2 p. 22',
    ),
    # düzey 3
    '0027': patch(
        "Bir işletme yıl içinde kur 1 $ = 30 ₺ iken 10.000 $'a ticari mal ithal etmiştir. Yıl sonunda mallar satılmamıştır; işletme malları yurt dışına 12.000 $'a satmayı beklemektedir ve satış maliyeti yoktur. Yıl sonu kuru 1 $ = 28 ₺'dir. Mallar finansal durum tablosunda kaç ₺ ile gösterilir?",
        {
            'A': '300.000',
            'B': '280.000',
            'C': '336.000',
            'D': '360.000',
            'E': '20.000',
        },
        'A',
        "Stok parasal olmayan kalemdir; maliyeti işlem tarihi kuruyla 10.000 × 30 = 300.000 ₺'dir. NGD yıl sonu kuruyla 12.000 × 28 = 336.000 ₺'dir. TMS 2 p. 9 ve TMS 21 p. 25'e göre düşük olan **300.000 ₺** alınır.",
        'TMS 2 p. 9; TMS 21 p. 23',
    ),
    # düzey 3
    '0028': patch(
        "Bir işletmenin elindeki 1.000 birim ürünün birim maliyeti 48 ₺'dir. Bunların 600 birimi için bir müşteriyle birim fiyatı 55 ₺ olan kesin satış sözleşmesi vardır; kalan birimlerin tahmini satış fiyatı 50 ₺'dir. Satış maliyeti yoktur. Stoklar kaç ₺ ile gösterilir?",
        {
            'A': '53.000',
            'B': '50.000',
            'C': '55.000',
            'D': '46.000',
            'E': '48.000',
        },
        'E',
        "TMS 2 p. 31'e göre kesin satış sözleşmesi kapsamındaki stokların NGD'si **sözleşme fiyatına** dayanır; fazla miktarın NGD'si genel satış fiyatına göre belirlenir. Her iki kısımda da NGD maliyeti aştığından stoklar maliyetle ölçülür: **48.000 ₺**.",
        'TMS 2 p. 31',
    ),
    # düzey 3
    '0029': patch(
        'Bir işletme yıl sonunda NGD tahmin ederken, tahmin tarihinde mevcut en güvenilir kanıtları kullanmaktadır. Raporlama döneminden sonra, tablolar onaylanmadan önce gerçekleşen satış fiyatları dönem sonundaki koşulları doğrulamaktadır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Sonraki satışlar TMS 10 kapsamında kanıt sağlayabilir',
            'B': 'Tahminler mevcut en güvenilir kanıtlara dayanır',
            'C': 'Dönem sonu koşullarını doğrulayan sonraki fiyat değişimleri dikkate alınır',
            'D': 'Stokların elde tutulma amacı dikkate alınır',
            'E': 'NGD belirlenirken sonraki olaylar dikkate alınmaz',
        },
        'E',
        "TMS 2 p. 30'a göre NGD tahminleri mevcut en güvenilir kanıtlara dayanır ve **dönem sonundaki koşulları doğrulayan ölçüde, dönem sonundan sonra meydana gelen olaylarla doğrudan ilişkili fiyat veya maliyet değişimleri** dikkate alınır; stokların elde tutulma amacı da dikkate alınır.",
        'TMS 2 p. 30',
    ),
    # düzey 2
    '0030': patch(
        "Bir işletme dönem içinde stoklarını satmış ve ayrıca dönem sonunda bazı stoklarını NGD'ye indirmiştir. TMS 2'ye göre stok değer düşüklüğü tutarı hangi dönemde gider olarak tanınır?",
        {
            'A': 'Denetim tamamlandığında',
            'B': 'Değer düşüklüğünün olduğu dönemde',
            'C': 'Değer düşüklüğü iptal edildiğinde',
            'D': 'Stoklar satıldığında',
            'E': 'Gelecek yılda',
        },
        'B',
        "TMS 2 p. 34'e göre stokların NGD'ye indirilme tutarı ve stoklardaki bütün kayıplar, **indirim veya kaybın olduğu dönemde** gider olarak tanınır; satılan stokların defter değeri ilgili hasılatın tanındığı dönemde gider yazılır.",
        'TMS 2 p. 34',
    ),
    # düzey 3
    '0031': patch(
        "Bir işletmenin dönem sonu stoklarının maliyeti 240.000 ₺, NGD'si 205.000 ₺'dir; önceden ayrılmış karşılık yoktur. Dönem sonunda tanınacak stok değer düşüklüğü gideri kaç ₺'dir?",
        {
            'A': '205.000',
            'B': '445.000',
            'C': '240.000',
            'D': '0',
            'E': '35.000',
        },
        'E',
        "TMS 2 p. 9'a göre stoklar maliyet ile NGD'nin düşüğüyle ölçülür; p. 34'e göre NGD'ye indirim tutarı indirimin olduğu dönemde gider yazılır: 240.000 − 205.000 = **35.000 ₺**.",
        'TMS 2 p. 9, 34',
    ),
    # düzey 2
    '0032': patch(
        "Bir işletme, stoklarının NGD'si ile gerçeğe uygun değeri arasındaki farkı değerlendirmektedir. TMS 2'ye göre bu iki kavram arasındaki temel fark hangisidir?",
        {
            'A': "NGD'nin işletmeye özgü olması",
            'B': "NGD'nin piyasa katılımcısı bakışı olması",
            'C': "GUD'nin işletmeye özgü olması",
            'D': 'İki kavramın eşit kabul edilmesi',
            'E': "NGD'nin vergi esaslı olması",
        },
        'A',
        "TMS 2 p. 7'ye göre NGD, işletmenin stokların olağan faaliyet akışı içinde satışından elde etmeyi beklediği net tutardır ve **işletmeye özgüdür**; gerçeğe uygun değer ise piyasa katılımcıları arasındaki işlemi yansıtır, bu nedenle ikisi farklı olabilir.",
        'TMS 2 p. 7',
    ),
    # düzey 3
    '0033': patch(
        "Bir tarım işletmesi kendi bahçesinden hasat ettiği elmaları depoya almıştır. Hasat noktasında elmaların gerçeğe uygun değeri 100.000 ₺, satış maliyetleri 5.000 ₺'dir. Elmaların TMS 2'ye göre stok maliyeti kaç ₺'dir?",
        {
            'A': '95.000',
            'B': '100.000',
            'C': '105.000',
            'D': '0',
            'E': '5.000',
        },
        'A',
        "TMS 2 p. 20'ye göre işletmenin biyolojik varlıklarından hasat ettiği tarımsal ürünler, TMS 41 uyarınca **hasat noktasındaki satış maliyetleri düşülmüş gerçeğe uygun değerle** ölçülür ve bu tutar TMS 2'nin uygulanmasında stok maliyeti sayılır: **95.000 ₺**.",
        'TMS 2 p. 20; TMS 41 p. 13',
    ),
    # düzey 2
    '0034': patch(
        'Bir işletme yurt içinden ticari mal satın almıştır. Aşağıdaki kalemlerden hangisi stokların satın alma maliyetine eklenmez?',
        {
            'A': 'Taşıma sigortası',
            'B': 'Geri alınamayan vergiler',
            'C': 'İndirilebilecek KDV',
            'D': 'Nakliye bedeli',
            'E': 'Yükleme ve boşaltma giderleri',
        },
        'C',
        "TMS 2 p. 11'e göre satın alma maliyeti alış fiyatı, **vergi idaresinden geri alınamayan** vergiler, nakliye, yükleme-boşaltma ve doğrudan ilişkili diğer maliyetlerden oluşur. **İndirim yoluyla geri alınabilecek KDV** maliyete eklenmez.",
        'TMS 2 p. 11',
    ),
    # düzey 3
    '0035': patch(
        "Bir işletmenin dönem başı stoku 1.000 birim × 10 ₺'dir. Dönemde önce 2.000 birim 10 ₺'den, sonra 1.000 birim 12 ₺'den alış yapılmış; 2.500 birim satılmıştır. FIFO yöntemine göre satışların maliyeti kaç ₺'dir?",
        {
            'A': '26.250',
            'B': '30.000',
            'C': '17.000',
            'D': '25.000',
            'E': '42.000',
        },
        'D',
        "Satılabilir mallar maliyeti 42.000 ₺, FIFO'ya göre dönem sonu stok 17.000 ₺'dir. Satışların maliyeti 42.000 − 17.000 = **25.000 ₺**; ilk giren birimler satılmış sayılır.",
        'TMS 2 p. 25-27',
    ),
    # düzey 3
    '0036': patch(
        "Bir ticari işletmenin dönem başı stoku 150.000 ₺, dönem içi alışları 900.000 ₺'dir. Dönem sonu stokların maliyeti 180.000 ₺, NGD'si 150.000 ₺'dir; önceki karşılık yoktur. Dönemde gider olarak tanınan toplam stok tutarı kaç ₺'dir?",
        {
            'A': '840.000',
            'B': '900.000',
            'C': '870.000',
            'D': '1.050.000',
            'E': '30.000',
        },
        'B',
        "TMS 2 p. 34'e göre satılan stokların defter değeri ve NGD'ye indirim tutarı dönemin gideridir: satışların maliyeti 870.000 ₺ + değer düşüklüğü 30.000 ₺ = **900.000 ₺**; p. 36(d) bu tutarın açıklanmasını ister.",
        'TMS 2 p. 34, 36(d)',
    ),
    # düzey 2
    '0037': patch(
        "Bir işletmenin dönemdeki üretim maliyetleri: direkt malzeme 150.000 ₺, direkt işçilik 60.000 ₺, stoklara dağıtılan genel üretim giderleri 40.000 ₺'dir. TMS 2'ye göre dönüştürme maliyetleri kaç ₺'dir?",
        {
            'A': '60.000',
            'B': '40.000',
            'C': '100.000',
            'D': '210.000',
            'E': '250.000',
        },
        'C',
        "TMS 2 p. 12'ye göre dönüştürme maliyetleri, **direkt işçilik** gibi üretimle doğrudan ilgili maliyetler ile sistematik olarak dağıtılan **sabit ve değişken genel üretim giderlerinden** oluşur: 60.000 + 40.000 = **100.000 ₺**; direkt malzeme satın alma maliyetidir.",
        'TMS 2 p. 12',
    ),
    # düzey 2
    '0038': patch(
        "Bir sanat galerisinin elinde maliyetleri sırasıyla 40.000 ₺, 55.000 ₺ ve 70.000 ₺ olan, her biri benzersiz üç tablo vardır. Dönemde 55.000 ₺ ve 70.000 ₺ maliyetli tablolar satılmıştır. Satışların maliyeti kaç ₺'dir?",
        {
            'A': '95.000',
            'B': '70.000',
            'C': '165.000',
            'D': '125.000',
            'E': '110.000',
        },
        'D',
        "Birbirinin yerine geçemeyen kalemlerde TMS 2 p. 23'e göre **özel tanımlama** kullanılır; satılan tabloların gerçek maliyetleri gider yazılır: 55.000 + 70.000 = **125.000 ₺**.",
        'TMS 2 p. 23-24',
    ),
    # düzey 3
    '0039': patch(
        "Aşağıdakilerden hangileri TMS 2'ye göre doğrudur?\n\nI. Düşük üretim döneminde birim başına dağıtılan sabit GÜG artırılır\n\nII. LIFO yöntemi kullanılamaz\n\nIII. Stoklar NGD'ye genellikle kalem bazında indirilir",
        {
            'A': 'I ve II',
            'B': 'Yalnız II',
            'C': 'I, II ve III',
            'D': 'Yalnız III',
            'E': 'II ve III',
        },
        'E',
        "TMS 2 p. 25'e göre LIFO kullanılamaz (II); p. 29'a göre NGD'ye indirim genellikle kalem bazında yapılır (III). p. 13'e göre düşük üretimde birim başına sabit GÜG **artırılmaz**, dağıtılmayan kısım gider yazılır (I yanlış).",
        'TMS 2 p. 13, 25, 29',
    ),
    # düzey 2
    '0040': patch(
        'Aşağıdakilerden hangileri doğrudur?\n\nI. Anormal fireler stok maliyetine dâhil edilir\n\nII. Birbirinin yerine geçemeyen stoklarda özel tanımlama uygulanır\n\nIII. Genel yönetim giderleri stok maliyetine dâhil edilir',
        {
            'A': 'Yalnız II',
            'B': 'I, II ve III',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'Yalnız I',
        },
        'A',
        "TMS 2 p. 23'e göre birbirinin yerine geçemeyen stoklarda özel tanımlama uygulanır (II). p. 16'ya göre anormal fireler (I) ve genel yönetim giderleri (III) **stok maliyetine dâhil edilmez**.",
        'TMS 2 p. 16, 19, 23',
    ),
    # düzey 3
    '0041': patch(
        "Bir işletme yurt dışından ticari mal ithal etmiştir. Faturadaki alış bedeli 400.000 ₺, satıcının verdiği ticari iskonto 20.000 ₺, ödenen gümrük vergisi 16.000 ₺, işletmenin deposuna kadar nakliye 9.000 ₺, yolda sigorta 3.000 ₺ ve sonradan indirim konusu yapılacak KDV 80.000 ₺'dir. Stokların satın alma maliyeti kaç ₺'dir?",
        {
            'A': '392.000',
            'B': '380.000',
            'C': '388.000',
            'D': '408.000',
            'E': '328.000',
        },
        'D',
        "TMS 2 p. 11'e göre satın alma maliyeti; alış fiyatı, ithalat vergileri ve **vergi idaresinden geri alınamayan** diğer vergiler, nakliye ve doğrudan ilişkili diğer maliyetlerden oluşur; **ticari iskontolar düşülür**. İndirilecek KDV maliyete girmez: 400.000 − 20.000 + 16.000 + 9.000 + 3.000 = **408.000 ₺**.",
        'TMS 2 p. 11',
    ),
    # düzey 3
    '0042': patch(
        "Normal kapasitesi 10.000 adet olan bir işletme olağandışı yüksek talep nedeniyle dönemde 12.500 adet üretmiştir; sabit GÜG 200.000 ₺'dir. Mamullere birim başına dağıtılacak sabit GÜG kaç ₺'dir?",
        {
            'A': '9',
            'B': '0',
            'C': '16',
            'D': '4',
            'E': '20',
        },
        'C',
        "TMS 2 p. 13'e göre olağandışı yüksek üretim dönemlerinde birim başına dağıtılan sabit genel üretim gideri, stokların maliyetin üstünde ölçülmemesi için **azaltılır**: 200.000 / 12.500 = **16 ₺**.",
        'TMS 2 p. 13',
    ),
    # düzey 2
    '0043': patch(
        "Bir işletme peşin fiyatı 500.000 ₺ olan ticari malları normal kredi koşullarını aşan bir vadeyle 560.000 ₺'ye satın almıştır. Stokların maliyeti kaç ₺'dir?",
        {
            'A': '560.000',
            'B': '530.000',
            'C': '620.000',
            'D': '60.000',
            'E': '500.000',
        },
        'E',
        "TMS 2 p. 18'e göre stoklar vadeli alındığında ve anlaşma bir finansman unsuru içeriyorsa, normal kredi koşullarıyla ödenecek bedel ile ödenen tutar arasındaki fark **finansman süresi boyunca faiz gideri** olarak tanınır: stok maliyeti **500.000 ₺**.",
        'TMS 2 p. 18',
    ),
    # düzey 2
    '0044': patch(
        "Bir mimarlık firması, müşterisi için yürüttüğü ve henüz hasılat tanınmamış bir projede çalışan mimarların ücretleri ile doğrudan malzeme maliyetlerini izlemektedir. TMS 2'ye göre hizmet işletmesinin stok maliyetine hangi maliyetler dâhil edilmez?",
        {
            'A': 'Projedeki mimarların ücretleri',
            'B': 'Doğrudan personel giderleri',
            'C': 'Genel yönetim personelinin ücretleri',
            'D': 'Doğrudan ilişkili genel giderler',
            'E': 'Doğrudan malzemeler',
        },
        'C',
        "TMS 2 p. 19'a göre hizmet sunucusunun stok maliyeti; hizmeti doğrudan sunan personelin işçilik ve diğer maliyetleri ile ilişkili genel giderlerden oluşur; **satış ve genel yönetim personelinin maliyetleri dâhil edilmez**. (Bu tür maliyetler TFRS 15 kapsamındaki sözleşmelerde farklı değerlendirilebilir.)",
        'TMS 2 p. 19',
    ),
    # düzey 2
    '0045': patch(
        "TMS 2'ye göre stok maliyet yöntemleriyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Vergi avantajı sağlıyorsa LIFO yöntemi kullanılabilir',
            'B': 'İlk giren ilk çıkar (FIFO) yöntemi kullanılabilir',
            'C': 'Ağırlıklı ortalama maliyet yöntemi kullanılabilir',
            'D': 'Birbirinin yerine kullanılamayan kalemlerde özel tanımlama uygulanır',
            'E': 'Benzer nitelik ve kullanımdaki stoklarda aynı yöntem kullanılır',
        },
        'A',
        "TMS 2.23-25: birbirinin yerine kullanılamayan kalemlerde maliyetler özel tanımlama yöntemiyle; diğerlerinde FIFO veya ağırlıklı ortalama maliyet yöntemiyle belirlenir ve benzer nitelik ve kullanımdaki stoklar için aynı yöntem kullanılır. LIFO yöntemine TMS 2'de izin verilmez.",
        'TMS 2 p. 25',
    ),
    # düzey 3
    '0046': patch(
        "Bir gıda şirketinin stoklarında henüz paketlenmemiş 2.000 kg kahve vardır. Kahvenin maliyeti 145 ₺/kg, paketlenmiş hâldeki tahmini satış fiyatı 160 ₺/kg, paketleme (tamamlanma) maliyeti 12 ₺/kg ve tahmini satış maliyeti 8 ₺/kg'dır. Kahve finansal tablolarda kaç ₺ ile gösterilir?",
        {
            'A': '320.000',
            'B': '296.000',
            'C': '280.000',
            'D': '304.000',
            'E': '290.000',
        },
        'C',
        "TMS 2 p. 6'ya göre NGD, tahmini satış fiyatından **tahmini tamamlanma maliyeti ve satış için gerekli tahmini maliyetler** düşülerek bulunur: 160 − 12 − 8 = 140 ₺/kg. p. 9'a göre maliyet (145) ile NGD'nin düşük olanı alınır: 2.000 × 140 = **280.000 ₺**.",
        'TMS 2 p. 6, 9',
    ),
    # düzey 3
    '0047': patch(
        "Bir üretim işletmesinin elinde maliyeti 90.000 ₺ olan hammadde vardır; hammaddenin piyasa fiyatı düşmüş ve yenileme maliyeti 70.000 ₺'ye inmiştir. Bu hammaddenin kullanılacağı mamullerin tahmini maliyeti 300.000 ₺, tahmini NGD'si 320.000 ₺'dir. Hammadde finansal tablolarda kaç ₺ ile gösterilir?",
        {
            'A': '80.000',
            'B': '110.000',
            'C': '70.000',
            'D': '20.000',
            'E': '90.000',
        },
        'E',
        "TMS 2 p. 32'ye göre üretimde kullanılacak hammaddeler, dâhil olacakları mamullerin **maliyet veya maliyetin üzerinde satılması bekleniyorsa** maliyetin altına indirilmez. Mamullerin NGD'si maliyetini aştığından hammadde maliyetle, **90.000 ₺** ile gösterilir.",
        'TMS 2 p. 32',
    ),
    # düzey 3
    '0048': patch(
        "Bir işletmenin elindeki 1.000 birim ürünün birim maliyeti 48 ₺'dir. Bunların 600 birimi için birim fiyatı 52 ₺ olan kesin satış sözleşmesi vardır; kalan birimlerin piyasa satış fiyatı 44 ₺'ye düşmüştür. Satış maliyeti yoktur. Stoklar kaç ₺ ile gösterilir?",
        {
            'A': '43.200',
            'B': '44.800',
            'C': '46.400',
            'D': '44.000',
            'E': '45.600',
        },
        'C',
        "TMS 2 p. 31'e göre sözleşmeli kısım sözleşme fiyatıyla, fazla kısım genel satış fiyatıyla değerlendirilir: 600 × 48 + 400 × 44 = **46.400 ₺**.",
        'TMS 2 p. 31',
    ),
    # düzey 2
    '0049': patch(
        "Bir işletmenin stoklarındaki bir kısım ürün, depodaki nem nedeniyle hasar görmüş ve satış fiyatları düşmüştür. TMS 2'ye göre bu stokların maliyetinin geri kazanılamaması durumunda ne yapılır?",
        {
            'A': 'Maliyetle bırakılır',
            'B': 'Özkaynaktan düşülür',
            'C': 'Dipnotla yetinilir',
            'D': "NGD'ye indirilir",
            'E': 'Yeniden değerlenir',
        },
        'D',
        "TMS 2 p. 28'e göre stoklar hasar görmüşse, tamamen veya kısmen eskimişse ya da satış fiyatları düşmüşse maliyetleri geri kazanılamayabilir; stoklar **net gerçekleşebilir değerine indirilir**, çünkü varlıklar satış veya kullanımla gerçekleşmesi beklenen tutarın üzerinde taşınmamalıdır.",
        'TMS 2 p. 28',
    ),
    # düzey 2
    '0050': patch(
        'Bir işletme ürettiği stokların bir kısmını kendi kullanımı için maddi duran varlık yapımında kullanmıştır. Bu stokların maliyeti hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Genel yönetim giderine eklenir',
            'B': 'Satışların maliyetine eklenir',
            'C': 'Diğer kapsamlı gelire alınır',
            'D': 'Özkaynaktan düşülür',
            'E': 'Maddi duran varlığın maliyetine eklenir',
        },
        'E',
        "TMS 2 p. 35'e göre bazı stoklar başka varlık hesaplarına, örneğin **kendi imal ettiği maddi duran varlığın bileşeni** olarak kullanılabilir; bu şekilde kullanılan stoklar o varlığın yararlı ömrü boyunca gider olarak tanınır.",
        'TMS 2 p. 35',
    ),
    # düzey 3
    '0051': patch(
        "Bir işletme TMS 2 kapsamında stoklarına ilişkin açıklamalarını hazırlamaktadır. Aşağıdakilerden hangisinin açıklanması TMS 2'de istenmez?",
        {
            'A': 'Kullanılan maliyet formülleri',
            'B': 'Stokların toplam defter değeri',
            'C': 'Stok alışlarının yapıldığı tedarikçilerin adları',
            'D': 'Dönemde gider yazılan stok tutarı',
            'E': 'Borçlara teminat olarak rehnedilen stokların defter değeri',
        },
        'C',
        "TMS 2 p. 36'ya göre işletme; kullanılan maliyet formülleri dâhil muhasebe politikalarını, stokların toplam defter değerini ve sınıflandırmasını, dönemde gider yazılan stok tutarını, değer düşüklükleri ve iptallerini ve **teminat olarak rehnedilen stokların** defter değerini açıklar. Tedarikçi adları istenmez.",
        'TMS 2 p. 36',
    ),
    # düzey 3
    '0052': patch(
        "Bir rafineri bir üretim sürecinde ana ürünle birlikte önemsiz tutarda bir yan ürün elde etmiştir. Sürecin toplam üretim maliyeti 500.000 ₺, yan ürünün net gerçekleşebilir değeri 30.000 ₺'dir. Ana ürünün maliyeti kaç ₺'dir?",
        {
            'A': '500.000',
            'B': '30.000',
            'C': '470.000',
            'D': '530.000',
            'E': '250.000',
        },
        'C',
        "TMS 2 p. 14'e göre önemsiz yan ürünler çoğunlukla **net gerçekleşebilir değerleriyle** ölçülür ve bu değer **ana ürünün maliyetinden düşülür**: 500.000 − 30.000 = **470.000 ₺**.",
        'TMS 2 p. 14',
    ),
    # düzey 2
    '0053': patch(
        "Bir işletme sabit genel üretim giderlerini dağıtmak için normal kapasiteyi belirlemektedir.\n\nTMS 2'ye göre bu konuyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Normal kapasite, tesisin teorik azami üretim düzeyidir',
            'B': 'Planlı bakımdan doğan kapasite kayıpları dikkate alınır',
            'C': 'Fiilî üretim normal kapasiteye yakınsa fiilî düzey kullanılabilir',
            'D': 'Düşük üretim nedeniyle dağıtılamayan sabit GÜG gider yazılır',
            'E': 'Olağandışı yüksek üretimde birim başına sabit GÜG azaltılır',
        },
        'A',
        'TMS 2.13: normal kapasite, planlı bakımdan kaynaklanan kapasite kayıpları dikkate alınarak birkaç dönem veya mevsim boyunca normal koşullarda ulaşılması beklenen ortalama üretimdir; teorik azami düzey değildir. Fiilî üretim normal kapasiteye yakınsa fiilî düzey kullanılabilir; dağıtılamayan sabit GÜG gider yazılır, olağandışı yüksek üretimde birim başına tutar azaltılır.',
        'TMS 2 p. 13',
    ),
    # düzey 3
    '0054': patch(
        "Bir işletmenin elinde birim maliyeti 50 ₺ olan 1.000 adet yarı mamul vardır. Yarı mamullerin tamamlanması için birim başına 20 ₺ daha harcanacak; mamul birim 75 ₺'ye satılacak ve birim başına 8 ₺ satış gideri katlanılacaktır. Yarı mamuller finansal tablolarda kaç ₺ ile gösterilir?",
        {
            'A': '55.000',
            'B': '50.000',
            'C': '67.000',
            'D': '47.000',
            'E': '75.000',
        },
        'D',
        "Yarı mamulün NGD'si: 75 − 20 (tamamlanma) − 8 (satış) = 47 ₺. Maliyet 50 ₺ olduğundan düşük olan alınır: 1.000 × 47 = **47.000 ₺**.",
        'TMS 2 p. 6',
    ),
    # düzey 3
    '0055': patch(
        "Bir işletme geçen yıl maliyeti 100.000 ₺ olan stoklar için 20.000 ₺ değer düşüklüğü ayırmıştır. Bu yıl sonunda aynı stoklar elde olup piyasa koşullarının iyileşmesiyle NGD 130.000 ₺'ye yükselmiştir. İptal edilecek karşılık kaç ₺'dir?",
        {
            'A': '20.000',
            'B': '0',
            'C': '130.000',
            'D': '30.000',
            'E': '50.000',
        },
        'A',
        "TMS 2 p. 33'e göre iptal **önceki değer düşüklüğü tutarıyla sınırlıdır**; yeni defter değeri maliyet ile NGD'nin düşüğüdür. Stoklar maliyete (100.000 ₺) kadar yükseltilebilir: iptal **20.000 ₺**.",
        'TMS 2 p. 33',
    ),
    # düzey 2
    '0056': patch(
        'Bir inşaat şirketinin elindeki varlıklar şunlardır: satmak için inşa ettiği konutlar, satış amacıyla elde tuttuğu arsalar, inşaatlarda kullanacağı çimento, kendi merkez ofisi olarak kullandığı bina ve satılmak üzere yapımı süren villalar. Bunlardan hangisi stok değildir?',
        {
            'A': 'Satış amaçlı arsalar',
            'B': 'Merkez ofis binası',
            'C': 'Yapımı süren villalar',
            'D': 'Çimento',
            'E': 'Satmak için inşa edilen konutlar',
        },
        'B',
        "TMS 2 p. 6'ya göre stoklar, olağan faaliyet akışında satış amacıyla elde tutulan, satış amacıyla üretim sürecinde bulunan veya üretimde kullanılacak varlıklardır. İşletmenin **kendi kullanımındaki bina** TMS 16 kapsamında maddi duran varlıktır.",
        'TMS 2 p. 6; TMS 16',
    ),
    # düzey 3
    '0057': patch(
        "Bir tekstil işletmesi NGD'ye indirim yaparken stoklarını gruplamak istemektedir. TMS 2'ye göre aşağıdakilerden hangisi uygun bir gruplama olabilir?",
        {
            'A': 'Bütün mamuller',
            'B': 'Aynı ürün hattına ait benzer kalemler',
            'C': 'İşletmenin toplam stokları',
            'D': 'Bir faaliyet bölümündeki bütün stoklar',
            'E': 'Bütün hazır giyim ürünleri',
        },
        'B',
        "TMS 2 p. 29'a göre stoklar genellikle kalem bazında indirilir; ancak **aynı ürün hattına ait, benzer amaç veya kullanımı olan, aynı coğrafi bölgede üretilip pazarlanan ve ayrı değerlemesi pratik olmayan** kalemler gruplanabilir. Mamuller veya bir sektörün bütün stokları gibi sınıflandırmalar temelinde indirim uygun değildir.",
        'TMS 2 p. 29',
    ),
    # düzey 2
    '0058': patch(
        "Bir işletme bu yıl, geçen yıl ayırdığı stok değer düşüklüğünün bir kısmını ürün fiyatlarının yükselmesi nedeniyle iptal etmiştir. TMS 2'ye göre bu iptale ilişkin olarak hangi bilgi açıklanır?",
        {
            'A': 'İptale yol açan koşullar',
            'B': 'Gelecek yıl fiyat tahmini',
            'C': 'Vergi idaresinin görüşü',
            'D': 'İptali onaylayan yöneticinin adı',
            'E': 'Rakiplerin stok değerleri',
        },
        'A',
        "TMS 2 p. 36(f)-(g)'ye göre işletme dönemde gider olarak tanınan tutardaki azalış olarak muhasebeleştirilen **değer düşüklüğü iptalinin tutarını** ve **iptale yol açan olay ve koşulları** açıklar.",
        'TMS 2 p. 36(f)-(g)',
    ),
    # düzey 2
    '0059': patch(
        'Net gerçekleşebilir değere ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Tahmini satış fiyatından tamamlanma ve satış maliyetleri düşülür\n\nII. Kesin satış sözleşmesi kapsamındaki stoklarda sözleşme fiyatı esas alınır\n\nIII. Mamuller maliyetin üzerinde satılacaksa hammaddeler maliyetin altına indirilmez',
        {
            'A': 'Yalnız I',
            'B': 'I, II ve III',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'I ve II',
        },
        'B',
        "TMS 2 p. 6'ya göre NGD tanımı (I), p. 31'e göre sözleşme fiyatı (II) ve p. 32'ye göre hammaddelerin maliyetin altına indirilmemesi (III) doğrudur.",
        'TMS 2 p. 6, 31-32',
    ),
    # düzey 3
    '0060': patch(
        "Aşağıdakilerden hangileri TMS 2'ye göre doğrudur?\n\nI. Hasat noktasındaki tarımsal ürünler TMS 2 kapsamındadır\n\nII. Perakende yönteminde maliyet satış fiyatından brüt kâr marjı düşülerek bulunur\n\nIII. Standart maliyet sonuçları fiilî maliyete yakınsa kullanılabilir",
        {
            'A': 'Yalnız III',
            'B': 'I ve II',
            'C': 'Yalnız II',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'D',
        "TMS 2 p. 22'ye göre perakende yöntemi (II) ve p. 21'e göre standart maliyet (III) doğrudur. Hasat noktasındaki tarımsal ürünler **TMS 41** kapsamındadır; TMS 2 hasattan sonra uygulanır (I yanlış).",
        'TMS 2 p. 2-3, 21-22',
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
    print(f"1 paket / {len(PATCHES)} soru ('TMS 2 Stoklar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
