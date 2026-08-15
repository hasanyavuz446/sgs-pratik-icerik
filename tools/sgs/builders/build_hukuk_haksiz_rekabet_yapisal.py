#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Haksiz Rekabet — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

    olcut                gercek   once   sonra
    medyan kok              257    137     240
    olumsuz kok           %41,5     %0     %43
    onculu                %14,3    %10     %11
    kor ogrenci            <=%30    %20     %23
    boy (uzun/kisa)           —  14/14   12/13

Eski koklerin tamami '... bakimindan asagidakilerden hangisi dogrudur?'
kalibindaydi; tanim ezberi olcuyordu. Yeni kokler somut bir ticari davranis
verip hangi haksiz rekabet haline girdigini, hangi davanin acilabilecegini
ve kimin dava hakki bulundugunu sorduruyor.

Ayirt edici noktalar uzerinden yazildi: rekabet iliskisi SART DEGIL (md. 54)
· kusur yalniz tazminat davasinda aranir, tespit/men/duzeltmede aranmaz
(md. 56) · zarar men davasinda aranmaz, tehlike yeterlidir · musteriler ve
birlikler dava acabilir ama birlikler TAZMINAT isteyemez (md. 56/2-3) ·
zamanasimi 1 yil / 3 yil, daha uzun ceza zamanasimi hukuk davasinda da
uygulanir (md. 60) · basin-yayinda dava ONCELIKLE yazi sahibi/ilan verene
(md. 58) · istihdam edenin sorumlulugu (md. 57) · ceza davasi sikayete bagli
(md. 62) · tuzel kisi adina hareket edenler cezalandirilir (md. 63) ·
haksiz rekabet davasi MUTLAK TICARI DAVA (md. 4/1-a, 5).

BOY: uc tur gerekti. Ilk uretimde audit 'en uzunu sec' ile kor %30 verdi
(hedefin tam sinirinda ve tabandan kotu). 19 celdirici genisletilince dogru
sik HIC en uzun kalmadi (0/60) — bu da 'en uzunu asla secme' kuralidir.
Kucuk farkli 12 genisletme geri alinarak dagilim 12 uzun / 13 kisa yapildi.

