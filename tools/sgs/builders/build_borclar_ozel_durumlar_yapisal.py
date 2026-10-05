#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Borc Iliskilerinde Ozel Durumlar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Borclar hukuku gercek sinav profiliyle yeniden yazim (eski surumde celdiricilerin buyuk kismi mutlak ifadeliydi, kor %48): temsil ve yetkisiz temsil, temsil yetkisinin sona ermesi, muteselsil borcluluk (savunmalar, ifa/takas/ibra etkisi, ic iliski ve rucu, halefiyet), muteselsil alacaklilik, geciktirici ve bozucu kosul, durustluge aykiri engelleme, yasak kosul, baglanma ve cayma parasi, ceza kosulu. Gercek sinav kaliplari (temsil yanlis listeleri, muteselsil alacaklilik ve muteselsil borcluluk tanimi) olaylara ve pay hesaplarina cevrildi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 6098 sayili Turk Borclar Kanunu m. 40-48, 61-62, 162-182 guncel metni (mevzuat.gov.tr)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/borclar_hukuku/ozel_durumlar.json"
STYLE_REF = 'SGS Borclar Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "ozeldurum-gen-"


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
        "A, satın alma yetkisi verdiği B aracılığıyla, B'nin A adına ve hesabına yaptığı sözleşmeyle C'den bir makine almıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "C, makinenin bedelini A'dan isteyebilir",
            'B': "A, makinenin teslimini C'den isteyebilir",
            'C': 'B, kural olarak sözleşmenin tarafı hâline gelmez',
            'D': "Sözleşmenin sonuçları doğrudan A'yı bağlar",
            'E': "Makinenin bedelini ödeme borcu B'ye ait olur",
        },
        'E',
        "TBK m. 40/1'e göre **yetkili bir temsilci tarafından bir başkası adına ve hesabına yapılan hukuki işlemin sonuçları, doğrudan doğruya temsil olunanı** bağlar. Haklar da borçlar da A'ya aittir; B sözleşmenin tarafı olmaz.",
        '6098 sayılı TBK m. 40/1',
    ),
    # düzey 3
    '0002': patch(
        "Bir şirket, müşterilerine gönderdiği yazıyla satış temsilcisi B'nin şirket adına 1.000.000 ₺'ye kadar sözleşme yapabileceğini bildirmiş; iç talimatla ise B'nin yetkisini 500.000 ₺ ile sınırlamıştır. B, bildirimi alan müşteri C ile 800.000 ₺'lik sözleşme yapmıştır. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Sözleşme ancak şirket sonradan onarsa bağlar',
            'B': "Sözleşme iç talimattaki 500.000 ₺ kadarıyla şirketi bağlar, fazlası B'ye aittir",
            'C': 'Sözleşme iç talimattaki sınırı aştığından şirketi bağlamaz',
            'D': 'Sözleşme, bildirilen yetki kapsamında kaldığından şirketi bağlar',
            'E': "Sözleşme B'yi kişisel olarak bağlar",
        },
        'D',
        "TBK m. 41/2'ye göre **temsil yetkisi üçüncü kişilere bildirilmişse, yetkinin içeriği ve derecesi bu bildirime göre** belirlenir. C'ye bildirilen yetki 1.000.000 ₺ olduğundan iç sınırlama ona karşı ileri sürülemez.",
        '6098 sayılı TBK m. 41/2',
    ),
    # düzey 3
    '0003': patch(
        "A'nın temsilcisi B, A'nın öldüğünü bilmeden A adına C ile bir sözleşme yapmıştır; C de ölümden habersizdir. Taraflar arasında aksine bir anlaşma yoktur. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': "A'nın mirasçıları sözleşmenin sonuçlarıyla bağlıdır",
            'B': 'Yetki sona erdiğinden mirasçıları bağlamaz',
            'C': 'Sözleşme kesin hükümsüzdür',
            'D': "Sözleşmenin sonuçları B'ye aittir",
            'E': 'Mirasçılar sözleşmeyi onamadıkça bağlı değildir',
        },
        'A',
        "TBK m. 43'e göre temsil yetkisi temsil olunanın ölümüyle kural olarak sona erer; ancak m. 45'e göre **temsilci yetkisinin sona ermiş olduğunu bilmediği sürece**, temsil olunan veya **halefleri**, yaptığı işlemlerin sonuçlarıyla bağlıdır. Üçüncü kişi sona ermeyi bilseydi bu kural uygulanmazdı.",
        '6098 sayılı TBK m. 43, 45',
    ),
    # düzey 2
    '0004': patch(
        'Aşağıdakilerden hangileri temsile ilişkin olarak doğrudur?\n\nI. Yetkisiz temsilcinin işlemi temsil olunanın onamasıyla onu bağlar\n\nII. Temsil olunan, temsil yetkisini geri alma hakkından önceden feragat edebilir\n\nIII. Temsilci sıfatını bildirmezse kural olarak işlemin sonuçları kendisine ait olur',
        {
            'A': 'I ve III',
            'B': 'I, II ve III',
            'C': 'Yalnız III',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'A',
        "TBK m. 46'ya göre yetkisiz temsilcinin işlemi **onama** ile temsil olunanı bağlar (I); m. 40/2'ye göre sıfatını bildirmeyen temsilcinin işleminin sonuçları kural olarak kendisine ait olur (III). m. 42/2'ye göre temsil olunan geri alma hakkından **önceden feragat edemez** (II).",
        '6098 sayılı TBK m. 40-47',
    ),
    # düzey 3
    '0005': patch(
        "Üç arkadaş, birlikte kiraladıkları tekne için 90.000 ₺'lik kira borcunu üstlenmiş; sözleşmede müteselsil sorumluluk kaydı yoktur ve kanunda da bu durum için müteselsil sorumluluk öngörülmemiştir. Kiraya veren tüm kirayı arkadaşlardan birinden istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Sözleşmeye müteselsil sorumluluk kaydı konabilirdi',
            'B': 'Kiranın tamamı birinden istenebilir',
            'C': 'Müteselsil borçluluk bildirim veya kanun hükmüyle doğar',
            'D': 'Bu olayda müteselsil borçluluk bulunmamaktadır',
            'E': 'Her arkadaş kural olarak kendi payından sorumludur',
        },
        'B',
        "TBK m. 162'ye göre müteselsil borçluluk, **birden çok borçludan her birinin borcun tamamından sorumlu olmayı kabul ettiğini bildirmesiyle** ya da **kanunda öngörülen hâllerde** doğar; aksi hâlde borç paylara bölünür.",
        '6098 sayılı TBK m. 162',
    ),
    # düzey 2
    '0006': patch(
        'Müteselsil borçlulardan A, diğerlerinin haberi olmadan alacaklıyla borcun faiz oranını artıran bir anlaşma yapmıştır. Kanunda veya sözleşmede aksine bir hüküm yoktur. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Diğerleri eski faiz oranı üzerinden sorumlu kalır',
            'B': 'A, yaptığı anlaşmayla artırılmış faizden sorumludur',
            'C': 'Diğer borçluların durumu bu anlaşmayla ağırlaşmaz',
            'D': 'Artırılmış faizden bütün borçlular sorumlu olur',
            'E': 'Kanun veya sözleşme aksini öngörseydi sonuç değişebilirdi',
        },
        'D',
        "TBK m. 165'e göre kanun veya sözleşme ile aksi belirlenmedikçe **borçlulardan biri kendi davranışıyla diğer borçluların durumunu ağırlaştıramaz**; artırılmış faiz A'yı bağlar, diğerleri eski koşullarla sorumlu kalır.",
        '6098 sayılı TBK m. 165',
    ),
    # düzey 3
    '0007': patch(
        "A, B ve C, 90.000 ₺'lik müteselsil borçta iç ilişkide eşit paylıdır. A borcun tamamını ödemiş; C ise aciz hâlindedir ve ondan hiçbir şey alınamamaktadır. A, B'den kaç ₺ isteyebilir?",
        {
            'A': '15.000',
            'B': '30.000',
            'C': '90.000',
            'D': '45.000',
            'E': '60.000',
        },
        'D',
        "TBK m. 167'ye göre her borçlunun payı 30.000 ₺'dir; fazla ödeyen **her borçluya payı oranında** rücu eder. **Borçlulardan birinden alınamayan miktarı diğer borçlular eşit olarak üstlenir**: C'nin 30.000 ₺'lik payını A ve B 15.000'er ₺ paylaşır. B'nin payı 30.000 + 15.000 = **45.000 ₺**.",
        '6098 sayılı TBK m. 167',
    ),
    # düzey 2
    '0008': patch(
        'Aşağıdakilerden hangileri müteselsil borçluluğa ilişkin olarak doğrudur?\n\nI. Borçlulardan birinin takası diğerlerini de o oranda borçtan kurtarır\n\nII. Bir borçlunun faizi artıran anlaşması diğer borçluları da bağlar\n\nIII. Alacaklının borçlulardan birini ibra etmesi diğerlerini borcun tamamından kurtarır',
        {
            'A': 'I ve III',
            'B': 'Yalnız III',
            'C': 'Yalnız I',
            'D': 'I, II ve III',
            'E': 'I ve II',
        },
        'C',
        "TBK m. 166/1'e göre takas diğerlerini de o oranda kurtarır (I). m. 165'e göre bir borçlu kendi davranışıyla diğerlerinin durumunu **ağırlaştıramaz** (II yanlış); m. 166/3'e göre ibra, diğerlerini ancak **ibra edilenin iç ilişkideki payı oranında** kurtarır (III yanlış).",
        '6098 sayılı TBK m. 165, 166',
    ),
    # düzey 3
    '0009': patch(
        "A, bir tabloyu B'nin mezun olması koşuluyla B'ye satmayı taahhüt etmiştir. Koşul askıdayken A tabloyu başkasına satmak için girişimde bulunmaktadır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Koşulun hükümlerini zedeleyen tasarruflar o oranda geçersiz olur',
            'B': 'Koşul gerçekleşirse sözleşme hüküm ifade eder',
            'C': 'A, borcun gereği gibi ifasını engelleyecek davranışlardan kaçınmalıdır',
            'D': 'Koşul askıdayken A tabloyu dilediğine devredebilir',
            'E': 'B, hakkı tehlikeye düştüğünde koruyucu önlemler alabilir',
        },
        'D',
        "TBK m. 171'e göre **koşul gerçekleşinceye kadar borçlu, borcun gereği gibi ifasını engelleyecek her türlü davranıştan kaçınmakla yükümlüdür**; hakkı tehlikeye düşürülen alacaklı önlem alabilir ve koşulun gerçekleşmesinden önce yapılan tasarruflar koşulun hükümlerini zedelediği oranda geçersiz olur.",
        '6098 sayılı TBK m. 171',
    ),
    # düzey 2
    '0010': patch(
        "Bir sözleşmede, A'nın sahip olduğu arsaya yapı izni çıkması koşulu öngörülmüştür. Koşul gerçekleşmeden A ölmüştür. Koşulun gerçekleşmesi A'nın bizzat yapması gereken bir davranış değildir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Koşul, A öldüğü için gerçekleşmemiş sayılır',
            'B': "Sözleşme A'nın ölümüyle sona erer",
            'C': 'Sözleşme mahkeme kararıyla devam eder',
            'D': 'Koşul mirasçılar için geçersizdir',
            'E': "Mirasçı, koşul bakımından A'nın yerine geçebilir",
        },
        'E',
        "TBK m. 174'e göre **koşul, taraflardan birinin bizzat yerine getirmesi gerekli bir davranış değilse, o tarafın ölümü hâlinde mirasçısı onun yerine geçebilir**.",
        '6098 sayılı TBK m. 174',
    ),
    # düzey 2
    '0011': patch(
        "A, B'ye 'rakibimin iş yerini kundaklarsan sana bir daire bağışlayacağım' demiş ve bu vaadi yazılı hâle getirmiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Koşul, hukuka aykırı bir fiili sağlamaya yöneliktir',
            'B': 'B, kundaklamayı gerçekleştirse de daireyi isteyemez',
            'C': 'Koşul gerçekleşirse vaat geçerli olur',
            'D': 'Yazılı şekle uyulması işlemi geçerli kılmaz',
            'E': 'Bu koşula bağlı bağışlama vaadi kesin hükümsüzdür',
        },
        'C',
        "TBK m. 176'ya göre **bir koşul, hukuka veya ahlaka aykırı bir yapma veya yapmama fiilini sağlamak amacıyla konulmuşsa, bu koşula bağlı hukuki işlem kesin olarak hükümsüzdür**; koşulun gerçekleşmesi veya yazılı şekil bu sonucu değiştirmez.",
        '6098 sayılı TBK m. 176',
    ),
    # düzey 3
    '0012': patch(
        "Alıcı, satış sözleşmesi yapılırken satıcıya 30.000 ₺ vermiş; bunun cayma parası olduğu kararlaştırılmamıştır. Alıcı daha sonra bu parayı bırakarak sözleşmeden caymak istemektedir.\n\nTBK'ya göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Sözleşme yapılırken verilen para kural olarak bağlanma parasıdır',
            'B': 'Bağlanma parası kural olarak esas alacaktan düşülür',
            'C': 'Verilen para alıcıya parayı bırakarak cayma hakkı verir',
            'D': 'Cayma parası kararlaştırılsaydı alıcı parayı bırakıp cayabilirdi',
            'E': 'Cayma parasını alan taraf cayarsa iki katını geri verir',
        },
        'C',
        'TBK m. 177: sözleşme yapılırken verilen para cayma parası değil bağlanma parası sayılır ve aksine hüküm yoksa esas alacaktan düşülür. m. 178: cayma parası kararlaştırılmışsa parayı veren onu bırakarak, alan ise iki katını geri vererek sözleşmeden cayabilir.',
        '6098 sayılı TBK m. 177, 178',
    ),
    # düzey 2
    '0013': patch(
        "İnşaat sözleşmesinde, her gün gecikme için 5.000 ₺ ceza kararlaştırılmıştır. Yüklenici binayı on gün geç teslim etmiş; iş sahibi binayı hiçbir çekince koymadan teslim almıştır.\n\nTBK'ya göre gecikme cezasıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Ceza, borcun zamanında ifa edilmemesi için kararlaştırılabilir',
            'B': 'Gecikme cezası kural olarak ifayla birlikte istenebilir',
            'C': 'Açık feragat da ceza isteme hakkını ortadan kaldırır',
            'D': 'Çekince konsaydı ceza ifayla birlikte istenebilirdi',
            'E': 'Çekincesiz kabul, ceza istemeye engel olmaz',
        },
        'E',
        'TBK m. 179/2: ceza, borcun belirlenen zaman veya yerde ifa edilmemesi için kararlaştırılmışsa alacaklı, hakkından açıkça feragat etmiş veya ifayı çekince ileri sürmeksizin kabul etmiş olmadıkça, asıl borcun ifasıyla birlikte cezayı da isteyebilir.',
        '6098 sayılı TBK m. 179/2',
    ),
    # düzey 3
    '0014': patch(
        'Bir taşınmaz satış vaadi resmî şekle uyulmadan yapılmış ve buna 100.000 ₺ ceza koşulu eklenmiştir. Taraflardan biri vaatten dönmüştür. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Asıl borç geçersiz olsa da ceza istenebilir',
            'B': "Ceza koşulu asıl borca bağlı bir fer'î yükümlülüktür",
            'C': 'Resmî şekle uyulmadığından asıl borç geçersizdir',
            'D': 'Ceza koşulunun geçersizliği asıl borcu etkilemezdi',
            'E': 'Asıl borç geçersiz olduğundan cezanın ifası istenemez',
        },
        'A',
        "TBK m. 182/2'ye göre **asıl borç herhangi bir sebeple geçersiz ise cezanın ifası istenemez**; buna karşılık ceza koşulunun geçersizliği asıl borcun geçerliliğini etkilemez. Ceza koşulu asıl borca bağlıdır.",
        '6098 sayılı TBK m. 182/2',
    ),
    # düzey 3
    '0015': patch(
        'Aşağıdakilerden hangileri ceza koşuluna ilişkin olarak doğrudur?\n\nI. Alacaklı zarara uğramadığını kabul ederse ceza istenemez\n\nII. Gecikme için kararlaştırılan ceza, ifa çekincesiz kabul edilirse istenemez\n\nIII. Ceza koşulunun geçersizliği asıl borcu da geçersiz kılar',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'Yalnız II',
            'D': 'I, II ve III',
            'E': 'II ve III',
        },
        'C',
        "TBK m. 179/2'ye göre zaman veya yer için kararlaştırılan ceza, ifa **çekincesiz kabul** edilirse istenemez (II). m. 180/1'e göre alacaklı hiç zarara uğramasa bile ceza istenebilir (I yanlış); m. 182/2'ye göre ceza koşulunun geçersizliği **asıl borcun geçerliliğini etkilemez** (III yanlış).",
        '6098 sayılı TBK m. 179-182',
    ),
    # düzey 2
    '0016': patch(
        "A, B'ye yalnızca kendi adına daire kiralama yetkisi vermiş ve bunu kimseye bildirmemiştir. B, A adına bir otomobil satın almıştır. Satın alma hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Temsilci sıfatıyla yapıldığından A'yı bağlar",
            'B': "Bedelin yarısı kadarıyla A'yı bağlar",
            'C': "B satın almaya A'nın kefili olarak katılır",
            'D': 'Yetki kapsamı dışında olduğundan onanmadıkça bağlamaz',
            'E': 'Satış işlemi kesin hükümsüzdür',
        },
        'D',
        "TBK m. 41/1'e göre hukuki işlemden doğan temsil yetkisinin **kapsamı, bu işleme göre** belirlenir. Yetkinin dışındaki işlem yetkisiz temsildir ve m. 46'ya göre **ancak onanırsa** A'yı bağlar.",
        '6098 sayılı TBK m. 41/1, 46',
    ),
    # düzey 3
    '0017': patch(
        "A, B ve C, alacaklı D'ye 90.000 ₺ müteselsilen borçludur; iç ilişkide eşit paylıdırlar. D, A'yı ibra etmiş; B de kalan borcun tamamını D'ye ödemiştir. B, C'den kaç ₺ isteyebilir?",
        {
            'A': '45.000',
            'B': '30.000',
            'C': '60.000',
            'D': '15.000',
            'E': '20.000',
        },
        'B',
        "TBK m. 166/3'e göre A'nın ibrası diğerlerini A'nın payı (30.000 ₺) oranında kurtarır; kalan borç 60.000 ₺'dir. B bunu ödediğinde m. 167'ye göre C'ye **payı oranında**, yani **30.000 ₺** rücu eder.",
        '6098 sayılı TBK m. 166/3, 167',
    ),
    # düzey 3
    '0018': patch(
        'Müteselsil borçlulardan A, alacaklıya ödeme yapmadan, sözleşmenin kendisi bakımından iptal edilmesiyle borçtan kurtulmuştur. Diğer borçluların bu durumdan yararlanması hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ancak alacaklının açık onayıyla bu durumdan yararlanırlar',
            'B': "A'nın iç ilişkideki payı oranında borçtan kurtulurlar",
            'C': 'Durumun veya borcun niteliği elverdiği ölçüde',
            'D': 'Borcun tamamından kurtulmuş olurlar',
            'E': 'Bundan yararlanamazlar',
        },
        'C',
        "TBK m. 166/2'ye göre **borçlulardan biri, alacaklıya ifada bulunmaksızın borçtan kurtulmuşsa, diğer borçlular bundan ancak durumun veya borcun niteliğinin elverdiği ölçüde** yararlanabilirler.",
        '6098 sayılı TBK m. 166/2',
    ),
    # düzey 3
    '0019': patch(
        'Bir kira sözleşmesinde, kiracının 40.000 ₺ cezayı ödeyerek sözleşmeyi feshedebileceği kararlaştırılmıştır. Kiracı cezayı ödeyerek sözleşmeyi feshetmek istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Kiracı cezayı ödese de sözleşmeyle bağlı kalır',
            'B': 'Cezanın miktarını taraflar belirleyebilir',
            'C': 'Kiracı cezayı ödeyerek sözleşmeyi sona erdirebilir',
            'D': 'Hâkim aşırı gördüğü cezayı indirebilir',
            'E': 'Borçlu, ceza ödeyerek fesih yetkisinin saklı olduğunu ispat edebilir',
        },
        'A',
        "TBK m. 179/3'e göre **borçlunun, kararlaştırılan cezayı ifa ederek sözleşmeyi dönme veya fesih suretiyle sona erdirmeye yetkili olduğunu ispat etme hakkı saklıdır**. m. 182'ye göre miktar serbesttir ve hâkim aşırı cezayı indirir.",
        '6098 sayılı TBK m. 179/3, 182',
    ),
    # düzey 2
    '0020': patch(
        'Aşağıdakilerden hangileri bağlanma ve cayma parasına ilişkin olarak doğrudur?\n\nI. Bağlanma parası, aksine sözleşme veya yerel âdet yoksa esas alacaktan düşülür\n\nII. Cayma parasını veren taraf cayarsa verdiğini bırakır\n\nIII. Cayma parasını almış olan taraf sözleşmeden cayamaz',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız II',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'D',
        "TBK m. 177/2'ye göre bağlanma parası kural olarak esas alacaktan düşülür (I); m. 178'e göre parayı veren cayarsa verdiğini bırakır (II). Aynı hükme göre **taraflardan her biri** caymaya yetkilidir; parayı alan da cayabilir, ancak aldığının iki katını geri verir (III yanlış).",
        '6098 sayılı TBK m. 177, 178',
    ),
    # düzey 3
    '0021': patch(
        'Bir marketin kasiyeri, market adına olduğunu söylemeden toptancıdan marketin rafları için ürün almıştır; toptancı kasiyeri market önlüğüyle ve market aracından tanımaktadır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Karşı tarafın durumdan çıkarması gereken hâllerde de temsil hükümleri uygulanır',
            'B': 'Temsil sıfatı bildirilmediğinden sözleşmenin sonuçları kasiyere aittir',
            'C': 'Temsil sıfatının açıkça bildirilmesi şart olmayabilir',
            'D': 'Toptancı temsil ilişkisini durumdan çıkarabilecek durumdadır',
            'E': 'Sözleşmenin sonuçları doğrudan markete aittir',
        },
        'B',
        "TBK m. 40/2'ye göre temsilci sıfatını bildirmezse sonuçlar kural olarak kendisine ait olur; ancak **karşı taraf bir temsil ilişkisinin varlığını durumdan çıkarıyor veya çıkarması gerekiyorsa** ya da işlemi kiminle yaptığı farksızsa sonuçlar doğrudan temsil olunana ait olur.",
        '6098 sayılı TBK m. 40/2',
    ),
    # düzey 3
    '0022': patch(
        "A, tedarikçilerine B'nin kendisi adına alım yapmaya yetkili olduğunu bildirmiş; sonra B'nin yetkisini geri almış ancak bunu tedarikçilere bildirmemiştir. B, iyiniyetli tedarikçi C'den A adına mal almıştır. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Yetki geri alındığından sözleşme A'yı bağlamaz",
            'B': 'Sözleşme kesin hükümsüzdür',
            'C': "A, geri almayı iyiniyetli C'ye karşı ileri süremez",
            'D': "C'nin hakkı A'nın onayına bağlıdır",
            'E': "Sözleşme B'yi kişisel olarak bağlar",
        },
        'C',
        "TBK m. 42/3'e göre temsil olunan verdiği yetkiyi üçüncü kişilere bildirmişse, **bu yetkiyi geri aldığını onlara bildirmediği takdirde, yetkinin geri alındığını iyiniyetli üçüncü kişilere karşı ileri süremez**.",
        '6098 sayılı TBK m. 42/3',
    ),
    # düzey 2
    '0023': patch(
        'Temsil yetkisinin sona ermesine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Temsil olunanın ölümü kural olarak yetkiyi sona erdirir',
            'B': 'Temsil olunanın fiil ehliyetini kaybetmesi yetkiyi sona erdirir',
            'C': 'Taraflar ölümle sona ermeyeceğini kararlaştırabilir',
            'D': 'Tüzel kişiliğin sona ermesi de yetkiyi sona erdirir',
            'E': 'Temsilcinin iflası temsil yetkisini kural olarak etkilemez',
        },
        'E',
        "TBK m. 43'e göre hukuki işlemden doğan temsil yetkisi, aksi kararlaştırılmadıkça veya işin özelliğinden anlaşılmadıkça, **temsil olunanın veya temsilcinin** ölümü, gaipliğine karar verilmesi, fiil ehliyetini kaybetmesi veya **iflası** durumlarında sona erer; tüzel kişiliğin sona ermesinde de uygulanır.",
        '6098 sayılı TBK m. 43, 45',
    ),
    # düzey 2
    '0024': patch(
        "B, hiçbir yetkisi olmadığı hâlde A adına C ile bir kira sözleşmesi yapmıştır. C, A'dan bu işlemi onayıp onamayacağını bildirmesi için uygun bir süre vermiş, A süre içinde cevap vermemiştir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Sözleşme süresiz olarak askıda kalır',
            'B': "A'nın susması onama sayılır ve sözleşme A'yı bağlar",
            'C': 'C, sözleşmeyle bağlı olmaktan kurtulur',
            'D': "Sözleşme B'yi bağlar",
            'E': "C, A'yı dava ederek onamaya zorlayabilir",
        },
        'C',
        "TBK m. 46'ya göre yetkisiz temsilcinin yaptığı işlem **ancak onandığı takdirde** temsil olunanı bağlar; diğer taraf uygun bir süre verebilir ve **bu süre içinde işlem onanmazsa diğer taraf işlemle bağlı olmaktan kurtulur**.",
        '6098 sayılı TBK m. 46',
    ),
    # düzey 3
    '0025': patch(
        "Müteselsil borçlulardan A, alacaklının istemi üzerine, tüm borçlulara karşı ileri sürülebilecek olan zamanaşımı def'ini ileri sürmeden borcu ödemiştir. A, diğer borçlulara rücu etmek istemektedir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Diğer borçlular A'ya ödemekle yükümlüdür",
            'B': "A'nın ödemesi kesin hükümsüzdür",
            'C': "Zamanaşımı def'i rücu ilişkisinde önemsizdir",
            'D': "A, ortak def'iyi kullanmadığı için diğerlerine sorumludur",
            'E': "A, def'i ileri sürmese de tam rücu edebilir",
        },
        'D',
        "TBK m. 164/2'ye göre **müteselsil borçlulardan biri ortak def'i ve itirazları ileri sürmezse, diğerlerine karşı sorumlu olur**. Ortak bir savunmayı kullanmadan ödeyen borçlu, bu yüzden rücu hakkını diğerlerine karşı ileri süremez.",
        '6098 sayılı TBK m. 164/2',
    ),
    # düzey 3
    '0026': patch(
        "A, B ve C, alacaklı D'ye 90.000 ₺ müteselsilen borçludur; iç ilişkide eşit paylıdırlar. D, A'yı borçtan ibra etmiştir. D, B'den en fazla kaç ₺ isteyebilir?",
        {
            'A': '30.000',
            'B': '90.000',
            'C': '60.000',
            'D': '45.000',
            'E': '0',
        },
        'C',
        "TBK m. 166/3'e göre **alacaklının borçlulardan biriyle yaptığı ibra sözleşmesi, diğer borçluları da ibra edilen borçlunun iç ilişkideki borca katılma payı oranında** borçtan kurtarır: A'nın payı 30.000 ₺ olduğundan B ve C 60.000 ₺'den müteselsilen sorumlu kalır.",
        '6098 sayılı TBK m. 166/3',
    ),
    # düzey 2
    '0027': patch(
        "Müteselsil borçlulardan A borcun tamamını ödemiştir. Alacaklının alacağı, diğer borçlu B'nin evi üzerindeki ipotekle güvence altındadır. A'nın B'ye rücu hakkına ilişkin aşağıdakilerden hangisi doğrudur?",
        {
            'A': "A'nın rücu hakkı yoktur",
            'B': 'A ancak kişisel olarak rücu edebilir, ipoteğe dayanamaz',
            'C': 'A, alacaklıya halef olarak ipotekten yararlanabilir',
            'D': "İpotek A'ya ancak B'nin onayıyla geçer",
            'E': 'İpotek alacaklının ödeme almasıyla sona erer',
        },
        'C',
        "TBK m. 168'e göre **diğerlerine rücu hakkına sahip olan borçlulardan her biri, ifa ettiği miktar oranında alacaklının haklarına halef olur**; bu halefiyet alacağı güvence altına alan hakları da kapsar.",
        '6098 sayılı TBK m. 168',
    ),
    # düzey 3
    '0028': patch(
        "Müteselsil alacaklılardan A, borçlu D aleyhine icra takibi başlatmış ve bunu D'ye bildirmiştir. Buna rağmen D, borcun tamamını diğer alacaklı B'ye ödemiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "Takip bildirildikten sonra D, takip eden A'ya ödemelidir",
            'B': 'Fazlasını alan alacaklı diğerlerine payını öder',
            'C': 'Takip bildirilmeseydi D dilediği alacaklıya ödeyebilirdi',
            'D': 'Müteselsil alacaklılıkta alacaklılardan her biri tamamını isteyebilir',
            'E': "D, B'ye ödemekle bütün alacaklılara karşı borcundan kurtulur",
        },
        'E',
        "TBK m. 169'a göre borçlu, **alacaklılardan birinin icraya veya mahkemeye başvurmuş olduğu kendisine bildirilmedikçe** dilediği birine ifada bulunabilir; bildirimden sonra takip eden alacaklıya ödemesi gerekir, aksi hâlde borçtan kurtulmaz.",
        '6098 sayılı TBK m. 169/3',
    ),
    # düzey 2
    '0029': patch(
        'Geciktirici koşula bağlı bir satışta inek, koşul gerçekleşmeden alıcıya teslim edilmiş ve bu sırada bir buzağı doğmuştur. Koşul gerçekleşmemiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'İnek de satıcıya iade edilmelidir',
            'B': 'Buzağı, askı döneminde doğduğu için alıcıda kalır',
            'C': 'Alıcı elde ettiği yararları geri vermelidir',
            'D': 'Koşul gerçekleşseydi buzağı alıcıya ait olurdu',
            'E': 'Koşul gerçekleşmediğinden sözleşme hüküm doğurmaz',
        },
        'B',
        "TBK m. 172'ye göre borcun konusu şey koşulun gerçekleşmesinden önce alacaklıya verilmişse, **koşul gerçekleşirse** alacaklı elde ettiği yararların sahibi olur; **koşul gerçekleşmezse elde ettiği yararları geri vermekle yükümlüdür**.",
        '6098 sayılı TBK m. 172',
    ),
    # düzey 2
    '0030': patch(
        'Bir işveren, işçisine ehliyet sınavını geçmesi hâlinde maaş artışı taahhüt etmiştir. İşçi sınavı hileyle geçtiği sonradan anlaşılmıştır. Koşul hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşveren ancak ceza davası sonucunu bekleyebilir',
            'B': 'Hile nedeniyle koşul gerçekleşmemiş sayılır',
            'C': 'Koşul yarı oranda gerçekleşmiş sayılır',
            'D': 'Sınav geçildiğinden koşul gerçekleşmiştir',
            'E': 'Taahhüt kesin hükümsüzdür',
        },
        'B',
        "TBK m. 175/2'ye göre **taraflardan biri, koşulun gerçekleşmesini dürüstlük kurallarına aykırı biçimde sağlarsa, koşul gerçekleşmemiş sayılır**.",
        '6098 sayılı TBK m. 175/2',
    ),
    # düzey 2
    '0031': patch(
        'Koşullara ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Bozucu koşulun gerçekleşmesi kural olarak geçmişe etkili olarak hükümleri kaldırır\n\nII. Geciktirici koşula bağlı sözleşme kural olarak koşulun gerçekleştiği andan hüküm ifade eder\n\nIII. Koşulu dürüstlüğe aykırı engelleyene karşı koşul gerçekleşmiş sayılır',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız II',
            'C': 'Yalnız III',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'E',
        "TBK m. 170'e göre geciktirici koşulda sözleşme koşulun gerçekleştiği andan hüküm ifade eder (II); m. 175/1'e göre dürüstlüğe aykırı engellemede koşul gerçekleşmiş sayılır (III). m. 173'e göre bozucu koşulda sona erme kural olarak **geçmişe etkili olmaz** (I yanlış).",
        '6098 sayılı TBK m. 170-175',
    ),
    # düzey 3
    '0032': patch(
        'Bir satış sözleşmesinde 20.000 ₺ cayma parası kararlaştırılmış ve alıcı bunu satıcıya ödemiştir. Satıcı sözleşmeden caymıştır. Satıcı alıcıya kaç ₺ geri vermelidir?',
        {
            'A': '10.000',
            'B': '20.000',
            'C': '0',
            'D': '60.000',
            'E': '40.000',
        },
        'E',
        "TBK m. 178'e göre cayma parası kararlaştırılmışsa taraflardan her biri caymaya yetkilidir; **parayı vermiş olan cayarsa verdiğini bırakır; almış olan cayarsa aldığının iki katını geri verir**: 20.000 × 2 = **40.000 ₺**.",
        '6098 sayılı TBK m. 178',
    ),
    # düzey 3
    '0033': patch(
        'Bir sözleşmede ifa edilmeme hâli için 50.000 ₺ ceza kararlaştırılmıştır. Alacaklının zararı 80.000 ₺ olarak ispat edilmiş, borçlunun kusuru da ispatlanmıştır. Alacaklı toplam kaç ₺ isteyebilir?',
        {
            'A': '80.000',
            'B': '30.000',
            'C': '50.000',
            'D': '65.000',
            'E': '130.000',
        },
        'A',
        "TBK m. 180/2'ye göre **alacaklının uğradığı zarar kararlaştırılan ceza tutarını aşıyorsa alacaklı, borçlunun kusuru bulunduğunu ispat etmedikçe aşan miktarı isteyemez**. Kusur ispatlandığından 50.000 ₺ ceza ve 30.000 ₺ aşan zarar, toplam **80.000 ₺** istenebilir.",
        '6098 sayılı TBK m. 180/2',
    ),
    # düzey 2
    '0034': patch(
        'Bir konserde sahne alacak sanatçı için geç gelme cezası kararlaştırılmıştır. Konser salonu, sanatçının sorumlu tutulamayacağı bir yangınla kullanılamaz hâle gelmiş ve konser yapılamamıştır; sözleşmede bu hâle ilişkin bir hüküm yoktur. Ceza hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ceza sanatçının zarar görmemesine bağlıdır',
            'B': 'Organizatör cezayı ancak mahkemeye başvurarak isteyebilir',
            'C': 'Borç kusursuz imkânsızlaştığından ceza istenemez',
            'D': 'Cezanın yarısı istenebilir',
            'E': 'Konser yapılmadığından ceza istenir',
        },
        'C',
        "TBK m. 182/2'ye göre aksi kararlaştırılmadıkça asıl borç **sonradan borçlunun sorumlu tutulamayacağı bir sebeple imkânsız hâle gelmişse cezanın ifası istenemez**.",
        '6098 sayılı TBK m. 182/2',
    ),
    # düzey 2
    '0035': patch(
        'Aylık 10.000 ₺ kira bedeli olan bir konut kira sözleşmesinde, bir günlük gecikme için 500.000 ₺ ceza kararlaştırılmıştır. Kiracı bir gün gecikmiş, indirim de istememiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'İndirim için kiracının istemi gerekmez',
            'B': 'Hâkim aşırı gördüğü cezayı indirir',
            'C': 'Cezanın miktarını taraflar belirleyebilir',
            'D': 'Ceza koşulu bu durumda tamamen geçersiz sayılmaz',
            'E': 'Kiracı istemediği için hâkim cezayı indiremez',
        },
        'E',
        "TBK m. 182'ye göre taraflar cezanın miktarını serbestçe belirleyebilir; ancak **hâkim, aşırı gördüğü ceza koşulunu kendiliğinden indirir**; indirim için borçlunun istemi gerekmez.",
        '6098 sayılı TBK m. 182',
    ),
    # düzey 3
    '0036': patch(
        "A, temsilcisi B'nin yetkisini geri almıştır. B bunu henüz öğrenmeden A adına C ile bir sözleşme yapmıştır; C ise yetkinin geri alındığını A'dan öğrenmiştir. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Sözleşme A ile C arasında yarı oranda hüküm doğurur',
            'B': "C, sözleşmenin ifasını A'dan isteyebilir",
            'C': "B iyiniyetli olduğundan sözleşme A'yı bağlar",
            'D': 'Sözleşme A adına değil, B adına kurulmuş sayılır',
            'E': "C geri almayı bildiğinden sözleşme A'yı bağlamaz",
        },
        'E',
        "TBK m. 45/1'e göre temsilci yetkisinin sona erdiğini bilmediği sürece yaptığı işlemler temsil olunanı bağlar; ancak m. 45/2'ye göre **üçüncü kişinin, temsilcinin yetkisinin sona erdiğini bildiği durumlarda bu hüküm uygulanmaz**.",
        '6098 sayılı TBK m. 45',
    ),
    # düzey 3
    '0037': patch(
        "Müteselsil borçlulardan A'ya, alacaklı tarafından kişisel olarak altı aylık ödeme ertelemesi tanınmıştır. Diğer borçlu B'ye böyle bir erteleme verilmemiştir. Alacaklı, borcun tamamını B'den istemiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "Borcun sebep ve konusundan doğan def'iler her borçluca ileri sürülebilir",
            'B': "B, A'ya tanınan ertelemeyi alacaklıya karşı ileri sürebilir",
            'C': "Alacaklı borcun tamamını B'den isteyebilir",
            'D': "Erteleme, A'nın kişisel ilişkisinden doğan bir def'idir",
            'E': "B, kendi kişisel ilişkisinden doğan def'ileri ileri sürebilir",
        },
        'B',
        "TBK m. 164/1'e göre müteselsil borçlulardan biri alacaklıya karşı **ancak onunla kendi arasındaki kişisel ilişkilerden veya müteselsil borcun sebep ya da konusundan doğan** def'i ve itirazları ileri sürebilir. A'ya tanınan erteleme A'nın kişisel def'idir; B bunu ileri süremez.",
        '6098 sayılı TBK m. 164/1',
    ),
    # düzey 3
    '0038': patch(
        "Bir satış sözleşmesinde 25.000 ₺ cayma parası kararlaştırılmış ve alıcı bu parayı satıcıya ödemiştir. Alıcı sözleşmeden caymıştır. Satıcının alıcıya geri vermesi gereken tutar kaç ₺'dir?",
        {
            'A': '25.000',
            'B': '50.000',
            'C': '0',
            'D': '75.000',
            'E': '12.500',
        },
        'C',
        "TBK m. 178'e göre cayma parası kararlaştırılmışsa taraflardan her biri caymaya yetkilidir; **parayı vermiş olan cayarsa verdiğini bırakır**. Cayan alıcı olduğundan satıcı hiçbir tutar geri vermez: **0 ₺**.",
        '6098 sayılı TBK m. 178',
    ),
    # düzey 3
    '0039': patch(
        "Bir sözleşmede ifa edilmeme hâli için 50.000 ₺ ceza kararlaştırılmıştır. Alacaklının zararı 80.000 ₺'dir; ancak borçlunun kusurlu olduğu ispat edilememiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Hâkim aşırı bulursa cezayı indirebilir',
            'B': 'Alacaklı kararlaştırılan 50.000 ₺ cezayı isteyebilir',
            'C': 'Zarar olmasaydı da cezanın ifası gerekirdi',
            'D': "Alacaklı zararının tamamı olan 80.000 ₺'yi isteyebilir",
            'E': "Aşan 30.000 ₺'yi isteyebilmesi için borçlunun kusurunu ispat etmesi gerekir",
        },
        'D',
        "TBK m. 180/2'ye göre zarar ceza tutarını aşıyorsa alacaklı, **borçlunun kusuru bulunduğunu ispat etmedikçe aşan miktarı isteyemez**. Kusur ispatlanamadığından alacaklı yalnız 50.000 ₺ cezayı alabilir.",
        '6098 sayılı TBK m. 180/2',
    ),
    # düzey 2
    '0040': patch(
        'Aşağıdakilerden hangileri koşullara ilişkin olarak doğrudur?\n\nI. Koşula bağlı hakkı tehlikeye düşürülen alacaklı koruyucu önlemler alabilir\n\nII. Koşul, tarafın bizzat yapması gereken bir davranış değilse mirasçı onun yerine geçebilir\n\nIII. Hukuka aykırı bir fiili sağlamaya yönelik koşula bağlı işlem, koşul gerçekleşince geçerli olur',
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'II ve III',
            'D': 'Yalnız II',
            'E': 'I, II ve III',
        },
        'A',
        "TBK m. 171/2'ye göre hakkı tehlikeye düşürülen alacaklı önlem alabilir (I); m. 174'e göre bizzat yapılması gereken bir davranış değilse mirasçı yerine geçebilir (II). m. 176'ya göre böyle bir koşula bağlı işlem **kesin hükümsüzdür** (III yanlış).",
        '6098 sayılı TBK m. 171, 174, 176',
    ),
    # düzey 2
    '0041': patch(
        "A'nın çalışanı B, temsil sıfatını belirtmeden bir kırtasiyeden peşin ödemeyle kâğıt almıştır. Kırtasiye için satışın B'ye veya A'ya yapılması farksızdır. Satış sözleşmesinin sonuçları hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Kırtasiyenin seçimine göre belirlenir',
            'B': "Alacağın devri hükümleriyle A'ya geçer",
            'C': "Temsil sıfatı bildirilmediğinden B'ye aittir",
            'D': "Kiminle yapıldığı farksız olduğundan A'ya aittir",
            'E': 'B ile A arasında yarı yarıya paylaşılır',
        },
        'D',
        "TBK m. 40/2'ye göre temsil sıfatı bildirilmese de **hukuki işlemi temsilci veya temsil olunandan biri ile yapması karşı taraf için farksız ise**, işlemin sonuçları doğrudan temsil olunana ait olur.",
        '6098 sayılı TBK m. 40/2',
    ),
    # düzey 3
    '0042': patch(
        "A, B'ye verdiği temsil yetkisinde 'bu yetkiyi hiçbir zaman geri almayacağım' kaydına yer vermiştir. Daha sonra yetkiyi geri almak istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Yetki üçüncü kişilere bildirilmişse geri alma da onlara bildirilmelidir',
            'B': 'Temsil olunan verdiği yetkiyi sınırlayabilir veya geri alabilir',
            'C': 'Temsil olunan bu hakkından önceden feragat edemez',
            'D': 'Önceden yapılan feragat nedeniyle A yetkiyi geri alamaz',
            'E': 'Aradaki vekâlet ilişkisinden doğan haklar saklıdır',
        },
        'D',
        "TBK m. 42'ye göre temsil olunan, hukuki işlemden doğan temsil yetkisini **her zaman sınırlayabilir veya geri alabilir** ve **bu hakkından önceden feragat edemez**; taraflar arasındaki hizmet, vekâlet veya ortaklık ilişkilerinden doğan haklar saklıdır.",
        '6098 sayılı TBK m. 42',
    ),
    # düzey 2
    '0043': patch(
        "Yetkisi sona eren temsilci, yetki belgesini temsil olunan A'ya geri vermemiş; A da belgenin geri alınması için bir girişimde bulunmamıştır. Eski temsilci bu belgeyle iyiniyetli üçüncü kişiye zarar vermiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Üçüncü kişi kötüniyetli olsaydı bu korumadan yararlanamazdı',
            'B': 'Yetkisi sona eren temsilci belgeyi geri vermelidir',
            'C': 'Zarardan eski temsilci sorumludur, A sorumlu tutulamaz',
            'D': 'A, belgenin geri alınması için gerekeni yapmamıştır',
            'E': 'A, iyiniyetli üçüncü kişinin zararını gidermelidir',
        },
        'C',
        "TBK m. 44'e göre yetki sona erince temsilci belgeyi geri vermekle yükümlüdür; **temsil olunan veya halefleri, temsilcinin belgeyi geri vermesi için gerekeni yapmazlarsa, bundan dolayı iyiniyetli üçüncü kişilerin zararını gidermekle** yükümlüdür.",
        '6098 sayılı TBK m. 44',
    ),
    # düzey 3
    '0044': patch(
        "Yetkisiz temsilci B'nin A adına yaptığı işlemi A onamamıştır. Karşı taraf C, işlem sırasında B'nin yetkisiz olduğunu bilmiyordu ve bilmesi de gerekmiyordu. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "Hakkaniyet gerektirirse kusurlu B'den diğer zararlar da istenebilir",
            'B': "İşlem A'yı bağlamaz",
            'C': "C bilseydi veya bilmesi gerekseydi B'den zarar istenemezdi",
            'D': "C, işlemin geçersizliğinden doğan zararını B'den isteyemez",
            'E': "C, işlemin geçersizliğinden doğan zararını B'den isteyebilir",
        },
        'D',
        "TBK m. 47'ye göre temsil olunan işlemi onamazsa **geçersizlikten doğan zararın giderilmesi yetkisiz temsilciden istenebilir**; ancak temsilci, karşı tarafın yetkisizliği bildiğini veya bilmesi gerektiğini ispat ederse sorumlu olmaz. Hakkaniyet gerektirirse kusurlu yetkisiz temsilciden diğer zararlar da istenebilir.",
        '6098 sayılı TBK m. 47',
    ),
    # düzey 2
    '0045': patch(
        "A, B ve C, 90.000 ₺'lik bir borçtan müteselsilen sorumludur. Alacaklı, borcun tamamını B'den istemiştir.\n\nTBK'ya göre bu durumla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Borçluların her biri borcun tamamından sorumludur',
            'B': 'Alacaklı borcun bir kısmını da isteyebilir',
            'C': "Alacaklı B'den payı olan 30.000 ₺'yi isteyebilir, fazlasını isteyemez",
            'D': "B'nin ödemesi diğer borçluları da alacaklıya karşı kurtarır",
            'E': 'B, payını aşan ödeme için diğerlerine rücu edebilir',
        },
        'C',
        'TBK m. 163: alacaklı, müteselsil borçlulardan her birinden borcun tamamını veya bir kısmını isteyebilir; borcun tamamı ödenmedikçe bütün borçluların sorumluluğu devam eder. m. 166-167: ödeme diğerlerini de kurtarır; payını aşan ödeme yapan borçlu diğerlerine rücu eder.',
        '6098 sayılı TBK m. 163',
    ),
    # düzey 3
    '0046': patch(
        "A, B ve C, alacaklı D'ye 90.000 ₺ müteselsilen borçludur. A'nın D'den 30.000 ₺'lik muaccel alacağı vardır ve A bunu takas etmiştir. D, kalan alacağı için B'ye başvurmuştur. B'nin D'ye ödemesi gereken tutar en fazla kaç ₺'dir?",
        {
            'A': '20.000',
            'B': '90.000',
            'C': '60.000',
            'D': '30.000',
            'E': '45.000',
        },
        'C',
        "TBK m. 166/1'e göre **borçlulardan biri ifa veya takasla borcun tamamını veya bir kısmını sona erdirmişse, bu oranda diğer borçluları da borçtan kurtarmış** olur: 90.000 − 30.000 = **60.000 ₺**.",
        '6098 sayılı TBK m. 166/1',
    ),
    # düzey 3
    '0047': patch(
        "A, B ve C, borçlu D'ye karşı 60.000 ₺'lik alacağın müteselsil alacaklılarıdır; aralarında paylar eşittir. Borçlu D, borcun tamamını A'ya ödemiştir. A'nın B'ye ödemesi gereken tutar kaç ₺'dir?",
        {
            'A': '60.000',
            'B': '20.000',
            'C': '40.000',
            'D': '0',
            'E': '30.000',
        },
        'B',
        "TBK m. 169'a göre borçlu, alacaklılardan birine yaptığı ifayla bütün alacaklılara karşı borcundan kurtulur; aksi kararlaştırılmadıkça alacaklıların hakları eşittir ve **kendisine düşen paydan fazlasını elde eden alacaklı, bu fazlalığı payını alamamış diğer alacaklılara** öder: 60.000 / 3 = **20.000 ₺**.",
        '6098 sayılı TBK m. 169',
    ),
    # düzey 2
    '0048': patch(
        "Baba, oğluna 'üniversite sınavını kazanırsan sana bir otomobil alacağım' diyerek yazılı bir bağışlama vaadinde bulunmuştur.\n\nTBK'ya göre bu vaatle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Vaat geciktirici koşula bağlıdır',
            'B': 'Koşul gerçekleşmeden vaat hüküm doğurmaz',
            'C': 'Vaat hemen hüküm doğurur; sınav kaybedilirse sona erer',
            'D': 'Koşul gerçekleşince hüküm kural olarak o andan doğar',
            'E': 'Bağışlama vaadi yazılı şekle tabidir',
        },
        'C',
        "TBK m. 170: bir sözleşmenin hüküm doğurması gerçekleşip gerçekleşmeyeceği belli olmayan bir olguya bağlanmışsa sözleşme geciktirici koşula bağlıdır; koşulun gerçekleşmesiyle, kural olarak o andan itibaren hüküm doğurur. Bağışlama vaadi m. 288'e göre yazılı şekle tabidir.",
        '6098 sayılı TBK m. 170',
    ),
    # düzey 2
    '0049': patch(
        'Bir kira sözleşmesinde, kiracının yurt dışına tayini çıkarsa sözleşmenin sona ereceği kararlaştırılmıştır. Kiracının tayini sözleşmenin altıncı ayında çıkmıştır; sözleşmede başka bir hüküm yoktur. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Sona erme kural olarak geçmişe etkili olmaz',
            'B': 'Tayinden önceki aylara ait kiralar geri istenemez',
            'C': 'Sözleşme bozucu koşula bağlanmıştır',
            'D': 'Sözleşmenin hükümleri tayinle ortadan kalkar',
            'E': 'Ödenen kiralar iade edilir',
        },
        'E',
        "TBK m. 173'e göre sona ermesi gerçekleşip gerçekleşmeyeceği bilinmeyen bir olguya bırakılan sözleşme **bozucu koşula** bağlıdır; hükümleri koşulun gerçekleştiği anda ortadan kalkar ve aksi kararlaştırılmadıkça **sona erme geçmişe etkili olmaz**.",
        '6098 sayılı TBK m. 173',
    ),
    # düzey 3
    '0050': patch(
        "Emlakçı B'ye, taşınmaz satılırsa komisyon ödenmesi kararlaştırılmıştır. Malik A, komisyon ödememek için B'nin bulduğu alıcıyla B'den habersiz görüşmeleri keserek satışı bir süre sonra aynı alıcıya doğrudan yapmıştır. Aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Koşul gerçekleşmiş sayılır; B komisyonu isteyebilir',
            'B': 'Koşul gerçekleşmemiş sayılır',
            'C': 'Satış emlakçı aracılığıyla yapılmadığından komisyon doğmaz',
            'D': 'Emlakçı ancak masraflarını isteyebilir',
            'E': 'Sözleşme kesin hükümsüzdür',
        },
        'A',
        "TBK m. 175/1'e göre **taraflardan biri, koşulun gerçekleşmesine dürüstlük kurallarına aykırı olarak engel olursa, koşul gerçekleşmiş sayılır**.",
        '6098 sayılı TBK m. 175/1',
    ),
    # düzey 2
    '0051': patch(
        "Bedeli 500.000 ₺ olan bir satış sözleşmesi yapılırken alıcı, niteliği ayrıca belirtilmeden satıcıya 50.000 ₺ vermiştir. Aksine yerel âdet yoktur. Alıcının teslimde ödeyeceği kalan tutar kaç ₺'dir?",
        {
            'A': '500.000',
            'B': '400.000',
            'C': '550.000',
            'D': '475.000',
            'E': '450.000',
        },
        'E',
        "TBK m. 177'ye göre sözleşme yapılırken verilen para, **cayma parası olarak değil sözleşmenin yapıldığına kanıt olarak** verilmiş sayılır (bağlanma parası) ve aksine sözleşme veya yerel âdet olmadıkça **esas alacaktan düşülür**: 500.000 − 50.000 = **450.000 ₺**.",
        '6098 sayılı TBK m. 177',
    ),
    # düzey 3
    '0052': patch(
        'Bir tedarik sözleşmesinde, malın hiç teslim edilmemesi hâlinde satıcının 100.000 ₺ ceza ödeyeceği kararlaştırılmıştır. Satıcı malı teslim etmemiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Aksi anlaşılmadıkça alıcı ya ifayı ya cezayı isteyebilir',
            'B': 'Alıcı teslimi ve cezayı birlikte isteyebilir',
            'C': 'Alıcı cezayı seçerse malın teslimini ayrıca isteyemez',
            'D': 'Alıcının zarara uğramamış olması cezanın istenmesine engel değildir',
            'E': 'Satıcı cezayı ödeyerek dönme yetkisi olduğunu ispat edebilir',
        },
        'B',
        "TBK m. 179/1'e göre sözleşmenin **hiç veya gereği gibi ifa edilmemesi** için ceza kararlaştırılmışsa, aksi sözleşmeden anlaşılmadıkça alacaklı **ya borcun ya da cezanın** ifasını isteyebilir (seçimlik ceza). m. 179/3 borçluya ispat hakkı tanır; m. 180/1'e göre zarar şartı yoktur.",
        '6098 sayılı TBK m. 179/1',
    ),
    # düzey 2
    '0053': patch(
        'Bir sözleşmede gecikme hâlinde 30.000 ₺ ceza ödeneceği kararlaştırılmıştır. Borçlu gecikmiş, ancak alacaklı bu gecikmeden hiçbir zarar görmemiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ceza ancak zarar kadar istenebilir',
            'B': 'Zarar olmasa da cezanın ifası gerekir',
            'C': 'Ceza yarı oranda istenebilir',
            'D': 'Ceza ağır kusurda istenebilir',
            'E': 'Zarar olmadığından ceza istenemez',
        },
        'B',
        "TBK m. 180/1'e göre **alacaklı hiçbir zarara uğramamış olsa bile, kararlaştırılan cezanın ifası gerekir**; hâkimin aşırı cezayı indirme yetkisi (m. 182/3) saklıdır.",
        '6098 sayılı TBK m. 180/1',
    ),
    # düzey 3
    '0054': patch(
        'Bir yazılım geliştirme sözleşmesinde, iş sahibi ödemede temerrüde düşer ve yüklenici sözleşmeden dönerse, o güne kadar yapılan ödemelerin yükleniciye kalacağı kararlaştırılmıştır. Yüklenici dönmüştür ve iş sahibi 300.000 ₺ ödemiş durumdadır. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ceza koşulu hükümleri uygulanır; hâkim indirebilir',
            'B': 'Kayıt ancak iş sahibi tacirse geçerlidir',
            'C': 'Yüklenici ödemeleri indirimsiz alıkoyar',
            'D': 'Kayıt kesin hükümsüzdür',
            'E': 'Kayıt bağlanma parası hükmündedir',
        },
        'A',
        "TBK m. 181'e göre **ceza koşuluna ilişkin hükümler, dönme durumunda ifa edilmiş olan kısmın alacaklıya kalacağını öngören sözleşmelere de uygulanır** (kısmi ifanın yanması); dolayısıyla m. 182/3'teki indirim yetkisi de uygulanır. Taksitle satışa ilişkin hükümler saklıdır.",
        '6098 sayılı TBK m. 181',
    ),
    # düzey 3
    '0055': patch(
        "B, yetkisi olmadığı hâlde A adına C'den bir araç kiralamıştır. A durumu öğrenince aracı kullanmaya başlamış ve ilk ayın kirasını C'ye ödemiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'A, işlemi davranışıyla onamış sayılabilir',
            'B': "Onama için A'nın yazılı beyanı gerekir",
            'C': "Onamayla birlikte işlem A'yı bağlar",
            'D': "Onamadan önce işlem A'yı bağlamaz",
            'E': "C, onama için A'ya uygun bir süre verebilirdi",
        },
        'B',
        "TBK m. 46'ya göre yetkisiz temsilcinin işlemi **onandığı takdirde** temsil olunanı bağlar. Onama için bir şekil öngörülmemiştir; aracı kullanıp kirayı ödemek gibi **örtülü davranışlar da onama** sayılabilir.",
        '6098 sayılı TBK m. 46',
    ),
    # düzey 3
    '0056': patch(
        "A, B ve C, 120.000 ₺'lik müteselsil borçta iç ilişkide sırasıyla %50, %25 ve %25 paya sahip olduklarını kararlaştırmıştır. B borcun tamamını alacaklıya ödemiştir. B, A'dan kaç ₺ isteyebilir?",
        {
            'A': '120.000',
            'B': '40.000',
            'C': '90.000',
            'D': '60.000',
            'E': '30.000',
        },
        'D',
        "TBK m. 167'ye göre paylar kural olarak eşittir; ancak **aksi kararlaştırılabilir**. Fazla ödeyen borçlu her borçluya **ancak payı oranında** rücu eder: A'nın payı 120.000 × %50 = **60.000 ₺**.",
        '6098 sayılı TBK m. 167',
    ),
    # düzey 3
    '0057': patch(
        'İki sürücünün birlikte kusurlu hareketiyle bir yaya yaralanmıştır. Sürücüler arasında müteselsil sorumluluk konusunda hiçbir anlaşma yoktur. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Her sürücü yarı zarardan sorumludur',
            'B': 'İç paylaşımda kusurun ağırlığı göz önünde tutulur',
            'C': 'Payını aşan tutarı ödeyen sürücü diğerine rücu edebilir',
            'D': 'Yaya, zararın tamamını sürücülerden birinden isteyebilir',
            'E': 'Kanun bu durumda müteselsil sorumluluk öngörmüştür',
        },
        'A',
        "TBK m. 162/2'ye göre bildirim yoksa müteselsil borçluluk **kanunda öngörülen hâllerde** doğar. TBK m. 61, birlikte zarar verenler için **müteselsil sorumluluk** öngörür; m. 62'ye göre iç ilişkide kusurun ağırlığı ve tehlikenin yoğunluğu dikkate alınır, fazla ödeyen rücu eder.",
        '6098 sayılı TBK m. 61, 62',
    ),
    # düzey 2
    '0058': patch(
        "A, B ve C, alacaklıya 60.000 ₺ müteselsilen borçludur. Alacaklı A'dan 20.000 ₺ tahsil etmiştir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': "A'nın ödemesi diğerlerini de 20.000 ₺ oranında kurtarır",
            'B': "B ve C, 20.000'er ₺'den sorumludur",
            'C': 'A da kalan borçtan sorumlu olmaya devam eder',
            'D': 'Kalan 40.000 ₺ borçlulardan herhangi birinden istenebilir',
            'E': 'Sorumluluk borcun tamamı ödeninceye kadar sürer',
        },
        'B',
        "TBK m. 163'e göre alacaklı borcun tamamını veya bir kısmını dilediği borçludan isteyebilir ve **sorumluluk borcun tamamı ödeninceye kadar** devam eder; m. 166/1'e göre A'nın ifası diğerlerini ödenen oranda kurtarır.",
        '6098 sayılı TBK m. 163, 166/1',
    ),
    # düzey 2
    '0059': patch(
        'Bir hizmet sözleşmesinde, işverenin şirketinin tasfiyeye girmesi hâlinde sözleşmenin sona ereceği ve bu sona ermenin sözleşme başlangıcına etkili olacağı kararlaştırılmıştır. Şirket tasfiyeye girmiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bozucu koşulda sona erme, kararlaştırılsa da geçmişe etkili olamaz',
            'B': 'Sona erme, sözleşme başlangıcına kadar geriye yürür',
            'C': 'Koşul geciktirici koşuldur',
            'D': 'Sona erme ancak tasfiye bitince hüküm doğurur',
            'E': 'Kayıt kesin hükümsüzdür',
        },
        'B',
        "TBK m. 173/3'e göre bozucu koşulun gerçekleşmesiyle sona erme, **aksi kararlaştırılmadıkça veya işin niteliğinden anlaşılmadıkça** geçmişe etkili olmaz. Taraflar geçmişe etkiyi kararlaştırdığından sona erme geriye yürür.",
        '6098 sayılı TBK m. 173/3',
    ),
    # düzey 3
    '0060': patch(
        'Aşağıdakilerden hangileri temsile ilişkin olarak doğrudur?\n\nI. Temsilcinin iflası, aksi kararlaştırılmadıkça temsil yetkisini sona erdirir\n\nII. Yetkisi sona eren temsilci yetki belgesini geri vermekle yükümlüdür\n\nIII. Onanmayan işlemde yetkisizliği bilmeyen karşı taraf, yetkisiz temsilciden zararını isteyebilir',
        {
            'A': 'I, II ve III',
            'B': 'I ve II',
            'C': 'Yalnız I',
            'D': 'I ve III',
            'E': 'II ve III',
        },
        'A',
        "TBK m. 43'e göre temsilcinin iflası yetkiyi sona erdirir (I); m. 44'e göre yetki belgesi geri verilir (II); m. 47'ye göre onanmayan işlemde, yetkisizliği bilmeyen ve bilmesi gerekmeyen karşı taraf **geçersizlikten doğan zararını** yetkisiz temsilciden isteyebilir (III).",
        '6098 sayılı TBK m. 43-47',
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
    print(f"1 paket / {len(PATCHES)} soru ('Borc Iliskilerinde Ozel Durumlar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
