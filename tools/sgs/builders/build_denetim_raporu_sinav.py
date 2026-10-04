#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Denetim Raporu ve Görüş Türleri — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Denetim turu (gerçek denetim bloğu 73-88 ile ölçüldü; raporlama en sık sorulan alan). Paket baştan yazıldı: BDS 700 (rapor bölümleri ve sırası, Görüşün Dayanağı unsurları, sorumluluk bölümleri, rapor tarihi, mevzuattan kaynaklanan yükümlülükler, görüş oluşturma), BDS 705 (önemli/yaygın matrisi, yaygınlık tanımı, kapsam sınırlaması ve çekilme, kaçınmada KDK ve Diğer Bilgiler bölümünün olmaması, parçalı görüş yasağı, birden fazla belirsizlik), BDS 706 (dikkat çeken husus ve diğer husus), BDS 701 (KDK), BDS 720 (diğer bilgiler), BDS 570 (süreklilik ve rapor), BDS 710 ve BDS 560. Önemlilik karşılaştırmalı olay soruları kesirli aritmetikle.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: BDS 700, 701, 705, 706, 710, 720, 570, 560
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/denetim/denetim_raporu.json"
STYLE_REF = 'SGS Denetim (standarda atıflı/olay kök + kısa şık; gerçek sınav profili)'
ONEK = "den-rapor-gen-"


