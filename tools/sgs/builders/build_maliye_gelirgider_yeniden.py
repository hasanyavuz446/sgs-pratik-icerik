#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kamu Gelirleri ve Giderleri — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gercek sinav profiline gore yeniden yazim: kamu gelirlerinin turleri, vergi teorisi (tarife, yansima, kapitalizasyon, ek yuk, esneklik, vergi gayreti, entegrasyon, vergi harcamalari), kamu harcamalarinin siniflandirilmasi ve artis teorileri. Cikmis sorularin yakin turevleri (§11) bilincli olarak farkli olay ve acilarla yazildi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Kamu maliyesi teorisi; analitik butce siniflandirmasi (5018 sayili KMYKK cercevesi)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/maliye/kamu_gelir_gider.json"
STYLE_REF = 'SGS Maliye (gercek sinav profiline kalibre: kisa sik + olay/hesap)'
ONEK = "mal-gelirgider-gen-"


def patch(stem, options, answer, solution, ref='Kamu maliyesi teorisi'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Bir belediye, mülkiyetindeki bir dükkânı ihaleyle kiraya vermiş ve kiracıdan kira bedeli almıştır. Kiracı aynı dükkânda faaliyete başlayabilmek için belediyeden işyeri açma ruhsatı almış ve bunun için ayrıca bir bedel ödemiştir. İki gelir sırasıyla hangi türdendir?',
        {
            'A': 'Parafiskal gelir – Resim',
            'B': 'Mülk geliri – Resim',
            'C': 'Resim – Harç',
            'D': 'Harç – Mülk geliri',
            'E': 'Mülk geliri – Harç',
        },
        'B',
        'Belediyenin kendi taşınmazını kiraya vermesi özel hukuk ilişkisine dayanır ve egemenlik gücüne dayanmayan **mülk (domen) geliridir**. Bir faaliyete başlamak için idareden alınan izin veya ruhsatın karşılığı ise cebri nitelikteki **resimdir**. Harç, kişinin yararlandığı özel bir kamu hizmetinin (tapu, yargı işlemi) karşılığıdır.',
        'Kamu maliyesi teorisi: kamu gelirlerinin sınıflandırılması',
    ),
    # düzey 0
    '0002': patch(
        'Devletin (merkez bankası aracılığıyla) para basma yetkisini kullanarak paranın nominal değeri ile basım maliyeti arasındaki farktan elde ettiği gelir aşağıdakilerden hangisidir?',
        {
            'A': 'Senyoraj',
            'B': 'Rant geliri',
            'C': 'Parafiskal gelir',
            'D': 'Tekel kârı',
            'E': 'Şerefiye (değerlenme payı)',
        },
        'A',
        "**Senyoraj** para basma gelirine verilen addır; paranın satın alma gücü ile üretim maliyeti arasındaki farktan doğar. Enflasyon yoluyla paranın değerinin düşmesi de benzer biçimde bir 'enflasyon vergisi' yaratır.",
        'Kamu maliyesi teorisi: senyoraj',
    ),
    # düzey 2
    '0003': patch(
        'Aşağıdaki uygulamalardan hangisi vergi indirimi niteliğindedir?',
        {
            'A': 'Tahsil imkânı kalmayan vergi alacağının kayıtlardan silinmesi',
            'B': 'Emisyon primi kazancının kurumlar vergisi dışında bırakılması',
            'C': 'Engelli çalışanın ücret matrahından engellilik derecesine göre bir tutarın düşülmesi',
            'D': 'Vergi borcunun ödeme süresinin teminat karşılığında uzatılması',
            'E': 'Kanunla kurulan bir emekli sandığının kurum olarak kurumlar vergisi dışında tutulması',
        },
        'C',
        'Matrahtan veya hesaplanan vergiden belirli bir tutarın düşülmesi **vergi indirimidir** (ör. engellilik indirimi). Bir kurumun bütünüyle vergi dışında tutulması **muafiyet**, belirli bir kazancın vergi dışında bırakılması **istisna**, ödeme süresinin uzatılması **tecil**, alacağın kayıtlardan silinmesi ise **terkindir**.',
        'Kamu maliyesi teorisi: vergi indirimi',
    ),
    # düzey 2
    '0004': patch(
        'Düz (proporsiyonel) oranlı bir gelir vergisinde marjinal vergi oranı ile ortalama vergi oranı arasındaki ilişki aşağıdakilerden hangisidir?',
        {
            'A': 'Gelir arttıkça ikisi de yükselir',
            'B': 'Marjinal oran ortalama orandan küçüktür',
            'C': 'Marjinal oran ortalama orandan büyüktür',
            'D': 'Her gelir düzeyinde birbirine eşittir',
            'E': 'Gelir arttıkça ikisi de düşer',
        },
        'D',
        'Düz oranlı vergide her ek liraya aynı oran uygulandığı için marjinal oran sabittir ve ortalama orana **eşittir**. Artan oranlıda marjinal oran ortalamanın üstünde, tersine artan oranlıda altındadır.',
        'Kamu maliyesi teorisi: tarife türleri',
    ),
    # düzey 2
    '0005': patch(
        "Vergi idaresinin aynı matrahı her yıl farklı yorumlarla belirlemesi ve mükelleflerin ödeyecekleri vergiyi önceden hesaplayamaması Adam Smith'in hangi vergileme ilkesiyle çelişir?",
        {
            'A': 'Esneklik ilkesi',
            'B': 'Uygunluk ilkesi',
            'C': 'Genellik ilkesi',
            'D': 'İktisadilik ilkesi',
            'E': 'Belirlilik ilkesi',
        },
        'E',
        '**Belirlilik ilkesi**, verginin tutarının, ödeme zamanının ve biçiminin mükellef için açık ve kesin olmasını, idarenin keyfi yorumuna bırakılmamasını öngörür. Uygunluk ödeme zamanının mükellefe elverişli olmasını, iktisadilik tahsil maliyetinin düşüklüğünü ifade eder.',
        'Kamu maliyesi teorisi: vergileme ilkeleri',
    ),
    # düzey 1
    '0006': patch(
        'Vergi yükünün mükelleflerin kamu hizmetlerinden sağladıkları yarar ölçüsünde dağıtılmasını öngören yaklaşım aşağıdakilerden hangisidir?',
        {
            'A': 'Yararlanma ilkesi',
            'B': 'Ödeme gücü ilkesi',
            'C': 'Eşit fedakârlık ilkesi',
            'D': 'Genellik ilkesi',
            'E': 'Mali anestezi',
        },
        'A',
        '**Yararlanma (fayda) ilkesi** vergiyi kamu hizmetinin bir fiyatı gibi görür ve bireylerin yararlandıkları ölçüde ödemesini öngörür; harç ve katılma payları bu mantığa yakındır. **Ödeme gücü** ilkesi ise vergiyi gelir, servet ve harcama gibi ödeme gücü göstergelerine bağlar ve modern vergi sistemlerinin temelidir.',
        'Kamu maliyesi teorisi: vergilendirmede fayda ilkesi',
    ),
    # düzey 2
    '0007': patch(
        'Bir market zinciri, rakip mağazalar nedeniyle yeni vergi konulan hazır yemek ürünlerinin fiyatını artıramamaktadır. Zincir, bu vergi yükünü müşterilerin fiyata duyarsız olduğu ekmek ve tuz gibi ürünlerin fiyatlarını artırarak karşılamaktadır. Bu durum hangi yansıma türüdür?',
        {
            'A': 'Verginin amortismanı',
            'B': 'Vergi takozu',
            'C': 'Ters yansıma',
            'D': 'Çapraz yansıma',
            'E': 'Geri yansıma',
        },
        'D',
        'Vergi yükünün, vergi konulan maldan farklı bir malın fiyatına eklenerek aktarılması **çapraz yansımadır**. Satıcı, talebi esnek olan vergili malda fiyatı artırırsa satışlarını kaybedeceği için yükü talebi esnek olmayan başka mallara aktarır. Geri yansımada yük mal akışının tersine, tedarikçilere aktarılır.',
        'Kamu maliyesi teorisi: verginin yansıması',
    ),
    # düzey 2
    '0008': patch(
        'Ücret gelirlerine uygulanan vergi oranının artırılması karşısında bir çalışanın eski gelir düzeyini korumak için daha fazla çalışması, verginin hangi etkisiyle açıklanır?',
        {
            'A': 'Dışlama etkisi',
            'B': 'Gelir etkisi',
            'C': 'Çarpan etkisi',
            'D': 'Duyuru etkisi',
            'E': 'İkame (yerine koyma) etkisi',
        },
        'B',
        'Vergi kişinin reel gelirini azaltır; eski yaşam düzeyini korumak isteyen birey daha çok çalışırsa bu **gelir etkisidir**. **İkame etkisi** ise vergi nedeniyle çalışmanın boş zamana göre göreli getirisinin düşmesi ve kişinin daha az çalışmasıdır. Net etki iki etkinin göreli büyüklüğüne bağlıdır.',
        'Kamu maliyesi teorisi: gelir ve ikame etkisi',
    ),
    # düzey 3
    '0009': patch(
        "Doğrusal arz ve talep koşullarında bir mala konulan birim başına 10 ₺'lik vergi, satış miktarını 1.000 birimden 800 birime düşürmüştür. Verginin yarattığı ek yük (refah kaybı) kaç ₺'dir?",
        {
            'A': '8.000 ₺',
            'B': '2.000 ₺',
            'C': '500 ₺',
            'D': '1.000 ₺',
            'E': '10.000 ₺',
        },
        'D',
        'Doğrusal arz ve talepte ek yük, Harberger üçgeninin alanıdır: ½ × birim vergi × miktardaki azalış = ½ × 10 × (1.000 − 800) = **1.000 ₺**. 8.000 ₺ devletin elde ettiği vergi hasılatıdır (10 × 800); ek yük, hasılatın ötesinde ortaya çıkan net refah kaybıdır.',
        'Kamu maliyesi teorisi: ek yük',
    ),
    # düzey 2
    '0010': patch(
        'Artan oranlı gelir vergisi tarifesinin dilim tutarları enflasyona göre güncellenmediğinde, reel geliri artmayan mükelleflerin üst dilimlere geçmesiyle reel vergi yükünün artmasına ne ad verilir?',
        {
            'A': 'Verginin amortismanı',
            'B': 'Mali anestezi',
            'C': 'Mali sürüklenme',
            'D': 'Vergi gayreti',
            'E': 'Tanzi-Olivera etkisi',
        },
        'C',
        'Nominal gelirler enflasyonla artarken dilimler sabit kalırsa mükellefler reel olarak zenginleşmeden üst dilimlere kayar ve vergi yükü artar: **mali sürüklenme** (bracket creep). **Tanzi-Olivera etkisi** ise tarh ile tahsil arasındaki gecikme nedeniyle enflasyonun tahsil edilen verginin reel değerini düşürmesidir.',
        'Kamu maliyesi teorisi: enflasyon ve vergi',
    ),
    # düzey 2
    '0011': patch(
        'Aşağıdakilerden hangisi vergi kaçakçılığı değil, vergiden kaçınma örneğidir?',
        {
            'A': 'Gerçek olmayan giderleri sahte belgeyle kayda almak',
            'B': 'Defter ve belgeleri incelemeden kaçırmak için gizlemek',
            'C': 'Elde edilen kira gelirini beyan etmemek',
            'D': 'Satışları faturasız yapıp beyan dışı bırakmak',
            'E': 'Yüksek vergili bir malın tüketiminden vazgeçip vergisiz ikame mala yönelmek',
        },
        'E',
        '**Vergiden kaçınma** yasal yollarla vergi yükünden kurtulmaktır: vergiye konu faaliyetten veya tüketimden vazgeçmek, kanunun tanıdığı seçenekleri kullanmak gibi. Faturasız satış, sahte belge, defter gizleme ve gelirin beyan dışı bırakılması kanuna aykırı olduğundan **vergi kaçakçılığıdır** (ya da vergi ziyaına yol açan fiillerdir).',
        'Kamu maliyesi teorisi: vergi kaçınması',
    ),
    # düzey 3
    '0012': patch(
        "Türkiye'de yerleşik bir mühendisin Almanya'da yürüttüğü proje için aldığı ücrete hem Almanya'da hem Türkiye'de vergi hesaplanmıştır. İki ülke arasındaki anlaşma, Almanya'da ödenen verginin Türkiye'de hesaplanan vergiden düşülmesine imkân vermektedir. Anlaşmanın çözdüğü sorun ve kullandığı yöntem aşağıdakilerden hangisidir?",
        {
            'A': 'Vergi arbitrajı – Mahsup yöntemi',
            'B': 'Uluslararası çifte vergilendirme – Mahsup yöntemi',
            'C': 'Uluslararası vergi rekabeti – Mahsup yöntemi',
            'D': 'Transfer fiyatlandırması – İstisna yöntemi',
            'E': 'Uluslararası çifte vergilendirme – İstisna yöntemi',
        },
        'B',
        'Aynı gelirin iki ülkede vergilendirilmesi **uluslararası çifte vergilendirmedir**. İkamet ülkesinin yurt dışında ödenen vergiyi kendi hesapladığı vergiden düşmesi **mahsup (vergi kredisi) yöntemidir**; yurt dışı gelirin ikamet ülkesinde hiç vergilendirilmemesi ise istisna yöntemi olurdu.',
        'Kamu maliyesi teorisi: uluslararası vergilendirme',
    ),
    # düzey 1
    '0013': patch(
        'Bütçe kanununa ekli cetvelde ödeneklerin Millî Eğitim Bakanlığı, Sağlık Bakanlığı ve Karayolları Genel Müdürlüğü gibi kamu idareleri itibarıyla gösterilmesi hangi sınıflandırmaya dayanır?',
        {
            'A': 'Kurumsal (idari) sınıflandırma',
            'B': 'Fonksiyonel sınıflandırma',
            'C': 'Finansman tipi sınıflandırması',
            'D': 'Ekonomik sınıflandırma',
            'E': 'Hukuki sınıflandırma',
        },
        'A',
        'Ödeneklerin harcamayı yapacak **kamu idareleri** itibarıyla gösterilmesi kurumsal (idari) sınıflandırmadır. **Fonksiyonel** sınıflandırma harcamanın hangi kamu hizmetine (eğitim, sağlık) gittiğini, **ekonomik** sınıflandırma ise harcamanın ekonomik niteliğini (personel, mal-hizmet alımı, faiz, transfer, sermaye) gösterir.',
        'Kamu maliyesi teorisi: kamu harcamalarının sınıflandırılması',
    ),
    # düzey 2
    '0014': patch(
        '"Eğitim harcamaları bu yıl bütçede en yüksek paya sahip kalemdir." ve "Personel giderleri toplam harcamaların üçte birini oluşturmaktadır." ifadeleri sırasıyla hangi sınıflandırmalara dayanır?',
        {
            'A': 'Ekonomik – İdari',
            'B': 'Fonksiyonel – İdari',
            'C': 'İdari – Ekonomik',
            'D': 'Fonksiyonel – Ekonomik',
            'E': 'Ekonomik – Fonksiyonel',
        },
        'D',
        'Eğitim, sağlık, savunma gibi **kamu hizmeti türleri fonksiyonel** sınıflandırmanın, personel giderleri, mal ve hizmet alımları, faiz ve transferler gibi **harcamanın ekonomik niteliği** ise ekonomik sınıflandırmanın konusudur. Kurum bazında dağılım idari sınıflandırmadır.',
        'Kamu maliyesi teorisi: analitik bütçe sınıflandırması',
    ),
    # düzey 2
    '0015': patch(
        'Aşağıdakilerden hangileri transfer harcaması niteliğindedir?\n\nI. Yoksul ailelere yapılan nakdi sosyal yardım\n\nII. Kamu hastanesinde çalışan hemşirenin maaşı\n\nIII. Üniversite öğrencilerine verilen karşılıksız burs\n\nIV. İç borçlara ödenen faiz',
        {
            'A': 'I ve III',
            'B': 'I, II ve III',
            'C': 'I, III ve IV',
            'D': 'II ve IV',
            'E': 'I, II, III ve IV',
        },
        'C',
        'Sosyal yardım (I), karşılıksız burs (III) ve borç faizi (IV) karşılığında devlete mal veya hizmet sunulmayan, satın alma gücünü aktaran **transfer harcamalarıdır**. Hemşire maaşı (II) devletin emek hizmeti satın aldığı **gerçek (reel)** bir harcamadır.',
        'Kamu maliyesi teorisi: reel ve transfer harcamaları',
    ),
    # düzey 2
    '0016': patch(
        'Sağlık ve eğitim gibi emek yoğun kamu hizmetlerinde verimlilik artışının sanayiye göre yavaş kalması, buna karşın ücretlerin ekonomi genelinde birlikte artması nedeniyle kamu hizmetlerinin göreli maliyetinin yükselmesini açıklayan yaklaşım hangisidir?',
        {
            'A': 'Baumol yaklaşımı',
            'B': 'Peacock-Wiseman yaklaşımı',
            'C': 'Rostow-Musgrave yaklaşımı',
            'D': 'Mali yanılsama yaklaşımı',
            'E': 'Wagner kanunu',
        },
        'A',
        "**Baumol**, verimlilik artışı hızlı olan sektörlerdeki ücret artışlarının verimliliği düşük emek yoğun hizmet sektörlerine de yansıdığını, bu nedenle bu hizmetlerin birim maliyetinin sürekli yükseldiğini ('maliyet hastalığı') ileri sürer. Kamu hizmetleri ağırlıkla bu nitelikte olduğundan kamu harcamaları artar.",
        'Kamu maliyesi teorisi: kamu harcamalarının artış teorileri',
    ),
    # düzey 2
    '0017': patch(
        'Kamu harcamaları ile özel harcamalar arasındaki ilişkiye ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kamunun özel sektörle rekabet eden alanlara girmesi özel harcamaların yerini alabilir',
            'B': 'Tam istihdama yakın dönemde kamu harcamalarının dışlama etkisi güçlenir',
            'C': 'Kamu yatırımları özel yatırımları dışlayamaz, onları ancak tamamlar',
            'D': 'Kamunun borçlanarak harcaması faizleri yükselterek özel yatırımları dışlayabilir',
            'E': 'Altyapı yatırımları özel yatırımların verimliliğini artırarak onları özendirebilir',
        },
        'C',
        'Kamu harcamaları özel harcamalarla hem **tamamlayıcı** (altyapının özel yatırımı özendirmesi, içleme etkisi) hem de **ikame** (dışlama etkisi) ilişkisi içinde olabilir. Borçlanmanın faizi yükseltmesi ve kapasitenin dolu olduğu dönemler dışlamayı güçlendirir. Dışlamanın hiç olamayacağını söyleyen ifade yanlıştır.',
        'Kamu maliyesi teorisi: kamu harcamalarının etkileri',
    ),
    # düzey 2
    '0018': patch(
        'Bir işverenin çalışan için katlandığı toplam işgücü maliyeti ile çalışanın eline geçen net ücret arasındaki, gelir vergisi ve sosyal güvenlik primlerinden oluşan farka ne ad verilir?',
        {
            'A': 'Mali sürüklenme',
            'B': 'Vergi takozu',
            'C': 'Mali anestezi',
            'D': 'Vergi gayreti',
            'E': 'Vergi harcaması',
        },
        'B',
        '**Vergi takozu** (tax wedge), işgücü maliyeti ile net ücret arasındaki farktır; ücret üzerindeki gelir vergisi ile işçi ve işveren sigorta primlerinin toplam maliyete oranı olarak ölçülür. Yüksek takoz kayıt dışı istihdamı özendirebilir.',
        'Kamu maliyesi teorisi: vergi takozu',
    ),
    # düzey 3
    '0019': patch(
        "Bir mala birim başına 30 ₺ vergi konulmuş; malın alıcıların ödediği fiyatı 100 ₺'den 120 ₺'ye yükselmiştir. Verginin yükü alıcı ve satıcı arasında nasıl dağılmıştır ve talep ile arzın göreli esnekliği hakkında ne söylenebilir?",
        {
            'A': 'Alıcılar 10 ₺, satıcılar 20 ₺ taşır; talep arza göre daha esnektir',
            'B': 'Yük yarı yarıya paylaşılır; esneklikler eşittir',
            'C': 'Alıcılar 20 ₺, satıcılar 10 ₺ taşır; talep arza göre daha esnektir',
            'D': 'Yükün tamamı satıcılarda kalır; talep tam esnektir',
            'E': 'Alıcılar 20 ₺, satıcılar 10 ₺ taşır; talep arza göre daha az esnektir',
        },
        'E',
        "Alıcının ödediği fiyat 20 ₺ artmıştır; satıcının eline geçen net fiyat 120 − 30 = 90 ₺, yani 10 ₺ düşmüştür. Yükün 2/3'ü alıcıda, 1/3'ü satıcıdadır. Yük **esnekliği düşük tarafta** toplandığından talep, arza göre daha az esnektir.",
        'Kamu maliyesi teorisi: vergi yükünün dağılımı',
    ),
    # düzey 2
    '0020': patch(
        'Bir ülkenin, diğer ülkelerin vergi tabanını aşındıracak biçimde düşük vergi oranları ve özel avantajlar sunarak yabancı sermaye ve şirket merkezlerini kendine çekmeye çalışması hangi kavramla açıklanır?',
        {
            'A': 'Zararlı vergi rekabeti',
            'B': 'Mali sürüklenme',
            'C': 'Vergi arbitrajı',
            'D': 'Uluslararası çifte vergilendirme',
            'E': 'Transfer fiyatlandırması',
        },
        'A',
        "**Vergi rekabeti**, ülkelerin hareketli vergi tabanlarını (sermaye, kâr) çekmek için vergi yükünü düşürme yarışıdır; diğer ülkelerin vergi tabanını aşındıran biçimi 'zararlı vergi rekabeti' olarak adlandırılır. Transfer fiyatlandırması şirket içi fiyatlarla kârı düşük vergili ülkeye kaydırmadır.",
        'Kamu maliyesi teorisi: vergi rekabeti',
    ),
    # düzey 2
    '0021': patch(
        'Bir meslek odasının kanun gereği üyelerinden topladığı zorunlu aidatı kendi bütçesinde harcaması ile devletin genel bütçesine giren gümrük vergisi arasındaki temel farka ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Aidat, özel bir hizmetin karşılığı olduğu için bir harçtır',
            'B': 'Gümrük vergisi parafiskal gelir, aidat ise genel bütçe geliridir',
            'C': 'Aidat gönüllü ödendiği için kamu geliri niteliği taşımaz',
            'D': 'İkisi de genel bütçe geliridir; aralarındaki tek fark tahsil eden kurumun farklı olmasıdır',
            'E': 'Aidat, belirli bir kesimden özel amaçla alınan bütçe dışı parafiskal gelirdir',
        },
        'E',
        '**Parafiskal gelirler**, kamu kurumu niteliğindeki meslek kuruluşları ve sosyal güvenlik kurumları gibi genel bütçe dışındaki kuruluşların belirli bir kesimden **zorunlu** olarak topladığı ve kendi özel amaçlarına harcadığı gelirlerdir. Oda aidatı zorunlu olduğu için kamu geliridir; belirli bir hizmetin karşılığı olmadığından harç da değildir. Gümrük vergisi genel bütçe geliridir.',
        'Kamu maliyesi teorisi: parafiskal gelirler',
    ),
    # düzey 2
    '0022': patch(
        'Vergiyi doğuran olay gerçekleştiği hâlde yükümlünün kanun gereği vergi dışında tutulduğu durum ile vergi konusunun bir kısmının vergi dışında bırakıldığı durum sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',
        {
            'A': 'İstisna – Muafiyet',
            'B': 'Muafiyet – Vergi indirimi',
            'C': 'Muafiyet – İstisna',
            'D': 'İstisna – Vergi indirimi',
            'E': 'Vergi indirimi – İstisna',
        },
        'C',
        '**Muafiyet** sübjektif niteliktedir: kanunen vergi mükellefi olması gereken kişi (ör. bir kurum) vergi dışında bırakılır. **İstisna** objektif niteliktedir: vergi konusunun bir bölümü (ör. belirli bir kazanç türü) vergi dışında tutulur. Vergi indirimi ise matrah veya hesaplanan vergiden yapılan indirimdir.',
        'Kamu maliyesi teorisi: vergi unsurları',
    ),
    # düzey 3
    '0023': patch(
        "Dilim usulü artan oranlı bir gelir vergisi tarifesinde ilk 10.000 ₺'ye %10, 10.001-30.000 ₺ arasına %20, 30.000 ₺'yi aşan kısma %30 uygulanmaktadır. Geliri 40.000 ₺ olan mükellefin ortalama ve marjinal vergi oranları sırasıyla kaçtır?",
        {
            'A': '%20 ve %30',
            'B': '%30 ve %30',
            'C': '%30 ve %20',
            'D': '%25 ve %30',
            'E': '%20 ve %20',
        },
        'A',
        "Vergi = 10.000 × %10 + 20.000 × %20 + 10.000 × %30 = 1.000 + 4.000 + 3.000 = 8.000 ₺. Ortalama oran = 8.000 / 40.000 = **%20**; son liraya uygulanan marjinal oran **%30**'dur. Dilim usulü artan oranlılıkta marjinal oran ortalama orandan büyüktür.",
        'Kamu maliyesi teorisi: artan oranlı tarife',
    ),
    # düzey 1
    '0024': patch(
        'Aşağıdakilerden hangisi spesifik (miktar esaslı) bir vergiye örnektir?',
        {
            'A': "Taşınmazın rayiç değerinin binde 2'si oranında alınan vergi",
            'B': 'Sigaranın paketi başına alınan sabit tutarlı vergi',
            'C': "Beyan edilen yıllık gelirin %15'i oranında alınan vergi",
            'D': "Otomobilin satış bedelinin %20'si oranında alınan vergi",
            'E': "İthal malın gümrük değerinin %10'u oranında alınan vergi",
        },
        'B',
        '**Spesifik vergilerde** matrah malın fiziki birimidir (adet, litre, kilogram, paket) ve birim başına sabit tutar alınır. Matrahın değer (bedel, rayiç, gümrük değeri) olarak ifade edildiği ve buna oran uygulandığı vergiler **ad valorem** vergilerdir.',
        'Kamu maliyesi teorisi: ad valorem ve spesifik vergi',
    ),
    # düzey 2
    '0025': patch(
        "Tarım ürünlerinin hasadının sonbaharda yapıldığı dikkate alınarak çiftçilerin vergi ödeme zamanının hasat sonrasına denk getirilmesi Adam Smith'in hangi vergileme ilkesiyle uyumludur?",
        {
            'A': 'Adalet ilkesi',
            'B': 'İktisadilik ilkesi',
            'C': 'Belirlilik ilkesi',
            'D': 'Uygunluk ilkesi',
            'E': 'Genellik ilkesi',
        },
        'D',
        "Smith'in **uygunluk (ödeme kolaylığı)** ilkesine göre vergi, mükellefin ödemesinin en kolay olduğu zaman ve biçimde alınmalıdır. Belirlilik vergi tutarı ve zamanının açık olmasını, iktisadilik tahsil maliyetinin düşük olmasını ifade eder.",
        'Kamu maliyesi teorisi: vergileme ilkeleri',
    ),
    # düzey 2
    '0026': patch(
        'Aynı gelir düzeyindeki iki mükellefin eşit vergi ödemesi ile farklı gelir düzeyindeki mükelleflerin farklı vergi ödemesi sırasıyla hangi kavramlarla ifade edilir?',
        {
            'A': 'Yatay eşitlik – Dikey eşitlik',
            'B': 'Fayda ilkesi – Ödeme gücü ilkesi',
            'C': 'Yatay eşitlik – Fayda ilkesi',
            'D': 'Genellik ilkesi – Eşitlik ilkesi',
            'E': 'Dikey eşitlik – Yatay eşitlik',
        },
        'A',
        '**Yatay eşitlik**, eşit ödeme gücüne sahip olanların eşit vergilendirilmesini; **dikey eşitlik**, farklı ödeme gücüne sahip olanların farklı (ödeme gücüyle orantılı ya da artan oranlı) vergilendirilmesini ifade eder. Fayda ilkesi vergiyi kamu hizmetinden yararlanmaya bağlar.',
        'Kamu maliyesi teorisi: vergide adalet',
    ),
    # düzey 2
    '0027': patch(
        'Yeni konulan bir verginin yükünün kimde kalacağı, arz ve talep esneklikleriyle ilişkili olarak aşağıdakilerden hangisinde doğru verilmiştir?',
        {
            'A': 'Yük, esnekliklerden bağımsız olarak yarı yarıya paylaşılır',
            'B': 'Yük, kanunen vergiyi ödeyen tarafta kalır',
            'C': 'Yük, esnekliği daha düşük olan tarafta daha fazla kalır',
            'D': 'Yük, esnekliği daha yüksek olan tarafta daha fazla kalır',
            'E': 'Talep tam esnek ise yükün tamamı alıcıya geçer',
        },
        'C',
        'Vergi yükü piyasada **daha az esnek** tarafta toplanır; çünkü o taraf fiyat değişikliklerine miktarını ayarlayarak tepki veremez. Talep tam esnekse (yatay talep) fiyat yükselemez ve yükün tamamı satıcıda kalır. Kanunen vergiyi ödeyenin kimliği yükün nihai dağılımını belirlemez.',
        'Kamu maliyesi teorisi: verginin yansıması',
    ),
    # düzey 2
    '0028': patch(
        'Aşağıdaki vergilerden hangisi yalnız gelir etkisi doğurduğu için ek yük (refah kaybı) yaratmaz?',
        {
            'A': 'Faiz gelirine uygulanan stopaj',
            'B': 'Sigara üzerine alınan spesifik vergi',
            'C': 'Tek bir mala uygulanan özel tüketim vergisi',
            'D': 'Götürü (sabit tutarlı) vergi',
            'E': 'Emek gelirine uygulanan artan oranlı vergi',
        },
        'D',
        'Tutarı bireyin kararlarından (çalışma, tüketim, tasarruf) bağımsız olan **götürü vergi**, göreli fiyatları değiştirmediği için ikame etkisi doğurmaz; yalnız gelir etkisi yaratır ve ek yük oluşturmaz. Oranı bir faaliyete veya mala bağlı olan vergiler göreli fiyatları değiştirerek ikame etkisi ve refah kaybı doğurur.',
        'Kamu maliyesi teorisi: ek yük ve etkin vergi',
    ),
    # düzey 3
    '0029': patch(
        'Bir yılda gayrisafi yurt içi hasıla %10, toplam vergi hasılatı %15 artmıştır. Vergi sisteminin gelir esnekliği ve bu değerin anlamı aşağıdakilerden hangisidir?',
        {
            'A': '1,5; vergi hasılatı gelirden daha yavaş artmaktadır',
            'B': '0,67; vergi sistemi artan oranlı yapıdadır',
            'C': '1,5; vergi hasılatı gelirden daha hızlı artmaktadır',
            'D': '0,67; vergi hasılatı gelirden daha yavaş artmaktadır',
            'E': '5; vergi hasılatı gelirle aynı hızda artmaktadır',
        },
        'C',
        "Vergi gelir esnekliği = vergi hasılatındaki % değişme / milli gelirdeki % değişme = 15 / 10 = **1,5**. Esnekliğin 1'den büyük olması hasılatın gelirden daha hızlı arttığını gösterir; bu genellikle artan oranlı tarifelerin ve dolaysız vergilerin ağırlıklı olduğu sistemlerde görülür.",
        'Kamu maliyesi teorisi: vergi gelir esnekliği',
    ),
    # düzey 2
    '0030': patch(
        'Yüksek enflasyon döneminde verginin doğduğu tarih ile tahsil edildiği tarih arasındaki gecikme nedeniyle devletin reel vergi gelirinin azalması hangi kavramla açıklanır?',
        {
            'A': 'Verginin kapitalizasyonu',
            'B': 'Tanzi-Olivera etkisi',
            'C': 'Laffer etkisi',
            'D': 'Pigou etkisi',
            'E': 'Mali sürüklenme',
        },
        'B',
        '**Tanzi-Olivera etkisine** göre vergi, doğduğu tarihteki nominal değerle ve gecikmeyle tahsil edildiğinde enflasyon bu tutarın satın alma gücünü eritir; reel vergi hasılatı düşer. Mali sürüklenme ise enflasyonun tersine reel vergi yükünü artırdığı durumdur.',
        'Kamu maliyesi teorisi: enflasyon ve vergi',
    ),
    # düzey 2
    '0031': patch(
        'Vergi harcamasını, ilgili istisna veya indirim kaldırıldığında mükelleflerin davranışlarındaki değişiklik de hesaba katılarak elde edilecek ek gelirle ölçen yöntem aşağıdakilerden hangisidir?',
        {
            'A': 'Harcama eşdeğeri yöntemi',
            'B': 'Vazgeçilen gelir yöntemi',
            'C': 'Katsayı yöntemi',
            'D': 'Kazanılan gelir yöntemi',
            'E': 'Ortalama gelir yöntemi',
        },
        'D',
        '**Vazgeçilen gelir** yöntemi statiktir: davranışların değişmeyeceğini varsayarak düzenleme nedeniyle kaybedilen vergiyi hesaplar. **Kazanılan gelir** yöntemi, düzenleme kaldırıldığında mükelleflerin tepkilerini de hesaba katarak fiilen elde edilecek ek geliri ölçer. **Harcama eşdeğeri** yöntemi ise aynı faydayı doğrudan harcamayla sağlamanın maliyetini esas alır.',
        'Kamu maliyesi teorisi: vergi harcamaları',
    ),
    # düzey 2
    '0032': patch(
        '"Sübjektif, dolaysız, nakdi, artan oranlı" özelliklerin tamamını taşıyan vergi aşağıdakilerden hangisidir?',
        {
            'A': 'Damga vergisi',
            'B': 'Özel tüketim vergisi',
            'C': 'Katma değer vergisi',
            'D': 'Gelir vergisi',
            'E': 'Emlak vergisi',
        },
        'D',
        'Gelir vergisi, mükellefin kişisel durumunu (asgari geçim, aile durumu vb.) dikkate aldığı için **sübjektif**, yükü kanuni mükellefte kaldığı kabul edildiği için **dolaysız**, parayla ödendiği için **nakdi** ve dilim tarifesi nedeniyle **artan oranlıdır**. KDV ve ÖTV dolaylı ve objektif; emlak vergisi objektif; damga vergisi ise çoğunlukla nispi ya da maktu objektif vergidir.',
        'Kamu maliyesi teorisi: vergi türleri',
    ),
    # düzey 2
    '0033': patch(
        'Analitik bütçe sınıflandırmasının ekonomik kodlarına göre aşağıdaki eşleştirmelerden hangisi yanlıştır?',
        {
            'A': 'Belediyeye altyapı yatırımı için verilen hibe – Sermaye transferleri',
            'B': 'Memur maaşları – Personel giderleri',
            'C': 'Okul binası inşası – Sermaye giderleri',
            'D': 'Kırtasiye ve yakıt alımı – Mal ve hizmet alım giderleri',
            'E': 'İç borç faizi ödemesi – Cari transferler',
        },
        'E',
        'Ekonomik sınıflandırmada borçlanmaya ilişkin faiz ödemeleri ayrı bir kalem olan **faiz giderleri** altında gösterilir; cari transferler karşılıksız cari ödemelerdir. Personel giderleri, sermaye giderleri (sabit sermaye yatırımları), mal ve hizmet alım giderleri ve yatırım amaçlı karşılıksız aktarımlar (sermaye transferleri) eşleştirmeleri doğrudur.',
        'Kamu maliyesi teorisi: ekonomik sınıflandırma',
    ),
    # düzey 3
    '0034': patch(
        'Bir ülkede eğitim harcamaları nominal olarak %40 artmış; aynı dönemde fiyatlar %30, öğrenci sayısı %5 yükselmiştir. Öğrenci başına reel eğitim harcamasındaki değişim aşağıdakilerden hangisidir?',
        {
            'A': 'Yaklaşık %2,6 gerçek artış',
            'B': 'Gerçek artış yoktur, artışın tamamı görünüştedir',
            'C': 'Yaklaşık %10 gerçek artış',
            'D': 'Yaklaşık %40 gerçek artış',
            'E': 'Yaklaşık %5 gerçek artış',
        },
        'A',
        'Öğrenci başına reel harcama endeksi = 1,40 / (1,30 × 1,05) = 1,40 / 1,365 ≈ 1,026, yani yaklaşık **%2,6 gerçek artış**. Nominal artışın büyük kısmı fiyat artışı ve nüfus (öğrenci) artışından kaynaklanan **görünüşte** artıştır. %5 sonucu, basitçe 40 − 30 − 5 çıkarmasının hatalı uygulamasıdır.',
        'Kamu maliyesi teorisi: kamu harcamalarında görünüşte ve gerçek artış',
    ),
    # düzey 2
    '0035': patch(
        'Aşağıdakilerden hangileri kamu harcamalarında görünüşte (nominal) artışa yol açar?\n\nI. Genel fiyat düzeyinin yükselmesi\n\nII. Kişi başına hizmet sabitken nüfusun artması\n\nIII. Kişi başına sunulan hizmetin miktar ve kalitesinin artması\n\nIV. Safi bütçe usulünden gayrisafi bütçe usulüne geçilmesi',
        {
            'A': 'I, II ve III',
            'B': 'I, II ve IV',
            'C': 'I, II, III ve IV',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'B',
        'Fiyat artışı (I), kişi başı hizmet sabitken nüfus artışı (II) ve gelirlerle giderlerin birbirinden mahsup edilmeden bütçeye yazılmasını gerektiren gayrisafi bütçe usulüne geçiş (IV) harcama tutarını büyütür ama kişi başına düşen kamu hizmetini artırmaz: **görünüşte** artış. Kişi başına hizmetin miktar ve kalitesinin artması (III) ise **gerçek** artıştır.',
        'Kamu maliyesi teorisi: görünüşte artış',
    ),
    # düzey 1
    '0036': patch(
        'Sanayileşme ve kişi başı gelirin artmasıyla birlikte kamu harcamalarının milli gelir içindeki payının da artacağını ileri süren yaklaşım aşağıdakilerden hangisidir?',
        {
            'A': 'Peacock-Wiseman yaklaşımı',
            'B': 'Kuznets hipotezi',
            'C': 'Baumol yaklaşımı',
            'D': 'Wagner kanunu',
            'E': 'Mali yanılsama modeli',
        },
        'D',
        '**Wagner kanununa** (artan devlet faaliyetleri kanunu) göre sanayileşme, kentleşme ve gelir artışıyla birlikte düzenleme, altyapı, eğitim ve kültür hizmetlerine talep artar; kamu harcamaları milli gelirden daha hızlı büyür.',
        'Kamu maliyesi teorisi: Wagner kanunu',
    ),
    # düzey 2
    '0037': patch(
        'Kamu projelerinin değerlendirilmesinde kullanılan sosyal iskonto oranının yükseltilmesiyle ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Faydası uzak gelecekte ortaya çıkan projelerin net bugünkü değeri artar',
            'B': 'Uzun vadeli projeler kısa vadelilere göre dezavantajlı hâle gelir',
            'C': 'Gelecekteki fayda ve maliyetlerin bugünkü değeri azalır',
            'D': 'Kabul edilebilir proje sayısı azalabilir',
            'E': 'Oran, toplumun zaman tercihini yansıtır',
        },
        'A',
        'Sosyal iskonto oranı toplumun bugünkü tüketimi geleceğe tercih etme derecesini yansıtır. Oran yükseldikçe gelecekteki fayda ve maliyetlerin bugünkü değeri düşer; faydası uzak gelecekte ortaya çıkan projelerin net bugünkü değeri azalır ve kabul edilebilir proje sayısı daralır.',
        'Kamu maliyesi teorisi: fayda-maliyet analizi',
    ),
    # düzey 2
    '0038': patch(
        'Belirli bir vergi hasılatını en az ek yükle elde etmek için talebi fiyata daha az duyarlı mallara daha yüksek oranlı vergi uygulanmasını öngören kural aşağıdakilerden hangisidir?',
        {
            'A': 'Yatay eşitlik ilkesi',
            'B': 'Eşit marjinal fedakârlık ilkesi',
            'C': 'Ters esneklik (Ramsey) kuralı',
            'D': 'Yararlanma ilkesi',
            'E': 'Haig-Simons gelir tanımı',
        },
        'C',
        "**Ramsey'in ters esneklik kuralına** göre ek yük, vergi karşısında miktarı çok değişen (esnek) mallarda büyüktür; bu nedenle etkinlik açısından talep esnekliği düşük mallara daha yüksek vergi uygulanmalıdır. Kural etkinliği sağlar ancak temel ihtiyaç mallarını ağır vergileyerek dikey eşitlikle çatışabilir.",
        'Kamu maliyesi teorisi: Ramsey vergi kuralı',
    ),
    # düzey 2
    '0039': patch(
        'Bir vergi sisteminde dolaysız vergilerin payının artırılmasının aşağıdaki sonuçlarından hangisi beklenmez?',
        {
            'A': 'Vergi hasılatının gelir esnekliğinin artması',
            'B': 'Vergilerin otomatik istikrarlandırıcı etkisinin güçlenmesi',
            'C': 'Vergi yükünün mükelleflerce daha az hissedilmesi',
            'D': 'Sistemin artan oranlı niteliğinin güçlenmesi',
            'E': 'Mükelleflerin kişisel durumlarının daha çok dikkate alınması',
        },
        'C',
        'Dolaysız vergiler (gelir, kurumlar) mükellefin doğrudan beyan ettiği ve ödediği vergilerdir; yükleri daha **çok** hissedilir. Dolaysız vergilerin payı artınca artan oranlılık ve sübjektiflik güçlenir, hasılat gelire daha duyarlı hâle gelir ve bu duyarlılık otomatik istikrarlandırıcı etkiyi artırır. Yükün daha az hissedilmesi (mali anestezi) dolaylı vergilerin özelliğidir.',
        'Kamu maliyesi teorisi: dolaysız vergilerin payı',
    ),
    # düzey 3
    '0040': patch(
        'Bir vergi reformunda gelir vergisinin sabit ortalama oranı korunarak tarife, marjinal oranın ortalama orana eşit olacağı biçimde değiştirilmek istenmektedir. Bu değişiklik tarifenin hangi yapıya dönüştüğünü gösterir?',
        {
            'A': 'Düz oranlıdan artan oranlıya',
            'B': 'Artan oranlıdan tersine artan oranlıya',
            'C': 'Tersine artan oranlıdan artan oranlıya',
            'D': 'Düz oranlıdan tersine artan oranlıya',
            'E': 'Artan oranlıdan düz oranlıya',
        },
        'E',
        'Marjinal oranın ortalama orana eşit olması **düz oranlı** tarifenin tanımıdır. Artan oranlı tarifede marjinal oran ortalamadan büyük, tersine artan oranlıda küçüktür. Ortalama oranın sabit tutulup marjinal oranın ona eşitlenmesi, artan oranlı yapıdan düz oranlı yapıya geçiştir.',
        'Kamu maliyesi teorisi: artan oranlılığın ölçümü',
    ),
    # düzey 1
    '0041': patch(
        'Kamu iç borçlanmasıyla ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İç borçlanma kural olarak isteğe bağlıdır',
            'B': 'İç borçlanma, vergi gibi geri ödenmeyen bir gelirdir',
            'C': 'İç borçlanma gelecek dönemlere faiz yükü aktarır',
            'D': 'Kaynak yurt içindeki tasarruf sahiplerinden sağlanır',
            'E': 'Devlet tahvili ve hazine bonosu iç borçlanma araçlarıdır',
        },
        'B',
        'Kamu iç borcu, devletin yurt içindeki tasarruf sahiplerinden kural olarak isteğe bağlı biçimde sağladığı ve geri ödeme ile faiz yükümlülüğü doğuran bir gelirdir; başlıca araçları devlet tahvili ve hazine bonosudur. Vergiyi ondan ayıran temel özellik, verginin karşılıksız ve geri ödenmeyen olmasıdır.',
        'Kamu maliyesi teorisi: kamu borçlanması',
    ),
    # düzey 2
    '0042': patch(
        'Bir kamu geliri türü olan harçla ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Harç, belirli bir hizmetle ilişkilendirilmeden alınan karşılıksız bir gelirdir',
            'B': 'Harç, cebrî nitelikte bir kamu geliridir',
            'C': 'Harç, kamu hizmetinden yararlanan kişiden alınır',
            'D': 'Harç tutarı hizmetin maliyetini tam karşılamayabilir',
            'E': 'Pasaport ve noter işlemlerinde alınan bedeller harca örnektir',
        },
        'A',
        'Harç, belirli bir kamu hizmetinden yararlanan kişiden o hizmet karşılığında cebren alınan bir kamu geliridir; tutarı hizmetin maliyetiyle birebir örtüşmeyebilir. Karşılıksız alınması vergiye özgü bir özelliktir.',
        'Kamu maliyesi teorisi: harç ve vergi',
    ),
    # düzey 2
    '0043': patch(
        'Gelir arttıkça ortalama vergi oranının düştüğü tarife aşağıdakilerden hangisidir?',
        {
            'A': 'Sınıf usulü artan oranlı tarife',
            'B': 'Artan oranlı (progresif) tarife',
            'C': 'Düz (proporsiyonel) oranlı tarife',
            'D': 'Azalan oranlı (degresif) artan oranlı tarife',
            'E': 'Tersine artan oranlı (regresif) tarife',
        },
        'E',
        '**Tersine artan oranlı (regresif)** tarifede gelir yükseldikçe ödenen verginin gelire oranı (ortalama oran) düşer; örneğin herkesten aynı tutarda alınan götürü vergi ya da düşük gelirlilerin gelirinin büyük kısmını tükettiği durumlarda harcama vergileri böyle etki yapar. Artan oranlıda ortalama oran yükselir, düz oranlıda sabittir.',
        'Kamu maliyesi teorisi: tarife türleri',
    ),
    # düzey 2
    '0044': patch(
        'Katma değer vergisi gibi genel harcama vergilerinin, düşük gelirlilerin gelirlerinin daha büyük bölümünü tüketime ayırması nedeniyle gelir dağılımı üzerindeki etkisi aşağıdakilerden hangisidir?',
        {
            'A': 'Artan oranlı (progresif) etki',
            'B': 'Ek yükü sıfırlayan etki',
            'C': 'Tersine artan oranlı etki',
            'D': 'Yalın gelir etkisi',
            'E': 'Nötr (dağılımdan bağımsız) etki',
        },
        'C',
        'Düz oranlı bir harcama vergisi, gelire oranlandığında düşük gelirlilere daha yüksek yük bindirir; çünkü onların tüketim/gelir oranı (ortalama tüketim eğilimi) daha yüksektir. Bu nedenle harcama vergilerinin gelire göre etkisi **tersine artan oranlıdır**.',
        'Kamu maliyesi teorisi: harcama vergilerinin etkisi',
    ),
    # düzey 2
    '0045': patch(
        'Aşağıdaki vergileme ilkesi–içerik eşleştirmelerinden hangisi yanlıştır?',
        {
            'A': 'Uygunluk ilkesi – En kolay zaman ve biçimde tahsil',
            'B': 'Genellik ilkesi – Ödeme gücü olan herkesin vergilendirilmesi',
            'C': 'Belirlilik ilkesi – Vergi tutarı ve ödeme zamanının açık olması',
            'D': 'Eşitlik ilkesi – Ödeme gücüne göre vergilendirme',
            'E': 'İktisadilik ilkesi – Vergi hasılatının milli gelirle birlikte artması',
        },
        'E',
        '**İktisadilik** ilkesi, verginin tarh ve tahsil maliyetinin (idarenin ve mükellefin katlandığı maliyetlerin) mümkün olduğunca düşük tutulmasıdır. Vergi hasılatının milli gelirle birlikte değişmesi **esneklik** ilkesinin konusudur. Diğer eşleştirmeler doğrudur.',
        'Kamu maliyesi teorisi: vergileme ilkeleri',
    ),
    # düzey 2
    '0046': patch(
        'Üreticinin, hammadde tedarikçisinin kendisine uyguladığı fiyatı düşürmesini sağlayarak yeni konan verginin yükünü tedarikçiye aktarması hangi yansıma türüdür?',
        {
            'A': 'Dağınık yansıma',
            'B': 'Geri yansıma',
            'C': 'İleri yansıma',
            'D': 'Verginin kapitalizasyonu',
            'E': 'Çapraz yansıma',
        },
        'B',
        'Vergi yükünün mal akışının tersine, yani üretim faktörü sahiplerine veya tedarikçilere aktarılması **geri yansımadır**. Yükün satış fiyatına eklenerek alıcıya aktarılması ileri yansıma, vergi konulan maldan başka bir malın fiyatına aktarılması ise çapraz yansımadır.',
        'Kamu maliyesi teorisi: verginin yansıması',
    ),
    # düzey 3
    '0047': patch(
        "Bir arsanın yıllık kira getirisi 50.000 ₺'dir ve bu getiri üzerinden %30 vergi alınmaktadır. Piyasa, arsanın vergi sonrası net getirisini %5 oranıyla kapitalize ederek değer biçmektedir. Vergi kaldırılırsa arsanın değeri ne kadar artar?",
        {
            'A': '150.000 ₺',
            'B': '700.000 ₺',
            'C': '15.000 ₺',
            'D': '1.000.000 ₺',
            'E': '300.000 ₺',
        },
        'E',
        "Vergili durumda net getiri 50.000 × 0,70 = 35.000 ₺ ve değer 35.000 / 0,05 = 700.000 ₺'dir. Vergi kaldırılınca değer 50.000 / 0,05 = 1.000.000 ₺ olur; artış **300.000 ₺'dir**. Bu, yıllık 15.000 ₺ vergi tasarrufunun kapitalize edilmiş değeridir (15.000 / 0,05). Verginin kaldırılmasıyla servet değerinin artmasına **verginin kapitalizasyonu** denir.",
        'Kamu maliyesi teorisi: verginin kapitalizasyonu',
    ),
    # düzey 2
    '0048': patch(
        'Bir servet unsuru üzerine yeni bir vergi konulması ya da mevcut verginin artırılması sonucunda o servet unsurunun piyasa değerinin düşmesine ne ad verilir?',
        {
            'A': 'Verginin yayılması',
            'B': 'Verginin dönüştürülmesi',
            'C': 'Verginin amortismanı',
            'D': 'Mali sürüklenme',
            'E': 'Verginin kapitalizasyonu',
        },
        'C',
        'Servetten beklenen net gelir vergi nedeniyle azalınca, bu gelirin bugünkü değeri olan servetin fiyatı da düşer; bu **verginin amortismanıdır** ve yükü, vergi konulduğu anda servetin sahibi bulunan kişi taşır. Verginin kaldırılmasıyla ortaya çıkan değer artışı ise kapitalizasyondur.',
        'Kamu maliyesi teorisi: verginin amortismanı',
    ),
    # düzey 2
    '0049': patch(
        "Bir ülkede gelir vergisinin en yüksek oranı %60'tan %50'ye indirilmiş ve izleyen dönemde vergi hasılatı artmıştır. Laffer eğrisine göre bu gözlem neyi gösterir?",
        {
            'A': 'Oran indirimi verginin ek yükünü artırmıştır',
            'B': "Hasılatı en yükselten oran %60'ın üzerindedir",
            'C': 'Başlangıçtaki oran, hasılatı en yükselten oranın altındaydı',
            'D': 'Başlangıçtaki oran, hasılatı en yükselten oranın üzerindeydi',
            'E': 'Vergi oranı ile hasılat arasındaki ilişki doğrusaldır',
        },
        'D',
        "Laffer eğrisi ters U biçimlidir. Oran indirimine rağmen hasılatın artması, ekonominin eğrinin **azalan kolunda** (optimal oranın üzerinde, 'yasak bölgede') bulunduğunu gösterir; bu bölgede oran düşünce çalışma, yatırım ve kayıt içi faaliyet artarak tabanı genişletir. Optimal oranın altında olunsaydı indirim hasılatı düşürürdü.",
        'Kamu maliyesi teorisi: Laffer eğrisi',
    ),
    # düzey 3
    '0050': patch(
        "Bir ülkede fiilî vergi yükü (vergi hasılatı/GSYH) %24, ekonometrik olarak tahmin edilen vergi kapasitesi %30'dur. Bu ülkenin vergi gayreti ve yorumu aşağıdakilerden hangisidir?",
        {
            'A': '0,80; ülke vergi kapasitesinin altında vergi toplamaktadır',
            'B': '0,06; vergi kapasitesi ile fiilî yük arasındaki fark kapanmıştır',
            'C': '1,25; ülke vergi kapasitesinin altında vergi toplamaktadır',
            'D': '0,80; ülke vergi kapasitesinin üzerinde vergi toplamaktadır',
            'E': '1,25; ülke vergi kapasitesinin üzerinde vergi toplamaktadır',
        },
        'A',
        "**Vergi gayreti** = fiilî vergi yükü / vergi kapasitesi (potansiyel vergi yükü) = 24 / 30 = **0,80**. Değerin 1'den küçük olması ülkenin vergileme potansiyelini tam kullanmadığını; 1'den büyük olması ise kapasitenin üzerinde vergi alındığını gösterir.",
        'Kamu maliyesi teorisi: vergi gayreti',
    ),
    # düzey 1
    '0051': patch(
        'Vergi yükünün mükellefler tarafından daha az hissedilmesini sağlamak için dolaylı vergilerin, kaynakta kesintinin ve küçük tutarlı sık ödemelerin tercih edilmesine ne ad verilir?',
        {
            'A': 'Vergi arbitrajı',
            'B': 'Vergi gayreti',
            'C': 'Mali anestezi',
            'D': 'Vergi takozu',
            'E': 'Mali sürüklenme',
        },
        'C',
        '**Mali anestezi**, vergi yükünü mükellefe hissettirmeden alma tekniğidir: fiyatın içine gizlenen dolaylı vergiler, ücretten kaynakta kesilen stopaj ve bölünmüş ödemeler bu amaçla kullanılır. Vergi takozu ise brüt ücret ile net ücret arasındaki vergi ve prim farkıdır.',
        'Kamu maliyesi teorisi: mali anestezi',
    ),
    # düzey 2
    '0052': patch(
        'Ortağın, aldığı kâr payı üzerinden kurum düzeyinde ödenmiş kurumlar vergisinin tamamını veya bir kısmını kendi gelir vergisinden mahsup ettiği entegrasyon yöntemi aşağıdakilerden hangisidir?',
        {
            'A': 'Ortaklık (isnat) yöntemi',
            'B': 'Klasik sistem',
            'C': 'Farklılaştırılmış oran yöntemi',
            'D': 'Kâr payı indirimi yöntemi',
            'E': 'Vergi kredisi yöntemi',
        },
        'E',
        '**Vergi kredisi (imputation)** yönteminde kurum düzeyinde ödenen vergi, ortak düzeyinde bir alacak (kredi) olarak dikkate alınır ve ortağın gelir vergisinden düşülür. Kâr payı indirimi yönteminde dağıtılan kâr kurum matrahından düşülür; ortaklık yönteminde kurum kazancının tamamı dağıtılsın dağıtılmasın ortaklara isnat edilir; klasik sistemde entegrasyon yoktur.',
        'Kamu maliyesi teorisi: kurumlar ve gelir vergisi entegrasyonu',
    ),
    # düzey 2
    '0053': patch(
        "Babasından miras kalan daireyi adına tescil ettiren Ali'nin bu intikal nedeniyle ödediği vergi, vergilerin konularına göre sınıflandırılmasında hangi gruba girer?",
        {
            'A': 'Servet transferi üzerinden alınan vergiler',
            'B': 'Gelir üzerinden alınan vergiler',
            'C': 'Harcama üzerinden alınan vergiler',
            'D': 'Parafiskal yükümlülükler',
            'E': 'Dış ticaret işlemleri üzerinden alınan vergiler',
        },
        'A',
        'Miras yoluyla intikal eden mallar üzerinden alınan **veraset ve intikal vergisi**, servetin karşılıksız el değiştirmesini konu alır; servet (servet transferi) vergileri grubundadır. Intikal bir gelir elde etme veya harcama işlemi değildir; ödenen tutar da belirli bir kesimin özel amaçlı zorunlu katkısı (parafiskal) niteliği taşımaz.',
        'Kamu maliyesi teorisi: vergi türleri',
    ),
    # düzey 2
    '0054': patch(
        'Devletin emeklilere ödediği aylıklar ile bir köprü inşaatı için müteahhide yaptığı hakediş ödemesi, milli gelire etkileri bakımından nasıl nitelendirilir?',
        {
            'A': 'İkisi de gerçek harcamadır; milli geliri doğrudan artırır',
            'B': 'Emekli aylığı transfer harcaması, hakediş ödemesi gerçek harcamadır',
            'C': 'Emekli aylığı sermaye transferi, hakediş ödemesi cari harcamadır',
            'D': 'Emekli aylığı gerçek harcama, hakediş ödemesi transfer harcamasıdır',
            'E': 'İkisi de transfer harcamasıdır; milli geliri doğrudan etkilemez',
        },
        'B',
        'Emekli aylığında devlet karşılığında o dönemde mal veya hizmet almaz; satın alma gücünü aktarır: **transfer harcaması**. Köprü inşaatı için yapılan ödeme ise devletin kaynak kullanarak üretim faktörü ve mal-hizmet satın aldığı **gerçek (reel)** bir harcamadır ve milli geliri doğrudan artırır.',
        'Kamu maliyesi teorisi: reel ve transfer harcamaları',
    ),
    # düzey 2
    '0055': patch(
        'Bir ülkede savaş döneminde hızla artan kamu harcamaları savaş sona erdikten sonra da eski düzeyine inmemiş, vergi yükü de yüksek düzeyde kalmıştır. Bu gelişmeyi açıklayan yaklaşım aşağıdakilerden hangisidir?',
        {
            'A': 'Meltzer-Richard modeli',
            'B': 'Niskanen modeli',
            'C': 'Wagner kanunu',
            'D': 'Peacock-Wiseman yaklaşımı',
            'E': "Baumol'un dengesiz verimlilik yaklaşımı",
        },
        'D',
        "**Peacock ve Wiseman'a** göre kamu harcamaları sürekli değil, savaş ve kriz gibi olağanüstü dönemlerde **sıçramalı** artar; kriz sırasında kabul edilen yüksek vergi yükü toplumca kanıksandığı için harcamalar kriz sonrası eski düzeyine dönmez (yerini alma / eşik etkisi).",
        'Kamu maliyesi teorisi: kamu harcamalarının artış teorileri',
    ),
    # düzey 2
    '0056': patch(
        'Oy hakkının genişlemesiyle medyan seçmenin gelirinin ortalama gelirin altında kalması, yeniden dağıtım politikalarına ve dolayısıyla kamu harcamalarına olan talebi artırır. Bu açıklamayı yapan model aşağıdakilerden hangisidir?',
        {
            'A': 'Peacock-Wiseman yaklaşımı',
            'B': 'Meltzer-Richard modeli',
            'C': 'Baumol yaklaşımı',
            'D': 'Niskanen modeli',
            'E': 'Leviathan modeli',
        },
        'B',
        '**Meltzer-Richard** modelinde gelir dağılımı sağa çarpık olduğundan medyan seçmenin geliri ortalamanın altındadır; bu seçmen yüksek gelirlilerden kendisine yeniden dağıtım yapan daha büyük bir kamu kesimini destekler. Oy hakkının yayılması ve eşitsizliğin artması kamu harcamalarını büyütür.',
        'Kamu maliyesi teorisi: kamu harcamalarının artış teorileri',
    ),
    # düzey 3
    '0057': patch(
        'Bugün 1.000 ₺ maliyeti olan bir kamu projesi iki yıl sonra tek seferde 1.210 ₺ fayda sağlayacaktır. Sosyal iskonto oranı %10 ise projeye ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Net bugünkü değer 100 ₺'dir; proje kabul edilmelidir",
            'B': "Net bugünkü değer 210 ₺'dir; proje kabul edilmelidir",
            'C': "Net bugünkü değer eksi 110 ₺'dir; proje reddedilmelidir",
            'D': "Fayda-maliyet oranı 1,21'dir; proje kabul edilmelidir",
            'E': 'Net bugünkü değer sıfırdır; kabul ve ret arasında kayıtsız kalınır',
        },
        'E',
        "Faydanın bugünkü değeri = 1.210 / (1,10)² = 1.210 / 1,21 = 1.000 ₺. Net bugünkü değer = 1.000 − 1.000 = **0**; fayda-maliyet oranı 1'dir. İskonto yapılmadan hesaplanan 210 ₺ ve 1,21 oranı paranın zaman değerini göz ardı eder.",
        'Kamu maliyesi teorisi: fayda-maliyet analizi',
    ),
    # düzey 2
    '0058': patch(
        'Aşağıdakilerden hangisi olağanüstü (istisnai) kamu gelirlerinden biri değildir?',
        {
            'A': 'Her yıl bütçeye düzenli olarak giren gelir vergisi hasılatı',
            'B': 'Savaş döneminde alınan olağanüstü servet vergisi',
            'C': 'Zorunlu (cebri) istikraz',
            'D': 'Kamu varlıklarının özelleştirilmesinden elde edilen gelir',
            'E': 'Emisyon (karşılıksız para basma)',
        },
        'A',
        'Olağanüstü kamu gelirleri düzenli olarak her yıl elde edilmeyen, genellikle kriz ve özel dönemlerde başvurulan gelirlerdir: olağanüstü vergiler, zorunlu borçlanma, para basma ve varlık satışları. Her yıl düzenli tahsil edilen gelir vergisi **olağan** kamu geliridir.',
        'Kamu maliyesi teorisi: olağanüstü kamu gelirleri',
    ),
    # düzey 2
    '0059': patch(
        'Aşağıdaki kamu geliri–türü eşleştirmelerinden hangisi doğrudur?',
        {
            'A': 'Avukatın baroya ödediği zorunlu aidat – Resim',
            'B': 'İşverenin ödediği sigorta primi – Mülk geliri',
            'C': 'Taşınmazın satışında tapuda ödenen bedel – Harç',
            'D': 'Hazine taşınmazının satış bedeli – Vergi',
            'E': 'Karşılıksız para basmadan doğan gelir – Parafiskal gelir',
        },
        'C',
        'Tapu işlemi, kişinin yararlandığı özel bir kamu hizmetidir; karşılığında ödenen bedel **harçtır**. Baroya ödenen zorunlu aidat ve sigorta primi parafiskal gelir, hazine taşınmazının satış bedeli mülk (varlık satış) geliri, para basma geliri ise senyorajdır.',
        'Kamu maliyesi teorisi: kamu gelirlerinin sınıflandırılması',
    ),
    # düzey 2
    '0060': patch(
        'Vergi kapasitesini belirleyen etkenlere ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Vergi idaresinin etkinliği fiilî yükün kapasiteye yaklaşmasını sağlar',
            'B': 'Kişi başına milli gelirin yükselmesi kapasiteyi artırır',
            'C': 'Ekonominin parasallaşma derecesi kapasiteyi etkiler',
            'D': 'Kayıt dışı ekonominin büyümesi vergi kapasitesini artırır',
            'E': 'Dış ticaretin milli gelire oranı kapasiteyi etkiler',
        },
        'D',
        'Vergi kapasitesi; kişi başı gelir, sanayileşme, parasallaşma, dış ticaretin payı gibi ekonominin vergilendirilebilir potansiyelini gösteren etkenlere bağlıdır. **Kayıt dışı ekonomi** vergilendirilebilir tabanı idarenin erişiminden çıkardığı için fiilî vergi yükünü düşürür; kapasiteyi artıran bir etken değildir.',
        'Kamu maliyesi teorisi: vergi kapasitesi',
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
    print(f"1 paket / {len(PATCHES)} soru ('Kamu Gelirleri ve Giderleri' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
