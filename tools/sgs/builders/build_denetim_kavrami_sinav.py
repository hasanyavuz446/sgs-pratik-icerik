#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Denetim Kavramı, Türleri ve Denetçi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Denetim turu (gerçek denetim bloğu 73-88 ile ölçüldü). Paket baştan yazıldı: denetimin tanımı ve bilgi riski, yapısal kısıtlar, denetim türleri, iç denetim, güvence hizmetleri, denetim süreci ve risk odaklı yaklaşım, önemlilik ve toplulaştırma riski, tamamlama aşaması, TTK ve KGK, hata-hile. 2026-10-05: 4 soru dört doğru ifadeli olumsuz köke çevrildi (gerçek sınavda denetim köklerinin %46'sı olumsuz).

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: BDS 200, 320; Güvence Denetimi Standartları; TTK m.397-399; 660 sayılı KHK
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/denetim/denetim_kavrami.json"
STYLE_REF = 'SGS Denetim (standarda atıflı/olay kök + kısa şık; gerçek sınav profili)'
ONEK = "den-kavram-gen-"


def patch(stem, options, answer, solution, ref='BDS 200; BDS 320; TTK m.397-399; KGK'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Güvence denetimi raporunda yer alması gereken asgari unsurlardan biri aşağıdakilerden hangisi değildir?',
        {
            'A': 'Konu bilgisi ve uygulanan ölçütlerin açıklaması',
            'B': 'Sonuç ifadesi',
            'C': 'Muhatap',
            'D': 'Denetim ekibinin ücret dağılımı',
            'E': 'Başlık',
        },
        'D',
        'Güvence raporunda başlık, muhatap, konu bilgisi, ölçütler, tarafların sorumlulukları, uygulanan standartlar, sonuç, imza, tarih ve yer bulunur; ücret dağılımı yer almaz.',
    ),
    # düzey 3
    '0002': patch(
        'I. Finansal tabloları hazırlamak\nII. İç kontrolü tasarlamak\nIII. Tablolar hakkında görüş vermek\n\nYukarıdakilerden hangileri yönetimin sorumluluğundadır?',
        {
            'A': 'Yalnız I',
            'B': 'I, II ve III',
            'C': 'II ve III',
            'D': 'I ve III',
            'E': 'I ve II',
        },
        'E',
        'Tabloların hazırlanması ve iç kontrolün tasarlanması yönetimin, tablolar hakkında görüş vermek ise denetçinin sorumluluğundadır.',
    ),
    # düzey 2
    '0003': patch(
        'Bir meslek mensubunun, işletme yönetiminin sağladığı bilgilerle finansal tabloları hazırlamasına yardım ettiği ve güvence vermediği hizmet aşağıdakilerden hangisidir?',
        {
            'A': 'Sınırlı bağımsız denetim',
            'B': 'Bağımsız denetim',
            'C': 'Derleme hizmeti',
            'D': 'Üzerinde mutabık kalınan prosedürler',
            'E': 'İç denetim',
        },
        'C',
        'Derleme hizmetinde meslek mensubu finansal bilginin hazırlanmasında ve sunulmasında yönetime yardım eder; güvence vermez.',
    ),
    # düzey 2
    '0004': patch(
        'Bir işletmenin üretim biriminin kaynakları etkin ve verimli kullanıp kullanmadığının araştırılması hangi denetim türüdür?',
        {
            'A': 'Bağımsız denetim',
            'B': 'Faaliyet denetimi',
            'C': 'Kamu denetimi',
            'D': 'Uygunluk denetimi',
            'E': 'Finansal tablo denetimi',
        },
        'B',
        'Faaliyet (performans) denetimi, bir birimin ya da faaliyetin etkinliğini ve verimliliğini değerlendirip iyileştirme önerileri sunar.',
    ),
    # düzey 3
    '0005': patch(
        'Bir yatırımcı, yatırım yapmayı düşündüğü şirketin finansal tablolarını şirket yönetiminin hazırladığını ve yönetimin sonuçları iyi gösterme eğiliminde olabileceğini düşünmektedir.\n\nBu endişe bağımsız denetime talep yaratan hangi kavramla açıklanır?',
        {
            'A': 'Tespit riski',
            'B': 'Kontrol riski',
            'C': 'Örnekleme riski',
            'D': 'İş riski',
            'E': 'Bilgi riski',
        },
        'E',
        'Bilgi riski, karar vermede kullanılan bilginin yanlış olma olasılığıdır; bilgi kaynağının uzaklığı, hazırlayanın taraflılığı, veri hacmi ve işlemlerin karmaşıklığı bu riski artırır. Bağımsız denetim bilgi riskini azaltır.',
    ),
    # düzey 2
    '0006': patch(
        'Bir şirketin finansal tablolarında kullanılan önceden belirlenmiş ölçütlere örnek aşağıdakilerden hangisidir?',
        {
            'A': 'Türkiye Finansal Raporlama Standartları',
            'B': 'Rakip şirketlerin sonuçları',
            'C': 'Denetçinin çalışma kâğıtları',
            'D': 'Yönetim kurulunun onayladığı yıllık bütçe hedefleri',
            'E': 'Şirketin ürün kataloğu',
        },
        'A',
        'Finansal tablo denetiminde ölçüt, uygulanacak finansal raporlama çerçevesidir; TFRS ya da BOBİ FRS buna örnektir.',
    ),
    # düzey 3
    '0007': patch(
        'Bir belediyenin harcamalarının ilgili mevzuata uygun yapılıp yapılmadığını kamu adına görevli denetçiler incelemektedir.\n\nBu denetim, konusuna ve denetçinin statüsüne göre sırasıyla nasıl sınıflanır?',
        {
            'A': 'Faaliyet denetimi – Kamu denetimi',
            'B': 'Finansal tablo denetimi – Kamu denetimi',
            'C': 'Uygunluk denetimi – Kamu denetimi',
            'D': 'Faaliyet denetimi – Bağımsız denetim',
            'E': 'Uygunluk denetimi – İç denetim',
        },
        'C',
        'Mevzuata uygunluğun araştırılması uygunluk denetimi, kamu adına görevli denetçilerce yapılması kamu denetimidir.',
    ),
    # düzey 3
    '0008': patch(
        "Türk Ticaret Kanunu'na göre bağımsız denetime tabi olduğu hâlde denetlenmeyen bir şirketin finansal tabloları ve yıllık faaliyet raporu için aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Geçerliliğini korur',
            'B': 'Düzenlenmemiş hükmündedir',
            'C': 'Vergi dairesine verilerek geçerlilik kazanır',
            'D': 'Bir yıl içinde denetlenirse geçerlidir',
            'E': 'Genel kurul onayıyla geçerlidir',
        },
        'B',
        "TTK 397'ye göre denetime tabi olup da denetlenmemiş finansal tablolar ve yönetim kurulunun yıllık faaliyet raporu düzenlenmemiş hükmündedir.",
    ),
    # düzey 3
    '0009': patch(
        "Denetçi seçildikten sonra Türk Ticaret Kanunu'na göre yönetim kurulunun yapması gereken aşağıdakilerden hangisidir?",
        {
            'A': 'Denetçiye görüş türünü bildirmek',
            'B': 'Denetçinin raporunu önceden onaylamak',
            'C': 'Denetçiyi kendi kararıyla değiştirmek',
            'D': 'Görevi verip tescil ve ilan ettirmek',
            'E': 'Denetçinin ücretini kamuya açıklamak',
        },
        'D',
        'Seçimden sonra yönetim kurulu gecikmeksizin denetleme görevini denetçiye verir ve denetçiyi ticaret siciline tescil ettirip ilan eder.',
    ),
    # düzey 3
    '0010': patch(
        'Bir şirket, denetçiden alacak bakiyelerine belirli prosedürleri uygulayıp bulgularını raporlamasını istemiştir; sonuçların değerlendirilmesi raporu kullananlara bırakılacaktır.\n\nBu hizmet aşağıdakilerden hangisidir?',
        {
            'A': 'Üzerinde mutabık kalınan prosedürler',
            'B': 'Faaliyet denetimi',
            'C': 'Sınırlı bağımsız denetim',
            'D': 'Bağımsız denetim',
            'E': 'Tabloların meslek mensubunca derlendiği hizmet',
        },
        'A',
        'Üzerinde mutabık kalınan prosedürler hizmetinde denetçi kararlaştırılan prosedürleri uygular ve bulguları raporlar; güvence vermez, sonuçları kullanıcılar değerlendirir.',
    ),
    # düzey 3
    '0011': patch(
        'Denetçinin, bir belgenin gerçek olmadığına işaret eden bir durumla karşılaştığında belgeyi araştırması aşağıdakilerden hangisinin gereğidir?',
        {
            'A': 'Rotasyon',
            'B': 'Gizlilik',
            'C': 'Mesleki davranış',
            'D': 'Önemlilik',
            'E': 'Mesleki şüphecilik',
        },
        'E',
        'Mesleki şüphecilik, belgelerin güvenilirliğini sorgulayan ve kanıtı eleştirel değerlendiren bir tutumdur; aksi yönde gösterge yoksa denetçi kayıt ve belgeleri gerçek kabul edebilir.',
    ),
    # düzey 2
    '0012': patch(
        'Makul güvence ve sınırlı güvence denetimleriyle ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İkisi de güvence denetimi türüdür',
            'B': 'Makul güvence yüksek ama mutlak olmayan güvencedir',
            'C': 'Sınırlı güvencede prosedürler daha dardır',
            'D': 'Sınırlı güvencede sonuç olumlu görüşle bildirilir',
            'E': 'Bağımsız denetim makul güvence sağlar',
        },
        'D',
        'Sınırlı güvence denetiminde sonuç olumsuz ifade biçiminde bildirilir; olumlu görüş makul güvence denetimine özgüdür.',
    ),
    # düzey 2
    '0013': patch(
        'İç denetçinin bağımsızlığı ile bağımsız denetçinin bağımsızlığı arasındaki farkla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İç denetçi işletmeden tamamen bağımsızdır',
            'B': 'İç denetçinin bağımsızlığı örgütsel konumuna dayanır',
            'C': 'Bağımsız denetçinin bağımsızlığı ücretinden kaynaklanır',
            'D': 'Bağımsız denetçi yönetime bağlıdır',
            'E': 'İkisinin bağımsızlık düzeyi aynıdır',
        },
        'B',
        'İç denetçi işletmenin çalışanı olduğundan bağımsızlığı denetim komitesine raporlama gibi örgütsel düzenlemelere dayanır; bağımsız denetçi ise işletmeden tümüyle ayrı bir meslek mensubudur.',
    ),
    # düzey 2
    '0014': patch(
        'Finansal tabloların bütün olarak uygulanabilir finansal raporlama çerçevesine uygunluğunun araştırılması hangi denetim türüdür?',
        {
            'A': 'Kalite denetimi',
            'B': 'Vergi denetimi',
            'C': 'Finansal tablo denetimi',
            'D': 'Faaliyet denetimi',
            'E': 'Uygunluk denetimi',
        },
        'C',
        'Finansal tablo denetimi, tabloların önceden belirlenmiş ölçüt olan finansal raporlama çerçevesine uygun olarak gerçeğe uygun sunulup sunulmadığını araştırır.',
    ),
    # düzey 2
    '0015': patch(
        'Aşağıdakilerden hangisi bilgi riskini artıran nedenlerden biri değildir?',
        {
            'A': 'İşlemlerin karmaşık olması',
            'B': 'Veri hacminin büyük olması',
            'C': 'Hazırlayanın taraflı olabilmesi',
            'D': 'Bilgi kaynağının kullanıcıya uzak olması',
            'E': 'Bilginin bağımsız denetimden geçmesi',
        },
        'E',
        'Kaynağın uzaklığı, hazırlayanın taraflılığı, veri hacmi ve karmaşıklık bilgi riskini artırır; bağımsız denetim ise bu riski azaltır.',
    ),
    # düzey 2
    '0016': patch(
        'Faaliyet denetimi ile ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Etkinlik ve verimliliği değerlendirir',
            'B': 'Sonuçları genellikle yönetime sunulur',
            'C': 'İyileştirme önerileri içerir',
            'D': 'Ölçütleri her zaman kanunla belirlenir',
            'E': 'Ölçütleri finansal tablo denetimine göre daha az nesneldir',
        },
        'D',
        'Faaliyet denetiminde ölçütler çoğunlukla işletme amaçlarına göre belirlenir ve finansal tablo denetimine göre daha az nesneldir; kanunla belirlenmesi şart değildir.',
    ),
    # düzey 3
    '0017': patch(
        'Risk odaklı denetim yaklaşımında risklerin değerlendirilmesi, denetim sürecinin hangi aşamasını ifade eder?',
        {
            'A': 'Raporlama',
            'B': 'Müşteri kabulü',
            'C': 'Tamamlama',
            'D': 'Riske karşılık',
            'E': 'Planlama',
        },
        'E',
        'Risk odaklı yaklaşımda süreç risk değerlendirme, riske karşılık ve raporlama aşamalarından oluşur; risklerin değerlendirilmesi planlama aşamasına karşılık gelir.',
    ),
    # düzey 2
    '0018': patch(
        'Denetim süreci ile ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Planlama denetim boyunca güncellenir',
            'B': 'Aşamalar birbirinden bağımsız ve tek yönlüdür',
            'C': 'Süreç raporlamayla sonuçlanır',
            'D': 'Risk değerlendirmesi prosedürleri yönlendirir',
            'E': 'Süreç müşteri kabulüyle başlar',
        },
        'B',
        'Denetim süreci yinelemeli bir süreçtir; yeni bilgiler risk değerlendirmesini ve planı değiştirebilir. Aşamalar birbirinden bağımsız değildir.',
    ),
    # düzey 2
    '0019': patch(
        'İç denetim ile bağımsız denetim karşılaştırıldığında aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İki denetimin amacı birbirinden farklıdır',
            'B': 'İç denetim yönetime hizmet eder',
            'C': 'Bağımsız denetçi işletmenin çalışanıdır',
            'D': 'İç denetçi işletmenin çalışanıdır',
            'E': 'Bağımsız denetçi tablolar hakkında görüş bildirir',
        },
        'C',
        'İç denetçi işletme bünyesinde çalışır ve yönetime hizmet eder; bağımsız denetçi işletme dışındadır ve finansal tablolar hakkında kullanıcılara görüş bildirir.',
    ),
    # düzey 3
    '0020': patch(
        'Denetçi, tamamlama aşamasında finansal tabloların denetim sırasında edindiği bilgilerle tutarlı olup olmadığını analitik prosedürlerle değerlendirmektedir.\n\nBu prosedürlerin amaçlarından biri aşağıdakilerden hangisi değildir?',
        {
            'A': 'Tabloların bütün olarak makullüğünü değerlendirmek',
            'B': 'Genel bir sonuca varmak',
            'C': 'Önceden tespit edilmemiş riskleri fark etmek',
            'D': 'Örneklem büyüklüğünü belirlemek',
            'E': 'Ek prosedür gerekip gerekmediğini belirlemek',
        },
        'D',
        'Tamamlama aşamasındaki analitik prosedürler genel bir sonuca varmaya, tabloların makullüğünü değerlendirmeye ve daha önce fark edilmemiş riskleri belirlemeye yardımcı olur; örneklem büyüklüğü bu aşamada belirlenmez.',
    ),
    # düzey 2
    '0021': patch(
        'Hata ile hile arasındaki temel fark aşağıdakilerden hangisidir?',
        {
            'A': 'Hesabın türü',
            'B': 'Tespit edilme zamanı',
            'C': 'Tutarın büyüklüğü',
            'D': 'Kasıt unsuru',
            'E': 'Kayıt yöntemi',
        },
        'D',
        'Hileyi hatadan ayıran unsur, yanlışlığa yol açan eylemin kasıtlı olmasıdır.',
    ),
    # düzey 2
    '0022': patch(
        'Finansal tablolardaki hileyi önleme ve tespit etme sorumluluğu öncelikle kime aittir?',
        {
            'A': 'Yönetime ve üst yönetimden sorumlu olanlara',
            'B': 'Bağımsız denetçiye ve denetim kuruluşunun sorumlu ortağına',
            'C': 'Vergi müfettişine',
            'D': 'Kamu Gözetimi Kurumuna',
            'E': 'Pay sahiplerine',
        },
        'A',
        'Hileyi önleme ve tespit etmenin temel sorumluluğu yönetime ve üst yönetimden sorumlu olanlara aittir; denetçi hile kaynaklı önemli yanlışlık bulunmadığına dair makul güvence elde etmekle sorumludur.',
    ),
    # düzey 2
    '0023': patch(
        'Aşağıdakilerden hangisi denetim sürecinin sırası açısından doğru bir dizilimdir?',
        {
            'A': 'Planlama, kabul, raporlama, prosedürler',
            'B': 'Kabul, planlama, prosedürler, raporlama',
            'C': 'Prosedürler, kabul, planlama, raporlama',
            'D': 'Kabul, raporlama, planlama, prosedürler',
            'E': 'Raporlama, prosedürler, planlama, kabul',
        },
        'B',
        'Denetim süreci müşteri kabulüyle başlar, planlama ve risk değerlendirmeyle sürer, riske karşılık prosedürlerle devam eder ve tamamlama ile raporlamayla sona erer.',
    ),
    # düzey 3
    '0024': patch(
        "Türk Ticaret Kanunu'na göre bağımsız denetime tabi şirketlerin belirlenmesine ilişkin ölçütler nasıl belirlenir?",
        {
            'A': 'Her şirketin kendi kararıyla',
            'B': 'Denetçinin önerisiyle',
            'C': 'Genel kurulun oybirliğiyle',
            'D': 'Ticaret odası kararıyla',
            'E': 'Cumhurbaşkanı kararıyla',
        },
        'E',
        'Bağımsız denetime tabi olacak şirketler, aktif toplamı, satış hasılatı ve çalışan sayısı gibi ölçütlere göre Cumhurbaşkanı kararıyla belirlenir.',
    ),
    # düzey 2
    '0025': patch(
        'Aşağıdakilerden hangisinde toplulaştırma riski doğru tanımlanmıştır?',
        {
            'A': 'Yönetimin kontrolleri ihlal etme riski',
            'B': 'Tek bir yanlışlığın önemliliği aşma olasılığı',
            'C': 'Seçilen örneklemin anakütlenin özelliklerini temsil etmeme riski',
            'D': 'Yanlışlıklar toplamının önemliliği aşma olasılığı',
            'E': 'Denetçinin yanlış prosedür seçme riski',
        },
        'D',
        'Toplulaştırma riski, tek başına önemsiz olan düzeltilmemiş ve tespit edilmemiş yanlışlıkların toplamının finansal tabloların bütünü için önemliliği aşma olasılığıdır; performans önemliliği bu riski azaltmak için belirlenir.',
    ),
    # düzey 3
    '0026': patch(
        'Bir şirketin ara dönem finansal tablolarının sınırlı bağımsız denetiminde denetçinin sonucu hangi biçimde ifade edilir?',
        {
            'A': 'Ayrıntılı kanıt dökümü biçiminde',
            'B': 'Olumlu görüş biçiminde',
            'C': 'Bulgu listesi biçiminde',
            'D': 'Güvence içermeyen derleme raporu biçiminde',
            'E': 'Olumsuz ifade biçiminde',
        },
        'E',
        'Sınırlı güvence denetiminde sonuç, tabloların önemli yönlerden çerçeveye uygun olmadığına dair bir hususun dikkate çekilmediği şeklinde olumsuz ifadeyle bildirilir.',
    ),
    # düzey 2
    '0027': patch(
        'Denetçinin statüsüne göre yapılan sınıflamada aşağıdakilerden hangisi yer almaz?',
        {
            'A': 'Kamu denetimi',
            'B': 'Faaliyet denetimi',
            'C': 'İç denetim',
            'D': 'Dış denetim',
            'E': 'Bağımsız denetim',
        },
        'B',
        'Denetçinin statüsüne göre denetim bağımsız (dış) denetim, iç denetim ve kamu denetimi olarak sınıflanır. Faaliyet denetimi konusuna göre yapılan sınıflamadadır.',
    ),
    # düzey 3
    '0028': patch(
        'Halka açık bir şirketin denetiminde kamu yararı nedeniyle bağımsız denetçiden beklenen aşağıdakilerden hangisidir?',
        {
            'A': 'Raporu yönetime onaylatması',
            'B': 'Daha sıkı bağımsızlık kurallarına uyması',
            'C': 'Yönetimle daha yakın çalışıp danışmanlık da vermesi',
            'D': 'Ücretini sonuca bağlaması',
            'E': 'Gözetimden muaf olması',
        },
        'B',
        'Kamu yararını ilgilendiren kuruluşların denetiminde bağımsızlık kuralları daha sıkıdır; örneğin kilit denetim ortaklarının rotasyonu ve bazı denetim dışı hizmetlerin yasaklanması öngörülür.',
    ),
    # düzey 2
    '0029': patch(
        'Denetçi görüşü ile ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İşletmenin gelecekteki başarısını garanti eder',
            'B': 'Tabloların bütünü hakkındadır',
            'C': 'Makul güvenceye dayanır',
            'D': 'Tablolara ilişkin kullanıcıların güvenini artırır',
            'E': 'Önemlilik çerçevesinde verilir',
        },
        'A',
        'Denetçi görüşü işletmenin gelecekteki başarısını ya da yönetimin etkinliğini garanti etmez; tabloların bütün olarak önemli yanlışlık içerip içermediği hakkındadır.',
    ),
    # düzey 2
    '0030': patch(
        "BDS 320'ye göre aşağıdaki aşamalardan hangisinde denetçi önemlilik kavramını kullanmaz?",
        {
            'A': 'Denetimin planlanması',
            'B': 'Müşteri kabul ücretinin belirlenmesi',
            'C': 'Risklerin değerlendirilmesi',
            'D': 'Prosedürlerin kapsamının belirlenmesi',
            'E': 'Yanlışlıkların etkisinin değerlendirilmesi',
        },
        'B',
        'Önemlilik; planlamada, risklerin belirlenmesinde, ileri prosedürlerin niteliği, zamanlaması ve kapsamının belirlenmesinde ve tespit edilen yanlışlıkların etkisinin değerlendirilmesinde kullanılır.',
    ),
    # düzey 3
    '0031': patch(
        'Denetçi, bir hesabın denetimine yıl sonundan önce başlayıp bazı prosedürleri ara dönemde uygulamıştır.\n\nBu durumda dönem sonuna kadar yapılması gereken aşağıdakilerden hangisidir?',
        {
            'A': 'Kalan dönem için ek prosedür uygulamak',
            'B': 'Dönem sonu bakiyesini incelememek',
            'C': 'Ara dönem sonuçlarını aynen kullanmak',
            'D': 'Prosedürleri sonraki yıla bırakmak',
            'E': 'Önemliliği yükseltmek',
        },
        'A',
        'Ara dönemde uygulanan prosedürlerin sonuçlarının dönem sonuna taşınabilmesi için denetçi kalan dönem için ek maddi doğrulama prosedürleri ya da kontrol testleriyle birlikte maddi doğrulama uygular.',
    ),
    # düzey 2
    '0032': patch(
        'Aşağıdakilerden hangisi denetimin tamamlanma aşamasında yapılan işlerden biri değildir?',
        {
            'A': 'Müşteri kabul kararı verilmesi',
            'B': 'Sonraki olayların gözden geçirilmesi',
            'C': 'Düzeltilmemiş yanlışlıkların değerlendirilmesi',
            'D': 'Yazılı beyanların alınması',
            'E': 'Genel analitik incelemenin yapılması',
        },
        'A',
        'Tamamlama aşamasında sonraki olaylar gözden geçirilir, yazılı beyanlar alınır, genel analitik inceleme yapılır, düzeltilmemiş yanlışlıklar ve süreklilik değerlendirilir. Müşteri kabulü sürecin başındadır.',
    ),
    # düzey 2
    '0033': patch(
        "Türkiye'de bağımsız denetim standartlarını belirleyip yayımlamaya ve bağımsız denetçileri yetkilendirmeye yetkili kurum aşağıdakilerden hangisidir?",
        {
            'A': 'Türkiye Odalar ve Borsalar Birliği',
            'B': 'Türkiye Muhasebe Standartları Kurulu',
            'C': 'Kamu Gözetimi Kurumu',
            'D': 'Gelir İdaresi Başkanlığı',
            'E': 'Sermaye Piyasası Kurulu',
        },
        'C',
        "Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu (KGK), TFRS ve BDS'leri belirleyip yayımlar, bağımsız denetçi ve kuruluşları yetkilendirir ve gözetler.",
    ),
    # düzey 2
    '0034': patch(
        'Aşağıdakilerden hangisi sınırlı güvence denetiminin tanımıdır?',
        {
            'A': 'Tabloların denetçi tarafından derlendiği hizmet',
            'B': 'Güvence verilmeyen bulgu raporu hizmeti',
            'C': 'Riskin kabul edilebilir en düşük düzeye indirildiği denetim',
            'D': 'Riskin kabul edilebilir ama daha yüksek tutulduğu denetim',
            'E': 'Mevzuata uyumun kamu adına incelendiği denetim',
        },
        'D',
        'Sınırlı güvence denetiminde güvence denetimi riski, makul güvence denetimine göre daha yüksek ancak kabul edilebilir bir düzeye indirilir ve sonuç olumsuz ifadeyle bildirilir.',
    ),
    # düzey 2
    '0035': patch(
        "Türk Ticaret Kanunu'na göre anonim şirketin denetçisini kim seçer?",
        {
            'A': 'Genel kurul',
            'B': 'Ticaret sicili müdürlüğü',
            'C': 'Kamu Gözetimi Kurumu',
            'D': 'Yönetim kurulu',
            'E': 'Şirketin muhasebe müdürü',
        },
        'A',
        "TTK'ya göre denetçi her faaliyet dönemi için ve her hâlde görevini yerine getireceği dönem bitmeden genel kurul tarafından seçilir.",
    ),
    # düzey 2
    '0036': patch(
        'İç Denetim Enstitüsü tanımına göre iç denetim aşağıdakilerden hangisidir?',
        {
            'A': 'Finansal tabloları hazırlama faaliyeti',
            'B': 'Yönetimden bağımsız dış denetim',
            'C': 'Değer katmaya yönelik güvence ve danışmanlık faaliyeti',
            'D': 'Kamu adına yürütülen vergi incelemesi',
            'E': 'Pay sahipleri adına yapılan ve kamuya görüş bildirilen yasal denetim',
        },
        'C',
        'İç denetim, kurumun faaliyetlerine değer katmak ve geliştirmek için bağımsız ve objektif güvence ve danışmanlık faaliyetidir.',
    ),
    # düzey 3
    '0037': patch(
        'I. Finansal tablo denetimi\nII. Uygunluk denetimi\nIII. Kamu denetimi\n\nYukarıdakilerden hangileri denetimin konusuna göre yapılan sınıflamada yer alır?',
        {
            'A': 'Yalnız I',
            'B': 'I, II ve III',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'I ve III',
        },
        'D',
        'Konusuna göre sınıflama finansal tablo, uygunluk ve faaliyet denetimidir; kamu denetimi denetçinin statüsüne göre yapılan sınıflamadadır.',
    ),
    # düzey 2
    '0038': patch(
        'Bir bağımsız denetçinin mesleki faaliyetini yürütebilmesi için aşağıdakilerden hangisi gereklidir?',
        {
            'A': 'Yönetim kurulunun tavsiyesi',
            'B': 'Şirket genel kurulunun onayı',
            'C': 'Denetlenen şirketin yazılı daveti',
            'D': 'Vergi dairesinin izni',
            'E': 'Kamu Gözetimi Kurumunca yetkilendirilmesi',
        },
        'E',
        'Bağımsız denetim faaliyeti, KGK tarafından yetkilendirilen bağımsız denetçiler ve denetim kuruluşlarınca yürütülür.',
    ),
    # düzey 2
    '0039': patch(
        'Denetimin genel kabul gören tanımına göre denetçinin, iddiaların uygunluk derecesini araştırırken esas aldığı dayanak aşağıdakilerden hangisidir?',
        {
            'A': 'Sektördeki yaygın uygulamalar',
            'B': 'Denetçinin kişisel tercihleri',
            'C': 'Önceden belirlenmiş ölçütler',
            'D': 'Pay sahiplerinin talepleri',
            'E': 'Yönetimin beklentileri',
        },
        'C',
        'Denetim; ekonomik faaliyet ve olaylarla ilgili iddiaların önceden belirlenmiş ölçütlere uygunluk derecesini araştırmak ve sonuçları ilgililere bildirmek amacıyla tarafsız olarak kanıt toplayıp değerleyen sistematik bir süreçtir.',
    ),
    # düzey 3
    '0040': patch(
        'Denetçinin, denetlenen şirketin faaliyet gösterdiği sektörde daha önce hiç deneyimi bulunmamaktadır ve bunu giderecek bir önlem almamıştır.\n\nBu durum geleneksel genel kabul görmüş denetim standartlarından hangisi açısından risk oluşturur?',
        {
            'A': 'Yeterli açıklama',
            'B': 'Görüş bildirme',
            'C': 'Tutarlılık',
            'D': 'Bağımsızlık',
            'E': 'Mesleki eğitim ve yeterlilik',
        },
        'E',
        'Denetçinin işi yürütecek yeterli teknik eğitim ve deneyime sahip olması genel standartlardan mesleki eğitim ve yeterlilik standardının gereğidir.',
    ),
    # düzey 3
    '0041': patch(
        'Bir şirketin sürdürülebilirlik raporundaki sera gazı verilerine ilişkin güvence sağlanması hangi tür hizmete örnektir?',
        {
            'A': 'Üzerinde mutabık kalınan prosedürler',
            'B': 'Finansal tablo dışındaki güvence denetimi',
            'C': 'Vergi incelemesi',
            'D': 'Finansal tablo bağımsız denetimi',
            'E': 'Derleme hizmeti',
        },
        'B',
        'Tarihî finansal bilgiler dışındaki konu bilgilerine, örneğin sürdürülebilirlik verilerine güvence sağlanması finansal tablo dışındaki güvence denetimidir.',
    ),
    # düzey 2
    '0042': patch(
        "Kamu Gözetimi Kurumu'nun görevlerinden biri aşağıdakilerden hangisi değildir?",
        {
            'A': 'Türkiye Finansal Raporlama Standartlarını yayımlamak',
            'B': 'Bağımsız denetim standartlarını belirlemek',
            'C': 'Şirketlerin vergi incelemesini yapmak',
            'D': 'Denetim kuruluşlarını gözetlemek',
            'E': 'Bağımsız denetçileri yetkilendirmek',
        },
        'C',
        'KGK standartları yayımlar, denetçileri yetkilendirir ve denetim faaliyetlerini gözetler; vergi incelemesi vergi idaresinin görevidir.',
    ),
    # düzey 2
    '0043': patch(
        'Aşağıdakilerden hangisi denetimin genel kabul gören tanımında yer alan unsurlardan biri değildir?',
        {
            'A': 'Sonuçların ilgililere bildirilmesi',
            'B': 'İddiaların ölçütlerle karşılaştırılması',
            'C': 'Sistematik bir süreç olması',
            'D': 'Yönetime danışmanlık vermek',
            'E': 'Tarafsız kanıt toplanması',
        },
        'D',
        'Tanımda sistematik süreç, tarafsız kanıt toplama ve değerleme, iddiaların önceden belirlenmiş ölçütlerle karşılaştırılması ve sonuçların ilgililere bildirilmesi yer alır. Danışmanlık denetimin tanım unsuru değildir.',
    ),
    # düzey 2
    '0044': patch(
        'Bağımsız denetçinin taşıması gereken temel niteliklerden biri aşağıdakilerden hangisi değildir?',
        {
            'A': 'Bağımsızlık',
            'B': 'Mesleki yeterlilik',
            'C': 'Mesleki özen',
            'D': 'Denetlenen şirkette pay sahibi olmak',
            'E': 'Mesleki şüphecilik',
        },
        'D',
        'Denetçi mesleki yeterlilik, bağımsızlık, mesleki özen ve şüphecilik taşımalıdır; denetlenen şirkette pay sahipliği bağımsızlığı ortadan kaldırır.',
    ),
    # düzey 2
    '0045': patch(
        'Aşağıdakilerden hangisi bağımsız denetimin işletme dışındaki kullanıcılara sağladığı yararlardan biri değildir?',
        {
            'A': 'Yönetimin tabloları hazırlama sorumluluğunu kaldırması',
            'B': 'Yatırım kararlarına güvenli dayanak oluşturması',
            'C': 'Finansal bilginin güvenilirliğini artırması',
            'D': 'Kredi değerlendirmelerinde güveni artırması',
            'E': 'Kaynakların daha doğru yönlendirilmesine katkı sağlaması',
        },
        'A',
        'Bağımsız denetim finansal bilginin güvenilirliğini artırır ve kullanıcı kararlarını destekler; ancak tabloları hazırlama sorumluluğu yönetimde kalır.',
    ),
    # düzey 2
    '0046': patch(
        "Sayıştay'ın bir kamu idaresinin harcamalarını denetlemesi denetçinin statüsüne göre hangi tür denetimdir?",
        {
            'A': 'Finansal tablo denetimi',
            'B': 'İç denetim',
            'C': 'Bağımsız denetim',
            'D': 'Faaliyet denetimi',
            'E': 'Kamu denetimi',
        },
        'E',
        'Kamu kurumlarında görevli denetçilerce kamu adına yapılan denetim kamu denetimidir; Sayıştay denetimi buna örnektir.',
    ),
    # düzey 3
    '0047': patch(
        'I. Bağımsız denetim\nII. Sınırlı bağımsız denetim\nIII. Derleme hizmeti\n\nYukarıdaki hizmetlerden hangileri güvence içerir?',
        {
            'A': 'II ve III',
            'B': 'I, II ve III',
            'C': 'I ve II',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'C',
        'Bağımsız denetim makul, sınırlı bağımsız denetim sınırlı güvence verir; derleme hizmeti güvence içermez.',
    ),
    # düzey 3
    '0048': patch(
        'I. Müşteri kabulü\nII. Risk değerlendirme\nIII. Raporlama\n\nRisk odaklı denetim yaklaşımının temel üç aşaması dikkate alındığında yukarıdakilerden hangileri bu aşamalar arasındadır?',
        {
            'A': 'II ve III',
            'B': 'I ve III',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'A',
        'Risk odaklı yaklaşımın üç temel aşaması risk değerlendirme, riske karşılık ve raporlamadır; müşteri kabulü bu aşamalardan önce gelir.',
    ),
    # düzey 2
    '0049': patch(
        'Aşağıdakilerden hangisi denetimin planlanmasını oluşturan alt aşamalardan biri değildir?',
        {
            'A': 'Risklerin değerlendirilmesi',
            'B': 'İşletmenin ve çevresinin anlaşılması',
            'C': 'Genel stratejinin oluşturulması',
            'D': 'Önemliliğin belirlenmesi',
            'E': 'Denetçi raporunun yayımlanması',
        },
        'E',
        'Planlama; işletmeyi ve çevresini anlama, önemliliği belirleme, riskleri değerlendirme ve genel strateji ile planı oluşturmayı içerir. Raporun yayımlanması son aşamadır.',
    ),
    # düzey 2
    '0050': patch(
        'Aşağıdakilerden hangisi denetim sürecinin temel aşamalarından biri değildir?',
        {
            'A': 'Finansal tabloların hazırlanması',
            'B': 'Riske karşılık prosedürleri',
            'C': 'Tamamlama ve raporlama',
            'D': 'Planlama ve risk değerlendirme',
            'E': 'Müşteri kabulü ve sözleşme',
        },
        'A',
        'Denetim süreci müşteri kabulü ve sözleşme, planlama ve risk değerlendirme, değerlendirilen risklere karşılık prosedürler ile tamamlama ve raporlama aşamalarından oluşur. Tabloları hazırlamak yönetimin işidir.',
    ),
    # düzey 2
    '0051': patch(
        'Bağımsız denetçinin hileye ilişkin sorumluluğu ile ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tespit ettiği hileyi uygun kademeye bildirir',
            'B': 'Hile riskini değerlendirirken yönetimi sorgular',
            'C': 'Tüm hileleri tespit etmeyi garanti eder',
            'D': 'Denetim boyunca mesleki şüphecilik gösterir',
            'E': 'Hile kaynaklı önemli yanlışlık için makul güvence elde eder',
        },
        'C',
        'Denetçi, tabloların hata ya da hile kaynaklı önemli yanlışlık içermediğine dair makul güvence elde etmekle sorumludur; her hileyi tespit etmeyi garanti etmez.',
    ),
    # düzey 2
    '0052': patch(
        'Aşağıdakilerden hangisi müşterinin seçimi ve işin kabulü kapsamında değerlendirilmez?',
        {
            'A': 'Kuruluşun yetkinliği ve kaynakları',
            'B': 'Bağımsızlık gerekliliklerine uyum',
            'C': 'Denetimin ön şartlarının varlığı',
            'D': 'Yönetimin dürüstlüğü',
            'E': 'Örneklem büyüklüğünün hesaplanması',
        },
        'E',
        'Müşteri kabulünde yönetimin dürüstlüğü, bağımsızlık, yetkinlik ve kaynaklar ile denetimin ön şartları değerlendirilir. Örneklem büyüklüğü riske karşılık aşamasında belirlenir.',
    ),
    # düzey 3
    '0053': patch(
        'Aşağıdakilerden hangisi bağımsız denetimin yapısal kısıtlarından finansal raporlamanın niteliğiyle ilgili olanıdır?',
        {
            'A': 'Yönetimin bilgi saklayabilmesi',
            'B': 'Muvazaa ve sahtecilik',
            'C': 'Denetçinin yasal yetkilerinin sınırlı olması',
            'D': 'Tahmin ve muhakemelerin bulunması',
            'E': 'Makul süre ve maliyet sınırı',
        },
        'D',
        'Finansal tabloların hazırlanması yönetimin muhakemesini ve sübjektif kararlar ile tahminleri içerir; bu, finansal raporlamanın niteliğinden kaynaklanan bir kısıttır. Bilgi saklama, muvazaa ve yetki sınırı prosedürlerin niteliğiyle, süre-maliyet ise zamanlılıkla ilgilidir.',
    ),
    # düzey 3
    '0054': patch(
        'Bir bankanın, kredi verdiği şirketin kredi sözleşmesindeki finansal oran koşullarına uyup uymadığını belirlemek için yaptırdığı inceleme hangi denetim türüdür?',
        {
            'A': 'İç denetim',
            'B': 'Uygunluk denetimi',
            'C': 'Faaliyet denetimi',
            'D': 'Finansal tablo denetimi',
            'E': 'Kamu denetimi',
        },
        'B',
        'Sözleşme hükümlerine uyumun araştırılması uygunluk denetimidir.',
    ),
    # düzey 2
    '0055': patch(
        'Muhasebe süreci ile denetim süreci arasındaki ilişki için aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Denetim, tablolardan belgelere doğru ilerler',
            'B': 'Muhasebe denetimden sonra yapılır',
            'C': 'Denetim, muhasebe kayıtlarını oluşturur ve tabloları hazırlar',
            'D': 'İkisi aynı yönde ilerler',
            'E': 'Denetim, yönetimin yerine kayıt tutar',
        },
        'A',
        'Muhasebe belgelerden kayıtlara ve finansal tablolara doğru ilerler; denetim ise finansal tablolardaki iddialardan başlayarak kayıt ve belgelere doğru geriye giden bir süreçtir.',
    ),
    # düzey 3
    '0056': patch(
        "I. Finansal raporlama standartlarını yayımlamak\nII. Bağımsız denetçileri yetkilendirmek\nIII. Şirketlerin yönetim kurulu üyelerini atamak\n\nYukarıdakilerden hangileri Kamu Gözetimi Kurumu'nun görevlerindendir?",
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I ve III',
        },
        'C',
        'KGK standartları yayımlar ve denetçileri yetkilendirir; şirket yönetim kurulu üyelerini atamak görevi değildir.',
    ),
    # düzey 2
    '0057': patch(
        'Kamu Gözetimi Kurumunun bağımsız denetim kuruluşları üzerindeki inceleme yetkisinin temel amacı aşağıdakilerden hangisidir?',
        {
            'A': 'Denetim kalitesini gözetlemek',
            'B': 'Şirketlerin vergi borcunu tahsil etmek',
            'C': 'Denetim ücretlerini belirlemek',
            'D': 'Şirketlerin finansal tablolarını hazırlamak',
            'E': 'Denetçi raporlarını yeniden yazmak',
        },
        'A',
        "KGK'nın kalite güvence incelemeleri, denetim kuruluşlarının standartlara ve mevzuata uygun çalışıp çalışmadığını ve denetim kalitesini gözetlemeyi amaçlar.",
    ),
    # düzey 2
    '0058': patch(
        'Bir muhasebe çalışanı, bir faturayı dikkatsizlik sonucu yanlış hesaba kaydetmiştir.\n\nBu yanlışlığın niteliği aşağıdakilerden hangisidir?',
        {
            'A': 'Hata',
            'B': 'Varlıkların kötüye kullanılması',
            'C': 'Hileli finansal raporlama',
            'D': 'Muvazaa',
            'E': 'Zimmet',
        },
        'A',
        'Kasıt içermeyen yanlışlıklar hatadır; dikkatsizlik sonucu yanlış kayıt buna örnektir.',
    ),
    # düzey 2
    '0059': patch(
        'Denetçi işletmeyi ve faaliyet ortamını anlamaya çalışmaktadır.\n\nAşağıdakilerden hangisi bu kapsamda yapması gerekenlerden biri değildir?',
        {
            'A': 'Muhasebe politikalarını anlamak',
            'B': 'İşletmenin yapısını ve faaliyetlerini anlamak',
            'C': 'Finansal performans ölçütlerini anlamak',
            'D': 'Sektör ve düzenleyici çevreyi anlamak',
            'E': 'İşletmenin satış fiyatlarını belirlemek',
        },
        'E',
        'Denetçi işletmenin sektörünü, düzenleyici çevresini, yapısını, faaliyetlerini, muhasebe politikalarını ve performans ölçütlerini anlar; işletme kararlarını vermek görevi değildir.',
    ),
    # düzey 3
    '0060': patch(
        'Vergi müfettişlerinin bir mükellefin beyannamelerini vergi mevzuatına uygunluk yönünden incelemesi, konusuna göre hangi denetim türüdür?',
        {
            'A': 'Faaliyet denetimi',
            'B': 'İç denetim',
            'C': 'Uygunluk denetimi',
            'D': 'Bağımsız denetim',
            'E': 'Finansal tablo denetimi',
        },
        'C',
        'Belirli kurallara, mevzuata ya da sözleşme hükümlerine uyulup uyulmadığının araştırılması uygunluk denetimidir; vergi incelemesi buna örnektir.',
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
    print(f"1 paket / {len(PATCHES)} soru ('Denetim Kavramı, Türleri ve Denetçi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
