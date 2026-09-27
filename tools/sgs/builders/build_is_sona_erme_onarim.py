#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Is Sozlesmesinin Sona Ermesi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Olay tabanli 60 soru korunarak onarildi: genisletilmis ELEME_ISARETI olcutune gore 91 mutlak ifadeli sik ayni dogruluk degerini koruyacak bicimde yeniden yazildi, sisirilmis celdiriciler sadelestirildi, gerekce tasiyan dogru siklar kisaltildi. 0029'da ikinci yanlis ifade (E) duzeltildi (iki dogru cevap vardi); 0040 0019'un yakin kopyasiydi, yeniden kurgulandi; oncul cevap yigilmasi giderildi. Kor ogrenci %43 -> %25.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 4857 sayili Is Kanunu md. 17-21, 24-26, 29, 32, 53, 59, 75 · 1475 sayili Is Kanunu md. 14 · 7036 sayili Is Mahkemeleri Kanunu md. 3 · 6098 sayili TBK md. 420, 440, 441
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/is_ve_sosyal_guvenlik_hukuku/is_sozlesmesinin_sona_ermesi.json"
STYLE_REF = 'SGS İş Sözleşmesinin Sona Ermesi (2014-2026 gerçek sınav zorluk kalibrasyonu)'
ONEK = "ish-sona-gen-"


