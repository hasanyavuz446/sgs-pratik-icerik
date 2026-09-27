#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TMS 1 Finansal Tablolarin Sunulusu — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gercek sinav profiliyle yeniden yazim (89 gercek standart sorusu: medyan kok ~310, medyan sik ~22, olumsuz %11, sayisal %18). Eski surumde siklar 75-80 karakterlik aciklamalardi ve ~100 mutlak ifadeli celdirici tasiyordu (kor %50). Kapsam: tam set, genel ozellikler (sureklilik, tahakkuk, onemlilik, netlestirme, raporlama sikligi, karsilastirmali bilgi, tutarlilik, uyum beyani), donen/duran ve kisa/uzun vade siniflamasi (sozlesme kosullari, yeniden finansman, ertelenmis vergi), kar veya zarar ve DKG (fonksiyon/nitelik, yeniden siniflandirma, KGOP), dipnotlar. 16 hesap sorusu modulde hesaplandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: TMS 1 Finansal Tablolarin Sunulusu (KGK, 2023 degisiklikleri dahil); TMS 10, TMS 16, TMS 21, TMS 34, TFRS 5, TFRS 15 ilgili paragraflar
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/tms_1_sunulus.json"
STYLE_REF = 'SGS Muhasebe Standartlari (gercek sinav profiline kalibre: senaryo kok + kisa sik)'
ONEK = "std-tms1-gen-"


