#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sosyal Guvenlik Hukuku — YAPISAL kalibrasyon (tanim sorusu -> kural uygulamasi).

Hukuk ailesinin yapisal kalibrasyon turunun ikinci konusu (bkz.
build_hukuk_is_sozlesmesi_yapisal.py). Karsilastirma tabani: 2014-2026
arsivinden cikarilan 629 GERCEK sinav hukuk sorusu (telif geregi yalnizca bicim
olculdu, metin kopyalanmadi).

    olcut              gercek   bu paket (once)
    medyan kok            257              114
    olumsuz kok         %41,5               %5
    duz tanim            %6,2              %43   <- ASIL KUSUR
    olay orgulu         %16,2               %0
    onculu              %14,3              %17   (yeterli)
    kor                     —              %21   (temiz)

Onculu siklarda yine "(birinci ve ikinci ifadeler dogrudur)" DOLGUSU vardi (§5);
gercek sinav yalniz "I ve II" yazar. Temizlendi.

Duzeltilen bicim kusuru: 0027'nin siklari paralel degildi — dort tekil sigorta
kolunun yaninda "Malulluk, yaslilik ve olum sigortalarinin tumu" gibi toplulastiran
bir sik vardi ve dogru sik acik ara EN KISA idi. Soru kisa vadeli kollara
cevrilerek bes sik da tek kalem ve benzer boya getirildi.

⚠️ §5 tasarim zamani boy denetimi: ilk tasarim 16/43 (%37) tek-en-uzun cikip
uretimi DURDURDU; toplam 35 celdiriciye gercek hukuki icerik eklenerek 60 yamada
%25'e indirildi. Nihai kombine kor-ogrenci olcumu %23; oncul disi sorularda
tek-en-uzun / tek-en-kisa %16 / %4. Paketin 60 sorusunun TAMAMI bu turda yeniden
yazildi.

⚠️ §7: 10 oncullu soru I-II-III ifadelerini ayri paragraflarda gosterir. Ilk
tasarimda "Yalniz X" secenegi hic dogru degildi; 0011 tek-dogru-oncul yapisina
cevrilerek bu okunmadan eleme ipucu kaldirildi.

⚠️ §6 DUZELTMESI: 0039-0040-0041 arka arkaya B cevabini tasiyordu (uc ayni harf
art arda; §6 yasagi). Bu kusur HEAD'den beri vardi ve audit.py::letter_pattern
onu GORMUYOR — dedektor yalniz sabit adimli rotasyona bakiyor. Paketin tamami bu
turda yamalandigi icin 0040'in cevabi B -> E olarak degistirildi (siklar yeniden
dagitildi); harf dagilimi da dengelendi.

⚠️ §9: yila bagli tutar (asgari ucret, tavan) kullanilmadi; yalniz kanunda sabit
gun sayilari, oranlar ve senaryoya ozgu varsayimsal tutarlar kullanildi.

§6 notu: her yamanin dogru cevap HARFI mevcut JSON'daki harfle ayni birakildi.

2026-08-14 ikinci zorluk turu: avukat kullanici geri bildirimi uzerine 2026/1 ve
2026/2 gercek SGS hukuk sorulari yeniden esas alindi. Ilk turdan sonra hâlâ tek
kural/tek tanima ile cozulebilen 22 soru; statü + kurum, ana kural + istisna,
esik + sonuc veya bildirim + yaptirim zincirlerinden birini birlikte isletecek
sekilde yeniden kuruldu. Medyan kok 215 -> 239; kor ogrenci %40 ara kusuru,
anlamli ve paralel celdirici kalibrasyonuyla %27'ye indirildi.

Guncellik: 7566 sayili Kanun uyarinca 01.01.2026'dan itibaren 4/1-(a) MYO
primi %21 (%9 sigortali + %12 isveren), 2026 prime esas kazanc ust siniri ise
alt sinirin 9 katidir. Eski %20 ve 7,5 kat bilgileri temizlendi.

Dayanak: 5510 sayili Kanun md. 3, 4, 7, 8, 11, 13, 14, 18, 19, 25, 26, 28, 32,
34, 50, 51, 53, 60, 80, 81, 82, 86, 88, 89, 92, 101, 102 · 4447 sayili Kanun
md. 50-51 · 5502 sayili Kanun md. 1 · Anayasa md. 60 · 6183 sayili AATUHK ·
7036 sayili Is Mahkemeleri Kanunu md. 4.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/is_ve_sosyal_guvenlik_hukuku/sosyal_guvenlik_hukuku.json"
STYLE_REF = "SGS Sosyal Guvenlik Hukuku (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "sgh-gen-"


