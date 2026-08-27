#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vergi Usul Kanunu — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Tanim kalibindan olay + kural uygulamasina: medyan kok 65->237, olumsuz kok %0->%32, kor ogrenci %25. Kapsam vergilendirme_sureci ile cakismayacak sekilde daraltildi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: VUK m. 8-11, 13-18, 127, 134, 135, 139, 142, 148, 153, 172, 176-180, 220, 221, 229, 231, 232, 235, 236, 253, 256, 258, 262, 265-267, 281, 313, 315, mukerrer 315, 320, 322-324, 339, 341, 344, 351-353, 359, 376 (resmi metinden dogrulandi)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/vergi_hukuku/vergi_usul_kanunu.json"
STYLE_REF = "SGS Hukuk (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "vuk-gen-"


def patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": '213 sayili Vergi Usul Kanunu'},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'On beş yaşındaki bir kişi, kendisine miras kalan bir dükkânı kiraya vererek düzenli kira geliri elde etmeye başlamıştır. Vergi dairesi bu kişi adına mükellefiyet tesis etmiş; kanuni temsilcisi ise küçüğün fiil ehliyeti bulunmadığını ileri sürerek mükellefiyete itiraz etmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Mükellefiyet için ehliyet aranmaz ancak vergi sorumluluğu için aranır; bu nedenle küçük mükellef olur, temsilcinin bir ödevi doğmaz',
            'B': 'Küçükler bakımından mükellefiyet ancak sulh hukuk mahkemesinin izniyle tesis edilebilir; izin alınmadığından tarhiyat geçersizdir',
            'C': 'Mükellefiyet ve vergi sorumluluğu için kanuni ehliyet şart olmadığından küçük adına mükellefiyet tesisi hukuka uygundur; ödevler kanuni temsilci tarafından yerine getirilir',
            'D': 'Küçüğün geliri kanuni temsilcisinin geliri sayılır ve onun matrahına eklenir; bu nedenle küçük adına ayrı bir mükellefiyet kaydı açılmaz',
            'E': 'Fiil ehliyeti bulunmayan kişiler adına mükellefiyet tesis edilemez; vergi ancak ehliyetli kişilerden alınabildiğinden işlem iptal edilmelidir ve küçük adına yapılan tarhiyat baştan itibaren geçersiz sayılarak terkin edilir',
        },
        'C',
        '**VUK m. 9/1:** mükellefiyet ve vergi sorumluluğu için **kanuni ehliyet şart değildir.** **m. 10** uyarınca küçüklerin ve kısıtlıların vergi ödevleri **kanuni temsilcileri** tarafından yerine getirilir.',
    ),
    # düzey 3
    '0002': patch(
        'Bir limited şirketin vergi borçları, şirket malvarlığından tahsil edilememiştir. Vergi dairesi, ödevlerin yerine getirilmemesinden doğan bu borçlar için şirket müdürüne başvurmuştur. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Tüzel kişinin borcundan kanuni temsilci sorumlu tutulamaz; sorumluluk tüzel kişiliğin malvarlığıyla sınırlı olduğundan şirketten tahsil edilemeyen alacak için takip düşer ve borç terkin edilir',
            'B': 'Tüzel kişilerde vergi ödevlerini ortaklar yerine getirir; müdürün bu konuda bir ödevi bulunmadığından sorumluluğu da doğmaz',
            'C': 'Kanuni temsilci ancak kendisi hakkında ayrıca ceza davası açılmışsa sorumlu tutulur; ceza yargılaması olmadan mal varlığına başvurulamaz',
            'D': 'Kanuni temsilcinin sorumluluğu yalnız ortaklık payı oranındadır; müdür payı kadar sorumlu olduğundan aşan kısım için takip yapılamaz',
            'E': 'Tüzel kişilerin vergi ödevleri kanuni temsilcilerince yerine getirilir; bu ödevlerin yerine getirilmemesi yüzünden tüzel kişiden alınamayan vergiler kanuni temsilcilerin varlıklarından alınır',
        },
        'E',
        '**VUK m. 10:** tüzel kişilerin vergi ödevleri **kanuni temsilcileri** tarafından yerine getirilir ve bu ödevlerin yerine getirilmemesi yüzünden **mükelleflerin varlığından tamamen veya kısmen alınamayan vergi ve buna bağlı alacaklar, kanuni ödevleri yerine getirmeyenlerin varlıklarından alınır.**',
    ),
    # düzey 2
    '0003': patch(
        'Bir vergi dairesi, aynı dosyada hem verginin asıl borçlusu hem de kesinti yaparak vergiyi yatırmakla yükümlü olan kişi bakımından işlem yapmakta; iki sıfatın hukuki sonuçlarını ayırmaya çalışmaktadır. Buna göre vergi mükellefi ve vergi sorumlusu kavramları ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Mükellef, vergi kanunlarına göre kendisine vergi borcu terettüp eden gerçek veya tüzel kişidir',
            'B': 'Vergi sorumlusu, verginin ödenmesi bakımından alacaklı vergi dairesine karşı muhatap olan kişidir',
            'C': 'Vergi sorumlusu, vergi kanunlarına göre kendisine vergi borcu düşen gerçek veya tüzel kişidir',
            'D': 'Mükellefiyet ve vergi sorumluluğu için kanuni ehliyet şart değildir',
            'E': 'Vergi kanunlarıyla kabul edilen hâller dışında mükellefiyete ilişkin özel sözleşmeler vergi dairesini bağlamaz',
        },
        'C',
        '**VUK m. 8:** **mükellef**, kendisine vergi borcu terettüp eden kişidir; **vergi sorumlusu** ise verginin ödenmesi bakımından **alacaklı vergi dairesine karşı muhatap olan** kişidir. Yanlış olan şık, sorumluya mükellefin tanımını vermektedir.',
    ),
    # düzey 2
    '0004': patch(
        'Bir işveren, çalışanlarının ücretlerinden gelir vergisi kesintisi yapmış ancak kestiği vergiyi vergi dairesine yatırmamıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'İşveren yalnız kestiği tutarın yarısından sorumludur; kalan kısım için asıl mükellefe başvurulması gerekir',
            'B': 'Vergi kesintisi yapanlar sorumlu tutulamaz; sorumluluk ancak açık bir sözleşme hükmüyle doğduğundan kanuni bir yükümlülükten söz edilemez ve idare yalnız asıl mükellefe başvurur',
            'C': 'Ödemelerden vergi kesmeye mecbur olanlar, verginin tam olarak kesilip ödenmesinden ve buna ilişkin ödevleri yerine getirmekten sorumludur; kesilen verginin ödenmemesi bu sorumluluğu doğurur',
            'D': 'Kesinti yapan işverenin sorumluluğu yalnız kesintiyi yapmakla sınırlıdır; ödeme yükümlülüğü doğrudan çalışana ait olduğundan kesilen verginin yatırılmaması hâlinde takip çalışana yöneltilir',
            'E': 'Kesilen vergi ödenmediğinde sorumluluk kendiliğinden ortadan kalkar; verginin asıl mükellefi çalışan olduğundan idare yalnız ona başvurabilir',
        },
        'C',
        '**VUK m. 11/1:** yaptıkları veya yapacakları ödemelerden **vergi kesmeye mecbur olanlar**, verginin **tam olarak kesilip ödenmesinden** ve bununla ilgili diğer ödevleri yerine getirmekten sorumludurlar.',
    ),
    # düzey 3
    '0005': patch(
        'Bir mükellefe tanınan ve gün olarak belirlenmiş on beş günlük bir süre, tebliğin yapıldığı 3 Mart günü başlamıştır. Sürenin son günü resmî tatile rastlamaktadır. Buna göre sürenin hesabı bakımından aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Süre gün olarak belli edilmişse başladığı gün hesaba katılmaz ve son günün tatil saatinde biter; son gün resmî tatile rastlarsa süre tatili izleyen ilk iş günü mesai saati sonunda sona erer',
            'B': 'Gün olarak belirlenen sürelerde başlangıç günü hesaba katılmaz ancak tatil günleri süreden düşülür; bu nedenle süre fiilen daha uzun sürer',
            'C': 'Sürelerin hesabı vergi dairesinin takdirine bırakılmıştır; kanunda bir hesap kuralı bulunmadığından idare süreyi belirler',
            'D': 'Sürenin son günü tatile rastlarsa süre kendiliğinden bir hafta uzar; bu suretle mükellefe ek bir çalışma haftası tanınmış olur',
            'E': 'Süre gün olarak belli edilmişse başladığı gün de hesaba katılır; son günün tatile rastlaması sürenin bitimini değiştirmediğinden süre o gün mesai saati sonunda sona erer ve tatile rastlayan son günde yapılan başvurular süresinde sayılmaz',
        },
        'A',
        '**VUK m. 18/1:** süre gün olarak belli edilmişse **başladığı gün hesaba katılmaz** ve son günün tatil saatinde biter. **m. 18/4:** sürenin son günü resmî tatile rastlarsa süre, tatili izleyen ilk iş günü tatil saatinde biter.',
    ),
    # düzey 3
    '0006': patch(
        'Bir mükellef, ağır hastalığı nedeniyle beyannamesini süresinde veremeyeceğini bildirerek vergi dairesinden ek süre istemiştir. Talep, sürenin bitmesinden önce yapılmıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Zor durum nedeniyle verilecek mühletin üst sınırı bulunmaz; idare gerekli gördüğü kadar süre tanıyabileceğinden talep sınırsız karşılanabilir',
            'B': 'Zor durum hâlinde süre kendiliğinden durur ve zor durum ortadan kalkınca kaldığı yerden işlemeye devam eder',
            'C': 'Vergi kanunlarındaki süreler uzatılamaz; kanuni süre emredici olduğundan idarenin mühlet verme yetkisi bulunmaz ve ödev süresinde yerine getirilmediğinde doğrudan ceza kesilir',
            'D': 'Zor durumda bulunmaları nedeniyle ödevlerini süresinde yerine getiremeyecek olanlara kanuni sürenin bir katını geçmemek üzere Maliye Bakanlığınca uygun bir mühlet verilebilir',
            'E': 'Zor durum hâlinde mühlet ancak vergi mahkemesince verilebilir; idarenin bu konuda bir yetkisi olmadığından başvuru mahkemeye yapılmalıdır',
        },
        'D',
        "**VUK m. 17:** zor durumda bulunmaları hasebiyle vergi muamelelerine ilişkin ödevleri süresinde yerine getiremeyecek olanlara, **kanuni sürenin bir katını geçmemek üzere** Maliye Bakanlığınca uygun bir mühlet verilebilir. Sürelerin durması ise **m. 15**'teki mücbir sebebe özgüdür.",
    ),
    # düzey 2
    '0007': patch(
        'Bir mükellefe kanunda süresi açıkça yazılı olmayan bir ödev için süre tanınmış; ayrıca sürenin son gününün resmî tatile rastlaması ve zor durum başvurusu gündeme gelmiştir. Buna göre vergi hukukunda süreler ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Kanunda süresi açıkça yazılı olmayan hâllerde süreyi mükellef kendisi belirler ve vergi dairesine bildirir',
            'B': 'Zor durumda bulunanlara kanuni sürenin bir katını geçmemek üzere mühlet verilebilir',
            'C': 'Süre gün olarak belli edilmişse başladığı gün hesaba katılmaz',
            'D': 'Vergi muamelelerinde süreler kural olarak vergi kanunları ile belli edilir',
            'E': 'Sürenin son günü resmî tatile rastlarsa süre, tatili izleyen ilk iş günü tatil saatinde biter',
        },
        'A',
        '**VUK m. 14/2:** kanunda açıkça yazılı olmayan hâllerde **15 günden aşağı olmamak şartıyla süreyi, tebliği yapacak olan idare belirler** ve ilgiliye tebliğ eder. Süreyi mükellefin belirlemesi söz konusu değildir.',
    ),
    # düzey 2
    '0008': patch(
        'Bir kişi 10 Mart tarihinde ticari faaliyetine fiilen başlamış, ancak durumu vergi dairesine bildirmemiştir. Vergi dairesi yaptığı yoklamada faaliyetin sürdüğünü tespit etmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'İşe başlamayı bildirme ödevi yalnız şirketler için öngörülmüştür; gerçek kişi tacirler bakımından böyle bir yükümlülük bulunmadığından ceza kesilemez',
            'B': 'İşe başlamayı bildirmemek doğrudan kaçakçılık suçunu oluşturur; bu nedenle idari ceza yerine ceza davası açılması gerekir',
            'C': 'İşe başlama bildirimi ticaret sicilinde yapıldığından ayrıca vergi dairesine bildirim gerekmez; sicil kaydı bildirim yerine geçtiğinden ödev ihlali doğmaz',
            'D': 'Bildirim ödevi yalnız işi bırakma hâlinde doğar; işe başlamada bir bildirim yükümlülüğü öngörülmediğinden yoklama sonucu işlem yapılamaz',
            'E': 'Vergiye tabi ticaret ve sanat erbabı işe başlamayı vergi dairesine bildirmekle yükümlüdür; bildirimde bulunmamak usulsüzlük cezasını gerektiren bir ödev ihlalidir',
        },
        'E',
        '**VUK m. 153:** vergiye tabi ticaret ve sanat erbabı, serbest meslek erbabı ve kurumlar vergisi mükellefleri gibi kanunda sayılanlardan **işe başlayanlar keyfiyeti vergi dairesine bildirmeye mecburdurlar.** Bildirim ödevinin ihlali usulsüzlük hükümlerine tabidir.',
    ),
    # düzey 2
    '0009': patch(
        'Bir tüccarın iş hacmi kanunda öngörülen hadleri aşmış ve defter tutma usulü gündeme gelmiştir. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Birinci sınıf tüccarlar bilanço esasına göre defter tutar',
            'B': 'Tüccarlar defter tutma bakımından birinci ve ikinci sınıf olmak üzere ikiye ayrılır; bu nedenle iş hacmi hadleri yalnız istatistik amacıyla kullanılır ve sınıf değiştirmez',
            'C': 'İkinci sınıf tüccarlar işletme hesabı esasına göre defter tutar',
            'D': 'Defter tutma usulü tümüyle mükellefin tercihine bırakılmış olup iş hacmi hadlerinin bir etkisi bulunmaz',
            'E': 'Sınıf değişikliği kanunda öngörülen iş hacmi hadlerine bağlanmıştır',
        },
        'D',
        '**VUK m. 176** tüccarları iki sınıfa ayırır; **m. 177 ve m. 180** sınıfı ve sınıflar arası geçişi **iş hacmi hadlerine** bağlar. Usul mükellefin serbest tercihine bırakılmamıştır.',
    ),
    # düzey 3
    '0010': patch(
        'Bir mükellef, kullanacağı yevmiye defterini öteden beri işe devam etmekte olduğu hâlde takvim yılının Şubat ayında tasdik ettirmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Tasdik zamanı ticaret sicili müdürlüğünce belirlenir; vergi kanunlarında bir süre öngörülmediğinden idarenin bir itiraz hakkı yoktur',
            'B': 'Tasdik ancak defterin fiilen kullanılmaya başlandığı gün yapılır; kullanımdan önce yapılan tasdikler hükümsüz olduğundan işlem geçersizdir',
            'C': 'Öteden beri işe devam edenler defterlerini kullanacakları yıldan önce gelen son ayda tasdik ettirmekle yükümlüdür; Şubat ayında yapılan tasdik kanuni süresinde yapılmış sayılmaz',
            'D': 'Defterlerin tasdik zamanı kanunda düzenlenmemiştir; mükellef defterleri yıl içinde dilediği zaman tasdik ettirebileceğinden bir aykırılık doğmaz',
            'E': 'Öteden beri işe devam edenler için tasdik zorunluluğu bulunmaz; bu yükümlülük yalnız yeni işe başlayanlara özgü olduğundan Şubat tasdiki gereksizdir ve bu nedenle yıl içinde yapılan tasdikler baştan hükümsüz kabul edilir',
        },
        'C',
        "**VUK m. 221/1:** öteden beri işe devam etmekte olanlar defteri kullanacakları yıldan **önce gelen son ayda** tasdik ettirir. Tasdike tabi defterler **m. 220**'de sayılmıştır (yevmiye, envanter, işletme defteri vb.).",
    ),
    # düzey 2
    '0011': patch(
        'Bir mükellef yevmiye ve envanter defterlerini tasdik ettirmeden kullanmaya başlamış; vergi dairesi yaptığı incelemede hem tasdik hem de sınıflandırma yükümlülüklerini denetlemiştir. Buna göre defter tutma ve tasdik ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Ticaret şirketleri ile ticaret erbabı kanunun esaslarına göre defter tutmakla yükümlüdür',
            'B': 'Tasdike tabi defterlerin tasdik ettirilmesi mükellefin tercihine bırakılmış olup tasdiksiz defter kullanılması bir ödev ihlali oluşturmaz',
            'C': 'Yevmiye ve envanter defteri ile işletme defterinin tasdik ettirilmesi mükellefin tercihine bırakılmış olup tasdiksiz defter kullanmak bir ödev ihlali oluşturmaz',
            'D': 'Öteden beri işe devam edenler defterlerini kullanacakları yıldan önce gelen son ayda tasdik ettirir',
            'E': 'Tüccarlar defter tutma bakımından birinci ve ikinci sınıf olmak üzere ikiye ayrılır',
        },
        'B',
        '**VUK m. 220:** sayılan defterlerin tasdik ettirilmesi **mecburidir**; tasdik bir tercih değildir. Tasdiksiz defter kullanılması usulsüzlük hükümlerine göre cezalandırılır.',
    ),
    # düzey 3
    '0012': patch(
        'Birinci sınıf bir tüccar, 5 Ocak tarihinde teslim ettiği mal için faturayı 20 Ocak tarihinde düzenlemiştir. Alıcı da birinci sınıf tüccardır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Fatura, malın teslimi veya hizmetin yapıldığı tarihten itibaren kanunda öngörülen süre içinde düzenlenmelidir; bu süre aşıldığında fatura hiç düzenlenmemiş sayılır ve özel usulsüzlük hükümleri işler',
            'B': 'Faturanın süresinde düzenlenmemesi yalnız birinci derece usulsüzlük sayılır; özel usulsüzlük hükümleri belge hiç düzenlenmediğinde uygulanır',
            'C': 'Fatura ancak bedelin tahsil edildiği tarihte düzenlenebilir; teslim tarihi belge düzeni bakımından sonuç doğurmadığından işlem yerindedir',
            'D': "Fatura düzenleme süresi bulunmaz; mükellef bedeli tahsil ettiği tarihe kadar faturayı dilediği zaman düzenleyebileceğinden 20 Ocak'ta düzenlenen belge süresinde sayılır ve ceza kesilemez",
            'E': 'Fatura düzenleme ödevi yalnız alıcının talep etmesi hâlinde doğar; talep bulunmadıkça satıcının belge düzenleme yükümlülüğü ortaya çıkmaz',
        },
        'A',
        '**VUK m. 231/5:** fatura, malın teslimi veya hizmetin yapıldığı tarihten itibaren kanunda belirtilen süre içinde düzenlenir; **bu süre içinde düzenlenmeyen faturalar hiç düzenlenmemiş sayılır** ve m. 353 kapsamında özel usulsüzlük cezası gerektirir.',
    ),
    # düzey 2
    '0013': patch(
        'Birinci sınıf bir tüccar, kazancı basit usulde tespit edilen bir mükellefe mal satmış ve fatura düzenlememiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Fatura yalnız birinci sınıf tüccarlar arasındaki satışlarda düzenlenir; alıcı basit usulde olduğundan belge düzenleme yükümlülüğü doğmaz ve satıcıya özel usulsüzlük cezası kesilemez ve basit usule tabi alıcıya yapılan satışlarda perakende satış vesikası yeterli olur',
            'B': 'Fatura düzenlenmemesi yalnız alıcı bakımından sonuç doğurur; satıcının belge düzeni yükümlülüğü bulunmadığından ona ceza kesilemez',
            'C': 'Birinci ve ikinci sınıf tüccarlar ile kazancı basit usulde tespit edilenler ve defter tutan çiftçilere sattıkları emtia için fatura düzenlemekle yükümlüdür; satış bu kapsamda olduğundan belge düzenlenmelidir',
            'D': 'Basit usule tabi mükelleflere yapılan satışlarda perakende satış vesikası yeterlidir; bu nedenle fatura düzenlenmemesi bir aykırılık oluşturmaz',
            'E': 'Fatura düzenleme mecburiyeti tutar sınırına bağlı olmaksızın yalnız hizmet ifalarında doğar; emtia satışında belge zorunluluğu bulunmaz',
        },
        'C',
        '**VUK m. 232:** birinci ve ikinci sınıf tüccarlar, kazancı basit usulde tespit edilenler ve defter tutmak mecburiyetinde olan çiftçiler; **birinci ve ikinci sınıf tüccarlara, serbest meslek erbabına, kazancı basit usulde tespit edilenlere** ve defter tutmak mecburiyetinde olan çiftçilere sattıkları emtia için fatura vermek zorundadır.',
    ),
    # düzey 2
    '0014': patch(
        'Bir tüccar, sattığı emtia için düzenlediği faturada bedeli göstermemiş; ayrıca faturaları sıra numarası dâhilinde teselsül ettirmemiştir. Vergi dairesi belge düzenini incelemektedir. Buna göre belge düzeni ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Fatura, yalnızca satılan emtianın miktarını gösteren ve bedel içermeyen bir belge olup borç ilişkisini ispat etmez',
            'B': 'Birinci ve ikinci sınıf tüccarlar sattıkları emtia için kanunda sayılan kişilere fatura vermekle yükümlüdür',
            'C': 'Kanunda öngörülen süre içinde düzenlenmeyen faturalar hiç düzenlenmemiş sayılır',
            'D': 'Faturaların sıra numarası dâhilinde teselsül ettirilmesi gerekir',
            'E': 'Fatura, satılan emtia veya yapılan iş karşılığında müşterinin borçlandığı meblağı göstermek üzere düzenlenen ticari vesikadır',
        },
        'A',
        '**VUK m. 229:** fatura, satılan emtia veya yapılan iş karşılığında **müşterinin borçlandığı meblağı göstermek üzere** emtiayı satan veya işi yapan tüccar tarafından müşteriye verilen ticari vesikadır; bedel faturanın asli unsurudur.',
    ),
    # düzey 3
    '0015': patch(
        'Bir mükellef, 2020 takvim yılına ait defter ve belgelerini 2023 yılında imha etmiştir. Vergi dairesi 2026 yılında yaptığı incelemede bu defterleri istemiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Defter tutmak mecburiyetinde olanlar defter ve vesikaları ilgili bulundukları yılı takip eden takvim yılından başlayarak beş yıl süreyle muhafaza etmekle yükümlüdür; süre dolmadan yapılan imha ödev ihlalidir',
            'B': 'Muhafaza yükümlülüğü yalnız bilanço esasına tabi mükellefler için geçerlidir; işletme hesabı esasında saklama zorunluluğu bulunmaz',
            'C': 'Muhafaza süresi on yıl olmakla birlikte imha hâlinde yalnız birinci derece usulsüzlük cezası kesilir; ibraz etmeme ayrıca bir sonuç doğurmaz',
            'D': 'Defter ve belgelerin muhafazası zorunlu değildir; mükellef kayıtları elektronik ortamda tuttuğu sürece fiziki belgeleri saklamak durumunda kalmaz',
            'E': "Muhafaza süresi iki yıl olduğundan 2023'teki imha hukuka uygundur; süre dolduğu için idarenin 2026'da defter istemesi mümkün olmaz ve ibraz etmemek bir ödev ihlali oluşturmaz ve bu süre dolduktan sonra ibraz talebi hukuki dayanaktan yoksun kalır",
        },
        'A',
        '**VUK m. 253:** defter tutmak mecburiyetinde olanlar, tuttukları defterlerle vesikaları **ilgili bulundukları yılı takip eden takvim yılından başlayarak beş yıl süre ile muhafaza etmeye** mecburdurlar. **m. 256** bu belgelerin yetkililere ibrazını da zorunlu kılar.',
    ),
    # düzey 3
    '0016': patch(
        'Vergi incelemesi sırasında mükelleften muhafaza süresi içindeki defter ve belgeler istenmiş; mükellef bunları ibraz etmemiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'İbraz yükümlülüğü yalnız mahkeme kararıyla doğar; idarenin doğrudan talebi bağlayıcı olmadığından mükellef ibrazdan kaçınabilir',
            'B': 'Defterlerin ibraz edilmemesi yalnız ikinci derece usulsüzlük sayılır; matrahın tespiti bakımından bir sonuç doğurmadığından tarhiyat yapılamaz',
            'C': 'İbraz zorunluluğu muhafaza süresi dolduktan sonra da devam eder; süre sınırı olmadığından mükellef her zaman ibrazla yükümlüdür',
            'D': "İbraz talebine uyulmaması hâlinde idare doğrudan ikmalen tarhiyat yapar; matrah defterlere dayanılarak tespit edildiğinden re'sen tarha gerek kalmaz ve bu nedenle ibraz edilmeyen defterler için doğrudan ikmalen tarhiyat yapılır",
            'E': "Muhafaza edilmesi gereken defter ve belgelerin yetkili makam ve memurlara ibrazı gerekir; ibraz edilmemesi re'sen tarh sebebi oluşturur ve ayrıca cezai sonuç doğurur",
        },
        'E',
        "**VUK m. 256:** muhafaza mecburiyeti bulunanlar, bu belgeleri **yetkili makam ve memurların talebi üzerine ibraz ve inceleme için arz etmek zorundadır.** İbraz edilmemesi, matrahın belgelere dayanılarak tespitini imkânsız kıldığından **m. 30** uyarınca re'sen tarh sebebidir.",
    ),
    # düzey 2
    '0017': patch(
        'Mükellefin ödevleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Defter ve vesikalar ilgili bulundukları yılı takip eden takvim yılından başlayarak iki yıl muhafaza edilir.\n\nII. Muhafaza edilen defter ve belgeler yetkili makam ve memurların talebi üzerine ibraz edilir.\n\nIII. İşe başlamayı bildirme ödevi yalnız kurumlar vergisi mükelleflerine özgüdür.',
        {
            'A': 'Yalnız II',
            'B': 'Yalnız I',
            'C': 'Yalnız III',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'A',
        '**I yanlış:** m. 253 muhafaza süresini **beş yıl** olarak belirler. **II doğru:** m. 256. **III yanlış:** m. 153 bildirme ödevini ticaret ve sanat erbabı ile serbest meslek erbabını da kapsayacak biçimde düzenler.',
    ),
    # düzey 2
    '0018': patch(
        'Bir işletme, satın aldığı bir makinenin bedeline nakliye, montaj ve gümrük giderlerini de ekleyerek aktifleştirmek istemektedir. Vergi dairesi ise yalnız fatura bedelinin dikkate alınması gerektiğini savunmaktadır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Maliyet bedeline yalnız gümrük vergileri eklenir; nakliye ve montaj giderleri kanunda sayılmadığından maliyete dâhil edilmez',
            'B': 'Maliyet bedeli, iktisadi bir kıymetin iktisap edilmesi veya değerinin artırılması münasebetiyle yapılan ödemelerle bunlara ilişkin bütün giderlerin toplamını ifade eder; işletmenin uygulaması doğrudur',
            'C': 'Maliyet bedeli yalnız gayrimenkuller için kullanılan bir ölçüdür; makine gibi menkul kıymetler emsal bedelle değerlenir',
            'D': 'Maliyet bedeli mükellefin serbestçe belirleyeceği bir tutardır; kanunda bir tanım bulunmadığından her iki görüş de savunulabilir',
            'E': 'Maliyet bedeli yalnız satıcıya ödenen fatura bedelinden oluşur; nakliye ve montaj gibi giderler dönem gideri sayıldığından aktifleştirilemez ve amortisman matrahına dâhil edilmez ve bu giderler ilgili dönemde doğrudan gider yazılarak matrahtan indirilir',
        },
        'B',
        '**VUK m. 262:** maliyet bedeli, iktisadi bir kıymetin **iktisap edilmesi veyahut değerinin artırılması münasebetiyle yapılan ödemelerle bunlara müteferri bilumum giderlerin** toplamını ifade eder.',
    ),
    # düzey 3
    '0019': patch(
        'Bir işletmenin elinde, gerçek bedeli bilinmeyen ve doğru olarak tespit edilemeyen bir mal bulunmaktadır. Bu malın değerleme günündeki değeri belirlenecektir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Emsal bedeli sıra ile ortalama fiyat esası, maliyet bedeli esası ve takdir esasına göre tayin olunur; sıralamaya uyulması zorunludur',
            'B': 'Emsal bedeli, malın maliyet bedelinin iki katı olarak hesaplanır; kanun sabit bir oran öngördüğünden başka bir yönteme gerek kalmaz',
            'C': 'Emsal bedeli yalnız ortalama fiyat esasına göre belirlenir; diğer esaslar kanunda yer almadığından uygulanamaz',
            'D': 'Emsal bedeli doğrudan takdir komisyonunca belirlenir; ortalama fiyat ve maliyet bedeli esasları uygulanmadığından takdir ilk başvurulacak yoldur',
            'E': 'Emsal bedeli mükellefin beyan ettiği tutardır; kanunda bir belirleme yöntemi öngörülmediğinden beyan esas alınır',
        },
        'A',
        '**VUK m. 267:** emsal bedeli **sıra ile** (1) ortalama fiyat esası, (2) maliyet bedeli esası ve (3) takdir esasına göre tayin olunur. Sıra bağlayıcıdır; takdir esası ancak ilk iki esasın uygulanamadığı hâllerde devreye girer.',
    ),
    # düzey 2
    '0020': patch(
        'Bir işletme dönem sonunda stoklarını maliyet bedeliyle, alacak senetlerini mukayyet değerle, elindeki tahvilleri ise üzerinde yazılı tutarla değerlemiştir. Vergi dairesi kullanılan ölçüleri denetlemektedir. Buna göre değerleme ölçüleri ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'İtibari değer, her nevi senetlerle esham ve tahvillerin üzerinde yazılı olan değerdir',
            'B': 'Değerleme, vergi matrahlarının hesaplanmasıyla ilgili iktisadi kıymetlerin takdir ve tespitidir',
            'C': 'Mukayyet değer, işletmenin muhasebe kayıtlarında yer alan ve kayıt anındaki tutarı yansıtan değerdir',
            'D': 'İtibari değer, bir iktisadi kıymetin muhasebe kayıtlarında gösterilen hesap değeridir',
            'E': 'Emsal bedeli, gerçek bedeli olmayan veya bilinmeyen bir malın değerleme gününde emsaline nazaran haiz olacağı değerdir',
        },
        'D',
        '**VUK m. 265** mukayyet değeri *muhasebe kayıtlarındaki hesap değeri*, **m. 266** ise itibari değeri *senet, esham ve tahvillerin üzerinde yazılı değer* olarak tanımlar. Yanlış olan şık iki ölçüyü birbirine karıştırmaktadır.',
    ),
    # düzey 3
    '0021': patch(
        'Bir işletmenin aktifinde, vadesi gelmemiş ve senede bağlı bir alacağı bulunmaktadır. İşletme bu alacağı değerleme gününün kıymetine indirmek istemektedir. Senette faiz nispeti açıklanmamıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Vadesi gelmemiş senede bağlı alacaklar değerleme gününün kıymetine irca olunabilir; senette faiz nispeti açıklanmamışsa Merkez Bankasının resmî iskonto haddi uygulanır',
            'B': 'Faiz nispeti açıklanmamışsa reeskont hiç yapılamaz; oran belirlenemeyeceğinden alacak vade tarihine kadar aynen taşınır',
            'C': 'Faiz nispeti açıklanmamışsa mükellef dilediği oranı uygulayabilir; kanunda bir ölçüt bulunmadığından tercih serbesttir',
            'D': 'Vadesi gelmemiş senetler mukayyet değerle değerlenir; değerleme gününe indirgeme imkânı bulunmadığından senet vade tarihine kadar nominal tutarıyla taşınır',
            'E': 'Reeskont yalnız borç senetleri için yapılabilir; alacak senetlerinde indirgeme öngörülmediğinden talep reddedilir',
        },
        'A',
        '**VUK m. 281:** alacaklar mukayyet değerleriyle değerlenir; **vadesi gelmemiş olan senede bağlı alacaklar değerleme gününün kıymetine irca olunabilir.** Senette faiz nispeti açıklanmışsa o nispet, **açıklanmamışsa TCMB resmî iskonto haddi** uygulanır.',
    ),
    # düzey 2
    '0022': patch(
        'Bir işletme, aynı yıl içinde satın aldığı ve bir yıldan az kullanacağı bir alet için amortisman ayırmak istemektedir. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Amortismanın konusunu işletmede bir yıldan fazla kullanılan kıymetler oluşturur',
            'B': 'Amortismana tabi kıymetlerin yıpranmaya, aşınmaya veya kıymetten düşmeye maruz bulunması gerekir',
            'C': 'Gayrimenkuller ile alet, edevat, mefruşat ve demirbaşlar amortisman konusuna girer',
            'D': 'Amortisman süresi kıymetlerin aktife girdiği yıldan başlar',
            'E': 'İşletmede kullanılan bütün iktisadi kıymetler için kullanım süresine bakılmaksızın amortisman ayrılabilir',
        },
        'E',
        '**VUK m. 313:** amortismanın konusunu **bir yıldan fazla kullanılan** ve yıpranmaya maruz kıymetler oluşturur; kullanım süresi ölçütü kanunun aradığı şarttır.',
    ),
    # düzey 2
    '0023': patch(
        'Bilanço esasına göre defter tutan bir mükellef, amortismana tabi iktisadi kıymetlerini azalan bakiyeler usulüyle itfa etmek istemektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Azalan bakiyeler usulü bütün mükellefler için zorunludur; normal amortisman usulü kaldırıldığından başka bir yöntem uygulanamaz ve normal amortisman usulünü seçen mükellefler için ayrıca izin alınması gerekir',
            'B': 'Azalan bakiyeler usulü, bilanço esasına göre defter tutan mükelleflerden dileyenlerin uygulayabileceği bir yöntemdir; usul mükellefin tercihine bağlıdır',
            'C': 'Azalan bakiyeler usulü yalnız işletme hesabı esasına tabi mükelleflerce uygulanabilir; bilanço esasında bu yönteme başvurulamaz',
            'D': 'Azalan bakiyeler usulü yalnız binek otomobiller için öngörülmüştür; diğer kıymetlerde normal amortisman uygulanır',
            'E': 'Azalan bakiyeler usulüne geçiş yalnız Maliye Bakanlığının her mükellef için ayrı ayrı vereceği izinle mümkündür',
        },
        'B',
        '**VUK mükerrer m. 315:** **bilanço esasına göre defter tutan mükelleflerden dileyenler**, amortismana tabi iktisadi değerlerini azalan bakiyeler üzerinden amortisman usulü ile yok edebilirler. Yöntem seçimlik olup zorunlu değildir.',
    ),
    # düzey 2
    '0024': patch(
        'Bir işletme, aktifine yıl içinde giren bir makine için amortisman ayırmaya başlamış; oranı kendi belirlediği faydalı ömre göre hesaplamış ve süreyi fiilen kullanmaya başladığı tarihten işletmiştir. Buna göre amortisman ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Amortismanın konusunu işletmede bir yıldan fazla kullanılan ve yıpranmaya maruz kıymetler oluşturur',
            'B': 'Mükellefler amortismana tabi iktisadi kıymetlerini Maliye Bakanlığının tespit ve ilan edeceği oranlar üzerinden itfa eder',
            'C': 'Amortisman süresi kıymetlerin aktife girdiği yıldan başlar',
            'D': 'Amortisman süresi, iktisadi kıymetin satın alındığı tarihten değil işletmede fiilen kullanılmaya başlandığı tarihten itibaren işler',
            'E': 'İlan edilecek oranların tespitinde iktisadi kıymetlerin faydalı ömürleri dikkate alınır',
        },
        'D',
        '**VUK m. 320:** amortisman süresi **kıymetlerin aktife girdiği yıldan başlar**; ölçüt fiilen kullanılmaya başlama değil aktife girmedir. Sürenin yıl olarak hesabı için (1) rakamı uygulanan nispete bölünür.',
    ),
    # düzey 3
    '0025': patch(
        'Bir işletmenin ticari kazancının elde edilmesiyle ilgili bir alacağı için borçlusuna karşı icra takibi başlatılmıştır. İşletme bu alacak için karşılık ayırmak istemektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'İcra safhasındaki alacaklar değersiz alacak sayılır ve doğrudan zarara geçirilerek yok edilir; ayrıca karşılık ayrılmasına gerek kalmaz',
            'B': 'Karşılık ayrılabilmesi için alacağın tahsilinin kesin olarak imkânsız hâle gelmiş olması gerekir; icra takibi tek başına yeterli olmadığından ancak kazai bir hüküm elde edildiğinde işlem yapılabilir ve bu aşamaya gelmemiş alacaklar bilançoda mukayyet değeriyle taşınmaya devam eder',
            'C': 'Şüpheli alacak karşılığı yalnız işletme hesabı esasına tabi mükelleflerce ayrılabilir; bilanço esasında bu imkân bulunmaz',
            'D': 'Ticari kazancın elde edilmesi ve idame ettirilmesiyle ilgili olmak şartıyla dava veya icra safhasında bulunan alacaklar şüpheli alacak sayılır; değerleme gününün tasarruf değerine göre pasifte karşılık ayrılabilir',
            'E': 'Karşılık ancak alacağın tamamı için ve mukayyet değeri üzerinden ayrılabilir; tasarruf değeri ölçüsü kanunda öngörülmemiştir',
        },
        'D',
        '**VUK m. 323:** ticari ve zirai kazancın elde edilmesi ve idame ettirilmesiyle ilgili olmak şartıyla **dava veya icra safhasında bulunan alacaklar** şüpheli alacak sayılır ve **değerleme gününün tasarruf değerine göre pasifte karşılık** ayrılabilir.',
    ),
    # düzey 2
    '0026': patch(
        'Bir işletmenin alacağı, mahkeme kararıyla tahsilinin artık mümkün olmadığı kesinleşmiş durumdadır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Değersiz alacak yalnız konkordato hâlinde söz konusu olur; mahkeme kararı bu kapsamda değerlendirilmediğinden işlem yapılamaz',
            'B': 'Bu alacak için yalnız karşılık ayrılabilir; alacağın kayıtlardan çıkarılması mümkün olmadığından mahkeme kararına rağmen bilançoda taşınmaya devam edilir',
            'C': 'Kazai bir hükme veya kanaat verici bir vesikaya göre tahsiline artık imkân kalmayan alacaklar değersiz alacaktır; mukayyet kıymetleriyle zarara geçirilerek yok edilir',
            'D': 'Değersiz alacaklar tasarruf değeriyle değerlenir ve pasifte karşılık ayrılmak suretiyle izlenir; doğrudan zarara geçirilemez',
            'E': 'Mahkeme kararı bulunsa dahi alacak ancak beş yıl sonra değersiz sayılabilir; süre dolmadan kayıtlardan çıkarılamaz',
        },
        'C',
        '**VUK m. 322:** kazai bir hükme veya kanaat verici bir vesikaya göre **tahsiline artık imkân kalmayan** alacaklar değersiz alacaktır; bu mahiyete girdikleri tarihte tasarruf değerlerini kaybeder ve **mukayyet kıymetleriyle zarara geçirilerek yok edilirler.**',
    ),
    # düzey 3
    '0027': patch(
        'Bir borçlu ile konkordato yapılmış ve alacaklı, alacağının bir kısmından vazgeçmiştir. Buna göre borçlunun kayıtları bakımından aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Vazgeçilen alacak borçlunun defterlerinde beş yıl karşılık hesabında tutulur; sürenin sonunda kalan tutar sermayeye eklenir',
            'B': 'Konkordato veya sulh yoluyla alınmasından vazgeçilen alacaklar borçlunun defterlerinde özel bir karşılık hesabına alınır; bu hesap vazgeçildiği yılın sonundan başlayarak üç yıl içinde zararla itfa edilmezse kâr hesabına nakledilir',
            'C': 'Vazgeçilen alacak borçlu bakımından hiçbir kayıt gerektirmez; alacaklının vazgeçmesi borçlunun kayıtlarını etkilemediğinden işlem yapılmaz',
            'D': 'Vazgeçilen alacak yalnız alacaklının kayıtlarını ilgilendirir; borçlu bu tutarı zarar olarak kaydettiğinden ayrıca karşılık ayırmaz',
            'E': 'Vazgeçilen alacak borçlunun defterlerinde doğrudan kâr olarak yazılır; özel bir karşılık hesabı öngörülmediğinden tutar vazgeçildiği yılın matrahına eklenir ve o dönemde vergilendirilir ve borçlu bu tutarı üç yıl beklemeksizin doğrudan matrahına dâhil eder',
        },
        'B',
        '**VUK m. 324:** konkordato veya sulh yoluyla alınmasından vazgeçilen alacaklar **borçlunun defterlerinde özel bir karşılık hesabına** alınır; bu hesabın muhteviyatı vazgeçildiği yılın sonundan başlayarak **üç yıl içinde zararla itfa edilmezse kâr hesabına nakledilir.**',
    ),
    # düzey 2
    '0028': patch(
        'Alacakların değerlemesi ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Şüpheli alacaklar için mukayyet değer üzerinden doğrudan zarar yazılır; karşılık ayrılmaz.\n\nII. Kazai bir hükme veya kanaat verici bir vesikaya göre tahsiline imkân kalmayan alacaklar değersiz alacaktır.\n\nIII. Dava veya icra safhasında bulunan ticari alacaklar şüpheli alacak sayılır.',
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'Yalnız II',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'D',
        '**I yanlış:** şüpheli alacaklar için **değerleme gününün tasarruf değerine göre pasifte karşılık** ayrılır (m. 323); doğrudan zarar yazma değersiz alacaklara özgüdür (m. 322). **II doğru:** m. 322. **III doğru:** m. 323/1.',
    ),
    # düzey 3
    '0029': patch(
        'Bir işletmenin, protesto edilmiş ve yazı ile birden fazla kez istenmiş olmasına rağmen tahsil edilemeyen, dava ve icra takibine değmeyecek derecede küçük bir ticari alacağı bulunmaktadır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Şüpheli alacak sayılabilmesi için mutlaka dava veya icra takibi başlatılmış olması gerekir; küçük alacaklar bu kapsama girmediğinden protesto edilmiş olsalar dahi karşılık ayrılamaz ve protesto edilmiş küçük alacaklar için ancak değersiz alacak hükümleri işletilebilir',
            'B': 'Küçük alacaklar doğrudan değersiz alacak sayılır ve mukayyet kıymetiyle zarara geçirilir; karşılık ayrılması söz konusu olmaz',
            'C': 'Küçük alacaklarda karşılık ancak alacağın tamamı için ve vade tarihinden itibaren üç yıl geçtikten sonra ayrılabilir',
            'D': 'Yapılan protestoya veya yazı ile bir defadan fazla istenilmesine rağmen ödenmemiş bulunan, dava ve icra takibine değmeyecek derecede küçük alacaklar da şüpheli alacak sayılır ve karşılık ayrılabilir',
            'E': 'Protesto tek başına yeterli değildir; alacağın ayrıca mahkeme kararıyla tahsil edilemez olduğunun saptanması gerekir',
        },
        'D',
        '**VUK m. 323/2:** yapılan protestoya veya **yazı ile bir defadan fazla istenilmesine rağmen** borçlu tarafından ödenmemiş bulunan **dava ve icra takibine değmeyecek derecede küçük alacaklar** da şüpheli alacak sayılır.',
    ),
    # düzey 2
    '0030': patch(
        'Bir vergi dairesi memuru, mükellefin işyerine giderek faaliyetin sürüp sürmediğini, işyerinde çalışan sayısını ve ödeme kaydedici cihaz kullanılıp kullanılmadığını tespit etmiştir. Buna göre yapılan işlem bakımından aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Yapılan işlem vergi incelemesidir; defter ve kayıtlara bakılmasa dahi işyerine gidilmesi incelemeyi başlattığından inceleme hükümleri uygulanır ve bu nedenle memurun tespitleri inceleme raporu niteliği kazanarak tarhiyata esas alınır',
            'B': 'Yapılan işlem aramadır; mükellefin işyerine girilmesi arama sayıldığından sulh yargıcı kararı olmadan yapılması hukuka aykırıdır',
            'C': 'Yapılan işlem bilgi toplamadır; maddi olayların tespiti bilgi verme ödevi kapsamında olduğundan yazılı talep zorunludur',
            'D': 'Yoklama yalnız mükellefin beyanlarını doğrulamak için yapılır; fiili tespit yetkisi bulunmadığından memurun saptamaları hükümsüzdür',
            'E': 'Yoklamadan maksat mükellefleri ve mükellefiyetle ilgili maddi olayları, kayıtları ve mevzuları araştırmak ve tespit etmektir; yapılan işlem bu kapsamda bir yoklamadır',
        },
        'E',
        '**VUK m. 127:** yoklamadan maksat, **mükellefleri ve mükellefiyetle ilgili maddi olayları, kayıtları ve mevzuları araştırmak ve tespit etmektir.** Aynı madde, ödeme kaydedici cihaz mecburiyetine uyulup uyulmadığının tespitini de yoklama yetkileri arasında sayar.',
    ),
    # düzey 2
    '0031': patch(
        'Bir mükellef hakkında vergi incelemesi başlatılmış; işyerinin incelemeye elverişli olmadığı anlaşılmıştır. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'İş yerinin müsait olmaması hâlinde inceleme dairede yapılabilir',
            'B': 'Vergi incelemeleri esas itibarıyla incelemeye tabi olanın iş yerinde yapılır',
            'C': 'Vergi incelemesinden maksat ödenmesi gereken vergilerin doğruluğunu araştırmak ve tespit etmektir ve bu nedenle inceleme elemanının işyerine gitmesi usul yönünden sakatlık oluşturur',
            'D': 'Vergi incelemesi kanunda sayılan görevlilerce yapılır',
            'E': 'Vergi incelemeleri esas itibarıyla incelemeye tabi olanın iş yerinde yapılır; dairede inceleme yalnız iş yerinin müsait olmaması gibi zaruri hâllere özgüdür',
        },
        'E',
        '**VUK m. 139:** vergi incelemeleri **esas itibarıyla incelemeye tabi olanın iş yerinde** yapılır; dairede inceleme, iş yerinin müsait olmaması gibi zaruri hâllere özgü bir istisnadır.',
    ),
    # düzey 3
    '0032': patch(
        'Bir ihbar üzerine, bir mükellefin vergi kaçırdığına delalet eden emareler bulunmuştur. Vergi incelemesi yapmaya yetkili olanlar mükellefin işyerinde arama yapılmasını istemektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Arama, vergi incelemesine yetkili olanların kararıyla doğrudan yapılabilir; yargı merciinden karar alınmasına gerek bulunmadığından gecikmeksizin işleme başlanır',
            'B': 'Arama yapılabilmesi için incelemeye yetkili olanların lüzum göstermesi ve gerekçeli bir yazı ile sulh yargıcından istemesi ile sulh yargıcının arama kararı vermesi şarttır',
            'C': 'Arama için ihbarın varlığı tek başına yeterlidir; ayrıca emare aranmadığından ihbar üzerine doğrudan arama yapılır',
            'D': 'Arama kararını vergi dairesi başkanı verir; sulh yargıcının onayı yalnız sonradan alınacağından işlem hemen başlatılabilir',
            'E': 'Arama yalnız mükellefin yazılı muvafakatiyle yapılabilir; muvafakat verilmediğinde işlem durdurulur ve delil elde edilemez',
        },
        'B',
        '**VUK m. 142:** aramanın yapılabilmesi için (1) vergi incelemesi yapmaya yetkili olanların **buna lüzum göstermesi ve gerekçeli bir yazı ile arama kararı vermeye yetkili sulh yargıcından bunu istemesi**, (2) **sulh yargıcının** arama yapılmasına karar vermesi şarttır.',
    ),
    # düzey 2
    '0033': patch(
        'Bir vergi dairesi aynı mükellef hakkında sırasıyla yoklama yapmış, ardından vergi incelemesi başlatmış ve son olarak arama talebinde bulunmuştur. Her denetim yolu için farklı usul izlenmesi gerekmektedir. Buna göre vergi denetimi ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Yoklamadan maksat mükellefleri ve mükellefiyetle ilgili maddi olayları araştırmak ve tespit etmektir',
            'B': 'Arama yapılabilmesi için sulh yargıcının karar vermesi şarttır',
            'C': 'Vergi incelemeleri esas itibarıyla incelemeye tabi olanın iş yerinde yapılır',
            'D': 'Vergi incelemesinden maksat, ödenmesi gereken vergilerin doğruluğunu araştırmak, tespit etmek ve sağlamaktır',
            'E': 'Vergi incelemesi yalnız Vergi Müfettişleri tarafından yapılabilir; vergi dairesi müdürlerinin inceleme yetkisi bulunmaz',
        },
        'E',
        '**VUK m. 135:** vergi incelemesi **Vergi Müfettişleri, Vergi Müfettiş Yardımcıları, ilin en büyük mal memuru veya vergi dairesi müdürleri** tarafından yapılır; yetki yalnız müfettişlere ait değildir.',
    ),
    # düzey 2
    '0034': patch(
        'Bir banka, vergi dairesinin yazılı talebi üzerine bir mükellefe ilişkin bilgileri vermekten kaçınmıştır. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Bilgiler Hazine ve Maliye Bakanlığının veya incelemeye yetkili olanların isteği üzerine verilir; bu nedenle bankanın verdiği bilgiler hukuka aykırı delil sayılır',
            'B': 'Mükelleflerle muamelede bulunan gerçek ve tüzel kişiler de bilgi vermekle yükümlüdür',
            'C': 'Bilgi verme ödevi yalnız mükellefin kendisine yöneltilebilir; mükellefle muamelede bulunan üçüncü kişilerden bilgi istenemez',
            'D': 'Kamu idare ve müesseseleri istenecek bilgileri vermeye mecburdur',
            'E': 'Bilgi verme ödevinin ihlali kanunda yaptırıma bağlanmıştır',
        },
        'C',
        '**VUK m. 148:** kamu idare ve müesseseleri, mükellefler **veya mükelleflerle muamelede bulunan diğer gerçek ve tüzel kişiler** istenecek bilgileri vermeye mecburdurlar; ödev üçüncü kişileri de kapsar.',
    ),
    # düzey 3
    '0035': patch(
        'Vergi denetim yolları ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yoklama, mükellefiyetle ilgili maddi olayların araştırılıp tespit edilmesine yöneliktir.\n\nII. Arama, vergi incelemesine yetkili olanların kararıyla ve yargı merciine başvurulmaksızın yapılabilir.\n\nIII. Vergi incelemeleri esas itibarıyla incelemeye tabi olanın iş yerinde yapılır.',
        {
            'A': 'I ve II',
            'B': 'Yalnız II',
            'C': 'I ve III',
            'D': 'Yalnız I',
            'E': 'I, II ve III',
        },
        'C',
        '**I doğru:** m. 127. **III doğru:** m. 139. **II yanlış:** **m. 142** aramayı, incelemeye yetkili olanların gerekçeli yazısı üzerine **sulh yargıcının karar vermesi** şartına bağlar.',
    ),
    # düzey 2
    '0036': patch(
        'Bir mükellef, beyannamesini süresinde vermemesi nedeniyle verginin zamanında tahakkuk ettirilmemesine yol açmıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Verginin sonradan tahakkuk ettirilmesi ziyaı ortadan kaldırır; bu nedenle gecikmeli tahakkukta ceza kesilmez',
            'B': 'Ödevlerin zamanında yerine getirilmemesi yüzünden verginin zamanında tahakkuk ettirilmemesi vergi ziyaıdır; ziyaa uğratılan verginin bir katı tutarında vergi ziyaı cezası kesilir',
            'C': 'Beyannamenin verilmemesi yalnız usulsüzlük sayılır; vergi ziyaı ancak matrahın kasten gizlenmesi hâlinde doğduğundan bu olayda ziyaı cezası kesilemez ve yalnız maktu ceza uygulanır',
            'D': 'Vergi ziyaı cezası ziyaa uğratılan verginin üç katıdır; kanun bütün ziyaı hâllerinde aynı katsayıyı öngördüğünden ayrım yapılmaz',
            'E': 'Vergi ziyaı yalnız mükellef bakımından doğar; vergi sorumlusunun ödevlerini ihlali ziyaı oluşturmadığından ceza kesilmez',
        },
        'B',
        '**VUK m. 341** vergi ziyaını, ödevlerin zamanında yerine getirilmemesi yüzünden verginin zamanında veya eksik tahakkuk ettirilmesi olarak tanımlar; **m. 344/1** bu hâlde **ziyaa uğratılan verginin bir katı** tutarında ceza öngörür.',
    ),
    # düzey 3
    '0037': patch(
        'Bir mükellef, sahte belge kullanmak suretiyle vergi ziyaına sebebiyet vermiştir. Fiile iştirak eden bir başka kişi de bulunmaktadır. Buna göre kesilecek vergi ziyaı cezası bakımından aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Kaçakçılık fiilleriyle ziyaa sebebiyet verilse dahi ceza bir kat olarak uygulanır; fiilin niteliği ceza miktarını etkilemediğinden artırım yapılmaz',
            'B': 'Vergi ziyaına kaçakçılık fiilleriyle sebebiyet verilmesi hâlinde ceza üç kat, bu fiillere iştirak edenlere ise bir kat olarak uygulanır',
            'C': 'İştirak edenlere ceza kesilmez; ceza yalnız mükellef adına kesildiğinden üçüncü kişilerin sorumluluğu doğmaz',
            'D': 'Kaçakçılık fiilleri hâlinde idari ceza kesilmez; yalnız ceza davası açıldığından vergi ziyaı cezası uygulanmaz',
            'E': 'Ceza hem fail hem iştirak eden bakımından üç kat uygulanır; kanun iştirak edenler için ayrı bir oran öngörmediğinden aynı katsayı geçerlidir',
        },
        'B',
        '**VUK m. 344/2:** vergi ziyaına **359 uncu maddede yazılı fiillerle** sebebiyet verilmesi hâlinde bu ceza **üç kat**, **bu fiillere iştirak edenlere ise bir kat** olarak uygulanır.',
    ),
    # düzey 3
    '0038': patch(
        'Vergi ziyaına sebebiyet vermekten dolayı kesilen ve kesinleşen bir cezanın ardından, cezanın kesinleştiği tarihi izleyen yılın başından itibaren üç yıl içinde aynı mükellefe yeniden vergi ziyaı cezası kesilmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Tekerrür yalnız usulsüzlük cezaları için öngörülmüştür; vergi ziyaı cezalarında artırım uygulanmadığından ceza aynen kesilir',
            'B': 'Tekerrür süresi vergi ziyaında iki yıl olduğundan üçüncü yılda kesilen ceza artırılmaz; süre dolduğu için normal oran uygulanır',
            'C': 'Tekerrür süresi ilk fiilin işlendiği tarihten itibaren hesaplanır; cezanın kesinleşme tarihi dikkate alınmadığından süre çoktan dolmuştur ve bu nedenle tekerrür hesabında cezanın kesinleşme tarihi dikkate alınmaz',
            'D': 'Tekerrür hâlinde ceza yüzde yüz oranında artırılır; kanun ziyaı ve usulsüzlük için aynı artırım oranını öngördüğünden ayrım yapılmaz',
            'E': 'Vergi ziyaında beş yıl içinde tekrar ceza kesilmesi durumunda vergi ziyaı cezası yüzde elli oranında artırılarak uygulanır; olayda tekerrür hükümleri işler',
        },
        'E',
        '**VUK m. 339:** ceza kesilen ve **cezası kesinleşenlere**, cezanın kesinleştiği tarihi takip eden yılın başından başlamak üzere **vergi ziyaında beş, usulsüzlükte iki yıl** içinde tekrar ceza kesilmesi durumunda, **vergi ziyaı cezası %50, usulsüzlük cezası %25** oranında artırılır.',
    ),
    # düzey 3
    '0039': patch(
        'Kendisine vergi/ceza ihbarnamesi tebliğ edilen bir mükellef, ilk defa kesilen vergi ziyaı cezası için indirimden yararlanmak istemektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'İndirimden yararlanmak için cezanın tamamının peşin ödenmesi ve ayrıca dava açılmamış olması yeterli değildir; uzlaşma da sağlanmış olmalıdır',
            'B': 'İndirim oranı birinci defada üçte birdir; kanun ilk ve sonraki cezalar için aynı oranı öngördüğünden fark doğmaz',
            'C': 'Mükellef ihbarnamenin tebliğinden itibaren otuz gün içinde başvurup vadesinde ödeyeceğini bildirirse vergi ziyaı cezasının birinci defada yarısı indirilir',
            'D': 'İndirim yalnız usulsüzlük cezaları için uygulanır; vergi ziyaı cezasında indirim öngörülmediğinden talep reddedilir',
            'E': 'İndirim talebi için süre bulunmaz; mükellef ödeme yaptığı sürece her zaman indirimden yararlanabileceğinden başvuru zamanı önem taşımaz',
        },
        'C',
        '**VUK m. 376:** mükellef, ihbarnamelerin tebliğ tarihinden itibaren **otuz gün içinde** vergi dairesine başvurup vadesinde (veya teminat göstererek üç ay içinde) ödeyeceğini bildirirse **vergi ziyaı cezasında birinci defada yarısı**, müteakiben kesilenlerde üçte biri indirilir.',
    ),
    # düzey 2
    '0040': patch(
        'Bir mükellef hakkında hem vergi ziyaı hem de usulsüzlük fiilleri tespit edilmiş; ayrıca geçmişte kesinleşmiş bir cezası bulunduğu ve indirim talebinde bulunduğu görülmüştür. Buna göre vergi cezaları ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Vergi ziyaına kaçakçılık fiilleriyle sebebiyet verilmesi hâlinde ceza üç kat olarak uygulanır',
            'B': 'İhbarnamenin tebliğinden itibaren otuz gün içinde başvuran mükellef cezada indirimden yararlanabilir',
            'C': 'Vergi ziyaı cezası, ziyaa uğratılan verginin tutarına bakılmaksızın kanunda gösterilen maktu tutar üzerinden kesilir',
            'D': 'Tekerrür hâlinde vergi ziyaı cezası yüzde elli oranında artırılarak uygulanır',
            'E': 'Vergi ziyaı, ödevlerin zamanında yerine getirilmemesi yüzünden verginin zamanında tahakkuk ettirilmemesidir',
        },
        'C',
        "**VUK m. 344/1:** vergi ziyaı cezası **ziyaa uğratılan verginin bir katı** tutarındadır; nispi bir cezadır, maktu değildir. Maktu tutarlar usulsüzlük cezalarına (m. 352'ye bağlı cetvel) özgüdür.",
    ),
    # düzey 2
    '0041': patch(
        'Bir mükellef, defter ve kayıtlarında muhasebe hileleri yapmış ve defterleri gizlemiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Kaçakçılık fiilleri idari para cezasıyla karşılanır; kanun bu fiiller için hürriyeti bağlayıcı ceza öngörmediğinden ceza davası açılmaz',
            'B': 'Kaçakçılık fiilleri yalnız sahte belge düzenlemekle sınırlıdır; defterlerin gizlenmesi bu kapsamda değerlendirilmez',
            'C': 'Bu fiiller yalnız usulsüzlük sayılır; kaçakçılık kapsamına girmediğinden hakkında yalnız maktu usulsüzlük cezası kesilir ve vergi ziyaı cezası bir kat olarak uygulanır ve fiil hakkında ayrıca ceza mahkemesinde dava açılmasına gerek kalmaz',
            'D': 'Bu fiiller yalnız vergi ziyaı doğduğunda kaçakçılık sayılır; ziyaı bulunmadıkça fiilin cezai bir sonucu doğmaz',
            'E': 'Defter ve kayıtlarda hesap ve muhasebe hileleri yapmak ile defter, kayıt ve belgeleri tahrif etmek veya gizlemek kaçakçılık fiillerindendir; bu fiiller hürriyeti bağlayıcı cezayı gerektirir',
        },
        'E',
        '**VUK m. 359/a:** defter ve kayıtlarda **hesap ve muhasebe hileleri** yapanlar ile defter, kayıt ve belgeleri **tahrif edenler veya gizleyenler** hakkında kanunda öngörülen hapis cezası uygulanır. Ayrıca **m. 344/2** uyarınca vergi ziyaı cezası üç kat kesilir.',
    ),
    # düzey 2
    '0042': patch(
        'Vergi cezalarında tekerrür ve indirim ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Tekerrür hâlinde usulsüzlük cezası yüzde yirmi beş oranında artırılarak uygulanır.\n\nII. Tekerrür süresi usulsüzlükte iki yıldır.\n\nIII. Cezada indirimden yararlanmak için ihbarnamenin tebliğinden itibaren altmış gün içinde başvurulması gerekir.',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'Yalnız III',
            'D': 'I, II ve III',
            'E': 'II ve III',
        },
        'B',
        '**I ve II doğru:** m. 339, usulsüzlükte **iki yıl** ve **%25** artırım öngörür. **III yanlış:** **m. 376** indirim başvurusu için **otuz gün** süre tanır.',
    ),
    # düzey 3
    '0043': patch(
        "Bir mükellefe, beyannamesini kanuni süresinde vermemesi nedeniyle usulsüzlük cezası kesilmiştir. Aynı fiil re'sen takdiri de gerektirmektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': 'Usulsüzlük cezası, ziyaa uğratılan verginin bir katı olarak hesaplanır; nispi bir ceza olduğundan maktu tutar uygulanmaz',
            'B': "Usulsüzlükler kanuna bağlı cetvele göre derecelendirilerek cezalandırılır; usulsüzlük fiili re'sen takdiri gerektirdiğinde cetvelde gösterilen cezalar iki kat olarak kesilir",
            'C': "Re'sen takdiri gerektiren usulsüzlüklerde ceza yarı oranında indirilir; mükellefin işbirliği karine sayıldığından indirim uygulanır",
            'D': "Usulsüzlük cezaları tek bir maktu tutar üzerinden kesilir; derecelendirme veya artırım öngörülmediğinden fiilin niteliği sonucu değiştirmez; bu nedenle re'sen takdiri gerektiren fiillerde de aynı maktu tutar uygulanır",
            'E': "Re'sen takdiri gerektiren usulsüzlüklerde ceza kesilmez; matrah takdir edildiğinden ayrıca usulsüzlük cezası uygulanmaz",
        },
        'B',
        "**VUK m. 352:** usulsüzlükler kanuna bağlı cetvele göre **derecelere ayrılarak** cezalandırılır ve **usulsüzlük fiili re'sen takdiri gerektirirse** bağlı cetvelde gösterilen cezalar **iki kat** olarak kesilir.",
    ),
    # düzey 2
    '0044': patch(
        'Bir mükellef, beyannamesini geç vermesi nedeniyle eksik tahakkuk eden vergiyi sonradan kendiliğinden ödemiş ve bu ödeme sebebiyle ceza kesilemeyeceğini ileri sürmüştür. Buna göre vergi ziyaı ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Ödevlerin eksik yerine getirilmesi yüzünden verginin eksik tahakkuk ettirilmesi de vergi ziyaıdır',
            'B': 'Vergi ziyaı, ödevlerin zamanında yerine getirilmemesi yüzünden verginin zamanında tahakkuk ettirilmemesidir',
            'C': 'Verginin sonradan tahakkuk ettirilmesi veya tamamlanması hâlinde vergi ziyaı doğmamış sayılır ve kesilen ceza kaldırılır',
            'D': 'Şahsi veya aile durumu hakkında gerçeğe aykırı beyanla verginin noksan tahakkuk ettirilmesi de vergi ziyaı hükmündedir',
            'E': 'Vergi ziyaına sebebiyet verilmesi hâlinde ziyaa uğratılan verginin bir katı tutarında ceza kesilir',
        },
        'C',
        '**VUK m. 341** son fıkrası: yukarıdaki hâllerde **verginin sonradan tahakkuk ettirilmesi veya tamamlanması vergi ziyaı cezasının uygulanmasına mâni teşkil etmez.** Ziyaın sonradan giderilmesi cezayı ortadan kaldırmaz.',
    ),
    # düzey 2
    '0045': patch(
        'Bir mükellef, düzenlemesi gereken faturayı hiç düzenlememiş; alıcı da belgeyi almamıştır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Belge düzenlenmemesi hâlinde ceza kesilmez; yalnız matrah farkı bulunursa vergi ziyaı cezası uygulandığından ayrı bir yaptırım doğmaz',
            'B': 'Ceza yalnız belgeyi düzenlemesi gereken satıcıya kesilir; alıcının belge alma yükümlülüğü bulunmadığından ona ceza uygulanmaz ve belge almamak bir ödev ihlali sayılmaz ve alıcı hakkında belge almamaktan dolayı hiçbir işlem yapılmaz',
            'C': 'Ceza yalnız alıcıya kesilir; belgeyi talep etme yükümlülüğü alıcıda olduğundan satıcının sorumluluğu doğmaz',
            'D': 'Verilmesi ve alınması gereken fatura ve benzeri belgelerin verilmemesi ve alınmaması hâlinde belgeyi düzenlemek ve almak durumunda olanların her birine özel usulsüzlük cezası kesilir',
            'E': 'Belge düzenlenmemesi yalnız birinci derece usulsüzlük sayılır; özel usulsüzlük hükümleri belgenin eksik düzenlenmesi hâlinde işler',
        },
        'D',
        '**VUK m. 353/1:** verilmesi ve alınması icabeden fatura, serbest meslek makbuzu ve benzeri belgelerin verilmemesi ve alınmaması hâlinde **bu belgeleri düzenlemek ve almak zorunda olanların her birine** kanunda belirtilen tutarda özel usulsüzlük cezası kesilir.',
    ),
    # düzey 2
    '0046': patch(
        'Bir tüccar, defter tutmayan bir çiftçiden zirai ürün satın almıştır. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Birinci ve ikinci sınıf tüccarlar bu belgeyi düzenlemekle yükümlüdür',
            'B': 'Müstahsil makbuzu, malı satın alan tarafından düzenlenir',
            'C': 'Defter tutmayan çiftçilerden yapılan alımlar için fatura düzenlenir; müstahsil makbuzu kanunda öngörülmediğinden bu belgeyle yapılan kayıtlar geçersiz sayılır ve gider olarak indirilemez',
            'D': 'Defter tutmayan çiftçilerden yapılan alımlar belgeye bağlanmaz; satıcı defter tutmadığından alıcının da belge düzenleme yükümlülüğü doğmaz',
            'E': 'Müstahsil makbuzu iki nüsha düzenlenip bir nüshası satıcıya verilir',
        },
        'D',
        '**VUK m. 235:** defter tutmayan çiftçilerden satın alınan mallar için **müstahsil makbuzu** düzenlenir; belge düzenleme yükümlülüğü **satın alana** aittir.',
    ),
    # düzey 2
    '0047': patch(
        'Serbest meslek erbabının mesleki faaliyetine ilişkin tahsilatları için düzenleyeceği belge bakımından aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Serbest meslek erbabı, mesleki faaliyetlerine ilişkin her türlü tahsilatı için iki nüsha serbest meslek makbuzu düzenler ve bir nüshasını müşteriye verir',
            'B': 'Serbest meslek makbuzu yalnız kurumlara yapılan hizmetlerde düzenlenir; gerçek kişilere verilen hizmetlerde belge zorunluluğu bulunmaz ve bu nedenle serbest meslek erbabı yalnız kurumsal müşterilerine belge düzenler',
            'C': 'Serbest meslek makbuzu tek nüsha düzenlenir ve yalnız mükellefin kendi kayıtlarında saklanır',
            'D': 'Serbest meslek erbabı tahsilatları için fatura düzenler; serbest meslek makbuzu kanunda yer almadığından kullanılamaz',
            'E': 'Serbest meslek erbabı belge düzenlemekle yükümlü değildir; defter kaydı yeterli sayıldığından ayrıca makbuz aranmaz',
        },
        'A',
        '**VUK m. 236:** serbest meslek erbabı, mesleki faaliyetlerine ilişkin **her türlü tahsilatı için iki nüsha serbest meslek makbuzu** tanzim etmek ve bir nüshasını müşteriye vermek, müşteri de bu makbuzu istemek ve almak mecburiyetindedir.',
    ),
    # düzey 2
    '0048': patch(
        'Bir tüccar aynı gün içinde bir müşterisine mal satmış, malı sevk etmiş ve bir serbest meslek erbabından hizmet almıştır. Her işlem için ayrı bir belge düzenlenmesi gerekmektedir. Buna göre belge düzeni ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Defter tutmayan çiftçilerden satın alınan mallar için müstahsil makbuzu düzenlenir',
            'B': 'Fatura, satılan emtia karşılığında müşterinin borçlandığı meblağı göstermek üzere düzenlenir',
            'C': 'Serbest meslek erbabı tahsilatları için iki nüsha serbest meslek makbuzu düzenler',
            'D': 'Kanunda öngörülen süre içinde düzenlenmeyen faturalar hiç düzenlenmemiş sayılır',
            'E': 'Sevk irsaliyesi, satılan malın bedelini göstermek üzere düzenlenen ve fatura yerine geçen bir belgedir',
        },
        'E',
        'Sevk irsaliyesi malın **taşınmasını** belgelendiren bir vesikadır; **bedel içermez ve faturanın yerine geçmez.** Bedeli gösteren belge **m. 229** uyarınca faturadır.',
    ),
    # düzey 3
    '0049': patch(
        'Bir mükellef hakkında hem defterlerini tasdik ettirmemek hem de beyannamesini süresinde vermemek fiilleri tespit edilmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Şekle ilişkin ihlallerde ceza kesilmez; yalnız matrah farkı bulunduğunda yaptırım uygulandığından bu fiiller cezasız kalır',
            'B': 'Bu fiiller vergi ziyaı sayılır; şekle ilişkin aykırılıklar doğrudan verginin eksik tahakkukuna yol açtığından mükellef hakkında ziyaa uğratılan verginin bir katı tutarında ceza kesilir ve bu nedenle mükellef hakkında ayrıca usulsüzlük cezası kesilmesi mümkün olmaz',
            'C': 'Bu fiiller için yalnız özel usulsüzlük cezası kesilir; genel usulsüzlük hükümleri belge düzenine özgü olduğundan uygulanmaz',
            'D': 'Her iki fiil de vergi kanunlarının şekle ve usule ilişkin hükümlerine riayetsizlik oluşturduğundan usulsüzlük hükümlerine göre değerlendirilir; usulsüzlükler cetvele göre derecelendirilerek cezalandırılır',
            'E': 'Bu fiiller kaçakçılık suçunu oluşturur; defter tasdiki ve beyan yükümlülüğünün ihlali hürriyeti bağlayıcı cezayı gerektirir',
        },
        'D',
        '**VUK m. 351:** usulsüzlük, vergi kanunlarının **şekle ve usule** ilişkin hükümlerine riayet edilmemesidir. **m. 352** usulsüzlükleri derecelere ve kanuna bağlı cetvele göre cezalandırır.',
    ),
    # düzey 2
    '0050': patch(
        'Bir işveren ile çalışanı arasında yapılan sözleşmede, çalışanın gelir vergisinin işveren tarafından üstlenildiği kararlaştırılmıştır. Vergi dairesi bu sözleşmenin kendisini bağlayıp bağlamadığını değerlendirmektedir. Buna göre mükellefiyet ve sorumluluk ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Mükellefiyet ve vergi sorumluluğu için kanuni ehliyet şart değildir',
            'B': 'Vergi kanunlarıyla kabul edilen hâller dışında, mükellefiyete ilişkin özel sözleşmeler vergi dairesini bağlar ve borcun muhatabını değiştirir',
            'C': 'Tüzel kişilerin vergi ödevleri kanuni temsilcileri tarafından yerine getirilir',
            'D': 'Vergi sorumlusu, verginin ödenmesi bakımından alacaklı vergi dairesine karşı muhatap olan kişidir',
            'E': 'Mükellef, vergi kanunlarına göre kendisine vergi borcu terettüp eden gerçek veya tüzel kişi olduğundan taraflar bu sıfatı sözleşmeyle serbestçe devredebilir ve idare devri kabul eder',
        },
        'B',
        '**VUK m. 8** son fıkrası: **vergi kanunlarıyla kabul edilen hâller müstesna olmak üzere, mükellefiyete veya vergi sorumluluğuna müteallik özel mukaveleler vergi dairelerini bağlamaz.** Sözleşmeyle borcun muhatabı değiştirilemez.',
    ),
    # düzey 3
    '0051': patch(
        'Bir mükellef, ağır hastalığı nedeniyle ödevlerini yerine getiremediğini ileri sürmektedir. Vergi dairesi ise mükellefin zor durum hükümlerinden yararlanabileceğini belirtmiştir. Buna göre iki kurumun ayrımı bakımından aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Zor durumda verilecek mühletin üst sınırı bulunmaz; mücbir sebepte ise süre en çok bir yıl durur',
            'B': 'Mücbir sebep yalnız afetleri kapsar; ağır hastalık zor durum sayıldığından sürelerin durması söz konusu olmaz',
            'C': 'Mücbir sebepte idare mühlet verir, zor durumda ise süreler kendiliğinden durur; kanun bu iki kurumu bu şekilde ayırmıştır',
            'D': 'İki kurum aynı sonucu doğurur; her ikisinde de süreler kendiliğinden durduğundan mükellefin ayrıca idareye başvurmasına ve mühlet istemesine gerek kalmaz ve idarenin ayrıca bir mühlet kararı vermesine gerek kalmaz',
            'E': 'Mücbir sebepte süreler kendiliğinden işlemez ve sebep ortadan kalkıncaya kadar durur; zor durumda ise idarece kanuni sürenin bir katını geçmemek üzere ek mühlet verilir',
        },
        'E',
        '**VUK m. 15:** mücbir sebep hâlinde **süreler işlemez** ve tarh zamanaşımı işlemeyen süreler kadar uzar. **m. 17:** zor durumda bulunanlara **kanuni sürenin bir katını geçmemek üzere** mühlet verilebilir. **m. 13** ağır hastalığı mücbir sebep olarak sayar.',
    ),
    # düzey 2
    '0052': patch(
        'Bir mükellef, tasdik ettirdiği tarihten itibaren üç yıl geçtiği gerekçesiyle defterlerini imha etmiş; vergi incelemesinde bu defterler istenmiştir. Buna göre defter ve belgelerin muhafazası ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Muhafaza edilen defter ve belgeler yetkili makam ve memurların talebi üzerine ibraz edilir',
            'B': 'Muhafaza süresi ilgili bulunulan yılı takip eden takvim yılından başlar',
            'C': "İbraz yükümlülüğüne uyulmaması matrahın re'sen takdirini gerektirebilir",
            'D': 'Defter tutmak mecburiyetinde olanlar defter ve vesikaları muhafaza etmekle yükümlüdür',
            'E': 'Muhafaza süresi, defterlerin tasdik ettirildiği tarihten başlayarak üç yıldır',
        },
        'E',
        '**VUK m. 253:** muhafaza süresi, defter ve vesikaların **ilgili bulundukları yılı takip eden takvim yılından başlayarak beş yıldır**; başlangıç tasdik tarihi değil, ilgili olunan yıldır.',
    ),
    # düzey 3
    '0053': patch(
        'Amortisman ve değerleme ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Emsal bedeli doğrudan takdir esasına göre belirlenir.\n\nII. Amortisman süresi kıymetlerin aktife girdiği yıldan başlar.\n\nIII. Azalan bakiyeler usulü bütün mükellefler için zorunludur.',
        {
            'A': 'Yalnız II',
            'B': 'Yalnız I',
            'C': 'Yalnız III',
            'D': 'II ve III',
            'E': 'I ve II',
        },
        'A',
        '**I yanlış:** m. 267 emsal bedelin **sıra ile** ortalama fiyat, maliyet bedeli ve takdir esaslarına göre belirleneceğini öngörür. **II doğru:** m. 320. **III yanlış:** mükerrer m. 315 azalan bakiyeler usulünü **bilanço esasına göre defter tutanlardan dileyenlere** tanır; zorunlu değildir.',
    ),
    # düzey 2
    '0054': patch(
        'Bir mükellef, ikinci sınıf tüccar olarak işletme hesabı esasına göre defter tutmaktadır. İş hacmi kanunda öngörülen hadleri aşmış ve mükellef bilanço esasına geçirilmiştir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Defter tutma bakımından sınıflandırma kaldırılmıştır; bütün tüccarlar aynı esasa tabi olduğundan geçişten söz edilemez',
            'B': 'Sınıf değişikliği yalnız mükellefin talebiyle olur; iş hacmi hadlerinin aşılması kendiliğinden bir sonuç doğurmadığından geçiş yapılamaz ve hadleri aşan mükellef bildirimde bulunmadıkça eski usulünü sürdürebilir',
            'C': 'Tüccarlar defter tutma bakımından iki sınıfa ayrılır ve sınıf değişikliği iş hacmine ilişkin hadlere bağlanmıştır; hadleri aşan ikinci sınıf tüccar bilanço esasına geçer',
            'D': 'Bir kez işletme hesabı esasını seçen mükellef bu usulü değiştiremez; bilanço esasına geçiş kanunen mümkün olmadığından işlem hatalıdır',
            'E': 'Sınıf değişikliği ancak vergi mahkemesi kararıyla yapılabilir; idarenin resen sınıf değiştirme yetkisi bulunmaz',
        },
        'C',
        '**VUK m. 176** tüccarları defter tutma bakımından iki sınıfa ayırır; **m. 177** birinci sınıfa girecekleri iş hacmi hadleriyle belirler ve **m. 180** hadleri aşan ikinci sınıf tüccarın bilanço esasına geçişini düzenler.',
    ),
    # düzey 2
    '0055': patch(
        "Bir mükellefe hem re'sen takdiri gerektiren bir usulsüzlük fiili hem de belge düzenine aykırılık nedeniyle ceza kesilmiş; mükellef ayrıca tekerrür hükümlerinin uygulanmasına itiraz etmiştir. Buna göre vergi cezaları ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
        {
            'A': "Usulsüzlük fiili re'sen takdiri gerektirse dahi cetveldeki cezalar aynen uygulanır ve artırım yapılmaz",
            'B': 'Verilmesi ve alınması gereken belgelerin verilmemesi hâlinde her iki tarafa da özel usulsüzlük cezası kesilir',
            'C': 'Usulsüzlük, vergi kanunlarının şekle ve usule ilişkin hükümlerine riayet edilmemesidir',
            'D': 'Usulsüzlükler kanuna bağlı cetvele ve derecelere göre cezalandırılır',
            'E': 'Tekerrür hâlinde usulsüzlük cezası yüzde yirmi beş oranında artırılır',
        },
        'A',
        "**VUK m. 352:** usulsüzlük fiili **re'sen takdiri gerektirirse** bağlı cetvelde gösterilen cezalar **iki kat** olarak kesilir; artırım yapılmayacağını söyleyen ifade hükme aykırıdır.",
    ),
    # düzey 3
    '0056': patch(
        'Bir mükellefin defterleri, vergi incelemesi sırasında istenmesine rağmen ibraz edilmemiştir. İnceleme elemanı matrahı tespit edememektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'İbraz yükümlülüğünün ihlali yalnız hürriyeti bağlayıcı cezayı gerektirir; idari yönden bir tarhiyat yapılmaz',
            'B': "İbraz edilmemesi hâlinde ikmalen tarhiyat yapılır; matrah farkı belgelere dayanılarak tespit edilebildiğinden re'sen tarha gerek kalmaz",
            'C': 'İbraz edilmemesi hâlinde inceleme durdurulur; matrah tespit edilemediğinden vergi alacağı doğmamış sayılır',
            'D': "İbraz edilmeme nedeniyle matrahın defter ve belgelere dayanılarak tespitine imkân kalmadığından re'sen tarhiyat yapılır; ayrıca usulsüzlük hükümleri işler",
            'E': 'Defterlerin ibraz edilmemesi tarhiyat bakımından sonuç doğurmaz; idare mükellefin beyanıyla bağlı olduğundan matrah beyan üzerinden kesinleşir',
        },
        'D',
        "**VUK m. 256** ibrazı zorunlu kılar; ibraz edilmemesi matrahın belgelere dayanılarak tespitini imkânsız kıldığından **m. 30** uyarınca **re'sen tarh** sebebi oluşturur. Defterlerin gizlenmesi ayrıca m. 359 kapsamında değerlendirilebilir.",
    ),
    # düzey 2
    '0057': patch(
        'Mükellefin ödevleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Vergiye tabi ticaret ve sanat erbabı işe başlamayı vergi dairesine bildirmekle yükümlüdür.\n\nII. Öteden beri işe devam edenler defterlerini kullanacakları yılın sonunda tasdik ettirir.\n\nIII. Tasdike tabi defterlerin tasdik ettirilmesi mecburidir.',
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'Yalnız II',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'B',
        '**I doğru:** m. 153. **II yanlış:** m. 221/1 uyarınca tasdik, defterin kullanılacağı yıldan **önce gelen son ayda** yapılır. **III doğru:** m. 220 tasdiki mecburi kılar.',
    ),
    # düzey 3
    '0058': patch(
        'Bir işletme, ticari kazancının elde edilmesiyle ilgili olmayan, ortağına kullandırdığı kişisel bir borç için icra takibi başlatmış ve bu alacak için şüpheli alacak karşılığı ayırmak istemektedir. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Karşılık ancak alacağın tamamı tahsil edilemez hâle geldiğinde ayrılabilir; icra safhası yeterli olmadığından talep reddedilir',
            'B': 'Şüpheli alacak karşılığı ayrılabilmesi alacağın ticari ve zirai kazancın elde edilmesi ve idame ettirilmesiyle ilgili olması şartına bağlıdır; şart gerçekleşmediğinden karşılık ayrılamaz',
            'C': 'İcra takibi başlatılmış olması tek başına yeterlidir; alacağın ticari kazançla ilgisi aranmadığından ortağa kullandırılan kişisel borç için de değerleme gününün tasarruf değerine göre karşılık ayrılabilir',
            'D': 'Ortaklara kullandırılan borçlar için karşılık iki katı oranında ayrılır; kanun bu alacaklara özel bir imkân tanımıştır',
            'E': 'Kişisel alacaklar değersiz alacak sayılır ve doğrudan zarara geçirilir; bu nedenle karşılık ayrılmasına gerek kalmaz',
        },
        'B',
        '**VUK m. 323:** şüpheli alacak sayılmanın ön şartı, alacağın **ticari ve zirai kazancın elde edilmesi ve idame ettirilmesi ile ilgili** olmasıdır. Bu şart gerçekleşmedikçe dava veya icra safhasında bulunmak tek başına yeterli değildir.',
    ),
    # düzey 2
    '0059': patch(
        'Bir vergi dairesi memuru yoklama sırasında mükellefin defterlerini incelemiş ve matrah farkı bularak tarhiyat önerisinde bulunmuştur. Mükellef, yoklamanın sınırlarının aşıldığını ileri sürmektedir. Buna göre vergi denetimi ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Arama yapılabilmesi sulh yargıcının karar vermesine bağlıdır',
            'B': 'Vergi incelemesinden maksat ödenmesi gereken vergilerin doğruluğunu araştırmak ve tespit etmektir',
            'C': 'Vergi incelemesi Vergi Müfettişleri ile vergi dairesi müdürleri gibi kanunda sayılanlarca yapılır',
            'D': 'Yoklamaya yetkili memurlar, mükellefin defter ve kayıtlarını inceleyerek matrah farkı tespit etmeye ve bu farka göre tarhiyat önermeye yetkilidir',
            'E': 'Yoklamadan maksat mükellefleri ve mükellefiyetle ilgili maddi olayları araştırmak ve tespit etmek olduğundan defter incelemesi de bu kapsamda değerlendirilir ve tarhiyat önerilebilir',
        },
        'D',
        "**VUK m. 127** yoklamayı **maddi olayların tespiti** ile sınırlar; defter ve kayıtların incelenerek matrah farkı bulunması **m. 134**'teki **vergi incelemesinin** konusudur. İki denetim yolu birbirinin yerine geçmez.",
    ),
    # düzey 3
    '0060': patch(
        'Bir mükellef hakkında, sahte belge kullanmak suretiyle vergi ziyaına sebebiyet verdiği tespit edilmiş; ayrıca aynı mükellefe iki yıl önce kesinleşmiş bir vergi ziyaı cezası bulunmaktadır. Buna göre aşağıdaki ifadelerden hangisi doğrudur?',
        {
            'A': 'Kaçakçılık fiilleriyle ziyaa sebebiyet verildiğinden ceza üç kat uygulanır; ayrıca beş yıllık tekerrür süresi içinde bulunulduğundan ceza yüzde elli oranında artırılır',
            'B': 'Ceza üç kat uygulanır ancak tekerrür hükümleri işlemez; tekerrür yalnız usulsüzlük cezalarına özgü olduğundan artırım yapılmaz',
            'C': 'Ceza bir kat uygulanır ve tekerrür nedeniyle yüzde yirmi beş artırılır; vergi ziyaında artırım oranı bu şekilde belirlenmiştir',
            'D': 'Tekerrür süresi iki yıl olduğundan süre dolmuştur; bu nedenle yalnız üç kat ceza kesilir, ayrıca artırım yapılmaz',
            'E': 'Ceza yalnız bir kat uygulanır; kaçakçılık fiilleri idari cezanın miktarını etkilemediğinden yalnız ceza davası açılır ve tekerrür hükümleri de işlemez ve mükellef hakkında yalnız hürriyeti bağlayıcı ceza uygulanır',
        },
        'A',
        "**VUK m. 344/2:** kaçakçılık fiilleriyle ziyaa sebebiyet verilmesinde ceza **üç kat**. **m. 339:** vergi ziyaında tekerrür süresi **beş yıl** ve artırım oranı **%50**'dir. İki hüküm birlikte işler.",
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
    print(f"1 paket / {len(PATCHES)} soru ('Vergi Usul Kanunu' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
