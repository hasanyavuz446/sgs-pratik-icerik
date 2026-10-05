#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mesleki Degerler ve Etik — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Agustos yapisal kalibrasyonundaki olay tabanli 60 soru korunarak onarildi: genisletilmis ELEME_ISARETI olcutune gore 54 mutlak ifadeli sik ayni dogruluk degerini koruyacak bicimde yeniden yazildi; gerekce tasiyan 11 dogru sik kisaltildi. Kor ogrenci %31 -> %25.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: TURMOB Meslek Ahlak Kurallari · IESBA Etik Kurallari · 3568 sayili Kanun md. 1, 43-48 · VUK mukerrer md. 227 · TBK md. 502 vd.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/meslek_hukuku/mesleki_degerler_etik.json"
STYLE_REF = 'SGS Meslek Hukuku (gercek sinav yapisina kalibre: olay + kural uygulamasi)'
ONEK = "mh-etik-gen-"


def patch(stem, options, answer, solution, ref='TURMOB Meslek Ahlak Kurallari'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Bir meslek mensubu; hazırladığı raporda bulguları iş sahibi lehine yumuşatmış, uzmanlığı bulunmayan bir işi kabul etmiş ve müşterisinden öğrendiği bir bilgiyi kendi yatırımında kullanmıştır. Buna göre ihlal edilen temel etik ilkeler bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Gizlilik ilkesi ihlal edilmiştir; diğer davranışlar etik dışı sayılmaz',
            'B': 'Tarafsızlık, mesleki yeterlik ve özen ile gizlilik ilkeleri ihlal edilmiştir',
            'C': 'Sırasıyla gizlilik, dürüstlük ve tarafsızlık ilkeleri ihlal edilmiştir',
            'D': 'Tarafsızlık ilkesi ihlal edilmiştir; mesleki yeterlik ve gizlilik temel ilke sayılmaz',
            'E': 'İlke ihlali yoktur; üç davranış da meslek mensubunun takdirindedir',
        },
        'B',
        'Meslek Ahlak Kuralları ve IESBA temel ilkeleri: DÜRÜSTLÜK, TARAFSIZLIK, MESLEKİ YETERLİK VE ÖZEN, GİZLİLİK ve MESLEĞE UYGUN DAVRANIŞ. Bulguları taraf lehine değiştirmek tarafsızlığı, yeterliği bulunmayan işi kabul etmek mesleki yeterlik ve özeni, öğrenilen bilgiyi kendi yararına kullanmak ise gizliliği ihlal eder (3568 md. 43).',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 3
    '0002': patch(
        'Bir meslek mensubu, müşterisine ait bilgileri; (I) adli bir soruşturmada tanık olarak, (II) rakip bir firmaya ücret karşılığında, (III) kendi yatırım kararında kullanarak açıklamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'I gizlilik ihlali sayılmaz; II ve III ihlal oluşturur',
            'B': 'Üç davranış da hukuka uygundur',
            'C': 'Yalnızca II ihlal oluşturur; I ve III bakımından yasak yoktur',
            'D': 'Üç davranış da gizlilik ihlalidir',
            'E': 'I ve III ihlal oluşturur; II ihlal sayılmaz',
        },
        'A',
        '3568 md. 43: adli veya idari her türlü inceleme veya soruşturma sır saklama hükmünün kapsamı DIŞINDADIR ve TANIKLIK sırrın ifşası sayılmaz (I). Bilgiyi üçüncü kişiye aktarmak (II) ve kendi yararına kullanmak (III) ise açıkça yasaktır.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0003': patch(
        'Meslek mensubunun mesleğe uygun davranış ilkesi tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Mesleğe uygun davranış ilkesi, meslek mensubunun mesleki faaliyeti dışındaki davranışlarını da kapsayabilir',
            'B': 'İlgili mevzuata uygun davranmak bu ilkenin parçasıdır',
            'C': 'Mesleğe uygun davranış ilkesi mesleki faaliyet saatleri içindeki davranışlarla sınırlıdır',
            'D': 'İhlal disiplin sorumluluğu doğurabilir',
            'E': 'Meslek mensubu, mesleğin itibarını zedeleyecek davranışlardan kaçınmalıdır',
        },
        'C',
        'Meslek Ahlak Kuralları ve 3568 md. 45: meslek mensupları mesleğin gereği ve ONURUYLA BAĞDAŞMAYAN işlerle uğraşamaz. Mesleğe uygun davranış ilkesi, mesleğin saygınlığını zedeleyen davranışları mesleki faaliyet saatleriyle sınırlı olmaksızın kapsar.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0004': patch(
        'Bağımsızlığa yönelik tehditler belirlenmektedir. Buna göre aşağıdakilerden hangisi bu tehditlerden biri değildir?',
        {
            'A': 'Kişisel çıkar tehdidi',
            'B': 'Yakınlık ve yıldırma',
            'C': 'Kendi kendini denetleme tehdidi',
            'D': 'Mesleki eğitim yükümlülüğü',
            'E': 'Taraf tutma',
        },
        'D',
        'Bağımsızlığa yönelik tehditler kişisel çıkar, kendi kendini denetleme, taraf tutma, yakınlık ve yıldırmadır. MESLEKİ EĞİTİM bir tehdit değil, mesleki yeterliği korumaya yönelik bir yükümlülük ve aynı zamanda tehditlere karşı bir ÖNLEMDİR.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 3
    '0005': patch(
        'Bir meslek mensubu, iş sahibinin gerçeğe aykırı bir kaydı yapması yönündeki ısrarına karşı koymuş; iş sahibi sözleşmeyi sona erdirmekle ve kendisi hakkında şikâyette bulunmakla tehdit etmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İş sahibinin baskısı yıldırma tehdidi oluşturur',
            'B': 'Meslek mensubu hukuka aykırı talebi reddeder',
            'C': 'Önlemler yetersizse meslek mensubu iş ilişkisini sona erdirebilir',
            'D': 'Gerçeğe aykırı kayıt VUK ve TCK sorumluluğu doğurabilir',
            'E': 'Yazılı talimat, talebin yerine getirilmesini meşru kılar',
        },
        'E',
        'İş sahibinin baskısı yıldırma (intimidation) tehdidi oluşturur. Meslek mensubu dürüstlük ve tarafsızlık ilkeleri gereği hukuka aykırı talebi reddeder; önlemler yetersizse iş ilişkisini sona erdirir. Yazılı talimat ya da sonradan bildirim sorumluluğu kaldırmaz; gerçeğe aykırı kayıt ayrıca VUK ve TCK sorumluluğu doğurur.',
    ),
    # düzey 2
    '0006': patch(
        'Bir meslek mensubu, dürüstlüğü hakkında ciddi kuşku bulunan bir iş sahibinden gelen teklifi değerlendirmektedir. Buna göre müşteri kabulü bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu iş sahibini ve işi değerlendirmeli; kabul edilemez tehdit varsa işi almamalıdır',
            'B': 'Kabul edilen müşteri, sonradan ciddi kuşku doğsa dahi bırakılamaz',
            'C': 'Meslek mensubu her teklifi kabul etmekle yükümlüdür',
            'D': 'Müşteri kabulü aşamasında etik değerlendirme yapılması, bağlı olunan odanın yazılı iznine tabidir',
            'E': 'Değerlendirme ücretin yeterli olup olmadığıyla sınırlıdır',
        },
        'A',
        'Meslek Ahlak Kuralları: meslek mensubu bir işi kabul etmeden önce müşteriyi ve işi değerlendirir; iş sahibinin dürüstlüğüne ilişkin ciddi kuşkular kişisel çıkar ve mesleğe uygun davranış bakımından tehdit oluşturur. Önlemlerle kabul edilebilir düzeye indirilemiyorsa iş KABUL EDİLMEMELİ; devam eden işler de bırakılabilir.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0007': patch(
        'Bir meslek mensubu, hizmet verdiği bir şirketin yönetim kurulu üyeliğini kabul etmeyi planlamaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Üyeliğin iş sahibine bildirilmesi bağımsızlık sorununu gidermez',
            'B': 'Ücretsiz üyelik de bağımsızlığı tehdit eder',
            'C': 'Tehdit, meslek mensubu şirkete ortak olmasa da doğar',
            'D': 'Üyelik ayrı bir görev olduğundan etik sorun doğurmaz',
            'E': 'Meslek mensubu hizmet verdiği şirkette bu görevi almamalıdır',
        },
        'D',
        'Meslek Ahlak Kuralları ve 3568 md. 45: hizmet verilen işletmenin yönetiminde görev almak, meslek mensubunu kendi işlemlerini değerlendiren ve işletmenin çıkarını savunan bir konuma sokar. Bildirim, ücretsiz olma ya da ortaklık bulunmaması bu sakatlığı gidermez; görev alınmamalıdır.',
    ),
    # düzey 2
    '0008': patch(
        'Meslek mensubunun ücretine ilişkin etik ölçütler belirlenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tasdik gibi güvence gerektiren işlerde sonuca bağlı ücret meslek mensubunun bağımsızlığını zedeler',
            'B': 'Meslek mensubu, iş almak amacıyla asgari ücret tarifesinin altında fiyat teklif edebilir',
            'C': 'Ücret, işin kapsamı ve gerektirdiği emek gözetilerek belirlenir',
            'D': 'Ücret uyuşmazlığı meslek mensubuna belge alıkoyma hakkı vermez',
            'E': 'Asgari ücret tarifesinin altında iş kabul edilemez',
        },
        'B',
        '3568 md. 46: meslek mensupları tarifede yazılı asgari ücretin ALTINDA iş kabul edemezler; aksi davranış md. 48 uyarınca disiplin cezası gerektirir. Sonuca bağlı ücret kişisel çıkar tehdidi doğurur; ücret alacağı ise iş sahibine ait defter ve belgeler üzerinde alıkoyma hakkı vermez.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 3
    '0009': patch(
        'Bir meslek mensubu, iş sahibinin talebi üzerine gerçeğe aykırı bir kayıt yapmış ve bu kayda dayanan beyannameyi imzalamıştır. Fiil nedeniyle vergi ziyaı doğmuştur. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İş sahibinin yazılı talebi meslek mensubunun sorumluluğunu kaldırmaz',
            'B': 'Sorumluluk sözleşmeyle iş sahibine devredilemez',
            'C': 'Mali sorumluluk alınan ücretle sınırlı değildir',
            'D': 'Fiil disiplin sorumluluğu doğurur',
            'E': 'Mali sorumluluk iş sahibine aittir',
        },
        'E',
        'VUK mükerrer md. 227 meslek mensubunu imzaladığı beyannamedeki bilgilerin defter kayıtlarına ve belgelere uygunluğundan sorumlu tutar; 3568 md. 48 disiplin, genel hükümler ise cezai sorumluluk doğurur. İş sahibinin talebi sorumluluğu kaldırmaz, sorumluluk sözleşmeyle devredilemez ve ücretle sınırlı değildir.',
    ),
    # düzey 2
    '0010': patch(
        'Bir meslek mensubunun yanında çalışan bir personel, müşteriye ait bilgileri dışarıya sızdırmıştır. Meslek mensubu, fiilin kendisine ait olmadığını ileri sürmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu büroda gizliliği sağlayacak önlemleri almalıdır',
            'B': 'Yükümlülük için yazılı gizlilik sözleşmesi şart değildir',
            'C': 'Yükümlülük yanında çalışanları kapsamaz',
            'D': 'Fiile bizzat katılmamak meslek mensubunun yükümlülüğünü kaldırmaz',
            'E': 'Personelin fiili mesleki sonuç doğurabilir',
        },
        'C',
        '3568 md. 43: meslek mensupları ve yanlarında çalışanlar, işleri dolayısıyla öğrendikleri bilgi ve sırları ifşa edemezler. Meslek mensubu büro düzeni içinde gizliliği sağlayacak önlemleri almakla yükümlüdür; yazılı sözleşme koşulu aranmaz ve fiile bizzat katılmamak yükümlülüğü ortadan kaldırmaz.',
    ),
    # düzey 2
    '0011': patch(
        'Gizlilik ilkesi bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yükümlülük meslek mensubunun yanında çalışanları da kapsar',
            'B': 'Meslek mensubunun tanıklık yapması sırrın ifşası sayılmaz',
            'C': 'Yükümlülük iş ilişkisi sona erdikten sonra da devam eder',
            'D': 'Adli veya idari her türlü inceleme ve soruşturma, gizlilik yükümlülüğünün kapsamı dışında bırakılmıştır',
            'E': 'Meslek mensubu, öğrendiği bilgileri kendi yararına kullanabilir; yasak üçüncü kişilere ifşayla sınırlıdır',
        },
        'E',
        '3568 md. 43: meslek mensupları ve yanlarında çalışanlar, öğrendikleri bilgi ve sırları ifşa edemez VE KENDİ YARARLARINA KULLANAMAZLAR. Yasak her iki yönü kapsar. Adli ve idari inceleme/soruşturmalar hükmün kapsamı dışındadır ve tanıklık ifşa sayılmaz.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0012': patch(
        'Mesleki etik ilkeleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Dürüstlük, meslek mensubunun tüm mesleki ve iş ilişkilerinde doğru olmasını gerektirir. II. Tarafsızlık, mesleki yargının uygunsuz etkilerden korunmasını gerektirir. III. Gizlilik yükümlülüğü iş ilişkisinin sona ermesiyle birlikte kalkar.',
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'Yalnız I',
        },
        'B',
        'I ve II temel ilkelerin doğru ifadeleridir. III YANLIŞTIR: 3568 md. 43 ve Meslek Ahlak Kuralları uyarınca gizlilik yükümlülüğü iş ilişkisi SONA ERDİKTEN SONRA DA devam eder.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0013': patch(
        'Çıkar çatışması bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Çıkar çatışması ancak müşterilerden biri şikâyette bulunursa sonuç doğurur',
            'B': 'Çıkar çatışması belirlendiğinde ilgili tarafların bilgilendirilmesi gerekir',
            'C': 'Önlemler yeterli olmuyorsa işlerden biri bırakılır',
            'D': 'Çıkar çatışması tarafsızlığı tehdit eder',
            'E': 'Ayrı ekipler ve bilgi bariyerleri önlem olarak kullanılabilir',
        },
        'A',
        'Meslek Ahlak Kuralları: çıkar çatışması meslek mensubunun kendi değerlendirmesiyle belirlenir; müşterinin ŞİKÂYETİ koşul değildir. Çatışma belirlendiğinde bilgilendirme yapılır, önlemler alınır ve yeterli olmuyorsa iş bırakılır.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 1
    '0014': patch(
        'Bir meslek mensubu, bulgularını hiçbir tarafın etkisi altında kalmadan raporlamıştır. Buna göre uygulanan ilke aşağıdakilerden hangisidir?',
        {
            'A': 'Sürekli mesleki gelişim',
            'B': 'Gizlilik',
            'C': 'Ticari basiret',
            'D': 'Tarafsızlık',
            'E': 'Mesleki dayanışma',
        },
        'D',
        'TARAFSIZLIK (objektiflik) ilkesi, meslek mensubunun mesleki yargısını önyargı, çıkar çatışması ya da başkalarının uygunsuz etkisi altında bırakmamasını gerektirir; bulguların etkiden uzak raporlanması bu ilkenin uygulanmasıdır.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 0
    '0015': patch(
        'Bağımsızlığa yönelik tehditlerden biri, meslek mensubunun daha önce kendisinin yaptığı bir işi sonradan değerlendirmesinden doğar. Buna göre bu tehdit aşağıdakilerden hangisidir?',
        {
            'A': 'Kendi kendini denetleme tehdidi',
            'B': 'Taraf tutma',
            'C': 'Yıldırma',
            'D': 'Kişisel çıkar tehdidi',
            'E': 'Yakınlık',
        },
        'A',
        'KENDİ KENDİNİ DENETLEME (self-review) tehdidi, meslek mensubunun daha önce verdiği bir hizmetin ya da yaptığı bir işlemin sonucunu sonradan değerlendirmek durumunda kalmasından doğar; kendi işini objektif biçimde denetleyememe riski taşır.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 3
    '0016': patch(
        'Bir meslek mensubu; iş sahibinin gerçeğe aykırı beyan talebini reddetmiş, iş sahibi de sözleşmeyi sona erdirmiştir. İş sahibi daha sonra aynı işi başka bir meslek mensubuna götürmüştür. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İlk meslek mensubu doğru davranmıştır; ikinci meslek mensubunun da işi kabul öncesi değerlendirme yapması gerekir',
            'B': 'İlk meslek mensubu işi kaybettiği için hatalı davranmıştır',
            'C': 'İkinci meslek mensubu, iş sahibinin talebini yerine getirmekle yükümlüdür',
            'D': 'İlk meslek mensubu, reddettiği talebi odaya bildirmekten men edilmiştir',
            'E': 'İkinci meslek mensubu, işi devraldığı için müşteri kabulüne ve önceki meslektaşa bildirime ilişkin yükümlülük altında değildir',
        },
        'A',
        'Dürüstlük ve tarafsızlık ilkeleri gereği hukuka aykırı talep reddedilir; iş kaybı bu davranışı hatalı kılmaz. İkinci meslek mensubu ise MÜŞTERİ KABULÜ değerlendirmesi yapmalı, iş sahibinin dürüstlüğüne ilişkin kuşkuyu ve devir kurallarını (önceki meslektaşa bildirim) gözetmelidir.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0017': patch(
        'Meslek mensubunun sorumluluğu bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Aynı fiil mali ve cezai sorumluluk da doğurabilir',
            'B': 'Etik ihlali disiplin sorumluluğu doğurabilir',
            'C': 'Meslek mensubu, mesleki sorumluluk sigortası yaptırdığında kanuni sorumluluğundan kurtulur',
            'D': 'Meslek mensubu, imzaladığı beyannamedeki bilgilerin defter kayıtlarına uygunluğundan sorumludur',
            'E': 'Sorumluluk sözleşmeyle iş sahibine devredilemez',
        },
        'C',
        "Mesleki sorumluluk sigortası, doğan ZARARIN karşılanmasına yöneliktir; meslek mensubunun VUK mükerrer md. 227 ve 3568'den doğan KANUNİ sorumluluğunu ORTADAN KALDIRMAZ ve disiplin ile cezai sorumluluğu hiç etkilemez.",
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0018': patch(
        'Mesleki etik ve bağımsızlık bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bağımsızlık, denetim ve tasdik gibi güvence işlerinde kurucu koşuldur',
            'B': 'Bağımsızlık danışmanlık işlerine özgü bir ölçüttür',
            'C': 'Hizmet verilen işletmenin yönetiminde görev alınamaz',
            'D': 'Bağımsızlığa yönelik tehditler belirlenir ve önemliliği değerlendirilir',
            'E': 'Önlemler tehdidi kabul edilebilir düzeye indirmiyorsa iş bırakılır',
        },
        'B',
        'Bağımsızlık, özellikle DENETİM ve TASDİK gibi üçüncü kişilere güvence veren işlerde kurucu koşuldur; danışmanlıkla sınırlı değildir. Kavramsal çerçeve uyarınca tehdit belirlenir, değerlendirilir ve önlem alınır; yetersizse iş bırakılır.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0019': patch(
        'Bir meslek mensubu, kendisine teklif edilen bir işi bağımsızlığını koruyamayacağı gerekçesiyle reddetmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu bağımsızlığını koruyamayacağı işi kabul etmemelidir',
            'B': 'Red için odanın izni gerekmez',
            'C': 'Red haksız rekabet oluşturmaz',
            'D': 'Red gerekçesi iş sahibine açıklanabilir',
            'E': 'Red, disiplin soruşturması açılmasını gerektirir',
        },
        'E',
        'Meslek Ahlak Kuralları: meslek mensubu bağımsızlığını ve tarafsızlığını koruyamayacağı işleri kabul etmemekle yükümlüdür. Red bir yükümlülüğün yerine getirilmesi olup oda iznine bağlı değildir, gerekçesi açıklanabilir, haksız rekabet oluşturmaz ve disiplin soruşturması gerektirmez.',
    ),
    # düzey 1
    '0020': patch(
        'Bir meslek mensubu, mesleki faaliyetinde kendisine ibraz edilen belgelere dayanarak kayıt yapmıştır. Belgelerin sonradan gerçeği yansıtmadığı anlaşılmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sorumluluk sözleşmeyle kaldırılabilir',
            'B': 'Meslek mensubunun sorumluluğu doğmaz',
            'C': 'Sorumluluk yeminli mali müşavirler için doğar',
            'D': 'Meslek mensubu kayıtların belgelere uygunluğundan sorumludur; belgelerin gerçekliğini araştırma yükümlülüğü bulunmaz',
            'E': 'Meslek mensubu, kayıtların belgelere uygunluğunun yanında kendisine ibraz edilen belgelerin maddi gerçeğe uygunluğundan da ayrıca sorumludur',
        },
        'D',
        'VUK mükerrer md. 227: meslek mensubu, imzaladığı beyannamelerde yer alan bilgilerin DEFTER KAYITLARINA ve bu kayıtların dayanağını oluşturan BELGELERE uygunluğundan sorumludur; belgelerin muhteviyatının maddi gerçeğe uygun olup olmadığını araştırma yükümlülüğü yoktur. Sorumluluk kanuni olup sözleşmeyle kaldırılamaz.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0021': patch(
        'Meslek mensuplarının uyacağı temel etik ilkeler belirlenmektedir. Buna göre aşağıdakilerden hangisi bu temel ilkelerden biri değildir?',
        {
            'A': 'Gizlilik ve mesleğe uygun davranış',
            'B': 'Mesleki yeterlik ve gereken özeni gösterme ilkesi',
            'C': 'Dürüstlük',
            'D': 'Tarafsızlık',
            'E': 'İş sahibinin talimatlarına koşulsuz bağlılık',
        },
        'E',
        'Meslek Ahlak Kurallarının temel ilkeleri dürüstlük, tarafsızlık, mesleki yeterlik ve özen, gizlilik ve mesleğe uygun davranıştır. Meslek mensubu iş sahibinin TEMSİLCİSİ değildir; mevzuatla ve mesleki ilkelerle bağlıdır ve kamu yararını da gözetir. Koşulsuz bağlılık tarafsızlığa aykırıdır.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 1
    '0022': patch(
        'Bir meslek mensubu, mesleki yargısını iş sahibinin baskısı altında değiştirmiştir. Buna göre ihlal edilen ilke aşağıdakilerden hangisidir?',
        {
            'A': 'Sürekli mesleki gelişim',
            'B': 'Mesleğe uygun davranış ilkesi',
            'C': 'Tarafsızlık',
            'D': 'Gizlilik',
            'E': 'Mesleki yeterlik',
        },
        'C',
        'TARAFSIZLIK (objektiflik) ilkesi, meslek mensubunun mesleki yargısını önyargı, çıkar çatışması ya da başkalarının uygunsuz etkisi altında bırakmamasını gerektirir. İş sahibinin baskısıyla yargıyı değiştirmek doğrudan bu ilkenin ihlalidir.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0023': patch(
        'Bir meslek mensubuna, hiç deneyimi bulunmayan ve ileri uzmanlık gerektiren bir transfer fiyatlandırması işi teklif edilmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu işi kabul etmemeli ya da konunun uzmanından destek alarak yürütmelidir',
            'B': 'Ruhsat sahibi olmak her işi kabul etmek için yeterlidir',
            'C': 'Yeterlik değerlendirmesi tasdik işlerine özgüdür',
            'D': 'Meslek mensubu işi kabul edip doğacak mesleki sorumluluğu sözleşmeyle iş sahibine devredebilir',
            'E': 'İş ancak odanın yazılı izniyle kabul edilebilir',
        },
        'A',
        'Meslek Ahlak Kuralları (mesleki yeterlik ve özen): meslek mensubu gerekli bilgi, beceri ve deneyime sahip olmadığı işleri kabul etmemeli; kabul edecekse uzman desteği almalıdır. Sorumluluk iş sahibine devredilemez; ruhsat tek başına her işte yeterlik anlamına gelmez.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 3
    '0024': patch(
        'Bir meslek mensubu, tasdik hizmeti verdiği şirketin yönetim kurulunda yer alan bir yakınıyla uzun süredir ortak iş ilişkisi içindedir. Meslek mensubu durumun bağımsızlığını etkilemediğini düşünmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bağımsızlık değerlendirmesinde önce tehdit belirlenir',
            'B': 'Yakınlık ilişkileri bağımsızlık değerlendirmesinde dikkate alınmaz',
            'C': 'Tehdidin önemliliği değerlendirilir',
            'D': 'Önlem tehdidi kabul edilebilir düzeye indirmiyorsa iş kabul edilmez',
            'E': 'Durumun iş sahibine bildirilmesi tek başına yeterli önlem sayılmaz',
        },
        'B',
        'Bağımsızlık değerlendirmesi üç aşamalıdır: tehdidin belirlenmesi, önemliliğinin değerlendirilmesi ve önlem alınması. Uzun süreli ya da yakın ilişkiler yakınlık tehdidi doğurur ve değerlendirmede dikkate alınır. Önlemler tehdidi kabul edilebilir düzeye indirmiyorsa iş kabul edilmez; bildirim tek başına yeterli değildir.',
    ),
    # düzey 2
    '0025': patch(
        'Bir meslek mensubuna, tasdik hizmeti verdiği bir müşterisi tarafından yüksek değerli bir hediye sunulmuştur. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Hediye ile ilgili kısıt nakit hediyelerle sınırlı değildir',
            'B': 'Hediyenin odaya bildirilmesi kabulü uygun hâle getirmez',
            'C': 'Önemsiz ve makul düzeydeki ağırlamalar tehdit oluşturmayabilir',
            'D': 'Değerli hediye kişisel çıkar tehdidi doğurur',
            'E': 'Hediye kabulü bağımsızlık bakımından sorun doğurmaz',
        },
        'E',
        'Meslek Ahlak Kuralları: müşteriden alınan hediye ve ağırlamalar önemsiz ve makul düzeyi aşıyorsa kişisel çıkar ve yakınlık tehdidi doğurur; bu nedenle kabul edilmemelidir. Kısıt nakitle sınırlı değildir ve odaya bildirim bir önlem oluşturmaz.',
    ),
    # düzey 2
    '0026': patch(
        'Bir meslek mensubu, bağımsızlığına yönelik bir tehdit belirlemiş ve tehdidi kabul edilebilir düzeye indirecek önlemler aramaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tehdidin varlığı belirlendiğinde iş her hâlükârda reddedilir; önlem arayışına gerek yoktur',
            'B': 'Mevzuattan ve mesleki düzenlemelerden kaynaklanan önlemler bulunur',
            'C': 'Önlemler tehdidi kabul edilebilir düzeye indirmiyorsa iş kabul edilmemeli ya da bırakılmalıdır',
            'D': 'Meslek mensubu önce tehdidi belirler ve önemliliğini değerlendirir',
            'E': 'İş ortamında alınabilecek önlemler (ikinci bir meslek mensubunun gözden geçirmesi gibi) bulunur',
        },
        'A',
        'Etik kurallar KAVRAMSAL ÇERÇEVE yaklaşımını benimser: tehdit belirlenir, önemliliği değerlendirilir ve gerekiyorsa önlem alınır. Her tehdit otomatik red sonucu doğurmaz; önlemler tehdidi kabul edilebilir düzeye indiriyorsa iş yürütülebilir. İndirmiyorsa iş kabul edilmez ya da bırakılır.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 3
    '0027': patch(
        'Bir meslek mensubu, aynı ihalede karşı karşıya gelen iki şirkete de mali danışmanlık vermektedir. Meslek mensubu iki müşteriyi de bilgilendirmediğini belirtmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu çıkar çatışmasını belirlemelidir',
            'B': 'Durumdan ilgililer bilgilendirilmelidir',
            'C': 'Ayrı ekip ve bilgi bariyeri gibi önlemler alınabilir',
            'D': 'Önlem yetmezse işlerden biri bırakılır',
            'E': 'Çatışma şikâyet olursa sonuç doğurur',
        },
        'E',
        'Meslek Ahlak Kuralları: çıkar çatışması tarafsızlığı doğrudan tehdit eder. Meslek mensubu çatışmayı belirler, ilgilileri bilgilendirir ve ayrı ekipler, bilgi bariyerleri, gözden geçirme gibi önlemler alır. Önlemler yeterli olmuyorsa işlerden biri ya da her ikisi bırakılır; şikâyet koşulu aranmaz.',
    ),
    # düzey 2
    '0028': patch(
        'Bir meslek mensubu, bir işi almak için asgari ücret tarifesinin altında fiyat teklif etmiş; ayrıca rakip meslektaşının yetersiz olduğunu iş sahibine söylemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Serbest piyasa koşullarında iki davranış da hukuka uygundur',
            'B': 'Tarifenin altında teklif haksız rekabettir, meslektaş hakkındaki beyan değildir',
            'C': 'Meslektaş hakkındaki beyan haksız rekabettir, tarife altı teklif değildir',
            'D': 'Her iki davranış da haksız rekabet oluşturur ve disiplin sorumluluğu doğurur',
            'E': 'Haksız rekabet ticari işletmeler arasında söz konusu olup meslek mensuplarını kapsamaz',
        },
        'D',
        '3568 md. 46 tarifenin altında iş kabul edilemeyeceğini, md. 47 ise meslek mensupları arasında haksız rekabetin yasak olduğunu düzenler. Meslektaşı küçük düşüren beyanlar ve tarifenin altında fiyatla iş almaya çalışmak haksız rekabet sayılır; md. 48 uyarınca disiplin cezası gerektirir.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0029': patch(
        'Meslek mensubunun kamu yararını gözetme yükümlülüğü tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu iş sahibinin çıkarıyla birlikte kamu yararını da gözetir',
            'B': 'Mesleğin amacı gerçek durumu resmî mercilere de tarafsız sunmaktır',
            'C': 'Çatışmada iş sahibinin çıkarı önceliklidir',
            'D': 'Çatışma hâlinde mevzuat ve mesleki ilkeler esas alınır',
            'E': 'Kamu yararı gözetimi serbest muhasebeci mali müşavirleri de bağlar',
        },
        'C',
        '3568 md. 1: mesleğin amacı, faaliyet sonuçlarının gerçek durumunu ilgililerin ve resmî mercilerin istifadesine tarafsız biçimde sunmaktır. Meslek mensubu iş sahibinin çıkarını gözetirken kamu yararını da gözetir; çatışma hâlinde iş sahibinin çıkarı değil, mevzuat ve mesleki ilkeler esas alınır.',
    ),
    # düzey 2
    '0030': patch(
        'Mesleki etik bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu, mesleki yeterliği bulunmayan işi kabul etmemelidir',
            'B': 'Meslek mensubu, bağımsızlığını koruyamayacağı bir işi de kabul etmekle yükümlüdür',
            'C': 'Meslek mensubu, yanıltıcı bilgi içeren raporlarla ilişkilendirilmemelidir',
            'D': 'Meslek mensubu, mesleki yargısını başkalarının uygunsuz etkisi altında bırakmamalıdır',
            'E': 'Meslek mensubu, gizlilik yükümlülüğünü iş ilişkisi bittikten sonra da sürdürür',
        },
        'B',
        'Meslek Ahlak Kuralları: meslek mensubu bağımsızlığını ve tarafsızlığını koruyamayacağı işi KABUL ETMEMEKLE yükümlüdür; kabul zorunluluğu yoktur. Diğer seçenekler mesleki yeterlik, gizlilik, tarafsızlık ve dürüstlük ilkelerinin doğru ifadeleridir.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0031': patch(
        'Reklam ve iş elde etme bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İş elde etmeye yönelik reklam sayılabilecek faaliyetler yasaktır',
            'B': 'Yasak, açık ve kapalı her türlü reklamı kapsar',
            'C': 'Reklam yasağının ihlali disiplin sorumluluğu doğurur',
            'D': 'Meslek mensubu, iş elde etmek amacıyla dolaylı yollarla reklam yapabilir',
            'E': 'Tabela ve kartvizit gibi tanıtım araçları belirlenen ölçüler içinde kullanılabilir',
        },
        'D',
        '3568 md. 44: meslek mensupları iş elde etmek için AÇIK VEYA KAPALI, DOLAYLI YA DA DOLAYSIZ reklam sayılabilecek faaliyetlerde bulunamazlar. Yasak dolaylı yolları da kapsar; tabela ve kartvizit gibi araçlar ise yönetmelikte belirlenen ölçüler içinde reklam sayılmaz.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 3
    '0032': patch(
        'Bağımsızlık tehditleri ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Kişisel çıkar tehdidi, meslek mensubunun mali menfaatinden doğabilir. II. Kendi kendini denetleme tehdidi, meslek mensubunun daha önce yaptığı işi değerlendirmesinden doğar. III. Tehdit belirlendiğinde iş her hâlükârda reddedilir. IV. Yakınlık tehdidi yalnızca meslek mensubu pay sahibiyse doğar.',
        {
            'A': 'II ve III',
            'B': 'III ve IV',
            'C': 'I ve II',
            'D': 'I, III ve IV',
            'E': 'Yalnız III',
        },
        'B',
        'III YANLIŞ: kavramsal çerçeve yaklaşımı uyarınca tehdit belirlenir, önemliliği değerlendirilir ve önlem alınır; her tehdit otomatik red doğurmaz. IV YANLIŞ: yakınlık tehdidi uzun süreli ya da yakın ilişkilerden doğar, pay sahipliği koşulu aranmaz. I ve II doğrudur.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0033': patch(
        'Mesleki değerler bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu çıkar çatışması bulunan işlerde önlem alır',
            'B': 'Meslek mensubu, mesleğin itibarını zedeleyebilecek her türlü söz ve davranıştan kaçınır',
            'C': 'Meslek mensubu kamu yararını da gözetir',
            'D': 'Meslek mensubu mesleki yargısını önyargıdan uzak tutar',
            'E': 'Meslek mensubu, mesleki yargısını iş sahibinin ticari beklentilerine uyarlamakla yükümlüdür',
        },
        'E',
        'TARAFSIZLIK ilkesi, mesleki yargının önyargı, çıkar çatışması ve başkalarının uygunsuz etkisi altında bırakılmamasını gerektirir. Yargıyı iş sahibinin ticari beklentilerine uyarlamak bu ilkenin doğrudan ihlalidir.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 0
    '0034': patch(
        'Meslek Ahlak Kurallarının temel ilkelerinden biri, meslek mensubunun işleri dolayısıyla öğrendiği bilgileri korumasını gerektirir. Buna göre bu ilke aşağıdakilerden hangisidir?',
        {
            'A': 'Gizlilik',
            'B': 'Dürüstlük',
            'C': 'Mesleki yeterlik',
            'D': 'Mesleğe uygun davranış ilkesi',
            'E': 'Tarafsızlık',
        },
        'A',
        'GİZLİLİK ilkesi, meslek mensubunun mesleki ve iş ilişkileri sonucunda edindiği bilgilerin gizliliğine saygı göstermesini, bu bilgileri yetkisiz kişilere açıklamamasını ve kendi ya da üçüncü kişilerin çıkarı için kullanmamasını gerektirir (3568 md. 43).',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 0
    '0035': patch(
        'Bağımsızlığa yönelik tehditlerden biri, meslek mensubunun baskı veya tehdit altında bırakılması hâlinde doğar. Buna göre bu tehdit aşağıdakilerden hangisidir?',
        {
            'A': 'Yakınlık',
            'B': 'Kişisel çıkar tehdidi',
            'C': 'Yıldırma',
            'D': 'Taraf tutma',
            'E': 'Kendi kendini denetleme tehdidi',
        },
        'C',
        'YILDIRMA (intimidation) tehdidi, meslek mensubunun gerçek ya da algılanan baskı altında objektif davranmasının engellenmesi hâlinde doğar; sözleşmenin sona erdirilmesi ya da şikâyet tehdidi tipik örneklerdir.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0036': patch(
        'Bir meslek mensubu, bağımsızlığına yönelik bir tehdide karşı önlem aramaktadır. Buna göre aşağıdakilerden hangisi bir önlem sayılmaz?',
        {
            'A': 'Etkilenen işten ayrı bir ekip görevlendirmek',
            'B': 'Mesleki eğitim ve sürekli gelişim yükümlülüklerini uygulamak',
            'C': 'İşi ikinci bir meslek mensubunun gözden geçirmesini sağlamak',
            'D': 'Tehdidi kendi kayıtlarına not edip başka işlem yapmamak',
            'E': 'Gerektiğinde işi kabul etmemek ya da bırakmak',
        },
        'D',
        'Önlemler; mesleki düzenlemelerden kaynaklananlar (eğitim, ruhsat, disiplin sistemi) ile iş ortamındakiler (gözden geçirme, ayrı ekip, bilgi bariyeri) olarak sınıflandırılır ve gerekirse işten çekilmeye kadar gider. Tehdidi yalnızca KAYDA GEÇİRMEK, tehdidi kabul edilebilir düzeye indirmediği için önlem sayılmaz.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0037': patch(
        'Bir meslek mensubu, tasdik hizmeti verdiği işletmeye aynı dönemde muhasebe kaydı hizmeti de vermeyi planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Aynı işletmeye kayıt ve tasdik hizmeti vermek kendini denetleme tehdididir',
            'B': 'Durum iş sahibine bildirilirse tehdit ortadan kalkar',
            'C': 'Tehdit ancak meslek mensubu işletmeye ortak da olursa doğar',
            'D': 'İki hizmetin birlikte verilmesi bağımsızlık bakımından sorun doğurmaz',
            'E': 'Bağımsızlık sorunu, iki hizmetin ücretinin aynı faturada gösterilmesinden doğar',
        },
        'A',
        "Meslek mensubunun kendi tuttuğu kayıtları sonradan tasdik etmesi, kendi işini denetlemesi anlamına gelir ve KENDİ KENDİNİ DENETLEME tehdidi doğurur. Ayrıca 3568 md. 45 uyarınca YMM'ler defter tutamaz; tasdik ve kayıt işleri unvan bakımından da ayrıdır. Bildirim ya da faturalandırma biçimi bu sakatlığı gidermez.",
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0038': patch(
        'Bir meslek mensubu, mesleki faaliyeti sırasında elde ettiği belgeleri iş ilişkisi sona erdikten sonra iş sahibine vermeyi reddetmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Belgeleri geri verme yükümlülüğü yeminli mali müşavirlere özgüdür',
            'B': 'Belgeler ancak vergi dairesinin talebi üzerine geri verilir',
            'C': 'Belgeler talep hâlinde tutanakla geri verilir; ücret alacağı alıkoyma hakkı vermez',
            'D': 'Meslek mensubu belgeleri geri vermek yerine imha edebilir',
            'E': 'Meslek mensubu ücreti ödenene kadar belgeleri alıkoyabilir',
        },
        'C',
        'Meslek mevzuatı: iş sahibine ait defter ve belgeler özenle saklanır ve iş ilişkisi sona erdiğinde TUTANAKLA geri verilir. Ücret alacağı, yasal saklama yükümlülüğü bulunan bu belgeler üzerinde alıkoyma (hapis) hakkı vermez; alacak genel hükümlere göre takip edilir.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 3
    '0039': patch(
        'Bir meslek mensubu, uzun yıllar hizmet verdiği bir müşterisinin mali tablolarını her yıl aynı ekiple ve aynı yöntemle değerlendirmektedir. Müşteriyle kişisel yakınlık da gelişmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yakınlık tehdidi ancak akrabalık ilişkisi varsa doğar',
            'B': 'Yakınlık tehdidi ancak meslek mensubu müşteriden değerli bir hediye kabul ederse doğar',
            'C': 'Yakınlık tehdidi doğmuştur; ekip rotasyonu gibi önlemler alınmalıdır',
            'D': 'İlişkinin süresi bağımsızlık değerlendirmesinde dikkate alınmaz',
            'E': 'Uzun süreli ilişki güven oluşturduğu için bağımsızlığı güçlendirir',
        },
        'C',
        'YAKINLIK tehdidi, uzun süreli ya da yakın ilişkilerden doğar ve meslek mensubunun müşterinin çıkarlarına aşırı duyarlı hâle gelmesi riskini taşır. Akrabalık ya da hediye koşulu aranmaz. Önlemler ekip rotasyonu, bağımsız gözden geçirme ve gerekirse işin bırakılmasıdır.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0040': patch(
        'Meslek mensubunun kamu yararı ve iş sahibi çıkarı arasındaki konumu bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Faaliyet sonuçları, ilgililerin ve resmî mercilerin istifadesine tarafsız biçimde sunulmakla yükümlüdür',
            'B': 'Meslek mensubu mesleki ilkelerle ve mevzuatla bağlıdır',
            'C': 'Hukuka aykırı talep iş sahibinden gelse de reddedilir',
            'D': 'Meslek mensubu iş sahibinin temsilcisi değildir',
            'E': 'Kamu yararı ile iş sahibinin çıkarı çatıştığında meslek mensubu iş sahibinin çıkarını tercih eder',
        },
        'E',
        '3568 md. 1: mesleğin amacı faaliyet sonuçlarını ilgililerin VE RESMÎ MERCİLERİN istifadesine TARAFSIZ biçimde sunmaktır. Meslek mensubu iş sahibinin temsilcisi değildir; çatışma hâlinde mevzuat ve mesleki ilkeler esas alınır, iş sahibinin çıkarı öne geçmez.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0041': patch(
        'Bir meslek mensubu, önemli ölçüde yanıltıcı bilgi içerdiğini bildiği bir rapora adını koymuştur. Meslek mensubu, raporu kendisinin hazırlamadığını ileri sürmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İhlal disiplin sorumluluğu doğurabilir',
            'B': 'Raporu bizzat hazırlamayan meslek mensubu, adını koymuş olsa da dürüstlük ilkesinden sorumlu tutulamaz',
            'C': 'Meslek mensubu, önemli ölçüde yanlış ya da yanıltıcı bilgi içeren beyan ve raporlarla ilişkilendirilmemelidir',
            'D': 'Adını koymak, meslek mensubunu raporun içeriğiyle ilişkilendirir',
            'E': 'Dürüstlük ilkesi meslek mensubunun tüm mesleki ve iş ilişkilerini kapsar',
        },
        'B',
        'Meslek Ahlak Kuralları: DÜRÜSTLÜK ilkesi meslek mensubunun tüm mesleki ve iş ilişkilerinde açık sözlü ve doğru olmasını gerektirir; meslek mensubu önemli ölçüde yanlış ya da yanıltıcı bilgi içeren rapor ve beyanlarla İLİŞKİLENDİRİLMEMELİDİR. Adını koymak bu ilişkilendirmeyi kurar; raporu bizzat hazırlamamak sorumluluğu kaldırmaz.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0042': patch(
        'Bir meslek mensubu, iş ilişkisi sona eren eski bir müşterisine ait bilgileri üçüncü bir kişiye açıklamıştır. Meslek mensubu, iş ilişkisinin bittiğini gerekçe göstermektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Gizlilik yükümlülüğü iş ilişkisi sona erdikten sonra da devam eder',
            'B': 'Gizlilik yükümlülüğü yazılı sözleşmenin süresiyle sınırlıdır',
            'C': 'Eski müşteriye ait bilgilerin açıklanması ancak müşteri itiraz ederse ihlal sayılır',
            'D': 'Gizlilik yükümlülüğü yeminli mali müşavirlere özgüdür',
            'E': 'Gizlilik yükümlülüğü iş ilişkisinin sona ermesiyle birlikte kalkar',
        },
        'A',
        'Meslek Ahlak Kuralları ve 3568 md. 43: gizlilik (sır saklama) yükümlülüğü, iş ilişkisi sona erdikten SONRA da devam eder; meslek mensubu edindiği bilgileri ifşa edemez ve kendi ya da üçüncü kişilerin yararına kullanamaz. Yükümlülük unvana, sözleşme süresine ya da müşterinin itirazına bağlı değildir.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 3
    '0043': patch(
        'Bir yeminli mali müşavir; (I) tasdik hizmeti verdiği şirkette pay sahibidir, (II) daha önce kendi kurduğu muhasebe sistemini şimdi denetlemektedir, (III) tasdik ücretinin sağlanacak vergi avantajına bağlanmasını kabul etmiştir. Buna göre bu durumların karşılık geldiği bağımsızlık tehditleri sırasıyla aşağıdakilerden hangisidir?',
        {
            'A': 'Yıldırma – kendi kendini denetleme – taraf tutma',
            'B': 'Taraf tutma – kişisel çıkar – yakınlık',
            'C': 'Kendi kendini denetleme – yakınlık – taraf tutma tehdidi',
            'D': 'Yakınlık – taraf tutma – yıldırma',
            'E': 'Kişisel çıkar – kendi kendini denetleme – kişisel çıkar',
        },
        'E',
        "Bağımsızlığa yönelik beş tehdit; KİŞİSEL ÇIKAR, KENDİ KENDİNİ DENETLEME, TARAF TUTMA, YAKINLIK ve YILDIRMA'dır. Pay sahipliği ve ücretin sonuca bağlanması kişisel çıkar; kendi kurduğu sistemi denetlemek ise kendi kendini denetleme tehdidi doğurur.",
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 3
    '0044': patch(
        'Bir meslek mensubu, tasdik ücretinin mükellefe sağlanacak vergi avantajının belirli bir yüzdesi olarak belirlenmesini kabul etmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İş sahibinin yazılı onayı düzenlemeyi etik hâle getirmez',
            'B': 'Bu tür ücret tasdik işlerinde bağımsızlıkla bağdaşmaz',
            'C': 'Sonuca bağlı ücret tasdik işlerinde serbesttir',
            'D': 'Düzenleme meslek mensubunun yargısını sonuca bağlar',
            'E': 'Ücret, asgari ücret tarifesinin altına da inemez',
        },
        'C',
        'Meslek Ahlak Kuralları: koşullu (sonuca bağlı) ücret, meslek mensubunun mesleki yargısını sonuca bağladığı için kişisel çıkar tehdidi doğurur ve tasdik gibi güvence gerektiren işlerde bağımsızlıkla bağdaşmaz. İş sahibinin onayı bu sakatlığı gidermez; 3568 md. 46 ayrıca tarifenin altında iş kabulünü yasaklar.',
    ),
    # düzey 2
    '0045': patch(
        'Mesleki etik ve bağımsızlık ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Kişisel çıkar ve kendi kendini denetleme, bağımsızlığa yönelik tehditlerdendir. II. Bağımsızlık, denetim ve tasdik işlerinde özel önem taşır. III. İş elde etmek amacıyla reklam yapmak temel etik ilkelerden biridir.',
        {
            'A': 'I, II ve III',
            'B': 'I ve II',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'Yalnız I',
        },
        'B',
        'I doğrudur: tehditler kişisel çıkar, kendi kendini denetleme, taraf tutma, yakınlık ve yıldırmadır. II doğrudur: bağımsızlık özellikle güvence gerektiren denetim ve tasdik işlerinde kurucu koşuldur. III YANLIŞTIR: 3568 md. 44 iş elde etmek amacıyla reklamı YASAKLAR; bu bir etik ilke değil yasaklanan davranıştır.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 3
    '0046': patch(
        'Bir meslek mensubu, başka bir meslek mensubunun sürmekte olan müşterisini devralmak istemektedir. Önceki meslektaşın ücret alacağı ödenmemiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bildirim yükümlülüğü haksız rekabeti önlemeye yöneliktir',
            'B': 'İşi devralan meslek mensubu, önceki meslektaşına bildirimde bulunmaksızın işi kabul edebilir',
            'C': 'Önceki meslek mensubunun alacağı, yeni meslek mensubuna geçmez',
            'D': 'İşi devralacak meslek mensubu, işi kabul etmeden önce önceki meslektaşına yazılı bildirimde bulunmalıdır',
            'E': 'Ücret alacağının bulunup bulunmadığı araştırılmalıdır',
        },
        'B',
        'Meslek Ahlak Kuralları ve 3568 md. 47: bir meslektaşın işini devralmak isteyen meslek mensubu, işi kabul etmeden önce ÖNCEKİ MESLEK MENSUBUNA yazılı bildirimde bulunur ve ücret alacağı durumunu araştırır. Bu yükümlülük haksız rekabeti önler; ancak alacak yeni meslek mensubuna geçmez.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0047': patch(
        'Bir iş sahibi, mevcut meslek mensubunun görüşünden farklı bir görüş almak amacıyla başka bir meslek mensubuna başvurmuştur. Buna göre ikinci görüş verme bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İkinci görüşü serbest muhasebeci mali müşavirler de verebilir',
            'B': 'Görüş verilirken aynı olgu ve varsayımlar esas alınmalıdır',
            'C': 'İş sahibinin izniyle ilk meslektaşla iletişim kurulabilir',
            'D': 'Eksik olguya dayanma riski yeterlik ve özen bakımından tehdittir',
            'E': 'İkinci görüş vermek mesleki dayanışma gereği yasaktır',
        },
        'E',
        'Meslek Ahlak Kuralları: ikinci görüş verme, eksik olgu ve varsayımlara dayanma riski nedeniyle mesleki yeterlik ve özen bakımından tehdit doğurur. Görüş verilebilir ve unvana özgü değildir; ancak aynı olgu ve varsayımlar esas alınmalı, iş sahibinin izniyle ilk meslek mensubuyla iletişim kurulmalıdır.',
    ),
    # düzey 2
    '0048': patch(
        "Bir meslek mensubu, sosyal medya hesabından 'en düşük ücretle en hızlı hizmet' sloganıyla iş çağrısı yapmıştır. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Reklam yasağı dolaylı tanıtımı da kapsar',
            'B': 'Ücret indirimiyle iş çağrısı haksız rekabete yol açabilir',
            'C': 'Ücret bilgisi içermeyen iş tanıtımı serbesttir',
            'D': 'Reklam yasağı tüm meslek mensuplarını bağlar',
            'E': 'Sosyal medya paylaşımları yasak kapsamına girebilir',
        },
        'C',
        "3568 md. 44: meslek mensupları iş elde etmek için açık veya kapalı, dolaylı ya da dolaysız reklam sayılabilecek faaliyetlerde bulunamazlar; yasak mecra ayrımı yapmaz ve tüm meslek mensuplarını bağlar. Ücret indirimiyle iş çağrısı ayrıca md. 46 ve 47'ye aykırıdır.",
    ),
    # düzey 2
    '0049': patch(
        'Bir meslek mensubu, mesleki bilgi ve becerisini güncellemeyi ihmal etmiş; mevzuat değişikliğini bilmediği için hatalı bir beyanname düzenlemiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Mevzuatı bilmemek mazeret sayılmaz',
            'B': 'Hatalı beyannameden doğan sorumluluk meslek mensubunu da kapsar',
            'C': 'Güncelleme yükümlülüğü ruhsatın alınmasıyla sona ermez',
            'D': "Güncelleme yükümlülüğü YMM'lere özgüdür",
            'E': 'Mesleki yeterlik ve özen ilkesi güncel bilgiyi gerektirir',
        },
        'D',
        'Meslek Ahlak Kuralları (mesleki yeterlik ve özen): meslek mensubu yeterli düzeyde hizmet verebilmek için bilgi ve becerisini sürekli güncel tutmakla yükümlüdür; yükümlülük tüm meslek mensuplarını bağlar ve ruhsatla sona ermez. Mevzuatı bilmemek mazeret değildir; VUK mükerrer md. 227 uyarınca imzalanan beyannameden doğan sorumluluk meslek mensubuna aittir.',
    ),
    # düzey 2
    '0050': patch(
        'Bağımsızlık ve tarafsızlık bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tasdik hizmeti verilen şirkete ortak olmak, durum iş sahibine bildirilirse bağımsızlığı etkilemez',
            'B': 'Önlemler tehdidi kabul edilebilir düzeye indirmiyorsa iş bırakılır',
            'C': 'Önemsiz sayılamayacak hediyeler kişisel çıkar tehdidi doğurur',
            'D': 'Sonuca bağlı ücret kişisel çıkar tehdidi doğurur',
            'E': 'Hizmet verilen işletmenin yönetiminde görev almak meslek mensubunun bağımsızlığını doğrudan zedeler',
        },
        'A',
        'Meslek Ahlak Kuralları: tasdik hizmeti verilen işletmeye ORTAK olmak ya da yönetiminde görev almak bağımsızlığı doğrudan ortadan kaldırır; iş sahibine BİLDİRİM bu sakatlığı GİDERMEZ. Bildirim tek başına bir önlem değildir; tehdit kabul edilebilir düzeye inmiyorsa iş kabul edilmez ya da bırakılır.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0051': patch(
        'Meslek mensubunun iş sahibiyle ilişkisi bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İlişki kural olarak vekâlet sözleşmesidir',
            'B': 'İş sahibinin verdiği yazılı talimat, meslek mensubunun kanuni sorumluluğunu ortadan kaldırmaz',
            'C': 'Meslek mensubu, iş sahibinin yazılı talimatına dayanarak gerçeğe aykırı kayıt yapabilir',
            'D': 'Meslek mensubu mevzuatla ve mesleki ilkelerle bağlıdır',
            'E': 'Hukuka aykırı talep reddedilir; ısrar hâlinde iş bırakılabilir',
        },
        'C',
        'Meslek mensubu iş sahibinin talimatıyla değil MEVZUAT ve mesleki ilkelerle bağlıdır. Gerçeğe aykırı kayıt yapmak dürüstlük ilkesini ihlal eder; yazılı talimat sorumluluğu KALDIRMAZ ve ayrıca VUK ile TCK sorumluluğu doğurur. İlişki TBK md. 502 vd. uyarınca vekâlet sözleşmesidir.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 3
    '0052': patch(
        'Meslek mensubunun yükümlülükleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Meslek mensubu, mesleki yeterliği bulunmayan işi kabul etmemelidir. II. Meslek mensubu, asgari ücret tarifesinin altında iş kabul edemez. III. Meslek mensubu, iş elde etmek amacıyla reklam yapamaz. IV. Meslek mensubu, ücret alacağı için iş sahibinin defterlerini alıkoyabilir.',
        {
            'A': 'II ve IV',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'I, II, III ve IV',
            'E': 'I, II ve III',
        },
        'E',
        "I mesleki yeterlik ilkesinin, II 3568 md. 46'nın, III md. 44'ün gereğidir. IV YANLIŞTIR: iş sahibine ait defter ve belgeler talep hâlinde tutanakla geri verilir; ücret alacağı bunlar üzerinde alıkoyma (hapis) hakkı vermez.",
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0053': patch(
        'Etik ihlallerinin sonuçları ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Etik kural ihlali disiplin sorumluluğu doğurabilir. II. Aynı fiil ayrıca mali ve cezai sorumluluk doğurabilir. III. Disiplin süreci ceza yargılamasının sonucunu beklemek durumunda değildir.',
        {
            'A': 'I, II ve III',
            'B': 'II ve III',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'I ve III',
        },
        'A',
        'Üç ifade de doğrudur. 3568 md. 48 disiplin sorumluluğunu düzenler; VUK mükerrer md. 227 ve genel hükümler mali ve cezai sorumluluk doğurur. Disiplin, mali ve cezai sorumluluk AYRI REJİMLERDİR ve biri diğerinin sonucunu beklemez.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0054': patch(
        'Müşteri kabulü ve iş devri bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu iş sahibini ve işi kabul öncesinde değerlendirir',
            'B': 'İşi devralacak meslek mensubunun önceki meslektaşa bildirim yapması gerekmez',
            'C': 'İşi devralacak meslek mensubu, kabul öncesinde önceki meslektaşa yazılı bildirimde bulunur',
            'D': 'Bildirim yükümlülüğü haksız rekabeti önlemeye yöneliktir',
            'E': 'İş sahibinin dürüstlüğüne ilişkin ciddi kuşkular tehdit oluşturur',
        },
        'B',
        'Meslek Ahlak Kuralları ve 3568 md. 47: bir meslektaşın işini devralmak isteyen meslek mensubu, işi kabul etmeden önce önceki meslek mensubuna YAZILI BİLDİRİMDE bulunur ve ücret alacağı durumunu araştırır. Bu yükümlülük haksız rekabeti önlemeye yöneliktir.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 1
    '0055': patch(
        'Bir meslek mensubu, işini gerekli bilgi, beceri ve özenle yürütmek için mesleki gelişimini sürdürmektedir. Buna göre uygulanan ilke aşağıdakilerden hangisidir?',
        {
            'A': 'Dürüstlük',
            'B': 'Mesleğe uygun davranış ilkesi',
            'C': 'Gizlilik',
            'D': 'Mesleki yeterlik ve gereken özeni gösterme ilkesi',
            'E': 'Tarafsızlık',
        },
        'D',
        'MESLEKİ YETERLİK VE GEREKEN ÖZENİ GÖSTERME ilkesi, meslek mensubunun mesleki bilgi ve becerisini yeterli düzeyde tutmasını ve işi geçerli standartlara uygun biçimde özenle yürütmesini gerektirir; sürekli mesleki gelişim bu ilkenin gereğidir.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 0
    '0056': patch(
        'Bağımsızlığa yönelik tehditlerden biri, meslek mensubunun iş sahibinin görüşünü savunma konumuna geçmesinden doğar. Buna göre bu tehdit aşağıdakilerden hangisidir?',
        {
            'A': 'Kişisel çıkar tehdidi',
            'B': 'Taraf tutma',
            'C': 'Yıldırma',
            'D': 'Kendi kendini denetleme tehdidi',
            'E': 'Yakınlık',
        },
        'B',
        'TARAF TUTMA (advocacy) tehdidi, meslek mensubunun iş sahibinin konumunu ya da görüşünü, objektifliğini zedeleyecek ölçüde savunması hâlinde doğar; örneğin müşteri adına bir uyuşmazlıkta taraf gibi hareket etmek.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0057': patch(
        'Meslek mensuplarının birbirleriyle ilişkileri bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek örgütü, meslek mensupları arasındaki mesleki uyuşmazlıklarda arabuluculuk yapabilir',
            'B': 'Meslektaşın işini devralmak isteyen meslek mensubu ona bildirimde bulunur',
            'C': 'Meslek mensupları arasında haksız rekabet yasaktır',
            'D': 'Meslek mensubu meslektaşlarına karşı dürüstlük ilkesiyle bağlıdır',
            'E': 'Meslek mensubu, iş almak amacıyla meslektaşının yeterliği hakkında olumsuz beyanda bulunabilir',
        },
        'E',
        '3568 md. 47 meslek mensupları arasında haksız rekabeti YASAKLAR; meslektaşı küçük düşüren ya da yeterliğini kötüleyen beyanlarla iş almaya çalışmak haksız rekabet sayılır ve md. 48 uyarınca disiplin cezası gerektirir.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 2
    '0058': patch(
        'Mesleğe uygun davranış ilkesi bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İlke mesleki faaliyet saatlerindeki davranışlarla sınırlıdır',
            'B': 'İlke mevzuata uyma yükümlülüğünü kapsar',
            'C': 'İlke mesleğin itibarını korumayı amaçlar',
            'D': 'İlke tüm meslek mensuplarını bağlar',
            'E': 'İlkenin ihlali şikâyet olmadan da sonuç doğurur',
        },
        'A',
        "Mesleğe uygun davranış ilkesi, meslek mensubunun ilgili mevzuata uymasını ve mesleğin itibarını zedeleyebilecek davranışlardan kaçınmasını gerektirir (3568 md. 45'teki 'mesleğin gereği ve onuruyla bağdaşmayan işler' yasağıyla bağlantılı). İlke faaliyet saatleriyle sınırlı değildir, tüm meslek mensuplarını bağlar ve şikâyete bağlı değildir.",
    ),
    # düzey 2
    '0059': patch(
        'Bir meslek mensubu, mesleki faaliyeti dolayısıyla öğrendiği bir bilgiyi, kanunla yetkili kılınmış bir idari inceleme kapsamında istenmesi üzerine idareye vermiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu bilgiyi vermeyerek gizliliği korumakla yükümlüydü',
            'B': 'Gizlilik yükümlülüğü mutlak olup hiçbir istisna tanımaz',
            'C': 'Adli ve idari inceleme ve soruşturmalar gizlilik yükümlülüğünün kapsamı dışındadır',
            'D': 'Bilgi ancak iş sahibinin yazılı onayıyla verilebilirdi',
            'E': 'İdareye bilgi verme yükümlülüğü yeminli mali müşavirlere özgüdür',
        },
        'C',
        '3568 md. 43: meslek mensupları işleri dolayısıyla öğrendikleri bilgi ve sırları ifşa edemezler; ancak ADLİ VEYA İDARİ HER TÜRLÜ İNCELEME VEYA SORUŞTURMA bu hükmün kapsamı DIŞINDADIR. Kanunla yetkili kılınmış merciin talebi karşısında bilgi verilmesi gizlilik ihlali sayılmaz ve iş sahibinin onayı aranmaz.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
    ),
    # düzey 3
    '0060': patch(
        'Mesleki değerler ve etik ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Temel ilkeler dürüstlük, tarafsızlık, mesleki yeterlik ve özen, gizlilik ve mesleğe uygun davranıştır. II. Sonuca bağlı ücret, tasdik işlerinde bağımsızlığı zedeler. III. Gizlilik yükümlülüğü hiçbir istisna tanımaz. IV. Bağımsızlık tehdidi belirlendiğinde iş her hâlükârda reddedilir.',
        {
            'A': 'II ve III',
            'B': 'Yalnız III',
            'C': 'I, III ve IV',
            'D': 'I ve II',
            'E': 'III ve IV',
        },
        'E',
        'III YANLIŞ: 3568 md. 43 uyarınca adli ve idari inceleme ve soruşturmalar gizlilik hükmünün kapsamı dışındadır; tanıklık ifşa sayılmaz. IV YANLIŞ: kavramsal çerçeve uyarınca tehdit belirlenir, önemliliği değerlendirilir ve önlem alınır; her tehdit otomatik red doğurmaz. I ve II doğrudur.',
        '3568 sayili Kanun / Meslek Ahlak Kurallari',
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
    print(f"1 paket / {len(PATCHES)} soru ('Mesleki Degerler ve Etik' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