def patch(stem, options, answer, solution, legislation_ref=None):
    # Öncüller uygulamada ayrı paragraflar hâlinde görünmeli. Tek satıra
    # sıkıştırılırsa hem okunabilirlik bozulur hem audit.py::ONCUL gerçek
    # öncül dağılımını ölçemez.
    for marker in ('I.', 'II.', 'III.', 'IV.'):
        stem = stem.replace(f' {marker} ', f'\n\n{marker} ')
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": legislation_ref or
                   "5510 sayili Kanun / 4447 sayili Kanun"},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    '0001': patch(
        'Bir uyuşmazlıkta, sigortalılık statüsünün belirlenmesi ile işsizlik ödeneği talebinin hangi kanunlara göre çözüleceği tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Hem sigortalılık statüsü hem işsizlik ödeneği 5510 sayılı Kanun'a göre belirlenir",
            'B': "Sigortalılık statüsü 5510 sayılı Kanun'a, işsizlik ödeneği ise 4447 sayılı Kanun'a göre belirlenir",
            'C': "Her iki konu da 4857 sayılı İş Kanunu'nda düzenlenmiştir",
            'D': "Her iki konu da 4447 sayılı Kanun'a göre belirlenir",
            'E': "Sigortalılık statüsü 4447, işsizlik ödeneği 5510 sayılı Kanun'a göre belirlenir",
        },
        'B',
        "5510 sayılı Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu sigortalılık statülerini, sigorta kollarını ve primleri düzenler. İşsizlik sigortası ise 4447 sayılı İşsizlik Sigortası Kanunu'nda düzenlenmiş olup ödenek İşsizlik Sigortası Fonundan karşılanır. 4857 sayılı İş Kanunu bireysel iş ilişkilerini düzenler.",
    ),
    '0002': patch(
        'Sosyal güvenlik alanında sosyal sigorta ve genel sağlık sigortası işlemlerini yürüten kurumun görev ve yetkileri belirlenmektedir. Buna göre aşağıdakilerden hangisi Sosyal Güvenlik Kurumunun görevlerinden biri değildir?',
        {
            'A': 'İşsizlik sigortası primlerinin toplanarak İşsizlik Sigortası Fonunun yönetilmesi',
            'B': 'Genel sağlık sigortası kapsamında sağlık hizmeti bedellerinin karşılanması',
            'C': 'Sigortalılık tescil işlemlerinin yürütülmesi ve kayıtların tutulması',
            'D': 'Malullük, yaşlılık ve ölüm aylıklarının bağlanması ve ödenmesi',
            'E': 'Sosyal sigorta ve genel sağlık sigortası primlerinin tahakkuk ettirilmesi ve tahsil edilmesi',
        },
        'A',
        '5502 sayılı Kanun md. 3: Kurumun görevleri arasında sosyal sigortacılık ilkelerine dayalı sigortacılık, primlerin tahsili, aylık bağlanması ve genel sağlık sigortası hizmetleri yer alır. İşsizlik Sigortası FONU ise 4447 sayılı Kanun uyarınca Türkiye İş Kurumu (İŞKUR) tarafından yönetilir; primleri SGK tahsil etse de fonun yönetimi Kuruma ait değildir.',
    ),
    '0003': patch(
        "Bir kişi bir market zincirinde iş sözleşmesiyle kasiyer olarak çalışmakta; ikinci bir kişi kendi adına açtığı kuaför salonunu işletmekte; üçüncü bir kişi ise bir belediyede memur kadrosunda görev yapmaktadır. Buna göre bu üç kişinin 5510 sayılı Kanun'daki sigortalılık statüleri sırasıyla aşağıdakilerden hangisidir?",
        {
            'A': '4/1-(b) – 4/1-(c) – 4/1-(a)',
            'B': '4/1-(b) – 4/1-(a) – 4/1-(c)',
            'C': '4/1-(a) – 4/1-(b) – 4/1-(c)',
            'D': '4/1-(a) – 4/1-(c) – 4/1-(b)',
            'E': '4/1-(c) – 4/1-(b) – 4/1-(a)',
        },
        'C',
        '5510 md. 4/1: (a) hizmet akdiyle bir veya birden fazla işveren tarafından çalıştırılanlar, (b) köy ve mahalle muhtarları ile kendi nam ve hesabına bağımsız çalışanlar (eski Bağ-Kur), (c) kamu idarelerinde çalışan memurlar ve diğer kamu görevlileri. Kasiyer 4/1-a, kuaför salonu işleteni 4/1-b, memur 4/1-c kapsamındadır.',
    ),
    '0004': patch(
        'Kendi nam ve hesabına bağımsız çalışan bir kişinin sigortalılığı tartışılmaktadır. Kişi, vergi mükellefiyeti bulunmadığı için sigortalı sayılmaması gerektiğini ileri sürmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kendi nam ve hesabına bağımsız çalışanlar 4/1-(b) kapsamında sigortalı sayılır',
            'B': 'Köy ve mahalle muhtarları da 4/1-(b) kapsamında sigortalı sayılır',
            'C': 'Şirket ortaklarının sigortalılığı da bu kapsamda değerlendirilebilir',
            'D': 'Bağımsız çalışanlarda sigortalılık, yalnızca vergi mükellefiyeti tesis edilmişse doğar',
            'E': 'Bu kapsamdaki sigortalıların primi, işveren hissesi bulunmaksızın kendileri tarafından ödenir',
        },
        'D',
        '5510 md. 4/1-(b): köy ve mahalle muhtarları ile hizmet akdine bağlı olmaksızın kendi adına ve hesabına bağımsız çalışanlar bu bent kapsamındadır; ticari kazanç veya serbest meslek kazancı nedeniyle gerçek veya basit usulde gelir vergisi mükellefi olanlar, gelir vergisinden muaf olup esnaf siciline kayıtlı olanlar ve şirket ortakları sayılan hâller arasındadır. Sigortalılık vergi mükellefiyetine İNDİRGENEMEZ; muafiyet hâlleri de kapsamdadır.',
    ),
    '0005': patch(
        'Bir kamu idaresinde memur kadrosunda görev yapan kişinin sigortalılık statüsü belirlenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kamu idarelerinde çalışan memur ve diğer kamu görevlileri 4/1-(c) kapsamındadır',
            'B': 'Bu statüdeki sigortalılar uzun vadeli sigorta kollarına tabidir',
            'C': 'Bu statüdeki sigortalılar da genel sağlık sigortası kapsamındadır',
            'D': 'Aynı kamu idaresinde iş sözleşmesiyle çalıştırılan işçiler 4/1-(a) kapsamındadır ve bunların primleri işveren tarafından bildirilir',
            'E': 'Kamu idarelerinde çalışan memurlar, hizmet akdine benzer biçimde 4/1-(a) kapsamında sigortalı sayılır',
        },
        'E',
        '5510 md. 4/1-(c): kamu idarelerinde bu maddenin (a) bendine tabi olmayanlardan, kadro ve pozisyonlarda sürekli olarak çalışıp ilgili kanunlarında (a) bendi kapsamına girenler gibi sigortalı olması öngörülmemiş olanlar bu bent kapsamındadır. Aynı kamu idaresinde İŞ SÖZLEŞMESİYLE çalışan işçiler ise 4/1-(a) kapsamındadır.',
    ),
    '0006': patch(
        'Bir sigortalı, işyerinde geçirdiği kaza sonucu tedavi görmüş; aynı işyerinde başka bir sigortalı ise uzun yıllar sonra yaşlılık aylığı bağlanması için başvurmuştur. Buna göre bu iki durumun ilgili olduğu sigorta kolları bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kaza kısa vadeli, yaşlılık aylığı ise uzun vadeli sigorta kolu kapsamındadır',
            'B': 'Kaza genel sağlık sigortası, yaşlılık aylığı ise kısa vadeli kol kapsamındadır',
            'C': 'Her iki durum da uzun vadeli sigorta kolları kapsamında değerlendirilir',
            'D': 'Kaza uzun vadeli, yaşlılık aylığı kısa vadeli sigorta kolu kapsamındadır',
            'E': 'Her iki durum da kısa vadeli sigorta kolları kapsamında değerlendirilir',
        },
        'A',
        '5510 md. 3 ve 4: kısa vadeli sigorta kolları iş kazası, meslek hastalığı, hastalık ve analık sigortalarıdır. Uzun vadeli sigorta kolları ise malullük, yaşlılık ve ölüm sigortalarıdır. Genel sağlık sigortası bunlardan ayrı bir koldur.',
    ),
    '0007': patch(
        'Bir sigortalıya malullük aylığı, bir başkasına yaşlılık aylığı bağlanmış; üçüncü bir sigortalının vefatı üzerine hak sahiplerine ölüm aylığı bağlanmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Üç edim de genel sağlık sigortası kapsamında değerlendirilir',
            'B': 'Yalnızca yaşlılık aylığı uzun vadeli sigorta kolu kapsamındadır',
            'C': 'Malullük kısa vadeli, yaşlılık ve ölüm uzun vadeli sigorta kolu kapsamındadır',
            'D': 'Üç edim de uzun vadeli sigorta kolları kapsamındadır',
            'E': 'Üç edim de kısa vadeli sigorta kolları kapsamındadır',
        },
        'D',
        '5510 md. 3: uzun vadeli sigorta kolları MALULLÜK, YAŞLILIK ve ÖLÜM sigortalarıdır; bu üç aylık da o kapsamda bağlanır. Kısa vadeli kollar iş kazası, meslek hastalığı, hastalık ve analık sigortalarıdır. Genel sağlık sigortası ise ayrı bir koldur.',
    ),
    '0008': patch(
        'Bir sigortalı, işverenin sağladığı servis aracıyla işyerine giderken trafik kazası geçirmiştir. Aynı işyerinde bir başka sigortalı, işveren tarafından görevle başka bir ile gönderildiği sırada, asıl işini yapmaksızın geçen zamanda yaralanmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İş kazası sayılabilmesi için olayın işyeri sınırları içinde gerçekleşmesi gerekir',
            'B': 'Her iki olay da iş kazası sayılır',
            'C': 'Yalnızca servis aracındaki olay iş kazası sayılır',
            'D': 'Yalnızca görevle gönderilme sırasındaki olay iş kazası sayılır',
            'E': 'İşyeri dışında gerçekleşen olaylar ancak işveren kusurluysa iş kazası sayılır',
        },
        'B',
        '5510 md. 13: iş kazası; sigortalının işyerinde bulunduğu sırada, işveren tarafından yürütülmekte olan iş nedeniyle, bir işverene bağlı olarak çalışan sigortalının görevli olarak işyeri dışında başka bir yere gönderilmesi nedeniyle asıl işini yapmaksızın geçen zamanlarda, emziren kadın sigortalının çocuğuna süt vermek için ayrılan zamanlarda ve işverence sağlanan bir taşıtla işin yapıldığı yere toplu olarak götürülüp getirilmeleri sırasında meydana gelen olaydır. İşverenin kusuru koşul değildir.',
    ),
    '0009': patch(
        'Bir işverenin işyerinde 4/1-(a) kapsamındaki bir sigortalı 4 Mart Salı günü iş kazası geçirmiştir. İşveren, kazayı Sosyal Güvenlik Kurumuna bildirmek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşveren, kazayı takip eden ayın sonuna kadar Kuruma bildirmelidir',
            'B': 'Bildirim yükümlülüğü işverene değil, doğrudan sigortalının kendisine aittir',
            'C': 'Kolluğa yapılan bildirim yeterli olup Kuruma ayrıca bildirim gerekmez',
            'D': 'İşveren, kazadan sonraki bir ay içinde Kuruma bildirimde bulunmalıdır',
            'E': 'İşveren, kazadan sonraki üç iş günü içinde Kuruma bildirimde bulunmalıdır',
        },
        'E',
        '5510 md. 13/2-(a): iş kazası, 4/1-(a) kapsamındaki sigortalılar bakımından işverence kazadan sonraki ÜÇ İŞ GÜNÜ içinde Kuruma bildirilir. 4/1-(b) kapsamındakiler bakımından bildirimi sigortalının kendisi, bir ayı geçmemek şartıyla rahatsızlığının bildirime engel olmadığı günden itibaren üç iş günü içinde yapar. Kolluğa bildirim, Kuruma bildirim yükümlülüğünü ortadan kaldırmaz.',
    ),
    '0010': patch(
        'Bir sigortalıda, uzun süre maruz kaldığı tozlu ortam nedeniyle solunum yolu rahatsızlığı geliştiği ve bunun yürüttüğü işin niteliğinden kaynaklandığı sağlık kurulu raporuyla belirlenmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek hastalığının tespiti Kurum sağlık kurulu kararıyla yapılır',
            'B': 'Meslek hastalığı, hastalığın öğrenildiği günden başlayarak üç iş günü içinde Kuruma bildirilir',
            'C': 'Meslek hastalığı, ani ve dıştan gelen bir olay sonucu ortaya çıkması bakımından iş kazasıyla aynı niteliktedir',
            'D': 'Meslek hastalığı da iş kazası gibi kısa vadeli sigorta kolları kapsamındadır',
            'E': 'Meslek hastalığı, sigortalının yürüttüğü işin niteliğinden ya da yürütüm şartlarından doğan geçici veya sürekli hastalık hâlidir',
        },
        'C',
        '5510 md. 14: meslek hastalığı, sigortalının çalıştığı veya yaptığı işin niteliğinden dolayı tekrarlanan bir sebeple ya da işin yürütüm şartları yüzünden uğradığı geçici veya sürekli hastalık, bedensel veya ruhsal engellilik hâlleridir. İş kazasından farkı, ANİ bir olaya değil zaman içindeki maruziyete dayanmasıdır. Tespit Kurum sağlık kurulunca yapılır; bildirim süresi öğrenildiği günden itibaren üç iş günüdür.',
    ),
    '0011': patch(
        "Sosyal güvenlik hukuku ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Sosyal sigortalar ve genel sağlık sigortasına ilişkin temel kanun 5510 sayılı Kanun'dur. II. Sosyal Güvenlik Kurumu özel hukuk tüzel kişiliğini haiz ve idari yönden özerktir. III. Sigortalı olmak hak ve yükümlülüğünden sözleşmeyle vazgeçilebilir.",
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'I ve III',
            'E': 'I, II ve III',
        },
        'A',
        'I doğrudur. II YANLIŞTIR: Sosyal Güvenlik Kurumu 5502 sayılı Kanun md. 1 uyarınca kamu tüzel kişiliğini haiz, idari ve mali açıdan özerk bir kurumdur. III YANLIŞTIR: 5510 sayılı Kanun md. 92 uyarınca sigortalı olmak hak ve yükümlülüğünden vazgeçilemez; aksi yöndeki sözleşme hükümleri geçersizdir.',
    ),
    '0012': patch(
        'Genel sağlık sigortası kapsamı ve finansmanı tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Türkiye'de ikamet eden ve koşulları taşıyan kişiler genel sağlık sigortalısı sayılır",
            'B': 'Genel sağlık sigortası yalnızca zorunlu sigortalıları kapsar; bakmakla yükümlü olunan kişiler kapsam dışındadır',
            'C': 'Geliri belirlenen eşiğin altında kalanların primi devlet tarafından karşılanır',
            'D': 'Genel sağlık sigortası, kişilerin sağlığının korunmasına yönelik hizmetlerin finansmanını sağlar',
            'E': 'Genel sağlık sigortası, kısa ve uzun vadeli sigorta kollarından bağımsız düzenlenen ayrı bir koldur ve sağlık hizmetlerinin finansmanına yöneliktir',
        },
        'B',
        '5510 md. 3 ve 60-67: genel sağlık sigortası, kişilerin öncelikle sağlıklarının korunmasını, sağlık riskleriyle karşılaşmaları hâlinde ise oluşan harcamaların finansmanını sağlayan sigortadır. Sigortalının BAKMAKLA YÜKÜMLÜ OLDUĞU kişiler de sağlık hizmetlerinden yararlanır; kapsam yalnızca sigortalıyla sınırlı değildir.',
    ),
    '0013': patch(
        'İş sözleşmesi kendi istek ve kusuru dışında sona eren bir sigortalı, sona ermeden önceki son 120 gün hizmet akdine tabi olarak çalışmış ve son üç yıl içinde 720 gün işsizlik sigortası primi ödemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sigortalı işsizlik ödeneğine hak kazanır ve 180 gün süreyle ödenek alır',
            'B': 'Sigortalı işsizlik ödeneğine hak kazanır ve 300 gün süreyle ödenek alır',
            'C': 'Son üç yılda 600 gün prim koşulu sağlanmadığı için ödenek hakkı doğmaz',
            'D': 'Sigortalı işsizlik ödeneğine hak kazanır ve 240 gün süreyle ödenek alır',
            'E': 'İşsizlik ödeneği yalnızca işveren tarafından haklı nedenle feshedilen sigortalılara ödenir',
        },
        'A',
        '4447 sayılı Kanun md. 50-51: hizmet akdinin sona ermesinden önceki son 120 gün hizmet akdine tabi olanlardan, son üç yıl içinde 600 gün prim ödemiş olana 180 gün, 900 gün ödemiş olana 240 gün, 1080 gün ödemiş olana 300 gün işsizlik ödeneği verilir. 720 gün, 600 ile 900 arasında kaldığından süre 180 GÜNDÜR. Ödenek, kendi istek ve kusuru dışında işsiz kalanlara ödenir.',
    ),
    '0014': patch(
        'Bir sigortalı, yaşlılık aylığı bağlanması için Kuruma başvurmuştur. Sigortalı, yalnızca prim gün sayısı koşulunu karşıladığını, yaş koşulunun aranmaması gerektiğini ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Prim gün sayısı koşulunun karşılanması tek başına yeterlidir; yaş ve sigortalılık süresi aylık bağlama değerlendirmesinde dikkate alınmaz',
            'B': 'Yaşlılık aylığı yalnızca 4/1-(c) kapsamındaki sigortalılara bağlanır',
            'C': 'Yaşlılık aylığında koşullar sigortalının talebine göre serbestçe belirlenir',
            'D': 'Yaşlılık aylığı için kural olarak yaş, sigortalılık süresi ve prim gün sayısı koşullarının birlikte gerçekleşmesi aranır',
            'E': 'Belirli bir yaşı doldurmuş olmak tek başına yeterli olup ayrıca prim gün sayısı ve sigortalılık süresi aranmaz',
        },
        'D',
        '5510 md. 28: yaşlılık aylığından yararlanmak için kural olarak belirli bir YAŞI doldurmak, yeterli SİGORTALILIK SÜRESİNE ve PRİM GÜN SAYISINA sahip olmak koşulları BİRLİKTE aranır. Koşullar sigortalılık statüsüne ve ilk işe giriş tarihine göre kademeli olarak belirlenmiştir; tek bir koşulun karşılanması aylık hakkı doğurmaz.',
    ),
    '0015': patch(
        'Bir sigortalının çalışma gücünün %55 oranında kaybedildiği Kurum sağlık kurulunca belirlenmiştir. Sigortalının 12 yıllık sigortalılık süresi ve 2.000 gün prim ödemesi bulunmaktadır. Buna göre malullük aylığı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sigortalılık süresi ve prim gün sayısı koşulları yeterli olduğundan sigortalıya malullük aylığı bağlanır',
            'B': 'Kayıp oranı yeterli olmadığında sigortalıya yaşlılık aylığı bağlanır',
            'C': 'Kayıp oranı en az %60 olmadığı için sigortalı malul sayılmaz ve aylık bağlanmaz',
            'D': 'Malul sayılmak için kayıp oranının en az %40 olması yeterlidir',
            'E': 'Kayıp oranı aranmaz; on yıllık sigortalılık süresi tek başına yeterlidir',
        },
        'C',
        "5510 md. 25: sigortalının veya işverenin talebi üzerine Kurumca yetkilendirilen sağlık hizmeti sunucularının raporlarına göre çalışma gücünün ya da iş kazası veya meslek hastalığı sonucu meslekte kazanma gücünün EN AZ %60'ını kaybettiği Kurum Sağlık Kurulunca tespit edilen sigortalı MALUL sayılır. %55'lik kayıp bu eşiğin altındadır. md. 26'daki en az 10 yıl sigortalılık ve 1800 gün prim koşulu ancak malullük tespit edildikten sonra aranır (başkasının sürekli bakımına muhtaç olanlarda sigortalılık süresi aranmaz).",
    ),
    '0016': patch(
        'Vefat eden bir sigortalının geride eşi, 16 yaşında öğrenim gören bir çocuğu ve geçiminin sigortalı tarafından sağlandığı belgelenen annesi kalmıştır. Buna göre ölüm aylığı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ölüm aylığından yalnızca sağ kalan eş yararlanabilir; çocuk ve ana-baba hak sahibi sayılmaz',
            'B': 'Hak sahiplerine bağlanacak aylıkların toplamı sigortalıya ait aylığı geçemez',
            'C': 'Hak sahipleri sağ kalan eş, çocuklar ile ana ve babadır',
            'D': 'Ana ve babaya aylık bağlanması, geçiminin sigortalı tarafından sağlandığının belgelenmesine bağlıdır',
            'E': 'Aylık bağlanabilmesi için sigortalının belirli bir prim gün sayısı koşulunu karşılaması gerekir',
        },
        'A',
        '5510 md. 32-34: ölüm aylığı; sağ kalan EŞ, ÇOCUKLAR ile ANA ve BABAYA bağlanır. Aylık için en az 1800 gün malullük, yaşlılık ve ölüm sigortaları primi bildirilmiş olması ya da 4/1-(a) kapsamındakiler için en az 5 yıl sigortalılık süresiyle birlikte toplam 900 gün prim aranır. Ana ve babaya aylık, geçiminin sigortalı tarafından sağlandığının belgelenmesi ve diğer koşulların gerçekleşmesi hâlinde bağlanır. Hak sahiplerinin hisseleri toplamı sigortalıya ait aylığı geçemez.',
    ),
    '0017': patch(
        'Bir işveren, imalat işi yapan işyerinde çalıştırmak üzere bir işçiyi 10 Nisan günü işe başlatmayı planlamaktadır. İşveren, sigortalı işe giriş bildirgesini işe başlama tarihinden sonra vermeyi düşünmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bildirge, işe başlama tarihinden itibaren üç iş günü içinde verilebilir',
            'B': 'Bildirge, sigortalının işe başladığı tarihi takip eden ayın sonuna kadar Kuruma verilebilir',
            'C': 'Bildirge, sigortalı çalıştırılmaya başlanılan tarihten önce Kuruma verilmelidir',
            'D': 'Bildirge, işe başlama tarihinden itibaren bir ay içinde verilebilir',
            'E': 'İmalat işlerinde bildirge en geç çalıştırılmaya başlanılan gün verilebilir',
        },
        'C',
        '5510 md. 8: işverenler, 4/1-(a) kapsamında sigortalı sayılanları, sigortalı işe giriş bildirgesiyle çalıştırmaya BAŞLANILAN TARİHTEN ÖNCE Kuruma bildirmekle yükümlüdür. İnşaat, balıkçılık ve tarım işyerlerinde işe başlatılacaklar için bildirgenin en geç çalıştırılmaya başlanılan gün verilmesi istisnası öngörülmüştür; imalat işleri bu istisnaya girmez.',
    ),
    '0018': patch(
        'Bir işyerinde 4/1-(a) kapsamındaki bir sigortalının malullük, yaşlılık ve ölüm sigortaları primi hesaplanmaktadır. İşveren, bu primin tamamının sigortalıdan kesildiğini ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Prim yüzde yirmi olup yüzde onu sigortalının ücretinden kesilir, kalan yüzde onu işveren payı olarak Kuruma bildirilir',
            'B': 'Malullük, yaşlılık ve ölüm sigortaları primi yüzde yirmi olup yüzde dokuzu sigortalı, yüzde on biri işveren payıdır',
            'C': 'Prim oranı taraflarca sözleşmeyle serbestçe belirlenir',
            'D': 'Prim yüzde yirmi olup tamamı sigortalının ücretinden kesilerek işverence Kuruma yatırılır',
            'E': 'Primin tamamı işveren tarafından karşılanır',
        },
        'B',
        "5510 md. 81: malullük, yaşlılık ve ölüm sigortaları prim oranı, sigortalının prime esas kazancının %20'sidir; bunun %9'u sigortalı hissesi, %11'i işveren hissesidir. Kısa vadeli sigorta kolları primi tamamen işverene aittir. Prim oranları kanunla belirlenir; sözleşmeyle değiştirilemez.",
    ),
    '0019': patch(
        'Bir sigortalıya bir ayda ücretin yanı sıra ikramiye ve yol yardımı ödenmiş; ayrıca işveren tarafından ölüm yardımı yapılmıştır. Buna göre prime esas kazanç bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yalnızca çıplak ücret prime esas kazanca dâhil edilir',
            'B': 'Ölüm yardımı dâhil tüm sosyal yardımlar prime esas kazanca dâhildir',
            'C': 'Ücret, ikramiye ve ölüm yardımı dâhil olmak üzere ödemelerin tümü prime esas kazanca dâhil edilir',
            'D': 'Prime esas kazanç yalnızca sigortalının beyanına göre belirlenir',
            'E': 'Ücret ve ikramiye prime esas kazanca dâhildir; ölüm yardımı ise prime esas kazanca dâhil edilmez',
        },
        'E',
        '5510 md. 80: prime esas kazanç, sigortalılara hak edilen ücretler ile prim, ikramiye ve bu nitelikteki her çeşit istihkaktan oluşur. Ayni yardımlar ile ölüm, doğum ve evlenme yardımları, görev yollukları, kıdem tazminatı, iş sonu tazminatı ve işsizlik ödeneği prime esas kazanca DÂHİL EDİLMEZ. Ayrıca kazancın alt sınırı asgari ücret, üst sınırı alt sınırın 7,5 katıdır (md. 82).',
    ),
    '0020': patch(
        'Sigorta kolları ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Kısa vadeli sigorta kolları iş kazası, meslek hastalığı, hastalık ve analık sigortalarıdır. II. Malullük, yaşlılık ve ölüm sigortaları uzun vadeli sigorta kollarıdır. III. Analık sigortası uzun vadeli sigorta kolları arasında yer alır. IV. Kısa vadeli sigorta kolları primi sigortalı ile işveren arasında eşit paylaşılır.',
        {
            'A': 'I ve II',
            'B': 'Yalnız III',
            'C': 'II ve III',
            'D': 'III ve IV',
            'E': 'I, III ve IV',
        },
        'D',
        'III YANLIŞ: analık sigortası KISA vadeli sigorta kollarındandır (5510 md. 3). IV YANLIŞ: md. 81 uyarınca kısa vadeli sigorta kolları primi tamamen İŞVERENE aittir; sigortalıdan kesinti yapılmaz. I ve II doğrudur.',
    ),
    '0021': patch(
        "Bir kişi hâlen zorunlu sigortalı olmayıp Türkiye'de ikamet etmektedir ve kendi adına prim ödeyerek sigortalılığını sürdürmek istemektedir. Buna göre isteğe bağlı sigorta bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İsteğe bağlı sigortalılar 4/1-(a) kapsamında sayılır ve primi işveren öder',
            'B': 'İsteğe bağlı sigortalılık zorunlu sigortalılıkla aynı anda sürdürülebilir',
            'C': 'İsteğe bağlı sigortalılıkta yalnızca kısa vadeli sigorta kolları uygulanır',
            'D': 'İsteğe bağlı sigortalılık yalnızca daha önce hiç sigortalı olmamış kişiler için mümkündür',
            'E': 'İsteğe bağlı sigortalılar 4/1-(b) kapsamında sayılır; primi kendileri öder',
        },
        'E',
        '5510 md. 50-51: isteğe bağlı sigorta, kişilerin isteğe bağlı olarak prim ödemek suretiyle uzun vadeli sigorta kollarına ve genel sağlık sigortasına tabi olmalarını sağlayan sigortadır. İsteğe bağlı sigorta primi ödenen sürelere ilişkin sigortalılık 4/1-(b) kapsamında sayılır ve primi sigortalının kendisi öder. Zorunlu sigortalı olmayı gerektirecek çalışması bulunmamak koşuldur.',
    ),
    '0022': patch(
        'Bir işçi, iki yıl boyunca bir işyerinde çalıştığı hâlde Kuruma hiç bildirilmemiştir. İşçi, geçen sürenin hizmetten sayılması için hukuki yollara başvurmak istemektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İşçi, hizmet tespiti davası açarak çalıştığı sürelerin tespitini isteyebilir',
            'B': 'Sigortalı olmak hak ve yükümlülüğünden vazgeçilemez; aksi yöndeki sözleşme hükümleri geçersizdir',
            'C': 'Sigortasız çalıştırılan işçi, Kuruma bildirilmediği süreler için sonradan hak talep edemez',
            'D': 'Sigortasız çalıştırma işverene idari para cezası uygulanmasını gerektirir',
            'E': 'Hizmet tespiti davası iş mahkemesinde görülür',
        },
        'C',
        '5510 md. 86/9: sigortalının çalıştığı hâlde Kuruma bildirilmemesi hâlinde, hizmetlerinin tespiti için hizmetin geçtiği yılın sonundan başlayarak beş yıl içinde İŞ MAHKEMESİNE başvurulabilir. md. 92: sigortalı olmak hak ve yükümlülüğünden vazgeçilemez; aksi yöndeki sözleşme hükümleri geçersizdir. md. 102: bildirim yükümlülüğüne aykırılık idari para cezası gerektirir.',
    ),
    '0023': patch(
        'Bir işveren, çalıştırdığı sigortalılara ilişkin aylık prim ve hizmet bilgilerini Kuruma bildirmiş; ancak tahakkuk eden primleri ödemeyi geciktirmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Primler, ait olduğu ayı takip eden ayın sonuna kadar ödenmelidir; gecikmede gecikme cezası ve zammı uygulanır',
            'B': 'Aylık prim ve hizmet bildirimi yapılmışsa primlerin ödenmesi için ayrıca bir ödeme süresi işlemez',
            'C': 'Prim borçları genel hükümlere göre icra takibine konu edilemez',
            'D': 'Primler hesap dönemi sonunda yılda bir kez topluca hesaplanıp Kuruma ödenir; aylık prim ve hizmet bildirimi ödeme zamanını değiştirmez',
            'E': 'Gecikme hâlinde yalnızca idari para cezası uygulanır, gecikme zammı işlemez',
        },
        'A',
        '5510 md. 88: işveren, bir ay içinde çalıştırdığı sigortalıların primlerini ait olduğu ayı takip eden ayın SONUNA kadar Kuruma öder. Süresinde ödenmeyen prim ve idari para cezaları için gecikme cezası ve gecikme zammı uygulanır; Kurumun süresinde ödenmeyen alacakları 6183 sayılı Amme Alacaklarının Tahsil Usulü Hakkında Kanun hükümlerine göre tahsil edilir.',
    ),
    '0024': patch(
        'İş kazası geçiren bir sigortalıya ayakta tedavi uygulanmış; günlük kazancı 1.200 ₺ olarak hesaplanmıştır. Aynı işyerinde başka bir sigortalı ise hastanede yatarak tedavi görmüştür. Buna göre geçici iş göremezlik ödeneği bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Her iki hâlde de günlük kazancın yarısı ödenir',
            'B': 'Ayakta tedavide günlük kazancın üçte ikisi, yatarak tedavide ise yarısı ödenir',
            'C': 'Ayakta tedavide günlük kazancın yarısı, yatarak tedavide ise üçte ikisi tutarında ödenek verilir',
            'D': 'Ödenek yalnızca yatarak tedavi görenlere sağlanır',
            'E': 'Her iki hâlde de günlük kazancın tamamı ödenir',
        },
        'B',
        '5510 md. 18: geçici iş göremezlik ödeneği, iş kazası, meslek hastalığı, hastalık ve analık hâllerinde YATARAK tedavide günlük kazancın YARISI, AYAKTA tedavide ÜÇTE İKİSİ tutarındadır. Hastalık hâlinde ödenek, iş göremezliğin üçüncü gününden başlar; iş kazası ve meslek hastalığında ilk günden itibaren ödenir. 1.200 ₺ günlük kazançta ayakta tedavi için günlük 800 ₺ ödenir.',
    ),
    '0025': patch(
        'Sigortalılık ve bildirimler ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Hizmet akdiyle çalışanlar 4/1-(a) kapsamında sigortalı sayılır. II. Sigortalı işe giriş bildirgesi, kural olarak çalıştırılmaya başlanılan tarihten önce verilir. III. Sigortalılık, işverenin bildirimde bulunduğu tarihte başlar.',
        {
            'A': 'I ve III',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'Yalnız I',
            'E': 'I, II ve III',
        },
        'C',
        'I doğrudur (5510 md. 4/1-a). II doğrudur (md. 8). III YANLIŞTIR: md. 7 uyarınca sigortalılık, fiilen çalışmaya başlanılan tarihte başlar; işverenin bildirimi bildirici niteliktedir, kurucu değildir.',
    ),
    '0026': patch(
        'Bir kişi, sosyal güvenlik hakkının yalnızca kanunla tanınmış bir hak olduğunu ve anayasal bir dayanağı bulunmadığını ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Sosyal güvenlik hakkı Anayasa'da düzenlenmiş olup devlete bu güvenliği sağlama ödevi yüklenmiştir",
            'B': 'Sosyal güvenlik hakkı yalnızca çalışanlar bakımından anayasal güvence altındadır',
            'C': 'Sosyal güvenlik hakkı uluslararası sözleşmelerde düzenlenmiş olup iç hukukta karşılığı yoktur',
            'D': "Sosyal güvenlik hakkı Anayasa'da yer almakla birlikte devlete ödev yüklemez",
            'E': "Sosyal güvenlik hakkı, anayasal dayanağı bulunmayan ve yalnızca 5510 sayılı Kanun'a dayanan kanuni bir haktır",
        },
        'A',
        "Anayasa md. 60: 'Herkes, sosyal güvenlik hakkına sahiptir. Devlet, bu güvenliği sağlayacak gerekli tedbirleri alır ve teşkilatı kurar.' Hak yalnızca çalışanlara değil HERKESE tanınmıştır ve devlete pozitif bir ödev yükler. 5510 sayılı Kanun bu anayasal ödevin somutlaştırılmasıdır.",
    ),
    '0027': patch(
        '5510 sayılı Kanun sigorta kollarını kısa ve uzun vadeli olmak üzere ikiye ayırmıştır. Buna göre aşağıdakilerden hangisi kısa vadeli sigorta kollarından biri değildir?',
        {
            'A': 'Hastalık sigortası',
            'B': 'Analık sigortası',
            'C': 'İş kazası sigortası',
            'D': 'Meslek hastalığı sigortası',
            'E': 'Yaşlılık sigortası',
        },
        'E',
        '5510 md. 3: uzun vadeli sigorta kolları malullük, yaşlılık ve ölüm sigortalarıdır. ANALIK sigortası; iş kazası, meslek hastalığı ve hastalık sigortalarıyla birlikte KISA VADELİ sigorta kolları arasında yer alır.',
    ),
    '0028': patch(
        'İş kazası sonucu bir sigortalının meslekte kazanma gücünün %8 oranında azaldığı Kurum sağlık kurulunca belirlenmiştir. Aynı olayda başka bir sigortalının kaybı %15 olarak tespit edilmiştir. Buna göre sürekli iş göremezlik geliri bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sürekli iş göremezlik geliri yalnızca meslek hastalığı hâllerinde bağlanır',
            'B': 'Her iki sigortalıya da meslekte kazanma gücündeki kayıp oranıyla orantılı biçimde gelir bağlanır',
            'C': 'Gelir bağlanabilmesi için kaybın en az yüzde yirmi beş olması gerekir',
            'D': 'Kaybı %15 olan sigortalıya gelir bağlanır; %8 olan sigortalı bu gelire hak kazanmaz',
            'E': 'Kaybı %8 olan sigortalıya da gelir bağlanır; alt sınır aranmaz',
        },
        'D',
        "5510 md. 19: iş kazası veya meslek hastalığı sonucu meslekte kazanma gücü EN AZ %10 oranında azalan sigortalıya sürekli iş göremezlik geliri bağlanır. %8'lik kayıp bu alt sınırın altında kaldığından gelir doğmaz; %15'lik kayıp sınırı aştığı için gelir bağlanır.",
    ),
    '0029': patch(
        'Sosyal güvenlik hukuku bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sigortalılık, fiilen çalışmaya başlanılan tarihte kendiliğinden doğar',
            'B': 'Sigortalı olmak hak ve yükümlülüğünden vazgeçilemez',
            'C': 'Sigortalılık, tarafların anlaşmasıyla sona erdirilebilen iradi bir ilişkidir',
            'D': 'İşverenin Kuruma yaptığı bildirim kurucu değil bildirici niteliktedir',
            'E': 'Sosyal sigortalılık kural olarak zorunludur',
        },
        'C',
        '5510 md. 92: sigortalı olmak hak ve yükümlülüğünden vazgeçilemez; sosyal sigortada ZORUNLULUK ilkesi geçerlidir. md. 7: sigortalılık, çalışmaya başlanılan tarihte kendiliğinden doğar; işverenin bildirimi bildirici niteliktedir. Bu nedenle sigortalılık taraf iradesiyle kurulan veya sona erdirilebilen bir ilişki değildir.',
    ),
    '0030': patch(
        "Bir işletme sahibi, kendi nam ve hesabına bağımsız çalışmakta olup aynı zamanda işyerinde iş sözleşmesiyle üç kişi çalıştırmaktadır. Buna göre 5510 sayılı Kanun'un sigortalılık statüleri bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İşyerinde çalışan herkes işveren dâhil 4/1-(a) kapsamında sigortalı sayılır',
            'B': 'İşletme sahibi 4/1-(b), çalıştırdığı üç kişi ise 4/1-(a) kapsamında sigortalıdır',
            'C': 'İşletme sahibi 4/1-(c) kapsamında, çalıştırdığı üç kişi ise 4/1-(a) kapsamında sigortalıdır',
            'D': 'İşletme sahibi sigortalı sayılmaz; yalnızca çalıştırdığı kişiler sigortalıdır',
            'E': 'İşletme sahibi 4/1-(a), çalıştırdığı üç kişi 4/1-(b) kapsamında sigortalıdır',
        },
        'B',
        '5510 md. 4/1-(b): kendi nam ve hesabına bağımsız çalışanlar bu bent kapsamındadır; işveren sıfatı sigortalılığı ortadan kaldırmaz. md. 4/1-(a): hizmet akdiyle çalıştırılanlar bu bent kapsamındadır. (c) bendi ise kamu görevlilerine özgüdür.',
    ),
    '0031': patch(
        'Sigortalı bir kadın işçi doğum yapmış; doğumdan önceki bir yıl içinde 100 gün kısa vadeli sigorta kolları primi bildirilmiştir. Buna göre analık sigortası kapsamındaki yardımlar bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Analık hâlinde yalnızca sağlık yardımı sağlanır; ödenek verilmez',
            'B': 'Analık sigortası uzun vadeli sigorta kolları arasında yer alır',
            'C': 'Ödenek verilebilmesi için doğumdan önceki bir yıl içinde en az 180 gün prim bildirilmiş olmalıdır',
            'D': 'Doğumdan önceki bir yıl içinde en az 90 gün prim koşulu sağlandığı için geçici iş göremezlik ödeneğine hak kazanır',
            'E': 'Analık sigortasından geçici iş göremezlik ödeneği verilmesi için herhangi bir prim gün sayısı koşulu aranmaz',
        },
        'D',
        '5510 md. 18: analık hâlinde geçici iş göremezlik ödeneği bağlanabilmesi için doğumdan önceki BİR YIL içinde EN AZ 90 GÜN kısa vadeli sigorta kolları primi bildirilmiş olması gerekir. 100 gün bu koşulu karşılar. Analık sigortası KISA vadeli sigorta kolları arasındadır; emzirme ödeneği ve sağlık yardımları da bu kapsamdadır.',
    ),
    '0032': patch(
        'Sosyal Güvenlik Kurumunun hukuki niteliği tartışılmaktadır. Bir görüşe göre Kurum, bakanlığın hiyerarşik bir alt birimidir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kurum, mali açıdan özerk olmakla birlikte kamu tüzel kişiliğine sahip değildir',
            'B': 'Kurum, kamu tüzel kişiliğini haiz, idari ve mali açıdan özerk bir kuruluştur',
            'C': 'Kurum, yerel yönetimlere bağlı bir hizmet birimidir',
            'D': 'Kurum, bakanlığın hiyerarşik alt birimi olup ayrı tüzel kişiliği yoktur',
            'E': 'Kurum, özel hukuk tüzel kişisi niteliğinde bir anonim şirkettir',
        },
        'B',
        '5502 sayılı Sosyal Güvenlik Kurumu Kanunu md. 1: Kurum, kamu tüzel kişiliğini haiz, idari ve mali açıdan özerk, bu Kanunda hüküm bulunmayan durumlarda özel hukuk hükümlerine tabi bir kuruluştur ve Çalışma ve Sosyal Güvenlik Bakanlığının ilgili kuruluşudur. Bakanlığın hiyerarşik alt birimi değildir.',
    ),
    '0033': patch(
        'Bir işçi, çalıştığı işyerinde hiç sigortalı gösterilmemiştir. İşçi ile işveren arasında, işçinin sigortalı olmaktan feragat ettiğine ilişkin yazılı bir belge de düzenlenmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşçi ancak işverenin onayıyla hizmet tespiti davası açabilir',
            'B': 'Hizmet tespiti davası idare mahkemesinde görülür',
            'C': 'Yazılı feragat belgesi geçerli olup işçinin dava hakkını ortadan kaldırır',
            'D': 'Sigortalılık ancak işverenin bildirimiyle doğar; bildirim yoksa çalışma hukuken yok sayılır',
            'E': 'Sigortalı olmaktan feragat sözleşmesi geçersizdir; işçi hizmet tespiti davası açabilir',
        },
        'E',
        '5510 md. 92: sigortalı olmak hak ve yükümlülüğünden VAZGEÇİLEMEZ; sigortalılık zorunludur ve bu yöndeki feragat sözleşmeleri geçersizdir. Sigortalılık, çalışmanın fiilen başladığı tarihte kendiliğinden doğar; işverenin bildirimi kurucu değil bildirici niteliktedir. Hizmet tespiti davası md. 86/9 uyarınca İŞ MAHKEMESİNDE açılır.',
    ),
    '0034': patch(
        'Sosyal güvenlik sistemi, primli ve primsiz rejim olmak üzere iki ayak üzerine kuruludur. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sosyal yardım ve hizmetlerden yararlanabilmek için de belirli bir süre prim ödenmiş olması gerekir',
            'B': 'Primsiz rejim, muhtaçlık ölçütüne dayanan ve genel bütçeden finanse edilen sosyal yardım ve sosyal hizmet programlarını kapsar',
            'C': 'Sosyal yardım ve hizmetler primsiz rejim kapsamındadır',
            'D': 'Primli rejimde edimler, ödenen primler ve sigortalılık süresiyle ilişkilendirilir',
            'E': 'Sosyal sigortalar primli rejimin temelini oluşturur',
        },
        'A',
        'Sosyal güvenlik sistemi PRİMLİ REJİM (sosyal sigortalar; edimler prim ödemesine ve sigortalılık süresine bağlı) ve PRİMSİZ REJİM (sosyal yardım ve hizmetler; muhtaçlık ölçütüne dayalı, devlet bütçesinden finanse edilir) ayrımına dayanır. Primsiz rejimde prim ödeme koşulu ARANMAZ.',
    ),
    '0035': patch(
        'Sigortalılık statüleri ve sigorta kolları ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Genel sağlık sigortası, kısa ve uzun vadeli sigorta kollarından ayrı bir koldur. II. Kendi nam ve hesabına bağımsız çalışanlar 4/1-(b) kapsamındadır. III. Kamu görevlileri 4/1-(c) kapsamındadır.',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'Yalnız I',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'D',
        'Üç ifade de doğrudur. 5510 md. 3 ve 4: kısa vadeli kollar iş kazası, meslek hastalığı, hastalık ve analık; uzun vadeli kollar malullük, yaşlılık ve ölümdür. Genel sağlık sigortası bunlardan ayrı düzenlenmiştir. 4/1-(b) bağımsız çalışanları, 4/1-(c) kamu görevlilerini kapsar.',
    ),
    '0036': patch(
        'Bir kişi hem bir şirkette iş sözleşmesiyle çalışmakta hem de aynı dönemde kendi adına kayıtlı bir ticari işletmeyi bağımsız olarak işletmektedir. Her iki faaliyeti de aynı anda sürdürmektedir. Buna göre 5510 sayılı Kanun uyarınca aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kişi 4/1-(b) kapsamında sigortalı sayılır; hizmet akdi sigortalılığı askıya alınır',
            'B': 'Kişi dilediği statüyü seçmekte serbesttir ve seçimini her yıl değiştirebilir',
            'C': 'Çakışma hâlinde sigortalılık tümüyle sona erer, kişi isteğe bağlı sigortalı olur',
            'D': 'Kişi 4/1-(a) kapsamında sigortalı sayılır; bağımsız çalışması nedeniyle ayrıca 4/1-(b) sigortalılığı doğmaz',
            'E': 'Kişi her iki statüde de aynı anda sigortalı sayılır ve iki statü için ayrı ayrı prim ödemekle yükümlüdür',
        },
        'D',
        '5510 md. 53: sigortalının 4/1-(a) ile 4/1-(b) kapsamına giren çalışmaları çakışırsa 4/1-(a) kapsamındaki sigortalılık geçerli sayılır. Böylece aynı dönem için iki ayrı statüde sigortalılık ve mükerrer prim doğmaz; seçim hakkı da bulunmaz.',
    ),
    '0037': patch(
        'Bir işverenin Kuruma ödenmemiş prim borcu ile kesinleşmiş idari para cezası borcu bulunmaktadır. İşveren, bu borçların genel hükümlere göre takip edilmesi gerektiğini ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kurumun süresinde ödenmeyen prim ve idari para cezası alacakları 6183 sayılı Kanun hükümlerine göre tahsil edilir',
            'B': 'Kurumun prim ve idari para cezası alacakları genel hükümlere göre ilamsız icra yoluyla takip edilir',
            'C': 'Kurum alacakları için gecikme cezası ve gecikme zammı uygulanmaz',
            'D': 'Prim alacakları için yalnızca dava yoluna başvurulabilir, cebri takip yapılamaz',
            'E': 'Kesinleşmiş idari para cezaları 6183 sayılı Kanun kapsamı dışında bırakılmış olup genel hükümlere tabidir',
        },
        'A',
        '5510 md. 88 ve 89: Kurumun süresi içinde ödenmeyen prim ve diğer alacakları ile kesinleşmiş idari para cezaları, 6183 sayılı Amme Alacaklarının Tahsil Usulü Hakkında Kanun hükümlerine göre tahsil edilir; Kurum bu Kanunun uygulanmasında alacaklı amme idaresi sayılır. Ayrıca gecikme cezası ve gecikme zammı uygulanır.',
    ),
    '0038': patch(
        'Bir sigortalı, yaşlılık aylığı koşullarının tüm sigortalılar için tek ve sabit olduğunu ileri sürmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Koşulların tamamını taşımayan sigortalıya kısmi aylık bağlanması gündeme gelebilir',
            'B': 'Koşullar, sigortalının ilk defa sigortalı sayıldığı tarihe göre kademeli biçimde belirlenir ve geçiş hükümleri farklı yaş ile prim koşulları doğurur',
            'C': 'Yaşlılık aylığı koşulları, sigortalılık statüsünden ve ilk işe giriş tarihinden bağımsız olarak herkes için aynıdır',
            'D': 'Yaşlılık aylığı için yaş, sigortalılık süresi ve prim gün sayısı birlikte aranır',
            'E': 'Prim gün sayısı koşulu sigortalılık statüsüne göre farklılaşabilir',
        },
        'C',
        '5510 md. 28 ve geçici maddeler: yaşlılık aylığı koşulları sigortalının İLK DEFA sigortalı sayıldığı tarihe ve statüsüne göre kademeli olarak belirlenmiştir; yaş, sigortalılık süresi ve prim gün sayısı birlikte aranır. Koşullar herkes için tek ve sabit DEĞİLDİR.',
    ),
    '0039': patch(
        'Sosyal Güvenlik Kurumunca sigortalılara ve hak sahiplerine sağlanan edimler belirlenmektedir. Buna göre aşağıdakilerden hangisi Kurumca sağlanan edimlerden biri değildir?',
        {
            'A': 'Genel sağlık sigortası kapsamında sağlık hizmeti sunulması',
            'B': 'İşsizlik ödeneğinin Kurum bütçesinden ödenmesi',
            'C': 'Malullük, yaşlılık ve ölüm aylığı bağlanması',
            'D': 'Geçici iş göremezlik ödeneği verilmesi',
            'E': 'Sürekli iş göremezlik geliri bağlanması',
        },
        'B',
        '5510 kapsamında Kurumca sağlanan edimler; geçici iş göremezlik ödeneği, sürekli iş göremezlik geliri, malullük, yaşlılık ve ölüm aylıkları, emzirme ve cenaze ödeneği ile genel sağlık sigortası yardımlarıdır. İŞSİZLİK ÖDENEĞİ 4447 sayılı Kanun kapsamındadır ve İşsizlik Sigortası Fonundan karşılanır; Kurum bütçesinden ödenen bir 5510 edimi değildir.',
    ),
    '0040': patch(
        "Sosyal güvenlik ve sigorta yardımları ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Geçici iş göremezlik ödeneği yatarak tedavide günlük kazancın yarısıdır. II. Sürekli iş göremezlik geliri için meslekte kazanma gücünün en az %10 azalması gerekir. III. Malul sayılmak için çalışma gücünün en az %40'ının kaybedilmesi yeterlidir. IV. İşsizlik ödeneği 5510 sayılı Kanun kapsamında Kurum bütçesinden ödenir.",
        {
            'A': 'II ve IV',
            'B': 'I, III ve IV',
            'C': 'I ve II',
            'D': 'Yalnız III',
            'E': 'III ve IV',
        },
        'E',
        "III YANLIŞ: 5510 md. 25 uyarınca malul sayılmak için çalışma gücünün ya da meslekte kazanma gücünün EN AZ %60'ının kaybedilmesi gerekir. IV YANLIŞ: işsizlik ödeneği 4447 sayılı Kanun kapsamında İşsizlik Sigortası Fonundan ödenir. I (md. 18) ve II (md. 19) doğrudur.",
    ),
    '0041': patch(
        "İşsizlik ödeneğine hak kazanan bir sigortalının son dört aylık prime esas kazançlarının günlük ortalaması 1.500 ₺'dir. Buna göre günlük işsizlik ödeneği tutarı ve üst sınırı bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Günlük ödenek son dört aylık ortalamanın yarısı olan 750 ₺'dir ve herhangi bir üst sınıra tabi değildir",
            'B': "Günlük ödenek 600 ₺'dir; ancak aylık tutarı, aylık asgari ücretin brüt tutarının yüzde seksenini geçemez",
            'C': 'Ödenek tutarı prim gün sayısına göre belirlenir; kazanç ortalaması dikkate alınmaz',
            'D': "Günlük ödenek 900 ₺'dir ve yalnızca alt sınır uygulanır",
            'E': "Günlük ödenek 1.500 ₺'dir; ödenek son kazancın tamamı üzerinden hesaplanır",
        },
        'B',
        '4447 md. 50: günlük işsizlik ödeneği, sigortalının son dört aylık prime esas kazançları dikkate alınarak hesaplanan günlük ortalama brüt kazancının YÜZDE KIRKIDIR: 1.500 × %40 = 600 ₺. Bu şekilde hesaplanan ödenek miktarı, aylık asgari ücretin brüt tutarının yüzde seksenini GEÇEMEZ.',
    ),
    '0042': patch(
        'Sosyal güvenlik primleri bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kısa vadeli sigorta kolları primi sigortalı ile işveren arasında eşit olarak paylaştırılır',
            'B': 'Bu primin yüzde dokuzu sigortalı hissesi, yüzde on biri ise işveren hissesi olarak ayrılır',
            'C': 'Prime esas günlük kazancın üst sınırı, alt sınırın yedi buçuk katıdır',
            'D': 'Primler, ait olduğu ayı takip eden ayın sonuna kadar Kuruma ödenir',
            'E': 'Malullük, yaşlılık ve ölüm sigortaları primi yüzde yirmidir',
        },
        'A',
        "5510 md. 81: kısa vadeli sigorta kolları primi tamamen İŞVERENE aittir; sigortalıdan kesinti yapılmaz. Malullük, yaşlılık ve ölüm sigortaları primi %20 olup %9'u sigortalı, %11'i işveren hissesidir. md. 82 kazanç sınırlarını, md. 88 ise ödeme süresini düzenler.",
    ),
    '0043': patch(
        'Bir işveren ile işçi, aralarında yaptıkları sözleşmeye, işçinin sosyal sigorta kapsamı dışında tutulacağına ilişkin bir hüküm koymuştur. İşçi de bu hükmü kabul etmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Hüküm geçerli olup işçi yalnızca isteğe bağlı sigortalı olabilir',
            'B': 'Hüküm ancak Kurumun onayıyla geçersiz hâle gelir',
            'C': 'Sözleşme özgürlüğü uyarınca tarafların iradesi esas olduğundan bu hüküm geçerlidir',
            'D': 'Hüküm, işçinin yazılı onayı bulunduğu için geçerli sayılır',
            'E': 'Sigortalı olmak hak ve yükümlülüğünden vazgeçilemeyeceğinden bu hüküm geçersizdir',
        },
        'E',
        '5510 md. 92: sigortalı olmak hak ve yükümlülüğünden VAZGEÇİLEMEZ. Sosyal sigortada ZORUNLULUK (mecburilik) ilkesi geçerlidir; sigortalılık, kanunda belirtilen koşullar gerçekleştiğinde kendiliğinden doğar ve taraf iradesiyle ortadan kaldırılamaz. Aksi yöndeki sözleşme hükümleri geçersizdir.',
    ),
    '0044': patch(
        'Bir işçi 15 Mayıs günü fiilen çalışmaya başlamış; işveren ise sigortalı işe giriş bildirgesini 20 Mayıs günü Kuruma vermiştir. Buna göre sigortalılığın başlangıcı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sigortalılık, bildirgenin Kuruma verildiği 20 Mayıs tarihinde başlar',
            'B': 'Sigortalılığın başlangıcı, işveren ile işçinin anlaşmasıyla belirlenir',
            'C': 'Sigortalılık, fiilen çalışmaya başlanılan 15 Mayıs tarihinde başlar',
            'D': 'Bildirge süresinde verilmediği için sigortalılık hiç doğmaz',
            'E': 'Sigortalılık, bildirgenin verildiği ayı takip eden ayın başında başlar',
        },
        'C',
        '5510 md. 7: 4/1-(a) kapsamındaki sigortalılar için sigortalılık, çalışmaya, mesleki eğitime veya staja başladıkları tarihten itibaren başlar. İşverenin bildirimi KURUCU değil BİLDİRİCİ niteliktedir; geç bildirim sigortalılığı ortadan kaldırmaz, yalnızca işverene idari para cezası uygulanmasını gerektirir (md. 102).',
    ),
    '0045': patch(
        "Sosyal güvenlik hukuku ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Sosyal sigortalılık kural olarak zorunludur. II. Kurumun süresinde ödenmeyen alacakları 6183 sayılı Kanun'a göre tahsil edilir. III. Sosyal güvenlik uyuşmazlıkları kural olarak iş mahkemelerinde görülür.",
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'C',
        "Üç ifade de doğrudur. 5510 md. 92 zorunluluk ilkesini, md. 88-89 alacakların 6183 sayılı Kanun'a göre tahsilini, md. 101 ise uyuşmazlıkların iş mahkemelerinde görüleceğini düzenler.",
    ),
    '0046': patch(
        'İş kazası ve meslek hastalığı sigortasından sağlanan haklar belirlenmektedir. Buna göre aşağıdakilerden hangisi bu sigorta kolundan sağlanan haklardan biri değildir?',
        {
            'A': 'Sigortalıya geçici iş göremezlik ödeneği verilmesi',
            'B': 'Sigortalıya yaşlılık aylığı bağlanması',
            'C': 'Sigortalıya sürekli iş göremezlik geliri bağlanması',
            'D': 'Sigortalının cenazesi için cenaze ödeneği verilmesi',
            'E': 'Hak sahiplerine gelir bağlanması ve evlenme ödeneği verilmesi',
        },
        'B',
        '5510 md. 16: iş kazası veya meslek hastalığı sigortasından sigortalıya geçici iş göremezlik ödeneği verilmesi, sürekli iş göremezlik geliri bağlanması, ölen sigortalının hak sahiplerine gelir bağlanması, evlenme ödeneği ve cenaze ödeneği verilmesi hakları sağlanır. YAŞLILIK AYLIĞI uzun vadeli sigorta kolları kapsamındadır.',
    ),
    '0047': patch(
        'Sosyal sigorta sisteminin finansmanı tartışılmaktadır. Bir görüşe göre sistem tümüyle devlet bütçesinden karşılanmakta olup prim tahsili yalnızca biçimseldir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Finansman biçimi her yıl Kurum yönetim kurulunca serbestçe belirlenir',
            'B': 'Finansman yalnızca işveren primlerinden sağlanır',
            'C': 'Sistem tümüyle sigortalı primleriyle finanse edilir; işveren ve devlet katkısı bulunmaz',
            'D': 'Sistem tümüyle devlet bütçesinden karşılanır; prim tahsili biçimseldir',
            'E': 'Sosyal sigorta ağırlıklı olarak prim esasına dayanır; devlet katkısı bu finansmanı tamamlar',
        },
        'E',
        'Sosyal sigorta, karşılığında prim ödenen bir güvence sistemidir: 5510 md. 79 ve 81 uyarınca primler sigortalı ve işveren hisselerinden oluşur; md. 81/1-(i) devlet katkısını düzenler. Primsiz rejim (sosyal yardım ve hizmetler) ise doğrudan bütçeden finanse edilir; bu ikisi ayrı ayaklardır.',
    ),
    '0048': patch(
        'Sigorta kolları ile kapsamları eşleştirilmektedir. Buna göre aşağıdaki eşleştirmelerden hangisi doğrudur?',
        {
            'A': 'Uzun vadeli sigorta kolları → iş kazası, meslek hastalığı, hastalık ve analık',
            'B': 'Uzun vadeli sigorta kolları → hastalık ve analık sigortaları',
            'C': 'Kısa vadeli sigorta kolları → iş kazası, meslek hastalığı, hastalık ve analık',
            'D': 'Kısa vadeli sigorta kolları → malullük, yaşlılık ve ölüm',
            'E': 'Genel sağlık sigortası → malullük, yaşlılık ve ölüm aylıkları',
        },
        'C',
        '5510 md. 3: kısa vadeli sigorta kolları iş kazası, meslek hastalığı, hastalık ve analık sigortalarıdır. Uzun vadeli sigorta kolları malullük, yaşlılık ve ölüm sigortalarıdır. Genel sağlık sigortası ise sağlık hizmetlerinin finansmanını sağlayan ayrı bir koldur.',
    ),
    '0049': patch(
        "Türkiye'de ikamet eden ve zorunlu sigortalı olmayan bir kişi, genel sağlık sigortası kapsamında olup olmadığını öğrenmek istemektedir. Kişinin bakmakla yükümlü olduğu bir sigortalı da bulunmamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Genel sağlık sigortası yalnızca 4/1-(a) kapsamındaki sigortalıları kapsar',
            'B': 'Genel sağlık sigortası primi her durumda devlet tarafından karşılanır',
            'C': 'Zorunlu sigortalı olmayan ve bakmakla yükümlü olunan kişi durumunda bulunmayanlar genel sağlık sigortası kapsamı dışındadır',
            'D': 'Kişi, gelir testi sonucuna göre genel sağlık sigortalısı sayılır ve primini kendisi öder',
            'E': "Genel sağlık sigortası kapsamı için Türkiye'de ikamet koşulu aranmaz",
        },
        'D',
        "5510 md. 60: Türkiye'de ikamet eden kişilerden belirtilen koşulları taşıyanlar genel sağlık sigortalısı sayılır. Zorunlu sigortalı olmayan ve bakmakla yükümlü olunan kişi durumunda da bulunmayanlar, gelir tespiti sonucuna göre genel sağlık sigortalısı olur; geliri belirlenen eşiğin altında kalanların primi devletçe karşılanır, diğerleri primini kendisi öder.",
    ),
    '0050': patch(
        "Sosyal güvenlik hukuku ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Sosyal Güvenlik Kurumu kamu tüzel kişiliğini haizdir. II. Sosyal güvenlik hakkı Anayasa'da düzenlenmiştir. III. Prime esas kazancın üst sınırı, alt sınırın yedi buçuk katıdır.",
        {
            'A': 'I, II ve III',
            'B': 'I ve III',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'I ve II',
        },
        'A',
        'Üç ifade de doğrudur. 5502 md. 1 Kurumun kamu tüzel kişiliğini, Anayasa md. 60 sosyal güvenlik hakkını, 5510 md. 82 ise prime esas günlük kazancın alt sınırının asgari ücret, üst sınırının bu tutarın 7,5 katı olduğunu düzenler.',
    ),
    '0051': patch(
        'Bir işverenin sosyal güvenlik mevzuatından doğan yükümlülükleri belirlenmektedir. Buna göre aşağıdakilerden hangisi işverenin bu yükümlülüklerinden biri değildir?',
        {
            'A': 'Sigortalı işe giriş bildirgesini süresinde Kuruma vermek',
            'B': 'İşyeri bildirgesini süresinde Kuruma vermek',
            'C': 'Sigortalının bağlanacak aylığının tutarını belirlemek',
            'D': 'İş kazasını üç iş günü içinde Kuruma bildirmek',
            'E': 'Aylık prim ve hizmet bilgilerini Kuruma bildirmek ve primleri ödemek',
        },
        'C',
        'İşverenin başlıca yükümlülükleri; işyeri bildirgesi (5510 md. 11), sigortalı işe giriş bildirgesi (md. 8), prim ve hizmet bildirimi ile prim ödeme (md. 86, 88) ve iş kazası bildirimidir (md. 13). Bağlanacak AYLIĞIN TUTARINI belirlemek Kurumun görevidir; işverenin böyle bir yetkisi ve yükümlülüğü yoktur.',
    ),
    '0052': patch(
        'Bir girişimci yeni bir işyeri açmış ve sigortalı çalıştırmaya başlamıştır. İşyeri bildirgesini Kuruma vermeyi ertelemek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ticaret sicili tescili, işyeri bildirgesi yükümlülüğünü tümüyle ortadan kaldırır',
            'B': 'İşyeri bildirgesi, işyerinin açıldığı tarihten itibaren bir ay içinde verilebilir',
            'C': 'İşyeri bildirgesi yalnızca ticaret siciline tescil edilmemiş işyerleri için aranır',
            'D': 'İşyeri bildirgesi, ilk sigortalının işe girişini takip eden ayın sonuna kadar verilebilir; işe giriş bildirgesi verilmesi bu süreyi başlatır',
            'E': 'İşyeri bildirgesi, en geç sigortalı çalıştırılmaya başlanılan tarihte Kuruma verilmelidir',
        },
        'E',
        '5510 md. 11: işveren, örneği Kurumca hazırlanacak işyeri bildirgesini en geç sigortalı çalıştırmaya BAŞLANILAN TARİHTE Kuruma vermekle yükümlüdür. Şirket kuruluşu aşamasında çalıştırılacak sigortalı sayısının ticaret sicili memurluklarına bildirilmesi hâlinde bu bildirim Kuruma yapılmış sayılır; ancak yükümlülük genel olarak ortadan kalkmaz.',
    ),
    '0053': patch(
        'Bir sigortalı, Kurumun aylık bağlanmasına ilişkin işlemine karşı dava açmak istemektedir. Sigortalı, doğrudan mahkemeye başvurabileceğini düşünmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Uyuşmazlık iş mahkemesinde görülür; dava açılmadan önce Kuruma başvuru yapılması gerekir',
            'B': 'Uyuşmazlık asliye hukuk mahkemesinde görülür',
            'C': 'Sosyal güvenlik uyuşmazlıklarında yargı yolu kapalı olup yalnızca idari itiraz mümkündür',
            'D': 'Uyuşmazlık idare mahkemesinde görülür ve ön başvuru koşulu aranmaz',
            'E': 'Sigortalı, Kuruma başvurmaksızın doğrudan iş mahkemesinde dava açabilir',
        },
        'A',
        '5510 md. 101: bu Kanunda aksine hüküm bulunmayan hâllerde, Kurumun bu Kanun hükümlerinin uygulanmasıyla ilgili ortaya çıkan uyuşmazlıklar İŞ MAHKEMELERİNDE görülür. 7036 sayılı İş Mahkemeleri Kanunu md. 4 uyarınca Kurum aleyhine dava açılabilmesi için önce Kuruma başvurulması ve talebin reddedilmesi (ya da altmış gün içinde cevap verilmemesi) gerekir; bu bir dava şartıdır.',
    ),
    '0054': patch(
        'Sosyal güvenlik sistemi ve ilkeleri ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Sosyal sigorta sistemi ağırlıklı olarak prim esasına dayanır. II. Sigortalılıktan sözleşmeyle vazgeçilebilir. III. Sosyal yardım ve hizmetler prim ödeme koşuluna bağlı değildir. IV. Kısa vadeli sigorta kolları primi sigortalıdan kesilir.',
        {
            'A': 'I ve III',
            'B': 'II ve IV',
            'C': 'Yalnız II',
            'D': 'I, II ve IV',
            'E': 'III ve IV',
        },
        'B',
        'II YANLIŞ: 5510 md. 92 uyarınca sigortalı olmak hak ve yükümlülüğünden vazgeçilemez. IV YANLIŞ: md. 81 uyarınca kısa vadeli sigorta kolları primi tamamen işverene aittir. I ve III doğrudur; sosyal yardım ve hizmetler primsiz rejimin parçasıdır.',
    ),
    '0055': patch(
        'Sosyal güvenlik uyuşmazlıkları ve yükümlülükler bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sosyal güvenlik uyuşmazlıkları kural olarak iş mahkemelerinde görülür',
            'B': 'Bildirim yükümlülüğüne aykırılık idari para cezası uygulanmasını gerektirir',
            'C': "Kurumun süresinde ödenmeyen alacakları 6183 sayılı Kanun'a göre tahsil edilir",
            'D': 'Kurum aleyhine dava açılabilmesi için önceden Kuruma başvurulması gerekmez',
            'E': 'Hizmet tespiti davası, hizmetin geçtiği yılın sonundan başlayarak beş yıl içinde açılır',
        },
        'D',
        '5510 md. 101 uyuşmazlıkların iş mahkemelerinde görüleceğini düzenler; ancak 7036 sayılı İş Mahkemeleri Kanunu md. 4 uyarınca Kurum aleyhine dava açılabilmesi için ÖNCE KURUMA BAŞVURULMASI ve talebin reddedilmesi (ya da altmış gün içinde cevap verilmemesi) gerekir; bu bir DAVA ŞARTIDIR. md. 86/9 hizmet tespiti süresini, md. 88-89 tahsili, md. 102 idari para cezalarını düzenler.',
    ),
    '0056': patch(
        "Sosyal güvenlikte 'tek çatı' anlayışı tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Birleşme, norm ve standart birliğini sağlamayı amaçlamıştır',
            'B': 'Tek çatı, tüm sigortalıların aynı statüde toplanarak 4/1-(a) kapsamına alınması anlamına gelir',
            'C': 'Tek çatı, dağınık sosyal güvenlik kuruluşlarının tek bir kurum altında birleştirilmesini ifade eder',
            'D': 'SSK, Bağ-Kur ve Emekli Sandığı Sosyal Güvenlik Kurumu çatısı altında birleştirilmiştir',
            'E': 'Sigortalılık statüleri 4/1-(a), (b) ve (c) olarak varlığını sürdürmektedir',
        },
        'B',
        "5502 sayılı Kanun'la SSK, Bağ-Kur ve Emekli Sandığı tek bir kamu tüzel kişiliği olan Sosyal Güvenlik Kurumu çatısı altında birleştirilmiş; 5510 sayılı Kanun'la norm ve standart birliği amaçlanmıştır. Ancak sigortalılık STATÜLERİ ortadan kalkmamıştır; 4/1-(a), (b) ve (c) ayrımı varlığını sürdürür.",
    ),
    '0057': patch(
        'Sosyal güvenlik ve sigortalılık ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. İsteğe bağlı sigortalılık 4/1-(b) kapsamında sayılır. II. İş kazası, 4/1-(a) sigortalıları için işverence üç iş günü içinde bildirilir. III. İşyeri bildirgesi en geç sigortalı çalıştırılmaya başlanılan tarihte verilir.',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'I ve III',
            'D': 'I, II ve III',
            'E': 'II ve III',
        },
        'D',
        'Üç ifade de doğrudur. 5510 md. 51 isteğe bağlı sigortalılığın 4/1-(b) kapsamında sayılacağını, md. 13/2-(a) iş kazasının üç iş günü içinde bildirileceğini, md. 11 ise işyeri bildirgesinin en geç sigortalı çalıştırılmaya başlanılan tarihte verileceğini düzenler.',
    ),
    '0058': patch(
        'Bir sigortalı çalıştığı işyerinde iş kazası geçirmiştir. Kaza sonrası sürecin işleyişi belirlenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kurumun sigortalıya yaptığı ödemeler, işverenin kusuru bulunsa dahi işverene rücu edilemez',
            'B': 'Meslekte kazanma gücü en az %10 oranında azalmışsa sigortalıya sürekli iş göremezlik geliri bağlanır',
            'C': 'İşveren, kazayı kazadan sonraki üç iş günü içinde Kuruma bildirmelidir',
            'D': 'Sigortalıya geçici iş göremezlik ödeneği kazanın ilk gününden itibaren ödenir',
            'E': 'Kurum, sigortalıya sağlanan sağlık hizmetlerinin bedelini karşılar',
        },
        'A',
        "5510 md. 21: iş kazası, işverenin kastı veya sigortalıların sağlığını koruma ve iş güvenliği mevzuatına aykırı hareketi sonucu meydana gelmişse, Kurumca sigortalıya veya hak sahiplerine yapılan ödemeler ile bağlanan gelirin başladığı tarihteki ilk peşin sermaye değeri toplamı İŞVERENE RÜCU EDİLİR. Diğer seçenekler md. 13, 18 ve 19'a uygundur.",
    ),
    '0059': patch(
        'Sosyal güvenlik hukukunun temel kavramları eşleştirilmektedir. Buna göre aşağıdaki eşleştirmelerden hangisi doğrudur?',
        {
            'A': 'Geçici iş göremezlik ödeneği → yatarak tedavide günlük kazancın tamamı',
            'B': 'İşsizlik ödeneği → son dört aylık günlük ortalama kazancın yüzde altmışı',
            'C': 'Sürekli iş göremezlik geliri → meslekte kazanma gücünün en az %10 azalması',
            'D': 'Ölüm aylığı → yalnızca sağ kalan eşe bağlanan aylık',
            'E': 'Malullük aylığı → çalışma gücünün en az %10 kaybedilmesi',
        },
        'C',
        "5510 md. 19: sürekli iş göremezlik geliri için meslekte kazanma gücünün EN AZ %10 azalması gerekir. md. 25: malullük için kayıp oranı en az %60'tır. md. 18: geçici iş göremezlik ödeneği yatarak tedavide günlük kazancın YARISIDIR. 4447 md. 50: işsizlik ödeneği günlük ortalama brüt kazancın %40'ıdır. md. 32-34: ölüm aylığı eş, çocuklar ile ana ve babaya bağlanabilir.",
    ),
    '0060': patch(
        "Sosyal güvenlik hukuku ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Temel kanun 5510 sayılı Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu'dur. II. Hizmet tespiti davası idare mahkemesinde görülür. III. Malullük, yaşlılık ve ölüm sigortaları primi yüzde yirmidir. IV. Sigortalılık, işverenin bildirim yaptığı tarihte başlar.",
        {
            'A': 'II ve III',
            'B': 'Yalnız II',
            'C': 'I ve III',
            'D': 'II ve IV',
            'E': 'I, II ve IV',
        },
        'D',
        'II YANLIŞ: 5510 md. 86/9 uyarınca hizmet tespiti davası İŞ MAHKEMESİNDE görülür. IV YANLIŞ: md. 7 uyarınca sigortalılık fiilen çalışmaya başlanılan tarihte başlar; bildirim bildirici niteliktedir. I ve III (md. 81) doğrudur.',
    ),
}

