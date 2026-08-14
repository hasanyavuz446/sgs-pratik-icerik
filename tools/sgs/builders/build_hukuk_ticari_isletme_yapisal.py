#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ticari Isletme ve Tacir — YAPISAL kalibrasyon.

Hukuk ailesi yapisal kalibrasyon turunun 10. konusu. Paketin 60 sorusunun
TAMAMI yeniden yazildi.

    olcut                gercek   once   sonra
    medyan kok              257    112     172
    olumsuz kok           %41,5     %8     %37
    onculu                %14,3     %8       —
    kor ogrenci            <=%30    %30       —
    boy egilimi               —   29/7       —

⚠️ SAHIPLIK DEVRI: fix_ticaret_length_quality bu pakette 4 soru tutuyordu ve
`--check` DESTEKLEMIYOR (argumani yok sayip YAZAR — fix_meslek_length_quality
ile ayni tuzak sinifi; 2026-08-14'te meslek_orgutu_disiplin'de hasar vermisti).
Bloklari CIKARILDI ve builder'a argv korumasi eklendi.

IKI KAPI: §5 boy (ilk tasarim 33/60 = %55 cikip uretimi DURDURDU; uc turda 55
celdirici dogru sikla PARALEL yapiya tasinarak %30) · §1 bilissel duzey
(0 = 5 <=6, 0+1 = 12 <=24, duzey 2 = 30 >=24, duzey 3 = 18 >=12).

Ayrica 12 kisa tarama koku olay cercevesine tasindi (medyan 136 -> 172).

Dayanak: TTK md. 1, 2, 3, 4, 5, 7, 8, 11, 12, 13, 15, 16, 18, 20, 21, 35, 36,
39, 40, 48, 52, 53, 64, 82, 89, 90 · TBK md. 547 vd. · ticari islemlerde tasinir
rehni mevzuati.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/ticaret_hukuku/ticari_isletme_tacir.json"
STYLE_REF = "SGS Ticaret Hukuku (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "tic-isletme-gen-"


def patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": "6102 sayili Turk Ticaret Kanunu"},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        'Bir kişi, sermayesinden çok bedeni çalışmasına dayanan ve geliri kanunda öngörülen sınırı aşmayan bir terzilik faaliyeti yürütmektedir. Bir diğeri ise aynı sınırı aşan düzeyde gelir hedefleyen, devamlı ve bağımsız bir konfeksiyon işletmesi işletmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ayrım yalnızca ticaret siciline kayıt olup olmamaya göre yapılır',
            'B': 'Birincisi esnaf, ikincisi ticari işletme işleten tacirdir',
            'C': 'Her ikisi de esnaftır',
            'D': 'Her ikisi de tacirdir',
            'E': 'Birincisi tacir, ikincisi esnaftır',
        },
        'B',
        'TTK md. 11: ticari işletme, esnaf işletmesi için öngörülen sınırı aşan düzeyde gelir sağlamayı hedef tutan faaliyetlerin devamlı ve bağımsız şekilde yürütüldüğü işletmedir. md. 15: ekonomik faaliyeti sermayesinden fazla BEDENİ ÇALIŞMASINA dayanan ve geliri sınırı aşmayan kişi ESNAFTIR. Ayrım sicile kayda değil, faaliyetin niteliğine dayanır.',
    ),
    # düzey 2
    '0002': patch(
        'Bir kişi, ticari işletmesini kurup açtığını gazete ilanıyla duyurmuş ve ticaret siciline kaydettirmiş; ancak henüz fiilen faaliyete başlamamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kişi, işletmeyi fiilen işletmese de tacir sayılır',
            'B': 'Kişi, işletmeyi fiilen işletmeye başlasa dahi tacir sayılmaz',
            'C': 'Tacir sıfatı yalnızca ticaret siciline kayıtla doğar; ilan sonuç doğurmaz',
            'D': 'Kişi ancak fiilen faaliyete başladığında tacir sayılır',
            'E': 'Tacir sıfatı için ilk faturanın düzenlenmesi gerekir',
        },
        'A',
        'TTK md. 12/2: bir ticari işletmeyi kurup açtığını, sirküler, gazete, radyo, televizyon ve diğer ilan araçlarıyla halka bildirmiş veya işletmesini ticaret siciline tescil ettirerek durumu ilan etmiş olan kimse, fiilen işletmeye başlamamış olsa bile TACİR SAYILIR.',
    ),
    # düzey 3
    '0003': patch(
        'Bir ticari işletme, on beş yaşındaki bir çocuğa miras yoluyla geçmiş ve işletme vasi tarafından çocuk adına işletilmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ne küçük ne vasi tacir sayılır; işletme tacirsiz işletilir',
            'B': 'Küçük tacir sayılmaz; tacir sıfatı vasiye aittir',
            'C': 'Küçük tacir sayılır; ancak ceza ve disiplin sorumluluğu işletmeyi yöneten kanuni temsilciye aittir',
            'D': 'Küçük ancak ergin olduğunda tacir sıfatını kazanır',
            'E': 'Küçük tacir sayılır ve işletmeden doğan ceza ile disiplin sorumluluğu da bizzat kendisine aittir',
        },
        'C',
        'TTK md. 13: küçük ve kısıtlılara ait ticari işletmeyi bunların adına işleten yasal temsilci, ticari işletmenin sahibi olmadığı hâlde tacir sayılmaz; TACİR SIFATI temsil edilene aittir. Ancak ceza ve disiplin sorumlulukları bakımından yasal temsilci sorumlu olur.',
    ),
    # düzey 3
    '0004': patch(
        'Bir belediye kendi tüzel kişiliği altında bir ticari işletme işletmektedir. Ayrıca bir ticaret şirketi ve amacına ulaşmak için ticari işletme işleten bir dernek bulunmaktadır. Buna göre tacir sıfatı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Üçü de tacirdir',
            'B': 'Üçü de tacir sayılmaz',
            'C': 'Belediye tacirdir; ticaret şirketi ve dernek tacir sayılmaz',
            'D': 'Ticaret şirketi ve dernek tacirdir; belediye tacir sayılmaz ancak işlettiği işletmeye ticari hükümler uygulanır',
            'E': 'Yalnızca ticaret şirketleri tacirdir; amacına varmak için ticari işletme işleten dernek ile belediyeler tacir sayılmaz',
        },
        'D',
        'TTK md. 16: ticaret şirketleri ile amacına varmak için ticari bir işletme işleten dernekler ve kendi kuruluş kanunları gereğince özel hukuk hükümleri dairesinde yönetilmek üzere kurulan kamu tüzel kişileri tacir sayılır. md. 16/2: DEVLET, il özel idaresi, BELEDİYE, köy ve diğer kamu tüzel kişileri ile kamuya yararlı dernekler TACİR SAYILMAZ; ancak işlettikleri ticari işletmelere ticari hükümler uygulanır.',
    ),
    # düzey 2
    '0005': patch(
        'Bir tacir, ticari işletmesini bir bütün hâlinde devretmek istemektedir. Devir sözleşmesinin kapsamı ve şekli tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Devir ticaret siciline tescil ve ilan edilir',
            'B': 'Ticari işletme bir bütün hâlinde devredilebilir',
            'C': 'Aksi öngörülmemişse devir; duran malvarlığını, işletme değerini ve kiracılık hakkını içerir',
            'D': 'Devir sözleşmesi yazılı yapılır',
            'E': 'Ticari işletme ancak unsurları tek tek devredilerek elden çıkarılabilir',
        },
        'E',
        'TTK md. 11/3: ticari işletme, içerdiği malvarlığı unsurlarının devri için zorunlu tasarruf işlemlerinin ayrı ayrı yapılmasına gerek olmaksızın BİR BÜTÜN hâlinde devredilebilir ve diğer hukuki işlemlere konu olabilir. Aksi öngörülmemişse devir sözleşmesi duran malvarlığını, işletme değerini, kiracılık hakkını, ticaret unvanı ile diğer fikri mülkiyet haklarını içerir. Devir yazılı yapılır, ticaret siciline tescil ve ilan edilir.',
    ),
    # düzey 3
    '0006': patch(
        'Bir tacir; iflasa tabi olmadığını, ticari defter tutma yükümlülüğü bulunmadığını ve ticaret unvanı seçmek zorunda olmadığını ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Üç iddia da yanlıştır; tacir iflasa tabidir, defter tutar ve ticaret unvanı seçip kullanır',
            'B': 'Yalnızca defter tutma yükümlülüğünün bulunmaması doğrudur',
            'C': 'Yalnızca iflasa tabi olmama iddiası doğrudur',
            'D': 'Üç iddia da doğrudur; sayılan yükümlülükler yalnızca tüzel kişi tacirler için geçerlidir',
            'E': 'Yalnızca ticaret unvanı seçme zorunluluğunun bulunmaması doğrudur',
        },
        'A',
        'TTK md. 18: tacir, her türlü borcu için İFLASA TABİDİR; ayrıca kanun hükümleri uyarınca bir TİCARET UNVANI seçmek, işletmesini ticaret siciline TESCİL ettirmek ve bu Kanun hükümlerince gerekli TİCARİ DEFTERLERİ tutmakla yükümlüdür. Yükümlülükler gerçek ve tüzel kişi tacirlerin tamamını kapsar.',
    ),
    # düzey 3
    '0007': patch(
        'Bir tacir, ticari işletmesiyle ilgili faaliyetlerinde ortalama bir kişinin göstereceği özeni yeterli saydığını ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Basiretli iş adamı gibi hareket etme ölçüsü yalnızca tüzel kişi tacirler için ağırlaştırılmış olup gerçek kişi tacirleri bağlamaz',
            'B': 'Tacir, ortalama bir kişinin özenini göstermekle yeterli sayılır',
            'C': 'Tacir için özel bir özen ölçüsü öngörülmemiştir',
            'D': 'Tacirin her türlü faaliyetinde basiretli bir iş adamı gibi hareket etmesi gerekir',
            'E': 'Özen ölçüsü sözleşmeyle serbestçe belirlenir',
        },
        'D',
        'TTK md. 18/2: her tacirin, ticaretine ait bütün faaliyetlerinde BASİRETLİ BİR İŞ ADAMI GİBİ hareket etmesi gerekir. Bu, ortalama bir kişiden beklenenden AĞIR bir özen ölçüsüdür ve tüm tacirleri bağlar; sözleşmeyle hafifletilemez.',
    ),
    # düzey 3
    '0008': patch(
        'Bir tacir, kendisine 3 Mart günü teslim edilen faturanın içeriğine 20 Mart günü itiraz etmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Faturaya itiraz için süre öngörülmemiştir',
            'B': 'Fatura sekiz gün içinde itiraz edilmediğinden içeriği kabul edilmiş sayılır',
            'C': 'İtiraz süresi on beş gün olup itiraz süresindedir',
            'D': 'Fatura içeriği ancak yazılı kabulle bağlayıcı olur',
            'E': 'Faturaya itiraz süresi bir ay olarak öngörüldüğünden yapılan itiraz süresinde sayılır',
        },
        'B',
        "TTK md. 21/2: bir faturayı alan kişi, aldığı tarihten itibaren SEKİZ GÜN içinde faturanın içeriği hakkında bir itirazda bulunmamışsa bu içeriği KABUL ETMİŞ SAYILIR. 3 Mart'ta alınan faturaya 20 Mart'ta yapılan itiraz süresinde değildir.",
    ),
    # düzey 3
    '0009': patch(
        'İki kişi, yalnızca biri için ticari nitelik taşıyan bir iş dolayısıyla birlikte borç altına girmiş; sözleşmede sorumluluk biçimi düzenlenmemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ticari işlerde müteselsil sorumluluk karinesi bulunmaz',
            'B': 'Müteselsil sorumluluk yalnızca her iki taraf için de ticari iş sayılan hâllerde doğar',
            'C': 'Sorumluluk biçimi mahkemece takdir edilir',
            'D': 'Borçlular eşit paylarla sorumlu olur',
            'E': 'Aksi kararlaştırılmadıkça borçlular müteselsilen sorumlu olur',
        },
        'E',
        'TTK md. 7: iki veya daha fazla kişi, içlerinden yalnız biri veya hepsi için ticari nitelikte bir iş dolayısıyla diğer bir kimseye karşı birlikte borç altına girerse, kanunda veya sözleşmede aksi öngörülmemişse MÜTESELSİLEN sorumlu olur. Karine ticari işlerde geçerlidir; işin her iki taraf için ticari olması şart değildir.',
    ),
    # düzey 2
    '0010': patch(
        'Bir tacir, ticari işletmesiyle ilgili bir ödünç sözleşmesinde faiz oranını serbestçe belirlemek istemektedir. Buna göre ticari işlerde faiz bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bileşik faiz yürütülmesi yalnızca kanunda sayılan sınırlı hâllerde mümkündür',
            'B': 'Temerrüt faizi ticari işlerde ayrıca düzenlenmiştir',
            'C': 'Ticari işlerde faiz oranı kanunla sabitlenmiş olup taraflarca değiştirilemez',
            'D': 'Ticari işlerde faiz oranı kural olarak serbestçe belirlenebilir',
            'E': 'Faiz oranı serbestçe belirlenmemişse kanuni faiz uygulanır',
        },
        'C',
        'TTK md. 8-9: ticari işlerde faiz oranı SERBESTÇE belirlenir; belirlenmemişse kanuni faiz uygulanır. md. 8/2: bileşik faiz (faize faiz yürütülmesi) yalnızca cari hesap sözleşmeleri ile her iki taraf için de ticari iş niteliğinde olan ödünç sözleşmelerinde ve kanunda öngörülen koşullarla mümkündür.',
    ),
    # düzey 3
    '0011': patch(
        "Bir tacirin ticari işletmesini ilgilendiren bir işlem ile TTK'da düzenlenen bir hususa ilişkin başka bir işlem söz konusudur. Buna göre ticari iş kavramı bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Ticari iş kavramı yalnızca tacirler arasındaki işlemleri kapsar',
            'B': 'Yalnızca ticari işletmeyi ilgilendiren işlemler ticari iştir',
            'C': "Yalnızca TTK'da düzenlenen hususlar ticari iştir",
            'D': 'Bir işlemin ticari iş sayılabilmesi için ayrıca ticaret siciline tescil edilmiş ve usulüne uygun biçimde ilan olunmuş olması gerekir',
            'E': "Her ikisi de ticari iştir; TTK'da düzenlenen hususlar ile bir ticari işletmeyi ilgilendiren işlem ve fiiller ticari iştir",
        },
        'E',
        'TTK md. 3: bu Kanunda düzenlenen hususlarla bir ticari işletmeyi ilgilendiren bütün işlem ve fiiller TİCARİ İŞTİR. Tanım iki ölçütü birlikte kapsar; tarafların ikisinin de tacir olması ya da işlemin tescili aranmaz.',
    ),
    # düzey 2
    '0012': patch(
        'Ticari nitelikteki bir uyuşmazlığın hangi mahkemede görüleceği tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ticari davalar sulh hukuk mahkemesinde görülür',
            'B': 'Ticari davalar kural olarak asliye ticaret mahkemesinde görülür',
            'C': 'Ticari davalar yalnızca tahkim yoluyla çözülür',
            'D': 'Ticari davalar için özel bir görevli mahkeme öngörülmemiştir',
            'E': 'Ticari davalar idare mahkemesinde görülür',
        },
        'B',
        'TTK md. 4-5: bu Kanunda öngörülen hususlardan doğan hukuk davaları ile sayılan diğer davalar TİCARİ DAVA sayılır ve aksine hüküm bulunmadıkça ASLİYE TİCARET MAHKEMESİNDE görülür. Asliye ticaret mahkemesi bulunmayan yerlerde bu davalara asliye hukuk mahkemesi bakar.',
    ),
    # düzey 2
    '0013': patch(
        'Bir tacir, ticari işletmesiyle ilgili işlemleri kendi ad ve soyadıyla yapmakta, ticaret unvanını kullanmamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tacir işletmesiyle ilgili işlemleri ticaret unvanıyla yapar ve unvanı işletmesinin görülebilecek bir yerine yazar',
            'B': 'Ticaret unvanı yalnızca tüzel kişi tacirler için zorunludur',
            'C': 'Ticaret unvanının işletmede görünür biçimde yazılması gerekmez',
            'D': 'Ticaret unvanı yalnızca ticaret siciline kayıt için kullanılır',
            'E': 'Tacir, işlemlerini dilerse ad ve soyadıyla yapabilir; ayrıca ticaret unvanı kullanma yükümlülüğü bulunmaz',
        },
        'A',
        'TTK md. 39: her tacir, ticari işletmesine ilişkin işlemleri TİCARET UNVANIYLA yapmak ve işletmesiyle ilgili senetlerle diğer belgeleri bu unvan altında imzalamak zorundadır. Tescil edilen ticaret unvanı, işletmenin görülebilecek bir yerine okunaklı biçimde YAZILIR. Yükümlülük gerçek ve tüzel kişi tacirlerin tamamını bağlar.',
    ),
    # düzey 2
    '0014': patch(
        'Ticaret sicilinin niteliği ve etkileri tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tescil ve ilan edilen hususlar, iyiniyetli olsun olmasın üçüncü kişilere karşı ileri sürülebilir',
            'B': 'Sicil kayıtlarının tutulmasından doğan zarardan sorumluluk düzenlenmiştir',
            'C': 'Tescili gerekirken tescil edilmemiş hususlar iyiniyetli üçüncü kişilere karşı ileri sürülemez',
            'D': 'Ticaret sicili yalnızca ilgili kişilere açık olup üçüncü kişiler kayıtları inceleyemez',
            'E': 'Ticaret sicili alenidir',
        },
        'D',
        'TTK md. 35 vd.: ticaret sicili ALENİDİR; herkes sicilin içeriğini ve belgeleri inceleyebilir, onaylı suret isteyebilir. md. 36: tescil ve ilan edilen hususlar üçüncü kişilere karşı ileri sürülebilirken, tescili gerekirken tescil edilmemiş hususlar iyiniyetli üçüncü kişilere karşı ileri sürülemez.',
    ),
    # düzey 3
    '0015': patch(
        'Bir tacir, ticari defterlerini tutmakta ancak açılış ve kapanış onaylarını yaptırmamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Elektronik ortamda tutulan defterler için hiçbir onay aranmaz',
            'B': 'Yalnızca kapanış onayı zorunlu olup açılış onayı aranmaz',
            'C': 'Ticari defterlerin kanunda öngörülen onaylara tabi olması zorunludur; onaysız defter usulüne uygun sayılmaz',
            'D': 'Defterlerin açılış ve kapanış onayı yükümlülüğü yalnızca tüzel kişi tacirler için öngörülmüş olup gerçek kişileri bağlamaz',
            'E': 'Defterlerin onaylanması tacirin tercihine bırakılmıştır',
        },
        'C',
        'TTK md. 64: fiziki ortamda tutulan yevmiye defteri, defterikebir ve envanter defteri ile ilgili diğer defterlerin AÇILIŞ onayları kuruluş sırasında ve her faaliyet dönemi başında, KAPANIŞ onayları ise kanunda belirtilen sürelerde yapılır. Onaylar zorunludur ve tüm tacirleri bağlar.',
    ),
    # düzey 2
    '0016': patch(
        'Bir anonim şirketin tutmakla yükümlü olduğu defterler belirlenmektedir. Buna göre aşağıdakilerden hangisi bu defterlerden biri değildir?',
        {
            'A': 'Personel özlük defteri',
            'B': 'Pay defteri, yönetim kurulu karar defteri ve genel kurul toplantı ve müzakere defteri',
            'C': 'Yevmiye defteri',
            'D': 'Defterikebir',
            'E': 'Envanter defteri',
        },
        'A',
        'TTK md. 64: her tacir yevmiye defteri, defterikebir ve envanter defterini tutar. Anonim şirketler ayrıca PAY DEFTERİ, YÖNETİM KURULU KARAR DEFTERİ ile GENEL KURUL TOPLANTI VE MÜZAKERE DEFTERİNİ tutar. Personel özlük dosyası iş mevzuatına ilişkindir; ticari defter değildir.',
    ),
    # düzey 2
    '0017': patch(
        'Bir tacir, ticari işletmesiyle ilgili olarak başka bir tacire verdiği hizmet için ücret kararlaştırılmadığını, bu nedenle ücret isteyemeyeceğini düşünmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ücret ancak yazılı sözleşme varsa istenebilir',
            'B': 'Ücret kararlaştırılmamışsa tacir hiçbir talepte bulunamaz',
            'C': 'Tacir, ticari işletmesiyle ilgili verdiği hizmet ve yaptığı giderler için uygun bir ücret ve faiz isteyebilir',
            'D': 'Ücret isteme hakkı yalnızca tüzel kişi tacirlere tanınmıştır',
            'E': 'Tacir yalnızca yaptığı giderleri ve verdiği avansları isteyebilir; gördüğü iş veya hizmet için ayrıca ücret talep edemez',
        },
        'C',
        'TTK md. 20: tacir olan veya olmayan bir kişiye, ticari işletmesiyle ilgili bir iş veya hizmet görmüş olan tacir, uygun bir ÜCRET isteyebilir; ayrıca verdiği avanslar ve yaptığı giderler için ödeme tarihinden itibaren FAİZ isteyebilir.',
    ),
    # düzey 3
    '0018': patch(
        'İki tacir arasında telefonla bir sözleşme kurulmuş; taraflardan biri sözleşmenin özetini içeren bir teyit mektubu göndermiştir. Karşı taraf mektubu aldıktan 12 gün sonra itiraz etmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Teyit mektubuna itiraz için süre öngörülmemiştir',
            'B': 'Sekiz gün içinde itiraz edilmediğinden teyit mektubu içeriği kabul edilmiş sayılır',
            'C': 'Faturaya itiraz süresi bir ay olarak öngörüldüğünden yapılan itiraz süresinde sayılır',
            'D': 'Teyit mektubu hiçbir hukuki sonuç doğurmaz',
            'E': 'Teyit mektubu ancak karşı tarafça imzalanırsa bağlayıcı olur',
        },
        'B',
        'TTK md. 21/3: telefonla, telgrafla, herhangi bir iletişim veya bilişim aracıyla ya da diğer bir teknik araçla veya sözlü olarak kurulan sözleşmelerle yapılan açıklamaların içeriğini doğrulayan bir yazıyı alan kişi, aldığı tarihten itibaren SEKİZ GÜN içinde itirazda bulunmamışsa, söz konusu teyit mektubunun içeriğini kabul etmiş sayılır.',
    ),
    # düzey 3
    '0019': patch(
        "Bir uyuşmazlıkta uygulanacak hükümler tartışılmaktadır: TTK'da özel bir hüküm yoktur, ancak ticari örf ve âdet ile genel hükümler gündeme gelmiştir. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Uyuşmazlık hakkında karar verilemez',
            'B': 'Hâkim, uygulanacak kuralı serbestçe seçer',
            'C': 'Yalnızca ticari örf ve âdet uygulanır; bulunmadığı hâllerde dahi genel hükümlere gidilemez',
            'D': 'Doğrudan genel hükümlere gidilir; ticari örf ve âdet uygulanmaz',
            'E': 'Ticari hükümlerle düzenlenmemiş konularda ticari örf ve âdete, o da yoksa genel hükümlere başvurulur',
        },
        'E',
        'TTK md. 1 ve 2: ticari hükümlerle düzenlenmemiş konularda TİCARİ ÖRF VE ÂDETE, bu da yoksa genel hükümlere göre karar verilir. Ticari örf ve âdet, ancak tacirler arasında ya da bir bölgede yerleşmişse uygulanır; bunu bilmeyenlere karşı da uygulanabilmesi için tacir olmaları gerekir.',
    ),
    # düzey 2
    '0020': patch(
        'Bir tacir, ticari işletmesini teslim etmeksizin teminat olarak göstermek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ticari işletme rehni, işletmenin zilyetliği devredilmeksizin sicile tescille kurulabilir',
            'B': 'Ticari işletme rehni yalnızca taşınmazlar için mümkündür',
            'C': 'Ticari işletme, ancak zilyetliği alacaklıya devredilmek suretiyle rehnedilebilir',
            'D': 'Ticari işletme rehni yalnızca noterde düzenlenirse geçerlidir',
            'E': 'Ticari işletme, bir bütün olarak rehne konu edilemez',
        },
        'A',
        'Ticari işlemlerde taşınır rehni mevzuatı: ticari işletme, zilyetliğin devredilmesine gerek olmaksızın rehin sicilinde TESCİL edilmek suretiyle rehnedilebilir. Bu, işletmenin faaliyetini sürdürerek kredi temin etmesine imkân verir.',
    ),
    # düzey 3
    '0021': patch(
        'Bir uyuşmazlıkta tacirin ticari defterlerinin delil olarak kullanılması gündeme gelmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ticari defterler kesin delil sayılır ve mahkemeyi bağlar',
            'B': 'Ticari defterler yalnızca sahibi aleyhine delil olabilir',
            'C': 'Ticari defterlerin delil değeri yalnızca tacir olmayanlar için doğar',
            'D': 'Ticari defterler, usulüne uygun biçimde tutulmuş olsa dahi hiçbir uyuşmazlıkta delil olarak dikkate alınamaz',
            'E': 'Ticari defterler, kanunda öngörülen koşullar gerçekleştiğinde sahibi lehine de delil olabilir; mahkeme takdir eder',
        },
        'E',
        'Ticari defterlerin ispat gücü, usul hukuku ve TTK hükümleri çerçevesinde belirlenir: usulüne uygun tutulan defterler sahibi ALEYHİNE delil olabileceği gibi, kanunda öngörülen koşullar gerçekleştiğinde LEHİNE de delil oluşturabilir. Defterler kesin delil değildir; mahkemenin değerlendirmesine tabidir.',
    ),
    # düzey 2
    '0022': patch(
        'Bir tacir, ticari defterlerini ve belgelerini bir yıl sonra imha etmeyi planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Saklama süresi yalnızca vergi mevzuatında düzenlenmiştir',
            'B': 'Defter ve belgeleri saklama yükümlülüğü yalnızca tüzel kişi tacirler için öngörülmüştür',
            'C': 'Ticari defter ve belgeler kanunda öngörülen süre boyunca saklanır; bir yıl sonra imha edilemez',
            'D': 'Defterler hesap dönemi kapandıktan sonra derhâl imha edilebilir',
            'E': 'Defterlerin saklanması tacirin tercihine bırakılmıştır',
        },
        'C',
        'TTK md. 82: her tacir; tutmakla yükümlü olduğu ticari defterleri ve bu defterlere yapılan kayıtların dayandığı belgeleri kanunda öngörülen süre boyunca SAKLAMAKLA yükümlüdür. Yükümlülük tüm tacirleri bağlar; vergi mevzuatındaki saklama süreleri ayrıca uygulanır.',
    ),
    # düzey 2
    '0023': patch(
        'Bir tacir, merkezi başka bir ilde bulunan işletmesine bağlı bir şube açmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Şube, bulunduğu yerin ticaret siciline tescil edilir; merkezin ticaret unvanına şube olduğunu gösteren ibare eklenir',
            'B': 'Şubenin ayrıca tescil edilmesi gerekmez',
            'C': 'Şube bağımsız bir tüzel kişilik kazanır',
            'D': 'Şube açılışı yalnızca vergi dairesine bildirilir',
            'E': 'Şube, merkezin unvanından tümüyle bağımsız kendi ticaret unvanını serbestçe seçer ve ayrı bir tüzel kişi olarak ticaret siciline tescil ettirir',
        },
        'A',
        "TTK md. 40 ve 48: merkezi Türkiye'de bulunan işletmelerin şubeleri, bulundukları yerin ticaret siciline TESCİL ve ilan olunur. Şubenin ticaret unvanı, merkezin unvanına şube olduğunu gösterir bir ek yapılarak oluşturulur. Şubenin ayrı tüzel kişiliği YOKTUR.",
    ),
    # düzey 2
    '0024': patch(
        'Bir tacir, işletmesini tanıtmak için ticaret unvanından farklı bir ad kullanmak istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşletme adı yalnızca tüzel kişi tacirler için mümkündür',
            'B': 'Tacir işletme adı kullanabilir; işletme adı da ticaret siciline tescil ve ilan edilir',
            'C': 'İşletme adı ticaret unvanının yerine geçer',
            'D': 'İşletme adı kullanılabilir ancak tescili gerekmez',
            'E': 'İşletme adı hiç kullanılamaz; işletmenin tanıtımı yalnızca ticaret unvanıyla yapılabilir',
        },
        'B',
        'TTK md. 53: işletme sahibi ile ilgili olmaksızın doğrudan doğruya işletmeyi tanıtmak ve benzer işletmelerden ayırt etmek için kullanılan adların da tescili zorunludur. İşletme adı ticaret unvanının yerine geçmez; ikisi birlikte kullanılır.',
    ),
    # düzey 3
    '0025': patch(
        'Bir tacirin tescil edilmiş ticaret unvanını başka bir kişi haksız olarak kullanmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Unvan sahibi, haksız kullanımın tespitini, önlenmesini ve haksız kullanılan unvanın sicilden silinmesini isteyebilir',
            'B': 'Tescil edilmiş ticaret unvanı kanunen korunur',
            'C': 'Unvan sahibi maddi tazminat talep edebilir',
            'D': 'Tescilli ticaret unvanının korunması için ayrıca marka tescili yaptırılması zorunludur',
            'E': 'Koşulları varsa manevi tazminat da istenebilir',
        },
        'D',
        'TTK md. 52: ticaret unvanı kanuna aykırı olarak başkası tarafından kullanılırsa hak sahibi kullanımın tespitini, yasaklanmasını, haksız kullanılan unvanın silinmesini ve koşulları varsa maddi ile manevi tazminat isteyebilir. Koruma TESCİLDEN doğar; ayrıca marka tescili koşul değildir.',
    ),
    # düzey 3
    '0026': patch(
        'İki tacir, karşılıklı alacaklarını tek tek istemeyip belirli dönemlerde bakiyeyi talep etmek üzere anlaşmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Cari hesap sözleşmesi kurulmuştur; sözleşmenin yazılı yapılması geçerlilik koşuludur',
            'B': 'Cari hesap sözleşmesi ticaret siciline tescil ve ilan edilmedikçe geçersiz sayılır',
            'C': 'Cari hesap sözleşmesi yalnızca bankalarla yapılabilir',
            'D': 'Cari hesap sözleşmesi sözlü olarak da geçerli biçimde kurulabilir',
            'E': 'Cari hesapta taraflar alacaklarını her zaman tek tek isteyebilir',
        },
        'A',
        'TTK md. 89: iki kişinin herhangi bir hukuki sebep veya ilişkiden doğan alacaklarını teker teker ve ayrı ayrı istemekten karşılıklı olarak vazgeçip bunları kalem kalem alacak ve borç şekline çevirerek hesabın kesilmesinden sonra çıkacak bakiyeyi isteyebileceklerine ilişkin sözleşme CARİ HESAP sözleşmesidir. md. 90: sözleşme YAZILI yapılmadıkça geçerli olmaz.',
    ),
    # düzey 3
    '0027': patch(
        'Bir tacir adına, ticari işletmeyi yönetme ve işletmeye ilişkin işlemleri yapma konusunda geniş yetkiyle donatılmış bir kişi görevlendirilmiştir. Bir diğeri ise yalnızca belirli işlerde yetkilendirilmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Her ikisi de tacir sıfatını kazanır',
            'B': 'Her ikisi de pazarlamacı sayılır',
            'C': 'Her ikisi de acente sayılır',
            'D': 'Birincisi ticari vekil, ikincisi ticari temsilcidir',
            'E': 'Birincisi ticari temsilci, ikincisi ticari vekildir',
        },
        'E',
        'TBK md. 547 vd.: TİCARİ TEMSİLCİ, işletme sahibinin işletmeyi yönetme ve işletmeyle ilgili işlemlerde ticaret unvanı altında temsil yetkisi verdiği kişidir. TİCARİ VEKİL ise temsilci sıfatı olmaksızın işletmenin bütün işleri veya belirli bazı işleri için yetkilendirilen kişidir. Tacir yardımcıları bu sıfatla tacir olmaz.',
    ),
    # düzey 2
    '0028': patch(
        'Bir tacir, ticari işletmesini bir bütün hâlinde devretmek istemekte; devrin kapsamını ve şeklini belirlemeye çalışmaktadır. Buna göre ticari işletme kavramı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Devir sözleşmesi yazılı yapılır ve sicile tescil edilir',
            'B': 'Faaliyetin devamlı ve bağımsız biçimde yürütülmesi aranır',
            'C': 'Ticari işletme, esnaf işletmesi sınırını aşan düzeyde gelir hedefleyen işletmedir',
            'D': 'Ticari işletme, unsurları ayrı ayrı devredilmedikçe elden çıkarılamaz',
            'E': 'Ticari işletme bir bütün hâlinde devredilebilir',
        },
        'D',
        'TTK md. 11: ticari işletme, unsurlarının devri için zorunlu tasarruf işlemlerinin ayrı ayrı yapılmasına gerek olmaksızın BİR BÜTÜN hâlinde devredilebilir.',
    ),
    # düzey 2
    '0029': patch(
        'Bir belediye, bir ticaret şirketi ve amacına ulaşmak için ticari işletme işleten bir dernek karşılaştırılmaktadır. Buna göre tacir sıfatı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Amacına varmak için ticari işletme işleten dernekler tacirdir',
            'B': 'Ticaret şirketleri tacirdir',
            'C': 'Belediyeler ve il özel idareleri işlettikleri ticari işletmeler nedeniyle tacir sayılır',
            'D': 'Bir ticari işletmeyi kısmen de olsa kendi adına işleten gerçek kişi tacirdir',
            'E': 'Kamu tüzel kişilerinin işlettiği ticari işletmelere ticari hükümler uygulanır',
        },
        'C',
        'TTK md. 16/2: Devlet, il özel idaresi, belediye ve köy ile diğer kamu tüzel kişileri ile kamuya yararlı dernekler ve gelirinin yarısından fazlasını kamu görevi niteliğindeki işlere harcayan vakıflar TACİR SAYILMAZ. Ancak işlettikleri ticari işletmelere ticari hükümler uygulanır.',
    ),
    # düzey 2
    '0030': patch(
        'Bir tacir, iflasa tabi olmadığını ve ticari işletmesiyle ilgili faaliyetlerinde ortalama bir kişinin özenini göstermenin yeterli olduğunu ileri sürmektedir. Buna göre tacir olmanın hükümleri bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tacir ticari defter tutmakla yükümlüdür',
            'B': 'Tacir, ticari işletmesiyle ilgili faaliyetlerinde ortalama bir kişinin özenini göstermekle yeterli sayılır',
            'C': 'Tacir her türlü borcu için iflasa tabidir',
            'D': 'Tacir basiretli bir iş adamı gibi hareket etmelidir',
            'E': 'Tacir, kanun hükümleri uyarınca bir ticaret unvanı seçmek ve tüm işlemlerinde bu unvanı kullanmakla yükümlüdür',
        },
        'B',
        'TTK md. 18/2: her tacirin ticaretine ait bütün faaliyetlerinde BASİRETLİ BİR İŞ ADAMI GİBİ hareket etmesi gerekir; bu, ortalama bir kişiden beklenenden ağır bir özen ölçüsüdür.',
    ),
    # düzey 2
    '0031': patch(
        'İki kişi, yalnızca biri için ticari nitelik taşıyan bir iş dolayısıyla birlikte borç altına girmiş; faiz oranı da kararlaştırılmamıştır. Buna göre ticari işlerde faiz ve teselsül bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ticari işlerde faiz oranı kural olarak serbestçe belirlenir',
            'B': 'Bileşik faiz yalnızca kanunda sayılan hâllerde mümkündür',
            'C': 'Faiz oranı belirlenmemişse kanuni faiz uygulanır',
            'D': 'Ticari işlerde borçlular arasında müteselsil sorumluluk karinesi bulunmaz',
            'E': 'Aksi kararlaştırılmadıkça ticari işlerde borçlular müteselsilen sorumludur',
        },
        'D',
        'TTK md. 7: iki veya daha fazla kişi, içlerinden yalnız biri veya hepsi için ticari nitelikte bir iş dolayısıyla borç altına girerse, aksi öngörülmedikçe MÜTESELSİLEN sorumlu olur. Ticari işlerde teselsül KARİNESİ vardır.',
    ),
    # düzey 2
    '0032': patch(
        'Bir tacir, kendisine ulaşan faturaya ve telefonla kurulan sözleşmeye ilişkin teyit mektubuna yirmi gün sonra itiraz etmiştir. Buna göre fatura ve teyit mektubu bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Teyit mektubuna sekiz gün içinde itiraz edilmezse içeriği kabul edilmiş sayılır',
            'B': 'Faturaya itiraz için otuz günlük bir süre öngörülmüştür',
            'C': 'Fatura, sözleşmenin kurulmasından sonra düzenlenir',
            'D': 'İtiraz süreleri hak düşürücü nitelikte sonuçlar doğurur',
            'E': 'Faturayı alan sekiz gün içinde itiraz etmezse içeriği kabul etmiş sayılır',
        },
        'B',
        'TTK md. 21: faturayı alan kişi aldığı tarihten itibaren SEKİZ GÜN içinde içeriği hakkında itirazda bulunmazsa içeriği kabul etmiş sayılır. Aynı süre teyit mektupları için de geçerlidir.',
    ),
    # düzey 2
    '0033': patch(
        'Bir tacir, işletmesini ticaret siciline tescil ettirmiş ancak ticaret unvanını işletmesinde görünür biçimde yazmamıştır. Buna göre ticaret sicili ve ticaret unvanı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tescil ve ilan edilen hususlar, iyiniyetli olsun olmasın üçüncü kişilere karşı ileri sürülebilir',
            'B': 'Tacir işlemlerini ticaret unvanıyla yapar',
            'C': 'Tescilli ticaret unvanı kanunen korunur',
            'D': 'Ticaret sicili alenidir',
            'E': 'Ticaret sicili gizli olup yalnızca ilgili taraflarca incelenebilir',
        },
        'E',
        'TTK md. 35 vd.: ticaret sicili ALENİDİR; herkes sicil kayıtlarını inceleyebilir ve onaylı suret isteyebilir. Aleniyet, sicile bağlanan hukuki sonuçların temelidir.',
    ),
    # düzey 2
    '0034': patch(
        'Bir tacir, tutacağı defterleri ve bunların ispat gücünü belirlemeye çalışmaktadır. Buna göre ticari defterler bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ticari defterler yalnızca sahibi aleyhine delil oluşturur',
            'B': 'Her tacir yevmiye defteri, defterikebir ve envanter defteri tutar',
            'C': 'Defterlerin açılış ve kapanış onayları kanunda düzenlenmiştir',
            'D': 'Defterler ve dayanak belgeler kanunda öngörülen süre boyunca saklanır',
            'E': 'Anonim şirketler ayrıca pay defteri ve karar defteri tutar',
        },
        'A',
        'Usulüne uygun tutulan ticari defterler sahibi ALEYHİNE delil oluşturabileceği gibi, kanunda öngörülen koşullar gerçekleştiğinde LEHİNE de delil oluşturabilir; değerlendirme mahkemeye aittir.',
    ),
    # düzey 2
    '0035': patch(
        'Ticari işletme ve tacir ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Ticari işletme bir bütün hâlinde devredilebilir. II. Bir ticari işletmeyi kısmen de olsa kendi adına işleten gerçek kişi tacirdir. III. Belediyeler işlettikleri ticari işletmeler nedeniyle tacir sayılır.',
        {
            'A': 'I ve III',
            'B': 'I, II ve III',
            'C': 'I ve II',
            'D': 'Yalnız I',
            'E': 'II ve III',
        },
        'C',
        'I doğrudur (TTK md. 11/3). II doğrudur (md. 12). III YANLIŞTIR: md. 16/2 uyarınca belediye ve diğer kamu tüzel kişileri TACİR SAYILMAZ; yalnızca işlettikleri işletmelere ticari hükümler uygulanır.',
    ),
    # düzey 3
    '0036': patch(
        'Tacir olmanın hükümleri ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Tacir her türlü borcu için iflasa tabidir. II. Tacir basiretli bir iş adamı gibi hareket etmelidir. III. Faturaya itiraz süresi otuz gündür. IV. Ticari işlerde müteselsil sorumluluk karinesi bulunmaz.',
        {
            'A': 'I, III ve IV',
            'B': 'II ve III',
            'C': 'Yalnız III',
            'D': 'III ve IV',
            'E': 'I ve II',
        },
        'D',
        'III YANLIŞ: TTK md. 21 uyarınca faturaya itiraz süresi SEKİZ GÜNDÜR. IV YANLIŞ: md. 7 ticari işlerde MÜTESELSİL sorumluluk karinesi getirir. I (md. 18) ve II (md. 18/2) doğrudur.',
    ),
    # düzey 2
    '0037': patch(
        'Ticaret sicili ve unvan ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Ticaret sicili alenidir. II. Tacir işletmesiyle ilgili işlemleri ticaret unvanıyla yapar. III. Şube bağımsız bir tüzel kişilik kazanır.',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'Yalnız I',
            'D': 'I ve III',
            'E': 'I, II ve III',
        },
        'A',
        'I doğrudur (TTK md. 35 vd.). II doğrudur (md. 39). III YANLIŞTIR: şubenin ayrı tüzel kişiliği yoktur; merkeze bağlıdır ve unvanı merkezin unvanına ek yapılarak oluşturulur (md. 48).',
    ),
    # düzey 3
    '0038': patch(
        'Ticari işletme ve tacir ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Esnaf, ticari işletme işleten kişidir. II. Küçüğe ait işletmede tacir sıfatı küçüğe aittir. III. Ticari işletme rehni zilyetliğin devrini gerektirir. IV. Cari hesap sözleşmesi yazılı yapılmadıkça geçerli olmaz.',
        {
            'A': 'I, III ve IV',
            'B': 'II ve IV',
            'C': 'I ve III',
            'D': 'Yalnız I',
            'E': 'I ve II',
        },
        'C',
        'I YANLIŞ: TTK md. 15 uyarınca esnafın faaliyeti sermayesinden çok bedeni çalışmasına dayanır ve geliri sınırı aşmaz; ticari işletme işletmez. III YANLIŞ: ticari işletme rehni zilyetlik devredilmeksizin sicile tescille kurulur. II (md. 13) ve IV (md. 90) doğrudur.',
    ),
    # düzey 0
    '0039': patch(
        'Bir kişi, esnaf işletmesi için öngörülen sınırı aşan düzeyde gelir hedefleyen ve devamlı biçimde yürütülen bir işletme kurmuştur. Buna göre bu işletme aşağıdakilerden hangisidir?',
        {
            'A': 'Esnaf işletmesi',
            'B': 'Ticari işletme',
            'C': 'Adi ortaklık',
            'D': 'Kamu işletmesi',
            'E': 'Serbest meslek işletmesi',
        },
        'B',
        'TTK md. 11: ticari işletme, esnaf işletmesi için öngörülen sınırı aşan düzeyde gelir sağlamayı hedef tutan faaliyetlerin devamlı ve bağımsız şekilde yürütüldüğü işletmedir.',
    ),
    # düzey 0
    '0040': patch(
        'Bir ticari işletmeyi kısmen de olsa kendi adına işleten gerçek kişinin sıfatı aşağıdakilerden hangisidir?',
        {
            'A': 'Ticari temsilci',
            'B': 'Komisyoncu',
            'C': 'Tacir',
            'D': 'Acente',
            'E': 'Esnaf',
        },
        'C',
        'TTK md. 12: bir ticari işletmeyi, kısmen de olsa kendi adına işleten kişiye TACİR denir.',
    ),
    # düzey 0
    '0041': patch(
        'Ekonomik faaliyeti sermayesinden çok bedeni çalışmasına dayanan ve geliri kanunda öngörülen sınırı aşmayan kişinin sıfatı aşağıdakilerden hangisidir?',
        {
            'A': 'Simsar',
            'B': 'Esnaf',
            'C': 'Ticari vekil',
            'D': 'Pazarlamacı',
            'E': 'Tacir',
        },
        'B',
        'TTK md. 15: ekonomik faaliyeti sermayesinden fazla bedeni çalışmasına dayanan ve geliri belirlenen sınırı aşmayan kişi ESNAFTIR; ticari işletme işletmez.',
    ),
    # düzey 0
    '0042': patch(
        'Bir tacirin ticari işletmesine ilişkin işlemleri altında yaptığı ad aşağıdakilerden hangisidir?',
        {
            'A': 'Ticaret unvanı',
            'B': 'Ticari isim',
            'C': 'İşletme adı',
            'D': 'Tescilli tasarım',
            'E': 'Marka',
        },
        'A',
        'TTK md. 39: her tacir, ticari işletmesine ilişkin işlemleri TİCARET UNVANIYLA yapmak ve belgeleri bu unvan altında imzalamak zorundadır. İşletme adı ise işletmeyi tanıtmaya yarar.',
    ),
    # düzey 0
    '0043': patch(
        'Faturayı alan kişinin içeriğine itiraz edebileceği süre aşağıdakilerden hangisidir?',
        {
            'A': 'Üç gün',
            'B': 'Bir ay',
            'C': 'On beş gün',
            'D': 'Üç ay',
            'E': 'Sekiz gün',
        },
        'E',
        'TTK md. 21/2: faturayı alan kişi, aldığı tarihten itibaren SEKİZ GÜN içinde içeriği hakkında itirazda bulunmamışsa faturanın içeriğini kabul etmiş sayılır.',
    ),
    # düzey 1
    '0044': patch(
        'Bir tacir, ticari işletmesiyle ilgili bir uyuşmazlıkta hangi mahkemeye başvuracağını araştırmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ticari davalar sulh hukuk mahkemesinde görülür',
            'B': 'Ticari davalar icra mahkemesinde görülür',
            'C': 'Ticari davalar kural olarak asliye ticaret mahkemesinde görülür',
            'D': 'Ticari davalar tüketici mahkemesinde görülür',
            'E': 'Ticari davalar için görevli mahkeme taraflarca serbestçe belirlenir',
        },
        'C',
        'TTK md. 4-5: ticari davalar, aksine hüküm bulunmadıkça ASLİYE TİCARET MAHKEMESİNDE görülür; bu mahkemenin bulunmadığı yerlerde davaya asliye hukuk mahkemesi bakar.',
    ),
    # düzey 1
    '0045': patch(
        'Bir tacir, ticari işletmesini ticaret siciline tescil ettirmemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tescil edilmeyen işletme için hiçbir yükümlülük doğmaz',
            'B': 'Tescil yalnızca tüzel kişi tacirler için zorunludur',
            'C': 'Tescil, tacir sıfatının kurucu unsurudur',
            'D': 'Tacir sıfatı ticari işletmenin işletilmesiyle doğar; tescil ettirmemek tacir sıfatını ortadan kaldırmaz',
            'E': 'Ticaret siciline tescil ettirilmemiş bir işletmeyi kendi adına işleten kişi tacir sıfatını kazanmaz',
        },
        'D',
        'TTK md. 12: tacir sıfatı, bir ticari işletmenin kısmen de olsa kendi adına işletilmesiyle doğar; tescil BİLDİRİCİ etkilidir. Tescil ettirmemek tacir sıfatını kaldırmaz, aksine md. 18 uyarınca yükümlülüklere aykırılık oluşturur.',
    ),
    # düzey 1
    '0046': patch(
        'Bir tacirin ticari işletmesine ilişkin borçlarından dolayı iflasa tabi olup olmadığı sorulmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tacir yalnızca ticari borçları için iflasa tabidir',
            'B': 'Tacir, ticari olsun olmasın her türlü borcu için iflasa tabidir',
            'C': 'İflasa tabi olmak yalnızca ticaret siciline kayıtlı tacirler için geçerlidir',
            'D': 'Tacirin iflasa tabi olması yalnızca tüzel kişilerde söz konusudur',
            'E': 'Tacir hiçbir borcu için iflasa tabi değildir',
        },
        'B',
        'TTK md. 18/1: tacir, her türlü borcu için İFLASA TABİDİR. Borcun ticari olup olmaması ya da tacirin gerçek veya tüzel kişi olması sonucu değiştirmez.',
    ),
    # düzey 1
    '0047': patch(
        'Bir tacir, ticari işletmesiyle ilgili verdiği hizmet için ücret ve yaptığı giderler için faiz talep etmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tacir yalnızca giderlerini isteyebilir, ücret isteyemez',
            'B': 'Ücret ve faiz talebi yalnızca her iki tarafın da tacir sıfatını taşıdığı işlemlerde ileri sürülebilir; bunun dışındaki hâllerde herhangi bir talep hakkı doğmaz',
            'C': 'Tacir ancak yazılı sözleşme varsa ücret isteyebilir',
            'D': 'Tacir yalnızca ücret isteyebilir, faiz isteyemez',
            'E': 'Tacir, ticari işletmesiyle ilgili gördüğü iş ve hizmet için uygun bir ücret ile verdiği avans ve giderler için faiz isteyebilir',
        },
        'E',
        'TTK md. 20: ticari işletmesiyle ilgili bir iş veya hizmet görmüş olan tacir, uygun bir ÜCRET isteyebilir; ayrıca verdiği avanslar ve yaptığı giderler için ödeme tarihinden itibaren FAİZ isteyebilir. Karşı tarafın tacir olması şart değildir.',
    ),
    # düzey 1
    '0048': patch(
        'Bir şubenin hukuki durumu tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Şube yalnızca vergi dairesine bildirilir',
            'B': 'Şube, merkezden bağımsız kendi ticaret unvanını serbestçe seçip kullanabilir',
            'C': 'Şubenin ayrı tüzel kişiliği yoktur; bulunduğu yerin ticaret siciline tescil edilir',
            'D': 'Şube ayrı bir tüzel kişilik kazanır',
            'E': 'Şubenin tescili gerekmez',
        },
        'C',
        'TTK md. 40 ve 48: şubeler bulundukları yerin ticaret siciline tescil ve ilan olunur; şubenin unvanı merkezin unvanına şube olduğunu gösteren ek yapılarak oluşturulur. Şubenin AYRI TÜZEL KİŞİLİĞİ YOKTUR.',
    ),
    # düzey 1
    '0049': patch(
        'Ticari hükümlerle düzenlenmemiş bir konuda hâkimin başvuracağı kaynak sırası bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Uyuşmazlık hakkında karar verilemez',
            'B': 'Yalnızca ticari örf ve âdet uygulanır',
            'C': 'Hâkim, kanunda öngörülen kaynak sırasıyla bağlı olmaksızın uygulanacak kuralı serbestçe belirler',
            'D': 'Önce ticari örf ve âdete, bulunmazsa genel hükümlere başvurulur',
            'E': 'Doğrudan genel hükümlere başvurulur',
        },
        'D',
        'TTK md. 1 ve 2: ticari hükümlerle düzenlenmemiş konularda TİCARİ ÖRF VE ÂDETE, bu da yoksa genel hükümlere göre karar verilir.',
    ),
    # düzey 1
    '0050': patch(
        'Bir tacir, ticari defterlerinin saklanması yükümlülüğünü sorgulamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ticari defterler ve dayanak belgeler kanunda öngörülen süre boyunca saklanır',
            'B': 'Saklama yükümlülüğü yalnızca elektronik defterler için öngörülmüştür',
            'C': 'Saklama yükümlülüğü yalnızca vergi mevzuatından doğar',
            'D': 'Defterler hesap dönemi kapandığında imha edilebilir',
            'E': 'Saklama süresi tacirin takdirine bırakılmıştır',
        },
        'A',
        'TTK md. 82: her tacir, tutmakla yükümlü olduğu defterleri ve kayıtların dayandığı belgeleri kanunda öngörülen süre boyunca SAKLAMAKLA yükümlüdür; vergi mevzuatındaki süreler ayrıca uygulanır.',
    ),
    # düzey 2
    '0051': patch(
        'Bir tacirin ticari işletmesini devrettiği durumda devrin kapsamı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Aksi öngörülmemişse devir işletme değerini de kapsar',
            'B': 'Devir sözleşmesi, aksi kararlaştırılmadıkça yalnızca duran malvarlığını kapsar',
            'C': 'Aksi öngörülmemişse devir kiracılık hakkını da kapsar',
            'D': 'Ticari işletme bir bütün hâlinde devredilebilir',
            'E': 'Devir sözleşmesi yazılı yapılır ve ticaret siciline tescil ile ilan edilir',
        },
        'B',
        'TTK md. 11/3: aksi öngörülmemişse devir sözleşmesi duran malvarlığını, İŞLETME DEĞERİNİ, KİRACILIK HAKKINI, ticaret unvanı ile diğer fikri mülkiyet haklarını ve sürekli olarak işletmeye özgülenen malvarlığı unsurlarını içerir.',
    ),
    # düzey 2
    '0052': patch(
        'Küçük ve kısıtlılara ait ticari işletmeler bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tacir sıfatı temsil edilen küçüğe aittir',
            'B': 'Ceza ve disiplin sorumlulukları yasal temsilciye aittir',
            'C': 'Yasal temsilci, işletmenin sahibi olmadığı için tacir sayılmaz',
            'D': 'Küçük, ergin olduğunda tacir sıfatını sürdürebilir',
            'E': 'İşletmeyi küçük adına işleten yasal temsilci tacir sıfatını kazanır',
        },
        'E',
        'TTK md. 13: küçük ve kısıtlılara ait ticari işletmeyi bunların adına işleten yasal temsilci, işletmenin sahibi olmadığı için TACİR SAYILMAZ; tacir sıfatı temsil edilene aittir. Ceza ve disiplin sorumlulukları ise temsilciye yüklenmiştir.',
    ),
    # düzey 2
    '0053': patch(
        'İki tacir, karşılıklı alacaklarını tek tek istemeyip dönem sonunda bakiyeyi talep etmek üzere sözlü olarak anlaşmıştır. Buna göre cari hesap sözleşmesi bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Cari hesap sözleşmesi sözlü olarak da geçerli biçimde kurulabilir',
            'B': 'Sözleşmenin yazılı yapılması gerekir',
            'C': 'Taraflar alacaklarını tek tek istemekten karşılıklı olarak vazgeçer',
            'D': 'Hesabın kesilmesinden sonra çıkacak bakiye istenebilir',
            'E': 'Cari hesap sözleşmesi bileşik faiz uygulanabilen hâllerdendir',
        },
        'A',
        'TTK md. 89-90: cari hesap sözleşmesi, tarafların alacaklarını tek tek istemekten vazgeçip bakiyeyi talep etmelerine ilişkindir ve YAZILI yapılmadıkça geçerli olmaz. md. 8/2 uyarınca cari hesap, bileşik faize izin verilen sınırlı hâllerdendir.',
    ),
    # düzey 2
    '0054': patch(
        'Bir işletmede ticari temsilci, ticari vekil ve acente birlikte görev yapmaktadır. Buna göre tacir yardımcıları bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tacir yardımcılarının yetkileri kapsam bakımından farklılaşır',
            'B': 'Ticari temsilci ve ticari vekil, bu sıfatları nedeniyle tacir sayılır',
            'C': 'Acente, bağımsız bir tacir yardımcısıdır',
            'D': 'Ticari vekil, temsilci sıfatı olmaksızın belirli işler için yetkilendirilir',
            'E': 'Ticari temsilci işletmeyi yönetme ve temsil yetkisiyle donatılmıştır',
        },
        'B',
        'Tacir yardımcıları (TBK md. 547 vd. ve TTK md. 102 vd.) işletme sahibi adına iş görür; bu sıfatları TACİR OLMALARINI SAĞLAMAZ. Tacir sıfatı, işletmeyi kendi adına işletene aittir (TTK md. 12). Acente ise kendi ticari işletmesi bulunan bağımsız bir yardımcıdır.',
    ),
    # düzey 2
    '0055': patch(
        'Bir tacirin tescilli ticaret unvanı, başka bir kişi tarafından izinsiz kullanılmaktadır. Buna göre ticaret unvanının korunması bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Hak sahibi, haksız kullanımın önlenmesini ve unvanın sicilden silinmesini isteyebilir',
            'B': 'Hak sahibi haksız kullanımın tespitini isteyebilir',
            'C': 'Koşulları varsa maddi ve manevi tazminat istenebilir',
            'D': 'Ticaret unvanının korunabilmesi için ayrıca marka olarak tescil edilmesi gerekir',
            'E': 'Tescilli ticaret unvanı kanunen korunur',
        },
        'D',
        'TTK md. 52: ticaret unvanı kanuna aykırı olarak başkası tarafından kullanılırsa hak sahibi tespit, önleme, silme ve koşulları varsa maddi-manevi tazminat isteyebilir. Koruma TESCİLDEN doğar; ayrı bir marka tescili koşul değildir.',
    ),
    # düzey 2
    '0056': patch(
        'Bir tacir ile tacir olmayan bir kişi arasında, tacirin işletmesini ilgilendiren bir işlem yapılmıştır. Buna göre ticari iş kavramı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "TTK'da düzenlenen hususlar ticari iştir",
            'B': 'Bir işlemin ticari iş sayılabilmesi için her iki tarafın da tacir olması gerekir',
            'C': 'Ticari işlerde müteselsil sorumluluk karinesi geçerlidir',
            'D': 'Ticari işlerde faiz oranı kural olarak serbestçe belirlenir',
            'E': 'Bir ticari işletmeyi ilgilendiren bütün işlem ve fiiller de ticari iş sayılır',
        },
        'B',
        'TTK md. 3: bu Kanunda düzenlenen hususlarla bir ticari işletmeyi ilgilendiren bütün işlem ve fiiller ticari iştir. Her iki tarafın da tacir olması ARANMAZ; işin bir taraf için ticari olması yeterlidir.',
    ),
    # düzey 2
    '0057': patch(
        'Ticari işletme ve tacir ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Tacir her türlü borcu için iflasa tabidir. II. Tacir ticari defter tutmakla yükümlüdür. III. Esnaf ticari işletme işletir.',
        {
            'A': 'II ve III',
            'B': 'I, II ve III',
            'C': 'I ve III',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'D',
        'I ve II doğrudur (TTK md. 18). III YANLIŞTIR: md. 15 uyarınca esnafın faaliyeti sermayesinden çok bedeni çalışmasına dayanır ve geliri sınırı aşmaz; ticari işletme işletmez.',
    ),
    # düzey 2
    '0058': patch(
        'Fatura, teyit mektubu ve ticari örf ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Faturaya sekiz gün içinde itiraz edilmezse içeriği kabul edilmiş sayılır. II. Teyit mektubuna sekiz gün içinde itiraz edilmezse içeriği kabul edilmiş sayılır. III. Ticari hükümlerle düzenlenmemiş konularda önce genel hükümlere başvurulur.',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'II ve III',
            'D': 'I ve III',
            'E': 'Yalnız I',
        },
        'A',
        'I ve II doğrudur (TTK md. 21). III YANLIŞTIR: md. 1 ve 2 uyarınca önce TİCARİ ÖRF VE ÂDETE, bulunmazsa genel hükümlere başvurulur.',
    ),
    # düzey 2
    '0059': patch(
        'Bir tacir, tescili gerektiği hâlde tescil ettirmediği bir hususu iyiniyetli bir üçüncü kişiye karşı ileri sürmek istemektedir. Buna göre ticari defterler ve ticaret sicili bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tescil ve ilan edilen hususlar, iyiniyetli olsun olmasın üçüncü kişilere karşı ileri sürülebilir',
            'B': 'Ticaret sicili alenidir',
            'C': 'Ticaret siciline tescil edilmemiş bir husus, iyiniyetli üçüncü kişilere karşı ileri sürülebilir',
            'D': 'Defterlerin açılış ve kapanış onayları kanunda düzenlenmiştir',
            'E': 'Her tacir yevmiye defteri, defterikebir ve envanter defteri tutar',
        },
        'C',
        'TTK md. 36: tescili gerekirken tescil edilmemiş ya da tescil edilip de ilanı gerekirken ilan edilmemiş hususlar, ancak bunları BİLEN kişilere karşı ileri sürülebilir; İYİNİYETLİ üçüncü kişilere karşı ileri sürülemez.',
    ),
    # düzey 3
    '0060': patch(
        'Ticari işletme, tacir ve ticari iş ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Ticari işletme bir bütün hâlinde devredilebilir. II. Belediyeler işlettikleri ticari işletmeler nedeniyle tacir sayılır. III. Ticari işlerde faiz oranı kanunla sabitlenmiş olup değiştirilemez. IV. Tacir basiretli bir iş adamı gibi hareket etmelidir.',
        {
            'A': 'I ve IV',
            'B': 'I, II ve III',
            'C': 'Yalnız II',
            'D': 'II ve III',
            'E': 'III ve IV',
        },
        'D',
        'II YANLIŞ: TTK md. 16/2 uyarınca belediye ve diğer kamu tüzel kişileri TACİR SAYILMAZ; yalnız işlettikleri işletmelere ticari hükümler uygulanır. III YANLIŞ: md. 8-9 uyarınca ticari işlerde faiz oranı kural olarak SERBESTÇE belirlenir. I (md. 11/3) ve IV (md. 18/2) doğrudur.',
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
    print(f"1 paket / {len(PATCHES)} soru (Ticari Isletme ve Tacir yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
