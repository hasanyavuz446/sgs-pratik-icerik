#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Örnekleme ve Çalışma Kâğıtları — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Denetim turu: gerçek sınavın denetim bloğuyla (73-88; 256 soru) karşılaştırıldı — gerçekte köklerin %29'u standarda atıf yapar (bizde %0), olumsuz kök %46 (%34), şık medyanı 41 karakter (63), parantezli şık %1 (%14), olay anlatan kök %27 (%12). Paket baştan yazıldı: BDS 530 (kavramlar, örnekleme riski türleri, örneklem büyüklüğü faktörleri, seçim yöntemleri, prosedürün uygulanamaması, anomali, yansıtma ve sonuç değerlendirme) ve BDS 230 (dokümantasyonun içeriği, deneyimli denetçi ölçütü, nihai dosya, idari değişiklikler, sürekli/cari dosya, mülkiyet ve gizlilik). Hesaplar kesirli aritmetikle yapıldı.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: BDS 530 Bağımsız Denetimde Örnekleme; BDS 230 Denetim Dokümantasyonu
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/denetim/denetim_ornekleme.json"
STYLE_REF = 'SGS Denetim (standarda atıflı/olay kök + kısa şık; gerçek sınav profili)'
ONEK = "den-ornek-gen-"


def patch(stem, options, answer, solution, ref='BDS 530 Bağımsız Denetimde Örnekleme; BDS 230 Denetim Dokümantasyonu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "BDS 530'a göre detay testlerinde aşağıdakilerden hangisi örneklem büyüklüğünü artıran faktörlerden biri değildir?",
        {
            'A': 'İstenen güvence düzeyinin artması',
            'B': 'Diğer prosedürlerden alınan güvencenin azalması',
            'C': 'Uygun tabakalandırma yapılması',
            'D': 'Beklenen yanlışlık tutarının artması',
            'E': 'Önemli yanlışlık riskinin artması',
        },
        'C',
        'Anakütlenin uygun biçimde tabakalandırılması örneklem büyüklüğünü azaltır. Risk, beklenen yanlışlık ve istenen güvence arttıkça; aynı iddiaya yönelik diğer prosedürlerden alınan güvence azaldıkça örneklem büyür.',
    ),
    # düzey 2
    '0002': patch(
        "BDS 530'a göre istatistiksel örnekleme ile ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Seçimde denetçinin kişisel tercihi belirleyicidir',
            'B': 'Örneklem kalemleri rastgele seçilir',
            'C': 'Bu özellikleri taşımayan yaklaşım istatistiksel değildir',
            'D': 'Örnekleme riski ölçülür',
            'E': 'Sonuçlar olasılık teorisiyle değerlendirilir',
        },
        'A',
        'İstatistiksel örnekleme; kalemlerin rastgele seçimi ve örnekleme riskinin ölçülmesi dahil sonuçların olasılık teorisiyle değerlendirilmesi özelliklerini taşır. Bu özellikleri taşımayan yaklaşım istatistiksel olmayan örneklemedir. Seçimi denetçinin kişisel tercihi belirlemez.',
    ),
    # düzey 2
    '0003': patch(
        "BDS 530'a göre kontrol testlerinde, diğer koşullar aynı kalmak kaydıyla aşağıdaki değişikliklerden hangisi örneklem büyüklüğünü azaltır?",
        {
            'A': 'Beklenen sapma oranının artması',
            'B': 'Kontrollere dayanma planının artması',
            'C': 'İstenen güvence düzeyinin artması',
            'D': 'Anakütlenin önemli ölçüde büyümesi',
            'E': 'Tolere edilebilir sapma oranının artması',
        },
        'E',
        'Tolere edilebilir sapma oranı arttıkça örneklem büyüklüğü azalır. Beklenen sapma, kontrollere dayanma ve istenen güvence arttıkça örneklem büyür; büyük anakütlelerde birim sayısının etkisi önemsizdir.',
    ),
    # düzey 3
    '0004': patch(
        "Denetçi alacak anakütlesini iki tabakaya ayırmıştır. Tutarı 1.000.000 ₺'yi aşan 8 bakiyenin tamamını (toplam 14.000.000 ₺) teyit etmiş ve bunlarda 90.000 ₺ yanlışlık bulmuştur. Kalan 26.000.000 ₺'lik tabakadan seçtiği toplam 2.000.000 ₺'lik örneklemde ise 30.000 ₺ yanlışlık bulmuştur.\n\nOran yöntemine göre alacaklar için toplam yanlışlık tahmini kaç ₺'dir?",
        {
            'A': '1.560.000 ₺',
            'B': '480.000 ₺',
            'C': '300.000 ₺',
            'D': '390.000 ₺',
            'E': '420.000 ₺',
        },
        'B',
        'Tamamı incelenen tabakadaki 90.000 ₺ yansıtılmaz, doğrudan eklenir. Örneklenen tabaka: 30.000 / 2.000.000 × 26.000.000 = 390.000 ₺. Toplam 90.000 + 390.000 = 480.000 ₺.',
    ),
    # düzey 3
    '0005': patch(
        "Nihai denetim dosyası oluşturulduktan sonra denetçi, mevcut bir çalışma kâğıdına açıklayıcı bir ek yapmayı gerekli görmüştür.\n\nBDS 230'a göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Ekin nedeni belgelenir',
            'B': 'Eki kimin yaptığı kaydedilir',
            'C': 'Ekin yapıldığı tarih kaydedilir',
            'D': 'Nihai dosyaya ek yapılması yasaktır',
            'E': 'Saklama süresi dolmadan dokümantasyon silinemez',
        },
        'D',
        'BDS 230: nihai dosya oluşturulduktan sonra değişiklik ya da ilave gerekirse denetçi bunun nedenlerini, kimin ne zaman yaptığını ve gözden geçirdiğini belgeler; ek yapılması yasak değildir. Saklama süresi dolmadan dokümantasyon silinemez.',
    ),
    # düzey 3
    '0006': patch(
        "Denetçi alacakların varlığını test etmek için dış teyit yerine satış faturalarının işletme içindeki kopyalarını incelemiş ve bu nedenle yanlış sonuca varmıştır.\n\nBDS 530'a göre bu durum hangi risk kapsamında değerlendirilir?",
        {
            'A': 'Yetersiz güven riski',
            'B': 'Yanlış red riski',
            'C': 'Örnekleme dışı risk',
            'D': 'Örnekleme riski',
            'E': 'Tolere edilebilir risk',
        },
        'C',
        'Örnekleme dışı risk, denetçinin örnekleme riskiyle ilgisi olmayan bir nedenle yanlış sonuca varması riskidir; uygun olmayan prosedür seçilmesi buna örnektir.',
    ),
    # düzey 2
    '0007': patch(
        "BDS 530'a göre yanlışlık ve sapmaların anakütleye yansıtılmasıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Kontrol testinde sapmalar oranla ayrıca yansıtılır',
            'B': 'Anomaliler yansıtma dışında tutulur',
            'C': 'Örneklem sapma oranı yansıtılmış sapma oranıdır',
            'D': 'Detay testinde yanlışlıklar anakütleye yansıtılır',
            'E': 'Yansıtılan yanlışlık tolere edilebilirle karşılaştırılır',
        },
        'A',
        'Kontrol testlerinde örneklem sapma oranı aynı zamanda anakütle için yansıtılmış sapma oranı olduğundan açıkça yansıtma gerekmez. Detay testlerinde ise yanlışlıklar yansıtılır ve tolere edilebilir yanlışlıkla karşılaştırılır.',
    ),
    # düzey 3
    '0008': patch(
        'I. Örneklem büyüklüğü artırıldıkça örnekleme riski azalır.\nII. Örnekleme dışı risk; uygun planlama, yönlendirme ve gözetimle azaltılabilir.\nIII. Anakütlenin tamamı incelendiğinde örnekleme dışı risk ortadan kalkar.\n\nYukarıdaki ifadelerden hangileri doğrudur?',
        {
            'A': 'Yalnız I',
            'B': 'I, II ve III',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'I ve II',
        },
        'E',
        'Örnekleme riski örneklem büyüdükçe azalır. Örnekleme dışı risk ise örneklemeden bağımsızdır; anakütlenin tamamı incelense bile uygun olmayan prosedür ya da kanıtın yanlış yorumlanması nedeniyle varlığını sürdürür, ancak planlama ve gözetimle azaltılabilir.',
    ),
    # düzey 3
    '0009': patch(
        "Denetçi ticari borçların tamlığını test etmek için 27.500.000 ₺ tutarındaki anakütleden 1.500.000 ₺ tutarında örneklem seçmiş ve 18.000 ₺ eksik kayıt bulmuştur. Bu hesap için tolere edilebilir yanlışlık 300.000 ₺'dir.\n\nBDS 530'a göre denetçi hangi sonuca varır?",
        {
            'A': 'Fark anomali sayılır',
            'B': 'Örneklem makul dayanak sağlamaz',
            'C': 'Hesap doğru kabul edilir',
            'D': 'Tolere edilebilir yanlışlık artırılır',
            'E': 'Örnekleme dışı risk gerçekleşmiştir',
        },
        'B',
        'Yansıtılmış yanlışlık 18.000 ₺ / 1.500.000 ₺ × 27.500.000 ₺ = 330.000 ₺ olup tolere edilebilir yanlışlığı (300.000 ₺) aşmaktadır. Bu durumda örneklem, test edilen anakütle hakkında sonuca makul dayanak sağlamaz; denetçi ek prosedürler uygular ya da yönetimden düzeltme ister.',
    ),
    # düzey 2
    '0010': patch(
        "BDS 530'a göre aşağıdakilerden hangisi denetim örneklemesinin özelliklerinden biri değildir?",
        {
            'A': 'Kontrol testlerinde de kullanılabilmesi',
            'B': 'Her örnekleme biriminin seçilme şansının olması',
            'C': "Prosedürün kalemlerin %100'ünden azına uygulanması",
            'D': 'Anakütledeki kalemlerin tamamının test edilmesi',
            'E': 'Anakütle hakkında sonuca dayanak sağlaması',
        },
        'D',
        "Denetim örneklemesi, prosedürlerin anakütledeki kalemlerin %100'ünden azına, tüm örnekleme birimlerinin seçilme şansı olacak şekilde uygulanmasıdır. Kalemlerin tamamının incelenmesi örnekleme değildir.",
    ),
    # düzey 2
    '0011': patch(
        'Parasal birim örneklemesiyle ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Örnekleme birimi her bir parasal birimdir',
            'B': 'Her bakiyenin seçilme olasılığı eşittir',
            'C': 'Seçim değer ağırlıklıdır',
            'D': 'Büyük tutarların seçilme olasılığı yüksektir',
            'E': 'İstatistiksel bir örnekleme yöntemidir',
        },
        'B',
        'Parasal birim örneklemesinde örnekleme birimi her bir parasal birimdir ve yöntem istatistikseldir. Seçim değer ağırlıklı olduğundan büyük tutarlı kalemlerin seçilme olasılığı yüksektir; bakiyelerin seçilme olasılığı eşit değildir.',
    ),
    # düzey 3
    '0012': patch(
        "Denetçi geçen yıl satın alma onay kontrolünde sapma bulmamıştı. Bu yıl satın alma biriminde personelin büyük bölümü değiştiği için daha fazla sapma beklemektedir.\n\nDiğer koşullar aynı kaldığına göre BDS 530'a göre kontrol testi örneklem büyüklüğü nasıl etkilenir?",
        {
            'A': 'Artar',
            'B': 'Örnekleme bırakılır',
            'C': 'Değişmez',
            'D': 'Azalır',
            'E': 'Tabakalandırma gerekir',
        },
        'A',
        'Kontrol testlerinde beklenen sapma oranı arttıkça örneklem büyüklüğü artar.',
    ),
    # düzey 3
    '0013': patch(
        'Denetçi arşiv kutularından, belirli bir yönteme bağlı kalmadan ve bilinçli olarak herhangi bir belgeyi kayırmadan 40 belge çekmiştir.\n\nSeçim yöntemi ve bu yöntemin istatistiksel örneklemde kullanılabilirliği aşağıdakilerden hangisinde doğru verilmiştir?',
        {
            'A': 'Rastgele seçim – Uygundur',
            'B': 'Sistematik seçim – Uygun değildir',
            'C': 'Gelişigüzel seçim – Uygun değildir',
            'D': 'Blok seçim – Uygundur',
            'E': 'Gelişigüzel seçim – Uygundur',
        },
        'C',
        'Belirli bir yapıya bağlı kalmadan, bilinçli taraf tutmadan yapılan seçim gelişigüzel seçimdir ve istatistiksel örneklemede uygun değildir.',
    ),
    # düzey 3
    '0014': patch(
        'Kontrol testinde denetçi, örneklem sonucuna dayanarak gerçekte etkin olmayan bir kontrolü etkin kabul etmiştir.\n\nBu riskin etkilediği alan ve adı aşağıdakilerden hangisinde doğru verilmiştir?',
        {
            'A': 'Bağımsızlık – Örnekleme dışı risk',
            'B': 'Verimlilik – Yetersiz güven riski',
            'C': 'Etkinlik – Yetersiz güven riski',
            'D': 'Etkinlik – Aşırı güven riski',
            'E': 'Verimlilik – Aşırı güven riski',
        },
        'D',
        'Kontrolleri olduğundan daha etkin bulmak aşırı güven (beta) riskidir; denetimin etkinliğini etkiler ve uygun olmayan görüşe yol açabilir.',
    ),
    # düzey 2
    '0015': patch(
        "BDS 530'a göre aşağıdakilerden hangisi örnekleme birimi olarak kullanılabilecek kalemlerden biri değildir?",
        {
            'A': 'Banka hesap özetindeki alacak kayıtları',
            'B': 'Parasal birimler',
            'C': 'Müşteri bakiyeleri',
            'D': 'Satış faturaları',
            'E': 'Denetçinin belirlediği önemlilik tutarı',
        },
        'E',
        'Örnekleme birimi anakütleyi oluşturan bireysel kalemlerdir: çekler, banka hesap özetindeki alacak kayıtları, satış faturaları, müşteri bakiyeleri veya parasal birimler. Önemlilik bir eşik tutardır, anakütlenin kalemi değildir.',
    ),
    # düzey 3
    '0016': patch(
        "Denetçi örneklemde bulduğu üç yanlışlığın aynı muhasebe personelinin kaydettiği işlemlerde yoğunlaştığını görmüştür.\n\nBDS 530'a göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Yanlışlıkların niteliği araştırılır',
            'B': 'Yanlışlıklar araştırılmadan anomali sayılır',
            'C': 'Yanlışlıkların nedeni araştırılır',
            'D': 'Ortak özellik taşıyan kalemler belirlenebilir',
            'E': 'Prosedürler genişletilebilir',
        },
        'B',
        'BDS 530: denetçi tespit edilen sapma ve yanlışlıkların niteliğini ve nedenlerini araştırır; ortak bir özellik varsa o özelliği taşıyan tüm kalemleri belirleyip prosedürleri genişletebilir. Bir yanlışlığın anomali sayılması ancak son derece nadir durumlarda ve yüksek kesinlik düzeyinde kanıtla mümkündür.',
    ),
    # düzey 2
    '0017': patch(
        "BDS 230'a göre aşağıdakilerden hangisinin denetim dokümantasyonuna dahil edilmesi gerekmez?",
        {
            'A': 'Önemli konulara ilişkin yazılı özet ve değerlendirmeler',
            'B': 'Yazım hataları düzeltilmiş eski taslaklar',
            'C': 'Teyit yanıtları',
            'D': 'Yönetim beyan mektubu',
            'E': 'Analizler ve hesap tabloları',
        },
        'B',
        'Taslak çalışma kâğıtları ve finansal tablolar, eksik düşünceleri yansıtan notlar, yazım hatalarının düzeltildiği önceki suretler ve mükerrer belgeler dokümantasyona dahil edilmek zorunda değildir.',
    ),
    # düzey 3
    '0018': patch(
        "Denetçi ödemelerin onaylanmasına ilişkin kontrolü test ederken, örnekleme seçtiği bir çekin ödemeden önce usulüne uygun biçimde iptal edildiğini görmüştür.\n\nBDS 530'a göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Usulüne uygun iptal edilmiş çek sapma değildir',
            'B': 'Prosedür yerine geçecek bir kaleme uygulanır',
            'C': 'Örneklem bu nedenle geçersiz sayılmaz',
            'D': 'Anakütlenin yeniden tanımlanması gerekmez',
            'E': 'Çek kontrol testinde sapma olarak değerlendirilir',
        },
        'E',
        'BDS 530: prosedür seçilen kaleme uygulanamıyorsa denetçi prosedürü yerine geçecek bir kaleme uygular. Usulüne uygun iptal edilmiş çek sapma değildir; örneklemin geçersiz sayılması ya da anakütlenin yeniden tanımlanması gerekmez.',
    ),
    # düzey 2
    '0019': patch(
        "BDS 230 Denetim Dokümantasyonu'na göre aşağıdakilerden hangisi denetim dokümantasyonunda yer alması gereken hususlardan biri değildir?",
        {
            'A': 'Önemli mesleki yargılar',
            'B': 'Ulaşılan sonuçlar',
            'C': 'Denetim ücretinin hesaplanma yöntemi',
            'D': 'Uygulanan prosedürlerin niteliği ve kapsamı',
            'E': 'Elde edilen denetim kanıtları',
        },
        'C',
        'Denetim dokümantasyonu; uygulanan prosedürlerin niteliğini, zamanlamasını ve kapsamını, elde edilen kanıtları, ulaşılan sonuçları, önemli konuları ve bunlarla ilgili mesleki yargıları içerir. Ücretin hesaplanma yöntemi bu kapsamda değildir.',
    ),
    # düzey 3
    '0020': patch(
        "Denetçi bu yıl, geçen yıl 4.000 olan fatura sayısının 9.000'e çıktığını görmüştür; risk değerlendirmesi ve diğer faktörler değişmemiştir.\n\nBDS 530'a göre büyük anakütlelerde birim sayısının örneklem büyüklüğüne etkisi hangisidir?",
        {
            'A': 'Örneklemi iki katına çıkarır',
            'B': 'Önemsiz düzeydedir',
            'C': 'Doğru orantılı artırır',
            'D': 'Ters orantılı azaltır',
            'E': 'Örneklemi yarıya indirir',
        },
        'B',
        'Büyük anakütlelerde anakütledeki örnekleme birimi sayısının örneklem büyüklüğüne etkisi önemsizdir; küçük anakütlelerde ise örnekleme çoğu zaman alternatif yöntemler kadar etkin değildir.',
    ),
    # düzey 2
    '0021': patch(
        "BDS 230'a göre aşağıdakilerden hangisi nihai denetim dosyasının oluşturulması sırasında yapılabilecek idari nitelikteki değişikliklerden biri değildir?",
        {
            'A': 'Çalışma kâğıtlarının sıralanması',
            'B': 'Kontrol listelerinin imzalanması',
            'C': 'Yeni bir denetim prosedürü uygulanması',
            'D': 'Geçersiz hâle gelen dokümantasyonun atılması',
            'E': 'Çapraz referans verilmesi',
        },
        'C',
        'Nihai dosyanın oluşturulması idari bir süreçtir ve yeni prosedür uygulanmasını ya da yeni sonuca ulaşılmasını içermez.',
    ),
    # düzey 3
    '0022': patch(
        'Denetçi, toplam tutarı 12.000.000 ₺ olan alacak anakütlesinden parasal birim örneklemesiyle sistematik olarak 80 parasal birim seçecektir.\n\nÖrnekleme aralığı ve tutarı bu aralığa eşit ya da daha büyük olan bakiyeler için aşağıdakilerden hangisi doğrudur?',
        {
            'A': '150.000 ₺ – Örneklem dışı kalır',
            'B': '150.000 ₺ – Örnekleme girer',
            'C': '75.000 ₺ – Örnekleme girer',
            'D': '300.000 ₺ – Ayrıca yansıtılır',
            'E': '15.000 ₺ – Anomali sayılır',
        },
        'B',
        "Örnekleme aralığı 12.000.000 ₺ / 80 = 150.000 ₺'dir. Tutarı aralığa eşit ya da büyük olan bakiyeler en az bir seçim noktası içerdiğinden örneklemde yer alır.",
    ),
    # düzey 2
    '0023': patch(
        'Aşağıdakilerden hangisi denetim dokümantasyonunun amaçlarından biri değildir?',
        {
            'A': 'Ekibin denetimi planlama ve yürütmesine yardım etmek',
            'B': 'Gözetim ve gözden geçirmeyi kolaylaştırmak',
            'C': 'Kalite kontrol incelemelerine imkân vermek',
            'D': 'Müşterinin muhasebe kayıtlarının yerine geçmek',
            'E': 'Ekibin hesap verebilirliğini sağlamak',
        },
        'D',
        'Dokümantasyon; ekibin planlama ve yürütmesine yardım eder, gözetim ve gözden geçirmeyi, hesap verebilirliği, sonraki denetimler için önemli konuların kaydını ve kalite kontrol incelemelerini mümkün kılar. Müşterinin muhasebe kayıtlarının yerini tutmaz.',
    ),
    # düzey 3
    '0024': patch(
        "I. Nihai dosya oluşturulduktan sonra saklama süresi sona ermeden dokümantasyon silinemez.\nII. Taslak finansal tabloların dosyada saklanması zorunludur.\nIII. Sözlü açıklamalar uygulanan prosedürler için tek başına yeterli dayanak oluşturmaz.\n\nBDS 230'a göre yukarıdaki ifadelerden hangileri doğrudur?",
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'II ve III',
            'E': 'I ve III',
        },
        'E',
        'Saklama süresi dolmadan nihai dosyadan dokümantasyon silinemez; sözlü açıklamalar tek başına yeterli dayanak değildir. Taslak finansal tablolar ve eksik düşünceleri yansıtan notlar dokümantasyona dahil edilmek zorunda değildir.',
    ),
    # düzey 2
    '0025': patch(
        'Denetçi genel yönetim giderlerini test ederken mart ve eylül aylarına ait gider faturalarının tamamını incelemeye karar vermiştir.\n\nBu seçim yöntemi aşağıdakilerden hangisidir?',
        {
            'A': 'Parasal birim örneklemesi',
            'B': 'Sistematik seçim',
            'C': 'Rastgele seçim',
            'D': 'Blok seçim',
            'E': 'Gelişigüzel seçim',
        },
        'D',
        'Anakütle içindeki bitişik kalemlerden oluşan bir bloğun seçilmesi blok seçimdir.',
    ),
    # düzey 3
    '0026': patch(
        "Denetçi raporu tarihinden sonra ortaya çıkan istisnai bir durum nedeniyle yeni denetim prosedürleri uygulanmıştır.\n\nBDS 230'a göre aşağıdakilerden hangisinin belgelenmesi gerekmez?",
        {
            'A': 'Değişikliği yapan ve gözden geçiren',
            'B': 'Karşılaşılan durumlar',
            'C': 'Önceki yılın denetim ücret teklifi',
            'D': 'Uygulanan prosedürler ve elde edilen kanıtlar',
            'E': 'Ulaşılan yeni sonuçlar ve etkileri',
        },
        'C',
        'Rapor tarihinden sonra yeni prosedür uygulanırsa karşılaşılan durumlar, prosedürler, kanıtlar, sonuçlar ve etkileri ile değişikliği kimin ne zaman yaptığı ve gözden geçirdiği belgelenir.',
    ),
    # düzey 2
    '0027': patch(
        'Denetçi, 2026 yılında düzenlenen 18.000 satış faturasının tamamı hakkında sonuca varmak amacıyla bunlardan 90 faturayı incelemeyi planlamaktadır.\n\nBDS 530 Bağımsız Denetimde Örnekleme standardına göre 18.000 faturanın oluşturduğu küme nasıl adlandırılır?',
        {
            'A': 'Tabaka',
            'B': 'Anakütle',
            'C': 'Örnekleme birimi',
            'D': 'Örnekleme aralığı',
            'E': 'Örneklem',
        },
        'B',
        'Anakütle, içinden örneklemin seçildiği ve denetçinin hakkında sonuca varmak istediği veri setinin tamamıdır. İncelenecek 90 fatura örneklem, her bir fatura ise örnekleme birimidir.',
    ),
    # düzey 2
    '0028': patch(
        "BDS 230'a göre denetim dokümantasyonu ile ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Sözlü açıklamalar tek başına yeterli değildir',
            'B': 'Zamanında hazırlanır',
            'C': 'Rapor tarihinden sonra toplu hâlde hazırlanır',
            'D': 'Fiziki veya elektronik ortamda tutulabilir',
            'E': 'Gözden geçirenin kimliği kaydedilir',
        },
        'C',
        'Dokümantasyon zamanında hazırlanır; sonradan hazırlanan dokümantasyon, çalışma sürerken hazırlanana göre daha az doğru olur. Sözlü açıklamalar uygulanan prosedürler için tek başına yeterli dayanak oluşturmaz.',
    ),
    # düzey 3
    '0029': patch(
        'İç kontrol gerçekte güvenilir olduğu hâlde denetçi, örneklem sonucuna bakarak kontrolün yeterli güvence sağlamadığı sonucuna varmıştır.\n\nBu durumun denetime olası etkisi aşağıdakilerden hangisidir?',
        {
            'A': 'Gereksiz ek çalışma yapılır',
            'B': 'Uygun olmayan görüş verilir',
            'C': 'Önemli yanlışlık gözden kaçar',
            'D': 'Denetimden çekilmek gerekir',
            'E': 'Örneklem küçültülür',
        },
        'A',
        'Kontrolü olduğundan daha az etkin bulmak yetersiz güven (alfa) riskidir; denetimin verimliliğini etkiler ve genellikle ek çalışmaya yol açar.',
    ),
    # düzey 3
    '0030': patch(
        "Denetçi istisnai bir durumda ilgili bir BDS gerekliliğinden ayrılmayı gerekli görmüştür.\n\nBDS 230'a göre denetçinin belgelemesi gereken husus aşağıdakilerden hangisidir?",
        {
            'A': 'Müşterinin yazılı onayı',
            'B': 'Kamu Gözetimi Kurumuna yapılan yazılı bildirim',
            'C': 'Ayrılma nedeni ve alternatif prosedürler',
            'D': 'Görüşteki değişiklik',
            'E': 'Ekip üyelerinin imzaları',
        },
        'C',
        'İlgili bir gerekliliğden ayrılan denetçi, uygulanan alternatif prosedürlerin gerekliliğin amacına nasıl ulaştığını ve ayrılma nedenlerini belgeler.',
    ),
    # düzey 3
    '0031': patch(
        "Detay testinde örnekleme seçilen bir satış faturasının belgeleri kaybolmuş, denetçi uygun bir alternatif prosedür de uygulayamamıştır.\n\nBDS 530'a göre bu kalem nasıl dikkate alınır?",
        {
            'A': 'Yanlışlık olarak',
            'B': 'Anomali olarak',
            'C': 'Örneklemden çıkarılarak',
            'D': 'Doğru kabul edilerek',
            'E': 'Yerine yeni kalem seçilerek',
        },
        'A',
        'Tasarlanan prosedür ya da uygun bir alternatif prosedür seçilen kaleme uygulanamıyorsa denetçi bu kalemi kontrol testinde sapma, detay testinde yanlışlık olarak dikkate alır.',
    ),
    # düzey 3
    '0032': patch(
        "Denetçi, tutarı 1.000.000 ₺'yi aşan 12 alıcı bakiyesinin tamamını ve kalan küçük bakiyeler arasından rastgele seçtiği 40 bakiyeyi teyit etmiştir.\n\nBDS 530 açısından bu çalışmayla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Örneklem 52 bakiyeden oluşur',
            'B': '40 bakiye anomali sayılır',
            'C': '12 bakiye örneklem dışı risktir',
            'D': 'Büyük bakiyeler anakütleye yansıtılır',
            'E': 'Örnekleme 40 bakiyeyi kapsar',
        },
        'E',
        'Belirli kalemlerin tamamının seçilmesi örnekleme değildir; bu kalemlerin sonuçları anakütleye yansıtılmaz. Örnekleme, kalan anakütleden rastgele seçilen 40 bakiyeyi kapsar.',
    ),
    # düzey 3
    '0033': patch(
        "Denetçi sevkiyatların faturalandırılmasını test etmek için 1.200 sevk irsaliyesinden sistematik seçimle örneklem almıştır.\n\nBDS 230'a göre test edilen kalemleri tanımlamak için çalışma kâğıdına hangisini kaydetmesi uygundur?",
        {
            'A': 'Seçimi yapan yazılımın lisansını',
            'B': 'Sevkiyat araçlarının plakalarını',
            'C': 'Müşterinin seçime onayını',
            'D': 'İrsaliyelerin fotokopi sayısını',
            'E': 'Kaynağı, başlangıç noktasını ve aralığı',
        },
        'E',
        'Sistematik seçimle örneklem alındığında denetçi test edilen kalemleri; seçimin kaynağını, başlangıç noktasını ve örnekleme aralığını belirterek tanımlayabilir.',
    ),
    # düzey 3
    '0034': patch(
        'Denetçi raporu 10 Mart 2026 tarihlidir.\n\nBDS 230 uygulama açıklamalarına göre nihai denetim dosyasının oluşturulması için genellikle aşılmaması gereken tarih aşağıdakilerden hangisidir?',
        {
            'A': '10 Haziran 2026',
            'B': '9 Mayıs 2026',
            'C': '31 Mart 2026',
            'D': '10 Nisan 2026',
            'E': '10 Mart 2027',
        },
        'B',
        "Nihai denetim dosyasının oluşturulması için uygun süre sınırı genellikle denetçi raporu tarihinden itibaren 60 günü aşmaz: 10 Mart'tan 60 gün sonrası 9 Mayıs 2026'dır.",
    ),
    # düzey 3
    '0035': patch(
        "Bir ekip üyesi stok sayım gözlemine ilişkin çalışma kâğıdını hazırlamıştır.\n\nBDS 230'a göre bu kâğıtta aşağıdakilerden hangisinin kaydedilmesi gerekmez?",
        {
            'A': 'Çalışmanın tamamlandığı tarih',
            'B': 'Çalışmayı yapanın kimliği',
            'C': 'Test edilen kalemlerin tanımlayıcı özellikleri',
            'D': 'Kâğıdı hazırlayanın meslekteki kıdemi',
            'E': 'Gözden geçirenin kimliği ve tarihi',
        },
        'D',
        'Denetçi; test edilen kalemlerin tanımlayıcı özelliklerini, çalışmayı kimin yaptığını ve tarihini, kimin gözden geçirdiğini, tarihini ve kapsamını kaydeder.',
    ),
    # düzey 2
    '0036': patch(
        "Denetçi, 2.400 müşteri bakiyesinden oluşan alıcılar hesabından teyit mektubu gönderilecek bakiyeleri seçmektedir.\n\nBDS 530'a göre her bir müşteri bakiyesi ne olarak adlandırılır?",
        {
            'A': 'Anomali',
            'B': 'Anakütle',
            'C': 'Örnekleme birimi',
            'D': 'Tabaka',
            'E': 'Tolere edilebilir yanlışlık',
        },
        'C',
        'Anakütleyi oluşturan bireysel kalemler örnekleme birimidir; çekler, satış faturaları, müşteri bakiyeleri ya da parasal birimler örnekleme birimi olabilir.',
    ),
    # düzey 2
    '0037': patch(
        "BDS 530'a göre istatistiksel örnekleme uygulanırken aşağıdaki seçim yöntemlerinden hangisinin kullanılması uygun değildir?",
        {
            'A': 'Rastgele seçim',
            'B': 'Tabakalı rastgele seçim',
            'C': 'Parasal birim örneklemesi',
            'D': 'Gelişigüzel seçim',
            'E': 'Sistematik seçim',
        },
        'D',
        'Gelişigüzel seçim, istatistiksel olmayan örneklemede kabul edilebilir; ancak istatistiksel örnekleme kullanıldığında uygun değildir.',
    ),
    # düzey 2
    '0038': patch(
        'Çalışma kâğıtlarının mülkiyeti ve gizliliği ile ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kalite kontrol incelemesine sunulabilir',
            'B': 'Gizlilik ilkesi çalışma kâğıtlarını da kapsar',
            'C': 'Çalışma kâğıtları denetlenen şirkete aittir',
            'D': 'Yasal zorunlulukta yetkililere verilebilir',
            'E': 'Saklama süresi boyunca silinemez',
        },
        'C',
        'Denetim dokümantasyonu denetim kuruluşunun mülkiyetindedir. Gizlilik ilkesi gereği müşteri izni ya da yasal zorunluluk olmadan üçüncü kişilere açıklanmaz.',
    ),
    # düzey 3
    '0039': patch(
        'Detay testlerinde örneklem büyüklüğünü etkileyen faktör ile bu faktörün örneklem büyüklüğüne etkisi aşağıdakilerden hangisinde doğru eşleştirilmiştir?',
        {
            'A': 'Tabakalandırma yapılır – Artar',
            'B': 'Değerlendirilen risk artar – Azalır',
            'C': 'İstenen güvence artar – Azalır',
            'D': 'Beklenen yanlışlık artar – Azalır',
            'E': 'Tolere edilebilir yanlışlık artar – Azalır',
        },
        'E',
        'Tolere edilebilir yanlışlık arttıkça örneklem küçülür. Beklenen yanlışlık, değerlendirilen risk ve istenen güvence arttıkça örneklem büyür; tabakalandırma örneklemi küçültür.',
    ),
    # düzey 3
    '0040': patch(
        "Denetçi, defter değeri 48.000.000 ₺ olan stok anakütlesinden toplam defter değeri 3.200.000 ₺ olan bir örneklem seçmiş ve örneklemde 40.000 ₺ fazla değerleme tespit etmiştir. Denetçi oran yöntemini kullanmaktadır.\n\nAnakütleye yansıtılan yanlışlık kaç ₺'dir?",
        {
            'A': '640.000 ₺',
            'B': '128.000 ₺',
            'C': '560.000 ₺',
            'D': '600.000 ₺',
            'E': '40.000 ₺',
        },
        'D',
        "Örneklemdeki yanlışlık oranı 40.000 ₺ / 3.200.000 ₺'dir. Bu oran anakütleye uygulanır: 40.000 ₺ / 3.200.000 ₺ × 48.000.000 ₺ = 600.000 ₺.",
    ),
    # düzey 3
    '0041': patch(
        "Denetçi teyit örneklemini 2.000 müşteriden oluşan anakütlenin bakiyesi 10.000 ₺'nin üzerindeki kısmından seçmiş, ancak sonucu anakütlenin tamamına genellemiştir.\n\nBDS 530'a göre bu uygulamayla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Her örnekleme birimine seçilme şansı verilmelidir',
            'B': 'Küçük bakiyeler dışarıda kaldığında sonuç genellenemez',
            'C': 'Tabakalandırma kullanılması yasak değildir',
            'D': 'Teyit, varlık iddiası için uygun bir prosedürdür',
            'E': 'Sonucun anakütlenin tamamına genellenmesi uygundur',
        },
        'E',
        'BDS 530: denetçi örneklem kalemlerini anakütledeki her örnekleme biriminin seçilme şansı olacak şekilde seçer. Küçük bakiyeler seçim dışında bırakıldığından sonuç anakütlenin tamamına genellenemez. Tabakalandırma kullanılabilir; ancak her tabakanın sonucu yalnız o tabakaya yansıtılır.',
    ),
    # düzey 3
    '0042': patch(
        "Denetim ekibinde yer almamış, ancak bağımsız denetim süreçleri, BDS'ler ve sektörün raporlama konuları hakkında makul anlayışa sahip bir denetçi dosyayı incelemektedir.\n\nBDS 230'a göre dokümantasyonla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Sözlü açıklamayla tamamlanacak ölçüde hazırlanması yeterlidir',
            'B': 'Deneyimli bir denetçinin anlayacağı ölçüde hazırlanır',
            'C': 'Uygulanan prosedürler anlaşılabilmelidir',
            'D': 'Elde edilen kanıt ve sonuçlar anlaşılabilmelidir',
            'E': 'Önemli mesleki yargılar anlaşılabilmelidir',
        },
        'A',
        'BDS 230: dokümantasyon, denetimle önceden bağlantısı olmayan deneyimli bir denetçinin uygulanan prosedürleri, elde edilen kanıtları, varılan sonuçları ve önemli mesleki yargıları anlamasını sağlayacak şekilde hazırlanır. Sözlü açıklama yeterli dokümantasyonun yerini tutmaz.',
    ),
    # düzey 2
    '0043': patch(
        "Denetçi satın alma siparişlerinin onaylanmasına ilişkin kontrolü test ederken, anakütledeki fiili sapma oranının %5'i aşmayacağına dair uygun bir güvence seviyesi elde etmek istemektedir.\n\nBDS 530'a göre %5 oranı ne ifade eder?",
        {
            'A': 'Tolere edilebilir sapma oranı',
            'B': 'Güven düzeyi',
            'C': 'Örnekleme riski',
            'D': 'Beklenen sapma oranı',
            'E': 'Örneklem sapma oranı',
        },
        'A',
        'Tolere edilebilir sapma oranı, denetçinin anakütledeki fiili sapma oranının aşmayacağına dair uygun güvence elde etmek amacıyla belirlediği iç kontrol prosedürlerinden sapma oranıdır.',
    ),
    # düzey 2
    '0044': patch(
        "Denetçi stok hesabını test ederken, anakütledeki fiili yanlışlığın 250.000 ₺'yi aşmayacağına dair uygun bir güvence seviyesi elde etmeyi amaçlamaktadır.\n\nBDS 530'a göre 250.000 ₺ tutarı nasıl adlandırılır?",
        {
            'A': 'Yansıtılmış yanlışlık',
            'B': 'Beklenen yanlışlık',
            'C': 'Anomali tutarı',
            'D': 'Tolere edilebilir yanlışlık',
            'E': 'Örnekleme aralığı',
        },
        'D',
        'Tolere edilebilir yanlışlık, denetçinin anakütledeki fiili yanlışlığın aşmayacağına dair uygun güvence elde etmek amacıyla belirlediği parasal tutardır.',
    ),
    # düzey 2
    '0045': patch(
        "Denetçi 60 kalemlik örneklemde önemli yanlışlık bulmamış ve hesabın doğru olduğu sonucuna varmıştır. Oysa aynı prosedür anakütlenin tamamına uygulansaydı önemli yanlışlık tespit edilecekti.\n\nBDS 530'a göre bu durum hangi riskin gerçekleştiğini gösterir?",
        {
            'A': 'Kontrol riski',
            'B': 'Örnekleme dışı risk',
            'C': 'İş riski',
            'D': 'Doğal risk',
            'E': 'Örnekleme riski',
        },
        'E',
        'Örnekleme riski, örnekleme dayalı sonucun aynı prosedürün anakütlenin tamamına uygulanması durumunda varılacak sonuçtan farklı olması riskidir.',
    ),
    # düzey 2
    '0046': patch(
        "BDS 530'a göre örneklem seçim yöntemleriyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Gelişigüzel seçimde bilinçli bir taraf tutulmaz',
            'B': 'Blok seçim istatistiksel örneklemin temel yöntemidir',
            'C': 'Sistematik seçimde bir örnekleme aralığı hesaplanır',
            'D': 'Rastgele seçimde rastgele sayı üreteçleri kullanılır',
            'E': 'Parasal birim örneklemesi değer ağırlıklı bir seçimdir',
        },
        'B',
        "Blok seçim örneklemede genellikle kullanılamaz; geçerli çıkarım için çok sayıda blok gerekir. Diğer ifadeler BDS 530'daki seçim yöntemlerini doğru tanımlar.",
    ),
    # düzey 3
    '0047': patch(
        'Denetçi, 7.200 kalemlik alım faturası anakütlesinden sistematik seçimle 120 kalem seçecektir. Rastgele belirlenen başlangıç noktası 23. kalemdir.\n\nSeçilecek 4. kalem anakütlenin kaçıncı kalemidir?',
        {
            'A': '203',
            'B': '143',
            'C': '92',
            'D': '240',
            'E': '263',
        },
        'A',
        "Örnekleme aralığı 7.200 / 120 = 60'tır. Başlangıç noktasından sonra her 60. kalem seçilir: 23 + (4 − 1) × 60 = 203.",
    ),
    # düzey 2
    '0048': patch(
        'Aşağıdakilerden hangisi cari dönem dosyasında yer alan belgelerden biri değildir?',
        {
            'A': 'Teyit yanıtları',
            'B': 'Banka mutabakatları',
            'C': 'Dönem sonu mizanı',
            'D': 'Kasa sayım tutanağı',
            'E': 'Uzun süreli kira sözleşmesi',
        },
        'E',
        'Uzun süreli sözleşmeler birden çok dönemi ilgilendirdiğinden sürekli dosyada tutulur; diğerleri denetlenen döneme ait kanıtlardır.',
    ),
    # düzey 2
    '0049': patch(
        "Denetçi 3.000 kalemlik ticari alacak anakütlesini 500.000 ₺ üzeri, 50.000-500.000 ₺ arası ve 50.000 ₺ altı olmak üzere üç gruba ayırmış, her gruptan ayrı örneklem seçmiştir.\n\nBDS 530'a göre bu işlem nasıl adlandırılır?",
        {
            'A': 'Yansıtma',
            'B': 'Tabakalandırma',
            'C': 'Blok seçim',
            'D': 'Parasal birim örneklemesi',
            'E': 'Sistematik seçim',
        },
        'B',
        'Tabakalandırma, anakütlenin her biri benzer özelliklere (çoğunlukla parasal değere) sahip örnekleme birimlerinden oluşan alt anakütlelere ayrılmasıdır.',
    ),
    # düzey 2
    '0050': patch(
        "BDS 530'a göre anomaliler ile ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Anomali için yüksek düzeyde kesinlik gerekir',
            'B': 'Temsil etmediği ek prosedürlerle gösterilir',
            'C': 'Anomali tutarı anakütleye yansıtılır',
            'D': 'Anomali kabulü son derece nadir durumlarda yapılır',
            'E': 'Anomali anakütleyi temsil etmeyen yanlışlıktır',
        },
        'C',
        'Yanlışlığın anomali kabul edilmesi son derece nadirdir; denetçinin ek prosedürlerle anakütleyi temsil etmediğine dair yüksek düzeyde kesinlik elde etmesi gerekir. Anomaliler yansıtma dışında tutulur, etkileri ayrıca değerlendirilir.',
    ),
    # düzey 3
    '0051': patch(
        'Kontrol testinin örneklem sonucu, denetçinin kontrole planladığı ölçüde güvenmesi için makul dayanak sağlamamıştır.\n\nAşağıdakilerden hangisi bu durumda denetçinin başvurabileceği yollardan biri değildir?',
        {
            'A': 'Risk değerlendirmesini gözden geçirmek',
            'B': 'İlgili maddi doğrulama prosedürlerinin kapsamını değiştirmek',
            'C': 'Telafi edici kontrolleri test etmek',
            'D': 'Sapma bulunan kalemleri örneklemden çıkarmak',
            'E': 'Ek kalemleri test etmek',
        },
        'D',
        'Sonuçlar dayanak sağlamazsa denetçi ek kalemleri test edebilir, telafi edici kontrolleri test edebilir ya da maddi doğrulama prosedürlerini değiştirir. Sapmalı kalemleri örneklemden çıkarmak sonucu çarpıtır.',
    ),
    # düzey 2
    '0052': patch(
        "Denetçi stok değer düşüklüğü konusunu işletmenin finans direktörüyle görüşmüştür; konu denetim açısından önemlidir.\n\nBDS 230'a göre bu görüşmeyle ilgili olarak aşağıdakilerden hangisinin belgelenmesi gerekir?",
        {
            'A': 'Görüşmenin yapıldığı yerin adresi',
            'B': 'Direktörün özgeçmişi',
            'C': 'İçeriği, zamanı ve kiminle yapıldığı',
            'D': 'Direktörün imzalı taahhüdü',
            'E': 'Görüşmenin ses kaydı',
        },
        'C',
        'Önemli konuların yönetimle ve diğer taraflarla görüşülmesi, görüşülen konuların niteliği, görüşmenin ne zaman ve kiminle yapıldığı dahil belgelenir.',
    ),
    # düzey 3
    '0053': patch(
        "Detay testinde denetçi, gerçekte önemli yanlışlık içermeyen bir hesapta örneklem sonucuna dayanarak önemli yanlışlık bulunduğu sonucuna varmıştır.\n\nBDS 530'a göre bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Görüşün uygunluğunu bozar',
            'B': 'Örnekleme dışı risktir',
            'C': 'Tolere edilebilir yanlışlığı artırır',
            'D': 'Anomali olarak ele alınır',
            'E': 'Denetimin verimliliğini etkiler',
        },
        'E',
        'Detay testinde var olmayan önemli yanlışlığın varlığı sonucuna ulaşılması verimliliği etkileyen örnekleme riskidir; ek çalışma genellikle bu sonucun hatalı olduğunu ortaya çıkarır.',
    ),
    # düzey 2
    '0054': patch(
        'Denetçi, birden çok dönemin denetiminde yararlanacağı belgeleri ayrı bir dosyada toplamaktadır.\n\nAşağıdakilerden hangisi bu sürekli dosyaya konulan belgelerden biri değildir?',
        {
            'A': 'Dönem sonu mizanı',
            'B': 'Şirket ana sözleşmesi',
            'C': 'Organizasyon şeması',
            'D': 'Uzun vadeli sözleşmeler',
            'E': 'Ortaklık yapısına ilişkin belgeler',
        },
        'A',
        'Birden çok dönemde kullanılan kalıcı bilgiler sürekli dosyada tutulur: ana sözleşme, organizasyon şeması, ortaklık yapısı ve uzun vadeli sözleşmeler gibi. Dönem sonu mizanı döneme ait olup cari dosyaya konulur.',
    ),
    # düzey 3
    '0055': patch(
        "Denetçi satış iadelerinin onaylanmasına ilişkin kontrolü test etmek için 80 kalemlik örneklem incelemiş ve 4 kalemde sapma bulmuştur. Bu kontrol için tolere edilebilir sapma oranı %4'tür.\n\nBu sonuçla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Sapmalar anomali sayılır',
            'B': 'Kontrole planlanan ölçüde güvenilemez',
            'C': 'Kontrol etkin kabul edilir',
            'D': "Örneklem sapma oranı %4'tür",
            'E': 'Tolere edilebilir oran yükseltilir',
        },
        'B',
        "Örneklem sapma oranı 4 / 80 = %5'tir ve tolere edilebilir sapma oranı olan %4'ü aşmaktadır. Denetçi kontrole planladığı ölçüde güvenemez; ek kontrolleri test edebilir veya maddi doğrulama prosedürlerini genişletir.",
    ),
    # düzey 2
    '0056': patch(
        "Bir denetim kuruluşu, bir müşteri denetimine ait kayıtları hem sunucusundaki elektronik klasörlerde hem de fiziki klasörlerde saklamaktadır.\n\nBDS 230'a göre bu klasörlerin bütünü nasıl adlandırılır?",
        {
            'A': 'Kalite kontrol kaydı',
            'B': 'Sürekli dosya',
            'C': 'Kanıt envanteri',
            'D': 'Denetim dosyası',
            'E': 'Yönetim dosyası',
        },
        'D',
        'Denetim dosyası, belirli bir denetimin dokümantasyonunu oluşturan kayıtları içeren fiziki veya elektronik ortamdaki bir ya da daha fazla klasör veya diğer depolama araçlarıdır.',
    ),
    # düzey 3
    '0057': patch(
        "Denetçi, alacakların tahsil edilebilirliğine ilişkin nihai sonucuyla tutarsız bir bilgi tespit etmiş ve tutarsızlığı ek prosedürlerle gidermiştir.\n\nBDS 230'a göre bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Tutarsız bilgi dosyadan çıkarılır',
            'B': 'Tutarsızlığın nasıl giderildiği belgelenir',
            'C': 'Konu yönetimin yazılı beyanıyla kapatılıp dosyalanır',
            'D': 'Belgeleme gerekmez',
            'E': 'Rapor tarihi ertelenir',
        },
        'B',
        'Önemli bir konuda nihai sonuçla tutarsız bilgi tespit edilmişse denetçi tutarsızlığı nasıl ele aldığını belgeler.',
    ),
    # düzey 3
    '0058': patch(
        "Denetçi, örnekleme seçtiği bir faturadaki hatanın tek bir günle sınırlı bir yazılım arızasından kaynaklandığını, arızanın aynı gün giderildiğini ve diğer günlerin işlemlerini etkilemediğini kanıtlarıyla belirlemiştir.\n\nBDS 530'a göre bu yanlışlık nasıl nitelendirilir?",
        {
            'A': 'Anomali',
            'B': 'Tolere edilebilir sapma',
            'C': 'Örnekleme riski',
            'D': 'Örnekleme dışı risk',
            'E': 'Beklenen yanlışlık',
        },
        'A',
        'Anakütledeki yanlışlıkları veya sapmaları kanıtlanabilir şekilde temsil etmeyen yanlışlık ya da sapma anomalidir.',
    ),
    # düzey 3
    '0059': patch(
        "Denetçi, alacakların varlığına ilişkin olarak dönem sonrası tahsilatların incelenmesi prosedüründen önemli güvence elde etmiştir.\n\nBDS 530'a göre aynı iddiaya yönelik teyit örneklemi için aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Örneklem küçültülebilir',
            'B': 'Tolere edilebilir yanlışlık azalır',
            'C': 'Örnekleme dışı risk artar',
            'D': 'Tüm bakiyeler teyit edilir',
            'E': 'Örneklem büyütülmelidir',
        },
        'A',
        'Aynı iddiaya odaklanmış diğer maddi doğrulama prosedürlerinden alınan güvence arttıkça detay testi örneklem büyüklüğü azalır.',
    ),
    # düzey 3
    '0060': patch(
        'Denetlenen bir şirketin rakibi, denetçiden bu şirketin denetimine ait çalışma kâğıtlarını incelemek istemiştir.\n\nBu taleple ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Gizlilik ilkesi uygulanır',
            'B': 'Müşterinin izni olmadan paylaşılamaz',
            'C': 'Denetim raporu yayımlandıktan sonra rakibe verilebilir',
            'D': 'Yasal bir zorunluluk varsa paylaşılabilir',
            'E': 'Ücret karşılığında paylaşım yapılamaz',
        },
        'C',
        'Gizlilik ilkesi gereği denetçi, müşteriden izin alınmadıkça ya da yasal veya mesleki bir yükümlülük bulunmadıkça denetimde elde ettiği bilgileri üçüncü kişilere açıklayamaz; raporun yayımlanması ya da ücret bu sonucu değiştirmez.',
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
    print(f"1 paket / {len(PATCHES)} soru ('Örnekleme ve Çalışma Kâğıtları' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
