#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Muhasebe Standartları — sayısal uygulama kalibrasyonu.

Ölçülen sapma: standart paketlerinde sayısal senaryo oranı %6 iken 2026 SGS'nin
finansal muhasebe + standartlar bloğunda %57,7; öncüllü oran %15 iken %3,8'dir
(bkz. reports/SGS_CIKMIS_SORULAR_ANALIZI_2026-07-22.md, URETIM_KURALLARI §1-§2).
Bu builder, kavram sorularını standardın hükmünü UYGULATAN sayısal senaryolara çevirir
ve öncül oranını düşürür. Aritmetik builder dışında bağımsız doğrulanmıştır.
§5 gereği doğru şıkkın boy sırası dağıtılır (bir kısmı uzun, bir kısmı kısa). ID'ler korunur.

    --check : iki repoyu karşılaştır (fark varsa çıkış 1)
    --write : içerik + uygulama repolarına yaz
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
CERCEVE_RELATIVE_PATH = 'content/muhasebe_standartlari/kavramsal_cerceve.json'
STYLE_REF = 'SGS Muhasebe Standartları (sayısal uygulama; 2026 sınav profiline kalibre)'


def std_patch(stem, options, answer, solution, legislation_ref):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF, "legislationRef": legislation_ref},
        "validYear": 2026, "mockExamId": None,
    }


