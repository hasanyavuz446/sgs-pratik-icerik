#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Denetim — gerçek SGS profiline kalibrasyon yamaları.

Ölçülen sapma: denetim paketlerinde olumsuz kök oranı %1-8 iken 2026 SGS denetim
bloğunda %46,9; öncüllü soru oranı %5-8 iken %12,5'tir
(bkz. reports/SGS_CIKMIS_SORULAR_ANALIZI_2026-07-22.md, URETIM_KURALLARI §1-§2).
Bu builder seçilen soruları olumsuz köke (4 doğru + 1 yanlış ifade) ve öncüllü yapıya
dönüştürür. §5: yanlış ifade boy/ayrıntı bakımından ayırt edilmez. §7: öncüllerde tek
kombinasyon baskın değildir ve "Yalnız X" en az bir soruda doğrudur. ID'ler korunur.

    --check : iki repoyu karşılaştır (fark varsa çıkış 1)
    --write : içerik + uygulama repolarına yaz
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
# denetim_kavrami.json -> build_denetim_kavrami_onarim.py (tek sahip)
ICKONTROL_RELATIVE_PATH = 'content/denetim/ic_kontrol.json'
STYLE_REF = 'SGS Denetim (olumsuz kök ve öncül ağırlığı 2026 sınav profiline kalibre)'


def audit_patch(stem, options, answer, solution, legislation_ref):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF, "legislationRef": legislation_ref},
        "validYear": 2026, "mockExamId": None,
    }



