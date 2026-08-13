#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TMS 36 Varliklarda Deger Dusuklugu — bicim kalibrasyonu (kapsam zaten tam).

OLCULEN KUSURLAR (2026-08-13):
  · kokunde >=2 tutar **%0** ve sayisal-cevap %11 — oysa gercek sinav TMS 36'yi
    hesap sorusu olarak da soruyor. Arsivden olculen tipler:
      – 2026/2 s.44 NAKIT YARATAN BIRIM DAGITIMI (en guncel tip): serefiye
        200.000 + binalar 1.500.000 + demirbaslar 1.000.000, geri kazanilabilir
        tutar 2.250.000 -> "binalarin ve demirbaslarin degeri sirasiyla kac ₺"
      – 2023 / 2021: deger dusuklugu iptali ve ilave karsilik tutari
      – 2014-16 s.42: "satis maliyetleri dusulmus gercege uygun deger" tanimi
  · olumsuz kok **%5** — oysa KAPSAM sorusu olumsuz kokle UC KEZ sorulmus:
    1-2-3 s.53 "hangisine uygulanmaz", 2025 s.53 "testine tabi tutulanlardan
    biri degildir", 2025 s.50 "hangi varlik kapsami disindadir". Ayrica
    2016-18 s.41 "kullanim degerinin hesaplanmasinda hangisi dikkate alinmaz".
  · kok kalibi **43/60 ayni** (§2 ihlali) · para birimi TL (7 soru, §8) · kor %26

Bu tur icerik degil BICIM duzeltir; kapsam ve dogruluk korunur.

⚠️ §5 BOY TUZAGI — TASARIM ZAMANI DENETIMI: bu paketin yamalari once ayri bir
tasarim modulunde yazildi ve dogru sikkin "tek-en-uzun" olma orani URETIMDEN
ONCE olculdu. Ilk tasarimda 19/28 (%68) cikti ve uretim durduruldu; sonra
celdiricilere gercek icerik (yanlis iddianin kendi sonucu) eklenerek 2/28'e (%7)
indirildi. Dogru sikkin boy sirasi dagilimi: en uzun 5 · 2. 14 · 3. 4 · 4. 3 ·
en kisa 2. Ayni kontrol tms_2 / tms_16 / diger_guncel turlarinda URETIMDEN SONRA
yapilmis ve her seferinde yeniden calisma gerektirmisti.

§6 notu: her yamanin dogru cevap HARFI mevcut JSON'daki harfle ayni birakildi;
boylece paketin harf dagilimi {A:11, B:13, C:12, D:12, E:12} ve "ardisik uc ayni
harf yok" ozelligi degismeden korunur.

Dayanak: KGK TMS 36 par. 2, 4, 6, 10, 18, 22, 25-28, 30-33, 44, 49-50, 59-63,
80-90, 96, 100-105, 110-117, 124, 126.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/tms_36_deger_dusuklugu.json"
STYLE_REF = "SGS Muhasebe Standartlari TMS 36"

# §8: "₺ sembolu kullanilir". Bu pakette 7 soru TL kullaniyordu; yamalananlar
# zaten ₺ ile yazildi, yamalanmayanlar burada mekanik olarak cevrilir.
TL = re.compile(r"(\d)\s*TL\b")


def std_patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": "TMS 36 Varliklarda Deger Dusuklugu"},
        "validYear": 2026, "mockExamId": None,
    }


