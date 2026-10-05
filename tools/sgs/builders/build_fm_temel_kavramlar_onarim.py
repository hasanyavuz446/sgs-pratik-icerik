#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Muhasebenin Temel Kavramlari — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

FM cok adimli tur (hafif). Senaryo/kavram agirlikli 60 soru korundu. 10 mutlak ifadeli sik onarildi; cozumlerdeki harf atiflari (**X yanlistir**, '(A, C, D)') kaldirildi; oncul cevap yigilmasi (6'da 4 'I, II ve III') iki soru yeniden kurgulanarak giderildi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 1 Sira No'lu MSUGT - Muhasebenin Temel Kavramlari
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/finansal_muhasebe/muhasebenin_temel_kavramlari.json"
STYLE_REF = 'SGS Finansal Muhasebe (senaryo; sınav stiline kalibre)'
ONEK = "finmuh-temelkavram-gen-"


def patch(stem, options, answer, solution, ref="1 Sira No'lu MSUGT - Muhasebenin Temel Kavramlari"):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Mobilya imalatı yapan gerçek kişi işletmesinin sahibi, eşi adına kayıtlı bir dairenin 40.000 ₺ tutarındaki tapu harcını işletmenin banka hesabından ödemiş; ancak bu tutarı işletme gideri yazmayıp sahibin işletmeden çektiği değer olarak izlemiştir.\n\nBu uygulama öncelikle hangi temel kavramla açıklanır?',
        {
            'A': 'Süreklilik',
            'B': 'Maliyet Esası',
            'C': 'Kişilik',
            'D': 'Dönemsellik',
            'E': 'Tarafsızlık ve Belgelendirme',
        },
        'C',
        'İşletme, sahibinden ayrı ve bağımsız bir **kişilik** olarak ele alınır. Sahibin şahsi harcaması işletme gideri olamaz; sahibe çektirilen değer olarak izlenir. Bu, **Kişilik Kavramı**nın gereğidir.',
        "1 Sıra No'lu MSUGT - Muhasebenin Temel Kavramları (Kişilik)",
    ),
    # düzey 3
    '0002': patch(
        "2024 yılında 800.000 ₺'ye satın alınan bir arsanın, güncel piyasa değeri 2026 başında 1.400.000 ₺'ye çıkmış olmasına rağmen (yeniden değerleme/enflasyon düzeltmesi gibi özel düzenlemeler dışında) bilançoda hâlâ 800.000 ₺ üzerinden gösterilmesi hangi kavrama dayanır?",
        {
            'A': 'Önemlilik',
            'B': 'Süreklilik',
            'C': 'Dönemsellik',
            'D': 'İhtiyatlılık',
            'E': 'Maliyet Esası',
        },
        'E',
        '**Maliyet Esası Kavramı** gereği varlıklar edinme (maliyet) bedeliyle kaydedilir; sonradan oluşan piyasa değeri artışları, yeniden değerleme/enflasyon düzeltmesi gibi istisnalar dışında defter değerini kendiliğinden değiştirmez.',
        "1 Sıra No'lu MSUGT - Maliyet Esası",
    ),
    # düzey 2
    '0003': patch(
        'Muhasebe kayıtlarının, yönetimin sözlü beyanına değil; fatura, sözleşme, banka dekontu gibi objektif belgelere dayandırılması hangi temel kavramın gereğidir?',
        {
            'A': 'Parayla Ölçülme İlkesi',
            'B': 'Süreklilik ve Devamlılık İlkesi',
            'C': 'Tarafsızlık ve Belgelendirme',
            'D': 'Dönemsellik ve Tahakkuk',
            'E': 'İhtiyatlılık (Muhafazakârlık)',
        },
        'C',
        '**Tarafsızlık ve Belgelendirme Kavramı**, kayıtların gerçek durumu yansıtan, usulüne uygun düzenlenmiş objektif belgelere dayandırılmasını ve muhasebenin önyargısız (tarafsız) olmasını öngörür.',
        "1 Sıra No'lu MSUGT - Tarafsızlık ve Belgelendirme",
    ),
    # düzey 2
    '0004': patch(
        'Farklı ölçü birimleriyle (adet, kilogram, metre) izlenen stok kalemlerinin mali tablolarda ortak ölçü olan Türk Lirası cinsinden raporlanması hangi kavramla ilgilidir?',
        {
            'A': 'Parayla Ölçülme',
            'B': 'Maliyet Esası',
            'C': 'Özün Önceliği',
            'D': 'Sosyal Sorumluluk',
            'E': 'Tarafsızlık ve Belgelendirme',
        },
        'A',
        '**Parayla Ölçülme Kavramı**, işlemlerin ortak ölçü birimi olan ulusal para (₺) cinsinden ifade edilmesini öngörür; böylece farklı nitelikteki kalemler toplanabilir ve karşılaştırılabilir hâle gelir.',
        "1 Sıra No'lu MSUGT - Parayla Ölçülme",
    ),
    # düzey 2
    '0005': patch(
        "İşletmenin yurt dışından ithal ettiği makineyi, işlem tarihindeki döviz kuru üzerinden TL'ye çevirip edinme bedeliyle kaydetmesi öncelikle hangi iki kavramla birlikte açıklanır?",
        {
            'A': 'Tarafsızlık ve Belgelendirme ile Sosyal Sorumluluk',
            'B': 'Özün Önceliği ve Kişilik',
            'C': 'Önemlilik ve Tam Açıklama',
            'D': 'Süreklilik ve Dönemsellik',
            'E': 'Parayla Ölçülme ve Maliyet Esası',
        },
        'E',
        "İşlem tarihindeki kurla TL'ye çevirme **Parayla Ölçülme**, edinme (maliyet) bedeliyle kaydetme **Maliyet Esası** kavramının örneğidir; bu iki kavram burada birlikte uygulanır.",
        "1 Sıra No'lu MSUGT - Parayla Ölçülme ve Maliyet Esası",
    ),
    # düzey 2
    '0006': patch(
        'Net gerçekleşebilir değeri maliyetinin altına düşen stok için değer düşüklüğü karşılığı ayrılırken, aynı dönemde piyasa değeri artan başka bir stok için herhangi bir gelir/değer artışı kaydedilmemesi hangi kavramla açıklanır?',
        {
            'A': 'Dönemsellik',
            'B': 'İhtiyatlılık',
            'C': 'Tutarlılık',
            'D': 'Sosyal Sorumluluk',
            'E': 'Maliyet Esası',
        },
        'B',
        '**İhtiyatlılık Kavramı** simetrik değildir: muhtemel değer düşüşü (zarar) için karşılık ayrılır, ancak gerçekleşmemiş değer artışı (kâr) kaydedilmez. Bu asimetri tam da ihtiyatlılığın gereğidir.',
        "1 Sıra No'lu MSUGT - İhtiyatlılık; TMS 2",
    ),
    # düzey 3
    '0007': patch(
        'Aşağıdaki uygulamalardan hangileri Tam Açıklama Kavramı ile ilişkilendirilebilir?\n\nI. Kullanılan stok değerleme yönteminin mali tablo dipnotlarında belirtilmesi\n\nII. Kasadaki paranın itibari değeriyle kayıtlarda gösterilmesi\n\nIII. Bilanço tarihinden sonra ortaya çıkan ve mali tabloları etkileyebilecek önemli olayların açıklanması\n\nIV. İşletme sahibinin şahsi harcamalarının işletme gideri olarak yazılması',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'II ve IV',
        },
        'D',
        '**I ve III** Tam Açıklama kavramının gereğidir: kullanıcıların doğru karar vermesi için muhasebe politikaları ve bilanço sonrası önemli olaylar dipnotlarla açıklanır. **II** Parayla Ölçülme kavramıyla ilgilidir; **IV** ise **Kişilik Kavramı**na aykırı bir uygulamadır.',
        "1 Sıra No'lu MSUGT - Tam Açıklama; Kişilik",
    ),
    # düzey 3
    '0008': patch(
        'Aşağıdakilerden hangisi muhasebenin temel kavramlarından biri değildir?',
        {
            'A': 'Parayla Ölçülme İlkesi Kavramı',
            'B': 'Vergi kanunlarına mutlak uygunluk',
            'C': 'Sosyal Sorumluluk Kavramı',
            'D': 'Tarafsızlık ve Belgelendirme Kavramı',
            'E': 'İhtiyatlılık (Muhafazakârlık)',
        },
        'B',
        "'**Vergi kanunlarına mutlak uygunluk**' muhasebenin temel kavramlarından değildir. Kişilik, İhtiyatlılık, Özün Önceliği ve Dönemsellik MSUGT'deki temel kavramlar arasındadır.",
        "1 Sıra No'lu MSUGT - Temel kavramlar listesi",
    ),
    # düzey 2
    '0009': patch(
        'Aynı gerçek kişiye ait iki ayrı ticari işletmenin muhasebe kayıtlarının ve mali tablolarının birbirinden bağımsız olarak ayrı ayrı tutulması hangi kavramla açıklanır?',
        {
            'A': 'Kişilik',
            'B': 'Özün Önceliği',
            'C': 'Tutarlılık',
            'D': 'Parayla Ölçülme',
            'E': 'Süreklilik',
        },
        'A',
        '**Kişilik Kavramı** gereği her işletme, sahibinden ve diğer işletmelerden ayrı bağımsız bir birim olarak ele alınır; bu nedenle aynı kişiye ait işletmeler de ayrı ayrı muhasebeleştirilir.',
        "1 Sıra No'lu MSUGT - Kişilik",
    ),
    # düzey 2
    '0010': patch(
        "İşletme, kasım ayında 24 aylık bir kira gelirini peşin tahsil etmiştir. Bu gelirin yalnızca cari döneme düşen kısmının gelir yazılıp kalan kısmının 'Gelecek Aylara/Yıllara Ait Gelirler' hesabında bekletilmesi hangi kavramın gereğidir?",
        {
            'A': 'Maliyet Esası',
            'B': 'Özün Önceliği',
            'C': 'Parayla Ölçülme',
            'D': 'Sosyal Sorumluluk',
            'E': 'Dönemsellik',
        },
        'E',
        '**Dönemsellik Kavramı** gereği gelirler ait oldukları döneme kaydedilir. Peşin tahsil edilen gelirin gelecek dönemlere ait kısmı, o dönemlerin geliri olacağından bekletici hesaplarda (380/480) izlenir.',
        "1 Sıra No'lu MSUGT - Dönemsellik",
    ),
    # düzey 2
    '0011': patch(
        'Toplam varlıkları 80.000.000 ₺ olan bir işletme, yönetim kurulu başkanına 25.000 ₺ tutarında faizsiz borç vermiştir. Tutar işletme ölçeğine göre küçük olsa da işlemin ilişkili tarafla yapılması, kullanıcıların değerlendirmesini etkileyebilecek niteliktedir.\n\nBu işlemin yalnız tutarına bakılarak önemsiz sayılmaması hangi kavramla açıklanır?',
        {
            'A': 'Süreklilik',
            'B': 'Maliyet Esası',
            'C': 'Önemlilik',
            'D': 'Dönemsellik',
            'E': 'Parayla Ölçülme',
        },
        'C',
        'Önemlilik yalnız parasal büyüklüğe göre belirlenmez. İlişkili taraf işlemi, tutarı küçük olsa bile niteliği nedeniyle kullanıcı kararlarını etkileyebilir. Bu nedenle işlem **Önemlilik Kavramı** kapsamında değerlendirilir.',
        "1 Sıra No'lu MSUGT - Muhasebenin Temel Kavramları (Önemlilik)",
    ),
    # düzey 2
    '0012': patch(
        'Tutarlılık Kavramı ile ilgili aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Tutarlılık, gerçekleşmemiş kârların da erkenden gelir yazılmasını ve karşılıkların iptalini zorunlu kılan bir ilkedir.',
            'B': 'Tutarlılık gereği yöntemler her dönem değiştirilebilir; bu değişiklikler için ayrıca bir gerekçe aranmaz.',
            'C': 'Tutarlılık gelir tablosu hesapları için geçerlidir; bilanço kalemlerinin yöntemleri kapsam dışındadır.',
            'D': 'Tutarlılık, seçilen yöntemlerin gerekçe olsa da değiştirilemeyeceğini ve dipnot açıklaması gerekmediğini belirtir.',
            'E': 'Yöntemler kural olarak değiştirilmez; haklı bir neden varsa değiştirilebilir ve bu durum dipnotlarda açıklanır.',
        },
        'E',
        'Tutarlılık, yöntemlerin **kural olarak** dönemler arası değiştirilmemesini ister; ancak **haklı bir neden** varsa değişiklik yapılabilir ve etkisiyle birlikte **dipnotlarda açıklanır** (tam açıklama ile birlikte işler).',
        "1 Sıra No'lu MSUGT - Tutarlılık (istisnası)",
    ),
    # düzey 2
    '0013': patch(
        'Büyük ölçekli bir işletmenin, tutarı çok küçük olan kırtasiye malzemelerini stok kaydı yapıp izlemek yerine doğrudan gider yazması hangi kavrama dayanır?',
        {
            'A': 'Tam Açıklama',
            'B': 'Süreklilik',
            'C': 'Önemlilik',
            'D': 'Özün Önceliği',
            'E': 'Maliyet Esası',
        },
        'C',
        '**Önemlilik Kavramı**, tutar veya nitelik olarak önemsiz kalemlerin, kullanıcı kararlarını etkilemeyeceği için basitleştirilmiş biçimde (doğrudan gider) işlenebileceğini kabul eder.',
        "1 Sıra No'lu MSUGT - Önemlilik",
    ),
    # düzey 2
    '0014': patch(
        'Aralık ayına ait elektrik gideri belgeye bağlanmıştır. Yönetici dönem kârını yüksek göstermek için kaydın ocak ayına bırakılmasını istemesine rağmen muhasebe sorumlusu, kişisel hedeften etkilenmeden belge ve gerçekleşen hizmet dönemini esas almıştır.\n\nKayıtta yönetimin kâr hedefinden etkilenilmemesi öncelikle hangi kavramla ilgilidir?',
        {
            'A': 'Parayla Ölçülme',
            'B': 'Tarafsızlık ve Belgelendirme',
            'C': 'Kişilik',
            'D': 'Süreklilik',
            'E': 'Maliyet Esası',
        },
        'B',
        'Muhasebe kayıtları yönetimin dönem kârına ilişkin isteğine göre değil, gerçek durumu gösteren objektif belgelere göre yapılmalıdır. Bu tarafsız tutum **Tarafsızlık ve Belgelendirme Kavramı**nın gereğidir. Giderin aralık dönemine yazılması ayrıca dönemsellikle uyumludur.',
        "1 Sıra No'lu MSUGT - Muhasebenin Temel Kavramları (Tarafsızlık ve Belgelendirme)",
    ),
    # düzey 2
    '0015': patch(
        "İşletmenin aralık ayında peşin ödediği 12 aylık sigorta priminin, gelecek yıla ait kısmının '180 Gelecek Aylara Ait Giderler' hesabında izlenip ilgili aylarda gider yazılması hangi kavramın gereğidir?",
        {
            'A': 'Dönemsellik',
            'B': 'Kişilik',
            'C': 'Özün Önceliği',
            'D': 'Maliyet Esası',
            'E': 'İhtiyatlılık',
        },
        'A',
        "**Dönemsellik Kavramı** gereği giderler ait oldukları döneme yazılır. Peşin ödenen sigortanın gelecek döneme ait kısmı, o dönemin gideri olacağından '180 Gelecek Aylara Ait Giderler'de bekletilir.",
        "1 Sıra No'lu MSUGT - Dönemsellik",
    ),
    # düzey 2
    '0016': patch(
        'Muhasebe kayıtlarının; işletme yönetiminin kişisel tahmin ve isteklerine göre değil, gerçek durumu yansıtan objektif belgelere dayandırılması gerektiğini ifade eden kavram aşağıdakilerden hangisidir?',
        {
            'A': 'Maliyet Esası ve Edinme Bedeli',
            'B': 'Sosyal Sorumluluk İlkesi',
            'C': 'Tarafsızlık ve Belgelendirme',
            'D': 'Özün Önceliği Kavramı',
            'E': 'Süreklilik ve Devamlılık İlkesi',
        },
        'C',
        '**Tarafsızlık ve Belgelendirme Kavramı**, kayıtların önyargısız (tarafsız) ve usulüne uygun düzenlenmiş objektif belgelere dayandırılmasını öngörür; kişisel tahmin ve istekler esas alınamaz.',
        "1 Sıra No'lu MSUGT - Tarafsızlık ve Belgelendirme",
    ),
    # düzey 2
    '0017': patch(
        'İhtiyatlılık Kavramı ile ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Gerçekleşmesi muhtemel gelirler de kayıtlara alınır',
            'B': 'Muhtemel giderler için karşılık ayrılır',
            'C': 'İşletme ileride karşılaşabileceği risklere karşı temkinli davranır',
            'D': 'Kavram, gizli yedek ayrılmasına imkân vermez',
            'E': 'Muhtemel zararlar dönem sonucuna yansıtılır',
        },
        'A',
        "1 Sıra No'lu MSUGT'ye göre ihtiyatlılık kavramı, işletmenin karşılaşabileceği risklere karşı temkinli davranmasını; muhtemel gider ve zararlar için karşılık ayrılmasını, gerçekleşmemiş gelirlerin ise kaydedilmemesini gerektirir. Kavram gizli yedek veya gereğinden fazla karşılık ayrılmasına imkân vermez.",
        "1 Sıra No'lu MSUGT - İhtiyatlılık",
    ),
    # düzey 2
    '0018': patch(
        'Bir bankanın, kredi vereceği işletmenin mali tablolarına güvenebilmesi; bu tabloların tarafsız, belgeye dayalı ve gerçeğe uygun biçimde hazırlanmış olmasına bağlıdır. Bu güvenin sağlanmasında muhasebenin hangi temel işlevi öne çıkar?',
        {
            'A': 'Muhasebenin, ürünlerin tanıtımını ve satışını artırmaya yönelik pazarlama destek işlevi',
            'B': 'Muhasebenin, çalışan seçimi ve performans değerlendirmesine yönelik insan kaynakları işlevi',
            'C': 'Muhasebenin, ödenecek verginin hesaplanmasına yönelik teknik kayıt tutma işlevi',
            'D': 'Muhasebenin, ilgili taraflara güvenilir ve tarafsız bilgi sunma (sosyal sorumluluk) işlevi',
            'E': 'Muhasebenin, üretim miktarını ve stok seviyelerini planlamaya yönelik operasyonel işlevi',
        },
        'D',
        'Muhasebe, işletme dışındaki taraflara da (banka, yatırımcı, devlet) **güvenilir ve tarafsız bilgi** sunar; bu, **Sosyal Sorumluluk** kavramının bir yansımasıdır ve dış kullanıcıların karar almasını sağlar.',
        "1 Sıra No'lu MSUGT - Sosyal Sorumluluk",
    ),
    # düzey 3
    '0019': patch(
        'Aşağıdaki kavram–örnek eşleştirmelerinden hangisi yanlıştır?',
        {
            'A': 'Maliyet Esası → Varlığın edinme bedeliyle kaydedilmesi',
            'B': 'Dönemsellik → Peşin ödenen giderin gelecek döneme ait kısmının aktifleştirilmesi',
            'C': 'Kişilik → İşletme sahibinin şahsi giderinin işletme gideri yazılması',
            'D': 'İhtiyatlılık → Şüpheli alacak için karşılık ayrılması',
            'E': 'Özün Önceliği → Finansal kiralamada varlığın kiracıda gösterilmesi',
        },
        'C',
        'Kişilik Kavramı, sahibin şahsi giderinin işletme gideri **yazılmamasını** gerektirir; sahibin gideri işletme gideri sayılamaz. Diğer eşleştirmeler doğrudur.',
        "1 Sıra No'lu MSUGT - Temel Kavramlar",
    ),
    # düzey 2
    '0020': patch(
        'Muhasebenin temel kavramlarının belirlenmesinin temel amacı aşağıdakilerden hangisidir?',
        {
            'A': 'Tekdüzen hesap planını yürürlükten kaldırıp her işletmeye kendi planını kurma serbestisi vermek',
            'B': 'İşletmelerin dönem kârını olduğundan düşük göstererek daha az vergi ödemesine imkân tanımak',
            'C': 'İşletmeleri defter ve kayıt tutma yükümlülüğünden bütünüyle kurtararak iş yükünü azaltmak',
            'D': 'Vergi dairesinin denetim işini kolaylaştırmak; diğer kullanıcıları kapsam dışı bırakmak',
            'E': 'Mali tabloların gerçeğe uygun, güvenilir, tutarlı ve karşılaştırılabilir olmasını sağlamak',
        },
        'E',
        'Temel kavramlar, muhasebe bilgisinin ve mali tabloların **gerçeğe uygun, güvenilir, tutarlı ve karşılaştırılabilir** biçimde üretilmesini sağlamak için belirlenmiştir; tüm kullanıcıların doğru bilgiye ulaşmasını amaçlar.',
        "1 Sıra No'lu MSUGT - Temel kavramların amacı",
    ),
    # düzey 3
    '0021': patch(
        "Aşağıdaki uygulamalardan hangileri Dönemsellik Kavramı ile ilişkilendirilebilir?\n\nI. Ekimde peşin ödenen 12 aylık kasko priminin yalnızca cari döneme düşen kısmının gider yazılması\n\nII. Tahakkuk etmiş ancak henüz tahsil edilmemiş kira gelirinin döneme gelir kaydedilmesi\n\nIII. Gelecek yıla ait peşin tahsil edilen kira gelirinin '380 Gelecek Aylara Ait Gelirler' hesabında izlenmesi\n\nIV. Duran varlığın maliyet bedeli üzerinden kayda alınması",
        {
            'A': 'I, II ve III',
            'B': 'II ve IV',
            'C': 'I, II, III ve IV',
            'D': 'Yalnız I',
            'E': 'I ve IV',
        },
        'A',
        "**I, II ve III** dönemsellik (ve tahakkuk) ile ilgilidir: gelir ve giderler ait oldukları döneme yazılır; ait olmayan kısımlar 180/280 ya da 380/480'de bekletilir. **IV** ise **Maliyet Esası** kavramıyla ilgilidir; dönemsellikle doğrudan ilişkili değildir.",
        "1 Sıra No'lu MSUGT - Dönemsellik",
    ),
    # düzey 2
    '0022': patch(
        "Toplam aktifi 40.000.000 ₺ olan bir işletmenin, 90 ₺'ye aldığı bir hesap makinesini amortismana tabi tutmak yerine doğrudan gider yazması hangi temel kavramla açıklanır?",
        {
            'A': 'Tam Açıklama',
            'B': 'Tarafsızlık ve Belgelendirme',
            'C': 'Maliyet Esası',
            'D': 'Önemlilik',
            'E': 'Süreklilik',
        },
        'D',
        '**Önemlilik Kavramı**, bir bilginin gösterilmemesinin ya da farklı gösterilmesinin kullanıcı kararlarını etkileyip etkilemediğine bakar. İşletmenin ölçeği karşısında ihmal edilebilir tutarlar, kesin ilkelere birebir uyulmadan basitleştirilmiş biçimde işlem görebilir.',
        "1 Sıra No'lu MSUGT - Önemlilik",
    ),
    # düzey 2
    '0023': patch(
        'Bir işletmenin, stok değerleme yöntemini haklı bir neden olmaksızın her yıl değiştirerek bir yıl FIFO, ertesi yıl ağırlıklı ortalama uygulaması, mali tabloların dönemler arası karşılaştırılabilirliğini bozar.\n\nBu durum öncelikle hangi temel kavrama aykırıdır?',
        {
            'A': 'Önemlilik',
            'B': 'Tutarlılık',
            'C': 'Dönemsellik',
            'D': 'Maliyet Esası',
            'E': 'İhtiyatlılık',
        },
        'B',
        '**Tutarlılık Kavramı**, seçilen muhasebe politika ve yöntemlerinin dönemler arası **değiştirilmeden** uygulanmasını ister; değişiklik ancak haklı bir nedene dayanır ve dipnotta açıklanırsa yapılabilir. Gerekçesiz yöntem değişikliği tutarlılığa aykırıdır.',
        "1 Sıra No'lu MSUGT - Tutarlılık",
    ),
    # düzey 2
    '0024': patch(
        'Muhasebenin; işletme sahip ve ortaklarının yanı sıra kredi verenler, çalışanlar, devlet ve kamuoyunun da güvenilir bilgiye ulaşmasını gözetecek biçimde, toplum çıkarlarına duyarlı yürütülmesi hangi kavramla ilişkilidir?',
        {
            'A': 'Sosyal Sorumluluk',
            'B': 'Tam Açıklama',
            'C': 'Kişilik',
            'D': 'Önemlilik',
            'E': 'Tarafsızlık ve Belgelendirme',
        },
        'A',
        '**Sosyal Sorumluluk Kavramı**, muhasebenin işlevini yerine getirirken belirli kişi/grupların değil, toplumun tüm kesimlerinin çıkarlarını gözetmesini ve gerçeğe uygun, tarafsız bilgi üretmesini ifade eder.',
        "1 Sıra No'lu MSUGT - Sosyal Sorumluluk",
    ),
    # düzey 2
    '0025': patch(
        'Aşağıdaki durumlardan hangisi Kişilik Kavramına aykırıdır?',
        {
            'A': 'İşletme sahibinin şahsi otomobilinin masraflarının işletme gideri yazılması',
            'B': 'İşletmenin ticari alacaklarının bilançoda gösterilmesi',
            'C': 'İşletmenin ortaklarına dağıtacağı kâr payının kayıtlara alınması',
            'D': 'İşletmenin banka mevduatının hazır değerlerde izlenmesi',
            'E': 'İşletme adına düzenlenen faturaların kaydedilmesi',
        },
        'A',
        'İşletme, sahibinden ayrı bir **kişilik**tir; sahibin şahsi otomobil masrafı işletme gideri olamaz. Bu nedenle **A**, Kişilik Kavramına aykırıdır. Diğer şıklar işletmenin kendi işlemleridir ve kavrama uygundur.',
        "1 Sıra No'lu MSUGT - Kişilik",
    ),
    # düzey 3
    '0026': patch(
        'Muhasebenin temel kavramları ile ilgili aşağıdaki eşleştirmelerden hangisi yanlıştır?',
        {
            'A': 'Tutarlılık → Seçilen yöntemlerin haklı neden olmadıkça dönemler arası değiştirilmemesi',
            'B': 'Süreklilik → İşletmenin faaliyetlerini öngörülebilir gelecekte sürdüreceği varsayımı',
            'C': 'Maliyet Esası → Varlıkların edinme bedeliyle kaydedilmesi',
            'D': 'Tam Açıklama → Mali tabloların yeterli ve anlaşılır bilgi içermesi',
            'E': 'İhtiyatlılık → Gerçekleşmemiş kârların da erkenden gelir yazılması',
        },
        'E',
        'İhtiyatlılık, gerçekleşmemiş kârların gelir yazılmamasını gerektirir; erkenden gelir yazmak ihtiyatlılığa aykırıdır. Diğer eşleştirmeler doğrudur.',
        "1 Sıra No'lu MSUGT - Temel Kavramlar",
    ),
    # düzey 2
    '0027': patch(
        'Bir yazılım işletmesinin son derece deneyimli ve nitelikli mühendis kadrosu işletmeye önemli bir rekabet üstünlüğü sağlamasına rağmen, bu kadro bilançoda bir varlık olarak gösterilememektedir.\n\nBu durum öncelikle hangi temel kavramla açıklanır?',
        {
            'A': 'Özün Önceliği',
            'B': 'Tam Açıklama',
            'C': 'Süreklilik',
            'D': 'Parayla Ölçülme',
            'E': 'İhtiyatlılık',
        },
        'D',
        '**Parayla Ölçülme Kavramı** gereği yalnızca ortak ölçü birimi olan para ile güvenilir biçimde ölçülebilen işlem ve olaylar kaydedilir. Nitelikli insan kaynağı değerli olsa da parayla objektif biçimde ölçülemediğinden bilançoya varlık olarak alınmaz.',
        "1 Sıra No'lu MSUGT - Parayla Ölçülme",
    ),
    # düzey 2
    '0028': patch(
        'Muhasebenin; yalnızca işletme yöneticilerinin değil, yatırımcılar, kredi verenler, çalışanlar ve devlet gibi tüm ilgili kesimlerin gereksinim duyduğu güvenilir bilgiyi tarafsız biçimde üretmesi gerektiği hangi kavramla ifade edilir?',
        {
            'A': 'Kişilik',
            'B': 'Sosyal Sorumluluk',
            'C': 'Maliyet Esası',
            'D': 'Tutarlılık',
            'E': 'Dönemsellik',
        },
        'B',
        '**Sosyal Sorumluluk Kavramı**, muhasebenin belirli bir kesimin değil, toplumun tüm ilgili kesimlerinin çıkarlarını gözeterek gerçeğe uygun ve tarafsız bilgi üretmesini ifade eder.',
        "1 Sıra No'lu MSUGT - Sosyal Sorumluluk",
    ),
    # düzey 2
    '0029': patch(
        'İşletmenin maddi duran varlıklarına, ekonomik ömürleri boyunca faaliyetlerini sürdüreceği varsayımıyla amortisman ayırması hangi iki kavramla en yakından ilişkilidir?',
        {
            'A': 'Süreklilik ve Dönemsellik',
            'B': 'Kişilik ve Sosyal Sorumluluk',
            'C': 'Özün Önceliği ve Tutarlılık',
            'D': 'Önemlilik ve Tam Açıklama',
            'E': 'Parayla Ölçülme ve Tarafsızlık',
        },
        'A',
        'Amortisman; işletmenin faaliyetini sürdüreceği (**Süreklilik**) varsayımıyla, varlığın maliyetinin yararlanılan **dönemlere** (Dönemsellik) dağıtılmasıdır. Bu iki kavram amortismanda birlikte işler.',
        "1 Sıra No'lu MSUGT - Süreklilik ve Dönemsellik",
    ),
    # düzey 2
    '0030': patch(
        'İşletmenin kullandığı bir kredi için döneme ait olup henüz ödenmemiş faiz giderinin, ödeme gelecek dönemde yapılacak olsa bile cari döneme gider olarak kaydedilmesi hangi kavramla açıklanır?',
        {
            'A': 'Maliyet Esası ve Edinme Bedeli',
            'B': 'Özün Önceliği Kavramı',
            'C': 'Dönemsellik (tahakkuk esası)',
            'D': 'Parayla Ölçülme İlkesi',
            'E': 'Tam Açıklama ve Dipnotlar',
        },
        'C',
        '**Dönemsellik (tahakkuk esası)** gereği giderler, nakit ödemeden bağımsız olarak ait oldukları dönemde kaydedilir. Döneme ait tahakkuk etmiş faiz, ödeme sonraki dönemde olsa da cari döneme gider yazılır.',
        "1 Sıra No'lu MSUGT - Dönemsellik/tahakkuk",
    ),
    # düzey 2
    '0031': patch(
        'Bir hizmet giderine ait fatura henüz işletmeye ulaşmamıştır. Muhasebe sorumlusu, yalnız yöneticinin sözlü beyanıyla kayıt yapmak yerine imzalı sözleşmeyi, hizmet kabul tutanağını, banka ödeme kaydını ve karşı taraf teyidini inceleyerek işlemi doğrulamıştır.\n\nBu yaklaşım öncelikle hangi kavramın gereğidir?',
        {
            'A': 'Tam Açıklama',
            'B': 'Tarafsızlık ve Belgelendirme',
            'C': 'Maliyet Esası',
            'D': 'İhtiyatlılık',
            'E': 'Tutarlılık',
        },
        'B',
        'Bir işlemin kanıtı yalnız faturadan ibaret değildir; sözleşme, kabul tutanağı, banka kaydı ve teyit gibi objektif belgeler de işlemi destekleyebilir. Kaydın kişisel beyan yerine doğrulanabilir kanıta dayanması **Tarafsızlık ve Belgelendirme Kavramı**nın gereğidir.',
        "1 Sıra No'lu MSUGT - Muhasebenin Temel Kavramları (Tarafsızlık ve Belgelendirme)",
    ),
    # düzey 2
    '0032': patch(
        'İşletmenin uyguladığı önemli muhasebe politikalarının (stok değerleme yöntemi, amortisman yöntemi vb.) mali tablo kullanıcılarını bilgilendirmek amacıyla dipnotlarda açıklanması hangi kavramın gereğidir?',
        {
            'A': 'Önemlilik',
            'B': 'Kişilik',
            'C': 'Maliyet Esası',
            'D': 'Tam Açıklama',
            'E': 'İhtiyatlılık',
        },
        'D',
        '**Tam Açıklama Kavramı**, mali tabloların kullanıcıların doğru karar vermesine yetecek nitelikte bilgi içermesini gerektirir; uygulanan önemli muhasebe politikaları bu nedenle dipnotlarda açıklanır.',
        "1 Sıra No'lu MSUGT - Tam Açıklama",
    ),
    # düzey 2
    '0033': patch(
        'Özün Önceliği Kavramı ile ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İşlemler hukuki biçimden çok ekonomik özüne göre kaydedilir',
            'B': "Kavram, MSUGT'deki temel muhasebe kavramlarından biridir",
            'C': 'Muhasebeleştirmede ekonomik öz yerine hukuki biçim esas alınır',
            'D': 'Biçim ile öz ayrıştığında kayıt ekonomik öze göre yapılır',
            'E': 'Kavram, gerçeğe uygun sunumu desteklemeye yöneliktir',
        },
        'C',
        "1 Sıra No'lu MSUGT'ye göre özün önceliği kavramı, işlemlerin muhasebeye yansıtılmasında ve değerlemede biçimden çok özün esas alınmasını ifade eder; böylece mali tablolar gerçeğe uygun bilgi sunar.",
        "1 Sıra No'lu MSUGT - Özün Önceliği",
    ),
    # düzey 2
    '0034': patch(
        'Bir üretim işletmesinin çevreyi eski hâline getirme yükümlülüğü finansal durumunu etkileyebilecek düzeydedir. İşletme sahibi bu bilginin gizlenmesini istemiş; muhasebe sorumlusu ise yatırımcılar, çalışanlar, kredi verenler, devlet ve kamuoyunun güvenilir bilgi ihtiyacını gözetmiştir.\n\nYükümlülüğün nasıl ölçüleceğinden bağımsız olarak, bütün ilgili kesimlerin çıkarının gözetilmesi hangi kavramdır?',
        {
            'A': 'Maliyet Esası',
            'B': 'Tutarlılık',
            'C': 'Kişilik',
            'D': 'Sosyal Sorumluluk',
            'E': 'Özün Önceliği',
        },
        'D',
        'Muhasebenin bilgi üretirken yalnız işletme sahibini değil, işletmeyle ilgili bütün kesimleri ve kamu yararını gözetmesi **Sosyal Sorumluluk Kavramı**dır. Soru yükümlülüğün ölçümünü değil, bilgi kullanıcılarına karşı sorumluluğu ölçmektedir.',
        "1 Sıra No'lu MSUGT - Muhasebenin Temel Kavramları (Sosyal Sorumluluk)",
    ),
    # düzey 3
    '0035': patch(
        'Aşağıdaki durumlardan hangileri Dönemsellik Kavramı ile ilgilidir?\n\nI. Peşin ödenen kiranın gelecek döneme ait kısmının aktifleştirilmesi\n\nII. Dönem sonunda tahakkuk etmiş faiz gelirinin döneme yansıtılması\n\nIII. Stokların maliyet bedeliyle kayda alınması\n\nIV. İşletmenin sahibinden ayrı bir birim sayılması',
        {
            'A': 'I, II ve III',
            'B': 'I ve IV',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'I ve II',
        },
        'E',
        '**I ve II** dönemsellik ile ilgilidir: gelir ve giderler ait oldukları döneme yazılır. **III** **Maliyet Esası**, **IV** ise **Kişilik Kavramı**yla ilgilidir.',
        "1 Sıra No'lu MSUGT - Dönemsellik",
    ),
    # düzey 2
    '0036': patch(
        'Tutarlılık Kavramının mali tablolar açısından sağladığı temel yarar aşağıdakilerden hangisidir?',
        {
            'A': 'Varlıkların her dönem güncel piyasa değeriyle yeniden gösterilmesini sağlaması',
            'B': 'İşletme varlıklarının sahibin kişisel varlıklarından ayrı tutulmasını sağlaması',
            'C': 'Mali tabloların dönemler arasında karşılaştırılabilir olmasını sağlaması',
            'D': 'Gerçekleşmemiş kâr ve değer artışlarının erkenden gelir yazılmasını sağlaması',
            'E': 'İşletmenin ödeyeceği vergi matrahını yasal sınırların altına düşürmesi',
        },
        'C',
        'Aynı muhasebe yöntemlerinin dönemler arasında sürdürülmesi (**Tutarlılık**), mali tabloların **karşılaştırılabilir** olmasını sağlar; böylece dönemler arası değerlendirme sağlıklı yapılır.',
        "1 Sıra No'lu MSUGT - Tutarlılık",
    ),
    # düzey 2
    '0037': patch(
        'Önemlilik Kavramının değerlendirilmesinde esas alınan temel ölçüt aşağıdakilerden hangisidir?',
        {
            'A': 'İşletmenin kaç ortağı bulunduğu ve bu ortakların sermaye içindeki paylarının yüzde olarak dağılımı',
            'B': 'Bir bilginin gösterilmemesinin ya da yanlış gösterilmesinin, mali tablo kullanıcılarının kararlarını etkileyip etkilemeyeceği',
            'C': 'Yevmiye kaydının hangi renk kalemle ve defterin kaçıncı sayfasına yazıldığına ilişkin biçimsel ayrıntı',
            'D': 'İşleme ilişkin tahsilat veya ödemenin hangi banka şubesi aracılığıyla gerçekleştirilmiş olduğu bilgisi',
            'E': 'Bir işlemin kaydı için düzenlenen belgelerin sayısının ve bu belgelerin toplam sayfa adedinin defterlerde ne kadar yer kapladığı',
        },
        'B',
        '**Önemlilik**, bir bilginin gösterilmemesinin ya da hatalı gösterilmesinin **kullanıcı kararlarını etkileyip etkilemeyeceğine** bakar. Etkileyecekse önemlidir ve gösterilmelidir; etkilemeyecek kadar küçükse basitleştirme yapılabilir.',
        "1 Sıra No'lu MSUGT - Önemlilik",
    ),
    # düzey 2
    '0038': patch(
        'Bir perakendecinin deposunda, satılıncaya kadar mülkiyeti ve başlıca riskleri tedarikçide kalan konsinye mallar bulunmaktadır. Mallar fiziksel olarak depoda olsa da perakendeci bunları kendi stoku olarak kaydetmemiştir.\n\nBu uygulama hangi kavrama dayanır?',
        {
            'A': 'Özün Önceliği',
            'B': 'Maliyet Esası',
            'C': 'Dönemsellik',
            'D': 'Kişilik',
            'E': 'Önemlilik',
        },
        'A',
        'Malın işletmenin deposunda bulunması tek başına ekonomik sahipliği göstermez. Mülkiyet ve başlıca riskler tedarikçide kaldığından, işlemin fiziksel görünümü yerine ekonomik özü esas alınır. Bu, **Özün Önceliği Kavramı**dır.',
        "1 Sıra No'lu MSUGT - Muhasebenin Temel Kavramları (Özün Önceliği)",
    ),
    # düzey 2
    '0039': patch(
        'İşletme, hâkim ortağına ait bir taşınmazı piyasa koşullarından önemli ölçüde farklı bir bedelle kiralamıştır. İşlem yasal defterlere kaydedilmiş; kullanıcıların işlemin niteliğini değerlendirebilmesi için ilişkili taraf, bedel ve temel koşullar dipnotlarda ayrıca açıklanmıştır.\n\nDipnot açıklaması öncelikle hangi kavramın gereğidir?',
        {
            'A': 'Kişilik',
            'B': 'Tam Açıklama',
            'C': 'Parayla Ölçülme',
            'D': 'Süreklilik',
            'E': 'Maliyet Esası',
        },
        'B',
        'Kayıtlı tutar tek başına, ilişkili tarafla yapılan işlemin kullanıcı açısından taşıdığı anlamı göstermeyebilir. İşlemin tarafı ve koşullarının dipnotta sunulması, kullanıcıya yeterli bilgi verilmesini amaçlayan **Tam Açıklama Kavramı**nın gereğidir.',
        "1 Sıra No'lu MSUGT - Muhasebenin Temel Kavramları (Tam Açıklama)",
    ),
    # düzey 3
    '0040': patch(
        'Aşağıdakilerden hangisi muhasebenin temel kavramlarından biri değildir?',
        {
            'A': 'Gizlilik',
            'B': 'Tutarlılık',
            'C': 'Özün Önceliği',
            'D': 'Tam Açıklama',
            'E': 'Önemlilik',
        },
        'A',
        "'**Gizlilik**' MSUGT'de sayılan muhasebe temel kavramlarından biri değildir. Tam Açıklama, Özün Önceliği, Tutarlılık ve Önemlilik ise temel kavramlar arasındadır.",
        "1 Sıra No'lu MSUGT - Temel kavramlar listesi",
    ),
    # düzey 2
    '0041': patch(
        'Bir işletmenin maddi duran varlıklarını tasfiye (hurda) değeriyle değil, faaliyetine devam edeceği varsayımıyla maliyet ve amortisman esasına göre değerlemesi hangi temel kavramın gereğidir?',
        {
            'A': 'Özün Önceliği',
            'B': 'Süreklilik',
            'C': 'Dönemsellik',
            'D': 'Parayla Ölçülme',
            'E': 'Önemlilik',
        },
        'B',
        'İşletmenin faaliyetlerini öngörülebilir gelecekte sürdüreceği varsayımı **Süreklilik Kavramı**dır. Bu nedenle varlıklar tasfiye değeriyle değil, işletmenin devamlılığına uygun ölçütlerle (maliyet, amortisman) değerlenir.',
        "1 Sıra No'lu MSUGT - Süreklilik (İşletmenin Sürekliliği)",
    ),
    # düzey 3
    '0042': patch(
        'İhtiyatlılık (Muhafazakârlık) Kavramı ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Gerçekleşmemiş gelirler ve kârlar kayda alınmaz.',
            'B': 'Muhtemel giderler ve zararlar için karşılık ayrılır.',
            'C': 'Şüpheli hâle gelen alacaklar için karşılık ayrılır.',
            'D': 'Stokun net gerçekleşebilir değeri maliyetin altına düşerse değer düşüklüğü karşılığı ayrılır.',
            'E': 'Duran varlığın piyasa değerindeki artış, gerçekleşmese de gelir olarak kaydedilir.',
        },
        'E',
        'İhtiyatlılık **simetrik değildir**: muhtemel gider ve zararlar için (şüpheli alacak, stok değer düşüklüğü dâhil) karşılık ayrılır, ama **gerçekleşmemiş** gelir ve değer artışları kaydedilmez. Bu nedenle duran varlığın gerçekleşmemiş değer artışının gelir yazılması ihtiyatlılığa aykırıdır.',
        "1 Sıra No'lu MSUGT - İhtiyatlılık",
    ),
    # düzey 2
    '0043': patch(
        'Bir finansal kiralama (leasing) sözleşmesi hukuken kiracıya mülkiyet tanımasa da, kiralanan varlığın risk ve getirilerinin büyük ölçüde kiracıya geçmesi nedeniyle varlığın kiracının aktifinde izlenmesi hangi kavrama dayanır?',
        {
            'A': 'Kişilik',
            'B': 'Süreklilik',
            'C': 'Tarafsızlık ve Belgelendirme',
            'D': 'Özün Önceliği',
            'E': 'Tam Açıklama',
        },
        'D',
        '**Özün Önceliği Kavramı**, işlemlerin muhasebeleştirilmesinde hukuki biçimden çok **ekonomik özün** esas alınmasını gerektirir. Mülkiyet devri olmasa da risk-getiri kiracıya geçtiğinden varlık kiracıda izlenir.',
        "1 Sıra No'lu MSUGT - Özün Önceliği; TMS/TFRS",
    ),
    # düzey 2
    '0044': patch(
        'İşletme aleyhine açılmış, sonucu belirsiz bir davanın; henüz kesinleşmediği için bilançoya yükümlülük yazılmasa da mali tablo dipnotlarında açıklanması hangi temel kavramla ilgilidir?',
        {
            'A': 'İhtiyatlılık',
            'B': 'Kişilik',
            'C': 'Tam Açıklama',
            'D': 'Önemlilik',
            'E': 'Özün Önceliği',
        },
        'C',
        '**Tam Açıklama Kavramı**, mali tabloların kullanıcıların doğru karar vermesine yetecek nitelikte açık ve anlaşılır bilgi içermesini gerektirir. Kesinleşmemiş ama bilgilendirici hususlar **dipnotlarla** açıklanır.',
        "1 Sıra No'lu MSUGT - Tam Açıklama",
    ),
    # düzey 2
    '0045': patch(
        "'Bir işletmenin ömrünün sınırsız kabul edilmesi' ile 'bu sınırsız ömrün belirli dönemlere bölünerek her dönemin sonucunun ayrı saptanması' varsayımları sırasıyla hangi kavramlara karşılık gelir?",
        {
            'A': 'Süreklilik – Dönemsellik',
            'B': 'Dönemsellik – Süreklilik',
            'C': 'Süreklilik – Tutarlılık',
            'D': 'Kişilik – Dönemsellik',
            'E': 'Parayla Ölçülme – Dönemsellik',
        },
        'A',
        'İşletmenin sınırsız ömrü **Süreklilik**; bu ömrün dönemlere bölünüp her dönemin sonucunun bağımsız saptanması **Dönemsellik** kavramıdır. İki kavram birbirini tamamlar: süreklilik olmasa dönemselliğe gerek kalmazdı.',
        "1 Sıra No'lu MSUGT - Süreklilik ve Dönemsellik",
    ),
    # düzey 3
    '0046': patch(
        'İşletme, üretimde kullandığı makineler için gelecekte katlanacağı büyük bakım-onarım harcamalarını, henüz gerçekleşmemiş ve belgeye bağlanmamışken erkenden gider yazmak istemektedir. Bir muhasebe uzmanı bunun doğru olmayacağını belirtmiştir.\n\nBu uyarı öncelikle hangi kavramların gereğidir?\n\nI. Sosyal Sorumluluk\n\nII. Dönemsellik\n\nIII. Tarafsızlık ve Belgelendirme',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız III',
            'C': 'I ve II',
            'D': 'Yalnız I',
            'E': 'II ve III',
        },
        'E',
        'Henüz **gerçekleşmemiş ve belgeye dayanmayan** bir harcamanın erkenden gider yazılamaması; giderin ait olduğu dönemde (**Dönemsellik**) ve objektif belgeye dayanarak (**Tarafsızlık ve Belgelendirme**) kaydedilmesi gerektiğindendir. I bu durumla doğrudan ilgili değildir.',
        "1 Sıra No'lu MSUGT - Dönemsellik; Tarafsızlık ve Belgelendirme",
    ),
    # düzey 2
    '0047': patch(
        'Muhasebenin temel kavramları öncelikle aşağıdaki düzenlemelerden hangisinde yer almaktadır?',
        {
            'A': "Gelir Vergisi Kanunu'nun ticari kazanç maddeleri",
            'B': "Kurumlar Vergisi Kanunu'nun istisna hükümleri",
            'C': "Türk Ticaret Kanunu'nun anonim şirket hükümleri",
            'D': "1 Sıra No'lu Muhasebe Sistemi Uygulama Genel Tebliği (MSUGT)",
            'E': "Vergi Usul Kanunu'nun değerleme ölçülerine ilişkin hükümleri",
        },
        'D',
        "Muhasebenin temel kavramları, **1 Sıra No'lu Muhasebe Sistemi Uygulama Genel Tebliği (MSUGT)** ile düzenlenmiştir; muhasebe uygulamalarının dayandığı temel ilkeleri oluşturur.",
        "1 Sıra No'lu MSUGT - Temel kavramların kaynağı",
    ),
    # düzey 2
    '0048': patch(
        'İşletme yönetimi, kredi başvurusunda daha güçlü görünmek için dönem giderlerinin bir bölümünün gelecek döneme aktarılmasını istemektedir. Muhasebe sorumlusu, yalnız işletme sahibinin çıkarını değil kredi verenler ve diğer bilgi kullanıcılarını da gözeterek bu talebi reddetmiştir.\n\nBu tutum öncelikle hangi kavramın gereğidir?',
        {
            'A': 'Parayla Ölçülme',
            'B': 'Sosyal Sorumluluk',
            'C': 'Süreklilik',
            'D': 'Maliyet Esası',
            'E': 'Kişilik',
        },
        'B',
        'Muhasebe yalnız işletme sahibinin değil, kredi verenler dâhil bütün bilgi kullanıcılarının çıkarını gözeterek güvenilir bilgi üretmelidir. Kârı güçlü göstermek amacıyla gideri ertelemeyi reddetmek **Sosyal Sorumluluk Kavramı**nın gereğidir.',
        "1 Sıra No'lu MSUGT - Muhasebenin Temel Kavramları (Sosyal Sorumluluk)",
    ),
    # düzey 2
    '0049': patch(
        'Tasfiyeye girmesine karar verilen bir işletmede, varlıkların artık maliyet ve amortisman esasına göre değil, elden çıkarılabilecekleri (tasfiye) değerine göre değerlenmesi hangi kavramın geçerliliğini yitirmesiyle ilgilidir?',
        {
            'A': 'Önemlilik',
            'B': 'Süreklilik',
            'C': 'Tutarlılık',
            'D': 'Tam Açıklama',
            'E': 'Kişilik',
        },
        'B',
        'Değerlemenin maliyet/amortisman yerine tasfiye değeriyle yapılması, işletmenin faaliyetini sürdüreceği varsayımının (yani **Süreklilik Kavramı**nın) artık geçerli olmamasından kaynaklanır.',
        "1 Sıra No'lu MSUGT - Süreklilik",
    ),
    # düzey 2
    '0050': patch(
        'Bir işletmenin sahip olduğu güçlü marka itibarı ve yüksek müşteri memnuniyeti, işletmeye değer katmasına rağmen parayla objektif biçimde ölçülemediği için bilançoda bir varlık olarak gösterilmez. Bu durum hangi kavramla açıklanır?',
        {
            'A': 'İhtiyatlılık',
            'B': 'Sosyal Sorumluluk',
            'C': 'Dönemsellik',
            'D': 'Parayla Ölçülme',
            'E': 'Tutarlılık',
        },
        'D',
        '**Parayla Ölçülme Kavramı** gereği yalnızca para ile güvenilir biçimde ölçülebilen unsurlar kayda alınır. İtibar ve müşteri memnuniyeti değerli olsa da objektif biçimde parayla ölçülemediğinden bilançoya alınmaz.',
        "1 Sıra No'lu MSUGT - Parayla Ölçülme",
    ),
    # düzey 2
    '0051': patch(
        'İşletme, stok maliyetlerini daha güvenilir sunan yeni bir yönteme geçmek için haklı bir gerekçe belirlemiş; değişikliğin nedenini ve mali tablolara etkisini dipnotlarda açıklamıştır.\n\nBu uygulama Tutarlılık Kavramı bakımından nasıl değerlendirilir?',
        {
            'A': 'Yöntem değişikliği ancak vergi matrahı azalıyorsa yapılabilir.',
            'B': 'Haklı neden ve açıklama bulunduğu için kavramla uyumludur.',
            'C': 'Tutarlılık kasa ve banka hesapları için geçerlidir, diğer kalemler için aranmaz.',
            'D': 'Yöntem değişikliği yapılamayacağından kavrama aykırıdır.',
            'E': 'Her dönem farklı yöntem seçmek Tutarlılık Kavramının gereğidir.',
        },
        'B',
        'Tutarlılık, muhasebe yöntemlerinin keyfî biçimde değiştirilmesini önler; haklı bir neden varsa değişiklik yapılmasına engel değildir. Nedenin ve finansal etkinin açıklanması hâlinde uygulama **Tutarlılık Kavramı**yla uyumludur.',
        "1 Sıra No'lu MSUGT - Muhasebenin Temel Kavramları (Tutarlılık)",
    ),
    # düzey 2
    '0052': patch(
        'İşletmenin, tahsilinde şüphe doğan bir ticari alacağı için karşılık ayırması hangi kavramla açıklanır?',
        {
            'A': 'İhtiyatlılık',
            'B': 'Maliyet Esası',
            'C': 'Tutarlılık',
            'D': 'Parayla Ölçülme',
            'E': 'Sosyal Sorumluluk',
        },
        'A',
        '**İhtiyatlılık Kavramı**, muhtemel gider ve zararların (tahsili şüpheli alacak gibi) kayıtlara alınmasını gerektirir. Bu nedenle şüpheli alacak için karşılık ayrılır; henüz gerçekleşmemiş gelirler ise kaydedilmez.',
        "1 Sıra No'lu MSUGT - İhtiyatlılık",
    ),
    # düzey 2
    '0053': patch(
        'Aşağıdaki kavram–açıklama eşleştirmelerinden hangisi doğrudur?',
        {
            'A': 'Maliyet Esası → Muhtemel zararlar için karşılık ayrılması',
            'B': 'Kişilik → Gerçekleşmemiş gelirlerin kaydedilmemesi',
            'C': 'İhtiyatlılık → İşletmenin sahibinden ayrı bir birim sayılması',
            'D': 'Parayla Ölçülme → İşlemlerin ortak ölçü olan ulusal para ile ifade edilmesi',
            'E': 'Önemlilik → Varlıkların edinme bedeliyle kaydedilmesi',
        },
        'D',
        "Doğru eşleştirme **B**'dir: **Parayla Ölçülme**, işlemlerin ortak ölçü birimi olan ulusal para ile ifade edilmesidir. Diğer şıklarda kavramlar yanlış açıklamalarla eşleştirilmiştir.",
        "1 Sıra No'lu MSUGT - Temel Kavramlar",
    ),
    # düzey 2
    '0054': patch(
        "Bilançoda varlık ve kaynakların 'kısa vadeli / uzun vadeli' (bir yıl ölçütüne göre) ayrımına tabi tutulabilmesi, temelde hangi kavramın varsayımına dayanır?",
        {
            'A': 'Parayla Ölçülme',
            'B': 'Tarafsızlık ve Belgelendirme',
            'C': 'İşletmenin Sürekliliği',
            'D': 'Önemlilik',
            'E': 'Sosyal Sorumluluk',
        },
        'C',
        'Kısa/uzun vade ayrımı, işletmenin gelecekte de faaliyetine devam edeceği (**Süreklilik**) varsayımına dayanır; işletme bir dönem sonra da var olacağından yükümlülük/varlıklar vadelerine göre sınıflanabilir.',
        "1 Sıra No'lu MSUGT - Süreklilik",
    ),
    # düzey 2
    '0055': patch(
        'İşletmede yaşanan bir grev veya üst düzey yönetici değişikliği, işletmeyi etkileyebilecek olaylar olsa da doğrudan muhasebe kaydına konu edilmez. Bu durum hangi kavramla açıklanır?',
        {
            'A': 'İhtiyatlılık',
            'B': 'Tam Açıklama',
            'C': 'Tutarlılık',
            'D': 'Parayla Ölçülme',
            'E': 'Dönemsellik',
        },
        'D',
        '**Parayla Ölçülme Kavramı** gereği yalnızca para ile ölçülebilen işlem ve olaylar kaydedilir. Grev veya yönetici değişikliği gibi parayla doğrudan ölçülemeyen olaylar muhasebe kaydına konu edilmez (gerekirse dipnotta açıklanır).',
        "1 Sıra No'lu MSUGT - Parayla Ölçülme",
    ),
    # düzey 2
    '0056': patch(
        'Bilanço tarihinden sonra ancak mali tablolar kesinleşmeden önce ortaya çıkan ve kullanıcıların kararını etkileyebilecek önemli bir olayın dipnotlarda açıklanması öncelikle hangi kavramla ilgilidir?',
        {
            'A': 'Tam Açıklama',
            'B': 'Kişilik',
            'C': 'Maliyet Esası',
            'D': 'Önemlilik',
            'E': 'Parayla Ölçülme',
        },
        'A',
        '**Tam Açıklama Kavramı**, kullanıcıların doğru karar vermesi için gerekli bilgilerin sunulmasını gerektirir; bilanço sonrası önemli olaylar bu nedenle dipnotlarda açıklanır.',
        "1 Sıra No'lu MSUGT - Tam Açıklama",
    ),
    # düzey 3
    '0057': patch(
        'Bir muhasebe hatası, 100.000.000 ₺ toplam varlığa sahip işletmede yalnız 8.000 ₺ tutarındadır; ancak düzeltilmediğinde 3.000 ₺ dönem kârı, 5.000 ₺ dönem zararına dönüşmektedir.\n\nÖnemlilik Kavramına göre en uygun değerlendirme hangisidir?',
        {
            'A': 'Önemli sayılabilecek hatalar nakit işlemlerindeki hatalardır.',
            'B': 'Tutar toplam varlıklara göre küçük olduğu için hata önemli değildir.',
            'C': 'Kârı zarara dönüştürdüğü için hata niteliği bakımından önemli kabul edilebilir.',
            'D': 'Hata tutarı ne olursa olsun bütün hatalar mali tabloları aynı ölçüde etkiler.',
            'E': 'Önemlilik belgenin kaç sayfa olduğuna göre belirlenir.',
        },
        'C',
        'Bir kalemin önemi yalnız büyüklüğüne değil, kullanıcı kararını etkileyebilecek **niteliğine** de bağlıdır. Hatanın sonucu kârdan zarara çevirmesi kararları etkileyebileceğinden, 8.000 ₺ tutarındaki hata **önemli** kabul edilebilir.',
        "1 Sıra No'lu MSUGT - Muhasebenin Temel Kavramları (Önemlilik)",
    ),
    # düzey 3
    '0058': patch(
        'Aşağıdaki uygulamalardan hangileri İhtiyatlılık Kavramı ile ilişkilendirilebilir?\n\nI. Şüpheli ticari alacaklar için karşılık ayrılması\n\nII. Sonucu belirsiz bir dava için gider karşılığı oluşturulması\n\nIII. Stokların net gerçekleşebilir değeri maliyetin altına düşünce değer düşüklüğü karşılığı ayrılması\n\nIV. Duran varlığın piyasa değerindeki artışın gelir yazılması',
        {
            'A': 'Yalnız IV',
            'B': 'I, II ve III',
            'C': 'II ve IV',
            'D': 'I ve IV',
            'E': 'I, II, III ve IV',
        },
        'B',
        '**I, II ve III** muhtemel gider/zararların kayda alınmasıdır ve ihtiyatlılıkla ilişkilidir. **IV** ise gerçekleşmemiş bir değer artışının gelir yazılmasıdır ve ihtiyatlılığa **aykırıdır**.',
        "1 Sıra No'lu MSUGT - İhtiyatlılık",
    ),
    # düzey 2
    '0059': patch(
        'İşletmenin ithal ettiği bir hammaddeyi, işlem tarihindeki kur üzerinden Türk Lirasına çevirerek ve ödediği edinme bedeliyle kaydetmesi hangi kavramların birlikte uygulanmasına örnektir?',
        {
            'A': 'İhtiyatlılık ve Tutarlılık',
            'B': 'Sosyal Sorumluluk ve Dönemsellik',
            'C': 'Kişilik ve Süreklilik',
            'D': 'Parayla Ölçülme ve Maliyet Esası',
            'E': 'Önemlilik ve Tam Açıklama',
        },
        'D',
        "İşlem tarihindeki kurla TL'ye çevirme **Parayla Ölçülme**, edinme (maliyet) bedeliyle kaydetme **Maliyet Esası** kavramının örneğidir; ithal hammadde kaydında bu iki kavram birlikte işler.",
        "1 Sıra No'lu MSUGT - Parayla Ölçülme ve Maliyet Esası",
    ),
    # düzey 3
    '0060': patch(
        'Sosyal Sorumluluk Kavramıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Muhasebe bilgisi hazırlanırken yalnız işletme sahibinin kısa vadeli çıkarı gözetilir.\n\nII. Yatırımcı, çalışan, kredi veren, devlet ve kamuoyu gibi ilgili kesimlerin güvenilir bilgi ihtiyacı dikkate alınır.\n\nIII. İşletme aleyhine olan önemli bilgiler, yaptırım beklenmiyorsa kullanıcılardan gizlenebilir.',
        {
            'A': 'I ve II',
            'B': 'Yalnız II',
            'C': 'II ve III',
            'D': 'Yalnız I',
            'E': 'I, II ve III',
        },
        'B',
        'Sosyal sorumluluk, yalnız işletme sahibinin çıkarını değil bütün ilgili kesimlerin güvenilir bilgi ihtiyacını gözetir; bu nedenle **II doğrudur**. Bilgiyi sahibin kısa vadeli çıkarına göre hazırlamak (I) ve önemli olumsuz bilgiyi gizlemek (III) kavrama aykırıdır. Doğru cevap **Yalnız II**dir.',
        "1 Sıra No'lu MSUGT - Muhasebenin Temel Kavramları (Sosyal Sorumluluk)",
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
    print(f"1 paket / {len(PATCHES)} soru ('Muhasebenin Temel Kavramlari' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
