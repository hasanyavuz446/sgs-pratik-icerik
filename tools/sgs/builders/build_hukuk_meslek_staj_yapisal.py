#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Staj ve Sinavlar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turunun 8. konusu; meslek_hukuku dersinin SON
konusu. Paketin 60 sorusunun TAMAMI yeniden yazildi.

    olcut                gercek   once   sonra
    medyan kok              257    115     185
    olumsuz kok           %41,5     %0     %40
    ayni kok kalibi           —  53/60       —
    kor ogrenci               —    %28       —
    boy egilimi               —  29/1        —

⚠️ ARA OLCUM DERSI: ilk tur 60 soruyu bitirdiginde medyan kok 115 -> 111'e
DUSMUSTU. Neden: son bolumde cok sayida kisa "tanima" sorusu yazilmisti. 26 kok
olay cercevesine tasinarak 185'e cikarildi — dolgu eklenmeden, her cumle surecin
hukuken anlamli bir adimini tasiyacak bicimde.

⚠️ SAHIPLIK DEVRI: fix_meslek_length_quality (37 soru) ve
build_legal_oncul_cleanup (staj-gen-0005) bu pakette soru tutuyordu; bloklari
CIKARILDI. fix_lexical_tell paket duzeyi mekanik listede yerinde birakildi.

IKI KAPI: §5 boy (ilk tasarim 44/60 = %73 cikip uretimi DURDURDU; iki turda 51
celdirici dogru sikla PARALEL yapiya tasinarak %20) · §1 bilissel duzey
(0 = 5 <=6, 0+1 = 14 <=24, duzey 2 = 33 >=24, duzey 3 = 13 >=12).

Dayanak: 3568 sayili Kanun md. 3, 4, 5, 6, 8, 9, 11, 12, 19 · TESMER ve staj
yonetmelikleri · 5786 sayili Kanun degisikligi · VUK mukerrer md. 227.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/meslek_hukuku/staj_ve_sinavlar.json"
STYLE_REF = "SGS Meslek Hukuku (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "staj-gen-"


def patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": "3568 sayili SMMM ve YMM Kanunu"},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        'Üç aday SMMM olmak için başvurmuştur: (A) medeni hakları kullanma ehliyetine sahip, hiçbir mahkûmiyeti bulunmayan lisans mezunu; (B) geçmişte kasten işlediği bir suçtan hüküm giymiş ancak cezası affa uğramış lisans mezunu; (C) disiplin soruşturması sonucu memuriyetten çıkarılmış lisans mezunu. Buna göre genel şartlar bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yalnızca A ve B genel şartları taşımaz',
            'B': 'A ve C genel şartları taşır',
            'C': 'Üç aday da genel şartları taşır',
            'D': 'A ve B genel şartları taşır',
            'E': 'Yalnızca A genel şartları taşır',
        },
        'E',
        "3568 md. 4: genel şartlar T.C. vatandaşlığı, medeni hakları kullanma ehliyeti, kamu haklarından mahrum bulunmamak, AFFA UĞRAMIŞ OLSA BİLE sayılan suçlardan hüküm giymemiş olmak ve ceza ya da disiplin soruşturması sonucu MEMURİYETTEN ÇIKARILMAMIŞ olmaktır. Af B'nin engelini kaldırmaz; C ise memuriyetten çıkarılma nedeniyle şartı taşımaz.",
    ),
    # düzey 3
    '0002': patch(
        'SMMM olmak isteyen üç aday: (A) işletme lisansı mezunu, (B) mühendislik lisansını tamamladıktan sonra muhasebe alanında yüksek lisans yapmış, (C) muhasebe ön lisans programı mezunu. Buna göre öğrenim şartı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İşletme lisansı mezunu A öğrenim şartını karşılar',
            'B': 'Ön lisans mezunu C, muhasebe alanında öğrenim gördüğü için öğrenim şartını karşılar',
            'C': 'Öğrenim şartı en az lisans düzeyini gerektirir',
            'D': 'Lisansı farklı alanda olanlar için ilgili dallarda lisansüstü diploma yeterli sayılır',
            'E': 'Muhasebe alanında yüksek lisans yapan B öğrenim şartını karşılar',
        },
        'B',
        '3568 md. 5/A-a: hukuk, iktisat, maliye, işletme, muhasebe, bankacılık, kamu yönetimi ve siyasal bilimler dallarında EN AZ LİSANS düzeyinde öğrenim görmüş olmak ya da bu dallar dışındaki lisans öğrenimini tamamlayıp bu alanlarda LİSANSÜSTÜ diploma almış olmak gerekir. ÖN LİSANS bu şartı karşılamaz.',
    ),
    # düzey 3
    '0003': patch(
        'Bir aday, lisans öğrenimini tamamlamış ve staja giriş sınavını kazanmıştır. Aday, iki yıllık staj sonunda doğrudan ruhsat alabileceğini düşünmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Staj süresi üç yıldır',
            'B': 'Ruhsat, genel ve özel şartların tamamını taşıyanlara verilir',
            'C': 'İki yıllık staj süresinin dolmasıyla aday doğrudan ruhsat almaya hak kazanır',
            'D': 'Staja giriş sınavını kazanmak tek başına unvan kazandırmaz',
            'E': 'Staj tamamlandıktan sonra ayrıca meslek yeterlilik sınavı kazanılmalıdır',
        },
        'C',
        '3568 md. 5/A: SMMM olabilmek için staj amacıyla ÜÇ YIL çalışmış olmak ve SMMM SINAVINI kazanmış olmak gerekir. İki yıllık süre yeterli değildir; staj tek başına ruhsat hakkı doğurmaz.',
    ),
    # düzey 2
    '0004': patch(
        'Meslek yeterlilik sınavı koşulu tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Serbest muhasebeci mali müşavir unvanı için meslek yeterlilik sınavının kazanılması gerekir',
            'B': 'Staja giriş sınavı ile meslek yeterlilik sınavı ayrı sınavlardır',
            'C': 'Sınavı kazanan adaya ruhsat verilir ve odaya kaydolur',
            'D': 'Stajını tamamlayan aday, ayrıca sınava girmeksizin ruhsat almaya hak kazanır',
            'E': 'Sınav, mesleki bilgi düzeyini ölçmeye yöneliktir',
        },
        'D',
        '3568 md. 5/A-c: serbest muhasebeci mali müşavirlik SINAVINI kazanmış olmak özel şartlardandır. Staja giriş sınavı stajın başlangıcına, meslek yeterlilik sınavı ise unvana kapı açar; ikisi farklı aşamalardır ve staj tek başına sınav yerine geçmez.',
    ),
    # düzey 2
    '0005': patch(
        'SMMM olmanın özel şartları ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. İlgili dallarda en az lisans düzeyinde öğrenim görmüş olmak gerekir. II. Staj amacıyla üç yıl çalışmış olmak gerekir. III. En az on yıl bir meslek mensubunun yanında çalışmış olmak gerekir.',
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'II ve III',
        },
        'A',
        "I ve II doğrudur (3568 md. 5/A-a ve b). III YANLIŞTIR: on yıllık çalışma şartı md. 6'da YEMİNLİ MALİ MÜŞAVİR olmak için aranır; SMMM için böyle bir şart yoktur.",
    ),
    # düzey 2
    '0006': patch(
        'Bir aday, meslek stajını nerede yapabileceğini araştırmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Staj, yeminli mali müşavir veya belirli kıdeme sahip serbest muhasebeci mali müşavir yanında yapılabilir',
            'B': 'Staj yeri konusunda bir sınırlama bulunmaz',
            'C': 'Staj yalnızca kamu kurumlarında yapılabilir',
            'D': 'Staj, yanında meslek mensubu bulunmasa dahi herhangi bir ticari işletmenin muhasebe biriminde yapılabilir',
            'E': 'Staj yalnızca yeminli mali müşavir yanında yapılabilir',
        },
        'A',
        '3568 md. 6 ve staj yönetmeliği: staj, yeminli mali müşavir ya da belirli kıdeme sahip serbest muhasebeci mali müşavir yanında yapılır; ayrıca mevzuatta öngörülen kurum ve kuruluşlarda geçen mesleki içerikli hizmetler stajdan sayılabilir. Herhangi bir işletmenin muhasebe biriminde geçen süre kendiliğinden staj sayılmaz.',
    ),
    # düzey 2
    '0007': patch(
        "TESMER'in staj sürecindeki rolü tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'TESMER, staj ve sınavın yanında sürekli mesleki eğitim faaliyetlerini de yürütür',
            'B': 'TESMER, TÜRMOB bünyesinde kurulmuş bir merkezdir',
            'C': 'TESMER staj işlemlerini ve aday eğitimini yürütür',
            'D': 'TESMER, meslek mensuplarına disiplin cezası veren bağımsız bir kuruldur',
            'E': 'Staja giriş sınavı TESMER aracılığıyla düzenlenir',
        },
        'D',
        "TESMER (Temel Eğitim ve Staj Merkezi), TÜRMOB bünyesinde staj, temel eğitim, sınav ve sürekli mesleki eğitim faaliyetlerini yürütür. DİSİPLİN yetkisi ise oda ve Birlik DİSİPLİN KURULLARINA aittir (3568 md. 21, 48); TESMER'in böyle bir yetkisi yoktur.",
    ),
    # düzey 2
    '0008': patch(
        'Bir aday, staja giriş sınavını kazanmadan doğrudan staja başlamak istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Staja giriş sınavı zorunlu olmayıp adayın tercihine bırakılmıştır',
            'B': 'Staja giriş sınavı yalnızca lisansüstü mezunları için öngörülmüştür',
            'C': 'Staja giriş sınavını kazanan aday meslek yeterlilik sınavından muaf olur',
            'D': 'Staja başlayabilmek için önce staja giriş sınavının kazanılması gerekir',
            'E': 'Staja giriş sınavı, staj tamamlandıktan sonra yapılır',
        },
        'D',
        '3568 md. 5 ve staj yönetmeliği: staja giriş sınavı, adayın üç yıllık meslek stajına başlayabilmesi için aranan ön aşamadır. Sınav zorunludur, öğrenim düzeyine göre değişmez ve meslek yeterlilik sınavından MUAFİYET sağlamaz.',
    ),
    # düzey 2
    '0009': patch(
        'Bir aday, stajına ara vermiş ve bir süre sonra kaldığı yerden devam etmek istemektedir. Buna göre staj süresinin hesabı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Staj süresi meslek mensubunun takdirine bırakılmıştır',
            'B': 'Staj süresi mevzuatta öngörülen esaslara göre hesaplanır; ara verilen dönemler süreye eklenmez',
            'C': 'Staj süresi adayın beyanına göre belirlenir',
            'D': 'Staja ara veren aday, önceki süreleri geçersiz sayılarak stajını baştan yapar',
            'E': 'Staj süresi takvim yılı esasına göre kesintisiz işler; ara verilen dönemler de süreye dâhil edilir',
        },
        'B',
        'Staj yönetmeliği: staj süresi fiilen çalışılan süreler üzerinden hesaplanır; ara verilen dönemler süreye dâhil edilmez. Ara verme stajı baştan yapmayı gerektirmez; aday kaldığı yerden devam eder. Süre ne adayın beyanına ne de meslek mensubunun takdirine bırakılmıştır.',
    ),
    # düzey 2
    '0010': patch(
        'Meslek stajının amaçları belirlenmektedir. Buna göre aşağıdakilerden hangisi bu amaçlardan biri değildir?',
        {
            'A': 'Adayın mesleki faaliyetten doğan mali sorumluluğunu üstlenmesini sağlamak',
            'B': 'Adayın mesleki uygulama becerisini geliştirmek',
            'C': 'Adayı mesleğin etik ilkeleriyle tanıştırmak',
            'D': 'Adayı mevzuatın uygulanışı ve yerleşik mesleki teamüller konusunda yetiştirmek',
            'E': 'Adaya mesleki bilgi ve deneyim kazandırmak',
        },
        'A',
        'Stajın amacı adaya mesleki bilgi, deneyim, uygulama becerisi ve etik anlayış kazandırmaktır. Aday henüz meslek mensubu olmadığından mesleki faaliyetten doğan MALİ SORUMLULUĞU üstlenmesi söz konusu değildir; sorumluluk yanında staj yaptığı meslek mensubuna aittir.',
    ),
    # düzey 2
    '0011': patch(
        'Staja giriş sınavının düzenlenmesi ve amacı tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sınav, meslek yeterlilik sınavından ayrı bir aşamadır',
            'B': 'Sınav TÜRMOB/TESMER aracılığıyla düzenlenir',
            'C': 'Sınavı kazanmak tek başına unvan kazandırmaz',
            'D': 'Staja giriş sınavı, adayın mesleki yeterliğini ölçerek unvan kazanmasını sağlar',
            'E': 'Staja giriş sınavı, adayın staja başlayabilmesi için aranan temel bilgi düzeyini ölçer',
        },
        'D',
        'Staja giriş sınavı adayın staja başlayabilmesi için gereken TEMEL BİLGİ düzeyini ölçer; unvan kazandırmaz. Mesleki yeterliği ölçen ve unvana kapı açan sınav, staj tamamlandıktan sonra girilen MESLEK YETERLİLİK SINAVIDIR (3568 md. 5/A-c).',
    ),
    # düzey 2
    '0012': patch(
        'Üç yıllık stajını tamamlayan bir aday, unvanını kazanmak için gireceği sınavı ve bu sınavın hangi aşamada olduğunu belirlemektedir. Buna göre SMMM meslek yeterlilik sınavı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sınavı kazanmak zorunlu olmayıp staj tek başına yeterlidir',
            'B': 'Meslek yeterlilik sınavı yalnızca yeminli mali müşavir adayları için düzenlenir',
            'C': 'Sınav, stajını tamamlayan adayın mesleki yeterliğini ölçer ve unvana kapı açar',
            'D': 'Sınav, staja başlamadan önce girilen bir sınavdır',
            'E': 'Sınav, meslek odasınca her aday için ayrı ayrı düzenlenir',
        },
        'C',
        '3568 md. 5/A-c: SMMM unvanı için meslek yeterlilik sınavının kazanılması gerekir. Sınav staj tamamlandıktan sonra girilir, TÜRMOB/TESMER tarafından merkezî olarak düzenlenir ve staj yerine geçmez.',
    ),
    # düzey 2
    '0013': patch(
        'Meslek sınavında başarısız olan bir aday, yeniden sınava girmek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Başarısız olan adayın sınav hakkı tümüyle sona erer',
            'B': 'Adaya mevzuatta öngörülen sayı ve süre sınırları içinde yeniden sınav hakkı tanınır',
            'C': 'Aday sınırsız sayıda ve süresiz olarak sınava girebilir',
            'D': 'Aday yeniden sınava girmek için stajını tekrarlamalıdır',
            'E': 'Yeniden sınava girme hakkı yalnızca oda yönetim kurulunun izniyle kullanılabilir',
        },
        'B',
        'Sınav yönetmeliği: başarısız olan adaya belirlenen sayı ve süre sınırları içinde yeniden sınav hakkı tanınır. Hak ne tümüyle sona erer ne de sınırsızdır; stajın tekrarı da gerekmez.',
    ),
    # düzey 2
    '0014': patch(
        'Meslek sınavlarının kapsadığı konular belirlenmektedir. Buna göre aşağıdakilerden hangisi bu konular arasında yer almaz?',
        {
            'A': 'Muhasebe ve mali tablolar',
            'B': 'Vergi mevzuatı ve uygulaması ile vergi usul hükümleri',
            'C': 'Denetim ve mesleki etik',
            'D': 'Hukuk ve meslek hukuku',
            'E': 'Adayın kişisel mali durumu ve sermaye yeterliği',
        },
        'E',
        'Meslek sınavları muhasebe, mali tablolar analizi, vergi mevzuatı, hukuk, meslek hukuku, denetim ve mesleki etik gibi mesleki alanları kapsar. Adayın KİŞİSEL MALİ DURUMU sınav konusu değildir; 3568 md. 4-5 sermaye ya da teminat şartı da öngörmez.',
    ),
    # düzey 3
    '0015': patch(
        'Meslek mensubu olma süreci ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Staja giriş sınavı, staja başlamak için aranan aşamadır. II. Meslek yeterlilik sınavı staj tamamlandıktan sonra girilir. III. Sınavı kazanan aday ruhsat almadan mesleki faaliyette bulunabilir. IV. Staja giriş sınavını kazanmak SMMM unvanı kazandırır.',
        {
            'A': 'III ve IV',
            'B': 'I, III ve IV',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'Yalnız III',
        },
        'A',
        'III YANLIŞ: mesleki faaliyet için ruhsat ve oda kaydı gerekir (3568 md. 5, 19). IV YANLIŞ: staja giriş sınavı yalnızca stajın başlangıcına kapı açar; unvan için staj ve meslek yeterlilik sınavı gerekir. I ve II doğrudur.',
    ),
    # düzey 3
    '0016': patch(
        'Sekiz yıldır SMMM olarak çalışan bir meslek mensubu, yeminli mali müşavir olmak için başvurmak istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'On yıllık çalışma süresi şartı yalnızca lisansüstü diploması bulunmayan adaylar için aranır',
            'B': 'YMM olmak için çalışma süresi aranmaz; yalnızca sınav yeterlidir',
            'C': 'En az on yıllık çalışma şartı gerçekleşmediğinden başvuru koşulları henüz oluşmamıştır',
            'D': 'Sekiz yıllık çalışma yeterlidir; aday doğrudan YMM sınavına girebilir',
            'E': 'On yıllık süre, adayın stajda geçirdiği süreyi de kapsar',
        },
        'C',
        '3568 md. 6: yeminli mali müşavir olabilmek için en az ON YIL serbest muhasebeci mali müşavirlik yapmış olmak, YMM sınavını vermiş olmak ve YMM ruhsatını almış olmak gerekir. Süre, SMMM olarak FİİLEN çalışılan süredir; stajda geçen süre buna dâhil değildir.',
    ),
    # düzey 3
    '0017': patch(
        'Kanunları uyarınca vergi inceleme yetkisini almış ve bu yetkiyi uzun süre kullanmış bir kişi ile hukuk alanında profesör unvanı almış bir akademisyen, YMM olmak için başvurmuştur. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'YMM sınavından muafiyet yalnızca vergi inceleme yetkisini almış olanlar için öngörülmüştür',
            'B': 'Muafiyet yalnızca profesör unvanı alanlar için öngörülmüştür',
            'C': 'Kanunda sayılan koşulları taşımaları hâlinde her ikisi de YMM sınavından muaf tutulabilir',
            'D': 'YMM sınavından muafiyet hiçbir grup için öngörülmemiştir',
            'E': "Muafiyet, on yıllık SMMM'lik şartını da ortadan kaldırır",
        },
        'C',
        '3568 md. 9: kanunları uyarınca vergi inceleme yetkisini almış olup belirtilen süreyi tamamlayanlar ile hukuk, iktisat, maliye, işletme, muhasebe, bankacılık, kamu yönetimi ve siyasal bilimler dallarında PROFESÖRLÜK unvanı almış olanlar YMM SINAVINDAN muaf tutulur. Muafiyet yalnızca sınava ilişkindir; diğer şartlar ayrıca aranır.',
    ),
    # düzey 3
    '0018': patch(
        'Meslek yeterlilik sınavını kazanan bir aday, ruhsatını almadan ve odaya kaydolmadan büro açıp mesleki faaliyete başlamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Faaliyet, yalnızca vergi dairesine işe başlama bildirimi yapılmışsa hukuka uygundur',
            'B': 'Oda kaydı yeterlidir; ruhsat sonradan alınabilir',
            'C': 'Ruhsat yeterlidir; oda kaydı sonradan yapılabilir',
            'D': 'Sınavı kazanmak mesleki faaliyet için yeterlidir',
            'E': 'Mesleki faaliyet için ruhsat ve oda kaydı gerektiğinden bu faaliyet hukuka aykırıdır',
        },
        'E',
        '3568 md. 5 ve 19: sınavı kazanan ve genel şartları taşıyan adaya RUHSAT verilir; meslek mensubu mesleki faaliyette bulunabilmek için ayrıca bölgesindeki ODAYA KAYDOLUR. İki adım da tamamlanmadan mesleki faaliyet yürütülemez; md. 3 unvan ve yetkilerin ruhsatsız kullanılmasını yasaklar.',
    ),
    # düzey 2
    '0019': patch(
        'Meslek mensubu olma sürecinin adımları sıralanmaktadır. Buna göre doğru sıralama aşağıdakilerden hangisidir?',
        {
            'A': 'Öğrenim → ruhsat → staja giriş sınavı → üç yıllık staj → meslek yeterlilik sınavı',
            'B': 'Öğrenim → üç yıllık staj → staja giriş sınavı → meslek yeterlilik sınavı → ruhsat ve oda kaydı',
            'C': 'Staja giriş sınavı → öğrenim → meslek yeterlilik sınavı → üç yıllık staj → ruhsat',
            'D': 'Öğrenim → meslek yeterlilik sınavı → staja giriş sınavı → üç yıllık staj → ruhsat',
            'E': 'Öğrenim → staja giriş sınavı → üç yıllık staj → meslek yeterlilik sınavı → ruhsat ve oda kaydı',
        },
        'E',
        '3568 md. 4, 5 ve 8: aday önce öğrenim şartını karşılar, staja giriş sınavını kazanır, üç yıllık stajı tamamlar, meslek yeterlilik sınavını kazanır ve son olarak ruhsat alıp odaya kaydolur.',
    ),
    # düzey 2
    '0020': patch(
        'Yeminli mali müşavirlik ruhsatını alan bir meslek mensubu, yemin etmeden tasdik işlerine başlamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yemin yükümlülüğü ruhsat alındıktan sonra beş yıl içinde yerine getirilir',
            'B': 'Yemin yükümlülüğü serbest muhasebeci mali müşavirler için de öngörülmüş olup ruhsat öncesinde yerine getirilir',
            'C': 'Yeminli mali müşavirler mesleki faaliyete başlamadan önce yemin etmekle yükümlüdür',
            'D': 'Yemin yükümlülüğü kaldırılmış olup yerini yazılı taahhüt almıştır',
            'E': 'Yemin, her tasdik işi için ayrı ayrı edilir',
        },
        'C',
        '3568 md. 11: yeminli mali müşavirler mesleki faaliyete başlamadan ÖNCE yemin ederler. Yemin bir kez edilir, YMM unvanına özgüdür ve serbest muhasebeci mali müşavirler için öngörülmemiştir.',
    ),
    # düzey 2
    '0021': patch(
        'Bir kişi, mesleğe yeni girmek için serbest muhasebeci unvanını kullanmak istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bu unvanla mesleğe giriş sürmekte olup unvan yalnızca lisans mezunu olmayan adaylar tarafından kullanılmaktadır',
            'B': 'Bu unvanla mesleğe yeni giriş kapanmış olup mevcut serbest muhasebecilerin kazanılmış hakları korunmuştur',
            'C': 'Bu unvanla mesleğe giriş hâlen mümkündür',
            'D': 'Unvan tümüyle kaldırılmış olup kazanılmış hak tanınmamıştır',
            'E': 'Unvan, yeminli mali müşavirliğe geçiş için ara basamak olarak korunmuştur',
        },
        'B',
        "5786 sayılı Kanun'la 3568 sayılı Kanun'da yapılan değişiklikten sonra SERBEST MUHASEBECİ unvanıyla mesleğe YENİ GİRİŞ kapanmıştır. O tarihte unvanı taşıyanların kazanılmış hakları korunmuş; şartları taşıyanlara SMMM unvanına geçiş imkânı tanınmıştır.",
    ),
    # düzey 3
    '0022': patch(
        'Mevzuatta öngörülen kurumlarda mesleki içerikli görevlerde bulunmuş bir aday, bu sürelerin stajdan sayılmasını istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sürelerin stajdan sayılıp sayılmayacağını, yanında staj yapılan meslek mensubu tek başına takdir eder',
            'B': 'Her türlü çalışma süresi kendiliğinden stajdan sayılır',
            'C': 'Hiçbir önceki hizmet stajdan sayılmaz',
            'D': 'Süreler yalnızca kamu görevlileri için sayılabilir',
            'E': 'Mevzuatta öngörülen mesleki içerikli hizmetlerde geçen süreler, koşulları varsa stajdan sayılabilir',
        },
        'E',
        '3568 md. 6 ve staj yönetmeliği: kanunda ve yönetmelikte sayılan mesleki içerikli görevlerde geçen süreler, öngörülen koşullar gerçekleştiğinde stajdan SAYILABİLİR. Bu ne kendiliğinden olur ne de meslek mensubunun takdirine bırakılmıştır; TESMER/TÜRMOB değerlendirir.',
    ),
    # düzey 2
    '0023': patch(
        'Bir aday, stajını sürdürürken aynı zamanda ticari bir işletme işletmek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ticari faaliyet yasağı yalnızca yeminli mali müşavirler için geçerlidir',
            'B': 'Aday, ticari faaliyeti odaya bildirirse staj süresi iki katına çıkar',
            'C': 'Aday, ticari faaliyet yürütürse stajı kendiliğinden iptal edilir',
            'D': 'Staj döneminde de mesleğin gerekleriyle bağdaşmayan faaliyetlerden kaçınılması beklenir',
            'E': 'Aday henüz meslek mensubu olmadığından staj döneminde hiçbir sınırlamaya tabi değildir',
        },
        'D',
        'Staj yönetmeliği: staj, adayın mesleği öğrenmesine ayrılmış bir dönemdir ve mesleğin gerekleriyle bağdaşmayan faaliyetlerden kaçınılması beklenir. Sınırlama bulunmadığını söylemek yanlıştır; öte yandan yaptırım kendiliğinden iptal değil, yönetmelikteki değerlendirmeye bağlıdır.',
    ),
    # düzey 2
    '0024': patch(
        'Bir aday, staj süresince yanında çalıştığı meslek mensubunun sorumluluğunu tartışmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sorumluluk yalnızca odaya aittir',
            'B': 'Staj döneminde hiç kimsenin sorumluluğu doğmaz',
            'C': 'Sorumluluk stajyer adaya aittir',
            'D': 'Mesleki işlerden doğan sorumluluk aday ile meslek mensubu arasında eşit olarak paylaşılır',
            'E': 'Mesleki işlerden doğan sorumluluk, yanında staj yapılan meslek mensubuna aittir',
        },
        'E',
        'Stajyer aday henüz ruhsat sahibi meslek mensubu değildir; imza ve tasdik yetkisi yoktur. Mesleki işlerden doğan sorumluluk, işi yürüten ve imzalayan MESLEK MENSUBUNA aittir (VUK mükerrer md. 227, 3568 md. 12).',
    ),
    # düzey 2
    '0025': patch(
        'Bir aday, SMMM ve YMM unvanları için aranan özel şartları birbirine karıştırmıştır. Buna göre meslek mensubu olma şartları bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'SMMM olabilmek için meslek yeterlilik sınavını kazanmak gerekir',
            'B': 'SMMM olabilmek için üç yıl staj yapmış olmak gerekir',
            'C': 'SMMM olabilmek için en az on yıl bir meslek mensubunun yanında çalışmış olmak gerekir',
            'D': 'YMM olabilmek için en az on yıl SMMM olarak çalışmış olmak gerekir',
            'E': 'SMMM olabilmek için kanunda sayılan dallarda en az lisans düzeyinde öğrenim görmüş olmak gerekir',
        },
        'C',
        "3568 md. 5: SMMM'nin özel şartları öğrenim, ÜÇ YILLIK staj, sınav ve ruhsattır. ON YILLIK çalışma şartı md. 6'da YEMİNLİ MALİ MÜŞAVİR olmak için aranır.",
    ),
    # düzey 2
    '0026': patch(
        'Mesleğe girmek isteyen bir aday, unvandan bağımsız olarak herkesten aranan koşulları listelemektedir. Buna göre genel şartlar bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Medeni hakları kullanma ehliyetine sahip olmak genel şartlardandır',
            'B': 'Belirli bir tutarın üzerinde sermaye veya teminat göstermiş olmak genel şartlardandır',
            'C': 'Sayılan suçlardan hüküm giymemiş olmak, ceza affa uğramış olsa da aranır',
            'D': 'Ceza veya disiplin soruşturması sonucunda memuriyetten çıkarılmamış olmak genel şartlardandır',
            'E': 'Kamu haklarından mahrum bulunmamak genel şartlardandır',
        },
        'B',
        '3568 md. 4: genel şartlar vatandaşlık, medeni hakları kullanma ehliyeti, kamu haklarından mahrum bulunmama, sayılan suçlardan hüküm giymemiş olma (affa uğramış olsa dahi) ve memuriyetten çıkarılmamış olmadır. SERMAYE ya da TEMİNAT şartı öngörülmemiştir.',
    ),
    # düzey 2
    '0027': patch(
        'Bir aday, stajını nerede ve ne kadar süreyle yapacağını, ayrıca staja başlamak için hangi sınavı kazanması gerektiğini araştırmaktadır. Buna göre staj bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Staja başlamak için staja giriş sınavının kazanılması gerekir',
            'B': 'Staj süresi üç yıldır',
            'C': 'Mevzuatta öngörülen mesleki hizmetler stajdan sayılabilir',
            'D': 'Staj süresi iki yıl olup staja giriş sınavı aranmaz',
            'E': 'Staj, yeminli mali müşavir veya belirli kıdeme sahip SMMM yanında yapılabilir',
        },
        'D',
        '3568 md. 5/A-b: staj amacıyla ÜÇ YIL çalışmış olmak gerekir; staja başlamak için ayrıca staja giriş sınavının kazanılması aranır.',
    ),
    # düzey 2
    '0028': patch(
        'Staja giriş sınavını kazanan bir aday ile stajını tamamlamış bir başka aday, gireceği sınavları ve haklarını karşılaştırmaktadır. Buna göre sınavlar bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Staja giriş sınavını kazanan aday meslek yeterlilik sınavından muaf tutulur',
            'B': 'Başarısız olan adaya, mevzuattaki sayı ve süre sınırları içinde yeniden sınav hakkı tanınır',
            'C': 'Sınavlar TÜRMOB/TESMER aracılığıyla düzenlenir',
            'D': 'Staja giriş sınavı ile meslek yeterlilik sınavı ayrı aşamalardır',
            'E': 'Meslek yeterlilik sınavı, üç yıllık staj süresi tamamlandıktan sonra girilir ve unvana kapı açar',
        },
        'A',
        'Staja giriş sınavı stajın başlangıcına, meslek yeterlilik sınavı ise unvana kapı açar. İkisi AYRI aşamalardır; birini kazanmak diğerinden MUAFİYET sağlamaz (3568 md. 5/A-b ve c).',
    ),
    # düzey 2
    '0029': patch(
        'On yıldır serbest muhasebeci mali müşavir olarak çalışan bir meslek mensubu ile mesleğe yeni giren bir aday, yeminli mali müşavirlik koşullarını değerlendirmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kanunda sayılan bazı gruplar YMM sınavından muaf tutulabilir',
            'B': 'Yeminli mali müşavirlik unvanı, staj tamamlandıktan sonra doğrudan kazanılabilir',
            'C': "YMM'ler mesleki faaliyete başlamadan önce yemin eder",
            'D': 'Yeminli mali müşavir olmak için en az on yıl SMMM olarak çalışmış olmak gerekir',
            'E': 'YMM olmak için YMM sınavını vermiş olmak gerekir',
        },
        'B',
        '3568 md. 6: yeminli mali müşavirlik doğrudan kazanılamaz; en az ON YIL SMMM olarak çalışmış olmak, YMM sınavını vermek ve ruhsat almak gerekir. md. 9 bazı gruplara yalnızca SINAV muafiyeti tanır.',
    ),
    # düzey 2
    '0030': patch(
        'Meslek yeterlilik sınavını kazanan bir aday, faaliyete başlayabilmek için tamamlaması gereken son adımları belirlemektedir. Buna göre ruhsat ve oda kaydı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kanunda sayılan unvan ve yetkiler, ruhsat sahibi olmayanlarca kullanılamaz',
            'B': 'Ruhsat, genel ve özel şartların tamamını taşıyanlara verilir',
            'C': 'Ruhsat alan meslek mensubunun ayrıca odaya kaydolmasına gerek yoktur',
            'D': 'Meslek mensubu mesleki faaliyet için bölgesindeki odaya kaydolur',
            'E': 'Ruhsat hem SMMM hem YMM için düzenlenir',
        },
        'C',
        '3568 md. 19: meslek mensupları mesleki faaliyette bulunabilmek için bölgesi içinde bulundukları ODAYA KAYDOLMAK zorundadır. Ruhsat tek başına faaliyet için yeterli değildir.',
    ),
    # düzey 2
    '0031': patch(
        'Staj ve sınavlar ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Staj süresi üç yıldır. II. TESMER, TÜRMOB bünyesinde staj ve eğitim işlemlerini yürütür. III. Staja giriş sınavı, meslek yeterlilik sınavından muafiyet sağlar.',
        {
            'A': 'I ve III',
            'B': 'I, II ve III',
            'C': 'II ve III',
            'D': 'Yalnız I',
            'E': 'I ve II',
        },
        'E',
        'I doğrudur (3568 md. 5/A-b). II doğrudur. III YANLIŞTIR: iki sınav ayrı aşamalardır ve biri diğerinden muafiyet sağlamaz.',
    ),
    # düzey 3
    '0032': patch(
        'Genel ve özel şartlar ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Kamu haklarından mahrum bulunmamak genel şartlardandır. II. Affa uğramış mahkûmiyet, mesleğe girişe engel oluşturmaz. III. SMMM olabilmek için üç yıl staj gerekir. IV. Genel şartlar arasında belirli bir sermaye tutarı gösterme yer alır.',
        {
            'A': 'II ve III',
            'B': 'I, II ve IV',
            'C': 'I ve III',
            'D': 'II ve IV',
            'E': 'Yalnız II',
        },
        'D',
        "II YANLIŞ: 3568 md. 4 sayılan suçlardan mahkûmiyeti 'affa uğramış olsa bile' engel sayar. IV YANLIŞ: genel şartlar arasında sermaye ya da teminat gösterme yoktur. I ve III doğrudur.",
    ),
    # düzey 0
    '0033': patch(
        'Lisans öğrenimini tamamlamış ve staja giriş sınavını kazanmış bir aday, mesleğe giriş takvimini planlamaktadır. Buna göre serbest muhasebeci mali müşavir olabilmek için aranan staj süresi kaç yıldır?',
        {
            'A': 'Üç yıl',
            'B': 'On yıl',
            'C': 'Bir yıl',
            'D': 'Beş yıl',
            'E': 'İki yıl',
        },
        'A',
        "3568 md. 5/A-b: serbest muhasebeci mali müşavir olabilmek için staj amacıyla ÜÇ YIL çalışmış olmak gerekir. On yıl ise md. 6'da YMM olmak için aranan SMMM'lik süresidir.",
    ),
    # düzey 0
    '0034': patch(
        'Yeminli mali müşavir olabilmek için aranan serbest muhasebeci mali müşavirlik süresi kaç yıldır?',
        {
            'A': 'Beş yıl',
            'B': 'On beş yıl',
            'C': 'Üç yıl',
            'D': 'On yıl',
            'E': 'Yedi yıl',
        },
        'D',
        '3568 md. 6: yeminli mali müşavir olabilmek için en az ON YIL serbest muhasebeci mali müşavirlik yapmış olmak gerekir.',
    ),
    # düzey 0
    '0035': patch(
        'TÜRMOB bünyesinde staj ve mesleki eğitim faaliyetlerini yürüten birim aşağıdakilerden hangisidir?',
        {
            'A': 'TESK',
            'B': 'TOBB',
            'C': 'SPK',
            'D': 'TESMER',
            'E': 'KGK',
        },
        'D',
        'TESMER (Temel Eğitim ve Staj Merkezi), TÜRMOB bünyesinde staj, temel eğitim, sınav hazırlığı ve sürekli mesleki eğitim faaliyetlerini yürütür.',
    ),
    # düzey 0
    '0036': patch(
        'Meslek mensubunun mesleki faaliyete başlayabilmesi için ruhsatın yanında gereken işlem aşağıdakilerden hangisidir?',
        {
            'A': 'Ticaret siciline tescil olmak',
            'B': 'Vergi dairesinden yetki belgesi almak',
            'C': 'Bakanlıktan onay almak',
            'D': 'Kamu Gözetimi Kurumundan izin almak',
            'E': 'Bölgesindeki odaya kaydolmak',
        },
        'E',
        '3568 md. 19: meslek mensupları mesleki faaliyette bulunabilmek için bölgesi içinde bulundukları ODAYA KAYDOLMAK zorundadır. Ruhsat tek başına yeterli değildir.',
    ),
    # düzey 0
    '0037': patch(
        'Yeminli mali müşavirlerin mesleki faaliyete başlamadan önce yerine getirmesi gereken yükümlülük aşağıdakilerden hangisidir?',
        {
            'A': 'Bağımsız denetçi belgesi almak',
            'B': 'Teminat yatırmak',
            'C': 'Yemin etmek',
            'D': 'Ticaret siciline tescil olmak',
            'E': 'Sermaye taahhüdünde bulunmak',
        },
        'C',
        '3568 md. 11: yeminli mali müşavirler mesleki faaliyete başlamadan önce YEMİN ederler. Yemin YMM unvanına özgüdür ve bir kez edilir.',
    ),
    # düzey 3
    '0038': patch(
        'Bir aday staja giriş sınavını kazanmış, iki yıl staj yapmış ve ardından meslek yeterlilik sınavına başvurmuştur. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sınava giremez; ayrıca stajını baştan yapması gerekir',
            'B': 'Üç yıllık staj süresi tamamlanmadığı için aday meslek yeterlilik sınavına giremez',
            'C': 'Sınava girebilir; staja giriş sınavı staj süresinin yerine geçer',
            'D': 'Sınava girebilir; iki yıllık staj süresi lisans mezunu adaylar için yeterli sayılır',
            'E': 'Sınava girebilir; staj süresi sınav sonrasında tamamlanabilir',
        },
        'B',
        '3568 md. 5/A: SMMM olabilmek için ÜÇ YIL staj yapmış OLMAK ve ardından sınavı kazanmak gerekir; sıralama değiştirilemez. Ancak eksik süre stajın baştan yapılmasını gerektirmez, aday kalan süreyi tamamlar.',
    ),
    # düzey 1
    '0039': patch(
        'Stajını sürdüren bir aday, staj kayıtlarının kim tarafından tutulduğunu ve sürecin kimin denetiminde yürüdüğünü öğrenmek istemektedir. Buna göre meslek stajının denetimi ve kaydı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Staj denetimi Kamu Gözetimi Kurumuna aittir',
            'B': 'Staj için herhangi bir kayıt tutulmaz',
            'C': 'Staj yalnızca yanında staj yapılan meslek mensubunca izlenir',
            'D': 'Staj denetimi Hazine ve Maliye Bakanlığınca yürütülür',
            'E': 'Staj, TESMER/TÜRMOB tarafından izlenir ve kayıt altına alınır',
        },
        'E',
        'Staj yönetmeliği: staj TESMER/TÜRMOB tarafından izlenir, değerlendirilir ve kayıt altına alınır. Yanında staj yapılan meslek mensubu da izlemede rol alır; ancak denetim münhasıran ona bırakılmamıştır.',
    ),
    # düzey 1
    '0040': patch(
        'Staja giriş sınavını kazanan bir aday, stajına hemen başlamak istemekte ve öncelikle hangi adımı tamamlaması gerektiğini belirlemeye çalışmaktadır. Buna göre stajın başlatılabilmesi için aşağıdakilerden hangisi gereklidir?',
        {
            'A': 'Bağımsız denetçi belgesi almak',
            'B': 'Stajını yapacağı meslek mensubu ve staj yeri konusunda mevzuattaki koşulları sağlamak',
            'C': 'Ticaret siciline tescil olmak',
            'D': 'Bölgesindeki odaya meslek mensubu olarak kaydolup ruhsatını ibraz etmek ve levhaya yazılmak',
            'E': 'Ruhsat almak',
        },
        'B',
        'Staj yönetmeliği: staja giriş sınavını kazanan aday, mevzuatta öngörülen koşulları taşıyan bir meslek mensubu yanında ve uygun bir staj yerinde stajına başlar. Ruhsat ve oda kaydı ise sürecin SONUNDA, sınav kazanıldıktan sonra gerçekleşir.',
    ),
    # düzey 1
    '0041': patch(
        'Bir adayın staj dosyası TESMER tarafından incelenmiş ve mevzuata aykırı bir kayıt tespit edilmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Aykırılık hiçbir sonuç doğurmaz',
            'B': 'Aykırılık kendiliğinden stajın tümünü geçersiz kılar',
            'C': 'Tespit edilen aykırılık, adayın ruhsatının geri alınması ve stajın iptali sonucunu doğurur',
            'D': 'Aykırılık yalnızca meslek mensubunu bağlar',
            'E': 'Aykırılık, stajın geçerliliği bakımından yönetmelikteki esaslara göre değerlendirilir',
        },
        'E',
        'Staj yönetmeliği aykırılıkların değerlendirilmesi ve sonuçlarını düzenler; sonuç kendiliğinden tam geçersizlik değildir. Aday henüz ruhsat sahibi olmadığı için ruhsatın geri alınması da söz konusu olamaz.',
    ),
    # düzey 2
    '0042': patch(
        'Meslek yeterlilik sınavına hazırlanan bir aday, sınavın hangi alanları kapsadığını ve nelere çalışması gerektiğini belirlemektedir. Buna göre meslek yeterlilik sınavının kapsamı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sınav, muhasebe ve mali tabloların düzenlenmesi ile analizini kapsar',
            'B': 'Sınav denetim ve mesleki etiği kapsar',
            'C': 'Sınav hukuk ve meslek hukukunu kapsar',
            'D': 'Sınav yalnızca muhasebe alanındaki bilgileri ölçer',
            'E': 'Sınav vergi mevzuatını kapsar',
        },
        'D',
        'Meslek yeterlilik sınavı muhasebe ve mali tablolar, vergi mevzuatı, hukuk, meslek hukuku, denetim ve mesleki etik gibi geniş bir mesleki alanı kapsar; tek bir alanla sınırlı değildir.',
    ),
    # düzey 1
    '0043': patch(
        'Lisans öğrenimini yeni tamamlayan bir aday, staja giriş sınavına başvurabilmek için gereken öğrenim koşulunu araştırmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Herhangi bir öğrenim şartı aranmaz',
            'B': 'Adayın ilgili dallarda en az lisans düzeyinde öğrenim şartını taşıması gerekir',
            'C': 'Lisansüstü diploma zorunludur',
            'D': 'Ön lisans mezunu olmak yeterlidir',
            'E': 'Yalnızca muhasebe lisansı kabul edilir; diğer lisans dalları öğrenim şartını karşılamaz',
        },
        'B',
        '3568 md. 5/A-a: hukuk, iktisat, maliye, işletme, muhasebe, bankacılık, kamu yönetimi ve siyasal bilimler dallarında en az LİSANS düzeyinde öğrenim ya da bu dallar dışındaki lisansın ardından bu alanlarda lisansüstü diploma aranır.',
    ),
    # düzey 2
    '0044': patch(
        'Bir meslek mensubu, yanında staj yapan adayın hazırladığı beyannameleri adayın kendi adına imzalamasını istemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Stajyer adayın imza yetkisi, staj süresinin yarısı dolduğunda kendiliğinden doğar',
            'B': 'Stajyer aday kendi adına beyanname imzalayabilir',
            'C': 'İmza yetkisi odaya bildirimle kazanılır',
            'D': 'Stajyer adayın imza ve tasdik yetkisi bulunmaz; işleri meslek mensubu imzalar',
            'E': 'Stajyer aday meslek mensubu adına imza atabilir',
        },
        'D',
        'Stajyer aday henüz ruhsat sahibi meslek mensubu değildir; 3568 md. 3 unvan ve yetkilerin ruhsatsız kullanılmasını yasaklar. İmza ve tasdik yetkisi yalnızca ruhsatlı meslek mensubuna aittir ve süre ya da bildirimle doğmaz.',
    ),
    # düzey 2
    '0045': patch(
        'Staja giriş sınavını kazanan bir aday, stajı atlayarak doğrudan meslek yeterlilik sınavına girmenin mümkün olup olmadığını sormaktadır. Buna göre staj ve mesleğe giriş bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek yeterlilik sınavı, üç yıllık staj süresi tamamlandıktan sonra girilir ve unvana kapı açar',
            'B': 'Staja giriş sınavını kazanan aday, dilerse stajı atlayıp doğrudan meslek yeterlilik sınavına girebilir',
            'C': 'Staj TESMER/TÜRMOB tarafından izlenir',
            'D': 'Ruhsat ve oda kaydı sürecin son adımıdır',
            'E': 'Staj süresi üç yıldır',
        },
        'B',
        '3568 md. 5/A: staj ve sınav ayrı ve SIRALI koşullardır; staj atlanarak meslek yeterlilik sınavına girilemez.',
    ),
    # düzey 2
    '0046': patch(
        'Vergi inceleme yetkisini uzun süre kullanmış bir kişi, YMM sınavından muaf tutulacağını ve başka hiçbir koşul aranmayacağını düşünmektedir. Buna göre YMM sınavından muafiyet bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Muafiyet için kanunda öngörülen koşulların taşınması gerekir',
            'B': 'Muafiyet, on yıllık serbest muhasebeci mali müşavirlik şartını da ortadan kaldırır',
            'C': 'Kanunları uyarınca vergi inceleme yetkisi almış olanlar için muafiyet öngörülmüştür',
            'D': 'İlgili dallarda profesörlük unvanı almış olanlar için muafiyet öngörülmüştür',
            'E': 'Muafiyet yalnızca sınava ilişkindir',
        },
        'B',
        '3568 md. 9: sayılan gruplar YMM SINAVINDAN muaf tutulur. Muafiyet yalnızca sınava ilişkindir; diğer şartlar (ruhsat, yemin ve ilgili hâllerde çalışma süresi) ayrıca aranır.',
    ),
    # düzey 1
    '0047': patch(
        'Stajına yeni başlayan bir aday, staj döneminde hangi işleri kendi başına yürütebileceğini sormaktadır. Buna göre meslek stajı süresince adayın temel yükümlülüğü aşağıdakilerden hangisidir?',
        {
            'A': 'Bağımsız olarak beyanname imzalamak',
            'B': 'Kendi adına müşteri kabul etmek',
            'C': 'Tasdik işlerini yürütmek',
            'D': 'Yanında staj yaptığı meslek mensubunun gözetiminde mesleki uygulamayı öğrenmek',
            'E': 'Kendi bürosunu açarak bağımsız biçimde mesleki faaliyet gösterip müşteri kabul etmek',
        },
        'D',
        'Staj, adayın meslek mensubunun GÖZETİMİNDE mesleki bilgi ve uygulama kazandığı dönemdir. Müşteri kabulü, imza, büro açma ve tasdik yetkileri ruhsatlı meslek mensubuna aittir (3568 md. 3, 12).',
    ),
    # düzey 1
    '0048': patch(
        'Bir aday, staja giriş ve meslek yeterlilik sınavlarına nereden başvuracağını ve sınavların hangi kuruluşça yapıldığını araştırmaktadır. Buna göre meslek mensubu adaylarının tabi olduğu sınavları düzenleyen kuruluş aşağıdakilerden hangisidir?',
        {
            'A': 'Hazine ve Maliye Bakanlığı',
            'B': 'Kamu Gözetimi Kurumu',
            'C': 'TÜRMOB (TESMER aracılığıyla)',
            'D': 'Sermaye Piyasası Kurulu',
            'E': 'Ölçme, Seçme ve Yerleştirme Merkezi',
        },
        'C',
        'Staja giriş ve meslek yeterlilik sınavları TÜRMOB tarafından, TESMER aracılığıyla düzenlenir. Kamu Gözetimi Kurumu bağımsız denetim alanını düzenler; Bakanlık ise meslek örgütü üzerinde genel gözetim yetkisini kullanır.',
    ),
    # düzey 1
    '0049': patch(
        'Meslek yeterlilik sınavını kazanan bir aday, genel şartlardan birini taşımadığı hâlde ruhsat verileceğini düşünmektedir. Buna göre ruhsatın verilmesi bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ruhsat, genel ve özel şartların tamamını taşıyanlara verilir',
            'B': 'Ruhsat, staj tamamlandığında kendiliğinden doğar',
            'C': 'Ruhsat sınavı kazanan herkese başkaca şart aranmaksızın verilir',
            'D': 'Ruhsat yalnızca yeminli mali müşavirler için düzenlenir',
            'E': 'Ruhsat doğrudan Bakanlıkça resen düzenlenir',
        },
        'A',
        '3568 md. 4 ve 5: ruhsat, Kanunda aranan GENEL ve ÖZEL şartların tamamını taşıyanlara verilir. Sınavı kazanmak tek başına yeterli değildir; genel şartlar da aranır.',
    ),
    # düzey 1
    '0050': patch(
        'Bir aday; öğrenim, staja giriş sınavı, staj, meslek yeterlilik sınavı ve ruhsat adımlarını sıralamış, oda kaydını bu sıranın neresine yerleştireceğini belirleyememiştir. Buna göre aday mesleğe giriş sürecinde hangi aşamada odaya kaydolur?',
        {
            'A': 'Stajına başladığında',
            'B': 'Lisans öğrenimini tamamladığında',
            'C': 'Ruhsatını aldıktan sonra, mesleki faaliyete başlamadan önce',
            'D': 'Staja giriş sınavını kazandığında',
            'E': 'Meslek yeterlilik sınavına başvurusunu yaptığı aşamada, sınav sonucundan önce',
        },
        'C',
        '3568 md. 19: meslek mensupları mesleki faaliyette bulunabilmek için bölgesi içinde bulundukları odaya kaydolur. Bu, ruhsat alındıktan sonraki son adımdır; staj döneminde meslek mensubu sıfatı doğmadığı için oda kaydı da söz konusu olmaz.',
    ),
    # düzey 1
    '0051': patch(
        'Bir aday, tanıdığı herhangi bir meslek mensubunun yanında staj yapabileceğini düşünmektedir. Buna göre staj yapılacak meslek mensubunun niteliği bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubunun mevzuatta öngörülen unvan ve kıdem koşullarını taşıması gerekir',
            'B': 'Staj yeri adayın serbest seçimine bırakılmıştır',
            'C': 'Herhangi bir meslek mensubu yanında staj yapılabilir',
            'D': 'Staj yalnızca yeminli mali müşavir yanında yapılabilir; SMMM yanında yapılamaz',
            'E': 'Meslek mensubunun kıdemi önemli değildir',
        },
        'A',
        '3568 md. 6 ve staj yönetmeliği: staj, yeminli mali müşavir ya da mevzuatta öngörülen kıdeme sahip serbest muhasebeci mali müşavir yanında yapılır. Ne herhangi bir meslek mensubu ne de serbest seçim söz konusudur.',
    ),
    # düzey 2
    '0052': patch(
        'Meslek yeterlilik sınavını kazanan bir kişi, ruhsatını almadan kartvizit bastırıp unvanını kullanmaya başlamıştır. Buna göre staj ve sınav süreci bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ruhsat, şartların tamamını taşıyanlara verilir',
            'B': 'Kanunda sayılan unvan ve yetkiler, ruhsat sahibi olmayanlarca kullanılamaz',
            'C': 'Meslek yeterlilik sınavını kazanan aday, ruhsat almadan unvanını kullanabilir',
            'D': 'Stajyer adayın imza yetkisi bulunmaz',
            'E': 'Mesleki faaliyet için odaya kayıt gerekir',
        },
        'C',
        '3568 md. 3: Kanunda belirtilen unvanları taşımayanlar bu unvanları ve meslek mensuplarına tanınan yetkileri KULLANAMAZ. Sınavı kazanmak tek başına unvan kullanma hakkı vermez; ruhsat ve oda kaydı gerekir.',
    ),
    # düzey 2
    '0053': patch(
        'Bir aday, staja giriş sınavını kazandıktan sonra dört yıl boyunca staja başlamamış ve şimdi başvurmak istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Aday staja istediği zaman başlayabilir; süre sınırı yoktur',
            'B': 'Aday, stajı atlayarak doğrudan meslek yeterlilik sınavına girme hakkını kazanır',
            'C': 'Sınav başarısı bir yıl sonra kendiliğinden ruhsata dönüşür',
            'D': 'Staja başlama ve sınav geçerliliği mevzuatta öngörülen sürelere tabidir',
            'E': 'Sınav başarısı süresiz olarak geçerliliğini korur',
        },
        'D',
        'Staj ve sınav yönetmelikleri, staja giriş sınavı başarısının geçerlilik süresini ve staja başlama koşullarını düzenler. Başarı süresiz değildir, stajı atlamaya izin vermez ve kendiliğinden ruhsata dönüşmez.',
    ),
    # düzey 2
    '0054': patch(
        'Biri SMMM, diğeri YMM olmak isteyen iki aday, kendilerinden aranan koşulları karşılaştırmaktadır. Buna göre mesleğe giriş şartları bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Genel şartlar yalnızca serbest muhasebeci mali müşavirler için aranır',
            'B': 'Özel şartlar unvana göre farklılaşır',
            'C': 'Genel şartlar hem SMMM hem YMM adayları için aranır',
            'D': 'Her iki unvan için de ruhsat ve oda kaydı gerekir',
            'E': "SMMM için üç yıllık staj, YMM için ise en az on yıllık SMMM'lik süresi aranır",
        },
        'A',
        '3568 md. 4: genel şartlar mesleğe girecek HERKES için aranır; unvan ayrımı yapmaz. Özel şartlar ise md. 5 (SMMM) ve md. 6 (YMM) ile ayrı ayrı düzenlenmiştir.',
    ),
    # düzey 3
    '0055': patch(
        'Bir aday tüm genel şartları taşımakta, lisans öğrenimini tamamlamış, staja giriş sınavını kazanmış ve üç yıllık stajını bitirmiştir. Ancak meslek yeterlilik sınavına henüz girmemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Aday sınavdan muaf tutulur',
            'B': 'Aday stajını tamamladığı için odaya kaydolabilir',
            'C': 'Aday üç yıllık stajını tamamladığı için meslek mensubu sayılır ve unvanını kullanabilir',
            'D': 'Aday ruhsat almadan mesleki faaliyette bulunabilir',
            'E': 'Aday henüz meslek mensubu değildir; unvan için sınavı kazanıp ruhsat alması gerekir',
        },
        'E',
        '3568 md. 5/A: SMMM unvanı için öğrenim, staj VE meslek yeterlilik sınavı koşullarının tamamı gerçekleşmelidir. Sınav kazanılmadan ruhsat verilmez; ruhsat ve oda kaydı olmadan mesleki faaliyet yürütülemez (md. 3, 19).',
    ),
    # düzey 2
    '0056': patch(
        "Bir aday, staj ve sınav süreçlerinde muhatap olacağı birimi ve bu birimin yetki sınırlarını araştırmaktadır. Buna göre TESMER'in görevleri bakımından aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'TESMER, meslek mensuplarının ruhsatlarını iptal etme yetkisine sahiptir',
            'B': 'TESMER aday eğitimi düzenler',
            'C': 'TESMER sınav süreçlerinde görev alır',
            'D': 'TESMER, meslek mensuplarına yönelik sürekli mesleki eğitim programları düzenler',
            'E': 'TESMER staj işlemlerini yürütür',
        },
        'A',
        'TESMER, TÜRMOB bünyesinde staj, eğitim ve sınav süreçlerini yürütür. Ruhsatın geri alınması MESLEKTEN ÇIKARMA disiplin cezasının sonucudur ve yetki DİSİPLİN KURULLARINA aittir (3568 md. 48).',
    ),
    # düzey 3
    '0057': patch(
        'Staj ve sınavlar ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Staja giriş sınavını kazanmak stajın başlangıcı için aranır. II. Meslek yeterlilik sınavı staj tamamlandıktan sonra girilir. III. Ruhsat ve oda kaydı mesleki faaliyetin önkoşuludur.',
        {
            'A': 'II ve III',
            'B': 'I, II ve III',
            'C': 'I ve II',
            'D': 'I ve III',
            'E': 'Yalnız I',
        },
        'B',
        'Üç ifade de doğrudur. 3568 md. 5/A staja giriş ve meslek yeterlilik sınavlarını sıralı koşullar olarak belirler; md. 3 ve 19 ise unvan kullanımı ve mesleki faaliyet için ruhsat ile oda kaydını arar.',
    ),
    # düzey 2
    '0058': patch(
        'Stajını sürdüren bir aday, staj döneminde kendi adına beyanname imzalayıp imzalayamayacağını sormaktadır. Buna göre meslek stajının niteliği bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Staj, adaya meslek mensubu sıfatı kazandırır ve imza yetkisi verir',
            'B': 'Staj meslek mensubunun gözetiminde yürütülür',
            'C': 'Staj, adaya mesleki bilgi, uygulama deneyimi ve etik anlayış kazandırır',
            'D': 'Staj TESMER/TÜRMOB tarafından izlenir',
            'E': 'Staj süresi üç yıldır',
        },
        'A',
        'Staj bir öğrenme dönemidir; adaya meslek mensubu sıfatı KAZANDIRMAZ. Unvan ve imza yetkisi için meslek yeterlilik sınavının kazanılması, ruhsat alınması ve odaya kaydolunması gerekir (3568 md. 3, 5, 19).',
    ),
    # düzey 2
    '0059': patch(
        'Bir aday; öğrenim, staja giriş sınavı, staj, meslek yeterlilik sınavı ve ruhsat adımlarını sıraya koymaya çalışmaktadır. Buna göre mesleğe giriş süreci bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ruhsat ve oda kaydı sürecin son adımıdır',
            'B': 'Meslek yeterlilik sınavı, üç yıllık staj süresi tamamlandıktan sonra girilir ve unvana kapı açar',
            'C': 'Staja giriş sınavı stajın başlangıcı için aranır',
            'D': 'Meslek yeterlilik sınavı, staja giriş sınavından önce girilir',
            'E': 'Staj süresi üç yıldır',
        },
        'D',
        'Doğru sıra: öğrenim → staja giriş sınavı → üç yıllık staj → meslek yeterlilik sınavı → ruhsat ve oda kaydı (3568 md. 4, 5, 19). Meslek yeterlilik sınavı staja giriş sınavından SONRA ve staj tamamlandıktan sonra girilir.',
    ),
    # düzey 3
    '0060': patch(
        'Staj, sınavlar ve mesleğe giriş ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. SMMM olabilmek için üç yıl staj gerekir. II. YMM olabilmek için en az beş yıl SMMM olarak çalışmak gerekir. III. Staja giriş sınavını kazanmak SMMM unvanı kazandırır. IV. Ruhsat, genel ve özel şartların tamamını taşıyanlara verilir.',
        {
            'A': 'II ve III',
            'B': 'I ve IV',
            'C': 'III ve IV',
            'D': 'I, II ve III',
            'E': 'Yalnız II',
        },
        'A',
        "II YANLIŞ: 3568 md. 6 en az ON YIL SMMM'lik arar. III YANLIŞ: staja giriş sınavı yalnızca stajın başlangıcına kapı açar; unvan için staj ve meslek yeterlilik sınavı gerekir. I (md. 5/A-b) ve IV (md. 4-5) doğrudur.",
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
    print(f"1 paket / {len(PATCHES)} soru (Staj ve Sinavlar yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
