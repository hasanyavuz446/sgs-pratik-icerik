#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TMS 21 Kur Değişiminin Etkileri — profil kalibrasyonu + kalıp-dolgu temizliği.

ÖLÇÜLEN KUSUR (2026-07-28):
  · kör öğrenci %30 "en kısayı seç" — boy: uzun 14 / kısa 32 (n=50)
  · eleme stratejisi %34 (havuzun en kötüsüyle başabaş; rastgele %20, havuz ort. %23):
    "Her hâlde" 31 çeldiricide / 0 doğru şıkta · "zorunda" 39/0 · "hiçbir" 25/0 ·
    "…bir ölçümü ifade eder/karşılar" 29/0 · "niteliğinde" 12/0
  · olumsuz kök %16 — oysa TMS 21'in son iki gerçek görünümü de olumsuz köklü
  · harf dağılımı A12 B11 C12 D9 E16 (E fazla, D eksik)
  → 34 soruda 81 çeldirici kalıp-dolguludur. Dolgu SİLİNMİYOR; §5'in ertelenmiş
    reçetesi uygulanıyor: uygun boyutta GERÇEK içerikle değiştiriliyor.

KALİBRASYON (çıkmış kâğıtlardan ölçüldü, kopya yok — §1/§11):
  · 2024 s.50 + 2025 s.53 — "geçerli para biriminin tespiti", İKİSİ DE OLUMSUZ kök
  · 2021 + 2025 s.48 — öncüllü faktör listesi ("hangileri")
  · 2016-18 s.40/41/44 — parasal ↔ parasal olmayan ayrımı ve hangi kur; şıklar KISA
  · 2023 s.50 — yüksek enflasyonlu ekonomi · 2016-18 s.43 — kur farkının sunumu
  · 2014-16 s.39 — "…para birimine ne denir?" tanım
  ⚠️ TMS 21 incelenen 11 dosyada HESAP sorusu olarak HİÇ sorulmamış (kural §1 notu:
    "Hesap sorusu değil"). Bu yüzden sayısal oran ARTIRILMIYOR; mevcut 8 hesap
    sorusu öğretici olduğu için korunuyor ama üzerine eklenmiyor.

Dayanak: KGK TMS 21 par. 3, 8-14, 21-24, 28-32, 35, 39, 42-43, 47-48, 52.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/tms_21_kur_degisimi.json"
STYLE_REF = "SGS Muhasebe Standartlari TMS 21"


def std_patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": "TMS 21 Kur Degisiminin Etkileri"},
        "validYear": 2026, "mockExamId": None,
    }