# 2026/1 ve 2026/2 gercek SGS hukuk bloklariyla yapilan ikinci zorluk
# kalibrasyonu. Bu yamalar, ilk yapisal turdan sonra hâlâ tek bir ezber
# bilgisini soran maddeleri; birden cok kurali ayni olayda ayirt etmeyi
# gerektiren sinav tipi maddelere cevirir. Dogru cevap harfleri korunur.
# Ayrica 7566 sayili Kanunla 01.01.2026'da yururluge giren oranlar ile 2026
# prime esas kazanc tavani guncellenmistir.
_EXAM_LEVEL_PATCHES = {
    '0002': patch(
        'Sosyal güvenlik alanındaki üç işlem şöyledir: işsizlik sigortası primlerinin tahsili, İşsizlik Sigortası Fonunun yönetimi ve 4/1-(a) sigortalısına yaşlılık aylığı bağlanması. Bu işlemlerin yetkili kurumları sırasıyla aşağıdakilerden hangisinde doğru gösterilmiştir?',
        {
            'A': 'SGK – İŞKUR – SGK',
            'B': 'İŞKUR – SGK – SGK',
            'C': 'SGK – SGK – İŞKUR',
            'D': 'İŞKUR – İŞKUR – SGK',
            'E': 'SGK – İŞKUR – İŞKUR',
        },
        'A',
        'İşsizlik sigortası primlerini 5510 sayılı Kanun uyarınca SGK tahsil eder; İşsizlik Sigortası Fonu 4447 sayılı Kanun uyarınca İŞKUR tarafından yönetilir. 4/1-(a) sigortalısına yaşlılık aylığı bağlama işlemi ise SGK tarafından yürütülür. Prim tahsil eden kurum ile fonu yöneten kurumun aynı olduğu varsayılamaz.',
        '5502 sayılı Kanun md. 3; 4447 sayılı Kanun md. 46, 53; 5510 sayılı Kanun md. 28',
    ),
    '0005': patch(
        'Bir belediyede A memur kadrosunda, B sürekli işçi kadrosunda iş sözleşmesiyle çalışmaktadır. C ise belediyeye ait bir işi kendi adına kurduğu işletme üzerinden üstlenmiş ve belediyeyle arasında hizmet akdi kurulmamıştır. Bu kişilerin sigortalılık statüleri sırasıyla aşağıdakilerden hangisidir?',
        {
            'A': '4/1-(a) – 4/1-(c) – 4/1-(b)',
            'B': '4/1-(c) – 4/1-(b) – 4/1-(a)',
            'C': '4/1-(b) – 4/1-(a) – 4/1-(c)',
            'D': '4/1-(c) – 4/1-(a) – 4/1-(c)',
            'E': '4/1-(c) – 4/1-(a) – 4/1-(b)',
        },
        'E',
        'Kamu idaresinde çalışmak tek başına 4/1-(c) statüsü doğurmaz. Memur A, 4/1-(c); iş sözleşmesiyle çalışan B, 4/1-(a); hizmet akdine bağlı olmaksızın kendi adına ve hesabına çalışan C ise 4/1-(b) kapsamındadır. Statü, işin görüldüğü kurumdan çok hukuki çalışma ilişkisine göre belirlenir.',
        '5510 sayılı Kanun md. 4/1-(a), (b), (c)',
    ),
    '0006': patch(
        '4/1-(a) kapsamındaki sigortalı iş kazası nedeniyle on gün çalışamamış, taburcu olduktan sonra ayakta tedavisi sürmüş ve meslekte kazanma gücündeki kayıp %12 olarak kesinleşmiştir. Bu olayda sağlanabilecek parasal edimler bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Koşulları varsa geçici iş göremezlik ödeneği ile sürekli iş göremezlik geliri birlikte gündeme gelebilir',
            'B': 'Yalnız malullük aylığı bağlanabilir; kısa vadeli sigorta edimi sağlanamaz',
            'C': 'Sürekli iş göremezlik geliri için çalışma gücü kaybının en az %60 olması gerekir',
            'D': 'Geçici iş göremezlik ödeneği iş kazalarında üçüncü günden önce ödenemez',
            'E': 'Meslekte kazanma gücü kaybı %10’u geçtiğinde geçici iş göremezlik ödeneği kesilerek yaşlılık aylığına dönüşür',
        },
        'A',
        'İş kazasında geçici iş göremezlik ödeneği istirahat süresince ilk günden itibaren verilebilir. Meslekte kazanma gücü kaybı en az %10 ise sürekli iş göremezlik geliri de gündeme gelir. %60 eşiği malullük sigortasına ilişkindir; sürekli iş göremezlik gelirinin eşiği değildir.',
        '5510 sayılı Kanun md. 18, 19, 25',
    ),
    '0007': patch(
        'Kurum sağlık kurulu A’nın çalışma gücü kaybını %58, B’nin iş kazası sonucu meslekte kazanma gücü kaybını %12 olarak belirlemiştir. C ise yaşlılık aylığı almakta iken vefat etmiş ve hak sahiplerini geride bırakmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'A malul sayılır; B’ye sürekli iş göremezlik geliri bağlanamaz; C’nin aylığı sona erdiği için hak sahiplerine edim sağlanamaz',
            'B': 'A ve B yalnız kısa vadeli sigorta kollarından yararlanabilir; C bakımından genel sağlık sigortası uygulanır',
            'C': 'A’ya malullük aylığı, B’ye yaşlılık aylığı, C’nin hak sahiplerine geçici iş göremezlik ödeneği bağlanır',
            'D': 'A salt %58 kayıp nedeniyle malul sayılmaz; B için sürekli iş göremezlik geliri, C’nin hak sahipleri için ölüm sigortası hükümleri gündeme gelebilir',
            'E': 'A ile B için aynı %60 kayıp eşiği uygulanır; C’nin hak sahipleri yalnız prim iadesi isteyebilir',
        },
        'D',
        'Malullükte kural olarak en az %60 çalışma gücü veya meslekte kazanma gücü kaybı aranır. İş kazasına bağlı sürekli iş göremezlik gelirinde eşik %10’dur. Yaşlılık aylığı alan sigortalının ölümü hâlinde koşulları taşıyan hak sahipleri yönünden ölüm sigortası edimleri değerlendirilir.',
        '5510 sayılı Kanun md. 19, 25, 32-34',
    ),
    '0012': patch(
        'Türkiye’de ikamet eden A zorunlu sigortalıdır. A’nın çalışmayan eşi B, bakmakla yükümlü olunan kişi durumundadır. Zorunlu sigortalılığı ve başka bir sigortalı üzerinden sağlık güvencesi bulunmayan C’nin ise gelir testi sonucu aile içindeki kişi başına düşen geliri kanuni eşiğin altında kalmıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'A, zorunlu sigortalılığı nedeniyle genel sağlık sigortalısıdır',
            'B': 'B’nin sağlık hizmetlerinden yararlanabilmesi için ayrıca zorunlu sigortalı olarak tescil edilmesi gerekir',
            'C': 'B, koşulları taşıdığı sürece A üzerinden bakmakla yükümlü olunan kişi olarak sağlık hizmetlerinden yararlanabilir',
            'D': 'C’nin genel sağlık sigortası primi, gelir testinin sonucu nedeniyle devlet tarafından karşılanabilir',
            'E': 'Genel sağlık sigortası, kısa ve uzun vadeli sigorta kollarından ayrı bir sigorta koludur',
        },
        'B',
        'Bakmakla yükümlü olunan kişi, ayrıca zorunlu sigortalı tescili yapılmaksızın genel sağlık sigortalısı üzerinden sağlık hizmetlerinden yararlanabilir. Gelir testi sonucu kanuni eşiğin altında kalanların genel sağlık sigortası primi devletçe karşılanır.',
        '5510 sayılı Kanun md. 3/10, 60, 61',
    ),
    '0017': patch(
        'Bir işveren 10 Nisan günü imalat işyerinde A’yı, aynı gün başladığı tarım işyerinde ise B’yi ilk kez çalıştıracaktır. Sigortalı işe giriş bildirgelerinin son verilme zamanı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'A ve B için 10 Nisan gün sonuna kadar bildirim yeterlidir',
            'B': 'A ve B için işe başladıktan sonraki üç iş günü içinde bildirim yapılabilir',
            'C': 'A için 10 Nisandan önce, B için en geç 10 Nisan günü bildirim yapılmalıdır',
            'D': 'A için ay sonuna, B için takip eden ayın sonuna kadar süre vardır',
            'E': 'A için en geç 10 Nisan günü, B için 10 Nisandan önce bildirim yapılmalıdır',
        },
        'C',
        '4/1-(a) sigortalısı kural olarak çalışmaya başlamadan önce bildirilir. İnşaat, balıkçılık ve tarım işyerlerinde işe başlatılacak kişiler için bildirgenin en geç çalışmaya başlanılan gün verilmesi istisnadır. İmalat işyerindeki A genel kurala, tarım işyerindeki B istisnaya tabidir.',
        '5510 sayılı Kanun md. 8',
    ),
    '0018': patch(
        '2026 yılında 4/1-(a) kapsamındaki bir sigortalının prime esas kazancı üzerinden malullük, yaşlılık ve ölüm sigortaları primi ile kısa vadeli sigorta kolları primi hesaplanacaktır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Malullük, yaşlılık ve ölüm sigortaları primi %20’dir; sigortalı ve işveren arasında eşit paylaşılır',
            'B': 'Malullük, yaşlılık ve ölüm sigortaları primi %21’dir; %9’u sigortalı, %12’si işveren payıdır',
            'C': 'Malullük, yaşlılık ve ölüm sigortaları priminin tamamı sigortalıdan, kısa vadeli sigorta primi işverenden alınır',
            'D': 'Malullük, yaşlılık ve ölüm sigortaları primi %21’dir; tamamı işveren tarafından karşılanır',
            'E': 'Malullük, yaşlılık ve ölüm sigortaları primi sözleşmeyle belirlenebilir; kısa vadeli sigorta primi eşit paylaşılır',
        },
        'B',
        '1 Ocak 2026’dan itibaren malullük, yaşlılık ve ölüm sigortaları prim oranı %21’dir; bunun %9’u sigortalı, %12’si işveren payıdır. Kısa vadeli sigorta kolları primi ise tamamen işverene aittir. Kanuni prim oranları sözleşmeyle değiştirilemez.',
        '5510 sayılı Kanun md. 81; 7566 sayılı Kanun md. 23 ve 27 (01.01.2026)',
    ),
    '0019': patch(
        'Bir 4/1-(a) sigortalısına aynı ay içinde ücret, nakit ikramiye, ayni yemek yardımı ve ölüm yardımı ödenmiştir. Hesaplanan aylık kazanç 2026 yılı prime esas kazanç üst sınırını da aşmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yalnız çıplak ücret prime esas kazanca alınır; üst sınır uygulanmaz',
            'B': 'Ücret, ikramiye, ayni yemek ve ölüm yardımının tamamı sınırsız biçimde prime tabi tutulur',
            'C': 'Ölüm yardımı prime tabi, nakit ikramiye ise prime tabi değildir',
            'D': 'Prime esas kazanç yalnız işverenin bordroda prim adıyla gösterdiği ödemelerden oluşur',
            'E': 'Ücret ve nakit ikramiye prime tabi; ayni yardım ile ölüm yardımı kapsam dışıdır ve prime tabi toplam 2026 üst sınırını aşamaz',
        },
        'E',
        'Ücret ile prim, ikramiye ve benzeri nakit ödemeler prime esas kazanca dâhildir. Ayni yardımlar ile ölüm, doğum ve evlenme yardımları kapsam dışındadır. 2026 yılında prime esas günlük kazanç üst sınırı, günlük alt sınırın dokuz katıdır; kapsama giren ödemelerin bunun üzerindeki kısmı o ay için prime tabi tutulmaz.',
        '5510 sayılı Kanun md. 80, 82; 7566 sayılı Kanun md. 24 (2026 üst sınırı)',
    ),
    '0021': patch(
        'Türkiye’de ikamet eden A ayda yirmi gün 4/1-(a) kapsamında çalışmakta, kalan günlerini isteğe bağlı sigortayla tamamlamak istemektedir. B ise zorunlu sigortalı çalışması bulunmadan isteğe bağlı sigortaya başvurmuştur. Bu kişiler bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'A ve B’nin isteğe bağlı süreleri 4/1-(a) kapsamında sayılır ve primleri işverence ödenir',
            'B': 'Ay içinde zorunlu sigortalı çalışması bulunan A hiçbir durumda isteğe bağlı prim ödeyemez',
            'C': 'İsteğe bağlı sigorta yalnız kısa vadeli sigorta kollarını kapsar',
            'D': 'B’nin daha önce zorunlu sigortalı olmaması isteğe bağlı sigortaya engeldir',
            'E': 'Koşulları varsa A eksik günlerini tamamlayabilir; isteğe bağlı ödenen süreler kural olarak 4/1-(b) kapsamında sayılır ve primi ilgilisi öder',
        },
        'E',
        'Ay içinde otuz günden az çalışan veya tam gün çalışmayan kişi, diğer koşulları da taşıyorsa eksik günleri için isteğe bağlı sigortaya başvurabilir. İsteğe bağlı sigorta süreleri kural olarak 4/1-(b) kapsamında kabul edilir ve prim sigortalının kendisi tarafından ödenir.',
        '5510 sayılı Kanun md. 50, 51, 52',
    ),
    '0023': patch(
        'İşveren, mart ayına ait sigorta primlerini kanuni süresinden iki ay sonra ödemiştir. Gecikmeden önce Kuruma verdiği bildirgede prime esas kazancı da eksik gösterdiği sonradan saptanmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Süresinde ödenmeyen prim için gecikme cezası ve gecikme zammı uygulanabilir; eksik bildirim ayrıca idari yaptırım doğurabilir',
            'B': 'Bildirge zamanında verildiğinden primin geç ödenmesi hiçbir mali sonuç doğurmaz',
            'C': 'Prim borcuna yalnız sözleşmesel faiz uygulanabilir; Kurumun kamu alacağı takip yetkisi yoktur',
            'D': 'Eksik kazanç bildirimi yalnız sigortalının şikâyeti varsa yaptırıma bağlanabilir',
            'E': 'Prim geç ödense bile işverenin bildirim ve ödeme yükümlülükleri sigortalıya geçer',
        },
        'A',
        'Primleri süresinde ödememe ile prime esas kazancı eksik bildirme farklı yükümlülük ihlalleridir. Süresinde ödenmeyen primlere gecikme cezası ve gecikme zammı uygulanır; eksik bildirim ise prim farkının yanında idari para cezası ve diğer kanuni sonuçları doğurabilir.',
        '5510 sayılı Kanun md. 86, 88, 89, 102; 6183 sayılı Kanun',
    ),
    '0026': patch(
        'Kanun koyucu, sosyal güvenlik hakkının kapsamını düzenleyen bir değişiklik yaparken bir grup bakımından hakkın özüne dokunan ölçüsüz bir sınırlama getirmiştir. İdare ise bu sınırlamanın sosyal güvenliğin yalnız kanuni bir yardım olmasından dolayı anayasal denetime elverişli olmadığını savunmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sosyal güvenlik Anayasa’da güvence altına alınmış bir hak olduğundan kanuni düzenlemeler anayasal ilke ve sınırlara uygun olmalıdır',
            'B': 'Sosyal güvenlik yalnız prim ödeyenlere tanınan sözleşmesel bir haktır',
            'C': 'Anayasa sosyal güvenlik konusunda devlete herhangi bir görev yüklememiştir',
            'D': 'Sosyal güvenlik hakkı yalnız kamu görevlileri bakımından anayasal güvence altındadır',
            'E': 'Kanunda yer alan her sınırlama, hakkın özüne dokunsa bile kendiliğinden Anayasa’ya uygundur',
        },
        'A',
        'Anayasa md. 60 herkesin sosyal güvenlik hakkına sahip olduğunu, devletin bu güvenliği sağlayacak gerekli tedbirleri alıp teşkilatı kuracağını düzenler. Hakkın kanunla somutlaştırılması, kanun koyucuyu anayasal güvencelerden ve ölçülülük denetiminden bağımsız kılmaz.',
        'Türkiye Cumhuriyeti Anayasası md. 13, 60',
    ),
    '0027': patch(
        'Aynı işyerinde A iş kazası geçirmiş, B doğum nedeniyle analık hâline girmiş, C’nin çalışma gücündeki kayıp nedeniyle malullük koşulları araştırılmış, D’nin ise meslekte kazanma gücü kaybı %15 olarak belirlenmiştir. Aşağıdakilerden hangisinde olay ve uygulanacak sigorta kolu yanlış eşleştirilmiştir?',
        {
            'A': 'A – iş kazası sigortası',
            'B': 'B – analık sigortası',
            'C': 'C – malullük sigortası',
            'D': 'D – iş kazası veya meslek hastalığına bağlı sürekli iş göremezlik hükümleri',
            'E': 'C – kısa vadeli sigorta kolu',
        },
        'E',
        'İş kazası ve analık kısa vadeli; malullük ise uzun vadeli sigorta koludur. Meslekte kazanma gücü kaybına bağlı sürekli iş göremezlik geliri iş kazası ve meslek hastalığı sigortasından sağlanır. Bu nedenle C’nin malullük incelemesini kısa vadeli kol sayan eşleştirme yanlıştır.',
        '5510 sayılı Kanun md. 3, 19, 25',
    ),
    '0029': patch(
        'Bir işçi fiilen çalışmaya başladığı hâlde işe giriş bildirgesi verilmemiş ve taraflar “sigorta istemiyorum” içerikli belge imzalamıştır. İşçi işten ayrıldıktan sonra Kurum kayıtlarında görünmeyen çalışmalarının tespitini istemektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sigortalılık, kanuni koşullar gerçekleştiğinde işverenin bildiriminden bağımsız doğar',
            'B': 'İşe giriş bildirgesinin verilmemesi işveren bakımından idari yaptırım doğurabilir',
            'C': 'İşçinin yazılı feragati, bildirilmeyen çalışma süresinin sigortalı hizmet sayılmasını kesin olarak engeller',
            'D': 'Koşulları varsa işçi hizmet tespiti davasına başvurabilir',
            'E': 'Hizmet tespiti davasında kanundaki hak düşürücü süre ayrıca değerlendirilir',
        },
        'C',
        'Sigortalı olmak hak ve yükümlülüğünden vazgeçilemez; bu yöndeki belge geçersizdir. Bildirim sigortalılığın kurucu unsuru değildir. Kuruma bildirilmeyen çalışmalar kanundaki koşullar ve süre içinde hizmet tespiti davasına konu olabilir.',
        '5510 sayılı Kanun md. 7, 8, 86/9, 92, 102',
    ),
    '0032': patch(
        'Sosyal Güvenlik Kurumunun bir prim alacağı işlemi ile özel hukuk sözleşmesinden doğan kira uyuşmazlığı birlikte değerlendirilmektedir. Kurumun hukuki niteliği ve uygulanacak hukuk bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kurum özel hukuk tüzel kişisidir; bütün işlemlerine yalnız Borçlar Kanunu uygulanır',
            'B': 'Kurum kamu tüzel kişiliğine sahip, idari ve mali bakımdan özerktir; özel hukuk ilişkilerinde ilgili özel hukuk hükümleri uygulanabilir',
            'C': 'Kurum bakanlığın tüzel kişiliği bulunmayan hiyerarşik bir dairesidir',
            'D': 'Kurumun özerkliği nedeniyle hiçbir işlemi yargısal denetime tabi değildir',
            'E': 'Kurum kamu tüzel kişisi olduğundan taraf olduğu bütün uyuşmazlıklar idari yargıda görülür',
        },
        'B',
        'SGK kamu tüzel kişiliğini haiz, idari ve mali açıdan özerk bir kurumdur. Bu nitelik, Kurumun özel hukuk sözleşmesi yapmasına veya ilgili ilişkide özel hukuk kurallarının uygulanmasına engel değildir; ayrıca Kurumun taraf olması tek başına bütün uyuşmazlıkları idari yargıya taşımaz.',
        '5502 sayılı Kanun md. 1; 5510 sayılı Kanun md. 101',
    ),
    '0039': patch(
        'A iş kazası nedeniyle geçici iş göremezlik ödeneği, B yaşlılık aylığı, C ise hizmet akdinin kendi istek ve kusuru dışında sona ermesi üzerine işsizlik ödeneği talep etmektedir. Bu üç talebin karşılanacağı sistem ve kurumlar bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Üç talep de SGK tarafından 5510 sayılı Kanuna göre karşılanır',
            'B': 'A ve B’nin talepleri SGK; C’nin talebi 4447 sayılı Kanun kapsamında İşsizlik Sigortası Fonu ile ilgilidir',
            'C': 'Yalnız B’nin talebi SGK ile ilgilidir; A ve C belediyelerin sosyal yardım bütçesinden karşılanır',
            'D': 'A’nın talebi İŞKUR, B ve C’nin talepleri SGK tarafından karşılanır',
            'E': 'Üç talep de primsiz sosyal yardım niteliğindedir',
        },
        'B',
        'Geçici iş göremezlik ödeneği ile yaşlılık aylığı 5510 sayılı Kanun kapsamında SGK tarafından sağlanan sigorta edimleridir. İşsizlik ödeneği ise 4447 sayılı Kanun kapsamında İşsizlik Sigortası Fonundan karşılanır ve İŞKUR tarafından yürütülür.',
        '5510 sayılı Kanun md. 18, 28; 4447 sayılı Kanun md. 46, 50, 53',
    ),
    '0042': patch(
        '2026 yılında 4/1-(a) kapsamındaki sigortalılar için uygulanacak prim ve prime esas kazanç kuralları bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kısa vadeli sigorta kolları primi sigortalı ile işveren arasında eşit paylaştırılır',
            'B': 'Malullük, yaşlılık ve ölüm sigortaları priminin %9’u sigortalı, %12’si işveren payıdır',
            'C': 'Prime esas günlük kazancın üst sınırı, günlük alt sınırın dokuz katıdır',
            'D': 'Primler kural olarak ait olduğu ayı takip eden ayın sonuna kadar Kuruma ödenir',
            'E': 'Malullük, yaşlılık ve ölüm sigortaları toplam prim oranı %21’dir',
        },
        'A',
        'Kısa vadeli sigorta kolları primi tamamen işverene aittir; eşit paylaşılmaz. 1 Ocak 2026’dan itibaren malullük, yaşlılık ve ölüm sigortaları toplam primi %21 (%9 sigortalı, %12 işveren) ve prime esas kazanç üst sınırı alt sınırın dokuz katıdır.',
        '5510 sayılı Kanun md. 81, 82, 88; 7566 sayılı Kanun md. 23, 24 ve 27 (01.01.2026)',
    ),
    '0043': patch(
        'A, işverenle yaptığı yazılı sözleşmede sigortalılıktan vazgeçmiş; fiilen altı yıl çalıştıktan sonra işten ayrılmıştır. Çalışmaları Kuruma hiç bildirilmemiştir. A, işten ayrıldığı yılı izleyen üçüncü yılda hizmet tespiti istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yazılı feragat nedeniyle A’nın sigortalılığı hiç doğmamıştır',
            'B': 'Feragat ancak Kurumca iptal edilirse geçersiz hâle gelir',
            'C': 'Bildirge verilmediği için hizmet tespiti istenemez',
            'D': 'Sözleşme özgürlüğü gereği feragat geçerlidir; yalnız ödenen ücretler istenebilir',
            'E': 'Feragat geçersizdir; A, kanuni süre içinde olduğundan koşulları varsa hizmet tespiti isteyebilir',
        },
        'E',
        'Sigortalı olmak hak ve yükümlülüğünden vazgeçilemez. Fiilî çalışma ile sigortalılık doğar; bildirim kurucu değildir. Kuruma bildirilmeyen hizmetler, hizmetin geçtiği yılın sonundan başlayarak beş yıllık hak düşürücü süre içinde dava konusu edilebilir. Olayda üçüncü yılda başvuru süre yönünden mümkündür.',
        '5510 sayılı Kanun md. 7, 86/9, 92',
    ),
    '0049': patch(
        'Zorunlu sigortalılığı sona eren ve başka bir sigortalının bakmakla yükümlü olduğu kişi sayılmayan A, Türkiye’de ikamet etmeye devam etmektedir. Gelir testi sonucunda aile içindeki kişi başına düşen geliri kanuni eşiğin üzerinde belirlenmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'A, yalnız 4/1-(a) kapsamında işe girerse genel sağlık sigortalısı olabilir',
            'B': 'Geliri eşik üstünde olduğundan A’nın genel sağlık sigortası primi her durumda devletçe ödenir',
            'C': 'Zorunlu sigortalılığı bittiği anda A sürekli olarak genel sağlık sigortası kapsamı dışında kalır',
            'D': 'A genel sağlık sigortalısı olarak tescil edilir ve gelir testi sonucu nedeniyle primini kendisi öder',
            'E': 'Türkiye’de ikamet etmek genel sağlık sigortası bakımından hiçbir önem taşımaz',
        },
        'D',
        'Zorunlu sigortalı veya bakmakla yükümlü olunan kişi olmayan Türkiye’de ikamet eden kişi, 5510 md. 60 kapsamındaki koşullarla genel sağlık sigortalısı olur. Geliri kanuni eşiğin altında kalanların primi devletçe karşılanırken eşik üzerindeki kişi primini kendisi öder.',
        '5510 sayılı Kanun md. 60, 61, 80',
    ),
    '0050': patch(
        '2026 yılı sosyal güvenlik mevzuatı bakımından aşağıdaki ifadelerden hangileri doğrudur? I. Sosyal Güvenlik Kurumu kamu tüzel kişiliğine sahiptir. II. Sosyal güvenlik hakkı Anayasa’da güvence altındadır. III. Prime esas günlük kazanç üst sınırı, günlük alt sınırın dokuz katıdır.',
        {
            'A': 'I, II ve III',
            'B': 'I ve III',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'I ve II',
        },
        'A',
        'Üç ifade de doğrudur. SGK kamu tüzel kişiliğine sahip, idari ve mali açıdan özerk bir kurumdur. Sosyal güvenlik hakkı Anayasa md. 60’ta düzenlenir. 2026 yılında prime esas günlük kazanç üst sınırı günlük alt sınırın dokuz katıdır.',
        '5502 sayılı Kanun md. 1; Türkiye Cumhuriyeti Anayasası md. 60; 5510 sayılı Kanun md. 82 ve 7566 sayılı Kanun md. 24',
    ),
    '0052': patch(
        'X Anonim Şirketi ticaret siciline tescil edilirken çalıştıracağı sigortalı sayısını da ticaret sicili müdürlüğüne bildirmiştir. Aynı gün sigortalı çalıştırmaya başlayan şirketten ayrıca genel usulde işyeri bildirgesi vermesi istenmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ticaret siciline yapılan hiçbir bildirim SGK bakımından sonuç doğurmaz',
            'B': 'Şirket işyeri bildirgesini ilk prim ödemesinden sonra verebilir',
            'C': 'İşyeri bildirgesi yalnız gerçek kişi işverenler için zorunludur',
            'D': 'Şirket, sigortalı sayısını bildirmiş olsa bile bir ay içinde aynı bildirgeyi tekrar vermek zorundadır',
            'E': 'Kuruluş aşamasındaki bu bildirim Kuruma yapılmış sayılır; bilgileri Kuruma aktarma yükümlülüğü ticaret sicili müdürlüğüne aittir',
        },
        'E',
        'Genel kural, işyeri bildirgesinin en geç sigortalı çalıştırılmaya başlanılan tarihte verilmesidir. Şirket kuruluşunda çalıştırılacak sigortalı sayısı ticaret sicili müdürlüğüne bildirilmişse bu bildirim Kuruma yapılmış sayılır ve aktarım ilgili müdürlükçe gerçekleştirilir.',
        '5510 sayılı Kanun md. 11',
    ),
    '0059': patch(
        'A’nın iş kazası sonucu meslekte kazanma gücü kaybı %9, B’nin %14; C’nin hastalık nedeniyle çalışma gücü kaybı ise %59 olarak belirlenmiştir. Yalnız bu oranlar esas alındığında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'A sürekli iş göremez, B malul, C ise sürekli iş göremez sayılır',
            'B': 'A ve B sürekli iş göremezlik geliri alamaz; C malul sayılır',
            'C': 'B için sürekli iş göremezlik geliri gündeme gelebilir; A %10, C ise %60 eşiğini karşılamaz',
            'D': 'A için sürekli iş göremezlik geliri, C için malullük aylığı koşulu oran yönünden gerçekleşmiştir',
            'E': 'Üç kişi için de aynı %60 kayıp eşiği uygulanır',
        },
        'C',
        'Sürekli iş göremezlik geliri için meslekte kazanma gücü kaybının en az %10, malul sayılmak için çalışma gücü veya meslekte kazanma gücü kaybının kural olarak en az %60 olması gerekir. Bu nedenle B %14 ile ilk eşiği karşılar; A %9 ve C %59 ilgili eşiklerin altında kalır.',
        '5510 sayılı Kanun md. 19, 25',
    ),
    '0060': patch(
        '2026 yılı sosyal güvenlik hukuku bakımından aşağıdaki ifadelerden hangileri yanlıştır? I. Sosyal sigorta ve genel sağlık sigortasının temel kanunu 5510 sayılı Kanun’dur. II. Kuruma bildirilmeyen çalışmaya ilişkin hizmet tespiti davası idare mahkemesinde görülür. III. Malullük, yaşlılık ve ölüm sigortaları toplam prim oranı %21’dir. IV. 4/1-(a) sigortalılığı, işverenin bildirgeyi Kuruma verdiği tarihte başlar.',
        {
            'A': 'II ve III',
            'B': 'Yalnız II',
            'C': 'I ve III',
            'D': 'II ve IV',
            'E': 'I, II ve IV',
        },
        'D',
        'II yanlıştır: hizmet tespiti davası görevli iş mahkemesinde görülür. IV yanlıştır: 4/1-(a) sigortalılığı fiilen çalışmaya başlanan tarihte doğar; bildirim kurucu değil bildiricidir. I doğrudur. III de 1 Ocak 2026’dan itibaren geçerli %21 oran nedeniyle doğrudur.',
        '5510 sayılı Kanun md. 7, 81, 86/9, 101; 7566 sayılı Kanun md. 23 ve 27',
    ),
}

