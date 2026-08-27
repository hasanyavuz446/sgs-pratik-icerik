#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Borcun Ifasi ve Sona Ermesi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Tanim kalibindan olay + kural uygulamasina: medyan kok 119->259, olumsuz kok %8->%37, oncullu %12->%12, kor ogrenci %25.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: TBK m. 78/2, 83, 84, 89, 90, 97, 100, 101, 103, 104, 106-109, 112, 117-120, 124-126, 131-133, 135, 136, 139, 143, 146, 147, 149, 154, 160, 161, 186 (resmi metinden dogrulandi)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/borclar_hukuku/borcun_ifasi_sona_ermesi.json"
STYLE_REF = "SGS Hukuk (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "ifa-gen-"


def patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": '6098 sayili Turk Borclar Kanunu'},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Bir mobilya atölyesi, siparişi veren müşteriye özel tasarım bir masayı bizzat ustabaşının yapması kararlaştırılmadan üretmeyi üstlenmiştir. Atölye sahibi hastalanınca işi, aynı nitelikte çalışan bir başka marangoza yaptırmış; müşteri ise edimin borçlu tarafından şahsen yerine getirilmediğini ileri sürerek teslimi kabul etmemiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Borçlunun hastalığı ifa imkânsızlığı sayılacağından borç sona ermiş, müşterinin talep hakkı düşmüştür',
            'B': 'Borcun bizzat borçlu tarafından ifasında alacaklının menfaati bulunmadığından ifa geçerlidir ve müşteri teslimden kaçınamaz',
            'C': 'Üçüncü kişi ifayı yaptığı için borç sona ermez, yalnızca alacaklı ile üçüncü kişi arasında yeni bir sözleşme kurulur',
            'D': 'Üçüncü kişinin ifası ancak alacaklının önceden yazılı onayı alınmışsa borcu sona erdirir',
            'E': 'Edim bir eser meydana getirmeye ilişkin olduğundan borç her hâlükârda borçlunun şahsen ifasını gerektirir',
        },
        'B',
        '**TBK m. 83:** borcun bizzat borçlu tarafından ifa edilmesinde alacaklının menfaati bulunmadıkça borçlu, borcunu şahsen ifa etmekle yükümlü değildir. Olayda edim, kişisel nitelik taşıdığı kararlaştırılmamış sıradan bir üretim işidir; aynı nitelikte bir marangozun ifası borcu sona erdirir. Alacaklının onayı aranmaz.',
    ),
    # düzey 2
    '0002': patch(
        "Bir tacirin, tedarikçisine 90.000 ₺ tutarında muaccel ve miktarı çekişmesiz bir borcu vardır. Tacir vade günü kasasındaki 50.000 ₺'yi ödemek istemiş, tedarikçi ise borcun tamamı belli ve muaccel olduğu gerekçesiyle bu ödemeyi kabul etmemiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': 'Tedarikçi kısmen ifayı reddedebilir; borcun tamamı belli ve muaccel olduğundan bu ret hukuka uygundur',
            'B': 'Tedarikçi kısmi ifayı reddedemez; borç bölünebilir nitelikte olduğundan alacaklının kabul yükümlülüğü doğar ve ret hâlinde kendisi temerrüde düşer',
            'C': 'Borç bölünebilir nitelikte olduğundan tedarikçinin kısmi ifayı kabul etmesi zorunludur',
            'D': 'Tedarikçi kısmi ifayı reddederse kendisi alacaklı temerrüdüne düşer ve tevdi külfeti doğar',
            'E': 'Kısmi ifanın reddi ancak sözleşmede bu yönde açık bir hüküm bulunmasına bağlıdır',
        },
        'A',
        '**TBK m. 84/1:** borcun tamamı belli ve muaccel ise alacaklı kısmen ifayı reddedebilir. Reddi haklı olduğundan alacaklı temerrüdü doğmaz. (m. 84/2 yalnız alacaklının kısmi ifayı KABUL etmesi hâlinde borçlunun ikrar ettiği kısmı ifadan kaçınamayacağını düzenler.)',
    ),
    # düzey 2
    '0003': patch(
        'Bir alacaklı, borçlusundan olan para alacağının vadesinden önce yerleşim yerini başka bir ile taşımıştır. Vade geldiğinde borçlu, sözleşmede ifa yeri kararlaştırılmadığını, bu nedenle ödemeyi kendi yerleşim yerinde yapacağını bildirmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Para borçları borçlunun sözleşme kurulduğu andaki yerleşim yerinde ifa edilir, sonraki taşınma sonucu değiştirmez',
            'B': 'İfa yeri kararlaştırılmamışsa borç, sözleşmenin kurulduğu yerde ifa edilir; sonradan meydana gelen yer değişiklikleri borçluya yeni bir külfet yükleyemez',
            'C': 'Para borçları alacaklının ödeme zamanındaki yerleşim yerinde ifa edilir; borçlu alacaklının yeni yerleşim yerinde ödemekle yükümlüdür',
            'D': 'Alacaklının yer değiştirmesi ifa yerini etkilemez; borçlu dilediği yerde tevdi ederek borcundan kurtulur',
            'E': 'Para borçlarında ifa yeri her zaman borçlunun bulunduğu yerdir; aksi ancak resmî şekilde kararlaştırılabilir',
        },
        'C',
        '**TBK m. 89/1-1:** aksine anlaşma yoksa para borçları, **alacaklının ödeme zamanındaki yerleşim yerinde** ifa edilir (götürülecek borç). Belirleyici an sözleşmenin kurulduğu an değil, ödeme anıdır; alacaklının vadeden önceki taşınması ifa yerini değiştirir.',
    ),
    # düzey 2
    '0004': patch(
        'İki tacir arasında yapılan sözleşmede edimin ne zaman yerine getirileceği kararlaştırılmamış, hukuki ilişkinin özelliğinden de bir süre anlaşılmamaktadır. Alacaklı, sözleşmenin kurulduğu gün edimi talep etmiş; borçlu ise kendisine makul bir hazırlık süresi tanınması gerektiğini savunmuştur. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Borç muaccel olmadığından alacaklının talebi geçersizdir; muacceliyet ancak yazılı bildirimle doğar',
            'B': 'Ticari işlerde ifa zamanı belirlenmemişse kanunen otuz günlük hazırlık süresi işlemeye başlar',
            'C': 'Süre kararlaştırılmadığı için borç, alacaklının ihtarından itibaren işleyecek makul bir sürenin sonunda muaccel olur',
            'D': 'İfa zamanı kararlaştırılmadığından borç doğumu anında muaccel olmuştur ve alacaklı derhâl ifayı isteyebilir',
            'E': 'İfa zamanı belirlenmemiş borçlarda muacceliyet için hâkimden süre belirlenmesi istenmesi zorunludur',
        },
        'D',
        '**TBK m. 90:** ifa zamanı taraflarca kararlaştırılmadıkça veya hukuki ilişkinin özelliğinden anlaşılmadıkça **her borç doğumu anında muaccel olur**. Alacaklı derhâl ifayı isteyebilir; borçluya kanunen ayrı bir hazırlık süresi tanınmaz.',
    ),
    # düzey 3
    '0005': patch(
        'Bir borçlunun alacaklısına 200.000 ₺ anapara ve buna işlemiş 20.000 ₺ faiz borcu vardır. Borçlu faiz ödemelerinde hiç gecikmemiştir. Borçlu 60.000 ₺ ödeme yaparken bu tutarın anaparadan düşülmesini istemiş, alacaklı ise ödemenin önce işlemiş faize sayılması gerektiğini savunmuştur. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Anaparaya mahsup ancak alacaklının bu yönde yazılı muvafakat vermesiyle mümkün olur',
            'B': 'Faiz işlemiş olduğundan borçlunun kısmi ödeme yapma hakkı ortadan kalkmıştır',
            'C': 'Mahsubun sırasını alacaklı belirler; borçlunun bu yönde bir talep hakkı bulunmaz',
            'D': 'Kısmi ödemeler öncelikle işlemiş faize, artan bölüm anaparaya sayılır; borçlunun mahsup sırasını belirleme yetkisi bulunmadığından talebi sonuç doğurmaz',
            'E': 'Borçlu faiz ve giderleri ödemede gecikmediğinden kısmi ödemeyi anaparadan düşme hakkına sahiptir',
        },
        'E',
        '**TBK m. 100/1:** borçlu, **faiz veya giderleri ödemede gecikmemiş ise** kısmen yaptığı ödemeyi ana borçtan düşme hakkına sahiptir ve **aksine anlaşma yapılamaz**. Olayda faiz ödemelerinde gecikme bulunmadığından tercih borçlunundur.',
    ),
    # düzey 3
    '0006': patch(
        'Bir kiracı, kiraya verene ödediği Ağustos ayı kira bedeli için alacaklıdan hiçbir çekince içermeyen bir makbuz almıştır. Kiraya veren daha sonra Haziran ve Temmuz kiralarının ödenmediğini ileri sürerek bu iki ayın bedelini talep etmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Çekince belirtilmeksizin verilen makbuz önceki dönem edimlerinin de ifa edildiği karinesini doğurur; kiraya veren aksini ispatlamadıkça talepte bulunamaz',
            'B': 'Kiraya veren çekince koymamış olsa da dönemsel edimlerde karine borçlu aleyhine işler ve ispat yükü kiracıdadır',
            'C': 'Makbuz yalnız üzerinde yazılı tutar için geçerli olup önceki dönemler ancak borçlunun ikrarıyla ifa edilmiş sayılır',
            'D': 'Her dönem edimi bağımsız olduğundan sonraki aya ait makbuz önceki aylar bakımından sonuç doğurmaz; kiraya veren iki ayın bedelini talep edebilir',
            'E': 'Önceki dönemlerin ifa edilmiş sayılması için makbuzun resmî şekilde düzenlenmiş olması gerekir',
        },
        'A',
        '**TBK m. 104/1:** faiz veya kira bedeli gibi **dönemsel edimlerden biri için alacaklı tarafından çekince belirtilmeksizin makbuz verilmişse, önceki dönemlere ait edimler de ifa edilmiş sayılır.** Bu bir karinedir; aksini ispat külfeti alacaklıya düşer.',
    ),
    # düzey 2
    '0007': patch(
        'Bir borçlu, borcunun tamamını ödedikten sonra alacaklıdan hem makbuz hem de borç senedinin geri verilmesini istemiştir. Alacaklı makbuz vermiş, ancak senedi elinde tutmakta ısrar etmiştir. Buna göre borçlunun hakları bakımından aşağıdaki ifadelerden hangisi **yanlıştır**?',
        {
            'A': 'Alacaklının senedi geri vermekten kaçınması borçluya, ifadan kaçınma imkânı verecek bir aykırılık oluşturur',
            'B': 'Borcun tamamı ödenmemişse borçlu yalnızca makbuz ile senede ödemenin işlenmesini isteyebilir',
            'C': 'Borcun tamamı ödendiğinden borçlu, borç senedinin geri verilmesini veya iptalini isteyebilir',
            'D': 'Borçlu yalnızca makbuz isteyebilir; borç senedinin geri verilmesini veya iptalini talep etme hakkı bulunmaz',
            'E': 'Borç senedi alacaklıya başkaca haklar da veriyorsa borçlu senedin üzerine ödemenin yazılmasını isteyebilir',
        },
        'D',
        '**TBK m. 103:** borcu ödeyen borçlu **bir makbuz ve borcun tamamı ödenmişse borç senedinin geri verilmesini veya iptalini** isteyebilir. Yanlış olan şık, borçlunun senet üzerindeki hakkını tümüyle reddettiği için hükme aykırıdır.',
    ),
    # düzey 2
    '0008': patch(
        'Bir borçlunun aynı alacaklıya doğmuş üç ayrı borcu bulunmaktadır. Borçlu ödeme günü bir tutar ödemiş, hangi borcu ödediğini alacaklıya bildirmemiş ve alacaklının verdiği makbuzda gösterilen mahsuba da derhâl itiraz etmemiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Bildirim yapılmadığında ödeme, borçlar arasında tutarları oranında paylaştırılarak mahsup edilir',
            'B': 'Borçlu bildirimde bulunmadığı ve makbuzdaki mahsuba derhâl itiraz etmediği için ödeme, makbuzda gösterilen borca mahsup edilmiş sayılır',
            'C': 'Borçlu bildirimde bulunmamışsa ödeme geçersiz sayılır ve borçların hiçbiri sona ermez',
            'D': 'Bildirim yapılmadığında ödeme en eski tarihli borca mahsup edilir; alacaklının makbuzda gösterdiği borç bu sıralamayı değiştiremez',
            'E': 'Mahsubun hangi borca yapılacağını yalnızca hâkim belirleyebilir; tarafların iradesi sonuca etkili değildir',
        },
        'B',
        '**TBK m. 101:** birden çok borcu bulunan borçlu ödeme gününde hangisini ödediğini bildirebilir; **bildirimde bulunmazsa yapılan ödeme, kendisi tarafından derhâl itiraz edilmiş olmadıkça** alacaklının makbuzda gösterdiği borca mahsup edilir.',
    ),
    # düzey 2
    '0009': patch(
        "Bir satıcının alıcıya karşı 40.000 ₺ tutarındaki para borcu 1 Mart tarihinde muaccel olmuş, ancak sözleşmede ifa günü ayrıca kararlaştırılmamıştır. Alacaklı 20 Nisan'a kadar hiçbir bildirimde bulunmamış, bu tarihte borçluya ihtar çekmiştir. Buna göre borçlunun temerrüde düştüğü an bakımından aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': "İhtar çekilmiş olsa da temerrüt ancak dava açılmasıyla doğar; 20 Nisan'ın bir etkisi yoktur",
            'B': "Borç 1 Mart'ta muaccel olduğundan borçlu aynı tarihte kendiliğinden temerrüde düşmüş, temerrüt faizi de o günden itibaren işlemeye başlamıştır",
            'C': 'Alacaklı uzun süre sessiz kaldığından ihtar hakkını yitirmiş, borç temerrütsüz hâle gelmiştir',
            'D': 'Para borçlarında ihtar aranmaz; temerrüt muacceliyet tarihinde kendiliğinden doğar ve faiz o günden işler',
            'E': "Borç muaccel olmakla birlikte ifa günü belirlenmediğinden temerrüt, 20 Nisan'daki ihtarla doğmuştur",
        },
        'E',
        '**TBK m. 117/1:** muaccel bir borcun borçlusu **alacaklının ihtarıyla** temerrüde düşer. İfa günü birlikte belirlenmiş olsaydı (m. 117/2) ihtara gerek kalmaksızın vade gününde temerrüt doğardı; olayda gün belirlenmediği için temerrüt ihtar tarihinde başlar.',
    ),
    # düzey 2
    '0010': patch(
        'Bir sözleşmede edimin 15 Eylül günü yerine getirileceği taraflarca birlikte kararlaştırılmıştır. Borçlu bu tarihte edimi yerine getirmemiş, alacaklı ise herhangi bir ihtar çekmemiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': "İfa günü birlikte belirlendiğinden borçlu, ihtara gerek olmaksızın 15 Eylül'ün geçmesiyle temerrüde düşmüştür",
            'B': 'Belirli vadeli borçlarda temerrüt, vadeyi izleyen otuzuncu günün sonunda kendiliğinden doğar',
            'C': 'Vade belirlenmiş olsa dahi temerrüt için alacaklının ayrıca uygun bir süre vermesi zorunludur',
            'D': 'Alacaklı ihtar çekmediği sürece temerrüt doğmaz; vadenin belirlenmiş olması yalnız muacceliyeti sağlar, temerrüdün ayrıca ihtarla kurulması gerekir',
            'E': 'Temerrüt ancak borçlunun kusurunun alacaklı tarafından ispatlanmasıyla doğar',
        },
        'A',
        '**TBK m. 117/2:** borcun ifa edileceği gün birlikte belirlenmişse borçlu, **bu günün geçmesiyle ihtara gerek olmaksızın** temerrüde düşer. Kusur temerrüdün şartı değildir; kusursuzluk yalnız gecikme tazminatından kurtulmak için ileri sürülebilir (m. 118).',
    ),
    # düzey 2
    '0011': patch(
        'Borçlu temerrüdünde gecikme tazminatı ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Para borçlarında alacaklı, ayrıca zarara uğradığını ispat etmeksizin temerrüt faizi isteyebilir',
            'B': 'Borçlu, temerrüde düşmekte kusuru olmadığını ispat ederse gecikme zararından sorumlu olmaz',
            'C': 'Gecikme zararı bakımından kusursuzluğun ispatı borçluya düşer; alacaklıya kusur ispatı yüklenmez',
            'D': 'Temerrüdün doğması için borçlunun kusuru aranmaz; kusur yalnız tazminat aşamasında değerlendirilir',
            'E': 'Borçlu temerrüde düşmekte kusuru olmadığını ispat etse dahi gecikme zararından sorumlu tutulur',
        },
        'E',
        '**TBK m. 118:** temerrüde düşen borçlu, **kusuru olmadığını ispat etmedikçe** gecikme zararından sorumludur; ispat başarılırsa sorumluluk doğmaz. Bu imkânı tümüyle kaldıran ifade yanlıştır.',
    ),
    # düzey 3
    '0012': patch(
        'Temerrüde düşmüş bir borçlunun elindeki, alacaklıya teslim edilecek ferden belirlenmiş mal, temerrüt sırasında meydana gelen ve borçluya hiçbir biçimde yüklenemeyecek nitelikteki bir olay sonucu zarar görmüştür. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Zarar temerrüt sırasında doğduğundan hasar kendiliğinden alacaklıya geçmiş sayılır',
            'B': 'Temerrüde düşen borçlu beklenmedik hâlden de sorumlu olur; ancak temerrüde düşmekte kusuru bulunmadığını veya malın alacaklıya teslim edilseydi de zarara uğrayacağını ispat ederse sorumluluktan kurtulur',
            'C': 'Borçlu temerrütte olduğu için sorumluluğu mutlaktır ve hiçbir ispatla bundan kurtulamaz',
            'D': 'Beklenmedik hâl sorumluluğu kaldırdığından borçlu zarardan sorumlu tutulmaz; temerrüdün varlığı yalnız gecikme tazminatı bakımından sonuç doğurur',
            'E': 'Beklenmedik hâlden sorumluluk yalnızca para borçlarında doğar, parça borçlarında uygulanmaz',
        },
        'B',
        '**TBK m. 119:** temerrüde düşen borçlu **beklenmedik hâlden doğan zarardan da sorumludur**; ancak temerrüde düşmekte kusuru olmadığını ya da edimi zamanında ifa etseydi bile alacaklının bu zarara uğrayacağını ispat ederek sorumluluktan kurtulabilir.',
    ),
    # düzey 2
    '0013': patch(
        'Bir para borcunda taraflar temerrüt faizi oranını sözleşmede kararlaştırmamıştır. Alacaklı, temerrüde düşen borçludan piyasa koşullarına göre kendi belirlediği bir oran üzerinden faiz talep etmektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Oran kararlaştırılmadığından temerrüt faizi, faiz borcunun doğduğu tarihte yürürlükte olan mevzuata göre belirlenir',
            'B': 'Oran kararlaştırılmadığında alacaklı, uğradığı zararı ispat ederek talep ettiği oranı isteyebilir; kanuni oran yalnız ispat yapılamadığında uygulanır',
            'C': 'Oran belirlenmemişse anapara faizi oranı aynen temerrüt faizine uygulanır ve artırılamaz',
            'D': 'Sözleşmede oran yoksa temerrüt faizi hiç işlemez; alacaklı yalnız anaparayı isteyebilir',
            'E': 'Temerrüt faizi oranını hâkim, tarafların ekonomik durumunu gözeterek takdir eder; kanunda bağlayıcı bir ölçüt yer almaz',
        },
        'A',
        '**TBK m. 120/1:** uygulanacak yıllık temerrüt faizi oranı **sözleşmede kararlaştırılmamışsa, faiz borcunun doğduğu tarihte yürürlükte olan mevzuat hükümlerine göre** belirlenir. Alacaklının tek taraflı oran belirlemesi mümkün değildir.',
    ),
    # düzey 3
    '0014': patch(
        'Karşılıklı borç yükleyen bir sözleşmede borçlu temerrüde düşmüş, alacaklı ona uygun bir süre vermiş, borçlu bu süre içinde de borcunu ifa etmemiştir. Buna göre alacaklının seçimlik hakları bakımından aşağıdaki ifadelerden hangisi **yanlıştır**?',
        {
            'A': 'Sözleşmeden dönen alacaklı, karşılıklı olarak ifa yükümlülüğünden kurtulur ve verdiğini geri isteyebilir',
            'B': 'Alacaklı derhâl bildirimde bulunarak sözleşmeden dönme hakkını kullanabilir',
            'C': 'Alacaklı ifa ve gecikme tazminatı isteme hakkından vazgeçtiğini bildirerek borcun ifa edilmemesinden doğan zararın giderilmesini isteyebilir',
            'D': 'Alacaklı sözleşmeden dönerse dönmenin sonucu olarak müspet (olumlu) zararının giderilmesini isteyebilir',
            'E': 'Alacaklı her zaman borcun ifasını ve gecikme sebebiyle tazminat ödenmesini isteyebilir',
        },
        'D',
        '**TBK m. 125:** alacaklı ya ifa + gecikme tazminatı ister, ya ifadan vazgeçip **ifa edilmemesinden** doğan zararın (müspet zarar) giderilmesini ister, ya da sözleşmeden döner. Dönme hâlinde istenebilecek olan **menfi (olumsuz) zarardır**; yanlış olan şık dönme ile müspet zararı birleştirdiği için hükme aykırıdır.',
    ),
    # düzey 3
    '0015': patch(
        'İfasına başlanmış sürekli edimli bir sözleşmede borçlu temerrüde düşmüştür. Alacaklı, sözleşmenin geçmişe etkili biçimde ortadan kalkmasını ve baştan itibaren verdiği bütün edimlerin iadesini talep etmektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Alacaklı fesih hâlinde yalnız işlemiş edimleri isteyebilir, erken sona ermeden doğan zararı isteyemez',
            'B': 'Fesih ancak hâkim kararıyla mümkün olduğundan alacaklının tek taraflı bildirimi sonuç doğurmaz',
            'C': 'Sürekli edimli sözleşmelerde alacaklı kural olarak sözleşmeyi feshederek ileriye etkili sonuç doğurur ve süresinden önce sona ermeden doğan zararını isteyebilir',
            'D': 'Sürekli edimli sözleşmelerde temerrüt hükümleri hiç uygulanmaz; yalnız genel hükümlere gidilir',
            'E': 'Alacaklı bu sözleşmelerde de dönme hakkını kullanarak sözleşmeyi geçmişe etkili biçimde ortadan kaldırır ve o güne kadar verdiği bütün edimleri geri isteyebilir',
        },
        'C',
        '**TBK m. 126:** ifasına başlanmış sürekli edimli sözleşmelerde borçlunun temerrüdü hâlinde alacaklı, ifa ve gecikme tazminatı isteyebileceği gibi **sözleşmeyi feshederek** sözleşmenin süresinden önce sona ermesi yüzünden uğradığı zararın giderilmesini isteyebilir. Fesih ileriye etkilidir.',
    ),
    # düzey 2
    '0016': patch(
        'Borçlu temerrüdü ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Muaccel bir borçta ifa günü birlikte belirlenmemişse temerrüt, alacaklının ihtarıyla doğar.\n\nII. Temerrüde düşen borçlu, temerrüde düşmekte kusuru olmadığını ispat ederse gecikme tazminatından sorumlu olmaz.\n\nIII. Karşılıklı borç yükleyen sözleşmelerde alacaklı, süre verilmesini gerektirmeyen bir durum varsa süre vermeksizin seçimlik haklarını kullanabilir.',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'Yalnız III',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'A',
        'Üçü de doğrudur. **I:** m. 117/1 ihtar kuralı. **II:** m. 118 kusursuzluk ispatı. **III:** m. 125/1, borçluya süre verilmesini gerektirmeyen durumlarda (m. 124) alacaklı doğrudan seçimlik haklarına başvurabilir.',
    ),
    # düzey 2
    '0017': patch(
        'Bir borçlu, sözleşmeye uygun biçimde hazırladığı malı kararlaştırılan gün alacaklıya usulüne uygun olarak önermiş; alacaklı haklı bir sebep göstermeksizin malı teslim almaktan kaçınmıştır. Buna göre aşağıdaki ifadelerden hangisi **yanlıştır**?',
        {
            'A': 'Gereği gibi önerilen edimi haklı sebep olmaksızın kabulden kaçınan alacaklı temerrüde düşer',
            'B': 'Borçlu, hasar ve giderleri kendisine ait olmak üzere teslim edeceği şeyi tevdi ederek borcundan kurtulabilir; tevdi giderleri alacaklıya yüklenemez',
            'C': 'Alacaklının kabulden kaçınması borcu sona erdirir ve borçlunun edimi saklama yükümlülüğü kendiliğinden ortadan kalkar',
            'D': 'Tevdi yerini kural olarak ifa yerindeki hâkim belirler',
            'E': 'Alacaklının, borçlunun ifa edebilmesi için yapması gereken hazırlık fiillerinden kaçınması da temerrüde yol açar',
        },
        'C',
        '**TBK m. 106:** gereği gibi önerilen edimi haklı sebep olmaksızın kabulden veya kendisine düşen hazırlık fiillerini yapmaktan kaçınan alacaklı temerrüde düşer. Alacaklı temerrüdü borcu **kendiliğinden sona erdirmez**; borçlu ancak **m. 107** uyarınca tevdi ederek borcundan kurtulur — yanlış olan şık budur.',
    ),
    # düzey 3
    '0018': patch(
        'Alacaklı temerrüdünde tevdi ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Tevdi yerini kural olarak ifa yerindeki hâkim belirler',
            'B': 'Tevdi ile borç kesin olarak sona erdiğinden borçlunun tevdi edilen şeyi geri alma imkânı bulunmaz',
            'C': "Tevdi edilen şey geri alındığı anda alacak, fer'ileriyle birlikte yeniden doğar",
            'D': 'Alacaklı tevdi edileni kabul ettiğini açıklamadıkça borçlu kural olarak tevdi edilen şeyi geri alabilir',
            'E': 'Borçlu, hasar ve giderleri alacaklıya ait olmak üzere teslim edeceği şeyi tevdi ederek borcundan kurtulabilir',
        },
        'B',
        "**TBK m. 109:** alacaklı kabulünü açıklamadıkça veya tevdi bir rehnin kaldırılması sonucunu doğurmadıkça **borçlu tevdi edileni geri alabilir** ve alacak fer'ileriyle canlanır. Geri almayı tümüyle reddeden ifade yanlıştır.",
    ),
    # düzey 3
    '0019': patch(
        'Bir alacaklı, kendisine gereği gibi önerilen parayı kabul etmemiş; borçlu da parayı tevdi etmemiş ve elinde tutmuştur. Alacaklı daha sonra borçludan temerrüt faizi talep etmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Temerrüt faizi kamu düzenine ilişkin olduğundan alacaklının kendi temerrüdü sonucu etkilemez',
            'B': 'Alacaklı temerrüdü yalnız parça borçlarında söz konusu olduğundan para borcunda hüküm doğurmaz',
            'C': 'Borçlu parayı tevdi etmediği için borçlu temerrüdü ortadan kalkmaz; temerrüt faizi alacaklının kabulden kaçındığı dönem boyunca da işlemeye devam eder',
            'D': 'İki taraf da temerrütte olduğundan faiz yarı oranında indirilerek hesaplanır',
            'E': 'Alacaklı temerrüde düştüğünden borçlu temerrüdünün sonuçları doğmaz ve alacaklı bu dönem için temerrüt faizi isteyemez',
        },
        'E',
        'Alacaklının haklı sebep olmaksızın kabulden kaçınması onu **m. 106 uyarınca temerrüde** düşürür. Borçlu temerrüdünün şartları (m. 117) gerçekleşmediğinden gecikme faizi ve gecikme tazminatı istenemez; tevdi (m. 107) borçlu için bir külfet değil, borçtan kurtulma **imkânıdır**.',
    ),
    # düzey 2
    '0020': patch(
        'Taraflar, resmî şekilde düzenlenmiş bir sözleşmeden doğan borcu adi yazılı bir ibra sözleşmesiyle tamamen ortadan kaldırmışlardır. Alacaklı sonradan, borcu doğuran işlem resmî şekle tabi olduğu için ibranın da resmî şekilde yapılması gerektiğini ileri sürmüştür. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'İbra tek taraflı bir irade açıklamasıdır; borçlunun katılımı aranmadığından şekil tartışması konusuz kalır',
            'B': 'Borcu doğuran işlem resmî şekle tabi ise ibra da aynı şekilde yapılmadıkça geçersizdir',
            'C': 'Borcu doğuran işlem şekle bağlı olsa bile ibra sözleşmesi şekle bağlı olmaksızın yapılabilir; ibra geçerlidir',
            'D': 'İbra ancak borcun tamamı için yapılabilir; kısmi ibra geçerli sayılmadığından borcun bir bölümünü ortadan kaldırmak isteyen taraflar yenilemeye başvurmalıdır',
            'E': 'İbranın geçerliliği alacaklının borçludan karşı edim almasına bağlıdır',
        },
        'C',
        '**TBK m. 132:** borcu doğuran işlem kanunen veya taraflarca belli bir şekle bağlı tutulmuş olsa bile borç, tarafların **şekle bağlı olmaksızın** yapacakları ibra sözleşmesiyle **tamamen veya kısmen** ortadan kaldırılabilir. İbra bir sözleşmedir; iki tarafın uyuşan iradesini gerektirir.',
    ),
    # düzey 2
    '0021': patch(
        'Bir borçlu, mevcut para borcu için alacaklıya bir bono (kambiyo senedi) vermiştir. Taraflar senedin verilmesiyle eski borcun sona ereceği yönünde açık bir irade ortaya koymamıştır. Alacaklı daha sonra eski borca dayanarak talepte bulununca borçlu, borcun yenileme ile sona erdiğini savunmuştur. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Yenileme iradesi açık olmasa da senedin kabul edilmiş olması örtülü yenileme anlamına gelir',
            'B': 'Yenileme yalnız yazılı sözleşmeyle mümkün olduğundan senedin hiçbir hukuki sonucu doğmaz',
            'C': 'Kambiyo senedi verilmesi kanunen yenileme sayıldığından eski borç sona ermiş, alacaklının elinde yalnız senetten doğan talep hakkı kalmıştır',
            'D': "Senet verilmesiyle eski borç sona erer, ancak fer'i haklar aynen devam eder",
            'E': 'Mevcut borç için kambiyo taahhüdünde bulunulması, tarafların açık yenileme iradesi olmadıkça yenileme sayılmaz; eski borç varlığını sürdürür',
        },
        'E',
        '**TBK m. 133:** yeni bir borçla mevcut bir borcun sona erdirilmesi **ancak tarafların bu yöndeki açık iradesiyle** olur; özellikle mevcut borç için **kambiyo taahhüdünde bulunulması veya yeni bir alacak ya da kefalet senedi düzenlenmesi**, açık yenileme iradesi olmadıkça yenileme sayılmaz.',
    ),
    # düzey 3
    '0022': patch(
        'Bir kişi, kendisine 150.000 ₺ borcu olan babasının tek mirasçısı olarak mirası kayıtsız şartsız kabul etmiş; böylece alacaklı ve borçlu sıfatları aynı kişide birleşmiştir. Alacak üzerinde ise birleşmeden önce kurulmuş bir üçüncü kişi rehni bulunmaktadır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Birleşme borcu sona erdirdiğinden üçüncü kişinin alacak üzerindeki rehin hakkı da düşer; rehin veren bu durumda yalnız kişisel talep hakkını korur',
            'B': 'Birleşme borcu sona erdirmez; yalnız alacağın talep edilebilirliğini geçici olarak durdurur',
            'C': 'Sıfatların birleşmesiyle borç sona erer; ancak üçüncü kişinin alacak üzerinde önceden mevcut olan hakkı birleşmeden etkilenmez',
            'D': 'Birleşmenin sonuç doğurabilmesi için üçüncü kişinin buna yazılı olarak onay vermesi gerekir',
            'E': 'Mirasın kabulü hâlinde borç sona ermez, mirasçının kişisel malvarlığına aynen geçer ve talep edilebilir kalır',
        },
        'C',
        '**TBK m. 135:** alacaklı ve borçlu sıfatlarının aynı kişide birleşmesiyle borç sona erer; ancak **üçüncü kişilerin alacak üzerinde önceden mevcut olan hakları birleşmeden etkilenmez.** Birleşme geçmişe etkili olarak ortadan kalkarsa borç varlığını sürdürür.',
    ),
    # düzey 2
    '0023': patch(
        'Bir asıl borç, borçlunun tam ifasıyla sona ermiştir. Borç için daha önce kefalet verilmiş, ayrıca rehin kurulmuş ve ceza koşulu kararlaştırılmıştı. Alacaklı, asıl borç sona ermiş olsa da kefile ve rehne başvurabileceğini ileri sürmektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Asıl borç sona erdiğinden rehin, kefalet, faiz ve ceza koşulu gibi ona bağlı hak ve borçlar da sona ermiştir',
            'B': "Fer'i haklar asıl borçtan bağımsızdır; alacaklı asıl borç ifayla sona ermiş olsa dahi kefile ve rehne başvurarak alacağını yeniden tahsil edebilir",
            'C': 'Yalnız kefalet sona erer; rehin ve ceza koşulu ayrı bir sözleşmeye dayandığından varlığını korur',
            'D': "Asıl borcun ifayla sona ermesi fer'i hakları etkilemez, yalnız yenileme hâlinde bunlar düşer",
            'E': "Fer'i hakların sona ermesi için ayrıca alacaklının ibra beyanında bulunması gerekir",
        },
        'A',
        '**TBK m. 131/1:** asıl borç ifa ya da diğer bir sebeple sona erdiğinde **rehin, kefalet, faiz ve ceza koşulu gibi buna bağlı hak ve borçlar da sona erer.** (İşlemiş faiz ve ceza koşulu bakımından m. 131/2 sözleşmeyle veya ifa anına kadar yapılacak bildirimle saklı tutulma imkânı tanır.)',
    ),
    # düzey 3
    '0024': patch(
        "(A), (B)'den olan 30.000 ₺ tutarındaki muaccel para alacağını, (B)'ye olan 50.000 ₺ tutarındaki muaccel para borcuyla takas ettiğini (B)'ye bildirmiştir. Buna göre borçların durumu bakımından aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': 'Takas beyanıyla her iki borç da tamamen sona erer; tutar farkı bakımından taraflar arasında yeni bir alacak veya borç ilişkisi doğmaz',
            'B': "Her iki borç, takas edilebilecekleri anda daha az olan borç tutarı olan 30.000 ₺ oranında sona erer; (A)'nın 20.000 ₺ borcu devam eder",
            'C': 'Takas ancak borçların tutarları eşit olduğunda mümkün olduğundan beyan sonuç doğurmaz',
            'D': 'Takas beyanı yalnız gelecek için sonuç doğurur; beyandan önceki dönem için borçların ikisi de tam olarak varlığını sürdürür',
            'E': "Borçlar 50.000 ₺ oranında sona erer; (B)'nin (A)'dan 20.000 ₺ alacağı doğar",
        },
        'B',
        "**TBK m. 143/1:** takas, borçlunun takas iradesini alacaklıya bildirmesiyle gerçekleşir ve **her iki borç, takas edilebilecekleri anda daha az olan borç tutarınca sona erer.** Küçük olan 30.000 ₺ olduğundan (A)'nın borcundan geriye 20.000 ₺ kalır.",
    ),
    # düzey 2
    '0025': patch(
        'Bir kişi, karşı taraftan olan buğday alacağını, karşı tarafa olan para borcuyla takas etmek istemektedir. Her iki borç da muaccel ve çekişmesizdir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Buğday alacağı paraya çevrilerek takas kendiliğinden gerçekleşir; ayrı bir beyana gerek yoktur',
            'B': 'Her iki borç da muaccel olduğundan edimlerin cinsi önem taşımaz; takas beyanıyla buğday alacağı para alacağına çevrilerek borçlar sona erer',
            'C': 'Takas için edimlerin özdeş olması aranmaz; yalnız tutarların denk olması yeterlidir',
            'D': 'Edimler özdeş olmadığından takas mümkün değildir; takas ancak karşılıklı para veya özdeş diğer edimlerde söz konusu olur',
            'E': 'Takas ancak her iki alacak da çekişmeli olduğunda mümkündür; olayda bu şart gerçekleşmemiştir',
        },
        'D',
        '**TBK m. 139/1:** takas için taraflar **karşılıklı olarak bir miktar para veya özdeş diğer edimleri** birbirine borçlu olmalı ve **her iki borç muaccel** bulunmalıdır. Buğday ile para özdeş edim olmadığından takas şartı gerçekleşmez.',
    ),
    # düzey 2
    '0026': patch(
        'İki taraf birbirine karşılıklı olarak muaccel para borcu altındadır; alacaklardan biri taraflar arasında çekişmelidir. Borçlulardan biri takas beyanında bulunmuş, diğeri ise çekişmeli alacağın takasa konu olamayacağını ileri sürmüştür. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Alacaklardan biri çekişmeli olsa bile takas ileri sürülebilir',
            'B': 'Çekişme bulunduğunda takas kendiliğinden gerçekleşir, ayrıca beyana gerek kalmaz',
            'C': 'Çekişmeli alacak takasa engel olduğundan beyan hiçbir sonuç doğurmaz',
            'D': 'Takas ancak çekişme mahkeme kararıyla giderildikten sonra ileri sürülebilir',
            'E': 'Çekişmeli alacakta takas yalnız tacirler arasında mümkündür',
        },
        'A',
        '**TBK m. 139/2:** alacaklardan biri çekişmeli olsa bile takas ileri sürülebilir. Ancak takas, kendiliğinden değil **m. 143/1 uyarınca takas iradesinin bildirilmesiyle** gerçekleşir.',
    ),
    # düzey 3
    '0027': patch(
        'Takas ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Takasın gerçekleşmesi için her iki borcun muaccel olması gerekir.\n\nII. Takas, tarafların anlaşmasına gerek olmaksızın, borçlunun takas iradesini alacaklıya bildirmesiyle gerçekleşir.\n\nIII. Takas beyanı üzerine borçlar, beyanın yapıldığı andan itibaren ileriye etkili olarak sona erer.',
        {
            'A': 'II ve III',
            'B': 'Yalnız II',
            'C': 'I, II ve III',
            'D': 'Yalnız I',
            'E': 'I ve II',
        },
        'E',
        '**I doğru:** m. 139/1 her iki borcun muaccel olmasını arar. **II doğru:** m. 143/1, takasın tek taraflı bildirimle gerçekleştiğini düzenler. **III yanlış:** borçlar beyandan itibaren değil, **takas edilebilecekleri andan itibaren** ve daha az olan tutarınca sona erer; beyanın etkisi geçmişe yürür.',
    ),
    # düzey 3
    '0028': patch(
        'Bir galeri sahibi, sattığı ancak henüz teslim etmediği ferden belirlenmiş bir tabloyu, kendisine hiçbir kusur yüklenemeyecek bir yangında kaybetmiştir. Alıcı bedeli peşin ödemiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'İmkânsızlık borcu sona erdirmez; satıcı aynı nitelikte başka bir tablo temin etmekle yükümlüdür',
            'B': 'Borç kusursuz imkânsızlık sebebiyle sona erer; satıcı almış olduğu bedeli sebepsiz zenginleşme hükümleri uyarınca geri vermekle yükümlüdür',
            'C': 'Borç sona erse de satıcı aldığı bedeli kendiliğinden iade etmekle yükümlü değildir; alıcı bedeli ancak sözleşmeden dönerek geri isteyebilir',
            'D': 'Satıcı kusursuz olsa dahi imkânsızlıktan sorumlu tutulur ve alıcının müspet zararını karşılar',
            'E': 'Bedelin iadesi ancak sözleşmede bu yönde açık bir hüküm bulunması hâlinde istenebilir',
        },
        'B',
        '**TBK m. 136:** borcun ifası borçlunun sorumlu tutulamayacağı sebeplerle imkânsızlaşırsa borç sona erer. Karşılıklı borç yükleyen sözleşmelerde borçtan kurtulan borçlu, **karşı taraftan almış olduğu edimi sebepsiz zenginleşme hükümleri uyarınca geri vermekle** yükümlüdür.',
    ),
    # düzey 2
    '0029': patch(
        'Bir yüklenici, taahhüt ettiği işi kararlaştırılan nitelikte yerine getirmemiş; iş sahibi bundan doğan zararının giderilmesini istemiştir. Yüklenici, zararın kendi kusurundan kaynaklanmadığını ileri sürmektedir. Buna göre ispat yükü bakımından aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Alacaklı, borçlunun kusurlu olduğunu ispat etmedikçe tazminat isteyemez; borca aykırılıkta kusur karinesi alacaklı aleyhine işler',
            'B': 'Kusurun varlığı karine olarak alacaklı aleyhine kabul edilir ve borçlu ispat yükünden bağımsızdır',
            'C': 'Borç gereği gibi ifa edilmediğinden borçlu, kendisine hiçbir kusurun yüklenemeyeceğini ispat etmedikçe zarardan sorumludur',
            'D': 'İspat yükü, zararın miktarı belirlendikten sonra hâkim tarafından taraflar arasında paylaştırılır',
            'E': 'Gereği gibi ifa etmeme hâlinde kusur aranmaz; borçlu her hâlükârda kusursuz sorumluluğa tabidir',
        },
        'C',
        '**TBK m. 112:** borç hiç veya gereği gibi ifa edilmezse borçlu, **kendisine hiçbir kusurun yüklenemeyeceğini ispat etmedikçe** alacaklının bundan doğan zararını gidermekle yükümlüdür. Kusursuzluğun ispatı borçluya düşer (kusur karinesi).',
    ),
    # düzey 2
    '0030': patch(
        'Borcun sona ermesi hâlleri ile ilgili aşağıdaki ifadelerden hangisi **yanlıştır**?',
        {
            'A': 'Alacaklı ve borçlu sıfatlarının aynı kişide birleşmesi borcu sona erdirir; üçüncü kişilerin alacak üzerindeki önceki hakları da bu sona ermeden etkilenir',
            'B': 'Borcun ifasının borçlunun kusuruyla imkânsızlaşması da borcu sona erdirir ve borçlu herhangi bir tazminat yükümlülüğü altına girmez',
            'C': 'İbra sözleşmesi, borcu doğuran işlem şekle bağlı olsa bile şekle bağlı olmaksızın yapılabilir',
            'D': 'Takas beyanı, her iki borcu takas edilebilecekleri anda daha az olan tutarınca sona erdirir',
            'E': 'Borcun ifasının borçlunun sorumlu tutulamayacağı sebeplerle imkânsızlaşması borcu sona erdirir',
        },
        'B',
        "Kusurlu imkânsızlıkta borç aynen ifa edilemez hâle gelir; ancak **m. 112** uyarınca borçlu kusursuzluğunu ispat edemediği için **tazminat sorumluluğu doğar**. Tazminatsız sona erme yalnız **m. 136**'daki kusursuz imkânsızlıkta söz konusudur — yanlış olan şık budur.",
    ),
    # düzey 2
    '0031': patch(
        'Zamanaşımı süreleri ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Kira bedelleri, anapara faizleri ve ücret gibi dönemsel edimler beş yıllık zamanaşımına tabidir',
            'B': 'Kanunda aksine bir hüküm bulunmadıkça her alacak on yıllık zamanaşımına tabidir',
            'C': 'Zamanaşımı kural olarak alacağın muaccel olmasıyla işlemeye başlar',
            'D': 'Ticari nitelikteki alacaklar, kanunda aksine hüküm bulunmasa dahi beş yıllık zamanaşımına tabidir',
            'E': 'Muacceliyetin bir bildirime bağlı olduğu hâllerde süre, bildirimin yapılabileceği günden işler',
        },
        'D',
        "**TBK m. 146:** kanunda aksine hüküm yoksa **her alacak on yıllık** zamanaşımına tabidir; alacağın ticari nitelikte olması tek başına beş yıllık süreye tabi kılmaz. Beş yıllık süre m. 147'de sayılan dönemsel edimler içindir.",
    ),
    # düzey 2
    '0032': patch(
        "Bir işveren, işçisine ödemediği ücret alacağı bakımından zamanaşımı def'inde bulunmak istemektedir. Ücretin muaccel olduğu tarihten itibaren altı yıl geçmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': 'Ücret alacakları genel süreye tabi olduğundan on yıl dolmadan zamanaşımı ileri sürülemez',
            'B': 'Ücret gibi dönemsel edimler beş yıllık zamanaşımına tabi olduğundan alacak zamanaşımına uğramıştır',
            'C': 'Dönemsel edimlerde zamanaşımı yalnız sözleşmede kararlaştırılmışsa uygulanır',
            'D': 'İşçi alacakları zamanaşımına uğramaz; her zaman dava edilebilir',
            'E': "Ücret alacaklarında zamanaşımı süresi iki yıl olduğundan def'i çok daha önce ileri sürülebilirdi",
        },
        'B',
        '**TBK m. 147/1:** kira bedelleri, anapara faizleri ve **ücret gibi diğer dönemsel edimler** beş yıllık zamanaşımına tabidir. Muacceliyetten itibaren altı yıl geçtiğinden süre dolmuştur.',
    ),
    # düzey 3
    '0033': patch(
        "Bir alacağın muaccel olması, alacaklının borçluya yapacağı bir bildirime bağlanmıştır. Alacaklı bu bildirimi yapabileceği tarihten üç yıl sonra bildirimi yapmış ve hemen ardından dava açmıştır. Borçlu zamanaşımı def'inde bulunmuştur. Buna göre zamanaşımının başlangıcı bakımından aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': 'Alacaklı bildirimi geciktirdiği sürece zamanaşımı hiç işlemez',
            'B': 'Bildirime bağlı alacaklarda zamanaşımı ancak dava tarihinden itibaren işler',
            'C': 'Zamanaşımı, sözleşmenin kurulduğu tarihten itibaren işlemeye başlar',
            'D': 'Zamanaşımı, bildirimin fiilen yapıldığı tarihten itibaren işlemeye başlar; alacaklının bildirimi geciktirmesi süreyi kendiliğinden uzatır',
            'E': 'Muacceliyetin bir bildirime bağlı olduğu hâllerde zamanaşımı, bildirimin yapılabileceği günden işlemeye başlar',
        },
        'E',
        '**TBK m. 149:** zamanaşımı alacağın muaccel olmasıyla işlemeye başlar; **muacceliyetin bir bildirime bağlı olduğu hâllerde zamanaşımı, bu bildirimin yapılabileceği günden** işlemeye başlar. Aksi hâlde alacaklı bildirimi geciktirerek süreyi süresiz uzatabilirdi.',
    ),
    # düzey 2
    '0034': patch(
        'Zamanaşımının kesilmesi bakımından aşağıdaki hâllerden hangisi **zamanaşımını kesen bir sebep değildir**?',
        {
            'A': 'Alacaklının borçluya alacağını hatırlatan yazılı bir ihtar göndermesi ve borçlunun buna sessiz kalması',
            'B': "Alacaklının dava veya def'i yoluyla mahkemeye başvurması",
            'C': 'Borçlunun alacak için rehin vermesi veya kefil göstermesi, borcu ikrar niteliği taşıdığından zamanaşımını keser ve süre yeniden işlemeye başlar',
            'D': 'Borçlunun borcu ikrar etmesi, özellikle faiz ödemesi veya kısmen ifada bulunması',
            'E': 'Alacaklının icra takibinde bulunması veya iflas masasına başvurması',
        },
        'A',
        "**TBK m. 154:** zamanaşımı, borçlunun borcu ikrarı (faiz ödeme, kısmi ifa, rehin verme, kefil gösterme) ile alacaklının dava, def'i, icra takibi veya iflas masasına başvurusuyla kesilir. **Tek taraflı ihtar zamanaşımını kesmez** — yanlış olan şık budur.",
    ),
    # düzey 2
    '0035': patch(
        'Zamanaşımına ilişkin sözleşme hükümleri bakımından aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Zamanaşımı ileri sürülmedikçe hâkim bunu kendiliğinden göz önüne alamaz',
            'B': 'Müteselsil borçlulardan birinin feragat etmiş olması diğerlerine karşı ileri sürülemez',
            'C': "Borçlu, sözleşme kurulurken zamanaşımı def'inde bulunmayacağını taahhüt ederse bu taahhüt geçerli olur",
            'D': 'Zamanaşımından önceden feragat edilemez',
            'E': 'Borçlunun borcu ikrar etmesi zamanaşımını keser ve süre yeniden işlemeye başlar',
        },
        'C',
        "**TBK m. 160:** **zamanaşımından önceden feragat edilemez**; sözleşme kurulurken def'iden vazgeçme taahhüdü geçersizdir. Diğer şıklar m. 160/2, m. 161 ve m. 154'e uygundur.",
    ),
    # düzey 2
    '0036': patch(
        "Zamanaşımına uğramış bir alacak için açılan davada borçlu, zamanaşımı def'ini ileri sürmemiştir. Hâkim, dosyadan sürenin dolduğunu görmüş ve davayı kendiliğinden reddetmeyi düşünmektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': "Zamanaşımı def'i yalnız ilk itiraz olarak ileri sürülebilir; süresi geçtiğinde hâkim resen inceler",
            'B': "Zamanaşımı kamu düzenine ilişkin sayıldığından hâkim bunu resen dikkate alır ve def'i ileri sürülmese bile davayı süre yönünden reddeder",
            'C': 'Hâkim zamanaşımını resen dikkate alabilir, ancak bunu taraflara önceden bildirmesi gerekir',
            'D': 'Zamanaşımı ileri sürülmedikçe hâkim bunu kendiliğinden göz önüne alamaz; davanın bu gerekçeyle reddi mümkün değildir',
            'E': "Borçlu def'i ileri sürmemişse alacak kendiliğinden zamanaşımından arınmış sayılır ve süre yeniden işler",
        },
        'D',
        "**TBK m. 161:** zamanaşımı ileri sürülmedikçe **hâkim bunu kendiliğinden göz önüne alamaz.** Zamanaşımı bir **def'i**dir; itiraz değildir ve kamu düzenine ilişkin sayılmaz.",
    ),
    # düzey 2
    '0037': patch(
        'Bir borçlu, on yıllık zamanaşımı süresi dolmuş olan borcunu, süresinin dolduğunu bilerek ve kendi isteğiyle ödemiştir. Ödemeden sonra bu tutarı sebepsiz zenginleşme hükümlerine dayanarak geri istemektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Zamanaşımına uğramış bir borcun ifasından kaynaklanan zenginleşme geri istenemez; borçlu ödediğini talep edemez',
            'B': 'Zamanaşımı borcu tümüyle ortadan kaldırdığından yapılan ödeme sebepsizdir ve geri istenebilir',
            'C': 'Zamanaşımına uğramış borcun ödenmesi yenileme sayılır ve yeni bir on yıllık süre başlar',
            'D': 'Ödeme geçerli olmakla birlikte borçlu, ödediği tutarın faizini alacaklıdan isteyebilir',
            'E': 'Geri isteme hakkı yalnız borçlunun süreyi bilmeden ödemiş olması hâlinde doğar; bilerek ödemede de aynı sonuç geçerlidir',
        },
        'A',
        '**TBK m. 78/2:** **zamanaşımına uğramış bir borcun ifasından** veya ahlaki bir ödevin yerine getirilmesinden kaynaklanan zenginleşmeler **geri istenemez.** Zamanaşımı borcu sona erdirmez; onu dava edilemez (eksik) borç hâline getirir.',
    ),
    # düzey 2
    '0038': patch(
        'Zamanaşımı ile ilgili aşağıdaki ifadelerden hangisi **yanlıştır**?',
        {
            'A': 'Zamanaşımı kural olarak alacağın muaccel olmasıyla işlemeye başlar',
            'B': 'Kanunda aksine hüküm bulunmayan alacaklar on yıllık zamanaşımına tabidir; bu süre kanunla belirlendiğinden taraflarca değiştirilemez',
            'C': 'Zamanaşımının dolması alacağı tümüyle sona erdirdiğinden borçlunun bu borcu ödemesi hâlinde ödediğini geri isteme hakkı doğar',
            'D': 'Borçlunun borcu ikrar etmesi veya kısmen ifada bulunması zamanaşımını keser',
            'E': 'Kira bedelleri, anapara faizleri ve ücret gibi dönemsel edimler beş yıllık zamanaşımına tabidir',
        },
        'C',
        "Zamanaşımı alacağı **sona erdirmez**; alacak eksik borca dönüşür ve **m. 78/2** uyarınca ödenen tutar geri istenemez. Diğer şıklar sırasıyla m. 146, m. 147, m. 149 ve m. 154'e uygundur.",
    ),
    # düzey 2
    '0039': patch(
        'Bir alacaklı, borçludan olan alacağını üçüncü bir kişiye devretmiş; ancak devir ne devreden ne de devralan tarafından borçluya bildirilmiştir. Borçlu, devirden habersiz biçimde ve iyiniyetle önceki alacaklıya ödeme yapmıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Devrin geçerliliği borçlunun onayına bağlı olduğundan devir hiç hüküm doğurmamıştır',
            'B': 'Devir kendisine bildirilmediğinden borçlu, önceki alacaklıya iyiniyetle yaptığı ifayla borcundan kurtulur',
            'C': 'Borçlu, devri araştırmakla yükümlü olduğundan iyiniyeti korunmaz ve devralana yeniden ödeme yapar',
            'D': 'Borçlu ancak ödemeyi noter aracılığıyla yapmışsa borcundan kurtulmuş sayılır',
            'E': 'Devirle alacak devralana geçtiğinden borçlunun önceki alacaklıya yaptığı ödeme borcu sona erdirmez; borçlu devralana yeniden ödemek durumunda kalır',
        },
        'B',
        '**TBK m. 186:** borçlu, alacağın devredildiği kendisine bildirilmemişse **önceki alacaklıya iyiniyetle ifada bulunarak borcundan kurtulur.** Bildirim külfeti devreden veya devralana aittir; risk borçluya yüklenmez.',
    ),
    # düzey 2
    '0040': patch(
        'Karşılıklı borç yükleyen sözleşmelerde ifa sırası ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Sözleşmenin koşullarına göre daha sonra ifa etme hakkı bulunan taraf, önce ifa etmeksizin talepte bulunabilir',
            'B': "Ödemezlik def'i ileri sürüldüğünde karşı taraf, kendi ediminin ifasına kadar ifadan kaçınabilir",
            'C': "Kendi borcunu ifa etmeyen tarafın talebine karşı diğer taraf ödemezlik def'ini ileri sürebilir",
            'D': 'İfa isteminde bulunan taraf kendi borcunu ifa etmemiş olsa da karşı taraf ifadan kaçınamaz',
            'E': 'İfa isteminde bulunan tarafın kural olarak kendi borcunu ifa etmiş ya da ifasını önermiş olması gerekir',
        },
        'D',
        "**TBK m. 97:** ifa isteminde bulunan tarafın, daha sonra ifa etme hakkı olmadıkça **kendi borcunu ifa etmiş ya da ifasını önermiş olması gerekir**; aksi hâlde karşı taraf ödemezlik def'iyle ifadan kaçınır.",
    ),
    # düzey 3
    '0041': patch(
        'Bir alacaklı, temerrüde düşen borçluya süre vermeden doğrudan sözleşmeden dönmüştür. Borçlunun tutumundan, kendisine süre verilmesinin sonuçsuz kalacağı açıkça anlaşılmaktadır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Süre verme külfeti yalnız para borçlarında aranır; diğer borçlarda hiç aranmaz',
            'B': 'Borçlunun tutumundan süre verilmesinin etkisiz olacağı anlaşıldığından alacaklı süre vermeksizin seçimlik haklarını kullanabilir',
            'C': 'Alacaklı süre vermemişse yalnız ifa ve gecikme tazminatı isteyebilir, dönemez',
            'D': 'Süre verilmesi karşılıklı borç yükleyen sözleşmelerde zorunlu bir aşama olduğundan alacaklının süre vermeden yaptığı dönme beyanı sonuç doğurmaz',
            'E': 'Süre verilmeksizin dönme ancak hâkim kararıyla mümkündür',
        },
        'B',
        "**TBK m. 124/1:** borçlunun içinde bulunduğu durumdan veya tutumundan **süre verilmesinin etkisiz olacağı anlaşılıyorsa** süre verilmesine gerek yoktur. Bu hâlde alacaklı m. 125'teki seçimlik haklarını doğrudan kullanabilir.",
    ),
    # düzey 2
    '0042': patch(
        'Anapara faizi ile temerrüt faizi arasındaki fark bakımından aşağıdaki ifadelerden hangisi **yanlıştır**?',
        {
            'A': 'Temerrüt faizi ancak sözleşmede kararlaştırılmışsa istenebilir; oran belirlenmemişse hiç faiz işlemez',
            'B': 'Anapara faizi, sermayenin kullanılmasının karşılığı olarak borcun vadesine kadar işleyen faizdir',
            'C': 'Temerrüt faizi, borçlunun temerrüde düşmesinden sonra gecikme sebebiyle işleyen faizdir',
            'D': 'Sözleşmeyle kararlaştırılacak oran, kanuni orana göre kanunda öngörülen üst sınırı aşamaz',
            'E': 'Her iki faizde de oran sözleşmede kararlaştırılmamışsa faiz borcunun doğduğu tarihte yürürlükteki mevzuata göre belirlenir',
        },
        'A',
        '**TBK m. 120/1** (temerrüt faizi) ve **m. 88/1** (anapara faizi) paralel düzenlemedir: oran kararlaştırılmamışsa **mevzuata göre belirlenir**. Temerrüt faizinin sözleşme şartına bağlı olduğunu söyleyen şık bu nedenle yanlıştır.',
    ),
    # düzey 3
    '0043': patch(
        'Alacaklısı temerrüde düşen bir borçlunun teslim etmesi gereken şey, niteliği gereği tevdi edilmeye elverişli değildir ve bakımı önemli gider gerektirmektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Borçlu şeyi dilediği bedelle serbestçe satabilir; ihtar veya hâkim izni aranmaz',
            'B': 'Alacaklı temerrüdünde satış imkânı yalnız bozulabilir nitelikteki şeyler için tanınmıştır',
            'C': 'Borçlu, tevdi edilemeyen şeyi imha ederek borcundan kurtulur; imha giderleri alacaklı temerrüde düştüğü için ona yüklenir',
            'D': 'Tevdi mümkün olmadığından borç kendiliğinden sona erer ve borçlunun başka bir külfeti kalmaz',
            'E': 'Borçlu, alacaklıya önceden ihtarda bulunmak koşuluyla hâkimden izin alarak şeyi açık artırmayla sattırabilir ve bedelini tevdi edebilir',
        },
        'E',
        '**TBK m. 108:** tevdi edilmeye elverişli olmayan, bozulabilen veya bakımı/korunması önemli gider gerektiren şeylerde borçlu, **alacaklıya önceden ihtarda bulunarak** hâkimin izniyle şeyi sattırıp **bedelini tevdi edebilir**.',
    ),
    # düzey 2
    '0044': patch(
        'Borcun ifası ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Aksine anlaşma yoksa para borçları, alacaklının ödeme zamanındaki yerleşim yerinde ifa edilir.\n\nII. İfa zamanı kararlaştırılmamışsa borç, doğumu anında muaccel olur.\n\nIII. Borcun bizzat borçlu tarafından ifasında alacaklının menfaati bulunmasa dahi borçlu, borcunu şahsen ifa etmekle yükümlüdür.',
        {
            'A': 'Yalnız II',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'C',
        '**I doğru:** m. 89/1-1. **II doğru:** m. 90. **III yanlış:** m. 83 tam tersini söyler — alacaklının menfaati **bulunmadıkça** borçlu şahsen ifa etmekle yükümlü değildir.',
    ),
    # düzey 2
    '0045': patch(
        'Borcu sona erdiren hâller ile ilgili aşağıdaki ifadelerden hangisi **yanlıştır**?',
        {
            'A': 'Alacaklı ve borçlu sıfatlarının aynı kişide birleşmesi borcu sona erdirir',
            'B': 'İbra, tarafların şekle bağlı olmaksızın yapacakları bir sözleşmeyle borcu ortadan kaldırır',
            'C': 'Borcun ifasının borçlunun sorumlu tutulamayacağı sebeplerle imkânsızlaşması borcu sona erdirir',
            'D': 'Zamanaşımı süresinin dolması, ifa ve ibra gibi borcu sona erdiren hâllerden biridir',
            'E': 'Yenileme, ancak tarafların mevcut borcu sona erdirme yönündeki açık iradesiyle gerçekleşir',
        },
        'D',
        "Zamanaşımı borcu **sona erdirmez**; alacağı dava edilemez (eksik) borç hâline getirir ve **m. 78/2** uyarınca ödenen tutar geri istenemez. Diğer şıklar m. 132, m. 133, m. 135 ve m. 136'ya uygundur.",
    ),
    # düzey 3
    '0046': patch(
        "Bir borçlunun alacaklıya 120.000 ₺ tutarında, ifa günü 10 Mayıs olarak birlikte kararlaştırılmış bir para borcu vardır. Borçlu bu tarihte ödeme yapmamış; alacaklı 10 Haziran'da dava açmıştır. Sözleşmede temerrüt faizi oranı kararlaştırılmamıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': 'Temerrüt faizi işlemeye başlamak için ayrıca borçlunun kusurunun ispatlanması gerekir',
            'B': "Borçlu 10 Mayıs'ın geçmesiyle ihtarsız temerrüde düşmüştür ve temerrüt faizi bu tarihten itibaren mevzuattaki orana göre işler",
            'C': 'Oran kararlaştırılmadığından temerrüt faizi hiç işlemez; alacaklı yalnız anaparayı isteyebilir',
            'D': "Temerrüt faizi, alacaklının alacağını yargı önüne taşıdığı 10 Haziran'dan itibaren işlemeye başlar; vade günü yalnız muacceliyeti sağlar",
            'E': 'Alacaklı ihtar çekmediğinden temerrüt doğmamıştır; faiz talebi reddedilir',
        },
        'B',
        "İfa günü birlikte belirlendiğinden **m. 117/2** uyarınca ihtarsız temerrüt 10 Mayıs'ta doğar. Oran kararlaştırılmadığı için **m. 120/1** uyarınca faiz, borcun doğduğu tarihte yürürlükteki mevzuata göre belirlenir. Temerrüt kusura bağlı değildir.",
    ),
    # düzey 2
    '0047': patch(
        'Bir borçlu, alacaklısına olan 80.000 ₺ tutarındaki borcunu ödemiş ve borcun tamamının ödendiğine ilişkin makbuz almıştır. Ancak alacaklı, borç senedini geri vermemiş ve senedi üçüncü bir kişiye devretmiştir. Buna göre aşağıdaki ifadelerden hangisi **yanlıştır**?',
        {
            'A': 'Borçlu, ödemeyi makbuzla ispat ederek talep edilen borca karşı savunmada bulunabilir',
            'B': "Asıl borç ifayla sona erdiğinden rehin ve kefalet gibi fer'i haklar da sona ermiştir",
            'C': 'Borcun tamamı ödendiğinden borçlu, senedin geri verilmesini veya iptalini isteyebilirdi',
            'D': 'Alacaklının senedi geri vermemesi, borçlunun ifa ile borcundan kurtulduğu gerçeğini değiştirmez',
            'E': 'Borçlu borcu ödemiş olsa da senedin geri verilmesini isteyemez; makbuz alması hukuken yeterli sayılır',
        },
        'E',
        "**TBK m. 103:** borcun tamamı ödenmişse borçlu **makbuzun yanı sıra borç senedinin geri verilmesini veya iptalini** isteyebilir. Bu hakkı reddeden şık yanlıştır. Fer'i hakların sona ermesi m. 131'e uygundur.",
    ),
    # düzey 3
    '0048': patch(
        'Dönemsel edimlerde zamanaşımı ile ilgili aşağıdaki ifadelerden hangileri yanlıştır?\n\nI. Kira bedelleri on yıllık genel zamanaşımına tabidir.\n\nII. Anapara faizleri beş yıllık zamanaşımına tabidir.\n\nIII. Ücret alacakları için özel bir zamanaşımı süresi öngörülmemiştir.',
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'I ve III',
            'D': 'Yalnız II',
            'E': 'I, II ve III',
        },
        'C',
        '**I yanlış:** m. 147/1 uyarınca **kira bedelleri beş yıllık** süreye tabidir. **II doğru:** anapara faizleri m. 147/1 kapsamındadır. **III yanlış:** **ücret** de aynı fıkrada sayılan dönemsel edimlerdendir.',
    ),
    # düzey 3
    '0049': patch(
        "Bir borçlu, muaccel borcunun bir kısmını ödemiş ve ödeme sırasında borcu açıkça ikrar etmiştir. Bu işlemden dört yıl sonra alacaklı, kalan alacak için dava açmış; borçlu zamanaşımı def'inde bulunmuştur. Alacak on yıllık zamanaşımına tabidir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': 'Kesilme hâlinde süre durur ve kesilme sebebi ortadan kalkınca kaldığı yerden devam eder',
            'B': "Kısmi ifa zamanaşımını kesmez; süre ilk muacceliyet tarihinden itibaren kesintisiz işlediğinden borçlunun def'i yerindedir",
            'C': "Borç ikrarı zamanaşımından peşin feragat sayılacağından def'i tümüyle ortadan kalkmıştır",
            'D': 'Kısmi ifa ve borç ikrarı zamanaşımını kestiğinden süre o tarihten itibaren yeniden işlemeye başlamıştır ve alacak zamanaşımına uğramamıştır',
            'E': 'Zamanaşımını yalnız dava açılması keser; borçlunun işlemlerinin bir etkisi yoktur',
        },
        'D',
        '**TBK m. 154/1-1:** borçlunun borcu ikrar etmesi, özellikle **kısmen ifada bulunması** zamanaşımını keser. Kesilme hâlinde süre **yeniden işlemeye başlar** (durma değil kesilme). Borç ikrarı m. 160 anlamında peşin feragat değildir.',
    ),
    # düzey 2
    '0050': patch(
        'Borçlu temerrüdünün sonuçları ile ilgili aşağıdaki ifadelerden hangisi **yanlıştır**?',
        {
            'A': 'Temerrüde düşen borçlu, beklenmedik hâlden doğan zarardan sorumlu tutulamaz ve bu zarara alacaklı katlanır',
            'B': 'Karşılıklı borç yükleyen sözleşmelerde alacaklı uygun bir süre verip sonucunda seçimlik haklarını kullanabilir',
            'C': 'Sürekli edimli sözleşmelerde alacaklı, sözleşmeyi feshederek erken sona ermeden doğan zararını isteyebilir',
            'D': 'Para borçlarında alacaklı, ayrıca zarara uğradığını ispat etmeksizin temerrüt faizi isteyebilir',
            'E': 'Temerrüde düşen borçlu, kusursuzluğunu ispat etmedikçe gecikme zararını gidermekle yükümlüdür',
        },
        'A',
        "**TBK m. 119:** temerrüde düşen borçlu **beklenmedik hâlden doğan zarardan da sorumludur**; ancak temerrüde düşmekte kusursuz olduğunu veya edimi zamanında ifa etseydi de zararın doğacağını ispat ederse kurtulur. 'Hiçbir koşulda sorumlu tutulamaz' ifadesi bu nedenle yanlıştır.",
    ),
    # düzey 3
    '0051': patch(
        "Borcun sona ermesine ilişkin aşağıdaki ifadelerden hangileri yanlıştır?\n\nI. Alacaklının rızasıyla asıl edim yerine başka bir edimin ifası borcu sona erdirir.\n\nII. Yenileme, tarafların açık iradesi olmaksızın kambiyo senedi verilmesiyle de gerçekleşir.\n\nIII. Asıl borç sona erdiğinde kefalet ve rehin gibi fer'i haklar da sona erer.",
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'Yalnız II',
            'D': 'Yalnız III',
            'E': 'Yalnız I',
        },
        'C',
        '**II yanlış:** m. 133/2 uyarınca mevcut borç için kambiyo taahhüdünde bulunulması, **açık yenileme iradesi olmadıkça yenileme sayılmaz**. **I doğru** (alacaklının rızasıyla başka edimin ifası borcu sona erdirir), **III doğru** (m. 131/1).',
    ),
    # düzey 2
    '0052': patch(
        'İfa yeri ve ifa zamanı ile ilgili aşağıdaki ifadelerden hangisi **yanlıştır**?',
        {
            'A': 'İfa zamanı kararlaştırılmamış ve ilişkinin özelliğinden de anlaşılmıyorsa borç doğumu anında muaccel olur',
            'B': 'Aksine anlaşma yoksa para borçları alacaklının ödeme zamanındaki yerleşim yerinde ifa edilir',
            'C': 'Parça borçları, aksine anlaşma yoksa sözleşmenin kurulduğu sırada şeyin bulunduğu yerde ifa edilir',
            'D': 'İfa yeri öncelikle tarafların açık veya örtülü iradelerine göre belirlenir',
            'E': 'İfa yeri kararlaştırılmamışsa para borçları borçlunun yerleşim yerinde ifa edilir ve alacaklının taşınması bu sonucu değiştirmez',
        },
        'E',
        '**TBK m. 89/1-1:** para borçları **alacaklının ödeme zamanındaki yerleşim yerinde** ifa edilir. Borçlunun yerleşim yerini esas alan ve alacaklının taşınmasını etkisiz sayan şık bu hükme aykırıdır.',
    ),
    # düzey 2
    '0053': patch(
        'Takas ile ilgili aşağıdaki ifadelerden hangisi **yanlıştır**?',
        {
            'A': 'Takasın gerçekleşmesi için tarafların bu yönde bir takas sözleşmesi yapmaları zorunludur',
            'B': 'Takas için karşılıklı olarak bir miktar para veya özdeş diğer edimlerin borçlanılmış olması gerekir',
            'C': 'Takasın ileri sürülebilmesi için her iki borcun da muaccel olması gerekir',
            'D': 'Takas beyanı üzerine borçlar, takas edilebilecekleri anda daha az olan borç tutarınca sona erer',
            'E': 'Alacaklardan biri çekişmeli olsa bile takas ileri sürülebilir',
        },
        'A',
        "**TBK m. 143/1:** takas **borçlunun takas iradesini alacaklıya bildirmesiyle** gerçekleşir; tek taraflı bir irade açıklamasıdır, sözleşme aranmaz. Diğer şıklar m. 139/1, m. 139/2 ve m. 143/1'e uygundur.",
    ),
    # düzey 3
    '0054': patch(
        'Alacaklı temerrüdü ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Gereği gibi önerilen edimi haklı sebep olmaksızın kabulden kaçınan alacaklı temerrüde düşer.\n\nII. Alacaklı temerrüde düştüğünde borçlu, hasar ve giderleri alacaklıya ait olmak üzere teslim edeceği şeyi tevdi ederek borcundan kurtulabilir.\n\nIII. Alacaklının temerrüde düşmesi, borcu kendiliğinden sona erdirir.',
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'Yalnız III',
            'E': 'I, II ve III',
        },
        'C',
        '**I doğru:** m. 106. **II doğru:** m. 107. **III yanlış:** alacaklı temerrüdü borcu kendiliğinden sona erdirmez; borçlu ancak **tevdi** (m. 107) veya elverişsiz şeylerde **satış ve bedelin tevdii** (m. 108) yoluyla borcundan kurtulur.',
    ),
    # düzey 3
    '0055': patch(
        'Bir borçlunun alacaklıya hem 60.000 ₺ tutarında muaccel bir para borcu hem de aynı alacaklıdan 60.000 ₺ tutarında muaccel bir para alacağı vardır. Borçlu takas beyanında bulunmadan önce alacaklı, kendi alacağı için icra takibi başlatmıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Takas ancak icra dairesinin izniyle ileri sürülebilir',
            'B': 'İcra takibi başlatıldıktan sonra takas ileri sürülemez; borçlunun tek yolu takip konusu borcu ödeyip kendi alacağı için ayrı takip başlatmaktır',
            'C': 'Borçlar eşit olduğundan takas kendiliğinden gerçekleşmiş sayılır ve beyana gerek kalmaz',
            'D': 'Borçlu takas iradesini bildirerek borcunu sona erdirebilir; takas edilebilir oldukları anda her iki borç da tamamen sona ermiş sayılır',
            'E': 'Takas beyanı yalnız ileriye etkili sonuç doğuracağından takip tarihine kadar işleyen faiz aynen istenir',
        },
        'D',
        '**TBK m. 143/1:** takas beyanla gerçekleşir (kendiliğinden değil) ve borçlar **takas edilebilecekleri anda** daha az olan tutarınca sona erer. Tutarlar eşit olduğundan her iki borç da tamamen sona erer; etki geçmişe yürüdüğü için o andan sonrası için temerrüt faizi işlemez.',
    ),
    # düzey 2
    '0056': patch(
        "Borcun ifası ve sona ermesi ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Asıl borç sona erdiğinde rehin, kefalet, faiz ve ceza koşulu gibi fer'i hak ve borçlar da sona erer.\n\nII. Zamanaşımından önceden feragat edilemez.\n\nIII. Zamanaşımı ileri sürülmese bile hâkim bunu kendiliğinden göz önüne alır.",
        {
            'A': 'I, II ve III',
            'B': 'I ve II',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'Yalnız II',
        },
        'B',
        "**I doğru:** m. 131/1. **II doğru:** m. 160. **III yanlış:** m. 161 uyarınca zamanaşımı **ileri sürülmedikçe hâkim kendiliğinden göz önüne alamaz**; zamanaşımı bir def'idir.",
    ),
    # düzey 3
    '0057': patch(
        'Bir borçlu, faiz ödemelerinde gecikmiş durumdayken alacaklıya kısmi bir ödeme yapmış ve bu ödemenin anaparadan düşülmesini talep etmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Borçlu kısmi ödemeyi anaparadan düşme hakkına sahiptir; faizdeki gecikme yalnız temerrüt faizi doğurur, mahsup sırasını değiştirmez',
            'B': 'Mahsubun sırası yalnız alacaklının makbuzda göstereceği şekilde belirlenir; kanunda kural yoktur',
            'C': 'Faizde gecikme hâlinde alacaklı kısmi ödemeyi reddedebilir; kabul ederse ödeme öncelikle işlemiş faize sayılır',
            'D': 'Anaparaya mahsup hakkı sözleşmeyle borçlu lehine genişletilemez, ancak gecikme hâlinde de aynen uygulanır',
            'E': 'Borçlu faiz ödemede gecikmiş olduğundan kısmi ödemeyi anaparadan düşme hakkını kullanamaz',
        },
        'E',
        '**TBK m. 100/1:** borçlu **faiz veya giderleri ödemede gecikmemiş ise** kısmi ödemeyi ana borçtan düşme hakkına sahiptir. Olayda gecikme bulunduğundan bu hak kullanılamaz; hükmün şartı gerçekleşmemiştir.',
    ),
    # düzey 2
    '0058': patch(
        'Alacağın devri ve ifa ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Devir kendisine usulüne uygun bildirilmiş olsa dahi borçlu, önceki alacaklıya yaptığı ödemeyle borcundan kurtulur',
            'B': 'Alacak birkaç kez devredilmişse borçlu, önceki devralanlardan birine iyiniyetle ifayla borcundan kurtulabilir',
            'C': 'Devir kendisine bildirilmemişse borçlu, önceki alacaklıya iyiniyetle ifada bulunarak borcundan kurtulur',
            'D': 'Devrin borçluya bildirilmesi külfeti devreden veya devralana aittir',
            'E': 'Devir bildirildikten sonra borçlunun önceki alacaklıya yaptığı ödeme borcu sona erdirmez',
        },
        'A',
        '**TBK m. 186:** borçlunun önceki alacaklıya ifayla kurtulması, devrin **bildirilmemiş olması ve iyiniyet** şartına bağlıdır. Bildirimden sonra iyiniyet kalmayacağından ödeme borcu sona erdirmez.',
    ),
    # düzey 2
    '0059': patch(
        'İbra ve yenileme ile ilgili aşağıdaki ifadelerden hangisi **yanlıştır**?',
        {
            'A': 'Mevcut borç için kambiyo taahhüdünde bulunulması tek başına yenileme sayılmaz',
            'B': 'İbra sözleşmesiyle borç tamamen veya kısmen ortadan kaldırılabilir',
            'C': 'Mevcut bir borç için yeni bir alacak senedi düzenlenmesi, tarafların ayrıca açık bir iradesi aranmaksızın yenileme sayılır',
            'D': 'Yenileme, ancak tarafların mevcut borcu sona erdirme yönündeki açık iradesiyle gerçekleşir',
            'E': 'İbra, borcu doğuran işlem şekle bağlıysa aynı şekle uyularak yapılmalıdır; adi yazılı ibra bu hâlde borcu ortadan kaldırmaz',
        },
        'C',
        '**TBK m. 133/2:** mevcut borç için **kambiyo taahhüdünde bulunulması veya yeni bir alacak ya da kefalet senedi düzenlenmesi**, tarafların açık yenileme iradeleri olmadıkça **yenileme sayılmaz**. Yanlış olan şık bu hükmün tersini söylemektedir.',
    ),
    # düzey 3
    '0060': patch(
        'Bir borçlunun ferden belirlenmiş bir makineyi teslim borcu, borçlunun kusuruyla imkânsız hâle gelmiştir. Alacaklı bedeli peşin ödemiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Borçlu yalnız aldığı bedeli iade eder; bunun dışında bir tazminat yükümlülüğü doğmaz',
            'B': 'Alacaklı yalnız sözleşmeden dönebilir; tazminat isteme hakkı bulunmaz',
            'C': 'Kusurlu imkânsızlıkta sorumluluk için alacaklının borçlunun kusurunu ispat etmesi gerekir',
            'D': 'Borçlu kusurlu olduğundan aynen ifa yerine tazminat sorumluluğu doğar; kusursuzluğunu ispat edemediği için alacaklının zararını gidermekle yükümlüdür',
            'E': 'İmkânsızlık borcu her durumda sona erdirdiğinden borçlunun sorumluluğu kalmaz; alacaklı yalnız ödediği bedeli sebepsiz zenginleşme yoluyla geri alabilir',
        },
        'D',
        'Kusursuz imkânsızlık **m. 136** uyarınca borcu sona erdirir. Olayda imkânsızlık **borçlunun kusuruyla** doğduğundan bu hüküm uygulanmaz; **m. 112** işler ve borçlu kusursuzluğunu ispat edemediği için alacaklının zararını giderir. İspat külfeti borçludadır.',
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
    print(f"1 paket / {len(PATCHES)} soru ('Borcun Ifasi ve Sona Ermesi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
