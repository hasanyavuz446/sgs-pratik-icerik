#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""İş Sözleşmesinin Sona Ermesi — 2026 gerçek SGS zorluk kalibrasyonu.

2014-2026 gerçek SGS hukuk soruları ve ÇSGB'nin 2026 güncel mevzuat metinleri
esas alınmıştır. Önceki paket medyan 123 karakterdi; 60 sorunun 40'ı kısa ve tek
bilgi tanımayla çözülebiliyordu. Bu builder paketin tamamını ana kural + istisna,
süre + sonuç, fesih türü + tazminat veya iş güvencesi + başvuru zincirlerinden
en az birini ölçen bağımsız sorulara dönüştürür.

Doğru cevap harfleri korunur. Paket üç ardışık 20 soruluk test olarak sunulduğu
için bilişsel zorluk kapısı her blokta ayrıca doğrulanır.

Dayanak: 4857 sayılı İş Kanunu md. 17-21, 24-26, 29, 32, 53, 59, 75;
1475 sayılı İş Kanunu md. 14; 7036 sayılı İş Mahkemeleri Kanunu md. 3;
6098 sayılı TBK md. 420, 440, 441.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
REL = "content/is_ve_sosyal_guvenlik_hukuku/is_sozlesmesinin_sona_ermesi.json"
STYLE = "SGS İş Sözleşmesinin Sona Ermesi (2014-2026 gerçek sınav zorluk kalibrasyonu)"


def p(stem, options, answer, solution, ref):
    for marker in ("I.", "II.", "III.", "IV.", "V."):
        stem = stem.replace(f" {marker} ", f"\n\n{marker} ")
    return {
        "stem": stem,
        "options": options,
        "answer": answer,
        "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE, "legislationRef": ref},
        "validYear": 2026,
        "mockExamId": None,
    }