_PATCHES.update(_EXAM_LEVEL_PATCHES)

# Şık boyu, doğru cevabı ele veren ikinci bir sınava dönüşmemeli. Aşağıdaki
# metinler dolgu değildir; kısa kalan çeldiricilere eksik/yanlış hukuki önermenin
# hangi noktada ayrıldığını ekleyerek beş şıkkı aynı ayrıntı düzeyine getirir.
_OPTION_CALIBRATION = {
    '0001': {'A': "Sigortalılık statüsü ile işsizlik ödeneğinin koşulları ve finansmanı bütünüyle 5510 sayılı Kanun'a göre belirlenir"},
    '0007': {'A': 'A %58 kayıp nedeniyle malul sayılır; B için %60 eşiği aşılmadığından sürekli iş göremezlik geliri doğmaz ve C’nin hak sahiplerine yalnız toptan ödeme yapılır'},
    '0010': {'E': 'Meslek hastalığı, sigortalının yürüttüğü işten ya da işin yürütülme şartlarından doğan geçici veya sürekli hastalık, bedensel veya ruhsal engellilik hâlidir'},
    '0019': {'B': 'Ücret, nakit ikramiye, ayni yemek ve ölüm yardımının tamamı prime esas kazanca alınır; bu ödemeler için 2026 prime esas kazanç üst sınırı da uygulanmaz'},
    '0021': {'B': 'Ay içinde bir gün dahi zorunlu sigortalı çalışması bulunan A eksik günleri için isteğe bağlı prim ödeyemez; B’nin isteğe bağlı süreleri ise 4/1-(a) kapsamında sayılır'},
    '0023': {'C': 'Prim borcu özel hukuk borcu olduğundan yalnız sözleşmesel temerrüt faizi işletilebilir; Kurum gecikme cezası, gecikme zammı veya idari para cezası uygulayamaz'},
    '0026': {'E': 'Sosyal güvenlik hakkının kapsamı kanunla belirlendiğinden, kanun koyucunun hakkın özünü ortadan kaldıran veya kişiler arasında ölçüsüz ayrım yapan düzenlemeleri anayasal denetime tabi değildir'},
    '0029': {'A': 'Sigortalılık fiilî çalışmayla ve kanuni koşulların gerçekleşmesiyle doğar; işe giriş bildirgesinin hiç verilmemesi sigortalılık başlangıcını ileri bir tarihe taşımaz'},
    '0031': {'E': 'Analık sigortasından geçici iş göremezlik ödeneği verilmesinde doğumdan önceki sigortalılık süresi dikkate alınır, ancak kısa vadeli sigorta primi gün sayısı koşulu aranmaz'},
    '0032': {'E': 'Kurum kamu tüzel kişisi olduğundan prim, aylık, hizmet tespiti ve özel hukuk sözleşmelerinden doğan uyuşmazlıkların tamamı, ilişkinin niteliğine bakılmadan idari yargıda görülür'},
    '0036': {'E': 'Kişi hizmet akdine bağlı faaliyeti için 4/1-(a), bağımsız ticari faaliyeti için 4/1-(b) kapsamında aynı anda sigortalı sayılır ve iki statünün primini ayrı ayrı öder'},
    '0037': {'E': 'Kesinleşmiş idari para cezaları ile sigorta primi alacakları 6183 sayılı Kanun kapsamı dışında kalır; her ikisi de genel hükümlere göre ilamsız icra takibine konu edilir'},
    '0039': {'C': 'Yalnız B’nin yaşlılık aylığı talebi SGK tarafından karşılanır; A’nın geçici iş göremezlik ve C’nin işsizlik ödeneği talepleri belediyelerin primsiz sosyal yardım bütçesinden ödenir'},
    '0041': {'A': "Günlük ödenek son dört aylık ortalamanın yarısı olan 750 ₺'dir; aylık tutar bakımından brüt asgari ücretin iki katı dışında başka bir üst sınır uygulanmaz"},
    '0043': {'D': 'A’nın feragati sözleşme özgürlüğü gereği geçerlidir; altı yıllık çalışmanın Kuruma bildirilmemiş olması nedeniyle hizmet tespiti değil, yalnız ödenmeyen ücret ve tazminatlar istenebilir'},
    '0047': {'C': 'Sistem yalnız sigortalı primleriyle finanse edilir; işveren payı adına yapılan kesintiler sigortalının brüt ücretinin parçası, devlet katkısı ise primsiz yardım niteliğindedir'},
    '0048': {'B': 'Uzun vadeli sigorta kolları → hastalık ve analık sigortaları ile bunlara bağlı geçici ve sürekli iş göremezlik ödenekleri'},
    '0049': {'C': 'Zorunlu sigortalılığı sona eren A, bakmakla yükümlü olunan kişi de değilse gelir testi sonucuna bakılmaksızın sürekli olarak genel sağlık sigortası kapsamı dışında kalır'},
    '0052': {'D': 'Şirket, kuruluş sırasında sigortalı sayısını ticaret sicili müdürlüğüne bildirmiş olsa bile aynı bilgileri bir ay içinde yeniden işyeri bildirgesiyle Kuruma iletir; sicil bildirimi yalnız istatistik amacı taşır'},
    '0053': {'C': 'Sosyal güvenlik uyuşmazlıklarında iş veya idare mahkemesine başvuru yolu kapalıdır; Kurum içindeki itiraz süreci tüketildikten sonra işlem kesinleşir ve başka denetim yapılamaz'},
}
for _qid, _options in _OPTION_CALIBRATION.items():
    _PATCHES[_qid]['options'].update(_options)

