#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TFRS 9 Finansal Araclar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gercek sinav profiliyle yeniden yazim (senaryo kok + kisa olcum sinifi/tutar sik). Eski surum tanim agirlikliydi ve 94 mutlak ifadeli celdirici tasiyordu (kor %43). Kapsam: TMS 32 finansal varlik/yukumluluk tanimlari, ilk olcum ve islem maliyetleri, is modeli + SPPI ile siniflandirma, GUD opsiyonu, ozkaynak araclarinda DKG tercihi, etkin faiz ve itfa edilmis maliyet, GUDDKG borclanma araclarinda yeniden siniflandirma, kendi kredi riski, yeniden siniflandirma tarihi, BKZ (uc asama, 30/90 gun karineleri, karsilik matrisi, 3. asama faiz), tablo disi birakma (faktoring, %10 testi), riskten korunma turleri ve etkin kisim. 21 hesap sorusu modulde hesaplandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: TFRS 9 Finansal Araclar ve TMS 32 Finansal Araclar: Sunum (KGK); TFRS 7, TMS 21 ilgili paragraflar
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/tfrs_9_finansal_arac.json"
STYLE_REF = 'SGS Muhasebe Standartlari (gercek sinav profiline kalibre: senaryo kok + kisa sik)'
ONEK = "std-tfrs9-gen-"


