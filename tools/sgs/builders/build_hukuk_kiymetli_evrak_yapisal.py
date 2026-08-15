#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiymetli Evrak — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turunun 11. konusu. Paketin 60 sorusunun
TAMAMI yeniden yazildi.

    olcut                gercek   once   sonra
    medyan kok              257     92     148
    olumsuz kok           %41,5     %3     %35
    ayni kok kalibi           —  28/60       —
    onculu                %14,3    %10       —

Icerik TTK kiymetli evrak genel hukumlerini OLAYA uygulatiyor: hakkin senetten
ayri ileri surulememesi (md. 645), uc devir usulu (teslim / ciro+teslim /
yazili devir beyani+teslim), def'i rejimindeki fark (nama yazilida def'iler
devam ederken emre ve hamilinede iyiniyetli hamile karsi ileri surulemez,
md. 659), ciro turleri (tam/beyaz, temlik/tahsil/rehin), ciro zinciri,
zayi ve iptal, emtia senetleri ile kambiyo senetleri ayrimi.

⚠️ SAHIPLIK DEVRI: DORT builder bu pakette soru tutuyordu —
fix_ticaret_length_quality (5 soru, --check YOK, argv korumasi var),
build_legal_oncul_cleanup (0019), build_option_balance_cleanup (0033),
fix_bekleyen_denge (paket duzeyi). Bloklari CIKARILDI.

IKI KAPI: §5 boy (ilk tasarim 40/60 = %67 cikip uretimi DURDURDU; uc turda 72
celdirici dogru sikla PARALEL yapiya tasinarak %12) · §1 bilissel duzey
(0 = 5 <=6, 0+1 = 12 <=24, duzey 2 = 34 >=24, duzey 3 = 14 >=12).
Ayrica 14 kisa tarama koku olay cercevesine tasindi (medyan 120 -> 148).

