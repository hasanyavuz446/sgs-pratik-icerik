#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Denetim Standartları, Etik ve Bağımsızlık — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Denetim turu (gerçek denetim bloğu 73-88 ile ölçüldü; BDS 210 sözleşme ve kalite yönetimi sık soruluyor, havuzda yoktu). Paket baştan yazıldı: geleneksel GKGDS sınıflaması, BDS 200 (genel amaç, makul ve sınırlı güvence, mesleki muhakeme), Etik Kurallar (beş temel ilke, sır saklamanın istisnaları, özde ve görünüşte bağımsızlık, beş tehdit türü ve önlemler, koşullu ücret), TTK 400 denetçi olamayacaklar, BDS 210 (ön şartlar, sözleşme içeriği, kabul öncesi sınırlama, şartların değiştirilmesi), BDS 220 ve KYS 1-2 (sorumlu denetçi, sözleşme kalite gözden geçirmesi, danışma, görüş ayrılığı), müşteri kabulü ve önceki denetçiyle iletişim.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: BDS 200, 210, 220; KYS 1, KYS 2; Bağımsız Denetçiler İçin Etik Kurallar; TTK 400
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/denetim/denetim_standartlari_etik.json"
STYLE_REF = 'SGS Denetim (standarda atıflı/olay kök + kısa şık; gerçek sınav profili)'
ONEK = "den-standart-gen-"