def patch(stem, options, answer, solution, ref='BDS 700 Finansal Tablolara İlişkin Görüş Oluşturma ve Raporlama; BDS 705; BDS 706; BDS 701; BDS 720; BDS 570'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        "I. Etki, finansal tabloların belirli unsurları veya kalemleriyle sınırlı değildir.\nII. Etki belirli unsurlarla sınırlı olsa da finansal tabloların önemli bir bölümünü temsil eder.\nIII. Etki, kullanıcıların finansal tabloları anlaması açısından temel nitelikteki açıklamalarla ilgilidir.\n\nBDS 705'e göre yukarıdakilerden hangileri yaygın etkiyi tanımlar?",
        {
            'A': 'I ve III',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'Yalnız I',
        },
        'D',
        "BDS 705'e göre yaygın etki; belirli unsurlarla sınırlı olmayan, sınırlı olsa da tabloların önemli bir bölümünü temsil eden ya da açıklamalar bakımından kullanıcıların anlaması için temel nitelikte olan etkidir.",
    ),
    # düzey 2
    '0002': patch(
        "BDS 705'e göre olumsuz görüş içeren bir raporda Görüş bölümündeki ifade aşağıdakilerden hangisidir?",
        {
            'A': 'Tabloların bazı kalemler hariç doğru olduğu',
            'B': 'Yeterli kanıt elde edilemediği',
            'C': 'Tabloların denetlenmediği',
            'D': 'Görüş oluşturulamadığı',
            'E': 'Tabloların gerçeğe uygun sunulmadığı',
        },
        'E',
        'Olumsuz görüşte denetçi, dayanak bölümünde açıklanan hususların önemi nedeniyle finansal tabloların uygulanabilir çerçeveye uygun olarak gerçeğe uygun biçimde sunulmadığını belirtir.',
    ),
    # düzey 2
    '0003': patch(
        'Denetim sözleşmesinde aksi öngörülmediği ve mevzuat ayrıca bir muhatap belirlemediği durumda, bir anonim şirketin yıllık finansal tablolarına ilişkin denetçi raporu genellikle aşağıdakilerden hangisine hitaben düzenlenir?',
        {
            'A': 'Vergi dairesine',
            'B': 'Pay sahiplerine',
            'C': 'Şirketin bankalarına',
            'D': 'Muhasebe müdürüne',
            'E': 'Kamu Gözetimi Kurumuna',
        },
        'B',
        'Denetçi raporu sözleşme şartlarına göre belirlenen muhataba hitaben düzenlenir; bu genellikle denetimi yapılan işletmenin pay sahipleri ya da üst yönetimden sorumlu olanlardır.',
    ),
    # düzey 3
    '0004': patch(
        "Bir şirketin önceki yıl finansal tabloları denetlenmemiştir; cari yıl ilk kez denetlenmektedir.\n\nBDS 710'a göre denetçi bu durumu raporunda nasıl belirtir?",
        {
            'A': 'Rapora açıklama eklemeden',
            'B': 'Dikkat Çeken Husus paragrafında',
            'C': 'Görüş bölümünde sınırlı olumlu görüşle',
            'D': 'Kilit denetim konusu olarak',
            'E': 'Diğer Hususlar paragrafında açıklayarak',
        },
        'E',
        'Önceki dönem tabloları denetlenmemişse denetçi, karşılaştırmalı bilgilerin denetlenmediğini Diğer Hususlar paragrafında belirtir; bu açıklama, açılış bakiyelerine ilişkin yeterli kanıt elde etme sorumluluğunu ortadan kaldırmaz.',
    ),
    # düzey 2
    '0005': patch(
        "BDS 700'e göre denetçi raporunun başlığıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Bağımsız denetçi raporu olduğu açıkça belirtilir',
            'B': 'Başlık kullanılması isteğe bağlıdır',
            'C': 'Başlıkta yönetim kurulunun onayı belirtilir',
            'D': 'Başlıkta işletmenin unvanı yer almaz',
            'E': 'Görüş türü başlıkta belirtilir',
        },
        'A',
        'Denetçi raporunun, bağımsız bir denetçinin raporu olduğunu açıkça gösteren bir başlığı bulunur.',
    ),
    # düzey 3
    '0006': patch(
        "Denetçi, finansal tabloların tamamının hazırlandığına ve yetkililerin tablolara ilişkin sorumluluğu üstlendiğine dair kanıtı 18 Mart 2026'da elde etmiştir. Diğer kanıtların toplanması 11 Mart 2026'da tamamlanmıştır.\n\nBDS 700'e göre denetçi raporuna verilebilecek en erken tarih hangisidir?",
        {
            'A': '1 Mart 2026',
            'B': '31 Aralık 2025',
            'C': '18 Mart 2026',
            'D': '11 Mart 2026',
            'E': '31 Mart 2026',
        },
        'C',
        "Denetçi raporu, görüşe dayanak oluşturacak yeterli ve uygun kanıtın elde edildiği tarihten önceki bir tarihi taşıyamaz. Bu kanıt, tabloların tamamının hazırlandığına ve yetkililerin sorumluluğu üstlendiğine dair kanıtı da kapsar; bu nedenle en erken tarih 18 Mart 2026'dır.",
    ),
    # düzey 2
    '0007': patch(
        "BDS 705'e göre aşağıdakilerden hangisi denetçinin olumlu görüş dışında bir görüş vermesini gerektiren durumlardan biri değildir?",
        {
            'A': 'Önemli bir hesap için yeterli kanıt elde edilememesi',
            'B': 'Yönetimin kapsamı sınırlaması',
            'C': 'Önemli yanlışlık içeren tablolar',
            'D': 'Açıklanmış bir davaya dikkat çekilmesi',
            'E': 'Kayıtların bir kısmının yok olması',
        },
        'D',
        'Görüş, tabloların önemli yanlışlık içermesi ya da yeterli kanıt elde edilememesi durumunda değiştirilir. Tablolarda yeterince açıklanmış bir hususa dikkat çekmek görüşü değiştirmez; BDS 706 kapsamında Dikkat Çeken Husus paragrafıyla yapılır.',
    ),
    # düzey 3
    '0008': patch(
        "Bir denetim kuruluşu, borsada işlem gören bir şirketin bağımsız denetimine ilişkin raporunu hazırlamaktadır.\n\nBDS 700'e göre aşağıdakilerden hangisinin bu raporda yer alması gerekmez?",
        {
            'A': 'Sorumlu denetçinin adı',
            'B': 'Denetim ekibindeki tüm denetçilerin adları',
            'C': 'Rapor tarihi',
            'D': 'Kilit Denetim Konularının açıklandığı ayrı bölüm',
            'E': 'Denetçinin bulunduğu yer',
        },
        'B',
        'Borsada işlem gören işletmelerin raporlarında sorumlu denetçinin adı belirtilir ve BDS 701 uyarınca kilit denetim konuları bildirilir; raporda denetçinin bulunduğu yer ve tarih de yer alır. Ekipteki diğer denetçilerin adlarına yer verilmez.',
    ),
    # düzey 2
    '0009': patch(
        'Bir denetim raporunda yönetimin sorumluluklarını açıklayan bölümde "işletmenin sürekliliğini değerlendirmek" ifadesi yer almaktadır.\n\nBDS 700\'e göre bu sorumluluk kime aittir?',
        {
            'A': 'Kamu Gözetimi Kurumuna',
            'B': 'Yönetime',
            'C': 'Denetçiye',
            'D': 'Sorumlu denetçiye',
            'E': 'Bağımsız denetim kuruluşuna',
        },
        'B',
        'İşletmenin sürekliliğini değerlendirme, gerektiğinde süreklilikle ilgili hususları açıklama ve süreklilik esasını kullanma sorumluluğu yönetime aittir; denetçi yönetimin bu esası kullanmasının uygunluğu hakkında sonuca varır.',
    ),
    # düzey 2
    '0010': patch(
        "BDS 705'e göre sınırlı olumlu görüş içeren bir raporda Görüş bölümünün başlığı aşağıdakilerden hangisidir?",
        {
            'A': 'Dikkat Çeken Husus',
            'B': 'Şartlı Görüşün Dayanağı',
            'C': 'Görüş',
            'D': 'Sınırlı Olumlu Görüş',
            'E': 'Olumlu Görüş Dışında Görüş',
        },
        'D',
        'Görüş bölümünün başlığı verilen görüşe göre "Sınırlı Olumlu Görüş", "Olumsuz Görüş" ya da "Görüş Vermekten Kaçınma" olur; dayanak bölümünün başlığı da buna uygun değiştirilir.',
    ),
    # düzey 2
    '0011': patch(
        "BDS 701'e göre kilit denetim konuları aşağıdakilerden hangisidir?",
        {
            'A': 'Tablolarda açıklanmamış tüm riskler',
            'B': 'Cari dönem denetiminde en çok önem arz eden konular',
            'C': 'Yönetimin denetçi raporunda vurgulanmasını istediği konular',
            'D': 'Önemlilik düzeyini aşan tüm yanlışlıklar',
            'E': 'Görüşü değiştiren konuların tamamı',
        },
        'B',
        'Kilit denetim konuları, denetçinin mesleki muhakemesine göre cari döneme ait finansal tabloların denetiminde en çok önem arz eden ve üst yönetimden sorumlu olanlara bildirilen konular arasından seçilen konulardır.',
    ),
    # düzey 2
    '0012': patch(
        "BDS 720'ye göre denetçinin diğer bilgilere ilişkin sorumluluğu aşağıdakilerden hangisidir?",
        {
            'A': 'Okuyup önemli tutarsızlık olup olmadığını değerlendirmek',
            'B': 'Diğer bilgileri yönetim adına onaylamak',
            'C': 'Diğer bilgileri hazırlamak',
            'D': 'Diğer bilgileri denetleyip ayrıca makul güvence içeren görüş vermek',
            'E': 'Diğer bilgiler hakkında güvence vermek',
        },
        'A',
        'Denetçinin görüşü diğer bilgileri kapsamaz. Denetçi diğer bilgileri okur; tablolar ve denetimde edindiği bilgilerle önemli bir tutarsızlık bulunup bulunmadığını ve diğer bilgilerde önemli yanlışlık olup olmadığını değerlendirir.',
    ),
    # düzey 2
    '0013': patch(
        "BDS 700'e göre denetçi raporunun Denetçinin Sorumlulukları bölümüyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Amacın makul güvence elde etmek olduğu belirtilir',
            'B': 'Önemliliğin nasıl tanımlandığı açıklanır',
            'C': 'Yanlışlıkların hata veya hileden kaynaklanabileceği açıklanır',
            'D': 'Her önemli yanlışlığın tespit edileceği garanti edilir',
            'E': 'Mesleki muhakeme ve şüphecilik kullanıldığı belirtilir',
        },
        'D',
        "Makul güvence yüksek düzeyde bir güvencedir ancak BDS'lere uygun yürütülen bir denetimin var olan her önemli yanlışlığı her zaman tespit edeceğini garanti etmez. Raporda bu açıkça belirtilir.",
    ),
    # düzey 2
    '0014': patch(
        "BDS 706'ya göre dikkat çeken hususlar paragrafı ile ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Kilit denetim konusu olan hususun yerine kullanılmaz',
            'B': 'Kullanıcılar için temel nitelikteki konuyla ilgilidir',
            'C': 'Ayrı bir bölümde uygun başlıkla sunulur',
            'D': 'Tablolarda sunulmuş bir hususa atıf yapar',
            'E': 'Denetçinin görüşünü değiştirir',
        },
        'E',
        'Dikkat Çeken Husus paragrafı tablolarda uygun şekilde sunulmuş ya da açıklanmış ve kullanıcıların anlaması bakımından temel nitelikteki bir hususa dikkat çeker; raporda görüşün bu hususa ilişkin olarak değiştirilmediği belirtilir.',
    ),
    # düzey 2
    '0015': patch(
        "BDS 700'e göre denetçinin görüş oluştururken yapacağı değerlendirmelerden biri aşağıdakilerden hangisi değildir?",
        {
            'A': 'Tablolarda yeterli açıklama yapılıp yapılmadığı',
            'B': 'Muhasebe tahminlerinin makul olup olmadığı',
            'C': 'İşletmenin gelecek yıl kâr edip etmeyeceği',
            'D': 'Seçilen muhasebe politikalarının uygunluğu',
            'E': 'Düzeltilmemiş yanlışlıkların önemli olup olmadığı',
        },
        'C',
        'Denetçi; makul güvence elde edilip edilmediğini, düzeltilmemiş yanlışlıkların önemliliğini, muhasebe politikalarının uygunluğunu, tahminlerin makullüğünü, bilgilerin ihtiyaca uygunluğunu ve açıklamaların yeterliliğini değerlendirir. Gelecekteki kârlılığı tahmin etmek görüş oluşturmanın parçası değildir.',
    ),
    # düzey 3
    '0016': patch(
        "Yönetimin getirdiği kapsam sınırlaması nedeniyle denetçi yeterli kanıt elde edememiş, tespit edilmemiş yanlışlıkların olası etkilerinin önemli ve yaygın olduğu sonucuna varmıştır. Sözleşmeden çekilmesi mevzuat açısından mümkündür.\n\nBDS 705'e göre denetçi ne yapar?",
        {
            'A': 'Olumsuz görüş verir',
            'B': 'Sınırlı olumlu görüş verir',
            'C': 'Dikkat çekilen husus ekleyerek olumlu görüş verir',
            'D': 'Raporu yönetimin onayına sunar',
            'E': 'Sözleşmeden çekilir',
        },
        'E',
        'Olası etkiler önemli ve yaygınsa denetçi, mümkünse sözleşmeden çekilir; çekilmek mümkün değilse görüş vermekten kaçınır.',
    ),
    # düzey 3
    '0017': patch(
        "Begonya A.Ş.'nin denetiminde önemlilik 500.000 ₺'dir. Denetçi, ticari alacakların şüpheli alacak karşılığı ayrılmaması nedeniyle 1.400.000 ₺ fazla gösterildiğini tespit etmiş; yönetim düzeltme yapmayı reddetmiştir. Yanlışlık başka bir kalemi etkilememekte, finansal tabloların önemli bir bölümünü temsil etmemekte ve diğer konularda yeterli kanıt elde edilmiş bulunmaktadır.\n\nDenetçinin vereceği görüş aşağıdakilerden hangisidir?",
        {
            'A': 'Sınırlı olumlu görüş',
            'B': 'Olumlu görüş',
            'C': 'Olumsuz görüş',
            'D': 'Görüş vermekten kaçınma',
            'E': 'Dikkat çekilen husus içeren olumlu görüş',
        },
        'A',
        'Yanlışlık (1.400.000 ₺) önemlilik düzeyini (500.000 ₺) aşmaktadır, dolayısıyla önemlidir; ancak tek bir kalemle sınırlı olduğundan yaygın değildir. Önemli fakat yaygın olmayan yanlışlıkta sınırlı olumlu görüş verilir.',
    ),
    # düzey 2
    '0018': patch(
        "BDS 705'e göre denetçi olumlu görüş dışında bir görüş vermeyi öngördüğünde üst yönetimden sorumlu olanlara aşağıdakilerden hangisini bildirir?",
        {
            'A': 'Denetim ücretindeki değişikliği',
            'B': 'Diğer müşterilerdeki benzer durumları',
            'C': 'Koşulları ve önerilen ifadeleri',
            'D': 'Önemlilik hesaplama ayrıntılarını',
            'E': 'Ekibin çalışma saatlerini',
        },
        'C',
        'Denetçi olumlu görüş dışında bir görüş vermeyi öngördüğünde, buna yol açan koşulları ve görüşün öngörülen ifadesini üst yönetimden sorumlu olanlara bildirir.',
    ),
    # düzey 2
    '0019': patch(
        "BDS 700'e göre aşağıdakilerden hangisi denetçi raporunun Görüşün Dayanağı bölümünde yer alması gereken unsurlardan biri değildir?",
        {
            'A': 'Elde edilen kanıtın yeterli ve uygun olduğu',
            'B': 'Denetçinin işletmeden bağımsız olduğu',
            'C': "Denetimin BDS'lere uygun yürütüldüğü",
            'D': 'Denetçinin sorumluluklarının açıklandığı bölüme atıf',
            'E': 'İşletmenin iç kontrolünün etkinliğine ilişkin görüş',
        },
        'E',
        "Görüşün Dayanağı bölümünde denetimin BDS'lere uygun yürütüldüğü, denetçinin sorumluluklarına ilişkin bölüme atıf, bağımsızlık ve etik sorumlulukların yerine getirildiği ve elde edilen kanıtın görüşe dayanak oluşturmak için yeterli ve uygun olduğu belirtilir. Denetçi iç kontrolün etkinliğine ilişkin görüş vermez.",
    ),
    # düzey 3
    '0020': patch(
        "Süreklilik esasının kullanılması uygundur, ancak işletmenin sürekliliğine ilişkin önemli bir belirsizlik vardır ve bu belirsizlik dipnotlarda yeterli biçimde açıklanmıştır.\n\nBDS 570'e göre denetçi ne yapar?",
        {
            'A': 'Görüş vermekten kaçınır',
            'B': 'Sınırlı olumlu görüş verir',
            'C': 'Olumlu görüş verir, önemli belirsizlik bölümü ekler',
            'D': 'Olumsuz görüş verir',
            'E': 'Olumlu görüş verir, konuyu kilit denetim konusu olarak sunar',
        },
        'C',
        'Önemli belirsizlik yeterince açıklanmışsa denetçi olumlu görüş verir ve raporuna "İşletmenin Sürekliliğine İlişkin Önemli Belirsizlik" başlıklı ayrı bir bölüm ekler.',
    ),
    # düzey 3
    '0021': patch(
        'Bir şirket, finansal tablolarının tamamını etkileyecek biçimde bağlı ortaklıklarını konsolide etmemiş; bu durum varlıkların, borçların, hasılatın ve kârın büyük bölümünü önemli ölçüde değiştirmektedir. Denetçi bu konuda yeterli kanıt elde etmiştir.\n\nDenetçinin vereceği görüş aşağıdakilerden hangisidir?',
        {
            'A': 'Olumsuz görüş',
            'B': 'Sınırlı olumlu görüş',
            'C': 'Görüş vermekten kaçınma',
            'D': 'Olumlu görüş',
            'E': 'Dikkat çekilen husus içeren olumlu görüş',
        },
        'A',
        'Yeterli kanıt elde edilmiş ve yanlışlık tabloların büyük bölümünü etkileyecek şekilde hem önemli hem yaygındır; olumsuz görüş verilir.',
    ),
    # düzey 3
    '0022': patch(
        "Finansal tablo tarihi 31 Aralık 2025 olan bir şirkette yönetimin işletmenin sürekliliğine ilişkin değerlendirmesi 30 Haziran 2026'ya kadar olan dönemi kapsamaktadır.\n\nBDS 570'e göre denetçi ne yapar?",
        {
            'A': 'Altı aylık değerlendirmeyi yeterli kabul ederek devam eder',
            'B': 'Değerlendirmeyi kendisi hazırlar',
            'C': 'Görüş vermekten kaçınır',
            'D': 'Değerlendirmenin en az on iki aya uzatılmasını ister',
            'E': 'Olumsuz görüş verir',
        },
        'D',
        'Yönetimin değerlendirmesi finansal tablo tarihinden itibaren on iki aydan kısa bir dönemi kapsıyorsa denetçi, değerlendirme dönemini en az on iki aya uzatmasını yönetimden ister.',
    ),
    # düzey 3
    '0023': patch(
        "Denetçi bir şirket hakkında olumsuz görüş vermiştir. Bu görüşe yol açan konuya ek olarak, sınırlı olumlu görüşü gerektirecek başka bir önemli yanlışlık da tespit etmiştir.\n\nBDS 705'e göre bu ikinci konu raporda nasıl ele alınır?",
        {
            'A': 'Rapordan çıkarılır',
            'B': 'Ayrı bir rapora konu edilir',
            'C': 'Dayanak bölümünde açıklanır',
            'D': 'Diğer Hususlar paragrafına alınır',
            'E': 'Kilit denetim konusu olarak sunulur',
        },
        'C',
        'Olumsuz görüş verilse ya da görüş vermekten kaçınılsa bile denetçi, farkında olduğu ve görüşün değiştirilmesini gerektirecek diğer hususların nedenlerini ve etkilerini dayanak bölümünde açıklar.',
    ),
    # düzey 2
    '0024': patch(
        "BDS 570'e göre işletmenin sürekliliği ile ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Süreklilik esasını kullanma ve değerlendirme sorumluluğu yönetimindir',
            'B': 'Önemli belirsizlik Dikkat Çeken Husus paragrafıyla sunulur',
            'C': 'Denetçi esasın uygunluğu hakkında sonuca varır',
            'D': 'Yeterince açıklanan belirsizlikte görüş değişmez',
            'E': 'Esas uygun değilse olumsuz görüş verilir',
        },
        'B',
        'Yeterince açıklanmış önemli belirsizlik, Dikkat Çeken Husus paragrafıyla değil, "İşletmenin Sürekliliğine İlişkin Önemli Belirsizlik" başlıklı ayrı bir bölümle raporda yer alır.',
    ),
    # düzey 3
    '0025': patch(
        "Denetçi, stokların değerlemesindeki önemli yanlışlık nedeniyle sınırlı olumlu görüş vermiştir.\n\nBDS 701'e göre bu konu raporda nasıl sunulur?",
        {
            'A': 'Diğer Hususlar paragrafında açıklanır',
            'B': 'Dayanak bölümünde açıklanır, KDK bölümünde atıf yapılır',
            'C': 'KDK bölümünde ayrıntılı açıklanır',
            'D': 'Hem KDK bölümünde hem dayanak bölümünde ayrıntılı olarak açıklanır',
            'E': 'Raporda yer almaz',
        },
        'B',
        'Sınırlı olumlu ya da olumsuz görüşe yol açan konular niteliği gereği kilit denetim konusudur; ancak KDK bölümünde açıklanmaz. Bu konular dayanak bölümünde açıklanır, KDK bölümünde bu bölüme atıf yapılır.',
    ),
    # düzey 3
    '0026': patch(
        "Denetçi sözleşmeyi kabul ettikten sonra yönetim, önemli bir şube ile ilgili kayıtların incelenmesine izin vermeyeceğini bildirmiştir.\n\nBDS 705'e göre denetçinin ilk olarak yapması gereken aşağıdakilerden hangisidir?",
        {
            'A': 'Şubeyi denetim kapsamından çıkarmak',
            'B': 'Hemen olumsuz görüş vermek',
            'C': 'Raporu sınırlamadan söz etmeden olumlu görüşle yayımlamak',
            'D': 'Kamu Gözetimi Kurumuna şikâyette bulunmak',
            'E': 'Yönetimden sınırlamayı kaldırmasını istemek',
        },
        'E',
        'Yönetim kapsamı sınırladığında ve bunun sınırlı olumlu görüşe ya da görüş vermekten kaçınmaya yol açması muhtemelse denetçi önce yönetimden sınırlamayı kaldırmasını ister; kaldırılmazsa üst yönetimden sorumlu olanlara bildirir ve alternatif prosedürlerle kanıt elde edip edemeyeceğini belirler.',
    ),
    # düzey 3
    '0027': patch(
        "Denetçi bir şirketin finansal tabloları hakkında, tabloların bütününü etkileyen bir kanıt eksikliği nedeniyle görüş vermekten kaçınmıştır. Yönetim, en azından nakit akış tablosu için ayrıca olumlu görüş verilmesini talep etmektedir.\n\nBDS 705'e göre bu talep için hangisi doğrudur?",
        {
            'A': 'Aynı raporda tek bir tablo için olumlu görüş verilmez',
            'B': 'Ayrı bir dikkat çekilen husus eklenir',
            'C': 'Talep, yönetimin yazılı beyanı alınarak raporda ayrıca karşılanır',
            'D': 'Nakit tablosu Görüş bölümünden çıkarılır',
            'E': 'Nakit akış tablosu için olumlu görüş verilir',
        },
        'A',
        'Denetçi finansal tabloların bütünü hakkında olumsuz görüş verdiğinde ya da görüş vermekten kaçındığında, aynı çerçevede hazırlanmış tek bir tablo veya unsur hakkında olumlu görüşü aynı rapora dahil etmez; bu, bütüne ilişkin görüşle çelişir.',
    ),
    # düzey 3
    '0028': patch(
        "Denetçi raporunu 15 Mart 2026'da tarihlemiştir. Tablolar yayımlanmadan önce 22 Mart 2026'da önemli bir müşterinin iflas ettiği öğrenilmiş, yönetim tabloları değiştirmiş ve değişikliği 28 Mart 2026'da onaylamıştır.\n\nBDS 560'a göre denetçinin yeni raporuyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': "28 Mart 2026'dan önceki bir tarih taşıyamaz",
            'B': 'Tarihsiz düzenlenir',
            'C': '15 Mart 2026 tarihini korur',
            'D': '22 Mart 2026 tarihli olur',
            'E': 'Önceki raporun ekine konur',
        },
        'A',
        'Tablolar değiştirildiğinde denetçi değişikliğe ilişkin gerekli prosedürleri uygular ve yeni bir rapor verir; yeni rapor, değiştirilmiş tabloların onaylandığı tarihten önceki bir tarihi taşıyamaz. Mevzuat izin veriyorsa yalnız değişikliğe ilişkin çift tarih uygulaması da mümkündür.',
    ),
    # düzey 2
    '0029': patch(
        "Denetçi, yeterli ve uygun kanıt elde ettikten sonra yanlışlıkların tek başına veya toplu olarak önemli olduğu ve finansal tablolarda yaygın olduğu sonucuna varmıştır.\n\nBDS 705'e göre denetçi hangi görüşü verir?",
        {
            'A': 'Olumlu görüş',
            'B': 'Sınırlı olumlu görüş',
            'C': 'Olumsuz görüş',
            'D': 'Dikkat çekilen husus içeren olumlu görüş',
            'E': 'Görüş vermekten kaçınma',
        },
        'C',
        'Yeterli ve uygun kanıt elde edilmiş ve yanlışlıklar hem önemli hem yaygınsa olumsuz görüş verilir.',
    ),
    # düzey 2
    '0030': patch(
        "BDS 701'e göre kilit denetim konularıyla ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Borsada işlem gören işletmelerde bildirilir',
            'B': 'Ayrı bir görüş niteliği taşımaz',
            'C': 'Üst yönetime bildirilen konulardan seçilir',
            'D': 'Olumsuz görüşün yerine kullanılabilir',
            'E': 'Önemli belirsizlik bölümünün yerine geçmez',
        },
        'D',
        'Kilit denetim konularının bildirilmesi, denetçinin olumlu görüş dışında bir görüş vermesi gereken durumlarda görüşün değiştirilmesinin yerine geçmez; işletmenin sürekliliğine ilişkin önemli belirsizlik açıklamasının da yerine geçmez.',
    ),
    # düzey 3
    '0031': patch(
        "I. Denetlenen işletme belirtilir.\nII. Finansal tabloları oluşturan her bir tablonun başlığı belirtilir.\nIII. Denetimin BDS'lere uygun olarak yürütüldüğü belirtilir.\n\nBDS 700'e göre yukarıdakilerden hangileri denetçi raporunun Görüş bölümünde yer alır?",
        {
            'A': 'I ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'C',
        "Görüş bölümünde denetlenen işletme, finansal tabloların denetlendiği, her bir tablonun başlığı, dipnotlara atıf ve tabloların ilişkin olduğu tarih ve dönem belirtilir. Denetimin BDS'lere uygun yürütüldüğü ise Görüşün Dayanağı bölümünde yer alır.",
    ),
    # düzey 3
    '0032': patch(
        "Denetçi, her birine ilişkin yeterli kanıt elde ettiği birden fazla önemli belirsizliğin olası etkileşimi ve tablolar üzerindeki toplam etkisi nedeniyle tablolar hakkında görüş oluşturmanın mümkün olmadığı sonucuna varmıştır.\n\nBDS 705'e göre bu son derece nadir durumda verilecek görüş hangisidir?",
        {
            'A': 'Olumlu görüş',
            'B': 'Dikkat çekilen husus içeren olumlu görüş',
            'C': 'Görüş vermekten kaçınma',
            'D': 'Sınırlı olumlu görüş',
            'E': 'Olumsuz görüş',
        },
        'C',
        'Birden fazla belirsizlik içeren son derece nadir durumlarda, her birine ilişkin yeterli kanıt elde edilmiş olsa bile belirsizliklerin olası etkileşimi nedeniyle görüş oluşturulamıyorsa denetçi görüş vermekten kaçınır.',
    ),
    # düzey 3
    '0033': patch(
        "Denetçi, yatırım amaçlı gayrimenkullerin gerçeğe uygun değer ölçümünü kilit denetim konusu olarak belirlemiştir.\n\nBDS 701'e göre raporda bu konunun açıklamasında aşağıdakilerden hangisi yer alır?",
        {
            'A': 'Sınırlı olumlu görüş gerekçesi',
            'B': 'Değerleme uzmanının ücreti',
            'C': 'Yönetimin onay imzası',
            'D': 'Konunun nasıl ele alındığı',
            'E': 'Gayrimenkuller hakkında ayrı görüş',
        },
        'D',
        'Her kilit denetim konusu için konunun neden en önemli konulardan biri sayıldığı, denetimde nasıl ele alındığı ve varsa tablolardaki ilgili açıklamalara atıf yer alır. Kilit denetim konuları hakkında ayrı görüş verilmez.',
    ),
    # düzey 3
    '0034': patch(
        "I. Dikkat Çeken Husus paragrafı ayrı bir bölümde sunulur.\nII. Diğer Hususlar paragrafı tablolarda sunulmamış bir hususla ilgilidir.\nIII. Her iki paragraf da görüşün sınırlı olumlu hâle geldiğini gösterir.\n\nBDS 706'ya göre yukarıdaki ifadelerden hangileri doğrudur?",
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'I ve III',
            'D': 'Yalnız I',
            'E': 'I, II ve III',
        },
        'B',
        'Her iki paragraf da ayrı bölümlerde uygun başlıkla sunulur ve görüşü değiştirmez; dikkat çeken husus tablolarda açıklanmış, diğer husus tablolarda yer almayan konulara ilişkindir.',
    ),
    # düzey 2
    '0035': patch(
        "BDS 705'e göre görüş vermekten kaçınılan bir denetçi raporunda aşağıdaki bölümlerden hangisi yer almaz?",
        {
            'A': 'Yönetimin Sorumlulukları',
            'B': 'Kilit Denetim Konuları',
            'C': 'Görüş Vermekten Kaçınmanın Dayanağı',
            'D': 'Görüş Vermekten Kaçınma',
            'E': 'Denetçinin Sorumlulukları',
        },
        'B',
        'Görüş vermekten kaçınıldığında, mevzuat gerektirmedikçe raporda Kilit Denetim Konuları bölümü yer almaz; BDS 720 kapsamındaki Diğer Bilgiler bölümü de bulunmaz.',
    ),
    # düzey 3
    '0036': patch(
        "BDS 706'ya göre denetçinin rapora Diğer Hususlar paragrafı ekleyebilmesi için aşağıdakilerden hangisi gerekli değildir?",
        {
            'A': 'Hususun dipnotlarda açıklanmış olması',
            'B': 'Kullanıcıların raporu anlamasıyla ilgili olması',
            'C': 'Mevzuatın bunu yasaklamaması',
            'D': 'Hususun kilit denetim konusu olmaması',
            'E': 'Denetçinin bunu gerekli görmesi',
        },
        'A',
        'Diğer Hususlar paragrafı tablolarda sunulmamış ya da açıklanmamış bir hususa ilişkindir; bu nedenle dipnotlarda açıklanmış olması aranmaz. Mevzuatla yasaklanmamış ve kilit denetim konusu olarak belirlenmemiş olması gerekir.',
    ),
    # düzey 3
    '0037': patch(
        "Denetçi, şirketin faaliyet raporunda yer alan satış rakamının denetlenmiş tablolardaki tutardan önemli ölçüde farklı olduğunu tespit etmiştir. Finansal tablolar doğrudur; yönetim faaliyet raporunu düzeltmeyi reddetmiştir.\n\nBDS 720'ye göre bu durum raporu nasıl etkiler?",
        {
            'A': 'Olumsuz görüş verilir',
            'B': 'Diğer Bilgiler bölümünde açıklanır',
            'C': 'Kilit denetim konusu yapılır',
            'D': 'Sınırlı olumlu görüş verilir',
            'E': 'Görüş vermekten kaçınılır',
        },
        'B',
        'Düzeltilmemiş önemli yanlışlık tabloların değil diğer bilgilerin içindeyse finansal tablolara ilişkin görüş değişmez; denetçi bunu raporun Diğer Bilgiler bölümünde açıklar.',
    ),
    # düzey 3
    '0038': patch(
        "Bir şirketin finansal tabloları işletmenin sürekliliği esasına göre hazırlanmıştır. Ancak şirket faaliyetlerini durdurma kararı almış ve denetçinin yargısına göre bu esasın kullanılması uygun değildir.\n\nBDS 570'e göre denetçi hangi görüşü verir?",
        {
            'A': 'Görüş vermekten kaçınma',
            'B': 'Olumlu görüş',
            'C': 'Önemli belirsizlik bölümü içeren olumlu görüş',
            'D': 'Sınırlı olumlu görüş',
            'E': 'Olumsuz görüş',
        },
        'E',
        'Tablolar süreklilik esasına göre hazırlanmış ancak bu esasın kullanılması uygun değilse denetçi olumsuz görüş verir.',
    ),
    # düzey 2
    '0039': patch(
        "BDS 700'e göre aşağıdakilerden hangisi bağımsız denetçi raporunda yer alan unsurlardan biri değildir?",
        {
            'A': 'Rapor tarihi',
            'B': 'Denetçinin bulunduğu yer',
            'C': 'Yönetim kurulu üyelerinin imzaları',
            'D': 'Raporun muhatabı',
            'E': 'Denetçinin imzası',
        },
        'C',
        'Raporda başlık, muhatap, görüş ve dayanak bölümleri, sorumluluk bölümleri, denetçinin imzası, bulunduğu yer ve rapor tarihi yer alır. Yönetim kurulu üyelerinin imzaları denetçi raporunun unsuru değildir.',
    ),
    # düzey 3
    '0040': patch(
        "BDS 705'e göre görüşü değiştirme gerekçesinin niteliği ile görüş türü arasındaki ilişki aşağıdakilerden hangisinde doğru eşleştirilmiştir?",
        {
            'A': 'Kanıt elde edilemedi, etki önemli ve yaygın – Olumsuz',
            'B': 'Kanıt elde edilemedi, etki önemli ve yaygın – Kaçınma',
            'C': 'Kanıt elde edilemedi, etki önemli ama yaygın değil – Kaçınma',
            'D': 'Yanlışlık önemli ve yaygın – Kaçınma',
            'E': 'Yanlışlık önemli ama yaygın değil – Olumsuz',
        },
        'B',
        'Yanlışlık önemli ama yaygın değil: sınırlı olumlu; önemli ve yaygın: olumsuz. Kanıt elde edilemedi ve olası etkiler önemli ama yaygın değil: sınırlı olumlu; önemli ve yaygın: görüş vermekten kaçınma.',
    ),
    # düzey 2
    '0041': patch(
        "Aşağıdakilerden hangisi BDS 706'ya göre Dikkat Çeken Husus paragrafına konu olabilecek durumlara örnek değildir?",
        {
            'A': 'Tablolarda açıklanan önemli bir sonraki olay',
            'B': 'Yeni bir standardın erken uygulanması',
            'C': 'Önceki yılın başka denetçice denetlenmesi',
            'D': 'Önemli bir davanın belirsiz sonucu',
            'E': 'Faaliyetleri etkileyen büyük bir afet',
        },
        'C',
        'Davanın belirsiz sonucu, büyük afet, yeni bir standardın yaygın etkili erken uygulanması gibi tablolarda açıklanmış hususlar dikkat çekilen husus olabilir. Önceki yılın başka denetçi tarafından denetlenmesi tablolarda yer almayan bir husustur ve Diğer Hususlar paragrafında sunulur.',
    ),
    # düzey 3
    '0042': patch(
        "Denetçi, yurt dışındaki bir bağlı ortaklığa yapılan ve aktif toplamının yaklaşık %4'ünü oluşturan yatırımın değerine ilişkin yeterli kanıt elde edememiştir; bu tutar önemlilik düzeyini aşmakta, diğer tüm konularda ise yeterli kanıt bulunmaktadır.\n\nDenetçinin vereceği görüş aşağıdakilerden hangisidir?",
        {
            'A': 'Olumlu görüş',
            'B': 'Olumsuz görüş',
            'C': 'Dikkat çekilen husus içeren olumlu görüş',
            'D': 'Sınırlı olumlu görüş',
            'E': 'Görüş vermekten kaçınma',
        },
        'D',
        'Kanıt elde edilemeyen konunun olası etkisi önemli fakat tek bir kalemle sınırlı ve tabloların önemli bir bölümünü temsil etmediğinden yaygın değildir; sınırlı olumlu görüş verilir.',
    ),
    # düzey 3
    '0043': patch(
        "Akasya A.Ş.'nin denetiminde finansal tabloların bütünü için önemlilik 900.000 ₺ olarak belirlenmiştir. Denetim sonunda düzeltilmemiş yanlışlıklar şunlardır: stoklarda fazla değerleme 320.000 ₺; tahakkuk etmemiş gider 180.000 ₺; sınıflandırma hatası 150.000 ₺. Yanlışlıkların niteliği önemli kabul edilmesini gerektirmemektedir ve kanıt sınırlaması bulunmamaktadır.\n\nDenetçinin vereceği görüş aşağıdakilerden hangisidir?",
        {
            'A': 'Görüş vermekten kaçınma',
            'B': 'Dikkat çekilen husus içeren sınırlı görüş',
            'C': 'Sınırlı olumlu görüş',
            'D': 'Olumsuz görüş',
            'E': 'Olumlu görüş',
        },
        'E',
        'Düzeltilmemiş yanlışlıkların toplamı 650.000 ₺ olup önemlilik düzeyinin (900.000 ₺) altındadır ve nitelik yönünden de önemli değildir. Yeterli kanıt elde edildiğinden denetçi olumlu görüş verir.',
    ),
    # düzey 2
    '0044': patch(
        "BDS 560'a göre denetçi raporu tarihinden sonra, ancak tablolar yayımlanmadan önce öğrenilen ve rapor tarihinde bilinseydi raporu değiştirebilecek bir olgu karşısında denetçinin ilk yapması gereken aşağıdakilerden hangisidir?",
        {
            'A': 'Kamuoyuna duyuru yapmak',
            'B': 'Konuyu yönetimle görüşmek',
            'C': 'Raporu geri çekmek',
            'D': 'Sözleşmeyi feshetmek',
            'E': 'Olumsuz görüş vermek',
        },
        'B',
        'Denetçi böyle bir olgudan haberdar olursa konuyu yönetimle ve gerektiğinde üst yönetimden sorumlu olanlarla görüşür, tabloların değiştirilmesi gerekip gerekmediğini belirler ve değiştirilecekse yönetimin bunu nasıl ele alacağını sorgular.',
    ),
    # düzey 3
    '0045': patch(
        "Bir şirket, sonucu henüz belli olmayan ve önemli tutarlı bir tazminat davasını dipnotlarında uygun ve yeterli biçimde açıklamıştır. Denetçi bu konunun kullanıcılar için temel nitelikte olduğunu düşünmektedir; konu kilit denetim konusu olarak belirlenmemiştir.\n\nBDS 706'ya göre denetçi ne yapar?",
        {
            'A': 'Dikkat Çeken Husus paragrafı ekler',
            'B': 'Görüş vermekten kaçınır',
            'C': 'Sınırlı olumlu görüş verir',
            'D': 'Olumsuz görüş verir',
            'E': 'Diğer Hususlar paragrafı ekler',
        },
        'A',
        'Tablolarda uygun şekilde açıklanmış ve kullanıcıların anlaması için temel nitelikteki bir hususa, görüşü değiştirmeden Dikkat Çeken Husus paragrafıyla dikkat çekilir.',
    ),
    # düzey 2
    '0046': patch(
        "BDS 700'e göre denetçi raporunun Yönetimin Sorumlulukları bölümünde aşağıdakilerden hangisi yer almaz?",
        {
            'A': 'Süreklilik esasının uygun kullanılması',
            'B': 'Önemli yanlışlıkları tespit etme sorumluluğu',
            'C': 'Hatasız sunum için gerekli iç kontrol',
            'D': 'Tabloların çerçeveye uygun hazırlanması',
            'E': 'İşletmenin sürekliliğinin değerlendirilmesi',
        },
        'B',
        'Yönetim; tabloların uygulanabilir çerçeveye uygun hazırlanmasından, hata veya hile kaynaklı önemli yanlışlık içermeyecek şekilde gerekli iç kontrolden ve işletmenin sürekliliğinin değerlendirilmesinden sorumludur. Makul güvence elde ederek önemli yanlışlık olup olmadığını değerlendirmek denetçinin sorumluluğudur.',
    ),
    # düzey 3
    '0047': patch(
        'Denetçi yıl sonundan sonra atandığı için dönem sonu stok sayımına katılamamış; alternatif prosedürlerle stok miktarlarına ilişkin yeterli kanıt da elde edememiştir. Stoklar önemlidir, ancak tabloların önemli bir bölümünü temsil etmemektedir.\n\nDenetçinin vereceği görüş aşağıdakilerden hangisidir?',
        {
            'A': 'Görüş vermekten kaçınma',
            'B': 'Dikkat çekilen husus içeren olumlu görüş',
            'C': 'Sınırlı olumlu görüş',
            'D': 'Olumlu görüş',
            'E': 'Olumsuz görüş',
        },
        'C',
        'Kanıt elde edilemeyen stokların olası etkisi önemli ancak yaygın değildir; bu durumda sınırlı olumlu görüş verilir.',
    ),
    # düzey 3
    '0048': patch(
        "Bir şirketin önceki yıl finansal tabloları başka bir denetçi tarafından denetlenmiş ve o denetçi olumlu görüş vermiştir. Bu bilgi cari yıl finansal tablolarında yer almamaktadır.\n\nBDS 710 ve BDS 706'ya göre cari yıl denetçisi bu bilgiyi raporunda nasıl sunar?",
        {
            'A': 'Görüşün Dayanağı bölümünde',
            'B': 'Dikkat Çeken Husus paragrafında',
            'C': 'Kilit Denetim Konuları bölümünde',
            'D': 'Diğer Hususlar paragrafında',
            'E': 'Görüş bölümünde',
        },
        'D',
        'Önceki dönem başka bir denetçi tarafından denetlenmişse cari denetçi; önceki denetçinin denetlediğini, verdiği görüşün türünü ve rapor tarihini Diğer Hususlar paragrafında belirtir. Tablolarda yer almayan hususlar Diğer Hususlar paragrafının konusudur.',
    ),
    # düzey 2
    '0049': patch(
        'BDS 700 Finansal Tablolara İlişkin Görüş Oluşturma ve Raporlama standardına göre denetçi raporunda ilk sırada yer alması gereken bölüm aşağıdakilerden hangisidir?',
        {
            'A': 'Yönetimin Sorumlulukları',
            'B': 'Görüşün Dayanağı',
            'C': 'Diğer Bilgiler',
            'D': 'Kilit Denetim Konuları',
            'E': 'Görüş',
        },
        'E',
        'BDS 700\'e göre denetçi raporunun ilk bölümü "Görüş" başlığını taşıyan bölümdür; "Görüşün Dayanağı" bölümü görüş bölümünden hemen sonra gelir.',
    ),
    # düzey 3
    '0050': patch(
        'Bir şirketin merkez binasında çıkan yangında muhasebe kayıtlarının ve belgelerin büyük bölümü yok olmuş, yedekleri de bulunmamaktadır. Denetçi satışlar, alacaklar, stoklar ve giderler dahil tabloların büyük bölümü için alternatif prosedürlerle de yeterli kanıt elde edememiştir.\n\nDenetçinin vereceği görüş aşağıdakilerden hangisidir?',
        {
            'A': 'Görüş vermekten kaçınma',
            'B': 'Olumsuz görüş',
            'C': 'Dikkat çekilen husus içeren olumlu görüş',
            'D': 'Sınırlı olumlu görüş',
            'E': 'Olumlu görüş',
        },
        'A',
        'Yeterli ve uygun kanıt elde edilememiş ve tespit edilmemiş yanlışlıkların olası etkileri hem önemli hem yaygındır; bu durumda denetçi görüş vermekten kaçınır.',
    ),
    # düzey 2
    '0051': patch(
        'Aşağıdaki görüşlerden hangisini içeren bir raporda BDS 720 kapsamındaki Diğer Bilgiler bölümü yer almaz?',
        {
            'A': 'Dikkat çekilen husus içeren olumlu görüş',
            'B': 'Olumsuz görüş',
            'C': 'Sınırlı olumlu görüş',
            'D': 'Olumlu görüş',
            'E': 'Görüş vermekten kaçınma',
        },
        'E',
        'Görüş vermekten kaçınıldığında, tablolar hakkında daha fazla bilgi verilmesi kaçınmanın anlamını zayıflatacağından raporda Diğer Bilgiler bölümü yer almaz.',
    ),
    # düzey 2
    '0052': patch(
        "BDS 706'ya göre dikkat çeken husus ile diğer husus paragrafları arasındaki temel fark aşağıdakilerden hangisidir?",
        {
            'A': 'Yönetimin onayına bağlı olması',
            'B': 'Önemlilik tutarını aşıp aşmaması',
            'C': 'Tablolarda sunulup sunulmamış olması',
            'D': 'Raporun başında yer alması',
            'E': 'Görüşü değiştirip değiştirmemesi',
        },
        'C',
        'Dikkat çeken husus tablolarda sunulmuş ya da açıklanmış bir hususa, diğer husus ise tablolarda sunulmamış ancak kullanıcıların denetimi, denetçinin sorumluluklarını ya da raporu anlamasıyla ilgili bir hususa ilişkindir. İkisi de görüşü değiştirmez.',
    ),
    # düzey 2
    '0053': patch(
        'Bir şirket, aktif toplamı içinde küçük bir paya sahip olan ve önemlilik düzeyini aşmayan bir alacak için şüpheli alacak karşılığı ayırmamıştır. Diğer konularda sorun bulunmamaktadır.\n\nDenetçinin görüşü ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Görüş değişmez',
            'B': 'Sınırlı olumlu görüş verilir',
            'C': 'Olumsuz görüş verilir',
            'D': 'Rapor ertelenir',
            'E': 'Görüş vermekten kaçınılır',
        },
        'A',
        'Yanlışlık önemli değilse görüş değişmez; denetçi düzeltilmesini talep edebilir ancak olumlu görüş verir.',
    ),
    # düzey 3
    '0054': patch(
        "Süreklilik esasının kullanılması uygundur, işletmenin sürekliliğine ilişkin önemli bir belirsizlik bulunmakta, ancak yönetim bu belirsizliği finansal tablolarda yeterli şekilde açıklamamaktadır.\n\nBDS 570'e göre denetçi hangi görüşü verir?",
        {
            'A': 'Görüş vermekten kaçınma',
            'B': 'Olumlu görüş',
            'C': 'Önemli belirsizlik bölümü içeren olumlu görüş',
            'D': 'Duruma göre sınırlı olumlu veya olumsuz görüş',
            'E': 'Dikkat çeken husus içeren olumlu görüş',
        },
        'D',
        "Önemli belirsizlik yeterince açıklanmamışsa denetçi, BDS 705'e uygun olarak duruma göre sınırlı olumlu ya da olumsuz görüş verir ve dayanak bölümünde önemli belirsizliğin varlığını belirtir.",
    ),
    # düzey 3
    '0055': patch(
        "I. Raporun ilk bölümü Görüş bölümüdür.\nII. Görüşün Dayanağı bölümü Görüş bölümünden hemen sonra gelir.\nIII. Kilit Denetim Konuları bölümü tüm işletmelerin raporlarında zorunludur.\n\nBDS 700 ve BDS 701'e göre yukarıdaki ifadelerden hangileri doğrudur?",
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'Yalnız I',
            'D': 'I ve III',
            'E': 'I, II ve III',
        },
        'B',
        'Görüş bölümü ilk sırada, Görüşün Dayanağı hemen ardından yer alır. Kilit denetim konularının bildirilmesi borsada işlem gören işletmelerin denetimlerinde zorunludur; diğerlerinde mevzuat gerektirirse ya da denetçi karar verirse uygulanır.',
    ),
    # düzey 2
    '0056': patch(
        "BDS 701'e göre aşağıdakilerden hangisi denetçinin kilit denetim konularını belirlerken dikkate aldığı hususlardan biri değildir?",
        {
            'A': 'Önemli risk olarak belirlenmiş alanlar',
            'B': 'Yüksek önemli yanlışlık riski',
            'C': 'Yönetimin tercih ettiği konu olması',
            'D': 'Dönemde gerçekleşen önemli işlemlerin etkisi',
            'E': 'Yönetimin önemli muhakemesini içeren alanlar',
        },
        'C',
        'Denetçi; önemli yanlışlık riskinin yüksek olduğu ya da önemli risk olarak belirlenen alanları, önemli yönetim muhakemesi içeren alanları ve dönemde gerçekleşen önemli olay ve işlemlerin etkisini dikkate alır.',
    ),
    # düzey 2
    '0057': patch(
        "BDS 705'e göre sınırlı olumlu görüş içeren bir raporda Görüş bölümündeki ifadeyle ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Tabloların gerçeğe uygun sunulmadığı belirtilir',
            'B': 'Görüş oluşturulamadığı belirtilir',
            'C': 'Sorunun etkileri dahil gerçeğe uygun sunulduğu belirtilir',
            'D': 'Sorun nedeniyle görüşün ertelendiği belirtilir',
            'E': 'Sorunun etkileri hariç gerçeğe uygun sunulduğu belirtilir',
        },
        'E',
        'Sınırlı olumlu görüşte, dayanak bölümünde açıklanan hususun etkileri, kanıt sınırlamasında ise olası etkileri hariç olmak üzere tabloların tüm önemli yönleriyle gerçeğe uygun sunulduğu belirtilir.',
    ),
    # düzey 2
    '0058': patch(
        'Olumlu görüş içeren bir denetçi raporunda görüş cümlesinin özü aşağıdakilerden hangisidir?',
        {
            'A': 'Tüm önemli yönleriyle gerçeğe uygun sunulduğu',
            'B': 'Tüm işlemlerin incelendiği',
            'C': 'Yanlışlık içermediği',
            'D': 'İç kontrolün etkin olduğu',
            'E': 'Vergi mevzuatına uyulduğu',
        },
        'A',
        'Olumlu görüş, finansal tabloların tüm önemli yönleriyle uygulanabilir finansal raporlama çerçevesine uygun olarak gerçeğe uygun biçimde sunulduğunu ifade eder; tabloların hiç yanlışlık içermediği anlamına gelmez.',
    ),
    # düzey 3
    '0059': patch(
        "Denetçi, önceki dönem için sınırlı olumlu görüş vermiş, görüşe yol açan konu cari dönemde çözülmemiştir ve cari dönem rakamlarını da önemli ölçüde etkilemektedir.\n\nBDS 710'a göre cari dönem raporunda ne yapılır?",
        {
            'A': 'Önceki rapor geri çekilir',
            'B': 'Cari dönem görüşü de değiştirilir',
            'C': 'Konu Diğer Hususlar paragrafında geçer',
            'D': 'Görüş vermekten kaçınılır',
            'E': 'Konu raporda belirtilmez',
        },
        'B',
        'Önceki dönem görüşünü değiştiren konu çözülmemişse ve cari dönem rakamlarını da etkiliyorsa, denetçi cari dönem tablolarına ilişkin görüşünü de değiştirir ve dayanak bölümünde hem cari hem karşılaştırmalı rakamlar üzerindeki etkiye değinir.',
    ),
    # düzey 3
    '0060': patch(
        "Denetçi, denetlenen şirketle ilgili olarak Türk Ticaret Kanunu'nun ayrıca öngördüğü bildirim yükümlülüklerini de raporunda yerine getirmektedir.\n\nBDS 700'e göre bu bildirimler raporda nasıl sunulur?",
        {
            'A': 'Ayrı bir rapor bölümünde',
            'B': 'Görüşün Dayanağı bölümünde',
            'C': 'Kilit Denetim Konuları bölümünde',
            'D': 'Dikkat Çeken Hususlar bölümünde',
            'E': 'Görüş bölümünün içinde',
        },
        'A',
        'BDS\'lerin gerektirdiklerine ek olarak mevzuattan kaynaklanan raporlama sorumlulukları, raporun ayrı bir bölümünde, "Mevzuattan Kaynaklanan Diğer Yükümlülüklere İlişkin Rapor" gibi bir başlıkla sunulur.',
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
    print(f"1 paket / {len(PATCHES)} soru ('Denetim Raporu ve Görüş Türleri' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
