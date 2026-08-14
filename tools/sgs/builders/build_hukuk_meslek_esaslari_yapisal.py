#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Meslek Hukuku Esaslari — YAPISAL kalibrasyon (tanim sorusu -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turunun 4. konusu (bkz.
build_hukuk_is_sozlesmesi_yapisal.py, build_hukuk_sosyal_guvenlik_yapisal.py,
build_hukuk_is_sozlesmesi_sona_erme_yapisal.py).

OLCULEN ACIK (629 gercek sinav hukuk sorusuna karsi):
    olcut              gercek   bu paket (once)
    medyan kok            257              122
    olumsuz kok         %41,5              %10
    duz tanim            %6,2              %62   <- ASIL KUSUR
    olay orgulu         %16,2               %0

Paketin 60 sorusunun TAMAMI yeniden yazildi.

IKI KAPI birden uygulandi:

  1) §5 BOY — dogru sik kac yamada en uzun? BERABERLIK ve ONCUL SECICILERI DAHIL
     sayilir. Onceki turda bunlari haric tutmak gercek bir tell'i gizlemisti:
     sosyal_guvenlik_hukuku'nda "I, II ve III" 10 onculu sorunun 4'unde dogruydu
     ve yapisal olarak en uzun siikti; audit onu sayip FATAL vermisti.
     Bu pakette ilk tasarim 49/60 (%82) cikip uretimi DURDURDU; 56 celdirici
     dogru sikla PARALEL iki cumleli yapiya tasinarak %23'e indirildi.

  2) §1 BILISSEL DUZEY (Codex'in ekledigi kapi) — uzun ya da olumsuz kok soruyu
     kendiliginden zorlastirmaz. Olculen dagilim: duzey 0 = 2 (<=6),
     duzey 0+1 = 10 (<=24), duzey 2 = 30 (>=24), duzey 3 = 20 (>=12).

     2. turda 11 soru olumsuz koke ve somut veriye tasindi: olumsuz kok
     %23 -> %40 (bant %41), medyan kok 192 -> 200, duzey 3 sayisi 13 -> 20.

Dayanak: 3568 sayili SMMM ve YMM Kanunu md. 1, 2, 3, 4, 5, 6, 8, 11, 12, 43, 44,
45, 46, 47, 48 · VUK mukerrer md. 227 · TBK md. 502 vd. · Meslek Ahlak Kurallari ·
5786 sayili Kanun degisikligi.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/meslek_hukuku/meslek_hukuku_esaslari.json"
STYLE_REF = "SGS Meslek Hukuku (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "mh-esas-gen-"


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
        'Bir mükellef; 2026 hesap dönemine ilişkin defterlerinin tutulmasını, mali tablolarının düzenlenmesini ve kurumlar vergisi beyannamesinin tasdik edilmesini istemektedir. Mükellef bu üç iş için tek bir meslek mensubuyla anlaşmayı planlamakta; ayrıca meslek mensubunun şirkete ortak olmasını da teklif etmektedir. Buna göre 3568 sayılı Kanun uyarınca aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Hizmet verilen şirkete ortak olmak tarafsızlığı zedelediğinden mesleki hizmet verilemez',
            'B': 'Üç işin tamamı tek bir yeminli mali müşavir tarafından yürütülebilir',
            'C': 'Beyannamenin tasdiki yalnızca yeminli mali müşavir tarafından yapılabilir',
            'D': 'Yeminli mali müşavirler muhasebe ile ilgili defterleri tutamaz ve muhasebe bürosuna ortak olamaz',
            'E': 'Defter tutma ve mali tablo düzenleme işleri serbest muhasebeci mali müşavirin görev alanındadır',
        },
        'B',
        "3568 md. 2/A defter tutma ve tablo düzenlemeyi SMMM'nin, md. 2/B ile md. 12 tasdiki YMM'nin görev alanına verir. md. 45 YMM'nin defter tutmasını ve muhasebe bürosuna ortak olmasını yasaklar; bu nedenle üç iş tek bir YMM tarafından YÜRÜTÜLEMEZ. Ayrıca hizmet verilen işletmeye ortaklık meslek ahlak kuralları uyarınca tarafsızlığı ortadan kaldırır.",
    ),
    # düzey 2
    '0002': patch(
        'Bir kişi, 3568 sayılı Kanun kapsamında mesleğe yeni girmek istemektedir. Kişi, kullanabileceği unvanları araştırmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Mesleğe yeni girecekler bakımından kullanılabilen unvanlar serbest muhasebeci mali müşavir ve yeminli mali müşavirdir',
            'B': 'Mesleğe yeni girecekler serbest muhasebeci, serbest muhasebeci mali müşavir ve yeminli mali müşavir unvanlarından birini seçebilir',
            'C': 'Mesleğe yeni girecekler doğrudan yeminli mali müşavir unvanıyla başlayabilir',
            'D': 'Unvan seçimi bağlı olunan odanın takdirine bırakılmıştır',
            'E': 'Mesleğe yeni girecekler yalnızca serbest muhasebeci unvanını kullanabilir',
        },
        'A',
        "3568 md. 1: Kanun serbest muhasebeci mali müşavirlik ve yeminli mali müşavirlik mesleklerini düzenler. 5786 sayılı Kanun'la yapılan değişiklikten sonra SERBEST MUHASEBECİ unvanıyla mesleğe yeni giriş kapanmış, mevcut serbest muhasebecilerin kazanılmış hakları korunmuştur. YMM unvanı ise doğrudan kazanılamaz; md. 6 en az on yıl SMMM olarak çalışmayı arar.",
    ),
    # düzey 2
    '0003': patch(
        'Bir yeminli mali müşavir, bir mükellefin hem defterlerini tutmak hem de tasdik işlemini yapmak istemektedir. Ayrıca bu amaçla bir muhasebe bürosuna ortak olmayı planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'YMM hem defter tutabilir hem tasdik yapabilir; büro ortaklığı da mümkündür',
            'B': "YMM'nin defter tutma yasağı yalnızca kendi tasdik ettiği mükellefler için geçerlidir",
            'C': 'YMM defter tutamaz ve muhasebe bürosuna ortak olamaz; tasdik yetkisini ise kullanabilir',
            'D': 'YMM yalnızca muhasebe bürosuna ortak olmak koşuluyla defter tutabilir',
            'E': 'YMM defter tutabilir ancak kendi tuttuğu defterleri tasdik edemez',
        },
        'C',
        "3568 md. 2/B ve md. 45: yeminli mali müşavirler, md. 2/A'nın (a) bendinde belirtilen MUHASEBE İLE İLGİLİ DEFTERLERİ TUTAMAZLAR, muhasebe bürosu açamazlar ve muhasebe bürolarına ORTAK OLAMAZLAR. Bu yasak tasdik ettikleri mükelleflerle sınırlı değil, genel bir yasaktır. Tasdik yetkisi ise md. 12 uyarınca yalnızca YMM'ye aittir.",
    ),
    # düzey 2
    '0004': patch(
        'Aşağıdakilerden hangisi serbest muhasebeci mali müşavirin 3568 sayılı Kanun uyarınca yapabileceği işlerden biri değildir?',
        {
            'A': 'Gerçek ve tüzel kişilere ait teşebbüs ve işletmelerin muhasebe defterlerini tutmak',
            'B': 'Muhasebe sistemleri kurmak, geliştirmek ve bu konularda müşavirlik yapmak',
            'C': 'Mali tablolarla ilgili konularda bilirkişilik ve tahkim işlerini yürütmek',
            'D': 'Mali tabloların ve beyannamelerin vergi dairesine karşı doğruluğunu tasdik etmek',
            'E': 'Belgelere dayanarak inceleme, tahlil ve denetim yapıp yazılı görüş vermek',
        },
        'D',
        "3568 md. 2/A: SMMM'nin işleri defter tutmak, mali tablo ve beyanname düzenlemek, muhasebe sistemi kurmak ve müşavirlik yapmak, inceleme-tahlil-denetim yaparak yazılı görüş vermek, rapor düzenlemek, tahkim ve bilirkişilik yapmaktır. TASDİK (md. 2/B ve md. 12) yalnızca yeminli mali müşavirlere tanınmış bir yetkidir.",
    ),
    # düzey 3
    '0005': patch(
        'SMMM olmak isteyen üç aday bulunmaktadır: (A) hukuk lisansı mezunu, (B) mühendislik lisansını tamamladıktan sonra maliye alanında yüksek lisans yapmış, (C) iki yıllık muhasebe önlisans programı mezunu. Üçü de staja giriş sınavına başvurmuştur. Buna göre öğrenim şartı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Hukuk lisansı mezunu A öğrenim şartını karşılar',
            'B': 'Lisans öğrenimi farklı alanda olanlar için ilgili dallarda alınmış lisansüstü diploma yeterli sayılır',
            'C': 'Öğrenim şartı en az lisans düzeyini gerektirir',
            'D': 'Maliye alanında yüksek lisans yapan B öğrenim şartını karşılar',
            'E': 'İki yıllık önlisans programı mezunu C, öğrenim şartını karşıladığından staja başlayabilir',
        },
        'E',
        '3568 md. 5/A-a: hukuk, iktisat, maliye, işletme, muhasebe, bankacılık, kamu yönetimi ve siyasal bilimler dallarında EN AZ LİSANS düzeyinde öğrenim görmüş olmak ya da bu dallar dışındaki lisans öğrenimini tamamlayıp bu alanlarda LİSANSÜSTÜ diploma almış olmak gerekir. İki yıllık ÖNLİSANS bu şartı karşılamaz.',
    ),
    # düzey 3
    '0006': patch(
        'Bir aday, 2023 yılında lisans öğrenimini tamamlamış ve aynı yıl staja giriş sınavını kazanmıştır. Aday, iki yıllık staj sonunda doğrudan ruhsat alabileceğini düşünmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İki yıllık staj süresinin dolmasıyla aday doğrudan ruhsat almaya hak kazanır',
            'B': 'Staja giriş sınavını kazanmak tek başına unvan kazandırmaz',
            'C': 'Ruhsat, genel ve özel şartların tamamını taşıyanlara verilir',
            'D': 'Staj tamamlandıktan sonra ayrıca serbest muhasebeci mali müşavirlik sınavı kazanılmalıdır',
            'E': 'Staj süresi üç yıldır',
        },
        'A',
        "3568 md. 5/A: SMMM olabilmek için staj amacıyla ÜÇ YIL çalışmış olmak ve SMMM SINAVINI kazanmış olmak gerekir. İki yıllık süre yeterli değildir; staj tek başına da ruhsat hakkı doğurmaz. Ruhsat, md. 4'teki genel ve md. 5'teki özel şartların tamamı gerçekleşince verilir.",
    ),
    # düzey 0
    '0007': patch(
        'Staja Giriş Sınavı (SGS) bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sınavı kazananlar staj yükümlülüğünden muaf tutulur',
            'B': 'Sınavı kazanmak doğrudan SMMM unvanı kazandırır',
            'C': 'Sınav, yeminli mali müşavirliğe geçiş için düzenlenir',
            'D': 'Sınav, meslek stajına başlayabilmek için aranan bir aşamadır',
            'E': 'Sınav yalnızca ilgili dallarda lisansüstü diploma almış adaylar için öngörülmüştür',
        },
        'D',
        '3568 md. 5 ve staj yönetmeliği: staja giriş sınavı, adayın üç yıllık meslek stajına başlayabilmesi için aranan bir aşamadır. Sınavı kazanmak tek başına unvan kazandırmaz ve staj yükümlülüğünü ortadan kaldırmaz; unvan için staj tamamlanmalı ve SMMM sınavı kazanılmalıdır.',
    ),
    # düzey 1
    '0008': patch(
        'Bir kişinin serbest muhasebeci mali müşavir unvanını kazanıp mesleği fiilen yapabilmesi için gereken aşamalar belirlenmektedir. Buna göre aşağıdakilerden hangisi bu aşamalardan biri değildir?',
        {
            'A': 'İlgili dallarda lisans düzeyinde öğrenim görmüş olmak',
            'B': 'En az on yıl bir yeminli mali müşavirin yanında çalışmış olmak',
            'C': 'Staja giriş sınavını kazanıp üç yıllık meslek stajını tamamlamış olmak',
            'D': 'Serbest muhasebeci mali müşavirlik sınavını kazanmak',
            'E': 'Ruhsat alarak bağlı olunacak odaya kaydolmak',
        },
        'B',
        "3568 md. 4, 5 ve 8: SMMM olmanın aşamaları öğrenim, staja giriş sınavı, üç yıllık staj, SMMM sınavı, ruhsat ve odaya kayıttır. ON YILLIK çalışma md. 6'da YEMİNLİ MALİ MÜŞAVİR olmak için aranan bir şarttır; SMMM için böyle bir aşama yoktur.",
    ),
    # düzey 2
    '0009': patch(
        'Bir serbest muhasebeci mali müşavir, yeminli mali müşavir olmak için başvurmak istemektedir. Meslek mensubu sekiz yıldır SMMM olarak çalışmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'On yıllık süre yalnızca lisansüstü diploması bulunmayanlar için aranır',
            'B': 'On yıllık çalışma süresi şartı yalnızca vergi inceleme yetkisi bulunmayan adaylar için aranır',
            'C': 'YMM olmak için çalışma süresi aranmaz; yalnızca sınav yeterlidir',
            'D': 'Sekiz yıllık çalışma yeterlidir; aday doğrudan YMM sınavına girebilir',
            'E': 'En az on yıl SMMM olarak çalışma şartı gerçekleşmediğinden başvuru koşulları henüz oluşmamıştır',
        },
        'E',
        '3568 md. 6: yeminli mali müşavir olabilmek için en az ON YIL serbest muhasebeci mali müşavirlik yapmış olmak, yeminli mali müşavirlik sınavını vermiş olmak ve YMM ruhsatını almış olmak gerekir. md. 9 bazı gruplara SINAV muafiyeti tanır; ancak çalışma süresi şartı bu muafiyetle karışmaz.',
    ),
    # düzey 2
    '0010': patch(
        'Meslek mensubu olabilmenin genel şartları belirlenmektedir. Buna göre aşağıdakilerden hangisi bu genel şartlardan biri değildir?',
        {
            'A': 'Ceza veya disiplin soruşturması sonucunda memuriyetten çıkarılmamış olmak',
            'B': 'Medeni hakları kullanma ehliyetine sahip bulunmak',
            'C': 'Belirli bir tutarın üzerinde sermaye veya teminat göstermiş olmak',
            'D': 'Kamu haklarından mahrum bulunmamak',
            'E': 'Türkiye Cumhuriyeti vatandaşı olmak veya yabancı serbest muhasebeci mali müşavirlik hakkı tanınmış olmak',
        },
        'C',
        '3568 md. 4: genel şartlar; T.C. vatandaşı olmak (yabancılar için karşılıklılık), medeni hakları kullanma ehliyetine sahip olmak, kamu haklarından mahrum bulunmamak, sayılan suçlardan hüküm giymemiş olmak, memuriyetten çıkarılmamış olmak ve meslek şeref ve haysiyetine uymayan durumlarda bulunmamaktır. SERMAYE veya TEMİNAT şartı öngörülmemiştir.',
    ),
    # düzey 1
    '0011': patch(
        'Bir yeminli mali müşavirin defter tutma bakımından durumu belirlenmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Defter tutma yasağı yalnızca vergi inceleme yetkisi bulunan YMM'ler için geçerlidir",
            'B': 'Yeminli mali müşavirler yalnızca tasdik etmedikleri mükelleflerin defterlerini tutabilir',
            'C': 'Yeminli mali müşavirler defter tutabilir ancak muhasebe bürosu açamaz',
            'D': 'Yeminli mali müşavirler tüm mükelleflerin defterlerini tutabilir',
            'E': 'Yeminli mali müşavirler muhasebe ile ilgili defterleri tutamaz ve muhasebe bürosu açamaz',
        },
        'E',
        "3568 md. 45: yeminli mali müşavirler, md. 2/A'nın (a) bendinde belirtilen işleri (defter tutmak vb.) YAPAMAZLAR; muhasebe bürosu açamaz ve muhasebe bürolarına ortak olamazlar. Yasak geneldir; tasdik ilişkisine ya da vergi inceleme yetkisine bağlı değildir.",
    ),
    # düzey 2
    '0012': patch(
        'Bir yeminli mali müşavir, bir mükellefin mali tablolarının ve beyannamelerinin mevzuata, muhasebe ilkelerine ve standartlarına uygunluğunu inceleyip onaylamıştır. Buna göre bu işlem bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yanlış tasdik hâlinde YMM, mükellefle birlikte müteselsilen sorumlu olur',
            'B': 'Tasdik, finansal tabloların bir bütün olarak gerçeğe uygunluğu hakkında görüş bildirilmesidir',
            'C': 'Tasdik yetkisi yalnızca yeminli mali müşavirlere aittir',
            'D': 'Tasdik, mali tablo ve beyannamelerin mevzuata ve muhasebe standartlarına uygunluğunun onaylanmasıdır',
            'E': 'Tasdikin kapsamı ilgili mevzuatla belirlenir',
        },
        'B',
        '3568 md. 12: tasdik, mali tabloların ve beyannamelerin mevzuat hükümleri, muhasebe ilkeleri ile standartlarına UYGUNLUĞUNUN ve hesapların denetim standartlarına göre incelendiğinin onaylanmasıdır. Finansal tablolar hakkında bir bütün olarak GÖRÜŞ BİLDİRME ise BAĞIMSIZ DENETİMdir ve ayrı bir mevzuata tabidir; ikisi karıştırılmamalıdır.',
    ),
    # düzey 3
    '0013': patch(
        'Bir yeminli mali müşavir, gerçeği yansıtmadığını bildiği bir beyannameyi tasdik etmiştir. Tasdik nedeniyle vergi ziyaı doğmuş ve mükellef adına vergi ile ceza tarh edilmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'YMM, ziyaa uğratılan vergi ve kesilen cezalardan mükellefle birlikte müteselsilen sorumlu olur',
            'B': 'Ziyaa uğratılan vergiden sorumluluk yalnızca mükellefe aittir; YMM hakkında yalnızca disiplin işlemi yapılır',
            'C': "YMM'nin sorumluluğu, mükellefin malvarlığı tükendikten sonra ikinci derecede doğar",
            'D': 'YMM yalnızca tasdik ücretiyle sınırlı olarak sorumlu tutulur',
            'E': "YMM'nin mali sorumluluğu ancak kastı mahkeme kararıyla sabit olursa doğar",
        },
        'A',
        '3568 md. 12/4: yeminli mali müşavirler yaptıkları tasdikin DOĞRU OLMAMASI hâlinde, tasdikin kapsamı ile sınırlı olmak üzere ziyaa uğratılan vergilerden ve kesilecek cezalardan mükellefle BİRLİKTE MÜTESELSİLEN sorumlu olurlar. Sorumluluk müteselsildir; ikinci derecede değildir ve ücretle sınırlanamaz. Ayrıca disiplin ve cezai sorumluluk saklıdır.',
    ),
    # düzey 2
    '0014': patch(
        'Bir meslek mensubu, mesleğin gereği ve onuruyla bağdaşmayan bir işle uğraşmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubunun mesleki faaliyeti dışındaki işleri denetlenemez',
            'B': 'Yasak yalnızca ticari faaliyetlerle sınırlıdır',
            'C': 'Yasak yalnızca bağımsız çalışan meslek mensupları için geçerlidir',
            'D': 'Meslek mensupları mesleğin gereği ve onuruyla bağdaşmayan işlerle uğraşamaz; aykırılık disiplin sorumluluğu doğurur',
            'E': 'Aykırılık disiplin sorumluluğu doğurmaz; yalnızca meslek ruhsatının kendiliğinden düşmesi sonucunu doğurmakla kalır',
        },
        'D',
        '3568 md. 45: meslek mensupları, mesleğin gereği ve onuruyla BAĞDAŞMAYAN işlerle uğraşamazlar. Yasak ticari faaliyetle sınırlı olmayıp mesleğin saygınlığını zedeleyen her davranışı kapsar ve tüm meslek mensuplarını bağlar. Aykırılık md. 48 uyarınca disiplin cezası gerektirir; ruhsat kendiliğinden düşmez.',
    ),
    # düzey 3
    '0015': patch(
        'Bir meslek mensubu ile iş sahibi arasında, üç yıl süreyle muhasebe hizmeti verilmesine ilişkin yazılı bir sözleşme yapılmıştır. Sözleşmede meslek mensubunun belirli bir vergi avantajı sağlayacağı da taahhüt edilmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sözleşmeye konulan sonuç taahhüdü, meslek mensubunun mevzuattan doğan kanuni sorumluluğunu değiştirmez',
            'B': 'Meslek mensubu iş sahibinin talimatıyla değil mevzuatla bağlıdır',
            'C': 'İlişki eser sözleşmesi olduğundan meslek mensubu taahhüt ettiği sonucu sağlamakla yükümlüdür',
            'D': 'Meslek mensubu belirli bir sonucu değil, işi özenle görmeyi üstlenir',
            'E': 'İlişki kural olarak vekâlet sözleşmesidir',
        },
        'C',
        'Meslek mensubu ile iş sahibi arasındaki ilişki kural olarak VEKÂLET sözleşmesidir (TBK md. 502 vd.): meslek mensubu belirli bir SONUCU değil, işi özenle görmeyi üstlenir. Eser sözleşmesinde ise sonuç taahhüt edilir. Sözleşmeye konulan sonuç kaydı, meslek mensubunun mevzuattan doğan yükümlülüklerini ve sorumluluğunu değiştirmez.',
    ),
    # düzey 2
    '0016': patch(
        'Bir meslek mensubu, bir iş sahibiyle asgari ücret tarifesinde öngörülen tutarın altında bir ücret üzerinde anlaşmıştır. Meslek mensubu, sözleşme serbestisi bulunduğunu ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tarifede belirlenen tutarın altında ücretle iş kabul edilemez; bu davranış disiplin sorumluluğu doğurur',
            'B': 'Tarifenin altında ücret kararlaştırılması sözleşmeyi kesin hükümsüz kılar',
            'C': 'Tarife yalnızca yeminli mali müşavirlik işleri için bağlayıcıdır',
            'D': 'Taraflar ücreti serbestçe belirleyebilir; asgari ücret tarifesi bağlayıcı değil yalnızca yol göstericidir',
            'E': 'Tarife üst sınırı gösterir; altında ücret kararlaştırmak serbesttir',
        },
        'A',
        '3568 md. 46: ücretin asgari tutarı tarifeyle belirlenir ve meslek mensupları tarifede yazılı asgari ücretin ALTINDA iş kabul edemezler. Tarife ASGARİ (taban) tutarı gösterir, üst sınırı değil. Aykırılık sözleşmeyi kendiliğinden hükümsüz kılmaz; md. 48 uyarınca disiplin sorumluluğu doğurur.',
    ),
    # düzey 3
    '0017': patch(
        'Bir meslek mensubu, müşterisinin işleri dolayısıyla öğrendiği bir bilgiyi; bir yandan yürütülen adli soruşturmada tanık sıfatıyla açıklamış, diğer yandan aynı bilgiyi kendi yatırım kararında kullanmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Her iki davranış da sır saklama yükümlülüğünün ihlalidir',
            'B': 'Her iki davranış da hukuka uygundur; yükümlülük iş ilişkisi bitince sona erer',
            'C': 'Tanıklık sır ifşası sayılmaz; ancak bilgiyi kendi yararına kullanmak yasaktır',
            'D': 'Tanıklık sır ifşası sayılır; kendi yararına kullanmak ise serbesttir',
            'E': 'Sır saklama yükümlülüğü yalnızca yeminli mali müşavirler için öngörülmüştür',
        },
        'C',
        '3568 md. 43: meslek mensupları ve yanlarında çalışanlar, işleri dolayısıyla öğrendikleri bilgi ve sırları ifşa edemezler, çeşitli kanunlarla muhbirlere tanınan hak ve menfaatlerden yararlanamazlar; ancak ADLİ VEYA İDARİ her türlü inceleme veya soruşturma bu hükmün kapsamı dışındadır ve TANIKLIK SIRRIN İFŞASI SAYILMAZ. Bilgiyi kendi yararına kullanmak ise açıkça yasaktır.',
    ),
    # düzey 2
    '0018': patch(
        'Bir meslek mensubu, iş elde etmek amacıyla yerel bir gazeteye ilan vermeyi ve bürosunun girişine tabela asmayı planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Reklam yasağı yalnızca yeminli mali müşavirler için geçerlidir',
            'B': 'Tabela asabilir; iş elde etmek amacıyla reklam sayılabilecek ilan veremez',
            'C': 'İlan verebilir ancak tabela kullanamaz',
            'D': 'Her ikisi de yasaktır; meslek mensupları tabela dahi kullanamaz',
            'E': 'Meslek mensubu her ikisini de yapabilir; meslek mevzuatı iş elde etmeye yönelik reklamı serbest bırakmıştır',
        },
        'B',
        '3568 md. 44: meslek mensupları, iş elde etmek için açık veya kapalı dolaylı olarak REKLAM SAYILABİLECEK faaliyetlerde bulunamazlar. Tabela kullanımı ile kartvizit gibi mesleki tanıtım araçları, Yönetmelikte belirlenen ölçüler içinde kalmak koşuluyla reklam sayılmaz. Yasak tüm meslek mensuplarını kapsar.',
    ),
    # düzey 1
    '0019': patch(
        'Mesleğe giriş şartlarını tamamlayan bir aday, ruhsatını almak için başvurmuştur. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ruhsat yalnızca yeminli mali müşavirler için düzenlenir',
            'B': 'Ruhsat, sınavı kazanan herkese Kanundaki genel şartlar aranmaksızın verilir ve mesleki faaliyet için odaya kayıt gerekmez',
            'C': 'Ruhsat alan meslek mensubunun ayrıca odaya kaydolması gerekmez',
            'D': 'Ruhsat doğrudan Maliye Bakanlığınca ve resen düzenlenir',
            'E': 'Kanunda aranan genel ve özel şartları taşıyanlara ruhsat verilir; meslek icrası için odaya kayıt da gerekir',
        },
        'E',
        '3568 md. 4 ve 5: ruhsat, Kanunda aranan GENEL ve ÖZEL şartların tamamını taşıyanlara verilir. Meslek mensubunun mesleki faaliyette bulunabilmesi için ayrıca bağlı olacağı ODAYA KAYDOLMASI gerekir. Ruhsat hem SMMM hem YMM için düzenlenir.',
    ),
    # düzey 2
    '0020': patch(
        "Meslek hukuku ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Mesleğin dayanağı 3568 sayılı Kanun'dur. II. Tasdik yetkisi serbest muhasebeci mali müşavirlere aittir. III. Meslek mensupları meslek icrası sırasında ticari faaliyette bulunamaz. IV. Meslek mensupları iş elde etmek için reklam yapabilir.",
        {
            'A': 'II ve IV',
            'B': 'Yalnız II',
            'C': 'I ve III',
            'D': 'III ve IV',
            'E': 'I, II ve IV',
        },
        'A',
        'II YANLIŞ: 3568 md. 2/B ve md. 12 uyarınca tasdik yetkisi yalnızca YEMİNLİ MALİ MÜŞAVİRLERE aittir. IV YANLIŞ: md. 44 iş elde etmek amacıyla reklam sayılabilecek faaliyetleri yasaklar. I ve III (md. 1 ve md. 45) doğrudur.',
    ),
    # düzey 3
    '0021': patch(
        'Bir serbest muhasebeci mali müşavir, bir anonim şirkette haftada 45 saat hizmet akdiyle çalışmakta; aynı dönemde kendi bürosunda üç mükellefe serbest olarak hizmet vermeyi sürdürmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yeminli mali müşavirler mesleklerini yalnızca bağımsız olarak yürütür',
            'B': 'Meslek mensubu ya bağımsız ya da bağımlı olarak çalışır; ikisi bir arada yürütülemez',
            'C': 'Bağımlı çalışan meslek mensubu ruhsatını korur ancak serbest meslek faaliyeti yapamaz',
            'D': 'Meslek mensupları ticari mümessil, ticari vekil veya acente olarak çalışamaz',
            'E': 'Meslek mensubu bağımlı çalışırken kendi adına serbest meslek faaliyetini de sürdürebilir',
        },
        'E',
        '3568 md. 45: meslek mensupları gerçek ve tüzel kişilere tabi ve onların işyerlerine bağlı olarak hizmet akdiyle çalışamazlar. Bağımlı çalışan SMMM ruhsatını korur ancak aynı anda kendi adına SERBEST MESLEK FAALİYETİ yürütemez; iki çalışma biçimi bir arada olamaz.',
    ),
    # düzey 2
    '0022': patch(
        'Bir yeminli mali müşavire; muhasebe sistemi kurulması, mali tabloların tasdiki ve bir işletmenin defterlerinin tutulması için ayrı ayrı teklifler gelmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yalnızca defter tutma ve tasdik tekliflerini kabul edebilir',
            'B': "Yalnızca tasdik teklifini kabul edebilir; muhasebe sistemi kurma ve defter tutma işleri SMMM'ye özgüdür",
            'C': 'Muhasebe sistemi kurma ve tasdik tekliflerini kabul edebilir; defter tutma teklifini kabul edemez',
            'D': 'Üç teklifi de kabul edebilir',
            'E': 'Muhasebe sistemi kurma işi için ayrıca odadan izin alması gerekir',
        },
        'C',
        "3568 md. 2/B: yeminli mali müşavirlik mesleğinin konusu, md. 2/A'nın (b) ve (c) bentlerindeki işler (muhasebe sistemi kurmak, müşavirlik yapmak, inceleme-tahlil-denetim, yazılı görüş, tahkim ve bilirkişilik) ile TASDİK işidir. (a) bendindeki DEFTER TUTMA işi YMM'ye kapalıdır (md. 45).",
    ),
    # düzey 3
    '0023': patch(
        'Bir serbest muhasebeci mali müşavir; kendi adına bir market işletmeyi, bir anonim şirkete sermaye ortağı olmayı ve bir limited şirkette ticari vekil sıfatıyla görev almayı planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Anonim şirkete ortak olabilir; market işletemez ve ticari vekil olarak çalışamaz',
            'B': 'Market işletebilir ancak şirkete ortak olamaz ve ticari vekil olamaz',
            'C': 'Ticari vekil olarak çalışabilir; market işletme ve ortaklık ise yasaktır',
            'D': 'Üçü de yasaktır; meslek mensubu hiçbir şirkete ortak olamaz',
            'E': 'Üç işi de yapabilir; meslek mevzuatı ortaklık ve ticareti serbest bırakmıştır',
        },
        'A',
        '3568 md. 45: meslek mensupları meslek icrası sırasında TİCARİ FAALİYETTE bulunamazlar ve ticari mümessil, ticari vekil ya da acente olarak çalışamazlar. Ancak sermayesi paylara bölünmüş komandit şirketlerde komanditer ortak, limited ve anonim şirketlerde ORTAK olabilirler. Sermaye ortaklığı ile bizzat ticaret yapmak farklı şeylerdir.',
    ),
    # düzey 2
    '0024': patch(
        'Bir meslek mensubu, mesleki faaliyetini yürütmek için işyeri açmadan yalnızca evinden hizmet vermeyi ve ayrıca ikinci bir ilde şube büro açmayı planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Büro yerine yalnızca posta adresi bildirilmesi yeterlidir',
            'B': 'Meslek mensubu mesleki faaliyeti için büro açmakla yükümlüdür ve birden fazla büro edinemez',
            'C': 'Büro açma yükümlülüğü yalnızca yeminli mali müşavirler için öngörülmüş olup SMMM faaliyetini konuttan yürütebilir',
            'D': 'Büro açma yükümlülüğü bulunmaz; faaliyet konuttan da yürütülebilir',
            'E': 'Meslek mensubu dilediği sayıda şube büro açabilir',
        },
        'B',
        "Meslek mevzuatı uyarınca meslek mensupları mesleki faaliyetlerini sürdürebilmek için İŞYERİ (BÜRO) açmak zorundadır; büro standartlarına uygunluk aranır. Her meslek mensubu yalnızca BİR büro edinebilir ve şube niteliğinde ikinci bir büro açamaz. Yükümlülük hem SMMM'yi hem YMM'yi bağlar.",
    ),
    # düzey 3
    '0025': patch(
        'Dört meslek mensubu mesleği birlikte yürütmek istemektedir. Ortaklardan üçü serbest muhasebeci mali müşavir, biri ise meslek mensubu olmayan bir yatırımcıdır. Grup, ortaklık bürosu ya da şirket kurmayı değerlendirmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Her meslek mensubu yalnızca bir büro edinebilir',
            'B': 'Bu birlikteliklerde ortakların tamamının meslek mensubu olması gerekir',
            'C': 'Mesleki faaliyet için işyeri açma yükümlülüğü bulunur',
            'D': 'Meslek mensubu olmayan yatırımcı, sermaye koyarak meslek şirketine ortak olabilir',
            'E': 'Meslek mensupları mesleği ortaklık bürosu ya da şirket biçiminde birlikte yürütebilir',
        },
        'D',
        '3568 ve ilgili yönetmelik: meslek mensupları mesleklerini ortaklık bürosu ya da şirket biçiminde birlikte yürütebilir; ancak bu yapılarda ORTAKLARIN TAMAMI meslek mensubu olmak zorundadır. Meslek dışından sermayedar ortak alınamaz. Ayrıca her meslek mensubu tek büro edinebilir.',
    ),
    # düzey 2
    '0026': patch(
        'Meslek mensubu olma şartları ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. SMMM olmak için ilgili dallarda en az lisans düzeyinde öğrenim görmüş olmak gerekir. II. SMMM olmak için üç yıl staj yapmış olmak gerekir. III. YMM olmak için en az beş yıl SMMM olarak çalışmış olmak gerekir.',
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'II ve III',
        },
        'C',
        'I doğrudur (3568 md. 5/A-a). II doğrudur (md. 5/A-b). III YANLIŞTIR: md. 6 uyarınca yeminli mali müşavir olabilmek için en az ON YIL serbest muhasebeci mali müşavirlik yapmış olmak gerekir.',
    ),
    # düzey 0
    '0027': patch(
        "3568 sayılı Kanun'un amacı aşağıdakilerden hangisidir?",
        {
            'A': 'Ticaret şirketlerinin kuruluş, tescil ve ilan işlemlerinin usul ve esaslarını belirleyerek sicil düzenini kurmak',
            'B': 'Vergi matrahlarını idare adına resen belirlemek',
            'C': 'Kamu kurumlarının bütçe ve harcama usullerini belirlemek',
            'D': 'Bağımsız denetim kuruluşlarının yetkilendirilmesini düzenlemek',
            'E': 'İşletmelerde faaliyetlerin sağlıklı biçimde yürütülmesi ile mali tabloların gerçeği yansıtmasını sağlamak',
        },
        'E',
        '3568 md. 1: Kanunun amacı, işletmelerde faaliyetlerin ve işlemlerin sağlıklı ve güvenilir biçimde işleyişini sağlamak, faaliyet sonuçlarını ilgili mevzuat çerçevesinde denetlemeye, değerlendirmeye tabi tutarak gerçek durumu ilgililerin ve resmî mercilerin istifadesine tarafsız biçimde sunmak ve yüksek meslekî standartları gerçekleştirmektir.',
    ),
    # düzey 3
    '0028': patch(
        'Bir mükellefin defterlerini tutan serbest muhasebeci mali müşavir, mükellefin vergi beyannamesini imzalamıştır. Beyannamede, defter kayıtlarına ve belgelere aykırı bir beyan bulunduğu tespit edilmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu, kayıtsal uygunluğun yanında belgelerin gerçeği yansıtıp yansıtmadığını da araştırmakla yükümlüdür',
            'B': 'Sorumluluk yalnızca yeminli mali müşavirlerin tasdik ettiği beyannameler için doğar',
            'C': 'Meslek mensubunun sorumluluğu yalnızca beyannameyi süresinde vermekle sınırlıdır',
            'D': 'Meslek mensubu, imzaladığı beyannamede yer alan bilgilerin defter kayıtlarına ve belgelere uygunluğundan sorumludur',
            'E': 'Beyannamenin imzalanması meslek mensubuna hiçbir sorumluluk yüklemez',
        },
        'D',
        'VUK mükerrer md. 227: beyannameyi imzalayan meslek mensupları, imzaladıkları beyannamelerde yer alan bilgilerin DEFTER KAYITLARINA ve bu kayıtların dayanağını oluşturan BELGELERE uygun olmamasından sorumludur. Sorumluluk belgelerin maddi gerçeği yansıtıp yansıtmadığını araştırmayı kapsamaz; şekli ve kayıtsal uygunlukla sınırlıdır.',
    ),
    # düzey 2
    '0029': patch(
        'Meslek hukuku bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensupları arasında haksız rekabet yasaktır',
            'B': 'Meslek mensupları işleri dolayısıyla öğrendikleri sırları ifşa edemez',
            'C': 'Meslek mensupları, iş elde etmek amacıyla reklam sayılabilecek faaliyetlerde bulunabilir',
            'D': 'Meslek mensupları meslek icrası sırasında ticari faaliyette bulunamaz ve acente olarak çalışamaz',
            'E': 'Meslek mensupları asgari ücret tarifesinin altında iş kabul edemez',
        },
        'C',
        '3568 md. 44 iş elde etmek amacıyla REKLAM sayılabilecek faaliyetleri açıkça yasaklar. Diğer seçenekler doğrudur: md. 45 ticaret yasağını, md. 46 asgari ücret tarifesini, md. 47 haksız rekabet yasağını, md. 43 ise sır saklama yükümlülüğünü düzenler.',
    ),
    # düzey 3
    '0030': patch(
        'Bir aday ilgili lisans öğrenimini tamamlamış ve staja giriş sınavını kazanmıştır. Aday, bundan sonraki süreçte izlemesi gereken adımları belirlemek istemektedir. Buna göre doğru sıralama aşağıdakilerden hangisidir?',
        {
            'A': 'Üç yıllık staj → ruhsat alma → SMMM sınavını kazanma → odaya kayıt',
            'B': 'Üç yıllık staj → SMMM sınavını kazanma → ruhsat alma → odaya kayıt',
            'C': 'SMMM sınavını kazanma → üç yıllık staj → ruhsat alma → odaya kayıt',
            'D': 'Ruhsat alma → üç yıllık staj → SMMM sınavını kazanma → odaya kayıt',
            'E': 'Odaya kayıt → SMMM sınavını kazanma → üç yıllık staj → ruhsat alma',
        },
        'B',
        '3568 md. 5 ve md. 8: staja giriş sınavını kazanan aday üç yıllık stajını tamamlar, ardından serbest muhasebeci mali müşavirlik sınavını kazanır. Bu şartları taşıyanlara ruhsat verilir ve meslek mensubu, mesleki faaliyette bulunabilmek için bağlı olduğu odaya kaydolur.',
    ),
    # düzey 3
    '0031': patch(
        'İş sahibiyle sözleşmesi sona eren bir meslek mensubu, iş sahibine ait defter ve belgeleri ücret alacağı ödenene kadar teslim etmeyeceğini bildirmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Defter ve belgeleri geri verme yükümlülüğü yalnızca yeminli mali müşavirler için öngörülmüş olup SMMM bu yükümlülüğe tabi değildir',
            'B': 'Meslek mensubu belgeleri geri vermek yerine imha edebilir',
            'C': 'Defter ve belgeler yalnızca vergi dairesinin talebi üzerine geri verilir',
            'D': 'Defter ve belgeler talep hâlinde tutanakla geri verilir; ücret alacağı alıkoyma hakkı vermez',
            'E': 'Meslek mensubu ücreti ödenene kadar defter ve belgeleri alıkoyabilir',
        },
        'D',
        'Meslek mensubu, iş sahibine ait defter ve belgeleri özenle saklamak ve iş ilişkisi sona erdiğinde TUTANAKLA geri vermekle yükümlüdür. Ücret alacağı, üçüncü kişilere ait ve yasal saklama yükümlülüğü bulunan bu belgeler üzerinde alıkoyma (hapis) hakkı vermez; alacak genel hükümlere göre takip edilir.',
    ),
    # düzey 2
    '0032': patch(
        'Bir meslek mensubu, başka bir meslek mensubunun müşterisine ulaşarak tarifenin altında ücret teklif etmiş ve rakibinin mesleki yeterliği hakkında olumsuz beyanda bulunmuştur. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Serbest piyasa koşullarında her iki davranış da hukuka uygundur',
            'B': 'Her iki davranış da haksız rekabet oluşturur ve disiplin sorumluluğu doğurur',
            'C': 'Haksız rekabet yalnızca ticari işletmeler arasında söz konusu olup meslek mensupları arasında uygulanmaz',
            'D': 'Yalnızca rakip hakkındaki olumsuz beyan haksız rekabet oluşturur',
            'E': 'Yalnızca tarifenin altında ücret teklifi haksız rekabet oluşturur',
        },
        'B',
        '3568 md. 47: meslek mensupları arasında haksız rekabet yasaktır. Diğer meslek mensubunun müşterisini elde etmeye yönelik girişimler, tarifenin altında ücret teklif ederek iş almaya çalışmak (md. 46) ve meslektaşı hakkında küçük düşürücü beyanda bulunmak haksız rekabet sayılır; md. 48 uyarınca disiplin cezası gerektirir.',
    ),
    # düzey 2
    '0033': patch(
        'Yeminli mali müşavirlik ruhsatını yeni alan bir meslek mensubu, mesleki faaliyete başlamak üzeredir. Meslek mensubu, yemin yükümlülüğünü her tasdik işi için ayrı ayrı yerine getireceğini düşünmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yemin, ruhsatın alınmasından sonra ve faaliyete başlamadan önce yerine getirilir',
            'B': 'Yeminli mali müşavirler mesleki faaliyete başlamadan önce yemin eder',
            'C': 'Serbest muhasebeci mali müşavirler için yemin yükümlülüğü bulunmaz',
            'D': 'Yemin yükümlülüğü yalnızca yeminli mali müşavirler için öngörülmüştür',
            'E': 'Yemin, her tasdik işine başlamadan önce ayrı ayrı tekrarlanır',
        },
        'E',
        '3568 md. 11: yeminli mali müşavirler mesleki faaliyete başlamadan ÖNCE yemin ederler. Yemin bir kez edilir; her iş için tekrarlanmaz. Yükümlülük YMM unvanına özgüdür ve serbest muhasebeci mali müşavirler için öngörülmemiştir.',
    ),
    # düzey 3
    '0034': patch(
        'Bir iş sahibi, meslek mensubundan gerçeğe aykırı bir kayıt yapmasını istemiş; talebin reddi hâlinde sözleşmeyi sona erdireceğini bildirmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu talebi reddeder; ısrar hâlinde sözleşmeyi sona erdirebilir ve gerekiyorsa odaya bildirir',
            'B': 'Meslek mensubu talebi yerine getirip durumu sonradan odaya bildirebilir',
            'C': 'Meslek mensubu sözleşme süresince talebi reddedemez; süre sonunda ilişkiyi bitirir',
            'D': 'Meslek mensubu iş sahibinin talimatına uymakla yükümlüdür',
            'E': 'Meslek mensubu, iş sahibi talimatı yazılı olarak verdiği takdirde talebi yerine getirebilir ve sorumluluktan kurtulur',
        },
        'A',
        'Meslek mensubu iş sahibinin talimatıyla değil MEVZUAT ve mesleki ilkelerle bağlıdır. Dürüstlük ve tarafsızlık ilkeleri gereği hukuka aykırı talep reddedilir; yazılı talimat sorumluluğu kaldırmaz. Israr hâlinde meslek mensubu işi bırakabilir. Gerçeğe aykırı kayıt ayrıca VUK ve TCK sorumluluğu doğurabilir.',
    ),
    # düzey 2
    '0035': patch(
        'Bir meslek mensubu, mesleki faaliyeti sırasında tuttuğu kayıt ve belgelerin düzenine ilişkin yükümlülüklerini belirlemektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu düzenlediği belgelerde gerçeğe uygunluğu gözetmekle yükümlüdür',
            'B': 'Meslek mensubu, aldığı ve verdiği belgeleri düzenli biçimde kayda geçirmelidir',
            'C': 'Meslek mensubu, iş sahibine ait defter ve belgeleri kendi bürosunda süresiz olarak alıkoyabilir',
            'D': 'Meslek mensubu, mesleki faaliyetine ilişkin kayıtları mevzuatta öngörülen süre boyunca saklar',
            'E': 'İş sahibinden alınan belgeler tutanakla teslim alınır ve tutanakla geri verilir',
        },
        'C',
        'Meslek mevzuatı: meslek mensubu, iş sahibinden aldığı defter ve belgeleri TUTANAKLA teslim alır, mesleki kayıtlarını düzenli tutar ve mevzuatta öngörülen süre boyunca saklar. İş ilişkisi sona erdiğinde bu belgeler iş sahibine TUTANAKLA GERİ VERİLİR; süresiz alıkoyma hakkı yoktur.',
    ),
    # düzey 2
    '0036': patch(
        'Meslek mensuplarının yetkileri ve yasakları ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Yeminli mali müşavirler muhasebe ile ilgili defterleri tutamaz. II. Meslek mensupları limited ve anonim şirketlere ortak olabilir. III. Meslek mensupları ticari mümessil veya acente olarak çalışabilir.',
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'I, II ve III',
            'D': 'II ve III',
            'E': 'I ve II',
        },
        'E',
        'I doğrudur (3568 md. 45). II doğrudur: md. 45 meslek mensuplarının sermayesi paylara bölünmüş komandit şirketlerde komanditer ortak, limited ve anonim şirketlerde ortak olmasına izin verir. III YANLIŞTIR: aynı madde meslek mensuplarının ticari mümessil, ticari vekil veya acente olarak çalışmasını yasaklar.',
    ),
    # düzey 2
    '0037': patch(
        'Bir aday, geçmişte hüküm giydiği bir suç nedeniyle kamu haklarından yoksun bırakılmış; ancak bu ceza affa uğramıştır. Aday meslek mensubu olmak için başvurmuştur. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kanunda sayılan suçlardan hüküm giymemiş olmak şartı, affa uğramış olsa dahi aranır',
            'B': 'Şartın gerçekleşip gerçekleşmediğini takdir yetkisi odaya aittir',
            'C': 'Kamu haklarından yoksunluk yalnızca yeminli mali müşavir adayları için engel oluşturur; SMMM adayları için aranmaz',
            'D': 'Af hâlinde şart, cezanın infazından beş yıl sonra ortadan kalkar',
            'E': 'Af, şartı ortadan kaldırdığından başvuru kabul edilir',
        },
        'A',
        "3568 md. 4/d: 'Türk Ceza Kanunu'nun 53'üncü maddesinde belirtilen süreler geçmiş olsa bile; kasten işlenen bir suçtan dolayı bir yıl veya daha fazla süreyle hapis cezasına ya da AFFA UĞRAMIŞ OLSA BİLE' sayılan suçlardan mahkûm olmamak gerekir. Af, bu şartı ortadan kaldırmaz.",
    ),
    # düzey 3
    '0038': patch(
        'Bir yeminli mali müşavir, tasdik hizmeti verdiği bir anonim şirkette önemli oranda pay sahibidir ve aynı zamanda şirketin yönetim kurulu üyesidir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Durum iş sahibine yazılı olarak bildirilirse tasdik hizmeti verilebilir',
            'B': 'Yönetim kurulu üyeliğinden ayrılması hâlinde pay sahipliği tek başına engel oluşturmaz',
            'C': 'Bağımsızlık zedelendiğinden meslek mensubu bu şirkete tasdik hizmeti veremez',
            'D': 'Bağımsızlık yalnızca bağımsız denetim işlerinde aranır; tasdikte aranmaz',
            'E': 'Pay sahipliği bağımsızlığı etkilemez; tasdik yapılabilir',
        },
        'C',
        'Meslek ahlak kuralları ve 3568 md. 45: meslek mensubu, tarafsızlığını ve bağımsızlığını zedeleyecek ilişkiler içinde bulunamaz. Tasdik hizmeti verilen işletmeye ORTAK olmak ya da YÖNETİMİNDE görev almak bağımsızlığı doğrudan ortadan kaldırır; bildirim veya rıza bu sakatlığı gidermez. Bağımsızlık tasdik işlerinin kurucu koşuludur.',
    ),
    # düzey 2
    '0039': patch(
        'Serbest muhasebeci (SM) unvanının bugünkü durumu değerlendirilmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Mesleğe yeni girecekler bakımından kullanılabilen unvanlar SMMM ve YMM'dir",
            'B': 'Bu unvanla mesleğe yeni giriş hâlen mümkün olup önlisans mezunları bu yoldan mesleğe girer',
            'C': 'Öngörülen şartları taşıyan serbest muhasebecilere SMMM unvanına geçiş imkânı tanınmıştır',
            'D': '5786 sayılı Kanun değişikliğiyle bu unvanla mesleğe yeni giriş kapanmıştır',
            'E': 'Değişiklik tarihinde unvanı taşıyanların kazanılmış hakları korunmuştur',
        },
        'B',
        "5786 sayılı Kanun'la 3568 sayılı Kanun'da yapılan değişiklikten sonra SERBEST MUHASEBECİ unvanıyla mesleğe YENİ GİRİŞ KAPANMIŞTIR. O tarihte unvanı taşıyanların kazanılmış hakları korunmuş, şartları taşıyanlara SMMM unvanına geçiş imkânı tanınmıştır. Bugün mesleğe yeni girecekler yalnızca SMMM ve YMM unvanlarını kullanabilir.",
    ),
    # düzey 2
    '0040': patch(
        'Bir meslek mensubuna, hiç deneyiminin bulunmadığı ve uzmanlık gerektiren karmaşık bir iş teklif edilmiştir. Buna göre mesleki yeterlik ilkesi bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İş ancak odanın uygun görüşü alınarak kabul edilebilir',
            'B': 'Ruhsat sahibi olmak her işi kabul etmek için yeterlidir',
            'C': 'Meslek mensubu işi kabul edip sorumluluğu iş sahibine devredebilir',
            'D': 'Mesleki yeterlik değerlendirmesi yalnızca yeminli mali müşavirler için aranır; SMMM her işi kabul edebilir',
            'E': 'Meslek mensubu yeterliği bulunmayan işi kabul etmemeli ya da uzman desteğiyle yürütmelidir',
        },
        'E',
        'Meslek ahlak kuralları (mesleki yeterlik ve özen ilkesi): meslek mensubu, gerekli bilgi, beceri ve deneyime sahip olmadığı işleri kabul etmemeli; kabul edecekse konunun uzmanından destek almalıdır. Sorumluluk iş sahibine devredilemez. Ruhsat sahipliği tek başına her işte yeterlik anlamına gelmez.',
    ),
    # düzey 3
    '0041': patch(
        'Bir yeminli mali müşavir, tasdik yetkisini kullanmayacağını belirterek bir holdingde tam zamanlı hizmet akdiyle çalışmayı ve aynı zamanda bir muhasebe bürosuna ortak olmayı planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bağımlı çalışabilir ancak muhasebe bürosuna ortak olamaz',
            'B': 'Her iki plan da hukuka aykırıdır; YMM bağımlı çalışamaz ve muhasebe bürosuna ortak olamaz',
            'C': "Her iki plan da hukuka uygundur; tasdik yetkisi kullanılmadığı sürece md. 45'teki yasaklar doğmaz",
            'D': 'Her iki plan da odanın izniyle hukuka uygun hâle gelir',
            'E': 'Muhasebe bürosuna ortak olabilir ancak bağımlı çalışamaz',
        },
        'B',
        "3568 md. 45: yeminli mali müşavirler mesleklerini yalnızca BAĞIMSIZ olarak yürütür; gerçek ve tüzel kişilere tabi ve işyerlerine bağlı olarak hizmet akdiyle çalışamazlar. Aynı madde YMM'lerin muhasebe bürosu açmasını ve muhasebe bürolarına ORTAK OLMASINI da yasaklar. Her iki yasak da tasdik yetkisinin kullanılıp kullanılmamasından bağımsızdır ve oda izniyle aşılamaz.",
    ),
    # düzey 3
    '0042': patch(
        'Bir meslek mensubu, bir müşterisinin işleri dolayısıyla öğrendiği ticari sırları, ticari rakibi olan başka bir müşterisine aktarmıştır. Meslek mensubu, iki müşterinin de kendi müvekkili olduğunu ileri sürmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bilgi aynı meslek mensubunun başka bir müşterisine aktarıldığı için sır ifşası sayılmaz',
            'B': 'Meslek mensubu, işleri dolayısıyla öğrendiği bilgi ve sırları üçüncü kişilere ifşa edemez',
            'C': 'Bu davranış aynı zamanda haksız rekabet oluşturabilir',
            'D': 'Sır saklama yükümlülüğü meslek mensubunun yanında çalışanları da kapsar',
            'E': 'Bu davranış disiplin cezası uygulanmasını gerektirebilir',
        },
        'A',
        "3568 md. 43: yükümlülük 'işleri dolayısıyla öğrenilen' tüm bilgi ve sırları kapsar; bilginin aktarıldığı kişinin de müşteri olması ifşayı hukuka uygun hâle GETİRMEZ. Yükümlülük meslek mensubunun yanında çalışanları da bağlar. Fiil ayrıca md. 47 anlamında haksız rekabet ve md. 48 uyarınca disiplin sorumluluğu doğurabilir.",
    ),
    # düzey 2
    '0043': patch(
        'Aşağıdakilerden hangisi serbest muhasebeci mali müşavir olmanın özel şartlarından biri değildir?',
        {
            'A': 'Staj amacıyla üç yıl çalışmış olmak',
            'B': 'Serbest muhasebeci mali müşavirlik ruhsatını almış olmak',
            'C': 'Hukuk, iktisat, maliye veya işletme gibi ilgili dallarda en az lisans düzeyinde öğrenim görmüş olmak',
            'D': 'Serbest muhasebeci mali müşavirlik sınavını kazanmış olmak',
            'E': 'En az on yıl bir meslek mensubunun yanında bağımlı olarak çalışmış olmak',
        },
        'E',
        "3568 md. 5/A: SMMM'nin özel şartları öğrenim, üç yıllık staj, sınav ve ruhsattır. ON YILLIK çalışma şartı md. 6'da YEMİNLİ MALİ MÜŞAVİR olmak için aranan bir koşuldur; SMMM için böyle bir şart yoktur.",
    ),
    # düzey 1
    '0044': patch(
        "Meslek mensubu olmayan bir kişi, kartvizitinde ve tabelasında 'mali müşavir' ibaresini kullanmakta ve müşteri kabul etmektedir. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Yasak yalnızca 'yeminli mali müşavir' unvanı için öngörülmüştür",
            'B': 'Kişi odaya bildirimde bulunursa unvanı kullanabilir',
            'C': 'Kanunda sayılan unvanlar ve yetkiler, ruhsat sahibi olmayanlarca kullanılamaz; bu kullanım yasaktır',
            'D': 'Ticaret siciline tescil edilmişse unvan kullanımı hukuka uygun sayılır',
            'E': 'Unvanın kullanılması serbest olup yalnızca meslek mensuplarına tanınan yetkilerin kullanılması yasaktır',
        },
        'C',
        '3568 md. 3: Kanunda belirtilen unvanları taşımayanlar bu unvanları ya da bu unvanlarla iltibasa yol açacak ibareleri KULLANAMAZ; meslek mensuplarına tanınan yetkileri de kullanamazlar. Yasak hem unvanı hem yetkiyi kapsar ve tüm unvanlar için geçerlidir; odaya bildirim ya da ticaret sicili tescili bu yasağı kaldırmaz.',
    ),
    # düzey 1
    '0045': patch(
        'Meslek mensuplarının sürekli mesleki gelişim ve eğitim yükümlülüğü tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Eğitim yükümlülüğü yalnızca mevzuat değişikliği olduğu yıllarda doğar',
            'B': 'Eğitim yükümlülüğü yalnızca yeminli mali müşavirler için öngörülmüştür',
            'C': 'Sürekli eğitim meslek mensubunun kişisel tercihine bırakılmış olup mesleki bir yükümlülük değildir',
            'D': 'Meslek mensubu, mesleki bilgi ve becerisini yeterli düzeyde tutmak için sürekli eğitimi sürdürmelidir',
            'E': 'Ruhsat alındıktan sonra eğitim yükümlülüğü sona erer',
        },
        'D',
        "Meslek ahlak kuralları (mesleki yeterlik ve özen ilkesi): meslek mensubu, iş sahibine yeterli düzeyde hizmet verebilmek için mesleki bilgi ve becerisini SÜREKLİ olarak güncel tutmakla yükümlüdür. TÜRMOB'un sürekli mesleki gelişim düzenlemeleri bu ilkeyi somutlaştırır ve tüm meslek mensuplarını kapsar.",
    ),
    # düzey 3
    '0046': patch(
        'Meslek mevzuatı ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Meslek mensubu ile iş sahibi arasındaki ilişki kural olarak vekâlet sözleşmesidir. II. Meslek mensupları asgari ücret tarifesinin altında iş kabul edebilir. III. YMM yaptığı yanlış tasdikten mükellefle birlikte müteselsilen sorumludur. IV. Meslek mensubu, ücret alacağı için iş sahibinin defterlerini alıkoyabilir.',
        {
            'A': 'I, II ve IV',
            'B': 'Yalnız II',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'II ve IV',
        },
        'E',
        'II YANLIŞ: 3568 md. 46 uyarınca tarifede yazılı asgari ücretin altında iş kabul edilemez. IV YANLIŞ: iş sahibine ait defter ve belgeler talep hâlinde tutanakla geri verilir; ücret alacağı alıkoyma hakkı vermez. I doğrudur (TBK md. 502 vd.), III doğrudur (md. 12/4).',
    ),
    # düzey 3
    '0047': patch(
        'Bir yeminli mali müşavir, bir mükellefin beyannamesinin gerçeği yansıtmadığını bildiği hâlde tasdik etmiş; idare bu tasdike dayanarak işlem tesis etmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Fiil ayrıca disiplin cezası uygulanmasını gerektirebilir',
            'B': 'YMM, ziyaa uğratılan vergilerden ve kesilen cezalardan mükellefle birlikte müteselsilen sorumlu olur',
            'C': 'Sorumluluk, yapılan tasdikin kapsamı ile sınırlıdır',
            'D': 'Fiil koşulları varsa cezai sorumluluk da doğurabilir',
            'E': 'Tasdikin gerçeğe aykırı olması yalnızca disiplin sorumluluğu doğurur; mali sorumluluk doğmaz',
        },
        'E',
        '3568 md. 12/4: yanlış tasdik hâlinde YMM, tasdikin kapsamıyla sınırlı olmak üzere ziyaa uğratılan vergilerden ve cezalardan mükellefle müteselsilen MALİ olarak sorumludur. Bu sorumluluk disiplin (md. 48) ve cezai sorumluluğu ORTADAN KALDIRMAZ; üçü birlikte gündeme gelebilir.',
    ),
    # düzey 1
    '0048': patch(
        'Bir meslek mensubu, hazırladığı raporda iş sahibinin lehine olacak biçimde bazı bulguları yumuşatmıştır. Buna göre tarafsızlık ilkesi bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tarafsızlık yalnızca kamu kurumlarına verilen raporlarda aranır',
            'B': 'Meslek mensubu iş sahibinin çıkarını gözetmekle yükümlüdür',
            'C': 'Meslek mensubu bulgularını taraf tutmaksızın raporlamalıdır; lehe yumuşatma tarafsızlığa aykırıdır',
            'D': 'Tarafsızlık ilkesi yalnızca yeminli mali müşavirler için geçerlidir',
            'E': 'Bulguların iş sahibi lehine yumuşatılması, iş sahibinin yazılı onayı bulunması hâlinde hukuka uygundur',
        },
        'C',
        'Meslek ahlak kuralları: TARAFSIZLIK (objektiflik), meslek mensubunun mesleki yargısını önyargı, çıkar çatışması ya da başkalarının etkisi altında bırakmamasını gerektirir. Bulguların taraflardan biri lehine değiştirilmesi bu ilkeyi ihlal eder; iş sahibinin onayı ihlali hukuka uygun kılmaz.',
    ),
    # düzey 1
    '0049': patch(
        'Meslek mensubunun dürüstlük ilkesi tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Dürüstlük ilkesinin ihlali disiplin sorumluluğu doğurabilir',
            'B': 'Meslek mensubu tüm mesleki ilişkilerinde doğru ve dürüst davranmalıdır',
            'C': 'Dürüstlük ilkesi, meslek mensubunun beyanlarının doğruluğunu da kapsar',
            'D': 'Dürüstlük ilkesi yalnızca kamu kurumlarıyla ilişkilerde geçerli olup iş sahibiyle ilişkilerde uygulanmaz',
            'E': 'Meslek mensubu, önemli ölçüde yanıltıcı veya gerçeğe aykırı bilgi içeren beyan ve raporlara adını koymamalıdır',
        },
        'D',
        'Meslek ahlak kuralları: DÜRÜSTLÜK, meslek mensubunun tüm mesleki ve iş ilişkilerinde açık sözlü ve doğru olmasını gerektirir; muhatap ayrımı yapmaz. Meslek mensubu, önemli ölçüde yanlış ya da yanıltıcı bilgi içeren beyan ve raporlarla ilişkilendirilmemelidir. İhlal md. 48 uyarınca disiplin sorumluluğu doğurur.',
    ),
    # düzey 2
    '0050': patch(
        'Meslek unvanları ve yetkileri ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Mesleğe yeni girecekler serbest muhasebeci unvanını kullanamaz. II. Tasdik yetkisi yalnızca yeminli mali müşavirlere aittir. III. Meslek unvanlarını taşımayanlar bu unvanları kullanamaz.',
        {
            'A': 'I, II ve III',
            'B': 'I ve II',
            'C': 'I ve III',
            'D': 'Yalnız I',
            'E': 'II ve III',
        },
        'A',
        "Üç ifade de doğrudur. 5786 sayılı Kanun değişikliğiyle serbest muhasebeci unvanına yeni giriş kapanmış (I), tasdik yetkisi 3568 md. 2/B ve md. 12 uyarınca yalnızca YMM'ye tanınmış (II), md. 3 ise unvanların yetkisiz kişilerce kullanılmasını yasaklamıştır (III).",
    ),
    # düzey 2
    '0051': patch(
        'Bir meslek mensubu, başka bir meslek mensubunun sürmekte olan müşterisini devralmak istemektedir. Önceki meslek mensubunun ücret alacağı henüz ödenmemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşi devralan meslek mensubu önceki meslektaşına bildirimle yükümlü değildir; önceki meslek mensubunun ücret alacağı da kendisine geçer',
            'B': 'Meslek mensubu işi doğrudan kabul edebilir; meslektaşa bildirim gerekmez',
            'C': 'Meslek mensubu işi kabul etmeden önce önceki meslektaşına yazılı bildirimde bulunmalı ve alacak durumunu araştırmalıdır',
            'D': 'İş devri ancak önceki meslek mensubunun yazılı onayıyla mümkündür',
            'E': 'İş devri yalnızca oda kararıyla gerçekleşebilir',
        },
        'C',
        'Meslek ahlak kuralları ve md. 47: bir meslektaşın işini devralmak isteyen meslek mensubu, işi kabul etmeden önce ÖNCEKİ MESLEK MENSUBUNA yazılı olarak bildirimde bulunur ve ücret alacağının bulunup bulunmadığını araştırır. Bu, haksız rekabeti önlemeye yöneliktir; meslektaşın onayı ya da oda kararı koşul değildir ve alacak yeni meslek mensubuna geçmez.',
    ),
    # düzey 1
    '0052': patch(
        'Bir meslek mensubu, mesleki faaliyetinden doğabilecek zararlara karşı mesleki sorumluluk sigortası yaptırmayı değerlendirmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sigorta yaptıran meslek mensubu disiplin sorumluluğundan da kurtulur',
            'B': 'Sigorta, meslek mensubunun kanuni sorumluluğunu tümüyle ortadan kaldırır',
            'C': 'Sigorta, tasdikten doğan müteselsil sorumluluğu iş sahibine devreder',
            'D': "Mesleki sorumluluk sigortası yalnızca yeminli mali müşavirler için mümkün olup SMMM'ler bu sigortayı yaptıramaz",
            'E': 'Mesleki sorumluluk sigortası, meslek mensubunun mevzuattan doğan sorumluluğunu ortadan kaldırmaz',
        },
        'E',
        "Mesleki sorumluluk sigortası, meslek mensubunun mesleki faaliyetinden doğan ZARARIN karşılanmasına yöneliktir. Sigorta ilişkisi meslek mensubunun 3568 md. 12'den ve VUK mükerrer 227'den doğan KANUNİ sorumluluğunu ortadan kaldırmaz; disiplin ve cezai sorumluluğu ise hiç etkilemez.",
    ),
    # düzey 3
    '0053': patch(
        'Bir serbest muhasebeci mali müşavir, defterlerini tuttuğu bir limited şirkete ortak olmayı planlamaktadır. Meslek mensubu, şirkette yönetici sıfatı almayacağını belirtmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ortaklık ilişkisi tarafsızlığı zedelediğinden meslek mensubu bu şirkete mesleki hizmet veremez',
            'B': 'Meslek mensubu hiçbir limited şirkete ortak olamaz',
            'C': 'Ortaklık ancak yeminli mali müşavirler için engel oluşturur',
            'D': 'Ortaklık ilişkisi odaya bildirilirse mesleki hizmet verilebilir',
            'E': 'Meslek mensubu yönetici sıfatı almadığı için ortaklık ilişkisi mesleki hizmet vermeye engel oluşturmaz',
        },
        'A',
        '3568 md. 45 meslek mensuplarının limited ve anonim şirketlere ORTAK OLMASINA izin verir; ancak meslek ahlak kuralları, hizmet verilen işletmeyle ortaklık ilişkisi bulunmasını TARAFSIZLIĞA aykırı sayar. Yani ortaklık genel olarak serbest, fakat aynı işletmeye mesleki hizmet vermek bağdaşmaz. Bildirim bu sakatlığı gidermez.',
    ),
    # düzey 2
    '0054': patch(
        'Bir meslek mensubu, verdiği hizmet karşılığındaki ücretini iş sahibinden tahsil edememiştir. Meslek mensubu izleyeceği yolu belirlemek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu, ücret alacağını tahsil edene kadar iş sahibine ait defter ve belgeleri elinde tutma hakkına sahiptir',
            'B': 'Ücret alacağı için genel hükümlere göre dava veya icra yoluna başvurabilir; oda arabuluculuk yapabilir',
            'C': 'Meslek mensubu yalnızca odaya başvurabilir; yargı yolu kapalıdır',
            'D': 'Ücret uyuşmazlıkları zorunlu tahkime tabidir',
            'E': 'Ücret alacakları için yalnızca icra yoluna başvurulabilir, dava açılamaz',
        },
        'B',
        'Ücret alacağı özel hukuk alacağıdır; meslek mensubu genel hükümlere göre dava açabilir ya da icra takibi yapabilir. Odalar uyuşmazlıklarda arabuluculuk yapabilir. Ancak meslek mensubu, iş sahibine ait defter ve belgeleri ücret alacağı nedeniyle ALIKOYAMAZ; bunlar talep hâlinde geri verilir.',
    ),
    # düzey 2
    '0055': patch(
        'Aşağıdakilerden hangisi meslek mensuplarının uyması gereken temel mesleki etik ilkelerden biri değildir?',
        {
            'A': 'Sır saklama ve mesleğe uygun davranış',
            'B': 'Mesleki yeterlik ve mesleki faaliyette gerekli özeni gösterme',
            'C': 'Dürüstlük ve doğru sözlülük',
            'D': 'İş sahibinin çıkarını her koşulda kamu yararının önünde tutmak',
            'E': 'Tarafsızlık ve bağımsızlık',
        },
        'D',
        'Meslek ahlak kurallarının temel ilkeleri dürüstlük, tarafsızlık, mesleki yeterlik ve özen, gizlilik (sır saklama) ve mesleğe uygun davranıştır. Meslek mensubu iş sahibinin temsilcisi değil, KAMU YARARINI da gözeten bir meslek mensubudur; iş sahibinin çıkarını kamu yararının önünde tutmak ilke değil, ilkelere aykırılıktır.',
    ),
    # düzey 2
    '0056': patch(
        'Bir meslek mensubuna, bağımsızlığını koruyamayacağı bir iş teklif edilmiştir. Meslek mensubu işi reddetmeyi düşünmekte, ancak reddin haksız rekabet sayılabileceğinden endişe etmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Red ancak odanın izniyle mümkündür',
            'B': 'Meslek mensubu bağımsızlığını koruyamayacağı işi reddetmekle yükümlüdür; bu red haksız rekabet oluşturmaz',
            'C': 'Meslek mensubu işi reddetmekte serbesttir; ancak red gerekçesini iş sahibine açıklaması mesleki yasağa girer',
            'D': 'Bağımsızlık değerlendirmesi yalnızca tasdik işleri için yapılır',
            'E': 'Meslek mensubu kendisine teklif edilen işi reddedemez',
        },
        'B',
        'Meslek ahlak kuralları: meslek mensubu, bağımsızlığını ve tarafsızlığını koruyamayacağı ya da mesleki yeterliğinin yetmediği işleri KABUL ETMEMELİDİR. İşin reddi mesleki bir yükümlülüktür; oda izni gerekmez ve md. 47 anlamında haksız rekabet oluşturmaz.',
    ),
    # düzey 2
    '0057': patch(
        'Serbest muhasebeci mali müşavir ile yeminli mali müşavirin ortak ve ayrı yönleri karşılaştırılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tasdik yetkisi yalnızca yeminli mali müşavire aittir',
            'B': 'Her ikisi de sır saklama, reklam ve ticaret yasaklarına uyar',
            'C': 'Muhasebe defterlerinin tutulması yalnızca serbest muhasebeci mali müşavirin görev alanına girer',
            'D': "Her ikisi de 3568 sayılı Kanun'a tabi olup ruhsat alır ve odaya kaydolur",
            'E': 'Her ikisi de muhasebe ile ilgili defterleri tutmaya ve mali tabloları tasdik etmeye yetkilidir',
        },
        'E',
        "SMMM ve YMM aynı Kanuna tabidir, ruhsat alır, odaya kaydolur ve md. 43-47'deki yasaklara uyar. Ancak yetkiler AYRIDIR: TASDİK yalnızca YMM'ye (md. 2/B, md. 12), DEFTER TUTMA ise yalnızca SMMM'ye aittir (md. 2/A, md. 45). Hiçbir unvan iki yetkiyi birden taşımaz.",
    ),
    # düzey 2
    '0058': patch(
        'Bir serbest muhasebeci mali müşavir, tuttuğu defterlerdeki kayıtların ve düzenlediği belgelerin doğruluğundan sorumlu tutulmuştur. Meslek mensubu, kendisine ibraz edilen belgelere dayandığını ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu, kayıtların kendisine ibraz edilen belgelere uygunluğundan sorumludur; belgelerin gerçekliğini araştırma yükümlülüğü bulunmaz',
            'B': 'Belgelere dayanan meslek mensubunun hiçbir sorumluluğu doğmaz',
            'C': 'Meslek mensubu, kayıtların belgelere uygunluğunun yanında kendisine ibraz edilen belgelerin gerçeği yansıtıp yansıtmadığından da ayrıca sorumludur',
            'D': 'Sorumluluk, iş sahibiyle yapılan sözleşmeyle tümüyle kaldırılabilir',
            'E': 'Sorumluluk yalnızca beyanname imzalanmışsa doğar',
        },
        'A',
        'VUK mükerrer md. 227 ve meslek mevzuatı: meslek mensubu, kayıtların kendisine ibraz edilen BELGELERE uygunluğundan sorumludur; belgelerin muhteviyatının maddi gerçeğe uygun olup olmadığını araştırma yükümlülüğü yoktur. Ancak sorumluluk sözleşmeyle tümüyle kaldırılamaz; kanuni bir sorumluluktur.',
    ),
    # düzey 2
    '0059': patch(
        'Meslek hukuku esasları bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Serbest muhasebeci mali müşavir olabilmek için üç yıl staj yapmak gerekir',
            'B': 'Yeminli mali müşavir olabilmek için en az on yıl serbest muhasebeci mali müşavir olarak çalışmış olmak gerekir',
            'C': 'Serbest muhasebeci mali müşavirler mali tablo ve beyannameleri tasdik etmeye yetkilidir',
            'D': 'Tasdik yetkisi yalnızca yeminli mali müşavirlere aittir',
            'E': 'Yeminli mali müşavirler muhasebe ile ilgili defterleri tutamaz',
        },
        'C',
        "3568 md. 2/B ve md. 12: TASDİK yetkisi yalnızca yeminli mali müşavirlere aittir; SMMM'nin böyle bir yetkisi yoktur. Diğer seçenekler doğrudur: md. 45 YMM'nin defter tutma yasağını, md. 6 on yıllık çalışma şartını, md. 5 üç yıllık staj şartını düzenler.",
    ),
    # düzey 3
    '0060': patch(
        'Meslek hukuku esasları ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Meslek mensupları işleri dolayısıyla öğrendikleri sırları ifşa edemez. II. Meslek mensubunun tanıklık yapması sırrın ifşası sayılır. III. Meslek mensupları arasında haksız rekabet serbesttir. IV. Yeminli mali müşavirler mesleklerini yalnızca bağımsız olarak yürütür.',
        {
            'A': 'I ve IV',
            'B': 'III ve IV',
            'C': 'II ve III',
            'D': 'I, II ve III',
            'E': 'Yalnız II',
        },
        'C',
        'II YANLIŞ: 3568 md. 43 uyarınca adli veya idari inceleme ve soruşturmalar sır saklama hükmünün kapsamı dışındadır ve TANIKLIK sırrın ifşası sayılmaz. III YANLIŞ: md. 47 meslek mensupları arasında haksız rekabeti yasaklar. I (md. 43) ve IV (md. 45) doğrudur.',
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
    print(f"1 paket / {len(PATCHES)} soru (Meslek Hukuku Esaslari yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