# §2 hukuk bilişsel zorluk matrisi. Bu sınıflandırma kök uzunluğuna göre değil,
# doğru sonuca ulaşmak için birlikte işletilen hukuk kurallarına göre elle yapıldı.
# Paket üç ardışık 20 soruluk test olarak sunulduğundan her blok ayrıca denetlenir.
DIFFICULTY_LEVELS = {
    0: set(),
    1: {'0001', '0009', '0026', '0056'},
    3: {
        '0005', '0006', '0007', '0008', '0012', '0013', '0016', '0017', '0019',
        '0021', '0022', '0023', '0024', '0028', '0029', '0031', '0033', '0036',
        '0039', '0043', '0049', '0052', '0053', '0058', '0059', '0060',
    },
}
_all_ids = set(_PATCHES)
DIFFICULTY_LEVELS[2] = _all_ids - set().union(*DIFFICULTY_LEVELS.values())
assert set().union(*DIFFICULTY_LEVELS.values()) == _all_ids
assert sum(len(DIFFICULTY_LEVELS[level]) for level in (0, 1)) <= 24
assert len(DIFFICULTY_LEVELS[0]) <= 6
for _start in (1, 21, 41):
    _block = {f'{number:04d}' for number in range(_start, _start + 20)}
    assert len(_block & DIFFICULTY_LEVELS[2]) >= 8
    assert len(_block & DIFFICULTY_LEVELS[3]) >= 4

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
    print(f"1 paket / {len(PATCHES)} soru (Sosyal Guvenlik Hukuku yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