def patch(stem, options, answer, solution, ref='TFRS 9 Finansal Araclar'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Bir işletmenin finansal durum tablosunda şu kalemler vardır: bankadaki vadesiz mevduat, müşterilerden ticari alacaklar, başka bir şirketin hisse senetleri, peşin ödenmiş sigorta gideri ve bir müşteriye verilen kredi. TMS 32'ye göre bunlardan hangisi finansal varlık değildir?",
        {
            'A': 'Verilen kredi',
            'B': 'Hisse senetleri',
            'C': 'Peşin ödenmiş sigorta gideri',
            'D': 'Ticari alacaklar',
            'E': 'Vadesiz mevduat',
        },
        'C',
        "TMS 32 p. 11 ve UR 11'e göre finansal varlık nakit, başka bir işletmenin özkaynak aracı veya **nakit ya da başka bir finansal varlık alma hakkıdır**. Peşin ödenmiş giderlerde gelecekte nakit değil **mal veya hizmet** alınacağından finansal varlık değildir.",
        'TMS 32 p. 11, UR 7-11',
    ),
    # düzey 2
    '0002': patch(
        "Bir işletme vadesi 60 gün olan ve önemli bir finansman bileşeni içermeyen ticari alacaklarını ilk kez muhasebeleştirmektedir. TFRS 9'a göre bu alacaklar ilk muhasebeleştirmede hangi tutarla ölçülür?",
        {
            'A': 'İşlem bedeli',
            'B': 'Nominal faiz eklenmiş tutar',
            'C': 'Net gerçekleşebilir değer',
            'D': 'Bugünkü değer',
            'E': 'Tahsil edilebilir tutar',
        },
        'A',
        "TFRS 9 p. 5.1.3'e göre TFRS 15 kapsamında **önemli bir finansman bileşeni içermeyen ticari alacaklar**, ilk muhasebeleştirmede TFRS 15'te tanımlanan **işlem bedeliyle** ölçülür.",
        'TFRS 9 p. 5.1.3',
    ),
    # düzey 3
    '0003': patch(
        'Bir sigorta şirketi, tahvil portföyünü hem kupon faizlerini tahsil etmek hem de likidite ihtiyacına ve fiyat fırsatlarına göre satmak amacıyla yönetmektedir; tahviller SPPI ölçütünü sağlamaktadır. Bu tahviller hangi ölçüm sınıfına girer?',
        {
            'A': "GUD farkı DKG'ye yansıtılan",
            'B': 'Maliyet yöntemi',
            'C': 'İtfa edilmiş maliyet',
            'D': 'GUD farkı kâr veya zarara yansıtılan',
            'E': 'Özkaynak yöntemi',
        },
        'A',
        "TFRS 9 p. 4.1.2A'ya göre iş modelinin amacı **hem sözleşmeye bağlı nakit akışlarını tahsil etmek hem de finansal varlıkları satmak** ise ve SPPI ölçütü sağlanıyorsa varlık gerçeğe uygun değer farkı diğer kapsamlı gelire yansıtılarak ölçülür.",
        'TFRS 9 p. 4.1.2A',
    ),
    # düzey 2
    '0004': patch(
        'Bir işletme, ticari amaçla elde tutmadığı ve uzun vadeli stratejik yatırım olarak aldığı bir şirketin hisselerini ilk muhasebeleştirmede, gerçeğe uygun değer değişimlerini diğer kapsamlı gelirde sunmak üzere tanımlamıştır. Bu tercih hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Satışta kâr veya zarara aktarılır',
            'B': 'Her yıl yenilenir',
            'C': 'Geri dönülemez',
            'D': 'Değer düşüklüğü gerektirir',
            'E': 'Borçlanma araçlarına özgüdür',
        },
        'C',
        "TFRS 9 p. 5.7.5'e göre ticari amaçla elde tutulmayan özkaynak araçları için GUD değişimlerinin DKG'de sunulması tercihi ilk muhasebeleştirmede yapılır ve **geri dönülemez**; birikmiş tutarlar sonradan kâr veya zarara aktarılmaz.",
        'TFRS 9 p. 4.1.4, 5.7.5',
    ),
    # düzey 3
    '0005': patch(
        "Bir işletme 1 Ocak 2025'te nominal değeri 1.000.000 ₺, yıllık kupon faizi %8 olan 3 yıl vadeli bir tahvili 950.000 ₺'ye almış ve itfa edilmiş maliyetle ölçmektedir. Etkin faiz oranı %10 olarak hesaplanmıştır. İşletmenin 2025 yılında kâr veya zarara yansıtacağı faiz geliri kaç ₺'dir?",
        {
            'A': '80.000',
            'B': '76.000',
            'C': '100.000',
            'D': '15.000',
            'E': '95.000',
        },
        'E',
        "TFRS 9 p. 5.4.1'e göre faiz geliri **etkin faiz yöntemiyle**, brüt defter değeri üzerinden hesaplanır: 950.000 × %10 = **95.000 ₺**. Tahsil edilen kupon 80.000 ₺'dir; aradaki fark iskontonun itfasıdır.",
        'TFRS 9 p. 5.4.1',
    ),
    # düzey 3
    '0006': patch(
        "Bir işletme ticari amaçla elde tutmadığı hisseleri 300.000 ₺'ye almış, 3.000 ₺ komisyon ödemiş ve GUD değişimlerini DKG'de sunmayı geri dönülemez şekilde seçmiştir. Yıl sonunda hisselerin gerçeğe uygun değeri 340.000 ₺'dir. Yıl sonunda diğer kapsamlı gelire yansıtılacak tutar kaç ₺'dir?",
        {
            'A': '340.000',
            'B': '3.000',
            'C': '37.000',
            'D': '34.000',
            'E': '31.000',
        },
        'C',
        "GUDKZ dışındaki bu varlıkta komisyon ilk ölçüme eklenir: 300.000 + 3.000 = 303.000 ₺. Yıl sonu değer artışı DKG'ye yansır: 340.000 − 303.000 = **37.000 ₺**.",
        'TFRS 9 p. 5.1.1, 5.7.5',
    ),
    # düzey 3
    '0007': patch(
        'Bir işletme, GUDDKG olarak ölçtüğü ve özkaynakta 30.000 ₺ birikmiş kazancı bulunan bir tahvili satmıştır. Birikmiş kazanç hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sermayeye eklenir',
            'B': 'Yasal yedeklere aktarılır',
            'C': 'Geçmiş yıllar kârlarına aktarılır',
            'D': 'Kâr veya zarara aktarılır',
            'E': "DKG'de kalır",
        },
        'D',
        "TFRS 9 p. 5.7.10'a göre GUDDKG **borçlanma araçlarında** varlık finansal tablo dışı bırakıldığında DKG'de birikmiş kazanç veya kayıp **yeniden sınıflandırma düzeltmesi** olarak özkaynaktan kâr veya zarara aktarılır. Özkaynak araçlarındaki tercihten farkı budur.",
        'TFRS 9 p. 5.7.10',
    ),
    # düzey 3
    '0008': patch(
        "Bir banka, 15 Mart 2026'da tüketici kredileri iş modelini 'tahsil' modelinden 'tahsil ve satış' modeline değiştirmiştir; hesap dönemi takvim yılıdır ve ara dönem raporlaması üçer aylıktır. Krediler hangi tarihten itibaren yeni sınıfta ölçülür?",
        {
            'A': '31 Aralık 2026',
            'B': '1 Ocak 2026',
            'C': '15 Mart 2026',
            'D': '1 Ocak 2027',
            'E': '1 Nisan 2026',
        },
        'E',
        "TFRS 9 p. 4.4.1 ve 5.6.1'e göre finansal varlıklar **yalnızca iş modeli değiştiğinde** yeniden sınıflandırılır ve bu **ileriye dönük** olarak **yeniden sınıflandırma tarihinden**, yani iş modeli değişikliğini izleyen ilk raporlama döneminin ilk gününden itibaren uygulanır.",
        'TFRS 9 p. 4.4.1, 5.6.1',
    ),
    # düzey 3
    '0009': patch(
        "Önemli finansman bileşeni içermeyen ticari alacaklar için karşılık matrisi kullanan bir işletmenin yıl sonu alacakları şöyledir: vadesi geçmemiş 1.200.000 ₺ (%1), 1-90 gün gecikmiş 500.000 ₺ (%5), 90 günü aşan 300.000 ₺ (%30). Dönem başı zarar karşılığı 100.000 ₺'dir. Dönemin değer düşüklüğü gideri kaç ₺'dir?",
        {
            'A': '227.000',
            'B': '100.000',
            'C': '27.000',
            'D': '90.000',
            'E': '127.000',
        },
        'C',
        "TFRS 9 p. 5.5.15'e göre bu alacaklarda **basitleştirilmiş yaklaşım** (her zaman ömür boyu BKZ) uygulanır; karşılık matrisiyle gerekli karşılık 12.000 + 25.000 + 90.000 = 127.000 ₺'dir. Dönem gideri: 127.000 − 100.000 = **27.000 ₺**.",
        'TFRS 9 p. 5.5.15, UR B5.5.35',
    ),
    # düzey 3
    '0010': patch(
        'Bir işletme GUDDKG olarak ölçtüğü tahviller için 15.000 ₺ beklenen kredi zararı belirlemiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Değer düşüklüğü zararı kâr veya zarara yansır',
            'B': 'Tahvil gerçeğe uygun değeriyle gösterilir',
            'C': 'BKZ genel yaklaşıma göre ölçülür',
            'D': 'Karşılık tahvilin finansal durum tablosundaki defter değerini azaltır',
            'E': 'Karşılık diğer kapsamlı gelirde tanınır',
        },
        'D',
        "TFRS 9 p. 5.5.2'ye göre GUDDKG borçlanma araçlarında zarar karşılığı **diğer kapsamlı gelirde** tanınır ve **varlığın finansal durum tablosundaki defter değerini azaltmaz**; varlık gerçeğe uygun değerle gösterilir, değer düşüklüğü zararı ise kâr veya zarara yansır.",
        'TFRS 9 p. 5.5.2',
    ),
    # düzey 2
    '0011': patch(
        "Bir işletme beklenen kredi zararlarını ölçerken aşağıdaki bilgileri kullanmak istemektedir: geçmiş kayıp deneyimi, mevcut ekonomik koşullar, gelecekteki ekonomik koşullara ilişkin tahminler ve yalnızca tek bir en kötü senaryo. TFRS 9'a göre BKZ ölçümünde hangisi esas alınmaz?",
        {
            'A': 'Paranın zaman değeri',
            'B': 'Geçmiş kayıp deneyimi',
            'C': 'Geleceğe ilişkin tahminler',
            'D': 'Mevcut ekonomik koşullar',
            'E': 'Tek bir en kötü senaryo',
        },
        'E',
        "TFRS 9 p. 5.5.17'ye göre BKZ; olası sonuçların değerlendirilmesiyle belirlenen **tarafsız ve olasılıklarla ağırlıklandırılmış** tutarı, paranın zaman değerini ve geçmiş olaylar, mevcut koşullar ile gelecek ekonomik koşullara ilişkin makul ve desteklenebilir bilgileri yansıtır; tek bir en kötü senaryo esas alınmaz.",
        'TFRS 9 p. 5.5.17',
    ),
    # düzey 3
    '0012': patch(
        "Bir işletme bankayla kredi koşullarını yeniden müzakere etmiştir. Orijinal kredinin kalan nakit akışlarının orijinal etkin faiz oranıyla iskonto edilmiş değeri 1.000.000 ₺, yeni koşullardaki nakit akışlarının aynı oranla iskonto edilmiş değeri (ödenen ücretler dâhil) 870.000 ₺'dir. Bu değişiklik nasıl muhasebeleştirilir?",
        {
            'A': 'Eski borç söndürülür, yeni borç tanınır',
            'B': 'Borcun defter değeri korunur',
            'C': 'Fark gelecek yıllara yayılır',
            'D': 'Değişiklik dipnotla açıklanır',
            'E': 'Fark diğer kapsamlı gelire alınır',
        },
        'A',
        "TFRS 9 p. 3.3.2 ve UR B3.3.6'ya göre bugünkü değerler arasındaki fark en az %10 ise koşullar önemli ölçüde farklıdır. Fark (1.000.000 − 870.000) / 1.000.000 = %13 olduğundan **orijinal yükümlülük söndürülür ve yeni yükümlülük tanınır**.",
        'TFRS 9 p. 3.3.2, UR B3.3.6',
    ),
    # düzey 2
    '0013': patch(
        "Bir işletmenin tedarikçiye olan borcunun ödeme günü gelmiş ve işletme borcu tamamen ödemiştir. TFRS 9'a göre finansal yükümlülük hangi durumda finansal durum tablosundan çıkarılır?",
        {
            'A': 'Karşılık ayrıldığında',
            'B': 'Tedarikçi onayladığında',
            'C': 'Yükümlülük sona erdiğinde',
            'D': 'Vade yaklaştığında',
            'E': 'Ödeme planlandığında',
        },
        'C',
        "TFRS 9 p. 3.3.1'e göre finansal yükümlülük yalnızca **sona erdiğinde**, yani sözleşmede belirtilen yükümlülük yerine getirildiğinde, iptal edildiğinde veya zamanaşımına uğradığında finansal tablo dışı bırakılır.",
        'TFRS 9 p. 3.3.1',
    ),
    # düzey 3
    '0014': patch(
        "Bir işletme GUD değişimlerini DKG'de sunmayı seçtiği hisse senetlerinden 12.000 ₺ nakit temettü almıştır; temettü yatırımın maliyetinin geri kazanılması niteliğinde değildir. Temettü nerede muhasebeleştirilir?",
        {
            'A': 'Kâr veya zararda',
            'B': 'Pasif hesaplarda',
            'C': 'Yatırımın maliyetinden indirilerek',
            'D': 'Doğrudan özkaynakta',
            'E': 'Diğer kapsamlı gelirde',
        },
        'A',
        "TFRS 9 p. 5.7.6 ve UR B5.7.1'e göre bu tercihi yapılan özkaynak araçlarından elde edilen temettüler, açıkça yatırım maliyetinin geri kazanılmasını temsil etmedikçe **kâr veya zararda** muhasebeleştirilir.",
        'TFRS 9 p. 5.7.6',
    ),
    # düzey 2
    '0015': patch(
        'Bir işletme finansal tablolarının dipnotlarında finansal araçlarından kaynaklanan kredi riski, likidite riski ve piyasa riskinin niteliği ve boyutu hakkında bilgi vermektedir. Bu açıklamalar hangi standartta düzenlenmiştir?',
        {
            'A': 'TFRS 13',
            'B': 'TFRS 9',
            'C': 'TMS 32',
            'D': 'TFRS 7',
            'E': 'TMS 1',
        },
        'D',
        'Finansal araçlardan kaynaklanan risklerin niteliği ve boyutuna ilişkin açıklamalar **TFRS 7 Finansal Araçlar: Açıklamalar** standardında düzenlenmiştir; TFRS 9 muhasebeleştirme ve ölçümü, TMS 32 sunumu düzenler.',
        'TFRS 7 p. 1, 31',
    ),
    # düzey 3
    '0016': patch(
        "Bir işletme GUDDKG olarak ölçtüğü tahvili 1.030.000 ₺'ye satmıştır. Satış tarihinde tahvilin itfa edilmiş maliyeti 990.000 ₺, son değerleme tutarı 1.020.000 ₺'dir ve özkaynakta 30.000 ₺ birikmiş kazanç bulunmaktadır. Satış yılında kâr veya zarara yansıyan toplam kazanç kaç ₺'dir?",
        {
            'A': '1.030.000',
            'B': '40.000',
            'C': '10.000',
            'D': '30.000',
            'E': '70.000',
        },
        'B',
        "Satış kazancı 1.030.000 − 1.020.000 = 10.000 ₺'ye, DKG'den kâr veya zarara aktarılan 30.000 ₺ eklenir: **40.000 ₺**. Bu tutar, tahvil itfa edilmiş maliyetle ölçülseydi oluşacak kazanca eşittir.",
        'TFRS 9 p. 5.7.10, 3.2.12',
    ),
    # düzey 2
    '0017': patch(
        "Bir işletmenin itfa edilmiş maliyetle ölçülen 10.000 ABD doları ticari alacağı vardır. İşlem tarihinde kur 30 ₺, raporlama tarihinde 32 ₺'dir. Alacağın değerlemesinden kâr veya zarara yansıyacak kur farkı kaç ₺'dir?",
        {
            'A': '0',
            'B': '20.000',
            'C': '300.000',
            'D': '320.000',
            'E': '620.000',
        },
        'B',
        'Parasal kalemler raporlama tarihinde kapanış kuruyla çevrilir; itfa edilmiş maliyetle ölçülen parasal varlıklardaki kur farkları TFRS 9 UR B5.7.2 ve TMS 21 p. 28 uyarınca **kâr veya zarara** yansır: 10.000 × (32 − 30) = **20.000 ₺**.',
        'TFRS 9 UR B5.7.2; TMS 21 p. 23, 28',
    ),
    # düzey 2
    '0018': patch(
        "Bir işletme bankadan 1.000.000 ₺ kredi kullanmış, kredinin kullandırılmasıyla doğrudan ilişkili 20.000 ₺ dosya masrafı ve komisyon ödemiştir. Kredi itfa edilmiş maliyetle ölçülecektir. Kredinin ilk ölçüm tutarı kaç ₺'dir?",
        {
            'A': '960.000',
            'B': '1.000.000',
            'C': '1.020.000',
            'D': '980.000',
            'E': '20.000',
        },
        'D',
        "TFRS 9 p. 5.1.1'e göre GUDKZ olmayan finansal yükümlülüklerde, ihraçla doğrudan ilişkili **işlem maliyetleri gerçeğe uygun değerden düşülür**: 1.000.000 − 20.000 = **980.000 ₺**; fark etkin faiz yöntemiyle vadeye yayılır.",
        'TFRS 9 p. 5.1.1',
    ),
    # düzey 3
    '0019': patch(
        'Beklenen kredi zararlarına ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Kredi riskinde önemli artış yoksa 12 aylık BKZ kadar karşılık ayrılır\n\nII. Önemli finansman bileşeni içermeyen ticari alacaklarda ömür boyu BKZ uygulanır\n\nIII. Özkaynak araçları için de BKZ karşılığı ayrılır',
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'II ve III',
            'D': 'Yalnız II',
            'E': 'I, II ve III',
        },
        'A',
        "TFRS 9 p. 5.5.5'e göre 1. aşamada 12 aylık BKZ (I), p. 5.5.15'e göre bu ticari alacaklarda ömür boyu BKZ (II) uygulanır. Özkaynak araçları **değer düşüklüğü hükümlerine tabi değildir** (III yanlış).",
        'TFRS 9 p. 5.5.3, 5.5.5, 5.5.15',
    ),
    # düzey 2
    '0020': patch(
        'Aşağıdakilerden hangileri finansal varlık veya finansal yükümlülüktür?\n\nI. Ödenecek kurumlar vergisi\n\nII. Satıcılara olan ticari borçlar\n\nIII. Peşin ödenmiş kira giderleri',
        {
            'A': 'Yalnız II',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'Yalnız I',
            'E': 'I, II ve III',
        },
        'A',
        "TMS 32'ye göre ticari borçlar sözleşmeye dayalı nakit ödeme yükümlülüğü olduğundan finansal yükümlülüktür (II). Kanundan doğan vergi borcu (I) ve karşılığında hizmet alınacak peşin ödenmiş giderler (III) finansal araç değildir.",
        'TMS 32 p. 11, UR 11-12',
    ),
    # düzey 3
    '0021': patch(
        "Bir işletmenin borçları şunlardır: tedarikçilere ticari borçlar, banka kredisi, çıkarılmış tahviller, ödenecek kurumlar vergisi ve müşteriden alınan sipariş avansı (karşılığında mal teslim edilecek). Bunlardan kaç tanesi TMS 32'ye göre finansal yükümlülüktür?",
        {
            'A': '6',
            'B': '5',
            'C': '3',
            'D': '7',
            'E': '4',
        },
        'C',
        "TMS 32 p. 11'e göre finansal yükümlülük, **sözleşmeye dayalı** olarak nakit veya başka bir finansal varlık verme yükümlülüğüdür. Ticari borç, banka kredisi ve tahviller finansal yükümlülüktür (**3**). UR 12'ye göre sözleşmeden değil kanundan doğan vergi borcu ile mal teslimiyle ifa edilecek avans finansal yükümlülük değildir.",
        'TMS 32 p. 11, UR 12',
    ),
    # düzey 2
    '0022': patch(
        "Bir işletme sözleşmeye bağlı nakit akışlarını vadeye kadar tahsil etmek amacıyla 800.000 ₺'ye devlet tahvili almış, 8.000 ₺ işlem maliyetine katlanmıştır. Tahvil SPPI ölçütünü sağlamaktadır. Tahvilin ilk ölçüm tutarı kaç ₺'dir?",
        {
            'A': '792.000',
            'B': '816.000',
            'C': '8.000',
            'D': '808.000',
            'E': '800.000',
        },
        'D',
        "TFRS 9 p. 5.1.1'e göre GUDKZ dışındaki finansal varlıklarda **edinmeyle doğrudan ilişkili işlem maliyetleri gerçeğe uygun değere eklenir**: 800.000 + 8.000 = **808.000 ₺**.",
        'TFRS 9 p. 5.1.1',
    ),
    # düzey 2
    '0023': patch(
        'Bir banka, sözleşmeye bağlı nakit akışlarını tahsil etmek amacıyla elde tuttuğu ve nakit akışları yalnızca anapara ve anapara bakiyesine ilişkin faiz ödemelerinden oluşan kredileri sınıflandırmaktadır. GUD opsiyonu kullanılmamıştır. Bu krediler hangi ölçüm sınıfına girer?',
        {
            'A': 'Maliyet yöntemi',
            'B': "GUD farkı DKG'ye yansıtılan",
            'C': 'Özkaynak yöntemi',
            'D': 'İtfa edilmiş maliyet',
            'E': 'GUD farkı kâr veya zarara yansıtılan',
        },
        'D',
        "TFRS 9 p. 4.1.2'ye göre finansal varlık, **sözleşmeye bağlı nakit akışlarını tahsil etmeyi amaçlayan bir iş modeli** kapsamında elde tutuluyor ve nakit akışları **yalnızca anapara ve faiz ödemelerinden** oluşuyorsa itfa edilmiş maliyetle ölçülür.",
        'TFRS 9 p. 4.1.2',
    ),
    # düzey 3
    '0024': patch(
        'Bir işletme, itfa edilmiş maliyetle ölçülebilecek bir tahvil portföyünü, bununla ilişkili ve GUDKZ olarak ölçülen bir finansal yükümlülüğü nedeniyle ortaya çıkacak ölçüm tutarsızlığını gidermek amacıyla ilk muhasebeleştirmede GUDKZ olarak tanımlamak istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Amaç muhasebe uyumsuzluğunu gidermektir',
            'B': 'Tanımlama sonraki dönemlerde geri alınabilir',
            'C': 'Tanımlama ilk muhasebeleştirmede yapılır',
            'D': 'Bu seçenek GUD opsiyonu olarak adlandırılır',
            'E': 'Tanımlama geri dönülemez niteliktedir',
        },
        'B',
        "TFRS 9 p. 4.1.5'e göre işletme, muhasebe uyumsuzluğunu ortadan kaldırıyor veya önemli ölçüde azaltıyorsa, finansal varlığı **ilk muhasebeleştirmede ve geri dönülemez şekilde** GUDKZ olarak tanımlayabilir.",
        'TFRS 9 p. 4.1.5',
    ),
    # düzey 3
    '0025': patch(
        "Bir işletmenin GUDKZ olarak ölçtüğü hisse senetlerinin dönem başı gerçeğe uygun değeri 500.000 ₺, dönem sonu gerçeğe uygun değeri 560.000 ₺'dir. Dönem içinde 20.000 ₺ nakit temettü tahsil edilmiştir. Bu yatırımın dönemin kâr veya zararına toplam etkisi kaç ₺'dir?",
        {
            'A': '40.000',
            'B': '60.000',
            'C': '560.000',
            'D': '80.000',
            'E': '20.000',
        },
        'D',
        'GUDKZ varlıklarda gerçeğe uygun değer değişimi ve temettüler **kâr veya zarara** yansır: (560.000 − 500.000) + 20.000 = **80.000 ₺**.',
        'TFRS 9 p. 5.7.1, 5.7.1A',
    ),
    # düzey 3
    '0026': patch(
        "Bir işletmenin GUDDKG olarak ölçtüğü bir tahvilin dönem sonu itfa edilmiş maliyeti 990.000 ₺, gerçeğe uygun değeri 1.020.000 ₺'dir; dönem başında DKG'de birikmiş tutar yoktur ve faiz geliri etkin faiz yöntemiyle kâr veya zarara alınmıştır. Dönem sonunda diğer kapsamlı gelire yansıtılacak tutar kaç ₺'dir?",
        {
            'A': '30.000',
            'B': '1.020.000',
            'C': '40.000',
            'D': '990.000',
            'E': '0',
        },
        'A',
        "TFRS 9 p. 5.7.10-5.7.11'e göre GUDDKG borçlanma araçlarında faiz, BKZ ve kur farkları kâr veya zarara; **gerçeğe uygun değer ile itfa edilmiş maliyet arasındaki fark diğer kapsamlı gelire** yansır: 1.020.000 − 990.000 = **30.000 ₺**.",
        'TFRS 9 p. 5.7.10-5.7.11',
    ),
    # düzey 2
    '0027': patch(
        'Bir işletme, ticari amaçla elde tutmadığı ve GUD opsiyonunu kullanmadığı banka kredisini ilk muhasebeleştirmeden sonra ölçmektedir. Kredi hangi esasla ölçülür?',
        {
            'A': 'Net gerçekleşebilir değer',
            'B': 'Gerçeğe uygun değer',
            'C': 'Nominal değer',
            'D': 'Cari maliyet',
            'E': 'İtfa edilmiş maliyet',
        },
        'E',
        "TFRS 9 p. 4.2.1'e göre finansal yükümlülükler, GUDKZ olanlar ve bazı özel durumlar dışında **etkin faiz yöntemiyle itfa edilmiş maliyetle** ölçülür.",
        'TFRS 9 p. 4.2.1',
    ),
    # düzey 2
    '0028': patch(
        "Bir işletme, itfa edilmiş maliyetle ölçtüğü tahvil borçlarını, piyasa faizlerinin düşmesi nedeniyle GUDKZ sınıfına aktarmak istemektedir. TFRS 9'a göre bu yeniden sınıflandırma hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Geriye dönük yapılır',
            'B': 'İş modeli değişirse yapılır',
            'C': 'İleriye dönük yapılır',
            'D': 'Yapılamaz',
            'E': 'Dipnotla yapılır',
        },
        'D',
        "TFRS 9 p. 4.4.2'ye göre işletme **hiçbir finansal yükümlülüğü yeniden sınıflandıramaz**; yeniden sınıflandırma yalnız finansal varlıklar için ve iş modeli değişikliğiyle mümkündür.",
        'TFRS 9 p. 4.4.2',
    ),
    # düzey 3
    '0029': patch(
        "Bir bankanın 1.000.000 ₺ tutarındaki kredisinde kredi riski ilk muhasebeleştirmeden bu yana önemli ölçüde artmıştır; kredi henüz değer düşüklüğüne uğramamıştır. Kredinin ömrü boyunca temerrüt olasılığı %10, temerrüt hâlinde kayıp oranı %40'tır. Ayrılacak zarar karşılığı kaç ₺'dir?",
        {
            'A': '60.000',
            'B': '72.000',
            'C': '100.000',
            'D': '40.000',
            'E': '400.000',
        },
        'D',
        "TFRS 9 p. 5.5.3'e göre kredi riskinde **önemli artış** varsa (2. aşama) zarar karşılığı **ömür boyu beklenen kredi zararına** eşit ölçülür: 1.000.000 × %10 × %40 = **40.000 ₺**.",
        'TFRS 9 p. 5.5.3',
    ),
    # düzey 3
    '0030': patch(
        "Bir bankanın bir müşteriye verdiği kredide sözleşmeye bağlı ödemeler 35 gün gecikmiştir. Banka, gecikmenin kredi riskinde önemli bir artış olmadığını gösteren makul ve desteklenebilir bilgiye sahip değildir. TFRS 9'a göre zarar karşılığı nasıl ölçülür?",
        {
            'A': 'Gerçekleşmiş zarar',
            'B': '12 aylık beklenen kredi zararı',
            'C': 'Karşılık ayrılmaz',
            'D': 'Nominal tutarın yarısı',
            'E': 'Ömür boyu beklenen kredi zararı',
        },
        'E',
        "TFRS 9 p. 5.5.11'e göre ödemeler **30 günden fazla gecikmişse** kredi riskinin ilk muhasebeleştirmeden bu yana önemli ölçüde arttığı çürütülebilir bir varsayımdır; aksine bilgi yoksa zarar karşılığı **ömür boyu BKZ** ile ölçülür.",
        'TFRS 9 p. 5.5.11',
    ),
    # düzey 3
    '0031': patch(
        "Bir işletme 500.000 ₺'lik ticari alacaklarını bir faktoring şirketine 480.000 ₺'ye devretmiştir; ancak alacaklar tahsil edilemezse faktoring şirketine tam rücu hakkı tanımıştır. Alacaklara ilişkin risk ve getirilerin önemli ölçüde tamamı işletmede kalmıştır. İşletme alınan 480.000 ₺'yi nasıl muhasebeleştirir?",
        {
            'A': 'Alacak tahsilatı olarak',
            'B': 'Diğer kapsamlı gelir olarak',
            'C': 'Özkaynak olarak',
            'D': 'Hasılat olarak',
            'E': 'Finansal yükümlülük olarak',
        },
        'E',
        "TFRS 9 p. 3.2.6(b) ve 3.2.15'e göre işletme devredilen varlığın sahipliğine ilişkin **risk ve getirilerin önemli ölçüde tamamını elde tutuyorsa** varlığı tablo dışı bırakmaz ve alınan bedel için **finansal yükümlülük** tanır (teminatlı borçlanma).",
        'TFRS 9 p. 3.2.6, 3.2.15',
    ),
    # düzey 2
    '0032': patch(
        'Bir işletme, gelecek yıl gerçekleşmesi yüksek olasılıklı döviz cinsinden hammadde alımının kur riskinden korunmak için vadeli döviz alım sözleşmesi yapmış ve riskten korunma muhasebesi uygulamaktadır. Bu korunma ilişkisinin türü hangisidir?',
        {
            'A': 'Likidite riskinden korunma',
            'B': 'Nakit akış riskinden korunma',
            'C': 'Gerçeğe uygun değer riskinden korunma',
            'D': 'Kredi riskinden korunma',
            'E': 'Net yatırım riskinden korunma',
        },
        'B',
        "TFRS 9 p. 6.5.2(b)'ye göre **gerçekleşmesi yüksek olasılıklı tahmini bir işlemle** ilgili nakit akışlarındaki değişkenliğe karşı korunma **nakit akış riskinden korunmadır**.",
        'TFRS 9 p. 6.5.2',
    ),
    # düzey 3
    '0033': patch(
        "Bir işletme, gün içi alım satım yaptığı borsa hisselerinin GUD değişimlerini DKG'de sunmak istemektedir. TFRS 9'a göre bu tercih hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Ara dönemde yapılabilir',
            'B': 'Denetçi onayıyla yapılabilir',
            'C': 'Yapılamaz',
            'D': 'Geri dönülemez biçimde yapılabilir',
            'E': 'Yıllık olarak yapılabilir',
        },
        'C',
        "TFRS 9 p. 5.7.5'e göre GUD değişimlerini DKG'de sunma tercihi yalnızca **ticari amaçla elde tutulmayan** özkaynak araçları için yapılabilir. Gün içi alım satım yapılan hisseler ticari amaçlıdır ve GUDKZ ölçülür.",
        'TFRS 9 p. 4.1.4, 5.7.5',
    ),
    # düzey 2
    '0034': patch(
        "Bir işletme GUDKZ olarak ölçtüğü ve son değerlemede 560.000 ₺ ile taşıdığı hisse senetlerini 590.000 ₺'ye satmış, 3.000 ₺ komisyon ödemiştir. Satıştan kâr veya zarara yansıyan net kazanç kaç ₺'dir?",
        {
            'A': '33.000',
            'B': '3.000',
            'C': '587.000',
            'D': '30.000',
            'E': '27.000',
        },
        'E',
        "TFRS 9 p. 3.2.12'ye göre tablo dışı bırakmada defter değeri ile alınan bedel arasındaki fark kâr veya zarara yansır; satış komisyonu da giderdir: 590.000 − 560.000 − 3.000 = **27.000 ₺**.",
        'TFRS 9 p. 5.7.1, 3.2.12',
    ),
    # düzey 3
    '0035': patch(
        "Bir bankanın bir kredisi için önceki yıl sonunda 12 aylık BKZ esasıyla 8.000 ₺ karşılık ayrılmıştır. Bu yıl kredi riskinde önemli artış olmuş ve ömür boyu BKZ 40.000 ₺ olarak hesaplanmıştır. Bu yıl kâr veya zarara yansıtılacak değer düşüklüğü zararı kaç ₺'dir?",
        {
            'A': '8.000',
            'B': '48.000',
            'C': '32.000',
            'D': '0',
            'E': '40.000',
        },
        'C',
        "TFRS 9 p. 5.5.8'e göre raporlama tarihindeki gerekli karşılığa ulaşmak için yapılan düzeltme **değer düşüklüğü kazancı veya zararı** olarak kâr veya zarara yansır: 40.000 − 8.000 = **32.000 ₺**.",
        'TFRS 9 p. 5.5.3, 5.5.8',
    ),
    # düzey 2
    '0036': patch(
        'GUDDKG olarak ölçülen bir borçlanma aracına ilişkin olarak aşağıdaki kalemlerden hangisi dönemin kâr veya zararına yansıtılmaz?',
        {
            'A': 'Etkin faiz geliri',
            'B': 'Beklenen kredi zararı',
            'C': 'Dönem sonu GUD değişimi',
            'D': 'Satışta aktarılan birikmiş DKG',
            'E': 'Kur farkı',
        },
        'C',
        "TFRS 9 p. 5.7.10-5.7.11'e göre GUDDKG borçlanma araçlarında faiz geliri, değer düşüklüğü, kur farkları ve satışta yeniden sınıflandırılan tutar kâr veya zarara; **dönem sonundaki gerçeğe uygun değer değişimi** ise diğer kapsamlı gelire yansır.",
        'TFRS 9 p. 5.7.10-5.7.11',
    ),
    # düzey 3
    '0037': patch(
        "Bir işletme nominal değeri 1.000.000 ₺ olan 2 yıl vadeli sıfır kuponlu bir tahvili 826.000 ₺'ye almış ve itfa edilmiş maliyetle ölçmektedir; etkin faiz oranı %10'dur. Birinci yılın faiz geliri kaç ₺'dir?",
        {
            'A': '82.600',
            'B': '0',
            'C': '100.000',
            'D': '174.000',
            'E': '87.000',
        },
        'A',
        'Sıfır kuponlu tahvilde kupon tahsilatı olmasa da faiz geliri etkin faiz yöntemiyle tahakkuk ettirilir: 826.000 × %10 = **82.600 ₺**; iskontonun doğrusal dağıtımı etkin faiz yöntemi değildir.',
        'TFRS 9 p. 5.4.1',
    ),
    # düzey 1
    '0038': patch(
        'Bir işletme, ticari amaçla elde tutmadığı bir şirketin hisse senetlerini almış; ilk muhasebeleştirmede değer değişimlerini diğer kapsamlı gelirde sunma tercihinde bulunmamıştır. Hisselerin yıl sonundaki değer artışı nereye yansıtılır?',
        {
            'A': 'Yeniden değerleme fonuna',
            'B': 'Kâr veya zarara',
            'C': 'Diğer kapsamlı gelire',
            'D': 'Doğrudan özkaynağa',
            'E': 'Geçmiş yıllar kârlarına',
        },
        'B',
        "TFRS 9 p. 4.1.4'e göre özkaynak araçlarının nakit akışları anapara ve faizden oluşmadığından bunlar kural olarak **GUD farkı kâr veya zarara yansıtılarak** ölçülür; DKG sunumu ancak ilk muhasebeleştirmede yapılan geri dönülemez tercihle mümkündür.",
        'TFRS 9 p. 4.1.4',
    ),
    # düzey 2
    '0039': patch(
        "TFRS 9'a göre finansal varlıkların sınıflandırılmasında aşağıdakilerden hangileri dikkate alınır?\n\nI. İşletmenin finansal varlıkları yönetmeye yönelik iş modeli\n\nII. Sözleşmeye bağlı nakit akışlarının özellikleri\n\nIII. Varlığın ilk alındığı tarihteki vergi mevzuatı",
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'Yalnız II',
            'D': 'I ve III',
            'E': 'I ve II',
        },
        'E',
        "TFRS 9 p. 4.1.1'e göre finansal varlıklar **iş modeli** (I) ve **sözleşmeye bağlı nakit akışlarının özellikleri** (II) esas alınarak sınıflandırılır; vergi mevzuatı sınıflandırma ölçütü değildir (III yanlış).",
        'TFRS 9 p. 4.1.1-4.1.4',
    ),
    # düzey 3
    '0040': patch(
        "Aşağıdakilerden hangileri TFRS 9'a göre doğrudur?\n\nI. GUDKZ varlıklarda işlem maliyetleri ilk ölçüme eklenir\n\nII. İtfa edilmiş maliyetle ölçülen varlıklarda faiz geliri etkin faiz yöntemiyle hesaplanır\n\nIII. GUDKZ varlıkların değer değişimleri kâr veya zarara yansır",
        {
            'A': 'Yalnız III',
            'B': 'II ve III',
            'C': 'I, II ve III',
            'D': 'I ve II',
            'E': 'Yalnız II',
        },
        'B',
        "TFRS 9 p. 5.4.1'e göre etkin faiz yöntemi uygulanır (II); GUDKZ varlıkların değer değişimleri kâr veya zarara yansır (III). p. 5.1.1'e göre GUDKZ varlıklarda işlem maliyetleri **doğrudan gider** yazılır (I yanlış).",
        'TFRS 9 p. 5.1.1, 5.4.1, 5.7.1',
    ),
    # düzey 2
    '0041': patch(
        "Bir işletme kısa vadede satarak kâr elde etmek amacıyla borsadan 500.000 ₺'ye hisse senedi almış ve 5.000 ₺ aracı kurum komisyonu ödemiştir. Hisse senetlerinin ilk ölçüm tutarı kaç ₺'dir?",
        {
            'A': '500.000',
            'B': '495.000',
            'C': '480.000',
            'D': '490.000',
            'E': '5.000',
        },
        'A',
        "TFRS 9 p. 5.1.1'e göre finansal varlık ilk muhasebeleştirmede gerçeğe uygun değerle ölçülür; **gerçeğe uygun değer farkı kâr veya zarara yansıtılan** varlıklarda işlem maliyetleri maliyete eklenmez, **doğrudan gider** yazılır: **500.000 ₺**.",
        'TFRS 9 p. 5.1.1',
    ),
    # düzey 2
    '0042': patch(
        'Bir işletme, gelecek ay belirli bir fiyattan kendi kullanımı için hammadde almak üzere tedarikçisiyle sözleşme yapmıştır; sözleşme net nakitle kapatılamaz ve işletme bu tür sözleşmeleri teslim alarak ifa etmektedir. Bu sözleşme için TFRS 9 bakımından ne söylenebilir?',
        {
            'A': 'Finansal varlıktır',
            'B': 'Finansal yükümlülüktür',
            'C': 'Kapsam dışındadır',
            'D': 'Özkaynak aracıdır',
            'E': 'Türev araç olarak ölçülür',
        },
        'C',
        "TFRS 9 p. 2.4'e göre finansal olmayan kalemlerin, işletmenin **beklenen alım, satım veya kullanım ihtiyaçları doğrultusunda** teslim alınması amacıyla yapılan ve bu amaçla elde tutulan sözleşmeleri (kendi kullanımı istisnası) standardın kapsamı dışındadır.",
        'TFRS 9 p. 3.1.1',
    ),
    # düzey 3
    '0043': patch(
        'Bir işletme, faizi borsa endeksinin getirisine bağlı olarak değişen bir tahvil almış ve vadeye kadar tahsil etmek amacıyla elde tutmaktadır. Tahvilin nakit akışları yalnızca anapara ve faizden oluşmamaktadır. Tahvil hangi ölçüm sınıfına girer?',
        {
            'A': 'Maliyet yöntemi',
            'B': 'GUD farkı kâr veya zarara yansıtılan',
            'C': 'İtfa edilmiş maliyet',
            'D': "GUD farkı DKG'ye yansıtılan",
            'E': 'Özkaynak yöntemi',
        },
        'B',
        "TFRS 9 p. 4.1.4'e göre itfa edilmiş maliyet veya GUDDKG koşullarını sağlamayan finansal varlıklar GUD farkı kâr veya zarara yansıtılarak ölçülür. Hisse endeksine bağlı getiri **SPPI ölçütünü sağlamadığından**, iş modeli tahsil olsa bile varlık GUDKZ sınıfındadır.",
        'TFRS 9 p. 4.1.2, 4.1.4',
    ),
    # düzey 2
    '0044': patch(
        'Bir işletme, bir bankayla yaptığı faiz swapı sözleşmesini riskten korunma aracı olarak belirlememiştir. Bu türev aracın dönem sonundaki gerçeğe uygun değer değişimi nereye yansıtılır?',
        {
            'A': 'Doğrudan özkaynağa',
            'B': 'Karşılıklara',
            'C': 'Diğer kapsamlı gelire',
            'D': 'Kâr veya zarara',
            'E': 'Geçmiş yıllar kârlarına',
        },
        'D',
        "TFRS 9'a göre riskten korunma aracı olarak belirlenmeyen **türev araçlar ticari amaçla elde tutulan** kalemlerdir ve gerçeğe uygun değer farkı kâr veya zarara yansıtılarak ölçülür.",
        'TFRS 9 p. 4.1.4, UR B4.1.9',
    ),
    # düzey 3
    '0045': patch(
        "Bir işletme 1 Ocak 2025'te nominal değeri 1.000.000 ₺, yıllık kupon faizi %8 olan bir tahvili 950.000 ₺'ye almış ve itfa edilmiş maliyetle ölçmektedir; etkin faiz oranı %10'dur. Kupon yıl sonunda tahsil edilmiştir. Tahvilin 31 Aralık 2025 tarihli itfa edilmiş maliyeti kaç ₺'dir?",
        {
            'A': '1.045.000',
            'B': '950.000',
            'C': '870.000',
            'D': '965.000',
            'E': '1.000.000',
        },
        'D',
        'İtfa edilmiş maliyet: dönem başı 950.000 + etkin faiz 95.000 − tahsil edilen kupon 80.000 = **965.000 ₺**; iskonto vadeye kadar itfa edilerek nominal değere yaklaşır.',
        'TFRS 9 p. 5.4.1',
    ),
    # düzey 3
    '0046': patch(
        "Bir işletme, GUD değişimlerini DKG'de sunmayı seçtiği hisseleri önceki yıl sonunda 340.000 ₺ değerle taşımaktadır; özkaynakta birikmiş 37.000 ₺ kazanç vardır. Hisseler bu yıl 360.000 ₺'ye satılmıştır. Satış yılında kâr veya zarara yansıtılacak tutar kaç ₺'dir?",
        {
            'A': '0',
            'B': '37.000',
            'C': '360.000',
            'D': '20.000',
            'E': '57.000',
        },
        'A',
        "TFRS 9 p. 5.7.5 ve UR B5.7.1'e göre bu özkaynak araçlarında DKG'ye yansıtılan tutarlar **sonradan kâr veya zarara aktarılmaz**; satışa kadar oluşan değer değişimi de DKG'de kalır. Birikmiş tutar özkaynak içinde geçmiş yıllar kârlarına aktarılabilir. Temettüler ise kâr veya zarara yansır.",
        'TFRS 9 p. 5.7.5, UR B5.7.1',
    ),
    # düzey 3
    '0047': patch(
        "Bir işletme ihraç ettiği tahvilleri (finansal yükümlülük) GUDKZ olarak tanımlamıştır. Tahvillerin gerçeğe uygun değeri dönem içinde 1.000.000 ₺'den 940.000 ₺'ye düşmüştür; bu düşüşün 25.000 ₺'lik kısmı işletmenin kendi kredi riskindeki kötüleşmeden kaynaklanmaktadır. Bu sunum muhasebe uyumsuzluğu yaratmamaktadır. Kâr veya zarara yansıtılacak kazanç kaç ₺'dir?",
        {
            'A': '35.000',
            'B': '25.000',
            'C': '60.000',
            'D': '85.000',
            'E': '0',
        },
        'A',
        "TFRS 9 p. 5.7.7'ye göre GUDKZ olarak tanımlanan yükümlülüklerde **kendi kredi riskindeki değişimden** kaynaklanan GUD değişimi diğer kapsamlı gelirde, kalan kısım kâr veya zararda sunulur: (1.000.000 − 940.000) − 25.000 = **35.000 ₺**; 25.000 ₺ DKG'ye yansır.",
        'TFRS 9 p. 5.7.7',
    ),
    # düzey 3
    '0048': patch(
        "Bir banka 1.000.000 ₺ tutarında kredi vermiştir. Kredinin ilk muhasebeleştirmeden bu yana kredi riskinde önemli bir artış yoktur. 12 aylık temerrüt olasılığı %2, temerrüt hâlinde kayıp oranı %40'tır; temerrüt anındaki tutar kredi bakiyesine eşittir. Ayrılacak zarar karşılığı kaç ₺'dir?",
        {
            'A': '400.000',
            'B': '40.000',
            'C': '12.000',
            'D': '20.000',
            'E': '8.000',
        },
        'E',
        "TFRS 9 p. 5.5.5'e göre kredi riskinde önemli artış yoksa (1. aşama) **12 aylık beklenen kredi zararı** kadar karşılık ayrılır: 1.000.000 × %2 × %40 = **8.000 ₺**.",
        'TFRS 9 p. 5.5.5, 5.5.17',
    ),
    # düzey 3
    '0049': patch(
        "Bir bankanın brüt defter değeri 800.000 ₺ olan bir kredisi kredi değer düşüklüğüne uğramıştır (3. aşama); kredi için 300.000 ₺ zarar karşılığı ayrılmıştır. Etkin faiz oranı %10'dur. Kredi için tanınacak yıllık faiz geliri kaç ₺'dir?",
        {
            'A': '10.000',
            'B': '50.000',
            'C': '20.000',
            'D': '0',
            'E': '30.000',
        },
        'B',
        "TFRS 9 p. 5.4.1(b)'ye göre sonradan kredi değer düşüklüğüne uğrayan finansal varlıklarda faiz geliri **itfa edilmiş maliyet (brüt defter değeri eksi zarar karşılığı)** üzerinden hesaplanır: (800.000 − 300.000) × %10 = **50.000 ₺**. 1. ve 2. aşamada brüt defter değeri esas alınır.",
        'TFRS 9 p. 5.4.1(b)',
    ),
    # düzey 2
    '0050': patch(
        "Bir işletmenin varlıkları şunlardır: itfa edilmiş maliyetle ölçülen tahviller, GUDDKG olarak ölçülen tahviller, ticari alacaklar, kira alacakları ve GUD değişimleri DKG'de sunulan hisse senetleri. Bunlardan hangisi TFRS 9'un değer düşüklüğü hükümlerine tabi değildir?",
        {
            'A': 'Kira alacakları',
            'B': "DKG'de sunulan hisse senetleri",
            'C': 'GUDDKG tahviller',
            'D': 'Ticari alacaklar',
            'E': 'İtfa edilmiş maliyetli tahviller',
        },
        'B',
        "TFRS 9 p. 5.5.1'e göre değer düşüklüğü hükümleri itfa edilmiş maliyetle ve GUDDKG ölçülen **borçlanma araçlarına**, kira alacaklarına, sözleşme varlıklarına ve bazı kredi taahhütlerine uygulanır. **Özkaynak araçları** değer düşüklüğüne tabi değildir.",
        'TFRS 9 p. 5.5.1',
    ),
    # düzey 3
    '0051': patch(
        "Bir işletme alacaklarını rücu hakkı olmaksızın bir faktoring şirketine satmıştır; tahsil edilememe riski dâhil sahipliğe ilişkin risk ve getirilerin önemli ölçüde tamamı alıcıya geçmiştir. TFRS 9'a göre alacaklar hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Tabloda kalır',
            'B': 'Teminat olarak izlenir',
            'C': 'Sözleşme varlığına dönüşür',
            'D': 'Tablo dışı bırakılır',
            'E': 'Kısmen tabloda kalır',
        },
        'D',
        "TFRS 9 p. 3.2.6(a)'ya göre işletme finansal varlığın sahipliğine ilişkin **risk ve getirilerin önemli ölçüde tamamını devretmişse** varlığı finansal tablo dışı bırakır ve devirde oluşan veya elde tutulan hak ve yükümlülükleri ayrıca tanır.",
        'TFRS 9 p. 3.2.6',
    ),
    # düzey 3
    '0052': patch(
        "Nakit akış riskinden korunma ilişkisinde korunma aracının dönem içinde 70.000 ₺ değer kazancı olmuştur; korunan kalemin beklenen nakit akışlarının bugünkü değerindeki birikmiş değişim 55.000 ₺'dir. Bu kazancın diğer kapsamlı gelire yansıtılacak kısmı kaç ₺'dir?",
        {
            'A': '15.000',
            'B': '0',
            'C': '55.000',
            'D': '70.000',
            'E': '125.000',
        },
        'C',
        "TFRS 9 p. 6.5.11'e göre korunma aracındaki kazancın **etkin kısmı** (korunma aracındaki ve korunan kalemdeki birikmiş değişimlerden mutlak olarak küçük olanı, 55.000 ₺) DKG'de, **etkin olmayan kısmı** (15.000 ₺) kâr veya zararda muhasebeleştirilir.",
        'TFRS 9 p. 6.5.11',
    ),
    # düzey 2
    '0053': patch(
        'Bir işletme sabit faizli tahvil yatırımını, piyasa faizlerindeki değişimin gerçeğe uygun değer üzerindeki etkisine karşı faiz swapıyla korumakta ve riskten korunma muhasebesi uygulamaktadır. Korunma aracındaki kazanç veya kayıp nereye yansıtılır?',
        {
            'A': 'Kâr veya zarara',
            'B': 'Karşılıklara',
            'C': 'Sermayeye',
            'D': 'Geçmiş yıllar kârlarına',
            'E': 'Diğer kapsamlı gelire',
        },
        'A',
        "TFRS 9 p. 6.5.8'e göre **gerçeğe uygun değer riskinden korunmada** korunma aracındaki kazanç veya kayıp kâr veya zarara yansıtılır; korunan kalemin korunan riske ilişkin kazanç veya kaybı da defter değerini düzelterek kâr veya zarara alınır.",
        'TFRS 9 p. 6.5.8',
    ),
    # düzey 3
    '0054': patch(
        'Bir işletme, belirli koşullarda ihraççının hisse senetlerine dönüştürülebilen bir tahvile yatırım yapmıştır. Dönüştürme hakkı nedeniyle nakit akışları yalnızca anapara ve faizden oluşmamaktadır. Tahvil hangi ölçüm sınıfına girer?',
        {
            'A': 'İtfa edilmiş maliyet',
            'B': "GUD farkı DKG'ye yansıtılan",
            'C': 'Özkaynak yöntemi',
            'D': 'Maliyet yöntemi',
            'E': 'GUD farkı kâr veya zarara yansıtılan',
        },
        'E',
        "Dönüştürülebilir tahvilde getiri ihraççının pay değerine bağlı olduğundan **SPPI ölçütü sağlanmaz**; TFRS 9 p. 4.1.4'e göre bu tür bir finansal varlık, bütün olarak **GUD farkı kâr veya zarara yansıtılarak** ölçülür; finansal varlıklarda saklı türev ayrıştırılmaz.",
        'TFRS 9 p. 4.1.2(b), 4.1.4',
    ),
    # düzey 2
    '0055': patch(
        "Bir bankanın kredisinde sözleşmeye bağlı ödemeler 95 gün gecikmiştir ve banka aksini gösteren makul ve desteklenebilir bilgiye sahip değildir. TFRS 9'a göre bu durumda hangi varsayım yapılır?",
        {
            'A': 'Risk artmamıştır',
            'B': 'Kredi tahsil edilmiştir',
            'C': 'Temerrüt gerçekleşmiştir',
            'D': 'Kredi riski düşüktür',
            'E': 'Kredi yeniden sınıflandırılır',
        },
        'C',
        "TFRS 9 UR B5.5.37'ye göre işletme, aksini gösteren makul ve desteklenebilir bilgi yoksa **90 günü aşan gecikmede temerrüdün gerçekleştiğini** varsayar (çürütülebilir karine); bu durum kredi değer düşüklüğü göstergesidir.",
        'TFRS 9 UR B5.5.37',
    ),
    # düzey 2
    '0056': patch(
        "Bir işletme borsada hisse senedi almak için 29 Aralık'ta emir vermiş ve işlem gerçekleşmiş; hisseler piyasa düzenlemesi gereği 2 Ocak'ta hesabına teslim edilmiştir. TFRS 9'a göre bu normal yoldan alım hangi tarihte muhasebeleştirilebilir?",
        {
            'A': 'Genel kurul tarihinde',
            'B': 'Temettü tarihinde',
            'C': 'Yıl sonu değerleme tarihinde',
            'D': 'Ödeme planı tarihinde',
            'E': 'İşlem veya teslim tarihinde',
        },
        'E',
        "TFRS 9 p. 3.1.2'ye göre finansal varlığın **normal yoldan alım veya satımı işlem tarihi muhasebesi ya da teslim tarihi muhasebesi** kullanılarak muhasebeleştirilir; seçilen yöntem aynı sınıftaki bütün alımlara tutarlı uygulanır.",
        'TFRS 9 p. 3.1.2',
    ),
    # düzey 2
    '0057': patch(
        "Bir işletme tahvil yatırımı yaparken şu maliyetlere katlanmıştır: aracı kurum komisyonu, yatırım danışmanı ücreti, borsa payı, devir vergileri ve hazine biriminin genel yönetim giderleri. TFRS 9'a göre bunlardan hangisi işlem maliyeti sayılmaz?",
        {
            'A': 'Devir vergileri',
            'B': 'Borsa payı',
            'C': 'Danışman ücreti',
            'D': 'Hazine biriminin genel giderleri',
            'E': 'Aracı kurum komisyonu',
        },
        'D',
        "TFRS 9 UR B5.4.8'e göre işlem maliyetleri aracılara, danışmanlara ve komisyonculara ödenen ücret ve komisyonları, borsa paylarını ve devir vergilerini kapsar; **iç yönetim veya elde tutma maliyetlerini kapsamaz**.",
        'TFRS 9 UR B5.4.8',
    ),
    # düzey 3
    '0058': patch(
        "Bir işletme GUDKZ olarak tanımladığı bir yükümlülükte, kendi kredi riskindeki değişimin etkisini DKG'de sunmanın, bu yükümlülükle ekonomik olarak ilişkili ve GUDKZ ölçülen varlıklar nedeniyle kâr veya zararda muhasebe uyumsuzluğu yaratacağını belirlemiştir. Kendi kredi riskinden kaynaklanan değişim nerede sunulur?",
        {
            'A': 'Karşılıklarda',
            'B': 'Diğer kapsamlı gelirde',
            'C': 'Geçmiş yıllar kârlarında',
            'D': 'Kâr veya zararda',
            'E': 'Dipnotlarda',
        },
        'D',
        "TFRS 9 p. 5.7.8'e göre kendi kredi riskindeki değişimin DKG'de sunulması **kâr veya zararda muhasebe uyumsuzluğu yaratacak veya artıracaksa**, yükümlülüğün bütün kazanç ve kayıpları kâr veya zararda sunulur.",
        'TFRS 9 p. 5.7.8',
    ),
    # düzey 3
    '0059': patch(
        "Aşağıdakilerden hangileri TFRS 9'a göre doğrudur?\n\nI. Finansal yükümlülükler yeniden sınıflandırılamaz\n\nII. DKG'de sunulan özkaynak araçlarının birikmiş kazancı satışta kâr veya zarara aktarılır\n\nIII. Finansal varlıklar iş modeli değiştiğinde yeniden sınıflandırılır",
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'Yalnız III',
            'D': 'I ve II',
            'E': 'I ve III',
        },
        'E',
        "TFRS 9 p. 4.4.2'ye göre yükümlülükler yeniden sınıflandırılamaz (I); p. 4.4.1'e göre varlıklar iş modeli değiştiğinde yeniden sınıflandırılır (III). p. 5.7.5'e göre DKG'deki özkaynak aracı kazançları **kâr veya zarara aktarılmaz** (II yanlış).",
        'TFRS 9 p. 4.4.1-4.4.2, 5.7.5',
    ),
    # düzey 3
    '0060': patch(
        "Aşağıdakilerden hangileri TFRS 9'a göre doğrudur?\n\nI. Risk ve getirilerin önemli ölçüde tamamı elde tutulan devredilmiş varlık tabloda kalır\n\nII. Nakit akış riskinden korunmada etkin kısım diğer kapsamlı gelire yansır\n\nIII. Yüksek olasılıklı tahmini işlemler nakit akış riskinden korunmanın konusu olabilir",
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'I ve III',
            'D': 'I, II ve III',
            'E': 'I ve II',
        },
        'D',
        "TFRS 9 p. 3.2.6(b)'ye göre risk ve getirilerin önemli ölçüde tamamı elde tutuluyorsa varlık tabloda kalır (I); p. 6.5.11'e göre etkin kısım DKG'ye yansır (II); p. 6.5.2(b)'ye göre yüksek olasılıklı tahmini işlemler nakit akış riskinden korunmanın konusu olabilir (III).",
        'TFRS 9 p. 3.2.6, 6.5.2, 6.5.11',
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
    print(f"1 paket / {len(PATCHES)} soru ('TFRS 9 Finansal Araclar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