Q = {
    "0001": p(
        "A’nın belirli süreli iş sözleşmesi sürenin dolmasıyla, B’nin sözleşmesi tarafların anlaşmasıyla, C’nin sözleşmesi işverenin süreli feshiyle sona ermiştir. D ise yıllık ücretli izne ayrılmıştır. Bu kişiler bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "D’nin izne ayrılması da diğerleri gibi iş sözleşmesini sona erdirir",
            "B": "A, B ve C bakımından sona erme gerçekleşmiş; D’nin iş sözleşmesi ise izin süresince devam etmiştir",
            "C": "Yalnız A’nın sözleşmesi sona ermiş; anlaşma ve fesih sözleşmeyi sona erdirememiştir",
            "D": "Yalnız B ile D’nin sözleşmesi sona ermiş; belirli süre ve fesih sonuç doğurmamıştır",
            "E": "Dışarıdan bir makamın onayı bulunmadıkça dört işlem de iş sözleşmesini sona erdirmez",
        }, "B",
        "Sürenin dolması, tarafların bozma sözleşmesi yapması ve fesih iş sözleşmesini sona erdirebilir. Yıllık ücretli izin ise iş sözleşmesini sona erdirmez; iş görme borcu izin süresince geçici olarak yerine getirilmez.",
        "4857 sayılı İş Kanunu md. 17, 53; 6098 sayılı TBK md. 430",
    ),
    "0002": p(
        "Belirsiz süreli iş sözleşmesiyle çalışan A’nın sözleşmesi, haklı neden bulunmaksızın kanuni bildirim süresi sonunda sona erecek biçimde feshedilmiştir. Bu işlemin hukuki niteliği aşağıdakilerden hangisidir?",
        {
            "A": "Süreli fesih; fesih beyanı karşı tarafa ulaştıktan sonra bildirim süresinin sonunda sözleşme sona erer",
            "B": "Haklı nedenle derhal fesih; bildirim süresi boyunca iş ilişkisi devam etmez",
            "C": "İkale; işçinin kabulü olmadan hukuki sonuç doğurmaz",
            "D": "Belirli sürenin dolması; tarafların ayrıca fesih beyanı açıklamasına gerek yoktur",
            "E": "Geçersiz fesih; belirsiz süreli sözleşme hiçbir koşulda süreli feshedilemez",
        }, "A",
        "Belirsiz süreli iş sözleşmesinin kanuni bildirim süresine uyularak tek taraflı irade beyanıyla sona erdirilmesi süreli fesihtir. Haklı neden bulunmadığı için derhal fesih; karşılıklı anlaşma bulunmadığı için ikale değildir.",
        "4857 sayılı İş Kanunu md. 17",
    ),
    "0003": p(
        "A’nın kıdemi beş ay, B’nin bir yıl, C’nin iki yıl, D’nin dört yıldır. Belirsiz süreli sözleşmeleri süreli feshedilecektir. Kanuni bildirim süreleri sırasıyla aşağıdakilerden hangisidir?",
        {
            "A": "2 – 6 – 8 – 10 hafta",
            "B": "4 – 4 – 6 – 8 hafta",
            "C": "2 – 4 – 6 – 8 hafta",
            "D": "2 – 4 – 8 – 12 hafta",
            "E": "4 – 6 – 8 – 10 hafta",
        }, "C",
        "Bildirim süreleri; altı aydan az kıdemde iki, altı ay ile bir buçuk yıl arasında dört, bir buçuk ile üç yıl arasında altı, üç yıldan fazla kıdemde sekiz haftadır.",
        "4857 sayılı İş Kanunu md. 17",
    ),
    "0004": p(
        "İki yıl kıdemli işçinin belirsiz süreli sözleşmesi süreli feshedilmiş; işveren altı haftalık sürenin yalnız iki haftasını kullandırıp iş ilişkisini sona erdirmiştir. Sözleşmeyle daha uzun bir süre de kararlaştırılmamıştır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "İki haftalık kısmın kullandırılması yeterli olduğundan tazminat doğmaz",
            "B": "İşçi iki yıl kıdemli olduğu için dört haftalık bildirim süresine tabidir",
            "C": "Bildirim süresinin yalnız kullanılmayan dört haftası dikkate alınarak sonuç doğar",
            "D": "Bildirim süresi bölünemeyeceğinden altı haftanın tamamına ilişkin ihbar tazminatı gündeme gelir",
            "E": "Süre eksik kullandırılsa da fesih kendiliğinden haklı nedenle derhal feshe dönüşür",
        }, "D",
        "İki yıllık kıdem için bildirim süresi altı haftadır. Bildirim süresi bölünemez; eksik kullandırılması hâlinde tüm bildirim süresi esas alınarak ihbar tazminatı hesaplanır.",
        "4857 sayılı İş Kanunu md. 17",
    ),
    "0005": p(
        "Üç yıl dört ay kıdemli A haklı neden olmadan bildirimsiz istifa etmiş; iki yıl kıdemli B ise işverence haklı neden olmadan ve bildirim süresi verilmeden çıkarılmıştır. İhbar tazminatı bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "İhbar tazminatı yalnız işverence ödenebildiğinden A yönünden talep doğmaz",
            "B": "A ile B’nin kıdemleri farklı olsa da ikisi için aynı bildirim süresi uygulanır",
            "C": "A’nın istifası bildirim süresine bağlı olmadığından yalnız B tazminat öder",
            "D": "Haklı neden bulunmaması iki feshi de geçersiz kılar; ihbar tazminatı istenemez",
            "E": "A sekiz haftalık süreye ilişkin tazminattan işverene, işveren de B’nin altı haftalık süresine ilişkin tazminattan B’ye karşı sorumlu olabilir",
        }, "E",
        "Bildirim sürelerine uymayan taraf işçi veya işveren olabilir. Üç yıldan fazla kıdemli A için sekiz, bir buçuk ile üç yıl kıdemli B için altı haftalık süre uygulanır. Haklı neden bulunmayan bildirimsiz fesih ihbar tazminatına yol açabilir.",
        "4857 sayılı İş Kanunu md. 17",
    ),
    "0006": p(
        "İşveren A’yı işletmesel nedenle bildirim süresi vererek; B’yi hırsızlık yaptığı için; C’yi ise tarafların karşılıklı anlaşmasıyla işten ayırmıştır. Bu sona erme biçimlerinin hukuki nitelikleri sırasıyla aşağıdakilerden hangisidir?",
        {
            "A": "Süreli fesih – haklı nedenle derhal fesih – ikale",
            "B": "Haklı nedenle derhal fesih – süreli fesih – belirli sürenin dolması",
            "C": "İkale – süreli fesih – haklı nedenle derhal fesih",
            "D": "Süreli fesih – ikale – haklı nedenle derhal fesih",
            "E": "Belirli sürenin dolması – süreli fesih – ikale",
        }, "A",
        "İşletmesel geçerli neden, kural olarak süreli feshe; hırsızlık doğruluk ve bağlılığa aykırılık nedeniyle haklı derhal feshe; karşılıklı sona erdirme anlaşması ise ikaleye örnektir.",
        "4857 sayılı İş Kanunu md. 17, 18, 25/II; 6098 sayılı TBK md. 26",
    ),
    "0007": p(
        "A’nın ücreti sürekli eksik ödenmekte, B işyerinde üçüncü kişilerce cinsel tacize uğradığı hâlde işveren gerekli önlemleri almamakta, C ise daha yüksek ücretli bir iş bulduğu için ayrılmak istemektedir. İşçinin haklı nedenle derhal fesih hakkı bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Yalnız C haklı nedenle derhal feshedebilir",
            "B": "A ve C haklı nedenle, B ise yalnız süreli feshedebilir",
            "C": "Üç işçi de bildirim süresine uymadan haklı nedenle feshedebilir",
            "D": "A ve B haklı nedenle derhal feshedebilir; C’nin daha iyi iş bulması tek başına haklı neden değildir",
            "E": "Üç durumda da işçinin tek seçeneği bildirim süresine uyarak istifa etmektir",
        }, "D",
        "Ücretin kanuna veya sözleşmeye uygun ödenmemesi ile işyerindeki cinsel tacize karşı gerekli önlemlerin alınmaması işçiye haklı fesih hakkı verebilir. Daha iyi iş bulmak kişisel bir tercih olup tek başına haklı neden oluşturmaz.",
        "4857 sayılı İş Kanunu md. 24/II",
    ),
    "0008": p(
        "İşçi A izin almadan ardı ardına iki iş günü işe gelmemiş, B işverenin ticari sırrını rakibe açıklamış, C ise kanuni yıllık iznini kullanmıştır. İşverenin haklı nedenle derhal fesih hakkı bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Yalnız C’nin davranışı haklı fesih nedenidir",
            "B": "A ve B’nin davranışları haklı feshe dayanak olabilir; C’nin kanuni iznini kullanması olamaz",
            "C": "A’nın devamsızlığı yalnız üç ay sürerse haklı fesih nedeni olur",
            "D": "B’nin davranışı geçerli neden olabilir ancak hiçbir zaman haklı neden oluşturmaz",
            "E": "İşveren üç davranışta da işçiye önce sekiz haftalık bildirim süresi vermelidir",
        }, "B",
        "İzinsiz ve haklı nedensiz ardı ardına iki iş günü devamsızlık ile güveni kötüye kullanma veya meslek sırrını açıklama, İş Kanunu md. 25/II kapsamındaki haklı fesih nedenlerindendir. Kanuni yıllık iznin kullanılması haklı fesih nedeni değildir.",
        "4857 sayılı İş Kanunu md. 25/II-(e), (g)",
    ),
    "0009": p(
        "İşveren 1 Martta gerçekleşen ve işçiye maddi çıkar sağlamayan hırsızlığı 10 Martta öğrenmiş, fesih bildirimini 19 Martta yapmıştır. Başka bir olayda işçinin davranıştan maddi çıkar sağladığı belirlenmiştir. Ahlak ve iyi niyet kurallarına aykırılığa dayalı fesih süresi bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "İlk fesih öğrenmeden itibaren bir ay içinde yapıldığı için süresindedir",
            "B": "Altı iş günlük süre olay tarihinden, bir yıllık süre öğrenme tarihinden başlar",
            "C": "Haklı fesih hakkı on yıllık genel zamanaşımı içinde kullanılabilir",
            "D": "Altı iş günlük süre yalnız işçinin fesih hakkına uygulanır; işveren yönünden süre yoktur",
            "E": "İlk olayda öğrenmeden başlayan altı iş günlük süre geçirilmiştir; maddi çıkar sağlanan olayda ise kanundaki bir yıllık üst sınır uygulanmaz",
        }, "E",
        "Ahlak ve iyi niyet kurallarına aykırılıkta fesih hakkı, olayın öğrenilmesinden başlayarak altı iş günü ve kural olarak fiilden itibaren bir yıl içinde kullanılmalıdır. İşçinin olaydan maddi çıkar sağlaması hâlinde bir yıllık üst sınır uygulanmaz. İlk olayda 19 Mart tarihli fesih altı iş günlük süreyi aşmıştır.",
        "4857 sayılı İş Kanunu md. 26",
    ),
    "0010": p(
        "Fesih türleriyle ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Süreli fesih kural olarak belirsiz süreli sözleşmelerde bildirim süresine bağlıdır. II. Haklı nedenle derhal fesihte sözleşmenin sona ermesi için karşı tarafın kabulü gerekir. III. İkale iki tarafın sona erdirme iradelerinin uyuşmasını gerektirir.",
        {"A": "I ve III", "B": "I ve II", "C": "II ve III", "D": "Yalnız II", "E": "I, II ve III"},
        "A",
        "I ve III doğrudur. Haklı nedenle derhal fesih tek taraflı yenilik doğuran irade beyanıdır; karşı tarafın kabulü aranmaz. Kabul gerektiren sona erme biçimi ikaledir.",
        "4857 sayılı İş Kanunu md. 17, 24, 25; 6098 sayılı TBK md. 26",
    ),
    "0011": p(
        "A’nın son çıplak brüt ücreti 30.000 ₺; düzenli yemek ve yol menfaatlerinin aylık karşılığı 6.000 ₺’dir. A, aynı işverene bağlı iki yıl altı ay çalıştıktan sonra kıdem tazminatına hak kazanarak ayrılmıştır. Kanuni tavanın hesabı sınırlamadığı varsayımıyla aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Kıdem yalnız çıplak ücret ve tam yıllar üzerinden hesaplanır; altı aylık süre dikkate alınmaz",
            "B": "Düzenli menfaatler hesaba katılır ancak bir yıldan artan süreler oranlanmaz",
            "C": "Kıdem tazminatı bildirim süresine ait ücretle sınırlı olduğundan altı haftalık ücret ödenir",
            "D": "Hesap yalnız son bir yılda ödenen fazla çalışma ücretlerinin ortalaması üzerinden yapılır",
            "E": "Düzenli para ile ölçülebilen menfaatler ücrete eklenir ve iki yıl altı aylık kıdem orantılı hesaplanır",
        }, "E",
        "Kıdem tazminatına esas ücret, düzenli para ve para ile ölçülebilen menfaatleri de kapsayan giydirilmiş ücrettir. Her tam yıl için otuz günlük ücret ödenir; bir yıldan artan süreler de oranlanır. Kanuni tavan ayrıca gözetilir.",
        "1475 sayılı İş Kanunu md. 14",
    ),
    "0012": p(
        "İşçi aynı işverene ait A işyerinde sekiz ay, ardından kesintisiz biçimde B işyerinde yedi ay çalışmış ve işveren tarafından kıdem tazminatına hak kazandıran nedenle çıkarılmıştır. Asgari kıdem koşulu bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Her işyerindeki süre ayrı ayrı bir yıldan az olduğu için kıdem tazminatı doğmaz",
            "B": "Aynı işverene ait işyerlerindeki süreler birlikte değerlendirilir; toplam on beş ay bir yıllık koşulu karşılar",
            "C": "Süreler yalnız işyerleri aynı adreste ise birleştirilebilir",
            "D": "Bir yıllık koşul yerine her işyerinde en az altı ay çalışma aranır",
            "E": "Kıdem tazminatı için süre koşulu bulunmadığından ilk çalışma günü yeterlidir",
        }, "B",
        "Kıdem hesabında aynı işverenin bir veya değişik işyerlerinde geçen hizmet süreleri birlikte değerlendirilir. Toplam on beş aylık çalışma, bir yıllık asgari kıdem koşulunu karşılar.",
        "1475 sayılı İş Kanunu md. 14",
    ),
    "0013": p(
        "A işverence işletmesel nedenle, B ücretinin ödenmemesi üzerine kendisi tarafından, C muvazzaf askerlik nedeniyle ayrılmış; D ise işverenin güvenini kötüye kullanıp hırsızlık yaptığı için İş Kanunu md. 25/II uyarınca çıkarılmıştır. Hangisi kural olarak kıdem tazminatına hak kazanamaz?",
        {"A": "D", "B": "A", "C": "B", "D": "C", "E": "A ve C"},
        "A",
        "İşçinin ahlak ve iyi niyet kurallarına aykırı davranışı nedeniyle md. 25/II uyarınca haklı fesih, kıdem tazminatına hak kazandırmaz. İşverenin işletmesel feshi, işçinin ücret ödenmemesi nedeniyle haklı feshi ve askerlik nedeniyle ayrılma koşulları varsa kıdem tazminatı doğurur.",
        "1475 sayılı İş Kanunu md. 14; 4857 sayılı İş Kanunu md. 24/II, 25/II",
    ),
    "0014": p(
        "İşçinin aynı işverene bağlı kıdemi dört yıl altı aydır. Kıdem tazminatına hak kazanarak ayrıldığı ve kanuni tavanın hesabı sınırlamadığı varsayılırsa tazminat kaç günlük giydirilmiş ücret tutarındadır?",
        {"A": "120 günlük", "B": "125 günlük", "C": "130 günlük", "D": "135 günlük", "E": "150 günlük"},
        "D",
        "Her tam yıl için otuz günlük ücret ödenir; artan süre orantılanır. Dört yıl 120 gün, altı ay 15 gün olmak üzere toplam 135 günlük giydirilmiş ücret esas alınır.",
        "1475 sayılı İş Kanunu md. 14",
    ),
    "0015": p(
        "A, aynı işkolundaki işyerlerinde toplam kırk işçi çalıştıran işverenin bir işyerinde belirsiz süreli sözleşmeyle yedi aydır çalışmaktadır. B, kırk işçili yer altı işyerinde belirsiz süreli sözleşmeyle üç aydır çalışmaktadır. Her ikisi de işletmenin bütününü yöneten ve işe alma-çıkarma yetkisi bulunan işveren vekili değildir. İş güvencesi bakımından hangisi doğrudur?",
        {
            "A": "A işyerinde tek başına otuz işçi bulunmadığı varsayımıyla kapsam dışıdır; aynı işkolundaki diğer işyerleri sayılmaz",
            "B": "B altı aylık kıdemi bulunmadığından yer altı işinde de kapsam dışıdır",
            "C": "A işçi sayısı ve kıdem koşulunu; B ise yer altı işlerinde kıdem koşulu aranmadığından kapsam koşullarını karşılayabilir",
            "D": "İş güvencesi yalnız belirli süreli çalışanlara uygulanır",
            "E": "A ve B’nin kapsamı için işçi sayısı ile kıdemin hiçbir önemi yoktur",
        }, "C",
        "Otuz işçi hesabında işverenin aynı işkolundaki işyerlerinde çalışan toplam işçi sayısı dikkate alınır. Kural olarak en az altı aylık kıdem aranır; yer altı işlerinde çalışan işçilerde bu kıdem şartı aranmaz. Diğer kapsam koşulları da ayrıca bulunmalıdır.",
        "4857 sayılı İş Kanunu md. 18",
    ),
    "0016": p(
        "İş güvencesi kapsamındaki A’nın sözleşmesi düşük performans, B’ninki ekonomik daralma, C’ninki sendika üyeliği nedeniyle feshedilmiştir. Geçerli neden bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Yeterlilikten veya işletme gereklerinden kaynaklanan nedenler somut ve ölçülü ise geçerli olabilir; sendika üyeliği geçerli neden olamaz",
            "B": "Sendika üyeliği geçerli neden, ekonomik daralma ise hiçbir durumda geçerli neden değildir",
            "C": "İşverenin geçerli neden gösterme yükümlülüğü yalnız belirli süreli sözleşmelerde bulunur",
            "D": "Üç neden de işverenin yönetim hakkı kapsamında kendiliğinden geçerlidir",
            "E": "Geçerli fesih yalnız işçinin ahlak ve iyi niyet kurallarına aykırı davranışında mümkündür",
        }, "A",
        "İşçinin yeterliliği veya davranışları ile işletmenin, işyerinin ya da işin gerekleri geçerli neden oluşturabilir. Sendika üyeliği veya sendikal faaliyete katılma ise açıkça geçerli neden oluşturmaz.",
        "4857 sayılı İş Kanunu md. 18",
    ),
    "0017": p(
        "Fesih bildirimi 3 Haziranda tebliğ edilen iş güvencesi kapsamındaki işçi işe iade istemektedir. Arabuluculuk görüşmesi anlaşamama son tutanağıyla sona ermiştir. Başvuru sırası ve süreleri bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "İşçi doğrudan mahkemeye başvurmalı; arabuluculuk yalnız isteğe bağlıdır",
            "B": "İşçi fesihten itibaren beş yıl içinde arabulucuya başvurabilir",
            "C": "İşçi tebliğden itibaren bir ay içinde arabulucuya; anlaşma olmazsa son tutanaktan itibaren iki hafta içinde iş mahkemesine başvurmalıdır",
            "D": "Bir aylık süre mahkeme davası için, arabuluculuk süresi ise karar kesinleştikten sonra başlar",
            "E": "Arabuluculukta anlaşma olmazsa işe iade davası açma hakkı sona erer",
        }, "C",
        "İşe iade talebiyle fesih bildiriminin tebliğinden itibaren bir ay içinde arabulucuya başvurulur. Anlaşma sağlanamazsa son tutanağın düzenlendiği tarihten itibaren iki hafta içinde iş mahkemesinde dava açılabilir.",
        "4857 sayılı İş Kanunu md. 20; 7036 sayılı İş Mahkemeleri Kanunu md. 3",
    ),
    "0018": p(
        "Feshin geçersizliğine karar verilmiş, karar kesinleşince işçi on iş günü içinde başvurmuş ancak işveren bir ay içinde işe başlatmamıştır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "İşçi yalnız kıdem tazminatı isteyebilir; işe başlatmama ve boşta geçen süre ödemeleri doğmaz",
            "B": "İşçi dört ile sekiz aylık ücret tutarında işe başlatmama tazminatı ile en çok dört aya kadar boşta geçen süre ücret ve haklarını isteyebilir",
            "C": "İşe başlatmama tazminatı sabit olarak on iki aylık ücret, boşta geçen süre ücreti ise sınırsızdır",
            "D": "İşçinin on iş günlük başvurusu geç olduğundan kararın bütün sonuçları ortadan kalkmıştır",
            "E": "İşverenin işe başlatmaması hâlinde fesih tarihi değişmez ve ek bir ödeme doğmaz",
        }, "B",
        "Süresinde başvuran işçi bir ay içinde işe başlatılmazsa dört ile sekiz aylık ücret tutarında tazminat ödenir. Kararın kesinleşmesine kadar çalıştırılmadığı süre için en çok dört aya kadar ücret ve diğer haklar ayrıca doğar.",
        "4857 sayılı İş Kanunu md. 21",
    ),
    "0019": p(
        "İşe iade kararı sonrasında aşağıdaki ifadelerden hangileri doğrudur? I. İşçi kesinleşen kararın tebliğinden itibaren on iş günü içinde işverene başvurmalıdır. II. İşveren başvuran işçiyi altı ay içinde işe başlatabilir. III. İşçi süresinde başvurmazsa işverence yapılan fesih geçerli sayılır.",
        {"A": "Yalnız I", "B": "I ve II", "C": "II ve III", "D": "I ve III", "E": "I, II ve III"},
        "D",
        "I ve III doğrudur. İşveren, süresinde başvuran işçiyi bir ay içinde işe başlatmalıdır; altı aylık süre yoktur. İşçi on iş günü içinde başvurmazsa işverence yapılmış fesih geçerli sayılır.",
        "4857 sayılı İş Kanunu md. 21",
    ),
    "0020": p(
        "İşverenin sunduğu ikale önerisini kabul eden işçiye yalnız kanuni kıdem ve ihbar alacakları ödenmiş; işçi daha sonra sona erdirme iradesinin özgür olmadığını ve ek yarar sağlanmadığını ileri sürmüştür. İkalenin geçerliliği incelenirken aşağıdakilerden hangisi önem taşımaz?",
        {
            "A": "İkale teklifinin hangi taraftan geldiği",
            "B": "İşçinin makul yararının bulunup bulunmadığı",
            "C": "İrade fesadı ve işverenin üstün konumunu kullanıp kullanmadığı",
            "D": "İşverenin tek taraflı fesih için kanundaki haklı nedenlerden birine sahip olup olmadığı her ikalede tek ve kesin geçerlilik şartıdır",
            "E": "Sözleşmenin sona ermesi karşılığında işçiye sağlanan toplam menfaat",
        }, "D",
        "İkale karşılıklı anlaşmadır. Geçerlilikte teklifin kimden geldiği, işçinin makul yararı, iradenin özgür oluşu ve sağlanan menfaatler değerlendirilir. İşverenin tek taraflı haklı fesih nedenine sahip olması her ikale için zorunlu bir geçerlilik şartı değildir.",
        "6098 sayılı TBK md. 26-27; iş hukuku ikale ilkeleri",
    ),
    "0021": p(
        "Altı yıldır çalışan işçi vefat etmiş; geride eşi ile ergin olmayan çocuğu kalmıştır. İşçinin ölümü üzerine doğan haklar bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Sözleşme mirasçılarla aynen devam eder; ölüm sona erme nedeni değildir",
            "B": "Sözleşme sona erer ancak işverenin ölüm tazminatı veya doğmuş işçilik alacaklarına ilişkin hiçbir borcu kalmaz",
            "C": "Yalnız kullanılmayan yıllık izin ücreti ödenebilir; başka bir ödeme mümkün değildir",
            "D": "Ölüm tazminatı yalnız işçinin kıdemi bir yıldan azsa doğar",
            "E": "Sözleşme ölümle sona erer; doğmuş alacakların yanında beş yıldan uzun hizmet nedeniyle eşe veya ergin olmayan çocuklara iki aylık ücret tutarında ödeme gündeme gelir",
        }, "E",
        "İşçinin ölümü iş sözleşmesini kendiliğinden sona erdirir. İşveren, sağ kalan eşe ve ergin olmayan çocuklara; bunlar yoksa bakmakla yükümlü olunan kişilere bir aylık, hizmet beş yıldan uzunsa iki aylık ücret tutarında ödeme yapar. Doğmuş diğer alacaklar da saklıdır.",
        "6098 sayılı TBK md. 440; 4857 sayılı İş Kanunu md. 59",
    ),
    "0022": p(
        "Kadın işçi evlendiği tarihten on bir ay sonra, aynı işverene bağlı iki yıllık kıdemi varken evlilik nedeniyle sözleşmesini feshetmiştir. Bildirim süresine de uymamıştır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Evlilik yalnız işverene fesih hakkı verir; işçinin feshi istifa sayılır",
            "B": "İşçi kıdem tazminatı alamaz ve sekiz haftalık ihbar tazminatı öder",
            "C": "Bir yıl içinde evlilik nedeniyle feshettiği ve kıdem koşulunu taşıdığı için kıdem tazminatı alabilir; haklı/özel sona erme nedeniyle ihbar süresi aranmaz",
            "D": "Kıdem tazminatı için evlilikten sonra en az beş yıl çalışma gerekir",
            "E": "Evlilik nedeniyle ayrılmada kıdem tazminatı yalnız erkek işçiye ödenir",
        }, "C",
        "Kadın işçinin evlendiği tarihten itibaren bir yıl içinde kendi isteğiyle sözleşmesini sona erdirmesi kıdem tazminatına hak kazandırır; en az bir yıllık kıdem de olayda vardır. Bu özel fesihte ihbar süresi uygulanmaz.",
        "1475 sayılı İş Kanunu md. 14",
    ),
    "0023": p(
        "İşveren, ayrılan işçiye verdiği çalışma belgesinde işin türünü gerçeğe aykırı yazmış; bu nedenle işçi yeni işe alınmamış ve yeni işveren de yanıltıcı bilgi nedeniyle zarara uğramıştır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "İşveren gerçeğe aykırı veya zamanında verilmeyen belge nedeniyle zarar gören işçi ve yeni işverene karşı sorumlu olabilir",
            "B": "Çalışma belgesi yalnız işçinin ücretini içerir; işin türü ve süresi yazılamaz",
            "C": "Belge verme yükümlülüğü yalnız işçi en az beş yıl çalışmışsa doğar",
            "D": "Gerçeğe aykırı belge hiçbir hukuki sonuç doğurmaz; bilgi yalnız tavsiye niteliğindedir",
            "E": "Çalışma belgesini işveren değil, işçinin üyesi olduğu sendika düzenler",
        }, "A",
        "İşten ayrılan işçiye işinin çeşidini ve süresini gösteren belge verilir. Belgenin zamanında verilmemesi veya yanlış bilgi içermesi nedeniyle zarar gören işçi ya da işçiyi işe alan yeni işveren eski işverenden tazminat isteyebilir.",
        "4857 sayılı İş Kanunu md. 28",
    ),
    "0024": p(
        "İşçi ile işveren, iş sözleşmesinin sona erdiği gün bütün işçilik alacaklarının ibra edildiğini belirten yazılı belge düzenlemiştir. Belgede alacak tür ve miktarları ayrı ayrı gösterilmemiş, ödeme nakit yapılmıştır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Yazılı olması tek başına yeterlidir; tarih, miktar ve ödeme biçimi önem taşımaz",
            "B": "Sona ermeden en az bir ay geçmeden düzenlenmesi, alacakların açıkça gösterilmemesi ve banka yoluyla tam ödeme yapılmaması nedeniyle ibra kesin hükümsüzdür",
            "C": "İbraname yalnız noter onayı bulunmadığı için geçersizdir; diğer koşullar aranmaz",
            "D": "Nakit ödeme işçinin imzasıyla kanıtlandığı için bütün eksiklikleri giderir",
            "E": "İşçilik alacaklarında ibra sözleşmesi hiçbir biçimde yapılamaz",
        }, "B",
        "İşçi alacağına ilişkin ibra; yazılı olmalı, sözleşmenin sona ermesinden başlayarak en az bir ay geçtikten sonra düzenlenmeli, alacağın tür ve miktarını açıkça göstermeli ve ödeme hak tutarına uygun biçimde banka aracılığıyla yapılmalıdır. Koşulları taşımayan ibra kesin hükümsüzdür.",
        "6098 sayılı TBK md. 420",
    ),
    "0025": p(
        "Tazminatlarla ilgili aşağıdaki ifadelerden hangileri doğrudur? I. İhbar tazminatı, bildirim süresine uymayan tarafça karşı tarafa ödenebilir. II. Kıdem tazminatında kural olarak en az bir yıllık kıdem aranır. III. İşe başlatmama tazminatı, geçersiz fesih kararına rağmen süresinde başvuran işçinin işe başlatılmaması hâlinde doğabilir.",
        {"A": "I ve II", "B": "I, II ve III", "C": "II ve III", "D": "Yalnız III", "E": "I ve III"},
        "B",
        "Üç ifade de doğrudur. İhbar tazminatının borçlusu bildirim süresine uymayan işçi veya işveren olabilir; kıdem tazminatında bir yıl aranır; işe başlatmama tazminatı ise geçersiz fesih kararının uygulanmamasının sonucudur.",
        "4857 sayılı İş Kanunu md. 17, 21; 1475 sayılı İş Kanunu md. 14",
    ),
    "0026": p(
        "İşveren, 120 işçi çalıştırdığı işyerinde ekonomik nedenle bir ay içinde 15 işçiyi çıkarmayı planlamakta ve fesihleri aynı gün uygulamak istemektedir. Toplu işçi çıkarma bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "İşçi sayısı 101-300 arasındayken bir ay içinde en az %10 çıkarma toplu çıkarma sayılır; işyeri sendika temsilcileri, ilgili bölge müdürlüğü ve İŞKUR’a en az otuz gün önce bildirim yapılır",
            "B": "Toplu çıkarma yalnız 300’den fazla işçi bulunan işyerlerinde mümkündür",
            "C": "120 işçili işyerinde sayı eşiği her durumda otuz işçidir",
            "D": "Bildirim fesihlerden sonra yapılır ve fesihler bildirimden bağımsız aynı gün hüküm doğurur",
            "E": "Toplu çıkarma hükümleri ekonomik veya teknolojik nedenlerle yapılan fesihlere uygulanmaz",
        }, "A",
        "101-300 işçi çalıştırılan işyerinde bir ay içinde en az %10 oranında işçinin çıkarılması toplu işçi çıkarmadır. İşveren bunu en az otuz gün önce işyeri sendika temsilcilerine, ilgili bölge müdürlüğüne ve İŞKUR’a bildirir.",
        "4857 sayılı İş Kanunu md. 29",
    ),
    "0027": p(
        "İki yıl kıdemli işçi, işverene yüklenebilecek haklı bir neden bulunmaksızın ve bildirim yapmadan başka bir işe geçmek için ayrılmıştır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "İşçi her istifada kıdem ve ihbar tazminatına hak kazanır",
            "B": "İstifa kıdem tazminatına hak kazandırır; bildirim yapılmadığı için yalnız ihbar hakkı kaybolur",
            "C": "İşçi kıdem tazminatı alamaz ancak işverenden altı haftalık ihbar tazminatı isteyebilir",
            "D": "İşçinin ayrılması ancak işveren kabul ederse sonuç doğurur",
            "E": "Haklı nedensiz istifa kıdem tazminatı doğurmaz; altı haftalık bildirim süresine uyulmadığı için işveren ihbar tazminatı isteyebilir",
        }, "E",
        "Haklı nedene dayanmayan olağan istifa kıdem tazminatına hak kazandırmaz. İki yıllık kıdem için altı haftalık bildirim süresine uymayan işçiden işveren ihbar tazminatı talep edebilir.",
        "4857 sayılı İş Kanunu md. 17; 1475 sayılı İş Kanunu md. 14",
    ),
    "0028": p(
        "Erkek işçi üç yıllık kıdemi varken muvazzaf askerlik hizmeti nedeniyle sözleşmesini feshetmiştir. İşveren, feshi işçinin yaptığını ileri sürerek tazminat ödemeyi reddetmiştir. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "İşçi kendi feshettiğinden hem kıdem hem ihbar tazminatı alır",
            "B": "Askerlik yalnız ücretsiz izin nedenidir; sözleşme feshedilemez",
            "C": "Kıdem tazminatı için askerden döndükten sonra aynı işyerinde beş yıl çalışma gerekir",
            "D": "Muvazzaf askerlik nedeniyle ayrılma kıdem tazminatına hak kazandırır; bu özel fesihte işçi ihbar süresine bağlı değildir",
            "E": "Askerlik nedeniyle kıdem tazminatı yalnız bir yıldan az kıdemi olan işçiye ödenir",
        }, "D",
        "Muvazzaf askerlik hizmeti nedeniyle iş sözleşmesinin sona erdirilmesi, en az bir yıllık kıdem varsa kıdem tazminatına hak kazandırır. Bu özel sona ermede işçi bildirim süresine bağlı değildir ve ihbar tazminatı doğmaz.",
        "1475 sayılı İş Kanunu md. 14",
    ),
    "0029": p(
        "İşveren, iş güvencesi kapsamındaki işçiyi davranışına dayanarak çıkarmış; fesih bildirimini yazılı yapmış ancak işçinin savunmasını almamıştır. Davranış aynı zamanda İş Kanunu md. 25/II ağırlığında değildir. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            "A": "Davranışa dayalı geçerli fesihte kural olarak işçinin savunması alınmalıdır",
            "B": "Fesih bildirimi yazılı yapılmalı ve neden açık, kesin biçimde belirtilmelidir",
            "C": "Savunma alınmaması yalnız biçimsel bir eksikliktir ve feshin geçerliliğini hiçbir şekilde etkileyemez",
            "D": "İşveren gösterdiği fesih sebebiyle bağlıdır",
            "E": "Md. 25/II kapsamındaki haklı fesih hakkı, savunma alma kuralına ilişkin istisna oluşturur",
        }, "C",
        "İşçinin davranışı veya verimiyle ilgili geçerli fesih, savunması alınmadan yapılamaz. Savunma eksikliği feshin geçersizliğine yol açabilir; salt önemsiz bir biçim eksikliği değildir. Md. 25/II kapsamındaki haklı fesih hakkı saklıdır.",
        "4857 sayılı İş Kanunu md. 19",
    ),
    "0030": p(
        "Aşağıdaki olay–sona erme türü eşleştirmelerinden hangisi doğrudur?",
        {
            "A": "Tarafların karşılıklı anlaşması – işverenin tek taraflı süreli feshi",
            "B": "İşçinin işverenin güvenini kötüye kullanması – işverenin haklı nedenle derhal feshi",
            "C": "Belirli sürenin dolması – işçinin haklı nedenle derhal feshi",
            "D": "Ekonomik daralma – sözleşmenin işçinin ölümüyle sona ermesi",
            "E": "İşverenin ücreti ödememesi – işverenin süreli feshi",
        }, "B",
        "İşçinin güveni kötüye kullanması doğruluk ve bağlılığa aykırı davranıştır ve işverene haklı nedenle derhal fesih hakkı verebilir. Diğer seçeneklerde olay ile sona erme türü birbirine uymamaktadır.",
        "4857 sayılı İş Kanunu md. 25/II",
    ),
    "0031": p(
        "İşveren, iki yıl kıdemli ve iş güvencesi kapsamındaki işçinin sözleşmesini işletmesel nedenle feshetmiş; altı haftalık bildirim süresine ait ücreti peşin ödeyip işçiyi hemen işten ayırmıştır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Peşin ödeme feshi haklı nedenle derhal feshe dönüştürür ve geçerli neden incelemesini kaldırır",
            "B": "Peşin ödeme yalnız işçinin yazılı kabulüyle mümkündür",
            "C": "Bildirim ücreti peşin ödendiğinden işçi hiçbir koşulda işe iade talep edemez",
            "D": "İşveren bildirim süresi ücretini peşin ödeyebilir; ancak iş güvencesi kapsamındaki fesih yine geçerli nedene ve diğer koşullara uygun olmalıdır",
            "E": "Peşin ödeme yapılınca kıdem tazminatı ve kullanılmayan izin ücreti hakları kendiliğinden sona erer",
        }, "D",
        "İşveren bildirim süresine ait ücreti peşin vererek sözleşmeyi sona erdirebilir. Bu yöntem iş güvencesi hükümlerini bertaraf etmez; fesih geçerli nedene ve usule uygun olmalıdır. Kıdem ve izin gibi diğer haklar ayrıca değerlendirilir.",
        "4857 sayılı İş Kanunu md. 17-19",
    ),
    "0032": p(
        "İş güvencesi kapsamı dışında kalan dört yıl kıdemli işçi, işverene karşı ücret davası açtığı için sekiz haftalık bildirim süresi kullandırılarak çıkarılmıştır. Kötüniyet tazminatı bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Bildirim süresine uyulmuş olması kötüniyetli feshi her durumda hukuka uygun kılar",
            "B": "İş güvencesi dışında kalan işçi, fesih hakkı kötüye kullanılmışsa bildirim süresinin üç katı tutarında kötüniyet tazminatı isteyebilir",
            "C": "Kötüniyet tazminatı yalnız iş güvencesi kapsamındaki işçinin işe iade davasında istenir",
            "D": "Tazminat işçi tarafından işverene ödenir ve bir aylık ücretle sınırlıdır",
            "E": "İşçinin yasal hakkını araması fesihte kötüniyet değerlendirmesine konu olamaz",
        }, "B",
        "İş güvencesi hükümleri dışında kalan belirsiz süreli çalışan işçinin fesih hakkı kötüye kullanılarak sözleşmesi sona erdirilirse, bildirim süresinin üç katı tutarında kötüniyet tazminatı doğabilir. Bildirim süresine ayrıca uyulmuş olması kötüniyeti ortadan kaldırmaz.",
        "4857 sayılı İş Kanunu md. 17",
    ),
    "0033": p(
        "İş sözleşmesinin sona ermesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Belirli süreli sözleşme, aksi kararlaştırılmadıkça sürenin sonunda kendiliğinden sona erer. II. İşçinin ölümü hâlinde sözleşme mirasçılarla devam eder. III. İkale, tarafların karşılıklı ve birbirine uygun irade açıklamalarını gerektirir.",
        {"A": "Yalnız I", "B": "I ve II", "C": "I ve III", "D": "II ve III", "E": "I, II ve III"},
        "C",
        "I ve III doğrudur. Belirli süreli sözleşme kural olarak sürenin dolmasıyla sona erer; ikale karşılıklı anlaşmadır. İşçinin ölümü sözleşmeyi kendiliğinden sona erdirdiğinden mirasçılarla devam etmez.",
        "6098 sayılı TBK md. 430, 440",
    ),
    "0034": p(
        "İşyerinde bir haftadan uzun süre işin durmasını gerektiren zorlayıcı sebep ortaya çıkmıştır. İşçi bu nedenle sözleşmesini feshetmek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "İşçi, çalıştığı işyerinde işin bir haftadan fazla durmasını gerektiren zorlayıcı sebep varsa haklı nedenle derhal feshedebilir; ilk bir haftada yarım ücret kuralı da gündeme gelir",
            "B": "Zorlayıcı sebep yalnız işverene fesih hakkı verir; işçi sözleşmeyi sona erdiremez",
            "C": "İşçi feshedebilmek için işin en az altı ay durmuş olmasını beklemelidir",
            "D": "Zorlayıcı sebep sözleşmeyi kendiliğinden sona erdirir; fesih beyanı gerekmez",
            "E": "Zorlayıcı sebepte işçi kıdemi ne olursa olsun kıdem tazminatı alamaz",
        }, "A",
        "İşçinin çalıştığı işyerinde bir haftadan fazla süreyle işin durmasını gerektiren zorlayıcı neden, işçiye haklı fesih hakkı verir. Zorlayıcı sebeple çalışılmayan ilk bir hafta için yarım ücret ödenir. Kıdem koşulları varsa işçinin haklı feshi kıdem tazminatı doğurur.",
        "4857 sayılı İş Kanunu md. 24/III, 40; 1475 sayılı İş Kanunu md. 14",
    ),
    "0035": p(
        "Kıdem tazminatına ilişkin aşağıdaki ifadelerden hangileri doğrudur? I. İşçinin ücretinin ödenmemesi nedeniyle haklı feshi kıdem tazminatına hak kazandırabilir. II. İşçinin md. 25/II kapsamındaki hırsızlığı nedeniyle işverence çıkarılması kıdem tazminatına hak kazandırır. III. Muvazzaf askerlik nedeniyle ayrılma kıdem tazminatına hak kazandırabilir.",
        {"A": "Yalnız I", "B": "I ve II", "C": "II ve III", "D": "I ve III", "E": "I, II ve III"},
        "D",
        "I ve III doğrudur. Ücret ödenmemesi işçinin haklı fesih nedeni olabilir; askerlik özel kıdem tazminatı nedenidir. İşçinin hırsızlık gibi md. 25/II davranışı nedeniyle çıkarılması kıdem tazminatı doğurmaz.",
        "1475 sayılı İş Kanunu md. 14; 4857 sayılı İş Kanunu md. 24/II, 25/II",
    ),
    "0036": p(
        "İş güvencesi kapsamındaki işçinin sözleşmesi hiçbir neden gösterilmeden feshedilmiş; işçi bir ay içinde arabulucuya başvurmuş ve anlaşma sağlanamamıştır. İşçinin izlemesi gereken yol bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "İşçi yalnız kıdem tazminatı isteyebilir; fesih geçerliliği denetlenemez",
            "B": "İşçi doğrudan idare mahkemesinde iptal davası açmalıdır",
            "C": "Arabuluculukta anlaşma olmadığından işe iade isteme hakkı sona ermiştir",
            "D": "İşçi son tutanaktan itibaren iki hafta içinde iş mahkemesinde işe iade davası açabilir",
            "E": "İşe iade davası yalnız işverenin yazılı izniyle açılabilir",
        }, "D",
        "İşçi süresinde arabulucuya başvurmuş ve anlaşma sağlanamamıştır. Son tutanağın düzenlendiği tarihten itibaren iki hafta içinde iş mahkemesinde işe iade davası açabilir.",
        "4857 sayılı İş Kanunu md. 20; 7036 sayılı İş Mahkemeleri Kanunu md. 3",
    ),
    "0037": p(
        "İşçi bir ay içinde izin almaksızın pazartesi ve salı ardı ardına işe gelmemiş; aynı ay iki ayrı hafta tatilinden sonraki iş gününde de devamsızlık yapmıştır. Devamsızlıkların haklı sebebi bulunmamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Her iki devamsızlık biçimi de kanundaki eşiklerden birini karşılayabilir ve işverene haklı fesih hakkı verebilir",
            "B": "Haklı fesih için devamsızlığın kesintisiz otuz gün sürmesi gerekir",
            "C": "Yalnız hafta tatilinden sonraki devamsızlık dikkate alınır; ardı ardına iki iş günü yeterli değildir",
            "D": "Devamsızlık hiçbir durumda haklı fesih nedeni olmaz; yalnız ücret kesilebilir",
            "E": "İşveren devamsızlığı öğrendikten sonra bir yıllık bildirim süresi vermelidir",
        }, "A",
        "İzinsiz veya haklı nedensiz ardı ardına iki iş günü devamsızlık ile bir ay içinde iki kez tatil gününden sonraki iş günü devamsızlık, kanunda ayrı ayrı haklı fesih eşiğidir. Bir ayda üç iş günü devamsızlık da diğer eşiktir.",
        "4857 sayılı İş Kanunu md. 25/II-(g)",
    ),
    "0038": p(
        "İşveren A’yı düşük performans, B’yi işletmesel küçülme, C’yi ise hırsızlık nedeniyle çıkarmak istemektedir. Fesihte savunma alma yükümlülüğü bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Üç işçinin de savunması alınmadan yapılan her fesih kendiliğinden geçerlidir",
            "B": "Yalnız işletmesel fesihte savunma alınması zorunludur",
            "C": "A’nın davranış/yeterliliğine dayalı geçerli feshinden önce savunması alınır; B’nin işletmesel feshinde bu koşul aranmaz, md. 25/II kapsamındaki C yönünden haklı fesih hakkı saklıdır",
            "D": "Savunma yalnız sözlü alınabilir; yazılı savunma geçersizdir",
            "E": "Savunma alınması fesih nedeninin yazılı ve açık gösterilmesi yükümlülüğünü kaldırır",
        }, "C",
        "Davranış veya verime dayalı geçerli fesihte işçinin savunması alınmalıdır. İşletme, işyeri veya işin gereklerine dayalı fesihte savunma koşulu aranmaz. Md. 25/II kapsamındaki haklı derhal fesih hakkı ayrıca saklıdır.",
        "4857 sayılı İş Kanunu md. 19, 25/II",
    ),
    "0039": p(
        "İş güvencesi kapsamındaki işçinin sözleşmesi aşağıdaki nedenlerden hangisine dayanılarak geçerli biçimde feshedilemez?",
        {
            "A": "Belgelenen ve süreklilik gösteren yetersiz performans",
            "B": "İşçinin hamileliği ve doğum iznini kullanacak olması",
            "C": "İşletmenin faaliyet alanını daraltması nedeniyle işgücü fazlası doğması",
            "D": "İşçinin iş akışını ciddi biçimde bozan ancak haklı fesih ağırlığına ulaşmayan davranışı",
            "E": "İşyerinde teknolojik değişiklik nedeniyle belirli pozisyonun ortadan kalkması",
        }, "B",
        "Hamilelik, doğum ve kanuni izinlerin kullanılması geçerli fesih nedeni oluşturmaz. İşçinin yeterliliği veya davranışları ile işletmenin, işyerinin veya işin gerekleri somut ve ölçülü koşullarda geçerli neden olabilir.",
        "4857 sayılı İş Kanunu md. 18",
    ),
    "0040": p(
        "İşe iade kararının sonuçlarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur? I. İşçi kesinleşen kararın tebliğinden itibaren on iş günü içinde işverene başvurur. II. İşveren başvuruyu izleyen bir ay içinde işçiyi işe başlatır. III. İşçinin süresinde başvurmaması hâlinde işverence yapılan fesih geçerli sayılır.",
        {"A": "I ve II", "B": "I, II ve III", "C": "II ve III", "D": "Yalnız I", "E": "I ve III"},
        "B",
        "Üç ifade de doğrudur. İşçinin on iş günlük başvuru süresi ve işverenin bir aylık işe başlatma süresi vardır. İşçi süresinde başvurmazsa işverence yapılan fesih geçerli sayılır ve işveren yalnız geçerli feshin sonuçlarından sorumlu olur.",
        "4857 sayılı İş Kanunu md. 21",
    ),
    "0041": p(
        "İşçinin yaptığı iş, işin niteliğinden kaynaklanan bir nedenle sağlığı için tehlikeli hâle gelmiş; hekim raporu da tehlikeyi doğrulamıştır. İşveren uygun başka iş önermemiştir. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "İşçi yalnız bildirim süresine uyarak istifa edebilir ve kıdem tazminatı alamaz",
            "B": "İşçi sağlık nedeniyle haklı olarak derhal feshedebilir; en az bir yıllık kıdemi varsa kıdem tazminatı gündeme gelebilir",
            "C": "Sağlık nedeni yalnız işverene fesih hakkı verir, işçiye vermez",
            "D": "İşçi sözleşmeyi feshedebilmek için tehlikenin en az bir yıl sürmesini beklemelidir",
            "E": "Hekim raporu bulunsa da sağlık tehlikesi iş sözleşmesinin feshinde dikkate alınamaz",
        }, "B",
        "İşin yapılması işin niteliğinden doğan nedenle işçinin sağlığı veya yaşayışı için tehlikeli olursa işçi haklı nedenle derhal feshedebilir. En az bir yıllık kıdem dâhil diğer koşullar varsa kıdem tazminatı doğar.",
        "4857 sayılı İş Kanunu md. 24/I; 1475 sayılı İş Kanunu md. 14",
    ),
    "0042": p(
        "Bir yıllık belirli süreli iş sözleşmesi 31 Aralıkta sona erecektir. Taraflar sözleşmeyi yenilememiş ve sözleşmede ayrıca bildirim koşulu kararlaştırmamıştır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Sözleşme kural olarak 31 Aralıkta kendiliğinden sona erer; belirsiz süreli sözleşmelere özgü bildirim süreleri uygulanmaz",
            "B": "İşveren sekiz haftalık bildirim yapmadıkça sözleşme sonsuza kadar uzar",
            "C": "Sürenin dolması yalnız işçi kabul ederse sonuç doğurur",
            "D": "Sözleşme kendiliğinden sona erdiği için işçinin doğmuş ücret ve izin alacakları da ortadan kalkar",
            "E": "Belirli süreli sözleşme süresi dolsa bile ancak haklı nedenle fesihle sona erebilir",
        }, "A",
        "Belirli süreli sözleşme, aksi kararlaştırılmadıkça sürenin bitiminde kendiliğinden sona erer. İş Kanunu md. 17’deki bildirim süreleri belirsiz süreli sözleşmeler içindir. Sona erme doğmuş işçilik alacaklarını ortadan kaldırmaz.",
        "6098 sayılı TBK md. 430; 4857 sayılı İş Kanunu md. 17",
    ),
    "0043": p(
        "İşçi aynı işverene ait üç işyerinde sırasıyla iki yıl, bir yıl ve altı ay çalışmış; işyerleri arasında geçiş yapılırken sözleşmesi kesintiye uğramamıştır. Kıdem hesabı bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Yalnız son işyerindeki altı aylık süre dikkate alınır",
            "B": "Her işyerinde süre yeniden başlar; hiçbir süre bir yılı aşmadığından kıdem doğmaz",
            "C": "Yalnız aynı adreste geçen süreler birleştirilebilir",
            "D": "İşçi hangi işyerindeki sürenin dikkate alınacağını tek taraflı seçer",
            "E": "Aynı işverenin değişik işyerlerindeki süreler birleştirilir ve toplam üç yıl altı ay üzerinden hesap yapılır",
        }, "E",
        "Kıdem, işçinin aynı işverenin bir veya değişik işyerlerinde çalıştığı süreler birlikte değerlendirilerek hesaplanır. Olayda toplam kıdem üç yıl altı aydır.",
        "1475 sayılı İş Kanunu md. 14",
    ),
    "0044": p(
        "İşveren, işçinin hamileliği nedeniyle sözleşmesini feshetmiş; fesih bildiriminde gerekçeyi işletmesel küçülme olarak göstermiştir. Yargılamada başka bir neden ileri sürmek istemektedir. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            "A": "Hamilelik geçerli fesih nedeni oluşturmaz",
            "B": "Fesih nedeni yazılı bildirimde açık ve kesin biçimde gösterilmelidir",
            "C": "İşveren yargılamada bildirimde göstermediği sınırsız sayıda yeni fesih nedeni ileri sürerek feshi geçerli hâle getirebilir",
            "D": "Geçerli fesih nedenini ispat yükü kural olarak işverene aittir",
            "E": "Görünen işletmesel nedenin gerçek ve tutarlı olup olmadığı yargısal denetime tabidir",
        }, "C",
        "İşveren fesih bildiriminde gösterdiği nedenle bağlıdır; sonradan sınırsız biçimde yeni neden ileri sürerek feshi geçerli kılamaz. Hamilelik geçerli neden değildir; işletmesel nedenin gerçekliği ve tutarlılığı denetlenir.",
        "4857 sayılı İş Kanunu md. 18-20",
    ),
    "0045": p(
        "İki yıl kıdemli işçi işyeri dışındaki bir olay nedeniyle tutuklanmış ve devamsızlığı kıdemine göre uygulanacak bildirim süresini aşmıştır. İşverenin fesih hakkı bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Tutukluluk ilk günden itibaren md. 25/II kapsamında ahlak ve iyi niyet nedeni sayılır",
            "B": "İşveren ancak ceza mahkûmiyeti kesinleştikten beş yıl sonra feshedebilir",
            "C": "Devamsızlık bildirim süresini aşsa da işveren sözleşmeyi feshedemez",
            "D": "Gözaltı veya tutukluluk nedeniyle devamsızlık bildirim süresini aşarsa işveren md. 25/IV uyarınca derhal feshedebilir; kıdem koşulları varsa kıdem tazminatı saklıdır",
            "E": "Bu fesihte işçi hem ihbar hem kötüniyet tazminatına kendiliğinden hak kazanır",
        }, "D",
        "İşçinin gözaltına alınması veya tutuklanması nedeniyle devamsızlığının md. 17’deki bildirim süresini aşması işverene md. 25/IV uyarınca derhal fesih hakkı verir. Bu bent md. 25/II değildir; en az bir yıllık kıdem varsa kıdem tazminatı doğabilir, ihbar tazminatı doğmaz.",
        "4857 sayılı İş Kanunu md. 17, 25/IV; 1475 sayılı İş Kanunu md. 14",
    ),
    "0046": p(
        "İşveren iş güvencesi kapsamındaki işçinin sözleşmesini performans düşüklüğü nedeniyle feshetmiş; işçi ise gerçek nedenin sendikal faaliyet olduğunu ileri sürmüştür. İspat yükü bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Feshin geçerli nedene dayandığını her durumda yalnız işçi ispatlar",
            "B": "İşveren gösterdiği geçerli nedeni ispatlar; işçi feshin başka bir nedene dayandığını iddia ediyorsa bu iddiasını ispatla yükümlüdür",
            "C": "İspat yükü yalnız arabulucuya aittir; tarafların delil sunması yasaktır",
            "D": "İşveren hiçbir delil sunmasa da performans gerekçesi doğru kabul edilir",
            "E": "Sendikal neden iddiası ileri sürülünce işverenin gösterdiği neden artık incelenmez",
        }, "B",
        "Feshin geçerli bir nedene dayandığını ispat yükü işverene aittir. İşçi feshin işverenin gösterdiği nedenden başka bir nedene dayandığını iddia ederse bu iddiasını ispatla yükümlüdür. Sendikal güvencelere ilişkin özel ispat kuralları da saklıdır.",
        "4857 sayılı İş Kanunu md. 20; 6356 sayılı Kanun md. 25",
    ),
    "0047": p(
        "İşçi işe iade ile birlikte kıdem ve ihbar tazminatı alacaklarını da talep etmek istemektedir. Dava şartı arabuluculuk bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Arabuluculuk yalnız ceza uyuşmazlıklarında uygulanır",
            "B": "İşe iade talebinde arabuluculuk isteğe bağlı, tazminat alacaklarında yasaktır",
            "C": "İşçi yalnız işveren kabul ederse arabulucuya başvurabilir",
            "D": "Arabuluculuk başvurusu yapılmadan açılan dava her durumda esastan kabul edilir",
            "E": "İşe iade ile kanuna veya iş sözleşmesine dayanan işçi alacağı ve tazminatı davalarında, kanuni istisnalar dışında dava açmadan önce arabulucuya başvuru dava şartıdır",
        }, "E",
        "İşe iade talebi ile bireysel veya toplu iş sözleşmesine dayanan işçi ya da işveren alacağı ve tazminatı davalarında, kanuni istisnalar dışında arabulucuya başvuru dava şartıdır.",
        "7036 sayılı İş Mahkemeleri Kanunu md. 3; 4857 sayılı İş Kanunu md. 20",
    ),
    "0048": p(
        "İşveren satışların azalması üzerine aynı işi yapan on işçiden yalnız A’nın sözleşmesini feshetmiş; fazla çalışma uygulamasını ve yeni işçi alımını sürdürmüş, A’yı başka pozisyonda değerlendirme olanağını araştırmamıştır. A iki yıldır çalışmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Satış azalması ileri sürüldüğünde fesih otomatik olarak geçerlidir; alınan diğer önlemler incelenmez",
            "B": "İşletmesel fesihte işverenin tutarlılığı ve feshin son çare olması ilkesi hiçbir önem taşımaz",
            "C": "İşletmesel kararın gerçekliği, tutarlı uygulanması ve feshin son çare olması denetlenebilir; kıdem ve bildirim hakları da ayrıca değerlendirilir",
            "D": "İki yıllık kıdemi olan işçi işletmesel fesihte hiçbir tazminat talep edemez",
            "E": "İşveren işletmesel nedenle yalnız haklı derhal fesih yapabilir ve bildirim süresi uygulayamaz",
        }, "C",
        "İşletmesel fesihte kararın gerçekliği, tutarlı uygulanması, keyfîlik bulunmaması ve feshin son çare olması denetlenir. Fazla çalışma ile yeni işe alımın sürmesi ve alternatif pozisyonun araştırılmaması geçerliliği etkileyebilir. Kıdem ve ihbar hakları ayrıca değerlendirilir.",
        "4857 sayılı İş Kanunu md. 17-18; geçerli fesihte son çare ilkesi",
    ),
    "0049": p(
        "İşçinin performansı belgeli biçimde düşmüş ancak davranış haklı fesih ağırlığına ulaşmamıştır. İşveren sözleşmeyi bildirim süresine uyarak feshetmiştir. Geçerli fesih ile haklı derhal fesih ayrımı bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Geçerli ve haklı neden aynı kavramdır; iki fesihte de bildirim süresi uygulanmaz",
            "B": "Haklı fesih yalnız işçi, geçerli fesih yalnız işveren tarafından yapılabilir",
            "C": "Performans düşüklüğü varsa işveren her durumda kıdem tazminatı ödemeden derhal feshedebilir",
            "D": "Geçerli neden iş ilişkisinin sürdürülmesini makul ölçüde etkiler ve süreli feshe dayanak olabilir; haklı neden ise ilişkinin çekilmezliği nedeniyle bildirim süresiz derhal feshe imkân verir",
            "E": "Geçerli fesih yalnız belirli süreli, haklı fesih yalnız belirsiz süreli sözleşmede uygulanır",
        }, "D",
        "Geçerli neden, iş güvencesi kapsamında süreli feshi haklılaştıran fakat md. 24-25 ağırlığına ulaşmayan nedendir. Haklı neden ise sözleşmenin sürdürülmesini çekilmez kılar ve bildirim süresi beklenmeden derhal feshe imkân verir.",
        "4857 sayılı İş Kanunu md. 17, 18, 24, 25",
    ),
    "0050": p(
        "İş sözleşmesinin sona ermesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Kanuni bildirim süreleri iki ile sekiz hafta arasında kıdeme göre artar. II. Kıdem tazminatı hesabında her tam yıl için otuz günlük ücret esası uygulanır. III. İş güvencesinde gösterilen geçerli nedeni ispat yükü kural olarak işverene aittir.",
        {"A": "I, II ve III", "B": "I ve II", "C": "II ve III", "D": "I ve III", "E": "Yalnız III"},
        "A",
        "Üç ifade de doğrudur: bildirim süresi kıdeme göre iki, dört, altı ve sekiz haftadır; kıdem tazminatı her tam yıl için otuz günlük ücret esasıyla hesaplanır; geçerli fesih nedenini işveren ispatlar.",
        "4857 sayılı İş Kanunu md. 17, 20; 1475 sayılı İş Kanunu md. 14",
    ),
    "0051": p(
        "Gerçek kişi işveren vefat etmiş; işletme mirasçılarca aynı faaliyetle sürdürülmektedir. İş sözleşmesi özellikle işverenin kişiliği dikkate alınarak kurulmamıştır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "İşverenin ölümü bütün iş sözleşmelerini ve doğmuş alacakları kendiliğinden ortadan kaldırır",
            "B": "Sözleşme yalnız işçi yeniden yazılı onay verirse geçmişe etkili devam eder",
            "C": "İşverenin ölümü kural olarak sözleşmeyi sona erdirmez; iş ilişkisi mirasçılarla devam edebilir, ancak sözleşme ağırlıklı olarak işverenin kişiliğine dayanıyorsa sona erebilir",
            "D": "İşverenin ölümü yalnız belirli süreli sözleşmeleri sona erdirir",
            "E": "İşverenin ölümü işçiye doğmuş ücret ve izin alacaklarını talep etme hakkı vermez",
        }, "C",
        "İşverenin ölümü iş sözleşmesini kural olarak sona erdirmez; miras ve hizmet ilişkisinin devrine ilişkin hükümler uygulanır. Sözleşme ağırlıklı olarak işverenin kişiliği dikkate alınarak kurulmuşsa ölümle sona erebilir.",
        "6098 sayılı TBK md. 441",
    ),
    "0052": p(
        "İşçinin sözleşmesi sona erdiğinde 18 günlük kullanılmamış yıllık izni bulunmaktadır. İşveren, fesih nedeninin işçinin md. 25/II kapsamındaki davranışı olduğunu ileri sürerek izin ücretini ödememiştir. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Md. 25/II feshi kullanılmamış izin ücretini de ortadan kaldırır",
            "B": "İzin ücreti yalnız işçi emeklilik nedeniyle ayrılırsa ödenir",
            "C": "Kullanılmayan izin ancak yeni işverende izin olarak kullandırılabilir",
            "D": "İzin alacağı yalnız sözleşme devam ederken nakden ödenebilir",
            "E": "Sona erme nedeni ne olursa olsun hak kazanılıp kullanılmayan izin süresinin ücreti, sona erme tarihindeki ücret üzerinden işçiye veya hak sahiplerine ödenir",
        }, "E",
        "İş sözleşmesinin herhangi bir nedenle sona ermesi hâlinde işçinin hak kazanıp kullanmadığı yıllık izin sürelerine ait ücret, sona erme tarihindeki ücret üzerinden kendisine veya hak sahiplerine ödenir. Md. 25/II feshi bu doğmuş hakkı ortadan kaldırmaz.",
        "4857 sayılı İş Kanunu md. 59",
    ),
    "0053": p(
        "İş sözleşmesi 1 Temmuz 2026’da sona eren işçi kıdem, ihbar ve kullanılmayan yıllık izin ücreti alacaklarını talep etmektedir. Zamanaşımı bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Bu alacaklarda kanuni zamanaşımı süresi kural olarak beş yıldır; sürenin başlangıcı ve kesilme-durma nedenleri her alacağın muacceliyetine göre ayrıca değerlendirilir",
            "B": "İşçilik alacakları hiçbir zaman zamanaşımına uğramaz",
            "C": "Bütün işçilik alacaklarında süre yüz yıldır ve taraflarca değiştirilemez",
            "D": "Zamanaşımı dolunca borç kendiliğinden ödenmiş sayılır ve yapılmış ödeme geri alınır",
            "E": "Kıdem, ihbar ve izin alacağı yalnız ceza davasında talep edilebilir",
        }, "A",
        "Kıdem ve ihbar tazminatı ile yıllık izin ücreti dâhil kanunda sayılan işçilik alacaklarında zamanaşımı kural olarak beş yıldır. Muacceliyet, geçiş hükümleri ve zamanaşımını kesen veya durduran nedenler ayrıca değerlendirilir.",
        "4857 sayılı İş Kanunu ek md. 3; 7036 sayılı Kanun geçici md. 8",
    ),
    "0054": p(
        "Aşağıdaki kavram–hukuki sonuç eşleştirmelerinden hangisi doğrudur?",
        {
            "A": "Kıdem tazminatı – bildirim süresine uymayan tarafın karşı tarafa ödediği tazminat",
            "B": "Kötüniyet tazminatı – iş güvencesi dışındaki belirsiz süreli çalışanın fesih hakkı kötüye kullanıldığında bildirim süresinin üç katı tutarında isteyebileceği tazminat",
            "C": "İşe başlatmama tazminatı – her tam kıdem yılı için otuz günlük ücret",
            "D": "İkale – işverenin işçinin kabulü olmadan yaptığı tek taraflı fesih",
            "E": "İhbar tazminatı – yalnız işçinin ölümü hâlinde mirasçılara yapılan ödeme",
        }, "B",
        "Kötüniyet tazminatı, iş güvencesi dışında kalan belirsiz süreli çalışanın sözleşmesi fesih hakkı kötüye kullanılarak sona erdirildiğinde bildirim süresinin üç katı tutarında doğabilir. Diğer seçenekler farklı kurumları birbirine karıştırmaktadır.",
        "4857 sayılı İş Kanunu md. 17",
    ),
    "0055": p(
        "İşveren işçinin ücretini üç aydır ödememiştir. İki yıl kıdemli işçi bu nedenle sözleşmesini derhal feshetmiştir. Tazminatlar bakımından aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Sözleşmeyi işçi feshettiği için ücret alacağı dâhil bütün haklarını kaybeder",
            "B": "İşçi kıdem tazminatı alamaz ve altı haftalık ihbar tazminatını işverene öder",
            "C": "Ücretin ödenmemesi yalnız geçerli neden oluşturur; işçiye derhal fesih hakkı vermez",
            "D": "Ücretin ödenmemesi haklı fesih nedenidir; işçi bir yıllık kıdem koşulunu taşıdığından kıdem tazminatı isteyebilir ve ihbar süresine bağlı değildir",
            "E": "Haklı fesih nedeniyle kıdem tazminatı kanunen iki kat ödenir",
        }, "D",
        "Ücretin kanun veya sözleşme koşullarına uygun hesaplanmaması ya da ödenmemesi işçiye haklı nedenle derhal fesih hakkı verir. En az bir yıllık kıdemi bulunan işçi kıdem tazminatı isteyebilir; haklı derhal fesihte ihbar süresi uygulanmaz.",
        "4857 sayılı İş Kanunu md. 24/II-(e); 1475 sayılı İş Kanunu md. 14",
    ),
    "0056": p(
        "İşveren, aynı nitelikte çalışanlardan yalnız belirli etnik kökene sahip olanların sözleşmesini feshetmiş; işçiler iş güvencesi kapsamı dışında kalmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "İş güvencesi dışında olmak ayrımcı feshi serbest hâle getirir",
            "B": "Fesihte eşit davranma borcuna aykırılık ve kötüniyet ayrı hukuki sonuçlar doğurabilir; iş güvencesi dışında kalmak işçiyi bütün korumalardan yoksun bırakmaz",
            "C": "Ayrımcılık yalnız işe alımda yasaktır; sözleşmenin sona ermesinde serbesttir",
            "D": "İşçiler yalnız işe iade tazminatı isteyebilir, ayrımcılık veya kötüniyet tazminatı isteyemez",
            "E": "İşveren bildirim süresine uyduysa fesih nedeni hiçbir biçimde denetlenemez",
        }, "B",
        "Eşit davranma borcu iş ilişkisinin sona ermesinde de uygulanır. Ayrımcı fesih ayrımcılık tazminatı ve diğer hakları; iş güvencesi dışındaki belirsiz süreli çalışanda koşulları varsa kötüniyet tazminatını gündeme getirebilir.",
        "4857 sayılı İş Kanunu md. 5, 17",
    ),
    "0057": p(
        "Yirmi işçi çalıştıran işyerindeki iki yıl kıdemli işçinin belirsiz süreli sözleşmesi, işveren aleyhine tanıklık yaptığı için altı haftalık bildirim süresine uyularak feshedilmiştir. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "İşçi otuz işçi koşulunu taşımadığı hâlde mutlaka işe iade edilir",
            "B": "Bildirim süresine uyulduğu için fesihte kötüniyet iddiası ileri sürülemez",
            "C": "İş güvencesi dışında kalan işçiye kıdem tazminatı hiçbir koşulda ödenmez",
            "D": "İşveren iş güvencesi dışındaki işçiyi yalnız md. 25/II nedeniyle çıkarabilir",
            "E": "İşçi iş güvencesi kapsamında olmasa da fesih hakkının kötüye kullanılması nedeniyle kötüniyet tazminatı ve koşulları varsa diğer feshe bağlı haklarını isteyebilir",
        }, "E",
        "Otuz işçi koşulu bulunmadığından işçi kural olarak işe iade hükümlerinden yararlanamaz. Bununla birlikte fesih hakkının kötüye kullanılması kötüniyet tazminatını; bir yıllık kıdem ve diğer koşullar kıdem tazminatını gündeme getirebilir.",
        "4857 sayılı İş Kanunu md. 17-18; 1475 sayılı İş Kanunu md. 14",
    ),
    "0058": p(
        "Bildirim süreleriyle ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Kanundaki süreler asgari olup sözleşmeyle artırılabilir. II. Bildirim süresine uymayan taraf karşı tarafa bu sürenin ücreti tutarında tazminat ödeyebilir. III. Haklı nedenle derhal fesihte bildirim süresinin dolması beklenmez.",
        {"A": "Yalnız I", "B": "I ve II", "C": "I, II ve III", "D": "II ve III", "E": "I ve III"},
        "C",
        "Üç ifade de doğrudur. Kanundaki bildirim süreleri asgaridir ve artırılabilir; uymayan taraf ihbar tazminatı öder; haklı nedenle derhal fesihte bildirim süresi uygulanmaz.",
        "4857 sayılı İş Kanunu md. 17, 24, 25",
    ),
    "0059": p(
        "İş sözleşmesinin sona ermesi bakımından aşağıdakilerden hangisi yanlıştır?",
        {
            "A": "İşçinin ölümü sözleşmeyi kendiliğinden sona erdirir ve koşulları varsa yakınlara TBK md. 440 ödemesi yapılır",
            "B": "İşe iade isteyen işçi fesih bildiriminin tebliğinden itibaren bir ay içinde arabulucuya başvurur",
            "C": "İşçi kendi hırsızlığı nedeniyle md. 25/II uyarınca çıkarılsa bile kıdem tazminatına hak kazanır",
            "D": "Kıdem tazminatı için kural olarak aynı işverene bağlı en az bir yıllık çalışma aranır",
            "E": "Ahlak ve iyi niyet nedenindeki altı iş günlük süre olayın öğrenildiği günden başlar",
        }, "C",
        "İşçinin hırsızlık gibi ahlak ve iyi niyet kurallarına aykırı davranışı nedeniyle md. 25/II uyarınca haklı fesih, kıdem tazminatına hak kazandırmaz. Diğer ifadeler doğrudur.",
        "4857 sayılı İş Kanunu md. 20, 25/II, 26; 1475 sayılı İş Kanunu md. 14; 6098 sayılı TBK md. 440",
    ),
    "0060": p(
        "İş sözleşmesinin sona ermesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Süreli fesihte bildirim süresi kıdeme göre belirlenir. II. İş güvencesi için kural olarak en az üç yıllık kıdem gerekir. III. Kıdem tazminatında her tam yıl için otuz günlük ücret esası uygulanır.",
        {"A": "Yalnız I", "B": "I ve II", "C": "II ve III", "D": "I, II ve III", "E": "I ve III"},
        "E",
        "I ve III doğrudur. İş güvencesinde kural olarak altı aylık kıdem aranır; yer altı işlerinde kıdem koşulu da yoktur. Üç yıllık kıdem şartı bulunmaz.",
        "4857 sayılı İş Kanunu md. 17-18; 1475 sayılı İş Kanunu md. 14",
    ),
}

