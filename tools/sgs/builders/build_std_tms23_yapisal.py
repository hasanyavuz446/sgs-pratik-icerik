#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TMS 23 Borçlanma Maliyetleri — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Eylül standart turunun reçetesiyle baştan yazıldı (kalan iki paketten biri, kör %31). Olay anlatan kök, kısa şık (terim/tutar). Kapsam: özellikli varlık ve istisnalar, borçlanma maliyeti unsurları, özel borçlanma (geçici yatırım geliri, ara verme, kur farkının faiz düzeltmesi), genel borçlanma (ağırlıklı aktifleştirme oranı, katlanılan maliyet sınırı, ortalama harcama, hakediş ve teşvik indirimi, hazır olduktan sonra açık kalan özel kredi), başlama-ara verme-sona erme, açıklama. Hesap soruları her biri farklı bağlam ve anlatımla yazıldı (şablon klonu yok); tutarlar kesirli aritmetikle hesaplandı.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: TMS 23 Borçlanma Maliyetleri
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/tms_23_borclanma_maliyetleri.json"
STYLE_REF = 'SGS Muhasebe Standartları (senaryo kök + kısa şık; gerçek sınav profili)'
ONEK = "std-tms23-gen-"


def patch(stem, options, answer, solution, ref='TMS 23 Borçlanma Maliyetleri'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        'TMS 23 ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Geçici yatırım geliri düşülür',
            'B': 'Ara verme dönemleri dışlanır',
            'C': 'Seçimlik olarak gider yazılabilir',
            'D': 'Aktifleştirme katlanılanla sınırlıdır',
            'E': 'Özellikli varlık uzun hazırlık gerektirir',
        },
        'C',
        "TMS 23'e göre özellikli varlıkla doğrudan ilişkili borçlanma maliyetlerinin aktifleştirilmesi zorunludur; gider yazma seçeneği yoktur (zorunlu olmayan istisnalar dışında).",
    ),
    # düzey 2
    '0002': patch(
        "TMS 23'e göre aşağıdaki durumlardan hangisinde borçlanma maliyetlerinin aktifleştirilmesine ara verilmez?",
        {
            'A': 'Finansman sorunu nedeniyle durmada',
            'B': 'Talep düşüşü nedeniyle durmada',
            'C': 'Yasal izin beklenirken faaliyetsizlikte',
            'D': 'Teknik çalışmalar sürerken',
            'E': 'Uzun grevde',
        },
        'D',
        'Önemli teknik ve idari çalışmaların yürütüldüğü dönemlerde aktifleştirmeye ara verilmez. Aktif geliştirme faaliyetlerinin uzun süre durduğu dönemlerde ara verilir.',
    ),
    # düzey 3
    '0003': patch(
        "Bir gıda işletmesi kısa sürede ve büyük miktarlarda rutin olarak ürettiği konserveleri banka kredisiyle finanse etmektedir.\n\nTMS 23'e göre bu stoklarla ilgili borçlanma maliyetleri için aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Aktifleştirmek zorundadır',
            'B': 'Özkaynakta izlemek zorundadır',
            'C': "TMS 23'ü uygulamak zorunda değildir",
            'D': 'Kur farkı olarak sunmak zorundadır',
            'E': 'Stoklardan düşmek zorundadır',
        },
        'C',
        "Büyük miktarlarda ve sürekli olarak üretilen stoklarla ilgili borçlanma maliyetleri için TMS 23'ün uygulanması zorunlu değildir; işletme bunları gider yazabilir.",
    ),
    # düzey 2
    '0004': patch(
        "Bir işletme bir özellikli varlık için kullandığı özel krediyi, varlık tamamlandıktan sonra da geri ödemeyerek kullanmaya devam etmektedir.\n\nTMS 23'e göre tamamlanma sonrasındaki faiz için hangisi doğrudur?",
        {
            'A': 'Gider yazılır',
            'B': 'Kur farkıyla netleştirilir',
            'C': 'Ertelenir',
            'D': 'Varlığa eklenir',
            'E': 'Özkaynağa alınır',
        },
        'A',
        'Varlık kullanıma hazır hâle geldiğinde aktifleştirme sona erer; sonraki dönem faizleri gider yazılır.',
    ),
    # düzey 3
    '0005': patch(
        "I. Etkin faiz yöntemiyle hesaplanan faiz gideri\nII. TFRS 16 kapsamındaki kira yükümlülüklerine ilişkin faiz\nIII. Yabancı para borçlanmasından doğan kur farkının faiz maliyetine düzeltme sayılan kısmı\n\nYukarıdakilerden hangileri TMS 23'e göre borçlanma maliyetleri arasında yer alır?",
        {
            'A': 'I ve III',
            'B': 'II ve III',
            'C': 'I, II ve III',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'C',
        'Borçlanma maliyetleri; etkin faiz yöntemiyle hesaplanan faiz giderini, kira yükümlülüklerine ilişkin faizi ve yabancı para borçlanmalarından doğan kur farklarının faiz maliyetine düzeltme sayılan kısmını kapsar.',
    ),
    # düzey 3
    '0006': patch(
        "İzmir A.Ş. özellikli bir varlığın inşası için 1 Ocak 2026'da 100.000 Avro tutarında. yıllık %5 faizli bir kredi kullanmıştır. Kredi tarihinde kur 40 ₺, yıl sonunda 50 ₺'dir; yıllık faiz yıl sonu kuruyla ödenmiştir. İşletme aynı tutarı Türk lirasıyla %30 faizle borçlanabilirdi. İnşaat yıl boyunca sürmüştür ve kur farkının, TL borçlanmaya göre katlanılmayan faiz kadar olan kısmı faiz maliyetine düzeltme sayılmaktadır.\n\nBuna göre 2026 yılında aktifleştirilecek toplam borçlanma maliyeti kaç ₺'dir?",
        {
            'A': '1.200.000 ₺',
            'B': '1.000.000 ₺',
            'C': '1.150.000 ₺',
            'D': '250.000 ₺',
            'E': '2.200.000 ₺',
        },
        'A',
        'Avro faizi 100.000 · %5 · 50 = 250.000 ₺. Kur farkı 100.000 · (50 − 40) = 1.000.000 ₺. TL borçlanmada katlanılacak faiz 4.000.000 ₺ · %30 = 1.200.000 ₺. Kur farkının faiz düzeltmesi sayılan kısmı en çok 950.000 ₺ olup gerçekleşen kur farkıyla sınırlıdır: 950.000 ₺. Toplam aktifleştirilen 1.200.000 ₺.',
    ),
    # düzey 3
    '0007': patch(
        "Bora A.Ş.'nin hastane inşaatına ilişkin bilgiler şöyledir:\n\n- İnşaat için alınan özel kredi: 4.800.000 ₺\n- Kredinin yıllık faiz oranı: %25\n- Kredinin ve inşaatın başlangıcı: 1 Ocak 2026\n- Hastanenin kullanıma hazır olduğu süre: 9 ay sonra\n- Atıl kredinin repo yatırımından elde edilen gelir: 90.000 ₺\n\nBu bilgilere göre TMS 23 uyarınca hastanenin maliyetine eklenecek tutar kaç ₺'dir?",
        {
            'A': '1.110.000 ₺',
            'B': '810.000 ₺',
            'C': '1.200.000 ₺',
            'D': '900.000 ₺',
            'E': '990.000 ₺',
        },
        'B',
        'Özel borçlanmada aktifleştirilecek tutar, dönemde fiilen katlanılan borçlanma maliyetinden geçici yatırım gelirinin düşülmesiyle bulunur. Katlanılan faiz 4.800.000 ₺ · %25 · 9/12 = 900.000 ₺; geçici yatırım geliri 90.000 ₺ düşülünce 810.000 ₺.',
    ),
    # düzey 2
    '0008': patch(
        "TMS 23'e göre işletmenin dipnotlarında aşağıdakilerden hangisini açıklaması gerekmez?",
        {
            'A': 'Kredi veren bankaların adları',
            'B': 'Dönemde aktifleştirilen tutar',
            'C': 'Aktifleştirilen maliyetlerin niteliği',
            'D': 'Kullanılan aktifleştirme oranı',
            'E': 'Muhasebe politikası',
        },
        'A',
        'TMS 23 dönemde aktifleştirilen borçlanma maliyeti tutarının ve aktifleştirme oranının açıklanmasını ister; kredi veren kuruluşların adları istenmez.',
    ),
    # düzey 3
    '0009': patch(
        "Defne A.Ş. bir rafineri ünitesinin inşası amacıyla 2026 yılı başında 1.200.000 ₺ borçlanmıştır (yıllık faiz %35). Ünite 12 ayda tamamlanmıştır. Borçlanılan fonların bir kısmı inşaatta kullanılıncaya kadar hazine bonosunda değerlendirilmiş ve bundan 45.000 ₺ gelir sağlanmıştır.\n\nRafineri ünitesinin maliyetine TMS 23'e göre kaç ₺ borçlanma maliyeti eklenir?",
        {
            'A': '465.000 ₺',
            'B': '420.000 ₺',
            'C': '375.000 ₺',
            'D': '840.000 ₺',
            'E': '562.500 ₺',
        },
        'C',
        'Özel borçlanmada aktifleştirilecek tutar, dönemde fiilen katlanılan borçlanma maliyetinden geçici yatırım gelirinin düşülmesiyle bulunur. Katlanılan faiz 1.200.000 ₺ · %35 · 12/12 = 420.000 ₺; geçici yatırım geliri 45.000 ₺ düşülünce 375.000 ₺.',
    ),
    # düzey 3
    '0010': patch(
        "Uludağ A.Ş. için bilgiler:\n\n- Özel kredi: 1.200.000 ₺, yıllık %40, 1 Ocak 2026'da alındı\n- Harcamaların ve faaliyetlerin başlangıcı: 1 Şubat\n- Varlığın kullanıma hazır olduğu tarih: Temmuz sonu\n\nTMS 23'e göre aktifleştirilecek borçlanma maliyeti kaç ₺'dir?",
        {
            'A': '120.000 ₺',
            'B': '240.000 ₺',
            'C': '200.000 ₺',
            'D': '480.000 ₺',
            'E': '160.000 ₺',
        },
        'B',
        "Aktifleştirme, koşulların tamamlandığı 1 Şubat'ta başlar ve varlık hazır olunca (Temmuz sonu) biter: 6 ay. 1.200.000 ₺ · %40 · 6/12 = 240.000 ₺. Diğer aylardaki faiz gider yazılır.",
    ),
    # düzey 2
    '0011': patch(
        "Aşağıdakilerden hangisi TMS 23'ün kapsamı dışında kalan bir maliyettir?",
        {
            'A': 'Kur farkının faiz düzeltmesi',
            'B': 'Kredi faizi',
            'C': 'Tahvil faizi',
            'D': 'Kira yükümlülüğü faizi',
            'E': 'Tercihli olmayan özkaynak maliyeti',
        },
        'E',
        'Standart, borçlanma maliyetlerini kapsar; tercihli sermaye niteliğinde olmayan özkaynağın fiilî ya da tahmini maliyeti kapsam dışıdır.',
    ),
    # düzey 2
    '0012': patch(
        "Bir konut şirketi satmak amacıyla 30 ay sürecek bir site inşaatına başlamış ve inşaatı banka kredisiyle finanse etmektedir. Konutların satışa hazır hâle gelmesi için inşaatın tamamlanması gerekmektedir.\n\nTMS 23'e göre inşa edilen konutlar için aşağıdakilerden hangisi söylenebilir?",
        {
            'A': 'Elden çıkarılacak varlıktır',
            'B': 'Özellikli varlıktır',
            'C': "Sahibi kullanımındaki MDV'dir",
            'D': 'Finansal varlıktır',
            'E': 'Biyolojik varlıktır',
        },
        'B',
        'Satışa hazır hâle gelmesi uzun süre gerektiren stoklar özellikli varlıktır; inşa dönemindeki borçlanma maliyetleri maliyete eklenir.',
    ),
    # düzey 2
    '0013': patch(
        "Bir işletme, inşası iki yıl sürecek fabrika binasını tümüyle özkaynaklarıyla finanse etmektedir; dönem içinde hiçbir borçlanması yoktur.\n\nTMS 23'e göre fabrikanın maliyetine eklenecek borçlanma maliyeti kaç ₺'dir?",
        {
            'A': 'Piyasa faizi kadar',
            'B': 'Kâr payı kadar',
            'C': 'Mevduat faizi kadar',
            'D': '0 ₺',
            'E': 'Enflasyon farkı kadar',
        },
        'D',
        'Aktifleştirilecek borçlanma maliyeti fiilen katlanılan maliyetle sınırlıdır. Borçlanma yoksa aktifleştirilecek tutar da yoktur.',
    ),
    # düzey 3
    '0014': patch(
        "Bir köprü inşaatı, bölgedeki yüksek su seviyesi nedeniyle her yıl görülen ve inşaat sürecinin olağan parçası olan iki aylık beklemeyle durmuştur.\n\nTMS 23'e göre bu süre için aktifleştirme hakkında hangisi doğrudur?",
        {
            'A': 'Ara verilmez',
            'B': 'Yarısı aktifleştirilir',
            'C': 'Geriye dönük iptal edilir',
            'D': 'Sona erdirilir',
            'E': 'Ara verilir',
        },
        'A',
        'Geçici gecikme, varlığı hazırlama sürecinin gerekli bir parçasıysa aktifleştirmeye ara verilmez.',
    ),
    # düzey 3
    '0015': patch(
        "Özel borçlanma ile ilgili şu veriler Ege A.Ş.'nin lojistik deposu inşaatına aittir: kredi 6.000.000 ₺, faiz yıllık %20, aktifleştirme dönemi 8 ay (2026 başından itibaren), geçici yatırım geliri 150.000 ₺.\n\nTMS 23'e göre deponun maliyetine eklenecek borçlanma maliyeti kaç ₺'dir?",
        {
            'A': '1.050.000 ₺',
            'B': '950.000 ₺',
            'C': '1.200.000 ₺',
            'D': '800.000 ₺',
            'E': '650.000 ₺',
        },
        'E',
        'Özel borçlanmada aktifleştirilecek tutar, dönemde fiilen katlanılan borçlanma maliyetinden geçici yatırım gelirinin düşülmesiyle bulunur. Katlanılan faiz 6.000.000 ₺ · %20 · 8/12 = 800.000 ₺; geçici yatırım geliri 150.000 ₺ düşülünce 650.000 ₺.',
    ),
    # düzey 2
    '0016': patch(
        "TMS 23'e göre doğrudan bir özellikli varlıkla ilişkilendirilemeyen borçlanma maliyetleri nasıl muhasebeleştirilir?",
        {
            'A': 'Özkaynakta',
            'B': 'Varlık olarak',
            'C': 'Karşılık olarak',
            'D': 'Gider olarak',
            'E': 'Yeniden değerleme fonunda',
        },
        'D',
        'Özellikli varlığın elde edilmesi, inşası ya da üretimiyle doğrudan ilişkilendirilemeyen diğer borçlanma maliyetleri oluştukları dönemde gider olarak muhasebeleştirilir.',
    ),
    # düzey 2
    '0017': patch(
        "Bir işletme 1 Ocak 2026'da inşaatına başladığı alışveriş merkezini kiraya vermek amacıyla inşa etmektedir; inşaat 2027 sonunda bitecektir.\n\nTMS 23 bakımından bu varlık için aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Stok sayılır',
            'B': 'Finansal varlıktır',
            'C': 'Satış amaçlı varlıktır',
            'D': 'Kapsam dışıdır',
            'E': 'Özellikli varlıktır',
        },
        'E',
        'İnşa hâlindeki yatırım amaçlı gayrimenkuller, hazırlık süreleri uzun olduğunda özellikli varlıktır ve ilgili borçlanma maliyetleri aktifleştirilir.',
    ),
    # düzey 3
    '0018': patch(
        "Bir spor salonu inşa eden Toros A.Ş.'nin 3.600.000 ₺ tutarındaki %25 faizli kredisi yıl başından beri kullanılmaktadır. Salonun inşaatına ve ilk harcamaya Mart başında başlanmış, salon Ekim sonunda açılışa hazır hâle gelmiştir. Kredi yıl boyunca açık kalmıştır.\n\nKrediye ait 2026 faizinin kaç ₺'si salonun maliyetine eklenir?",
        {
            'A': '600.000 ₺',
            'B': '525.000 ₺',
            'C': '300.000 ₺',
            'D': '450.000 ₺',
            'E': '200.000 ₺',
        },
        'A',
        "Aktifleştirme, koşulların tamamlandığı 1 Mart'ta başlar ve varlık hazır olunca (Ekim sonu) biter: 8 ay. 3.600.000 ₺ · %25 · 8/12 = 600.000 ₺. Diğer aylardaki faiz gider yazılır.",
    ),
    # düzey 3
    '0019': patch(
        'Mavi A.Ş. birkaç özellikli varlığını ortak fonlarla finanse etmektedir. Yıl boyunca işletmenin bir bankaya 4.000.000 ₺ (%25) ve başka bir bankaya 4.000.000 ₺ (%35) genel amaçlı kredi borcu bulunmaktadır. Ayrıca yalnız bir depo inşaatı için kullanılan 1.000.000 ₺ tutarında %15 faizli bir kredi vardır.\n\nOrtak fonlarla finanse edilen varlıklar için aktifleştirme oranı kaç olmalıdır?',
        {
            'A': '%31',
            'B': '%30',
            'C': '%25',
            'D': '%28,33',
            'E': '%35',
        },
        'B',
        'Aktifleştirme oranı, özel borçlanmalar dışındaki genel borçlanmaların ağırlıklı ortalama maliyetidir: (4.000.000 ₺ · %25 + 4.000.000 ₺ · %35) / 8.000.000 ₺ = %30. Özel kredi hesaba katılmaz; basit ortalama da kullanılmaz.',
    ),
    # düzey 2
    '0020': patch(
        "Bir işletmenin özellikli varlık inşaatı, yüklenici ile çıkan uyuşmazlık nedeniyle beş ay boyunca durmuş ve bu sürede hiçbir teknik ya da idari çalışma yapılmamıştır.\n\nTMS 23'e göre bu dönemdeki borçlanma maliyetleri nasıl muhasebeleştirilir?",
        {
            'A': 'Karşılık olarak',
            'B': 'Aktifleştirilerek',
            'C': 'Gider olarak',
            'D': 'Özkaynakta',
            'E': 'Ertelenmiş vergi olarak',
        },
        'C',
        'Aktif geliştirme faaliyetlerinin uzun süre durdurulduğu dönemlerde aktifleştirmeye ara verilir; bu dönemdeki borçlanma maliyetleri gider yazılır.',
    ),
    # düzey 3
    '0021': patch(
        "Zirve A.Ş. yıl boyunca inşası süren bir özellikli varlık için genel borçlanmalarından 1 Ocak 2026'da 1.000.000 ₺, 1 Temmuz 2026'da 800.000 ₺ harcama yapmıştır. Aktifleştirme oranı %30'dir ve katlanılan toplam borçlanma maliyeti hesaplanan tutardan fazladır.\n\nTMS 23'e göre 2026 yılında aktifleştirilecek borçlanma maliyeti kaç ₺'dir?",
        {
            'A': '300.000 ₺',
            'B': '420.000 ₺',
            'C': '270.000 ₺',
            'D': '540.000 ₺',
            'E': '120.000 ₺',
        },
        'B',
        'Harcamaların ağırlıklı ortalaması: 1.000.000 ₺ · 12/12 + 800.000 ₺ · 6/12 = 1.400.000 ₺. Aktifleştirilen tutar 1.400.000 ₺ · %30 = 420.000 ₺.',
    ),
    # düzey 2
    '0022': patch(
        "Bir otel inşaatının fiziksel yapımı tamamlanmış, yalnızca kullanıcının isteğine göre küçük dekorasyon işleri kalmıştır.\n\nTMS 23'e göre bu aşamada borçlanma maliyetlerinin aktifleştirilmesi hakkında hangisi doğrudur?",
        {
            'A': 'Devam eder',
            'B': 'Ara verilir',
            'C': 'Yeniden başlar',
            'D': 'Sona erer',
            'E': 'İki katına çıkar',
        },
        'D',
        'Varlığı kullanıma hazırlamak için gerekli faaliyetlerin tamamına yakını bittiğinde aktifleştirme sona erer; küçük dekorasyon işleri bu durumu değiştirmez.',
    ),
    # düzey 3
    '0023': patch(
        "Kaya A.Ş. uzun süreli bir maden işleme tesisi kurmak için yıl başında Avro cinsinden 200.000 tutarında borçlanmıştır (yıllık faiz %4). Kur yıl başında 35 ₺ iken yıl sonunda 45 ₺'ye çıkmıştır; faiz yıl sonu kuruyla ödenmiştir. Aynı tutar için TL kredi faizi %25 olacaktı. İşletme, kur farkının TL borçlanmaya göre tasarruf edilen faizi aşmayan kısmını faiz düzeltmesi saymaktadır ve tesis yıl boyunca inşa hâlindedir.\n\nTesisin maliyetine eklenecek toplam tutar kaç ₺'dir?",
        {
            'A': '360.000 ₺',
            'B': '2.360.000 ₺',
            'C': '3.750.000 ₺',
            'D': '1.750.000 ₺',
            'E': '2.000.000 ₺',
        },
        'D',
        'Avro faizi 200.000 · %4 · 45 = 360.000 ₺. Kur farkı 200.000 · (45 − 35) = 2.000.000 ₺. TL borçlanmada katlanılacak faiz 7.000.000 ₺ · %25 = 1.750.000 ₺. Kur farkının faiz düzeltmesi sayılan kısmı en çok 1.390.000 ₺ olup gerçekleşen kur farkıyla sınırlıdır: 1.390.000 ₺. Toplam aktifleştirilen 1.750.000 ₺.',
    ),
    # düzey 2
    '0024': patch(
        "Bir işletmenin genel borçlanmalarına ilişkin aktifleştirme oranı yıl içinde değişmiştir. TMS 23'e göre aktifleştirme oranı hangi yöntemle belirlenir?",
        {
            'A': 'Basit ortalama',
            'B': 'En yüksek oran',
            'C': 'Ağırlıklı ortalama',
            'D': 'Politika faizi',
            'E': 'Yıl sonu oranı',
        },
        'C',
        'Aktifleştirme oranı, dönem boyunca açık olan genel borçlanmalara ilişkin borçlanma maliyetlerinin ağırlıklı ortalamasıdır.',
    ),
    # düzey 2
    '0025': patch(
        'Bir işletme TFRS 16 kapsamında kiraladığı arsa üzerinde iki yıl sürecek bir bina inşa etmektedir. Kira yükümlülüğü için faiz gideri oluşmaktadır.\n\nTMS 23 bakımından bu faiz için hangisi doğrudur?',
        {
            'A': 'Özkaynakta izlenir',
            'B': 'Kapsam dışıdır',
            'C': 'Kira geliri sayılır',
            'D': 'Değer düşüklüğüdür',
            'E': 'Borçlanma maliyetidir',
        },
        'E',
        "Kira yükümlülüklerine ilişkin faiz, TMS 23'te sayılan borçlanma maliyetleri arasındadır.",
    ),
    # düzey 2
    '0026': patch(
        "TMS 23'e göre aktifleştirmeye ara verilen dönemdeki borçlanma maliyetleri hangi tabloda sunulur?",
        {
            'A': 'Dipnotlarda gösterilir',
            'B': 'Finansal durum tablosu',
            'C': 'Kâr veya zarar tablosu',
            'D': 'Özkaynak değişim tablosu',
            'E': 'Nakit akış tablosu dışında',
        },
        'C',
        'Ara verilen dönemde aktifleştirilmeyen borçlanma maliyetleri gider olarak kâr veya zarar tablosunda yer alır.',
    ),
    # düzey 3
    '0027': patch(
        "Orman A.Ş. özellikli bir varlık için genel borçlanmalarından 2.400.000 ₺ harcama yapmıştır; harcama yılın 6. ayının sonunda yapılmış ve varlık yıl sonuna kadar inşa hâlinde kalmıştır. Genel borçlanmaların aktifleştirme oranı %25'dir ve işletmenin yıl içinde katlandığı toplam borçlanma maliyeti 900.000 ₺'dir.\n\nTMS 23'e göre aktifleştirilecek borçlanma maliyeti kaç ₺'dir?",
        {
            'A': '150.000 ₺',
            'B': '900.000 ₺',
            'C': '360.000 ₺',
            'D': '600.000 ₺',
            'E': '300.000 ₺',
        },
        'E',
        'Harcamanın varlıkta kaldığı süre 6 aydır: 2.400.000 ₺ · 6/12 · %25 = 300.000 ₺. Tutar katlanılan borçlanma maliyetini aşmadığından tamamı aktifleştirilir.',
    ),
    # düzey 2
    '0028': patch(
        'Bir işletme özellikli varlık için kullandığı kredi nedeniyle bankaya 50.000 ₺ dosya ve komisyon ücreti ödemiştir.\n\nTMS 23 bakımından bu ödeme nasıl değerlendirilir?',
        {
            'A': 'Kapsam dışı bir giderdir',
            'B': 'Borçlanma maliyetinin parçasıdır',
            'C': 'Doğrudan özkaynaktan düşülür',
            'D': 'Genel yönetim gideridir',
            'E': 'Kur farkı olarak sunulur',
        },
        'B',
        'Kredinin elde edilmesine ilişkin işlem maliyetleri etkin faiz yöntemiyle hesaplanan faiz giderinin parçasıdır; dolayısıyla borçlanma maliyeti sayılır.',
    ),
    # düzey 3
    '0029': patch(
        "Bir işletmenin belirli bir özellikli varlık için aldığı özel kredi, varlık kullanıma hazır hâle geldikten sonra da ödenmeyip açık kalmaktadır. İşletmenin başka özellikli varlıkları genel borçlanmalarla finanse edilmektedir.\n\nTMS 23'e göre açık kalan bu kredi aktifleştirme oranı hesabında nasıl dikkate alınır?",
        {
            'A': 'Hesaptan tamamen çıkarılır',
            'B': 'İlk edinilen varlığa yüklenir',
            'C': 'Genel borçlanmaya dahil edilir',
            'D': 'Ağırlığı iki katına çıkarılır',
            'E': 'Faizi özkaynağa alınır',
        },
        'C',
        'Özellikli varlık hazır hâle geldikten sonra açık kalan özel borçlanmalar, aktifleştirme oranının hesabında genel borçlanmaların içinde yer alır.',
    ),
    # düzey 3
    '0030': patch(
        "Volkan A.Ş. inşası yıl boyunca süren bir özellikli varlık için 1 Ocak 2026'da 2.000.000 ₺ tutarında, yıllık %30 faizli özel bir kredi kullanmış ve bu tutarı aynı gün harcamıştır. Varlık için ayrıca yılın son 6 ayında varlıkta kalan 1.200.000 ₺ tutarında ek harcama genel borçlanmalardan karşılanmıştır. Genel borçlanmaların aktifleştirme oranı %25'dir ve sınırı aşan bir durum yoktur.\n\nTMS 23'e göre 2026 yılında aktifleştirilecek toplam borçlanma maliyeti kaç ₺'dir?",
        {
            'A': '600.000 ₺',
            'B': '900.000 ₺',
            'C': '750.000 ₺',
            'D': '960.000 ₺',
            'E': '800.000 ₺',
        },
        'C',
        'Özel kredi faizi: 2.000.000 ₺ · %30 = 600.000 ₺. Genel borçlanmadan karşılanan kısım: 1.200.000 ₺ · 6/12 · %25 = 150.000 ₺. Toplam 750.000 ₺.',
    ),
    # düzey 2
    '0031': patch(
        "TMS 23'e göre aktifleştirilen borçlanma maliyetleri nedeniyle özellikli varlığın defter değeri geri kazanılabilir tutarını aşarsa ne yapılır?",
        {
            'A': 'Fark özkaynağa alınır',
            'B': 'Değer düşüklüğü ayrılır',
            'C': 'Faiz geri alınır',
            'D': 'Aktifleştirme oranı düşürülür',
            'E': 'Varlık yeniden değerlenir',
        },
        'B',
        'Defter değeri ya da beklenen nihai maliyet geri kazanılabilir tutarı aşarsa, ilgili standartlara (TMS 36 gibi) göre değer düşüklüğü kaydedilir.',
    ),
    # düzey 3
    '0032': patch(
        "Yayla A.Ş.'nin yıl boyunca inşası süren hastane projesi iki kaynaktan finanse edilmiştir: yıl başında alınıp hemen harcanan 3.000.000 ₺ tutarındaki %20 faizli proje kredisi ve yılın son 3 ayında varlıkta kalan, genel fonlardan karşılanan 2.400.000 ₺. Genel fonların aktifleştirme oranı %30'dir.\n\nHastanenin maliyetine eklenecek toplam borçlanma maliyeti kaç ₺'dir?",
        {
            'A': '600.000 ₺',
            'B': '1.620.000 ₺',
            'C': '1.320.000 ₺',
            'D': '1.080.000 ₺',
            'E': '780.000 ₺',
        },
        'E',
        'Özel kredi faizi: 3.000.000 ₺ · %20 = 600.000 ₺. Genel borçlanmadan karşılanan kısım: 2.400.000 ₺ · 3/12 · %30 = 180.000 ₺. Toplam 780.000 ₺.',
    ),
    # düzey 3
    '0033': patch(
        "Bir işletme 1 Mart'ta özellikli varlık için kredi kullanmış, 1 Mayıs'ta ilk harcamayı yapmış ve inşaat için gerekli izin ve teknik çalışmalara 1 Nisan'da başlamıştır.\n\nTMS 23'e göre aktifleştirmeye hangi tarihte başlanır?",
        {
            'A': '1 Haziran',
            'B': '1 Ocak',
            'C': '1 Nisan',
            'D': '1 Mart',
            'E': '1 Mayıs',
        },
        'E',
        "Aktifleştirme, üç koşulun (borçlanma, harcama, faaliyet) birlikte sağlandığı ilk tarihte başlar. Son koşul 1 Mayıs'ta (harcama) sağlanmıştır.",
    ),
    # düzey 3
    '0034': patch(
        "Bir çelik fabrikası, farklı aşamaları tamamlanmış olsa da ancak bütün tesis bitince kullanılabilecek şekilde inşa edilmektedir.\n\nTMS 23'e göre tamamlanmış aşamalar için aktifleştirme hakkında hangisi doğrudur?",
        {
            'A': 'Geriye dönük iptal edilir',
            'B': 'Tesis bitene kadar sürer',
            'C': 'Hemen ara verilir',
            'D': 'Aşama bitince sona erer',
            'E': 'Yarı oranda sürer',
        },
        'B',
        'Bütün kısımları tamamlanmadan kullanılamayan varlıklarda aktifleştirme, varlığın tamamı kullanıma hazır olana kadar sürer.',
    ),
    # düzey 3
    '0035': patch(
        "Bir okul binası inşa eden Pınar A.Ş.'nin bu bina için yaptığı tek harcama, son 8 ayda varlıkta kalan 3.000.000 ₺'dir ve genel fonlardan karşılanmıştır. Aktifleştirme oranı %30 olarak hesaplanmıştır; işletmenin tüm borçları için yıl içinde ödediği faiz ise 400.000 ₺'dir.\n\nBinanın maliyetine eklenecek tutar kaç ₺'dir?",
        {
            'A': '300.000 ₺',
            'B': '900.000 ₺',
            'C': '600.000 ₺',
            'D': '400.000 ₺',
            'E': '200.000 ₺',
        },
        'D',
        'Harcamanın varlıkta kaldığı süre 8 aydır: 3.000.000 ₺ · 8/12 · %30 = 600.000 ₺. Bu tutar katlanılan borçlanma maliyetini (400.000 ₺) aştığı için aktifleştirme 400.000 ₺ ile sınırlıdır.',
    ),
    # düzey 3
    '0036': patch(
        "I. Varlık için harcama yapılması\nII. Borçlanma maliyetine katlanılması\nIII. Varlığın sigortalanması\nIV. Varlığı hazırlamak için gerekli faaliyetlerin üstlenilmesi\n\nTMS 23'e göre borçlanma maliyetlerinin aktifleştirilmesine başlanabilmesi için yukarıdakilerden hangileri gerekir?",
        {
            'A': 'II, III ve IV',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'I, II ve IV',
            'E': 'I, II, III ve IV',
        },
        'D',
        'Aktifleştirme; harcama yapılması, borçlanma maliyetine katlanılması ve varlığı hazırlamaya yönelik faaliyetlerin üstlenilmesi koşullarının üçü birlikte sağlandığında başlar. Sigorta bu koşullardan biri değildir.',
    ),
    # düzey 3
    '0037': patch(
        "Bir işletmenin inşa ettiği depo kullanıma hazır hâle gelmiş, ancak işletme depoyu iki ay sonra kullanmaya başlamıştır.\n\nTMS 23'e göre bu iki aylık süredeki borçlanma maliyetleri için hangisi doğrudur?",
        {
            'A': 'Depoya eklenir',
            'B': 'Gider yazılır',
            'C': 'Kur farkıyla netleştirilir',
            'D': 'Ertelenir',
            'E': 'Özkaynağa alınır',
        },
        'B',
        'Aktifleştirme varlık kullanıma hazır olduğunda sona erer; fiilen kullanılmaya başlanma tarihi beklenmez.',
    ),
    # düzey 3
    '0038': patch(
        "Bir tarım işletmesi gerçeğe uygun değerinden satış maliyetleri düşülerek ölçülen meyve bahçesinin geliştirilmesini krediyle finanse etmektedir.\n\nTMS 23'e göre bu varlıkla ilgili borçlanma maliyetleri için aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Özkaynakta biriktirilir',
            'B': "TMS 23'ü uygulamak zorunda değildir",
            'C': 'Mutlaka aktifleştirilir',
            'D': 'Kur farkı olarak sunulur',
            'E': 'Biyolojik varlıktan düşülür',
        },
        'B',
        "Gerçeğe uygun değerle ölçülen özellikli varlıklar (örneğin biyolojik varlıklar) için TMS 23'ün uygulanması zorunlu değildir.",
    ),
    # düzey 2
    '0039': patch(
        "TMS 23'e göre aşağıdakilerden hangisi borçlanma maliyetlerinin aktifleştirilmesine başlama koşullarından biri değildir?",
        {
            'A': 'Varlığın sigortalanması',
            'B': 'Hazırlık faaliyetlerinin başlaması',
            'C': 'Borçlanma maliyetine katlanılması',
            'D': 'İnşaat izni başvurusu yapılması',
            'E': 'Harcama yapılması',
        },
        'A',
        'Başlama koşulları harcama, borçlanma maliyeti ve hazırlık faaliyetleridir. Hazırlık faaliyetleri inşaat izni almak gibi idari çalışmaları da kapsar; sigorta bir koşul değildir.',
    ),
    # düzey 3
    '0040': patch(
        "Bir işletme bir özellikli varlık için yapılan harcamaları hesaplarken müşteriden alınan 500.000 ₺ hakedişi ve 200.000 ₺ devlet teşvikini dikkate almak istemektedir. Toplam harcama 2.000.000 ₺'dir.\n\nTMS 23'e göre aktifleştirme oranının uygulanacağı harcama tutarı kaç ₺'dir?",
        {
            'A': '1.500.000 ₺',
            'B': '2.700.000 ₺',
            'C': '1.800.000 ₺',
            'D': '1.300.000 ₺',
            'E': '2.000.000 ₺',
        },
        'D',
        'Özellikli varlığa ilişkin harcamalar; varlık için alınan hakediş ödemeleri ve devlet teşvikleri kadar azaltılır: 2.000.000 − 500.000 − 200.000 = 1.300.000 ₺.',
    ),
    # düzey 3
    '0041': patch(
        "Sakarya A.Ş. 1 Ocak 2026'da 2.400.000 ₺ tutarında, yıllık %30 faizli özel bir kredi kullanmıştır. Özellikli varlık için ilk harcama 1 Nisan'ta yapılmış ve faaliyetler aynı gün başlamıştır. Varlık Eylül ayının sonunda kullanıma hazır hâle gelmiştir; geçici yatırım geliri yoktur.\n\nTMS 23'e göre 2026 yılında aktifleştirilecek borçlanma maliyeti kaç ₺'dir?",
        {
            'A': '180.000 ₺',
            'B': '360.000 ₺',
            'C': '240.000 ₺',
            'D': '60.000 ₺',
            'E': '300.000 ₺',
        },
        'B',
        "Aktifleştirme, koşulların tamamlandığı 1 Nisan'ta başlar ve varlık hazır olunca (Eylül sonu) biter: 6 ay. 2.400.000 ₺ · %30 · 6/12 = 360.000 ₺. Diğer aylardaki faiz gider yazılır.",
    ),
    # düzey 3
    '0042': patch(
        "Bir tersane işletmesi olan Ceren A.Ş., siparişsiz olarak kendi filosu için inşa ettiği gemiyi 1 Ocak 2026'da çektiği 3.600.000 ₺ tutarındaki, yıllık %40 faizli krediyle finanse etmektedir. Muhasebe müdürü, inşaatın sürdüğü 6 ay boyunca tahakkuk eden faizin tamamını gemiye eklemek istemektedir; oysa kredinin kullanılmayan kısmından 120.000 ₺ faiz geliri de elde edilmiştir.\n\nTMS 23'e göre gemiye eklenmesi gereken doğru tutar kaç ₺'dir?",
        {
            'A': '720.000 ₺',
            'B': '1.440.000 ₺',
            'C': '1.320.000 ₺',
            'D': '840.000 ₺',
            'E': '600.000 ₺',
        },
        'E',
        'Özel borçlanmada aktifleştirilecek tutar, dönemde fiilen katlanılan borçlanma maliyetinden geçici yatırım gelirinin düşülmesiyle bulunur. Katlanılan faiz 3.600.000 ₺ · %40 · 6/12 = 720.000 ₺; geçici yatırım geliri 120.000 ₺ düşülünce 600.000 ₺.',
    ),
    # düzey 2
    '0043': patch(
        "Bir enerji şirketi 2026 yılında aşağıdaki varlıkları edinmiştir:\n\n- İnşası üç yıl sürecek bir rüzgâr santrali\n- Tedarikçiden hazır satın alınan bir jeneratör\n- Her ay binlerce adet üretilen elektrik sayaçları\n- Bankada açılan altı aylık vadeli mevduat\n- Borsada işlem gören hisse senetleri\n\nTMS 23'e göre bu varlıklardan hangisi özellikli varlıktır?",
        {
            'A': 'Vadeli mevduat',
            'B': 'Hisse senetleri',
            'C': 'Rüzgâr santrali',
            'D': 'Jeneratör',
            'E': 'Elektrik sayaçları',
        },
        'C',
        'Özellikli varlık, amaçlanan kullanıma ya da satışa hazır hâle gelmesi zorunlu olarak uzun süre gerektiren varlıktır. Üç yıl sürecek santral inşası bu tanıma uyar. Hazır alınan varlıklar, kısa sürede seri üretilen stoklar ve finansal varlıklar özellikli varlık değildir.',
    ),
    # düzey 2
    '0044': patch(
        "Bir işletme bazı özellikli varlıklarını genel borçlanmalarla finanse etmektedir. TMS 23'e göre genel borçlanmalardan aktifleştirilecek tutarla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Katlanılan maliyeti aşamaz',
            'B': 'Özkaynak tutarıyla sınırlıdır',
            'C': 'Sınırsız aktifleştirilir',
            'D': 'Faiz gelirine eşittir',
            'E': 'Vergi matrahına eşittir',
        },
        'A',
        'Bir dönemde aktifleştirilen borçlanma maliyeti tutarı, o dönemde katlanılan borçlanma maliyeti tutarını aşamaz.',
    ),
    # düzey 3
    '0045': patch(
        "Fırat A.Ş. bir alışveriş merkezinin inşası için 1 Ocak 2026'da 3.000.000 ₺ tutarında, yıllık %24 faizli özel bir kredi kullanmıştır. İnşaat işletmenin finansman sorunları nedeniyle yıl içinde 3 ay boyunca durmuş, diğer aylarda kesintisiz sürmüştür ve 2026 sonunda henüz tamamlanmamıştır.\n\nTMS 23'e göre 2026 yılında aktifleştirilecek borçlanma maliyeti kaç ₺'dir?",
        {
            'A': '360.000 ₺',
            'B': '720.000 ₺',
            'C': '600.000 ₺',
            'D': '180.000 ₺',
            'E': '540.000 ₺',
        },
        'E',
        'Aktif geliştirme faaliyetleri uzun süre durdurulduğunda aktifleştirmeye ara verilir; 3 aylık dönem dışarıda bırakılır: 720.000 ₺ · 9/12 = 540.000 ₺.',
    ),
    # düzey 3
    '0046': patch(
        "Atlas A.Ş., inşasına 1 Ocak 2026'da başladığı bir otel için aynı tarihte 2.000.000 ₺ tutarında, yıllık %30 faizli bir kredi kullanmıştır. Kredinin henüz harcanmayan kısmı geçici olarak mevduata yatırılmış ve 60.000 ₺ faiz geliri elde edilmiştir. Otel 12 ay sonra kullanıma hazır hâle gelmiştir.\n\nTMS 23'e göre otelin maliyetine eklenecek borçlanma maliyeti kaç ₺'dir?",
        {
            'A': '540.000 ₺',
            'B': '270.000 ₺',
            'C': '660.000 ₺',
            'D': '600.000 ₺',
            'E': '1.200.000 ₺',
        },
        'A',
        'Özel borçlanmada aktifleştirilecek tutar, dönemde fiilen katlanılan borçlanma maliyetinden geçici yatırım gelirinin düşülmesiyle bulunur. Katlanılan faiz 2.000.000 ₺ · %30 · 12/12 = 600.000 ₺; geçici yatırım geliri 60.000 ₺ düşülünce 540.000 ₺.',
    ),
    # düzey 3
    '0047': patch(
        "I. Kısa sürede seri üretilen stoklar\nII. İnşası uzun süren baraj\nIII. Satın alındığında kullanıma hazır kamyon\n\nYukarıdakilerden hangileri TMS 23'e göre özellikli varlık değildir?",
        {
            'A': 'II ve III',
            'B': 'I, II ve III',
            'C': 'I ve III',
            'D': 'Yalnız I',
            'E': 'I ve II',
        },
        'C',
        'Kısa sürede seri üretilen stoklar ve elde edildiğinde kullanıma hazır varlıklar özellikli varlık değildir; inşası uzun süren baraj özellikli varlıktır.',
    ),
    # düzey 2
    '0048': patch(
        "TMS 23'e göre bir varlığın özellikli varlık sayılıp sayılmamasında belirleyici ölçüt aşağıdakilerden hangisidir?",
        {
            'A': 'Varlığın fiziksel büyüklüğü',
            'B': 'Varlığın satın alma fiyatı',
            'C': 'Finansman kaynağının türü',
            'D': 'Hazırlık süresinin uzunluğu',
            'E': 'Kredinin para birimi',
        },
        'D',
        'Özellikli varlık, amaçlanan kullanıma ya da satışa hazır hâle gelmesi zorunlu olarak uzun bir süre gerektiren varlıktır; ölçüt hazırlık süresidir.',
    ),
    # düzey 3
    '0049': patch(
        "Lale A.Ş.'nin 2026 yılı boyunca açık kalan borçlanmaları şunlardır:\n\n- Genel amaçlı banka kredisi: 3.000.000 ₺, yıllık %30\n- Genel amaçlı tahvil: 1.000.000 ₺, yıllık %20\n- Belirli bir fabrika inşaatı için alınan özel kredi: 2.000.000 ₺, yıllık %15\n\nTMS 23'e göre genel borçlanmalar için kullanılacak aktifleştirme oranı kaçtır?",
        {
            'A': '%27,5',
            'B': '%30',
            'C': '%25',
            'D': '%20',
            'E': '%23,33',
        },
        'A',
        'Aktifleştirme oranı, özel borçlanmalar dışındaki genel borçlanmaların ağırlıklı ortalama maliyetidir: (3.000.000 ₺ · %30 + 1.000.000 ₺ · %20) / 4.000.000 ₺ = %27,5. Özel kredi hesaba katılmaz; basit ortalama da kullanılmaz.',
    ),
    # düzey 3
    '0050': patch(
        "Bir işletme arsa üzerine bina inşa etmek amacıyla arsayı satın almış; ancak arsa üzerinde herhangi bir geliştirme faaliyeti yapmadan yalnız elde tutmaktadır.\n\nTMS 23'e göre bu süre içindeki borçlanma maliyetleri için aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Özkaynağa alınır',
            'B': 'Ertelenir',
            'C': 'Gider yazılır',
            'D': 'Binaya eklenir',
            'E': 'Arsaya eklenir',
        },
        'C',
        'Geliştirme faaliyeti yapılmaksızın yalnız elde tutulan arsa için katlanılan borçlanma maliyetleri aktifleştirilmeye uygun değildir.',
    ),
    # düzey 3
    '0051': patch(
        "Finans müdürü, Nehir A.Ş.'nin aktifleştirme oranını hesaplarken şu üç borcun basit ortalamasını almayı önermiştir: %20 faizli 6.000.000 ₺ genel kredi, %40 faizli 2.000.000 ₺ genel kredi ve yalnız bir okul inşaatına ait %15 faizli 3.000.000 ₺ kredi.\n\nTMS 23'e uygun aktifleştirme oranı kaçtır?",
        {
            'A': '%20',
            'B': '%40',
            'C': '%22,27',
            'D': '%25',
            'E': '%30',
        },
        'D',
        'Aktifleştirme oranı, özel borçlanmalar dışındaki genel borçlanmaların ağırlıklı ortalama maliyetidir: (6.000.000 ₺ · %20 + 2.000.000 ₺ · %40) / 8.000.000 ₺ = %25. Özel kredi hesaba katılmaz; basit ortalama da kullanılmaz.',
    ),
    # düzey 3
    '0052': patch(
        "Rüya A.Ş. için 2026 verileri:\n\n- Genel fonlardan yapılan özellikli varlık harcaması: 1.800.000 ₺\n- Harcamanın varlıkta kaldığı süre: 4 ay\n- Aktifleştirme oranı: %20\n- Yıl içinde katlanılan toplam borçlanma maliyeti: 500.000 ₺\n\nTMS 23'e göre aktifleştirilecek tutar kaç ₺'dir?",
        {
            'A': '60.000 ₺',
            'B': '500.000 ₺',
            'C': '150.000 ₺',
            'D': '360.000 ₺',
            'E': '120.000 ₺',
        },
        'E',
        'Harcamanın varlıkta kaldığı süre 4 aydır: 1.800.000 ₺ · 4/12 · %20 = 120.000 ₺. Tutar katlanılan borçlanma maliyetini aşmadığından tamamı aktifleştirilir.',
    ),
    # düzey 3
    '0053': patch(
        "Harran A.Ş.'nin yeni üretim tesisi için 2026 yılına ait bilgiler:\n\n- Yıl başında alınan özel kredi: 4.200.000 ₺\n- Yıllık faiz oranı: %20\n- İnşaatın durduğu süre: 4 ay (satın alma onayının beklenmesi nedeniyle hiçbir çalışma yapılmadan)\n- Tesis yıl sonunda tamamlanmamıştır.\n\nTMS 23'e göre tesisin maliyetine eklenecek borçlanma maliyeti kaç ₺'dir?",
        {
            'A': '560.000 ₺',
            'B': '840.000 ₺',
            'C': '280.000 ₺',
            'D': '700.000 ₺',
            'E': '420.000 ₺',
        },
        'A',
        'Aktif geliştirme faaliyetleri uzun süre durdurulduğunda aktifleştirmeye ara verilir; 4 aylık dönem dışarıda bırakılır: 840.000 ₺ · 8/12 = 560.000 ₺.',
    ),
    # düzey 3
    '0054': patch(
        "Bir işletme her biri ayrı ayrı kullanılabilen beş binadan oluşan bir iş merkezi inşa etmektedir. Binalardan ikisi tamamlanmış ve kullanıma açılmış, diğerlerinin inşaatı sürmektedir.\n\nTMS 23'e göre tamamlanan iki bina için aktifleştirme hakkında hangisi doğrudur?",
        {
            'A': 'Diğerleri bitince sona erer',
            'B': 'Devam eder',
            'C': 'Ara verilir',
            'D': 'Geriye dönük iptal edilir',
            'E': 'Sona erer',
        },
        'E',
        'Kısımlar hâlinde tamamlanan ve her bir kısmı diğerlerinin inşası sürerken kullanılabilen varlıklarda, tamamlanan kısım için aktifleştirme sona erer.',
    ),
    # düzey 2
    '0055': patch(
        "TMS 23'e göre aşağıdakilerden hangisi özellikli varlık olamaz?",
        {
            'A': 'Geliştirilmesi uzun süren yazılım',
            'B': 'Yapımı iki yıl süren otel binası',
            'C': 'Olgunlaşması yıllar alan viski stoku',
            'D': 'Satın alındığında kullanıma hazır makine',
            'E': 'İnşa hâlindeki yatırım amaçlı bina',
        },
        'D',
        'Elde edildiğinde amaçlanan kullanıma hazır olan varlıklar özellikli varlık değildir. Uzun hazırlık süreci gerektiren binalar, stoklar ve maddi olmayan duran varlıklar özellikli varlık olabilir.',
    ),
    # düzey 2
    '0056': patch(
        "Bir işletme özellikli varlık inşaatı için kullandığı kredinin faizi dışında aşağıdaki giderlere de katlanmıştır. TMS 23'e göre bunlardan hangisi borçlanma maliyeti sayılmaz?",
        {
            'A': 'Kur farkının faiz düzeltmesi kısmı',
            'B': 'Özkaynağın fırsat maliyeti',
            'C': 'Kredi faizi',
            'D': 'Etkin faizle itfa edilen ihraç gideri',
            'E': 'Kira yükümlülüğü faizi',
        },
        'B',
        'Borçlanma maliyetleri fon kullanımıyla ilgili fiilen katlanılan faiz ve diğer maliyetlerdir. Özkaynağın tercih edilen kâr payı dışındaki fırsat maliyeti borçlanma maliyeti değildir.',
    ),
    # düzey 3
    '0057': patch(
        "Akdeniz A.Ş.'nin bir liman yapımı için genel fonlardan yaptığı harcamalar şöyledir:\n\n- 1 Ocak 2026: 2.400.000 ₺\n- 1 Temmuz 2026: 1.200.000 ₺\n\nLiman yıl sonunda tamamlanmamıştır. Aktifleştirme oranı %25'dir ve katlanılan borçlanma maliyeti sınırı aşılmamaktadır.\n\nLimanın maliyetine eklenecek tutar kaç ₺'dir?",
        {
            'A': '900.000 ₺',
            'B': '600.000 ₺',
            'C': '450.000 ₺',
            'D': '750.000 ₺',
            'E': '150.000 ₺',
        },
        'D',
        'Harcamaların ağırlıklı ortalaması: 2.400.000 ₺ · 12/12 + 1.200.000 ₺ · 6/12 = 3.000.000 ₺. Aktifleştirilen tutar 3.000.000 ₺ · %25 = 750.000 ₺.',
    ),
    # düzey 3
    '0058': patch(
        "Bir baraj projesini yürüten Gediz A.Ş.'nin 2026 yılında kullandığı tek kredi, yıl başında alınan 2.400.000 ₺ tutarındaki %30 faizli kredidir. Baraj gövdesindeki çalışmalar beton dökümünden sonra teknik olarak zorunlu kür süresi nedeniyle 2 ay ara vermiş; proje yıl sonunda hâlâ sürmektedir.\n\nBu krediye ait 2026 faizinin ne kadarı TMS 23'e göre barajın maliyetine eklenir?",
        {
            'A': '120.000 ₺',
            'B': '600.000 ₺',
            'C': '720.000 ₺',
            'D': '360.000 ₺',
            'E': '660.000 ₺',
        },
        'C',
        'Gecikme, inşaatın gerektirdiği teknik bir bekleme olduğundan aktifleştirmeye ara verilmez; yıllık faizin tamamı aktifleştirilir.',
    ),
    # düzey 3
    '0059': patch(
        "Bir işletme yüksek enflasyonlu bir ekonomide faaliyet göstermekte ve TMS 29'u uygulamaktadır. TMS 23'e göre borçlanma maliyetlerinin enflasyonu telafi eden kısmı için hangisi doğrudur?",
        {
            'A': 'Ertelenir',
            'B': 'Özkaynağa alınır',
            'C': 'Kur farkına eklenir',
            'D': 'Gider yazılır',
            'E': 'Aktifleştirilir',
        },
        'D',
        'TMS 29 uygulanırken borçlanma maliyetlerinin aynı dönemdeki enflasyonu telafi eden kısmı gider olarak muhasebeleştirilir.',
    ),
    # düzey 3
    '0060': patch(
        "TMS 23'e göre özellikli varlıkla ilgili harcamalara aşağıdakilerden hangisi dahil edilmez?",
        {
            'A': 'Devredilen diğer varlıklar',
            'B': 'Faizli yükümlülük üstlenilmesi',
            'C': 'Önceden aktifleştirilen faiz',
            'D': 'Henüz ödenmemiş satıcı borçları',
            'E': 'Nakit ödemeler',
        },
        'D',
        'Harcamalar; nakit ödemeler, diğer varlıkların devri ya da faiz doğuran yükümlülüklerin üstlenilmesiyle sonuçlanan tutarlardır. Faiz doğurmayan, henüz ödenmemiş satıcı borçları harcamaya dahil edilmez.',
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
    print(f"1 paket / {len(PATCHES)} soru ('TMS 23 Borçlanma Maliyetleri' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