CERCEVE_PATCHES = {
    'std-cerceve-gen-0030': std_patch(
        "Bir işletmenin dönem sonu itibarıyla toplam varlıkları 1.850.000 ₺, toplam borçları ise 1.130.000 ₺'dir. Kavramsal Çerçeve'deki özkaynak tanımına göre işletmenin özkaynağı kaç ₺'dir?",
        {
            'A': '2.980.000',
            'B': '1.130.000',
            'C': '720.000',
            'D': '1.850.000',
            'E': '620.000',
        },
        'C',
        "Kavramsal Çerçeve'ye göre **özkaynak, işletmenin tüm borçları düşüldükten sonra varlıkları üzerinde kalan paydır**: 1.850.000 − 1.130.000 = **720.000 ₺**. Özkaynak bağımsız olarak ölçülmez; varlık ve borç ölçümlerinin artık (kalıntı) sonucudur.",
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0031': std_patch(
        "Bir işletmenin özkaynağı dönem başında 400.000 ₺, dönem sonunda 520.000 ₺'dir. Dönem içinde ortaklardan 30.000 ₺ sermaye katkısı alınmış, ortaklara 20.000 ₺ kâr payı dağıtılmıştır. Kavramsal Çerçeve'nin gelir-gider tanımına göre dönemin kâr veya zararı kaç ₺'dir?",
        {
            'A': '110.000 ₺ kâr',
            'B': '120.000 ₺ kâr',
            'C': '130.000 ₺ kâr',
            'D': '70.000 ₺ kâr',
            'E': '90.000 ₺ kâr',
        },
        'A',
        'Gelir ve gider tanımları **ortakların katkı ve dağıtımlarını kapsam dışı bırakır**. Dönem kârı = (Dönem sonu özkaynak − Dönem başı özkaynak) − sermaye katkısı + kâr payı dağıtımı = (520.000 − 400.000) − 30.000 + 20.000 = **110.000 ₺**. (Katkı ve dağıtımı düzeltmeden 120.000 ₺ bulunur.)',
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0032': std_patch(
        "Bir işletmede dönem içinde varlıklar 260.000 ₺ artmış, borçlar 90.000 ₺ artmıştır. Aynı dönemde ortaklardan 50.000 ₺ sermaye katkısı alınmış, ortaklara dağıtım yapılmamıştır. Kavramsal Çerçeve'ye göre dönemin geliri gideri aşan kısmı (kâr) kaç ₺'dir?",
        {
            'A': '170.000',
            'B': '220.000',
            'C': '70.000',
            'D': '120.000',
            'E': '260.000',
        },
        'D',
        "Özkaynak değişimi = varlık artışı − borç artışı = 260.000 − 90.000 = 170.000 ₺. Bu artışın 50.000 ₺'si **ortak katkısıdır** ve gelir tanımına girmez. Kâr = 170.000 − 50.000 = **120.000 ₺**.",
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0035': std_patch(
        "Bir işletmenin dönem başı özkaynağı 900.000 ₺, dönem sonu özkaynağı 1.020.000 ₺'dir. Dönem içinde ortaklara 80.000 ₺ kâr payı dağıtılmış, ortaklardan katkı alınmamıştır. İşletmenin dönem kârı kaç ₺'dir?",
        {
            'A': '120.000',
            'B': '200.000',
            'C': '40.000',
            'D': '80.000',
            'E': '1.100.000',
        },
        'B',
        'Ortaklara yapılan dağıtımlar gider değildir; özkaynağı azaltır ancak kâr hesabına girmez. Dönem kârı = (1.020.000 − 900.000) + 80.000 = **200.000 ₺**. (Dağıtımı eklemeden yalnız 120.000 ₺ bulunur.)',
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0036': std_patch(
        "Bir işletme, üç yıllık bir sözleşmeyle kiraladığı binayı sözleşme süresince kullanma hakkına sahiptir; hakkın sözleşme başlangıcındaki değeri 450.000 ₺ olarak ölçülmüştür. Binanın mülkiyeti kiraya verende kalmaktadır. Kavramsal Çerçeve'nin varlık tanımı bakımından bu durum nasıl değerlendirilir?",
        {
            'A': 'Mülkiyet kiraya verende olduğundan kiracının varlığı yoktur; hiçbir tutar tabloya alınmaz',
            'B': 'Kullanma hakkı ancak binanın tamamı satın alınırsa varlık sayılır',
            'C': 'Kiracı binanın tamamını 450.000 ₺ üzerinden varlık olarak kaydeder',
            'D': 'Kullanma hakkı kontrol edilen ekonomik kaynaktır; 450.000 ₺ varlık olarak alınabilir',
            'E': 'Kullanma hakkı yalnızca dipnotlarda açıklanır, ölçülmez',
        },
        'D',
        "Kavramsal Çerçeve'de varlık, **kontrol edilen ekonomik kaynaktır**; mülkiyet şart değildir. Kiracı, binanın kendisini değil **kullanma hakkını** kontrol eder ve bu hak 450.000 ₺ ile ölçülebiliyorsa varlık olarak finansal tablolara alınabilir. Binanın tamamının kaydedilmesi ise kontrol edilmeyen bir kaynağı kaydetmek olurdu.",
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0037': std_patch(
        "Bir işletme, müşterisine karşı açtığı davadan 300.000 ₺ tahsilat beklemektedir; ancak davanın sonucu ve tahsil edilecek tutar yüksek belirsizlik taşımaktadır. 2018 Kavramsal Çerçevesi'ndeki finansal tablolara alma ölçütleri bakımından doğru değerlendirme hangisidir?",
        {
            'A': 'Belirsizlik ne olursa olsun 300.000 ₺ mutlaka varlık olarak kaydedilir',
            'B': "Tahsil olasılığı %50'yi aştığı anda kayıt zorunludur",
            'C': 'Bilgi ihtiyaca uygun değilse 300.000 ₺ tabloya alınmayabilir',
            'D': 'Dava sonuçlanmadan hiçbir açıklama yapılamaz',
            'E': 'Tutarın yarısı olan 150.000 ₺ kaydedilir',
        },
        'C',
        '2018 Kavramsal Çerçevesi finansal tablolara almada **sabit bir olasılık eşiği aramaz**; ölçüt, kalemin varlık/borç tanımını karşılaması **ve** üretilecek bilginin ihtiyaca uygun, gerçeğe uygun sunum sağlayan nitelikte olmasıdır. Ölçüm belirsizliği çok yüksekse kayıt yerine açıklama daha uygun olabilir.',
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0038': std_patch(
        "Defter değeri 260.000 ₺ olan bir makineyi işletme 300.000 ₺'ye satmış ve makine üzerindeki kontrolünü tümüyle yitirmiştir. Kavramsal Çerçeve'nin finansal tablo dışı bırakma hükmü bakımından doğru değerlendirme hangisidir?",
        {
            'A': 'Kontrol sona erdiğinden varlık tablo dışı bırakılır ve 40.000 ₺ tutarında kazanç doğar',
            'B': 'Varlık tabloda kalmaya devam eder; yalnızca 300.000 ₺ hasılat yazılır',
            'C': 'Varlık tablo dışı bırakılır ve 300.000 ₺ kazanç doğar',
            'D': 'Kontrol sona erse de varlık amortisman süresi bitene kadar tabloda tutulur',
            'E': 'Tablo dışı bırakma yalnızca varlık bedelsiz devredilirse yapılır',
        },
        'A',
        'Bir varlık, işletme onun üzerindeki **kontrolü kaybettiğinde** finansal tablo dışı bırakılır. Satış bedeli ile defter değeri arasındaki fark sonuca yansır: 300.000 − 260.000 = **40.000 ₺ kazanç**. Kazanç, satış bedelinin tamamı değildir.',
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0043': std_patch(
        "Bir makine 2023 yılında 800.000 ₺'ye edinilmiş olup bugüne kadar ayrılan birikmiş amortisman 240.000 ₺'dir. Aynı makinenin bugünkü piyasa çıkış fiyatı 690.000 ₺, işletmedeki kullanımından beklenen nakit akışlarının bugünkü değeri 640.000 ₺, eşdeğerinin bugün edinme bedeli ise 900.000 ₺'dir. Makinenin TARİHİ MALİYET esasına göre ölçülen değeri kaç ₺'dir?",
        {
            'A': '690.000',
            'B': '640.000',
            'C': '900.000',
            'D': '800.000',
            'E': '560.000',
        },
        'E',
        'Tarihi maliyet esasında varlık, **edinme bedelinden birikmiş amortisman (ve varsa değer düşüklüğü) düşülerek** ölçülür: 800.000 − 240.000 = **560.000 ₺**. Diğer tutarlar cari değer esaslarına (gerçeğe uygun değer, kullanım değeri, cari maliyet) aittir.',
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0044': std_patch(
        "Bir varlığın edinme bedeli 500.000 ₺, edinmeye ilişkin doğrudan işlem maliyetleri 25.000 ₺'dir. Varlık için bugüne kadar 105.000 ₺ amortisman ayrılmıştır. Tarihi maliyet esasına göre varlığın güncel defter değeri kaç ₺'dir?",
        {
            'A': '395.000',
            'B': '420.000',
            'C': '525.000',
            'D': '500.000',
            'E': '605.000',
        },
        'B',
        'Tarihi maliyet, edinme bedeline **doğrudan işlem maliyetlerini** de içerir: 500.000 + 25.000 = 525.000 ₺. Birikmiş amortisman düşülünce defter değeri = 525.000 − 105.000 = **420.000 ₺**. (İşlem maliyetini ihmal etmek 395.000 ₺ verir.)',
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0045': std_patch(
        "Bir varlığın ölçüm tarihinde piyasa katılımcıları arasındaki olağan bir işlemde satılması hâlinde elde edilecek fiyat 460.000 ₺, bu satışa ilişkin tahmini işlem maliyetleri 15.000 ₺'dir. Kavramsal Çerçeve'ye göre varlığın GERÇEĞE UYGUN DEĞERİ kaç ₺'dir?",
        {
            'A': '445.000',
            'B': '475.000',
            'C': '15.000',
            'D': '460.000',
            'E': '230.000',
        },
        'D',
        'Gerçeğe uygun değer, ölçüm tarihinde piyasa katılımcıları arasındaki olağan işlemde varlığın satışından elde edilecek **çıkış fiyatıdır**: **460.000 ₺**. İşlem maliyetleri gerçeğe uygun değerin ölçümünde **düşülmez**; bunlar varlığa özgü değil işleme özgüdür. (Düşülseydi 445.000 ₺ bulunurdu.)',
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0046': std_patch(
        "Bir işletme, sahip olduğu özel amaçlı makineden gelecek üç yılda sırasıyla 200.000 ₺, 180.000 ₺ ve 150.000 ₺ nakit akışı beklemektedir. Bu akışların bugünkü değeri toplam 430.000 ₺ olarak hesaplanmıştır. Makinenin piyasadaki çıkış fiyatı ise 380.000 ₺'dir. Kavramsal Çerçeve'ye göre makinenin KULLANIM DEĞERİ kaç ₺'dir?",
        {
            'A': '380.000',
            'B': '530.000',
            'C': '430.000',
            'D': '150.000',
            'E': '50.000',
        },
        'C',
        'Kullanım değeri, varlığın **kullanımından ve nihai elden çıkarılmasından beklenen nakit akışlarının bugünkü değeridir** ve işletmeye özgüdür: **430.000 ₺**. Piyasadaki çıkış fiyatı (380.000 ₺) ise gerçeğe uygun değerdir; iki ölçüm birbirinden farklı olabilir.',
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0047': std_patch(
        "Bir işletmenin elindeki makinenin eşdeğerini bugün edinmek için ödenecek bedel 700.000 ₺, bu edinmeye ilişkin işlem maliyetleri 30.000 ₺'dir. Makinenin defter değeri 480.000 ₺, piyasa çıkış fiyatı 650.000 ₺'dir. Kavramsal Çerçeve'ye göre makinenin CARİ MALİYETİ kaç ₺'dir?",
        {
            'A': '730.000',
            'B': '700.000',
            'C': '650.000',
            'D': '480.000',
            'E': '670.000',
        },
        'A',
        'Cari maliyet, eşdeğer bir varlığın ölçüm tarihinde edinilmesi için ödenecek bedele **edinmeye ilişkin işlem maliyetlerinin eklenmesiyle** bulunan bir **giriş fiyatıdır**: 700.000 + 30.000 = **730.000 ₺**. Çıkış fiyatı olan 650.000 ₺ gerçeğe uygun değerdir.',
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0050': std_patch(
        "Bir varlığın gerçeğe uygun değeri 520.000 ₺, kullanım değeri 585.000 ₺'dir. Bu iki ölçümün farkı ve niteliği bakımından doğru değerlendirme hangisidir?",
        {
            'A': "65.000 ₺'lik fark her zaman ölçüm hatasıdır; iki değer eşit olmalıdır",
            'B': 'Kullanım değeri her koşulda gerçeğe uygun değerin altında olmak zorundadır',
            'C': "65.000 ₺'lik fark, kullanım değerinin işletmeye özgü olmasından doğar",
            'D': 'Gerçeğe uygun değer işletmeye özgü, kullanım değeri piyasaya özgü bir ölçümdür',
            'E': 'İki ölçüm arasındaki fark doğrudan kâr olarak sonuca yansıtılır',
        },
        'C',
        'Fark = 585.000 − 520.000 = 65.000 ₺. **Kullanım değeri işletmeye özgüdür** (işletmenin kendi kullanımından beklediği nakit akışları); **gerçeğe uygun değer piyasa katılımcılarının bakış açısını** yansıtan çıkış fiyatıdır. Bu nedenle iki ölçüm farklılaşabilir; fark ölçüm hatası değildir ve kendiliğinden kâr yazılmaz.',
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0057': std_patch(
        "Bir işletme dönem başında 100 birim stoka sahiptir; birim maliyeti 100 ₺ (toplam 10.000 ₺) ve bu tutar işletmenin tüm özkaynağını oluşturmaktadır. Stokun tamamı dönem içinde 15.000 ₺'ye satılmıştır. Dönem sonunda aynı stokun birim maliyeti 120 ₺'ye yükselmiştir. FİNANSAL (nakdi) sermayenin korunması yaklaşımına göre dönem kârı kaç ₺'dir?",
        {
            'A': '3.000',
            'B': '5.000',
            'C': '2.000',
            'D': '15.000',
            'E': '12.000',
        },
        'B',
        'Finansal sermayenin korunmasında kâr, dönem sonu net varlıkların **parasal tutarının** dönem başı parasal tutarı aşan kısmıdır: 15.000 − 10.000 = **5.000 ₺**. Fiyat artışı dikkate alınmaz; fiziki sermaye yaklaşımında ise kâr 3.000 ₺ olurdu.',
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0058': std_patch(
        "Dönem başı özkaynağı 10.000 ₺ olan bir işletme, 100 birimlik stokunun tamamını 15.000 ₺'ye satmıştır. Dönem sonunda aynı üretim kapasitesini yeniden edinmek için 100 birim stokun maliyeti 120 ₺/birimdir. FİZİKİ sermayenin korunması yaklaşımına göre dönem kârı kaç ₺'dir?",
        {
            'A': '5.000',
            'B': '2.000',
            'C': '12.000',
            'D': '3.000',
            'E': '15.000',
        },
        'D',
        'Fiziki sermayenin korunmasında kâr, ancak işletmenin **üretim kapasitesi korunduktan sonra** kalan tutardır. Kapasiteyi korumak için gereken tutar = 100 × 120 = 12.000 ₺. Kâr = 15.000 − 12.000 = **3.000 ₺**. Aradaki 2.000 ₺ kâr değil, sermayenin korunması düzeltmesi olarak özkaynakta izlenir.',
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0059': std_patch(
        "Bir işletmenin dönem kârı finansal sermayenin korunması yaklaşımına göre 5.000 ₺, fiziki sermayenin korunması yaklaşımına göre 3.000 ₺ hesaplanmıştır. Aradaki 2.000 ₺'lik farkın niteliği bakımından doğru değerlendirme hangisidir?",
        {
            'A': 'Fark bir hesaplama hatasıdır; iki yaklaşım her zaman aynı kârı vermelidir',
            'B': 'Fark, dönemin ek vergi yükümlülüğünü gösterir',
            'C': 'Fark, kapasiteyi korumak için gereken tutardır; kâr değil özkaynak düzeltmesidir',
            'D': 'Fark, ortaklara dağıtılması zorunlu asgari kâr payıdır',
            'E': 'Fark, fiziki sermaye yaklaşımında doğrudan gelir olarak raporlanır',
        },
        'C',
        'İki yaklaşım arasındaki fark (5.000 − 3.000 = **2.000 ₺**), varlık fiyatlarındaki artış nedeniyle **üretim kapasitesini korumak için gereken tutardır**. Fiziki sermayenin korunmasında bu tutar kâr sayılmaz; sermayenin korunması düzeltmesi olarak özkaynakta tutulur.',
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0041': std_patch(
        "Bir işletmenin dönem içinde varlıkları 340.000 ₺ artmış, borçları 120.000 ₺ azalmıştır. Aynı dönemde ortaklara 60.000 ₺ kâr payı dağıtılmış, ortaklardan katkı alınmamıştır. Kavramsal Çerçeve'ye göre dönemin kârı kaç ₺'dir?",
        {
            'A': '520.000',
            'B': '460.000',
            'C': '400.000',
            'D': '220.000',
            'E': '280.000',
        },
        'A',
        'Özkaynak değişimi = varlık artışı + borç azalışı = 340.000 + 120.000 = 460.000 ₺. Ortaklara dağıtım gider değildir; özkaynağı azalttığı için kâr hesabına **geri eklenir**: 460.000 + 60.000 = **520.000 ₺**.',
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0049': std_patch(
        "Bir varlık için şu ölçümler yapılmıştır: piyasa çıkış fiyatı 640.000 ₺, işletmeye özgü nakit akışlarının bugünkü değeri 700.000 ₺, eşdeğerini bugün edinme bedeli 750.000 ₺, edinme tarihindeki maliyeti 800.000 ₺ (birikmiş amortisman 300.000 ₺). Bu ölçümlerden hangisi Kavramsal Çerçeve'de TARİHİ MALİYET esasına, diğerleri cari değer esaslarına aittir?",
        {
            'A': '800.000 ₺ tarihi maliyettir; diğerlerinin tamamı gerçeğe uygun değerdir',
            'B': '640.000 ₺ tarihi maliyettir; diğerleri tarihi maliyetin türevleridir',
            'C': "750.000 ₺ tarihi maliyettir; kullanım değeri ise 640.000 ₺'dir",
            'D': "700.000 ₺ tarihi maliyettir; cari maliyet 640.000 ₺'dir",
            'E': '500.000 ₺ tarihi maliyettir; 640.000, 700.000 ve 750.000 ₺ sırasıyla gerçeğe uygun değer, kullanım değeri ve cari maliyettir',
        },
        'E',
        'Tarihi maliyet esasında varlık, edinme bedelinden birikmiş amortisman düşülerek ölçülür: 800.000 − 300.000 = **500.000 ₺**. Cari değer esasları ise **gerçeğe uygun değer** (çıkış fiyatı 640.000 ₺), **kullanım değeri** (işletmeye özgü bugünkü değer 700.000 ₺) ve **cari maliyet** (giriş fiyatı 750.000 ₺) olarak ayrılır.',
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0052': std_patch(
        "Bir işletmenin varlıkları 2.400.000 ₺, borçları 1.500.000 ₺'dir. Dönem içinde ortaklardan 100.000 ₺ katkı alınmış, 40.000 ₺ kâr payı dağıtılmıştır. Dönem başı özkaynak 760.000 ₺ olduğuna göre dönem kârı kaç ₺'dir?",
        {
            'A': '140.000',
            'B': '80.000',
            'C': '20.000',
            'D': '900.000',
            'E': '180.000',
        },
        'B',
        'Dönem sonu özkaynak = 2.400.000 − 1.500.000 = 900.000 ₺. Dönem kârı = (900.000 − 760.000) − ortak katkısı 100.000 + dağıtım 40.000 = **80.000 ₺**. Ortak işlemleri gelir-gider tanımına girmediğinden düzeltilir.',
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
    'std-cerceve-gen-0060': std_patch(
        "Bir işletmenin ticari alacağı 180.000 ₺, aynı müşteriye olan ticari borcu 110.000 ₺'dir; taraflar arasında yasal bir netleştirme hakkı bulunmamaktadır. Kavramsal Çerçeve'nin sunum ve açıklama ilkeleri bakımından doğru sunum hangisidir?",
        {
            'A': 'Aradaki 70.000 ₺ net alacak olarak tek kalemde sunulur',
            'B': 'Yalnızca büyük olan 180.000 ₺ sunulur, borç dipnotta açıklanır',
            'C': 'İki tutar toplanarak 290.000 ₺ olarak sunulur',
            'D': 'Alacak 180.000 ₺ ve borç 110.000 ₺ ayrı ayrı sunulur; netleştirme yapılmaz',
            'E': 'Netleştirme her durumda serbest olduğundan işletme dilediği sunumu seçebilir',
        },
        'D',
        "Varlık ve borçların **mahsup edilerek (netleştirilerek)** sunulması, kalemlerin ayrı ayrı ölçülmesi ilkesinden sapma yarattığı için kural olarak uygun değildir. Yasal netleştirme hakkı bulunmadığından alacak **180.000 ₺** ve borç **110.000 ₺** ayrı sunulur; 70.000 ₺'lik net gösterim bilgiyi gizler.",
        'Finansal Raporlamaya İlişkin Kavramsal Çerçeve',
    ),
}

PATCHES_BY_PATH = {
    CERCEVE_RELATIVE_PATH: CERCEVE_PATCHES,
}


def apply_or_check(path, patches, write):
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    by_id = {q["id"]: q for q in questions}
    mismatches = []
    for qid, fields in patches.items():
        q = by_id.get(qid)
        if q is None:
            raise SystemExit(f"Soru bulunamadı: {path}::{qid}")
        for field, expected in fields.items():
            if q.get(field) != expected:
                mismatches.append(f"{path}::{qid}.{field}")
                if write:
                    q[field] = expected
        if write and len(set(q["options"].values())) != 5:
            raise SystemExit(f"Seçenek çakışması: {path}::{qid}")
    if write:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return mismatches


def main():
    ap = argparse.ArgumentParser(); g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true"); g.add_argument("--write", action="store_true")
    args = ap.parse_args()
    mismatches = []
    for rel, patches in PATCHES_BY_PATH.items():
        for path in (ROOT / rel, APP_ROOT / rel):
            mismatches.extend(apply_or_check(path, patches, args.write))
    if args.check and mismatches:
        print("Eşleşmeyen alanlar:")
        for m in mismatches: print(f"- {m}")
        return 1
    total = sum(len(p) for p in PATCHES_BY_PATH.values())
    print(f"{len(PATCHES_BY_PATH)} paket / {total} soru (standartlar sayısal kalibrasyonu) iki repoda doğrulandı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