Onculu sorularda 'I ve II' (7 karakter) her secici kumesinin en kisasidir;
dogru secici Yalniz II / Yalniz III / I ve III / II ve III arasinda
dagitildi. Iki oncullu soruda cevap anahtari ile cozum metni celisiyordu;
oncüller yeniden kurgulandi ve yedisi de tek tek dogrulandi. Audit ayrica
iki tekrar yakaladi (ayni kural pakette iki kez soruluyordu); 0025 paye/odul
ve tehlike gizleme, 0034 gorevli mahkeme sorusuyla degistirildi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: TTK md. 4/1-a, 5, 54-63 · ozellikle md. 54, 55/1-a-f, 56, 57, 58, 59, 60, 61, 62, 63 · TBK md. 58 (manevi tazminat).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/ticaret_hukuku/haksiz_rekabet.json"
STYLE_REF = "SGS Hukuk (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "hakrek-gen-"


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
        'Bir yazılım firması, kendisiyle hiçbir rekabet ilişkisi bulunmayan bir gıda üreticisinin müşteri ağını ele geçirmek amacıyla bu üreticinin ürünleri hakkında yanıltıcı açıklamalar yapmıştır. Üretici, taraflar rakip olmadığı için haksız rekabet hükümlerinin uygulanamayacağını duymuştur. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Haksız rekabet hükümleri yalnızca aynı piyasada faaliyet gösteren rakipler arasında uygulanır',
            'B': 'Rekabet ilişkisi bulunmasa da hükümlerin uygulanabilmesi somut zararın ispatına bağlıdır',
            'C': 'Rekabet ilişkisinin bulunmadığı hâllerde yalnızca ceza hükümleri uygulama alanı bulur',
            'D': 'Haksız rekabet hükümlerinin uygulanması için taraflar arasında rekabet ilişkisi aranmaz',
            'E': 'Rekabet ilişkisi bulunmayan hâllerde ancak genel haksız fiil hükümlerine başvurulabilir',
        },
        'D',
        'TTK md. 54 uyarınca haksız rekabete ilişkin hükümlerin amacı bütün katılanların menfaatine dürüst ve bozulmamış rekabeti sağlamaktır; korumadan yararlanmak rakip olma koşuluna bağlanmamıştır.',
    ),
    # düzey 3
    '0002': patch(
        'Bir işletme, rakibinin ürünleri hakkında gerçeğe aykırı açıklamalar yayımlamış; ancak açıklamaların yanlış olduğunu bilmediğini, bu nedenle kusurunun bulunmadığını ileri sürmüştür. Rakip işletme davranışın durdurulmasını ve doğan zararın giderilmesini istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Haksız rekabete dayanan bütün davalarda failin kusurlu olması koşulu aranmaktadır',
            'B': 'Men davasında kusur aranmaz, buna karşılık tazminat istenebilmesi kusura bağlıdır',
            'C': 'Kusur yalnızca men davasında aranır, tazminat davasında kusur koşulu öngörülmemiştir',
            'D': 'Haksız rekabete dayanan davaların hiçbirinde failin kusurlu olması koşulu aranmaz',
            'E': 'Kusurun bulunmadığı hâllerde yalnızca haksız rekabetin tespiti istenebilir, men istenemez',
        },
        'B',
        'TTK md. 56 uyarınca tespit, men ve düzeltme davalarında kusur aranmaz; maddi ve manevi tazminat istemleri ise failin kusuruna bağlıdır.',
    ),
    # düzey 2
    '0003': patch(
        'Bir işletme, rakibinin dürüstlük kuralına aykırı reklamları nedeniyle müşteri kaybetme tehlikesiyle karşılaşmış, ancak henüz somut bir zarara uğramamıştır. İşletme bu aşamada dava açıp açamayacağını sormaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Dava açılabilmesi için somut bir zararın gerçekleşmiş ve miktarının belirlenmiş olması gerekir',
            'B': 'Zarar tehlikesiyle karşılaşan kişi de haksız rekabetin önlenmesini dava edebilir',
            'C': 'Zarar tehlikesi yalnızca ihtiyati tedbir istemine dayanak oluşturur, dava hakkı vermez',
            'D': 'Zarar doğmamışsa yalnızca tespit davası açılabilir, önleme davası açılamaz',
            'E': 'Zarar doğmadan açılan davalar hukuki yarar yokluğundan usulden reddedilmektedir',
        },
        'B',
        'TTK md. 56/1 uyarınca haksız rekabet sebebiyle müşterileri, kredisi, mesleki itibarı veya ticari faaliyetleri zarar gören ya da böyle bir tehlikeyle karşılaşan kimse dava açabilir.',
    ),
    # düzey 2
    '0004': patch(
        'Bir mesleki birlik, üyelerinin ekonomik menfaatlerini korumak amacıyla haksız rekabette bulunan bir işletmeye karşı dava açmak istemektedir. Birlik, hem fiilin durdurulmasını hem de üyelerinin uğradığı zararın tazminini talep etmeyi düşünmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Birliklerin haksız rekabet nedeniyle dava açma ehliyeti kanunda tanınmamıştır',
            'B': 'Birlik yalnızca tespit davası açabilir; men ve düzeltme istemleri üyelere aittir',
            'C': 'Birlik, üyelerinin menfaatini temsil ettiğinden tazminat dâhil bütün davaları açabilir',
            'D': 'Birliğin dava açabilmesi zarara uğrayan üyelerinin yazılı muvafakatine bağlı tutulmuştur',
            'E': 'Birlik tespit, men ve düzeltme davası açabilir, ancak tazminat isteyemez',
        },
        'E',
        'TTK md. 56/2-3 uyarınca ekonomik menfaatleri zarar gören müşteriler ile mesleki ve ekonomik birlikler tespit, men ve eski hâle getirme davalarını açabilir; tazminat davası açma hakkı bunlara tanınmamıştır.',
    ),
    # düzey 3
    '0005': patch(
        'Bir işletme sahibi, rakibinin haksız rekabet oluşturan davranışını iki yıl önce öğrenmiş, ancak dava açmamıştır. Fiil bir buçuk yıl önce gerçekleşmiştir. İşletme sahibi şimdi dava açmak istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Zamanaşımı süresi öğrenmeden itibaren iki yıl olduğundan dava süresinde sayılır',
            'B': 'Öğrenmeden itibaren bir yıllık süre dolduğundan dava hakkı zamanaşımına uğramıştır',
            'C': 'Zamanaşımı yalnızca tazminat istemleri için işler, men davası süreye bağlı değildir',
            'D': 'Haksız rekabet davaları için kanunda herhangi bir zamanaşımı süresi öngörülmemiştir',
            'E': 'Fiilin üzerinden üç yıl geçmediğinden dava hakkı henüz zamanaşımına uğramamıştır',
        },
        'B',
        'TTK md. 60 uyarınca haksız rekabetten doğan davalar, davaya hakkı olanın öğrendiği tarihten itibaren bir yıl ve her hâlde doğumundan itibaren üç yıl geçmekle zamanaşımına uğrar.',
    ),
    # düzey 2
    '0006': patch(
        'Bir işletme, rakibinin haksız rekabet oluşturan davranışı nedeniyle açtığı davayı kazanmıştır. İşletme, kararın kamuoyuna duyurulmasını istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İlan istemi yalnızca ceza mahkemesince verilen mahkûmiyet kararları bakımından ileri sürülebilir',
            'B': 'Mahkeme, kazanan tarafın istemiyle masrafı diğer tarafa ait olmak üzere ilana karar verebilir',
            'C': 'Kararın ilanına ancak davalının bu yönde açık rızası bulunması hâlinde karar verilebilir',
            'D': 'Kararın ilan masrafları kural olarak ilanı isteyen kazanan tarafa yükletilmektedir',
            'E': 'Mahkeme kararlarının ilanı kişilik haklarını zedelediğinden bu yönde istemde bulunulamaz',
        },
        'B',
        'TTK md. 59 uyarınca mahkeme, davayı kazanan tarafın istemiyle masrafı diğer tarafa ait olmak üzere kararın kesinleşmesinden sonra ilan edilmesine karar verebilir.',
    ),
    # düzey 3
    '0007': patch(
        'Bir işletme, tanıtım broşürlerinde rakibinin ürünlerinin sağlığa zararlı olduğunu, kendi ürünlerinin ise piyasadaki tek güvenilir ürün olduğunu belirtmiştir. İki iddia da gerçeğe aykırıdır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Rakibi kötüleme ve gerçek dışı üstünlük iddiası ayrı ayrı haksız rekabet hâlleridir',
            'B': 'Yalnızca rakibin kötülenmesi haksız rekabet sayılır, üstünlük iddiası ticari övgü kabul edilir',
            'C': 'Bu davranışlar ancak rakip işletmenin somut zararı ispat etmesi hâlinde haksız rekabet sayılır',
            'D': 'Üstünlük iddiası haksız rekabet sayılır, ancak rakibin ürünleri hakkındaki beyan bunun dışındadır',
            'E': 'Reklam metinlerinde yer alan abartılı ifadeler haksız rekabet hükümlerinin dışında bırakılmıştır',
        },
        'A',
        'TTK md. 55/1-a uyarınca başkalarını veya mallarını gerçek dışı beyanlarla kötülemek ve kendini gerçek dışı beyanlarla üstün duruma getirmek ayrı ayrı haksız rekabet hâlleridir.',
    ),
    # düzey 3
    '0008': patch(
        'Bir işletme, tanınmış bir markanın ambalaj biçimini, renk düzenini ve raf görünümünü tüketicide aynı işletmeye ait olduğu izlenimi doğuracak biçimde taklit etmiştir. Marka tescili bakımından bir ihlal saptanmamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Karıştırılmaya yol açan önlemler almak başlı başına haksız rekabet hâli oluşturur',
            'B': 'Karıştırılma iddiası ancak tüketicilerin fiilen yanıldığının anketle ispatına bağlıdır',
            'C': 'Bu davranış yalnızca tescilli tasarım bulunması hâlinde haksız rekabet olarak değerlendirilir',
            'D': 'Marka tescilinden doğan hak ihlal edilmediğinden davranış hukuka uygun sayılır',
            'E': 'Ambalaj ve renk düzeni fikri mülkiyet korumasına girmediğinden dava açılamaz',
        },
        'A',
        'TTK md. 55/1-a-4 uyarınca başkasının malları, iş ürünleri, faaliyetleri veya işleri ile karıştırılmaya yol açan önlemler almak haksız rekabet hâlidir; sınai hak ihlalinden bağımsızdır.',
    ),
    # düzey 3
    '0009': patch(
        'Bir işletme, rakibinin uzun süredir çalıştığı tedarikçilere başvurarak, sözleşmelerini erken sona erdirmeleri hâlinde kendilerine ek ödeme yapacağını bildirmiş ve bu yolla rakibin tedarik zincirini bozmuştur. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bu davranış ancak tedarikçilere ödenen tutarın piyasa değerini aşması hâlinde haksız sayılır',
            'B': 'Sözleşme serbestisi gereği tedarikçilerin sözleşmelerini sona erdirmeleri hukuka uygundur',
            'C': 'Bu davranış yalnızca tedarikçilerle işletme arasındaki sözleşme ilişkisini ilgilendirir',
            'D': 'Üçüncü kişileri sözleşmeye aykırı davranmaya yöneltmek haksız rekabet hâlidir',
            'E': 'Haksız rekabetin doğması için rakibin tedarik zincirinin tümüyle durmuş olması gerekir',
        },
        'D',
        'TTK md. 55/1-b uyarınca müşterilerle kendisinin sözleşme yapabilmesi için onları başkalarıyla yapmış oldukları sözleşmelere aykırı davranmaya yöneltmek haksız rekabet hâlidir.',
    ),
    # düzey 3
    '0010': patch(
        'Bir işletme, rakibinin eski çalışanına para vererek üretim yöntemine ilişkin gizli bilgileri elde etmiş ve bu bilgileri kendi üretiminde kullanmıştır. Çalışanın iş sözleşmesi sona ermiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bilgiyi kullanan işletme değil yalnızca sırrı açıklayan çalışan sorumlu tutulabilir',
            'B': 'İş sözleşmesi sona erdiğinden çalışanın sır saklama yükümlülüğü tümüyle ortadan kalkar',
            'C': 'Üretim sırlarını hukuka aykırı yolla ele geçirip değerlendirmek haksız rekabet hâlidir',
            'D': 'Üretim sırlarının korunması yalnızca patentle korunan bilgiler bakımından söz konusu olur',
            'E': 'Bu davranışın haksız rekabet sayılması bilginin ekonomik değerinin bilirkişice tespitine bağlıdır',
        },
        'C',
        'TTK md. 55/1-d uyarınca üretim ve iş sırlarını hukuka aykırı biçimde ele geçirmek ve değerlendirmek haksız rekabet hâlidir; işveren de sırrı kullanmakla sorumlu olur.',
    ),
    # düzey 2
    '0011': patch(
        'Bir işletme, kendisine güvenilerek verilen bir teklif ve maliyet hesabından yararlanarak aynı işi başka bir müşteriye sunmuştur. Belgeler işletmeye ticari görüşme sırasında teslim edilmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Teklif ve hesaplar fikri mülkiyet korumasına girmediğinden bunlardan yararlanılabilir',
            'B': 'Belgeler kendisine rızayla verildiğinden bunlardan yararlanmak hukuka uygun sayılır',
            'C': 'Bu davranış ancak belgelerde gizlilik kaydı bulunması hâlinde haksız rekabet oluşturur',
            'D': 'Kendisine emanet edilen iş ürünlerinden yetkisiz yararlanmak haksız rekabet hâlidir',
            'E': 'İş ürünlerinden yararlanma yalnızca teknik çoğaltma yöntemi kullanılmışsa haksız sayılır',
        },
        'D',
        'TTK md. 55/1-c uyarınca kendisine emanet edilen teklif, hesap veya plan gibi iş ürünlerinden yetkisiz yararlanmak haksız rekabet hâlidir.',
    ),
    # düzey 3
    '0012': patch(
        'Bir işletme, satış sözleşmelerinde müşteri aleyhine ağır dengesizlik yaratan ve dürüstlük kuralına aykırı genel işlem şartları kullanmaktadır. Şartlar önceden hazırlanmış ve tek yanlı olarak sözleşmelere konulmuştur. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bu şartlar yalnızca tüketici işlemlerinde denetlenebilir, ticari işlemlerde denetlenemez',
            'B': 'Genel işlem şartları yalnızca sözleşme hukuku kapsamında denetlenir, haksız rekabet sayılmaz',
            'C': 'Dürüstlük kuralına aykırı işlem şartları kullanmak haksız rekabet hâli sayılır',
            'D': 'Sözleşme serbestisi gereği taraflarca kabul edilen şartlar haksız rekabet oluşturmaz',
            'E': 'İşlem şartlarının haksız rekabet sayılması ancak rakiplerin zarara uğramasına bağlıdır',
        },
        'C',
        'TTK md. 55/1-f uyarınca dürüstlük kuralına aykırı işlem şartları kullanmak haksız rekabet hâlleri arasında sayılmıştır.',
    ),
    # düzey 3
    '0013': patch(
        'Bir işletme, mesleki teamüle ve kanuna göre rakiplerine de yüklenen iş şartlarına uymayarak maliyetlerini düşürmüş ve bu yolla rakiplerinin altında fiyat vermiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Mesleki teamüller bağlayıcı olmadığından bunlara uymamak hukuka aykırılık oluşturmaz',
            'B': 'Fiyat belirleme serbestisi gereği düşük fiyat uygulaması haksız rekabet sayılmaz',
            'C': 'İş şartlarına uymama ancak rakiplerin bundan somut zarar gördüğünü ispat etmesiyle haksız sayılır',
            'D': 'Rakiplere de yüklenen iş şartlarına uymamak haksız rekabet hâli oluşturur',
            'E': 'Bu davranış yalnızca ilgili mevzuattaki idari yaptırımı gerektirir, özel hukuk sonucu doğurmaz',
        },
        'D',
        'TTK md. 55/1-e uyarınca kanun veya sözleşmeyle rakiplere de yüklenmiş olan ya da mesleki teamüle aykırı iş şartlarına uymamak haksız rekabet hâlidir.',
    ),
    # düzey 2
    '0014': patch(
        'Bir işletme, taksitle satış sözleşmelerinde toplam fiyatı, peşin fiyatı ve taksit koşullarını açıkça belirtmeksizin ilan vermiş, tüketiciler ödeyecekleri toplam tutarı öğrenememiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Taksitli satışlarda zorunlu bilgilerin gizlenmesi haksız rekabet hâli sayılır',
            'B': 'Bilgilerin sözleşme kurulurken verilmesi yeterli olduğundan ilanda gösterilmesi gerekmez',
            'C': 'Bu davranış yalnızca tüketicinin sözleşmeden dönmesine olanak veren bir eksikliktir',
            'D': 'Fiyat bilgilerinin ilanda yer alması yalnızca reklam mevzuatı bakımından sonuç doğurur',
            'E': 'Taksitli satış ilanlarında hangi bilgilerin verileceği işletmenin takdirine bırakılmıştır',
        },
        'A',
        'TTK md. 55/1-a uyarınca taksitle satım sözleşmelerinde kanunen belirtilmesi gereken bilgileri açıklamamak dürüstlük kuralına aykırı reklam ve satış yöntemleri arasındadır.',
    ),
    # düzey 3
    '0015': patch(
        'Bir işletme, rakibinin üretim planlarını teknik bir çoğaltma yöntemiyle kopyalayarak devralmış ve kendi üretiminde doğrudan kullanmıştır. Planlar rakibin uzun süreli çalışmasının ürünüdür. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Fikri mülkiyet tescili bulunmayan iş ürünleri serbestçe çoğaltılıp kullanılabilir',
            'B': 'Teknik çoğaltma yöntemiyle elde edilen bilgilerin kullanılması yalnızca ceza hükümlerine tabidir',
            'C': 'İş ürünlerinin devralınması ancak rakibin pazar payını yitirmesiyle haksız rekabet oluşturur',
            'D': 'Bu davranış ancak kopyalanan planların ticari sır olarak nitelendirilmesi hâlinde haksız sayılır',
            'E': 'İş ürünlerini teknik çoğaltma yöntemiyle devralıp yararlanmak haksız rekabet hâlidir',
        },
        'E',
        'TTK md. 55/1-c-3 uyarınca başkasının iş ürünlerini teknik çoğaltma yöntemleriyle devralıp onlardan yararlanmak haksız rekabet hâlidir.',
    ),
    # düzey 3
    '0016': patch(
        'Bir işletme, rakibinin ürünlerini gerçeğe aykırı biçimde kötüleyen bir reklam kampanyası yürütmüş; ayrıca ürünlerini piyasadaki tek güvenilir ürün olarak tanıtmıştır. Rakip işletme hukuki yollara başvurmayı düşünmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Rakip işletme, davranışın önlenmesini kusur aranmaksızın dava edebilir',
            'B': 'Başkalarını gerçek dışı beyanlarla kötülemek haksız rekabet hâli sayılır',
            'C': 'Rakip işletme, kusurun bulunması koşuluyla uğradığı maddi zararın tazminini de isteyebilir',
            'D': 'Kendini gerçek dışı beyanlarla üstün duruma getirmek de haksız rekabet hâlidir',
            'E': 'Reklamlarda yer alan abartılı ifadeler ticari övgü sayılarak haksız rekabetin dışında tutulur',
        },
        'E',
        'TTK md. 55/1-a uyarınca gerçek dışı beyanlarla kötüleme ve üstünlük iddiası açık haksız rekabet hâlleridir; gerçeğe aykırı ifadeler ticari övgü sayılarak korunmaz.',
    ),
    # düzey 3
    '0017': patch(
        'Bir işletme, tanınmış bir markanın ambalajını ve raf görünümünü tüketicide aynı işletmeye ait olduğu izlenimi doğuracak biçimde taklit etmiştir. Marka hakkı bakımından ayrı bir ihlal saptanmamıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Mahkeme, karıştırılmaya yol açan durumun ortadan kaldırılmasına da karar verebilir',
            'B': 'Karıştırılmaya yol açan önlemler almak başlı başına haksız rekabet hâli oluşturur',
            'C': 'Tescilli bir sınai hak ihlal edilmediğinden haksız rekabet hükümleri uygulanamaz',
            'D': 'Zarar tehlikesiyle karşılaşan işletme de önleme davası açabilir',
            'E': 'Haksız rekabet koruması sınai hak korumasından bağımsız olarak uygulanabilir',
        },
        'C',
        'TTK md. 55/1-a-4 ve md. 56 uyarınca karıştırılma tehlikesi doğuran davranışlar sınai hak ihlalinden bağımsız olarak haksız rekabet oluşturur.',
    ),
    # düzey 2
    '0018': patch(
        'Bir işletmenin çalışanı, görevini yaparken üçüncü kişilere karşı haksız rekabet oluşturan davranışlarda bulunmuştur. Zarar gören işletme, doğrudan işverene başvurmak istemektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İstihdam edene karşı tespit, men ve düzeltme davaları yöneltilebilir',
            'B': 'Çalışanın kişisel davranışından yalnızca çalışanın kendisi sorumlu tutulabilir',
            'C': 'Haksız rekabet çalışanlar tarafından işlenmişse istihdam edene karşı da dava açılabilir',
            'D': 'İstihdam eden aleyhine tazminat davası açılabilmesi kusur koşuluna bağlıdır',
            'E': 'Zarar gören, dilerse hem çalışana hem istihdam edene karşı dava açabilir',
        },
        'B',
        'TTK md. 57 uyarınca haksız rekabet, hizmetlerini veya işlerini gördükleri sırada çalışanlar tarafından işlenmişse davalar istihdam edene karşı da açılabilir.',
    ),
    # düzey 3
    '0019': patch(
        'Bir gazetede yayımlanan ilan haksız rekabet oluşturmaktadır. Zarar gören işletme, doğrudan gazetenin sahibi ve yayımlayanı aleyhine dava açmak istemektedir. İlanı veren işletme bellidir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Basın yoluyla işlenen haksız rekabette dava öncelikle yayın kuruluşuna karşı açılır',
            'B': 'Dava öncelikle yazının sahibi veya ilan veren aleyhine açılır',
            'C': 'Zarar gören, yayın kuruluşundan düzeltmenin yayımlanmasını da isteyebilir',
            'D': 'Yayın sahibi ve yayımlayan aleyhine dava kanunda sayılan hâllerle sınırlıdır',
            'E': 'Yazı sahibinin izni olmaksızın yayımlanan yazılarda sorumluluk kuralı farklı işler',
        },
        'A',
        'TTK md. 58 uyarınca basın, yayın, iletişim ve bilişim kuruluşları yoluyla işlenen haksız rekabette dava öncelikle yazı sahibi veya ilan veren aleyhine açılır.',
    ),
    # düzey 2
    '0020': patch(
        'Bir işletme, rakibinin haksız rekabet oluşturan davranışının sürdüğünü, dava sonuna kadar beklemesi hâlinde giderilmesi güç zararlara uğrayacağını ileri sürerek mahkemeye başvurmuştur. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Mahkeme, haksız rekabetin önlenmesi için ihtiyati tedbire karar verebilir',
            'B': 'Tedbir kararıyla haksız rekabet oluşturan davranışın durdurulması sağlanabilir',
            'C': 'Haksız rekabet davalarında ihtiyati tedbir istenmesine kanunen olanak tanınmamıştır',
            'D': 'Mevcut durumun korunması amacıyla da ihtiyati tedbir istenebilir',
            'E': 'Tedbir istemi, esas hakkındaki dava açılmadan önce de ileri sürülebilir',
        },
        'C',
        'TTK md. 61 uyarınca dava açma hakkını haiz bulunan kimsenin talebi üzerine mahkeme ihtiyati tedbire karar verebilir.',
    ),
    # düzey 3
    '0021': patch(
        'Bir işletme sahibi, rakibinin haksız rekabet oluşturan fiili nedeniyle ceza soruşturması başlatılmasını istemektedir. Fiil kanunda cezai yaptırıma bağlanmış hâllerden biridir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tüzel kişinin faaliyeti çerçevesinde işlenen fiilde adına hareket edenler cezalandırılır',
            'B': 'Haksız rekabet suçları resen soruşturulur ve şikâyet aranmaz',
            'C': 'Cezai sorumluluk, hukuk davası açma hakkını ortadan kaldırmaz',
            'D': 'Ceza soruşturması dava açma hakkına sahip olanların şikâyeti üzerine yapılır',
            'E': 'Kanunda sayılan haksız rekabet fiilleri cezai yaptırıma bağlanmıştır',
        },
        'B',
        "TTK md. 62 uyarınca haksız rekabet suçlarının kovuşturulması md. 56/1'de yazılı kişilerin şikâyetine bağlıdır.",
    ),
    # düzey 2
    '0022': patch(
        'Bir işletme, haksız rekabet nedeniyle uğradığı zararı tazmin ettirmek istemektedir. Zararın miktarını kesin olarak belirlemek güçtür; ancak fail haksız rekabet yoluyla önemli bir kazanç elde etmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tazminat istemi, haksız rekabetin tespiti istemiyle birlikte ileri sürülebilir',
            'B': 'Maddi tazminat istenebilmesi failin kusurlu olmasına bağlıdır',
            'C': 'Mahkeme, tazminat olarak failin elde etmesi mümkün görülen menfaatin karşılığına hükmedebilir',
            'D': 'Koşulları varsa manevi tazminat da istenebilir',
            'E': 'Zararın miktarı kesin olarak ispat edilemiyorsa tazminat istemi tümüyle reddedilir',
        },
        'E',
        'TTK md. 56/1-e uyarınca mahkeme tazminat olarak, haksız rekabet sonucunda davalının elde etmesi mümkün görülen menfaatin karşılığına da karar verebilir.',
    ),
    # düzey 3
    '0023': patch(
        'Bir işletme, rakibinin eski çalışanına ödeme yaparak üretim sırlarını elde etmiş ve bu bilgileri kendi üretiminde kullanmıştır. Çalışanın iş sözleşmesi sona ermiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Çalışanlara menfaat sağlayarak sır elde etmeye yöneltmek haksız rekabet sayılır',
            'B': 'Üretim ve iş sırlarını hukuka aykırı yolla ele geçirmek haksız rekabet hâlidir',
            'C': 'İş sözleşmesi sona erdiğinden sırların açıklanması hukuka aykırılık oluşturmaz',
            'D': 'Ele geçirilen sırları değerlendirmek de ayrıca haksız rekabet oluşturur',
            'E': 'Sırrı kullanan işletme, kusuru varsa doğan zarardan tazminatla sorumlu olur',
        },
        'C',
        'TTK md. 55/1-b ve 55/1-d uyarınca çalışanları menfaat sağlayarak sır ifşasına yöneltmek ve sırları hukuka aykırı yolla ele geçirip değerlendirmek haksız rekabet hâlleridir.',
    ),
    # düzey 2
    '0024': patch(
        'Bir işletme, kendisine ticari görüşme sırasında güvenilerek verilen teklif ve maliyet hesabından yararlanarak aynı işi başka bir müşteriye sunmuştur. Belgelerde gizlilik kaydı bulunmamaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Zarar gören, haksız rekabetin tespitini kusur aranmaksızın dava edebilir',
            'B': 'Teklif, hesap ve plan gibi belgeler kanunda iş ürünü olarak sayılmıştır',
            'C': 'Belgelerde gizlilik kaydı bulunmadığından bunlardan yararlanmak hukuka uygun sayılır',
            'D': 'İş ürünlerini teknik çoğaltma yöntemiyle devralıp yararlanmak da haksız rekabettir',
            'E': 'Kendisine emanet edilen iş ürünlerinden yetkisiz yararlanmak haksız rekabet hâlidir',
        },
        'C',
        'TTK md. 55/1-c uyarınca kendisine emanet edilen teklif, hesap veya plan gibi iş ürünlerinden yetkisiz yararlanmak haksız rekabet hâlidir; gizlilik kaydı koşul değildir.',
    ),
    # düzey 3
    '0025': patch(
        'Bir işletme sahibi, sahip olmadığı bir mesleki payeye ve almadığı bir sektör ödülüne sahipmiş gibi hareket ederek tanıtım yapmakta; ayrıca sattığı ürünün kullanımına ilişkin tehlikeleri müşterilerden gizlemektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sahip olunmayan paye, diploma veya ödüle sahipmiş gibi hareket etmek haksız rekabettir',
            'B': 'Mahkeme, yanıltıcı beyanların düzeltilmesine kusur aranmaksızın karar verebilir',
            'C': 'Ekonomik menfaati zarar gören müşteri bu davranışlar nedeniyle dava açabilir',
            'D': 'Malın tehlikelerini gizleyerek müşteriyi yanıltmak da haksız rekabet hâli sayılır',
            'E': 'Ödül ve paye beyanları öznel tanıtım ifadesi sayıldığından haksız rekabet dışında kalır',
        },
        'E',
        'TTK md. 55/1-a-3 uyarınca paye, diploma veya ödüle sahip olmadığı hâlde sahipmiş gibi hareket etmek; md. 55/1-a-12 uyarınca malın tehlikelerini gizleyerek müşteriyi yanıltmak haksız rekabet hâlleridir.',
    ),
    # düzey 2
    '0026': patch(
        'Bir işletme, satış sözleşmelerinde karşı taraf aleyhine ağır dengesizlik yaratan ve dürüstlük kuralına aykırı genel işlem şartları kullanmaktadır. Şartlar tek yanlı hazırlanmış ve sözleşmelere konulmuştur. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Dürüstlük kuralına aykırı işlem şartları kullanmak haksız rekabet hâli sayılır',
            'B': 'Ekonomik menfaatleri zarar gören müşteriler de dava açabilir',
            'C': 'Mesleki ve ekonomik birlikler bu konuda tespit ve men davası açabilir',
            'D': 'Bu şartlar, genel işlem koşullarının denetimine ilişkin borçlar hukuku hükümlerine göre de denetlenebilir',
            'E': 'Genel işlem şartları yalnızca tüketici işlemlerinde denetlenebilen sözleşme hükümleridir',
        },
        'E',
        'TTK md. 55/1-f uyarınca dürüstlük kuralına aykırı işlem şartları kullanmak haksız rekabet hâlidir; denetim tüketici işlemleriyle sınırlı değildir.',
    ),
    # düzey 3
    '0027': patch(
        'Bir işletme, tüketicilerin karar verme özgürlüğünü kısıtlayan saldırgan satış yöntemleri kullanmakta, ayrıca malın gerçek değeri hakkında yanıltıcı fiyat gösterimleri yapmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Saldırgan satış yöntemleri kullanmak haksız rekabet hâli sayılır',
            'B': 'Mahkeme, haksız rekabetin sonucu olan maddi durumun ortadan kaldırılmasına karar verebilir',
            'C': 'Malın değeri hakkında yanıltıcı fiyat gösterimi de haksız rekabet oluşturur',
            'D': 'Satış yöntemlerinin seçimi işletmenin ticari serbestisi içinde kaldığından denetlenemez',
            'E': 'Bu davranışlar nedeniyle ekonomik menfaati zarar gören müşteri dava açabilir',
        },
        'D',
        'TTK md. 55/1-a uyarınca müşterinin karar verme özgürlüğünü sınırlayan saldırgan satış yöntemleri ve aldatıcı fiyat gösterimleri dürüstlük kuralına aykırı davranışlardır.',
    ),
    # düzey 2
    '0028': patch(
        'Bir işletme, haksız rekabet oluşturan basılı tanıtım malzemelerinin ve bu malzemeleri üretmeye yarayan kalıpların ortadan kaldırılmasını istemektedir. Malzemeler davalının elindedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yanlış veya yanıltıcı beyanların düzeltilmesi de talep edilebilir',
            'B': 'Haksız rekabetin sonucu olan maddi durumun ortadan kaldırılması istenebilir',
            'C': 'Haksız rekabette araçların imhası istenemez, yalnızca kullanımlarının durdurulması istenebilir',
            'D': 'Bu istemler için failin kusurlu olması koşulu aranmaz',
            'E': 'Mahkeme, haksız rekabetin işlenmesinde etkili olan araçların ve bu yolla üretilen malların imhasına karar verebilir',
        },
        'C',
        'TTK md. 56/1-b ve 56/2 uyarınca haksız rekabetin işlenmesinde etkili olan araçların ve malların imhası istenebilir.',
    ),
    # düzey 3
    '0029': patch(
        'Bir tüketici, bir işletmenin yanıltıcı fiyat gösterimleri nedeniyle ekonomik menfaatinin zarar gördüğünü ileri sürerek dava açmak istemektedir. İşletme, haksız rekabet davalarını yalnızca rakiplerin açabileceğini savunmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Haksız rekabet davalarını açma hakkı yalnızca zarar gören rakiplere tanınmıştır',
            'B': 'Ekonomik menfaatleri zarar gören müşteriler de haksız rekabet davası açabilir',
            'C': 'Müşteriler dava açabilir, ancak bu hak yalnızca tazminat istemleriyle sınırlıdır',
            'D': 'Müşterilerin dava hakkı yalnızca tüketici mevzuatındaki yollarla sınırlandırılmıştır',
            'E': 'Müşterilerin dava açabilmesi ilgili mesleki birliğin bu yönde onay vermesine bağlıdır',
        },
        'B',
        'TTK md. 56/1 ve 56/2 uyarınca haksız rekabet sebebiyle ekonomik menfaatleri zarar gören müşteriler de tespit, men ve eski hâle getirme davalarını açabilir.',
    ),
    # düzey 2
    '0030': patch(
        'Bir işletme, haksız rekabet oluşturan davranış nedeniyle mesleki itibarının zedelendiğini, bunun kişilik haklarına saldırı oluşturduğunu ileri sürmektedir. İşletme maddi zararını da talep etmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Manevi tazminat istenebilmesi için ayrıca ceza davasının açılmış olması gerekir',
            'B': 'Manevi tazminat yalnızca gerçek kişiler bakımından istenebilecek bir tazminat türüdür',
            'C': 'Koşulları varsa maddi tazminatın yanında manevi tazminat da istenebilir',
            'D': 'Haksız rekabet davalarında yalnızca maddi tazminat istenebilir, manevi tazminat istenemez',
            'E': 'Manevi tazminat ancak maddi zararın ispat edilememesi hâlinde ikame olarak istenebilir',
        },
        'C',
        "TTK md. 56/1-e uyarınca Türk Borçlar Kanunu'nun 58. maddesinde öngörülen koşulların varlığında manevi tazminat da istenebilir.",
    ),
    # düzey 3
    '0031': patch(
        'Bir işletme, rakibinin haksız rekabet oluşturan davranışının hukuka aykırılığının saptanmasını istemekte, ancak davranış sona ermiş olduğundan önleme istemekte hukuki yararı bulunmadığı söylenmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Davranış sona ermiş olsa da etkileri sürüyorsa tespit davası açılmasında hukuki yarar bulunur',
            'B': 'Davranış sona erdiğinde açılabilecek tek dava maddi tazminat davası olarak kalır',
            'C': 'Tespit istemi yalnızca men davasıyla birlikte ileri sürülebilen bağlı bir istemdir',
            'D': 'Tespit davası, haksız rekabetin sürmekte olduğu hâllerle sınırlı olup sona ermiş davranışlar bakımından açılamaz',
            'E': 'Davranışın sona ermesi bütün dava haklarını kendiliğinden düşüren bir sonuç doğurur',
        },
        'A',
        'TTK md. 56/1-a uyarınca fiilin haksız olup olmadığının tespiti bağımsız bir dava türüdür; haksız rekabetin etkileri sürdüğü sürece hukuki yarar bulunur.',
    ),
    # düzey 2
    '0032': patch(
        'Bir işletme, haksız rekabet nedeniyle yayılan yanlış beyanların düzeltilmesini talep etmiştir. Davalı, düzeltmenin ancak kendisinin rızasıyla yapılabileceğini ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Düzeltme istemi kanunda sayılmamış olup ancak tazminat yoluyla giderim istenebilir',
            'B': 'Mahkeme, yanlış veya yanıltıcı beyanların düzeltilmesine karar verebilir',
            'C': 'Beyanların düzeltilmesi ancak davalının bu yönde rıza göstermesiyle sağlanabilir',
            'D': 'Düzeltme kararı verilebilmesi davalının kusurunun ispat edilmesine bağlıdır',
            'E': 'Düzeltme yalnızca basın yoluyla işlenen haksız rekabet hâllerinde istenebilir',
        },
        'B',
        'TTK md. 56/1-c uyarınca yanlış veya yanıltıcı beyanların düzeltilmesi dava konusu yapılabilir ve bu dava kusur koşuluna bağlı değildir.',
    ),
    # düzey 3
    '0033': patch(
        'Bir tüzel kişinin faaliyeti çerçevesinde, organları tarafından haksız rekabet oluşturan ve cezai yaptırıma bağlanmış bir fiil işlenmiştir. Şikâyet üzerine soruşturma başlatılmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tüzel kişi adına hareket eden veya etmesi gereken kişiler cezalandırılır',
            'B': 'Tüzel kişilerin ceza sorumluluğu bulunduğundan tüzel kişi hapis cezasıyla cezalandırılır',
            'C': 'Tüzel kişi hakkında yalnızca hukuk davası açılabilir, ceza soruşturması yürütülemez',
            'D': 'Ceza sorumluluğu yalnızca fiili bizzat işleyen çalışana yüklenebilen kişisel bir sorumluluktur',
            'E': 'Tüzel kişinin faaliyeti çerçevesinde işlenen fiiller bakımından ceza sorumluluğu doğmaz',
        },
        'A',
        'TTK md. 63 uyarınca haksız rekabet fiili bir tüzel kişinin faaliyeti çerçevesinde işlenmişse, tüzel kişi adına hareket eden veya etmesi gerekli olan gerçek kişiler hakkında ceza hükümleri uygulanır.',
    ),
    # düzey 2
    '0034': patch(
        'Bir işletme, haksız rekabet nedeniyle açacağı davada hangi mahkemenin görevli olduğunu araştırmaktadır. Karşı taraf tacir değildir ve uyuşmazlığın ticari nitelik taşımadığını ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Görevli mahkeme, talep edilen tazminat tutarına göre belirlenen bir usul sorunudur',
            'B': 'Davanın ticari sayılabilmesi her iki tarafın da tacir sıfatını taşımasına bağlıdır',
            'C': 'Haksız rekabete ilişkin davalar mutlak ticari dava olup asliye ticaret mahkemesinde görülür',
            'D': 'Haksız rekabet davaları ticari nitelik taşımayıp genel hükümlere tabi olduğundan asliye hukuk mahkemesinde görülür',
            'E': 'Tarafların tacir olmadığı hâllerde uyuşmazlık tüketici mahkemesinde çözümlenir',
        },
        'C',
        "TTK md. 4/1-a uyarınca Türk Ticaret Kanunu'nda düzenlenen hususlardan doğan davalar tarafların sıfatına bakılmaksızın ticari dava sayılır; md. 5 uyarınca asliye ticaret mahkemesi görevlidir.",
    ),
    # düzey 3
    '0035': patch(
        "Bir işletme, haksız rekabet oluşturan fiili öğrendikten on ay sonra dava açmıştır. Fiilin işlenmesinin üzerinden ise dört yıl geçmiştir. Davalı zamanaşımı def'inde bulunmuştur. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Öğrenmeden itibaren bir yıllık süre dolmadığından dava süresinde açılmış sayılır',
            'B': 'Zamanaşımı süresi fiilin doğumundan itibaren on yıl olduğundan dava süresindedir',
            'C': 'Haksız rekabet davalarında yalnızca öğrenme tarihinden başlayan süre dikkate alınır',
            'D': "Zamanaşımı def'i ancak tazminat istemleri bakımından ileri sürülebilen bir savunmadır",
            'E': 'Fiilin doğumundan itibaren üç yıllık süre dolduğundan dava zamanaşımına uğramıştır',
        },
        'E',
        'TTK md. 60 uyarınca dava hakkı, öğrenilmesinden itibaren bir yıl ve her hâlde doğumundan itibaren üç yıl geçmekle zamanaşımına uğrar; iki süre birlikte işler.',
    ),
    # düzey 3
    '0036': patch(
        "Bir işletme, haksız rekabet oluşturan fiilin aynı zamanda Türk Ceza Kanunu'na göre daha uzun bir zamanaşımı süresine tabi suç oluşturduğunu ileri sürerek hukuk davasının süresinde olduğunu savunmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Fiil ceza kanununa göre daha uzun zamanaşımına tabi bir suçsa bu süre hukuk davasında da uygulanır',
            'B': 'Hukuk davasının zamanaşımı, fiilin suç oluşturup oluşturmadığına bakılmaksızın ticaret kanunundaki sürelerle sınırlı kalır',
            'C': 'Ceza davası açılmadıkça ceza zamanaşımına ilişkin sürelerden yararlanılamaz',
            'D': 'Fiilin suç oluşturması hukuk davasında zamanaşımı süresini kısaltan bir etki doğurur',
            'E': 'Ceza zamanaşımı yalnızca ceza soruşturması bakımından sonuç doğuran bir süredir',
        },
        'A',
        'TTK md. 60 uyarınca haksız rekabet fiili Türk Ceza Kanunu gereğince daha uzun dava zamanaşımına tabi bir suç oluşturuyorsa bu zamanaşımı hukuk davaları için de uygulanır.',
    ),
    # düzey 2
    '0037': patch(
        'Bir gazetede, yazarın izni olmaksızın ve içeriği değiştirilerek yayımlanan bir yazı haksız rekabet oluşturmaktadır. Zarar gören işletme kime karşı dava açacağını araştırmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yazının izinsiz yayımlanması yalnızca yazar ile yayın kuruluşu arasındaki ilişkiyi ilgilendirir',
            'B': 'Yayın kuruluşları basın özgürlüğü kapsamında bu davaların dışında tutulmuştur',
            'C': 'Dava, istisnasız biçimde öncelikle yazının sahibine karşı açılabilen bir davadır',
            'D': 'Yazı sahibinin izni olmaksızın yayımlanmışsa dava yayın sahibi ve yayımlayana yöneltilebilir',
            'E': 'Yayın kuruluşuna karşı dava açılabilmesi yazı sahibinin belirlenememesine bağlıdır',
        },
        'D',
        'TTK md. 58 uyarınca yazı sahibinin izni olmaksızın veya yazı içeriği değiştirilerek yayımlanmışsa dava, yayın sahibine ve yayımlayana karşı da açılabilir.',
    ),
    # düzey 3
    '0038': patch(
        'Bir işletme, rakibinin ürünleriyle kendi ürünlerini karşılaştıran bir reklam yayımlamıştır. Karşılaştırma somut, doğru ve objektif verilere dayanmaktadır. Rakip işletme reklamın haksız rekabet oluşturduğunu ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Doğru ve objektif verilere dayanan karşılaştırma kural olarak haksız rekabet oluşturmaz',
            'B': 'Karşılaştırmalı reklam kanunda mutlak biçimde yasaklanmış bir reklam biçimidir',
            'C': 'Karşılaştırmanın hukuka uygun sayılması rakibin önceden yazılı onayına bağlıdır',
            'D': 'Karşılaştırmalı reklam yalnızca fiyat unsuru bakımından yapılabilen sınırlı bir uygulamadır',
            'E': 'Rakibin adının veya ürünlerinin reklamda anılması başlı başına haksız rekabet sayılır',
        },
        'A',
        'TTK md. 55/1-a-5 uyarınca haksız rekabet oluşturan, gerçek dışı, yanıltıcı, gereksiz yere incitici veya rakibin tanınmışlığından yararlanan karşılaştırmalardır; doğru ve objektif karşılaştırma bu kapsamda değildir.',
    ),
    # düzey 2
    '0039': patch(
        'Bir işletme, seçilmiş bazı ürünleri birden çok kez tedarik fiyatının altında satışa sunmuş ve bunu reklamlarında özellikle vurgulayarak müşterilerde genel bir ucuzluk izlenimi doğurmuştur. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Seçilmiş malları tedarik fiyatının altında sunup bunu vurgulamak haksız rekabet hâlidir',
            'B': 'Bu uygulama yalnızca indirimli satış dönemlerinin dışında yapıldığında haksız rekabet olur',
            'C': 'Maliyet altı satışın haksız sayılması rakiplerin piyasadan çekilmesine bağlıdır',
            'D': 'Fiyat belirleme serbestisi gereği maliyetin altında satış, istisnasız hukuka uygun sayılır',
            'E': 'Bu davranış yalnızca rekabetin korunmasına ilişkin idari denetimin konusunu oluşturur',
        },
        'A',
        'TTK md. 55/1-a-7 uyarınca seçilmiş bazı malları tedarik fiyatının altında satışa sunmak, bunu reklamlarda vurgulamak ve böylece müşteriyi yanıltmak haksız rekabet hâlidir.',
    ),
    # düzey 3
    '0040': patch(
        'Bir işletme, müşterilere sunduğu ek edimlerle ürünün gerçek değeri hakkında yanıltıcı bir izlenim doğurmuş; ayrıca ürünün stok durumu ve satış kampanyasının biçimi hakkında gerçek dışı açıklamalar yapmıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Stoklar ve satış kampanyalarının biçimi hakkında gerçek dışı açıklama haksız rekabettir',
            'B': 'Mesleki ve ekonomik birlikler de bu konuda tespit ve men davası açabilir',
            'C': 'Ek edimlerle sunumun gerçek değeri hakkında yanıltmak haksız rekabet hâlidir',
            'D': 'Bu davranışlardan ekonomik menfaati zarar gören müşteri dava açabilir',
            'E': 'Stok ve kampanya biçimine ilişkin açıklamalar reklam serbestisi kapsamında denetim dışıdır',
        },
        'E',
        'TTK md. 55/1-a-2 ve 55/1-a-9 uyarınca stoklar ve kampanya biçimi hakkında gerçek dışı açıklama ile ek edimlerle yanıltma açıkça haksız rekabet hâlleri arasında sayılmıştır.',
    ),
    # düzey 2
    '0041': patch(
        'Bir işletme, başka bir işletmenin ticaret unvanını ve işletme işaretlerini, kendi işletmesiyle karıştırılmaya yol açacak biçimde kullanmaktadır. Unvan bakımından ayrıca sicil koruması tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Karıştırılmaya yol açan işaret kullanımı haksız rekabet hâli sayılır',
            'B': 'Mahkeme, karıştırılmaya yol açan maddi durumun ortadan kaldırılmasına karar verebilir',
            'C': 'Zarar tehlikesiyle karşılaşan işletme önleme davası açabilir',
            'D': 'Unvan ve işaret kullanımı yalnızca ticaret sicili hükümlerine göre değerlendirilebilir',
            'E': 'Haksız rekabet koruması unvanın korunmasına ilişkin hükümlerden bağımsız uygulanabilir',
        },
        'D',
        'TTK md. 55/1-a-4 uyarınca başkasının işletme işaretleriyle karıştırılmaya yol açan önlemler almak haksız rekabettir; unvan koruması ayrıca uygulanır.',
    ),
    # düzey 3
    '0042': patch(
        'Bir işletme, hukuka aykırı biçimde ele geçirdiği üretim sırlarını kullanarak ürettiği malları piyasaya sürmüştür. Zarar gören işletme hem malların hem de üretim kalıplarının ortadan kaldırılmasını istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Malların imhası yerine yalnızca satışlarının durdurulmasına karar verilebilir',
            'B': 'İmha istemi yalnızca fikri mülkiyet haklarının ihlali hâlinde ileri sürülebilir',
            'C': 'Haksız rekabet davalarında yalnızca fiilin durdurulması istenebilir, imha istenemez',
            'D': 'Haksız rekabetin işlenmesinde etkili olan araçların ve malların imhası istenebilir',
            'E': 'İmha kararı verilebilmesi davalının ağır kusurunun ispat edilmesine bağlıdır',
        },
        'D',
        'TTK md. 56/1-b ve 56/2 uyarınca haksız rekabetin işlenmesinde etkili olan araçların ve malların imhası dava konusu yapılabilir.',
    ),
    # düzey 2
    '0043': patch(
        'Haksız rekabet davalarına ilişkin olarak aşağıdaki ifadeler ileri sürülmüştür: I. Tespit davasında failin kusurlu olması gerekir. II. Men davasında kusur aranmaz. III. Maddi tazminat istenebilmesi failin kusuruna bağlıdır. Buna göre bu ifadelerden hangileri doğrudur?',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'I, II ve III',
            'E': 'Yalnız III',
        },
        'C',
        'TTK md. 56 uyarınca tespit, men ve düzeltme davalarında kusur aranmaz; tazminat istemleri kusura bağlıdır. Bu nedenle I yanlış, II ve III doğrudur.',
    ),
    # düzey 3
    '0044': patch(
        'Haksız rekabette dava hakkına ilişkin olarak aşağıdaki ifadeler ileri sürülmüştür: I. Dava açma hakkı yalnızca rakiplere tanınmıştır. II. Ekonomik menfaatleri zarar gören müşteriler de dava açabilir. III. Mesleki ve ekonomik birlikler tazminat davası açabilir. Buna göre bu ifadelerden hangileri doğrudur?',
        {
            'A': 'Yalnız II',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'Yalnız I',
        },
        'A',
        'TTK md. 56/2-3 uyarınca müşteriler ve birlikler de dava açabilir, ancak birlikler tazminat isteyemez; ayrıca dava hakkı rakiplerle sınırlı değildir. Yalnız II doğrudur.',
    ),
    # düzey 2
    '0045': patch(
        'Haksız rekabet hâllerine ilişkin olarak aşağıdaki ifadeler ileri sürülmüştür: I. Başkalarını gerçek dışı beyanlarla kötülemek haksız rekabettir. II. Dürüstlük kuralına aykırı işlem şartları kullanmak haksız rekabet sayılmaz. III. Karıştırılmaya yol açan önlemler almak haksız rekabettir. Buna göre bu ifadelerden hangileri doğrudur?',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'I ve III',
            'D': 'I, II ve III',
            'E': 'Yalnız II',
        },
        'C',
        'TTK md. 55/1-a ve 55/1-f uyarınca kötüleme ve karıştırılma haksız rekabettir; dürüstlük kuralına aykırı işlem şartları da kanunda haksız rekabet sayıldığından II yanlıştır.',
    ),
    # düzey 3
    '0046': patch(
        'Haksız rekabette zamanaşımına ilişkin olarak aşağıdaki ifadeler ileri sürülmüştür: I. Süre öğrenmeden itibaren üç yıldır. II. Her hâlde fiilin doğumundan itibaren beş yıl geçmekle zamanaşımı dolar. III. Fiil daha uzun ceza zamanaşımına tabi bir suç oluşturuyorsa bu süre hukuk davasında da uygulanır. Buna göre bu ifadelerden hangileri doğrudur?',
        {
            'A': 'Yalnız I',
            'B': 'I, II ve III',
            'C': 'Yalnız II',
            'D': 'Yalnız III',
            'E': 'I ve II',
        },
        'D',
        'TTK md. 60 uyarınca süreler öğrenmeden itibaren bir yıl ve her hâlde doğumdan itibaren üç yıldır; ceza zamanaşımı daha uzunsa hukuk davasında da uygulanır. Yalnız III doğrudur.',
    ),
    # düzey 2
    '0047': patch(
        'Haksız rekabet davalarında istenebilecek sonuçlara ilişkin olarak aşağıdaki ifadeler ileri sürülmüştür: I. Haksız rekabetin sonucu olan maddi durumun ortadan kaldırılması istenemez. II. Yanlış veya yanıltıcı beyanların düzeltilmesi istenebilir. III. Haksız rekabetin işlenmesinde etkili olan araçların imhası istenebilir. Buna göre bu ifadelerden hangileri doğrudur?',
        {
            'A': 'Yalnız I',
            'B': 'I, II ve III',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'I ve III',
        },
        'C',
        'TTK md. 56/1-b, 56/1-c ve 56/2 uyarınca maddi durumun ortadan kaldırılması, beyanların düzeltilmesi ve araçların imhası istenebilir; bu nedenle I yanlış, II ve III doğrudur.',
    ),
    # düzey 3
    '0048': patch(
        'Haksız rekabette sorumluluğun kime yöneltileceğine ilişkin olarak aşağıdaki ifadeler ileri sürülmüştür: I. Haksız rekabet çalışanlarca işlenmişse istihdam edene karşı da dava açılabilir. II. Basın yoluyla işlenen haksız rekabette dava öncelikle yayın sahibine karşı açılır. III. Tüzel kişinin faaliyeti çerçevesinde işlenen fiilde tüzel kişi adına hareket edenler cezalandırılır. Buna göre bu ifadelerden hangileri doğrudur?',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'Yalnız II',
        },
        'D',
        'TTK md. 57 ve 63 uyarınca I ve III doğrudur; md. 58 uyarınca basın yoluyla işlenen haksız rekabette dava öncelikle yazı sahibi veya ilan veren aleyhine açıldığından II yanlıştır.',
    ),
    # düzey 2
    '0049': patch(
        'Haksız rekabet hükümlerinin uygulama alanına ilişkin olarak aşağıdaki ifadeler ileri sürülmüştür: I. Hükümlerin uygulanması taraflar arasında rekabet ilişkisi bulunmasına bağlıdır. II. Zarar tehlikesiyle karşılaşan kişi de dava açabilir. III. Amaç bütün katılanların yararına dürüst ve bozulmamış rekabeti sağlamaktır. Buna göre bu ifadelerden hangileri doğrudur?',
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'Yalnız II',
            'D': 'I, II ve III',
            'E': 'II ve III',
        },
        'E',
        'TTK md. 54 ve 56 uyarınca korumadan yararlanmak rekabet ilişkisi koşuluna bağlanmamıştır; II ve III doğrudur.',
    ),
    # düzey 3
    '0050': patch(
        'Bir işletme, rakibinin ticari faaliyetleri ve iş ilişkileri hakkında yanıltıcı açıklamalarda bulunmuş; bu açıklamalar sonucunda rakip önemli bir müşterisini kaybetmiştir. Rakip hem fiilin durdurulmasını hem zararının giderilmesini istemektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Maddi tazminat istenebilmesi failin kusuruna bağlıdır',
            'B': 'Zarar gören, aynı davada tespit ve düzeltme istemlerini birlikte ileri sürebilir',
            'C': 'Başkasının iş ilişkileri hakkında yanıltıcı açıklama haksız rekabet hâlidir',
            'D': 'Zarar gerçekleştiğinden artık yalnızca tazminat istenebilir, önleme istenemez',
            'E': "Haksız rekabetin men'i kusur aranmaksızın dava edilebilir",
        },
        'D',
        'TTK md. 56/1 uyarınca tespit, men, düzeltme ve tazminat istemleri birlikte ileri sürülebilir; zararın gerçekleşmiş olması men istemini ortadan kaldırmaz.',
    ),
    # düzey 2
    '0051': patch(
        'Bir işletme, rakibinin çalışanlarına menfaat sağlayarak onları görevlerine aykırı davranmaya ve şirket sırlarını açıklamaya yöneltmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bu yolla elde edilen sırların değerlendirilmesi ayrıca haksız rekabet oluşturur',
            'B': 'Çalışanlara menfaat sağlamak yalnızca iş sözleşmesine aykırılık oluşturan bir davranıştır',
            'C': 'İşçileri ve vekilleri görevlerine aykırı davranmaya yöneltmek haksız rekabet hâlidir',
            'D': 'Zarar gören işletme, davranışın önlenmesini kusur aranmaksızın isteyebilir',
            'E': 'Fiil kanunda cezai yaptırıma bağlanmışsa şikâyet üzerine soruşturma yürütülebilir',
        },
        'B',
        'TTK md. 55/1-b uyarınca çalışanları, vekilleri veya yardımcıları menfaat sağlayarak görevlerine aykırı davranmaya yöneltmek haksız rekabet hâlidir.',
    ),
    # düzey 3
    '0052': patch(
        'Bir işletme aleyhine haksız rekabet davası açılmış, mahkeme davayı kabul etmiştir. Davacı, kararın gazetede yayımlanmasını istemekte; davalı ise ilan masrafının davacıya yükletilmesi gerektiğini savunmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İlan masrafı, davayı kaybeden tarafa ait olmak üzere hükmedilir',
            'B': 'Mahkeme, kazanan tarafın istemiyle kararın ilanına karar verebilir',
            'C': 'Kararın ilan masrafı, ilanı isteyen kazanan tarafa yükletilir',
            'D': 'İlan, kararın kesinleşmesinden sonra yapılır',
            'E': 'İlanın biçimi ve kapsamı mahkemece belirlenir',
        },
        'C',
        'TTK md. 59 uyarınca mahkeme, kazanan tarafın istemiyle masrafı diğer tarafa ait olmak üzere kararın ilanına karar verebilir.',
    ),
    # düzey 2
    '0053': patch(
        'Bir işletme, haksız rekabet oluşturan davranışın sürmesi hâlinde giderilmesi güç zararlara uğrayacağını ileri sürerek dava açmadan önce mahkemeye başvurmuştur. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Dava açma hakkına sahip olan kişi ihtiyati tedbir isteyebilir',
            'B': 'Mahkeme, mevcut durumun korunması amacıyla tedbire karar verebilir',
            'C': 'İhtiyati tedbir istemi ancak esas hakkındaki dava açıldıktan sonra ileri sürülebilir',
            'D': 'Tedbir kararı, esas hakkındaki hükümden bağımsız olarak uygulanabilir',
            'E': 'Tedbirle haksız rekabet oluşturan davranışın durdurulması ve mevcut durumun korunması birlikte sağlanabilir',
        },
        'C',
        'TTK md. 61 ve usul hükümleri uyarınca ihtiyati tedbir, dava açılmadan önce de istenebilir.',
    ),
    # düzey 3
    '0054': patch(
        'Bir işletme, üretim sırlarını hukuka aykırı yolla ele geçirdiği rakibine karşı açılan davada, sırları yalnızca öğrendiğini ancak kullanmadığını savunmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sırların kullanılmamış olması haksız rekabetin oluşmasını engelleyen bir savunmadır',
            'B': 'Ele geçirilen sırların değerlendirilmesi ayrıca haksız rekabet oluşturur',
            'C': 'Kusur bulunması hâlinde ayrıca tazminat istenebilir',
            'D': 'Zarar tehlikesiyle karşılaşan işletme önleme davası açabilir',
            'E': 'Sırları hukuka aykırı biçimde ele geçirmek başlı başına haksız rekabet hâlidir',
        },
        'A',
        'TTK md. 55/1-d uyarınca üretim ve iş sırlarını hukuka aykırı biçimde ele geçirmek ile değerlendirmek ayrı ayrı haksız rekabet hâlleridir.',
    ),
    # düzey 2
    '0055': patch(
        'Bir işletme, haksız rekabet oluşturan davranışın kendi çalışanınca ve görev sırasında işlendiğini, bu nedenle sorumluluğunun doğmadığını ileri sürmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İstihdam eden aleyhine tazminat istenebilmesi kusur koşuluna bağlıdır',
            'B': 'Çalışanın görev sırasında işlediği fiilden istihdam eden sorumlu tutulamaz',
            'C': 'İstihdam edene tespit, men ve düzeltme davaları yöneltilebilir',
            'D': 'Haksız rekabet çalışanlarca işlenmişse istihdam edene karşı da dava açılabilir',
            'E': 'Zarar gören, çalışan ve istihdam eden aleyhine birlikte dava açabilir',
        },
        'B',
        'TTK md. 57 uyarınca haksız rekabet, hizmetlerini gördükleri sırada çalışanlarca işlenmişse davalar istihdam edene karşı da açılır.',
    ),
    # düzey 3
    '0056': patch(
        'Bir işletme, ticari faaliyetine ilişkin gerçek dışı açıklamalarla kendisini rekabette öne çıkarmış; bu açıklamalar üçüncü kişilerce de yayılarak yaygınlaşmıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kendi ticari faaliyetleri ve iş ilişkileri hakkında gerçek dışı açıklamada bulunmak haksız rekabet hâlleri arasında sayılmıştır',
            'B': 'Gerçek dışı açıklamanın üçüncü kişilerce yayılması aslen açıklamayı yapanın sorumluluğunu kaldırır',
            'C': 'Zarar gören, açıklamaların düzeltilmesini dava edebilir',
            'D': 'Kusur bulunması hâlinde ayrıca maddi tazminat istenebilir',
            'E': 'Yanıltıcı biçimde kendini rekabette öne geçirmek de haksız rekabet oluşturur',
        },
        'B',
        'TTK md. 55/1-a-2 uyarınca kendi faaliyetleri hakkında gerçek dışı veya yanıltıcı açıklamalarla kendini rekabette öne geçirmek haksız rekabet hâlidir.',
    ),
    # düzey 2
    '0057': patch(
        'Bir işletme, haksız rekabet nedeniyle mesleki itibarının zedelendiğini ileri sürerek manevi tazminat istemektedir. Davalı, tüzel kişilerin manevi tazminat isteyemeyeceğini savunmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Manevi tazminat yalnızca gerçek kişiler tarafından istenebilen bir tazminat türüdür',
            'B': 'Manevi tazminat istemi maddi tazminat istemiyle birlikte ileri sürülebilir',
            'C': 'Manevi tazminat istenebilmesi failin kusuruna bağlıdır',
            'D': 'Mesleki itibarın zedelenmesi haksız rekabet davası açma hakkı veren hâllerdendir',
            'E': 'Koşulları varsa haksız rekabet nedeniyle manevi tazminat istenebilir',
        },
        'A',
        'TTK md. 56/1-e ve TBK md. 58 uyarınca koşulları varsa manevi tazminat istenebilir; tüzel kişilerin kişilik değerleri de korunur.',
    ),
    # düzey 3
    '0058': patch(
        'Bir işletme, rakibinin tanınmışlığından yararlanmak amacıyla reklamlarında rakibin markasına gereksiz yere gönderme yapmış ve karşılaştırmayı incitici biçimde kurgulamıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Rakibin tanınmışlığından yararlanan karşılaştırma haksız rekabet sayılır',
            'B': 'Karşılaştırmalı reklamlarda rakip markaya gönderme yapılması her durumda hukuka uygundur',
            'C': 'Doğru ve objektif verilere dayanan karşılaştırma kural olarak haksız rekabet değildir',
            'D': 'Zarar gören işletme reklamın durdurulmasını kusur aranmaksızın isteyebilir',
            'E': 'Gereksiz yere incitici karşılaştırmalar da haksız rekabet oluşturur',
        },
        'B',
        'TTK md. 55/1-a-5 uyarınca gereksiz yere incitici veya rakibin tanınmışlığından yararlanan karşılaştırmalar haksız rekabet hâlidir.',
    ),
    # düzey 2
    '0059': patch(
        'Bir işletme hakkında haksız rekabet nedeniyle hem hukuk davası açılmış hem de şikâyet üzerine ceza soruşturması başlatılmıştır. İşletme, iki yolun birlikte işletilemeyeceğini ileri sürmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ceza soruşturması dava açma hakkına sahip olanların şikâyetine bağlıdır',
            'B': 'Ceza soruşturması başlatıldığında hukuk davası görülemez ve bekletilmesi gerekir',
            'C': 'Hukuk davası, ceza soruşturmasından bağımsız olarak açılıp sürdürülebilir',
            'D': 'Fiil daha uzun ceza zamanaşımına tabiyse bu süre hukuk davasında da uygulanır',
            'E': 'Haksız rekabet fiilleri hem hukuki hem cezai sonuç doğurabilir',
        },
        'B',
        'TTK md. 60 ve 62 uyarınca hukuk ve ceza yolları birbirinden bağımsızdır; ceza soruşturmasının başlaması hukuk davasını durdurmaz.',
    ),
    # düzey 3
    '0060': patch(
        'Bir işletme, haksız rekabet oluşturan davranışı nedeniyle aleyhine açılan davada, davranışın kendisine ekonomik yarar sağlamadığını ve bu nedenle sorumlu tutulamayacağını savunmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Failin sağladığı menfaat, tazminat miktarının belirlenmesinde ölçüt olarak kullanılabilir',
            'B': 'Zarar tehlikesiyle karşılaşan kişi de dava açabilir',
            'C': 'Dürüstlük kuralına aykırı ticari uygulamalar haksız ve hukuka aykırı sayılır',
            'D': 'Tespit ve men davalarında failin kusuru aranmaz',
            'E': 'Haksız rekabetin oluşması failin bu davranıştan ekonomik yarar sağlamasına bağlıdır',
        },
        'E',
        'TTK md. 54 uyarınca dürüstlük kuralına aykırı davranışlar ve ticari uygulamalar haksızdır; failin yarar sağlamış olması kurucu unsur değildir.',
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
    print(f"1 paket / {len(PATCHES)} soru ('Haksiz Rekabet' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