ICKONTROL_PATCHES = {
    'den-ickontrol-gen-0001': audit_patch(
        'İç kontrol sistemi ile ilgili aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'İşletme amaçlarına ulaşılmasına makul güvence sağlamak üzere tasarlanmış süreçler bütünüdür',
            'B': 'Yönetim ve tüm çalışanların katılımıyla işleyen bir süreçtir',
            'C': 'Yalnızca muhasebe kayıtlarının doğruluğunu sağlamaya yönelik bir belge düzeninden oluşur',
            'D': 'Varlıkların korunmasını ve kayıtların güvenilirliğini amaçlar',
            'E': 'Yasa ve düzenlemelere uygunluğun sağlanmasına katkı verir',
        },
        'C',
        'İç kontrol yalnızca bir **belge düzeni veya muhasebe kontrolü** değildir; kontrol ortamı, risk değerlendirme, kontrol faaliyetleri, bilgi-iletişim ve izlemeyi kapsayan, faaliyetlerin etkinliği ile mevzuata uygunluğu da hedefleyen bütünsel bir süreçtir. Diğer ifadeler doğrudur.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0003': audit_patch(
        'İç kontrol sisteminin sorumluluğu bakımından aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'Sistemin kurulması ve işletilmesi bağımsız denetçinin sorumluluğundadır',
            'B': 'Sistemin kurulması ve sürdürülmesi öncelikle işletme yönetiminin sorumluluğundadır',
            'C': 'İç denetim birimi sistemin etkinliğini değerlendirerek yönetime katkı sağlar',
            'D': 'Tüm çalışanlar kendi görev alanlarındaki kontrollerin işletilmesinden sorumludur',
            'E': 'Bağımsız denetçi sistemi kurmaz, denetim planlaması için değerlendirir',
        },
        'A',
        'İç kontrolü kurmak ve sürdürmek **yönetimin** sorumluluğudur. Bağımsız denetçi sistemi kurmaz veya işletmez; yalnızca denetimini planlamak ve kontrol riskini belirlemek için sistemi anlar ve değerlendirir. Diğer ifadeler doğrudur.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0004': audit_patch(
        'İç kontrolün sağladığı güvence düzeyi bakımından aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'İşletme amaçlarına ulaşılmasına makul güvence sağlar',
            'B': 'İnsan hatası nedeniyle her zaman bir başarısızlık olasılığı bulunur',
            'C': 'Çalışanların gizlice anlaşması kontrolleri etkisiz bırakabilir',
            'D': 'Maliyet-fayda dengesi nedeniyle her risk için kontrol kurulamaz',
            'E': 'Hata ve hilenin hiç oluşmayacağına dair mutlak güvence sağlar',
        },
        'E',
        'İç kontrol **makul güvence** sağlar; insan hatası, danışıklı hareket (muvazaa), yönetimin kontrolleri aşması ve maliyet-fayda dengesi gibi doğal kısıtlar nedeniyle mutlak güvence mümkün değildir. Diğer ifadeler doğrudur.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0007': audit_patch(
        "Aşağıdakilerden hangisi COSO modelinde 'kontrol ortamı' bileşeni kapsamında YER ALMAZ?",
        {
            'A': 'Tepe yönetimin dürüstlük ve etik değerlere verdiği önem',
            'B': 'Banka hesaplarının ekstre ile düzenli olarak mutabakatının yapılması',
            'C': 'Örgüt yapısı ile yetki ve sorumlulukların belirlenmiş olması',
            'D': 'İnsan kaynakları politikaları ve personelin yeterliği',
            'E': 'Yönetimin kontrole ilişkin tutum ve bilinç düzeyi',
        },
        'B',
        'Banka mutabakatı somut bir **kontrol faaliyetidir** (ortaya çıkarıcı kontrol). Kontrol ortamı ise sistemin temelini oluşturan tutum, değerler, örgüt yapısı, yetki-sorumluluk düzeni ve personel politikalarıdır.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0008': audit_patch(
        "COSO bileşenlerinden 'risk değerlendirme' ile ilgili aşağıdakilerden hangisi YANLIŞTIR?",
        {
            'A': 'İşletme amaçlarını tehdit eden risklerin belirlenmesini içerir',
            'B': 'Belirlenen risklerin olasılık ve etkisinin analiz edilmesini içerir',
            'C': 'Risklere karşı nasıl yanıt verileceğinin kararlaştırılmasını içerir',
            'D': 'Yalnızca kuruluş aşamasında bir kez yapılan ve sonradan tekrarlanmayan bir çalışmadır',
            'E': 'İş koşulları değiştikçe yeni risklerin dikkate alınmasını gerektirir',
        },
        'D',
        'Risk değerlendirme **süreklidir**; işletmenin faaliyetleri, mevzuat ve teknoloji değiştikçe yeni riskler doğar ve değerlendirme güncellenir. Tek seferlik bir çalışma değildir. Diğer ifadeler doğrudur.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0009': audit_patch(
        "Aşağıdakilerden hangisi COSO modelinde 'kontrol faaliyetleri' kapsamında YER ALMAZ?",
        {
            'A': 'Yetkilendirme ve onay mekanizmaları',
            'B': 'Görevler ayrılığının uygulanması',
            'C': 'Tepe yönetimin etik değerlere ilişkin genel tutumu',
            'D': 'Fiziki koruma ve erişim kısıtlamaları',
            'E': 'Kayıt ve belgelerin bağımsız biçimde karşılaştırılması',
        },
        'C',
        'Tepe yönetimin etik tutumu **kontrol ortamı** bileşenine aittir. Kontrol faaliyetleri; yetkilendirme-onay, görevler ayrılığı, fiziki koruma-erişim kontrolleri ve bağımsız karşılaştırma/mutabakat gibi somut uygulamalardır.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0010': audit_patch(
        "COSO bileşenlerinden 'izleme (gözetim)' ile ilgili aşağıdakilerden hangisi YANLIŞTIR?",
        {
            'A': 'Yalnızca bağımsız denetçinin yıl sonunda yaptığı incelemeden oluşur',
            'B': 'İç kontrol sisteminin etkin işlemeye devam edip etmediğinin değerlendirilmesidir',
            'C': 'Sürekli izleme faaliyetleri ile ayrı değerlendirmeleri kapsar',
            'D': 'İç denetim birimi izleme işlevine katkı sağlar',
            'E': 'Tespit edilen eksikliklerin uygun düzeyde yönetime bildirilmesini gerektirir',
        },
        'A',
        'İzleme, işletmenin **kendi** iç kontrol sistemine ilişkin sürekli gözetimi ve ayrı değerlendirmelerini içerir; bağımsız denetçinin yıl sonu incelemesiyle sınırlı değildir. Diğer ifadeler doğrudur.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0011': audit_patch(
        "'Görevler ayrılığı' ilkesi ile ilgili aşağıdakilerden hangisi YANLIŞTIR?",
        {
            'A': 'İşlemi yetkilendirme, yürütme, kayıt ve varlığı koruma işlevlerinin ayrı kişilerde olmasını gerektirir',
            'B': 'Bir kişinin hem hatayı yapıp hem gizleyebilmesi olasılığını azaltır',
            'C': 'Hile riskini azaltan temel kontrol faaliyetlerinden biridir',
            'D': 'Küçük işletmelerde personel sayısı yetersizse telafi edici kontrollerle desteklenir',
            'E': 'Bu ilke uygulandığında çalışanların gizlice anlaşması dahi kontrolü etkisiz bırakamaz',
        },
        'E',
        'Görevler ayrılığı, **danışıklı hareket (muvazaa)** karşısında etkisiz kalabilir; iki veya daha fazla kişinin gizlice anlaşması iç kontrolün bilinen doğal kısıtlarındandır. Diğer ifadeler doğrudur.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0013': audit_patch(
        "Aşağıdakilerden hangisi bir 'kontrol faaliyeti' örneği DEĞİLDİR?",
        {
            'A': 'Ödemelerin yetkili kişinin onayına bağlanması',
            'B': 'İşletmenin genel ekonomik konjonktüre ilişkin beklentilerinin tartışılması',
            'C': 'Stokların kilitli ve erişimi sınırlı alanlarda tutulması',
            'D': 'Belgelerin önceden sıra numaralı basılması ve numaraların hesabının tutulması',
            'E': 'Banka kayıtlarının ekstre ile düzenli mutabakatının yapılması',
        },
        'B',
        'Genel ekonomik beklentilerin tartışılması bir **kontrol faaliyeti** değildir; olsa olsa risk değerlendirmesine girdi sağlar. Kontrol faaliyetleri onay, fiziki koruma, belge düzeni ve mutabakat gibi somut uygulamalardır.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0015': audit_patch(
        "COSO bileşenlerinden 'bilgi ve iletişim' ile ilgili aşağıdakilerden hangisi YANLIŞTIR?",
        {
            'A': 'Gerekli bilginin doğru, zamanında ve ilgili kişilere ulaşmasını sağlar',
            'B': 'Çalışanların kontrol sorumluluklarını anlamasına katkı verir',
            'C': 'İşletme içi ve dışı iletişim kanallarını kapsar',
            'D': 'Yalnızca bilgi işlem donanımının satın alınmasıyla sağlanır',
            'E': 'Kontrol eksikliklerinin uygun düzeye bildirilmesini içerir',
        },
        'D',
        'Bilgi ve iletişim bileşeni **donanım alımına indirgenemez**; doğru bilginin zamanında üretilip ilgili kişilere ulaşmasını sağlayan süreç ve kanalların tümünü kapsar. Diğer ifadeler doğrudur.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0017': audit_patch(
        "İç kontrolün 'finansal raporlamanın güvenilirliği' amacı bakımından aşağıdakilerden hangisi YANLIŞTIR?",
        {
            'A': 'İşlemlerin doğru tutarla ve doğru dönemde kaydedilmesini hedefler',
            'B': 'Finansal tabloların geçerli çerçeveye uygun hazırlanmasına katkı sağlar',
            'C': 'Finansal tablolar hakkında üçüncü taraflara bağımsız denetim görüşü verilmesini kapsar',
            'D': 'Kayıtların yetkisiz değiştirilmesini engellemeyi hedefler',
            'E': 'Raporlanan bilgilerin dayanaklarıyla desteklenmesini hedefler',
        },
        'C',
        'Bağımsız denetim görüşü vermek **bağımsız denetçinin** işidir; iç kontrolün amacı değildir. İç kontrol, güvenilir bilgi üretimini sağlayacak süreçleri kurar. Diğer ifadeler doğrudur.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0023': audit_patch(
        "İç kontrolde 'maliyet-fayda dengesi' kısıtı bakımından aşağıdakilerden hangisi YANLIŞTIR?",
        {
            'A': 'Maliyeti ne olursa olsun tüm riskler için kontrol kurulması zorunludur',
            'B': 'Bir kontrolün maliyeti sağlayacağı yarardan yüksekse kurulması beklenmez',
            'C': 'Bu nedenle her risk için ayrı bir kontrol kurulamaz',
            'D': 'Kontrollerin kapsamı riskin önemine göre belirlenir',
            'E': 'Bu kısıt iç kontrolün mutlak güvence sağlayamamasının nedenlerindendir',
        },
        'A',
        'Maliyet-fayda dengesi gereği **her risk için kontrol kurulması zorunlu değildir**; kontrolün maliyeti beklenen yararı aşıyorsa kurulmaz. Bu durum iç kontrolün doğal kısıtlarından biridir. Diğer ifadeler doğrudur.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0026': audit_patch(
        'Bağımsız denetçinin iç kontrol sistemini incelemesi bakımından aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'Denetimin niteliğini, zamanlamasını ve kapsamını belirlemeye yardımcı olur',
            'B': 'Kontrol riskinin değerlendirilmesini sağlar',
            'C': 'Yanlışlığın oluşabileceği alanların belirlenmesine katkı verir',
            'D': 'Kontrollere güvenilip güvenilmeyeceğine karar verilmesini sağlar',
            'E': 'Amacı, işletmenin iç kontrol sistemini denetçinin kurup geliştirmesidir',
        },
        'E',
        'Denetçi iç kontrolü **kurmaz veya geliştirmez**; sistemi anlamasının amacı denetim stratejisini belirlemek ve kontrol riskini değerlendirmektir. Sistemi kurmak yönetimin görevidir. Diğer ifadeler doğrudur.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0027': audit_patch(
        "'Kontrol testi (kontrol dayanıklılık testi)' bakımından aşağıdakilerden hangisi YANLIŞTIR?",
        {
            'A': 'Kontrollerin uygulamada etkin işleyip işlemediğini araştırır',
            'B': 'Hesap bakiyelerinin tutarsal doğruluğunu ölçmeyi amaçlar',
            'C': 'Kontrollere güvenilecekse yapılması gerekir',
            'D': 'Sonucu maddi doğrulama testlerinin kapsamını etkiler',
            'E': 'Örneğin onay imzalarının varlığının incelenmesi bir kontrol testidir',
        },
        'B',
        'Hesap bakiyelerinin tutarsal doğruluğunu ölçen testler **maddi doğrulama (tutar) testleridir**. Kontrol testi, kontrolün tasarlandığı gibi işleyip işlemediğini araştırır. Diğer ifadeler doğrudur.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0029': audit_patch(
        'Aşağıdakilerden hangisi güçlü bir iç kontrol ortamının göstergesi DEĞİLDİR?',
        {
            'A': 'Yetki ve sorumlulukların yazılı olarak belirlenmiş olması',
            'B': 'Tepe yönetimin etik değerlere açık biçimde önem vermesi',
            'C': 'Görevler ayrılığının fiilen uygulanıyor olması',
            'D': 'Yönetimin kurulu kontrolleri kendi kararıyla sık sık devre dışı bırakması',
            'E': 'Personelin işe alım ve eğitiminde yeterliğin gözetilmesi',
        },
        'D',
        'Yönetimin kontrolleri kendi kararıyla aşması (**management override**) kontrol ortamını zayıflatan en ciddi göstergelerden biridir; güçlü ortam göstergesi değildir. Diğer seçenekler güçlü kontrol ortamına işaret eder.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0049': audit_patch(
        "COSO'nun beş bileşeninin birbiriyle ilişkisi bakımından aşağıdakilerden hangisi YANLIŞTIR?",
        {
            'A': 'Bileşenler birbirini destekleyen bütünleşik bir yapı oluşturur',
            'B': 'Kontrol ortamı diğer bileşenlerin üzerine kurulduğu temeldir',
            'C': 'Bileşenler birbirinden bağımsız çalışır; birinin varlığı diğerlerini etkilemez',
            'D': 'Bir bileşendeki zayıflık sistemin bütününün etkinliğini azaltabilir',
            'E': 'İzleme, diğer bileşenlerin işleyişinin sürekli değerlendirilmesini sağlar',
        },
        'C',
        'COSO bileşenleri **bütünleşiktir**; birbirinden bağımsız değildir. Örneğin kontrol ortamı zayıfsa, iyi tasarlanmış kontrol faaliyetleri bile etkisiz kalabilir. Diğer ifadeler doğrudur.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0056': audit_patch(
        "İç kontrolde 'tepe yönetiminin tutumu (tone at the top)' bakımından aşağıdakilerden hangisi YANLIŞTIR?",
        {
            'A': 'Yalnızca yazılı bir etik kuralın varlığıyla sağlanmış sayılır',
            'B': 'Yönetimin dürüstlük ve etik değerlere verdiği önemi yansıtır',
            'C': 'Çalışanların kontrol bilincini doğrudan etkiler',
            'D': 'Kontrol ortamı bileşeninin en belirleyici unsurlarından biridir',
            'E': 'Yönetimin davranışlarıyla örnek olmasını gerektirir',
        },
        'A',
        'Tone at the top yalnızca **yazılı bir belgeyle** sağlanmaz; yönetimin fiilî davranışları, kontrollere verdiği önem ve örnek oluşu belirleyicidir. Yazılı kural uygulanmıyorsa kontrol ortamı zayıf kalır. Diğer ifadeler doğrudur.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0021': audit_patch(
        'İç kontrolün doğal (yapısal) kısıtları ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İnsan hatası, iyi tasarlanmış kontrollerin bile beklendiği gibi işlememesine yol açabilir.\n\nII. Çalışanların gizlice anlaşması (muvazaa) görevler ayrılığı kontrolünü etkisiz bırakabilir.\n\nIII. İyi tasarlanmış bir iç kontrol sistemi hata ve hile olasılığını tümüyle ortadan kaldırır.',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'B',
        '**III yanlıştır:** iç kontrol mutlak değil **makul güvence** sağlar; hata ve hile olasılığı tümüyle ortadan kalkmaz. **I** insan hatası ve **II** danışıklı hareket, iç kontrolün bilinen doğal kısıtlarındandır.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0038': audit_patch(
        'İç kontrol ile kontrol riski arasındaki ilişki konusunda aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kontrol riski, denetçinin kendi denetim yordamlarıyla doğrudan azaltabildiği bir risktir.\n\nII. İç kontrol güçlü ve etkin işlediğinde kontrol riski düşer.\n\nIII. Kontrol riski, işletmenin iç kontrolünün önemli bir yanlışlığı önleyememe ya da bulup düzeltememe riskidir.',
        {
            'A': 'Yalnız II',
            'B': 'I ve II',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'D',
        '**I yanlıştır:** kontrol riski **işletmenin** iç kontrolüne ait bir risktir; denetçi bunu doğrudan azaltamaz, yalnızca değerlendirir ve buna göre kendi tespit (bulgu) riskini yönetir. **II** ve **III** doğru ifadelerdir.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0042': audit_patch(
        'Kontrol türleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Önleyici kontroller, hata veya hilenin oluşmasını baştan engellemeyi amaçlar.\n\nII. Ortaya çıkarıcı (bulucu) kontroller, oluşmuş bir hata veya hileyi tespit etmeyi amaçlar.\n\nIII. Etkin bir sistemde önleyici ve ortaya çıkarıcı kontroller birlikte kullanılır.',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'E',
        'Üç ifade de doğrudur. Önleyici kontroller (onay, yetkilendirme, görevler ayrılığı) hatayı baştan engeller; ortaya çıkarıcı kontroller (mutabakat, sayım, bağımsız gözden geçirme) oluşmuş hatayı bulur. Etkin bir sistemde ikisi **birlikte** tasarlanır; yalnız birine dayanmak yetersiz kalır.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
    'den-ickontrol-gen-0052': audit_patch(
        'İç kontrolün amaçları ve sorumluluğu ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İç kontrol, işletmenin kâr elde etmesini garanti altına almayı amaçlar.\n\nII. İç kontrolün amaçları arasında yasa ve düzenlemelere uygunluğun sağlanması yer alır.\n\nIII. İç kontrol sisteminin kurulması bağımsız denetçinin sorumluluğundadır.',
        {
            'A': 'Yalnız II',
            'B': 'I ve II',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'A',
        '**I yanlıştır:** iç kontrol kârı garanti etmez; faaliyetlerin etkinliği, raporlamanın güvenilirliği ve mevzuata uygunluk konusunda makul güvence sağlar. **III yanlıştır:** sistemi kurmak **yönetimin** sorumluluğudur. Yalnızca **II** doğrudur.',
        'Denetim - iç kontrol sistemi (COSO)',
    ),
}





PATCHES_BY_PATH = {
    ICKONTROL_RELATIVE_PATH: ICKONTROL_PATCHES,
}


def apply_or_check(path, patches, write):
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    by_id = {q["id"]: q for q in questions}
    mismatches = []
    for qid, fields in patches.items():
        q = by_id.get(qid)
        if q is None:
            raise SystemExit(f"Soru bulunamadı: {path}::{qid}")
        for field, expected in fields.items():
            if q.get(field) != expected:
                mismatches.append(f"{path}::{qid}.{field}")
                if write:
                    q[field] = expected
        if write and len(set(q["options"].values())) != 5:
            raise SystemExit(f"Seçenek çakışması: {path}::{qid}")
    if write:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return mismatches


def main():
    ap = argparse.ArgumentParser(); g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true"); g.add_argument("--write", action="store_true")
    args = ap.parse_args()
    mismatches = []
    for rel, patches in PATCHES_BY_PATH.items():
        for path in (ROOT / rel, APP_ROOT / rel):
            mismatches.extend(apply_or_check(path, patches, args.write))
    if args.check and mismatches:
        print("Eşleşmeyen alanlar:")
        for m in mismatches: print(f"- {m}")
        return 1
    total = sum(len(p) for p in PATCHES_BY_PATH.values())
    print(f"{len(PATCHES_BY_PATH)} paket / {total} soru (denetim profil kalibrasyonu) iki repoda doğrulandı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
