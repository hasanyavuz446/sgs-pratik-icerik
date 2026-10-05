#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TMS 20 Devlet Tesvikleri — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Standartlar dersinin gercek sinav profiline gore yeniden yazim (senaryo kok + kisa tutar/terim sik; 2019-2026 sinavlarinda dogrudan TMS 20 sorusu yok). Kapsam: kapsam disi durumlar (vergi avantajlari, TMS 41, devlet ortakligi), tanimlar (varlik/gelire iliskin tesvik, geri odenmeyen kredi, devlet yardimi), makul guvence ile tanima, gelir yaklasimi, amortisman oraninda aktarim (dogrusal, azalan bakiyeler, uretim miktari, kist), kosula bagli arsa, parasal olmayan tesvik, sunum yontemleri ve nakit akis gosterimi, gecmis zararlari karsilayan tesvik, piyasa faizi altindaki kredi faydasi, geri odemeler, aciklamalar. Eski surum 76 mutlak ifadeli celdirici tasiyordu (kor %38). 25 hesap sorusu modulde hesaplandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: TMS 20 Devlet Tesviklerinin Muhasebelestirilmesi ve Devlet Yardimlarinin Aciklanmasi (KGK); TFRS 9, TMS 41 ilgili paragraflar
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/tms_20_devlet_tesvik.json"
STYLE_REF = 'SGS Muhasebe Standartlari (gercek sinav profiline kalibre: senaryo kok + kisa sik)'
ONEK = "std-tms20-gen-"


