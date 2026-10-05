#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Denetim Kanıtı ve Teknikleri — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Denetim turu (gerçek denetim bloğu 73-88 ile ölçüldü). Paket baştan yazıldı: BDS 500, kanıt toplama prosedürleri, yönetim beyanları, BDS 505, BDS 520, BDS 501, BDS 580 ve BDS 330. 2026-10-05: gerçek sınavda denetim köklerinin %46'sı olumsuz; 7 soru dört doğru ifadeli olumsuz köke çevrildi, aynı paketteki başka soruların cevaplarını sızdıran çeldiriciler ayıklandı.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: BDS 500, 501, 505, 520, 580, 330
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/denetim/denetim_kaniti.json"
STYLE_REF = 'SGS Denetim (standarda atıflı/olay kök + kısa şık; gerçek sınav profili)'
ONEK = "den-kanit-gen-"


def patch(stem, options, answer, solution, ref='BDS 500 Bağımsız Denetim Kanıtları; BDS 505; BDS 520; BDS 501; BDS 580; BDS 330'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        "Elma A.Ş.'nin geçen yıl personel gideri 18.000.000 ₺'dir. Bu yıl ücretlere ortalama %30 artış yapılmış, çalışan sayısı ise yıl boyunca %10 daha az olmuştur. Denetçi personel giderini analitik prosedürle test etmektedir.\n\nDenetçinin bu yıl için beklediği personel gideri kaç ₺'dir?",
        {
            'A': '16.200.000 ₺',
            'B': '25.200.000 ₺',
            'C': '21.060.000 ₺',
            'D': '21.600.000 ₺',
            'E': '23.400.000 ₺',
        },
        'C',
        "Beklenti 18.000.000 ₺ × 1,30 × 0,90 = 21.060.000 ₺'dir. Ücret artışı ile çalışan sayısındaki azalış çarpımsal olarak etki eder.",
    ),
    # düzey 2
    '0002': patch(
        'Denetçi bankalardaki mevduatın yıl içinde aydan aya olağan dışı dalgalanma gösterip göstermediğini belirlemek istemektedir.\n\nBu amaca en uygun teknik aşağıdakilerden hangisidir?',
        {
            'A': 'Analitik prosedür',
            'B': 'Tetkik',
            'C': 'Sorgulama',
            'D': 'Yeniden hesaplama',
            'E': 'Dış teyit',
        },
        'A',
        'Dönemler arası dalgalanmaların ve beklenmedik ilişkilerin belirlenmesi analitik prosedürlerle yapılır.',
    ),
    # düzey 2
    '0003': patch(
        "BDS 330'a göre kontrol testleriyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Kontrollerin işleyiş etkinliğini değerlendirir',
            'B': 'Kontrollere dayanılması planlanıyorsa uygulanır',
            'C': 'Yeniden uygulama ve tetkik gibi tekniklerle yürütülür',
            'D': 'Dönem boyunca işleyişe ilişkin kanıt sağlamayı amaçlar',
            'E': 'Hesaptaki parasal yanlışlığı doğrudan ölçer',
        },
        'E',
        'Kontrol testleri, kontrollerin işleyiş etkinliğini değerlendirir ve kontrollere dayanılacaksa uygulanır. Hesap bakiyesindeki parasal yanlışlığı doğrudan ölçmek maddi doğrulama prosedürlerinin işidir.',
    ),
    # düzey 3
    '0004': patch(
        "Denetçi bir teyit yanıtının teyit verenin adresinden değil, denetlenen işletmenin e-posta adresi üzerinden geldiğini fark etmiştir.\n\nBDS 505'e göre denetçi ne yapar?",
        {
            'A': 'Yanıtı negatif teyit sayar',
            'B': 'Yanıtın güvenilirliğini sorgulayıp ek kanıt arar',
            'C': 'Teyit verenin kimliğini işletmeye sorar',
            'D': 'Yanıtı doğrudan kabul eder',
            'E': 'Yanıtı imha eder',
        },
        'B',
        'Teyit yanıtının güvenilirliği hakkında şüpheye yol açan bir durum varsa denetçi bu şüpheyi gidermek için ek kanıt elde eder; örneğin teyit verenle doğrudan iletişim kurar.',
    ),
    # düzey 3
    '0005': patch(
        'Aşağıdakilerden hangisi menkul kıymetlerin denetiminde bir maddi doğrulama prosedürü değildir?',
        {
            'A': 'Faiz gelirini yeniden hesaplamak',
            'B': 'Alım emirlerinin yetkili kişilerce onaylandığını incelemek',
            'C': 'Saklama kuruluşu ekstresini mizanla karşılaştırmak',
            'D': 'Menkul kıymetleri borsa fiyatıyla değerlemek',
            'E': 'Aracı kurumdan bakiye teyidi almak',
        },
        'B',
        'Teyit, değerleme, karşılaştırma ve yeniden hesaplama hesap bakiyesine ilişkin doğrudan kanıt sağlayan maddi doğrulama prosedürleridir. Alım emirlerinin onaylanması bir iç kontroldür; bu kontrolün uygulandığının incelenmesi kontrol testidir.',
    ),
    # düzey 3
    '0006': patch(
        "Yönetim, önemli bir müşteriye alacak teyit mektubu gönderilmesine izin vermemiştir.\n\nBDS 505'e göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Denetçi mektubu yönetimden habersiz gönderir',
            'B': 'Denetçi reddin nedenlerini sorgular',
            'C': 'Reddin makullüğüne ilişkin kanıt aranır',
            'D': 'Reddin hile riskine etkisi değerlendirilir',
            'E': 'Ret makul değilse üst yönetime bildirilir',
        },
        'A',
        'BDS 505: yönetim teyit gönderilmesine izin vermezse denetçi reddin nedenlerini sorgular, geçerliliği ve makullüğüne ilişkin kanıt arar ve hile riski dâhil önemli yanlışlık risklerine etkisini değerlendirir. Ret makul değilse üst yönetimden sorumlu olanlara bildirir. Yönetimden habersiz gönderim söz konusu değildir.',
    ),
    # düzey 2
    '0007': patch(
        "Denetçi, işletmenin muhasebe müdürü ve satış sorumlusuyla görüşerek alacakların tahsil süreci hakkında bilgi almıştır.\n\nBDS 500'e göre bu prosedür aşağıdakilerden hangisidir?",
        {
            'A': 'Yeniden hesaplama',
            'B': 'Gözlem',
            'C': 'Sorgulama',
            'D': 'Tetkik',
            'E': 'Dış teyit',
        },
        'C',
        'Sorgulama, işletme içinden veya dışından bilgili kişilerden finansal ya da finansal olmayan bilgi alınmasıdır.',
    ),
    # düzey 2
    '0008': patch(
        "BDS 505'e göre dış teyitlerle elde edilen kanıtla ilgili aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Üçüncü taraftan doğrudan alındığı için güvenilirdir',
            'B': 'Yanıttaki istisnaların araştırılması gerekir',
            'C': 'Alacakların varlığı için güçlü kanıttır',
            'D': 'Teyit sürecinin denetçi kontrolünde olması gerekir',
            'E': 'Tüm yönetim beyanları için eşit güvence sağlar',
        },
        'E',
        'Dış teyit bazı beyanlar için daha ilgili kanıt sağlar; örneğin alacak teyidi varlık beyanı için güçlü, tahsil edilebilirlik yani değerleme için zayıf kanıttır.',
    ),
    # düzey 3
    '0009': patch(
        'Denetçi, şirketin stoklarında yer alan malların bir kısmının konsinye olarak başka bir şirkete ait olduğunu belirlemiştir.\n\nBu bulgu esas olarak hangi yönetim beyanıyla ilgilidir?',
        {
            'A': 'Sınıflandırma',
            'B': 'Haklar ve yükümlülükler',
            'C': 'Dönem ayırımı',
            'D': 'Doğruluk, değerleme ve tahsis',
            'E': 'Meydana gelme',
        },
        'B',
        'İşletmenin stoklar üzerindeki mülkiyet hakkına sahip olup olmadığı haklar ve yükümlülükler beyanıyla ilgilidir; konsinye mallar alıcının stoğunda yer almamalıdır.',
    ),
    # düzey 2
    '0010': patch(
        "BDS 500'e göre sorgulama yoluyla elde edilen kanıtla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Yanıtlar denetçiye yeni bilgiler kazandırabilir',
            'B': 'Diğer prosedürlerle desteklenmesi gerekir',
            'C': 'Denetim boyunca yaygın biçimde kullanılır',
            'D': 'Yazılı ya da sözlü olarak yapılabilir',
            'E': 'Kontrollerin işleyiş etkinliği için tek başına yeterlidir',
        },
        'E',
        'Sorgulama denetim boyunca yaygın biçimde kullanılır; ancak tek başına yönetim beyanı düzeyinde önemli yanlışlık bulunmadığına ya da kontrollerin işleyiş etkinliğine ilişkin yeterli kanıt sağlamaz.',
    ),
    # düzey 3
    '0011': patch(
        "Denetçi, yönetimin dürüstlüğü hakkında ciddi şüphe duymasına yol açan bulgular elde etmiştir.\n\nBDS 580'e göre bu durumun yazılı beyanlara etkisi aşağıdakilerden hangisidir?",
        {
            'A': 'Beyanlar yeterli kanıt sayılır',
            'B': 'Beyanlar daha güvenilir sayılır',
            'C': 'Beyan alınmasına gerek kalmaz',
            'D': 'Beyanlar sözlü olarak alınır',
            'E': 'Beyanların güvenilirliği yeniden değerlendirilir',
        },
        'E',
        'Yönetimin dürüstlüğü ya da etik değerlere bağlılığı hakkında şüphe varsa denetçi bunun yazılı ya da sözlü beyanların ve genel olarak kanıtın güvenilirliğine etkisini belirler.',
    ),
    # düzey 3
    '0012': patch(
        "Denetçi, öngörülemeyen bir olay nedeniyle stok sayımına katılamamıştır.\n\nBDS 501'e göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Denetçi alternatif bir tarihte sayım yapabilir',
            'B': 'Denetçi alternatif bir tarihte sayımı gözlemleyebilir',
            'C': 'Önceki yılın sayımı kanıt olarak kullanılmaz',
            'D': 'Stoklar sıfır kabul edilerek denetime devam edilir',
            'E': 'Yönetimin yazılı beyanı tek başına yetmez',
        },
        'D',
        'BDS 501: öngörülemeyen durumlar nedeniyle sayıma katılamayan denetçi alternatif bir tarihte fiziki sayım yapar veya gözlemler ve aradaki işlemler için prosedürler uygular. Önceki yıl sayımı ya da yazılı beyan bunun yerine geçmez; stokların sıfır kabul edilmesi söz konusu değildir.',
    ),
    # düzey 3
    '0013': patch(
        "Bir kaynaktan elde edilen kanıt, başka bir kaynaktan elde edilen kanıtla tutarsızdır.\n\nBDS 500'e göre aşağıdakilerden hangisi denetçinin bu durumda yapması beklenenlerden biri değildir?",
        {
            'A': 'Güvenilir görüneni seçip diğerini dikkate almamak',
            'B': 'Tutarsızlığın nedenini araştırmak',
            'C': 'Gerekirse risk değerlendirmesini gözden geçirmek',
            'D': 'Ek denetim prosedürleri uygulamak',
            'E': 'Diğer kanıtların güvenilirliğine etkisini değerlendirmek',
        },
        'A',
        'Kanıtlar tutarsızsa denetçi konuyu çözmek için prosedürlerde gereken değişiklik ya da ilaveleri belirler ve durumun denetimin diğer yönlerine etkisini değerlendirir; kanıtlardan birini gerekçesiz yok sayamaz.',
    ),
    # düzey 2
    '0014': patch(
        'BDS 580 Yazılı Beyanlar standardına göre yazılı beyanlarla ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Gerekli bir denetim kanıtıdır',
            'B': 'Denetlenen dönemlerin tamamını kapsar',
            'C': 'Rapor tarihinden sonraki tarihi taşıyamaz',
            'D': 'Tek başına yeterli ve uygun kanıt sağlar',
            'E': 'Denetçiye hitaben düzenlenir',
        },
        'D',
        'Yazılı beyanlar gerekli denetim kanıtıdır, ancak ele aldıkları konular hakkında tek başına yeterli ve uygun kanıt sağlamaz.',
    ),
    # düzey 2
    '0015': patch(
        "BDS 520'ye göre denetimin sonuna yakın uygulanan analitik prosedürlerle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Genel bir tutarlılık sonucuna varmaya yardımcı olur',
            'B': 'Amaç önemlilik düzeyini ilk kez belirlemektir',
            'C': 'Tablolar denetçinin işletme anlayışıyla karşılaştırılır',
            'D': 'Denetimin tamamlanma aşamasında uygulanır',
            'E': 'Önceden tanınmamış bir riskin belirlenmesine yol açabilir',
        },
        'B',
        'BDS 520: denetimin sonuna yakın uygulanan analitik prosedürler, tabloların denetçinin işletmeye ilişkin anlayışıyla tutarlı olup olmadığı hakkında genel bir sonuca varmasına yardımcı olur ve önceden tanınmamış bir önemli yanlışlık riskini ortaya çıkarabilir. Önemlilik planlama aşamasında belirlenir.',
    ),
    # düzey 3
    '0016': patch(
        'Denetçi planlama aşamasında iç kontrollerin etkin olduğunu düşünmüş ve kontrol riskini düşük değerlendirmiş, kontrol testleri de bu değerlendirmeyi desteklemiştir.\n\nBu durumun maddi doğrulama prosedürlerine etkisi aşağıdakilerden hangisidir?',
        {
            'A': 'Maddi doğrulamaya gerek kalmaz',
            'B': 'Maddi doğrulama kapsamı artırılır',
            'C': 'Kapsam azaltılabilir',
            'D': 'Dış teyit zorunlu olur',
            'E': 'Analitik prosedür kullanılamaz',
        },
        'C',
        'Kontrol riski düşükse kabul edilebilir tespit riski yükselir ve maddi doğrulama prosedürlerinin kapsamı azaltılabilir; ancak önemli her hesap için maddi doğrulama prosedürü yine uygulanır.',
    ),
    # düzey 2
    '0017': patch(
        'BDS 500 Bağımsız Denetim Kanıtları standardına göre denetim kanıtının uygunluğuyla ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Uygunluk kanıtın elde edilme maliyetiyle ölçülür',
            'B': 'Uygunluk kanıtın kalitesinin ölçüsüdür',
            'C': 'Uygunluk kanıtın ilgililiğini kapsar',
            'D': 'Uygunluk kanıtın güvenilirliğini kapsar',
            'E': 'Kanıtın miktarı yeterlilikle ilgilidir',
        },
        'A',
        'BDS 500: uygunluk kanıtın kalitesinin ölçüsüdür; görüşe dayanak oluşturan sonuçları desteklemedeki ilgililiğini ve güvenilirliğini ifade eder. Kanıtın miktarı yeterliliktir. Maliyet, kanıt aramamanın geçerli bir gerekçesi değildir ve uygunluğun ölçüsü olamaz.',
    ),
    # düzey 2
    '0018': patch(
        "BDS 500'e göre denetim kanıtının güvenilirliğine ilişkin aşağıdaki genellemelerden hangisi yanlıştır?",
        {
            'A': 'Doğrudan elde edilen kanıt dolaylı olandan daha güvenilirdir',
            'B': 'Kontroller etkinse iç kanıt daha güvenilirdir',
            'C': 'Belgeye dayalı kanıt sözlü olandan daha güvenilirdir',
            'D': 'Fotokopi belgeler asıl belgelerden daha güvenilirdir',
            'E': 'Bağımsız dış kaynaktan alınan kanıt daha güvenilirdir',
        },
        'D',
        "Asıl belgelerle sağlanan kanıt; fotokopi, faks ya da dijital ortama aktarılmış belgelerle sağlanandan daha güvenilirdir. Diğer genellemeler BDS 500'de yer alır.",
    ),
    # düzey 2
    '0019': patch(
        "BDS 580'e göre denetçinin yönetimden alması gereken yazılı beyanlardan biri aşağıdakilerden hangisi değildir?",
        {
            'A': 'Denetim ücretinin uygun olduğuna dair beyan',
            'B': 'Erişim izni verildiğine dair beyan',
            'C': 'Tüm işlemlerin kayıtlara yansıtıldığı',
            'D': 'Tabloların hazırlanma sorumluluğunun yerine getirildiği',
            'E': 'Tüm ilgili bilgilerin denetçiye sağlandığı',
        },
        'A',
        'Yönetimden; tabloların hazırlanmasına ilişkin sorumluluğun yerine getirildiği, ilgili tüm bilgilerin ve erişim izninin sağlandığı ve tüm işlemlerin kaydedildiği konusunda yazılı beyan alınır.',
    ),
    # düzey 3
    '0020': patch(
        "Denetçi raporu 20 Mart 2026 tarihlidir.\n\nBDS 580'e göre yazılı beyanların tarihi için aşağıdakilerden hangisi uygundur?",
        {
            'A': '25 Mart 2026',
            'B': '31 Aralık 2025',
            'C': '20 Mart 2026',
            'D': '15 Ocak 2026',
            'E': '30 Nisan 2026',
        },
        'C',
        'Yazılı beyanların tarihi denetçi raporu tarihine mümkün olduğunca yakın olur ve bu tarihten sonra olamaz.',
    ),
    # düzey 3
    '0021': patch(
        "Denetçi, önemli risk olarak belirlediği hasılatın tahakkuku için yalnızca maddi doğrulama amaçlı analitik prosedür uygulamayı planlamaktadır.\n\nBDS 330'a göre bu plan için aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Kontrol testi gereksizdir',
            'B': 'Analitik prosedür kullanılamaz',
            'C': 'Ayrıntı testleri de uygulanmalıdır',
            'D': 'Plan yeterlidir; ayrıca ayrıntı testine gerek yoktur',
            'E': 'Dış teyit yasaklanır',
        },
        'C',
        'Önemli risk için maddi doğrulama yaklaşımı yalnızca maddi doğrulama prosedürlerinden oluşuyorsa bu prosedürler ayrıntı testlerini içerir.',
    ),
    # düzey 3
    '0022': patch(
        'Denetçi bir kontrolün uygulanışını mart ayında bizzat izlemiştir.\n\nGözlem yoluyla elde edilen bu kanıtla ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sürecin yürütülüşüne ilişkin kanıt sağlar',
            'B': 'Yapıldığı ana özgüdür',
            'C': 'Gözlemlenme durumu yürütülüşü etkileyebilir',
            'D': 'Denetçinin bizzat izlemesine dayanır',
            'E': 'Dönem boyunca işleyişi tek başına kanıtlar',
        },
        'E',
        'Gözlem, denetçinin bizzat izlediği bir sürecin ya da prosedürün yürütülüşüne ilişkin kanıt sağlar; ancak gözlem yapıldığı ana özgüdür ve gözlemlenme durumu prosedürün yürütülüşünü etkileyebilir. Bu nedenle dönem boyunca işleyiş etkinliğini tek başına kanıtlamaz.',
    ),
    # düzey 2
    '0023': patch(
        "BDS 330'a göre maddi doğrulama prosedürleriyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Ayrıntı testleri ve maddi doğrulama amaçlı analitik prosedürlerden oluşur',
            'B': 'Riski düşük önemli hesaplarda uygulanmaz',
            'C': 'Niteliği ve kapsamı değerlendirilen riske göre belirlenir',
            'D': 'Dönem sonu finansal raporlama sürecine ilişkin prosedürleri içerir',
            'E': 'Ara dönemde uygulanmışsa kalan dönem için ek prosedür gerekir',
        },
        'B',
        'Değerlendirilen riskten bağımsız olarak önemli her işlem sınıfı, hesap bakiyesi ve açıklama için maddi doğrulama prosedürleri tasarlanır ve uygulanır.',
    ),
    # düzey 3
    '0024': patch(
        'Denetçi, satış hesabında kayıtlı işlemlerden seçtiklerini sevk irsaliyesi ve müşteri siparişiyle desteklemeye çalışmıştır.\n\nBu prosedür esas olarak hangi beyanı test eder?',
        {
            'A': 'Tamlık',
            'B': 'Meydana gelme',
            'C': 'Sınıflandırma',
            'D': 'Haklar ve yükümlülükler',
            'E': 'Değerleme',
        },
        'B',
        'Kayıttan kaynak belgeye doğru gidilmesi, kaydedilen işlemlerin gerçekten meydana gelip gelmediğini test eder.',
    ),
    # düzey 3
    '0025': patch(
        "Bir şirket fiziki stok sayımını 30 Kasım 2025'te yapmıştır; finansal tablo tarihi 31 Aralık 2025'tir.\n\nBDS 501'e göre denetçi ayrıca aşağıdakilerden hangisini yapar?",
        {
            'A': 'Aradaki hareketleri test eder',
            'B': 'Kasım tutarını aynen kabul eder',
            'C': 'Sayımı yok sayar',
            'D': "Sayımın 31 Aralık'ta tekrarlanmasını şart koşar",
            'E': 'Görüş vermekten kaçınır',
        },
        'A',
        'Sayım finansal tablo tarihinden farklı bir tarihte yapılmışsa denetçi, sayım tarihi ile tablo tarihi arasındaki stok değişikliklerinin doğru kaydedildiğine dair kanıt elde etmek için prosedürler uygular.',
    ),
    # düzey 3
    '0026': patch(
        "Denetçi, işletmenin kayıtlı olduğu makine listesinden seçtiği makineleri fabrikada bizzat görerek varlığını kontrol etmiştir.\n\nBDS 500'e göre bu prosedür aşağıdakilerden hangisidir?",
        {
            'A': 'Yeniden uygulama',
            'B': 'Gözlem',
            'C': 'Dış teyit',
            'D': 'Tetkik',
            'E': 'Yeniden hesaplama',
        },
        'D',
        'Tetkik; kayıt ve belgelerin incelenmesini ya da maddi varlıkların fiziki olarak incelenmesini kapsar. Maddi varlığın fiziki incelemesi varlığa ilişkin güvenilir kanıt sağlar, ancak haklar veya değerleme için yeterli olmayabilir.',
    ),
    # düzey 2
    '0027': patch(
        "BDS 500'e göre denetim kanıtıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Hem destekleyici hem çelişen bilgileri kapsar',
            'B': 'Muhasebe kayıtları dışındaki bilgileri kapsamaz',
            'C': 'Önceki denetimlerden elde edilen bilgileri de içerebilir',
            'D': 'Yönetimin uzmanının çalışmasından da elde edilebilir',
            'E': 'Görüşe dayanak sonuçlara ulaşırken kullanılan bilgilerdir',
        },
        'B',
        'Denetim kanıtı, muhasebe kayıtlarındaki bilgilerle birlikte diğer kaynaklardan elde edilen bilgileri de kapsar; destekleyici ve çelişen bilgileri içerir.',
    ),
    # düzey 3
    '0028': patch(
        "Yönetim, finansal tabloların hazırlanmasına ilişkin sorumluluğunu yerine getirdiğine dair yazılı beyan vermeyi reddetmiştir.\n\nBDS 580'e göre denetçi hangi görüşü verir?",
        {
            'A': 'Olumsuz görüş',
            'B': 'Olumlu görüş',
            'C': 'Sınırlı olumlu görüş',
            'D': 'Dikkat çekilen husus içeren olumlu görüş',
            'E': 'Görüş vermekten kaçınma',
        },
        'E',
        'Yönetim, tabloların hazırlanmasına ve bilgilerin sağlanmasına ilişkin sorumluluklarına dair yazılı beyan vermezse denetçi görüş vermekten kaçınır.',
    ),
    # düzey 3
    '0029': patch(
        "Bir müşteriden gelen teyit yanıtında, müşterinin kayıtlarındaki bakiyenin şirket kayıtlarından 45.000 ₺ düşük olduğu belirtilmiştir.\n\nBDS 505'e göre denetçi ne yapar?",
        {
            'A': 'Farkı ihmal eder',
            'B': 'Teyidi geçersiz sayar',
            'C': 'Farkın yanlışlık olup olmadığını araştırır',
            'D': 'Yanıtı müşteriye geri gönderir',
            'E': 'Farkı kendisi düzeltir',
        },
        'C',
        'Denetçi istisnaları araştırarak yanlışlığın göstergesi olup olmadığını belirler; fark zamanlama farkından kaynaklanabileceği gibi yanlışlık da olabilir.',
    ),
    # düzey 3
    '0030': patch(
        'I. Meydana gelme\nII. Varlık\nIII. Dönem ayırımı\n\nYukarıdakilerden hangileri işlem sınıflarına ilişkin yönetim beyanlarındandır?',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'I ve III',
            'E': 'I, II ve III',
        },
        'D',
        'Meydana gelme ve dönem ayırımı işlem sınıflarına ve olaylara ilişkin beyanlardır; varlık ise dönem sonu hesap bakiyelerine ilişkin bir beyandır.',
    ),
    # düzey 3
    '0031': patch(
        "Defne A.Ş. 40 daireyi kiraya vermektedir. Yıl boyunca tamamı doludur ve aylık kira daire başına 15.000 ₺'dir. Kayıtlardaki kira geliri 6.600.000 ₺'dir. Denetçi kabul edilebilir fark tutarını 250.000 ₺ olarak belirlemiştir.\n\nBDS 520'ye göre denetçinin yapması gereken aşağıdakilerden hangisidir?",
        {
            'A': 'Kayıtlı tutar yükseltilir',
            'B': 'Fark kabul edilebilir, ek iş yapılmaz',
            'C': 'Analitik prosedür terk edilir',
            'D': 'Fark tolere edilebilir yanlışlığa eklenir',
            'E': 'Farkı yönetimle sorgulayıp ek prosedür uygular',
        },
        'E',
        "Beklenti 40 × 12 × 15.000 ₺ = 7.200.000 ₺'dir. Kayıtlı tutarla fark 600.000 ₺ olup kabul edilebilir fark tutarını (250.000 ₺) aşmaktadır. Denetçi farkı yönetimle sorgular, yanıtlar için kanıt arar ve gerekirse diğer prosedürleri uygular.",
    ),
    # düzey 3
    '0032': patch(
        "Denetçinin gönderdiği bir pozitif alacak teyit mektubuna yanıt gelmemiştir.\n\nBDS 505'e göre denetçi bu bakiye için aşağıdakilerden hangisini yapar?",
        {
            'A': 'Bakiyeyi doğru kabul eder',
            'B': 'Teyidi işletme aracılığıyla yeniden ister',
            'C': 'Alternatif denetim prosedürü uygular',
            'D': 'Bakiyeyi yanlışlık sayar',
            'E': 'Müşteriden sözlü onay alır',
        },
        'C',
        'Yanıt alınamayan her durumda denetçi alternatif prosedürler uygular; alacaklar için örneğin sonradan yapılan tahsilatları, sevk belgelerini ve dönem sonuna yakın satışları inceleyebilir.',
    ),
    # düzey 3
    '0033': patch(
        "I. Denetim kanıtının miktarını artırmak\nII. Daha ilgili kanıt elde etmek\nIII. Daha güvenilir kanıt elde etmek\n\nBDS 330'a göre önemli yanlışlık riskini yüksek değerlendiren denetçi yukarıdakilerden hangilerini yapar?",
        {
            'A': 'II ve III',
            'B': 'I, II ve III',
            'C': 'I ve III',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'B',
        'Değerlendirilen risk arttıkça denetçi daha ikna edici kanıt elde eder; bunun için kanıtın miktarını artırabilir, daha ilgili ya da daha güvenilir kanıt elde edebilir.',
    ),
    # düzey 3
    '0034': patch(
        'Denetçi, stokların maliyetini net gerçekleşebilir değerleriyle karşılaştırmış ve bazı kalemlerde değer düşüklüğü ayrılmadığını tespit etmiştir.\n\nBu bulgu hangi yönetim beyanına ilişkindir?',
        {
            'A': 'Değerleme',
            'B': 'Dönem ayırımı',
            'C': 'Tamlık',
            'D': 'Varlık',
            'E': 'Meydana gelme',
        },
        'A',
        'Varlıkların uygun tutarlarla finansal tablolara alınması ve değerleme düzeltmelerinin uygun kaydedilmesi değerleme ve tahsis beyanıyla ilgilidir.',
    ),
    # düzey 3
    '0035': patch(
        'Denetçi, makine kaydından yola çıkarak makineyi fabrikada bulmuş; ayrıca fabrikada gördüğü bir makineden yola çıkarak kaydını aramıştır.\n\nBu iki yön sırasıyla hangi yönetim beyanlarını test eder?',
        {
            'A': 'Varlık – Değerleme',
            'B': 'Değerleme – Varlık',
            'C': 'Tamlık – Varlık',
            'D': 'Haklar – Sınıflandırma',
            'E': 'Varlık – Tamlık',
        },
        'E',
        'Kayıttan varlığa gidiş kayıtlı varlığın gerçekte bulunduğunu, yani varlık beyanını; varlıktan kayda gidiş ise var olan varlığın kaydedildiğini, yani tamlık beyanını test eder.',
    ),
    # düzey 3
    '0036': patch(
        'BDS 505 Dış Teyitler standardına göre teyit talepleriyle ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Teyit verenin yanıtı denetçiye doğrudan gönderilir',
            'B': 'Pozitif teyitte, bilgi doğru olsa da yanıt istenir',
            'C': 'Negatif teyitte yanıtsızlık bakiyenin doğruluğunu kanıtlar',
            'D': 'Teyit sürecinin denetçinin kontrolünde olması gerekir',
            'E': 'Talepler kâğıt ya da elektronik ortamda gönderilebilir',
        },
        'C',
        'Negatif teyitte yanıt gelmemesi, teyit verenin talebi aldığını ve bilgiyi doğruladığını açıkça göstermez; bu nedenle negatif teyit, pozitif teyide göre daha az ikna edici kanıt sağlar.',
    ),
    # düzey 3
    '0037': patch(
        'Denetçi, sevk irsaliyelerinden seçtiği örnekleri satış faturalarına ve oradan yevmiye kaydına kadar izlemiştir.\n\nBu prosedürle esas olarak hangi yönetim beyanı test edilir?',
        {
            'A': 'Meydana gelme',
            'B': 'Tamlık',
            'C': 'Sınıflandırma',
            'D': 'Haklar ve yükümlülükler',
            'E': 'Değerleme',
        },
        'B',
        'Kaynak belgeden muhasebe kaydına doğru izleme, gerçekleşen işlemlerin kayıtlara alınıp alınmadığını, yani tamlık beyanını test eder.',
    ),
    # düzey 2
    '0038': patch(
        "BDS 500'e göre aşağıdakilerden hangisi kanıtın güvenilirliğini artıran unsurlardan biri değildir?",
        {
            'A': 'Kanıtın denetçi tarafından doğrudan elde edilmesi',
            'B': 'Kanıtın bağımsız dış kaynaktan alınması',
            'C': 'Kanıtın yazılı olması',
            'D': 'Kanıtın yönetim tarafından seçilip sunulması',
            'E': 'Kanıtın asıl belge olması',
        },
        'D',
        'Bağımsız dış kaynak, asıl belge, denetçinin doğrudan elde etmesi ve yazılı olma güvenilirliği artırır. Kanıtın yönetim tarafından seçilip sunulması güvenilirliği artırmaz; aksine taraflılık riskini yükseltir.',
    ),
    # düzey 3
    '0039': patch(
        "Denetçi, kıdem tazminatı karşılığını test etmek için aşağıdaki kaynaklardan kanıt elde edebilmektedir.\n\nBDS 500'deki genellemelere göre bunlardan hangisi en güvenilir kanıttır?",
        {
            'A': 'Muhasebeden alınan özet tablonun fotokopisi',
            'B': 'Personelin kendi hesapladığı tutar',
            'C': 'Denetçinin mevzuata göre yaptığı hesaplama',
            'D': 'Geçen yılın karşılık tutarı',
            'E': 'İnsan kaynakları müdürünün sözlü açıklaması',
        },
        'C',
        'Denetçinin doğrudan kendisinin elde ettiği kanıt, dolaylı ya da sözlü kanıttan daha güvenilirdir; karşılığın yeniden hesaplanması bu nitelikte bir kanıttır.',
    ),
    # düzey 2
    '0040': patch(
        'Denetçi, cari yıl brüt kâr marjını önceki yıllar ve sektör ortalamasıyla karşılaştırmış, beklenmedik sapmaların nedenini araştırmıştır.\n\nBu prosedür aşağıdakilerden hangisidir?',
        {
            'A': 'Gözlem',
            'B': 'Analitik prosedür',
            'C': 'Yeniden hesaplama',
            'D': 'Dış teyit',
            'E': 'Tetkik',
        },
        'B',
        'Analitik prosedürler, finansal veriler arasındaki ya da finansal ve finansal olmayan veriler arasındaki makul ilişkilerin analiziyle finansal bilginin değerlendirilmesi ve beklentiden önemli ölçüde farklı dalgalanmaların araştırılmasıdır.',
    ),
    # düzey 3
    '0041': patch(
        'Bir şirket, uzun vadeli banka kredisinin gelecek yıl ödenecek taksitlerini kısa vadeli borçlara aktarmamıştır.\n\nBu yanlışlık hangi yönetim beyanını ilgilendirir?',
        {
            'A': 'Dönem ayırımı',
            'B': 'Haklar ve yükümlülükler',
            'C': 'Varlık',
            'D': 'Sınıflandırma',
            'E': 'Meydana gelme',
        },
        'D',
        'Tutarın doğru hesapta ve doğru vade grubunda gösterilmesi sınıflandırma beyanıyla ilgilidir.',
    ),
    # düzey 2
    '0042': patch(
        "Denetçi, işletmenin hesapladığı amortisman giderinin aritmetik doğruluğunu kendisi hesaplayarak kontrol etmiştir.\n\nBDS 500'e göre bu prosedür aşağıdakilerden hangisidir?",
        {
            'A': 'Tetkik',
            'B': 'Dış teyit',
            'C': 'Yeniden uygulama',
            'D': 'Analitik prosedür',
            'E': 'Yeniden hesaplama',
        },
        'E',
        'Yeniden hesaplama, belge ya da kayıtlardaki matematiksel doğruluğun denetçi tarafından kontrol edilmesidir.',
    ),
    # düzey 2
    '0043': patch(
        "BDS 501'e göre dava ve tazminat taleplerinin belirlenmesine yönelik prosedürlerden biri aşağıdakilerden hangisi değildir?",
        {
            'A': 'Hukuki gider hesaplarını incelemek',
            'B': 'İşletmenin dış avukatıyla iletişim kurmak',
            'C': 'Davacı tarafın avukatıyla sözleşme yapmak',
            'D': 'Yönetimi ve hukuk birimini sorgulamak',
            'E': 'Yönetim kurulu tutanaklarını incelemek',
        },
        'C',
        'Denetçi; yönetimi ve hukuk müşavirini sorgular, toplantı tutanaklarını ve hukuki gider hesaplarını inceler, gerektiğinde işletmenin dış hukuk danışmanıyla doğrudan iletişim kurar.',
    ),
    # düzey 2
    '0044': patch(
        "Denetçi, işletmenin dönem sonu stok sayımında hazır bulunarak sayım ekiplerinin talimatlara uyup uymadığını izlemiştir.\n\nBDS 500'e göre bu prosedür aşağıdakilerden hangisidir?",
        {
            'A': 'Dış teyit',
            'B': 'Tetkik',
            'C': 'Gözlem',
            'D': 'Yeniden hesaplama',
            'E': 'Yeniden uygulama',
        },
        'C',
        'Gözlem, başkaları tarafından yürütülen bir sürecin ya da prosedürün izlenmesidir; stok sayımının izlenmesi tipik örneğidir.',
    ),
    # düzey 2
    '0045': patch(
        "BDS 500'e göre denetim kanıtının yeterliliği ile ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Kanıtın kalitesi arttıkça gereken kanıt azalabilir',
            'B': 'Daha fazla kanıt düşük kaliteyi her durumda telafi eder',
            'C': 'Yeterlilik kanıtın miktarının ölçüsüdür',
            'D': 'Yeterlilik ve uygunluk birbiriyle ilişkilidir',
            'E': 'Değerlendirilen önemli yanlışlık riski arttıkça gereken kanıt artar',
        },
        'B',
        'Gerekli kanıt miktarı önemli yanlışlık riskinden ve kanıtın kalitesinden etkilenir. Ancak daha fazla kanıt elde etmek, kanıtın düşük kalitesini telafi etmeyebilir.',
    ),
    # düzey 3
    '0046': patch(
        "Denetçi, işletmenin ürettiği yaşlandırılmış alacak listesini şüpheli alacak karşılığını test etmek için kullanacaktır.\n\nBDS 500'e göre bu bilgiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Liste denetçi tarafından doğrudan kabul edilir',
            'B': 'Listenin doğruluğu hakkında kanıt elde edilir',
            'C': 'Listenin tamlığı hakkında kanıt elde edilir',
            'D': 'Yeterince kesin ve ayrıntılı olup olmadığı değerlendirilir',
            'E': 'Liste uygun prosedürlerle kanıt olarak kullanılabilir',
        },
        'A',
        'BDS 500: denetçi, işletmenin ürettiği bilgiyi kanıt olarak kullanırken bilginin doğruluğu ve tamlığı hakkında kanıt elde eder ve amaçlarına göre yeterince kesin ve ayrıntılı olup olmadığını değerlendirir; bilgi doğrudan kabul edilmez.',
    ),
    # düzey 3
    '0047': patch(
        'I. Risk değerlendirme\nII. Maddi doğrulama\nIII. Denetimin sonuna yakın genel sonuç oluşturma\n\nYukarıdaki aşamalardan hangilerinde analitik prosedürlerin uygulanması zorunludur?',
        {
            'A': 'II ve III',
            'B': 'I ve III',
            'C': 'I, II ve III',
            'D': 'Yalnız I',
            'E': 'I ve II',
        },
        'B',
        'Analitik prosedürler risk değerlendirme prosedürü olarak (BDS 315) ve denetimin sonuna yakın genel sonuç oluşturmak için (BDS 520) uygulanır. Maddi doğrulama prosedürü olarak kullanımı denetçinin tercihine bağlıdır.',
    ),
    # düzey 3
    '0048': patch(
        "Denetçi, 31 Aralık 2025'ten önceki ve sonraki beşer günde düzenlenen sevk irsaliyelerini satış kayıtlarıyla karşılaştırmıştır.\n\nBu prosedür esas olarak hangi yönetim beyanına yöneliktir?",
        {
            'A': 'Sınıflandırma',
            'B': 'Varlık',
            'C': 'Haklar ve yükümlülükler',
            'D': 'Değerleme',
            'E': 'Dönem ayırımı',
        },
        'E',
        'Dönem sonuna yakın işlemlerin doğru döneme kaydedilip kaydedilmediğinin test edilmesi dönem ayırımı (kesim) beyanına yöneliktir.',
    ),
    # düzey 3
    '0049': patch(
        "Bir şirket yatırım amaçlı gayrimenkullerinin değerini, yönetimin görevlendirdiği bir gayrimenkul değerleme uzmanına belirletmiştir.\n\nBDS 500'e göre aşağıdakilerden hangisi denetçinin bu uzmanla ilgili olarak yapması gerekenlerden biri değildir?",
        {
            'A': 'Uzmanın çalışmasını anlamak',
            'B': 'Uzmanın yetkinliğini değerlendirmek',
            'C': 'Çalışmanın uygunluğunu değerlendirmek',
            'D': 'Uzmanın ücretini onaylamak',
            'E': 'Uzmanın tarafsızlığını değerlendirmek',
        },
        'D',
        'Yönetimin uzmanının çalışması kanıt olarak kullanılacaksa denetçi uzmanın yetkinliğini, kabiliyetini ve tarafsızlığını değerlendirir, çalışmasını anlar ve ilgili yönetim beyanı için kanıt olarak uygunluğunu değerlendirir.',
    ),
    # düzey 2
    '0050': patch(
        "Denetçi, satın alma faturalarının onaylanmasına ilişkin kontrolü işletme personeli gibi bizzat ve bağımsız olarak baştan yürütmüştür.\n\nBDS 500'e göre bu prosedür aşağıdakilerden hangisidir?",
        {
            'A': 'Yeniden uygulama',
            'B': 'Dış teyit',
            'C': 'Yeniden hesaplama',
            'D': 'Gözlem',
            'E': 'Tetkik',
        },
        'A',
        'Yeniden uygulama, aslında işletmenin iç kontrolünün parçası olarak yürütülen prosedürlerin ya da kontrollerin denetçi tarafından bağımsız olarak yürütülmesidir.',
    ),
    # düzey 3
    '0051': patch(
        'Hesap bakiyelerine ilişkin yönetim beyanı ile bu beyanı test eden prosedür aşağıdakilerden hangisinde yanlış eşleştirilmiştir?',
        {
            'A': 'Dönem ayırımı – Yıl sonu sevkiyatların incelenmesi',
            'B': 'Haklar – Tapu kayıtlarının incelenmesi',
            'C': 'Tamlık – Sonraki ödemelerin incelenmesi',
            'D': 'Değerleme – Alacak bakiyesinin teyidi',
            'E': 'Varlık – Stok sayımının gözlemi',
        },
        'D',
        'Alacak teyidi alacağın varlığına ilişkin güçlü kanıt sağlar, ancak tahsil edilebilirliğine, yani değerlemeye ilişkin yeterli kanıt sağlamaz. Diğer eşleştirmeler uygundur.',
    ),
    # düzey 2
    '0052': patch(
        "Stoklar önemli olan bir şirkette denetçi fiziki sayıma katılmaktadır.\n\nBDS 501'e göre aşağıdakilerden hangisi denetçinin sayıma katılım sırasında yapması gereken işlerden biri değildir?",
        {
            'A': 'Stokları incelemek',
            'B': 'Stokları kendisi tek başına saymak',
            'C': 'Sayım prosedürlerinin uygulanışını gözlemlemek',
            'D': 'Test sayımları yapmak',
            'E': 'Yönetimin sayım talimatlarını değerlendirmek',
        },
        'B',
        'Denetçi sayıma katılarak yönetimin talimat ve prosedürlerini değerlendirir, uygulanışını gözlemler, stokları inceler ve test sayımları yapar. Sayımı yapmak yönetimin sorumluluğudur.',
    ),
    # düzey 3
    '0053': patch(
        "Yönetim, denetçinin işletmenin dış hukuk danışmanıyla görüşmesine ve ona soruşturma mektubu gönderilmesine izin vermemiştir; alternatif prosedürlerle de yeterli kanıt elde edilememiştir.\n\nBDS 501'e göre denetçi ne yapar?",
        {
            'A': 'Konuyu raporda belirtmez',
            'B': "BDS 705'e göre görüşünü değiştirir",
            'C': 'Davaları tablolardan çıkarır',
            'D': 'Olumlu görüş verir',
            'E': 'Avukata yönetimden habersiz yazar',
        },
        'B',
        "Yönetim dış hukuk danışmanıyla iletişime izin vermezse ve alternatif prosedürlerle yeterli kanıt elde edilemezse denetçi BDS 705'e uygun olarak görüşünü değiştirir.",
    ),
    # düzey 2
    '0054': patch(
        "BDS 520'ye göre maddi doğrulama amaçlı analitik prosedürlerle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Kullanılan verilerin güvenilirliği değerlendirilmez',
            'B': 'Kabul edilebilir fark tutarı önceden belirlenir',
            'C': 'Hacmi büyük ve öngörülebilir işlemlerde daha etkilidir',
            'D': 'Denetçi yeterince kesin bir beklenti geliştirir',
            'E': 'Beklentiden önemli sapmalar araştırılır',
        },
        'A',
        "Denetçi, beklentiyi geliştirirken kullandığı verilerin kaynağını, karşılaştırılabilirliğini ve güvenilirliğini değerlendirir. Diğer ifadeler BDS 520'nin gerekleridir.",
    ),
    # düzey 2
    '0055': patch(
        'Denetçi bankaya yazı göndererek işletmenin dönem sonu mevduat bakiyelerini ve kredi borçlarını bankanın doğrudan kendisine bildirmesini istemiştir.\n\nBu prosedür aşağıdakilerden hangisidir?',
        {
            'A': 'Yeniden hesaplama',
            'B': 'Tetkik',
            'C': 'Dış teyit',
            'D': 'Gözlem',
            'E': 'Yeniden uygulama',
        },
        'C',
        'Dış teyit, üçüncü taraftan denetçiye doğrudan, kâğıt ya da elektronik ortamda yazılı yanıt olarak elde edilen kanıttır.',
    ),
    # düzey 2
    '0056': patch(
        'Aşağıdakilerden hangisi kasa hesabının maddi doğrulamasında denetçinin uygulayacağı bir prosedür değildir?',
        {
            'A': 'Büyük tutarlı çıkışları belgeye dayandırmak',
            'B': 'Sürpriz kasa sayımı yapmak',
            'C': 'Dönem sonu kasa hareketlerini incelemek',
            'D': 'Kasa sorumlusunun izin günlerini planlamak',
            'E': 'Sayım sonucunu kayıtla karşılaştırmak',
        },
        'D',
        'Kasa denetiminde sürpriz sayım, sayımın kayıtla karşılaştırılması, dönem sonu hareketlerinin ve büyük çıkışların belgelerinin incelenmesi maddi doğrulama prosedürleridir. Personel planlaması denetçinin işi değildir.',
    ),
    # düzey 2
    '0057': patch(
        "BDS 520'ye göre maddi doğrulama amaçlı analitik prosedür tasarlarken denetçinin yapması gerekenlerden biri aşağıdakilerden hangisi değildir?",
        {
            'A': 'Prosedürün uygunluğunu belirlemek',
            'B': 'Yönetimin beklentisini esas almak',
            'C': 'Kullanılan verilerin güvenilirliğini değerlendirmek',
            'D': 'Yeterince kesin bir beklenti geliştirmek',
            'E': 'Kabul edilebilir fark tutarını belirlemek',
        },
        'B',
        'Denetçi; prosedürün beyana uygunluğunu belirler, verilerin güvenilirliğini değerlendirir, yeterince kesin bir beklentiyi kendisi geliştirir ve daha fazla araştırma gerektirmeyen kabul edilebilir fark tutarını belirler.',
    ),
    # düzey 2
    '0058': patch(
        'Denetçi, 400.000 ₺ borç bakiyesi veren alıcılar hesabından 280.000 ₺ tutarındaki bakiyeler için müşterilerden doğrudan kendisine yanıt istemiştir.\n\nBu çalışmada teyit edilen tutar alıcılar bakiyesinin yüzde kaçıdır?',
        {
            'A': '%28',
            'B': '%30',
            'C': '%70',
            'D': '%40',
            'E': '%60',
        },
        'C',
        "Teyit edilen tutar 280.000 / 400.000 = %70'tir.",
    ),
    # düzey 3
    '0059': patch(
        "BDS 505'e göre negatif teyit taleplerinin tek başına maddi doğrulama prosedürü olarak kullanılabilmesi için aşağıdaki koşullardan hangisi aranmaz?",
        {
            'A': 'Kontrollerin etkinliğine ilişkin kanıt elde edilmesi',
            'B': 'Beklenen istisna oranının çok düşük olması',
            'C': 'Teyitlerin dikkate alınmayacağına dair neden bilinmemesi',
            'D': 'Bakiyelerin az sayıda ve büyük tutarlı olması',
            'E': 'Önemli yanlışlık riskinin düşük değerlendirilmesi',
        },
        'D',
        'Negatif teyit tek başına ancak; risk düşük ve kontrollerin etkinliğine ilişkin kanıt elde edilmişse, anakütle çok sayıda küçük ve homojen bakiyeden oluşuyorsa, beklenen istisna oranı çok düşükse ve teyit verenlerin talepleri dikkate almayacağına dair bir neden bilinmiyorsa kullanılır.',
    ),
    # düzey 3
    '0060': patch(
        "Bir şirketin mali işler direktörü yıl ortasında göreve başlamıştır.\n\nBDS 580'e göre direktörün yazılı beyanının kapsamı aşağıdakilerden hangisidir?",
        {
            'A': 'Son çeyrek',
            'B': 'Denetçinin seçtiği aylar',
            'C': 'Önceki direktörün imzaladığı dönem',
            'D': 'Göreve başladığı tarihten sonrası',
            'E': 'Denetlenen dönemlerin tamamı',
        },
        'E',
        'Yazılı beyanlar raporda atıfta bulunulan tüm finansal tabloları ve dönemleri kapsar; mevcut yönetim dönemin bir kısmında görevde olmasa bile sorumluluklarını beyanlarında üstlenir.',
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
    print(f"1 paket / {len(PATCHES)} soru ('Denetim Kanıtı ve Teknikleri' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
