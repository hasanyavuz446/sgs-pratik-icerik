#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TMS 37 Karsiliklar, Kosullu Borclar ve Kosullu Varliklar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gercek sinav profiliyle yeniden yazim (senaryo kok + kisa sik). Eski surum 87 mutlak ifadeli celdirici tasiyordu (kor %38). Kapsam: tanima olcutleri ve muhtemel esigi, yasal/zimni yukumluluk, gelecekteki eylemlerle kacinilabilen maliyetler (filtre, bakim, kendi kendini sigorta), yasalasmasi neredeyse kesin kanun, kosullu borc/varlik ve aciklama esikleri, kefalet, muteselsil sorumluluk, olcum (beklenen deger, en olasi sonuc, bugunku deger ve iskontonun cozulmesi, gelecek olaylar, varlik satis kazanclari), geri odemeler, karsiliklarin guncellenmesi ve kullanimi, faaliyet zararlari, dezavantajli sozlesmeler (2022 ifa maliyeti), yeniden yapilandirma, soküm/restorasyon, aciklamalar. 13 hesap sorusu modulde hesaplandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: TMS 37 Karsiliklar, Kosullu Borclar ve Kosullu Varliklar (KGK, 2022 degisikligi dahil) ve Ek C ornekleri; TMS 16 p. 16
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/tms_37_karsiliklar.json"
STYLE_REF = 'SGS Muhasebe Standartlari (gercek sinav profiline kalibre: senaryo kok + kisa sik)'
ONEK = "std-tms37-gen-"


