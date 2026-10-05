#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Haksiz Fiil — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Borclar hukuku gercek sinav profiliyle yeniden yazim (eski surumde 103 celdirici mutlak ifadeliydi, kor %51): kusur sorumlulugu ve ispat, indirim, olum ve bedensel zarar (7589 ile m. 55'e eklenen faiz ve mahsup fikralari dahil), manevi tazminat, sorumluluk sebeplerinin coklugu, hukuka aykiriligi kaldiran haller, kusursuz sorumluluk halleri, zamanasimi ve yargilama. Gercek sinavda sorulan kaliplar olaya cevrildi; 6 hesap sorusu bagimsiz dogrulandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 6098 sayili Turk Borclar Kanunu m. 49-76 guncel metni (mevzuat.gov.tr)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/borclar_hukuku/haksiz_fiil.json"
STYLE_REF = 'SGS Borclar Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "hakfiil-gen-"


def patch(stem, options, answer, solution, ref='6098 sayili Turk Borclar Kanunu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "A, yalnızca komşusu B'nin manzarasını kapatmak amacıyla kendi arsasına kendisine hiçbir yararı olmayan yüksek bir duvar örmüştür. Duvar, imar mevzuatına uygundur. B'nin tazminat istemi hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'B, ancak sözleşmeye aykırılık hükümlerine dayanabilir',
            'B': 'Ahlaka aykırı fiille kasten zarar verildiğinden A sorumludur',
            'C': 'Yasaklayan bir hukuk kuralı bulunmadığından A, kastı olsa bile sorumlu olmaz',
            'D': 'A, ancak duvar imar mevzuatına aykırıysa sorumlu olur',
            'E': "A'nın sorumluluğu kusursuz sorumluluk hâlidir",
        },
        'B',
        "TBK m. 49/2'ye göre **zarar verici fiili yasaklayan bir hukuk kuralı bulunmasa bile, ahlaka aykırı bir fiille başkasına kasten zarar veren** de bu zararı gidermekle yükümlüdür. A'nın tek amacı B'ye zarar vermek olduğundan sorumluluk doğar.",
        '6098 sayılı TBK m. 49/2',
    ),
    # düzey 2
    '0002': patch(
        'Zarar kavramına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Manevi zarar, kişilik değerlerinde meydana gelen eksilmedir',
            'B': 'Yoksun kalınan kâr, beklenen artışın fiil nedeniyle engellenmesidir',
            'C': 'Fiili zarar, malvarlığında gerçekleşen azalmadır',
            'D': 'Zarar, zarar görenin iradesi dışında gerçekleşen bir eksilmedir',
            'E': 'Yoksun kalınan kâr haksız fiil tazminatına dâhil edilemez',
        },
        'E',
        'Haksız fiilde tazmin edilen maddi zarar, **fiili zarar** (mevcut malvarlığındaki azalma) ile **yoksun kalınan kârı** (beklenen artışın engellenmesi) birlikte kapsar; nitekim m. 54 kazanç kaybını bedensel zarar kalemleri arasında sayar.',
        '6098 sayılı TBK m. 49',
    ),
    # düzey 3
    '0003': patch(
        'Zarara ağır kusuruyla sebep olan kişi, tazminatı ödediğinde yoksulluğa düşeceğini ileri sürerek indirim istemektedir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yoksulluğa düşecek her yükümlü için, kusurun derecesine bakılmaksızın indirim yapılır',
            'B': 'Hâkim tazminatı tamamen kaldırmakla yükümlüdür',
            'C': 'Tazminat irat biçimine çevrilerek yarıya indirilir',
            'D': 'Yoksulluk sebebiyle indirim hafif kusur şartına bağlı olduğundan uygulanmaz',
            'E': 'İndirim, zarar görenin onayına bağlıdır',
        },
        'D',
        "TBK m. 52/2'ye göre yoksulluk sebebiyle indirim için **zarara hafif kusuruyla sebep olma**, tazminat ödendiğinde yoksulluğa düşme ve hakkaniyetin gerektirmesi birlikte aranır. Ağır kusurlu yükümlü bu hükümden yararlanamaz.",
        '6098 sayılı TBK m. 52/2',
    ),
    # düzey 2
    '0004': patch(
        'Bir iş kazasında ağır yaralanarak kalıcı olarak yatağa bağlı kalan işçinin eşi, kendisi için manevi tazminat istemektedir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yakınlar manevi tazminatı ancak zarar görenin mirasçısı olarak isteyebilir',
            'B': 'Ağır bedensel zarar hâlinde yakınlara da manevi tazminat verilebilir',
            'C': 'Manevi tazminatı ancak zarar gören kişi isteyebilir',
            'D': 'Yakınlar ancak ölüm hâlinde manevi tazminat isteyebilir',
            'E': 'Eşin istemi destekten yoksun kalma tazminatıdır',
        },
        'B',
        "TBK m. 56/2'ye göre **ağır bedensel zarar veya ölüm hâlinde, zarar görenin veya ölenin yakınlarına da** manevi tazminat olarak uygun bir miktar paranın ödenmesine karar verilebilir.",
        '6098 sayılı TBK m. 56/2',
    ),
    # düzey 3
    '0005': patch(
        "Bir davette içeceğine haberi olmadan uyuşturucu madde katılan A, ayırt etme gücünü geçici olarak yitirmiş ve bu sırada B'nin arabasına zarar vermiştir.\n\nTBK'ya göre A'nın sorumluluğuyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Ayırt etme gücünü geçici kaybeden kural olarak zarardan sorumludur',
            'B': 'Kaybetmede kusursuzluğunu ispat eden sorumluluktan kurtulur',
            'C': "Kusursuzluğu ispat yükü A'ya aittir",
            'D': 'İçeceğe habersiz madde katılması kusursuzluğu gösterebilir',
            'E': 'Ayırt etme gücü bulunmadığından sorumluluk hiç doğmaz',
        },
        'E',
        'TBK m. 59: ayırt etme gücünü geçici olarak kaybeden kişi, bu sırada verdiği zararları gidermekle yükümlüdür; ancak ayırt etme gücünü kaybetmede kusuru olmadığını ispat ederse sorumluluktan kurtulur. İspat yükü zarar verendedir.',
        '6098 sayılı TBK m. 59',
    ),
    # düzey 3
    '0006': patch(
        "Müteselsil sorumlulardan A, tazminatın tamamını 1 Mart 2026'da ödemiş; birlikte sorumlu olan B'nin kimliğini o gün bilmektedir. A'nın rücu istemi en geç hangi tarihte zamanaşımına uğrar?",
        {
            'A': '1 Mart 2036',
            'B': '31 Aralık 2027',
            'C': '1 Mart 2027',
            'D': '1 Mart 2028',
            'E': '1 Mart 2031',
        },
        'D',
        "TBK m. 73'e göre rücu istemi, **tazminatın tamamının ödendiği ve birlikte sorumlu kişinin öğrenildiği tarihten başlayarak iki yılın** ve her hâlde ödeme tarihinden başlayarak on yılın geçmesiyle zamanaşımına uğrar: **1 Mart 2028**.",
        '6098 sayılı TBK m. 73',
    ),
    # düzey 2
    '0007': patch(
        'Aynı zarardan birden çok kişinin sorumlu olmasına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Aynı zarardan çeşitli sebeplerle sorumlu olanlar da müteselsilen sorumludur',
            'B': 'Payından fazlasını ödeyen diğerlerine rücu edebilir',
            'C': 'Fazla ödeyen, zarar görenin haklarına halef olmaz',
            'D': 'Birlikte zarar verenler müteselsilen sorumludur',
            'E': 'İç ilişkide yaratılan tehlikenin yoğunluğu da gözetilir',
        },
        'C',
        "TBK m. 62/2'ye göre tazminatın kendi payına düşeninden fazlasını ödeyen kişi, bu fazla ödemesi için diğer müteselsil sorumlulara karşı **rücu hakkına sahip ve zarar görenin haklarına halef olur**.",
        '6098 sayılı TBK m. 61, 62',
    ),
    # düzey 3
    '0008': patch(
        'Kolluk görevlisi, kaçmaya çalışmayan ve direnmeyen bir şüpheliyi yakalarken gereğinden fazla güç kullanarak onu yaralamıştır. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kamusal yarar her türlü gücü hukuka uygun kılar',
            'B': 'Fiil haklı savunma olarak değerlendirilir',
            'C': 'Yakalama yetkisi bulunduğundan, kullanılan gücün ölçüsüne bakılmaksızın fiil hukuka uygundur',
            'D': 'Yetki sınırı aşıldığından aşan kısım bakımından fiil hukuka aykırıdır',
            'E': 'Şüpheli olmak rıza sayıldığından fiil hukuka uygundur',
        },
        'D',
        'TBK m. 63/1 kanundan doğan yetkinin kullanılmasını ancak fiil **bu yetkinin sınırları içinde kaldığı** sürece hukuka uygun sayar. Sınırı aşan güç kullanımı hukuka uygunluk sebebinin kapsamı dışındadır.',
        '6098 sayılı TBK m. 63/1',
    ),
    # düzey 3
    '0009': patch(
        'Ayırt etme gücü bulunmayan varlıklı bir kişi, geliri düşük bir esnafın dükkânına ağır zarar vermiştir. Esnafın tazminat istemi hakkında aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Hâkim hakkaniyet gerektiriyorsa giderime karar verebilir',
            'B': 'Bu sorumluluk kusur aranmayan bir sorumluluk hâlidir',
            'C': 'Hâkim zararın tamamının veya bir kısmının giderilmesine karar verebilir',
            'D': 'Tarafların ekonomik durumları hakkaniyet değerlendirmesinde önemlidir',
            'E': 'Ayırt etme gücü olmayan kişiden tazminat istenemez',
        },
        'E',
        "TBK m. 65'e göre **hakkaniyet gerektiriyorsa hâkim, ayırt etme gücü bulunmayan kişinin verdiği zararın tamamen veya kısmen giderilmesine** karar verir. Bu, kusur aranmayan hakkaniyet sorumluluğudur.",
        '6098 sayılı TBK m. 65',
    ),
    # düzey 3
    '0010': patch(
        'Bir fabrikada üretim hattının düzensiz işleyişi nedeniyle, hangi işçinin hatasından kaynaklandığı belirlenemeyen bir zarar üçüncü kişiye verilmiştir. İşletme sahibinin sorumluluğu hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sorumluluk işçiler arasında eşit paylaştırılır',
            'B': 'İşçileri seçerken gerekli özeni gösterdiğini ispatlaması sorumluluktan kurtulması için yeterlidir',
            'C': 'Çalışma düzeninin zararı önlemeye elverişli olduğunu ispat etmedikçe sorumludur',
            'D': 'Zarar gören işçilerin kusurunu ispat etmedikçe tazminat alamaz',
            'E': 'Zarar veren işçi belirlenemediğinden sorumlu tutulamaz',
        },
        'C',
        "TBK m. 66/3'e göre **bir işletmede adam çalıştıran, işletmenin çalışma düzeninin zararın doğmasını önlemeye elverişli olduğunu ispat etmedikçe**, işletmenin faaliyetleri dolayısıyla sebep olunan zararı gidermekle yükümlüdür; zarar veren çalışanın belirlenmesi gerekmez.",
        '6098 sayılı TBK m. 66/3',
    ),
    # düzey 2
    '0011': patch(
        'A, tatile giden komşusunun köpeğine bir hafta bakmayı üstlenmiş; köpek bu sırada bir yoldaşı ısırmıştır. Aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Hayvanın maliki olmadığından A sorumlu tutulamaz',
            'B': "A'nın sorumluluğu özen sorumluluğudur",
            'C': 'Bakımı geçici olarak üstlenen A hayvan bulunduran sayılır',
            'D': 'A, gerekli özeni gösterdiğini ispat ederse sorumlu olmaz',
            'E': "Hayvan başkası tarafından ürkütülmüşse A'nın o kişiye rücu hakkı vardır",
        },
        'A',
        "TBK m. 67'ye göre **bir hayvanın bakımını ve yönetimini sürekli veya geçici olarak üstlenen kişi**, hayvanın verdiği zararı gidermekle yükümlüdür; mülkiyet şartı yoktur. Gerekli özeni ispat eden sorumlu olmaz; hayvan başkası tarafından ürkütülmüşse o kişiye rücu hakkı saklıdır.",
        '6098 sayılı TBK m. 67',
    ),
    # düzey 3
    '0012': patch(
        'Bir binanın bakımındaki eksiklikten doğan zarardan aşağıdakilerden hangileri sorumludur?\n\nI. Binanın maliki\n\nII. Binada intifa hakkına sahip olan kişi\n\nIII. Binada kira sözleşmesiyle oturan kişi',
        {
            'A': 'I ve III',
            'B': 'Yalnız I',
            'C': 'Yalnız II',
            'D': 'I, II ve III',
            'E': 'I ve II',
        },
        'E',
        "TBK m. 69'a göre yapı maliki, yapımdaki bozukluklardan veya bakımdaki eksikliklerden doğan zararı gidermekle yükümlüdür; **intifa ve oturma hakkı sahipleri de bakımdaki eksikliklerden doğan zararlardan malikle birlikte müteselsilen** sorumludur. Kiracı bu sayımda yer almaz.",
        '6098 sayılı TBK m. 69',
    ),
    # düzey 2
    '0013': patch(
        'Önemli ölçüde tehlike arz eden işletmelere ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. İşletme sahibi ile işletenin sorumluluğu kusur oranında paylaştırılarak dış ilişkide bölünür\n\nII. Faaliyete hukuk düzenince izin verilmişse denkleştirme istenemez\n\nIII. Özel kanunda benzer tehlikeler için sorumluluk öngörülen işletmeler de bu nitelikte sayılır',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'Yalnız III',
            'E': 'I, II ve III',
        },
        'D',
        "TBK m. 71'e göre sahip ve işleten dış ilişkide **müteselsilen** sorumludur (I yanlış); izinli faaliyette de zarar görenler **denkleştirme** isteyebilir (II yanlış); **herhangi bir kanunda benzeri tehlikeler için özel sorumluluk öngörülen işletmeler de** önemli ölçüde tehlikeli sayılır (III).",
        '6098 sayılı TBK m. 71',
    ),
    # düzey 2
    '0014': patch(
        'Özen sorumluluğu hâllerine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Adam çalıştıran, gerekli özeni ispat ederek sorumluluktan kurtulabilir',
            'B': 'Yapı maliki, kendisine karşı sorumlu olan müteahhide rücu edebilir',
            'C': 'İntifa hakkı sahibi bakım eksikliğinden malikle müteselsilen sorumludur',
            'D': 'Adam çalıştıran, çalışanın verdiği zararı kusursuz olsa bile tamamen çalışana yükler',
            'E': 'Hayvan bulunduran, zararın doğmasını engellemek için gerekli özeni ispat ederek sorumluluktan kurtulabilir',
        },
        'D',
        "TBK m. 66/4'e göre adam çalıştıran, ödediği tazminat için çalışana **ancak onun bizzat sorumlu olduğu ölçüde** rücu edebilir. Özen ispatıyla kurtuluş m. 66/2 ve 67/2'de, intifa hakkı sahibinin müteselsil sorumluluğu ve rücu hakkı m. 69'da düzenlenmiştir.",
        '6098 sayılı TBK m. 66, 67, 69',
    ),
    # düzey 3
    '0015': patch(
        'Bir fabrikanın 2014 yılında toprağa gömdüğü kimyasal atıklar, 2025 yılında komşu arazideki su kuyusunu kirletmiş ve zarar ile sorumlu aynı yıl öğrenilmiştir. Fiil ceza zamanaşımı daha uzun bir suç değildir. Tazminat istemi hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Zarar sonradan doğduğundan zamanaşımı işlemez',
            'B': 'Fiilden itibaren on yıl geçtiğinden istem zamanaşımına uğramıştır',
            'C': 'İstem yirmi yıl içinde ileri sürülebilir',
            'D': "Zamanaşımı zararın doğduğu 2025'ten itibaren on yıldır",
            'E': 'Öğrenmeden itibaren iki yıl içinde istenebilir',
        },
        'B',
        "TBK m. 72'ye göre iki yıllık süre öğrenmeden başlasa da istem **her hâlde fiilin işlendiği tarihten başlayarak on yılın** geçmesiyle zamanaşımına uğrar. 2014'teki fiilden itibaren on yıl 2024'te dolmuştur.",
        '6098 sayılı TBK m. 72',
    ),
    # düzey 3
    '0016': patch(
        'Ağır yaralanan ve geliri kesilen davacının istemi üzerine hâkim, davalının geçici ödeme yapmasına karar vermiş; yargılama sonunda ise tazminat istemi reddedilmiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Davacı, tazminat reddedilse de aldığı geçici ödemeleri iade etmez',
            'B': 'Geçici ödeme için inandırıcı kanıt ve ekonomik durum birlikte aranır',
            'C': 'Hâkim davacının geçici ödemeleri yasal faiziyle iadesine karar verir',
            'D': 'Geçici ödeme davacının istemi üzerine kararlaştırılır',
            'E': 'Tazminata hükmedilseydi geçici ödemeler tazminattan mahsup edilirdi',
        },
        'A',
        "TBK m. 76'ya göre zarar gören inandırıcı kanıtlar sunar ve ekonomik durumu da gerektirirse hâkim, **istem üzerine** geçici ödemeye karar verebilir. Ödemeler hükmedilen tazminata mahsup edilir; **tazminata hükmedilmezse hâkim, geçici ödemelerin yasal faiziyle geri verilmesine** karar verir.",
        '6098 sayılı TBK m. 76',
    ),
    # düzey 2
    '0017': patch(
        'Aşağıdakilerden hangileri bedensel zarar ve manevi tazminata ilişkin olarak doğrudur?\n\nI. Rücu edilemeyen sosyal güvenlik ödemeleri tazminattan indirilir\n\nII. Ağır bedensel zararda zarar görenin yakınları da manevi tazminat isteyebilir\n\nIII. Bedensel bütünlüğü zedelenen kişiye manevi tazminat verilebilir',
        {
            'A': 'II ve III',
            'B': 'Yalnız II',
            'C': 'Yalnız III',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'A',
        "TBK m. 55'e göre **kısmen veya tamamen rücu edilemeyen sosyal güvenlik ödemeleri zarar veya tazminattan indirilemez** (I yanlış). m. 56'ya göre bedensel bütünlüğü zedelenene (III) ve ağır bedensel zarar veya ölümde yakınlara (II) manevi tazminat verilebilir.",
        '6098 sayılı TBK m. 55, 56',
    ),
    # düzey 2
    '0018': patch(
        'Kusur sorumluluğunun unsurlarına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kusur, kast veya ihmal biçiminde olabilir; ihmalin ağırlığı tazminatın belirlenmesinde gözetilir',
            'B': 'Bir zarar doğmuş olmalıdır',
            'C': 'Zarar verenin kusuru bulunmalıdır',
            'D': 'Fiil hukuka aykırı olmalıdır',
            'E': 'Fiil ile zarar arasında herhangi bir bağ bulunması yeterlidir, uygunluk aranmaz',
        },
        'E',
        'Haksız fiilin unsurları **fiil, zarar, hukuka aykırılık, kusur ve fiil ile zarar arasında uygun illiyet bağıdır**. Her türlü bağ yeterli değildir; fiilin olayların olağan akışına göre o zararı doğurmaya elverişli olması gerekir.',
        '6098 sayılı TBK m. 49',
    ),
    # düzey 3
    '0019': patch(
        "Fiil 1 Haziran 2017'de işlenmiş, zarar gören zararı ve faili 1 Mart 2026'da öğrenmiştir. Fiil ceza zamanaşımı daha uzun bir suç değildir. Tazminat istemi en geç hangi tarihte zamanaşımına uğrar?",
        {
            'A': '1 Mart 2036',
            'B': '1 Haziran 2027',
            'C': '1 Mart 2027',
            'D': '1 Haziran 2037',
            'E': '1 Mart 2028',
        },
        'B',
        "TBK m. 72'ye göre istem, öğrenmeden itibaren iki yıl (1 Mart 2028) ve **her hâlde fiilden itibaren on yıl** (1 Haziran 2027) geçmekle zamanaşımına uğrar; hangisi önce dolarsa o esas alınır: **1 Haziran 2027**.",
        '6098 sayılı TBK m. 72',
    ),
    # düzey 2
    '0020': patch(
        'Başkasının hayvanının taşınmazında verdiği zarara karşı taşınmaz zilyedinin haklarına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Zilyet, zarar veren hayvanı yakalayabilir',
            'B': 'Koşullar haklı gösteriyorsa hayvan başka yollarla etkisiz hâle getirilebilir',
            'C': 'Zilyet, zarar giderilinceye kadar hayvanı alıkoyabilir',
            'D': 'Zilyet, alıkoyduğu hayvanın sahibine bilgi vermekle yükümlü değildir',
            'E': 'Sahip bilinmiyorsa zilyet onun bulunması için girişimde bulunur',
        },
        'D',
        "TBK m. 68/2'ye göre taşınmazın zilyedi **derhâl hayvan sahibine bilgi vermek** ve sahibini bilmiyorsa onun bulunması için gerekli girişimleri yapmakla yükümlüdür.",
        '6098 sayılı TBK m. 68',
    ),
    # düzey 3
    '0021': patch(
        "Hiçbir hukuk kuralını ihlal etmeyen ancak ahlaka aykırı sayılan bir davranış, dikkatsizlik sonucu başkasına zarar vermiştir. Zarar görenin m. 49/2'ye dayanan istemi hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Hâkim hakkaniyet sorumluluğuna göre karar verir',
            'B': 'Dikkatsizlik hâlinde tazminat yarı oranda ödenir',
            'C': 'Ahlaka aykırılık yeterli olduğundan istem kabul edilir',
            'D': 'Fiilin ahlaka aykırılığı kusur karinesi doğurur',
            'E': 'm. 49/2 kast aradığından istem bu hükme dayandırılamaz',
        },
        'E',
        'TBK m. 49/2, hukuk kuralıyla yasaklanmamış ahlaka aykırı fiillerde sorumluluğu **kasten zarar verme** şartına bağlar. İhmalle verilen zararda bu hüküm uygulanmaz; m. 49/1 ise hukuka aykırılık arar.',
        '6098 sayılı TBK m. 49/2',
    ),
    # düzey 2
    '0022': patch(
        "Misafir olarak bulunduğu evde dikkatsizlikle B'ye ait antika bir vazoyu kıran A aleyhine B tazminat davası açmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Vazonun değeri tam ispat edilemezse hâkim hakkaniyete göre belirler',
            'B': "B, A'nın kusurunu ispat etmelidir",
            'C': 'B, uğradığı zararı ispat etmelidir',
            'D': "A'nın kusurunun ağırlığı tazminatın kapsamını etkiler",
            'E': 'A, kusursuz olduğunu ispat edemezse kusurlu sayılır',
        },
        'E',
        "TBK m. 50'ye göre **zarar gören, zararını ve zarar verenin kusurunu ispat yükü altındadır**; kusur sorumluluğunda kusur karinesi yoktur. Zararın miktarı tam ispat edilemiyorsa hâkim hakkaniyete göre belirler; m. 51'e göre kusurun ağırlığı tazminatın kapsamını etkiler.",
        '6098 sayılı TBK m. 50, 51',
    ),
    # düzey 2
    '0023': patch(
        "Aşağıdakilerden hangileri ölüm hâlinde TBK m. 53'e göre tazmini istenebilecek zararlardandır?\n\nI. Ölenin ekonomik geleceğinin sarsılmasından doğan kayıp\n\nII. Cenaze giderleri\n\nIII. Ölenin desteğinden yoksun kalanların kayıpları",
        {
            'A': 'Yalnız II',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'B',
        "TBK m. 53'e göre ölüm hâlinde zararlar: **cenaze giderleri**, ölüm hemen gerçekleşmemişse tedavi giderleri ve çalışma gücü kayıpları ile **ölenin desteğinden yoksun kalanların kayıplarıdır**. Ekonomik geleceğin sarsılması m. 54'te bedensel zarar kalemi olarak sayılır.",
        '6098 sayılı TBK m. 53',
    ),
    # düzey 3
    '0024': patch(
        "Bir gazete, B hakkında gerçeğe aykırı ve onur kırıcı bir haber yayımlamıştır. B'nin açtığı davada hâkimin verebileceği kararlara ilişkin aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Para yerine saldırıyı kınayan bir karar verebilir',
            'B': 'Kınama kararının yayımlanmasına hükmedebilir',
            'C': 'Manevi zarara karşılık manevi tazminat adı altında bir miktar para ödenmesine karar verebilir',
            'D': 'Kınama kararını paraya ek olarak verebilir',
            'E': 'Manevi tazminat ancak maddi zarar da ispat edilirse verilebilir',
        },
        'E',
        "TBK m. 58'e göre kişilik hakkının zedelenmesinden zarar gören, **uğradığı manevi zarara karşılık** manevi tazminat isteyebilir; maddi zararın ispatı şart değildir. Hâkim paranın yerine başka bir giderim biçimi kararlaştırabilir veya bunu paraya ekleyebilir; kınama kararı verip yayımlanmasına hükmedebilir.",
        '6098 sayılı TBK m. 58',
    ),
    # düzey 3
    '0025': patch(
        'Özel bir hastanede ameliyat edilen hastanın zararı hem hasta ile hastane arasındaki sözleşmeye hem de haksız fiile dayandırılabilmektedir. Hasta aksini istememiştir. Hâkim nasıl karar verir?',
        {
            'A': 'Sözleşme varsa haksız fiil hükümleri uygulanamaz',
            'B': 'Zarar veren lehine olan sebebe göre',
            'C': 'Her iki sebebe göre ayrı ayrı hesaplanan tazminatların toplamına hükmedilir',
            'D': 'Zamanaşımı en kısa olan sebebe göre',
            'E': 'Zarar görene en iyi giderim imkânı sağlayan sebebe göre',
        },
        'E',
        "TBK m. 60'a göre bir kişinin sorumluluğu birden çok sebebe dayandırılabiliyorsa hâkim, **zarar gören aksini istemiş olmadıkça** veya kanunda aksi öngörülmedikçe, **zarar görene en iyi giderim imkânı sağlayan sorumluluk sebebine** göre karar verir.",
        '6098 sayılı TBK m. 60',
    ),
    # düzey 2
    '0026': patch(
        'İki sürücünün birlikte kusuruyla meydana gelen kazada zarar gören yaya, tazminatın tamamını sürücülerden birinden istemiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Tamamını ödeyen sürücü diğerine payı oranında rücu edebilir',
            'B': 'Sürücüler yayaya karşı müteselsilen sorumludur',
            'C': 'Yaya her sürücüden ancak onun kusur payı kadar isteyebilir',
            'D': 'Paylaştırmada kusurların ağırlığı gözetilir',
            'E': 'Yaya tazminatın tamamını dilediği sürücüden isteyebilir',
        },
        'C',
        "TBK m. 61'e göre **birden çok kişi birlikte bir zarara sebebiyet verirse** müteselsil sorumluluk hükümleri uygulanır; zarar gören tamamını dilediğinden isteyebilir. Kusura göre paylaştırma m. 62 uyarınca iç ilişkiye aittir.",
        '6098 sayılı TBK m. 61',
    ),
    # düzey 3
    '0027': patch(
        "Tazminatın ödenmesi kendisinden istenen A, birlikte sorumlu olduğu B'ye durumu hiç bildirmemiştir. A'nın B'ye karşı rücu isteminde zamanaşımı hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Bildirim yapılana kadar zamanaşımı durur',
            'B': 'Bildirimin dürüstlük kurallarına göre yapılabileceği tarihte başlar',
            'C': 'Bildirim yapılmadığından rücu hakkı düşer',
            'D': "Zamanaşımı, B'nin zarar görenin açtığı davayı öğrendiği tarihte işlemeye başlar",
            'E': 'Zamanaşımı fiilin işlendiği tarihte başlar',
        },
        'B',
        "TBK m. 73/2'ye göre tazminatın ödenmesi kendisinden istenen kişi durumu birlikte sorumlu olduğu kişilere bildirmek zorundadır; aksi takdirde **zamanaşımı, bu bildirimin dürüstlük kurallarına göre yapılabileceği tarihte işlemeye başlar**.",
        '6098 sayılı TBK m. 73/2',
    ),
    # düzey 3
    '0028': patch(
        'Bir alacaklı, borcunu ödemeden ülkeyi terk etmek üzere havaalanına giden borçlusunu yolda görmüş; kolluk gücü zamanında gelemeyecek ve alacağın tahsili önemli ölçüde zorlaşacak olduğundan borçlunun valizini alıkoymuştur. Başka bir yol yoktur. Alacaklının sorumluluğu hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Hakkını kendi gücüyle koruma şartları oluştuğundan sorumlu tutulamaz',
            'B': 'Zarar verdiğinden tazminatın tamamını öder',
            'C': 'Kolluk yetkisini gasp ettiğinden sorumludur',
            'D': 'Ancak borçlu valizin alıkonulmasına sonradan rıza gösterirse sorumluluktan kurtulur',
            'E': 'Hâkim tazminatı yarıya indirir',
        },
        'A',
        "TBK m. 64/3'e göre hakkını kendi gücüyle koruma durumunda kalan kişi, **kolluk gücünün yardımını zamanında sağlayamayacak ise** ve hakkının kayba uğramasını ya da kullanılmasının önemli ölçüde zorlaşmasını önleyecek **başka bir yol da yoksa**, verdiği zarardan sorumlu tutulamaz.",
        '6098 sayılı TBK m. 64/3',
    ),
    # düzey 2
    '0029': patch(
        "Aşağıdakilerden hangileri TBK m. 63'e göre fiilin hukuka aykırılığını kaldıran hâllerdendir?\n\nI. Zarar görenin rızası\n\nII. Zarar verenin iyiniyetli olması\n\nIII. Daha üstün nitelikte kamusal yarar\n\nIV. Haklı savunma",
        {
            'A': 'I, III ve IV',
            'B': 'I, II, III ve IV',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'II ve IV',
        },
        'A',
        "TBK m. 63/2'ye göre **zarar görenin rızası, daha üstün nitelikte özel veya kamusal yarar, haklı savunma**, hakkını kendi gücüyle koruma ve zorunluluk hâllerinde fiil hukuka aykırı sayılmaz. Zarar verenin iyiniyeti bu hâller arasında sayılmamıştır.",
        '6098 sayılı TBK m. 63',
    ),
    # düzey 3
    '0030': patch(
        'Bir şirketin şoförü dikkatsiz sürüşüyle bir yayayı yaralamış, şirket tazminatı ödemiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Yaya tazminatı şirketten isteyebilir',
            'B': 'Şirket, şoförü seçerken ve denetlerken gerekli özeni ispat ederek sorumluluktan kurtulabilir',
            'C': 'Yaya şoföre de haksız fiil nedeniyle başvurabilir',
            'D': 'Şirket, şoförün kusur derecesine bakılmaksızın ödediğinin tamamını ona rücu eder',
            'E': 'Şirket şoföre onun bizzat sorumlu olduğu ölçüde rücu eder',
        },
        'D',
        "TBK m. 66/4'e göre adam çalıştıran, ödediği tazminat için zarar veren çalışana **ancak onun bizzat sorumlu olduğu ölçüde** rücu hakkına sahiptir; tamamını otomatik olarak rücu edemez.",
        '6098 sayılı TBK m. 66/4',
    ),
    # düzey 2
    '0031': patch(
        "Komşunun inekleri A'nın tarlasına girerek ekinlere zarar vermiştir. A'nın bu durumdaki hakları hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Hayvanlara el koyamaz; dava yoluna gitmelidir',
            'B': 'Hayvanların mülkiyetini kazanır',
            'C': 'Hayvanları derhal satarak zararını karşılayabilir',
            'D': 'Hayvanları yakalayıp zararı giderilinceye kadar alıkoyabilir',
            'E': 'Sahibine bilgi vermeden hayvanları süresiz tutabilir',
        },
        'D',
        "TBK m. 68'e göre bir kişinin hayvanı başkasının taşınmazında zarar verirse **taşınmazın zilyedi o hayvanı yakalayabilir, zararı giderilinceye kadar alıkoyabilir**; ancak derhâl hayvan sahibine bilgi vermek zorundadır.",
        '6098 sayılı TBK m. 68',
    ),
    # düzey 2
    '0032': patch(
        'Yeni teslim alınan bir binanın balkonu, müteahhidin yapım hatası nedeniyle çökerek yoldan geçen birini yaralamıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Malik yapım hatasını bilmediğini ispat ederek sorumluluktan kurtulur',
            'B': 'Malikin sorumluluğu kusur aranmayan bir sorumluluktur',
            'C': 'Yaralanan kişinin malikin kusurunu ispatlaması gerekmez',
            'D': 'Bina maliki yapım bozukluğundan doğan zarardan sorumludur',
            'E': 'Malik ödediği tazminat için müteahhide rücu edebilir',
        },
        'A',
        "TBK m. 69'a göre bina maliki **yapımındaki bozukluklardan** doğan zarardan kusur aranmaksızın sorumludur; hatayı bilmemesi sorumluluğu kaldırmaz. Sorumluların, kendilerine karşı sorumlu olan diğer kişilere (müteahhit) **rücu hakkı saklıdır**.",
        '6098 sayılı TBK m. 69',
    ),
    # düzey 3
    '0033': patch(
        "Bir inşaat şirketinin 2020 yılında yaptığı kazı çalışması komşu binaya zarar vermiş; bina sahibi zararı ve sorumlu şirketi 10 Ocak 2025'te öğrenmiştir. Fiil ceza zamanaşımı daha uzun bir suç oluşturmamaktadır. Tazminat istemi en geç hangi tarihte zamanaşımına uğrar?",
        {
            'A': 'Fiilden itibaren 2030 yılında',
            'B': '31 Aralık 2025',
            'C': '10 Ocak 2027',
            'D': '10 Ocak 2030',
            'E': '10 Ocak 2026',
        },
        'C',
        "TBK m. 72'ye göre tazminat istemi, **zararı ve tazminat yükümlüsünü öğrenme tarihinden başlayarak iki yılın** ve her hâlde fiilden itibaren on yılın geçmesiyle zamanaşımına uğrar. Öğrenme 10 Ocak 2025 → **10 Ocak 2027**; on yıllık süre (2030) daha sonra dolduğundan iki yıllık süre belirleyicidir.",
        '6098 sayılı TBK m. 72',
    ),
    # düzey 3
    '0034': patch(
        'Yaralamaya yol açan bir fiil, ceza kanununda sekiz yıllık dava zamanaşımına tabi bir suç oluşturmaktadır. Zarar gören zararı ve faili hemen öğrenmiştir. Tazminat istemi için uygulanacak zamanaşımı süresi hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İki yıllık süre ile sekiz yıllık süre toplanır',
            'B': 'İki yıllık süre uygulanır; ceza zamanaşımı dikkate alınmaz',
            'C': 'On yıllık süre uygulanır',
            'D': 'Zamanaşımı ceza davası bitinceye kadar işlemez',
            'E': 'Ceza zamanaşımı daha uzun olduğundan sekiz yıllık süre uygulanır',
        },
        'E',
        "TBK m. 72/1'e göre tazminat, **ceza kanunlarının daha uzun bir zamanaşımı öngördüğü cezayı gerektiren bir fiilden doğmuşsa, bu zamanaşımı uygulanır**.",
        '6098 sayılı TBK m. 72',
    ),
    # düzey 2
    '0035': patch(
        'Haksız fiilde zamanaşımına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ceza kanunu daha uzun zamanaşımı öngörüyorsa o süre uygulanır',
            'B': 'Fiilden itibaren on yıl geçince istem zamanaşımına uğrar',
            'C': 'İki yıllık süre, fiilin işlendiği tarihten başlar',
            'D': 'Haksız fiille doğan borcun ifasından zarar gören kaçınabilir',
            'E': 'Rücu isteminde iki yıllık süre ödeme ve birlikte sorumlunun öğrenilmesiyle başlar',
        },
        'C',
        "TBK m. 72'ye göre iki yıllık süre, **zarar görenin zararı ve tazminat yükümlüsünü öğrendiği tarihten** başlar; fiil tarihi on yıllık üst süre için esas alınır.",
        '6098 sayılı TBK m. 72, 73',
    ),
    # düzey 2
    '0036': patch(
        'Haksız fiil davalarında yargılamaya ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Ceza hâkiminin beraat kararı hukuk hâkimini bağlamaz\n\nII. Hâkim geçici ödemeye istem olmaksızın kendiliğinden karar verir\n\nIII. Hâkim bedensel zarar hükmünü değiştirme yetkisini saklı tutabilir',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'Yalnız I',
            'D': 'Yalnız III',
            'E': 'I ve III',
        },
        'E',
        "TBK m. 74'e göre hukuk hâkimi **ceza hâkiminin beraat kararıyla bağlı değildir** (I). m. 76'ya göre geçici ödemeye **istem üzerine** karar verilir (II yanlış). m. 75'e göre hâkim tazminat hükmünü değiştirme yetkisini iki yıl saklı tutabilir (III).",
        '6098 sayılı TBK m. 74-76',
    ),
    # düzey 3
    '0037': patch(
        'Bir cerrah, hastanın aydınlatılmış rızasıyla ve tıbbi kurallara uygun olarak estetik ameliyat yapmış; ameliyatın olağan sonucu olarak iz kalmıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Olağan sonuç olarak kalan iz nedeniyle cerrah tazminat öder',
            'B': 'Rızanın fiilden önce verilmiş olması gerekir',
            'C': 'Hastanın rızası fiilin hukuka aykırılığını kaldırır',
            'D': 'Rızanın kapsamı dışına çıkılırsa fiil hukuka aykırı olur',
            'E': 'Tıbbi kurallara aykırı müdahalede rıza sorumluluğu kaldırmaz',
        },
        'A',
        "TBK m. 63/2'ye göre **zarar görenin rızası** hâlinde fiil hukuka aykırı sayılmaz. Rıza fiilden önce verilmeli ve kapsamı içinde kalınmalıdır; tıbbi kurallara uygun ameliyatın olağan sonucundan cerrah sorumlu tutulamaz.",
        '6098 sayılı TBK m. 63/2',
    ),
    # düzey 3
    '0038': patch(
        'Hafif şekilde yaralanan ve kısa sürede iyileşen bir kişinin annesi, oğlunun yaralanması nedeniyle kendisi için manevi tazminat istemektedir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yakınlar her bedensel zararda manevi tazminat isteyebilir',
            'B': 'Ağır bedensel zarar veya ölüm bulunmadığından annenin istemi yerinde değildir',
            'C': 'Yakınların manevi tazminat hakkı ölüm hâliyle sınırlıdır',
            'D': 'Anne ancak maddi zararını da ispat ederse manevi tazminat alır',
            'E': 'Annenin istemi manevi değil, destekten yoksun kalma tazminatı olarak değerlendirilir',
        },
        'B',
        "TBK m. 56/1'e göre bedensel bütünlüğü zedelenen **kişinin kendisine** manevi tazminat verilebilir; m. 56/2'ye göre yakınlara manevi tazminat ancak **ağır bedensel zarar veya ölüm** hâlinde verilebilir.",
        '6098 sayılı TBK m. 56',
    ),
    # düzey 2
    '0039': patch(
        'Bir kargo şirketinin kuryesi, teslimat yaparken aracıyla bir bisikletliye çarpmıştır. Bisikletlinin tazminat istemi hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Şirket ancak kuryeyi seçerken kusurluysa zarar görene karşı sorumlu olur',
            'B': 'Şirketin sorumluluğu sözleşmeye aykırılık sorumluluğudur',
            'C': 'Zarar kuryenin kusurundan doğduğundan şirkete başvurulamaz',
            'D': 'İşin yapılması sırasında verilen zarardan kargo şirketi de sorumludur',
            'E': 'Bisikletli, kuryeye başvurmadan şirkete başvuramaz',
        },
        'D',
        "TBK m. 66/1'e göre **adam çalıştıran, çalışanın kendisine verilen işin yapılması sırasında başkalarına verdiği zararı gidermekle yükümlüdür**; bu, kusur aranmayan özen sorumluluğudur ve adam çalıştıran ancak gerekli özeni ispat ederek kurtulabilir.",
        '6098 sayılı TBK m. 66',
    ),
    # düzey 2
    '0040': patch(
        "Bir belediyenin açık bıraktığı çukura düşerek kalıcı sakatlığa uğrayan kişinin tazminatı hesaplanırken TBK'nın bedensel zarar hükümlerinin uygulanması hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İdarenin sorumlu olduğu bedensel zararlarda da TBK hükümleri uygulanır',
            'B': 'İdari eylemlerde TBK hükümleri uygulanmaz',
            'C': 'Hesap hâkimin serbest takdirine bırakılmıştır',
            'D': 'İdarenin sorumluluğunda hesaplanan tazminat kamu yararı gözetilerek hakkaniyetle azaltılır',
            'E': 'Hükümler ancak idare kusurluysa uygulanır',
        },
        'A',
        "TBK m. 55/2'ye göre bu Kanun hükümleri, **her türlü idari eylem ve işlemler ile idarenin sorumlu olduğu diğer sebeplerin** yol açtığı vücut bütünlüğünün yitirilmesine veya ölüme bağlı zararlara ilişkin istem ve davalarda da uygulanır.",
        '6098 sayılı TBK m. 55/2',
    ),
    # düzey 2
    '0041': patch(
        "Bir kafede yangın çıkmasına kusuruyla sebep olan kişi aleyhine açılan davada, kafenin yangında yok olan stoklarının tam tutarı belgelenememiştir.\n\nTBK'ya göre zararın belirlenmesiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Zarar gören zararını ispat eder',
            'B': 'Zarar gören zarar verenin kusurunu ispat eder',
            'C': 'Miktar tam ispat edilemezse hâkim hakkaniyete göre belirler',
            'D': 'Tam ispat edilemeyen zarar tazmin edilmez',
            'E': 'Hâkim olayların olağan akışını göz önünde tutar',
        },
        'D',
        'TBK m. 50: zarar gören zararını ve zarar verenin kusurunu ispat eder; ancak zararın miktarı tam olarak ispat edilemiyorsa hâkim, olayların olağan akışını ve zarar görenin aldığı önlemleri göz önünde tutarak zararın miktarını hakkaniyete uygun olarak belirler.',
        '6098 sayılı TBK m. 50',
    ),
    # düzey 2
    '0042': patch(
        'Trafik kazasında yaralanan yolcunun emniyet kemeri takmadığı ve bu nedenle yaralanmalarının ağırlaştığı tespit edilmiştir. Hâkim tazminat hakkında ne yapabilir?',
        {
            'A': 'Tazminatı sürücü ile yolcu arasında eşit böler',
            'B': 'Kusur sürücüye ait olduğundan tazminatı indiremez',
            'C': 'Tazminatı indirebilir veya tamamen kaldırabilir',
            'D': 'Tazminatı artırmakla yükümlüdür',
            'E': 'Davayı zamanaşımından reddeder',
        },
        'C',
        "TBK m. 52/1'e göre zarar gören **zararın doğmasında ya da artmasında etkili olmuşsa** hâkim tazminatı **indirebilir veya tamamen kaldırabilir** (müterafik kusur).",
        '6098 sayılı TBK m. 52/1',
    ),
    # düzey 3
    '0043': patch(
        'Destekten yoksun kalma tazminatı hesaplanırken ölenin kazancının bilindiği dönem ile bilinmediği dönem için ayrı tutarlar bulunmuştur. Kanuni faiz başlangıcı hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bilinen dönem tutarına olay tarihinden, bilinmeyen döneme karar tarihinden',
            'B': 'Her iki tutara da olay tarihinden',
            'C': 'Her iki tutara da karar tarihinden',
            'D': 'Her iki tutara da dava tarihinden',
            'E': 'Bilinen dönem tutarına karar tarihinden, bilinmeyen döneme olay tarihinden',
        },
        'A',
        "7589 sayılı Kanunla m. 55'e eklenen fıkraya göre (yürürlük 31/7/2026) çalışma gücü kaybı ve destekten yoksun kalma tazminatında, **kazancın bilindiği döneme ilişkin tutara haksız fiilin meydana geldiği tarihten, bilinemediği döneme ilişkin tutara karar tarihinden** itibaren kanuni faiz işletilir.",
        '6098 sayılı TBK m. 55 (7589 sayılı Kanunla eklenen fıkra)',
    ),
    # düzey 3
    '0044': patch(
        'Destekten yoksun kalma ve bedensel zararların hesabına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İfa amacı taşımayan ödemeler zarardan düşülemez',
            'B': 'Bu hükümler idarenin sorumlu olduğu ölüm ve yaralanmalarda da uygulanır',
            'C': 'Hâkim hesaplanan tazminatı miktarına bakarak hakkaniyetle azaltabilir',
            'D': 'Tahkikattan önce ifa amacıyla ödenen bedel oransal olarak mahsup edilir',
            'E': 'Rücu edilemeyen sosyal güvenlik ödemeleri tazminattan indirilemez',
        },
        'C',
        "TBK m. 55/1'e göre **hesaplanan tazminat, miktar esas alınarak hakkaniyet düşüncesiyle artırılamaz veya azaltılamaz**. Rücu edilemeyen sosyal güvenlik ödemeleri ve ifa amacı taşımayan ödemeler indirilemez; hükümler idari eylem ve işlemlerden doğan zararlara da uygulanır; 7589 ile tahkikattan önceki ödemelerin oransal mahsubu düzenlenmiştir.",
        '6098 sayılı TBK m. 55',
    ),
    # düzey 2
    '0045': patch(
        "TBK'da düzenlenen haksız rekabete ilişkin aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Ticari işlere ait haksız rekabette TTK hükümleri saklıdır',
            'B': 'Gerçek olmayan haberlerin yayılması veya bu tür ilanların yapılması haksız rekabet davranışıdır',
            'C': 'Müşterileri azalan kişi davranışa son verilmesini isteyebilir',
            'D': 'Zarar gören, kusur aranmaksızın zararının giderilmesini isteyebilir',
            'E': 'Müşterilerini kaybetme tehlikesi de istem hakkı verir',
        },
        'D',
        "TBK m. 57'ye göre müşterileri azalan veya onları kaybetme tehlikesiyle karşılaşan kişi, davranışlara son verilmesini ve **kusurun varlığı hâlinde** zararının giderilmesini isteyebilir; ticari işlere ait haksız rekabette TTK hükümleri saklıdır.",
        '6098 sayılı TBK m. 57',
    ),
    # düzey 3
    '0046': patch(
        "Bir zarardan müteselsilen sorumlu A ve B'den A, 300.000 ₺ tazminatın tamamını ödemiştir. İç ilişkide A'nın payı %60, B'nin payı %40 olarak belirlenmiştir. A, B'ye kaç ₺ için rücu edebilir?",
        {
            'A': '150.000',
            'B': '300.000',
            'C': '120.000',
            'D': '180.000',
            'E': '60.000',
        },
        'C',
        "TBK m. 62'ye göre tazminat müteselsil borçlular arasında kusurun ağırlığı ve tehlikenin yoğunluğuna göre paylaştırılır; **kendi payına düşeninden fazlasını ödeyen, fazla ödemesi için diğerlerine rücu eder ve zarar görenin haklarına halef olur**: 300.000 × %40 = **120.000 ₺**.",
        '6098 sayılı TBK m. 62',
    ),
    # düzey 2
    '0047': patch(
        'İcra memuru, usulüne uygun bir haciz kararı üzerine ve yetkisinin sınırları içinde kalarak borçlunun aracını haczetmiştir. Borçlunun haksız fiil istemi hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Zarar doğduğundan fiil hukuka aykırı sayılır',
            'B': 'Kanundan doğan yetki sınırları içinde kaldığından fiil hukuka aykırı değildir',
            'C': 'Hâkim hakkaniyete göre tazminata hükmeder',
            'D': 'Haciz, zarara yol açtığı için ancak borçlunun sonradan onay vermesiyle hukuka uygun hâle gelir',
            'E': 'Memur kusursuz sorumlu olduğundan tazminat öder',
        },
        'B',
        "TBK m. 63/1'e göre **kanunun verdiği yetkiye dayanan ve bu yetkinin sınırları içinde kalan bir fiil, zarara yol açsa bile hukuka aykırı sayılmaz**.",
        '6098 sayılı TBK m. 63/1',
    ),
    # düzey 3
    '0048': patch(
        "A, kendisine bıçakla saldıran B'yi etkisiz hâle getirirken B'yi yaralamış; olay yerinden kaçarken de C'nin vitrin camını kırmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "A'nın C'ye karşı giderim yükümlülüğünü hâkim hakkaniyete göre belirler",
            'B': "A, C'nin zararından da haklı savunma nedeniyle sorumlu tutulamaz",
            'C': "A'nın B'ye karşı davranışı hukuka aykırı sayılmaz",
            'D': "C'nin zararı zorunluluk hâli kapsamında değerlendirilir",
            'E': "A, B'nin zararından sorumlu tutulamaz",
        },
        'B',
        "TBK m. 64/1'e göre **haklı savunmada bulunan, saldıranın şahsına veya mallarına verdiği zarardan** sorumlu tutulamaz; bu kural saldırgan olmayan C'yi kapsamaz. Kendini tehlikeden korumak için **diğer bir kişinin mallarına zarar verenin** giderim yükümlülüğünü ise hâkim hakkaniyete göre belirler (m. 64/2).",
        '6098 sayılı TBK m. 64',
    ),
    # düzey 2
    '0049': patch(
        'Ayırt etme gücü ve kusura ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Hakkaniyet sorumluluğunda hâkim giderimin bir kısmına karar verebilir',
            'B': 'Hakkaniyet sorumluluğu kusur aranmayan bir sorumluluk hâlidir',
            'C': 'Ayırt etme gücünü geçici kaybeden kişi verdiği zarardan sorumlu olmaz',
            'D': 'Ayırt etme gücü olmayanın zararı hakkaniyet gerektiriyorsa giderilir',
            'E': 'Geçici kayıpta kusuru olmadığını ispat eden kişi sorumluluktan kurtulur',
        },
        'C',
        "TBK m. 59'a göre **ayırt etme gücünü geçici olarak kaybeden kişi, bu sırada verdiği zararları gidermekle yükümlüdür**; ancak kaybetmede kusuru olmadığını ispat ederse kurtulur.",
        '6098 sayılı TBK m. 59, 65',
    ),
    # düzey 3
    '0050': patch(
        'Aşağıdaki hâllerden hangilerinde adam çalıştıran, çalışanının verdiği zarardan sorumlu olmaz?\n\nI. Seçme, talimat, gözetim ve denetimde gerekli özeni gösterdiğini ispat ederse\n\nII. Zarar, çalışanın işiyle ilgisi olmayan özel faaliyeti sırasında doğmuşsa\n\nIII. Çalışan zararı işin yapılması sırasında kasten vermişse',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'Yalnız II',
            'E': 'I ve III',
        },
        'B',
        "TBK m. 66'ya göre adam çalıştıran, çalışanın **kendisine verilen işin yapılması sırasında** verdiği zarardan sorumludur (II bu kapsamda değildir) ve **gerekli özeni gösterdiğini ispat ederse** sorumlu olmaz (I). Çalışanın kastı, adam çalıştıranın sorumluluğunu ortadan kaldırmaz (III).",
        '6098 sayılı TBK m. 66',
    ),
    # düzey 3
    '0051': patch(
        'Bir çiftlikteki at, geçen bir motosikletlinin bilerek kornaya basması sonucu ürkmüş ve bahçe duvarına zarar vermiştir. Atı bulunduran zararı ödemiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Duvar sahibi ile at sahibi zararı paylaşır',
            'B': 'Atı bulunduran ödediğini geri isteyemez',
            'C': 'Atı bulunduranın motosiklet sürücüsüne rücu hakkı saklıdır',
            'D': 'Zarar motosiklet sürücüsünden istenebilir, at sahibinden istenemez',
            'E': 'Ürkütme olduğundan atı bulunduran sorumlu olmaz',
        },
        'C',
        "TBK m. 67/3'e göre hayvan **bir başkası veya bir başkasına ait hayvan tarafından ürkütülmüş olursa, hayvanı bulunduranın bu kişilere rücu hakkı** saklıdır.",
        '6098 sayılı TBK m. 67/3',
    ),
    # düzey 2
    '0052': patch(
        "Komşu binanın çatısındaki gevşek kiremitler, rüzgârlı havalarda A'nın bahçesine düşme tehlikesi yaratmaktadır. Henüz bir zarar doğmamıştır.\n\nTBK'ya göre A'nın haklarıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'A tehlikenin giderilmesi için önlem alınmasını isteyebilir',
            'B': 'İstem bina üzerinde hak sahibi olanlara yöneltilir',
            'C': 'İstem için zararın doğması beklenmez',
            'D': 'Zarar doğmadan A bir istemde bulunamaz',
            'E': 'Kural bina ve yapı eserlerinden doğan tehlikelere ilişkindir',
        },
        'D',
        'TBK m. 70: bir başkasına ait bina veya yapı eserlerinden zarar görme tehlikesiyle karşılaşan kişi, bu tehlikenin giderilmesi için gerekli önlemlerin alınmasını hak sahiplerinden isteyebilir; zararın doğması beklenmez.',
        '6098 sayılı TBK m. 70',
    ),
    # düzey 3
    '0053': patch(
        "Bir taş ocağının sahibi A, işletmeyi B'ye kiralamış; B'nin yaptığı patlatmalar nedeniyle çevredeki evlerde hasar oluşmuştur. Taş ocağının önemli ölçüde tehlike arz eden işletme olduğu kabul edilmiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Faaliyete hukuk düzenince izin verilmiş olması, zarar görenlerin denkleştirme istemini engellemez',
            'B': 'Sorumluluk için kusur aranmaz',
            'C': "Zarar görenler tazminatın tamamını A'dan isteyebilir",
            'D': 'A ve B zarar görenlere karşı müteselsilen sorumludur',
            'E': "Zarar görenler, patlatmayı yapan işleten B'ye başvurabilir; sahip A'ya başvuramaz",
        },
        'E',
        "TBK m. 71'e göre önemli ölçüde tehlike arz eden bir işletmenin faaliyetinden zarar doğarsa **işletme sahibi ve varsa işleten müteselsilen sorumludur**; kusur aranmaz ve izinli faaliyette de denkleştirme istenebilir.",
        '6098 sayılı TBK m. 71',
    ),
    # düzey 3
    '0054': patch(
        "A, aldatılarak B'ye bir borç senedi imzalamıştır. Aldatmadan doğan tazminat istemi zamanaşımına uğradıktan sonra B, senede dayanarak ödeme istemiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "A, B'nin ödeme istemine karşı aldatmayı savunma olarak ileri sürebilir",
            'B': "A'nın aldatmadan doğan tazminat istemi zamanaşımına uğramıştır",
            'C': 'Tazminat istemi zamanaşımına uğradığından A artık ifadan kaçınamaz',
            'D': 'İfadan kaçınma hakkı tazminat isteminin zamanaşımından etkilenmez',
            'E': 'A, senetten doğan borcu ifadan kaçınabilir',
        },
        'C',
        "TBK m. 72/2'ye göre **haksız fiil dolayısıyla zarar gören bakımından bir borç doğmuşsa zarar gören, haksız fiilden doğan tazminat istemi zamanaşımına uğramış olsa bile, her zaman bu borcu ifadan kaçınabilir**.",
        '6098 sayılı TBK m. 72/2',
    ),
    # düzey 2
    '0055': patch(
        'Trafik kazasında yaralanan kişinin kalıcı sakatlık oranı karar tarihinde tam olarak belirlenememiştir. Hâkim tazminat hükmünü değiştirme yetkisini, kararın kesinleşmesinden itibaren en fazla kaç yıl saklı tutabilir?',
        {
            'A': '5',
            'B': '3',
            'C': '10',
            'D': '2',
            'E': '1',
        },
        'D',
        "TBK m. 75'e göre **bedensel zararın kapsamı karar verme sırasında tam olarak belirlenemiyorsa hâkim, kararın kesinleşmesinden başlayarak iki yıl içinde** tazminat hükmünü değiştirme yetkisini saklı tutabilir.",
        '6098 sayılı TBK m. 75',
    ),
    # düzey 2
    '0056': patch(
        'Bir kazada sanık, ceza mahkemesince kusursuz bulunarak beraat etmiştir. Aynı olay nedeniyle açılan tazminat davasına ilişkin aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Ceza hâkiminin zarara ilişkin kararı hukuk hâkimini bağlamaz',
            'B': 'Kusurun varlığını hukuk hâkimi kendisi değerlendirir',
            'C': 'Hukuk hâkimi, ceza mahkemesinin kusur değerlendirmesini aynen benimser',
            'D': 'Hukuk hâkimi beraat kararıyla bağlı değildir',
            'E': 'Ayırt etme gücü bakımından ceza hukuku hükümleri hukuk hâkimini bağlamaz',
        },
        'C',
        "TBK m. 74'e göre hâkim, kusurun ve ayırt etme gücünün varlığı hakkında karar verirken **ceza hukukunun sorumlulukla ilgili hükümleriyle ve ceza hâkiminin beraat kararıyla bağlı değildir**; ceza hâkiminin kusurun değerlendirilmesine ve zararın belirlenmesine ilişkin kararı da hukuk hâkimini bağlamaz.",
        '6098 sayılı TBK m. 74',
    ),
    # düzey 2
    '0057': patch(
        "Hâkim, sürekli iş göremezlik tazminatının toplu ödeme yerine aylık irat biçiminde ödenmesine karar vermiştir.\n\nTBK'ya göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Hâkim tazminatın irat biçiminde ödenmesine karar verebilir',
            'B': 'İrat hükmedilirse borçlu güvence göstermekle yükümlüdür',
            'C': 'Borçlu iradı kendi iradesiyle durduramaz',
            'D': 'İrat hükmedilen borçlunun ek bir yükümlülüğü bulunmaz',
            'E': 'Güvence, iradın ödenmesini teminat altına alır',
        },
        'D',
        'TBK m. 51/2: hâkim, tazminatın ödenme biçimini belirler ve tazminatın irat biçiminde ödenmesine hükmedebilir; bu durumda borçlu güvence göstermekle yükümlüdür.',
        '6098 sayılı TBK m. 51/2',
    ),
    # düzey 3
    '0058': patch(
        "Bir kazada yaralanan kişinin tedavi giderleri 50.000 ₺, kazanç kaybı 30.000 ₺'dir. Zarar görenin zararın artmasında etkili olduğu gerekçesiyle hâkim tazminatı %20 oranında indirmiştir. Hükmedilecek maddi tazminat kaç ₺'dir?",
        {
            'A': '56.000',
            'B': '64.000',
            'C': '40.000',
            'D': '80.000',
            'E': '16.000',
        },
        'B',
        "TBK m. 54'e göre **tedavi giderleri ve kazanç kaybı** bedensel zarar kalemleridir: 50.000 + 30.000 = 80.000 ₺. m. 52/1'e göre zarar gören zararın artmasında etkili olmuşsa hâkim tazminatı indirebilir: 80.000 × %80 = **64.000 ₺**.",
        '6098 sayılı TBK m. 52, 54',
    ),
    # düzey 3
    '0059': patch(
        "Bir binanın bakım eksikliği ile tamircinin kusurlu işçiliği birlikte bir yayanın yaralanmasına yol açmıştır. Bina maliki yapı maliki sorumluluğuna, tamirci ise kusur sorumluluğuna göre sorumludur.\n\nTBK'ya göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Farklı sebeplerle sorumlu olduklarından her biri kendi payından sorumludur',
            'B': 'Aynı zarardan farklı sebeplerle sorumlu olanlar müteselsilen sorumludur',
            'C': 'Yaya sorumlulardan dilediğine başvurabilir',
            'D': 'İç ilişkide paylaştırma ayrıca yapılır',
            'E': 'Malikin sorumluluğu tamircinin kusuruyla ortadan kalkmaz',
        },
        'A',
        "TBK m. 61: birden çok kişi birlikte bir zarara sebebiyet verir veya aynı zarardan çeşitli sebeplerden dolayı sorumlu olursa müteselsil sorumluluk hükümleri uygulanır; zarar gören dilediğine başvurur, iç ilişkide paylaştırma m. 62'ye göre yapılır.",
        '6098 sayılı TBK m. 61',
    ),
    # düzey 3
    '0060': patch(
        'Sorumluluğu hem sözleşmeye hem haksız fiile dayanan bir olayda zarar gören, açıkça sözleşme sorumluluğuna göre karar verilmesini istemiştir. Hâkim hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Zarar görenin bu istemine göre karar verir',
            'B': 'Haksız fiil hükümlerini öncelikle uygular',
            'C': 'Zarar görenin istemine rağmen en elverişli sebebi uygular',
            'D': 'Her iki sebebe göre ayrı ayrı tazminata hükmeder',
            'E': 'Zarar verenin tercih ettiği sebebe göre karar verir',
        },
        'A',
        "TBK m. 60'a göre hâkim, **zarar gören aksini istemiş olmadıkça** veya kanunda aksi öngörülmedikçe, zarar görene en iyi giderim imkânı sağlayan sebebe göre karar verir. Zarar görenin açık tercihi hâkimi bağlar.",
        '6098 sayılı TBK m. 60',
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
    print(f"1 paket / {len(PATCHES)} soru ('Haksiz Fiil' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
