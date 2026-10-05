#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TFRS 16 Kiralamalar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gercek sinav profiliyle yeniden yazim (senaryo kok + kisa tutar/terim sik). Eski surum tanim agirlikliydi ve 79 mutlak ifadeli celdirici tasiyordu (kor %40). Kapsam: kiralamanin tanimi (esasli ikame hakki, kontrol), kiralama suresi (uzatma/fesih opsiyonlari, cezasiz fesih), kisa vadeli ve dusuk degerli muafiyetler, kira yukumlulugu ve kullanim hakki ilk olcumu, degisken odemeler, kalinti deger taahhudu, faiz ve amortisman, yeniden olcum, sunum, kiraya veren siniflandirmasi, faaliyet kiralamasi geliri ve dogrudan maliyetler, finansal kiralama net yatirimi ve finansman geliri, uretici kiraya veren, satis ve geri kiralama, alt kiralama. 22 hesap sorusu modulde hesaplandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: TFRS 16 Kiralamalar (KGK) ve Uygulama Rehberi
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/tfrs_16_kiralamalar.json"
STYLE_REF = 'SGS Muhasebe Standartlari (gercek sinav profiline kalibre: senaryo kok + kisa sik)'
ONEK = "std-tfrs16-gen-"


def patch(stem, options, answer, solution, ref='TFRS 16 Kiralamalar'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        "Bir perakendeci, bir alışveriş merkezinde 3 yıl boyunca 'uygun bir alan' kullanmak için sözleşme yapmıştır. AVM işletmesi, alanın yerini işletmenin onayı olmadan ve düşük maliyetle istediği zaman değiştirebilmekte ve bu değişiklikten ekonomik fayda sağlamaktadır. Sözleşme TFRS 16 bakımından nasıl değerlendirilir?",
        {
            'A': 'Finansal kiralamadır',
            'B': 'Faaliyet kiralamasıdır',
            'C': 'Alt kiralamadır',
            'D': 'Kiralama içermez',
            'E': 'Kiralama içerir',
        },
        'D',
        "TFRS 16 p. 9 ve UR B14'e göre tedarikçinin kullanım süresi boyunca varlığı ikame etmeye yönelik **esaslı bir ikame hakkı** varsa (pratik olarak ikame edebiliyor ve bundan ekonomik fayda sağlıyorsa) **tanımlanmış bir varlık yoktur**; sözleşme kiralama içermez.",
        'TFRS 16 p. 9, UR B14',
    ),
    # düzey 2
    '0002': patch(
        "Bir işletme, tek başına değeri düşük olmayan bir kamyonu 3 yıl süreyle kiralamıştır; kamyonun alt sistemlerinden bazıları ayrı ayrı düşük değerlidir. TFRS 16'ya göre bu kiralama için düşük değerli varlık muafiyeti uygulanabilir mi?",
        {
            'A': 'Yarısına uygulanabilir',
            'B': 'İlk yıl uygulanabilir',
            'C': 'Uygulanamaz',
            'D': 'Kiraya veren onaylarsa uygulanabilir',
            'E': 'Uygulanabilir',
        },
        'C',
        "TFRS 16 UR B7'ye göre düşük değer değerlendirmesi **dayanak varlığın yeni olduğundaki değerine** göre yapılır; yeni bir kamyon genellikle düşük değerli sayılmaz. Parçaların tek başına düşük değerli olması muafiyeti sağlamaz.",
        'TFRS 16 UR B7',
    ),
    # düzey 3
    '0003': patch(
        "Bir kiracının kira yükümlülüğü ilk ölçümde 250.000 ₺'dir. Kiracı kiralama başlamadan önce kiraya verene 20.000 ₺ peşin ödeme yapmış, kiraya verenden 8.000 ₺ kiralama teşviki almış, kiralamayı elde etmek için 6.000 ₺ komisyon (başlangıçtaki doğrudan maliyet) ödemiştir. Kiralama sonunda varlığı sökme ve alanı eski hâline getirme maliyetinin bugünkü değeri 12.000 ₺'dir. Kullanım hakkı varlığının maliyeti kaç ₺'dir?",
        {
            'A': '250.000',
            'B': '268.000',
            'C': '280.000',
            'D': '264.000',
            'E': '260.000',
        },
        'C',
        "TFRS 16 p. 24'e göre kullanım hakkı varlığının maliyeti; kira yükümlülüğünün ilk ölçüm tutarı, başlangıçta veya öncesinde yapılan ödemeler (alınan teşvikler düşülerek), başlangıçtaki doğrudan maliyetler ve söküm/restorasyon maliyeti tahmininden oluşur: 250.000 + 20.000 − 8.000 + 6.000 + 12.000 = **280.000 ₺**.",
        'TFRS 16 p. 23-24',
    ),
    # düzey 3
    '0004': patch(
        "Bir kiracının 1 Ocak 2025'teki kira yükümlülüğü 248.685 ₺'dir; faiz oranı %10, yıl sonunda 100.000 ₺ kira ödenmiştir. 2025 yılı faiz gideri kaç ₺'dir?",
        {
            'A': '32.383',
            'B': '24.869',
            'C': '75.131',
            'D': '10.000',
            'E': '37.304',
        },
        'B',
        "TFRS 16 p. 36-37'ye göre kira yükümlülüğü üzerindeki faiz, **yükümlülüğün kalan bakiyesine sabit dönemsel faiz oranı** uygulanarak hesaplanır: 248.685 × %10 = **24.869 ₺**.",
        'TFRS 16 p. 36-37',
    ),
    # düzey 3
    '0005': patch(
        "Bir kiracı kullanım hakkı varlığını 270.000 ₺ maliyetle tanımıştır. Kiralama süresi 3 yıl, dayanak varlığın yararlı ömrü 8 yıldır. Kiracının kiralama sonunda varlığı sembolik bir bedelle satın alma opsiyonu vardır ve bu opsiyonun kullanılacağı makul ölçüde kesindir. Kalıntı değer yoktur. Yıllık doğrusal amortisman kaç ₺'dir?",
        {
            'A': '33.750',
            'B': '13.500',
            'C': '0',
            'D': '7.500',
            'E': '24.545',
        },
        'A',
        "TFRS 16 p. 32'ye göre kiralama dayanak varlığın mülkiyetini devrediyorsa veya kiracının **satın alma opsiyonunu kullanacağı makul ölçüde kesinse**, kullanım hakkı varlığı **dayanak varlığın yararlı ömrü** boyunca amortismana tabi tutulur: 270.000 / 8 = **33.750 ₺**.",
        'TFRS 16 p. 32',
    ),
    # düzey 2
    '0006': patch(
        "Bir işletme, yatırım amaçlı gayrimenkullerini gerçeğe uygun değer modeliyle ölçmektedir. İşletme bir binayı kiralamış ve bu binayı alt kiralamaya vererek kira geliri elde etmektedir; bina TMS 40'taki yatırım amaçlı gayrimenkul tanımını karşılamaktadır. Bu kullanım hakkı varlığı nasıl ölçülür?",
        {
            'A': 'Net gerçekleşebilir değerle',
            'B': 'Yeniden değerleme modeliyle',
            'C': 'Maliyet modeliyle',
            'D': 'Gerçeğe uygun değer modeliyle',
            'E': 'Özkaynak yöntemiyle',
        },
        'D',
        "TFRS 16 p. 34'e göre kiracı yatırım amaçlı gayrimenkullerine TMS 40'taki **gerçeğe uygun değer modelini** uyguluyorsa, TMS 40'taki yatırım amaçlı gayrimenkul tanımını karşılayan kullanım hakkı varlıklarına da bu modeli uygular.",
        'TFRS 16 p. 34-35',
    ),
    # düzey 3
    '0007': patch(
        'Bir kiracının finansal tablolarının sunumuna ilişkin olarak aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Kullanım hakkı varlıkları ayrı sunulur veya dipnotta açıklanır',
            'B': 'Kira ödemelerinin tamamı faaliyet faaliyetlerinde gösterilir',
            'C': 'Anapara ödemeleri finansman faaliyetlerinde sınıflandırılır',
            'D': 'Kısa vadeli kiralama ödemeleri faaliyet faaliyetlerinde gösterilir',
            'E': 'Kira yükümlülüğündeki faiz gideri finansman gideridir',
        },
        'B',
        "TFRS 16 p. 47-50'ye göre kullanım hakkı varlıkları ve kira yükümlülükleri ayrı sunulur veya açıklanır; faiz finansman gideridir. Nakit akış tablosunda **anapara kısmı finansman faaliyetlerinde**, faiz TMS 7'ye göre, kısa vadeli ve düşük değerli kiralama ödemeleri ile yükümlülüğe dâhil edilmeyen değişken ödemeler **faaliyet faaliyetlerinde** sınıflandırılır.",
        'TFRS 16 p. 47-50',
    ),
    # düzey 2
    '0008': patch(
        'Bir kiraya veren, bir makineyi ekonomik ömrünün büyük bölümünü kapsayan süre için kiraya vermiştir; kira ödemelerinin bugünkü değeri makinenin gerçeğe uygun değerinin önemli ölçüde tamamına eşittir. Kiraya veren bu kiralamayı nasıl sınıflandırır?',
        {
            'A': 'Satış ve geri kiralama',
            'B': 'Alt kiralama',
            'C': 'Kısa vadeli kiralama',
            'D': 'Faaliyet kiralaması',
            'E': 'Finansal kiralama',
        },
        'E',
        "TFRS 16 p. 62-63'e göre dayanak varlığın sahipliğine ilişkin **risk ve getirilerin önemli ölçüde tamamını devreden** kiralama finansal kiralamadır; kiralama süresinin ekonomik ömrün büyük bölümünü kapsaması ve bugünkü değerin gerçeğe uygun değerin önemli ölçüde tamamına eşit olması bunun göstergeleridir.",
        'TFRS 16 p. 61-62',
    ),
    # düzey 2
    '0009': patch(
        'Bir kiraya veren, faaliyet kiralamasına konu ettiği ve kendisine ait olan makineleri finansal durum tablosunda göstermeye devam etmektedir. Bu makinelerin amortismanı hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kiracı amortisman ayırır',
            'B': 'Amortisman ayrılmaz',
            'C': "Amortisman DKG'ye yansır",
            'D': 'Kiraya veren amortisman ayırır',
            'E': 'Amortisman kira gelirinden düşülüp gösterilmez',
        },
        'D',
        "TFRS 16 p. 84 ve 88'e göre faaliyet kiralamasına konu dayanak varlık **kiraya verenin** finansal durum tablosunda kalır ve kiraya veren benzer varlıklar için uyguladığı amortisman politikasıyla (TMS 16, TMS 38) amortisman ayırır.",
        'TFRS 16 p. 88',
    ),
    # düzey 3
    '0010': patch(
        "Kendi ürettiği makineleri satan bir üretici, bir makineyi finansal kiralamayla kiraya vermiştir. Makinenin üretim maliyeti 300.000 ₺, gerçeğe uygun değeri 420.000 ₺'dir; kira ödemelerinin piyasa faiz oranıyla bugünkü değeri 410.000 ₺'dir. Kiralamanın başlangıcında tanınacak hasılat kaç ₺'dir?",
        {
            'A': '300.000',
            'B': '110.000',
            'C': '410.000',
            'D': '420.000',
            'E': '120.000',
        },
        'C',
        "TFRS 16 p. 71'e göre üretici veya satıcı kiraya veren, kiralamanın başlangıcında hasılatı **dayanak varlığın gerçeğe uygun değeri ile kira ödemelerinin piyasa faiz oranıyla bugünkü değerinden düşük olanıyla** ölçer: **410.000 ₺**. Satış kârı 410.000 − 300.000 = 110.000 ₺ olur.",
        'TFRS 16 p. 71',
    ),
    # düzey 2
    '0011': patch(
        "TFRS 16'ya göre kiracının kiralamanın fiilen başladığı tarihteki muhasebeleştirmesiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Kullanım hakkı varlığı maliyet bedeliyle ölçülür',
            'B': 'Kira yükümlülüğü ödenmemiş kira ödemelerinin bugünkü değeriyle ölçülür',
            'C': 'Başlangıçtaki doğrudan maliyetler kullanım hakkı varlığına eklenir',
            'D': 'Kullanım hakkı varlığı, kira yükümlülüğünün ilk ölçüm tutarını içerir',
            'E': 'Kiracı tabloya kalem almaz; kira ödemelerini gider yazar',
        },
        'E',
        'TFRS 16.22-26: kiracı fiilî başlama tarihinde bir kullanım hakkı varlığı ve bir kira yükümlülüğü muhasebeleştirir. Kira yükümlülüğü ödenmemiş kira ödemelerinin bugünkü değeriyle; kullanım hakkı varlığı ise kira yükümlülüğünün ilk ölçüm tutarı ile başlangıçtaki doğrudan maliyetler vb. kalemleri içeren maliyet bedeliyle ölçülür.',
        'TFRS 16 p. 22',
    ),
    # düzey 2
    '0012': patch(
        'Bir işletme bir bina kiralamış; sözleşme bedeli binanın kullanımı yanında temizlik ve güvenlik hizmetlerini de kapsamaktadır. İşletme, kiralama bileşenini kiralama dışı bileşenlerden ayırmamayı tercih etmek istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Kiracı dayanak varlık sınıfı bazında ayırmama tercihini yapabilir',
            'B': 'Bu tercih kiraya verene de tanınmış bir kolaylıktır',
            'C': 'Kiracı bileşenleri ayrı muhasebeleştirebilir',
            'D': 'Ayırmama hâlinde tüm bedel tek bir kiralama bileşeni sayılır',
            'E': 'Bedel göreli tek başına satış fiyatlarına göre dağıtılabilir',
        },
        'B',
        "TFRS 16 p. 12-15'e göre kiracı sözleşme bedelini bileşenlerin göreli tek başına fiyatlarına göre dağıtır; **kiracı**, dayanak varlık sınıfı bazında kiralama dışı bileşenleri ayırmayıp tek bir kiralama bileşeni olarak muhasebeleştirmeyi seçebilir. Bu pratik kolaylık **yalnız kiracıya** tanınmıştır.",
        'TFRS 16 p. 12, 15',
    ),
    # düzey 3
    '0013': patch(
        "Bir kiracı 1 Ocak'ta bir makine kiralamıştır. Kira ödemeleri her yılın başında 100.000 ₺ olmak üzere 3 yıl sürecektir; ilk ödeme kiralama başlangıcında yapılmıştır. Alternatif borçlanma faiz oranı %10'dur. İlk ödeme yapıldıktan sonra tanınacak kira yükümlülüğü yaklaşık kaç ₺'dir?",
        {
            'A': '248.685',
            'B': '173.554',
            'C': '300.000',
            'D': '273.554',
            'E': '200.000',
        },
        'B',
        "TFRS 16 p. 26'ya göre kira yükümlülüğü **o tarihte ödenmemiş** kira ödemelerinin bugünkü değeridir. Başlangıçta yapılan ödeme yükümlülüğe girmez, kullanım hakkının maliyetine eklenir. Kalan iki ödemenin bugünkü değeri: 100.000/1,1 + 100.000/1,21 ≈ **173.554 ₺**.",
        'TFRS 16 p. 26, 27',
    ),
    # düzey 3
    '0014': patch(
        "Bir kiracı 1 Ocak'ta 270.000 ₺ maliyetle kullanım hakkı varlığı tanımıştır; kiralama süresi 3 yıl, dayanak varlığın yararlı ömrü 8 yıldır, mülkiyet devri yoktur ve doğrusal amortisman uygulanır. Değer düşüklüğü yoktur. Birinci yıl sonunda kullanım hakkı varlığının defter değeri kaç ₺'dir?",
        {
            'A': '90.000',
            'B': '270.000',
            'C': '236.250',
            'D': '180.000',
            'E': '21.315',
        },
        'D',
        "TFRS 16 p. 30'a göre maliyet modelinde kullanım hakkı varlığı, maliyetinden birikmiş amortisman ve değer düşüklüğü düşülerek ölçülür: 270.000 − 90.000 = **180.000 ₺**.",
        'TFRS 16 p. 30',
    ),
    # düzey 3
    '0015': patch(
        'Bir işletme bir depoyu aylık olarak kendiliğinden yenilenen bir sözleşmeyle kiralamıştır; hem kiracı hem kiraya veren sözleşmeyi 1 ay önceden bildirmek koşuluyla önemsiz bir ceza bile ödemeden feshedebilmektedir. Kiralama süresi nasıl belirlenir?',
        {
            'A': 'Sözleşmenin toplam beklenen süresi',
            'B': '1 ay',
            'C': '12 ay',
            'D': 'Belirsiz süre',
            'E': 'Kiracının tahmini kullanım süresi',
        },
        'B',
        "TFRS 16 UR B34'e göre kiracı ve kiraya verenin her birinin kiralamayı diğerinin iznini almadan **önemsiz bir cezayla feshetme hakkı** varsa kiralama o süreden sonra uygulanabilir değildir; kiralama süresi ihbar süresiyle sınırlıdır ve kiralama kısa vadelidir.",
        'TFRS 16 UR B34',
    ),
    # düzey 2
    '0016': patch(
        'Bir işletmenin sözleşmeleri şunlardır: ofis binası kiralaması, petrol arama hakkı, bir film lisansı, bir kamu hizmet imtiyaz anlaşması ve kiracı olarak elde tutulan biyolojik varlık kiralaması. Bunlardan hangisi TFRS 16 kapsamındadır?',
        {
            'A': 'Petrol arama hakkı',
            'B': 'Ofis binası kiralaması',
            'C': 'Hizmet imtiyaz anlaşması',
            'D': 'Biyolojik varlık kiralaması',
            'E': 'Film lisansı',
        },
        'B',
        "TFRS 16 p. 3'e göre maden ve petrol gibi yenilenemeyen kaynakların arama veya kullanım hakları, kiracının elde tuttuğu TMS 41 kapsamındaki biyolojik varlıklar, hizmet imtiyaz anlaşmaları ve kiracının TMS 38 kapsamında elde tuttuğu film gibi lisanslar kapsam dışıdır; **ofis binası kiralaması** kapsamdadır.",
        'TFRS 16 p. 3',
    ),
    # düzey 2
    '0017': patch(
        "Bir işletme benzer özelliklere sahip yüzlerce araç kiralamasını tek tek değil, bir portföy olarak muhasebeleştirmek istemektedir; portföy yaklaşımının finansal tabloları tek tek uygulamadan önemli ölçüde farklı etkilemeyeceğini makul olarak beklemektedir. TFRS 16'ya göre bu uygulama hakkında ne söylenebilir?",
        {
            'A': 'Uygulanabilir',
            'B': 'Kiraya veren onayına bağlıdır',
            'C': 'Denetçi onayına bağlıdır',
            'D': 'Uygulanamaz',
            'E': 'Kısa vadede mümkündür',
        },
        'A',
        "TFRS 16 UR B1'e göre işletme, portföy yaklaşımının etkilerinin tek tek kiralamalara uygulamadan **önemli ölçüde farklı olmayacağını makul olarak bekliyorsa**, standardı benzer özelliklere sahip kiralama portföyüne uygulayabilir.",
        'TFRS 16 UR B1',
    ),
    # düzey 3
    '0018': patch(
        "Bir kiraya verenin finansal kiralamasında kira ödemelerinin zımni faiz oranıyla bugünkü değeri 450.000 ₺, kiralama sonunda kiraya verene dönecek ve kimsenin garanti etmediği kalıntı değerin bugünkü değeri 30.000 ₺'dir. Net kiralama yatırımı kaç ₺'dir?",
        {
            'A': '480.000',
            'B': '30.000',
            'C': '390.000',
            'D': '450.000',
            'E': '420.000',
        },
        'A',
        "TFRS 16 Ek A ve p. 68'e göre net kiralama yatırımı, kira ödemeleri ile **kiraya verene tahakkuk eden garanti edilmemiş kalıntı değerin** zımni faiz oranıyla iskonto edilmiş toplamıdır: 450.000 + 30.000 = **480.000 ₺**.",
        'TFRS 16 p. 68',
    ),
    # düzey 2
    '0019': patch(
        'Kiracı muhasebesine ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Kiracı, muafiyetler dışında bütün kiralamalar için kullanım hakkı varlığı tanır\n\nII. Mülkiyet devri ve satın alma opsiyonu yoksa kullanım hakkı, dayanak varlığın yararlı ömrü boyunca amortismana tabi tutulur\n\nIII. Kısa vadeli kiralamalar doğrusal olarak giderleştirilebilir',
        {
            'A': 'Yalnız I',
            'B': 'Yalnız III',
            'C': 'I ve III',
            'D': 'I, II ve III',
            'E': 'I ve II',
        },
        'C',
        "TFRS 16 p. 22'ye göre kiracı muafiyetler dışında kullanım hakkı tanır (I); p. 6'ya göre kısa vadeli kiralamalar doğrusal giderleştirilebilir (III). p. 32'ye göre mülkiyet devri veya makul kesin satın alma opsiyonu yoksa amortisman **kiralama süresi ile yararlı ömrün kısa olanı** boyunca ayrılır (II yanlış).",
        'TFRS 16 p. 5, 22, 32',
    ),
    # düzey 3
    '0020': patch(
        'Aşağıdakilerden hangileri doğrudur?\n\nI. Kira yükümlülüğü faizle artırılıp ödemelerle azaltılır\n\nII. Endeks değişikliğinden doğan yeniden ölçüm kâr veya zarara yansıtılır\n\nIII. Satış ve geri kiralamada devir satış değilse alınan bedel finansal yükümlülüktür',
        {
            'A': 'I ve III',
            'B': 'I ve II',
            'C': 'Yalnız III',
            'D': 'II ve III',
            'E': 'Yalnız I',
        },
        'A',
        "TFRS 16 p. 36'ya göre yükümlülük faizle artar, ödemelerle azalır (I); p. 103'e göre satış olmayan devirde bedel finansal yükümlülüktür (III). p. 39'a göre yeniden ölçüm **kullanım hakkı varlığında düzeltme** olarak muhasebeleştirilir (II yanlış).",
        'TFRS 16 p. 36, 39, 42',
    ),
    # düzey 3
    '0021': patch(
        'Bir işletme, belirli seri numaralı bir kamyonu 2 yıl süreyle kullanma hakkı elde etmiştir. Kamyonun hangi rotada ve ne zaman kullanılacağına işletme karar vermekte ve kamyonun sağladığı ekonomik faydaların önemli ölçüde tamamını elde etmektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'İşletme varlığın kullanımını yönlendirme hakkına sahiptir',
            'B': 'Faydaların önemli ölçüde tamamı işletmeye aittir',
            'C': 'Tanımlanmış bir varlık vardır',
            'D': 'Tedarikçi kamyonu kullandığı için sözleşme kiralama değildir',
            'E': 'Sözleşme kiralama içerir',
        },
        'D',
        "TFRS 16 p. 9 ve UR B9'a göre sözleşme, **tanımlanmış bir varlığın** kullanımını kontrol etme hakkını (faydaların önemli ölçüde tamamını elde etme ve kullanımını yönlendirme hakkı) belirli bir süre için bedel karşılığında devrediyorsa kiralama içerir. Kamyonu tedarikçi değil işletme kullanmaktadır.",
        'TFRS 16 p. 9, UR B9',
    ),
    # düzey 2
    '0022': patch(
        'Bir işletme çalışanları için yeni olduğunda değeri düşük olan dizüstü bilgisayarlar ve cep telefonları kiralamıştır; kiralamalar 3 yıl sürelidir. İşletme bu kiralamalar için hangi muafiyeti kullanabilir?',
        {
            'A': 'Satış ve geri kiralama muafiyeti',
            'B': 'Kiraya veren muafiyeti',
            'C': 'Kısa vadeli kiralama muafiyeti',
            'D': 'Portföy muafiyeti',
            'E': 'Düşük değerli varlık muafiyeti',
        },
        'E',
        "TFRS 16 p. 5(b) ve UR B3-B8'e göre dayanak varlığın **yeni olduğundaki değeri düşükse**, kiralama süresinden bağımsız olarak düşük değerli varlık muafiyeti uygulanabilir. Kısa vadeli muafiyet 12 ayı aşan bu kiralamalara uygulanamaz.",
        'TFRS 16 p. 5, UR B3-B8',
    ),
    # düzey 3
    '0023': patch(
        "Bir işletme 1 Ocak 2025'te bir makineyi 3 yıl süreyle kiralamıştır. Kira ödemeleri her yıl sonunda 100.000 ₺'dir; kiralamadaki zımni faiz oranı belirlenemediğinden işletmenin alternatif borçlanma faiz oranı %10 kullanılacaktır. Kira yükümlülüğünün ilk ölçüm tutarı yaklaşık kaç ₺'dir?",
        {
            'A': '270.000',
            'B': '272.727',
            'C': '273.554',
            'D': '300.000',
            'E': '248.685',
        },
        'E',
        "TFRS 16 p. 26'ya göre kira yükümlülüğü, **o tarihte ödenmemiş kira ödemelerinin bugünkü değeriyle** ölçülür; zımni oran belirlenemiyorsa alternatif borçlanma faiz oranı kullanılır: 100.000 × (1/1,1 + 1/1,21 + 1/1,331) ≈ **248.685 ₺**.",
        'TFRS 16 p. 26',
    ),
    # düzey 2
    '0024': patch(
        'Bir kiracı, kira yükümlülüğünü ölçerken kullanacağı iskonto oranını belirlemektedir. Kiralamadaki zımni faiz oranı kolaylıkla belirlenebilmektedir. Hangi oran kullanılır?',
        {
            'A': 'Kiralamadaki zımni faiz oranı',
            'B': 'Merkez bankası politika faizi',
            'C': 'Ortalama mevduat faizi',
            'D': 'Alternatif borçlanma faiz oranı',
            'E': 'Enflasyon oranı',
        },
        'A',
        "TFRS 16 p. 26'ya göre kira ödemeleri, **kolaylıkla belirlenebiliyorsa kiralamadaki zımni faiz oranı**, belirlenemiyorsa kiracının alternatif borçlanma faiz oranı kullanılarak iskonto edilir.",
        'TFRS 16 p. 26',
    ),
    # düzey 3
    '0025': patch(
        "Bir kiracının 1 Ocak 2025'teki kira yükümlülüğü 248.685 ₺'dir; faiz oranı %10, yıl sonunda 100.000 ₺ kira ödenmiştir. 31 Aralık 2025 tarihli kira yükümlülüğü kaç ₺'dir?",
        {
            'A': '148.685',
            'B': '273.554',
            'C': '173.554',
            'D': '248.685',
            'E': '200.000',
        },
        'C',
        "TFRS 16 p. 36'ya göre yükümlülüğün defter değeri faizle artırılır, yapılan ödemelerle azaltılır: 248.685 + 24.869 − 100.000 = **173.554 ₺**.",
        'TFRS 16 p. 36',
    ),
    # düzey 2
    '0026': patch(
        "Bir mağaza kiralamasında kiracı, sabit kiraya ek olarak yıllık satışlarının %2'si oranında kira ödemektedir. Bu yıl satışlara bağlı ek kira 36.000 ₺ olmuştur. Bu tutar nasıl muhasebeleştirilir?",
        {
            'A': 'Dönem gideri olarak',
            'B': 'Özkaynaktan düşülerek',
            'C': 'Kira yükümlülüğüne eklenerek',
            'D': "DKG'ye alınarak",
            'E': 'Kullanım hakkı maliyetine eklenerek',
        },
        'A',
        "TFRS 16 p. 38(b)'ye göre kira yükümlülüğünün ölçümüne dâhil edilmeyen değişken kira ödemeleri, **bu ödemeleri tetikleyen olay veya koşulun gerçekleştiği dönemde kâr veya zararda** muhasebeleştirilir.",
        'TFRS 16 p. 38',
    ),
    # düzey 3
    '0027': patch(
        "Kira ödemeleri TÜFE'ye bağlı olan bir kiralamada kira yükümlülüğünün mevcut defter değeri 180.000 ₺'dir. Yeni yılın başında endeks değişimiyle kalan kira ödemeleri %40 artmıştır; indirgeme oranı değiştirilmez. Kira yükümlülüğündeki artış yaklaşık kaç ₺'dir ve karşılığı nereye yansır?",
        {
            'A': '72.000 ₺, kâr veya zarara',
            'B': '180.000 ₺, kullanım hakkına',
            'C': 'Artış tanınmaz',
            'D': '72.000 ₺, kullanım hakkına',
            'E': "72.000 ₺, DKG'ye",
        },
        'D',
        "TFRS 16 p. 42(b) ve 43'e göre endeks veya orandaki değişiklik nedeniyle gelecek kira ödemeleri değişirse yükümlülük **değiştirilmemiş indirgeme oranıyla** yeniden ölçülür; p. 39'a göre yeniden ölçüm tutarı **kullanım hakkı varlığında düzeltme** olarak muhasebeleştirilir: 180.000 × %40 = **72.000 ₺**.",
        'TFRS 16 p. 42(b), 43',
    ),
    # düzey 2
    '0028': patch(
        'Bir kiraya veren, bir ofis binasını ekonomik ömrü 50 yıl iken 5 yıl süreyle kiraya vermiştir; mülkiyet devri veya satın alma opsiyonu yoktur ve kira ödemelerinin bugünkü değeri binanın gerçeğe uygun değerinin küçük bir kısmıdır. Bu kiralama hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Faaliyet kiralamasıdır',
            'B': 'Kiracı için faaliyet kiralamasıdır',
            'C': 'Finansal kiralamadır',
            'D': 'Kısa vadeli kiralamadır',
            'E': 'Satış ve geri kiralamadır',
        },
        'A',
        "TFRS 16 p. 61-63'e göre kiraya veren her kiralamayı finansal veya **faaliyet kiralaması** olarak sınıflandırır; risk ve getirilerin önemli ölçüde tamamını devretmeyen kiralama faaliyet kiralamasıdır. Kiracı açısından ise TFRS 16 böyle bir ayrım yapmaz; kiracı tek model uygular.",
        'TFRS 16 p. 61, 63',
    ),
    # düzey 3
    '0029': patch(
        "Bir kiraya veren bir makineyi 5 yıllık finansal kiralamayla kiraya vermiştir; yıllık 120.000 ₺ kira her yıl sonunda tahsil edilecektir ve kiralamadaki zımni faiz oranı %8'dir. Garanti edilmemiş kalıntı değer ve başlangıçtaki doğrudan maliyet yoktur. Kiraya verenin tanıyacağı net kiralama yatırımı yaklaşık kaç ₺'dir?",
        {
            'A': '479.125',
            'B': '517.455',
            'C': '600.000',
            'D': '552.000',
            'E': '555.556',
        },
        'A',
        "TFRS 16 p. 67-68'e göre kiraya veren finansal kiralamada **net kiralama yatırımına eşit** bir alacak tanır; net yatırım, kira ödemeleri ile garanti edilmemiş kalıntı değerin **kiralamadaki zımni faiz oranıyla** iskonto edilmiş toplamıdır: ≈ **479.125 ₺**.",
        'TFRS 16 p. 67-68',
    ),
    # düzey 3
    '0030': patch(
        "Bir işletme binasını bir yatırımcıya satmış ve aynı binayı 10 yıl süreyle geri kiralamıştır. Devir TFRS 15'e göre satış koşullarını sağlamaktadır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Alıcı-kiraya veren kiraya veren muhasebesini uygular',
            'B': 'Satıcı-kiracı binayı tablo dışı bırakır',
            'C': 'Kazanç devredilen haklar kadarıyla tanınır',
            'D': 'Satıcı-kiracı satış kazancının tamamını tanır',
            'E': 'Kullanım hakkı elde tutulan hakla orantılı ölçülür',
        },
        'D',
        "TFRS 16 p. 100'e göre devir satış ise satıcı-kiracı, geri kiralamadan doğan kullanım hakkı varlığını **elde tuttuğu kullanım hakkıyla orantılı** ölçer ve **yalnızca alıcı-kiraya verene devredilen haklara ilişkin** kazanç veya kaybı tanır; satış kazancının tamamı tanınmaz.",
        'TFRS 16 p. 99-100',
    ),
    # düzey 2
    '0031': patch(
        "Bir işletme makinesini bir finansman kuruluşuna 'satmış' ve geri kiralamıştır; ancak kiralama sonunda makineyi sembolik bedelle geri alma hakkı olduğundan devir TFRS 15'e göre satış koşullarını sağlamamaktadır. Satıcı-kiracı aldığı bedeli nasıl muhasebeleştirir?",
        {
            'A': 'Satış kazancı olarak',
            'B': 'Özkaynak olarak',
            'C': 'Finansal yükümlülük olarak',
            'D': 'Kullanım hakkı olarak',
            'E': 'Hasılat olarak',
        },
        'C',
        "TFRS 16 p. 103'e göre devir satış değilse satıcı-kiracı devredilen varlığı finansal tablolarında göstermeye devam eder ve aldığı bedele eşit bir **finansal yükümlülük** (TFRS 9) tanır.",
        'TFRS 16 p. 103',
    ),
    # düzey 2
    '0032': patch(
        "Bir işletme 1 Ocak 2026'da bir depoyu 10 ay süreyle kiralamıştır; sözleşmede kiracıya depoyu kiralama sonunda satın alma opsiyonu tanınmıştır. Bu kiralama için kısa vadeli kiralama muafiyeti uygulanabilir mi?",
        {
            'A': 'Opsiyon kullanılmazsa geriye dönük uygulanır',
            'B': 'Kiraya veren onaylarsa uygulanabilir',
            'C': 'Uygulanamaz',
            'D': 'Uygulanabilir',
            'E': 'İlk 6 ay uygulanabilir',
        },
        'C',
        "TFRS 16 Ek A'ya göre kısa vadeli kiralama, **kiralama süresi 12 ay veya daha kısa** olan ve **satın alma opsiyonu içermeyen** kiralamadır. Satın alma opsiyonu bulunduğundan muafiyet uygulanamaz.",
        'TFRS 16 p. 5-8',
    ),
    # düzey 3
    '0033': patch(
        "Bir kiracının 1 Ocak'ta tanıdığı kullanım hakkı varlığı 270.000 ₺ (3 yıl süreli, mülkiyet devri yok), kira yükümlülüğü 248.685 ₺'dir; faiz oranı %10, yıl sonu kira ödemesi 100.000 ₺'dir. Kiracının ilk yıl kâr veya zararına yansıyacak toplam gider yaklaşık kaç ₺'dir?",
        {
            'A': '104.869',
            'B': '100.000',
            'C': '90.000',
            'D': '114.869',
            'E': '39.738',
        },
        'D',
        "TFRS 16'da kiracı kira gideri değil, **kullanım hakkı amortismanı ve kira yükümlülüğü faizi** tanır: 90.000 + 24.869 ≈ **114.869 ₺**. Ödenen kira yükümlülüğü azaltır, gider değildir.",
        'TFRS 16 p. 31, 36',
    ),
    # düzey 3
    '0034': patch(
        "Bir kiracının 2. yıl başındaki kira yükümlülüğü 173.554 ₺, faiz oranı %10'dur. 2. yılın faiz gideri yaklaşık kaç ₺'dir?",
        {
            'A': '82.645',
            'B': '17.355',
            'C': '34.711',
            'D': '10.000',
            'E': '24.869',
        },
        'B',
        'Faiz, yükümlülüğün kalan bakiyesi üzerinden hesaplanır: 173.554 × %10 ≈ **17.355 ₺**; yükümlülük azaldıkça faiz gideri de azalır.',
        'TFRS 16 p. 36',
    ),
    # düzey 2
    '0035': patch(
        'Bir kiracı, kiraya verenden taşınma masraflarını karşılaması için 25.000 ₺ kiralama teşviki almıştır. Bu teşvik kullanım hakkı varlığının maliyetini nasıl etkiler?',
        {
            'A': 'Gelir yazılır',
            'B': 'Maliyetten düşülür',
            'C': 'Etkilemez',
            'D': 'Maliyete eklenir',
            'E': 'Yükümlülüğe eklenir',
        },
        'B',
        "TFRS 16 p. 24(b)'ye göre kullanım hakkı varlığının maliyetine, fiilî başlangıç tarihinde veya öncesinde yapılan kira ödemelerinden **alınan kiralama teşvikleri düşülerek** kalan tutar eklenir; teşvik maliyeti azaltır.",
        'TFRS 16 p. 24(b)',
    ),
    # düzey 3
    '0036': patch(
        'Bir kiraya veren bir depoyu 4 yıllık faaliyet kiralamasıyla kiraya vermiş ve kiralamayı elde etmek için 20.000 ₺ komisyon ödemiştir. Bu başlangıçtaki doğrudan maliyet her yıl kaç ₺ giderleştirilir?',
        {
            'A': '0',
            'B': '2.000',
            'C': '20.000',
            'D': '5.000',
            'E': '10.000',
        },
        'D',
        "TFRS 16 p. 83'e göre kiraya veren faaliyet kiralamasını elde etmek için katlandığı **başlangıçtaki doğrudan maliyetleri dayanak varlığın defter değerine ekler** ve kira geliriyle aynı esasla kiralama süresi boyunca giderleştirir: 20.000 / 4 = **5.000 ₺**.",
        'TFRS 16 p. 83',
    ),
    # düzey 2
    '0037': patch(
        "Bir işletme kısa vadeli kiralama ve düşük değerli varlık muafiyetlerini uygulamak istemektedir.\n\nTFRS 16'ya göre bu muafiyetlerle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Muafiyetlerin uygulanması kiracı için isteğe bağlıdır',
            'B': 'Kısa vade muafiyeti kiralama bazında, düşük değer muafiyeti varlık sınıfı bazında seçilir',
            'C': 'Kısa vadeli kiralamada kiralama süresi 12 ay veya daha kısadır',
            'D': 'Muafiyet uygulanırsa ödemeler genellikle doğrusal esasla gider yazılır',
            'E': 'Bu muafiyetler kiraya veren için değil kiracı için tanınmıştır',
        },
        'B',
        'TFRS 16.5-8: kiracı, kısa vadeli kiralamalar (12 ay veya daha kısa) ve dayanak varlığın düşük değerli olduğu kiralamalar için muafiyet uygulamayı seçebilir; ödemeler genellikle doğrusal esasla gider yazılır. Kısa vade muafiyeti dayanak varlık SINIFI bazında, düşük değer muafiyeti ise KİRALAMA bazında seçilir.',
        'TFRS 16 p. 8',
    ),
    # düzey 3
    '0038': patch(
        'Kira ödemeleri her yıl TÜFE oranında artan bir kiralamada, kiracı gelecek yıllarda yüksek enflasyon beklemektedir. Kira yükümlülüğünün ilk ölçümünde endekse bağlı ödemeler nasıl dikkate alınır?',
        {
            'A': 'Dikkate alınmaz',
            'B': 'Kiraya verenin tahminiyle',
            'C': 'Başlangıçtaki endeks düzeyiyle',
            'D': 'Geçmiş yıllar ortalamasıyla',
            'E': 'Beklenen enflasyonla',
        },
        'C',
        "TFRS 16 p. 27(b) ve 28'e göre endekse veya orana bağlı değişken kira ödemeleri, ilk ölçümde **kiralamanın fiilen başladığı tarihteki endeks veya oran** kullanılarak ölçülür; gelecekteki endeks değişimleri tahmin edilmez, gerçekleştikçe yükümlülük yeniden ölçülür.",
        'TFRS 16 p. 27(b), 28',
    ),
    # düzey 3
    '0039': patch(
        'Aşağıdakilerden hangileri kira yükümlülüğünün ilk ölçümüne dâhil edilir?\n\nI. Gelecekte beklenen enflasyona göre tahmin edilen kira artışları\n\nII. Kiracının satışlarına bağlı değişken kira ödemeleri\n\nIII. Kullanılacağı makul ölçüde kesin satın alma opsiyonunun bedeli',
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'II ve III',
            'D': 'I ve III',
            'E': 'Yalnız III',
        },
        'E',
        "TFRS 16 p. 27(d)'ye göre makul ölçüde kesin satın alma opsiyonu bedeli (III) kira ödemelerine dâhildir. Endekse bağlı ödemeler **başlangıçtaki endeksle** ölçülür, beklenen enflasyon tahmin edilmez (I yanlış); satışlara bağlı değişken ödemeler dâhil edilmez (II yanlış).",
        'TFRS 16 p. 27-28',
    ),
    # düzey 2
    '0040': patch(
        "Aşağıdakilerden hangileri TFRS 16'ya göre doğrudur?\n\nI. Tedarikçinin esaslı ikame hakkı varsa tanımlanmış varlık yoktur\n\nII. Kiralama süresine makul ölçüde kesin uzatma opsiyonları dâhil edilir\n\nIII. Başlangıçtaki doğrudan maliyetler kullanım hakkı maliyetine eklenir",
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'I ve III',
        },
        'A',
        "TFRS 16 UR B14'e göre esaslı ikame hakkı tanımlanmış varlığı ortadan kaldırır (I); p. 18'e göre makul kesin uzatma opsiyonu süreye dâhildir (II); p. 24'e göre başlangıçtaki doğrudan maliyetler kullanım hakkı maliyetine eklenir (III).",
        'TFRS 16 p. 9, 18, 24',
    ),
    # düzey 2
    '0041': patch(
        'Bir işletme bir depoyu 5 yıllık iptal edilemez süreyle kiralamıştır; sözleşmede işletmeye 3 yıl daha uzatma opsiyonu tanınmıştır. Depo işletmenin ana dağıtım merkezidir ve opsiyonun kullanılacağı makul ölçüde kesindir. Kiralama süresi kaç yıldır?',
        {
            'A': '6',
            'B': '8',
            'C': '3',
            'D': '10',
            'E': '5',
        },
        'B',
        "TFRS 16 p. 18'e göre kiralama süresi, **iptal edilemeyen süre** ile kiracının **kullanacağı makul ölçüde kesin olan uzatma opsiyonunun** kapsadığı süreden oluşur: 5 + 3 = **8 yıl**.",
        'TFRS 16 p. 18-19, UR B34',
    ),
    # düzey 3
    '0042': patch(
        "Bir işletme 1 Ekim 2025'te bir iş makinesini 6 ay süreyle aylık 15.000 ₺'ye kiralamıştır; sözleşmede satın alma opsiyonu yoktur. İşletme kısa vadeli kiralamalar için muafiyeti seçmiştir. 2025 yılında kâr veya zarara yansıyacak kira gideri kaç ₺'dir?",
        {
            'A': '0',
            'B': '15.000',
            'C': '180.000',
            'D': '45.000',
            'E': '90.000',
        },
        'D',
        "TFRS 16 p. 5-6'ya göre **12 ay veya daha kısa süreli ve satın alma opsiyonu içermeyen** kısa vadeli kiralamalarda kiracı, kullanım hakkı varlığı ve kira yükümlülüğü tanımak yerine kira ödemelerini kiralama süresince doğrusal olarak giderleştirebilir: 3 ay × 15.000 = **45.000 ₺**.",
        'TFRS 16 p. 5-6, UR B34',
    ),
    # düzey 3
    '0043': patch(
        "Bir mağaza kiralamasında kira ödemeleri şunlardan oluşmaktadır: yıllık 200.000 ₺ sabit kira, her yıl TÜFE oranında artış ve mağaza satışlarının %2'si oranında ek kira. Kira yükümlülüğünün ilk ölçümünde hangi ödeme dikkate alınmaz?",
        {
            'A': 'Fesih cezası',
            'B': 'Sabit kira',
            'C': "TÜFE'ye bağlı artış",
            'D': 'Makul kesin satın alma bedeli',
            'E': "Satışların %2'si oranındaki ek kira",
        },
        'E',
        "TFRS 16 p. 27-28'e göre kira ödemeleri sabit ödemeleri, **bir endekse veya orana bağlı** değişken ödemeleri, makul ölçüde kesin satın alma opsiyonu bedelini ve fesih cezalarını kapsar. **Satışlar gibi performansa bağlı** değişken ödemeler yükümlülüğe dâhil edilmez; gerçekleştiği dönemde gider yazılır.",
        'TFRS 16 p. 27-28',
    ),
    # düzey 3
    '0044': patch(
        "Bir kiracı, kiralama sonunda dayanak varlığın en az 50.000 ₺ değer taşıyacağını kiraya verene taahhüt etmiştir; kiracı varlığın kiralama sonunda 42.000 ₺ değerinde olmasını ve aradaki farkı ödemeyi beklemektedir. Kira yükümlülüğüne dâhil edilecek kalıntı değer taahhüdü tutarı kaç ₺'dir?",
        {
            'A': '42.000',
            'B': '8.000',
            'C': '92.000',
            'D': '50.000',
            'E': '0',
        },
        'B',
        "TFRS 16 p. 27(c)'ye göre kira ödemelerine **kalıntı değer taahhütleri kapsamında kiracı tarafından ödenmesi beklenen tutarlar** dâhil edilir: 50.000 − 42.000 = **8.000 ₺** (bugünkü değeri alınarak).",
        'TFRS 16 p. 27(c)',
    ),
    # düzey 3
    '0045': patch(
        "Bir kiracı kullanım hakkı varlığını 270.000 ₺ maliyetle tanımıştır. Kiralama süresi 3 yıl, dayanak varlığın yararlı ömrü 8 yıldır. Kiralama sonunda mülkiyet devri veya satın alma opsiyonu yoktur. Kalıntı değer yoktur ve doğrusal yöntem uygulanmaktadır. Yıllık amortisman gideri kaç ₺'dir?",
        {
            'A': '135.000',
            'B': '270.000',
            'C': '155.455',
            'D': '146.250',
            'E': '90.000',
        },
        'E',
        "TFRS 16 p. 31-32'ye göre mülkiyet devri veya makul kesin satın alma opsiyonu yoksa kullanım hakkı varlığı, **kiralama süresi ile yararlı ömrün kısa olanı** boyunca amortismana tabi tutulur: 270.000 / 3 = **90.000 ₺**.",
        'TFRS 16 p. 31-32',
    ),
    # düzey 2
    '0046': patch(
        'Bir kiracı, kullanım hakkı varlığının maliyet modeliyle sonraki ölçümünü yapmaktadır. Varlıkta değer düşüklüğü göstergesi ortaya çıkmıştır. Kiracı değer düşüklüğünü hangi standarda göre belirler?',
        {
            'A': 'TMS 2',
            'B': 'TMS 37',
            'C': 'TFRS 13',
            'D': 'TFRS 9',
            'E': 'TMS 36',
        },
        'E',
        "TFRS 16 p. 33'e göre kiracı, kullanım hakkı varlığının değer düşüklüğüne uğrayıp uğramadığını belirlemek ve tespit edilen değer düşüklüğü zararını muhasebeleştirmek için **TMS 36 Varlıklarda Değer Düşüklüğü**'nü uygular.",
        'TFRS 16 p. 29-30, 33',
    ),
    # düzey 2
    '0047': patch(
        'Bir kiracı, başlangıçta kullanmayacağını değerlendirdiği satın alma opsiyonunu, kendi kontrolündeki önemli bir olay nedeniyle artık kullanacağının makul ölçüde kesin olduğunu belirlemiştir. Kira yükümlülüğü yeniden ölçülürken hangi iskonto oranı kullanılır?',
        {
            'A': 'Revize edilmiş iskonto oranı',
            'B': 'Sıfır oran',
            'C': 'Başlangıçtaki oran',
            'D': 'Kiraya verenin oranı',
            'E': 'Enflasyon oranı',
        },
        'A',
        "TFRS 16 p. 40'a göre kiralama süresinde veya **satın alma opsiyonunun değerlendirilmesinde değişiklik** olursa kira yükümlülüğü **revize edilmiş iskonto oranıyla** yeniden ölçülür; endeks değişikliklerinde ise oran değiştirilmez (p. 42-43).",
        'TFRS 16 p. 40',
    ),
    # düzey 3
    '0048': patch(
        "Bir kiraya veren bir depoyu 4 yıllık faaliyet kiralamasıyla kiraya vermiştir. Kiracıyı çekmek için ilk yıl kira alınmamakta, sonraki 3 yılın her birinde 120.000 ₺ kira alınmaktadır. Kiraya verenin ilk yıl kâr veya zarara yansıtacağı kira geliri kaç ₺'dir?",
        {
            'A': '360.000',
            'B': '120.000',
            'C': '0',
            'D': '30.000',
            'E': '90.000',
        },
        'E',
        "TFRS 16 p. 81'e göre kiraya veren faaliyet kiralamasından elde ettiği kira ödemelerini, başka bir sistematik esas daha uygun değilse **doğrusal olarak** gelir yazar; kira teşvikleri dâhil toplam kira süreye yayılır: 360.000 / 4 = **90.000 ₺**.",
        'TFRS 16 p. 81',
    ),
    # düzey 3
    '0049': patch(
        "Bir kiraya verenin finansal kiralamadan doğan net kiralama yatırımı 1 Ocak'ta 479.125 ₺'dir; zımni faiz oranı %8'dir. Kiraya verenin ilk yıl tanıyacağı finansman geliri yaklaşık kaç ₺'dir?",
        {
            'A': '120.000',
            'B': '81.670',
            'C': '57.495',
            'D': '38.330',
            'E': '67.060',
        },
        'D',
        "TFRS 16 p. 75'e göre kiraya veren finansman gelirini, **net kiralama yatırımı üzerinden sabit dönemsel getiri** oranını yansıtacak şekilde tanır: 479.125 × %8 ≈ **38.330 ₺**.",
        'TFRS 16 p. 75',
    ),
    # düzey 2
    '0050': patch(
        'Bir kiraya veren bir kiralamayı sınıflandırırken şu durumları değerlendirmektedir: kiralama sonunda mülkiyetin kiracıya geçmesi, kiracının varlığı gerçeğe uygun değerin çok altında bir bedelle satın alma opsiyonu, dayanak varlığın yalnızca kiracının kullanabileceği özel nitelikte olması ve kiralama süresinin 1 yıl olması. Bunlardan hangisi tek başına finansal kiralama göstergesi değildir?',
        {
            'A': 'Varlığın özel nitelikte olması',
            'B': 'Kiralama süresinin 1 yıl olması',
            'C': 'Pazarlıklı satın alma opsiyonu',
            'D': "Bugünkü değerin GUD'ye yakın olması",
            'E': 'Mülkiyetin kiracıya geçmesi',
        },
        'B',
        "TFRS 16 p. 63'e göre mülkiyet devri, pazarlıklı satın alma opsiyonu, sürenin ekonomik ömrün büyük bölümünü kapsaması, bugünkü değerin gerçeğe uygun değerin önemli ölçüde tamamına ulaşması ve varlığın **özel nitelikte** olması finansal kiralama göstergeleridir. Kısa süre ise faaliyet kiralamasını işaret eder.",
        'TFRS 16 p. 63',
    ),
    # düzey 2
    '0051': patch(
        'Bir işletme kiraladığı ofis katını, kalan kiralama süresinin tamamı için başka bir şirkete alt kiralamaya vermiştir. Alt kiralama, ana kiralamadan doğan kullanım hakkı varlığına göre sınıflandırılır ve sahipliğe ilişkin risk ve getirilerin önemli ölçüde tamamını devretmektedir. Ara kiraya veren alt kiralamayı nasıl sınıflandırır?',
        {
            'A': 'Kısa vadeli kiralama',
            'B': 'Satış ve geri kiralama',
            'C': 'Finansal kiralama',
            'D': 'Faaliyet kiralaması',
            'E': 'Kiralama değildir',
        },
        'C',
        "TFRS 16 UR B58'e göre ara kiraya veren alt kiralamayı **ana kiralamadan doğan kullanım hakkı varlığına göre** sınıflandırır; kalan sürenin tamamı için risk ve getiriler devredildiğinden alt kiralama **finansal kiralamadır**.",
        'TFRS 16 UR B58',
    ),
    # düzey 3
    '0052': patch(
        'Bir kiracı ile kiraya veren, mevcut 5 yıllık kiralamaya ayrı bir fiyatla ve bağımsız fiyatına uygun bedelle ek bir depo alanı eklemek için sözleşmeyi değiştirmiştir. Bu değişiklik nasıl muhasebeleştirilir?',
        {
            'A': 'Tahmin değişikliği olarak',
            'B': 'Mevcut kiralamanın yeniden ölçümü olarak',
            'C': 'Hata düzeltmesi olarak',
            'D': 'Dipnot açıklamasıyla',
            'E': 'Ayrı bir kiralama olarak',
        },
        'E',
        "TFRS 16 p. 44'e göre değişiklik **bir veya daha fazla dayanak varlığı kullanma hakkı ekleyerek kiralamanın kapsamını artırıyor** ve bedel bu kapsam artışının tek başına fiyatıyla orantılı artıyorsa, değişiklik **ayrı bir kiralama** olarak muhasebeleştirilir.",
        'TFRS 16 p. 44-46',
    ),
    # düzey 2
    '0053': patch(
        'Bir kiracı dipnotlarında kullanım hakkı varlıklarına ilişkin amortisman giderlerini dayanak varlık sınıfları itibarıyla, kira yükümlülüklerinin faiz giderini ve kısa vadeli kiralamalara ilişkin giderleri açıklamaktadır. Bu açıklamalar hangi standardın gereğidir?',
        {
            'A': 'TMS 1',
            'B': 'TMS 7',
            'C': 'TMS 17',
            'D': 'TFRS 9',
            'E': 'TFRS 16',
        },
        'E',
        "Kiracının kullanım hakkı amortismanı, kira yükümlülüğü faizi, kısa vadeli ve düşük değerli kiralama giderleri ve değişken kira ödemelerine ilişkin açıklamaları **TFRS 16 p. 53**'te düzenlenmiştir; TMS 17 TFRS 16 ile yürürlükten kalkmıştır.",
        'TFRS 16 p. 53',
    ),
    # düzey 2
    '0054': patch(
        'Bir kiraya veren bir makineyi finansal kiralamayla kiraya vermiştir. Kiralamanın başlangıcında kiraya veren finansal durum tablosunda dayanak varlığın yerine hangi kalemi gösterir?',
        {
            'A': 'Stok',
            'B': 'Peşin ödenmiş gider',
            'C': 'Kullanım hakkı varlığı',
            'D': 'Kiralama alacağı',
            'E': 'Maddi duran varlık',
        },
        'D',
        "TFRS 16 p. 67'ye göre kiraya veren, finansal kiralamaya konu varlıkları finansal durum tablosunda **net kiralama yatırımına eşit tutarda alacak** olarak gösterir; dayanak varlık tablo dışı bırakılır.",
        'TFRS 16 p. 67',
    ),
    # düzey 3
    '0055': patch(
        'Bir işletme bir binayı 10 yıllık sözleşmeyle kiralamıştır; sözleşme kiracıya 6. yılın sonunda cezasız fesih hakkı vermektedir. Bina işletmenin üretim tesisidir ve kiracının bu fesih opsiyonunu kullanmayacağı makul ölçüde kesindir. Kiralama süresi kaç yıldır?',
        {
            'A': '6',
            'B': '4',
            'C': '10',
            'D': '16',
            'E': '5',
        },
        'C',
        "TFRS 16 p. 18'e göre kiralama süresi, iptal edilemeyen süreye ek olarak kiracının **kullanmayacağı makul ölçüde kesin olan fesih opsiyonunun** kapsadığı süreyi de içerir: 6 + 4 = **10 yıl**.",
        'TFRS 16 p. 18, UR B34-B35',
    ),
    # düzey 3
    '0056': patch(
        "Bir işletme defter değeri 600.000 ₺ olan binasını gerçeğe uygun değeri olan 1.000.000 ₺'ye satmış ve hemen geri kiralamıştır. Geri kiralamadaki kira ödemelerinin bugünkü değeri 300.000 ₺'dir; devir TFRS 15'e göre satıştır. Satıcı-kiracının tanıyacağı satış kazancı kaç ₺'dir?",
        {
            'A': '280.000',
            'B': '180.000',
            'C': '120.000',
            'D': '400.000',
            'E': '100.000',
        },
        'A',
        "Elde tutulan hak oranı 300.000 / 1.000.000 = %30; kullanım hakkı 600.000 × %30 = 180.000 ₺ olarak ölçülür. Toplam kazanç 400.000 ₺'nin **yalnız devredilen haklara ilişkin** %70'lik kısmı tanınır: **280.000 ₺**.",
        'TFRS 16 p. 100(a)',
    ),
    # düzey 2
    '0057': patch(
        "Bir işletme bir iş makinesi kiralama sözleşmesini 1 Mart'ta imzalamıştır; kiraya veren makineyi 1 Mayıs'ta işletmenin kullanımına hazır hâle getirmiştir. İlk kira ödemesi 1 Haziran'da yapılacaktır. Kiracı kullanım hakkı varlığını ve kira yükümlülüğünü hangi tarihte finansal tablolara alır?",
        {
            'A': '1 Mart',
            'B': '1 Haziran',
            'C': 'Sözleşme süresinin ortası',
            'D': '31 Aralık',
            'E': '1 Mayıs',
        },
        'E',
        "TFRS 16 Ek A ve p. 22'ye göre kiracı, kullanım hakkı varlığını ve kira yükümlülüğünü **kiralamanın fiilen başladığı tarihte**, yani kiraya verenin dayanak varlığı kiracının kullanımına hazır hâle getirdiği tarihte tanır.",
        'TFRS 16 Ek A, p. 22',
    ),
    # düzey 3
    '0058': patch(
        "Bir işletme, kendi binalarını TMS 16'daki yeniden değerleme modeliyle ölçmektedir. İşletme ayrıca bir ofis binası kiralamış ve bu kiralamadan doğan kullanım hakkı varlığı binalar sınıfıyla ilişkilidir. Kiracı bu kullanım hakkı varlığına hangi ölçüm modelini uygulayabilir?",
        {
            'A': 'Yeniden değerleme modelini',
            'B': 'Net gerçekleşebilir değeri',
            'C': 'Özkaynak yöntemini',
            'D': 'Gerçeğe uygun değer modelini',
            'E': 'İtfa edilmiş maliyeti',
        },
        'A',
        "TFRS 16 p. 35'e göre kullanım hakkı varlıkları, kiracının **TMS 16'daki yeniden değerleme modelini uyguladığı** maddi duran varlık sınıfıyla ilişkiliyse, kiracı o sınıftaki bütün kullanım hakkı varlıklarına **yeniden değerleme modelini uygulamayı seçebilir**.",
        'TFRS 16 p. 35',
    ),
    # düzey 3
    '0059': patch(
        'Kiraya veren muhasebesine ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Faaliyet kiralamasına konu varlık kiraya verenin tablolarında kalır\n\nII. Finansal kiralamada kiraya veren net kiralama yatırımına eşit alacak tanır\n\nIII. Faaliyet kiralaması geliri tahsil edildiği dönemde tanınır',
        {
            'A': 'II ve III',
            'B': 'I, II ve III',
            'C': 'Yalnız II',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'D',
        "TFRS 16 p. 88'e göre faaliyet kiralamasına konu varlık kiraya verende kalır (I); p. 67'ye göre finansal kiralamada net yatırıma eşit alacak tanınır (II). p. 81'e göre faaliyet kiralaması geliri tahsilata göre değil **genellikle doğrusal esasla** tanınır (III yanlış).",
        'TFRS 16 p. 61-63, 67, 81, 88',
    ),
    # düzey 2
    '0060': patch(
        'Aşağıdakilerden hangileri düşük değerli varlık muafiyetine ilişkin olarak doğrudur?\n\nI. Değerlendirme varlığın kullanılmış hâldeki değerine göre yapılır\n\nII. Muafiyet kiralama süresinden bağımsızdır\n\nIII. Yeni bir otomobil genellikle düşük değerli sayılır',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'I, II ve III',
            'D': 'Yalnız II',
            'E': 'Yalnız I',
        },
        'D',
        "TFRS 16 UR B3-B6'ya göre düşük değerli varlık muafiyeti kiralama süresinden bağımsızdır (II). Değerlendirme varlığın **yeni olduğundaki** değerine göre yapılır (I yanlış); yeni bir otomobil **düşük değerli sayılmaz** (III yanlış).",
        'TFRS 16 p. 5, UR B3-B7',
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
    print(f"1 paket / {len(PATCHES)} soru ('TFRS 16 Kiralamalar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
