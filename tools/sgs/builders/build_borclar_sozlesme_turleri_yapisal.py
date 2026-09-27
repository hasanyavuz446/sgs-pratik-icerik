#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sozlesme Turleri — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Borclar hukuku gercek sinav profiliyle yeniden yazim (eski surumde tum sorular 'X bakimindan hangisi dogrudur' tanim kalibindaydi, kor %65): satis (yarar-hasar, zapt, ayip ve bildirim, secimlik haklar, zamanasimi, sekil, taksitle satis), bagislama (sekil, oneri, sorumluluk, geri alma), kira (TUFE siniri, guvence, temerrut, uzama ve fesih, alt kira, el degistirme, erken tahliye, iki hakli ihtar), odunc, hizmet, eser (bizzat ifa, ayip, kabul, zamanasimi, goturu bedel, fesih), vekalet, simsarlik ve kefalet (sekil, es rizasi, adi/muteselsil, azami miktar, def'iler, on yil). Kurallar olaylara, surelere ve tutarlara uygulatildi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 6098 sayili Turk Borclar Kanunu m. 207-256, 285-297, 299-352, 379-394, 470-485, 502-521, 581-598 guncel metni (mevzuat.gov.tr)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/borclar_hukuku/sozlesme_turleri.json"
STYLE_REF = 'SGS Borclar Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "sozturu-gen-"


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
        "A, B'ye sattığı otomobili teslim etmeden önce, tarafların kusuru olmaksızın çıkan bir otopark yangınında otomobil yanmıştır. Sözleşmede yarar ve hasara ilişkin özel bir hüküm yoktur. Hasara kim katlanır?",
        {
            'A': 'Zilyetlik devredilmediğinden satıcı A katlanır',
            'B': 'Sözleşme kurulduğundan alıcı B katlanır',
            'C': 'Hasar taraflar arasında yarı yarıya paylaşılır',
            'D': 'Bedeli ödemişse B, ödememişse A katlanır',
            'E': 'Hasar otopark işletmecisine aittir',
        },
        'A',
        "TBK m. 208/1'e göre ayrık hâller dışında satılanın yarar ve hasarı **taşınır satışlarında zilyetliğin devrine**, taşınmaz satışlarında tescil anına kadar **satıcıya** aittir.",
        '6098 sayılı TBK m. 208',
    ),
    # düzey 3
    '0002': patch(
        "B'nin satın aldığı araç, sözleşme sırasında var olan bir hakka dayanılarak üçüncü kişi tarafından tamamen elinden alınmıştır; B bu riski bilmiyordu. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Satıcı kusursuzluğunu ispat ederse diğer zararlardan kurtulur',
            'B': "Sözleşmenin sona ermesi için B'nin dönme beyanı gerekir",
            'C': 'Satış sözleşmesi sona ermiş sayılır',
            'D': 'Elde edilen ürünlerin değeri iade edilecek bedelden indirilir',
            'E': 'B, ödediği bedeli faiziyle geri isteyebilir',
        },
        'B',
        "TBK m. 217'ye göre **satılanın tamamı alıcının elinden alınmışsa, satış sözleşmesi kendiliğinden sona ermiş sayılır**; alıcı ürün değerleri indirilerek bedelin faiziyle iadesini ve giderlerini isteyebilir; satıcı kusursuzluğunu ispat etmedikçe diğer zararları da giderir.",
        '6098 sayılı TBK m. 217',
    ),
    # düzey 3
    '0003': patch(
        'Alıcı B, satın aldığı ayıplı televizyon nedeniyle satıcıya başvurmuştur; satıcının ayıptan sorumluluğu vardır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'B, aşırı masraf gerektirmiyorsa ücretsiz onarım isteyebilir',
            'B': 'B, dönme ile bedel indirimini birlikte kullanabilir',
            'C': 'B, televizyonu alıkoyup bedelde indirim isteyebilir',
            'D': 'B, televizyonu geri vermeye hazır olduğunu bildirerek dönebilir',
            'E': "B'nin genel hükümlere göre tazminat hakkı saklıdır",
        },
        'B',
        "TBK m. 227'ye göre alıcı; dönme, bedelden indirim, ücretsiz onarım ve ayıpsız benzeriyle değiştirme haklarından **birini** kullanabilir; genel hükümlere göre tazminat hakkı saklıdır. Dönme ile indirim birbirini dışlayan seçimlik haklardır.",
        '6098 sayılı TBK m. 227',
    ),
    # düzey 2
    '0004': patch(
        'Satışa ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Satıcı, satılandaki ayıbı bilmese de ayıptan sorumludur\n\nII. Taşınmaz satış vaadi resmî şekilde yapılmadıkça geçerli olmaz\n\nIII. Önalım sözleşmesi resmî şekilde yapılmadıkça geçerli olmaz',
        {
            'A': 'I, II ve III',
            'B': 'II ve III',
            'C': 'Yalnız I',
            'D': 'Yalnız II',
            'E': 'I ve II',
        },
        'E',
        "TBK m. 219'a göre satıcı ayıbı bilmese de sorumludur (I); m. 237/2'ye göre taşınmaz satış vaadi resmî şekle tabidir (II). Önalım sözleşmesi ise **yazılı şekle** tabidir (III yanlış).",
        '6098 sayılı TBK m. 219, 237',
    ),
    # düzey 3
    '0005': patch(
        "A, yeğeni B'ye 100.000 ₺ bağışlamayı sözlü olarak vaat etmiş, daha sonra bu parayı B'ye ödemiştir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Ödeme, ödünç verme sayılır',
            'B': 'Söz yazılı olmadığından B parayı iade etmelidir',
            'C': 'Para bağışlaması resmî şekle tabi olduğundan işlem geçersizdir',
            'D': 'A, parayı sebepsiz zenginleşme hükümlerine göre geri isteyebilir',
            'E': 'Şekilsiz söz yerine getirildiğinden elden bağışlama hükmündedir',
        },
        'E',
        "TBK m. 288'e göre bağışlama sözü yazılı şekle tabidir; ancak **şekle uyulmaması sebebiyle geçersiz olan bağışlama sözü, bağışlayan tarafından yerine getirildiğinde elden bağışlama hükmündedir** (resmî şekle bağlı bağışlamalar hariç).",
        '6098 sayılı TBK m. 288',
    ),
    # düzey 2
    '0006': patch(
        "A, arkadaşı B'ye kullanılmış bir bisiklet bağışlamıştır. Bisikletin freninde A'nın hafif ihmaliyle fark edemediği bir arıza nedeniyle B kaza yapıp zarara uğramıştır. A, bisiklet hakkında garanti vermemiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "A, hafif ihmali nedeniyle B'nin zararını gidermelidir",
            'B': "A'nın ağır kusuru bulunsaydı B'ye karşı sorumluluğu doğabilirdi",
            'C': 'Bağışlayan ağır kusuru yoksa sorumlu değildir',
            'D': 'A, garanti vermiş olsaydı bununla sorumlu olurdu',
            'E': 'Bağışlama karşılıksız bir kazandırmadır',
        },
        'A',
        "TBK m. 294'e göre **bağışlayan, bağışlamadan doğan zarardan bu zarara ağır kusuruyla sebep olmadıkça bağışlanana karşı sorumlu değildir**; ayrıca garanti sözü vermişse bununla sorumlu olur.",
        '6098 sayılı TBK m. 294',
    ),
    # düzey 3
    '0007': patch(
        "A, yeğeni B'ye bir yıl sonra 500.000 ₺ bağışlamayı yazılı olarak vaat etmiştir. Aradan geçen sürede A'nın mali durumu, sözün yerine getirilmesini kendisi için olağanüstü ağır kılacak ölçüde bozulmuştur. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Bağışlama sözünün yazılı yapılması geçerlilik koşuludur',
            'B': "A'nın iflasına karar verilseydi ifa yükümlülüğü ortadan kalkardı",
            'C': 'A, sözünü geri alarak ifadan kaçınabilir',
            'D': 'Yeni aile yükümlülükleri doğsaydı da aynı hak doğardı',
            'E': 'Söz yazılı olduğundan A ifadan kaçınamaz',
        },
        'E',
        "TBK m. 296'ya göre bağışlama sözü veren, **mali durumu sözün yerine getirilmesini kendisi için olağanüstü ağır kılacak ölçüde değişmişse** veya yeni aile yükümlülükleri doğmuşsa sözünü geri alabilir ve ifadan kaçınabilir; ödeme güçsüzlüğü veya iflasta ifa yükümlülüğü ortadan kalkar.",
        '6098 sayılı TBK m. 288, 296',
    ),
    # düzey 3
    '0008': patch(
        "Aylık kirası 15.000 ₺ olan bir konut kira sözleşmesinde kiracıdan güvence verilmesi kararlaştırılmıştır. Güvencenin üst sınırı kaç ₺'dir?",
        {
            'A': '60.000',
            'B': '45.000',
            'C': '90.000',
            'D': '15.000',
            'E': '30.000',
        },
        'B',
        "TBK m. 342'ye göre konut ve çatılı işyeri kiralarında kiracıya güvence verme borcu getirilmişse **bu güvence üç aylık kira bedelini aşamaz**: 3 × 15.000 = **45.000 ₺**.",
        '6098 sayılı TBK m. 342',
    ),
    # düzey 2
    '0009': patch(
        "Konut kiracısı B, kiraya verenin yazılı rızası olmadan evin bir odasını C'ye kiraya vermiştir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Konut kirasında alt kira için kiraya verenin yazılı rızası gerekir',
            'B': 'Alt kira için sözlü onay yeterlidir',
            'C': 'C, doğrudan kiraya verenin kiracısı olur',
            'D': 'Kısmi alt kira izne bağlı değildir',
            'E': 'Kiraya verene zarar vermedikçe B alt kiraya verebilir',
        },
        'A',
        "TBK m. 322/2'ye göre **kiracı, konut ve çatılı işyeri kiralarında, kiraya verenin yazılı rızası olmadıkça kiralananı başkasına kiralayamaz** ve kullanım hakkını devredemez.",
        '6098 sayılı TBK m. 322',
    ),
    # düzey 3
    '0010': patch(
        'Bir yıl süreli konut kirasında kiracı, aynı kira yılı içinde kira bedelini ödemediği için kendisine yazılı olarak iki haklı ihtarda bulunulmasına sebep olmuştur. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İki ihtar tahliye sebebi oluşturmaz',
            'B': 'Kiraya veren sözleşmeyi ihtarsız hemen feshedebilir',
            'C': 'Kiracı üçüncü ihtara kadar tahliye edilemez',
            'D': 'Kiraya veren, süre bitiminden itibaren bir ay içinde sona erdirebilir',
            'E': 'Kiraya veren on yıllık süre dolmadan başvuramaz',
        },
        'D',
        "TBK m. 352/2'ye göre kiracı bir kira yılı içinde kira bedelini ödemediği için **iki haklı ihtara sebep olmuşsa**, kiraya veren **kira süresinin veya kira yılının bitiminden başlayarak bir ay içinde** icraya başvurarak veya dava açarak sözleşmeyi sona erdirebilir.",
        '6098 sayılı TBK m. 352/2',
    ),
    # düzey 2
    '0011': patch(
        "B, arkadaşı A'dan karşılıksız ödünç aldığı kamerayı A'nın izni olmadan C'ye kullandırmış; kamera C'nin elindeyken yıldırım düşmesiyle zarar görmüştür. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Zarar beklenmedik hâlden doğduğundan B sorumlu değildir',
            'B': 'B, ödünç konusunu başkasına kullandıramaz',
            'C': 'Zararın yine doğacağını ispat ederse B kurtulur',
            'D': 'Bu bir kullanım ödüncü sözleşmesidir',
            'E': 'B, aykırılık nedeniyle beklenmedik hâlden de sorumludur',
        },
        'A',
        "TBK m. 380'e göre ödünç alan ödünç konusunu başkasına kullandıramaz; **bu hükme aykırı davranırsa beklenmedik hâllerden doğan zararlardan da sorumludur**, ancak uyulmuş olsaydı da zararın doğacağını ispat ederse kurtulur.",
        '6098 sayılı TBK m. 379, 380',
    ),
    # düzey 2
    '0012': patch(
        "Ticari olmayan bir tüketim ödüncünde A, arkadaşı B'ye 50.000 ₺ ödünç vermiş; faiz kararlaştırılmamıştır. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'A, ödünç zamanındaki piyasa faizini isteyebilir',
            'B': 'A, yasal faiz isteyebilir',
            'C': 'A, faizi anaparaya ekleyerek isteyebilir',
            'D': 'Faiz oranını hâkim belirler',
            'E': 'Faiz kararlaştırılmadığından A faiz isteyemez',
        },
        'E',
        "TBK m. 387'ye göre **ticari olmayan tüketim ödüncü sözleşmesinde, taraflarca kararlaştırılmış olmadıkça faiz istenemez**; ticari tüketim ödüncünde kararlaştırılmasa da istenebilir.",
        '6098 sayılı TBK m. 387',
    ),
    # düzey 3
    '0013': patch(
        "A, ancak ücret karşılığında yapılabilecek bir işi B'nin işletmesinde belli bir süre görmüş, B de bunu kabul etmiştir; aralarında yazılı sözleşme yoktur. Sonradan sözleşmenin geçersiz olduğu anlaşılmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Sözleşme, ilişki ortadan kaldırılıncaya kadar geçerli gibi hüküm doğurur',
            'B': 'Yazılı sözleşme bulunmaması kurulmayı engellemez',
            'C': 'Geçersizlik nedeniyle A, çalıştığı dönem için ücret isteyemez',
            'D': 'Taraflar arasında hizmet sözleşmesi kurulmuş sayılır',
            'E': 'Hizmet sözleşmesi kural olarak özel bir şekle bağlı değildir',
        },
        'C',
        "TBK m. 394'e göre hizmet sözleşmesi kural olarak şekle bağlı değildir; durumun gereğine göre ancak ücret karşılığında yapılabilecek iş kabul edilirse sözleşme kurulmuş sayılır. **Geçersizliği sonradan anlaşılan hizmet sözleşmesi, hizmet ilişkisi ortadan kaldırılıncaya kadar geçerli bir sözleşmenin bütün hüküm ve sonuçlarını doğurur**.",
        '6098 sayılı TBK m. 394',
    ),
    # düzey 2
    '0014': patch(
        'Bir heykeltıraşa, kendi üslubuyla bir büst yapması için sipariş verilmiştir. Heykeltıraş işi, kendi yönetimi dışında bağımsız çalışan bir sanatçıya yaptırmak istemektedir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Eser sözleşmesinde bizzat ifa borcu bulunmaz',
            'B': 'İş sahibinin onayı olmadan yardımcı çalıştıramaz',
            'C': 'Eseri dilediği kişiye bağımsız olarak yaptırabilir',
            'D': 'Eseri kendisi yapmalı veya kendi yönetiminde yaptırmalıdır',
            'E': 'İşi başkasına vermesi sözleşmenin devri sayılır',
        },
        'D',
        "TBK m. 471'e göre yüklenici eseri **doğrudan kendisi yapmak veya kendi yönetimi altında yaptırmakla** yükümlüdür; ancak yüklenicinin kişisel özellikleri önem taşımıyorsa işi başkasına da yaptırabilir. Burada kişisel üslup önemlidir.",
        '6098 sayılı TBK m. 471',
    ),
    # düzey 3
    '0015': patch(
        'Yüklenici, götürü bedelle üstlendiği binayı yaparken, malzeme fiyatlarındaki öngörülebilir olağan artışlar nedeniyle beklediğinden fazla masraf yapmıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Yüklenici eseri belirlenen bedelle meydana getirmelidir',
            'B': 'Olağanüstü ve öngörülemeyen durumlarda uyarlama istenebilirdi',
            'C': 'Yüklenici, masraf artışı nedeniyle bedelin artırılmasını isteyebilir',
            'D': 'Uyarlama mümkün olmasaydı dönme hakkı doğabilirdi',
            'E': 'Eser öngörülenden az masraf gerektirseydi iş sahibi bedelin tamamını öderdi',
        },
        'C',
        "TBK m. 480'e göre **bedel götürü olarak belirlenmişse yüklenici, eser öngörülenden fazla emek ve masrafı gerektirmiş olsa bile bedelin artırılmasını isteyemez**; öngörülemeyen durumlar ifayı son derece güçleştirirse uyarlama veya dönme istenebilir. Eser daha az masrafla yapılsa da iş sahibi bedelin tamamını öder.",
        '6098 sayılı TBK m. 480',
    ),
    # düzey 3
    '0016': patch(
        "A, avukat olmayan arkadaşı B'ye alacaklarının tahsili için genel bir vekâlet vermiştir; B'ye ayrıca özel yetki verilmemiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'B, A adına üçüncü kişilere bağışlama yapamaz',
            'B': 'B, A adına bir başkasının borcuna kefil olamaz',
            'C': "B, A'nın taşınmazını devredemez veya sınırlandıramaz",
            'D': 'B, borçlulardan biriyle sulh olabilir',
            'E': 'B, tahsil için gerekli hukuki işlemleri yapabilir',
        },
        'D',
        "TBK m. 504'e göre vekâlet, işin görülmesi için gerekli hukuki işlemleri yapma yetkisini kapsar; ancak vekil **özel olarak yetkili kılınmadıkça dava açamaz, sulh olamaz**, hakeme başvuramaz, bağışlama yapamaz, kefil olamaz, taşınmazı devredemez ve bir hak ile sınırlandıramaz.",
        '6098 sayılı TBK m. 504',
    ),
    # düzey 3
    '0017': patch(
        "Vekil B, davanın duruşmasına bir gün kala, haklı bir sebep olmaksızın ve A'nın başka bir avukat bulmasına imkân bırakmayacak biçimde istifa etmiş; A bu yüzden zarara uğramıştır. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'B, duruşma bitmeden istifa edemez',
            'B': 'B, aldığı ücretin iki katını iade eder',
            'C': 'İstifa geçersizdir, vekâlet devam eder',
            'D': "B'nin istifası için A'nın rızası gerekir",
            'E': "B istifa edebilir, ancak A'nın zararını gidermelidir",
        },
        'E',
        "TBK m. 512'ye göre vekâlet veren ve vekil sözleşmeyi **her zaman tek taraflı olarak sona erdirebilir**; ancak **uygun olmayan zamanda sona erdiren taraf, diğerinin bundan doğan zararını gidermekle yükümlüdür**.",
        '6098 sayılı TBK m. 512',
    ),
    # düzey 3
    '0018': patch(
        'Aşağıdakilerden hangileri doğrudur?\n\nI. Vekil, özel olarak yetkili kılınmadıkça vekâlet veren adına dava açamaz\n\nII. Götürü bedelde yüklenici, masrafları arttığı için bedelin artırılmasını isteyebilir\n\nIII. Eser tamamlanmadan sözleşmeyi fesheden iş sahibi yükleniciye bir ödeme yapmaz',
        {
            'A': 'I ve III',
            'B': 'Yalnız II',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'C',
        "TBK m. 504/3'e göre vekil özel yetki olmadıkça dava açamaz (I). m. 480'e göre götürü bedelde masraf artışı bedelin artırılmasını gerektirmez (II yanlış); m. 484'e göre fesheden iş sahibi yapılan kısmın karşılığını öder ve zararları giderir (III yanlış).",
        '6098 sayılı TBK m. 480, 484, 504',
    ),
    # düzey 3
    '0019': patch(
        "C, B'nin A'ya olan borcuna müteselsil kefil olmuştur. Borç muaccel olmuş, B ödemede gecikmiş ve A'nın ihtarı sonuçsuz kalmıştır; alacak teslime bağlı taşınır rehniyle güvence altına alınmamıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "A, C'ye başvurmadan önce B'yi takip etmelidir",
            'B': "A, B'yi takip etmeden C'yi takip edebilir",
            'C': 'Teslime bağlı taşınır rehni olsaydı önce rehin paraya çevrilirdi',
            'D': "C'nin sorumluluğu müteselsil kefil sıfatına dayanır",
            'E': "B'nin açık ödeme güçsüzlüğü de başvuru için yeterli olurdu",
        },
        'A',
        "TBK m. 586'ya göre müteselsil kefalette alacaklı, **borçlunun ifada gecikmesi ve ihtarın sonuçsuz kalması veya açıkça ödeme güçsüzlüğü** hâlinde borçluyu takip etmeden kefili takip edebilir; teslime bağlı taşınır rehninde önce rehin paraya çevrilir.",
        '6098 sayılı TBK m. 586',
    ),
    # düzey 2
    '0020': patch(
        "Asıl borçlu B, alacaklının kendi edimini ifa etmediğine dayanan ödemezlik def'inden vazgeçmiştir. Alacaklı, kefil C'ye başvurmuştur. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "Ödeme güçsüzlüğünden doğan def'iler bu kapsamda değildir",
            'B': "C, B'nin vazgeçtiği def'iyi ileri sürebilir",
            'C': "B vazgeçtiği için C bu def'iyi ileri süremez",
            'D': "Kefil, asıl borçluya ait def'ileri ileri sürmelidir",
            'E': "C, def'iyi bilmeden öderse rücu hakkına sahip olur",
        },
        'C',
        "TBK m. 591'e göre kefil, asıl borçluya ait ve ödeme güçsüzlüğünden doğmayan bütün def'ileri ileri sürme hakkına sahiptir ve bunları ileri sürmelidir; **asıl borçlu kendisine ait bir def'iden vazgeçmiş olsa bile kefil, bu def'iyi alacaklıya karşı ileri sürebilir**.",
        '6098 sayılı TBK m. 591',
    ),
    # düzey 3
    '0021': patch(
        'Alıcı B, satın aldığı mobilyanın kendi isteğiyle başka bir şehre gönderilmesini istemiş; satıcı mobilyayı taşıyıcıya teslim etmiştir. Mobilya yolda tarafların kusuru olmadan hasar görmüştür. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': "Yarar ve hasar taşıyıcıya teslim anında B'ye geçmiştir",
            'B': 'Taşınırda kural, zilyetliğin devrine kadar hasarın satıcıda olmasıdır',
            'C': "Gönderme B'nin isteğiyle yapılmıştır",
            'D': "Hasar, mobilya B'ye ulaşıncaya kadar satıcıya aittir",
            'E': 'B, bedeli ödemekle yükümlü kalır',
        },
        'D',
        "TBK m. 208/3'e göre **satıcı alıcının isteği üzerine satılanı ifa yerinden başka bir yere gönderirse, yarar ve hasar satılanın taşıyıcıya teslim edildiği anda alıcıya geçer**.",
        '6098 sayılı TBK m. 208',
    ),
    # düzey 2
    '0022': patch(
        'Satıcı A, sattığı buzdolabının kompresöründeki üretim hatasını bilmiyordu. Hata, buzdolabının kullanım amacı bakımından değerini önemli ölçüde azaltmaktadır. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Alıcı, ancak bedelin yarısını geri isteyebilir',
            'B': 'A, ayıbı bilmediği için sorumlu değildir',
            'C': 'A, ayıbı bilmese de sorumludur',
            'D': 'A, ancak kusurluysa tazminat öder',
            'E': "Sorumluluk üreticiye aittir, A'ya başvurulamaz",
        },
        'C',
        "TBK m. 219'a göre satıcı, satılandaki maddi, hukuki veya ekonomik ayıplardan sorumludur ve **bu ayıpların varlığını bilmese bile onlardan sorumludur**.",
        '6098 sayılı TBK m. 219',
    ),
    # düzey 3
    '0023': patch(
        "Alıcı B, satın aldığı makineyi 1 Mart 2024'te teslim almıştır. Satıcı daha uzun bir süre üstlenmemiştir ve ağır kusurlu değildir. Gizli ayıp 1 Şubat 2026'da ortaya çıkmıştır. Ayıptan doğan davalar hangi tarihte zamanaşımına uğrar?",
        {
            'A': '1 Mart 2034',
            'B': '1 Mart 2026',
            'C': '1 Mart 2029',
            'D': '1 Şubat 2026',
            'E': '1 Şubat 2028',
        },
        'B',
        "TBK m. 231'e göre ayıptan doğan her türlü dava, **ayıp daha sonra ortaya çıksa bile, satılanın alıcıya devrinden başlayarak iki yıl** geçmekle zamanaşımına uğrar: 1 Mart 2024 + 2 yıl = **1 Mart 2026**.",
        '6098 sayılı TBK m. 231',
    ),
    # düzey 2
    '0024': patch(
        'Aşağıdaki sözleşmelerden hangisinin geçerliliği resmî şekle bağlı değildir?',
        {
            'A': 'Alım sözleşmesi',
            'B': 'Taşınmaz satış vaadi',
            'C': 'Taşınmaz satış sözleşmesi',
            'D': 'Önalım sözleşmesi',
            'E': 'Geri alım sözleşmesi',
        },
        'D',
        "TBK m. 237'ye göre taşınmaz satışı, taşınmaz satış vaadi, geri alım ve alım sözleşmeleri **resmî şekilde** düzenlenmedikçe geçerli olmaz; **önalım sözleşmesinin geçerliliği ise yazılı şekle** bağlıdır.",
        '6098 sayılı TBK m. 237',
    ),
    # düzey 3
    '0025': patch(
        "A, yeğeni B'ye evini bağışlamayı adi yazılı bir belgeyle vaat etmiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Bu söz şekil eksikliği nedeniyle geçersizdir',
            'B': 'Söz yerine getirilse de elden bağışlama hükmü uygulanmaz',
            'C': 'Söz yazılı yapıldığından geçerlidir',
            'D': 'Taşınır bağışlama sözü için yazılı şekil yeterli olurdu',
            'E': 'Taşınmaz bağışlama sözü resmî şekle tabidir',
        },
        'C',
        "TBK m. 288/2'ye göre **bir taşınmazın bağışlanması sözü vermenin geçerliliği resmî şekilde yapılmasına bağlıdır**; geçerliliği resmî şekle bağlanmış bağışlamalarda şekilsiz sözün yerine getirilmesi elden bağışlama sayılmaz.",
        '6098 sayılı TBK m. 288',
    ),
    # düzey 2
    '0026': patch(
        "A, kızı B'ye bağışlamayı önerdiği tabloyu diğer eşyalarından ayırıp paketlemiştir. B henüz öneriyi kabul etmemişken A vazgeçmiştir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': "A, tablonun değerini B'ye ödemelidir",
            'B': 'Tablo ayrıldığından öneri geri alınamaz',
            'C': "Öneri ancak B'nin onayıyla geri alınabilir",
            'D': 'Öneri, ayırmayla elden bağışlamaya dönüşmüştür',
            'E': 'A, B kabul edinceye kadar öneriyi geri alabilir',
        },
        'E',
        "TBK m. 293'e göre bir kimse başkasına bağışlamayı önerdiği bir malı **başka mallarından fiilen ayırmış olsa bile, bağışlananın kabulüne kadar bağışlama önerisini geri alabilir**.",
        '6098 sayılı TBK m. 293',
    ),
    # düzey 3
    '0027': patch(
        "Bir konut kira sözleşmesinde aylık kira 20.000 ₺'dir. Bir önceki kira yılında tüketici fiyat endeksindeki on iki aylık ortalamalara göre değişim oranı %40'tır; taraflar yeni dönem için %50 artış kararlaştırmıştır. Yeni dönemde geçerli olabilecek en yüksek aylık kira kaç ₺'dir?",
        {
            'A': '28.000',
            'B': '24.000',
            'C': '30.000',
            'D': '20.000',
            'E': '25.000',
        },
        'A',
        "TBK m. 344'e göre yenilenen kira dönemlerinde kira bedeline ilişkin anlaşmalar, **bir önceki kira yılında TÜFE'deki on iki aylık ortalamalara göre değişim oranını geçmemek koşuluyla** geçerlidir: 20.000 × 1,40 = **28.000 ₺**.",
        '6098 sayılı TBK m. 344',
    ),
    # düzey 2
    '0028': patch(
        'Konut kiracısı B, kiralananın tesliminden sonra muaccel olan kira bedelini ödememiştir. Kiraya veren A, sözleşmeyi feshetmek istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'A, on günlük süre vererek fesih ihtarında bulunabilir',
            'B': 'A, kiracıya yazılı olarak süre vermelidir',
            'C': 'Süre içinde ödeme yapılmazsa A sözleşmeyi feshedebilir',
            'D': 'Süre, bildirimi izleyen günden işlemeye başlar',
            'E': 'Konut kirasında verilecek süre en az otuz gündür',
        },
        'A',
        "TBK m. 315'e göre kiraya veren kiracıya **yazılı olarak** süre verip ödenmemesi hâlinde feshedeceğini bildirebilir; verilecek süre en az on gün, **konut ve çatılı işyeri kiralarında en az otuz gündür** ve bildirimi izleyen günden işler.",
        '6098 sayılı TBK m. 315',
    ),
    # düzey 2
    '0029': patch(
        "A'ya ait kiralık daire, kira süresi devam ederken C'ye satılmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'C, kira sözleşmesinin tarafı olur',
            'B': "Kiracı kira bedelini artık yeni malik C'ye öder",
            'C': 'Kamulaştırmaya ilişkin hükümler saklıdır',
            'D': 'Satışla birlikte kira sözleşmesi sona erer',
            'E': 'Kiracının kullanım hakkı devam eder',
        },
        'D',
        "TBK m. 310'a göre **sözleşmenin kurulmasından sonra kiralanan herhangi bir sebeple el değiştirirse, yeni malik kira sözleşmesinin tarafı olur**; kamulaştırmaya ilişkin hükümler saklıdır.",
        '6098 sayılı TBK m. 310',
    ),
    # düzey 3
    '0030': patch(
        'Üç yıl süreli konut kira sözleşmesinin kiracısı B, birinci yılın sonunda evi boşaltmış; kiraya verenden kabul etmesi beklenebilecek, ödeme gücü olan ve sözleşmeyi devralmaya hazır bir kiracı bulmuştur. Kiraya veren bu kişiyi reddetmiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': "B'nin borcu kiraya verenin onayına kadar sürer",
            'B': "B'nin kira sözleşmesinden doğan borçları sona erer",
            'C': 'B, makul süreye bakılmaksızın bir yıllık kira öder',
            'D': 'B, kalan iki yılın kirasını ödemekle yükümlüdür',
            'E': 'Kiraya veren yeni kiracıyı kabule zorlanır',
        },
        'B',
        "TBK m. 325'e göre sözleşmeye uymadan kiralananı geri veren kiracının borçları makul bir süre devam eder; ancak **kiraya verenden kabul etmesi beklenebilecek, ödeme gücüne sahip ve kira ilişkisini devralmaya hazır yeni bir kiracı bulması hâlinde kiracının borçları sona erer**.",
        '6098 sayılı TBK m. 325',
    ),
    # düzey 3
    '0031': patch(
        'Konut kiracısı B, zaman zaman yüksek sesle müzik dinleyerek komşuları rahatsız etmektedir. Davranış komşular için çekilmez boyutta değildir ve kiralanana zarar verilmemiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Aykırılık sürerse kiraya veren sözleşmeyi feshedebilir',
            'B': 'Konut dışındaki kiralarda ihtarsız fesih mümkündür',
            'C': 'Kiraya veren ihtarsız olarak hemen feshedebilir',
            'D': 'Kiraya veren en az otuz gün süre vererek yazılı ihtarda bulunur',
            'E': 'Kiracı komşulara gerekli saygıyı göstermekle yükümlüdür',
        },
        'C',
        "TBK m. 316'ya göre konut ve çatılı işyeri kirasında kiraya veren, **en az otuz gün süre vererek aykırılığın giderilmesi, aksi hâlde feshedeceği konusunda yazılı ihtarda** bulunur. Hemen fesih, kasten ağır zarar veya çekilmezlik gibi hâllere özgüdür; diğer kiralarda ihtarsız fesih mümkündür.",
        '6098 sayılı TBK m. 316',
    ),
    # düzey 3
    '0032': patch(
        "A, arkadaşı B'ye düğününde giymesi için takım elbisesini ödünç vermiştir. Düğünden önce A'nın, önceden bilinmeyen bir cenaze nedeniyle elbiseye ivedi gereksinimi doğmuştur. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'A, düğün bitmeden elbiseyi geri isteyemez',
            'B': "A, ancak B'nin rızasıyla geri alabilir",
            'C': 'A, elbiseyi kullanım bitmeden önce geri isteyebilir',
            'D': "A, geri almak için B'ye tazminat ödemelidir",
            'E': 'A, elbiseyi geri istemeden önce altı hafta beklemelidir',
        },
        'C',
        "TBK m. 383'e göre **önceden bilinmeyen bir durum yüzünden ödünç verenin ivedi gereksinimi ortaya çıkarsa, ödünç veren o şeyi daha önce geri isteyebilir**.",
        '6098 sayılı TBK m. 383',
    ),
    # düzey 2
    '0033': patch(
        'Ödünç sözleşmelerine ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Kullanım ödüncünde ödünç alan, şeyi başkasına kullandırabilir\n\nII. Ticari olmayan tüketim ödüncünde faiz kararlaştırılmadıkça istenemez\n\nIII. Ticari tüketim ödüncünde faiz kararlaştırılmasa da istenebilir',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'Yalnız III',
            'D': 'II ve III',
            'E': 'Yalnız II',
        },
        'D',
        "TBK m. 387'ye göre ticari olmayan tüketim ödüncünde faiz kararlaştırılmadıkça istenemez (II), ticari olanda istenebilir (III). m. 380'e göre ödünç alan ödünç konusunu **başkasına kullandıramaz** (I yanlış).",
        '6098 sayılı TBK m. 380, 387',
    ),
    # düzey 3
    '0034': patch(
        "Yüklenici, iş sahibine 1 Ekim 2022'de bir bina teslim etmiştir; yüklenicinin ağır kusuru yoktur. Binadaki ayıp nedeniyle açılacak davalar hangi tarihte zamanaşımına uğrar?",
        {
            'A': '1 Ekim 2042',
            'B': '1 Ekim 2023',
            'C': '1 Ekim 2032',
            'D': '1 Ekim 2024',
            'E': '1 Ekim 2027',
        },
        'E',
        "TBK m. 478'e göre ayıplı eser nedeniyle açılacak davalar teslim tarihinden başlayarak taşınmaz yapılar dışındaki eserlerde iki yıl, **taşınmaz yapılarda beş yıl**, yüklenicinin ağır kusurunda yirmi yıl geçmekle zamanaşımına uğrar: 1 Ekim 2022 + 5 yıl = **1 Ekim 2027**.",
        '6098 sayılı TBK m. 478',
    ),
    # düzey 2
    '0035': patch(
        'İş sahibi, teslim aldığı mobilyaları gözden geçirmiş ve açıkça kabul etmiştir. Daha sonra yüklenicinin kasten gizlediği ve usulüne uygun gözden geçirmede fark edilemeyecek bir ayıp ortaya çıkmıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Kasten gizlenmeyen açık ayıplar için kabul sorumluluğu kaldırır',
            'B': 'Kabulden sonra yüklenici bu ayıptan da sorumlu olmaz',
            'C': 'İş sahibi ayıbı gecikmeksizin bildirmelidir',
            'D': 'Yüklenicinin bu ayıptan sorumluluğu devam eder',
            'E': 'Kabul açık veya örtülü olabilir',
        },
        'B',
        "TBK m. 477'ye göre eserin açıkça veya örtülü kabulünden sonra yüklenici sorumluluktan kurtulur; **ancak onun tarafından kasten gizlenen ve usulüne göre gözden geçirme sırasında fark edilemeyecek ayıplar için sorumluluğu devam eder**. Sonradan ortaya çıkan ayıp gecikmeksizin bildirilmelidir.",
        '6098 sayılı TBK m. 477',
    ),
    # düzey 3
    '0036': patch(
        "Vekil B'ye, A'nın hisse senetlerini 100 ₺'nin altında satmaması talimatı verilmiştir. Borsa kapanmak üzereyken fiyat hızla düşmüş, A'ya ulaşılamamış; A durumu bilseydi izin vereceği açık olduğundan B senetleri 95 ₺'den satmıştır. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': "B, satışı ancak A'nın sonradan onayıyla geçerli kılabilir",
            'B': "B'nin talimattan ayrılması haklıdır",
            'C': 'B vekâlet borcunu ifa etmemiş sayılır, ücret isteyemez',
            'D': 'B, talimata aykırılık nedeniyle satışın tüm zararını öder',
            'E': 'Satış, talimata aykırı olduğundan kesin hükümsüzdür',
        },
        'B',
        "TBK m. 505'e göre vekil açık talimata uymakla yükümlüdür; ancak **vekâlet verenden izin alma imkânı bulunmadığında, durumu bilseydi onun da izin vereceği açık olan hâllerde vekil talimattan ayrılabilir**.",
        '6098 sayılı TBK m. 505',
    ),
    # düzey 3
    '0037': patch(
        "Vekâlet veren A ölmüştür; sözleşmeden veya işin niteliğinden aksi anlaşılmamaktadır. Vekâletin hemen sona ermesi A'nın mirasçılarının menfaatlerini tehlikeye düşürmektedir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Aksi kararlaştırılsaydı vekâlet devam edebilirdi',
            'B': "Vekâlet kural olarak A'nın ölümüyle sona erer",
            'C': 'B, mirasçılar işi üstlenebilene kadar ifaya devam eder',
            'D': "Vekil B, A'nın ölümüyle işi derhâl bırakmalıdır",
            'E': 'Vekilin ölümü de vekâleti sona erdirirdi',
        },
        'D',
        "TBK m. 513'e göre aksi anlaşılmadıkça vekâlet, taraflardan birinin ölümüyle sona erer; ancak **sona erme vekâlet verenin menfaatlerini tehlikeye düşürüyorsa, mirasçılar işleri kendi başına görebilecek duruma gelinceye kadar vekil vekâleti ifaya devam etmekle** yükümlüdür.",
        '6098 sayılı TBK m. 513',
    ),
    # düzey 3
    '0038': patch(
        "Evli olan ve hakkında ayrılık kararı ya da ayrı yaşama hakkı bulunmayan B, arkadaşının tüketici kredisine kefil olmak istemektedir; kefalet, B'nin ticari veya mesleki faaliyetiyle ilgili değildir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Sorumlu olunacak miktarı artıran değişiklikte de rıza aranır',
            'B': 'Kefalet için eşin yazılı rızası gerekir',
            'C': 'Eşin rızası kefaletten sonra da verilebilir',
            'D': 'Rıza en geç sözleşme anında verilmelidir',
            'E': 'Ayrılık kararı olsaydı eşin rızası aranmazdı',
        },
        'C',
        "TBK m. 584'e göre eşlerden biri, ayrılık kararı veya yasal ayrı yaşama hakkı yoksa **ancak diğerinin yazılı rızasıyla** kefil olabilir; **rızanın sözleşmenin kurulmasından önce veya en geç kurulması anında verilmesi şarttır**. Miktarı artıran değişiklikler de rızaya tabidir.",
        '6098 sayılı TBK m. 584',
    ),
    # düzey 3
    '0039': patch(
        "C, azami 100.000 ₺ ile sınırlı olarak müteselsil kefil olmuştur. Asıl borçta anapara 90.000 ₺, işlemiş bir yıllık akdi faiz 15.000 ₺'dir. C'nin sorumlu olduğu en yüksek tutar kaç ₺'dir?",
        {
            'A': '100.000',
            'B': '90.000',
            'C': '105.000',
            'D': '95.000',
            'E': '115.000',
        },
        'A',
        "TBK m. 589'a göre **kefil her durumda kefalet sözleşmesinde belirtilen azami miktara kadar sorumludur**; anapara ve bir yıllık akdi faiz toplamı 105.000 ₺ olsa da C en fazla **100.000 ₺** öder.",
        '6098 sayılı TBK m. 589',
    ),
    # düzey 2
    '0040': patch(
        'Kefalete ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Adi kefalette alacaklı kural olarak önce borçluya başvurmalıdır\n\nII. Kefalet sözleşmesi sözlü olarak da geçerli biçimde yapılabilir\n\nIII. Kefil, sözleşmedeki azami miktarı aşan tutardan sorumlu olmaz',
        {
            'A': 'I ve III',
            'B': 'I, II ve III',
            'C': 'Yalnız III',
            'D': 'Yalnız I',
            'E': 'I ve II',
        },
        'A',
        "TBK m. 585'e göre adi kefalette önce borçluya başvurulur (I); m. 589'a göre kefil azami miktara kadar sorumludur (III). m. 583'e göre kefalet **yazılı şekle** ve el yazısı koşullarına tabidir (II yanlış).",
        '6098 sayılı TBK m. 583, 585, 589',
    ),
    # düzey 3
    '0041': patch(
        "A, B'ye sattığı tablonun C'ye ait olduğu yönündeki iddiayı sözleşme sırasında B'ye anlatmış; B yine de tabloyu satın almıştır. Tablo, C tarafından mahkeme kararıyla B'nin elinden alınmıştır. A, bu riske karşı ayrıca sorumluluk üstlenmemiştir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'A, bedelin yarısını iade eder',
            'B': 'Sözleşme kesin hükümsüz olur',
            'C': 'A, C ile birlikte müteselsilen sorumludur',
            'D': 'A, bedeli faiziyle iade etmekle yükümlüdür',
            'E': 'A, zapttan sorumlu olmaz',
        },
        'E',
        "TBK m. 214/2'ye göre **alıcı, elinden alınma tehlikesini sözleşmenin kurulduğu sırada biliyor idiyse satıcı, ayrıca üstlenmiş olmadıkça bundan dolayı sorumlu olmaz**.",
        '6098 sayılı TBK m. 214',
    ),
    # düzey 3
    '0042': patch(
        "Satıcı A, sattığı ikinci el aracın motorundaki ciddi arızayı bildiği hâlde gizlemiş; sözleşmeye 'araç olduğu gibi satılmıştır, satıcı ayıptan sorumlu değildir' kaydı konmuştur. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Sorumsuzluk kaydı kesin hükümsüzdür',
            'B': 'A, ayıbı gizlemekle ağır kusurludur',
            'C': 'Sorumsuzluk kaydı nedeniyle A ayıptan sorumlu tutulamaz',
            'D': 'A, iki yıllık zamanaşımı süresinden yararlanamaz',
            'E': 'Alıcı, ayıptan doğan seçimlik haklarından birini kullanabilir',
        },
        'C',
        "TBK m. 221'e göre **satıcı satılanı ayıplı olarak devretmekte ağır kusurlu ise, ayıptan sorumluluğunu kaldıran veya sınırlayan her anlaşma kesin olarak hükümsüzdür**; m. 231/3'e göre ağır kusurlu satıcı iki yıllık zamanaşımından yararlanamaz.",
        '6098 sayılı TBK m. 221, 231',
    ),
    # düzey 2
    '0043': patch(
        'Alıcı B, teslim aldığı çamaşır makinesini gözden geçirmiş ve bir sorun görmemiştir. Üç ay sonra, olağan bir gözden geçirmeyle anlaşılamayacak bir ayıp ortaya çıkmıştır. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'B, ayıbı hemen bildirmezse malı ayıbıyla kabul etmiş sayılır',
            'B': 'Gizli ayıplardan satıcı sorumlu değildir',
            'C': "Gözden geçirme yapıldığından B'nin hakları düşmüştür",
            'D': 'B, ayıbı ancak bilirkişi raporuyla bildirebilir',
            'E': 'B, ayıbı iki yıl içinde dilediği zaman bildirebilir',
        },
        'A',
        "TBK m. 223'e göre olağan gözden geçirmeyle ortaya çıkarılamayacak bir ayıp sonradan anlaşılırsa **hemen satıcıya bildirilmelidir; bildirilmezse satılan bu ayıpla birlikte kabul edilmiş sayılır**.",
        '6098 sayılı TBK m. 223',
    ),
    # düzey 3
    '0044': patch(
        "Tüketici B, bir mağazadan taksitle satış sözleşmesiyle buzdolabı almıştır; taraflarca imzalanmış sözleşmenin bir nüshası 1 Haziran'da B'nin eline geçmiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Taksitle satış sözleşmesi yazılı şekilde yapılmalıdır',
            'B': "Sözleşme B bakımından 8 Haziran'da hüküm doğurur",
            'C': 'B, geri alma hakkından önceden feragat edebilir',
            'D': 'B, yedi gün içinde yazılı bildirimle irade açıklamasını geri alabilir',
            'E': 'Geri alma bildirimi son gün postaya verilirse sonuç doğurur',
        },
        'C',
        "TBK m. 253'e göre taksitle satış yazılı yapılmalıdır. m. 255'e göre sözleşme alıcı bakımından nüshanın eline geçmesinden **yedi gün sonra** hüküm doğurur; alıcı bu süre içinde yazılı bildirimle irade açıklamasını geri alabilir ve **bu haktan önceden feragat edilemez**.",
        '6098 sayılı TBK m. 253, 255',
    ),
    # düzey 2
    '0045': patch(
        'Aşağıdakilerden hangisi bağışlama sayılmaz?',
        {
            'A': 'Bir işverenin emekli işçisine karşılıksız bir tablo vermesi',
            'B': 'Mirasçının kendisine kalan mirası reddetmesi',
            'C': 'Bir kişinin arkadaşına saatini karşılıksız olarak teslim etmesi',
            'D': 'Teyzenin yeğenine karşılıksız para göndermesi',
            'E': 'Babanın oğluna karşılıksız otomobil vermesi',
        },
        'B',
        "TBK m. 285'e göre bağışlama, bağışlayanın malvarlığından karşılıksız kazandırma yapmayı üstlendiği sözleşmedir. **Henüz edinilmemiş bir haktan feragat etmek veya bir mirası reddetmek bağışlama değildir**; ahlaki bir ödevin yerine getirilmesi de bağışlama sayılmaz.",
        '6098 sayılı TBK m. 285',
    ),
    # düzey 3
    '0046': patch(
        "A, yeğeni B'ye 200.000 ₺ değerinde bir otomobili elden bağışlamıştır. B, daha sonra A'ya karşı ağır bir suç işlemiştir. A'nın bağışlamayı geri aldığı ve iade istediği tarihte otomobilin B'deki değeri 150.000 ₺'dir. A, B'den en fazla kaç ₺ değerinde iade isteyebilir?",
        {
            'A': '200.000',
            'B': '100.000',
            'C': '50.000',
            'D': '0',
            'E': '150.000',
        },
        'E',
        "TBK m. 295'e göre bağışlanan, bağışlayana karşı ağır bir suç işlemişse bağışlayan elden bağışlamayı geri alabilir ve **bağışlananın istem tarihindeki zenginleşmesi ölçüsünde** geri verilmesini isteyebilir: **150.000 ₺**.",
        '6098 sayılı TBK m. 295',
    ),
    # düzey 2
    '0047': patch(
        'Bağışlamaya ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Bir mirasın reddedilmesi bağışlama sayılmaz\n\nII. Taşınır bağışlama sözü sözlü olarak da geçerli biçimde verilebilir\n\nIII. Bağışlayan, önerisini bağışlanan kabul edinceye kadar geri alabilir',
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'Yalnız III',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'B',
        "TBK m. 285/2'ye göre mirası reddetmek bağışlama değildir (I); m. 293'e göre öneri kabule kadar geri alınabilir (III). m. 288/1'e göre bağışlama sözü **yazılı şekle** tabidir (II yanlış).",
        '6098 sayılı TBK m. 285, 288, 293',
    ),
    # düzey 2
    '0048': patch(
        'Bir yıl süreli konut kira sözleşmesinde kiracı, sürenin bitiminden önce herhangi bir bildirimde bulunmamıştır. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kiraya veren süre bitimine dayanarak sözleşmeyi sona erdirebilir',
            'B': 'Sözleşme sürenin bitiminde sona erer',
            'C': 'Sözleşme belirsiz süreli hâle gelir, kira yeniden belirlenir',
            'D': 'Sözleşme aynı koşullarla bir yıl uzatılmış sayılır',
            'E': 'Kiracı ecrimisil ödemekle yükümlü olur',
        },
        'D',
        "TBK m. 347'ye göre konut ve çatılı işyeri kiralarında kiracı, **süre bitiminden en az on beş gün önce bildirimde bulunmadıkça sözleşme aynı koşullarla bir yıl için uzatılmış sayılır**; kiraya veren süre bitimine dayanarak sözleşmeyi sona erdiremez.",
        '6098 sayılı TBK m. 347',
    ),
    # düzey 3
    '0049': patch(
        'Belirli süreli bir konut kira sözleşmesi, kiracı bildirimde bulunmadığı için yıllardır uzamaktadır ve on yıllık uzama süresi dolmuştur. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Fesih bildirimi yazılı yapılmalıdır',
            'B': 'Kiracı da süre bitiminden on beş gün önce bildirimle çıkabilir',
            'C': 'On yıldan önce kiraya veren süre bitimine dayanamazdı',
            'D': 'Kiraya veren, uzama yılı bitiminden üç ay önce bildirimle son verebilir',
            'E': 'Kiraya veren sebep göstermedikçe sözleşmeyi sona erdiremez',
        },
        'E',
        "TBK m. 347'ye göre **on yıllık uzama süresi sonunda kiraya veren, bu süreyi izleyen her uzama yılının bitiminden en az üç ay önce bildirimde bulunmak koşuluyla, herhangi bir sebep göstermeksizin** sözleşmeye son verebilir; m. 348'e göre fesih bildirimi yazılı olmalıdır.",
        '6098 sayılı TBK m. 347, 348',
    ),
    # düzey 2
    '0050': patch(
        'Kiracı B, kiraya verenin yazılı rızasıyla dairenin mutfağını yenilemiş; bu konuda başka bir yazılı anlaşma yapılmamıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Kiraya veren kiralananın eski durumuyla geri verilmesini isteyemez',
            'B': 'Rıza, yenilemenin yapılmasına izin verir',
            'C': 'Yenilik için kiraya verenin yazılı rızası gerekir',
            'D': 'B, yenilemenin sağladığı değer artışının karşılığını isteyebilir',
            'E': 'Aksine yazılı anlaşma olsaydı değer artışı istenebilirdi',
        },
        'D',
        "TBK m. 321'e göre kiracı kiraya verenin **yazılı rızasıyla** yenilik yapabilir; rıza gösteren kiraya veren, yazılı olarak kararlaştırılmadıkça eski durumla geri verilmesini isteyemez; **kiracı da aksine yazılı anlaşma yoksa değer artışının karşılığını isteyemez**.",
        '6098 sayılı TBK m. 321',
    ),
    # düzey 3
    '0051': patch(
        'Konut kirasına ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Kiracıdan istenecek güvence üç aylık kira bedelini aşamaz\n\nII. Kiracı, kiraya verenin yazılı rızası olmadan alt kiraya veremez\n\nIII. Fesih bildiriminin geçerliliği yazılı yapılmasına bağlıdır',
        {
            'A': 'I, II ve III',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'A',
        "TBK m. 342'ye göre güvence üç aylık kirayı aşamaz (I); m. 322/2'ye göre konut kirasında alt kira yazılı rızaya bağlıdır (II); m. 348'e göre fesih bildirimi yazılı olmalıdır (III).",
        '6098 sayılı TBK m. 310, 322, 342, 348',
    ),
    # düzey 3
    '0052': patch(
        "A, B'ye geri verme günü, bildirim süresi veya istem anında muaccel olacağı kararlaştırılmadan ödünç para vermiş; ödüncü ilk kez 1 Mart'ta geri istemiştir. B en erken hangi tarihte geri vermekle yükümlüdür?",
        {
            'A': '1 Mart',
            'B': '12 Nisan',
            'C': '15 Mart',
            'D': '1 Mayıs',
            'E': '1 Nisan',
        },
        'B',
        "TBK m. 392'ye göre belirli bir gün, bildirim süresi veya istem anında muacceliyet kararlaştırılmamışsa ödünç alan, **ilk istemden başlayarak altı hafta geçmedikçe** ödüncü geri vermekle yükümlü değildir: 1 Mart + 42 gün = **12 Nisan**.",
        '6098 sayılı TBK m. 392',
    ),
    # düzey 2
    '0053': patch(
        'Bir yazılımcı, bir şirkete bağımlı olarak aylık ücretle belirsiz süreli çalışmayı; bir diğeri ise şirkete belirli bir mobil uygulamayı götürü bedelle teslim etmeyi üstlenmiştir. Sözleşmelerin niteliği hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İlki vekâlet, ikincisi eser sözleşmesidir',
            'B': 'İlki eser, ikincisi hizmet sözleşmesidir',
            'C': 'Her ikisi de vekâlet sözleşmesidir',
            'D': 'Her ikisi de hizmet sözleşmesidir',
            'E': 'İlki hizmet, ikincisi eser sözleşmesidir',
        },
        'E',
        "TBK m. 393'e göre hizmet sözleşmesinde işçi işverene **bağımlı olarak** iş görür ve zamana veya işe göre ücret alır. m. 470'e göre eser sözleşmesinde yüklenici **bir eser meydana getirmeyi** (sonucu) üstlenir.",
        '6098 sayılı TBK m. 393, 470',
    ),
    # düzey 3
    '0054': patch(
        'Yüklenici, iş sahibinin arsası üzerine inşa ettiği evi ayıplı olarak teslim etmiştir; evin sökülüp kaldırılması iş sahibine aşırı zarar doğuracaktır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'İş sahibi sözleşmeden dönerek evin kaldırılmasını isteyebilir',
            'B': 'İş sahibi ayıp oranında bedelden indirim isteyebilir',
            'C': 'Aşırı masraf gerektirmiyorsa masrafı yükleniciye ait onarım istenebilir',
            'D': 'İş sahibinin genel hükümlere göre tazminat hakkı saklıdır',
            'E': 'Bu durumda dönme hakkı kullanılamaz',
        },
        'A',
        "TBK m. 475'e göre iş sahibi dönme, bedelden indirim veya ücretsiz onarım haklarından birini kullanabilir; ancak **eser iş sahibinin taşınmazı üzerinde yapılmış olup sökülüp kaldırılması aşırı zarar doğuracaksa iş sahibi sözleşmeden dönme hakkını kullanamaz**.",
        '6098 sayılı TBK m. 475',
    ),
    # düzey 3
    '0055': patch(
        "İş sahibi, bedeli 300.000 ₺ olan eser tamamlanmadan sözleşmeyi feshetmiştir. Yapılmış kısmın karşılığı 120.000 ₺, yüklenicinin diğer zararları 40.000 ₺'dir. İş sahibi yükleniciye toplam kaç ₺ ödemelidir?",
        {
            'A': '120.000',
            'B': '300.000',
            'C': '140.000',
            'D': '160.000',
            'E': '180.000',
        },
        'D',
        "TBK m. 484'e göre iş sahibi, **eserin tamamlanmasından önce yapılmış olan kısmın karşılığını ödemek ve yüklenicinin bütün zararlarını gidermek koşuluyla** sözleşmeyi feshedebilir: 120.000 + 40.000 = **160.000 ₺**.",
        '6098 sayılı TBK m. 484',
    ),
    # düzey 2
    '0056': patch(
        "Vekil B, A'nın işini yürütürken tahsil ettiği 50.000 ₺'yi A'ya teslim etmekte gecikmiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "B, aldığı parayı A'ya vermekle yükümlüdür",
            'B': 'B, geciktiği paranın faizini ödemelidir',
            'C': 'B, istem üzerine yürüttüğü işin hesabını vermelidir',
            'D': 'B, işi sadakat ve özenle yürütmelidir',
            'E': 'Gecikme nedeniyle B faiz ödemekle yükümlü değildir',
        },
        'E',
        "TBK m. 508'e göre vekil, istem üzerine yürüttüğü işin hesabını vermek ve vekâletle ilgili aldıklarını vermekle yükümlüdür; **tesliminde geciktiği paranın faizini de öder**. m. 506'ya göre sadakat ve özen borcu vardır.",
        '6098 sayılı TBK m. 506, 508',
    ),
    # düzey 3
    '0057': patch(
        "Simsar B'nin aracılığıyla, alıcının kredi onayı alması koşuluyla bir araç satış sözleşmesi kurulmuştur; kredi henüz onaylanmamıştır. Simsarlık sözleşmesinde giderlerin ödeneceği kararlaştırılmamıştır. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Sözleşme kurulduğundan ücret hemen ödenir',
            'B': 'Ücret, kredi onayı gerçekleşirse ödenir',
            'C': 'B ücreti alamaz, ancak giderlerini isteyebilir',
            'D': 'Simsar ücrete hak kazanamaz',
            'E': 'Ücret, koşul gerçekleşmese de yarı oranda ödenir',
        },
        'B',
        "TBK m. 521'e göre simsar faaliyeti sonucunda sözleşme kurulursa ücrete hak kazanır; **kurulan sözleşme geciktirici koşula bağlanmışsa ücret, koşulun gerçekleşmesi hâlinde ödenir**. Giderler ancak kararlaştırılmışsa ödenir.",
        '6098 sayılı TBK m. 521',
    ),
    # düzey 2
    '0058': patch(
        "B, C'nin A'ya olan borcuna kefil olmak üzere bilgisayarla hazırlanmış bir sözleşmeyi imzalamıştır; sözleşmede azami miktar ve tarih yazılıdır, ancak B bunları kendi el yazısıyla belirtmemiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Azami miktarın kefilin el yazısıyla belirtilmesi şarttır',
            'B': 'Kefalet tarihinin de el yazısıyla belirtilmesi gerekir',
            'C': 'Sözleşme yazılı ve imzalı olduğundan geçerlidir',
            'D': 'Şekil eksikliği nedeniyle kefalet geçersizdir',
            'E': 'Kefalet yazılı şekilde yapılmalıdır',
        },
        'C',
        "TBK m. 583'e göre kefalet yazılı yapılmalı; **kefilin sorumlu olduğu azami miktarı, kefalet tarihini ve müteselsil kefalette bu sıfatı kendi el yazısıyla belirtmesi** şarttır.",
        '6098 sayılı TBK m. 583',
    ),
    # düzey 3
    '0059': patch(
        "C, B'nin A'ya olan borcuna adi kefil olmuştur. B borcunu ödememiştir; hakkında iflas, konkordato veya takip işlemi yoktur. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'C, borcun yarısından sorumludur',
            'B': "A, önce B'ye başvurmadıkça C'yi takip edemez",
            'C': "A, B'ye ihtar çekmesi hâlinde C'yi takip edebilir",
            'D': "A, dilerse doğrudan C'yi takip edebilir",
            'E': 'C, B ile müteselsilen sorumludur',
        },
        'B',
        "TBK m. 585'e göre **adi kefalette alacaklı, borçluya başvurmadıkça kefili takip edemez**; kesin aciz belgesi, iflas, konkordato mehli veya Türkiye'de takibin imkânsızlaşması hâllerinde doğrudan kefile başvurabilir.",
        '6098 sayılı TBK m. 585',
    ),
    # düzey 3
    '0060': patch(
        "Gerçek kişi C, 1 Ocak 2016'da bir borca süresiz olarak kefil olmuştur; kefalet uzatılmamış ve yeni kefalet verilmemiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "Kefalet 1 Ocak 2026'da ortadan kalkar",
            'B': 'On yıllık süre sözleşmenin kurulmasından işler',
            'C': 'Asıl borç sona erseydi C de borçtan kurtulurdu',
            'D': "C'nin kefaleti asıl borç sona erinceye kadar devam eder",
            'E': 'Uzatma, kefalet sözleşmesinin şekline uygun yazılı açıklamayla yapılabilirdi',
        },
        'D',
        "TBK m. 598'e göre **bir gerçek kişi tarafından verilmiş her türlü kefalet, sözleşmenin kurulmasından başlayarak on yılın geçmesiyle kendiliğinden ortadan kalkar**; süre, kefilin sözleşme şekline uygun yazılı açıklamasıyla uzatılabilir. Asıl borç sona erince kefil de kurtulur.",
        '6098 sayılı TBK m. 598',
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
    print(f"1 paket / {len(PATCHES)} soru ('Sozlesme Turleri' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
