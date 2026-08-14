#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mesleki Degerler ve Etik — YAPISAL kalibrasyon (tanim -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turunun 6. konusu. Paketin 60 sorusunun TAMAMI
yeniden yazildi.

    olcut              gercek   bu paket (once)
    medyan kok            257              131
    olumsuz kok         %41,5               %5
    duz tanim            %6,2              %55   <- ASIL KUSUR

⚠️ SAHIPLIK DEVRI: bu paket v167'de yalniz boy-cilasi almisti ve
build_legal_oncul_cleanup.py mh-etik-gen-0015'i tutuyordu. 60 sorunun tamami bu
turda yeniden yazildigi icin o kayit eski builder'dan CIKARILDI — Codex'in
v178'de uyguladigi yontem. Bir sorunun tek sahibi olmali; aksi hâlde iki builder
ayni metne yazar ve --check sirasa bagimli hale gelir.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL; ilk tasarim 44/60 (%73)
cikip uretimi DURDURDU, 62 celdirici dogru sikla PARALEL yapiya tasinarak %20) ve
§1 bilissel duzey (0 = 4 <=6 · 0+1 = 8 <=24 · duzey 2 = 39 >=24 · duzey 3 = 13 >=12).

Icerik: bes temel ilke (durustluk, tarafsizlik, mesleki yeterlik ve ozen,
gizlilik, meslege uygun davranis) ve bes bagimsizlik tehdidi (kisisel cikar,
kendi kendini denetleme, taraf tutma, yakinlik, yildirma) OLAYA uygulatiliyor;
kavramsal cerceve yaklasimi (tehdit -> onemlilik -> onlem -> gerekirse isi
birakma) paketin omurgasi.

Dayanak: TURMOB Meslek Ahlak Kurallari · IESBA Etik Kurallari temel ilkeleri ve
bagimsizlik tehditleri · 3568 sayili Kanun md. 1, 43, 44, 45, 46, 47, 48 ·
VUK mukerrer md. 227 · TBK md. 502 vd.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/meslek_hukuku/mesleki_degerler_etik.json"
STYLE_REF = "SGS Meslek Hukuku (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "mh-etik-gen-"


def patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": "3568 sayili Kanun / Meslek Ahlak Kurallari"},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Bir meslek mensubu; hazırladığı raporda bulguları iş sahibi lehine yumuşatmış, uzmanlığı bulunmayan bir işi kabul etmiş ve müşterisinden öğrendiği bir bilgiyi kendi yatırımında kullanmıştır. Buna göre ihlal edilen temel etik ilkeler bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Hiçbir ilke ihlal edilmemiştir; üç davranış da meslek mensubunun takdirindedir',
            'B': 'Sırasıyla tarafsızlık, mesleki yeterlik ve özen ile gizlilik ilkeleri ihlal edilmiştir',
            'C': 'Yalnızca gizlilik ilkesi ihlal edilmiştir; diğer davranışlar etik dışı sayılmaz',
            'D': 'Sırasıyla gizlilik, dürüstlük ve tarafsızlık ilkeleri ihlal edilmiştir',
            'E': 'Yalnızca tarafsızlık ilkesi ihlal edilmiştir; mesleki yeterlik ve gizlilik temel ilke sayılmaz',
        },
        'B',
        'Meslek Ahlak Kuralları ve IESBA temel ilkeleri: DÜRÜSTLÜK, TARAFSIZLIK, MESLEKİ YETERLİK VE ÖZEN, GİZLİLİK ve MESLEĞE UYGUN DAVRANIŞ. Bulguları taraf lehine değiştirmek tarafsızlığı, yeterliği bulunmayan işi kabul etmek mesleki yeterlik ve özeni, öğrenilen bilgiyi kendi yararına kullanmak ise gizliliği ihlal eder (3568 md. 43).',
    ),
    # düzey 2
    '0002': patch(
        'Meslek mensuplarının uyacağı temel etik ilkeler belirlenmektedir. Buna göre aşağıdakilerden hangisi bu temel ilkelerden biri değildir?',
        {
            'A': 'İş sahibinin talimatlarına koşulsuz bağlılık',
            'B': 'Dürüstlük',
            'C': 'Mesleki yeterlik ve gereken özeni gösterme ilkesi',
            'D': 'Gizlilik ve mesleğe uygun davranış',
            'E': 'Tarafsızlık',
        },
        'A',
        'Meslek Ahlak Kurallarının temel ilkeleri dürüstlük, tarafsızlık, mesleki yeterlik ve özen, gizlilik ve mesleğe uygun davranıştır. Meslek mensubu iş sahibinin TEMSİLCİSİ değildir; mevzuatla ve mesleki ilkelerle bağlıdır ve kamu yararını da gözetir. Koşulsuz bağlılık tarafsızlığa aykırıdır.',
    ),
    # düzey 2
    '0003': patch(
        'Bir meslek mensubu, önemli ölçüde yanıltıcı bilgi içerdiğini bildiği bir rapora adını koymuştur. Meslek mensubu, raporu kendisinin hazırlamadığını ileri sürmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Adını koymak, meslek mensubunu raporun içeriğiyle ilişkilendirir',
            'B': 'Dürüstlük ilkesi meslek mensubunun tüm mesleki ve iş ilişkilerini kapsar',
            'C': 'Raporu bizzat hazırlamayan meslek mensubu, adını koymuş olsa da dürüstlük ilkesinden sorumlu tutulamaz',
            'D': 'İhlal disiplin sorumluluğu doğurabilir',
            'E': 'Meslek mensubu, önemli ölçüde yanlış ya da yanıltıcı bilgi içeren beyan ve raporlarla ilişkilendirilmemelidir',
        },
        'C',
        'Meslek Ahlak Kuralları: DÜRÜSTLÜK ilkesi meslek mensubunun tüm mesleki ve iş ilişkilerinde açık sözlü ve doğru olmasını gerektirir; meslek mensubu önemli ölçüde yanlış ya da yanıltıcı bilgi içeren rapor ve beyanlarla İLİŞKİLENDİRİLMEMELİDİR. Adını koymak bu ilişkilendirmeyi kurar; raporu bizzat hazırlamamak sorumluluğu kaldırmaz.',
    ),
    # düzey 1
    '0004': patch(
        'Bir meslek mensubu, mesleki yargısını iş sahibinin baskısı altında değiştirmiştir. Buna göre ihlal edilen ilke aşağıdakilerden hangisidir?',
        {
            'A': 'Mesleki yeterlik',
            'B': 'Gizlilik',
            'C': 'Mesleğe uygun davranış ilkesi',
            'D': 'Tarafsızlık',
            'E': 'Sürekli mesleki gelişim',
        },
        'D',
        'TARAFSIZLIK (objektiflik) ilkesi, meslek mensubunun mesleki yargısını önyargı, çıkar çatışması ya da başkalarının uygunsuz etkisi altında bırakmamasını gerektirir. İş sahibinin baskısıyla yargıyı değiştirmek doğrudan bu ilkenin ihlalidir.',
    ),
    # düzey 2
    '0005': patch(
        'Bir meslek mensubu, iş ilişkisi sona eren eski bir müşterisine ait bilgileri üçüncü bir kişiye açıklamıştır. Meslek mensubu, iş ilişkisinin bittiğini gerekçe göstermektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Gizlilik yükümlülüğü yalnızca yeminli mali müşavirler için öngörülmüştür',
            'B': 'Gizlilik yükümlülüğü yalnızca yazılı sözleşme süresince geçerlidir',
            'C': 'Gizlilik yükümlülüğü iş ilişkisinin sona ermesiyle birlikte kalkar',
            'D': 'Eski müşteriye ait bilgilerin açıklanması yalnızca müşteri itiraz ederse ihlal sayılır',
            'E': 'Gizlilik yükümlülüğü iş ilişkisi sona erdikten sonra da devam eder',
        },
        'E',
        'Meslek Ahlak Kuralları ve 3568 md. 43: gizlilik (sır saklama) yükümlülüğü, iş ilişkisi sona erdikten SONRA da devam eder; meslek mensubu edindiği bilgileri ifşa edemez ve kendi ya da üçüncü kişilerin yararına kullanamaz. Yükümlülük unvana, sözleşme süresine ya da müşterinin itirazına bağlı değildir.',
    ),
    # düzey 3
    '0006': patch(
        'Bir meslek mensubu, müşterisine ait bilgileri; (I) adli bir soruşturmada tanık olarak, (II) rakip bir firmaya ücret karşılığında, (III) kendi yatırım kararında kullanarak açıklamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'I gizlilik ihlali sayılmaz; II ve III ihlal oluşturur',
            'B': 'Üç davranış da hukuka uygundur',
            'C': 'Üç davranış da gizlilik ihlalidir',
            'D': 'Yalnızca II ihlal oluşturur; I ve III bakımından yasak yoktur',
            'E': 'I ve III ihlal oluşturur; II ihlal sayılmaz',
        },
        'A',
        '3568 md. 43: adli veya idari her türlü inceleme veya soruşturma sır saklama hükmünün kapsamı DIŞINDADIR ve TANIKLIK sırrın ifşası sayılmaz (I). Bilgiyi üçüncü kişiye aktarmak (II) ve kendi yararına kullanmak (III) ise açıkça yasaktır.',
    ),
    # düzey 2
    '0007': patch(
        'Bir meslek mensubuna, hiç deneyimi bulunmayan ve ileri uzmanlık gerektiren bir transfer fiyatlandırması işi teklif edilmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ruhsat sahibi olmak her işi kabul etmek için yeterlidir',
            'B': 'Yeterlik değerlendirmesi yalnızca tasdik işlerinde yapılır',
            'C': 'Meslek mensubu işi kabul edip doğacak mesleki sorumluluğu sözleşmeyle iş sahibine devredebilir',
            'D': 'Meslek mensubu işi kabul etmemeli ya da konunun uzmanından destek alarak yürütmelidir',
            'E': 'İş ancak odanın yazılı izniyle kabul edilebilir',
        },
        'D',
        'Meslek Ahlak Kuralları (mesleki yeterlik ve özen): meslek mensubu gerekli bilgi, beceri ve deneyime sahip olmadığı işleri kabul etmemeli; kabul edecekse uzman desteği almalıdır. Sorumluluk iş sahibine devredilemez; ruhsat tek başına her işte yeterlik anlamına gelmez.',
    ),
    # düzey 2
    '0008': patch(
        'Meslek mensubunun mesleğe uygun davranış ilkesi tartışılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İlgili mevzuata uygun davranmak bu ilkenin parçasıdır',
            'B': 'Mesleğe uygun davranış ilkesi yalnızca mesleki faaliyet saatleri içindeki davranışları kapsar',
            'C': 'Mesleğe uygun davranış ilkesi, meslek mensubunun mesleki faaliyeti dışındaki davranışlarını da kapsayabilir',
            'D': 'Meslek mensubu, mesleğin itibarını zedeleyecek davranışlardan kaçınmalıdır',
            'E': 'İhlal disiplin sorumluluğu doğurabilir',
        },
        'B',
        'Meslek Ahlak Kuralları ve 3568 md. 45: meslek mensupları mesleğin gereği ve ONURUYLA BAĞDAŞMAYAN işlerle uğraşamaz. Mesleğe uygun davranış ilkesi, mesleğin saygınlığını zedeleyen davranışları mesleki faaliyet saatleriyle sınırlı olmaksızın kapsar.',
    ),
    # düzey 3
    '0009': patch(
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
    ),
    # düzey 2
    '0010': patch(
        'Bağımsızlığa yönelik tehditler belirlenmektedir. Buna göre aşağıdakilerden hangisi bu tehditlerden biri değildir?',
        {
            'A': 'Yakınlık ve yıldırma',
            'B': 'Kendi kendini denetleme tehdidi',
            'C': 'Mesleki eğitim yükümlülüğü',
            'D': 'Kişisel çıkar tehdidi',
            'E': 'Taraf tutma',
        },
        'C',
        'Bağımsızlığa yönelik tehditler kişisel çıkar, kendi kendini denetleme, taraf tutma, yakınlık ve yıldırmadır. MESLEKİ EĞİTİM bir tehdit değil, mesleki yeterliği korumaya yönelik bir yükümlülük ve aynı zamanda tehditlere karşı bir ÖNLEMDİR.',
    ),
    # düzey 3
    '0011': patch(
        'Bir meslek mensubu, tasdik hizmeti verdiği şirketin yönetim kurulunda yer alan bir yakınıyla uzun süredir ortak iş ilişkisi içindedir. Meslek mensubu durumun bağımsızlığını etkilemediğini düşünmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubunun kendi yaptığı değerlendirme yeterlidir; ayrıca önlem alınmasına gerek yoktur',
            'B': 'Tehdit yalnızca meslek mensubu doğrudan pay sahibiyse doğar',
            'C': 'Durum iş sahibine bildirilirse bağımsızlık sorunu ortadan kalkar',
            'D': 'Yakınlık ilişkileri bağımsızlık değerlendirmesinde dikkate alınmaz',
            'E': 'Yakınlık tehdidi doğduğundan önlem alınmalı; önlem yeterli olmuyorsa iş kabul edilmemelidir',
        },
        'E',
        'Bağımsızlık değerlendirmesi ÜÇ AŞAMALIDIR: tehdidin belirlenmesi, önemliliğinin değerlendirilmesi ve önlem alınması. YAKINLIK tehdidi uzun süreli veya yakın ilişkilerden doğar; kişisel pay sahipliği aranmaz. Önlemler tehdidi kabul edilebilir düzeye indirmiyorsa iş KABUL EDİLMEMELİ ya da bırakılmalıdır. Bildirim tek başına yeterli bir önlem değildir.',
    ),
    # düzey 3
    '0012': patch(
        'Bir meslek mensubu, tasdik ücretinin mükellefe sağlanacak vergi avantajının belirli bir yüzdesi olarak belirlenmesini kabul etmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Düzenleme iş sahibinin yazılı onayı bulunması hâlinde etik hâle gelir',
            'B': 'Ücretin sonuca bağlanması kişisel çıkar tehdidi doğurur ve tasdik işlerinde bağımsızlıkla bağdaşmaz',
            'C': 'Düzenleme yalnızca asgari ücret tarifesi bakımından sorun doğurur; meslek mensubunun bağımsızlığını etkilemez',
            'D': 'Ücretin serbestçe belirlenmesi mümkün olduğundan bu düzenleme etik açıdan sorun doğurmaz',
            'E': 'Sonuca bağlı ücret yalnızca danışmanlık işlerinde yasaktır',
        },
        'B',
        'Meslek Ahlak Kuralları: koşullu (sonuca bağlı) ücret, meslek mensubunun mesleki yargısını sonuca bağladığı için KİŞİSEL ÇIKAR tehdidi doğurur ve tasdik gibi güvence gerektiren işlerde bağımsızlıkla bağdaşmaz. Ayrıca 3568 md. 46 asgari ücret tarifesinin altında iş kabul edilemeyeceğini düzenler; iş sahibinin onayı bu sakatlığı gidermez.',
    ),
    # düzey 2
    '0013': patch(
        'Bir meslek mensubuna, tasdik hizmeti verdiği bir müşterisi tarafından yüksek değerli bir hediye sunulmuştur. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Önemsiz sayılamayacak hediye ve ağırlamalar kişisel çıkar tehdidi doğurduğundan kabul edilmemelidir',
            'B': 'Hediye kabulü meslek mensubunun kişisel takdirinde olup bağımsızlık bakımından herhangi bir etik sorun doğurmaz',
            'C': 'Hediye, değeri odaya bildirilirse kabul edilebilir',
            'D': 'Hediye yasağı yalnızca kamu görevlileri için öngörülmüştür',
            'E': 'Hediye ancak nakit olarak verildiğinde etik sorun doğurur',
        },
        'A',
        'Meslek Ahlak Kuralları: müşteriden alınan hediye ve ağırlamalar, önemsiz ve makul kabul edilebilir düzeyi aşıyorsa KİŞİSEL ÇIKAR ve YAKINLIK tehdidi doğurur; bu nedenle kabul edilmemelidir. Yasak nakitle sınırlı değildir ve odaya bildirim bir önlem oluşturmaz.',
    ),
    # düzey 3
    '0014': patch(
        'Bir meslek mensubu, iş sahibinin gerçeğe aykırı bir kaydı yapması yönündeki ısrarına karşı koymuş; iş sahibi sözleşmeyi sona erdirmekle ve kendisi hakkında şikâyette bulunmakla tehdit etmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu ancak yazılı talimat alırsa talebi yerine getirebilir',
            'B': 'Tehdit hâlinde meslek mensubunun sorumluluğu ortadan kalkar',
            'C': 'Meslek mensubu talebi yerine getirip durumu sonradan bağlı olduğu odaya bildirebilir',
            'D': 'Yıldırma tehdidi doğmuştur; meslek mensubu talebi reddeder ve gerekirse işi bırakır',
            'E': 'Meslek mensubu, işini kaybetmemek için talebi yerine getirebilir',
        },
        'D',
        'İş sahibinin baskısı YILDIRMA (intimidation) tehdidi oluşturur. Meslek mensubu dürüstlük ve tarafsızlık ilkeleri gereği hukuka aykırı talebi reddeder; önlemler yetersizse iş ilişkisini sona erdirir. Yazılı talimat ya da sonradan bildirim sorumluluğu KALDIRMAZ; gerçeğe aykırı kayıt ayrıca VUK ve TCK sorumluluğu doğurur.',
    ),
    # düzey 2
    '0015': patch(
        'Mesleki etik ve bağımsızlık ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Kişisel çıkar ve kendi kendini denetleme, bağımsızlığa yönelik tehditlerdendir. II. Bağımsızlık, denetim ve tasdik işlerinde özel önem taşır. III. İş elde etmek amacıyla reklam yapmak temel etik ilkelerden biridir.',
        {
            'A': 'I ve II',
            'B': 'II ve III',
            'C': 'I ve III',
            'D': 'Yalnız I',
            'E': 'I, II ve III',
        },
        'A',
        'I doğrudur: tehditler kişisel çıkar, kendi kendini denetleme, taraf tutma, yakınlık ve yıldırmadır. II doğrudur: bağımsızlık özellikle güvence gerektiren denetim ve tasdik işlerinde kurucu koşuldur. III YANLIŞTIR: 3568 md. 44 iş elde etmek amacıyla reklamı YASAKLAR; bu bir etik ilke değil yasaklanan davranıştır.',
    ),
    # düzey 2
    '0016': patch(
        'Bir meslek mensubu, bağımsızlığına yönelik bir tehdit belirlemiş ve tehdidi kabul edilebilir düzeye indirecek önlemler aramaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tehdidin varlığı belirlendiğinde iş her hâlükârda reddedilir; önlem arayışına gerek yoktur',
            'B': 'İş ortamında alınabilecek önlemler (ikinci bir meslek mensubunun gözden geçirmesi gibi) bulunur',
            'C': 'Meslek mensubu önce tehdidi belirler ve önemliliğini değerlendirir',
            'D': 'Mevzuattan ve mesleki düzenlemelerden kaynaklanan önlemler bulunur',
            'E': 'Önlemler tehdidi kabul edilebilir düzeye indirmiyorsa iş kabul edilmemeli ya da bırakılmalıdır',
        },
        'A',
        'Etik kurallar KAVRAMSAL ÇERÇEVE yaklaşımını benimser: tehdit belirlenir, önemliliği değerlendirilir ve gerekiyorsa önlem alınır. Her tehdit otomatik red sonucu doğurmaz; önlemler tehdidi kabul edilebilir düzeye indiriyorsa iş yürütülebilir. İndirmiyorsa iş kabul edilmez ya da bırakılır.',
    ),
    # düzey 3
    '0017': patch(
        'Bir meslek mensubu, aynı ihalede karşı karşıya gelen iki şirkete de mali danışmanlık vermektedir. Meslek mensubu iki müşteriyi de bilgilendirmediğini belirtmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İki müşteriye hizmet vermek serbest olduğundan etik bir sorun doğmaz',
            'B': 'Çıkar çatışması ancak müşterilerden biri şikâyet ederse sonuç doğurur',
            'C': 'Çıkar çatışması doğmuştur; taraflar bilgilendirilmeli ve önlem yeterli olmuyorsa işlerden biri bırakılmalıdır',
            'D': 'Çıkar çatışması yalnızca tasdik işlerinde söz konusu olur',
            'E': 'Meslek mensubu her iki işi de sürdürebilir; yalnızca ücretleri ayrı ayrı faturalandırması ve kayıt tutması yeterlidir',
        },
        'C',
        'Meslek Ahlak Kuralları: çıkar çatışması, meslek mensubunun tarafsızlığını doğrudan tehdit eder. Meslek mensubu çatışmayı belirler, ilgilileri BİLGİLENDİRİR ve gerekli önlemleri (ayrı ekipler, bilgi bariyerleri, gözden geçirme) alır. Önlemler yeterli olmuyorsa işlerden biri ya da her ikisi bırakılır; şikâyet koşulu aranmaz.',
    ),
    # düzey 2
    '0018': patch(
        'Bir meslek mensubu, dürüstlüğü hakkında ciddi kuşku bulunan bir iş sahibinden gelen teklifi değerlendirmektedir. Buna göre müşteri kabulü bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Değerlendirme yalnızca ücretin yeterli olup olmadığına ilişkindir',
            'B': 'Meslek mensubu iş sahibini ve işi değerlendirmeli; kabul edilemez tehdit varsa işi almamalıdır',
            'C': 'Müşteri kabulü aşamasında etik değerlendirme yapılması, bağlı olunan odanın yazılı iznine tabidir',
            'D': 'Meslek mensubu her teklifi kabul etmekle yükümlüdür',
            'E': 'Kabul edilen müşteri, sonradan ciddi kuşku doğsa dahi bırakılamaz',
        },
        'B',
        'Meslek Ahlak Kuralları: meslek mensubu bir işi kabul etmeden önce müşteriyi ve işi değerlendirir; iş sahibinin dürüstlüğüne ilişkin ciddi kuşkular kişisel çıkar ve mesleğe uygun davranış bakımından tehdit oluşturur. Önlemlerle kabul edilebilir düzeye indirilemiyorsa iş KABUL EDİLMEMELİ; devam eden işler de bırakılabilir.',
    ),
    # düzey 3
    '0019': patch(
        'Bir meslek mensubu, başka bir meslek mensubunun sürmekte olan müşterisini devralmak istemektedir. Önceki meslektaşın ücret alacağı ödenmemiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Önceki meslek mensubunun alacağı, yeni meslek mensubuna geçmez',
            'B': 'Ücret alacağının bulunup bulunmadığı araştırılmalıdır',
            'C': 'Bildirim yükümlülüğü haksız rekabeti önlemeye yöneliktir',
            'D': 'İşi devralacak meslek mensubu, işi kabul etmeden önce önceki meslektaşına yazılı bildirimde bulunmalıdır',
            'E': 'İşi devralan meslek mensubu, önceki meslektaşına bildirimde bulunmaksızın işi kabul edebilir',
        },
        'E',
        'Meslek Ahlak Kuralları ve 3568 md. 47: bir meslektaşın işini devralmak isteyen meslek mensubu, işi kabul etmeden önce ÖNCEKİ MESLEK MENSUBUNA yazılı bildirimde bulunur ve ücret alacağı durumunu araştırır. Bu yükümlülük haksız rekabeti önler; ancak alacak yeni meslek mensubuna geçmez.',
    ),
    # düzey 2
    '0020': patch(
        'Bir iş sahibi, mevcut meslek mensubunun görüşünden farklı bir görüş almak amacıyla başka bir meslek mensubuna başvurmuştur. Buna göre ikinci görüş verme bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İkinci görüş, ilk meslek mensubunun yazılı onayı alınmadıkça ve olgular yeniden incelenmedikçe verilemez',
            'B': 'İkinci görüş yalnızca yeminli mali müşavirler tarafından verilebilir',
            'C': 'İkinci görüş verilmesi mesleki dayanışma gereği tümüyle yasaktır',
            'D': 'İkinci görüş verilebilir; ancak aynı olgu ve varsayımlara dayanılması ve gerektiğinde ilk meslek mensubuyla iletişim kurulması gerekir',
            'E': 'İkinci görüş verilirken olgu ve varsayımların araştırılması gerekmez',
        },
        'D',
        'Meslek Ahlak Kuralları: ikinci görüş verme, eksik olgu ve varsayımlara dayanma riski nedeniyle mesleki yeterlik ve özen bakımından tehdit doğurur. Görüş verilebilir; ancak aynı olgu ve varsayımlar esas alınmalı ve iş sahibinin izniyle ilk meslek mensubuyla iletişim kurularak bilgi tamamlanmalıdır.',
    ),
    # düzey 2
    '0021': patch(
        'Bir meslek mensubu, hizmet verdiği bir şirketin yönetim kurulu üyeliğini kabul etmeyi planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yönetim kurulu üyeliği mesleki faaliyetten tümüyle ayrı bir görev olduğundan bağımsızlık bakımından herhangi bir etik sorun doğurmaz',
            'B': 'Tehdit yalnızca meslek mensubu şirkete ortak da olursa doğar',
            'C': 'Yalnızca ücretli yönetim kurulu üyeliği tehdit doğurur',
            'D': 'Üyelik, iş sahibine bildirilirse bağımsızlık sorunu ortadan kalkar',
            'E': 'Yönetim kurulu üyeliği kendi kendini denetleme ve taraf tutma tehdidi doğurur; hizmet verilen şirkette bu görev alınamaz',
        },
        'E',
        'Meslek Ahlak Kuralları ve 3568 md. 45: hizmet verilen işletmenin yönetiminde görev almak, meslek mensubunu kendi işlemlerini denetleyen konuma sokar (KENDİ KENDİNİ DENETLEME) ve işletmenin çıkarını savunma konumuna taşır (TARAF TUTMA). Bildirim, ücretsiz olma ya da ortaklık bulunmaması bu sakatlığı gidermez.',
    ),
    # düzey 2
    '0022': patch(
        'Bir meslek mensubu, bir işi almak için asgari ücret tarifesinin altında fiyat teklif etmiş; ayrıca rakip meslektaşının yetersiz olduğunu iş sahibine söylemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Serbest piyasa koşullarında iki davranış da hukuka uygundur',
            'B': 'Yalnızca tarifenin altında teklif haksız rekabet oluşturur',
            'C': 'Her iki davranış da haksız rekabet oluşturur ve disiplin sorumluluğu doğurur',
            'D': 'Yalnızca meslektaş hakkındaki beyan haksız rekabet oluşturur',
            'E': 'Haksız rekabet yalnızca ticari işletmeler arasında söz konusu olup meslek mensuplarını kapsamaz',
        },
        'C',
        '3568 md. 46 tarifenin altında iş kabul edilemeyeceğini, md. 47 ise meslek mensupları arasında haksız rekabetin yasak olduğunu düzenler. Meslektaşı küçük düşüren beyanlar ve tarifenin altında fiyatla iş almaya çalışmak haksız rekabet sayılır; md. 48 uyarınca disiplin cezası gerektirir.',
    ),
    # düzey 2
    '0023': patch(
        "Bir meslek mensubu, sosyal medya hesabından 'en düşük ücretle en hızlı hizmet' sloganıyla iş çağrısı yapmıştır. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İş elde etmeye yönelik bu tanıtım reklam yasağı kapsamındadır ve yapılamaz',
            'B': 'Reklam yasağı yalnızca yeminli mali müşavirleri bağlar',
            'C': 'İş elde etmeye yönelik tanıtım serbesttir; yalnızca ücret bilgisi verilmesi yasaktır',
            'D': 'Sosyal medya paylaşımları reklam yasağı dışındadır',
            'E': 'Reklam yasağı yalnızca basılı ilanlar için geçerlidir',
        },
        'A',
        "3568 md. 44: meslek mensupları iş elde etmek için açık veya kapalı, dolaylı ya da dolaysız REKLAM SAYILABİLECEK faaliyetlerde bulunamazlar. Yasak mecra ayrımı yapmaz; sosyal medya da kapsamdadır ve tüm meslek mensuplarını bağlar. Ayrıca ücret indirimiyle iş çağrısı md. 46 ve 47'ye de aykırıdır.",
    ),
    # düzey 2
    '0024': patch(
        'Meslek mensubunun ücretine ilişkin etik ölçütler belirlenmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tasdik gibi güvence gerektiren işlerde sonuca bağlı ücret meslek mensubunun bağımsızlığını zedeler',
            'B': 'Meslek mensubu, iş almak amacıyla asgari ücret tarifesinin altında fiyat teklif edebilir',
            'C': 'Ücret, işin kapsamı ve gerektirdiği emek gözetilerek belirlenir',
            'D': 'Asgari ücret tarifesinin altında iş kabul edilemez',
            'E': 'Ücret uyuşmazlığı meslek mensubuna belge alıkoyma hakkı vermez',
        },
        'B',
        '3568 md. 46: meslek mensupları tarifede yazılı asgari ücretin ALTINDA iş kabul edemezler; aksi davranış md. 48 uyarınca disiplin cezası gerektirir. Sonuca bağlı ücret kişisel çıkar tehdidi doğurur; ücret alacağı ise iş sahibine ait defter ve belgeler üzerinde alıkoyma hakkı vermez.',
    ),
    # düzey 3
    '0025': patch(
        'Bir meslek mensubu, iş sahibinin talebi üzerine gerçeğe aykırı bir kayıt yapmış ve bu kayda dayanan beyannameyi imzalamıştır. Fiil nedeniyle vergi ziyaı doğmuştur. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu sorumluluğunu sözleşmeyle iş sahibine devredebilir',
            'B': 'Yalnızca disiplin sorumluluğu doğar; mali sorumluluk iş sahibine aittir',
            'C': 'İş sahibinin yazılı talebi bulunduğu için meslek mensubunun sorumluluğu doğmaz',
            'D': 'Meslek mensubunun mali sorumluluğu, imzaladığı beyanname için aldığı ücret tutarıyla sınırlı kalır',
            'E': 'Fiil disiplin, mali ve cezai sorumluluğu birlikte doğurabilir; iş sahibinin talebi sorumluluğu kaldırmaz',
        },
        'E',
        'VUK mükerrer md. 227 meslek mensubunu imzaladığı beyannamedeki bilgilerin defter kayıtlarına ve belgelere uygunluğundan sorumlu tutar; 3568 md. 48 disiplin, genel hükümler ise cezai sorumluluk doğurur. İş sahibinin talebi ya da yazılı talimatı sorumluluğu KALDIRMAZ ve sorumluluk sözleşmeyle devredilemez.',
    ),
    # düzey 2
    '0026': patch(
        'Meslek mensubunun kamu yararını gözetme yükümlülüğü tartışılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu, iş sahibinin çıkarını gözetmekle birlikte kamu yararını da gözetmekle yükümlüdür',
            'B': 'Kamu yararı ile iş sahibinin çıkarı çatıştığında meslek mensubu iş sahibinin çıkarını tercih eder',
            'C': 'Kamu yararı gözetimi yalnızca yeminli mali müşavirler için öngörülmüştür',
            'D': 'Kamu yararı gözetimi yalnızca kamu kurumlarına verilen hizmetlerde aranır',
            'E': 'Meslek mensubu yalnızca iş sahibinin çıkarını gözetir',
        },
        'A',
        '3568 md. 1: mesleğin amacı, faaliyet sonuçlarının gerçek durumunu ilgililerin ve RESMÎ MERCİLERİN istifadesine tarafsız biçimde sunmaktır. Meslek mensubu iş sahibinin temsilcisi değil, kamu yararını da gözeten bir meslek mensubudur; çatışma hâlinde mevzuat ve mesleki ilkeler esas alınır.',
    ),
    # düzey 2
    '0027': patch(
        'Bir meslek mensubu, mesleki bilgi ve becerisini güncellemeyi ihmal etmiş; mevzuat değişikliğini bilmediği için hatalı bir beyanname düzenlemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ruhsat alındıktan sonra mesleki bilgiyi güncelleme yükümlülüğü sona erer',
            'B': 'Mesleki bilgi ve beceriyi güncel tutma yükümlülüğü yalnızca yeminli mali müşavirler için öngörülmüş olup serbest muhasebeci mali müşavirleri bağlamaz',
            'C': 'Mevzuatı bilmemek sorumluluğu ortadan kaldıran bir mazerettir',
            'D': 'Hatalı beyanname yalnızca iş sahibinin sorumluluğunu doğurur',
            'E': 'Meslek mensubu, mesleki yeterliğini sürekli olarak güncel tutmakla yükümlüdür; ihmal disiplin sorumluluğu doğurabilir',
        },
        'E',
        'Meslek Ahlak Kuralları (mesleki yeterlik ve özen): meslek mensubu, yeterli düzeyde hizmet verebilmek için bilgi ve becerisini SÜREKLİ güncel tutmakla yükümlüdür. Mevzuatı bilmemek mazeret değildir; VUK mükerrer md. 227 uyarınca imzalanan beyannameden doğan sorumluluk meslek mensubuna aittir.',
    ),
    # düzey 2
    '0028': patch(
        'Bir meslek mensubunun yanında çalışan bir personel, müşteriye ait bilgileri dışarıya sızdırmıştır. Meslek mensubu, fiilin kendisine ait olmadığını ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yükümlülük yalnızca yazılı gizlilik sözleşmesi imzalanmışsa doğar',
            'B': 'Yükümlülük yalnızca meslek mensubunu bağlar; personelin fiili sonuç doğurmaz',
            'C': 'Yanında çalışan personelin fiili yalnızca iş hukuku bakımından sonuç doğurur; meslek mensubu bakımından herhangi bir mesleki sonuç doğurmaz',
            'D': 'Gizlilik yükümlülüğü meslek mensubunun yanında çalışanları da kapsar; meslek mensubu gerekli önlemleri almakla yükümlüdür',
            'E': 'Meslek mensubu ancak fiile bizzat katılmışsa sorumlu tutulabilir',
        },
        'D',
        '3568 md. 43: meslek mensupları VE YANLARINDA ÇALIŞANLAR, işleri dolayısıyla öğrendikleri bilgi ve sırları ifşa edemezler. Meslek mensubu, büro düzeni içinde gizliliği sağlayacak önlemleri almakla yükümlüdür; yazılı sözleşme koşulu aranmaz ve fiile bizzat katılmamak yükümlülüğü ortadan kaldırmaz.',
    ),
    # düzey 2
    '0029': patch(
        'Mesleki etik bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu, mesleki yargısını başkalarının uygunsuz etkisi altında bırakmamalıdır',
            'B': 'Meslek mensubu, mesleki yeterliği bulunmayan işi kabul etmemelidir',
            'C': 'Meslek mensubu, bağımsızlığını koruyamayacağı bir işi de kabul etmekle yükümlüdür',
            'D': 'Meslek mensubu, yanıltıcı bilgi içeren raporlarla ilişkilendirilmemelidir',
            'E': 'Meslek mensubu, gizlilik yükümlülüğünü iş ilişkisi bittikten sonra da sürdürür',
        },
        'C',
        'Meslek Ahlak Kuralları: meslek mensubu bağımsızlığını ve tarafsızlığını koruyamayacağı işi KABUL ETMEMEKLE yükümlüdür; kabul zorunluluğu yoktur. Diğer seçenekler mesleki yeterlik, gizlilik, tarafsızlık ve dürüstlük ilkelerinin doğru ifadeleridir.',
    ),
    # düzey 2
    '0030': patch(
        'Bağımsızlık ve tarafsızlık bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Önemsiz sayılamayacak hediyeler kişisel çıkar tehdidi doğurur',
            'B': 'Tasdik hizmeti verilen şirkete ortak olmak, durum iş sahibine bildirilirse bağımsızlığı etkilemez',
            'C': 'Sonuca bağlı ücret kişisel çıkar tehdidi doğurur',
            'D': 'Önlemler tehdidi kabul edilebilir düzeye indirmiyorsa iş bırakılır',
            'E': 'Hizmet verilen işletmenin yönetiminde görev almak meslek mensubunun bağımsızlığını doğrudan zedeler',
        },
        'B',
        'Meslek Ahlak Kuralları: tasdik hizmeti verilen işletmeye ORTAK olmak ya da yönetiminde görev almak bağımsızlığı doğrudan ortadan kaldırır; iş sahibine BİLDİRİM bu sakatlığı GİDERMEZ. Bildirim tek başına bir önlem değildir; tehdit kabul edilebilir düzeye inmiyorsa iş kabul edilmez ya da bırakılır.',
    ),
    # düzey 2
    '0031': patch(
        'Gizlilik ilkesi bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yükümlülük meslek mensubunun yanında çalışanları da kapsar',
            'B': 'Yükümlülük iş ilişkisi sona erdikten sonra da devam eder',
            'C': 'Meslek mensubunun tanıklık yapması sırrın ifşası sayılmaz',
            'D': 'Meslek mensubu, öğrendiği bilgileri kendi yararına kullanabilir; yasak yalnızca üçüncü kişilere ifşayı kapsar',
            'E': 'Adli veya idari her türlü inceleme ve soruşturma, gizlilik yükümlülüğünün kapsamı dışında bırakılmıştır',
        },
        'D',
        '3568 md. 43: meslek mensupları ve yanlarında çalışanlar, öğrendikleri bilgi ve sırları ifşa edemez VE KENDİ YARARLARINA KULLANAMAZLAR. Yasak her iki yönü kapsar. Adli ve idari inceleme/soruşturmalar hükmün kapsamı dışındadır ve tanıklık ifşa sayılmaz.',
    ),
    # düzey 2
    '0032': patch(
        'Reklam ve iş elde etme bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yasak, açık ve kapalı her türlü reklamı kapsar',
            'B': 'Meslek mensubu, iş elde etmek amacıyla dolaylı yollarla reklam yapabilir',
            'C': 'Tabela ve kartvizit gibi tanıtım araçları belirlenen ölçüler içinde kullanılabilir',
            'D': 'İş elde etmeye yönelik reklam sayılabilecek faaliyetler yasaktır',
            'E': 'Reklam yasağının ihlali disiplin sorumluluğu doğurur',
        },
        'B',
        '3568 md. 44: meslek mensupları iş elde etmek için AÇIK VEYA KAPALI, DOLAYLI YA DA DOLAYSIZ reklam sayılabilecek faaliyetlerde bulunamazlar. Yasak dolaylı yolları da kapsar; tabela ve kartvizit gibi araçlar ise yönetmelikte belirlenen ölçüler içinde reklam sayılmaz.',
    ),
    # düzey 2
    '0033': patch(
        'Meslek mensubunun iş sahibiyle ilişkisi bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İş sahibinin verdiği yazılı talimat, meslek mensubunun kanuni sorumluluğunu ortadan kaldırmaz',
            'B': 'Hukuka aykırı talep reddedilir; ısrar hâlinde iş bırakılabilir',
            'C': 'Meslek mensubu mevzuatla ve mesleki ilkelerle bağlıdır',
            'D': 'İlişki kural olarak vekâlet sözleşmesidir',
            'E': 'Meslek mensubu, iş sahibinin yazılı talimatına dayanarak gerçeğe aykırı kayıt yapabilir',
        },
        'E',
        'Meslek mensubu iş sahibinin talimatıyla değil MEVZUAT ve mesleki ilkelerle bağlıdır. Gerçeğe aykırı kayıt yapmak dürüstlük ilkesini ihlal eder; yazılı talimat sorumluluğu KALDIRMAZ ve ayrıca VUK ile TCK sorumluluğu doğurur. İlişki TBK md. 502 vd. uyarınca vekâlet sözleşmesidir.',
    ),
    # düzey 2
    '0034': patch(
        'Mesleki etik ilkeleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Dürüstlük, meslek mensubunun tüm mesleki ve iş ilişkilerinde doğru olmasını gerektirir. II. Tarafsızlık, mesleki yargının uygunsuz etkilerden korunmasını gerektirir. III. Gizlilik yükümlülüğü iş ilişkisinin sona ermesiyle birlikte kalkar.',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'II ve III',
            'D': 'I ve III',
            'E': 'Yalnız I',
        },
        'A',
        'I ve II temel ilkelerin doğru ifadeleridir. III YANLIŞTIR: 3568 md. 43 ve Meslek Ahlak Kuralları uyarınca gizlilik yükümlülüğü iş ilişkisi SONA ERDİKTEN SONRA DA devam eder.',
    ),
    # düzey 3
    '0035': patch(
        'Bağımsızlık tehditleri ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Kişisel çıkar tehdidi, meslek mensubunun mali menfaatinden doğabilir. II. Kendi kendini denetleme tehdidi, meslek mensubunun daha önce yaptığı işi değerlendirmesinden doğar. III. Tehdit belirlendiğinde iş her hâlükârda reddedilir. IV. Yakınlık tehdidi yalnızca meslek mensubu pay sahibiyse doğar.',
        {
            'A': 'I ve II',
            'B': 'I, III ve IV',
            'C': 'III ve IV',
            'D': 'II ve III',
            'E': 'Yalnız III',
        },
        'C',
        'III YANLIŞ: kavramsal çerçeve yaklaşımı uyarınca tehdit belirlenir, önemliliği değerlendirilir ve önlem alınır; her tehdit otomatik red doğurmaz. IV YANLIŞ: yakınlık tehdidi uzun süreli ya da yakın ilişkilerden doğar, pay sahipliği koşulu aranmaz. I ve II doğrudur.',
    ),
    # düzey 3
    '0036': patch(
        'Meslek mensubunun yükümlülükleri ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Meslek mensubu, mesleki yeterliği bulunmayan işi kabul etmemelidir. II. Meslek mensubu, asgari ücret tarifesinin altında iş kabul edemez. III. Meslek mensubu, iş elde etmek amacıyla reklam yapamaz. IV. Meslek mensubu, ücret alacağı için iş sahibinin defterlerini alıkoyabilir.',
        {
            'A': 'I ve II',
            'B': 'I, II, III ve IV',
            'C': 'II ve IV',
            'D': 'I, II ve III',
            'E': 'Yalnız I',
        },
        'D',
        "I mesleki yeterlik ilkesinin, II 3568 md. 46'nın, III md. 44'ün gereğidir. IV YANLIŞTIR: iş sahibine ait defter ve belgeler talep hâlinde tutanakla geri verilir; ücret alacağı bunlar üzerinde alıkoyma (hapis) hakkı vermez.",
    ),
    # düzey 2
    '0037': patch(
        'Etik ihlallerinin sonuçları ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Etik kural ihlali disiplin sorumluluğu doğurabilir. II. Aynı fiil ayrıca mali ve cezai sorumluluk doğurabilir. III. Disiplin süreci ceza yargılamasının sonucunu beklemek durumunda değildir.',
        {
            'A': 'I, II ve III',
            'B': 'II ve III',
            'C': 'I ve III',
            'D': 'Yalnız I',
            'E': 'I ve II',
        },
        'A',
        'Üç ifade de doğrudur. 3568 md. 48 disiplin sorumluluğunu düzenler; VUK mükerrer md. 227 ve genel hükümler mali ve cezai sorumluluk doğurur. Disiplin, mali ve cezai sorumluluk AYRI REJİMLERDİR ve biri diğerinin sonucunu beklemez.',
    ),
    # düzey 2
    '0038': patch(
        'Mesleki değerler bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu çıkar çatışması bulunan işlerde önlem alır',
            'B': 'Meslek mensubu mesleki yargısını önyargıdan uzak tutar',
            'C': 'Meslek mensubu, mesleki yargısını iş sahibinin ticari beklentilerine uyarlamakla yükümlüdür',
            'D': 'Meslek mensubu kamu yararını da gözetir',
            'E': 'Meslek mensubu, mesleğin itibarını zedeleyebilecek her türlü söz ve davranıştan kaçınır',
        },
        'C',
        'TARAFSIZLIK ilkesi, mesleki yargının önyargı, çıkar çatışması ve başkalarının uygunsuz etkisi altında bırakılmamasını gerektirir. Yargıyı iş sahibinin ticari beklentilerine uyarlamak bu ilkenin doğrudan ihlalidir.',
    ),
    # düzey 2
    '0039': patch(
        'Çıkar çatışması bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ayrı ekipler ve bilgi bariyerleri önlem olarak kullanılabilir',
            'B': 'Önlemler yeterli olmuyorsa işlerden biri bırakılır',
            'C': 'Çıkar çatışması yalnızca müşterilerden biri şikâyette bulunursa sonuç doğurur',
            'D': 'Çıkar çatışması belirlendiğinde ilgili tarafların bilgilendirilmesi gerekir',
            'E': 'Çıkar çatışması tarafsızlığı tehdit eder',
        },
        'C',
        'Meslek Ahlak Kuralları: çıkar çatışması meslek mensubunun kendi değerlendirmesiyle belirlenir; müşterinin ŞİKÂYETİ koşul değildir. Çatışma belirlendiğinde bilgilendirme yapılır, önlemler alınır ve yeterli olmuyorsa iş bırakılır.',
    ),
    # düzey 2
    '0040': patch(
        'Müşteri kabulü ve iş devri bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bildirim yükümlülüğü haksız rekabeti önlemeye yöneliktir',
            'B': 'İş sahibinin dürüstlüğüne ilişkin ciddi kuşkular tehdit oluşturur',
            'C': 'Meslek mensubu iş sahibini ve işi kabul öncesinde değerlendirir',
            'D': 'İşi devralacak meslek mensubu, kabul öncesinde önceki meslektaşa yazılı bildirimde bulunur',
            'E': 'İşi devralacak meslek mensubunun önceki meslektaşa bildirim yapması gerekmez',
        },
        'E',
        'Meslek Ahlak Kuralları ve 3568 md. 47: bir meslektaşın işini devralmak isteyen meslek mensubu, işi kabul etmeden önce önceki meslek mensubuna YAZILI BİLDİRİMDE bulunur ve ücret alacağı durumunu araştırır. Bu yükümlülük haksız rekabeti önlemeye yöneliktir.',
    ),
    # düzey 1
    '0041': patch(
        'Bir meslek mensubu, bulgularını hiçbir tarafın etkisi altında kalmadan raporlamıştır. Buna göre uygulanan ilke aşağıdakilerden hangisidir?',
        {
            'A': 'Mesleki dayanışma',
            'B': 'Tarafsızlık',
            'C': 'Ticari basiret',
            'D': 'Gizlilik',
            'E': 'Sürekli mesleki gelişim',
        },
        'B',
        'TARAFSIZLIK (objektiflik) ilkesi, meslek mensubunun mesleki yargısını önyargı, çıkar çatışması ya da başkalarının uygunsuz etkisi altında bırakmamasını gerektirir; bulguların etkiden uzak raporlanması bu ilkenin uygulanmasıdır.',
    ),
    # düzey 1
    '0042': patch(
        'Bir meslek mensubu, işini gerekli bilgi, beceri ve özenle yürütmek için mesleki gelişimini sürdürmektedir. Buna göre uygulanan ilke aşağıdakilerden hangisidir?',
        {
            'A': 'Mesleki yeterlik ve gereken özeni gösterme ilkesi',
            'B': 'Dürüstlük',
            'C': 'Gizlilik',
            'D': 'Tarafsızlık',
            'E': 'Mesleğe uygun davranış ilkesi',
        },
        'A',
        'MESLEKİ YETERLİK VE GEREKEN ÖZENİ GÖSTERME ilkesi, meslek mensubunun mesleki bilgi ve becerisini yeterli düzeyde tutmasını ve işi geçerli standartlara uygun biçimde özenle yürütmesini gerektirir; sürekli mesleki gelişim bu ilkenin gereğidir.',
    ),
    # düzey 0
    '0043': patch(
        'Meslek Ahlak Kurallarının temel ilkelerinden biri, meslek mensubunun işleri dolayısıyla öğrendiği bilgileri korumasını gerektirir. Buna göre bu ilke aşağıdakilerden hangisidir?',
        {
            'A': 'Tarafsızlık',
            'B': 'Mesleğe uygun davranış ilkesi',
            'C': 'Mesleki yeterlik',
            'D': 'Dürüstlük',
            'E': 'Gizlilik',
        },
        'E',
        'GİZLİLİK ilkesi, meslek mensubunun mesleki ve iş ilişkileri sonucunda edindiği bilgilerin gizliliğine saygı göstermesini, bu bilgileri yetkisiz kişilere açıklamamasını ve kendi ya da üçüncü kişilerin çıkarı için kullanmamasını gerektirir (3568 md. 43).',
    ),
    # düzey 0
    '0044': patch(
        'Bağımsızlığa yönelik tehditlerden biri, meslek mensubunun daha önce kendisinin yaptığı bir işi sonradan değerlendirmesinden doğar. Buna göre bu tehdit aşağıdakilerden hangisidir?',
        {
            'A': 'Yakınlık',
            'B': 'Yıldırma',
            'C': 'Kendi kendini denetleme tehdidi',
            'D': 'Taraf tutma',
            'E': 'Kişisel çıkar tehdidi',
        },
        'C',
        'KENDİ KENDİNİ DENETLEME (self-review) tehdidi, meslek mensubunun daha önce verdiği bir hizmetin ya da yaptığı bir işlemin sonucunu sonradan değerlendirmek durumunda kalmasından doğar; kendi işini objektif biçimde denetleyememe riski taşır.',
    ),
    # düzey 0
    '0045': patch(
        'Bağımsızlığa yönelik tehditlerden biri, meslek mensubunun iş sahibinin görüşünü savunma konumuna geçmesinden doğar. Buna göre bu tehdit aşağıdakilerden hangisidir?',
        {
            'A': 'Kişisel çıkar tehdidi',
            'B': 'Taraf tutma',
            'C': 'Kendi kendini denetleme tehdidi',
            'D': 'Yakınlık',
            'E': 'Yıldırma',
        },
        'B',
        'TARAF TUTMA (advocacy) tehdidi, meslek mensubunun iş sahibinin konumunu ya da görüşünü, objektifliğini zedeleyecek ölçüde savunması hâlinde doğar; örneğin müşteri adına bir uyuşmazlıkta taraf gibi hareket etmek.',
    ),
    # düzey 0
    '0046': patch(
        'Bağımsızlığa yönelik tehditlerden biri, meslek mensubunun baskı veya tehdit altında bırakılması hâlinde doğar. Buna göre bu tehdit aşağıdakilerden hangisidir?',
        {
            'A': 'Kişisel çıkar tehdidi',
            'B': 'Yıldırma',
            'C': 'Taraf tutma',
            'D': 'Yakınlık',
            'E': 'Kendi kendini denetleme tehdidi',
        },
        'B',
        'YILDIRMA (intimidation) tehdidi, meslek mensubunun gerçek ya da algılanan baskı altında objektif davranmasının engellenmesi hâlinde doğar; sözleşmenin sona erdirilmesi ya da şikâyet tehdidi tipik örneklerdir.',
    ),
    # düzey 2
    '0047': patch(
        'Bir meslek mensubu, bağımsızlığına yönelik bir tehdide karşı önlem aramaktadır. Buna göre aşağıdakilerden hangisi bir önlem sayılmaz?',
        {
            'A': 'Mesleki eğitim ve sürekli gelişim yükümlülüklerini uygulamak',
            'B': 'Gerektiğinde işi kabul etmemek ya da bırakmak',
            'C': 'İşi ikinci bir meslek mensubunun gözden geçirmesini sağlamak',
            'D': 'Etkilenen işten ayrı bir ekip görevlendirmek',
            'E': 'Tehdidin varlığını yalnızca kendi kayıtlarına not etmek',
        },
        'E',
        'Önlemler; mesleki düzenlemelerden kaynaklananlar (eğitim, ruhsat, disiplin sistemi) ile iş ortamındakiler (gözden geçirme, ayrı ekip, bilgi bariyeri) olarak sınıflandırılır ve gerekirse işten çekilmeye kadar gider. Tehdidi yalnızca KAYDA GEÇİRMEK, tehdidi kabul edilebilir düzeye indirmediği için önlem sayılmaz.',
    ),
    # düzey 2
    '0048': patch(
        'Bir meslek mensubu, tasdik hizmeti verdiği işletmeye aynı dönemde muhasebe kaydı hizmeti de vermeyi planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Durum iş sahibine bildirilirse tehdit ortadan kalkar',
            'B': 'Tehdit yalnızca meslek mensubu işletmeye ortak da olursa doğar',
            'C': 'Aynı işletmeye hem kayıt hem tasdik hizmeti vermek kendi kendini denetleme tehdidi doğurur',
            'D': 'İki hizmetin birlikte verilmesi bağımsızlık bakımından sorun doğurmaz',
            'E': 'Bağımsızlık sorunu yalnızca iki hizmetin ücretinin aynı faturada gösterilmesinden doğar',
        },
        'C',
        "Meslek mensubunun kendi tuttuğu kayıtları sonradan tasdik etmesi, kendi işini denetlemesi anlamına gelir ve KENDİ KENDİNİ DENETLEME tehdidi doğurur. Ayrıca 3568 md. 45 uyarınca YMM'ler defter tutamaz; tasdik ve kayıt işleri unvan bakımından da ayrıdır. Bildirim ya da faturalandırma biçimi bu sakatlığı gidermez.",
    ),
    # düzey 3
    '0049': patch(
        'Bir meslek mensubu; iş sahibinin gerçeğe aykırı beyan talebini reddetmiş, iş sahibi de sözleşmeyi sona erdirmiştir. İş sahibi daha sonra aynı işi başka bir meslek mensubuna götürmüştür. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İlk meslek mensubu, reddettiği talebi odaya bildirmekten men edilmiştir',
            'B': 'İlk meslek mensubu işi kaybettiği için hatalı davranmıştır',
            'C': 'İkinci meslek mensubu, iş sahibinin talebini yerine getirmekle yükümlüdür',
            'D': 'İlk meslek mensubu doğru davranmıştır; ikinci meslek mensubunun da işi kabul öncesi değerlendirme yapması gerekir',
            'E': 'İkinci meslek mensubu, işi devraldığı için müşteri kabulüne ve önceki meslektaşa bildirime ilişkin hiçbir yükümlülük altında değildir',
        },
        'D',
        'Dürüstlük ve tarafsızlık ilkeleri gereği hukuka aykırı talep reddedilir; iş kaybı bu davranışı hatalı kılmaz. İkinci meslek mensubu ise MÜŞTERİ KABULÜ değerlendirmesi yapmalı, iş sahibinin dürüstlüğüne ilişkin kuşkuyu ve devir kurallarını (önceki meslektaşa bildirim) gözetmelidir.',
    ),
    # düzey 2
    '0050': patch(
        'Meslek mensubunun sorumluluğu bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu, mesleki sorumluluk sigortası yaptırdığında kanuni sorumluluğundan kurtulur',
            'B': 'Meslek mensubu, imzaladığı beyannamedeki bilgilerin defter kayıtlarına uygunluğundan sorumludur',
            'C': 'Etik ihlali disiplin sorumluluğu doğurabilir',
            'D': 'Aynı fiil mali ve cezai sorumluluk da doğurabilir',
            'E': 'Sorumluluk sözleşmeyle iş sahibine devredilemez',
        },
        'A',
        "Mesleki sorumluluk sigortası, doğan ZARARIN karşılanmasına yöneliktir; meslek mensubunun VUK mükerrer md. 227 ve 3568'den doğan KANUNİ sorumluluğunu ORTADAN KALDIRMAZ ve disiplin ile cezai sorumluluğu hiç etkilemez.",
    ),
    # düzey 2
    '0051': patch(
        'Meslek mensuplarının birbirleriyle ilişkileri bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu meslektaşlarına karşı dürüstlük ilkesiyle bağlıdır',
            'B': 'Meslek örgütü, meslek mensupları arasındaki mesleki uyuşmazlıklarda arabuluculuk yapabilir',
            'C': 'Meslek mensubu, iş almak amacıyla meslektaşının yeterliği hakkında olumsuz beyanda bulunabilir',
            'D': 'Meslektaşın işini devralmak isteyen meslek mensubu ona bildirimde bulunur',
            'E': 'Meslek mensupları arasında haksız rekabet yasaktır',
        },
        'C',
        '3568 md. 47 meslek mensupları arasında haksız rekabeti YASAKLAR; meslektaşı küçük düşüren ya da yeterliğini kötüleyen beyanlarla iş almaya çalışmak haksız rekabet sayılır ve md. 48 uyarınca disiplin cezası gerektirir.',
    ),
    # düzey 2
    '0052': patch(
        'Bir meslek mensubu, mesleki faaliyeti sırasında elde ettiği belgeleri iş ilişkisi sona erdikten sonra iş sahibine vermeyi reddetmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu ücreti ödenene kadar belgeleri alıkoyabilir',
            'B': 'Belgeleri geri verme yükümlülüğü yalnızca yeminli mali müşavirler için öngörülmüştür',
            'C': 'Belgeler yalnızca vergi dairesinin talebi üzerine geri verilir',
            'D': 'Meslek mensubu belgeleri geri vermek yerine imha edebilir',
            'E': 'Belgeler talep hâlinde tutanakla geri verilir; ücret alacağı alıkoyma hakkı vermez',
        },
        'E',
        'Meslek mevzuatı: iş sahibine ait defter ve belgeler özenle saklanır ve iş ilişkisi sona erdiğinde TUTANAKLA geri verilir. Ücret alacağı, yasal saklama yükümlülüğü bulunan bu belgeler üzerinde alıkoyma (hapis) hakkı vermez; alacak genel hükümlere göre takip edilir.',
    ),
    # düzey 2
    '0053': patch(
        'Mesleğe uygun davranış ilkesi bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu ilgili mevzuata uymalı ve mesleğin itibarını zedeleyecek davranışlardan kaçınmalıdır',
            'B': 'Mesleğe uygun davranış ilkesinin ihlali yalnızca iş sahibinin yazılı şikâyeti hâlinde sonuç doğurur',
            'C': 'İlke yalnızca mesleki faaliyet saatlerindeki davranışları kapsar',
            'D': 'İlke yalnızca yeminli mali müşavirleri bağlar',
            'E': 'İlke, mevzuata uygunluk yükümlülüğünü kapsamaz',
        },
        'A',
        "MESLEĞE UYGUN DAVRANIŞ ilkesi, meslek mensubunun ilgili mevzuata uymasını ve mesleğin itibarını zedeleyebilecek davranışlardan kaçınmasını gerektirir (3568 md. 45'teki 'mesleğin gereği ve onuruyla bağdaşmayan işler' yasağıyla bağlantılı). İlke tüm meslek mensuplarını bağlar ve şikâyet koşuluna bağlı değildir.",
    ),
    # düzey 3
    '0054': patch(
        'Bir meslek mensubu, uzun yıllar hizmet verdiği bir müşterisinin mali tablolarını her yıl aynı ekiple ve aynı yöntemle değerlendirmektedir. Müşteriyle kişisel yakınlık da gelişmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yakınlık tehdidi yalnızca meslek mensubunun müşteriden değerli bir hediye kabul etmesi hâlinde doğar',
            'B': 'Uzun süreli ilişki yakınlık tehdidi doğurur; ekip rotasyonu ve gözden geçirme gibi önlemler alınmalıdır',
            'C': 'Yakınlık tehdidi yalnızca akrabalık ilişkisi varsa doğar',
            'D': 'İlişkinin süresi bağımsızlık değerlendirmesinde dikkate alınmaz',
            'E': 'Uzun süreli ilişki güven oluşturduğu için bağımsızlığı güçlendirir',
        },
        'B',
        'YAKINLIK tehdidi, uzun süreli ya da yakın ilişkilerden doğar ve meslek mensubunun müşterinin çıkarlarına aşırı duyarlı hâle gelmesi riskini taşır. Akrabalık ya da hediye koşulu aranmaz. Önlemler ekip rotasyonu, bağımsız gözden geçirme ve gerekirse işin bırakılmasıdır.',
    ),
    # düzey 2
    '0055': patch(
        'Mesleki etik ve bağımsızlık bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Önlemler tehdidi kabul edilebilir düzeye indirmiyorsa iş bırakılır',
            'B': 'Bağımsızlığa yönelik tehditler belirlenir ve önemliliği değerlendirilir',
            'C': 'Hizmet verilen işletmenin yönetiminde görev alınamaz',
            'D': 'Bağımsızlık yalnızca danışmanlık işlerinde aranan bir ölçüttür',
            'E': 'Bağımsızlık, denetim ve tasdik gibi güvence işlerinde kurucu koşuldur',
        },
        'D',
        'Bağımsızlık, özellikle DENETİM ve TASDİK gibi üçüncü kişilere güvence veren işlerde kurucu koşuldur; danışmanlıkla sınırlı değildir. Kavramsal çerçeve uyarınca tehdit belirlenir, değerlendirilir ve önlem alınır; yetersizse iş bırakılır.',
    ),
    # düzey 2
    '0056': patch(
        'Bir meslek mensubu, kendisine teklif edilen bir işi bağımsızlığını koruyamayacağı gerekçesiyle reddetmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu kendisine teklif edilen işi reddedemez',
            'B': 'Red mesleki bir yükümlülüğün yerine getirilmesidir; haksız rekabet oluşturmaz',
            'C': 'İşin reddi, meslek mensubu hakkında disiplin soruşturması açılmasını gerektirir',
            'D': 'Red serbesttir ancak gerekçenin iş sahibine açıklanması yasaktır',
            'E': 'Red ancak odanın yazılı izniyle mümkündür',
        },
        'B',
        'Meslek Ahlak Kuralları: meslek mensubu bağımsızlığını ve tarafsızlığını koruyamayacağı ya da mesleki yeterliğinin yetmediği işleri KABUL ETMEMEKLE yükümlüdür. Red bir yükümlülüğün yerine getirilmesi olup oda iznine bağlı değildir, haksız rekabet oluşturmaz ve disiplin soruşturması gerektirmez.',
    ),
    # düzey 2
    '0057': patch(
        'Bir meslek mensubu, mesleki faaliyeti dolayısıyla öğrendiği bir bilgiyi, kanunla yetkili kılınmış bir idari inceleme kapsamında istenmesi üzerine idareye vermiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Gizlilik yükümlülüğü mutlak olup hiçbir istisna tanımaz',
            'B': 'Meslek mensubu bilgiyi vermeyerek gizliliği korumakla yükümlüydü',
            'C': 'İdareye bilgi verme yükümlülüğü yalnızca yeminli mali müşavirler için öngörülmüştür',
            'D': 'Bilgi ancak iş sahibinin yazılı onayıyla verilebilirdi',
            'E': 'Adli ve idari inceleme ve soruşturmalar gizlilik yükümlülüğünün kapsamı dışındadır',
        },
        'E',
        '3568 md. 43: meslek mensupları işleri dolayısıyla öğrendikleri bilgi ve sırları ifşa edemezler; ancak ADLİ VEYA İDARİ HER TÜRLÜ İNCELEME VEYA SORUŞTURMA bu hükmün kapsamı DIŞINDADIR. Kanunla yetkili kılınmış merciin talebi karşısında bilgi verilmesi gizlilik ihlali sayılmaz ve iş sahibinin onayı aranmaz.',
    ),
    # düzey 1
    '0058': patch(
        'Bir meslek mensubu, mesleki faaliyetinde kendisine ibraz edilen belgelere dayanarak kayıt yapmıştır. Belgelerin sonradan gerçeği yansıtmadığı anlaşılmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Meslek mensubu kayıtların belgelere uygunluğundan sorumludur; belgelerin gerçekliğini araştırma yükümlülüğü bulunmaz',
            'B': 'Sorumluluk yalnızca yeminli mali müşavirler için doğar',
            'C': 'Sorumluluk sözleşmeyle tümüyle kaldırılabilir',
            'D': 'Meslek mensubunun hiçbir sorumluluğu doğmaz',
            'E': 'Meslek mensubu, kayıtların belgelere uygunluğunun yanında kendisine ibraz edilen belgelerin maddi gerçeğe uygunluğundan da ayrıca sorumludur',
        },
        'A',
        'VUK mükerrer md. 227: meslek mensubu, imzaladığı beyannamelerde yer alan bilgilerin DEFTER KAYITLARINA ve bu kayıtların dayanağını oluşturan BELGELERE uygunluğundan sorumludur; belgelerin muhteviyatının maddi gerçeğe uygun olup olmadığını araştırma yükümlülüğü yoktur. Sorumluluk kanuni olup sözleşmeyle kaldırılamaz.',
    ),
    # düzey 2
    '0059': patch(
        'Meslek mensubunun kamu yararı ve iş sahibi çıkarı arasındaki konumu bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Meslek mensubu mesleki ilkelerle ve mevzuatla bağlıdır',
            'B': 'Hukuka aykırı talep iş sahibinden gelse de reddedilir',
            'C': 'Kamu yararı ile iş sahibinin çıkarı çatıştığında meslek mensubu iş sahibinin çıkarını tercih eder',
            'D': 'Meslek mensubu iş sahibinin temsilcisi değildir',
            'E': 'Faaliyet sonuçları, ilgililerin ve resmî mercilerin istifadesine tarafsız biçimde sunulmakla yükümlüdür',
        },
        'C',
        '3568 md. 1: mesleğin amacı faaliyet sonuçlarını ilgililerin VE RESMÎ MERCİLERİN istifadesine TARAFSIZ biçimde sunmaktır. Meslek mensubu iş sahibinin temsilcisi değildir; çatışma hâlinde mevzuat ve mesleki ilkeler esas alınır, iş sahibinin çıkarı öne geçmez.',
    ),
    # düzey 3
    '0060': patch(
        'Mesleki değerler ve etik ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Temel ilkeler dürüstlük, tarafsızlık, mesleki yeterlik ve özen, gizlilik ve mesleğe uygun davranıştır. II. Sonuca bağlı ücret, tasdik işlerinde bağımsızlığı zedeler. III. Gizlilik yükümlülüğü hiçbir istisna tanımaz. IV. Bağımsızlık tehdidi belirlendiğinde iş her hâlükârda reddedilir.',
        {
            'A': 'Yalnız III',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'I, III ve IV',
            'E': 'III ve IV',
        },
        'E',
        'III YANLIŞ: 3568 md. 43 uyarınca adli ve idari inceleme ve soruşturmalar gizlilik hükmünün kapsamı dışındadır; tanıklık ifşa sayılmaz. IV YANLIŞ: kavramsal çerçeve uyarınca tehdit belirlenir, önemliliği değerlendirilir ve önlem alınır; her tehdit otomatik red doğurmaz. I ve II doğrudur.',
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
    print(f"1 paket / {len(PATCHES)} soru (Mesleki Degerler ve Etik yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
