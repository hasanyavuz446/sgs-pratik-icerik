#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ticaret Sirketleri — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turunun 9. konusu; ticaret_hukuku dersinin ilk
konusu. Paketin 60 sorusunun TAMAMI yeniden yazildi.

    olcut                gercek   once   sonra
    medyan kok              257     97     158
    olumsuz kok           %41,5     %5     %42
    ayni kok kalibi           —  37/60       —
    onculu                %14,3     %8       —

⚠️ SAHIPLIK: bu pakette yalniz fix_lexical_tell paket duzeyi mekanik listede;
soru bazli sahip yoktu, devir gerekmedi.

⚠️ §9: yila bagli asgari sermaye tutarlari KULLANILMADI (AS/limited asgari
sermayesi mevzuatla degisiyor); "kanunda ongorulen asgari sermaye" denildi.

IKI KAPI: §5 boy (ilk tasarim 40/60 = %67 cikip uretimi DURDURDU; iki turda 50
celdirici dogru sikla PARALEL yapiya tasinarak %25) · §1 bilissel duzey
(0 = 5 <=6, 0+1 = 13 <=24, duzey 2 = 32 >=24, duzey 3 = 15 >=12).

Dayanak: TTK md. 124, 125, 136, 180, 211, 230, 236-237, 304-305, 329, 332, 338,
342, 344, 355, 359, 364, 375, 407-408, 533 vd., 573-574, 584, 595, 616, 623 ·
TBK md. 620 vd. (adi sirket) · 6183 sayili Kanun md. 35 ve mukerrer 35.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/ticaret_hukuku/ticaret_sirketleri.json"
STYLE_REF = "SGS Ticaret Hukuku (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "tic-sirket-gen-"


def patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": "6102 sayili Turk Ticaret Kanunu"},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Bir hukukçu, ortaklık ilişkilerini sınıflandırırken adi şirketi de ticaret şirketleri arasında saymıştır. Buna göre Türk Ticaret Kanunu'nda düzenlenen ticaret şirketleri bakımından aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Ticaret şirketleri tüzel kişiliğe sahiptir',
            'B': "Adi şirket, Türk Ticaret Kanunu'nda düzenlenen ticaret şirketlerinden biridir",
            'C': 'Anonim ve limited şirketler ticaret şirketlerindendir',
            'D': "Kollektif ve komandit şirketler TTK'da sayılan ticaret şirketlerindendir",
            'E': 'Kooperatifler de ticaret şirketleri arasında sayılmıştır',
        },
        'B',
        "TTK md. 124: ticaret şirketleri KOLLEKTİF, KOMANDİT, ANONİM, LİMİTED ve KOOPERATİF şirketlerdir; hepsi tüzel kişiliğe sahiptir. ADİ ŞİRKET ise TTK'da değil TBK md. 620 vd.'da düzenlenmiştir, ticaret şirketi değildir ve TÜZEL KİŞİLİĞİ YOKTUR.",
    ),
    # düzey 3
    '0002': patch(
        'Üç ortaklık kurulmuştur: (A) iki gerçek kişinin sınırsız sorumlu olduğu kollektif şirket, (B) pay sahiplerinin yalnızca taahhüt ettikleri sermaye ile sorumlu olduğu anonim şirket, (C) sermayesi paylara bölünmüş komandit şirket. Buna göre şahıs–sermaye şirketi ayrımı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'A şahıs şirketi; B ve C sermaye şirketidir',
            'B': 'Üçü de şahıs şirketidir',
            'C': 'A şahıs şirketi; B sermaye şirketi; C hiçbir gruba girmez',
            'D': 'A ve C şahıs şirketi; B sermaye şirketidir',
            'E': 'Üçü de sermaye şirketidir',
        },
        'A',
        'TTK md. 124/2: kollektif ile komandit şirket ŞAHIS; anonim, limited ve SERMAYESİ PAYLARA BÖLÜNMÜŞ KOMANDİT şirket ise SERMAYE şirketi sayılır. Sıradan komandit şirket şahıs şirketiyken, sermayesi paylara bölünmüş komandit şirket sermaye şirketidir.',
    ),
    # düzey 2
    '0003': patch(
        'İki kişi, aralarında yazılı bir sözleşmeyle ortak bir iş yürütmek üzere anlaşmış ancak ticaret siciline herhangi bir tescil yaptırmamıştır. Buna göre adi şirket bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Adi şirket Türk Borçlar Kanunu'nda düzenlenmiştir",
            'B': 'Adi şirketin tüzel kişiliği bulunmaz',
            'C': 'Adi şirket tüzel kişiliğe sahip olup kendi adına hak edinip borç altına girebilir',
            'D': 'Adi şirket ticaret şirketi sayılmaz',
            'E': 'Adi şirkette ortaklar, şirket borçlarından kişisel malvarlıklarıyla müteselsilen sorumludur',
        },
        'C',
        'TBK md. 620 vd.: adi şirket, iki veya daha fazla kişinin emeklerini ve mallarını ortak bir amaca erişmek üzere birleştirmeyi üstlendikleri sözleşmedir. TÜZEL KİŞİLİĞİ YOKTUR; hak ve borçlar ortaklara aittir ve ortaklar şirket borçlarından müteselsilen sorumludur.',
    ),
    # düzey 2
    '0004': patch(
        'Üç gerçek kişi, bir ticari işletmeyi ticaret unvanı altında işletmek üzere şirket kurmuş; ortakların hiçbirinin sorumluluğu sınırlandırılmamıştır. Buna göre bu şirket türü bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Şirket komandit şirkettir; ortaklardan biri sınırlı sorumludur',
            'B': 'Şirket limited şirkettir; ortaklar sermaye payları ile sorumludur',
            'C': 'Şirket adi şirkettir; tüzel kişiliği bulunmaz',
            'D': 'Şirket kollektif şirkettir; ortakların tamamı gerçek kişi olup sorumlulukları sınırsızdır',
            'E': 'Şirket anonim şirkettir; ortaklar yalnızca taahhüt ettikleri sermaye payı ile sorumludur',
        },
        'D',
        'TTK md. 211: kollektif şirket, ticari bir işletmeyi bir ticaret unvanı altında işletmek amacıyla GERÇEK KİŞİLER arasında kurulan ve ortaklardan hiçbirinin sorumluluğu şirket alacaklılarına karşı SINIRLANDIRILMAMIŞ olan şirkettir.',
    ),
    # düzey 3
    '0005': patch(
        'Bir kollektif şirketin alacaklısı, şirketten alacağını tahsil edemeyince doğrudan ortaklardan birinin kişisel malvarlığına başvurmak istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Alacaklı doğrudan ortağa başvurabilir; şirkete başvurma koşulu aranmaz',
            'B': 'Alacaklı, ortakların kişisel malvarlığına hiç başvuramaz; yalnızca şirkete gidebilir',
            'C': 'Ortakların kişisel malvarlığına başvurabilmek için şirketin iflasına karar verilmiş olması dahi yeterli değildir',
            'D': 'Ortakların sorumluluğu koydukları sermaye ile sınırlıdır',
            'E': 'Alacaklı, şirketten tahsil edemediği alacağı için ortakların kişisel malvarlığına başvurabilir',
        },
        'E',
        'TTK md. 236-237: kollektif şirket ortakları şirket borçlarından SINIRSIZ ve MÜTESELSİLEN sorumludur; ancak sorumluluk TALİ (ikinci derecede) niteliktedir. Alacaklı, şirketten tahsil edemediği takdirde ortakların kişisel malvarlığına başvurabilir; şirket sona ermiş ya da borç ödemeden aciz belgesi alınmışsa doğrudan da gidilebilir.',
    ),
    # düzey 3
    '0006': patch(
        'Bir komandit şirkette (A) ortağı sınırsız sorumlu, (B) ortağı ise yalnızca koyduğu sermaye ile sorumludur. (B) ortağı bir tüzel kişidir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Komandite ortak da tüzel kişi olabilir; sorumluluğun sınırsızlığı tüzel kişiliğe engel değildir',
            'B': 'Komanditer ortak tüzel kişi olabilir',
            'C': 'Komanditer ortağın şirket alacaklılarına karşı sorumluluğu, koyduğu sermaye tutarı ile sınırlıdır',
            'D': 'Komandite ortağın sorumluluğu sınırsızdır',
            'E': 'A komandite, B komanditer ortaktır',
        },
        'A',
        'TTK md. 304: komandit şirkette şirket alacaklılarına karşı ortaklardan bir veya birkaçının sorumluluğu sınırlandırılmamış (KOMANDİTE), diğerlerininki belirli bir sermaye ile sınırlandırılmıştır (KOMANDİTER). md. 305: komandite ortakların GERÇEK KİŞİ olması gerekir; komanditer ortak tüzel kişi de olabilir.',
    ),
    # düzey 2
    '0007': patch(
        'Sermayesi belirli ve paylara bölünmüş, borçlarından yalnızca malvarlığıyla sorumlu bir şirket kurulmuştur. Buna göre anonim şirket bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Anonim şirket bir sermaye şirketidir',
            'B': 'Anonim şirketin sermayesi belirli ve paylara bölünmüştür',
            'C': 'Anonim şirket, ticaret siciline tescil edilmesiyle birlikte tüzel kişilik kazanır',
            'D': 'Anonim şirketin borçlarından pay sahipleri de kişisel malvarlıklarıyla sorumludur',
            'E': 'Anonim şirket borçlarından yalnızca malvarlığıyla sorumludur',
        },
        'D',
        'TTK md. 329: anonim şirket, sermayesi belirli ve paylara bölünmüş olan, borçlarından dolayı YALNIZ MALVARLIĞIYLA sorumlu bulunan şirkettir. Pay sahipleri şirkete karşı yalnızca taahhüt ettikleri sermaye payları ile sorumludur; şirket borçlarından kişisel sorumlulukları yoktur.',
    ),
    # düzey 2
    '0008': patch(
        'Bir anonim şirketin alacaklısı, şirketten tahsil edemediği alacağı için pay sahiplerinin kişisel malvarlığına başvurmak istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Alacaklı önce şirkete, sonuç alamazsa pay sahibine başvurabilir',
            'B': 'Pay sahibi yalnızca taahhüt ettiği sermaye payı kadar ve şirkete karşı sorumludur; alacaklı ona başvuramaz',
            'C': 'Pay sahibi şirket borçlarından sınırsız sorumludur',
            'D': 'Pay sahibi şirket borçlarından payı oranında doğrudan sorumludur',
            'E': 'Pay sahibinin kişisel sorumluluğu yalnızca şirketin ödenmemiş kamu borçları bakımından ve payı oranında doğar',
        },
        'B',
        'TTK md. 329/2: pay sahipleri, sadece taahhüt ettikleri sermaye payları ile ve ŞİRKETE karşı sorumludur. Şirket alacaklıları pay sahiplerinin kişisel malvarlığına başvuramaz; sorumluluk tali ya da oransal da değildir.',
    ),
    # düzey 2
    '0009': patch(
        'Bir girişimci, tek başına anonim şirket kurmak istemekte ancak en az beş kurucu gerektiğini düşünmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tek pay sahipli anonim şirket kurulabilir; ancak bu durumun ticaret siciline tescil ve ilan edilmesi gerekmez',
            'B': 'Anonim şirket en az beş pay sahibiyle kurulabilir',
            'C': 'Anonim şirket en az üç pay sahibiyle kurulabilir',
            'D': 'Anonim şirket en az iki pay sahibiyle kurulabilir',
            'E': 'Anonim şirket tek pay sahibiyle kurulabilir; tek pay sahipliği ticaret siciline tescil ve ilan edilir',
        },
        'E',
        'TTK md. 338: anonim şirket, bir veya daha fazla kurucunun varlığıyla kurulabilir. Pay sahibi sayısı BİRE düşerse ya da şirket tek pay sahibiyle kurulursa bu durum yönetim kurulunca ticaret siciline TESCİL ve İLAN ettirilir.',
    ),
    # düzey 2
    '0010': patch(
        'Bir anonim şirkette esas sözleşme hazırlanırken organların belirlenmesi gündeme gelmiştir. Buna göre anonim şirketin zorunlu organları bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Limited şirketin zorunlu organları genel kurul, yönetim kurulu ve müdürler kuruludur',
            'B': 'Zorunlu organlar genel kurul, yönetim kurulu ve denetçidir',
            'C': 'Zorunlu organlar genel kurul ve yönetim kuruludur; denetçi zorunlu organ değildir',
            'D': 'Zorunlu organ yalnızca genel kuruldur',
            'E': 'Zorunlu organ yalnızca yönetim kuruludur',
        },
        'C',
        'TTK md. 364 vd. ve 407 vd.: anonim şirketin zorunlu organları GENEL KURUL ve YÖNETİM KURULUDUR. 6102 sayılı TTK ile denetçi organ olmaktan çıkarılmış, bağımsız denetim ayrı bir rejime bağlanmıştır. Müdürler kurulu ise limited şirkete özgüdür.',
    ),
    # düzey 3
    '0011': patch(
        'Bir anonim şirketin yönetim kurulu, esas sözleşmeyi değiştirme ve kâr dağıtımına karar verme yetkisinin kendisinde olduğunu ileri sürmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yönetim kurulu üyelerinin seçimi ve azli genel kurula aittir',
            'B': 'Şirketin feshine karar verme genel kurula aittir',
            'C': 'Esas sözleşmenin değiştirilmesi, genel kurulun kanunen devredilemez görev ve yetkilerinden biridir',
            'D': 'Finansal tabloların onaylanması genel kurulun yetkisindedir',
            'E': 'Esas sözleşme değişikliği ve kâr dağıtımı kararı yönetim kurulunun devredilemez yetkilerindendir',
        },
        'E',
        'TTK md. 408: esas sözleşmenin değiştirilmesi, yönetim kurulu üyelerinin seçimi, azli ve ibrası, finansal tabloların onaylanması, kâr payının belirlenmesi, denetçinin seçimi ve şirketin feshi GENEL KURULUN devredilemez görev ve yetkilerindendir. md. 375 ise yönetim kurulunun devredilemez görevlerini ayrı olarak sayar.',
    ),
    # düzey 2
    '0012': patch(
        'Bir ortaklık, ticaret unvanı altında kurulmuş; esas sermayesi belirli olup ortakların sorumluluğu taahhüt ettikleri esas sermaye payları ile sınırlandırılmıştır. Buna göre limited şirket bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Limited şirket bir sermaye şirketidir',
            'B': 'Limited şirket ortakları şirket borçlarından sınırsız ve müteselsilen sorumludur',
            'C': 'Limited şirketin organları genel kurul ve müdürlerdir',
            'D': 'Ortakların sorumluluğu taahhüt ettikleri esas sermaye payları ile sınırlıdır',
            'E': 'Limited şirket ticaret siciline tescille tüzel kişilik kazanır',
        },
        'B',
        'TTK md. 573: limited şirket, bir veya daha çok gerçek ya da tüzel kişi tarafından bir ticaret unvanı altında kurulur; esas sermayesi belirlidir ve ortaklar şirket borçlarından sorumlu OLMAYIP sadece taahhüt ettikleri esas sermaye paylarını ödemekle ve şirket sözleşmesinde öngörülen ek ödeme ve yan edim yükümlülüklerini yerine getirmekle yükümlüdür.',
    ),
    # düzey 2
    '0013': patch(
        'Bir limited şirkete 52 ortak alınmak istenmektedir. Buna göre ortak sayısı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Limited şirkette ortak sayısı elliyi aşamaz; bu nedenle 52 ortakla kurulamaz',
            'B': 'Limited şirkette ortak sayısı bakımından herhangi bir üst sınır öngörülmemiştir',
            'C': 'Limited şirkette ortak sayısı en çok yüzdür',
            'D': 'Üst sınır yalnızca tüzel kişi ortaklar için uygulanır',
            'E': 'Limited şirkette ortak sayısı en çok yirmidir',
        },
        'A',
        'TTK md. 574: limited şirketin ortak sayısı ELLİYİ AŞAMAZ. Alt sınır ise birdir; şirket tek ortakla da kurulabilir. Ortak sayısı bire düşerse durum ticaret siciline tescil ve ilan ettirilir.',
    ),
    # düzey 3
    '0014': patch(
        'Bir limited şirketin ödenmemiş vergi borcu bulunmaktadır. Alacaklı idare, tahsil edemediği bu borç için ortaklara başvurmak istemektedir. Aynı durumda bir anonim şirketin pay sahipleri de gündeme gelmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Anonim şirket pay sahipleri sorumlu; limited ortakları sorumlu değildir',
            'B': 'Hem limited şirket ortakları hem de anonim şirket pay sahipleri, kamu borcundan sermaye payları oranında doğrudan doğruya sorumlu tutulur',
            'C': 'Her iki şirkette de ortakların kamu borcundan sorumluluğu bulunmaz',
            'D': 'Limited şirket ortakları kamu borcundan sermaye payları oranında doğrudan sorumludur; anonim şirket pay sahiplerinin böyle bir sorumluluğu yoktur',
            'E': 'Sorumluluk her iki şirkette de yalnızca kanuni temsilcilere aittir',
        },
        'D',
        '6183 sayılı Kanun md. 35: limited şirket ORTAKLARI, şirketten tahsil edilemeyen amme alacağından SERMAYE HİSSELERİ ORANINDA doğrudan doğruya sorumludur. Anonim şirkette ise pay sahibinin böyle bir sorumluluğu yoktur; sorumluluk mükerrer md. 35 uyarınca KANUNİ TEMSİLCİLERE (yönetim kurulu) aittir.',
    ),
    # düzey 3
    '0015': patch(
        'Bir anonim şirketin yönetim kurulu, şirketin borca batık olduğunu tespit etmiş ancak durumu mahkemeye bildirmemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bildirim yükümlülüğü pay sahiplerine aittir',
            'B': 'Borca batıklık bildirimi genel kurulun görevi olup yönetim kurulunun bu konuda bir yükümlülüğü yoktur',
            'C': 'Borca batıklık durumunun mahkemeye bildirilmesi yönetim kurulunun devredilemez görevlerindendir',
            'D': 'Bildirim yükümlülüğü yalnızca denetçiye aittir',
            'E': 'Borca batıklık hâlinde bildirim yükümlülüğü öngörülmemiştir',
        },
        'C',
        'TTK md. 375/1-f ve md. 376: şirketin borca batık durumda bulunduğu şüphesini uyandıran işaretler varsa yönetim kurulu ara bilanço düzenler; borca batıklık tespit edilirse durumu MAHKEMEYE BİLDİRMEK yönetim kurulunun DEVREDİLEMEZ görevlerindendir.',
    ),
    # düzey 3
    '0016': patch(
        'Bir limited şirket ortağı, esas sermaye payını üçüncü bir kişiye devretmek istemekte; devrin sözlü anlaşmayla geçerli olacağını düşünmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Pay devri için yazılı şekil ve imzaların noterce onaylanması gerekir; ayrıca aksi öngörülmedikçe genel kurul onayı aranır',
            'B': 'Pay devri için yalnızca ticaret siciline tescil yeterlidir',
            'C': 'Pay devri sözlü anlaşmayla geçerli olarak yapılabilir',
            'D': 'Limited şirkette esas sermaye payı devredilemez; ortaklık sıfatı yalnızca şirketin sona ermesiyle ortadan kalkar',
            'E': 'Pay devri yalnızca yazılı şekilde yapılırsa yeterlidir; noter onayı aranmaz',
        },
        'A',
        'TTK md. 595: esas sermaye payının devri ve devir borcunu doğuran işlemler YAZILI şekilde yapılır ve tarafların imzaları NOTERCE ONAYLANIR. Şirket sözleşmesinde aksi öngörülmemişse devir için GENEL KURULUN ONAYI şarttır; devir bu onayla geçerli olur.',
    ),
    # düzey 2
    '0017': patch(
        'Kurucular anonim şirket esas sözleşmesini imzalamış ancak henüz ticaret siciline tescil başvurusu yapmamıştır. Bu aşamada şirket adına bir sözleşme imzalanmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Şirket, esas sözleşmenin imzalanmasıyla tüzel kişilik kazanır',
            'B': 'Tüzel kişilik, sermayenin tamamının ödenmesiyle kazanılır',
            'C': 'Tescilden önce yapılan işlemler kendiliğinden şirketi bağlar',
            'D': 'Ticaret şirketleri ticaret siciline tescille tüzel kişilik kazanır; tescilden önce şirket adına işlem yapanlar kişisel olarak sorumlu olur',
            'E': 'Şirket, kuruluş genel kurulunun toplanıp organlarını seçmesiyle tüzel kişilik kazanır; ticaret siciline tescil yalnızca bildirici etki doğurur',
        },
        'D',
        'TTK md. 355: anonim şirket ticaret siciline TESCİL ile tüzel kişilik kazanır. md. 355/2: tescilden önce şirket adına işlem yapanlar bu işlemlerden ŞAHSEN ve MÜTESELSİLEN sorumludur; işlemin şirketçe üstlenilmesi hâlinde sorumluluk şirkete geçer.',
    ),
    # düzey 2
    '0018': patch(
        'Bir anonim şirketin yönetim kurulu, esas sözleşmedeki işletme konusu dışında kalan bir işlem yapmıştır. Karşı taraf iyiniyetlidir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşlem ancak genel kurul onaylarsa şirketi bağlar',
            'B': 'İşletme konusu dışındaki işlemler de şirketi bağlar; ultra vires ilkesi kaldırılmıştır',
            'C': 'İşlem yok hükmünde olup şirketi bağlamaz; karşı tarafın iyiniyeti sonucu değiştirmez',
            'D': 'İşlem yalnızca yönetim kurulu üyelerini bağlar',
            'E': 'İşlem, ticaret siciline tescil edilirse şirketi bağlar',
        },
        'B',
        'TTK md. 125/2: ticaret şirketleri, TMK md. 48 çerçevesinde bütün haklardan yararlanabilir ve borçları üstlenebilir. 6102 sayılı TTK ile ULTRA VIRES ilkesi kaldırılmıştır; işletme konusu dışındaki işlemler de şirketi bağlar. Yönetim kurulunun iç sorumluluğu ise saklıdır.',
    ),
    # düzey 2
    '0019': patch(
        'Bir anonim şirket kurulurken sermayenin tamamının kuruluşta nakden ödenmesi gerektiği ileri sürülmüştür. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ayni sermaye konulması mümkündür',
            'B': 'Nakden taahhüt edilen payların bir bölümünün tescilden önce ödenmesi aranır',
            'C': 'Hizmet edimi ve kişisel emek sermaye olarak konulamaz',
            'D': 'Anonim şirketin sermayesi kanunda öngörülen asgari tutardan az olamaz',
            'E': 'Nakden taahhüt edilen payların tamamının kuruluşta ödenmesi zorunludur',
        },
        'E',
        'TTK md. 332, 344 ve 342: anonim şirket sermayesi kanunda öngörülen asgari tutardan az olamaz; nakden taahhüt edilen payların itibarî değerinin kanunda belirtilen oranı tescilden ÖNCE, kalanı ise öngörülen sürede ödenir. Tamamının kuruluşta ödenmesi zorunlu DEĞİLDİR. Hizmet edimi, kişisel emek ve vadesi gelmemiş alacaklar sermaye olarak konulamaz.',
    ),
    # düzey 2
    '0020': patch(
        'Bir ticaret şirketi tür değiştirerek limited şirketten anonim şirkete dönüşmek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tür değiştirme için tüm alacaklıların yazılı onayı gerekir',
            'B': 'Tür değiştirme mümkün değildir; şirketin tasfiye edilip yeniden kurulması gerekir',
            'C': 'Tür değiştirmede şirket tüzel kişiliği sona erer ve yenisi doğar',
            'D': 'Tür değiştirme mümkündür; yeni türe dönüşen şirket eskisinin devamıdır',
            'E': 'Tür değiştirme yalnızca anonimden limitede mümkündür',
        },
        'D',
        'TTK md. 180 vd.: bir şirket hukuki şeklini değiştirebilir; yeni türe dönüştürülen şirket eskisinin DEVAMIDIR. Tüzel kişilik sona ermez, tasfiye gerekmez ve dönüşüm iki yönlü mümkündür. Alacaklıların korunması ayrı hükümlerle sağlanır.',
    ),
    # düzey 2
    '0021': patch(
        'İki anonim şirket birleşmek istemektedir. Buna göre birleşme bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Birleşme kararı genel kurulca alınır',
            'B': 'Devrolunan şirketin ortakları, devralan şirkette kendiliğinden ortaklık hakkı kazanır',
            'C': 'Devrolunan şirketin malvarlığı külli halefiyetle devralana geçer',
            'D': 'Birleşme, devralma veya yeni kuruluş şeklinde olabilir',
            'E': 'Birleşmede devrolunan şirketin tasfiye edilmesi zorunludur',
        },
        'E',
        'TTK md. 136 vd.: birleşme, bir şirketin diğerini DEVRALMASI ya da yeni bir şirket içinde bir araya gelmeleri şeklinde olur. Devrolunan şirket TASFİYESİZ sona erer; malvarlığı külli halefiyetle devralana geçer ve ortaklar devralan şirkette ortaklık hakkı kazanır.',
    ),
    # düzey 3
    '0022': patch(
        'Bir anonim şirketin genel kurulu, yönetim kurulu üyelerini seçme yetkisini yönetim kuruluna devretmek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yönetim kurulu üyeleri zaten yönetim kurulunca seçilir',
            'B': 'Devir, esas sözleşmede öngörülmüşse mümkündür',
            'C': 'Yönetim kurulu üyelerinin seçimi genel kurulun devredilemez yetkisi olduğundan bu devir yapılamaz',
            'D': 'Genel kurul, kanunen devredilemez sayılanlar dâhil bütün yetkilerini yönetim kuruluna devredebilir',
            'E': 'Devir, ticaret siciline tescil edilirse geçerli olur',
        },
        'C',
        'TTK md. 408: yönetim kurulu üyelerinin SEÇİMİ, AZLİ ve İBRASI genel kurulun DEVREDİLEMEZ görev ve yetkilerindendir. Devredilemez yetkiler esas sözleşmeyle ya da tescil ile devredilebilir hâle getirilemez.',
    ),
    # düzey 2
    '0023': patch(
        'Bir limited şirkette yönetim ve temsil yetkisinin hangi organda olduğu tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Limited şirket müdür veya müdürler tarafından yönetilir ve temsil edilir; en az bir ortağın yönetim hakkı bulunmalıdır',
            'B': 'Limited şirkette yönetim yetkisi doğrudan genel kuruldadır',
            'C': 'Limited şirkette müdür yalnızca ortak olmayan üçüncü kişilerden seçilebilir; şirket ortakları müdür olarak atanamaz',
            'D': 'Limited şirket yönetim kurulu tarafından yönetilir',
            'E': 'Limited şirkette temsil yetkisi ticaret siciline tescil edilmez',
        },
        'A',
        'TTK md. 623: limited şirketin yönetimi ve temsili şirket sözleşmesiyle düzenlenir; şirketin müdürlerinden en az birinin şirket ORTAĞI olması ve yönetim hakkına sahip bulunması gerekir. Müdürler ortak olmayan kişilerden de seçilebilir; temsil yetkisi tescil ve ilan edilir.',
    ),
    # düzey 3
    '0024': patch(
        'Bir kollektif şirket ortağı, şirketin faaliyet konusuna giren bir işi kendi hesabına yapmaya başlamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Rekabet yasağı yalnızca şirket sözleşmesinde yazılıysa uygulanır',
            'B': 'Ortaklar, diğer ortakların izni olmadan şirketin işletme konusuna giren ticari işleri kendi veya başkası hesabına yapamaz',
            'C': 'Ortak, şirket dışındaki faaliyetlerinde tümüyle serbesttir',
            'D': 'Rekabet yasağı yalnızca anonim şirket yöneticileri bakımından öngörülmüş olup kollektif şirket ortaklarını hiç bağlamaz',
            'E': 'Ortak, faaliyeti ticaret siciline tescil ettirirse yasak uygulanmaz',
        },
        'B',
        'TTK md. 230: kollektif şirket ortakları, diğer ortakların izni olmaksızın şirketin işletme konusuna giren bir ticari işi kendi veya başkası hesabına yapamaz ve aynı tür işle uğraşan bir şirkete sorumluluğu sınırlandırılmamış ortak olarak giremez. Yasak kanundan doğar; sözleşmeye yazılması ya da tescil koşuluna bağlı değildir.',
    ),
    # düzey 2
    '0025': patch(
        'Bir anonim şirkette yönetim kurulu üyesi olabilmek için pay sahibi olma koşulunun aranıp aranmadığı tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yönetim kuruluna yalnızca gerçek kişiler seçilebilir',
            'B': 'Yönetim kurulu üyeliği yalnızca kurucu pay sahiplerine açıktır',
            'C': 'Yönetim kurulu üyesinin pay sahibi olması ve ayrıca şirkete teminat göstermesi gerekir',
            'D': 'Yönetim kurulu üyesinin pay sahibi olması gerekmez; tüzel kişiler de üye seçilebilir',
            'E': 'Yönetim kurulu üyesi mutlaka pay sahibi olmalıdır',
        },
        'D',
        'TTK md. 359: anonim şirketin yönetim kurulu bir veya daha fazla kişiden oluşur ve üyelerin PAY SAHİBİ OLMASI ŞART DEĞİLDİR. Tüzel kişiler de yönetim kuruluna üye seçilebilir; bu hâlde tüzel kişi adına yalnızca bir gerçek kişi tescil ve ilan edilir.',
    ),
    # düzey 2
    '0026': patch(
        'Bir anonim şirketin sona ermesi ve tasfiyesi gündeme gelmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sona erme kararıyla şirketin tüzel kişiliği derhâl ortadan kalkar',
            'B': 'Tasfiyenin tamamlanmasıyla ticaret sicilinden terkin edilir',
            'C': 'Tasfiye memurları şirketi temsil eder',
            'D': 'Sona eren şirket tasfiye hâline girer',
            'E': 'Tasfiye hâlindeki şirket tüzel kişiliğini tasfiye sonuna kadar korur',
        },
        'A',
        "TTK md. 529 vd.: sona eren anonim şirket TASFİYE hâline girer ve tüzel kişiliğini tasfiye sonuna kadar KORUR; ticaret unvanına 'tasfiye hâlinde' ibaresi eklenir. Tüzel kişilik ancak tasfiyenin tamamlanıp sicilden terkinle sona erer.",
    ),
    # düzey 2
    '0027': patch(
        'Bir limited şirkette ortak sayısı bire düşmüştür. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Şirketin altı ay içinde yeni ortak alması gerekir; aksi hâlde mahkemece feshine karar verilir',
            'B': 'Şirket adi şirkete dönüşür',
            'C': 'Durum sicile bildirilmez; ortak sayısı şirketin iç işidir',
            'D': 'Şirket kendiliğinden sona erer ve tasfiyeye girer',
            'E': 'Şirket tek ortakla varlığını sürdürebilir; durum ticaret siciline tescil ve ilan ettirilir',
        },
        'E',
        'TTK md. 574 ve 584: limited şirket tek ortakla kurulabilir ve varlığını sürdürebilir. Ortak sayısı bire düşerse bu durum, sonucu doğuran işlem tarihinden itibaren müdürlere yazıyla bildirilir ve müdürler tarafından ticaret siciline TESCİL ve İLAN ettirilir.',
    ),
    # düzey 2
    '0028': patch(
        'Bir hukuk öğrencisi ticaret şirketlerinin türlerini ve niteliklerini karşılaştırmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Kooperatifler de TTK'da ticaret şirketleri arasında sayılmıştır",
            'B': 'Sermayesi paylara bölünmüş komandit şirket bir şahıs şirketidir',
            'C': 'Limited şirket bir sermaye şirketidir',
            'D': 'Kollektif şirket bir şahıs şirketidir',
            'E': 'Anonim şirket bir sermaye şirketidir',
        },
        'B',
        'TTK md. 124/2: kollektif ile komandit şirket ŞAHIS; anonim, limited ve SERMAYESİ PAYLARA BÖLÜNMÜŞ KOMANDİT şirket SERMAYE şirketi sayılır. Sıradan komandit şahıs şirketiyken, sermayesi paylara bölünmüş komandit sermaye şirketidir.',
    ),
    # düzey 2
    '0029': patch(
        'Bir yatırımcı, ortak olacağı şirket türüne göre üstleneceği riski değerlendirmektedir. Buna göre ortakların sorumluluğu bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Komanditer ortağın şirket alacaklılarına karşı sorumluluğu, koyduğu sermaye tutarı ile sınırlıdır',
            'B': 'Limited şirkette ortak, yalnızca taahhüt ettiği esas sermaye payını ödemekle yükümlüdür',
            'C': 'Anonim şirkette pay sahibi, şirket borçlarından payı oranında alacaklılara karşı sorumludur',
            'D': 'Kollektif şirkette ortaklar sınırsız ve müteselsilen sorumludur',
            'E': 'Adi şirkette ortaklar, şirket borçlarından kişisel malvarlıklarıyla müteselsilen sorumludur',
        },
        'C',
        'TTK md. 329/2: anonim şirkette pay sahibi yalnızca taahhüt ettiği sermaye payı ile ve ŞİRKETE karşı sorumludur; alacaklılara karşı kişisel ya da oransal bir sorumluluğu yoktur.',
    ),
    # düzey 2
    '0030': patch(
        'Bir girişimci, kuracağı şirketin organ yapısını planlamaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Anonim şirketin zorunlu organları genel kurul ve yönetim kuruludur',
            'B': 'Limited şirketin zorunlu organları genel kurul ve yönetim kuruludur',
            'C': 'Limited şirkette genel kurul bir organdır',
            'D': 'Limited şirket müdür veya müdürler tarafından yönetilir',
            'E': 'Anonim şirkette denetçi zorunlu organ değildir',
        },
        'B',
        'TTK md. 616 vd.: limited şirketin organları GENEL KURUL ve MÜDÜR(LER)dir; yönetim kurulu anonim şirkete özgüdür. Anonim şirkette zorunlu organlar genel kurul ve yönetim kuruludur; denetçi 6102 sayılı TTK ile organ olmaktan çıkarılmıştır.',
    ),
    # düzey 2
    '0031': patch(
        'Bir şirketin kuruluş ve tüzel kişilik kazanma süreci incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ticaret şirketleri, ticaret siciline tescil edilmekle tüzel kişilik kazanır',
            'B': 'Adi şirketin tüzel kişiliği bulunmaz',
            'C': 'Tüzel kişilik, tasfiyenin tamamlanıp terkinle sona erer',
            'D': 'Ticaret şirketleri, kurucuların sözleşmeyi imzalamasıyla tüzel kişilik kazanır',
            'E': 'Tescilden önce şirket adına işlem yapanlar şahsen sorumlu olur',
        },
        'D',
        'TTK md. 355 ve genel hükümler: ticaret şirketleri ticaret siciline TESCİL ile tüzel kişilik kazanır; sözleşmenin imzalanması tek başına yeterli değildir. Tescilden önce şirket adına işlem yapanlar şahsen ve müteselsilen sorumludur.',
    ),
    # düzey 3
    '0032': patch(
        'Bir anonim şirketin genel kurul ve yönetim kurulu yetkileri karşılaştırılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Şirketin üst düzey yönetimi ve teşkilat yapısının belirlenmesi yönetim kurulunun devredilemez görevidir',
            'B': 'Şirketin üst düzey yönetimi ve muhasebe düzeninin kurulması genel kurulun devredilemez yetkisidir',
            'C': 'Esas sözleşme değişikliği genel kurulun devredilemez yetkisidir',
            'D': 'Borca batıklık bildirimi yönetim kurulunun devredilemez görevidir',
            'E': 'Finansal tabloların onaylanması genel kurula aittir',
        },
        'B',
        'TTK md. 375: şirketin üst düzey yönetimi, muhasebe ve finansal denetim düzeninin kurulması, müdürlerin atanması ve borca batıklık bildirimi YÖNETİM KURULUNUN devredilemez görevlerindendir. md. 408 ise genel kurulun devredilemez yetkilerini ayrıca sayar; ikisi karıştırılmamalıdır.',
    ),
    # düzey 2
    '0033': patch(
        'Limited şirkette esas sermaye payının devri incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Devir için yazılı şekil gerekir',
            'B': 'Tarafların imzalarının noterce onaylanması gerekir',
            'C': 'Şirket sözleşmesinde aksi öngörülmemişse pay devri için genel kurulun onayı aranır',
            'D': 'Devir pay defterine kaydedilir',
            'E': 'Esas sermaye payının devri için yazılı şekil yeterli olup noter onayı aranmaz',
        },
        'E',
        'TTK md. 595: esas sermaye payının devri ve devir borcunu doğuran işlemler YAZILI şekilde yapılır ve tarafların imzaları NOTERCE ONAYLANIR. Şirket sözleşmesinde aksi öngörülmemişse devir için genel kurulun onayı şarttır.',
    ),
    # düzey 2
    '0034': patch(
        'Ticaret şirketleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Kollektif ve komandit şirketler şahıs şirketidir. II. Anonim ve limited şirketler sermaye şirketidir. III. Adi şirket bir ticaret şirketidir.',
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'II ve III',
        },
        'A',
        "I ve II doğrudur (TTK md. 124/2). III YANLIŞTIR: adi şirket TBK md. 620 vd.'da düzenlenmiştir, ticaret şirketi değildir ve tüzel kişiliği yoktur.",
    ),
    # düzey 3
    '0035': patch(
        'Ortakların sorumluluğu ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Kollektif şirkette ortakların sorumluluğu sınırsız ve müteselsildir. II. Anonim şirkette pay sahibi şirket borçlarından kişisel olarak sorumludur. III. Komanditer ortağın sorumluluğu koyduğu sermaye ile sınırlıdır. IV. Limited şirket ortakları kamu borcundan sermaye payları oranında sorumludur.',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'Yalnız II',
            'D': 'II ve IV',
            'E': 'I, II ve IV',
        },
        'C',
        'II YANLIŞ: TTK md. 329/2 uyarınca pay sahibi yalnızca taahhüt ettiği sermaye payı ile ve şirkete karşı sorumludur. I (md. 236-237), III (md. 304) ve IV (6183 md. 35) doğrudur.',
    ),
    # düzey 2
    '0036': patch(
        'Anonim şirket organları ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Zorunlu organlar genel kurul ve yönetim kuruludur. II. Esas sözleşme değişikliği genel kurulun devredilemez yetkisidir. III. Yönetim kurulu üyesinin pay sahibi olması şarttır.',
        {
            'A': 'I ve III',
            'B': 'II ve III',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'D',
        'I doğrudur (TTK md. 364, 407 vd.). II doğrudur (md. 408). III YANLIŞTIR: md. 359 uyarınca yönetim kurulu üyesinin pay sahibi olması ŞART DEĞİLDİR; tüzel kişiler de üye seçilebilir.',
    ),
    # düzey 3
    '0037': patch(
        'Limited şirket ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Ortak sayısı elliyi aşamaz. II. Şirket tek ortakla kurulabilir. III. Şirket yönetim kurulu tarafından yönetilir. IV. Esas sermaye payının devrinde noter onayı aranmaz.',
        {
            'A': 'III ve IV',
            'B': 'II ve III',
            'C': 'Yalnız III',
            'D': 'I, III ve IV',
            'E': 'I ve II',
        },
        'A',
        'III YANLIŞ: TTK md. 623 uyarınca limited şirket MÜDÜR veya müdürlerce yönetilir; yönetim kurulu anonim şirkete özgüdür. IV YANLIŞ: md. 595 pay devrinde yazılı şekil ve NOTER ONAYI arar. I (md. 574) ve II (md. 573) doğrudur.',
    ),
    # düzey 2
    '0038': patch(
        'Ticaret şirketlerinde yapısal değişiklikler ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Birleşme devralma veya yeni kuruluş şeklinde olabilir. II. Tür değiştiren şirket eskisinin devamıdır. III. Birleşmede devrolunan şirket tasfiye edilir.',
        {
            'A': 'Yalnız I',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'I ve III',
            'E': 'I, II ve III',
        },
        'C',
        'I doğrudur (TTK md. 136). II doğrudur (md. 180). III YANLIŞTIR: birleşmede devrolunan şirket TASFİYESİZ sona erer; malvarlığı külli halefiyetle devralana geçer.',
    ),
    # düzey 0
    '0039': patch(
        "Bir girişimci, kuracağı ortaklığın Türk Ticaret Kanunu'nda sayılan ticaret şirketlerinden biri olmasını istemektedir. Buna göre aşağıdakilerden hangisi TTK'da düzenlenen ticaret şirketlerinden biri değildir?",
        {
            'A': 'Kollektif şirket',
            'B': 'Adi şirket',
            'C': 'Komandit şirket',
            'D': 'Anonim şirket',
            'E': 'Limited şirket',
        },
        'B',
        "TTK md. 124: ticaret şirketleri kollektif, komandit, anonim, limited ve kooperatif şirketlerdir. ADİ ŞİRKET TBK md. 620 vd.'da düzenlenmiştir; ticaret şirketi değildir.",
    ),
    # düzey 0
    '0040': patch(
        'Bir yatırımcı, sorumluluğu koyduğu sermaye ile sınırlı olacak biçimde komandit şirkete girmek istemektedir. Buna göre bu ortağın sıfatı aşağıdakilerden hangisidir?',
        {
            'A': 'Kurucu ortak',
            'B': 'Kollektif ortak',
            'C': 'İmtiyazlı ortak',
            'D': 'Komandite ortak',
            'E': 'Komanditer ortak',
        },
        'E',
        "TTK md. 304: komandit şirkette sorumluluğu belirli bir sermaye ile sınırlandırılmış ortak KOMANDİTER, sorumluluğu sınırlandırılmamış ortak ise KOMANDİTE'dir.",
    ),
    # düzey 0
    '0041': patch(
        'Bir anonim şirkette pay sahiplerinin oluşturduğu ve şirketin en yetkili karar organı olan yapı aşağıdakilerden hangisidir?',
        {
            'A': 'Müdürler kurulu',
            'B': 'Genel kurul',
            'C': 'Yönetim kurulu',
            'D': 'Denetim komitesi',
            'E': 'Tasfiye kurulu',
        },
        'B',
        'TTK md. 407 vd.: pay sahipleri anonim şirkete ilişkin haklarını GENEL KURULDA kullanır; genel kurul şirketin en yetkili karar organıdır. Yönetim kurulu icra organı, müdürler kurulu ise limited şirkete özgüdür.',
    ),
    # düzey 0
    '0042': patch(
        'Bir limited şirketin yönetimini ve temsilini üstlenen organ aşağıdakilerden hangisidir?',
        {
            'A': 'Müdür veya müdürler',
            'B': 'Tasfiye memurları',
            'C': 'Genel kurul başkanlığı',
            'D': 'Denetim kurulu',
            'E': 'Yönetim kurulu',
        },
        'A',
        'TTK md. 623: limited şirketin yönetimi ve temsili müdür veya müdürlere aittir; müdürlerden en az birinin şirket ortağı olması ve yönetim hakkına sahip bulunması gerekir.',
    ),
    # düzey 0
    '0043': patch(
        'Ticaret şirketlerinin tüzel kişilik kazandığı an aşağıdakilerden hangisidir?',
        {
            'A': 'Vergi dairesine kayıt yaptırıldığı an',
            'B': 'Sermayenin tamamının ödendiği an',
            'C': 'İlk genel kurulun toplandığı an',
            'D': 'Şirket sözleşmesinin imzalandığı an',
            'E': 'Ticaret siciline tescil edildikleri an',
        },
        'E',
        'Ticaret şirketleri ticaret siciline TESCİL ile tüzel kişilik kazanır (TTK md. 355 ve ilgili hükümler). Sözleşmenin imzalanması, sermayenin ödenmesi ya da vergi kaydı tek başına tüzel kişilik doğurmaz.',
    ),
    # düzey 1
    '0044': patch(
        'Bir kollektif şirkette ortak olacak kişilerin niteliği tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kollektif şirkette ortak sayısı en az beş olmalıdır',
            'B': 'Kollektif şirkete yalnızca tüzel kişiler ortak olabilir',
            'C': 'Kollektif şirket yalnızca gerçek kişiler arasında kurulabilir',
            'D': 'Kollektif şirkete gerçek ve tüzel kişiler birlikte ortak olabilir',
            'E': 'Kollektif şirkete yalnızca tacir sıfatı taşıyanlar ortak olabilir',
        },
        'C',
        'TTK md. 211: kollektif şirket, ticari bir işletmeyi bir ticaret unvanı altında işletmek amacıyla GERÇEK KİŞİLER arasında kurulur. Tüzel kişiler kollektif şirkete ortak olamaz.',
    ),
    # düzey 1
    '0045': patch(
        'Bir anonim şirkette pay sahibinin şirkete karşı temel yükümlülüğü aşağıdakilerden hangisidir?',
        {
            'A': 'Şirket borçlarını kişisel malvarlığıyla karşılamak',
            'B': 'Şirket yönetiminde bizzat görev almak',
            'C': 'Şirkete ek teminat göstermek',
            'D': 'Taahhüt ettiği sermaye payını ödemek',
            'E': 'Şirketin kamu borçlarından payı oranında sorumlu olmak',
        },
        'D',
        'TTK md. 329/2: pay sahipleri yalnızca taahhüt ettikleri SERMAYE PAYLARI ile ve şirkete karşı sorumludur. Şirket borçlarından kişisel sorumlulukları yoktur; yönetimde görev alma yükümlülüğü de bulunmaz.',
    ),
    # düzey 1
    '0046': patch(
        'Bir limited şirket ortağı, şirketin ödenmemiş kamu borcu nedeniyle kendisine başvurulmasını beklememektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ortak, kamu borcunun tamamından müteselsilen sorumludur',
            'B': 'Ortak, şirketten tahsil edilemeyen kamu alacağından sermaye payı oranında doğrudan sorumludur',
            'C': 'Sorumluluk yalnızca şirket müdürlerine aittir',
            'D': 'Ortağın kamu borcundan hiçbir sorumluluğu bulunmaz',
            'E': 'Kamu borcundan doğrudan sorumluluk yalnızca anonim şirket pay sahipleri için öngörülmüş olup limited ortaklarını kapsamaz',
        },
        'B',
        '6183 sayılı Kanun md. 35: limited şirket ortakları, şirketten tamamen veya kısmen tahsil edilemeyen amme alacağından SERMAYE HİSSELERİ ORANINDA doğrudan doğruya sorumludur. Sorumluluk oransaldır; müteselsil değildir.',
    ),
    # düzey 1
    '0047': patch(
        'Bir anonim şirketin ticaret siciline tescilinden önce şirket adına yapılan bir işlemin sonucu bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşlem kendiliğinden şirketi bağlar',
            'B': 'Tescilden önce şirket adına yapılan işlemden yalnızca kurucu ortaklar payları oranında sorumlu olur',
            'C': 'İşlem yok hükmündedir ve hiçbir sonuç doğurmaz',
            'D': 'İşlem yalnızca genel kurul onayıyla geçerli olur',
            'E': 'İşlemi yapanlar şahsen ve müteselsilen sorumlu olur; şirket üstlenirse sorumluluk şirkete geçer',
        },
        'E',
        'TTK md. 355/2: şirket adına tescilden önce işlem yapanlar bu işlemlerden ŞAHSEN ve MÜTESELSİLEN sorumludur. İşlemin açıkça şirket adına yapıldığı ve şirketin tescilden sonraki belirli süre içinde bu işlemleri kabul ettiği hâllerde sorumluluk şirkete geçer.',
    ),
    # düzey 1
    '0048': patch(
        'Bir anonim şirketin yönetim kurulu üyeliğine bir tüzel kişinin seçilmesi planlanmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tüzel kişi üyelik yalnızca kamu iştiraklerinde mümkündür',
            'B': 'Tüzel kişi üye seçilebilir ancak temsilcisinin tescili gerekmez',
            'C': 'Tüzel kişiler yönetim kuruluna üye seçilebilir; tüzel kişi adına bir gerçek kişi tescil ve ilan edilir',
            'D': 'Yönetim kuruluna yalnızca gerçek kişiler seçilebilir',
            'E': 'Tüzel kişinin yönetim kuruluna seçilmesi için esas sözleşmede açık hüküm bulunması dahi yeterli değildir',
        },
        'C',
        'TTK md. 359/2: bir tüzel kişi yönetim kuruluna üye seçildiğinde, tüzel kişiyle birlikte tüzel kişi adına, tüzel kişi tarafından belirlenen ve tescil ve ilan edilen bir GERÇEK KİŞİ de toplantılara katılır ve oy verir.',
    ),
    # düzey 1
    '0049': patch(
        'Bir ticaret şirketi tür değiştirdiğinde şirketin hukuki durumu bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tür değiştirmede malvarlığı tek tek devredilir',
            'B': 'Tür değiştirme yalnızca sermaye şirketleri arasında mümkün olup şahıs şirketlerini kapsamaz',
            'C': 'Tür değiştirme için mahkeme kararı gerekir',
            'D': 'Yeni türe dönüştürülen şirket eskisinin devamıdır; tüzel kişilik sona ermez',
            'E': 'Eski şirket tasfiye edilir ve yeni bir tüzel kişilik doğar',
        },
        'D',
        'TTK md. 180: bir şirket hukuki şeklini değiştirebilir ve yeni türe dönüştürülen şirket ESKİSİNİN DEVAMIDIR. Tasfiye gerekmez, tüzel kişilik sürer ve malvarlığı bir bütün olarak korunur.',
    ),
    # düzey 1
    '0050': patch(
        'Bir anonim şirketin sona ermesinden sonra tüzel kişiliğinin durumu bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Şirket tasfiyesiz olarak sicilden terkin edilir',
            'B': 'Tasfiye hâlinde ticaret unvanı değiştirilemez',
            'C': 'Şirket tasfiye hâline girer ve tüzel kişiliğini tasfiye sonuna kadar korur',
            'D': 'Tasfiye hâlinde şirketi genel kurul temsil eder',
            'E': 'Şirketin tüzel kişiliği, sona erme kararının alınmasıyla birlikte derhâl ortadan kalkar',
        },
        'C',
        "TTK md. 533 vd.: sona eren anonim şirket tasfiye hâline girer, tüzel kişiliğini TASFİYE SONUNA KADAR korur ve unvanına 'tasfiye hâlinde' ibaresi eklenir. Tasfiye hâlindeki şirketi TASFİYE MEMURLARI temsil eder.",
    ),
    # düzey 1
    '0051': patch(
        'Bir limited şirkette ortak sayısının üst sınırı aşıldığında ne olacağı sorulmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Üst sınır yalnızca tüzel kişi ortaklar için uygulanır',
            'B': 'Ortak sayısı yüze kadar çıkabilir',
            'C': 'Limited şirkette ortak sayısı elliyi aşamaz; bu sınırı aşan bir kuruluş yapılamaz',
            'D': 'Ortak sayısında bir üst sınır bulunmaz',
            'E': 'Ortak sayısı üst sınırı aşarsa şirket kendiliğinden anonim şirkete dönüşmüş sayılır',
        },
        'C',
        'TTK md. 574: limited şirketin ortak sayısı ELLİYİ AŞAMAZ. Sınırın aşılması hâlinde şirket kendiliğinden başka bir türe dönüşmez; kanuna uygunluk sağlanmalıdır.',
    ),
    # düzey 2
    '0052': patch(
        'Bir kollektif şirket ortağı, diğer ortakların izni olmadan şirketin işletme konusuna giren bir işi kendi hesabına yapmıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ortaklar diğer ortakların izni olmadan şirketin işletme konusuna giren işleri yapamaz',
            'B': 'Yasak kanundan doğar',
            'C': 'Yasak, aynı tür işle uğraşan bir şirkete sınırsız sorumlu ortak olmayı da kapsar',
            'D': 'Yasağın ihlali şirkete tazminat ve diğer talep hakları doğurabilir',
            'E': 'Rekabet yasağı yalnızca şirket sözleşmesinde açıkça kararlaştırılmışsa uygulanır',
        },
        'E',
        'TTK md. 230: kollektif şirket ortakları, diğer ortakların izni olmaksızın şirketin işletme konusuna giren bir ticari işi kendi veya başkası hesabına yapamaz ve aynı tür işle uğraşan bir şirkete sorumluluğu sınırlandırılmamış ortak olarak giremez. Yasak KANUNDAN doğar; sözleşme koşuluna bağlı değildir.',
    ),
    # düzey 2
    '0053': patch(
        'Bir anonim şirkette esas sözleşme, genel kurulun devredilemez yetkilerinden birini yönetim kuruluna bırakmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Devredilemez yetkiler esas sözleşmeyle dahi devredilemez; bu hüküm geçersizdir',
            'B': 'Hüküm, genel kurulun oybirliğiyle onayı hâlinde geçerli olur',
            'C': 'Hüküm, ticaret siciline tescil edilirse geçerli olur',
            'D': 'Devredilemez yetkiler yalnızca kanunda sayılanlarla sınırlı değildir',
            'E': 'Esas sözleşme hükmü geçerlidir; taraflar yetki dağılımını serbestçe düzenleyebilir',
        },
        'A',
        'TTK md. 408: genel kurulun devredilemez görev ve yetkileri kanunla belirlenmiştir ve esas sözleşmeyle başka bir organa BIRAKILAMAZ. Aksi yöndeki esas sözleşme hükümleri geçersizdir; tescil ya da oybirliği bu sonucu değiştirmez.',
    ),
    # düzey 2
    '0054': patch(
        'Bir şirketin işletme konusu dışında kalan bir işlem yaptığı ileri sürülmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ticaret şirketleri kanunda öngörülen istisnalar dışında bütün haklardan yararlanabilir',
            'B': 'İşletme konusu dışındaki işlemler yok hükmünde olup şirketi bağlamaz',
            'C': 'Ultra vires ilkesi 6102 sayılı TTK ile kaldırılmıştır',
            'D': 'İşletme konusu dışındaki işlemler de şirketi bağlar',
            'E': 'Yönetim kurulunun iç sorumluluğu saklıdır',
        },
        'B',
        'TTK md. 125/2: ticaret şirketleri TMK md. 48 çerçevesinde bütün haklardan yararlanabilir ve borçları üstlenebilir. 6102 sayılı TTK ile ULTRA VIRES kaldırıldığından işletme konusu dışındaki işlemler de şirketi BAĞLAR; yöneticinin şirkete karşı sorumluluğu ayrıdır.',
    ),
    # düzey 2
    '0055': patch(
        'Bir anonim şirkette sermaye olarak neyin konulabileceği tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Vadesi gelmemiş alacaklar sermaye olarak konulamaz',
            'B': 'Üzerinde sınırlı ayni hak bulunmayan taşınmazlar ayni sermaye olarak konulabilir',
            'C': 'Fikri mülkiyet hakları ayni sermaye olarak konulabilir',
            'D': 'Ortağın kişisel emeği ve hizmet edimi sermaye olarak konulabilir',
            'E': 'Nakit sermaye konulabilir',
        },
        'D',
        'TTK md. 342: paradan başka, ekonomik değeri olan ve devrolunabilen malvarlığı unsurları ayni sermaye olarak konulabilir. Ancak HİZMET EDİMLERİ, KİŞİSEL EMEK, ticari itibar ve vadesi gelmemiş alacaklar sermaye olamaz.',
    ),
    # düzey 2
    '0056': patch(
        'Bir anonim şirketin birleşme yoluyla başka bir şirketi devraldığı durumda aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Malvarlığı külli halefiyetle devralan şirkete geçer',
            'B': 'Devrolunan şirket önce tasfiye edilir, ardından malvarlığı devralana geçer',
            'C': 'Devrolunan şirket tasfiyesiz sona erer',
            'D': 'Devrolunan şirketin ortakları, devralan şirkette kendiliğinden ortaklık hakkı kazanır',
            'E': 'Birleşme kararı genel kurullarca alınır',
        },
        'B',
        'TTK md. 136: birleşmede devrolunan şirket TASFİYESİZ sona erer; malvarlığı bir bütün olarak (külli halefiyet) devralana geçer ve ortaklar devralan şirkette ortaklık hakkı kazanır.',
    ),
    # düzey 3
    '0057': patch(
        'Ticaret şirketleri ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Ticaret şirketleri ticaret siciline tescille tüzel kişilik kazanır. II. Ultra vires ilkesi 6102 sayılı TTK ile kaldırılmıştır. III. Adi şirket tüzel kişiliğe sahiptir. IV. Kollektif şirkete tüzel kişiler de ortak olabilir.',
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'I, III ve IV',
            'D': 'Yalnız III',
            'E': 'III ve IV',
        },
        'E',
        'III YANLIŞ: adi şirketin tüzel kişiliği yoktur (TBK md. 620 vd.). IV YANLIŞ: TTK md. 211 uyarınca kollektif şirket yalnızca GERÇEK KİŞİLER arasında kurulur. I ve II doğrudur.',
    ),
    # düzey 3
    '0058': patch(
        'Anonim ve limited şirketlerin karşılaştırılması ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Her ikisi de sermaye şirketidir. II. Limited şirkette ortak sayısı elliyi aşamaz; anonim şirkette üst sınır yoktur. III. Limited şirket ortakları kamu borcundan payları oranında sorumludur.',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'II ve III',
            'D': 'I ve III',
            'E': 'I ve II',
        },
        'A',
        'Üç ifade de doğrudur. TTK md. 124/2 her iki şirketi de sermaye şirketi sayar; md. 574 limited için elli ortak üst sınırı getirir (anonimde üst sınır yoktur); 6183 md. 35 limited ortaklarının kamu borcundan sermaye payları oranında sorumluluğunu düzenler.',
    ),
    # düzey 2
    '0059': patch(
        'Ticaret şirketlerinin türleri bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Komandit şirket bir ticaret şirketidir',
            'B': 'Limited şirket bir ticaret şirketidir',
            'C': "Kooperatifler TTK'da ticaret şirketleri arasında sayılmamıştır",
            'D': "Kollektif şirket, TTK'da sayılan ticaret şirketlerinden biridir",
            'E': 'Anonim şirket bir ticaret şirketidir',
        },
        'C',
        'TTK md. 124: ticaret şirketleri kollektif, komandit, anonim, limited ve KOOPERATİF şirketlerdir. Kooperatifler de ticaret şirketleri arasında sayılmıştır.',
    ),
    # düzey 3
    '0060': patch(
        'Ticaret şirketlerinde organlar ve sorumluluk ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Anonim şirkette denetçi zorunlu bir organdır. II. Limited şirket müdür veya müdürlerce yönetilir. III. Anonim şirkette pay sahibi şirket borçlarından kişisel olarak sorumludur. IV. Genel kurulun devredilemez yetkileri esas sözleşmeyle devredilemez.',
        {
            'A': 'III ve IV',
            'B': 'I, II ve III',
            'C': 'II ve IV',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'E',
        'I YANLIŞ: 6102 sayılı TTK ile denetçi organ olmaktan çıkarılmıştır; zorunlu organlar genel kurul ve yönetim kuruludur. III YANLIŞ: md. 329/2 uyarınca pay sahibi yalnızca taahhüt ettiği sermaye payı ile ve şirkete karşı sorumludur. II (md. 623) ve IV (md. 408) doğrudur.',
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
    print(f"1 paket / {len(PATCHES)} soru (Ticaret Sirketleri yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