def patch(stem, options, answer, solution, ref='TMS 1 Finansal Tablolarin Sunulusu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 1
    '0001': patch(
        "Borsada işlem gören bir işletme, TFRS'ye uygun hazırladığı yıllık finansal raporunun içine finansal tablolar dışında yönetimin hazırladığı bazı raporları da koymuştur. TMS 1'e göre aşağıdakilerden hangisi tam bir finansal tablo setinin parçası değildir?",
        {
            'A': 'Nakit akış tablosu',
            'B': 'Özkaynak değişim tablosu',
            'C': 'Yönetim faaliyet raporu',
            'D': 'Finansal durum tablosu',
            'E': 'Dipnotlar',
        },
        'C',
        "TMS 1 p. 10'a göre tam set; finansal durum tablosu, kâr veya zarar ve diğer kapsamlı gelir tablosu, özkaynak değişim tablosu, nakit akış tablosu, dipnotlar ve karşılaştırmalı bilgiden oluşur. p. 14'e göre **yönetimin finansal raporlarla birlikte sunduğu faaliyet raporu, çevre raporu gibi raporlar TFRS kapsamı dışındadır**.",
        'TMS 1 p. 10, 14',
    ),
    # düzey 3
    '0002': patch(
        "Bir işletmenin dönem başı özkaynağı 2.000.000 ₺'dir. Dönem içinde 350.000 ₺ net kâr elde edilmiş, diğer kapsamlı gelir olarak 60.000 ₺ yeniden değerleme artışı doğmuş, 400.000 ₺ nakit sermaye artırımı yapılmış, ortaklara 150.000 ₺ kâr payı dağıtılmış ve işletme kendi paylarından 80.000 ₺ tutarında geri almıştır. Dönem sonu özkaynak toplamı kaç ₺'dir?",
        {
            'A': '2.660.000',
            'B': '2.580.000',
            'C': '2.520.000',
            'D': '2.180.000',
            'E': '2.810.000',
        },
        'B',
        'Özkaynak değişim tablosunda: 2.000.000 + 350.000 (kâr) + 60.000 (DKG) + 400.000 (sermaye artırımı) − 150.000 (kâr payı) − 80.000 (geri alınan paylar, özkaynaktan indirilir) = **2.580.000 ₺**.',
        'TMS 1 p. 106',
    ),
    # düzey 2
    '0003': patch(
        'Bir işletmenin yönetimi 31.12.2025 tarihli finansal tablolar yayımlanmadan önce, 2026 yılının ilk yarısında işletmeyi tasfiye etmeye ve faaliyetlerine son vermeye karar vermiştir; başka gerçekçi bir seçenek yoktur. Bu durumda finansal tabloların hazırlanmasında hangi varsayım kullanılamaz?',
        {
            'A': 'Tahakkuk esası',
            'B': 'Sunumda tutarlılık',
            'C': 'Karşılaştırmalı bilgi',
            'D': 'İşletmenin sürekliliği',
            'E': 'Önemlilik',
        },
        'D',
        "TMS 1 p. 25'e göre yönetim işletmeyi tasfiye etme veya faaliyetlerine son verme niyetindeyse ya da bunu yapmaktan başka gerçekçi seçeneği yoksa finansal tablolar **işletmenin sürekliliği esasına göre hazırlanmaz**; kullanılan esas ve nedeni açıklanır. TMS 10 p. 14 raporlama döneminden sonra alınan bu kararı da kapsar.",
        'TMS 1 p. 25-26; TMS 10 p. 14',
    ),
    # düzey 2
    '0004': patch(
        'Bir işletmenin K müşterisinden 240.000 ₺ ticari alacağı, aynı müşteriye 90.000 ₺ ticari borcu vardır. Taraflar arasında karşılıklı tutarları netleştirme hakkı veren bir anlaşma yoktur ve işletme de net tahsil etmeyi planlamamaktadır. İşletme finansal durum tablosunda ticari alacaklar içinde bu müşteri için kaç ₺ sunmalıdır?',
        {
            'A': '90.000',
            'B': '240.000',
            'C': '330.000',
            'D': '0',
            'E': '150.000',
        },
        'B',
        "TMS 1 p. 32'ye göre bir TFRS gerektirmedikçe veya izin vermedikçe **varlıklar ile borçlar netleştirilmez**. Alacak 240.000 ₺ olarak varlıklarda, borç 90.000 ₺ olarak borçlarda brüt sunulur.",
        'TMS 1 p. 32',
    ),
    # düzey 3
    '0005': patch(
        'Bir işletme önceki yılın dipnotlarında, sonucu belirsiz olan bir tazminat davasını açıklamıştır. Dava cari yılın sonunda da sonuçlanmamıştır. Cari yıl finansal tablolarında bu dava hakkında aşağıdakilerden hangisi yapılır?',
        {
            'A': 'Önceki dönem tabloları yeniden düzenlenir',
            'B': 'Dava faaliyet raporunda anlatılır',
            'C': 'Karşılık ayrılması zorunludur',
            'D': 'Dava yeniden açıklanmaz',
            'E': 'Önceki dönem anlatımı da verilir',
        },
        'E',
        "TMS 1 p. 38 ve 38B'ye göre karşılaştırmalı bilgi **anlatım niteliğindeki bilgileri de** kapsar; önceki dönemde açıklanan ve belirsizliği süren bir davanın ayrıntıları, cari dönemde de önceki dönemde bilinen durum ve sonradan atılan adımlarla birlikte açıklanır.",
        'TMS 1 p. 38, 38B',
    ),
    # düzey 2
    '0006': patch(
        "TMS 1'e göre finansal tabloların işletmenin finansal durumunu, finansal performansını ve nakit akışlarını gerçeğe uygun olarak sunması, Kavramsal Çerçeve'deki tanım ve muhasebeleştirme ölçütlerine uygun biçimde işlemlerin sadakatle gösterilmesini gerektirir. Aşağıdakilerden hangisi, TFRS'lerin uygulanmasıyla birlikte gerçeğe uygun sunumun sağlanması için gerekli görülen unsurlardan biridir?",
        {
            'A': 'Tahminlerden kaçınılması',
            'B': 'Vergi mevzuatına uyulması',
            'C': 'Varlıkların düşük gösterilmesi',
            'D': 'Gelirlerin ertelenmesi',
            'E': 'Ek açıklamalar sunulması',
        },
        'E',
        "TMS 1 p. 17'ye göre gerçeğe uygun sunum; muhasebe politikalarının TMS 8'e göre seçilip uygulanmasını, bilginin ilgili, güvenilir, karşılaştırılabilir ve anlaşılabilir sunulmasını ve TFRS'lerin gerektirdiklerinin yetersiz kaldığı durumlarda **ek açıklamalar** yapılmasını gerektirir.",
        'TMS 1 p. 15-17',
    ),
    # düzey 3
    '0007': patch(
        "Bir işletmenin raporlama dönemi sonundaki ertelenmiş vergi varlığı 180.000 ₺'dir. Bu tutarın 70.000 ₺'lik kısmının raporlama döneminden sonraki 12 ay içinde geri çevrilmesi beklenmektedir. İşletme finansal durum tablosunda dönen varlıklar arasında ertelenmiş vergi varlığı olarak kaç ₺ sunmalıdır?",
        {
            'A': '35.000',
            'B': '110.000',
            'C': '0',
            'D': '180.000',
            'E': '70.000',
        },
        'C',
        "TMS 1 p. 56'ya göre işletme, finansal durum tablosunda dönen ve duran ayrımı yaptığında **ertelenmiş vergi varlıklarını (borçlarını) dönen varlık (kısa vadeli borç) olarak sınıflandırmaz**; tamamı duran varlıktır.",
        'TMS 1 p. 56',
    ),
    # düzey 3
    '0008': patch(
        'Bir işletmenin kredisi 2026 Nisan ayında ödenecektir. Raporlama dönemi sonunda işletmenin bu krediyi yenileme hakkı yoktur. İşletme, raporlama döneminden sonra ve finansal tablolar yayımlanmadan önce, krediyi 2030 yılına kadar uzatan yeni bir anlaşma imzalamıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Yeni anlaşma düzeltme gerektirmeyen bir olaydır',
            'B': 'Yeni anlaşma dipnotlarda açıklanabilir',
            'C': 'Kredi kısa vadeli sınıflandırılır',
            'D': 'Kredi uzun vadeli sınıflandırılır',
            'E': 'Sınıflama raporlama dönemi sonundaki haklara göre yapılır',
        },
        'D',
        "TMS 1 p. 72'ye göre 12 ay içinde ödenecek borç, raporlama döneminden sonra ve tablolar onaylanmadan önce uzun vadeli yeniden finansman anlaşması yapılsa bile **kısa vadeli** sınıflandırılır; p. 76'ya göre bu anlaşma düzeltme gerektirmeyen olay olarak açıklanır.",
        'TMS 1 p. 72, 76',
    ),
    # düzey 2
    '0009': patch(
        "Bir bankanın faaliyetleri belirgin bir faaliyet döngüsü içinde gerçekleşmemektedir ve varlık ile borçlarını dönen/duran ayrımı yerine likiditelerine göre sıralamak daha güvenilir ve ilgili bilgi sağlamaktadır. TMS 1'e göre banka finansal durum tablosunu hangi esasa göre sunabilir?",
        {
            'A': 'Önem derecesi sırası',
            'B': 'Likidite sırası',
            'C': 'Alfabetik sıra',
            'D': 'Vade eşleşmesi',
            'E': 'Tarihî maliyet sırası',
        },
        'B',
        "TMS 1 p. 60 ve 63'e göre likiditeye dayalı sunum güvenilir ve daha ilgili bilgi sağlıyorsa, örneğin finansal kuruluşlarda, varlık ve borçlar dönen/duran ayrımı yerine **likidite sırasına** göre sunulur.",
        'TMS 1 p. 60, 63',
    ),
    # düzey 3
    '0010': patch(
        'Bir işletmenin bankadaki 400.000 ₺ tutarındaki mevduatı, yurt dışında bir fabrika inşası için verilen teminat nedeniyle raporlama döneminden sonraki 18 ay boyunca kullanılamayacaktır. Bu mevduat finansal durum tablosunda nasıl sınıflandırılır?',
        {
            'A': 'Dönen varlık',
            'B': 'Nakit ve nakit benzeri',
            'C': 'Kısa vadeli borç',
            'D': 'Duran varlık',
            'E': 'Özkaynak kalemi',
        },
        'D',
        "TMS 1 p. 66(d)'ye göre nakit ancak **raporlama döneminden sonra en az 12 ay süreyle bir borcun ödenmesinde veya takasında kullanımı kısıtlanmamışsa** dönen varlıktır; 18 ay kısıtlı mevduat duran varlık olarak sınıflandırılır.",
        'TMS 1 p. 66',
    ),
    # düzey 3
    '0011': patch(
        "Giderlerini fonksiyon esasına göre sunan bir işletmenin dönem verileri şöyledir: hasılat 3.000.000 ₺, satışların maliyeti 1.800.000 ₺, pazarlama giderleri 250.000 ₺, genel yönetim giderleri 320.000 ₺, araştırma ve geliştirme giderleri 90.000 ₺, finansman giderleri 140.000 ₺. Finansman giderinden önceki esas faaliyet kârı kaç ₺'dir?",
        {
            'A': '1.200.000',
            'B': '400.000',
            'C': '540.000',
            'D': '950.000',
            'E': '630.000',
        },
        'C',
        'Fonksiyon esasında: brüt kâr 3.000.000 − 1.800.000 = 1.200.000 ₺; faaliyet giderleri 250.000 + 320.000 + 90.000 düşülünce esas faaliyet kârı **540.000 ₺**. Finansman gideri sonraki aşamada düşülür.',
        'TMS 1 p. 99, 103',
    ),
    # düzey 2
    '0012': patch(
        "Giderlerini fonksiyon esasına göre (satışların maliyeti, pazarlama, genel yönetim) sunan bir işletme, TMS 1'e göre giderlerin niteliğine ilişkin ek bilgi de açıklamak zorundadır. Aşağıdakilerden hangisi bu kapsamda açıklanması özellikle istenen bilgilerdendir?",
        {
            'A': 'Amortisman giderleri',
            'B': 'Satış hedefleri',
            'C': 'Kurumlar vergisi matrahı',
            'D': 'Bütçe sapmaları',
            'E': 'Pay başına temettü tahmini',
        },
        'A',
        "TMS 1 p. 104'e göre giderlerini fonksiyon esasına göre sınıflandıran işletmeler, **amortisman ve itfa giderleri ile çalışanlara sağlanan fayda giderleri** dâhil, giderlerin niteliğine ilişkin ek bilgi açıklar.",
        'TMS 1 p. 104',
    ),
    # düzey 3
    '0013': patch(
        "Bir işletmenin cari dönem diğer kapsamlı gelir kalemleri şöyledir: maddi duran varlık yeniden değerleme artışı 200.000 ₺, tanımlanmış fayda planlarının yeniden ölçüm kaybı 50.000 ₺, gerçeğe uygun değer değişimi diğer kapsamlı gelire yansıtılan özkaynak araçlarından kazanç 30.000 ₺, yurt dışı işletmenin çevrim farkı kazancı 80.000 ₺, nakit akış riskinden korunmanın etkin kısmından kazanç 40.000 ₺. Sonradan kâr veya zarara yeniden sınıflandırılmayacak kalemlerin net toplamı kaç ₺'dir?",
        {
            'A': '300.000',
            'B': '280.000',
            'C': '230.000',
            'D': '180.000',
            'E': '120.000',
        },
        'D',
        "TMS 1 p. 82A'ya göre DKG kalemleri yeniden sınıflandırılacak ve sınıflandırılmayacak olarak gruplanır. Yeniden değerleme artışı, tanımlanmış fayda planı yeniden ölçümleri ve DKG'ye yansıtılan özkaynak araçları **yeniden sınıflandırılmaz**: 200.000 − 50.000 + 30.000 = **180.000 ₺**. Çevrim farkı ve nakit akış riskinden korunma kazancı yeniden sınıflandırılabilir gruptadır.",
        'TMS 1 p. 82A, 96',
    ),
    # düzey 2
    '0014': patch(
        "Bir işletme kâr veya zarar ile diğer kapsamlı gelir bilgilerini iki ayrı tabloda sunmak istemektedir. TMS 1'e göre bu durumda diğer kapsamlı gelir tablosu hangi tutarla başlar?",
        {
            'A': 'Brüt kâr',
            'B': 'Esas faaliyet kârı',
            'C': 'Vergi öncesi kâr',
            'D': 'Dönem kâr veya zararı',
            'E': 'Hasılat',
        },
        'D',
        "TMS 1 p. 10A'ya göre işletme tek bir tablo veya iki tablo sunabilir; iki tablo sunulursa ayrı kâr veya zarar tablosu kapsamlı gelir tablosundan hemen önce gelir ve **kapsamlı gelir tablosu kâr veya zararla başlar**.",
        'TMS 1 p. 10A, 81A',
    ),
    # düzey 2
    '0015': patch(
        "Bir işletme, gerçeğe uygun değeriyle ölçtüğü yatırım amaçlı gayrimenkullerinin değerlemesinde kullanılan varsayımların, gelecek yıl varlıkların defter değerinde önemli bir düzeltmeye yol açma riskinin yüksek olduğunu belirlemiştir. TMS 1'e göre bu bilgi hangi başlık altında açıklanır?",
        {
            'A': 'Muhasebe politikası değişiklikleri',
            'B': 'Tahmin belirsizliğinin kaynakları',
            'C': 'Koşullu varlıklar',
            'D': 'Sermayenin yönetimi',
            'E': 'Hata düzeltmeleri',
        },
        'B',
        "TMS 1 p. 125'e göre işletme, **gelecek finansal yıl içinde varlık ve borçların defter değerlerinde önemli düzeltme riski taşıyan** geleceğe ilişkin varsayımları ve **tahmin belirsizliğinin diğer temel kaynaklarını** açıklar.",
        'TMS 1 p. 125',
    ),
    # düzey 3
    '0016': patch(
        "Bir işletmenin yönetimi, bir kuruluş üzerinde oy haklarının %40'ına sahip olmasına rağmen diğer oy haklarının dağınık olması nedeniyle kontrol gücü bulunduğuna karar vermiş ve kuruluşu bağlı ortaklık olarak konsolide etmiştir. Bu karar tahmin içermeyen, muhasebe politikasının uygulanmasına ilişkin bir değerlendirmedir. TMS 1'e göre bu karar dipnotlarda hangi başlıkta açıklanır?",
        {
            'A': 'Hata düzeltmeleri',
            'B': 'Tahmin belirsizliğinin kaynakları',
            'C': 'Yönetimin yaptığı muhakemeler',
            'D': 'Sonraki olaylar',
            'E': 'Koşullu borçlar',
        },
        'C',
        "TMS 1 p. 122'ye göre işletme, muhasebe politikalarını uygularken **tahminler dışında** yönetimin yaptığı ve tutarlar üzerinde en önemli etkiye sahip **muhakemeleri** açıklar; bir kuruluşun kontrol edilip edilmediğine ilişkin karar bunun örneğidir.",
        'TMS 1 p. 122',
    ),
    # düzey 2
    '0017': patch(
        'Bir işletme dipnotlarını, finansal tablolarda sunulan kalemlerle çapraz referans vermeden ve rastgele sırayla düzenlemiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Tablodaki kalemler ilgili dipnota çapraz referans verir',
            'B': 'Sıralamada anlaşılabilirlik dikkate alınır',
            'C': 'Dipnotlar sistematik biçimde sunulur',
            'D': 'Dipnotların sırası serbesttir, referans gerekmez',
            'E': "TFRS'ye uygunluk beyanı dipnotlarda yer alır",
        },
        'D',
        "TMS 1 p. 113'e göre işletme dipnotları, uygulanabildiği ölçüde **sistematik biçimde** sunar ve finansal tablolardaki her kalem için ilgili dipnota **çapraz referans** verir; p. 114'e göre sıralamada anlaşılabilirlik ve karşılaştırılabilirlik dikkate alınır.",
        'TMS 1 p. 113-114',
    ),
    # düzey 3
    '0018': patch(
        "Bir işletmenin dönem içindeki brüt satışları 2.400.000 ₺, müşterilere verilen satış iskontoları 150.000 ₺ ve ciro primleri 50.000 ₺'dir. TMS 1 ve TFRS 15'e göre kâr veya zarar tablosunda hasılat olarak kaç ₺ sunulur?",
        {
            'A': '2.400.000',
            'B': '2.350.000',
            'C': '2.250.000',
            'D': '2.600.000',
            'E': '2.200.000',
        },
        'E',
        'TMS 1 p. 34(a) ve TFRS 15 uyarınca hasılat, işletmenin verdiği **ticari iskonto ve miktar indirimleri düşülmüş tutarla** ölçülür; bu netleştirme yasağının ihlali değildir: 2.400.000 − 150.000 − 50.000 = **2.200.000 ₺**.',
        'TMS 1 p. 34; TFRS 15 p. 47',
    ),
    # düzey 3
    '0019': patch(
        'Finansal durum tablosunda sınıflandırmaya ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Ertelenmiş vergi borcu kısa vadeli borç olarak sınıflandırılmaz\n\nII. Raporlama döneminden sonra yapılan yeniden finansman anlaşması borcu uzun vadeli yapar\n\nIII. Normal faaliyet döngüsündeki ticari borçlar 12 aydan geç ödense de kısa vadelidir',
        {
            'A': 'II ve III',
            'B': 'Yalnız III',
            'C': 'I, II ve III',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'E',
        "TMS 1 p. 56'ya göre ertelenmiş vergi kısa vadeli sınıflandırılmaz (I); p. 70'e göre işletme sermayesinin parçası olan ticari borçlar kısa vadelidir (III). p. 72'ye göre raporlama döneminden sonraki yeniden finansman **sınıflamayı değiştirmez** (II yanlış).",
        'TMS 1 p. 56, 69-73',
    ),
    # düzey 3
    '0020': patch(
        "Aşağıdakilerden hangileri TMS 1'e göre dipnotlarda açıklanır?\n\nI. Önemli muhasebe politikası bilgisi\n\nII. Tahmin belirsizliğinin temel kaynakları\n\nIII. Fonksiyon esasını seçen işletmede amortisman gideri tutarı",
        {
            'A': 'I ve III',
            'B': 'II ve III',
            'C': 'Yalnız I',
            'D': 'I, II ve III',
            'E': 'I ve II',
        },
        'D',
        "TMS 1 p. 117'ye göre önemli muhasebe politikası bilgisi (I), p. 125'e göre tahmin belirsizliğinin temel kaynakları (II) ve p. 104'e göre fonksiyon esasını seçen işletmede giderlerin niteliğine ilişkin ek bilgi, özellikle amortisman (III) açıklanır.",
        'TMS 1 p. 104, 117, 125',
    ),
    # düzey 2
    '0021': patch(
        'Bir işletme 2025 yılında bir finansal tablo kalemini yeniden sınıflandırmış ve karşılaştırmalı tutarları da buna göre düzenlemiştir. Yeniden sınıflandırmanın 1 Ocak 2024 tarihli finansal durum tablosundaki bilgiler üzerinde önemli bir etkisi yoktur. İşletme 2025 finansal tablolarında kaç adet finansal durum tablosu sunmalıdır?',
        {
            'A': '4',
            'B': '2',
            'C': '6',
            'D': '1',
            'E': '3',
        },
        'B',
        "TMS 1 p. 40A'ya göre önceki dönemin başına ait üçüncü bir finansal durum tablosu ancak geriye dönük uygulama, düzeltme veya yeniden sınıflandırma **önceki dönem başındaki bilgiler üzerinde önemli bir etkiye sahipse** sunulur. Etki önemli olmadığından cari dönem sonu ve önceki dönem sonu olmak üzere **2** tablo yeterlidir.",
        'TMS 1 p. 10(f), 40A',
    ),
    # düzey 3
    '0022': patch(
        "Bir işletmenin cari dönem verileri şöyledir: dönem net kârı 850.000 ₺, maddi duran varlık yeniden değerleme artışı 120.000 ₺, yurt dışı işletmenin çevriminden doğan kur farkı kaybı 40.000 ₺, nakit sermaye artırımı 300.000 ₺ ve ortaklara dağıtılan kâr payı 100.000 ₺. İşletmenin toplam kapsamlı geliri kaç ₺'dir?",
        {
            'A': '930.000',
            'B': '1.230.000',
            'C': '1.010.000',
            'D': '830.000',
            'E': '850.000',
        },
        'A',
        'Toplam kapsamlı gelir = kâr veya zarar + diğer kapsamlı gelir: 850.000 + 120.000 − 40.000 = **930.000 ₺**. Sermaye artırımı ve kâr payı ortaklarla işlemdir; toplam kapsamlı gelire girmez.',
        'TMS 1 p. 7, 81A',
    ),
    # düzey 2
    '0023': patch(
        "Raporlama dönemi 31 Aralık 2025'te sona eren bir işletmenin yönetimi, işletmenin sürekliliği varsayımının uygunluğunu değerlendirirken TMS 1'e göre en az hangi tarihe kadar olan dönemi dikkate almalıdır?",
        {
            'A': 'Finansal tabloların onay tarihi',
            'B': '31 Aralık 2027',
            'C': '31 Aralık 2026',
            'D': '30 Haziran 2026',
            'E': '31 Mart 2026',
        },
        'C',
        "TMS 1 p. 26'ya göre yönetim, işletmenin sürekliliği varsayımını değerlendirirken **raporlama döneminin sonundan itibaren en az on iki aylık** geleceğe ilişkin bütün bilgileri dikkate alır; ancak bu süreyle sınırlı değildir.",
        'TMS 1 p. 26',
    ),
    # düzey 3
    '0024': patch(
        "Bir işletme defter değeri 380.000 ₺ olan bir makinesini 500.000 ₺'ye satmış, satış için 20.000 ₺ komisyon ödemiştir. Makine yatırım amaçlı değildir ve işletmenin olağan faaliyeti makine satmak değildir. Bu satıştan doğan ve kâr veya zarar tablosunda sunulacak tutar kaç ₺'dir?",
        {
            'A': '100.000',
            'B': '380.000',
            'C': '120.000',
            'D': '480.000',
            'E': '500.000',
        },
        'A',
        "TMS 1 p. 34'e göre duran varlıkların elden çıkarılmasından doğan kazanç ve kayıplar, **satış bedelinden varlığın defter değeri ve ilgili satış giderleri düşülerek net** sunulur; bu, netleştirme yasağının ihlali sayılmaz: 500.000 − 380.000 − 20.000 = **100.000 ₺**.",
        'TMS 1 p. 34',
    ),
    # düzey 2
    '0025': patch(
        "Bir perakende işletmesi, faaliyet dönemini her yıl ocak ayının son cumartesi günü biten 52 haftalık dönem olarak belirlemiştir. Bu yıl bir birleşme nedeniyle raporlama dönemi 9 ay olmuştur. TMS 1'e göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Finansal tablolar en az yılda bir kez sunulur',
            'B': "52 haftalık dönem TMS 1'e aykırıdır",
            'C': 'Raporlama dönemi değiştiği için nedeni açıklanır',
            'D': 'Dönem uzunluğu değişse de karşılaştırmalı bilgi verilir',
            'E': 'Tutarların tam karşılaştırılabilir olmadığı açıklanır',
        },
        'B',
        "TMS 1 p. 36'ya göre finansal tablolar en az yılda bir sunulur; raporlama dönemi bir yıldan uzun veya kısa olursa **dönemin kullanılma nedeni ve tutarların tam karşılaştırılabilir olmadığı** açıklanır. p. 37'ye göre uygulamada **52 haftalık dönem kullanılması TMS 1 tarafından engellenmez**.",
        'TMS 1 p. 36',
    ),
    # düzey 3
    '0026': patch(
        "Normal faaliyet döngüsü 18 ay olan bir üretim işletmesinin raporlama dönemi sonundaki bakiyeleri şöyledir: kasa ve banka 150.000 ₺ (kullanım kısıtı yok), 10 ay vadeli ticari alacaklar 320.000 ₺, ticari amaçla elde tutulan hisse senetleri 90.000 ₺, 15 ayda satılması beklenen stoklar 410.000 ₺, personele verilen 30 ay vadeli borçlar 200.000 ₺, yatırım amaçlı gayrimenkuller 750.000 ₺ ve ertelenmiş vergi varlığı 60.000 ₺. İşletmenin dönen varlık toplamı kaç ₺'dir?",
        {
            'A': '1.170.000',
            'B': '880.000',
            'C': '970.000',
            'D': '1.030.000',
            'E': '560.000',
        },
        'C',
        "TMS 1 p. 66'ya göre normal faaliyet döngüsünde gerçekleşecek (stoklar 15 ay olsa da), ticari amaçla elde tutulan ve 12 ay içinde gerçekleşecek varlıklar ile kısıtsız nakit dönen varlıktır. 30 ay vadeli personel alacakları ve yatırım amaçlı gayrimenkuller duran varlıktır; p. 56'ya göre **ertelenmiş vergi varlıkları dönen varlık olarak sınıflandırılmaz**: 150.000 + 320.000 + 90.000 + 410.000 = **970.000 ₺**.",
        'TMS 1 p. 56, 66, 68',
    ),
    # düzey 3
    '0027': patch(
        'Bir işletmenin 2026 Mart ayında vadesi dolacak kredisi vardır. Raporlama dönemi sonunda yürürlükte olan kredi sözleşmesi, işletmeye tek taraflı kararıyla krediyi aynı bankadan 2029 yılına kadar yenileme hakkı vermektedir ve işletme bu hakkı kullanmayı beklemektedir. Kredi finansal durum tablosunda nasıl sınıflandırılır?',
        {
            'A': 'Özkaynak kalemi',
            'B': 'Karşılık',
            'C': 'Koşullu borç',
            'D': 'Kısa vadeli borç',
            'E': 'Uzun vadeli borç',
        },
        'E',
        "TMS 1 p. 73'e göre işletme, raporlama dönemi sonunda mevcut bir kredi sözleşmesi uyarınca borcu **raporlama döneminden sonra en az 12 ay süreyle yenileme hakkına sahipse ve bunu bekliyorsa**, borç vadesi daha kısa olsa bile uzun vadeli sınıflandırılır.",
        'TMS 1 p. 73',
    ),
    # düzey 2
    '0028': patch(
        'Normal faaliyet döngüsü 20 ay olan bir gemi inşa işletmesinin, üretimde kullandığı malzemeler için tedarikçilere olan ticari borçlarının bir kısmı raporlama döneminden 14 ay sonra ödenecektir. Bu ticari borçlar nasıl sınıflandırılır?',
        {
            'A': 'Uzun vadeli borç',
            'B': 'Kısa vadeli borç',
            'C': 'Koşullu borç',
            'D': 'Diğer duran yükümlülük',
            'E': 'Kısmen uzun vadeli borç',
        },
        'B',
        "TMS 1 p. 70'e göre ticari borçlar ile çalışanlara ilişkin tahakkuklar gibi işletmenin **normal faaliyet döngüsünde kullanılan işletme sermayesinin parçası** olan borçlar, raporlama döneminden sonraki 12 aydan daha geç ödenecek olsalar bile **kısa vadeli** sınıflandırılır.",
        'TMS 1 p. 70',
    ),
    # düzey 3
    '0029': patch(
        'Bir işletme, yönetimin satışa karar verdiği ve aktif olarak alıcı aradığı bir fabrika binasını TFRS 5 kapsamında satış amaçlı sınıflandırmıştır; binaya ilişkin ipotekli kredi de alıcıya devredilecektir. Bu kalemlerin finansal durum tablosunda sunumu hakkında aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Kredi diğer borçlardan ayrı sunulur',
            'B': 'Kredi kısa vadeli borçlarda yer alır',
            'C': 'Bina diğer varlıklardan ayrı sunulur',
            'D': 'Bina ile kredi netleştirilerek gösterilir',
            'E': 'Bina dönen varlıklar arasında yer alır',
        },
        'D',
        "TMS 1 p. 54(j) ve (p) ile TFRS 5 p. 38'e göre satış amaçlı sınıflandırılan varlıklar ile bunlarla ilişkili borçlar **ayrı ayrı** sunulur; **netleştirilmez**. Satış amaçlı duran varlık grupları dönen varlık, ilişkili borçlar kısa vadeli borç olarak gösterilir.",
        'TMS 1 p. 54; TFRS 5 p. 38',
    ),
    # düzey 2
    '0030': patch(
        'Borsada işlem gören bir işletme 30 Haziran 2026 tarihli altı aylık özet (kısa) finansal tablolarını hazırlamaktadır. Bu özet tabloların yapısı ve içeriği hangi standarda göre belirlenir?',
        {
            'A': 'TMS 10',
            'B': 'TMS 1',
            'C': 'TFRS 7',
            'D': 'TMS 34',
            'E': 'TMS 8',
        },
        'D',
        "TMS 1 p. 4'e göre TMS 1, ara dönemde hazırlanan **özet finansal tabloların yapısına ve içeriğine uygulanmaz**; bunlar **TMS 34 Ara Dönem Finansal Raporlama**'ya göre hazırlanır. TMS 1'in genel özelliklere ilişkin paragrafları (p. 15-35) ise bu tablolara da uygulanır.",
        'TMS 1 p. 4; TMS 34',
    ),
    # düzey 1
    '0031': patch(
        "Bir işletme finansal durum tablosunu 'Bilanço', kâr veya zarar ve diğer kapsamlı gelir tablosunu 'Gelir Tablosu' başlığıyla sunmuştur. TMS 1'e göre bu başlıkların kullanılması hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Kullanılabilir',
            'B': 'Konsolide tablolarda kullanılamaz',
            'C': 'Denetçi onayıyla kullanılabilir',
            'D': 'Kullanılamaz',
            'E': 'Ara dönemde kullanılabilir',
        },
        'A',
        "TMS 1 p. 10'a göre işletme, bu standartta kullanılanlardan **farklı tablo başlıkları kullanabilir**; örneğin finansal durum tablosu yerine 'bilanço' başlığı kullanılabilir.",
        'TMS 1 p. 10',
    ),
    # düzey 3
    '0032': patch(
        "Giderlerini nitelik esasına göre sunan bir üretim işletmesinin dönem verileri şöyledir: hasılat 5.000.000 ₺, kullanılan hammadde ve malzeme 2.100.000 ₺, mamul ve yarı mamul stoklarında artış 150.000 ₺, çalışanlara sağlanan fayda giderleri 1.200.000 ₺, amortisman giderleri 400.000 ₺. İşletmenin faaliyet kârı kaç ₺'dir?",
        {
            'A': '1.150.000',
            'B': '1.850.000',
            'C': '1.600.000',
            'D': '1.700.000',
            'E': '1.450.000',
        },
        'E',
        "TMS 1 p. 102'ye göre nitelik esasında mamul ve yarı mamul stoklarındaki **artış, giderleri azaltan** bir kalem olarak gösterilir: 5.000.000 − 2.100.000 + 150.000 − 1.200.000 − 400.000 = **1.450.000 ₺**.",
        'TMS 1 p. 102',
    ),
    # düzey 3
    '0033': patch(
        'Bir işletme, yeniden değerleme modeliyle ölçtüğü ve özkaynakta 150.000 ₺ yeniden değerleme artışı bulunan arsasını dönem içinde satmıştır. İşletme yeniden değerleme artışını kullanım sırasında aktarmamaktadır. Satışla birlikte bu 150.000 ₺ nereye aktarılır?',
        {
            'A': 'Hasılata',
            'B': 'Kâr veya zarara',
            'C': 'Sermayeye',
            'D': 'Geçmiş yıllar kârlarına',
            'E': 'Yasal yedeklere',
        },
        'D',
        "TMS 1 p. 96 ve TMS 16 p. 41'e göre yeniden değerleme artışları sonraki dönemlerde **kâr veya zarara yeniden sınıflandırılmaz**; varlık elden çıkarıldığında özkaynak içinde **doğrudan geçmiş yıllar kârlarına** aktarılabilir.",
        'TMS 1 p. 96; TMS 16 p. 41',
    ),
    # düzey 3
    '0034': patch(
        "Bir işletme yurt dışındaki bağlı ortaklığını dönem içinde tamamen elden çıkarmıştır. Bu bağlı ortaklığa ilişkin olarak özkaynakta birikmiş 60.000 ₺ çevrim farkı kazancı bulunmaktadır. Elden çıkarma döneminde bu tutarın diğer kapsamlı gelirden kâr veya zarara aktarılması TMS 1'de hangi terimle ifade edilir?",
        {
            'A': 'Yeniden değerleme',
            'B': 'Geriye dönük düzeltme',
            'C': 'Hata düzeltmesi',
            'D': 'Yeniden sınıflandırma düzeltmesi',
            'E': 'Tahmin değişikliği',
        },
        'D',
        "TMS 1 p. 7 ve 92'ye göre cari veya önceki dönemlerde diğer kapsamlı gelirde muhasebeleştirilip cari dönemde **kâr veya zarara aktarılan** tutarlara **yeniden sınıflandırma düzeltmesi** denir; TMS 21 p. 48 yurt dışı işletmenin elden çıkarılmasında bunu gerektirir.",
        'TMS 1 p. 92-93; TMS 21 p. 48',
    ),
    # düzey 2
    '0035': patch(
        "Bir işletme kâr veya zarar bölümünde sunulacak zorunlu kalemleri belirlemektedir. Aşağıdakilerden hangisi TMS 1'e göre kâr veya zarar bölümünde ayrıca gösterilmesi gereken kalemlerden biri değildir?",
        {
            'A': 'Yeniden değerleme artışı',
            'B': 'Özkaynak yöntemiyle değerlenen yatırımların kâr payı',
            'C': 'Finansman maliyetleri',
            'D': 'Vergi gideri',
            'E': 'Hasılat',
        },
        'A',
        "TMS 1 p. 82'ye göre kâr veya zarar bölümünde hasılat, finansman maliyetleri, özkaynak yöntemiyle değerlenen iştirak ve iş ortaklıklarının kâr veya zararlarından paylar ve vergi gideri gibi kalemler sunulur. **Yeniden değerleme artışı diğer kapsamlı gelir** kalemidir.",
        'TMS 1 p. 82',
    ),
    # düzey 2
    '0036': patch(
        'Bir işletme dipnotlarında sermayesini nasıl yönettiğini, sermaye olarak neyi kabul ettiğini ve dışarıdan belirlenen bir sermaye yeterliliği şartına tabi olup olmadığını anlatmaktadır. Bu açıklamanın amacı aşağıdakilerden hangisidir?',
        {
            'A': 'Vergi planlaması yapmak',
            'B': 'Kâr payı dağıtmak',
            'C': 'Hasılatı ölçmek',
            'D': 'Stokları değerlemek',
            'E': 'Sermaye yönetimini değerlendirmek',
        },
        'E',
        "TMS 1 p. 134'e göre işletme, finansal tablo kullanıcılarının **sermayenin yönetimine ilişkin amaç, politika ve süreçlerini değerlendirebilmesini** sağlayacak bilgileri açıklar.",
        'TMS 1 p. 134-135',
    ),
    # düzey 3
    '0037': patch(
        "Bir işletme finansal tablolarının dipnotlarında hukuki şeklini, kayıtlı adresini ve faaliyetlerinin niteliğini açıklamış, ancak ana ortaklığının ve grubun nihai ana ortaklığının adını açıklamamıştır. İşletme bir grubun parçasıdır. TMS 1'e göre eksik bırakılan bilgi hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Açıklanması isteğe bağlıdır',
            'B': 'Açıklanması gerekir',
            'C': 'Vergi dairesine bildirilir',
            'D': 'Faaliyet raporunda verilir',
            'E': 'Denetim raporunda verilir',
        },
        'B',
        "TMS 1 p. 138'e göre işletme; yerleşim yeri ve hukuki şeklini, kayıtlı adresini, faaliyetlerinin niteliğini ve **ana ortaklığının ve grubun nihai ana ortaklığının adını** finansal tablolarla birlikte açıklar.",
        'TMS 1 p. 138',
    ),
    # düzey 3
    '0038': patch(
        "Bir işletmenin raporlama dönemi sonundaki varlıkları şöyledir: kasa 90.000 ₺, vadeli mevduat 60.000 ₺ (raporlama döneminden sonra 2 yıl süreyle teminat olarak bloke), TFRS 5 kapsamında satış amaçlı sınıflandırılmış bina 500.000 ₺, 6 ay vadeli ticari alacaklar 280.000 ₺, bağlı ortaklığa verilen 3 yıl vadeli borç 120.000 ₺ ve stoklar 340.000 ₺. Dönen varlıkların toplamı kaç ₺'dir?",
        {
            'A': '1.210.000',
            'B': '1.270.000',
            'C': '710.000',
            'D': '1.390.000',
            'E': '1.330.000',
        },
        'A',
        "TMS 1 p. 66'ya göre 12 ay içinde gerçekleşecek varlıklar ve kullanımı kısıtlanmamış nakit dönen varlıktır; TFRS 5 kapsamında **satış amaçlı sınıflandırılan duran varlık** dönen varlıklar arasında ayrı kalem olarak sunulur. 2 yıl bloke mevduat ve 3 yıl vadeli borç verme duran varlıktır: 90.000 + 500.000 + 280.000 + 340.000 = **1.210.000 ₺**.",
        'TMS 1 p. 54, 66; TFRS 5',
    ),
    # düzey 2
    '0039': patch(
        "TMS 1'e ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Nakit akış tablosu dışındaki tablolar tahakkuk esasına göre hazırlanır\n\nII. Olağanüstü kalemler dipnotlarda ayrı başlıkla sunulabilir\n\nIII. Dipnotlar tam finansal tablo setinin parçasıdır",
        {
            'A': 'I ve III',
            'B': 'I ve II',
            'C': 'Yalnız III',
            'D': 'Yalnız I',
            'E': 'I, II ve III',
        },
        'A',
        "TMS 1 p. 27'ye göre tahakkuk esası uygulanır (I); p. 10'a göre dipnotlar tam setin parçasıdır (III). p. 87'ye göre olağanüstü kalem **ne tabloda ne dipnotlarda** sunulabilir (II yanlış).",
        'TMS 1 p. 10, 27, 87',
    ),
    # düzey 2
    '0040': patch(
        'Netleştirmeye ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Hasılatın satış iskontoları düşülerek sunulması netleştirme yasağına aykırıdır\n\nII. Duran varlık satış kazancı, satış giderleri düşülerek net sunulur\n\nIII. Stoklar için ayrılan değer düşüklüğü karşılığı düşülerek sunum netleştirme sayılmaz',
        {
            'A': 'Yalnız II',
            'B': 'I, II ve III',
            'C': 'II ve III',
            'D': 'Yalnız III',
            'E': 'I ve II',
        },
        'C',
        "TMS 1 p. 33-34'e göre duran varlık satış kazancının satış giderleri düşülerek sunulması (II) ve stok değer düşüklüğü gibi **değerleme düzeltmelerinin** düşülerek sunulması (III) netleştirme sayılmaz. Hasılatın iskonto düşülerek ölçülmesi de TFRS 15'in gereğidir, yasağa aykırı değildir (I yanlış).",
        'TMS 1 p. 32-34',
    ),
    # düzey 2
    '0041': patch(
        'Bir anonim şirket dönem içinde ortaklarına nakit kâr payı dağıtmış, nakit karşılığı sermaye artırımı yapmış, maddi duran varlıklarını yeniden değerlemiş ve yurt dışı işletmesinden çevrim farkı doğmuştur. Aşağıdakilerden hangisi özkaynak değişim tablosunda ortakların ortaklık sıfatıyla yaptıkları işlemler arasında gösterilir?',
        {
            'A': 'Kâr payı dağıtımı',
            'B': 'Yabancı para çevrim farkı',
            'C': 'Yeniden değerleme artışı',
            'D': 'Aktüeryal kayıp',
            'E': 'Dönem net kârı',
        },
        'A',
        "TMS 1 p. 106'ya göre özkaynak değişim tablosu toplam kapsamlı geliri ve **ortaklarla ortaklık sıfatıyla yapılan işlemleri** (katkılar ve dağıtımlar) ayrı gösterir. Kâr payı dağıtımı ve sermaye artırımı ortaklarla işlemdir; yeniden değerleme, çevrim farkı, dönem kârı ve aktüeryal kayıp toplam kapsamlı gelirin parçasıdır.",
        'TMS 1 p. 106-107',
    ),
    # düzey 1
    '0042': patch(
        "Bir işletme finansal tablolarını hazırlarken işlemleri nakit tahsil veya ödendiği anda değil, gerçekleştiği dönemde tanımaktadır. TMS 1'e göre nakit akış tablosu dışındaki finansal tablolar hangi esasa göre hazırlanır?",
        {
            'A': 'Temkinlilik esası',
            'B': 'Tahakkuk esası',
            'C': 'Tarihî maliyet esası',
            'D': 'Gerçeğe uygun değer esası',
            'E': 'Nakit esası',
        },
        'B',
        "TMS 1 p. 27'ye göre işletme, **nakit akışlarına ilişkin bilgiler hariç** finansal tablolarını **tahakkuk esasına** göre hazırlar.",
        'TMS 1 p. 27-28',
    ),
    # düzey 3
    '0043': patch(
        "Bir işletmenin yönetimi, uzun vadeli kredisinin yenilenmesine ilişkin görüşmelerin sonuçlanmaması nedeniyle işletmenin sürekliliği konusunda önemli şüphe doğuran bir belirsizlik bulunduğunu, ancak tasfiye niyeti olmadığını ve süreklilik varsayımının uygun olduğunu değerlendirmiştir. TMS 1'e göre yapılması gereken aşağıdakilerden hangisidir?",
        {
            'A': 'Tasfiye esasına geçilmesi',
            'B': 'Kredi için karşılık ayrılması',
            'C': 'Tabloların yayımının ertelenmesi',
            'D': 'Varlıkların satış değeriyle ölçülmesi',
            'E': 'Belirsizliğin açıklanması',
        },
        'E',
        "TMS 1 p. 25'e göre yönetim, işletmenin sürekliliği konusunda önemli şüphe doğurabilecek olay veya koşullara ilişkin **önemli belirsizliklerin farkındaysa bunları açıklar**; tasfiye niyeti yoksa tablolar süreklilik esasına göre hazırlanmaya devam eder.",
        'TMS 1 p. 25',
    ),
    # düzey 2
    '0044': patch(
        "Bir işletme finansal durum tablosunda, her biri toplam varlıkların %0,3'ü kadar olan peşin ödenmiş sigorta, peşin ödenmiş kira ve iş avansları kalemlerini tek satırda 'diğer dönen varlıklar' olarak göstermiştir. Bu uygulama TMS 1'in hangi ilkesiyle açıklanır?",
        {
            'A': 'Sunumda tutarlılık',
            'B': 'Tahakkuk esası',
            'C': 'İşletmenin sürekliliği',
            'D': 'Önemlilik ve birleştirme',
            'E': 'Netleştirme',
        },
        'D',
        "TMS 1 p. 29'a göre işletme, benzer kalemlerin **önemli olan her sınıfını ayrı** sunar; **önemli olmayan** kalemler niteliği veya işlevi benzer kalemlerle birleştirilir. Bu birleştirme netleştirme sayılmaz, çünkü varlık ile borç birbirinden düşülmemektedir.",
        'TMS 1 p. 29-31',
    ),
    # düzey 2
    '0045': patch(
        "Bir işletme, faaliyetlerinin niteliğinde önemli bir değişiklik olmamasına ve hiçbir TFRS bunu gerektirmemesine rağmen her yıl finansal durum tablosundaki kalemlerin sırasını ve gruplamasını değiştirmektedir. Bu uygulama TMS 1'in hangi ilkesine aykırıdır?",
        {
            'A': 'Sunumda tutarlılık',
            'B': 'Önemlilik',
            'C': 'Netleştirme',
            'D': 'Gerçeğe uygun sunum',
            'E': 'Tahakkuk esası',
        },
        'A',
        "TMS 1 p. 45'e göre finansal tablolardaki kalemlerin sunumu ve sınıflandırılması, faaliyetlerin niteliğinde önemli bir değişiklik olması veya bir TFRS'nin gerektirmesi dışında **dönemden döneme tutarlı** olarak sürdürülür.",
        'TMS 1 p. 45',
    ),
    # düzey 3
    '0046': patch(
        'Bir işletme, bir standardın ölçüm hükmünü uygulamamış; bunun yerine uygun gördüğü farklı bir yöntemi kullanmıştır. Farkın etkisi önemlidir ve söz konusu hükmün uygulanmasının finansal tabloları yanıltıcı hâle getireceğine ilişkin aşırı nadir bir durum da yoktur. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Uygun olmayan politika açıklamayla düzeltilemez',
            'B': "İşletme TFRS'ye tam uyum beyan edebilir",
            'C': "Finansal tablolar TFRS'ye uygun sayılmaz",
            'D': 'Uyum beyanı açık ve koşulsuz olmalıdır',
            'E': 'Uygunsuzluk dipnot açıklamasıyla giderilmez',
        },
        'B',
        "TMS 1 p. 16'ya göre işletme ancak TFRS'lerin **bütün gerekliliklerine** uyuyorsa TFRS'ye uygunluğu açık ve koşulsuz olarak beyan edebilir. p. 18'e göre uygun olmayan muhasebe politikaları, açıklama yapılarak veya dipnotla düzeltilemez; p. 19'daki sapma ancak aşırı nadir durumlarda mümkündür.",
        'TMS 1 p. 16, 19-20',
    ),
    # düzey 3
    '0047': patch(
        "Bir işletmenin 31.12.2025 tarihli borçları şöyledir: 4 ay içinde ödenecek ticari borçlar 260.000 ₺; taksitli 5 yıl vadeli banka kredisi 1.000.000 ₺ (bunun 200.000 ₺'lik taksidi 2026 yılında ödenecek); 3 yıl vadeli başka bir kredi 600.000 ₺ (31.12.2025 itibarıyla sözleşme koşulu ihlal edildiği için banka ödemeyi hemen talep edebilir durumdadır; banka Şubat 2026'da, tablolar onaylanmadan önce, ödeme talep etmeyeceğini bildirmiştir) ve 15 ay sonra ödenecek bir borç senedi 900.000 ₺. Kısa vadeli borçların toplamı kaç ₺'dir?",
        {
            'A': '860.000',
            'B': '1.960.000',
            'C': '1.060.000',
            'D': '460.000',
            'E': '1.860.000',
        },
        'C',
        "TMS 1 p. 69'a göre 12 ay içinde ödenecek kısım kısa vadelidir (ticari borçlar ve kredinin 2026 taksidi). p. 74'e göre raporlama dönemi sonunda koşul ihlali nedeniyle talep edildiğinde ödenecek hâle gelen borç, **raporlama döneminden sonra** kreditör ödeme talep etmemeyi kabul etse bile kısa vadelidir. 15 ay vadeli senet uzun vadelidir: 260.000 + 200.000 + 600.000 = **1.060.000 ₺**.",
        'TMS 1 p. 69, 74',
    ),
    # düzey 3
    '0048': patch(
        "Bir işletmenin 5 yıl vadeli kredisinin sözleşmesine göre, işletmenin 30 Haziran 2026 tarihli ara dönem tablolarında cari oranı 1,2'nin altına düşerse banka krediyi hemen geri isteyebilecektir. 31 Aralık 2025 itibarıyla sözleşmenin ihlal edildiği bir koşul yoktur. Kredi 31.12.2025 tarihli finansal durum tablosunda nasıl sınıflandırılır?",
        {
            'A': 'Kısa vadeli borç',
            'B': 'Koşullu borç',
            'C': 'Uzun vadeli borç',
            'D': 'Özkaynak kalemi',
            'E': 'Kısmen kısa vadeli borç',
        },
        'C',
        "TMS 1 p. 72B'ye göre (2022 değişikliği) işletmenin **raporlama döneminden sonra uyması gereken** sözleşme koşulları, raporlama dönemi sonundaki erteleme hakkının varlığını etkilemez; kredi uzun vadeli kalır. p. 76ZA uyarınca koşullar ve ihlal riskine ilişkin bilgiler açıklanır.",
        'TMS 1 p. 72B, 76ZA',
    ),
    # düzey 2
    '0049': patch(
        "Bir holdingin konsolide finansal durum tablosunda bağlı ortaklıklardaki azınlık ortaklarına ait paylar bulunmaktadır. TMS 1'e göre kontrol gücü olmayan paylar finansal durum tablosunda nerede sunulur?",
        {
            'A': 'Dönen varlıklarda',
            'B': 'Dipnotlarda',
            'C': 'Uzun vadeli borçlarda',
            'D': 'Kısa vadeli borçlarda',
            'E': 'Özkaynaklar içinde',
        },
        'E',
        "TMS 1 p. 54(q)-(r)'ye göre finansal durum tablosunda **özkaynaklar içinde sunulan kontrol gücü olmayan paylar** ile ana ortaklığın sahiplerine ait çıkarılmış sermaye ve yedekler ayrı kalemler olarak gösterilir.",
        'TMS 1 p. 54',
    ),
    # düzey 3
    '0050': patch(
        "Bir işletme 5 yıl vadeli kredisinin bir sözleşme koşulunu Kasım 2025'te ihlal etmiştir. Banka, raporlama döneminin sonundan önce, 15 Aralık 2025'te işletmeye ihlali gidermesi için 31.12.2025'ten itibaren 15 ay süre tanımış ve bu süre içinde ödeme talep etmeyeceğini yazılı olarak kabul etmiştir. Kredi 31.12.2025 tarihli finansal durum tablosunda nasıl sınıflandırılır?",
        {
            'A': 'Diğer kısa vadeli yükümlülük',
            'B': 'Kısa vadeli borç',
            'C': 'Uzun vadeli borç',
            'D': 'Karşılık',
            'E': 'Koşullu borç',
        },
        'C',
        "TMS 1 p. 75'e göre kreditör **raporlama döneminin sonuna kadar**, işletmenin ihlali giderebileceği ve bu süre içinde ödeme talep edemeyeceği, raporlama döneminden sonra **en az 12 ay** süren bir ek süre tanımayı kabul etmişse borç uzun vadeli sınıflandırılır. Ek süre raporlama tarihinden sonra verilseydi borç kısa vadeli olurdu.",
        'TMS 1 p. 75',
    ),
    # düzey 3
    '0051': patch(
        'Bir işletme cari dönemde finansal tablo kalemlerinin sınıflandırmasını değiştirmiştir. Ancak önceki döneme ait verilerin bir kısmı, yeni sınıflandırmayı mümkün kılacak şekilde toplanmamıştır ve bu verilerin yeniden oluşturulması uygulanabilir değildir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Sınıflandırma değişikliğinin niteliği açıklanır',
            'B': 'Uygulanabilir ölçüde karşılaştırmalı tutarlar yeniden sınıflandırılır',
            'C': 'Tutarlar yeniden sınıflandırılsaydı yapılacak düzeltmelerin niteliği açıklanır',
            'D': 'Yeniden sınıflandırılamayan tutarların nedeni açıklanır',
            'E': 'Önceki dönem tutarları tahmini rakamlarla doldurulmalıdır',
        },
        'E',
        "TMS 1 p. 41'e göre sunum veya sınıflandırma değiştiğinde karşılaştırmalı tutarlar **uygulanabilir olmadıkça** yeniden sınıflandırılır; p. 42'ye göre uygulanabilir değilse bunun **nedeni** ve tutarlar yeniden sınıflandırılsaydı yapılacak düzeltmelerin **niteliği** açıklanır. Uydurma tahminle doldurma öngörülmez.",
        'TMS 1 p. 41-42',
    ),
    # düzey 2
    '0052': patch(
        "Bir işletmenin fabrikası deprem nedeniyle ağır hasar görmüş ve bu olay önemli bir zarara yol açmıştır. Yönetim bu zararı kâr veya zarar tablosunda 'olağanüstü kalemler' başlığıyla ayrı göstermek istemektedir. TMS 1'e göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Olağanüstü kalem özkaynakta sunulur',
            'B': 'Olağanüstü kalem vergi sonrası sunulur',
            'C': 'Olağanüstü kalem dipnotta sunulur',
            'D': "Olağanüstü kalem DKG'de sunulur",
            'E': 'Olağanüstü kalem sunulamaz',
        },
        'E',
        "TMS 1 p. 87'ye göre işletme hiçbir gelir veya gider kalemini **ne tabloda ne de dipnotlarda olağanüstü kalem olarak** sunamaz. Zarar önemliyse p. 97-98 uyarınca niteliği ve tutarı ayrıca açıklanır.",
        'TMS 1 p. 87',
    ),
    # düzey 2
    '0053': patch(
        "Bir grubun konsolide dönem kârı 900.000 ₺'dir. Bu kârın 180.000 ₺'lik kısmı bağlı ortaklıklardaki kontrol gücü olmayan paylara aittir. Kâr veya zarar tablosunda ana ortaklığın sahiplerine ait dönem kârı olarak kaç ₺ gösterilir?",
        {
            'A': '540.000',
            'B': '900.000',
            'C': '720.000',
            'D': '180.000',
            'E': '1.080.000',
        },
        'C',
        "TMS 1 p. 81B'ye göre dönem kâr veya zararı; **kontrol gücü olmayan paylara** ve **ana ortaklığın sahiplerine** ait olarak ayrı ayrı sunulur: 900.000 − 180.000 = **720.000 ₺**.",
        'TMS 1 p. 81B',
    ),
    # düzey 3
    '0054': patch(
        'Bir işletme, diğer kapsamlı gelir kalemlerinin her birini vergi etkisinden önce sunmayı ve vergiyi toplu göstermeyi tercih etmiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Vergi tek satırda ve gruplamadan gösterilir',
            'B': 'Her DKG kalemine ilişkin vergi açıklanır',
            'C': 'Vergi, yeniden sınıflandırılacak ve sınıflandırılmayacak gruplara dağıtılır',
            'D': 'DKG kalemleri vergi öncesi sunulabilir',
            'E': 'DKG kalemleri vergi etkisi düşülmüş sunulabilir',
        },
        'A',
        "TMS 1 p. 90-91'e göre DKG kalemleri vergi etkisi düşülmüş olarak veya vergi öncesi sunulabilir; vergi öncesi sunulursa vergi, **yeniden sınıflandırılacak ve sınıflandırılmayacak kalemler arasında dağıtılarak** gösterilir. Her kaleme ilişkin vergi tutarı da açıklanır.",
        'TMS 1 p. 90-91',
    ),
    # düzey 2
    '0055': patch(
        "Bir işletme dipnotlarında, TFRS'lerde birebir yer alan ve işletmeye özgü hiçbir unsur içermeyen standart politika metinlerini uzun uzun tekrarlamaktadır. 2023'te değişen TMS 1'e göre işletmenin açıklaması gereken muhasebe politikası bilgisi hangisidir?",
        {
            'A': 'Bütün muhasebe politikaları',
            'B': 'Vergi mevzuatındaki politikalar',
            'C': 'Değişen politikalar',
            'D': 'Denetçinin önerdiği politikalar',
            'E': 'Önemli muhasebe politikası bilgisi',
        },
        'E',
        "TMS 1 p. 117'ye göre (2023 değişikliği) işletme **önemli muhasebe politikası bilgisini** açıklar. Önemli olmayan politika bilgilerini açıklaması gerekmez; açıklarsa önemli bilgiyi gölgelememelidir (p. 117D).",
        'TMS 1 p. 117-117B',
    ),
    # düzey 3
    '0056': patch(
        "Bir işletmenin yönetim kurulu, 31.12.2025 tarihli finansal tablolar onaylanmadan önce, 2025 kârından ortaklara 500.000 ₺ kâr payı dağıtılmasını genel kurula önermiştir. Genel kurul toplantısı Nisan 2026'da yapılacaktır. Bu kâr payı 31.12.2025 tarihli finansal tablolarda nasıl yer alır?",
        {
            'A': 'Dipnotlarda açıklanır',
            'B': 'Kısa vadeli borç olarak',
            'C': 'Kâr veya zararda gider olarak',
            'D': 'Özkaynaktan indirim olarak',
            'E': 'Karşılık olarak',
        },
        'A',
        "TMS 10 p. 12-13'e göre raporlama döneminden sonra önerilen kâr payları raporlama dönemi sonunda borç olarak **muhasebeleştirilmez**; TMS 1 p. 137 uyarınca tablolar onaylanmadan önce önerilen ancak dağıtıma yöneltilmemiş kâr payı tutarı **dipnotlarda açıklanır**.",
        'TMS 1 p. 137; TMS 10 p. 12-13',
    ),
    # düzey 3
    '0057': patch(
        "Bir işletmenin dönem net kârı 400.000 ₺'dir. Dönemde yurt dışı işletmeden 90.000 ₺ çevrim farkı kaybı, tanımlanmış fayda planından 30.000 ₺ aktüeryal kayıp ve maddi duran varlıklardan 70.000 ₺ yeniden değerleme artışı doğmuştur. Diğer kapsamlı gelir kalemleri vergi etkisi düşülmüş tutarlardır. Toplam kapsamlı gelir kaç ₺'dir?",
        {
            'A': '350.000',
            'B': '400.000',
            'C': '280.000',
            'D': '470.000',
            'E': '590.000',
        },
        'A',
        'Toplam kapsamlı gelir: 400.000 − 90.000 − 30.000 + 70.000 = **350.000 ₺**.',
        'TMS 1 p. 81A',
    ),
    # düzey 3
    '0058': patch(
        "Bir grubun konsolide dönem kârı 800.000 ₺, konsolide diğer kapsamlı geliri 200.000 ₺'dir. Kârın 120.000 ₺'lik, diğer kapsamlı gelirin 30.000 ₺'lik kısmı kontrol gücü olmayan paylara aittir. Ana ortaklığın sahiplerine ait toplam kapsamlı gelir kaç ₺'dir?",
        {
            'A': '880.000',
            'B': '850.000',
            'C': '820.000',
            'D': '680.000',
            'E': '1.000.000',
        },
        'B',
        "TMS 1 p. 81B'ye göre toplam kapsamlı gelir de kontrol gücü olmayan paylara ve ana ortaklığın sahiplerine dağıtılarak sunulur: (800.000 − 120.000) + (200.000 − 30.000) = **850.000 ₺**.",
        'TMS 1 p. 81B',
    ),
    # düzey 2
    '0059': patch(
        'Aşağıdakilerden hangileri sonradan kâr veya zarara yeniden sınıflandırılabilecek diğer kapsamlı gelir kalemlerindendir?\n\nI. Yurt dışı işletmenin çevriminden doğan kur farkları\n\nII. Maddi duran varlık yeniden değerleme artışları\n\nIII. Tanımlanmış fayda planlarının yeniden ölçüm kazanç ve kayıpları',
        {
            'A': 'I ve II',
            'B': 'Yalnız II',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'Yalnız I',
        },
        'E',
        "TMS 1 p. 82A ve 96'ya göre yurt dışı işletmenin çevrim farkları elden çıkarmada kâr veya zarara yeniden sınıflandırılır (I). Yeniden değerleme artışları (II) ile tanımlanmış fayda planı yeniden ölçümleri (III) **yeniden sınıflandırılmaz**.",
        'TMS 1 p. 82A, 96',
    ),
    # düzey 3
    '0060': patch(
        "Aşağıdakilerden hangileri TMS 1'e göre doğrudur?\n\nI. Raporlama dönemi bir yıldan kısa olursa bunun nedeni açıklanır\n\nII. Tasfiye niyeti olmasa da önemli süreklilik belirsizlikleri açıklanır\n\nIII. Sunum ve sınıflandırma yönetimin tercihine göre her yıl değiştirilebilir",
        {
            'A': 'I ve III',
            'B': 'II ve III',
            'C': 'Yalnız I',
            'D': 'Yalnız II',
            'E': 'I ve II',
        },
        'E',
        "TMS 1 p. 36'ya göre dönem uzunluğundaki değişikliğin nedeni açıklanır (I); p. 25'e göre tasfiye niyeti olmasa da önemli süreklilik belirsizlikleri açıklanır (II). p. 45'e göre sunum ancak faaliyetlerde önemli değişiklik olması veya bir TFRS'nin gerektirmesi hâlinde değiştirilir (III yanlış).",
        'TMS 1 p. 25, 36, 45',
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
    print(f"1 paket / {len(PATCHES)} soru ('TMS 1 Finansal Tablolarin Sunulusu' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