PATCHES = {
    'std-tms21-gen-0002': std_patch(
        "TMS 21'e göre raporlama para birimi bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Yalnızca işletmenin yerleşik bulunduğu ülkenin resmî para birimi raporlama para birimi olabilir',
            'B': 'Geçerli para birimiyle aynı olma koşuluna bağlıdır ve ondan farklı seçilemez',
            'C': 'Yalnızca ABD doları veya avro olarak seçilebilir',
            'D': 'Finansal tabloların sunulduğu para birimidir ve geçerli para biriminden farklı olabilir',
            'E': 'Vergi idaresi tarafından belirlenir ve değiştirilemez',
        },
        'D',
        "TMS 21 par. 8 ve 38: raporlama para birimi, finansal tabloların sunulduğu para birimidir. İşletme tablolarını herhangi bir para biriminde sunabilir; bu para birimi geçerli para biriminden farklı olduğunda par. 39'daki çevrim yöntemi uygulanır.",
    ),
    'std-tms21-gen-0007': std_patch(
        'Geçerli para biriminin değiştirilmesi bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Değişiklik geriye dönük uygulanır; karşılaştırmalı önceki dönem tutarları yeniden düzenlenir',
            'B': 'Geçerli para birimi bir kez seçildikten sonra sabit kalır',
            'C': 'Değişiklik ileriye dönük uygulanır; kalemler değişim tarihindeki kurla çevrilir',
            'D': 'Değişiklik yalnızca yönetimin tercihiyle serbestçe yapılabilir',
            'E': 'Değişimden doğan farklar dönemin kâr veya zararına yansıtılır',
        },
        'C',
        'TMS 21 par. 35-37: geçerli para birimi, ancak esas işlem koşullarında değişiklik olduğunda değişir. Değişiklik ileriye dönük uygulanır; tüm kalemler değişim tarihindeki kur kullanılarak yeni geçerli para birimine çevrilir ve doğan tutarlar tarihî maliyet sayılır.',
    ),
    'std-tms21-gen-0009': std_patch(
        "Aşağıdakilerden hangisi TMS 21'e göre parasal kalem DEĞİLDİR?",
        {
            'A': 'Sabit tutarda tahsil edilecek ticari alacak',
            'B': 'Belirli tutarda ödenecek satıcı borcu',
            'C': 'Kasadaki ve bankadaki yabancı para nakit',
            'D': 'Peşin ödenmiş sigorta primi',
            'E': 'Nakden ödenecek temettü borcu',
        },
        'D',
        'TMS 21 par. 16: parasal kalemin ayırt edici özelliği, sabit veya belirlenebilir tutarda para alma hakkı ya da ödeme yükümlülüğü taşımasıdır. Peşin ödenmiş sigorta primi para değil hizmet alma hakkı verdiğinden parasal olmayan kalemdir.',
    ),
    'std-tms21-gen-0010': std_patch(
        "Aşağıdakilerden hangisi TMS 21'e göre parasal olmayan kalemdir?",
        {
            'A': 'Tahsil edilecek alacak senetleri',
            'B': 'Ödenecek banka kredisi',
            'C': 'Yabancı para vadesiz mevduat',
            'D': 'Şerefiye',
            'E': 'Tutarı sözleşmeyle belirlenmiş kira borcu',
        },
        'D',
        'TMS 21 par. 16: parasal olmayan kalemler para alma/ödeme hakkı içermez. Şerefiye, stoklar, maddi duran varlıklar ve peşin ödenmiş giderler bu gruptadır; alacak, borç, mevduat ve kredi ise parasal kalemdir.',
    ),
    'std-tms21-gen-0013': std_patch(
        'Yurtdışındaki işletmenin geçerli para biriminin belirlenmesi bakımından aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'Yurtdışı işletmenin geçerli para birimi ana ortaklığınkiyle aynı kabul edilir',
            'B': 'Faaliyetlerin ana ortaklığın uzantısı mı bağımsız mı olduğu değerlendirilir',
            'C': 'Ana ortaklıkla yapılan işlemlerin faaliyetler içindeki payı dikkate alınır',
            'D': 'Faaliyetlerden doğan nakit akışlarının ana ortaklığı doğrudan etkileyip etkilemediğine bakılır',
            'E': 'Faaliyet nakit akışlarının borç servisine yetip yetmediği değerlendirilir',
        },
        'A',
        "TMS 21 par. 11: yurtdışındaki işletmenin geçerli para birimi ayrıca belirlenir ve ana ortaklığınkiyle aynı olmak durumunda değildir. Par. 11'deki dört gösterge faaliyetin bağımsızlık derecesini ölçer.",
    ),
    'std-tms21-gen-0014': std_patch(
        'Bir işletmenin ürün fiyatları ve maliyetleri ağırlıklı olarak avro cinsinden belirlenmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Geçerli para birimi yerleşik olduğu ülkenin para birimidir',
            'B': 'Geçerli para birimi bütçesini hazırladığı para birimidir',
            'C': 'Geçerli para birimi ortaklarının bulunduğu ülkenin para birimidir',
            'D': 'İşletmenin geçerli para birimi avrodur',
            'E': 'Geçerli para birimi en çok borçlandığı para birimidir',
        },
        'D',
        'TMS 21 par. 9: geçerli para birimi belirlenirken birincil göstergeler, satış fiyatlarını ve mal/hizmet maliyetlerini en çok etkileyen para birimidir. İkisi de avro olduğundan geçerli para birimi avrodur; yerleşim yeri veya bütçe para birimi belirleyici değildir.',
    ),
    'std-tms21-gen-0017': std_patch(
        'Yabancı para işlemin ilk muhasebeleştirilmesi bakımından aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'İşlem tarihindeki spot kur uygulanır',
            'B': 'Raporlama dönemi sonundaki kapanış kuru uygulanır',
            'C': 'İşlem tarihi, muhasebeleştirme koşullarının ilk kez sağlandığı tarihtir',
            'D': 'Kurlar önemli ölçüde dalgalanmıyorsa haftalık veya aylık ortalama kur kullanılabilir',
            'E': 'Yabancı para tutar, geçerli para birimine çevrilerek kaydedilir',
        },
        'B',
        'TMS 21 par. 21: yabancı para işlem, ilk muhasebeleştirmede işlem tarihindeki spot kur uygulanarak geçerli para biriminde kaydedilir. Kapanış kuru ilk kayıt değil, par. 23(a) uyarınca dönem sonu ölçümünde kullanılır.',
    ),
    'std-tms21-gen-0018': std_patch(
        'İşlem tarihindeki kurun uygulanmasında kolaylık bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kur ne kadar dalgalansın, ortalama kur her zaman kullanılabilir',
            'B': 'Ortalama kur yalnızca yıllık dönemler için kullanılabilir',
            'C': 'Kurlar önemli ölçüde dalgalanmıyorsa dönemin ortalama kuru kullanılabilir',
            'D': "Ortalama kur kullanımı TMS 21'de tümüyle yasaklanmıştır",
            'E': 'Ortalama kur yerine yıl sonu kapanış kuru geriye dönük uygulanır',
        },
        'C',
        'TMS 21 par. 22: kolaylık sağlamak amacıyla haftalık veya aylık ortalama kur kullanılabilir; ancak kurlar önemli ölçüde dalgalanıyorsa dönem ortalamasının kullanılması uygun değildir.',
    ),
    'std-tms21-gen-0019': std_patch(
        'Raporlama dönemi sonunda yabancı para PARASAL kalemler bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kapanış kuruyla çevrilir; doğan kur farkı dönemin kâr veya zararına yansıtılır',
            'B': 'İşlem tarihindeki kurla çevrilir ve dönem sonunda değiştirilmez',
            'C': 'Çevrim yapılmaz; kalem ilk kayıt tutarında bırakılır ve kur değişimi sonuçlara girmez',
            'D': 'Dönemin ortalama kuruyla çevrilir',
            'E': 'Gerçeğe uygun değerin belirlendiği tarihteki kurla çevrilir',
        },
        'A',
        'TMS 21 par. 23(a): her raporlama dönemi sonunda yabancı para parasal kalemler kapanış kuruyla çevrilir. Par. 28 uyarınca çevrimden doğan kur farkı, oluştuğu dönemin kâr veya zararında muhasebeleştirilir.',
    ),
    'std-tms21-gen-0020': std_patch(
        'Tarihî maliyetiyle ölçülen yabancı para PARASAL OLMAYAN kalemler bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kapanış kuruyla çevrilir ve kur farkı doğar',
            'B': 'Dönemin ortalama kuruyla çevrilir',
            'C': 'Gerçeğe uygun değerin belirlendiği tarihteki kurla çevrilir',
            'D': 'Her raporlama döneminde yeniden değerlenir ve fark özkaynağa alınır',
            'E': 'İşlem tarihindeki kurla çevrilir',
        },
        'E',
        'TMS 21 par. 23(b): yabancı para üzerinden tarihî maliyetle ölçülen parasal olmayan kalemler işlem tarihindeki kurla çevrilir. Kapanış kuruyla yeniden çevrilmediği için bu kalemlerden kur farkı doğmaz.',
    ),
    'std-tms21-gen-0021': std_patch(
        'Gerçeğe uygun değeriyle ölçülen yabancı para PARASAL OLMAYAN kalemler bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşlem tarihindeki tarihî kurla çevrilir ve sonraki dönemlerde yeniden ölçülmez',
            'B': 'Raporlama dönemi sonundaki kapanış kuruyla çevrilir',
            'C': 'Gerçeğe uygun değerin belirlendiği tarihteki kurla çevrilir',
            'D': 'Dönemin ortalama kuruyla çevrilir',
            'E': 'İlk kayıt tutarında bırakılır ve çevrim yapılmaz',
        },
        'C',
        'TMS 21 par. 23(c): gerçeğe uygun değeri üzerinden ölçülen yabancı para parasal olmayan kalemler, gerçeğe uygun değerin belirlendiği tarihteki kur kullanılarak çevrilir.',
    ),
    'std-tms21-gen-0022': std_patch(
        'Parasal kalemlerin ödenmesinden veya çevrilmesinden doğan kur farkları bakımından aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'Kural olarak oluştukları dönemin kâr veya zararında muhasebeleştirilir',
            'B': 'Yurtdışındaki işletmedeki net yatırımın parçası olan kalemde diğer kapsamlı gelire alınır',
            'C': 'Ödeme dönem içinde yapılırsa fark ödeme tarihi itibarıyla kâr veya zarara yansıtılır',
            'D': 'Kur farkı, kalemin ilk kaydı ile ödeme veya dönem sonu ölçümü arasındaki kur değişiminden doğar',
            'E': 'Kur farkları doğrudan özkaynakta biriktirilir',
        },
        'E',
        "TMS 21 par. 28: parasal kalemlerden doğan kur farkları oluştukları dönemin kâr veya zararında muhasebeleştirilir. Özkaynakta biriktirme genel kural değildir; par. 32'deki net yatırım istisnası ile par. 39(c)'deki çevrim farkları dışında uygulanmaz.",
    ),
    'std-tms21-gen-0023': std_patch(
        'Parasal olmayan bir kalemin kazanç veya kaybı diğer kapsamlı gelirde muhasebeleştiriliyorsa kur bileşeni bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kur bileşeni de diğer kapsamlı gelirde muhasebeleştirilir',
            'B': 'Kur bileşeni ayrıştırılıp kâr veya zarara yansıtılır',
            'C': 'Kur bileşeni ayrıştırılarak ilgili varlığın maliyetine eklenir',
            'D': 'Kur bileşeni yalnızca dipnotta açıklanır',
            'E': 'Kur bileşeni dağıtılmamış kârlara doğrudan aktarılır',
        },
        'A',
        'TMS 21 par. 30: bir parasal olmayan kalemin kazanç veya kaybı diğer kapsamlı gelirde muhasebeleştirildiğinde, bu kazanç veya kaybın kur bileşeni de diğer kapsamlı gelirde muhasebeleştirilir.',
    ),
    'std-tms21-gen-0027': std_patch(
        'Bir işletme yabancı para cinsinden aldığı makineyi tarihî maliyetle izlemektedir. Dönem sonunda kur yükselmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Makine işlem tarihi kuruyla kayıtlı kalır; kur farkı doğmaz',
            'B': 'Makine kapanış kuruyla yeniden çevrilir ve kur farkı geliri yazılır',
            'C': 'Makine kapanış kuruyla çevrilir ve fark özkaynağa alınır',
            'D': 'Makine dönemin ortalama kuruyla yeniden çevrilir',
            'E': 'Makinenin amortismanı kapanış kuruyla yeniden hesaplanır',
        },
        'A',
        'TMS 21 par. 23(b): tarihî maliyetle ölçülen yabancı para parasal olmayan kalemler işlem tarihindeki kurla çevrilir ve dönem sonunda yeniden çevrilmez. Bu nedenle kur değişimi makinenin defter değerini ve amortismanını etkilemez.',
    ),
    'std-tms21-gen-0029': std_patch(
        'Yurtdışındaki işletmedeki net yatırımın bir parçası olan parasal kalemin kur farkı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Doğrudan dönemin kâr veya zararına yansıtılır; elden çıkarmada ek bir işlem yapılmaz',
            'B': 'Diğer kapsamlı gelirde muhasebeleştirilir; elden çıkarmada kâr veya zarara sınıflandırılır',
            'C': 'Yatırımın defter değerine eklenir ve elden çıkarmada maliyetle birlikte dikkate alınır',
            'D': 'Özkaynakta biriktirilir ve elden çıkarmada da özkaynakta kalır',
            'E': 'Yalnızca dipnotta açıklanır, kayda alınmaz',
        },
        'B',
        'TMS 21 par. 32: yurtdışındaki işletmedeki net yatırımın parçasını oluşturan parasal kalemden doğan kur farkı diğer kapsamlı gelirde muhasebeleştirilir ve par. 48 uyarınca net yatırımın elden çıkarılmasında kâr veya zarara yeniden sınıflandırılır.',
    ),
    'std-tms21-gen-0031': std_patch(
        'Geçerli para biriminden farklı bir raporlama para birimine çevrimde varlık ve borçlar bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşlem tarihlerindeki tarihî kurlarla çevrilir',
            'B': 'İlgili tablonun tarihindeki kapanış kuruyla çevrilir',
            'C': 'Dönemin ortalama kuruyla çevrilir',
            'D': 'Geçerli para biriminde bırakılır, çevrim yapılmaz',
            'E': 'Yalnızca parasal olanlar çevrilir, parasal olmayanlar aynen aktarılır',
        },
        'B',
        'TMS 21 par. 39(a): her finansal durum tablosundaki varlık ve borçlar, o tablonun tarihindeki kapanış kuru kullanılarak raporlama para birimine çevrilir.',
    ),
    'std-tms21-gen-0032': std_patch(
        'Raporlama para birimine çevrimde gelir ve giderler bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tüm gelir ve giderler, finansal durum tablosu tarihindeki kapanış kuru kullanılarak çevrilir',
            'B': 'Dönem başındaki açılış kuruyla çevrilir',
            'C': 'Çevrilmez, geçerli para biriminde raporlanır',
            'D': 'İşlem tarihlerindeki kurlarla çevrilir; ortalama kur yaklaşık olarak kullanılabilir',
            'E': 'Yalnızca nakit çıkışı doğuran giderler çevrilir',
        },
        'D',
        'TMS 21 par. 39(b): gelir ve giderler işlem tarihlerindeki kurlar kullanılarak çevrilir. Par. 40 uyarınca kurlar önemli ölçüde dalgalanmıyorsa yaklaşık bir kur olarak dönemin ortalama kuru kullanılabilir.',
    ),
    'std-tms21-gen-0033': std_patch(
        'Raporlama para birimine çevrimden doğan kur farkları bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Doğrudan dönemin kâr veya zararında muhasebeleştirilir',
            'B': 'Diğer kapsamlı gelirde muhasebeleştirilir',
            'C': 'Varlıkların maliyetine eklenir',
            'D': 'Kayda alınmaz, yalnızca dipnotta açıklanır',
            'E': 'Dağıtılmamış kârlara doğrudan aktarılır',
        },
        'B',
        "TMS 21 par. 39(c): geçerli para biriminden farklı bir raporlama para birimine çevrimde ortaya çıkan tüm kur farkları diğer kapsamlı gelirde muhasebeleştirilir. Bu, tek tek parasal kalemlerin par. 28'deki kur farkından ayrı bir sunumdur.",
    ),
    'std-tms21-gen-0034': std_patch(
        'Yurtdışındaki işletmenin elden çıkarılması bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Özkaynakta biriken kur farkları kâr veya zarara yeniden sınıflandırılır',
            'B': 'Biriken kur farkları özkaynakta kalmaya devam eder',
            'C': 'Biriken kur farkları dağıtılmamış kârlara aktarılır',
            'D': 'Biriken kur farkları geriye dönük olarak düzeltilir',
            'E': 'Biriken kur farkları elden çıkarma bedelinden indirilir',
        },
        'A',
        'TMS 21 par. 48: yurtdışındaki bir işletmenin elden çıkarılmasında, diğer kapsamlı gelirde muhasebeleştirilip özkaynakta biriktirilmiş olan kur farklarının birikmiş tutarı, elden çıkarma kazanç veya kaybının muhasebeleştirildiği anda kâr veya zarara sınıflandırılır.',
    ),
    'std-tms21-gen-0035': std_patch(
        'Yurtdışındaki işletmenin ediniminde doğan şerefiye ve gerçeğe uygun değer düzeltmeleri bakımından aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'Şerefiye yurtdışındaki işletmenin varlığı olarak ele alınır',
            'B': 'Şerefiye yurtdışındaki işletmenin geçerli para biriminde ifade edilir',
            'C': 'Şerefiye kapanış kuruyla raporlama para birimine çevrilir',
            'D': 'Defter değerlerine yapılan gerçeğe uygun değer düzeltmeleri de aynı biçimde çevrilir',
            'E': 'Şerefiye ana ortaklığın geçerli para biriminde sabit tutulur',
        },
        'E',
        'TMS 21 par. 47: yurtdışındaki işletmenin ediniminde doğan şerefiye ile varlık ve borçların defter değerlerine yapılan gerçeğe uygun değer düzeltmeleri, o işletmenin geçerli para biriminde ifade edilen kalemler olarak ele alınır ve kapanış kuruyla çevrilir.',
    ),
    'std-tms21-gen-0036': std_patch(
        "TMS 21'e göre yapılacak açıklamalar bakımından aşağıdakilerden hangisi YANLIŞTIR?",
        {
            'A': 'Kâr veya zarara yansıtılan kur farkı tutarı, gerçeğe uygun değer farkı kâr veya zarara yansıtılanlar hariç açıklanır',
            'B': 'Kur farkları için açıklama yükümlülüğü yalnızca yurtdışı faaliyeti olanlara getirilmiştir',
            'C': 'Özkaynakta biriken net kur farkları açıklanır',
            'D': 'Biriken kur farklarının dönem başı ve dönem sonu mutabakatı verilir',
            'E': 'Raporlama para birimi geçerli para biriminden farklıysa bu durum ve gerekçesi açıklanır',
        },
        'B',
        'TMS 21 par. 52-53: açıklama yükümlülüğü kur farkı doğan tüm işletmeler için geçerlidir; yurtdışı faaliyet koşuluna bağlanmamıştır. Kâr veya zarara yansıtılan tutar, özkaynakta biriken net farklar ve bunların mutabakatı açıklanır.',
    ),
    'std-tms21-gen-0037': std_patch(
        'Raporlama para biriminin geçerli para biriminden farklı olması hâlinde aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Sonuçlar ve finansal durum, TMS 21 par. 39'daki yönteme göre raporlama para birimine çevrilir",
            'B': 'İşletme raporlama para birimini kullanmaktan vazgeçmek durumundadır',
            'C': 'Yalnızca geçerli para birimindeki tablolar sunulur, çevrim yapılmaz',
            'D': 'Çevrim yapılır ancak doğan farklar kâr veya zarara yansıtılır',
            'E': 'Varlık, borç, gelir ve giderler dâhil tüm kalemler işlem tarihlerindeki tarihî kurlarla çevrilir',
        },
        'A',
        "TMS 21 par. 38-39: bir işletme finansal tablolarını herhangi bir para biriminde sunabilir; raporlama para birimi geçerli para biriminden farklıysa sonuçlar ve finansal durum par. 39'daki yönteme göre çevrilir ve doğan farklar diğer kapsamlı gelire alınır.",
    ),
    'std-tms21-gen-0038': std_patch(
        'Yüksek enflasyonlu bir ekonomideki yurtdışı işletmenin çevrimi bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Doğrudan kapanış kuruyla çevrilir, yeniden düzenleme yapılmaz',
            'B': "Tablolar önce TMS 29'a göre yeniden düzenlenir, sonra kapanış kuruyla çevrilir",
            'C': 'Doğrudan dönemin ortalama kuruyla çevrilir',
            'D': 'Yalnızca parasal kalemler yeniden düzenlenir',
            'E': 'Çevrim yapılmaz, tablolar yerel para biriminde sunulur',
        },
        'B',
        'TMS 21 par. 42-43: geçerli para birimi yüksek enflasyonlu bir ekonominin para birimi olan işletmenin tabloları önce TMS 29 uyarınca yeniden düzenlenir; ardından tüm tutarlar en güncel finansal durum tablosu tarihindeki kapanış kuruyla çevrilir.',
    ),
    'std-tms21-gen-0039': std_patch(
        "Aşağıdakilerden hangisi TMS 21'e göre kur farkının kâr veya zarar DIŞINDA muhasebeleştirildiği durumdur?",
        {
            'A': 'Yabancı para satıcı borcunun dönem sonunda çevrilmesi',
            'B': 'Yabancı para ticari alacağın vadesinde tahsil edilmesi',
            'C': 'Raporlama para birimine çevrimden doğan kur farkları',
            'D': 'Yabancı para banka kredisinin kapanış kuruyla ölçülmesi',
            'E': 'Yabancı para kasa mevcudunun dönem sonu değerlemesi',
        },
        'C',
        'TMS 21 par. 39(c): geçerli para biriminden farklı bir raporlama para birimine çevrimde doğan tüm kur farkları diğer kapsamlı gelirde muhasebeleştirilir. Diğer şıklardaki olağan parasal kalem hareketleri par. 28 uyarınca kâr veya zarara yansıtılır.',
    ),
    'std-tms21-gen-0041': std_patch(
        'Bir işletme yabancı para cinsinden borcunu vadesinde ödemiştir ve ödeme tarihindeki kur, borcun kaydedildiği kurdan yüksektir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Aradaki fark kur farkı geliri olarak kaydedilir',
            'B': 'Aradaki fark diğer kapsamlı gelirde muhasebeleştirilir',
            'C': 'Aradaki fark ödeme tarihinde kur farkı gideri olarak kâr veya zarara yansıtılır',
            'D': 'Aradaki fark ilgili varlığın maliyetine eklenir',
            'E': 'Aradaki fark kaydedilmez, yalnızca dipnotta açıklanır',
        },
        'C',
        'TMS 21 par. 28: parasal kalemin ödenmesinden doğan kur farkı, oluştuğu dönemin kâr veya zararında muhasebeleştirilir. Borçta kurun yükselmesi daha fazla ödeme demektir; bu nedenle fark kur farkı giderdir.',
    ),
    'std-tms21-gen-0043': std_patch(
        "TMS 21'in kapsamı bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Standart istisnasız tüm yabancı para işlemlere uygulanır',
            'B': 'Standart yalnızca yurtdışında faaliyeti olan işletmelere uygulanır',
            'C': 'TFRS 9 kapsamındaki türev işlem ve bakiyeler ile riskten korunma muhasebesi kapsam dışıdır',
            'D': 'Standart yalnızca nakit işlemlere uygulanır',
            'E': 'TFRS 9 kapsamındaki türev işlemler de dâhil olmak üzere tüm yabancı para kalemler kapsamdadır',
        },
        'C',
        'TMS 21 par. 3: standart, TFRS 9 kapsamındaki türev işlem ve bakiyelere ve yabancı para kalemlerine ilişkin riskten korunma muhasebesine uygulanmaz. Bunun dışındaki yabancı para işlemler ile yurtdışı işletme çevrimi kapsamdadır.',
    ),
    'std-tms21-gen-0044': std_patch(
        "Aşağıdakilerden hangisi TMS 21'e göre kapanış kuruyla çevrilmez?",
        {
            'A': 'Yabancı para ticari alacaklar',
            'B': 'Yabancı para satıcı borçları',
            'C': 'Yabancı para vadesiz mevduat',
            'D': 'Tarihî maliyetiyle ölçülen yabancı para stoklar',
            'E': 'Yabancı para banka kredisi',
        },
        'D',
        'TMS 21 par. 23(a): kapanış kuruyla çevrilenler parasal kalemlerdir. Tarihî maliyetle ölçülen stoklar parasal olmayan kalem olduğundan par. 23(b) uyarınca işlem tarihindeki kurla çevrilir ve dönem sonunda yeniden çevrilmez.',
    ),
    'std-tms21-gen-0048': std_patch(
        'Aynı yabancı para tutarında hem alacağı hem borcu bulunan bir işletmede dönem sonu değerlemesi bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Alacak ve borç netleştirilerek tek bir tutar üzerinden çevrilir',
            'B': 'Yalnızca alacak kapanış kuruyla çevrilir; borç ilk kayıt tutarında bırakıldığı için kur farkı doğurmaz',
            'C': 'Kur farkları netleştirilip tek kalemde özkaynağa alınır',
            'D': 'İkisi de kapanış kuruyla çevrilir; kur farkı geliri ile gideri ayrı ayrı gösterilir',
            'E': 'Tutarlar eşit olduğundan çevrim yapılmasına gerek görülmez',
        },
        'D',
        'TMS 21 par. 23(a) her parasal kalemin kapanış kuruyla çevrilmesini öngörür; TMS 1 par. 32 ise netleştirmeyi yasaklar. Alacaktan doğan gelir ile borçtan doğan gider brüt olarak gösterilir; tutarların eşitliği çevrim yükümlülüğünü ortadan kaldırmaz.',
    ),
    'std-tms21-gen-0049': std_patch(
        'Yabancı para cinsinden peşin ödenen sigorta primi bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Parasal kalemdir; kapanış kuruyla çevrilir ve kur farkı doğar',
            'B': 'Parasal olmayan kalemdir; işlem tarihi kuruyla çevrilir ve kur farkı doğmaz',
            'C': 'Parasal kalemdir; ancak kur farkı özkaynağa alınır',
            'D': 'Parasal olmayan kalemdir; yine de kapanış kuruyla çevrilir',
            'E': 'Kayda alınmaz, doğrudan dönem gideri yazılır',
        },
        'B',
        'TMS 21 par. 16: peşin ödenmiş giderler para alma hakkı değil mal veya hizmet alma hakkı verdiğinden parasal olmayan kalemdir. Par. 23(b) uyarınca işlem tarihindeki kurla çevrilir ve dönem sonunda yeniden çevrilmediği için kur farkı doğmaz.',
    ),
    'std-tms21-gen-0050': std_patch(
        'Yabancı para cinsinden alınan ve henüz mal teslim edilmemiş sipariş avansı bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Parasal kalemdir; kapanış kuruyla çevrilir',
            'B': 'Parasal kalemdir; kur farkı özkaynağa alınır',
            'C': 'Parasal olmayan kalemdir; ancak kapanış kuruyla çevrilir',
            'D': 'Parasal olmayan kalemdir; işlem tarihi kuruyla ölçülür',
            'E': 'Avans hasılat olarak kaydedilir ve kur farkı doğmaz',
        },
        'D',
        'Alınan sipariş avansı, para geri ödeme yükümlülüğü değil mal teslim yükümlülüğü doğurur; bu nedenle TMS 21 par. 16 uyarınca parasal olmayan kalemdir ve par. 23(b) gereği işlem tarihindeki kurla ölçülüp dönem sonunda yeniden çevrilmez.',
    ),
    'std-tms21-gen-0053': std_patch(
        'Bir işletmenin geçerli para birimi ile raporlama para birimi aynıdır. TMS 21 bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tablo çevrimi gerekmez; yalnızca yabancı para işlemler için kur uygulanır',
            'B': 'Tüm kalemler için raporlama para birimine çevrim yapılır',
            'C': 'Tüm kalemler kapanış kuruyla yeniden çevrilir',
            'D': 'İşletme finansal tablo düzenlemekten muaf tutulur',
            'E': 'Çevrim farkları diğer kapsamlı gelirde gösterilir',
        },
        'A',
        'TMS 21 par. 39 yalnızca raporlama para biriminin geçerli para biriminden FARKLI olduğu durumda uygulanır. İkisi aynıysa tablo çevrimi gündeme gelmez; yabancı para işlemler için par. 21-23 hükümleri uygulanmaya devam eder.',
    ),
    'std-tms21-gen-0054': std_patch(
        'Yabancı para işlemin kaydedileceği tarih bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Fatura düzenlenme tarihi esas alınır; muhasebeleştirme koşullarının sağlandığı tarih dikkate alınmaz',
            'B': "İşlemin TMS'lere göre muhasebeleştirilme koşullarının sağlandığı tarih esas alınır",
            'C': 'Ödemenin fiilen yapıldığı tarih esas alınır',
            'D': 'Sözleşmenin imzalandığı tarih esas alınır',
            'E': 'Malın gümrükten çekildiği tarih esas alınır',
        },
        'B',
        "TMS 21 par. 22: işlem tarihi, işlemin TFRS'lere göre muhasebeleştirilme koşullarının ilk kez sağlandığı tarihtir. Fatura, sözleşme veya ödeme tarihi bu ölçütün yerine geçmez.",
    ),
    'std-tms21-gen-0056': std_patch(
        'Yabancı para cinsinden yeniden değerleme modeliyle ölçülen arsa bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Gerçeğe uygun değerin belirlendiği tarihteki kurla çevrilir; kur bileşeni değerleme farkını izler',
            'B': 'İlk işlem tarihindeki tarihî kurla çevrilir; yeniden değerleme kur açısından dikkate alınmaz',
            'C': 'Kapanış kuruyla çevrilir ve kur farkı kâr veya zarara yazılır',
            'D': 'Arsa parasal kalem sayıldığından kapanış kuruyla çevrilir',
            'E': 'Çevrilmez, ilk kayıt tutarında bırakılır',
        },
        'A',
        'TMS 21 par. 23(c): gerçeğe uygun değeriyle ölçülen parasal olmayan kalem, değerin belirlendiği tarihteki kurla çevrilir. Par. 30 uyarınca yeniden değerleme farkı diğer kapsamlı gelirde muhasebeleştirildiğinden kur bileşeni de aynı yeri izler.',
    ),
    'std-tms21-gen-0058': std_patch(
        'Kur farkının ilgili varlığın maliyetine eklenmesi bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tüm yabancı para kredilerin kur farkı varlık maliyetine eklenir',
            'B': 'TMS 21 böyle bir uygulamaya izin vermez; kur farkı kâr veya zarara yansıtılır',
            'C': 'Yabancı para kredi ile alınan duran varlığın kur farkı, varlığın maliyetine eklenerek aktifleştirilir',
            'D': 'Kur farkı işletmenin tercihine göre aktifleştirilebilir',
            'E': 'Kur farkı yalnızca stoklar için aktifleştirilir',
        },
        'B',
        "TMS 21 par. 28 kur farklarının kâr veya zararda muhasebeleştirilmesini öngörür ve maliyete ekleme seçeneği tanımaz. Özellikli varlıklarda borçlanma maliyetlerinin aktifleştirilmesi TMS 23'ün konusudur ve faiz benzeri düzeltme ile sınırlıdır.",
    ),
    'std-tms21-gen-0060': std_patch(
        'Bir işletmenin yurtdışındaki bağlı ortaklığının geçerli para birimi ana ortaklığından farklıdır. Buna göre aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'Bağlı ortaklık, ana ortaklığın geçerli para birimini benimsemek durumundadır',
            'B': 'Bağlı ortaklığın tabloları konsolidasyon öncesinde raporlama para birimine çevrilir',
            'C': 'Varlık ve borçlar kapanış kuruyla, gelir ve giderler işlem tarihi kurlarıyla çevrilir',
            'D': 'Çevrimden doğan farklar diğer kapsamlı gelirde muhasebeleştirilir',
            'E': 'Bağlı ortaklığın elden çıkarılmasında biriken farklar kâr veya zarara sınıflandırılır',
        },
        'A',
        "TMS 21 par. 11 ve 39: her işletmenin geçerli para birimi kendi işlem koşullarına göre belirlenir; bağlı ortaklık ana ortaklığın para birimini benimsemek durumunda değildir. Konsolidasyonda tablolar par. 39'a göre çevrilir ve farklar diğer kapsamlı gelire alınır.",
    ),
}


def apply_or_check(path, patches, write):
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    by_id = {q["id"]: q for q in questions}
    mismatches = []
    for qid, fields in patches.items():
        q = by_id.get(qid)
        if q is None:
            raise SystemExit(f"Soru bulunamadi: {path}::{qid}")
        for field, expected in fields.items():
            if q.get(field) != expected:
                mismatches.append(f"{path}::{qid}.{field}")
                if write:
                    q[field] = expected
        if write:
            if len(set(q["options"].values())) != 5:
                raise SystemExit(f"Secenek cakismasi: {path}::{qid}")
            if q["answer"] not in q["options"]:
                raise SystemExit(f"Cevap secenekte yok: {path}::{qid}")
    if write:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return mismatches


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--write", action="store_true")
    args = ap.parse_args()
    mismatches = []
    for path in (ROOT / RELATIVE_PATH, APP_ROOT / RELATIVE_PATH):
        mismatches.extend(apply_or_check(path, PATCHES, args.write))
    if args.check and mismatches:
        print("Eslesmeyen alanlar:")
        for m in mismatches:
            print(f"- {m}")
        return 1
    print(f"1 paket / {len(PATCHES)} soru (TMS 21 profil kalibrasyonu) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
