#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anonim Sirket — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

    olcut                gercek   once   sonra
    medyan kok              257     89     136
    olumsuz kok           %41,5     %0     %40
    kor ogrenci            <=%30    %30       —
    boy egilimi               —   29/9       —

Konu AS'ye OZGU derinligi olcuyor (ticaret_sirketleri sirket turlerini genel
olarak isliyor): kurulus ve sermaye sistemleri (esas ↔ kayitli), pay ve pay
senetleri, genel kurul ↔ yonetim kurulu devredilemez yetki ayrimi (md. 408 ↔
375), azinlik haklari (md. 411, 438-439, 531), sermaye artirimi-azaltimi ve
rushan hakki, kar dagitimi ve yedek akceler, sermaye kaybi ile borca batiklik
(md. 376), sona erme ve tasfiye.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: TTK md. 329-562 · ozellikle md. 329, 332, 340, 342, 344, 355, 359, 365, 375, 376, 395-396, 407, 408, 411, 416, 437, 438-439, 445, 460, 461, 473-474, 478, 482-483, 489-493, 509, 519, 523, 531, 533, 553.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/ticaret_hukuku/anonim_sirket.json"
STYLE_REF = "SGS Hukuk (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "as-gen-"


def patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": '6102 sayili Turk Ticaret Kanunu'},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        'Bir anonim şirket kurulurken sermayenin bir bölümü nakit, bir bölümü ise kurucu ortağın vereceği danışmanlık hizmeti olarak taahhüt edilmiştir. Ayrıca bir ortak vadesi gelmemiş bir alacağını sermaye olarak koymak istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Üç kalem de sermaye olarak konulabilir',
            'B': 'Vadesi gelmemiş alacak konulabilir ancak hizmet edimi konulamaz',
            'C': 'Hizmet edimi konulabilir ancak vadesi gelmemiş alacak konulamaz',
            'D': 'Nakit sermaye konulabilir; hizmet edimi ve vadesi gelmemiş alacak sermaye olarak konulamaz',
            'E': 'Yalnızca ayni sermaye konulabilir; nakit sermaye için ayrıca özel bir izin alınması gerekir',
        },
        'D',
        'TTK md. 342: paradan başka, ekonomik değeri olan ve devrolunabilen malvarlığı unsurları ayni sermaye olarak konulabilir. Ancak HİZMET EDİMLERİ, KİŞİSEL EMEK, ticari itibar ve VADESİ GELMEMİŞ ALACAKLAR sermaye olamaz.',
    ),
    # düzey 3
    '0002': patch(
        'Bir anonim şirkette kurucular, nakden taahhüt edilen payların tamamını tescilden sonraki beş yıl içinde ödemeyi kararlaştırmıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Nakden taahhüt edilen payların kanunda belirtilen bölümünün tescilden önce ödenmesi gerekir',
            'B': 'Sermaye kanunda öngörülen asgari tutardan az olamaz',
            'C': 'Nakden taahhüt edilen payların tamamı tescilden sonra serbestçe belirlenen bir sürede ödenebilir',
            'D': 'Ayni sermaye taahhütleri tescille birlikte şirkete geçer',
            'E': 'Kalan bölüm kanunda öngörülen süre içinde ödenir',
        },
        'C',
        'TTK md. 344: nakden taahhüt edilen payların itibarî değerinin kanunda belirtilen oranı TESCİLDEN ÖNCE, kalanı ise kanunda öngörülen süre içinde ödenir. Ödeme takvimi taraflarca serbestçe uzatılamaz. md. 332 asgari sermayeyi, md. 128 ayni sermayenin geçişini düzenler.',
    ),
    # düzey 3
    '0003': patch(
        'Bir anonim şirket, esas sermaye sistemi yerine kayıtlı sermaye sistemini benimsemek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kayıtlı sermaye sisteminde yönetim kurulu, tavan içinde kalmak koşuluyla sermaye artırımına karar verebilir',
            'B': 'Kayıtlı sermaye sisteminde tavan öngörülmez',
            'C': 'Kayıtlı sermaye sistemi limited şirketlere özgüdür',
            'D': 'Kayıtlı sermaye sisteminde de her bir sermaye artırımı için ayrıca genel kurul kararı alınması gerekir',
            'E': 'Kayıtlı sermaye sistemi yalnızca halka açık şirketlere kapalıdır',
        },
        'A',
        'TTK md. 332 ve 460: kayıtlı sermaye sisteminde esas sözleşmeyle belirlenen TAVAN içinde kalmak ve kanuni koşullara uymak kaydıyla YÖNETİM KURULU sermaye artırımına karar verebilir. Esas sermaye sisteminde ise her artırım genel kurul kararını gerektirir.',
    ),
    # düzey 2
    '0004': patch(
        'Bir anonim şirketin kuruluşunda pay bedellerinin ödenmesi ve tescil sırası tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sermaye kanunda öngörülen asgari tutardan az olamaz',
            'B': 'Tescilden önce şirket adına işlem yapanlar şahsen sorumludur',
            'C': 'Kuruluşta bir veya daha fazla kurucu bulunabilir',
            'D': 'Anonim şirket, esas sözleşmenin noterde onaylanmasıyla tüzel kişilik kazanır',
            'E': 'Anonim şirket, ticaret siciline tescil edilmekle birlikte tüzel kişilik kazanır',
        },
        'D',
        'TTK md. 355: anonim şirket, ticaret siciline TESCİL ile tüzel kişilik kazanır; esas sözleşmenin onaylanması tek başına yeterli değildir. md. 355/2 tescilden önceki işlemlerin sorumluluğunu düzenler.',
    ),
    # düzey 2
    '0005': patch(
        'Anonim şirket ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Sermayesi belirli ve paylara bölünmüştür. II. Borçlarından yalnızca malvarlığıyla sorumludur. III. Pay sahipleri şirket borçlarından kişisel olarak sorumludur.',
        {
            'A': 'II ve III',
            'B': 'I, II ve III',
            'C': 'I ve II',
            'D': 'I ve III',
            'E': 'Yalnız I',
        },
        'C',
        'I ve II doğrudur (TTK md. 329). III YANLIŞTIR: pay sahipleri yalnızca taahhüt ettikleri sermaye payları ile ve şirkete karşı sorumludur.',
    ),
    # düzey 3
    '0006': patch(
        'Bir anonim şirkette bir pay sahibi nama yazılı pay senetlerini, bir diğeri hamiline yazılı pay senetlerini devretmek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Nama yazılı pay senetleri yalnızca teslimle, hamiline yazılı pay senetleri ise ciro ve teslimle devredilir',
            'B': 'Her ikisi de noter onaylı sözleşmeyle devredilir',
            'C': 'Her ikisi de yalnızca zilyetliğin devriyle devredilir',
            'D': 'Pay senetleri, esas sözleşmede aksi yazılsa dahi devredilemez',
            'E': 'Nama yazılı pay senetleri ciro ve zilyetliğin devriyle, hamiline yazılı pay senetleri zilyetliğin devriyle devredilir',
        },
        'E',
        'TTK md. 489-490: HAMİLİNE yazılı pay senetlerinin devri, zilyetliğin geçirilmesiyle şirkete ve üçüncü kişilere karşı hüküm ifade eder. NAMA yazılı pay senetleri ise ciro edilmiş nama yazılı pay senedinin zilyetliğinin geçirilmesiyle devredilir.',
    ),
    # düzey 3
    '0007': patch(
        'Bir anonim şirketin esas sözleşmesinde nama yazılı payların devri için yönetim kurulunun onayı öngörülmüştür. Yönetim kurulu, esas sözleşmede sayılmayan bir gerekçeyle onay vermemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Onay şartı yalnızca hamiline yazılı paylar için konulabilir',
            'B': 'Yönetim kurulu onayı serbestçe reddedebilir',
            'C': 'Devrin sınırlandırılması ancak kanunda ve esas sözleşmede öngörülen sebeplere dayanabilir; keyfî red mümkün değildir',
            'D': 'Onay verilmemesi devri kendiliğinden geçerli kılar',
            'E': 'Nama yazılı payların devri, esas sözleşmede aksine hüküm bulunsa dahi hiçbir sebeple sınırlandırılamaz',
        },
        'C',
        'TTK md. 493: şirket, esas sözleşmede öngörülmüş ÖNEMLİ BİR SEBEBİ ileri sürerek ya da devredene paylarını gerçek değeriyle almayı önererek onay vermekten kaçınabilir. Red keyfî olamaz; sebep kanunda ve esas sözleşmede sınırlanmıştır.',
    ),
    # düzey 2
    '0008': patch(
        'Bir anonim şirkette pay sahibinin hakları sınıflandırılmaktadır. Buna göre aşağıdakilerden hangisi pay sahibinin haklarından biri değildir?',
        {
            'A': 'Genel kurul toplantısına katılma ve oy kullanma hakkı',
            'B': 'Bilgi alma ve inceleme hakkı',
            'C': 'Şirketin günlük yönetimine doğrudan katılma ve talimat verme hakkı',
            'D': 'Kâr payı alma hakkı',
            'E': 'Tasfiye payı alma hakkı',
        },
        'C',
        'TTK md. 407, 437, 507 vd.: pay sahibinin başlıca hakları kâr payı, genel kurula katılma ve oy, bilgi alma ve inceleme, tasfiye payı ile rüçhan hakkıdır. Şirketin YÖNETİMİ md. 365 uyarınca YÖNETİM KURULUNA aittir; pay sahibi doğrudan talimat veremez.',
    ),
    # düzey 3
    '0009': patch(
        'Bir anonim şirket sermaye artırımına gitmiş; mevcut pay sahiplerinden biri yeni paylardan öncelikle alma hakkını kullanmak istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Rüçhan hakkı, haklı sebep bulunsa bile sınırlandırılamaz',
            'B': 'Pay sahibi rüçhan hakkına sahiptir; bu hak ancak haklı sebeple ve nitelikli çoğunlukla sınırlandırılabilir',
            'C': 'Rüçhan hakkı yalnızca imtiyazlı pay sahiplerine tanınmıştır',
            'D': 'Rüçhan hakkı bulunmaz; yeni paylar serbestçe satılır',
            'E': 'Pay sahiplerinin rüçhan hakkı, haklı sebep aranmaksızın yönetim kurulu kararıyla serbestçe kaldırılabilir',
        },
        'B',
        'TTK md. 461: her pay sahibi, yeni çıkarılan payları mevcut paylarının sermayeye oranına göre alma hakkını haizdir. RÜÇHAN HAKKI, ancak HAKLI SEBEPLERİN varlığında ve genel kurulun nitelikli çoğunlukla alacağı kararla sınırlandırılabilir ya da kaldırılabilir.',
    ),
    # düzey 3
    '0010': patch(
        'Bir anonim şirkette yönetim kurulu; esas sözleşmeyi değiştirme, finansal tabloları onaylama ve şirketin üst düzey yönetimini belirleme yetkilerinin kendisinde olduğunu ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Esas sözleşme değişikliği yönetim kuruluna; finansal tabloların onayı ile üst düzey yönetim ise genel kurula aittir',
            'B': 'Yetki dağılımı esas sözleşmeyle serbestçe belirlenir',
            'C': 'Esas sözleşme değişikliği ve finansal tabloların onaylanması genel kurula, üst düzey yönetim ise yönetim kuruluna aittir',
            'D': 'Üç yetki de genel kurula aittir',
            'E': 'Üç yetki de yönetim kuruluna aittir',
        },
        'C',
        'TTK md. 408: esas sözleşmenin değiştirilmesi ve finansal tabloların onaylanması GENEL KURULUN devredilemez yetkilerindendir. md. 375: şirketin üst düzey yönetimi ve teşkilat yapısının belirlenmesi YÖNETİM KURULUNUN devredilemez görevlerindendir. Devredilemez yetkiler esas sözleşmeyle değiştirilemez.',
    ),
    # düzey 3
    '0011': patch(
        'Bir anonim şirkette sermayenin yirmide birini oluşturan pay sahipleri, genel kurulun toplantıya çağrılmasını istemektedir. Yönetim kurulu talebi reddetmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Azınlık doğrudan genel kurulu toplayabilir',
            'B': 'Talep reddedilirse başvurulacak bir yol bulunmaz',
            'C': 'Azınlık genel kurulun toplantıya çağrılmasını isteyebilir; yönetim kurulu reddederse mahkemeye başvurulabilir',
            'D': 'Genel kurulu yalnızca yönetim kurulu toplantıya çağırabilir; azınlık pay sahiplerine böyle bir hak tanınmamıştır',
            'E': 'Çağrı hakkı yalnızca sermayenin çoğunluğuna tanınmıştır',
        },
        'C',
        'TTK md. 411: sermayenin en az yirmide birini oluşturan pay sahipleri (halka kapalı şirketlerde), yönetim kurulundan genel kurulu toplantıya çağırmasını isteyebilir. md. 412: talep yönetim kurulunca reddedilir veya yedi iş günü içinde olumlu yanıt verilmezse, MAHKEMEDEN çağrı izni istenebilir.',
    ),
    # düzey 3
    '0012': patch(
        'Bir anonim şirket genel kurulunda alınan bir karar, kanuna ve dürüstlük kuralına aykırı bulunmuştur. Bir pay sahibi karara karşı ne yapabileceğini araştırmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kanuna aykırı genel kurul kararı yalnızca yeni bir genel kurul kararıyla kaldırılabilir; dava yolu kapalıdır',
            'B': 'Genel kurul kararlarına karşı dava açılamaz',
            'C': 'Dava süresi bir yıl olup muhalefet şerhi aranmaz',
            'D': 'Toplantıda hazır bulunup muhalefetini tutanağa geçirten pay sahibi, üç ay içinde iptal davası açabilir',
            'E': 'İptal davasını yalnızca yönetim kurulu açabilir',
        },
        'D',
        'TTK md. 445-446: kanuna, esas sözleşmeye ya da dürüstlük kuralına aykırı genel kurul kararları aleyhine, toplantıda hazır bulunup KARARA MUHALİF KALARAK muhalefetini tutanağa geçirten pay sahipleri ile yönetim kurulu, karar tarihinden itibaren ÜÇ AY içinde iptal davası açabilir.',
    ),
    # düzey 3
    '0013': patch(
        'Bir anonim şirkette yönetim kurulu üyesi, şirketle kendi adına işlem yapmak ve şirketin faaliyet konusuna giren bir işi kendi hesabına yürütmek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Şirketle işlem yapma ve şirketle rekabet etme yasağı vardır; ancak genel kurulun izniyle bu işlemler yapılabilir',
            'B': 'Yönetim kurulu üyesi, genel kurulun izni aranmaksızın hem şirketle işlem yapabilir hem de rekabet edebilir',
            'C': 'Yasak yalnızca murahhas üyeler için geçerlidir',
            'D': 'Yasak mutlak olup genel kurul izniyle dahi aşılamaz',
            'E': 'Yasak yalnızca esas sözleşmede yazılıysa uygulanır',
        },
        'A',
        'TTK md. 395-396: yönetim kurulu üyesi, GENEL KURULUN İZNİ olmaksızın şirketle kendisi veya başkası adına işlem yapamaz ve şirketin işletme konusuna giren ticari iş türünden bir işlemi kendi veya başkası hesabına yapamaz. Yasak kanundan doğar; izinle aşılabilir.',
    ),
    # düzey 2
    '0014': patch(
        'Bir anonim şirkette yönetim kurulunun görev ve yetkileri belirlenmektedir. Buna göre aşağıdakilerden hangisi yönetim kurulunun devredilemez görevlerinden biri değildir?',
        {
            'A': 'Yıllık finansal tabloların onaylanması ve kâr payının belirlenmesi',
            'B': 'Şirketin üst düzey yönetimi ve yönetim talimatlarının verilmesi',
            'C': 'Muhasebe, finansal denetim ve finansal planlama düzeninin kurulması',
            'D': 'Borca batıklık durumunun mahkemeye bildirilmesi',
            'E': 'Müdürlerin ve aynı işleve sahip kişilerin atanması ve görevden alınması',
        },
        'A',
        'TTK md. 375: üst düzey yönetim, muhasebe ve finansal denetim düzeninin kurulması, müdürlerin atanması ve borca batıklık bildirimi yönetim kurulunun devredilemez görevlerindendir. FİNANSAL TABLOLARIN ONAYLANMASI ve KÂR PAYININ belirlenmesi md. 408 uyarınca GENEL KURULA aittir.',
    ),
    # düzey 3
    '0015': patch(
        'Bir anonim şirkette son yıllık bilançoya göre sermaye ile kanuni yedek akçeler toplamının yarısının karşılıksız kaldığı anlaşılmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sermaye kaybı hâlinde herhangi bir yükümlülük doğmaz',
            'B': 'Şirket kendiliğinden sona erer',
            'C': 'Sermaye kaybı durumu yalnızca izleyen yılın olağan genel kurul toplantısında görüşülür',
            'D': 'Yönetim kurulu genel kurulu derhâl toplantıya çağırır ve iyileştirici önlemleri sunar',
            'E': 'Yönetim kurulu doğrudan iflas bildiriminde bulunur',
        },
        'D',
        "TTK md. 376/1: son yıllık bilançodan sermaye ile kanuni yedek akçeler toplamının yarısının zarar sebebiyle karşılıksız kaldığı anlaşılırsa, yönetim kurulu genel kurulu HEMEN toplantıya çağırır ve uygun gördüğü iyileştirici önlemleri sunar. Borca batıklık hâli ise md. 376/3'te ayrıca düzenlenmiştir.",
    ),
    # düzey 3
    '0016': patch(
        'Bir anonim şirket sermayesini azaltmak istemektedir. Alacaklıların durumu tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sermaye azaltımı alacaklıları ilgilendirmez',
            'B': 'Anonim şirkette esas sermaye azaltılamaz',
            'C': 'Sermaye azaltımı yönetim kurulu kararıyla yapılır; alacaklılara çağrı yapılması ve ilan edilmesi gerekmez',
            'D': 'Sermaye azaltımında alacaklılara çağrı yapılır ve alacaklarının teminat altına alınması istenebilir',
            'E': 'Sermaye azaltımı yalnızca mahkeme kararıyla yapılabilir',
        },
        'D',
        'TTK md. 473-474: esas sermayenin azaltılmasına genel kurul karar verir; alacaklılara ilan yoluyla çağrı yapılarak alacaklarını bildirmeleri ve TEMİNAT verilmesini istemeleri imkânı tanınır. Azaltım, alacaklıların korunmasına ilişkin bu usul tamamlanmadan tescil edilemez.',
    ),
    # düzey 3
    '0017': patch(
        'Bir anonim şirkette genel kurul, kâr elde edilmiş olmasına rağmen kanuni yedek akçeleri ayırmadan kâr dağıtımına karar vermiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kanuni yedek akçe ayırma yükümlülüğü yalnızca halka açık anonim şirketler için öngörülmüştür',
            'B': 'Yedek akçe yalnızca esas sözleşmede öngörülmüşse ayrılır',
            'C': 'Kanuni yedek akçeler ayrılmadıkça kâr payı dağıtılamaz; karar bu yönüyle kanuna aykırıdır',
            'D': 'Yedek akçeler kâr dağıtımından sonra ayrılır',
            'E': 'Genel kurul kârı serbestçe dağıtabilir; yedek akçe zorunlu değildir',
        },
        'C',
        'TTK md. 519 ve 523: yıllık kârın belirli bir oranı genel kanuni yedek akçeye ayrılır; kanun ve esas sözleşmede öngörülen yedek akçeler AYRILMADIKÇA kâr payı dağıtılamaz. Aksi yöndeki genel kurul kararı iptale tabidir.',
    ),
    # düzey 2
    '0018': patch(
        'Bir anonim şirkette kâr payı dağıtımı incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kâr payı, şirket zarar etmiş olsa dahi sermayeden karşılanarak dağıtılabilir',
            'B': 'Kâr payı pay sahibinin haklarındandır',
            'C': 'Kâr payı ancak net dönem kârından ve serbest yedek akçelerden dağıtılabilir',
            'D': 'Kanuni yedek akçeler ayrılmadıkça kâr payı dağıtılamaz',
            'E': 'Kâr payı dağıtımına genel kurul karar verir',
        },
        'A',
        'TTK md. 509: kâr payı ancak NET DÖNEM KÂRINDAN ve serbest yedek akçelerden dağıtılabilir. Sermayeden kâr dağıtımı sermayenin korunması ilkesine aykırıdır.',
    ),
    # düzey 3
    '0019': patch(
        'Bir anonim şirketin aktiflerinin borçlarını karşılayamadığı bir ara bilançodan anlaşılmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Aktiflerin borçları karşılamadığı anlaşılsa dahi mahkemeye ya da başka bir mercie bildirim yapılması gerekmez',
            'B': 'Bildirim yükümlülüğü genel kurula aittir',
            'C': 'Şirket kendiliğinden sona erer',
            'D': 'Yönetim kurulu durumu mahkemeye bildirir; iyileştirme imkânı varsa iflasın ertelenmesi yolları değerlendirilir',
            'E': 'Bildirim yalnızca alacaklılar talep ederse yapılır',
        },
        'D',
        'TTK md. 376/3: şirketin borca batık olduğu şüphesini uyandıran işaretler varsa yönetim kurulu ara bilanço düzenler; aktiflerin borçları karşılamadığı anlaşılırsa durumu MAHKEMEYE bildirir. md. 375/1-f bu bildirimi yönetim kurulunun devredilemez görevi sayar.',
    ),
    # düzey 3
    '0020': patch(
        'Bir anonim şirkette azınlık pay sahipleri, şirketin belirli olaylarının aydınlatılması için özel denetçi atanmasını istemektedir. Genel kurul talebi reddetmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Özel denetim kurumu kanunda öngörülmemiştir',
            'B': 'Talep reddedilirse azınlık, mahkemeden özel denetçi atanmasını isteyebilir',
            'C': 'Özel denetçi yalnızca genel kurulun olumlu kararıyla atanabilir; başka yol yoktur',
            'D': 'Red hâlinde başvurulacak bir yol bulunmaz',
            'E': 'Özel denetçiyi yönetim kurulu atar',
        },
        'B',
        'TTK md. 438-439: her pay sahibi, pay sahipliği haklarının kullanılabilmesi için gerekliyse belirli olayların özel bir denetimle açıklığa kavuşturulmasını genel kuruldan isteyebilir. Talep REDDEDİLİRSE, sermayenin kanunda öngörülen oranını temsil eden pay sahipleri MAHKEMEDEN özel denetçi atanmasını isteyebilir.',
    ),
    # düzey 2
    '0021': patch(
        'Bir anonim şirkette pay sahibinin bilgi alma hakkı incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Pay sahibi genel kurulda yönetim kurulundan bilgi isteyebilir',
            'B': 'Bilgi alma hakkı esas sözleşmeyle veya genel kurul kararıyla kaldırılabilir',
            'C': 'Finansal tablolar ve raporlar genel kuruldan önce incelemeye sunulur',
            'D': 'Bilgi verilmesi şirket sırlarını tehlikeye düşürecek nitelikteyse talep reddedilebilir',
            'E': 'Bilgi alma talebi reddedilirse mahkemeye başvurulabilir',
        },
        'B',
        'TTK md. 437: bilgi alma ve inceleme hakkı, esas sözleşmeyle veya şirket organlarından birinin kararıyla KALDIRILAMAZ ve SINIRLANDIRILAMAZ. Yalnızca şirket sırlarının veya korunması gereken menfaatlerin tehlikeye girmesi hâlinde bilgi verilmesi reddedilebilir; red hâlinde mahkemeye başvurulur.',
    ),
    # düzey 3
    '0022': patch(
        'Bir anonim şirkette haklı sebeplerin varlığı hâlinde şirketin feshi gündeme gelmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Mahkeme yalnızca şirketin feshine karar verebilir; payların gerçek değeriyle alınması gibi başka bir çözüme hükmedemez',
            'B': 'Şirketin feshi yalnızca genel kurul kararıyla mümkündür',
            'C': 'Haklı sebeple fesih davası kanunda öngörülmemiştir',
            'D': 'Fesih davasını yalnızca yönetim kurulu açabilir',
            'E': 'Azınlık haklı sebeple fesih davası açabilir; mahkeme fesih yerine payların gerçek değerle alınmasına da karar verebilir',
        },
        'E',
        'TTK md. 531: haklı sebeplerin varlığında, sermayenin kanunda öngörülen oranını temsil eden pay sahipleri şirketin feshini mahkemeden isteyebilir. Mahkeme fesih yerine, davacı pay sahiplerine paylarının KARAR TARİHİNE EN YAKIN TARİHTEKİ GERÇEK DEĞERLERİNİN ödenmesine ve şirketten çıkarılmalarına ya da duruma uygun düşen başka bir çözüme karar verebilir.',
    ),
    # düzey 2
    '0023': patch(
        'Bir anonim şirket sona ermiş ve tasfiye süreci başlamıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tasfiyenin tamamlanmasıyla sicilden terkin edilir',
            'B': "Şirketin ticaret unvanına 'tasfiye hâlinde' ibaresinin eklenmesi gerekir",
            'C': 'Tasfiye hâlindeki şirket tüzel kişiliğini korur',
            'D': 'Sona eren şirket tasfiye hâline girer',
            'E': 'Sona erme kararıyla şirketin tüzel kişiliği derhâl ortadan kalkar',
        },
        'E',
        "TTK md. 533: sona eren şirket tasfiye hâline girer ve tüzel kişiliğini TASFİYE SONUNA KADAR korur; unvanına 'tasfiye hâlinde' ibaresi eklenir. Tüzel kişilik ancak tasfiye tamamlanıp sicilden terkinle sona erer.",
    ),
    # düzey 2
    '0024': patch(
        'Bir yatırımcı anonim şirketin temel özelliklerini incelemektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Anonim şirket borçlarından yalnızca malvarlığıyla sorumludur',
            'B': 'Anonim şirket bir sermaye şirketidir',
            'C': 'Anonim şirketin sermayesi belirli ve paylara bölünmüştür',
            'D': 'Anonim şirketin borçlarından pay sahipleri de kişisel malvarlıklarıyla sorumludur',
            'E': 'Pay sahipleri yalnızca taahhüt ettikleri sermaye payı ile şirkete karşı sorumludur',
        },
        'D',
        'TTK md. 329: anonim şirket borçlarından dolayı YALNIZ MALVARLIĞIYLA sorumludur; pay sahipleri yalnızca taahhüt ettikleri sermaye payları ile ve ŞİRKETE karşı sorumludur.',
    ),
    # düzey 2
    '0025': patch(
        'Bir anonim şirkette sermaye olarak konulabilecek değerler incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Fikri mülkiyet hakları ayni sermaye olabilir',
            'B': 'Üzerinde sınırlı ayni hak bulunmayan taşınmazlar da ayni sermaye olarak konulabilir',
            'C': 'Ortağın şirkete vereceği kişisel emek ve hizmet edimi sermaye olarak konulabilir',
            'D': 'Vadesi gelmemiş alacaklar sermaye olarak konulamaz',
            'E': 'Nakit sermaye konulabilir',
        },
        'C',
        'TTK md. 342: hizmet edimleri, KİŞİSEL EMEK, ticari itibar ve vadesi gelmemiş alacaklar sermaye olarak konulamaz.',
    ),
    # düzey 2
    '0026': patch(
        'Anonim şirkette organların yetki dağılımı incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Şirketin üst düzey yönetimi, yönetim kurulunun devredilemez görevlerinden biridir',
            'B': 'Genel kurul, devredilemez yetkilerini esas sözleşmeyle yönetim kuruluna bırakabilir',
            'C': 'Borca batıklık bildirimi yönetim kuruluna aittir',
            'D': 'Esas sözleşme değişikliği genel kurulun devredilemez yetkisidir',
            'E': 'Yönetim kurulu üyelerinin seçimi genel kurula aittir',
        },
        'B',
        'TTK md. 408: genel kurulun devredilemez görev ve yetkileri kanunla belirlenmiştir ve esas sözleşmeyle başka bir organa BIRAKILAMAZ.',
    ),
    # düzey 2
    '0027': patch(
        'Anonim şirkette pay devri incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Nama yazılı pay senetleri, ciro edilerek ve zilyetliğin devriyle devredilir',
            'B': 'Nama yazılı payların devri esas sözleşmeyle sınırlandırılabilir',
            'C': 'Hamiline yazılı pay senetleri zilyetliğin devriyle devredilir',
            'D': 'Hamiline yazılı pay senetleri ancak noter onaylı sözleşmeyle devredilir',
            'E': 'Devrin sınırlandırılmasında keyfî red mümkün değildir',
        },
        'D',
        'TTK md. 489: HAMİLİNE yazılı pay senetlerinin devri, zilyetliğin geçirilmesiyle hüküm ifade eder; noter onayı aranmaz.',
    ),
    # düzey 2
    '0028': patch(
        'Anonim şirkette pay sahibinin hakları incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bilgi alma hakkı genel kurul kararıyla sınırlandırılabilir',
            'B': 'Genel kurula katılma ve oy kullanma hakkı yönetsel haklardandır',
            'C': 'Rüçhan hakkı sermaye artırımında gündeme gelir',
            'D': 'Tasfiye payı hakkı tasfiye sonunda doğar',
            'E': 'Kâr payı hakkı pay sahibinin mali haklarındandır',
        },
        'A',
        'TTK md. 437: bilgi alma ve inceleme hakkı esas sözleşmeyle veya ŞİRKET ORGANLARINDAN BİRİNİN KARARIYLA kaldırılamaz ve sınırlandırılamaz.',
    ),
    # düzey 2
    '0029': patch(
        'Anonim şirkette genel kurul kararlarına karşı başvuru yolları incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Genel kurul kararları kesin olup yargı denetimine tabi tutulamaz',
            'B': 'Dava süresi karar tarihinden itibaren üç aydır',
            'C': 'Toplantıda muhalefetini tutanağa geçirten pay sahibi dava açabilir',
            'D': 'Butlan hâlleri ayrıca düzenlenmiştir',
            'E': 'Kanuna aykırı kararlar aleyhine iptal davası açılabilir',
        },
        'A',
        "TTK md. 445-447: genel kurul kararları iptal davasına konu edilebilir; batıl kararlar ayrıca md. 447'de düzenlenmiştir. Kararlar yargı denetimine tabidir.",
    ),
    # düzey 2
    '0030': patch(
        'Anonim şirkette yönetim kurulu üyeliği incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tüzel kişiler yönetim kuruluna üye seçilebilir',
            'B': 'Tüzel kişi adına bir gerçek kişi tescil ve ilan edilir',
            'C': 'Yönetim kurulu üyesinin pay sahibi olması zorunludur',
            'D': 'Üyeler genel kurulca seçilir',
            'E': 'Yönetim kurulu bir veya daha fazla kişiden oluşur',
        },
        'C',
        'TTK md. 359: yönetim kurulu üyelerinin PAY SAHİBİ OLMASI ŞART DEĞİLDİR; tüzel kişiler de üye seçilebilir.',
    ),
    # düzey 2
    '0031': patch(
        'Anonim şirkette sermaye kaybı ve borca batıklık incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bildirim yönetim kurulunun devredilemez görevidir',
            'B': 'Sermaye ile kanuni yedeklerin yarısı karşılıksızsa genel kurul hemen toplanır',
            'C': 'Borca batıklık hâlinde durum mahkemeye bildirilir',
            'D': 'Yönetim kurulu iyileştirici önlemleri genel kurula sunar',
            'E': 'Sermaye kaybı hâlinde şirket kendiliğinden sona erer',
        },
        'E',
        'TTK md. 376: sermaye kaybı hâlinde şirket kendiliğinden SONA ERMEZ; yönetim kurulu genel kurulu toplayarak iyileştirici önlemleri sunar.',
    ),
    # düzey 2
    '0032': patch(
        'Anonim şirkette kâr dağıtımı ve yedek akçeler incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kâr payı net dönem kârından ve serbest yedek akçelerden dağıtılır',
            'B': 'Kanuni yedek akçeler kâr payı dağıtıldıktan sonra ayrılır',
            'C': 'Kâr dağıtımına genel kurul karar verir',
            'D': 'Sermayeden kâr dağıtılamaz',
            'E': 'Kanuni yedek akçeler ayrılmadıkça kâr payı dağıtılamaz',
        },
        'B',
        'TTK md. 519 ve 523: kanun ve esas sözleşmede öngörülen YEDEK AKÇELER AYRILMADIKÇA kâr payı dağıtılamaz; yedekler dağıtımdan ÖNCE ayrılır.',
    ),
    # düzey 2
    '0033': patch(
        'Anonim şirkette azınlık hakları incelenmektedir. Buna göre aşağıdakilerden hangisi azınlık haklarından biri değildir?',
        {
            'A': 'Gündeme madde eklenmesini isteme',
            'B': 'Yönetim kuruluna doğrudan talimat verme hakkı',
            'C': 'Özel denetçi atanmasını isteme',
            'D': 'Genel kurulun toplantıya çağrılmasını isteme hakkı',
            'E': 'Haklı sebeple fesih davası açma',
        },
        'B',
        'TTK md. 411, 412, 438-439 ve 531: azınlık hakları genel kurulun toplantıya çağrılması, gündeme madde eklenmesi, özel denetçi atanması ve haklı sebeple fesih davasıdır. Şirketin YÖNETİMİ md. 365 uyarınca yönetim kuruluna aittir; pay sahipleri doğrudan talimat veremez.',
    ),
    # düzey 2
    '0034': patch(
        'Anonim şirkette sermaye artırımı incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Pay sahiplerinin rüçhan hakkı, haklı sebep aranmaksızın yönetim kurulu kararıyla serbestçe kaldırılabilir',
            'B': 'Kayıtlı sermaye sisteminde, esas sözleşmedeki tavan içinde yönetim kurulu artırım kararı verebilir',
            'C': 'Pay sahiplerinin rüçhan hakkı vardır',
            'D': 'Esas sermaye sisteminde artırıma genel kurul karar verir',
            'E': 'Rüçhan hakkı haklı sebeple ve nitelikli çoğunlukla sınırlandırılabilir',
        },
        'A',
        'TTK md. 461: rüçhan hakkı ancak HAKLI SEBEPLERİN varlığında ve GENEL KURULUN nitelikli çoğunlukla alacağı kararla sınırlandırılabilir; yönetim kurulu serbestçe kaldıramaz.',
    ),
    # düzey 2
    '0035': patch(
        'Anonim şirketin sona ermesi ve tasfiyesi incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tasfiye hâlindeki şirketi genel kurul temsil eder',
            'B': 'Tasfiye memurları şirketi temsil eder',
            'C': 'Tasfiye sonunda sicilden terkin edilir',
            'D': 'Sona eren şirket tasfiye hâline girer',
            'E': 'Şirketin tüzel kişiliği tasfiye sonuna kadar korunur',
        },
        'A',
        'TTK md. 536 vd.: tasfiye hâlindeki şirketi TASFİYE MEMURLARI temsil eder; genel kurul varlığını sürdürse de temsil yetkisi tasfiye memurlarındadır.',
    ),
    # düzey 2
    '0036': patch(
        'Yönetim kurulu üyesinin şirketle ilişkileri incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Şirketle işlem yapma ve rekabet yasakları genel kurulun izniyle aşılabilir',
            'B': 'Şirketle işlem yapma yasağı vardır',
            'C': 'Yasaklar kanundan doğar',
            'D': 'Yönetim kurulu üyesi şirketle kendi adına serbestçe işlem yapabilir',
            'E': 'Rekabet yasağı vardır',
        },
        'D',
        'TTK md. 395-396: yönetim kurulu üyesi GENEL KURULUN İZNİ olmaksızın şirketle kendisi veya başkası adına işlem yapamaz.',
    ),
    # düzey 0
    '0037': patch(
        'Bir yatırımcı, borçlarından yalnızca malvarlığıyla sorumlu olan ve sermayesi paylara bölünmüş şirket türünü aramaktadır. Buna göre bu şirket türü aşağıdakilerden hangisidir?',
        {
            'A': 'Adi komandit şirket',
            'B': 'Komandit şirket',
            'C': 'Anonim şirket',
            'D': 'Adi şirket',
            'E': 'Kollektif şirket',
        },
        'C',
        'TTK md. 329: anonim şirket, sermayesi belirli ve paylara bölünmüş olan, borçlarından dolayı yalnız malvarlığıyla sorumlu bulunan şirkettir.',
    ),
    # düzey 0
    '0038': patch(
        'Anonim şirketin zorunlu organları aşağıdakilerden hangisinde birlikte ve doğru verilmiştir?',
        {
            'A': 'Genel kurul, yönetim kurulu ve denetçi',
            'B': 'Genel kurul ve müdürler kurulu',
            'C': 'Yalnızca yönetim kurulu',
            'D': 'Yönetim kurulu ve denetim komitesi',
            'E': 'Genel kurul ve yönetim kurulu',
        },
        'E',
        'TTK md. 364 vd. ve 407 vd.: anonim şirketin zorunlu organları GENEL KURUL ve YÖNETİM KURULUDUR; denetçi 6102 sayılı TTK ile organ olmaktan çıkarılmıştır.',
    ),
    # düzey 0
    '0039': patch(
        'Sermaye artırımında pay sahibinin yeni paylardan öncelikle alma hakkı aşağıdakilerden hangisidir?',
        {
            'A': 'Rüçhan hakkı',
            'B': 'Tasfiye payı hakkı',
            'C': 'Kâr payı hakkı',
            'D': 'Oy hakkı',
            'E': 'Bilgi alma hakkı',
        },
        'A',
        'TTK md. 461: her pay sahibi, yeni çıkarılan payları mevcut paylarının sermayeye oranına göre alma hakkını (RÜÇHAN HAKKI) haizdir.',
    ),
    # düzey 0
    '0040': patch(
        'Anonim şirkette esas sözleşmenin değiştirilmesi yetkisi hangi organa aittir?',
        {
            'A': 'Tasfiye memurları',
            'B': 'Denetim komitesi',
            'C': 'Yönetim kurulu',
            'D': 'Genel kurul',
            'E': 'Müdürler kurulu',
        },
        'D',
        'TTK md. 408: esas sözleşmenin değiştirilmesi GENEL KURULUN devredilemez görev ve yetkilerindendir.',
    ),
    # düzey 0
    '0041': patch(
        'Bir anonim şirkette borca batıklık durumunun mahkemeye bildirilmesi görevi hangi organa aittir?',
        {
            'A': 'Yönetim kurulu',
            'B': 'Denetçi',
            'C': 'Tasfiye memurları',
            'D': 'Genel kurul',
            'E': 'Pay sahipleri',
        },
        'A',
        'TTK md. 375/1-f ve 376/3: borca batıklık durumunun mahkemeye bildirilmesi YÖNETİM KURULUNUN devredilemez görevlerindendir.',
    ),
    # düzey 0
    '0042': patch(
        'Anonim şirket hangi anda tüzel kişilik kazanır?',
        {
            'A': 'Sermayenin tamamının ödenmesiyle',
            'B': 'Ticaret siciline tescil ile',
            'C': 'Vergi dairesine kayıtla',
            'D': 'Esas sözleşmenin noterde onaylanmasıyla',
            'E': 'İlk genel kurulun toplanmasıyla',
        },
        'B',
        'TTK md. 355: anonim şirket, ticaret siciline TESCİL ile tüzel kişilik kazanır.',
    ),
    # düzey 1
    '0043': patch(
        'Bir anonim şirkette pay sahibi, taahhüt ettiği sermaye payını ödememiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Şirketin başvurabileceği bir yol bulunmaz',
            'B': 'Pay sahibi temerrüde düşer; şirket kanunda öngörülen yollarla payı iptal edebilir',
            'C': 'Pay sahibi kendiliğinden ortaklıktan çıkar',
            'D': 'Ödenmeyen sermaye borcu, şirketteki diğer pay sahiplerinden payları oranında istenir',
            'E': 'Şirket doğrudan iflas bildiriminde bulunur',
        },
        'B',
        'TTK md. 482-483: sermaye borcunu süresinde ödemeyen pay sahibi temerrüt faizi ödemekle yükümlüdür; şirket ayrıca pay sahibini haklarından yoksun bırakabilir ve payını İPTAL edebilir (ıskat).',
    ),
    # düzey 1
    '0044': patch(
        'Bir anonim şirkette genel kurul toplantısına çağrı yapılmamış ancak tüm pay sahipleri hazır bulunmuştur. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Çağrısız toplantı ancak mahkeme izniyle yapılabilir',
            'B': 'Çağrısız toplantıda yalnızca bilgilendirme yapılabilir; hiçbir bağlayıcı karar alınamaz',
            'C': 'Çağrı usulüne uyulmadan genel kurul toplanamaz ve karar alamaz',
            'D': 'Çağrısız toplantı yalnızca tek pay sahipli şirketlerde mümkündür',
            'E': 'Pay sahiplerinin tamamı hazırsa ve itiraz olmazsa çağrısız genel kurul yapılabilir',
        },
        'E',
        'TTK md. 416: bütün payların sahipleri veya temsilcileri, aralarından biri itirazda bulunmadığı takdirde genel kurula ÇAĞRI USULÜNE UYULMAKSIZIN katılabilir ve gündeme dâhil konularda karar alabilir (çağrısız genel kurul).',
    ),
    # düzey 1
    '0045': patch(
        'Bir anonim şirkette imtiyazlı pay çıkarılması gündeme gelmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İmtiyaz yönetim kurulu kararıyla tanınır',
            'B': 'İmtiyazlı paylar oy hakkından yoksundur',
            'C': 'İmtiyaz esas sözleşmeyle tanınır; kâr payı, oy hakkı gibi konularda üstün hak sağlayabilir',
            'D': 'İmtiyazlı pay çıkarılamaz',
            'E': 'İmtiyaz yalnızca tasfiye payı bakımından tanınabilir; kâr payı ve oy hakkı bakımından tanınamaz',
        },
        'C',
        'TTK md. 478: imtiyaz; kâr payı, tasfiye payı, rüçhan ve oy hakkı gibi haklarda paya tanınan üstün bir hak veya kanunda öngörülmemiş yeni bir pay sahipliği hakkıdır ve ESAS SÖZLEŞMEYLE tanınır.',
    ),
    # düzey 1
    '0046': patch(
        'Bir anonim şirkette yönetim kurulu üyelerinin sorumluluğu incelenmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sorumluluk yalnızca pay sahibi üyeler için doğar',
            'B': 'Yönetim kurulu üyeleri, kanundan ve esas sözleşmeden doğan yükümlülüklerini kusurlarıyla ihlal ederlerse sorumlu olur',
            'C': 'Sorumluluk kusursuz sorumluluk esasına dayanır',
            'D': 'Yönetim kurulu üyelerinin şirkete, pay sahiplerine ve şirket alacaklılarına karşı herhangi bir sorumluluğu bulunmaz',
            'E': 'Sorumluluk yalnızca genel kurul kararıyla doğar',
        },
        'B',
        'TTK md. 553: yönetim kurulu üyeleri, kanundan ve esas sözleşmeden doğan yükümlülüklerini KUSURLARIYLA ihlal ettikleri takdirde şirkete, pay sahiplerine ve alacaklılara karşı verdikleri zarardan sorumludur. Sorumluluk KUSUR esasına dayanır.',
    ),
    # düzey 1
    '0047': patch(
        'Bir anonim şirkette genel kurulun toplantıya çağrılmasını isteme hakkı incelenmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Her pay sahibi tek başına çağrı yapabilir',
            'B': 'Yalnızca yönetim kurulu genel kurulu çağırabilir',
            'C': 'Sermayenin kanunda öngörülen oranını temsil eden azınlık bu talebi yöneltebilir',
            'D': 'Genel kurulu toplantıya çağırma talebi hakkı yalnızca halka açık şirketlerde tanınmıştır',
            'E': 'Yalnızca sermayenin çoğunluğu talep edebilir',
        },
        'C',
        'TTK md. 411: sermayenin en az yirmide birini oluşturan pay sahipleri (halka açık şirketlerde kırkta bir), yönetim kurulundan genel kurulu toplantıya çağırmasını isteyebilir.',
    ),
    # düzey 1
    '0048': patch(
        'Bir anonim şirkette esas sözleşmede öngörülen sermaye tavanı içinde yönetim kurulunun sermaye artırımına karar verebildiği sistem aşağıdakilerden hangisidir?',
        {
            'A': 'Kayıtlı sermaye sistemi',
            'B': 'Değişken sermaye sistemi',
            'C': 'Nominal sermaye sistemi',
            'D': 'Şarta bağlı sermaye sistemi',
            'E': 'Esas sermaye sistemi',
        },
        'A',
        'TTK md. 332 ve 460: KAYITLI SERMAYE SİSTEMİNDE esas sözleşmeyle belirlenen tavan içinde kalmak kaydıyla yönetim kurulu sermaye artırımına karar verebilir.',
    ),
    # düzey 1
    '0049': patch(
        'Bir anonim şirkette belirli olayların aydınlatılması için atanan denetçi aşağıdakilerden hangisidir?',
        {
            'A': 'Kayyım',
            'B': 'Tasfiye memuru',
            'C': 'Bağımsız denetçi',
            'D': 'İşlem denetçisi',
            'E': 'Özel denetçi',
        },
        'E',
        'TTK md. 438-439: pay sahipleri, belirli olayların açıklığa kavuşturulması için ÖZEL DENETİM isteyebilir; genel kurul reddederse mahkemeden ÖZEL DENETÇİ atanması istenebilir.',
    ),
    # düzey 1
    '0050': patch(
        'Bir anonim şirkette pay sahibinin genel kurul kararına karşı iptal davası açma süresi aşağıdakilerden hangisidir?',
        {
            'A': 'Süre öngörülmemiştir',
            'B': 'Karar tarihinden itibaren bir ay',
            'C': 'Karar tarihinden itibaren altı ay',
            'D': 'Karar tarihinden itibaren bir yıl',
            'E': 'Karar tarihinden itibaren üç ay',
        },
        'E',
        'TTK md. 445: iptal davası, karar tarihinden itibaren ÜÇ AY içinde açılır.',
    ),
    # düzey 3
    '0051': patch(
        'Anonim şirket organları ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Zorunlu organlar genel kurul ve yönetim kuruludur. II. Yönetim kurulu üyesinin pay sahibi olması şarttır. III. Esas sözleşme değişikliği genel kurulun devredilemez yetkisidir. IV. Genel kurul devredilemez yetkilerini yönetim kuruluna bırakabilir.',
        {
            'A': 'II ve III',
            'B': 'Yalnız II',
            'C': 'I ve III',
            'D': 'II ve IV',
            'E': 'I, II ve IV',
        },
        'D',
        "II YANLIŞ: TTK md. 359 uyarınca üyenin pay sahibi olması şart değildir. IV YANLIŞ: md. 408'deki devredilemez yetkiler esas sözleşmeyle dahi devredilemez. I ve III doğrudur.",
    ),
    # düzey 2
    '0052': patch(
        'Sermaye ve kâr ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Kişisel emek sermaye olarak konulamaz. II. Kanuni yedek akçeler ayrılmadıkça kâr payı dağıtılamaz. III. Kâr payı sermayeden de dağıtılabilir.',
        {
            'A': 'I ve III',
            'B': 'I, II ve III',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'Yalnız I',
        },
        'C',
        'I doğrudur (TTK md. 342). II doğrudur (md. 519, 523). III YANLIŞTIR: md. 509 uyarınca kâr payı ancak net dönem kârından ve serbest yedek akçelerden dağıtılabilir.',
    ),
    # düzey 3
    '0053': patch(
        'Azınlık hakları ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Azınlık genel kurulun toplantıya çağrılmasını isteyebilir. II. Azınlık özel denetçi atanmasını isteyebilir. III. Azınlık yönetim kuruluna doğrudan talimat verebilir. IV. Azınlık haklı sebeple fesih davası açamaz.',
        {
            'A': 'Yalnız III',
            'B': 'I ve II',
            'C': 'I, III ve IV',
            'D': 'II ve III',
            'E': 'III ve IV',
        },
        'E',
        'III YANLIŞ: şirketin yönetimi yönetim kuruluna aittir (TTK md. 365). IV YANLIŞ: md. 531 uyarınca azınlık haklı sebeple fesih davası açabilir. I (md. 411) ve II (md. 438-439) doğrudur.',
    ),
    # düzey 2
    '0054': patch(
        'Pay ve pay senetleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Hamiline yazılı pay senetleri zilyetliğin devriyle devredilir. II. Nama yazılı payların devri esas sözleşmeyle sınırlandırılabilir. III. Bilgi alma hakkı genel kurul kararıyla kaldırılabilir.',
        {
            'A': 'II ve III',
            'B': 'I ve III',
            'C': 'I, II ve III',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'D',
        'I doğrudur (TTK md. 489). II doğrudur (md. 492-493). III YANLIŞTIR: md. 437 uyarınca bilgi alma hakkı esas sözleşmeyle veya organ kararıyla kaldırılamaz.',
    ),
    # düzey 2
    '0055': patch(
        'Anonim şirkette sermaye artırımı ve azaltımı ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Kayıtlı sermaye sisteminde yönetim kurulu tavan içinde artırım kararı alabilir. II. Sermaye azaltımında alacaklılara çağrı yapılır. III. Rüçhan hakkı yönetim kurulu kararıyla kaldırılabilir.',
        {
            'A': 'I ve III',
            'B': 'I, II ve III',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'I ve II',
        },
        'E',
        'I doğrudur (TTK md. 460). II doğrudur (md. 474). III YANLIŞTIR: md. 461 uyarınca rüçhan hakkı ancak haklı sebeple ve genel kurulun nitelikli çoğunluğuyla sınırlandırılabilir.',
    ),
    # düzey 2
    '0056': patch(
        'Anonim şirkette sorumluluk ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Yönetim kurulu üyeleri kusurlarıyla verdikleri zarardan sorumludur. II. Pay sahipleri şirket borçlarından kişisel olarak sorumlu değildir. III. Yönetim kurulu üyelerinin sorumluluğu kusursuz sorumluluktur.',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'I ve III',
            'E': 'I, II ve III',
        },
        'B',
        'I doğrudur (TTK md. 553). II doğrudur (md. 329/2). III YANLIŞTIR: sorumluluk KUSUR esasına dayanır.',
    ),
    # düzey 2
    '0057': patch(
        'Anonim şirkette genel kurul ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Çağrısız genel kurul mümkündür. II. İptal davası üç ay içinde açılır. III. Genel kurul kararları hiçbir denetime tabi değildir.',
        {
            'A': 'I, II ve III',
            'B': 'II ve III',
            'C': 'I ve III',
            'D': 'Yalnız I',
            'E': 'I ve II',
        },
        'E',
        'I doğrudur (TTK md. 416). II doğrudur (md. 445). III YANLIŞTIR: kararlar iptal ve butlan yönünden yargı denetimine tabidir.',
    ),
    # düzey 2
    '0058': patch(
        'Bir anonim şirkette pay sahibi, genel kurulda yönetim kurulundan şirketin ticari sırlarını da içeren ayrıntılı bilgi istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bilgi alma hakkı bulunmadığından talep dikkate alınmaz',
            'B': 'Bilgi ancak genel kurul kararıyla verilebilir',
            'C': 'Pay sahibinin her bilgi talebi eksiksiz olarak karşılanır',
            'D': 'Bilgi verilmesi şirket sırlarını tehlikeye düşürecekse talep reddedilebilir; red hâlinde mahkemeye başvurulur',
            'E': 'Bilgi talebi yalnızca yönetim kurulunun takdirine bağlı olup bu takdir hiçbir merci tarafından denetlenemez',
        },
        'D',
        'TTK md. 437: bilgi verilmesi, şirket sırlarının açıklanmasına veya korunması gereken diğer şirket menfaatlerinin tehlikeye girmesine yol açacaksa REDDEDİLEBİLİR. Red hâlinde pay sahibi MAHKEMEYE başvurabilir.',
    ),
    # düzey 2
    '0059': patch(
        'Anonim şirkette esas sözleşme ve kanun ilişkisi incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Esas sözleşme, kanunun emredici hükümlerinden ayrılan düzenlemeler getirebilir',
            'B': 'Esas sözleşme değişikliği genel kurul kararıyla yapılır',
            'C': 'Esas sözleşme kanunun emredici hükümlerine aykırı olamaz',
            'D': 'Kanunun açıkça izin verdiği hâllerde esas sözleşmeyle farklı düzenleme yapılabilir',
            'E': 'Genel kurulun devredilemez yetkileri esas sözleşmeyle devredilemez',
        },
        'A',
        "TTK md. 340 (emredici hükümler ilkesi): esas sözleşme, TTK'nın anonim şirketlere ilişkin hükümlerinden ancak KANUNDA AÇIKÇA İZİN VERİLMİŞSE sapabilir.",
    ),
    # düzey 3
    '0060': patch(
        'Anonim şirket ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Anonim şirket ticaret siciline tescille tüzel kişilik kazanır. II. Sermaye kaybı hâlinde şirket kendiliğinden sona erer. III. Kâr payı ancak net dönem kârından ve serbest yedek akçelerden dağıtılır. IV. Bilgi alma hakkı esas sözleşmeyle kaldırılabilir.',
        {
            'A': 'Yalnız II',
            'B': 'I ve III',
            'C': 'II ve IV',
            'D': 'II ve III',
            'E': 'I, II ve IV',
        },
        'C',
        'II YANLIŞ: TTK md. 376 uyarınca sermaye kaybında şirket kendiliğinden sona ermez; yönetim kurulu genel kurulu toplar. IV YANLIŞ: md. 437 uyarınca bilgi alma hakkı esas sözleşmeyle kaldırılamaz. I (md. 355) ve III (md. 509) doğrudur.',
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
    print(f"1 paket / {len(PATCHES)} soru ('Anonim Sirket' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
