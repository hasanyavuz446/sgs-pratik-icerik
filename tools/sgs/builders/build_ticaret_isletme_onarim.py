#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ticari Isletme ve Tacir — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Agustos yapisal kalibrasyonundaki olay tabanli 60 soru korunarak onarildi: genisletilmis ELEME_ISARETI olcutune gore 64 mutlak ifadeli sik (yalnizca/hicbir/serbestce/her zaman...) ayni dogruluk degerini koruyacak bicimde yeniden yazildi; gerekce tasiyan 14 dogru sik kisaltildi (gercek sinav medyan sik ~33 karakter). Kor ogrenci %48 -> %22.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 6102 sayili Turk Ticaret Kanunu (md. 1-90 ilgili hukumler)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/ticaret_hukuku/ticari_isletme_tacir.json"
STYLE_REF = 'SGS Ticaret Hukuku (gercek sinav yapisina kalibre: olay + kural uygulamasi)'
ONEK = "tic-isletme-gen-"


def patch(stem, options, answer, solution, ref='6102 sayili Turk Ticaret Kanunu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        'Bir kişi, sermayesinden çok bedeni çalışmasına dayanan ve geliri kanunda öngörülen sınırı aşmayan bir terzilik faaliyeti yürütmektedir. Bir diğeri ise aynı sınırı aşan düzeyde gelir hedefleyen, devamlı ve bağımsız bir konfeksiyon işletmesi işletmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Her ikisi de esnaftır',
            'B': 'Birincisi esnaf, ikincisi ticari işletme işleten tacirdir',
            'C': 'Ayrım, ticaret siciline kayıt olup olmamaya göre yapılır',
            'D': 'Her ikisi de tacirdir',
            'E': 'Birincisi tacir, ikincisi esnaftır',
        },
        'B',
        'TTK md. 11: ticari işletme, esnaf işletmesi için öngörülen sınırı aşan düzeyde gelir sağlamayı hedef tutan faaliyetlerin devamlı ve bağımsız şekilde yürütüldüğü işletmedir. md. 15: ekonomik faaliyeti sermayesinden fazla BEDENİ ÇALIŞMASINA dayanan ve geliri sınırı aşmayan kişi ESNAFTIR. Ayrım sicile kayda değil, faaliyetin niteliğine dayanır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0002': patch(
        'Bir tacir, ticari işletmesini bir bütün hâlinde devretmek istemektedir. Devir sözleşmesinin kapsamı ve şekli tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ticari işletme ancak unsurları tek tek devredilerek elden çıkarılabilir',
            'B': 'Devir ticaret siciline tescil ve ilan edilir',
            'C': 'Aksi öngörülmemişse devir; duran malvarlığını, işletme değerini ve kiracılık hakkını içerir',
            'D': 'Ticari işletme bir bütün hâlinde devredilebilir',
            'E': 'Devir sözleşmesi yazılı yapılır',
        },
        'A',
        'TTK md. 11/3: ticari işletme, içerdiği malvarlığı unsurlarının devri için zorunlu tasarruf işlemlerinin ayrı ayrı yapılmasına gerek olmaksızın BİR BÜTÜN hâlinde devredilebilir ve diğer hukuki işlemlere konu olabilir. Aksi öngörülmemişse devir sözleşmesi duran malvarlığını, işletme değerini, kiracılık hakkını, ticaret unvanı ile diğer fikri mülkiyet haklarını içerir. Devir yazılı yapılır, ticaret siciline tescil ve ilan edilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0003': patch(
        'Bir tacir, ticari işletmesiyle ilgili faaliyetlerinde ortalama bir kişinin göstereceği özeni yeterli saydığını ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tacir için özel bir özen ölçüsü öngörülmemiştir',
            'B': 'Özen ölçüsü taraflarca sözleşmeyle belirlenir',
            'C': 'Tacirin her türlü faaliyetinde basiretli bir iş adamı gibi hareket etmesi gerekir',
            'D': 'Basiretli iş adamı ölçüsü tüzel kişi tacirlere özgü olup gerçek kişi tacirleri bağlamaz',
            'E': 'Tacir, ortalama bir kişinin özenini göstermekle yeterli sayılır',
        },
        'C',
        'TTK md. 18/2: her tacirin, ticaretine ait bütün faaliyetlerinde BASİRETLİ BİR İŞ ADAMI GİBİ hareket etmesi gerekir. Bu, ortalama bir kişiden beklenenden AĞIR bir özen ölçüsüdür ve tüm tacirleri bağlar; sözleşmeyle hafifletilemez.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0004': patch(
        "Bir tacirin ticari işletmesini ilgilendiren bir işlem ile TTK'da düzenlenen bir hususa ilişkin başka bir işlem söz konusudur. Buna göre ticari iş kavramı bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Bir işlemin ticari iş sayılabilmesi için ayrıca ticaret siciline tescil edilmiş ve usulüne uygun biçimde ilan olunmuş olması gerekir',
            'B': 'Ticari iş kavramı tacirler arasındaki işlemlerle sınırlıdır',
            'C': "Ticari iş, TTK'da düzenlenen hususlardan ibarettir",
            'D': "Her ikisi de ticari iştir; TTK'da düzenlenen hususlar ile bir ticari işletmeyi ilgilendiren işlem ve fiiller ticari iştir",
            'E': 'Ticari iş, ticari işletmeyi ilgilendiren işlemlerden ibarettir',
        },
        'D',
        'TTK md. 3: bu Kanunda düzenlenen hususlarla bir ticari işletmeyi ilgilendiren bütün işlem ve fiiller TİCARİ İŞTİR. Tanım iki ölçütü birlikte kapsar; tarafların ikisinin de tacir olması ya da işlemin tescili aranmaz.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0005': patch(
        'Bir tacir, ticari işletmesiyle ilgili işlemleri kendi ad ve soyadıyla yapmakta, ticaret unvanını kullanmamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ticaret unvanı sicile kayıt amacıyla kullanılır, işlemlerde kullanılmaz',
            'B': 'Ticaret unvanı tüzel kişi tacirler için zorunlu, gerçek kişiler için isteğe bağlıdır',
            'C': 'Tacir, işlemlerini dilerse ad ve soyadıyla yapabilir; ayrıca ticaret unvanı kullanma yükümlülüğü bulunmaz',
            'D': 'Ticaret unvanının işletmede görünür biçimde yazılması gerekmez',
            'E': 'İşlemlerini ticaret unvanıyla yapar ve unvanı işletmede görünür biçimde yazar',
        },
        'E',
        'TTK md. 39: her tacir, ticari işletmesine ilişkin işlemleri TİCARET UNVANIYLA yapmak ve işletmesiyle ilgili senetlerle diğer belgeleri bu unvan altında imzalamak zorundadır. Tescil edilen ticaret unvanı, işletmenin görülebilecek bir yerine okunaklı biçimde YAZILIR. Yükümlülük gerçek ve tüzel kişi tacirlerin tamamını bağlar.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0006': patch(
        'İki tacir arasında telefonla bir sözleşme kurulmuş; taraflardan biri sözleşmenin özetini içeren bir teyit mektubu göndermiştir. Karşı taraf mektubu aldıktan 12 gün sonra itiraz etmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sekiz gün içinde itiraz edilmediğinden teyit mektubu içeriği kabul edilmiş sayılır',
            'B': 'Faturaya itiraz süresi bir ay olarak öngörüldüğünden yapılan itiraz süresinde sayılır',
            'C': 'Teyit mektubu ancak karşı tarafça imzalanırsa bağlayıcı olur',
            'D': 'Teyit mektubu hukuki sonuç doğurmaz',
            'E': 'Teyit mektubuna itiraz için süre öngörülmemiştir',
        },
        'A',
        'TTK md. 21/3: telefonla, telgrafla, herhangi bir iletişim veya bilişim aracıyla ya da diğer bir teknik araçla veya sözlü olarak kurulan sözleşmelerle yapılan açıklamaların içeriğini doğrulayan bir yazıyı alan kişi, aldığı tarihten itibaren SEKİZ GÜN içinde itirazda bulunmamışsa, söz konusu teyit mektubunun içeriğini kabul etmiş sayılır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0007': patch(
        'Bir tacir, ticari işletmesini teslim etmeksizin teminat olarak göstermek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ticari işletme, ancak zilyetliği alacaklıya devredilmek suretiyle rehnedilebilir',
            'B': 'Ticari işletme rehni ancak noterde düzenlenirse geçerli olur',
            'C': 'Ticari işletme, bir bütün olarak rehne konu edilemez',
            'D': 'İşletme, zilyetlik devredilmeksizin sicile tescille rehnedilebilir',
            'E': 'Ticari işletme rehni taşınmazlarla sınırlıdır',
        },
        'D',
        'Ticari işlemlerde taşınır rehni mevzuatı: ticari işletme, zilyetliğin devredilmesine gerek olmaksızın rehin sicilinde TESCİL edilmek suretiyle rehnedilebilir. Bu, işletmenin faaliyetini sürdürerek kredi temin etmesine imkân verir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0008': patch(
        'Bir tacir, merkezi başka bir ilde bulunan işletmesine bağlı bir şube açmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Şube, merkezin unvanından bağımsız kendi ticaret unvanını seçer ve ayrı bir tüzel kişi olarak ticaret siciline tescil edilir',
            'B': 'Şube, bulunduğu yerin ticaret siciline tescil edilir; merkezin ticaret unvanına şube olduğunu gösteren ibare eklenir',
            'C': 'Şube açılışı vergi dairesine bildirilir, sicile tescil edilmez',
            'D': 'Şubenin ayrıca tescil edilmesi gerekmez',
            'E': 'Şube bağımsız bir tüzel kişilik kazanır',
        },
        'B',
        "TTK md. 40 ve 48: merkezi Türkiye'de bulunan işletmelerin şubeleri, bulundukları yerin ticaret siciline TESCİL ve ilan olunur. Şubenin ticaret unvanı, merkezin unvanına şube olduğunu gösterir bir ek yapılarak oluşturulur. Şubenin ayrı tüzel kişiliği YOKTUR.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0009': patch(
        'Bir tacirin tescil edilmiş ticaret unvanını başka bir kişi haksız olarak kullanmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Unvan sahibi, haksız kullanımın tespitini, önlenmesini ve haksız kullanılan unvanın sicilden silinmesini isteyebilir',
            'B': 'Tescil edilmiş ticaret unvanı kanunen korunur',
            'C': 'Unvan sahibi maddi tazminat talep edebilir',
            'D': 'Koşulları varsa manevi tazminat da istenebilir',
            'E': 'Tescilli ticaret unvanının korunması için ayrıca marka tescili yaptırılması zorunludur',
        },
        'E',
        'TTK md. 52: ticaret unvanı kanuna aykırı olarak başkası tarafından kullanılırsa hak sahibi kullanımın tespitini, yasaklanmasını, haksız kullanılan unvanın silinmesini ve koşulları varsa maddi ile manevi tazminat isteyebilir. Koruma TESCİLDEN doğar; ayrıca marka tescili koşul değildir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0010': patch(
        'Bir belediye, bir ticaret şirketi ve amacına ulaşmak için ticari işletme işleten bir dernek karşılaştırılmaktadır. Buna göre tacir sıfatı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ticaret şirketleri tacirdir',
            'B': 'Amacına varmak için ticari işletme işleten dernekler tacirdir',
            'C': 'Belediyeler ve il özel idareleri işlettikleri ticari işletmeler nedeniyle tacir sayılır',
            'D': 'Bir ticari işletmeyi kısmen de olsa kendi adına işleten gerçek kişi tacirdir',
            'E': 'Kamu tüzel kişilerinin işlettiği ticari işletmelere ticari hükümler uygulanır',
        },
        'C',
        'TTK md. 16/2: Devlet, il özel idaresi, belediye ve köy ile diğer kamu tüzel kişileri ile kamuya yararlı dernekler ve gelirinin yarısından fazlasını kamu görevi niteliğindeki işlere harcayan vakıflar TACİR SAYILMAZ. Ancak işlettikleri ticari işletmelere ticari hükümler uygulanır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0011': patch(
        'Bir tacir, kendisine ulaşan faturaya ve telefonla kurulan sözleşmeye ilişkin teyit mektubuna yirmi gün sonra itiraz etmiştir. Buna göre fatura ve teyit mektubu bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Teyit mektubuna sekiz gün içinde itiraz edilmezse içeriği kabul edilmiş sayılır',
            'B': 'İtiraz süreleri hak düşürücü nitelikte sonuçlar doğurur',
            'C': 'Faturayı alan sekiz gün içinde itiraz etmezse içeriği kabul etmiş sayılır',
            'D': 'Fatura, sözleşmenin kurulmasından sonra düzenlenir',
            'E': 'Faturaya itiraz için otuz günlük bir süre öngörülmüştür',
        },
        'E',
        'TTK md. 21: faturayı alan kişi aldığı tarihten itibaren SEKİZ GÜN içinde içeriği hakkında itirazda bulunmazsa içeriği kabul etmiş sayılır. Aynı süre teyit mektupları için de geçerlidir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0012': patch(
        'Ticari işletme ve tacir ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Ticari işletme bir bütün hâlinde devredilebilir. II. Bir ticari işletmeyi kısmen de olsa kendi adına işleten gerçek kişi tacirdir. III. Belediyeler işlettikleri ticari işletmeler nedeniyle tacir sayılır.',
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'B',
        'I doğrudur (TTK md. 11/3). II doğrudur (md. 12). III YANLIŞTIR: md. 16/2 uyarınca belediye ve diğer kamu tüzel kişileri TACİR SAYILMAZ; yalnızca işlettikleri işletmelere ticari hükümler uygulanır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0013': patch(
        'Ticari işletme ve tacir ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Esnaf, ticari işletme işleten kişidir. II. Küçüğe ait işletmede tacir sıfatı küçüğe aittir. III. Ticari işletme rehni zilyetliğin devrini gerektirir. IV. Cari hesap sözleşmesi yazılı yapılmadıkça geçerli olmaz.',
        {
            'A': 'I ve III',
            'B': 'I, III ve IV',
            'C': 'Yalnız I',
            'D': 'II ve IV',
            'E': 'I ve II',
        },
        'A',
        'I YANLIŞ: TTK md. 15 uyarınca esnafın faaliyeti sermayesinden çok bedeni çalışmasına dayanır ve geliri sınırı aşmaz; ticari işletme işletmez. III YANLIŞ: ticari işletme rehni zilyetlik devredilmeksizin sicile tescille kurulur. II (md. 13) ve IV (md. 90) doğrudur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0014': patch(
        'Bir ticari işletmeyi kısmen de olsa kendi adına işleten gerçek kişinin sıfatı aşağıdakilerden hangisidir?',
        {
            'A': 'Komisyoncu',
            'B': 'Acente',
            'C': 'Ticari temsilci',
            'D': 'Tacir',
            'E': 'Esnaf',
        },
        'D',
        'TTK md. 12: bir ticari işletmeyi, kısmen de olsa kendi adına işleten kişiye TACİR denir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0015': patch(
        'Faturayı alan kişinin içeriğine itiraz edebileceği süre aşağıdakilerden hangisidir?',
        {
            'A': 'Üç gün',
            'B': 'Üç ay',
            'C': 'Sekiz gün',
            'D': 'On beş gün',
            'E': 'Bir ay',
        },
        'C',
        'TTK md. 21/2: faturayı alan kişi, aldığı tarihten itibaren SEKİZ GÜN içinde içeriği hakkında itirazda bulunmamışsa faturanın içeriğini kabul etmiş sayılır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0016': patch(
        'Bir tacirin ticari işletmesine ilişkin borçlarından dolayı iflasa tabi olup olmadığı sorulmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tacir, ticari olsun olmasın her türlü borcu için iflasa tabidir',
            'B': 'İflasa tabi olmak ticaret siciline kayıtlı tacirlere özgüdür',
            'C': 'İflasa tabiiyet tüzel kişi tacirler için söz konusudur',
            'D': 'Tacir ticari borçları için iflasa tabidir, diğer borçları için değildir',
            'E': 'Tacir borçları için iflasa tabi değildir',
        },
        'A',
        'TTK md. 18/1: tacir, her türlü borcu için İFLASA TABİDİR. Borcun ticari olup olmaması ya da tacirin gerçek veya tüzel kişi olması sonucu değiştirmez.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0017': patch(
        'Ticari hükümlerle düzenlenmemiş bir konuda hâkimin başvuracağı kaynak sırası bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Uyuşmazlık hakkında karar verilemez',
            'B': 'Hâkim, kanundaki kaynak sırasıyla bağlı olmaksızın uygulanacak kuralı belirler',
            'C': 'Önce ticari örf ve âdete, bulunmazsa genel hükümlere başvurulur',
            'D': 'Doğrudan genel hükümlere başvurulur',
            'E': 'Ticari örf ve âdet uygulanır, genel hükümlere gidilmez',
        },
        'C',
        'TTK md. 1 ve 2: ticari hükümlerle düzenlenmemiş konularda TİCARİ ÖRF VE ÂDETE, bu da yoksa genel hükümlere göre karar verilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0018': patch(
        'Küçük ve kısıtlılara ait ticari işletmeler bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yasal temsilci, işletmenin sahibi olmadığı için tacir sayılmaz',
            'B': 'İşletmeyi küçük adına işleten yasal temsilci tacir sıfatını kazanır',
            'C': 'Tacir sıfatı temsil edilen küçüğe aittir',
            'D': 'Ceza ve disiplin sorumlulukları yasal temsilciye aittir',
            'E': 'Küçük, ergin olduğunda tacir sıfatını sürdürebilir',
        },
        'B',
        'TTK md. 13: küçük ve kısıtlılara ait ticari işletmeyi bunların adına işleten yasal temsilci, işletmenin sahibi olmadığı için TACİR SAYILMAZ; tacir sıfatı temsil edilene aittir. Ceza ve disiplin sorumlulukları ise temsilciye yüklenmiştir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0019': patch(
        'Bir tacirin tescilli ticaret unvanı, başka bir kişi tarafından izinsiz kullanılmaktadır. Buna göre ticaret unvanının korunması bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Hak sahibi haksız kullanımın tespitini isteyebilir',
            'B': 'Hak sahibi, haksız kullanımın önlenmesini ve unvanın sicilden silinmesini isteyebilir',
            'C': 'Koşulları varsa maddi ve manevi tazminat istenebilir',
            'D': 'Tescilli ticaret unvanı kanunen korunur',
            'E': 'Ticaret unvanının korunabilmesi için ayrıca marka olarak tescil edilmesi gerekir',
        },
        'E',
        'TTK md. 52: ticaret unvanı kanuna aykırı olarak başkası tarafından kullanılırsa hak sahibi tespit, önleme, silme ve koşulları varsa maddi-manevi tazminat isteyebilir. Koruma TESCİLDEN doğar; ayrı bir marka tescili koşul değildir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0020': patch(
        'Fatura, teyit mektubu ve ticari örf ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Faturaya sekiz gün içinde itiraz edilmezse içeriği kabul edilmiş sayılır. II. Teyit mektubuna sekiz gün içinde itiraz edilmezse içeriği kabul edilmiş sayılır. III. Ticari hükümlerle düzenlenmemiş konularda önce genel hükümlere başvurulur.',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'Yalnız I',
            'D': 'I ve III',
            'E': 'II ve III',
        },
        'A',
        'I ve II doğrudur (TTK md. 21). III YANLIŞTIR: md. 1 ve 2 uyarınca önce TİCARİ ÖRF VE ÂDETE, bulunmazsa genel hükümlere başvurulur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0021': patch(
        'Bir kişi, ticari işletmesini kurup açtığını gazete ilanıyla duyurmuş ve ticaret siciline kaydettirmiş; ancak henüz fiilen faaliyete başlamamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tacir sıfatı için ilk faturanın düzenlenmesi gerekir',
            'B': 'Kişi ancak fiilen faaliyete başladığında tacir sayılır',
            'C': 'Tacir sıfatı ancak sicile kayıtla doğar; ilanın bir sonucu yoktur',
            'D': 'Kişi, işletmeyi fiilen işletmeye başlasa dahi tacir sayılmaz',
            'E': 'Kişi, işletmeyi fiilen işletmese de tacir sayılır',
        },
        'E',
        'TTK md. 12/2: bir ticari işletmeyi kurup açtığını, sirküler, gazete, radyo, televizyon ve diğer ilan araçlarıyla halka bildirmiş veya işletmesini ticaret siciline tescil ettirerek durumu ilan etmiş olan kimse, fiilen işletmeye başlamamış olsa bile TACİR SAYILIR.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0022': patch(
        'Bir belediye kendi tüzel kişiliği altında bir ticari işletme işletmektedir. Ayrıca bir ticaret şirketi ve amacına ulaşmak için ticari işletme işleten bir dernek bulunmaktadır. Buna göre tacir sıfatı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Belediye tacirdir; ticaret şirketi ve dernek tacir sayılmaz',
            'B': 'Üçü de tacirdir',
            'C': 'Şirket ve dernek tacirdir; belediye değildir, ancak işletmesine ticari hükümler uygulanır',
            'D': 'Üçü de tacir sayılmaz',
            'E': 'Ticaret şirketleri tacirdir; amacına varmak için ticari işletme işleten dernek ile belediye ise tacir sayılmaz',
        },
        'C',
        'TTK md. 16: ticaret şirketleri ile amacına varmak için ticari bir işletme işleten dernekler ve kendi kuruluş kanunları gereğince özel hukuk hükümleri dairesinde yönetilmek üzere kurulan kamu tüzel kişileri tacir sayılır. md. 16/2: DEVLET, il özel idaresi, BELEDİYE, köy ve diğer kamu tüzel kişileri ile kamuya yararlı dernekler TACİR SAYILMAZ; ancak işlettikleri ticari işletmelere ticari hükümler uygulanır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0023': patch(
        'Bir tacir, kendisine 3 Mart günü teslim edilen faturanın içeriğine 20 Mart günü itiraz etmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Fatura sekiz gün içinde itiraz edilmediğinden içeriği kabul edilmiş sayılır',
            'B': 'İtiraz süresi on beş gün olup itiraz süresindedir',
            'C': 'Faturaya itiraz süresi bir ay olarak öngörüldüğünden yapılan itiraz süresinde sayılır',
            'D': 'Fatura içeriği ancak yazılı kabulle bağlayıcı olur',
            'E': 'Faturaya itiraz için süre öngörülmemiştir',
        },
        'A',
        "TTK md. 21/2: bir faturayı alan kişi, aldığı tarihten itibaren SEKİZ GÜN içinde faturanın içeriği hakkında bir itirazda bulunmamışsa bu içeriği KABUL ETMİŞ SAYILIR. 3 Mart'ta alınan faturaya 20 Mart'ta yapılan itiraz süresinde değildir.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0024': patch(
        'Ticari nitelikteki bir uyuşmazlığın hangi mahkemede görüleceği tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ticari davalar için özel bir görevli mahkeme öngörülmemiştir',
            'B': 'Ticari davalar kural olarak asliye ticaret mahkemesinde görülür',
            'C': 'Ticari davalar tahkim kurullarında görülür',
            'D': 'Ticari davalar idare mahkemesinde görülür',
            'E': 'Ticari davalar sulh hukuk mahkemesinde görülür',
        },
        'B',
        'TTK md. 4-5: bu Kanunda öngörülen hususlardan doğan hukuk davaları ile sayılan diğer davalar TİCARİ DAVA sayılır ve aksine hüküm bulunmadıkça ASLİYE TİCARET MAHKEMESİNDE görülür. Asliye ticaret mahkemesi bulunmayan yerlerde bu davalara asliye hukuk mahkemesi bakar.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0025': patch(
        'Bir tacir, ticari defterlerini tutmakta ancak açılış ve kapanış onaylarını yaptırmamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Elektronik ortamda tutulan defterler için onay aranmaz',
            'B': 'Defterlerin onaylanması tacirin tercihine bırakılmıştır',
            'C': 'Kapanış onayı zorunlu olup açılış onayı aranmaz',
            'D': 'Defterler kanuni onaylara tabidir; onaysız defter usulüne uygun sayılmaz',
            'E': 'Açılış ve kapanış onayı tüzel kişi tacirlere özgü olup gerçek kişi tacirleri bağlamaz',
        },
        'D',
        'TTK md. 64: fiziki ortamda tutulan yevmiye defteri, defterikebir ve envanter defteri ile ilgili diğer defterlerin AÇILIŞ onayları kuruluş sırasında ve her faaliyet dönemi başında, KAPANIŞ onayları ise kanunda belirtilen sürelerde yapılır. Onaylar zorunludur ve tüm tacirleri bağlar.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0026': patch(
        'Bir anonim şirketin tutmakla yükümlü olduğu defterler belirlenmektedir. Buna göre aşağıdakilerden hangisi bu defterlerden biri değildir?',
        {
            'A': 'Personel özlük defteri',
            'B': 'Yevmiye defteri',
            'C': 'Defterikebir',
            'D': 'Pay defteri, yönetim kurulu karar defteri ve genel kurul toplantı ve müzakere defteri',
            'E': 'Envanter defteri',
        },
        'A',
        'TTK md. 64: her tacir yevmiye defteri, defterikebir ve envanter defterini tutar. Anonim şirketler ayrıca PAY DEFTERİ, YÖNETİM KURULU KARAR DEFTERİ ile GENEL KURUL TOPLANTI VE MÜZAKERE DEFTERİNİ tutar. Personel özlük dosyası iş mevzuatına ilişkindir; ticari defter değildir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0027': patch(
        'Bir uyuşmazlıkta tacirin ticari defterlerinin delil olarak kullanılması gündeme gelmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ticari defterler sahibi lehine delil olamaz, aleyhine olabilir',
            'B': 'Ticari defterler kesin delil sayılır ve mahkemeyi bağlar',
            'C': 'Ticari defterler, usulüne uygun tutulmuş olsa dahi uyuşmazlıklarda delil olarak dikkate alınamaz',
            'D': 'Ticari defterlerin delil değeri tacir olmayanlarla uyuşmazlıklarda doğar',
            'E': 'Koşullar gerçekleşirse sahibi lehine de delil olabilir',
        },
        'E',
        'Ticari defterlerin ispat gücü, usul hukuku ve TTK hükümleri çerçevesinde belirlenir: usulüne uygun tutulan defterler sahibi ALEYHİNE delil olabileceği gibi, kanunda öngörülen koşullar gerçekleştiğinde LEHİNE de delil oluşturabilir. Defterler kesin delil değildir; mahkemenin değerlendirmesine tabidir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0028': patch(
        'Bir tacir, işletmesini tanıtmak için ticaret unvanından farklı bir ad kullanmak istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşletme adı tüzel kişi tacirlere özgüdür',
            'B': 'İşletme adı ticaret unvanının yerine geçer',
            'C': 'İşletme adı kullanılamaz; işletmenin tanıtımı ticaret unvanıyla yapılır',
            'D': 'Kullanabilir; işletme adı da sicile tescil ve ilan edilir',
            'E': 'İşletme adı kullanılabilir ancak tescili gerekmez',
        },
        'D',
        'TTK md. 53: işletme sahibi ile ilgili olmaksızın doğrudan doğruya işletmeyi tanıtmak ve benzer işletmelerden ayırt etmek için kullanılan adların da tescili zorunludur. İşletme adı ticaret unvanının yerine geçmez; ikisi birlikte kullanılır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0029': patch(
        'Bir tacir adına, ticari işletmeyi yönetme ve işletmeye ilişkin işlemleri yapma konusunda geniş yetkiyle donatılmış bir kişi görevlendirilmiştir. Bir diğeri ise yalnızca belirli işlerde yetkilendirilmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Her ikisi de tacir sıfatını kazanır',
            'B': 'Her ikisi de acente sayılır',
            'C': 'Birincisi ticari temsilci, ikincisi ticari vekildir',
            'D': 'Her ikisi de pazarlamacı sayılır',
            'E': 'Birincisi ticari vekil, ikincisi ticari temsilcidir',
        },
        'C',
        'TBK md. 547 vd.: TİCARİ TEMSİLCİ, işletme sahibinin işletmeyi yönetme ve işletmeyle ilgili işlemlerde ticaret unvanı altında temsil yetkisi verdiği kişidir. TİCARİ VEKİL ise temsilci sıfatı olmaksızın işletmenin bütün işleri veya belirli bazı işleri için yetkilendirilen kişidir. Tacir yardımcıları bu sıfatla tacir olmaz.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0030': patch(
        'Bir tacir, ticari işletmesini bir bütün hâlinde devretmek istemekte; devrin kapsamını ve şeklini belirlemeye çalışmaktadır. Buna göre ticari işletme kavramı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Faaliyetin devamlı ve bağımsız biçimde yürütülmesi aranır',
            'B': 'Ticari işletme, unsurları ayrı ayrı devredilmedikçe elden çıkarılamaz',
            'C': 'Ticari işletme bir bütün hâlinde devredilebilir',
            'D': 'Ticari işletme, esnaf işletmesi sınırını aşan düzeyde gelir hedefleyen işletmedir',
            'E': 'Devir sözleşmesi yazılı yapılır ve sicile tescil edilir',
        },
        'B',
        'TTK md. 11: ticari işletme, unsurlarının devri için zorunlu tasarruf işlemlerinin ayrı ayrı yapılmasına gerek olmaksızın BİR BÜTÜN hâlinde devredilebilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0031': patch(
        'İki kişi, yalnızca biri için ticari nitelik taşıyan bir iş dolayısıyla birlikte borç altına girmiş; faiz oranı da kararlaştırılmamıştır. Buna göre ticari işlerde faiz ve teselsül bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Faiz oranı belirlenmemişse kanuni faiz uygulanır',
            'B': 'Bileşik faiz kanunda sayılan hâllerde mümkündür',
            'C': 'Aksi kararlaştırılmadıkça ticari işlerde borçlular müteselsilen sorumludur',
            'D': 'Ticari işlerde borçlular arasında müteselsil sorumluluk karinesi bulunmaz',
            'E': 'Ticari işlerde faiz oranını kural olarak taraflar belirler',
        },
        'D',
        'TTK md. 7: iki veya daha fazla kişi, içlerinden yalnız biri veya hepsi için ticari nitelikte bir iş dolayısıyla borç altına girerse, aksi öngörülmedikçe MÜTESELSİLEN sorumlu olur. Ticari işlerde teselsül KARİNESİ vardır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0032': patch(
        'Bir tacir, tutacağı defterleri ve bunların ispat gücünü belirlemeye çalışmaktadır. Buna göre ticari defterler bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Her tacir yevmiye defteri, defterikebir ve envanter defteri tutar',
            'B': 'Ticari defterler sahibi lehine delil oluşturamaz',
            'C': 'Anonim şirketler ayrıca pay defteri ve karar defteri tutar',
            'D': 'Defterler ve dayanak belgeler kanunda öngörülen süre boyunca saklanır',
            'E': 'Defterlerin açılış ve kapanış onayları kanunda düzenlenmiştir',
        },
        'B',
        'Usulüne uygun tutulan ticari defterler sahibi ALEYHİNE delil oluşturabileceği gibi, kanunda öngörülen koşullar gerçekleştiğinde LEHİNE de delil oluşturabilir; değerlendirme mahkemeye aittir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0033': patch(
        'Bir kişi, esnaf işletmesi için öngörülen sınırı aşan düzeyde gelir hedefleyen ve devamlı biçimde yürütülen bir işletme kurmuştur. Buna göre bu işletme aşağıdakilerden hangisidir?',
        {
            'A': 'Kamu işletmesi',
            'B': 'Serbest meslek işletmesi',
            'C': 'Esnaf işletmesi',
            'D': 'Adi ortaklık',
            'E': 'Ticari işletme',
        },
        'E',
        'TTK md. 11: ticari işletme, esnaf işletmesi için öngörülen sınırı aşan düzeyde gelir sağlamayı hedef tutan faaliyetlerin devamlı ve bağımsız şekilde yürütüldüğü işletmedir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0034': patch(
        'Bir tacirin ticari işletmesine ilişkin işlemleri altında yaptığı ad aşağıdakilerden hangisidir?',
        {
            'A': 'Ticaret unvanı',
            'B': 'Ticari isim',
            'C': 'Tescilli tasarım',
            'D': 'Marka',
            'E': 'İşletme adı',
        },
        'A',
        'TTK md. 39: her tacir, ticari işletmesine ilişkin işlemleri TİCARET UNVANIYLA yapmak ve belgeleri bu unvan altında imzalamak zorundadır. İşletme adı ise işletmeyi tanıtmaya yarar.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0035': patch(
        'Bir tacir, ticari işletmesini ticaret siciline tescil ettirmemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ticaret siciline tescil ettirilmemiş bir işletmeyi kendi adına işleten kişi tacir sıfatını kazanmaz',
            'B': 'Tescil tüzel kişi tacirler için zorunlu, gerçek kişiler için isteğe bağlıdır',
            'C': 'Tacir sıfatı işletmenin işletilmesiyle doğar; tescil etmemek bunu kaldırmaz',
            'D': 'Tescil edilmeyen işletme için tacir yükümlülükleri doğmaz',
            'E': 'Tescil, tacir sıfatının kurucu unsurudur',
        },
        'C',
        'TTK md. 12: tacir sıfatı, bir ticari işletmenin kısmen de olsa kendi adına işletilmesiyle doğar; tescil BİLDİRİCİ etkilidir. Tescil ettirmemek tacir sıfatını kaldırmaz, aksine md. 18 uyarınca yükümlülüklere aykırılık oluşturur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0036': patch(
        'Bir şubenin hukuki durumu tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Şube ayrı bir tüzel kişilik kazanır',
            'B': 'Şube, merkezden bağımsız kendi ticaret unvanını seçip kullanabilir',
            'C': 'Şube vergi dairesine bildirilir, tescil edilmez',
            'D': 'Şube ayrı tüzel kişi değildir; bulunduğu yerde tescil edilir',
            'E': 'Şubenin tescili gerekmez',
        },
        'D',
        'TTK md. 40 ve 48: şubeler bulundukları yerin ticaret siciline tescil ve ilan olunur; şubenin unvanı merkezin unvanına şube olduğunu gösteren ek yapılarak oluşturulur. Şubenin AYRI TÜZEL KİŞİLİĞİ YOKTUR.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0037': patch(
        'Bir tacirin ticari işletmesini devrettiği durumda devrin kapsamı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Devir, aksi kararlaştırılmadıkça duran malvarlığıyla sınırlıdır, işletme değerini kapsamaz',
            'B': 'Ticari işletme bir bütün hâlinde devredilebilir',
            'C': 'Aksi öngörülmemişse devir işletme değerini de kapsar',
            'D': 'Aksi öngörülmemişse devir kiracılık hakkını da kapsar',
            'E': 'Devir sözleşmesi yazılı yapılır ve ticaret siciline tescil ile ilan edilir',
        },
        'A',
        'TTK md. 11/3: aksi öngörülmemişse devir sözleşmesi duran malvarlığını, İŞLETME DEĞERİNİ, KİRACILIK HAKKINI, ticaret unvanı ile diğer fikri mülkiyet haklarını ve sürekli olarak işletmeye özgülenen malvarlığı unsurlarını içerir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0038': patch(
        'Bir işletmede ticari temsilci, ticari vekil ve acente birlikte görev yapmaktadır. Buna göre tacir yardımcıları bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Acente, bağımsız bir tacir yardımcısıdır',
            'B': 'Ticari vekil, temsilci sıfatı olmaksızın belirli işler için yetkilendirilir',
            'C': 'Ticari temsilci ve ticari vekil, bu sıfatları nedeniyle tacir sayılır',
            'D': 'Ticari temsilci işletmeyi yönetme ve temsil yetkisiyle donatılmıştır',
            'E': 'Tacir yardımcılarının yetkileri kapsam bakımından farklılaşır',
        },
        'C',
        'Tacir yardımcıları (TBK md. 547 vd. ve TTK md. 102 vd.) işletme sahibi adına iş görür; bu sıfatları TACİR OLMALARINI SAĞLAMAZ. Tacir sıfatı, işletmeyi kendi adına işletene aittir (TTK md. 12). Acente ise kendi ticari işletmesi bulunan bağımsız bir yardımcıdır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0039': patch(
        'Ticari işletme ve tacir ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Tacir her türlü borcu için iflasa tabidir. II. Tacir ticari defter tutmakla yükümlüdür. III. Esnaf ticari işletme işletir.',
        {
            'A': 'I, II ve III',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'I ve III',
            'E': 'Yalnız I',
        },
        'B',
        'I ve II doğrudur (TTK md. 18). III YANLIŞTIR: md. 15 uyarınca esnafın faaliyeti sermayesinden çok bedeni çalışmasına dayanır ve geliri sınırı aşmaz; ticari işletme işletmez.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0040': patch(
        'Ticari işletme, tacir ve ticari iş ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Ticari işletme bir bütün hâlinde devredilebilir. II. Belediyeler işlettikleri ticari işletmeler nedeniyle tacir sayılır. III. Ticari işlerde faiz oranı kanunla sabitlenmiş olup değiştirilemez. IV. Tacir basiretli bir iş adamı gibi hareket etmelidir.',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız II',
            'C': 'II ve III',
            'D': 'III ve IV',
            'E': 'I ve IV',
        },
        'C',
        'II YANLIŞ: TTK md. 16/2 uyarınca belediye ve diğer kamu tüzel kişileri TACİR SAYILMAZ; yalnız işlettikleri işletmelere ticari hükümler uygulanır. III YANLIŞ: md. 8-9 uyarınca ticari işlerde faiz oranı kural olarak SERBESTÇE belirlenir. I (md. 11/3) ve IV (md. 18/2) doğrudur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0041': patch(
        'Bir ticari işletme, on beş yaşındaki bir çocuğa miras yoluyla geçmiş ve işletme vasi tarafından çocuk adına işletilmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Küçük tacir sayılır ve işletmeden doğan ceza ile disiplin sorumluluğu da bizzat kendisine aittir',
            'B': 'Küçük tacir sayılır; ceza ve disiplin sorumluluğu kanuni temsilcidedir',
            'C': 'Ne küçük ne vasi tacir sayılır; işletme tacirsiz işletilir',
            'D': 'Küçük ancak ergin olduğunda tacir sıfatını kazanır',
            'E': 'Küçük tacir sayılmaz; tacir sıfatı vasiye aittir',
        },
        'B',
        'TTK md. 13: küçük ve kısıtlılara ait ticari işletmeyi bunların adına işleten yasal temsilci, ticari işletmenin sahibi olmadığı hâlde tacir sayılmaz; TACİR SIFATI temsil edilene aittir. Ancak ceza ve disiplin sorumlulukları bakımından yasal temsilci sorumlu olur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0042': patch(
        'Bir tacir; iflasa tabi olmadığını, ticari defter tutma yükümlülüğü bulunmadığını ve ticaret unvanı seçmek zorunda olmadığını ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Üç iddia da yanlıştır',
            'B': 'Defter tutma yükümlülüğünün bulunmadığı iddiası doğru, diğerleri yanlıştır',
            'C': 'Unvan seçme zorunluluğunun bulunmadığı iddiası doğru, diğerleri yanlıştır',
            'D': 'Üç iddia da doğrudur; sayılan yükümlülükler tüzel kişi tacirlere özgüdür',
            'E': 'İflasa tabi olmama iddiası doğru, diğer ikisi yanlıştır',
        },
        'A',
        'TTK md. 18: tacir, her türlü borcu için İFLASA TABİDİR; ayrıca kanun hükümleri uyarınca bir TİCARET UNVANI seçmek, işletmesini ticaret siciline TESCİL ettirmek ve bu Kanun hükümlerince gerekli TİCARİ DEFTERLERİ tutmakla yükümlüdür. Yükümlülükler gerçek ve tüzel kişi tacirlerin tamamını kapsar.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0043': patch(
        'İki kişi, yalnızca biri için ticari nitelik taşıyan bir iş dolayısıyla birlikte borç altına girmiş; sözleşmede sorumluluk biçimi düzenlenmemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sorumluluk biçimi mahkemece takdir edilir',
            'B': 'Ticari işlerde müteselsil sorumluluk karinesi bulunmaz',
            'C': 'Borçlular eşit paylarla sorumlu olur',
            'D': 'Müteselsil sorumluluk için işin alacaklı bakımından da ticari olması gerekir',
            'E': 'Aksi kararlaştırılmadıkça borçlular müteselsilen sorumlu olur',
        },
        'E',
        'TTK md. 7: iki veya daha fazla kişi, içlerinden yalnız biri veya hepsi için ticari nitelikte bir iş dolayısıyla diğer bir kimseye karşı birlikte borç altına girerse, kanunda veya sözleşmede aksi öngörülmemişse MÜTESELSİLEN sorumlu olur. Karine ticari işlerde geçerlidir; işin her iki taraf için ticari olması şart değildir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0044': patch(
        'Bir tacir, ticari işletmesiyle ilgili bir ödünç sözleşmesinde faiz oranını serbestçe belirlemek istemektedir. Buna göre ticari işlerde faiz bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Faiz oranı kararlaştırılmamışsa kanuni faiz uygulanır',
            'B': 'Temerrüt faizi ticari işlerde ayrıca düzenlenmiştir',
            'C': 'Ticari işlerde faiz oranı kanunla sabitlenmiş olup taraflarca değiştirilemez',
            'D': 'Bileşik faiz yürütülmesi kanunda sayılan sınırlı hâllerde mümkündür',
            'E': 'Ticari işlerde faiz oranını kural olarak taraflar kararlaştırabilir',
        },
        'C',
        'TTK md. 8-9: ticari işlerde faiz oranı SERBESTÇE belirlenir; belirlenmemişse kanuni faiz uygulanır. md. 8/2: bileşik faiz (faize faiz yürütülmesi) yalnızca cari hesap sözleşmeleri ile her iki taraf için de ticari iş niteliğinde olan ödünç sözleşmelerinde ve kanunda öngörülen koşullarla mümkündür.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0045': patch(
        'Ticaret sicilinin niteliği ve etkileri tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tescili gerekirken tescil edilmemiş hususlar iyiniyetli üçüncü kişilere karşı ileri sürülemez',
            'B': 'Ticaret sicili alenidir',
            'C': 'Sicil kayıtlarının tutulmasından doğan zarardan sorumluluk düzenlenmiştir',
            'D': 'Ticaret sicili kayıtları gizlidir; üçüncü kişiler bu kayıtları inceleyemez',
            'E': 'Tescil ve ilan edilen hususlar, iyiniyetli olsun olmasın üçüncü kişilere karşı ileri sürülebilir',
        },
        'D',
        'TTK md. 35 vd.: ticaret sicili ALENİDİR; herkes sicilin içeriğini ve belgeleri inceleyebilir, onaylı suret isteyebilir. md. 36: tescil ve ilan edilen hususlar üçüncü kişilere karşı ileri sürülebilirken, tescili gerekirken tescil edilmemiş hususlar iyiniyetli üçüncü kişilere karşı ileri sürülemez.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0046': patch(
        'Bir tacir, ticari işletmesiyle ilgili olarak başka bir tacire verdiği hizmet için ücret kararlaştırılmadığını, bu nedenle ücret isteyemeyeceğini düşünmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ücret isteme hakkı tüzel kişi tacirlere özgüdür',
            'B': 'Tacir uygun bir ücret ve faiz isteyebilir',
            'C': 'Ücret ancak yazılı sözleşme varsa istenebilir',
            'D': 'Tacir yaptığı giderleri ve avansları isteyebilir; gördüğü iş veya hizmet için ayrıca ücret talep edemez',
            'E': 'Ücret kararlaştırılmamışsa tacir ücret ve faiz talep edemez',
        },
        'B',
        'TTK md. 20: tacir olan veya olmayan bir kişiye, ticari işletmesiyle ilgili bir iş veya hizmet görmüş olan tacir, uygun bir ÜCRET isteyebilir; ayrıca verdiği avanslar ve yaptığı giderler için ödeme tarihinden itibaren FAİZ isteyebilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0047': patch(
        "Bir uyuşmazlıkta uygulanacak hükümler tartışılmaktadır: TTK'da özel bir hüküm yoktur, ancak ticari örf ve âdet ile genel hükümler gündeme gelmiştir. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Ticari örf ve âdet uygulanır; bulunmadığı hâllerde de genel hükümlere gidilemez',
            'B': 'Doğrudan genel hükümlere gidilir; ticari örf ve âdet uygulanmaz',
            'C': 'Hâkim, uygulanacak kuralı kaynak sırası gözetmeden seçer',
            'D': 'Uyuşmazlık hakkında karar verilemez',
            'E': 'Önce ticari örf ve âdete, yoksa genel hükümlere başvurulur',
        },
        'E',
        'TTK md. 1 ve 2: ticari hükümlerle düzenlenmemiş konularda TİCARİ ÖRF VE ÂDETE, bu da yoksa genel hükümlere göre karar verilir. Ticari örf ve âdet, ancak tacirler arasında ya da bir bölgede yerleşmişse uygulanır; bunu bilmeyenlere karşı da uygulanabilmesi için tacir olmaları gerekir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0048': patch(
        'Bir tacir, ticari defterlerini ve belgelerini bir yıl sonra imha etmeyi planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Saklama süresi TTK'da değil vergi mevzuatında düzenlenmiştir",
            'B': 'Defterler hesap dönemi kapandıktan sonra derhâl imha edilebilir',
            'C': 'Kanuni süre boyunca saklanır; bir yıl sonra imha edilemez',
            'D': 'Defter ve belgeleri saklama yükümlülüğü tüzel kişi tacirlere özgüdür',
            'E': 'Defterlerin saklanması tacirin tercihine bırakılmıştır',
        },
        'C',
        'TTK md. 82: her tacir; tutmakla yükümlü olduğu ticari defterleri ve bu defterlere yapılan kayıtların dayandığı belgeleri kanunda öngörülen süre boyunca SAKLAMAKLA yükümlüdür. Yükümlülük tüm tacirleri bağlar; vergi mevzuatındaki saklama süreleri ayrıca uygulanır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0049': patch(
        'İki tacir, karşılıklı alacaklarını tek tek istemeyip belirli dönemlerde bakiyeyi talep etmek üzere anlaşmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Cari hesap sözleşmesi ancak bir bankayla kurulabilir',
            'B': 'Cari hesapta taraflar alacaklarını dönem beklemeden tek tek isteyebilir',
            'C': 'Cari hesap sözleşmesi ticaret siciline tescil ve ilan edilmedikçe geçersiz sayılır',
            'D': 'Cari hesap sözleşmesi kurulmuştur; sözleşmenin yazılı yapılması geçerlilik koşuludur',
            'E': 'Cari hesap sözleşmesi sözlü olarak da geçerli biçimde kurulabilir',
        },
        'D',
        'TTK md. 89: iki kişinin herhangi bir hukuki sebep veya ilişkiden doğan alacaklarını teker teker ve ayrı ayrı istemekten karşılıklı olarak vazgeçip bunları kalem kalem alacak ve borç şekline çevirerek hesabın kesilmesinden sonra çıkacak bakiyeyi isteyebileceklerine ilişkin sözleşme CARİ HESAP sözleşmesidir. md. 90: sözleşme YAZILI yapılmadıkça geçerli olmaz.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0050': patch(
        'Bir tacir, iflasa tabi olmadığını ve ticari işletmesiyle ilgili faaliyetlerinde ortalama bir kişinin özenini göstermenin yeterli olduğunu ileri sürmektedir. Buna göre tacir olmanın hükümleri bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tacir, ticari işletmesiyle ilgili faaliyetlerinde ortalama bir kişinin özenini göstermekle yeterli sayılır',
            'B': 'Tacir, kanun hükümleri uyarınca bir ticaret unvanı seçmek ve tüm işlemlerinde bu unvanı kullanmakla yükümlüdür',
            'C': 'Tacir basiretli bir iş adamı gibi hareket etmelidir',
            'D': 'Tacir her türlü borcu için iflasa tabidir',
            'E': 'Tacir ticari defter tutmakla yükümlüdür',
        },
        'A',
        'TTK md. 18/2: her tacirin ticaretine ait bütün faaliyetlerinde BASİRETLİ BİR İŞ ADAMI GİBİ hareket etmesi gerekir; bu, ortalama bir kişiden beklenenden ağır bir özen ölçüsüdür.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0051': patch(
        'Bir tacir, işletmesini ticaret siciline tescil ettirmiş ancak ticaret unvanını işletmesinde görünür biçimde yazmamıştır. Buna göre ticaret sicili ve ticaret unvanı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tescil ve ilan edilen hususlar, iyiniyetli olsun olmasın üçüncü kişilere karşı ileri sürülebilir',
            'B': 'Ticaret sicili gizlidir; kayıtları ilgili taraflar inceleyebilir',
            'C': 'Ticaret sicili alenidir',
            'D': 'Tescilli ticaret unvanı kanunen korunur',
            'E': 'Tacir işlemlerini ticaret unvanıyla yapar',
        },
        'B',
        'TTK md. 35 vd.: ticaret sicili ALENİDİR; herkes sicil kayıtlarını inceleyebilir ve onaylı suret isteyebilir. Aleniyet, sicile bağlanan hukuki sonuçların temelidir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0052': patch(
        'Tacir olmanın hükümleri ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Tacir her türlü borcu için iflasa tabidir. II. Tacir basiretli bir iş adamı gibi hareket etmelidir. III. Faturaya itiraz süresi otuz gündür. IV. Ticari işlerde müteselsil sorumluluk karinesi bulunmaz.',
        {
            'A': 'Yalnız III',
            'B': 'I, III ve IV',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'III ve IV',
        },
        'E',
        'III YANLIŞ: TTK md. 21 uyarınca faturaya itiraz süresi SEKİZ GÜNDÜR. IV YANLIŞ: md. 7 ticari işlerde MÜTESELSİL sorumluluk karinesi getirir. I (md. 18) ve II (md. 18/2) doğrudur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0053': patch(
        'Ticaret sicili ve unvan ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Ticaret sicili alenidir. II. Tacir işletmesiyle ilgili işlemleri ticaret unvanıyla yapar. III. Şube bağımsız bir tüzel kişilik kazanır.',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'I ve III',
            'D': 'Yalnız I',
            'E': 'II ve III',
        },
        'A',
        'I doğrudur (TTK md. 35 vd.). II doğrudur (md. 39). III YANLIŞTIR: şubenin ayrı tüzel kişiliği yoktur; merkeze bağlıdır ve unvanı merkezin unvanına ek yapılarak oluşturulur (md. 48).',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0054': patch(
        'Ekonomik faaliyeti sermayesinden çok bedeni çalışmasına dayanan ve geliri kanunda öngörülen sınırı aşmayan kişinin sıfatı aşağıdakilerden hangisidir?',
        {
            'A': 'Pazarlamacı',
            'B': 'Esnaf',
            'C': 'Tacir',
            'D': 'Simsar',
            'E': 'Ticari vekil',
        },
        'B',
        'TTK md. 15: ekonomik faaliyeti sermayesinden fazla bedeni çalışmasına dayanan ve geliri belirlenen sınırı aşmayan kişi ESNAFTIR; ticari işletme işletmez.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0055': patch(
        'Bir tacir, ticari işletmesiyle ilgili bir uyuşmazlıkta hangi mahkemeye başvuracağını araştırmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ticari davalar sulh hukuk mahkemesinde görülür',
            'B': 'Ticari davalar için görevli mahkemeyi taraflar sözleşmeyle belirler',
            'C': 'Ticari davalar icra mahkemesinde görülür',
            'D': 'Ticari davalar kural olarak asliye ticaret mahkemesinde görülür',
            'E': 'Ticari davalar tüketici mahkemesinde görülür',
        },
        'D',
        'TTK md. 4-5: ticari davalar, aksine hüküm bulunmadıkça ASLİYE TİCARET MAHKEMESİNDE görülür; bu mahkemenin bulunmadığı yerlerde davaya asliye hukuk mahkemesi bakar.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0056': patch(
        'Bir tacir, ticari işletmesiyle ilgili verdiği hizmet için ücret ve yaptığı giderler için faiz talep etmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tacir ücret isteyebilir, faiz isteyemez',
            'B': 'Tacir uygun bir ücret ile avans ve giderleri için faiz isteyebilir',
            'C': 'Tacir giderlerini isteyebilir, ücret isteyemez',
            'D': 'Tacir ancak yazılı sözleşme varsa ücret isteyebilir',
            'E': 'Ücret ve faiz talebi, işlemde her iki tarafın da tacir olmasına bağlıdır; aksi hâlde istenemez',
        },
        'B',
        'TTK md. 20: ticari işletmesiyle ilgili bir iş veya hizmet görmüş olan tacir, uygun bir ÜCRET isteyebilir; ayrıca verdiği avanslar ve yaptığı giderler için ödeme tarihinden itibaren FAİZ isteyebilir. Karşı tarafın tacir olması şart değildir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0057': patch(
        'Bir tacir, ticari defterlerinin saklanması yükümlülüğünü sorgulamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Saklama süresi tacirin takdirine bırakılmıştır',
            'B': 'Defterler hesap dönemi kapandığında imha edilebilir',
            'C': "Saklama yükümlülüğü TTK'dan değil vergi mevzuatından doğar",
            'D': 'Ticari defterler ve dayanak belgeler kanunda öngörülen süre boyunca saklanır',
            'E': 'Saklama yükümlülüğü elektronik defterlere özgüdür',
        },
        'D',
        'TTK md. 82: her tacir, tutmakla yükümlü olduğu defterleri ve kayıtların dayandığı belgeleri kanunda öngörülen süre boyunca SAKLAMAKLA yükümlüdür; vergi mevzuatındaki süreler ayrıca uygulanır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0058': patch(
        'İki tacir, karşılıklı alacaklarını tek tek istemeyip dönem sonunda bakiyeyi talep etmek üzere sözlü olarak anlaşmıştır. Buna göre cari hesap sözleşmesi bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Cari hesap sözleşmesi sözlü olarak da geçerli biçimde kurulabilir',
            'B': 'Taraflar alacaklarını tek tek istemekten karşılıklı olarak vazgeçer',
            'C': 'Hesabın kesilmesinden sonra çıkacak bakiye istenebilir',
            'D': 'Cari hesap sözleşmesi bileşik faiz uygulanabilen hâllerdendir',
            'E': 'Sözleşmenin yazılı yapılması gerekir',
        },
        'A',
        'TTK md. 89-90: cari hesap sözleşmesi, tarafların alacaklarını tek tek istemekten vazgeçip bakiyeyi talep etmelerine ilişkindir ve YAZILI yapılmadıkça geçerli olmaz. md. 8/2 uyarınca cari hesap, bileşik faize izin verilen sınırlı hâllerdendir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0059': patch(
        'Bir tacir ile tacir olmayan bir kişi arasında, tacirin işletmesini ilgilendiren bir işlem yapılmıştır. Buna göre ticari iş kavramı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "TTK'da düzenlenen hususlar ticari iştir",
            'B': 'Ticari işlerde faiz oranını kural olarak taraflar belirler',
            'C': 'Bir işlemin ticari iş sayılabilmesi için her iki tarafın da tacir olması gerekir',
            'D': 'Ticari işlerde müteselsil sorumluluk karinesi geçerlidir',
            'E': 'Bir ticari işletmeyi ilgilendiren bütün işlem ve fiiller de ticari iş sayılır',
        },
        'C',
        'TTK md. 3: bu Kanunda düzenlenen hususlarla bir ticari işletmeyi ilgilendiren bütün işlem ve fiiller ticari iştir. Her iki tarafın da tacir olması ARANMAZ; işin bir taraf için ticari olması yeterlidir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0060': patch(
        'Bir tacir, tescili gerektiği hâlde tescil ettirmediği bir hususu iyiniyetli bir üçüncü kişiye karşı ileri sürmek istemektedir. Buna göre ticari defterler ve ticaret sicili bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tescil ve ilan edilen hususlar, iyiniyetli olsun olmasın üçüncü kişilere karşı ileri sürülebilir',
            'B': 'Her tacir yevmiye defteri, defterikebir ve envanter defteri tutar',
            'C': 'Ticaret sicili alenidir',
            'D': 'Ticaret siciline tescil edilmemiş bir husus, iyiniyetli üçüncü kişilere karşı ileri sürülebilir',
            'E': 'Defterlerin açılış ve kapanış onayları kanunda düzenlenmiştir',
        },
        'D',
        'TTK md. 36: tescili gerekirken tescil edilmemiş ya da tescil edilip de ilanı gerekirken ilan edilmemiş hususlar, ancak bunları BİLEN kişilere karşı ileri sürülebilir; İYİNİYETLİ üçüncü kişilere karşı ileri sürülemez.',
        '6102 sayili Turk Ticaret Kanunu',
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
    print(f"1 paket / {len(PATCHES)} soru ('Ticari Isletme ve Tacir' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