def patch(stem, options, answer, solution, ref='4857 sayili Is Kanunu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'A’nın belirli süreli iş sözleşmesi sürenin dolmasıyla, B’nin sözleşmesi tarafların anlaşmasıyla, C’nin sözleşmesi işverenin süreli feshiyle sona ermiştir. D ise yıllık ücretli izne ayrılmıştır. Bu kişiler bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Dışarıdan bir makamın onayı bulunmadıkça dört işlem de iş sözleşmesini sona erdirmez',
            'B': 'A, B ve C bakımından sona erme gerçekleşmiş; D’nin iş sözleşmesi ise izin süresince devam etmiştir',
            'C': 'D’nin izne ayrılması da diğerleri gibi iş sözleşmesini sona erdirir',
            'D': 'A’nın sözleşmesi sona ermiş; anlaşma ve fesih sözleşmeyi sona erdirememiştir',
            'E': 'B ile D’nin sözleşmesi sona ermiş; belirli süre ve fesih sonuç doğurmamıştır',
        },
        'B',
        'Sürenin dolması, tarafların bozma sözleşmesi yapması ve fesih iş sözleşmesini sona erdirebilir. Yıllık ücretli izin ise iş sözleşmesini sona erdirmez; iş görme borcu izin süresince geçici olarak yerine getirilmez.',
        '4857 sayılı İş Kanunu md. 17, 53; 6098 sayılı TBK md. 430',
    ),
    # düzey 2
    '0002': patch(
        'İki yıl kıdemli işçinin belirsiz süreli sözleşmesi süreli feshedilmiş; işveren altı haftalık sürenin yalnız iki haftasını kullandırıp iş ilişkisini sona erdirmiştir. Sözleşmeyle daha uzun bir süre de kararlaştırılmamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bildirim süresi bölünemeyeceğinden altı haftanın tamamına ilişkin ihbar tazminatı gündeme gelir',
            'B': 'İşçi iki yıl kıdemli olduğu için dört haftalık bildirim süresine tabidir',
            'C': 'Süre eksik kullandırıldığında fesih haklı nedenle derhal feshe dönüşür',
            'D': 'Bildirim süresinin kullanılmayan dört haftası için tazminat ödenir; kanuni süre bölünebilir',
            'E': 'İki haftalık kısmın kullandırılması yeterli olduğundan tazminat doğmaz',
        },
        'A',
        'İki yıllık kıdem için bildirim süresi altı haftadır. Bildirim süresi bölünemez; eksik kullandırılması hâlinde tüm bildirim süresi esas alınarak ihbar tazminatı hesaplanır.',
        '4857 sayılı İş Kanunu md. 17',
    ),
    # düzey 2
    '0003': patch(
        'A’nın ücreti sürekli eksik ödenmekte, B işyerinde üçüncü kişilerce cinsel tacize uğradığı hâlde işveren gerekli önlemleri almamakta, C ise daha yüksek ücretli bir iş bulduğu için ayrılmak istemektedir. İşçinin haklı nedenle derhal fesih hakkı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'A ve C haklı nedenle derhal, B ise süreli feshedebilir',
            'B': 'Üç işçi de bildirim süresine uymadan haklı nedenle feshedebilir',
            'C': 'A ve B haklı nedenle derhal feshedebilir; C’nin daha iyi iş bulması tek başına haklı neden değildir',
            'D': 'A ve B ancak kanuni bildirim süresinin ücretini işverene peşin ödedikten sonra ayrılabilir; ücretin eksikliği veya tacize karşı önlem alınmaması derhal fesih doğurmaz',
            'E': 'C haklı nedenle derhal feshedebilir; A ve B süreli feshedebilir',
        },
        'C',
        'Ücretin kanuna veya sözleşmeye uygun ödenmemesi ile işyerindeki cinsel tacize karşı gerekli önlemlerin alınmaması işçiye haklı fesih hakkı verebilir. Daha iyi iş bulmak kişisel bir tercih olup tek başına haklı neden oluşturmaz.',
        '4857 sayılı İş Kanunu md. 24/II',
    ),
    # düzey 3
    '0004': patch(
        'Fesih türleriyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Süreli fesih kural olarak belirsiz süreli sözleşmelerde bildirim süresine bağlıdır.\n\nII. Haklı nedenle derhal fesihte sözleşmenin sona ermesi için karşı tarafın kabulü gerekir.\n\nIII. İkale, işverenin tek taraflı fesih beyanıyla kurulur.',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'II ve III',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'D',
        'Yalnız I doğrudur. Haklı nedenle derhal fesih tek taraflı yenilik doğuran irade beyanıdır ve karşı tarafın kabulünü gerektirmez. İkale ise tek taraflı fesih değil, tarafların karşılıklı sona erdirme anlaşmasıdır.',
        '4857 sayılı İş Kanunu md. 17, 24, 25; 6098 sayılı TBK md. 26',
    ),
    # düzey 2
    '0005': patch(
        'A işverence işletmesel nedenle, B ücretinin ödenmemesi üzerine kendisi tarafından, C muvazzaf askerlik nedeniyle ayrılmış; D ise işverenin güvenini kötüye kullanıp hırsızlık yaptığı için İş Kanunu md. 25/II uyarınca çıkarılmıştır. Hangisi kural olarak kıdem tazminatına hak kazanamaz?',
        {
            'A': 'C',
            'B': 'A ve C',
            'C': 'B',
            'D': 'A',
            'E': 'D',
        },
        'E',
        'İşçinin ahlak ve iyi niyet kurallarına aykırı davranışı nedeniyle md. 25/II uyarınca haklı fesih, kıdem tazminatına hak kazandırmaz. İşverenin işletmesel feshi, işçinin ücret ödenmemesi nedeniyle haklı feshi ve askerlik nedeniyle ayrılma koşulları varsa kıdem tazminatı doğurur.',
        '1475 sayılı İş Kanunu md. 14; 4857 sayılı İş Kanunu md. 24/II, 25/II',
    ),
    # düzey 2
    '0006': patch(
        'Fesih bildirimi 3 Haziranda tebliğ edilen iş güvencesi kapsamındaki işçi işe iade istemektedir. Arabuluculuk görüşmesi anlaşamama son tutanağıyla sona ermiştir. Başvuru sırası ve süreleri bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşçi tebliğden itibaren bir ay içinde arabulucuya; anlaşma olmazsa son tutanaktan itibaren iki hafta içinde iş mahkemesine başvurmalıdır',
            'B': 'İşçi doğrudan mahkemeye başvurmalı; arabuluculuk isteğe bağlıdır',
            'C': 'İşçi fesihten itibaren beş yıl içinde arabulucuya başvurabilir',
            'D': 'Bir aylık hak düşürücü süre arabuluculuk için değil doğrudan iş mahkemesinde açılacak dava için işler; arabulucuya ise mahkeme kararı kesinleştikten sonra başvurulur',
            'E': 'Arabuluculukta anlaşma olmazsa işe iade davası açma hakkı sona erer',
        },
        'A',
        'İşe iade talebiyle fesih bildiriminin tebliğinden itibaren bir ay içinde arabulucuya başvurulur. Anlaşma sağlanamazsa son tutanağın düzenlendiği tarihten itibaren iki hafta içinde iş mahkemesinde dava açılabilir.',
        '4857 sayılı İş Kanunu md. 20; 7036 sayılı İş Mahkemeleri Kanunu md. 3',
    ),
    # düzey 2
    '0007': patch(
        'İşverenin sunduğu ikale önerisini kabul eden işçiye yalnız kanuni kıdem ve ihbar alacakları ödenmiş; işçi daha sonra sona erdirme iradesinin özgür olmadığını ve ek yarar sağlanmadığını ileri sürmüştür. İkalenin geçerliliği incelenirken aşağıdakilerden hangisi önem taşımaz?',
        {
            'A': 'İkale teklifinin hangi taraftan geldiği',
            'B': 'İrade fesadı ve işverenin üstün konumunu kullanıp kullanmadığı',
            'C': 'İşçinin makul yararının bulunup bulunmadığı',
            'D': 'İşverenin tek taraflı haklı fesih nedenine sahip olması',
            'E': 'Sözleşmenin sona ermesi karşılığında işçiye sağlanan kıdem, ihbar ve ek menfaatlerin toplamı ile işçinin bu anlaşmayı kabul etmekte makul yararının bulunması',
        },
        'D',
        'İkale karşılıklı anlaşmadır. Geçerlilikte teklifin kimden geldiği, işçinin makul yararı, iradenin özgür oluşu ve sağlanan menfaatler değerlendirilir. İşverenin tek taraflı haklı fesih nedenine sahip olması her ikale için zorunlu bir geçerlilik şartı değildir.',
        '6098 sayılı TBK md. 26-27; iş hukuku ikale ilkeleri',
    ),
    # düzey 2
    '0008': patch(
        'İşveren, ayrılan işçiye verdiği çalışma belgesinde işin türünü gerçeğe aykırı yazmış; bu nedenle işçi yeni işe alınmamış ve yeni işveren de yanıltıcı bilgi nedeniyle zarara uğramıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Çalışma belgesi işçinin ücretini içerir; işin türü ve süresi yazılamaz',
            'B': 'İşveren gerçeğe aykırı veya zamanında verilmeyen belge nedeniyle zarar gören işçi ve yeni işverene karşı sorumlu olabilir',
            'C': 'Çalışma belgesini işveren değil, işçinin üyesi olduğu sendika düzenler',
            'D': 'Gerçeğe aykırı çalışma belgesi, işverenin yönetim hakkı kapsamında kaldığından zarar doğursa bile eski işverenin işçiye veya yanıltılan yeni işverene karşı sorumluluğuna yol açmaz',
            'E': 'Belge verme yükümlülüğü ancak işçi en az beş yıl çalışmışsa doğar',
        },
        'B',
        'İşten ayrılan işçiye işinin çeşidini ve süresini gösteren belge verilir. Belgenin zamanında verilmemesi veya yanlış bilgi içermesi nedeniyle zarar gören işçi ya da işçiyi işe alan yeni işveren eski işverenden tazminat isteyebilir.',
        '4857 sayılı İş Kanunu md. 28',
    ),
    # düzey 3
    '0009': patch(
        'Tazminatlarla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İhbar tazminatı, bildirim süresine uymayan tarafça karşı tarafa ödenebilir.\n\nII. Kıdem tazminatında kural olarak en az bir yıllık kıdem aranır.\n\nIII. İşe başlatmama tazminatı, geçersiz fesih kararına rağmen süresinde başvuran işçinin işe başlatılmaması hâlinde doğabilir.',
        {
            'A': 'II ve III',
            'B': 'Yalnız III',
            'C': 'I ve II',
            'D': 'I ve III',
            'E': 'I, II ve III',
        },
        'E',
        'Üç ifade de doğrudur. İhbar tazminatının borçlusu bildirim süresine uymayan işçi veya işveren olabilir; kıdem tazminatında bir yıl aranır; işe başlatmama tazminatı ise geçersiz fesih kararının uygulanmamasının sonucudur.',
        '4857 sayılı İş Kanunu md. 17, 21; 1475 sayılı İş Kanunu md. 14',
    ),
    # düzey 2
    '0010': patch(
        'Aşağıdaki olay–sona erme türü eşleştirmelerinden hangisi doğrudur?',
        {
            'A': 'İşçinin işverenin güvenini kötüye kullanması – işverenin haklı nedenle derhal feshi',
            'B': 'Tarafların karşılıklı ve birbirine uygun irade açıklamalarıyla sözleşmeyi sona erdirmesi – işverenin tek taraflı süreli feshi',
            'C': 'Belirli sürenin dolması – işçinin haklı nedenle derhal feshi',
            'D': 'Ekonomik daralma – sözleşmenin işçinin ölümüyle sona ermesi',
            'E': 'İşverenin ücreti ödememesi – işverenin süreli feshi',
        },
        'A',
        'İşçinin güveni kötüye kullanması doğruluk ve bağlılığa aykırı davranıştır ve işverene haklı nedenle derhal fesih hakkı verebilir. Diğer seçeneklerde olay ile sona erme türü birbirine uymamaktadır.',
        '4857 sayılı İş Kanunu md. 25/II',
    ),
    # düzey 3
    '0011': patch(
        'İş sözleşmesinin sona ermesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Belirli süreli sözleşme, aksi kararlaştırılmadıkça sürenin sonunda kendiliğinden sona erer.\n\nII. İşçinin ölümü hâlinde sözleşme mirasçılarla devam eder.\n\nIII. İkale, tarafların karşılıklı ve birbirine uygun irade açıklamalarını gerektirir.',
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'E',
        'I ve III doğrudur. Belirli süreli sözleşme kural olarak sürenin dolmasıyla sona erer; ikale karşılıklı anlaşmadır. İşçinin ölümü sözleşmeyi kendiliğinden sona erdirdiğinden mirasçılarla devam etmez.',
        '6098 sayılı TBK md. 430, 440',
    ),
    # düzey 2
    '0012': patch(
        'İşyerinde bir haftadan uzun süre işin durmasını gerektiren zorlayıcı sebep ortaya çıkmıştır. İşçi bu nedenle sözleşmesini feshetmek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Zorlayıcı sebepte işçi kıdemi ne olursa olsun kıdem tazminatı alamaz',
            'B': 'İşin bir haftadan fazla durmasını gerektiren zorlayıcı sebep işçiye haklı fesih hakkı verir; ilk hafta yarım ücret ödenir',
            'C': 'Zorlayıcı neden işverene derhal fesih hakkı verir; işçi işin yeniden başlamasını beklemelidir',
            'D': 'Zorlayıcı sebep sözleşmeyi fesih beyanı gerekmeksizin sona erdirir',
            'E': 'İşçi feshedebilmek için işin en az altı ay durmuş olmasını beklemelidir',
        },
        'B',
        'İşçinin çalıştığı işyerinde bir haftadan fazla süreyle işin durmasını gerektiren zorlayıcı neden, işçiye haklı fesih hakkı verir. Zorlayıcı sebeple çalışılmayan ilk bir hafta için yarım ücret ödenir. Kıdem koşulları varsa işçinin haklı feshi kıdem tazminatı doğurur.',
        '4857 sayılı İş Kanunu md. 24/III, 40; 1475 sayılı İş Kanunu md. 14',
    ),
    # düzey 2
    '0013': patch(
        'İşveren A’yı düşük performans, B’yi işletmesel küçülme, C’yi ise hırsızlık nedeniyle çıkarmak istemektedir. Fesihte savunma alma yükümlülüğü bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'A’nın performansa dayalı feshinden önce savunması alınır; B’nin işletmesel feshinde aranmaz, C yönünden md. 25/II hakkı saklıdır',
            'B': 'Savunma alınması işletmesel fesihte aranır, davranışa dayalı fesihte aranmaz',
            'C': 'Üç işçinin de savunması alınmadan yapılan fesih geçerlidir',
            'D': 'Savunma sözlü alınır; yazılı savunma geçersizdir',
            'E': 'İşçinin savunmasının alınması, işverenin fesih nedenini yazılı bildirimde açık ve kesin biçimde gösterme yükümlülüğünü kaldırır; savunma tutanağı tek başına fesih bildirimi yerine geçer',
        },
        'A',
        'Davranış veya verime dayalı geçerli fesihte işçinin savunması alınmalıdır. İşletme, işyeri veya işin gereklerine dayalı fesihte savunma koşulu aranmaz. Md. 25/II kapsamındaki haklı derhal fesih hakkı ayrıca saklıdır.',
        '4857 sayılı İş Kanunu md. 19, 25/II',
    ),
    # düzey 2
    '0014': patch(
        'Bir yıllık belirli süreli iş sözleşmesi 31 Aralıkta sona erecektir. Taraflar sözleşmeyi yenilememiş ve sözleşmede ayrıca bildirim koşulu kararlaştırmamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşveren sekiz haftalık bildirim yapmadıkça sözleşme sonsuza kadar uzar',
            'B': 'Belirli süreli sözleşme süresi dolsa bile ancak haklı nedenle fesihle sona erebilir',
            'C': 'Süre dolduğu için işçinin doğmuş ücret ve izin alacakları da ortadan kalkar',
            'D': 'Sözleşme kural olarak 31 Aralıkta fesih beyanı gerekmeksizin sona erer; bildirim süreleri uygulanmaz',
            'E': 'Sürenin dolması ancak işçi kabul ederse sonuç doğurur',
        },
        'D',
        'Belirli süreli sözleşme, aksi kararlaştırılmadıkça sürenin bitiminde kendiliğinden sona erer. İş Kanunu md. 17’deki bildirim süreleri belirsiz süreli sözleşmeler içindir. Sona erme doğmuş işçilik alacaklarını ortadan kaldırmaz.',
        '6098 sayılı TBK md. 430; 4857 sayılı İş Kanunu md. 17',
    ),
    # düzey 3
    '0015': patch(
        'İşveren, işçinin hamileliği nedeniyle sözleşmesini feshetmiş; fesih bildiriminde gerekçeyi işletmesel küçülme olarak göstermiştir. Yargılamada başka bir neden ileri sürmek istemektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Fesih nedeni yazılı bildirimde açık ve kesin biçimde gösterilmelidir',
            'B': 'Hamilelik geçerli fesih nedeni oluşturmaz',
            'C': 'İşveren yargılamada bildirimde göstermediği yeni nedenlerle feshi geçerli kılabilir',
            'D': 'İşverenin yazılı bildirimde işletmesel neden göstermesi yeterlidir; küçülme kararının gerçekliği, tutarlı uygulanıp uygulanmadığı ve görünürdeki nedenin hamileliği gizleyip gizlemediği yargısal denetime tabi değildir',
            'E': 'Geçerli fesih nedenini ispat yükü kural olarak işverene aittir',
        },
        'C',
        'İşveren fesih bildiriminde gösterdiği nedenle bağlıdır; sonradan sınırsız biçimde yeni neden ileri sürerek feshi geçerli kılamaz. Hamilelik geçerli neden değildir; işletmesel nedenin gerçekliği ve tutarlılığı denetlenir.',
        '4857 sayılı İş Kanunu md. 18-20',
    ),
    # düzey 2
    '0016': patch(
        'İşveren iş güvencesi kapsamındaki işçinin sözleşmesini performans düşüklüğü nedeniyle feshetmiş; işçi ise gerçek nedenin sendikal faaliyet olduğunu ileri sürmüştür. İspat yükü bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşveren gösterdiği geçerli nedeni; işçi ise feshin başka nedene dayandığı iddiasını ispatlar',
            'B': 'Feshin geçerli nedene dayandığını işçi ispatlar',
            'C': 'İşçi sendikal neden iddiasında bulunduğu anda işverenin performans düşüklüğüne ilişkin gösterdiği neden ve deliller inceleme dışı kalır; fesih başka araştırma yapılmadan geçersiz sayılır',
            'D': 'İşveren delil sunmasa da performans gerekçesi doğru kabul edilir',
            'E': 'İspat yükü arabulucuya aittir; tarafların delil sunması yasaktır',
        },
        'A',
        'Feshin geçerli bir nedene dayandığını ispat yükü işverene aittir. İşçi feshin işverenin gösterdiği nedenden başka bir nedene dayandığını iddia ederse bu iddiasını ispatla yükümlüdür. Sendikal güvencelere ilişkin özel ispat kuralları da saklıdır.',
        '4857 sayılı İş Kanunu md. 20; 6356 sayılı Kanun md. 25',
    ),
    # düzey 2
    '0017': patch(
        'İşçinin performansı belgeli biçimde düşmüş ancak davranış haklı fesih ağırlığına ulaşmamıştır. İşveren sözleşmeyi bildirim süresine uyarak feshetmiştir. Geçerli fesih ile haklı derhal fesih ayrımı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Haklı fesih işçiye, geçerli fesih işverene özgüdür',
            'B': 'Geçerli fesih belirli süreli, haklı fesih belirsiz süreli sözleşmeye özgüdür',
            'C': 'Geçerli neden süreli feshe; ilişkiyi çekilmez kılan haklı neden ise bildirim süresiz derhal feshe dayanak olur',
            'D': 'Belgelenen her performans düşüklüğü, ağırlığına ve iş ilişkisinin sürdürülüp sürdürülemeyeceğine bakılmadan md. 25/II kapsamında değerlendirilir ve işveren kıdem ile ihbar tazminatı ödemeden derhal fesheder',
            'E': 'Geçerli ve haklı neden aynı kavramdır; iki fesihte de bildirim süresi uygulanmaz',
        },
        'C',
        'Geçerli neden, iş güvencesi kapsamında süreli feshi haklılaştıran fakat md. 24-25 ağırlığına ulaşmayan nedendir. Haklı neden ise sözleşmenin sürdürülmesini çekilmez kılar ve bildirim süresi beklenmeden derhal feshe imkân verir.',
        '4857 sayılı İş Kanunu md. 17, 18, 24, 25',
    ),
    # düzey 2
    '0018': patch(
        'İşçinin sözleşmesi sona erdiğinde 18 günlük kullanılmamış yıllık izni bulunmaktadır. İşveren, fesih nedeninin işçinin md. 25/II kapsamındaki davranışı olduğunu ileri sürerek izin ücretini ödememiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Md. 25/II feshi kullanılmamış izin ücretini de ortadan kaldırır',
            'B': 'Sona erme nedeni ne olursa olsun kullanılmayan izin ücreti sona erme tarihindeki ücret üzerinden işçiye veya hak sahiplerine ödenir',
            'C': 'İzin ücreti ancak işçi emeklilik nedeniyle ayrılırsa ödenir',
            'D': 'Kullanılmayan yıllık izin süreleri iş sözleşmesi sona erdikten sonra yeni işveren yanında aynen izin olarak kullandırılır; eski işverenin bu süreleri ücrete çevirme veya ödeme yükümlülüğü yoktur',
            'E': 'İzin alacağı ancak sözleşme devam ederken nakden ödenebilir',
        },
        'B',
        'İş sözleşmesinin herhangi bir nedenle sona ermesi hâlinde işçinin hak kazanıp kullanmadığı yıllık izin sürelerine ait ücret, sona erme tarihindeki ücret üzerinden kendisine veya hak sahiplerine ödenir. Md. 25/II feshi bu doğmuş hakkı ortadan kaldırmaz.',
        '4857 sayılı İş Kanunu md. 59',
    ),
    # düzey 2
    '0019': patch(
        'İşveren işçinin ücretini üç aydır ödememiştir. İki yıl kıdemli işçi bu nedenle sözleşmesini derhal feshetmiştir. Tazminatlar bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sözleşmeyi işçi feshettiği için ücret alacağı dâhil bütün haklarını kaybeder',
            'B': 'Haklı fesih nedeniyle kıdem tazminatı kanunen iki kat ödenir',
            'C': 'İşçi kıdem tazminatı alamaz ve altı haftalık ihbar tazminatını işverene öder',
            'D': 'Ücretin ödenmemesi haklı fesih nedenidir; bir yıllık kıdemi bulunan işçi kıdem tazminatı isteyebilir',
            'E': 'Ücretin ödenmemesi haklı fesih hakkı vermez; işçi bildirim süresini çalışmalıdır',
        },
        'D',
        'Ücretin kanun veya sözleşme koşullarına uygun hesaplanmaması ya da ödenmemesi işçiye haklı nedenle derhal fesih hakkı verir. En az bir yıllık kıdemi bulunan işçi kıdem tazminatı isteyebilir; haklı derhal fesihte ihbar süresi uygulanmaz.',
        '4857 sayılı İş Kanunu md. 24/II-(e); 1475 sayılı İş Kanunu md. 14',
    ),
    # düzey 3
    '0020': patch(
        'İş sözleşmesinin sona ermesi bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İşe iade isteyen işçi fesih bildiriminin tebliğinden itibaren bir ay içinde arabulucuya başvurur',
            'B': 'Kıdem tazminatı için kural olarak aynı işverene bağlı en az bir yıllık çalışma aranır',
            'C': 'İşçinin ölümüyle sözleşme sona erer ve koşulları varsa yakınlara TBK md. 440 ödemesi yapılır',
            'D': 'İşçi kendi hırsızlığı nedeniyle md. 25/II uyarınca çıkarılsa bile kıdem tazminatına hak kazanır',
            'E': 'Ahlak ve iyi niyet nedenindeki altı iş günlük süre olayın öğrenildiği günden başlar',
        },
        'D',
        'İşçinin hırsızlık gibi ahlak ve iyi niyet kurallarına aykırı davranışı nedeniyle md. 25/II uyarınca haklı fesih, kıdem tazminatına hak kazandırmaz. Diğer ifadeler doğrudur.',
        '4857 sayılı İş Kanunu md. 20, 25/II, 26; 1475 sayılı İş Kanunu md. 14; 6098 sayılı TBK md. 440',
    ),
    # düzey 2
    '0021': patch(
        'Belirsiz süreli iş sözleşmesiyle çalışan A’nın sözleşmesi, haklı neden bulunmaksızın kanuni bildirim süresi sonunda sona erecek biçimde feshedilmiştir. Bu işlemin hukuki niteliği aşağıdakilerden hangisidir?',
        {
            'A': 'Haklı nedenle derhal fesih; işverenin geçerli neden göstermesiyle sözleşme bildirim süresi sonunda değil, beyanın ulaştığı anda sona erer',
            'B': 'Belirli sürenin dolması; tarafların ayrıca fesih beyanı açıklamasına gerek yoktur',
            'C': 'İkale; işçinin kabulü olmadan hukuki sonuç doğurmaz',
            'D': 'Geçersiz fesih; belirsiz süreli sözleşme süreli feshedilemez',
            'E': 'Süreli fesih; fesih beyanı karşı tarafa ulaştıktan sonra bildirim süresinin sonunda sözleşme sona erer',
        },
        'E',
        'Belirsiz süreli iş sözleşmesinin kanuni bildirim süresine uyularak tek taraflı irade beyanıyla sona erdirilmesi süreli fesihtir. Haklı neden bulunmadığı için derhal fesih; karşılıklı anlaşma bulunmadığı için ikale değildir.',
        '4857 sayılı İş Kanunu md. 17',
    ),
    # düzey 2
    '0022': patch(
        'Üç yıl dört ay kıdemli A haklı neden olmadan bildirimsiz istifa etmiş; iki yıl kıdemli B ise işverence haklı neden olmadan ve bildirim süresi verilmeden çıkarılmıştır. İhbar tazminatı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Haklı neden bulunmaması iki feshi de geçersiz kılar; ihbar tazminatı istenemez',
            'B': 'İhbar tazminatı işverene özgü bir borç olduğundan A yönünden talep doğmaz',
            'C': 'A işverene sekiz haftalık, işveren B’ye altı haftalık ihbar tazminatı öder',
            'D': 'A ile B’nin kıdemleri farklı olsa da ikisi için aynı bildirim süresi uygulanır',
            'E': 'A’nın istifası bildirim süresine bağlı olmadığından tazminatı B öder',
        },
        'C',
        'Bildirim sürelerine uymayan taraf işçi veya işveren olabilir. Üç yıldan fazla kıdemli A için sekiz, bir buçuk ile üç yıl kıdemli B için altı haftalık süre uygulanır. Haklı neden bulunmayan bildirimsiz fesih ihbar tazminatına yol açabilir.',
        '4857 sayılı İş Kanunu md. 17',
    ),
    # düzey 2
    '0023': patch(
        'İşçi A izin almadan ardı ardına iki iş günü işe gelmemiş, B işverenin ticari sırrını rakibe açıklamış, C ise kanuni yıllık iznini kullanmıştır. İşverenin haklı nedenle derhal fesih hakkı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'A ve B’nin davranışları haklı feshe dayanak olabilir; C’nin kanuni iznini kullanması olamaz',
            'B': 'B’nin ticari sırrı rakibe açıklaması geçerli fesih nedenidir, haklı fesih ağırlığına ulaşmaz',
            'C': 'A’nın devamsızlığı ancak üç ay sürerse haklı fesih nedeni olur',
            'D': 'C’nin davranışı haklı fesih nedenidir; A ve B’ninki değildir',
            'E': 'İşveren üç davranışta da işçiye önce sekiz haftalık bildirim süresi vermelidir',
        },
        'A',
        'İzinsiz ve haklı nedensiz ardı ardına iki iş günü devamsızlık ile güveni kötüye kullanma veya meslek sırrını açıklama, İş Kanunu md. 25/II kapsamındaki haklı fesih nedenlerindendir. Kanuni yıllık iznin kullanılması haklı fesih nedeni değildir.',
        '4857 sayılı İş Kanunu md. 25/II-(e), (g)',
    ),
    # düzey 2
    '0024': patch(
        'İşçi aynı işverene ait A işyerinde sekiz ay, ardından kesintisiz biçimde B işyerinde yedi ay çalışmış ve işveren tarafından kıdem tazminatına hak kazandıran nedenle çıkarılmıştır. Asgari kıdem koşulu bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kıdem tazminatı için süre koşulu bulunmadığından ilk çalışma günü yeterlidir',
            'B': 'Aynı işverene ait işyerlerindeki süreler birlikte değerlendirilir; toplam on beş ay bir yıllık koşulu karşılar',
            'C': 'Süreler ancak işyerleri aynı adreste ise birleştirilebilir',
            'D': 'Bir yıllık koşul yerine her işyerinde en az altı ay çalışma aranır',
            'E': 'Her işyerindeki çalışma ayrı bir sözleşmeye dayandığı için süreler birleştirilemez; sekiz ve yedi aylık dönemlerin hiçbiri tek başına bir yılı doldurmadığından kıdem hakkı doğmaz',
        },
        'B',
        'Kıdem hesabında aynı işverenin bir veya değişik işyerlerinde geçen hizmet süreleri birlikte değerlendirilir. Toplam on beş aylık çalışma, bir yıllık asgari kıdem koşulunu karşılar.',
        '1475 sayılı İş Kanunu md. 14',
    ),
    # düzey 3
    '0025': patch(
        'A, aynı işkolundaki işyerlerinde toplam kırk işçi çalıştıran işverenin bir işyerinde belirsiz süreli sözleşmeyle yedi aydır çalışmaktadır. B, kırk işçili yer altı işyerinde belirsiz süreli sözleşmeyle üç aydır çalışmaktadır. Her ikisi de işletmenin bütününü yöneten ve işe alma-çıkarma yetkisi bulunan işveren vekili değildir. İş güvencesi bakımından hangisi doğrudur?',
        {
            'A': 'B altı aylık kıdemi bulunmadığından yer altı işinde de kapsam dışıdır',
            'B': 'A sayı ve kıdem koşulunu karşılar; B yer altında çalıştığından kıdem aranmaz',
            'C': 'İş güvencesi belirli süreli çalışanlara uygulanır',
            'D': 'A işyerinde tek başına otuz işçi bulunmadığı varsayımıyla kapsam dışıdır; aynı işkolundaki diğer işyerleri sayılmaz',
            'E': 'A ve B’nin kapsamı için işçi sayısı ile kıdem aranmaz',
        },
        'B',
        'Otuz işçi hesabında işverenin aynı işkolundaki işyerlerinde çalışan toplam işçi sayısı dikkate alınır. Kural olarak en az altı aylık kıdem aranır; yer altı işlerinde çalışan işçilerde bu kıdem şartı aranmaz. Diğer kapsam koşulları da ayrıca bulunmalıdır.',
        '4857 sayılı İş Kanunu md. 18',
    ),
    # düzey 2
    '0026': patch(
        'İş güvencesi kapsamındaki A’nın sözleşmesi düşük performans, B’ninki ekonomik daralma, C’ninki sendika üyeliği nedeniyle feshedilmiştir. Geçerli neden bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yeterlilikten veya işletme gereklerinden kaynaklanan nedenler somut ve ölçülü ise geçerli olabilir; sendika üyeliği geçerli neden olamaz',
            'B': 'Geçerli fesih ancak işçinin ahlak ve iyi niyet kurallarına aykırı davranışında mümkündür',
            'C': 'İşverenin geçerli neden gösterme yükümlülüğü belirli süreli sözleşmelere özgüdür',
            'D': 'Üç neden de işverenin yönetim hakkı kapsamında geçerli sayılır',
            'E': 'İşçinin sendikaya üye olması işverenin yönetim hakkı kapsamında geçerli fesih nedeni oluşturur; buna karşılık ekonomik daralma ve belgeli performans düşüklüğü feshe dayanak olamaz',
        },
        'A',
        'İşçinin yeterliliği veya davranışları ile işletmenin, işyerinin ya da işin gerekleri geçerli neden oluşturabilir. Sendika üyeliği veya sendikal faaliyete katılma ise açıkça geçerli neden oluşturmaz.',
        '4857 sayılı İş Kanunu md. 18',
    ),
    # düzey 3
    '0027': patch(
        'İşe iade kararı sonrasında aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İşçi kesinleşen kararın tebliğinden itibaren on iş günü içinde işverene başvurmalıdır.\n\nII. İşveren başvuran işçiyi altı ay içinde işe başlatabilir.\n\nIII. İşçi süresinde başvurmazsa işverence yapılan fesih geçerli sayılır.',
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'Yalnız I',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'E',
        'I ve III doğrudur. İşveren, süresinde başvuran işçiyi bir ay içinde işe başlatmalıdır; altı aylık süre yoktur. İşçi on iş günü içinde başvurmazsa işverence yapılmış fesih geçerli sayılır.',
        '4857 sayılı İş Kanunu md. 21',
    ),
    # düzey 2
    '0028': patch(
        'Kadın işçi evlendiği tarihten on bir ay sonra, aynı işverene bağlı iki yıllık kıdemi varken evlilik nedeniyle sözleşmesini feshetmiştir. Bildirim süresine de uymamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Evlilik işverene fesih hakkı verir; işçinin feshi istifa sayılır',
            'B': 'Kıdem tazminatı için evlilikten sonra en az beş yıl daha çalışılması ve bu sürenin sonunda işverenin yazılı onayıyla ayrılınması gerekir',
            'C': 'Evlilik nedeniyle ayrılmada kıdem tazminatı erkek işçiye ödenir',
            'D': 'Bir yıl içinde evlilik nedeniyle fesih ve kıdem koşulları gerçekleştiğinden işçi kıdem tazminatı alabilir; bildirim süresi aranmaz',
            'E': 'İşçi kıdem tazminatı alamaz ve sekiz haftalık ihbar tazminatı öder',
        },
        'D',
        'Kadın işçinin evlendiği tarihten itibaren bir yıl içinde kendi isteğiyle sözleşmesini sona erdirmesi kıdem tazminatına hak kazandırır; en az bir yıllık kıdem de olayda vardır. Bu özel fesihte ihbar süresi uygulanmaz.',
        '1475 sayılı İş Kanunu md. 14',
    ),
    # düzey 2
    '0029': patch(
        'İşveren, 120 işçi çalıştırdığı işyerinde ekonomik nedenle bir ay içinde 15 işçiyi çıkarmayı planlamakta ve fesihleri aynı gün uygulamak istemektedir. Toplu işçi çıkarma bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': '120 işçili işyerinde sayı eşiği otuz işçidir',
            'B': 'Toplu çıkarma hükümleri ekonomik veya teknolojik nedenlerle yapılan fesihlere uygulanmaz',
            'C': '101-300 işçili işyerinde en az %10 çıkarma toplu çıkarmadır; otuz gün önce bildirilir',
            'D': 'Bildirim fesihlerden sonra yapılır ve fesihler bildirimden bağımsız aynı gün hüküm doğurur',
            'E': 'Toplu çıkarma ancak 300’den fazla işçi bulunan işyerlerinde söz konusu olur',
        },
        'C',
        '101-300 işçi çalıştırılan işyerinde bir ay içinde en az %10 oranında işçinin çıkarılması toplu işçi çıkarmadır. İşveren bunu en az otuz gün önce işyeri sendika temsilcilerine, ilgili bölge müdürlüğüne ve İŞKUR’a bildirir.',
        '4857 sayılı İş Kanunu md. 29',
    ),
    # düzey 2
    '0030': patch(
        'Erkek işçi üç yıllık kıdemi varken muvazzaf askerlik hizmeti nedeniyle sözleşmesini feshetmiştir. İşveren, feshi işçinin yaptığını ileri sürerek tazminat ödemeyi reddetmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Askerlik ücretsiz izin nedenidir; sözleşme feshedilemez',
            'B': 'Muvazzaf askerlik nedeniyle ayrılma kıdem tazminatına hak kazandırır; bu özel fesihte işçi ihbar süresine bağlı değildir',
            'C': 'Askerlik nedeniyle kıdem tazminatı bir yıldan az kıdemi olan işçiye ödenir',
            'D': 'İşçi kendi feshettiğinden hem kıdem hem ihbar tazminatı alır',
            'E': 'Muvazzaf askerlik nedeniyle ayrılan işçinin kıdem tazminatı isteyebilmesi için askerlik dönüşünde aynı işveren yanında yeniden işe girip kesintisiz beş yıl daha çalışması gerekir',
        },
        'B',
        'Muvazzaf askerlik hizmeti nedeniyle iş sözleşmesinin sona erdirilmesi, en az bir yıllık kıdem varsa kıdem tazminatına hak kazandırır. Bu özel sona ermede işçi bildirim süresine bağlı değildir ve ihbar tazminatı doğmaz.',
        '1475 sayılı İş Kanunu md. 14',
    ),
    # düzey 2
    '0031': patch(
        'İşveren, iki yıl kıdemli ve iş güvencesi kapsamındaki işçinin sözleşmesini işletmesel nedenle feshetmiş; altı haftalık bildirim süresine ait ücreti peşin ödeyip işçiyi hemen işten ayırmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Peşin ödeme ancak işçinin yazılı kabulüyle mümkündür',
            'B': 'Bildirim süresi ücretinin peşin ödenmesiyle işçinin o tarihe kadar doğmuş kıdem tazminatı ve kullanılmayan yıllık izin ücreti alacakları sona erer; ayrıca ödeme yapılmaz',
            'C': 'Bildirim ücreti peşin ödendiğinden işçi işe iade talep edemez',
            'D': 'İşveren bildirim ücretini peşin ödeyebilir; iş güvencesi koşulları yine uygulanır',
            'E': 'Peşin ödeme feshi haklı nedenle derhal feshe dönüştürür ve geçerli neden incelemesini kaldırır',
        },
        'D',
        'İşveren bildirim süresine ait ücreti peşin vererek sözleşmeyi sona erdirebilir. Bu yöntem iş güvencesi hükümlerini bertaraf etmez; fesih geçerli nedene ve usule uygun olmalıdır. Kıdem ve izin gibi diğer haklar ayrıca değerlendirilir.',
        '4857 sayılı İş Kanunu md. 17-19',
    ),
    # düzey 3
    '0032': patch(
        'Kıdem tazminatına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İşçinin ücretinin ödenmemesi nedeniyle haklı feshi kıdem tazminatına hak kazandırabilir.\n\nII. İşçinin md. 25/II kapsamındaki hırsızlığı nedeniyle işverence çıkarılması kıdem tazminatına hak kazandırır.\n\nIII. Muvazzaf askerlik nedeniyle ayrılma kıdem tazminatına hak kazandırabilir.',
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'B',
        'I ve III doğrudur. Ücret ödenmemesi işçinin haklı fesih nedeni olabilir; askerlik özel kıdem tazminatı nedenidir. İşçinin hırsızlık gibi md. 25/II davranışı nedeniyle çıkarılması kıdem tazminatı doğurmaz.',
        '1475 sayılı İş Kanunu md. 14; 4857 sayılı İş Kanunu md. 24/II, 25/II',
    ),
    # düzey 2
    '0033': patch(
        'İşçi bir ay içinde izin almaksızın pazartesi ve salı ardı ardına işe gelmemiş; aynı ay iki ayrı hafta tatilinden sonraki iş gününde de devamsızlık yapmıştır. Devamsızlıkların haklı sebebi bulunmamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Haklı fesih için devamsızlığın kesintisiz otuz gün sürmesi gerekir',
            'B': 'Tatil gününden sonraki iş günü yapılan devamsızlık feshe dayanak olabilir; ardı ardına iki iş günü eşik değildir',
            'C': 'Her iki devamsızlık biçimi de kanundaki eşiklerden birini karşılayabilir ve işverene haklı fesih hakkı verebilir',
            'D': 'Devamsızlık haklı fesih nedeni olmaz; ücret kesintisi yapılabilir',
            'E': 'İşveren devamsızlığı öğrendikten sonra bir yıllık bildirim süresi vermelidir',
        },
        'C',
        'İzinsiz veya haklı nedensiz ardı ardına iki iş günü devamsızlık ile bir ay içinde iki kez tatil gününden sonraki iş günü devamsızlık, kanunda ayrı ayrı haklı fesih eşiğidir. Bir ayda üç iş günü devamsızlık da diğer eşiktir.',
        '4857 sayılı İş Kanunu md. 25/II-(g)',
    ),
    # düzey 2
    '0034': patch(
        'İşçinin yaptığı iş, işin niteliğinden kaynaklanan bir nedenle sağlığı için tehlikeli hâle gelmiş; hekim raporu da tehlikeyi doğrulamıştır. İşveren uygun başka iş önermemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşçi sağlık nedeniyle haklı olarak derhal feshedebilir; en az bir yıllık kıdemi varsa kıdem tazminatı gündeme gelebilir',
            'B': 'Sağlık nedeni işverene fesih hakkı verir, işçiye vermez',
            'C': 'İşçi bildirim süresine uyarak istifa edebilir ve kıdem tazminatı alamaz',
            'D': 'İşçi sözleşmeyi feshedebilmek için tehlikenin en az bir yıl sürmesini beklemelidir',
            'E': 'Hekim raporuyla doğrulanan sağlık tehlikesi işçi yönünden haklı fesih nedeni oluşturmaz',
        },
        'A',
        'İşin yapılması işin niteliğinden doğan nedenle işçinin sağlığı veya yaşayışı için tehlikeli olursa işçi haklı nedenle derhal feshedebilir. En az bir yıllık kıdem dâhil diğer koşullar varsa kıdem tazminatı doğar.',
        '4857 sayılı İş Kanunu md. 24/I; 1475 sayılı İş Kanunu md. 14',
    ),
    # düzey 2
    '0035': patch(
        'İşçi aynı işverene ait üç işyerinde sırasıyla iki yıl, bir yıl ve altı ay çalışmış; işyerleri arasında geçiş yapılırken sözleşmesi kesintiye uğramamıştır. Kıdem hesabı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Son işyerindeki altı aylık süre dikkate alınır',
            'B': 'İşçi hangi işyerindeki sürenin dikkate alınacağını tek taraflı seçer',
            'C': 'Aynı adreste geçen süreler birleştirilebilir, diğerleri birleştirilemez',
            'D': 'Aynı işverenin değişik işyerlerindeki süreler birleştirilir ve toplam üç yıl altı ay üzerinden hesap yapılır',
            'E': 'Her işyeri geçişinde kıdem yeniden başlar; dönemler birbirinden bağımsız hesaplanır',
        },
        'D',
        'Kıdem, işçinin aynı işverenin bir veya değişik işyerlerinde çalıştığı süreler birlikte değerlendirilerek hesaplanır. Olayda toplam kıdem üç yıl altı aydır.',
        '1475 sayılı İş Kanunu md. 14',
    ),
    # düzey 2
    '0036': patch(
        'İşçi işe iade ile birlikte kıdem ve ihbar tazminatı alacaklarını da talep etmek istemektedir. Dava şartı arabuluculuk bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşçi ancak işveren kabul ederse arabulucuya başvurabilir',
            'B': 'İşe iade talebinde arabuluculuk isteğe bağlı, tazminat alacaklarında yasaktır',
            'C': 'Arabuluculuk ceza uyuşmazlıklarında uygulanır',
            'D': 'İşe iade ve işçilik alacağı davalarında arabulucuya başvuru dava şartıdır',
            'E': 'Arabulucuya başvurulmadan açılan davalar doğrudan esastan incelenir',
        },
        'D',
        'İşe iade talebi ile bireysel veya toplu iş sözleşmesine dayanan işçi ya da işveren alacağı ve tazminatı davalarında, kanuni istisnalar dışında arabulucuya başvuru dava şartıdır.',
        '7036 sayılı İş Mahkemeleri Kanunu md. 3; 4857 sayılı İş Kanunu md. 20',
    ),
    # düzey 3
    '0037': patch(
        'İş sözleşmesinin sona ermesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kanuni bildirim süreleri iki ile sekiz hafta arasında kıdeme göre artar.\n\nII. Kıdem tazminatı hesabında her tam yıl için otuz günlük ücret esası uygulanır.\n\nIII. İş güvencesinde gösterilen geçerli nedeni ispat yükü kural olarak işçiye aittir.',
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'II ve III',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'A',
        'I ve II doğrudur: bildirim süresi kıdeme göre iki, dört, altı ve sekiz haftadır; kıdem tazminatı her tam yıl için otuz günlük ücret esasıyla hesaplanır. III yanlıştır: feshin geçerli bir nedene dayandığını ispat yükü İŞVERENE aittir (İş K. md. 20).',
        '4857 sayılı İş Kanunu md. 17, 20; 1475 sayılı İş Kanunu md. 14',
    ),
    # düzey 2
    '0038': patch(
        'İş sözleşmesi 1 Temmuz 2026’da sona eren işçi kıdem, ihbar ve kullanılmayan yıllık izin ücreti alacaklarını talep etmektedir. Zamanaşımı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşçilik alacakları zamanaşımına tabi değildir',
            'B': 'Bütün işçilik alacaklarında süre yüz yıldır ve taraflarca değiştirilemez',
            'C': 'Bu alacaklarda zamanaşımı kural olarak beş yıldır; muacceliyet ve süreyi etkileyen nedenler ayrıca değerlendirilir',
            'D': 'Zamanaşımı dolunca borç ifa edilmiş sayılır; sonradan yapılan ödeme geri istenebilir',
            'E': 'Kıdem, ihbar ve izin alacağı ceza davasında talep edilir',
        },
        'C',
        'Kıdem ve ihbar tazminatı ile yıllık izin ücreti dâhil kanunda sayılan işçilik alacaklarında zamanaşımı kural olarak beş yıldır. Muacceliyet, geçiş hükümleri ve zamanaşımını kesen veya durduran nedenler ayrıca değerlendirilir.',
        '4857 sayılı İş Kanunu ek md. 3; 7036 sayılı Kanun geçici md. 8',
    ),
    # düzey 2
    '0039': patch(
        'İşveren, aynı nitelikte çalışanlardan yalnız belirli etnik kökene sahip olanların sözleşmesini feshetmiş; işçiler iş güvencesi kapsamı dışında kalmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşçiler işe iade tazminatı isteyebilir, ayrımcılık veya kötüniyet tazminatı isteyemez',
            'B': 'Ayrımcılık ve kötüniyet, iş güvencesi dışındaki işçi için de ayrı sonuç doğurur',
            'C': 'Ayrımcılık yasağı işe alımla sınırlıdır; sona ermede uygulanmaz',
            'D': 'İş güvencesi dışında olmak ayrımcı feshi serbest hâle getirir',
            'E': 'İşveren bildirim süresine uyduysa fesih nedeni denetlenemez',
        },
        'B',
        'Eşit davranma borcu iş ilişkisinin sona ermesinde de uygulanır. Ayrımcı fesih ayrımcılık tazminatı ve diğer hakları; iş güvencesi dışındaki belirsiz süreli çalışanda koşulları varsa kötüniyet tazminatını gündeme getirebilir.',
        '4857 sayılı İş Kanunu md. 5, 17',
    ),
    # düzey 3
    '0040': patch(
        'İş sözleşmesinin sona ermesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Süreli fesihte bildirim süresi işçinin yaşına göre belirlenir.\n\nII. İş güvencesi için kural olarak en az üç yıllık kıdem gerekir.\n\nIII. Kıdem tazminatında her tam yıl için otuz günlük ücret esası uygulanır.',
        {
            'A': 'Yalnız III',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'A',
        'Yalnız III doğrudur. I yanlıştır: bildirim süresi yaşa göre değil, işçinin KIDEMİNE göre (iki, dört, altı, sekiz hafta) belirlenir. II yanlıştır: iş güvencesinde kural olarak altı aylık kıdem aranır; yer altı işlerinde kıdem koşulu da yoktur.',
        '4857 sayılı İş Kanunu md. 17-18; 1475 sayılı İş Kanunu md. 14',
    ),
    # düzey 2
    '0041': patch(
        'A’nın kıdemi beş ay, B’nin bir yıl, C’nin iki yıl, D’nin dört yıldır. Belirsiz süreli sözleşmeleri süreli feshedilecektir. Kanuni bildirim süreleri sırasıyla aşağıdakilerden hangisidir?',
        {
            'A': '2 – 6 – 8 – 10 hafta',
            'B': '2 – 4 – 6 – 8 hafta',
            'C': '4 – 4 – 6 – 8 hafta',
            'D': '4 – 6 – 8 – 10 hafta',
            'E': '2 – 4 – 8 – 12 hafta',
        },
        'B',
        'Bildirim süreleri; altı aydan az kıdemde iki, altı ay ile bir buçuk yıl arasında dört, bir buçuk ile üç yıl arasında altı, üç yıldan fazla kıdemde sekiz haftadır.',
        '4857 sayılı İş Kanunu md. 17',
    ),
    # düzey 2
    '0042': patch(
        'İşveren A’yı işletmesel nedenle bildirim süresi vererek; B’yi hırsızlık yaptığı için; C’yi ise tarafların karşılıklı anlaşmasıyla işten ayırmıştır. Bu sona erme biçimlerinin hukuki nitelikleri sırasıyla aşağıdakilerden hangisidir?',
        {
            'A': 'Süreli fesih – haklı nedenle derhal fesih – ikale',
            'B': 'Süreli fesih – ikale – haklı nedenle derhal fesih',
            'C': 'İkale – süreli fesih – haklı nedenle derhal fesih',
            'D': 'Belirli sürenin dolması – süreli fesih – ikale',
            'E': 'Haklı nedenle derhal fesih – süreli fesih – belirli sürenin dolması',
        },
        'A',
        'İşletmesel geçerli neden, kural olarak süreli feshe; hırsızlık doğruluk ve bağlılığa aykırılık nedeniyle haklı derhal feshe; karşılıklı sona erdirme anlaşması ise ikaleye örnektir.',
        '4857 sayılı İş Kanunu md. 17, 18, 25/II; 6098 sayılı TBK md. 26',
    ),
    # düzey 3
    '0043': patch(
        'İşveren 1 Martta gerçekleşen ve işçiye maddi çıkar sağlamayan hırsızlığı 10 Martta öğrenmiş, fesih bildirimini 19 Martta yapmıştır. Başka bir olayda işçinin davranıştan maddi çıkar sağladığı belirlenmiştir. Ahlak ve iyi niyet kurallarına aykırılığa dayalı fesih süresi bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Altı iş günlük süre olay tarihinden, bir yıllık süre öğrenme tarihinden başlar',
            'B': 'Altı iş günlük süre işçinin feshine özgüdür; işveren öğrenmeden başlayarak bir yıl içinde feshedebilir',
            'C': 'İlk fesih öğrenmeden itibaren bir ay içinde yapıldığı için süresindedir',
            'D': 'Haklı fesih hakkı on yıllık genel zamanaşımı içinde kullanılabilir',
            'E': 'İlk olayda altı iş günlük süre geçmiş; maddi çıkarlı olayda bir yıllık sınır uygulanmaz',
        },
        'E',
        'Ahlak ve iyi niyet kurallarına aykırılıkta fesih hakkı, olayın öğrenilmesinden başlayarak altı iş günü ve kural olarak fiilden itibaren bir yıl içinde kullanılmalıdır. İşçinin olaydan maddi çıkar sağlaması hâlinde bir yıllık üst sınır uygulanmaz. İlk olayda 19 Mart tarihli fesih altı iş günlük süreyi aşmıştır.',
        '4857 sayılı İş Kanunu md. 26',
    ),
    # düzey 2
    '0044': patch(
        'A’nın son çıplak brüt ücreti 30.000 ₺; düzenli yemek ve yol menfaatlerinin aylık karşılığı 6.000 ₺’dir. A, aynı işverene bağlı iki yıl altı ay çalıştıktan sonra kıdem tazminatına hak kazanarak ayrılmıştır. Kanuni tavanın hesabı sınırlamadığı varsayımıyla aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kıdem tazminatı bildirim süresine ait ücretle sınırlı olduğundan altı haftalık ücret ödenir',
            'B': 'Kıdem çıplak ücret ve tam yıllar üzerinden hesaplanır; altı aylık süre dikkate alınmaz',
            'C': 'Düzenli para ile ölçülebilen menfaatler ücrete eklenir ve iki yıl altı aylık kıdem orantılı hesaplanır',
            'D': 'Düzenli menfaatler hesaba katılır ancak bir yıldan artan süreler oranlanmaz',
            'E': 'Hesap son bir yılda ödenen fazla çalışma ücretlerinin ortalaması üzerinden yapılır',
        },
        'C',
        'Kıdem tazminatına esas ücret, düzenli para ve para ile ölçülebilen menfaatleri de kapsayan giydirilmiş ücrettir. Her tam yıl için otuz günlük ücret ödenir; bir yıldan artan süreler de oranlanır. Kanuni tavan ayrıca gözetilir.',
        '1475 sayılı İş Kanunu md. 14',
    ),
    # düzey 2
    '0045': patch(
        'İşçinin aynı işverene bağlı kıdemi dört yıl altı aydır. Kıdem tazminatına hak kazanarak ayrıldığı ve kanuni tavanın hesabı sınırlamadığı varsayılırsa tazminat kaç günlük giydirilmiş ücret tutarındadır?',
        {
            'A': '130 günlük',
            'B': '120 günlük',
            'C': '125 günlük',
            'D': '135 günlük',
            'E': '150 günlük',
        },
        'D',
        'Her tam yıl için otuz günlük ücret ödenir; artan süre orantılanır. Dört yıl 120 gün, altı ay 15 gün olmak üzere toplam 135 günlük giydirilmiş ücret esas alınır.',
        '1475 sayılı İş Kanunu md. 14',
    ),
    # düzey 2
    '0046': patch(
        'Feshin geçersizliğine karar verilmiş, karar kesinleşince işçi on iş günü içinde başvurmuş ancak işveren bir ay içinde işe başlatmamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşçi kıdem tazminatı isteyebilir; işe başlatmama ve boşta geçen süre ödemeleri doğmaz',
            'B': 'İşçi dört ile sekiz aylık ücret tutarında işe başlatmama tazminatı ile en çok dört aya kadar boşta geçen süre ücret ve haklarını isteyebilir',
            'C': 'İşçinin on iş günlük başvurusu geç olduğundan kararın bütün sonuçları ortadan kalkmıştır',
            'D': 'İşverenin işe başlatmaması hâlinde fesih tarihi değişmez ve ek bir ödeme doğmaz',
            'E': 'İşe başlatmama tazminatı işçinin kıdeminden bağımsız olarak sabit on iki aylık ücrettir; boşta geçen süre ücretinde ise kararın kesinleşmesine kadar herhangi bir üst sınır uygulanmaz',
        },
        'B',
        'Süresinde başvuran işçi bir ay içinde işe başlatılmazsa dört ile sekiz aylık ücret tutarında tazminat ödenir. Kararın kesinleşmesine kadar çalıştırılmadığı süre için en çok dört aya kadar ücret ve diğer haklar ayrıca doğar.',
        '4857 sayılı İş Kanunu md. 21',
    ),
    # düzey 2
    '0047': patch(
        'Altı yıldır çalışan işçi vefat etmiş; geride eşi ile ergin olmayan çocuğu kalmıştır. İşçinin ölümü üzerine doğan haklar bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sözleşme sona erer; işverenin ölüm tazminatı veya doğmuş alacaklara ilişkin borcu kalmaz',
            'B': 'Ölüm tazminatı ancak işçinin kıdemi bir yıldan azsa doğar',
            'C': 'Kullanılmayan yıllık izin ücreti ödenir; başka bir ödeme mümkün değildir',
            'D': 'Sözleşme mirasçılarla aynen devam eder; ölüm sona erme nedeni değildir',
            'E': 'Sözleşme sona erer; doğmuş alacaklar yanında eş ve çocuklara iki aylık ücret ödenir',
        },
        'E',
        'İşçinin ölümü iş sözleşmesini kendiliğinden sona erdirir. İşveren, sağ kalan eşe ve ergin olmayan çocuklara; bunlar yoksa bakmakla yükümlü olunan kişilere bir aylık, hizmet beş yıldan uzunsa iki aylık ücret tutarında ödeme yapar. Doğmuş diğer alacaklar da saklıdır.',
        '6098 sayılı TBK md. 440; 4857 sayılı İş Kanunu md. 59',
    ),
    # düzey 2
    '0048': patch(
        'İşçi ile işveren, iş sözleşmesinin sona erdiği gün bütün işçilik alacaklarının ibra edildiğini belirten yazılı belge düzenlemiştir. Belgede alacak tür ve miktarları ayrı ayrı gösterilmemiş, ödeme nakit yapılmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşçilik alacaklarında ibra sözleşmesi yapılamaz',
            'B': 'İbra yazılı biçimde düzenlendiğinde sona erme tarihinden sonra bir ay geçmesi, alacak tür ve miktarlarının ayrı ayrı yazılması ve ödemenin banka aracılığıyla yapılması gerekmez',
            'C': 'Kanuni koşullar bulunmadığından ibra kesin hükümsüzdür',
            'D': 'Nakit ödeme işçinin imzasıyla kanıtlandığı için bütün eksiklikleri giderir',
            'E': 'İbraname noter onayı bulunmadığı için geçersizdir; diğer koşullar aranmaz',
        },
        'C',
        'İşçi alacağına ilişkin ibra; yazılı olmalı, sözleşmenin sona ermesinden başlayarak en az bir ay geçtikten sonra düzenlenmeli, alacağın tür ve miktarını açıkça göstermeli ve ödeme hak tutarına uygun biçimde banka aracılığıyla yapılmalıdır. Koşulları taşımayan ibra kesin hükümsüzdür.',
        '6098 sayılı TBK md. 420',
    ),
    # düzey 2
    '0049': patch(
        'İki yıl kıdemli işçi, işverene yüklenebilecek haklı bir neden bulunmaksızın ve bildirim yapmadan başka bir işe geçmek için ayrılmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşçi kıdem tazminatı alamaz ancak işverenden altı haftalık ihbar tazminatı isteyebilir',
            'B': 'İstifa kıdem tazminatına hak kazandırır; bildirim süresine uyulmaması işveren lehine ihbar alacağı doğurmaz',
            'C': 'İşçinin ayrılması ancak işveren kabul ederse sonuç doğurur',
            'D': 'Haklı nedensiz istifa kıdem tazminatı doğurmaz; altı haftalık bildirim süresine uymayan işçiden işveren ihbar tazminatı isteyebilir',
            'E': 'İşçi her istifada kıdem ve ihbar tazminatına hak kazanır',
        },
        'D',
        'Haklı nedene dayanmayan olağan istifa kıdem tazminatına hak kazandırmaz. İki yıllık kıdem için altı haftalık bildirim süresine uymayan işçiden işveren ihbar tazminatı talep edebilir.',
        '4857 sayılı İş Kanunu md. 17; 1475 sayılı İş Kanunu md. 14',
    ),
    # düzey 3
    '0050': patch(
        'İşveren, iş güvencesi kapsamındaki işçiyi davranışına dayanarak çıkarmış; fesih bildirimini yazılı yapmış ancak işçinin savunmasını almamıştır. Davranış aynı zamanda İş Kanunu md. 25/II ağırlığında değildir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Savunma alınmaması biçimsel bir eksikliktir ve feshin geçerliliğini etkilemez',
            'B': 'Fesih bildirimi yazılı yapılmalı ve neden açık, kesin biçimde belirtilmelidir',
            'C': 'Davranışa dayalı geçerli fesihte kural olarak işçinin savunması alınmalıdır',
            'D': 'İşveren gösterdiği fesih sebebiyle bağlıdır',
            'E': 'Davranış md. 25/II ağırlığında olsaydı işveren savunma almadan derhal feshedebilirdi',
        },
        'A',
        'İşçinin davranışı veya verimiyle ilgili geçerli fesih, savunması alınmadan yapılamaz. Savunma eksikliği feshin geçersizliğine yol açabilir; salt önemsiz bir biçim eksikliği değildir. Md. 25/II kapsamındaki haklı fesih hakkı saklıdır.',
        '4857 sayılı İş Kanunu md. 19',
    ),
    # düzey 2
    '0051': patch(
        'İş güvencesi kapsamı dışında kalan dört yıl kıdemli işçi, işverene karşı ücret davası açtığı için sekiz haftalık bildirim süresi kullandırılarak çıkarılmıştır. Kötüniyet tazminatı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bildirim süresine uyulmuş olması kötüniyetli feshi hukuka uygun kılar',
            'B': 'Kötüniyet tazminatı iş güvencesi kapsamındaki işçinin işe iade davasında istenir',
            'C': 'İşçi, bildirim süresinin üç katı tutarında kötüniyet tazminatı isteyebilir',
            'D': 'Tazminat işçi tarafından işverene ödenir ve bir aylık ücretle sınırlıdır',
            'E': 'İşçinin yasal hakkını araması fesihte kötüniyet değerlendirmesine konu olamaz',
        },
        'C',
        'İş güvencesi hükümleri dışında kalan belirsiz süreli çalışan işçinin fesih hakkı kötüye kullanılarak sözleşmesi sona erdirilirse, bildirim süresinin üç katı tutarında kötüniyet tazminatı doğabilir. Bildirim süresine ayrıca uyulmuş olması kötüniyeti ortadan kaldırmaz.',
        '4857 sayılı İş Kanunu md. 17',
    ),
    # düzey 2
    '0052': patch(
        'İş güvencesi kapsamındaki işçinin sözleşmesi hiçbir neden gösterilmeden feshedilmiş; işçi bir ay içinde arabulucuya başvurmuş ve anlaşma sağlanamamıştır. İşçinin izlemesi gereken yol bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Arabuluculukta anlaşma sağlanamaması işe iade talebini sona erdirir; mahkemeye başvurulamaz',
            'B': 'İşçi kıdem tazminatı isteyebilir; fesih geçerliliği denetlenemez',
            'C': 'İşçi doğrudan idare mahkemesinde iptal davası açmalıdır',
            'D': 'İşe iade davası ancak işverenin yazılı izniyle açılabilir',
            'E': 'İşçi son tutanaktan itibaren iki hafta içinde iş mahkemesinde işe iade davası açabilir',
        },
        'E',
        'İşçi süresinde arabulucuya başvurmuş ve anlaşma sağlanamamıştır. Son tutanağın düzenlendiği tarihten itibaren iki hafta içinde iş mahkemesinde işe iade davası açabilir.',
        '4857 sayılı İş Kanunu md. 20; 7036 sayılı İş Mahkemeleri Kanunu md. 3',
    ),
    # düzey 2
    '0053': patch(
        'İş güvencesi kapsamındaki işçinin sözleşmesi aşağıdaki nedenlerden hangisine dayanılarak geçerli biçimde feshedilemez?',
        {
            'A': 'İşçinin hamileliği ve doğum iznini kullanacak olması',
            'B': 'İşçinin iş akışını ciddi biçimde bozan ancak haklı fesih ağırlığına ulaşmayan davranışı',
            'C': 'Belgelenen ve süreklilik gösteren yetersiz performans',
            'D': 'İşletmenin faaliyet alanını daraltması nedeniyle işgücü fazlası doğması',
            'E': 'İşyerinde teknolojik değişiklik nedeniyle belirli pozisyonun ortadan kalkması',
        },
        'A',
        'Hamilelik, doğum ve kanuni izinlerin kullanılması geçerli fesih nedeni oluşturmaz. İşçinin yeterliliği veya davranışları ile işletmenin, işyerinin veya işin gerekleri somut ve ölçülü koşullarda geçerli neden olabilir.',
        '4857 sayılı İş Kanunu md. 18',
    ),
    # düzey 3
    '0054': patch(
        'İşe iade davası ve sonuçlarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Arabuluculukta anlaşma sağlanamazsa dava son tutanaktan itibaren iki hafta içinde açılır.\n\nII. İşe başlatmama tazminatı en az dört, en çok sekiz aylık ücret tutarındadır.\n\nIII. Boşta geçen süre için işçiye en çok altı aya kadar ücret ve diğer hakları ödenir.',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'II ve III',
        },
        'B',
        'I ve II doğrudur. Arabuluculuk son tutanağından itibaren iki hafta içinde iş mahkemesinde dava açılır; işe başlatmama tazminatı dört ile sekiz aylık ücret tutarındadır. III yanlıştır: boşta geçen süre için ödenecek ücret ve haklar en çok DÖRT ay ile sınırlıdır.',
        '4857 sayılı İş Kanunu md. 21',
    ),
    # düzey 2
    '0055': patch(
        'İki yıl kıdemli işçi işyeri dışındaki bir olay nedeniyle tutuklanmış ve devamsızlığı kıdemine göre uygulanacak bildirim süresini aşmıştır. İşverenin fesih hakkı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşçinin işyeri dışındaki bir olay nedeniyle gözaltına alınması veya tutuklanması, devamsızlığın süresine ve mahkûmiyet bulunup bulunmadığına bakılmadan ilk günden md. 25/II kapsamında değerlendirilir',
            'B': 'Devamsızlık bildirim süresini aşsa da işveren sözleşmeyi feshedemez',
            'C': 'İşveren ancak ceza mahkûmiyeti kesinleştikten beş yıl sonra feshedebilir',
            'D': 'Devamsızlık bildirim süresini aşarsa işveren md. 25/IV uyarınca derhal feshedebilir; koşulları varsa kıdem hakkı saklıdır',
            'E': 'Bu fesihte işçi hem ihbar hem kötüniyet tazminatına hak kazanır',
        },
        'D',
        'İşçinin gözaltına alınması veya tutuklanması nedeniyle devamsızlığının md. 17’deki bildirim süresini aşması işverene md. 25/IV uyarınca derhal fesih hakkı verir. Bu bent md. 25/II değildir; en az bir yıllık kıdem varsa kıdem tazminatı doğabilir, ihbar tazminatı doğmaz.',
        '4857 sayılı İş Kanunu md. 17, 25/IV; 1475 sayılı İş Kanunu md. 14',
    ),
    # düzey 2
    '0056': patch(
        'İşveren satışların azalması üzerine aynı işi yapan on işçiden yalnız A’nın sözleşmesini feshetmiş; fazla çalışma uygulamasını ve yeni işçi alımını sürdürmüş, A’yı başka pozisyonda değerlendirme olanağını araştırmamıştır. A iki yıldır çalışmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Satışların azaldığı ileri sürülünce fesih geçerli olur; seçim ve alternatifler incelenmez',
            'B': 'Kararın gerçekliği, tutarlılığı ve feshin son çare olması denetlenebilir',
            'C': 'İşletmesel fesihte tutarlılık ve son çare ilkesi aranmaz',
            'D': 'İki yıllık kıdemi olan işçi işletmesel fesihte tazminat talep edemez',
            'E': 'İşveren işletmesel nedenle haklı derhal fesih yapar ve bildirim süresi uygulamaz',
        },
        'B',
        'İşletmesel fesihte kararın gerçekliği, tutarlı uygulanması, keyfîlik bulunmaması ve feshin son çare olması denetlenir. Fazla çalışma ile yeni işe alımın sürmesi ve alternatif pozisyonun araştırılmaması geçerliliği etkileyebilir. Kıdem ve ihbar hakları ayrıca değerlendirilir.',
        '4857 sayılı İş Kanunu md. 17-18; geçerli fesihte son çare ilkesi',
    ),
    # düzey 2
    '0057': patch(
        'Gerçek kişi işveren vefat etmiş; işletme mirasçılarca aynı faaliyetle sürdürülmektedir. İş sözleşmesi özellikle işverenin kişiliği dikkate alınarak kurulmamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşverenin ölümü iş sözleşmelerini ve doğmuş alacakları ortadan kaldırır',
            'B': 'Sözleşme ancak işçi yeniden yazılı onay verirse geçmişe etkili devam eder',
            'C': 'İşverenin ölümü işçiye doğmuş ücret ve izin alacaklarını talep etme hakkı vermez',
            'D': 'İşverenin ölümü belirli süreli sözleşmeleri sona erdirir, diğerlerini sürdürür',
            'E': 'İşverenin ölümü kural olarak sözleşmeyi sona erdirmez; ilişki mirasçılarla sürer',
        },
        'E',
        'İşverenin ölümü iş sözleşmesini kural olarak sona erdirmez; miras ve hizmet ilişkisinin devrine ilişkin hükümler uygulanır. Sözleşme ağırlıklı olarak işverenin kişiliği dikkate alınarak kurulmuşsa ölümle sona erebilir.',
        '6098 sayılı TBK md. 441',
    ),
    # düzey 2
    '0058': patch(
        'Aşağıdaki kavram–hukuki sonuç eşleştirmelerinden hangisi doğrudur?',
        {
            'A': 'İhbar tazminatı – işçinin ölümü hâlinde mirasçılara yapılan ödeme',
            'B': 'Kıdem tazminatı – bildirim süresine uymayan tarafın karşı tarafa ödediği tazminat',
            'C': 'Kötüniyet tazminatı – iş güvencesi dışındaki belirsiz süreli çalışanın fesih hakkı kötüye kullanıldığında bildirim süresinin üç katı tutarında isteyebileceği tazminat',
            'D': 'İkale – işverenin işçiye bildirim süresi vermeden açıkladığı, işçinin kabul veya imzasına ihtiyaç bulunmayan ve tek taraflı olarak sözleşmeyi sona erdiren olağan fesih beyanı',
            'E': 'İşe başlatmama tazminatı – her tam kıdem yılı için otuz günlük ücret',
        },
        'C',
        'Kötüniyet tazminatı, iş güvencesi dışında kalan belirsiz süreli çalışanın sözleşmesi fesih hakkı kötüye kullanılarak sona erdirildiğinde bildirim süresinin üç katı tutarında doğabilir. Diğer seçenekler farklı kurumları birbirine karıştırmaktadır.',
        '4857 sayılı İş Kanunu md. 17',
    ),
    # düzey 2
    '0059': patch(
        'Yirmi işçi çalıştıran işyerindeki iki yıl kıdemli işçinin belirsiz süreli sözleşmesi, işveren aleyhine tanıklık yaptığı için altı haftalık bildirim süresine uyularak feshedilmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Otuzdan az işçili işyerinde işveren ancak md. 25/II davranışını ispatlarsa feshedebilir',
            'B': 'İşçi otuz işçi koşulunu taşımadığı hâlde mutlaka işe iade edilir',
            'C': 'İşçi işe iade isteyemese de kötüniyet tazminatı isteyebilir',
            'D': 'İş güvencesi dışında kalan işçiye kıdem tazminatı ödenmez',
            'E': 'Bildirim süresine uyulduğu için fesihte kötüniyet iddiası ileri sürülemez',
        },
        'C',
        'Otuz işçi koşulu bulunmadığından işçi kural olarak işe iade hükümlerinden yararlanamaz. Bununla birlikte fesih hakkının kötüye kullanılması kötüniyet tazminatını; bir yıllık kıdem ve diğer koşullar kıdem tazminatını gündeme getirebilir.',
        '4857 sayılı İş Kanunu md. 17-18; 1475 sayılı İş Kanunu md. 14',
    ),
    # düzey 3
    '0060': patch(
        'Bildirim süreleriyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kanundaki süreler asgari olup sözleşmeyle artırılabilir.\n\nII. Bildirim süresine uymayan taraf karşı tarafa bu sürenin ücreti tutarında tazminat ödeyebilir.\n\nIII. Haklı nedenle derhal fesihte bildirim süresinin dolması beklenmez.',
        {
            'A': 'I ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'E',
        'Üç ifade de doğrudur. Kanundaki bildirim süreleri asgaridir ve artırılabilir; uymayan taraf ihbar tazminatı öder; haklı nedenle derhal fesihte bildirim süresi uygulanmaz.',
        '4857 sayılı İş Kanunu md. 17, 24, 25',
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
    print(f"1 paket / {len(PATCHES)} soru ('Is Sozlesmesinin Sona Ermesi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
