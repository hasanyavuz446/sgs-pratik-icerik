#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kambiyo Senetleri — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Agustos yapisal kalibrasyonundaki olay tabanli 60 soru korunarak onarildi: genisletilmis ELEME_ISARETI olcutune gore 38 mutlak ifadeli sik ayni dogruluk degerini koruyacak bicimde yeniden yazildi; gerekce tasiyan 9 dogru sik kisaltildi. Kor ogrenci %36 -> %24.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 6102 sayili Turk Ticaret Kanunu (police, bono, cek hukumleri)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/ticaret_hukuku/kambiyo_senetleri.json"
STYLE_REF = 'SGS Ticaret Hukuku (gercek sinav yapisina kalibre: olay + kural uygulamasi)'
ONEK = "kmb-gen-"


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
        "Bir senette 'poliçe' kelimesi yer almakta ancak vade kaydı bulunmamaktadır. Başka bir senette ise 'bono' kelimesi bulunmamakta, yalnızca ödeme vaadi yazmaktadır. Buna göre kambiyo senetlerinde şekle bağlılık ilkesi bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Vadesi gösterilmeyen poliçe geçersiz sayılır; 'bono' kelimesindeki eksiklik ise kanunen tamamlanabilir",
            'B': 'Eksik unsurları hamil dilediği zaman tamamlayabilir',
            'C': 'Her iki senet de geçerli kambiyo senedi sayılır',
            'D': "Poliçe görüldüğünde ödenecek sayılır; 'bono' kelimesi olmayan senet bono sayılmaz",
            'E': 'Her iki senet de geçersizdir ve sonuç doğurmaz',
        },
        'D',
        "TTK md. 671-672: poliçede vade zorunlu unsurdur; ancak vade gösterilmemişse senet GÖRÜLDÜĞÜNDE ödenecek poliçe sayılır (kanuni tamamlama). md. 776-777: bonoda 'BONO' veya 'emre muharrer senet' kelimesi kanunen tamamlanamayan zorunlu unsurdur; yokluğu senedi bono olmaktan çıkarır.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0002': patch(
        "Bir bononun üzerine 'emre yazılı değildir' kaydı düşülmüştür. Buna göre senedin devri bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Senet yine ciro ile devredilir; kayıt sonuç doğurmaz',
            'B': 'Senet hamiline yazılı hâle gelir ve bundan sonra zilyetliğin devriyle devredilir',
            'C': 'Senet devredilemez hâle gelir',
            'D': 'Senet nama yazılı hâle gelir ve alacağın temliki hükümlerine göre devredilir',
            'E': 'Kayıt senedi geçersiz kılar',
        },
        'D',
        "TTK md. 681: kambiyo senetleri KANUNEN EMRE YAZILIDIR; ciro ile devredilir. Ancak senede 'EMRE YAZILI DEĞİLDİR' ya da buna eş bir kayıt konulmuşsa senet nama yazılı hâle gelir ve ALACAĞIN TEMLİKİ hükümlerine göre devredilir.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0003': patch(
        'Bir çekin üzerine ileri bir tarih vade olarak yazılmış; ayrıca muhatap bankaya kabul için ibraz edilmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Çekte kabul mümkün olup kabul şerhiyle birlikte muhatap banka çekin asıl borçlusu hâline gelir',
            'B': 'Çekte vade bulunmaz; çek görüldüğünde ödenir ve kabul yasaktır, kabul şerhi yazılmamış sayılır',
            'C': 'Vade yazılması çeki geçersiz kılar',
            'D': 'Kabul için ibraz çeki bonoya dönüştürür',
            'E': 'Çekteki vade geçerlidir; çek vade tarihinde ödenir',
        },
        'B',
        'TTK md. 795: çek GÖRÜLDÜĞÜNDE ödenir; buna aykırı herhangi bir kayıt yazılmamış hükmündedir. md. 784: çekte KABUL YASAKTIR; çek üzerine yazılan kabul şerhi yazılmamış sayılır. Muhatap banka kabul yoluyla asıl borçlu hâline gelmez.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0004': patch(
        'Bir poliçe muhataba ibraz edilmiş ve muhatap poliçeyi kabul etmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kabul muhatabın ödeme niyetini gösterir; borç doğurmaz',
            'B': 'Kabul edilen poliçede protesto çekilmesi gerekmez',
            'C': 'Kabulle düzenleyenin sorumluluğu sona erer',
            'D': 'Kabul eden muhatap ikinci derecede sorumlu olur',
            'E': 'Kabul eden muhatap poliçenin asıl borçlusu hâline gelir',
        },
        'E',
        'TTK md. 691: muhatap kabul ile poliçe bedelini vadesinde ödemek yükümlülüğü altına girer; poliçenin ASIL BORÇLUSU olur. Düzenleyenin sorumluluğu sona ermez; kabul etmeme ya da ödememe hâlinde müracaat hakkı için protesto gerekir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0005': patch(
        "Bir poliçede vade olarak 'düzenlenme gününden üç ay sonra' yazılmıştır. Bir diğerinde 'görüldükten on gün sonra' kaydı bulunmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Düzenlenme gününden belirli süre sonra vadesi geçersizdir',
            'B': 'Belirli bir günde ödeme dışındaki vadeler geçersizdir',
            'C': 'Poliçede görüldüğünde ödeme vadesi dışında vade konulamaz',
            'D': 'Her iki vade türü de kanunda öngörülmüştür ve geçerlidir',
            'E': 'Görüldükten belirli süre sonra vadesi kanunda öngörülmemiştir',
        },
        'D',
        'TTK md. 703: poliçe görüldüğünde, görüldükten belirli bir süre sonra, düzenlenme gününden belirli bir süre sonra ya da belirli bir günde ödenmek üzere düzenlenebilir. Bunlardan başka vadeleri gösteren veya birbirini izleyen vadeleri içeren poliçeler geçersizdir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0006': patch(
        "Bir hamil, vadesinde ödenmeyen bonoyu protesto ettirmeden doğrudan cirantalara başvurmuştur. Senette 'protestosuz' kaydı bulunmamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Cirantalara başvuru için ödememe protestosu çekilmesi gerekir',
            'B': "Protesto ancak 'protestosuz' kaydı varsa gerekir",
            'C': 'Protesto eksikliği düzenleyene başvuruyu da engeller',
            'D': 'Protesto poliçeye özgüdür',
            'E': 'Protesto çekilmesi gerekmez; hamil müracaat hakkını doğrudan bütün cirantalara karşı kullanabilir',
        },
        'A',
        "TTK md. 714 ve 725: kabul etmeme veya ödememe, PROTESTO adı verilen resmî bir belgeyle belirlenir; hamilin cirantalara, düzenleyene ve diğer borçlulara müracaat hakkı protestonun çekilmesine bağlıdır. 'PROTESTOSUZ' kaydı bu külfeti kaldırır. Bono düzenleyeni asıl borçlu olduğundan ona başvuru için protesto gerekmez.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0007': patch(
        'Bir tacir, elindeki poliçe, bono ve çeki ortak özellikleri bakımından karşılaştırmaktadır. Buna göre kambiyo senetleri bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kambiyo senetleri kanunen nama yazılı olup alacağın temliki ile devredilir',
            'B': 'Kambiyo senetleri şekle sıkı biçimde bağlıdır',
            'C': 'Kambiyo senetlerinde imzaların bağımsızlığı ilkesi kanun tarafından benimsenmiştir',
            'D': 'Kambiyo senetleri poliçe, bono ve çektir',
            'E': 'Kambiyo senetleri mücerret (soyut) senetlerdir',
        },
        'A',
        "TTK md. 681 ve 824: kambiyo senetleri KANUNEN EMRE YAZILIDIR ve ciro ile devredilir; nama yazılı hâle gelmeleri ancak 'emre yazılı değildir' kaydıyla mümkündür.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0008': patch(
        'Bono ile poliçe karşılaştırılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bono iki taraflıdır: düzenleyen ve lehtar',
            'B': 'Bonoda düzenleyen bizzat ödeme vaadinde bulunur',
            'C': 'Bonoda muhatap bulunur ve düzenleyen muhataba havale verir',
            'D': 'Bono düzenleyeni poliçeyi kabul eden muhatap gibi sorumludur',
            'E': 'Poliçe üç taraflıdır: düzenleyen, muhatap ve lehtar',
        },
        'C',
        'TTK md. 776: bonoda MUHATAP YOKTUR; düzenleyen bizzat ödeme vaadinde bulunur ve senet iki taraflıdır. Havale ve muhatap POLİÇEYE (md. 671) ve çeke özgüdür.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0009': patch(
        'Aval kurumu incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Aval veren kişi, kimin için taahhüt altına girmişse tam olarak onun gibi sorumlu olur',
            'B': 'Aval kambiyo senetlerinde mümkündür',
            'C': 'Avalin taahhüdü şekle ilişkin noksanlık dışında geçerli kalır',
            'D': 'Aval, senet bedelinin ödenmesini güvence altına alır',
            'E': 'Lehine aval verilenin borcu herhangi bir sebeple geçersizse aval de geçersiz olur',
        },
        'E',
        'TTK md. 702: aval verenin taahhüdü, lehine taahhüt altına girdiği kişinin borcu ŞEKLE İLİŞKİN NOKSANLIK DIŞINDA herhangi bir sebeple geçersiz olsa da GEÇERLİDİR.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0010': patch(
        'Çekte ibraz süreleri incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Başka yerde ödenecek çek bir ay içinde ibraz edilir',
            'B': 'Çekte ibraz süresi öngörülmemiş olup çek dilendiğinde ibraz edilebilir',
            'C': 'İbraz süreleri kanunda düzenlenmiştir',
            'D': 'Süresinde ibraz edilmeyen çekte müracaat hakkı düşer',
            'E': 'Düzenlendiği yerde ödenecek olan çek, on gün içinde muhatap bankaya ibraz edilir',
        },
        'B',
        'TTK md. 796: çek düzenlendiği yerde ödenecekse ON GÜN, başka yerde ödenecekse BİR AY içinde muhataba ibraz edilmelidir; süreler kanunda açıkça öngörülmüştür.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0011': patch(
        'Kambiyo senetlerinin devri incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kambiyo senetleri kanunen emre yazılıdır',
            'B': 'Nama yazılı hâle gelen senet alacağın temliki ile devredilir',
            'C': 'Kambiyo senetleri kural olarak ciro ve teslimle devredilir',
            'D': "Senede konulan 'emre yazılı değildir' kaydı, senedi nama yazılı senet hâline getirir",
            'E': "Kambiyo senedine konulan 'emre yazılı değildir' kaydı yazılmamış sayılır",
        },
        'E',
        "TTK md. 681: 'EMRE YAZILI DEĞİLDİR' kaydı yazılmamış sayılmaz; tam tersine senedi nama yazılı hâle getirir ve alacağın temliki hükümlerine tabi kılar.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0012': patch(
        'Poliçede vade türleri incelenmektedir. Buna göre aşağıdakilerden hangisi bir vade türü değildir?',
        {
            'A': 'Alacaklının talep ettiği tarihte ödenmek üzere düzenlenen poliçe',
            'B': 'Düzenlenme gününden belirli bir süre geçtikten sonra ödenmek üzere düzenlenen poliçe',
            'C': 'Belirli bir günde ödenecek poliçe',
            'D': 'Görüldüğünde ödenecek poliçe',
            'E': 'Görüldükten belirli bir süre sonra ödenecek poliçe',
        },
        'A',
        'TTK md. 703: poliçe görüldüğünde, görüldükten belirli süre sonra, düzenlenme gününden belirli süre sonra ya da belirli bir günde ödenmek üzere düzenlenebilir. Bunlardan BAŞKA vadeleri içeren poliçeler GEÇERSİZDİR; alacaklının takdirine bırakılan vade kanunda yoktur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0013': patch(
        'Muhatabı yalnızca banka olabilen kambiyo senedi aşağıdakilerden hangisidir?',
        {
            'A': 'Konşimento',
            'B': 'Bono',
            'C': 'Çek',
            'D': 'Poliçe',
            'E': 'Makbuz senedi',
        },
        'C',
        'TTK md. 782: çek ancak bir BANKA üzerine düzenlenebilir; poliçede muhatap herhangi bir kişi olabilir, bonoda ise muhatap yoktur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0014': patch(
        'Kambiyo senedi bedelinin ödenmesini güvence altına alan kambiyo hukuku kurumu aşağıdakilerden hangisidir?',
        {
            'A': 'Kabul',
            'B': 'İbraz',
            'C': 'Aval',
            'D': 'Protesto',
            'E': 'Ciro',
        },
        'C',
        'TTK md. 700: poliçede bedelin ödenmesi, aval şerhiyle tamamen veya kısmen güvence altına alınabilir; AVAL bir kambiyo taahhüdüdür.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0015': patch(
        'Bir poliçe muhataba ibraz edilmiş ancak muhatap kabulden kaçınmıştır. Buna göre hamilin izleyeceği yol aşağıdakilerden hangisidir?',
        {
            'A': 'Senedi geçersiz saymak',
            'B': 'Muhatabı kabule zorlamak için dava açmak',
            'C': 'Vadenin gelmesini beklemek dışında bir yol izlememek',
            'D': 'Protesto çekmeksizin doğrudan icra takibi başlatmak ve müracaat hakkını kullanmak',
            'E': 'Kabul etmeme protestosu çekerek müracaat hakkını kullanmak',
        },
        'E',
        'TTK md. 714 ve 716: muhatap kabulden kaçınırsa hamil KABUL ETMEME PROTESTOSU çekerek vadeden önce müracaat hakkını kullanabilir; muhatabı kabule zorlama imkânı yoktur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0016': patch(
        'Bir poliçede vade gösterilmemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Vadeyi hamil dilediği gibi doldurur',
            'B': 'Poliçe geçersizdir',
            'C': 'Poliçe görüldüğünde ödenecek sayılır',
            'D': 'Vade muhatabın belirlediği tarihtir',
            'E': 'Poliçe bir yıl sonra ödenecek sayılır',
        },
        'C',
        'TTK md. 672: vadesi gösterilmemiş poliçe, GÖRÜLDÜĞÜNDE ödenecek poliçe sayılır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0017': patch(
        "Bir kambiyo senedinde 'protestosuz' kaydı bulunmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Kayıt çeklere özgüdür',
            'B': 'Kayıt senedi geçersiz kılar',
            'C': "'Protestosuz' kaydı, hamilin cirantalara ve düzenleyene karşı müracaat hakkını ortadan kaldırır",
            'D': 'Hamil, müracaat hakkını kullanmak için protesto çekme külfetinden kurtulur',
            'E': 'Kayıt geçersizdir ve protesto yine gereklidir',
        },
        'D',
        "TTK md. 722: düzenleyen, ciranta veya aval veren, senede 'PROTESTOSUZ' ya da 'masrafsız' kaydını koyarak hamili protesto çekme külfetinden kurtarabilir; müracaat hakkı devam eder.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0018': patch(
        'Aval ve ciro ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Aval veren, lehine aval verdiği kişi gibi sorumludur. II. Tahsil cirosu mülkiyeti devretmez. III. Beyaz ciro geçersizdir.',
        {
            'A': 'I, II ve III',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'C',
        'I doğrudur (TTK md. 702). II doğrudur (md. 688). III YANLIŞTIR: md. 683 uyarınca beyaz ciro geçerlidir ve yalnızca cirantanın imzasıyla yapılır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0019': patch(
        'Bir poliçede ödeme yeri gösterilmemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ödeme yeri, poliçeyi düzenleyen kişinin yerleşim yeri olarak kabul edilir',
            'B': 'Poliçe geçersizdir',
            'C': 'Muhatabın adı yanında yazılı yer ödeme yeri sayılır',
            'D': 'Ödeme yeri mahkemece belirlenir',
            'E': 'Ödeme yeri hamilin yerleşim yeridir',
        },
        'C',
        'TTK md. 672: ödeme yeri gösterilmemiş poliçede, MUHATABIN ADI YANINDA yazılı olan yer ödeme yeri ve aynı zamanda muhatabın yerleşim yeri sayılır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0020': patch(
        'Kambiyo senetlerinde şekle bağlılık incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Senet kelimesi ve imza gibi unsurlar tamamlanamaz',
            'B': 'Zorunlu unsurların tamamı kanunen tamamlanabilir niteliktedir',
            'C': 'Kambiyo senetleri şekle sıkı biçimde bağlıdır',
            'D': 'Bazı eksiklikler kanunen tamamlanır (vade, ödeme yeri, düzenlenme yeri)',
            'E': 'Tamamlanamayan unsur eksikse senet o tür kambiyo senedi sayılmaz',
        },
        'B',
        'TTK md. 671-672, 776-777, 780-781: zorunlu unsurların yalnızca BİR KISMI (vade, ödeme yeri, düzenlenme yeri) kanunen tamamlanır. Senet kelimesi, imza ve düzenlenme tarihi gibi unsurlar TAMAMLANAMAZ.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0021': patch(
        'Bir kambiyo senedinde üç imza bulunmaktadır: birincisi ehliyetsiz bir kişiye, ikincisi sahte bir imzaya, üçüncüsü ise geçerli bir imzaya aittir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Geçerli imza sahibi, ancak senetteki bütün diğer imzalar da geçerli olduğu takdirde sorumlu olur',
            'B': 'Ehliyetsizlik hâlinde tüm imza sahipleri sorumluluktan kurtulur',
            'C': 'Bir imzanın geçersizliği senedin tamamını geçersiz kılar',
            'D': 'Sahte imza bulunması hâlinde senet hükümsüz olur',
            'E': 'Geçersiz imzalar diğerlerinin geçerliliğini etkilemez; geçerli imza sahibi sorumlu kalır',
        },
        'E',
        'TTK md. 677 (imzaların bağımsızlığı): kambiyo senedi, borç altına girme ehliyeti bulunmayan kişilerin imzasını, sahte imzaları, hayali kişilerin imzalarını veya imzalayanı bağlamayan imzaları taşırsa, DİĞER İMZALARIN GEÇERLİLİĞİ bundan etkilenmez.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0022': patch(
        'Bir bonoyu düzenleyen, iki ciranta ve bir aval veren bulunmaktadır. Hamil vadede ödeme alamamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Hamil önce düzenleyene başvurur; ondan sonuç alamadığı takdirde cirantalara yönelebilir',
            'B': 'Cirantalar hamile karşı sorumlu değildir',
            'C': 'Hepsi hamile karşı müteselsilen sorumludur; hamil dilediğine başvurabilir',
            'D': 'Sorumluluk imza sırasına göre tek tek işler',
            'E': 'Aval verenin sorumluluğu ancak düzenleyen ödeme yapmazsa doğar',
        },
        'C',
        'TTK md. 724: bir poliçeyi düzenleyen, kabul eden, ciro eden veya aval veren kişiler hamile karşı MÜTESELSİLEN borçludur. Hamil bunlardan birine, birkaçına veya hepsine, borç altına girişlerindeki sıraya bağlı kalmaksızın başvurabilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0023': patch(
        "Türk Ticaret Kanunu'na göre kambiyo senetleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Poliçe, bono ve çek kambiyo senetleridir. II. Kambiyo senetleri kanunen emre yazılıdır. III. Konşimento da bir kambiyo senedidir.",
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'Yalnız I',
            'D': 'I ve III',
            'E': 'I, II ve III',
        },
        'B',
        'I doğrudur (TTK md. 670 vd.). II doğrudur (md. 681, 824). III YANLIŞTIR: konşimento bir emtia senedidir; kambiyo senedi değildir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0024': patch(
        'Bir poliçede ödeme yeri ve düzenlenme yeri gösterilmemiştir; muhatabın adı yanında bir yer, düzenleyenin adı yanında da başka bir yer yazılıdır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ödeme yeri eksikliği poliçeyi geçersiz kılar; düzenlenme yeri eksikliği ise kanun gereği tamamlanabilir',
            'B': 'Eksik yerler muhatabın beyanına göre belirlenir',
            'C': 'Her iki eksiklik de poliçeyi geçersiz kılar',
            'D': 'Her iki yeri de hamil dilediği gibi doldurur',
            'E': 'Muhatabın adı yanındaki yer ödeme yeri, düzenleyenin adı yanındaki yer düzenlenme yeri sayılır',
        },
        'E',
        'TTK md. 672: ödeme yeri gösterilmeyen poliçede muhatabın adı yanında yazılı yer ödeme yeri ve aynı zamanda muhatabın yerleşim yeri sayılır. Düzenlenme yeri gösterilmeyen poliçe, düzenleyenin adı yanında yazılı yerde düzenlenmiş sayılır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0025': patch(
        'Bir senedin çek sayılabilmesi için taşıması gereken unsurlar belirlenmektedir. Buna göre aşağıdakilerden hangisi çekin zorunlu unsurlarından biri değildir?',
        {
            'A': 'Senedin vadesini gösteren kayıt',
            'B': 'Kayıtsız ve şartsız belirli bir bedelin ödenmesi için havale',
            'C': 'Muhatap bankanın ticaret unvanı',
            'D': "Senet metninde 'çek' kelimesi",
            'E': 'Düzenlenme tarihi ve yeri ile düzenleyenin imzası',
        },
        'A',
        "TTK md. 780: çekin zorunlu unsurları arasında VADE YOKTUR; md. 795 uyarınca çek görüldüğünde ödenir ve aksine kayıtlar yazılmamış sayılır. Muhatabın BANKA olması ise md. 782'nin gereğidir.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0026': patch(
        'Bir bonoya aval veren kişi, lehine aval verdiği cirantanın imzasının sahte olduğunu öğrenmiş ve kendi taahhüdünün de geçersiz olduğunu ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Aval poliçeye özgüdür',
            'B': 'Lehine aval verilen kişinin borcu herhangi bir sebeple geçersiz sayılırsa aval taahhüdü de geçersiz olur',
            'C': 'Aval veren lehtara karşı sorumlu olur, hamillere karşı değil',
            'D': 'Şekil noksanlığı dışında, asıl borç geçersiz olsa da aval geçerlidir',
            'E': 'Aval verenin sorumluluğu lehine aval verilenden daha hafiftir',
        },
        'D',
        'TTK md. 702: aval veren kişi, kimin için taahhüt altına girmişse tam olarak onun GİBİ sorumlu olur. Aval verenin taahhüdü, lehine taahhüt altına girdiği kişinin borcu ŞEKLE İLİŞKİN noksanlık dışında herhangi bir sebeple geçersiz olsa da GEÇERLİDİR.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0027': patch(
        'Bir hamil, kambiyo senedinden doğan hakkını zamanaşımı nedeniyle kaybetmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Hamil, kambiyo hakkıyla birlikte temel ilişkiye dayanan talep haklarını da kaybeder',
            'B': 'Hamil, düzenleyen ve kabul edene karşı sebepsiz zenginleşme davası açabilir',
            'C': 'Zamanaşımı sonrası talep hakkı kalmaz',
            'D': 'Hamil cirantalara başvurabilir, düzenleyene başvuramaz',
            'E': 'Zamanaşımı kambiyo senetlerinde işlemez',
        },
        'B',
        'TTK md. 732: zamanaşımı veya kambiyo hukukuna özgü işlemlerin yapılmasına gerekli sürelerin geçmesi nedeniyle poliçeden doğan haklar düşmüş olsa bile, düzenleyen ve KABUL EDEN, hamilin zararına SEBEPSİZ ZENGİNLEŞTİKLERİ ölçüde borçlu kalır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0028': patch(
        'Bir senette üç imzadan biri ehliyetsiz bir kişiye aittir. Buna göre imzaların bağımsızlığı ilkesi bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İlke kambiyo senetlerinin tedavül güvenliğine hizmet eder',
            'B': 'Geçersiz imza diğer imzaların geçerliliğini etkilemez',
            'C': 'Hayali kişilerin imzası diğerlerini etkilemez',
            'D': 'Bir imzanın geçersizliği senetteki tüm imzaları geçersiz kılar',
            'E': 'Sahte imza bulunması senedi hükümsüz kılmaz',
        },
        'D',
        'TTK md. 677: kambiyo senedi borç altına girme ehliyeti bulunmayan kişilerin imzasını, sahte imzaları veya hayali kişilerin imzalarını taşırsa DİĞER İMZALARIN GEÇERLİLİĞİ bundan ETKİLENMEZ.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0029': patch(
        'Bir poliçenin zorunlu unsurları incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Poliçe metninde 'poliçe' kelimesi bulunmalıdır",
            'B': 'Vadesi gösterilmeyen poliçe zorunlu unsur eksikliği nedeniyle geçersizdir',
            'C': 'Vadesi gösterilmeyen poliçe görüldüğünde ödenecek sayılır',
            'D': 'Kayıtsız şartsız belirli bir bedelin ödenmesi için havale bulunmalıdır',
            'E': 'Ödeme yeri gösterilmemişse muhatabın adı yanındaki yer esas alınır',
        },
        'B',
        'TTK md. 672: vadesi gösterilmemiş poliçe GÖRÜLDÜĞÜNDE ödenecek poliçe sayılır; bu kanuni bir tamamlamadır ve senedi geçersiz kılmaz.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0030': patch(
        'Kambiyo senetlerinde protesto incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Cirantalara müracaat için kural olarak protesto gerekir',
            'B': 'Bono düzenleyenine başvuru için protesto gerekmez',
            'C': "'Protestosuz' kaydı protesto külfetini kaldırır",
            'D': 'Protesto, senedin geçerliliği için aranan bir şekil şartıdır',
            'E': 'Protesto kabul etmeme veya ödememenin resmî belgeyle tespitidir',
        },
        'D',
        'TTK md. 714 vd.: protesto senedin GEÇERLİLİK ŞARTI DEĞİLDİR; müracaat hakkının korunması için aranan bir işlemdir. Senedin geçerliliği zorunlu şekil unsurlarına bağlıdır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0031': patch(
        'Kambiyo senetlerinde zamanaşımı incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Cirantaların birbirlerine karşı talepleri altı ayda zamanaşımına uğrar',
            'B': 'Zamanaşımı dolsa da sebepsiz zenginleşme davası açılabilir',
            'C': 'Hamilin cirantalara karşı talepleri protesto tarihinden itibaren bir yılda zamanaşımına uğrar',
            'D': 'Kabul edene karşı talepler vadeden itibaren üç yılda zamanaşımına uğrar',
            'E': 'Kabul edene karşı talepler on yıllık genel zamanaşımına tabidir',
        },
        'E',
        'TTK md. 749: poliçeyi kabul edene karşı talepler VADEDEN itibaren ÜÇ YIL geçmekle zamanaşımına uğrar; genel on yıllık süre uygulanmaz.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0032': patch(
        'Poliçede kabul kurumu incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kabul poliçe üzerine yazılır ve imzalanır',
            'B': 'Muhatap kabul ile poliçenin asıl borçlusu olur',
            'C': 'Kabul etmeme hâlinde protesto çekilebilir',
            'D': 'Çekte kabul yasaktır',
            'E': 'Kabulle birlikte düzenleyenin sorumluluğu sona erer',
        },
        'E',
        'TTK md. 691 ve 725: muhatap kabul ile asıl borçlu olur; ancak DÜZENLEYENİN sorumluluğu SONA ERMEZ, müracaat borçlusu olarak devam eder.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0033': patch(
        'Bir tacir elindeki senetleri sınıflandırırken kambiyo senetlerini ayırmaktadır. Buna göre aşağıdakilerden hangisi bir kambiyo senedi değildir?',
        {
            'A': 'Emre yazılı olarak düzenlenmiş poliçe',
            'B': 'Çek',
            'C': 'Konşimento',
            'D': 'Poliçe',
            'E': 'Bono',
        },
        'C',
        'TTK md. 670 vd.: kambiyo senetleri POLİÇE, BONO ve ÇEKTİR. Konşimento bir emtia senedidir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0034': patch(
        'Kabul etmeme veya ödememenin resmî bir belgeyle tespit edilmesi işlemi aşağıdakilerden hangisidir?',
        {
            'A': 'Kabul',
            'B': 'Aval',
            'C': 'Ciro',
            'D': 'Protesto',
            'E': 'Ödeme yasağı',
        },
        'D',
        'TTK md. 714: kabul etmeme veya ödememe, PROTESTO adı verilen resmî bir belgeyle belirlenir; müracaat hakkının korunması için gereklidir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0035': patch(
        'Bir bononun düzenleyeni ödeme yapmamıştır. Hamil düzenleyene başvurmak istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Düzenleyene başvuru için mahkeme kararı gerekir',
            'B': 'Bono düzenleyeni asıl borçlu olduğundan ona başvuru için protesto gerekmez',
            'C': 'Bono düzenleyeni, ancak cirantalar ödeme yapmazsa ikinci derecede sorumlu tutulur',
            'D': 'Düzenleyene başvuru için de protesto çekilmesi gerekir',
            'E': 'Düzenleyenin sorumluluğu vadeyle sona erer',
        },
        'B',
        'TTK md. 778/3: bono düzenleyeni poliçeyi KABUL EDEN MUHATAP gibi sorumludur; asıl borçlu olduğundan ona başvurmak için protesto çekilmesi gerekmez.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0036': patch(
        "Bir senette 'bono' veya 'emre muharrer senet' kelimesi bulunmamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Senet poliçeye dönüşür',
            'B': "Senet metnindeki 'bono' kelimesi eksikliği, sonradan hamil tarafından tamamlanabilir",
            'C': 'Senet bono sayılmaz; kanunen tamamlanamayan bir zorunlu unsur eksiktir',
            'D': 'Senet çek sayılır',
            'E': 'Senet yine bono sayılır',
        },
        'C',
        "TTK md. 776-777: senet metninde 'BONO' veya 'EMRE MUHARRER SENET' kelimesinin bulunması zorunludur ve bu eksiklik kanunen tamamlanamaz; senet bono sayılmaz.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0037': patch(
        'Bir cirantanın sorumluluğu incelenmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ciranta sorumluluk üstlenmez',
            'B': 'Ciranta, aksi kararlaştırılmadıkça kabul edilmeme ve ödenmemeden sorumludur',
            'C': 'Cirantanın sorumluluğu senet üzerinde açıkça yazılmadıkça doğmaz',
            'D': 'Ciranta ancak asıl borçlu ödeme yapmazsa ve mahkeme kararıyla sorumlu olur',
            'E': 'Ciranta kendisinden sonraki hamillere karşı sorumsuzdur',
        },
        'B',
        "TTK md. 685: ciranta, aksi kararlaştırılmadıkça poliçenin KABUL EDİLMEMESİNDEN ve ÖDENMEMESİNDEN sorumludur; sorumluluk kanundan doğar. Ciranta 'ciro edilemez' kaydıyla sonraki hamillere karşı sorumluluğunu kaldırabilir.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0038': patch(
        'Zamanaşımı ve müracaat ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Kabul edene karşı talepler vadeden itibaren üç yılda zamanaşımına uğrar. II. Protesto senedin geçerlilik şartıdır. III. Zamanaşımı dolsa da sebepsiz zenginleşme davası açılabilir. IV. Bono düzenleyenine başvuru için protesto gerekir.',
        {
            'A': 'Yalnız II',
            'B': 'I, II ve IV',
            'C': 'II ve III',
            'D': 'I ve III',
            'E': 'II ve IV',
        },
        'E',
        'II YANLIŞ: protesto geçerlilik şartı değil, müracaat hakkının korunması için gereken bir işlemdir. IV YANLIŞ: bono düzenleyeni asıl borçludur, ona başvuru için protesto gerekmez (TTK md. 778/3). I (md. 749) ve III (md. 732) doğrudur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0039': patch(
        'Çek ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Çek görüldüğünde ödenir. II. Çekte kabul yasaktır. III. Çekte muhatap herhangi bir tüzel kişi olabilir.',
        {
            'A': 'I ve II',
            'B': 'I ve III',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'A',
        'I doğrudur (TTK md. 795). II doğrudur (md. 784). III YANLIŞTIR: md. 782 uyarınca çekte muhatap ancak BANKA olabilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0040': patch(
        'Bir hamil, süresinde ibraz etmediği çekin bedelini cirantadan istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Çekte ibraz süresi bulunmadığından sorun doğmaz',
            'B': 'Müracaat hakkı düzenleyene karşı düşer, cirantalara karşı düşmez',
            'C': 'İbraz süresi geçtiğinde çek geçersiz olur',
            'D': 'İbraz süresi geçmiş olsa dahi hamilin cirantalara ve düzenleyene karşı müracaat hakkı devam eder',
            'E': 'Süresinde ibraz edilmeyen çekte hamilin cirantalara karşı müracaat hakkı düşer',
        },
        'E',
        'TTK md. 808: süresi içinde ibraz edilmeyen çekte hamilin cirantalara, düzenleyene ve diğer borçlulara karşı MÜRACAAT HAKKI DÜŞER. Çek geçersiz olmaz; sebepsiz zenginleşme ve temel ilişkiye dayanan talepler ayrıca değerlendirilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0041': patch(
        'Bir bono, mal alım satımından doğan bir borç için düzenlenmiştir. Satış sözleşmesi sonradan geçersiz sayılmış; senedi ciro yoluyla devralan iyiniyetli hamil ödeme talep etmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Hamil ancak temel ilişki geçerliyse ödeme talep edebilir',
            'B': "Temel ilişkiye dayanan def'i iyiniyetli hamile karşı ileri sürülemez",
            'C': "Borçlu, temel ilişkiye dayanan def'iyi hamilin iyiniyetli olup olmadığına bakılmaksızın herkese karşı ileri sürebilir",
            'D': 'Mücerretlik poliçeye özgüdür',
            'E': 'Temel ilişkinin geçersizliği senedi de geçersiz kılar',
        },
        'B',
        "Kambiyo senetleri MÜCERRET (soyut) senetlerdir; senetteki borç temel ilişkiden bağımsızdır. TTK md. 687: borçlu, temel ilişkiye dayanan kişisel def'ileri, hamil senedi devralırken bilerek borçlunun zararına hareket etmiş olmadıkça ileri süremez.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0042': patch(
        'Üç senet incelenmektedir: (A) düzenleyen, muhatap ve lehtar olmak üzere üç taraflı ve muhataba havale içeren senet; (B) düzenleyenin bizzat ödeme vaadi içeren iki taraflı senet; (C) muhatabı banka olan ve görüldüğünde ödenen senet. Buna göre bu senetler sırasıyla aşağıdakilerden hangisidir?',
        {
            'A': 'Bono – çek – poliçe',
            'B': 'Poliçe – bono – çek',
            'C': 'Bono – poliçe – çek',
            'D': 'Poliçe – çek – bono',
            'E': 'Çek – bono – poliçe',
        },
        'B',
        "TTK md. 671: POLİÇE üç taraflıdır (düzenleyen, muhatap, lehtar) ve muhataba yönelik kayıtsız şartsız havale içerir. md. 776: BONO iki taraflıdır ve düzenleyenin bizzat ÖDEME VAADİNİ içerir; muhatap yoktur. md. 780 ve 782: ÇEK'te muhatap ancak BANKA olabilir ve çek görüldüğünde ödenir.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0043': patch(
        'Bir bonoyu düzenleyen kişi, sorumluluğunun poliçeyi kabul eden muhataptan daha hafif olduğunu ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bono düzenleyeni protesto çekilmedikçe sorumlu olmaz',
            'B': 'Bono düzenleyeni lehtara karşı sorumludur, sonraki hamillere karşı değil',
            'C': 'Bono düzenleyeninin sorumluluğu, senedi ciro eden kişilerin sorumluluğuyla aynıdır',
            'D': 'Bono düzenleyeni ikinci derecede sorumludur',
            'E': 'Bono düzenleyeni, poliçeyi kabul eden muhatap gibi sorumludur',
        },
        'E',
        'TTK md. 778/3: bononun düzenleyeni, POLİÇEYİ KABUL EDEN MUHATAP GİBİ sorumludur. Yani asıl borçludur; sorumluluğu için protesto çekilmesi gerekmez ve tüm hamillere karşı devam eder.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0044': patch(
        'Bir senedin bono sayılabilmesi için taşıması gereken unsurlar belirlenmektedir. Buna göre aşağıdakilerden hangisi bononun zorunlu unsurlarından biri değildir?',
        {
            'A': 'Muhatabın adı ve soyadı ile ticaret unvanı',
            'B': 'Kayıtsız ve şartsız belirli bir bedeli ödemek vaadi',
            'C': 'Lehtarın adı ve soyadı ile ticaret unvanı',
            'D': 'Düzenlenme tarihi ile düzenleyenin imzası',
            'E': "Senet metninde 'bono' veya 'emre muharrer senet' kelimesi",
        },
        'A',
        "TTK md. 776: bononun zorunlu unsurları 'bono' veya 'emre muharrer senet' kelimesi, kayıtsız şartsız ödeme vaadi, vade, ödeme yeri, lehtar, düzenlenme tarihi ve yeri ile düzenleyenin imzasıdır. Bonoda MUHATAP YOKTUR; muhatap poliçe ve çeke özgüdür.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0045': patch(
        'Bir çek, düzenlendiği yerde ödenecek biçimde düzenlenmiştir. Hamil çeki düzenlenme tarihinden 20 gün sonra bankaya ibraz etmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'On günlük ibraz süresi geçtiğinden müracaat hakkı düşer',
            'B': 'Süre geçse de müracaat hakkı devam eder',
            'C': 'İbraz süresi bir ay olduğundan ibraz süresindedir',
            'D': 'Çekte ibraz süresi öngörülmemiştir',
            'E': 'Çekte ibraz süresi yurt dışında düzenlenip yurt içinde ödenecek çeklere özgüdür',
        },
        'A',
        'TTK md. 796: bir çek düzenlendiği yerde ödenecekse ON GÜN, düzenlendiği yerden başka bir yerde ödenecekse BİR AY içinde muhataba ibraz edilmelidir. Süresinde ibraz edilmeyen çekte hamilin cirantalara ve düzenleyene karşı MÜRACAAT HAKKI düşer (md. 808).',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0046': patch(
        "Bir kambiyo senedinin arkasına 'bedeli teminattır' kaydıyla ciro yapılmıştır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Tahsil cirosudur; hamile senedin mülkiyeti geçmeksizin tahsil yetkisi verilir',
            'B': 'Temlik cirosudur; mülkiyet ciro edilene geçer',
            'C': 'Beyaz cirodur; lehtar gösterilmemiştir',
            'D': 'Rehin cirosudur; hamil hakları kullanır, mülkiyeti kazanmaz',
            'E': 'Kayıt geçersiz olup ciro temlik cirosu sayılır',
        },
        'D',
        "TTK md. 689: 'bedeli teminattır', 'bedeli rehindir' veya rehni ifade eden diğer kayıtları taşıyan ciro REHİN CİROSUDUR. Hamil poliçeden doğan bütün hakları kullanabilir; ancak mülkiyeti kazanmadığından yaptığı ciro tahsil cirosu hükmündedir.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0047': patch(
        "Bir bonoda vade 1 Haziran'dır. Hamil, kabul eden konumundaki düzenleyene karşı hakkını ne kadar süreyle ileri sürebileceğini araştırmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Poliçeyi kabul edene karşı ileri sürülecek talepler vadeden itibaren bir yıllık zamanaşımına tabidir',
            'B': 'Kabul edene karşı talepler vadeden itibaren üç yıllık zamanaşımına tabidir',
            'C': 'Kambiyo senetlerinde zamanaşımı işlemez',
            'D': 'Kabul edene karşı talepler altı aylık zamanaşımına tabidir',
            'E': 'Kabul edene karşı talepler on yıllık zamanaşımına tabidir',
        },
        'B',
        'TTK md. 749: poliçeyi kabul edene karşı ileri sürülecek talepler VADEDEN itibaren ÜÇ YIL geçmekle zamanaşımına uğrar. Hamilin cirantalarla düzenleyene karşı talepleri protesto tarihinden itibaren bir yıl, cirantaların birbirlerine ve düzenleyene karşı talepleri ise altı ay içinde zamanaşımına uğrar.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0048': patch(
        'Bir çekin hukuki rejimi incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Çekin muhatap bankaya ibraz süreleri kanunda ayrıca düzenlenmiştir',
            'B': 'Çek görüldüğünde ödenir',
            'C': 'Çekte muhatap ancak banka olabilir',
            'D': 'Çekte muhatap herhangi bir gerçek veya tüzel kişi olabilir',
            'E': 'Çekte kabul yasaktır',
        },
        'D',
        'TTK md. 782: çek ancak bir BANKA üzerine düzenlenebilir; banka dışındaki kişiler üzerine düzenlenen belge çek sayılmaz. md. 795 çekin görüldüğünde ödeneceğini, md. 784 kabul yasağını, md. 796 ibraz sürelerini düzenler.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0049': patch(
        'Kambiyo senetlerinde sorumluluk incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bono düzenleyeni asıl borçludur',
            'B': 'Aval veren, lehine aval verdiği kişi gibi sorumludur',
            'C': 'Hamil, borçlulara borç altına girişlerindeki sıraya uygun biçimde başvurur',
            'D': 'Düzenleyen, kabul eden, ciranta ve aval veren müteselsilen sorumludur',
            'E': 'Hamil borçlulardan birine, birkaçına veya hepsine başvurabilir',
        },
        'C',
        'TTK md. 724: hamil, bu kişilerden birine, birkaçına veya hepsine, borç altına girişlerindeki SIRAYA BAĞLI KALMAKSIZIN başvurabilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0050': patch(
        'Kambiyo senetlerinde mücerretlik ilkesi incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Temel ilişkinin geçersizliği kambiyo senedini de geçersiz kılar',
            'B': "Bilerek borçlunun zararına hareket eden hamile karşı def'i ileri sürülebilir",
            'C': 'Kambiyo senedindeki borç temel ilişkiden bağımsızdır',
            'D': 'Mücerretlik senedin tedavülünü kolaylaştırır',
            'E': "Borçlu temel ilişkiye dayanan def'iyi iyiniyetli hamile karşı ileri süremez",
        },
        'A',
        'Kambiyo senetleri MÜCERRETTİR: senetteki borç temel ilişkiden bağımsızdır ve temel ilişkinin geçersizliği senedi kendiliğinden geçersiz KILMAZ (TTK md. 687).',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0051': patch(
        'Kambiyo senetlerinde ciro incelenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tahsil cirosuyla senedin mülkiyeti ciro edilene geçer',
            'B': 'Beyaz ciro cirantanın imzasıyla yapılabilir',
            'C': 'Rehin cirosu senedi teminat olarak verir',
            'D': 'Ciro senedin arkasına veya alonj üzerine yazılır',
            'E': 'Temlik cirosu mülkiyeti devreder',
        },
        'A',
        'TTK md. 688: tahsil cirosunda hamil senetten doğan hakları kullanabilir ancak MÜLKİYET GEÇMEZ; hamil yalnızca tahsil yetkisine sahiptir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0052': patch(
        'Bir hamil zamanaşımı nedeniyle kambiyo hakkını kaybetmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Düzenleyen ile kabul eden kişi, hamilin zararına sebepsiz zenginleştikleri ölçüde borçlu kalır',
            'B': 'Talep hamilin zararıyla sınırlıdır',
            'C': 'Zamanaşımının dolmasıyla hamilin bütün talep hakları sona erer',
            'D': 'Sebepsiz zenginleşme davası kanunda düzenlenmiştir',
            'E': 'Temel ilişkiye dayanan talep ayrıca değerlendirilebilir',
        },
        'C',
        'TTK md. 732: zamanaşımı nedeniyle poliçeden doğan haklar düşmüş olsa bile düzenleyen ve kabul eden, hamilin zararına SEBEPSİZ ZENGİNLEŞTİKLERİ ÖLÇÜDE borçlu kalır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0053': patch(
        'Düzenleyenin bizzat ödeme vaadini içeren ve muhatabı bulunmayan kambiyo senedi aşağıdakilerden hangisidir?',
        {
            'A': 'Bono',
            'B': 'Poliçe',
            'C': 'Konşimento',
            'D': 'Çek',
            'E': 'Varant',
        },
        'A',
        'TTK md. 776: bono, düzenleyenin kayıtsız şartsız belirli bir bedeli ödeme vaadini içerir ve iki taraflıdır; muhatap yoktur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 0
    '0054': patch(
        'Bir kambiyo senedinin ciro ve teslimle devredilmesini sağlayan özelliği aşağıdakilerden hangisidir?',
        {
            'A': 'Şekle bağlı olması',
            'B': 'Kanunen emre yazılı olması',
            'C': 'Mücerret olması',
            'D': 'Hamiline yazılı olması',
            'E': 'Nama yazılı olması',
        },
        'B',
        'TTK md. 681 ve 824: kambiyo senetleri KANUNEN EMRE YAZILIDIR; bu nedenle ayrıca emre kaydı aranmaksızın ciro ve teslimle devredilir.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0055': patch(
        "Bir çekin üzerine 'kabul edilmiştir' şerhi düşülmüştür. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Şerh geçerlidir ve banka asıl borçlu olur',
            'B': 'Şerh çeki bonoya dönüştürür',
            'C': 'Şerh çeki geçersiz kılar',
            'D': 'Çekte kabul yasak olduğundan şerh yazılmamış sayılır',
            'E': 'Kabul şerhi, muhatap bankanın ayrıca yazılı onay vermesi hâlinde geçerli olur',
        },
        'D',
        'TTK md. 784: çekte KABUL YASAKTIR; çek üzerine yazılan kabul şerhi YAZILMAMIŞ sayılır. Banka kabul yoluyla asıl borçlu hâline gelmez.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 1
    '0056': patch(
        "Bir hamil, senedi devralırken borçlunun zararına hareket ettiğini bilmektedir. Buna göre def'iler bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Borçlu, temel ilişkiye dayanan kişisel def'ilerini bu hamile karşı ileri sürebilir",
            'B': "Hamilin bilgisi def'i rejimini etkilemez",
            'C': "Borçlu, hamilin bilgisine bakılmaksızın senedin metninden anlaşılan def'ileri ileri sürebilir, diğerlerini süremez",
            'D': "Def'i ileri sürmek için ayrıca dava açılması gerekir",
            'E': "Borçlu def'i ileri süremez",
        },
        'A',
        "TTK md. 687: borçlu, önceki hamillerle arasındaki kişisel ilişkilere dayanan def'ileri, hamil senedi devralırken BİLEREK BORÇLUNUN ZARARINA HAREKET ETMİŞ olmadıkça ileri süremez; bu koşul gerçekleşince def'iler ileri sürülebilir.",
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0057': patch(
        'Kambiyo senetleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Kambiyo senetleri kanunen emre yazılıdır. II. Kambiyo senetleri mücerret senetlerdir. III. Çekte vade gösterilebilir.',
        {
            'A': 'I, II ve III',
            'B': 'I ve III',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'Yalnız I',
        },
        'C',
        'I doğrudur (TTK md. 681, 824). II doğrudur. III YANLIŞTIR: md. 795 uyarınca çek görüldüğünde ödenir; aksine kayıtlar yazılmamış sayılır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0058': patch(
        'Kambiyo senetleri ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Bonoda muhatap bulunur. II. Çekte muhatap ancak banka olabilir. III. İmzaların bağımsızlığı ilkesi geçerlidir. IV. Vadesi gösterilmeyen poliçe geçersizdir.',
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'I, III ve IV',
            'D': 'I ve IV',
            'E': 'II ve III',
        },
        'D',
        'I YANLIŞ: bonoda muhatap yoktur (TTK md. 776). IV YANLIŞ: vadesi gösterilmeyen poliçe görüldüğünde ödenecek sayılır (md. 672). II (md. 782) ve III (md. 677) doğrudur.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 2
    '0059': patch(
        'Bir kambiyo senedinde düzenlenme tarihi bulunmamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tarih eksikliği çekte sonuç doğurur, diğer senetlerde doğurmaz',
            'B': 'Düzenlenme tarihi zorunlu unsurdur; senet o tür kambiyo senedi sayılmaz',
            'C': 'Tarih eksikliği senedi etkilemez',
            'D': 'Düzenlenme tarihindeki eksikliği hamil, borçlunun onayı aranmaksızın dilediği zaman doldurabilir',
            'E': 'Tarih muhatabın beyanına göre belirlenir',
        },
        'B',
        'TTK md. 671, 776 ve 780: DÜZENLENME TARİHİ poliçe, bono ve çekin zorunlu unsurlarındandır ve kanunen tamamlanamaz; yokluğu senedi o tür kambiyo senedi olmaktan çıkarır.',
        '6102 sayili Turk Ticaret Kanunu',
    ),
    # düzey 3
    '0060': patch(
        'Kambiyo senetleri ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Kambiyo senetleri poliçe, bono ve çektir. II. Aval veren, lehine aval verilenin borcu şekil noksanı dışında geçersiz olsa da sorumludur. III. Tahsil cirosu mülkiyeti devreder. IV. Çekte kabul mümkündür.',
        {
            'A': 'II ve III',
            'B': 'Yalnız III',
            'C': 'III ve IV',
            'D': 'I, III ve IV',
            'E': 'I ve II',
        },
        'C',
        'III YANLIŞ: tahsil cirosu mülkiyeti devretmez (TTK md. 688). IV YANLIŞ: md. 784 uyarınca çekte KABUL YASAKTIR. I (md. 670 vd.) ve II (md. 702) doğrudur.',
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
    print(f"1 paket / {len(PATCHES)} soru ('Kambiyo Senetleri' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
