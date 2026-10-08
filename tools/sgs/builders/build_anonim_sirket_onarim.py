#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anonim Sirket — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Agustos yapisal kalibrasyonundaki olay tabanli 60 soru korunarak onarildi: genisletilmis ELEME_ISARETI olcutune gore 47 mutlak ifadeli sik ayni dogruluk degerini koruyacak bicimde yeniden yazildi; gerekce tasiyan 15 dogru sik kisaltildi. Kor ogrenci %38 -> %24.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 6102 sayili Turk Ticaret Kanunu (anonim sirket hukumleri)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/ticaret_hukuku/anonim_sirket.json"
STYLE_REF = 'SGS Ticaret Hukuku (gercek sinav yapisina kalibre: olay + kural uygulamasi)'
ONEK = "as-gen-"


def patch(stem, options, answer, solution, ref='6102 sayili Turk Ticaret Kanunu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        "Bir anonim şirket kurulurken sermayenin bir bölümü nakit, bir bölümü ise kurucu ortağın vereceği danışmanlık hizmeti olarak taahhüt edilmiştir. Ayrıca bir ortak vadesi gelmemiş bir alacağını sermaye olarak koymak istemektedir.\n\nTTK'ya göre sermaye olarak konulabilecek değerlerle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Nakit sermaye olarak konulabilir',
            'B': 'Devredilebilen ve ekonomik değeri olan unsurlar ayni sermaye olabilir',
            'C': 'Hizmet edimleri sermaye olarak konulamaz',
            'D': 'Kurucunun danışmanlık hizmeti sermaye olarak konulabilir',
            'E': 'Vadesi gelmemiş alacaklar sermaye olarak konulamaz',
        },
        'D',
        'TTK md. 342: paradan başka, ekonomik değeri olan ve devrolunabilen malvarlığı unsurları ayni sermaye olarak konulabilir. Ancak hizmet edimleri, kişisel emek, ticari itibar ve vadesi gelmemiş alacaklar sermaye olamaz.',
    ),
    # düzey 2
    '0002': patch(
        'Bir anonim şirketin kuruluşunda pay bedellerinin ödenmesi ve tescil sırası tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kuruluşta bir veya daha fazla kurucu bulunabilir',
            'B': 'Tescilden önce şirket adına işlem yapanlar şahsen sorumludur',
            'C': 'Anonim şirket, esas sözleşmenin noterde onaylanmasıyla tüzel kişilik kazanır',
            'D': 'Anonim şirket, ticaret siciline tescil edilmekle birlikte tüzel kişilik kazanır',
            'E': 'Sermaye kanunda öngörülen asgari tutardan az olamaz',
        },
        'C',
        'TTK md. 355: anonim şirket, ticaret siciline TESCİL ile tüzel kişilik kazanır; esas sözleşmenin onaylanması tek başına yeterli değildir. md. 355/2 tescilden önceki işlemlerin sorumluluğunu düzenler.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0003': patch(
        'Bir anonim şirketin esas sözleşmesinde nama yazılı payların devri için yönetim kurulunun onayı öngörülmüştür. Yönetim kurulu, esas sözleşmede sayılmayan bir gerekçeyle onay vermemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Devir ancak kanun ve esas sözleşmedeki sebeplerle sınırlandırılabilir',
            'B': 'Nama yazılı payların devri, esas sözleşmede hüküm bulunsa dahi sınırlandırılamaz',
            'C': 'Onay şartı hamiline yazılı paylar için konulabilir, nama yazılılar için konulamaz',
            'D': 'Onay verilmemesi devri geçerli kılar',
            'E': 'Yönetim kurulu onayı gerekçe göstermeden reddedebilir',
        },
        'A',
        'TTK md. 493: şirket, esas sözleşmede öngörülmüş ÖNEMLİ BİR SEBEBİ ileri sürerek ya da devredene paylarını gerçek değeriyle almayı önererek onay vermekten kaçınabilir. Red keyfî olamaz; sebep kanunda ve esas sözleşmede sınırlanmıştır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0004': patch(
        'Bir anonim şirkette yönetim kurulu; esas sözleşmeyi değiştirme, finansal tabloları onaylama ve şirketin üst düzey yönetimini belirleme yetkilerinin kendisinde olduğunu ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Esas sözleşme değişikliği yönetim kuruluna; finansal tabloların onayı ile üst düzey yönetim ise genel kurula aittir',
            'B': 'Yetki dağılımı esas sözleşmeyle dilendiği gibi belirlenir',
            'C': 'Üç yetki de yönetim kuruluna aittir',
            'D': 'Esas sözleşme değişikliği genel kurulda, üst düzey yönetim yönetim kurulundadır',
            'E': 'Üç yetki de genel kurula aittir',
        },
        'D',
        'TTK md. 408: esas sözleşmenin değiştirilmesi ve finansal tabloların onaylanması GENEL KURULUN devredilemez yetkilerindendir. md. 375: şirketin üst düzey yönetimi ve teşkilat yapısının belirlenmesi YÖNETİM KURULUNUN devredilemez görevlerindendir. Devredilemez yetkiler esas sözleşmeyle değiştirilemez.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0005': patch(
        "Bir anonim şirkette yönetim kurulu üyesi, şirketle kendi adına işlem yapmak ve şirketin faaliyet konusuna giren bir işi kendi hesabına yürütmek istemektedir.\n\nTTK'ya göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Üye genel kurulun izni olmadan şirketle işlem yapamaz',
            'B': 'Üye izinsiz olarak şirketle rekabet edemez',
            'C': 'Bu yasaklar murahhas üyelere özgüdür',
            'D': 'Yasaklar kanundan doğar',
            'E': 'Genel kurulun izniyle bu işlemler yapılabilir',
        },
        'C',
        'TTK md. 395-396: yönetim kurulu üyesi, genel kurulun izni olmaksızın şirketle kendisi veya başkası adına işlem yapamaz ve şirketin işletme konusuna giren ticari iş türünden bir işlemi kendi veya başkası hesabına yapamaz. Yasaklar kanundan doğar, tüm üyeleri bağlar ve genel kurul izniyle aşılabilir.',
    ),
    # düzey 3
    '0006': patch(
        "Bir anonim şirkette genel kurul, kâr elde edilmiş olmasına rağmen kanuni yedek akçeleri ayırmadan kâr dağıtımına karar vermiştir.\n\nTTK'ya göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Yıllık kârın belirli bir oranı genel kanuni yedek akçeye ayrılır',
            'B': 'Kanuni yedek akçe ayrılmadıkça kâr payı dağıtılamaz',
            'C': 'Esas sözleşmede öngörülen yedek akçeler de ayrılmalıdır',
            'D': 'Aksi yöndeki genel kurul kararı iptale tabidir',
            'E': 'Yedek akçeler kâr dağıtımından sonra ayrılır',
        },
        'E',
        'TTK md. 519 ve 523: yıllık kârın belirli bir oranı genel kanuni yedek akçeye ayrılır; kanun ve esas sözleşmede öngörülen yedek akçeler ayrılmadıkça kâr payı dağıtılamaz. Aksi yöndeki genel kurul kararı iptale tabidir.',
    ),
    # düzey 2
    '0007': patch(
        'Bir anonim şirkette pay sahibinin bilgi alma hakkı incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Finansal tablolar ve raporlar genel kuruldan önce incelemeye sunulur',
            'B': 'Bilgi verilmesi şirket sırlarını tehlikeye düşürecek nitelikteyse talep reddedilebilir',
            'C': 'Bilgi alma hakkı esas sözleşmeyle veya genel kurul kararıyla kaldırılabilir',
            'D': 'Bilgi alma talebi reddedilirse mahkemeye başvurulabilir',
            'E': 'Pay sahibi genel kurulda yönetim kurulundan bilgi isteyebilir',
        },
        'C',
        'TTK md. 437: bilgi alma ve inceleme hakkı, esas sözleşmeyle veya şirket organlarından birinin kararıyla KALDIRILAMAZ ve SINIRLANDIRILAMAZ. Yalnızca şirket sırlarının veya korunması gereken menfaatlerin tehlikeye girmesi hâlinde bilgi verilmesi reddedilebilir; red hâlinde mahkemeye başvurulur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0008': patch(
        'Bir anonim şirkette haklı sebeplerin varlığı hâlinde şirketin feshi gündeme gelmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Fesih davasını azınlık değil yönetim kurulu açabilir',
            'B': 'Mahkeme şirketin feshine karar verebilir; payların gerçek değeriyle alınması gibi başka bir çözüme hükmedemez',
            'C': 'Azınlık fesih davası açabilir; mahkeme payların alınmasına da karar verebilir',
            'D': 'Şirketin feshi ancak genel kurul kararıyla mümkündür',
            'E': 'Haklı sebeple fesih davası kanunda öngörülmemiştir',
        },
        'C',
        'TTK md. 531: haklı sebeplerin varlığında, sermayenin kanunda öngörülen oranını temsil eden pay sahipleri şirketin feshini mahkemeden isteyebilir. Mahkeme fesih yerine, davacı pay sahiplerine paylarının KARAR TARİHİNE EN YAKIN TARİHTEKİ GERÇEK DEĞERLERİNİN ödenmesine ve şirketten çıkarılmalarına ya da duruma uygun düşen başka bir çözüme karar verebilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0009': patch(
        'Bir anonim şirkette sermaye olarak konulabilecek değerler incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Nakit sermaye konulabilir',
            'B': 'Ortağın şirkete vereceği kişisel emek ve hizmet edimi sermaye olarak konulabilir',
            'C': 'Üzerinde sınırlı ayni hak bulunmayan taşınmazlar da ayni sermaye olarak konulabilir',
            'D': 'Vadesi gelmemiş alacaklar sermaye olarak konulamaz',
            'E': 'Fikri mülkiyet hakları ayni sermaye olabilir',
        },
        'B',
        'TTK md. 342: hizmet edimleri, KİŞİSEL EMEK, ticari itibar ve vadesi gelmemiş alacaklar sermaye olarak konulamaz.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0010': patch(
        'Anonim şirkette pay sahibinin hakları incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Genel kurula katılma ve oy kullanma hakkı yönetsel haklardandır',
            'B': 'Tasfiye payı hakkı tasfiye sonunda doğar',
            'C': 'Bilgi alma hakkı genel kurul kararıyla sınırlandırılabilir',
            'D': 'Kâr payı hakkı pay sahibinin mali haklarındandır',
            'E': 'Rüçhan hakkı sermaye artırımında gündeme gelir',
        },
        'C',
        'TTK md. 437: bilgi alma ve inceleme hakkı esas sözleşmeyle veya ŞİRKET ORGANLARINDAN BİRİNİN KARARIYLA kaldırılamaz ve sınırlandırılamaz.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0011': patch(
        'Anonim şirkette sermaye kaybı ve borca batıklık incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sermaye ile kanuni yedeklerin yarısı karşılıksızsa genel kurul hemen toplanır',
            'B': 'Bildirim yönetim kurulunun devredilemez görevidir',
            'C': 'Sermaye kaybı hâlinde şirket başka bir işleme gerek olmadan sona erer',
            'D': 'Borca batıklık hâlinde durum mahkemeye bildirilir',
            'E': 'Yönetim kurulu iyileştirici önlemleri genel kurula sunar',
        },
        'C',
        'TTK md. 376: sermaye kaybı hâlinde şirket kendiliğinden SONA ERMEZ; yönetim kurulu genel kurulu toplayarak iyileştirici önlemleri sunar.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0012': patch(
        'Anonim şirkette sermaye artırımı incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Esas sermaye sisteminde artırıma genel kurul karar verir',
            'B': 'Rüçhan hakkı haklı sebeple ve nitelikli çoğunlukla sınırlandırılabilir',
            'C': 'Kayıtlı sermaye sisteminde, esas sözleşmedeki tavan içinde yönetim kurulu artırım kararı verebilir',
            'D': 'Pay sahiplerinin rüçhan hakkı, haklı sebep aranmaksızın yönetim kurulu kararıyla kaldırılabilir',
            'E': 'Pay sahiplerinin rüçhan hakkı vardır',
        },
        'D',
        'TTK md. 461: rüçhan hakkı ancak HAKLI SEBEPLERİN varlığında ve GENEL KURULUN nitelikli çoğunlukla alacağı kararla sınırlandırılabilir; yönetim kurulu serbestçe kaldıramaz.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0013': patch(
        'Sermaye artırımında pay sahibinin yeni paylardan öncelikle alma hakkı aşağıdakilerden hangisidir?',
        {
            'A': 'Rüçhan hakkı',
            'B': 'Kâr payı hakkı',
            'C': 'Oy hakkı',
            'D': 'Tasfiye payı hakkı',
            'E': 'Bilgi alma hakkı',
        },
        'A',
        'TTK md. 461: her pay sahibi, yeni çıkarılan payları mevcut paylarının sermayeye oranına göre alma hakkını (RÜÇHAN HAKKI) haizdir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0014': patch(
        'Anonim şirket hangi anda tüzel kişilik kazanır?',
        {
            'A': 'Ticaret siciline tescil ile',
            'B': 'Vergi dairesine kayıtla',
            'C': 'Esas sözleşmenin noterde onaylanmasıyla',
            'D': 'İlk genel kurulun toplanmasıyla',
            'E': 'Sermayenin tamamının ödenmesiyle',
        },
        'A',
        'TTK md. 355: anonim şirket, ticaret siciline TESCİL ile tüzel kişilik kazanır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0015': patch(
        "Bir anonim şirkette imtiyazlı pay çıkarılması gündeme gelmiştir.\n\nTTK'ya göre imtiyazla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'İmtiyaz esas sözleşmeyle tanınır',
            'B': 'İmtiyaz kâr payı bakımından tanınabilir',
            'C': 'İmtiyaz oy hakkı bakımından tanınabilir',
            'D': 'İmtiyaz yönetim kurulu kararıyla tanınır',
            'E': 'İmtiyaz tasfiye payı bakımından tanınabilir',
        },
        'D',
        'TTK md. 478: imtiyaz; kâr payı, tasfiye payı, rüçhan ve oy hakkı gibi haklarda paya tanınan üstün bir hak veya kanunda öngörülmemiş yeni bir pay sahipliği hakkıdır ve esas sözleşmeyle tanınır; yönetim kurulu kararıyla tanınamaz.',
    ),
    # düzey 1
    '0016': patch(
        'Bir anonim şirkette esas sözleşmede öngörülen sermaye tavanı içinde yönetim kurulunun sermaye artırımına karar verebildiği sistem aşağıdakilerden hangisidir?',
        {
            'A': 'Şarta bağlı sermaye sistemi',
            'B': 'Nominal sermaye sistemi',
            'C': 'Değişken sermaye sistemi',
            'D': 'Kayıtlı sermaye sistemi',
            'E': 'Esas sermaye sistemi',
        },
        'D',
        'TTK md. 332 ve 460: KAYITLI SERMAYE SİSTEMİNDE esas sözleşmeyle belirlenen tavan içinde kalmak kaydıyla yönetim kurulu sermaye artırımına karar verebilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0017': patch(
        'Sermaye ve kâr ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Kişisel emek sermaye olarak konulamaz. II. Kanuni yedek akçeler ayrılmadıkça kâr payı dağıtılamaz. III. Kâr payı sermayeden de dağıtılabilir.',
        {
            'A': 'I ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'C',
        'I doğrudur (TTK md. 342). II doğrudur (md. 519, 523). III YANLIŞTIR: md. 509 uyarınca kâr payı ancak net dönem kârından ve serbest yedek akçelerden dağıtılabilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0018': patch(
        'Anonim şirkette sorumluluk ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Yönetim kurulu üyeleri kusurlarıyla verdikleri zarardan sorumludur. II. Pay sahipleri şirket borçlarından kişisel olarak sorumlu değildir. III. Yönetim kurulu üyelerinin sorumluluğu kusursuz sorumluluktur.',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'Yalnız I',
        },
        'A',
        'I doğrudur (TTK md. 553). II doğrudur (md. 329/2). III YANLIŞTIR: sorumluluk KUSUR esasına dayanır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0019': patch(
        'Anonim şirkette genel kurul ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Çağrısız genel kurul mümkündür. II. İptal davası üç ay içinde açılır. III. Genel kurul kararları hiçbir denetime tabi değildir.',
        {
            'A': 'Yalnız I',
            'B': 'II ve III',
            'C': 'I ve III',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'D',
        'I doğrudur (TTK md. 416). II doğrudur (md. 445). III YANLIŞTIR: kararlar iptal ve butlan yönünden yargı denetimine tabidir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0020': patch(
        'Anonim şirket ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Anonim şirket ticaret siciline tescille tüzel kişilik kazanır. II. Sermaye kaybı hâlinde şirket kendiliğinden sona erer. III. Kâr payı ancak net dönem kârından ve serbest yedek akçelerden dağıtılır. IV. Bilgi alma hakkı esas sözleşmeyle kaldırılabilir.',
        {
            'A': 'II ve III',
            'B': 'II ve IV',
            'C': 'I, II ve IV',
            'D': 'I ve III',
            'E': 'Yalnız II',
        },
        'B',
        'II YANLIŞ: TTK md. 376 uyarınca sermaye kaybında şirket kendiliğinden sona ermez; yönetim kurulu genel kurulu toplar. IV YANLIŞ: md. 437 uyarınca bilgi alma hakkı esas sözleşmeyle kaldırılamaz. I (md. 355) ve III (md. 509) doğrudur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0021': patch(
        'Bir anonim şirkette kurucular, nakden taahhüt edilen payların tamamını tescilden sonraki beş yıl içinde ödemeyi kararlaştırmıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sermaye kanunda öngörülen asgari tutardan az olamaz',
            'B': 'Nakden taahhüt edilen payların tamamı tescilden sonra dilenen bir sürede ödenebilir',
            'C': 'Kalan bölüm kanunda öngörülen süre içinde ödenir',
            'D': 'Ayni sermaye taahhütleri tescille birlikte şirkete geçer',
            'E': 'Nakden taahhüt edilen payların kanunda belirtilen bölümünün tescilden önce ödenmesi gerekir',
        },
        'B',
        'TTK md. 344: nakden taahhüt edilen payların itibarî değerinin kanunda belirtilen oranı TESCİLDEN ÖNCE, kalanı ise kanunda öngörülen süre içinde ödenir. Ödeme takvimi taraflarca serbestçe uzatılamaz. md. 332 asgari sermayeyi, md. 128 ayni sermayenin geçişini düzenler.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0022': patch(
        'Anonim şirket ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Sermayesi belirli ve paylara bölünmüştür. II. Borçlarından yalnızca malvarlığıyla sorumludur. III. Pay sahipleri şirket borçlarından kişisel olarak sorumludur.',
        {
            'A': 'I ve III',
            'B': 'I, II ve III',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'I ve II',
        },
        'E',
        'I ve II doğrudur (TTK md. 329). III YANLIŞTIR: pay sahipleri yalnızca taahhüt ettikleri sermaye payları ile ve şirkete karşı sorumludur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0023': patch(
        "Bir anonim şirket sermaye artırımına gitmiş; mevcut pay sahiplerinden biri yeni paylardan öncelikle alma hakkını kullanmak istemektedir.\n\nTTK'ya göre rüçhan hakkıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Pay sahibi yeni payları mevcut payı oranında alma hakkına sahiptir',
            'B': 'Rüçhan hakkı haklı sebeplerin varlığında sınırlandırılabilir',
            'C': 'Sınırlama genel kurulun nitelikli çoğunluk kararıyla yapılır',
            'D': 'Haklı sebep varsa rüçhan hakkı kaldırılabilir',
            'E': 'Rüçhan hakkı yönetim kurulu kararıyla sebepsiz kaldırılabilir',
        },
        'E',
        'TTK md. 461: her pay sahibi yeni çıkarılan payları mevcut paylarının sermayeye oranına göre alma hakkını haizdir. Rüçhan hakkı ancak haklı sebeplerin varlığında ve genel kurulun nitelikli çoğunlukla alacağı kararla sınırlandırılabilir ya da kaldırılabilir; sebepsiz kaldırılamaz.',
    ),
    # düzey 3
    '0024': patch(
        'Halka açık olmayan bir anonim şirkette sermayenin onda birini oluşturan pay sahipleri, genel kurulun toplantıya çağrılmasını istemektedir. Yönetim kurulu talebi reddetmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Çağrı hakkı sermayenin çoğunluğunu temsil edenlere tanınmıştır',
            'B': 'Talep reddedilirse başvurulacak bir yol bulunmaz',
            'C': 'Genel kurulu yönetim kurulu toplantıya çağırır; azınlık pay sahiplerine böyle bir hak tanınmamıştır',
            'D': 'Azınlık çağrı isteyebilir; reddedilirse mahkemeye başvurabilir',
            'E': 'Azınlık doğrudan genel kurulu toplayabilir',
        },
        'D',
        'TTK md. 411: sermayenin en az onda birini (halka açık şirketlerde yirmide birini) oluşturan pay sahipleri, yönetim kurulundan genel kurulu toplantıya çağırmasını isteyebilir. md. 412: talep yönetim kurulunca reddedilir veya yedi iş günü içinde olumlu yanıt verilmezse, MAHKEMEDEN çağrı izni istenebilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0025': patch(
        'Bir anonim şirkette yönetim kurulunun görev ve yetkileri belirlenmektedir. Buna göre aşağıdakilerden hangisi yönetim kurulunun devredilemez görevlerinden biri değildir?',
        {
            'A': 'Muhasebe, finansal denetim ve finansal planlama düzeninin kurulması',
            'B': 'Müdürlerin ve aynı işleve sahip kişilerin atanması ve görevden alınması',
            'C': 'Yıllık finansal tabloların onaylanması ve kâr payının belirlenmesi',
            'D': 'Şirketin üst düzey yönetimi ve yönetim talimatlarının verilmesi',
            'E': 'Borca batıklık durumunun mahkemeye bildirilmesi',
        },
        'C',
        'TTK md. 375: üst düzey yönetim, muhasebe ve finansal denetim düzeninin kurulması, müdürlerin atanması ve borca batıklık bildirimi yönetim kurulunun devredilemez görevlerindendir. FİNANSAL TABLOLARIN ONAYLANMASI ve KÂR PAYININ belirlenmesi md. 408 uyarınca GENEL KURULA aittir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0026': patch(
        'Bir anonim şirket sermayesini azaltmak istemektedir. Alacaklıların durumu tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Anonim şirkette esas sermaye azaltılamaz',
            'B': 'Sermaye azaltımında alacaklılara çağrı yapılır ve alacaklarının teminat altına alınması istenebilir',
            'C': 'Sermaye azaltımı alacaklıları ilgilendirmez',
            'D': 'Sermaye azaltımı ancak mahkeme kararıyla yapılabilir',
            'E': 'Sermaye azaltımı yönetim kurulu kararıyla yapılır; alacaklılara çağrı yapılması ve ilan edilmesi gerekmez',
        },
        'B',
        'TTK md. 473-474: esas sermayenin azaltılmasına genel kurul karar verir; alacaklılara ilan yoluyla çağrı yapılarak alacaklarını bildirmeleri ve TEMİNAT verilmesini istemeleri imkânı tanınır. Azaltım, alacaklıların korunmasına ilişkin bu usul tamamlanmadan tescil edilemez.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0027': patch(
        'Bir anonim şirketin aktiflerinin borçlarını karşılayamadığı bir ara bilançodan anlaşılmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Şirket başka bir işleme gerek olmadan sona erer',
            'B': 'Bildirim ancak alacaklılar talep ederse yapılır',
            'C': 'Bildirim yükümlülüğü genel kurula aittir',
            'D': 'Yönetim kurulu durumu mahkemeye bildirir',
            'E': 'Aktiflerin borçları karşılamadığı anlaşılsa dahi mahkemeye ya da başka bir mercie bildirim yapılması gerekmez',
        },
        'D',
        'TTK md. 376/3: şirketin borca batık olduğu şüphesini uyandıran işaretler varsa yönetim kurulu ara bilanço düzenler; aktiflerin borçları karşılamadığı anlaşılırsa durumu MAHKEMEYE bildirir. md. 375/1-f bu bildirimi yönetim kurulunun devredilemez görevi sayar.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0028': patch(
        'Bir anonim şirket sona ermiş ve tasfiye süreci başlamıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sona erme kararıyla şirketin tüzel kişiliği derhâl ortadan kalkar',
            'B': 'Tasfiye hâlindeki şirket tüzel kişiliğini korur',
            'C': 'Sona eren şirket tasfiye hâline girer',
            'D': 'Tasfiyenin tamamlanmasıyla sicilden terkin edilir',
            'E': "Şirketin ticaret unvanına 'tasfiye hâlinde' ibaresinin eklenmesi gerekir",
        },
        'A',
        "TTK md. 533: sona eren şirket tasfiye hâline girer ve tüzel kişiliğini TASFİYE SONUNA KADAR korur; unvanına 'tasfiye hâlinde' ibaresi eklenir. Tüzel kişilik ancak tasfiye tamamlanıp sicilden terkinle sona erer.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0029': patch(
        'Anonim şirkette organların yetki dağılımı incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Genel kurul, devredilemez yetkilerini esas sözleşmeyle yönetim kuruluna bırakabilir',
            'B': 'Esas sözleşme değişikliği genel kurulun devredilemez yetkisidir',
            'C': 'Yönetim kurulu üyelerinin seçimi genel kurula aittir',
            'D': 'Şirketin üst düzey yönetimi, yönetim kurulunun devredilemez görevlerinden biridir',
            'E': 'Borca batıklık bildirimi yönetim kuruluna aittir',
        },
        'A',
        'TTK md. 408: genel kurulun devredilemez görev ve yetkileri kanunla belirlenmiştir ve esas sözleşmeyle başka bir organa BIRAKILAMAZ.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0030': patch(
        'Anonim şirkette genel kurul kararlarına karşı başvuru yolları incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kanuna aykırı kararlar aleyhine iptal davası açılabilir',
            'B': 'Toplantıda muhalefetini tutanağa geçirten pay sahibi dava açabilir',
            'C': 'Genel kurul kararları kesin olup yargı denetimine tabi tutulamaz',
            'D': 'Butlan hâlleri ayrıca düzenlenmiştir',
            'E': 'Dava süresi karar tarihinden itibaren üç aydır',
        },
        'C',
        "TTK md. 445-447: genel kurul kararları iptal davasına konu edilebilir; batıl kararlar ayrıca md. 447'de düzenlenmiştir. Kararlar yargı denetimine tabidir.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0031': patch(
        'Anonim şirkette kâr dağıtımı ve yedek akçeler incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kâr payı net dönem kârından ve serbest yedek akçelerden dağıtılır',
            'B': 'Kanuni yedek akçeler ayrılmadıkça kâr payı dağıtılamaz',
            'C': 'Sermayeden kâr dağıtılamaz',
            'D': 'Kâr dağıtımına genel kurul karar verir',
            'E': 'Kanuni yedek akçeler kâr payı dağıtıldıktan sonra ayrılır',
        },
        'E',
        'TTK md. 519 ve 523: kanun ve esas sözleşmede öngörülen YEDEK AKÇELER AYRILMADIKÇA kâr payı dağıtılamaz; yedekler dağıtımdan ÖNCE ayrılır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0032': patch(
        'Anonim şirketin sona ermesi ve tasfiyesi incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Şirketin tüzel kişiliği tasfiye sonuna kadar korunur',
            'B': 'Tasfiye hâlindeki şirketi genel kurul temsil eder',
            'C': 'Tasfiye sonunda sicilden terkin edilir',
            'D': 'Sona eren şirket tasfiye hâline girer',
            'E': 'Tasfiye memurları şirketi temsil eder',
        },
        'B',
        'TTK md. 536 vd.: tasfiye hâlindeki şirketi TASFİYE MEMURLARI temsil eder; genel kurul varlığını sürdürse de temsil yetkisi tasfiye memurlarındadır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0033': patch(
        'Bir yatırımcı, borçlarından yalnızca malvarlığıyla sorumlu olan ve sermayesi paylara bölünmüş şirket türünü aramaktadır. Buna göre bu şirket türü aşağıdakilerden hangisidir?',
        {
            'A': 'Adi şirket',
            'B': 'Anonim şirket',
            'C': 'Adi komandit şirket',
            'D': 'Komandit şirket',
            'E': 'Kollektif şirket',
        },
        'B',
        'TTK md. 329: anonim şirket, sermayesi belirli ve paylara bölünmüş olan, borçlarından dolayı yalnız malvarlığıyla sorumlu bulunan şirkettir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0034': patch(
        'Anonim şirkette esas sözleşmenin değiştirilmesi yetkisi hangi organa aittir?',
        {
            'A': 'Genel kurul',
            'B': 'Denetim komitesi',
            'C': 'Tasfiye memurları',
            'D': 'Müdürler kurulu',
            'E': 'Yönetim kurulu',
        },
        'A',
        'TTK md. 408: esas sözleşmenin değiştirilmesi GENEL KURULUN devredilemez görev ve yetkilerindendir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0035': patch(
        "Bir anonim şirkette pay sahibi, taahhüt ettiği sermaye payını ödememiştir.\n\nTTK'ya göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Pay sahibi başka bir işleme gerek olmadan ortaklıktan çıkar',
            'B': 'Süresinde ödemeyen pay sahibi temerrüt faizi öder',
            'C': 'Şirket pay sahibini haklarından yoksun bırakabilir',
            'D': 'Şirket payı iptal edebilir',
            'E': 'Ödenmeyen borç diğer pay sahiplerine yüklenmez',
        },
        'A',
        'TTK md. 482-483: sermaye borcunu süresinde ödemeyen pay sahibi temerrüt faizi ödemekle yükümlüdür; şirket ayrıca kanunda öngörülen usulle pay sahibini haklarından yoksun bırakabilir ve payını iptal edebilir (ıskat). Ortaklıktan çıkma kendiliğinden gerçekleşmez.',
    ),
    # düzey 1
    '0036': patch(
        'Bir anonim şirkette yönetim kurulu üyelerinin sorumluluğu incelenmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yönetim kurulu üyelerinin şirkete, pay sahiplerine ve şirket alacaklılarına karşı herhangi bir sorumluluğu bulunmaz',
            'B': 'Sorumluluk kusursuz sorumluluk esasına dayanır',
            'C': 'Sorumluluk ancak genel kurul kararıyla doğar',
            'D': 'Üyeler yükümlülüklerini kusurlarıyla ihlal ederlerse sorumlu olur',
            'E': 'Sorumluluk pay sahibi olan üyelere özgüdür',
        },
        'D',
        'TTK md. 553: yönetim kurulu üyeleri, kanundan ve esas sözleşmeden doğan yükümlülüklerini KUSURLARIYLA ihlal ettikleri takdirde şirkete, pay sahiplerine ve alacaklılara karşı verdikleri zarardan sorumludur. Sorumluluk KUSUR esasına dayanır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0037': patch(
        'Bir anonim şirkette belirli olayların aydınlatılması için atanan denetçi aşağıdakilerden hangisidir?',
        {
            'A': 'Kayyım',
            'B': 'İşlem denetçisi',
            'C': 'Özel denetçi',
            'D': 'Tasfiye memuru',
            'E': 'Bağımsız denetçi',
        },
        'C',
        'TTK md. 438-439: pay sahipleri, belirli olayların açıklığa kavuşturulması için ÖZEL DENETİM isteyebilir; genel kurul reddederse mahkemeden ÖZEL DENETÇİ atanması istenebilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0038': patch(
        'Anonim şirket organları ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Zorunlu organlar genel kurul ve yönetim kuruludur. II. Yönetim kurulu üyesinin pay sahibi olması şarttır. III. Esas sözleşme değişikliği genel kurulun devredilemez yetkisidir. IV. Genel kurul devredilemez yetkilerini yönetim kuruluna bırakabilir.',
        {
            'A': 'I, II ve IV',
            'B': 'Yalnız II',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'II ve IV',
        },
        'E',
        "II YANLIŞ: TTK md. 359 uyarınca üyenin pay sahibi olması şart değildir. IV YANLIŞ: md. 408'deki devredilemez yetkiler esas sözleşmeyle dahi devredilemez. I ve III doğrudur.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0039': patch(
        'Pay ve pay senetleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Hamiline yazılı pay senetleri zilyetliğin devriyle devredilir. II. Nama yazılı payların devri esas sözleşmeyle sınırlandırılabilir. III. Bilgi alma hakkı genel kurul kararıyla kaldırılabilir.',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'I ve III',
            'D': 'I, II ve III',
            'E': 'Yalnız I',
        },
        'A',
        'I doğrudur (TTK md. 489). II doğrudur (md. 492-493). III YANLIŞTIR: md. 437 uyarınca bilgi alma hakkı esas sözleşmeyle veya organ kararıyla kaldırılamaz.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0040': patch(
        'Bir anonim şirkette pay sahibi, genel kurulda yönetim kurulundan şirketin ticari sırlarını da içeren ayrıntılı bilgi istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bilgi alma hakkı bulunmadığından talep dikkate alınmaz',
            'B': 'Pay sahibinin her bilgi talebi eksiksiz olarak karşılanır',
            'C': 'Bilgi ancak genel kurul kararıyla verilebilir',
            'D': 'Şirket sırları tehlikeye düşecekse reddedilebilir; red hâlinde mahkemeye gidilir',
            'E': 'Bilgi talebi yönetim kurulunun takdirine bağlı olup bu takdir yargısal denetime tabi değildir',
        },
        'D',
        'TTK md. 437: bilgi verilmesi, şirket sırlarının açıklanmasına veya korunması gereken diğer şirket menfaatlerinin tehlikeye girmesine yol açacaksa REDDEDİLEBİLİR. Red hâlinde pay sahibi MAHKEMEYE başvurabilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0041': patch(
        'Bir anonim şirket, esas sermaye sistemi yerine kayıtlı sermaye sistemini benimsemek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yönetim kurulu tavan içinde sermaye artırımına karar verebilir',
            'B': 'Kayıtlı sermaye sistemi limited şirketlere özgüdür',
            'C': 'Kayıtlı sermaye sisteminde tavan öngörülmez',
            'D': 'Kayıtlı sermaye sistemi halka açık şirketlere kapalıdır',
            'E': 'Kayıtlı sermaye sisteminde de her bir sermaye artırımı için ayrıca genel kurul kararı alınması gerekir',
        },
        'A',
        'TTK md. 332 ve 460: kayıtlı sermaye sisteminde esas sözleşmeyle belirlenen TAVAN içinde kalmak ve kanuni koşullara uymak kaydıyla YÖNETİM KURULU sermaye artırımına karar verebilir. Esas sermaye sisteminde ise her artırım genel kurul kararını gerektirir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0042': patch(
        'Bir anonim şirkette bir pay sahibi nama yazılı pay senetlerini, bir diğeri hamiline yazılı pay senetlerini devretmek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Her ikisi de noter onaylı sözleşmeyle devredilir',
            'B': 'Nama yazılı ciro ve teslimle, hamiline yazılı teslimle devredilir',
            'C': 'Pay senetleri, esas sözleşmede aksi yazılsa dahi devredilemez',
            'D': 'Nama yazılı pay senetleri teslimle, hamiline yazılı pay senetleri ise ciro ve teslimle devredilir',
            'E': 'Her ikisi de ciro aranmaksızın zilyetliğin devriyle devredilir',
        },
        'B',
        'TTK md. 489-490: HAMİLİNE yazılı pay senetleri zilyetliğin geçirilmesiyle devredilir; devir, payı devralanın Merkezi Kayıt Kuruluşuna yapacağı bildirimle şirkete ve üçüncü kişilere karşı hüküm ifade eder. NAMA yazılı pay senetleri ise ciro edilmiş nama yazılı pay senedinin zilyetliğinin geçirilmesiyle devredilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0043': patch(
        'Bir anonim şirkette pay sahibinin hakları sınıflandırılmaktadır. Buna göre aşağıdakilerden hangisi pay sahibinin haklarından biri değildir?',
        {
            'A': 'Genel kurul toplantısına katılma ve oy kullanma hakkı',
            'B': 'Şirketin günlük yönetimine doğrudan katılma ve talimat verme hakkı',
            'C': 'Tasfiye payı alma hakkı',
            'D': 'Kâr payı alma hakkı',
            'E': 'Bilgi alma ve inceleme hakkı',
        },
        'B',
        'TTK md. 407, 437, 507 vd.: pay sahibinin başlıca hakları kâr payı, genel kurula katılma ve oy, bilgi alma ve inceleme, tasfiye payı ile rüçhan hakkıdır. Şirketin YÖNETİMİ md. 365 uyarınca YÖNETİM KURULUNA aittir; pay sahibi doğrudan talimat veremez.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0044': patch(
        'Bir anonim şirket genel kurulunda alınan bir karar, kanuna ve dürüstlük kuralına aykırı bulunmuştur. Bir pay sahibi karara karşı ne yapabileceğini araştırmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Genel kurul kararlarına karşı dava açılamaz',
            'B': 'İptal davasını pay sahibi değil yönetim kurulu açabilir',
            'C': 'Dava süresi bir yıl olup muhalefet şerhi aranmaz',
            'D': 'Kanuna aykırı genel kurul kararı yeni bir genel kurul kararıyla kaldırılır; dava yolu kapalıdır',
            'E': 'Muhalefetini tutanağa geçirten pay sahibi üç ay içinde iptal davası açabilir',
        },
        'E',
        'TTK md. 445-446: kanuna, esas sözleşmeye ya da dürüstlük kuralına aykırı genel kurul kararları aleyhine, toplantıda hazır bulunup KARARA MUHALİF KALARAK muhalefetini tutanağa geçirten pay sahipleri ile yönetim kurulu, karar tarihinden itibaren ÜÇ AY içinde iptal davası açabilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0045': patch(
        'Bir anonim şirkette son yıllık bilançoya göre sermaye ile kanuni yedek akçeler toplamının yarısının karşılıksız kaldığı anlaşılmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yönetim kurulu doğrudan iflas bildiriminde bulunur',
            'B': 'Şirket başka bir işleme gerek olmadan sona erer',
            'C': 'Yönetim kurulu genel kurulu derhâl toplantıya çağırır ve iyileştirici önlemleri sunar',
            'D': 'Sermaye kaybı hâlinde herhangi bir yükümlülük doğmaz',
            'E': 'Sermaye kaybı durumu izleyen yılın olağan genel kurul toplantısında görüşülür',
        },
        'C',
        "TTK md. 376/1: son yıllık bilançodan sermaye ile kanuni yedek akçeler toplamının yarısının zarar sebebiyle karşılıksız kaldığı anlaşılırsa, yönetim kurulu genel kurulu HEMEN toplantıya çağırır ve uygun gördüğü iyileştirici önlemleri sunar. Borca batıklık hâli ise md. 376/3'te ayrıca düzenlenmiştir.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0046': patch(
        'Bir anonim şirkette kâr payı dağıtımı incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kâr payı pay sahibinin haklarındandır',
            'B': 'Kâr payı, şirket zarar etmiş olsa dahi sermayeden karşılanarak dağıtılabilir',
            'C': 'Kâr payı dağıtımına genel kurul karar verir',
            'D': 'Kanuni yedek akçeler ayrılmadıkça kâr payı dağıtılamaz',
            'E': 'Kâr payı ancak net dönem kârından ve serbest yedek akçelerden dağıtılabilir',
        },
        'B',
        'TTK md. 509: kâr payı ancak NET DÖNEM KÂRINDAN ve serbest yedek akçelerden dağıtılabilir. Sermayeden kâr dağıtımı sermayenin korunması ilkesine aykırıdır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0047': patch(
        "Bir anonim şirkette azınlık pay sahipleri, şirketin belirli olaylarının aydınlatılması için özel denetçi atanmasını istemektedir. Genel kurul talebi reddetmiştir.\n\nTTK'ya göre özel denetimle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Pay sahibi özel denetim isteminde bulunabilir',
            'B': 'İstem önce genel kurula yöneltilir',
            'C': 'Özel denetçiyi yönetim kurulu atar',
            'D': 'Genel kurul reddederse azınlık mahkemeye başvurabilir',
            'E': 'Özel denetçi mahkemece atanabilir',
        },
        'C',
        'TTK md. 438-439: her pay sahibi, belirli olayların özel bir denetimle açıklığa kavuşturulmasını genel kuruldan isteyebilir. Talep reddedilirse, sermayenin kanunda öngörülen oranını temsil eden pay sahipleri mahkemeden özel denetçi atanmasını isteyebilir; yönetim kurulunun atama yetkisi yoktur.',
    ),
    # düzey 2
    '0048': patch(
        'Bir yatırımcı anonim şirketin temel özelliklerini incelemektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Anonim şirketin borçlarından pay sahipleri de kişisel malvarlıklarıyla sorumludur',
            'B': 'Anonim şirket bir sermaye şirketidir',
            'C': 'Anonim şirketin sermayesi belirli ve paylara bölünmüştür',
            'D': 'Anonim şirket borçlarından kendi malvarlığıyla sorumludur',
            'E': 'Pay sahipleri taahhüt ettikleri sermaye payı ile şirkete karşı sorumludur',
        },
        'A',
        'TTK md. 329: anonim şirket borçlarından dolayı YALNIZ MALVARLIĞIYLA sorumludur; pay sahipleri yalnızca taahhüt ettikleri sermaye payları ile ve ŞİRKETE karşı sorumludur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0049': patch(
        'Anonim şirkette pay devri incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Nama yazılı payların devri esas sözleşmeyle sınırlandırılabilir',
            'B': 'Hamiline yazılı pay senetleri zilyetliğin devriyle devredilir',
            'C': 'Nama yazılı pay senetleri, ciro edilerek ve zilyetliğin devriyle devredilir',
            'D': 'Devrin sınırlandırılmasında keyfî red mümkün değildir',
            'E': 'Hamiline yazılı pay senetleri ancak noter onaylı sözleşmeyle devredilir',
        },
        'E',
        'TTK md. 489: HAMİLİNE yazılı pay senetleri zilyetliğin geçirilmesiyle devredilir; devir, devralanın Merkezi Kayıt Kuruluşuna bildirimiyle şirkete ve üçüncü kişilere karşı hüküm ifade eder. Noter onaylı sözleşme aranmaz.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0050': patch(
        'Anonim şirkette yönetim kurulu üyeliği incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Üyeler genel kurulca seçilir',
            'B': 'Tüzel kişi adına bir gerçek kişi tescil ve ilan edilir',
            'C': 'Yönetim kurulu bir veya daha fazla kişiden oluşur',
            'D': 'Tüzel kişiler yönetim kuruluna üye seçilebilir',
            'E': 'Yönetim kurulu üyesinin pay sahibi olması zorunludur',
        },
        'E',
        'TTK md. 359: yönetim kurulu üyelerinin PAY SAHİBİ OLMASI ŞART DEĞİLDİR; tüzel kişiler de üye seçilebilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0051': patch(
        'Anonim şirkette azınlık hakları incelenmektedir. Buna göre aşağıdakilerden hangisi azınlık haklarından biri değildir?',
        {
            'A': 'Özel denetçi atanmasını isteme',
            'B': 'Haklı sebeple fesih davası açma',
            'C': 'Genel kurulun toplantıya çağrılmasını isteme hakkı',
            'D': 'Yönetim kuruluna doğrudan talimat verme hakkı',
            'E': 'Gündeme madde eklenmesini isteme',
        },
        'D',
        'TTK md. 411, 412, 438-439 ve 531: azınlık hakları genel kurulun toplantıya çağrılması, gündeme madde eklenmesi, özel denetçi atanması ve haklı sebeple fesih davasıdır. Şirketin YÖNETİMİ md. 365 uyarınca yönetim kuruluna aittir; pay sahipleri doğrudan talimat veremez.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0052': patch(
        'Yönetim kurulu üyesinin şirketle ilişkileri incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yasaklar kanundan doğar',
            'B': 'Şirketle işlem yapma ve rekabet yasakları genel kurulun izniyle aşılabilir',
            'C': 'Yönetim kurulu üyesi şirketle kendi adına izinsiz işlem yapabilir',
            'D': 'Şirketle işlem yapma yasağı vardır',
            'E': 'Rekabet yasağı vardır',
        },
        'C',
        'TTK md. 395-396: yönetim kurulu üyesi GENEL KURULUN İZNİ olmaksızın şirketle kendisi veya başkası adına işlem yapamaz.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0053': patch(
        'Anonim şirketin zorunlu organları aşağıdakilerden hangisinde birlikte ve doğru verilmiştir?',
        {
            'A': 'Genel kurul, yönetim kurulu ve denetçi',
            'B': 'Yönetim kurulu ve denetim komitesi',
            'C': 'Genel kurul ve müdürler kurulu',
            'D': 'Yönetim kurulu',
            'E': 'Genel kurul ve yönetim kurulu',
        },
        'E',
        'TTK md. 359 ve 407 vd.: anonim şirketin zorunlu organları GENEL KURUL ve YÖNETİM KURULUDUR; denetçi 6102 sayılı TTK ile organ olmaktan çıkarılmıştır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0054': patch(
        'Bir anonim şirkette borca batıklık durumunun mahkemeye bildirilmesi görevi hangi organa aittir?',
        {
            'A': 'Denetçi',
            'B': 'Genel kurul',
            'C': 'Pay sahipleri',
            'D': 'Yönetim kurulu',
            'E': 'Tasfiye memurları',
        },
        'D',
        'TTK md. 375/1-f ve 376/3: borca batıklık durumunun mahkemeye bildirilmesi YÖNETİM KURULUNUN devredilemez görevlerindendir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0055': patch(
        'Bir anonim şirkette genel kurul toplantısına çağrı yapılmamış ancak tüm pay sahipleri hazır bulunmuştur. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Çağrısız toplantı ancak mahkeme izniyle yapılabilir',
            'B': 'Çağrısız toplantı tek pay sahipli şirketlere özgüdür',
            'C': 'Çağrısız toplantıda bilgilendirme yapılabilir, bağlayıcı karar alınamaz',
            'D': 'Çağrı usulüne uyulmadan genel kurul toplanamaz ve karar alamaz',
            'E': 'Pay sahiplerinin tamamı hazırsa ve itiraz olmazsa çağrısız genel kurul yapılabilir',
        },
        'E',
        'TTK md. 416: bütün payların sahipleri veya temsilcileri, aralarından biri itirazda bulunmadığı takdirde genel kurula ÇAĞRI USULÜNE UYULMAKSIZIN katılabilir ve gündeme dâhil konularda karar alabilir (çağrısız genel kurul).',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0056': patch(
        'Bir anonim şirkette genel kurulun toplantıya çağrılmasını isteme hakkı incelenmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Genel kurulu yönetim kurulu çağırır, azınlık çağrı isteyemez',
            'B': 'Sermayenin kanunda öngörülen oranını temsil eden azınlık bu talebi yöneltebilir',
            'C': 'Talebi sermayenin çoğunluğu yöneltebilir',
            'D': 'Her pay sahibi tek başına çağrı yapabilir',
            'E': 'Genel kurulu toplantıya çağırma talebi hakkı halka açık şirketlere özgüdür',
        },
        'B',
        'TTK md. 411: sermayenin en az onda birini (halka açık şirketlerde yirmide birini) oluşturan pay sahipleri, yönetim kurulundan genel kurulu toplantıya çağırmasını isteyebilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0057': patch(
        'Bir anonim şirkette pay sahibinin genel kurul kararına karşı iptal davası açma süresi aşağıdakilerden hangisidir?',
        {
            'A': 'Süre öngörülmemiştir',
            'B': 'Karar tarihinden itibaren altı ay',
            'C': 'Karar tarihinden itibaren bir yıl',
            'D': 'Karar tarihinden itibaren bir ay',
            'E': 'Karar tarihinden itibaren üç ay',
        },
        'E',
        'TTK md. 445: iptal davası, karar tarihinden itibaren ÜÇ AY içinde açılır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0058': patch(
        'Azınlık hakları ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Azınlık genel kurulun toplantıya çağrılmasını isteyebilir. II. Azınlık özel denetçi atanmasını isteyebilir. III. Azınlık yönetim kuruluna doğrudan talimat verebilir. IV. Azınlık haklı sebeple fesih davası açamaz.',
        {
            'A': 'I ve II',
            'B': 'Yalnız III',
            'C': 'I, III ve IV',
            'D': 'III ve IV',
            'E': 'II ve III',
        },
        'D',
        'III YANLIŞ: şirketin yönetimi yönetim kuruluna aittir (TTK md. 365). IV YANLIŞ: md. 531 uyarınca azınlık haklı sebeple fesih davası açabilir. I (md. 411) ve II (md. 438-439) doğrudur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0059': patch(
        'Anonim şirkette sermaye artırımı ve azaltımı ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Kayıtlı sermaye sisteminde yönetim kurulu tavan içinde artırım kararı alabilir. II. Sermaye azaltımında alacaklılara çağrı yapılır. III. Rüçhan hakkı yönetim kurulu kararıyla kaldırılabilir.',
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'II ve III',
            'D': 'I ve III',
            'E': 'I, II ve III',
        },
        'A',
        'I doğrudur (TTK md. 460). II doğrudur (md. 474). III YANLIŞTIR: md. 461 uyarınca rüçhan hakkı ancak haklı sebeple ve genel kurulun nitelikli çoğunluğuyla sınırlandırılabilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0060': patch(
        'Anonim şirkette esas sözleşme ve kanun ilişkisi incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kanunun açıkça izin verdiği hâllerde esas sözleşmeyle farklı düzenleme yapılabilir',
            'B': 'Genel kurulun devredilemez yetkileri esas sözleşmeyle devredilemez',
            'C': 'Esas sözleşme, kanunun emredici hükümlerinden ayrılan düzenlemeler getirebilir',
            'D': 'Esas sözleşme kanunun emredici hükümlerine aykırı olamaz',
            'E': 'Esas sözleşme değişikliği genel kurul kararıyla yapılır',
        },
        'C',
        "TTK md. 340 (emredici hükümler ilkesi): esas sözleşme, TTK'nın anonim şirketlere ilişkin hükümlerinden ancak KANUNDA AÇIKÇA İZİN VERİLMİŞSE sapabilir.",
        '6102 sayili Turk Ticaret Kanunu',
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
