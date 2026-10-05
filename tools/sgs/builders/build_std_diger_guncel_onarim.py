#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Diger Guncel Standartlar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

TFRS 5/15/3/13, TMS 41/34 karma paketindeki 60 soru korunarak onarildi: genisletilmis ELEME_ISARETI olcutune gore 59 mutlak ifadeli celdirici ayni dogruluk degerini koruyacak bicimde yeniden yazildi; gerekce tasiyan 11 dogru sik kisaltildi. Kor ogrenci %35 -> %24 (UYARI kapandi).

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: KGK TFRS 5, TFRS 15, TFRS 3, TFRS 13, TMS 41, TMS 34
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/diger_guncel_standartlar.json"
STYLE_REF = 'SGS Muhasebe Standartlari diger guncel TMS/TFRS'
ONEK = "std-diger-gen-"


def patch(stem, options, answer, solution, ref='KGK TFRS 5, TFRS 15, TFRS 3, TFRS 13, TMS 41, TMS 34'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "TFRS 5'e göre bir duran varlığın satış amaçlı elde tutulan olarak sınıflandırılabilmesi için aşağıdakilerden hangisi aranmaz?",
        {
            'A': 'Varlığın mevcut durumunda derhâl satılabilir olması',
            'B': 'Yönetimin satış planını onaylamış ve alıcı aramaya başlamış olması',
            'C': 'Satışın yüksek olasılıklı olması',
            'D': 'Satışın bir yıl içinde tamamlanmasının beklenmesi',
            'E': 'Varlığın satışına ilişkin sözleşmenin imzalanmış olması',
        },
        'E',
        'TFRS 5 par. 7-8: sınıflandırma için varlığın mevcut durumunda derhâl satılabilir olması ve satışın yüksek olasılıklı olması aranır. Yüksek olasılık; yönetimin planı onaylaması, aktif alıcı arayışı ve satışın bir yıl içinde tamamlanmasının beklenmesiyle desteklenir. Sözleşmenin imzalanmış olması koşul değildir.',
        'TFRS 5 par. 7-8',
    ),
    # düzey 2
    '0002': patch(
        "TFRS 5'e göre satış amaçlı elde tutulan duran varlıkların finansal durum tablosundaki sunumu bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Özkaynaklardan indirim kalemi olarak gösterilir',
            'B': 'Diğer varlıklardan ayrı olarak ve dönen varlıklar içinde gösterilir',
            'C': 'Dipnotta açıklanır, tabloda ayrı satır açılmaz',
            'D': 'Stoklar içinde ve maliyet bedeliyle gösterilir',
            'E': 'Duran varlıklar içinde eski sınıfında gösterilir; sınıflandırma dipnotta belirtilir',
        },
        'B',
        'TFRS 5 par. 38: satış amaçlı elde tutulan duran varlıklar ve elden çıkarılacak gruplar finansal durum tablosunda diğer varlıklardan ayrı olarak sunulur; kısa sürede satılacakları için dönen varlıklar bölümünde yer alır.',
        'TFRS 5 par. 38',
    ),
    # düzey 3
    '0003': patch(
        "Satış amaçlı elde tutulan bir varlığın satış maliyeti düşülmüş gerçeğe uygun değeri sonraki dönemde artmıştır. TFRS 5'e göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Daha önce muhasebeleştirilen değer düşüklüğü zararını aşmayan tutarda kazanç kaydedilir',
            'B': 'Artış diğer kapsamlı gelirde muhasebeleştirilir',
            'C': 'Artış varlık satıldığında kâr olarak kaydedilir',
            'D': 'Artışın tamamı sınırsız biçimde kazanç olarak kaydedilir; defter değeri sınıflandırma öncesindeki tutarı aşabilir',
            'E': 'Artış kaydedilmez; varlık düşük değerinde bırakılır',
        },
        'A',
        'TFRS 5 par. 21-22: sonraki artışlardan doğan kazanç muhasebeleştirilir; ancak daha önce bu standart veya TMS 36 uyarınca muhasebeleştirilmiş birikmiş değer düşüklüğü zararını aşamaz. Defter değeri hiçbir durumda önceki tutarının üzerine çıkarılamaz.',
        'TFRS 5 par. 21-22',
    ),
    # düzey 2
    '0004': patch(
        "TFRS 5'e göre durdurulan faaliyet kavramı bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Geçici olarak üretimine ara verilen her üretim hattını anlatır; faaliyetin ayrı bir ana alanı temsil etmesi aranmaz',
            'B': 'İşletmenin kârlılığı düşen her ürün grubunu anlatır',
            'C': 'Yurt dışında yürütülen faaliyetleri anlatır',
            'D': 'Tasfiyeye giren bağlı ortaklıkları anlatır',
            'E': 'Elden çıkarılan veya satış amaçlı elde tutulan, ayrı bir ana faaliyet alanını temsil eden bölümdür',
        },
        'E',
        'TFRS 5 Ek A: durdurulan faaliyet, elden çıkarılan veya satış amaçlı elde tutulan olarak sınıflandırılan ve ayrı bir ana faaliyet alanını ya da coğrafi bölümü temsil eden işletme bölümüdür. Kârlılığın düşmesi veya üretime ara verilmesi tek başına yeterli değildir.',
        'TFRS 5 Ek A',
    ),
    # düzey 3
    '0005': patch(
        "İşletme 15 Kasım'da bir üretim hattını satış amaçlı elde tutulan olarak sınıflandırmıştır. Bu tarihteki defter değeri 800.000 ₺, gerçeğe uygun değeri 900.000 ₺ ve satış maliyeti 40.000 ₺'dir. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Varlık 800.000 ₺ ile ölçülür; değer düşüklüğü veya kazanç kaydedilmez',
            'B': 'Varlık 860.000 ₺ ile ölçülür ve 60.000 ₺ kazanç kaydedilir',
            'C': 'Varlık 860.000 ₺ ile ölçülür ve fark özkaynağa alınır',
            'D': 'Varlık 900.000 ₺ ile ölçülür ve 100.000 ₺ kazanç kaydedilir; satış maliyeti ölçümde dikkate alınmaz',
            'E': 'Varlık 760.000 ₺ ile ölçülür ve 40.000 ₺ zarar kaydedilir',
        },
        'A',
        "Satış maliyeti düşülmüş gerçeğe uygun değer 900.000 − 40.000 = 860.000 ₺'dir. TFRS 5 par. 15 düşük olanı öngördüğünden defter değeri 800.000 ₺ korunur. Standart, satış amaçlı sınıflandırmada değer artışının kaydedilmesine izin vermez.",
        'TFRS 5 par. 15',
    ),
    # düzey 2
    '0006': patch(
        "TFRS 15'e göre bir edim yükümlülüğünün zamana yayılı olarak yerine getirilmiş sayılması bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Zamana yayılı devir hizmet sözleşmelerinde uygulanır, mal satışında uygulanmaz',
            'B': 'Sözleşme süresi bir yılı aştığında devir zamana yayılı sayılır; başka ölçüt aranmaz',
            'C': 'Ödemenin taksitle yapılması devri zamana yayılı hâle getirir',
            'D': 'Müşteri, edim yerine getirildikçe eş anlı olarak fayda sağlıyorsa',
            'E': 'Zamana yayılı devir inşaat sözleşmelerine özgüdür',
        },
        'D',
        'TFRS 15 par. 35: üç ölçütten biri sağlanırsa edim zamana yayılı yerine getirilmiş sayılır — müşterinin eş anlı fayda sağlaması, kontrolü müşteride olan bir varlığın oluşturulması ya da alternatif kullanımı olmayan bir varlıkla birlikte tamamlanan kısım için ödeme hakkının bulunması.',
        'TFRS 15 par. 35',
    ),
    # düzey 2
    '0007': patch(
        "TFRS 15'e göre değişken bedel bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Değişken bedel sözleşme sonunda toplu olarak kaydedilir; ara dönemde tahmin yapılmaz',
            'B': 'Değişken bedel sözleşmedeki azami tutarla ölçülür',
            'C': 'Değişken bedel belirsizlik giderilene kadar dikkate alınmaz',
            'D': 'Değişken bedel doğrudan özkaynağa yansıtılır',
            'E': 'Beklenen değer veya en olası tutar yöntemiyle tahmin edilir',
        },
        'E',
        'TFRS 15 par. 53 ve 56: değişken bedel, beklenen değer ya da en olası tutar yöntemlerinden durumu daha iyi yansıtanla tahmin edilir. Par. 56 uyarınca hasılat tutarında önemli ölçüde tersine dönme olmayacağı yüksek olasılıkla söylenebildiği ölçüde işlem bedeline dâhil edilir.',
        'TFRS 15 par. 53-56',
    ),
    # düzey 3
    '0008': patch(
        "Bir işletme müşterisine iki yıl vadeli satış yapmış ve peşin fiyatın üzerinde bir bedel belirlemiştir. TFRS 15'e göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Vadeli bedelin tamamı satış hasılatı olarak kaydedilir',
            'B': 'Aradaki fark stok maliyetinden indirilir',
            'C': 'Hasılat tahsilat gerçekleştikçe nakit esasına göre kaydedilir; vade farkı ayrıca ayrıştırılmaz',
            'D': 'Hasılat peşin fiyattan ölçülür, fark faiz geliri olur',
            'E': 'Aradaki fark doğrudan özkaynağa alınır',
        },
        'D',
        'TFRS 15 par. 60-61: sözleşmede önemli bir finansman bileşeni bulunduğunda işlem bedeli, müşterinin peşin ödemesi hâlinde ödeyeceği fiyata indirgenir. Aradaki fark sözleşme süresince faiz geliri olarak muhasebeleştirilir.',
        'TFRS 15 par. 60-61',
    ),
    # düzey 2
    '0009': patch(
        "TFRS 15'e göre garantiler ile ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Ürünün kararlaştırılan özelliklere uygunluğunu güvenceye alan garanti TMS 37 kapsamındadır',
            'B': "Müşterinin ayrıca satın alabildiği garanti TMS 37'ye göre karşılıkla izlenir",
            'C': 'Güvenceye ek hizmet sunan garanti ayrı bir edim yükümlülüğü olabilir',
            'D': 'Garantinin kanunen zorunlu olması, ayrı bir edim yükümlülüğü olmadığına işaret eder',
            'E': 'Garanti süresinin uzunluğu değerlendirmede dikkate alınır',
        },
        'B',
        "TFRS 15 B28-B33: müşterinin garantiyi ayrıca satın alma seçeneği varsa garanti ayrı bir edim yükümlülüğüdür ve işlem bedelinin bir kısmı ona dağıtılır. Yalnızca kararlaştırılan özelliklere uygunluğu güvenceye alan garanti TMS 37'ye göre karşılıkla izlenir. Kanuni zorunluluk ve garanti süresi değerlendirmede dikkate alınan göstergelerdir.",
        'TFRS 15 par. B28-B33',
    ),
    # düzey 2
    '0010': patch(
        "TMS 41'e göre hasat edilen tarımsal ürünler bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Hasat edilen ürünler duran varlık olarak sınıflandırılır',
            'B': 'Hasat edilen ürünler için ölçüm yapılmaz',
            'C': 'Hasatta satış maliyeti düşülmüş gerçeğe uygun değerle ölçülür',
            'D': 'Hasat noktasında maliyet bedeliyle ölçülür',
            'E': 'Hasat sonrasında da TMS 41 hükümleri uygulanmaya devam eder',
        },
        'C',
        "TMS 41 par. 13: canlı varlıklardan hasat edilen tarımsal ürünler, hasat noktasındaki gerçeğe uygun değerinden satış maliyetleri düşülmek suretiyle ölçülür. Bu tutar TMS 2 uygulamasında maliyet olarak kabul edilir ve sonraki ölçüm TMS 2'ye tabidir.",
        'TMS 41 par. 13',
    ),
    # düzey 2
    '0011': patch(
        'TMS 41 kapsamındaki tarımsal faaliyet bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tarım makinelerinin üretilmesi ve satılmasıdır',
            'B': 'Hasat sonrası ürünlerin işlenerek mamule dönüştürülmesidir; biyolojik dönüşümün yönetilmesi aranmaz',
            'C': 'Tarım ürünlerinin toptan ticaretini yapmaktır',
            'D': 'Doğada yabani olarak yetişen ürünlerin toplanmasıdır',
            'E': 'Canlı varlıkların biyolojik dönüşümünün ve hasadının işletmece yönetilmesidir',
        },
        'E',
        'TMS 41 par. 5-6: tarımsal faaliyet, satışa veya tarımsal ürüne ya da ilave canlı varlığa dönüştürülmek üzere canlı varlıkların biyolojik dönüşümünün ve hasadının bir işletme tarafından yönetilmesidir. Yönetimin bulunmadığı doğal toplama ve hasat sonrası işleme kapsam dışıdır.',
        'TMS 41 par. 5-6',
    ),
    # düzey 2
    '0012': patch(
        "TMS 41'e göre canlı varlıkların finansal durum tablosunda sunulması bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Canlı varlıklar stoklar içinde birleştirilerek gösterilir',
            'B': 'Canlı varlıklar maddi duran varlıklar içinde gösterilir',
            'C': 'Canlı varlıklar ayrı bir kalem olarak gösterilir',
            'D': 'Canlı varlıklar özkaynaklarda ayrı kalem olarak gösterilir',
            'E': 'Canlı varlıklar dipnotta gösterilir',
        },
        'C',
        'TMS 41 par. 39: işletme canlı varlıkların defter değerini finansal durum tablosunda ayrı bir kalem olarak sunar. Tüketilebilir ve taşıyıcı canlı varlıklar ile olgunlaşmış ve olgunlaşmamış varlıklar arasındaki ayrım da açıklanır.',
        'TMS 41 par. 39',
    ),
    # düzey 3
    '0013': patch(
        "TFRS 3'e göre satın alma yönteminin uygulanmasında aşağıdakilerden hangisi gerekli DEĞİLDİR?",
        {
            'A': 'Tanımlanabilir varlık ve borçlar ile kontrol gücü olmayan payların muhasebeleştirilmesi',
            'B': 'Şerefiye ya da pazarlıklı satın alım kazancının muhasebeleştirilmesi',
            'C': 'Edinim tarihinin belirlenmesi',
            'D': 'Edinen işletmenin belirlenmesi',
            'E': 'Edinilen işletmenin geçmiş dönem finansal tablolarının yeniden düzenlenmesi',
        },
        'E',
        'TFRS 3 par. 5: satın alma yöntemi dört adımdan oluşur — edinen işletmenin belirlenmesi, edinim tarihinin belirlenmesi, tanımlanabilir varlık/borçlar ile kontrol gücü olmayan payların muhasebeleştirilip ölçülmesi ve şerefiye veya pazarlıklı satın alım kazancının muhasebeleştirilmesi. Geçmiş tabloların yeniden düzenlenmesi bu yöntemin bir adımı değildir.',
        'TFRS 3 par. 5',
    ),
    # düzey 2
    '0014': patch(
        "TFRS 3'e göre işletme birleşmesinde ortaya çıkan şerefiye bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Faydalı ömrü boyunca doğrudan itfa edilir; ayrıca değer düşüklüğü testi yapılmaz',
            'B': 'İtfaya tabi tutulmaz; yılda en az bir kez değer düşüklüğü testine tabidir',
            'C': 'Satış hâlinde ölçülür',
            'D': 'Edinim yılında gider yazılır',
            'E': 'Her yıl yeniden değerlemeye tabi tutulur',
        },
        'B',
        'TFRS 3 ve TMS 36 par. 10: işletme birleşmesinde edinilen şerefiye itfa edilmez; her yıl ve değer düşüklüğü belirtisi bulunduğunda değer düşüklüğü testine tabi tutulur. Kaydedilen değer düşüklüğü sonraki dönemlerde iptal edilemez.',
        'TFRS 3 · TMS 36 par. 10',
    ),
    # düzey 2
    '0015': patch(
        "TFRS 3'e göre kontrol gücü olmayan payların (KGOP) ölçümü bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'KGOP finansal tablolara alınmaz',
            'B': 'KGOP sıfır kabul edilir',
            'C': 'Gerçeğe uygun değerle ya da oransal pay ile ölçülebilir',
            'D': 'Gerçeğe uygun değerle ölçülür; oransal pay seçeneği bulunmaz',
            'E': 'Defter değeriyle ölçülür',
        },
        'C',
        "TFRS 3 par. 19: edinen işletme her bir birleşme için KGOP'u gerçeğe uygun değerinden ya da edinilenin net tanımlanabilir varlıklarındaki oransal payı üzerinden ölçmeyi seçebilir. Birinci seçenek tam şerefiye, ikincisi kısmi şerefiye sonucunu doğurur.",
        'TFRS 3 par. 19',
    ),
    # düzey 2
    '0016': patch(
        "TFRS 13'e göre gerçeğe uygun değer bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Piyasa katılımcıları arasındaki olağan işlemde varlığın satış fiyatıdır',
            'B': 'Varlığın kayıtlı defter değeridir',
            'C': 'Varlığın edinilmesi için ödenecek giriş fiyatıdır',
            'D': 'Varlığın vergi mevzuatına göre belirlenen değeridir; piyasa katılımcılarının varsayımları dikkate alınmaz',
            'E': 'Varlığın yerine konma (ikame) maliyetidir',
        },
        'A',
        'TFRS 13 par. 9: gerçeğe uygun değer, ölçüm tarihinde piyasa katılımcıları arasındaki olağan bir işlemde bir varlığın satışından elde edilecek veya bir borcun devrinde ödenecek fiyattır. Bir çıkış fiyatıdır; giriş fiyatı veya ikame maliyeti değildir.',
        'TFRS 13 par. 9',
    ),
    # düzey 2
    '0017': patch(
        "TFRS 13'e göre finansal olmayan bir varlığın gerçeğe uygun değeri ölçülürken aşağıdakilerden hangisi esas alınır?",
        {
            'A': 'Varlığın yasal olarak izin verilen tek kullanımı',
            'B': 'Varlığın piyasa katılımcılarınca en yüksek ve en iyi kullanımı',
            'C': 'Varlığın işletmedeki mevcut fiili kullanımı',
            'D': 'Varlığın işletme yönetimince planlanan gelecekteki kullanımı',
            'E': 'Varlığın edinildiği tarihteki kullanım amacı',
        },
        'B',
        'TFRS 13 par. 27-28: finansal olmayan varlığın gerçeğe uygun değeri, piyasa katılımcılarının varlığı en yüksek ve en iyi şekilde kullanarak elde edecekleri ekonomik faydayı dikkate alır. Bu kullanım fiziken mümkün, hukuken izin verilebilir ve finansal açıdan uygulanabilir olmalıdır.',
        'TFRS 13 par. 27-28',
    ),
    # düzey 2
    '0018': patch(
        "TFRS 13'ün kapsamı bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Standart borsaya kote işletmeleri kapsar',
            'B': 'Standart ilk muhasebeleştirmede uygulanır',
            'C': 'Standart finansal araçlara uygulanır',
            'D': 'Standart ölçümün nasıl yapılacağını düzenler; hangi kalemin gerçeğe uygun değerle ölçüleceğini ilgili standart belirler',
            'E': 'Standart hangi varlıkların gerçeğe uygun değerle ölçüleceğini de belirler; ilgili standartların bu konuda bir rolü bulunmaz',
        },
        'D',
        'TFRS 13 par. 5-7: standart, başka bir TFRS gerçeğe uygun değerle ölçüm gerektirdiğinde ya da izin verdiğinde ölçümün nasıl yapılacağını ve neyin açıklanacağını düzenler. Hangi kalemin bu değerle ölçüleceğine ilgili standart karar verir.',
        'TFRS 13 par. 5-7',
    ),
    # düzey 2
    '0019': patch(
        "TMS 34'e göre ara dönemde uygulanacak muhasebe politikaları ve ölçümle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Sonraki yıllık tablolara yansıyacak politika değişikliği ara dönemde de uygulanır',
            'B': 'Ara dönemde yıllık tablolardan farklı, basitleştirilmiş politikalar uygulanır',
            'C': 'Ara dönem ölçümleri yılbaşından bugüne esasına göre yapılır',
            'D': 'Raporlama sıklığı yıllık sonuçların ölçümünü etkilememelidir',
            'E': 'Ara dönem, bir tam yıldan kısa bir finansal raporlama dönemidir',
        },
        'B',
        'TMS 34.28: işletme ara dönem finansal tablolarında yıllık finansal tablolarında uyguladığı muhasebe politikalarının aynısını uygular; sonraki yıllık tablolara yansıyacak politika değişiklikleri bunun istisnasıdır. Raporlama sıklığı yıllık sonuçların ölçümünü etkilememeli, ara dönem ölçümleri yılbaşından bugüne esasına göre yapılmalıdır.',
        'TMS 34 par. 28',
    ),
    # düzey 2
    '0020': patch(
        "TMS 34'e göre ara dönemde gelir vergisi gideri nasıl hesaplanır?",
        {
            'A': 'Peşin ödenen vergiler gider yazılarak',
            'B': 'Yıllık toplam kazanç için beklenen ağırlıklı ortalama efektif vergi oranı uygulanarak',
            'C': 'Ara dönem kazancına yasal vergi oranı doğrudan uygulanarak',
            'D': 'Vergi gideri ara dönemde hesaplanmaz',
            'E': 'Bir önceki yılın fiilî vergi tutarının dörtte biri alınarak; cari yıl tahminleri hesaba katılmaz',
        },
        'B',
        'TMS 34 par. B12: ara dönem gelir vergisi gideri, yıllık toplam kazanç için beklenen ağırlıklı ortalama yıllık efektif gelir vergisi oranının ara dönem kazancına uygulanmasıyla tahakkuk ettirilir.',
        'TMS 34 par. B12',
    ),
    # düzey 2
    '0021': patch(
        "TFRS 5'e göre satış amaçlı elde tutulan olarak sınıflandırılan bir duran varlık hangi değerle ölçülür?",
        {
            'A': 'Defter değeri ile gerçeğe uygun değerinden satış maliyetleri düşülmüş tutarın düşük olanı',
            'B': 'Gerçeğe uygun değeriyle',
            'C': "Geri kazanılabilir tutar ile kullanım değerinin yüksek olanı; bu ölçüm TMS 36'daki değer düşüklüğü testiyle aynıdır",
            'D': 'Defter değeri ile net gerçekleşebilir değerin yüksek olanı',
            'E': 'Sınıflandırma öncesi defter değeriyle',
        },
        'A',
        'TFRS 5 par. 15: satış amaçlı elde tutulan olarak sınıflandırılan duran varlık, defter değeri ile gerçeğe uygun değerinden satış maliyetleri düşülmüş tutarın DÜŞÜK olanı üzerinden ölçülür.',
        'TFRS 5 par. 15',
    ),
    # düzey 2
    '0022': patch(
        "TFRS 5'e göre durdurulan faaliyetlerin kâr veya zarar tablosunda sunumu bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Vergi öncesi tutarla ve satış hasılatı içinde gösterilir',
            'B': 'Sürdürülen faaliyet gelirleriyle birleştirilerek sunulur',
            'C': 'Diğer kapsamlı gelirde sunulur',
            'D': 'Vergi sonrası tek bir tutar olarak ayrı gösterilir',
            'E': 'Özkaynak değişim tablosunda gösterilir',
        },
        'D',
        'TFRS 5 par. 33: durdurulan faaliyetlerin vergi sonrası kâr veya zararı ile elden çıkarma kazanç/kaybının vergi sonrası tutarı, kâr veya zarar tablosunda tek bir tutar olarak ayrıca sunulur. Böylece kullanıcı sürdürülen faaliyetlerin sonucunu ayırt edebilir.',
        'TFRS 5 par. 33',
    ),
    # düzey 3
    '0023': patch(
        "Bir işletme satış amaçlı elde tutulan olarak sınıflandırdığı varlığı satmaktan vazgeçmiştir. TFRS 5'e göre varlık hangi tutarla ölçülür?",
        {
            'A': 'Sınıflandırma yapılmasaydı ulaşılacak defter değeri ile geri kazanılabilir tutarın düşük olanı',
            'B': 'Ölçüm değişmez; varlık satış amaçlı grupta bırakılır',
            'C': 'Sınıflandırma tarihindeki defter değeriyle aynen ölçülür; sınıflandırma süresince ayrılmayan amortismanlar dikkate alınmaz',
            'D': 'İlk maliyet bedeline geri döndürülerek ölçülür',
            'E': 'Vazgeçme tarihindeki gerçeğe uygun değeriyle ölçülür',
        },
        'A',
        'TFRS 5 par. 27: sınıflandırma ölçütleri artık sağlanmıyorsa varlık gruptan çıkarılır ve sınıflandırma yapılmamış olsaydı ulaşılacak defter değeri (amortismanlar dâhil düzeltilmiş) ile karar tarihindeki geri kazanılabilir tutarın düşük olanıyla ölçülür.',
        'TFRS 5 par. 27',
    ),
    # düzey 2
    '0024': patch(
        'TFRS 5 kapsamına girmeyen kalemler bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Stoklar da satış amaçlı elde tutulan olarak sınıflandırılır',
            'B': 'Şerefiye standardın kapsamı dışında bırakılmıştır',
            'C': 'Standardın ölçüm hükümleri istisnasız tüm varlıklara uygulanır; ertelenmiş vergi varlıkları da bu hükümlere tabidir',
            'D': 'Standardın kapsamı maddi duran varlıklarla sınırlıdır',
            'E': 'Ertelenmiş vergi varlıkları ve çalışanlara sağlanan fayda varlıkları ölçüm hükümlerinin dışındadır',
        },
        'E',
        'TFRS 5 par. 5: ertelenmiş vergi varlıkları, çalışanlara sağlanan faydalara ilişkin varlıklar, TFRS 9 kapsamındaki finansal varlıklar, gerçeğe uygun değerle ölçülen yatırım amaçlı gayrimenkuller ve TMS 41 kapsamındaki varlıklar ölçüm hükümlerinin dışındadır.',
        'TFRS 5 par. 5',
    ),
    # düzey 2
    '0025': patch(
        "TFRS 5'e göre satış amaçlı elde tutulan varlıkların açıklanması bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Satış bedeli açıklanır, başka bilgi verilmez',
            'B': 'Açıklama yükümlülüğü halka açık işletmelere özgüdür; diğerleri dipnot düzenlemez',
            'C': 'Açıklama durdurulan faaliyetlerle sınırlıdır',
            'D': 'Varlıkların tanımı, satışa ilişkin olay ve koşullar ile beklenen zamanlama açıklanır',
            'E': 'Satış tamamlanana kadar açıklama yapılmaz',
        },
        'D',
        'TFRS 5 par. 41: satış amaçlı elde tutulan duran varlıkların tanımı, satışa yol açan olay ve koşullar, beklenen satış biçimi ve zamanlaması ile varsa raporlanabilir bölüm bilgisi açıklanır.',
        'TFRS 5 par. 41',
    ),
    # düzey 3
    '0026': patch(
        "Bir aracı işletme, bir ürünü müşteriye 36.000 ₺'ye satmakta ve tedarikçiden bu tutar üzerinden %10 komisyon almaktadır. Ürünün kontrolü müşteriye devredilmeden önce aracıya geçmemektedir. TFRS 15'e göre aracı ne kadar hasılat muhasebeleştirir?",
        {
            'A': '3.600 ₺',
            'B': '39.600 ₺',
            'C': '18.000 ₺',
            'D': '36.000 ₺',
            'E': '32.400 ₺',
        },
        'A',
        'TFRS 15 par. B34-B38: işletme, malın kontrolünü devretmeden önce elinde bulundurmuyorsa vekil konumundadır ve hasılatı brüt tutar üzerinden değil, elde ettiği komisyon (net tutar) üzerinden muhasebeleştirir: 36.000 × %10 = 3.600 ₺.',
        'TFRS 15 par. B34-B38',
    ),
    # düzey 2
    '0027': patch(
        "TFRS 15'e göre sözleşme varlığı ile alacak arasındaki fark bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Sözleşme varlığında bedeli isteme hakkı koşulsuzdur',
            'B': 'Sözleşme varlığı özkaynak kalemidir',
            'C': 'Alacakta hak koşulsuzdur; sözleşme varlığında bir koşula bağlıdır',
            'D': 'İkisi aynı kalemdir; ayrım bir sunum tercihidir ve koşulsuz hak ölçütü kullanılmaz',
            'E': 'Alacak peşin tahsilatlarda doğar',
        },
        'C',
        'TFRS 15 par. 105-108: işletmenin bedeli isteme hakkı koşulsuz hâle geldiğinde alacak muhasebeleştirilir. Hak, yalnızca zamanın geçmesinden başka bir koşula (örneğin başka bir edimin tamamlanmasına) bağlıysa sözleşme varlığı gösterilir.',
        'TFRS 15 par. 105-108',
    ),
    # düzey 2
    '0028': patch(
        "TFRS 15'e göre sözleşmenin elde edilmesine yönelik ek maliyetler bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Bu maliyetler sözleşme iptal edilirse gider yazılır; sözleşme sürerken izlenmez',
            'B': 'Bu maliyetler stok maliyetine eklenir',
            'C': 'Bu maliyetler oluştuğu dönemde gider yazılır',
            'D': 'Geri kazanılması bekleniyorsa varlık olarak muhasebeleştirilir',
            'E': 'Bu maliyetler doğrudan özkaynaklardan indirilir',
        },
        'D',
        'TFRS 15 par. 91-99: sözleşmenin elde edilmesine ilişkin ek maliyetler (örneğin satış primi) geri kazanılması bekleniyorsa varlık olarak muhasebeleştirilir ve ilgili mal veya hizmetin devriyle tutarlı biçimde itfa edilir. İtfa süresi bir yılı aşmıyorsa gider yazma kolaylığı uygulanabilir.',
        'TFRS 15 par. 91-99',
    ),
    # düzey 2
    '0029': patch(
        "TMS 41'e göre canlı varlıklar ilk muhasebeleştirmede hangi değerle ölçülür?",
        {
            'A': 'Maliyet bedeliyle',
            'B': 'Vergi değeriyle',
            'C': 'Gerçeğe uygun değerinden satış maliyetleri düşülmüş tutarla',
            'D': 'Yeniden üretim maliyetiyle',
            'E': 'Net gerçekleşebilir değerle; satış maliyetleri ayrıca düşülmez',
        },
        'C',
        'TMS 41 par. 12: canlı varlıklar ilk muhasebeleştirmede ve her raporlama dönemi sonunda gerçeğe uygun değerinden satış maliyetleri düşülmek suretiyle ölçülür.',
        'TMS 41 par. 12',
    ),
    # düzey 2
    '0030': patch(
        "TMS 41'e göre taşıyıcı bitkiler (meyve veren ağaçlar gibi) ile ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Taşıyıcı bitki birden fazla dönem ürün vermesi beklenen bitkidir',
            'B': 'Taşıyıcı bitki üzerindeki ürün TMS 41 kapsamında kalır',
            'C': 'Canlı varlık olarak satış maliyeti düşülmüş gerçeğe uygun değerle ölçülür',
            'D': 'Meyve veren ağaçlar taşıyıcı bitki örneğidir',
            'E': 'Taşıyıcı bitkinin hurda olarak satılma ihtimali çok düşüktür',
        },
        'C',
        'TMS 41.5 ve 41.5A: taşıyıcı bitki, tarımsal ürün üretiminde kullanılan, birden fazla dönem ürün vermesi beklenen ve hurda olarak satılma ihtimali çok düşük olan bitkidir. Taşıyıcı bitkiler TMS 16 kapsamında maddi duran varlık olarak muhasebeleştirilir; üzerindeki ürün ise TMS 41 kapsamında kalır.',
        'TMS 41 par. 5B-5C',
    ),
    # düzey 2
    '0031': patch(
        "TMS 41'e göre koşula bağlı olmayan devlet teşvikleri bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Doğrudan özkaynaklara aktarılır',
            'B': 'Ertelenmiş gelir olarak kaydedilip varlığın ömrüne yayılır',
            'C': 'Dipnotta açıklanır, kâr veya zarara yansıtılmaz',
            'D': 'Canlı varlığın maliyetinden indirilir',
            'E': 'Alacak hâline geldiğinde kâr veya zarara yansıtılır',
        },
        'E',
        'TMS 41 par. 34: gerçeğe uygun değerinden satış maliyetleri düşülerek ölçülen canlı varlıkla ilgili koşulsuz devlet teşviki, yalnızca alacak hâline geldiğinde kâr veya zarara yansıtılır. Koşullu teşvik ise koşullar yerine getirildiğinde muhasebeleştirilir.',
        'TMS 41 par. 34',
    ),
    # düzey 3
    '0032': patch(
        "Bir çiftlikte 200 baş besi sığırının dönem sonundaki gerçeğe uygun değeri baş başına 48.000 ₺, tahmini satış maliyeti baş başına 1.500 ₺'dir. Dönem başındaki kayıtlı değer 8.400.000 ₺ olduğuna göre kâr veya zarara yansıyacak tutar kaç ₺'dir?",
        {
            'A': '300.000 ₺ kazanç',
            'B': '1.200.000 ₺ kazanç',
            'C': '900.000 ₺ kayıp',
            'D': '900.000 ₺ kazanç',
            'E': '9.300.000 ₺ kazanç',
        },
        'D',
        "Dönem sonu ölçüm değeri: 200 × (48.000 − 1.500) = 200 × 46.500 = 9.300.000 ₺. Dönem başı kayıtlı değer 8.400.000 ₺ olduğundan artış 9.300.000 − 8.400.000 = 900.000 ₺'dir. TMS 41 par. 26 uyarınca bu tutar dönemin kâr veya zararına yansıtılır.",
        'TMS 41 par. 12, 26',
    ),
    # düzey 2
    '0033': patch(
        "TFRS 3'e göre pazarlıklı satın alımdan doğan kazanç (negatif şerefiye) nereye yansıtılır?",
        {
            'A': 'Edinim tarihinde kâr veya zarara',
            'B': 'Diğer kapsamlı gelire',
            'C': 'Gelecek dönemlere yayılarak',
            'D': 'Doğrudan özkaynaklara',
            'E': 'Şerefiyeden indirim olarak',
        },
        'A',
        'TFRS 3 par. 34-36: edinilen net tanımlanabilir varlıkların gerçeğe uygun değeri transfer edilen bedeli aşıyorsa fark pazarlıklı satın alım kazancıdır. Edenen işletme önce ölçüm ve tanımlamaları yeniden gözden geçirir, kazanç doğruluyorsa edinim tarihinde kâr veya zarara yansıtır.',
        'TFRS 3 par. 34-36',
    ),
    # düzey 3
    '0034': patch(
        "(A) A.Ş., (B) Ltd.'nin %100 payını 5.000.000 ₺'ye edinmiştir. Edinim tarihinde (B)'nin tanımlanabilir varlıklarının gerçeğe uygun değeri 7.200.000 ₺, üstlendiği borçların gerçeğe uygun değeri 2.900.000 ₺'dir. TFRS 3'e göre ortaya çıkan tutar nedir?",
        {
            'A': '2.200.000 ₺ şerefiye',
            'B': '700.000 ₺ pazarlıklı satın alım kazancı',
            'C': '300.000 ₺ pazarlıklı satın alım kazancı',
            'D': '4.300.000 ₺ şerefiye',
            'E': '700.000 ₺ şerefiye',
        },
        'E',
        'Net tanımlanabilir varlık = 7.200.000 − 2.900.000 = 4.300.000 ₺. Transfer edilen bedel 5.000.000 ₺ bunu aştığından fark şerefiyedir: 5.000.000 − 4.300.000 = 700.000 ₺. TFRS 3 par. 32 uyarınca bedel net varlığı aşarsa şerefiye, altında kalırsa pazarlıklı satın alım kazancı doğar.',
        'TFRS 3 par. 32',
    ),
    # düzey 2
    '0035': patch(
        "TFRS 3'e göre edinim tarihi bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Genel kurulun birleşmeyi onayladığı tarihtir; kontrolün fiilen geçtiği tarih dikkate alınmaz',
            'B': 'Ticaret siciline tescil edildiği tarihtir',
            'C': 'Edinen işletmenin edinilen üzerindeki kontrolü fiilen ele geçirdiği tarihtir',
            'D': 'Birleşme sözleşmesinin imzalandığı tarihtir',
            'E': 'Bedelin son taksitinin ödendiği tarihtir',
        },
        'C',
        'TFRS 3 par. 8-9: edinim tarihi, edinen işletmenin edinilen işletme üzerindeki kontrolü elde ettiği tarihtir. Bu genellikle bedelin transfer edildiği ve varlıkların devralındığı tarih olsa da belirleyici olan kontrolün fiilen geçmesidir.',
        'TFRS 3 par. 8-9',
    ),
    # düzey 2
    '0036': patch(
        "TFRS 13'te yer alan değerleme yöntemleri aşağıdakilerden hangisidir?",
        {
            'A': 'Tarihî maliyet, cari maliyet ve nominal değer yöntemleri',
            'B': 'Piyasa yaklaşımı, maliyet yaklaşımı ve gelir yaklaşımı',
            'C': 'Doğrusal, azalan bakiye ve üretim miktarı yöntemleri',
            'D': 'Brüt, net ve karma değerleme yöntemleri',
            'E': 'İlk giren ilk çıkar, ortalama maliyet ve özel maliyet yöntemleri',
        },
        'B',
        'TFRS 13 par. 62: gerçeğe uygun değer ölçümünde piyasa yaklaşımı, maliyet yaklaşımı ve gelir yaklaşımı kullanılır. İşletme koşullara uygun ve gözlemlenebilir girdileri azami ölçüde kullanan yöntemi seçer.',
        'TFRS 13 par. 62',
    ),
    # düzey 2
    '0037': patch(
        "TFRS 13'e göre gerçeğe uygun değer ölçümünde esas alınacak piyasa bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İşletmenin bulunduğu ülkenin piyasası esas alınır',
            'B': 'Asıl piyasa; asıl piyasa yoksa en avantajlı piyasa esas alınır',
            'C': 'En avantajlı piyasa esas alınır',
            'D': 'Piyasa seçimi işletmenin serbest tercihine bırakılmıştır',
            'E': 'En düşük fiyatın oluştuğu piyasa esas alınır',
        },
        'B',
        'TFRS 13 par. 16: ölçüm, varlık veya borca ilişkin asıl piyasada gerçekleşeceği varsayılan işlem esas alınarak yapılır. Asıl piyasa bulunmuyorsa en avantajlı piyasadaki fiyat kullanılır.',
        'TFRS 13 par. 16',
    ),
    # düzey 3
    '0038': patch(
        "30 Eylül 2025 tarihli ara dönem finansal durum tablosunu sunan bir işletme, TMS 34'e göre bunu hangi tarihli tabloyla karşılaştırmalı olarak verir?",
        {
            'A': '1 Ocak 2025 tarihli açılış tablosuyla',
            'B': '31 Aralık 2025 tarihli tahmini tabloyla',
            'C': '30 Eylül 2024 tarihli ara dönem tablosuyla',
            'D': '30 Haziran 2025 tarihli ara dönem tablosuyla',
            'E': '31 Aralık 2024 tarihli yıl sonu finansal durum tablosuyla',
        },
        'E',
        'TMS 34 par. 20(a): ara dönem finansal durum tablosu, bir önceki hesap dönemi sonu (yıl sonu) tarihli finansal durum tablosuyla karşılaştırmalı olarak sunulur. Kâr veya zarar tablosunda ise önceki yılın karşılaştırılabilir ara dönemi kullanılır.',
        'TMS 34 par. 20',
    ),
    # düzey 2
    '0039': patch(
        "TMS 34'e göre ara dönem finansal raporun asgari içeriği bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Ara dönemde dipnot sunulmaz',
            'B': 'Yönetim kurulu faaliyet raporu sunulur',
            'C': 'Özet finansal tablolar ve seçilmiş açıklayıcı dipnotlar yeterlidir',
            'D': 'Yıllık finansal tabloların tamamı aynı ayrıntıyla sunulur; özet sunum seçeneği bulunmaz',
            'E': 'Kâr veya zarar tablosu sunulur',
        },
        'C',
        'TMS 34 par. 8 ve 10: ara dönem finansal rapor asgari olarak özet finansal durum tablosu, özet kâr veya zarar ve diğer kapsamlı gelir tablosu, özet özkaynak değişim tablosu, özet nakit akış tablosu ve seçilmiş açıklayıcı dipnotları içerir. İşletme tam set sunmayı da seçebilir.',
        'TMS 34 par. 8, 10',
    ),
    # düzey 2
    '0040': patch(
        "TMS 34'e göre mevsimsel veya dönemsel olarak elde edilen gelirler bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Hesap dönemi içinde eşitlenerek dağıtılmaz; oluştuğu ara dönemde muhasebeleştirilir',
            'B': 'Doğrudan özkaynaklara aktarılır',
            'C': 'Tahmini yıllık tutar üzerinden peşinen kaydedilir',
            'D': 'Yıla eşit biçimde dağıtılarak her ara döneme paylaştırılır; gelirin gerçekleştiği dönem dikkate alınmaz',
            'E': 'Yıl sonunda muhasebeleştirilir',
        },
        'A',
        'TMS 34 par. 37: mevsimlik, dönemsel veya arızi olarak elde edilen gelirler, yıllık raporlama döneminde öne alınmaz ya da ertelenmez. Bu gelirler gerçekleştikleri ara dönemde muhasebeleştirilir.',
        'TMS 34 par. 37',
    ),
    # düzey 3
    '0041': patch(
        "Bir işletme 1 Temmuz 2024'te 600.000 ₺'ye aldığı, 10 yıl faydalı ömürlü ve kalıntı değeri olmayan makineyi 1 Ocak 2026'da satış amaçlı elde tutulan varlık olarak sınıflandırmıştır. Bu tarihte makinenin gerçeğe uygun değeri 520.000 ₺, tahmini satış maliyeti 30.000 ₺'dir. Makine hangi tutarla ölçülür?",
        {
            'A': '570.000 ₺',
            'B': '600.000 ₺',
            'C': '520.000 ₺',
            'D': '510.000 ₺',
            'E': '490.000 ₺',
        },
        'E',
        'Sınıflandırma tarihine kadar amortisman ayrılır: 600.000 / 10 = 60.000 ₺ yıllık; 1 Temmuz 2024 - 1 Ocak 2026 arası 18 ay = 90.000 ₺. Defter değeri 600.000 − 90.000 = 510.000 ₺. Gerçeğe uygun değerden satış maliyeti düşülür: 520.000 − 30.000 = 490.000 ₺. TFRS 5 par. 15 uyarınca düşük olan alınır: 490.000 ₺.',
        'TFRS 5 par. 15',
    ),
    # düzey 2
    '0042': patch(
        "TFRS 5'e göre satış amaçlı elde tutulan olarak sınıflandırılan bir duran varlığın amortismanı bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Amortisman ayrılmaya kalan faydalı ömür üzerinden devam edilir',
            'B': 'Sınıflandırma tarihinden itibaren amortisman ayrılmaz',
            'C': 'Geçmiş dönem amortismanları iptal edilerek maliyete geri eklenir',
            'D': 'Amortisman ayrılır ancak doğrudan özkaynağa yansıtılır',
            'E': 'Amortisman satış gerçekleşene kadar yarı oranda ayrılır',
        },
        'B',
        'TFRS 5 par. 25: satış amaçlı elde tutulan olarak sınıflandırılan duran varlık amortismana tabi tutulmaz. Varlık artık kullanımla değil satışla geri kazanılacağından amortisman mantığı ortadan kalkar.',
        'TFRS 5 par. 25',
    ),
    # düzey 2
    '0043': patch(
        'TFRS 5 kapsamında ölçüm sonrası değer düşüklüğü zararı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Değer düşüklüğü satış gerçekleştiğinde kaydedilir; öncesindeki kayıplar yansıtılmaz',
            'B': 'Satış amaçlı varlıklarda değer düşüklüğü kaydı yapılmaz',
            'C': 'Defter değerinin satış maliyeti düşülmüş gerçeğe uygun değeri aşan kısmı zarar yazılır',
            'D': 'Değer düşüklüğü ilgili varlığın maliyetine eklenir',
            'E': 'Değer düşüklüğü doğrudan özkaynaklardan indirilir',
        },
        'C',
        'TFRS 5 par. 20: ilk sınıflandırmada ve sonraki ölçümlerde defter değeri, satış maliyeti düşülmüş gerçeğe uygun değeri aşıyorsa fark değer düşüklüğü zararı olarak kâr veya zarara yansıtılır.',
        'TFRS 5 par. 20',
    ),
    # düzey 2
    '0044': patch(
        "Bir elden çıkarılacak varlık grubunun değer düşüklüğü zararının dağıtımı bakımından TFRS 5'e göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Zarar dağıtılmaz; tek kalemde gösterilir',
            'B': 'Zarar önce en likit varlıklara dağıtılır',
            'C': 'Zarar önce şerefiyeye, kalan tutar diğer varlıklara defter değerleri oranında dağıtılır',
            'D': 'Zarar tüm varlıklara eşit tutarlarda dağıtılır; şerefiyeye öncelik tanınmaz ve defter değerleri dikkate alınmaz',
            'E': 'Zarar stoklara dağıtılır',
        },
        'C',
        'TFRS 5 par. 23: elden çıkarılacak grupta muhasebeleştirilen değer düşüklüğü zararı, önce gruba tahsis edilen şerefiyenin defter değerini azaltır; kalan tutar TMS 36 sırasına göre diğer varlıklara defter değerleri oranında dağıtılır.',
        'TFRS 5 par. 23',
    ),
    # düzey 3
    '0045': patch(
        "TFRS 15'e göre aşağıdakilerden hangisi hasılatın muhasebeleştirilmesinde izlenen beş adımdan biri DEĞİLDİR?",
        {
            'A': 'Müşterinin kredi değerliliğine göre hasılatın sınıflandırılması',
            'B': 'Müşteriyle yapılan sözleşmenin ve tahsil edilebilirlik ölçütünün belirlenmesi',
            'C': 'İşlem bedelinin belirlenmesi',
            'D': 'Sözleşmedeki edim yükümlülüklerinin belirlenmesi',
            'E': 'İşlem bedelinin edim yükümlülüklerine dağıtılması',
        },
        'A',
        'TFRS 15 par. IN7: beş adım sözleşmenin belirlenmesi, edim yükümlülüklerinin belirlenmesi, işlem bedelinin belirlenmesi, bedelin edim yükümlülüklerine dağıtılması ve edim yükümlülüğü yerine getirildiğinde hasılatın muhasebeleştirilmesidir. Kredi değerliliği ayrı bir adım değildir; sözleşmenin varlığı değerlendirilirken tahsil edilebilirlik ölçütü içinde ele alınır.',
        'TFRS 15 par. IN7',
    ),
    # düzey 2
    '0046': patch(
        "TFRS 15'e göre işlem bedelinin edim yükümlülüklerine dağıtılmasında esas alınan ölçüt aşağıdakilerden hangisidir?",
        {
            'A': 'Edimlerin maliyetlerinin nispi oranı',
            'B': 'Müşterinin ödeme takvimi',
            'C': 'Edimlerin yerine getirilme sırasına göre eşit dağıtım',
            'D': 'Bağımsız satış fiyatlarının nispi oranı',
            'E': 'Sözleşmede yazılı liste fiyatları',
        },
        'D',
        'TFRS 15 par. 74: işlem bedeli, sözleşmedeki her bir edim yükümlülüğüne bağımsız satış fiyatlarının nispi oranına göre dağıtılır. Bağımsız satış fiyatı gözlemlenemiyorsa tahmin edilir.',
        'TFRS 15 par. 74',
    ),
    # düzey 2
    '0047': patch(
        "TFRS 15'e göre müşterinin gayri nakdî bedel ödemeyi taahhüt ettiği sözleşmelerde işlem bedeli nasıl ölçülür?",
        {
            'A': 'Sözleşmede yazılı nominal tutarla',
            'B': 'Bedel ölçülemediğinden hasılat kaydedilmez',
            'C': 'Bedelin vergi değeriyle',
            'D': 'Gayri nakdî bedelin gerçeğe uygun değeriyle',
            'E': 'Devredilen malın maliyet bedeliyle',
        },
        'D',
        'TFRS 15 par. 66: müşterinin nakit dışı bedel taahhüt ettiği durumda işlem bedeli, gayri nakdî bedelin gerçeğe uygun değeri esas alınarak ölçülür. Gerçeğe uygun değer makul biçimde tahmin edilemiyorsa devredilen mal veya hizmetin bağımsız satış fiyatı kullanılır.',
        'TFRS 15 par. 66',
    ),
    # düzey 2
    '0048': patch(
        'TFRS 15 kapsamında sözleşmenin varlığından söz edilebilmesi için aşağıdakilerden hangisi aranmaz?',
        {
            'A': 'Tarafların sözleşmeyi onaylamış ve edimlerini yerine getirmeyi taahhüt etmiş olması',
            'B': 'Ödeme koşullarının belirlenebilir olması',
            'C': 'Sözleşmenin resmî şekilde ve yazılı olarak düzenlenmiş olması',
            'D': 'Bedelin tahsil edilmesinin muhtemel olması',
            'E': 'Devredilecek mal veya hizmetlere ilişkin hakların belirlenebilir olması',
        },
        'C',
        'TFRS 15 par. 9-10: sözleşme yazılı, sözlü ya da işletmenin olağan ticari teamülleri doğrultusunda zımni olabilir. Aranan beş ölçüt onay ve taahhüt, hakların belirlenebilirliği, ödeme koşulları, ticari özün bulunması ve tahsilin muhtemel olmasıdır.',
        'TFRS 15 par. 9-10',
    ),
    # düzey 3
    '0049': patch(
        "Bir yazılım işletmesi müşterisine lisans, kurulum ve bir yıllık destek hizmetini tek sözleşmede 100.000 ₺'ye satmıştır. Bağımsız satış fiyatları sırasıyla 60.000, 20.000 ve 45.000 ₺'dir. TFRS 15'e göre lisansa dağıtılacak bedel kaç ₺'dir?",
        {
            'A': '60.000 ₺',
            'B': '48.000 ₺',
            'C': '33.333 ₺',
            'D': '52.000 ₺',
            'E': '40.000 ₺',
        },
        'B',
        'Bağımsız satış fiyatları toplamı 60.000 + 20.000 + 45.000 = 125.000 ₺. Lisansın payı 60.000 / 125.000 = %48. İşlem bedelinden dağıtılan tutar 100.000 × %48 = 48.000 ₺. TFRS 15 par. 76 nispi bağımsız satış fiyatı yöntemini öngörür.',
        'TFRS 15 par. 74-76',
    ),
    # düzey 2
    '0050': patch(
        "TMS 41'e göre canlı varlıkların gerçeğe uygun değerindeki değişimden doğan kazanç veya kayıp nereye yansıtılır?",
        {
            'A': 'Doğrudan geçmiş yıl kârlarına',
            'B': 'İlgili varlığın maliyetine',
            'C': 'Satış gerçekleşene kadar ertelenir',
            'D': 'Oluştuğu dönemin kâr veya zararına',
            'E': 'Diğer kapsamlı gelire',
        },
        'D',
        'TMS 41 par. 26: canlı varlığın ilk muhasebeleştirilmesinden ve gerçeğe uygun değerinden satış maliyetleri düşülerek bulunan tutardaki değişimlerden doğan kazanç veya kayıplar, oluştukları dönemin kâr veya zararına dâhil edilir.',
        'TMS 41 par. 26',
    ),
    # düzey 2
    '0051': patch(
        "TMS 41'e göre gerçeğe uygun değerin güvenilir biçimde ölçülemediği durumda aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Canlı varlık maliyetinden birikmiş amortisman ve değer düşüklüğü düşülerek ölçülür',
            'B': 'Canlı varlık nominal bir değerle izlenir',
            'C': 'Bağımsız değerleme raporu alınır; rapor alınamıyorsa varlık kayda alınmaz',
            'D': 'Canlı varlık finansal tablolara alınmaz',
            'E': 'Varlık net gerçekleşebilir değerle ölçülür',
        },
        'A',
        'TMS 41 par. 30: gerçeğe uygun değerin güvenilir biçimde ölçülemediğine ilişkin açık kanıt bulunması hâlinde ilk muhasebeleştirmede canlı varlık, maliyetinden birikmiş amortisman ve birikmiş değer düşüklüğü zararları düşülerek ölçülür. Değer güvenilir ölçülebilir hâle geldiğinde gerçeğe uygun değer esasına dönülür.',
        'TMS 41 par. 30',
    ),
    # düzey 2
    '0052': patch(
        "TMS 41'e göre canlı varlıkların gerçeğe uygun değerinin belirlenmesinde aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Değerleme hasat tarihindeki fiyatla yapılır',
            'B': 'En yakın büyük şehirdeki fiyat esas alınır',
            'C': 'Bir önceki yılın ortalama fiyatı esas alınır',
            'D': 'Gelecekte oluşacağı tahmin edilen fiyat esas alınır',
            'E': 'Varlığın bulunduğu yer ve mevcut durumu esas alınır',
        },
        'E',
        'TMS 41 par. 9 ve 15: canlı varlığın gerçeğe uygun değeri, bulunduğu yer ve mevcut durumu dikkate alınarak belirlenir. Varlığı pazara ulaştırma maliyetleri gerçeğe uygun değerin belirlenmesinde göz önünde bulundurulur.',
        'TMS 41 par. 9, 15',
    ),
    # düzey 2
    '0053': patch(
        "TFRS 3'e göre işletme birleşmesinde edinilen tanımlanabilir varlık ve üstlenilen borçlar hangi değerle ölçülür?",
        {
            'A': 'Edinim tarihindeki gerçeğe uygun değerleriyle',
            'B': 'Edinilen işletmenin kayıtlı defter değerleriyle',
            'C': 'Birleşme sözleşmesinde yazılı nominal değerlerle',
            'D': 'Vergi mevzuatındaki değerleme ölçüleriyle',
            'E': 'Edinen işletmenin maliyet bedelleriyle',
        },
        'A',
        'TFRS 3 par. 18: edinen işletme, edinilen tanımlanabilir varlıkları ve üstlenilen borçları edinim tarihindeki gerçeğe uygun değerleriyle ölçer. Edinilenin defter değerleri esas alınmaz.',
        'TFRS 3 par. 18',
    ),
    # düzey 2
    '0054': patch(
        "TFRS 3'e göre işletme birleşmesiyle ilgili işlem maliyetleri (danışmanlık, aracılık, hukuk giderleri) bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Gelecek dönemlere yayılarak itfa edilir',
            'B': 'Transfer edilen bedele eklenerek şerefiyeyi artırır',
            'C': 'Edinilen varlıkların maliyetine dağıtılır',
            'D': 'Oluştukları dönemde gider olarak muhasebeleştirilir',
            'E': 'Doğrudan özkaynaklardan indirilir',
        },
        'D',
        'TFRS 3 par. 53: edinimle ilgili maliyetler, hizmetlerin alındığı dönemde gider olarak muhasebeleştirilir. Borçlanma araçlarının ve özkaynağa dayalı araçların ihraç maliyetleri ise TMS 32 ve TFRS 9 uyarınca ele alınır.',
        'TFRS 3 par. 53',
    ),
    # düzey 2
    '0055': patch(
        "TFRS 3'e göre ölçüm dönemi bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Bir yılı aşamaz; geçici tutarlar geriye dönük düzeltilebilir',
            'B': 'Ölçüm dönemi üç ayla sınırlıdır',
            'C': 'Ölçüm dönemi süresizdir; bir yıllık üst sınır öngörülmemiştir',
            'D': 'Düzeltmeler ileriye dönük uygulanır',
            'E': 'Geçici tutarlar sonradan düzeltilemez',
        },
        'A',
        'TFRS 3 par. 45-46: muhasebeleştirme edinim tarihinde tamamlanamamışsa geçici tutarlar raporlanır ve ölçüm döneminde düzeltilir. Ölçüm dönemi, edinen işletmenin gerekli bilgiyi elde ettiği ana kadar sürer ve edinim tarihinden itibaren bir yılı aşamaz.',
        'TFRS 3 par. 45-46',
    ),
    # düzey 2
    '0056': patch(
        "TFRS 13'ün gerçeğe uygun değer hiyerarşisinde 1. seviye girdiler aşağıdakilerden hangisidir?",
        {
            'A': 'Bağımsız değerleme raporundaki tutarlar',
            'B': 'Aktif piyasalarda özdeş varlık veya borçlar için kote edilmiş düzeltilmemiş fiyatlar',
            'C': 'Benzer varlıklar için gözlemlenebilir fiyatlar',
            'D': 'Varlığın kayıtlı maliyet bedeli',
            'E': 'İşletmenin kendi tahminlerine dayanan gözlemlenemeyen girdiler; bu girdiler en güvenilir kanıt sayılır',
        },
        'B',
        'TFRS 13 par. 76: 1. seviye girdiler, işletmenin ölçüm tarihinde ulaşabildiği aktif piyasalardaki özdeş varlık veya borçlara ilişkin düzeltilmemiş kote fiyatlardır ve en güvenilir kanıtı oluşturur.',
        'TFRS 13 par. 76',
    ),
    # düzey 2
    '0057': patch(
        "TFRS 13'e göre gerçeğe uygun değer ölçümünde işlem maliyetleriyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Ölçüm, varlığın özellikleri dikkate alınarak yapılır',
            'B': 'İşlem maliyetleri gerçeğe uygun değere eklenir',
            'C': 'İşlem maliyetleri varlığa değil işleme özgüdür',
            'D': 'İşlem maliyetleri ilgili diğer standartlara göre muhasebeleştirilir',
            'E': 'Konum varlığın bir özelliğiyse taşıma maliyeti dikkate alınır',
        },
        'B',
        'TFRS 13.25-26: gerçeğe uygun değer ölçümünde kullanılan fiyat işlem maliyetlerine göre düzeltilmez; işlem maliyetleri varlığın değil işlemin özelliğidir ve diğer standartlara göre muhasebeleştirilir. Taşıma maliyetleri ise konum varlığın bir özelliğiyse dikkate alınır.',
        'TFRS 13 par. 25',
    ),
    # düzey 3
    '0058': patch(
        "Bir varlığın gerçeğe uygun değeri ölçülürken kullanılan girdilerin bir bölümü gözlemlenebilir, önemli bir bölümü ise gözlemlenemeyen girdilerden oluşmaktadır. TFRS 13'e göre ölçüm hangi seviyede sınıflandırılır?",
        {
            'A': 'Sınıflandırma yapılmaz',
            'B': '2. seviye',
            'C': 'Girdilerin ağırlıklı ortalamasına göre belirlenen ara seviye',
            'D': '3. seviye',
            'E': '1. seviye',
        },
        'D',
        'TFRS 13 par. 73: gerçeğe uygun değer ölçümü, ölçüm için önemli olan en düşük seviyedeki girdiye göre sınıflandırılır. Gözlemlenemeyen girdiler ölçüm açısından önemliyse ölçüm bütünüyle 3. seviyede sınıflandırılır.',
        'TFRS 13 par. 73',
    ),
    # düzey 2
    '0059': patch(
        "TMS 34'e göre ara dönemde önemlilik değerlendirmesi bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Önemlilik sınırı kanunla maktu olarak belirlenmiştir',
            'B': 'Ara dönemde önemlilik değerlendirmesi yapılmaz',
            'C': 'Önemlilik yıllık tahmini sonuçlara göre değerlendirilir',
            'D': 'Önemlilik bağımsız denetçi tarafından belirlenir',
            'E': 'Ara dönem verileri esas alınarak değerlendirilir',
        },
        'E',
        'TMS 34 par. 23 ve 25: muhasebeleştirme, ölçüm, sınıflandırma ve açıklama kararlarında önemlilik ara dönem finansal verileri esas alınarak değerlendirilir. Yıllık verilere göre değerlendirme yanıltıcı olur; ara dönem tahminleri yıllığa göre daha çok tahmine dayanır.',
        'TMS 34 par. 23, 25',
    ),
    # düzey 3
    '0060': patch(
        'Bir işletme ara dönemde şerefiye için değer düşüklüğü zararı muhasebeleştirmiştir. Sonraki ara dönemde koşullar iyileşmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Zarar yıl sonunda iptal edilir',
            'B': 'Zarar sonraki ara dönemde iptal edilir',
            'C': 'Şerefiyeye ilişkin değer düşüklüğü zararı sonraki dönemde iptal edilemez',
            'D': 'Zarar iptal edilerek özkaynağa aktarılır',
            'E': 'Zarar iptal edilir ve geçmişe dönük düzeltme yapılır; şerefiyede iptal yasağı uygulanmaz',
        },
        'C',
        'TFRS Yorum 10 ve TMS 36 par. 124: şerefiye için muhasebeleştirilen değer düşüklüğü zararı sonraki dönemlerde iptal edilemez. Ara dönemde kaydedilen zarar, koşullar sonradan iyileşse bile geri çevrilmez.',
        'TFRS Yorum 10 · TMS 36 par. 124',
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
    print(f"1 paket / {len(PATCHES)} soru ('Diger Guncel Standartlar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
