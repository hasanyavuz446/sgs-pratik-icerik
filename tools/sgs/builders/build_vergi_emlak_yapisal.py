#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Emlak Vergisi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Vergiye ozgu profille yeniden yazim: bina ve arazi vergisinin konusu ve mukellefi, daimi ve gecici muafliklar, oranlar ve buyuksehir artirimi, mukellefiyetin baslamasi ve sona ermesi, bildirim, vergi degeri (7566 sonrasi), odeme ve kisitli tasinmaz, vergi degerini tadil eden sebepler, degerli konut vergisi. Yila bagli esik ve tutar sorulmadi; 16 hesap sorusu bagimsiz dogrulandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 1319 sayili Emlak Vergisi Kanunu guncel metni (7566 degisikligi dahil; mevzuat.gov.tr)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/vergi_hukuku/emlak_vergisi.json"
STYLE_REF = 'SGS Vergi Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "emlak-gen-"


def patch(stem, options, answer, solution, ref='1319 sayili Emlak Vergisi Kanunu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Aşağıdakilerden hangisi Emlak Vergisi Kanunu'na göre bina vergisi bakımından bina sayılmaz?",
        {
            'A': 'Ahşap yazlık ev',
            'B': 'Su üzerinde sabit olarak inşa edilmiş restoran',
            'C': 'Betonarme depo',
            'D': 'Araca takılıp çekilebilen seyyar ev',
            'E': 'Zemine sabitlenmiş prefabrik ofis',
        },
        'D',
        "m. 2'ye göre bina tabiri, yapıldığı madde ne olursa olsun **karada veya su üzerindeki sabit inşaatın** hepsini kapsar. **Yüzer havuzlar, diğer yüzer yapılar, çadırlar ve nakil vasıtalarına takılıp çekilebilen seyyar evler** bina sayılmaz.",
        '1319 sayılı Emlak Vergisi Kanunu m. 2',
    ),
    # düzey 3
    '0002': patch(
        'Bir belediyeye ait bina bir şirkete kiraya verilmiştir. Binanın bina vergisi muaflığı hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kira gelirinin yarısı oranında vergi alınır',
            'B': 'Vergiyi kiracı şirket öder',
            'C': 'Muaflık kira süresince askıya alınır',
            'D': 'Muaflık devam eder; belediye binalarında kiraya verilmeme şartı aranmaz',
            'E': 'Kiraya verildiği için muaflık kalkar; vergi, kiranın başladığı yılı izleyen yıldan alınır',
        },
        'D',
        "m. 4'e göre daimi muaflıklar kural olarak **kiraya verilmemek şartıyla** tanınır; ancak **(a), (b), (s), (y) ve (z) bentleri** için bu şart aranmaz. Belediyelere ait binalar (a) bendindedir; kiraya verilse de muaflık devam eder.",
        '1319 sayılı Emlak Vergisi Kanunu m. 4',
    ),
    # düzey 2
    '0003': patch(
        'Aşağıdaki binalardan hangileri, kiraya verilmedikleri sürece bina vergisinden daimi olarak muaftır?\n\nI. Kamu yararına çalışan derneğin binası\n\nII. Umuma açık ibadethane\n\nIII. Kazanç amacı güden özel okulun binası',
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'Yalnız II',
        },
        'B',
        "m. 4'e göre kamu menfaatine yararlı derneklere ait binalar (e) ve **umuma açık ibadethaneler** (g) daimi muaftır. Hastane, yurt, kreş gibi yerler için muaflık (f) **kazanç gayesi olmamak şartıyla** tanınır; kazanç amacı güden özel okul bu kapsamda değildir.",
        '1319 sayılı Emlak Vergisi Kanunu m. 4',
    ),
    # düzey 1
    '0004': patch(
        'Gençlik ve Spor Bakanlığına tescilli bir amatör spor kulübüne ait bina, kulübün kendi faaliyetleri için kullanılmaktadır. Bu bina bina vergisi bakımından nasıl değerlendirilir?',
        {
            'A': 'Daimi olarak muaftır',
            'B': 'Yarı oranda vergilenir',
            'C': 'Vergiye tabidir',
            'D': 'Beş yıl geçici muaftır',
            'E': 'Arazi vergisine tabidir',
        },
        'A',
        "m. 4/o'ya göre Bakanlığa tescilli **amatör spor kulüplerine ait binalar**, gelir veya kurumlar vergisine tabi işletmelere ait olmamaları veya bunlara tahsis edilmemeleri şartıyla daimi muaftır.",
        '1319 sayılı Emlak Vergisi Kanunu m. 4/o',
    ),
    # düzey 3
    '0005': patch(
        'Geçici muaflıktan yararlanan yeni bir daire, muaflığın ikinci yılında satılmış ve alıcı tarafından mesken olarak kullanılmaya devam edilmiştir. Muaflık hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Muaflık satıcıda kalır',
            'B': 'Muaflık, alıcının tapu tescil tarihinden itibaren yeniden beş yıl işler',
            'C': 'Satışla birlikte muaflık sona erer',
            'D': 'Muaflık yarı oranda devam eder',
            'E': 'Kalan süre için muaflık alıcı yönünden devam eder',
        },
        'E',
        "m. 5/a'ya göre bu binaların, mesken olarak kullanılması şartıyla **satın alma veya diğer yollarla iktisap edilmesi** hâlinde de muaflık hükmü **kalan süre için** uygulanır.",
        '1319 sayılı Emlak Vergisi Kanunu m. 5/a',
    ),
    # düzey 1
    '0006': patch(
        'Turizm müessesesi belgesi alan bir otelin binası, belgenin alındığı yılı takip eden bütçe yılından itibaren kaç yıl geçici muaflıktan yararlanır?',
        {
            'A': '10',
            'B': '7',
            'C': '8',
            'D': '15',
            'E': '5',
        },
        'E',
        "m. 5/b'ye göre turizm müessesesi belgesi almış gelir veya kurumlar vergisi mükelleflerinin bu maksatlara tahsis ettikleri binalar, inşaatın bittiği veya belgenin alındığı yılı takip eden bütçe yılından itibaren **beş yıl** geçici muaftır.",
        '1319 sayılı Emlak Vergisi Kanunu m. 5/b',
    ),
    # düzey 2
    '0007': patch(
        'Bir fabrikanın bina vergisi matrahı belirlenirken binaya bağlı sabit üretim tesisatının değeri nasıl dikkate alınır?',
        {
            'A': 'Vergi matrahına alınmaz',
            'B': 'Ayrıca arazi vergisine tabi tutulur',
            'C': 'Yarısı matraha eklenir',
            'D': 'Amortisman düşülerek eklenir',
            'E': 'Vergi matrahına tamamen eklenir',
        },
        'A',
        "m. 7'ye göre bina vergisinin matrahı binanın vergi değeridir; **sabit istihsal tesisatına ait değerler vergi matrahına alınmaz**.",
        '1319 sayılı Emlak Vergisi Kanunu m. 7',
    ),
    # düzey 2
    '0008': patch(
        "Yeni inşa edilen bir binanın inşaatı Mart 2026'da tamamlanmıştır. Bu binanın bina vergisi mükellefiyeti ne zaman başlar?",
        {
            'A': '1 Ocak 2028',
            'B': '1 Temmuz 2026',
            'C': '1 Ocak 2027',
            'D': '1 Ocak 2026',
            'E': 'Mart 2026',
        },
        'C',
        "m. 9'a göre bina vergisi mükellefiyeti, m. 33'teki vergi değerini tadil eden sebeplerin (yeni bina inşası dâhil) **doğduğu tarihi takip eden bütçe yılından** itibaren başlar. İnşaat 2026'da bittiğinden mükellefiyet **2027 yılı başında** başlar.",
        '1319 sayılı Emlak Vergisi Kanunu m. 9',
    ),
    # düzey 3
    '0009': patch(
        "Vergiye tabi bir bina Nisan 2026'da yangında tamamen yıkılmıştır. Emlak vergisinin birinci taksiti Mart-Mayıs, ikinci taksiti Kasım ayında ödendiğine göre, vergi hangi taksitten itibaren alınmaz?",
        {
            'A': 'Mayıs 2026 taksitinden',
            'B': 'Mart 2026 taksitinden',
            'C': 'Kasım 2026 taksitinden',
            'D': '2028 yılından',
            'E': '2027 birinci taksitinden',
        },
        'C',
        "m. 9'a göre yanan, yıkılan veya tamamen kullanılmaz hâle gelen binalardan dolayı mükellefiyet, **bu olayların vuku bulduğu tarihi takip eden taksitten** itibaren sona erer. Nisan'daki olaydan sonraki ilk taksit Kasım taksitidir (m. 30).",
        '1319 sayılı Emlak Vergisi Kanunu m. 9, 30',
    ),
    # düzey 2
    '0010': patch(
        'Aşağıdakilerden hangisi arazi vergisinden daimi olarak muaf değildir?',
        {
            'A': 'Belediye ve mücavir alan sınırları dışında ekim yapılan tarım arazisi',
            'B': 'Mezarlık',
            'C': 'Köy tüzel kişiliğine ait arazi',
            'D': 'Belediye sınırları dışında fabrikanın kullandığı arsa',
            'E': 'Toplu Konut İdaresine ait arsa',
        },
        'D',
        "m. 14'e göre mezarlıklar (e), TOKİ'ye ait arazi ve arsalar (i), köy tüzel kişiliğine ait araziler (a) ve **belediye ve mücavir alan sınırları dışındaki araziler** (g) muaftır. Ancak (g) bendindeki muafiyet **ticari, sınai ve turistik faaliyetlerde kullanılan** arazi ve arsalara uygulanmaz.",
        '1319 sayılı Emlak Vergisi Kanunu m. 14',
    ),
    # düzey 3
    '0011': patch(
        "Büyükşehir belediyesi sınırları içinde bulunan bir arsanın vergi değeri 3.000.000 ₺'dir. Cumhurbaşkanınca oran değişikliği yapılmadığı varsayılırsa yıllık arazi vergisi kaç ₺'dir?",
        {
            'A': '18.000',
            'B': '3.000',
            'C': '9.000',
            'D': '6.000',
            'E': '12.000',
        },
        'A',
        "m. 18'e göre arazi vergisinin oranı **binde bir, arsalarda binde üçtür**; bu oranlar büyükşehir belediye sınırları ve mücavir alanlarda **%100 artırımlı** uygulanır. Arsa için oran binde 6 olur: 3.000.000 × binde 6 = **18.000 ₺**. Artırım uygulanmazsa 9.000 ₺ bulunur.",
        '1319 sayılı Emlak Vergisi Kanunu m. 18',
    ),
    # düzey 2
    '0012': patch(
        "Mülkiyeti ihtilaflı bir araziye ait arazi vergisini, mutasarrıfı olmayan bir kişi ödemiştir. Mülkiyet davası ödeme yapan aleyhine sonuçlanmıştır.\n\nEmlak Vergisi Kanunu'na göre ödenen vergiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Ödenen vergi iade edilebilir',
            'B': 'İade için başvuru gerekir',
            'C': 'Vergi başvuru aranmadan faiziyle iade edilir',
            'D': 'Başvuru süresi karar tarihinden başlar',
            'E': 'Başvuru süresi bir yıldır',
        },
        'C',
        'EVK m. 13/3: mülkiyeti ihtilaflı arazi için mutasarrıfı bulunmayan kişilerce ödenen arazi vergileri, ihtilafın ödeme yapan aleyhine sonuçlanması hâlinde, ilgililerin karar tarihinden itibaren bir yıl içinde başvurmaları şartıyla ret ve iade olunur. İade kendiliğinden yapılmaz.',
        '1319 sayılı Emlak Vergisi Kanunu m. 13/3',
    ),
    # düzey 3
    '0013': patch(
        '7566 sayılı Kanunla yapılan değişiklikten sonra emlak vergi değerinin yıllık güncellenmesine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Cumhurbaşkanı belediye grupları itibarıyla farklı oran belirleyebilir',
            'B': 'Cumhurbaşkanı artış oranını sıfıra kadar indirebilir',
            'C': 'Vergi değeri her yıl yeniden değerleme oranında artırılır',
            'D': 'Cumhurbaşkanı artış oranını yeniden değerleme oranının üzerine çıkarabilir',
            'E': 'Arsa ve arazi birim değerleri de yeniden değerleme oranında güncellenir',
        },
        'D',
        "7566 sayılı Kanunla değişen m. 29'a göre vergi değeri her yıl **bir önceki yıl değerinin yeniden değerleme oranında** artırılmasıyla bulunur (önceden oranın yarısıydı); birim değerler de aynı oranda güncellenir. Cumhurbaşkanı artış oranını **sıfıra kadar indirebilir** ve bunu belediye grupları itibarıyla farklı oranlarla kullanabilir. Değişiklikle Cumhurbaşkanının oranı **artırma yetkisi metinden çıkarılmıştır**.",
        '1319 sayılı Emlak Vergisi Kanunu m. 29 (7566 sayılı Kanunla değişik)',
    ),
    # düzey 2
    '0014': patch(
        'Kanunlarla tasarrufu kısıtlanan bir arsanın yıllık arazi vergisi 20.000 ₺ olarak hesaplanmıştır. Kısıtlama sürdüğü müddetçe bu vergiden ne kadarı tahsil edilir?',
        {
            'A': '0 ₺',
            'B': '20.000 ₺',
            'C': '18.000 ₺',
            'D': '10.000 ₺',
            'E': '2.000 ₺',
        },
        'E',
        "m. 30'a göre kanunlar veya diğer kamu düzeni koyan mevzuatla **tasarrufu kısıtlanan** bina, arsa ve arazinin vergisi, kısıtlamanın devam ettiği sürece **1/10 oranında** tahsil olunur: 20.000 × 1/10 = **2.000 ₺**. Tecil edilen 9/10 kısım, taşınmaz satılır veya başkasına devredilirse muaccel olur.",
        '1319 sayılı Emlak Vergisi Kanunu m. 30',
    ),
    # düzey 2
    '0015': patch(
        'Mevcut bir binaya kalorifer tesisatı konulması emlak vergisi bakımından nasıl nitelendirilir?',
        {
            'A': 'Bir sonraki dört yıllık takdire kadar dikkate alınmaz',
            'B': 'Yeni inşaat hükmündedir; vergi değerini tadil eder',
            'C': 'Bina vergisinden muafiyet sebebidir',
            'D': 'Vergi değerini etkilemez',
            'E': 'Arazi vergisi değerini değiştirir',
        },
        'B',
        "m. 33/1'e göre yeni bina inşası vergi değerini tadil eden sebeptir; **mevcut binalara ilaveler yapılması veya asansör ya da kalorifer tesisatı konulması yeni inşaat hükmündedir**.",
        '1319 sayılı Emlak Vergisi Kanunu m. 33',
    ),
    # düzey 3
    '0016': patch(
        'Emlak vergisinin uygulanmasında belediyelerin görev ve yetkilerine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Belediye gelir şube müdürü vergi dairesi müdürü sıfat ve yetkisine sahiptir',
            'B': 'Kanunda geçen vergi dairesi tabiri belediyeleri ifade eder',
            'C': 'Emlak vergisi hakkında VUK ve 6183 sayılı Kanun hükümleri uygulanır',
            'D': "Belediyeler Vergi Usul Kanunu'na göre vergi incelemesi yapabilir",
            'E': "VUK'ta mahallin en büyük mal memuruna verilen yetkileri belediye başkanı kullanır",
        },
        'D',
        "m. 37'ye göre emlak vergisi hakkında VUK ve 6183 sayılı Kanun uygulanır; vergi dairesi tabiri belediyeleri ifade eder; gelir şube müdürü vergi dairesi müdürü, belediye başkanı da mahallin en büyük mal memuru yetkisini kullanır. Ancak bu yetkiler **VUK'un vergi inceleme yetkisi hariç** olmak üzere tanınmıştır.",
        '1319 sayılı Emlak Vergisi Kanunu m. 37',
    ),
    # düzey 3
    '0017': patch(
        "Bir mükellefin binası yıllarca bildirim dışı kalmış ve belediye bu durumu 2026 yılında öğrenmiştir.\n\nEmlak Vergisi Kanunu'na göre bu binanın vergi ve cezalarında zamanaşımıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Zamanaşımı idarenin öğrendiği tarihi izleyen yıl başlar',
            'B': "Bu olayda zamanaşımı 1 Ocak 2027'de başlar",
            'C': 'Kural bildirim dışı kalan bina ve araziye ilişkindir',
            'D': 'Zamanaşımı binanın inşa edildiği yılı izleyen yıl başlar',
            'E': 'Kural vergi ile birlikte cezalar için de geçerlidir',
        },
        'D',
        "EVK m. 40: bildirim dışı kalan bina ve arazinin vergi ve cezalarında zamanaşımı, bildirim dışı bırakıldığının idarece öğrenildiği tarihi takip eden yılın başından itibaren başlar. Öğrenme 2026'da olduğundan zamanaşımı 1 Ocak 2027'de başlar; inşa tarihi esas alınmaz.",
        '1319 sayılı Emlak Vergisi Kanunu m. 40',
    ),
    # düzey 3
    '0018': patch(
        'Değerli konut vergisine tabi bir meskene iki kişi eşit paylarla paylı mülkiyet hâlinde maliktir. Matrahın belirlenmesi ve mükellefiyet hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Vergi en büyük hisse sahibinden alınır',
            'B': 'Paylı mülkiyette değerli konut vergisi alınmaz',
            'C': 'Malikler vergiden müteselsilen sorumludur',
            'D': 'Her malikin hisse değeri ayrı ayrı eşikle karşılaştırılır',
            'E': 'Toplam değer esas alınır; her malik hissesi oranında mükelleftir',
        },
        'E',
        "m. 44'e göre **paylı ve elbirliği mülkiyette matrahın hesabında mesken nitelikli taşınmazın toplam değeri** esas alınır. m. 45'e göre **paylı mülkiyette** malikler **hisseleri oranında** mükelleftir; elbirliği mülkiyette ise müteselsilen sorumludur.",
        '1319 sayılı Emlak Vergisi Kanunu m. 44-45',
    ),
    # düzey 2
    '0019': patch(
        'Aşağıdakilerden hangileri değerli konut vergisinden muaftır?\n\nI. Müteahhidin henüz satmadığı ancak kiraya verdiği yeni konut\n\nII. Karşılıklılık şartıyla yabancı devletin elçisinin ikametine mahsus konut\n\nIII. Bir şirketin genel müdürünün kullandığı şirkete ait konut',
        {
            'A': 'I, II ve III',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'Yalnız II',
            'E': 'Yalnız I',
        },
        'D',
        "m. 46'ya göre karşılıklılık şartıyla **elçilik ve konsolosluk olarak kullanılan veya elçilerin ikametine mahsus** mesken nitelikli taşınmazlar (II) muaftır. Müteahhit stoğundaki yeni konutlar muaftır; ancak **kiraya verilmesi veya sair surette kullanılması** hâlinde muafiyet uygulanmaz (I). Şirkete ait konut (III) için muafiyet öngörülmemiştir.",
        '1319 sayılı Emlak Vergisi Kanunu m. 46',
    ),
    # düzey 2
    '0020': patch(
        'Esas faaliyet konusu bina inşası olan bir şirketin işletmesine kayıtlı, henüz ilk satışı yapılmamış ve boş duran yeni konutları değerli konut vergisi bakımından nasıl değerlendirilir?',
        {
            'A': 'Emlak vergisine dâhil edilir',
            'B': 'Değerli konut vergisinden muaftır',
            'C': 'Vergiye tabidir; şirket öder',
            'D': 'İlk satışta alıcı öder',
            'E': 'Yarı oranda vergilenir',
        },
        'B',
        "m. 46/ç'ye göre **esas faaliyet konusu bina inşası olanların işletmelerine kayıtlı** bulunan ve henüz ilk satışa, devir ve temlike konu edilmemiş yeni inşa edilen mesken nitelikli taşınmazlar muaftır; bu taşınmazların kiraya verilmesi veya sair surette kullanılması hâlinde muafiyet uygulanmaz.",
        '1319 sayılı Emlak Vergisi Kanunu m. 46/ç',
    ),
    # düzey 1
    '0021': patch(
        "Bina vergisinin uygulanmasında, Vergi Usul Kanunu'nda yazılı bina mütemmimleri nasıl dikkate alınır?",
        {
            'A': 'Ayrıca arazi vergisine tabi tutulur',
            'B': 'Değerinin yarısı dikkate alınır',
            'C': 'Vergi dışı bırakılır',
            'D': 'Ayrı bir bina sayılır',
            'E': 'Bina ile birlikte dikkate alınır',
        },
        'E',
        "m. 2/2'ye göre bu Kanunun uygulanmasında **Vergi Usul Kanunu'nda yazılı bina mütemmimleri de bina ile birlikte** nazara alınır.",
        '1319 sayılı Emlak Vergisi Kanunu m. 2',
    ),
    # düzey 2
    '0022': patch(
        "Bir daireye paylı mülkiyetle malik olan kişinin payı 1/4'tür. Dairenin yıllık bina vergisi 8.000 ₺ ise bu kişinin mükellef olduğu tutar kaç ₺'dir?",
        {
            'A': '2.000',
            'B': '2.400',
            'C': '6.000',
            'D': '8.000',
            'E': '4.000',
        },
        'A',
        "m. 3/2'ye göre bir binaya **paylı mülkiyet** hâlinde malik olanlar **hisseleri oranında** mükelleftir: 8.000 × 1/4 = **2.000 ₺**. **Elbirliği** mülkiyette ise malikler vergiden **müteselsilen** sorumludur.",
        '1319 sayılı Emlak Vergisi Kanunu m. 3/2',
    ),
    # düzey 2
    '0023': patch(
        'Aşağıdaki binalardan hangisi bina vergisinden daimi olarak muaf değildir?',
        {
            'A': 'Organize sanayi bölgesinde yer alan ve üretimde kullanılan fabrika binası',
            'B': 'Serbest bölgedeki depo binası',
            'C': 'Belediyenin kiraya verdiği hizmet binası',
            'D': 'Kazanç amacıyla işletilen özel hastane binası',
            'E': 'Umuma açık ibadethane',
        },
        'D',
        "m. 4/f'ye göre hastane, dispanser ve benzerleri **kazanç gayesi olmamak şartıyla** muaftır. 7033 sayılı Kanunla (m. 4/m) **organize sanayi bölgeleri, serbest bölgeler, endüstri bölgeleri, teknoloji geliştirme bölgeleri ve sanayi sitelerindeki** binalar muaflık kapsamına alınmıştır. İbadethaneler (g) ve belediye binaları (a) da muaftır; belediye binalarında kiraya verilmeme şartı aranmaz.",
        '1319 sayılı Emlak Vergisi Kanunu m. 4',
    ),
    # düzey 3
    '0024': patch(
        'Belediye ve mücavir alan sınırları dışında bir köyde bulunan ve yalnızca yaz aylarında tatil için kullanılan bir ev hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yarı oranda vergilenir',
            'B': 'Belediye ve mücavir alan sınırları dışında olduğu için kullanım amacına bakılmaksızın muaftır',
            'C': 'Köy tüzel kişiliğine ait sayılır ve muaftır',
            'D': 'Kullanılmayan aylar için vergi alınmaz',
            'E': 'Dinlenme amaçlı kullanıldığı için bina vergisine tabidir',
        },
        'E',
        "m. 4/u'ya göre belediye ve mücavir alan sınırları dışındaki binalar muaftır; ancak **ticari, sınai ve turistik faaliyetlerde kullanılan binalar ile muayyen zamanlarda dinlenme amacıyla kullanılan binalar** için bu muafiyet uygulanmaz.",
        '1319 sayılı Emlak Vergisi Kanunu m. 4/u',
    ),
    # düzey 2
    '0025': patch(
        'Geçici muaflıktan yararlanan bir daire, muaflık süresi içinde işyeri olarak kullanılmaya başlanmıştır. Muaflık ne zaman düşer?',
        {
            'A': 'İzleyen ilk taksit döneminden',
            'B': 'Bu hâlin olduğu yılı takip eden bütçe yılından itibaren',
            'C': 'Muaflık süresinin sonunda',
            'D': 'İşyeri olarak kullanılmaya başlandığı gün',
            'E': 'İşyeri kullanımı bir yılı aşınca',
        },
        'B',
        "m. 5/a'ya göre binanın veya dairenin **kısmen veya tamamen mesken olarak kullanılmaması** hâlinde tanınmış muaflık **bu hâlin vuku bulduğu yılı takip eden bütçe yılından** itibaren düşer.",
        '1319 sayılı Emlak Vergisi Kanunu m. 5/a',
    ),
    # düzey 3
    '0026': patch(
        'Yeni inşa edilen meskenlere tanınan geçici muaflıktan yararlanmak için gerekli bildirime ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bildirim yılın ilk üç ayında yapılmalıdır',
            'B': "Bildirim şartı yoktur; muaflık belediyece re'sen uygulanır",
            'C': 'Süresinde bildirilmezse muaflık bildirim yılını izleyen yıldan başlar',
            'D': 'Geç bildirimde geçmiş yılların muaflığı da ödenen vergiler iade edilerek geri verilir',
            'E': 'Bildirim ancak afet durumlarında aranır',
        },
        'C',
        "m. 5'e göre geçici muaflıklardan yararlanmak için keyfiyetin **bütçe yılı içinde** vergi dairesine bildirilmesi gerekir; olay yılın son üç ayında olursa bildirim üç ay içinde yapılır. **Süresinde bildirilmezse muafiyet, bildirimin yapıldığı yılı takip eden bütçe yılından muteber olur** ve geçen yıllara ait muafiyet hakkı düşer.",
        '1319 sayılı Emlak Vergisi Kanunu m. 5',
    ),
    # düzey 3
    '0027': patch(
        "Büyükşehir belediyesi sınırları içindeki bir iş yeri binasının vergi değeri 5.000.000 ₺'dir. Cumhurbaşkanınca oran değişikliği yapılmadığı varsayılırsa yıllık bina vergisi kaç ₺'dir?",
        {
            'A': '20.000',
            'B': '10.000',
            'C': '15.000',
            'D': '5.000',
            'E': '40.000',
        },
        'A',
        "m. 8'e göre bina vergisi oranı meskenlerde binde bir, **diğer binalarda binde ikidir**; bu oranlar 5216 sayılı Kanunun uygulandığı **büyükşehir belediye sınırları ve mücavir alanlarda %100 artırımlı** uygulanır. İş yeri için oran binde 4'tür: 5.000.000 × binde 4 = **20.000 ₺**. Artırım uygulanmazsa 10.000 ₺ bulunur.",
        '1319 sayılı Emlak Vergisi Kanunu m. 8',
    ),
    # düzey 2
    '0028': patch(
        'Kanunların verdiği yetkiye dayanılarak oturulması ve kullanılması yasaklanan bir binanın vergisi hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Vergi alınmaya devam eder, sonra iade edilir',
            'B': 'Vergi arazi vergisine dönüştürülür',
            'C': 'Bildirim veya tespit üzerine sonraki taksitlerden itibaren alınmaz',
            'D': 'Mükellefiyet kalıcı olarak sona erer',
            'E': 'Yasak süresince vergi iki kat alınır',
        },
        'C',
        "m. 9'a göre oturulması ve kullanılması kanunların verdiği yetkiye dayanılarak yasaklanan binaların vergileri, keyfiyetin **mükellefçe bildirilmesi veya vergi dairesince re'sen tespiti üzerine**, olayın vuku bulduğu tarihten sonraki taksitlerden itibaren **bu hâl devam ettiği sürece** alınmaz.",
        '1319 sayılı Emlak Vergisi Kanunu m. 9',
    ),
    # düzey 2
    '0029': patch(
        'Bina vergisinin tarh ve tahakkukuna ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sonraki yıllarda vergi her bütçe yılı başında tahakkuk etmiş sayılır',
            'B': 'Bina vergisini Gelir İdaresine bağlı vergi daireleri tarh eder',
            'C': 'Dört yılda bir takdirlerde tarh izleyen yılın Ocak-Şubat aylarında yapılır',
            'D': 'Belediye sınırları dışındaki bina için yetkili belediyeyi vali belirler',
            'E': 'Tarh edilen vergi tarh tarihinde tahakkuk etmiş sayılır',
        },
        'B',
        "m. 11'e göre bina vergisi **ilgili belediye** tarafından tarh edilir; m. 37'ye göre Kanunda geçen vergi dairesi tabiri belediyeleri ifade eder. Dört yılda bir takdirlerde tarh izleyen yılın Ocak-Şubat aylarında yapılır, tarh edilen vergi tarh tarihinde tahakkuk eder ve sonraki yıllarda her bütçe yılı başında tahakkuk etmiş sayılır.",
        '1319 sayılı Emlak Vergisi Kanunu m. 11',
    ),
    # düzey 3
    '0030': patch(
        'Kazancı basit usulde tespit edilen bir marangoz, belediye ve mücavir alan sınırları dışındaki arsasını bizzat atölye olarak kullanmaktadır. Arsa hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bina vergisine tabi olur',
            'B': 'Muaflık belediye onayına bağlıdır',
            'C': 'Arazi vergisinden muaftır',
            'D': 'Yarı oranda vergilenir',
            'E': 'Ticari faaliyette kullanıldığı için vergilenir',
        },
        'C',
        "m. 14/g'ye göre belediye ve mücavir alan dışındaki arazi muaftır; ticari, sınai ve turistik faaliyetlerde kullanılanlar için muafiyet uygulanmaz. Ancak parantez içi hükümle **gelir vergisinden muaf esnaf ile basit usul mükelleflerince bizzat işyeri olarak kullanılan** arsa ve arazi bu istisnanın dışında bırakılmıştır; muaflık devam eder.",
        '1319 sayılı Emlak Vergisi Kanunu m. 14/g',
    ),
    # düzey 3
    '0031': patch(
        'Arazi vergisi mükellefiyetinin başlaması ve sona ermesine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Muafiyetin sukutunda mükellefiyet izleyen bütçe yılından başlar',
            'B': 'Dört yıllık takdirde mükellefiyet takdiri izleyen bütçe yılında başlar',
            'C': 'Üzerine bina yapılan arsanın vergisi inşaatın başladığı yıl sona erer',
            'D': 'Tasarrufu kanunla yasaklanan araziden yasak sürdükçe vergi alınmaz',
            'E': 'Muaflık şartını kazanan araziden izleyen taksitten itibaren vergi alınmaz',
        },
        'C',
        "m. 19'a göre **üzerine bina yapılan arsanın arazi vergisi mükellefiyeti, inşaatın başladığı yıl değil, inşaatın bittiği yılı takip eden bütçe yılından itibaren sona erer**; aynı tarihten itibaren bina vergisi mükellefiyeti başlar. Diğer ifadeler m. 19'daki başlama, sona erme ve yasaklama hükümleridir.",
        '1319 sayılı Emlak Vergisi Kanunu m. 19',
    ),
    # düzey 2
    '0032': patch(
        'Depremde yıkılan bir binanın arsasına ait arazi vergisi, olayın gerçekleştiği yılı takip eden bütçe yılından itibaren kaç yıl süreyle alınmaz?',
        {
            'A': '5',
            'B': '2',
            'C': '10',
            'D': '4',
            'E': '3',
        },
        'B',
        "m. 19'a göre **deprem, su basması, yangın gibi tabii afetler** sebebiyle yanan veya yıkılan binaların arsalarına ait vergiler, bu olayların vuku bulduğu tarihi takip eden bütçe yılından itibaren **iki yıl** süreyle alınmaz.",
        '1319 sayılı Emlak Vergisi Kanunu m. 19',
    ),
    # düzey 1
    '0033': patch(
        "Bina ve arazi vergileriyle ilgili yeni bir muaflık getirilmesi düşünülmektedir.\n\nEmlak Vergisi Kanunu'na göre bu konuyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Muaflık bu Kanuna hüküm eklenerek düzenlenir',
            'B': 'Muaflık bu Kanunda değişiklik yapılarak düzenlenebilir',
            'C': 'Özel kanunlardaki muaflıklar kaldırılmıştır',
            'D': 'Tebliğle muaflık getirilebilir',
            'E': 'Belediye meclisi kararıyla muaflık getirilemez',
        },
        'D',
        'EVK m. 22: bina ve arazi vergileriyle ilgili muaflık ve istisna hükümleri bu Kanuna eklenmek veya bu Kanunda değişiklik yapılmak suretiyle düzenlenir; özel kanunlardaki muaflıklar m. 41 uyarınca kaldırılmıştır. Tebliğ ya da meclis kararıyla muaflık getirilemez.',
        '1319 sayılı Emlak Vergisi Kanunu m. 22',
    ),
    # düzey 3
    '0034': patch(
        "Tasarrufu kanunla kısıtlanan bir arsanın vergisi yıllarca 1/10 oranında ödenmiştir. Kısıtlama devam ederken arsa bir başkasına satılmıştır. Tecil edilen 9/10'luk kısım hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Borç alıcıya devredilir ve kısıtlama sürdükçe tecil alıcı adına devam eder',
            'B': 'Kısıtlama kalkana kadar tecil devam eder',
            'C': 'Tecil edilen kısım terkin edilir',
            'D': "Satış bedelinin 1/10'u oranında tahsil edilir",
            'E': 'Tahsil zamanaşımına uğramamış olanlar muaccel olur',
        },
        'E',
        "m. 30'a göre kısıtlamanın devam ettiği sürede **tecil edilen verginin 9/10'u**; bina, arsa veya arazinin **satılması, istimlaki veya hibe yoluyla başkasına devir ve temliki** hâlinde, **tahsil zamanaşımına uğramamış olanları muaccel** hâle gelir. Kısıtlama kaldırılırsa ise izleyen bütçe yılından itibaren vergi tüm değer üzerinden ödenir.",
        '1319 sayılı Emlak Vergisi Kanunu m. 30',
    ),
    # düzey 2
    '0035': patch(
        "Emlak vergisi borcu bulunan bir taşınmazın tapuda devri söz konusudur.\n\nEmlak Vergisi Kanunu'na göre bu konuyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Borç bulunan taşınmazın devir ve ferağı kural olarak yapılmaz',
            'B': 'Alıcının borcu üstlendiğini beyan etmesi devre imkân verir',
            'C': 'Mirasçılara intikalde bu yasak uygulanmaz',
            'D': 'Mahkeme kararıyla devirde bu yasak uygulanmaz',
            'E': 'Cebri icra yoluyla satışta bu yasak uygulanmaz',
        },
        'B',
        'EVK m. 30/8 (7327 sayılı Kanunla değişik): emlak vergisi borcu bulunan bina ve arazinin devir ve ferağı yapılmaz; ancak miras, mahkeme kararı, cebri icra, kamulaştırma ve özel kanunlarda öngörülen diğer hâller bu yasağın dışındadır. Alıcının borcu üstlenmesi yasağı kaldırmaz.',
        '1319 sayılı Emlak Vergisi Kanunu m. 30/8',
    ),
    # düzey 2
    '0036': patch(
        'Aşağıdakilerden hangileri emlak vergisinde vergi değerini tadil eden sebeplerdendir?\n\nI. Arazinin parsellenerek arsa hâline getirilmesi\n\nII. Binanın satılarak mükellefin değişmesi\n\nIII. Mevcut binaya asansör konulması\n\nIV. Binanın dış cephesinin boyanması',
        {
            'A': 'II, III ve IV',
            'B': 'I ve III',
            'C': 'I ve II',
            'D': 'I, II, III ve IV',
            'E': 'I, II ve III',
        },
        'E',
        "m. 33'e göre **arazinin parsellenerek arsa hâline getirilmesi** (4-e), bina veya arazinin **taksim, ifraz veya mükellefinin değişmesi** (6) ve **mevcut binaya asansör veya kalorifer konulması** (1) vergi değerini tadil eden sebeplerdir. Boya gibi olağan bakım (IV) bu sebepler arasında değildir.",
        '1319 sayılı Emlak Vergisi Kanunu m. 33',
    ),
    # düzey 1
    '0037': patch(
        "Emlak vergisi bildirimini süresinde vermeyen bir mükellef bulunmaktadır.\n\nEmlak Vergisi Kanunu'na göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Vergi idarece tarh edilir',
            'B': 'Her yılın vergi değeri kanundaki esaslara göre hesaplanır',
            'C': 'Bildirim yapılmaması mükellefiyeti ortadan kaldırmaz',
            'D': 'Vergi mükellefin sonraki beyanına bırakılmaz',
            'E': 'Bildirimi yapılmayan bina vergiden muaf sayılır',
        },
        'E',
        'EVK m. 32: bildirimin süresinde verilmemesi hâlinde vergi idarece tarh edilir; idarece tarhiyatta her yıla ilişkin vergi değeri m. 29 dikkate alınarak hesaplanır. Bildirim yapılmaması mükellefiyeti ortadan kaldırmaz ve muaflık doğurmaz.',
        '1319 sayılı Emlak Vergisi Kanunu m. 32',
    ),
    # düzey 3
    '0038': patch(
        "Değerli konut vergisinde eşik tutarının 10.000.000 ₺, ilk dilim üst sınırının 15.000.000 ₺ olduğu varsayılsın. Bina vergi değeri 13.000.000 ₺ olan ve muafiyet kapsamına girmeyen tek sahipli bir mesken için değerli konut vergisi kaç ₺'dir? (İlk dilim oranı binde 3'tür.)",
        {
            'A': '39.000',
            'B': '18.000',
            'C': '3.000',
            'D': '9.000',
            'E': '13.000',
        },
        'D',
        "m. 44'e göre verginin matrahı **bina vergi değerinin m. 42'deki eşiği aşan kısmıdır**: 13.000.000 − 10.000.000 = 3.000.000 ₺. Değer ilk dilimde kaldığından eşiği aşan kısma **binde 3** uygulanır: 3.000.000 × binde 3 = **9.000 ₺**. Değerin tamamına oran uygulanırsa 39.000 ₺ bulunur.",
        '1319 sayılı Emlak Vergisi Kanunu m. 44',
    ),
    # düzey 3
    '0039': patch(
        "Türkiye'de değerli konut vergisi eşiğini aşan iki meskeni bulunan bir kişi hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Daha düşük değerli olanı muaf, diğeri vergiye tabidir',
            'B': 'Kişi muaf tutulacak meskeni seçer',
            'C': 'İki mesken de vergiye tabidir',
            'D': 'İki mesken de muaftır',
            'E': 'Daha yüksek değerli olanı muaf, diğeri vergiye tabidir',
        },
        'A',
        "7221 sayılı Kanunla değişen m. 46/b'ye göre Türkiye'de **mesken nitelikli tek taşınmazı olanlar** ile birden fazla mesken nitelikli taşınmazı bulunanların **değerli konut vergisi konusuna giren en düşük değerli tek taşınmazı** muaftır. Diğer mesken vergiye tabidir.",
        '1319 sayılı Emlak Vergisi Kanunu m. 46/b',
    ),
    # düzey 2
    '0040': patch(
        'Değerli konut vergisinin beyanı ve ödenmesine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Vergi Şubat ve Ağustos aylarında iki eşit taksitte ödenir',
            'B': 'Vergi taşınmazın bulunduğu belediyeye beyan edilir',
            'C': "Eşiğin aşıldığı yılı izleyen yılın Şubat ayının 20'sine kadar beyan edilir",
            'D': 'Tahsil edilen vergi genel bütçe geliri olarak kaydedilir',
            'E': 'Paylı mülkiyette beyanname münferiden verilir',
        },
        'B',
        "m. 47'ye göre değerli konut vergisi, taşınmazın bulunduğu yerdeki **Gelir İdaresi Başkanlığına bağlı yetkili vergi dairesine** beyan edilir; belediyeye değil. Beyan eşiğin aşıldığı yılı izleyen yılın Şubat ayının 20'sine kadar yapılır, vergi Şubat ve Ağustos sonuna kadar iki taksitte ödenir, paylı mülkiyette beyanname münferiden verilir. m. 48'e göre hasılat genel bütçe geliridir.",
        '1319 sayılı Emlak Vergisi Kanunu m. 47-48',
    ),
    # düzey 2
    '0041': patch(
        "Bir dairenin mülkiyeti A'ya, bu daire üzerindeki intifa hakkı ise B'ye aittir.\n\nEmlak Vergisi Kanunu'na göre bina vergisinin mükellefiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Vergiyi malik A ile intifa hakkı sahibi B müteselsilen öder',
            'B': 'Bina vergisini kural olarak bina maliki öder',
            'C': 'İntifa hakkı varsa vergiyi intifa hakkı sahibi öder',
            'D': "Bu olayda mükellef intifa hakkı sahibi B'dir",
            'E': 'Daireyi kullanan kiracı vergi mükellefi değildir',
        },
        'A',
        "EVK m. 3: bina vergisini binanın maliki, varsa intifa hakkı sahibi, her ikisi de yoksa binaya malik gibi tasarruf edenler öder. İntifa hakkı bulunduğundan mükellef B'dir; malik ile müteselsil sorumluluk ya da kiracının mükellefiyeti söz konusu değildir.",
        '1319 sayılı Emlak Vergisi Kanunu m. 3',
    ),
    # düzey 3
    '0042': patch(
        'Kamu menfaatine yararlı bir derneğe ait bina bir bankaya kiraya verilmiştir. Bina vergisi muaflığı hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kiraya verildiği için muaflıktan yararlanılamaz',
            'B': 'Vergiyi banka öder, dernek muaftır',
            'C': 'Muaflık binanın yarısı için sürer',
            'D': 'Kira gelirine bakılmaksızın muaftır',
            'E': 'Dernek kamu yararına olduğundan muaflık sürer',
        },
        'A',
        "m. 4/e'ye göre kamu menfaatine yararlı derneklere ait binalar daimi muaftır; ancak bu bent, kiraya verilmeme şartının aranmadığı (a), (b), (s), (y) ve (z) bentleri arasında değildir. **Kiraya verilen bina muaflıktan yararlanamaz**.",
        '1319 sayılı Emlak Vergisi Kanunu m. 4/e',
    ),
    # düzey 3
    '0043': patch(
        'Bir çiftçinin zirai üretimde kullandığı ahır binasının bir bölümü, çiftçi ailesinin ikametine ayrılmıştır. Bina vergisi nasıl uygulanır?',
        {
            'A': 'Binanın tamamı zirai amaçla kullanıldığı kabul edilerek muaftır',
            'B': 'Tamamı arazi vergisine tabi tutulur',
            'C': 'Binanın yarısı vergilenir',
            'D': 'İkamete ayrılan kısım vergilenir, ahır kısmı muaftır',
            'E': 'Binanın tamamı vergilenir',
        },
        'D',
        "m. 4/h'ye göre zirai üretimde kullanılan ahır, ağıl, ambar gibi binalar daimi muaftır. Bu binaların bir kısmının ikamete, bir kısmının zirai amaçlara tahsis edilmesi hâlinde **vergi, ikamete tahsis olunan kısım için** uygulanır.",
        '1319 sayılı Emlak Vergisi Kanunu m. 4/h',
    ),
    # düzey 2
    '0044': patch(
        "İnşaatı 2025 yılında tamamlanan ve mesken olarak kullanılan bir dairenin vergi değeri 2.000.000 ₺'dir. Geçici muaflık kapsamında vergi değerinin ne kadarı muaf tutulur?",
        {
            'A': '500.000 ₺',
            'B': '400.000 ₺',
            'C': '2.000.000 ₺',
            'D': '1.000.000 ₺',
            'E': '200.000 ₺',
        },
        'A',
        "m. 5/a'ya göre mesken olarak kullanılan bina veya dairelerin, kanunda belirtilen alt sınırdan az olmamak üzere **vergi değerinin 1/4'ü**, inşalarının sona erdiği yılı takip eden bütçe yılından itibaren **beş yıl** süreyle geçici muaftır: 2.000.000 × 1/4 = **500.000 ₺**.",
        '1319 sayılı Emlak Vergisi Kanunu m. 5/a',
    ),
    # düzey 2
    '0045': patch(
        'Depremde yıkılan binası yerine, afet tarihinden itibaren beş yıl içinde afet bölgesinde yeni bina inşa eden mükellefin yeni binası kaç yıl süreyle geçici muaflıktan yararlanır?',
        {
            'A': '10',
            'B': '5',
            'C': '2',
            'D': '3',
            'E': '15',
        },
        'A',
        "m. 5/c'ye göre tabii afetler nedeniyle binaları yıkılan veya kullanılmaz hâle gelen mükelleflerin afet tarihinden itibaren en geç beş yıl içinde inşa ettikleri binalar, inşalarının sona erdiği yılı takip eden bütçe yılından itibaren **10 yıl** süreyle geçici muaftır; bu durumda (a) bendi uygulanmaz.",
        '1319 sayılı Emlak Vergisi Kanunu m. 5/c',
    ),
    # düzey 1
    '0046': patch(
        'Yatırım teşvik belgesi kapsamında inşa edilen binalar, inşalarının sona erdiği tarihi takip eden bütçe yılından itibaren ne kadar süre bina vergisinden geçici muaftır?',
        {
            'A': 'İki yıl',
            'B': 'On yıl',
            'C': 'Beş yıl',
            'D': 'Üç yıl',
            'E': 'Teşvik belgesi süresince',
        },
        'C',
        "6728 sayılı Kanunla eklenen m. 5/g'ye göre **yatırım teşvik belgesi kapsamında inşa edilen binalar**, inşalarının sona erdiği tarihi takip eden bütçe yılından itibaren **beş yıl** süreyle geçici muaftır. Teşvik belgesi süresince muaflık ise arazi vergisinde (m. 15/e) öngörülmüştür.",
        '1319 sayılı Emlak Vergisi Kanunu m. 5/g',
    ),
    # düzey 2
    '0047': patch(
        "Emlak Vergisi Kanunu'na göre Cumhurbaşkanının bina vergisi oranları üzerindeki yetkisi aşağıdakilerden hangisidir?",
        {
            'A': 'Oranları değiştirmemek',
            'B': 'Yarısına kadar indirmek, üç katına kadar artırmak',
            'C': 'Yarısına kadar artırmak, üçte birine indirmek',
            'D': 'Dört katına kadar artırmak',
            'E': 'İki katına kadar artırmak, tek meskenler dışında sıfıra kadar indirmek',
        },
        'B',
        "m. 8/1'e göre Cumhurbaşkanı bina vergisi oranlarını **yarısına kadar indirmeye veya üç katına kadar artırmaya** yetkilidir. Ayrıca belirli kişilerin 200 m²'yi aşmayan tek meskenleri için oranı sıfıra indirme yetkisi (m. 8/2) vardır.",
        '1319 sayılı Emlak Vergisi Kanunu m. 8',
    ),
    # düzey 3
    '0048': patch(
        'Cumhurbaşkanınca belirli kişilerin tek meskenlerine uygulanan sıfır oranlı bina vergisinden aşağıdakilerden hangisi yararlanamaz?',
        {
            'A': "Brüt 250 m²'lik tek meskeni olan emekli",
            'B': "Geliri olmadığını belgeleyen kişinin 120 m²'lik tek meskeni",
            'C': "Brüt 150 m²'lik tek meskeni olan emekli",
            'D': 'Tek meskene hisseyle sahip gazinin hissesi',
            'E': "Brüt 180 m²'lik tek meskeni olan engelli",
        },
        'A',
        "m. 8/2'ye göre sıfır oran; geliri olmadığını belgeleyenler, gelirleri yalnız sosyal güvenlik kurumlarından aldıkları aylıktan ibaret olanlar, gaziler, engelliler ve şehitlerin dul ve yetimlerinin **Türkiye'de brüt 200 m²'yi geçmeyen tek meskeni** için uygulanabilir; hisseli sahiplikte hisseye uygulanır. Dinlenme amacıyla kullanılan meskenler kapsam dışındadır.",
        '1319 sayılı Emlak Vergisi Kanunu m. 8/2',
    ),
    # düzey 2
    '0049': patch(
        "Emlak Vergisi Kanunu'na göre arsa ve arazinin nitelendirilmesiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Belediye sınırları içinde belediyece parsellenmiş arazi arsa sayılır',
            'B': 'Parsellenmemiş araziden arsa sayılacaklar Cumhurbaşkanınca belirlenir',
            'C': 'Belediyece parsellenmiş arazi tarım arazisi sayılır',
            'D': 'Arsa ve araziler arazi vergisine tabidir',
            'E': 'Arsa sayılma kuralı belediye sınırları içindeki araziye ilişkindir',
        },
        'C',
        'EVK m. 12: belediye sınırları içinde belediyece parsellenmiş arazi arsa sayılır; parsellenmemiş araziden hangilerinin arsa sayılacağı Cumhurbaşkanı kararıyla belirlenir. Arsa ve araziler arazi vergisinin konusunu oluşturur.',
        '1319 sayılı Emlak Vergisi Kanunu m. 12',
    ),
    # düzey 1
    '0050': patch(
        'Özel kanunlarına göre Devlet ormanları dışında insan emeğiyle yeniden orman hâline getirilmek üzere ağaçlandırılan arazi kaç yıl süreyle arazi vergisinden geçici muaftır?',
        {
            'A': '50',
            'B': '5',
            'C': '25',
            'D': '15',
            'E': '10',
        },
        'A',
        "m. 15/a'ya göre Devlet ormanları dışında insan emeğiyle yeniden orman hâline getirilmek üzere ağaçlandırılan arazi **50 yıl** geçici muaftır. Islahla tarıma elverişli hâle getirilen arazide süre 10 yıldır.",
        '1319 sayılı Emlak Vergisi Kanunu m. 15/a',
    ),
    # düzey 3
    '0051': patch(
        'Arazi vergisi istisnasına (Emlak Vergisi Kanunu m. 16) ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Cumhurbaşkanı istisna tutarını üç katına kadar artırabilir',
            'B': 'Mükellef, eşi ve velayetteki çocukların arazileri birlikte dikkate alınır',
            'C': 'İstisna arsalara da uygulanır',
            'D': 'İstisna belediye ve mücavir alan içindeki arazi için uygulanır',
            'E': 'Hisseli arazide her hissedarın hissesi ayrı dikkate alınır',
        },
        'C',
        "m. 16'ya göre mükelleflerin bir belediye ve mücavir alan sınırları içindeki arazisinin **(arsalar hariç)** toplam vergi değerinin kanunda belirtilen kısmı istisnadır. Uygulamada mükellef ile eş ve velayet altındaki çocuklara ait araziler toplu dikkate alınır, hisseli arazide hisseler ayrı ayrı nazara alınır ve Cumhurbaşkanı tutarı üç misline kadar artırabilir.",
        '1319 sayılı Emlak Vergisi Kanunu m. 16',
    ),
    # düzey 3
    '0052': patch(
        "Yeni inşa edilen bir binanın inşaatı 15 Kasım 2026'da sona ermiştir. Emlak vergisi bildirimi en geç hangi tarihe kadar verilmelidir?",
        {
            'A': '31 Ocak 2027',
            'B': '15 Aralık 2026',
            'C': '31 Aralık 2026',
            'D': '15 Şubat 2027',
            'E': '31 Mart 2027',
        },
        'D',
        "m. 23'e göre yeni inşa edilen binalar için bildirim, inşaatın sona erdiği **bütçe yılı içinde** verilir; ancak olay **bütçe yılının son üç ayı içinde** vuku bulmuşsa bildirim **olay tarihinden itibaren üç ay içinde** verilir. Kasım son üç ay içinde olduğundan süre **15 Şubat 2027**'de dolar.",
        '1319 sayılı Emlak Vergisi Kanunu m. 23',
    ),
    # düzey 2
    '0053': patch(
        'Emlak vergisi bildirimine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Olay yılın son üç ayındaysa üç ay içinde verilir',
            'B': 'Elbirliği mülkiyetinde müşterek veya münferit bildirim verilebilir',
            'C': 'Paylı mülkiyette malikler müşterek imzalı tek bildirim verir',
            'D': 'Devlete ait arazi için bildirim verilmez',
            'E': 'Yeni bina için inşaatın bittiği bütçe yılında verilir',
        },
        'C',
        "m. 23'e göre **paylı mülkiyette bildirim münferiden** verilir. Elbirliği mülkiyetinde müşterek imzalı veya münferit bildirim verilebilir; münferit bildirimde vergi hissedar sayısına göre ayrı ayrı tarh edilir. Devlete ait arazi için bildirim verilmez.",
        '1319 sayılı Emlak Vergisi Kanunu m. 23',
    ),
    # düzey 2
    '0054': patch(
        "Büyükşehir belediyesi sınırları dışında bulunan bir meskenin hesaplanan vergi değeri 1.284.750 ₺'dir. Kesirlere ilişkin kural uygulandığında, oran değişikliği yapılmadığı varsayılırsa yıllık bina vergisi kaç ₺'dir?",
        {
            'A': '1.280',
            'B': '1.284',
            'C': '1.284,75',
            'D': '2.568',
            'E': '1.285',
        },
        'B',
        "m. 29'a göre **vergi değerinin hesabında bin liraya, verginin hesaplanmasında ise bir liraya kadar olan kesirler dikkate alınmaz**. Vergi değeri 1.284.000 ₺ olur; mesken oranı binde 1 olduğundan vergi 1.284.000 × binde 1 = **1.284 ₺** bulunur. Büyükşehirdeki artırımlı oran uygulanırsa 2.568 ₺ çıkar.",
        '1319 sayılı Emlak Vergisi Kanunu m. 29, 8',
    ),
    # düzey 3
    '0055': patch(
        "Bir apartmanın zemin katındaki dairelerden biri mağazaya dönüştürülmüştür.\n\nEmlak Vergisi Kanunu'na göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Kullanış tarzının değişmesi vergi değerini tadil eder',
            'B': 'Tadil tüm apartmana uygulanır',
            'C': 'Bu hükmün uygulanmasında her daire bir bina sayılır',
            'D': 'Tadil sebebi kullanış tarzı değişen daire için geçerlidir',
            'E': 'Daireyi mağazaya dönüştürmek tadil sebebidir',
        },
        'B',
        'EVK m. 33/3: bir binanın kullanış tarzının değiştirilmesi veya ikamete mahsus kısımların dükkân, mağaza gibi mahallere dönüştürülmesi vergi değerini tadil eder. Bu hükmün uygulanmasında bir apartmanın her dairesi bir bina sayılır ve tadil sebebi kullanış tarzı değişen daire için geçerli olur.',
        '1319 sayılı Emlak Vergisi Kanunu m. 33/3',
    ),
    # düzey 2
    '0056': patch(
        "Emlak Vergisi Kanunu'na göre bir şehir, kasaba veya köyün tamamında bina veya arazi değerlerinde hangi oranı aşan sürekli bir değişme vergi değerini tadil eden sebep sayılır?",
        {
            'A': '%20',
            'B': '%50',
            'C': '%100',
            'D': '%10',
            'E': '%25',
        },
        'E',
        "m. 33/8'e göre herhangi bir sebeple bir şehir, kasaba veya köyün tamamında **devamlı olmak üzere** bina veya arazi değerlerinde **%25'i aşan** oranda artma veya eksilme olması vergi değerini tadil eden sebeptir; bu durumda takdir işlemine bağlı olarak mükellefiyet değişir.",
        '1319 sayılı Emlak Vergisi Kanunu m. 33/8',
    ),
    # düzey 2
    '0057': patch(
        'Emlak vergisinin taksitleri hangi aylarda ödenir?',
        {
            'A': 'Şubat ve Ağustos aylarında iki eşit taksit',
            'B': 'Nisan ve Ekim aylarında iki eşit taksit',
            'C': 'Tamamı Mayıs ayında',
            'D': 'Mart-Mayıs döneminde ve Kasım ayında iki eşit taksit',
            'E': 'Ocak ve Temmuz aylarında iki eşit taksit',
        },
        'D',
        "m. 30'a göre emlak vergisinin **birinci taksiti Mart, Nisan ve Mayıs aylarında, ikinci taksiti Kasım ayında** olmak üzere iki eşit taksitte ödenir; Maliye Bakanlığı ödeme aylarını bölgelerin özelliklerine göre değiştirebilir. Ocak-Temmuz MTV'nin, Şubat-Ağustos değerli konut vergisinin ödeme aylarıdır.",
        '1319 sayılı Emlak Vergisi Kanunu m. 30',
    ),
    # düzey 3
    '0058': patch(
        'Değerli konut vergisinde eşik tutarı ve dilim sınırları her yıl nasıl güncellenir?',
        {
            'A': 'Emlak vergi değeri artış oranında',
            'B': 'TÜFE oranında',
            'C': 'Yeniden değerleme oranının yarısı nispetinde',
            'D': 'Yeniden değerleme oranında',
            'E': 'Belediye meclisi kararıyla',
        },
        'C',
        "m. 44'e göre m. 42'deki eşik tutarı ve vergi oranlarına esas değerlerin alt ve üst sınırları her yıl **yeniden değerleme oranının yarısı nispetinde** artırılır; Cumhurbaşkanı bu artışı yeniden değerleme oranına kadar yükseltebilir. Emlak vergi değeri ise 7566 sayılı Kanundan sonra m. 29'a göre yeniden değerleme oranının tamamında artırılır.",
        '1319 sayılı Emlak Vergisi Kanunu m. 44/5',
    ),
    # düzey 2
    '0059': patch(
        'Bir meskenin bina vergi değeri 2026 yılı içinde değerli konut vergisi eşiğini aşmıştır. Değerli konut vergisi mükellefiyeti ne zaman başlar?',
        {
            'A': 'Mesken satıldığında',
            'B': '2026 yılının ikinci yarısından',
            'C': '2028 yılı başından',
            'D': 'Eşiğin aşıldığı günden',
            'E': '2027 yılı başından itibaren',
        },
        'E',
        "m. 45'e göre değerli konut vergisi mükellefiyeti, mesken nitelikli taşınmazın bina vergi değerinin **eşiği aştığı tarihi takip eden yıldan** itibaren başlar. 2026'da aşıldığından mükellefiyet **2027 yılı başında** başlar ve beyan 2027 Şubat ayında yapılır.",
        '1319 sayılı Emlak Vergisi Kanunu m. 45',
    ),
    # düzey 2
    '0060': patch(
        'Aşağıdakilerden hangileri emlak vergisinde oranların %100 artırımlı uygulanması için gereklidir?\n\nI. Taşınmazın büyükşehir belediye veya mücavir alan sınırları içinde olması\n\nII. Taşınmazın iş yeri olarak kullanılması\n\nIII. Malikin gerçek kişi olması',
        {
            'A': 'I, II ve III',
            'B': 'I ve III',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'Yalnız II',
        },
        'C',
        "m. 8 ve 18'e göre bina ve arazi vergisi oranları **5216 sayılı Kanunun uygulandığı büyükşehir belediye sınırları ve mücavir alanlar içinde %100 artırımlı** uygulanır. Artırım taşınmazın mesken veya iş yeri olmasına ya da malikin niteliğine bağlı değildir.",
        '1319 sayılı Emlak Vergisi Kanunu m. 8, 18',
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
    print(f"1 paket / {len(PATCHES)} soru ('Emlak Vergisi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
