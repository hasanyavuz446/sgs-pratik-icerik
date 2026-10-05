#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vergi Cezalari ve Uyusmazliklar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Vergiye ozgu profille yeniden yazim (hukuk bandindaki uzun sikli surum mutlak ifadeli celdiriciler nedeniyle FATAL veriyordu): duzeltme-sikayet, 7524 sonrasi uzlasma (yalniz cezalar), cezalarda indirim, izaha davet, ceza genel hukumleri, ceza zamanasimi, IYUK dava sureleri, yurutmenin durdurulmasi, istinaf-temyiz-kanun yararina temyiz-yargilamanin yenilenmesi. Parasal sinirlar sorulmadi; 17 hesap sorusu bagimsiz dogrulandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 213 sayili VUK ve 2577 sayili IYUK guncel metinleri (7331, 7524, 7589 dahil; mevzuat.gov.tr)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/vergi_hukuku/vergi_denetimi_ceza_uyusmazlik.json"
STYLE_REF = 'SGS Vergi Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "vh-denetim-gen-"


def patch(stem, options, answer, solution, ref='213 sayili VUK ve 2577 sayili IYUK'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 1
    '0001': patch(
        "Vergi Usul Kanunu'na göre vergi hatalarının düzeltilmesine kural olarak kim karar verir?",
        {
            'A': 'Vergi mahkemesi',
            'B': 'İlgili vergi dairesi müdürü',
            'C': 'Uzlaşma komisyonu',
            'D': 'Vergi dairesinin bağlı olduğu il defterdarı',
            'E': 'Takdir komisyonu',
        },
        'B',
        "m. 120'ye göre vergi hatalarının düzeltilmesine **ilgili vergi dairesi müdürü** karar verir; vergi dairesi başkanlıklarında bu yetki başkana aittir ve devredilebilir.",
        '213 sayılı VUK m. 120',
    ),
    # düzey 3
    '0002': patch(
        'Bir mükellef, emlak vergisindeki hatanın düzeltilmesini dava açma süresi geçtikten sonra istemiş; talebi reddedilmiştir. Mükellef şikâyet yoluyla nereye başvurabilir?',
        {
            'A': 'Belediye başkanlığına',
            'B': 'Gelir İdaresi Başkanlığına',
            'C': 'Hazine ve Maliye Bakanlığına',
            'D': 'Valiliğe',
            'E': 'Vergi mahkemesine',
        },
        'A',
        "m. 124'e göre **dava açma süresi geçtikten sonra** yaptıkları düzeltme talepleri reddedilenler şikâyet yoluyla Bakanlığa başvurabilir; ancak **il özel idare vergileri için valiliğe, belediye vergileri için belediye başkanlığına** başvurulur. Emlak vergisi belediye vergisidir.",
        '213 sayılı VUK m. 124',
    ),
    # düzey 2
    '0003': patch(
        "Vergi/ceza ihbarnamesi 12 Mayıs'ta tebliğ edilen mükellef, tarhiyat sonrası uzlaşma talebini en geç hangi tarihte yapmalıdır?",
        {
            'A': '12 Temmuz',
            'B': '12 Haziran',
            'C': '11 Haziran',
            'D': '27 Mayıs',
            'E': '22 Mayıs',
        },
        'C',
        "Ek m. 1'e göre uzlaşma talebi **vergi ihbarnamesinin tebliğ tarihinden itibaren otuz gün içinde** yapılır. Süre tebliği izleyen günden başlar: 13 Mayıs birinci gün olmak üzere 30. gün **11 Haziran**'dır.",
        '213 sayılı VUK ek m. 1',
    ),
    # düzey 3
    '0004': patch(
        'Bir mükellef ihbarnameye karşı önce vergi mahkemesinde dava açmış, ardından süresi içinde aynı ceza için uzlaşma talep etmiştir. Açılan dava hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Uzlaşma talebiyle dava konusuz kalarak düşer',
            'B': 'Mahkeme davayı süre aşımından reddeder',
            'C': 'Dava açıldığı için uzlaşma talebi reddedilir',
            'D': 'Uzlaşma sonuçlanıncaya kadar incelenmez; incelenip karara bağlanırsa karar hükümsüzdür',
            'E': 'Dava ve uzlaşma birbirinden bağımsız yürür; önce sonuçlanan geçerli olur',
        },
        'D',
        "Ek m. 7'ye göre mükellef aynı ceza için **uzlaşma talebinden önce dava açmışsa dava, uzlaşma işleminin sonuca bağlanmasından önce incelenmez**; herhangi bir sebeple incelenip karara bağlanırsa **bu karar hükümsüz sayılır**. Uzlaşma vaki olmazsa davanın görülmesine devam edilir.",
        '213 sayılı VUK ek m. 7',
    ),
    # düzey 3
    '0005': patch(
        'Sahte fatura kullanarak vergi ziyaına sebebiyet veren mükellef adına üç kat vergi ziyaı cezası kesilmiştir. Mükellefin uzlaşma talebi hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Uzlaşma talebi dava süresini iki kat uzatır',
            'B': 'Uzlaşma Bakanlık onayıyla yapılabilir',
            'C': 'Uzlaşma tarhiyat öncesi aşamada yapılabilir',
            'D': 'Ceza bir kata indirilerek uzlaşılabilir',
            'E': 'Bu ceza uzlaşma kapsamı dışındadır',
        },
        'E',
        "Ek m. 1'e göre **m. 359'da yazılı fiillerle vergi ziyaına sebebiyet verilmesi hâlinde kesilen ceza** ile bu fiillere iştirak edenlere kesilen ceza uzlaşma kapsamı dışındadır; ek m. 11 tarhiyat öncesi uzlaşma için de aynı istisnayı öngörür.",
        '213 sayılı VUK ek m. 1',
    ),
    # düzey 3
    '0006': patch(
        'Cezalarda indirim için süresinde başvuran mükellef, ödeme süresi dolmadan aynı tarhiyata karşı vergi mahkemesinde dava açmıştır. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İndirim dava sonucuna kadar askıda kalır',
            'B': 'Dava reddedilir, indirim korunur',
            'C': 'Vergi aslı için indirim uygulanır',
            'D': 'İndirim oranı üçte bire düşer',
            'E': 'İndirimden yararlanamaz',
        },
        'E',
        "m. 376'ya göre mükellef **ödeyeceğini bildirdiği vergi ve cezayı süresinde ödemez veya dava konusu yaparsa bu madde hükmünden faydalandırılmaz**.",
        '213 sayılı VUK m. 376',
    ),
    # düzey 2
    '0007': patch(
        'İzaha davete ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kural olarak m. 359 fiillerine ilişkin ön tespitlerde davet yapılmaz',
            'B': 'İzah için davet yazısının tebliğinden itibaren otuz gün süre vardır',
            'C': 'Davet, vergi incelemesine başlanmadan önce yapılır',
            'D': 'İzah yeterli bulunsa da tespit konusu için vergi incelemesi yapılır',
            'E': 'Tespit tarihine kadar ihbarda bulunulmamış olması gerekir',
        },
        'D',
        "m. 370/a-1'e göre izah sonucu vergi ziyaına sebebiyet verilmediğinin anlaşılması hâlinde mükellefler **söz konusu tespitle ilgili olarak vergi incelemesine tabi tutulmaz** veya takdir komisyonuna sevk edilmez. m. 370/b'ye göre m. 359 fiillerine ilişkin ön tespitlerde, kanunda sayılan sınırlı hâller dışında izaha davet yapılmaz.",
        '213 sayılı VUK m. 370',
    ),
    # düzey 2
    '0008': patch(
        'Bir kira sözleşmesine ait damga vergisi cezasından hem kiraya veren hem kiracı sorumludur. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Birden fazla sorumlu varsa ceza kesilmez',
            'B': 'Müteselsilen sorumludurlar; birbirlerine rücu hakları saklıdır',
            'C': 'Ceza yarı yarıya bölünür',
            'D': 'Sadece sözleşmeyi son imzalayan sorumludur',
            'E': 'Sadece kiraya veren sorumludur; kiracıya ödenmeyen kısım için başvurulur',
        },
        'B',
        "m. 334'e göre damga vergisi uygulamalarında cezadan sorumlu olanlar birden fazla ise **birbirlerine müracaat hakları saklı kalmak üzere müteselsilen sorumlu** tutulur.",
        '213 sayılı VUK m. 334',
    ),
    # düzey 3
    '0009': patch(
        "Bir fiil nedeniyle önce 3.000 ₺ usulsüzlük cezası kesilmiş, sonradan aynı fiille 12.000 ₺ vergi ziyaı cezasını gerektiren vergi ziyaına sebebiyet verildiği anlaşılmıştır. İkmalen kesilecek ceza kaç ₺'dir?",
        {
            'A': '12.000',
            'B': '6.000',
            'C': '3.000',
            'D': '0',
            'E': '9.000',
        },
        'E',
        "m. 336'ya göre tek fiille vergi ziyaı ve usulsüzlük birlikte işlenirse **yalnız miktarca en ağırı** kesilir. Önce usulsüzlük cezası kesilmiş olması, **vergi ziyaı cezasıyla mukayeseye ve noksan kesilen cezanın ikmaline** engel değildir: 12.000 − 3.000 = **9.000 ₺**.",
        '213 sayılı VUK m. 336',
    ),
    # düzey 3
    '0010': patch(
        'Bir mükellef bir işlemini yürürlükteki genel tebliğe uygun şekilde yapmış; bir yıl sonra idare aynı konuda görüşünü değiştiren yeni bir tebliğ yayımlamıştır. Önceki işlem hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Önceki işlemler için yeni görüşe göre vergi alınır, ancak ceza kesilmez',
            'B': 'Mükellef yeni görüşe göre düzeltme beyannamesi vermelidir',
            'C': 'Yeni görüş geriye yürümez; yayım tarihinden itibaren geçerlidir',
            'D': 'Yeni görüş önceki işlemlere de uygulanır',
            'E': 'Önceki işlem için sadece gecikme faizi alınır',
        },
        'C',
        "m. 369/2'ye göre yetkili makamların genel tebliğ veya sirkülerde değişiklik yaparak görüşünü değiştirmesi hâlinde **yeni görüş yayımlandığı tarihten itibaren geçerlidir ve geriye dönük uygulanamaz**; yargı mercilerince iptal edilen tebliğ ve sirkülerler bu hükmün dışındadır.",
        '213 sayılı VUK m. 369/2',
    ),
    # düzey 3
    '0011': patch(
        'Bir mükellef 2024 yılında fatura düzenlememiş (özel usulsüzlük) ve aynı yıl defterlerini tasdik ettirmemiştir (usulsüzlük). Bu fiiller için ceza en geç hangi yılların sonuna kadar kesilebilir?',
        {
            'A': 'İkisi için de 2026',
            'B': 'Fatura için 2026, tasdik için 2029',
            'C': 'Fatura için 2029, tasdik için 2026',
            'D': 'İkisi için de 2029',
            'E': 'Fatura için 2034, tasdik için 2027',
        },
        'C',
        "m. 374'e göre **m. 353 kapsamındaki özel usulsüzlüklerde** usulsüzlüğün yapıldığı yılı takip eden yılın birinci gününden başlayarak **beş yıl** (2025-2029), **usulsüzlükte** ise **iki yıl** (2025-2026) geçtikten sonra ceza kesilmez.",
        '213 sayılı VUK m. 374',
    ),
    # düzey 2
    '0012': patch(
        'Vergi cezalarında ceza kesme zamanaşımına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Usulsüzlükte süre fiilin yapıldığı yılı izleyen yılın başından işler',
            'B': 'Ceza ihbarnamesinin tebliği zamanaşımını kesmez',
            'C': 'Süre geçtikten sonra vergi cezası kesilmez',
            'D': 'Takdir komisyonuna başvuru ceza zamanaşımını da durdurur',
            'E': 'Birleşen vergi ziyaı ve usulsüzlük cezası vergi ziyaı süresi içinde kesilir',
        },
        'B',
        "m. 374'e göre **süreler içinde ceza ihbarnamesi tebliğ edilmekle zamanaşımı kesilmiş olur**. m. 336'ya göre birleşen cezalar vergi ziyaı süresinde kesilir; m. 114/2'deki durma hükmü ceza zamanaşımında da geçerlidir.",
        '213 sayılı VUK m. 374',
    ),
    # düzey 2
    '0013': patch(
        'Vergi mahkemesinde dava açma hakkına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Vergi dairesi takdir komisyonu kararlarına karşı dava açamaz',
            'B': 'Belediyede dava açma yetkisini gelir (varidat) müdürü kullanır',
            'C': 'Mükellefler tarh edilen vergilere karşı dava açabilir',
            'D': 'Mükellef beyan ettiği matraha kural olarak dava açamaz',
            'E': 'Kendisine ceza kesilen kişi cezaya karşı dava açabilir',
        },
        'A',
        "m. 377'ye göre mükellefler ve ceza muhatapları tarh edilen vergi ve kesilen cezalara karşı; **vergi dairesi de tadilat ve takdir komisyonlarınca tahmin ve takdir olunan matrahlara karşı** vergi mahkemesinde dava açabilir. m. 378/2'ye göre beyan edilen matraha kural olarak dava açılamaz.",
        '213 sayılı VUK m. 377',
    ),
    # düzey 3
    '0014': patch(
        "Bir vergi davasının açılma süresi, idari yargıda çalışmaya ara verme döneminde dolmaktadır. Ara verme 31 Ağustos'ta sona ermektedir. Dava en geç hangi tarihte açılabilir?",
        {
            'A': '30 Eylül',
            'B': '15 Eylül',
            'C': '1 Eylül',
            'D': '7 Eylül',
            'E': '31 Ağustos',
        },
        'D',
        "İYUK m. 8/3'e göre sürelerin bitmesi çalışmaya ara verme zamanına rastlarsa bu süreler, **ara vermenin sona erdiği günü izleyen tarihten itibaren yedi gün uzamış** sayılır: 1 Eylül birinci gün olmak üzere süre **7 Eylül**'de biter.",
        '2577 sayılı İYUK m. 8/3',
    ),
    # düzey 3
    '0015': patch(
        'Bir mükellef, vergi tarhiyatına karşı süresi içinde asliye hukuk mahkemesinde dava açmış; mahkeme görev yönünden davayı reddetmiş ve karar kesinleşmiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Vergi mahkemesindeki otuz günlük süre geçtiğinden idari yargıda dava açılamaz',
            'B': 'Mükellef ancak düzeltme yoluna başvurabilir',
            'C': 'Kesinleşmeyi izleyen günden itibaren otuz gün içinde vergi mahkemesinde dava açılabilir',
            'D': 'Asliye hukuk mahkemesine yeniden başvurulmalıdır',
            'E': 'Dava dosyası Danıştaya gönderilir',
        },
        'C',
        "İYUK m. 9'a göre idari yargının görevine giren hâlde adli yargı yerlerine açılan davaların görev noktasından reddi hâlinde, **kararın kesinleşmesini izleyen günden itibaren otuz gün içinde görevli mahkemede dava açılabilir**; görevsiz yargı merciine başvurma tarihi idari yargıya başvurma tarihi sayılır.",
        '2577 sayılı İYUK m. 9',
    ),
    # düzey 2
    '0016': patch(
        'Hukuka aykırı bir haciz işlemi nedeniyle zarara uğrayan mükellef, hem işlemin iptalini hem de zararının tazminini istemektedir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İptal ve tam yargı davalarını birlikte açabilir',
            'B': 'Önce iptal davası sonuçlanmadan tam yargı davası açamaz',
            'C': 'Tazminat için adli yargıya başvurmalıdır',
            'D': 'İptal davası açma hakkını kaybeder, tam yargı davası açar',
            'E': 'Tazminat istemi uzlaşma komisyonunca karara bağlanır',
        },
        'A',
        "İYUK m. 12'ye göre ilgililer haklarını ihlal eden bir idari işlem dolayısıyla **doğrudan tam yargı davası veya iptal ve tam yargı davalarını birlikte** açabilecekleri gibi, önce iptal davası açıp kararın tebliği üzerine dava süresi içinde tam yargı davası da açabilirler.",
        '2577 sayılı İYUK m. 12',
    ),
    # düzey 2
    '0017': patch(
        'Vergi mahkemesinde davalı idare, dava dilekçesine savunma vermek için süre uzatımı istemiş ve haklı sebep kabul edilmiştir. İdarenin savunma vermek için sahip olabileceği toplam süre en fazla kaç gündür?',
        {
            'A': '90',
            'B': '45',
            'C': '60',
            'D': '30',
            'E': '15',
        },
        'C',
        "İYUK m. 16/3'e göre taraflar tebliğden itibaren **otuz gün içinde** cevap verebilir; bu süre haklı sebeplerle mahkeme kararıyla **otuz günü geçmemek ve bir defaya mahsus olmak üzere** uzatılabilir: 30 + 30 = **60 gün**.",
        '2577 sayılı İYUK m. 16',
    ),
    # düzey 2
    '0018': patch(
        "Yürütmenin durdurulması isteminin reddine ilişkin vergi mahkemesi kararı 3 Mart'ta tebliğ edilmiştir. Bu karara en geç hangi tarihte itiraz edilebilir?",
        {
            'A': '8 Mart',
            'B': '10 Mart',
            'C': '13 Mart',
            'D': '18 Mart',
            'E': '2 Nisan',
        },
        'B',
        "İYUK m. 27/7'ye göre yürütmenin durdurulması istemleri hakkındaki kararlara **tebliğini izleyen günden itibaren yedi gün içinde bir defaya mahsus** itiraz edilebilir; itiraz mercii yedi gün içinde karar verir ve kararı kesindir: 4 Mart birinci gün olmak üzere son gün **10 Mart**'tır.",
        '2577 sayılı İYUK m. 27/7',
    ),
    # düzey 3
    '0019': patch(
        'Bölge idare mahkemesi, istinaf incelemesinde vergi mahkemesinin esasa ilişkin kararını maddi hukuka aykırı bulmuştur. Usule ilişkin bir eksiklik bulunmamaktadır. Bölge idare mahkemesi ne yapar?',
        {
            'A': 'Kararı onar, gerekçeyi değiştirir',
            'B': 'Kararı bozarak yeniden karar verilmek üzere dosyayı vergi mahkemesine gönderir',
            'C': 'Davayı düşürür',
            'D': 'Dosyayı Danıştaya gönderir',
            'E': 'Kararı kaldırır ve işin esası hakkında yeniden karar verir',
        },
        'E',
        "İYUK m. 45/4'e göre bölge idare mahkemesi ilk derece kararını hukuka uygun bulmazsa **istinaf başvurusunun kabulüyle kararın kaldırılmasına karar verir ve işin esası hakkında yeniden karar verir**. Dosyanın ilk derece mahkemesine gönderilmesi yalnız m. 45/5'te sayılan usul hâllerinde mümkündür.",
        '2577 sayılı İYUK m. 45/4',
    ),
    # düzey 2
    '0020': patch(
        'Vergi yargısında kanun yollarına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Temyiz istemleri Danıştay Başkanlığına hitaben dilekçeyle yapılır',
            'B': 'Parasal sınırı geçmeyen vergi davalarındaki ilk derece kararları kesindir',
            'C': 'İstinaf süresi kararın tebliğinden itibaren otuz gündür',
            'D': 'İstinaf başvurusu kararın yürütülmesini durdurur',
            'E': 'Kararı veren hâkim istinaf incelemesinde görev alamaz',
        },
        'D',
        "İYUK m. 52/1'e göre **temyiz veya istinaf yoluna başvurulmuş olması, kararların yürütülmesini durdurmaz**; ancak teminat karşılığında yürütmenin durdurulmasına karar verilebilir. Diğer ifadeler m. 45 ve 48'e uygundur.",
        '2577 sayılı İYUK m. 45-52',
    ),
    # düzey 2
    '0021': patch(
        "Mükellef aleyhine yapılmış bir vergi hatası düzeltilmiş ve iade edilecek tutarı gösteren düzeltme fişi mükellefe 5 Mart 2026'da tebliğ edilmiştir. Mükellef parasını geri almak için en geç ne zamana kadar başvurmalıdır?",
        {
            'A': '4 Nisan 2026',
            'B': '5 Mart 2027',
            'C': '5 Eylül 2026',
            'D': '31 Aralık 2026',
            'E': '5 Mart 2031',
        },
        'B',
        "m. 120'ye göre düzeltme fişi mükellefe tebliğ edilir ve mükellef **tebliğ tarihinden başlayarak bir yıl içinde** parasını geri almak üzere başvurmazsa hakkı düşer.",
        '213 sayılı VUK m. 120',
    ),
    # düzey 3
    '0022': patch(
        'Vergi mahkemesinden geçip kesinleşen bir tarhiyatta, mahkemenin incelemediği bir hesap hatası sonradan fark edilmiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Düzeltme için Danıştay'ın izni gerekir",
            'B': 'Hata, kanun yararına temyiz yoluyla düzeltilir',
            'C': 'Yargı mercii bu hata hakkında karar vermediğinden düzeltme yapılabilir',
            'D': 'Hata ancak yargılamanın yenilenmesiyle giderilir',
            'E': 'Kesinleşen yargı kararının bağlayıcılığı nedeniyle idare bu hatayı düzeltemez',
        },
        'C',
        "m. 125'e göre vergi mahkemesi, bölge idare mahkemesi ve Danıştaydan geçmiş muamelelerde vergi hataları bulunursa, **yargı kararları kesinleşmiş olsa bile** düzeltme yapılabilir; şu kadar ki **hatalar hakkında yargı mercilerince bir karar verilmemiş olması** şarttır.",
        '213 sayılı VUK m. 125',
    ),
    # düzey 3
    '0023': patch(
        'Uzlaşma görüşmesinde anlaşma sağlanamamış ve idarenin nihai teklifi tutanağa yazılmıştır. Mükellef birkaç gün sonra bu teklifi kabul etmek istemektedir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Dava açma süresi içinde teklifi yazılı kabul ederse uzlaşma sağlanmış sayılır',
            'B': 'Teklifi ancak vergi mahkemesi onaylarsa kabul edebilir',
            'C': 'Uzlaşma vaki olmadığından teklif kabul edilemez',
            'D': 'Yeniden uzlaşma talebinde bulunarak görüşmenin komisyonda tekrarlanmasını sağlamalıdır',
            'E': 'Kabul için bir yıl içinde başvurması gerekir',
        },
        'A',
        "Ek m. 1'e göre uzlaşmanın vaki olmaması hâlinde **yeniden uzlaşma talebinde bulunulamaz**; tutanağa idarenin nihai teklifi yazılır ve **mükellef dava açma süresinin sonuna kadar teklif edilen cezayı kabul ettiğini yazılı olarak bildirirse uzlaşma sağlanmış sayılır**.",
        '213 sayılı VUK ek m. 1',
    ),
    # düzey 3
    '0024': patch(
        'Vergi incelemesi sonunda talep edilen tarhiyat öncesi uzlaşmada anlaşma sağlanamamıştır. Ceza kesildikten sonra mükellef tarhiyat sonrası uzlaşma talep etmiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Mükellef şikâyet yoluyla Bakanlığa başvurmalıdır',
            'B': 'Tarhiyat sonrası uzlaşma talep edilemez; dava yolu açıktır',
            'C': 'Tarhiyat sonrası uzlaşma, ihbarname tebliğinden itibaren otuz gün içinde talep edilebilir',
            'D': 'Talep ancak ceza iki katına çıkarılarak kabul edilir',
            'E': 'Tarhiyat öncesi uzlaşma yeniden talep edilebilir',
        },
        'B',
        "Ek m. 11'e göre tarhiyat öncesi uzlaşmanın temin edilememesi veya uzlaşmaya varılamaması hâlinde mükellefler **cezanın kesilmesinden sonra uzlaşma talep edemezler**; genel hükümlere göre dava açma hakları saklıdır.",
        '213 sayılı VUK ek m. 11',
    ),
    # düzey 2
    '0025': patch(
        "İkmalen tarh edilen 100.000 ₺ vergi ve kesilen 100.000 ₺ vergi ziyaı cezası için mükellef, ihbarnamenin tebliğinden itibaren 30 gün içinde m. 376'ya göre başvurmuştur. Şartları yerine getirirse toplam kaç ₺ öder?",
        {
            'A': '200.000',
            'B': '225.000',
            'C': '175.000',
            'D': '150.000',
            'E': '100.000',
        },
        'D',
        "m. 376'ya göre mükellef, tarh edilen vergiyi ve cezaların yarısını vadesinde veya teminat göstererek vadenin bitiminden itibaren üç ay içinde ödeyeceğini **tebliğden itibaren otuz gün içinde** bildirirse **kesilen cezanın yarısı indirilir**: 100.000 + 50.000 = **150.000 ₺**.",
        '213 sayılı VUK m. 376',
    ),
    # düzey 3
    '0026': patch(
        "İzaha davet edilen mükellefin izahı yeterli bulunmamış; mükellef değerlendirme yazısının tebliğinden itibaren 30 gün içinde eksik beyanını düzeltip 50.000 ₺ vergiyi gecikme zammı oranında zamla ödemiştir. Kesilecek vergi ziyaı cezası kaç ₺'dir?",
        {
            'A': '10.000',
            'B': '25.000',
            'C': '0',
            'D': '50.000',
            'E': '15.000',
        },
        'A',
        "m. 370/a-2'ye göre izahın yeterli bulunmaması hâlinde, değerlendirme yazısının tebliğinden itibaren otuz gün içinde beyanın tamamlanması ve verginin gecikme zammı oranında zamla ödenmesi şartıyla **vergi ziyaı cezası, ziyaa uğratılan vergi üzerinden %20** oranında kesilir: 50.000 × %20 = **10.000 ₺**.",
        '213 sayılı VUK m. 370/a-2',
    ),
    # düzey 3
    '0027': patch(
        'Bir limited şirketin müdürü, şirket adına verilmesi gereken beyannameyi vermemiş ve vergi ziyaı doğmuştur. Ceza hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ceza doğrudan müdür adına kesilir',
            'B': 'Tüzel kişilere vergi cezası kesilemez',
            'C': 'Ceza, şirket ortakları adına sermaye payları oranında ayrı ayrı kesilir',
            'D': 'Ceza şirket ile müdüre ayrı ayrı iki kez kesilir',
            'E': 'Ceza şirket adına kesilir; tahsil edilemeyen kısım müdürden aranabilir',
        },
        'E',
        "m. 333'e göre tüzel kişilerin idaresinde vergi kanununa aykırı hareketlerden doğan **vergi cezaları tüzel kişiler adına kesilir**; kanuni temsilcilerin sorumluluğuna ilişkin **m. 10 hükmü vergi cezaları hakkında da uygulanır**, yani tüzel kişiden alınamayan ceza kanuni temsilcinin varlığından alınır.",
        '213 sayılı VUK m. 333',
    ),
    # düzey 2
    '0028': patch(
        'Vergi cezalarıyla kaçakçılık suçları arasındaki ilişkiye dair aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sahte belge kullanımında vergi ziyaı cezası üç kat uygulanır',
            'B': 'Vergi cezası kesilmesi kaçakçılık kovuşturmasına engel değildir',
            'C': 'Hapis cezası verilmesi vergi ziyaı cezası kesilmesine engel değildir',
            'D': 'Vergi ziyaı cezası ile hapis cezası tekerrür bakımından birleştirilir',
            'E': 'Pişmanlık şartlarına uygun bildirimde m. 359 uygulanmaz',
        },
        'D',
        "m. 340'a göre vergi ziyaı ve usulsüzlük cezaları ile m. 359'daki cezalar **içtima ve tekerrür hükümleri bakımından birleştirilemez**; vergi cezası kesilmesi m. 359'a göre takibata engel olmaz. m. 359 son fıkrası hapis cezasının vergi ziyaı cezasına engel olmadığını belirtir.",
        '213 sayılı VUK m. 340, 359, 344',
    ),
    # düzey 3
    '0029': patch(
        'Bir anonim şirket adına sahte fatura düzenlendiği tespit edilmiştir. Bu fiil için öngörülen hapis cezası kim hakkında hükmolunur?',
        {
            'A': 'Şirket tüzel kişiliği hakkında',
            'B': 'Şirketin denetçisi hakkında',
            'C': 'Fiili işleyen gerçek kişiler hakkında',
            'D': 'Bütün ortaklar hakkında',
            'E': 'Faturayı kullanan alıcı şirket hakkında',
        },
        'C',
        "m. 333/3'e göre m. 359'da yazılı fiillerin işlenmesi hâlinde bu fiiller için öngörülen cezalar **bu fiilleri işleyenler hakkında** hükmolunur; hapis cezası tüzel kişiye verilemez.",
        '213 sayılı VUK m. 333/3',
    ),
    # düzey 2
    '0030': patch(
        'Bir mükellef, vergi dairesinden aldığı yazılı özelgeye uygun hareket etmiş; özelgenin hatalı olduğu sonradan anlaşılmıştır. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Vergi de ceza da aranmaz',
            'B': 'Vergi aranmaz, sadece gecikme faizi alınır',
            'C': 'Özelge hatalı olduğundan vergi, ceza ve gecikme faizi birlikte aranır',
            'D': 'Vergi aranır; ceza kesilmez ve gecikme faizi hesaplanmaz',
            'E': 'Ceza yarı oranda kesilir',
        },
        'D',
        "m. 369/1'e göre **yetkili makamların mükellefe yazıyla yanlış izahat vermiş olmaları** hâlinde **vergi cezası kesilmez ve gecikme faizi hesaplanmaz**; ancak vergi aslı kanuna göre alınır.",
        '213 sayılı VUK m. 369/1',
    ),
    # düzey 2
    '0031': patch(
        "Aşağıdakilerden hangisi Vergi Usul Kanunu'na göre ceza ihbarnamesinde bulunması gereken bilgilerden biri değildir?",
        {
            'A': 'Varsa tekerrür ve içtima durumu',
            'B': 'Vergi cezasının hesabı ve miktarı',
            'C': 'Olayın izahı ve ilgili kanun maddeleri',
            'D': 'Uzlaşma komisyonunun görüşü',
            'E': 'Vergi mahkemesinde dava açma süresi',
        },
        'D',
        "m. 366'ya göre ceza ihbarnamesinde sıra numarası, tanzim tarihi, ilgilinin kimliği ve adresi, **olayın izahı**, dönem, **tekerrür ve içtima durumu**, **cezanın hesabı ve miktarı** ile **vergi mahkemesinde dava açma süresi** bulunur.",
        '213 sayılı VUK m. 366',
    ),
    # düzey 3
    '0032': patch(
        'Gelir İdaresi Başkanlığının belirlediği tutarı aşan bir davada vergi mahkemesi kararı vergi dairesi aleyhine sonuçlanmıştır. Vergi dairesinin kanun yoluna başvurması hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Muvafakat istinaf için aranır, temyiz için aranmaz',
            'B': "GİB'in muvafakatini almadan temyize gidemez",
            'C': 'Kanun yoluna başvurması yasaktır',
            'D': 'Defterdarın onayıyla temyize gidebilir',
            'E': 'Önce uzlaşma komisyonuna başvurmalıdır',
        },
        'B',
        "m. 377/4'e göre vergi dairesi başkanlıkları ve vergi daireleri, **GİB'in belirlediği tutarları aşan davalarda GİB'in (il özel idareleri ve belediyelerde valinin) muvafakatini almadan** vergi mahkemesi kararları aleyhine temyiz yoluna gidemez; GİB bu yetkiyi belirli hadlerle devredebilir.",
        '213 sayılı VUK m. 377/4',
    ),
    # düzey 2
    '0033': patch(
        "Vergi/ceza ihbarnamesi 10 Nisan'da tebliğ edilen mükellef, vergi mahkemesinde en geç hangi tarihte dava açabilir? (Son günün tatile rastlamadığı varsayılsın.)",
        {
            'A': '9 Mayıs',
            'B': '25 Nisan',
            'C': '11 Mayıs',
            'D': '10 Haziran',
            'E': '10 Mayıs',
        },
        'E',
        "İYUK m. 7'ye göre dava açma süresi **vergi mahkemelerinde otuz gündür** ve tebliği **izleyen günden** başlar: 11 Nisan birinci gün olmak üzere 30. gün **10 Mayıs**'tır.",
        '2577 sayılı İYUK m. 7',
    ),
    # düzey 3
    '0034': patch(
        'Bir kişi, idari davaya konu olabilecek bir işlem yapılması için idareye başvurmuş; idare otuz gün içinde kesin olmayan bir cevap vermiştir. Kişi kesin cevabı beklemeyi tercih etmiştir. Bekleme süresi en fazla ne kadardır?',
        {
            'A': 'Başvuru tarihinden itibaren dört ay',
            'B': 'Başvuru tarihinden itibaren altı ay',
            'C': 'Süre sınırı yoktur',
            'D': 'Kesin olmayan cevaptan itibaren altmış gün',
            'E': 'Başvuru tarihinden itibaren bir yıl',
        },
        'A',
        "İYUK m. 10'a göre otuz gün içinde cevap verilmezse istek reddedilmiş sayılır. Otuz gün içinde verilen cevap kesin değilse ilgili kesin cevabı bekleyebilir; bu takdirde dava süresi işlemez, ancak **bekleme süresi başvuru tarihinden itibaren dört ayı geçemez** (7331 ile altı aydan dört aya indirildi).",
        '2577 sayılı İYUK m. 10 (7331 sayılı Kanunla değişik)',
    ),
    # düzey 2
    '0035': patch(
        'İdari yargının denetim yetkisine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Mahkeme idarenin takdir yetkisini kaldıracak biçimde karar veremez',
            'B': 'İdari yargı yetkisi hukuka uygunluk denetimiyle sınırlıdır',
            'C': 'Mahkeme işlemin yerindeliğini denetleyerek idare yerine yeni işlem kurabilir',
            'D': 'İptal davası yetki, şekil, sebep, konu veya maksat yönünden açılır',
            'E': 'Tam yargı davası kişisel hakları doğrudan zarar görenlerce açılır',
        },
        'C',
        "İYUK m. 2/2'ye göre idari yargı yetkisi **idari eylem ve işlemlerin hukuka uygunluğunun denetimiyle sınırlıdır**; idari mahkemeler **yerindelik denetimi yapamaz** ve idari işlem niteliğinde veya takdir yetkisini kaldıracak biçimde karar veremez.",
        '2577 sayılı İYUK m. 2',
    ),
    # düzey 3
    '0036': patch(
        'Vergi mahkemesine verilen dilekçede uyuşmazlık konusu miktar gösterilmemiştir. İlk inceleme sonucunda mahkeme ne karar verir?',
        {
            'A': 'Davanın esastan reddine',
            'B': 'Dosyanın Danıştaya gönderilmesine',
            'C': 'Eksikliğin duruşmada tamamlanmasına',
            'D': 'Otuz gün içinde yeniden düzenlenmek üzere dilekçenin reddine',
            'E': 'Eksik dilekçe süresinde verilmiş sayılmadığından davanın süre aşımından reddine',
        },
        'D',
        "İYUK m. 15/1-d'ye göre m. 3'e uygun olmayan dilekçeler için **otuz gün içinde m. 3 ve 5'e uygun şekilde yeniden düzenlenmek üzere dilekçenin reddine** karar verilir; yeni dilekçe için ayrıca harç alınmaz, aynı yanlışlık tekrarlanırsa dava reddedilir.",
        '2577 sayılı İYUK m. 15/1-d',
    ),
    # düzey 3
    '0037': patch(
        'Aşağıdaki davalardan hangilerinin açılması tahsil işlemini kendiliğinden durdurur?\n\nI. İkmalen tarh edilen vergiye karşı açılan dava\n\nII. İhtirazi kayıtla verilen beyanname üzerine tahakkuk eden vergiye karşı açılan dava\n\nIII. Tahsilat işlemlerinden dolayı açılan dava',
        {
            'A': 'Yalnız I',
            'B': 'Yalnız II',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'I ve II',
        },
        'A',
        "İYUK m. 27/4'e göre vergi davasının açılması tarh edilen vergilerin tahsilini durdurur (I). Ancak **ihtirazi kayıtla verilen beyannameler üzerine yapılan işlemlerle tahsilat işlemlerinden dolayı açılan davalar tahsil işlemini durdurmaz**; bunlar için yürütmenin durdurulması istenebilir.",
        '2577 sayılı İYUK m. 27/4',
    ),
    # düzey 2
    '0038': patch(
        'Yürütmenin durdurulmasına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İstem yerinde değilse savunma alınmadan reddedilebilir',
            'B': 'Yürütmenin durdurulması kararı verilen dosyalar öncelikle incelenir',
            'C': 'Adli yardımdan yararlanan davacıdan teminat alınması zorunludur',
            'D': 'Yürütmenin durdurulmasına dair kararlar on beş gün içinde yazılır',
            'E': 'Aynı sebeplere dayanılarak ikinci kez istemde bulunulamaz',
        },
        'C',
        "İYUK m. 27/6'ya göre yürütmenin durdurulması kararları teminat karşılığında verilir; ancak durumun gereğine göre teminat aranmayabilir ve **idareden ve adli yardımdan faydalanan kimselerden teminat alınmaz**.",
        '2577 sayılı İYUK m. 27',
    ),
    # düzey 2
    '0039': patch(
        'Vergi mahkemesi mükellef lehine karar vermiş ve karar idareye tebliğ edilmiştir. İdare kararın gereğini en geç ne kadar sürede yerine getirmelidir?',
        {
            'A': 'Karar kesinleşinceye kadar bekleyerek',
            'B': 'Tebliğden itibaren otuz gün içinde',
            'C': 'Tebliğden itibaren on beş gün içinde',
            'D': 'Bir sonraki mali yıl içinde',
            'E': 'Tebliğden itibaren altmış gün içinde',
        },
        'B',
        "İYUK m. 28/1'e göre idare, mahkemelerin esasa ve yürütmenin durdurulmasına ilişkin kararlarının gereğine göre gecikmeksizin işlem tesis etmeye mecburdur; bu süre **kararın idareye tebliğinden başlayarak otuz günü geçemez**.",
        '2577 sayılı İYUK m. 28',
    ),
    # düzey 3
    '0040': patch(
        'Mükellef lehine verilen ve istinaf incelemesinden geçmeden kesinleşen bir vergi mahkemesi kararı, Danıştay Başsavcısının başvurusu üzerine kanun yararına bozulmuştur. Mükellefin durumu hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Mükellefin kazandığı hak ortadan kalkar',
            'B': 'Mükellef bozma kararına itiraz etmelidir',
            'C': 'Bozma, kesinleşmiş kararın hukuki sonuçlarını kaldırmaz',
            'D': 'Vergi yeniden tarh edilir',
            'E': 'Dava yeniden görülür',
        },
        'C',
        "İYUK m. 51'e göre kesin olarak verilen veya istinaf ya da temyizden geçmeden kesinleşen kararlar, ilgili bakanlıkların göstereceği lüzum üzerine veya kendiliğinden **Başsavcı tarafından kanun yararına temyiz** edilebilir; **bu bozma kararı, daha önce kesinleşmiş kararın hukuki sonuçlarını kaldırmaz**.",
        '2577 sayılı İYUK m. 51',
    ),
    # düzey 3
    '0041': patch(
        'Vergi dairesi, beyannamedeki açık bir toplama hatasını kendiliğinden düzeltmiş ve bu düzeltme mükellef aleyhine vergi farkı doğurmuştur. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Açık hatalar ancak mükellef talebiyle düzeltilebilir',
            'B': 'Mükellef bu düzeltmeye karşı vergi mahkemesinde dava açabilir',
            'C': "Re'sen düzeltmeye karşı dava açılamaz",
            'D': 'Mükellef dava açmadan önce Bakanlığa şikâyet yoluyla başvurmalıdır',
            'E': 'Düzeltme için mükellefin onayı gerekir',
        },
        'B',
        "m. 121'e göre **idarece tereddüt edilmeyen açık ve mutlak vergi hataları re'sen düzeltilir**; kendi aleyhlerine düzeltme yapılan kimselerin **düzeltmeye karşı vergi mahkemesinde dava açma hakları saklıdır**.",
        '213 sayılı VUK m. 121',
    ),
    # düzey 3
    '0042': patch(
        'İkmalen tarh edilen vergi ve kesilen vergi ziyaı cezası için tarhiyat sonrası uzlaşma talep eden mükellef, hem vergi aslını hem cezayı müzakere etmek istemektedir. 7524 sayılı Kanun sonrası aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Uzlaşma, vergi ziyaı cezasıyla sınırlı olarak yapılabilir',
            'B': 'Uzlaşma gecikme faizi için yapılır',
            'C': 'Uzlaşma vergi aslı ve ceza üzerinde birlikte yapılır',
            'D': 'Tarhiyat sonrası uzlaşma kaldırılmıştır',
            'E': 'Uzlaşma vergi aslıyla sınırlı yapılır',
        },
        'A',
        "7524 sayılı Kanunla değişen ek m. 1'e göre uzlaşma, ikmalen, re'sen veya idarece tarh edilen vergilere ilişkin **vergi ziyaı cezaları** ile kanunda belirtilen tutarı aşan **usulsüzlük ve özel usulsüzlük cezalarının** tahakkuk edecek miktarları konusunda yapılır. **Vergi aslı artık uzlaşma konusu değildir** (yürürlük 2/8/2024).",
        '213 sayılı VUK ek m. 1 (7524 sayılı Kanunla değişik)',
    ),
    # düzey 3
    '0043': patch(
        'Uzlaşma talep eden bir mükellef, tutanak imzalanmadan önce fikrini değiştirmiş ve cezalarda indirimden (m. 376) yararlanmak istemiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Uzlaşma talep eden mükellef, talebinden vazgeçse bile m. 376'dan yararlanamaz",
            'B': 'Önce uzlaşma sonuçlanmalı, sonra indirim uygulanır',
            'C': 'Uzlaşılan cezaya ayrıca m. 376 indirimi de uygulanır',
            'D': 'İndirim için yeniden ihbarname düzenlenir',
            'E': 'Tutanak imzalanıncaya kadar uzlaşmadan vazgeçip indirimi isteyebilir',
        },
        'E',
        "Ek m. 9'a göre uzlaşılan cezalar hakkında **başkaca bir indirim uygulanmaz**; m. 376 uygulanan cezalar için de uzlaşma yapılmaz. Ancak mükellefin **uzlaşma tutanağını imzalayıncaya kadar uzlaşma talebinden vazgeçerek m. 376'nın uygulanmasını isteme hakkı saklıdır**.",
        '213 sayılı VUK ek m. 9',
    ),
    # düzey 2
    '0044': patch(
        'Tarhiyat sonrası uzlaşmaya ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Mükellef görüşmede bir meslek mensubu bulundurabilir',
            'B': 'Uzlaşma tutanakları kesindir ve vergi dairesince derhal yerine getirilir',
            'C': 'Uzlaşılan ceza tutarına karşı vergi mahkemesinde dava açılabilir',
            'D': 'Uzlaşma vaki olmazsa yeniden uzlaşma talep edilemez',
            'E': 'Uzlaşma vaki olmadığına dair tutanağa idarenin nihai teklifi yazılır',
        },
        'C',
        "Ek m. 6'ya göre uzlaşma tutanakları kesindir; **mükellef, üzerinde uzlaşılan ve tutanakla tespit edilen hususlar hakkında dava açamaz ve hiçbir mercie şikâyette bulunamaz**. Diğer ifadeler ek m. 1'e uygundur.",
        '213 sayılı VUK ek m. 1, 6',
    ),
    # düzey 3
    '0045': patch(
        "Vergi aslına bağlı olmaksızın kesilen 20.000 ₺'lik bir usulsüzlük cezası, uzlaşma için kanunda öngörülen tutarı aşmamaktadır. Mükellef süresinde m. 376'ya göre başvurup şartları yerine getirirse kaç ₺ öder?",
        {
            'A': '6.667',
            'B': '5.000',
            'C': '15.000',
            'D': '10.000',
            'E': '20.000',
        },
        'B',
        "Ek m. 1'e göre uzlaşma için öngörülen tutarı aşmayan usulsüzlük ve özel usulsüzlük cezaları için **m. 376'daki indirim oranı %50 artırımlı** uygulanır: %50 × 1,5 = **%75** indirim. 20.000 × %25 = **5.000 ₺** ödenir.",
        '213 sayılı VUK ek m. 1, m. 376',
    ),
    # düzey 3
    '0046': patch(
        'Kendisine izaha davet yazısı tebliğ edilen mükellef, davet konusu tespitle ilgili olarak pişmanlık dilekçesi vermiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Pişmanlıktan yararlanır ve ceza kesilmez',
            'B': 'Davet konusu tespit için pişmanlıktan yararlanamaz',
            'C': 'Pişmanlık dilekçesi izaha daveti ortadan kaldırır',
            'D': 'Hem izaha davet hem pişmanlık hükümleri birlikte uygulanır',
            'E': 'Pişmanlık zammı yerine gecikme faizi uygulanır',
        },
        'B',
        "m. 370/a'ya göre kendisine izaha davet yazısı tebliğ edilen mükellefler, **davet konusu tespitle sınırlı olarak m. 371'deki pişmanlık hükümlerinden yararlanamaz**.",
        '213 sayılı VUK m. 370',
    ),
    # düzey 2
    '0047': patch(
        'Velayet altındaki bir çocuğa miras kalan dükkânın kira geliri için beyannameyi veli süresinde vermemiştir. Usulsüzlük cezası kime kesilir?',
        {
            'A': 'Çocuğa',
            'B': 'Kiracıya',
            'C': 'Çocuk ile veliye müteselsilen',
            'D': 'Ceza kesilmez',
            'E': 'Veliye',
        },
        'E',
        "m. 332'ye göre velayet ve vesayet altında bulunanlar, kendilerine izafeten **veli, vasi veya kayyımın vergi kanunlarına aykırı hareketlerinden dolayı cezaya muhatap tutulmaz**; bu hâllerde cezanın muhatabı veli, vasi veya kayyımdır.",
        '213 sayılı VUK m. 332',
    ),
    # düzey 2
    '0048': patch(
        "Bir mükellef tek bir fiille hem 30.000 ₺ gelir vergisi hem 20.000 ₺ katma değer vergisi ziyaına sebebiyet vermiştir. Fiil m. 359 kapsamında değildir. Kesilecek toplam vergi ziyaı cezası kaç ₺'dir?",
        {
            'A': '100.000',
            'B': '150.000',
            'C': '50.000',
            'D': '20.000',
            'E': '30.000',
        },
        'C',
        "m. 335'e göre vergi ziyaı cezasını gerektiren **tek bir fiil ile başka neviden birkaç vergi ziyaa uğramışsa her vergi bakımından ayrı ayrı ceza** kesilir; ceza ziyaa uğratılan verginin bir katıdır: 30.000 + 20.000 = **50.000 ₺**. Yalnız en ağırının kesilmesi m. 336'da vergi ziyaı ile usulsüzlüğün birleştiği durum içindir.",
        '213 sayılı VUK m. 335',
    ),
    # düzey 3
    '0049': patch(
        'Cumhuriyet başsavcılığı, bir mükellefin sahte belge kullandığını basın haberlerinden öğrenmiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Olayı vergi mahkemesine bildirmekle yetinir',
            'B': 'Konuyu uzlaşma komisyonuna gönderir',
            'C': 'Doğrudan kamu davası açar',
            'D': 'Vergi dairesinden inceleme ister; dava inceleme sonucuna bağlıdır',
            'E': 'Mükellefin yazılı rızasını alarak vergi incelemesini beklemeden soruşturma başlatır',
        },
        'D',
        "m. 367'ye göre m. 359'daki suçların işlendiğini sair suretlerle öğrenen Cumhuriyet başsavcılığı **hemen ilgili vergi dairesini haberdar ederek inceleme yapılmasını talep eder**; **kamu davasının açılması, inceleme neticesinin başsavcılığa bildirilmesine talik olunur**.",
        '213 sayılı VUK m. 367',
    ),
    # düzey 2
    '0050': patch(
        'Hakkında vergi ziyaı cezası kesilen mükellef, ceza ödenmeden vefat etmiştir; mirasçılar mirası reddetmemiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ceza düşer; vergi aslı mirasçılardan aranabilir',
            'B': 'Vergi aslı da ölümle düşer',
            'C': 'Ceza ancak kesinleşmemişse düşer',
            'D': 'Ceza ve vergi mirasçılardan aranır',
            'E': 'Ceza yarı oranda mirasçılardan alınır',
        },
        'A',
        "m. 372'ye göre **ölüm hâlinde vergi cezası düşer**. Vergi borcu ise m. 12 uyarınca mirası reddetmemiş kanuni ve mansup mirasçılara geçer.",
        '213 sayılı VUK m. 372',
    ),
    # düzey 2
    '0051': patch(
        'Aşağıdakilerden hangileri vergi cezası kesilmesini engeller veya kesilen cezayı ortadan kaldırır?\n\nI. Mükellefin iflas etmesi\n\nII. Mükellefin ölmesi\n\nIII. Mücbir sebebin varlığının ispat edilmesi',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız III',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'Yalnız II',
        },
        'C',
        "m. 372'ye göre **ölüm hâlinde vergi cezası düşer**; m. 373'e göre **mücbir sebeplerden birinin vukuu malum ise veya ispat olunursa vergi cezası kesilmez**. İflas hâlinde m. 162'ye göre mükellefiyet vergiyle ilgili işlemler bitinceye kadar sürer; iflas cezayı ortadan kaldırmaz.",
        '213 sayılı VUK m. 372, 373',
    ),
    # düzey 3
    '0052': patch(
        'Bir şirket, yapacağı serbest meslek ödemesinden stopaj kesintisi hesaplamış ancak ödemeyi henüz yapmamıştır. Serbest meslek erbabı bu kesintiye karşı dava açmak istemektedir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Dava ancak şirket tarafından açılabilir',
            'B': 'Kesinti hesaplandığı anda, ödeme beklenmeden dava açılabilir',
            'C': 'Kesintiye karşı dava yolu kapalıdır',
            'D': 'Önce uzlaşma talep edilmesi zorunludur',
            'E': 'Ödeme yapılıp vergi kesilmeden dava açılamaz',
        },
        'E',
        "m. 378/1'e göre dava açabilmek için verginin tarh edilmiş, cezanın kesilmiş olması; **tevkif yoluyla alınan vergilerde ise istihkak sahiplerine ödemenin yapılmış ve ödemeyi yapan tarafından verginin kesilmiş olması** gerekir. İYUK m. 7'ye göre dava süresi ödemeyi izleyen gün başlar.",
        '213 sayılı VUK m. 378/1',
    ),
    # düzey 2
    '0053': patch(
        'İdari yargıda dava sürelerine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Vergi mahkemelerinde dava açma süresi altmış gündür',
            'B': 'Tahakkuku tahsile bağlı vergilerde süre tahsilatı izleyen gün başlar',
            'C': 'Tevkif yoluyla alınan vergilerde süre ödemeyi izleyen gün başlar',
            'D': 'Son gün tatile rastlarsa süre izleyen iş gününün bitimine kadar uzar',
            'E': 'Tatil günleri sürelere dâhildir',
        },
        'A',
        "İYUK m. 7'ye göre dava açma süresi özel kanunlarında ayrı süre gösterilmeyen hâllerde **Danıştay ve idare mahkemelerinde altmış, vergi mahkemelerinde otuz gündür**. m. 7/2 başlangıç anlarını, m. 8 tatil kurallarını düzenler.",
        '2577 sayılı İYUK m. 7, 8',
    ),
    # düzey 3
    '0054': patch(
        'Otuz günlük dava açma süresinin 12. gününde üst makama başvurarak işlemin kaldırılmasını isteyen mükellefin başvurusu reddedilmiş ve ret kararı tebliğ edilmiştir. Mükellefin dava açmak için kaç günü kalmıştır?',
        {
            'A': '15',
            'B': '18',
            'C': '60',
            'D': '12',
            'E': '30',
        },
        'B',
        "İYUK m. 11'e göre üst makama başvurma, **işlemeye başlamış olan dava açma süresini durdurur**; isteğin reddedilmesi hâlinde dava açma süresi **yeniden işlemeye başlar ve başvurma tarihine kadar geçmiş süre de hesaba katılır**: 30 − 12 = **18 gün**.",
        '2577 sayılı İYUK m. 11',
    ),
    # düzey 2
    '0055': patch(
        'Aşağıdakilerden hangileri vergi davası dilekçesinde gösterilmesi gereken bilgilerdendir?\n\nI. Davanın ilgili bulunduğu verginin nevi ve yılı\n\nII. Tebliğ edilen ihbarnamenin tarihi ve numarası\n\nIII. Davacının son üç yıllık beyan ettiği matrahlar',
        {
            'A': 'Yalnız I',
            'B': 'II ve III',
            'C': 'I, II ve III',
            'D': 'I ve II',
            'E': 'Yalnız II',
        },
        'D',
        "İYUK m. 3/2-e'ye göre vergi davalarında dilekçede **verginin veya vergi cezasının nevi ve yılı, tebliğ edilen ihbarnamenin tarihi ve numarası** ve varsa mükellef hesap numarası gösterilir; ayrıca uyuşmazlık konusu miktar da belirtilir. Önceki yılların matrahları istenmez.",
        '2577 sayılı İYUK m. 3',
    ),
    # düzey 2
    '0056': patch(
        'Bir vergi davasında mahkeme, tarafların dosyaya sunmadığı banka kayıtlarını ilgili bankadan istemiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Belgeler ancak bilirkişi aracılığıyla istenebilir',
            'B': "Mahkeme gerekli bilgi ve belgeleri re'sen isteyebilir",
            'C': 'Bu işlem için davacının onayı gerekir',
            'D': 'Mahkeme ancak taraflarca sunulan delillerle bağlıdır',
            'E': 'Mahkeme bu belgeleri isteyemez; dava reddedilir',
        },
        'B',
        "İYUK m. 20'ye göre mahkemeler **bakmakta oldukları davalara ait her türlü incelemeyi kendiliğinden yapar**; lüzum gördükleri evrakın gönderilmesini ve bilgilerin verilmesini taraflardan ve **ilgili diğer yerlerden** isteyebilirler (re'sen araştırma ilkesi).",
        '2577 sayılı İYUK m. 20',
    ),
    # düzey 3
    '0057': patch(
        "Adına 100.000 ₺ vergi tarh edilen mükellef, bu tutarın 40.000 ₺'lik kısmına karşı vergi mahkemesinde dava açmıştır. Dava açılması nedeniyle tahsil işlemi durdurulan tutar kaç ₺'dir?",
        {
            'A': '100.000',
            'B': '60.000',
            'C': '20.000',
            'D': '0',
            'E': '40.000',
        },
        'E',
        "İYUK m. 27/4'e göre vergi mahkemelerinde dava açılması, tarh edilen vergi ve cezaların **dava konusu edilen bölümünün** tahsil işlemlerini durdurur: **40.000 ₺**. Dava konusu yapılmayan 60.000 ₺ kesinleşir ve tahsil edilir.",
        '2577 sayılı İYUK m. 27/4',
    ),
    # düzey 2
    '0058': patch(
        'Vergi mahkemesinin, istinaf sınırını aşan bir davada verdiği karara karşı mükellef hangi kanun yoluna, ne kadar sürede başvurabilir?',
        {
            'A': 'Bölge idare mahkemesine, tebliğden itibaren otuz gün içinde istinaf',
            'B': 'Bölge idare mahkemesine, on beş gün içinde itiraz',
            'C': "Danıştay'a, kararın tebliğinden itibaren otuz gün içinde doğrudan temyiz yoluyla",
            'D': 'Vergi mahkemesine, yedi gün içinde karar düzeltme',
            'E': 'Anayasa Mahkemesine, altmış gün içinde bireysel başvuru',
        },
        'A',
        "İYUK m. 45'e göre idare ve vergi mahkemelerinin kararlarına karşı **mahkemenin bulunduğu yargı çevresindeki bölge idare mahkemesine, kararın tebliğinden itibaren otuz gün içinde istinaf** yoluna başvurulabilir; kanunda belirtilen parasal sınırı geçmeyen vergi davalarındaki kararlar kesindir.",
        '2577 sayılı İYUK m. 45',
    ),
    # düzey 3
    '0059': patch(
        "Danıştay'ın bozma kararına uymayan bölge idare mahkemesi önceki kararında ısrar etmiştir. Israr kararı temyiz edilirse aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Uyuşmazlık Mahkemesine gönderilir',
            'B': 'Israr kararı kesindir, temyiz edilemez',
            'C': 'Vergi Dava Daireleri Kurulunca incelenir ve kararına uyulması zorunludur',
            'D': 'Anayasa Mahkemesince incelenir',
            'E': 'Aynı Danıştay dairesince yeniden incelenir',
        },
        'C',
        "İYUK m. 50'ye göre bölge idare mahkemesi bozmaya uymayıp kararında ısrar ederse, ısrar kararının temyizi hâlinde talep konusuna göre **Danıştay İdari veya Vergi Dava Daireleri Kurulunca** incelenir; **bu kurulların kararlarına uyulması zorunludur**.",
        '2577 sayılı İYUK m. 50',
    ),
    # düzey 2
    '0060': patch(
        'Karara esas alınan bir belgenin sahte olduğu, karar kesinleştikten sonra verilen bir mahkeme kararıyla belirlenmiş ve istemde bulunacak taraf bunu öğrenmiştir. Yargılamanın yenilenmesi kaç gün içinde istenebilir?',
        {
            'A': '105',
            'B': '100',
            'C': '365',
            'D': '60',
            'E': '90',
        },
        'D',
        "İYUK m. 53/3'e göre yargılamanın yenilenmesi süresi, (h) bendi için on yıl, AİHM kararına dayanan (ı) bendi için bir yıl, **diğer sebepler için altmış gündür**; süre, dayanılan sebebin istemde bulunan yönünden gerçekleştiği tarihi izleyen günden başlar.",
        '2577 sayılı İYUK m. 53',
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
    print(f"1 paket / {len(PATCHES)} soru ('Vergi Cezalari ve Uyusmazliklar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