def patch(stem, options, answer, solution, ref='BDS 200; BDS 210; BDS 220; KYS 1; KYS 2; Etik Kurallar; TTK m.400'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        'Bir denetçi, uzmanlık alanı dışında kalan karmaşık bir türev araç değerlemesini, gerekli bilgi ve deneyime sahip olmadan tek başına üstlenmiştir.\n\nBu durum hangi temel ilkeyi tehdit eder?',
        {
            'A': 'Mesleki yeterlilik ve özen',
            'B': 'Mesleki davranış',
            'C': 'Bağımsızlık ve tarafsızlığın görünüşte korunması',
            'D': 'Dürüstlük',
            'E': 'Sır saklama',
        },
        'A',
        'Mesleki yeterlilik ve özen ilkesi, denetçinin hizmeti yetkin biçimde sunacak bilgi ve beceriye sahip olmasını ve özenle çalışmasını gerektirir.',
    ),
    # düzey 3
    '0002': patch(
        'Bir müşteri, denetçiden finansal tablolarına ilişkin olarak denetime göre daha düşük güvence içeren ve olumsuz bir dille ifade edilen bir sonuç talep etmektedir.\n\nBu talep hangi hizmet türüne karşılık gelir?',
        {
            'A': 'Makul güvence denetimi',
            'B': 'Vergi incelemesi',
            'C': 'Sınırlı güvence denetimi',
            'D': 'Derleme hizmeti',
            'E': 'Üzerinde mutabık kalınan prosedürler',
        },
        'C',
        'Sınırlı güvence denetiminde risk, makul güvence denetimine göre daha yüksek ama kabul edilebilir bir düzeye indirilir ve sonuç olumsuz biçimde ifade edilir.',
    ),
    # düzey 2
    '0003': patch(
        "Etik Kurallar'a göre görünüşte bağımsızlık aşağıdakilerden hangisini ifade eder?",
        {
            'A': 'Denetçinin zihinsel tutumu',
            'B': 'Denetçinin ücret düzeyi',
            'C': 'Denetçinin mesleki unvanı',
            'D': 'Yönetimle kişisel dostluğun güçlü olması',
            'E': 'Makul üçüncü kişinin bağımsızlığı sorgulamayacağı durum',
        },
        'E',
        'Görünüşte bağımsızlık, ilgili bilgilere sahip makul ve bilgili bir üçüncü kişinin denetçinin dürüstlüğünün, tarafsızlığının veya mesleki şüpheciliğinin zedelendiği sonucuna varmasına yol açacak durumlardan kaçınılmasıdır. Zihinsel tutum özde bağımsızlıktır.',
    ),
    # düzey 2
    '0004': patch(
        'Şirket yönetimi, denetçinin sınırlı olumlu görüş vermesi hâlinde sözleşmeyi feshedeceğini ve başka bir denetim kuruluşuyla çalışacağını bildirmiştir.\n\nBu durum hangi tehdidi oluşturur?',
        {
            'A': 'Kendi çalışmasını denetleme',
            'B': 'Yıldırma',
            'C': 'Taraf tutma',
            'D': 'Yakınlık',
            'E': 'Kişisel çıkar',
        },
        'B',
        'Denetçinin gerçek ya da algılanan baskılarla tarafsız davranmaktan alıkonulması yıldırma tehdidi oluşturur.',
    ),
    # düzey 2
    '0005': patch(
        "Etik Kurallar'a göre bağımsızlık tehdidini kabul edilebilir düzeye indirecek önlem bulunmadığında denetçi ne yapar?",
        {
            'A': 'Ekip sayısını azaltır',
            'B': 'Tehdidi yönetime bildirip yönetimin yazılı onayıyla hizmete devam eder',
            'C': 'Hizmeti reddeder veya sona erdirir',
            'D': 'Ücretini artırır',
            'E': 'Tehdidi raporda açıklar',
        },
        'C',
        'Önlemlerle tehdit ortadan kaldırılamıyor ya da kabul edilebilir düzeye indirilemiyorsa denetçi hizmeti reddeder veya sona erdirir.',
    ),
    # düzey 2
    '0006': patch(
        'Sorumlu denetçi aynı şirketin denetimini uzun yıllardır sürdürmekte ve şirketin genel müdürüyle yakın arkadaşlık ilişkisi kurmuş bulunmaktadır.\n\nBu durum hangi tehdidi oluşturur?',
        {
            'A': 'Yakınlık',
            'B': 'Taraf tutma',
            'C': 'Yıldırma',
            'D': 'Kişisel çıkar',
            'E': 'Kendi çalışmasını denetleme',
        },
        'A',
        'Uzun süreli ya da yakın ilişki nedeniyle müşterinin çıkarlarına fazla anlayış gösterilmesi yakınlık tehdidi oluşturur.',
    ),
    # düzey 3
    '0007': patch(
        'Bir denetim kuruluşu reklamında, rakip kuruluşların çalışmalarını dayanaksız biçimde kötüleyen ifadeler kullanmıştır.\n\nBu davranış hangi temel ilkeye aykırıdır?',
        {
            'A': 'Mesleki davranış',
            'B': 'Dürüstlük ile mesleki yeterlilik ve özen birlikte',
            'C': 'Mesleki yeterlilik',
            'D': 'Sır saklama',
            'E': 'Tarafsızlık',
        },
        'A',
        'Mesleki davranış ilkesi mesleğin itibarını zedeleyen davranışlardan kaçınmayı gerektirir; başkalarının çalışmalarına dayanaksız atıflar bu ilkeye aykırıdır.',
    ),
    # düzey 2
    '0008': patch(
        'Yeni bir müşteriyi kabul etmeyi değerlendiren denetçi, müşterinin izniyle önceki denetçiyle görüşmüştür.\n\nAşağıdakilerden hangisi denetçinin önceki denetçiye sorması beklenen konulardan biri değildir?',
        {
            'A': 'Yönetimin dürüstlüğüne ilişkin bilgiler',
            'B': 'Hile ya da mevzuata aykırılık bildirimleri',
            'C': 'Önceki denetçinin diğer müşterileri',
            'D': 'Muhasebe politikalarındaki görüş ayrılıkları',
            'E': 'Denetçi değişikliğinin nedenleri',
        },
        'C',
        'Önceki denetçiye yönetimin dürüstlüğü, muhasebe politikaları ve denetim prosedürleri konusundaki görüş ayrılıkları, değişikliğin nedenleri ve hile ya da mevzuata aykırılık bildirimleri sorulur. Diğer müşterilere ilişkin bilgiler gizlidir.',
    ),
    # düzey 2
    '0009': patch(
        "BDS 200'e göre denetçinin mesleki muhakeme kullanması gereken alanlardan biri aşağıdakilerden hangisi değildir?",
        {
            'A': 'Prosedürlerin niteliğinin seçilmesi',
            'B': 'Mevzuattaki zorunlu sürelerin belirlenmesi',
            'C': 'Önemliliğin ve denetim riskinin belirlenmesi',
            'D': 'Kanıtın yeterliliğinin değerlendirilmesi',
            'E': 'Yönetimin muhakemelerinin değerlendirilmesi',
        },
        'B',
        'Mesleki muhakeme önemlilik ve risk, prosedürlerin niteliği, zamanlaması ve kapsamı, kanıtın yeterliliği ve yönetim muhakemelerinin değerlendirilmesinde kullanılır. Mevzuatın açıkça belirlediği süreler muhakeme konusu değildir.',
    ),
    # düzey 3
    '0010': patch(
        'I. Kişisel çıkar\nII. Kendi çalışmasını denetleme\nIII. Mesleki davranış\n\nYukarıdakilerden hangileri bağımsızlığa yönelik tehdit türlerindendir?',
        {
            'A': 'I, II ve III',
            'B': 'I ve III',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'D',
        'Kişisel çıkar ve kendi çalışmasını denetleme tehdit türleridir; mesleki davranış ise temel etik ilkelerden biridir.',
    ),
    # düzey 3
    '0011': patch(
        'Bir denetçi, yürürlüğe giren yeni finansal raporlama standartlarını izlemeyip eski bilgilerle denetim yürütmektedir.\n\nBu durum hangi temel ilkeyle bağdaşmaz?',
        {
            'A': 'Mesleki davranış ve sır saklama birlikte',
            'B': 'Sır saklama',
            'C': 'Tarafsızlık',
            'D': 'Dürüstlük',
            'E': 'Mesleki yeterlilik ve özen',
        },
        'E',
        'Mesleki yeterlilik ve özen ilkesi, denetçinin bilgi ve becerisini sürekli güncel tutmasını gerektirir.',
    ),
    # düzey 3
    '0012': patch(
        'Denetlenen şirketin muhasebe müdürü, denetim ekibinin kıdemli üyesi olarak görev yapan bir denetçiyi kısa süre önce işe almıştır; denetçi bu yılın denetimine katılmıştı.\n\nBu durum hangi tehditleri oluşturabilir?',
        {
            'A': 'Sır saklama ve mesleki davranış',
            'B': 'Yakınlık ve yıldırma',
            'C': 'Kişisel çıkar ve rekabet',
            'D': 'Taraf tutma ve kendi çalışmasını denetleme',
            'E': 'Tarafsızlık ve dürüstlük',
        },
        'B',
        'Eski ekip üyesinin müşteride önemli bir pozisyona geçmesi, ekibin onunla ilişkisi nedeniyle yakınlık ve ekibe baskı kurabilmesi nedeniyle yıldırma tehditleri oluşturabilir.',
    ),
    # düzey 2
    '0013': patch(
        "KYS 2'ye göre aşağıdakilerden hangisi sözleşme kalite gözden geçireninde aranmaz?",
        {
            'A': 'Denetim ekibinin üyesi olması',
            'B': 'Yetkin olması',
            'C': 'İlgili etik hükümlere uyması',
            'D': 'Tarafsız olması',
            'E': 'Yeterli zamana sahip olması',
        },
        'A',
        'Sözleşme kalite gözden geçireni yetkin, tarafsız, yeterli zamanı olan ve etik hükümlere uyan biri olmalıdır; denetim ekibinin üyesi olamaz.',
    ),
    # düzey 2
    '0014': patch(
        "Etik Kurallar'a göre sır saklama ilkesinin istisnası olarak denetçinin bilgi açıklayabileceği durumlardan biri aşağıdakilerden hangisi değildir?",
        {
            'A': 'Kamu otoritesinin kanuna dayanan talebi',
            'B': 'Mesleki bir hak veya görev bulunması',
            'C': 'Yasal bir zorunluluk bulunması',
            'D': 'Müşterinin izin vermesi',
            'E': 'Yeni bir müşteri kazanmak',
        },
        'E',
        'Bilgi; müşterinin izniyle, kanunun gerektirmesi ya da izin vermesi hâlinde veya mesleki bir hak ya da görev bulunduğunda açıklanabilir. Ticari çıkar bir istisna değildir.',
    ),
    # düzey 2
    '0015': patch(
        "BDS 200'e göre bağımsız denetimin genel amacı aşağıdakilerden hangisidir?",
        {
            'A': 'Yönetimin yerine finansal tabloları hazırlayarak kullanıcılara sunmak',
            'B': 'İşletmenin geleceğini garanti etmek',
            'C': 'Makul güvence elde edip görüş bildirmek',
            'D': 'Tüm hileleri ortaya çıkarmak',
            'E': 'Mutlak güvence sağlamak',
        },
        'C',
        'Denetçinin genel amacı, tabloların bütün olarak hata veya hile kaynaklı önemli yanlışlık içermediğine dair makul güvence elde etmek ve bulgularına göre rapor vermektir.',
    ),
    # düzey 3
    '0016': patch(
        "BDS 210'a göre yönetim sorumluluklarını kabul ettiğine dair mutabakatı sağlamayı reddetmiştir.\n\nBu durumda denetçi ne yapar?",
        {
            'A': 'Sözleşmeyi kabul eder',
            'B': 'Sorumlulukları kendisi üstlenir',
            'C': 'Sözleşmeyi kabul etmez',
            'D': 'Sözlü beyanla yetinir',
            'E': 'Kabul edip sorumlulukların reddini raporun ekinde açıklar',
        },
        'C',
        'Yönetimin sorumluluklarını kabul etmesi denetimin ön şartıdır; mutabakat sağlanamazsa ve mevzuat gerektirmiyorsa denetçi sözleşmeyi kabul etmez.',
    ),
    # düzey 2
    '0017': patch(
        'Denetim kuruluşu, denetlediği şirketin muhasebe kayıtlarını tutmakta ve finansal tablolarını hazırlamaktadır.\n\nBu durum hangi tehdidi oluşturur?',
        {
            'A': 'Kişisel çıkar',
            'B': 'Yakınlık',
            'C': 'Yıldırma',
            'D': 'Taraf tutma',
            'E': 'Kendi çalışmasını denetleme',
        },
        'E',
        'Denetçinin kendisinin hazırladığı kayıt ve tabloları denetlemesi kendi çalışmasını denetleme tehdidi oluşturur.',
    ),
    # düzey 2
    '0018': patch(
        "KYS 1'e göre aşağıdakilerden hangisi kalite yönetim sisteminin bileşenlerinden biri değildir?",
        {
            'A': 'Müşteri kabulü ve devamı',
            'B': 'Müşterinin pazarlama stratejisi',
            'C': 'İzleme ve iyileştirme süreci',
            'D': 'Kaynaklar',
            'E': 'Yönetişim ve liderlik',
        },
        'B',
        "KYS 1'deki bileşenler; risk değerlendirme süreci, yönetişim ve liderlik, etik hükümler, müşteri ilişkisinin ve sözleşmenin kabulü ve devamı, sözleşmenin yürütülmesi, kaynaklar, bilgi ve iletişim ile izleme ve iyileştirme sürecidir.",
    ),
    # düzey 3
    '0019': patch(
        "Türk Ticaret Kanunu'nun 400. maddesine göre aşağıdakilerden hangisi denetçi olarak seçilmeye engel değildir?",
        {
            'A': 'Yönetim kurulu üyelerinden birinin eşi olmak',
            'B': 'Şirketin defterlerini tutmak',
            'C': 'Denetlenecek şirkette pay sahibi olmak',
            'D': 'Şirkete daha önce eğitim semineri vermiş olmak',
            'E': 'Son üç yılda şirkette yönetici olmak',
        },
        'D',
        'Pay sahipliği, son üç yılda yöneticilik veya çalışanlık, defter tutma ya da tabloları hazırlama gibi denetim dışı hizmetler ve yönetim kurulu üyesiyle yakınlık denetçiliğe engeldir. Geçmişte verilen bir eğitim semineri tek başına engel sayılmaz.',
    ),
    # düzey 2
    '0020': patch(
        'Müşteri ilişkisinin kabulü ve devamı kapsamında aşağıdakilerden hangisi değerlendirilmez?',
        {
            'A': 'Etik hükümlere uyulabilmesi',
            'B': 'Müşterinin ürün fiyatlarının rakiplerden düşük olması',
            'C': 'Yönetimin dürüstlüğü',
            'D': 'Kuruluşun yetkinliği ve kaynakları',
            'E': 'Sözleşmeyi yürütmek için yeterli zaman bulunması',
        },
        'B',
        'Müşteri kabulünde yönetimin dürüstlüğü, kuruluşun yetkinliği ve kaynakları, etik hükümlere uyum ve zaman yeterliliği değerlendirilir; ürün fiyatlama politikası bu değerlendirmenin konusu değildir.',
    ),
    # düzey 3
    '0021': patch(
        'Denetçi, yönetiminin dürüstlüğü konusunda ciddi şüpheler bulunan bir şirketten teklif almıştır.\n\nBu durumun sözleşmenin kabulüne etkisi aşağıdakilerden hangisidir?',
        {
            'A': 'Önemli bir etkisi yoktur',
            'B': 'Kısa süreli sözleşmeyle kabul edilir',
            'C': 'Kabul edilmemesi gerekebilir',
            'D': 'Ücret yükseltilerek kabul edilir',
            'E': 'Daha az deneyimli bir ekiple ve düşük ücretle kabul edilir',
        },
        'C',
        'Yönetimin dürüstlüğü hakkında ciddi şüphe bulunması, denetim riskini kabul edilemez düzeye çıkarabileceğinden sözleşmenin kabul edilmemesini gerektirebilir.',
    ),
    # düzey 3
    '0022': patch(
        "I. Dürüstlük\nII. Tarafsızlık\nIII. Kârlılık\n\nEtik Kurallar'a göre yukarıdakilerden hangileri temel ilkelerdendir?",
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'D',
        'Dürüstlük ve tarafsızlık temel ilkelerdendir; kârlılık bir etik ilke değildir.',
    ),
    # düzey 3
    '0023': patch(
        "Bir şirketin yönetimi, denetimin sonuna yaklaşıldığında, makul bir gerekçe olmaksızın sözleşmenin bağımsız denetimden sınırlı güvence denetimine dönüştürülmesini istemiştir.\n\nBDS 210'a göre denetçi ne yapar?",
        {
            'A': 'Değişikliği kabul etmez',
            'B': 'Değişikliği kabul eder',
            'C': 'Görüşü olumluya çevirir',
            'D': 'Değişikliği kabul edip raporda önceki sözleşmeye atıf yapmadan yeni rapor verir',
            'E': 'Ücreti artırarak kabul eder',
        },
        'A',
        'Denetçi, makul bir gerekçe olmadan sözleşme şartlarının daha düşük güvence içeren bir hizmete dönüştürülmesini kabul etmez; değişikliği kabul etmezse ve yönetim mevcut şartlarla devam etmesine izin vermezse çekilmeyi değerlendirir.',
    ),
    # düzey 3
    '0024': patch(
        "BDS 220'ye göre denetim ekibi üyeleri ile sorumlu denetçi arasında önemli bir konuda görüş ayrılığı ortaya çıkmıştır.\n\nBu durumla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Sorumlu denetçinin görüşü uygulanır',
            'B': 'Görüş ayrılığı çözülmeden rapora tarih atılmaz',
            'C': 'Konu belgelenmez',
            'D': 'Ekip üyesi görevden alınarak konu kapatılır',
            'E': 'Görüş ayrılığı rapora eklenir',
        },
        'B',
        'Görüş ayrılıkları kuruluşun politika ve prosedürlerine göre ele alınıp çözülür; çözülmeden denetçi raporuna tarih atılmaz.',
    ),
    # düzey 3
    '0025': patch(
        "Bir denetçi, yanıltıcı olduğunu bildiği bir bilgiyi içeren bir rapora adının karışmasına göz yummuştur.\n\nEtik Kurallar'a göre bu davranış öncelikle hangi temel ilkeye aykırıdır?",
        {
            'A': 'Mesleki davranış',
            'B': 'Sır saklama',
            'C': 'Mesleki yeterlilik ve özen',
            'D': 'Dürüstlük',
            'E': 'Tarafsızlık ile mesleki yeterlilik ve özen birlikte',
        },
        'D',
        'Dürüstlük ilkesi, denetçinin bilerek yanlış ya da yanıltıcı bilgi içeren rapor ve iletişimlerle ilişkilendirilmemesini gerektirir.',
    ),
    # düzey 2
    '0026': patch(
        "BDS 220 ve KYS 2'ye göre sözleşme kalite gözden geçirmesi gereken bir denetimde rapora ne zaman tarih atılabilir?",
        {
            'A': 'Gözden geçirenin görüşü alınmadan, yönetimin onayıyla',
            'B': 'Gözden geçirme başlamadan',
            'C': 'Gözden geçirme tamamlandıktan sonra',
            'D': 'Gözden geçirme sürerken',
            'E': 'Rapor yayımlandıktan sonra',
        },
        'C',
        'Sözleşme kalite gözden geçirmesi gereken denetimlerde, gözden geçirme tamamlanmadan denetçi raporuna tarih atılmaz.',
    ),
    # düzey 2
    '0027': patch(
        "BDS 210'a göre aşağıdakilerden hangisi denetim sözleşmesinde yer alması gereken hususlardan biri değildir?",
        {
            'A': 'Yönetimin sorumlulukları',
            'B': 'Verilecek görüşün türü',
            'C': 'Denetçinin sorumlulukları',
            'D': 'Beklenen raporun şekli ve içeriğinin farklı olabileceği beyanı',
            'E': 'Denetimin amacı ve kapsamı',
        },
        'B',
        'Sözleşmede denetimin amacı ve kapsamı, denetçinin ve yönetimin sorumlulukları, uygulanacak çerçeve ve beklenen raporların şekli ve içeriği ile koşullara göre farklı olabileceği belirtilir. Görüşün türü önceden taahhüt edilemez.',
    ),
    # düzey 2
    '0028': patch(
        'BDS 210 ve kalite yönetimi standartlarına göre denetim kuruluşunun yeni bir müşteriyi kabul etmeden önce aşağıdakilerden hangisini değerlendirmesi gerekmez?',
        {
            'A': 'Müşterinin gelecek yılki kâr tahmini',
            'B': 'Denetimin ön şartlarının varlığı',
            'C': 'Etik hükümlere uyulup uyulamayacağı',
            'D': 'Yetkin ekip bulunup bulunmadığı',
            'E': 'Yönetimin dürüstlüğü',
        },
        'A',
        'Kabul öncesinde etik hükümlere uyum, yetkinlik ve kaynaklar, denetimin ön şartları ve yönetimin dürüstlüğü değerlendirilir. Müşterinin kâr tahmini kabul kararının ölçütü değildir.',
    ),
    # düzey 3
    '0029': patch(
        "Karmaşık bir türev araç konusunda ekipte anlaşmazlık bulunan sorumlu denetçi, kuruluş içindeki uzman bir ortağın görüşüne başvurmuştur.\n\nBDS 220'ye göre bu uygulama hangi kavrama karşılık gelir?",
        {
            'A': 'Rotasyon',
            'B': 'Danışma',
            'C': 'Soğuma',
            'D': 'Sözleşme kalite gözden geçirmesinin yerine geçen inceleme',
            'E': 'Sözleşme feshi',
        },
        'B',
        "Zor ya da tartışmalı konularda kuruluş içinde veya dışında uygun kişilere danışılması ve sonuçların belgelenmesi BDS 220'nin gerektirdiği danışma sürecidir.",
    ),
    # düzey 2
    '0030': patch(
        "BDS 210'a göre denetçinin sözleşmeyi kabul etmeden önce yönetimle mutabık kalması gereken sorumluluklardan biri aşağıdakilerden hangisi değildir?",
        {
            'A': 'Tabloların çerçeveye uygun hazırlanması',
            'B': 'Gerekli iç kontrolün sağlanması',
            'C': 'İlgili tüm bilgilere erişim sağlanması',
            'D': 'Kişilere sınırsız erişim sağlanması',
            'E': 'Denetçinin önemlilik düzeyini onaylamak',
        },
        'E',
        'Yönetim; tabloların çerçeveye uygun hazırlanmasını, önemli yanlışlık içermemesi için gerekli iç kontrolü ve denetçiye bilgilere, ek bilgilere ve kişilere sınırsız erişimi sağlama sorumluluğunu kabul eder. Önemliliği denetçi belirler.',
    ),
    # düzey 2
    '0031': patch(
        'Denetim ekibi üyesi, denetlediği şirketin hisse senetlerinden önemli tutarda satın almıştır.\n\nBu durum hangi tehdidi oluşturur?',
        {
            'A': 'Yıldırma',
            'B': 'Yakınlık',
            'C': 'Kişisel çıkar',
            'D': 'Taraf tutma',
            'E': 'Kendi çalışmasını denetleme',
        },
        'C',
        'Denetlenen işletmede doğrudan finansal çıkara sahip olmak kişisel çıkar tehdidi oluşturur.',
    ),
    # düzey 3
    '0032': patch(
        "Önceki yıl aynı şirketin sorumlu denetçisi olan kişinin bu yıl sözleşme kalite gözden geçireni olarak atanması düşünülmektedir.\n\nKYS 2'ye göre bu atama için hangisi doğrudur?",
        {
            'A': 'Hemen atanabilir',
            'B': 'Yönetimin onayı alınırsa soğuma süresi aranmaz',
            'C': 'Sorumlu denetçiyle birlikte atanabilir',
            'D': 'Ücreti artırılarak atanabilir',
            'E': 'Soğuma süresi geçmeden atanamaz',
        },
        'E',
        'Önceki dönemde sorumlu denetçi olan kişinin aynı denetimde sözleşme kalite gözden geçireni olabilmesi için soğuma süresi geçmesi gerekir; bu, tarafsızlık tehditlerini azaltır.',
    ),
    # düzey 2
    '0033': patch(
        "Etik Kurallar'a göre özde bağımsızlık aşağıdakilerden hangisini ifade eder?",
        {
            'A': 'Denetçinin müşteriyle olan finansal ilişkilerinin dışarıdan nasıl göründüğü',
            'B': 'Tarafsızlığı zedelemeyen zihinsel tutum',
            'C': 'Kuruluşun büyüklüğü',
            'D': 'Denetim ücretinin büyüklüğü',
            'E': 'Makul üçüncü kişinin algısı',
        },
        'B',
        'Özde bağımsızlık, mesleki muhakemeyi zedeleyecek etkilere maruz kalmadan görüş bildirmeye imkân veren zihinsel tutumdur; makul üçüncü kişinin algısı görünüşte bağımsızlıktır.',
    ),
    # düzey 2
    '0034': patch(
        "Tekrarlanan bir denetimde aşağıdakilerden hangisi BDS 210'a göre sözleşme şartlarının yeniden değerlendirilmesini gerektirebilecek durumlardan biri değildir?",
        {
            'A': 'Denetçinin ofis adresinin değişmesi',
            'B': 'Yeni yasal raporlama gereklilikleri',
            'C': 'Şirket mülkiyetinde önemli değişiklik',
            'D': 'Yönetimde önemli değişiklik olması',
            'E': 'Yönetimin sözleşme şartlarını yanlış anladığına dair bir gösterge bulunması',
        },
        'A',
        'Yönetimde ya da mülkiyette önemli değişiklik, yeni yasal gereklilikler, şartların yanlış anlaşıldığına dair göstergeler ve işletmenin faaliyetlerinde önemli değişiklik sözleşmenin yeniden değerlendirilmesini gerektirebilir.',
    ),
    # düzey 2
    '0035': patch(
        'Denetçi, denetlediği şirketi bir vergi uyuşmazlığında mahkeme önünde savunmayı üstlenmiştir.\n\nBu durum hangi tehdidi oluşturur?',
        {
            'A': 'Kişisel çıkar',
            'B': 'Taraf tutma',
            'C': 'Yakınlık',
            'D': 'Kendi çalışmasını denetleme',
            'E': 'Yıldırma',
        },
        'B',
        'Denetçinin müşterinin tutumunu tarafsızlığını tehlikeye atacak ölçüde savunması taraf tutma (savunuculuk) tehdidi oluşturur.',
    ),
    # düzey 3
    '0036': patch(
        "Sözleşmenin kabulünden önce yönetim, denetçinin bazı önemli hesaplara erişimini sınırlayacağını ve bunun görüş vermekten kaçınmaya yol açacağının bilindiğini belirtmiştir. Mevzuat denetçiyi bu sözleşmeyi kabule zorlamamaktadır.\n\nBDS 210'a göre denetçi ne yapar?",
        {
            'A': 'Sınırlamayı yok sayar',
            'B': 'Kabul edip olumlu görüş verir',
            'C': 'Sözleşmeyi kabul etmez',
            'D': 'Kabul edip sınırlı olumlu görüş verir',
            'E': 'Kabul edip sınırlamayı yönetimin yazılı beyanıyla gidermeye çalışır',
        },
        'C',
        'Yönetim kabul öncesinde kapsamı, görüş vermekten kaçınmaya yol açacak şekilde sınırlıyorsa ve mevzuat zorunlu tutmuyorsa denetçi sözleşmeyi kabul etmez.',
    ),
    # düzey 3
    '0037': patch(
        'Denetim ekibi üyesinin eşi, denetlenen şirkette finansal tabloların hazırlanmasından sorumlu mali işler müdürü olarak çalışmaya başlamıştır.\n\nBu duruma uygun önlem aşağıdakilerden hangisidir?',
        {
            'A': 'Üyeyi ekipten çıkarmak',
            'B': 'Durumu dipnotlarda açıklamak',
            'C': 'Üyenin ekipte kalıp belirli hesapları denetlemesine izin vermek',
            'D': 'Eşin yazılı beyanını almak',
            'E': 'Ücreti düşürmek',
        },
        'A',
        'Yakın aile üyesinin tabloların hazırlanmasında önemli etkisi olan bir pozisyonda bulunması önemli bir yakınlık ve kişisel çıkar tehdidi oluşturur; ekip üyesinin denetim ekibinden çıkarılması gerekir.',
    ),
    # düzey 3
    '0038': patch(
        "I. Denetimin amacı ve kapsamı\nII. Yönetimin sorumlulukları\nIII. Denetim ekibindeki tüm personelin isimleri\n\nBDS 210'a göre yukarıdakilerden hangileri denetim sözleşmesinde yer alması gereken hususlardandır?",
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'C',
        'Denetimin amacı ve kapsamı ile yönetimin sorumlulukları sözleşmede yer alır; ekipteki tüm personelin isimleri zorunlu unsur değildir.',
    ),
    # düzey 2
    '0039': patch(
        'Aşağıdakilerden hangisi bağımsızlık tehdidini azaltmaya yönelik bir önlem değildir?',
        {
            'A': 'Farklı ekiplerle hizmet vermek',
            'B': 'Kilit denetim personelini rotasyona tabi tutmak',
            'C': 'Tehdidi üst yönetimden sorumlu olanlarla görüşmek',
            'D': 'Ücreti denetim sonucuna bağlamak',
            'E': 'Bağımsız bir gözden geçiren görevlendirmek',
        },
        'D',
        'Bağımsız gözden geçirme, rotasyon, farklı ekip kullanımı ve üst yönetimle görüşme önlemlere örnektir. Ücreti sonuca bağlamak yeni bir kişisel çıkar tehdidi yaratır.',
    ),
    # düzey 2
    '0040': patch(
        "BDS 200'e göre makul güvence ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Sınırlı güvenceyle aynıdır',
            'B': 'Tüm işlemlerin tek tek incelenmesiyle elde edilen kesin güvencedir',
            'C': 'Yüksek ama mutlak olmayan güvencedir',
            'D': 'Güvence vermeme anlamına gelir',
            'E': 'Mutlak güvencedir',
        },
        'C',
        'Makul güvence yüksek düzeyde bir güvencedir; denetimin yapısal kısıtları nedeniyle mutlak güvence değildir.',
    ),
    # düzey 3
    '0041': patch(
        'Önceki denetçi, yeni denetçinin sorularını yanıtlamak için müşterinin iznine ihtiyaç duymaktadır.\n\nBu gereklilik hangi etik ilkeden kaynaklanır?',
        {
            'A': 'Mesleki davranış ve rekabet ilkesi',
            'B': 'Mesleki yeterlilik',
            'C': 'Tarafsızlık',
            'D': 'Sır saklama',
            'E': 'Dürüstlük',
        },
        'D',
        'Önceki denetçi müşteri bilgilerini ancak müşterinin izniyle açıklayabilir; bu sır saklama ilkesinin gereğidir.',
    ),
    # düzey 3
    '0042': patch(
        "BDS 220'ye göre sorumlu denetçinin rapora tarih atmadan önce kendisinin karar vermesi gereken husus aşağıdakilerden hangisidir?",
        {
            'A': 'Denetim ücretinin tahsil edildiği',
            'B': 'Yönetimin görüşü onayladığı',
            'C': 'Yeterli ve uygun kanıt elde edildiği',
            'D': 'Gelecek yılın sözleşmesinin imzalandığı ve ücret artışının kararlaştırıldığı',
            'E': 'Raporun basına duyurulacağı',
        },
        'C',
        'Sorumlu denetçi rapora tarih atmadan önce, denetim boyunca kalite yönetimine yeterince katıldığını ve elde edilen kanıtın görüşe dayanak oluşturmak için yeterli ve uygun olduğunu belirler.',
    ),
    # düzey 3
    '0043': patch(
        "Bir denetçi, son beş yılda mesleki faaliyetlerinden elde ettiği toplam gelirin %35'ini denetlemeye aday olduğu şirketten ve bu şirketin önemli payına sahip olduğu şirketlerden elde etmiştir.\n\nTürk Ticaret Kanunu'na göre bu durum için aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Yönetim kurulunun onayıyla seçilebilir',
            'B': 'Denetçi seçilemez',
            'C': 'Genel kurulda oybirliği sağlanırsa engel ortadan kalkar',
            'D': 'Denetçi seçilebilir',
            'E': 'Gelirin açıklanmasıyla seçilebilir',
        },
        'B',
        "TTK 400'e göre son beş yılda mesleki faaliyetlerinden elde ettiği toplam gelirin yüzde otuzundan fazlasını denetlenecek şirketten ve onun önemli paylarına sahip olduğu şirketlerden elde eden kişi denetçi olamaz.",
    ),
    # düzey 2
    '0044': patch(
        "BDS 210'a göre denetimin ön şartlarının mevcut olup olmadığını belirlemek için denetçinin yapması gerekenlerden biri aşağıdakilerden hangisidir?",
        {
            'A': 'Raporlama çerçevesinin kabul edilebilirliğini belirlemek',
            'B': 'Önemlilik düzeyini kesinleştirmek',
            'C': 'Denetim ücretini tahsil etmek',
            'D': 'Örneklem büyüklüğünü hesaplamak',
            'E': 'Görüş türünü önceden belirlemek',
        },
        'A',
        'Denetimin ön şartları; tabloların hazırlanmasında kullanılacak finansal raporlama çerçevesinin kabul edilebilir olması ve yönetimin sorumluluklarını kabul ettiğine dair mutabakattır.',
    ),
    # düzey 3
    '0045': patch(
        "BDS 200'e göre denetçi, bir BDS'nin belirli bir hükmüne ilişkin istisnai bir durumda ne yapabilir?",
        {
            'A': 'Yönetimden yazılı izin alır',
            'B': 'Alternatif prosedürle amaca ulaşır',
            'C': 'Hükmü uygulamaz ve belgelemez',
            'D': 'Hükmü sonraki yılın denetimine erteleyerek raporda açıklamaz',
            'E': 'Görüş vermekten kaçınır',
        },
        'B',
        'İstisnai durumlarda denetçi ilgili bir hükümden ayrılmayı gerekli görebilir; bu durumda hükmün amacına ulaşmak için alternatif prosedürler uygular ve bunu belgeler.',
    ),
    # düzey 2
    '0046': patch(
        "Bağımsız Denetçiler İçin Etik Kurallar'a göre aşağıdakilerden hangisi temel ilkelerden biri değildir?",
        {
            'A': 'Mesleki yeterlilik ve özen',
            'B': 'Tarafsızlık',
            'C': 'Dürüstlük',
            'D': 'Sır saklama',
            'E': 'Kârlılık',
        },
        'E',
        'Temel ilkeler dürüstlük, tarafsızlık, mesleki yeterlilik ve özen, sır saklama ve mesleki davranıştır.',
    ),
    # düzey 2
    '0047': patch(
        "BDS 210'a göre denetim sözleşmesinin şekliyle ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Yönetimin tek taraflı beyanıdır',
            'B': 'Denetim ücretini ve ödeme takvimini içeren kısa bir mektuptur',
            'C': 'Sözlü yapılabilir',
            'D': 'Rapordan sonra imzalanır',
            'E': 'Yazılı olarak düzenlenir',
        },
        'E',
        'Denetim sözleşmesinin şartları denetim sözleşmesinde ya da uygun başka bir yazılı anlaşma biçiminde kayıt altına alınır.',
    ),
    # düzey 2
    '0048': patch(
        'Geleneksel genel kabul görmüş denetim standartları sınıflamasına göre raporlama standartlarından biri aşağıdakilerden hangisidir?',
        {
            'A': 'Yeterli açıklama',
            'B': 'Bağımsızlık',
            'C': 'İç kontrolün değerlendirilmesi',
            'D': 'Mesleki özen',
            'E': 'İşin planlanması ve yardımcıların gözetimi',
        },
        'A',
        'Raporlama standartları; genel kabul görmüş muhasebe ilkelerine uygunluk, tutarlılık, yeterli açıklama ve görüş bildirmeye ilişkindir.',
    ),
    # düzey 2
    '0049': patch(
        "Etik Kurallar'a göre tarafsızlık ilkesi aşağıdakilerden hangisini ifade eder?",
        {
            'A': 'Ücreti sonuca bağlamak',
            'B': 'Müşteriyle yakın dostluk kurmak',
            'C': 'Yönetimin tercihlerine uymak',
            'D': 'Önyargı ve çıkar çatışmasından etkilenmemek',
            'E': 'Müşterinin görüşünü benimsemek',
        },
        'D',
        'Tarafsızlık, mesleki ya da ticari muhakemenin önyargı, çıkar çatışması veya başkalarının aşırı etkisi altında kalmamasıdır.',
    ),
    # düzey 2
    '0050': patch(
        "Etik Kurallar'a göre aşağıdakilerden hangisi bağımsızlığa yönelik tehdit türlerinden biri değildir?",
        {
            'A': 'Rekabet tehdidi',
            'B': 'Yakınlık',
            'C': 'Yıldırma ya da baskı yoluyla etki altına alınma',
            'D': 'Kendi çalışmasını denetleme',
            'E': 'Kişisel çıkar',
        },
        'A',
        'Tehditler; kişisel çıkar, kendi çalışmasını denetleme, taraf tutma, yakınlık ve yıldırmadır.',
    ),
    # düzey 3
    '0051': patch(
        "Denetçi, yönetimin kullandığı finansal raporlama çerçevesinin kabul edilebilir olmadığı sonucuna varmıştır ve mevzuat bu çerçeveyi zorunlu tutmamaktadır.\n\nBDS 210'a göre denetçi ne yapar?",
        {
            'A': 'Kabul edip çerçeve konusunu kilit denetim konusu olarak raporlar',
            'B': 'Kabul edip dikkat çekilen husus ekler',
            'C': 'Kabul edip olumsuz görüş verir',
            'D': 'Sözleşmeyi kabul eder',
            'E': 'Sözleşmeyi kabul etmez',
        },
        'E',
        'Kabul edilebilir bir finansal raporlama çerçevesi denetimin ön şartıdır; ön şartlar mevcut değilse ve mevzuat zorunlu tutmuyorsa denetçi sözleşmeyi kabul etmez.',
    ),
    # düzey 2
    '0052': patch(
        'Geleneksel genel kabul görmüş denetim standartları sınıflamasına göre aşağıdakilerden hangisi genel standartlar arasında yer almaz?',
        {
            'A': 'Mesleki özen',
            'B': 'Bağımsızlık',
            'C': 'Denetçinin tarafsız bir zihin yapısıyla çalışması',
            'D': 'İşin planlanması ve gözetimi',
            'E': 'Mesleki eğitim ve yeterlilik',
        },
        'D',
        'Genel standartlar denetçinin kişisel niteliklerine ilişkindir: mesleki eğitim ve yeterlilik, bağımsızlık ve mesleki özen. İşin planlanması ve gözetimi çalışma alanı standardıdır.',
    ),
    # düzey 3
    '0053': patch(
        'Denetçi sözleşme imzalandıktan sonra yönetimin kapsamı sınırladığını fark etmiş ve bunun sınırlı olumlu görüşe yol açabileceğini değerlendirmiştir.\n\nDenetçinin ilk adımı aşağıdakilerden hangisidir?',
        {
            'A': 'Hemen sözleşmeyi feshetmek',
            'B': 'Olumsuz görüş vermek',
            'C': 'Kamu Gözetimi Kurumuna bildirimde bulunup denetimi durdurmak',
            'D': 'Sınırlamanın kaldırılmasını istemek',
            'E': 'Sınırlamayı raporda belirtmeden devam etmek',
        },
        'D',
        'Kabulden sonra yönetim kapsamı sınırlarsa denetçi önce sınırlamanın kaldırılmasını ister; kaldırılmazsa üst yönetimden sorumlu olanlara bildirir ve alternatif prosedürleri değerlendirir.',
    ),
    # düzey 3
    '0054': patch(
        'Bir denetçi, müşterisinin yeni ürün maliyetlerine ilişkin bilgilerini, aynı sektörde faaliyet gösteren başka bir müşterisine danışmanlık verirken kullanmıştır.\n\nBu davranış öncelikle hangi temel ilkeye aykırıdır?',
        {
            'A': 'Sır saklama',
            'B': 'Mesleki davranış',
            'C': 'Dürüstlük',
            'D': 'Mesleki yeterlilik',
            'E': 'Tarafsızlık ve bağımsızlığın görünüşte sağlanması',
        },
        'A',
        'Sır saklama ilkesi, mesleki ilişki sonucu elde edilen bilgilerin üçüncü kişilere açıklanmamasını ve denetçinin kendi ya da başkalarının yararına kullanılmamasını gerektirir.',
    ),
    # düzey 3
    '0055': patch(
        'Denetim ücretinin, şirketin vergi incelemesinde elde edeceği vergi tasarrufunun belirli bir yüzdesi olarak belirlenmesi teklif edilmiştir.\n\nBu düzenleme için aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yönetimin onayıyla uygundur',
            'B': 'Koşullu ücret olduğundan kabul edilemez',
            'C': 'Ücretin artmasını sağladığı için uygundur',
            'D': 'Sözleşmeye yazılırsa uygundur',
            'E': 'Ücret sonuç ne olursa olsun bağımsızlığı etkilemediğinden uygundur',
        },
        'B',
        'Denetim ücretinin işin sonucuna bağlanması koşullu ücrettir ve kişisel çıkar tehdidini kabul edilebilir düzeye indirecek önlem bulunmadığından denetim sözleşmelerinde kabul edilemez.',
    ),
    # düzey 3
    '0056': patch(
        'Müşteri, yeni denetçinin önceki denetçiyle görüşmesine izin vermemiştir.\n\nBu durumun yeni denetçi açısından anlamı aşağıdakilerden hangisidir?',
        {
            'A': 'Önceki denetçiye habersiz başvurulur',
            'B': 'Önemsiz bir ayrıntıdır',
            'C': 'Sözleşmeyi kabulü ciddi biçimde sorgulanır',
            'D': 'Önceki raporun kopyasıyla yetinilir',
            'E': 'Ücret artırılarak telafi edilir',
        },
        'C',
        'Müşterinin önceki denetçiyle iletişime izin vermemesi önemli bir uyarı işaretidir; yeni denetçi bunun nedenlerini değerlendirir ve sözleşmeyi kabul edip etmeyeceğini ciddi biçimde sorgular.',
    ),
    # düzey 2
    '0057': patch(
        "BDS 220'ye göre denetimde kalite yönetimine ilişkin genel sorumluluk kime aittir?",
        {
            'A': 'Ekipteki en kıdemsiz denetçiye',
            'B': 'Yönetim kuruluna',
            'C': 'Kamu Gözetimi Kurumuna',
            'D': 'Denetlenen şirketin iç denetim birimine ve iç denetim komitesine',
            'E': 'Sorumlu denetçiye',
        },
        'E',
        'Sorumlu denetçi, denetimde kalite yönetimine ve denetimin kalitesinin sağlanmasına ilişkin genel sorumluluğu üstlenir.',
    ),
    # düzey 2
    '0058': patch(
        "BDS 210'a göre denetim sözleşmesine eklenebilecek hususlardan biri aşağıdakilerden hangisi değildir?",
        {
            'A': 'Olumlu görüş verileceği taahhüdü',
            'B': 'Yazılı beyan alınacağı',
            'C': 'Denetimin planlanması ve yürütülmesine ilişkin düzenlemeler',
            'D': 'Ücret ve faturalama düzenlemeleri',
            'E': 'Önceki denetçiyle yapılacak görüşmelere ilişkin düzenlemeler',
        },
        'A',
        'Sözleşme planlama düzenlemeleri, yazılı beyanlar, ücret ve faturalama ile önceki denetçiyle iletişim gibi hususları içerebilir. Görüşün türü önceden taahhüt edilemez.',
    ),
    # düzey 2
    '0059': patch(
        'Geleneksel genel kabul görmüş denetim standartları sınıflamasına göre aşağıdakilerden hangisi çalışma alanı standartları kapsamındadır?',
        {
            'A': 'Muhasebe ilkelerine uygunluğun raporda belirtilmesi',
            'B': 'Bağımsızlık',
            'C': 'Yeterli ve uygun kanıt toplanması',
            'D': 'Görüşün açıkça bildirilmesi',
            'E': 'Mesleki eğitim ve yeterlilik',
        },
        'C',
        'Çalışma alanı standartları; işin planlanması ve gözetimi, iç kontrolün anlaşılması ve yeterli kanıt toplanmasıdır. Eğitim-yeterlilik ve bağımsızlık genel standartlar, görüş bildirme raporlama standartlarıdır.',
    ),
    # düzey 3
    '0060': patch(
        'Denetim kuruluşunun toplam gelirinin önemli bir bölümü tek bir denetim müşterisinden elde edilmektedir.\n\nBu durum esas olarak hangi tehdidi oluşturur?',
        {
            'A': 'Kişisel çıkar',
            'B': 'Taraf tutma',
            'C': 'Kendi çalışmasını denetleme',
            'D': 'Mesleki yeterlilik ve özen eksikliği',
            'E': 'Yakınlık',
        },
        'A',
        'Gelirin tek bir müşteriye aşırı bağımlı olması, o müşteriyi kaybetme endişesi nedeniyle kişisel çıkar tehdidi oluşturur.',
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
    print(f"1 paket / {len(PATCHES)} soru ('Denetim Standartları, Etik ve Bağımsızlık' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