# Öncüllü sorularda “Yalnız X hiçbir zaman doğru değil” ve I+III yığılması
# oluşmamalı. 0010 tek-doğru-öncül olacak biçimde kalibre edilir.
Q["0010"].update({
    "stem": "Fesih türleriyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Süreli fesih kural olarak belirsiz süreli sözleşmelerde bildirim süresine bağlıdır.\n\nII. Haklı nedenle derhal fesihte sözleşmenin sona ermesi için karşı tarafın kabulü gerekir.\n\nIII. İkale, işverenin tek taraflı fesih beyanıyla kurulur.",
    "options": {"A": "Yalnız I", "B": "I ve II", "C": "II ve III", "D": "I ve III", "E": "I, II ve III"},
    "solution": "Yalnız I doğrudur. Haklı nedenle derhal fesih tek taraflı yenilik doğuran irade beyanıdır ve karşı tarafın kabulünü gerektirmez. İkale ise tek taraflı fesih değil, tarafların karşılıklı sona erdirme anlaşmasıdır.",
})

# İlk sınav-zorluğu taslağında doğru seçenek, daha çok hukuki koşulu taşıdığı için
# 51 düz sorunun 45'inde en uzun kalmıştı. Aşağıdaki kalibrasyon dolgu eklemez:
# doğru seçeneği özlüleştirir veya kısa kalan çeldiricideki yanlış hukuk kuralını
# tam kurar. Böylece seçenekler aynı ayrıntı düzeyine gelir.
_OPTION_CALIBRATION = {
    "0002": {"B": "Haklı nedenle derhal fesih; işverenin geçerli neden göstermesiyle sözleşme bildirim süresi sonunda değil, beyanın ulaştığı anda sona erer"},
    "0004": {"C": "Bildirim süresinin yalnız kullanılmayan dört haftası için tazminat ödenir; kullandırılan iki hafta nedeniyle kanuni süre bölünebilir kabul edilir"},
    "0007": {"E": "A ve B ancak kanuni bildirim süresinin ücretini işverene peşin ödedikten sonra ayrılabilir; ücretin eksikliği veya tacize karşı önlem alınmaması derhal fesih doğurmaz"},
    "0008": {"D": "B’nin ticari sırrı rakibe açıklaması işveren açısından yalnız geçerli fesih nedeni sayılır; güven ilişkisinin ihlali hiçbir durumda haklı fesih ağırlığına ulaşmaz"},
    "0009": {"D": "Altı iş günlük hak düşürücü süre yalnız işçinin haklı fesih hakkına uygulanır; işveren ahlak ve iyi niyet nedenini öğrendiği tarihten başlayarak bir yıl içinde feshedebilir"},
    "0012": {"A": "Her işyerindeki çalışma ayrı bir sözleşmeye dayandığı için süreler birleştirilemez; sekiz ve yedi aylık dönemlerin hiçbiri tek başına bir yılı doldurmadığından kıdem hakkı doğmaz"},
    "0016": {"B": "İşçinin sendikaya üye olması işverenin yönetim hakkı kapsamında geçerli fesih nedeni oluşturur; buna karşılık ekonomik daralma ve belgeli performans düşüklüğü feshe dayanak olamaz"},
    "0017": {"D": "Bir aylık hak düşürücü süre arabuluculuk için değil doğrudan iş mahkemesinde açılacak dava için işler; arabulucuya ise mahkeme kararı kesinleştikten sonra başvurulur"},
    "0018": {"C": "İşe başlatmama tazminatı işçinin kıdeminden bağımsız olarak sabit on iki aylık ücrettir; boşta geçen süre ücretinde ise kararın kesinleşmesine kadar herhangi bir üst sınır uygulanmaz"},
    "0020": {"D": "İşverenin tek taraflı haklı fesih nedenine sahip olması", "E": "Sözleşmenin sona ermesi karşılığında işçiye sağlanan kıdem, ihbar ve ek menfaatlerin toplamı ile işçinin bu anlaşmayı kabul etmekte makul yararının bulunması"},
    "0022": {"C": "Bir yıl içinde evlilik nedeniyle fesih ve kıdem koşulları gerçekleştiğinden işçi kıdem tazminatı alabilir; bildirim süresi aranmaz", "D": "Kıdem tazminatı için evlilikten sonra en az beş yıl daha çalışılması ve bu sürenin sonunda işverenin yazılı onayıyla ayrılınması gerekir"},
    "0023": {"D": "Gerçeğe aykırı çalışma belgesi, işverenin yönetim hakkı kapsamında kaldığından zarar doğursa bile eski işverenin işçiye veya yanıltılan yeni işverene karşı sorumluluğuna yol açmaz"},
    "0024": {"B": "Kanuni koşullar bulunmadığından ibra kesin hükümsüzdür", "A": "İbra yazılı biçimde düzenlendiğinde sona erme tarihinden sonra bir ay geçmesi, alacak tür ve miktarlarının ayrı ayrı yazılması ve ödemenin banka aracılığıyla yapılması gerekmez"},
    "0027": {"E": "Haklı nedensiz istifa kıdem tazminatı doğurmaz; altı haftalık bildirim süresine uymayan işçiden işveren ihbar tazminatı isteyebilir", "B": "İşçinin tek taraflı istifası her durumda kıdem tazminatına hak kazandırır; bildirim süresine uyulmaması yalnız işe iade hakkını ortadan kaldırır, işveren lehine ihbar alacağı doğurmaz"},
    "0028": {"C": "Muvazzaf askerlik nedeniyle ayrılan işçinin kıdem tazminatı isteyebilmesi için askerlik dönüşünde aynı işveren yanında yeniden işe girip kesintisiz beş yıl daha çalışması gerekir"},
    "0029": {"E": "İşçinin davranışı md. 25/II ağırlığına ulaşmasa bile işverenin savunma almadan derhal fesih hakkı saklıdır; bu nedenle savunma şartı yalnız işletmesel fesihlerde uygulanır"},
    "0030": {"A": "Tarafların karşılıklı ve birbirine uygun irade açıklamalarıyla sözleşmeyi sona erdirmesi – işverenin tek taraflı süreli feshi"},
    "0031": {"D": "İşveren bildirim ücretini peşin ödeyebilir; iş güvencesi koşulları yine uygulanır", "E": "Bildirim süresi ücretinin peşin ödenmesiyle işçinin o tarihe kadar doğmuş kıdem tazminatı ve kullanılmayan yıllık izin ücreti alacakları sona erer; ayrıca ödeme yapılmaz"},
    "0034": {"A": "İşin bir haftadan fazla durmasını gerektiren zorlayıcı sebep işçiye haklı fesih hakkı verir; ilk hafta yarım ücret ödenir", "B": "İşyerinde işi bir haftadan fazla durduran zorlayıcı neden yalnız işverene bildirim süresiz fesih hakkı verir; işçi işin yeniden başlamasını süresiz beklemekle yükümlüdür"},
    "0036": {"C": "İşçi süresinde arabulucuya başvurmuş olsa bile görüşmelerde anlaşma sağlanmaması işe iade talebini kesin olarak sona erdirir; son tutanaktan sonra mahkemeye başvurulamaz"},
    "0037": {"C": "Yalnız bir ay içinde iki ayrı tatil gününden sonraki iş günü yapılan devamsızlık feshe dayanak olabilir; ardı ardına iki iş günü devamsızlık kanunda sayılan eşiklerden değildir"},
    "0038": {"C": "A’nın performansa dayalı feshinden önce savunması alınır; B’nin işletmesel feshinde aranmaz, C yönünden md. 25/II hakkı saklıdır", "E": "İşçinin savunmasının alınması, işverenin fesih nedenini yazılı bildirimde açık ve kesin biçimde gösterme yükümlülüğünü kaldırır; savunma tutanağı tek başına fesih bildirimi yerine geçer"},
    "0041": {"E": "İşin niteliğinden doğan ve hekim raporuyla doğrulanan sağlık tehlikesi, işçi yönünden haklı fesih nedeni oluşturmaz; işçi sağlığı ağır biçimde bozulsa bile sözleşmeyi sürdürmelidir"},
    "0043": {"B": "İşçinin aynı işverene ait her işyerine geçişinde kıdemi yeniden başlar; iki yıl, bir yıl ve altı aylık dönemler birbirinden bağımsız olduğundan yalnız son altı aylık süre hesaba katılır"},
    "0044": {"C": "İşveren yargılamada bildirimde göstermediği yeni nedenlerle feshi geçerli kılabilir", "E": "İşverenin yazılı bildirimde işletmesel neden göstermesi yeterlidir; küçülme kararının gerçekliği, tutarlı uygulanıp uygulanmadığı ve görünürdeki nedenin hamileliği gizleyip gizlemediği yargısal denetime tabi değildir"},
    "0045": {"D": "Devamsızlık bildirim süresini aşarsa işveren md. 25/IV uyarınca derhal feshedebilir; koşulları varsa kıdem hakkı saklıdır", "A": "İşçinin işyeri dışındaki bir olay nedeniyle gözaltına alınması veya tutuklanması, devamsızlığın süresine ve mahkûmiyet bulunup bulunmadığına bakılmadan ilk günden md. 25/II kapsamında değerlendirilir"},
    "0046": {"B": "İşveren gösterdiği geçerli nedeni; işçi ise feshin başka nedene dayandığı iddiasını ispatlar", "E": "İşçi sendikal neden iddiasında bulunduğu anda işverenin performans düşüklüğüne ilişkin gösterdiği neden ve deliller inceleme dışı kalır; fesih başka araştırma yapılmadan geçersiz sayılır"},
    "0047": {"E": "İşe iade ile işçi veya işveren alacağı ve tazminatı davalarında, kanuni istisnalar dışında arabulucuya başvuru dava şartıdır", "D": "Dava şartı arabuluculuğa hiç başvurulmadan açılan işe iade ve işçilik alacağı davaları usul eksikliğine rağmen doğrudan esastan incelenir; mahkeme arabuluculuk noksanlığını gözetemez"},
    "0048": {"C": "İşletmesel kararın gerçekliği, tutarlı uygulanması ve feshin son çare olması denetlenebilir; feshe bağlı haklar ayrıca değerlendirilir", "A": "İşveren satışların azaldığını ileri sürdüğünde fesih kendiliğinden geçerli olur; aynı işi görenler arasındaki seçimin, yeni işçi alımının, fazla çalışmanın veya alternatif pozisyonların ayrıca incelenmesi mümkün değildir"},
    "0049": {"D": "Geçerli neden süreli feshe; ilişkiyi çekilmez kılan haklı neden ise bildirim süresiz derhal feshe dayanak olur", "C": "Belgelenen her performans düşüklüğü, ağırlığına ve iş ilişkisinin sürdürülüp sürdürülemeyeceğine bakılmadan md. 25/II kapsamında değerlendirilir ve işveren kıdem ile ihbar tazminatı ödemeden derhal fesheder"},
    "0052": {"E": "Sona erme nedeni ne olursa olsun kullanılmayan izin ücreti sona erme tarihindeki ücret üzerinden işçiye veya hak sahiplerine ödenir", "C": "Kullanılmayan yıllık izin süreleri iş sözleşmesi sona erdikten sonra yeni işveren yanında aynen izin olarak kullandırılır; eski işverenin bu süreleri ücrete çevirme veya ödeme yükümlülüğü yoktur"},
    "0053": {"A": "Bu alacaklarda zamanaşımı kural olarak beş yıldır; muacceliyet ve süreyi etkileyen nedenler ayrıca değerlendirilir", "D": "Beş yıllık zamanaşımı süresi dolduğunda borç yalnız dava edilemez hâle gelmez, kendiliğinden ifa edilmiş sayılır; işverenin süre geçtikten sonra yaptığı ödeme sebepsiz zenginleşme olarak geri istenir"},
    "0054": {"B": "Kötüniyet tazminatı – iş güvencesi dışındaki belirsiz süreli çalışanın fesih hakkı kötüye kullanıldığında bildirim süresinin üç katı tutarında isteyebileceği tazminat", "D": "İkale – işverenin işçiye bildirim süresi vermeden açıkladığı, işçinin kabul veya imzasına ihtiyaç bulunmayan ve tek taraflı olarak sözleşmeyi sona erdiren olağan fesih beyanı"},
    "0055": {"D": "Ücretin ödenmemesi haklı fesih nedenidir; bir yıllık kıdemi bulunan işçi kıdem tazminatı isteyebilir", "C": "Ücretin üç ay boyunca hiç ödenmemesi işçiye haklı derhal fesih hakkı vermez; işçi önce kanuni bildirim süresini çalışmalı, ayrılırsa işverene ihbar tazminatı ödemeli ve kıdem hakkından vazgeçmelidir"},
    "0057": {"E": "İşçi işe iade kapsamında olmasa da kötüniyet tazminatı ile koşulları varsa diğer feshe bağlı haklarını isteyebilir", "D": "Otuzdan az işçi çalıştıran işyerinde işveren, belirsiz süreli iş sözleşmesini yalnız işçinin md. 25/II kapsamındaki davranışını ispatlarsa sona erdirebilir; süreli fesih ve bildirim süresi kuralları uygulanmaz"},
}
for _qid, _options in _OPTION_CALIBRATION.items():
    Q[_qid]["options"].update(_options)


