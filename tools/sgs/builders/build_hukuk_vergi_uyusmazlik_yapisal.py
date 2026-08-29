#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vergi Uyusmazliklari ve Yargi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Tanim kalibindan olay + kural uygulamasina: medyan kok 99->224, olumsuz kok %3->%35, kor ogrenci %26. Kapsam UYUSMAZLIK VE YARGI eksenine daraltildi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: IYUK m. 2, 3, 5, 7, 10, 11, 12, 14, 15, 17, 20, 27, 28, 45, 46, 48 · VUK m. 124, 125, 332, 336, 369, 372, 373, 374, 376, 377, 378, 413 (resmi metinden dogrulandi)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/vergi_hukuku/vergi_denetimi_ceza_uyusmazlik.json"
STYLE_REF = "SGS Hukuk (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "vh-denetim-gen-"


def patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": '2577 sayili IYUK ve 213 sayili VUK'},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Bir mükellef adına re'sen vergi tarh edilmiş ve vergi ziyaı cezası kesilmiştir. İhbarname usulüne uygun biçimde tebliğ edilmiştir. Mükellef, tarhiyatın ve cezanın hukuka aykırı olduğunu ileri sürerek yargı yoluna başvurmak istemektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': 'Dava açılabilmesi için önce verginin ödenmiş olması gerekir; ödeme yapılmadan açılan davalar esasa girilmeksizin reddedildiğinden mükellef önce ödemelidir',
            'B': 'Mükellefler ve kendilerine vergi cezası kesilenler, tarh edilen vergilere ve kesilen cezalara karşı vergi mahkemesinde dava açabilirler; dava açılabilmesi verginin tarh edilmiş ve cezanın kesilmiş olmasına bağlıdır',
            'C': 'Ceza kesilen kişi mükellef değilse dava açamaz; dava hakkı yalnız verginin mükellefine tanındığından ceza muhatabının başvurusu incelenmez',
            'D': 'Vergi uyuşmazlıkları idare mahkemesinde görülür; vergi mahkemesinin görev alanı yalnız tahsil işlemleriyle sınırlı olduğundan tarhiyata karşı orada dava açılamaz ve bu nedenle vergi uyuşmazlıklarında görevli mahkeme belirlenirken işlemin türü esas alınmaz',
            'E': 'Vergi ve ceza için ayrı ayrı dava açılması zorunludur; aynı ihbarnameye dayansalar dahi tek dilekçeyle dava açılamayacağından başvuru usulden reddedilir',
        },
        'B',
        '**VUK m. 377:** mükellefler ve kendilerine vergi cezası kesilenler, tarh edilen vergilere ve kesilen cezalara karşı **vergi mahkemesinde** dava açabilirler. **m. 378:** dava açılabilmesi için verginin tarh edilmesi, cezanın kesilmesi veya komisyon kararlarının tebliğ edilmiş olması gerekir; ödeme şartı yoktur.',
    ),
    # düzey 3
    '0002': patch(
        'Bir kişi, kendisiyle hiçbir hukuki ilişkisi bulunmayan başka bir mükellef adına yapılan tarhiyatın hukuka aykırı olduğunu ileri sürerek bu işlemin iptali istemiyle vergi mahkemesinde dava açmıştır. Davacının işlemle kişisel bir bağlantısı bulunmamaktadır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'İptal davası ancak menfaatleri ihlal edilenler tarafından açılabileceğinden, işlemle kişisel bağlantısı bulunmayan davacının davası ehliyet yönünden reddedilir',
            'B': 'İdari işlemlerin hukuka uygunluğu kamu yararını ilgilendirdiğinden herkes iptal davası açabilir; menfaat şartı aranmadığından mahkeme işin esasını inceler',
            'C': 'Üçüncü kişiler ancak vergi dairesinin izniyle dava açabilir; izin alınmadığından dava usul yönünden değil esastan reddedilir',
            'D': 'Menfaat şartı yalnız tam yargı davalarında aranır; iptal davasında böyle bir sınırlama bulunmadığından başvuru incelenir',
            'E': 'Dava ehliyeti yalnız davanın esasına girildikten sonra değerlendirilir; mahkeme önce hukuka aykırılığı saptamak zorunda olduğundan ön inceleme yapılamaz',
        },
        'A',
        '**İYUK m. 2/1-a:** iptal davası, idari işlemler hakkında hukuka aykırılıkları nedeniyle iptalleri için **menfaatleri ihlal edilenler tarafından** açılır. Menfaat, dava ehliyetinin (subjektif ehliyet) şartıdır; bulunmadığında dava esasa girilmeksizin reddedilir.',
    ),
    # düzey 2
    '0003': patch(
        'Bir mükellef adına hem vergi tarh edilmiş hem ceza kesilmiş; mükellef uzlaşmaya başvurmadan doğrudan yargı yoluna gitmek istemektedir. Vergi dairesi ise önce idari yolların tüketilmesi gerektiğini savunmaktadır. Buna göre vergi uyuşmazlıklarında dava hakkı ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Mükellefler tarh edilen vergilere karşı vergi mahkemesinde dava açabilirler',
            'B': 'Kendilerine vergi cezası kesilenler de kesilen cezalara karşı dava açabilirler',
            'C': 'Vergi mahkemesinde dava açılabilmesi için uyuşmazlığın önce uzlaşma komisyonunda görüşülmüş olması zorunludur',
            'D': 'Dava açılabilmesi için verginin tarh edilmiş veya cezanın kesilmiş olması gerekir ve bu nedenle tarh edilmemiş bir vergi için de dava açılabilir',
            'E': 'Mükellefler kural olarak beyan ettikleri matrahlara karşı dava açamazlar',
        },
        'C',
        '**VUK m. 377 ve 378** dava hakkını ve şartlarını düzenler; **uzlaşmaya başvurmuş olmak dava şartı değildir.** Uzlaşma, yargı yoluna alternatif bir idari çözüm yoludur.',
    ),
    # düzey 3
    '0004': patch(
        'Bir mükellefe vergi/ceza ihbarnamesi 10 Nisan tarihinde usulüne uygun olarak tebliğ edilmiştir. Mükellef 20 Mayıs tarihinde vergi mahkemesinde dava açmıştır. Özel kanununda ayrı bir süre gösterilmemiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Ceza kesilen kişi mükellef değilse dava açamaz; dava hakkı yalnız verginin mükellefine tanındığından ceza muhatabının başvurusu ehliyet yönünden reddedilir',
            'B': 'Vergi davalarında süre sınırı bulunmaz; tarhiyat zamanaşımına uğramadıkça dava her zaman açılabileceğinden başvuru incelenir',
            'C': 'Dava açma süresi vergi mahkemelerinde altmış gün olduğundan dava süresindedir; idare mahkemeleriyle vergi mahkemeleri arasında bir süre farkı bulunmaz ve bu nedenle vergi mahkemelerinde açılan davalarda süre yönünden ret kararı verilemez',
            'D': "Vergi mahkemelerinde dava açma süresi özel kanunlarında ayrı süre gösterilmeyen hâllerde otuz gün olduğundan süre 10 Mayıs'ta dolmuş, 20 Mayıs'taki dava süresinde açılmamıştır",
            'E': 'Dava açma süresi ihbarnamenin düzenlendiği tarihten işlediğinden süre henüz dolmamıştır; tebliğ tarihi süre bakımından sonuç doğurmaz',
        },
        'D',
        "**İYUK m. 7/1:** dava açma süresi, özel kanunlarında ayrı süre gösterilmeyen hâllerde **Danıştayda ve idare mahkemelerinde altmış, vergi mahkemelerinde otuz gündür.** Süre tebliğ tarihini izleyen günden işler; 10 Nisan tebliğinde süre 10 Mayıs'ta dolar.",
    ),
    # düzey 2
    '0005': patch(
        'Bir mükellef vergi mahkemesinde, bir başka ilgili ise idare mahkemesinde dava açacaktır; her ikisi de özel kanunlarında ayrı süre öngörülmeyen işlemlere karşı başvurmaktadır. Buna göre dava açma süreleri ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Özel kanunlarda ayrı bir süre öngörülmüşse o süre uygulanır',
            'B': 'Dava açma süresinin geçirilmesi hâlinde dava süre yönünden reddedilir',
            'C': 'Danıştayda ve idare mahkemelerinde dava açma süresi altmış gündür',
            'D': 'Dava açma süresi özel kanunlarında ayrı süre gösterilmeyen hâllerde vergi mahkemelerinde otuz gündür',
            'E': 'Vergi mahkemelerinde dava açma süresi altmış gün olup idare mahkemeleriyle aynıdır',
        },
        'E',
        '**İYUK m. 7/1:** süre **Danıştayda ve idare mahkemelerinde altmış**, **vergi mahkemelerinde otuz** gündür. İki yargı yeri için aynı süreyi gösteren ifade hükme aykırıdır.',
    ),
    # düzey 3
    '0006': patch(
        'Bir ilgili, idari dava açma süresi içinde, işlemin kaldırılması istemiyle üst makama başvurmuştur. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Üst makama başvuru zorunlu bir idari başvuru yolu olduğundan bu yol tüketilmeden açılan davalar esastan reddedilir',
            'B': 'Üst makama başvuru dava açma süresini kesintiye uğratır ve başvurunun reddi hâlinde otuz günlük süre baştan işlemeye başlar',
            'C': 'Üst makama başvuru dava açma süresini kesintiye uğratmaz; süre işlemeye devam ettiğinden ilgilinin ayrıca süresinde dava açması gerekir ve aksi hâlde hakkı düşer',
            'D': 'Üst makama başvuru yalnız idare mahkemelerinde açılacak davalar için öngörülmüştür; vergi uyuşmazlıklarında bu imkân bulunmaz',
            'E': 'İdari dava açma süresi içinde üst makama başvurulması işlemeye başlamış olan dava açma süresini durdurur; başvurunun reddi hâlinde kalan süre yeniden işlemeye başlar',
        },
        'E',
        '**İYUK m. 11:** ilgililer, idari dava açma süresi içinde işlemin kaldırılması, geri alınması veya değiştirilmesi için üst makama başvurabilir; bu başvuru **işlemeye başlamış olan dava açma süresini durdurur.** Durma söz konusudur, kesilme değil.',
    ),
    # düzey 2
    '0007': patch(
        'Bir mükellef, dava açmış olmasının işlemin uygulanmasını kendiliğinden durduracağını düşünmektedir. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Yürütmenin durdurulması kararları gerekçeli olarak verilir',
            'B': 'Yürütmenin durdurulması için işlemin açıkça hukuka aykırı olması aranır',
            'C': 'Yürütmenin durdurulmasına ancak talep üzerine ve kanunda öngörülen şartlarla karar verilir ve bu nedenle mahkemenin ayrıca bir karar vermesine gerek kalmadan tahsil işlemleri durur',
            'D': 'Danıştayda veya idari mahkemelerde dava açılması, dava edilen idari işlemin yürütülmesini kendiliğinden durdurur',
            'E': 'Yürütmenin durdurulması için telafisi güç veya imkânsız zararların doğması da aranır',
        },
        'D',
        "**İYUK m. 27/1:** dava açılması dava edilen idari işlemin yürütülmesini **durdurmaz**; durdurma ancak m. 27/2'deki iki şartın birlikte gerçekleşmesi hâlinde ve talep üzerine mümkündür.",
    ),
    # düzey 2
    '0008': patch(
        'Bir mükellef, dava dilekçesinde yürütmenin durdurulmasını talep etmiş; mahkeme işlemin hukuka aykırılığını saptamakla birlikte zarar unsurunu ayrıca değerlendirmiştir. Buna göre yürütmenin durdurulması ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Dava açılması dava edilen idari işlemin yürütülmesini kendiliğinden durdurmaz',
            'B': 'Yürütmenin durdurulmasına karar verilebilmesi için işlemin hukuka aykırı olması tek başına yeterlidir',
            'C': 'Yürütmenin durdurulması istemi dava dilekçesinde ileri sürülür',
            'D': 'Yürütmenin durdurulması kararı verilebilmesi telafisi güç veya imkânsız zararların doğması şartına da bağlıdır',
            'E': 'Yürütmenin durdurulması kararları gerekçeli olarak verilir',
        },
        'B',
        '**İYUK m. 27/2:** yürütmenin durdurulmasına, **idari işlemin uygulanması hâlinde telafisi güç veya imkânsız zararların doğması ve idari işlemin açıkça hukuka aykırı olması şartlarının birlikte gerçekleşmesi** durumunda karar verilir. Tek şartın yeterli olduğunu söyleyen ifade yanlıştır.',
    ),
    # düzey 2
    '0009': patch(
        'Bir vergi davasında taraflar belirli delilleri dosyaya sunmuş; mahkeme ise uyuşmazlığın çözümü için başka bilgi ve belgelere ihtiyaç duymuştur. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Kendiliğinden araştırma yetkisi yalnız Danıştaya tanınmıştır; ilk derece mahkemeleri bu yetkiyi kullanamayacağından talep reddedilir',
            'B': 'Mahkeme yalnız tarafların sunduğu delillerle bağlıdır; kendiliğinden araştırma yapamayacağından dosyaya sunulmamış belgeler hükme esas alınamaz ve karar eksik incelemeye dayanır',
            'C': 'Mahkemenin bilgi istemesi ancak tarafların ortak talebiyle mümkündür; taraflardan biri karşı çıkarsa araştırma yapılamaz',
            'D': 'Vergi yargısında delil serbestisi bulunmadığından yalnız defter ve belgeler delil olarak kabul edilir; başka bilgi istenemez',
            'E': 'Vergi mahkemeleri bakmakta oldukları davalara ait her türlü incelemeyi kendiliğinden yapar; gerekli gördükleri bilgi ve belgelerin gönderilmesini taraflardan veya ilgili yerlerden isteyebilir',
        },
        'E',
        "**İYUK m. 20/1:** Danıştay, bölge idare mahkemeleri ile idare ve vergi mahkemeleri, **bakmakta oldukları davalara ait her türlü incelemeyi kendiliğinden yapar** ve gerekli gördükleri belgelerin gönderilmesini isteyebilir (re'sen araştırma ilkesi).",
    ),
    # düzey 2
    '0010': patch(
        'Bir vergi mahkemesi, mükellefin açtığı davayı reddetmiştir. Mükellef bu karara karşı kanun yoluna başvurmak istemektedir. Kararın istinaf yoluna kapalı olduğuna dair bir hüküm bulunmamaktadır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'İstinaf başvurusu kararı veren vergi mahkemesine yapılır ve aynı mahkemece karara bağlanır; üst bir yargı merciine gidilmez',
            'B': 'Vergi mahkemesi kararları kesin olup hiçbir kanun yoluna tabi değildir; bu nedenle mükellefin başvurusu incelenmeksizin reddedilir',
            'C': 'İdare ve vergi mahkemelerinin kararlarına karşı, mahkemenin bulunduğu yargı çevresindeki bölge idare mahkemesine istinaf yoluyla başvurulabilir',
            'D': 'Vergi mahkemesi kararlarına karşı doğrudan Danıştaya temyiz yoluyla başvurulur; istinaf yolu vergi yargısında öngörülmediğinden bölge idare mahkemesine gidilemez',
            'E': 'İstinaf başvurusu yalnız davanın kabulü hâlinde mümkündür; ret kararlarına karşı kanun yolu kapalı olduğundan mükellef başvuramaz',
        },
        'C',
        '**İYUK m. 45/1:** idare ve vergi mahkemelerinin kararlarına karşı, başka kanunlarda farklı bir kanun yolu öngörülmüş olsa dahi, **mahkemenin bulunduğu yargı çevresindeki bölge idare mahkemesine istinaf yoluna** başvurulabilir.',
    ),
    # düzey 3
    '0011': patch(
        'Bir bölge idare mahkemesi, istinaf başvurusu üzerine verdiği kararla uyuşmazlığı sonuçlandırmıştır. Karar, kanunda temyize açık olarak sayılan davalardan birine ilişkindir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Bölge idare mahkemesi kararlarının tamamı temyize tabidir; kanunda bir sınırlama bulunmadığından her karar Danıştaya taşınabilir',
            'B': 'Bölge idare mahkemesi kararları kesindir; istinaf sonrası başka bir kanun yolu bulunmadığından temyiz başvurusu incelenmeksizin reddedilir ve karar o aşamada kesinleşir',
            'C': 'Bölge idare mahkemelerinin kanunda sayılan davalar hakkında verdikleri kararlar, başka kanunlarda aksine hüküm bulunsa dahi Danıştayda temyiz edilebilir',
            'D': 'Temyiz başvurusu kararı veren bölge idare mahkemesine yapılır ve aynı merci tarafından incelenir; Danıştaya gönderilmez',
            'E': 'Temyiz yolu yalnız idare mahkemesi kararları için açıktır; vergi uyuşmazlıklarında temyiz imkânı öngörülmemiştir',
        },
        'C',
        '**İYUK m. 46:** Danıştay dava dairelerinin nihai kararları ile **bölge idare mahkemelerinin aşağıda sayılan davalar hakkında verdikleri kararlar**, başka kanunlarda aksine hüküm bulunsa dahi Danıştayda temyiz edilebilir. Temyiz, sayılan davalarla sınırlıdır.',
    ),
    # düzey 2
    '0012': patch(
        'Bir mükellef vergi mahkemesi kararına karşı kanun yoluna başvuracak; kararın hangi mercie ve hangi usulle taşınacağını belirlemek istemektedir. Buna göre vergi uyuşmazlıklarında kanun yolları ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Danıştay dava dairelerinin nihai kararları temyize tabidir',
            'B': 'Vergi mahkemesi kararlarına karşı istinaf başvurusu doğrudan Danıştaya yapılır ve Danıştay kararı kesindir',
            'C': 'Bölge idare mahkemelerinin kanunda sayılan davalar hakkındaki kararları Danıştayda temyiz edilebilir',
            'D': 'İdare ve vergi mahkemesi kararlarına karşı bölge idare mahkemesine istinaf yoluna başvurulabilir',
            'E': 'Temyiz istemleri Danıştay Başkanlığına hitaben yazılmış dilekçelerle yapılır',
        },
        'B',
        '**İYUK m. 45:** istinaf başvurusu **mahkemenin bulunduğu yargı çevresindeki bölge idare mahkemesine** yapılır; Danıştay istinaf mercii değildir. **m. 46 ve 48** temyizi düzenler.',
    ),
    # düzey 2
    '0013': patch(
        'Bir vergi mahkemesi kararı kesinleşmiş; idare kararın gereğini yerine getirmemektedir. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'İdarenin işlem tesis etme yükümlülüğü yalnız iptal kararlarında doğar; yürütmenin durdurulması kararları bakımından böyle bir zorunluluk bulunmaz',
            'B': 'Mahkemelerin esasa ilişkin kararlarının icaplarına göre idare gecikmeksizin işlem tesis etmekle yükümlüdür ve idare yürütmenin durdurulması kararını uygulamakta serbest kalır',
            'C': 'Yargı kararlarının uygulanmaması hukuki sonuçlar doğurur',
            'D': 'Bu yükümlülük yürütmenin durdurulmasına ilişkin kararlar için de geçerlidir',
            'E': 'İdarenin yükümlülüğü kanunla düzenlenmiş olup takdire bırakılmamıştır',
        },
        'A',
        '**İYUK m. 28/1:** yükümlülük **esasa ve yürütmenin durdurulmasına ilişkin** kararların her ikisi için de geçerlidir.',
    ),
    # düzey 3
    '0014': patch(
        'Bir mükellefin vergi hatasının düzeltilmesine ilişkin talebi, vergi mahkemesinde dava açma süresi geçtikten sonra vergi dairesince reddedilmiştir. Mükellef bu redde karşı ne yapabileceğini sormaktadır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Şikâyet yolu yalnız tarh işlemlerine karşı açıktır; vergi hatalarında bu yola başvurulamayacağından talep reddedilir',
            'B': 'Şikâyet başvurusu kararı veren vergi dairesine yapılır ve aynı daire tarafından yeniden değerlendirilir; üst makama gidilmez',
            'C': 'Mükellef doğrudan vergi mahkemesinde dava açabilir; dava açma süresinin geçmiş olması düzeltme talebinin reddi bakımından sonuç doğurmaz',
            'D': 'Dava açma süresi geçtikten sonra yaptıkları düzeltme talepleri reddolunanlar şikâyet yolu ile Hazine ve Maliye Bakanlığına müracaat edebilirler',
            'E': 'Dava açma süresi geçtikten sonra hiçbir başvuru yolu kalmaz; düzeltme talebinin reddi kesin olduğundan mükellefin yapabileceği bir işlem bulunmaz',
        },
        'D',
        '**VUK m. 124:** vergi mahkemesinde **dava açma süresi geçtikten sonra** yaptıkları düzeltme talepleri reddolunanlar, **şikâyet yolu ile Bakanlığa** müracaat edebilirler. Bu, süre geçtikten sonra açık kalan idari başvuru yoludur.',
    ),
    # düzey 3
    '0015': patch(
        'Vergi mahkemesi ve Danıştaydan geçmiş, yargı kararı kesinleşmiş bir işlemde sonradan vergi hatası bulunduğu anlaşılmıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Kesinleşmiş kararlardaki hatalar yalnız mükellef lehine ise düzeltilebilir; idare lehine olan hatalar düzeltme kapsamı dışındadır',
            'B': 'Düzeltme yalnız hükmü veren mahkemenin izniyle yapılabilir; izin alınmadan yapılan düzeltme işlemleri geçersiz sayılır',
            'C': 'Yargı mercilerinden geçmiş işlemlerde vergi hataları bulunması hâlinde bu hatalar, yargı kararları kesinleşmiş olsa bile düzeltme hükümlerine göre düzeltilebilir',
            'D': 'Kesinleşmiş kararlarda düzeltme ancak yargılamanın yenilenmesi yoluyla mümkündür; idari düzeltme yolu tümüyle kapalıdır',
            'E': 'Yargı kararı kesinleştikten sonra hiçbir düzeltme yapılamaz; kesin hüküm her türlü idari işleme engel oluşturduğundan hata giderilemez ve bu nedenle kesinleşmiş kararlardaki maddi hatalar hiçbir yolla giderilemez',
        },
        'C',
        '**VUK m. 125:** vergi mahkemesi, bölge idare mahkemesi ve Danıştaydan geçmiş olan muamelelerde vergi hataları bulunduğu takdirde, bu hatalar **yargı kararları kesinleşmiş olsa bile** önceki maddelere göre düzeltilebilir.',
    ),
    # düzey 3
    '0016': patch(
        'Bir mükellef idareden aldığı izahata uygun hareket etmiş; sonradan bu görüşün hatalı olduğu anlaşılmıştır. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'İdareden alınan izahata uygun hareket eden mükelleften vergi aslı da aranmaz; verilen görüş mükellef bakımından vergiyi ortadan kaldırır',
            'B': 'Mükellefler vergi uygulaması bakımından tereddüde düştükleri hususlarda idareden izahat isteyebilirler ve bu nedenle özelge alan mükellef hakkında hiçbir tarhiyat yapılamaz',
            'C': 'Alınan izahata uygun hareket eden mükellefe ceza kesilmez',
            'D': 'İzahat talebi Gelir İdaresi Başkanlığından veya yetkili kıldığı makamlardan yapılır',
            'E': 'İzahata uygun hareket eden mükelleften eksik ödenen vergi aslı aranmaya devam eder',
        },
        'A',
        '**VUK m. 369** izahata uygun hareket edenlere **ceza kesilmemesini** öngörür; koruma cezaya yöneliktir. **Vergi aslı ve gecikme faizi** bu korumanın dışındadır.',
    ),
    # düzey 2
    '0017': patch(
        'Bir mükellefin düzeltme talebi dava açma süresi dolmadan reddedilmiş; bir başka mükellefin talebi ise süre geçtikten sonra reddedilmiştir. İki mükellef izleyecekleri yolu sormaktadır. Buna göre vergi uyuşmazlıklarının idari çözüm yolları ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Vergi hatalarının düzeltilmesi vergi dairesinden yazı ile istenebilir',
            'B': 'Dava açma süresi geçtikten sonra düzeltme talebi reddolunanlar şikâyet yoluyla Bakanlığa başvurabilir',
            'C': 'Şikâyet yoluyla Bakanlığa müracaat, vergi mahkemesinde dava açma süresi henüz dolmadan başvurulabilecek bir yoldur',
            'D': 'Mükellefler tereddüt ettikleri hususlarda idareden izahat isteyebilirler',
            'E': 'Yargı mercilerinden geçmiş işlemlerdeki vergi hataları kararlar kesinleşmiş olsa bile düzeltilebilir',
        },
        'C',
        '**VUK m. 124:** şikâyet yolu, **dava açma süresi geçtikten sonra** düzeltme talebi reddolunanlara açıktır. Süre henüz dolmamışsa mükellefin başvuracağı yol dava yoludur.',
    ),
    # düzey 3
    '0018': patch(
        'Bir mükellef adına vergi ziyaı cezası kesilmek istenmektedir. Cezanın bağlı olduğu vergi alacağı 2020 takvim yılında doğmuş; idare cezayı 2026 yılında kesmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Ceza kesme zamanaşımı bulunmaz; vergi cezaları süreye bağlı olmaksızın her zaman kesilebileceğinden mükellefin itirazı dinlenmez',
            'B': 'Vergi ziyaı cezasında ceza kesme zamanaşımı, cezanın bağlı olduğu vergi alacağının doğduğu takvim yılını takip eden yılın birinci gününden başlayarak beş yıldır; süre dolduğundan ceza kesilemez',
            'C': 'Ceza kesme zamanaşımı yalnız usulsüzlük cezalarında uygulanır; vergi ziyaı cezasında süre sınırı öngörülmediğinden ceza kesilebilir',
            'D': "Ceza kesme zamanaşımı cezanın kesildiği tarihten itibaren işler; bu nedenle 2026'daki işlemde süre henüz başlamamış sayılır",
            'E': "Ceza kesme zamanaşımı on yıl olduğundan idare 2026'da ceza kesebilir; vergi ziyaı cezalarında uzun süre uygulandığından işlem hukuka uygundur ve bu nedenle idare zamanaşımı def'ini dikkate almaksızın işlem tesis edebilir",
        },
        'B',
        "**VUK m. 374/1:** vergi ziyaı cezasında, cezanın bağlı olduğu **vergi alacağının doğduğu takvim yılını takip eden yılın birinci gününden** başlayarak **beş yıl** geçtikten sonra ceza kesilmez. 2020'de doğan alacakta süre 31 Aralık 2025'te dolar.",
    ),
    # düzey 2
    '0019': patch(
        'Cezayı gerektiren tek bir fiil ile hem vergi ziyaı hem de usulsüzlük birlikte işlenmiştir. Buna göre kesilecek ceza bakımından aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Cezalardan miktar itibarıyla en hafif olanı kesilir; ağır cezanın uygulanması ölçülülük ilkesine aykırı sayıldığından tercih hafif olandan yana yapılır',
            'B': 'Cezaların ortalaması alınarak tek bir ceza kesilir; kanun bu yöntemi öngördüğünden iki ceza da kısmen uygulanmış olur',
            'C': 'Her iki ceza da ayrı ayrı kesilir ve toplanarak tahsil edilir; kanun bu hâlde bir birleştirme öngörmediğinden iki yaptırım birlikte uygulanır',
            'D': 'Yalnız usulsüzlük cezası kesilir; vergi ziyaı cezası şekli aykırılığın içinde eridiğinden ayrıca uygulanmaz',
            'E': 'Tek bir fiil ile vergi ziyaı ve usulsüzlük birlikte işlenmişse bunlara ait cezalardan sadece miktar itibarıyla en ağır olanı kesilir',
        },
        'E',
        '**VUK m. 336:** cezayı istilzam eden **tek bir fiil ile vergi ziyaı ve usulsüzlük birlikte işlenmiş olursa** bunlara ait cezalardan **sadece miktar itibarıyla en ağırı** kesilir.',
    ),
    # düzey 2
    '0020': patch(
        'Vergi cezası kesilen bir mükellef, ceza kesinleşmeden önce vefat etmiştir. Mirasçılar cezanın kendilerinden istenip istenemeyeceğini sormaktadır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Ceza yalnız mirası reddeden mirasçılar bakımından düşer; mirası kabul edenler cezadan sorumlu olmaya devam eder',
            'B': 'Vergi cezaları mirasçılara intikal eder; borç mirasla birlikte geçtiğinden mirasçılar cezadan da sorumlu tutulur ve mirasçılar cezayı miras payları oranında ödemekle yükümlü tutulur',
            'C': 'Ölüm hâlinde hem vergi aslı hem ceza düşer; mirasçılardan hiçbir alacak istenemeyeceğinden dosya kapatılır',
            'D': 'Ölüm hâlinde vergi cezası düşer; cezaların şahsiliği gereği mirasçılardan ceza istenemez, ancak vergi aslı mirasçılara intikal eder',
            'E': 'Ölüm hâlinde ceza düşmez ancak yarı oranında indirilir; kanun bu hâl için özel bir indirim öngörmüştür',
        },
        'D',
        '**VUK m. 372:** **ölüm hâlinde vergi cezası düşer.** Bu, cezaların şahsiliği ilkesinin sonucudur. Vergi aslı ise borç niteliğiyle mirasçılara intikal eder.',
    ),
    # düzey 3
    '0021': patch(
        'Velayet altındaki bir küçüğün vergi ödevleri velisi tarafından yerine getirilmekte olup, velinin vergi kanunlarına aykırı hareketi nedeniyle ceza gündeme gelmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Ceza hem küçüğe hem veliye ayrı ayrı kesilir; kanun her iki tarafı da sorumlu tuttuğundan iki ceza birlikte uygulanır',
            'B': 'Velayet ve vesayet altında bulunanlar, kendilerine izafeten veli, vasi veya kayyımın vergi kanunlarına aykırı hareketlerinden dolayı cezaya muhatap tutulmazlar; ceza bu kişilerin kendilerine kesilir',
            'C': 'Küçükler bakımından hiçbir ceza kesilmez ve velinin de sorumluluğu doğmaz; bu nedenle fiil cezasız kalır',
            'D': 'Ceza küçük adına kesilir; vergi ödevlerinin muhatabı küçük olduğundan aykırı hareketin sonucu da ona yüklenir ve veli yalnız ödemeden sorumlu tutulur',
            'E': 'Ceza küçük adına kesilir ancak veli tarafından ödenir; muhataplık ile ödeme yükümlülüğü birbirinden ayrıldığından sonuç değişmez ve bu nedenle veli ile küçük arasında ceza bakımından bir ayrım gözetilmez',
        },
        'B',
        '**VUK m. 332:** velayet ve vesayet altında bulunanlar veya işleri kayyıma tevdi edilmiş olanlar, **kendilerine izafeten veli, vasi veya kayyımın** vergi kanunlarına aykırı hareketlerinden dolayı **cezaya muhatap tutulmazlar**; ceza bu kişiler adına kesilir.',
    ),
    # düzey 2
    '0022': patch(
        'Bir mükellefin vergi ödevini süresinde yerine getirememesine, kanunda sayılan bir mücbir sebep yol açmış ve bu durum ispatlanmıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Mücbir sebep yalnız süreleri durdurur; ceza kesilmesine engel oluşturmadığından mükellef adına ceza uygulanır',
            'B': 'Mücbir sebep hâlinde ceza yarı oranında indirilerek kesilir; kanun tam bir muafiyet öngörmemiştir',
            'C': 'Kanunda yazılı mücbir sebeplerden birinin vukua geldiği malûm ise veya ispat olunursa vergi cezası kesilmez',
            'D': 'Mücbir sebebin ceza kesilmesine engel olabilmesi için ayrıca mahkeme kararıyla tespit edilmiş olması gerekir',
            'E': 'Mücbir sebep yalnız afetleri kapsar; ağır hastalık gibi kişisel hâller ceza bakımından sonuç doğurmaz',
        },
        'C',
        "**VUK m. 373:** bu Kanunda yazılı mücbir sebeplerden herhangi birinin **vukua geldiği malûm ise veya tevsik ve ispat olunursa vergi cezası kesilmez.** Mücbir sebepler m. 13'te sayılmıştır.",
    ),
    # düzey 2
    '0023': patch(
        'Bir mükellef vergi cezası kesildikten sonra vefat etmiş; mirasçıları hem cezadan hem vergi aslından sorumlu tutulup tutulmayacaklarını sormaktadır. Buna göre vergi cezaları ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Vergi cezaları mirasçılara intikal eder; ölüm cezanın tahsilini engellemediğinden mirasçılardan istenebilir',
            'B': 'Ölüm hâlinde vergi cezası düşer',
            'C': 'Mücbir sebebin varlığı ispat olunursa vergi cezası kesilmez',
            'D': 'Velayet altındakiler, veli veya vasinin aykırı hareketlerinden dolayı cezaya muhatap tutulmazlar',
            'E': 'Tek bir fiille vergi ziyaı ve usulsüzlük birlikte işlenmişse cezalardan en ağırı kesilir',
        },
        'A',
        '**VUK m. 372:** **ölüm hâlinde vergi cezası düşer**; cezaların şahsiliği gereği mirasçılara intikal etmez. Vergi aslı ise borç olarak intikal eder.',
    ),
    # düzey 3
    '0024': patch(
        'Vergi uyuşmazlıklarında zamanaşımı ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Vergi ziyaı cezasında ceza kesme zamanaşımı beş yıldır.\n\nII. Ceza kesme zamanaşımı, cezanın kesildiği tarihten itibaren işlemeye başlar.\n\nIII. Zamanaşımı süresi dolduktan sonra vergi cezası kesilemez.',
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'Yalnız II',
            'D': 'I, II ve III',
            'E': 'I ve II',
        },
        'B',
        '**I ve III doğru:** m. 374/1 vergi ziyaı cezasında beş yıllık süre öngörür ve süre dolduktan sonra ceza kesilemez. **II yanlış:** süre, cezanın bağlı olduğu **vergi alacağının doğduğu** takvim yılını takip eden yılın birinci gününden başlar.',
    ),
    # düzey 2
    '0025': patch(
        'Bir mükellef, vergi mahkemesinde dava açmak üzere hazırladığı dilekçeyi imzalamaksızın mahkemeye vermiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Dilekçenin imzalı olması yalnız Danıştaya açılan davalarda aranır; vergi mahkemelerinde imza şartı öngörülmemiştir',
            'B': 'Dilekçenin imzalanması zorunlu değildir; dilekçenin mahkemeye verilmiş olması dava açmak için yeterli sayıldığından eksiklik sonuç doğurmaz ve mahkeme dilekçedeki eksiklikleri kendiliğinden tamamlayarak davayı görür',
            'C': 'İmzasız dilekçeyle açılan dava doğrudan esastan reddedilir; eksikliğin sonradan giderilmesi mümkün olmadığından yeniden dava açılamaz',
            'D': 'İdari davalar ilgili mahkeme başkanlıklarına hitaben yazılmış imzalı dilekçelerle açılır; imza eksikliği dilekçe üzerine yapılan ilk incelemede saptanarak giderilmesi istenir',
            'E': 'İmza eksikliği yalnız davalı idarenin itirazı hâlinde dikkate alınır; mahkeme kendiliğinden bu hususu inceleyemez',
        },
        'D',
        '**İYUK m. 3/1:** idari davalar, Danıştay, idare mahkemesi ve vergi mahkemesi başkanlıklarına hitaben yazılmış **imzalı dilekçelerle** açılır. **m. 14** dilekçeler üzerinde ilk incelemeyi, **m. 15** bu inceleme sonucu verilecek kararları düzenler.',
    ),
    # düzey 3
    '0026': patch(
        'Bir mükellef, aralarında sebep-sonuç ilişkisi bulunan birden fazla idari işleme karşı tek dilekçeyle dava açmıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Kural olarak her idari işlem aleyhine ayrı ayrı dava açılır; ancak aralarında maddi veya hukuki yönden bağlılık ya da sebep-sonuç ilişkisi bulunan işlemlere karşı tek dilekçeyle dava açılabilir',
            'B': 'Tek dilekçeyle dava yalnız Danıştayda mümkündür; ilk derece mahkemelerinde her işlem için ayrı dilekçe zorunludur',
            'C': 'Her idari işlem için mutlaka ayrı dava açılması gerekir; işlemler arasında bağlantı bulunsa dahi tek dilekçeyle dava açılamayacağından dilekçe reddedilir ve bu nedenle bağlantılı işlemler için ayrı ayrı harç ödenmesi gerekir',
            'D': 'Birden fazla işleme karşı tek dilekçeyle dava açılabilir; kanun bu konuda bir sınırlama getirmediğinden işlemler arasında bağlantı bulunması aranmaz',
            'E': 'Tek dilekçeyle dava açılabilmesi işlemlerin aynı idare tarafından tesis edilmiş olmasına bağlıdır; başka bir ölçüt aranmaz',
        },
        'A',
        '**İYUK m. 5/1:** her idari işlem aleyhine **ayrı ayrı** dava açılır; ancak **aralarında maddi veya hukuki yönden bağlılık ya da sebep-sonuç ilişkisi bulunan** birden fazla işleme karşı bir dilekçe ile de dava açılabilir.',
    ),
    # düzey 3
    '0027': patch(
        'Bir ilgili, idari davaya konu olabilecek bir işlemin yapılması için idari makama başvurmuş; idare altmış gün içinde cevap vermemiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Cevap verilmemesi hâlinde ilgili yalnız üst makama başvurabilir; doğrudan dava yolu kapalı olduğundan yargıya gidilemez',
            'B': 'İdare cevap verinceye kadar dava açılamaz; cevap gelmedikçe dava açma süresi işlemeye başlamadığından bekleme zorunludur ve bu nedenle idarenin sükûtu hâlinde dava açma süresi hiç işlemez',
            'C': 'Cevap süresi otuz gün olup bu süre sonunda istek kabul edilmiş sayılır; idare işlemi tesis etmekle yükümlü hâle gelir',
            'D': 'İdarenin cevap vermemesi isteğin kabul edildiği anlamına gelir; bu nedenle ilgilinin dava açmasına gerek kalmaz',
            'E': 'Altmış gün içinde bir cevap verilmezse istek reddedilmiş sayılır ve ilgili, bu tarihten itibaren dava açma süresi içinde yargı yoluna başvurabilir',
        },
        'E',
        '**İYUK m. 10/2:** ilgililerin idari makamlara yaptıkları başvuruya **altmış gün içinde bir cevap verilmezse istek reddedilmiş sayılır** ve ilgili bu tarihten itibaren dava açma süresi içinde dava açabilir (zımni ret).',
    ),
    # düzey 2
    '0028': patch(
        'Bir mükellef, aralarında sebep-sonuç ilişkisi bulunan iki işleme karşı tek dilekçeyle ve imzasız olarak dava açmak istemektedir. Buna göre vergi yargısında dava açma usulü ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Aralarında sebep-sonuç ilişkisi bulunan işlemlere karşı tek dilekçeyle dava açılabilir ve bu nedenle bağlantılı işlemler için ayrı ayrı dilekçe verilmesi zorunlu olur',
            'B': 'İdari davalar mahkeme başkanlıklarına hitaben yazılmış imzalı dilekçelerle açılır',
            'C': 'Kural olarak her idari işlem aleyhine ayrı ayrı dava açılır',
            'D': 'Vergi davaları sözlü başvuruyla da açılabilir; dilekçe şartı yalnız Danıştayda görülen davalar için aranır',
            'E': 'Dilekçeler üzerinde mahkemece ilk inceleme yapılır',
        },
        'D',
        '**İYUK m. 3/1:** idari davalar **imzalı dilekçelerle** açılır; sözlü başvuru bir dava açma usulü olarak öngörülmemiştir ve bu kural bütün idari yargı yerleri için geçerlidir.',
    ),
    # düzey 2
    '0029': patch(
        'Vergi mahkemesinde görülen bir davada taraflardan biri duruşma talebinde bulunmuştur. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'İptal davalarında taraflardan birinin isteği üzerine duruşma yapılır',
            'B': 'Tarh edilen vergilere ilişkin davalarda kanunda öngörülen parasal sınırı aşan uyuşmazlıklarda duruşma yapılabilir',
            'C': 'İdari yargıda duruşma yapılmaz; yargılama tümüyle yazılı usule tabi olduğundan taraf talebi sonuç doğurmaz',
            'D': 'Danıştay ile idare ve vergi mahkemelerinde duruşma usulü kanunda düzenlenmiştir',
            'E': 'Duruşma talebi dava dilekçesinde ileri sürülebilir',
        },
        'C',
        '**İYUK m. 17:** iptal davaları ile kanunda belirtilen parasal sınırı aşan tam yargı davalarında ve tarh edilen vergilere ilişkin davalarda **taraflardan birinin isteği üzerine duruşma yapılır.**',
    ),
    # düzey 2
    '0030': patch(
        'Vergi uyuşmazlıklarında yargılama usulü ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Mahkemeler bakmakta oldukları davalara ait her türlü incelemeyi kendiliğinden yapar.\n\nII. Dava açılması dava edilen idari işlemin yürütülmesini kendiliğinden durdurur.\n\nIII. İdari davalar mahkeme başkanlıklarına hitaben yazılmış imzalı dilekçelerle açılır.',
        {
            'A': 'Yalnız I',
            'B': 'Yalnız II',
            'C': 'I ve II',
            'D': 'I ve III',
            'E': 'I, II ve III',
        },
        'D',
        "**I doğru:** m. 20/1 re'sen araştırma ilkesi. **III doğru:** m. 3/1. **II yanlış:** **m. 27/1** uyarınca dava açılması yürütmeyi **durdurmaz**; yürütmenin durdurulması ayrı bir karara bağlıdır.",
    ),
    # düzey 3
    '0031': patch(
        "Bir mükellefe 3 Mart tarihinde vergi/ceza ihbarnamesi tebliğ edilmiştir. Mükellef 20 Mart'ta tarhiyat sonrası uzlaşma talebinde bulunmuş, uzlaşma sağlanamamıştır. Buna göre dava açma süresi bakımından aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': "Uzlaşma talebi dava açma süresini hiç etkilemez; süre kesintisiz işlediğinden mükellefin 2 Nisan'a kadar ayrıca dava açmış olması gerekirdi",
            'B': 'Uzlaşma talebinde bulunan mükellef dava açma hakkını tümüyle kaybeder; uzlaşma yolu seçildiğinde yargı yolu kapandığından başvuru incelenmez ve mükellefin uzlaşma tutanağını imzalamış olması yargı yolunu tümüyle kapatır',
            'C': 'Uzlaşmanın sağlanamaması hâlinde dava açma süresi yeniden otuz gün olarak baştan işler; önceki günler hesaba katılmaz',
            'D': 'Uzlaşma talebi dava açma süresini etkileyen bir başvuru olduğundan uzlaşmanın sağlanamaması hâlinde mükellefin dava açma hakkı kanunda öngörülen kalan süre içinde kullanılabilir',
            'E': 'Uzlaşma sağlanamazsa mükellef ancak şikâyet yoluyla Bakanlığa başvurabilir; dava yolu bu aşamada kullanılamaz',
        },
        'D',
        "Uzlaşma, **VUK Ek m. 1 vd.**'de düzenlenen idari çözüm yoludur; uzlaşmanın sağlanamaması hâlinde mükellefin **VUK m. 377** uyarınca dava açma hakkı devam eder. Uzlaşmaya başvurmak dava hakkını ortadan kaldırmaz.",
    ),
    # düzey 3
    '0032': patch(
        'Bir mükellef, vergi mahkemesinde açtığı davayı kaybetmiş; karar kendisine tebliğ edilmiştir. Mükellef üst yargı yoluna başvurmak istemektedir. Buna göre başvurulacak merci bakımından aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Vergi mahkemesi kararına karşı doğrudan Danıştaya temyiz başvurusu yapılır; istinaf aşaması vergi yargısında bulunmadığından bölge idare mahkemesine gidilmez ve bölge idare mahkemesi vergi uyuşmazlıklarında hiçbir görev üstlenmez',
            'B': 'Vergi mahkemesi kararına karşı, mahkemenin bulunduğu yargı çevresindeki bölge idare mahkemesine istinaf yoluyla başvurulur; istinaf sonrası kanunda sayılan hâllerde Danıştayda temyiz mümkündür',
            'C': 'Vergi mahkemesi kararları kesin olduğundan hiçbir kanun yoluna başvurulamaz; mükellefin yapabileceği tek şey düzeltme talebidir',
            'D': 'Vergi mahkemesi kararına karşı yeniden aynı mahkemede dava açılır; kanun yolları yerine yenileme usulü öngörüldüğünden başka bir merciye başvurulmaz',
            'E': 'Vergi mahkemesi kararına karşı önce Bakanlığa şikâyet başvurusu yapılması zorunludur; bu yol tüketilmeden kanun yoluna gidilemez',
        },
        'B',
        '**İYUK m. 45:** vergi mahkemesi kararlarına karşı **bölge idare mahkemesine istinaf**; **m. 46:** bölge idare mahkemesinin kanunda sayılan davalar hakkındaki kararlarına karşı **Danıştayda temyiz** yolu açıktır.',
    ),
    # düzey 3
    '0033': patch(
        'Bir mükellef, vergi hatası bulunduğu gerekçesiyle vergi dairesine düzeltme talebinde bulunmuş; talep dava açma süresi içinde reddedilmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Düzeltme talebi reddedilse dahi mükellef aynı talebi sınırsız sayıda yenileyebilir; her yenileme süreyi durdurur',
            'B': 'Düzeltme talebinin reddi dava açma süresini yeniden başlatır; mükellef ret tarihinden itibaren otuz gün daha kazanır',
            'C': 'Düzeltme talebinin reddine karşı hiçbir başvuru yolu bulunmaz; ret işlemi kesin olduğundan mükellefin yapabileceği bir şey kalmaz',
            'D': 'Düzeltme talebinin reddi hâlinde her durumda önce Bakanlığa şikâyet başvurusu yapılması gerekir; bu yol tüketilmeden dava açılamaz ve mükellef bu aşamada doğrudan yargıya başvuramaz',
            'E': 'Düzeltme talebi dava açma süresi içinde reddedilmişse mükellef, kalan süre içinde vergi mahkemesinde dava açabilir; şikâyet yolu süre geçtikten sonraki redler içindir',
        },
        'E',
        '**VUK m. 124** şikâyet yolunu **dava açma süresi geçtikten sonra** reddolunan düzeltme talepleri için öngörür. Süre henüz dolmamışsa mükellefin yolu **m. 377** uyarınca vergi mahkemesinde dava açmaktır.',
    ),
    # düzey 3
    '0034': patch(
        'Bir mükellef önce uzlaşmaya başvurmuş, uzlaşma sağlanamayınca dava açmıştır; bir başka mükellef ise uzlaşma sağladıktan sonra aynı hususu dava konusu yapmak istemektedir. Buna göre vergi uyuşmazlıklarının çözüm yolları ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'İdari çözüm yollarına başvurulması, aynı uyuşmazlık için yargı yoluna gitme hakkını istisnasız biçimde ortadan kaldırır',
            'B': 'Dava açma süresi geçtikten sonra reddolunan düzeltme taleplerinde şikâyet yoluna başvurulabilir ve bu nedenle uzlaşma tutanağı imzalanmasa dahi dava açılamaz',
            'C': 'Vergi hatalarının düzeltilmesi idari çözüm yollarındandır',
            'D': 'Uzlaşma, vergi uyuşmazlıklarının idari aşamada çözümüne yönelik bir yoldur',
            'E': 'Yargısal çözüm yolunda ilk derece mercii vergi mahkemesidir',
        },
        'A',
        "İdari çözüm yolları ile yargı yolu birbirini tümüyle dışlamaz: uzlaşmanın sağlanamaması hâlinde dava hakkı sürer (**VUK m. 377**); yalnız **uzlaşma sağlandığında** uzlaşılan hususlar dava konusu yapılamaz. 'Her hâlde ortadan kaldırır' ifadesi bu nedenle yanlıştır.",
    ),
    # düzey 2
    '0035': patch(
        'Vergi cezalarında sorumluluk ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Ölüm hâlinde vergi cezası düşer ancak vergi aslı mirasçılara intikal eder.\n\nII. Velayet altındakiler, velinin aykırı hareketlerinden dolayı cezaya muhatap tutulur.\n\nIII. Mücbir sebebin ispatı hâlinde de vergi cezası kesilir.',
        {
            'A': 'I ve II',
            'B': 'Yalnız III',
            'C': 'Yalnız I',
            'D': 'Yalnız II',
            'E': 'II ve III',
        },
        'C',
        '**I doğru:** m. 372 cezayı düşürür; vergi aslı borç olarak intikal eder. **II yanlış:** m. 332 uyarınca velayet altındakiler **cezaya muhatap tutulmazlar**. **III yanlış:** m. 373 uyarınca mücbir sebebin ispatı hâlinde **ceza kesilmez**.',
    ),
    # düzey 3
    '0036': patch(
        'Bir bölge idare mahkemesi, istinaf incelemesi sonunda ilk derece mahkemesi kararını kaldırarak işin esası hakkında yeniden karar vermiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'İstinaf üzerine verilen kararlara karşı yeniden istinaf yoluna başvurulabilir; kanun yolu sayısında bir sınır bulunmaz',
            'B': 'Bölge idare mahkemesi istinaf incelemesinde yalnız kararı bozup dosyayı geri gönderebilir; esas hakkında karar veremeyeceğinden işlem hatalıdır',
            'C': 'Bölge idare mahkemesi kararlarının tamamı temyize tabidir; kanunda bir sınırlama bulunmadığından her karar Danıştaya taşınabilir',
            'D': 'Bölge idare mahkemesinin istinaf üzerine verdiği karar kural olarak kesindir; ancak kanunda sayılan davalarda Danıştayda temyiz yolu açıktır',
            'E': 'İstinaf kararına karşı yalnız yargılamanın yenilenmesi istenebilir; temyiz yolu vergi uyuşmazlıklarında kapalıdır',
        },
        'D',
        '**İYUK m. 45** istinaf mercii olarak bölge idare mahkemesini gösterir ve kararlarının kural olarak kesin olduğunu düzenler; **m. 46** ise **kanunda sayılan davalar** bakımından Danıştayda temyiz yolunu açık tutar.',
    ),
    # düzey 2
    '0037': patch(
        'Bir mükellef, tarh işleminin yetki ve şekil yönünden hukuka aykırı olduğunu ileri sürerek iptalini istemektedir. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'İptal davası yalnız düzenleyici işlemlere karşı açılabilir; bireysel tarh işlemlerine karşı bu yola başvurulamaz',
            'B': 'İptal davası, idari işlemlerin hukuka aykırılıkları nedeniyle iptali için açılır',
            'C': 'İlgililer iptal ve tam yargı davalarını birlikte açabilirler',
            'D': 'İptal davası açabilmek için menfaatin ihlal edilmiş olması gerekir',
            'E': 'İptal davasında hukuka aykırılık yetki, şekil, sebep, konu ve maksat yönlerinden incelenir ve bu nedenle sebep ve maksat unsurları yargısal denetimin dışında kalır',
        },
        'A',
        '**İYUK m. 2/1-a** iptal davasını **idari işlemler** hakkında düzenler; birel (bireysel) işlemler de iptal davasına konu olur. Tarh işlemi tipik bir birel idari işlemdir.',
    ),
    # düzey 2
    '0038': patch(
        'Bir mükellef, hakkındaki işlemin iptalini isterken bir başka mükellef bu işlem nedeniyle uğradığı zararın giderilmesini talep etmektedir. İki talebin dava türü bakımından farkı sorulmaktadır. Buna göre idari dava türleri ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'İlgililer iptal ve tam yargı davalarını birlikte açabilirler',
            'B': 'İptal davası, idari işlemlerin hukuka aykırılıkları nedeniyle iptali için açılır',
            'C': 'Tam yargı davası, idari işlemin yalnızca hukuka uygunluk denetiminin yapılmasını sağlayan dava türüdür',
            'D': 'İptal davasında hukuka aykırılık yetki, şekil, sebep, konu ve maksat yönlerinden incelenir',
            'E': 'İptal davası açabilmek için menfaatin ihlal edilmiş olması gerekir',
        },
        'C',
        '**İYUK m. 2/1-b:** tam yargı davası, idari eylem ve işlemlerden dolayı **kişisel hakları doğrudan muhtel olanlar tarafından açılan** davadır; konusu **hakkın yerine getirilmesi veya zararın giderilmesidir**, salt hukuka uygunluk denetimi değildir.',
    ),
    # düzey 3
    '0039': patch(
        'Bir mükellef, hakkında yapılan tarhiyata karşı hem işlemin iptalini hem de bu işlem nedeniyle uğradığı zararın giderilmesini istemektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Vergi uyuşmazlıklarında tam yargı davası açılamaz; zarar iddiaları adli yargıda ileri sürülebileceğinden idari yargıda incelenmez',
            'B': 'İlgililer haklarını ihlal eden bir idari işlem dolayısıyla doğrudan doğruya tam yargı davası veya iptal ve tam yargı davalarını birlikte açabilirler',
            'C': 'Tam yargı davası ancak iptal davası kesin hükümle sonuçlandıktan sonra açılabilir; önce açılan tam yargı davaları erken sayılır',
            'D': 'İptal ve tam yargı davalarının birlikte açılması yalnız Danıştayda mümkündür; ilk derece mahkemelerinde ayrı ayrı açılır',
            'E': 'İptal ve tam yargı davaları birlikte açılamaz; her biri için ayrı dava açılması gerektiğinden tek dilekçeyle yapılan başvuru dilekçe ret kararıyla sonuçlanır',
        },
        'B',
        '**İYUK m. 12:** ilgililer haklarını ihlal eden bir idari işlem dolayısıyla **doğrudan doğruya tam yargı davası veya iptal ve tam yargı davalarını birlikte** açabilecekleri gibi, önce iptal davası açıp bu davanın karara bağlanması üzerine de tam yargı davası açabilirler.',
    ),
    # düzey 2
    '0040': patch(
        'Vergi yargısında kanun yolları ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İdare ve vergi mahkemesi kararlarına karşı bölge idare mahkemesine istinaf yoluna başvurulur.\n\nII. Bölge idare mahkemesi kararlarının tamamı Danıştayda temyiz edilebilir.\n\nIII. Temyiz istemleri Danıştay Başkanlığına hitaben yazılmış dilekçelerle yapılır.',
        {
            'A': 'Yalnız II',
            'B': 'I, II ve III',
            'C': 'I ve III',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'C',
        '**I doğru:** m. 45. **III doğru:** m. 48/1. **II yanlış:** **m. 46** temyizi bölge idare mahkemesinin **kanunda sayılan davalar** hakkındaki kararlarıyla sınırlar; kararların tamamı temyize açık değildir.',
    ),
    # düzey 3
    '0041': patch(
        'Bir mükellef, vergi mahkemesinde dava açarken yürütmenin durdurulmasını da talep etmiştir. Mahkeme işlemin açıkça hukuka aykırı olduğunu ancak uygulanması hâlinde telafisi güç bir zarar doğmayacağını saptamıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Vergi davalarında yürütmenin durdurulması istemi incelenmez; tahsil işlemleri zaten dava süresince durduğundan talebin konusu kalmaz',
            'B': 'Yürütmenin durdurulmasına karar verilebilmesi için hukuka aykırılık ile telafisi güç veya imkânsız zarar şartlarının birlikte gerçekleşmesi gerektiğinden istem reddedilir',
            'C': 'Zarar şartı gerçekleşmese dahi mahkeme kendiliğinden yürütmeyi durdurabilir; kanun mahkemeye bu konuda serbestlik tanımıştır',
            'D': 'Hukuka aykırılık saptandığından yürütmenin durdurulmasına karar verilmesi zorunludur; zarar şartı ayrıca aranmadığından istem kabul edilir ve mahkeme zarar unsurunu ayrıca değerlendirmeksizin karar vermek durumunda kalır',
            'E': 'Yürütmenin durdurulması istemi hakkında karar verilebilmesi için davanın esastan sonuçlanması beklenir; bu aşamada karar verilemez',
        },
        'B',
        '**İYUK m. 27/2:** yürütmenin durdurulmasına, **idari işlemin uygulanması hâlinde telafisi güç veya imkânsız zararların doğması** ve **idari işlemin açıkça hukuka aykırı olması** şartlarının **birlikte** gerçekleşmesi durumunda karar verilir.',
    ),
    # düzey 2
    '0042': patch(
        "Bir mükellefe ihbarname 3 Mart'ta düzenlenmiş, 10 Mart'ta tebliğ edilmiştir. Mükellef sürenin hangi tarihten işlediğini ve üst makama başvurunun süreye etkisini sormaktadır. Buna göre vergi uyuşmazlıklarında süreler ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
        {
            'A': 'Vergi mahkemesinde dava açma süresi, ihbarnamenin düzenlendiği tarihten itibaren işlemeye başlar',
            'B': 'Vergi mahkemelerinde dava açma süresi kural olarak otuz gündür',
            'C': 'Danıştayda ve idare mahkemelerinde dava açma süresi altmış gündür',
            'D': 'İdari makama yapılan başvuruya altmış gün içinde cevap verilmezse istek reddedilmiş sayılır',
            'E': 'Dava açma süresi içinde üst makama başvurulması işlemeye başlamış süreyi durdurur',
        },
        'A',
        "Dava açma süresi, işlemin **tebliğ edildiği** tarihi izleyen günden itibaren işler; ihbarnamenin düzenlenme tarihi süre başlangıcı değildir. Süreler **İYUK m. 7**'de düzenlenmiştir.",
    ),
    # düzey 3
    '0043': patch(
        'Bir mükellef hakkında, defter tasdik ettirmemek fiili nedeniyle usulsüzlük cezası; bundan bağımsız olarak matrahı eksik beyan etmek fiili nedeniyle de vergi ziyaı cezası kesilmiştir. Mükellef, iki cezadan yalnız ağır olanının uygulanması gerektiğini ileri sürmektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Usulsüzlük cezası vergi ziyaı cezasının içinde eridiğinden yalnız ziyaı cezası kesilir; şekli ihlaller ayrıca cezalandırılmaz',
            'B': 'İki ceza kesilir ancak mükellef bunlardan dilediğini ödeyerek diğerinden kurtulur; seçim hakkı mükellefe tanınmıştır',
            'C': 'Cezalar her hâlde birleştirilir ve yalnız en ağırı kesilir; fiillerin ayrı olması sonucu değiştirmediğinden mükellefin iddiası yerindedir',
            'D': 'Ayrı fiillerden doğan cezalar toplanır ancak toplam tutar yarı oranında indirilir; kanun bu hâl için özel bir indirim öngörmüştür',
            'E': 'Cezaların birleştirilmesi tek bir fiille her iki ihlalin birlikte işlenmesine bağlı olduğundan, ayrı fiillerden doğan bu cezalar ayrı ayrı kesilir ve mükellefin iddiası yerinde değildir',
        },
        'E',
        "**VUK m. 336** cezaların birleştirilmesini **'cezayı istilzam eden tek bir fiil ile'** vergi ziyaı ve usulsüzlüğün birlikte işlenmesi şartına bağlar. Olayda iki ayrı fiil bulunduğundan hüküm uygulanmaz; her fiil kendi cezasını doğurur.",
    ),
    # düzey 2
    '0044': patch(
        'Vergi uyuşmazlıklarının çözüm yolları ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Uzlaşmaya başvurmuş olmak vergi mahkemesinde dava açmanın ön şartıdır.\n\nII. Dava açma süresi geçtikten sonra reddolunan düzeltme taleplerinde şikâyet yoluna başvurulabilir.\n\nIII. İdari çözüm yollarına başvurulması yargı yolunu her hâlde kapatır.',
        {
            'A': 'Yalnız III',
            'B': 'Yalnız I',
            'C': 'Yalnız II',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'C',
        '**II doğru:** VUK m. 124. **I yanlış:** m. 377-378 dava hakkını uzlaşma şartına bağlamaz. **III yanlış:** uzlaşmanın sağlanamaması hâlinde dava hakkı sürer; yalnız **uzlaşma sağlandığında** uzlaşılan hususlar dava konusu yapılamaz.',
    ),
    # düzey 2
    '0045': patch(
        'Bir vergi mahkemesi mükellef lehine karar vermiş, karar kesinleşmiş; ancak idare aylardır kararın gereğini yerine getirmemiştir. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'İdarenin bu yükümlülüğü kanunla düzenlenmiştir',
            'B': 'İdare, yargı kararının gereğini yerine getirip getirmemekte takdir yetkisine sahiptir',
            'C': 'Mahkemelerin esasa ilişkin kararlarının icaplarına göre idare gecikmeksizin işlem tesis etmekle yükümlüdür',
            'D': 'Yargı kararlarının uygulanmaması hukuki sonuçlar doğurur',
            'E': 'Yürütmenin durdurulmasına ilişkin kararlar bakımından da idarenin aynı yükümlülüğü bulunur',
        },
        'B',
        '**İYUK m. 28/1:** mahkemelerin **esasa ve yürütmenin durdurulmasına ilişkin kararlarının icaplarına göre idare, gecikmeksizin işlem tesis etmeye veya eylemde bulunmaya mecburdur.** Takdir yetkisinden söz edilemez.',
    ),
    # düzey 3
    '0046': patch(
        'Bir mükellef, kendisine tebliğ edilen ödeme emrine karşı değil; ödeme emrinin dayanağı olan tarh işlemine karşı, tarhiyat ihbarnamesinin tebliğinden bir yıl sonra dava açmıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Tarh işlemine karşı dava süresi altmış gündür; vergi mahkemeleriyle idare mahkemeleri arasında bir fark bulunmadığından süre henüz dolmamıştır',
            'B': 'Tarh işlemine karşı dava açma süresi ihbarnamenin tebliğinden itibaren otuz gün olduğundan süre dolmuş; bu aşamada tarhiyat kesinleşmiş sayılır',
            'C': 'Ödeme emri tebliğ edildiğinden tarh işlemine karşı dava açma süresi yeniden başlar; mükellef otuz gün daha kazanır',
            'D': 'Tarh işlemine karşı dava her zaman açılabilir; tahsil aşamasına gelinmiş olması dava hakkını etkilemediğinden başvuru incelenir',
            'E': 'Tarh işlemine karşı dava süresi altmış gün olduğundan süre henüz dolmamıştır; mahkeme işin esasını inceler',
        },
        'B',
        "**İYUK m. 7/1** vergi mahkemelerinde süreyi **otuz gün** olarak belirler. Süresinde dava açılmayan tarhiyat kesinleşir; sonraki tahsil aşamasında ancak **6183 m. 58**'deki sınırlı sebeplerle ödeme emrine karşı dava açılabilir.",
    ),
    # düzey 3
    '0047': patch(
        'Bir mükellef, vergi dairesinden aldığı özelgeye uygun hareket etmiş; ancak sonradan yapılan incelemede bu görüşün mevzuata aykırı olduğu saptanmıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Özelge yalnız kendisine verildiği mükellefi değil bütün mükellefleri bağlar; bu nedenle idare görüşünü sonradan değiştiremez',
            'B': 'Özelgeye aykırı tarhiyat yapılabilmesi için önce özelgenin mahkemece iptal edilmesi gerekir; iptal olmadan işlem tesis edilemez',
            'C': 'Özelgeye uygun hareket eden mükelleften vergi aslı da aranmaz; idarenin görüşü mükellefe kazanılmış hak sağladığından tarhiyat yapılamaz',
            'D': 'Özelgeye uygun hareket edilmiş olması hiçbir koruma sağlamaz; hem vergi aslı hem ceza aranacağından mükellef tam sorumludur',
            'E': 'İdareden alınan izahata uygun hareket eden mükellefe ceza kesilmez; ancak eksik ödenen vergi aslı ile buna bağlı gecikme faizi aranmaya devam eder',
        },
        'E',
        '**VUK m. 413** izahat isteme hakkını düzenler; **m. 369** ise yetkili makamların verdiği izahata göre hareket eden mükelleflere **ceza kesilmeyeceğini** öngörür. Vergi aslı ve gecikme faizi bu korumanın dışındadır.',
    ),
    # düzey 2
    '0048': patch(
        'Bir vergi davasında mahkeme, taraflarca sunulmayan bilgi ve belgelere ihtiyaç duymuştur. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Mahkemeler gerekli gördükleri belgeleri ilgili yerlerden de isteyebilir',
            'B': "Mahkemeler bakmakta oldukları davalara ait her türlü incelemeyi kendiliğinden yapar ve bu nedenle idari yargıda re'sen araştırma ilkesinden söz edilemez",
            'C': 'Mahkeme yalnız tarafların sunduğu delillerle bağlıdır; kendiliğinden inceleme yapma yetkisi bulunmadığından eksik bilgiyle karar verir',
            'D': 'Mahkemeler gerekli gördükleri belgelerin gönderilmesini taraflardan isteyebilir',
            'E': "Re'sen araştırma ilkesi idari yargılama usulünde kanunla düzenlenmiştir",
        },
        'C',
        "**İYUK m. 20/1:** mahkemeler bakmakta oldukları davalara ait **her türlü incelemeyi kendiliğinden yapar**; re'sen araştırma ilkesi idari yargının temel özelliklerindendir.",
    ),
    # düzey 2
    '0049': patch(
        'Vergi cezalarının kesilmesi ve düşmesi ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Vergi ziyaı cezasında ceza kesme zamanaşımı süresi beş yıldır.\n\nII. Ölüm hâlinde vergi cezası düşer.\n\nIII. Tek fiille vergi ziyaı ve usulsüzlük birlikte işlenmişse her iki ceza da ayrı ayrı kesilir.',
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'I, II ve III',
            'D': 'I ve II',
            'E': 'Yalnız III',
        },
        'D',
        '**I doğru:** m. 374/1. **II doğru:** m. 372. **III yanlış:** **m. 336** uyarınca bu hâlde cezalardan **sadece miktar itibarıyla en ağırı** kesilir.',
    ),
    # düzey 3
    '0050': patch(
        'Bir mükellef, dava açma süresi içinde işlemin geri alınması istemiyle üst makama başvurmuş; başvurusu reddedilmiştir. Buna göre dava açma süresi bakımından aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Üst makama başvuru işlemeye başlamış olan dava açma süresini durdurduğundan, başvurunun reddi üzerine sürenin durmadan önce kalan kısmı yeniden işlemeye başlar',
            'B': 'Başvurunun reddi hâlinde dava yolu kapanır; idari başvuru yolunu seçen ilgili yargı yolundan feragat etmiş sayılır',
            'C': 'Üst makama başvuru dava açma süresini kesintiye uğratır ve ret tarihinden itibaren altmış günlük yeni bir süre başlar',
            'D': 'Üst makama başvuru süreyi hiç etkilemediğinden mükellefin ayrıca ilk tebliğ tarihinden itibaren süresinde dava açmış olması gerekirdi ve mükellef bu suretle ilk tebliğden bağımsız yeni bir hak kazanır',
            'E': 'Başvurunun reddi üzerine dava açma süresi baştan otuz gün olarak yeniden işler; durmadan önce geçen günler hesaba katılmaz',
        },
        'A',
        '**İYUK m. 11:** dava açma süresi içinde üst makama başvuru **işlemeye başlamış olan dava açma süresini durdurur.** İsteğin reddi hâlinde dava açma süresi **kaldığı yerden** işlemeye devam eder.',
    ),
    # düzey 2
    '0051': patch(
        'Vergi yargısında yürütmenin durdurulması ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Dava açılması dava edilen idari işlemin yürütülmesini kendiliğinden durdurmaz.\n\nII. Yürütmenin durdurulması için hukuka aykırılık ve telafisi güç zarar şartları birlikte aranır.\n\nIII. Yürütmenin durdurulması kararları gerekçesiz olarak verilebilir.',
        {
            'A': 'I, II ve III',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'Yalnız III',
            'E': 'Yalnız I',
        },
        'C',
        '**I doğru:** m. 27/1. **II doğru:** m. 27/2. **III yanlış:** aynı madde yürütmenin durdurulması kararlarının **gerekçeli** olarak verilmesini öngörür.',
    ),
    # düzey 3
    '0052': patch(
        'Bir mükellefin düzeltme talebi vergi dairesince reddedilmiş; mükellef dava açma süresi geçtikten sonra şikâyet yoluyla Bakanlığa başvurmuş, bu başvurusu da reddedilmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Şikâyet başvurusunun reddine karşı yalnız Danıştaya doğrudan başvurulabilir; vergi mahkemesinin görev alanına girmez',
            'B': 'Şikâyet başvurusu reddedilse dahi mükellef aynı talebi sınırsız sayıda yenileyebilir; her yenileme yeni bir süre doğurur',
            'C': 'Şikâyet başvurusu yapılmışsa artık düzeltme talebinde bulunulamaz; iki yol birbirini dışladığından mükellefin seçimi kesindir',
            'D': 'Şikâyet başvurusunun reddiyle bütün başvuru yolları tükenir; ret işlemi kesin olduğundan yargıya gidilemez',
            'E': 'Şikâyet başvurusunun reddi üzerine mükellef, bu ret işlemine karşı vergi mahkemesinde dava açabilir; şikâyet yolu yargı yolunu kapatmaz',
        },
        'E',
        '**VUK m. 124** şikâyet yolunu düzenler; şikâyet başvurusunun **reddi de idari bir işlem** olduğundan **İYUK m. 2** uyarınca iptal davasına konu edilebilir ve **m. 7** süresi içinde vergi mahkemesinde dava açılabilir.',
    ),
    # düzey 2
    '0053': patch(
        'Bir mükellef idareden aldığı özelgeye uygun hareket etmiş; sonradan bu görüşün mevzuata aykırı olduğu anlaşılınca hem vergi hem ceza aranıp aranamayacağını sormaktadır. Buna göre vergi uyuşmazlıklarının idari çözüm yolları ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Mükellefin idareden izahat istemesi hâlinde verilen görüş, o mükellef bakımından vergi aslını da ortadan kaldırır',
            'B': 'Vergi hatalarının düzeltilmesi vergi dairesinden yazı ile istenebilir',
            'C': 'Dava açma süresi geçtikten sonra reddolunan düzeltme taleplerinde şikâyet yoluna gidilebilir ve süre geçtikten sonra yapılan başvurular incelenmeksizin reddedilir',
            'D': 'Alınan izahata uygun hareket eden mükellefe ceza kesilmez',
            'E': 'Mükellefler tereddüde düştükleri hususlarda idareden izahat isteyebilirler',
        },
        'A',
        '**VUK m. 369** izahata uygun hareket edenlere **ceza kesilmemesini** öngörür; vergi aslı ve buna bağlı gecikme faizi bu korumanın dışındadır. Vergi aslını da ortadan kaldırdığını söyleyen ifade yanlıştır.',
    ),
    # düzey 3
    '0054': patch(
        'Bir mükellef, hakkında kesilen cezaya karşı hem cezada indirim talebinde bulunmuş hem de aynı ceza için vergi mahkemesinde dava açmıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'İndirim yalnız dava açıldıktan sonra istenebilir; dava açılmadan yapılan başvurular erken sayılarak reddedilir',
            'B': 'Cezada indirim uygulamasından yararlanmak, ihbarnamenin tebliğinden itibaren otuz gün içinde başvurup ödeme taahhüdünde bulunmayı gerektirir; bu yol ile dava yolu birlikte işletilemez',
            'C': 'İndirim talebi ile dava birlikte yürütülebilir; iki yol birbirini etkilemediğinden mükellef her ikisinden de yararlanır ve idare her iki başvuruyu da ayrı ayrı sonuçlandırmakla yükümlü kalır',
            'D': 'İndirim talebi dava açma süresini durdurur; dava daha sonra kalan süre içinde açılabileceğinden çakışma doğmaz',
            'E': 'İndirim talebi vergi aslını da kapsar; bu nedenle mükellef hem vergi hem ceza bakımından indirimden yararlanır',
        },
        'B',
        '**VUK m. 376** indirim için ihbarnamelerin tebliğinden itibaren **otuz gün içinde** başvurup ödeme taahhüdünde bulunulmasını arar. İndirim, uyuşmazlığı idari aşamada sona erdirmeye yönelik bir yoldur; aynı ceza için dava yoluyla birlikte işletilmesi amaçla bağdaşmaz.',
    ),
    # düzey 2
    '0055': patch(
        'Bir mükellef, tarh edilen vergiye ve kesilen cezaya karşı hangi yargı yerinde dava açacağını belirlemek istemektedir. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Vergi mahkemesi kararlarına karşı bölge idare mahkemesine istinaf yoluna başvurulur',
            'B': 'Mükellefler tarh edilen vergilere karşı vergi mahkemesinde dava açar',
            'C': 'Kendilerine ceza kesilenler de kesilen cezalara karşı vergi mahkemesinde dava açabilir ve tarhiyata ilişkin davalar bu nedenle idare mahkemesinde görülür',
            'D': 'Vergi uyuşmazlıkları ilk derecede idare mahkemesinde görülür; vergi mahkemesi yalnız istinaf mercii olarak görev yapar',
            'E': 'Bölge idare mahkemesinin kanunda sayılan kararları Danıştayda temyiz edilebilir',
        },
        'D',
        '**VUK m. 377** dava mercii olarak **vergi mahkemesini** gösterir; vergi mahkemesi ilk derece mahkemesidir. İstinaf mercii **İYUK m. 45** uyarınca bölge idare mahkemesidir.',
    ),
    # düzey 2
    '0056': patch(
        'Vergi yargısında kararların yerine getirilmesi ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İdare, kararın gereğini yerine getirip getirmemekte takdir yetkisine sahiptir.\n\nII. İdare, mahkeme kararlarının icaplarına göre gecikmeksizin işlem tesis etmekle yükümlüdür.\n\nIII. Bu yükümlülük yalnız iptal kararları bakımından geçerli olup yürütmenin durdurulması kararlarını kapsamaz.',
        {
            'A': 'II ve III',
            'B': 'Yalnız II',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'Yalnız III',
        },
        'B',
        '**II doğru:** m. 28/1. **I yanlış:** takdir yetkisi yoktur. **III yanlış:** aynı fıkra yükümlülüğü **esasa ve yürütmenin durdurulmasına ilişkin** kararların her ikisi için de öngörür.',
    ),
    # düzey 3
    '0057': patch(
        'Bir mükellef adına kesilen vergi ziyaı cezasının bağlı olduğu vergi alacağı 2022 takvim yılında doğmuştur. İdare cezayı 2026 yılının Mart ayında kesmiş; mükellef zamanaşımı itirazında bulunmuştur. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': "Süre alacağın doğduğu 2022'den itibaren işlediğinden 31 Aralık 2026'da dolar; ceza yine de süresinde kesilmiş sayılır ancak hesap farklıdır ve bu nedenle idarenin 2026 yılında ceza kesmesi zamanaşımı yönünden hukuka aykırı olur",
            'B': 'Ceza kesme zamanaşımı üç yıl olduğundan süre dolmuştur; mükellefin itirazı yerindedir ve ceza kaldırılmalıdır',
            'C': 'Ceza kesme zamanaşımı yoktur; idare her zaman ceza kesebileceğinden itirazın incelenmesine gerek kalmaz',
            'D': 'Süre cezanın kesildiği tarihten işlediğinden henüz başlamamıştır; bu nedenle zamanaşımı tartışması konusuz kalır',
            'E': "Ceza kesme zamanaşımı 2023 yılının birinci gününden başlayarak beş yıl işleyeceğinden süre 31 Aralık 2027'de dolar; 2026 Mart'taki ceza süresinde kesilmiştir",
        },
        'E',
        "**VUK m. 374/1:** vergi ziyaı cezasında süre, cezanın bağlı olduğu **vergi alacağının doğduğu takvim yılını takip eden yılın birinci gününden** başlar. 2022'de doğan alacakta süre 1 Ocak 2023'te başlar ve beş yıl sonra 31 Aralık 2027'de dolar.",
    ),
    # düzey 2
    '0058': patch(
        'Bir mükellef, özel kanununda otuz günden farklı bir dava süresi öngörülen bir işleme karşı vergi mahkemesinde dava açacaktır. Buna göre vergi uyuşmazlıklarında dava açma süresi ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Özel kanunlarda ayrı bir süre öngörülmüş olsa dahi vergi mahkemelerinde istisnasız otuz günlük genel süre uygulanır',
            'B': 'Danıştayda ve idare mahkemelerinde bu süre altmış gündür',
            'C': 'Dava açma süresi özel kanunlarında ayrı süre gösterilmeyen hâllerde vergi mahkemelerinde otuz gündür ve özel kanunlardaki farklı süreler vergi yargısında uygulanmaz',
            'D': 'Dava açma süresi içinde üst makama başvurulması süreyi durdurur',
            'E': 'Sürenin geçirilmesi hâlinde dava süre yönünden reddedilir',
        },
        'A',
        '**İYUK m. 7/1** süreyi **özel kanunlarında ayrı süre gösterilmeyen hâllerde** belirler; özel kanunda farklı bir süre varsa **o süre uygulanır**. Genel sürenin her hâlde uygulanacağını söyleyen ifade yanlıştır.',
    ),
    # düzey 2
    '0059': patch(
        'Bir mükellef, ödevini yerine getirememesine yol açan mücbir sebebi ispatlamış; ayrıca aynı dosyada ölüm ve velayet altındaki kişilere ilişkin ceza sorunları da gündeme gelmiştir. Buna göre vergi cezalarında sorumluluk ve düşme ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Tek fiille vergi ziyaı ve usulsüzlük birlikte işlenmişse en ağır ceza kesilir',
            'B': 'Velayet altındakiler, velinin aykırı hareketlerinden dolayı cezaya muhatap tutulmazlar',
            'C': 'Mücbir sebebin varlığı yalnız süreleri durdurur; vergi cezasının kesilmesine engel oluşturmaz',
            'D': 'Mücbir sebebin ispatı hâlinde vergi cezası kesilmez',
            'E': 'Ölüm hâlinde vergi cezası düşer',
        },
        'C',
        '**VUK m. 373:** mücbir sebeplerden birinin vukua geldiği malûm ise veya ispat olunursa **vergi cezası kesilmez.** Mücbir sebep hem süreleri durdurur (m. 15) hem de ceza kesilmesine engel olur.',
    ),
    # düzey 3
    '0060': patch(
        "Bir mükellefe 5 Mayıs'ta vergi/ceza ihbarnamesi tebliğ edilmiştir. Mükellef 15 Mayıs'ta işlemin kaldırılması istemiyle üst makama başvurmuş; başvuru 25 Mayıs'ta reddedilmiştir. Buna göre dava açma süresi bakımından aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': 'Ret üzerine mükellefe otuz günlük yeni bir süre tanınır; durmadan önce geçen günler dikkate alınmaz',
            'B': 'Üst makama başvuru dava açma hakkını ortadan kaldırdığından mükellef artık dava açamaz',
            'C': 'Süre yalnız ret kararının tebliğinden itibaren altmış gün olarak işler; vergi uyuşmazlıklarında genel süre uygulanır ve bu nedenle vergi uyuşmazlıklarında idare mahkemesiyle aynı süre işler',
            'D': "Süre 5 Mayıs'ı izleyen günden işlemeye başlamış, 15 Mayıs'taki başvuruyla durmuş ve 25 Mayıs'taki ret üzerine kalan süre yeniden işlemeye başlamıştır",
            'E': "Üst makama başvuru süreyi etkilemediğinden dava açma süresi kesintisiz işlemiş ve 4 Haziran'da dolmuştur",
        },
        'D',
        '**İYUK m. 11:** dava açma süresi içinde üst makama başvuru **işlemeye başlamış süreyi durdurur**; isteğin reddi hâlinde süre **kaldığı yerden** işler. Vergi mahkemesinde süre **m. 7/1** uyarınca otuz gündür.',
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
    print(f"1 paket / {len(PATCHES)} soru ('Vergi Uyusmazliklari ve Yargi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
