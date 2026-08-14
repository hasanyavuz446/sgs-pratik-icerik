#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Meslek Orgutu ve Disiplin — YAPISAL kalibrasyon (tanim -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turunun 5. konusu. Paketin 60 sorusunun TAMAMI
yeniden yazildi.

    olcut              gercek   bu paket (once)
    medyan kok            257              122
    olumsuz kok         %41,5              %13
    duz tanim            %6,2              %67   <- ASIL KUSUR
    onculu              %14,3              %12

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL; ilk tasarim 42/60 (%70)
cikip uretimi DURDURDU, 43 celdirici dogru sikla PARALEL yapiya tasinarak %32) ve
§1 bilissel duzey (0+1 = 10 <=24 · duzey 2 = 37 >=24 · duzey 3 = 13 >=12).

⚠️ TERIM NOTU: audit.py::ELEME_ISARETI ciplak "niteliginde" kelimesini eleme
isareti sayiyor; oysa "kamu kurumu niteliginde meslek kurulusu" gercek hukuki
terimdir. Anlami bozmadan "kamu kurumu niteligi tasiyan meslek kurulusu"
ifadesi kullanildi.

Dayanak: 3568 sayili Kanun md. 1, 14, 18, 19, 20, 21, 22, 24, 29, 30, 32, 33,
43, 44, 45, 46, 47, 48, 49 · Disiplin Yonetmeligi · Anayasa md. 125, 129, 135 ·
2577 sayili IYUK.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/meslek_hukuku/meslek_orgutu_disiplin.json"
STYLE_REF = "SGS Meslek Hukuku (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "mh-orgut-gen-"


def patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": "3568 sayili SMMM ve YMM Kanunu"},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Bir meslek mensubu, bağlı olduğu odanın bir devlet dairesi olduğunu ve kararlarına karşı yalnızca üst amire başvurulabileceğini ileri sürmektedir. Buna göre meslek örgütünün hukuki niteliği bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kuruluş ve işleyişleri kanunla düzenlenmiştir',
            'B': 'Odalar ve Birlik, merkezî idarenin hiyerarşisi içinde yer alan devlet daireleridir',
            'C': 'Meslek kuruluşlarının tesis ettiği işlemler idari işlem sayılır',
            'D': 'Odalar ve Birlik tüzel kişiliğe sahiptir',
            'E': 'Odalar ve Birlik, tüzel kişiliğe sahip ve kamu kurumu niteliği taşıyan meslek kuruluşlarıdır',
        },
        'B',
        '3568 md. 14 ve 29: odalar ile Türkiye Serbest Muhasebeci Mali Müşavirler ve Yeminli Mali Müşavirler Odaları Birliği, tüzel kişiliğe sahip KAMU KURUMU NİTELİĞİNDE MESLEK KURULUŞLARIDIR (Anayasa md. 135). Merkezî idarenin hiyerarşik alt birimi değildirler; idari ve mali özerklikleri vardır. İşlemleri idari işlem olduğundan idari yargı denetimine tabidir.',
    ),
    # düzey 2
    '0002': patch(
        'Ruhsatını yeni alan bir meslek mensubu, mesleki faaliyete başlamadan önce odaya kaydolmanın isteğe bağlı olduğunu düşünmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu, bölgesindeki odaya kaydolmadan mesleki faaliyette bulunamaz',
            'B': 'Odaya kayıt isteğe bağlıdır; ruhsat tek başına faaliyet için yeterlidir',
            'C': 'Odaya kayıt, mesleki faaliyete başlandıktan bir yıl sonra yapılır',
            'D': 'Odaya kayıt yalnızca yeminli mali müşavirler için zorunludur',
            'E': 'Meslek mensubu dilediği bölgedeki odaya kaydolabilir',
        },
        'A',
        '3568 md. 19: meslek mensupları, mesleki faaliyette bulunabilmek için bölgesi içinde bulundukları ODAYA KAYDOLMAK zorundadır. Kayıt isteğe bağlı değildir ve unvana göre değişmez; ayrıca meslek mensubu işyerinin bulunduğu bölgenin odasına kaydolur, oda seçiminde serbest değildir.',
    ),
    # düzey 1
    '0003': patch(
        'Odaların bir araya gelerek oluşturduğu ulusal üst kuruluş belirlenmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Odaların bağlı olduğu üst kuruluş Hazine ve Maliye Bakanlığı'dır",
            'B': "Odaların üye olduğu üst kuruluş, ticaret ve sanayi odalarını da çatısı altında toplayan Türkiye Odalar ve Borsalar Birliği'dir",
            'C': "Odaların üye olduğu üst kuruluş, Türkiye Serbest Muhasebeci Mali Müşavirler ve Yeminli Mali Müşavirler Odaları Birliği'dir",
            'D': "Odaların üye olduğu üst kuruluş Türkiye Bankalar Birliği'dir",
            'E': "Odaların üye olduğu üst kuruluş Kamu Gözetimi Kurumu'dur",
        },
        'C',
        "3568 md. 29: odaların üye olduğu üst kuruluş TÜRMOB kısaltmasıyla anılan Türkiye Serbest Muhasebeci Mali Müşavirler ve Yeminli Mali Müşavirler Odaları Birliği'dir. Hazine ve Maliye Bakanlığı üst kuruluş değil, mesleğin ve meslek örgütünün GENEL GÖZETİM VE DENETİMİNDEN sorumlu bakanlıktır (md. 1 ve 49).",
    ),
    # düzey 2
    '0004': patch(
        'Bir meslek odasının organları belirlenmektedir. Buna göre aşağıdakilerden hangisi odanın zorunlu organlarından biri değildir?',
        {
            'A': 'Disiplin kurulu',
            'B': 'Genel kurul',
            'C': 'Yönetim kurulu',
            'D': 'Yüksek danışma kurulu',
            'E': 'Denetleme kurulu',
        },
        'D',
        "3568 md. 18: odanın organları GENEL KURUL, YÖNETİM KURULU, DİSİPLİN KURULU ve DENETLEME KURULU'dur. Yüksek danışma kurulu oda düzeyinde değil, Birlik bünyesinde öngörülmüş bir danışma organıdır.",
    ),
    # düzey 2
    '0005': patch(
        'Bir oda genel kurulu toplanmış; yönetim kurulunun bu kararı değiştirebileceği ileri sürülmüştür. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Genel kurul kararları ancak Birlik yönetim kurulunun onayıyla yürürlüğe girer',
            'B': 'Yönetim kurulu odanın en yetkili organı olup genel kurulun aldığı kararları değiştirebilir',
            'C': 'Genel kurul yalnızca danışma organıdır; bağlayıcı karar alamaz',
            'D': 'Disiplin kurulu genel kurul kararlarını denetleyip iptal edebilir',
            'E': 'Genel kurul odanın en yetkili karar organıdır; yönetim kurulu onun kararlarını değiştiremez',
        },
        'E',
        '3568 md. 18 ve 19: genel kurul odanın EN YETKİLİ KARAR ORGANIDIR; oda organlarını seçer, bütçeyi ve kesin hesabı görüşüp karara bağlar, yönetim kurulunu ibra eder. Yönetim kurulu genel kurulun icra organıdır ve onun kararlarını değiştiremez.',
    ),
    # düzey 1
    '0006': patch(
        'Bir odada, genel kurul kararlarının uygulanması ve günlük işlerin yürütülmesi görevini hangi organın taşıdığı belirlenmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yönetim kurulu, genel kurul kararlarını uygulayan ve odayı temsil eden icra organıdır',
            'B': 'Yönetim kurulu odanın en yetkili karar organı olup genel kurulun kararlarını değiştirebilir',
            'C': 'Yönetim kurulu yalnızca disiplin cezası vermekle görevlidir',
            'D': 'Yönetim kurulu odanın hesaplarını denetleyen organdır',
            'E': 'Yönetim kurulu Hazine ve Maliye Bakanlığınca atanır',
        },
        'A',
        '3568 md. 18 ve 20: yönetim kurulu, genel kurulca seçilen ve odanın işlerini yürüten İCRA organıdır; odayı temsil eder ve genel kurul kararlarını uygular. Karar organı genel kurul, ceza organı disiplin kurulu, denetim organı ise denetleme kuruludur.',
    ),
    # düzey 1
    '0007': patch(
        'Bir odada meslek mensuplarına disiplin cezası verme görevini hangi organın taşıdığı belirlenmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Disiplin kurulu üyeleri Birlik yönetim kurulunca atanır ve oda genel kurulu tarafından seçilmez',
            'B': 'Disiplin kurulu odanın en yetkili karar organıdır',
            'C': 'Disiplin kurulu odanın icra organı olup günlük işleri yürütür',
            'D': 'Disiplin kurulu, meslek mensupları hakkında disiplin soruşturması sonucunda ceza vermekle görevlidir',
            'E': 'Disiplin kurulu odanın hesaplarını denetlemekle görevlidir',
        },
        'D',
        '3568 md. 18 ve 21: disiplin kurulu, meslek mensupları hakkında disiplin kovuşturması yapmak ve ceza vermekle görevlidir. Tüm oda organları GENEL KURULCA seçilir; hesap denetimi denetleme kuruluna, icra ise yönetim kuruluna aittir.',
    ),
    # düzey 2
    '0008': patch(
        'Mesleğin ve meslek örgütünün genel gözetim ve denetiminden sorumlu idare belirlenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Gözetim yetkisi, meslek kuruluşunun idari özerkliğini ortadan kaldırmaz',
            'B': 'Meslek örgütü üzerinde genel gözetim ve denetim yetkisi Kamu Gözetimi Kurumuna aittir',
            'C': 'Meslek kuruluşlarının işlemleri idari yargı denetimine tabidir',
            'D': 'Bakanlık, meslek örgütünün organlarının yerine geçerek karar alamaz',
            'E': 'Mesleğin ve meslek örgütünün genel gözetim ve denetimi Hazine ve Maliye Bakanlığına aittir',
        },
        'B',
        '3568 md. 1 ve 49: mesleğin ve meslek örgütünün genel gözetim ve denetimi HAZİNE VE MALİYE BAKANLIĞINCA yürütülür. Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu ise BAĞIMSIZ DENETİM alanını düzenler; 3568 meslek örgütü üzerinde genel gözetim yetkisi yoktur. Gözetim yetkisi vesayet niteliğindedir ve organların yerine geçmeye izin vermez.',
    ),
    # düzey 2
    '0009': patch(
        "3568 sayılı Kanun'a göre meslek mensuplarına verilebilecek disiplin cezaları belirlenmektedir. Buna göre aşağıdakilerden hangisi bu cezalardan biri değildir?",
        {
            'A': 'Kınama cezası',
            'B': 'Meslekten çıkarma',
            'C': 'Geçici olarak mesleki faaliyetten alıkoyma',
            'D': 'Uyarma cezası',
            'E': 'Ruhsatın süresiz olarak askıya alınması',
        },
        'E',
        "3568 md. 48: disiplin cezaları UYARMA, KINAMA, GEÇİCİ OLARAK MESLEKÎ FAALİYETTEN ALIKOYMA, YEMİNLİ SIFATINI KALDIRMA ve MESLEKTEN ÇIKARMA'dır. 'Ruhsatın süresiz askıya alınması' kanunda öngörülmüş bir disiplin cezası değildir.",
    ),
    # düzey 1
    '0010': patch(
        'Bir meslek mensubuna, mesleğin yürütülmesinde daha dikkatli davranması gerektiğinin yazıyla bildirilmesine karar verilmiştir. Buna göre uygulanan disiplin cezası aşağıdakilerden hangisidir?',
        {
            'A': 'Kınama cezası',
            'B': 'Meslekten çıkarma',
            'C': 'Uyarma cezası',
            'D': 'Geçici olarak mesleki faaliyetten alıkoyma',
            'E': 'Yeminli sıfatını kaldırma',
        },
        'C',
        '3568 md. 48: UYARMA, meslek mensubuna mesleğin yürütülmesinde daha dikkatli davranması gerektiğinin yazı ile bildirilmesidir. KINAMA ise meslek mensubuna görevinde ve davranışında kusurlu sayıldığının yazı ile bildirilmesidir; uyarmadan bir derece ağırdır.',
    ),
    # düzey 1
    '0011': patch(
        'Bir meslek mensubuna, görevinde ve davranışında kusurlu sayıldığının yazıyla bildirilmesine karar verilmiştir. Buna göre uygulanan disiplin cezası aşağıdakilerden hangisidir?',
        {
            'A': 'Geçici olarak mesleki faaliyetten alıkoyma',
            'B': 'Uyarma cezası',
            'C': 'Yeminli sıfatını kaldırma',
            'D': 'Meslekten çıkarma',
            'E': 'Kınama cezası',
        },
        'E',
        '3568 md. 48: KINAMA, meslek mensubuna görevinde ve davranışında KUSURLU sayıldığının yazı ile bildirilmesidir. Uyarma ise yalnızca daha dikkatli davranılması gerektiğinin bildirilmesi olup kusur tespiti içermez.',
    ),
    # düzey 2
    '0012': patch(
        'Bir meslek mensubuna geçici olarak mesleki faaliyetten alıkoyma cezası verilmiştir. Meslek mensubu, ceza süresince unvanını kullanmaya ve ruhsatını elinde tutmaya devam edeceğini düşünmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ceza süresince meslek mensubu yalnızca danışmanlık işlerini yürütebilir',
            'B': 'Ceza süresince meslek mensubu mesleki faaliyette bulunamaz ve unvanının gerektirdiği yetkileri kullanamaz',
            'C': 'Ceza, meslek mensubunun ruhsatının kalıcı olarak geri alınması sonucunu doğurur',
            'D': 'Ceza yalnızca yeminli mali müşavirlere uygulanabilir',
            'E': 'Ceza süresince meslek mensubu mevcut faaliyetini sürdürebilir; yalnızca yeni iş kabul etmesi yasaktır',
        },
        'B',
        '3568 md. 48: GEÇİCİ OLARAK MESLEKÎ FAALİYETTEN ALIKOYMA, mesleki sıfatı saklı kalmak koşuluyla belirli bir süre için meslekî faaliyetten alıkonulmadır. Ceza süresince meslek mensubu faaliyette bulunamaz ve yetkilerini kullanamaz; ancak ruhsatı kalıcı olarak geri alınmaz — bu sonuç MESLEKTEN ÇIKARMA cezasına özgüdür.',
    ),
    # düzey 2
    '0013': patch(
        'Bir meslek mensubu hakkında meslekten çıkarma cezası kesinleşmiştir. Meslek mensubu, cezanın yalnızca bir süre için faaliyeti durdurduğunu ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslekten çıkarma en ağır disiplin cezası olup meslek mensubunun ruhsatı geri alınır',
            'B': 'Meslekten çıkarma yalnızca yeminli mali müşavirlere uygulanabilir',
            'C': 'Meslekten çıkarma, belirli bir süre için mesleki faaliyetin durdurulması anlamına gelir',
            'D': 'Meslekten çıkarma cezası verildikten sonra kendiliğinden kınamaya dönüşür',
            'E': 'Meslekten çıkarma yalnızca odaya olan aidat borcunun ödenmemesi hâlinde verilir',
        },
        'A',
        '3568 md. 48: MESLEKTEN ÇIKARMA, meslek mensubunun ruhsatnamesinin geri alınarak bir daha mesleği icra etmesine izin verilmemesidir; en ağır disiplin cezasıdır. Geçici süreli faaliyet yasağı ise ayrı bir ceza türüdür (geçici olarak meslekî faaliyetten alıkoyma).',
    ),
    # düzey 2
    '0014': patch(
        'Bir yeminli mali müşavir hakkında yeminli sıfatının kaldırılması cezası uygulanmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ceza, meslek mensubunun yalnızca tasdik yetkisini değil tüm mesleki faaliyetini kalıcı olarak sona erdirir',
            'B': 'Ceza yalnızca serbest muhasebeci mali müşavirlere uygulanır',
            'C': 'Ceza yalnızca tasdik yetkisini geçici olarak durdurur',
            'D': 'Ceza yeminli mali müşavirlere özgüdür; meslek mensubu YMM unvanını ve tasdik yetkisini kaybeder',
            'E': 'Ceza tüm meslek mensuplarına uygulanabilir',
        },
        'D',
        "3568 md. 48: YEMİNLİ SIFATININ KALDIRILMASI cezası, niteliği gereği yalnızca YEMİNLİ MALİ MÜŞAVİRLERE uygulanabilir; meslek mensubu YMM unvanını ve buna bağlı TASDİK yetkisini kaybeder. Tüm mesleki faaliyeti sona erdiren ceza ise MESLEKTEN ÇIKARMA'dır.",
    ),
    # düzey 2
    '0015': patch(
        'Meslek örgütü ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Odalar ve TÜRMOB kamu kurumu niteliği taşıyan meslek kuruluşlarıdır. II. Meslek mensupları mesleki faaliyette bulunabilmek için odaya kaydolmak zorundadır. III. Odaların en yetkili karar organı yönetim kuruludur.',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'Yalnız I',
            'D': 'I ve III',
            'E': 'II ve III',
        },
        'A',
        'I doğrudur (3568 md. 14, 29; Anayasa md. 135). II doğrudur (md. 19). III YANLIŞTIR: odanın en yetkili karar organı GENEL KURULDUR; yönetim kurulu genel kurul kararlarını uygulayan icra organıdır (md. 18-20).',
    ),
    # düzey 2
    '0016': patch(
        'Bir meslek mensubu hakkında disiplin soruşturması yürütülmüş ve ceza verilmesi gündeme gelmiştir. Meslek mensubu, cezayı doğrudan Birliğin vereceğini düşünmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Disiplin cezasını ilk derecede meslek mensubunun kayıtlı olduğu odanın disiplin kurulu verir',
            'B': 'Disiplin cezasını ilk derecede idare mahkemesi verir',
            'C': 'Disiplin cezasını ilk derecede, meslek örgütü üzerinde gözetim yetkisi bulunan Hazine ve Maliye Bakanlığı verir',
            'D': 'Disiplin cezasını ilk derecede Birlik disiplin kurulu verir',
            'E': 'Disiplin cezasını ilk derecede oda yönetim kurulu verir',
        },
        'A',
        '3568 md. 18, 21 ve 48: disiplin cezası verme yetkisi ilk derecede meslek mensubunun kayıtlı olduğu ODANIN DİSİPLİN KURULUNA aittir. Birlik disiplin kurulu itiraz mercii olarak görev yapar; yönetim kurulu soruşturmayı başlatır ancak ceza vermez.',
    ),
    # düzey 3
    '0017': patch(
        'Oda disiplin kurulunca hakkında kınama cezası verilen bir meslek mensubu, karara karşı başvuru yolunu araştırmaktadır. Meslek mensubu doğrudan idare mahkemesine gitmeyi düşünmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Oda disiplin kurulu kararları kesin olup hiçbir başvuru yolu bulunmaz',
            'B': 'Meslek mensubu doğrudan Hazine ve Maliye Bakanlığına itiraz eder',
            'C': 'Meslek mensubu önce Birlik disiplin kuruluna itiraz eder; ceza kesinleştikten sonra idari yargıya başvurabilir',
            'D': 'Meslek mensubu itirazını oda genel kuruluna yapar',
            'E': 'Meslek mensubu doğrudan idare mahkemesinde iptal davası açar; meslek örgütü içinde bir itiraz yolu bulunmaz',
        },
        'C',
        '3568 md. 48 ve Disiplin Yönetmeliği: oda disiplin kurulu kararlarına karşı BİRLİK DİSİPLİN KURULUNA itiraz edilir. İtiraz üzerine verilen kararla ceza kesinleşir; kesinleşen disiplin cezası bir idari işlem olduğundan 2577 sayılı İYUK uyarınca İDARİ YARGIDA iptal davasına konu edilebilir.',
    ),
    # düzey 2
    '0018': patch(
        "TÜRMOB'un organları belirlenmektedir. Buna göre aşağıdakilerden hangisi Birliğin organlarından biri değildir?",
        {
            'A': 'Birlik yönetim kurulu',
            'B': 'Oda genel kurulu',
            'C': 'Birlik disiplin kurulu',
            'D': 'Birlik genel kurulu',
            'E': 'Birlik denetleme kurulu',
        },
        'B',
        "3568 md. 30: Birliğin organları BİRLİK GENEL KURULU, BİRLİK YÖNETİM KURULU, BİRLİK DİSİPLİN KURULU ve BİRLİK DENETLEME KURULU'dur. Oda genel kurulu ise ODA düzeyindeki bir organdır ve Birliğin organı değildir.",
    ),
    # düzey 2
    '0019': patch(
        'Meslek örgütünün temel amaçları belirlenmektedir. Buna göre aşağıdakilerden hangisi bu amaçlardan biri değildir?',
        {
            'A': 'Meslek disiplinini ve ahlakını korumak',
            'B': 'Mesleğin gelişmesini sağlamak ve mesleki standartları yükseltmek',
            'C': 'Meslek mensuplarının birbirleriyle ve iş sahipleriyle ilişkilerinde dürüstlüğü ve güveni sağlamak',
            'D': 'Meslek mensuplarının hak ve menfaatlerini korumak ve temsil etmek',
            'E': 'Üyeleri adına müşterilerle ücret sözleşmesi imzalamak ve iş dağıtımı yapmak',
        },
        'E',
        '3568 md. 14 ve 29: meslek kuruluşlarının amaçları mesleğin gelişmesini sağlamak, meslek mensupları arasında ve iş sahipleriyle ilişkilerde dürüstlük ve güveni tesis etmek, meslek disiplinini ve ahlakını korumaktır. Üyeler adına iş almak ya da iş dağıtmak meslek kuruluşunun görevi değildir; bu meslek mensubunun kendi faaliyetidir.',
    ),
    # düzey 3
    '0020': patch(
        'Bir disiplin dosyasında, verilebilecek cezaların ağırlığına göre sıralanması istenmiştir. Buna göre en hafiften en ağıra doğru doğru sıralama aşağıdakilerden hangisidir?',
        {
            'A': 'Uyarma – kınama – meslekten çıkarma – geçici olarak mesleki faaliyetten alıkoyma – yeminli sıfatını kaldırma',
            'B': 'Geçici olarak mesleki faaliyetten alıkoyma – uyarma – kınama – yeminli sıfatını kaldırma – meslekten çıkarma',
            'C': 'Kınama – uyarma – geçici olarak mesleki faaliyetten alıkoyma – meslekten çıkarma – yeminli sıfatını kaldırma',
            'D': 'Uyarma – kınama – geçici olarak mesleki faaliyetten alıkoyma – yeminli sıfatını kaldırma – meslekten çıkarma',
            'E': 'Uyarma – geçici olarak mesleki faaliyetten alıkoyma – kınama – meslekten çıkarma – yeminli sıfatını kaldırma',
        },
        'D',
        "3568 md. 48 cezaları hafiften ağıra şöyle sıralar: uyarma (dikkat çekme), kınama (kusurun bildirilmesi), geçici olarak meslekî faaliyetten alıkoyma (belirli süre faaliyet yasağı), yeminli sıfatının kaldırılması (YMM'ye özgü) ve meslekten çıkarma (en ağır ceza; ruhsat geri alınır).",
    ),
    # düzey 2
    '0021': patch(
        'Bir odada denetleme kurulunun görev alanı tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Denetleme kurulu odanın en yetkili karar organıdır',
            'B': 'Denetleme kurulu meslek mensuplarına disiplin cezası verir',
            'C': 'Denetleme kurulu odanın günlük işlerini yürüten icra organıdır',
            'D': 'Denetleme kurulu üyeleri Birlik yönetim kurulu tarafından atanır ve oda genel kurulunca seçilmez',
            'E': 'Denetleme kurulu odanın işlem ve hesaplarını denetler; disiplin cezası verme yetkisi bulunmaz',
        },
        'E',
        '3568 md. 18 ve 22: denetleme kurulu, odanın işlemlerini ve hesaplarını denetleyerek genel kurula rapor sunar. Disiplin cezası verme yetkisi DİSİPLİN KURULUNA, icra yetkisi YÖNETİM KURULUNA aittir. Tüm oda organları genel kurulca seçilir.',
    ),
    # düzey 2
    '0022': patch(
        'Bir meslek mensubunun disiplin soruşturmasına konu olabilecek fiilleri belirlenmektedir. Buna göre aşağıdakilerden hangisi disiplin soruşturmasına konu olmaz?',
        {
            'A': 'Meslek mensubunun iş elde etmek amacıyla reklam yapması',
            'B': 'Meslek mensubunun asgari ücret tarifesinin altında iş kabul etmesi',
            'C': 'Meslek mensubunun bir anonim şirkete sermaye ortağı olması',
            'D': 'Meslek mensubunun meslek sırlarını ifşa etmesi',
            'E': 'Meslek mensubunun bir meslektaşına karşı haksız rekabette bulunması',
        },
        'C',
        "3568 md. 45 meslek mensuplarının limited ve anonim şirketlere ORTAK OLMASINA açıkça izin verir; bu tek başına disiplin suçu değildir (hizmet verilen işletmeye ortaklık ise ayrı bir tarafsızlık sorunudur). Diğer seçenekler md. 46, 44, 43 ve 47'ye aykırılık oluşturur ve md. 48 uyarınca disiplin cezası gerektirir.",
    ),
    # düzey 2
    '0023': patch(
        'Bir meslek mensubu hakkında yapılan şikâyet üzerine disiplin sürecinin nasıl başlayacağı tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Disiplin soruşturması yalnızca şikâyet üzerine başlar; oda resen soruşturma açamaz',
            'B': 'Soruşturma sonucunda dosya, karar verilmek üzere disiplin kuruluna sevk edilebilir',
            'C': 'Meslek mensubuna savunma hakkı tanınması gerekir',
            'D': 'Soruşturma şikâyet üzerine ya da resen başlatılabilir',
            'E': 'Soruşturma sonunda ceza verilmemesine de karar verilebilir',
        },
        'A',
        '3568 ve Disiplin Yönetmeliği: disiplin soruşturması ilgililerin şikâyeti üzerine başlatılabileceği gibi oda yönetim kurulunca RESEN de başlatılabilir. Soruşturmada meslek mensubuna SAVUNMA HAKKI tanınması zorunludur; savunma alınmadan ceza verilemez.',
    ),
    # düzey 3
    '0024': patch(
        'Disiplin cezaları ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Uyarma, meslek mensubuna daha dikkatli davranması gerektiğinin yazıyla bildirilmesidir. II. Meslekten çıkarma cezasında meslek mensubunun ruhsatnamesi geri alınır. III. Disiplin cezasını ilk derecede Birlik disiplin kurulu verir. IV. Kesinleşen disiplin cezalarına karşı yargı yolu kapalıdır.',
        {
            'A': 'Yalnız III',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'I, III ve IV',
            'E': 'III ve IV',
        },
        'E',
        'III YANLIŞ: disiplin cezasını ilk derecede ODA DİSİPLİN KURULU verir; Birlik disiplin kurulu itiraz merciidir. IV YANLIŞ: kesinleşen disiplin cezası idari işlem olduğundan Anayasa md. 125 ve İYUK uyarınca idari yargıda iptal davasına konu edilebilir. I ve II (md. 48) doğrudur.',
    ),
    # düzey 2
    '0025': patch(
        'Bir bölgede yeni bir meslek odası kurulması gündeme gelmiştir. Bölgede kayıtlı meslek mensubu sayısı yeterli görülmemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Oda kurulması yalnızca Birlik genel kurulunun takdirine bağlıdır',
            'B': 'Oda kurulması için meslek mensubu sayısı bakımından bir koşul aranmaz',
            'C': 'Her ilde meslek mensubu sayısına bakılmaksızın oda kurulur',
            'D': 'Oda kurulabilmesi için bölgede kanunda öngörülen sayıda meslek mensubu bulunması gerekir',
            'E': 'Oda kurulması için bölgede kayıtlı en az bir yeminli mali müşavir bulunması yeterli sayılır',
        },
        'D',
        '3568 md. 14: odalar, bölgelerinde kanunda öngörülen sayıda meslek mensubunun bulunması hâlinde kurulur. Sayı koşulu gerçekleşmeyen yerlerdeki meslek mensupları en yakın odaya kaydolur. Kuruluş kanuni koşula bağlıdır; takdire ya da tek bir meslek mensubunun varlığına bırakılmamıştır.',
    ),
    # düzey 1
    '0026': patch(
        "TÜRMOB bünyesindeki Yüksek Danışma Kurulu'nun işlevi tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Kurul, mesleğe ve meslek örgütüne ilişkin konularda görüş ve öneri oluşturan bir danışma kuruludur',
            'B': 'Kurul meslek mensuplarına disiplin cezası verir',
            'C': 'Kurul, oda genel kurullarının yerine geçerek seçim yapar',
            'D': 'Kurul, meslek mensuplarının ruhsat başvurularını inceleyerek karara bağlayan yürütme organıdır',
            'E': 'Kurul Birliğin en yetkili karar organıdır',
        },
        'A',
        'Yüksek Danışma Kurulu, mesleğe ve meslek örgütüne ilişkin konularda görüş ve öneri oluşturmakla görevli DANIŞMA organıdır; bağlayıcı karar almaz. Birliğin en yetkili karar organı Birlik Genel Kurulu, ceza organı Birlik Disiplin Kuruludur (md. 30).',
    ),
    # düzey 2
    '0027': patch(
        'Meslek mensuplarının odaya karşı mali yükümlülükleri belirlenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Aidatların süresinde ödenmemesi takip ve disiplin sorumluluğu doğurabilir',
            'B': 'Meslek mensupları odaya giriş aidatı öder',
            'C': 'Aidat tutarları ilgili mevzuat çerçevesinde belirlenir',
            'D': 'Meslek mensupları odaya yıllık aidat öder',
            'E': 'Meslek mensuplarının odaya karşı herhangi bir mali yükümlülüğü bulunmaz',
        },
        'E',
        '3568 md. 24 ve ilgili düzenlemeler: meslek mensupları odaya GİRİŞ AİDATI ve YILLIK AİDAT ödemekle yükümlüdür. Aidat, odanın temel gelir kaynaklarındandır; ödenmemesi takip ve disiplin sonuçları doğurur.',
    ),
    # düzey 2
    '0028': patch(
        'Meslek mensubuna verilen disiplin cezalarının sonuçları değerlendirilmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kesinleşen disiplin cezaları meslek mensubunun sicilinde yer alır',
            'B': 'Geçici olarak mesleki faaliyetten alıkoyma cezası süresince hiçbir mesleki faaliyet yapılamaz',
            'C': 'Meslekten çıkarma cezasında ruhsatname geri alınır',
            'D': 'Disiplin cezaları yalnızca odayı ilgilendirir; meslek mensubunun sicilinde yer almaz',
            'E': 'Disiplin cezaları tekerrürde ağırlaştırıcı olarak dikkate alınır',
        },
        'D',
        "Disiplin Yönetmeliği: kesinleşen disiplin cezaları meslek mensubunun SİCİLİNE İŞLENİR ve tekerrürde ağırlaştırıcı sebep olarak dikkate alınır. Ceza türlerine bağlı sonuçlar (faaliyet yasağı, ruhsatın geri alınması) md. 48'de düzenlenmiştir.",
    ),
    # düzey 3
    '0029': patch(
        'Bir meslek mensubu, aynı fiil nedeniyle hem oda disiplin kurulunca cezalandırılmış hem de hakkında ceza yargılaması başlatılmıştır. Meslek mensubu, aynı fiilden iki kez cezalandırılamayacağını ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Aynı fiile ilişkin ceza yargılaması başladığında verilmiş disiplin cezası kendiliğinden ortadan kalkar',
            'B': 'Disiplin cezası ancak mahkûmiyet kesinleştikten sonra verilebilir',
            'C': 'Disiplin sorumluluğu ile cezai sorumluluk ayrı ayrı doğar; aynı fiil için her ikisi birlikte uygulanabilir',
            'D': 'Meslek mensubu, iki süreçten hangisine tabi olacağını seçebilir',
            'E': 'Disiplin cezası verilmişse ceza yargılaması yapılamaz',
        },
        'C',
        "Disiplin sorumluluğu ile cezai sorumluluk AYRI HUKUKİ REJİMLERDİR: biri meslek düzenini, diğeri kamu düzenini korur. Aynı fiil nedeniyle her ikisi birlikte uygulanabilir ve bu 'aynı fiilden iki kez cezalandırma' yasağını ihlal etmez. Meslek mensubunun seçim hakkı yoktur; disiplin süreci ceza yargılamasının sonucunu beklemek zorunda da değildir.",
    ),
    # düzey 2
    '0030': patch(
        "TÜRMOB ve odalar ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Odaların en yetkili karar organı genel kuruldur. II. Odaların üye olduğu üst kuruluş TÜRMOB'dur. III. Mesleğin genel gözetim ve denetimi Hazine ve Maliye Bakanlığına aittir.",
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'II ve III',
            'E': 'I ve III',
        },
        'C',
        "Üç ifade de doğrudur. 3568 md. 18-19 genel kurulu odanın en yetkili karar organı sayar, md. 29 odaların üst kuruluşu olarak TÜRMOB'u düzenler, md. 1 ve 49 ise mesleğin ve meslek örgütünün genel gözetim ve denetimini Bakanlığa bırakır.",
    ),
    # düzey 3
    '0031': patch(
        'Bir meslek mensubu, defterlerini tuttuğu bir müşterisine ait ticari sırları rakip bir firmaya para karşılığında aktarmıştır. Fiil hem müşteriye zarar vermiş hem de kamuya yansımıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Fiil yalnızca disiplin sorumluluğu doğurur',
            'B': 'Müşteri şikâyet etmezse hiçbir sorumluluk doğmaz',
            'C': 'Disiplin süreci, aynı fiile ilişkin ceza yargılaması kesinleşmeden başlatılamaz; mahkeme kararının sonucu beklenir',
            'D': 'Fiil disiplin, mali ve cezai sorumluluğu birlikte doğurabilir; disiplin süreci ceza yargılamasının sonucunu beklemez',
            'E': 'Fiil yalnızca cezai sorumluluk doğurur; disiplin süreci yürütülemez',
        },
        'D',
        '3568 md. 43 sır saklama yükümlülüğünü, md. 48 disiplin sorumluluğunu düzenler; fiil ayrıca TBK md. 49 vd. uyarınca tazminat ve koşulları varsa cezai sorumluluk doğurur. Üç rejim birbirinden BAĞIMSIZDIR; disiplin soruşturması resen de açılabilir ve ceza yargılamasının sonucunu beklemek zorunda değildir.',
    ),
    # düzey 2
    '0032': patch(
        'Meslek örgütünün mesleki denetim işlevi tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Mesleki denetim, meslek mensuplarının mevzuata ve mesleki ilkelere uygun çalışıp çalışmadığını izlemeyi kapsar',
            'B': 'Mesleki denetim, meslek mensubunun müşterisinin vergi matrahını yeniden belirlemeyi kapsar',
            'C': 'Meslek mensubu, denetim kapsamında istenen bilgi ve belgeleri vermekle yükümlüdür',
            'D': 'Mesleki denetimde tespit edilen aykırılıklar disiplin sürecine konu olabilir',
            'E': 'Mesleki denetim, meslek kuruluşunun mesleki standartları koruma işlevinin parçasıdır',
        },
        'B',
        'Meslek örgütünün MESLEKİ DENETİMİ, meslek mensuplarının mevzuata ve mesleki ilkelere uygunluğunu izlemeye yöneliktir; aykırılıklar disiplin sürecine taşınır. Mükellefin VERGİ MATRAHINI belirlemek ise vergi idaresinin yetkisidir; meslek kuruluşunun görev alanında değildir.',
    ),
    # düzey 3
    '0033': patch(
        "TÜRMOB Genel Kurulunca usulüne uygun olarak alınan ve Resmî Gazete'de yayımlanan bir mecburi meslek kararı bulunmaktadır. Bir meslek mensubu bu karara uymamıştır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Kararlar yalnızca kendisine katılan meslek mensuplarını bağlar',
            'B': "Mecburi meslek kararları yalnızca yeminli mali müşavirleri bağlar; SMMM'ler için tavsiye değeri taşır",
            'C': 'Mecburi meslek kararları bağlayıcı olmayıp yalnızca tavsiye değeri taşır',
            'D': 'Kararlara uymamak yalnızca odaya bildirim yükümlülüğü doğurur',
            'E': 'Mecburi meslek kararları meslek mensuplarını bağlar; uymamak disiplin sorumluluğu doğurur',
        },
        'E',
        "3568 md. 33: Birlik Genel Kurulu, meslek mensuplarının uyacağı MECBURİ MESLEK KARARLARI alır; bu kararlar Resmî Gazete'de yayımlanarak yürürlüğe girer ve TÜM meslek mensuplarını bağlar. Uymamak md. 48 uyarınca disiplin cezası gerektirir; kararlar tavsiye niteliğinde değildir.",
    ),
    # düzey 2
    '0034': patch(
        'Bir meslek mensubu mesleği bırakmaya ve ruhsatını iade etmeye karar vermiştir. Meslek mensubunun devam eden müşteri işleri bulunmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ruhsat iadesi, meslek mensubunun mesleki faaliyet döneminden doğan sorumluluklarını da sona erdirir',
            'B': 'Meslek mensubu mesleği bırakma yönündeki iradesini bağlı olduğu odaya bildirmelidir',
            'C': 'Devam eden işlerin devri ve belgelerin iş sahiplerine geri verilmesi gerekir',
            'D': 'Odaya kayıt silinir ve unvanın kullanılması sona erer',
            'E': 'Faaliyet dönemine ilişkin defter ve belgeler, mevzuatta öngörülen süre boyunca saklanmaya devam eder',
        },
        'A',
        'Mesleği bırakan meslek mensubu odaya bildirimde bulunur, kaydı silinir ve unvanı kullanmaya son verir; devam eden işleri devretmesi ve belgeleri iş sahiplerine geri vermesi gerekir. Ancak ruhsat iadesi, FAALİYET DÖNEMİNDEN doğan mali, disiplin ve cezai sorumluluğu ORTADAN KALDIRMAZ.',
    ),
    # düzey 2
    '0035': patch(
        'Kesinleşen bir disiplin cezasına karşı hangi yargı yoluna başvurulacağı tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Dava iş mahkemesinde açılır',
            'B': 'Dava adliye mahkemelerinde, genel görevli asliye hukuk mahkemesinde iptal talebiyle açılır',
            'C': 'Meslek kuruluşunun işlemi idari işlem olduğundan iptal davası idari yargıda açılır',
            'D': "Dava yalnızca Danıştay'da ilk derece olarak açılabilir",
            'E': 'Kesinleşen disiplin cezalarına karşı hiçbir yargı yoluna başvurulamaz',
        },
        'C',
        'Odalar ve Birlik kamu kurumu niteliği taşıyan meslek kuruluşu olduğundan işlemleri İDARİ İŞLEMDİR (Anayasa md. 135). Kesinleşen disiplin cezasına karşı 2577 sayılı İYUK uyarınca İDARE MAHKEMESİNDE iptal davası açılır. Anayasa md. 125 uyarınca idarenin her türlü işlem ve eylemine karşı yargı yolu açıktır.',
    ),
    # düzey 3
    '0036': patch(
        'Disiplin süreci ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. İlk derece disiplin cezasını oda disiplin kurulu verir. II. Savunma hakkı tanınmadan disiplin cezası verilebilir. III. Oda disiplin kurulu kararlarına karşı Birlik disiplin kuruluna itiraz edilir. IV. Aynı fiil nedeniyle disiplin ve cezai sorumluluk birlikte doğamaz.',
        {
            'A': 'II ve III',
            'B': 'Yalnız II',
            'C': 'II ve IV',
            'D': 'I, II ve IV',
            'E': 'I ve III',
        },
        'C',
        'II YANLIŞ: Anayasa md. 129 uyarınca savunma hakkı tanınmadıkça disiplin cezası verilemez. IV YANLIŞ: disiplin sorumluluğu ile cezai sorumluluk ayrı rejimler olup aynı fiil için birlikte doğabilir. I ve III doğrudur.',
    ),
    # düzey 2
    '0037': patch(
        'Bir meslek mensubu, ilk kez ve hafif nitelikte bir kural ihlalinde bulunmuştur (şeklî bir eksiklik). Disiplin kurulu, doğrudan geçici olarak mesleki faaliyetten alıkoyma cezası vermeyi değerlendirmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Disiplin cezası fiilin ağırlığıyla orantılı olmalıdır; hafif ve ilk ihlalde uyarma veya kınama uygun düşer',
            'B': 'Disiplin kurulu ceza türünü fiilin ağırlığına bakmaksızın serbestçe belirler',
            'C': 'İlk kez işlenen ihlallerde hiçbir ceza verilemez; disiplin cezası yalnızca ikinci ihlalde gündeme gelir',
            'D': 'Hafif ihlallerde de en ağır cezanın verilmesi kanunen zorunludur',
            'E': 'Ceza türü meslek mensubunun kıdemine göre belirlenir',
        },
        'A',
        'Disiplin hukukunda ÖLÇÜLÜLÜK ilkesi geçerlidir: verilecek ceza, fiilin ağırlığı, meslek mensubunun kusuru ve varsa tekerrür gibi ölçütlerle orantılı olmalıdır. İlk kez işlenen hafif nitelikli bir ihlalde uyarma veya kınama uygun düşer. Kurulun takdiri sınırsız değildir ve yargı denetimine tabidir.',
    ),
    # düzey 3
    '0038': patch(
        'Bir meslek mensubu, daha önce kınama cezası aldığı bir kural ihlalini tekrar işlemiştir. Buna göre tekerrür bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tekerrür hâlinde ceza kendiliğinden meslekten çıkarmaya dönüşür',
            'B': 'Tekerrür yalnızca yeminli mali müşavirler bakımından ağırlaştırıcı sonuç doğurur',
            'C': 'Aynı veya benzer ihlalin tekrarı, bir derece ağır cezanın uygulanması sonucunu doğurabilir',
            'D': 'Tekerrür disiplin hukukunda dikkate alınmaz; her fiil önceki cezalardan bağımsız olarak değerlendirilir',
            'E': 'Tekerrür hâlinde önceki ceza ortadan kalkar ve yalnızca yeni ceza uygulanır',
        },
        'C',
        'Disiplin Yönetmeliği: disiplin cezası verilmesine karar verilen bir fiilin tekrarlanması hâlinde BİR DERECE AĞIR ceza uygulanır. Tekerrür otomatik olarak en ağır cezayı doğurmaz ve unvana göre değişmez; ayrıca önceki ceza ortadan kalkmaz, ağırlaştırıcı olarak dikkate alınır.',
    ),
    # düzey 1
    '0039': patch(
        'Meslek örgütünün üyelerini temsil etme işlevi tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek örgütünün temsil yetkisi bulunmaz; her meslek mensubu kendini temsil eder',
            'B': 'Meslek örgütü, üyelerini yurt içinde ve gerektiğinde yurt dışında temsil eder',
            'C': 'Temsil yetkisi yalnızca yeminli mali müşavirler bakımından söz konusudur',
            'D': 'Temsil yetkisi yalnızca Hazine ve Maliye Bakanlığı tarafından kullanılır',
            'E': 'Meslek örgütü üyelerini yalnızca disiplin süreçlerinde temsil eder',
        },
        'B',
        '3568 md. 14 ve 29: odalar ve Birlik, mesleği ve meslek mensuplarını temsil eden kuruluşlardır; üyelerini yurt içinde ve gerektiğinde uluslararası kuruluşlar nezdinde temsil eder. Temsil yetkisi unvana ya da disiplin süreçlerine sınırlı değildir.',
    ),
    # düzey 2
    '0040': patch(
        'Meslek örgütü organlarının göreve gelme biçimi tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Oda ve Birlik organları Hazine ve Maliye Bakanlığınca atanır',
            'B': 'Organ üyeleri idare mahkemesi kararıyla belirlenir',
            'C': 'Organlar kıdem sırasına göre kendiliğinden göreve gelir',
            'D': 'Oda organları genel kurulda seçimle, Birlik organları ise atamayla göreve gelir',
            'E': 'Oda ve Birlik organları, üyelerin katıldığı genel kurullarda seçimle göreve gelir',
        },
        'E',
        "3568 md. 18-22 ve 30-33: oda ve Birlik organları, ilgili GENEL KURULLARDA yapılan SEÇİMLE göreve gelir. Kamu kurumu niteliği taşıyan meslek kuruluşlarında organların seçimle oluşması Anayasa md. 135'in gereğidir; atama ya da kıdem esası uygulanmaz.",
    ),
    # düzey 1
    '0041': patch(
        "TESMER'in (Temel Eğitim ve Staj Merkezi) işlevi tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'TESMER, meslek mensuplarının ücret tarifesini belirleyen kuruldur',
            'B': 'TESMER, TÜRMOB bünyesinde staj ve mesleki eğitim faaliyetlerini yürüten birimdir',
            'C': 'TESMER, bağımsız denetim kuruluşlarını yetkilendiren kurumdur',
            'D': 'TESMER, Hazine ve Maliye Bakanlığına bağlı bir genel müdürlüktür',
            'E': 'TESMER, meslek mensuplarına disiplin cezası vermekle görevli bağımsız bir kuruldur',
        },
        'B',
        'TESMER, TÜRMOB bünyesinde kurulmuş olup staj, temel eğitim, sınav hazırlığı ve sürekli mesleki eğitim faaliyetlerini yürütür. Disiplin yetkisi disiplin kurullarına, bağımsız denetim yetkilendirmesi Kamu Gözetimi Kurumuna, ücret tarifesi ise ilgili mevzuat sürecine aittir.',
    ),
    # düzey 2
    '0042': patch(
        'Meslek örgütü ve disiplin bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Oda disiplin kurulu kararları kesin olup itiraz edilemez',
            'B': 'Oda disiplin kurulu kararlarına karşı Birlik disiplin kuruluna itiraz edilir',
            'C': 'Kesinleşen disiplin cezasına karşı idari yargı yolu açıktır',
            'D': 'Disiplin cezasını ilk derecede oda disiplin kurulu verir',
            'E': 'Savunma hakkı tanınmadan disiplin cezası verilemez',
        },
        'A',
        'Oda disiplin kurulu kararları KESİN DEĞİLDİR; Birlik disiplin kuruluna itiraz edilebilir (3568 md. 48 ve Disiplin Yönetmeliği). İtiraz üzerine kesinleşen ceza ise idari yargı denetimine tabidir. Savunma hakkı Anayasa md. 129 güvencesidir.',
    ),
    # düzey 2
    '0043': patch(
        'Hakkında disiplin soruşturması yürütülen bir meslek mensubunun usul güvenceleri belirlenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu savunmasını yazılı olarak sunabilir',
            'B': 'Verilen karara karşı itiraz yolu açıktır',
            'C': 'Meslek mensubu isnat edilen fiilden haberdar edilmelidir',
            'D': 'Meslek mensubuna savunma hakkı tanınmadan hakkında herhangi bir disiplin cezası verilemez',
            'E': 'Meslek mensubuna savunma hakkı tanınması, cezanın ağırlığına göre disiplin kurulunun takdirindedir',
        },
        'E',
        "Disiplin hukukunun temel güvencesi SAVUNMA HAKKIDIR ve Anayasa md. 129 uyarınca 'savunma hakkı tanınmadıkça disiplin cezası verilemez'. Bu güvence cezanın ağırlığına ya da kurulun takdirine bağlı değildir; isnadın bildirilmesi ve itiraz yolu da sürecin parçasıdır.",
    ),
    # düzey 2
    '0044': patch(
        'İki meslek mensubu arasında iş devri ve ücret paylaşımı konusunda bir uyuşmazlık doğmuştur. Buna göre meslek örgütünün konumu bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek örgütünün kararı kesin olup yargı yoluna başvurulamaz',
            'B': 'Meslek örgütü uyuşmazlıkta taraflardan biri lehine karar vermekle yükümlüdür',
            'C': 'Meslek örgütü uyuşmazlıkta arabuluculuk yapabilir; yargı yolu ise açık kalır',
            'D': 'Uyuşmazlık yalnızca Hazine ve Maliye Bakanlığınca çözülür',
            'E': 'Meslek örgütünün meslek mensupları arasındaki uyuşmazlıklarda hiçbir işlevi bulunmaz',
        },
        'C',
        'Meslek örgütü, meslek mensupları arasındaki mesleki uyuşmazlıklarda taraflar arasında uzlaşma sağlamaya çalışır ve gerektiğinde disiplin boyutunu değerlendirir. Bu bir arabuluculuk işlevidir; tarafların YARGI YOLUNA başvurma hakkını ortadan kaldırmaz ve örgüt taraf tutmakla yükümlü değildir.',
    ),
    # düzey 2
    '0045': patch(
        'Meslek örgütü ve organları ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Oda organları genel kurul, yönetim kurulu, disiplin kurulu ve denetleme kuruludur. II. Oda organları genel kurulca seçimle göreve gelir. III. Disiplin cezası verme yetkisi denetleme kuruluna aittir.',
        {
            'A': 'Yalnız I',
            'B': 'II ve III',
            'C': 'I ve III',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'D',
        'I doğrudur (3568 md. 18). II doğrudur (md. 18-22). III YANLIŞTIR: disiplin cezası verme yetkisi DİSİPLİN KURULUNA aittir; denetleme kurulu odanın işlem ve hesaplarını denetler (md. 21-22).',
    ),
    # düzey 3
    '0046': patch(
        'Bir meslek mensubu, altı ay süreyle geçici olarak mesleki faaliyetten alıkoyma cezası almıştır. Meslek mensubu, ceza süresince müşterilerinin defterlerini tutmayı sürdürmeyi ve büro tabelasını korumayı planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu ceza süresince mevcut müşterilerinin işlerini sürdürebilir; yalnızca yeni iş kabul etmesi yasaktır',
            'B': 'Ceza süresince mesleki faaliyette bulunamaz; müşterilerinin işlerini başka bir meslek mensubuna devretmesi gerekir',
            'C': 'Ceza yalnızca yeni ruhsat başvurularını engeller; mevcut faaliyet etkilenmez',
            'D': 'Ceza süresince faaliyetini bir yardımcı aracılığıyla sürdürebilir',
            'E': 'Ceza süresince yalnızca danışmanlık verebilir, defter tutabilir',
        },
        'B',
        '3568 md. 48: geçici olarak meslekî faaliyetten alıkoyma, mesleki sıfat saklı kalmak koşuluyla belirli süre için FAALİYETTEN ALIKONULMADIR. Ceza süresince meslek mensubu hiçbir mesleki iş göremez; mevcut işlerin başka bir meslek mensubuna devri gerekir. Faaliyetin yardımcı ya da başka bir kişi üzerinden dolaylı sürdürülmesi cezanın dolanılması sayılır.',
    ),
    # düzey 2
    '0047': patch(
        'Odaların gelir kaynakları belirlenmektedir. Buna göre aşağıdakilerden hangisi bir oda geliri sayılmaz?',
        {
            'A': 'Meslek mensuplarının odaya kayıtta ödediği giriş aidatı',
            'B': 'Odanın düzenlediği eğitim, seminer ve yayın faaliyetlerinden sağlanan gelirler',
            'C': 'Meslek mensuplarının ödediği yıllık aidat',
            'D': 'Bağış, yardım ve faiz gelirleri',
            'E': 'Meslek mensuplarının müşterilerinden tahsil ettiği hizmet ücretlerinin tamamı',
        },
        'E',
        '3568 md. 24: oda gelirleri giriş ve yıllık aidatlar, belge ve yayın gelirleri, eğitim faaliyeti gelirleri, bağış ve yardımlar ile faiz gelirlerinden oluşur. Meslek mensubunun müşterisinden aldığı HİZMET ÜCRETİ kendi mesleki kazancıdır; odanın geliri değildir.',
    ),
    # düzey 1
    '0048': patch(
        'Meslek örgütünün üyelerine yönelik sürekli mesleki eğitim düzenleme işlevi tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Eğitim yalnızca yeminli mali müşavirlere yöneliktir',
            'B': 'Eğitim düzenleme yetkisi yalnızca Hazine ve Maliye Bakanlığına aittir',
            'C': 'Meslek örgütü sürekli mesleki eğitim düzenler; meslek mensubu bilgi ve becerisini güncel tutmakla yükümlüdür',
            'D': 'Meslek örgütünün sürekli mesleki eğitim düzenleme işlevi bulunmaz; bu görev üniversitelere ve özel eğitim kurumlarına aittir',
            'E': 'Ruhsat alındıktan sonra meslek mensubunun eğitim yükümlülüğü sona erer',
        },
        'C',
        '3568 md. 29 ve TESMER düzenlemeleri: meslek örgütünün amaçları arasında mesleğin gelişmesini sağlamak ve mesleki standartları yükseltmek vardır; sürekli mesleki eğitim bu işlevin parçasıdır. Meslek ahlak kurallarının mesleki yeterlik ilkesi de meslek mensubuna bilgisini güncel tutma yükümlülüğü yükler.',
    ),
    # düzey 2
    '0049': patch(
        'Bir oda genel kurulunun görevleri belirlenmektedir. Buna göre aşağıdakilerden hangisi genel kurulun görevlerinden biri değildir?',
        {
            'A': 'Yönetim kurulunun çalışma raporunu inceleyerek ibra etmek',
            'B': 'Oda organlarını seçmek',
            'C': 'Bütçeyi ve kesin hesabı görüşerek karara bağlamak',
            'D': 'Meslek mensupları hakkında disiplin cezası vermek',
            'E': 'Odanın taşınmaz alım satımı konusunda yönetim kuruluna yetki vermek',
        },
        'D',
        '3568 md. 19: genel kurul organları seçer, bütçe ve kesin hesabı karara bağlar, yönetim kurulunu ibra eder ve taşınmaz işlemleri gibi konularda yetki verir. DİSİPLİN CEZASI verme yetkisi ise md. 21 uyarınca DİSİPLİN KURULUNA aittir.',
    ),
    # düzey 3
    '0050': patch(
        'Meslek örgütü ve disiplin ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Disiplin cezaları uyarma, kınama, geçici olarak faaliyetten alıkoyma, yeminli sıfatını kaldırma ve meslekten çıkarmadır. II. Mecburi meslek kararları meslek mensuplarını bağlar. III. Meslek kuruluşları kuruluş amaçları dışında faaliyet gösteremez.',
        {
            'A': 'I, II ve III',
            'B': 'II ve III',
            'C': 'Yalnız I',
            'D': 'I ve III',
            'E': 'I ve II',
        },
        'A',
        'Üç ifade de doğrudur. 3568 md. 48 disiplin cezalarını sayar, md. 33 mecburi meslek kararlarının bağlayıcılığını düzenler, Anayasa md. 135 ise meslek kuruluşlarının kuruluş amaçları dışında faaliyet gösteremeyeceğini öngörür.',
    ),
    # düzey 2
    '0051': patch(
        'Serbest muhasebeci mali müşavirler odası ile yeminli mali müşavirler odasının örgütlenmesi tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Serbest muhasebeci mali müşavirler odası, yeminli mali müşavirler odasının şubesidir',
            'B': 'İki unvan tek bir oda çatısı altında birlikte örgütlenir',
            'C': 'İki unvan ayrı odalarda örgütlenir; her iki oda türü de aynı Birliğe üyedir',
            'D': 'Yeminli mali müşavirler için ayrı bir üst birlik kurulmuştur',
            'E': 'Yeminli mali müşavirler odaya kaydolmaksızın faaliyet gösterebilir',
        },
        'C',
        "3568 md. 14 ve 29: serbest muhasebeci mali müşavirler odaları ile yeminli mali müşavirler odaları AYRI AYRI kurulur; ancak her iki oda türü de tek bir üst kuruluş olan TÜRMOB'a üyedir. Odalar arasında ast-üst ilişkisi yoktur ve her iki unvan için de odaya kayıt zorunludur.",
    ),
    # düzey 2
    '0052': patch(
        'Bir meslek mensubu, odanın mesleki denetim kapsamında istediği bilgi ve belgeleri, müşteri sırrı gerekçesiyle vermeyi reddetmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Odaya bilgi ve belge verme yükümlülüğü yalnızca hakkında disiplin soruşturması açılmışsa doğar',
            'B': 'Bilgi verme yükümlülüğü yalnızca yeminli mali müşavirler için geçerlidir',
            'C': 'Meslek mensubu müşteri sırrı gerekçesiyle hiçbir bilgi vermeyebilir',
            'D': 'Meslek mensubu bilgi ve belge vermekle yükümlüdür; buna karşılık oda bakımından herhangi bir gizlilik yükümlülüğü öngörülmemiştir',
            'E': 'Meslek mensubu odaya karşı bilgi ve belge verme yükümlülüğü altındadır; oda da bu bilgilerin gizliliğini korumakla yükümlüdür',
        },
        'E',
        "Meslek mevzuatı: meslek mensubu, mesleki faaliyetiyle ilgili olarak odanın istediği bilgi ve belgeleri VERMEKLE yükümlüdür; bu yükümlülük mesleki denetimin işlemesi için gereklidir. Odanın kendisi de bu bilgiler bakımından gizlilik yükümlülüğü altındadır; 3568 md. 43'teki sır saklama meslek kuruluşu içinde de geçerlidir.",
    ),
    # düzey 2
    '0053': patch(
        'Meslek örgütünün siyasi ve mesleki tarafsızlığı tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek kuruluşları kuruluş amaçları dışında faaliyet gösteremez ve siyasi tarafsızlığını korur',
            'B': 'Siyasi tarafsızlık yükümlülüğü yalnızca meslek mensuplarını bağlar; meslek kuruluşunun kendisini bağlamaz',
            'C': 'Meslek kuruluşları siyasi parti faaliyeti yürütebilir ve seçim çalışması yapabilir',
            'D': 'Meslek kuruluşları kuruluş amaçları dışında serbestçe faaliyet gösterebilir',
            'E': 'Meslek kuruluşları üyelerinin oy tercihini belirleme yetkisine sahiptir',
        },
        'A',
        'Anayasa md. 135 ve 3568: kamu kurumu niteliği taşıyan meslek kuruluşları KURULUŞ AMAÇLARI DIŞINDA faaliyet gösteremez; siyasi tarafsızlıklarını korumakla yükümlüdür. Yükümlülük kuruluşun kendisini bağlar ve üyelerin siyasi tercihine müdahale yetkisi vermez.',
    ),
    # düzey 3
    '0054': patch(
        'Meslekten çıkarma cezası kesinleşen bir meslek mensubu, bir süre sonra yeniden ruhsat almak için başvurmayı düşünmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslekten çıkarma, disiplin cezalarının en ağırıdır',
            'B': 'Meslekten çıkarma cezası alan meslek mensubu, ceza tarihinden bir yıl sonra yeniden ruhsat almaya hak kazanır',
            'C': 'Ceza kesinleşene kadar meslek mensubunun itiraz hakkı bulunur',
            'D': 'Meslekten çıkarma cezasında meslek mensubunun ruhsatnamesi geri alınır ve odaya olan kaydı silinir',
            'E': 'Kesinleşen disiplin cezasına karşı idari yargı yolu açıktır',
        },
        'B',
        '3568 md. 48: meslekten çıkarma, ruhsatnamenin geri alınarak bir daha mesleğin icrasına izin verilmemesidir; kanun otomatik bir yeniden kazanım süresi öngörmez. Ceza kesinleşmeden önce itiraz yolu, kesinleştikten sonra ise idari yargı yolu açıktır.',
    ),
    # düzey 2
    '0055': patch(
        'Meslek örgütü ve disiplin bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek kuruluşlarının organları seçimle göreve gelir',
            'B': 'Mecburi meslek kararları meslek mensuplarını bağlar',
            'C': 'Meslek kuruluşlarının işlemleri idari yargı denetimine tabidir',
            'D': 'Meslek kuruluşları, kuruluş amaçları dışında da serbestçe faaliyet gösterebilir',
            'E': 'Odalar ve Birlik, tüzel kişiliği bulunan ve kamu kurumu niteliği taşıyan meslek kuruluşlarıdır',
        },
        'D',
        'Anayasa md. 135: kamu kurumu niteliği taşıyan meslek kuruluşları KURULUŞ AMAÇLARI DIŞINDA FAALİYET GÖSTEREMEZ. Diğer seçenekler doğrudur: kuruluş niteliği (3568 md. 14, 29), organların seçimle oluşması (md. 18-22), mecburi meslek kararlarının bağlayıcılığı (md. 33) ve idari yargı denetimi (Anayasa md. 125).',
    ),
    # düzey 2
    '0056': patch(
        'Bir meslek mensubu, odaya olan aidat borcunu ödememiş ve genel kurula katılıp oy kullanmak istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Aidat borcu bulunan meslek mensubunun ruhsatı kendiliğinden düşer',
            'B': 'Genel kurula katılma ve oy kullanma hakkı, oda yükümlülüklerinin yerine getirilmesine bağlanabilir',
            'C': 'Oy hakkı yalnızca yeminli mali müşavirlere tanınmıştır',
            'D': 'Aidat borcu bulunsa dahi meslek mensubunun genel kurulda oy kullanma hakkı hiçbir koşula bağlanamaz',
            'E': 'Genel kurula katılım yalnızca oda yönetim kurulu üyelerine açıktır',
        },
        'B',
        '3568 md. 19 ve ilgili yönetmelikler: genel kurula katılma ve oy kullanma hakkı odaya kayıtlı meslek mensuplarına aittir; ancak aidat gibi oda yükümlülüklerinin yerine getirilmesi koşulu getirilebilir. Aidat borcu ruhsatı kendiliğinden düşürmez; ödenmemesi disiplin ve takip sonuçları doğurur.',
    ),
    # düzey 2
    '0057': patch(
        'Disiplin cezalarında zamanaşımı tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Disiplin hukukunda zamanaşımı öngörülmemiş olup fiil, işlendiği tarihten ne kadar süre geçmiş olursa olsun soruşturulabilir',
            'B': 'Zamanaşımı süreleri yalnızca meslekten çıkarma cezası bakımından işler',
            'C': 'Zamanaşımı süresi ceza yargılamasındaki sürelerle her zaman aynıdır',
            'D': 'Zamanaşımı, cezanın kesinleşmesinden sonra işlemeye başlar',
            'E': 'Disiplin cezasını gerektiren fiiller bakımından zamanaşımı süreleri öngörülmüştür; süre geçtikten sonra soruşturma yapılamaz',
        },
        'E',
        'Disiplin Yönetmeliği, disiplin cezasını gerektiren fiiller bakımından soruşturma ve ceza zamanaşımı süreleri öngörür; bu süreler geçtikten sonra soruşturma açılamaz ve ceza verilemez. Süreler fiilin işlenmesinden ya da öğrenilmesinden itibaren işler; cezanın kesinleşmesinden sonra değil. Ceza yargılamasındaki zamanaşımı ise ayrı bir rejimdir.',
    ),
    # düzey 1
    '0058': patch(
        'Meslek örgütünün, meslekle ilgili mevzuatın hazırlanmasına katkı sağlaması tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek örgütü, meslekle ilgili mevzuat çalışmalarında görüş bildirebilir ve öneri sunabilir',
            'B': 'Meslek örgütünün mevzuat hazırlık süreçlerine katkı sağlama imkânı bulunmaz',
            'C': 'Mevzuat çalışmalarında görüş bildirme yetkisi yalnızca odalara ait olup Birlik bu yetkiyi kullanamaz',
            'D': 'Meslek örgütü yalnızca yürürlükteki mevzuatı uygular; görüş bildiremez',
            'E': 'Meslek örgütü meslekle ilgili kanunları doğrudan çıkarma yetkisine sahiptir',
        },
        'A',
        '3568 md. 29 ve 32: Birlik, mesleğin gelişmesi için mevzuat çalışmalarında görüş bildirir, öneri sunar ve ilgili kurumlarla iş birliği yapar. Kanun çıkarma yetkisi yasama organına aittir; meslek kuruluşu yalnızca katkı sağlar.',
    ),
    # düzey 3
    '0059': patch(
        'Bir meslek mensubu, odasının usulüne uygun aldığı ve kendisini bağlayan bir mecburi meslek kararının hukuka aykırı olduğunu düşünmekte; bu nedenle karara uymayarak sonucu beklemeyi planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu karara uymayarak hukuka aykırılığı ileri sürebilir; bu durumda kendisine herhangi bir yaptırım uygulanmaz',
            'B': 'Meslek mensubu karara uymamakla birlikte disiplin sorumluluğundan kurtulur',
            'C': 'Meslek mensubu karara uymakla yükümlüdür; hukuka aykırılık iddiasını idari yargıda iptal davasıyla ileri sürebilir',
            'D': 'Meslek mensubu karara ancak oda genel kurulunda itiraz edebilir; yargı yolu kapalıdır',
            'E': 'Mecburi meslek kararları yargı denetimine tabi değildir',
        },
        'C',
        'Mecburi meslek kararları bağlayıcı düzenleyici işlemlerdir; yürürlükte olduğu sürece meslek mensubunu bağlar ve uymamak disiplin sorumluluğu doğurur. Hukuka aykırılık iddiası, Anayasa md. 125 ve 2577 sayılı İYUK uyarınca İDARİ YARGIDA iptal davası açılarak ileri sürülür; karara tek taraflı uymamak meşru bir yol değildir.',
    ),
    # düzey 3
    '0060': patch(
        'Meslek örgütü ve disiplin ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Disiplin cezalarının en ağırı meslekten çıkarmadır. II. Yeminli sıfatının kaldırılması cezası tüm meslek mensuplarına uygulanabilir. III. Mecburi meslek kararları bağlayıcı olmayıp tavsiye değeri taşır. IV. Kesinleşen disiplin cezasına karşı idari yargı yolu açıktır.',
        {
            'A': 'I ve IV',
            'B': 'III ve IV',
            'C': 'Yalnız II',
            'D': 'I, II ve III',
            'E': 'II ve III',
        },
        'E',
        'II YANLIŞ: yeminli sıfatının kaldırılması niteliği gereği yalnızca YEMİNLİ MALİ MÜŞAVİRLERE uygulanabilir. III YANLIŞ: 3568 md. 33 uyarınca mecburi meslek kararları bağlayıcıdır ve uymamak disiplin sorumluluğu doğurur. I (md. 48) ve IV (İYUK) doğrudur.',
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
    print(f"1 paket / {len(PATCHES)} soru (Meslek Orgutu ve Disiplin yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