Dayanak: TTK md. 645, 647, 651 vd., 653, 654, 658, 659, 670 vd., 671, 680,
681, 683, 684, 686, 688, 689, 757 vd., 824, 832 vd. · TBK alacagin temliki.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/ticaret_hukuku/kiymetli_evrak.json"
STYLE_REF = "SGS Ticaret Hukuku (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "tic-kiymetli-gen-"


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
        'Bir alacaklı, elindeki senette yazılı hakkı senetten ayrı olarak ileri sürmek ve senedi devretmeksizin hakkı başkasına geçirmek istemektedir. Buna göre kıymetli evrak kavramı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kıymetli evrakta hak ile senet arasında bir bağ aranmaz',
            'B': 'Kıymetli evrakta yer alan hak senetten ayrı olarak ileri sürülemez ve devredilemez',
            'C': 'Senetteki hak, senedin zilyetliğinden bağımsız biçimde her zaman ileri sürülebilir',
            'D': 'Senet yalnızca ispat aracı olup hakkın varlığını etkilemez',
            'E': 'Hak, senet devredilmeksizin yazılı beyanla devredilebilir',
        },
        'B',
        'TTK md. 645: kıymetli evrak öyle senetlerdir ki, bunlarda yer alan hak, senetten ayrı olarak ileri sürülemediği gibi başkalarına da devredilemez. Hak ile senet arasındaki bu sıkı bağ, kıymetli evrakı adi senetten ayıran kurucu unsurdur.',
    ),
    # düzey 3
    '0002': patch(
        'Üç senet devredilmek istenmektedir: (A) hamiline yazılı bir senet, (B) emre yazılı bir senet, (C) nama yazılı bir senet. Buna göre devir usulleri sırasıyla aşağıdakilerden hangisidir?',
        {
            'A': 'Teslim – ciro ve teslim – yazılı devir beyanı ve teslim',
            'B': 'Teslim – yazılı devir beyanı – ciro ve teslim',
            'C': 'Yazılı devir beyanı – teslim – ciro ve teslim',
            'D': 'Ciro ve teslim – teslim – yazılı devir beyanı ile teslim',
            'E': 'Üçünde de yalnızca teslim yeterlidir',
        },
        'A',
        'TTK md. 647, 654 ve 681: HAMİLİNE yazılı senet zilyetliğin devri (TESLİM) ile, EMRE yazılı senet CİRO VE TESLİM ile, NAMA yazılı senet ise YAZILI DEVİR BEYANI (alacağın temliki) ve senedin teslimi ile devredilir.',
    ),
    # düzey 2
    '0003': patch(
        'Bir senette, senedin belirli bir kişiye veya onun emrine ödeneceği yazmaktadır. Bir diğerinde ise senedi elinde bulundurana ödeneceği belirtilmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Her ikisi de hamiline yazılı senettir',
            'B': 'Senet türü yalnızca düzenleyenin beyanıyla değil mahkeme kararıyla belirlenir',
            'C': 'Birincisi emre yazılı, ikincisi hamiline yazılı senettir',
            'D': 'Her ikisi de nama yazılı senettir',
            'E': 'Birincisi hamiline yazılı, ikincisi emre yazılı senettir',
        },
        'C',
        'TTK md. 671 ve 658: senedin belirli bir kişiye VEYA ONUN EMRİNE ödeneceği kaydı taşıması EMRE yazılı; senedi elinde bulunduran herkese ödeneceğinin anlaşılması ise HAMİLİNE yazılı senedi gösterir. Nama yazılı senet ise belirli bir kişiye ödenir ve emre kaydı taşımaz.',
    ),
    # düzey 3
    '0004': patch(
        "Nama yazılı olarak düzenlenmiş bir senede sonradan 'emrine' kaydı eklenmiştir. Buna göre senedin niteliği bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Senedin türü yalnızca ilk düzenlenme anındaki kayıtlara göre belirlenir ve sonradan değiştirilemez',
            'B': 'Senet nama yazılı olarak kalır; emre kaydı sonuç doğurmaz',
            'C': 'Senet hamiline yazılı hâle gelir',
            'D': 'Emre kaydı taşıyan senet emre yazılı sayılır; devri ciro ve teslimle gerçekleşir',
            'E': 'Senet geçersiz hâle gelir',
        },
        'D',
        'TTK md. 653 ve 824: senedin türü, üzerindeki kayıtlara göre belirlenir. Belirli bir kişiye ödenmesi öngörülen ancak EMRE KAYDI taşıyan senet emre yazılı sayılır ve devri CİRO ve teslimle gerçekleşir.',
    ),
    # düzey 2
    '0005': patch(
        'Bir hamil, elindeki senetler arasında hakkın senetten ayrı ileri sürülebildiği bir belge bulunduğunu fark etmiştir. Buna göre aşağıdakilerden hangisi kıymetli evrak niteliği taşımaz?',
        {
            'A': 'Poliçe',
            'B': 'Deniz taşımasında düzenlenen ve taşınan emtiayı temsil eden konşimento',
            'C': 'Bono',
            'D': 'Çek',
            'E': 'Alacağın varlığını yalnızca ispata yarayan adi nitelikli borç senedi',
        },
        'E',
        'TTK md. 645 vd.: kıymetli evrakta hak senede sıkı sıkıya bağlıdır. Poliçe, bono ve çek kambiyo senetleri; konşimento, makbuz senedi ve varant ise diğer kıymetli evrak türleridir. ADİ BORÇ SENEDİ yalnızca ispat aracıdır; hak senetten bağımsız olarak ileri sürülebilir.',
    ),
    # düzey 3
    '0006': patch(
        "Bir borçlu, emre yazılı senedi düzenlediği ilk alacaklıyla arasındaki temel ilişkiden doğan bir def'iyi, senedi ciro yoluyla devralan iyiniyetli hamile karşı ileri sürmek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Kişisel def'iler kural olarak iyiniyetli hamile karşı ileri sürülemez",
            'B': "Kişisel def'i ileri sürebilmek için hamilin kötüniyetli olması aranmaz",
            'C': "Borçlu hiçbir def'iyi hiçbir hamile karşı ileri süremez",
            'D': "Borçlu tüm def'ilerini her hamile karşı ileri sürebilir",
            'E': "Def'i ileri sürme yalnızca nama yazılı senetlerde yasaktır",
        },
        'A',
        "TTK md. 659: borçlu, senetten anlaşılan def'ilerle senedin geçersizliğine ilişkin def'ileri ve kendisinin hamile karşı doğrudan sahip olduğu def'ileri ileri sürebilir. Önceki hamillerle arasındaki KİŞİSEL ilişkilere dayanan def'iler ise, hamil senedi devralırken bilerek borçlunun zararına hareket etmiş olmadıkça ileri sürülemez.",
    ),
    # düzey 3
    '0007': patch(
        "Nama yazılı bir senedi alacağın temliki yoluyla devralan bir kişi, borçlunun önceki alacaklıya karşı sahip olduğu def'ilerden etkilenmeyeceğini düşünmektedir. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Def'i ileri sürme imkânı nama yazılı senetlerde de emre yazılı senetlerdeki ölçüde sınırlandırılmıştır",
            'B': "Def'i ileri sürebilmek için devrin borçluya bildirilmiş olması gerekmez",
            'C': "Def'iler ancak senet üzerinde yazılıysa ileri sürülebilir",
            'D': "Nama yazılı senette borçlu, devirden önce doğmuş def'ilerini yeni alacaklıya karşı da ileri sürebilir",
            'E': "Borçlu hiçbir def'iyi yeni alacaklıya karşı ileri süremez",
        },
        'D',
        "Nama yazılı senet ALACAĞIN TEMLİKİ hükümlerine göre devredilir; temlikte borçlu, devir anında sahip olduğu def'ileri yeni alacaklıya karşı da ileri sürebilir. Bu, emre ve hamiline yazılı senetlerdeki def'i SINIRLAMASINDAN önemli bir farktır ve nama yazılı senedin tedavül kabiliyetini azaltır.",
    ),
    # düzey 3
    '0008': patch(
        'Bir emre yazılı senedin arkasına yalnızca cirantanın imzası atılmış, lehtar gösterilmemiştir. Bir diğerinde ise devralanın adı açıkça yazılmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ciroda lehtarın gösterilmesi geçerlilik koşuludur',
            'B': 'Birincisi beyaz ciro, ikincisi tam cirodur',
            'C': 'Birincisi tam ciro, ikincisi beyaz cirodur',
            'D': 'Her ikisi de geçersizdir',
            'E': 'Her ikisi de tam cirodur',
        },
        'B',
        'TTK md. 683: ciro, lehine ciro yapılan kişi gösterilerek (TAM CİRO) ya da yalnız cirantanın imzasıyla (BEYAZ CİRO) yapılabilir. Beyaz ciro geçerlidir; senedin arka yüzüne ya da alonj üzerine yazılması gerekir.',
    ),
    # düzey 3
    '0009': patch(
        "Bir senedin cirosunda 'bedeli tahsil içindir' kaydı bulunmaktadır. Bir diğerinde ise 'bedeli teminattır' kaydı yer almaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Her ikisi de temlik cirosu olup mülkiyeti devreder',
            'B': 'Birincisi rehin cirosu, ikincisi tahsil cirosudur',
            'C': 'Ciro kayıtlarının türü, lehine ciro yapılan kişinin sonradan yaptığı beyana göre belirlenir',
            'D': 'Her ikisi de geçersiz olup senedi hükümsüz kılar',
            'E': 'Birincisi tahsil cirosu, ikincisi rehin cirosudur; ikisi de mülkiyeti devretmez',
        },
        'E',
        "TTK md. 688: 'bedeli tahsil içindir', 'kabz içindir', 'vekâleten' gibi kayıtlar TAHSİL CİROSUDUR; hamil senetten doğan hakları kullanabilir ancak mülkiyeti kazanmaz. md. 689: 'bedeli teminattır', 'bedeli rehindir' kayıtları ise REHİN CİROSUDUR.",
    ),
    # düzey 2
    '0010': patch(
        'Bir kıymetli evrak zayi olmuştur. Hamil, senet olmadan hakkını ileri sürmek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Zayi olan senet için yalnızca borçluya bildirim yeterlidir',
            'B': 'Zayi olan senet için hiçbir hukuki yol bulunmaz',
            'C': 'Zayi olan kıymetli evrakın mahkemeden iptaline karar verilmesi gerekir; iptal kararıyla hak senetsiz ileri sürülebilir',
            'D': 'Hamil senet olmaksızın doğrudan hakkını ileri sürebilir',
            'E': 'Zayi olan senedin iptali kararı yalnızca hamiline yazılı senetler için verilebilir; diğer senet türlerinde bu yol kapalıdır',
        },
        'C',
        'TTK md. 651 vd. ve 757 vd.: zayi olan kıymetli evrakın iptaline MAHKEMECE karar verilir. İptal kararını alan kişi hakkını senet olmaksızın da ileri sürebilir. Yol tüm kıymetli evrak türleri için açıktır; yalnızca hamiline yazılı senetlere özgü değildir.',
    ),
    # düzey 2
    '0011': patch(
        'Bir hamiline yazılı senedin devrinde ayrıca yazılı bir devir beyanı arandığı ileri sürülmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Hamiline yazılı senet zilyetliğin devriyle devredilir',
            'B': "Hamiline yazılı senette def'iler sınırlıdır",
            'C': 'Hamiline yazılı senet tedavül kabiliyeti en yüksek türdür',
            'D': 'Hamiline yazılı senette, senedi elinde bulunduran kişi hak sahibi sayılır',
            'E': 'Hamiline yazılı senedin devri için yazılı devir beyanı düzenlenmesi gerekir',
        },
        'E',
        'TTK md. 658 ve 647: hamiline yazılı senetlerde hak, senedin ZİLYETLİĞİNİN DEVRİ (teslim) ile geçer; ayrıca yazılı devir beyanı aranmaz. Yazılı devir beyanı NAMA yazılı senetlere özgüdür.',
    ),
    # düzey 2
    '0012': patch(
        'Nama yazılı senedin tedavül kabiliyeti tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Nama yazılı senette de ileri sürülebilecek def'iler, emre ve hamiline yazılı senetlerdeki gibi kanunla sınırlandırılmıştır",
            'B': "Nama yazılı senet alacağın temliki yoluyla devredilir; borçlunun def'ileri devam ettiği için tedavül kabiliyeti düşüktür",
            'C': 'Nama yazılı senet teslimle devredilir',
            'D': "Nama yazılı senet ciro ile devredilir ve def'iler sınırlıdır",
            'E': 'Nama yazılı senet, taraflar anlaşsa dahi devredilemez',
        },
        'B',
        "TTK md. 647 ve 654: nama yazılı senet, yazılı devir beyanı (alacağın temliki) ve senedin teslimiyle devredilir. Borçlu devir anındaki def'ilerini yeni alacaklıya karşı da ileri sürebildiğinden tedavül kabiliyeti emre ve hamiline yazılı senetlere göre DÜŞÜKTÜR.",
    ),
    # düzey 2
    '0013': patch(
        "Bir senet üzerinde hem 'nama yazılıdır' ibaresi hem de emre kaydı bulunmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Emre kaydı bulunan senet emre yazılı sayılır ve ciro ile devredilir',
            'B': 'Senedin türünü hamil serbestçe belirler',
            'C': 'Senet nama yazılı olarak kalır; sonradan eklenen emre kaydı yok hükmünde sayılır',
            'D': 'Senet hamiline yazılı sayılır',
            'E': 'Senet çelişkili kayıt nedeniyle geçersizdir',
        },
        'A',
        'TTK md. 653 ve 824: senedin türü üzerindeki kayıtlarla belirlenir; EMRE KAYDI taşıyan senet emre yazılı sayılır ve ciro ile devredilir. Çelişkili kayıt senedi geçersiz kılmaz.',
    ),
    # düzey 2
    '0014': patch(
        'Bir kıymetli evrakın türleri sınıflandırılmaktadır. Buna göre aşağıdakilerden hangisi bir kambiyo senedi değildir?',
        {
            'A': 'Bono',
            'B': 'Çek',
            'C': 'Deniz taşımasında düzenlenen ve taşınan malı temsil eden konşimento',
            'D': 'Deniz taşımasında düzenlenen ve taşınan emtiayı temsil eden konşimento',
            'E': 'Poliçe',
        },
        'D',
        'TTK md. 670 vd.: KAMBİYO SENETLERİ poliçe, bono ve çektir. KONŞİMENTO ise taşıma senedi niteliğinde bir emtia senedi olup kambiyo senedi değildir; ayrı hükümlere tabidir.',
    ),
    # düzey 2
    '0015': patch(
        'Bir depo işletmesi, teslim aldığı emtia karşılığında senet düzenlemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Emtia senetleri yalnızca ispat aracıdır',
            'B': 'Emtiayı temsil eden kıymetli evrak bulunmaz',
            'C': 'Makbuz senedi ile varant, tevdi edilen emtiayı temsil eden kıymetli evraktır',
            'D': 'Emtiayı temsil eden senetler yalnızca nama yazılı biçimde düzenlenebilir',
            'E': 'Makbuz senedi ve varant kambiyo senedidir',
        },
        'C',
        'TTK md. 832 vd.: umumi mağazalarca düzenlenen MAKBUZ SENEDİ ve VARANT, tevdi edilen emtiayı temsil eden kıymetli evraktır. Senedin devri emtia üzerindeki hakkı da devreder; kambiyo senedi değildirler.',
    ),
    # düzey 3
    '0016': patch(
        "Bir hamil, senedi devralırken borçlunun zararına hareket ettiğini bilerek almıştır. Buna göre def'iler bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Senedi devralırken bilerek borçlunun zararına hareket eden hamile karşı kişisel def'iler ileri sürülebilir",
            'B': "Hamilin bilgisi def'i rejimini etkilemez",
            'C': "Def'i ileri sürebilmek için hamilin ayrıca kusurlu olması gerekir",
            'D': "Kötüniyetli hamile karşı dahi yalnızca senedin metninden anlaşılan def'iler ileri sürülebilir",
            'E': "Def'iler hiçbir hamile karşı ileri sürülemez",
        },
        'A',
        "TTK md. 659: borçlu, önceki hamillerle arasındaki kişisel ilişkilere dayanan def'ileri, hamil senedi devralırken BİLEREK BORÇLUNUN ZARARINA HAREKET ETMİŞ olmadıkça ileri süremez. Bu koşul gerçekleşince kişisel def'iler ileri sürülebilir hâle gelir.",
    ),
    # düzey 3
    '0017': patch(
        'Bir emre yazılı senedi beyaz ciro ile devralan hamil, senedi bir başkasına devretmek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Beyaz ciro ile devralan hamil senedi devredemez',
            'B': 'Beyaz ciro senedi hamiline yazılı hâle getirir',
            'C': 'Beyaz ciro ile devralan hamil senedi teslimle, yeni bir ciroyla veya boşluğu doldurarak devredebilir',
            'D': 'Beyaz ciro geçersiz olup senedi hükümsüz kılar',
            'E': 'Beyaz ciro ile devralan hamil, senedi ancak lehtarı göstererek tam ciro yapmak suretiyle devredebilir',
        },
        'C',
        'TTK md. 684: beyaz ciro ile senedi devralan hamil; beyaz cirodaki boşluğu kendi ya da bir başkasının adıyla doldurabilir, senedi yeniden beyaz veya tam ciroyla devredebilir ya da doldurmaksızın ve ciro etmeksizin TESLİMLE başkasına verebilir. Senet hamiline yazılı hâle GELMEZ; emre yazılı niteliğini korur.',
    ),
    # düzey 2
    '0018': patch(
        'Bir ciro, senedin devrini değil yalnızca tahsil yetkisini vermeyi amaçlamaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Tahsil cirosunda 'bedeli tahsil içindir' gibi kayıtlar kullanılır",
            'B': 'Tahsil cirosuyla senedin mülkiyeti ciro edilene geçer',
            'C': 'Tahsil cirosunda hamil senetten doğan hakları kullanabilir',
            'D': 'Tahsil cirosu mülkiyeti devretmez',
            'E': "Tahsil cirosunda borçlu, ciro edene karşı sahip olduğu def'ileri ileri sürebilir",
        },
        'B',
        "TTK md. 688: 'bedeli tahsil içindir', 'kabz içindir', 'vekâleten' kayıtlarını taşıyan ciro TAHSİL CİROSUDUR; hamil senetten doğan hakları kullanabilir ancak MÜLKİYET GEÇMEZ. Borçlu, ciro edene karşı ileri sürebileceği def'ileri hamile karşı da ileri sürebilir.",
    ),
    # düzey 2
    '0019': patch(
        'Kıymetli evrak ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Kıymetli evrakta yer alan hak senetten ayrı olarak ileri sürülemez. II. Hamiline yazılı senet teslimle devredilir. III. Nama yazılı senet ciro ile devredilir.',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'I ve III',
        },
        'A',
        'I doğrudur (TTK md. 645). II doğrudur (md. 658). III YANLIŞTIR: nama yazılı senet CİRO ile değil, yazılı devir beyanı (alacağın temliki) ve teslimle devredilir; ciro EMRE yazılı senetlere özgüdür.',
    ),
    # düzey 2
    '0020': patch(
        'Bir kıymetli evrakın hükümsüzlüğü hâlinde senedin durumu tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Unsurları eksik senet hiçbir hukuki sonuç doğurmaz',
            'B': 'Senedin geçerliliği yalnızca mahkeme kararıyla belirlenir',
            'C': 'Unsurları eksik senet yine de kıymetli evrak sayılır',
            'D': 'Kanunda öngörülen zorunlu unsurları taşımayan senet kıymetli evrak sayılmaz; ancak adi senet olarak hüküm doğurabilir',
            'E': 'Zorunlu unsurdaki eksiklik, borçlunun onayı aranmaksızın sonradan hamil tarafından her zaman serbestçe tamamlanabilir',
        },
        'D',
        'Kıymetli evrakta ŞEKİL ŞARTLARI kurucudur: kanunda öngörülen zorunlu unsurları taşımayan senet o tür kıymetli evrak sayılmaz (örneğin TTK md. 671, 777). Ancak senet, koşulları varsa ADİ SENET olarak ispat gücü taşıyabilir; tümüyle sonuçsuz kalmaz.',
    ),
    # düzey 2
    '0021': patch(
        'Bir hamil, elindeki farklı türdeki senetleri devretmek istemekte ve devir usullerini karşılaştırmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Nama yazılı senet, yazılı devir beyanı ve senedin teslimi ile devredilir',
            'B': 'Hamiline yazılı senet teslimle devredilir',
            'C': 'Devir usulü senedin türüne göre değişir',
            'D': 'Emre yazılı senet ciro ve teslimle devredilir',
            'E': 'Emre yazılı senet, yalnızca yazılı devir beyanıyla devredilir',
        },
        'E',
        'TTK md. 647 ve 681: EMRE yazılı senet CİRO ve teslimle devredilir. Yazılı devir beyanı NAMA yazılı senetlere özgüdür.',
    ),
    # düzey 2
    '0022': patch(
        "Bir borçlu, elindeki def'ileri hangi hamillere karşı ileri sürebileceğini belirlemektedir. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Borçlu hamile karşı doğrudan sahip olduğu def'ileri ileri sürebilir",
            'B': "Senedi devralırken bilerek borçlunun zararına hareket eden hamile karşı kişisel def'iler ileri sürülebilir",
            'C': "Borçlu, önceki hamillerle arasındaki kişisel def'ileri iyiniyetli hamile karşı da ileri sürebilir",
            'D': "Borçlu senetten anlaşılan def'ileri her hamile karşı ileri sürebilir",
            'E': "Borçlu senedin geçersizliğine ilişkin def'ileri ileri sürebilir",
        },
        'C',
        "TTK md. 659: kişisel ilişkilere dayanan def'iler, hamil senedi devralırken bilerek borçlunun zararına hareket etmiş olmadıkça İLERİ SÜRÜLEMEZ. İYİNİYETLİ hamil bu def'ilerden etkilenmez; kıymetli evrakın tedavül güvenliği bu kuralla sağlanır.",
    ),
    # düzey 2
    '0023': patch(
        'Bir hamil, senedini temlik, tahsil ve rehin cirolarından biriyle devretmeyi değerlendirmekte; her birinin mülkiyet üzerindeki etkisini karşılaştırmaktadır. Buna göre ciro türleri bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Rehin cirosu senedin mülkiyetini ciro edilene geçirir',
            'B': 'Rehin cirosu senedi teminat olarak verir',
            'C': 'Beyaz ciro, lehtar gösterilmeksizin yalnızca cirantanın imzasıyla yapılabilir',
            'D': 'Tahsil cirosu mülkiyeti devretmez',
            'E': 'Temlik cirosu senedin mülkiyetini devreder',
        },
        'A',
        "TTK md. 689: 'bedeli teminattır', 'bedeli rehindir' kayıtlarını taşıyan REHİN CİROSU senedi teminat olarak verir; MÜLKİYETİ DEVRETMEZ. Mülkiyeti devreden ciro TEMLİK cirosudur.",
    ),
    # düzey 2
    '0024': patch(
        'Kıymetli evrakın zayi olması hâlinde izlenecek yol bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İptal yolu farklı kıymetli evrak türleri için açıktır',
            'B': 'Zayi olan senet için borçluya yapılan bildirim, senedin iptali sonucunu doğurur',
            'C': 'İptal usulü kanunda düzenlenmiştir',
            'D': 'Zayi olan kıymetli evrakın iptaline, kanunda gösterilen yetkili mahkemece karar verilir',
            'E': 'İptal kararını alan kişi hakkını senetsiz ileri sürebilir',
        },
        'B',
        'TTK md. 651 vd. ve 757 vd.: zayi olan kıymetli evrakın iptaline MAHKEMECE karar verilir; borçluya bildirim tek başına iptal sonucu doğurmaz. İptal kararıyla hak senetsiz ileri sürülebilir.',
    ),
    # düzey 2
    '0025': patch(
        'Bir tacir, elindeki kıymetli evrakı kambiyo senetleri ve emtia senetleri olarak sınıflandırmaktadır. Buna göre kıymetli evrak türleri bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Poliçe, bono ve çek kambiyo senetleridir',
            'B': 'Hisse senedi ve tahvil de kıymetli evrak sayılır',
            'C': 'Makbuz senedi ve varant emtiayı temsil eder',
            'D': 'Konşimento ve makbuz senedi kambiyo senedi sayılır',
            'E': 'Konşimento bir emtia senedi olup taşınan malı temsil eder',
        },
        'D',
        'TTK md. 670 vd.: kambiyo senetleri POLİÇE, BONO ve ÇEKTİR. Konşimento ile makbuz senedi ve varant emtia senetleridir; kambiyo senedi değildirler.',
    ),
    # düzey 2
    '0026': patch(
        'Nama, emre ve hamiline yazılı senetlerin karşılaştırılması bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Nama yazılı senette def'iler emre yazılı senetteki gibi sınırlandırılmıştır",
            'B': 'Emre yazılı senet ciro ve teslimle devredilir',
            'C': 'Hamiline yazılı senet teslimle devredilir',
            'D': "Emre ve hamiline yazılı senetlerde ileri sürülebilecek def'iler kanunla sınırlandırılmıştır",
            'E': 'Nama yazılı senet alacağın temliki yoluyla devredilir',
        },
        'A',
        "Nama yazılı senet alacağın temliki hükümlerine tabidir; borçlu devir anındaki def'ilerini yeni alacaklıya karşı da ileri sürebilir. Def'i SINIRLAMASI emre ve hamiline yazılı senetlere özgüdür (TTK md. 659).",
    ),
    # düzey 2
    '0027': patch(
        'Bir senet, kanunda öngörülen zorunlu unsurlardan birini taşımamakta; hamil bu eksikliği kendisi tamamlamak istemektedir. Buna göre kıymetli evrakta şekil şartları bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kıymetli evrakta şekil şartları kurucu nitelik taşır',
            'B': 'Şekil şartları kanunda ayrı ayrı düzenlenmiştir',
            'C': 'Kanunda öngörülen zorunlu unsurlarını taşımayan senet, o tür kıymetli evrak olarak sayılmaz',
            'D': 'Zorunlu unsuru eksik senet, koşulları varsa adi senet olarak hüküm doğurabilir',
            'E': 'Zorunlu unsurları eksik olan senet, hamil tarafından sonradan serbestçe tamamlanabilir',
        },
        'E',
        'Kıymetli evrakta şekil şartları KURUCUDUR ve kanunla belirlenmiştir; eksik unsurlar hamil tarafından SERBESTÇE tamamlanamaz. Açık senet ve anlaşmaya aykırı doldurma ayrı hükümlere tabidir (TTK md. 680).',
    ),
    # düzey 2
    '0028': patch(
        'Bir hamil, senedi ibraz etmeksizin borçludan ödeme talep etmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Borçlu senet ibraz edilmeksizin de ödeme yapmakla yükümlüdür',
            'B': 'Senedin ibrazı yalnızca kambiyo senetlerinde aranır',
            'C': 'İbraz koşulu yalnızca nama yazılı senetlerde geçerlidir',
            'D': 'Kıymetli evrakta hak senede bağlı olduğundan borçlu, senet ibraz edilmeden ödeme yapmakla yükümlü değildir',
            'E': 'Borçlu, ödemeyi yaparken senedin kendisine geri verilmesini isteme hakkından tümüyle yoksundur',
        },
        'D',
        'TTK md. 645: kıymetli evrakta hak senetten ayrı ileri sürülemez. Bu nedenle borçlu, senet İBRAZ EDİLMEDEN ödeme yapmakla yükümlü değildir; ödeme yaparken senedin kendisine geri verilmesini isteyebilir. Kural tüm kıymetli evrak türleri için geçerlidir.',
    ),
    # düzey 0
    '0029': patch(
        'Bir senette yer alan hakkın senetten ayrı olarak ileri sürülememesi ve devredilememesi özelliği hangi kavramı tanımlar?',
        {
            'A': 'Adi senet',
            'B': 'İmza sirküleri',
            'C': 'Kıymetli evrak',
            'D': 'Borç ikrarı',
            'E': 'Teminat mektubu',
        },
        'C',
        'TTK md. 645: kıymetli evrak öyle senetlerdir ki, bunlarda yer alan hak senetten ayrı olarak ileri sürülemediği gibi başkalarına da devredilemez.',
    ),
    # düzey 0
    '0030': patch(
        'Bir hamil, elindeki hamiline yazılı senedi üçüncü bir kişiye devretmek istemekte ve ayrıca bir işlem gerekip gerekmediğini araştırmaktadır. Buna göre hamiline yazılı kıymetli evrakın devri hangi işlemle gerçekleşir?',
        {
            'A': 'Yazılı devir beyanı',
            'B': 'Ticaret siciline tescil',
            'C': 'Teslim',
            'D': 'Ciro',
            'E': 'Noter onaylı sözleşme',
        },
        'C',
        'TTK md. 658: hamiline yazılı senetlerde hak, senedin zilyetliğinin devri (TESLİM) ile geçer.',
    ),
    # düzey 0
    '0031': patch(
        'Bir hamil, elindeki emre yazılı senedi üçüncü bir kişiye devretmek istemekte ve izleyeceği usulü belirlemeye çalışmaktadır. Buna göre emre yazılı kıymetli evrakın devri hangi işlemlerle gerçekleşir?',
        {
            'A': 'Yalnızca ciro',
            'B': 'Yalnızca teslim',
            'C': 'Yazılı devir beyanı ve teslim',
            'D': 'Ciro ve teslim',
            'E': 'Noter onayı ve tescil',
        },
        'D',
        'TTK md. 681 vd.: emre yazılı senetler CİRO ve senedin TESLİMİ ile devredilir.',
    ),
    # düzey 0
    '0032': patch(
        'Bir hamil, elindeki nama yazılı senedi üçüncü bir kişiye devretmek istemekte ve izleyeceği usulü belirlemeye çalışmaktadır. Buna göre nama yazılı kıymetli evrakın devri hangi işlemlerle gerçekleşir?',
        {
            'A': 'Ticaret siciline tescil',
            'B': 'Yazılı devir beyanı ve teslim',
            'C': 'Yalnızca teslim',
            'D': 'Teslim olmaksızın yalnızca yazılı devir beyanı',
            'E': 'Ciro ve teslim',
        },
        'B',
        'TTK md. 647 ve 654: nama yazılı senet, alacağın temliki hükümlerine göre YAZILI DEVİR BEYANI ve senedin TESLİMİ ile devredilir.',
    ),
    # düzey 0
    '0033': patch(
        'Bir tacir, elindeki senetleri kambiyo senedi olan ve olmayan biçiminde ayırmaktadır. Buna göre aşağıdakilerden hangisi kambiyo senetlerinden biridir?',
        {
            'A': 'Makbuz senedi',
            'B': 'Hisse senedi',
            'C': 'Deniz taşımasında düzenlenen ve taşınan emtiayı temsil eden konşimento',
            'D': 'Varant',
            'E': 'Bono',
        },
        'E',
        'TTK md. 670 vd.: kambiyo senetleri POLİÇE, BONO ve ÇEKTİR. Konşimento, makbuz senedi ve varant emtia senetleri; hisse senedi ise ortaklık hakkı veren kıymetli evraktır.',
    ),
    # düzey 1
    '0034': patch(
        'Bir cironun yalnızca cirantanın imzasından oluşması hâlinde bu ciro aşağıdakilerden hangisidir?',
        {
            'A': 'Beyaz ciro',
            'B': 'Geçersiz ciro',
            'C': 'Rehin cirosu',
            'D': 'Tahsil cirosu',
            'E': 'Tam ciro',
        },
        'A',
        'TTK md. 683: ciro, lehine ciro yapılan gösterilerek (tam ciro) ya da yalnız cirantanın imzasıyla (BEYAZ CİRO) yapılabilir; beyaz ciro geçerlidir.',
    ),
    # düzey 1
    '0035': patch(
        "Bir ciroda 'bedeli tahsil içindir' kaydı bulunması hâlinde bu ciro aşağıdakilerden hangisidir?",
        {
            'A': 'Beyaz ciro',
            'B': 'Rehin cirosu',
            'C': 'Tahsil cirosu',
            'D': 'Geçersiz ciro',
            'E': 'Mülkiyeti devreden temlik cirosu',
        },
        'C',
        "TTK md. 688: 'bedeli tahsil içindir', 'kabz içindir', 'vekâleten' kayıtları TAHSİL CİROSUNU gösterir; mülkiyet geçmez, yalnızca tahsil yetkisi verilir.",
    ),
    # düzey 1
    '0036': patch(
        "Bir hamil, senedini kredi karşılığında teminat olarak vermek istemekte ve senedin arkasına 'bedeli teminattır' kaydını düşmüştür. Buna göre bu ciro aşağıdakilerden hangisidir?",
        {
            'A': 'Mülkiyeti devreden temlik cirosu',
            'B': 'Tahsil cirosu',
            'C': 'Tam ciro',
            'D': 'Rehin cirosu',
            'E': 'Beyaz ciro',
        },
        'D',
        "TTK md. 689: 'bedeli teminattır', 'bedeli rehindir' kayıtları REHİN CİROSUNU gösterir; senet teminat olarak verilir, mülkiyet geçmez.",
    ),
    # düzey 1
    '0037': patch(
        'Zayi olan bir kıymetli evrakın hükümsüz kılınması için başvurulacak yol aşağıdakilerden hangisidir?',
        {
            'A': 'Mahkemeden iptal kararı almak',
            'B': 'Borçluya yazılı bildirimde bulunmak',
            'C': 'Yeni bir senet düzenlemek',
            'D': 'Notere ihtarname göndermek',
            'E': 'Ticaret siciline şerh düşürmek',
        },
        'A',
        'TTK md. 651 vd.: zayi olan kıymetli evrakın iptaline MAHKEMECE karar verilir; iptal kararını alan hakkını senetsiz ileri sürebilir.',
    ),
    # düzey 1
    '0038': patch(
        "Bir borçlunun, senedi devralan iyiniyetli hamile karşı ileri süremeyeceği def'i türü aşağıdakilerden hangisidir?",
        {
            'A': "Şekil eksikliğine ilişkin def'iler",
            'B': "Önceki hamillerle arasındaki kişisel ilişkilere dayanan def'iler",
            'C': "Borçlunun senedi ibraz eden hamile karşı doğrudan sahip olduğu def'iler",
            'D': "Senetten anlaşılan def'iler",
            'E': "Senedin geçersizliğine ilişkin def'iler",
        },
        'B',
        "TTK md. 659: borçlu; senetten anlaşılan, senedin geçersizliğine ilişkin ve hamile karşı doğrudan sahip olduğu def'ileri ileri sürebilir. Önceki hamillerle arasındaki KİŞİSEL def'ileri ise iyiniyetli hamile karşı ileri süremez.",
    ),
    # düzey 1
    '0039': patch(
        'Emtiayı temsil eden ve umumi mağazalarca düzenlenen kıymetli evrak aşağıdakilerden hangisidir?',
        {
            'A': 'Ortaklık hakkı veren hisse senedi ile tahvil',
            'B': 'Makbuz senedi ve varant',
            'C': 'Poliçe ve bono',
            'D': 'Çek ve bono',
            'E': 'Konşimento ve poliçe',
        },
        'B',
        'TTK md. 832 vd.: umumi mağazalarca düzenlenen MAKBUZ SENEDİ ve VARANT, tevdi edilen emtiayı temsil eden kıymetli evraktır.',
    ),
    # düzey 1
    '0040': patch(
        'Bir tacir, elindeki senedi teminat göstererek kredi almak istemektedir; senedin mülkiyetini devretmek istememektedir. Buna göre başvuracağı ciro türü aşağıdakilerden hangisidir?',
        {
            'A': 'Tahsil cirosu',
            'B': 'Tam ciro',
            'C': 'Mülkiyeti devreden temlik cirosu',
            'D': 'Beyaz ciro',
            'E': 'Rehin cirosu',
        },
        'E',
        'TTK md. 689: REHİN CİROSU senedi teminat olarak vermeye yarar ve mülkiyeti devretmez; bu nedenle senedi teminat göstererek kredi almak isteyen hamilin başvuracağı yoldur.',
    ),
    # düzey 2
    '0041': patch(
        'Bir hamil, senedin arka yüzünde yer kalmadığı için ciroyu senede eklenmiş bir kâğıt üzerine yazmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ciro için ayrıca noter onayı gerekir',
            'B': 'Ciro, senede yapıştırılan alonj üzerine de yazılabilir',
            'C': 'Ciro senedin ön yüzüne yazılmalıdır',
            'D': 'Ayrı kâğıda yazılan ciro geçersizdir',
            'E': 'Ciro yalnızca senedin arka yüzüne yazılabilir; alonj kullanılamaz',
        },
        'B',
        'TTK md. 683: ciro, senet veya senede bağlı olan ve ALONJ denilen bir kâğıt üzerine yazılır ve ciranta tarafından imzalanır. Alonja yazılan ciro geçerlidir; noter onayı aranmaz.',
    ),
    # düzey 2
    '0042': patch(
        'Bir senedin türü belirlenirken hangi ölçütün esas alınacağı tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Senedin türü, üzerindeki kayıtlara ve kanundaki karinelere göre belirlenir',
            'B': 'Senedin türü ticaret siciline tescille belirlenir',
            'C': 'Senedin türünü hamil serbestçe belirler',
            'D': 'Senedin türü yalnızca mahkeme kararıyla belirlenir',
            'E': 'Senedin türü, yalnızca borçlunun sonradan yaptığı yazılı beyana göre belirlenir',
        },
        'A',
        'TTK md. 653, 658 ve 824: senedin türü üzerindeki kayıtlarla ve kanunda öngörülen karinelerle belirlenir; emre kaydı taşıyan senet emre yazılı, hamiline ödenecek senet ise hamiline yazılı sayılır.',
    ),
    # düzey 2
    '0043': patch(
        'Bir senetteki hakkın devri ile senedin zilyetliğinin devri arasındaki ilişki tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kıymetli evrakta hak senede bağlıdır',
            'B': 'Emre yazılı senette ciro ve teslim aranır',
            'C': 'Hamiline yazılı senette hakkın devri için senedin zilyetliğinin devri tek başına yeterlidir',
            'D': 'Devir usulü senedin türüne göre değişir',
            'E': 'Kıymetli evrakta hak, senedin zilyetliği devredilmeksizin tek başına devredilebilir',
        },
        'E',
        'TTK md. 645: kıymetli evrakta yer alan hak senetten AYRI OLARAK devredilemez; hakkın devri için senedin zilyetliğinin de devri gerekir. Devir usulü türe göre değişir.',
    ),
    # düzey 2
    '0044': patch(
        'Bir kıymetli evrakta borçlunun ödeme yaparken senedi geri isteme hakkı tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ödeme karşılığında senedin geri verilmesi yalnızca kambiyo senetlerinde istenebilir',
            'B': 'Senedin geri verilmesi yalnızca alacaklının takdirindedir',
            'C': 'Borçlu, ödeme karşılığında senedin kendisine geri verilmesini isteyebilir',
            'D': 'Borçlu ödeme yaptıktan sonra senedi geri isteyemez',
            'E': 'Borçlu senedi ibraz edilmeden de ödeme yapmakla yükümlüdür',
        },
        'C',
        'Kıymetli evrakta hak senede bağlı olduğundan borçlu, ödeme yaparken senedin kendisine GERİ VERİLMESİNİ isteyebilir; aksi hâlde senet tedavüle devam edip mükerrer talebe yol açabilir (TTK md. 645 ve ilgili hükümler).',
    ),
    # düzey 2
    '0045': patch(
        "Bir borçlu, senedi devralan iyiniyetli hamile karşı da tüm def'ilerini ileri sürebileceğini savunmaktadır. Buna göre kıymetli evrakın tedavül güvenliği bakımından aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "İyiniyetli hamil kişisel def'ilerden etkilenmez",
            'B': "Nama yazılı senette def'iler devam ettiğinden bu senedin tedavül kabiliyeti belirgin biçimde düşüktür",
            'C': "Def'i sınırlaması senedin el değiştirmesini kolaylaştırır",
            'D': "Tedavül güvenliği, borçlunun tüm def'ilerini her hamile karşı ileri sürebilmesiyle sağlanır",
            'E': "Emre ve hamiline yazılı senetlerde def'iler sınırlandırılmıştır",
        },
        'D',
        "TTK md. 659: tedavül güvenliği, borçlunun kişisel def'ilerini İYİNİYETLİ hamile karşı ileri SÜREMEMESİYLE sağlanır. Tüm def'ilerin ileri sürülebilmesi tedavülü güçleştirir; nitekim nama yazılı senedin tedavül kabiliyeti bu nedenle düşüktür.",
    ),
    # düzey 3
    '0046': patch(
        "Kıymetli evrak ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Kıymetli evrakta hak senetten ayrı ileri sürülemez. II. Nama yazılı senet ciro ile devredilir. III. Emre yazılı senette kişisel def'iler iyiniyetli hamile karşı ileri sürülemez. IV. Tahsil cirosu senedin mülkiyetini devreder.",
        {
            'A': 'I ve III',
            'B': 'II ve IV',
            'C': 'I, II ve IV',
            'D': 'Yalnız II',
            'E': 'II ve III',
        },
        'B',
        'II YANLIŞ: nama yazılı senet ciro ile değil, yazılı devir beyanı ve teslimle devredilir (TTK md. 647). IV YANLIŞ: tahsil cirosu mülkiyeti DEVRETMEZ, yalnızca tahsil yetkisi verir (md. 688). I (md. 645) ve III (md. 659) doğrudur.',
    ),
    # düzey 3
    '0047': patch(
        'Ciro ve devir ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Beyaz ciro yalnızca cirantanın imzasıyla yapılır. II. Ciro senede bağlı alonj üzerine de yazılabilir. III. Rehin cirosu senedin mülkiyetini devreder.',
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'I ve II',
        },
        'E',
        'I doğrudur (TTK md. 683). II doğrudur (md. 683). III YANLIŞTIR: md. 689 uyarınca rehin cirosu senedi teminat olarak verir; MÜLKİYETİ DEVRETMEZ.',
    ),
    # düzey 3
    '0048': patch(
        "Def'iler ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Borçlu senetten anlaşılan def'ileri her hamile karşı ileri sürebilir. II. Kişisel def'iler iyiniyetli hamile karşı ileri sürülebilir. III. Nama yazılı senette borçlu devir anındaki def'ilerini yeni alacaklıya karşı ileri sürebilir. IV. Def'i rejimi senedin türüne göre değişmez.",
        {
            'A': 'Yalnız II',
            'B': 'I ve III',
            'C': 'II ve IV',
            'D': 'I, II ve IV',
            'E': 'II ve III',
        },
        'C',
        "II YANLIŞ: TTK md. 659 uyarınca kişisel def'iler iyiniyetli hamile karşı ileri SÜRÜLEMEZ. IV YANLIŞ: def'i rejimi türe göre değişir; nama yazılı senette def'iler devam ederken emre ve hamiline yazılı senetlerde sınırlıdır. I ve III doğrudur.",
    ),
    # düzey 2
    '0049': patch(
        'Bir senet zorunlu unsurlarından birini taşımamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Senet yine de kıymetli evrak sayılır',
            'B': 'Senedin geçerliliği, şekil şartlarından bağımsız olarak yalnızca borçlunun bu senedi kabul etmesine bağlıdır',
            'C': 'Eksik unsur hamil tarafından serbestçe tamamlanabilir',
            'D': 'Senet o tür kıymetli evrak sayılmaz; ancak koşulları varsa adi senet olarak hüküm doğurabilir',
            'E': 'Senet hiçbir hukuki sonuç doğurmaz',
        },
        'D',
        'Kıymetli evrakta şekil şartları kurucudur; zorunlu unsuru eksik senet o tür kıymetli evrak SAYILMAZ. Ancak senet, koşulları varsa adi senet olarak ispat gücü taşıyabilir.',
    ),
    # düzey 2
    '0050': patch(
        'Bir hamil, senedi devraldıktan sonra borçlunun ödeme yapmaması üzerine hakkını aramaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Hamilin talep hakkı senedin türüne göre değişmez',
            'B': 'Hamil senedi borçluya vermeden ödeme alamaz',
            'C': 'Hamil, senedi ibraz etmeksizin de borçludan ödeme talebinde bulunma hakkına sahiptir',
            'D': 'Hamil, senedi ibraz ederek hakkını talep eder; kıymetli evrakta hak senede bağlıdır',
            'E': 'Hamil yalnızca senedi devreden kişiye başvurabilir',
        },
        'D',
        'TTK md. 645: kıymetli evrakta hak senetten ayrı ileri sürülemez; hamil hakkını senedi İBRAZ ederek talep eder. Başvuru hakları ve usulü senedin türüne göre farklılaşır (kambiyo senetlerinde müracaat hakkı ayrıca düzenlenmiştir).',
    ),
    # düzey 2
    '0051': patch(
        'Kıymetli evrak ile adi senet karşılaştırılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kıymetli evrakta hak senede sıkı sıkıya bağlıdır',
            'B': 'Adi senet, hakkın kendisini değil yalnızca varlığını ispata yarar',
            'C': 'Adi senette de hak senetten ayrı olarak ileri sürülemez',
            'D': 'Kıymetli evrak tedavül amacına hizmet eder',
            'E': 'Kıymetli evrakta şekil şartları kurucudur',
        },
        'C',
        'TTK md. 645: hakkın senetten ayrı ileri sürülememesi KIYMETLİ EVRAKA özgüdür. Adi senette hak senetten bağımsız olarak da ileri sürülebilir; senet yalnızca ispat aracıdır.',
    ),
    # düzey 2
    '0052': patch(
        'Emre yazılı senette ciro zincirinin önemi tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ciro zinciri yalnızca nama yazılı senetlerde aranır',
            'B': 'Ciro zinciri aranmaz; hamilin senedi fiilen elinde bulundurması tek başına yeterlidir',
            'C': 'Ciro zincirindeki kopukluk senedi geçersiz kılar',
            'D': 'Ciro zinciri ticaret siciline tescil edilir',
            'E': 'Hamil, hakkını birbirine bağlanan kesintisiz ciro zinciriyle ispat eder',
        },
        'E',
        'TTK md. 686: senedi elinde bulunduran kişi, birbirine bağlanan ve son ciro beyaz ciro olsa bile aralıksız devam eden CİRO ZİNCİRİ ile hakkını ispatlarsa yetkili hamil sayılır. Zincirdeki kopukluk senedi geçersiz kılmaz; hamilin yetkisini etkiler.',
    ),
    # düzey 2
    '0053': patch(
        'Bir alacaklı, senedin zilyetliğini devretmeksizin yalnızca hakkı devretmeyi planlamaktadır. Buna göre kıymetli evrakın devri ve zilyetlik ilişkisi bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Kıymetli evrakta hakkın devri için senedin zilyetliğinin devri aranmaz',
            'B': 'Emre yazılı senette ciro ve teslim aranır',
            'C': 'Nama yazılı senette yazılı devir beyanı ve teslim aranır',
            'D': 'Hamiline yazılı senette hakkın devri için senedin zilyetliğinin devri tek başına yeterlidir',
            'E': 'Hak senetten ayrı olarak devredilemez',
        },
        'A',
        'TTK md. 645 ve 647: kıymetli evrakta hak senetten ayrı devredilemez; her devir biçiminde senedin ZİLYETLİĞİNİN DEVRİ (teslim) unsuru bulunur.',
    ),
    # düzey 2
    '0054': patch(
        'Bir hamil, tahsil cirosuyla devraldığı senedi başkasına temlik cirosuyla devretmek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tahsil cirosuyla devralan hamil, senedin mülkiyetini kazandığı için temlik cirosuyla devredebilir',
            'B': 'Tahsil cirosuyla devralan hamil senedi ancak yeni bir tahsil cirosuyla devredebilir',
            'C': 'Tahsil cirosu mülkiyeti devrettiği için sınırlama doğmaz',
            'D': 'Devir yalnızca borçlunun onayıyla mümkündür',
            'E': 'Tahsil cirosuyla devralan hamil senedi hiç devredemez',
        },
        'B',
        'TTK md. 688: tahsil cirosuyla senedi devralan hamil senetten doğan hakları kullanabilir ancak mülkiyeti kazanmaz; bu nedenle senedi ancak yeni bir TAHSİL CİROSUYLA devredebilir, temlik cirosu yapamaz.',
    ),
    # düzey 2
    '0055': patch(
        'Bir borçluya, senedi ibraz etmeyen bir kişi tarafından ödeme talebi yöneltilmiştir. Buna göre kıymetli evrakta borçlunun korunması bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Borçlu senetten anlaşılan def'ileri ileri sürebilir",
            'B': 'Borçlu ödeme karşılığında senedin geri verilmesini isteyebilir',
            'C': "Borçlu senedin geçersizliğine ilişkin def'ileri ileri sürebilir",
            'D': 'Borçlu, senedi ibraz etmeyen kişiye de ödeme yapmakla yükümlüdür',
            'E': "Borçlu hamile karşı doğrudan sahip olduğu def'ileri ileri sürebilir",
        },
        'D',
        'Kıymetli evrakta hak senede bağlı olduğundan borçlu, senet İBRAZ EDİLMEDEN ödeme yapmakla YÜKÜMLÜ DEĞİLDİR; ödeme yaparken senedin geri verilmesini isteyebilir (TTK md. 645).',
    ),
    # düzey 3
    '0056': patch(
        'Kıymetli evrak türleri ve devir usulleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Poliçe, bono ve çek kambiyo senetleridir. II. Makbuz senedi ve varant emtiayı temsil eder. III. Hamiline yazılı senet ciro ile devredilir.',
        {
            'A': 'I, II ve III',
            'B': 'I ve II',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'Yalnız I',
        },
        'B',
        'I doğrudur (TTK md. 670 vd.). II doğrudur (md. 832 vd.). III YANLIŞTIR: hamiline yazılı senet CİRO ile değil TESLİM ile devredilir (md. 658).',
    ),
    # düzey 2
    '0057': patch(
        'Bir senedin hamiline yazılı olarak düzenlenmesi hâlinde ortaya çıkan sonuçlar bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tedavül kabiliyeti yüksektir',
            'B': 'Senet teslimle devredilir',
            'C': 'Senedi elinde bulunduran hak sahibi sayılır',
            'D': "Önceki hamillerle ilişkiye dayanan kişisel def'iler iyiniyetli hamile karşı ileri sürülemez",
            'E': "Hamiline yazılı senette borçlu, tüm kişisel def'ilerini her hamile karşı ileri sürebilir",
        },
        'E',
        "TTK md. 659: hamiline yazılı senetlerde de kişisel def'iler İYİNİYETLİ hamile karşı ileri sürülemez; bu, senedin tedavül güvenliğini sağlar.",
    ),
    # düzey 2
    '0058': patch(
        'Zayi olan senedi için mahkemeden iptal kararı alan bir hamil, bundan sonra hakkını nasıl ileri süreceğini araştırmaktadır. Buna göre iptal kararının sonuçları bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İptal kararını alan kişi, hakkını senet olmaksızın ileri sürebilir',
            'B': 'İptal kararı borçluyu ödemeden kurtarır',
            'C': 'İptal kararı yalnızca kambiyo senetleri için verilebilir',
            'D': 'İptal kararı yalnızca zayi olan senedin yeniden düzenlenmesini sağlar',
            'E': 'İptal kararı hakkın da sona ermesine yol açar',
        },
        'A',
        'TTK md. 651 vd.: mahkemece verilen iptal kararı senedi hükümsüz kılar; iptal kararını alan kişi hakkını SENET OLMAKSIZIN ileri sürebilir. Hak sona ermez, borçlu da ödemeden kurtulmaz.',
    ),
    # düzey 2
    '0059': patch(
        'Bir uyuşmazlıkta senedin zorunlu unsurları ve bu unsurların hukuki işlevi tartışılmaktadır. Buna göre kıymetli evrakta şekil ve içerik bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Zorunlu unsuru eksik senet o tür kıymetli evrak sayılmaz',
            'B': 'Şekil şartları kanunda tür tür düzenlenmiştir',
            'C': 'Kıymetli evrakta şekil şartları yalnızca ispat kolaylığı sağlamaya yarar',
            'D': 'Şekil şartları kurucu nitelik taşır',
            'E': 'Zorunlu unsuru eksik senet, koşulları varsa adi senet olarak hüküm doğurabilir',
        },
        'C',
        'Kıymetli evrakta şekil şartları KURUCUDUR; ispat kolaylığı sağlamakla sınırlı değildir. Zorunlu unsuru eksik senet o tür kıymetli evrak sayılmaz.',
    ),
    # düzey 3
    '0060': patch(
        "Kıymetli evrak ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Kıymetli evrakta hak senede bağlıdır. II. Şekil şartları kurucu değil yalnızca ispata yarar. III. Zayi olan senedin iptaline mahkemece karar verilir. IV. Nama yazılı senette def'iler emre yazılı senetteki gibi sınırlıdır.",
        {
            'A': 'I ve III',
            'B': 'I, II ve IV',
            'C': 'Yalnız II',
            'D': 'II ve IV',
            'E': 'II ve III',
        },
        'D',
        "II YANLIŞ: kıymetli evrakta şekil şartları KURUCUDUR. IV YANLIŞ: nama yazılı senette borçlu devir anındaki def'ilerini yeni alacaklıya karşı ileri sürebilir; def'i sınırlaması emre ve hamiline yazılı senetlere özgüdür. I (md. 645) ve III (md. 651 vd.) doğrudur.",
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
    print(f"1 paket / {len(PATCHES)} soru (Kiymetli Evrak yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
