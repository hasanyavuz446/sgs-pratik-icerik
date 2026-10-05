#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""İç Kontrol — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Denetim turu (gerçek denetim bloğu 73-88 ile ölçüldü; BDS 265 eksiklik bildirimi ve BDS 610/402 havuzda yoktu). Paket baştan yazıldı: iç kontrolün amaçları ve sorumluluk, BDS 315'teki beş bileşen, BT genel ve uygulama kontrolleri, görevler ayrılığı ve kontrol türleri, yapısal kısıtlar, BDS 265, BDS 610, BDS 402 ve denetçinin kontrol değerlendirmesinin sonuçları. 2026-10-05: gerçek sınavda denetim köklerinin %46'sı olumsuz; 11 soru dört doğru ifadeli olumsuz köke çevrildi (aynı paketteki başka sorunun cevabını sızdıran çeldiriciler ayıklandı).

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: BDS 315, 265, 610, 402, 330; COSO İç Kontrol Çerçevesi
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/denetim/ic_kontrol.json"
STYLE_REF = 'SGS Denetim (standarda atıflı/olay kök + kısa şık; gerçek sınav profili)'
ONEK = "den-ickontrol-gen-"


def patch(stem, options, answer, solution, ref='BDS 315; BDS 265; BDS 610; BDS 402; COSO'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Stokların sayımının, stokları koruyan depo sorumlusu dışındaki bir ekip tarafından yapılmasının temel nedeni aşağıdakilerden hangisidir?',
        {
            'A': 'Sayım maliyetini düşürmek',
            'B': 'Stokların satış fiyatlarını güncellemek ve indirim kampanyalarını planlamak',
            'C': 'Görevler ayrılığını sağlamak',
            'D': 'Depo sorumlusunun iş yükünü artırmak',
            'E': 'Sayım süresini kısaltmak',
        },
        'C',
        'Varlığı koruyan kişinin sayımı da yapması eksiklikleri gizleme imkânı verir; bağımsız sayım görevler ayrılığının gereğidir.',
    ),
    # düzey 3
    '0002': patch(
        'Kontrol testleri, iç kontrollerin etkin işlemediğini göstermiştir.\n\nBu sonucun denetime etkileriyle ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kontrol riski yüksek değerlendirilir',
            'B': 'Eksiklikler yönetime bildirilebilir',
            'C': 'Prosedürler dönem sonuna yakın uygulanabilir',
            'D': 'Kabul edilebilir tespit riski yükseltilir',
            'E': 'Maddi doğrulama prosedürleri genişletilir',
        },
        'D',
        'Kontroller etkin işlemiyorsa kontrol riski yüksek değerlendirilir; bu durumda kabul edilebilir tespit riski düşer ve maddi doğrulama kapsamı genişletilir. Tespit riskinin yükseltilmesi tersi bir sonuçtur.',
    ),
    # düzey 3
    '0003': patch(
        "BDS 610'a göre aşağıdaki alanlardan hangisinde iç denetim çalışmalarından yararlanma düzeyinin daha düşük olması gerekir?",
        {
            'A': 'Önemli muhakeme gerektiren alanlar',
            'B': 'Rutin ve düşük riskli alanlar',
            'C': 'Basit mutabakatlar',
            'D': 'Kayıtların aritmetik kontrolü',
            'E': 'Sabit kıymet listesi kontrolü',
        },
        'A',
        'Planlama ve yürütmede önemli muhakeme gerektiren, değerlendirilen riskin yüksek olduğu alanlarda denetçi işin daha büyük kısmını kendisi yapar ve iç denetimden daha az yararlanır.',
    ),
    # düzey 3
    '0004': patch(
        'I. Faaliyetlerin etkinliği ve verimliliği\nII. Finansal raporlamanın güvenilirliği\nIII. Yürürlükteki mevzuata uyum\n\nYukarıdakilerden hangileri iç kontrolün amaçları arasındadır?',
        {
            'A': 'II ve III',
            'B': 'I ve III',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'E',
        'İç kontrolün amaçları faaliyetlerin etkinliği ve verimliliği, raporlamanın güvenilirliği ve mevzuata uyumdur.',
    ),
    # düzey 2
    '0005': patch(
        "BDS 315'e göre aşağıdakilerden hangisi işletmenin iç kontrol sisteminin bileşenlerinden biri değildir?",
        {
            'A': 'Bilgi sistemi ve iletişim',
            'B': 'Bağımsız denetim',
            'C': 'Kontrol faaliyetleri',
            'D': 'İşletmenin risk değerlendirme süreci',
            'E': 'Kontrol çevresi',
        },
        'B',
        'İç kontrol sisteminin bileşenleri kontrol çevresi, işletmenin risk değerlendirme süreci, iç kontrol sistemini izleme süreci, bilgi sistemi ve iletişim ile kontrol faaliyetleridir. Bağımsız denetim iç kontrolün bileşeni değildir.',
    ),
    # düzey 3
    '0006': patch(
        'Bir şirkette satın alma siparişini veren, malı teslim alan ve faturayı ödeyen kişi aynı çalışandır.\n\nBu durum aşağıdakilerden hangisine yol açabilir?',
        {
            'A': 'Vergi yükünün azalmasına',
            'B': 'Satışların artmasına',
            'C': 'Stok devir hızının artmasına',
            'D': 'Pazarlık gücünün artmasına',
            'E': 'Hayali alımların gizlenmesine',
        },
        'E',
        'Birbiriyle çatışan görevlerin aynı kişide toplanması, hayali alım ve ödemelerin ya da varlıkların kötüye kullanılmasının gizlenmesine imkân verir.',
    ),
    # düzey 3
    '0007': patch(
        'Bir şirket, döviz kurlarındaki dalgalanmaların finansal tablolar üzerindeki etkisini belirleyip olasılığını ve büyüklüğünü değerlendirerek karşılık verme kararları almaktadır.\n\nBu faaliyet hangi bileşen kapsamındadır?',
        {
            'A': 'Döviz pozisyonu raporlama ve izleme süreci',
            'B': 'Risk değerlendirme süreci',
            'C': 'İzleme süreci',
            'D': 'Kontrol çevresi',
            'E': 'Bilgi sistemi ve iletişim',
        },
        'B',
        'İşletmenin risk değerlendirme süreci, finansal raporlama amaçlarıyla ilgili iş risklerinin belirlenmesini, öneminin ve olasılığının değerlendirilmesini ve bunlara karşılık verilmesini kapsar.',
    ),
    # düzey 2
    '0008': patch(
        'Bir işletmenin bilgi işlem ortamında kullanıcıların yalnızca görevleri için gerekli ekranlara erişebilmesi sağlanmıştır.\n\nBu düzenleme aşağıdakilerden hangisine örnektir?',
        {
            'A': 'Performans incelemesi',
            'B': 'Bağımsız denetçinin uyguladığı yeniden uygulama prosedürü',
            'C': 'Fiziki sayım',
            'D': 'Erişim kontrolü',
            'E': 'Risk değerlendirme süreci',
        },
        'D',
        'Kullanıcı erişimlerinin göreve göre sınırlandırılması BT genel kontrolleri içindeki erişim kontrolüdür.',
    ),
    # düzey 3
    '0009': patch(
        "Denetçi, önemli eksiklik olarak nitelendirmediği ancak yönetimin dikkatini hak ettiğini düşündüğü bazı iç kontrol eksiklikleri tespit etmiştir.\n\nBDS 265'e göre bu eksiklikler için hangisi doğrudur?",
        {
            'A': 'Kamuoyuna duyurulur',
            'B': 'Bildirilmez',
            'C': 'Uygun yönetim kademesine bildirilir',
            'D': 'Görüşü değiştirir',
            'E': 'Kilit denetim konusu yapılır',
        },
        'C',
        'Denetçi, yönetimin dikkatini hak eden diğer eksiklikleri de uygun yönetim kademesine zamanında bildirir.',
    ),
    # düzey 2
    '0010': patch(
        "BDS 265'e göre denetçinin önemli eksikliklere ilişkin yazılı bildiriminde aşağıdakilerden hangisi yer almaz?",
        {
            'A': 'İç kontrolün etkin olduğuna dair görüş',
            'B': 'Bildirimin kullanımına ilişkin sınırlama',
            'C': 'Denetimin amacının iç kontrol hakkında görüş vermek olmadığı',
            'D': 'Eksikliklerin tanımı ve olası etkileri',
            'E': 'Bildirimin amacına ilişkin açıklama',
        },
        'A',
        'Yazılı bildirimde eksikliklerin tanımı ve olası etkileri ile denetimin amacının iç kontrolün etkinliği hakkında görüş vermek olmadığına ilişkin açıklama yer alır; iç kontrolün etkin olduğuna dair bir görüş verilmez.',
    ),
    # düzey 2
    '0011': patch(
        'Belgelerin önceden müteselsil sıra numarasıyla basılması ve kullanılmayan numaraların açıklanması aşağıdakilerden hangisinin sağlanmasına yardımcı olur?',
        {
            'A': 'Personelin performans primlerinin hesaplanması',
            'B': 'Satış fiyatlarının artırılması',
            'C': 'Vergi borcunun azaltılması',
            'D': 'Stokların değerlenmesi',
            'E': 'İşlemlerin tam kaydedilmesi',
        },
        'E',
        'Sıra numaralı belgelerin izlenmesi, eksik ya da atlanan belgelerin tespitini sağlayarak işlemlerin tamlığına katkıda bulunur.',
    ),
    # düzey 2
    '0012': patch(
        'Aşağıdakilerden hangisi iç denetimin örgütsel bağımsızlığını güçlendiren düzenlemelerden biri değildir?',
        {
            'A': 'Kayıtlara ve personele erişim hakkı tanınması',
            'B': 'Atama ve görevden almanın yönetim kurulunca yapılması',
            'C': 'Denetim komitesine doğrudan raporlaması',
            'D': 'İç denetimin muhasebe müdürüne bağlanması',
            'E': 'Denetim planının denetim komitesince onaylanması',
        },
        'D',
        'İç denetimin denetlediği birimlerden birine, örneğin muhasebe müdürüne bağlanması tarafsızlığını zayıflatır. Denetim komitesine raporlama, atamanın üst yönetimce yapılması ve erişim hakkı bağımsızlığı güçlendirir.',
    ),
    # düzey 3
    '0013': patch(
        'Bir şirkette yönetim kurulu, dürüstlük ve etik değerlere ilişkin davranış kurallarını yazılı hâle getirmiş, ihlallerde yaptırım uygulamakta ve yöneticilere yetki ve sorumlulukları açıkça dağıtmaktadır.\n\nBu uygulamalar hangi bileşen kapsamındadır?',
        {
            'A': 'Risk değerlendirme süreci',
            'B': 'Kontrol çevresi',
            'C': 'Mevzuata uyum ve yaptırım süreci',
            'D': 'İzleme süreci',
            'E': 'Bilgi sistemi ve iletişim',
        },
        'B',
        'Kontrol çevresi; yönetişim ve yönetim işlevlerini, dürüstlük ve etik değerlere bağlılığı, yetki ve sorumlulukların dağıtılmasını ve yetkinliğe bağlılığı kapsar.',
    ),
    # düzey 2
    '0014': patch(
        "BDS 265'e göre iç kontroldeki önemli eksiklikler kime ve nasıl bildirilir?",
        {
            'A': 'Denetim raporunun görüş bölümünde pay sahiplerine',
            'B': 'Muhasebe müdürüne sözlü olarak',
            'C': 'Kamuoyuna basın yoluyla',
            'D': 'Vergi idaresine sözlü olarak',
            'E': 'Üst yönetimden sorumlu olanlara yazılı olarak',
        },
        'E',
        'Denetçi, denetim sırasında tespit ettiği önemli eksiklikleri zamanında ve yazılı olarak üst yönetimden sorumlu olanlara bildirir.',
    ),
    # düzey 2
    '0015': patch(
        "BDS 315'e göre BT genel kontrolleri ile ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Uygulama kontrollerinin sürekli işleyişini destekler',
            'B': 'BT operasyonlarına ilişkin kontrolleri içerir',
            'C': 'Veri yedekleme ve kurtarma işlemlerini içerir',
            'D': 'Tek bir işlemin tutarını denetler',
            'E': 'Kullanıcı erişimlerinin yönetimini kapsar',
        },
        'D',
        'BT genel kontrolleri; erişim yönetimi, program değişiklikleri, yedekleme ve BT operasyonları gibi bilgi sisteminin bütününe ilişkin kontrollerdir ve uygulama kontrollerinin sürekli işleyişini destekler. Tek bir işlemin tutarını denetleyen kontroller uygulama kontrolüdür.',
    ),
    # düzey 2
    '0016': patch(
        'Tepe yönetimin tutumu iç kontrol açısından en çok hangi bileşeni etkiler?',
        {
            'A': 'Risk değerlendirme süreci',
            'B': 'Kontrol çevresi',
            'C': 'İzleme süreci',
            'D': 'Bilgi sistemi ve iletişim',
            'E': 'Bilgi teknolojileri genel kontrolleri',
        },
        'B',
        'Yönetimin felsefesi, işletme tarzı ve dürüstlüğe verdiği önem kontrol çevresini, dolayısıyla tüm iç kontrol sisteminin temelini belirler.',
    ),
    # düzey 2
    '0017': patch(
        'Bağımsız denetçinin finansal tablo denetiminde iç kontrolü anlaması ile ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Önemli yanlışlık risklerinin belirlenmesine yardımcı olur',
            'B': 'İleri denetim prosedürlerinin tasarımına dayanak oluşturur',
            'C': 'İç kontrol hakkında ayrı görüş vermek için yapılır',
            'D': 'Kontrollerin tasarımının değerlendirilmesini kapsar',
            'E': 'Kontrollerin uygulanıp uygulanmadığının belirlenmesini içerir',
        },
        'C',
        'Denetçi iç kontrolü riskleri belirlemek ve ileri prosedürleri tasarlamak için anlar; kontrollerin tasarımını ve uygulanıp uygulanmadığını değerlendirir. Finansal tablo denetiminde iç kontrolün etkinliği hakkında ayrı bir görüş verilmez.',
    ),
    # düzey 2
    '0018': patch(
        "BDS 265'e göre aşağıdakilerden hangisi bir iç kontrol eksikliği sayılmaz?",
        {
            'A': 'Kontrolün yanlış tasarlanması',
            'B': 'Kontrolü yürüten kişinin yeterli yetkinliğe sahip olmaması',
            'C': 'Kontrolün tasarlandığı gibi uygulanmaması',
            'D': 'Denetçinin zamanının yetersiz kalması',
            'E': 'Gerekli bir kontrolün bulunmaması',
        },
        'D',
        'Eksiklik; bir kontrolün tasarımının, uygulanmasının ya da işleyişinin yanlışlıkları zamanında önlemeye veya tespit edip düzeltmeye elverişli olmaması ya da gerekli bir kontrolün bulunmamasıdır. Denetçinin zaman kısıtı işletmenin iç kontrolüyle ilgili değildir.',
    ),
    # düzey 3
    '0019': patch(
        "Bir şirket bordro işlemlerini dışarıdaki bir hizmet kuruluşuna yaptırmaktadır. Denetçi, hizmet kuruluşundaki kontrollerin belirli bir dönem boyunca etkin işlediğine dair kanıt elde etmek istemektedir.\n\nBDS 402'ye göre bu amaçla kullanılabilecek rapor aşağıdakilerden hangisidir?",
        {
            'A': 'Hizmet kuruluşunun belirli bir tarihteki kontrol tasarımını açıklayan rapor',
            'B': 'Vergi inceleme raporu',
            'C': 'Tip 1 rapor',
            'D': 'Faaliyet raporu',
            'E': 'Tip 2 rapor',
        },
        'E',
        'Tip 1 rapor kontrollerin tasarımını ve belirli bir tarihte uygulandığını; Tip 2 rapor ayrıca belirli bir dönem boyunca işleyiş etkinliğini kapsar. İşleyiş etkinliği kanıtı için Tip 2 rapor gerekir.',
    ),
    # düzey 2
    '0020': patch(
        'Bir depoya giriş ve çıkışların kartlı geçiş sistemiyle yetkili personelle sınırlandırılması hangi kontrol faaliyetine örnektir?',
        {
            'A': 'Kontrol çevresi',
            'B': 'Performans incelemesi',
            'C': 'Bilgi işleme kontrolü',
            'D': 'Fiziki kontrol',
            'E': 'Görevler ayrılığı ve yetkilendirme kontrolü',
        },
        'D',
        'Varlıklara erişimin sınırlandırılması ve varlıkların korunması fiziki kontrollere örnektir.',
    ),
    # düzey 3
    '0021': patch(
        'Bir denetçi, satış sürecinin bir işlemini başlangıcından kayda kadar belgeler ve personel üzerinden izleyerek kontrolleri anlamaya çalışmıştır.\n\nBu prosedür esas olarak hangi amaca hizmet eder?',
        {
            'A': 'Hesap bakiyesini teyit etmek',
            'B': 'Kontrollerin uygulandığını anlamak',
            'C': 'Önemliliği belirlemek',
            'D': 'Kontrollerin dönem boyunca etkinliğini kanıtlamak',
            'E': 'Satış hasılatının tamlığı için tek başına yeterli maddi doğrulama kanıtı sağlamak',
        },
        'B',
        'Bir işlemin sistem boyunca izlenmesi, kontrollerin tasarımını ve uygulanıp uygulanmadığını anlamaya yardımcı olur; dönem boyunca işleyiş etkinliği için ayrıca kontrol testi gerekir.',
    ),
    # düzey 2
    '0022': patch(
        'İç kontrol sistemine ilişkin sorumluluklarla ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yönetim iç kontrolün tasarlanmasından sorumludur',
            'B': 'Üst yönetimden sorumlu olanlar iç kontrolü gözetir',
            'C': 'Diğer personel de iç kontrolün işleyişinde rol alır',
            'D': 'Tasarlama sorumluluğu bağımsız denetçiye aittir',
            'E': 'Denetçi iç kontrolü risk değerlendirmesi amacıyla anlar',
        },
        'D',
        'İç kontrol sistemi üst yönetimden sorumlu olanlar, yönetim ve diğer personel tarafından tasarlanır, uygulanır ve sürdürülür. Bağımsız denetçi iç kontrolü anlar ve değerlendirir, ancak tasarlamaz.',
    ),
    # düzey 3
    '0023': patch(
        "Denetçi, yönetimin daha önce bilgilendirildiği ve bilinçli olarak gidermediği bir önemli eksikliğin cari yılda da devam ettiğini tespit etmiştir.\n\nBDS 265'e göre bu eksiklik için hangisi doğrudur?",
        {
            'A': 'Yeniden yazılı olarak bildirilir',
            'B': 'Daha önce bildirildiği için bildirilmez',
            'C': 'Sözlü bildirim yeterlidir',
            'D': 'Eksiklik giderilmediği için sözleşmeden derhâl çekilmek gerekir',
            'E': 'Rapor görüşü olumsuza çevrilir',
        },
        'A',
        'Önemli eksiklikler, önceki dönemde bildirilmiş ve giderilmemiş olsa bile her dönem üst yönetimden sorumlu olanlara yazılı olarak bildirilir; önceki bildirime atıf yapılabilir.',
    ),
    # düzey 3
    '0024': patch(
        'Denetçi, kredi limitlerinin sistemde güncellenmediğini ve bu nedenle limitini aşan müşterilere sevkiyat yapıldığını tespit etmiştir; bu durum şüpheli alacakların önemli ölçüde artmasına yol açmıştır.\n\nBu bulgu için en uygun nitelendirme aşağıdakilerden hangisidir?',
        {
            'A': 'Kilit denetim konusu olmayan önemsiz bulgu',
            'B': 'Önemli eksiklik',
            'C': 'Dikkat çekilen husus',
            'D': 'Anomali',
            'E': 'Diğer husus',
        },
        'B',
        'Önemli yanlışlığa yol açma olasılığı ve büyüklüğü yüksek olan bir kontrol eksikliği önemli eksiklik olarak değerlendirilir ve üst yönetimden sorumlu olanlara yazılı olarak bildirilir.',
    ),
    # düzey 3
    '0025': patch(
        'Personel sayısı az olan küçük bir şirkette görevler ayrılığı yeterince sağlanamamaktadır.\n\nBu eksikliği telafi etmek için en uygun kontrol aşağıdakilerden hangisidir?',
        {
            'A': 'Personelin sürekli değiştirilmesi',
            'B': 'Bağımsız denetimden vazgeçilmesi',
            'C': 'Kontrollerin tamamen kaldırılması',
            'D': 'Her işlemin müşteriye teyit ettirilmesiyle gözetimin dışarıya devredilmesi',
            'E': 'Sahibin doğrudan gözetimi',
        },
        'E',
        'Küçük işletmelerde görevler ayrılığının eksikliği, sahip ya da yöneticinin işlemlere doğrudan katılımı ve gözetimiyle kısmen telafi edilebilir.',
    ),
    # düzey 3
    '0026': patch(
        'Satın alma sorumlusu ile ambar memuru gizlice anlaşarak teslim alınmayan mallar için teslim tutanağı düzenlemiş ve ödeme yapılmasını sağlamıştır.\n\nBu durum iç kontrolün hangi kısıtına örnektir?',
        {
            'A': 'Yönetimin kontrolleri ihlal etmesi',
            'B': 'Maliyet-fayda dengesi',
            'C': 'Rutin olmayan işlemler',
            'D': 'Kontrol çevresinin güçlü olması',
            'E': 'Gizli anlaşma',
        },
        'E',
        'Görevler ayrılığı iki kişinin gizlice anlaşmasıyla aşılabilir; muvazaa iç kontrolün yapısal kısıtlarındandır.',
    ),
    # düzey 2
    '0027': patch(
        'COSO iç kontrol çerçevesine göre iç kontrolün amaç kategorilerinden biri aşağıdakilerden hangisi değildir?',
        {
            'A': 'Mevzuata uyum',
            'B': 'Kârın en üst düzeye çıkarılması',
            'C': 'Raporlamanın güvenilirliği',
            'D': 'Faaliyet, raporlama ve uyum amaçlarının birlikte gözetilmesi',
            'E': 'Faaliyetlerin etkinliği ve verimliliği',
        },
        'B',
        "COSO'ya göre iç kontrolün amaçları faaliyetler, raporlama ve uyum kategorilerinde toplanır. Kârın en üst düzeye çıkarılması iç kontrolün değil işletme stratejisinin amacıdır.",
    ),
    # düzey 2
    '0028': patch(
        "BDS 610'a göre denetçinin iç denetim fonksiyonunun çalışmalarından yararlanıp yararlanamayacağını değerlendirirken dikkate aldığı hususlardan biri aşağıdakilerden hangisi değildir?",
        {
            'A': 'Sistematik ve disiplinli yaklaşım uygulaması',
            'B': 'Fonksiyonun tarafsızlığını destekleyen örgütsel statüsü',
            'C': 'İç denetçilerin ücret düzeyi',
            'D': 'Fonksiyonun yetkinlik düzeyi',
            'E': 'Kalite kontrol uygulamaları',
        },
        'C',
        'Denetçi, iç denetim fonksiyonunun örgütsel statüsü ve politikalarının tarafsızlığı ne ölçüde desteklediğini, yetkinlik düzeyini ve kalite kontrol dahil sistematik ve disiplinli bir yaklaşım uygulayıp uygulamadığını değerlendirir.',
    ),
    # düzey 2
    '0029': patch(
        'Aşağıdakilerden hangisi bir BT genel kontrolüdür?',
        {
            'A': "Faturadaki KDV'nin sistemce hesaplanması",
            'B': 'Müşteri kodunun girişte kontrolü',
            'C': 'Mükerrer fatura numarasının girişte reddedilmesi',
            'D': 'Yetkisiz kullanıcı erişiminin engellenmesi',
            'E': 'Kredi limitini aşan siparişin sistemce durdurulması',
        },
        'D',
        'Erişim yönetimi BT genel kontrolüdür. Tutar hesaplama, kod kontrolü, limit ve mükerrerlik kontrolleri belirli bir uygulamadaki işlemlere ilişkin uygulama kontrolleridir.',
    ),
    # düzey 3
    '0030': patch(
        'Genel müdür, mevcut onay prosedürlerini atlayarak kendi talimatıyla dönem sonunda büyük tutarlı bir satış kaydı yaptırmıştır.\n\nBu durum aşağıdakilerden hangisine örnektir?',
        {
            'A': 'Gizli anlaşma',
            'B': 'Maliyet-fayda kısıtı',
            'C': 'İnsan hatası',
            'D': 'Bilgi sistemi kontrolünün olağan işleyişi',
            'E': 'Yönetimin kontrolleri ihlali',
        },
        'E',
        'Yönetimin konumunu kullanarak kontrolleri devre dışı bırakması, iç kontrolün iyi tasarlanmış olsa bile önleyemeyeceği bir kısıttır.',
    ),
    # düzey 3
    '0031': patch(
        "BDS 315'e göre denetçinin iç kontrolün tasarımını ve uygulanmasını değerlendirmesi ile kontrollerin işleyiş etkinliğini test etmesi arasındaki ilişki için aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Uygulanmış olması etkin işlediğini göstermez',
            'B': 'Tasarım değerlendirmesi kontrol testinin yerine geçer',
            'C': 'İkisi aynı prosedürle kanıtlanır',
            'D': 'İşleyiş etkinliği sorgulamayla tek başına kanıtlanır',
            'E': 'Kontrolün bir kez uygulanmış görülmesi tüm dönem için yeterli kanıttır',
        },
        'A',
        'Bir kontrolün belirli bir anda uygulandığının görülmesi, dönem boyunca etkin işlediğine kanıt değildir; işleyiş etkinliği kontrol testleriyle sınanır.',
    ),
    # düzey 2
    '0032': patch(
        "BDS 265'e göre bir iç kontrol eksikliğinin önemli eksiklik olup olmadığına karar verirken denetçinin dikkate aldığı hususlardan biri aşağıdakilerden hangisi değildir?",
        {
            'A': 'Önemli yanlışlığa yol açma olasılığı',
            'B': 'Diğer eksikliklerle etkileşimi',
            'C': 'Eksikliği gideren personelin kıdemi',
            'D': 'İlgili varlığın hileye açıklığı',
            'E': 'Gözlenen sapmaların sıklığı',
        },
        'C',
        'Denetçi; eksikliğin önemli yanlışlığa yol açma olasılığını ve büyüklüğünü, ilgili varlığın ya da borcun hileye açıklığını, sübjektifliği, sapmaların nedenini ve sıklığını ve diğer eksikliklerle etkileşimini dikkate alır.',
    ),
    # düzey 2
    '0033': patch(
        'Denetçinin iç kontrolü değerlendirmesinin sonuçlarıyla ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Prosedürlerin zamanlamasını etkileyebilir',
            'B': 'Eksikliklerin bildirilmesine yol açabilir',
            'C': 'Maddi doğrulama kapsamını etkiler',
            'D': 'Kontroller etkinse maddi doğrulama yapılmaz',
            'E': 'Kontrol riski değerlendirmesini etkiler',
        },
        'D',
        'Kontroller etkin olsa bile önemli her işlem sınıfı, hesap bakiyesi ve açıklama için maddi doğrulama prosedürleri uygulanır; değerlendirme yalnızca bu prosedürlerin kapsamını, zamanlamasını ve niteliğini etkiler.',
    ),
    # düzey 3
    '0034': patch(
        'Bir şirketin iç denetim birimi, iç kontrol sistemindeki eksiklikleri tespit ederek yönetime raporlamaktadır.\n\nBu faaliyet iç kontrol sisteminin hangi bileşeni kapsamındadır?',
        {
            'A': 'Bilgi sistemi ve iletişim',
            'B': 'İzleme süreci',
            'C': 'Risk değerlendirme süreci',
            'D': 'Kontrol çevresi',
            'E': 'Yönetişim ve iç denetim komitesi süreci',
        },
        'B',
        'İç kontrol sisteminin etkinliğinin sürekli faaliyetler ve ayrı değerlendirmelerle izlenmesi izleme sürecidir; iç denetim faaliyetleri bu bileşenin önemli bir parçasıdır.',
    ),
    # düzey 3
    '0035': patch(
        'I. Kontrol çevresi\nII. Kontrol faaliyetleri\nIII. Bağımsız denetçinin görüşü\n\nYukarıdakilerden hangileri iç kontrol sisteminin bileşenlerindendir?',
        {
            'A': 'II ve III',
            'B': 'I ve III',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'D',
        'Kontrol çevresi ve kontrol faaliyetleri iç kontrol bileşenleridir; denetçinin görüşü iç kontrolün parçası değildir.',
    ),
    # düzey 3
    '0036': patch(
        'Denetçinin iç kontrolde tespit ettiği bir eksiklik, ilgili hesapta önemli yanlışlık riskini artırmaktadır.\n\nAşağıdakilerden hangisi bu durumda denetçinin yapması beklenenlerden biri değildir?',
        {
            'A': 'Eksikliğin bildirilmesi gerekip gerekmediğini değerlendirmek',
            'B': 'Risk değerlendirmesini gözden geçirmek',
            'C': 'İleri prosedürlerin kapsamını genişletmek',
            'D': 'Etkilenen hesaplarda daha güvenilir kanıt aramak',
            'E': 'Eksikliği dikkate almadan aynı planla devam etmek',
        },
        'E',
        'Eksiklik risk değerlendirmesini etkiliyorsa denetçi değerlendirmesini gözden geçirir, ileri prosedürleri değiştirir ya da genişletir ve eksikliğin bildirilmesi gerekip gerekmediğini değerlendirir.',
    ),
    # düzey 2
    '0037': patch(
        'Denetçi bir satış iadesi kontrolünü test etmek için iade belgelerinden örnek seçip yetkili müdürün onay imzasını aramıştır.\n\nBu prosedür hangi amaca yöneliktir?',
        {
            'A': 'Satış hasılatını teyit etmek',
            'B': 'Kontrolün işleyişini test etmek',
            'C': 'Müşterilerden iade bakiyelerine ilişkin dış teyit almak',
            'D': 'Önemliliği belirlemek',
            'E': 'İade tutarlarını yeniden hesaplamak',
        },
        'B',
        'Onay imzasının varlığının örnek belgeler üzerinde aranması, iade onay kontrolünün işleyiş etkinliğini test eden bir kontrol testidir.',
    ),
    # düzey 2
    '0038': patch(
        "BDS 265'e göre önemli eksiklik aşağıdakilerden hangisidir?",
        {
            'A': 'Yönetimin kabul ettiği risk',
            'B': 'Tutarı önemliliği aşan her yanlışlık',
            'C': 'Denetim ekibinin kendi içinde çözdüğü ve bildirime gerek görmediği eksiklik',
            'D': 'Üst yönetimin dikkatini hak eden eksiklik',
            'E': 'Denetçinin düzelttiği eksiklik',
        },
        'D',
        'Önemli eksiklik, denetçinin mesleki muhakemesine göre üst yönetimden sorumlu olanların dikkatini hak edecek kadar önemli olan eksiklik ya da eksiklikler bütünüdür.',
    ),
    # düzey 3
    '0039': patch(
        "Denetçi, iç denetim biriminden bir uzmanı kendi gözetimi altında belirli prosedürleri uygulamak üzere doğrudan yardım için görevlendirmek istemektedir.\n\nBDS 610'a göre bu kişiye aşağıdakilerden hangisi verilemez?",
        {
            'A': 'Önemli muhakeme gerektiren işler',
            'B': 'Basit mutabakatlar',
            'C': 'Belgelerin derlenmesi',
            'D': 'Denetçinin yönlendirmesiyle aritmetik kontroller ve belge karşılaştırmaları',
            'E': 'Gözetim altında rutin testler',
        },
        'A',
        'Doğrudan yardım sağlayan iç denetçilere önemli muhakeme gerektiren, yüksek riskli ya da çalıştıkları alanla ilgili prosedürler verilmez; işleri denetçinin yönlendirme, gözetim ve gözden geçirmesine tabidir.',
    ),
    # düzey 2
    '0040': patch(
        'Stok kayıtlarının dönemsel olarak fiziki sayımla karşılaştırılması ve farkların araştırılması hangi amaca hizmet eder?',
        {
            'A': 'Önemliliği belirlemek',
            'B': 'Kayıtlarla varlıkların uyumunu sağlamak',
            'C': 'Denetçi sayımını gereksiz kılmak',
            'D': 'Vergi matrahını düşürmek',
            'E': 'Satış fiyatını belirlemek',
        },
        'B',
        'Kayıtlı tutarların fiili varlıklarla karşılaştırılması, varlıkların korunmasına ve kayıtların doğruluğuna yönelik bir kontroldür.',
    ),
    # düzey 2
    '0041': patch(
        'Aşağıdakilerden hangisi önleyici kontrole örnek değildir?',
        {
            'A': 'Mükerrer fatura numarasının girişte reddedilmesi',
            'B': 'Görevlerin farklı çalışanlara dağıtılması',
            'C': 'Faturaların ekstrelerle sonradan karşılaştırılması',
            'D': 'Ödemenin yetkili onayı olmadan yapılamaması',
            'E': 'Kredi limitini aşan siparişin sistemce durdurulması',
        },
        'C',
        'Önleyici kontroller hata ya da hilenin gerçekleşmesini baştan engeller. Gerçekleşmiş işlemlerin sonradan karşılaştırılması ise farkları ortaya çıkaran tespit edici bir kontroldür.',
    ),
    # düzey 2
    '0042': patch(
        "BDS 315'e göre iç kontrol sisteminin diğer bileşenlerine genel bir temel oluşturan bileşen aşağıdakilerden hangisidir?",
        {
            'A': 'Risk değerlendirme süreci',
            'B': 'İzleme süreci',
            'C': 'Bağımsız denetim ve gözetim faaliyetleri',
            'D': 'Bilgi sistemi ve iletişim',
            'E': 'Kontrol çevresi',
        },
        'E',
        'Kontrol çevresi, iç kontrol sisteminin diğer bileşenlerinin işleyişine genel bir temel oluşturur.',
    ),
    # düzey 2
    '0043': patch(
        'Görevler ayrılığı ilkesine göre birbirinden ayrılması gereken temel görevler aşağıdakilerden hangisinde doğru verilmiştir?',
        {
            'A': 'Üretim, kalite ve bakım',
            'B': 'Yetkilendirme, kayıt ve varlıkların muhafazası',
            'C': 'İşe alım, eğitim ve performans değerlendirmesi',
            'D': 'Satış, pazarlama ve reklam',
            'E': 'Planlama, bütçeleme ve raporlama',
        },
        'B',
        'İşlemlerin yetkilendirilmesi, kaydı ve ilgili varlıkların muhafazası farklı kişilerce yürütülmelidir.',
    ),
    # düzey 2
    '0044': patch(
        'İç kontrolün sağladığı güvence ile ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İyi tasarlanmış olsa da yapısal sınırları vardır',
            'B': 'Amaçlara ulaşılacağına dair makul düzeyde güvence verir',
            'C': 'Etkinliği zaman içinde değişebilir',
            'D': 'İşleyişi kişilerin dikkat ve özenine bağlıdır',
            'E': 'Hata ve hilelerin tamamını önlemeyi garanti eder',
        },
        'E',
        'İç kontrol, ne kadar iyi tasarlanmış olursa olsun yapısal kısıtları nedeniyle amaçlara ulaşılacağına dair ancak makul güvence sağlar; hata ve hilelerin tamamını önlemeyi garanti edemez.',
    ),
    # düzey 2
    '0045': patch(
        'Yoğun dönem sonunda yorgun bir muhasebe çalışanının bir faturayı iki kez kaydetmesi iç kontrolün hangi kısıtına örnektir?',
        {
            'A': 'Maliyet-fayda dengesi',
            'B': 'Gizli anlaşma',
            'C': 'İnsan hatası',
            'D': 'Kontrol çevresinin bilinçli olarak zayıflatılması',
            'E': 'Yönetimin kontrolleri ihlali',
        },
        'C',
        'Dikkatsizlik, yorgunluk ya da yanlış muhakeme nedeniyle yapılan hatalar insan hatasıdır ve iç kontrolün kısıtlarındandır.',
    ),
    # düzey 2
    '0046': patch(
        "BDS 402'ye göre hizmet kuruluşu denetçisinin Tip 1 raporuyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Kullanıcı işletmenin denetçisine kanıt sağlayabilir',
            'B': 'Bir yıllık işleyiş testlerini içerir',
            'C': 'Kontrollerin tasarımının uygunluğunu kapsar',
            'D': 'Hizmet kuruluşunun sistemine ilişkin açıklamayı içerir',
            'E': 'Kontrollerin belirli bir tarihte uygulandığını kapsar',
        },
        'B',
        'Tip 1 rapor, hizmet kuruluşunun sistemine ilişkin açıklamayı ve kontrollerin belirli bir tarihteki tasarımı ile uygulanmasının uygunluğunu kapsar; dönem boyunca işleyiş etkinliğine ilişkin test sonuçlarını içermez.',
    ),
    # düzey 3
    '0047': patch(
        "I. Yazılı olarak yapılır.\nII. Zamanında yapılır.\nIII. İç kontrolün etkinliği hakkında görüş içerir.\n\nBDS 265'e göre önemli eksikliklerin üst yönetimden sorumlu olanlara bildirilmesiyle ilgili yukarıdaki ifadelerden hangileri doğrudur?",
        {
            'A': 'II ve III',
            'B': 'I, II ve III',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'I ve III',
        },
        'D',
        'Önemli eksiklikler zamanında ve yazılı olarak bildirilir; bildirim iç kontrolün etkinliği hakkında görüş içermez.',
    ),
    # düzey 3
    '0048': patch(
        'Bir şirket, yazılımında yapılan değişikliklerin canlı sisteme alınmadan önce test edilmesini ve yetkili kişilerce onaylanmasını şart koşmaktadır.\n\nBu uygulama hangi kontrol türüne örnektir?',
        {
            'A': 'Program değişikliği kontrolü',
            'B': 'Performans incelemesi',
            'C': 'Uygulama girdi kontrolü',
            'D': 'Fiziki sayım kontrolü',
            'E': 'Sonuç raporlarının elle karşılaştırılmasına dayalı çıktı kontrolü',
        },
        'A',
        'Program değişikliklerinin test edilip onaylanması, BT genel kontrolleri içinde program değişikliği yönetimi kontrolüdür.',
    ),
    # düzey 3
    '0049': patch(
        'Bir şirkette satış işlemlerinin başlatılması, kaydedilmesi, işlenmesi ve finansal tablolara yansıtılmasına ilişkin prosedürler ile bu süreçteki görev ve sorumlulukların personele duyurulması ele alınmaktadır.\n\nBu unsurlar hangi bileşene aittir?',
        {
            'A': 'İzleme süreci',
            'B': 'Kontrol çevresi',
            'C': 'Bilgi sistemi ve iletişim',
            'D': 'Muhasebe kayıt ve belge düzeni',
            'E': 'Risk değerlendirme süreci',
        },
        'C',
        'Bilgi sistemi işlemlerin başlatılması, kaydı, işlenmesi ve raporlanmasını; iletişim ise iç kontrole ilişkin rol ve sorumlulukların duyurulmasını kapsar.',
    ),
    # düzey 3
    '0050': patch(
        'Bir şirkette yönetim, aylık satış raporlarını bütçe ve önceki dönemlerle karşılaştırarak beklenmedik sapmaları araştırmaktadır.\n\nBu uygulama aşağıdakilerden hangisine örnektir?',
        {
            'A': 'Kontrol çevresi',
            'B': 'İşletme dışı bağımsız denetim prosedürü',
            'C': 'Performans incelemesi',
            'D': 'Fiziki kontrol',
            'E': 'Görevler ayrılığı',
        },
        'C',
        'Gerçekleşen sonuçların bütçe, tahmin ve önceki dönemlerle karşılaştırılması performans incelemesi niteliğindeki kontrol faaliyetidir.',
    ),
    # düzey 2
    '0051': patch(
        "BDS 610'a göre denetçinin iç denetim fonksiyonunun çalışmalarından yararlanmasıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Yararlanma kararı denetim dosyasında belgelendirilir',
            'B': 'Yararlanılan alanlarda denetçinin sorumluluğu iç denetime geçer',
            'C': 'Denetçi kullanılan çalışmalara kendi prosedürlerini uygular',
            'D': 'İç denetimin çalışmaları denetçi tarafından değerlendirilir',
            'E': 'Denetçi görüşüne ilişkin sorumluluk denetçide kalır',
        },
        'B',
        'Denetçi görüşü ile ilgili tüm sorumluluk denetçiye aittir; iç denetimin çalışmalarından yararlanılması bu sorumluluğu azaltmaz ve iç denetime devretmez.',
    ),
    # düzey 2
    '0052': patch(
        'Aşağıdakilerden hangisi bir kontrol faaliyeti örneği değildir?',
        {
            'A': 'Etik kuralların yayımlanması',
            'B': 'Stoka erişimin sınırlandırılması',
            'C': 'Banka mutabakatının yapılması',
            'D': 'Fatura ile sevk belgesinin karşılaştırılması',
            'E': 'Satın alma siparişinin onaylanması',
        },
        'A',
        'Onay, mutabakat, fiziki erişim sınırlaması ve belgelerin karşılaştırılması kontrol faaliyetleridir. Etik kuralların yayımlanması kontrol çevresine ilişkindir.',
    ),
    # düzey 3
    '0053': patch(
        'İç kontrolün güçlü olduğu ve kontrol testleriyle doğrulandığı bir denetimde aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Maddi doğrulamaya gerek kalmaz',
            'B': 'Denetim riski sıfıra iner',
            'C': 'Sorgulama yeterli olur',
            'D': 'Maddi doğrulama kapsamı azaltılabilir',
            'E': 'Kanıt ihtiyacı artar',
        },
        'D',
        'Etkin kontroller kabul edilebilir tespit riskini yükselttiğinden maddi doğrulama kapsamı azaltılabilir; ancak önemli hesaplar için maddi doğrulama tamamen kaldırılamaz.',
    ),
    # düzey 3
    '0054': patch(
        'Bir şirket, yıllık 10.000 ₺ kayıp riskini önlemek için yıllık 80.000 ₺ maliyetli bir kontrol kurmamaya karar vermiştir.\n\nBu karar iç kontrolün hangi özelliğiyle açıklanır?',
        {
            'A': 'İnsan hatası',
            'B': 'Gizli anlaşma',
            'C': 'Maliyet-fayda dengesi',
            'D': 'Yönetimin kontrolleri ihlali',
            'E': 'Görevler ayrılığı ve yetkilendirme ilkesi',
        },
        'C',
        'Bir kontrolün maliyeti sağlayacağı faydayı aşmamalıdır; maliyet-fayda dengesi iç kontrolün yapısal kısıtlarındandır.',
    ),
    # düzey 2
    '0055': patch(
        'Bir şirkette satış iadeleri ancak yetkili müdürün yazılı onayıyla kabul edilmektedir.\n\nBu uygulama hangi tür kontrol faaliyetidir?',
        {
            'A': 'Performans incelemesi',
            'B': 'Fiziki kontrol',
            'C': 'Mutabakat',
            'D': 'Bilgi sistemlerinde program değişikliği kontrolü',
            'E': 'Yetkilendirme ve onay',
        },
        'E',
        'İşlemlerin yetkili kişilerce onaylanması yetkilendirme ve onay türündeki kontrol faaliyetidir.',
    ),
    # düzey 3
    '0056': patch(
        'Görevler ayrılığı ilkesine göre aşağıdaki görevlerden hangisinin aynı kişide birleşmesi en yüksek riski yaratır?',
        {
            'A': 'Kasaya tahsilat ve kasa kaydının tutulması',
            'B': 'Banka ekstresi temini ve dosyalanması',
            'C': 'Satış teklifi hazırlama ve müşteri ziyareti',
            'D': 'Stok sayımı ve sayım tutanağının imzalanması',
            'E': 'Bordro hesaplama ve personel eğitimi',
        },
        'A',
        'Varlığın muhafazası ile kaydının aynı kişide birleşmesi, bir hatanın ya da zimmetin kayıtlar değiştirilerek gizlenmesine olanak verir.',
    ),
    # düzey 3
    '0057': patch(
        'Denetçinin kontrol testi yapmadan kontrol riskini düşük değerlendirmesi için aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Uygundur',
            'B': 'Uygun değildir',
            'C': 'Küçük işletmelerde zorunludur',
            'D': 'Yönetim onaylarsa uygundur',
            'E': 'Önceki yıl kontrol testi yapılmışsa yeniden değerlendirmeye gerek yoktur',
        },
        'B',
        'Kontrollere dayanılacaksa, yani kontrol riski düşük değerlendirilecekse denetçi kontrollerin işleyiş etkinliğine ilişkin kanıt elde etmek için kontrol testi uygular.',
    ),
    # düzey 2
    '0058': patch(
        'İç kontrolün yapısal kısıtlarından biri aşağıdakilerden hangisi değildir?',
        {
            'A': 'Gizli anlaşma',
            'B': 'İnsan hatası',
            'C': 'Yönetimin kontrolleri ihlali',
            'D': 'Maliyet-fayda dengesi',
            'E': 'Görevler ayrılığının uygulanması',
        },
        'E',
        'İnsan hatası, gizli anlaşma (muvazaa), yönetimin kontrolleri ihlali ve maliyet-fayda dengesi iç kontrolün kısıtlarıdır. Görevler ayrılığı bir kısıt değil, kontrol ilkesidir.',
    ),
    # düzey 2
    '0059': patch(
        'Ay sonunda yapılan banka mutabakatında kayıtlardaki bir hatanın ortaya çıkarılması hangi tür kontrole örnektir?',
        {
            'A': 'Tespit edici kontrol',
            'B': 'Hatanın oluşmadan önce engellenmesini sağlayan erişim kontrolü',
            'C': 'Yönlendirici kontrol',
            'D': 'Kontrol çevresi',
            'E': 'Önleyici kontrol',
        },
        'A',
        'Gerçekleşmiş bir hatayı sonradan ortaya çıkaran kontrol tespit edici (ortaya çıkarıcı) kontroldür.',
    ),
    # düzey 3
    '0060': patch(
        "I. İç denetimin örgütsel statüsü\nII. İç denetimin yetkinliği\nIII. İç denetçilerin yaş ortalaması\n\nBDS 610'a göre iç denetimden yararlanma kararında yukarıdakilerden hangileri dikkate alınır?",
        {
            'A': 'I ve III',
            'B': 'II ve III',
            'C': 'I, II ve III',
            'D': 'Yalnız I',
            'E': 'I ve II',
        },
        'E',
        'Örgütsel statü ve politikaların tarafsızlığı desteklemesi ile yetkinlik dikkate alınır; yaş ortalaması bir ölçüt değildir.',
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
    print(f"1 paket / {len(PATCHES)} soru ('İç Kontrol' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
