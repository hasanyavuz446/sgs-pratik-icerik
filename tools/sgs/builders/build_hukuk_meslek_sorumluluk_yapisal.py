#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sorumluluk ve Yasaklar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turunun 7. konusu. Paketin 60 sorusunun TAMAMI
yeniden yazildi.

    olcut                gercek   once   sonra
    medyan kok              257    122     156
    olumsuz kok           %41,5     %0     %42
    ayni kok kalibi           —  51/60       —

⚠️ ASIL KUSUR OLCUM DUZELTMESI: 51/60 soru "...bakimindan asagidakilerden hangisi
dogrudur?" kalibindaydi (§2). Onceki turlarda kullandigim tanim-regex'i bu
ifadeyi KACIRIYORDU ve paketi "%2 tanim" diye temiz gosteriyordu; kalip tekrari
bu turda dogrudan olculdu.

⚠️ SAHIPLIK DEVRI — bu pakette BES builder soru tutuyordu:
  · fix_meslek_length_quality      39 soru  -> blok CIKARILDI
  · build_legal_oncul_cleanup      sorum-gen-0005 -> blok CIKARILDI
  · build_option_balance_cleanup   sorum-gen-0037 -> blok CIKARILDI
  · fix_lexical_tell / fix_bekleyen_denge  paket duzeyi mekanik listeler,
    yerinde birakildi (yeni metin yasak kalip tasimadigi icin idempotent).
Bir sorunun tek sahibi olmali; aksi hâlde iki builder ayni metne yazar.

IKI KAPI: §5 boy (ilk tasarim 44/60 = %73 cikip uretimi DURDURDU; 44 celdirici
dogru sikla PARALEL yapiya tasinarak %28) · §1 bilissel duzey (0 = 4 <=6,
0+1 = 8 <=24, duzey 2 = 39 >=24, duzey 3 = 13 >=12).

Dayanak: 3568 sayili Kanun md. 1, 12, 43, 44, 45, 46, 47, 48 · VUK mukerrer
md. 227 ve md. 359 · TBK md. 49 vd., 162 vd., 502 vd., 506 · Anayasa md. 129 ·
Meslek Ahlak Kurallari.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/meslek_hukuku/sorumluluk_ve_yasaklar.json"
STYLE_REF = "SGS Meslek Hukuku (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "sorum-gen-"


def patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": "3568 sayili Kanun / VUK mukerrer md. 227"},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        'Bir meslek mensubu, iş sahibinin talebiyle gerçeğe aykırı bir kayıt yapmış; bu kayda dayanan beyanname nedeniyle vergi ziyaı doğmuş, müşteri de zarara uğramıştır. Fiil ayrıca kamuya yansımıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Disiplin sorumluluğu meslek örgütü önünde, cezai sorumluluk ceza yargısında doğar',
            'B': 'Hukuki sorumluluk, meslek mensubunun kusuruyla verdiği zararın tazminini kapsar',
            'C': 'Meslek mensubu aynı fiil nedeniyle disiplin, hukuki ve cezai sorumluluğa birlikte tabi olabilir',
            'D': 'İş sahibinin talebi meslek mensubunun sorumluluğunu ortadan kaldırmaz',
            'E': 'Meslek mensubu hakkında disiplin süreci başlatıldığında hukuki ve cezai sorumluluk gündeme gelmez',
        },
        'E',
        'Meslek mensubunun disiplin (3568 md. 48), HUKUKİ (TBK md. 49 vd. ve vekâlet hükümleri) ve CEZAİ sorumluluğu AYRI REJİMLERDİR; aynı fiil için birlikte doğabilir ve biri diğerini ortadan kaldırmaz. İş sahibinin talimatı meslek mensubunu sorumluluktan kurtarmaz.',
    ),
    # düzey 2
    '0002': patch(
        'Bir meslek mensubu, meslek kurallarına aykırı davranışı nedeniyle hakkında işlem yapılmasını beklemektedir. Buna göre disiplin sorumluluğu bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Savunma hakkı tanınmadan disiplin cezası verilemez',
            'B': 'İlk derece disiplin cezasını oda disiplin kurulu verir',
            'C': 'Disiplin sorumluluğu meslek örgütü önünde doğar',
            'D': 'Disiplin cezası verilebilmesi için fiilin ayrıca suç oluşturması gerekir',
            'E': 'Kesinleşen disiplin cezasına karşı idari yargıda iptal davası açılabilir',
        },
        'D',
        'Disiplin sorumluluğu, meslek düzenini korumaya yönelik bağımsız bir rejimdir; fiilin ayrıca SUÇ oluşturması ARANMAZ. 3568 md. 48 disiplin cezalarını, Anayasa md. 129 savunma hakkını, İYUK ise kesinleşen cezaya karşı yargı yolunu düzenler.',
    ),
    # düzey 3
    '0003': patch(
        'Bir meslek mensubu, özensiz davranarak müşterisinin defterlerini hatalı tutmuş; hata nedeniyle müşteri idari para cezasına muhatap olmuştur. Meslek mensubu, sözleşmede sorumluluğunu kaldıran bir kayıt bulunduğunu ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Zarardan yalnızca müşteri sorumludur; meslek mensubuna başvurulamaz',
            'B': 'Sorumluluğu kaldıran sözleşme kaydı geçerli olduğundan meslek mensubunun bu olayda hiçbir sorumluluğu doğmaz',
            'C': 'Meslek mensubu kusuruyla verdiği zarardan sorumludur; kanuni sorumluluğu kaldıran sözleşme kaydı geçersizdir',
            'D': 'Meslek mensubu ancak kastı bulunması hâlinde sorumlu tutulabilir',
            'E': 'Sorumluluk yalnızca beyanname imzalanmışsa doğar',
        },
        'C',
        "Meslek mensubu ile iş sahibi arasındaki ilişki vekâlettir (TBK md. 502 vd.); meslek mensubu işi ÖZENLE görmekle yükümlüdür ve kusuruyla verdiği zarardan sorumludur. Sorumluluk kast koşuluna bağlı değildir; VUK mükerrer md. 227 ve 3568'den doğan KANUNİ sorumluluk ise sözleşmeyle kaldırılamaz.",
    ),
    # düzey 2
    '0004': patch(
        'Bir meslek mensubunun mesleğiyle bağlantılı bir fiili, kanunda suç olarak tanımlanmıştır. Buna göre cezai sorumluluk bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Aynı fiil ayrıca disiplin ve hukuki sorumluluk doğurabilir',
            'B': 'Sahte belge düzenlemek veya bilerek kullanmak ayrıca cezai sorumluluk doğurabilir',
            'C': 'Meslek mensubu hakkında disiplin cezası verilmişse ayrıca ceza yargılaması yapılamaz',
            'D': 'Cezai sorumluluk ceza yargısında, genel hükümlere göre belirlenir',
            'E': 'İş sahibinin talimatı cezai sorumluluğu ortadan kaldırmaz',
        },
        'C',
        "Disiplin ve cezai sorumluluk AYRI REJİMLERDİR; biri diğerini engellemez ve 'aynı fiilden iki kez cezalandırma' yasağını ihlal etmez. Vergi suçları VUK md. 359'da, genel suçlar TCK'da düzenlenmiştir; talimat cezai sorumluluğu kaldırmaz.",
    ),
    # düzey 2
    '0005': patch(
        'Meslek mensubunun mesleki faaliyeti nedeniyle karşılaşabileceği sorumluluklar ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Disiplin sorumluluğu meslek örgütü önünde doğar. II. Hukuki sorumluluk, kusurla verilen zararın tazminini kapsar. III. Disiplin cezası verilmişse ayrıca cezai sorumluluk doğmaz.',
        {
            'A': 'I ve II',
            'B': 'I ve III',
            'C': 'II ve III',
            'D': 'I, II ve III',
            'E': 'Yalnız I',
        },
        'A',
        'I ve II doğrudur. III YANLIŞTIR: disiplin ve cezai sorumluluk ayrı rejimlerdir; aynı fiil için birlikte doğabilir ve biri diğerini engellemez.',
    ),
    # düzey 3
    '0006': patch(
        'Bir serbest muhasebeci mali müşavir, defterlerini tuttuğu mükellefin beyannamesini imzalamıştır. Beyannamedeki bir tutarın defter kayıtlarına aykırı olduğu, kayıtların dayanağı belgelerin ise sahte olduğu sonradan anlaşılmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sorumluluk, meslek mensubunun aldığı ücretle sınırlıdır',
            'B': 'Sorumluluk yalnızca yeminli mali müşavirler için doğar',
            'C': 'Meslek mensubunun hiçbir sorumluluğu doğmaz; beyanname mükellefe aittir',
            'D': 'Meslek mensubu her iki durumdan da sorumludur; kendisine ibraz edilen belgelerin gerçekliğini araştırmalıydı',
            'E': 'Meslek mensubu kayıtlara aykırılıktan sorumludur; belgelerin sahteliğini araştırma yükümlülüğü bulunmaz',
        },
        'E',
        'VUK mükerrer md. 227: beyannameyi imzalayan meslek mensupları, imzaladıkları beyannamelerde yer alan bilgilerin DEFTER KAYITLARINA ve bu kayıtların dayanağını oluşturan BELGELERE uygun olmamasından sorumludur. Belgelerin muhteviyatının maddi gerçeği yansıtıp yansıtmadığını araştırma yükümlülüğü yoktur; sorumluluk ücretle de sınırlanamaz.',
    ),
    # düzey 3
    '0007': patch(
        'Bir yeminli mali müşavir, gerçeği yansıtmayan bir beyannameyi tasdik etmiş; tasdik nedeniyle vergi ziyaı doğmuş ve mükellef adına vergi ile ceza tarh edilmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Koşulları varsa cezai sorumluluk da doğabilir',
            'B': 'Yeminli mali müşavirin sorumluluğu ikinci derecededir; önce mükellefin malvarlığına başvurulur',
            'C': 'Fiil ayrıca disiplin sorumluluğu doğurabilir',
            'D': 'Sorumluluk, yapılan tasdikin kapsamı ile sınırlıdır',
            'E': 'YMM, ziyaa uğratılan vergiden ve kesilecek cezalardan mükellefle birlikte müteselsilen sorumludur',
        },
        'B',
        '3568 md. 12/4: yeminli mali müşavirler yaptıkları tasdikin doğru olmaması hâlinde, tasdikin kapsamıyla sınırlı olmak üzere ziyaa uğratılan vergilerden ve kesilecek cezalardan mükellefle birlikte MÜTESELSİLEN sorumludur. Müteselsil sorumlulukta alacaklı borçlulardan herhangi birine doğrudan başvurabilir; sıra koşulu yoktur.',
    ),
    # düzey 2
    '0008': patch(
        'Bir vergi alacağı için hem mükellefe hem de beyannameyi imzalayan meslek mensubuna başvurulabileceği belirtilmiştir. Buna göre müşterek ve müteselsil sorumluluk bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Müteselsil sorumluluk yalnızca yeminli mali müşavirler için öngörülmüştür',
            'B': 'Alacak, borçlular arasında eşit paylara bölünerek talep edilir',
            'C': 'Alacaklı, borcun tamamı için borçlulardan dilediğine başvurabilir; sıra gözetmesi gerekmez',
            'D': 'Alacaklı önce mükellefe başvurur; ondan sonuç alamazsa ikinci derecede meslek mensubuna yönelebilir',
            'E': 'Meslek mensubu ödeme yaparsa mükellefe rücu edemez',
        },
        'C',
        "Müteselsil sorumlulukta alacaklı, borcun tamamı için borçlulardan HERHANGİ BİRİNE ya da hepsine birden başvurabilir; sıra ya da eşit paylaşım söz konusu değildir (TBK md. 162 vd.). Ödeyen borçlu diğerlerine rücu edebilir. Sorumluluk VUK mükerrer md. 227 uyarınca SMMM'leri, 3568 md. 12 uyarınca YMM'leri kapsar.",
    ),
    # düzey 2
    '0009': patch(
        'Bir meslek mensubu, sorumluluğunun kapsamını sözleşmeyle daraltmak istemektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu, kanundan doğan sorumluluğunu sözleşmeyle iş sahibine devredebilir',
            'B': 'İş sahibinin yazılı talimatı sorumluluğu kaldırmaz',
            'C': 'Kanuni sorumluluk sözleşmeyle ortadan kaldırılamaz',
            'D': 'Sorumluluk disiplin, hukuki ve cezai boyutlarıyla ayrı ayrı doğar',
            'E': 'Mesleki sorumluluk sigortası, meslek mensubunun kanuni sorumluluğunu ortadan kaldırmaz',
        },
        'A',
        "Meslek mensubunun VUK mükerrer md. 227 ve 3568'den doğan sorumluluğu KANUNİDİR; sözleşmeyle kaldırılamaz ya da devredilemez. Mesleki sorumluluk sigortası yalnızca zararın karşılanmasına yöneliktir; kanuni, disiplin ve cezai sorumluluğu etkilemez.",
    ),
    # düzey 3
    '0010': patch(
        'Müşterek ve müteselsil sorumluluk ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Beyannameyi imzalayan meslek mensubu, kayıtlara aykırılıktan mükellefle birlikte sorumlu olabilir. II. YMM, yanlış tasdikten mükellefle birlikte müteselsilen sorumludur. III. Alacaklı, önce mükellefe başvurmak ve sonuç alamazsa meslek mensubuna yönelmek durumundadır. IV. Meslek mensubu, kanuni sorumluluğunu sözleşmeyle kaldırabilir.',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'Yalnız III',
            'D': 'I, III ve IV',
            'E': 'III ve IV',
        },
        'E',
        'III YANLIŞ: müteselsil sorumlulukta alacaklı borçlulardan dilediğine doğrudan başvurabilir; sıra koşulu yoktur (TBK md. 162 vd.). IV YANLIŞ: kanuni sorumluluk sözleşmeyle kaldırılamaz. I (VUK mük. md. 227) ve II (3568 md. 12/4) doğrudur.',
    ),
    # düzey 2
    '0011': patch(
        "Bir meslek mensubu, bürosunun tabelasını yönetmelikte öngörülen ölçüler içinde asmış; ayrıca yerel bir gazeteye 'en uygun ücret' vurgusuyla ilan vermiştir. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Reklam yasağı yalnızca yeminli mali müşavirleri bağlar',
            'B': 'Her ikisi de reklam yasağını ihlal eder',
            'C': 'İş elde etmeye yönelik gazete ilanı serbesttir; yalnızca tabela ölçüsü aşılırsa ihlal doğar',
            'D': 'Her ikisi de serbesttir; meslek mevzuatı reklamı yasaklamaz',
            'E': 'Tabela reklam sayılmaz; iş elde etmeye yönelik gazete ilanı reklam yasağını ihlal eder',
        },
        'E',
        "3568 md. 44: meslek mensupları iş elde etmek için açık veya kapalı, dolaylı ya da dolaysız REKLAM SAYILABİLECEK faaliyetlerde bulunamazlar. Yönetmelikte belirlenen ölçüler içindeki tabela ve kartvizit reklam sayılmaz; ücret vurgusuyla iş çağrısı ise ayrıca md. 46 ve 47'ye de aykırıdır.",
    ),
    # düzey 3
    '0012': patch(
        'Bir meslek mensubu; bir anonim şirkete sermaye ortağı olmayı, kendi adına bir kırtasiye işletmesi açmayı ve bir limited şirkette ticari vekil sıfatıyla görev almayı planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kırtasiye işletebilir ancak şirkete ortak olamaz ve ticari vekil olamaz',
            'B': 'Ticari vekil olarak çalışabilir; ortaklık ve ticaret ise yasaktır',
            'C': 'Meslek mensubu üçünü de yapabilir; meslek mevzuatı ortaklık ve ticareti serbest bırakmıştır',
            'D': 'Anonim şirkete ortak olabilir; kırtasiye işletemez ve ticari vekil olarak çalışamaz',
            'E': 'Üçü de yasaktır; meslek mensubu hiçbir şirkete ortak olamaz',
        },
        'D',
        '3568 md. 45: meslek mensupları meslek icrası sırasında TİCARİ FAALİYETTE bulunamaz ve ticari mümessil, ticari vekil ya da acente olarak çalışamazlar. Ancak sermayesi paylara bölünmüş komandit şirketlerde komanditer, limited ve anonim şirketlerde ORTAK olabilirler; sermaye ortaklığı bizzat ticaret yapmaktan farklıdır.',
    ),
    # düzey 2
    '0013': patch(
        'Bir meslek mensubunun, mesleğin gereği ve onuruyla bağdaşmayan bir işle uğraştığı belirlenmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yasak tüm meslek mensuplarını bağlar',
            'B': 'Yasak mesleğin saygınlığını zedeleyen davranışları da kapsar',
            'C': 'Yasak yalnızca ticari faaliyetlerle sınırlı olup diğer davranışları kapsamaz',
            'D': 'Meslek mensupları mesleğin gereği ve onuruyla bağdaşmayan işlerle uğraşamaz',
            'E': 'Aykırılık disiplin sorumluluğu doğurabilir',
        },
        'C',
        '3568 md. 45: meslek mensupları, mesleğin gereği ve onuruyla BAĞDAŞMAYAN işlerle uğraşamazlar. Yasak ticari faaliyetle sınırlı değildir; mesleğin saygınlığını zedeleyen her davranışı kapsar ve md. 48 uyarınca disiplin cezası gerektirir.',
    ),
    # düzey 2
    '0014': patch(
        'Bir meslek mensubu, meslektaşının müşterisine ulaşarak tarifenin altında ücret teklif etmiş ve meslektaşının yetersiz olduğunu söylemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yalnızca meslektaş hakkındaki beyan haksız rekabet oluşturur',
            'B': 'Haksız rekabet yalnızca ticari işletmeler arasında söz konusu olup meslek mensuplarını kapsamaz',
            'C': 'Serbest piyasa koşullarında iki davranış da hukuka uygundur',
            'D': 'Yalnızca tarifenin altında teklif haksız rekabet oluşturur',
            'E': 'Her iki davranış da haksız rekabet oluşturur ve disiplin sorumluluğu doğurur',
        },
        'E',
        '3568 md. 46 tarifenin altında iş kabul edilemeyeceğini, md. 47 ise meslek mensupları arasında haksız rekabetin yasak olduğunu düzenler. Meslektaşı küçük düşüren beyanlar ve tarifenin altında fiyatla iş almaya çalışmak haksız rekabet sayılır; md. 48 uyarınca disiplin cezası gerektirir.',
    ),
    # düzey 3
    '0015': patch(
        'Meslek mensupları için öngörülen yasaklar ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Meslek mensupları meslek icrası sırasında ticari faaliyette bulunamaz. II. Meslek mensupları ticari mümessil, ticari vekil veya acente olarak çalışamaz. III. Meslek mensupları limited ve anonim şirketlere ortak olamaz. IV. Meslek mensupları iş elde etmek için reklam yapamaz.',
        {
            'A': 'I, II, III ve IV',
            'B': 'I ve III',
            'C': 'Yalnız I',
            'D': 'I, II ve IV',
            'E': 'II ve III',
        },
        'D',
        'I, II ve IV doğrudur (3568 md. 45 ve 44). III YANLIŞTIR: md. 45 meslek mensuplarının sermayesi paylara bölünmüş komandit şirketlerde komanditer ortak, limited ve anonim şirketlerde ORTAK olmasına açıkça izin verir.',
    ),
    # düzey 3
    '0016': patch(
        'Bir meslek mensubu; müşterisine ait bilgiyi (I) kanunla yetkili kılınmış bir idari incelemede idareye vermiş, (II) mahkemede tanık sıfatıyla açıklamış, (III) bir yatırım kararında kendi yararına kullanmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'I ve II sır ifşası sayılmaz; III yasaktır',
            'B': 'Üçü de sır ifşası sayılır',
            'C': 'Yalnızca III sır ifşası sayılmaz; I ve II yasaktır',
            'D': 'Üçü de hukuka uygundur',
            'E': 'Yalnızca I sır ifşası sayılmaz; II ve III yasaktır',
        },
        'A',
        '3568 md. 43: meslek mensupları işleri dolayısıyla öğrendikleri bilgi ve sırları ifşa edemez ve KENDİ YARARLARINA KULLANAMAZLAR. Ancak ADLİ VEYA İDARİ her türlü inceleme ve soruşturma bu hükmün kapsamı dışındadır ve TANIKLIK sırrın ifşası sayılmaz.',
    ),
    # düzey 2
    '0017': patch(
        'Bir yeminli mali müşavir, tasdik hizmeti verdiği şirkette pay sahibidir ve şirketin yönetim kurulunda görev almaktadır. Buna göre bağımsızlık bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Pay sahipliği ve yöneticilik bağımsızlığı etkilemez',
            'B': 'Bağımsızlık ortadan kalktığından meslek mensubu bu şirkete tasdik hizmeti veremez',
            'C': 'Bağımsızlık yalnızca bağımsız denetim işlerinde aranır',
            'D': 'Durum iş sahibine bildirilirse tasdik hizmeti verilebilir',
            'E': 'Meslek mensubu yöneticilikten ayrılırsa pay sahipliği tek başına engel oluşturmaz',
        },
        'B',
        '3568 md. 45 ve Meslek Ahlak Kuralları: hizmet verilen işletmeye ortak olmak ya da yönetiminde görev almak, kişisel çıkar ve kendi kendini denetleme tehditlerini doğurarak bağımsızlığı ORTADAN KALDIRIR. Bildirim bu sakatlığı gidermez; bağımsızlık tasdik işlerinin kurucu koşuludur.',
    ),
    # düzey 2
    '0018': patch(
        'Bir meslek mensubu, hazırladığı raporda iş sahibi lehine sonuç doğuracak biçimde bulguları yumuşatmıştır. Buna göre tarafsızlık ilkesi bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bulguların iş sahibi lehine düzenlenmesi, iş sahibinin yazılı onayı varsa hukuka uygundur',
            'B': 'Meslek mensubu, mesleki yargısını başkalarının uygunsuz etkisi altında bırakmamalıdır',
            'C': 'Bulgular taraf tutmaksızın raporlanmalıdır',
            'D': 'Meslek mensubu iş sahibinin temsilcisi değildir',
            'E': 'Tarafsızlık ihlali disiplin sorumluluğu doğurabilir',
        },
        'A',
        'TARAFSIZLIK ilkesi, mesleki yargının önyargı, çıkar çatışması ve uygunsuz etkilerden korunmasını gerektirir. Bulguların taraflardan biri lehine değiştirilmesi bu ilkeyi ihlal eder; iş sahibinin ONAYI ihlali hukuka uygun kılmaz.',
    ),
    # düzey 2
    '0019': patch(
        'Sır saklama yükümlülüğünün istisnaları belirlenmektedir. Buna göre aşağıdakilerden hangisi bu istisnalardan biri değildir?',
        {
            'A': 'Meslek mensubunun bilgiyi kendi ticari kararında kullanması',
            'B': 'Kanunla yetkili kılınmış merciin talebi',
            'C': 'İdari inceleme veya soruşturma kapsamında bilgi istenmesi',
            'D': 'Meslek mensubunun mahkemede tanıklık yapması',
            'E': 'Adli inceleme veya soruşturma kapsamında bilgi istenmesi',
        },
        'A',
        '3568 md. 43: adli veya idari her türlü inceleme ve soruşturma sır saklama hükmünün kapsamı dışındadır ve tanıklık ifşa sayılmaz. Buna karşılık meslek mensubunun bilgiyi KENDİ YARARINA kullanması istisna değil, açıkça yasaklanmış bir davranıştır.',
    ),
    # düzey 2
    '0020': patch(
        'Bir meslek mensubu, iş sahibiyle asgari ücret tarifesinin altında bir ücret üzerinde anlaşmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Taraflar ücreti serbestçe belirleyebilir; tarife yol göstericidir',
            'B': 'Tarifede belirlenen tutarın altında iş kabul edilemez; aykırılık disiplin sorumluluğu doğurur',
            'C': 'Tarifenin altında ücret kararlaştırılması, taraflar arasındaki sözleşmeyi baştan kesin hükümsüz kılar',
            'D': 'Tarife yalnızca yeminli mali müşavirlik işleri için bağlayıcıdır',
            'E': 'Tarife üst sınırı gösterir; altında ücret kararlaştırmak serbesttir',
        },
        'B',
        '3568 md. 46: ücretin asgari tutarı tarifeyle belirlenir ve meslek mensupları tarifede yazılı ASGARİ ücretin altında iş kabul edemezler. Tarife TABAN tutarı gösterir. Aykırılık sözleşmeyi kendiliğinden hükümsüz kılmaz; md. 48 uyarınca disiplin sorumluluğu doğurur.',
    ),
    # düzey 3
    '0021': patch(
        'Sorumluluk türleri ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Meslek mensubu aynı fiil nedeniyle disiplin, hukuki ve cezai sorumluluğa birlikte tabi olabilir. II. Mesleki sorumluluk sigortası kanuni sorumluluğu ortadan kaldırır. III. İş sahibinin yazılı talimatı meslek mensubunu sorumluluktan kurtarır. IV. Kesinleşen disiplin cezasına karşı idari yargı yolu açıktır.',
        {
            'A': 'I ve IV',
            'B': 'III ve IV',
            'C': 'II ve III',
            'D': 'I, II ve III',
            'E': 'Yalnız II',
        },
        'C',
        'II YANLIŞ: sigorta yalnızca zararın karşılanmasına yöneliktir; kanuni, disiplin ve cezai sorumluluğu ortadan kaldırmaz. III YANLIŞ: yazılı talimat sorumluluğu kaldırmaz. I ve IV doğrudur.',
    ),
    # düzey 2
    '0022': patch(
        'Sır saklama yükümlülüğü ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Yükümlülük meslek mensubunun yanında çalışanları da kapsar. II. Yükümlülük iş ilişkisi sona erdikten sonra da devam eder. III. Meslek mensubu öğrendiği bilgiyi kendi yararına kullanabilir.',
        {
            'A': 'II ve III',
            'B': 'I ve III',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'Yalnız I',
        },
        'C',
        'I ve II doğrudur (3568 md. 43 ve Meslek Ahlak Kuralları). III YANLIŞTIR: md. 43 meslek mensubunun bilgiyi ifşa etmesini VE kendi yararına kullanmasını birlikte yasaklar.',
    ),
    # düzey 3
    '0023': patch(
        'Bir meslek mensubu, defterlerini tuttuğu şirkete aynı dönemde ortak olmuş; ortaklığını odaya bildirmiş ve mesleki hizmeti sürdürmüştür. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ortaklık yalnızca yeminli mali müşavirler için engel oluşturur',
            'B': 'Şirkete ortak olmak serbest olmakla birlikte aynı şirkete mesleki hizmet vermek tarafsızlıkla bağdaşmaz',
            'C': 'Meslek mensubu hiçbir limited veya anonim şirkete ortak olamaz',
            'D': 'Hizmet verilen şirkete ortak olmak, meslek mensubunun ruhsatının kendiliğinden düşmesi sonucunu doğurur',
            'E': 'Ortaklık ve mesleki hizmet birlikte yürütülebilir; bildirim yeterlidir',
        },
        'B',
        '3568 md. 45 meslek mensuplarının limited ve anonim şirketlere ORTAK OLMASINA izin verir; ancak Meslek Ahlak Kuralları, hizmet verilen işletmeyle ortaklık ilişkisini TARAFSIZLIĞA aykırı sayar. Bildirim bu sakatlığı gidermez ve ruhsat kendiliğinden düşmez.',
    ),
    # düzey 2
    '0024': patch(
        'Bir meslek mensubu, iş sahibinden aldığı defter ve belgeleri iş ilişkisi sona erdikten sonra ücret alacağı ödenene kadar teslim etmeyeceğini bildirmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Belgeler yalnızca vergi dairesinin talebi üzerine geri verilir',
            'B': 'Defter ve belgeleri geri verme yükümlülüğü yalnızca yeminli mali müşavirler için öngörülmüştür',
            'C': 'Meslek mensubu belgeleri geri vermek yerine imha edebilir',
            'D': 'Meslek mensubu ücreti ödenene kadar belgeleri alıkoyabilir',
            'E': 'Defter ve belgeler talep hâlinde tutanakla geri verilir; ücret alacağı alıkoyma hakkı vermez',
        },
        'E',
        'Meslek mevzuatı: iş sahibine ait defter ve belgeler özenle saklanır ve iş ilişkisi sona erdiğinde TUTANAKLA geri verilir. Yasal saklama yükümlülüğü bulunan bu belgeler üzerinde ücret alacağı alıkoyma (hapis) hakkı vermez; alacak genel hükümlere göre takip edilir.',
    ),
    # düzey 3
    '0025': patch(
        'Bir meslek mensubu, bir şirkette tam zamanlı hizmet akdiyle çalışırken kendi bürosunda da serbest olarak üç mükellefe hizmet vermeyi sürdürmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yeminli mali müşavirler mesleklerini yalnızca bağımsız olarak yürütür',
            'B': 'Meslek mensupları ticari mümessil, ticari vekil veya acente olarak çalışamaz',
            'C': 'Meslek mensubu bağımlı çalışırken kendi adına serbest meslek faaliyetini de sürdürebilir',
            'D': 'Bağımlı çalışan meslek mensubu ruhsatını korur ancak serbest meslek faaliyeti yapamaz',
            'E': 'Meslek mensubu ya bağımsız ya da bağımlı olarak çalışır',
        },
        'C',
        '3568 md. 45: meslek mensupları gerçek ve tüzel kişilere tabi ve onların işyerlerine bağlı olarak hizmet akdiyle çalışamazlar. Bağımlı çalışan SMMM ruhsatını korur ancak aynı anda kendi adına SERBEST MESLEK FAALİYETİ yürütemez.',
    ),
    # düzey 2
    '0026': patch(
        'Bir meslek mensubu, mesleki yeterliği bulunmayan karmaşık bir işi kabul etmiş ve hatalı bir rapor düzenlemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yeterlik değerlendirmesi yalnızca tasdik işlerinde aranır',
            'B': 'Meslek mensubu yeterliği bulunmayan işi kabul etmemeli ya da uzman desteği almalıydı; hatadan sorumludur',
            'C': 'Meslek mensubu sorumluluğu sözleşmeyle iş sahibine devredebilir',
            'D': 'Sorumluluk yalnızca iş sahibinin işi doğru anlatmamasından doğar',
            'E': 'Meslek mensubu ruhsat sahibi olduğu için her işi kabul etmekte serbesttir ve hatadan sorumluluğu doğmaz',
        },
        'B',
        'Meslek Ahlak Kuralları (mesleki yeterlik ve özen): meslek mensubu gerekli bilgi, beceri ve deneyime sahip olmadığı işleri kabul etmemeli, kabul edecekse uzman desteği almalıdır. Özen borcunun ihlali hukuki sorumluluk doğurur (TBK md. 506) ve sorumluluk devredilemez.',
    ),
    # düzey 2
    '0027': patch(
        'Bir meslek mensubu, iş sahibinin gerçeğe aykırı kayıt talebini reddetmiş; iş sahibi sözleşmeyi sona erdirmekle tehdit etmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu sözleşme süresince talebi reddedemez',
            'B': 'Meslek mensubu talebi yerine getirip durumu sonradan odaya bildirebilir',
            'C': 'Meslek mensubu işini kaybetmemek için talebi yerine getirebilir',
            'D': 'Meslek mensubu, iş sahibi talimatı yazılı olarak verdiği takdirde talebi yerine getirebilir',
            'E': 'Meslek mensubu talebi reddetmekle doğru davranmıştır; ısrar hâlinde işi bırakabilir',
        },
        'E',
        'Meslek mensubu iş sahibinin talimatıyla değil MEVZUAT ve mesleki ilkelerle bağlıdır. Gerçeğe aykırı kayıt dürüstlük ilkesini ihlal eder; yazılı talimat sorumluluğu kaldırmaz ve ayrıca VUK ile TCK sorumluluğu doğurur. Israr hâlinde iş bırakılabilir.',
    ),
    # düzey 2
    '0028': patch(
        'Bir meslek mensubunun yanında çalışan personel, müşteriye ait bilgileri dışarı sızdırmıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Fiil ayrıca tazminat sorumluluğu doğurabilir',
            'B': 'Yükümlülük meslek mensubunun yanında çalışanları da kapsar',
            'C': 'Meslek mensubu, kendi büro düzeni içinde gizliliği sağlayacak her türlü önlemi almakla yükümlüdür',
            'D': 'Sır saklama yükümlülüğü yalnızca meslek mensubunu bağlar; personelin fiili mesleki sonuç doğurmaz',
            'E': 'Fiil disiplin sorumluluğu doğurabilir',
        },
        'D',
        '3568 md. 43: meslek mensupları VE YANLARINDA ÇALIŞANLAR, işleri dolayısıyla öğrendikleri bilgi ve sırları ifşa edemezler. Meslek mensubu gizliliği sağlayacak önlemleri almakla yükümlüdür; fiil disiplin ve tazminat sorumluluğu doğurabilir.',
    ),
    # düzey 2
    '0029': patch(
        'Meslek mensubunun yasaklar bakımından durumu değerlendirilmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu, bir ticari işletmenin ticari mümessili olarak çalışabilir',
            'B': 'Meslek mensubu, meslek icrası sırasında kendi adına ya da başkası hesabına ticari faaliyette bulunamaz',
            'C': 'Meslek mensubu limited ve anonim şirketlere ortak olabilir',
            'D': 'Meslek mensubu mesleğin onuruyla bağdaşmayan işlerle uğraşamaz',
            'E': 'Meslek mensubu hizmet akdiyle bağlı çalışırken serbest meslek faaliyeti yapamaz',
        },
        'A',
        '3568 md. 45: meslek mensupları TİCARİ MÜMESSİL, ticari vekil ya da acente olarak ÇALIŞAMAZLAR. Buna karşılık aynı madde limited ve anonim şirketlere ortak olmalarına izin verir; ticaret ve bağımlı çalışma ise yasaktır.',
    ),
    # düzey 2
    '0030': patch(
        'Meslek mensubunun hukuki sorumluluğu bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu yalnızca kastı bulunması hâlinde hukuki sorumluluk altına girer',
            'B': 'İlişki kural olarak vekâlet sözleşmesidir',
            'C': 'Meslek mensubu, iş sahibine ya da üçüncü kişiye kusuruyla verdiği zarardan sorumludur',
            'D': 'Meslek mensubu işi özenle görmekle yükümlüdür',
            'E': 'Kanuni sorumluluk sözleşmeyle kaldırılamaz',
        },
        'A',
        "TBK md. 502 vd. ve 506: vekil işi özenle görmekle yükümlüdür ve KUSURUYLA verdiği zarardan sorumludur; sorumluluk KAST koşuluna bağlı değildir, ihmal de yeterlidir. VUK mükerrer md. 227 ve 3568'den doğan kanuni sorumluluk ise sözleşmeyle kaldırılamaz.",
    ),
    # düzey 1
    '0031': patch(
        'Meslek mensubunun mesleki faaliyeti nedeniyle uğradığı zararı tazmin borcu doğuran sorumluluk türü aşağıdakilerden hangisidir?',
        {
            'A': 'Disiplin sorumluluğu türü',
            'B': 'Cezai sorumluluk',
            'C': 'Anayasal sorumluluk',
            'D': 'Hukuki sorumluluk',
            'E': 'İdari sorumluluk',
        },
        'D',
        'HUKUKİ SORUMLULUK, meslek mensubunun kusuruyla verdiği zararın tazminini kapsar; vekâlet (TBK md. 502 vd.) ve haksız fiil (TBK md. 49 vd.) hükümlerine dayanır.',
    ),
    # düzey 1
    '0032': patch(
        'Bir meslek mensubu hakkında, mesleki kurallara aykırılık nedeniyle meslek örgütü önünde işlem yapılmıştır. Buna göre söz konusu sorumluluk türü aşağıdakilerden hangisidir?',
        {
            'A': 'Cezai sorumluluk',
            'B': 'Vergisel sorumluluk',
            'C': 'Kusursuz sorumluluk',
            'D': 'Disiplin sorumluluğu türü',
            'E': 'Hukuki sorumluluk',
        },
        'D',
        "DİSİPLİN SORUMLULUĞU, meslek kurallarına aykırılık nedeniyle meslek örgütü (oda ve Birlik disiplin kurulları) önünde doğar ve 3568 md. 48'deki cezaları gerektirir. Hukuki sorumluluk zararın tazminini, cezai sorumluluk ise ceza yargısını ilgilendirir.",
    ),
    # düzey 1
    '0033': patch(
        'Bir meslek mensubunun kusuruyla müşterisine verdiği zararın tazmini gündeme gelmiştir. Buna göre söz konusu sorumluluk türü aşağıdakilerden hangisidir?',
        {
            'A': 'Cezai sorumluluk',
            'B': 'Hukuki (mali) sorumluluk',
            'C': 'İdari sorumluluk',
            'D': 'Siyasi sorumluluk',
            'E': 'Disiplin sorumluluğu türü',
        },
        'B',
        'HUKUKİ (MALİ) SORUMLULUK, meslek mensubunun kusuruyla müşteriye ya da üçüncü kişiye verdiği zararın tazminini kapsar; vekâlet ilişkisi ve haksız fiil hükümlerine dayanır (TBK md. 49 vd., 502 vd.).',
    ),
    # düzey 1
    '0034': patch(
        'Meslek mensubunun mesleğiyle bağlantılı bir fiili kanunda suç olarak tanımlanmıştır. Buna göre söz konusu sorumluluk türü aşağıdakilerden hangisidir?',
        {
            'A': 'Cezai sorumluluk',
            'B': 'Müteselsil sorumluluk',
            'C': 'Hukuki sorumluluk',
            'D': 'Disiplin sorumluluğu türü',
            'E': 'Kusursuz sorumluluk',
        },
        'A',
        'CEZAİ SORUMLULUK, fiilin kanunda suç olarak tanımlanması hâlinde ceza yargısında doğar (VUK md. 359, TCK ilgili hükümleri). Disiplin ve hukuki sorumluluktan ayrı bir rejimdir ve onlarla birlikte doğabilir.',
    ),
    # düzey 2
    '0035': patch(
        'Bir meslek mensubu, mesleki sorumluluk sigortası yaptırmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sigorta, tasdikten doğan müteselsil sorumluluğu iş sahibine devreder',
            'B': "Mesleki sorumluluk sigortası yalnızca yeminli mali müşavirler için mümkün olup SMMM'ler bu sigortayı yaptıramaz",
            'C': 'Sigorta meslek mensubunun tüm sorumluluklarını ortadan kaldırır',
            'D': 'Sigorta doğan zararın karşılanmasına yöneliktir; kanuni, disiplin ve cezai sorumluluğu ortadan kaldırmaz',
            'E': 'Sigorta yaptıran meslek mensubu disiplin sorumluluğundan kurtulur',
        },
        'D',
        "Mesleki sorumluluk sigortası, mesleki faaliyetten doğan ZARARIN karşılanmasına yöneliktir. Meslek mensubunun 3568 md. 12 ve VUK mükerrer md. 227'den doğan KANUNİ sorumluluğunu ortadan kaldırmaz; disiplin ve cezai sorumluluğu ise hiç etkilemez.",
    ),
    # düzey 2
    '0036': patch(
        'Bir meslek mensubu, sorumluluğunun zamanaşımına uğradığını ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubunun sorumluluğunda zamanaşımı işlemez',
            'B': 'Zamanaşımı süreleri taraflarca sözleşmeyle belirlenir',
            'C': 'Disiplin, hukuki ve cezai sorumluluk için tek ve ortak bir zamanaşımı süresi uygulanır',
            'D': 'Disiplin, hukuki ve cezai sorumluluk için ayrı zamanaşımı rejimleri uygulanır',
            'E': 'Zamanaşımı yalnızca cezai sorumluluk için öngörülmüştür',
        },
        'D',
        "Her sorumluluk türü kendi rejimine tabidir: disiplin zamanaşımı Disiplin Yönetmeliğinde, hukuki sorumluluk zamanaşımı TBK'da (vekâlet ve haksız fiil hükümleri), cezai sorumluluk zamanaşımı ise TCK ve VUK'ta düzenlenmiştir. Süreler kanunla belirlenir; sözleşmeye bırakılmaz.",
    ),
    # düzey 2
    '0037': patch(
        'Bir meslek mensubu, tasdik hizmeti verdiği işletmeye aynı dönemde defter tutma hizmeti de vermeyi planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sorun yalnızca ücretlerin aynı faturada gösterilmesinden doğar',
            'B': 'Tehdit yalnızca meslek mensubu işletmeye ortak da olursa doğar',
            'C': 'Durum iş sahibine bildirilirse tehdit ortadan kalkar',
            'D': 'Defter tutma ve tasdik hizmetlerinin birlikte verilmesi bağımsızlık bakımından herhangi bir sorun doğurmaz',
            'E': 'Kendi tuttuğu kayıtları tasdik etmek kendi kendini denetleme tehdidi doğurur; ayrıca YMM defter tutamaz',
        },
        'E',
        'Kendi tuttuğu kayıtları sonradan tasdik etmek KENDİ KENDİNİ DENETLEME tehdidi doğurur. Ayrıca 3568 md. 45 uyarınca yeminli mali müşavirler muhasebe ile ilgili defterleri TUTAMAZ; tasdik ve defter tutma işleri unvan bakımından da ayrılmıştır.',
    ),
    # düzey 2
    '0038': patch(
        'Bir meslek mensubu, başka bir meslek mensubunun müşterisini devralmak istemektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Önceki meslek mensubunun alacağı yeni meslek mensubuna geçmez',
            'B': 'İşi devralacak meslek mensubunun önceki meslektaşa bildirimde bulunması gerekmez',
            'C': 'İşi devralacak meslek mensubu, kabul öncesinde önceki meslektaşa yazılı bildirimde bulunur',
            'D': 'Bildirim yükümlülüğü haksız rekabeti önlemeye yöneliktir',
            'E': 'Önceki meslek mensubunun ücret alacağı araştırılır',
        },
        'B',
        'Meslek Ahlak Kuralları ve 3568 md. 47: bir meslektaşın işini devralmak isteyen meslek mensubu, işi kabul etmeden önce ÖNCEKİ MESLEK MENSUBUNA yazılı bildirimde bulunur ve ücret alacağı durumunu araştırır. Bu yükümlülük haksız rekabeti önlemeye yöneliktir.',
    ),
    # düzey 2
    '0039': patch(
        'Reklam yasağı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Belirlenen ölçüler içindeki tabela ve kartvizit reklam sayılmaz',
            'B': 'Yasağın ihlali disiplin sorumluluğu doğurur',
            'C': 'Yasak açık ve kapalı her türlü reklamı kapsar',
            'D': 'İş elde etmeye yönelik reklam sayılabilecek her türlü faaliyet yasaktır',
            'E': 'Meslek mensubu, iş elde etmek amacıyla dolaylı yollarla tanıtım yapabilir',
        },
        'E',
        '3568 md. 44: meslek mensupları iş elde etmek için AÇIK VEYA KAPALI, DOLAYLI YA DA DOLAYSIZ reklam sayılabilecek faaliyetlerde bulunamazlar. Yasak dolaylı yolları da kapsar.',
    ),
    # düzey 2
    '0040': patch(
        'Bir meslek mensubu, iş sahibinin bilgisi dışında onun rakibine de hizmet vermeye başlamıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bilgi bariyeri, ayrı ekip görevlendirme ve bağımsız gözden geçirme birer önlem olarak kullanılabilir',
            'B': 'Önlemler yetersizse işlerden biri bırakılır',
            'C': 'Meslek mensubu iki rakip müşteriye hizmet verirken bilgilendirme ve önlem yükümlülüğü altında değildir',
            'D': 'Durum çıkar çatışması doğurabilir',
            'E': 'Meslek mensubu ilgilileri bilgilendirmelidir',
        },
        'C',
        'Meslek Ahlak Kuralları: rakip müşterilere aynı anda hizmet vermek çıkar çatışması doğurur. Meslek mensubu çatışmayı belirler, ilgilileri BİLGİLENDİRİR ve önlem alır; önlemler yeterli olmuyorsa işlerden biri bırakılır.',
    ),
    # düzey 2
    '0041': patch(
        'Meslek mensubunun ücreti bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ücret uyuşmazlığı belge alıkoyma hakkı vermez',
            'B': 'Asgari ücret tarifesinin altında iş kabul edilemez',
            'C': 'Ücret işin kapsamı ve gerektirdiği emek gözetilerek belirlenir',
            'D': 'Tasdik gibi güvence gerektiren işlerde sonuca bağlı ücret meslek mensubunun bağımsızlığını zedeler',
            'E': 'Meslek mensubu iş almak amacıyla asgari ücret tarifesinin altında fiyat verebilir',
        },
        'E',
        '3568 md. 46: meslek mensupları tarifede yazılı ASGARİ ücretin altında iş kabul edemezler; aksi davranış md. 48 uyarınca disiplin cezası gerektirir ve md. 47 anlamında haksız rekabet oluşturur.',
    ),
    # düzey 2
    '0042': patch(
        'Bir meslek mensubu, tasdik ücretinin mükellefe sağlanacak vergi avantajının bir yüzdesi olarak belirlenmesini kabul etmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sonuca bağlı ücret kişisel çıkar tehdidi doğurur ve tasdik işlerinde bağımsızlıkla bağdaşmaz',
            'B': 'Düzenleme yalnızca asgari ücret tarifesi bakımından sorun doğurur; meslek mensubunun bağımsızlığını etkilemez',
            'C': 'Sonuca bağlı ücret yalnızca danışmanlık işlerinde yasaktır',
            'D': 'Ücretin serbestçe belirlenmesi mümkün olduğundan sorun doğmaz',
            'E': 'Düzenleme iş sahibinin yazılı onayıyla etik hâle gelir',
        },
        'A',
        'Koşullu (sonuca bağlı) ücret, meslek mensubunun yargısını sonuca bağladığı için KİŞİSEL ÇIKAR tehdidi doğurur ve tasdik gibi güvence işlerinde bağımsızlıkla bağdaşmaz. İş sahibinin onayı bu sakatlığı gidermez.',
    ),
    # düzey 2
    '0043': patch(
        'Bir meslek mensubu, aynı ihalede karşı karşıya gelen iki şirkete de danışmanlık vermektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Çıkar çatışması ancak müşterilerden biri şikâyet ederse sonuç doğurur',
            'B': 'Çıkar çatışması yalnızca tasdik işlerinde söz konusu olur',
            'C': 'Çıkar çatışması doğmuştur; taraflar bilgilendirilmeli, önlem yeterli olmuyorsa işlerden biri bırakılmalıdır',
            'D': 'İki müşteriye hizmet vermek serbest olduğundan etik sorun doğmaz',
            'E': 'Meslek mensubu iki işi de sürdürebilir; ücretleri ayrı ayrı faturalandırması ve ayrı kayıt tutması yeterlidir',
        },
        'C',
        'Meslek Ahlak Kuralları: çıkar çatışması tarafsızlığı doğrudan tehdit eder. Meslek mensubu çatışmayı belirler, ilgilileri bilgilendirir ve önlem alır (ayrı ekip, bilgi bariyeri, gözden geçirme); önlemler yeterli olmuyorsa işlerden biri ya da her ikisi bırakılır.',
    ),
    # düzey 2
    '0044': patch(
        'Bir meslek mensubuna, tasdik hizmeti verdiği müşterisi tarafından yüksek değerli bir hediye sunulmuştur. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Hediye ancak nakit olarak verildiğinde etik sorun doğurur',
            'B': 'Hediye kabulü meslek mensubunun kişisel takdirinde olup bağımsızlık bakımından sorun doğurmaz',
            'C': 'Hediye, değeri odaya bildirilirse kabul edilebilir',
            'D': 'Hediye yasağı yalnızca kamu görevlileri için öngörülmüştür',
            'E': 'Önemsiz sayılamayacak hediyeler kişisel çıkar tehdidi doğurduğundan kabul edilmemelidir',
        },
        'E',
        'Meslek Ahlak Kuralları: müşteriden alınan hediye ve ağırlamalar önemsiz ve makul düzeyi aşıyorsa KİŞİSEL ÇIKAR ve YAKINLIK tehdidi doğurur; kabul edilmemelidir. Yasak nakitle sınırlı değildir ve odaya bildirim bir önlem oluşturmaz.',
    ),
    # düzey 0
    '0045': patch(
        'Meslek mensubunun aynı fiil nedeniyle hem meslek örgütü hem ceza yargısı önünde sorumlu olabilmesi neyi gösterir?',
        {
            'A': 'Meslek mensubunun iki süreçten birini seçebileceğini',
            'B': 'Disiplin ve cezai sorumluluğun ayrı rejimler olduğunu',
            'C': 'Cezai sorumluluğun disiplin sorumluluğunu ortadan kaldırdığını',
            'D': 'Disiplin sürecinin ceza yargılamasının sonucunu beklediğini',
            'E': 'Disiplin sorumluluğunun cezai sorumluluğa dönüştüğünü',
        },
        'B',
        'Disiplin sorumluluğu meslek düzenini, cezai sorumluluk kamu düzenini korur. İkisi AYRI REJİMLERDİR; aynı fiil için birlikte doğabilir, biri diğerini ortadan kaldırmaz ve meslek mensubunun seçim hakkı yoktur.',
    ),
    # düzey 0
    '0046': patch(
        'Beyannameyi imzalayan meslek mensubunun sorumluluğunun kaynağı aşağıdakilerden hangisidir?',
        {
            'A': "Vergi Usul Kanunu'nun mükerrer 227. maddesi",
            'B': "Türk Ticaret Kanunu'nun haksız rekabet hükümleri",
            'C': "İş Kanunu'nun işveren sorumluluğu hükümleri",
            'D': "Türk Borçlar Kanunu'nun eser sözleşmesi hükümleri",
            'E': "Anayasa'nın sosyal güvenlik hükümleri",
        },
        'A',
        'VUK mükerrer md. 227: beyannameyi imzalayan meslek mensupları, beyannamelerde yer alan bilgilerin defter kayıtlarına ve bu kayıtların dayanağı belgelere uygun olmamasından sorumludur ve ziyaa uğratılan vergi ile cezalardan mükellefle müteselsilen sorumlu olur.',
    ),
    # düzey 0
    '0047': patch(
        'Yeminli mali müşavirin tasdikten doğan müteselsil sorumluluğunun kaynağı aşağıdakilerden hangisidir?',
        {
            'A': "3568 sayılı Kanun'un 12. maddesi",
            'B': "Türk Borçlar Kanunu'nun 49. maddesi",
            'C': "Türk Ticaret Kanunu'nun 18. maddesi",
            'D': "3568 sayılı Kanun'un 45. maddesi",
            'E': "3568 sayılı Kanun'un 43. maddesi",
        },
        'A',
        '3568 md. 12/4: yeminli mali müşavirler yaptıkları tasdikin doğru olmaması hâlinde, tasdikin kapsamıyla sınırlı olmak üzere ziyaa uğratılan vergilerden ve kesilecek cezalardan mükellefle birlikte müteselsilen sorumludur. md. 43 sır saklamayı, md. 45 yasakları düzenler.',
    ),
    # düzey 0
    '0048': patch(
        'Meslek mensupları için öngörülen ticaret yasağının kaynağı aşağıdakilerden hangisidir?',
        {
            'A': "Vergi Usul Kanunu'nun mükerrer 227. maddesi",
            'B': "Türk Ticaret Kanunu'nun tacir hükümleri",
            'C': "3568 sayılı Kanun'un 45. maddesi",
            'D': "3568 sayılı Kanun'un 46. maddesi",
            'E': "3568 sayılı Kanun'un 12. maddesi",
        },
        'C',
        '3568 md. 45: meslek mensupları meslek icrası sırasında ticari faaliyette bulunamaz, hizmet akdiyle çalışamaz ve ticari mümessil, ticari vekil ya da acente olarak görev alamazlar; ancak limited ve anonim şirketlere ortak olabilirler.',
    ),
    # düzey 2
    '0049': patch(
        'Bir meslek mensubu, bağımsızlığını koruyamayacağı bir işi reddetmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu kendisine teklif edilen işi reddedemez',
            'B': 'İşin reddi, meslek mensubu hakkında disiplin soruşturması açılmasını gerektirir',
            'C': 'Red mesleki bir yükümlülüğün yerine getirilmesidir; haksız rekabet oluşturmaz',
            'D': 'Red ancak odanın yazılı izniyle mümkündür',
            'E': 'Red serbesttir ancak gerekçenin iş sahibine açıklanması yasaktır',
        },
        'C',
        'Meslek Ahlak Kuralları: meslek mensubu bağımsızlığını ve tarafsızlığını koruyamayacağı ya da yeterliğinin yetmediği işleri KABUL ETMEMEKLE yükümlüdür. Red bir yükümlülüğün yerine getirilmesidir; oda iznine bağlı değildir ve md. 47 anlamında haksız rekabet oluşturmaz.',
    ),
    # düzey 2
    '0050': patch(
        'Bir meslek mensubu, hakkında yürütülen disiplin soruşturmasında savunma hakkı tanınmadan ceza verildiğini ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubuna savunma hakkı tanınması, cezanın ağırlığına göre disiplin kurulunun takdirindedir',
            'B': 'Savunma hakkı tanınmadan disiplin cezası verilemez; bu bir anayasal güvencedir',
            'C': 'Savunma hakkı yalnızca ağır cezalarda aranır',
            'D': 'Savunma hakkı yalnızca ceza yargılamasında geçerlidir',
            'E': 'Savunma alınmaması cezayı geçerli kılmaya engel değildir',
        },
        'B',
        "Anayasa md. 129: 'savunma hakkı tanınmadıkça disiplin cezası verilemez.' Bu güvence cezanın ağırlığına ya da kurulun takdirine bağlı değildir; ihlali kesinleşen cezaya karşı açılacak iptal davasında iptal sebebidir.",
    ),
    # düzey 2
    '0051': patch(
        'Meslek mensubunun sır saklama yükümlülüğü bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yükümlülük iş ilişkisi sona erdikten sonra da sürer',
            'B': 'Yükümlülük kanundan doğar',
            'C': 'Yükümlülük yanında çalışanları da kapsar',
            'D': 'Adli ve idari her türlü inceleme ile soruşturma yükümlülüğün kapsamı dışındadır',
            'E': 'Yükümlülük yalnızca yazılı gizlilik sözleşmesi bulunduğunda doğar',
        },
        'E',
        '3568 md. 43: sır saklama yükümlülüğü KANUNDAN doğar; ayrıca yazılı sözleşme aranmaz. Yükümlülük meslek mensubunu ve yanında çalışanları bağlar, iş ilişkisi bittikten sonra da sürer; adli ve idari inceleme ve soruşturmalar kapsam dışındadır.',
    ),
    # düzey 2
    '0052': patch(
        'Bir meslek mensubu, mesleki faaliyeti dolayısıyla öğrendiği bilgiyi kanunla yetkili kılınmış bir merciin talebi üzerine vermiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Gizlilik yükümlülüğü mutlak olup istisna tanımaz',
            'B': 'Bilgi ancak iş sahibinin yazılı onayıyla verilebilirdi',
            'C': 'Adli ve idari inceleme ile soruşturmalar sır saklama yükümlülüğünün kapsamı dışındadır',
            'D': 'Meslek mensubu bilgiyi vermeyerek gizliliği korumakla yükümlüydü',
            'E': 'Yetkili merciye bilgi verme yükümlülüğü yalnızca yeminli mali müşavirler için öngörülmüştür',
        },
        'C',
        '3568 md. 43: meslek mensupları öğrendikleri bilgi ve sırları ifşa edemezler; ancak ADLİ VEYA İDARİ HER TÜRLÜ İNCELEME VEYA SORUŞTURMA bu hükmün kapsamı DIŞINDADIR. Yetkili merciin talebi karşısında bilgi verilmesi ihlal sayılmaz ve iş sahibinin onayı aranmaz.',
    ),
    # düzey 2
    '0053': patch(
        'Meslek mensubunun tarafsızlığı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu, mesleki yargısını önyargı ve başkalarının uygunsuz etkilerinden uzak tutmakla yükümlüdür',
            'B': 'Tarafsızlık ihlali disiplin sorumluluğu doğurabilir',
            'C': 'Çıkar çatışması bulunan işlerde önlem alınır',
            'D': 'Meslek mensubu, iş sahibinin ticari beklentilerini karşılamak için mesleki yargısını uyarlayabilir',
            'E': 'Meslek mensubu iş sahibinin temsilcisi değildir',
        },
        'D',
        'TARAFSIZLIK ilkesi, mesleki yargının önyargı, çıkar çatışması ve başkalarının uygunsuz etkisi altında bırakılmamasını gerektirir. Yargıyı iş sahibinin ticari beklentilerine uyarlamak bu ilkenin doğrudan ihlalidir.',
    ),
    # düzey 2
    '0054': patch(
        'Meslek mensubunun bağımsızlığı bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bağımsızlık yalnızca danışmanlık işlerinde aranan bir ölçüttür',
            'B': 'Sonuca bağlı ücret bağımsızlığı zedeler',
            'C': 'Hizmet verilen işletmenin yönetiminde görev alınamaz',
            'D': 'Bağımsızlık denetim ve tasdik gibi güvence işlerinde kurucu koşuldur',
            'E': 'Önlemler tehdidi kabul edilebilir düzeye indirmiyorsa iş bırakılır',
        },
        'A',
        'Bağımsızlık, üçüncü kişilere güvence veren DENETİM ve TASDİK işlerinde kurucu koşuldur; danışmanlıkla sınırlı değildir. Kavramsal çerçeve uyarınca tehdit belirlenir, değerlendirilir ve önlem alınır; yetersizse iş bırakılır.',
    ),
    # düzey 2
    '0055': patch(
        'Bir meslek mensubu, mesleğe yeni başlayan bir meslektaşının müşterilerine ulaşarak onun deneyimsiz olduğunu söylemiş ve daha düşük ücret önermiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Davranış serbest piyasa koşullarında hukuka uygundur',
            'B': 'Davranış haksız rekabet oluşturur; ayrıca tarife altı teklif nedeniyle de aykırılık doğar',
            'C': 'Haksız rekabet yalnızca aynı unvanı taşıyan meslek mensupları arasında doğar; farklı unvanlarda uygulanmaz',
            'D': 'Yalnızca meslektaş hakkındaki beyan aykırılık oluşturur',
            'E': 'Yalnızca ücret teklifi aykırılık oluşturur',
        },
        'B',
        "3568 md. 47 meslek mensupları arasında haksız rekabeti yasaklar; meslektaşı küçük düşüren beyanlar ve md. 46'ya aykırı tarife altı teklif birlikte aykırılık oluşturur ve md. 48 uyarınca disiplin cezası gerektirir.",
    ),
    # düzey 2
    '0056': patch(
        'Meslek mensubunun yükümlülükleri bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu mevzuatla ve mesleki ilkelerle bağlıdır',
            'B': 'Meslek mensubu hukuka aykırı talebi reddeder',
            'C': 'Meslek mensubu, faaliyet sonuçlarını ilgililerin ve resmî mercilerin istifadesine tarafsız biçimde sunar',
            'D': 'Meslek mensubu, iş sahibinin çıkarını kamu yararının önünde tutmakla yükümlüdür',
            'E': 'Meslek mensubu mesleki yeterliğini güncel tutar',
        },
        'D',
        '3568 md. 1: mesleğin amacı faaliyet sonuçlarını ilgililerin ve RESMÎ MERCİLERİN istifadesine tarafsız biçimde sunmaktır. Meslek mensubu iş sahibinin temsilcisi değildir; çatışma hâlinde mevzuat ve mesleki ilkeler esas alınır.',
    ),
    # düzey 3
    '0057': patch(
        'Bir meslek mensubu; müşterisinin sahte belge kullandığını fark etmiş, buna rağmen kaydı yapmış ve beyannameyi imzalamıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Fiil cezai sorumluluk doğurabilir',
            'B': 'Meslek mensubu belgeleri araştırmakla yükümlü olmadığından hiçbir sorumluluğu doğmaz',
            'C': 'Meslek mensubu, sahteliği bildiği hâlde kayıt yapmakla dürüstlük ilkesini ihlal eder',
            'D': 'Fiil disiplin sorumluluğu doğurabilir',
            'E': 'Fiil ziyaa uğratılan vergi bakımından müteselsil sorumluluk doğurabilir',
        },
        'B',
        'VUK mükerrer md. 227 meslek mensubuna belgelerin maddi gerçekliğini ARAŞTIRMA yükümlülüğü yüklemez; ancak sahteliği BİLEREK kayıt yapmak farklıdır. Bu, dürüstlük ilkesinin ihlali olup VUK md. 359 kapsamında cezai, md. 48 uyarınca disiplin ve müteselsil mali sorumluluk doğurabilir.',
    ),
    # düzey 2
    '0058': patch(
        'Meslek mensubunun disiplin sorumluluğu bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Disiplin cezasını Hazine ve Maliye Bakanlığı verir',
            'B': 'Disiplin cezasını oda yönetim kurulu verir',
            'C': 'Disiplin cezasını doğrudan idare mahkemesi verir',
            'D': 'Disiplin cezasını ilk derecede oda disiplin kurulu verir; Birlik disiplin kurulu itiraz merciidir',
            'E': 'Disiplin cezasını ilk derecede Birlik disiplin kurulu verir; oda disiplin kurulu itiraz merciidir',
        },
        'D',
        '3568 md. 18, 21 ve 48: disiplin cezası verme yetkisi ilk derecede meslek mensubunun kayıtlı olduğu ODANIN DİSİPLİN KURULUNA aittir; Birlik disiplin kurulu itiraz merciidir. Kesinleşen cezaya karşı idari yargı yolu açıktır.',
    ),
    # düzey 2
    '0059': patch(
        'Meslek mensubunun sorumluluğu ve yasakları bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu asgari ücret tarifesinin altında iş kabul edemez',
            'B': 'Meslek mensubu iş elde etmek için reklam yapamaz',
            'C': 'Meslek mensubu, hizmet akdiyle bağlı çalışırken aynı anda serbest meslek faaliyeti yürütebilir',
            'D': 'Meslek mensubu limited ve anonim şirketlere ortak olabilir',
            'E': 'Meslek mensubu, meslek icrası sırasında kendi adına ya da başkası hesabına ticari faaliyette bulunamaz',
        },
        'C',
        '3568 md. 45: meslek mensupları gerçek ve tüzel kişilere tabi ve işyerlerine bağlı olarak hizmet akdiyle çalışamazlar. Bağımlı çalışan meslek mensubu ruhsatını korur ancak aynı anda SERBEST MESLEK FAALİYETİ yürütemez.',
    ),
    # düzey 3
    '0060': patch(
        'Sorumluluk ve yasaklar ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Meslek mensubu kanuni sorumluluğunu sözleşmeyle kaldırabilir. II. YMM yanlış tasdikten mükellefle birlikte müteselsilen sorumludur. III. Meslek mensupları limited ve anonim şirketlere ortak olamaz. IV. Sır saklama yükümlülüğü iş ilişkisi bittikten sonra da sürer.',
        {
            'A': 'I ve II',
            'B': 'I ve III',
            'C': 'I, III ve IV',
            'D': 'II ve IV',
            'E': 'Yalnız I',
        },
        'B',
        "I YANLIŞ: VUK mükerrer md. 227 ve 3568'den doğan kanuni sorumluluk sözleşmeyle kaldırılamaz. III YANLIŞ: md. 45 meslek mensuplarının limited ve anonim şirketlere ORTAK OLMASINA izin verir. II (md. 12/4) ve IV (md. 43) doğrudur.",
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
    print(f"1 paket / {len(PATCHES)} soru (Sorumluluk ve Yasaklar yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
