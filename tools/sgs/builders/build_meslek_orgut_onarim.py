#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Meslek Orgutu ve Disiplin — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Agustos yapisal kalibrasyonundaki olay tabanli 60 soru korunarak onarildi: genisletilmis ELEME_ISARETI olcutune gore 57 mutlak ifadeli sik ayni dogruluk degerini koruyacak bicimde yeniden yazildi; gerekce tasiyan 12 dogru sik kisaltildi. Kor ogrenci %33 -> %25.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 3568 sayili Kanun · Disiplin Yonetmeligi · Anayasa md. 125, 129, 135 · 2577 sayili IYUK
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/meslek_hukuku/meslek_orgutu_disiplin.json"
STYLE_REF = 'SGS Meslek Hukuku (gercek sinav yapisina kalibre: olay + kural uygulamasi)'
ONEK = "mh-orgut-gen-"


def patch(stem, options, answer, solution, ref='3568 sayili SMMM ve YMM Kanunu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Bir meslek mensubu, bağlı olduğu odanın bir devlet dairesi olduğunu ve kararlarına karşı yalnızca üst amire başvurulabileceğini ileri sürmektedir. Buna göre meslek örgütünün hukuki niteliği bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Odalar ve Birlik tüzel kişiliğe sahiptir',
            'B': 'Odalar ve Birlik, merkezî idarenin hiyerarşisi içinde yer alan devlet daireleridir',
            'C': 'Odalar ve Birlik, tüzel kişiliğe sahip ve kamu kurumu niteliği taşıyan meslek kuruluşlarıdır',
            'D': 'Meslek kuruluşlarının tesis ettiği işlemler idari işlem sayılır',
            'E': 'Kuruluş ve işleyişleri kanunla düzenlenmiştir',
        },
        'B',
        '3568 md. 14 ve 28: odalar ile Türkiye Serbest Muhasebeci Mali Müşavirler ve Yeminli Mali Müşavirler Odaları Birliği, tüzel kişiliğe sahip KAMU KURUMU NİTELİĞİNDE MESLEK KURULUŞLARIDIR (Anayasa md. 135). Merkezî idarenin hiyerarşik alt birimi değildirler; idari ve mali özerklikleri vardır. İşlemleri idari işlem olduğundan idari yargı denetimine tabidir.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0002': patch(
        'Bir oda genel kurulu toplanmış; yönetim kurulunun bu kararı değiştirebileceği ileri sürülmüştür. Buna göre oda genel kurulu bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yönetim kurulu, genel kurulun aldığı kararları değiştirebilir',
            'B': 'Genel kurul odanın en yetkili karar organıdır',
            'C': 'Genel kurul odanın bütçesini görüşüp karara bağlar',
            'D': 'Genel kurul kesin hesabı görüşür',
            'E': 'Genel kurul yönetim kurulunu ibra eder',
        },
        'A',
        '3568 md. 18 ve 19: genel kurul odanın en yetkili karar organıdır; bütçeyi ve kesin hesabı görüşüp karara bağlar, yönetim kurulunu ibra eder. Yönetim kurulu genel kurulun icra organıdır ve onun kararlarını değiştiremez.',
    ),
    # düzey 1
    '0003': patch(
        'Bir odada meslek mensuplarına disiplin cezası verme görevini hangi organın taşıdığı belirlenmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Disiplin kurulu üyeleri Birlik yönetim kurulunca atanır ve oda genel kurulu tarafından seçilmez',
            'B': 'Disiplin kurulu odanın en yetkili karar organıdır',
            'C': 'Disiplin cezası vermek disiplin kurulunun görevidir',
            'D': 'Disiplin kurulu odanın icra organı olup günlük işleri yürütür',
            'E': 'Disiplin kurulu odanın hesaplarını denetlemekle görevlidir',
        },
        'C',
        '3568 md. 17, 25 ve 26: disiplin kurulu, meslek mensupları hakkında disiplin kovuşturması yapmak ve ceza vermekle görevlidir. Tüm oda organları GENEL KURULCA seçilir; hesap denetimi denetleme kuruluna, icra ise yönetim kuruluna aittir.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 1
    '0004': patch(
        'Bir meslek mensubuna, görevinde ve davranışında kusurlu sayıldığının yazıyla bildirilmesine karar verilmiştir. Buna göre uygulanan disiplin cezası aşağıdakilerden hangisidir?',
        {
            'A': 'Geçici olarak mesleki faaliyetten alıkoyma',
            'B': 'Uyarma cezası',
            'C': 'Meslekten çıkarma',
            'D': 'Kınama cezası',
            'E': 'Yeminli sıfatını kaldırma',
        },
        'D',
        '3568 md. 48: KINAMA, meslek mensubuna görevinde ve davranışında KUSURLU sayıldığının yazı ile bildirilmesidir. Uyarma ise yalnızca daha dikkatli davranılması gerektiğinin bildirilmesi olup kusur tespiti içermez.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0005': patch(
        'Bir yeminli mali müşavir hakkında yeminli sıfatının kaldırılması cezası uygulanmıştır. Buna göre bu ceza bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ceza, yeminli mali müşavirlere uygulanabilen bir disiplin cezasıdır',
            'B': 'Ceza sonucunda YMM unvanı kaybedilir',
            'C': 'Cezayla birlikte tasdik yetkisi de sona erer',
            'D': "Ceza, 3568 sayılı Kanun'da sayılan disiplin cezalarındandır",
            'E': 'Ceza tasdik yetkisini belirli bir süre için durdurur',
        },
        'E',
        '3568 md. 48: yeminli sıfatının kaldırılması cezası, niteliği gereği yeminli mali müşavirlere uygulanabilir; meslek mensubu YMM unvanını ve buna bağlı tasdik yetkisini kalıcı olarak kaybeder. Belirli bir süre için faaliyeti durduran ceza ise geçici olarak meslekî faaliyetten alıkoymadır.',
    ),
    # düzey 3
    '0006': patch(
        'Oda disiplin kurulunca hakkında kınama cezası verilen bir meslek mensubu, karara karşı başvuru yolunu araştırmaktadır. Meslek mensubu doğrudan idare mahkemesine gitmeyi düşünmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Önce Birlik disiplin kuruluna itiraz edilir, sonra idari yargıya gidilir',
            'B': 'Meslek mensubu itirazını oda genel kuruluna yapar',
            'C': 'Meslek mensubu doğrudan Hazine ve Maliye Bakanlığına itiraz eder',
            'D': 'Oda disiplin kurulu kararları kesin olup itiraz yolu kapalıdır',
            'E': 'Meslek mensubu doğrudan idare mahkemesinde iptal davası açar; meslek örgütü içinde bir itiraz yolu bulunmaz',
        },
        'A',
        '3568 md. 25: oda disiplin kurulu kararlarına karşı tebliğden itibaren otuz gün içinde BİRLİK DİSİPLİN KURULUNA itiraz edilir. Birlik Disiplin Kurulunun itirazı reddeden kararı Maliye Bakanlığının tasdiki ile kesinleşir (md. 38); kesinleşen disiplin cezası bir idari işlem olduğundan 2577 sayılı İYUK uyarınca İDARİ YARGIDA iptal davasına konu edilebilir.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0007': patch(
        "TÜRMOB'un organları belirlenmektedir. Buna göre aşağıdakilerden hangisi Birliğin organlarından biri değildir?",
        {
            'A': 'Birlik yönetim kurulu',
            'B': 'Birlik genel kurulu',
            'C': 'Birlik disiplin kurulu',
            'D': 'Oda genel kurulu',
            'E': 'Birlik denetleme kurulu',
        },
        'D',
        "3568 md. 31: Birliğin organları BİRLİK GENEL KURULU, BİRLİK YÖNETİM KURULU, BİRLİK DİSİPLİN KURULU ve BİRLİK DENETLEME KURULU'dur. Oda genel kurulu ise ODA düzeyindeki bir organdır ve Birliğin organı değildir.",
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0008': patch(
        'Bir meslek mensubunun disiplin soruşturmasına konu olabilecek fiilleri belirlenmektedir. Buna göre aşağıdakilerden hangisi disiplin soruşturmasına konu olmaz?',
        {
            'A': 'Meslek mensubunun meslek sırlarını ifşa etmesi',
            'B': 'Meslek mensubunun bir anonim şirkete sermaye ortağı olması',
            'C': 'Meslek mensubunun asgari ücret tarifesinin altında iş kabul etmesi',
            'D': 'Meslek mensubunun bir meslektaşına karşı haksız rekabette bulunması',
            'E': 'Meslek mensubunun iş elde etmek amacıyla reklam yapması',
        },
        'B',
        "Çalışma Usul ve Esasları Yönetmeliği md. 43 limited ve anonim şirketlere ORTAK olmayı yasaklamaz; bu tek başına disiplin suçu değildir (ortağı olunan firmanın işlerine bakma yasağı ise yalnız yeminli mali müşavirler içindir). Diğer seçenekler md. 46, 45, 43 ve Haksız Rekabet Yönetmeliğine aykırılık oluşturur ve md. 48 uyarınca disiplin cezası gerektirir.",
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0009': patch(
        'Meslek mensuplarının odaya karşı mali yükümlülükleri belirlenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensupları odaya yıllık aidat öder',
            'B': 'Aidatların süresinde ödenmemesi takip ve disiplin sorumluluğu doğurabilir',
            'C': 'Aidat tutarları ilgili mevzuat çerçevesinde belirlenir',
            'D': 'Meslek mensupları odaya giriş aidatı öder',
            'E': 'Meslek mensuplarının odaya karşı herhangi bir mali yükümlülüğü bulunmaz',
        },
        'E',
        '3568 md. 16 ve 19/h: meslek mensupları odaya GİRİŞ ÜCRETİ ve YILLIK AİDAT ödemekle yükümlüdür. Aidat, odanın temel gelir kaynaklarındandır; ödenmemesi takip ve disiplin sonuçları doğurur.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0010': patch(
        'Meslek mensubuna verilen disiplin cezalarının sonuçları değerlendirilmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Geçici olarak mesleki faaliyetten alıkoyma cezası süresince mesleki faaliyette bulunulamaz',
            'B': 'Disiplin cezaları tekerrürde ağırlaştırıcı olarak dikkate alınır',
            'C': 'Disiplin cezaları odanın iç işidir; meslek mensubunun sicilinde yer almaz',
            'D': 'Meslekten çıkarma cezasında ruhsatname geri alınır',
            'E': 'Kesinleşen disiplin cezaları meslek mensubunun sicilinde yer alır',
        },
        'C',
        "Disiplin Yönetmeliği: kesinleşen disiplin cezaları meslek mensubunun SİCİLİNE İŞLENİR ve tekerrürde ağırlaştırıcı sebep olarak dikkate alınır. Ceza türlerine bağlı sonuçlar (faaliyet yasağı, ruhsatın geri alınması) md. 48'de düzenlenmiştir.",
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 3
    '0011': patch(
        'Bir meslek mensubu, defterlerini tuttuğu bir müşterisine ait ticari sırları rakip bir firmaya para karşılığında aktarmıştır. Fiil hem müşteriye zarar vermiş hem de kamuya yansımıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Müşteri şikâyet etmezse sorumluluk doğmaz',
            'B': 'Fiil disiplin sorumluluğu doğurur, mali sorumluluk doğurmaz',
            'C': 'Fiil cezai sorumluluk doğurur; disiplin süreci yürütülemez',
            'D': 'Disiplin süreci, aynı fiile ilişkin ceza yargılaması kesinleşmeden başlatılamaz; mahkeme kararının sonucu beklenir',
            'E': 'Fiil disiplin, mali ve cezai sorumluluğu birlikte doğurabilir',
        },
        'E',
        '3568 md. 43 sır saklama yükümlülüğünü, md. 48 disiplin sorumluluğunu düzenler; fiil ayrıca TBK md. 49 vd. uyarınca tazminat ve koşulları varsa cezai sorumluluk doğurur. Üç rejim birbirinden BAĞIMSIZDIR; disiplin soruşturması resen de açılabilir ve ceza yargılamasının sonucunu beklemek zorunda değildir.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0012': patch(
        'Kesinleşen bir disiplin cezasına karşı hangi yargı yoluna başvurulacağı tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Dava adliye mahkemelerinde, genel görevli asliye hukuk mahkemesinde iptal talebiyle açılır',
            'B': 'Meslek kuruluşunun işlemi idari işlem olduğundan iptal davası idari yargıda açılır',
            'C': "Dava Danıştay'da ilk derece mahkemesi olarak açılır",
            'D': 'Dava iş mahkemesinde açılır',
            'E': 'Kesinleşen disiplin cezalarına karşı yargı yolu kapalıdır',
        },
        'B',
        'Odalar ve Birlik kamu kurumu niteliği taşıyan meslek kuruluşu olduğundan işlemleri İDARİ İŞLEMDİR (Anayasa md. 135). Kesinleşen disiplin cezasına karşı 2577 sayılı İYUK uyarınca İDARE MAHKEMESİNDE iptal davası açılır. Anayasa md. 125 uyarınca idarenin her türlü işlem ve eylemine karşı yargı yolu açıktır.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 3
    '0013': patch(
        'Bir meslek mensubu, daha önce kınama cezası aldığı bir kural ihlalini tekrar işlemiştir. Buna göre tekerrür bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tekerrür hâlinde ceza doğrudan meslekten çıkarmaya dönüşür',
            'B': 'Aynı ihlalin tekrarı bir derece ağır ceza uygulanmasına yol açabilir',
            'C': 'Tekerrür hâlinde önceki ceza ortadan kalkmaz',
            'D': 'Tekerrür kuralı serbest muhasebeci mali müşavirlere de uygulanır',
            'E': 'Önceki ceza, yeni fiilde ağırlaştırıcı olarak dikkate alınır',
        },
        'A',
        '3568 md. 48: üç yıllık bir dönem içinde iki veya daha fazla disiplin cezasını gerektiren davranışta bulunan meslek mensubuna her yeni fiili için bir öncekinden daha ağır ceza uygulanabilir; disiplin kurulları bir derece ağır ya da hafif ceza uygulanmasına karar verebilir. Tekerrür otomatik olarak en ağır cezayı doğurmaz ve unvana göre değişmez; önceki ceza ortadan kalkmaz, ağırlaştırıcı olarak dikkate alınır.',
    ),
    # düzey 1
    '0014': patch(
        "TESMER'in (Temel Eğitim ve Staj Merkezi) işlevi tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'TESMER, TÜRMOB bünyesinde kurulmuştur',
            'B': 'TESMER meslek stajına ilişkin faaliyetleri yürütür',
            'C': 'TESMER sınavlara hazırlık eğitimleri düzenler',
            'D': 'TESMER meslek mensuplarına disiplin cezası verir',
            'E': 'TESMER temel eğitim programları düzenler',
        },
        'D',
        'TESMER, TÜRMOB bünyesinde kurulmuş olup staj, temel eğitim, sınav hazırlığı ve mesleki eğitim faaliyetlerini yürütür. Disiplin cezası verme yetkisi oda disiplin kurullarına ve itiraz merci olarak Birlik disiplin kuruluna aittir.',
    ),
    # düzey 2
    '0015': patch(
        'Hakkında disiplin soruşturması yürütülen bir meslek mensubunun usul güvenceleri belirlenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubuna savunma hakkı tanınması, cezanın ağırlığına göre disiplin kurulunun takdirindedir',
            'B': 'Meslek mensubuna savunma hakkı tanınmadan hakkında herhangi bir disiplin cezası verilemez',
            'C': 'Meslek mensubu savunmasını yazılı olarak sunabilir',
            'D': 'Meslek mensubu isnat edilen fiilden haberdar edilmelidir',
            'E': 'Verilen karara karşı itiraz yolu açıktır',
        },
        'A',
        "Disiplin hukukunun temel güvencesi SAVUNMA HAKKIDIR ve Anayasa md. 129 uyarınca 'savunma hakkı tanınmadıkça disiplin cezası verilemez'. Bu güvence cezanın ağırlığına ya da kurulun takdirine bağlı değildir; isnadın bildirilmesi ve itiraz yolu da sürecin parçasıdır.",
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0016': patch(
        'Odaların gelir kaynakları belirlenmektedir. Buna göre aşağıdakilerden hangisi bir oda geliri sayılmaz?',
        {
            'A': 'Meslek mensuplarının müşterilerinden tahsil ettiği hizmet ücretlerinin tamamı',
            'B': 'Odanın düzenlediği eğitim, seminer ve yayın faaliyetlerinden sağlanan gelirler',
            'C': 'Bağış, yardım ve faiz gelirleri',
            'D': 'Meslek mensuplarının ödediği yıllık aidat',
            'E': 'Meslek mensuplarının odaya kayıtta ödediği giriş aidatı',
        },
        'A',
        '3568 md. 16: oda gelirleri giriş ücreti, yıllık üye aidatları, yardım ve bağışlar ile mesleki eğitime yönelik kurs ve staj ücretleri ve diğer çeşitli gelirlerden oluşur. Meslek mensubunun müşterisinden aldığı HİZMET ÜCRETİ kendi mesleki kazancıdır; odanın geliri değildir.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 3
    '0017': patch(
        'Meslek örgütü ve disiplin ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Disiplin cezaları uyarma, kınama, geçici olarak faaliyetten alıkoyma, yeminli sıfatını kaldırma ve meslekten çıkarmadır. II. Mecburi meslek kararları meslek mensuplarını bağlar. III. Meslek kuruluşları kuruluş amaçları dışında faaliyet gösteremez.',
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'I ve II',
        },
        'C',
        'Üç ifade de doğrudur. 3568 md. 48 disiplin cezalarını sayar, md. 33 mecburi meslek kararlarının bağlayıcılığını düzenler, Anayasa md. 135 ise meslek kuruluşlarının kuruluş amaçları dışında faaliyet gösteremeyeceğini öngörür.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0018': patch(
        'Bir meslek mensubu, odanın mesleki denetim kapsamında istediği bilgi ve belgeleri, müşteri sırrı gerekçesiyle vermeyi reddetmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu odanın istediği bilgi ve belgeleri vermekle yükümlüdür',
            'B': 'Meslek mensubu müşteri sırrı gerekçesiyle odaya bilgi vermeyi reddedebilir',
            'C': 'Oda, edindiği bilgilerin gizliliğini korumakla yükümlüdür',
            'D': 'Yükümlülük mesleki denetimin işlemesi için öngörülmüştür',
            'E': 'Yükümlülük, disiplin soruşturması açılmamış olsa da vardır',
        },
        'B',
        'Meslek mevzuatı: meslek mensubu, mesleki faaliyetiyle ilgili olarak odanın istediği bilgi ve belgeleri vermekle yükümlüdür; bu yükümlülük mesleki denetimin işlemesi için gereklidir ve bir disiplin soruşturmasına bağlı değildir. Oda da bu bilgilerin gizliliğini korur; bu nedenle müşteri sırrı ret gerekçesi olamaz.',
    ),
    # düzey 2
    '0019': patch(
        'Meslek örgütü ve disiplin bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Mecburi meslek kararları meslek mensuplarını bağlar',
            'B': 'Meslek kuruluşlarının organları seçimle göreve gelir',
            'C': 'Odalar ve Birlik, tüzel kişiliği bulunan ve kamu kurumu niteliği taşıyan meslek kuruluşlarıdır',
            'D': 'Meslek kuruluşlarının işlemleri idari yargı denetimine tabidir',
            'E': 'Meslek kuruluşları, kuruluş amaçları dışında da faaliyet gösterebilir',
        },
        'E',
        'Anayasa md. 135: kamu kurumu niteliği taşıyan meslek kuruluşları KURULUŞ AMAÇLARI DIŞINDA FAALİYET GÖSTEREMEZ. Diğer seçenekler doğrudur: kuruluş niteliği (3568 md. 14, 28), organların seçimle oluşması (md. 19, 21, 25 ve 27), mecburi meslek kararlarının bağlayıcılığı (md. 33) ve idari yargı denetimi (Anayasa md. 125).',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 1
    '0020': patch(
        'Meslek örgütünün, meslekle ilgili mevzuatın hazırlanmasına katkı sağlaması tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Birlik, mevzuat çalışmalarında görüş bildirebilir',
            'B': 'Meslek örgütü mevzuat önerisi sunabilir',
            'C': 'Kanun çıkarma yetkisi yasama organına aittir',
            'D': 'Meslek örgütü meslekle ilgili kanunları doğrudan çıkarabilir',
            'E': 'Meslek örgütü ilgili kurumlarla iş birliği yapabilir',
        },
        'D',
        '3568 md. 29: Birlik, mesleğin gelişmesi için mevzuat çalışmalarında görüş bildirir, öneri sunar ve ilgili kurumlarla iş birliği yapar. Kanun çıkarma yetkisi yasama organına aittir; meslek kuruluşu yalnızca katkı sağlar.',
    ),
    # düzey 2
    '0021': patch(
        'Ruhsatını yeni alan bir meslek mensubu, mesleki faaliyete başlamadan önce odaya kaydolmanın isteğe bağlı olduğunu düşünmektedir. Buna göre odaya kayıt bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu bölgesindeki odaya kaydolmalıdır',
            'B': 'Kayıt yükümlülüğü yeminli mali müşavirleri de kapsar',
            'C': 'Meslek mensubu oda seçiminde serbest değildir',
            'D': 'Kayıt, mesleki faaliyete başlamadan önce yapılır',
            'E': 'Ruhsat tek başına faaliyet için yeterlidir; kayıt isteğe bağlıdır',
        },
        'E',
        '3568 md. 15: odalara üye olmayan meslek mensupları mesleki faaliyette bulunamaz; meslek mensupları, mesleki faaliyette bulunabilmek için bölgesi içinde bulundukları odaya kaydolmak zorundadır. Kayıt isteğe bağlı değildir, faaliyete başlamadan önce yapılır ve unvana göre değişmez; meslek mensubu işyerinin bulunduğu bölgenin odasına kaydolur.',
    ),
    # düzey 1
    '0022': patch(
        'Bir odada, genel kurul kararlarının uygulanması ve günlük işlerin yürütülmesi görevini hangi organın taşıdığı belirlenmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yönetim kurulu odanın disiplin cezası veren organıdır',
            'B': 'Yönetim kurulu Hazine ve Maliye Bakanlığınca atanır',
            'C': 'Yönetim kurulu, genel kurul kararlarını uygulayan ve odayı temsil eden icra organıdır',
            'D': 'Yönetim kurulu odanın hesaplarını denetleyen organdır',
            'E': 'Yönetim kurulu odanın en yetkili karar organı olup genel kurulun kararlarını değiştirebilir',
        },
        'C',
        '3568 md. 17, 21 ve 23: yönetim kurulu, genel kurulca seçilen ve odanın işlerini yürüten İCRA organıdır; odayı temsil eder ve genel kurul kararlarını uygular. Karar organı genel kurul, ceza organı disiplin kurulu, denetim organı ise denetleme kuruludur.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0023': patch(
        'Mesleğin ve meslek örgütünün genel gözetim ve denetiminden sorumlu idare belirlenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek örgütü üzerinde genel gözetim ve denetim yetkisi Kamu Gözetimi Kurumuna aittir',
            'B': 'Meslek kuruluşlarının işlemleri idari yargı denetimine tabidir',
            'C': 'Gözetim yetkisi, meslek kuruluşunun idari özerkliğini ortadan kaldırmaz',
            'D': 'Mesleğin ve meslek örgütünün genel gözetim ve denetimi Hazine ve Maliye Bakanlığına aittir',
            'E': 'Bakanlık, meslek örgütünün organlarının yerine geçerek karar alamaz',
        },
        'A',
        '3568 md. 41: mesleğin ve meslek örgütünün genel gözetim ve denetimi HAZİNE VE MALİYE BAKANLIĞINCA yürütülür. Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu ise BAĞIMSIZ DENETİM alanını düzenler; 3568 meslek örgütü üzerinde genel gözetim yetkisi yoktur. Gözetim yetkisi vesayet niteliğindedir ve organların yerine geçmeye izin vermez.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0024': patch(
        'Bir meslek mensubuna geçici olarak mesleki faaliyetten alıkoyma cezası verilmiştir. Meslek mensubu, ceza süresince unvanını kullanmaya ve ruhsatını elinde tutmaya devam edeceğini düşünmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ceza, meslek mensubunun ruhsatının kalıcı olarak geri alınması sonucunu doğurur',
            'B': 'Ceza süresince meslek mensubu mevcut faaliyetini sürdürebilir; yeni iş kabul etmesi yasaktır',
            'C': 'Ceza yeminli mali müşavirlere özgü bir yaptırımdır',
            'D': 'Ceza süresince meslek mensubu danışmanlık işlerini yürütebilir',
            'E': 'Ceza süresince mesleki faaliyette bulunamaz ve unvan yetkilerini kullanamaz',
        },
        'E',
        '3568 md. 48: GEÇİCİ OLARAK MESLEKÎ FAALİYETTEN ALIKOYMA, mesleki sıfatı saklı kalmak koşuluyla belirli bir süre için meslekî faaliyetten alıkonulmadır. Ceza süresince meslek mensubu faaliyette bulunamaz ve yetkilerini kullanamaz; ancak ruhsatı kalıcı olarak geri alınmaz — bu sonuç MESLEKTEN ÇIKARMA cezasına özgüdür.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0025': patch(
        'Meslek örgütü ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Odalar ve TÜRMOB kamu kurumu niteliği taşıyan meslek kuruluşlarıdır. II. Meslek mensupları mesleki faaliyette bulunabilmek için odaya kaydolmak zorundadır. III. Odaların en yetkili karar organı yönetim kuruludur.',
        {
            'A': 'I ve III',
            'B': 'I, II ve III',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'D',
        'I doğrudur (3568 md. 14, 28; Anayasa md. 135). II doğrudur (md. 15). III YANLIŞTIR: odanın en yetkili karar organı GENEL KURULDUR; yönetim kurulu genel kurul kararlarını uygulayan icra organıdır (md. 18, 21 ve 23).',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0026': patch(
        'Meslek örgütünün temel amaçları belirlenmektedir. Buna göre aşağıdakilerden hangisi bu amaçlardan biri değildir?',
        {
            'A': 'Üyeleri adına müşterilerle ücret sözleşmesi imzalamak ve iş dağıtımı yapmak',
            'B': 'Meslek disiplinini ve ahlakını korumak',
            'C': 'Meslek mensuplarının hak ve menfaatlerini korumak ve temsil etmek',
            'D': 'Mesleğin gelişmesini sağlamak ve mesleki standartları yükseltmek',
            'E': 'Meslek mensuplarının birbirleriyle ve iş sahipleriyle ilişkilerinde dürüstlüğü ve güveni sağlamak',
        },
        'A',
        '3568 md. 14 ve 29: meslek kuruluşlarının amaçları mesleğin gelişmesini sağlamak, meslek mensupları arasında ve iş sahipleriyle ilişkilerde dürüstlük ve güveni tesis etmek, meslek disiplinini ve ahlakını korumaktır. Üyeler adına iş almak ya da iş dağıtmak meslek kuruluşunun görevi değildir; bu meslek mensubunun kendi faaliyetidir.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 3
    '0027': patch(
        'Bir disiplin dosyasında, verilebilecek cezaların ağırlığına göre sıralanması istenmiştir. Buna göre en hafiften en ağıra doğru doğru sıralama aşağıdakilerden hangisidir?',
        {
            'A': 'Kınama – uyarma – geçici olarak mesleki faaliyetten alıkoyma – meslekten çıkarma – yeminli sıfatını kaldırma',
            'B': 'Uyarma – geçici olarak mesleki faaliyetten alıkoyma – kınama – meslekten çıkarma – yeminli sıfatını kaldırma',
            'C': 'Geçici olarak mesleki faaliyetten alıkoyma – uyarma – kınama – yeminli sıfatını kaldırma – meslekten çıkarma',
            'D': 'Uyarma – kınama – meslekten çıkarma – geçici olarak mesleki faaliyetten alıkoyma – yeminli sıfatını kaldırma',
            'E': 'Uyarma – kınama – geçici olarak mesleki faaliyetten alıkoyma – yeminli sıfatını kaldırma – meslekten çıkarma',
        },
        'E',
        "3568 md. 48 cezaları hafiften ağıra şöyle sıralar: uyarma (dikkat çekme), kınama (kusurun bildirilmesi), geçici olarak meslekî faaliyetten alıkoyma (belirli süre faaliyet yasağı), yeminli sıfatının kaldırılması (YMM'ye özgü) ve meslekten çıkarma (en ağır ceza; ruhsat geri alınır).",
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0028': patch(
        'Bir meslek mensubu hakkında yapılan şikâyet üzerine disiplin sürecinin nasıl başlayacağı tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubuna savunma hakkı tanınması gerekir',
            'B': 'Soruşturma şikâyet üzerine ya da resen başlatılabilir',
            'C': 'Soruşturma sonunda ceza verilmemesine de karar verilebilir',
            'D': 'Disiplin soruşturması şikâyet üzerine başlar; oda resen soruşturma açamaz',
            'E': 'Soruşturma sonucunda dosya, karar verilmek üzere disiplin kuruluna sevk edilebilir',
        },
        'D',
        '3568 ve Disiplin Yönetmeliği: disiplin soruşturması ilgililerin şikâyeti üzerine başlatılabileceği gibi oda yönetim kurulunca RESEN de başlatılabilir. Soruşturmada meslek mensubuna SAVUNMA HAKKI tanınması zorunludur; savunma alınmadan ceza verilemez.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 1
    '0029': patch(
        "TÜRMOB bünyesindeki Yüksek Danışma Kurulu'nun işlevi tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Kurul bir danışma organıdır',
            'B': 'Kurul mesleğe ilişkin konularda görüş ve öneri oluşturur',
            'C': 'Kurul Birliğin en yetkili karar organıdır',
            'D': 'Kurulun görüşleri bağlayıcı karar niteliği taşımaz',
            'E': 'Kurul TÜRMOB bünyesinde yer alır',
        },
        'C',
        'Yüksek Danışma Kurulu, mesleğe ve meslek örgütüne ilişkin konularda görüş ve öneri oluşturmakla görevli danışma organıdır; bağlayıcı karar almaz. Birliğin en yetkili karar organı Birlik Genel Kuruludur (md. 31-33).',
    ),
    # düzey 3
    '0030': patch(
        'Bir meslek mensubu, aynı fiil nedeniyle hem oda disiplin kurulunca cezalandırılmış hem de hakkında ceza yargılaması başlatılmıştır. Meslek mensubu, aynı fiilden iki kez cezalandırılamayacağını ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Disiplin cezası verilmişse ceza yargılaması yapılamaz',
            'B': 'Aynı fiile ilişkin ceza yargılaması başladığında verilmiş disiplin cezası ortadan kalkar',
            'C': 'Disiplin ve cezai sorumluluk ayrıdır; aynı fiil için ikisi birlikte uygulanabilir',
            'D': 'Disiplin cezası ancak mahkûmiyet kesinleştikten sonra verilebilir',
            'E': 'Meslek mensubu, iki süreçten hangisine tabi olacağını seçebilir',
        },
        'C',
        "Disiplin sorumluluğu ile cezai sorumluluk AYRI HUKUKİ REJİMLERDİR: biri meslek düzenini, diğeri kamu düzenini korur. Aynı fiil nedeniyle her ikisi birlikte uygulanabilir ve bu 'aynı fiilden iki kez cezalandırma' yasağını ihlal etmez. Meslek mensubunun seçim hakkı yoktur; disiplin süreci ceza yargılamasının sonucunu beklemek zorunda da değildir.",
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0031': patch(
        'Meslek örgütünün mesleki denetim işlevi tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Mesleki denetimde tespit edilen aykırılıklar disiplin sürecine konu olabilir',
            'B': 'Meslek mensubu, denetim kapsamında istenen bilgi ve belgeleri vermekle yükümlüdür',
            'C': 'Mesleki denetim, meslek mensuplarının mevzuata ve mesleki ilkelere uygun çalışıp çalışmadığını izlemeyi kapsar',
            'D': 'Mesleki denetim, meslek mensubunun müşterisinin vergi matrahını yeniden belirlemeyi kapsar',
            'E': 'Mesleki denetim, meslek kuruluşunun mesleki standartları koruma işlevinin parçasıdır',
        },
        'D',
        'Meslek örgütünün MESLEKİ DENETİMİ, meslek mensuplarının mevzuata ve mesleki ilkelere uygunluğunu izlemeye yöneliktir; aykırılıklar disiplin sürecine taşınır. Mükellefin VERGİ MATRAHINI belirlemek ise vergi idaresinin yetkisidir; meslek kuruluşunun görev alanında değildir.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 3
    '0032': patch(
        'Disiplin süreci ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. İlk derece disiplin cezasını oda disiplin kurulu verir. II. Savunma hakkı tanınmadan disiplin cezası verilebilir. III. Oda disiplin kurulu kararlarına karşı Birlik disiplin kuruluna itiraz edilir. IV. Aynı fiil nedeniyle disiplin ve cezai sorumluluk birlikte doğamaz.',
        {
            'A': 'II ve III',
            'B': 'II ve IV',
            'C': 'I ve III',
            'D': 'I, II ve IV',
            'E': 'Yalnız II',
        },
        'B',
        'II YANLIŞ: Anayasa md. 129 uyarınca savunma hakkı tanınmadıkça disiplin cezası verilemez. IV YANLIŞ: disiplin sorumluluğu ile cezai sorumluluk ayrı rejimler olup aynı fiil için birlikte doğabilir. I ve III doğrudur.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0033': patch(
        'Bir meslek mensubu, ilk kez ve hafif nitelikte bir kural ihlalinde bulunmuştur (şeklî bir eksiklik). Disiplin kurulu, doğrudan geçici olarak mesleki faaliyetten alıkoyma cezası vermeyi değerlendirmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Disiplin kurulu ceza türünü fiilin ağırlığına bakmaksızın belirler',
            'B': 'İlk kez işlenen ihlallerde ceza verilemez; disiplin cezası ikinci ihlalde gündeme gelir',
            'C': 'Hafif ihlallerde de en ağır cezanın verilmesi kanunen zorunludur',
            'D': 'Ceza türü meslek mensubunun kıdemine göre belirlenir',
            'E': 'Ceza fiilin ağırlığıyla orantılı olmalı; hafif ilk ihlalde uyarma veya kınama uygundur',
        },
        'E',
        'Disiplin hukukunda ÖLÇÜLÜLÜK ilkesi geçerlidir: verilecek ceza, fiilin ağırlığı, meslek mensubunun kusuru ve varsa tekerrür gibi ölçütlerle orantılı olmalıdır. İlk kez işlenen hafif nitelikli bir ihlalde uyarma veya kınama uygun düşer. Kurulun takdiri sınırsız değildir ve yargı denetimine tabidir.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0034': patch(
        'Meslek örgütü organlarının göreve gelme biçimi tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Oda ve Birlik organları, üyelerin katıldığı genel kurullarda seçimle göreve gelir',
            'B': 'Oda organları genel kurulda seçimle, Birlik organları ise atamayla göreve gelir',
            'C': 'Oda ve Birlik organları Hazine ve Maliye Bakanlığınca atanır',
            'D': 'Organlar seçim yapılmaksızın kıdem sırasına göre göreve gelir',
            'E': 'Organ üyeleri idare mahkemesi kararıyla belirlenir',
        },
        'A',
        "3568 md. 19, 21, 25, 27 ve 31-33: oda ve Birlik organları, ilgili GENEL KURULLARDA yapılan SEÇİMLE göreve gelir. Kamu kurumu niteliği taşıyan meslek kuruluşlarında organların seçimle oluşması Anayasa md. 135'in gereğidir; atama ya da kıdem esası uygulanmaz.",
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0035': patch(
        'İki meslek mensubu arasında iş devri ve ücret paylaşımı konusunda bir uyuşmazlık doğmuştur. Buna göre meslek örgütünün konumu bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek örgütü taraflar arasında uzlaşma sağlamaya çalışabilir',
            'B': 'Taraflar uyuşmazlık için yargı yoluna başvurabilir',
            'C': 'Meslek örgütünün kararı kesin olup yargı yolu kapalıdır',
            'D': 'Örgüt taraflardan biri lehine karar vermekle yükümlü değildir',
            'E': 'Örgüt uyuşmazlığın disiplin boyutunu değerlendirebilir',
        },
        'C',
        'Meslek örgütü, meslek mensupları arasındaki mesleki uyuşmazlıklarda uzlaşma sağlamaya çalışır ve gerektiğinde disiplin boyutunu değerlendirir. Bu arabuluculuk işlevi tarafların yargı yoluna başvurma hakkını ortadan kaldırmaz; örgüt taraf tutmakla yükümlü değildir.',
    ),
    # düzey 1
    '0036': patch(
        'Meslek örgütünün üyelerine yönelik sürekli mesleki eğitim düzenleme işlevi tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Eğitim yeminli mali müşavirlere yöneliktir',
            'B': 'Eğitim düzenleme yetkisi Hazine ve Maliye Bakanlığına aittir',
            'C': 'Meslek örgütü sürekli mesleki eğitim düzenler; meslek mensubu bilgi ve becerisini güncel tutmakla yükümlüdür',
            'D': 'Ruhsat alındıktan sonra meslek mensubunun eğitim yükümlülüğü sona erer',
            'E': 'Meslek örgütünün sürekli mesleki eğitim düzenleme işlevi bulunmaz; bu görev üniversitelere ve özel eğitim kurumlarına aittir',
        },
        'C',
        '3568 md. 29 ve TESMER düzenlemeleri: meslek örgütünün amaçları arasında mesleğin gelişmesini sağlamak ve mesleki standartları yükseltmek vardır; sürekli mesleki eğitim bu işlevin parçasıdır. Meslek ahlak kurallarının mesleki yeterlik ilkesi de meslek mensubuna bilgisini güncel tutma yükümlülüğü yükler.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0037': patch(
        'Bir oda genel kurulunun görevleri belirlenmektedir. Buna göre aşağıdakilerden hangisi genel kurulun görevlerinden biri değildir?',
        {
            'A': 'Meslek mensupları hakkında disiplin cezası vermek',
            'B': 'Oda organlarını seçmek',
            'C': 'Odanın taşınmaz alım satımı konusunda yönetim kuruluna yetki vermek',
            'D': 'Bütçeyi ve kesin hesabı görüşerek karara bağlamak',
            'E': 'Yönetim kurulunun çalışma raporunu inceleyerek ibra etmek',
        },
        'A',
        '3568 md. 19: genel kurul organları seçer, bütçe ve kesin hesabı karara bağlar, yönetim kurulunu ibra eder ve taşınmaz işlemleri gibi konularda yetki verir. DİSİPLİN CEZASI verme yetkisi ise md. 26 uyarınca DİSİPLİN KURULUNA aittir.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0038': patch(
        'Meslek örgütünün siyasi ve mesleki tarafsızlığı tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek kuruluşları kuruluş amaçları dışında faaliyet gösteremez',
            'B': 'Meslek kuruluşları siyasi tarafsızlığını korur',
            'C': 'Meslek kuruluşları siyasi parti faaliyeti yürütebilir',
            'D': 'Tarafsızlık yükümlülüğü kuruluşun kendisini bağlar',
            'E': 'Kuruluşlar üyelerinin oy tercihine müdahale edemez',
        },
        'C',
        'Anayasa md. 135 ve 3568: kamu kurumu niteliği taşıyan meslek kuruluşları kuruluş amaçları dışında faaliyet gösteremez ve siyasi tarafsızlıklarını korumakla yükümlüdür. Yükümlülük kuruluşun kendisini bağlar; üyelerin siyasi tercihine müdahale yetkisi vermez.',
    ),
    # düzey 2
    '0039': patch(
        'Disiplin cezalarında zamanaşımı tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Disiplin fiilleri için zamanaşımı süreleri öngörülmüştür',
            'B': 'Zamanaşımı, cezanın kesinleşmesinden sonra işlemeye başlar',
            'C': 'Süre geçtikten sonra soruşturma açılamaz',
            'D': 'Süre geçtikten sonra disiplin cezası verilemez',
            'E': 'Disiplin zamanaşımı ceza yargılamasındaki zamanaşımından ayrıdır',
        },
        'B',
        'Disiplin Yönetmeliği, disiplin cezasını gerektiren fiiller için soruşturma ve ceza zamanaşımı süreleri öngörür; bu süreler geçince soruşturma açılamaz ve ceza verilemez. Süreler fiilin işlenmesinden ya da öğrenilmesinden itibaren işler; cezanın kesinleşmesinden sonra değil. Ceza yargılamasındaki zamanaşımı ayrı bir rejimdir.',
    ),
    # düzey 3
    '0040': patch(
        'Bir meslek mensubu, odasının usulüne uygun aldığı ve kendisini bağlayan bir mecburi meslek kararının hukuka aykırı olduğunu düşünmekte; bu nedenle karara uymayarak sonucu beklemeyi planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu karara uymayarak hukuka aykırılığı ileri sürebilir; bu durumda kendisine herhangi bir yaptırım uygulanmaz',
            'B': 'Meslek mensubu karara uymamakla birlikte disiplin sorumluluğundan kurtulur',
            'C': 'Mecburi meslek kararları yargı denetimine tabi değildir',
            'D': 'Meslek mensubu karara ancak oda genel kurulunda itiraz edebilir; yargı yolu kapalıdır',
            'E': 'Meslek mensubu karara uymakla yükümlüdür; hukuka aykırılık iddiasını idari yargıda iptal davasıyla ileri sürebilir',
        },
        'E',
        'Mecburi meslek kararları bağlayıcı düzenleyici işlemlerdir; yürürlükte olduğu sürece meslek mensubunu bağlar ve uymamak disiplin sorumluluğu doğurur. Hukuka aykırılık iddiası, Anayasa md. 125 ve 2577 sayılı İYUK uyarınca İDARİ YARGIDA iptal davası açılarak ileri sürülür; karara tek taraflı uymamak meşru bir yol değildir.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 1
    '0041': patch(
        'Odaların bir araya gelerek oluşturduğu ulusal üst kuruluş belirlenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Odaların üye olduğu üst kuruluş TÜRMOB'dur",
            'B': "Odaların üye olduğu üst kuruluş Kamu Gözetimi Kurumu'dur",
            'C': 'Hazine ve Maliye Bakanlığı meslek örgütünü gözetir ve denetler',
            'D': 'Hazine ve Maliye Bakanlığı odaların üst kuruluşu değildir',
            'E': 'TOBB, meslek odalarının üst kuruluşu değildir',
        },
        'B',
        '3568 md. 28: odaların üye olduğu üst kuruluş TÜRMOB (Türkiye Serbest Muhasebeci Mali Müşavirler ve Yeminli Mali Müşavirler Odaları Birliği) adıyla anılır. Hazine ve Maliye Bakanlığı üst kuruluş değil, meslek örgütünün genel gözetim ve denetiminden sorumlu bakanlıktır; Kamu Gözetimi Kurumu ise bağımsız denetim alanını düzenler.',
    ),
    # düzey 2
    '0042': patch(
        'Bir meslek odasının organları belirlenmektedir. Buna göre aşağıdakilerden hangisi odanın zorunlu organlarından biri değildir?',
        {
            'A': 'Yüksek danışma kurulu',
            'B': 'Denetleme kurulu',
            'C': 'Disiplin kurulu',
            'D': 'Yönetim kurulu',
            'E': 'Genel kurul',
        },
        'A',
        "3568 md. 17: odanın organları GENEL KURUL, YÖNETİM KURULU, DİSİPLİN KURULU ve DENETLEME KURULU'dur. Yüksek danışma kurulu oda düzeyinde değil, Birlik bünyesinde öngörülmüş bir danışma organıdır.",
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0043': patch(
        "3568 sayılı Kanun'a göre meslek mensuplarına verilebilecek disiplin cezaları belirlenmektedir. Buna göre aşağıdakilerden hangisi bu cezalardan biri değildir?",
        {
            'A': 'Geçici olarak mesleki faaliyetten alıkoyma',
            'B': 'Kınama cezası',
            'C': 'Uyarma cezası',
            'D': 'Meslekten çıkarma',
            'E': 'Ruhsatın süresiz olarak askıya alınması',
        },
        'E',
        "3568 md. 48: disiplin cezaları UYARMA, KINAMA, GEÇİCİ OLARAK MESLEKÎ FAALİYETTEN ALIKOYMA, YEMİNLİ SIFATINI KALDIRMA ve MESLEKTEN ÇIKARMA'dır. 'Ruhsatın süresiz askıya alınması' kanunda öngörülmüş bir disiplin cezası değildir.",
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 1
    '0044': patch(
        'Bir meslek mensubuna, mesleğin yürütülmesinde daha dikkatli davranması gerektiğinin yazıyla bildirilmesine karar verilmiştir. Buna göre uygulanan disiplin cezası aşağıdakilerden hangisidir?',
        {
            'A': 'Kınama cezası',
            'B': 'Yeminli sıfatını kaldırma',
            'C': 'Uyarma cezası',
            'D': 'Geçici olarak mesleki faaliyetten alıkoyma',
            'E': 'Meslekten çıkarma',
        },
        'C',
        '3568 md. 48: UYARMA, meslek mensubuna mesleğin yürütülmesinde daha dikkatli davranması gerektiğinin yazı ile bildirilmesidir. KINAMA ise meslek mensubuna görevinde ve davranışında kusurlu sayıldığının yazı ile bildirilmesidir; uyarmadan bir derece ağırdır.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0045': patch(
        'Bir meslek mensubu hakkında meslekten çıkarma cezası kesinleşmiştir. Meslek mensubu, cezanın yalnızca bir süre için faaliyeti durdurduğunu ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslekten çıkarma, odaya olan aidat borcunun ödenmemesine bağlanmış bir cezadır',
            'B': 'Meslekten çıkarma cezası belli bir süre sonra kınamaya dönüşür',
            'C': 'Meslekten çıkarma yeminli mali müşavirlere özgü bir cezadır',
            'D': 'Meslekten çıkarma en ağır disiplin cezası olup meslek mensubunun ruhsatı geri alınır',
            'E': 'Meslekten çıkarma, belirli bir süre için mesleki faaliyetin durdurulması anlamına gelir',
        },
        'D',
        '3568 md. 48: MESLEKTEN ÇIKARMA, meslek mensubunun ruhsatnamesinin geri alınarak bir daha mesleği icra etmesine izin verilmemesidir; en ağır disiplin cezasıdır. Geçici süreli faaliyet yasağı ise ayrı bir ceza türüdür (geçici olarak meslekî faaliyetten alıkoyma).',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0046': patch(
        'Bir meslek mensubu hakkında disiplin soruşturması yürütülmüş ve ceza verilmesi gündeme gelmiştir. Meslek mensubu, cezayı doğrudan Birliğin vereceğini düşünmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Disiplin cezasını ilk derecede Birlik disiplin kurulu verir',
            'B': 'Disiplin cezasını ilk derecede meslek mensubunun kayıtlı olduğu odanın disiplin kurulu verir',
            'C': 'Disiplin cezasını ilk derecede, meslek örgütü üzerinde gözetim yetkisi bulunan Hazine ve Maliye Bakanlığı verir',
            'D': 'Disiplin cezasını ilk derecede idare mahkemesi verir',
            'E': 'Disiplin cezasını ilk derecede oda yönetim kurulu verir',
        },
        'B',
        '3568 md. 25, 26 ve 48: disiplin cezası verme yetkisi ilk derecede meslek mensubunun kayıtlı olduğu ODANIN DİSİPLİN KURULUNA aittir. Birlik disiplin kurulu itiraz mercii olarak görev yapar; yönetim kurulu soruşturmayı başlatır ancak ceza vermez.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0047': patch(
        'Bir odada denetleme kurulunun görev alanı tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Denetleme kurulu odanın en yetkili karar organıdır',
            'B': 'Denetleme kurulu meslek mensuplarına disiplin cezası verir',
            'C': 'Denetleme kurulu odanın günlük işlerini yürüten icra organıdır',
            'D': 'Denetleme kurulu üyeleri Birlik yönetim kurulu tarafından atanır ve oda genel kurulunca seçilmez',
            'E': 'Denetleme kurulu odanın işlem ve hesaplarını denetler; disiplin cezası verme yetkisi bulunmaz',
        },
        'E',
        '3568 md. 17 ve 27: denetleme kurulu, odanın işlemlerini ve hesaplarını denetleyerek genel kurula rapor sunar. Disiplin cezası verme yetkisi DİSİPLİN KURULUNA, icra yetkisi YÖNETİM KURULUNA aittir. Tüm oda organları genel kurulca seçilir.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 3
    '0048': patch(
        'Disiplin cezaları ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Uyarma, meslek mensubuna daha dikkatli davranması gerektiğinin yazıyla bildirilmesidir. II. Meslekten çıkarma cezasında meslek mensubunun ruhsatnamesi geri alınır. III. Disiplin cezasını ilk derecede Birlik disiplin kurulu verir. IV. Kesinleşen disiplin cezalarına karşı yargı yolu kapalıdır.',
        {
            'A': 'I ve II',
            'B': 'Yalnız III',
            'C': 'III ve IV',
            'D': 'I, III ve IV',
            'E': 'II ve III',
        },
        'C',
        'III YANLIŞ: disiplin cezasını ilk derecede ODA DİSİPLİN KURULU verir; Birlik disiplin kurulu itiraz merciidir. IV YANLIŞ: kesinleşen disiplin cezası idari işlem olduğundan Anayasa md. 125 ve İYUK uyarınca idari yargıda iptal davasına konu edilebilir. I ve II (md. 48) doğrudur.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0049': patch(
        'Bir bölgede yeni bir meslek odası kurulması gündeme gelmiştir. Bölgede kayıtlı meslek mensubu sayısı yeterli görülmemektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sayı koşulu gerçekleşmeyen yerlerdeki meslek mensupları en yakın odaya kaydolur',
            'B': 'Oda kuruluşu kanuni koşula bağlıdır',
            'C': 'Oda kurulması Birlik genel kurulunun serbest takdirine bırakılmamıştır',
            'D': 'Oda kurulması için meslek mensubu sayısı bakımından koşul aranmaz',
            'E': 'Oda, kamu kurumu statüsünde bir meslek kuruluşudur',
        },
        'D',
        '3568 md. 14: odalar, bölgelerinde kanunda öngörülen sayıda meslek mensubunun bulunması hâlinde kurulur. Sayı koşulu gerçekleşmeyen yerlerdeki meslek mensupları en yakın odaya kaydolur. Kuruluş kanuni koşula bağlıdır ve takdire bırakılmamıştır; odalar kamu kurumu niteliğindeki meslek kuruluşlarıdır.',
    ),
    # düzey 2
    '0050': patch(
        "TÜRMOB ve odalar ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Odaların en yetkili karar organı genel kuruldur. II. Odaların üye olduğu üst kuruluş TÜRMOB'dur. III. Mesleğin genel gözetim ve denetimi Hazine ve Maliye Bakanlığına aittir.",
        {
            'A': 'I, II ve III',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'A',
        "Üç ifade de doğrudur. 3568 md. 18 genel kurulu odanın en yetkili karar organı sayar, md. 28 odaların üst kuruluşu olarak TÜRMOB'u düzenler, md. 41 ise mesleğin ve meslek örgütünün genel gözetim ve denetimini Bakanlığa bırakır.",
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 3
    '0051': patch(
        "TÜRMOB Genel Kurulunca usulüne uygun olarak alınan ve Resmî Gazete'de yayımlanan bir mecburi meslek kararı bulunmaktadır. Bir meslek mensubu bu karara uymamıştır. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Mecburi meslek kararlarını Birlik Genel Kurulu alır',
            'B': "Kararlar Resmî Gazete'de yayımlanarak yürürlüğe girer",
            'C': 'Karara uymamak disiplin sorumluluğu doğurmaz',
            'D': 'Kararlar serbest muhasebeci mali müşavirleri de bağlar',
            'E': 'Kararlar tavsiye değil, bağlayıcı düzenlemedir',
        },
        'C',
        "3568 md. 33: Birlik Genel Kurulu, meslek mensuplarının uyacağı mecburi meslek kararlarını alır; bu kararlar Resmî Gazete'de yayımlanarak yürürlüğe girer ve tüm meslek mensuplarını bağlar. Kararlar tavsiye niteliğinde değildir; uymamak md. 48 uyarınca disiplin cezası gerektirir.",
    ),
    # düzey 2
    '0052': patch(
        'Bir meslek mensubu mesleği bırakmaya ve ruhsatını iade etmeye karar vermiştir. Meslek mensubunun devam eden müşteri işleri bulunmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Odaya kayıt silinir ve unvanın kullanılması sona erer',
            'B': 'Meslek mensubu mesleği bırakma yönündeki iradesini bağlı olduğu odaya bildirmelidir',
            'C': 'Faaliyet dönemine ilişkin defter ve belgeler, mevzuatta öngörülen süre boyunca saklanmaya devam eder',
            'D': 'Devam eden işlerin devri ve belgelerin iş sahiplerine geri verilmesi gerekir',
            'E': 'Ruhsat iadesi, meslek mensubunun mesleki faaliyet döneminden doğan sorumluluklarını da sona erdirir',
        },
        'E',
        'Mesleği bırakan meslek mensubu odaya bildirimde bulunur, kaydı silinir ve unvanı kullanmaya son verir; devam eden işleri devretmesi ve belgeleri iş sahiplerine geri vermesi gerekir. Ancak ruhsat iadesi, FAALİYET DÖNEMİNDEN doğan mali, disiplin ve cezai sorumluluğu ORTADAN KALDIRMAZ.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 1
    '0053': patch(
        'Meslek örgütünün üyelerini temsil etme işlevi tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Temsil yetkisi Hazine ve Maliye Bakanlığı tarafından kullanılır',
            'B': 'Odalar ve Birlik mesleği ve meslek mensuplarını temsil eder',
            'C': 'Meslek örgütü gerektiğinde uluslararası kuruluşlar nezdinde de temsil yapar',
            'D': 'Temsil yetkisi disiplin süreçleriyle sınırlı değildir',
            'E': 'Temsil, serbest muhasebeci mali müşavirleri de kapsar',
        },
        'A',
        '3568 md. 14 ve 29: odalar ve Birlik, mesleği ve meslek mensuplarını temsil eden kuruluşlardır; üyelerini yurt içinde ve gerektiğinde uluslararası kuruluşlar nezdinde temsil eder. Temsil yetkisi unvana ya da disiplin süreçlerine sınırlı değildir ve bakanlık tarafından kullanılmaz.',
    ),
    # düzey 2
    '0054': patch(
        'Meslek örgütü ve disiplin bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Disiplin cezasını ilk derecede oda disiplin kurulu verir',
            'B': 'Oda disiplin kurulu kararları kesin olup itiraz edilemez',
            'C': 'Oda disiplin kurulu kararlarına karşı Birlik disiplin kuruluna itiraz edilir',
            'D': 'Savunma hakkı tanınmadan disiplin cezası verilemez',
            'E': 'Kesinleşen disiplin cezasına karşı idari yargı yolu açıktır',
        },
        'B',
        'Oda disiplin kurulu kararları KESİN DEĞİLDİR; Birlik disiplin kuruluna itiraz edilebilir (3568 md. 48 ve Disiplin Yönetmeliği). İtiraz üzerine kesinleşen ceza ise idari yargı denetimine tabidir. Savunma hakkı Anayasa md. 129 güvencesidir.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0055': patch(
        'Meslek örgütü ve organları ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Oda organları genel kurul, yönetim kurulu, disiplin kurulu ve denetleme kuruludur. II. Oda organları genel kurulca seçimle göreve gelir. III. Disiplin cezası verme yetkisi denetleme kuruluna aittir.',
        {
            'A': 'I ve III',
            'B': 'Yalnız I',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'D',
        'I doğrudur (3568 md. 17). II doğrudur (md. 19, 21, 25 ve 27). III YANLIŞTIR: disiplin cezası verme yetkisi DİSİPLİN KURULUNA aittir; denetleme kurulu odanın işlem ve hesaplarını denetler (md. 26-27).',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 3
    '0056': patch(
        'Bir meslek mensubu, altı ay süreyle geçici olarak mesleki faaliyetten alıkoyma cezası almıştır. Meslek mensubu, ceza süresince müşterilerinin defterlerini tutmayı sürdürmeyi ve büro tabelasını korumayı planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ceza yeni ruhsat başvurularını engeller; mevcut faaliyet etkilenmez',
            'B': 'Ceza süresince faaliyette bulunamaz; işleri başka meslek mensubuna devretmelidir',
            'C': 'Ceza süresince danışmanlık verebilir, defter tutabilir',
            'D': 'Ceza süresince faaliyetini bir yardımcı aracılığıyla sürdürebilir',
            'E': 'Meslek mensubu ceza süresince mevcut müşterilerinin işlerini sürdürebilir; yeni iş kabul edemez',
        },
        'B',
        '3568 md. 48: geçici olarak meslekî faaliyetten alıkoyma, mesleki sıfat saklı kalmak koşuluyla belirli süre için FAALİYETTEN ALIKONULMADIR. Ceza süresince meslek mensubu hiçbir mesleki iş göremez; mevcut işlerin başka bir meslek mensubuna devri gerekir. Faaliyetin yardımcı ya da başka bir kişi üzerinden dolaylı sürdürülmesi cezanın dolanılması sayılır.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0057': patch(
        'Serbest muhasebeci mali müşavirler odası ile yeminli mali müşavirler odasının örgütlenmesi tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Serbest muhasebeci mali müşavirler odası, yeminli mali müşavirler odasının şubesidir',
            'B': 'Yeminli mali müşavirler için ayrı bir üst birlik kurulmuştur',
            'C': 'Yeminli mali müşavirler odaya kaydolmaksızın faaliyet gösterebilir',
            'D': 'İki unvan tek bir oda çatısı altında birlikte örgütlenir',
            'E': 'İki unvan ayrı odalarda örgütlenir; her iki oda türü de aynı Birliğe üyedir',
        },
        'E',
        "3568 md. 14 ve 28: serbest muhasebeci mali müşavirler odaları ile yeminli mali müşavirler odaları AYRI AYRI kurulur; ancak her iki oda türü de tek bir üst kuruluş olan TÜRMOB'a üyedir. Odalar arasında ast-üst ilişkisi yoktur ve her iki unvan için de odaya kayıt zorunludur.",
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 3
    '0058': patch(
        'Meslekten çıkarma cezası kesinleşen bir meslek mensubu, bir süre sonra yeniden ruhsat almak için başvurmayı düşünmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslekten çıkarma cezası alan meslek mensubu, ceza tarihinden bir yıl sonra yeniden ruhsat almaya hak kazanır',
            'B': 'Meslekten çıkarma cezasında meslek mensubunun ruhsatnamesi geri alınır ve odaya olan kaydı silinir',
            'C': 'Ceza kesinleşene kadar meslek mensubunun itiraz hakkı bulunur',
            'D': 'Meslekten çıkarma, disiplin cezalarının en ağırıdır',
            'E': 'Kesinleşen disiplin cezasına karşı idari yargı yolu açıktır',
        },
        'A',
        '3568 md. 48: meslekten çıkarma, ruhsatnamenin geri alınarak bir daha mesleğin icrasına izin verilmemesidir; kanun otomatik bir yeniden kazanım süresi öngörmez. Ceza kesinleşmeden önce itiraz yolu, kesinleştikten sonra ise idari yargı yolu açıktır.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 2
    '0059': patch(
        'Bir meslek mensubu, odaya olan aidat borcunu ödememiş ve genel kurula katılıp oy kullanmak istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Aidat borcu bulunsa dahi meslek mensubunun genel kurulda oy kullanma hakkı bir koşula bağlanamaz',
            'B': 'Aidat borcu bulunan meslek mensubunun ruhsatı doğrudan düşer',
            'C': 'Oy hakkı, oda yükümlülüklerinin yerine getirilmesine bağlanabilir',
            'D': 'Oy hakkı yeminli mali müşavirlere tanınmıştır',
            'E': 'Genel kurula katılım oda yönetim kurulu üyelerine açıktır',
        },
        'C',
        '3568 md. 18 ve ilgili yönetmelikler: genel kurula katılma ve oy kullanma hakkı odaya kayıtlı meslek mensuplarına aittir; ancak aidat gibi oda yükümlülüklerinin yerine getirilmesi koşulu getirilebilir. Aidat borcu ruhsatı kendiliğinden düşürmez; ödenmemesi disiplin ve takip sonuçları doğurur.',
        '3568 sayili SMMM ve YMM Kanunu',
    ),
    # düzey 3
    '0060': patch(
        'Meslek örgütü ve disiplin ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Disiplin cezalarının en ağırı meslekten çıkarmadır. II. Yeminli sıfatının kaldırılması cezası tüm meslek mensuplarına uygulanabilir. III. Mecburi meslek kararları bağlayıcı olmayıp tavsiye değeri taşır. IV. Kesinleşen disiplin cezasına karşı idari yargı yolu açıktır.',
        {
            'A': 'Yalnız II',
            'B': 'I, II ve III',
            'C': 'III ve IV',
            'D': 'I ve IV',
            'E': 'II ve III',
        },
        'E',
        'II YANLIŞ: yeminli sıfatının kaldırılması niteliği gereği yalnızca YEMİNLİ MALİ MÜŞAVİRLERE uygulanabilir. III YANLIŞ: 3568 md. 33 uyarınca mecburi meslek kararları bağlayıcıdır ve uymamak disiplin sorumluluğu doğurur. I (md. 48) ve IV (İYUK) doğrudur.',
        '3568 sayili SMMM ve YMM Kanunu',
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
    print(f"1 paket / {len(PATCHES)} soru ('Meslek Orgutu ve Disiplin' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