# Elle bilişsel sınıflandırma: 0 tanıma, 1 tek kural, 2 çoklu ayrım, 3 bütünleşik olay.
LEVELS = {
    0: set(),
    1: {"0002", "0014", "0030", "0042"},
    3: {
        "0004", "0005", "0007", "0008", "0009", "0011", "0015", "0017",
        "0018", "0020", "0022", "0024", "0026", "0027", "0029", "0031", "0032",
        "0034", "0036", "0037", "0038", "0044", "0045", "0046", "0048", "0049",
        "0051", "0052", "0053", "0055", "0056", "0057",
    },
}
LEVELS[2] = set(Q) - set().union(*LEVELS.values())
assert len(Q) == 60 and set().union(*LEVELS.values()) == set(Q)
assert len(LEVELS[0]) <= 6 and len(LEVELS[0] | LEVELS[1]) <= 24
for start in (1, 21, 41):
    block = {f"{n:04d}" for n in range(start, start + 20)}
    assert len(block & LEVELS[2]) >= 8
    assert len(block & LEVELS[3]) >= 4

PATCHES = {"ish-sona-gen-" + key: value for key, value in Q.items()}


def apply(path: Path, write: bool) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data if isinstance(data, list) else data["questions"]
    by_id = {q["id"]: q for q in questions}
    diffs = []
    for qid, expected in PATCHES.items():
        if qid not in by_id:
            raise SystemExit(f"Soru bulunamadı: {path}::{qid}")
        q = by_id[qid]
        for field, value in expected.items():
            if q.get(field) != value:
                diffs.append(f"{path}::{qid}.{field}")
                if write:
                    q[field] = value
        if write and (set(q["options"]) != set("ABCDE") or len(set(q["options"].values())) != 5):
            raise SystemExit(f"Seçenek kusuru: {path}::{qid}")
    if write:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return diffs


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()
    diffs = []
    for path in (ROOT / REL, APP_ROOT / REL):
        diffs.extend(apply(path, args.write))
    if args.check and diffs:
        print("Eşleşmeyen alanlar:")
        print("\n".join(f"- {x}" for x in diffs[:20]))
        return 1
    print(f"1 paket / {len(PATCHES)} soru iki repoda doğrulandı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
