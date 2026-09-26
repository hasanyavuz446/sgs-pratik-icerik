#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kurumlar Vergisi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Vergi-ozel profil (arsivdeki 126 gercek vergi sorusundan): kisa sik, olumsuz kok ~%32, sayisal ~%30. 2026 guncelligi: 9160 sayili CK (%50 istirak hissesi satis istisnasi), gecici m.16 (%25 tasinmaz), m.11/1-k (7577, sans oyunu reklami), m.32/C asgari kurumlar vergisi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 5520 sayili KVK guncel metni (mevzuat.gov.tr, 4/6/2026'ya kadar islenmis) + GIB Kurumlarin Tasinmaz ve Istirak Hisselerinin Satisinda Istisna Rehberi (2026)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/vergi_hukuku/kurumlar_vergisi.json"
STYLE_REF = 'SGS Vergi Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "kurumlar-gen-"


def patch(stem, options, answer, solution, ref='5520 sayili Kurumlar Vergisi Kanunu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Aşağıdaki işletmelerden hangisinin kazancı, 5520 sayılı Kurumlar Vergisi Kanunu'na göre işletme adına kurumlar vergisine tabi tutulmaz; kazanç ortakların gelir vergisi beyanında vergilendirilir?",
        {
            'A': 'Sendikaya ait, sürekli çalışan lokanta',
            'B': 'Ortaklarıyla iş gören tüketim kooperatifi',
            'C': 'Belediyeye ait, tüzel kişiliği olmayan asfalt tesisi',
            'D': 'Adi komandit şirket',
            'E': 'Sermayesi paylara bölünmüş komandit şirket',
        },
        'D',
        "KVK m. 1'deki mükellefler sermaye şirketleri, kooperatifler, iktisadi kamu kuruluşları, dernek veya vakıflara ait iktisadi işletmeler ve iş ortaklıklarıdır. Adi komandit şirket bir şahıs şirketidir; kazancı ortakların gelir vergisine konu olur. Sermayesi paylara bölünmüş komandit şirket ise m. 2/1 uyarınca sermaye şirketidir. Sendikalar dernek sayılır (m. 2/5), bu nedenle sendikanın sürekli işletmesi iktisadi işletmedir. Belediyenin asfalt tesisi iktisadi kamu kuruluşudur; tüzel kişiliğinin olmaması mükellefiyeti etkilemez (m. 2/6). Tüketim kooperatifleri de muafiyet dışında bırakılmış mükelleflerdendir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 1-2',
    ),
    # düzey 1
    '0002': patch(
        "İki anonim şirket, bir baraj inşaatını ortaklaşa üstlenmek ve kazancını paylaşmak üzere iş ortaklığı kurmuştur. 5520 sayılı Kanun'a göre bu iş ortaklığının kendisinin kurumlar vergisi mükellefi olması hangi koşula bağlıdır?",
        {
            'A': 'İşin birden çok takvim yılına yayılması',
            'B': 'Ortaklığa tüzel kişilik kazandırılması',
            'C': 'Mükellefiyet tesisinin talep edilmesi',
            'D': 'Ortaklardan birinin yabancı kurum olması',
            'E': 'Ortaklığın ticaret siciline tescil edilmesi',
        },
        'C',
        "KVK m. 2/7'ye göre iş ortaklıkları, kurumların kendi aralarında veya şahıs ortaklıkları ya da gerçek kişilerle belli bir işi birlikte yapmak için kurdukları ortaklıklardan bu şekilde mükellefiyet tesis edilmesini talep edenlerdir. Tüzel kişiliklerinin olmaması mükellefiyetlerini etkilemez; sicil tescili, işin yıllara yaygınlığı veya yabancı ortak şartı aranmaz.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 2/7',
    ),
    # düzey 3
    '0003': patch(
        "(A) A.Ş., sermayesinin %5'ine sahip olduğu tam mükellef (B) Ltd. Şti.'nden 400.000 ₺ kâr payı almıştır. Paylar dört aydır (A)'nın aktifindedir. Bu kâr payına ilişkin aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Kâr payının tamamı iştirak kazançları istisnasından yararlanır',
            'B': "Kâr payının %50'si istisnadır, kalanı kurum kazancına girer",
            'C': "İştirak oranı %10'un altında kaldığından istisna uygulanmaz",
            'D': 'Paylar bir yıl elde tutulmadığından kâr payı kurum kazancına eklenerek vergilendirilir',
            'E': 'Kâr payı yalnız sermayeye eklenirse istisnadan yararlanır',
        },
        'A',
        "Tam mükellef bir kurumun sermayesine katılımdan elde edilen kazançlar KVK m. 5/1-a-1 uyarınca istisnadır ve bu istisna için asgari iştirak oranı veya elde tutma süresi aranmaz. %10 iştirak ve bir yıl elde tutma şartları, **yurt dışı** iştirak kazançlarına ilişkin m. 5/1-b'de yer alır. İstisnanın amacı, dağıtan kurumda vergilenmiş kazancın ikinci kez vergilenmesini önlemektir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 5/1-a, 5/1-b',
    ),
    # düzey 1
    '0004': patch(
        "Bir anonim şirket, itibari değeri 10 ₺ olan paylarını 16 ₺'den ihraç ederek sermaye artırımı yapmıştır. Pay başına 6 ₺ tutarındaki fark kurumlar vergisi bakımından nasıl değerlendirilir?",
        {
            'A': 'Yalnız sermayeye eklenirse istisna kapsamına girer',
            'B': 'Olağandışı gelir olarak kurum kazancına eklenir',
            'C': 'Ertelenmiş gelir sayılıp izleyen yıl vergilendirilir',
            'D': 'Yarısı istisna sayılır, kalan yarısı dönem kazancına eklenerek vergilendirilir',
            'E': 'Emisyon primi olarak kurumlar vergisinden müstesnadır',
        },
        'E',
        'KVK m. 5/1-ç uyarınca anonim şirketlerin kuruluşlarında veya sermaye artırımlarında çıkardıkları payların bedelinin itibari değeri aşan kısmı (emisyon primi) kurumlar vergisinden müstesnadır. İstisna, tutarın sermayeye eklenmesi şartına veya kısmi orana bağlanmamıştır.',
        '5520 sayili Kurumlar Vergisi Kanunu m. 5/1-ç',
    ),
    # düzey 2
    '0005': patch(
        "Tam mükellef (T) A.Ş., Ocak 2024'te satın aldığı ve iki tam yıldan uzun süre aktifinde tuttuğu işyerini Şubat 2026'da satarak kazanç elde etmiştir. Bu satış kazancına ilişkin aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Kazancın tamamı kurum kazancına dahil edilir',
            'B': "Bedel iki yıl içinde tahsil edilirse kazancın %75'i istisnadır",
            'C': "Kazancın %50'si istisnadır",
            'D': 'Kazanç özel fon hesabına alınırsa tamamı istisnadır',
            'E': "Kazancın %25'i istisnadır",
        },
        'A',
        "7456 sayılı Kanunla 15.07.2023'ten itibaren taşınmazlar KVK m. 5/1-e kapsamından çıkarılmıştır. Geçici madde 16 yalnız bu tarihten **önce** aktifte yer alan taşınmazlar için eski hükmü %25 oranıyla korur. Ocak 2024'te edinilen işyeri bu kapsama girmediğinden satış kazancının tamamı vergilendirilir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 5/1-e (7456 ile degisik), gecici m. 16',
    ),
    # düzey 3
    '0006': patch(
        'İştirak kazançları istisnasından yararlanan (A) A.Ş., bu kazancın elde edilmesiyle doğrudan ilgili 30.000 ₺ gider yapmıştır. Ayrıca iştirak hisselerini satın almak için kullandığı kredinin 80.000 ₺ faizini ödemiştir. Bu giderlerin istisna dışı kurum kazancından indirilmesine ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': '30.000 ₺ indirilebilir; 80.000 ₺ finansman gideri indirilemez',
            'B': '30.000 ₺ indirilemez; 80.000 ₺ finansman gideri indirilebilir',
            'C': 'Yalnız istisna tutarını aşan gider kısmı indirilebilir',
            'D': 'İki gider de istisna dışı kazançtan indirilebilir',
            'E': 'İki gider de istisna dışı kazançtan indirilemez',
        },
        'B',
        "KVK m. 5/3'e göre kurumlar vergisinden istisna edilen kazançlara ilişkin giderlerin istisna dışı kurum kazancından indirilmesi kabul edilmez. Aynı fıkra bir ayrık durum öngörür: **iştirak hisseleri alımıyla ilgili finansman giderleri** kurum kazancından indirilebilir. Bu nedenle 30.000 ₺ indirilemez, 80.000 ₺ faiz indirilebilir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 5/3',
    ),
    # düzey 3
    '0007': patch(
        "(A) A.Ş.'nin elde ettiği aşağıdaki kâr paylarından hangisi 5520 sayılı Kanun'un 5/1-a bendindeki iştirak kazançları istisnasından yararlanamaz?",
        {
            'A': 'Tam mükellef anonim şirketin kurucu senedinden alınan kâr payı',
            'B': 'Tam mükellef anonim şirketin intifa senedinden alınan kâr payı',
            'C': 'Menkul kıymetler yatırım ortaklığı hissesinden alınan kâr payı',
            'D': 'Tam mükellef girişim sermayesi yatırım ortaklığından alınan kâr payı',
            'E': 'Tam mükellef limited şirketten alınan kâr payı',
        },
        'C',
        'KVK m. 5/1-a; tam mükellef kurumların sermayesine katılım kazançlarını, kurucu ve intifa senetlerinden elde edilen kâr paylarını ve girişim sermayesi yatırım fonu/ortaklığı kâr paylarını istisna eder. Bendin son cümlesine göre **diğer yatırım fonu katılma payları ile yatırım ortaklıklarının hisse senetlerinden** elde edilen kâr payları (m. 5/1-d istisnasından yararlanamayan fon ve ortaklıklar hariç) bu istisnadan yararlanamaz; menkul kıymetler yatırım ortaklığının kazancı zaten m. 5/1-d ile istisna edilmiştir.',
        '5520 sayili Kurumlar Vergisi Kanunu m. 5/1-a (son cumle), 5/1-d',
    ),
    # düzey 2
    '0008': patch(
        "Sermayesinin yarısı zarar nedeniyle karşılıksız kalan (Z) A.Ş.'nin ortakları, TTK m. 376 uyarınca sermayenin tamamlanmasına karar verilmesi üzerine zararı kapatacak tutarda 900.000 ₺ aktarmıştır. Bu tutara ilişkin aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Geçmiş yıl zararlarıyla mahsup edildikten sonra vergilendirilir',
            'B': 'Ortaklara borç sayılıp örtülü sermaye hesabına dahil edilir',
            'C': 'Kurum kazancının tespitinde dikkate alınmaz',
            'D': 'Emisyon primi sayılarak m. 5 kapsamında istisna edilir',
            'E': 'Olağandışı gelir olarak kurum kazancına eklenir',
        },
        'C',
        "KVK m. 6/3'e göre TTK m. 376 uyarınca sermayenin tamamlanmasına karar verilen şirketin ortakları tarafından zarar sebebiyle karşılıksız kalan kısmı kapatacak miktarda aktarılan tutarlar kurum kazancının tespitinde **dikkate alınmaz**. Bu bir istisna değil, kazanç unsuru sayılmama hâlidir; emisyon primi de değildir, çünkü pay ihracı yoktur.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 6/3; 6102 sayili TTK m. 376',
    ),
    # düzey 2
    '0009': patch(
        "(Z) A.Ş.'nin 2021 hesap döneminde oluşan ve beyannamesinde gösterilen zararı, kurumlar vergisi matrahının tespitinde en son hangi hesap döneminin kazancından indirilebilir?",
        {
            'A': '2027',
            'B': '2026',
            'C': '2031',
            'D': '2024',
            'E': '2025',
        },
        'B',
        "KVK m. 9/1-a'ya göre geçmiş yıl zararları, her yıla ilişkin tutarlar beyannamede ayrı ayrı gösterilmek şartıyla **beş yıldan fazla nakledilmemek** üzere indirilir. 2021 zararı 2022, 2023, 2024, 2025 ve 2026 hesap dönemlerine taşınabilir; 2027'ye devredilemez.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 9/1-a',
    ),
    # düzey 2
    '0010': patch(
        '(A) A.Ş., aynı hesap döneminde amatör spor dalında faaliyet gösteren bir kulübe 120.000 ₺, profesyonel spor dalındaki bir kulübe 180.000 ₺ sponsorluk harcaması yapmıştır. Bu harcamalardan kurum kazancından indirilebilecek toplam tutar kaçtır?',
        {
            'A': '300.000 ₺',
            'B': '150.000 ₺',
            'C': '120.000 ₺',
            'D': '210.000 ₺',
            'E': '270.000 ₺',
        },
        'D',
        "KVK m. 10/1-b'ye göre sponsorluk harcamalarının amatör spor dalları için **tamamı**, profesyonel spor dalları için **%50'si** indirilir: 120.000 + (180.000 × %50) = 210.000 ₺. 270.000 ₺ oranların ters uygulanmasının, 150.000 ₺ ikisine de %50 uygulanmasının sonucudur.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 10/1-b',
    ),
    # düzey 2
    '0011': patch(
        "Aşağıdakilerden hangisi 5520 sayılı Kanun'a göre kurum kazancının tespitinde kanunen kabul edilmeyen giderlerden değildir?",
        {
            'A': 'Hesaplanan kurumlar vergisi',
            'B': 'Ödenen vergi ziyaı cezası',
            'C': 'Şans oyunlarına ait ilan ve reklam gideri',
            'D': 'Sözleşmedeki ceza şartı uyarınca ödenen tazminat',
            'E': 'Ortağın suçundan doğan tazminat gideri',
        },
        'D',
        "KVK m. 11/1-g, kurumun, ortaklarının, yöneticilerinin ve çalışanlarının suçlarından doğan tazminat giderlerini kabul etmez; ancak **sözleşmelerde ceza şartı olarak konulan tazminatlar** bu yasağın dışındadır. Hesaplanan kurumlar vergisi ve vergi cezaları m. 11/1-d uyarınca, her türlü şans ve bahis oyunlarına ait ilan ve reklam giderleri ise 7577 sayılı Kanunla 2026'da eklenen m. 11/1-k uyarınca indirilemez.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 11/1-d, g, k',
    ),
    # düzey 2
    '0012': patch(
        'Kurumun öz sermayesinin üç katını aşan borçlanmalarından hangisi örtülü sermaye kapsamında değerlendirilmez?',
        {
            'A': 'Ortağın %30 ortağı olduğu şirketten alınan borç',
            'B': 'Ortağın gayrinakdi teminatıyla üçüncü kişiden alınan kredi',
            'C': 'Ortağın %15 pay sahibi olduğu kurumdan alınan borç',
            'D': 'Ortağın bir aracı şirket üzerinden dolaylı sağladığı borç',
            'E': 'Ortaktan doğrudan alınan faizli borç',
        },
        'B',
        "KVK m. 12/1 ortaklardan veya ortaklarla ilişkili kişilerden **doğrudan veya dolaylı** temin edilen borçları kapsar; ortakla ilişkili kişi en az %10 ortaklık ilişkisiyle tanımlanır (m. 12/3-a). Buna karşılık m. 12/6-a'ya göre ortakların veya ilişkili kişilerin sağladığı **gayrinakdi teminatlar karşılığında üçüncü kişilerden** yapılan borçlanmalar örtülü sermaye sayılmaz.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 12/1, 12/6-a',
    ),
    # düzey 1
    '0013': patch(
        '(A) A.Ş., yurt dışındaki ilişkili şirketi için fason üretim yapmaktadır. Fason bedelini, üretim maliyetine benzer işleri yapan bağımsız üreticilerin elde ettiği makul brüt kâr oranını ekleyerek belirlemektedir. Kullanılan transfer fiyatlandırması yöntemi hangisidir?',
        {
            'A': 'Karşılaştırılabilir fiyat yöntemi',
            'B': 'Yeniden satış fiyatı yöntemi',
            'C': 'İşleme dayalı net kâr marjı yöntemi',
            'D': 'Ortalama maliyet yöntemi',
            'E': 'Maliyet artı yöntemi',
        },
        'E',
        "KVK m. 13/4-b'ye göre maliyet artı yöntemi, emsallere uygun fiyatın ilgili mal veya hizmet maliyetlerinin makul bir brüt kâr oranı kadar artırılmasıyla hesaplanmasıdır. Yeniden satış fiyatı yöntemi bağımsız kişilere yeniden satış fiyatından brüt kâr düşülerek, karşılaştırılabilir fiyat yöntemi piyasa fiyatıyla karşılaştırılarak uygulanır. İşleme dayalı net kâr marjı yöntemi brüt kâr değil net kâr marjı üzerinden çalışır. Ortalama maliyet yöntemi bir stok değerleme yöntemidir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 13/4-b',
    ),
    # düzey 2
    '0014': patch(
        "Hesap dönemi takvim yılı olan (A) A.Ş.'nin 2025 hesap dönemine ait kurumlar vergisi beyannamesi 5520 sayılı Kanun'a göre hangi ay içinde verilir ve vergi en geç ne zaman ödenir?",
        {
            'A': "Nisan 2026'da verilir; vergi Nisan sonuna kadar ödenir",
            'B': "Nisan 2026'da verilir; vergi Mayıs sonuna kadar ödenir",
            'C': "Mart 2026'da verilir; vergi Mart sonuna kadar ödenir",
            'D': "Mayıs 2026'da verilir; vergi Haziran sonuna kadar ödenir",
            'E': "Şubat 2026'da verilir; vergi iki eşit taksitte ödenir",
        },
        'A',
        "KVK m. 14/3'e göre beyanname, hesap döneminin kapandığı ayı izleyen **dördüncü ay** içinde verilir; Aralık'ı izleyen dördüncü ay Nisan'dır. m. 21/1'e göre kurumlar vergisi, **beyannamenin verildiği ayın sonuna** kadar ödenir. Kurumlar vergisinde iki taksitle ödeme öngörülmemiştir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 14/3, m. 21/1',
    ),
    # düzey 2
    '0015': patch(
        'Kurumlar vergisinin kimin adına tarh edileceğine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sermaye şirketinde vergi, şirketin tüzel kişiliği adına tarh edilir',
            'B': 'Fonlarda vergi, fonun kurucusu adına tarh edilir',
            'C': 'İş ortaklığında vergi, her ortak adına payı oranında ayrı ayrı tarh edilir',
            'D': 'Tüzel kişiliği olmayan dernek iktisadi işletmesinde dernek adına tarh edilir',
            'E': 'Tüzel kişiliği olmayan iktisadi kamu kuruluşunda bağlı kamu tüzel kişisi adına tarh edilir',
        },
        'C',
        "KVK m. 16/4'e göre iş ortaklıklarında vergi, verginin ödenmesinden **müteselsilen sorumlu** olmak üzere yönetici ortak veya ortaklardan herhangi birisi adına tarh olunur; ortaklar adına paylarına göre ayrı ayrı tarh yapılmaz. Diğer ifadeler aynı fıkradaki kurallardır.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 16/4',
    ),
    # düzey 2
    '0016': patch(
        "Başka bir kurumla birleşerek infisah eden ve 19-20. maddelerdeki devir şartlarını taşımayan (K) A.Ş.'ye ilişkin aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Birleşme kârı yalnız ortakların gelir vergisi beyanında vergilendirilir',
            'B': 'Birleşme tasfiye hükmündedir; birleşme kârı vergiye matrah olur',
            'C': 'Birleşme vergisiz devir sayılır; kurum kazancı vergilendirilmez',
            'D': "Tasfiye memurlarının ödevleri (K)'nin ortaklarına geçer",
            'E': "(K)'nin geçmiş yıl zararlarının tamamı birleşilen kuruma devreder",
        },
        'B',
        "KVK m. 18/1'e göre birleşme, infisah eden kurumlar bakımından tasfiye hükmündedir; tasfiye kârı yerine **birleşme kârı** vergiye matrah olur. Tasfiye memurlarına düşen ödev ve sorumluluklar birleşilen kuruma ait olur (m. 18/3). Devir hükmünde olmayan bir birleşmede vergisiz devir ve devralınan zarar indirimi uygulanmaz.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 18',
    ),
    # düzey 1
    '0017': patch(
        'Aşağıdakilerden hangisi bir birleşmenin 5520 sayılı Kanun uyarınca "devir" hükmünde sayılması için aranan şartlardan biri değildir?',
        {
            'A': "İnfisah eden kurumun kanuni veya iş merkezinin Türkiye'de bulunması",
            'B': 'Devralınan değerlerin birleşilen kurumun bilançosuna aynen geçirilmesi',
            'C': 'Münfesih kurumun bilanço değerlerinin bir bütün hâlinde devralınması',
            'D': 'Münfesih kurumun en az iki tam yıl faaliyette bulunmuş olması',
            'E': "Birleşilen kurumun kanuni veya iş merkezinin Türkiye'de bulunması",
        },
        'D',
        "KVK m. 19/1'e göre birleşmenin devir hükmünde sayılması için birleşme sonucunda infisah eden kurum ile birleşilen kurumun kanuni veya iş merkezlerinin Türkiye'de bulunması ve münfesih kurumun devir tarihindeki bilanço değerlerinin birleşilen kurum tarafından bir bütün hâlinde devralınıp aynen bilançosuna geçirilmesi gerekir. Münfesih kurum için asgari faaliyet süresi aranmaz; iki tam yıl şartı kısmi bölünmede devredilen iştirak hisselerine ilişkindir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 19/1-2',
    ),
    # düzey 3
    '0018': patch(
        "Genel oranla vergilendirilen (İ) A.Ş.'nin 2026 kurum kazancı 4.000.000 ₺ olup bunun 1.000.000 ₺'si münhasıran ihracattan elde edilmiştir. Şirketin üretim faaliyeti yoktur. Hesaplanan kurumlar vergisi kaçtır?",
        {
            'A': '990.000 ₺',
            'B': '1.000.000 ₺',
            'C': '750.000 ₺',
            'D': '800.000 ₺',
            'E': '950.000 ₺',
        },
        'E',
        "KVK m. 32/1'e göre genel oran %25'tir; m. 32/7'ye göre münhasıran ihracattan elde edilen kazançlara oran **5 puan indirimli** (%20) uygulanır: (3.000.000 × %25) + (1.000.000 × %20) = 750.000 + 200.000 = 950.000 ₺. 1.000.000 ₺ indirimsiz hesabın, 990.000 ₺ indirimin 1 puan alınmasının sonucudur.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 32/1, 32/7',
    ),
    # düzey 2
    '0019': patch(
        "Paylarının %30'u 2026 yılında ilk kez Borsa İstanbul Pay Piyasasında işlem görmek üzere halka arz edilen perakende şirketi (P) A.Ş.'ye ilişkin aşağıdakilerden hangisi doğrudur?",
        {
            'A': "2026'dan başlayarak beş hesap dönemi oran 2 puan indirimli uygulanır",
            'B': 'Yalnız halka arz yılında oran 5 puan indirimli uygulanır',
            'C': "Halka arz oranı %50'nin altında kaldığı için indirim uygulanmaz",
            'D': 'İndirim halka arzı izleyen yıldan başlayarak üç dönem uygulanır',
            'E': 'Halka arz yılından başlayarak süresiz olarak %20 oran uygulanır',
        },
        'A',
        "KVK m. 32/6'ya göre payları Borsa İstanbul Pay Piyasasında ilk defa işlem görmek üzere **en az %20** oranında halka arz edilen kurumların (finans kesimi hariç) kazançlarına, payların ilk defa halka arz edildiği hesap döneminden başlayarak **beş hesap dönemi** boyunca kurumlar vergisi oranı **2 puan** indirimli uygulanır. Beş yıl içinde pay oranı şartı kaybedilirse alınmayan vergiler gecikme faiziyle tahsil edilir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 32/6',
    ),
    # düzey 2
    '0020': patch(
        'Yurt içi asgari kurumlar vergisine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Hesaplanan vergi, indirim ve istisnalar düşülmeden önceki kurum kazancının %10'undan az olamaz",
            'B': 'Cumhurbaşkanı %10 oranını sektör itibarıyla sıfıra kadar indirebilir',
            'C': 'İştirak kazançları istisnası asgari vergi matrahından düşülebilir',
            'D': 'İlk kez faaliyete başlayanlara üç hesap dönemi boyunca uygulanmaz',
            'E': 'Yalnız yıllık beyanda uygulanır, geçici vergi dönemlerinde dikkate alınmaz',
        },
        'E',
        "KVK m. 32/C/4'e göre madde hükmü **geçici vergi dönemleri için de** uygulanır. Hesaplanan vergi, indirim ve istisnalar düşülmeden önceki kazancın %10'undan az olamaz (m. 32/C/1); m. 5/1-a iştirak kazançları asgari vergi matrahından düşülebilecek istisnalardandır (m. 32/C/2-a); Cumhurbaşkanı oranı sıfıra kadar indirmeye veya bir katına kadar artırmaya yetkilidir (m. 32/C/7); ilk defa faaliyete başlayanlara üç hesap dönemi uygulanmaz (m. 32/C/5).",
        '5520 sayili Kurumlar Vergisi Kanunu m. 32/C',
    ),
    # düzey 2
    '0021': patch(
        'Aşağıdakilerden hangileri kurumlar vergisi mükellefidir?\n\nI. Bir sendikaya ait, devamlı faaliyet gösteren kitap satış işletmesi\n\nII. İki gerçek kişinin kurduğu adi ortaklık\n\nIII. Sermaye Piyasası Kurulunun denetimine tabi bir yatırım fonu\n\nIV. Belediyeye ait, tüzel kişiliği bulunmayan ekmek fabrikası',
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'I, II ve IV',
            'D': 'I, III ve IV',
            'E': 'I, II, III ve IV',
        },
        'D',
        "Sendika KVK m. 2/5 uyarınca dernek sayılır; devamlı işletmesi dernek iktisadi işletmesidir. SPK denetimindeki fonlar m. 2/1 gereği sermaye şirketi sayılır (kazançları ayrıca m. 5/1-d ile istisna edilse de mükelleftirler). Belediyenin ekmek fabrikası iktisadi kamu kuruluşudur ve m. 4'teki muafiyetler arasında değildir; tüzel kişiliğinin olmaması sonucu değiştirmez. Adi ortaklığın kazancı ise ortakların gelir vergisine tabidir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 1-2',
    ),
    # düzey 1
    '0022': patch(
        "Türkiye'de iş yeri bulunan dar mükellef bir yabancı kurumun aşağıdaki kazançlarından hangisi Türkiye'de elde edilmiş sayılmaz?",
        {
            'A': "Türkiye'de kiraya verdiği taşınmazından elde ettiği kira iradı",
            'B': "Türkiye'de bulunan zirai işletmesinden elde ettiği kazanç",
            'C': "Türkiye'deki bir şirketten aldığı kâr payından oluşan menkul sermaye iradı",
            'D': "İhraç için Türkiye'de alıp satmadan yurt dışına gönderdiği malların kazancı",
            'E': "Türkiye'deki iş yeri aracılığıyla yurt içindeki alıcılara yaptığı satışların kazancı",
        },
        'D',
        "KVK m. 3/3-a'daki parantez hükmüne göre kurumların ihraç edilmek üzere Türkiye'de satın aldıkları malları Türkiye'de satmaksızın yabancı ülkelere göndermelerinden doğan kazançlar, iş yeri veya daimi temsilci şartı taşınsa bile Türkiye'de elde edilmiş sayılmaz. İş yeri aracılığıyla Türkiye'de yapılan satışlar, Türkiye'deki zirai işletme kazancı, Türkiye'de kiralama iradı ve Türkiye'de elde edilen menkul sermaye iradı dar mükellefiyette kurum kazancını oluşturur.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 3/3-a',
    ),
    # düzey 3
    '0023': patch(
        "Tam mükellef (A) A.Ş., Almanya'da üretim faaliyetinde bulunan (G) GmbH'nin ödenmiş sermayesinin %12'sine sekiz aydır sahiptir. (G)'nin kazancı %22 oranında vergi yükü taşımış, (A)'ya dağıtılan kâr payı beyanname verme tarihinden önce Türkiye'ye transfer edilmiştir. Bu kâr payına 5/1-b bendindeki genel şartlarla istisna uygulanmasına ilişkin aşağıdakilerden hangisi doğrudur?",
        {
            'A': "İştirak oranı %25'in altında kaldığından istisna uygulanmaz",
            'B': 'Şartların tamamı sağlandığından kâr payının tamamı kurumlar vergisinden istisnadır',
            'C': "Vergi yükü %25'in altında kaldığından istisna uygulanmaz",
            'D': 'Transfer süresi dolmadığından istisna izleyen yıla kalır',
            'E': 'Elde tutma süresi bir yılı doldurmadığından istisna uygulanmaz',
        },
        'E',
        "KVK m. 5/1-b'ye göre yurt dışı iştirak kazançları istisnası için yurt dışı iştirakin ödenmiş sermayesinin **en az %10'una** sahip olunması, iştirak payının kazancın elde edildiği tarih itibarıyla **kesintisiz en az bir yıl** elde tutulması, kazancın faaliyet ülkesinde **en az %15** vergi yükü taşıması ve beyanname verme tarihine kadar Türkiye'ye transferi gerekir. Oran (%12), vergi yükü (%22) ve transfer şartı sağlanmıştır; sekiz aylık elde tutma süresi ise bir yılın altındadır.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 5/1-b',
    ),
    # düzey 3
    '0024': patch(
        "(A) A.Ş., 10.03.2023'te edindiği iştirak hisselerini 20.02.2026'da satmış ve 1.000.000 ₺ kazanç elde etmiştir; bedelin tamamı satış yılında tahsil edilmiş ve istisna tutarı özel fon hesabına alınmıştır. 9160 sayılı Cumhurbaşkanı Kararı dikkate alındığında bu kazancın ne kadarı kurumlar vergisinden istisnadır?",
        {
            'A': '0 ₺',
            'B': '250.000 ₺',
            'C': '1.000.000 ₺',
            'D': '500.000 ₺',
            'E': '750.000 ₺',
        },
        'D',
        "KVK m. 5/1-e, en az **iki tam yıl** aktifte tutulan iştirak hisselerinin satış kazancının bir kısmını istisna eder. Kanun metnindeki %75 oranı, 27.11.2024'te yayımlanan 9160 sayılı Cumhurbaşkanı Kararıyla bu tarihten itibaren yapılan satışlar için **%50**'ye indirilmiştir (GİB 2026 istisna rehberi). Hisseler yaklaşık üç yıl aktifte kaldığından süre şartı sağlanmıştır: 1.000.000 × %50 = 500.000 ₺. 750.000 ₺ eski oranın, 250.000 ₺ ise 15.07.2023 öncesi taşınmazlara uygulanan geçici oranın sonucudur.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 5/1-e; 9160 sayili CK (RG 27/11/2024)',
    ),
    # düzey 2
    '0025': patch(
        '(A) A.Ş., m. 5/1-e kapsamındaki iştirak hisselerini 2026 yılında vadeli olarak satmıştır. İstisnanın korunması için satış bedelinin en geç hangi tarihe kadar tahsil edilmesi gerekir?',
        {
            'A': '31.12.2028',
            'B': '31.12.2030',
            'C': '31.12.2026',
            'D': '31.12.2031',
            'E': '31.12.2027',
        },
        'A',
        "KVK m. 5/1-e'ye göre satış bedelinin, satışın yapıldığı yılı izleyen **ikinci takvim yılının sonuna** kadar tahsil edilmesi şarttır: 2026 + 2 = 31.12.2028. Bu süre içinde tahsil edilmeyen bedele isabet eden vergiler ziyaa uğramış sayılır. 31.12.2031 ise istisna tutarının pasifte özel fon hesabında tutulacağı sürenin sonudur (satış yılını izleyen beşinci yıl).",
        '5520 sayili Kurumlar Vergisi Kanunu m. 5/1-e (ikinci paragraf)',
    ),
    # düzey 1
    '0026': patch(
        "Tam mükellef (A) A.Ş.'nin elde ettiği aşağıdaki kazançlardan hangisi kurumlar vergisinden müstesna değildir?",
        {
            'A': "Türkiye'deki bir ofisini kiraya vermesinden elde ettiği kira",
            'B': 'Tam mükellef bir anonim şirketin ortağı sıfatıyla aldığı kâr payı',
            'C': 'Tam mükellef bir girişim sermayesi yatırım ortaklığından aldığı kâr payı',
            'D': 'Pay ihracında itibari değeri aşan bedel olarak elde ettiği tutar',
            'E': "Yurt dışında üstlendiği montaj işinden Türkiye'deki hesaplara aktardığı kazanç",
        },
        'A',
        "Yurt dışında yapılan inşaat, onarım, montaj ve teknik hizmetlerden sağlanıp Türkiye'de genel sonuç hesaplarına aktarılan kazançlar (m. 5/1-h), tam mükellef kurumlardan alınan kâr payları (m. 5/1-a-1), emisyon primi (m. 5/1-ç) ve girişim sermayesi yatırım ortaklıklarından alınan kâr payları (m. 5/1-a-3) istisnadır. Kurumun yurt içindeki taşınmazını kiraya vermesinden doğan gelir ise kurum kazancına dahildir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 5/1',
    ),
    # düzey 2
    '0027': patch(
        "Özel bir ilkokul 2026 hesap döneminde faaliyete geçmiştir. Okulun işletilmesinden elde edilen kazanç, 5520 sayılı Kanun'daki istisnadan hangi hesap dönemlerinde yararlanır?",
        {
            'A': 'Yalnız 2026 hesap dönemi',
            'B': '2026-2035 hesap dönemleri',
            'C': '2027-2031 hesap dönemleri',
            'D': '2026-2028 hesap dönemleri',
            'E': '2026-2030 hesap dönemleri',
        },
        'E',
        'KVK m. 5/1-ı; okul öncesi eğitim, ilköğretim, özel eğitim ve orta öğretim özel okullarının işletilmesinden **beş hesap dönemi** itibarıyla elde edilen kazançları istisna eder ve istisna okulun **faaliyete geçtiği hesap döneminden** başlar: 2026, 2027, 2028, 2029 ve 2030.',
        '5520 sayili Kurumlar Vergisi Kanunu m. 5/1-ı',
    ),
    # düzey 0
    '0028': patch(
        "5520 sayılı Kanun'a göre safi kurum kazancının tespitinde, aşağıdaki hükümlerden hangisi uygulanır?",
        {
            'A': "Gelir Vergisi Kanunu'nun ticari kazanç hükümleri",
            'B': "Vergi Usul Kanunu'nun yalnız değerleme hükümleri",
            'C': "Türk Ticaret Kanunu'nun kâr dağıtımına ilişkin hükümleri",
            'D': "Gelir Vergisi Kanunu'nun zirai kazanç hükümleri",
            'E': "Gelir Vergisi Kanunu'nun serbest meslek kazancı hükümleri",
        },
        'A',
        "KVK m. 6/2'ye göre safi kurum kazancının tespitinde Gelir Vergisi Kanunu'nun **ticari kazanç** hakkındaki hükümleri uygulanır. Zirai faaliyetle uğraşan kurumlarda GVK m. 59'un son fıkrası da dikkate alınır; bu, zirai kazanç hükümlerinin genel ölçüt olduğu anlamına gelmez.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 6/2',
    ),
    # düzey 2
    '0029': patch(
        "Yurt dışı faaliyetlerden doğan zararların Türkiye'de kurumlar vergisi matrahından indirilmesine ilişkin aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Türkiye'de istisna edilen kazançlarla ilgili yurt dışı zararlar da indirilebilir",
            'B': 'Denetim kuruluşu yoksa beyanname örneği Türk konsolosluğuna onaylatılabilir',
            'C': "Raporun aslı ile tercümesi Türkiye'deki vergi dairesine ibraz edilir",
            'D': 'Yurt dışı matrah, o ülkede yetkili denetim kuruluşunca rapora bağlanmalıdır',
            'E': 'Bu zararlar beş yıldan fazla nakledilemez',
        },
        'A',
        "KVK m. 9/1-b, yurt dışı faaliyet zararlarının indirimini **Türkiye'de kurumlar vergisinden istisna edilen kazançlarla ilgili olanlar hariç** tutar. Zararın beş yıldan fazla nakledilmemesi, o ülkede yetkili kuruluşlarca rapora bağlanması ve raporun aslı ile tercümesinin vergi dairesine ibrazı gerekir; denetim kuruluşu olmayan ülkelerde beyanname örneğinin Türk elçilik veya konsolosluğuna onaylatılması yeterlidir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 9/1-b',
    ),
    # düzey 3
    '0030': patch(
        "(A) A.Ş., 5520 sayılı Kanun'un 20. maddesine uygun bir devirle (B) A.Ş.'yi devralmıştır. (B)'nin devir tarihindeki öz sermayesi 2.000.000 ₺, beş yılı aşmamış geçmiş yıl zararları 3.000.000 ₺'dir. (B)'nin son beş yıla ait beyannameleri süresinde verilmiş ve (A), (B)'nin faaliyetini sürdürmektedir. (A) bu zararların en fazla ne kadarını indirebilir?",
        {
            'A': '1.000.000 ₺',
            'B': '5.000.000 ₺',
            'C': '2.000.000 ₺',
            'D': '0 ₺',
            'E': '3.000.000 ₺',
        },
        'C',
        "KVK m. 9/1-a'ya göre devralınan kurumun zararları, **devir tarihindeki öz sermaye tutarını geçmemek** kaydıyla indirilebilir. Bunun için devralınan kurumun son beş yıla ait beyannamelerinin kanuni süresinde verilmiş olması ve faaliyetine devrin gerçekleştiği dönemden itibaren en az beş yıl devam edilmesi gerekir. Şartlar sağlandığından indirilebilir zarar öz sermaye ile sınırlıdır: 2.000.000 ₺.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 9/1-a, m. 20/1',
    ),
    # düzey 2
    '0031': patch(
        "Aşağıdaki bağış ve harcamalardan hangisi, kurum kazancının %5'i sınırına bağlı olmaksızın tamamı kurum kazancından indirilebilir?",
        {
            'A': 'Belediyeye makbuz karşılığı yapılan nakdi bağış',
            'B': 'Genel bütçeli idareye bağışlanmak üzere yapılan okul inşası harcaması',
            'C': 'Kamu yararına çalışan derneğe yapılan nakdi bağış',
            'D': 'Profesyonel spor kulübüne yapılan sponsorluk harcaması',
            'E': 'Vergi muafiyeti tanınan vakfa yapılan ayni bağış',
        },
        'B',
        "KVK m. 10/1-ç'ye göre genel ve özel bütçeli kamu idareleri gibi kuruluşlara bağışlanan okul, sağlık tesisi, belirli kapasitedeki öğrenci yurdu gibi tesislerin inşası için yapılan harcamaların **tamamı** indirilir. Belediyeye, kamu yararına çalışan derneğe veya vergi muafiyeti tanınan vakfa yapılan bağışlar m. 10/1-c'deki %5 sınırına tabidir; profesyonel spor sponsorluğunun ise %50'si indirilir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 10/1-c, 10/1-ç, 10/1-b',
    ),
    # düzey 2
    '0032': patch(
        "(A) A.Ş.'nin Vergi Usul Kanunu'na göre tespit edilen hesap dönemi başındaki öz sermayesi 2.000.000 ₺'dir. Şirket yıl içinde %40 ortağı olan gerçek kişiden 7.500.000 ₺ faizli borç almıştır. Örtülü sermaye sayılan tutar kaçtır?",
        {
            'A': '1.500.000 ₺',
            'B': '0 ₺',
            'C': '3.500.000 ₺',
            'D': '7.500.000 ₺',
            'E': '5.500.000 ₺',
        },
        'A',
        "KVK m. 12/1'e göre ortaklardan veya ortaklarla ilişkili kişilerden temin edilen borçların, hesap dönemi içinde herhangi bir tarihte kurumun öz sermayesinin **üç katını** aşan kısmı örtülü sermayedir; öz sermaye, VUK'a göre tespit edilmiş hesap dönemi başındaki öz sermayedir (m. 12/3-b). Sınır 2.000.000 × 3 = 6.000.000 ₺; örtülü sermaye 7.500.000 − 6.000.000 = 1.500.000 ₺. 5.500.000 ₺ bir kat, 3.500.000 ₺ iki kat alınmasının sonucudur.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 12/1, 12/3-b',
    ),
    # düzey 2
    '0033': patch(
        'Transfer fiyatlandırması yoluyla örtülü kazanç dağıtımına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ortağın eşi ve eşinin üstsoyu da ilişkili kişi sayılır',
            'B': 'Kanundaki yöntemlerle emsale ulaşılamıyorsa mükellef kendi yöntemini kullanabilir',
            'C': 'Belgelendirme tam yapılmışsa vergi ziyaı cezası kural olarak %50 indirimli uygulanır',
            'D': 'Bakanlıkla anlaşılarak belirlenen yöntem üç yılı aşmamak üzere kesinlik taşır',
            'E': 'Yurt içi ilişkili kurumlar arasında örtülü kazanç, Hazine zararı aranmadan kabul edilir',
        },
        'E',
        "KVK m. 13/7'ye göre tam mükellef kurumlar arasında yurt içinde gerçekleştirilen işlemlerde örtülü kazanç dağıtımının kabulü **Hazine zararının doğması** şartına bağlıdır. Peşin fiyatlandırma anlaşmasıyla belirlenen yöntem üç yılı aşmamak üzere kesinlik taşır (m. 13/5); belgelendirme yükümlülüğü tam ve zamanında yerine getirilmişse vergi ziyaı cezası (VUK m. 359 fiilleri hariç) %50 indirimli uygulanır (m. 13/8); yöntemlerle emsale ulaşılamıyorsa mükellef kendi yöntemini kullanabilir (m. 13/4-d).",
        '5520 sayili Kurumlar Vergisi Kanunu m. 13/4-d, 13/5, 13/7, 13/8',
    ),
    # düzey 2
    '0034': patch(
        "Kendisine 1 Temmuz–30 Haziran özel hesap dönemi tayin edilen (Ö) A.Ş.'nin 01.07.2025–30.06.2026 dönemine ait kurumlar vergisi beyannamesi hangi ay içinde verilir?",
        {
            'A': 'Nisan 2027',
            'B': 'Ekim 2026',
            'C': 'Eylül 2026',
            'D': 'Temmuz 2026',
            'E': 'Nisan 2026',
        },
        'B',
        'Özel hesap dönemi tayin edilenlerin vergilendirme dönemi özel hesap dönemleridir (m. 16/1). Beyanname, hesap döneminin kapandığı ayı (Haziran 2026) izleyen **dördüncü ay** içinde verilir (m. 14/3): Temmuz, Ağustos, Eylül, Ekim → Ekim 2026. Nisan, takvim yılı hesap dönemine göre yapılan hatalı sayımdır.',
        '5520 sayili Kurumlar Vergisi Kanunu m. 14/3, m. 16/1',
    ),
    # düzey 2
    '0035': patch(
        "(T) A.Ş.'nin tasfiyeye girmesine ilişkin genel kurul kararı 15.09.2025'te tescil edilmiş, tasfiye sona ermiş ve bu karar 10.03.2027'de tescil edilmiştir. Bu tasfiyede kaç bağımsız tasfiye dönemi oluşur?",
        {
            'A': '1',
            'B': '2',
            'C': '4',
            'D': '3',
            'E': '5',
        },
        'D',
        "KVK m. 17/1-a'ya göre tasfiye, tasfiye kararının tescil edildiği tarihte başlar ve sona erme kararının tescil edildiği tarihte biter. Başlangıçtan aynı takvim yılı sonuna kadar olan dönem, sonraki her takvim yılı ve son takvim yılının başından bitiş tarihine kadar olan dönem ayrı birer tasfiye dönemidir: 15.09–31.12.2025, 2026 yılı ve 01.01–10.03.2027.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 17/1-a',
    ),
    # düzey 1
    '0036': patch(
        "Tasfiyesi 10.03.2026'da sonuçlanan (T) A.Ş.'nin tasfiyenin sona erdiği döneme ilişkin tasfiye beyannamesinin verilme süresi hangisidir?",
        {
            'A': 'Dönemin kapandığı ayı izleyen dördüncü ay içinde',
            'B': 'Tasfiyenin sonuçlandığı tarihten itibaren 15 gün içinde',
            'C': 'Tasfiyenin sonuçlandığı tarihten itibaren 30 gün içinde',
            'D': 'Tasfiye kararının tescilinden itibaren üç ay içinde',
            'E': 'İzleyen takvim yılının Mart ayı içinde',
        },
        'C',
        "KVK m. 17/2'ye göre ara tasfiye dönemlerinin beyannameleri m. 14'teki sürelerde (dönemi izleyen dördüncü ay) verilir; **tasfiyenin sona erdiği döneme** ilişkin beyanname ise tasfiyenin sonuçlandığı tarihten itibaren **otuz gün** içinde tasfiye memurlarınca verilir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 17/2',
    ),
    # düzey 2
    '0037': patch(
        'Kurumların tasfiyesine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bir yıldan uzun tasfiyede tarh zamanaşımı, tasfiyenin bittiği dönemi izleyen yıldan başlar',
            'B': 'Tasfiyeden vazgeçme kararı, alındığı dönemin başından itibaren geçerli olur',
            'C': 'Tasfiye, tasfiyeye giriş kararının alındığı genel kurul tarihinde başlar',
            'D': 'Tasfiye beyannameleri tasfiye memurlarınca verilir',
            'E': 'Tasfiye hâlindeki kurumun vergi matrahı tasfiye kârıdır',
        },
        'C',
        "KVK m. 17/1-a'ya göre tasfiye, genel kurul kararının **tescil edildiği tarihte** başlar; kararın alındığı tarih esas alınmaz. Bir yıldan fazla süren tasfiyelerde tarh zamanaşımı tasfiyenin sona erdiği dönemi izleyen yıldan başlar (m. 17/1-ç); vazgeçme kararı alındığı dönemin başından geçerlidir (m. 17/1-d); matrah tasfiye kârıdır (m. 17/4) ve beyannameleri tasfiye memurları verir (m. 17/2).",
        '5520 sayili Kurumlar Vergisi Kanunu m. 17/1-a, ç, d; 17/2; 17/4',
    ),
    # düzey 2
    '0038': patch(
        'Kısmi bölünmeye ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Üretim işletmesi devrinde faaliyet için gerekli tüm aktif ve pasifler devredilir',
            'B': 'Düzenleyici hesaplar ilgili oldukları hesapla birlikte devrolunur',
            'C': 'Devredilen iştirak hisseleri en az iki tam yıl elde tutulmuş olmalıdır',
            'D': 'Devralan şirketin hisseleri yalnız devreden şirketin ortaklarına verilebilir',
            'E': 'Devir, kayıtlı değerler üzerinden aynî sermaye olarak yapılır',
        },
        'D',
        "KVK m. 19/3-b'ye göre kısmi bölünmede devredilen varlıklara karşılık edinilen devralan şirket hisseleri **devreden şirkette kalabileceği gibi** doğrudan ortaklarına da verilebilir. Devredilen iştirak hisselerinin en az iki tam yıl elde tutulması, üretim veya hizmet işletmesi devrinde işletme bütünlüğünü sağlayan aktif ve pasiflerin tümünün devredilmesi ve devrin kayıtlı değerlerle aynî sermaye olarak yapılması gerekir; düzenleyici hesaplar ilgili hesapla birlikte devrolunur (m. 19/4).",
        '5520 sayili Kurumlar Vergisi Kanunu m. 19/3-b, 19/4',
    ),
    # düzey 1
    '0039': patch(
        "5520 sayılı Kanun'a göre bir bankanın kurum kazancına uygulanan kurumlar vergisi oranı yüzde kaçtır?",
        {
            'A': '%25',
            'B': '%22',
            'C': '%20',
            'D': '%35',
            'E': '%30',
        },
        'E',
        "KVK m. 32/1'e göre kurumlar vergisi genel olarak %25 oranında alınır. Bankalar, 6361 sayılı Kanun kapsamındaki şirketler, elektronik ödeme ve para kuruluşları, sigorta, reasürans ve emeklilik şirketleri gibi finans kesimi kurumlarının kazançlarına ise %30 oranı uygulanır.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 32/1 (7394 ve 7456 ile degisik)',
    ),
    # düzey 3
    '0040': patch(
        "2015'ten beri faaliyette olan ve indirimli oran veya yatırım teşviki kullanmayan (M) A.Ş.'nin 2026 ticari bilanço kârı 800.000 ₺, kanunen kabul edilmeyen giderleri 200.000 ₺'dir. Şirket, iştirak hissesi satışından doğan 700.000 ₺'lik kazancına m. 5/1-e istisnasını uygulamıştır. Ödenmesi gereken kurumlar vergisi kaçtır?",
        {
            'A': '30.000 ₺',
            'B': '75.000 ₺',
            'C': '100.000 ₺',
            'D': '250.000 ₺',
            'E': '80.000 ₺',
        },
        'C',
        "Normal hesap: (800.000 + 200.000 − 700.000) × %25 = 75.000 ₺. KVK m. 32/C'ye göre hesaplanan vergi, indirim ve istisnalar düşülmeden önceki kurum kazancının (ticari bilanço kârı + KKEG = 1.000.000 ₺, m. 32/C/6) **%10'undan az olamaz**: 100.000 ₺. Asgari vergi matrahından düşülebilecek istisnalar m. 32/C/2'de sayılmıştır; iştirak hissesi satış kazancı istisnası (m. 5/1-e) bunlar arasında olmadığından 700.000 ₺ düşülmez. Ödenecek vergi 100.000 ₺'dir. 80.000 ₺ KKEG'nin tabana eklenmemesinin, 250.000 ₺ ise istisnanın normal vergi hesabında da düşülmemesinin sonucudur.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 32/C/1, 2, 6',
    ),
    # düzey 3
    '0041': patch(
        'Bir vakfa ait kafeterya işletmesi devamlı faaliyet göstermekte, ürünlerini yaklaşık maliyetine satmakta ve oluşan küçük kârı vakfın amaçlarına harcamaktadır. İşletmenin ayrı tüzel kişiliği ve ayrılmış sermayesi yoktur. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kâr amacı gütmediği için kurumlar vergisi mükellefiyeti doğmaz',
            'B': 'İşletme mükelleftir; vergi, vakıf adına tarh edilir',
            'C': 'Kârını vakıf amacına harcadığı için kazancı istisnadır',
            'D': 'İşletme mükelleftir; vergi, işletme müdürü adına tarh edilir',
            'E': 'Sermayesi ayrılmadığı için vakfın gelir vergisine tabidir',
        },
        'B',
        "KVK m. 2/6'ya göre dernek veya vakıflara ait iktisadi işletmelerin kazanç amacı gütmemeleri, tüzel kişiliklerinin ve ayrılmış sermayelerinin olmaması, bedelin sadece maliyeti karşılaması veya kârın kuruluş amaçlarına tahsis edilmesi mükellefiyetlerini ve iktisadi niteliklerini etkilemez. Tüzel kişiliği olmayan iktisadi işletmeler için vergi, bağlı oldukları dernek veya vakıf adına tarh olunur (m. 16/4); müdür adına tarh söz konusu değildir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 2/6, m. 16/4',
    ),
    # düzey 2
    '0042': patch(
        "Kanuni merkezi Hollanda'da bulunan (X) B.V.'nin bütün yönetim kararları İstanbul'daki ofisinde alınmakta ve işlemleri burada toplanmaktadır. Bu kurumun Türkiye'deki vergilendirilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Kanuni merkezi esas alındığından Türkiye'de mükellefiyeti doğmaz",
            'B': 'Tam mükelleftir; Türkiye içi ve dışı kazançlarının tamamı vergilendirilir',
            'C': 'Dar mükelleftir; kanuni merkezi yurt dışında olduğundan yalnız Türkiye kazancı vergilenir',
            'D': "Tam mükelleftir; ancak yalnız Türkiye'deki kazançları vergilendirilir",
            'E': 'Dar mükelleftir; iş merkezindeki işlemler yurt dışı kazanç sayılır',
        },
        'B',
        "KVK m. 3/1'e göre kanuni **veya** iş merkezi Türkiye'de bulunan kurumlar tam mükelleftir ve Türkiye içinde ve dışında elde ettikleri kazançların tamamı üzerinden vergilendirilir. Dar mükellefiyet için kanuni ve iş merkezinin **her ikisinin** de Türkiye dışında olması gerekir (m. 3/2). İş merkezi, işlemlerin fiilen toplandığı ve yönetildiği merkezdir (m. 3/6); burada İstanbul'dur.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 3/1-2, 3/5-6',
    ),
    # düzey 2
    '0043': patch(
        "Aşağıdakilerden hangisi 5520 sayılı Kanun'un 4. maddesi uyarınca kurumlar vergisinden muaf değildir?",
        {
            'A': 'Yaptığı iş karşılığında harç alan kamu kuruluşu',
            'B': 'Kamu idaresi tarafından sosyal amaçla işletilen öğrenci yurdu',
            'C': 'Belediyeye ait, şehirlerarası yolcu taşıyan otobüs işletmesi',
            'D': 'Belediyeye ait, boru hattıyla dağıtım yapan su işletmesi',
            'E': 'Kamu idaresince yetkili makam izniyle açılan uluslararası fuar',
        },
        'C',
        'Belediyelere ait yolcu taşıma işletmelerinin muafiyeti KVK m. 4/1-ı-2 uyarınca **belediye sınırları içinde** faaliyette bulunanlarla sınırlıdır; şehirlerarası taşımacılık muafiyet kapsamında değildir. Kanal ve boru ile dağıtım yapan su işletmeleri (m. 4/1-ı-1), izinle açılan fuarlar (m. 4/1-ç), sosyal amaçlı öğrenci yurtları (m. 4/1-c) ve resim ve harç alan kamu kuruluşları (m. 4/1-f) muaftır.',
        '5520 sayili Kurumlar Vergisi Kanunu m. 4/1-ı, c, ç, f',
    ),
    # düzey 1
    '0044': patch(
        'Ana sözleşmesinde sermaye üzerinden kazanç dağıtılmaması ve yalnız ortaklarla iş görülmesi gibi hükümler bulunan ve bunlara fiilen uyan kooperatiflerden hangisi kurumlar vergisi muafiyetinden yararlanamaz?',
        {
            'A': 'Hayvancılık kooperatifi',
            'B': 'Tüketim kooperatifi',
            'C': 'Tarımsal kalkınma kooperatifi',
            'D': 'Su ürünleri kooperatifi',
            'E': 'Sulama kooperatifi',
        },
        'B',
        'KVK m. 4/1-k, kanunda sayılan şartları taşıyan ve bunlara fiilen uyan kooperatifleri muaf tutar; ancak **tüketim ve taşımacılık kooperatifleri** bu muafiyetin dışında bırakılmıştır. Yapı kooperatiflerinde ayrıca yapı ruhsatı ve arsa tapusunun kooperatif adına tescili ve yönetimde müteahhitle ilişkili kişilere yer verilmemesi aranır.',
        '5520 sayili Kurumlar Vergisi Kanunu m. 4/1-k',
    ),
    # düzey 3
    '0045': patch(
        "(T) A.Ş., 2021'de satın aldığı ve o tarihten beri aktifinde tuttuğu bir depoyu Mart 2026'da 800.000 ₺ kazançla satmış, bedelin tamamını satış yılında tahsil etmiş ve istisnaya konu tutarı özel fon hesabına almıştır. Satış kazancının ne kadarı kurumlar vergisinden istisnadır?",
        {
            'A': '400.000 ₺',
            'B': '600.000 ₺',
            'C': '200.000 ₺',
            'D': '800.000 ₺',
            'E': '0 ₺',
        },
        'C',
        "15.07.2023'ten önce kurumların aktifinde yer alan taşınmazlar için KVK geçici madde 16 uyarınca m. 5/1-e'nin eski hükümleri uygulanır; ancak %50 oranı, bu tarihten sonra yapılan satışlar için **%25** olarak uygulanır. İki tam yıl şartı sağlanmıştır: 800.000 × %25 = 200.000 ₺. 400.000 ₺ eski %50 oranının, 0 ₺ ise taşınmazın 15.07.2023'ten sonra edinilmiş olması hâlinin sonucudur.",
        '5520 sayili Kurumlar Vergisi Kanunu gecici m. 16; m. 5/1-e (7456 oncesi)',
    ),
    # düzey 2
    '0046': patch(
        'Bir tüketim kooperatifi, ortaklarının kişisel ve ailevi gıda alımlarının değerine göre hesapladığı risturnu ortaklarına iade etmiştir. Bu risturna ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kurumlar vergisinden istisnadır; ortaklara dağıtımı kâr dağıtımı sayılmaz',
            'B': 'Kâr dağıtımı sayılır ve ortaklar adına vergi kesintisine tabidir',
            'C': 'Yalnız nakden ödenirse istisnadan yararlanır',
            'D': 'Kooperatif muaf olmadığından risturn da vergilendirilir',
            'E': 'Ortak dışı işlemlerden doğan kısmı da istisnaya dahildir',
        },
        'A',
        'KVK m. 5/1-i, tüketim kooperatiflerinin ortaklarının kişisel ve ailevi gıda ve giyecek ihtiyaçları için satın aldıkları malların değerine göre hesapladıkları risturnları istisna eder; bunların dağıtımı kâr dağıtımı sayılmaz ve risturnun aynı değerde mal ile ödenmesi istisnaya engel değildir. Tüketim kooperatifinin m. 4/1-k muafiyetinden yararlanamaması, risturn istisnasını ortadan kaldırmaz. Ortak dışı işlemlerden doğan kazançlara istisna uygulanmaz.',
        '5520 sayili Kurumlar Vergisi Kanunu m. 5/1-i, m. 4/1-k',
    ),
    # düzey 3
    '0047': patch(
        "Tam mükellef (A) A.Ş., yurt dışındaki (Y) Ltd.'nin sermayesinin %60'ına sahiptir. (Y)'nin hasılatının %40'ı faiz ve kira gibi pasif gelirlerden oluşmakta, ticari bilanço kârı üzerinden %8 vergi yükü taşımakta ve hasılatı kanundaki tutar eşiğini aşmaktadır. (Y)'nin kazancına ilişkin aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Kazancın tamamı dağıtım yılında gelir vergisine tabi olur',
            'B': "Kontrol oranı %75'in altında kaldığı için hüküm uygulanmaz",
            'C': "Türkiye'ye transfer edilmedikçe (A) nezdinde vergilendirilmez",
            'D': 'Yurt dışı iştirak kazancı olarak (A) nezdinde istisnadır',
            'E': "Dağıtılmasa da pay oranında (A)'nın kurumlar vergisi matrahına girer",
        },
        'E',
        "KVK m. 7'ye göre tam mükelleflerin en az %50'sini kontrol ettikleri yurt dışı iştiraklerinin kazançları; hasılatın %25 veya fazlasının pasif gelirlerden oluşması, ticari bilanço kârı üzerinden %10'dan az vergi yükü taşınması ve hasılatın kanuni eşiği aşması şartlarının birlikte gerçekleşmesi hâlinde, **dağıtılsın veya dağıtılmasın** hisse oranında Türkiye'de kurumlar vergisi matrahına dahil edilir. Şartların hepsi (%60 kontrol, %40 pasif gelir, %8 vergi yükü) sağlanmıştır.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 7',
    ),
    # düzey 2
    '0048': patch(
        "Ticari kazanç gibi hesaplanan kurum kazancının tespitinde 5520 sayılı Kanun'un 8. maddesiyle ayrıca indirilmesine izin verilen giderler arasında aşağıdakilerden hangisi yer almaz?",
        {
            'A': 'Sermayesi paylara bölünmüş komandit şirkette komandite ortağın kâr payı',
            'B': 'Menkul kıymet ihraç giderleri',
            'C': 'Ortaklara öz sermaye üzerinden ödenen faiz',
            'D': 'Genel kurul toplantıları için yapılan giderler',
            'E': 'Kuruluş ve örgütlenme giderleri',
        },
        'C',
        'KVK m. 8; menkul kıymet ihraç giderlerini, kuruluş ve örgütlenme giderlerini, genel kurul ile birleşme, devir, bölünme, fesih ve tasfiye giderlerini ve sermayesi paylara bölünmüş komandit şirkette komandite ortağın kâr payını indirilecek giderler arasında sayar. Öz sermaye üzerinden ödenen veya hesaplanan faizler ise m. 11/1-a uyarınca kanunen kabul edilmeyen giderdir.',
        '5520 sayili Kurumlar Vergisi Kanunu m. 8, m. 11/1-a',
    ),
    # düzey 2
    '0049': patch(
        "(A) A.Ş.'nin 2026 hesap dönemi kurum kazancı 4.000.000 ₺'dir. Şirket yıl içinde bir belediyeye makbuz karşılığı 300.000 ₺ nakdi bağış yapmıştır; başka bağış ve yardımı yoktur. Bu bağıştan kurum kazancından indirilebilecek tutar kaçtır?",
        {
            'A': '150.000 ₺',
            'B': '400.000 ₺',
            'C': '120.000 ₺',
            'D': '200.000 ₺',
            'E': '300.000 ₺',
        },
        'D',
        "KVK m. 10/1-c'ye göre belediyelere makbuz karşılığı yapılan bağış ve yardımların toplamının o yıla ait **kurum kazancının %5'ine** kadar olan kısmı indirilir: 4.000.000 × %5 = 200.000 ₺. Bağışın aşan 100.000 ₺'lik kısmı indirilemez.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 10/1-c',
    ),
    # düzey 2
    '0050': patch(
        "Aşağıdakilerden hangileri kurum kazancının tespitinde indirilemez?\n\nI. TTK uyarınca safi kazançtan ayrılan kanuni yedek akçe\n\nII. İşletmenin esas faaliyetiyle ilgisi olmayan yatın amortismanı\n\nIII. Sözleşmedeki ceza şartı uyarınca ödenen tazminat\n\nIV. 6183 sayılı Kanun'a göre ödenen gecikme zammı",
        {
            'A': 'II ve III',
            'B': 'I, II, III ve IV',
            'C': 'I, II ve IV',
            'D': 'I, III ve IV',
            'E': 'I ve II',
        },
        'C',
        "KVK m. 11/1-ç her ne ad altında olursa olsun ayrılan yedek akçeleri, m. 11/1-f esas faaliyet konusuyla ilgisi olmayan yat, kotra, uçak gibi taşıtların gider ve amortismanlarını, m. 11/1-d ise 6183 sayılı Kanun'a göre ödenen gecikme zamlarını kanunen kabul edilmeyen gider sayar. Sözleşmede ceza şartı olarak konulan tazminatlar m. 11/1-g'deki yasağın dışında bırakılmıştır.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 11/1-ç, d, f, g',
    ),
    # düzey 1
    '0051': patch(
        'Örtülü sermaye üzerinden ödenen faiz, hem borç alan hem de borç veren nezdinde hangi tarih itibarıyla dağıtılmış kâr payı sayılır?',
        {
            'A': 'Örtülü sermaye şartlarının gerçekleştiği hesap döneminin son günü',
            'B': 'İzleyen hesap döneminin ilk günü',
            'C': 'Borcun kuruma aktarıldığı gün',
            'D': 'Kurumlar vergisi beyannamesinin verildiği gün',
            'E': 'Faizin ödendiği gün',
        },
        'A',
        "KVK m. 12/7'ye göre örtülü sermaye üzerinden kur farkı hariç faiz ve benzeri ödemeler, Gelir ve Kurumlar Vergisi kanunlarının uygulanmasında gerek borç alan gerekse borç veren nezdinde, örtülü sermaye şartlarının gerçekleştiği **hesap döneminin son günü** itibarıyla dağıtılmış kâr payı (dar mükelleflerde ana merkeze aktarılan tutar) sayılır.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 12/7',
    ),
    # düzey 2
    '0052': patch(
        "(A) A.Ş.'nin ortağı olan gerçek kişiyle akrabalık ilişkisi bulunan aşağıdaki kişilerden hangisi transfer fiyatlandırması bakımından ilişkili kişi sayılmaz?",
        {
            'A': 'Ortağın yeğeni',
            'B': 'Ortağın eşi',
            'C': 'Ortağın eşinin babası',
            'D': 'Ortağın kardeşi',
            'E': 'Ortağın kuzeni',
        },
        'E',
        "KVK m. 13/2'ye göre ortakların eşleri, ortakların veya eşlerinin üstsoy ve altsoyu ile **üçüncü derece dahil** yansoy hısımları ve kayın hısımları ilişkili kişi sayılır. Kardeş ikinci, yeğen üçüncü derece yansoy hısımdır; eşin babası kayın hısmıdır. Kuzen ise dördüncü derece yansoy hısım olduğundan bu sayıma girmez.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 13/2',
    ),
    # düzey 3
    '0053': patch(
        "(A) A.Ş., emsal bedeli 1.000.000 ₺ olan bir makineyi %100 ortağı (B) A.Ş.'ye 600.000 ₺'ye satmıştır; işlem Hazine zararına yol açmıştır. Bu işleme ilişkin aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Bedel ilişkili taraflarca serbestçe belirlenebildiğinden düzeltme yapılmaz',
            'B': "600.000 ₺'lik satış bedelinin tamamı kâr payı dağıtımı sayılır",
            'C': "400.000 ₺ örtülü kazanç dağıtılmış sayılır ve (A)'nın kazancına eklenir",
            'D': "Fark yalnız (B)'nin kazancına eklenerek orada vergilendirilir",
            'E': '400.000 ₺ örtülü sermaye sayılır ve bu tutarın faizi gider yazılamaz',
        },
        'C',
        "KVK m. 13/1'e göre ilişkili kişilerle emsallere aykırı bedelle mal alım-satımında kazanç transfer fiyatlandırması yoluyla örtülü olarak dağıtılmış sayılır; fark 1.000.000 − 600.000 = 400.000 ₺'dir ve m. 11/1-c uyarınca indirim konusu yapılamaz. m. 13/6'ya göre bu tutar, şartların gerçekleştiği hesap döneminin son günü itibarıyla dağıtılmış kâr payı sayılır. Yurt içi ilişkili kurumlar arasında bu sonuç Hazine zararı şartına bağlıdır (m. 13/7); soruda bu şart gerçekleşmiştir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 13/1, 13/6',
    ),
    # düzey 2
    '0054': patch(
        'Kurumlar vergisi beyanı ve ödemesine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Vergi, beyannamenin verildiği ayı izleyen ayın sonuna kadar ödenir',
            'B': 'Tüzel kişiliği olmayan dernek işletmesi için beyannameyi dernek verir',
            'C': 'Beyanname, kanuni veya iş merkezinin bulunduğu yerin vergi dairesine verilir',
            'D': 'Bağımsız muhasebesi olan şubeler için ayrı beyanname verilmez',
            'E': 'Geliri yalnız kesintiye tabi taşınmaz kirasından oluşan kooperatif beyanname vermez',
        },
        'A',
        "KVK m. 21/1'e göre kurumlar vergisi, **beyannamenin verildiği ayın sonuna** kadar ödenir; izleyen aya sarkmaz. Şubeler için bağımsız muhasebeleri olsa da ayrı beyanname verilmez (m. 14/4); bağlı olunan vergi dairesi kanuni veya iş merkezinin bulunduğu yerin dairesidir (m. 14/6); gelirleri kesintiye tabi taşınmaz kira gelirinden ibaret kooperatifler beyanname vermez (m. 14/5); tüzel kişiliği olmayan iktisadi işletmeler için beyannameyi bağlı oldukları dernek veya vakıf verir (m. 14/2).",
        '5520 sayili Kurumlar Vergisi Kanunu m. 14/2, 14/4, 14/5, 14/6, m. 21/1',
    ),
    # düzey 1
    '0055': patch(
        'Posta ile gönderilen kurumlar vergisi beyannamesine ilişkin vergi, beyannamenin vergiyi tarh edecek daireye geldiği tarihi izleyen kaç gün içinde tarh edilir?',
        {
            'A': '3',
            'B': '1',
            'C': '5',
            'D': '15',
            'E': '7',
        },
        'A',
        "KVK m. 16/5'e göre kurumlar vergisi, bağlı olunan vergi dairesine beyannamenin verildiği günde; beyanname posta ile gönderilmişse vergiyi tarh edecek daireye geldiği tarihi izleyen **üç gün** içinde tarh edilir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 16/5',
    ),
    # düzey 2
    '0056': patch(
        "Önceki tasfiye dönemlerinde kâr beyan ederek vergi ödeyen (T) A.Ş.'nin tasfiyesi zararla kapanmıştır. Bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Önceki dönem vergileri kesinleştiğinden düzeltme yapılmaz',
            'B': 'Sonuç önceki tasfiye dönemlerine doğru düzeltilir ve fazla ödenen vergi iade edilir',
            'C': 'Zarar, ortakların gelir vergisi beyanlarında indirim konusu yapılır',
            'D': 'Fazla ödenen vergi yalnız tasfiye memurlarının borçlarına mahsup edilir',
            'E': 'Zarar izleyen beş yılın kazancından indirilmek üzere devreder',
        },
        'B',
        "KVK m. 17/1-c'ye göre tasfiyenin zararla kapanması hâlinde tasfiye sonucu önceki tasfiye dönemlerine doğru düzeltilir ve bu dönemlerde fazla ödenen vergi mükellefe iade edilir. Tasfiye edilen kurum için ileriye zarar devri söz konusu olmaz; zarar ortakların beyanına da aktarılmaz.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 17/1-c',
    ),
    # düzey 2
    '0057': patch(
        "(B) A.Ş., tam bölünme yoluyla infisah ederek varlıklarını iki tam mükellef sermaye şirketine devretmektedir. Ortaklarına verilecek iştirak hisselerinin toplam itibari değeri 5.000.000 ₺'dir. İşlemin tam bölünme sayılmasını engellemeden ortaklara en fazla ne kadar nakit ödenebilir?",
        {
            'A': '2.500.000 ₺',
            'B': '250.000 ₺',
            'C': '0 ₺',
            'D': '500.000 ₺',
            'E': '1.000.000 ₺',
        },
        'D',
        "KVK m. 19/3-a'ya göre tam bölünmede devredilen şirketin ortaklarına verilecek iştirak hisselerinin itibari değerinin **%10'una kadarlık** kısmının nakit olarak ödenmesi, işlemin bölünme sayılmasına engel değildir: 5.000.000 × %10 = 500.000 ₺. Tam bölünmede mal varlığının iki veya daha fazla tam mükellef sermaye şirketine devredilmesi gerekir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 19/3-a',
    ),
    # düzey 1
    '0058': patch(
        "Tam mükellef (A) A.Ş., (B) A.Ş.'nin yönetimini ve hisse çoğunluğunu elde edecek şekilde hisselerini devralmış, karşılığında (B)'nin bu hisseleri devreden ortaklarına kendi sermayesini temsil eden iştirak hisselerini vermiştir. Bu işlem 5520 sayılı Kanun bakımından hangisidir?",
        {
            'A': 'Tam bölünme',
            'B': 'Hisse değişimi',
            'C': 'Kısmi bölünme',
            'D': 'Devir',
            'E': 'Tür değiştirme',
        },
        'B',
        "KVK m. 19/3-c'ye göre tam mükellef bir sermaye şirketinin, diğer bir sermaye şirketinin hisselerini **yönetimini ve hisse çoğunluğunu** elde edecek şekilde devralması ve karşılığında devreden ortaklara kendi iştirak hisselerini vermesi hisse değişimidir. Devirde bir kurum infisah eder; bölünmede ise mal varlığı devredilir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 19/3-c',
    ),
    # düzey 1
    '0059': patch(
        'Kurumlar vergisi mükelleflerinin ödediği geçici vergiye ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Geçici vergi, Gelir Vergisi Kanunu'nda belirtilen esaslara göre ödenir",
            'B': 'Dar mükellef kurumlarda geçici vergi ticari ve zirai kazançlarla sınırlıdır',
            'C': 'Geçici vergi, cari dönemin kurumlar vergisi oranında hesaplanır',
            'D': 'Cumhurbaşkanı geçici vergi oranını 10 puana kadar indirebilir',
            'E': 'Ödenen geçici vergi, cari dönemin kurumlar vergisinden mahsup edilir',
        },
        'D',
        "KVK m. 32/2'ye göre geçici vergi, cari vergilendirme döneminin kurumlar vergisine mahsup edilmek üzere GVK'daki esaslara göre ve **cari dönemin kurumlar vergisi oranında** ödenir; dar mükelleflerde ticari ve zirai kazançlarla sınırlıdır. m. 32/3'e göre Cumhurbaşkanı bu oranı **5 puana kadar** indirmeye yetkilidir; 10 puanlık bir yetki yoktur.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 32/2-3',
    ),
    # düzey 2
    '0060': patch(
        "2024 yılında kurulup aynı yıl faaliyete başlayan (Y) A.Ş.'ye yurt içi asgari kurumlar vergisi hükümleri ilk kez hangi hesap döneminde uygulanır?",
        {
            'A': '2025',
            'B': '2026',
            'C': '2027',
            'D': '2028',
            'E': '2029',
        },
        'C',
        "KVK m. 32/C/5'e göre ilk defa faaliyete başlayan kurumlar hakkında faaliyete başlanılan hesap döneminden itibaren **üç hesap dönemi** boyunca asgari kurumlar vergisi hükümleri uygulanmaz: 2024, 2025 ve 2026 dışarıda kalır; ilk uygulama dönemi 2027'dir.",
        '5520 sayili Kurumlar Vergisi Kanunu m. 32/C/5',
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
    print(f"1 paket / {len(PATCHES)} soru ('Kurumlar Vergisi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
