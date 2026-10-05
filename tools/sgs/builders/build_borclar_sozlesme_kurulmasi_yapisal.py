#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sozlesmenin Kurulmasi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Borclar hukuku gercek sinav profiliyle yeniden yazim (eski surum tanim kalibindaydi, 121 celdirici mutlak ifadeli, kor %46): oneri ve kabul, sekil, borc tanimasi, yorum ve muvazaa, genel islem kosullari, kesin hukumsuzluk, asiri yararlanma, onsozlesme, yanilma-aldatma-korkutma. Gercek sinav kaliplari (GIK tanimi, hazir olmayanlar arasinda hukum ani, kesin hukumsuzluk listeleri, sekil 'yanlis' sorusu) olaylara ve tarih hesaplarina cevrildi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 6098 sayili Turk Borclar Kanunu m. 1-39 guncel metni (mevzuat.gov.tr)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/borclar_hukuku/sozlesmenin_kurulmasi.json"
STYLE_REF = 'SGS Borclar Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "sozlesme-gen-"


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
        'A ile B, bir aracın satışında aracın kendisi ve bedel üzerinde anlaşmış; teslim yerini konuşmamışlardır. Daha sonra teslim yeri konusunda uyuşmazlık çıkmıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Esaslı noktalarda uyuşma sözleşmeyi kurar',
            'B': 'Teslim yeri kararlaştırılmadığından sözleşme kurulmamıştır',
            'C': 'Uyuşmazlığı hâkim işin özelliğine bakarak çözer',
            'D': 'Satılan araç ve bedel sözleşmenin esaslı noktalarıdır',
            'E': 'Teslim yeri ikinci derecedeki bir noktadır',
        },
        'B',
        "TBK m. 2'ye göre taraflar **esaslı noktalarda uyuşmuşlarsa, ikinci derecedeki noktalar üzerinde durulmamış olsa bile sözleşme kurulmuş sayılır**; ikinci derecedeki noktalarda uyuşulamazsa hâkim uyuşmazlığı işin özelliğine bakarak karara bağlar.",
        '6098 sayılı TBK m. 1, 2',
    ),
    # düzey 3
    '0002': patch(
        'Hazır olmayanlar arasında süresiz yapılan bir öneriye zamanında gönderilen kabul, posta gecikmesi nedeniyle önerene geç ulaşmıştır. Öneren, sözleşmeyle bağlı olmak istemediği hâlde durumu kabul edene bildirmemiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Kabul geç ulaştığından öneren sözleşmeyle bağlı değildir',
            'B': 'Kabulün zamanında gönderilmiş olması önemlidir',
            'C': 'Öneren önerisini zamanında ulaşmış sayabilir',
            'D': 'Bildirim yapılmadığından sözleşme kurulmuş sayılır',
            'E': 'Öneren, bağlı olmak istemiyorsa durumu hemen bildirmelidir',
        },
        'A',
        "TBK m. 5/3'e göre **zamanında gönderilen kabul önerene geç ulaşır ve öneren onunla bağlı olmak istemezse, durumu hemen kabul edene bildirmek zorundadır**. Bildirim yapılmazsa öneren sözleşmeyle bağlı olur.",
        '6098 sayılı TBK m. 5/3',
    ),
    # düzey 2
    '0003': patch(
        "A, bir ürün için gönderdiği teklif mektubunda 'Bu teklif bağlayıcı değildir' ifadesine yer vermiştir. B, teklifi kabul ettiğini bildirmiştir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': "B'nin kabulüyle sözleşme kurulmuştur",
            'B': "A'nın bağlı olup olmadığına hâkim karar verir",
            'C': 'Bağlanmama hakkı açıkça saklı tutulduğundan A önerisiyle bağlı değildir',
            'D': 'A ancak bir ay süreyle bağlıdır',
            'E': 'Bağlanmama kaydı dürüstlük kuralına aykırı olduğundan geçersizdir ve A bağlıdır',
        },
        'C',
        "TBK m. 8/1'e göre öneren, **önerisiyle bağlı olmama hakkının saklı olduğunu açıkça belirtirse** veya işin özelliğinden ya da durumun gereğinden bağlanma niyetinde olmadığı anlaşılırsa, önerisi kendisini bağlamaz.",
        '6098 sayılı TBK m. 8/1',
    ),
    # düzey 2
    '0004': patch(
        "A, arkadaşının banka kredisine sözlü olarak kefil olmuştur. Kefalet sözleşmesi için kanunda yazılı şekil öngörülmüştür.\n\nTBK'ya göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Kanunda öngörülen şekil kural olarak geçerlilik şeklidir',
            'B': 'Şekle uyulmadan kurulan sözleşme hüküm doğurmaz',
            'C': 'Kefalet sözleşmesi yazılı şekle tabidir',
            'D': 'Sözlü kefalet geçerlidir; şekil ispat içindir',
            'E': 'Şekil eksikliği bankanın onayıyla giderilmez',
        },
        'D',
        "TBK m. 12: kanunda sözleşmeler için öngörülen şekil kural olarak geçerlilik şeklidir; öngörülen şekle uyulmaksızın kurulan sözleşmeler hüküm doğurmaz. Kefalet sözleşmesi m. 583'e göre yazılı şekle tabidir; şekil eksikliği tarafların onayıyla giderilemez.",
        '6098 sayılı TBK m. 12, 583',
    ),
    # düzey 3
    '0005': patch(
        'Kanunen yazılı şekle tabi bir sözleşmenin tarafları sonradan sözlü olarak iki değişiklik yapmıştır: sözleşme bedelinin artırılması ve sözleşmede düzenlenmemiş olan ödeme yerinin belirlenmesi. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Bu kural yazılı şekil dışındaki geçerlilik şekillerinde de uygulanır',
            'B': 'Yazılı şekle tabi sözleşmenin değiştirilmesi de yazılı yapılır',
            'C': 'Metinle çelişmeyen tamamlayıcı yan hükümler şekle tabi değildir',
            'D': 'Ödeme yeri kaydı metinle çelişmeyen tamamlayıcı bir yan hükümdür',
            'E': 'Sözlü olarak yapılan bedel artışı geçerlidir',
        },
        'E',
        "TBK m. 13'e göre kanunda yazılı şekilde yapılması öngörülen sözleşmenin **değiştirilmesinde de yazılı şekle uyulması zorunludur**; ancak **sözleşme metniyle çelişmeyen tamamlayıcı yan hükümler** bu kuralın dışındadır. Bedel artışı esaslı bir değişikliktir.",
        '6098 sayılı TBK m. 13',
    ),
    # düzey 2
    '0006': patch(
        "Taraflar, bir malın mülkiyetini bedel karşılığında devretmek istemiş, ancak belgeye yanlışlıkla 'kira sözleşmesi' başlığı yazmışlardır.\n\nTBK'ya göre sözleşmenin türünün belirlenmesiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Sözleşmenin türü belgedeki başlığa göre belirlenir',
            'B': 'Tarafların gerçek ve ortak iradesi esas alınır',
            'C': 'Yanlışlıkla kullanılan sözcükler belirleyici değildir',
            'D': 'Gerçek amacı gizlemek için kullanılan sözcükler de belirleyici değildir',
            'E': 'Bu sözleşme satış olarak nitelendirilir',
        },
        'A',
        'TBK m. 19/1: sözleşmenin türünün ve içeriğinin belirlenmesinde, tarafların yanlışlıkla veya gerçek amaçlarını gizlemek için kullandıkları sözcüklere bakılmaksızın, gerçek ve ortak iradeleri esas alınır. Bu nedenle sözleşme satıştır.',
        '6098 sayılı TBK m. 19/1',
    ),
    # düzey 3
    '0007': patch(
        "A, B ile muvazaalı olarak B'ye 100.000 ₺ borçlu olduğunu yazılı olarak tanımıştır. B bu alacağı, borç tanımasına güvenerek iyiniyetli C'ye devretmiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'C, yazılı borç tanımasına güvenerek alacağı kazanmıştır',
            'B': 'A ile B arasında muvazaa ileri sürülebilir',
            'C': "A, C'ye karşı muvazaa savunmasında bulunamaz",
            'D': "A, muvazaayı ispat ederek C'ye karşı borçtan kurtulur",
            'E': 'A ile B arasındaki borç tanıması muvazaalıdır',
        },
        'D',
        "TBK m. 19/2'ye göre **borçlu, yazılı bir borç tanımasına güvenerek alacağı kazanmış olan üçüncü kişiye karşı, bu işlemin muvazaalı olduğu savunmasında bulunamaz**; muvazaa taraflar arasında ileri sürülebilir.",
        '6098 sayılı TBK m. 19/2',
    ),
    # düzey 3
    '0008': patch(
        'Bir sözleşmedeki iki genel işlem koşulu yazılmamış sayılmıştır. Düzenleyen şirket, bu koşullar olmasaydı sözleşmeyi yapmayacağını ileri sürerek sözleşmenin tamamının geçersizliğini istemektedir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Düzenleyen sözleşmeden tazminatsız dönebilir',
            'B': 'Düzenleyen bunu ileri süremez; sözleşme ayakta kalır',
            'C': 'Hâkim sözleşmeyi uyarlayarak koşulları geri getirir',
            'D': 'Sözleşme karşı tarafın onayına kadar askıda kalır',
            'E': 'Sözleşmenin tamamı kesin hükümsüz olur',
        },
        'B',
        "TBK m. 22'ye göre sözleşmenin **yazılmamış sayılan genel işlem koşulları dışındaki hükümleri geçerliliğini korur**; düzenleyen, **yazılmamış sayılan koşullar olmasaydı diğer hükümlerle sözleşmeyi yapmayacak olduğunu ileri süremez**. Bu kural m. 27/2'deki kısmi hükümsüzlük kuralından ayrılır.",
        '6098 sayılı TBK m. 22',
    ),
    # düzey 2
    '0009': patch(
        "Bir kiralık araç sözleşmesinin genel işlem koşulunda 'araç günlük kullanım sınırını aşarsa ek ücret alınır' denmiş, ancak sınırın kilometre mi saat mi olduğu belirtilmemiştir. Koşul nasıl yorumlanır?",
        {
            'A': 'Hâkimin serbest takdirine göre',
            'B': 'Taraflar arasında yarı yarıya ve sektör uygulamasına göre',
            'C': 'Düzenleyenin lehine',
            'D': 'Sektördeki en yüksek ücret esas alınarak',
            'E': 'Düzenleyenin aleyhine, karşı tarafın lehine',
        },
        'E',
        "TBK m. 23'e göre genel işlem koşullarında yer alan bir hüküm **açık ve anlaşılır değilse veya birden çok anlama geliyorsa, düzenleyenin aleyhine ve karşı tarafın lehine yorumlanır**.",
        '6098 sayılı TBK m. 23',
    ),
    # düzey 3
    '0010': patch(
        'Aşağıdaki sözleşmelerden hangileri kesin hükümsüzdür?\n\nI. Taraflarca bilinmeden, sözleşmeden bir gün önce yanıp yok olan evin satışı\n\nII. Tehdit edilerek imzalatılan araba satışı\n\nIII. Rakibin iş yerini kundaklaması karşılığında ücret ödenmesine ilişkin sözleşme',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'Yalnız I',
            'D': 'I ve III',
            'E': 'Yalnız III',
        },
        'D',
        "TBK m. 27'ye göre **konusu imkânsız** (I: sözleşme kurulurken edim zaten imkânsız) ve **hukuka, ahlaka aykırı** (III) sözleşmeler kesin hükümsüzdür. Korkutma (II) bir irade bozukluğudur; sözleşme kesin hükümsüz değil, korkutulan için bağlayıcı olmayan (iptal edilebilir) bir sözleşmedir (m. 37, 39).",
        '6098 sayılı TBK m. 27',
    ),
    # düzey 3
    '0011': patch(
        "Ağır hastalığı nedeniyle acil paraya ihtiyaç duyan A, piyasa değeri 3.000.000 ₺ olan dairesini, bu durumu bilen ve bundan yararlanan B'ye 1.500.000 ₺'ye satmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'A sözleşmeye bağlı kalarak oransızlığın giderilmesini isteyebilir',
            'B': 'Edimler arasında açık bir oransızlık vardır',
            'C': "Oransızlık A'nın zor durumundan yararlanılarak gerçekleşmiştir",
            'D': 'A sözleşmeyle bağlı olmadığını bildirip edimini geri isteyebilir',
            'E': 'Oransızlık bulunduğundan sözleşme kesin hükümsüzdür',
        },
        'E',
        "TBK m. 28'e göre karşılıklı edimler arasındaki açık oransızlık, **zarar görenin zor durumundan, düşüncesizliğinden veya deneyimsizliğinden yararlanılarak** gerçekleştirilmişse zarar gören, **ya sözleşmeyle bağlı olmadığını bildirerek ediminin geri verilmesini ya da sözleşmeye bağlı kalarak oransızlığın giderilmesini** isteyebilir. Aşırı yararlanma kesin hükümsüzlük sebebi değildir.",
        '6098 sayılı TBK m. 28',
    ),
    # düzey 3
    '0012': patch(
        "Zor durumda kalarak 2019'da aşırı yararlanmaya maruz kalan bir satıcının zor durumu 10 Ocak 2025'te ortadan kalkmıştır. Satıcı 1 Mart 2025'te hakkını kullanmak istemektedir.\n\nTBK'ya göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Zor durumda kalmada bir yıllık süre durumun kalktığı tarihten başlar',
            'B': 'Bir yıl geçmediğinden satıcı hakkını kullanabilir',
            'C': 'Hak en geç sözleşmeden itibaren beş yıl içinde kullanılır',
            'D': 'Bu olayda beş yıllık süre dolmuştur',
            'E': 'İki süreden önce dolan, hakkın kullanılmasını engeller',
        },
        'B',
        "TBK m. 28/2: zor durumda kalmada bir yıllık süre zor durumun ortadan kalktığı tarihten başlar; ancak hak her hâlde sözleşmenin kurulduğu tarihten başlayarak beş yıl içinde kullanılmalıdır. 2019'daki sözleşmeden itibaren beş yıl 2024'te dolmuştur; bir yıllık sürenin dolmamış olması sonucu değiştirmez.",
        '6098 sayılı TBK m. 28/2',
    ),
    # düzey 3
    '0013': patch(
        'A, bir dükkânı, önüne metro istasyonu yapılacağı ve bunun sözleşmenin temeli olduğu hem kendisi hem de satıcı tarafından açıkça bilinerek satın almıştır. Metro projesinin çoktan iptal edildiği ortaya çıkmıştır. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Saikte yanılma bu olayda esaslı sayılır',
            'B': 'Saikte yanılma esaslı yanılma sayılmaz',
            'C': 'Sözleşme kesin hükümsüzdür',
            'D': 'A ancak aldatma varsa sözleşmeden kurtulabilir',
            'E': 'Yanılma basit hesap yanlışlığıdır',
        },
        'A',
        "TBK m. 32'ye göre saikte yanılma kural olarak esaslı değildir; ancak **yanılanın yanıldığı saiki sözleşmenin temeli sayması**, bunun iş ilişkilerinde geçerli **dürüstlük kurallarına uygun olması** ve **karşı tarafça da bilinebilir** olması hâlinde esaslı sayılır.",
        '6098 sayılı TBK m. 32',
    ),
    # düzey 3
    '0014': patch(
        "Kendi dikkatsizliği sonucu esaslı yanılmaya düşen A sözleşmeyle bağlı olmadığını bildirmiştir. Karşı taraf B, sözleşmenin geçerliliğine güvenerek masraf yapmıştır. B, A'nın yanıldığını bilmemekte ve bilmesi de gerekmemektedir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'B yanılmayı bilseydi tazminat isteyemezdi',
            'B': 'Hâkim hakkaniyet gerektirirse daha fazla tazminata hükmedebilir',
            'C': "A, yanılmasında kusurlu olduğundan B'nin zararını gidermekle yükümlüdür",
            'D': "A yanıldığı için B'nin zararını gidermekle yükümlü değildir",
            'E': 'Hâkimin hükmedeceği tazminat ifadan beklenen yararı aşamaz',
        },
        'D',
        "TBK m. 35'e göre **yanılan, yanılmasında kusurlu ise sözleşmenin hükümsüzlüğünden doğan zararı gidermekle yükümlüdür**; diğer taraf yanılmayı biliyor veya bilmesi gerekiyorsa tazminat istenemez. Hâkim hakkaniyet gerektirirse, ifadan beklenen yararı aşmamak kaydıyla daha fazla tazminata hükmedebilir.",
        '6098 sayılı TBK m. 35',
    ),
    # düzey 3
    '0015': patch(
        "İşveren B, çalışanı A'nın 20.000 ₺ zimmete para geçirdiğini öğrenmiş ve savcılığa şikâyet edeceğini söyleyerek A'ya 60.000 ₺'lik bir borç senedi imzalatmıştır.\n\nTBK'ya göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Şikâyet bir hak olduğundan bu olayda korkutma söz konusu olamaz',
            'B': 'Hakkın kullanılacağı korkutması tek başına korkutma sayılmaz',
            'C': 'Aşırı menfaat sağlanmışsa korkutmanın varlığı kabul edilir',
            'D': 'Zararın üç katı tutarındaki senet aşırı menfaattir',
            'E': 'Korkutulan taraf sözleşmeyle bağlı olmayabilir',
        },
        'C',
        'TBK m. 38/2: bir hakkın veya kanundan doğan bir yetkinin kullanılacağı korkutmasıyla sözleşme yapıldığında, bunu açıklayanın diğer tarafın zor durumda kalmasından aşırı bir menfaat sağlamış olması hâlinde korkutmanın varlığı kabul edilir. Zararın üç katı tutarında senet aşırı menfaattir.',
        '6098 sayılı TBK m. 38/2',
    ),
    # düzey 2
    '0016': patch(
        "A, aldatılarak yaptığı bir sözleşmedeki aldatmayı 5 Şubat 2025'te öğrenmiştir. A, sözleşmeyle bağlı olmadığını en geç hangi tarihe kadar bildirmelidir?",
        {
            'A': '5 Şubat 2026',
            'B': '5 Şubat 2027',
            'C': '5 Şubat 2030',
            'D': '5 Ağustos 2025',
            'E': '31 Aralık 2025',
        },
        'A',
        "TBK m. 39'a göre yanılma veya aldatma sebebiyle sözleşme yapan taraf, **yanılma veya aldatmayı öğrendiği andan başlayarak bir yıl içinde** sözleşmeyle bağlı olmadığını bildirmez veya verdiği şeyi geri istemezse, sözleşmeyi onamış sayılır.",
        '6098 sayılı TBK m. 39',
    ),
    # düzey 3
    '0017': patch(
        'Aşağıdakilerden hangileri esaslı yanılmadır?\n\nI. Gerçekte üstlenmek istediğinden önemli ölçüde fazla bir edim için irade açıklaması\n\nII. Toplam tutarın hesaplanmasındaki basit bir hesap yanlışlığı\n\nIII. Karşı tarafça bilinmesi mümkün olmayan saikte yanılma',
        {
            'A': 'I, II ve III',
            'B': 'I ve II',
            'C': 'Yalnız I',
            'D': 'Yalnız II',
            'E': 'I ve III',
        },
        'C',
        "TBK m. 31/5'e göre üstlenmek istediğinden **önemli ölçüde fazla** edim için irade açıklaması esaslıdır (I). Basit hesap yanlışlıkları yalnız düzeltilir (II). m. 32'ye göre saikte yanılmanın esaslı sayılması için **karşı tarafça bilinebilir** olması gerekir (III).",
        '6098 sayılı TBK m. 31, 32',
    ),
    # düzey 2
    '0018': patch(
        'Genel işlem koşullarına ilişkin olaylardan hangisinde varılan sonuç yanlıştır?',
        {
            'A': 'Sözleşmenin niteliğine yabancı koşul yazılmamış sayılmıştır',
            'B': 'Belirsiz bir koşul, düzenleyen şirketin lehine yorumlanmıştır',
            'C': 'Yazılmamış sayılan koşul dışındaki hükümler geçerli kabul edilmiştir',
            'D': 'Tek yanlı faiz değiştirme yetkisi veren kayıt yazılmamış sayılmıştır',
            'E': 'Bilgi verilmeden konulan aleyhe koşul yazılmamış sayılmıştır',
        },
        'B',
        "TBK m. 23'e göre açık ve anlaşılır olmayan veya birden çok anlama gelen hüküm **düzenleyenin aleyhine, karşı tarafın lehine** yorumlanır. m. 21, 22 ve 24'teki sonuçlar doğrudur.",
        '6098 sayılı TBK m. 20-25',
    ),
    # düzey 2
    '0019': patch(
        "Bir yayınevi, sipariş vermeyen A'ya bir kitap göndermiş ve '10 gün içinde iade edilmezse satın alınmış sayılacaktır' notunu eklemiştir. A kitabı iade etmemiştir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'A iade etmediği için satış sözleşmesi kurulmuştur',
            'B': 'Sözleşme, sürenin bitiminde örtülü kabulle kurulur',
            'C': 'A kitabın bedelinin yarısını öder',
            'D': 'A kitabı özenle saklamak ve iade için yayınevine haber vermekle yükümlüdür',
            'E': 'Öneri sayılmaz; A iade veya saklama yükümlülüğü taşımaz',
        },
        'E',
        "TBK m. 7'ye göre **ısmarlanmamış bir şeyin gönderilmesi öneri sayılmaz**; bu şeyi alan kişi, **onu geri göndermek veya saklamakla yükümlü değildir**. Tek taraflı konulan süre bir sözleşme doğurmaz.",
        '6098 sayılı TBK m. 7',
    ),
    # düzey 3
    '0020': patch(
        'Bir konut kira sözleşmesinde kiracının beş aylık kira bedeli tutarında güvence vermesi kararlaştırılmıştır. Kanun, konut kirasında güvencenin üç aylık kira bedelini aşamayacağını emredici olarak düzenlemektedir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kiracı sözleşmeyi aşırı yararlanma nedeniyle iptal etmelidir',
            'B': 'Aşan kısım hükümsüzdür; sözleşmenin geri kalanı geçerlidir',
            'C': 'Güvence kaydı ancak kiracı itiraz ederse geçersiz olur',
            'D': 'Kira sözleşmesinin tamamı kesin hükümsüzdür',
            'E': 'Güvence kaydı tamamen geçerlidir',
        },
        'B',
        "TBK m. 27'ye göre kanunun **emredici hükmüne aykırı** kayıt kesin hükümsüzdür; m. 27/2'ye göre bir kısım hükümlerin hükümsüzlüğü, bunlar olmaksızın sözleşmenin yapılmayacağı açıkça anlaşılmadıkça diğerlerini etkilemez. Konut kirasında m. 342 güvenceyi üç aylık kira bedeliyle sınırlar.",
        '6098 sayılı TBK m. 27/2, 342',
    ),
    # düzey 3
    '0021': patch(
        "A, B'ye 1 Mart'ta gönderdiği yazılı öneride kabul için 15 Mart'a kadar süre vermiştir. B kabul yanıtını 14 Mart'ta postaya vermiş, yanıt A'ya 17 Mart'ta ulaşmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'A, önerisiyle bağlılıktan kurtulmuştur',
            'B': 'A dilerse aynı koşullarla yeni bir öneri yapabilir',
            'C': 'Belirleyici olan kabulün süre içinde ulaşmasıdır',
            'D': "A, 15 Mart'a kadar önerisiyle bağlıdır",
            'E': 'Kabul süre içinde gönderildiğinden sözleşme kurulmuştur',
        },
        'E',
        "TBK m. 3'e göre kabul için süre belirleyerek öneride bulunan **bu sürenin sona ermesine kadar** önerisiyle bağlıdır; **kabul bu süre içinde kendisine ulaşmazsa** öneren bağlılıktan kurtulur.",
        '6098 sayılı TBK m. 3',
    ),
    # düzey 2
    '0022': patch(
        'Bir kırtasiye yıllardır her ayın başında toptancıya sipariş listesini göndermekte, toptancı da açıkça kabul bildirmeden malları sevk etmektedir. Bu ay da liste gönderilmiş, toptancı reddetmemiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sözleşme ancak mallar teslim edildiğinde kurulur',
            'B': 'Açık kabul olmadığından sözleşme kurulmamıştır',
            'C': 'Toptancının susmasıyla sözleşme kurulmuş sayılır',
            'D': 'Toptancının susması öneriyi reddettiği anlamına gelir',
            'E': 'Sözleşme ancak yazılı olarak kurulabilir',
        },
        'C',
        "TBK m. 6'ya göre öneren, **kanun veya işin özelliği ya da durumun gereği açık bir kabulü beklemek zorunda değilse**, öneri uygun bir sürede reddedilmediği takdirde **sözleşme kurulmuş sayılır** (örtülü kabul). Taraflar arasındaki süregelen uygulama bu durumu gösterir.",
        '6098 sayılı TBK m. 6',
    ),
    # düzey 3
    '0023': patch(
        "A, B'ye bir satış önerisi içeren mektup göndermiş, ertesi gün fikrini değiştirerek geri alma e-postası yollamıştır. Mektup B'ye e-postadan önce ulaşmış, ancak B mektubu açmadan önce e-postayı okumuştur. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Mektup e-postadan önce ulaştığından öneri geçerlidir',
            'B': 'B öneriyi kabul etse de sözleşme kurulmaz',
            'C': 'Geri alma B tarafından öneriden önce öğrenilmiştir',
            'D': 'Aynı kural kabulün geri alınmasında da uygulanır',
            'E': 'Öneri yapılmamış sayılır',
        },
        'A',
        "TBK m. 10'a göre geri alma açıklaması diğer tarafa öneriden önce veya aynı anda ulaşmış **ya da daha sonra ulaşmakla birlikte diğer tarafça öneriden önce öğrenilmiş** olursa öneri yapılmamış sayılır; kural kabulün geri alınmasında da uygulanır.",
        '6098 sayılı TBK m. 10',
    ),
    # düzey 2
    '0024': patch(
        "Hazır olmayanlar arasında yapılan bir öneriye B, kabulünü 10 Nisan'da göndermiş; kabul A'ya 13 Nisan'da ulaşmıştır. Sözleşme hangi tarihten başlayarak hüküm doğurur?",
        {
            'A': '14 Nisan',
            'B': '10 Nisan',
            'C': '13 Nisan',
            'D': '11 Nisan',
            'E': 'Önerinin gönderildiği tarih',
        },
        'B',
        "TBK m. 11/1'e göre **hazır olmayanlar arasında kurulan sözleşmeler, kabulün gönderildiği andan başlayarak** hüküm doğurur. Açık kabulün gerekli olmadığı durumlarda ise önerinin ulaşma anı esas alınır.",
        '6098 sayılı TBK m. 11',
    ),
    # düzey 2
    '0025': patch(
        'Okuma yazma bilmeyen ve imza atamayan bir kişi, yazılı şekle tabi bir sözleşmeyi nasıl imzalayabilir?',
        {
            'A': 'İmza gerekmez; beyan yeterlidir',
            'B': 'Sadece hâkim onayıyla',
            'C': 'Tanık huzurunda sözlü beyanla',
            'D': 'Usulüne göre onaylanmış parmak izi veya mühürle',
            'E': 'Bir yakınının, kendi adına ve onun onayıyla el yazısıyla imza atmasıyla',
        },
        'D',
        "TBK m. 16'ya göre **imza atamayanlar**, imza yerine **usulüne göre onaylanmış olması koşuluyla** parmak izi, el ile yapılmış bir işaret ya da mühür kullanabilirler; kambiyo senetlerine ilişkin hükümler saklıdır.",
        '6098 sayılı TBK m. 16',
    ),
    # düzey 3
    '0026': patch(
        'A ile B, kanunda şekle bağlanmamış bir hizmet alımının yazılı yapılmasını, türünü belirtmeden kararlaştırmıştır. Daha sonra telefonda anlaşmışlar, ancak yazılı metin düzenlememişlerdir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Kanunda şekil öngörülmediğinden telefonla yapılan sözleşme tarafları bağlar',
            'B': 'Taraflar sözleşmenin belirli bir şekilde yapılmasını kararlaştırabilir',
            'C': 'Türü belirtilmeyen yazılı şekil için yasal yazılı şekil hükümleri uygulanır',
            'D': 'Yazılı şekil için borç altına girenlerin imzası aranır',
            'E': 'Belirlenen şekle uyulmayan sözleşme tarafları bağlamaz',
        },
        'A',
        "TBK m. 17'ye göre kanunda şekle bağlanmamış bir sözleşmenin **taraflarca belirli bir şekilde yapılması kararlaştırılmışsa, belirlenen şekilde yapılmayan sözleşme tarafları bağlamaz**; herhangi bir belirleme olmaksızın yazılı şekil kararlaştırılmışsa yasal yazılı şekil hükümleri uygulanır.",
        '6098 sayılı TBK m. 17',
    ),
    # düzey 3
    '0027': patch(
        "Bir bankanın matbu kredi sözleşmesinin sonunda 'Bu sözleşmenin tüm maddeleri taraflarca ayrı ayrı müzakere edilerek kabul edilmiştir' kaydı yer almaktadır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Matbu koşullar önceden düzenleyence tek başına hazırlanmıştır',
            'B': 'Koşulların metinde veya ekte yer alması nitelendirmeyi etkilemez',
            'C': 'İzinle hizmet veren bankaların sözleşmelerine bu hükümler uygulanır',
            'D': 'Kayıt tek başına koşulları genel işlem koşulu olmaktan çıkarmaz',
            'E': 'Kayıt nedeniyle koşullar bireysel olarak müzakere edilmiş sayılır',
        },
        'E',
        "TBK m. 20/3'e göre koşulların her birinin **tartışılarak kabul edildiğine ilişkin kayıtlar, tek başına, onları genel işlem koşulu olmaktan çıkarmaz**; m. 20/4'e göre izinle hizmet veren kuruluşların sözleşmelerine de uygulanır.",
        '6098 sayılı TBK m. 20',
    ),
    # düzey 2
    '0028': patch(
        'Bir cep telefonu hattı abonelik sözleşmesine, abonenin operatörden her yıl ev sigortası satın alacağına dair matbu bir koşul eklenmiştir. Bu koşulun durumu hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Koşul, abonenin lehine yorumlanarak uygulanır',
            'B': 'Koşul yüzünden sözleşmenin tamamı kesin hükümsüzdür',
            'C': 'Koşul ancak abone itiraz ederse iptal edilir',
            'D': 'Niteliğe yabancı koşul olarak yazılmamış sayılır',
            'E': 'Abone imzaladığı için geçerlidir',
        },
        'D',
        "TBK m. 21/2'ye göre **sözleşmenin niteliğine ve işin özelliğine yabancı olan genel işlem koşulları da yazılmamış sayılır**.",
        '6098 sayılı TBK m. 21/2',
    ),
    # düzey 2
    '0029': patch(
        'Bir bankanın genel işlem koşullarında, bankaya kredi faiz oranını müşteri aleyhine tek taraflı olarak değiştirme yetkisi veren bir kayıt bulunmaktadır. Bu kaydın durumu hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Faiz oranını yarı oranda artırma yetkisi verir',
            'B': 'Kayıt nedeniyle kredi sözleşmesinin tamamı hükümsüz hâle gelir ve iade doğar',
            'C': 'Düzenleyene tek yanlı değiştirme yetkisi verdiğinden yazılmamış sayılır',
            'D': 'Kayıt ancak müşteri tüketiciyse geçersizdir',
            'E': 'Müşteri imzaladığı için geçerlidir',
        },
        'C',
        "TBK m. 24'e göre genel işlem koşulları içeren bir sözleşmede **düzenleyene tek yanlı olarak karşı taraf aleyhine sözleşmenin bir hükmünü değiştirme ya da yeni düzenleme getirme yetkisi veren kayıtlar yazılmamış sayılır**.",
        '6098 sayılı TBK m. 24',
    ),
    # düzey 3
    '0030': patch(
        "A, evini B'ye satmış; sözleşme kurulduktan iki gün sonra ve teslimden önce ev, A'nın kusuru olmadan yıldırım düşmesiyle yanmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "A'nın kusuru yoksa borcu sona erebilir",
            'B': 'İmkânsızlık sözleşme kurulduktan sonra doğmuştur',
            'C': 'Konusu imkânsız olduğundan sözleşme kesin hükümsüzdür',
            'D': 'Durum ifa imkânsızlığı hükümlerine göre değerlendirilir',
            'E': 'Kesin hükümsüzlük, kurulma anında var olan imkânsızlık için söz konusudur',
        },
        'C',
        "TBK m. 27'deki kesin hükümsüzlük, **sözleşme kurulurken** edimin imkânsız olmasına ilişkindir. İmkânsızlık **sonradan** doğmuşsa sözleşme geçerli kurulmuştur; sonuç m. 136 vd. ifa imkânsızlığı hükümlerine göre belirlenir.",
        '6098 sayılı TBK m. 27, 136',
    ),
    # düzey 3
    '0031': patch(
        "Aşırı yararlanmaya dayanan bir sözleşme 2022'de kurulmuş; zarar gören deneyimsizliğini 1 Mart 2025'te öğrenmiştir. Zarar gören, aşırı yararlanmadan doğan hakkını en geç hangi tarihe kadar kullanabilir?",
        {
            'A': '1 Mart 2030',
            'B': '1 Mart 2027',
            'C': '2027 yılı sonuna kadar',
            'D': '1 Mart 2026',
            'E': '31 Aralık 2025',
        },
        'D',
        "TBK m. 28/2'ye göre zarar gören bu hakkını, **düşüncesizlik veya deneyimsizliğini öğrendiği** tarihten başlayarak **bir yıl** ve her hâlde sözleşmenin kurulduğu tarihten başlayarak **beş yıl** içinde kullanabilir. Bir yıllık süre (1 Mart 2026) beş yıllık süreden (2027) önce dolar.",
        '6098 sayılı TBK m. 28/2',
    ),
    # düzey 2
    '0032': patch(
        "A, bir sitede 3 numaralı daireyi satın almak isterken dalgınlıkla 5 numaralı dairenin satış sözleşmesini imzalamıştır. A'nın durumu hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Saikte yanılma olduğundan sözleşmeyle bağlıdır',
            'B': 'A, konuda esaslı yanılmaya düşmüştür',
            'C': 'Sözleşme kesin hükümsüzdür',
            'D': 'Aldatma olmadığından sözleşmeyle bağlıdır',
            'E': 'Basit hesap yanlışlığı olduğundan düzeltme yapılır',
        },
        'B',
        "TBK m. 31/2'ye göre yanılanın **istediğinden başka bir konu için iradesini açıklaması** esaslı yanılmadır; m. 30'a göre esaslı yanılmaya düşen taraf sözleşmeyle bağlı olmaz.",
        '6098 sayılı TBK m. 31',
    ),
    # düzey 3
    '0033': patch(
        "Bir alım sözleşmesinde birim fiyat 100 ₺ ve adet 50 olarak doğru yazılmış, ancak toplam tutar 5.500 ₺ olarak hesaplanmıştır. Alıcının ödemesi gereken tutar kaç ₺'dir?",
        {
            'A': '5.250',
            'B': '4.500',
            'C': '5.500',
            'D': '0',
            'E': '5.000',
        },
        'E',
        "TBK m. 31/2 son cümlesine göre **basit hesap yanlışlıkları sözleşmenin geçerliliğini etkilemez; bunların düzeltilmesi ile yetinilir**. Doğru hesap 100 × 50 = **5.000 ₺**'dir.",
        '6098 sayılı TBK m. 31',
    ),
    # düzey 3
    '0034': patch(
        'A, 3 numaralı daireyi almak isterken yanılarak 5 numaralı daire için sözleşme imzalamış ve yanıldığını bildirmiştir. Satıcı B, sözleşmenin 3 numaralı daire için aynı koşullarla kurulmasına razı olduğunu hemen açıklamıştır. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sözleşme 3 numaralı daire için kurulmuş sayılır',
            'B': "A, B'ye tazminat ödeyerek sözleşmeden kurtulur",
            'C': 'Taraflar yeni bir sözleşme yapmadıkça bağ doğmaz',
            'D': 'Sözleşme 5 numaralı daire için geçerlidir',
            'E': 'A yanılma nedeniyle sözleşmeyle bağlı değildir',
        },
        'A',
        "TBK m. 34'e göre yanılan, yanıldığını dürüstlük kurallarına aykırı olarak ileri süremez; özellikle **diğer tarafın, sözleşmenin yanılanın kastettiği anlamda kurulmasına razı olduğunu bildirmesi durumunda, sözleşme bu anlamda kurulmuş sayılır**.",
        '6098 sayılı TBK m. 34',
    ),
    # düzey 3
    '0035': patch(
        "A'yı korkutan, sözleşmenin tarafı olmayan üçüncü kişi C'dir. Karşı taraf B, korkutmayı bilmemekte ve bilecek durumda da değildir. A sözleşmeyle bağlı kalmak istememektedir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': "A, B'ye hakkaniyete bakılmaksızın tam tazminat öder",
            'B': 'A, B korkutmayı bilmediği için sözleşmeyle bağlıdır',
            'C': 'A bağlı değildir; hakkaniyet gerekirse tazminat öder',
            'D': 'Sözleşme kesin hükümsüzdür',
            'E': "A ancak C'nin onayıyla sözleşmeden kurtulur",
        },
        'C',
        "TBK m. 37'ye göre taraflardan biri **diğerinin veya üçüncü bir kişinin korkutması** sonucu sözleşme yapmışsa bağlı değildir. Korkutan üçüncü kişi olup da diğer taraf korkutmayı bilmiyor veya bilecek durumda değilse, bağlı kalmak istemeyen korkutulan **hakkaniyet gerektiriyorsa diğer tarafa tazminat** öder. Üçüncü kişinin aldatmasından (m. 36/2) farkı budur.",
        '6098 sayılı TBK m. 37/2',
    ),
    # düzey 3
    '0036': patch(
        'Aşağıdaki hâllerden hangilerinde irade bozukluğuna uğrayan taraf sözleşmeyle bağlı olmaz?\n\nI. Karşı tarafın aldatması, yanılma esaslı değil\n\nII. Üçüncü kişinin aldatması, karşı taraf bilmiyor ve bilecek durumda değil\n\nIII. Üçüncü kişinin korkutması, karşı taraf bilmiyor ve bilecek durumda değil',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'Yalnız I',
            'D': 'I ve III',
            'E': 'I, II ve III',
        },
        'D',
        "TBK m. 36/1'e göre karşı tarafın aldatmasında yanılma esaslı olmasa da bağlılık yoktur (I). m. 36/2'ye göre üçüncü kişinin aldatmasında karşı taraf bilmiyor ve bilecek durumda değilse bağlılık devam eder (II). m. 37'ye göre üçüncü kişinin korkutmasında korkutulan, karşı taraf bilmese de bağlı değildir; hakkaniyet gerektirirse tazminat öder (III).",
        '6098 sayılı TBK m. 36, 37',
    ),
    # düzey 2
    '0037': patch(
        'Bir anonim şirket, yüz binlerce adet çıkardığı hisse senetlerini yöneticilerinin makineyle basılmış imzalarıyla imzalamıştır. Bu imzanın geçerliliği hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Çok sayıda çıkarılan kıymetli evrakta el yazısı dışındaki imza yeterli sayılır',
            'B': 'İmza el yazısıyla atılmadığından senetler geçersizdir',
            'C': 'Senetler ancak parmak iziyle tamamlanırsa geçerli olur',
            'D': 'Makine imzası ancak noter onayıyla geçerli olur',
            'E': 'Makine imzası, güvenli elektronik imza eklenirse geçerlidir',
        },
        'A',
        "TBK m. 15'e göre imzanın **borç altına girenin el yazısıyla atılması zorunludur**; ancak imzanın el yazısı dışında bir araçla atılması, **örf ve âdetçe kabul edilen durumlarda ve özellikle çok sayıda çıkarılan kıymetli evrakın imzalanmasında** yeterli sayılır.",
        '6098 sayılı TBK m. 15',
    ),
    # düzey 3
    '0038': patch(
        'Bir özel okulun kayıt sözleşmesindeki genel işlem koşuluna göre, öğrenci eğitim yılının ilk haftasında kaydını sildirse bile yıllık ücretin tamamı iade edilmeyecektir. Bu koşul hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Koşul ancak okul kâr amacı güdüyorsa geçersizdir',
            'B': 'Okulun lehine yorumlanarak uygulanır',
            'C': 'Karşı taraf aleyhine olduğundan konulamaz',
            'D': 'Koşul yüzünden sözleşmenin tamamı hükümsüzdür',
            'E': 'Veli imzaladığından geçerlidir',
        },
        'C',
        "TBK m. 25'e göre **genel işlem koşullarına, dürüstlük kurallarına aykırı olarak, karşı tarafın aleyhine veya onun durumunu ağırlaştırıcı nitelikte hükümler konulamaz** (içerik denetimi).",
        '6098 sayılı TBK m. 25',
    ),
    # düzey 2
    '0039': patch(
        "B, A'ya evini düşük bir fiyata satmazsa küçük çocuğuna zarar vereceğini ciddi biçimde söylemiş; A bu tehdide inanarak evini satmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Bir yıllık süre korkutmanın etkisinin kalkmasıyla başlar',
            'B': "Tehdit A'ya değil çocuğuna yöneldiğinden korkutma yoktur",
            'C': "Tehdit A'nın yakınının kişilik haklarına yöneliktir",
            'D': 'A, tehdide inanmakta haklıdır',
            'E': 'A sözleşmeyle bağlı değildir',
        },
        'B',
        "TBK m. 38/1'e göre korkutulan **kendisinin veya yakınlarından birinin kişilik haklarına ya da malvarlığına yönelik ağır ve yakın bir zarar tehlikesinin** doğduğuna inanmakta haklı ise korkutma gerçekleşmiş sayılır; m. 37'ye göre bağlı değildir, m. 39'a göre süre korkutmanın etkisi kalkınca başlar.",
        '6098 sayılı TBK m. 37, 38',
    ),
    # düzey 3
    '0040': patch(
        'Yazılı şekle tabi bir kefalet sözleşmesinde metni yalnızca kefil imzalamış, alacaklı banka imzalamamıştır. İmza yönünden sözleşmenin geçerliliği hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Her iki tarafın imzası bulunmadığından sözleşme geçersizdir',
            'B': 'Bankaların taraf olduğu sözleşmelerde imza şartı aranmaz',
            'C': 'Sözleşme ancak noter onayıyla geçerli olur',
            'D': 'Borç altına giren kefilin imzası yeterlidir',
            'E': 'Alacaklının imzası eksik olduğundan kefil yarı oranda sorumludur',
        },
        'D',
        "TBK m. 14/1'e göre yazılı şekilde yapılması öngörülen sözleşmelerde **borç altına girenlerin imzalarının bulunması zorunludur**. Kefalette borç altına giren kefil olduğundan onun imzası yeterlidir; diğer şekil şartları (m. 583) ayrıca aranır.",
        '6098 sayılı TBK m. 14/1',
    ),
    # düzey 2
    '0041': patch(
        "A, telefonla aradığı B'ye malını 50.000 ₺'ye satmayı önermiş, süre belirtmemiştir. B 'düşünüp yarın haber vereyim' demiş ve ertesi gün kabul ettiğini bildirmiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "A dilerse B'nin yeni önerisini kabul edebilir",
            'B': 'Telefonla yapılan öneri hazır olmayanlar arasında yapılmış sayılır',
            'C': 'Öneri hemen kabul edilmediğinden A bağlılıktan kurtulmuştur',
            'D': "B'nin ertesi günkü açıklaması yeni bir öneri niteliği taşır",
            'E': 'Öneri hazır olanlar arasında yapılmış sayılır',
        },
        'B',
        "TBK m. 4'e göre **telefon gibi araçlarla doğrudan iletişim sırasında yapılan öneri hazır olanlar arasında yapılmış sayılır**; süre belirlenmeksizin hazır olan kişiye yapılan öneri **hemen kabul edilmezse** öneren bağlılıktan kurtulur. Geç kabul yeni bir öneri olarak değerlendirilebilir.",
        '6098 sayılı TBK m. 4',
    ),
    # düzey 3
    '0042': patch(
        'Bir toptancı, müşterilerine ürünlerinin birim fiyatlarını gösteren bir liste göndermiş; listede bağlayıcılıkla ilgili bir açıklama yoktur. Bir müşteri listedeki fiyattan sipariş vermiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Fiyat listesi öneriye çağrıdır; sözleşme toptancının onayıyla kurulur',
            'B': 'Fiyat listesi gönderilmesi kural olarak öneri sayılır',
            'C': 'Müşterinin siparişi kabul niteliği taşır',
            'D': 'Aksi açıkça ve kolaylıkla anlaşılsaydı öneri sayılmazdı',
            'E': 'Sözleşme listedeki fiyat üzerinden kurulur',
        },
        'A',
        "TBK m. 8/2'ye göre **fiyatını göstererek mal sergilenmesi veya tarife, fiyat listesi ya da benzerlerinin gönderilmesi, aksi açıkça ve kolaylıkla anlaşılmadıkça öneri sayılır**; müşterinin siparişiyle sözleşme kurulur.",
        '6098 sayılı TBK m. 8/2',
    ),
    # düzey 3
    '0043': patch(
        "A, kaybolan köpeğini bulana 10.000 ₺ ödül vereceğini ilan etmiş; köpek bulunmadan sözünden caymıştır. Arama için dürüstlük kurallarına uygun olarak B 7.000 ₺, C 6.000 ₺ gider yapmıştır. A'nın ödemesi gereken toplam tutar en fazla kaç ₺'dir?",
        {
            'A': '13.000',
            'B': '20.000',
            'C': '7.000',
            'D': '6.500',
            'E': '10.000',
        },
        'E',
        "TBK m. 9/2'ye göre ödül sözü veren, sonucun gerçekleşmesinden önce cayarsa dürüstlük kurallarına uygun olarak yapılan giderleri ödemekle yükümlüdür; ancak **bir ya da birden çok kişiye ödenecek giderlerin toplamı ödülün değerini aşamaz**: 7.000 + 6.000 = 13.000 ₺ yerine **10.000 ₺**.",
        '6098 sayılı TBK m. 9',
    ),
    # düzey 2
    '0044': patch(
        'Öneri ve kabule ilişkin olaylardan hangisinde varılan sonuç yanlıştır?',
        {
            'A': 'Geri alma öneriyle aynı anda ulaşırsa öneri yapılmamış sayılır',
            'B': 'Açık kabulün gerekli olmadığı durumlarda sözleşme önerinin ulaşma anından başlayarak hüküm doğurur',
            'C': 'Ödül ilanından cayan kişi, sonuca ulaşılamayacağını ispat etse de gideri öder',
            'D': 'Kabulün geri alınmasına da geri alma kuralları uygulanır',
            'E': 'Ödül ilanı yapan, sonuç gerçekleşirse sözünü yerine getirir',
        },
        'C',
        "TBK m. 9/3'e göre ödül sözü veren, **giderlerinin ödenmesini isteyenlerin beklenen sonucu gerçekleştiremeyeceklerini ispat ederse, giderleri ödeme yükümlülüğünden kurtulur**. m. 10 geri almayı, m. 11 hüküm anını düzenler.",
        '6098 sayılı TBK m. 9, 10, 11',
    ),
    # düzey 3
    '0045': patch(
        'Aşağıdakilerden hangileri, kanunda aksi öngörülmedikçe yazılı şekil yerine geçer?\n\nI. Güvenli elektronik imza taşımayan sıradan bir e-posta\n\nII. Borç altına girenin imzaladığı mektup\n\nIII. Teyit edilmiş faks',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız II',
            'C': 'Yalnız III',
            'D': 'II ve III',
            'E': 'I ve II',
        },
        'D',
        "TBK m. 14/2'ye göre **imzalı bir mektup**, asılları borç altına girenlerce imzalanmış telgraf, **teyit edilmiş olmaları kaydıyla faks** veya benzeri araçlar ya da **güvenli elektronik imza** ile gönderilip saklanabilen metinler yazılı şekil yerine geçer. İmzasız sıradan e-posta bu kapsamda değildir.",
        '6098 sayılı TBK m. 14',
    ),
    # düzey 2
    '0046': patch(
        "A, B'ye imzaladığı bir belgede '50.000 ₺ borçluyum' yazmış, ancak borcun hangi sebepten doğduğunu belirtmemiştir.\n\nTBK'ya göre bu borç tanımasıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Borç tanıması borcun sebebini içermese de geçerlidir',
            'B': 'Borç tanıması sebep ispat edilinceye kadar askıdadır',
            'C': 'Sebep gösterilmemesi kesin hükümsüzlük doğurmaz',
            'D': 'Borç tanımasının noterde yapılması şart değildir',
            'E': 'Kural tacir olmayanlar için de geçerlidir',
        },
        'B',
        'TBK m. 18: borcun sebebini içermemiş olsa bile borç tanıması geçerlidir; geçerlilik sebebin ispatına, noter onayına ya da tacir sıfatına bağlı değildir.',
        '6098 sayılı TBK m. 18',
    ),
    # düzey 2
    '0047': patch(
        'Bir sigorta şirketi, farklı müşterileri için kullandığı poliçe metinlerinde küçük sözcük farklılıkları yapmıştır. Bu durumun genel işlem koşulu niteliğine etkisi hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sigorta sözleşmelerine genel işlem koşulu hükümleri uygulanmaz',
            'B': 'Metinler farklı olduğundan genel işlem koşulu söz konusu olmaz',
            'C': 'Ancak her poliçede aynı kelimeler varsa genel işlem koşulu vardır',
            'D': 'Farklılık varsa hükümler müşteri lehine geçerli sayılır',
            'E': 'Metin farklılığı genel işlem koşulu sayılmayı engellemez',
        },
        'E',
        "TBK m. 20/2'ye göre **aynı amaçla düzenlenen sözleşmelerin metinlerinin özdeş olmaması**, içerdiği hükümlerin genel işlem koşulu sayılmasını engellemez. m. 20/4'e göre izinle hizmet veren kuruluşların sözleşmelerine de bu hükümler uygulanır.",
        '6098 sayılı TBK m. 20',
    ),
    # düzey 3
    '0048': patch(
        'Bir spor salonunun üyelik sözleşmesinde, üyenin sakatlanması hâlinde salonun hiçbir sorumluluk üstlenmediğine dair küçük puntolu bir koşul bulunmakta, üyeye bu koşul hakkında ayrıca bilgi verilmemiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Bilgi verilmediğinden koşul yazılmamış sayılır',
            'B': 'Koşul karşı tarafın menfaatine aykırıdır',
            'C': 'Üye imzaladığı için koşul sözleşmeye girmiştir',
            'D': 'Sözleşmenin diğer hükümleri geçerliliğini korur',
            'E': 'Koşulun kapsama girmesi açıkça bilgi verilmesine bağlıdır',
        },
        'C',
        "TBK m. 21'e göre karşı tarafın menfaatine aykırı genel işlem koşullarının sözleşmenin kapsamına girmesi, düzenleyenin **bu koşulların varlığı hakkında açıkça bilgi verip içeriğini öğrenme imkânı sağlamasına** ve karşı tarafın kabulüne bağlıdır; aksi hâlde **yazılmamış sayılır**. m. 22'ye göre diğer hükümler geçerliliğini korur.",
        '6098 sayılı TBK m. 21',
    ),
    # düzey 3
    '0049': patch(
        'Aşağıdakilerden hangileri yazılmamış sayılır?\n\nI. Açıkça bilgi verilmeden kabul ettirilen, karşı taraf aleyhine genel işlem koşulu\n\nII. Düzenleyene tek yanlı değişiklik yetkisi veren kayıt\n\nIII. Karşı tarafın lehine olan ve bireysel olarak müzakere edilmiş hüküm',
        {
            'A': 'I ve III',
            'B': 'Yalnız II',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'D',
        "TBK m. 21'e göre **açıkça bilgi verilmeden kabul ettirilen karşı taraf aleyhine koşullar** (I) ve m. 24'e göre **düzenleyene tek yanlı değiştirme yetkisi veren kayıtlar** (II) yazılmamış sayılır. Müzakere edilmiş lehe hüküm geçerlidir (III).",
        '6098 sayılı TBK m. 21-24',
    ),
    # düzey 3
    '0050': patch(
        'Bir sözleşmedeki fahiş faiz hükmü kesin hükümsüzdür. Taraflar, bu hüküm olmaksızın sözleşmeyi hiç yapmayacaklarını açıkça ortaya koymuştur. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sözleşmenin tamamı hükümsüz hâle gelir',
            'B': 'Sözleşme iptal edilebilir niteliktedir',
            'C': 'Faiz hükmü hükümsüzdür; diğer hükümler geçerliliğini korur',
            'D': 'Sözleşmenin tamamı ancak alacaklı isterse hükümsüz olur',
            'E': 'Faiz hükmü yasal faize indirilerek sözleşme ayakta tutulur',
        },
        'A',
        "TBK m. 27/2'ye göre sözleşmenin bazı hükümlerinin hükümsüz olması kural olarak diğerlerinin geçerliliğini etkilemez; ancak **bu hükümler olmaksızın sözleşmenin yapılmayacağı açıkça anlaşılırsa sözleşmenin tamamı kesin olarak hükümsüz** olur.",
        '6098 sayılı TBK m. 27/2',
    ),
    # düzey 2
    '0051': patch(
        'Bir kişinin, bir kulüple yaptığı sözleşmede ömür boyu başka hiçbir kulüpte spor yapmamayı ve evlenmemeyi taahhüt etmesi hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Taahhütler iptal edilebilir niteliktedir',
            'B': 'Hâkim taahhütleri makul süreye indirerek uygular',
            'C': 'Taahhütler kişilik haklarına aykırı ve hükümsüzdür',
            'D': 'Sözleşme özgürlüğü gereği geçerlidir',
            'E': 'Taahhütler ancak ceza koşulu varsa geçerlidir',
        },
        'C',
        "TBK m. 27'ye göre **kanunun emredici hükümlerine, ahlaka, kamu düzenine, kişilik haklarına aykırı** veya konusu imkânsız olan sözleşmeler kesin olarak hükümsüzdür. Kişinin ekonomik ve kişisel özgürlüğünü aşırı biçimde sınırlayan taahhütler kişilik haklarına aykırıdır.",
        '6098 sayılı TBK m. 27',
    ),
    # düzey 3
    '0052': patch(
        "A ile B, A'ya ait bir taşınmazın ileride B'ye satılacağını adi yazılı bir sözleşmeyle kararlaştırmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Taşınmaz satışı resmî şekle tabidir',
            'B': 'Önsözleşmenin geçerliliği ileride kurulacak sözleşmenin şekline bağlıdır',
            'C': 'Resmî şekle uyulmayan bu önsözleşme hüküm doğurmaz',
            'D': 'Önsözleşmeler kural olarak geçerlidir',
            'E': 'Önsözleşmeler şekle bağlı olmadığından bu sözleşme geçerlidir',
        },
        'E',
        "TBK m. 29'a göre önsözleşmeler geçerlidir; ancak kanunlarda öngörülen istisnalar dışında **önsözleşmenin geçerliliği, ileride kurulacak sözleşmenin şekline bağlıdır**. Taşınmaz satışı resmî şekle tabidir.",
        '6098 sayılı TBK m. 29',
    ),
    # düzey 3
    '0053': patch(
        "Yabancı bir şirket, Türk tedarikçiye verdiği siparişi bir çevirmen aracılığıyla iletmiş; çevirmen '1.000 adet' yerine '10.000 adet' çevirmiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Çevirmenin hatası şirkete ait olduğundan şirket 10.000 adetle bağlıdır',
            'B': 'Şirket sözleşmeyle bağlı olmadığını bildirebilir',
            'C': 'Yanılmada kusuru varsa şirket karşı tarafın zararını gidermekle yükümlüdür',
            'D': 'Miktardaki önemli fark esaslı yanılma oluşturur',
            'E': 'İradenin aracı tarafından yanlış iletilmesinde yanılma hükümleri uygulanır',
        },
        'A',
        "TBK m. 33'e göre iradenin **haberci veya çevirmen gibi bir aracı** tarafından yanlış iletilmesinde de yanılma hükümleri uygulanır; m. 31/5'e göre önemli ölçüde fazla edim esaslı yanılmadır. m. 35'e göre kusurlu yanılan hükümsüzlükten doğan zararı giderir.",
        '6098 sayılı TBK m. 33, 35',
    ),
    # düzey 2
    '0054': patch(
        "Satıcı B, aracın kazalı olduğunu bildiği hâlde kaza yapmadığını söyleyerek A'yı ikna etmiştir. A'nın yanılması esaslı yanılma hâllerinden birine girmemektedir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'A sözleşmeyle bağlı değildir',
            'B': 'Yanılma esaslı olmadığından A sözleşmeyle bağlıdır',
            'C': "B, A'yı aldatmıştır",
            'D': 'A, aldatmayı öğrendiği andan itibaren bir yıl içinde bildirimde bulunmalıdır',
            'E': 'A sözleşmeyi onamış sayılsa bile tazminat isteyebilir',
        },
        'B',
        "TBK m. 36/1'e göre taraflardan biri **diğerinin aldatması sonucu** bir sözleşme yapmışsa, **yanılması esaslı olmasa bile** sözleşmeyle bağlı değildir; m. 39'a göre bir yıllık süre öğrenmeden başlar ve onama tazminat hakkını kaldırmaz.",
        '6098 sayılı TBK m. 36, 39',
    ),
    # düzey 3
    '0055': patch(
        "A'yı aldatan, sözleşmenin tarafı olmayan üçüncü kişi C'dir. Sözleşmenin karşı tarafı B, aldatmayı bilmemekte ve bilecek durumda da değildir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': "A, B'ye tazminat ödeyerek sözleşmeden kurtulur",
            'B': 'A sözleşmeyle bağlı değildir',
            'C': "Sözleşme C'nin onayıyla geçerli olur",
            'D': 'A sözleşmeyle bağlıdır',
            'E': 'Sözleşme kesin hükümsüzdür',
        },
        'D',
        "TBK m. 36/2'ye göre üçüncü bir kişinin aldatması sonucu sözleşme yapan taraf, ancak **sözleşmenin yapıldığı sırada karşı tarafın aldatmayı bilmesi veya bilecek durumda olması hâlinde** sözleşmeyle bağlı değildir. Bu koşul yoksa sözleşmeyle bağlıdır; C'ye karşı haksız fiil istemi saklıdır.",
        '6098 sayılı TBK m. 36/2',
    ),
    # düzey 3
    '0056': patch(
        "A, ağır bir tehdit altında 1 Haziran 2024'te bir sözleşme imzalamış; tehdidin etkisi, tehdit edenin tutuklanmasıyla 1 Ekim 2024'te ortadan kalkmıştır. A'nın sözleşmeyle bağlı olmadığını bildirme süresi hangi tarihte sona erer?",
        {
            'A': '1 Ekim 2026',
            'B': '1 Ekim 2025',
            'C': '1 Ocak 2026',
            'D': '1 Haziran 2029',
            'E': '1 Haziran 2025',
        },
        'B',
        "TBK m. 39'a göre korkutulma sonucunda sözleşme yapan taraf için bir yıllık süre, **korkutmanın etkisinin ortadan kalktığı andan** başlar: 1 Ekim 2024 + 1 yıl = **1 Ekim 2025**.",
        '6098 sayılı TBK m. 39',
    ),
    # düzey 2
    '0057': patch(
        "Aldatılarak sözleşme yapan A, bir yıllık süre içinde bağlı olmadığını bildirmemiş ve sözleşmeyi onamış sayılmıştır.\n\nTBK'ya göre A'nın aldatmadan doğan zararlarıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Aldatılan bir yıl içinde bildirmezse sözleşmeyi onamış sayılır',
            'B': 'Onanan sözleşme geçerlilik kazanır',
            'C': 'Onama tazminat hakkını ortadan kaldırmaz',
            'D': 'Tazminat için sözleşmenin iptali şart değildir',
            'E': 'Onama ile tazminat hakkı da düşer',
        },
        'E',
        'TBK m. 39: aldatılan, öğrenmeden itibaren bir yıl içinde bağlı olmadığını bildirmezse sözleşmeyi onamış sayılır. m. 39/2: aldatma veya korkutmadan dolayı bağlayıcılığı olmayan bir sözleşmenin onanmış sayılması tazminat hakkını ortadan kaldırmaz.',
        '6098 sayılı TBK m. 39/2',
    ),
    # düzey 3
    '0058': patch(
        'Sözleşmedeki haklara ilişkin sürelerden hangileri doğrudur?\n\nI. Aşırı yararlanmada hak, deneyimsizliğin öğrenilmesinden bir yıl ve her hâlde sözleşmeden beş yıl içinde kullanılır\n\nII. Aldatmada bir yıllık süre aldatmanın öğrenilmesinden başlar\n\nIII. Korkutmada bir yıllık süre sözleşmenin kurulmasından başlar',
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'II ve III',
            'D': 'Yalnız II',
            'E': 'I, II ve III',
        },
        'A',
        "TBK m. 28/2'ye göre aşırı yararlanmada hak **bir yıl ve her hâlde beş yıl** içinde kullanılır (I). m. 39'a göre aldatmada süre **öğrenmeden** (II), korkutmada ise **korkutmanın etkisinin ortadan kalktığı andan** başlar (III yanlış).",
        '6098 sayılı TBK m. 28, 39',
    ),
    # düzey 2
    '0059': patch(
        "A, B'ye mektupla süre belirtmeden bir satış önerisi göndermiş; B, önerinin kendisine ulaşmasından iki ay sonra kabul ettiğini bildirmiştir. Posta yoluyla olağan yanıt süresi birkaç gündür. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Hazır olmayanlar arasında öneri bir yıl süreyle bağlar',
            'B': 'Öneren iki ay boyunca önerisiyle bağlıdır',
            'C': 'Yanıt süresi geçtiğinden A bağlı değildir',
            'D': "B'nin kabulüyle sözleşme kurulmuştur",
            'E': 'Süresiz öneri öneren geri alıncaya kadar bağlayıcıdır',
        },
        'C',
        "TBK m. 5/1'e göre süre belirlenmeksizin hazır olmayan bir kişiye yapılan öneri, **zamanında ve usulüne uygun olarak gönderilmiş bir yanıtın ulaşmasının beklenebileceği ana kadar** önereni bağlar. Bu süre geçtikten sonra yapılan kabul öneren için bağlayıcı değildir.",
        '6098 sayılı TBK m. 5',
    ),
    # düzey 3
    '0060': patch(
        "B, A'nın önerisini kabul ettiğini bildiren mektubu postaya vermiş; ertesi gün fikrini değiştirerek A'yı telefonla aramış ve kabulünü geri almıştır. Telefon görüşmesi, kabul mektubu A'ya ulaşmadan önce yapılmıştır. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Kabulün geri alınması mümkün değildir',
            'B': 'Geri alma ancak yazılı yapılabilir',
            'C': 'Kabul gönderildiği anda hüküm doğurduğundan sözleşme kurulmuştur',
            'D': 'Geri alma kabulden önce ulaştığından kabul yapılmamış sayılır',
            'E': "B, A'ya tazminat ödeyerek sözleşmeden kurtulur",
        },
        'D',
        "TBK m. 10'a göre geri alma açıklaması diğer tarafa **önceden veya aynı anda ulaşırsa** ya da sonra ulaşmakla birlikte önce öğrenilirse açıklama yapılmamış sayılır; **bu kural kabulün geri alınmasında da uygulanır**.",
        '6098 sayılı TBK m. 10/2',
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
    print(f"1 paket / {len(PATCHES)} soru ('Sozlesmenin Kurulmasi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
