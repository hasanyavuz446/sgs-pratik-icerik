#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Denetim Kavrami — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Kavram agirlikli 60 soru (gercek sinavin denetim blogu da kavram agirlikli, olumsuz kok %52) korunarak onarildi: genisletilmis ELEME_ISARETI olcutune gore 39 mutlak ifadeli sik ayni dogruluk degerini koruyacak bicimde yeniden yazildi, sisirilmis celdiriciler sadelestirildi; gerekce tasiyan 9 dogru sik kisaltildi. Kor ogrenci %36 -> %21.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: BDS 200, 315 · 6102 sayili TTK md. 397 vd. · 660 sayili KHK
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/denetim/denetim_kavrami.json"
STYLE_REF = 'SGS Denetim (olumsuz kök ve öncül ağırlığı 2026 sınav profiline kalibre)'
ONEK = "den-kavram-gen-"


def patch(stem, options, answer, solution, ref='BDS 200 Bagimsiz Denetcinin Genel Amaclari'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Genel kabul görmüş tanıma göre denetim aşağıdakilerden hangisidir?',
        {
            'A': 'İşletmenin günlük ticari işlemlerini fatura ve belgelere dayanarak yevmiye defterine kaydeden, defter-i kebire aktaran ve dönem sonunda mizanla özetleyerek finansal tabloları üreten kayıt tutma işlemi',
            'B': 'Gelecek döneme ilişkin gelir ve giderleri önceden tahmin ederek işletmenin kaynak dağılımını, yatırım ve harcama önceliklerini belirleyen ve hedeflerle karşılaştırma imkânı sağlayan bir bütçeleme süreci',
            'C': 'İşletmenin ürünlerini iç ve dış pazarlarda tanıtarak satış hacmini, cirosunu ve pazar payını artırmayı amaçlayan; reklam, kampanya, dağıtım ve fiyatlandırma kararlarını içeren bir pazarlama ve satış geliştirme faaliyeti',
            'D': 'İktisadi faaliyet ve olaylara ilişkin iddiaların, önceden belirlenmiş ölçütlere uygunluk derecesini araştırmak ve sonuçları ilgili taraflara raporlamak amacıyla tarafsızca kanıt toplayıp değerleyen sistematik bir süreç',
            'E': 'Dönem içinde elde edilen kazanç üzerinden hesaplanan verginin beyanname aracılığıyla vergi dairesine bildirilip tahakkuk ettirilmesi ve yasal süresi içinde ödenmesini kapsayan bir mükellefiyet işlemi',
        },
        'D',
        'Denetim; iktisadi faaliyet ve olaylara ilişkin **iddiaların**, önceden belirlenmiş **ölçütlere uygunluk derecesini** araştırmak ve sonuçları ilgili taraflara **raporlamak** amacıyla **tarafsızca kanıt toplayıp değerleyen sistematik bir süreçtir**.',
        'Denetim - tanım (genel kabul görmüş)',
    ),
    # düzey 2
    '0002': patch(
        "'Bilgi riski' kavramı ile anlatılmak istenen aşağıdakilerden hangisidir?",
        {
            'A': 'Piyasa faiz oranlarındaki değişimin işletmenin borçlanma maliyetini ve faiz giderini artırma olasılığı',
            'B': 'Deprem, yangın ve sel gibi doğal afetlerin işletmenin maddi varlıklarında hasara yol açma olasılığı',
            'C': 'İşletmenin vadesi gelen borçlarını ödeyemeyip faaliyetlerini durdurma ve iflas etme olasılığı',
            'D': 'Döviz kurlarındaki dalgalanmanın işletmenin yabancı para pozisyonunda zarara yol açma olasılığı',
            'E': 'Karar vericiye sunulan bilginin (finansal tabloların) yanlış veya yanıltıcı olma olasılığı',
        },
        'E',
        '**Bilgi riski**, karar vericiye sunulan bilginin (finansal tabloların) **yanlış veya yanıltıcı olma olasılığıdır**. Bağımsız denetim, güvence sağlayarak bu riski azaltır.',
        'Denetim - bilgi riski',
    ),
    # düzey 2
    '0003': patch(
        "Denetimin sağladığı 'makul güvence' ile anlatılmak istenen aşağıdakilerden hangisidir?",
        {
            'A': 'Finansal tabloların kuruşuna kadar doğru olduğunu garanti eden mutlak güvence',
            'B': 'İşletmenin gelecek dönemde kâr edeceğine ve nakit yaratacağına ilişkin verilen teminat',
            'C': 'Tabloların önemli yanlışlık içermediğine dair yüksek ama mutlak olmayan güvence',
            'D': 'Denetçinin görüş bildirmediği ve finansal tablolara güvence vermediği bir çalışma',
            'E': 'İşletmenin gelecekte iflas etmeyeceğine ve faaliyetlerini kesintisiz sürdüreceğine dair verilen kesin bir garanti',
        },
        'C',
        'Denetim **mutlak değil, makul (yüksek ama tam olmayan)** güvence sağlar: finansal tabloların **önemli bir yanlışlık içermediğine** dair makul ölçüde güvence. Denetimin doğal kısıtları nedeniyle mutlak güvence mümkün değildir.',
        'BDS 200 - makul güvence',
    ),
    # düzey 3
    '0004': patch(
        'Denetimin mutlak (kesin) güvence yerine makul güvence sağlamasının nedenlerinden biri DEĞİLDİR?',
        {
            'A': 'Kanıtların çoğunlukla kesin değil ikna edici olması',
            'B': 'Denetçinin tüm işlemleri istisnasız yüzde yüz incelemesi',
            'C': 'Denetimin örnekleme (test) yöntemiyle yapılması',
            'D': 'Muhasebe tahminlerinin doğası gereği belirsizlik içermesi',
            'E': 'İç kontrolün doğal kısıtlarının bulunması',
        },
        'B',
        'Makul güvencenin nedenleri; örnekleme, tahminlerin belirsizliği, iç kontrolün kısıtları ve kanıtların ikna edici (kesin değil) niteliğidir. **Tüm işlemlerin istisnasız %100 incelenmesi** zaten pratikte mümkün değildir ve makul güvencenin nedeni değil, tersidir.',
        'BDS 200 - makul güvence kısıtları',
    ),
    # düzey 2
    '0005': patch(
        "'Uygunluk denetimi' aşağıdakilerden hangisini araştırır?",
        {
            'A': 'Dönem sonunda elde edilen ticari kârın büyüklüğünü ve kârlılık oranlarını',
            'B': 'Rakip işletmelerin uyguladığı satış fiyatı, indirim ve kampanya politikalarını karşılaştırmalı olarak',
            'C': 'Finansal tabloların gerçeğe uygun ve belirlenmiş raporlama çerçevesine uygun biçimde sunulup sunulmadığını ayrıntılıca',
            'D': 'İşletmenin sektör içindeki pazar payını ve rakiplerine göre pazar konumunu ayrıntılı biçimde',
            'E': 'Faaliyetlerin ve işlemlerin belirli kural, yasa, sözleşme veya politikalara uygun yürütülüp yürütülmediğini',
        },
        'E',
        '**Uygunluk denetimi**, işletmenin faaliyet ve işlemlerinin belirli **kural, yasa, sözleşme veya politikalara uygun** yürütülüp yürütülmediğini araştırır (ör. vergi denetimi, SGK denetimi).',
        'Denetim - uygunluk denetimi',
    ),
    # düzey 2
    '0006': patch(
        'Denetim türleri denetçinin STATÜSÜNE göre sınıflandırıldığında aşağıdakilerden hangisi bu sınıflandırmada yer alır?',
        {
            'A': 'Bağımsız (dış) denetim, iç denetim, kamu denetimi',
            'B': 'Sürekli denetim, ara dönem denetimi, yıl sonu denetimi',
            'C': 'Finansal tablo denetimi, uygunluk denetimi, faaliyet denetimi',
            'D': 'Zorunlu (yasal) denetim, isteğe bağlı (ihtiyari) denetim',
            'E': 'Tam sayım (kül) denetimi, örnekleme yoluyla denetim',
        },
        'A',
        'Denetçinin **statüsüne göre** denetim: **bağımsız (dış) denetim, iç denetim ve kamu denetimi** olarak sınıflandırılır.',
        'Denetim - türleri (statü)',
    ),
    # düzey 3
    '0007': patch(
        'Denetim kavramı ve türleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Denetim tarafsızca kanıt toplayıp değerleyen sistematik bir süreçtir.\n\nII. Statüsüne göre denetim; finansal tablo, uygunluk ve faaliyet denetimi olarak ayrılır.\n\nIII. Konusuna göre denetim; finansal tablo, uygunluk ve faaliyet denetimi olarak ayrılır.',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'I ve II',
        },
        'C',
        '**II yanlıştır:** statüsüne (denetçinin konumuna) göre denetim bağımsız (dış), iç ve kamu denetimi olarak ayrılır; finansal tablo/uygunluk/faaliyet ayrımı ise KONUSUNA göre yapılan sınıflandırmadır. **I** denetim tarafsız/sistematik bir süreçtir ve **III** konusuna göre üçlü ayrım doğrudur. Doğru cevap **I ve III**.',
        'Denetim - kavram ve türler',
    ),
    # düzey 3
    '0008': patch(
        "Aşağıdakilerden hangisi Türkiye'de finansal tabloların bağımsız denetimini yapmaya YETKİLİ DEĞİLDİR?",
        {
            'A': 'Yetkilendirilmiş denetçi kadrosuyla faaliyet gösteren bağımsız denetim şirketi',
            'B': 'İşletmenin kendi bünyesinde kurulmuş olan iç denetim birimi',
            'C': 'Kamu Gözetimi Kurumu tarafından yetkilendirilmiş serbest muhasebeci mali müşavir',
            'D': 'Kamu Gözetimi Kurumu tarafından yetkilendirilmiş yeminli mali müşavir',
            'E': 'Kamu Gözetimi Kurumu tarafından yetkilendirilmiş bağımsız denetim kuruluşu',
        },
        'B',
        'Bağımsız denetim, **Kamu Gözetimi Kurumu (KGK) tarafından yetkilendirilmiş** SMMM/YMM unvanlı denetçiler ile denetim kuruluşları tarafından yapılır. İşletmenin **iç denetim birimi** işletmeye bağlı olduğundan bağımsız denetim yapamaz; iç denetim ayrı bir faaliyettir.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 3
    '0009': patch(
        'Güvence düzeyleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Bağımsız denetim makul güvence sağlar.\n\nII. İnceleme (gözden geçirme) hizmeti sınırlı güvence sağlar.\n\nIII. Makul güvence, denetçinin finansal tabloların mutlak doğruluğunu garanti ettiği anlamına gelir.',
        {
            'A': 'I ve III',
            'B': 'I, II ve III',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'Yalnız II',
        },
        'D',
        "**III yanlıştır:** makul güvence mutlak güvence değildir; örnekleme, iç kontrolün doğal sınırları ve kanıtın ikna edici niteliği nedeniyle mutlak doğruluk garanti edilemez. **I** denetim makul, **II** inceleme sınırlı güvence sağlar. Doğru cevap I ve II'dir.",
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 2
    '0010': patch(
        'Bir denetçinin, bir belediyenin harcamalarının ilgili mevzuata ve bütçeye uygun yapılıp yapılmadığını incelemesi, konusuna göre hangi denetim türüdür?',
        {
            'A': 'Uygunluk denetimi',
            'B': 'Pazar denetimi',
            'C': 'Kalite denetimi',
            'D': 'Finansal tablo denetimi',
            'E': 'Faaliyet denetimi',
        },
        'A',
        'Harcamaların **mevzuata ve bütçeye uygunluğunun** incelenmesi konusuna göre bir **uygunluk denetimidir**.',
        'Denetim - uygunluk denetimi',
    ),
    # düzey 2
    '0011': patch(
        'Finansal tablo denetiminde denetçinin sorumluluğu ile yönetimin sorumluluğu için doğru ifade hangisidir?',
        {
            'A': 'Hem finansal tabloları hazırlamak hem de bu tabloları denetleyip görüş bildirmek denetçinin sorumluluğundadır',
            'B': 'Finansal tabloları hazırlamak da denetleyip görüş bildirmek de yönetimin sorumluluğundadır',
            'C': 'Finansal tabloları hazırlamak da denetleyip görüş bildirmek de denetçinin sorumluluğundadır',
            'D': 'Finansal tabloları denetçi hazırlar; yönetim bu tabloları onaylayıp imzalar',
            'E': 'Finansal tabloları hazırlamak yönetimin, bu tablolara ilişkin görüş bildirmek denetçinin sorumluluğundadır',
        },
        'E',
        '**Finansal tabloları hazırlamak yönetimin**, bu tabloların denetlenip **görüş bildirilmesi denetçinin** sorumluluğundadır. Denetçinin tabloları hazırlaması bağımsızlığı zedeler.',
        'BDS 200 - sorumluluklar',
    ),
    # düzey 3
    '0012': patch(
        'Aşağıdakilerden hangisi denetçinin taşıması gereken temel niteliklerden biri DEĞİLDİR?',
        {
            'A': 'Mesleki özen ve şüphecilikle hareket etmek',
            'B': 'Mesleki yeterlik, yani gerekli bilgi ve deneyime sahip olmak',
            'C': 'Değerlendirmelerinde tarafsız davranmak',
            'D': 'Denetlediği işletmenin ortaklık yapısında pay sahibi olmak',
            'E': 'Denetlenen işletmeye karşı bağımsız olmak',
        },
        'D',
        'Denetlenen işletmede **pay sahibi olmak**, denetçinin bağımsızlığını ve tarafsızlığını zedeleyen bir çıkar ilişkisidir; nitelik değil engeldir. Mesleki yeterlik, bağımsızlık, tarafsızlık ve mesleki özen/şüphecilik ise denetçinin temel nitelikleridir.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 3
    '0013': patch(
        "Denetçinin 'mesleki şüphecilik' göstermesi ile ilgili aşağıdakilerden hangisi YANLIŞTIR?",
        {
            'A': 'Birbiriyle çelişen kanıtların araştırılmasını gerektirir',
            'B': 'Yönetimin ve çalışanların baştan hileli davrandığının kabul edilmesi demektir',
            'C': 'Denetimin tamamı boyunca sürdürülmesi gerekir',
            'D': 'Kanıtları sorgulayan bir zihin yapısıyla hareket etmeyi gerektirir',
            'E': 'Yönetim beyanlarının doğrulanmaksızın olduğu gibi kabul edilmemesini gerektirir',
        },
        'B',
        'Mesleki şüphecilik, **peşin bir suçlama değil**; kanıtı sorgulayan, çelişkileri araştıran ve beyanları doğrulamadan kabul etmeyen bir zihin yapısıdır. Herkesi baştan hileli saymak mesleki şüpheciliğin tanımı değildir. Diğer ifadeler doğrudur.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 2
    '0014': patch(
        "Bağımsız denetimin varlık nedeni olan 'bilgi asimetrisi (bilgi eşitsizliği)' aşağıdakilerden hangisini ifade eder?",
        {
            'A': 'İşletme hakkındaki finansal bilginin karar vericiler açısından önemsiz olması durumudur',
            'B': 'Denetçinin, işletme hakkında ön bilgi edinmeden denetime başlaması durumudur',
            'C': 'Yönetimin işletme hakkında dış bilgi kullanıcılarından daha fazla bilgiye sahip olması',
            'D': 'İşletmeyle ilişkili tüm tarafların dönem sonunda birbirine eşit tutarda kâr payı elde etmesi durumunu ifade eder',
            'E': 'İşletmeyle ilgili tüm tarafların işletme hakkında aynı düzeyde, eksiksiz ve tam bilgiye sahip olması durumunu ifade eder',
        },
        'C',
        '**Bilgi asimetrisi**, işletme yönetiminin dış bilgi kullanıcılarına göre işletme hakkında **daha fazla bilgiye sahip olmasıdır**. Bağımsız denetim, tabloların güvenilirliğini artırarak bu eşitsizliğin yarattığı güven sorununu azaltır.',
        'Denetim - bilgi asimetrisi',
    ),
    # düzey 3
    '0015': patch(
        'Aşağıdakilerden hangisi bağımsız denetimin doğal kısıtlarından (denetimin sınırlarından) biri DEĞİLDİR?',
        {
            'A': 'Örnekleme (test) yöntemi kullanılması',
            'B': 'Muhasebe tahminlerinin öznellik/belirsizlik içermesi',
            'C': 'Kanıtların ikna edici nitelikte olması (kesin olmaması)',
            'D': 'Hile için yapılan gizli anlaşmaların ortaya çıkarılmasının güç olması',
            'E': 'Denetçinin tüm işlemleri istisnasız incelemesi',
        },
        'E',
        'Denetimin doğal kısıtları; örnekleme, kanıtların ikna edici (kesin değil) niteliği, gizli anlaşmaların güçlüğü ve tahminlerin belirsizliğidir. **Tüm işlemlerin istisnasız incelenmesi** zaten mümkün değildir; bu bir kısıt değil, denetimin neden örnekleme yaptığının nedenidir.',
        'Denetim - doğal kısıtlar',
    ),
    # düzey 2
    '0016': patch(
        'Bir denetçinin, denetlediği işletmenin aynı zamanda muhasebe kayıtlarını da tutması durumunda ortaya çıkan temel sorun aşağıdakilerden hangisidir?',
        {
            'A': 'İşletmeye ek bir vergi avantajı sağlanır; ödenecek kurumlar vergisi azalır',
            'B': 'Sakınca doğmaz; aynı kişinin kaydı tutup denetlemesi olağan bir durumdur',
            'C': 'Denetçi kayıtları bizzat kendisi tuttuğu için yaptığı denetim daha güvenilir, daha tutarlı ve daha hatasız hâle gelir',
            'D': 'Kendi tuttuğu kayıtları denetleyeceği için bağımsızlık ve tarafsızlık zedelenir (kendi kendini denetleme)',
            'E': 'Denetçi tek elden çalıştığından işletmenin ödediği toplam denetim ve muhasebe ücreti belirgin biçimde azalır',
        },
        'D',
        'Denetçinin denetlediği işletmenin kayıtlarını da tutması, **kendi işini denetlemesi (kendi kendini denetleme)** anlamına gelir ve **bağımsızlık/tarafsızlığı** ciddi biçimde zedeler. Bu nedenle yasaktır.',
        'Denetim - bağımsızlık (kendi kendini denetleme)',
    ),
    # düzey 2
    '0017': patch(
        'Aşağıdakilerden hangisi bağımsız denetimin işlevleri arasında YER ALMAZ?',
        {
            'A': 'Sermaye piyasalarının güvenilir bilgiyle işlemesine katkı sağlamak',
            'B': 'Kullanıcıların taşıdığı bilgi riskini azaltmak',
            'C': 'Yönetimin hesap verebilirliğini desteklemek',
            'D': 'Finansal tablolara güvenilirlik kazandırmak',
            'E': 'İşletmenin muhasebe politikalarını denetçinin belirleyip uygulaması',
        },
        'E',
        'Muhasebe politikalarını belirlemek ve uygulamak **yönetimin** sorumluluğundadır; denetçi bu politikaların uygunluğunu değerlendirir ama kendisi belirleyip uygulamaz (bağımsızlığı zedelenir). Diğer seçenekler denetimin bilinen işlevleridir.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 3
    '0018': patch(
        'Aşağıdakilerden hangisi denetimin KONUSUNA göre sınıflandırılmasına örnek DEĞİLDİR?',
        {
            'A': 'Performans denetimi',
            'B': 'İç denetim',
            'C': 'Finansal tablo denetimi',
            'D': 'Uygunluk denetimi',
            'E': 'Faaliyet denetimi',
        },
        'B',
        '**İç denetim**, denetçinin statüsüne (kim yaptığına) göre yapılan sınıflandırmanın bir türüdür. Konusuna göre sınıflandırma; finansal tablo, uygunluk ve faaliyet (performans) denetimi ayrımıdır.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 2
    '0019': patch(
        'Bir denetim kuruluşunun, denetlediği şirketin hisselerine sahip olması durumu hangi ilkeyi zedeler?',
        {
            'A': 'İhtiyatlılık (temkinli olma) ilkesi',
            'B': 'Tarihi maliyet (maliyet esası) ilkesi',
            'C': 'Bağımsızlık (kişisel çıkar tehdidi)',
            'D': 'Reklam ve tanıtım yasağı ilkesi',
            'E': 'İşletmenin sürekliliği (süreklilik)',
        },
        'C',
        'Denetim kuruluşunun denetlediği şirketin hisselerine sahip olması, o şirketin finansal durumundan **kişisel çıkar** sağlaması demektir; bu durum **bağımsızlığı** doğrudan zedeler (kişisel çıkar tehdidi).',
        'Denetim - bağımsızlık (kişisel çıkar)',
    ),
    # düzey 2
    '0020': patch(
        'Bir işletmenin iç denetçisinin hazırladığı rapor ile bağımsız denetçinin raporu arasındaki temel fark aşağıdakilerden hangisidir?',
        {
            'A': 'İç denetim raporu her dönem kamuya ilan edilir ve ticaret siciline tescil ettirilir',
            'B': 'İç denetim raporu üçüncü taraflara güvence verir ve kamuya açıklanır; bağımsız denetim raporu ise yönetime sunulur',
            'C': 'İki rapor aynı içerik ve amaçtadır; muhatap ve kapsam yönünden aralarında fark yoktur',
            'D': 'İç denetim raporu yönetime, bağımsız denetim raporu üçüncü taraflara yöneliktir',
            'E': 'Bağımsız denetim raporu yönetime ve iç birimlere verilir; üçüncü taraflarla paylaşılmaz',
        },
        'D',
        '**İç denetim raporu** öncelikle **yönetime** yönelik olup iç kontrol/süreçlere ilişkindir. **Bağımsız denetim raporu** ise **finansal tablolara** ilişkin, üçüncü taraflara **güvence** veren bir görüş içerir.',
        'Denetim - iç/bağımsız denetim raporu',
    ),
    # düzey 3
    '0021': patch(
        'Aşağıdakilerden hangisi denetimin temel unsurlarından biri DEĞİLDİR?',
        {
            'A': 'Tarafsız (objektif) kanıt toplama ve değerleme',
            'B': 'İktisadi olaylara ilişkin iddialar',
            'C': 'Sonuçların ilgili taraflara raporlanması',
            'D': 'İşletmenin satış hasılatının artırılması',
            'E': 'Önceden belirlenmiş ölçütler',
        },
        'D',
        'Denetimin unsurları; iddialar, ölçütler, tarafsız kanıt toplama/değerleme, uygunluk derecesi ve raporlamadır. **Satış hasılatının artırılması** denetimin bir unsuru değildir.',
        'Denetim - unsurlar',
    ),
    # düzey 2
    '0022': patch(
        "Finansal tablo denetiminde kullanılan 'önceden belirlenmiş ölçüt' genellikle aşağıdakilerden hangisidir?",
        {
            'A': 'İşletmenin tabi olduğu finansal raporlama çerçevesi (ör. TMS/TFRS veya MSUGT)',
            'B': 'Borsada işlem gören payların günlük fiyat hareketini gösteren pay senedi piyasa endeksinin değeri',
            'C': 'Ülke genelinde tüketici fiyatlarındaki artışı ölçen ve aylık açıklanan yıllık enflasyon oranı verisi',
            'D': 'Denetçinin herhangi bir raporlama çerçevesine bağlı kalmadan oluşturduğu kişisel kanaat ve sezgi',
            'E': 'Aynı sektörde faaliyet gösteren bir rakip işletmenin yayımladığı bilanço ve gelir tablosu tutarları',
        },
        'A',
        'Finansal tablo denetiminde ölçüt, işletmenin uymak zorunda olduğu **finansal raporlama çerçevesidir** (TMS/TFRS veya MSUGT/BOBİ FRS). Denetçi, tabloların bu çerçeveye uygunluğunu değerlendirir.',
        'Denetim - raporlama çerçevesi',
    ),
    # düzey 2
    '0023': patch(
        'Muhasebe ile denetim arasındaki ilişki için aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Muhasebe ile denetim aynı işlemin iki farklı adı olup ikisi de işlemleri deftere kaydetme faaliyetidir',
            'B': 'Muhasebe verileri kaydedip özetleyerek finansal tabloları ÜRETİR; denetim ise bu tabloların doğruluğunu tarafsızca inceleyip DOĞRULAR',
            'C': 'Muhasebe ile denetim birbirinden tamamen kopuktur; ikisi arasında ne veri, ne yöntem ne de amaç yönünden herhangi bir bağ veya ilişki yoktur',
            'D': 'Denetim işlemleri belgelere dayanarak deftere kaydeder; muhasebe ise bu kayıtları tarafsızca inceleyip doğrular',
            'E': 'Muhasebe, denetimin bir alt dalıdır ve denetçinin gözetimi ve talimatı altında yürütülür',
        },
        'B',
        '**Muhasebe**, işlemleri kaydedip sınıflayıp özetleyerek finansal tabloları **üretir** (yapıcı/ileriye doğru). **Denetim** ise bu tabloların doğruluğunu tarafsızca **inceleyip doğrular** (çözümleyici/tersine doğru).',
        'Denetim - muhasebe ilişkisi',
    ),
    # düzey 2
    '0024': patch(
        'Denetim türleri KONUSUNA (amacına) göre sınıflandırıldığında aşağıdakilerden hangisi bu sınıflandırmada yer alır?',
        {
            'A': 'İç denetim, dış (bağımsız) denetim ve kamu denetimi ayrımı',
            'B': 'Ulusal denetim ile sınır ötesi uluslararası denetim ayrımı',
            'C': 'Yıl boyu sürekli denetim ile belirli dönemlerde yapılan ara denetim',
            'D': 'Tüm işlemlerin incelendiği tam denetim ile sınırlı (örnekleme) denetim',
            'E': 'Finansal tablo denetimi, uygunluk denetimi, faaliyet denetimi',
        },
        'E',
        'Denetim **konusuna/amacına göre**: **finansal (mali) tablo denetimi, uygunluk denetimi ve faaliyet (performans) denetimi** olarak sınıflandırılır. (İç/dış/kamu ayrımı ise denetçinin statüsüne göredir.)',
        'Denetim - türleri (konu)',
    ),
    # düzey 2
    '0025': patch(
        "'Faaliyet (performans) denetimi' temel olarak aşağıdakilerden hangisini değerlendirir?",
        {
            'A': 'İşletmenin sahip olduğu depo, ambar ve üretim alanlarının fiziksel büyüklüğünü',
            'B': 'İşletmenin vergi yasalarına uygunluğunu ve verdiği beyanların doğruluğunu',
            'C': 'İşletmenin ortaklarının kimlik bilgilerini, pay oranlarını ve ikametgâhlarını',
            'D': 'Faaliyetlerin etkinliğini, verimliliğini ve ekonomikliğini',
            'E': 'Finansal tabloların raporlama çerçevesine uygun sunulup sunulmadığını',
        },
        'D',
        '**Faaliyet (performans) denetimi**, işletme faaliyetlerinin/birimlerinin **etkinliğini, verimliliğini ve ekonomikliğini** (3E: etkinlik, verimlilik, ekonomiklik) değerlendirip iyileştirme önerileri sunar.',
        'Denetim - faaliyet denetimi',
    ),
    # düzey 3
    '0026': patch(
        'İç denetim ile ilgili aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'İşletme bünyesinde, işletmeye bağlı iç denetçiler tarafından yürütülür',
            'B': 'Örgütsel bağımsızlığı güçlendirmek için genellikle yönetim kuruluna veya denetim komitesine raporlar',
            'C': 'Kapsamı finansal tablolarla sınırlı olmayıp faaliyetlerin etkinliğini de içerir',
            'D': 'İç kontrol ve risk yönetimi süreçlerinin etkinliğini değerlendirir',
            'E': 'İç denetçinin raporu üçüncü taraflara bağımsız denetim görüşü sağlar',
        },
        'E',
        'İç denetim işletmeye **bağlı** bir faaliyettir ve öncelikle yönetime hizmet eder; raporu üçüncü taraflara yönelik **bağımsız denetim görüşü niteliği taşımaz**. Üçüncü taraflara güvence, işletme dışından yetkili bağımsız denetçinin raporuyla sağlanır. Diğer ifadeler doğrudur.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 2
    '0027': patch(
        "'Kamu denetimi' aşağıdakilerden hangisiyle tanımlanır?",
        {
            'A': 'Özel sektör şirketlerinin, aralarındaki sözleşmeye dayanarak birbirini karşılıklı denetlemesi',
            'B': 'Devlet adına, kamu kurumlarınca (ör. Sayıştay, vergi denetim birimleri) yürütülen denetim',
            'C': 'Bağımsız denetim kuruluşlarının, ücret karşılığında yürüttüğü finansal tablo denetimi hizmeti',
            'D': 'Müşterilerin memnuniyet düzeyini ölçmek amacıyla yapılan anket ve geri bildirim araştırması',
            'E': 'İşletme çalışanlarının, kendi yaptıkları işleri dönem içinde kendi aralarında karşılıklı denetlemesi',
        },
        'B',
        "**Kamu denetimi**, devlet adına **kamu kurumlarınca** yürütülen denetimdir (ör. Sayıştay'ın kamu kaynaklarını, vergi denetim birimlerinin mükellefleri denetlemesi).",
        'Denetim - kamu denetimi',
    ),
    # düzey 2
    '0028': patch(
        "Türkiye'de bağımsız denetim alanını düzenleyen ve denetçileri yetkilendiren kamu otoritesi aşağıdakilerden hangisidir?",
        {
            'A': 'Rekabet Kurumu (piyasada rekabetin korunması)',
            'B': 'KGK (Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu)',
            'C': 'TCMB (Türkiye Cumhuriyet Merkez Bankası, para ve kur politikası)',
            'D': 'TÜİK (Türkiye İstatistik Kurumu, resmî istatistik)',
            'E': 'SPK (Sermaye Piyasası Kurulu, sermaye piyasaları)',
        },
        'B',
        "Türkiye'de bağımsız denetimi düzenleyen, denetim standartlarını yayımlayan ve denetçileri yetkilendiren otorite **KGK (Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu)**'dur.",
        'KGK - düzenleyici otorite',
    ),
    # düzey 3
    '0029': patch(
        'Aşağıdakilerden hangisi bağımsız denetimin sağladığı yararlardan biri DEĞİLDİR?',
        {
            'A': 'İşletmenin gelecekte kâr edeceğini garanti etmesi',
            'B': 'Sermaye piyasalarının etkin işleyişine katkı sağlaması',
            'C': 'Kredi ve yatırım kararlarına güven sağlaması',
            'D': 'Bilgi riskini azaltması',
            'E': 'Finansal bilginin güvenilirliğini artırması',
        },
        'A',
        'Bağımsız denetim güvenilirlik sağlar, bilgi riskini azaltır, karar ve piyasalara güven verir. Ancak işletmenin **gelecekte kâr edeceğini garanti etmez**; denetim geçmiş/mevcut tablolara güvence verir, gelecek performansını garanti etmez.',
        'Denetim - yararları',
    ),
    # düzey 3
    '0030': patch(
        'Aşağıdakilerden hangisi bir kamu denetim organı/denetçisi DEĞİLDİR?',
        {
            'A': 'Sayıştay denetçileri',
            'B': 'İşletme yönetim kurulunun atadığı iç denetim birimi çalışanları',
            'C': 'Vergi Denetim Kurulu vergi müfettişleri',
            'D': 'Kamu kurumlarında görev yapan teftiş kurulu müfettişleri',
            'E': 'Sosyal Güvenlik Kurumu denetim elemanları',
        },
        'B',
        'Kamu denetimi, devlet adına yetkili **kamu kurumları** tarafından yapılır (Sayıştay, Vergi Denetim Kurulu, SGK, teftiş kurulları). İşletme yönetiminin atadığı **iç denetim birimi** işletmeye bağlıdır; kamu denetimi değil iç denetim kapsamındadır.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 2
    '0031': patch(
        "Bir işletmenin finansal tablolarının TFRS'ye uygun olarak gerçeğe uygun sunulup sunulmadığının incelenmesi hangi denetim türüdür?",
        {
            'A': 'Finansal (mali) tablo denetimi',
            'B': 'Kalite (ürün standardı) denetimi',
            'C': 'Uygunluk (yasaya uyum) denetimi',
            'D': 'Faaliyet (etkinlik) denetimi',
            'E': 'Performans (birim çıktı) denetimi',
        },
        'A',
        'Finansal tabloların bir raporlama çerçevesine (TFRS) uygun ve gerçeğe uygun sunumunun incelenmesi **finansal (mali) tablo denetimidir**.',
        'Denetim - finansal tablo denetimi',
    ),
    # düzey 3
    '0032': patch(
        'Hata ve hile ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Hata, kasıtlı olarak yapılan ve gizlenmeye çalışılan bir eylemdir.\n\nII. Hile kasıtlı bir eylemdir ve genellikle gizlenmeye çalışılır.\n\nIII. Denetçi, her koşulda hilenin tamamını kesin biçimde ortaya çıkarmakla yükümlüdür.',
        {
            'A': 'Yalnız II',
            'B': 'I, II ve III',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I ve III',
        },
        'A',
        '**I yanlıştır:** hata kasıt içermeyen yanlışlıktır; kasıt ve gizleme hilenin özelliğidir. **III yanlıştır:** denetim makul güvence sağladığından, özenle gizlenmiş bir hilenin tamamının ortaya çıkarılacağı garanti edilemez. Yalnızca **II** doğrudur.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 2
    '0033': patch(
        "'Hata' ile 'hile' arasındaki temel fark aşağıdakilerden hangisidir?",
        {
            'A': 'Hata da hile de kasıtlı (bilerek) yapılan yanlışlıklardır; aralarında herhangi bir kasıt ya da amaç farkı yoktur',
            'B': 'Hata bilerek ve kasıtlı olarak yapılan bir yanlışlıktır; hile ise yanlışlıkla, herhangi bir kasıt ya da amaç olmadan yapılan bir yanlışlıktır',
            'C': 'Hata kasıtsız bir yanlışlık, hile ise aldatma amacıyla yapılan kasıtlı bir yanlışlıktır',
            'D': 'Hata da hile de kasıtsız, yani yanlışlıkla yapılan yanlışlıklardır; aralarında herhangi bir kasıt ya da amaç farkı bulunmaz',
            'E': 'Hata ile hile arasında fark yoktur; ikisi de aynı nitelikte yanlışlığı ifade eder',
        },
        'C',
        '**Hata**, kasıtsız (yanlışlıkla yapılan) bir yanlışlıktır. **Hile**, kasıtlı olarak (bilerek, çıkar sağlamak veya aldatmak amacıyla) yapılan bir yanlışlıktır. Temel ayrım **kasıt** unsurudur.',
        'BDS 240 - hata ve hile',
    ),
    # düzey 3
    '0034': patch(
        'İç denetim ile bağımsız denetimin karşılaştırılması bakımından aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'İç denetim işletme bünyesinde, bağımsız denetim işletme dışından yürütülür',
            'B': 'Bağımsız denetçinin denetlenen işletmeyle çıkar ilişkisi bulunmaz',
            'C': 'İç denetimin kapsamı finansal tablolarla sınırlı olmayıp faaliyet ve riskleri de içerir',
            'D': 'İç denetçinin raporu, bağımsız denetim raporunun yerine geçerek üçüncü taraflara güvence sağlar',
            'E': 'İç denetim öncelikle yönetime, bağımsız denetim üçüncü taraflara hizmet eder',
        },
        'D',
        'İç denetim raporu bağımsız denetim raporunun **yerine geçmez**; iç denetçi işletmeye bağlı olduğundan üçüncü taraflara yönelik bağımsız güvence veremez. İki denetim birbirini tamamlar ancak yerine geçmez. Diğer ifadeler doğrudur.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 3
    '0035': patch(
        'Denetçi görüşü ile ilgili aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'Finansal tablolardaki her rakamın mutlak doğruluğunu garanti eden bir belgedir',
            'B': 'Tabloların geçerli raporlama çerçevesine uygunluğuna ilişkindir',
            'C': 'Önemlilik çerçevesinde tabloların bütünü değerlendirilerek oluşturulur',
            'D': 'Finansal tabloların önemli yanlışlık içermediğine ilişkin makul güvence sağlar',
            'E': 'İşletmenin gelecekteki başarısına ilişkin bir güvence içermez',
        },
        'A',
        'Denetim **makul güvence** sağlar; örnekleme, iç kontrolün doğal sınırları ve kanıtın ikna edici (kesin olmayan) niteliği nedeniyle her rakamın mutlak doğruluğu garanti edilemez. Diğer ifadeler doğrudur.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 2
    '0036': patch(
        'Halka açık bir şirketin bağımsız denetimini yapan denetçinin görüşü öncelikle kime yönelik güvence sağlar?',
        {
            'A': 'İşletmenin kadrosunda çalışan personele ve iç birimlere',
            'B': 'İşletmenin üst yönetimine ve yönetim kuruluna',
            'C': 'Başta ortaklar ve yatırımcılar olmak üzere tablo kullanıcılarına',
            'D': 'İşletme içi bilgilendirme ve arşiv birimine',
            'E': 'Aynı sektördeki rakip firmalara ve tedarikçilere',
        },
        'C',
        'Bağımsız denetçinin görüşü, başta **mevcut ve potansiyel ortaklar/yatırımcılar** olmak üzere kredi verenler, kamu ve diğer **finansal tablo kullanıcılarına** güvence sağlar.',
        'Denetim - tablo kullanıcıları',
    ),
    # düzey 2
    '0037': patch(
        'Denetim kanıtı toplayıp değerleyen denetçinin ulaştığı sonucu açıkladığı nihai çıktı aşağıdakilerden hangisidir?',
        {
            'A': 'Envanter listesi (sayım dökümü)',
            'B': 'Bütçe (gelir-gider tahmini)',
            'C': 'Gelir tablosu (kâr-zarar tablosu)',
            'D': 'Denetim raporu (denetçi görüşü)',
            'E': 'Bilanço (finansal durum tablosu)',
        },
        'D',
        'Denetim sürecinin nihai çıktısı, denetçinin ulaştığı sonucu/görüşü açıkladığı **denetim raporudur (denetçi görüşü)**. Bilanço/gelir tablosu ise denetlenen finansal tablolardır.',
        'Denetim - denetim raporu',
    ),
    # düzey 2
    '0038': patch(
        "Denetimin 'iddia (beyan) — ölçüt — kanıt' üçlüsündeki mantığı hangi seçenekte doğru sıralanmıştır?",
        {
            'A': 'Ölçüt kullanılmaz; yönetimin iddiaları bir çerçeveyle karşılaştırılmadan kabul edilir',
            'B': 'Yönetimin ileri sürdüğü iddialar denetçinin kendisi tarafından üretilir; denetçi hem iddiayı oluşturur hem de kendisi doğrular',
            'C': 'Denetçi kanıt toplamadan, yönetimin iddialarına dayanarak doğrudan görüş bildirir',
            'D': 'Denetçi önce finansal tablolar hakkında görüşünü açıklar; ardından bu görüşü doğrulayacak kanıtları geriye dönük olarak arar ve toplar',
            'E': 'İddialar ölçütlerle karşılaştırılır; bunun için kanıt toplanıp değerlenir ve sonuç raporlanır',
        },
        'E',
        'Denetim mantığı: **yönetimin iddiaları**, belirlenmiş **ölçütlerle** karşılaştırılır; bu karşılaştırma için **tarafsız kanıt** toplanıp değerlenir ve sonuç raporlanır. Denetçi önce kanıt toplar, sonra görüş oluşturur.',
        'Denetim - iddia/ölçüt/kanıt',
    ),
    # düzey 2
    '0039': patch(
        'Aşağıdakilerden hangisi iç denetimin kapsamına GİRMEZ?',
        {
            'A': 'İşletme politika ve prosedürlerine uyumu izlemek',
            'B': 'Faaliyetlerin verimliliğini ve etkinliğini incelemek',
            'C': 'Üçüncü taraflara bağımsız denetim görüşü açıklamak',
            'D': 'İç kontrol sisteminin etkinliğini değerlendirmek',
            'E': 'Risk yönetimi süreçlerini gözden geçirmek',
        },
        'C',
        'Üçüncü taraflara yönelik **bağımsız denetim görüşü** açıklamak, işletme dışından yetkilendirilmiş bağımsız denetçinin işidir. İç denetim; iç kontrol, risk yönetimi, verimlilik ve uyum konularında yönetime hizmet eder.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 3
    '0040': patch(
        'Aşağıdakilerden hangisi denetim kavramıyla ilgili YANLIŞ bir ifadedir?',
        {
            'A': 'Denetim standartlara (BDS) uygun yürütülür',
            'B': 'Denetim, finansal tablolara güvence kazandırarak bilgi riskini azaltır',
            'C': 'Denetim tarafsız kanıt toplayıp değerleyen sistematik bir süreçtir',
            'D': 'Denetçi mesleki şüphecilikle hareket eder',
            'E': 'Denetim, finansal tabloları hazırlama işlemidir',
        },
        'E',
        "Yanlış olan **A**'dir: finansal tabloları **hazırlamak muhasebenin/yönetimin** işidir. Denetim, hazır tabloları **inceleyip görüş bildirme** sürecidir. Diğer ifadeler doğrudur.",
        'Denetim - kavram',
    ),
    # düzey 2
    '0041': patch(
        "Finansal tablo denetiminde 'iddialar (yönetim beyanları)' ile anlatılmak istenen aşağıdakilerden hangisidir?",
        {
            'A': 'Vergi dairesinin, mükelleften belirli hesap dönemlerine ait defter, kayıt ve belgeleri incelenmek üzere ibraz etmesini istediği resmî yazışma ve tebligat talepleri',
            'B': 'Yönetimin finansal tablolar aracılığıyla açık veya örtük olarak ileri sürdüğü (var olma, tamlık, değerleme, haklar-yükümlülükler, sunum vb.) beyanlar',
            'C': 'Denetçinin, topladığı denetim kanıtlarını değerlendirdikten sonra finansal tabloların bütünü hakkında ulaştığı olumlu, şartlı ya da olumsuz nitelikteki denetim görüşü',
            'D': 'Bankanın, işletmeye kullandırdığı kredinin faiz oranını, geri ödeme vadesini, teminatını ve temerrüt sonuçlarını belirleyen ve sözleşmeye bağlanan kredi koşulları',
            'E': 'Rakip firmaların kendi ürün, hizmet ve fiyat politikaları hakkında kamuoyuna ve müşterilere yönelik yaptığı reklam, tanıtım ve basın açıklamaları',
        },
        'B',
        '**İddialar (yönetim beyanları)**, yönetimin finansal tablolar aracılığıyla açık/örtük olarak ileri sürdüğü beyanlardır: **var olma/gerçekleşme, tamlık, değerleme/ölçüm, haklar ve yükümlülükler, sınıflandırma ve sunum** gibi. Denetçi bu iddiaların doğruluğunu araştırır.',
        'BDS 315 - yönetim beyanları',
    ),
    # düzey 2
    '0042': patch(
        'Aşağıdakilerden hangisi bağımsız denetimin amaçları arasında YER ALMAZ?',
        {
            'A': 'Kullanıcıların karar kalitesini destekleyecek güvenilir bilgi sağlanmasına katkı vermek',
            'B': 'Finansal tablo kullanıcılarının taşıdığı bilgi riskini azaltmak',
            'C': 'İşletmenin gelecek dönem kârını öngörüp yatırımcılara tahmin sunmak',
            'D': 'Finansal tabloların geçerli raporlama çerçevesine uygunluğu hakkında görüş bildirmek',
            'E': 'Finansal tablolara bağımsız bir uzman güvencesi kazandırmak',
        },
        'C',
        'Bağımsız denetim geçmiş döneme ait finansal tabloların çerçeveye uygunluğunu inceler; **gelecek kârı öngörmek veya tahmin sunmak denetimin amacı değildir**. Diğer seçenekler (görüş bildirme, bilgi riskini azaltma, güvence kazandırma, karar kalitesine katkı) denetimin tanınmış amaçlarıdır.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 2
    '0043': patch(
        'Denetim süreci, muhasebe sürecine göre hangi yönde işler?',
        {
            'A': 'Muhasebe ile tamamen aynı yönde işler; belgelerden başlayıp kayıt ve mizan yoluyla finansal tablolara doğru ilerler',
            'B': 'Muhasebeyle aynı yönde: belgelerden başlayıp kayıtlara ve finansal tablolara doğru (bireşimsel)',
            'C': 'Denetimde yön diye bir kavram yoktur; süreç herhangi bir mantıksal sıraya bağlı olmadan yürütülür',
            'D': 'Muhasebenin tersi yönde: finansal tablolardan başlayıp kanıtlara/belgelere doğru (analitik/çözümleyici)',
            'E': 'Belirli bir yön izlemez; toplanan kanıtlar rastgele, plansız ve sırasız biçimde ele alınıp değerlendirilir',
        },
        'D',
        'Denetim, muhasebenin **tersi yönde** işler: finansal tablolardan başlanıp altındaki kayıt ve belgelere (kanıtlara) doğru inilir. Bu nedenle denetim **çözümleyici/analitik** bir süreçtir.',
        'Denetim - süreç yönü',
    ),
    # düzey 2
    '0044': patch(
        "'Finansal (mali) tablo denetimi' aşağıdakilerden hangisini amaçlar?",
        {
            'A': 'İşletmenin işlem ve faaliyetlerinin yürürlükteki yasa, yönetmelik, tebliğ ve sözleşme hükümlerine uygun yürütülüp yürütülmediğini araştırmak',
            'B': 'Çalışanların iş performansını, verimliliğini ve belirlenen hedeflere ulaşma derecesini değerlendirip ödüllendirmek',
            'C': 'İşletme faaliyetlerinde kaynakların ne ölçüde verimli ve ekonomik kullanıldığını ve elde edilen çıktı düzeyini ölçmek',
            'D': 'Finansal tabloların, belirlenmiş finansal raporlama çerçevesine uygun ve gerçeğe uygun biçimde sunulup sunulmadığı konusunda görüş bildirmek',
            'E': 'Üretilen ürünlerin ve verilen hizmetlerin belirlenen kalite standartlarını karşılayıp karşılamadığını test etmek',
        },
        'D',
        '**Finansal tablo denetimi**, finansal tabloların belirlenmiş **finansal raporlama çerçevesine** uygun ve **gerçeğe uygun** biçimde sunulup sunulmadığı konusunda görüş bildirmeyi amaçlar.',
        'Denetim - finansal tablo denetimi',
    ),
    # düzey 2
    '0045': patch(
        'Vergi incelemesi (vergi denetimi), konusuna göre hangi denetim türüne en yakındır?',
        {
            'A': 'Uygunluk denetimi (vergi yasalarına uygunluk araştırılır)',
            'B': 'Performans denetimi (birim çıktı düzeyi ölçülür)',
            'C': 'Faaliyet denetimi (kaynakların verimliliği ölçülür)',
            'D': 'Kalite denetimi (ürünün standarda uygunluğu ölçülür)',
            'E': 'Pazarlama denetimi (satış kanallarının etkinliği ölçülür)',
        },
        'A',
        'Vergi incelemesi, mükellefin işlemlerinin **vergi yasalarına uygunluğunu** araştırdığından konusuna göre bir **uygunluk denetimidir**.',
        'Denetim - uygunluk denetimi',
    ),
    # düzey 3
    '0046': patch(
        'Bağımsız (dış) denetim ile ilgili aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'Denetçinin denetlediği işletmeyle çıkar ilişkisi bulunmaması gerekir',
            'B': 'Öncelikle yatırımcı ve kredi verenler gibi üçüncü taraflara güvence sağlar',
            'C': 'İşletme dışından, yetkilendirilmiş denetçiler tarafından yürütülür',
            'D': 'Finansal tablolar hakkında mutlak değil makul güvence verir',
            'E': 'Denetçi, tespit ettiği yanlışlıkları kendisi düzelterek tabloları yeniden düzenler',
        },
        'E',
        'Finansal tabloları düzenlemek **yönetimin sorumluluğudur**; denetçi tabloları kendisi düzeltip yeniden düzenlerse bağımsızlığını yitirir ve kendi hazırladığı bilgiyi denetlemiş olur. Denetçi yanlışlığı belirler ve düzeltilmesini ister; düzeltmeyi yönetim yapar. Diğer ifadeler doğrudur.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 3
    '0047': patch(
        'İç denetim ve bağımsız denetim ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Bağımsız denetim, işletme dışından yetkilendirilmiş denetçiler tarafından yürütülür.\n\nII. İç denetimin kapsamı yalnızca finansal tabloların denetimiyle sınırlıdır.\n\nIII. Bağımsız denetim, yatırımcı ve kredi verenler gibi üçüncü taraflara güvence sağlar.',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'I ve III',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'C',
        "**II yanlıştır:** iç denetimin kapsamı finansal tablolarla sınırlı değildir; iç kontrol, risk yönetimi ve faaliyetlerin etkinliğini de içerir. **I** bağımsız denetim işletme dışından yetkili denetçilerce yapılır; **III** bağımsız denetim üçüncü taraflara güvence sağlar. Doğru cevap I ve III'tür.",
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 2
    '0048': patch(
        'İç denetçinin bağımsızlığı ile bağımsız denetçinin bağımsızlığı arasındaki fark için doğru ifade hangisidir?',
        {
            'A': 'İç denetçi işletmeye bağlı olduğundan tam bağımsız değildir ama denetlediği birimlerden ayrı ve tarafsız olmalıdır',
            'B': 'Bağımsız denetçi, denetim ücretini doğrudan denetlediği işletmeden aldığı için o işletmenin yönetimine bağlı çalışan bir personel konumundadır ve bağımsız sayılmaz',
            'C': 'İç denetçi de bağımsız denetçi de işletmenin bir parçasıdır; her ikisi de işletme kadrosunda yer alan ve yönetime bağlı çalışan personel olup dışarıdan görev almaz',
            'D': 'İç denetçinin tarafsız olması gerekmez; yönetimin talep ettiği sonuçları raporlaması yeterlidir',
            'E': 'İç denetçi de bağımsız denetçi gibi işletme dışından atanır; ikisi arasında bağımsızlık farkı yoktur',
        },
        'A',
        '**İç denetçi** işletmeye bağlı çalıştığından tam bağımsız değildir; yine de denetlediği birimlerden **örgütsel olarak ayrı ve tarafsız** olması beklenir. **Bağımsız denetçi** ise işletmeden **tümüyle bağımsızdır**.',
        'Denetim - iç/bağımsız denetçi bağımsızlığı',
    ),
    # düzey 3
    '0049': patch(
        'Güvence hizmetleri ile ilgili aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'Makul güvence veya sınırlı güvence düzeyinde sunulabilir',
            'B': 'Bağımsız denetim bir güvence hizmetidir',
            'C': 'Ulaşılan sonuç bir raporla ilgili taraflara bildirilir',
            'D': 'Bir konu hakkındaki bilginin güvenilirliğini artırmayı amaçlar',
            'E': 'Güvenceyi veren taraf, güvence verdiği bilgiyi hazırlayan taraf ile aynı olmalıdır',
        },
        'E',
        'Güvence hizmetinin özü, bilgiyi **hazırlayan taraftan bağımsız** bir uzmanın değerlendirme yapmasıdır; bilgiyi hazırlayanla güvence verenin aynı olması bağımsızlığı ortadan kaldırır ve güvence sağlamaz. Diğer ifadeler doğrudur.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 2
    '0050': patch(
        'Bir denetçinin, işletmenin üretim biriminin kaynakları ne ölçüde verimli ve ekonomik kullandığını değerlendirmesi hangi denetim türüdür?',
        {
            'A': 'Faaliyet (performans) denetimi',
            'B': 'Finansal (mali) tablo denetimi',
            'C': 'Uygunluk (mevzuata uyum) denetimi',
            'D': 'Kasa (nakit sayımı) denetimi',
            'E': 'Vergi (beyan doğruluğu) denetimi',
        },
        'A',
        'Kaynakların **verimli ve ekonomik** kullanımının değerlendirilmesi bir **faaliyet (performans) denetimidir** (etkinlik-verimlilik-ekonomiklik).',
        'Denetim - faaliyet denetimi',
    ),
    # düzey 3
    '0051': patch(
        "Denetimin 'sistematik bir süreç' olması ile ilgili aşağıdakilerden hangisi YANLIŞTIR?",
        {
            'A': 'Denetim standartlarına dayanılarak yürütülür',
            'B': 'Yapılan çalışma çalışma kâğıtlarıyla belgelenir',
            'C': 'Her denetçinin standartlardan bağımsız, kendi belirlediği sırayla yürüttüğü incelemedir',
            'D': 'Rastgele değil, önceden planlanmış bir program çerçevesinde ilerler',
            'E': 'Planlama, kanıt toplama, değerlendirme ve raporlama aşamalarını içerir',
        },
        'C',
        'Denetimin sistematik olması, **standartlara ve önceden belirlenmiş bir plana** bağlı yürütülmesi demektir; denetçinin standartlardan bağımsız, keyfî bir sıra izlemesi sistematik süreç anlayışıyla çelişir. Diğer ifadeler doğrudur.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 3
    '0052': patch(
        'Denetim türlerinin sınıflandırılması bakımından aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'Denetçinin statüsüne göre bağımsız denetim, iç denetim ve kamu denetimi ayrımı yapılır',
            'B': 'Uygunluk denetimi, işlemlerin belirlenmiş kural ve mevzuata uygunluğunu araştırır',
            'C': 'Konusuna göre finansal tablo, uygunluk ve faaliyet denetimi ayrımı yapılır',
            'D': 'Faaliyet denetimi, kaynakların etkin ve verimli kullanımını değerlendirir',
            'E': 'Konusuna göre sınıflandırmada bağımsız denetim, iç denetim ve kamu denetimi ayrımı yapılır',
        },
        'E',
        'Bağımsız denetim / iç denetim / kamu denetimi ayrımı **denetçinin statüsüne** göre yapılır; konusuna göre ayrım finansal tablo, uygunluk ve faaliyet denetimidir. Bu nedenle iki ölçütü birbirine karıştıran ifade yanlıştır.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 2
    '0053': patch(
        "Bağımsız denetimin 'zorunlu' olduğu durum aşağıdakilerden hangisidir?",
        {
            'A': 'Yabancı sermayeli şirketler için zorunludur; yerli şirketler için isteğe bağlıdır',
            'B': 'İstisnasız her işletme için, büyüklüğüne ve niteliğine bakılmaksızın yasa gereği zorunlu tutulan bir denetimdir',
            'C': 'Zorunlu olmayıp denetim yaptırılıp yaptırılmayacağı her işletmenin tercihine bırakılmıştır',
            'D': 'Belirli büyüklük veya nitelik ölçütlerini taşıyan ya da mevzuatça kapsama alınan şirketler için zorunludur',
            'E': 'Kamu kurum ve kuruluşları için zorunludur; özel sektör şirketleri büyüklüğüne bakılmaksızın kapsam dışıdır',
        },
        'D',
        'Bağımsız denetim, **belirli ölçütleri taşıyan veya mevzuatça kapsama alınan** şirketler (ör. halka açık şirketler, bankalar, ölçütleri aşan şirketler) için **zorunludur**; kapsam dışındaki işletmeler **isteğe bağlı** denetim yaptırabilir.',
        'TTK/KGK - bağımsız denetim kapsamı',
    ),
    # düzey 3
    '0054': patch(
        "Denetçi ve güvence ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Türkiye'de bağımsız denetçileri SPK (Sermaye Piyasası Kurulu) yetkilendirir.\n\nII. Denetim mutlak değil makul güvence sağlar.\n\nIII. Denetçi mesleki şüphecilikle hareket etmelidir.",
        {
            'A': 'Yalnız I',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'B',
        "**I yanlıştır:** Türkiye'de bağımsız denetçileri **SPK değil KGK (Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu)** yetkilendirir. **II** denetim mutlak değil makul güvence sağlar (doğru); **III** denetçi mesleki şüphecilikle hareket eder (doğru). Doğru cevap **II ve III**.",
        'Denetim - denetçi ve güvence',
    ),
    # düzey 2
    '0055': patch(
        'Aşağıdakilerden hangisi faaliyet (performans) denetiminin değerlendirdiği ölçütler arasında YER ALMAZ?',
        {
            'A': 'Finansal tabloların raporlama çerçevesine uygunluğu hakkında görüş bildirilmesi',
            'B': 'Faaliyetlerde kaynak israfının önlenmiş olup olmaması',
            'C': 'Kaynakların verimli kullanılması, yani girdi-çıktı ilişkisinin uygunluğu',
            'D': 'Belirlenen hedeflere ulaşma derecesi, yani etkililik',
            'E': 'Kaynakların ekonomik biçimde edinilip kullanılması',
        },
        'A',
        'Faaliyet denetimi **ekonomiklik, verimlilik ve etkililik (3E)** ölçütlerini değerlendirir. Finansal tabloların çerçeveye uygunluğu hakkında görüş bildirmek ise **finansal tablo denetiminin** konusudur; faaliyet denetiminin ölçütü değildir.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 3
    '0056': patch(
        'Denetim ile muhasebe arasındaki ilişki bakımından aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'Denetim süreci muhasebe süreci tamamlandıktan sonra başlar',
            'B': 'Denetçinin görevini yapabilmesi için muhasebe bilgisine sahip olması gerekir',
            'C': 'Denetim, muhasebe kayıtlarının oluşturulması ve tabloların düzenlenmesidir',
            'D': 'Denetim, finansal tablolardan kayıt ve belgelere doğru ters yönde ilerler',
            'E': 'Muhasebe işlemleri kaydedip raporlar, denetim bu raporların güvenilirliğini araştırır',
        },
        'C',
        'Kayıtları oluşturmak ve tabloları düzenlemek **muhasebenin (ve yönetimin)** işidir; denetim bu çıktıların güvenilirliğini bağımsız biçimde araştırır. Denetçi tabloları hazırlarsa kendi ürettiği bilgiyi denetlemiş olur. Diğer ifadeler doğrudur.',
        'Denetim - denetim kavramı ve türleri',
    ),
    # düzey 2
    '0057': patch(
        "Bir bağımsız denetçinin, hile riskine karşı denetim boyunca 'sorgulayıcı bir zihin' taşıması gerekliliği aşağıdaki hangi ilkenin gereğidir?",
        {
            'A': 'Mesleki şüphecilik',
            'B': 'Süreklilik',
            'C': 'Ücret pazarlığı',
            'D': 'Gizlilik',
            'E': 'Reklam serbestisi',
        },
        'A',
        'Denetim boyunca sorgulayıcı bir zihin taşımak, kanıtları eleştirel değerlendirmek ve hata/hile belirtilerine dikkat etmek **mesleki şüphecilik** ilkesinin gereğidir.',
        'BDS 200 - mesleki şüphecilik',
    ),
    # düzey 2
    '0058': patch(
        'İç denetçinin örgütsel bağımsızlığını güçlendirmek için genellikle hangi düzenleme yapılır?',
        {
            'A': 'İç denetim birimi, denetlediği birimlerden ayrı olarak denetim komitesine bağlanır',
            'B': 'İç denetçi bir birime bağlanmadan ve kimseye rapor vermeden kendi başına çalışır',
            'C': 'İç denetim birimi tamamen kaldırılır ve denetim görevi, denetlenecek bölümlerin kendi personeline ve amirlerine bırakılır',
            'D': 'İç denetim birimi, kendi denetleyeceği yürütme bölümünün altına bağlanır ve bulgularını doğrudan o bölümün yöneticisine rapor eder',
            'E': 'İç denetçi satış müdürüne bağlanır ve bulgularını satış birimine bildirir',
        },
        'A',
        'İç denetçinin örgütsel bağımsızlığı için iç denetim birimi, denetlediği yürütme birimlerinden **ayrı** olarak **üst yönetime/denetim komitesine (yönetim kuruluna)** bağlanır. Böylece tarafsız değerlendirme yapabilir.',
        'Denetim - iç denetim örgütlenmesi',
    ),
    # düzey 2
    '0059': patch(
        'Denetimin, işletmenin tüm işlemlerini tek tek incelemek yerine örnekleme yoluyla yürütülmesinin temel nedeni aşağıdakilerden hangisidir?',
        {
            'A': 'Denetimde kanıt toplamanın gereksiz olması ve yönetimin sunduğu beyanın tek başına yeterli kabul edilmesi',
            'B': 'Denetçinin tembel davranarak işlemlerin tamamını tek tek incelemekten kaçınmak istemesi ve işini kolaylaştırması',
            'C': 'Örneklemenin, işlemlerin tamamını incelemekten daha yüksek güvence sağlaması',
            'D': 'Yürürlükteki denetim mevzuatının, işlemlerin tamamının tek tek incelenmesini açıkça yasaklaması ve buna izin vermemesi',
            'E': 'Tam incelemenin zaman ve maliyet açısından elverişsiz olması; örneklemeyle makul güvenceye ulaşılabilmesi',
        },
        'E',
        'İşlem hacmi çok büyük olduğundan tüm işlemlerin tek tek incelenmesi (tam sayım) **zaman ve maliyet** açısından pratik değildir. Denetçi **örnekleme** ile makul güvenceye ulaşır. Bu, makul güvencenin de bir nedenidir.',
        'Denetim - örnekleme',
    ),
    # düzey 3
    '0060': patch(
        'Denetim kavramı, türleri ve denetçi ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Denetim, iddiaları ölçütlerle karşılaştırıp kanıta dayalı görüş bildiren sistematik süreçtir.\n\nII. Uygunluk denetimi faaliyetlerin kural/yasalara uygunluğunu; faaliyet denetimi ise etkinlik-verimlilik-ekonomikliği inceler.\n\nIII. İç denetim, bağımsız (dış) denetimin yerine geçer ve finansal tablolar hakkında üçüncü taraflara bağımsız denetim görüşü verir.',
        {
            'A': 'I ve III',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'Yalnız I',
            'E': 'I, II ve III',
        },
        'C',
        '**III yanlıştır:** İç denetim, bağımsız (dış) denetimin **yerine geçmez**; farklı amaç ve taraflara hizmet eder, üçüncü taraflara bağımsız denetim görüşü **vermez** (bu bağımsız denetimin işidir). İç denetim işletme içinden, yönetime bağlı yürütülüp öncelikle yönetime rapor verir. **I** denetim kanıta dayalı sistematik süreçtir (doğru); **II** uygunluk denetimi kural/yasa uygunluğu, faaliyet denetimi 3E (doğru). Doğru cevap **I ve II**.',
        'Denetim - kavram ve türler',
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
    print(f"1 paket / {len(PATCHES)} soru ('Denetim Kavrami' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
