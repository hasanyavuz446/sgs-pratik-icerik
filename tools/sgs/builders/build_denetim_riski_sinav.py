#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Denetim Riski ve Önemlilik — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Denetim turu (gerçek denetim bloğu 73-88 ile ölçüldü; risk ikinci, hile BDS 240 sık sorulan alan). Paket baştan yazıldı: BDS 200, 315, 320 ve 450, 240, 300 ve 330. 2026-10-05: gerçek sınavda denetim köklerinin %46'sı olumsuz; 6 soru dört doğru ifadeli olumsuz köke çevrildi (öncüllü soruların cevabını sızdıracak ve mevcut olumsuz soruları tekrar edecek adaylar elendi).

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: BDS 200, 315, 320, 450, 240, 300, 330
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/denetim/denetim_riski.json"
STYLE_REF = 'SGS Denetim (standarda atıflı/olay kök + kısa şık; gerçek sınav profili)'
ONEK = "den-risk-gen-"


def patch(stem, options, answer, solution, ref='BDS 200; BDS 315; BDS 320; BDS 450; BDS 240; BDS 300; BDS 330'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        'Denetçi, işletmede yöneticilerin ikramiyelerinin net kâr hedefine bağlandığını ve hedefe ulaşılmasının zor göründüğünü tespit etmiştir.\n\nBu durum aşağıdakilerden hangisini artırır?',
        {
            'A': 'Kabul edilebilir denetim riskini',
            'B': 'Örneklem aralığını',
            'C': 'Önemlilik düzeyini',
            'D': 'Önemli yanlışlık riskini',
            'E': 'Tespit riskini',
        },
        'D',
        'Yönetime kâr hedefi yönünde baskı ya da teşvik oluşması yönetimin taraflılığına ve hileye açıklığı, dolayısıyla önemli yanlışlık riskini artırır.',
    ),
    # düzey 3
    '0002': patch(
        'Bir şirketin iç kontrol sistemi zayıf olduğundan denetçi kontrollere güvenmemeye karar vermiş ve kontrol riskini en yüksek düzeyde değerlendirmiştir.\n\nBu kararın sonucu aşağıdakilerden hangisidir?',
        {
            'A': 'Maddi doğrulamaya gerek kalmaz',
            'B': 'Kontrol testleri ağırlaştırılır',
            'C': 'Maddi doğrulama prosedürleri genişletilir',
            'D': 'Denetim riski hedefi artırılır',
            'E': 'Tespit riski yükseltilir',
        },
        'C',
        'Kontrol riski en yüksek düzeydeyse kabul edilebilir tespit riski düşer; denetçi kontrollere dayanmadan daha kapsamlı maddi doğrulama prosedürleri uygular.',
    ),
    # düzey 3
    '0003': patch(
        "I. Kontrol testleri\nII. Ayrıntı testleri\nIII. Maddi doğrulama amaçlı analitik prosedürler\n\nBDS 330'a göre yukarıdakilerden hangileri maddi doğrulama prosedürüdür?",
        {
            'A': 'Yalnız I',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'I ve III',
            'E': 'I, II ve III',
        },
        'B',
        'Maddi doğrulama prosedürleri ayrıntı testlerinden ve maddi doğrulama amaçlı analitik prosedürlerden oluşur; kontrol testleri kontrollerin işleyiş etkinliğini değerlendirir.',
    ),
    # düzey 3
    '0004': patch(
        "Bir şirkette muhasebe, nakit tahsilat ve banka mutabakatı görevlerinin tamamı tek bir çalışan tarafından yürütülmektedir.\n\nBDS 240'a göre bu durum hangi risk faktörü grubuna örnektir?",
        {
            'A': 'Tespit riski',
            'B': 'İş riski',
            'C': 'Teşvik ve baskı',
            'D': 'Tutum ve bahaneler',
            'E': 'Fırsat',
        },
        'E',
        'Görevlerin ayrılmamış olması gibi iç kontrol zayıflıkları hile işlenmesi için fırsat oluşturur.',
    ),
    # düzey 2
    '0005': patch(
        "BDS 320'ye göre performans önemliliği ile ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Bütün için önemlilikten daha yüksek tutulur',
            'B': 'Belirli kalemler için ayrıca belirlenebilir',
            'C': 'Denetim sırasında revize edilebilir',
            'D': 'Mesleki muhakemeyle belirlenir',
            'E': 'Toplulaştırma riskini azaltmak amacıyla belirlenir',
        },
        'A',
        'Performans önemliliği, düzeltilmemiş ve tespit edilmemiş yanlışlıkların toplamının bütün için önemliliği aşma olasılığını düşürmek amacıyla bütün için önemlilikten daha düşük bir tutar olarak belirlenir.',
    ),
    # düzey 2
    '0006': patch(
        "BDS 300'e göre planlama ile ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Sorumlu denetçi ve kilit ekip üyeleri katılır',
            'B': 'Strateji ve plan gerektiğinde güncellenir',
            'C': 'Planlama sürekli ve yinelemeli bir süreçtir',
            'D': 'Planlama tek seferlik bir aşamadır',
            'E': 'Ekip üyelerinin yönlendirilmesi planlanır',
        },
        'D',
        'Planlama denetimin ayrı bir aşaması değil, önceki denetimin tamamlanmasından sonra başlayıp denetim boyunca devam eden sürekli ve yinelemeli bir süreçtir.',
    ),
    # düzey 3
    '0007': patch(
        "İnci A.Ş.'nin denetiminde önemlilik 1.000.000 ₺, açıkça önemsiz tutar eşiği 50.000 ₺'dir. Denetçi şu yanlışlıkları tespit etmiştir: 320.000 ₺, 40.000 ₺, 180.000 ₺, 25.000 ₺, 90.000 ₺.\n\nBDS 450'ye göre biriktirilmesi gereken yanlışlıkların toplamı kaç ₺'dir?",
        {
            'A': '320.000 ₺',
            'B': '270.000 ₺',
            'C': '655.000 ₺',
            'D': '410.000 ₺',
            'E': '590.000 ₺',
        },
        'E',
        'Açıkça önemsiz eşiği (50.000 ₺) aşan yanlışlıklar biriktirilir: 320.000 ₺ + 180.000 ₺ + 90.000 ₺ = 590.000 ₺. Eşiğin altındaki yanlışlıklar biriktirilmez.',
    ),
    # düzey 3
    '0008': patch(
        "BDS 240'a göre yönetimin kontrolleri ihlal etme riskine karşı denetçinin her denetimde uyguladığı prosedürlerden biri aşağıdakilerden hangisi değildir?",
        {
            'A': 'Yevmiye kayıtlarının uygunluğunu test etmek',
            'B': 'Dönem sonu düzeltme kayıtlarını incelemek',
            'C': 'Tüm çalışanların banka hesaplarını incelemek',
            'D': 'Muhasebe tahminlerini taraflılık açısından incelemek',
            'E': 'Olağan dışı önemli işlemlerin ticari mantığını değerlendirmek',
        },
        'C',
        'Denetçi yevmiye kayıtlarını ve dönem sonu düzeltmelerini test eder, muhasebe tahminlerini taraflılık açısından gözden geçirir ve olağan işleyiş dışındaki önemli işlemlerin ticari mantığını değerlendirir.',
    ),
    # düzey 3
    '0009': patch(
        "Denetçi zayıf bir kontrol ortamı nedeniyle finansal tablo düzeyinde yüksek risk değerlendirmiştir.\n\nBDS 330'a göre bu durum prosedürlerin zamanlamasını nasıl etkiler?",
        {
            'A': 'Prosedürler dönem sonuna yakın yapılır',
            'B': 'Prosedürlerin zamanlaması önemsizdir',
            'C': 'Prosedürler ara dönemde tamamlanır',
            'D': 'Prosedürler denetim sonrasına ertelenir',
            'E': 'Prosedürler yönetimin seçtiği tarihte yapılır',
        },
        'A',
        'Zayıf kontrol ortamında denetçi ara dönem yerine dönem sonunda daha fazla prosedür uygulayabilir, maddi doğrulama kapsamını genişletebilir ve daha fazla yerde prosedür uygulayabilir.',
    ),
    # düzey 2
    '0010': patch(
        "BDS 240'a göre hile ve hata arasındaki temel ayrım aşağıdakilerden hangisidir?",
        {
            'A': 'Yanlışlığı kimin düzelttiği',
            'B': 'Yanlışlığın tespit edildiği tarih',
            'C': 'Yanlışlığın tutarı',
            'D': 'Eylemin kasıtlı olup olmaması',
            'E': 'Yanlışlığın hangi hesapta olduğu',
        },
        'D',
        'Hileyi hatadan ayıran unsur, yanlışlığa yol açan eylemin kasıtlı ya da kasıtsız olmasıdır.',
    ),
    # düzey 3
    '0011': patch(
        "Yönetim, denetçinin bildirdiği yanlışlıkların bir kısmını düzeltmeyi reddetmiştir.\n\nBDS 450'ye göre denetçinin yapması gereken aşağıdakilerden hangisidir?",
        {
            'A': 'Önemlilik düzeyini yükseltmek',
            'B': 'Hemen görüş vermekten kaçınmak',
            'C': 'Nedenlerini anlayıp etkisini değerlendirmek',
            'D': 'Düzeltilmeyen yanlışlıkları raporun ekinde ayrıntılı listelemek',
            'E': 'Denetimi yeniden başlatmak',
        },
        'C',
        'Yönetim düzeltmeyi reddederse denetçi nedenlerini anlar; düzeltilmemiş yanlışlıkların tek başına ve toplu olarak önemli olup olmadığını değerlendirirken bunu dikkate alır.',
    ),
    # düzey 2
    '0012': patch(
        "Bir hesapta, ilgili kontroller dikkate alınmadan önce yönetim beyanının önemli bir yanlışlığa açıklığı yüksek bulunmuştur.\n\nBDS 200'e göre bu açıklık hangi riski ifade eder?",
        {
            'A': 'Denetim riski',
            'B': 'Yapısal risk',
            'C': 'Tespit riski',
            'D': 'Kontrol riski',
            'E': 'Örnekleme riski',
        },
        'B',
        'Yapısal risk, ilgili kontroller dikkate alınmadan önce bir yönetim beyanının tek başına ya da diğer yanlışlıklarla birlikte önemli olabilecek bir yanlışlığa açıklığıdır.',
    ),
    # düzey 3
    '0013': patch(
        "Şirkette düşen kâr marjlarının eşlik ettiği yoğun rekabet ve pazarın doygunluğa ulaşması söz konusudur.\n\nBDS 240'a göre bu durum hileli finansal raporlamaya ilişkin hangi risk faktörü grubuna örnektir?",
        {
            'A': 'Teşvik ve baskı',
            'B': 'Fırsat',
            'C': 'Kontrol ortamı',
            'D': 'Tutum ve bahaneler',
            'E': 'Muvazaa',
        },
        'A',
        'Finansal istikrarın ya da kârlılığın ekonomik, sektörel veya faaliyet koşulları nedeniyle tehdit altında olması teşvik ve baskı grubundaki risk faktörlerine örnektir.',
    ),
    # düzey 3
    '0014': patch(
        "Tutarı önemliliğin oldukça altında olan bir yanlışlık, şirketin kredi sözleşmesindeki bir finansal oran koşulunun ihlalini gizlemektedir.\n\nBDS 450'ye göre bu yanlışlık için hangisi doğrudur?",
        {
            'A': 'Önemlilik düzeyi düşürülerek yok sayılır',
            'B': 'Gelecek yıl değerlendirilir',
            'C': 'Niteliği nedeniyle önemli sayılabilir',
            'D': 'Açıkça önemsiz kabul edilir',
            'E': 'Tutarı küçük olduğundan ihmal edilir',
        },
        'C',
        'Yanlışlığın önemliliği değerlendirilirken tutarı kadar niteliği de dikkate alınır; düzenleyici ya da sözleşmesel bir koşula uyumsuzluğu gizleyen küçük bir yanlışlık önemli sayılabilir.',
    ),
    # düzey 3
    '0015': patch(
        "Denetim sırasında şirketin gerçekleşen yıllık kârının, planlamada kullanılan tahmini kârdan önemli ölçüde düşük olduğu anlaşılmıştır.\n\nBDS 320'ye göre denetçi ne yapar?",
        {
            'A': 'Gösterge olarak hasılatı zorunlu kullanır',
            'B': 'Denetimi durdurur',
            'C': 'Önemliliği yükseltir',
            'D': 'Önemliliği yeniden belirler',
            'E': 'Planlamadaki önemliliği korur',
        },
        'D',
        'Denetim sırasında ilk önemliliği farklı belirlemesine neden olacak bilgiler edinen denetçi, önemliliği ve gerekiyorsa performans önemliliğini revize eder.',
    ),
    # düzey 2
    '0016': patch(
        "BDS 240'a göre finansal tablolardaki yanlışlıklara yol açan hile türleri aşağıdakilerden hangisinde doğru verilmiştir?",
        {
            'A': 'Hileli finansal raporlama ve kasıtsız tahmin ve muhasebe hataları',
            'B': 'Muvazaa ve sahtecilik',
            'C': 'Hileli finansal raporlama ve varlıkların kötüye kullanılması',
            'D': 'Rüşvet ve vergi kaçakçılığı',
            'E': 'Hata ve varlıkların kötüye kullanılması',
        },
        'C',
        'BDS 240 denetçiyi ilgilendiren iki tür kasıtlı yanlışlığı ele alır: hileli finansal raporlamadan ve varlıkların kötüye kullanılmasından kaynaklanan yanlışlıklar.',
    ),
    # düzey 2
    '0017': patch(
        "BDS 320 ve BDS 450'ye göre önemlilikle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Önemlilik mesleki muhakemeyle belirlenir',
            'B': 'Önemlilik denetim sırasında revize edilebilir',
            'C': 'Yanlışlığın niteliği de dikkate alınır',
            'D': 'Önemliliğin altındaki yanlışlıklar değerlendirmeye alınmaz',
            'E': 'Performans önemliliği daha düşük belirlenir',
        },
        'D',
        'Önemliliğin altındaki yanlışlıklar da biriktirilir ve toplu etkileri ile nitelikleri bakımından değerlendirilir; yalnızca açıkça önemsiz olanlar biriktirilmez.',
    ),
    # düzey 2
    '0018': patch(
        "BDS 320'ye göre bir yanlışlığın önemli kabul edilmesinin ölçütü aşağıdakilerden hangisidir?",
        {
            'A': 'Yönetimin onayına bağlı olması',
            'B': 'Kullanıcı kararlarını etkilemesinin beklenmesi',
            'C': 'Tutarının her işletme için sabit kabul edilen bir milyon lirayı aşması',
            'D': 'Vergi matrahını değiştirmesi',
            'E': 'Denetim ücretini aşması',
        },
        'B',
        'Yanlışlıklar, tek başına ya da toplu olarak kullanıcıların finansal tablolara dayanarak alacakları ekonomik kararları etkilemesi makul olarak bekleniyorsa önemlidir.',
    ),
    # düzey 3
    '0019': patch(
        "Denetçi, şirketin faaliyet gösterdiği sektörde ciddi bir daralma yaşandığını ve şirketin borç sözleşmelerindeki finansal oran koşullarını sağlamakta zorlandığını öğrenmiştir.\n\nBDS 315'e göre bu bilgi esas olarak hangi düzeyde risk göstergesidir?",
        {
            'A': 'Kontrol testi düzeyinde',
            'B': 'Finansal tablo düzeyinde',
            'C': 'Tespit riski düzeyinde',
            'D': 'Tek bir yönetim beyanı düzeyinde',
            'E': 'Örnekleme düzeyinde',
        },
        'B',
        'Sektördeki daralma ve borç koşullarına uyum güçlüğü birçok yönetim beyanını etkileyebilecek, finansal tabloların bütününe yayılan risklere işaret eder; ayrıca süreklilik ve hile risk faktörleri açısından da değerlendirilir.',
    ),
    # düzey 2
    '0020': patch(
        'Aşağıdakilerden hangisi varlıkların kötüye kullanılmasına örnek değildir?',
        {
            'A': 'Karşılıkların bilerek düşük ayrılması',
            'B': 'Şirket kaynaklarıyla kişisel harcama yapılması',
            'C': 'Satış tahsilatlarının kasiyerce zimmete geçirilmesi',
            'D': 'Stokların çalışanlarca çalınması',
            'E': 'Hayali tedarikçilere ödeme yapılması',
        },
        'A',
        'Varlıkların kötüye kullanılması işletme varlıklarının çalınmasıdır. Karşılıkların bilerek düşük ayrılması ise tabloları olduğundan iyi göstermeye yönelik hileli finansal raporlamadır.',
    ),
    # düzey 2
    '0021': patch(
        "BDS 300'e göre aşağıdakilerden hangisi denetçinin genel denetim stratejisini oluştururken dikkate alacağı hususlardan biri değildir?",
        {
            'A': 'Raporlama amaçlarını ve zamanlamayı belirlemek',
            'B': 'Ekip yönünü belirleyen önemli faktörleri dikkate almak',
            'C': 'Denetimin kapsamını belirlemek',
            'D': 'Gerekli kaynakların niteliğini belirlemek',
            'E': 'Şirketin yatırım projelerini hazırlamak',
        },
        'E',
        'Denetçi genel stratejide denetimin kapsamını, raporlama amaçlarını ve zamanlamasını, ekibin çalışmalarının yönünü belirleyen önemli faktörleri ve gerekli kaynakların niteliği, zamanlaması ve kapsamını dikkate alır. İşletmenin yatırım projelerini hazırlamak denetçinin görevi değildir.',
    ),
    # düzey 2
    '0022': patch(
        "BDS 450'ye göre denetçinin biriktirdiği yanlışlıklarla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Denetçi biriktirdiği yanlışlıkları kendisi düzeltir',
            'B': 'Denetçi denetim sırasında belirlenen yanlışlıkları biriktirir',
            'C': 'Yanlışlıklar uygun yönetim kademesine bildirilir',
            'D': 'Yanlışlıkların düzeltilmesi yönetimden talep edilir',
            'E': 'Bildirim zamanında yapılır',
        },
        'A',
        'BDS 450: denetçi, açıkça önemsiz olanlar dışında denetim sırasında belirlenen yanlışlıkları biriktirir, zamanında uygun yönetim kademesine bildirir ve düzeltilmelerini talep eder. Tabloları düzeltmek yönetimin sorumluluğudur; denetçi düzeltme yapmaz.',
    ),
    # düzey 3
    '0023': patch(
        "Gümüş A.Ş.'nin denetiminde denetçi, alacakların değerlemesi için yapısal riski %100 değerlendirmiştir. Kontrol testleri, ilgili kontrollerin kısmen etkin olduğunu göstermiş ve kontrol riski %25 olarak belirlenmiştir. Denetçi denetim riskini %5 ile sınırlamak istemektedir.\n\nKabul edilebilir tespit riski yüzde kaçtır?",
        {
            'A': '%50',
            'B': '%25',
            'C': '%20',
            'D': '%75',
            'E': '%5',
        },
        'C',
        'Tespit riski = %5 / (%100 × %25) = %5 / %25 = %20.',
    ),
    # düzey 3
    '0024': patch(
        "Denetim sırasında beklenmedik bir olay nedeniyle risk değerlendirmesi önemli ölçüde değişmiştir.\n\nBDS 300'e göre aşağıdakilerden hangisi denetçinin bu durumda yapması gerekenlerden biri değildir?",
        {
            'A': 'Genel denetim stratejisini güncellemek',
            'B': 'Değişikliği bir sonraki yılın denetimine bırakmak',
            'C': 'Denetim planını değiştirmek',
            'D': 'Ekibi yeni duruma göre yönlendirmek',
            'E': 'Değişikliği ve nedenlerini belgelemek',
        },
        'B',
        'Denetçi gerektiğinde genel stratejiyi ve denetim planını güncelleyip değiştirir, önemli değişiklikleri ve nedenlerini belgeler; ekibi buna göre yönlendirir.',
    ),
    # düzey 2
    '0025': patch(
        "BDS 200'e göre denetçinin mesleki şüphecilik göstermesiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Çelişen kanıtlara karşı uyanık olmayı gerektirir',
            'B': 'Sorgulayıcı bir zihin yapısını ifade eder',
            'C': 'Kanıtın eleştirel değerlendirilmesini gerektirir',
            'D': 'Yönetimin dürüst olmadığını varsaymayı gerektirir',
            'E': 'Belgelerin güvenilirliğini sorgulamayı içerir',
        },
        'D',
        'Mesleki şüphecilik, sorgulayıcı bir zihin yapısı ve kanıtın eleştirel değerlendirilmesidir; yönetimin dürüst olmadığını varsaymayı gerektirmez.',
    ),
    # düzey 3
    '0026': patch(
        "Denetim sırasında elde edilen yeni kanıtlar, denetçinin risk değerlendirmesinin dayandığı bilgilerle tutarsızdır.\n\nBDS 315'e göre denetçi ne yapar?",
        {
            'A': 'Görüş vermekten kaçınır',
            'B': 'Risk değerlendirmesini revize eder',
            'C': 'İlk değerlendirmeyi korur',
            'D': 'Kanıtı yok sayar',
            'E': 'Önemliliği sıfırlar',
        },
        'B',
        'Risk değerlendirmesi denetim boyunca değişebilir; yeni kanıt ilk değerlendirmeyle tutarsızsa denetçi değerlendirmeyi revize eder ve planlanan prosedürleri buna göre değiştirir.',
    ),
    # düzey 2
    '0027': patch(
        "BDS 330'a göre finansal tablo düzeyinde değerlendirilen önemli yanlışlık risklerine karşı denetçinin genel yanıtlarından biri aşağıdakilerden hangisi değildir?",
        {
            'A': 'Gözetimi artırmak',
            'B': 'Analizleri sorgusuz kabul etmek',
            'C': 'Daha deneyimli personel görevlendirmek',
            'D': 'Prosedürlere öngörülemezlik katmak',
            'E': 'Ekibe mesleki şüpheciliğin önemini vurgulamak',
        },
        'B',
        'Genel yanıtlar; mesleki şüpheciliğin vurgulanması, deneyimli ya da uzman personel görevlendirilmesi, gözetimin artırılması, prosedürlere öngörülemezlik katılması ve prosedürlerin niteliği, zamanlaması ve kapsamında genel değişikliklerdir.',
    ),
    # düzey 3
    '0028': patch(
        "Denetçi, yeni yürürlüğe giren bir muhasebe standardı nedeniyle şirketin hasılat hesaplamalarının çok sayıda varsayım ve karmaşık sözleşme yorumuna dayandığını belirlemiştir.\n\nBDS 315'e göre bu durum hangi yapısal risk faktörlerini öne çıkarır?",
        {
            'A': 'Karmaşıklık ve tespit riski',
            'B': 'Belirsizlik ve iş riski',
            'C': 'Değişim ve örnekleme riski',
            'D': 'Kontrol riski ve belirsizlik',
            'E': 'Karmaşıklık ve değişim',
        },
        'E',
        'Yeni bir standardın uygulanması değişim, çok sayıda varsayım ve karmaşık sözleşme yorumu karmaşıklık faktörünü öne çıkarır.',
    ),
    # düzey 2
    '0029': patch(
        "BDS 315'e göre önemli riskle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Yapısal risk yelpazesinin üst ucuna yakın değerlendirilir',
            'B': 'Önemlilik tutarını aşan her yanlışlık önemli risktir',
            'C': 'Yanlışlığın olasılığı ve büyüklüğü birlikte dikkate alınır',
            'D': 'Yönetimin önemli bulması tek başına belirleyici değildir',
            'E': 'Değerlendirmede yapısal risk faktörleri esas alınır',
        },
        'B',
        'BDS 315: önemli risk, yapısal risk faktörlerinin yanlışlığın olasılığını ve büyüklüğünü etkileme derecesi nedeniyle yapısal riskin yelpazenin üst ucuna yakın değerlendirildiği risktir. Bir yanlışlığın tutarı önemliliği aşıyor olması onu önemli risk yapmaz; değerlendirme yönetimin görüşüne de bırakılmaz.',
    ),
    # düzey 2
    '0030': patch(
        "BDS 300'e göre aşağıdakilerden hangisi denetim planında yer alan unsurlardan biri değildir?",
        {
            'A': 'Denetim ücretinin tahsil takvimi',
            'B': 'Risk değerlendirme prosedürlerinin niteliği ve kapsamı',
            'C': 'İleri denetim prosedürlerinin zamanlaması',
            'D': 'Yönetim beyanı düzeyinde planlanan prosedürler',
            'E': 'Diğer planlanan denetim prosedürleri',
        },
        'A',
        'Denetim planı; planlanan risk değerlendirme prosedürlerinin, yönetim beyanı düzeyindeki ileri denetim prosedürlerinin niteliğini, zamanlamasını ve kapsamını ve diğer planlanan prosedürleri içerir. Ücretin tahsili denetim planının konusu değildir.',
    ),
    # düzey 2
    '0031': patch(
        "BDS 200'e göre aşağıdakilerden hangisi denetimin yapısal kısıtlarından biri değildir?",
        {
            'A': 'Denetçinin bağımsız olması',
            'B': 'Yönetimin bilgi saklayabilmesi',
            'C': 'Finansal raporlamada muhakeme kullanılması',
            'D': 'Makul süre ve maliyet sınırı',
            'E': 'Hileyi gizlemeye yönelik muvazaa',
        },
        'A',
        'Yapısal kısıtlar; finansal raporlamanın niteliğinden (muhakeme ve tahminler), prosedürlerin niteliğinden (bilgi saklama, muvazaa, sahtecilik) ve makul süre ve maliyet sınırından kaynaklanır. Bağımsızlık bir kısıt değil, denetimin ön koşuludur.',
    ),
    # düzey 2
    '0032': patch(
        "BDS 330'a göre ileri denetim prosedürlerinin tasarlanmasında prosedürlerin niteliği, zamanlaması ve kapsamı neye göre belirlenir?",
        {
            'A': 'Denetim ücretine göre',
            'B': 'Ekip üyelerinin tercihine göre',
            'C': 'Yönetimin isteğine göre',
            'D': 'Değerlendirilen risklere göre',
            'E': 'Önceki yılın prosedürlerinin aynısı olarak',
        },
        'D',
        'Denetçi ileri denetim prosedürlerini, yönetim beyanı düzeyinde değerlendirilen önemli yanlışlık risklerine karşılık verecek şekilde tasarlar ve uygular.',
    ),
    # düzey 3
    '0033': patch(
        "Denetçi, satış hasılatı için yapısal riski %80, kontrol riskini %50 olarak değerlendirmiştir. Kabul edilebilir denetim riski %4'tir.\n\nDenetim riski modeline göre kabul edilebilir tespit riski yüzde kaçtır?",
        {
            'A': '%60',
            'B': '%40',
            'C': '%10',
            'D': '%8',
            'E': '%5',
        },
        'C',
        'Denetim riski = yapısal risk × kontrol riski × tespit riski. Tespit riski = %4 / (%80 × %50) = %10.',
    ),
    # düzey 3
    '0034': patch(
        "Bir bankanın finansal tablolarında üst yönetime yapılan ödemeler, toplam tutarı önemlilik düzeyinin altında olmasına rağmen kullanıcılar için özel önem taşımaktadır.\n\nBDS 320'ye göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Bu açıklama için daha düşük bir önemlilik belirlenebilir',
            'B': 'Bütün için önemlilik yükseltilir',
            'C': 'Kullanıcılar için özel önem taşıyan kalemler dikkate alınır',
            'D': 'Kalem denetim dışında bırakılmaz',
            'E': 'Bütün için önemliliğin altındaki yanlışlıklar da önemli olabilir',
        },
        'B',
        'BDS 320: belirli işlem sınıfları, hesap bakiyeleri veya açıklamalarda bütün için önemliliğin altındaki yanlışlıkların da kullanıcı kararlarını etkilemesi bekleniyorsa denetçi bu kalemler için daha düşük önemlilik düzeyleri belirler. Bütün için önemliliği yükseltmek bu amaçla bağdaşmaz.',
    ),
    # düzey 2
    '0035': patch(
        "BDS 315'e göre aşağıdakilerden hangisi denetçinin işletmeyi ve çevresini anlarken elde ettiği bilgilerden biri değildir?",
        {
            'A': 'Finansal performansın ölçülmesi',
            'B': 'Sektör ve düzenleyici faktörler',
            'C': 'İşletmenin yapısı ve faaliyetleri',
            'D': 'Denetçinin diğer müşterilerinin sonuçları',
            'E': 'Uygulanan finansal raporlama çerçevesi',
        },
        'D',
        'Denetçi işletmenin organizasyon yapısını, iş modelini, sektörünü, düzenleyici çevresini, finansal performans ölçütlerini ve raporlama çerçevesini anlar. Diğer müşterilerin bilgileri gizlilik kapsamındadır.',
    ),
    # düzey 3
    '0036': patch(
        "Denetçi, üst yönetimin hileli finansal raporlamaya karıştığına dair kanıt elde etmiştir.\n\nBDS 240'a göre bu durumda denetçi aşağıdakilerden hangisini yapar?",
        {
            'A': 'Üst yönetimden sorumlu olanlara bildirir',
            'B': 'Rapor tarihini geriye alır',
            'C': 'Konuyu muhasebe müdürüyle görüşür',
            'D': 'Yanlışlığı kendisi düzeltir',
            'E': 'Bulguyu belgelemeden sözleşmeyi sürdürür',
        },
        'A',
        'Hile yönetimi, iç kontrolde önemli rolü olan çalışanları ya da önemli yanlışlığa yol açan diğer kişileri içeriyorsa denetçi konuyu zamanında üst yönetimden sorumlu olanlara bildirir; ayrıca sözleşmeyi sürdürmenin uygunluğunu değerlendirir.',
    ),
    # düzey 2
    '0037': patch(
        "BDS 240'a göre hasılatın muhasebeleştirilmesinde hile riski bulunduğu karinesiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Denetçi hasılatta hile riski bulunduğunu varsayar',
            'B': 'Karine belirli durumlarda çürütülebilir',
            'C': 'Çürütme gerekçesi belgelenir',
            'D': 'Karine halka açık şirketlerle sınırlı değildir',
            'E': 'Karine yönetimin beyanıyla çürütülür',
        },
        'E',
        'BDS 240: denetçi hasılatın muhasebeleştirilmesinde hile riski bulunduğunu varsayar; bu karineyi kendi değerlendirmesiyle çürüttüğü sonucuna varırsa gerekçelerini belgeler. Karine işletme türüyle sınırlı değildir ve yönetimin beyanı onu çürütmeye yetmez.',
    ),
    # düzey 2
    '0038': patch(
        "BDS 315'e göre aşağıdakilerden hangisi risk değerlendirme prosedürlerinden biri değildir?",
        {
            'A': 'Gözlem',
            'B': 'Yönetimin sorgulanması',
            'C': 'Tetkik',
            'D': 'Dış teyit gönderilmesi',
            'E': 'Analitik prosedürler',
        },
        'D',
        'Risk değerlendirme prosedürleri yönetimin ve diğer kişilerin sorgulanmasını, analitik prosedürleri, gözlem ve tetkiki içerir. Dış teyit ileri denetim prosedürü olarak kullanılır.',
    ),
    # düzey 2
    '0039': patch(
        "BDS 315'e göre aşağıdakilerden hangisi yapısal risk faktörlerinden biri değildir?",
        {
            'A': 'Belirsizlik',
            'B': 'Sübjektiflik',
            'C': 'Yönetimin taraflılığına açıklık',
            'D': 'Denetim ücretinin düşüklüğü',
            'E': 'Karmaşıklık',
        },
        'D',
        'Yapısal risk faktörleri; karmaşıklık, sübjektiflik, değişim, belirsizlik ve yönetimin taraflılığına veya diğer hile risk faktörlerine açıklıktır.',
    ),
    # düzey 2
    '0040': patch(
        "BDS 240'a göre aşağıdakilerden hangisi standardın amaçlarından biri değildir?",
        {
            'A': 'Bu risklere uygun karşılık vererek kanıt elde etmek',
            'B': 'Hile şüphesine uygun biçimde karşılık vermek',
            'C': 'Tespit edilen hileye uygun karşılık vermek',
            'D': 'Hile kaynaklı önemli yanlışlık risklerini belirlemek',
            'E': 'Hileyi önlemek ve işletmede ortadan kaldırmak',
        },
        'E',
        'Denetçinin amaçları; hile kaynaklı önemli yanlışlık risklerini belirlemek ve değerlendirmek, bunlara karşılık vererek yeterli kanıt elde etmek ve tespit edilen hile ya da şüpheye uygun karşılık vermektir. Hileyi önlemek öncelikle yönetimin sorumluluğudur.',
    ),
    # düzey 2
    '0041': patch(
        "BDS 300'e göre genel denetim stratejisiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Denetimin kapsamını belirler',
            'B': 'Denetimin zamanlamasını belirler',
            'C': 'Denetimin yönünü belirler',
            'D': 'Denetim planının geliştirilmesine rehberlik eder',
            'E': 'Denetim planı tamamlandıktan sonra hazırlanır',
        },
        'E',
        'BDS 300: genel denetim stratejisi denetimin kapsamını, zamanlamasını ve yönünü belirler ve denetim planının geliştirilmesine rehberlik eder. Bu nedenle strateji plandan önce oluşturulur; ikisi denetim boyunca güncellenebilir.',
    ),
    # düzey 2
    '0042': patch(
        "BDS 200'e göre denetim riski bileşenlerinden hangisi denetçinin uyguladığı prosedürlerin niteliği, zamanlaması ve kapsamıyla doğrudan yönetilebilir?",
        {
            'A': 'Tespit riski',
            'B': 'Yapısal risk',
            'C': 'Kontrol riski',
            'D': 'İş riski',
            'E': 'Önemli yanlışlık riski',
        },
        'A',
        'Yapısal risk ve kontrol riski işletmeye aittir ve denetimden bağımsız olarak vardır; denetçi bunları değerlendirir. Tespit riski ise denetçinin prosedürleriyle yönetilir.',
    ),
    # düzey 3
    '0043': patch(
        'Denetçi, düzeltilmemiş yanlışlıkların toplamının önemliliğe yaklaştığını görmüştür.\n\nBu durumun anlamı aşağıdakilerden hangisidir?',
        {
            'A': 'Denetim riski sıfırlanmıştır',
            'B': 'Örneklem küçültülebilir',
            'C': 'Önemliliğin aşılma olasılığı artar',
            'D': 'Önemlilik aşılmadığı için risk yoktur',
            'E': 'Performans önemliliği yükseltilmelidir',
        },
        'C',
        'Düzeltilmemiş yanlışlıklar önemliliğe yaklaştıkça, tespit edilmemiş yanlışlıklarla birlikte toplamın önemliliği aşma riski kabul edilebilir düzeyin üstüne çıkabilir; denetçi ek prosedürler uygulayabilir ya da düzeltme isteyebilir.',
    ),
    # düzey 3
    '0044': patch(
        'Denetçi, alacaklarda önemli yanlışlık riskini önceki planına göre daha yüksek değerlendirmiştir; kabul edilebilir denetim riski değişmemiştir.\n\nBu durumun kabul edilebilir tespit riski ve toplanacak kanıt üzerindeki etkisi aşağıdakilerden hangisidir?',
        {
            'A': 'Tespit riski düşer – Kanıt azalır',
            'B': 'Tespit riski düşer – Kanıt artar',
            'C': 'Tespit riski artar – Kanıt artar',
            'D': 'Tespit riski artar – Kanıt azalır',
            'E': 'Tespit riski değişmez – Kanıt artar',
        },
        'B',
        'Önemli yanlışlık riski arttıkça kabul edilebilir tespit riski düşer; daha düşük tespit riski için denetçi daha ikna edici kanıt toplar.',
    ),
    # düzey 2
    '0045': patch(
        "BDS 240'a göre denetçinin hileye ilişkin olarak yönetimden sorgulaması gereken konulardan biri aşağıdakilerden hangisi değildir?",
        {
            'A': 'Bildiği ya da şüphelendiği hileler',
            'B': 'Hile riskine ilişkin değerlendirmesi',
            'C': 'Çalışanlara iş etiğine ilişkin yaptığı iletişim',
            'D': 'Rakip firmaların hile vakaları',
            'E': 'Hile risklerini belirleme süreci',
        },
        'D',
        'Denetçi yönetimi; hile riskine ilişkin değerlendirmesi, bu riskleri belirleme ve karşılık verme süreci, üst yönetime bu konudaki iletişimi, çalışanlara iş uygulamaları ve etik davranışa ilişkin iletişimi ve bildiği hileler hakkında sorgular.',
    ),
    # düzey 2
    '0046': patch(
        "BDS 240'a göre hileden kaynaklanan önemli yanlışlığın tespit edilememe riski, hatadan kaynaklananınkinden daha yüksektir.\n\nBunun nedenleriyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Hile belgelerde sahtecilik içerebilir',
            'B': 'Hile birden fazla kişinin muvazaasını içerebilir',
            'C': 'Hile gizlemeye yönelik ayrıntılı planlar içerebilir',
            'D': 'Hile denetçiye yanlış beyan verilmesini içerebilir',
            'E': 'Hile tutarları hatalardan daha küçüktür',
        },
        'E',
        'BDS 240: hile; sahtecilik, kayıtların bilerek atlanması, muvazaa ve denetçiye kasıtlı yanlış beyan gibi gizlemeye yönelik ayrıntılı planlar içerebildiğinden tespit edilememe riski hatadan daha yüksektir. Bu farkın nedeni tutarların küçüklüğü değildir.',
    ),
    # düzey 3
    '0047': patch(
        "Denetçi, yönetimin yazılı beyanlarının gerçeği yansıtmadığını gösteren bir hile tespit etmiştir.\n\nBDS 240'a göre bu durumun denetime etkisi aşağıdakilerden hangisidir?",
        {
            'A': 'Önemlilik yükseltilir',
            'B': 'Diğer kanıtların güvenilirliği sorgulanır',
            'C': 'Beyanlar daha güvenilir sayılır',
            'D': 'Bulgu ilgili hesapla sınırlı kalır, diğer alanlar etkilenmez',
            'E': 'Denetim riski düşer',
        },
        'B',
        'Tespit edilen hile yönetimin katılımını gösteriyorsa denetçi, değerlendirilen riskleri ve diğer yönetim beyanlarıyla elde edilen kanıtların güvenilirliğini yeniden değerlendirir.',
    ),
    # düzey 2
    '0048': patch(
        "BDS 315'e göre denetim ekibi üyeleri arasında yapılan görüşmeyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Sorumlu denetçi ve kilit ekip üyeleri katılır',
            'B': 'Tabloların önemli yanlışlığa açıklığı görüşülür',
            'C': 'Görüşmenin amacı denetim ücretini paylaştırmaktır',
            'D': 'Raporlama çerçevesinin uygulanışı görüşülür',
            'E': 'Hile kaynaklı yanlışlığa açıklık da ele alınır',
        },
        'C',
        'BDS 315 (ve BDS 240): sorumlu denetçi ve kilit ekip üyeleri, uygulanacak finansal raporlama çerçevesinin uygulanışını ve finansal tabloların hile ya da hata kaynaklı önemli yanlışlığa açıklığını görüşür.',
    ),
    # düzey 2
    '0049': patch(
        "BDS 240'a göre aşağıdakilerden hangisi yönetimin kontrolleri ihlal ederek hile yapma yöntemlerinden biri değildir?",
        {
            'A': 'Satış faturasına yanlışlıkla eksik tutar yazılması',
            'B': 'Önemli işlemlerin dipnotlarda gizlenmesi',
            'C': 'Dönem sonuna yakın hayali yevmiye kaydı yapılması',
            'D': 'Hasılatın kasıtlı olarak erken muhasebeleştirilmesi',
            'E': 'Tahminlerde kullanılan varsayımların kasıtlı değiştirilmesi',
        },
        'A',
        'Hayali yevmiye kayıtları, tahmin varsayımlarının kasıtlı değiştirilmesi, işlemlerin gizlenmesi ve hasılatın erken muhasebeleştirilmesi kontrollerin ihlal edilmesiyle yapılan hilelerdir. Yanlışlıkla yapılan bir tutar hatası kasıt içermediğinden hatadır.',
    ),
    # düzey 3
    '0050': patch(
        "I. Yapısal risk\nII. Kontrol riski\nIII. Tespit riski\n\nBDS 200'e göre yukarıdakilerden hangileri denetimden bağımsız olarak işletmede bulunan risklerdir?",
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'Yalnız I',
        },
        'A',
        'Yapısal risk ve kontrol riski işletmeye özgüdür ve finansal tabloların denetiminden bağımsız olarak vardır. Tespit riski denetçinin prosedürleriyle ilgilidir.',
    ),
    # düzey 3
    '0051': patch(
        'Denetçi stok hesabı için önemli yanlışlık riskini %40 değerlendirmiş ve %10 tespit riskini kabul edilebilir bulmuştur.\n\nBu durumda planlanan denetim riski yüzde kaçtır?',
        {
            'A': '%30',
            'B': '%4',
            'C': '%14',
            'D': '%50',
            'E': '%25',
        },
        'B',
        'Denetim riski = önemli yanlışlık riski × tespit riski = %40 × %10 = %4.',
    ),
    # düzey 2
    '0052': patch(
        "BDS 200'e göre tespit riski ile ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Yeterli kanıtla sıfıra indirilebilir',
            'B': 'Denetimin yapısal kısıtları nedeniyle vardır',
            'C': 'Önemli yanlışlık riskiyle ters ilişkilidir',
            'D': 'Kabul edilebilir düzeyi denetçi belirler',
            'E': 'Denetçinin prosedürleriyle yönetilir',
        },
        'A',
        'Tespit riski azaltılabilir ancak denetimin yapısal kısıtları nedeniyle sıfıra indirilemez; dolayısıyla bir miktar tespit riski her zaman bulunur.',
    ),
    # düzey 3
    '0053': patch(
        "Şirkette denetim prosedürlerine aşina olan kişilerin hileli raporlamayı daha iyi gizleyebileceği değerlendirilmiştir.\n\nBDS 240'a göre denetçi bu nedenle prosedürlerin seçimine hangi unsuru katar?",
        {
            'A': 'Örnekleme aralığı',
            'B': 'Önemlilik eşiği',
            'C': 'Kontrol riski artışı',
            'D': 'Öngörülemezlik',
            'E': 'Dış teyit muafiyeti',
        },
        'D',
        'Denetçi, uygulanacak prosedürlerin niteliğinin, zamanlamasının ve kapsamının seçimine öngörülemezlik unsuru katar; örneğin önceden haber verilmeyen yerlerde sayım yapar.',
    ),
    # düzey 2
    '0054': patch(
        "Yöneticilere belirli bir kâr hedefine ulaşıldığında ikramiye ödenmesi BDS 240'a göre hangi hile risk faktörü grubunda yer alır?",
        {
            'A': 'Varlıkların kötüye kullanılması',
            'B': 'Fırsat',
            'C': 'Teşvik ve baskı',
            'D': 'Tutum ve bahaneler',
            'E': 'Yapısal kısıt',
        },
        'C',
        'Yönetimin ücretlendirmesinin önemli bir bölümünün finansal sonuçlara bağlı olması, hileli finansal raporlama için teşvik ve baskı oluşturan bir risk faktörüdür.',
    ),
    # düzey 3
    '0055': patch(
        "Hazar A.Ş.'nin vergi öncesi kârı 40.000.000 ₺'dir. Denetçi finansal tabloların bütünü için önemliliği vergi öncesi kârın %5'i, performans önemliliğini ise bu tutarın %75'i olarak belirlemiştir.\n\nPerformans önemliliği kaç ₺'dir?",
        {
            'A': '1.500.000 ₺',
            'B': '500.000 ₺',
            'C': '2.000.000 ₺',
            'D': '30.000.000 ₺',
            'E': '3.000.000 ₺',
        },
        'A',
        'Önemlilik 40.000.000 ₺ × %5 = 2.000.000 ₺. Performans önemliliği 2.000.000 ₺ × %75 = 1.500.000 ₺.',
    ),
    # düzey 2
    '0056': patch(
        "BDS 200'e göre denetim riski aşağıdaki bileşenlerden hangilerinden oluşur?",
        {
            'A': 'Önemlilik ve örnekleme riski',
            'B': 'Yapısal risk ve iş riski',
            'C': 'Tespit riski ve iş riski',
            'D': 'Önemli yanlışlık riski ve tespit riski',
            'E': 'Kontrol riski ve örnekleme riski',
        },
        'D',
        'Denetim riski, önemli yanlışlık riski ile tespit riskinin bir fonksiyonudur; önemli yanlışlık riski de yapısal risk ve kontrol riskinden oluşur.',
    ),
    # düzey 3
    '0057': patch(
        "I. Hasılatın muhasebeleştirilmesindeki hile riski\nII. Yönetimin kontrolleri ihlal etme riski\nIII. Kasa sayım farkları\n\nBDS 240'a göre yukarıdakilerden hangileri her denetimde önemli risk olarak ele alınır veya karine olarak var sayılır?",
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'A',
        'Hasılatın muhasebeleştirilmesinde hile riski bulunduğu karine olarak kabul edilir (gerekçelendirilerek çürütülebilir); yönetimin kontrolleri ihlal etme riski ise her işletmede bulunan önemli bir risktir.',
    ),
    # düzey 3
    '0058': patch(
        "Denetçi, önceki yıl test ettiği ve o tarihten beri değişmeyen bir kontrole bu yıl da dayanmayı planlamaktadır; kontrol önemli bir riskle ilgili değildir.\n\nBDS 330'a göre denetçi bu kontrolü en geç hangi sıklıkla test etmelidir?",
        {
            'A': 'Her beş denetimde bir kez',
            'B': 'Her denetimde',
            'C': 'Her üç denetimde en az bir kez',
            'D': 'Kontrolde değişiklik olursa',
            'E': 'Yönetim talep ettiğinde',
        },
        'C',
        'Değişmemiş kontrollere ilişkin önceki denetim kanıtına dayanılıyorsa bu kontroller her üç denetimde en az bir kez test edilir; önemli riskle ilgili kontroller ise cari dönemde test edilir.',
    ),
    # düzey 3
    '0059': patch(
        "Denetçi bir depo sorumlusunun küçük tutarlı stokları zimmetine geçirdiğini tespit etmiştir; tutar önemli değildir ve yönetimin katılımı yoktur.\n\nBDS 240'a göre denetçi ne yapar?",
        {
            'A': 'Çalışanla ödeme planı yapar',
            'B': 'Doğrudan savcılığa bildirir',
            'C': 'Görüş vermekten kaçınır',
            'D': 'Önemli olmadığı için kayıt dışı bırakır',
            'E': 'Uygun yönetim kademesine bildirir',
        },
        'E',
        'Denetçi hileyi tespit ettiğinde ya da hile bulunduğuna işaret eden bilgi elde ettiğinde, hileyi önleme ve tespit etme sorumluluğu taşıyanların dikkatine sunmak için konuyu zamanında uygun yönetim kademesine bildirir.',
    ),
    # düzey 2
    '0060': patch(
        "BDS 320'ye göre aşağıdakilerden hangisi önemliliğin belirlenmesinde gösterge olarak kullanılabilecek tutarlardan biri değildir?",
        {
            'A': 'Toplam hasılat',
            'B': 'Denetim ücreti',
            'C': 'Özkaynaklar',
            'D': 'Toplam giderler',
            'E': 'Vergi öncesi kâr',
        },
        'B',
        'Uygun göstergeler vergi öncesi kâr, toplam hasılat, brüt kâr, toplam giderler, özkaynaklar ya da net varlık değeri gibi tutarlardır.',
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
    print(f"1 paket / {len(PATCHES)} soru ('Denetim Riski ve Önemlilik' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