def patch(stem, options, answer, solution, ref='TMS 20 Devlet Tesviklerinin Muhasebelestirilmesi'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Bir işletme yıl içinde şu desteklerden yararlanmıştır: yatırım teşvik belgesi kapsamında kurumlar vergisi indirimi, makine alımı için devletten nakit hibe, istihdam edilen her personel için ücret desteği, bölgesel kalkınma ajansından AR-GE hibesi ve belediyeden bedelsiz arsa. Bunlardan hangisi TMS 20 kapsamı dışındadır?',
        {
            'A': 'Ücret desteği',
            'B': 'Kurumlar vergisi indirimi',
            'C': 'Makine alımı için devletten alınan hibe',
            'D': 'Bedelsiz arsa',
            'E': 'AR-GE hibesi',
        },
        'B',
        "TMS 20 p. 2(b)'ye göre gelir vergisi tatilleri, yatırım vergi indirimleri ve vergi oranı indirimleri gibi **gelir vergisi yükümlülüğünün belirlenmesinde sağlanan avantajlar** TMS 20 kapsamı dışındadır; bunlar TMS 12'ye göre ele alınır.",
        'TMS 20 p. 2',
    ),
    # düzey 2
    '0002': patch(
        'Bir işletme devletten ücretsiz teknik danışmanlık hizmeti almış ve bir kamu kurumunun ürünlerinin önemli bir kısmını satın alması nedeniyle satışları artmıştır; bu desteklere makul bir değer biçilememektedir. Bu destekler hakkında ne yapılır?',
        {
            'A': 'Önemliyse açıklanır',
            'B': 'Gelir olarak tanınır',
            'C': 'Ertelenmiş gelir tanınır',
            'D': 'Varlık olarak tanınır',
            'E': 'Özkaynağa eklenir',
        },
        'A',
        "TMS 20 p. 34-36'ya göre makul biçimde değer biçilemeyen **devlet yardımları** (ücretsiz teknik danışmanlık, devlet alımları gibi) finansal tablolara alınmaz; yardımın niteliği, kapsamı ve süresi yanıltıcı olmaması için **açıklanır**.",
        'TMS 20 p. 34-35',
    ),
    # düzey 2
    '0003': patch(
        "Bir işletme bir teşvikin tamamını nakit alındığı dönemde gelir yazmak istemektedir; teşvik ise gelecek 4 yılda katlanılacak eğitim giderlerini karşılamak için verilmiştir. Bu uygulama TMS 20'ye göre nasıl değerlendirilir?",
        {
            'A': 'Önemsizse zorunludur',
            'B': 'Tercihe bağlıdır',
            'C': 'İhtiyatlılık gereğidir',
            'D': 'Uygundur',
            'E': 'Uygun değildir',
        },
        'E',
        "TMS 20 p. 12 ve 16'ya göre teşvikler, **karşılayacağı ilgili maliyetlerin gider yazıldığı dönemler boyunca** sistematik esasla gelir yazılır; nakit esasına göre tanıma yalnızca daha sistematik bir esas bulunmadığında uygundur.",
        'TMS 20 p. 12, 16',
    ),
    # düzey 3
    '0004': patch(
        "Bir işletme 1.000.000 ₺'lik makine için aldığı 200.000 ₺ teşviki makinenin defter değerinden düşerek sunmaktadır. Makinenin yararlı ömrü 5 yıl, kalıntı değeri sıfırdır. Yıllık amortisman gideri kaç ₺'dir?",
        {
            'A': '280.000',
            'B': '160.000',
            'C': '200.000',
            'D': '800.000',
            'E': '240.000',
        },
        'B',
        "TMS 20 p. 24 ve 27'ye göre varlıkla ilgili teşvikler varlığın defter değerinden düşülerek de sunulabilir; bu durumda teşvik, **azaltılmış amortisman** yoluyla gelire yansır: (1.000.000 − 200.000) / 5 = **160.000 ₺**.",
        'TMS 20 p. 24-27',
    ),
    # düzey 3
    '0005': patch(
        "Bir belediye bir işletmeye, üzerine 20 yıl yararlı ömürlü bir fabrika binası inşa etmesi koşuluyla gerçeğe uygun değeri 300.000 ₺ olan arsayı bedelsiz vermiştir. İşletme teşviki GUD'den tanımıştır ve bina bu yıl başında kullanıma alınmıştır. Teşvikten her yıl gelire aktarılacak tutar kaç ₺'dir?",
        {
            'A': '15.000',
            'B': '0',
            'C': '10.000',
            'D': '300.000',
            'E': '6.000',
        },
        'A',
        "TMS 20 p. 18'e göre amortismana tabi olmayan bir varlığa (arsa) ilişkin teşvik belirli yükümlülüklerin yerine getirilmesini gerektirebilir; bu durumda teşvik, **bu yükümlülüklerin maliyetlerinin gider yazıldığı dönemlere**, yani bina amortismanı boyunca yayılır: 300.000 / 20 = **15.000 ₺**.",
        'TMS 20 p. 18',
    ),
    # düzey 2
    '0006': patch(
        "Gelire ilişkin devlet teşviklerinin kâr veya zarar tablosunda sunumunda TMS 20'nin izin verdiği iki yöntem hangisidir?",
        {
            'A': "Hasılat olarak veya DKG'de",
            'B': 'Özkaynakta veya karşılıkta',
            'C': 'Finansman geliri veya vergi geliri',
            'D': 'Diğer gelir olarak veya ilgili giderden indirilerek',
            'E': 'Olağanüstü gelir veya dipnot',
        },
        'D',
        "TMS 20 p. 29'a göre gelire ilişkin teşvikler kâr veya zarar tablosunda **ayrı bir kalem veya 'diğer gelir'** gibi genel bir başlık altında ya da **ilgili giderden indirilerek** sunulabilir.",
        'TMS 20 p. 29',
    ),
    # düzey 3
    '0007': patch(
        "Bir işletme devletten 1.000.000 ₺ faizsiz ve 3 yıl sonunda tek seferde geri ödenecek kredi almıştır. Benzer bir kredi için piyasa faiz oranı %10'dur. Kredinin piyasa faizinin altında olmasından doğan ve devlet teşviki olarak ele alınacak fayda yaklaşık kaç ₺'dir?",
        {
            'A': '248.685',
            'B': '751.315',
            'C': '300.000',
            'D': '0',
            'E': '1.000.000',
        },
        'A',
        "TMS 20 p. 10A'ya göre **piyasa faiz oranının altındaki devlet kredisinin faydası** devlet teşviki olarak ele alınır; kredi TFRS 9'a göre gerçeğe uygun değerle ölçülür ve fayda, **ilk ölçüm tutarı ile alınan tutar arasındaki farktır**: 1.000.000 − 1.000.000/1,331 ≈ **248.685 ₺**.",
        'TMS 20 p. 10A; TFRS 9',
    ),
    # düzey 3
    '0008': patch(
        "Bir işletme, koşullarına uyamadığı gelire ilişkin bir teşvik için devlete 50.000 ₺ geri ödeme yapacaktır. Bu teşvike ilişkin henüz gelire aktarılmamış ertelenmiş gelir bakiyesi 30.000 ₺'dir. Geri ödemenin kâr veya zarara yansıyan kısmı kaç ₺'dir?",
        {
            'A': '0',
            'B': '30.000',
            'C': '20.000',
            'D': '80.000',
            'E': '50.000',
        },
        'C',
        "TMS 20 p. 32'ye göre geri ödenen teşvik **muhasebe tahmini değişikliği** olarak ele alınır; gelire ilişkin teşvikin geri ödemesi önce **ertelenmiş gelirden** mahsup edilir, aşan kısım hemen gider yazılır: 50.000 − 30.000 = **20.000 ₺**.",
        'TMS 20 p. 32',
    ),
    # düzey 2
    '0009': patch(
        "Bir işletme finansal tablolarında devlet teşviklerine ilişkin açıklamalarını hazırlamaktadır. TMS 20'ye göre aşağıdakilerden hangisinin açıklanması istenmez?",
        {
            'A': 'Uygulanan muhasebe politikası',
            'B': 'Tanınan teşviklere ilişkin yerine getirilmemiş koşullar',
            'C': 'Teşviki veren kamu görevlilerinin adları',
            'D': 'Tanınan teşviklerin niteliği ve kapsamı',
            'E': 'Sunum yöntemi',
        },
        'C',
        "TMS 20 p. 39'a göre işletme; teşviklere ilişkin **muhasebe politikasını ve sunum yöntemini**, tanınan teşviklerin **niteliği ve kapsamını**, doğrudan yararlanılan diğer devlet yardımlarını ve tanınan teşviklere ilişkin **yerine getirilmemiş koşulları ve diğer koşullu durumları** açıklar.",
        'TMS 20 p. 39',
    ),
    # düzey 3
    '0010': patch(
        "Bir işletme 1 Temmuz'da kullanıma aldığı ve 3 yıl yararlı ömürlü bir yazılım altyapısı için 900.000 ₺ teşvik almış ve teşviki ertelenmiş gelir olarak sunmaktadır; itfa doğrusal ve kıst esaslıdır. Hesap dönemi takvim yılıdır. İlk yıl gelire aktarılacak teşvik kaç ₺'dir?",
        {
            'A': '75.000',
            'B': '900.000',
            'C': '100.000',
            'D': '0',
            'E': '150.000',
        },
        'E',
        "TMS 20 p. 17'ye göre teşvik, varlığın itfa giderlerinin tanındığı dönemler boyunca ve aynı oranda gelir yazılır; varlık yılın yarısında kullanıldığından ilk yıl: 900.000 / 3 × 6/12 = **150.000 ₺**.",
        'TMS 20 p. 17',
    ),
    # düzey 2
    '0011': patch(
        'Bir işletme devletten; faaliyet gösterdiği bölgeye yol yapılması, genel ekonomik koşulları iyileştiren altyapı yatırımları ve rakip ürünlere uygulanan gümrük vergileri gibi dolaylı faydalar sağlamaktadır. Bu faydalar hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Devlet teşviki olarak kâr veya zararda tanınır',
            'B': 'Ertelenmiş gelir olarak tanınır',
            'C': 'Varlığın maliyetinden düşülür',
            'D': 'Koşullu varlıktır',
            'E': 'Devlet yardımı kapsamında değildir',
        },
        'E',
        "TMS 20 p. 3 ve 38'e göre devlet yardımı, belirli ölçütleri karşılayan bir işletmeye veya işletme grubuna özgü ekonomik fayda sağlamaya yönelik eylemdir; **altyapı sağlanması veya rekabetçi kısıtlamalar gibi genel ticari koşulları etkileyen dolaylı faydalar** devlet yardımı kapsamında değildir.",
        'TMS 20 p. 3',
    ),
    # düzey 3
    '0012': patch(
        "Bir işletme 1 Nisan'da kullanıma aldığı makine için 240.000 ₺ teşvik almış ve ertelenmiş gelir olarak sunmaktadır; makinenin yararlı ömrü 4 yıldır ve kıst amortisman uygulanır. Hesap dönemi takvim yılıdır. İlk yıl gelire aktarılacak teşvik kaç ₺'dir?",
        {
            'A': '90.000',
            'B': '75.000',
            'C': '240.000',
            'D': '45.000',
            'E': '60.000',
        },
        'D',
        'Teşvik amortisman oranında gelire aktarılır: 240.000 / 4 × 9/12 = **45.000 ₺**.',
        'TMS 20 p. 17',
    ),
    # düzey 3
    '0013': patch(
        "Bir işletme yeni istihdam ettiği personelin brüt ücretinin %30'unun bir yıl boyunca devlet tarafından karşılanacağı bir teşvikten yararlanmaktadır. Bu personele her ay 50.000 ₺ ücret tahakkuk etmiştir ve koşullar sağlanmıştır. Yıllık teşvik geliri kaç ₺'dir?",
        {
            'A': '270.000',
            'B': '180.000',
            'C': '420.000',
            'D': '600.000',
            'E': '345.000',
        },
        'B',
        'Teşvik, karşıladığı ücret giderleriyle aynı dönemde gelir yazılır: 50.000 × 12 × %30 = **180.000 ₺**.',
        'TMS 20 p. 12, 20',
    ),
    # düzey 3
    '0014': patch(
        "Bir işletme bir makine için aldığı 200.000 ₺ teşviki ertelenmiş gelir olarak sunmuştur; ertelenmiş gelir bakiyesi 120.000 ₺ iken koşul ihlali nedeniyle teşvikin tamamı geri ödenecektir. Geri ödeme yılında kâr veya zarara yansıyacak gider kaç ₺'dir?",
        {
            'A': '120.000',
            'B': '320.000',
            'C': '200.000',
            'D': '80.000',
            'E': '0',
        },
        'D',
        "TMS 20 p. 32'ye göre varlıkla ilgili teşvikin geri ödemesi **ertelenmiş gelir bakiyesi azaltılarak** kaydedilir; önceki dönemlerde gelire aktarılan kısım hemen gider yazılır: 200.000 − 120.000 = **80.000 ₺**.",
        'TMS 20 p. 32',
    ),
    # düzey 3
    '0015': patch(
        "Bir işletmenin faizsiz devlet kredisinden doğan ve teşvik olarak ele alınan fayda 248.685 ₺'dir. Kredi, iki yıl boyunca eşit tutarda gerçekleşecek AR-GE giderlerini finanse etmek koşuluyla verilmiştir. Birinci yıl gelire aktarılacak teşvik yaklaşık kaç ₺'dir?",
        {
            'A': '82.896',
            'B': '0',
            'C': '248.685',
            'D': '82.895',
            'E': '124.343',
        },
        'E',
        "TMS 20 p. 10A ve 12'ye göre kredi faydası, teşvikin **karşılamayı amaçladığı maliyetlerin** tanındığı dönemlerde sistematik biçimde gelire aktarılır: 248.685 / 2 ≈ **124.343 ₺**.",
        'TMS 20 p. 10A, 12',
    ),
    # düzey 2
    '0016': patch(
        "Kredi verenin belirli koşullar altında geri ödemesinden vazgeçmeyi üstlendiği krediler TMS 20'de nasıl adlandırılır?",
        {
            'A': 'Devlet tahvilleri',
            'B': 'Koşullu borçlar',
            'C': 'Geri ödenmeyen krediler',
            'D': 'Faizsiz krediler',
            'E': 'Piyasa faizinin altındaki sübvansiyonlu krediler',
        },
        'C',
        "TMS 20 p. 3'e göre **geri ödenmeyen krediler**, kredi verenin belirli koşullar altında geri ödemeden vazgeçmeyi üstlendiği kredilerdir; koşullara uyulacağına dair makul güvence oluşunca teşvik olarak ele alınır (p. 10).",
        'TMS 20 p. 3',
    ),
    # düzey 3
    '0017': patch(
        'Bir işletme, yıl içinde gerçekleştirdiği ihracat nedeniyle hak kazandığı ve koşullarını yıl sonunda tamamen sağladığı 150.000 ₺ ihracat desteğinin ödemesini gelecek yılın mart ayında alacaktır; destek geçmişte oluşan maliyetleri karşılamaktadır. Bu destek hangi yıl gelir yazılır?',
        {
            'A': 'Gelir yazılmaz',
            'B': 'Nakdin alındığı yıl',
            'C': 'İki yıla eşit olarak',
            'D': 'Hak kazanılan yıl',
            'E': 'Gelecek beş yıla',
        },
        'D',
        "TMS 20 p. 20 ve 22'ye göre geçmiş maliyetleri karşılayan teşvik **alacak hâline geldiği dönemde** gelir yazılır; koşullar yıl sonunda sağlandığından teşvik alacağı ve geliri o yıl tanınır, nakdin sonra alınması önemli değildir.",
        'TMS 20 p. 20, 22',
    ),
    # düzey 2
    '0018': patch(
        "Bir işletme, amortismana tabi bir tesis için aldığı teşviki ertelenmiş gelir olarak sunmaktadır. TMS 20'ye göre bu teşvik hangi dönem boyunca sistematik esasla gelire aktarılır?",
        {
            'A': 'Vergi mevzuatındaki süre boyunca',
            'B': 'Kredi vadesi boyunca',
            'C': 'Teşvikin tahsil edildiği yılda',
            'D': 'Varlığın yararlı ömrü boyunca',
            'E': 'Beş yıl boyunca',
        },
        'D',
        "TMS 20 p. 17 ve 26'ya göre varlıklara ilişkin teşvik, ertelenmiş gelir yönteminde **varlığın yararlı ömrü boyunca** sistematik esasla, amortisman giderleriyle aynı oranda gelire aktarılır.",
        'TMS 20 p. 17, 26',
    ),
    # düzey 3
    '0019': patch(
        'Aşağıdakilerden hangileri doğrudur?\n\nI. Yatırım vergi indirimi TMS 20 kapsamındadır\n\nII. Piyasa faizinin altındaki devlet kredisinin faydası teşvik olarak ele alınır\n\nIII. Geçmiş zararları karşılayan teşvik alacak hâline geldiği dönemde gelir yazılır',
        {
            'A': 'I, II ve III',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'Yalnız II',
            'E': 'Yalnız III',
        },
        'C',
        "TMS 20 p. 10A'ya göre piyasa faizinin altındaki kredinin faydası teşviktir (II); p. 20'ye göre geçmiş zararları karşılayan teşvik alacak hâline geldiğinde gelir yazılır (III). p. 2(b)'ye göre yatırım vergi indirimi **TMS 20 kapsamı dışındadır** (I yanlış).",
        'TMS 20 p. 2, 10A, 20',
    ),
    # düzey 3
    '0020': patch(
        'Varlıkla ilgili teşviklerin sunumuna ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Varlıktan indirim yönteminde teşvik azaltılmış amortisman yoluyla gelire yansır\n\nII. Parasal olmayan teşvik nominal tutarla kaydedilebilir\n\nIII. Ertelenmiş gelir yönteminde teşvikin tamamı ilk yıl gelir yazılır',
        {
            'A': 'Yalnız I',
            'B': 'I, II ve III',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'Yalnız II',
        },
        'C',
        "TMS 20 p. 27'ye göre varlıktan indirimde teşvik azaltılmış amortismanla gelire yansır (I); p. 23'e göre parasal olmayan teşvik nominal tutarla kaydedilebilir (II). p. 26'ya göre ertelenmiş gelir **yararlı ömür boyunca sistematik esasla** gelire aktarılır (III yanlış).",
        'TMS 20 p. 23-24, 26-27',
    ),
    # düzey 2
    '0021': patch(
        'Bir tarım işletmesi, gerçeğe uygun değerinden satış maliyetleri düşülerek ölçtüğü süt ineklerine ilişkin olarak devletten koşulsuz bir hibe almıştır. Bu hibe hangi standarda göre muhasebeleştirilir?',
        {
            'A': 'TMS 41',
            'B': 'TMS 12',
            'C': 'TFRS 15',
            'D': 'TMS 16',
            'E': 'TMS 20',
        },
        'A',
        "TMS 20 p. 2(d)'ye göre **TMS 41 kapsamındaki devlet teşvikleri** TMS 20'nin kapsamı dışındadır. Satış maliyetleri düşülmüş GUD ile ölçülen biyolojik varlıklara ilişkin koşulsuz teşvik, TMS 41 p. 34'e göre alacak hâline geldiğinde kâr veya zarara yansıtılır.",
        'TMS 20 p. 2(d); TMS 41 p. 34-35',
    ),
    # düzey 2
    '0022': patch(
        'Bir işletme, 3 yıl boyunca en az 50 kişi istihdam etme koşuluyla 600.000 ₺ teşvik almıştır. Yönetim koşula uyacağından ve teşvikin geri istenmeyeceğinden makul güvence duymaktadır. Teşvik ne zaman finansal tablolara alınır?',
        {
            'A': 'Koşul süresinin sonunda kesinleştiğinde',
            'B': 'Makul güvence sağlandığında',
            'C': 'Denetçi onayladığında',
            'D': 'Nakit alındığında',
            'E': 'Üç yıl dolduğunda',
        },
        'B',
        "TMS 20 p. 7'ye göre devlet teşvikleri, işletmenin **teşvike ilişkin koşullara uyacağına** ve **teşvikin alınacağına** ilişkin **makul bir güvence** oluştuğunda finansal tablolara alınır.",
        'TMS 20 p. 7',
    ),
    # düzey 3
    '0023': patch(
        "Bir işletme 1.000.000 ₺'ye bir makine almış ve bu alım için devletten 200.000 ₺ teşvik almıştır. Makinenin yararlı ömrü 5 yıl, kalıntı değeri sıfırdır; doğrusal amortisman uygulanır. İşletme teşviki ertelenmiş gelir olarak sunmaktadır. Her yıl kâr veya zarara yansıtılacak teşvik geliri kaç ₺'dir?",
        {
            'A': '200.000',
            'B': '100.000',
            'C': '0',
            'D': '40.000',
            'E': '160.000',
        },
        'D',
        "TMS 20 p. 17'ye göre amortismana tabi varlıklarla ilgili teşvikler, **varlığın amortisman giderlerinin tanındığı dönemler boyunca ve aynı oranda** gelir yazılır: 200.000 / 5 = **40.000 ₺**.",
        'TMS 20 p. 17, 24-26',
    ),
    # düzey 2
    '0024': patch(
        "Varlıklara ilişkin devlet teşviklerinin finansal durum tablosunda sunumunda TMS 20'nin izin verdiği iki yöntem hangisidir?",
        {
            'A': 'Ertelenmiş gelir veya varlıktan indirim',
            'B': 'Kısa vadeli borç veya uzun vadeli karşılık olarak',
            'C': 'Hasılat veya diğer gelir',
            'D': 'Özkaynak veya DKG',
            'E': 'Sermaye veya yedek',
        },
        'A',
        "TMS 20 p. 24'e göre varlıklara ilişkin teşvikler finansal durum tablosunda **ertelenmiş gelir olarak** veya **varlığın defter değerinden düşülerek** sunulur.",
        'TMS 20 p. 24',
    ),
    # düzey 3
    '0025': patch(
        "Bir işletme, bu yıl işe aldığı engelli personelin ücretlerinin %20'sinin devlet tarafından karşılanacağı bir teşvikten yararlanmaktadır. Yıl içinde bu personele 500.000 ₺ ücret tahakkuk etmiş ve teşvik koşulları sağlanmıştır. Bu yıl kâr veya zarara yansıyacak teşvik geliri kaç ₺'dir?",
        {
            'A': '500.000',
            'B': '400.000',
            'C': '50.000',
            'D': '100.000',
            'E': '0',
        },
        'D',
        "TMS 20 p. 12'ye göre teşvikler, karşılayacağı maliyetlerin gider yazıldığı dönemde gelir yazılır: 500.000 × %20 = **100.000 ₺**.",
        'TMS 20 p. 12, 20',
    ),
    # düzey 3
    '0026': patch(
        "Bir işletme 1 Ocak'ta, gelecek 4 yıl boyunca her yıl eşit tutarda katlanacağı personel eğitim giderlerini karşılamak üzere 480.000 ₺ teşvik almıştır; koşullara uyulacağına dair makul güvence vardır. Birinci yıl kâr veya zarara yansıyacak teşvik geliri kaç ₺'dir?",
        {
            'A': '360.000',
            'B': '480.000',
            'C': '120.000',
            'D': '240.000',
            'E': '0',
        },
        'C',
        "TMS 20 p. 12'ye göre teşvik, ilgili maliyetlerin gider yazıldığı dönemler boyunca sistematik biçimde gelir yazılır: 480.000 / 4 = **120.000 ₺**; kalan tutar ertelenmiş gelir olarak izlenir.",
        'TMS 20 p. 12',
    ),
    # düzey 2
    '0027': patch(
        'Bir işletme devletten, 5 yıl boyunca bölgede faaliyet göstermesi hâlinde geri ödenmesi istenmeyecek 400.000 ₺ kredi almıştır. Beş yılın sonunda koşul yerine getirilmiş ve kredinin geri ödenmeyeceği kesinleşmiştir. Bu kredi hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sermayeye eklenir',
            'B': 'Devlet teşviki olarak ele alınır',
            'C': 'Hasılat olarak tanınır',
            'D': 'Koşullu borçtur',
            'E': 'Kredi borcu olarak kalmaya devam eder ve itfa edilir',
        },
        'B',
        "TMS 20 p. 10'a göre devletten alınan ve **geri ödenmemesi belirli koşullara bağlı** krediler, işletmenin bu koşulları karşılayacağına dair makul güvence oluştuğunda **devlet teşviki** olarak ele alınır.",
        'TMS 20 p. 10',
    ),
    # düzey 3
    '0028': patch(
        "Bir işletme 1.000.000 ₺'lik makine için aldığı 200.000 ₺ teşviki makinenin defter değerinden düşerek sunmuştur; yararlı ömür 5 yıldır. 2. yılın sonunda koşul ihlali nedeniyle teşvikin tamamı geri ödenecektir. Geri ödeme yılında hemen gider yazılacak kümülatif ek amortisman kaç ₺'dir?",
        {
            'A': '0',
            'B': '200.000',
            'C': '40.000',
            'D': '80.000',
            'E': '120.000',
        },
        'D',
        "TMS 20 p. 32'ye göre varlıkla ilgili teşvikin geri ödemesi varlığın defter değeri artırılarak veya ertelenmiş gelir azaltılarak kaydedilir; **teşvik olmasaydı gider yazılacak kümülatif ek amortisman hemen gider yazılır**: 40.000 × 2 = **80.000 ₺**.",
        'TMS 20 p. 32',
    ),
    # düzey 3
    '0029': patch(
        'Bir teşvik, finansal tablolara alındıktan sonra koşullara uyulmaması nedeniyle geri ödenecek hâle gelmiştir; teşvike konu makine de değer düşüklüğü belirtisi göstermektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': "Oluşan koşullu borç TMS 37'ye göre ele alınır",
            'B': 'Makine için değer düşüklüğü değerlendirilebilir',
            'C': 'Geri ödeme geçmiş yılların tablolarını düzeltir',
            'D': 'Kümülatif ek amortisman hemen gider yazılır',
            'E': 'Geri ödeme tahmin değişikliğidir',
        },
        'C',
        "TMS 20 p. 11 ve 32-33'e göre tanınan teşvike ilişkin oluşan koşullu borç TMS 37'ye göre ele alınır; geri ödeme **tahmin değişikliğidir**, geçmiş tablolar düzeltilmez; varlıkla ilgili teşvikin geri ödemesi varlığın değer düşüklüğüne uğramış olabileceğini gösterebilir.",
        'TMS 20 p. 11, 32-33',
    ),
    # düzey 2
    '0030': patch(
        "TMS 20'nin devlet teşvikleri için benimsediği yaklaşımla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'TMS 20 gelir yaklaşımını benimser',
            'B': 'Teşvikler hissedar katkısı gibi doğrudan özkaynağa alınır',
            'C': 'Teşvik, ilgili maliyetlerle eşleştirilerek gelire aktarılır',
            'D': 'Teşvik, hissedarlar dışındaki bir kaynaktan elde edilir',
            'E': 'Teşvik, koşullara uyumla kazanıldığından gelir sayılır',
        },
        'B',
        'TMS 20.13-16: standart gelir yaklaşımını benimser. Teşvik hissedarlar dışındaki bir kaynaktan elde edildiği ve koşullara uyumla kazanıldığı için doğrudan özkaynağa alınmaz; karşılamayı amaçladığı maliyetlerle eşleştirilerek sistematik biçimde kâr veya zarara yansıtılır.',
        'TMS 20 p. 13-14',
    ),
    # düzey 3
    '0031': patch(
        "Bir işletme 750.000 ₺'lik bir makine için 150.000 ₺ teşvik almış ve ertelenmiş gelir olarak sunmuştur; yararlı ömür 6 yıl, kalıntı değer sıfırdır. Üçüncü yılın sonunda ertelenmiş teşvik geliri bakiyesi kaç ₺'dir?",
        {
            'A': '100.000',
            'B': '75.000',
            'C': '25.000',
            'D': '375.000',
            'E': '150.000',
        },
        'B',
        'Yıllık gelire aktarım 150.000 / 6 = 25.000 ₺; üç yıl sonunda bakiye 150.000 − 3 × 25.000 = **75.000 ₺**.',
        'TMS 20 p. 26',
    ),
    # düzey 3
    '0032': patch(
        "Bir işletme 500.000 ₺'lik bir makine için 100.000 ₺ teşvik almıştır; makine %40 oranla azalan bakiyeler yöntemiyle amortismana tabi tutulmaktadır. Teşvik ertelenmiş gelir olarak sunulmaktadır. İlk yıl gelire aktarılacak teşvik kaç ₺'dir?",
        {
            'A': '80.000',
            'B': '200.000',
            'C': '60.000',
            'D': '100.000',
            'E': '40.000',
        },
        'E',
        "TMS 20 p. 17'ye göre teşvik, **amortisman giderlerinin tanındığı oranda** gelire aktarılır; ilk yıl amortisman maliyetin %40'ı olduğundan teşvikin de %40'ı gelir yazılır: **40.000 ₺**.",
        'TMS 20 p. 17',
    ),
    # düzey 3
    '0033': patch(
        "Bir işletmenin yatırım kredisinin dönem faizi 80.000 ₺'dir; devlet bu faizin %50'sini karşılayan koşulsuz bir faiz desteği vermiştir. İşletme gelire ilişkin teşvikleri ilgili giderden indirerek sunmaktadır. Kâr veya zarar tablosunda gösterilecek net faiz gideri kaç ₺'dir?",
        {
            'A': '120.000',
            'B': '20.000',
            'C': '80.000',
            'D': '0',
            'E': '40.000',
        },
        'E',
        "TMS 20 p. 29'a göre gelire ilişkin teşvik ilgili giderden indirilerek sunulabilir: 80.000 − 40.000 = **40.000 ₺**.",
        'TMS 20 p. 12, 29',
    ),
    # düzey 3
    '0034': patch(
        "Bir işletme devletten 500.000 ₺ faizsiz ve 2 yıl sonunda tek seferde geri ödenecek kredi almıştır; piyasa faiz oranı %8'dir. Devlet teşviki olarak ele alınacak fayda yaklaşık kaç ₺'dir?",
        {
            'A': '71.331',
            'B': '428.669',
            'C': '102.662',
            'D': '500.000',
            'E': '80.000',
        },
        'A',
        'Kredinin gerçeğe uygun değeri 500.000 / 1,08² ≈ 428.669 ₺; fayda, alınan tutar ile ilk ölçüm arasındaki fark: ≈ **71.331 ₺**.',
        'TMS 20 p. 10A',
    ),
    # düzey 2
    '0035': patch(
        "Temel koşulu, teşvik almaya hak kazanan işletmenin uzun vadeli varlıklar satın alması, inşa etmesi veya başka şekilde edinmesi olan devlet teşvikleri TMS 20'de nasıl adlandırılır?",
        {
            'A': 'Devlet yardımları',
            'B': 'Varlıklara ilişkin teşvikler',
            'C': 'Vergi teşvikleri',
            'D': 'Gelire ilişkin teşvikler',
            'E': 'Geri ödenmeyen krediler',
        },
        'B',
        "TMS 20 p. 3'e göre **varlıklara ilişkin teşvikler**, temel koşulu teşvik almaya hak kazanan işletmenin uzun vadeli varlıklar satın alması, inşa etmesi veya edinmesi olan teşviklerdir.",
        'TMS 20 p. 3',
    ),
    # düzey 2
    '0036': patch(
        'Bir kamu kurumu, bir işletmenin sermaye artırımına katılarak %20 oranında ortak olmuştur. Bu işlem TMS 20 bakımından nasıl değerlendirilir?',
        {
            'A': 'TMS 20 kapsamı dışındadır',
            'B': 'Sermayeye katılım şeklindeki devlet teşvikidir',
            'C': 'Gelire ilişkin teşviktir',
            'D': 'Ertelenmiş gelirdir',
            'E': 'Geri ödenmeyen kredidir',
        },
        'A',
        "TMS 20 p. 2(c)'ye göre **devletin işletmeye ortak olması** TMS 20'nin kapsamı dışındadır; ortaklık payı özkaynak katkısı olarak muhasebeleştirilir.",
        'TMS 20 p. 2',
    ),
    # düzey 2
    '0037': patch(
        'Bir işletme varlıkla ilgili teşviki makinenin maliyetinden düşerek sunmaktadır. Nakit akış tablosunda makine alımı ve teşvik tahsilatı nasıl gösterilir?',
        {
            'A': 'Net tutarla tek satırda',
            'B': 'Gösterilmez',
            'C': 'Finansman faaliyetinde net',
            'D': 'Brüt olarak ayrı ayrı',
            'E': 'Dipnotta',
        },
        'D',
        "TMS 20 p. 28'e göre teşvik finansal durum tablosunda varlıktan düşülerek sunulsa da, nakit akış tablosunda varlık alımı ve teşvik tahsilatı **ayrı kalemler olarak brüt** gösterilir ve bu durum açıklanır.",
        'TMS 20 p. 28',
    ),
    # düzey 3
    '0038': patch(
        'Bir işletme varlıkla ilgili bir teşvik için ertelenmiş gelir yöntemi ile varlıktan indirim yöntemini karşılaştırmaktadır.\n\nİki yöntemle ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ertelenmiş gelir yönteminde varlık brüt tutarıyla gösterilir',
            'B': 'Varlıktan indirim yönteminde amortisman daha düşük hesaplanır',
            'C': 'İki yöntemde finansal durum tablosundaki sunum farklıdır',
            'D': 'Varlıktan indirim yönteminde teşvik amortisman yoluyla kâra yansır',
            'E': 'Ertelenmiş gelir yönteminde dönem kârları daha yüksek çıkar',
        },
        'E',
        'TMS 20.24-27: ertelenmiş gelir yönteminde varlık brüt tutarla gösterilir ve teşvik sistematik olarak gelire aktarılır; varlıktan indirim yönteminde teşvik varlığın defter değerinden düşülür, daha düşük amortisman yoluyla kâra yansır. Sunum farklı olsa da her dönemin kârı aynıdır.',
        'TMS 20 p. 24-27',
    ),
    # düzey 2
    '0039': patch(
        'Aşağıdakilerden hangileri doğrudur?\n\nI. Amortismana tabi varlık teşviki amortisman oranında gelire aktarılır\n\nII. Gelire ilişkin teşvik ilgili giderden indirilerek sunulabilir\n\nIII. Koşula bağlı arsa teşviki koşulun maliyetlerinin gider yazıldığı dönemlere yayılır',
        {
            'A': 'I ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'II ve III',
        },
        'D',
        "TMS 20 p. 17'ye göre amortisman oranında gelire aktarım (I), p. 29'a göre giderden indirim (II) ve p. 18'e göre koşula bağlı arsa teşvikinin yayılması (III) doğrudur.",
        'TMS 20 p. 17-18, 29',
    ),
    # düzey 3
    '0040': patch(
        'Aşağıdakilerden hangileri doğrudur?\n\nI. Teşvikin nakit alınması koşullara uyulduğunu tek başına göstermez\n\nII. Geri ödenen teşvik önceki dönem hatası olarak düzeltilir\n\nIII. Değer biçilemeyen devlet yardımları finansal tablolara alınır',
        {
            'A': 'Yalnız I',
            'B': 'II ve III',
            'C': 'I ve III',
            'D': 'Yalnız II',
            'E': 'I ve II',
        },
        'A',
        "TMS 20 p. 8'e göre nakit alınması koşullara uyulduğunu göstermez (I). p. 32'ye göre geri ödeme **tahmin değişikliğidir** (II yanlış); p. 34-36'ya göre değer biçilemeyen yardımlar **tablolara alınmaz, açıklanır** (III yanlış).",
        'TMS 20 p. 8, 32, 34',
    ),
    # düzey 2
    '0041': patch(
        "Devletin bir işletmeye, işletmenin faaliyetleriyle ilgili geçmişte veya gelecekte belirli koşullara uyması karşılığında kaynak aktarması şeklindeki yardım TMS 20'de hangi kavramla ifade edilir?",
        {
            'A': 'Devlet teşviki',
            'B': 'Devlet yardımı',
            'C': 'Sermaye katkısı',
            'D': 'Koşullu varlık',
            'E': 'Vergi avantajı',
        },
        'A',
        "TMS 20 p. 3'e göre **devlet teşvikleri**, işletmenin faaliyetlerine ilişkin geçmişte veya gelecekte belirli koşullara uyması karşılığında devletin işletmeye kaynak aktarması şeklindeki yardımlardır; makul biçimde değer biçilemeyen yardımlar bu tanıma girmez.",
        'TMS 20 p. 3',
    ),
    # düzey 3
    '0042': patch(
        'Bir işletme bir teşvikin tutarını nakit olarak tahsil etmiştir; ancak teşvikin koşullarından biri olan ihracat hedefine ulaşacağına ilişkin makul güvence bulunmamaktadır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Alınan tutar yükümlülük olarak izlenebilir',
            'B': 'Teşvikin alınması koşullara uyulduğunu göstermez',
            'C': 'Makul güvence olmadan gelir tanınmaz',
            'D': 'Koşul ihlali hâlinde geri ödeme doğabilir',
            'E': 'Nakit alındığı için teşvik gelir olarak tanınır',
        },
        'E',
        "TMS 20 p. 8'e göre **teşvikin alınması tek başına, teşvike ilişkin koşulların yerine getirildiğine veya getirileceğine dair kesin kanıt sağlamaz**; makul güvence oluşuncaya kadar teşvik gelir olarak tanınmaz.",
        'TMS 20 p. 8',
    ),
    # düzey 2
    '0043': patch(
        "Bir işletme, aldığı yatırım teşvikini doğrudan özkaynakta 'teşvik fonu' olarak göstermek istemektedir. TMS 20'ye göre devlet teşvikleri nasıl muhasebeleştirilir?",
        {
            'A': 'Doğrudan özkaynakta',
            'B': 'Sermaye olarak',
            'C': 'Diğer kapsamlı gelirde',
            'D': 'Kâr veya zararda',
            'E': 'Yasal yedek olarak',
        },
        'D',
        "TMS 20 p. 12-13 ve 15'e göre devlet teşvikleri **gelir yaklaşımıyla**, karşılayacağı maliyetlerin gider olarak tanındığı dönemler boyunca sistematik bir şekilde **kâr veya zararda** muhasebeleştirilir; doğrudan özkaynağa alınmaz.",
        'TMS 20 p. 13, 15',
    ),
    # düzey 3
    '0044': patch(
        "Bir işletme 1.000.000 ₺'lik makine için aldığı 200.000 ₺ teşviki ertelenmiş gelir olarak sunmaktadır; makinenin yararlı ömrü 5 yıldır. İkinci yılın sonunda finansal durum tablosundaki ertelenmiş teşvik geliri bakiyesi kaç ₺'dir?",
        {
            'A': '200.000',
            'B': '160.000',
            'C': '120.000',
            'D': '80.000',
            'E': '600.000',
        },
        'C',
        "TMS 20 p. 26'ya göre ertelenmiş gelir yönteminde teşvik, varlığın yararlı ömrü boyunca sistematik esasla gelire aktarılır: 200.000 − 2 × 40.000 = **120.000 ₺**.",
        'TMS 20 p. 26',
    ),
    # düzey 2
    '0045': patch(
        "Bir işletmeye devlet tarafından gerçeğe uygun değeri 500.000 ₺ olan bir arazi, fabrika kurulması amacıyla bedelsiz tahsis edilmiştir. TMS 20'ye göre bu parasal olmayan teşvik hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Özkaynakta gösterilir',
            'B': 'Finansal tablolara alınmaz',
            'C': 'Hemen gelir yazılır',
            'D': 'Maliyeti sıfır olduğundan açıklanmaz',
            'E': 'GUD veya nominal tutarla ölçülebilir',
        },
        'E',
        "TMS 20 p. 23'e göre parasal olmayan varlık şeklindeki teşviklerde genellikle varlığın **gerçeğe uygun değeri** belirlenir ve hem teşvik hem varlık bu değerle muhasebeleştirilir; alternatif olarak varlık ve teşvik **nominal tutarla** kaydedilebilir.",
        'TMS 20 p. 23',
    ),
    # düzey 3
    '0046': patch(
        "Doğal afet nedeniyle faaliyetleri duran bir işletmeye, geçmişte uğradığı zararların karşılanması için devlet 300.000 ₺ koşulsuz destek vermiştir; destek bu yıl alacak hâline gelmiştir ve gelecekte ilgili bir maliyet yoktur. Bu yıl kâr veya zarara yansıyacak gelir kaç ₺'dir?",
        {
            'A': '60.000',
            'B': '300.000',
            'C': '30.000',
            'D': '150.000',
            'E': '0',
        },
        'B',
        "TMS 20 p. 20'ye göre **daha önce oluşan gider veya zararları karşılamak için** ya da gelecekte ilgili bir maliyet olmaksızın **acil mali destek** amacıyla verilen teşvik, **alacak hâline geldiği dönemde** tamamen gelir yazılır: **300.000 ₺**.",
        'TMS 20 p. 20-21',
    ),
    # düzey 3
    '0047': patch(
        "Bir işletme devletten 1.000.000 ₺ faizsiz ve 3 yıl vadeli kredi almıştır; piyasa faiz oranı %10'dur. Kredi, ilk muhasebeleştirmede finansal durum tablosunda yaklaşık kaç ₺ ile ölçülür?",
        {
            'A': '248.685',
            'B': '900.000',
            'C': '751.315',
            'D': '1.000.000',
            'E': '909.091',
        },
        'C',
        "TMS 20 p. 10A ve TFRS 9'a göre kredi ilk muhasebeleştirmede **gerçeğe uygun değeriyle**, yani piyasa faiz oranıyla iskonto edilmiş bugünkü değeriyle ölçülür: 1.000.000 / 1,1³ ≈ **751.315 ₺**; fark teşvik olarak ele alınır.",
        'TMS 20 p. 10A',
    ),
    # düzey 2
    '0048': patch(
        "Bir işletmenin daha önce aldığı bir teşvikin koşulları ihlal edilmiş ve teşvikin geri ödenmesi gerekmiştir. TMS 20'ye göre bu geri ödeme nasıl nitelendirilir?",
        {
            'A': 'Muhasebe tahmini değişikliği',
            'B': 'Politika değişikliği',
            'C': 'Önceki dönem hatası',
            'D': 'Olağanüstü kalem',
            'E': 'Sonraki olay',
        },
        'A',
        "TMS 20 p. 32'ye göre geri ödenmesi gereken devlet teşviki, **muhasebe tahmininde değişiklik** olarak (TMS 8) muhasebeleştirilir; geçmiş dönemler düzeltilmez.",
        'TMS 20 p. 32',
    ),
    # düzey 2
    '0049': patch(
        'Bir işletmeye bir dizi mali ve mali olmayan yükümlülükle birlikte tek bir teşvik paketi verilmiştir; paket hem makine alımını hem de 3 yıllık personel giderlerini karşılamaktadır. Teşvikin gelire aktarılma esası nasıl belirlenir?',
        {
            'A': 'Tamamı özkaynağa alınarak',
            'B': 'Tamamı alındığında gelir yazılarak',
            'C': 'Tamamı makine ömrüne yayılarak',
            'D': 'Maliyet ve yükümlülüklerin oluştuğu koşullara göre ayrıştırılarak',
            'E': 'Tamamı 3 yıla eşit dağıtılarak',
        },
        'D',
        "TMS 20 p. 19'a göre teşvikler bazen bir dizi mali ve mali olmayan yükümlülük karşılığında paket olarak verilir; bu durumda **teşvike ilişkin maliyet ve yükümlülüklerin oluştuğu koşulların belirlenmesi** gerekir ve teşvikin bölümleri farklı esaslarla dağıtılabilir.",
        'TMS 20 p. 19',
    ),
    # düzey 3
    '0050': patch(
        "Bir işletmeye 400.000 ₺'lik bir teşvik verilmiştir: 250.000 ₺'si bu yıl gerçekleşen ve koşulları sağlanan AR-GE giderlerini karşılamakta, 150.000 ₺'si ise gelecek yıl sağlanıp sağlanamayacağı konusunda makul güvence bulunmayan bir ihracat koşuluna bağlıdır. Bu yıl kâr veya zarara yansıyacak teşvik geliri kaç ₺'dir?",
        {
            'A': '0',
            'B': '250.000',
            'C': '400.000',
            'D': '150.000',
            'E': '200.000',
        },
        'B',
        "TMS 20 p. 7'ye göre teşvik ancak koşullara uyulacağına dair **makul güvence** varsa tanınır; p. 12'ye göre ilgili maliyetlerle eşleştirilir. Bu yıl koşulu sağlanan AR-GE kısmı, **250.000 ₺** gelir yazılır.",
        'TMS 20 p. 7, 12',
    ),
    # düzey 3
    '0051': patch(
        "Bir işletme 750.000 ₺'lik makine için aldığı 150.000 ₺ teşviki makinenin defter değerinden düşmüştür; yararlı ömür 6 yıl, kalıntı değer sıfırdır. Üçüncü yılın sonunda makinenin net defter değeri kaç ₺'dir?",
        {
            'A': '375.000',
            'B': '450.000',
            'C': '300.000',
            'D': '600.000',
            'E': '225.000',
        },
        'C',
        'Net maliyet 750.000 − 150.000 = 600.000 ₺; yıllık amortisman 100.000 ₺. Üç yıl sonunda net defter değeri 600.000 − 3 × 100.000 = **300.000 ₺**.',
        'TMS 20 p. 27',
    ),
    # düzey 3
    '0052': patch(
        "Bir işletme toplam 100.000 birim üretim kapasiteli bir makine için 120.000 ₺ teşvik almıştır; makine üretim miktarı yöntemiyle amortismana tabi tutulmaktadır. İlk yıl 30.000 birim üretilmiştir. İlk yıl gelire aktarılacak teşvik kaç ₺'dir?",
        {
            'A': '18.000',
            'B': '36.000',
            'C': '24.000',
            'D': '84.000',
            'E': '120.000',
        },
        'B',
        'Teşvik amortisman oranında gelire aktarılır; üretim miktarı yönteminde oran üretim payıdır: 120.000 × 30.000 / 100.000 = **36.000 ₺**.',
        'TMS 20 p. 17',
    ),
    # düzey 3
    '0053': patch(
        "Bir işletme iki yıllık bir eğitim programının maliyetlerini karşılamak için 200.000 ₺ teşvik almıştır. Program giderlerinin %70'i birinci yılda, kalanı ikinci yılda oluşmuştur. Birinci yıl gelire aktarılacak teşvik kaç ₺'dir?",
        {
            'A': '200.000',
            'B': '140.000',
            'C': '100.000',
            'D': '0',
            'E': '60.000',
        },
        'B',
        "TMS 20 p. 12'ye göre teşvik, **karşılayacağı maliyetlerin gider yazıldığı dönemlerle eşleştirilir**; giderlerin %70'i ilk yılda olduğundan: 200.000 × %70 = **140.000 ₺**.",
        'TMS 20 p. 12',
    ),
    # düzey 3
    '0054': patch(
        "Bir işletme devletten 1.000.000 ₺ faizsiz ve 3 yıl vadeli kredi almış; kredi ilk muhasebeleştirmede piyasa faizi %10 ile 751.315 ₺ olarak ölçülmüştür. Birinci yıl kredi için tanınacak faiz gideri yaklaşık kaç ₺'dir?",
        {
            'A': '75.131',
            'B': '82.895',
            'C': '0',
            'D': '100.000',
            'E': '37.566',
        },
        'A',
        "Kredi TFRS 9'a göre etkin faiz yöntemiyle itfa edilmiş maliyetle ölçülür; faizsiz olsa da **iskontonun itfası** faiz gideri doğurur: 751.315 × %10 ≈ **75.131 ₺**.",
        'TMS 20 p. 10A; TFRS 9',
    ),
    # düzey 2
    '0055': patch(
        "Bir teşvik, işletmenin herhangi bir uzun vadeli varlık edinmesi koşuluna bağlı değildir; dönemin personel ve eğitim giderlerini karşılamaya yöneliktir. TMS 20'ye göre bu teşvik hangi gruba girer?",
        {
            'A': 'Koşullu varlıklar',
            'B': 'Sermaye katkıları',
            'C': 'Varlıklara ilişkin teşvikler',
            'D': 'Gelire ilişkin teşvikler',
            'E': 'Devlet yardımları',
        },
        'D',
        "TMS 20 p. 3'e göre varlıklara ilişkin teşvikler dışında kalan teşvikler **gelire ilişkin teşviklerdir**.",
        'TMS 20 p. 3',
    ),
    # düzey 3
    '0056': patch(
        'Bir işletme 5 yıl boyunca belirli sayıda çalışanı istihdam etme koşuluyla 1 milyon ₺ nakit teşvik almıştır; ancak sektördeki daralma nedeniyle koşula uyulacağına ilişkin makul güvence bulunmamaktadır. Alınan nakit nasıl izlenir?',
        {
            'A': 'Yükümlülük olarak',
            'B': 'Ertelenmiş vergi varlığı olarak',
            'C': 'Özkaynak olarak',
            'D': 'Diğer gelir olarak',
            'E': 'Hasılat olarak',
        },
        'A',
        "TMS 20 p. 7-8'e göre makul güvence oluşmadan teşvik finansal tablolara (gelir olarak) alınmaz; alınan nakit, koşullar sağlanmazsa geri ödenecek olduğundan **yükümlülük** olarak izlenir.",
        'TMS 20 p. 7-8',
    ),
    # düzey 2
    '0057': patch(
        'Bir işletmeye verilen teşvik, nakit ödeme yerine işletmenin devlete olan bir borcunun silinmesi şeklinde sağlanmıştır. Teşvikin bu şekilde alınması muhasebeleştirme yöntemini nasıl etkiler?',
        {
            'A': 'Teşvik özkaynağa alınır',
            'B': 'Teşvik hasılata eklenir',
            'C': 'Teşvik tanınmaz',
            'D': "Teşvik DKG'ye alınır",
            'E': 'Etkilemez',
        },
        'E',
        "TMS 20 p. 9'a göre teşvikin **alınma şekli**, nakit alınması veya devlete olan borcun azalması, teşvikin muhasebeleştirilme yöntemini etkilemez.",
        'TMS 20 p. 9',
    ),
    # düzey 3
    '0058': patch(
        'Bir işletme bir teşvik paketinin makine alımına ilişkin kısmını ertelenmiş gelir olarak sunmakta, geçmiş yıl zararlarını karşılayan kısmını ise alacak hâline geldiği yıl gelir yazmaktadır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Makine teşviki amortisman oranında gelire aktarılır',
            'B': 'Paketteki unsurlar farklı esaslarla dağıtılabilir',
            'C': 'Geçmiş zararları karşılayan kısım hemen gelir yazılır',
            'D': "Uygulama TMS 20'ye uygundur",
            'E': 'Makine teşviki de alacak hâline geldiği yıl gelir yazılmalıdır',
        },
        'E',
        "TMS 20 p. 17'ye göre varlıkla ilgili teşvik amortisman oranında, p. 20'ye göre geçmiş zararları karşılayan teşvik alacak hâline geldiğinde gelir yazılır; p. 19'a göre paket unsurları farklı esaslarla dağıtılabilir.",
        'TMS 20 p. 17, 20',
    ),
    # düzey 2
    '0059': patch(
        "Aşağıdakilerden hangileri TMS 20'ye göre doğrudur?\n\nI. Teşvik, koşullara uyulacağına dair makul güvence oluştuğunda tanınır\n\nII. Teşvikler doğrudan özkaynakta muhasebeleştirilir\n\nIII. Varlıkla ilgili teşvikler ertelenmiş gelir olarak sunulabilir",
        {
            'A': 'I, II ve III',
            'B': 'Yalnız III',
            'C': 'I ve II',
            'D': 'I ve III',
            'E': 'Yalnız I',
        },
        'D',
        "TMS 20 p. 7'ye göre makul güvence esastır (I); p. 24'e göre ertelenmiş gelir sunumu mümkündür (III). p. 12'ye göre teşvikler **kâr veya zararda** muhasebeleştirilir, doğrudan özkaynağa alınmaz (II yanlış).",
        'TMS 20 p. 7, 12, 24',
    ),
    # düzey 2
    '0060': patch(
        'Devlet yardımlarına ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Ücretsiz teknik danışmanlık gibi değer biçilemeyen yardımlar açıklanabilir\n\nII. Teşviklere ilişkin yerine getirilmemiş koşullar açıklanır\n\nIII. Genel altyapı yatırımlarından doğan dolaylı faydalar devlet teşviki olarak tanınır',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'Yalnız II',
            'D': 'I ve III',
            'E': 'I, II ve III',
        },
        'B',
        "TMS 20 p. 36'ya göre değer biçilemeyen yardımlar açıklanabilir (I); p. 39'a göre yerine getirilmemiş koşullar açıklanır (II). p. 38'e göre genel altyapıdan doğan dolaylı faydalar **devlet yardımı değildir** (III yanlış).",
        'TMS 20 p. 35-36, 39',
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
    print(f"1 paket / {len(PATCHES)} soru ('TMS 20 Devlet Tesvikleri' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
