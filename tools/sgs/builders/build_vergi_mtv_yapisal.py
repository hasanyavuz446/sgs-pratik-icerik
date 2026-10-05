#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Motorlu Tasitlar Vergisi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Vergiye ozgu profille yeniden yazim: konu, tanimlar ve mukellef, istisnalar (7566 ile YIKOB dahil), (I)-(I/A)-(II)-(IV) tarifeleri, elektrikli tasitlarda %25, kasko siniri, mukellefiyetin baslamasi-devir-silinme, tahakkuk ve taksitler, bildirim ve sorumluluk, gider kabul edilmeme. Yila bagli tarife tutari sorulmadi (tutar kokte verildi); 15 hesap sorusu bagimsiz dogrulandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 197 sayili Motorlu Tasitlar Vergisi Kanunu guncel metni (7566 degisikligi dahil; mevzuat.gov.tr)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/vergi_hukuku/mtv.json"
STYLE_REF = 'SGS Vergi Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "mtv-gen-"


def patch(stem, options, answer, solution, ref='197 sayili Motorlu Tasitlar Vergisi Kanunu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 1
    '0001': patch(
        'Aşağıdakilerden hangisi motorlu taşıtlar vergisinin konusuna girmez?',
        {
            'A': 'Sivil hava siciline kayıtlı helikopter',
            'B': 'Özel amaçla kullanılan motorlu yat',
            'C': 'Trafikte tescilli kamyonet',
            'D': 'Trafikte tescilli motosiklet',
            'E': 'Trafikte tescilli arazi taşıtı',
        },
        'B',
        "m. 1'e göre vergiye tabi olanlar, tarifelerde yer alan ve **trafik siciline** kayıtlı motorlu kara taşıtları ile **sivil hava vasıtaları siciline** kayıtlı uçak ve helikopterlerdir. Yat, kotra ve motorlu teknelere ilişkin (III) sayılı tarife 5897 sayılı Kanunla **yürürlükten kaldırılmıştır**.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 1',
    ),
    # düzey 2
    '0002': patch(
        "İzin verilebilen azami yüklü ağırlığı 3.200 kg olan ve yük taşımak için imal edilmiş bir motorlu araç Motorlu Taşıtlar Vergisi Kanunu'na göre nasıl sınıflandırılır?",
        {
            'A': 'Panel van',
            'B': 'Çekici',
            'C': 'Arazi taşıtı',
            'D': 'Kamyonet',
            'E': 'Kamyon',
        },
        'D',
        "m. 2'ye göre **kamyonet**, izin verilebilen azami yüklü ağırlığı **3,5 tonu geçmeyen** ve yük taşımak için imal edilmiş araçtır; 3,5 tondan fazla olan **kamyondur**. Çekici yük taşımayan, römork çekmek için imal edilmiş araçtır.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 2',
    ),
    # düzey 2
    '0003': patch(
        "Bir otomobilin ilk iktisabında KDV ve ÖTV hariç satış bedeli 900.000 ₺, hesaplanan ÖTV 720.000 ₺, hesaplanan KDV 324.000 ₺'dir. Motorlu taşıtlar vergisinde esas alınacak taşıt değeri kaç ₺'dir?",
        {
            'A': '900.000',
            'B': '1.944.000',
            'C': '1.620.000',
            'D': '1.224.000',
            'E': '1.800.000',
        },
        'A',
        "m. 2/20'ye göre taşıt değeri, taşıtların teslimi, ilk iktisabı ve ithalinde **KDV matrahını oluşturan unsurlardan, vade farkı ile hesaplanan ÖTV hariç** teşekkül eden değerdir. KDV zaten matraha girmez, ÖTV de hariç tutulur: taşıt değeri **900.000 ₺**. ÖTV eklenirse 1.620.000 ₺ bulunur.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 2/20',
    ),
    # düzey 3
    '0004': patch(
        'Bir belediyenin sermayesinin tamamına sahip olduğu ve ayrı tüzel kişiliği bulunan ulaşım anonim şirketi adına tescilli otobüsler hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Vergiye tabidir; ayrı tüzel kişilikli işletme istisna dışıdır',
            'B': 'Sermayesi belediyeye ait olduğundan belediye taşıtı sayılır ve istisnadır',
            'C': 'Yarı oranda vergilendirilir',
            'D': 'Belediye meclisi kararıyla istisna edilebilir',
            'E': 'Yolcu taşımacılığında kullanıldığı için istisnadır',
        },
        'A',
        "m. 4/a'ya göre belediyeler adına tescilli taşıtlar istisnadır; ancak **bu idarelere bağlı olup ayrı tüzel kişiliği olan işletmeler** ile özel kanunlarında malları Devlet malı sayılmış kuruluşların taşıtları istisna dışında bırakılmıştır.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 4/a',
    ),
    # düzey 1
    '0005': patch(
        "Motorlu taşıtlar vergisine ilişkin yeni bir istisna getirilmesi düşünülmektedir.\n\nMotorlu Taşıtlar Vergisi Kanunu'na göre bu konuyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'İstisna bu Kanuna hüküm eklenerek düzenlenir',
            'B': 'Yeni istisna Cumhurbaşkanı kararıyla getirilebilir',
            'C': 'İstisna bu Kanunda değişiklik yapılarak düzenlenebilir',
            'D': 'Bu Kanunda yer almayan istisnalar hükümsüzdür',
            'E': 'Uluslararası anlaşma hükümleri saklıdır',
        },
        'B',
        'MTVK m. 4 son fıkrası: motorlu taşıtlar vergisiyle ilgili muaflık ve istisna hükümleri bu Kanuna hüküm eklenmek veya bu Kanunda değişiklik yapılmak suretiyle düzenlenir; bu Kanunda yer almayan istisna ve muaflıklar hükümsüzdür. Uluslararası anlaşma hükümleri saklıdır.',
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 4 son fıkra',
    ),
    # düzey 2
    '0006': patch(
        'Aşağıdakilerden hangisine ait uçaklar (IV) sayılı tarifeye göre motorlu taşıtlar vergisine tabi tutulmaz?',
        {
            'A': 'Ticari havayolu şirketi',
            'B': 'Özel jet sahibi şirket',
            'C': 'Pilot eğitimi veren özel şirket',
            'D': 'Türk Hava Kurumu',
            'E': 'Zirai ilaçlama şirketi',
        },
        'D',
        "m. 6'ya göre uçak ve helikopterler (IV) sayılı tarifeye göre vergilendirilir; **Türkkuşu ve Türk Hava Kurumuna ait olanlar hariç** tutulmuştur. Zirai ilaçlama uçaklarında ise tarife tutarlarının %25'i uygulanır.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 6',
    ),
    # düzey 3
    '0007': patch(
        'Hem benzinli motoru hem de elektrik motoru bulunan hibrit bir otomobilin vergilendirilmesi hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Motor gücüne göre satır belirlenip %25 uygulanır',
            'B': "Tarife tutarının %50'si uygulanır",
            'C': 'Vergiden müstesnadır',
            'D': 'Silindir hacmi ve taşıt değerine göre tam tutar uygulanır',
            'E': "Tarife tutarının %25'i uygulanır",
        },
        'D',
        "m. 5'teki %25 oranı yalnızca **sadece elektrik motoru olan** taşıtlar için öngörülmüştür. İçten yanmalı motoru da bulunan hibrit otomobil, (I) sayılı tarifede **motor silindir hacmi ve taşıt değerine** göre belirlenen satırdan tam tutarla vergilendirilir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 5',
    ),
    # düzey 3
    '0008': patch(
        "2016'da tescil edilmiş bir otomobilin kasko değeri 80.000 ₺'dir. I/A sayılı tarifede bu otomobilin satırında yaşına isabet eden vergi 4.800 ₺, bir önceki satırdaki aynı yaş grubunun vergisi 3.100 ₺'dir. Ödenecek yıllık vergi kaç ₺'dir?",
        {
            'A': '3.100',
            'B': '2.400',
            'C': '4.000',
            'D': '4.800',
            'E': '1.550',
        },
        'A',
        "Geçici m. 8'e göre I/A tarifesindeki vergi tutarının **kasko değerinin %5'ini aşması** hâlinde, **bir önceki satırdaki aynı yaş grubunun** vergi tutarı esas alınır. 80.000 × %5 = 4.000 ₺ < 4.800 ₺ olduğundan vergi **3.100 ₺**'dir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu Geçici m. 8',
    ),
    # düzey 2
    '0009': patch(
        "Bir otomobilin hesaplanan taşıt değeri 1.234.567 ₺'dir. Kesirlere ilişkin kural uygulandığında tarifede esas alınacak taşıt değeri kaç ₺'dir?",
        {
            'A': '1.234.000',
            'B': '1.234.567',
            'C': '1.234.500',
            'D': '1.230.000',
            'E': '1.233.000',
        },
        'C',
        "m. 10/4'e göre **taşıt değerlerinin hesabında yüz Türk lirasına**, ödenmesi gereken vergi miktarlarında ise **bir Türk lirasına** kadar olan kesirler dikkate alınmaz: 1.234.567 → **1.234.500 ₺**.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 10',
    ),
    # düzey 2
    '0010': patch(
        "(II) sayılı tarifede yer alan ve sadece elektrik motoru bulunan bir kamyonet için tarifede yaşına isabet eden vergi 8.000 ₺ ise ödenecek yıllık vergi kaç ₺'dir?",
        {
            'A': '4.000',
            'B': '800',
            'C': '6.000',
            'D': '8.000',
            'E': '2.000',
        },
        'E',
        "m. 6'ya göre (II) sayılı tarifedeki minibüs, otobüs, **kamyonet**, kamyon, çekici ve benzeri taşıtlardan **sadece elektrik motoru olanlar**, yaşları itibarıyla tarifede yer alan tutarların **%25'i** oranında vergilendirilir: 8.000 × %25 = **2.000 ₺**.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 6',
    ),
    # düzey 2
    '0011': patch(
        "Tescilli bir otomobil 15 Nisan 2026'da satılmış ve aynı gün alıcı adına tescil edilmiştir. Alıcının mükellefiyeti hangi tarihten itibaren dikkate alınır?",
        {
            'A': '1 Ocak 2026',
            'B': '15 Nisan 2026',
            'C': '1 Temmuz 2026',
            'D': '1 Mayıs 2026',
            'E': '1 Ocak 2027',
        },
        'C',
        "m. 7/b'ye göre devir ve temlik sebebiyle yapılan tescil değişikliği **takvim yılının ilk altı ayında** yapılmışsa **takip eden son altı aylık dönemin başından**, son altı ayında yapılmışsa takip eden takvim yılı başından itibaren dikkate alınır.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 7/b',
    ),
    # düzey 3
    '0012': patch(
        "Tescilli bir otomobil 12 Ocak 2026'da satılacaktır. 2026 yılının birinci taksiti henüz ödenmemiştir.\n\nMotorlu Taşıtlar Vergisi Kanunu'na göre bu taksitle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Taksit ayında yapılan devirde vergi devirden önce ödenir',
            'B': 'Ödeme malik değişikliği yapılmadan önce yapılır',
            'C': 'Kural satış nedeniyle malik değişikliğine uygulanır',
            'D': 'Birinci taksit satıştan sonra alıcı tarafından ödenir',
            'E': 'Bu olayda birinci taksit devirden önce ödenmelidir',
        },
        'D',
        'MTVK m. 9: devir ve temlik sebebiyle Ocak ve Temmuz ayları içinde yapılacak kayıt ve tescil veya satış nedeniyle malik değişikliğinde vergi, bu değişikliğin yapılmasından önce ödenir. Bu nedenle birinci taksitin alıcıya bırakılması mümkün değildir.',
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 9',
    ),
    # düzey 1
    '0013': patch(
        'Motorlu taşıtlar vergisi hangi aylarda ödenir?',
        {
            'A': 'Ocak ve Temmuz aylarında iki eşit taksitte',
            'B': 'Nisan ve Ekim aylarında iki eşit taksitte',
            'C': 'Mart ve Kasım aylarında iki eşit taksitte',
            'D': 'Ocak ayında tek seferde',
            'E': 'Şubat ve Ağustos aylarında iki eşit taksitte',
        },
        'A',
        "m. 9'a göre MTV **her yıl Ocak ve Temmuz aylarında iki eşit taksitte** ödenir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 9',
    ),
    # düzey 3
    '0014': patch(
        "Yıllık motorlu taşıtlar vergisi 6.000 ₺ olan bir kamyonette Mart ayında yapılan değişiklik sonucu azami toplam ağırlık artmış ve yeni duruma göre yıllık vergi 9.000 ₺ olmuştur. O yılın Temmuz taksiti kaç ₺'dir?",
        {
            'A': '3.000',
            'B': '9.000',
            'C': '6.000',
            'D': '3.750',
            'E': '4.500',
        },
        'E',
        "m. 11'e göre vergiyi etkileyen değişiklik **ilk altı ayda** yapılmışsa **takip eden son altı aylık dönemin başından** dikkate alınır; m. 9'a göre bu durumda **ikinci taksit yeni duruma göre** ödenir: 9.000 / 2 = **4.500 ₺**. Ocak taksiti eski duruma göre 3.000 ₺'dir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 9, 11',
    ),
    # düzey 3
    '0015': patch(
        "Bir noter, geçmiş yıllara ait motorlu taşıtlar vergisinin ödendiğini gösteren belgeyi aramadan otomobilin satışını yapmıştır.\n\nMotorlu Taşıtlar Vergisi Kanunu'na göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Noter satıştan önce vergi ödendi belgesini aramalıdır',
            'B': 'Ödenmemiş vergi borcu satışla alıcıya geçer',
            'C': 'Belgeyi aramayan noter mükellefle müteselsilen sorumludur',
            'D': 'Noter ödediği vergi için mükellefe rücu edebilir',
            'E': 'Sorumluluk gecikme zammı ve cezaları da kapsar',
        },
        'B',
        'MTVK m. 13/c-e: noterler taşıtların satış veya devir işlemlerini yapmadan önce ödenmemiş vergi, gecikme zammı, gecikme faizi ve cezaların ödendiğini gösteren belgeyi aramak zorundadır; bu zorunluluğa uymadan işlem yapanlar mükelleflerle birlikte müteselsilen sorumludur ve ödedikleri için mükellefe rücu edebilir. Geçmiş yıllar borcu alıcıya geçmez.',
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 13/c, e',
    ),
    # düzey 2
    '0016': patch(
        'Bir anonim şirketin genel müdürüne tahsis ettiği otomobil için ödediği motorlu taşıtlar vergisi kurumlar vergisi matrahının tespitinde nasıl dikkate alınır?',
        {
            'A': 'Gider olarak kabul edilmez',
            'B': 'Gelecek yıla gider olarak devreder',
            'C': 'Yarısı gider yazılır',
            'D': 'Tamamı gider yazılır',
            'E': 'Amortismana eklenir',
        },
        'A',
        "m. 14'e göre (I), I/A ve (IV) sayılı tarifelerdeki taşıtlardan alınan **vergi ve cezalar ile gecikme zamları** gelir ve kurumlar vergisi matrahlarının tespitinde **gider olarak kabul edilmez**; taşıt kiralama işletmelerinin kiraya verdikleri taşıtlar ile ticari uçak ve helikopterler hariçtir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 14',
    ),
    # düzey 2
    '0017': patch(
        'Motorlu taşıtlar vergisinin gider kabul edilmemesine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kısıtlama gecikme zamlarını da kapsar',
            'B': 'Kısıtlama (II) sayılı tarifedeki kamyonları da kapsar',
            'C': 'Ticari amaçla kullanılan helikopterler kapsam dışıdır',
            'D': 'Kısıtlama vergi cezalarını da kapsar',
            'E': 'Araç kiralama işletmesinin kiraya verdiği otomobiller kapsam dışıdır',
        },
        'B',
        'm. 14 yalnızca **(I), I/A ve (IV)** sayılı tarifelerdeki taşıtlardan alınan vergi, ceza ve gecikme zamlarını gider dışı sayar; **(II) sayılı tarifedeki** minibüs, otobüs, kamyonet ve kamyonların vergisi gider yazılabilir. Kiralama işletmelerinin kiraya verdikleri taşıtlar ile ticari uçak ve helikopterler kapsam dışıdır.',
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 14',
    ),
    # düzey 2
    '0018': patch(
        'Motorlu taşıtlar vergisinin ödenmesine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ocak ayındaki satışta vergi malik değişikliğinden önce ödenir',
            'B': 'Vergi Ocak ve Temmuz aylarında iki eşit taksitte ödenir',
            'C': 'Vergi yetkili banka şubelerine de ödenebilir',
            'D': 'Yıl içinde vergi artırılırsa fark birinci taksite eklenir',
            'E': 'İlk altı ayda taşıtın bünyesi değişirse ikinci taksit yeni duruma göre ödenir',
        },
        'D',
        "m. 9'a göre takvim yılının ilk altı ayında taşıtın bünyesinde değişiklik olması veya **verginin artırılması ya da azaltılması** hâlinde **ikinci taksit** yeni duruma göre ödenir; birinci taksit değişmez.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 9',
    ),
    # düzey 3
    '0019': patch(
        'Engellilik oranı %40 olan bir kişi, durumuna uygun hâle getirilmiş özel tertibatlı otomobilini bir yakınına satmıştır. Yeni malik engelli değildir. Otomobilin vergisi hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yeni malik engelliye bakıyorsa istisnadır',
            'B': 'Satış yılında istisna devam eder, sonra kalkar',
            'C': 'Yeni malik adına tescilden sonra vergiye tabidir',
            'D': 'Özel tertibat bulunduğu sürece istisnadır',
            'E': 'Yarı oranda vergilendirilir',
        },
        'C',
        "m. 4/c'deki istisna, **engellilerin** durumlarına uygun özel tertibatlı taşıtlar içindir; istisna taşıtın değil **malikin engellilik durumuna** bağlıdır. Engelli olmayan kişi adına tescil edilen taşıt, mükellefiyet başlangıcı kurallarına göre vergiye tabi olur.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 4/c',
    ),
    # düzey 2
    '0020': patch(
        'Aşağıdaki taşıtlardan hangisi (II) sayılı tarifeye göre vergilendirilmez?',
        {
            'A': 'Minibüs',
            'B': 'Motorlu karavan',
            'C': 'Panel van',
            'D': 'Kaptıkaçtı',
            'E': 'Çekici',
        },
        'D',
        "m. 6'ya göre (I) sayılı tarifedeki taşıtlar dışında kalan motorlu kara taşıtları (II) sayılı tarifeye göre vergilendirilir: **minibüs, panel van ve motorlu karavan, otobüs, kamyonet, kamyon ve çekiciler**. **Kaptıkaçtı** otomobil ve arazi taşıtlarıyla birlikte (I) sayılı tarifededir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 6',
    ),
    # düzey 2
    '0021': patch(
        "A, otomobilini Mayıs ayında noterde B'ye satmış ancak devir işlemi tamamlanıp trafik sicilindeki kayıt B adına değiştirilmeden önce yıl bitmiştir. Bu süre içinde motorlu taşıtlar vergisinin mükellefi kimdir?",
        {
            'A': 'Satış bedelini ödeyen taraf',
            'B': 'Sicilde adına kayıtlı olan A',
            'C': 'A ile B yarı yarıya',
            'D': 'Taşıtı kullanan B',
            'E': 'A ile B müteselsilen',
        },
        'B',
        "m. 3'e göre mükellef, **trafik sicili veya sivil hava vasıtaları sicilinde adına motorlu taşıt kayıt ve tescil edilmiş** gerçek ve tüzel kişilerdir. Kayıt değişmediği sürece mükellef A'dır; taşıtı fiilen kullanan kişi mükellef olmaz.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 3',
    ),
    # düzey 2
    '0022': patch(
        'Model yılı 2023 olan bir otomobil, 2026 yılında (I) sayılı tarifenin hangi yaş grubunda vergilendirilir?',
        {
            'A': '7-11 yaş',
            'B': '4-6 yaş',
            'C': '16 ve yukarı yaş',
            'D': '1-3 yaş',
            'E': '12-15 yaş',
        },
        'B',
        "Model yılında bir yaşında kabul edildiğinden 2023 modelin yaşı 2026'da **4**'tür (2023: 1, 2024: 2, 2025: 3, 2026: 4). (I) sayılı tarifede yaş grupları 1-3, **4-6**, 7-11, 12-15 ve 16 ve yukarısıdır.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 2, 11',
    ),
    # düzey 2
    '0023': patch(
        "Zirai ilaçlama amacıyla kayıt ve tescil edilmiş bir uçak için (IV) sayılı tarifede yaşına isabet eden vergi 400.000 ₺ ise ödenecek yıllık motorlu taşıtlar vergisi kaç ₺'dir?",
        {
            'A': '200.000',
            'B': '0',
            'C': '40.000',
            'D': '100.000',
            'E': '400.000',
        },
        'D',
        "m. 6'ya göre uçak ve helikopterler (IV) sayılı tarifeye göre vergilendirilir; **zirai ilaçlama amacıyla kayıt ve tescil edilmiş uçaklar için tarifedeki tutarlar %25 oranında** uygulanır: 400.000 × %25 = **100.000 ₺**.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 6',
    ),
    # düzey 1
    '0024': patch(
        "7566 sayılı Kanunla Motorlu Taşıtlar Vergisi Kanunu'nun istisna maddesine aşağıdakilerden hangisi adına tescil edilen taşıtlar eklenmiştir?",
        {
            'A': 'Üniversite döner sermaye işletmeleri',
            'B': 'Kalkınma ajansları',
            'C': 'Organize sanayi bölgeleri',
            'D': 'Kamu yararına çalışan dernekler',
            'E': 'Yatırım izleme ve koordinasyon başkanlıkları',
        },
        'E',
        "7566 sayılı Kanunun 4. maddesiyle m. 4/a'ya **il özel idarelerinden sonra gelmek üzere yatırım izleme ve koordinasyon başkanlıkları** eklenmiştir (yürürlük 19/12/2025).",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 4/a (7566 sayılı Kanunla değişik)',
    ),
    # düzey 3
    '0025': patch(
        'Aşağıdaki taşıtlardan hangileri motorlu taşıtlar vergisinden müstesnadır?\n\nI. Engellilik oranı %95 olan kişi adına tescilli, özel tertibatı bulunmayan otomobil\n\nII. Engellilik oranı %70 olan kişi adına tescilli, özel tertibatı bulunmayan otomobil\n\nIII. Engellilik oranı %50 olan kişinin durumuna uygun özel tertibatlı otomobil',
        {
            'A': 'Yalnız III',
            'B': 'I ve II',
            'C': 'I ve III',
            'D': 'I, II ve III',
            'E': 'Yalnız I',
        },
        'C',
        "m. 4/c'ye göre **engellilik oranı %90 ve daha fazla** olanların adlarına kayıtlı taşıtlar (I) ile **diğer engellilerin durumlarına uygun hâle getirilmiş özel tertibatlı** taşıtlar (III) istisnadır. Oranı %90'ın altında olan kişinin özel tertibatsız taşıtı (II) vergiye tabidir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 4/c',
    ),
    # düzey 3
    '0026': patch(
        "2021'de ilk kez tescil edilen bir otomobil 2026'da ikinci el olarak satılmıştır. Yeni malik için (I) sayılı tarifede esas alınacak satır nasıl belirlenir?",
        {
            'A': 'İlk tescil tarihindeki taşıt değerine isabet eden satır esas alınır',
            'B': 'Yeni malik satırı seçer',
            'C': 'En düşük satır uygulanır',
            'D': 'Yeni malikin ödediği ikinci el satış bedeline göre tarifede yeni satır belirlenir',
            'E': 'Kasko değerine göre yeni satır belirlenir',
        },
        'A',
        "m. 5'e göre (I) sayılı tarifedeki otomobil, kaptıkaçtı ve arazi taşıtlarında **ilk kayıt ve tescil edildiği tarih itibarıyla taşıt değerine isabet eden satır, sonraki yıllarda da** vergi tutarının belirlenmesinde esas alınır; malik değişikliği satırı değiştirmez.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 5',
    ),
    # düzey 3
    '0027': patch(
        '(I) sayılı tarifedeki otomobillerde vergi tutarının kasko değerine göre sınırlandırılması hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Cumhurbaşkanına %10 oranı üzerinden tanınmış bir yetkidir',
            'B': 'Sınır, mükellefin başvurusuyla uygulanır',
            'C': 'Kasko değerini aşan vergi ertesi yıla devreder',
            'D': "Kasko değerinin %5'ini aşan kısım terkin edilir",
            'E': "Vergi, tarife tutarına bakılmaksızın kasko değerinin %10'u olarak hesaplanır",
        },
        'A',
        "m. 5'e göre (I) sayılı tarifedeki taşıtlara ait vergi tutarlarının **kasko değerinin %10'unu** aşması hâlinde vergiyi bir önceki satırdaki aynı yaş grubunun tutarı olarak belirlemeye, bu oranı **%4'e kadar indirmeye ve kanuni oranına kadar artırmaya Cumhurbaşkanı yetkilidir**. I/A tarifesinde ise %5 sınırı kanunla doğrudan uygulanır.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 5',
    ),
    # düzey 2
    '0028': patch(
        "Aşağıdakilerden hangileri motorlu taşıtlar vergisinde Cumhurbaşkanına tanınmış yetkilerdendir?\n\nI. Kanunda sayılmayan taşıtlar için yeni istisna getirmek\n\nII. Katalitik konvertörlü taşıtlarda vergiyi %50'ye kadar indirmek\n\nIII. Taşıt değerlerini ayrı ayrı veya birlikte yeniden belirlemek",
        {
            'A': 'I, II ve III',
            'B': 'Yalnız II',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'Yalnız III',
        },
        'D',
        "m. 10'a göre Cumhurbaşkanı yeni oranlar tespit etmeye, **taşıt değerlerini ayrı ayrı veya birlikte yeniden belirlemeye** ve **EURO normlarını sağlayan katalitik konvertörlü taşıtlarda oranı veya vergi miktarlarını %50 nispetine kadar indirmeye** yetkilidir. İstisnalar (I) m. 4 uyarınca ancak Kanunla düzenlenebilir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 10',
    ),
    # düzey 1
    '0029': patch(
        'Motorlu taşıtlar vergisi mükellefiyeti hangi işlemle başlar?',
        {
            'A': 'Faturanın düzenlenmesiyle',
            'B': 'Trafik sigortasının yapılmasıyla',
            'C': 'Taşıtın sicile kayıt ve tescili ile',
            'D': 'İlk fenni muayene ile',
            'E': 'Taşıtın satın alınmasıyla',
        },
        'C',
        "m. 7'ye göre MTV mükellefiyeti motorlu taşıtların **trafik sicili veya sivil hava vasıtaları siciline kayıt ve tescili ile** başlar.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 7',
    ),
    # düzey 2
    '0030': patch(
        "Sıfır kilometre bir otomobil 5 Kasım 2026'da ilk kez trafiğe tescil edilmiştir. Motorlu taşıtlar vergisi mükellefiyeti hangi tarihten itibaren dikkate alınır?",
        {
            'A': '5 Kasım 2026',
            'B': '1 Ocak 2027',
            'C': '1 Ocak 2026',
            'D': '1 Aralık 2026',
            'E': '1 Temmuz 2026',
        },
        'E',
        "m. 7/a'ya göre **son altı ay içinde** yeni kayıt ve tescil edilen taşıtlarda mükellefiyet **son altı aylık dönemin başından** (1 Temmuz) itibaren dikkate alınır.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 7/a',
    ),
    # düzey 2
    '0031': patch(
        "Hurdaya ayrılan bir otomobilin trafik kaydı 20 Mart 2026'da silinmiştir. Motorlu taşıtlar vergisi mükellefiyeti ne zaman sona erer?",
        {
            'A': '1 Temmuz 2026',
            'B': '1 Ocak 2027',
            'C': '31 Aralık 2026',
            'D': '20 Mart 2026',
            'E': '1 Nisan 2026',
        },
        'A',
        "m. 8'e göre kaydın silinmesi **takvim yılının ilk altı ayı içinde** yapılmışsa **ikinci altı aylık dönemin başından**, ikinci altı aylık dönemde yapılmışsa takip eden takvim yılı başından itibaren mükellefiyet sona erer. Temmuz taksiti ödenmez.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 8',
    ),
    # düzey 3
    '0032': patch(
        'Motorlu taşıtlar vergisinde kaydın silinmesine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Mart'ta silinen taşıt için Temmuz taksiti ödenmez",
            'B': "Haziran'da silinen taşıt için o yıl Ocak taksiti ödenir, Temmuz taksiti ödenmez",
            'C': "Eylül'de silinen taşıtın mükellefiyeti izleyen yıl sona erer",
            'D': 'Mükellefiyet, sicil kaydının silinmesine bağlı olarak sona erer',
            'E': "Ağustos'ta silinen taşıtın Temmuz taksiti iade edilir",
        },
        'E',
        "m. 8'e göre ikinci altı aylık dönemde yapılan silinmede mükellefiyet **takip eden takvim yılı başından** sona erer; bu nedenle Ağustos'ta silinen taşıtın o yılın ikinci taksiti de ödenir, **iade edilmez**. İlk altı ayda silinmede ikinci altı aylık dönemden itibaren vergi alınmaz.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 8',
    ),
    # düzey 3
    '0033': patch(
        "Yıllık motorlu taşıtlar vergisi 10.000 ₺ olan sıfır kilometre bir otomobil 20 Eylül'de ilk kez tescil edilmiştir.\n\nMotorlu Taşıtlar Vergisi Kanunu'na göre o yılın vergisiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'İlk altı aydan sonraki tescilde ikinci yarının vergisi doğar',
            'B': 'Yıllık verginin tamamı tahakkuk eder',
            'C': "Bu olayda ödenecek vergi 5.000 ₺'dir",
            'D': 'Temmuz süresi geçtiğinden vergi bir ay içinde ödenir',
            'E': "Ödeme süresi 20 Ekim'de dolar",
        },
        'B',
        "MTVK m. 9: ilk altı aylık dönem geçtikten sonra yapılan tescillerde sadece ikinci altı aylık döneme ilişkin vergi tahakkuk eder: 10.000 / 2 = 5.000 ₺. Temmuz taksit süresi geçmiş olduğundan bu tutar tescilden itibaren bir ay içinde, yani 20 Ekim'e kadar ödenir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 9',
    ),
    # düzey 1
    '0034': patch(
        'Motorlu taşıtlar vergisi mükellefi, adına kayıtlı taşıtın niteliklerinde vergiyi etkileyen bir değişikliği ne kadar süre içinde vergi dairesine bildirmelidir?',
        {
            'A': 'Bir sonraki taksit ayına kadar',
            'B': 'On beş gün',
            'C': 'Bir ay',
            'D': 'Yıl sonuna kadar',
            'E': 'Üç ay',
        },
        'C',
        "m. 13/b'ye göre mükellefler, adlarına tescilli taşıtları ve bunlarda meydana gelen değişiklikleri **kayıt ve tescilin yapıldığı veya değişikliğin meydana geldiği tarihten itibaren bir ay içinde** ilgili vergi dairesine bildirmek zorundadır; uymayanlara usulsüzlük cezası kesilir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 13/b',
    ),
    # düzey 2
    '0035': patch(
        'Motorlu taşıtlar vergisinde bildirim ve sorumluluk hükümlerine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bildirim yükümlülüğüne uymayan mükellefe usulsüzlük cezası kesilir',
            'B': 'Fenni muayene yapan kişiler, vergiyi araştırmasa da sorumlu tutulamaz',
            'C': 'Noterler satıştan önce vergilerin ödendiğini gösteren belgeyi arar',
            'D': 'Trafik sicil memurları tescil ettikleri taşıtları bir ay içinde vergi dairesine bildirir',
            'E': 'Sorumlu sıfatıyla ödeme yapanlar mükellefe rücu edebilir',
        },
        'B',
        "m. 13/d'ye göre fenni muayene yapma yetkisi verilen gerçek ve tüzel kişiler muayeneden önce verginin ödenip ödenmediğini araştırmak zorundadır; m. 13/e'ye göre bu zorunluluğa uymadan işlem yapanlar **mükellefle birlikte müteselsilen sorumludur**. Diğer ifadeler m. 13'ün (a), (b), (c) ve (e) bentlerine uygundur.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 13',
    ),
    # düzey 3
    '0036': patch(
        'Aşağıdaki taşıtlardan hangilerine ait motorlu taşıtlar vergisi kazancın tespitinde gider olarak yazılabilir?\n\nI. Araç kiralama şirketinin kiraya verdiği otomobil\n\nII. Nakliye şirketinin yük taşıdığı kamyon\n\nIII. Danışmanlık şirketinin ortağına tahsis ettiği otomobil',
        {
            'A': 'Yalnız II',
            'B': 'I ve III',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'D',
        "m. 14'teki gider kısıtlaması yalnız **(I), I/A ve (IV)** sayılı tarifelerdeki taşıtlar içindir ve **taşıt kiralama işletmelerinin kiraya verdikleri taşıtlar** bu kısıtlamanın dışındadır (I). Kamyon **(II)** sayılı tarifede olduğundan kısıtlama kapsamında değildir (II). Ortağa tahsis edilen otomobilin vergisi gider yazılamaz (III).",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 14',
    ),
    # düzey 3
    '0037': patch(
        "Yıllık vergisi 7.000 ₺ olan tescilli bir otomobil 15 Mart'ta satılmış ve alıcı adına tescil edilmiştir. Satıcı Ocak taksitini ödemiştir. O yılın Temmuz taksitini kim öder?",
        {
            'A': 'Alıcı, 3.500 ₺',
            'B': 'Satıcı ve alıcı yarı yarıya',
            'C': 'Alıcı, 7.000 ₺',
            'D': 'Satıcı, 3.500 ₺',
            'E': 'Alıcı, 1.750 ₺',
        },
        'A',
        "m. 7/b'ye göre devir **ilk altı ayda** yapıldığından alıcının mükellefiyeti **takip eden son altı aylık dönemin başından** başlar. Temmuz taksiti (7.000 / 2 = **3.500 ₺**) alıcıya aittir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 7, 9',
    ),
    # düzey 2
    '0038': patch(
        'Motorlu taşıtlar vergisinde mükellefiyetin başlamasına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Mayıs'ta devralınan taşıtta alıcının mükellefiyeti Temmuz başında başlar",
            'B': "Şubat'ta yeni tescil edilen taşıtın mükellefiyeti yıl başından dikkate alınır",
            'C': "Kasım'da devralınan taşıtta alıcının mükellefiyeti izleyen yıl başlar",
            'D': "Ağustos'ta yeni tescil edilen taşıtın mükellefiyeti Temmuz başından dikkate alınır",
            'E': "Haziran'da yeni tescil edilen taşıtın mükellefiyeti Temmuz başında başlar",
        },
        'E',
        "m. 7/a'ya göre **ilk altı ayda yeni tescil edilen** taşıtlarda mükellefiyet **takvim yılı başından** dikkate alınır; Haziran ilk altı aya dâhil olduğundan Temmuz değil yıl başı esas alınır. Devir hâlinde ise ilk altı aydaki değişiklik son altı aylık dönemden, son altı aydaki değişiklik izleyen yıl başından dikkate alınır.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 7',
    ),
    # düzey 3
    '0039': patch(
        'Bir leasing şirketi adına tescilli otomobili kiracı şirket kullanmaktadır. Motorlu taşıtlar vergisinin mükellefi hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İki şirket müteselsilen mükelleftir',
            'B': 'Sicilde adına tescilli leasing şirketi mükelleftir',
            'C': 'Taraflar sözleşmeyle mükellefi belirler',
            'D': 'Kiracı, finansal kiralama süresince taşıtı kullandığı için mükellef sayılır',
            'E': 'Aracı kullanan kiracı şirket mükelleftir',
        },
        'B',
        "m. 3'e göre MTV mükellefi, **trafik sicilinde adına tescil edilmiş** gerçek ve tüzel kişidir. Otomobil leasing şirketi adına tescilli olduğundan vergi mükellefi leasing şirketidir; vergi yükünün sözleşmeyle kiracıya yansıtılması mükellefiyeti değiştirmez.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 3, 7',
    ),
    # düzey 2
    '0040': patch(
        "Azami toplam ağırlığı 3.000 kg olan, kapalı kasalı, sürücü kısmından başka sıralı oturma yeri bulunan ve insan ile yük taşımak için imal edilmiş taşıt Kanun'a göre nasıl sınıflandırılır?",
        {
            'A': 'Kamyonet',
            'B': 'Motorlu karavan',
            'C': 'Panel van',
            'D': 'Minibüs',
            'E': 'Kaptıkaçtı',
        },
        'C',
        "m. 2/8'e göre **panel van**, azami toplam ağırlığı **3.500 kg'ı geçmeyen, kapalı kasalı**, sürücü kısmından başka tek veya daha fazla sıralı oturma yeri bulunan, **insan ve yük taşımak** için imal edilmiş taşıttır. Kamyonet yalnız yük taşımak için imal edilir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 2',
    ),
    # düzey 1
    '0041': patch(
        "Sürücüsü dâhil 14 oturma yeri olan ve insan taşımak için imal edilmiş motorlu araç, Motorlu Taşıtlar Vergisi Kanunu'na göre hangi sınıfta yer alır?",
        {
            'A': 'Panel van',
            'B': 'Otomobil',
            'C': 'Otobüs',
            'D': 'Minibüs',
            'E': 'Kaptıkaçtı',
        },
        'D',
        "m. 2'ye göre **otomobil** sürücü dâhil en çok 8, **minibüs** sürücü dâhil **9 ile 17**, **otobüs** sürücü dâhil en az 18 oturma yeri olan ve insan taşımak için imal edilmiş araçtır.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 2',
    ),
    # düzey 2
    '0042': patch(
        'Tescil belgesinde model yılı 2024 olarak yazılı bir otomobil, 2026 yılında motorlu taşıtlar vergisi bakımından kaç yaşında kabul edilir?',
        {
            'A': '5',
            'B': '1',
            'C': '2',
            'D': '3',
            'E': '4',
        },
        'D',
        "m. 11'e göre taşıtların **tescil belgesinde yazılı model yılında bir yaşında** olduğu kabul edilir ve yaş takvim yılı itibarıyla belirlenir: 2024'te 1, 2025'te 2, **2026'da 3** yaşındadır.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 2, 11',
    ),
    # düzey 2
    '0043': patch(
        'Aşağıdaki taşıtlardan hangileri (I) sayılı tarifeye göre vergilendirilir?\n\nI. Minibüs\n\nII. Arazi taşıtı\n\nIII. Kamyonet',
        {
            'A': 'Yalnız II',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'A',
        "m. 5'e göre **otomobil, kaptıkaçtı, arazi taşıtları ve benzerleri ile motosikletler (I)** sayılı tarifeye göre vergilendirilir. **Minibüs** ve **kamyonet**, panel van, motorlu karavan, otobüs, kamyon ve çekicilerle birlikte m. 6'daki **(II)** sayılı tarifededir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 5, 6',
    ),
    # düzey 2
    '0044': patch(
        'Aşağıdakilerden hangisi adına tescilli taşıt motorlu taşıtlar vergisinden müstesna değildir?',
        {
            'A': 'Sosyal güvenlik kurumu',
            'B': 'Türkiye Kızılay Derneği',
            'C': 'Köy tüzel kişiliği',
            'D': 'Belediyelerin üye olduğu mahalli idare birliği',
            'E': 'Malları özel kanununda Devlet malı sayılan kuruluş',
        },
        'E',
        "m. 4/a'ya göre genel ve özel bütçeli idareler, **sosyal güvenlik kurumları**, il özel idareleri, YİKOB'lar, belediyeler, **köy tüzel kişilikleri** ile **bunların üyesi oldukları mahalli idare birlikleri** ve **Türkiye Kızılay Derneği** adına tescilli taşıtlar istisnadır. Parantez içi hükümle **özel kanunlarında malları Devlet malı sayılmış kuruluşların** taşıtları istisna dışındadır.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 4/a',
    ),
    # düzey 3
    '0045': patch(
        "Karşılıklılık şartının bulunduğu bir ülkenin İzmir'deki fahri konsolosu adına tescilli bir otomobil bulunmaktadır.\n\nMotorlu Taşıtlar Vergisi Kanunu'na göre bu konuyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Elçilik taşıtları karşılıklılık şartıyla istisnadır',
            'B': 'Konsolosluk taşıtları karşılıklılık şartıyla istisnadır',
            'C': 'Karşılıklılık varsa fahri konsolosun taşıtı da istisnadır',
            'D': 'Fahri konsoloslar istisna kapsamı dışındadır',
            'E': 'Bu istisnada karşılıklılık şartı aranır',
        },
        'C',
        'MTVK m. 4/b: karşılıklı olmak şartıyla yabancı devletlerin elçilik ve konsoloslukları ile elçi, maslahatgüzar ve konsoloslarına (fahri konsoloslar hariç) ait taşıtlar istisnadır. Fahri konsolos adına tescilli otomobil, karşılıklılık bulunsa da vergiye tabidir.',
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 4/b',
    ),
    # düzey 2
    '0046': patch(
        "Sadece elektrik motoru bulunan bir otomobil için (I) sayılı tarifede motor gücü, taşıt değeri ve yaşına isabet eden tutar 12.000 ₺'dir. Ödenecek yıllık vergi kaç ₺'dir?",
        {
            'A': '3.000',
            'B': '12.000',
            'C': '1.200',
            'D': '9.000',
            'E': '6.000',
        },
        'A',
        "m. 5'e göre **sadece elektrik motoru olan** otomobiller, motor gücüne göre belirlenen satırda yaşına isabet eden vergi tutarlarının **%25'i** oranında vergilendirilir: 12.000 × %25 = **3.000 ₺**.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 5',
    ),
    # düzey 1
    '0047': patch(
        '31/12/2017 tarihinde veya daha önce kayıt ve tescil edilmiş bir otomobil hangi tarifeye göre vergilendirilir?',
        {
            'A': '(IV) sayılı tarife',
            'B': '(II) sayılı tarife',
            'C': "Kasko değerinin %5'i",
            'D': 'I/A sayılı tarife',
            'E': '(I) sayılı tarife',
        },
        'D',
        "Geçici m. 8'e göre **31/12/2017 tarihinden (bu tarih dâhil) önce kayıt ve tescil edilen** otomobil, kaptıkaçtı, arazi taşıtları ve benzerleri **I/A** sayılı tarifeye göre vergilendirilir; bu tarifede taşıt değeri sütunu yoktur.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu Geçici m. 8',
    ),
    # düzey 3
    '0048': patch(
        '2017 yılında satın alınan ancak çeşitli nedenlerle tescil ettirilmeyen bir otomobil ilk kez 2019 yılında trafiğe tescil edilmiştir. Bu otomobil hangi tarifeye göre vergilendirilir?',
        {
            'A': '(II) sayılı tarife',
            'B': 'İki tarifeden yüksek olanı',
            'C': 'Tescil yılına göre (I), sonraki yıllarda I/A',
            'D': '(I) sayılı tarife',
            'E': 'I/A sayılı tarife',
        },
        'E',
        "Geçici m. 8 son fıkrasına göre, maddenin yürürlüğe girdiği 1/1/2018 tarihinden **önce iktisap edilmiş ancak çeşitli nedenlerle tescil edilmemiş** otomobiller 1/1/2018'den sonra ilk defa tescil edilirse de **I/A** sayılı tarifeye göre vergilendirilir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu Geçici m. 8',
    ),
    # düzey 3
    '0049': patch(
        "Bir yıl için ilan edilen yeniden değerleme oranı %40'tır.\n\nMotorlu Taşıtlar Vergisi Kanunu'na göre vergi tutarlarının artırılmasıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Vergi kural olarak yeniden değerleme oranında artırılır',
            'B': 'Cumhurbaşkanı farklı bir artış oranı belirleyebilir',
            'C': "Bu olayda Cumhurbaşkanı artışı %70'e çıkarabilir",
            'D': "Alt sınır yeniden değerleme oranının %20'sidir",
            'E': 'Üst sınır yeniden değerleme oranının %50 fazlasıdır',
        },
        'C',
        "MTVK m. 10: vergi miktarları kural olarak yeniden değerleme oranında artırılır; Cumhurbaşkanı yeniden değerleme oranının %50 fazlasını geçmemek, %20'sinden az olmamak üzere yeni oran belirleyebilir. %40 için aralık %8 ile %60'tır; %70 üst sınırı aşar.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 10',
    ),
    # düzey 2
    '0050': patch(
        "Sıfır kilometre bir otomobil 10 Mayıs 2026'da ilk kez trafiğe tescil edilmiştir. Motorlu taşıtlar vergisi mükellefiyeti hangi tarihten itibaren dikkate alınır?",
        {
            'A': '1 Ocak 2027',
            'B': '10 Mayıs 2026',
            'C': '1 Ocak 2026',
            'D': '1 Haziran 2026',
            'E': '1 Temmuz 2026',
        },
        'C',
        "m. 7/a'ya göre **takvim yılının ilk altı ayı içinde** yeni tescil edilen taşıtlarda mükellefiyet **tescilin yapıldığı takvim yılı başından**, son altı ayı içinde tescil edilenlerde son altı aylık dönemin başından itibaren dikkate alınır.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 7/a',
    ),
    # düzey 2
    '0051': patch(
        "Tescilli bir otomobil 20 Ekim 2026'da satılarak alıcı adına tescil edilmiştir. 2026 yılının ikinci taksiti ile 2027 yılının vergisinden kim sorumludur?",
        {
            'A': 'İkisi de satıcıya aittir',
            'B': '2026 ikinci taksiti satıcıya, 2027 vergisi alıcıya aittir',
            'C': 'İkisi de alıcıya aittir',
            'D': 'Taraflar sözleşmeyle belirler',
            'E': '2026 ikinci taksiti alıcıya, 2027 vergisi satıcıya aittir',
        },
        'B',
        "m. 7/b'ye göre devir son altı ayda yapılmışsa alıcının mükellefiyeti **takip eden takvim yılı başından** itibaren başlar. Bu nedenle 2026'nın ikinci taksitinden satıcı, 2027 vergisinden alıcı sorumludur.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 7/b',
    ),
    # düzey 2
    '0052': patch(
        'Motorlu taşıtlar vergisinin tahakkuku ve tebliğine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Vergi, tahakkuk ettirildiği günde tebliğ edilmiş sayılır',
            'B': 'Tahakkuk eden vergi mükellefe ihbarnameyle tebliğ edilir',
            'C': 'Bakanlık, tescil yerinden farklı bir vergi dairesini yetkili kılabilir',
            'D': 'Eksik tahakkuk hâlinde vergi dairesi ikmalen tarh eder',
            'E': 'Vergi her yıl Ocak ayının başında yıllık olarak tahakkuk etmiş sayılır',
        },
        'B',
        "m. 9'a göre MTV **her yıl Ocak ayının başında** yıllık olarak tahakkuk etmiş sayılır; tahakkuk eden vergi **ayrıca mükellefe tebliğ olunmaz** ve tahakkuk günü tebliğ edilmiş sayılır. Eksik veya hiç tahakkuk ettirilmeyen vergi ikmalen tarh edilir; Bakanlık tescil yerinden bağımsız vergi dairesi belirleyebilir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 9',
    ),
    # düzey 3
    '0053': patch(
        "Yıllık motorlu taşıtlar vergisi 8.000 ₺ olan sıfır kilometre bir otomobil 10 Mart'ta ilk kez tescil edilmiştir. Birinci taksite isabet eden 4.000 ₺ en geç ne zaman ödenmelidir?",
        {
            'A': "31 Mayıs'a kadar",
            'B': "31 Mart'a kadar",
            'C': "10 Nisan'a kadar",
            'D': 'Temmuz taksitiyle birlikte',
            'E': "31 Ocak'a kadar",
        },
        'C',
        "Taşıt ilk altı ayda tescil edildiğinden vergi yıllık olarak tahakkuk eder (m. 7/a). m. 9'a göre **taksit süresi geçmiş olan kısım, kayıt ve tescil tarihinden itibaren bir ay içinde** ödenir: Ocak taksiti **10 Nisan'a kadar**, ikinci taksit ise Temmuz'da ödenir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 9',
    ),
    # düzey 3
    '0054': patch(
        "Bir taşıtın motor silindir hacmini değiştiren tadilat Ekim 2026'da yapılmış ve bu değişiklik vergiyi artırmıştır. Yeni vergi tutarı hangi tarihten itibaren uygulanır?",
        {
            'A': '1 Kasım 2026',
            'B': '1 Ocak 2027',
            'C': 'Ekim 2026',
            'D': '1 Temmuz 2027',
            'E': '1 Temmuz 2026',
        },
        'B',
        "m. 11'e göre model yılı, cinsi, motor silindir hacmi, motor gücü, azami toplam ağırlık gibi unsurlarda vergiyi değiştiren bir değişiklik **son altı ayda** yapılmışsa **takip eden takvim yılı başından** itibaren dikkate alınır.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 11',
    ),
    # düzey 3
    '0055': patch(
        "Motorlu taşıtlar vergisi borcu 6183 sayılı Kanun'un 48. maddesine göre taksitlendirilmiş bir taşıt fenni muayeneye götürülmüştür.\n\nMotorlu Taşıtlar Vergisi Kanunu'na göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Vergisi ödenmemiş taşıta kural olarak muayene yapılmaz',
            'B': 'Taksitlendirilmiş borç muayeneye engel değildir',
            'C': "Taksitlendirme 6183 sayılı Kanun'un 48. maddesine göre olmalıdır",
            'D': 'Borcun tamamının ödenmesi beklenmez',
            'E': 'Taksitlerin yarısı ödenmeden muayene yapılamaz',
        },
        'E',
        "MTVK m. 13/d: vergisi ödenmemiş veya 6183 sayılı Kanun'un 48. maddesine göre taksitlendirilmemiş taşıtlara fenni muayene yapılamaz. Borç m. 48'e göre taksitlendirilmişse ödenen taksit oranına bakılmaksızın muayene engeli yoktur.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 13/d',
    ),
    # düzey 3
    '0056': patch(
        'Bir havayolu şirketinin yolcu taşımacılığında kullandığı uçak için ödediği motorlu taşıtlar vergisi hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Uçaklar vergiden müstesnadır',
            'B': 'Maliyet bedeline eklenerek amortismana tabi tutulur',
            'C': 'Yarısı gider yazılabilir',
            'D': 'Uçaklar (IV) sayılı tarifede olduğu için gider yazılamaz',
            'E': 'Ticari maksatla kullanıldığı için gider yazılabilir',
        },
        'E',
        "m. 14'e göre (IV) sayılı tarifedeki taşıtların vergisi kural olarak gider kabul edilmez; ancak **ticari maksatla kullanılan uçak ve helikopterler** bu hükmün dışında tutulmuştur. Ticari yolcu uçağı için ödenen MTV gider yazılabilir.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 14',
    ),
    # düzey 2
    '0057': patch(
        'Motorlu taşıtlar vergisinde yaş ve tarifelere ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yaş, taşıtın ilk tescil tarihinden itibaren ay esasına göre hesaplanır',
            'B': 'Yaş takvim yılı itibarıyla tespit edilir',
            'C': '(I) sayılı tarifede satır, ilk tescildeki taşıt değerine göre belirlenir',
            'D': 'Sadece elektrik motoru olan otomobilde satır motor gücüne göre belirlenir',
            'E': 'Taşıt, tescil belgesindeki model yılında bir yaşında kabul edilir',
        },
        'A',
        "m. 2/18'e göre yaş, **model yılına göre geçen süredir ve takvim yılı itibarıyla** tespit edilir; m. 11'e göre taşıt model yılında bir yaşında kabul edilir. Tescil tarihine göre ay esaslı yaş hesabı yoktur.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 2, 5',
    ),
    # düzey 2
    '0058': patch(
        "2016'da tescil edilmiş ve sadece elektrik motoru olan bir otomobil için I/A sayılı tarifede motor gücü ve yaşına isabet eden tutar 2.000 ₺'dir. Ödenecek yıllık vergi kaç ₺'dir?",
        {
            'A': '200',
            'B': '1.500',
            'C': '2.000',
            'D': '500',
            'E': '1.000',
        },
        'D',
        "Geçici m. 8'e göre I/A sayılı tarifedeki **sadece elektrik motoru olan** taşıtlar motor gücüne göre belirlenen satırda yaşına isabet eden tutarın **%25'i** oranında vergilendirilir: 2.000 × %25 = **500 ₺**.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 5, Geçici m. 8',
    ),
    # düzey 3
    '0059': patch(
        "Sadece elektrik motoru olan bir panel vanın motor gücü 100 kW'tır. (II) sayılı tarifenin panel van bölümünde yaşına isabet eden tutar birinci satırda 6.000 ₺, ikinci satırda 9.000 ₺'dir. Ödenecek yıllık vergi kaç ₺'dir?",
        {
            'A': '6.000',
            'B': '3.000',
            'C': '2.250',
            'D': '1.500',
            'E': '9.000',
        },
        'D',
        "m. 6'ya göre (II) sayılı tarifenin panel van ve motorlu karavan bölümündeki **sadece elektrik motoru olan** taşıtlardan motor gücü **115 kW'ı geçmeyenler birinci satırda**, geçenler ikinci satırda yer alan tutarların **%25'i** oranında vergilendirilir: 6.000 × %25 = **1.500 ₺**. İkinci satır kullanılırsa 2.250 ₺ bulunur.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 6',
    ),
    # düzey 2
    '0060': patch(
        "Aşağıdakilerden hangisi Motorlu Taşıtlar Vergisi Kanunu'ndaki tanımlara göre yanlıştır?",
        {
            'A': 'Arazi taşıtında bütün tekerlekler motordan güç alabilir',
            'B': 'Otomobil, sürücü dâhil en çok 8 oturma yeri olan araçtır',
            'C': 'Otobüs, sürücü dâhil en az 25 oturma yeri olan araçtır',
            'D': 'Troleybüsler otobüs sınıfına dâhildir',
            'E': 'Çekici, römork çekmek için imal edilen ve yük taşımayan araçtır',
        },
        'C',
        "m. 2'ye göre **otobüs sürücü dâhil en az 18 oturma yeri** olan araçtır; troleybüsler de bu sınıfa dâhildir. 25 kişi, (II) sayılı tarifede otobüslerin ilk kademesinin üst sınırıdır.",
        '197 sayılı Motorlu Taşıtlar Vergisi Kanunu m. 2',
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
    print(f"1 paket / {len(PATCHES)} soru ('Motorlu Tasitlar Vergisi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
