#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Temerrut ve Tazminat — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Borclar hukuku gercek sinav profiliyle yeniden yazim (eski surumde celdiricilerin buyuk kismi mutlak ifadeliydi, kor %50): alacakli temerrudu ve tevdi-satma, borca aykirilik ve kusur karinesi, sorumsuzluk anlasmalari, yardimci kisiler, borclu temerrudu ve temerrut faizi, asan zarar, secimlik haklar, ifa imkansizligi ve asiri ifa guclugu. Gercek sinav kaliplari (agir kusurdan sorumsuzluk, akdi temerrut faizi siniri, temerrut dogru/yanlis listeleri) olaylara cevrildi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 6098 sayili Turk Borclar Kanunu m. 106-126, 136-138 guncel metni (mevzuat.gov.tr)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/borclar_hukuku/temerrut_tazminat.json"
STYLE_REF = 'SGS Borclar Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "temerrut-gen-"


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
        'Satıcı, kararlaştırılan gün ve yerde malı gereği gibi teslim etmek istemiş; alıcı haklı bir sebep göstermeden malı almaktan kaçınmıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Alıcı alacaklı temerrüdüne düşmüştür',
            'B': 'Alıcının kabulden kaçınmasının haklı sebebi yoktur',
            'C': 'Satıcı borçlu temerrüdüne düşmüştür',
            'D': 'Tevdi hâlinde hasar ve giderler alıcıya aittir',
            'E': 'Satıcı malı tevdi ederek borçtan kurtulabilir',
        },
        'C',
        "TBK m. 106'ya göre edimi gereği gibi kendisine önerilen alacaklı **haklı bir sebep olmaksızın kabulden kaçınırsa** temerrüde düşer; m. 107'ye göre borçlu, hasar ve giderleri alacaklıya ait olmak üzere tevdi ederek borcundan kurtulabilir.",
        '6098 sayılı TBK m. 106, 107',
    ),
    # düzey 3
    '0002': patch(
        'Alacaklı temerrüdü nedeniyle teslim edilemeyen bir kamyon dolusu taze sebze bozulmak üzeredir. Sebzelerin halde oluşan bir piyasa fiyatı vardır. Borçlunun hakları hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Alacaklıya ihtar edilmeden satış izni verilemez',
            'B': 'Sebzeleri tevdi etmelidir; satış yapılamaz',
            'C': 'Hâkim izniyle sattırabilir; açık artırma şart değildir',
            'D': 'Sebzeleri kendi hesabına satıp bedeli alıkoyabilir',
            'E': 'Hâkim izni aranmadan açık artırmayla sattırmalıdır',
        },
        'C',
        "TBK m. 108'e göre bozulabilir şeyleri borçlu, alacaklıya önceden ihtar koşuluyla **hâkimin izniyle** açık artırmayla sattırıp bedelini tevdi edebilir; şey **borsada kayıtlı veya piyasa fiyatı varsa** ya da değeri gidere oranla azsa, **açık artırma zorunlu değildir** ve hâkim **ihtar koşulunu aramaksızın** satışa izin verebilir.",
        '6098 sayılı TBK m. 108',
    ),
    # düzey 2
    '0003': patch(
        'Alacaklı temerrüdünde borçlunun kullanabileceği haklara ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Teslim edeceği şeyi tevdi ederek borcundan kurtulabilir\n\nII. Bozulabilir malı hâkim izniyle sattırıp bedelini tevdi edebilir\n\nIII. Teslim gerektirmeyen edimlerde de şeyi tevdi etmek zorundadır',
        {
            'A': 'Yalnız II',
            'B': 'I, II ve III',
            'C': 'Yalnız I',
            'D': 'I ve III',
            'E': 'I ve II',
        },
        'E',
        "TBK m. 107'ye göre borçlu **tevdi** (I), m. 108'e göre **bozulabilir malı hâkim izniyle sattırma** (II) hakkına sahiptir. m. 110'a göre teslim gerektirmeyen edimlerde borçlu, borçlu temerrüdü hükümlerine göre **sözleşmeden dönebilir**; tevdi söz konusu değildir (III).",
        '6098 sayılı TBK m. 107, 108, 110',
    ),
    # düzey 3
    '0004': patch(
        'Alıcının temerrüdü üzerine satıcı malları hâkimin belirlediği depoya tevdi etmiştir. Bir hafta sonra depoda çıkan ve satıcının kusuruna dayanmayan yangında mallar yanmıştır. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tevdi yangınla geçersiz hâle gelir',
            'B': 'Satıcı malları yeniden teslim etmekle yükümlüdür',
            'C': 'Hasar alıcıya aittir; satıcı bedeli ister',
            'D': 'Hasar tevdi eden satıcıya aittir',
            'E': 'Alıcı ile satıcı hasarı yarı yarıya paylaşır',
        },
        'C',
        "TBK m. 107'ye göre alacaklının temerrüdünde borçlu, **hasar ve giderleri alacaklıya ait olmak üzere** teslim edeceği şeyi tevdi ederek borcundan kurtulabilir.",
        '6098 sayılı TBK m. 107',
    ),
    # düzey 3
    '0005': patch(
        "Evin boyanması için anlaşılan usta, defalarca uyarılmasına rağmen işe başlamamıştır.\n\nTBK'ya göre ev sahibinin haklarıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'İşi başkasına yaptırırsa masrafı ev sahibi karşılar',
            'B': 'Ev sahibi edimin başkasınca ifasına izin verilmesini isteyebilir',
            'C': 'Masraf yapma borcunu ifa etmeyen ustaya aittir',
            'D': 'Ev sahibinin giderim isteme hakkı saklıdır',
            'E': 'İfaya izin için ustanın onayı gerekmez',
        },
        'A',
        'TBK m. 113/1: yapma borcu borçlu tarafından ifa edilmezse alacaklı, masrafı borçluya ait olmak üzere edimin kendisi veya başkası tarafından ifasına izin verilmesini isteyebilir; her türlü giderim isteme hakkı saklıdır.',
        '6098 sayılı TBK m. 113/1',
    ),
    # düzey 2
    '0006': patch(
        'A, komşusunun rica etmesi üzerine tatil süresince onun köpeğine ücretsiz olarak bakmış; köpek hafif bir dikkatsizlik sonucu kaçarak bir süre kaybolmuştur. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Sorumluluğun kapsamı işin özel niteliğine göre belirlenir',
            'B': 'Ücretsiz iş olduğundan A kusurundan sorumlu tutulamaz',
            'C': "İş A'ya bir yarar sağlamamaktadır",
            'D': "A'nın sorumluluğu daha hafif değerlendirilir",
            'E': 'Borçlu genel olarak her türlü kusurdan sorumludur',
        },
        'B',
        "TBK m. 114/1'e göre borçlu **genel olarak her türlü kusurdan sorumludur**; sorumluluğun kapsamı işin özel niteliğine göre belirlenir ve **iş borçlu için bir yarar sağlamıyorsa sorumluluk daha hafif** değerlendirilir; tamamen ortadan kalkmaz.",
        '6098 sayılı TBK m. 114/1',
    ),
    # düzey 3
    '0007': patch(
        'Aşağıdaki önceden yapılan anlaşmalardan hangileri kesin hükümsüzdür?\n\nI. Bir bankanın hafif kusurundan sorumlu olmayacağına ilişkin anlaşma\n\nII. Bir boya ustasının hafif kusurundan sorumlu olmayacağına ilişkin anlaşma\n\nIII. Bir nakliyecinin ağır kusurundan sorumlu olmayacağına ilişkin anlaşma',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'Yalnız III',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'E',
        "TBK m. 115/1'e göre **ağır kusurdan** sorumsuzluk anlaşması kesin hükümsüzdür (III). m. 115/3'e göre uzmanlık gerektiren ve **ancak izinle yürütülebilen** meslekte (banka) **hafif kusurdan** sorumsuzluk da hükümsüzdür (I). İzne bağlı olmayan meslekte hafif kusurdan sorumsuzluk geçerlidir (II).",
        '6098 sayılı TBK m. 115',
    ),
    # düzey 2
    '0008': patch(
        'Aşağıdaki hâllerden hangilerinde borçlu ihtara gerek olmaksızın temerrüde düşer?\n\nI. İyiniyetli sebepsiz zenginleşenin geri verme borcu\n\nII. Birlikte belirlenen ifa gününün geçmesi\n\nIII. Haksız fiilden doğan tazminat borcu',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'II ve III',
            'D': 'Yalnız II',
            'E': 'Yalnız III',
        },
        'C',
        "TBK m. 117/2'ye göre **birlikte belirlenen ifa gününün geçmesiyle** (II), **haksız fiilde fiilin işlendiği** (III) tarihte borçlu temerrüde düşer. Sebepsiz zenginleşmede temerrüt zenginleşme tarihindedir; ancak **sebepsiz zenginleşen iyiniyetli ise temerrüt için bildirim şarttır** (I).",
        '6098 sayılı TBK m. 117',
    ),
    # düzey 3
    '0009': patch(
        'Teslimde temerrüde düşen satıcının deposundaki mallar yıldırım sonucu yanmıştır. Satıcı, alıcının deposunun da aynı gün aynı yıldırım nedeniyle yandığını ve malları zamanında teslim etseydi de yanacağını ispat etmiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Satıcı zamanında ifa etseydi de zararın doğacağını ispat ederek kurtulabilir',
            'B': 'Temerrütteki borçlu beklenmedik hâlden sorumlu olduğundan satıcı zararı öder',
            'C': 'Satıcı temerrüde düşmekte kusursuz olduğunu ispat ederek de kurtulabilirdi',
            'D': 'Temerrütteki borçlu kural olarak beklenmedik hâlden sorumludur',
            'E': 'Satıcı bu olayda beklenmedik hâlden doğan zarardan sorumlu değildir',
        },
        'B',
        "TBK m. 119'a göre temerrüde düşen borçlu **beklenmedik hâl** sebebiyle doğacak zarardan sorumludur; ancak **temerrüde düşmekte kusuru olmadığını veya borcunu zamanında ifa etmiş olsaydı bile beklenmedik hâlin ifa konusu şeye zarar vereceğini** ispat ederek kurtulabilir.",
        '6098 sayılı TBK m. 119',
    ),
    # düzey 3
    '0010': patch(
        "Bir kredi sözleşmesinde yıllık akdi faiz %30 olarak kararlaştırılmış, temerrüt faizi için hüküm konulmamıştır. Mevzuata göre yıllık faiz oranı %24'tür. Borçlu temerrüde düşmüştür. Uygulanacak yıllık temerrüt faizi oranı yüzde kaçtır?",
        {
            'A': '%60',
            'B': '%27',
            'C': '%24',
            'D': '%30',
            'E': '%48',
        },
        'D',
        "TBK m. 120/3'e göre **akdî faiz oranı kararlaştırılmakla birlikte sözleşmede temerrüt faizi kararlaştırılmamışsa ve yıllık akdî faiz oranı mevzuattaki orandan fazla ise, temerrüt faizi oranı hakkında akdî faiz oranı geçerli** olur: **%30**.",
        '6098 sayılı TBK m. 120/3',
    ),
    # düzey 2
    '0011': patch(
        'Borçlu bir para borcunda iki yıldır temerrüttedir ve 50.000 ₺ temerrüt faizi birikmiştir. Alacaklı, bu birikmiş faize de temerrüt faizi işletilmesini istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Temerrüt faizine ayrıca temerrüt faizi yürütülemez',
            'B': 'Faiz oranı kararlaştırılmamışsa mevzuata göre belirlenir',
            'C': 'Anapara için temerrüt faizi işlemeye devam eder',
            'D': 'Koşulları varsa temerrüt faizini aşan zarar ayrıca istenebilir',
            'E': 'Birikmiş temerrüt faizine de temerrüt faizi işletilerek anaparaya eklenir',
        },
        'E',
        "TBK m. 121/3'e göre **temerrüt faizine, ayrıca temerrüt faizi yürütülemez**. m. 120 oranı, m. 122 aşkın zararı düzenler.",
        '6098 sayılı TBK m. 120-122',
    ),
    # düzey 3
    '0012': patch(
        'Temerrüde düşen satıcıya verilen süre de sonuçsuz kalınca alıcı sözleşmeden dönmüştür. Alıcı önceden 20.000 ₺ kapora ödemiş ve sözleşme için 3.000 ₺ gider yapmıştır. Satıcı kusursuzluğunu ispat edememiştir. Alıcı toplam kaç ₺ isteyebilir?',
        {
            'A': '17.000',
            'B': '3.000',
            'C': '40.000',
            'D': '20.000',
            'E': '23.000',
        },
        'E',
        "TBK m. 125/3'e göre sözleşmeden dönme hâlinde taraflar **daha önce ifa ettikleri edimleri geri isteyebilir** (20.000 ₺); borçlu kusursuzluğunu ispat edemezse alacaklı **sözleşmenin hükümsüz kalması sebebiyle uğradığı zararı** (olumsuz zarar: 3.000 ₺) da isteyebilir: **23.000 ₺**.",
        '6098 sayılı TBK m. 125/3',
    ),
    # düzey 3
    '0013': patch(
        'Sözleşmede alacaklıya, ödeme gününü bildirimle belirleme hakkı tanınmıştır. Alacaklı usulüne uygun bildirimle ödeme gününü 10 Nisan olarak belirlemiştir. Borçlu o gün ödeme yapmamıştır. Borçlunun temerrüdü hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bildirim tarihinde temerrüde düşer',
            'B': 'Ayrı bir ihtar yapılmadıkça temerrüde düşmez',
            'C': 'Bir aylık ek süre geçtikten sonra temerrüde düşer',
            'D': "10 Nisan'ın geçmesiyle temerrüde düşer",
            'E': 'Ancak icra takibiyle temerrüde düşer',
        },
        'D',
        "TBK m. 117/2'ye göre borcun ifa edileceği gün **sözleşmede saklı tutulan bir hakka dayanarak taraflardan biri usulüne uygun bir bildirimde bulunmak suretiyle belirlemişse, bu günün geçmesiyle** borçlu temerrüde düşer.",
        '6098 sayılı TBK m. 117/2',
    ),
    # düzey 2
    '0014': patch(
        "Bir para borcunun sözleşmesinde ne akdi faiz ne de temerrüt faizi kararlaştırılmıştır. Borçlu temerrüde düşmüştür.\n\nTBK'ya göre temerrüt faiziyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Temerrüt faizi oranı sözleşmede kararlaştırılabilir',
            'B': 'Kararlaştırılmamışsa borcun doğduğu tarihteki mevzuat uygulanır',
            'C': 'Temerrüde düşen borçlu temerrüt faizi öder',
            'D': 'Oran alacaklının belirleyeceği orandır',
            'E': 'Oran hâkimin serbest takdirine bırakılmamıştır',
        },
        'D',
        'TBK m. 120/1: uygulanacak yıllık temerrüt faizi oranı, sözleşmede kararlaştırılmamışsa faiz borcunun doğduğu tarihte yürürlükte olan mevzuat hükümlerine göre belirlenir; alacaklının ya da hâkimin takdirine bırakılmamıştır.',
        '6098 sayılı TBK m. 120/1',
    ),
    # düzey 2
    '0015': patch(
        'Karşılıklı borç yükleyen bir sözleşmede satıcı teslimde temerrüde düşmüştür; ifa alıcı için hâlâ yararlıdır ve süre verilmesini gereksiz kılan bir durum yoktur. Alıcının seçimlik haklarını kullanmadan önce yapması gereken nedir?',
        {
            'A': 'Uygun süre vermek veya hâkimden istemek',
            'B': 'Süre vermeden doğrudan olumlu zarar istemek',
            'C': 'Doğrudan sözleşmeden dönmek',
            'D': 'Malı başka yerden alıp bedelini satıcıdan tahsil etmek',
            'E': 'Satıcıya ceza koşulu uygulamak',
        },
        'A',
        "TBK m. 123'e göre karşılıklı borç yükleyen sözleşmelerde taraflardan biri temerrüde düşerse diğeri, **borcun ifası için uygun bir süre verebilir veya uygun bir süre verilmesini hâkimden isteyebilir**; m. 124'teki hâller dışında seçimlik haklara ancak bu süre sonunda geçilir.",
        '6098 sayılı TBK m. 123',
    ),
    # düzey 2
    '0016': patch(
        'Temerrüde düşen borçlunun sorumluluğuna ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Kusursuzluğunu ispat etmedikçe gecikme zararını öder\n\nII. Beklenmedik hâlden kural olarak sorumlu değildir\n\nIII. Temerrüt faizini aşan zararı da kusursuzluğunu ispat etmedikçe öder',
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'I, II ve III',
            'D': 'I ve II',
            'E': 'Yalnız III',
        },
        'B',
        "TBK m. 118'e göre borçlu kusursuzluğunu ispat etmedikçe **gecikme zararını** (I), m. 122'ye göre **aşkın zararı** (III) öder. m. 119'a göre temerrüdeki borçlu **beklenmedik hâlden kural olarak sorumludur** (II yanlış).",
        '6098 sayılı TBK m. 118, 119, 122',
    ),
    # düzey 3
    '0017': patch(
        "Satıcı, satış bedelinin 30.000 ₺'lik kısmını peşin almıştı. Teslimden önce mal, satıcının sorumlu tutulamayacağı bir sebeple yok olmuştur; hasarın alıcıya yüklendiğine dair bir hüküm yoktur. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Satıcı, kalan satış bedelini alıcıdan isteyebilir',
            'B': 'Satıcının teslim borcu sona ermiştir',
            'C': 'Satıcı henüz kendisine ifa edilmemiş karşı edimi isteme hakkını kaybeder',
            'D': "Satıcı aldığı 30.000 ₺'yi sebepsiz zenginleşme hükümlerine göre geri verir",
            'E': 'Hasar kanun veya sözleşmeyle alıcıya yüklenmiş olsaydı sonuç farklı olabilirdi',
        },
        'A',
        "TBK m. 136/2'ye göre karşılıklı sözleşmelerde imkânsızlık sebebiyle borçtan kurtulan borçlu, **karşı taraftan almış olduğu edimi sebepsiz zenginleşme hükümleri uyarınca geri vermekle** yükümlüdür ve **henüz kendisine ifa edilmemiş olan edimi isteme hakkını kaybeder**; hasarın alacaklıya yüklendiği durumlar hariçtir.",
        '6098 sayılı TBK m. 136/2',
    ),
    # düzey 3
    '0018': patch(
        'Bir düğün organizasyonu için kiralanan salonun yalnızca mutfak bölümü kullanılamaz hâle gelmiş ve taraflarca mutfaksız bir salonun hiç kiralanmayacağı açıkça anlaşılmaktadır. Borç hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kısmi imkânsızlık borcun tamamını etkilemez',
            'B': 'Borçlu salonu eksiksiz teslim etmekle yükümlüdür',
            'C': 'Borçlu mutfak kısmından kurtulur, salonu teslim eder',
            'D': 'Sözleşme baştan kesin hükümsüzdür',
            'E': 'Borcun tamamı sona erer, salon teslim edilmez',
        },
        'E',
        "TBK m. 137/1'e göre kısmi imkânsızlıkta borçlu kural olarak **sadece imkânsızlaşan kısımdan kurtulur**; ancak **bu kısmi imkânsızlık önceden öngörülseydi taraflarca böyle bir sözleşmenin yapılmayacağı açıkça anlaşılırsa, borcun tamamı sona erer**.",
        '6098 sayılı TBK m. 137/1',
    ),
    # düzey 3
    '0019': patch(
        'Aşırı ifa güçlüğüne ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Haklarını saklı tutarak ifa etmiş borçlu da uyarlama isteyebilir',
            'B': 'Olağanüstü durum sözleşme sırasında öngörülmemiş ve öngörülmesi beklenmemiş olmalıdır',
            'C': 'Hükmün yabancı para borçlarında uygulanması mümkün değildir',
            'D': 'Olağanüstü durum borçludan kaynaklanmamış olmalıdır',
            'E': 'Sürekli edimli sözleşmelerde kural olarak dönme yerine fesih hakkı kullanılır',
        },
        'C',
        "TBK m. 138/2'ye göre **bu madde hükmü yabancı para borçlarında da uygulanır**. Diğer ifadeler m. 138/1'deki koşullara ve sürekli edimli sözleşmelerde fesih kuralına uygundur.",
        '6098 sayılı TBK m. 138',
    ),
    # düzey 3
    '0020': patch(
        '100 ton malın satışında 40 ton satıcının sorumlu olmadığı bir sebeple yok olmuştur. Alıcı, kalan 60 tonu kabul etmeyeceğini bildirmiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sözleşme baştan kesin hükümsüz sayılır',
            'B': 'Tam imkânsızlık hükümleri uygulanır; karşı edim istenemez',
            'C': 'Satıcı eksik 40 tonu başka yerden temin etmekle yükümlüdür',
            'D': 'Alıcı bedelin tamamını ödemekle yükümlüdür',
            'E': 'Alıcı 60 tonu kabul etmek ve bedelini ödemekle yükümlüdür',
        },
        'B',
        "TBK m. 137/2'ye göre karşılıklı sözleşmelerde bir tarafın borcu kısmen imkânsızlaşır ve **alacaklının kısmi ifaya razı olmaması** hâlinde **tam imkânsızlık hükümleri** uygulanır; m. 136/2 uyarınca karşı edim istenemez ve alınmış edim iade edilir.",
        '6098 sayılı TBK m. 137/2',
    ),
    # düzey 3
    '0021': patch(
        "A ve B, C'ye karşı müteselsil borçludur. A borcu gereği gibi ifa etmeyi önermiş, C haklı bir sebep olmaksızın kabulden kaçınmıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "C'nin kabulden kaçınması haklı bir sebebe dayanmamaktadır",
            'B': "C, B'ye karşı da temerrüde düşmüş olur",
            'C': 'C alacaklı temerrüdüne düşmüştür',
            'D': 'A, teslim edilecek bir şey varsa bunu tevdi ederek borçtan kurtulabilir',
            'E': "C, ifayı öneren A'ya karşı temerrüde düşmüş, B'ye karşı düşmemiştir",
        },
        'E',
        "TBK m. 106/2'ye göre **alacaklı, müteselsil borçlulardan birine karşı temerrüde düşerse, diğerlerine karşı da temerrüde düşmüş olur**; m. 107'ye göre borçlu tevdi ile borçtan kurtulabilir.",
        '6098 sayılı TBK m. 106/2',
    ),
    # düzey 2
    '0022': patch(
        'Borçlu, alacaklı temerrüdü üzerine malı tevdi etmiştir. Alacaklı henüz tevdi edilen malı kabul ettiğini açıklamamıştır ve tevdi bir rehni ortadan kaldırmamıştır. Borçlu malı geri almak istemektedir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Geri alabilir; alacak yan haklarıyla sürer',
            'B': 'Geri alırsa alacak yan hakları olmadan devam eder',
            'C': 'Geri alma hâlinde borç sona erer',
            'D': 'Geri alma ancak alacaklının onayıyla mümkündür',
            'E': 'Tevdiden sonra mal geri alınamaz',
        },
        'A',
        "TBK m. 109'a göre alacaklı tevdi edilen şeyi kabul ettiğini açıklamış veya tevdi bir rehnin ortadan kaldırılması sonucunu doğurmuş olmadıkça borçlu, **tevdi edilen şeyi geri alabilir**; geri alındığı anda **alacak bütün yan haklarıyla birlikte varlığını sürdürür**.",
        '6098 sayılı TBK m. 109',
    ),
    # düzey 2
    '0023': patch(
        'FOB koşuluyla yapılan satışta alıcı, malların yükleneceği gemiyi kararlaştırılan tarihte limana göndermemiştir; satıcı mallarla limanda hazırdır. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Temerrüt için alıcıya ayrıca ihtar gerekir',
            'B': 'Satıcı teslim edemediği için borçlu temerrüdüne düşmüştür',
            'C': 'Hazırlık fiilleri alacaklı temerrüdünü etkilemez',
            'D': 'Sözleşme alıcının gecikmesiyle kesin hükümsüz olur',
            'E': 'Alıcı alacaklı temerrüdüne düşmüştür',
        },
        'E',
        "TBK m. 106'ya göre alacaklı, edimi kabulden **veya borçlunun borcunu ifa edebilmesi için kendisi tarafından yapılması gereken hazırlık fiillerini yapmaktan** haklı sebep olmaksızın kaçınırsa temerrüde düşer.",
        '6098 sayılı TBK m. 106',
    ),
    # düzey 2
    '0024': patch(
        'Bir nakliyeci, taşıdığı eşyayı hasarlı olarak teslim etmiştir. Eşya sahibinin tazminat istemine ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Nakliyeci kusursuz olsa da zararı öder',
            'B': 'Eşya sahibi nakliyecinin kusurunu ispat etmelidir',
            'C': 'Nakliyeci kusursuzluğunu ispat etmedikçe zararı öder',
            'D': 'Tazminat ancak haksız fiil hükümlerine göre istenebilir',
            'E': 'Nakliyeci ağır kusuru varsa sorumludur',
        },
        'C',
        "TBK m. 112'ye göre borç hiç veya **gereği gibi ifa edilmezse borçlu, kendisine hiçbir kusurun yüklenemeyeceğini ispat etmedikçe** alacaklının zararını gidermekle yükümlüdür. Sözleşmeye aykırılıkta kusur karinesi borçlu aleyhinedir.",
        '6098 sayılı TBK m. 112',
    ),
    # düzey 3
    '0025': patch(
        'Sözleşmeye aykırılık ile haksız fiil sorumluluğu arasındaki farka ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sözleşmeye aykırılıkta da borçlunun kusurunu alacaklı ispat eder',
            'B': 'Haksız fiil hükümleri sözleşmeye aykırılığa kıyasen uygulanır',
            'C': 'Haksız fiilde kusurun ispatı zarar görene aittir',
            'D': 'Sözleşmeye aykırılıkta borçlu kusursuzluğunu ispat ederek kurtulabilir',
            'E': 'Her iki sorumlulukta da zararın varlığı aranır',
        },
        'A',
        "TBK m. 112'ye göre sözleşmeye aykırılıkta **borçlu kusursuzluğunu ispat etmedikçe** sorumludur (kusur karinesi); m. 50'ye göre haksız fiilde ise **kusuru zarar gören ispat eder**. m. 114/2'ye göre haksız fiil hükümleri sözleşmeye aykırılığa kıyasen uygulanır.",
        '6098 sayılı TBK m. 49, 112',
    ),
    # düzey 3
    '0026': patch(
        "Kiralanan aracın frenlerinin arızalı teslim edilmesi nedeniyle kiracı kaza yapmış; kiracının da hız sınırını aşarak zararın artmasına katkıda bulunduğu anlaşılmıştır.\n\nTBK'ya göre kiracının sözleşmeye dayanan tazminat istemiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Sözleşmeye aykırılıkta indirim sebepleri uygulanmaz',
            'B': 'Haksız fiil hükümleri sözleşmeye aykırılığa kıyasen uygulanır',
            'C': 'Zarar görenin zararın artmasına katkısı indirim sebebidir',
            'D': 'Hâkim tazminatta indirim yapabilir',
            'E': 'Koşulları varsa hâkim tazminatı kaldırabilir',
        },
        'A',
        "TBK m. 114/2: haksız fiil sorumluluğuna ilişkin hükümler kıyas yoluyla sözleşmeye aykırılık hâllerine de uygulanır; zarar görenin zararın artmasında etkili olması m. 52'ye göre hâkime tazminatı indirme ya da kaldırma imkânı veren bir sebeptir.",
        '6098 sayılı TBK m. 114/2, 52',
    ),
    # düzey 3
    '0027': patch(
        'Bir oto tamircisinin yanında çalışan çırak, müşterinin aracını tamir sırasında çizmiştir. Müşteri zararını tamirciden istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Tamirci çırağın verdiği zarardan sorumludur',
            'B': 'Tamircinin sorumluluğu sözleşmeye aykırılığa dayanır',
            'C': 'Tamirci, çırağı seçmede özen gösterdiğini ispat ederse sorumlu olmaz',
            'D': 'Çırak zararı işi yürütürken vermiştir',
            'E': 'Bu sorumluluk önceden yapılan anlaşmayla kaldırılabilirdi',
        },
        'C',
        "TBK m. 116'ya göre borçlu, ifayı **yardımcılarına bırakmış olsa bile, onların işi yürüttükleri sırada diğer tarafa verdikleri zararı** gidermekle yükümlüdür; m. 66'daki özen ispatıyla kurtuluş burada öngörülmemiştir. Bu sorumluluk izinli uzmanlık mesleği dışında önceden anlaşmayla kaldırılabilir.",
        '6098 sayılı TBK m. 116',
    ),
    # düzey 2
    '0028': patch(
        "Taraflar borcun 15 Haziran'da ödeneceğini birlikte kararlaştırmıştır. Borçlu o gün ödeme yapmamış, alacaklı da ihtarda bulunmamıştır. Borçlunun temerrüdü hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Temerrüt faizi ancak icra takibiyle başlar',
            'B': 'İhtar yapılmadıkça temerrüde düşmez',
            'C': 'İhtara gerek olmadan temerrüde düşer',
            'D': 'Temerrüt için bir aylık ek süre geçmelidir',
            'E': 'Ancak dava açılınca temerrüde düşer',
        },
        'C',
        "TBK m. 117/2'ye göre **borcun ifa edileceği gün birlikte belirlenmişse bu günün geçmesiyle** borçlu temerrüde düşer; ayrıca ihtar gerekmez (belirli vadeli borç).",
        '6098 sayılı TBK m. 117/2',
    ),
    # düzey 3
    '0029': patch(
        "B, kendisine yanlışlıkla havale edilen 50.000 ₺'nin başkasına ait olduğundan habersizdir. Havale 1 Mart'ta yapılmış, gönderen durumu B'ye 1 Nisan'da bildirmiştir. B'nin temerrüdü hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Zenginleşmenin gerçekleştiği 1 Mart'ta temerrüde düşer",
            'B': 'Ancak dava açılınca temerrüde düşer',
            'C': 'İcra takibi başlatılınca temerrüde düşer',
            'D': "Bildirimle, 1 Nisan'da temerrüde düşer",
            'E': 'İyiniyetli zenginleşen temerrüde düşmez',
        },
        'D',
        "TBK m. 117/2'ye göre sebepsiz zenginleşmede borçlu **zenginleşmenin gerçekleştiği tarihte** temerrüde düşer; **ancak sebepsiz zenginleşenin iyiniyetli olduğu hâllerde temerrüt için bildirim şarttır**.",
        '6098 sayılı TBK m. 117/2',
    ),
    # düzey 3
    '0030': patch(
        "A, B'ye 100.000 ₺ bağışlamayı yazılı olarak vaat etmiş, ancak ödemede temerrüde düşmüştür. B, 1 Mart'ta ihtarname göndermiş, 1 Haziran'da dava açmıştır. Temerrüt faizi hangi tarihten itibaren işler?",
        {
            'A': 'Kararın kesinleştiği tarih',
            'B': 'Bağışlama vaadinin yapıldığı tarih',
            'C': '1 Nisan',
            'D': '1 Haziran',
            'E': '1 Mart',
        },
        'D',
        "TBK m. 121'e göre **faiz veya irat borcunu ya da bağışladığı bir miktar parayı ödemekte temerrüde düşen borçlu, icra takibine girişildiği veya dava açıldığı günden** başlayarak temerrüt faizi ödemekle yükümlüdür; ihtar tarihi esas alınmaz.",
        '6098 sayılı TBK m. 121',
    ),
    # düzey 2
    '0031': patch(
        'Aşağıdaki hâllerden hangilerinde temerrüde düşen borçluya ek süre verilmesine gerek yoktur?\n\nI. Düğün günü getirilmesi gereken pastanın o gün getirilmemesi\n\nII. Borçlunun artık hiçbir şekilde ifa etmeyeceğini açıkça bildirmesi\n\nIII. Borçlunun birkaç gün gecikmesi, ifanın alacaklı için hâlâ yararlı olması',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'Yalnız I',
            'D': 'I ve III',
            'E': 'Yalnız II',
        },
        'A',
        "TBK m. 124'e göre süre verilmesine gerek yoktur: ifanın **belirli bir zamanda gerçekleşmemesi üzerine artık kabul edilmeyeceği sözleşmeden anlaşılıyorsa** (I) ve **borçlunun tutumundan süre verilmesinin etkisiz olacağı anlaşılıyorsa** (II). İfa hâlâ yararlıysa (III) m. 123'e göre süre verilmelidir.",
        '6098 sayılı TBK m. 123, 124',
    ),
    # düzey 3
    '0032': patch(
        'Borçlu temerrüdüne ilişkin olaylardan hangisinde varılan sonuç yanlıştır?',
        {
            'A': 'Kesin vadeli pasta siparişinde alıcı süre vermeden dönmüştür',
            'B': 'Alıcı ifa ile birlikte gecikme tazminatı istemiştir',
            'C': 'Alıcı ek süre vermeyi hâkimden istemiştir',
            'D': 'Ek süre gereken hâlde alıcı süre vermeden dönmüştür',
            'E': 'Alıcı ifadan vazgeçtiğini hemen bildirip olumlu zarar istemiştir',
        },
        'D',
        "TBK m. 123'e göre karşılıklı sözleşmelerde alacaklı kural olarak **uygun bir süre verir veya hâkimden ister**; m. 124'teki hâller dışında süre verilmeden seçimlik haklara geçilemez. m. 125 alacaklının seçimlik haklarını düzenler.",
        '6098 sayılı TBK m. 123-125',
    ),
    # düzey 2
    '0033': patch(
        "1 Mart 2025'te meydana gelen bir kazada zarar gören, 1 Eylül 2025'te tazminat davası açmıştır. Tazminat borcuna ilişkin temerrüt hangi tarihte gerçekleşmiştir?",
        {
            'A': '1 Eylül 2025',
            'B': 'Zararın tespit edildiği tarih',
            'C': 'İhtarın ulaştığı tarih',
            'D': '1 Mart 2025',
            'E': 'Kararın kesinleştiği tarih',
        },
        'D',
        "TBK m. 117/2'ye göre **haksız fiilde fiilin işlendiği tarihte** borçlu temerrüde düşmüş olur; temerrüt faizi bu tarihten işler.",
        '6098 sayılı TBK m. 117/2',
    ),
    # düzey 3
    '0034': patch(
        "Bağışlama vaadine, bağışlayanın ödemede gecikmesi hâlinde ihtar tarihinden itibaren temerrüt faizi işleyeceğine dair bir hüküm konulmuştur.\n\nTBK'ya göre bu hükümle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Bağışlanan paranın temerrüt faizi takip veya dava gününden işler',
            'B': 'Bu kurala aykırı anlaşma ceza koşulu hükümlerine tabidir',
            'C': 'Anlaşma geçerlidir ve m. 121 uygulanmaz',
            'D': 'Hâkimin ceza koşulunu indirme yetkisi uygulanabilir',
            'E': 'Anlaşma bağışlamanın tamamını geçersiz kılmaz',
        },
        'C',
        'TBK m. 121/1: bağışlanan paranın ödenmesinde temerrüt faizi icra takibi veya dava gününden işler. m. 121/2: buna aykırı olarak yapılan anlaşmalar ceza koşulu hükümlerine tabi olur; hâkimin indirim yetkisi gibi kurallar uygulanır ve bağışlama geçerliliğini korur.',
        '6098 sayılı TBK m. 121/2',
    ),
    # düzey 2
    '0035': patch(
        "Bir mağaza, yaz sezonu için sipariş ettiği mayoların sezon sonunda, eylül ayında teslim edilmek istendiğini görmüştür. Mayoların satış imkânı kalmamıştır.\n\nTBK'ya göre mağazanın haklarıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Mağaza mayoları kabul etmek ve bedelini ödemekle yükümlüdür',
            'B': 'Kural olarak alacaklı borçluya uygun bir süre verir',
            'C': 'İfa alacaklı için yararsız kalmışsa süre verilmesi gerekmez',
            'D': 'Sezon sonu teslim alacaklı için yararsız olabilir',
            'E': 'Mağaza süre vermeden seçimlik haklarını kullanabilir',
        },
        'A',
        "TBK m. 123-125: borçlunun temerrüdünde alacaklı kural olarak uygun bir süre verir; ancak m. 124/2'ye göre borçlunun temerrüdü sonucunda borcun ifası alacaklı için yararsız kalmışsa süre verilmesine gerek yoktur ve alacaklı seçimlik haklarını doğrudan kullanabilir.",
        '6098 sayılı TBK m. 124/2',
    ),
    # düzey 2
    '0036': patch(
        'Kiralanan bir tekne, kiracıya teslimden önce kiraya verenin kusuru olmaksızın fırtınada batmıştır; kiraya veren bir aylık kirayı peşin almıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Kiraya veren peşin aldığı kirayı iade eder',
            'B': 'Kiraya veren imkânsızlığı gecikmeksizin bildirmelidir',
            'C': 'İmkânsızlık kiraya verenin sorumluluğuna dayanmamaktadır',
            'D': 'Kiraya verenin teslim borcu sona erer',
            'E': 'Kiraya veren benzer bir tekne bulup teslim etmekle yükümlüdür',
        },
        'E',
        "TBK m. 136'ya göre borcun ifası **borçlunun sorumlu tutulamayacağı sebeplerle imkânsızlaşırsa borç sona erer**; borçlu aldığı karşı edimi sebepsiz zenginleşme hükümlerine göre iade eder ve imkânsızlığı gecikmeksizin bildirmekle yükümlüdür. Belirli teknenin yerine başka tekne verme borcu yoktur.",
        '6098 sayılı TBK m. 136',
    ),
    # düzey 3
    '0037': patch(
        "Konser salonu kiraya veren A, salonun kusursuz bir yangınla kullanılamaz hâle geldiğini bildiği hâlde organizatöre haber vermemiş; organizatör bilet basımı ve reklam için ek harcamalar yapmıştır. A'nın sorumluluğu hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Bildirmemeden doğan zararları gidermelidir',
            'B': 'İmkânsızlık kusursuz olduğundan sorumluluğu yoktur',
            'C': 'Sorumluluğu ancak ceza koşulu varsa doğar',
            'D': 'Organizatörün tüm kâr kaybını ödemekle yükümlüdür',
            'E': 'Aldığı kira bedelini iade eder, başka sorumluluğu yoktur',
        },
        'A',
        "TBK m. 136/3'e göre borçlu **ifanın imkânsızlaştığını alacaklıya gecikmeksizin bildirmez ve zararın artmaması için gerekli önlemleri almazsa, bundan doğan zararları gidermekle** yükümlüdür.",
        '6098 sayılı TBK m. 136/3',
    ),
    # düzey 3
    '0038': patch(
        'Satıcı, satılan antika vazoyu teslimden önce kendi dikkatsizliğiyle kırmıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Satıcı kusursuzluğunu ispat edemezse tazminat öder',
            'B': 'Satıcı imkânsızlıkla borcundan tazminatsız kurtulur',
            'C': 'Kusursuz imkânsızlık hükmü bu olayda uygulanmaz',
            'D': 'Satıcı alıcının zararını gidermekle yükümlüdür',
            'E': 'İmkânsızlık satıcının sorumlu olduğu bir sebepten doğmuştur',
        },
        'B',
        "TBK m. 136'daki borcun sona ermesi, imkânsızlığın **borçlunun sorumlu tutulamayacağı** sebeplerle doğmasına bağlıdır. Borçlunun kusuruyla imkânsızlaşan ifada m. 112 uyarınca borçlu **alacaklının zararını giderir**.",
        '6098 sayılı TBK m. 112, 136',
    ),
    # düzey 3
    '0039': patch(
        'Borçlu, ifayı olağanüstü biçimde güçleştiren duruma rağmen hiçbir çekince koymadan edimini tamamen ifa etmiş, sonra uyarlama istemiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Haklarını saklı tutarak ifa eden borçlu uyarlama isteyebilirdi',
            'B': 'Uyarlama için borçlunun henüz ifa etmemiş olması aranır',
            'C': 'Çekincesiz ifa uyarlama hakkını ortadan kaldırır',
            'D': 'Uyarlama, koşulları varsa hâkimden istenir',
            'E': 'Borçlu ifadan sonra da çekince koymadan uyarlama isteyebilir',
        },
        'E',
        "TBK m. 138'e göre uyarlama veya dönme hakkı, borçlunun **borcunu henüz ifa etmemiş veya ifanın aşırı ölçüde güçleşmesinden doğan haklarını saklı tutarak ifa etmiş** olmasına bağlıdır. Çekincesiz ifa hâlinde bu hak kullanılamaz.",
        '6098 sayılı TBK m. 138',
    ),
    # düzey 3
    '0040': patch(
        'Satış sözleşmesine, malın hasarının sözleşme tarihinden itibaren alıcıya ait olacağı kaydı konulmuştur. Mal teslimden önce, satıcının sorumlu tutulamayacağı bir sebeple yok olmuştur. Alıcının bedel ödeme borcu hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Satıcı benzer bir mal teslim etmekle yükümlüdür',
            'B': 'Satıcının borcu sona erdiğinden alıcı da bedel ödemekten kurtulur',
            'C': 'Alıcı bedeli ödemekle yükümlüdür',
            'D': 'Hasar kaydı kesin hükümsüzdür',
            'E': 'Alıcı bedelin yarısını öder',
        },
        'C',
        "TBK m. 136/2'ye göre imkânsızlıkla borçtan kurtulan borçlu karşı edimi isteme hakkını kaybeder; ancak **kanun veya sözleşmeyle borcun ifasından önce doğan hasarın alacaklıya yükletilmiş olduğu durumlar bu hükmün dışındadır**. Hasar alıcıya yüklendiğinden bedel borcu devam eder.",
        '6098 sayılı TBK m. 136/2',
    ),
    # düzey 3
    '0041': patch(
        'Alıcının temerrüde düşmesi üzerine toptancı, teslim edeceği ticari malları hâkim kararı almadan bir ardiyeye tevdi etmiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Ticari mallar hâkim kararı olmadan da ardiyeye tevdi edilebilir',
            'B': 'Tevdi ile toptancı borcundan kurtulabilir',
            'C': 'Ticari mal dışındaki şeylerde tevdi yerini ifa yerindeki hâkim belirler',
            'D': 'Tevdi yeri hâkimce belirlenmediğinden tevdi geçersizdir',
            'E': 'Hasar ve giderler alacaklıya aittir',
        },
        'D',
        "TBK m. 107'ye göre alacaklının temerrüdünde borçlu, **hasar ve giderleri alacaklıya ait olmak üzere** teslim edeceği şeyi tevdi ederek borcundan kurtulabilir; tevdi yerini ifa yerindeki hâkim belirler; ancak **ticari mallar hâkim kararı olmadan da bir ardiyeye tevdi edilebilir**.",
        '6098 sayılı TBK m. 107',
    ),
    # düzey 3
    '0042': patch(
        'Bir portre ressamı ile anlaşan müşteri, kararlaştırılan poz günlerine haklı bir sebep olmaksızın gelmemektedir. Ressamın hakları hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Portreyi tevdi ederek borcundan kurtulur',
            'B': 'Sözleşme sona ermiştir',
            'C': 'Portreyi açık artırmayla sattırır',
            'D': 'Ressam sözleşmeden dönebilir',
            'E': 'Müşterinin gelmesini beklemelidir',
        },
        'D',
        "TBK m. 110'a göre **borcun konusu bir şeyin teslimini gerektirmiyorsa**, alacaklının temerrüdü hâlinde borçlu, **borçlunun temerrüdüne ilişkin hükümlere göre sözleşmeden dönebilir**.",
        '6098 sayılı TBK m. 110',
    ),
    # düzey 2
    '0043': patch(
        'Ölen alacaklının mirasçıları arasında alacağın kime ait olduğu konusunda uyuşmazlık vardır; borçlu kusuru olmaksızın kime ödeme yapacağını belirleyememektedir. Borçlunun hakları hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Her mirasçıya ayrı ayrı tam ödeme yapmalıdır',
            'B': 'Mirasçılardan dilediğine ödeyerek borçtan kurtulur',
            'C': 'Borçlu tevdi veya dönme hakkını kullanabilir',
            'D': 'Borç mirasçılar arasındaki uyuşmazlık nedeniyle sona erer',
            'E': 'Uyuşmazlık bitene kadar temerrüt faizi öder',
        },
        'C',
        "TBK m. 111'e göre borçlunun kusuru olmaksızın **alacağın kime ait olduğunda veya alacaklının kimliğinde duraksama** sebebiyle borç ifa edilemezse borçlu, **alacaklının temerrüdünde olduğu gibi tevdi ya da sözleşmeden dönme** hakkını kullanabilir.",
        '6098 sayılı TBK m. 111',
    ),
    # düzey 2
    '0044': patch(
        'Alacaklı temerrüdü nedeniyle teslim edilemeyen ve piyasa fiyatı bulunmayan antika bir mobilyanın saklanması önemli bir gider gerektirmektedir. Borçlunun satma hakkına ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Satış yapılamaz; saklama giderlerine katlanır',
            'B': 'İhtar yapmadan dilediği fiyata satabilir',
            'C': 'Mobilyayı kendisi alıkoyarak bedelini ödemez',
            'D': 'İhtar ve hâkim izniyle açık artırmada sattırabilir',
            'E': 'Hâkim izni olmadan pazarlıkla satabilir',
        },
        'D',
        "TBK m. 108'e göre saklanması önemli gider gerektiren şeyi borçlu, **alacaklıya önceden ihtarda bulunması koşuluyla, hâkimin izniyle açık artırma yoluyla** sattırıp bedelini tevdi edebilir. Piyasa fiyatı olmadığından açık artırma ve ihtar koşulları aranır.",
        '6098 sayılı TBK m. 108',
    ),
    # düzey 3
    '0045': patch(
        "A, komşusu B'ye bahçesine iki metreden yüksek duvar örmemeyi taahhüt etmiş, ancak dört metrelik duvar örmüştür. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'B, aykırı durumun ortadan kaldırılmasını isteyebilir',
            'B': "B'nin bu durumda ancak tazminat isteme hakkı vardır",
            'C': 'A, aykırı davranışının doğurduğu zararı gidermekle yükümlüdür',
            'D': "A'nın yükümlülüğü bir yapmama borcudur",
            'E': "B, masrafı A'ya ait olmak üzere duvarı yıkmaya yetkili kılınmayı isteyebilir",
        },
        'B',
        "TBK m. 113/2-3'e göre **yapmama borcuna aykırı davranan borçlu** doğan zararı gidermekle yükümlüdür; alacaklı ayrıca **borca aykırı durumun ortadan kaldırılmasını** veya masrafı borçluya ait olmak üzere kendisinin yetkili kılınmasını isteyebilir.",
        '6098 sayılı TBK m. 113/2-3',
    ),
    # düzey 3
    '0046': patch(
        'Bir iş sözleşmesine, işverenin işçiye karşı sözleşmeden doğan hiçbir borcundan sorumlu olmayacağına dair bir hüküm konulmuştur. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'İşveren borca aykırılıktan doğan zarardan sorumlu kalır',
            'B': 'Hüküm işçi tarafından imzalandığı için geçerlidir',
            'C': 'Hüküm hizmet sözleşmesinden doğan borçlarla ilgilidir',
            'D': 'Önceden yapılan bu anlaşma kesin hükümsüzdür',
            'E': 'Hükümsüzlük kusurun derecesine bağlı değildir',
        },
        'B',
        "TBK m. 115/2'ye göre **borçlunun alacaklı ile hizmet sözleşmesinden kaynaklanan herhangi bir borç sebebiyle sorumlu olmayacağına ilişkin önceden yaptığı her türlü anlaşma kesin olarak hükümsüzdür**; kusurun derecesine bakılmaz.",
        '6098 sayılı TBK m. 115/2',
    ),
    # düzey 3
    '0047': patch(
        'Yardımcı kişilerin fiillerinden sorumluluğa ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Borçlu, yardımcısının işi yürütürken verdiği zarardan sorumludur\n\nII. Bu sorumluluk önceden yapılan bir anlaşmayla hiçbir durumda kaldırılamaz\n\nIII. İzinle yürütülen uzmanlık mesleklerinde bu sorumluluk anlaşmayla kaldırılabilir',
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'I ve II',
            'D': 'Yalnız II',
            'E': 'I, II ve III',
        },
        'A',
        "TBK m. 116/1'e göre borçlu yardımcısının işi yürütürken verdiği zarardan sorumludur (I). m. 116/2'ye göre bu sorumluluk **önceden yapılan bir anlaşmayla tamamen veya kısmen kaldırılabilir** (II yanlış); ancak m. 116/3'e göre **izinle yürütülen uzmanlık mesleklerinde** bu anlaşma kesin hükümsüzdür (III yanlış).",
        '6098 sayılı TBK m. 116',
    ),
    # düzey 2
    '0048': patch(
        "Vadesi belirlenmemiş ve muaccel bir para borcu için alacaklı, borçluya 5 Mayıs'ta tebliğ edilen bir ihtarname göndermiştir. Borçlu hangi tarihte temerrüde düşer?",
        {
            'A': 'Borcun doğduğu tarihte',
            'B': '5 Mayıs',
            'C': 'Dava açıldığı tarihte',
            'D': 'İhtarın gönderildiği tarihte',
            'E': '5 Haziran',
        },
        'B',
        "TBK m. 117/1'e göre **muaccel bir borcun borçlusu, alacaklının ihtarıyla temerrüde düşer**; ihtar borçluya ulaştığında hüküm doğurur.",
        '6098 sayılı TBK m. 117/1',
    ),
    # düzey 2
    '0049': patch(
        'Teslim tarihinde makineyi teslim etmeyen satıcı temerrüde düşmüş; alıcı üretim yapamadığı için zarara uğramıştır. Satıcı temerrüde düşmesinde kusurunun olmadığını ispat edememiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Gecikme tazminatı ancak sözleşmede ceza koşulu varsa istenebilir',
            'B': 'Alıcı satıcının kusurunu ispat etmedikçe tazminat alamaz',
            'C': 'Satıcı temerrüt faiziyle sınırlı sorumludur',
            'D': 'Alıcının tek hakkı sözleşmeden dönmektir',
            'E': 'Satıcı gecikmeden doğan zararı gidermekle yükümlüdür',
        },
        'E',
        "TBK m. 118'e göre **temerrüde düşen borçlu, temerrüde düşmekte kusuru olmadığını ispat etmedikçe**, borcun geç ifasından dolayı alacaklının uğradığı zararı gidermekle yükümlüdür.",
        '6098 sayılı TBK m. 118',
    ),
    # düzey 3
    '0050': patch(
        'Yabancı para borcunu geç ödeyen borçlu temerrüde düşmüştür. Temerrüt faizi 10.000 ₺ olarak hesaplanmış, alacaklının kur farkı nedeniyle uğradığı gerçek zarar ise 25.000 ₺ olarak ispat edilmiştir. Borçlu kusursuzluğunu ispat edememiştir. Alacaklı temerrüt faizine ek olarak kaç ₺ aşkın zarar isteyebilir?',
        {
            'A': '10.000',
            'B': '25.000',
            'C': '0',
            'D': '15.000',
            'E': '35.000',
        },
        'D',
        "TBK m. 122'ye göre alacaklı **temerrüt faizini aşan bir zarara** uğramışsa borçlu, **hiçbir kusuru bulunmadığını ispat etmedikçe** bu zararı da giderir: 25.000 − 10.000 = **15.000 ₺**.",
        '6098 sayılı TBK m. 122',
    ),
    # düzey 3
    '0051': patch(
        'Satıcının teslimde temerrüde düşmesi üzerine alıcı, verdiği ek süre de sonuçsuz kalınca, ifadan vazgeçtiğini hemen bildirip malı başka yerden daha pahalıya almış ve aradaki farkı istemiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Alıcı dilerse bunun yerine sözleşmeden de dönebilirdi',
            'B': 'Alıcı ifadan vazgeçtiği için artık bir tazminat isteyemez',
            'C': 'Alıcı dilerseydi ifa ve gecikme tazminatı da isteyebilirdi',
            'D': 'Alıcı, ifa edilmemeden doğan zararının giderilmesini isteyebilir',
            'E': 'Alıcı ifadan ve gecikme tazminatından vazgeçtiğini hemen bildirmiştir',
        },
        'B',
        "TBK m. 125'e göre temerrüt ve süre sonuçsuz kalınca alacaklı **ifa ve gecikme tazminatı** isteyebilir; ya da **ifadan vazgeçtiğini hemen bildirerek ifa edilmemeden doğan zararın (olumlu zarar) giderilmesini** isteyebilir veya sözleşmeden dönebilir.",
        '6098 sayılı TBK m. 125',
    ),
    # düzey 2
    '0052': patch(
        'Bir apartman ile asansör bakım şirketi arasındaki iki yıllık bakım sözleşmesinin sekizinci ayında şirket, bakımları uzun süre aksatarak temerrüde düşmüştür. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Yönetim sözleşmeyi feshedebilir',
            'B': 'Apartman yönetimi sözleşmeden geriye etkili olarak dönmelidir',
            'C': 'Yönetim erken sona ermeden doğan zararını isteyebilir',
            'D': 'Sözleşme sürekli edimli bir sözleşmedir',
            'E': 'Sözleşmenin ifasına başlanmıştır',
        },
        'B',
        "TBK m. 126'ya göre **ifasına başlanmış sürekli edimli sözleşmelerde** borçlunun temerrüdü hâlinde alacaklı, ifa ve gecikme tazminatı isteyebileceği gibi **sözleşmeyi feshederek**, erken sona ermeden doğan zararının giderilmesini de isteyebilir.",
        '6098 sayılı TBK m. 126',
    ),
    # düzey 2
    '0053': patch(
        "Vadesi 1 Eylül olarak kararlaştırılan bir borç için alacaklı, 15 Ağustos'ta borçluya ihtarname göndererek hemen ödeme istemiştir. Borçlu 20 Ağustos'ta ödeme yapmamıştır. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': "İhtarla borçlu 15 Ağustos'ta temerrüde düşer",
            'B': 'Borçlu ihtarın ulaşmasıyla temerrüde düşer ve faiz öder',
            'C': "Borçlu 20 Ağustos'ta temerrüde düşer",
            'D': "20 Ağustos'ta temerrüt oluşmaz",
            'E': 'Vade ihtarla öne alınmış olur',
        },
        'D',
        "TBK m. 117/1'e göre temerrüt için borcun **muaccel** olması ve alacaklının ihtarı gerekir. Vadesi gelmemiş borç için yapılan ihtar temerrüt doğurmaz; kesin vadeli borçta borçlu vade gününün geçmesiyle temerrüde düşer.",
        '6098 sayılı TBK m. 117/1',
    ),
    # düzey 3
    '0054': patch(
        "Teslim gününde ağır bir hastalık nedeniyle hastaneye kaldırılan ve bu nedenle teslimi geciktiren satıcının deposundaki mallar, gecikme sırasında sel sonucu zarar görmüştür. Satıcı, temerrüde düşmekte kusuru olmadığını ispat etmiştir.\n\nTBK'ya göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Temerrütteki borçlu kusursuz olsa da beklenmedik hâlden sorumludur',
            'B': 'Temerrütteki borçlu kural olarak beklenmedik hâlden de sorumludur',
            'C': 'Temerrüde düşmekte kusursuzluğunu ispat eden borçlu kurtulur',
            'D': 'Zamanında ifada da zararın doğacağını ispat eden borçlu kurtulur',
            'E': 'Bu olayda satıcı beklenmedik hâlden doğan zarardan sorumlu değildir',
        },
        'A',
        'TBK m. 119: temerrüde düşen borçlu beklenmedik hâlden doğan zararlardan da sorumludur; ancak temerrüde düşmekte kusuru olmadığını veya zamanında ifa etseydi de beklenmedik hâlin zarar vereceğini ispat ederek bu sorumluluktan kurtulabilir.',
        '6098 sayılı TBK m. 119',
    ),
    # düzey 2
    '0055': patch(
        "Temerrüt faizini aşan zararın miktarı, görülmekte olan alacak davasında bilirkişi incelemesiyle belirlenebilmektedir. Davacı bu zararın da hüküm altına alınmasını istemiştir.\n\nTBK'ya göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Temerrüt faizini aşan zarar istenebilir',
            'B': 'Hâkim aşkın zararı temerrüt faiziyle sınırlar',
            'C': 'Aşkın zarar görülmekte olan davada belirlenebiliyorsa hükme bağlanır',
            'D': 'Hüküm davacının istemi üzerine verilir',
            'E': 'Aşkın zarar için ayrı dava açılması beklenmez',
        },
        'B',
        'TBK m. 122/2: temerrüt faizini aşan zarar miktarı görülmekte olan davada belirlenebiliyorsa, davacının istemi üzerine hâkim, esas hakkında karar verirken bu zararın miktarına da hükmeder.',
        '6098 sayılı TBK m. 122/2',
    ),
    # düzey 3
    '0056': patch(
        "Alıcı, 100.000 ₺'ye satın aldığı ve satıcının temerrüdü nedeniyle teslim almadığı malı, ifadan vazgeçtiğini hemen bildirerek başka bir satıcıdan 130.000 ₺'ye almıştır. Satıcı kusursuzluğunu ispat edememiştir. Alıcı olumlu zarar olarak kaç ₺ isteyebilir?",
        {
            'A': '230.000',
            'B': '0',
            'C': '100.000',
            'D': '130.000',
            'E': '30.000',
        },
        'E',
        "TBK m. 125/2'ye göre alacaklı ifadan vazgeçtiğini hemen bildirerek **borcun ifa edilmemesinden doğan zararın (olumlu zarar)** giderilmesini isteyebilir; bu, sözleşme ifa edilseydi olacağı durumla fiili durum arasındaki farktır: 130.000 − 100.000 = **30.000 ₺**.",
        '6098 sayılı TBK m. 125/2',
    ),
    # düzey 3
    '0057': patch(
        "100 ton mal satışında, satıcının sorumlu olmadığı bir sebeple 40 ton yok olmuştur. Toplam bedel 500.000 ₺'dir ve alıcı kısmi ifaya razı olmuştur. Alıcının ödemesi gereken bedel kaç ₺'dir?",
        {
            'A': '200.000',
            'B': '500.000',
            'C': '0',
            'D': '250.000',
            'E': '300.000',
        },
        'E',
        "TBK m. 137/2'ye göre karşılıklı sözleşmelerde bir tarafın borcu kısmen imkânsızlaşır ve **alacaklı kısmi ifaya razı olursa, karşı edim de o oranda ifa edilir**: 60 ton için 500.000 × 60/100 = **300.000 ₺**.",
        '6098 sayılı TBK m. 137',
    ),
    # düzey 3
    '0058': patch(
        'Sözleşmenin yapıldığı sırada öngörülemeyen olağanüstü bir ekonomik kriz, borçludan kaynaklanmayan bir sebeple ham madde fiyatlarını on katına çıkarmış ve ifayı istemeyi dürüstlük kurallarına aykırı hâle getirmiştir. Borçlu henüz ifada bulunmamıştır. Borçlunun hakları hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ancak alacaklının rızasıyla fiyat artırabilir',
            'B': 'Hâkimden uyarlama, bu olmazsa dönme ister',
            'C': 'Doğrudan sözleşmeden dönmekle yükümlüdür',
            'D': 'Borcundan tazminatsız olarak kurtulur',
            'E': 'Aşırı ifa güçlüğü ifa tamamlandıktan sonra ileri sürülebilir',
        },
        'B',
        "TBK m. 138'e göre öngörülmeyen olağanüstü durum borçludan kaynaklanmayan sebeple ortaya çıkar ve ifayı istemeyi dürüstlük kurallarına aykırı kılarsa, **henüz ifa etmemiş** borçlu **hâkimden sözleşmenin yeni koşullara uyarlanmasını**, bu mümkün değilse **sözleşmeden dönmeyi** isteyebilir.",
        '6098 sayılı TBK m. 138',
    ),
    # düzey 2
    '0059': patch(
        'İfa imkânsızlığına ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. İmkânsızlığı bildirmeyen borçlu bundan doğan zarardan sorumlu olmaz\n\nII. Borçlunun sorumlu tutulamayacağı imkânsızlıkta borç sona erer\n\nIII. Kısmi imkânsızlıkta borçlu kural olarak imkânsızlaşan kısımdan kurtulur',
        {
            'A': 'Yalnız III',
            'B': 'I, II ve III',
            'C': 'Yalnız II',
            'D': 'II ve III',
            'E': 'I ve II',
        },
        'D',
        "TBK m. 136/1'e göre kusursuz imkânsızlıkta **borç sona erer** (II); m. 137/1'e göre kısmi imkânsızlıkta borçlu kural olarak **imkânsızlaşan kısımdan kurtulur** (III). m. 136/3'e göre imkânsızlığı bildirmeyen borçlu bundan doğan zararlardan **sorumludur** (I yanlış).",
        '6098 sayılı TBK m. 136, 137',
    ),
    # düzey 2
    '0060': patch(
        'Beş yıllık bir enerji tedarik sözleşmesinin ikinci yılında öngörülemeyen olağanüstü bir kriz, tedarikçinin maliyetlerini dürüstlük kurallarına aykırı düşecek ölçüde artırmıştır. Uyarlama mümkün olmamıştır. Tedarikçinin hakkı hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Dönme yerine kural olarak fesih hakkını kullanır',
            'B': 'Sözleşmeden geriye etkili olarak dönmelidir',
            'C': 'Fiyatı tek taraflı olarak artırabilir',
            'D': 'Sözleşme süresinin sonuna kadar ifaya devam etmelidir',
            'E': 'Krizden kaynaklanan zararın tamamını alıcıya yükler',
        },
        'A',
        "TBK m. 138/1'e göre aşırı ifa güçlüğünde borçlu uyarlama, bu mümkün değilse dönme hakkına sahiptir; **sürekli edimli sözleşmelerde borçlu, kural olarak dönme hakkının yerine fesih hakkını** kullanır.",
        '6098 sayılı TBK m. 138',
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
    print(f"1 paket / {len(PATCHES)} soru ('Temerrut ve Tazminat' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