PATCHES = {
    'std-tms36-gen-0003': std_patch(
        "TMS 36'ya göre bir varlığın geri kazanılabilir tutarı nasıl belirlenir?",
        {
            'A': 'Satış maliyeti düşülmüş gerçeğe uygun değeri ile kullanım değerinden yüksek olanı',
            'B': 'Her zaman satış maliyeti düşülmüş gerçeğe uygun değeri; kullanım değeri hesaplanmaz',
            'C': 'Her zaman kullanım değeri; satış olanağı bulunsa bile bu ölçüm esas alınır',
            'D': 'Satış maliyeti düşülmüş gerçeğe uygun değeri ile kullanım değerinden düşük olanı',
            'E': 'Defter değeri ile kullanım değerinden düşük olanı',
        },
        'A',
        'TMS 36 par. 6 ve 18: geri kazanılabilir tutar, varlığın satış maliyetleri düşülmüş gerçeğe uygun değeri ile kullanım değerinden yüksek olanıdır. İkisinden biri defter değerini aşıyorsa değer düşüklüğü yoktur ve diğerini hesaplamaya gerek kalmaz.',
    ),
    'std-tms36-gen-0004': std_patch(
        "TMS 36'ya göre kullanım değeri neyi ifade eder?",
        {
            'A': 'Varlığın raporlama tarihinde piyasada satılabileceği cari fiyatı',
            'B': 'Varlığın aynı nitelikte bir varlıkla yerine konma (ikame) maliyetini',
            'C': 'Varlığın defter değeri ile gerçeğe uygun değeri arasındaki farkı',
            'D': 'Varlığın sigorta poliçesinde yer alan teminat bedelini',
            'E': 'Varlıktan beklenen gelecekteki nakit akışlarının bugünkü değerini',
        },
        'E',
        'TMS 36 par. 6: kullanım değeri, bir varlık veya nakit yaratan birimden elde edilmesi beklenen gelecekteki nakit akışlarının bugünkü değeridir. Piyasa fiyatı değil işletmeye özgü bir ölçümdür.',
    ),
    'std-tms36-gen-0005': std_patch(
        "TMS 36'ya göre nakit yaratan birim ne zaman gündeme gelir?",
        {
            'A': 'Bireysel bir varlık için geri kazanılabilir tutar tahmin edilemediğinde',
            'B': 'Varlık tamamen amorti edilip defter değeri sıfıra indiğinde',
            'C': 'Varlığın defter değeri güvenilir biçimde belirlenemediğinde',
            'D': 'Varlık satış amaçlı elde tutulan duran varlık olarak sınıflandırıldığında',
            'E': 'İşletme birleşmesi gerçekleşip şerefiye muhasebeleştirildiğinde',
        },
        'A',
        'TMS 36 par. 22 ve 66: bireysel bir varlık için geri kazanılabilir tutar tahmin edilemiyorsa — yani varlık diğer varlıklardan büyük ölçüde bağımsız nakit girişi sağlamıyorsa — varlığın ait olduğu nakit yaratan birimin geri kazanılabilir tutarı belirlenir.',
    ),
    'std-tms36-gen-0007': std_patch(
        "Aşağıdakilerden hangisi TMS 36'ya göre değer düşüklüğü belirtisi aranmaksızın her yıl teste tabi tutulmaz?",
        {
            'A': 'Faydalı ömrü sınırsız olan ve itfaya tabi tutulmayan maddi olmayan duran varlık',
            'B': 'Henüz kullanıma hazır olmayan maddi olmayan duran varlık',
            'C': 'Sınırsız ömürlü olarak değerlendirilen tescilli marka hakkı',
            'D': 'Faydalı ömrü sınırlı olan ve itfaya tabi maddi olmayan duran varlık',
            'E': 'İşletme birleşmesinde edinilen ve nakit yaratan birimlere dağıtılan şerefiye',
        },
        'D',
        'TMS 36 par. 10: şerefiye, sınırsız faydalı ömürlü maddi olmayan duran varlıklar ve henüz kullanıma hazır olmayan maddi olmayan duran varlıklar belirti aranmaksızın yılda en az bir kez teste tabidir. Sınırlı ömürlü ve itfa edilen varlıklar ise yalnızca belirti bulunduğunda test edilir.',
    ),
    'std-tms36-gen-0011': std_patch(
        'Maliyet modeliyle izlenen bir varlıkta değer düşüklüğü zararı nereye yansıtılır?',
        {
            'A': 'Gelecek dönemlere yayılarak eşit taksitlerle',
            'B': 'Doğrudan geçmiş yıllar kârlarına',
            'C': 'İlgili varlığın maliyetine eklenerek kalan faydalı ömre yayılır',
            'D': 'Doğrudan dönemin kâr veya zararına',
            'E': 'Diğer kapsamlı gelire; varlık maliyet modeliyle izlense de bu kural uygulanır',
        },
        'D',
        "TMS 36 par. 60: değer düşüklüğü zararı, varlık yeniden değerlenmiş tutarıyla izlenmiyorsa doğrudan kâr veya zararda muhasebeleştirilir. Yeniden değerlenmiş varlıklarda par. 61'deki sıra uygulanır.",
    ),
    'std-tms36-gen-0015': std_patch(
        "Bir makinenin defter değeri 500.000 ₺'dir. Gerçeğe uygun değerinden satış maliyetleri düşülmüş tutarı 430.000 ₺, kullanım değeri ise 465.000 ₺ olarak hesaplanmıştır. TMS 36'ya göre muhasebeleştirilecek değer düşüklüğü zararı kaç ₺'dir?",
        {
            'A': '105.000 ₺',
            'B': '70.000 ₺',
            'C': '0 ₺',
            'D': '465.000 ₺',
            'E': '35.000 ₺',
        },
        'E',
        "TMS 36 par. 6 ve 18: geri kazanılabilir tutar, satış maliyeti düşülmüş gerçeğe uygun değer ile kullanım değerinin YÜKSEK olanıdır: max(430.000; 465.000) = 465.000 ₺. Defter değeri bunun üzerinde olduğundan değer düşüklüğü 500.000 − 465.000 = 35.000 ₺'dir.",
    ),
    'std-tms36-gen-0016': std_patch(
        "Yeniden değerleme modeliyle izlenen bir binanın defter değeri 700.000 ₺, bu binaya ilişkin özkaynakta biriken yeniden değerleme fazlası 90.000 ₺'dir. Binanın geri kazanılabilir tutarı 580.000 ₺ olarak belirlenmiştir. TMS 36'ya göre 120.000 ₺'lik değer düşüklüğü zararı nasıl muhasebeleştirilir?",
        {
            'A': '90.000 ₺ diğer kapsamlı gelirde fazlayı azaltır, kalan 30.000 ₺ kâr veya zarara yazılır',
            'B': 'Tamamı diğer kapsamlı gelirde fazlayı azaltır; aşan 30.000 ₺ sonraki döneme devreder',
            'C': '30.000 ₺ diğer kapsamlı gelirde fazlayı azaltır, kalan 90.000 ₺ kâr veya zarara yazılır',
            'D': 'Tamamı doğrudan geçmiş yıllar kârlarından indirilir',
            'E': 'Tamamı kâr veya zarara yazılır; özkaynaktaki yeniden değerleme fazlası olduğu gibi korunur',
        },
        'A',
        'TMS 36 par. 60-61: yeniden değerlenmiş varlıkta değer düşüklüğü zararı, o varlığa ilişkin yeniden değerleme fazlası bulunduğu ölçüde diğer kapsamlı gelirde muhasebeleştirilerek fazlayı azaltır. Fazlayı aşan kısım kâr veya zarara yansıtılır: 90.000 ₺ + 30.000 ₺.',
    ),
    'std-tms36-gen-0017': std_patch(
        "Bir makinenin defter değeri 480.000 ₺, gerçeğe uygun değerinden satış maliyetleri düşülmüş tutarı 455.000 ₺ ve kullanım değeri 495.000 ₺'dir. TMS 36'ya göre yapılacak işlem aşağıdakilerden hangisidir?",
        {
            'A': 'Varlık 495.000 ₺ ile ölçülür ve 15.000 ₺ fark diğer kapsamlı gelire alınır',
            'B': "25.000 ₺ değer düşüklüğü zararı kaydedilir ve varlık 455.000 ₺'ye indirilir",
            'C': 'Varlık iki ölçümün ortalaması olan 475.000 ₺ ile ölçülür ve 5.000 ₺ zarar yazılır',
            'D': 'Değer düşüklüğü kaydı yapılmaz; varlık 480.000 ₺ ile taşınmaya devam eder',
            'E': "15.000 ₺ değer artışı kaydedilerek varlık 495.000 ₺'ye yükseltilir",
        },
        'D',
        'Geri kazanılabilir tutar iki ölçümün yükseğidir: max(455.000; 495.000) = 495.000 ₺. Bu tutar defter değerinin üzerinde olduğundan TMS 36 par. 59 uyarınca değer düşüklüğü yoktur. Standart değer artışı kaydına da izin vermez; varlık defter değeriyle taşınır.',
    ),
    'std-tms36-gen-0018': std_patch(
        "Aşağıdakilerden hangisi TMS 36'ya göre kullanım değerinin hesaplanmasında dikkate alınmaz?",
        {
            'A': 'Varlığın kullanımından beklenen gelecekteki nakit girişleri',
            'B': 'Henüz taahhüt edilmemiş bir yeniden yapılandırmadan beklenen nakit tasarrufları',
            'C': 'Varlığın faydalı ömrünün sonunda elden çıkarılmasından beklenen net nakit akışları',
            'D': 'Nakit akışlarının tutar ve zamanlamasındaki olası değişkenlik beklentileri',
            'E': 'Paranın zaman değerini yansıtan cari piyasa faiz oranı',
        },
        'B',
        'TMS 36 par. 30 ve 44: kullanım değeri; beklenen nakit akışları, bu akışlardaki değişkenlik beklentisi, paranın zaman değeri ve belirsizlik primi gibi unsurları yansıtır. Ancak henüz taahhüt edilmemiş bir yeniden yapılandırmadan ya da varlığın performansını artıracak henüz yapılmamış iyileştirmelerden doğacak nakit akışları hesaba katılmaz.',
    ),
    'std-tms36-gen-0021': std_patch(
        "Aşağıdakilerden hangisi TMS 36'ya göre kullanım değeri hesabındaki nakit akışı tahminlerine dâhil edilir?",
        {
            'A': 'Gelir vergisi ödemeleri ve iadeleri',
            'B': 'Finansman faaliyetlerinden doğan nakit çıkışları',
            'C': 'Varlığın günlük bakımına ilişkin olağan nakit çıkışları',
            'D': 'Varlığın performansını artıracak henüz yapılmamış iyileştirme harcamaları',
            'E': 'Henüz taahhüt edilmemiş yeniden yapılandırma çıkışları',
        },
        'C',
        'TMS 36 par. 50: kullanım değeri hesabında finansman faaliyetlerinden kaynaklanan nakit akışları ile gelir vergisi tahsilat ve ödemeleri dikkate alınmaz. Varlığın mevcut performansını sürdürmek için gereken olağan bakım çıkışları ise par. 49 uyarınca hesaba dâhildir.',
    ),
    'std-tms36-gen-0023': std_patch(
        "Defter değeri 900.000 ₺, kalan faydalı ömrü 6 yıl ve kalıntı değeri bulunmayan bir makinenin geri kazanılabilir tutarı 600.000 ₺ olarak belirlenmiş ve değer düşüklüğü muhasebeleştirilmiştir. TMS 36'ya göre izleyen yılın amortisman gideri kaç ₺'dir?",
        {
            'A': '300.000 ₺',
            'B': '120.000 ₺',
            'C': '150.000 ₺',
            'D': '100.000 ₺',
            'E': '50.000 ₺',
        },
        'D',
        "Değer düşüklüğü sonrası defter değeri 600.000 ₺'dir. TMS 36 par. 63: değer düşüklüğü zararının muhasebeleştirilmesinden sonra amortisman, düzeltilmiş defter değerinin kalan faydalı ömre sistematik dağıtılmasıyla hesaplanır: 600.000 / 6 = 100.000 ₺.",
    ),
    'std-tms36-gen-0026': std_patch(
        'Bir nakit yaratan birimde dağıtılan değer düşüklüğü zararı, birimdeki tek tek varlıkların defter değerini hangi tutarın altına indiremez?',
        {
            'A': 'Birimdeki varlık sayısına bölünerek bulunan eşit dağıtım payı tutarı',
            'B': 'Varlığın vergi mevzuatı uyarınca belirlenen değerlenmiş tutarı',
            'C': 'Varlığın satış maliyeti düşülmüş gerçeğe uygun değeri, kullanım değeri ve sıfırdan en yükseği',
            'D': 'Varlığın birikmiş amortisman ve itfa payları düşülmemiş brüt kayıtlı değeri',
            'E': 'Varlığın işletme birleşmesindeki ilk muhasebeleştirme tarihindeki maliyet bedeli',
        },
        'C',
        'TMS 36 par. 105: bir varlığın defter değeri; satış maliyeti düşülmüş gerçeğe uygun değeri (belirlenebiliyorsa), kullanım değeri (belirlenebiliyorsa) ve sıfır tutarlarının en yükseğinin altına indirilemez. Dağıtılamayan zarar birimdeki diğer varlıklara oransal olarak paylaştırılır.',
    ),
    'std-tms36-gen-0027': std_patch(
        "Bir nakit yaratan birimin defter değeri 3.000.000 ₺ olup bunun 300.000 ₺'si şerefiye, 1.800.000 ₺'si binalar ve 900.000 ₺'si makinelerden oluşmaktadır. Yapılan değerlendirmede birimin geri kazanılabilir tutarı 2.400.000 ₺ olarak tahmin edilmiştir. TMS 36'ya göre binaların ve makinelerin değer düşüklüğü sonrası defter değerleri sırasıyla kaç ₺'dir?",
        {
            'A': '1.440.000 ₺ ve 720.000 ₺',
            'B': '1.600.000 ₺ ve 800.000 ₺',
            'C': '1.800.000 ₺ ve 900.000 ₺',
            'D': '1.500.000 ₺ ve 900.000 ₺',
            'E': '1.680.000 ₺ ve 840.000 ₺',
        },
        'B',
        "Toplam değer düşüklüğü: 3.000.000 − 2.400.000 = 600.000 ₺. TMS 36 par. 104 sırayı belirler: önce şerefiyenin defter değeri silinir (300.000 ₺). Kalan 300.000 ₺, diğer varlıklara defter değerleri oranında dağıtılır. Binalar 1.800.000 / 2.700.000 = 2/3 payla 200.000 ₺, makineler 1/3 payla 100.000 ₺ pay alır. Yeni defter değerleri 1.800.000 − 200.000 = 1.600.000 ₺ ve 900.000 − 100.000 = 800.000 ₺'dir.",
    ),
    'std-tms36-gen-0028': std_patch(
        'Şerefiye değer düşüklüğü testine nasıl tabi tutulur?',
        {
            'A': 'Yalnızca edinim yılında',
            'B': 'Tek başına ve bireysel varlık olarak',
            'C': 'Faaliyet bölümleri toplulaştırılmadan, her varlık için ayrı ayrı',
            'D': 'Dağıtıldığı nakit yaratan birim ya da birim grubu düzeyinde',
            'E': 'İşletmenin tamamı düzeyinde ve yalnızca satış hâlinde',
        },
        'D',
        'TMS 36 par. 80-90: şerefiye tek başına nakit girişi sağlamadığından bireysel test edilemez; birleşmenin sinerjisinden yararlanması beklenen nakit yaratan birime ya da birim grubuna dağıtılır ve test o düzeyde yapılır.',
    ),
    'std-tms36-gen-0031': std_patch(
        'Şerefiye dışındaki bir varlıkta değer düşüklüğü zararının iptali hangi koşulda yapılır?',
        {
            'A': 'Yalnızca varlık satıldığında veya başka bir yolla elden çıkarıldığında',
            'B': 'Geri kazanılabilir tutarın tahmininde kullanılan varsayımlar değiştiğinde',
            'C': 'Her raporlama döneminde ayrıca belirti aranmaksızın otomatik olarak',
            'D': 'Yalnızca işletme kâra geçtiğinde ve dağıtılabilir kâr oluştuğunda',
            'E': 'Yalnızca varlığın faydalı ömrü uzatıldığında ve amortisman planı değiştiğinde',
        },
        'B',
        'TMS 36 par. 110-114: her raporlama döneminde önceki zararın azalmış ya da ortadan kalkmış olabileceğine ilişkin belirti aranır. Belirti varsa geri kazanılabilir tutar yeniden tahmin edilir; tahminlerde değişiklik olmuşsa iptal muhasebeleştirilir.',
    ),
    'std-tms36-gen-0032': std_patch(
        "Aşağıdakilerden hangisi TMS 36'ya göre yanlıştır?",
        {
            'A': 'İptal edilen tutar, geçmişte hiç değer düşüklüğü kaydedilmemiş olsaydı ulaşılacak defter değerini aşamaz',
            'B': 'Şerefiye dışındaki varlıklarda değer düşüklüğü zararı koşullar değişirse iptal edilebilir',
            'C': 'İptal, maliyet modelinde kâr veya zarara yansıtılır',
            'D': 'Şerefiye için muhasebeleştirilen değer düşüklüğü zararı, koşullar iyileşirse sonraki dönemde iptal edilir',
            'E': 'İptalden sonraki amortisman, düzeltilmiş defter değerinin kalan ömre dağıtılmasıyla bulunur',
        },
        'D',
        'TMS 36 par. 124: şerefiye için muhasebeleştirilen değer düşüklüğü zararı sonraki dönemlerde İPTAL EDİLEMEZ. Diğer varlıklarda ise par. 110-117 uyarınca koşullar değiştiğinde iptal mümkündür ve tavan, hiç zarar kaydedilmemiş olsaydı ulaşılacak defter değeridir.',
    ),
    'std-tms36-gen-0033': std_patch(
        'Değer düşüklüğü zararının iptalinde defter değeri hangi tutarı aşamaz?',
        {
            'A': 'Varlığın ilk muhasebeleştirilmesindeki maliyet bedelini; birikmiş amortisman dikkate alınmaz',
            'B': 'Varlığın raporlama tarihindeki cari gerçeğe uygun değerini',
            'C': 'Hiç değer düşüklüğü kaydedilmeseydi ulaşılacak amortismanlı defter değerini',
            'D': 'Geri kazanılabilir tutarı; bu tutar iptalde tavan olarak uygulanır',
            'E': 'Varlığın yeniden üretim maliyetini; amortisman düşülerek bulunan tutarı',
        },
        'C',
        'TMS 36 par. 117: iptal sonrası artırılan defter değeri, geçmiş yıllarda hiç değer düşüklüğü zararı muhasebeleştirilmemiş olsaydı belirlenecek olan (amortisman düşülmüş) defter değerini aşamaz.',
    ),
    'std-tms36-gen-0035': std_patch(
        "Maliyeti 800.000 ₺, faydalı ömrü 8 yıl ve kalıntı değeri bulunmayan bir makine doğrusal amortismana tabidir. İkinci yılın sonunda geri kazanılabilir tutarı 480.000 ₺'ye düştüğü için değer düşüklüğü kaydedilmiştir. Dördüncü yılın sonunda koşullar iyileşmiş ve geri kazanılabilir tutar 500.000 ₺ olmuştur. TMS 36'ya göre iptal edilecek değer düşüklüğü kaç ₺'dir?",
        {
            'A': '100.000 ₺',
            'B': '180.000 ₺',
            'C': '80.000 ₺',
            'D': '120.000 ₺',
            'E': '20.000 ₺',
        },
        'C',
        "İkinci yıl sonu defter değeri 800.000 − 2×100.000 = 600.000 ₺; 480.000 ₺'ye indirgendi. Kalan 6 yıl için yıllık amortisman 480.000 / 6 = 80.000 ₺; dördüncü yıl sonu defter değeri 480.000 − 160.000 = 320.000 ₺. TMS 36 par. 117: iptal sonrası defter değeri, hiç değer düşüklüğü kaydedilmeseydi ulaşılacak tutarı aşamaz: 800.000 − 4×100.000 = 400.000 ₺. Geri kazanılabilir tutar 500.000 ₺ bunun üzerinde olduğundan tavan uygulanır ve iptal 400.000 − 320.000 = 80.000 ₺ olur.",
    ),
    'std-tms36-gen-0043': std_patch(
        'TMS 36 uyarınca değer düşüklüğüne ilişkin olarak aşağıdakilerden hangisi açıklanır?',
        {
            'A': 'Kâr veya zarara yansıtılan değer düşüklüğü ve iptal tutarları ile sunuldukları kalemler',
            'B': 'Yalnızca değer düşüklüğü kaydedilen varlıkların adedi ve amortisman süreleri',
            'C': 'Yalnızca kullanım değeri hesabında kullanılan iskonto oranının belirlenme yöntemi ve dayanağı',
            'D': 'Yalnızca değer düşüklüğüne uğrayan varlıkların sigorta poliçesindeki bedelleri',
            'E': 'Yalnızca değer düşüklüğüne uğrayan varlıkların ilk maliyet bedelleri',
        },
        'A',
        'TMS 36 par. 126: her varlık sınıfı için dönemde kâr veya zarara yansıtılan değer düşüklüğü zararları ile iptal tutarları ve bunların kapsamlı gelir tablosunda hangi kalemde sunulduğu açıklanır. Diğer kapsamlı gelirde muhasebeleştirilen tutarlar da ayrıca belirtilir.',
    ),
    'std-tms36-gen-0044': std_patch(
        'Aşağıdakilerden hangisi TMS 36 Varlıklarda Değer Düşüklüğü standardının kapsamı dışındadır?',
        {
            'A': 'Sınırsız ömürlü tescilli marka hakkı',
            'B': 'Özkaynak yöntemiyle izlenen iştirak yatırımı',
            'C': 'İşletme birleşmesinde edinilen şerefiye',
            'D': 'Üretimde kullanılan makine ve tesisler',
            'E': 'Satılmak üzere elde tutulan stoklar',
        },
        'E',
        "TMS 36 par. 2: standart stoklara, inşaat sözleşmelerinden doğan varlıklara, ertelenmiş vergi varlıklarına, çalışanlara sağlanan fayda varlıklarına, TFRS 9 kapsamındaki finansal varlıklara, gerçeğe uygun değerle ölçülen yatırım amaçlı gayrimenkullere ve TFRS 5 kapsamındaki satış amaçlı varlıklara uygulanmaz. Stokların değer düşüklüğü TMS 2'ye tabidir.",
    ),
    'std-tms36-gen-0047': std_patch(
        'Satış maliyeti düşülmüş gerçeğe uygun değer en güvenilir biçimde neye dayanılarak belirlenir?',
        {
            'A': 'Varlığın vergi mevzuatı uyarınca belirlenen değerlenmiş tutarına',
            'B': 'İşletme yönetiminin varlığa ilişkin gelecek dönem satış beklentilerine',
            'C': 'Varlığın sigorta poliçesinde yer alan teminat bedeline',
            'D': 'Benzer nitelikteki varlıkların muhasebe kayıtlarındaki ilk maliyet bedellerine',
            'E': 'Aktif bir piyasada oluşan bağlayıcı satış sözleşmesi veya piyasa fiyatına',
        },
        'E',
        'TMS 36 par. 25-27: en güvenilir kanıt, karşılıklı pazarlık ortamında düzenlenmiş bağlayıcı satış sözleşmesi fiyatıdır. Böyle bir sözleşme yoksa aktif piyasadaki cari alış fiyatı, o da yoksa benzer işlemlere dayanan en iyi tahmin kullanılır.',
    ),
    'std-tms36-gen-0048': std_patch(
        "Aşağıdakilerden hangisi TMS 36'ya göre satış (elden çıkarma) maliyeti sayılmaz?",
        {
            'A': 'Elden çıkarmaya ilişkin hukuki danışmanlık giderleri',
            'B': 'Satışa konu varlığın taşınması ve teslimine ilişkin doğrudan maliyetler',
            'C': 'Varlığın elden çıkarılmasından doğacak gelir vergisi yükü',
            'D': 'Varlığın satışına aracılık eden kuruma ödenecek komisyon',
            'E': 'Satış işlemine ilişkin damga vergisi ve benzeri işlem vergileri',
        },
        'C',
        'TMS 36 par. 28: satış maliyetleri; hukuki giderler, damga vergisi ve benzeri işlem vergileri, varlığın elden çıkarılmasına doğrudan atfedilebilen taşıma ve teslim maliyetleri ile komisyonlardan oluşur. Finansman giderleri ve gelir vergisi gideri bu kapsamda değildir.',
    ),
    'std-tms36-gen-0049': std_patch(
        'Kullanım değeri hesabında nakit akışı projeksiyonları en fazla kaç yıllık dönemi kapsar?',
        {
            'A': 'Yalnızca izleyen bir yıl; sonrası için büyüme oranı kullanılır',
            'B': 'Genel olarak beş yıl; daha uzunu gerekçelendirilebiliyorsa kullanılır',
            'C': 'En fazla on yıl; bu süre sektör koşullarına göre uzatılabilir',
            'D': 'Varlığın kalan faydalı ömrünün tamamı; standart bir üst sınır öngörmez',
            'E': 'En fazla üç yıl; daha uzun dönem için ayrıca kurul onayı alınır',
        },
        'B',
        'TMS 36 par. 33(b): nakit akışı projeksiyonları en fazla beş yıllık en son bütçe ve tahminlere dayanır. Daha uzun bir dönem, işletme bunu haklı gösterebiliyorsa kullanılabilir.',
    ),
    'std-tms36-gen-0050': std_patch(
        'Beş yılı aşan dönemler için nakit akışı tahminleri nasıl belirlenir?',
        {
            'A': 'İçinde bulunulan sektörün ortalama büyüme oranı doğrudan uygulanır',
            'B': 'Her yıl için ayrı ayrı ayrıntılı bütçe hazırlanır ve beş yıl sınırı uygulanmaz',
            'C': 'Tahmin yapılmaz; kullanım değeri hesabı beşinci yılın sonunda kesilir',
            'D': 'Beşinci yılın nakit akışı tutarı sabit tutulur ve büyüme oranı uygulanmaz',
            'E': 'Sabit ya da azalan bir büyüme oranıyla dışa yansıtılır',
        },
        'E',
        'TMS 36 par. 33(c): beş yılı aşan dönemler, sabit ya da azalan bir büyüme oranı kullanılarak dışa yansıtılır. Artan bir oran, ancak objektif bilgilerle desteklenebiliyorsa kullanılabilir; oran ürün, sektör veya ülkenin uzun dönemli ortalama büyüme oranını aşmamalıdır.',
    ),
    'std-tms36-gen-0051': std_patch(
        "TMS 36'ya göre ortak varlıklar neyi anlatır?",
        {
            'A': 'Şerefiye dışında kalan ve birden fazla nakit yaratan birime katkı sağlayan varlıkları',
            'B': 'İşletme birleşmesinde edinilen ve şerefiye dâhil tüm varlıkları',
            'C': 'Ortaklar tarafından sermaye taahhüdü karşılığında işletmeye devredilen ve özkaynakta izlenen varlıkları',
            'D': 'Finansal kiralama yoluyla edinilmiş kullanım hakkı varlıklarını',
            'E': 'İki veya daha çok işletmenin müşterek mülkiyetinde bulunan varlıkları',
        },
        'A',
        'TMS 36 par. 100-102: ortak varlıklar, şerefiye dışında kalan ve hem incelenen nakit yaratan birimin hem de diğer birimlerin gelecekteki nakit akışlarına katkıda bulunan varlıklardır (genel merkez binası, bilgi işlem donanımı gibi). Tek başına nakit girişi sağlamadıkları için makul ve tutarlı bir esasla birimlere dağıtılır.',
    ),
    'std-tms36-gen-0053': std_patch(
        'Sınırsız faydalı ömürlü bir maddi olmayan duran varlığın yıllık değer düşüklüğü testi ne zaman yapılabilir?',
        {
            'A': 'Yıl içinde herhangi bir tarihte, her yıl aynı zamanda olmak koşuluyla',
            'B': 'Yalnızca bağımsız denetimin tamamlandığı tarihte',
            'C': 'Yalnızca varlığın edinildiği aya denk gelen tarihte',
            'D': 'Her çeyrek dönemde ayrı ayrı; yıllık tek test yeterli sayılmaz',
            'E': 'Yalnızca hesap dönemi sonunda; ara raporlama dönemlerinde test yapılamaz',
        },
        'A',
        'TMS 36 par. 10 ve 96: test yıl içinde herhangi bir zamanda yapılabilir; ancak her yıl aynı dönemde tekrarlanır. Farklı maddi olmayan duran varlıklar farklı tarihlerde test edilebilir.',
    ),
    'std-tms36-gen-0054': std_patch(
        'Şerefiyenin dağıtıldığı nakit yaratan birim veya birim grubu en fazla hangi büyüklükte olabilir?',
        {
            'A': 'Tek bir varlık büyüklüğünde; şerefiye bireysel olarak test edilir',
            'B': "TFRS 8'e göre belirlenen faaliyet bölümü büyüklüğünde",
            'C': 'Faaliyet gösterilen coğrafi ülke büyüklüğünde',
            'D': 'Yasal şirket tüzel kişiliği büyüklüğünde',
            'E': 'İşletmenin tamamı büyüklüğünde; alt kırılım yapılması gerekmez',
        },
        'B',
        'TMS 36 par. 80: şerefiyenin dağıtıldığı birim ya da birim grubu, işletmenin şerefiyeyi iç raporlamada izlediği en küçük düzeyi temsil eder ve TFRS 8 uyarınca belirlenen faaliyet bölümünden büyük olamaz.',
    ),
    'std-tms36-gen-0058': std_patch(
        "Bir varlıktan gelecek üç yıl boyunca her yıl sonunda 100.000 ₺ net nakit girişi beklenmektedir. İşletmenin kullandığı vergi öncesi iskonto oranı %10'dur. TMS 36'ya göre varlığın kullanım değeri yaklaşık kaç ₺'dir?",
        {
            'A': '227.000 ₺',
            'B': '273.000 ₺',
            'C': '300.000 ₺',
            'D': '248.685 ₺',
            'E': '330.000 ₺',
        },
        'D',
        'Kullanım değeri, beklenen nakit akışlarının bugünkü değeridir (TMS 36 par. 30-31): 100.000/1,10 + 100.000/1,10² + 100.000/1,10³ = 90.909 + 82.645 + 75.131 = 248.685 ₺. 300.000 ₺ iskonto edilmemiş toplamdır; paranın zaman değeri dikkate alınmadığında bulunur.',
    ),
}


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
    for q in questions:
        yeni_stem = TL.sub(r"\1 ₺", q["stem"])
        yeni_coz = TL.sub(r"\1 ₺", q["solution"])
        yeni_opt = {L: TL.sub(r"\1 ₺", v) for L, v in q["options"].items()}
        if (yeni_stem, yeni_coz, yeni_opt) != (q["stem"], q["solution"], q["options"]):
            fark.append(f"{path}::{q['id']} TL->₺")
            if write:
                q["stem"], q["solution"], q["options"] = yeni_stem, yeni_coz, yeni_opt
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
    print(f"1 paket / {len(PATCHES)} soru (TMS 36 bicim kalibrasyonu) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