def patch(stem, options, answer, solution, ref='TMS 37 Karsiliklar, Kosullu Borclar ve Kosullu Varliklar'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Bir işletme aleyhine açılan tazminat davasında hukuk müşaviri, davanın kaybedilme olasılığını %65 olarak değerlendirmiştir; dava 2025'te meydana gelen bir olaya dayanmaktadır ve tazminat tutarı güvenilir biçimde tahmin edilebilmektedir. İşletme 31.12.2025 tablolarında ne yapar?",
        {
            'A': 'Gelecek yıl gider yazılır',
            'B': 'Koşullu varlık olarak açıklanır',
            'C': 'Özkaynaktan düşülür',
            'D': 'Karşılık tanınır',
            'E': 'Koşullu borç olarak açıklanır',
        },
        'D',
        "TMS 37 p. 14'e göre geçmiş olaydan kaynaklanan mevcut yükümlülük varsa, kaynak çıkışı **muhtemelse** (p. 23: gerçekleşme olasılığı gerçekleşmeme olasılığından yüksek) ve tutar güvenilir tahmin edilebiliyorsa karşılık tanınır.",
        'TMS 37 p. 14, 23',
    ),
    # düzey 3
    '0002': patch(
        'Bir işletme, rakibine karşı açtığı patent davasını kazanacağını ve 400.000 ₺ tazminat alacağını muhtemel görmektedir; ancak karar kesinleşmemiştir ve tahsilat neredeyse kesin değildir. İşletme 31.12.2025 tablolarında ne yapar?',
        {
            'A': 'Özkaynağa eklenir',
            'B': 'Koşullu varlık açıklanır',
            'C': 'Açıklama yapılmaz',
            'D': 'Karşılık ayrılır',
            'E': 'Alacak ve gelir tanınır',
        },
        'B',
        "TMS 37 p. 31-35 ve 89'a göre koşullu varlıklar finansal tablolara alınmaz; ekonomik fayda girişi **muhtemelse açıklanır**. Girişin gerçekleşmesi **neredeyse kesin** hâle geldiğinde varlık tanınır.",
        'TMS 37 p. 31-35, 89',
    ),
    # düzey 2
    '0003': patch(
        'Bir perakendeci yasal zorunluluk olmamasına rağmen yıllardır memnun kalmayan müşterilerin ürünlerini 30 gün içinde iade almakta ve bu politikası kamuoyunca bilinmektedir. İade yükümlülüğü hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yasal yükümlülük vardır',
            'B': 'Yükümlülük gelecekte doğar',
            'C': 'Zımni yükümlülük vardır',
            'D': 'Yükümlülük yoktur',
            'E': 'Koşullu varlık vardır',
        },
        'C',
        "TMS 37 p. 10'a göre **zımni yükümlülük**, işletmenin yerleşik uygulamaları, yayımlanmış politikaları veya açıklamalarıyla başkalarında sorumluluk üstleneceğine dair geçerli beklenti oluşturmasından doğar; iade politikası buna örnektir.",
        'TMS 37 p. 10, 17',
    ),
    # düzey 3
    '0004': patch(
        "Bir işletme tek bir büyük tesisin arızası nedeniyle müşteriye karşı tek bir yükümlülükle karşı karşıyadır. Onarımın ilk denemede başarılı olması ve 500.000 ₺'ye mal olması en olası sonuçtur; diğer olası sonuçların çoğu bu tutardan belirgin biçimde yüksektir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'En olası sonuç en iyi tahmin olabilir',
            'B': 'Diğer sonuçlar ölçümde dikkate alınmaz',
            'C': 'Diğer sonuçlar çoğunlukla yüksekse tahmin artırılabilir',
            'D': 'Diğer olası sonuçlar da değerlendirilir',
            'E': 'Tek yükümlülükte beklenen değer yöntemi esas değildir',
        },
        'B',
        "TMS 37 p. 40'a göre tek bir yükümlülük ölçülürken **en olası sonuç** en iyi tahmin olabilir; ancak işletme **diğer olası sonuçları da dikkate alır** ve bunlar çoğunlukla daha yüksek veya düşükse en iyi tahmin buna göre yükseltilir veya düşürülür.",
        'TMS 37 p. 40',
    ),
    # düzey 3
    '0005': patch(
        "Bir işletme kapatacağı bir tesis için yeniden yapılandırma kapsamında 350.000 ₺ tutarında karşılık hesaplamıştır. Tesisteki makinelerin satışından 60.000 ₺ kazanç beklenmektedir. Tanınacak karşılık kaç ₺'dir?",
        {
            'A': '60.000',
            'B': '350.000',
            'C': '290.000',
            'D': '0',
            'E': '410.000',
        },
        'B',
        "TMS 37 p. 51'e göre varlıkların beklenen elden çıkarılmasından doğacak kazançlar, elden çıkarma karşılığa neden olan olayla yakından ilişkili olsa bile **karşılığın ölçümünde dikkate alınmaz**: **350.000 ₺**; kazanç ilgili standarda göre gerçekleşince tanınır.",
        'TMS 37 p. 51-52',
    ),
    # düzey 2
    '0006': patch(
        "Bir işletme 200.000 ₺ dava karşılığı ayırmış ve neredeyse kesin olan 120.000 ₺ sigorta geri ödemesini ayrı varlık olarak tanımıştır. İşletme kâr veya zarar tablosunda bu karşılığa ilişkin gideri net sunmayı tercih etmiştir. Sunulacak net gider kaç ₺'dir?",
        {
            'A': '0',
            'B': '120.000',
            'C': '200.000',
            'D': '320.000',
            'E': '80.000',
        },
        'E',
        "TMS 37 p. 54'e göre kâr veya zarar tablosunda, karşılığa ilişkin gider **geri ödeme için tanınan tutar düşülerek** sunulabilir: 200.000 − 120.000 = **80.000 ₺**.",
        'TMS 37 p. 54',
    ),
    # düzey 3
    '0007': patch(
        "Bir işletme, garanti yükümlülükleri için ayırdığı ve kullanılmayan 80.000 ₺ karşılığı, aynı yıl ortaya çıkan bir dava tazminatını ödemek için kullanmak istemektedir. TMS 37'ye göre bu uygulama hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Dipnotla yapılabilir',
            'B': 'Yapılamaz',
            'C': 'Denetçi onayıyla yapılabilir',
            'D': 'Önemsizse yapılabilir',
            'E': 'Yapılabilir',
        },
        'B',
        "TMS 37 p. 61-62'ye göre karşılık **yalnızca başlangıçta ayrıldığı harcamalar için** kullanılır; bir karşılığı başka bir amaçla ayrılmış harcamalara mahsup etmek iki farklı olayın etkisini gizler.",
        'TMS 37 p. 61-62',
    ),
    # düzey 3
    '0008': patch(
        "Bir işletme bir bölümünü kapatma kararını ilan etmiş ve zımni mükellefiyet doğmuştur. Beklenen harcamalar: işten çıkarılacak personelin kıdem tazminatı 300.000 ₺, boşaltılacak binanın kira sözleşmesi fesih cezası 50.000 ₺, kalan personelin yeniden eğitimi 80.000 ₺, yeni ürünlerin pazarlaması 40.000 ₺, yeni bilgi sistemine yatırım 100.000 ₺. Yeniden yapılandırma karşılığı kaç ₺'dir?",
        {
            'A': '430.000',
            'B': '380.000',
            'C': '350.000',
            'D': '300.000',
            'E': '570.000',
        },
        'C',
        "TMS 37 p. 80-81'e göre yeniden yapılandırma karşılığı yalnızca yeniden yapılandırmadan **zorunlu olarak doğan ve işletmenin süregelen faaliyetleriyle ilişkili olmayan doğrudan harcamaları** içerir. Kalan personelin eğitimi, pazarlama ve yeni sistem yatırımı gelecekteki faaliyetlerle ilgilidir: 300.000 + 50.000 = **350.000 ₺**.",
        'TMS 37 p. 80-81',
    ),
    # düzey 2
    '0009': patch(
        "Bir enerji şirketi yıl içinde bir rüzgâr santrali kurmuş ve ruhsat koşulları gereği santrali 25 yıl sonra sökmekle yükümlüdür; söküm maliyetinin bugünkü değeri 3 milyon ₺'dir. Bu söküm karşılığının karşı tarafı nerede muhasebeleştirilir?",
        {
            'A': 'Diğer kapsamlı gelirde',
            'B': 'Santralin maliyetinde',
            'C': 'Koşullu varlıklarda',
            'D': 'Geçmiş yıllar kârlarında',
            'E': 'Kâr veya zararda',
        },
        'B',
        "Santral kurulduğu için söküm yükümlülüğü geçmiş olaydan doğar ve TMS 37'ye göre karşılık tanınır; TMS 16 p. 16(c)'ye göre varlığın sökülmesi ve bulunduğu yerin restorasyonuna ilişkin ilk tahmini maliyet **maddi duran varlığın maliyetine** eklenir.",
        'TMS 37 p. 14; TMS 16 p. 16',
    ),
    # düzey 2
    '0010': patch(
        'Bir işletme karşılıklarının her sınıfı için dönem başı ve dönem sonu defter değerlerini, dönemde ayrılan ek karşılıkları, kullanılan ve iptal edilen tutarları açıklamaktadır. Bu açıklamada karşılaştırmalı bilgi sunulması hakkında ne söylenebilir?',
        {
            'A': 'Gerekmez',
            'B': 'Gerekir',
            'C': 'Önemliyse gerekir',
            'D': 'Her karşılık için ayrı gerekir',
            'E': 'Denetçi isterse gerekir',
        },
        'A',
        "TMS 37 p. 84'e göre işletme karşılıkların her sınıfı için dönem başı ve sonu defter değerlerini, ek karşılıkları, kullanılan ve iptal edilen tutarları ve iskonto etkisini açıklar; bu mutabakat için **karşılaştırmalı bilgi gerekmez**.",
        'TMS 37 p. 84',
    ),
    # düzey 3
    '0011': patch(
        "Bir işletme bir rakibiyle süren bir anlaşmazlığa ilişkin karşılığın ayrıntılı açıklanmasının, işletmenin karşı tarafla ilişkisinde ciddi zarar doğuracağını değerlendirmektedir; bu aşırı nadir bir durumdur. TMS 37'ye göre işletme ne yapabilir?",
        {
            'A': 'Karşılık tanımaz',
            'B': 'Tutarın tamamını açıklar',
            'C': 'Anlaşmazlığın genel niteliğini açıklar',
            'D': 'Açıklama yapmaz',
            'E': 'Karşılığı özkaynakta gösterir',
        },
        'C',
        "TMS 37 p. 92'ye göre aşırı nadir durumlarda bilgilerin açıklanması işletmeyi diğer taraflarla anlaşmazlıkta ciddi şekilde zarara uğratacaksa, işletme o bilgileri açıklamayabilir; ancak **anlaşmazlığın genel niteliğini, bilginin açıklanmama gerekçesiyle birlikte** açıklar.",
        'TMS 37 p. 92',
    ),
    # düzey 3
    '0012': patch(
        "Bir sigorta şirketi benzer nitelikte çok sayıda küçük tazminat talebine ilişkin yükümlülüğünü ölçmektedir. Toplam talepler için olası sonuçlar: %60 olasılıkla ödeme yapılmaması, %30 olasılıkla 500.000 ₺, %10 olasılıkla 1.200.000 ₺ ödeme. Karşılık kaç ₺'dir?",
        {
            'A': '270.000',
            'B': '1.200.000',
            'C': '500.000',
            'D': '1.700.000',
            'E': '0',
        },
        'A',
        "Çok sayıda kalemi kapsayan yükümlülükte TMS 37 p. 39'a göre beklenen değer kullanılır: %60 × 0 + %30 × 500.000 + %10 × 1.200.000 = **270.000 ₺**.",
        'TMS 37 p. 39',
    ),
    # düzey 2
    '0013': patch(
        'Bir işletmenin aşağıdaki yükümlülüklerinden hangisi TMS 37 kapsamında değil, kendi özel standardı kapsamında muhasebeleştirilir?',
        {
            'A': 'Kurumlar vergisi yükümlülüğü',
            'B': 'Dava yükümlülüğü',
            'C': 'Yeniden yapılandırma yükümlülüğü',
            'D': 'Çevre temizliği yükümlülüğü',
            'E': 'Garanti yükümlülüğü',
        },
        'A',
        "TMS 37 p. 5'e göre bir karşılık, koşullu borç veya koşullu varlık başka bir standart kapsamındaysa o standart uygulanır; **gelir vergileri TMS 12** kapsamındadır.",
        'TMS 37 p. 1, 5',
    ),
    # düzey 3
    '0014': patch(
        "Bir işletmenin kefil olduğu grup dışı şirket 31.12.2025'ten önce iflas başvurusunda bulunmuş; kefaletin paraya çevrilmesi ve işletmeden 700.000 ₺ ödeme istenmesi muhtemel hâle gelmiştir. İşletme ne yapar?",
        {
            'A': '1.000.000 ₺ koşullu varlık tanır',
            'B': '700.000 ₺ karşılık tanır',
            'C': 'Gelecek yıl gider yazar',
            'D': 'Açıklama yapmaz',
            'E': 'Koşullu borç açıklar',
        },
        'B',
        'Borçlunun mali durumunun bozulmasıyla kaynak çıkışı **muhtemel** hâle gelmiştir; TMS 37 p. 14 uyarınca en iyi tahmin olan **700.000 ₺ karşılık** tanınır.',
        'TMS 37 p. 14; Ek C',
    ),
    # düzey 3
    '0015': patch(
        "Bir şirket açık denizde petrol platformu kurmuştur; ruhsat gereği platform söküldüğünde deniz tabanı eski hâline getirilecektir. Toplam restorasyon maliyetinin %90'ı platformun kurulmasından, kalanı petrol çıkarımından doğacaktır; henüz çıkarım başlamamıştır. Toplam restorasyon maliyetinin bugünkü değeri 1.000.000 ₺ ise kurulum tarihinde tanınacak karşılık kaç ₺'dir?",
        {
            'A': '100.000',
            'B': '900.000',
            'C': '0',
            'D': '1.000.000',
            'E': '450.000',
        },
        'B',
        'Platformun kurulması yasal yükümlülük doğuran **geçmiş olaydır**; çıkarım henüz yapılmadığından çıkarıma ilişkin kısım için mevcut yükümlülük yoktur. Karşılık yalnız kurulumdan doğan kısım için tanınır: **900.000 ₺**; çıkarım yapıldıkça ek karşılık ayrılır.',
        'TMS 37 p. 19; Ek C',
    ),
    # düzey 3
    '0016': patch(
        "Bir işletmenin dava karşılıkları dönem başında 100.000 ₺'dir. Dönem içinde karşılığın 70.000 ₺'si ödemelerde kullanılmış, bir davanın kazanılması nedeniyle 30.000 ₺'si iptal edilmiş ve yeni davalar için 50.000 ₺ karşılık ayrılmıştır. Dönem sonu dava karşılıkları kaç ₺'dir?",
        {
            'A': '20.000',
            'B': '150.000',
            'C': '120.000',
            'D': '50.000',
            'E': '80.000',
        },
        'D',
        "TMS 37 p. 84'teki karşılık mutabakatına göre: dönem başı + ek karşılıklar − kullanılanlar − iptal edilenler: 100.000 + 50.000 − 70.000 − 30.000 = **50.000 ₺**.",
        'TMS 37 p. 59, 61, 84',
    ),
    # düzey 2
    '0017': patch(
        "Yeni bir mevzuat, işletmelerin 2026 yılında personelini yeni vergi kurallarına ilişkin eğitmesini zorunlu kılmaktadır; eğitim maliyeti 150.000 ₺ olacaktır ve henüz eğitim verilmemiştir. 31.12.2025'te ne yapılır?",
        {
            'A': 'Koşullu borç açıklanır',
            'B': 'Özkaynakta yedek ayrılır',
            'C': 'Karşılık tanınır',
            'D': 'Maddi olmayan varlık tanınır',
            'E': 'Karşılık ayrılmaz',
        },
        'E',
        'Eğitim maliyeti **gelecekteki faaliyetle** ilgilidir; raporlama tarihinde geçmiş olaydan doğan mevcut yükümlülük yoktur. TMS 37 p. 19 uyarınca karşılık ayrılmaz.',
        'TMS 37 p. 19',
    ),
    # düzey 3
    '0018': patch(
        'Bir işletme binlerce ürün için garanti vermiştir. Tek bir ürün için kaynak çıkışı olasılığı düşük olsa da, ürünler bütün olarak değerlendirildiğinde bazı ürünler için kaynak çıkışı muhtemeldir. Garanti yükümlülüğü nasıl değerlendirilir?',
        {
            'A': 'Koşullu varlık tanınır',
            'B': 'Her ürün tek tek değerlendirilir',
            'C': 'Karşılık ayrılmaz',
            'D': 'Koşullu borç açıklanır',
            'E': 'Grup bütün olarak değerlendirilir',
        },
        'E',
        "TMS 37 p. 24'e göre ürün garantileri gibi benzer nitelikte çok sayıda yükümlülük varsa, kaynak çıkışı olasılığı **yükümlülük grubu bütün olarak** değerlendirilerek belirlenir; tek kalem için olasılık düşük olsa da grup için muhtemel olabilir ve karşılık tanınır.",
        'TMS 37 p. 24',
    ),
    # düzey 2
    '0019': patch(
        'Aşağıdakilerden hangileri yeniden yapılandırma karşılığına dâhil edilir?\n\nI. İşten çıkarılacak personelin tazminatı\n\nII. Kalan personelin yeniden eğitimi\n\nIII. Yeni dağıtım ağına yatırım',
        {
            'A': 'I ve III',
            'B': 'Yalnız II',
            'C': 'Yalnız I',
            'D': 'I, II ve III',
            'E': 'I ve II',
        },
        'C',
        "TMS 37 p. 80-81'e göre karşılık yeniden yapılandırmadan zorunlu olarak doğan doğrudan harcamaları (I) içerir; kalan personelin yeniden eğitimi (II) ve yeni dağıtım ağına yatırım (III) **süregelen faaliyetlerle ilgilidir** ve dâhil edilmez.",
        'TMS 37 p. 80-81',
    ),
    # düzey 2
    '0020': patch(
        'Aşağıdakilerden hangileri karşılığın ölçümünde doğrudur?\n\nI. Çok sayıda kalemde beklenen değer kullanılır\n\nII. Tek yükümlülükte en olası sonuç en iyi tahmin olabilir\n\nIII. Paranın zaman değeri önemliyse bugünkü değer kullanılır',
        {
            'A': 'I ve III',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'Yalnız I',
            'E': 'I, II ve III',
        },
        'E',
        "TMS 37 p. 39'a göre çok sayıda kalemde beklenen değer (I), p. 40'a göre tek yükümlülükte en olası sonuç (II) ve p. 45'e göre önemli zaman değerinde bugünkü değer (III) kullanılır.",
        'TMS 37 p. 39-40, 45',
    ),
    # düzey 2
    '0021': patch(
        'Bir işletme aleyhine açılan davada hukuk müşaviri, kaybetme olasılığını %30 olarak değerlendirmektedir; bu olasılık uzak değildir. İşletme 31.12.2025 tablolarında ne yapar?',
        {
            'A': 'Koşullu borç olarak açıklanır',
            'B': 'Tahmini tutarın yarısı kadar karşılık ayrılır',
            'C': 'Koşullu varlık tanınır',
            'D': 'Karşılık tanınır',
            'E': 'Gelecek yıl gider yazılır',
        },
        'A',
        "TMS 37 p. 16 ve 86'ya göre mevcut yükümlülük olasılığı düşükse veya kaynak çıkışı muhtemel değilse karşılık tanınmaz; kaynak çıkışı **uzak olasılık değilse koşullu borç** olarak açıklanır.",
        'TMS 37 p. 16, 86',
    ),
    # düzey 2
    '0022': patch(
        'Bir işletme davayı kazanmış, karar kesinleşmiş ve karşı tarafın 400.000 ₺ tazminatı ödeme gücü bulunduğu için tahsilat neredeyse kesin hâle gelmiştir. Bu tutar finansal tablolarda nasıl yer alır?',
        {
            'A': 'Koşullu varlık olarak açıklanır',
            'B': 'Tanınmaz',
            'C': 'Özkaynakta gösterilir',
            'D': 'Karşılıktan düşülür',
            'E': 'Varlık olarak tanınır',
        },
        'E',
        "TMS 37 p. 33'e göre gelirin gerçekleşmesi **neredeyse kesin** hâle geldiğinde ilgili varlık artık koşullu varlık değildir ve finansal tablolara alınır.",
        'TMS 37 p. 33',
    ),
    # düzey 3
    '0023': patch(
        'Bir işletme çevreyi kirletmiştir. Raporlama tarihinde temizlik yükümlülüğü getiren bir yasa yoktur; ancak yıl sonundan önce kabul edilen ve yürürlüğe girmesi neredeyse kesin olan bir kanun geçmişe yönelik temizlik yükümlülüğü getirecektir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Yükümlülük kanunun neredeyse kesin yasalaşmasıyla doğar',
            'B': 'Karşılık tanınabilir',
            'C': 'Geçmiş olay kirliliktir',
            'D': 'Temizlik maliyeti güvenilir tahmin edilmelidir',
            'E': 'Kanun yürürlüğe girmeden yükümlülük doğmaz',
        },
        'E',
        "TMS 37 p. 21-22'ye göre önerilen yeni bir kanunun ayrıntıları kesinleşmişse ve kanunun **neredeyse kesin olarak yasalaşacağı** açıksa, yasal yükümlülük kanun yürürlüğe girmeden doğmuş kabul edilir.",
        'TMS 37 p. 21-22',
    ),
    # düzey 3
    '0024': patch(
        "Bir işletmenin maden sahasını 5 yıl sonra eski hâline getirme yükümlülüğü vardır; bu tarihte ödenmesi beklenen tutar 1.000.000 ₺'dir. Paranın zaman değeri önemlidir ve uygun vergi öncesi iskonto oranı %8'dir. Karşılığın bugünkü tutarı yaklaşık kaç ₺'dir?",
        {
            'A': '1.000.000',
            'B': '714.286',
            'C': '600.000',
            'D': '680.583',
            'E': '925.926',
        },
        'D',
        "TMS 37 p. 45-47'ye göre paranın zaman değerinin etkisi önemliyse karşılık, yükümlülüğü yerine getirmek için gereken harcamaların **vergi öncesi oranla** iskonto edilmiş bugünkü değeridir: 1.000.000 / 1,08⁵ ≈ **680.583 ₺**.",
        'TMS 37 p. 45-47',
    ),
    # düzey 2
    '0025': patch(
        "Bir işletme karşılıkları ölçerken belirsizlikleri dikkate almakta, ancak 'ne olur ne olmaz' diyerek bütün karşılıkları %30 fazlasıyla ayırmaktadır. Bu uygulama TMS 37'ye göre nasıl değerlendirilir?",
        {
            'A': 'Uygun değildir',
            'B': 'Uygundur',
            'C': 'Tutarlılık gereğidir',
            'D': 'Önemlilik gereğidir',
            'E': 'İhtiyatlılık gereği zorunludur',
        },
        'A',
        "TMS 37 p. 43'e göre belirsizlik, karşılıkların fazla, varlıkların ve gelirlerin eksik gösterilmesini haklı kılmaz; **ihtiyatlılık kasıtlı fazla karşılık ayrılmasına izin vermez**. Karşılık en iyi tahminle ölçülür.",
        'TMS 37 p. 42-43',
    ),
    # düzey 3
    '0026': patch(
        "Bir işletme bir dava için 200.000 ₺ karşılık tanımıştır. Sigorta şirketinin bu tutarın 120.000 ₺'sini ödemesi neredeyse kesindir; ancak işletme davacıya karşı tutarın tamamından sorumludur. Finansal durum tablosunda karşılık ve sigorta alacağı nasıl gösterilir?",
        {
            'A': 'Karşılık 80.000 ₺, varlık yok',
            'B': 'Karşılık 200.000, varlık 120.000 ₺',
            'C': 'Karşılık 320.000 ₺, varlık yok',
            'D': 'Karşılık 200.000 ₺, varlık yok',
            'E': 'Karşılık 120.000, varlık 200.000 ₺',
        },
        'B',
        "TMS 37 p. 53'e göre geri ödeme **ancak alınacağı neredeyse kesin olduğunda ayrı bir varlık** olarak tanınır ve karşılık tutarını aşamaz; finansal durum tablosunda karşılık brüt gösterilir. p. 54'e göre kâr veya zarar tablosunda gider geri ödeme düşülerek net sunulabilir.",
        'TMS 37 p. 53-54',
    ),
    # düzey 2
    '0027': patch(
        'Bir işletmenin yönetimi, gelecek yıl kötüleşen pazar koşulları nedeniyle 2 milyon ₺ faaliyet zararı beklemektedir. Bu beklenen zararlar için 31.12.2025 tablolarında ne yapılır?',
        {
            'A': 'Koşullu borç açıklanır',
            'B': 'Varlıklar yeniden değerlenir',
            'C': 'Karşılık ayrılmaz',
            'D': 'Özkaynakta yedek ayrılır',
            'E': 'Karşılık tanınır',
        },
        'C',
        "TMS 37 p. 63'e göre **gelecekteki faaliyet zararları için karşılık ayrılmaz**; bu zararlar karşılık tanımını ve tanıma ölçütlerini karşılamaz. p. 65 uyarınca varlıklar değer düşüklüğü bakımından test edilebilir.",
        'TMS 37 p. 63-65',
    ),
    # düzey 3
    '0028': patch(
        'Bir işletme, ekonomik açıdan dezavantajlı olup olmadığını değerlendirdiği bir üretim sözleşmesinin ifa maliyetini belirlemektedir. 2022 değişikliğine göre sözleşmenin ifa maliyeti aşağıdakilerden hangisini kapsamaz?',
        {
            'A': 'Sözleşmeyle doğrudan ilişkili diğer maliyetlerin payı',
            'B': 'Sözleşmede kullanılan makinenin amortisman payı',
            'C': 'Doğrudan malzeme',
            'D': 'Genel yönetim giderleri',
            'E': 'Doğrudan işçilik',
        },
        'D',
        "TMS 37 p. 68A'ya göre ifa maliyeti **sözleşmeyle doğrudan ilişkili maliyetlerden** oluşur: ek maliyetler (doğrudan işçilik ve malzeme) ile doğrudan ilişkili diğer maliyetlerin dağıtılan payı (ör. kullanılan makinenin amortismanı). Sözleşmeyle doğrudan ilişkili olmayan genel yönetim giderleri dâhil edilmez.",
        'TMS 37 p. 68A',
    ),
    # düzey 3
    '0029': patch(
        "Bir işletmenin yönetim kurulu Aralık 2025'te bir bölümü kapatmaya karar vermiştir; ancak yıl sonuna kadar ayrıntılı resmî plan hazırlanmamış, karar çalışanlara, müşterilere veya tedarikçilere duyurulmamış ve uygulamaya başlanmamıştır. 31.12.2025'te yeniden yapılandırma karşılığı hakkında ne söylenebilir?",
        {
            'A': 'Karşılığın yarısı ayrılır',
            'B': 'Koşullu borç açıklanır',
            'C': 'Karşılık tanınır',
            'D': 'Koşullu varlık tanınır',
            'E': 'Karşılık ayrılmaz',
        },
        'E',
        "TMS 37 p. 72'ye göre yeniden yapılandırmaya ilişkin zımni mükellefiyet, işletmenin **ayrıntılı resmî bir planının** olması ve plana başlayarak veya ana özelliklerini duyurarak **etkilenenlerde geçerli bir beklenti** oluşturmasıyla doğar. Yıl sonundan önce yalnızca yönetim kararı alınması mükellefiyet doğurmaz.",
        'TMS 37 p. 72',
    ),
    # düzey 3
    '0030': patch(
        "Bir işletme, bir banka kredisinde başka bir şirketle birlikte müteselsil sorumludur. Kredinin 600.000 ₺'lik kısmının diğer şirket tarafından ödenmesi beklenmektedir; işletmenin kendi payı olan 400.000 ₺ için kaynak çıkışı muhtemeldir. İşletme ne yapar?",
        {
            'A': '600.000 ₺ karşılık, 400.000 ₺ koşullu borç',
            'B': 'Bir işlem yapılmaz',
            'C': '400.000 ₺ karşılık, 600.000 ₺ koşullu borç',
            'D': '1.000.000 ₺ koşullu borç',
            'E': '1.000.000 ₺ karşılık',
        },
        'C',
        "TMS 37 p. 29'a göre müteselsil sorumlulukta, yükümlülüğün **diğer taraflarca karşılanması beklenen kısmı koşullu borç** olarak ele alınır; işletme kaynak çıkışının muhtemel olduğu kısım için karşılık tanır.",
        'TMS 37 p. 29',
    ),
    # düzey 3
    '0031': patch(
        "Bir işletmenin garanti karşılığı dönem başında 60.000 ₺'dir. Dönem içinde önceki satışlara ilişkin garanti harcamaları için 45.000 ₺ kullanılmıştır. Dönem sonunda, satışların %2'si (5.000.000 ₺ × %2) olarak hesaplanan gerekli karşılık 100.000 ₺'dir. Dönemin garanti karşılığı gideri kaç ₺'dir?",
        {
            'A': '45.000',
            'B': '85.000',
            'C': '40.000',
            'D': '100.000',
            'E': '145.000',
        },
        'B',
        'Kullanılan tutar karşılıktan düşülür: 60.000 − 45.000 = 15.000 ₺ kalır. Dönem sonu gerekli karşılığa ulaşmak için ek gider: 100.000 − 15.000 = **85.000 ₺**.',
        'TMS 37 p. 36, 59, 61',
    ),
    # düzey 2
    '0032': patch(
        "TMS 37'de zamanlaması veya tutarı belirsiz olan yükümlülük hangi kavramla ifade edilir?",
        {
            'A': 'Yedek',
            'B': 'Karşılık',
            'C': 'Tahakkuk',
            'D': 'Koşullu borç',
            'E': 'Koşullu varlık',
        },
        'B',
        "TMS 37 p. 10'a göre **karşılık, zamanlaması veya tutarı belirsiz olan yükümlülüktür**. Tahakkuklarda belirsizlik genellikle çok daha azdır (p. 11); koşullu borç ise tanınmayan olası veya ölçülemeyen yükümlülüktür.",
        'TMS 37 p. 10',
    ),
    # düzey 3
    '0033': patch(
        'Bir işletme aleyhine açılan davada, yıl sonu itibarıyla mevcut bir yükümlülük bulunup bulunmadığı belirsizdir. Bilirkişi görüşü dâhil mevcut bütün kanıtlar, raporlama tarihinde mevcut yükümlülüğün bulunmama olasılığının daha yüksek olduğunu göstermektedir; olasılık uzak değildir. İşletme ne yapar?',
        {
            'A': 'Koşullu borç açıklanır',
            'B': 'Koşullu varlık tanır',
            'C': 'Karşılık tanınır',
            'D': 'Açıklama yapmaz',
            'E': 'Gelecek yıl karşılık ayırır',
        },
        'A',
        "TMS 37 p. 15-16'ya göre mevcut kanıtlar dikkate alındığında raporlama tarihinde **mevcut yükümlülük bulunmama olasılığı daha yüksekse** karşılık tanınmaz; kaynak çıkışı uzak olasılık değilse **koşullu borç açıklanır**.",
        'TMS 37 p. 15-16',
    ),
    # düzey 2
    '0034': patch(
        "Bir işletme, grup dışı bir şirketin 1 milyon ₺'lik banka kredisine kefil olmuştur. 31.12.2025 itibarıyla borçlu şirketin mali durumu güçlüdür ve kefaletin paraya çevrilmesi olasılığı düşüktür, ancak uzak değildir. İşletme ne yapar?",
        {
            'A': 'Kefalet tutarı kadar borç tanır',
            'B': 'Açıklama yapmaz',
            'C': 'Koşullu varlık tanır',
            'D': 'Koşullu borç açıklanır',
            'E': 'Karşılık tanınır',
        },
        'D',
        "Kefalet sözleşmesi geçmiş olaydır ve yükümlülük doğurur; ancak kaynak çıkışı **muhtemel değilse** karşılık tanınmaz. TMS 37 p. 86'ya göre olasılık uzak değilse **koşullu borç açıklanır**. (Finansal garanti sözleşmeleri TFRS 9 kapsamına da girebilir; burada TMS 37 örneği esas alınmıştır.)",
        'TMS 37 p. 14, 86; Ek C',
    ),
    # düzey 3
    '0035': patch(
        "Bir işletmenin fırınının astarının her 5 yılda bir yenilenmesi gerekmektedir; yasal bir zorunluluk yoktur ve fırın satılabilir veya kullanımı durdurulabilir. Yönetim her yıl astar yenileme maliyetinin beşte biri kadar karşılık ayırmak istemektedir. TMS 37'ye göre bu uygulama hakkında ne söylenebilir?",
        {
            'A': 'Özkaynakta yedek ayrılır',
            'B': 'Koşullu varlık tanınır',
            'C': 'Karşılık ayrılmaz',
            'D': 'Karşılık ayrılır',
            'E': 'Koşullu borç açıklanır',
        },
        'C',
        "Raporlama tarihinde astarın yenilenmesine ilişkin **işletmenin gelecekteki eylemlerinden bağımsız mevcut yükümlülüğü yoktur**; karşılık ayrılmaz. Astar maliyeti TMS 16'ya göre ayrı bileşen olarak 5 yılda amortismana tabi tutulur.",
        'TMS 37 Ek C; TMS 16 p. 13-14',
    ),
    # düzey 3
    '0036': patch(
        'Koşullu varlıklara ilişkin olarak aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Fayda girişi muhtemelse açıklanır',
            'B': 'Sürekli olarak değerlendirilir',
            'C': 'Fayda girişi muhtemelse varlık olarak tanınır',
            'D': 'Giriş neredeyse kesinleşince varlık tanınır',
            'E': 'Finansal tablolara alınmaz',
        },
        'C',
        "TMS 37 p. 31-35'e göre koşullu varlık finansal tablolara alınmaz; fayda girişi **muhtemelse yalnızca açıklanır**, gelişmeler sürekli değerlendirilir ve giriş **neredeyse kesin** hâle geldiğinde varlık tanınır.",
        'TMS 37 p. 31-35',
    ),
    # düzey 2
    '0037': patch(
        'Bir işletme 2025 yılında izinsiz atık boşaltarak çevre mevzuatını ihlal etmiş; yıl sonu itibarıyla idari para cezası kesilmesi muhtemeldir ve tutar güvenilir tahmin edilebilmektedir. İşletme ne yapar?',
        {
            'A': 'Karşılık tanınır',
            'B': 'Gelecek yıl gider yazar',
            'C': 'Açıklama yapmaz',
            'D': 'Koşullu varlık tanır',
            'E': 'Koşullu borç açıklanır',
        },
        'A',
        'Mevzuata aykırı faaliyet **geçmiş olaydır** ve cezaya ilişkin mevcut yükümlülük doğurur; kaynak çıkışı muhtemel olduğundan TMS 37 p. 14 uyarınca karşılık tanınır.',
        'TMS 37 p. 14, 17',
    ),
    # düzey 2
    '0038': patch(
        "TMS 37'ye göre karşılık olarak tanınacak tutar, raporlama tarihindeki mevcut yükümlülüğü yerine getirmek için gereken harcamanın en iyi tahminidir. Bu en iyi tahmin nasıl tanımlanır?",
        {
            'A': 'Sigorta limitinin tamamı',
            'B': 'Olası en yüksek tutar',
            'C': 'Geçmiş yıl ortalaması',
            'D': 'Olası en düşük tutar',
            'E': 'İşletmenin rasyonel olarak ödeyeceği tutar',
        },
        'E',
        "TMS 37 p. 36-37'ye göre en iyi tahmin, **işletmenin raporlama tarihinde yükümlülüğü yerine getirmek veya üçüncü tarafa devretmek için rasyonel olarak ödeyeceği tutardır**.",
        'TMS 37 p. 36-37',
    ),
    # düzey 3
    '0039': patch(
        'Aşağıdakilerden hangileri karşılığın ölçümü ve kullanımı bakımından doğrudur?\n\nI. Varlıkların beklenen satış kazançları karşılıktan düşülür\n\nII. Geri ödeme, alınması neredeyse kesinse ayrı varlık olarak tanınır\n\nIII. Karşılık yalnızca ayrıldığı harcamalar için kullanılır',
        {
            'A': 'I ve II',
            'B': 'Yalnız II',
            'C': 'I, II ve III',
            'D': 'II ve III',
            'E': 'Yalnız III',
        },
        'D',
        "TMS 37 p. 53'e göre neredeyse kesin geri ödeme ayrı varlıktır (II); p. 61'e göre karşılık ayrıldığı amaçla kullanılır (III). p. 51'e göre beklenen varlık satış kazançları **dikkate alınmaz** (I yanlış).",
        'TMS 37 p. 51, 53, 61',
    ),
    # düzey 3
    '0040': patch(
        'Aşağıdakilerden hangileri geçmiş olaydan doğan mevcut yükümlülük örneğidir?\n\nI. Kamuoyuna duyurulmuş ve uygulanan iade politikası kapsamındaki iadeler\n\nII. Kurulmuş bir tesisin ruhsat gereği sökülmesi\n\nIII. Gelecekte zorunlu olacak bir filtrenin henüz takılmamış olması',
        {
            'A': 'I, II ve III',
            'B': 'I ve II',
            'C': 'Yalnız I',
            'D': 'Yalnız II',
            'E': 'I ve III',
        },
        'B',
        "TMS 37 p. 10 ve 17'ye göre duyurulmuş iade politikası zımni (I), ruhsat gereği söküm yasal yükümlülük (II) doğurur. Henüz takılmamış filtrenin maliyeti işletmenin **gelecekteki eylemleriyle kaçınılabilir** olduğundan mevcut yükümlülük değildir (III).",
        'TMS 37 p. 10, 17, 19',
    ),
    # düzey 2
    '0041': patch(
        'Bir işletme, çok düşük ihtimalli ve uzak olasılık olarak değerlendirilen bir yükümlülük riskiyle karşı karşıyadır. Bu risk hakkında finansal tablolarda ne yapılır?',
        {
            'A': 'Koşullu borç açıklanır',
            'B': 'Karşılık tanınır',
            'C': 'Koşullu varlık tanınır',
            'D': 'Açıklama gerekmez',
            'E': 'Özkaynakta yedek ayrılır',
        },
        'D',
        "TMS 37 p. 28 ve 86'ya göre koşullu borç, kaynak çıkışı **uzak bir olasılık olmadıkça** açıklanır; uzak olasılık hâlinde açıklama da gerekmez.",
        'TMS 37 p. 28, 86',
    ),
    # düzey 3
    '0042': patch(
        'Yasal bir zorunluluk bulunmamasına rağmen bir işletme, fabrikalarına gelecek yıl filtre takmayı planlamaktadır; işletme fabrikayı kapatarak veya faaliyet biçimini değiştirerek bu harcamadan kaçınabilir. 31.12.2025 tablolarında filtre maliyeti için ne yapılır?',
        {
            'A': 'Karşılık tanınır',
            'B': 'Koşullu varlık tanınır',
            'C': 'Özkaynakta yedek ayrılır',
            'D': 'Maddi duran varlık tanınır',
            'E': 'Karşılık tanınmaz',
        },
        'E',
        "TMS 37 p. 19'a göre yalnızca işletmenin **gelecekteki eylemlerinden bağımsız olarak var olan** geçmiş olaylardan doğan yükümlülükler karşılık olarak tanınır. İşletme gelecekteki eylemleriyle harcamadan kaçınabildiğinden mevcut yükümlülük yoktur.",
        'TMS 37 p. 17-19',
    ),
    # düzey 3
    '0043': patch(
        "Bir işletme dönem içinde 1.000.000 ₺ garantili satış yapmıştır. Geçmiş deneyime göre ürünlerin %75'i kusursuz olacak, %20'inde küçük kusurlar çıkacak (tamamında küçük kusur olsaydı onarım maliyeti 100.000 ₺ olurdu), %5'inde büyük kusurlar çıkacaktır (tamamında büyük kusur olsaydı maliyet 400.000 ₺ olurdu). Garanti karşılığı kaç ₺'dir?",
        {
            'A': '250.000',
            'B': '100.000',
            'C': '20.000',
            'D': '40.000',
            'E': '500.000',
        },
        'D',
        "TMS 37 p. 39'a göre çok sayıda kalemi kapsayan karşılıklar **beklenen değer** yöntemiyle, olası sonuçların olasılıklarıyla ağırlıklandırılmasıyla ölçülür: %75 × 0 + %20 × 100.000 + %5 × 400.000 = **40.000 ₺**.",
        'TMS 37 p. 39',
    ),
    # düzey 3
    '0044': patch(
        "Bir işletme, 5 yıl sonra ödenecek bir yükümlülük için bugünkü değeriyle 680.583 ₺ karşılık tanımıştır; iskonto oranı %8'dir. Bir yıl sonra karşılıktaki iskontonun çözülmesinden doğan artış yaklaşık kaç ₺'dir ve nasıl sınıflandırılır?",
        {
            'A': 'Artış tanınmaz',
            'B': '80.000 ₺, finansman gideri',
            'C': '54.447 ₺, finansman gideri',
            'D': '54.447 ₺, faaliyet gideri',
            'E': '54.447 ₺, DKG',
        },
        'C',
        "TMS 37 p. 60'a göre iskonto uygulandığında karşılığın defter değeri zamanın geçmesiyle her dönem artar ve bu artış **borçlanma maliyeti (finansman gideri)** olarak muhasebeleştirilir: 680.583 × %8 ≈ **54.447 ₺**.",
        'TMS 37 p. 60',
    ),
    # düzey 2
    '0045': patch(
        'Bir işletme söküm karşılığını ölçerken, yıl sonunda mevcut ve kullanıma girmesi beklenen yeni söküm teknolojisinin maliyetleri düşüreceğine ilişkin yeterli objektif kanıta sahiptir. Bu teknoloji karşılığın ölçümünde nasıl ele alınır?',
        {
            'A': 'Dikkate alınır',
            'B': 'Koşullu varlık tanınır',
            'C': 'Ayrı gelir yazılır',
            'D': 'Dikkate alınmaz',
            'E': 'Dipnotta açıklanır, ölçüme girmez',
        },
        'A',
        "TMS 37 p. 48-49'a göre yükümlülüğü karşılamak için gerekecek tutarı etkileyebilecek gelecekteki olaylar, gerçekleşeceklerine dair **yeterli objektif kanıt** varsa karşılık tutarına yansıtılır; yeni teknolojiye ilişkin makul beklentiler buna dâhildir.",
        'TMS 37 p. 48-49',
    ),
    # düzey 2
    '0046': patch(
        'Bir işletme geçen yıl bir dava için 150.000 ₺ karşılık ayırmıştır. Bu yıl davacı davadan feragat etmiş ve kaynak çıkışı artık muhtemel değildir. Karşılık hakkında ne yapılır?',
        {
            'A': 'Koşullu varlık tanınır',
            'B': 'Karşılık iptal edilir',
            'C': 'Karşılık korunur',
            'D': 'Önceki yıl düzeltilir',
            'E': 'Karşılık özkaynağa aktarılır',
        },
        'B',
        "TMS 37 p. 59'a göre karşılıklar her raporlama döneminin sonunda gözden geçirilir; kaynak çıkışı **artık muhtemel değilse karşılık iptal edilir**. Bu tahmin değişikliğidir, geçmiş dönem düzeltilmez.",
        'TMS 37 p. 59',
    ),
    # düzey 3
    '0047': patch(
        "Bir işletme kullanmadığı bir depo için yıllık 100.000 ₺ kira ödemeye kalan 3 yıl boyunca sözleşmeyle bağlıdır; depoyu alt kiraya vererek yıllık 40.000 ₺ elde edebilecektir. Sözleşmeyi hemen feshetmenin cezası 150.000 ₺'dir. Paranın zaman değeri ihmal edildiğinde ekonomik açıdan dezavantajlı sözleşme için ayrılacak karşılık kaç ₺'dir?",
        {
            'A': '150.000',
            'B': '300.000',
            'C': '120.000',
            'D': '330.000',
            'E': '180.000',
        },
        'A',
        "TMS 37 p. 68'e göre dezavantajlı sözleşmede karşılık, sözleşmeden çıkmanın **net maliyetini** yansıtan kaçınılamaz maliyettir: ifa maliyeti (100.000 − 40.000) × 3 = 180.000 ₺ ile fesih cezası 150.000 ₺'nin **düşük olanı**, **150.000 ₺**. (TFRS 16 kapsamındaki kiralamalarda önce kullanım hakkı değer düşüklüğü değerlendirilir; hesap mantığı aynıdır.)",
        'TMS 37 p. 66-68',
    ),
    # düzey 3
    '0048': patch(
        'Bir işletme bir faaliyet bölümünü satmaya karar vermiş ve bunu kamuya duyurmuştur; ancak yıl sonunda bağlayıcı bir satış anlaşması yoktur. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Bağlayıcı satış anlaşmasına kadar yükümlülük doğmaz',
            'B': 'Varlıklar TMS 36 kapsamında gözden geçirilebilir',
            'C': 'Satışa ilişkin karşılık ayrılmaz',
            'D': 'Bağlayıcı anlaşma sonrası değerlendirme değişebilir',
            'E': 'Satış kararı ilanıyla satışa ilişkin yükümlülük doğar',
        },
        'E',
        "TMS 37 p. 78'e göre bir faaliyetin satışı nedeniyle **bağlayıcı bir satış anlaşması yapılıncaya kadar** yükümlülük doğmaz; ilan tek başına yeterli değildir. p. 79'a göre varlıklar TMS 36'ya göre değer düşüklüğü açısından gözden geçirilebilir.",
        'TMS 37 p. 78-79',
    ),
    # düzey 3
    '0049': patch(
        "Yeni bir mevzuat, işletmelerin 30 Haziran 2026'dan itibaren fabrikalarına duman filtresi takmasını zorunlu kılmaktadır. 31.12.2025 itibarıyla işletme filtre takmamıştır ve henüz bir ceza doğuracak faaliyet de gerçekleşmemiştir. Filtre maliyeti için 31.12.2025'te ne yapılır?",
        {
            'A': 'Koşullu borç açıklanır',
            'B': 'Maddi duran varlık tanınır',
            'C': 'Özkaynakta yedek ayrılır',
            'D': 'Karşılık tanınır',
            'E': 'Karşılık tanınmaz',
        },
        'E',
        "31.12.2025'te filtre takma maliyetine ilişkin **geçmiş olaydan doğan mevcut yükümlülük yoktur**; işletme gelecekte faaliyetini değiştirerek maliyetten kaçınabilir. TMS 37 p. 19 uyarınca karşılık tanınmaz; yükümlülük ancak filtre takılmadan faaliyete devam edilirse (ör. ceza) doğabilir.",
        'TMS 37 p. 10, 19',
    ),
    # düzey 2
    '0050': patch(
        'Bir işletme, aleyhine açılan davada mevcut yükümlülüğü ve kaynak çıkışını muhtemel görmektedir; ancak tutar aşırı nadir bir durum olarak hiçbir biçimde güvenilir tahmin edilememektedir. Bu yükümlülük nasıl ele alınır?',
        {
            'A': 'Tahmini tutarın yarısı karşılık ayrılır',
            'B': 'Koşullu varlık tanınır',
            'C': 'Koşullu borç açıklanır',
            'D': 'Karşılık tanınır',
            'E': 'Açıklama yapılmaz',
        },
        'C',
        "TMS 37 p. 25-26'ya göre tahmin kullanımı karşılıkların hazırlanmasında esastır ve aşırı nadir durumlar dışında güvenilir tahmin yapılabilir; **güvenilir tahmin yapılamayan aşırı nadir durumda** borç tanınmaz, **koşullu borç** olarak açıklanır.",
        'TMS 37 p. 26',
    ),
    # düzey 3
    '0051': patch(
        "Bir işletme geçen yıl bir dava için 180.000 ₺ karşılık ayırmıştır. Bu yıl bilirkişi raporu doğrultusunda en iyi tahmin 240.000 ₺'ye yükselmiştir. Bu yıl kâr veya zarara yansıyacak ek karşılık gideri kaç ₺'dir?",
        {
            'A': '420.000',
            'B': '0',
            'C': '240.000',
            'D': '60.000',
            'E': '180.000',
        },
        'D',
        "TMS 37 p. 59'a göre karşılıklar her dönem sonunda gözden geçirilir ve güncel en iyi tahmini yansıtacak şekilde düzeltilir; fark tahmin değişikliği olarak cari döneme yansır: 240.000 − 180.000 = **60.000 ₺**.",
        'TMS 37 p. 59',
    ),
    # düzey 2
    '0052': patch(
        'Bir işletmenin yıl sonunda aldığı ancak faturası henüz gelmemiş elektrik hizmetine ilişkin tutar, sayaç okumasına göre yaklaşık olarak bilinmektedir. Bu yükümlülük finansal durum tablosunda genellikle nasıl sınıflandırılır?',
        {
            'A': 'Koşullu varlık',
            'B': 'Koşullu borç',
            'C': 'Özkaynak',
            'D': 'Ticari borç veya tahakkuk',
            'E': 'Karşılık',
        },
        'D',
        "TMS 37 p. 11'e göre alınan mal veya hizmetler için ödenecek ve faturası alınmamış tutarlar gibi **tahakkuklar**, belirsizlik karşılıklara göre çok daha az olduğundan genellikle ticari ve diğer borçların parçası olarak raporlanır; karşılık olarak ayrı gösterilmez.",
        'TMS 37 p. 11',
    ),
    # düzey 3
    '0053': patch(
        'Bir işletme 10 yıl sonra ödenecek bir söküm yükümlülüğünün bugünkü değerini hesaplamaktadır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Oran yükümlülüğe özgü riskleri yansıtır',
            'B': 'İskontonun çözülmesi finansman gideridir',
            'C': 'İskonto oranı vergi sonrası oran olmalıdır',
            'D': 'Paranın zaman değeri önemliyse iskonto uygulanır',
            'E': 'Nakit akışlarında yansıtılan riskler orana tekrar eklenmez',
        },
        'C',
        "TMS 37 p. 47'ye göre iskonto oranı paranın zaman değerine ve yükümlülüğe özgü risklere ilişkin güncel piyasa değerlendirmelerini yansıtan **vergi öncesi** oran(lar) olmalıdır; nakit akışı tahminlerinde dikkate alınan riskler oranda tekrar yansıtılmaz. p. 60'a göre iskontonun çözülmesi borçlanma maliyetidir.",
        'TMS 37 p. 45-47, 60',
    ),
    # düzey 2
    '0054': patch(
        'Bir ülkede yıl içinde çıkarılan ve yürürlüğe giren bir kanun, işletmelerin faaliyetleriyle kirlettikleri araziyi temizlemesini zorunlu kılmıştır. Bir işletme yıl içinde bir araziyi kirletmiştir. 31.12.2025 itibarıyla temizlik maliyeti için ne yapılır?',
        {
            'A': 'Koşullu varlık tanınır',
            'B': 'Koşullu borç açıklanır',
            'C': 'Açıklama yapılmaz',
            'D': 'Karşılık tanınır',
            'E': 'Gelecek yıl gider yazılır',
        },
        'D',
        'Kirlilik geçmiş olaydır ve yürürlükteki kanun **yasal yükümlülük** doğurur; kaynak çıkışı muhtemel olduğundan TMS 37 p. 14 uyarınca karşılık tanınır.',
        'TMS 37 p. 21; Ek C',
    ),
    # düzey 3
    '0055': patch(
        'Bir havayolu şirketi mevzuat gereği uçaklarını her 3 yılda bir kapsamlı bakıma sokmak zorundadır; ancak uçağı satarak veya uçuştan çekerek bu bakımdan kaçınabilir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Karşılık ayrılmaz',
            'B': 'Maliyet işletmenin gelecekteki eylemleriyle kaçınılabilir',
            'C': 'Mevzuat zorunluluğu nedeniyle bakım karşılığı ayrılır',
            'D': 'Mevcut yükümlülük yoktur',
            'E': 'Bakım maliyeti ayrı bileşen olarak amortismana tabi tutulabilir',
        },
        'C',
        'Bakım yasal olarak zorunlu olsa da yükümlülük uçağın **gelecekte işletilmesine** bağlıdır; işletme uçağı satarak kaçınabileceğinden raporlama tarihinde mevcut yükümlülük yoktur ve **karşılık ayrılmaz** (TMS 37 p. 19).',
        'TMS 37 Ek C',
    ),
    # düzey 2
    '0056': patch(
        "Bir işletme binalarını yangına karşı sigortalatmamış, bunun yerine her yıl olası yangın zararları için 'kendi kendini sigorta karşılığı' ayırmak istemektedir; herhangi bir yangın gerçekleşmemiştir. TMS 37'ye göre bu karşılık hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Özkaynakta gösterilir',
            'B': 'Koşullu borç olarak açıklanır',
            'C': 'Ayrılamaz',
            'D': 'Ayrılabilir',
            'E': 'Varlık maliyetine eklenir',
        },
        'C',
        "Henüz gerçekleşmemiş yangına ilişkin **geçmiş olay ve mevcut yükümlülük yoktur**; gelecekteki olası zararlar için TMS 37'ye göre karşılık ayrılamaz.",
        'TMS 37 p. 14, 19',
    ),
    # düzey 3
    '0057': patch(
        "Bir işletme 1 Ocak'ta bugünkü değeriyle 680.583 ₺ söküm karşılığı tanımıştır; iskonto oranı %8'dir ve tahminlerde değişiklik yoktur. Karşılığın 31 Aralık'taki defter değeri yaklaşık kaç ₺'dir?",
        {
            'A': '680.583',
            'B': '1.000.000',
            'C': '54.447',
            'D': '735.030',
            'E': '626.137',
        },
        'D',
        "TMS 37 p. 60'a göre iskonto uygulanan karşılığın defter değeri **zamanın geçmesini yansıtacak şekilde** her dönem artar: 680.583 × 1,08 ≈ **735.030 ₺**; artış finansman gideridir.",
        'TMS 37 p. 60',
    ),
    # düzey 1
    '0058': patch(
        "TMS 37'de bir kaynak çıkışının 'muhtemel' sayılması için olayın gerçekleşme olasılığı hakkında hangi koşul aranır?",
        {
            'A': 'Gerçekleşmeme olasılığından yüksek olması',
            'B': 'Kesin olması',
            'C': 'Denetçice onaylanması',
            'D': "%25'i aşması",
            'E': "%90'ı aşması",
        },
        'A',
        "TMS 37 p. 23'e göre bir kaynak çıkışı, olayın **gerçekleşme olasılığı gerçekleşmeme olasılığından yüksekse** (yani %50'yi aşıyorsa) muhtemel kabul edilir.",
        'TMS 37 p. 23',
    ),
    # düzey 2
    '0059': patch(
        "Aşağıdakilerden hangileri TMS 37'ye göre doğrudur?\n\nI. Karşılık, kaynak çıkışı muhtemel ve tutarı güvenilir tahmin edilebilen mevcut yükümlülük için tanınır\n\nII. Koşullu borç finansal tablolara borç olarak alınır\n\nIII. Koşullu varlık, ekonomik fayda girişi muhtemelse açıklanır",
        {
            'A': 'I ve III',
            'B': 'I ve II',
            'C': 'Yalnız III',
            'D': 'Yalnız I',
            'E': 'I, II ve III',
        },
        'A',
        "TMS 37 p. 14'e göre karşılık tanıma koşulları (I) ve p. 89'a göre koşullu varlığın açıklanması (III) doğrudur. p. 27'ye göre koşullu borç **finansal tablolara alınmaz**, açıklanır (II yanlış).",
        'TMS 37 p. 14, 27, 31',
    ),
    # düzey 3
    '0060': patch(
        'Aşağıdakilerden hangileri doğrudur?\n\nI. Gelecekteki faaliyet zararları için karşılık ayrılmaz\n\nII. Ekonomik açıdan dezavantajlı sözleşmeden doğan mevcut yükümlülük karşılık olarak tanınır\n\nIII. Yeniden yapılandırma kararının yönetim kurulunda alınması tek başına zımni mükellefiyet doğurur',
        {
            'A': 'Yalnız II',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'II ve III',
            'E': 'Yalnız I',
        },
        'B',
        "TMS 37 p. 63'e göre faaliyet zararı karşılığı ayrılmaz (I); p. 66'ya göre dezavantajlı sözleşme karşılığı tanınır (II). p. 72-75'e göre yalnız yönetim kurulu kararı, ayrıntılı plan ve geçerli beklenti olmadan **mükellefiyet doğurmaz** (III yanlış).",
        'TMS 37 p. 63, 66, 72',
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
    print(f"1 paket / {len(PATCHES)} soru ('TMS 37 Karsiliklar, Kosullu Borclar ve Kosullu Varliklar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
