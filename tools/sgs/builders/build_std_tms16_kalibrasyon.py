#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TMS 16 Maddi Duran Varlıklar — biçim kalibrasyonu (içerik kapsamı zaten tam).

ÖLÇÜLEN KUSURLAR (2026-07-28):
  · kökünde ≥2 tutar **%0** — oysa gerçek sınav TMS 16'yı ağırlıkla HESAP sorusu
    olarak soruyor. Ölçülen tipler:
      – azalan bakiyeler → normal amortismana GEÇİŞ: 2014-16, 2023, 2024 (üç kez!)
      – kıst amortisman: 2025 s.43 (01.07.2023, 1.200.000 ₺, 5 yıl, azalan bakiyeler)
      – birikmiş amortisman: 2026/1 (31.12.2025 finansal durum tablosunda)
      – maliyet bedeli + amortisman birlikte: 2016-18 (95.000 + 5.000 montaj, 4 yıl)
      – yeniden değerleme kaydı: 2022 s.34 (800.000 ₺ maliyet + birikmiş amortisman)
      – maliyete dâhil edilemeyen unsur: 2014-16 s.42 (olumsuz kök)
  · kök kalıbı **43/60 aynı** ("…bakımından aşağıdakilerden hangisi doğrudur?") —
    §2: "Aynı kök kalıbı seri üretimde kullanılmaz."
  · para birimi **TL** (8 soru) — §8 "₺ sembolü kullanılır"
  · olumsuz kök %6 · kör öğrenci %28 (eşiğe yakın)

Bu tur içerik değil BİÇİM düzeltir; kapsam ve doğruluk korunur.
Dayanak: KGK TMS 16 par. 7, 16-22, 24, 43-49, 50-62A, 67-72, 73-79.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/tms_16_mdv.json"
STYLE_REF = "SGS Muhasebe Standartlari TMS 16"

# §8: "₺ sembolü kullanılır". Bu pakette 8 soru TL kullaniyordu; yamalananlar
# zaten ₺ ile yazildi, yamalanmayanlar burada mekanik olarak cevrilir.
TL = re.compile(r"(\d)\s*TL\b")


def std_patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": "TMS 16 Maddi Duran Varliklar"},
        "validYear": 2026, "mockExamId": None,
    }


PATCHES = {
    'std-tms16-gen-0003': std_patch(
        "TMS 16'ya göre bir maddi duran varlık ilk muhasebeleştirmede hangi değerle ölçülür?",
        {
            'A': 'Gerçeğe uygun değeriyle',
            'B': 'Net gerçekleşebilir değeriyle',
            'C': 'Yeniden üretim maliyetiyle',
            'D': 'Vergi değeriyle',
            'E': 'Maliyet bedeliyle',
        },
        'E',
        'TMS 16 par. 15: muhasebeleştirme ölçütlerini karşılayan bir maddi duran varlık kalemi, ilk muhasebeleştirmede maliyet bedeliyle ölçülür. Gerçeğe uygun değer ancak yeniden değerleme modelinde ve sonraki ölçümde gündeme gelir.',
    ),
    'std-tms16-gen-0004': std_patch(
        "Aşağıdakilerden hangisi TMS 16'ya göre bir maddi duran varlık kaleminin maliyetine dâhil edilemez?",
        {
            'A': 'Satın alma fiyatı ile iade edilmeyen alış vergileri',
            'B': 'Yeni bir tesisin açılışına ilişkin tanıtım ve reklam maliyetleri',
            'C': 'Varlığı çalışır duruma getirmek için katlanılan montaj maliyetleri',
            'D': 'Varlığın taşınması ve yerleştirilmesine ilişkin maliyetler',
            'E': 'Varlığın düzgün çalışıp çalışmadığının sınanması maliyetleri',
        },
        'B',
        'TMS 16 par. 16-17: maliyete satın alma fiyatı, iade edilmeyen vergiler ile varlığı amaçlanan kullanıma hazır duruma getiren doğrudan maliyetler (montaj, taşıma, sınama) girer. Par. 19: yeni tesis açılış maliyetleri, yeni ürün tanıtım maliyetleri, personel eğitimi ve yönetim genel giderleri maliyete alınmaz.',
    ),
    'std-tms16-gen-0007': std_patch(
        'Bir maddi duran varlığın maliyetine ekleme ne zaman durdurulur?',
        {
            'A': 'Varlık fiilen üretimde kullanılmaya başlandığında; kullanıma hazır olması yeterli sayılmaz',
            'B': 'Varlığın bedeli tümüyle ödendiğinde',
            'C': 'Varlık normal kapasitesine ulaştığında',
            'D': 'Varlık yönetimin amaçladığı biçimde çalışabileceği konum ve duruma geldiğinde',
            'E': 'İlgili hesap dönemi sona erdiğinde',
        },
        'D',
        'TMS 16 par. 20: bir maddi duran varlığın maliyetine ekleme, varlık yönetimin amaçladığı biçimde çalışabilmesi için gerekli konum ve duruma geldiğinde sona erer. Sonraki dönemde varlık henüz kullanılmasa veya kapasitenin altında çalışsa da maliyete ekleme yapılmaz.',
    ),
    'std-tms16-gen-0013': std_patch(
        "Bir işletme makineyi 500.000 ₺ liste fiyatıyla almış, satıcıdan 50.000 ₺ ticari iskonto elde etmiştir. Ayrıca nakliye için 20.000 ₺, montaj için 35.000 ₺, makinenin düzgün çalıştığını sınamak amacıyla yapılan deneme üretimi için 15.000 ₺, personelin makineyi kullanmak üzere eğitilmesi için 12.000 ₺ ve açılış tanıtımı için 8.000 ₺ harcanmıştır. TMS 16'ya göre makinenin maliyeti kaç ₺'dir?",
        {
            'A': '540.000 ₺',
            'B': '520.000 ₺',
            'C': '505.000 ₺',
            'D': '532.000 ₺',
            'E': '570.000 ₺',
        },
        'B',
        'TMS 16 par. 16-17: satın alma fiyatından ticari iskonto düşülür; varlığı çalışır duruma getiren nakliye, montaj ve düzgün çalıştığını sınama (deneme üretimi) maliyetleri eklenir. 500.000 − 50.000 + 20.000 + 35.000 + 15.000 = 520.000 ₺. Par. 19 uyarınca personel eğitimi ile tanıtım ve reklam maliyetleri maliyete alınmaz, dönem gideri yazılır.',
    ),
    'std-tms16-gen-0014': std_patch(
        "Bir işletme 800.000 ₺'ye tesis satın almıştır. Sözleşme gereği tesis on yıl sonra sökülecek ve arazi eski hâline getirilecektir. Sökme ve restorasyon maliyetinin on yıl sonraki tahmini tutarı 200.000 ₺, bu yükümlülüğün bugünkü değeri ise 90.000 ₺ olarak hesaplanmıştır. TMS 16'ya göre tesisin ilk muhasebeleştirme değeri kaç ₺'dir?",
        {
            'A': '800.000 ₺',
            'B': '1.000.000 ₺',
            'C': '710.000 ₺',
            'D': '890.000 ₺',
            'E': '910.000 ₺',
        },
        'D',
        'TMS 16 par. 16(c): maddi duran varlığın sökülmesi, taşınması ve yerleştirildiği alanın restorasyonuna ilişkin tahmini maliyet, TMS 37 uyarınca karşılık ayrılması gerektiğinde varlığın maliyetine dâhil edilir. Karşılık bugünkü değeriyle ölçülür: 800.000 + 90.000 = 890.000 ₺.',
    ),
    'std-tms16-gen-0016': std_patch(
        "Bir işletme makinesine düzenli günlük bakım yaptırmış ve bedelini ödemiştir. TMS 16'ya göre bu harcama nasıl muhasebeleştirilir?",
        {
            'A': 'Oluştuğu dönemde kâr veya zararda gider olarak',
            'B': 'Varlığın defter değerine eklenerek',
            'C': 'Kalan faydalı ömre yayılarak',
            'D': 'Doğrudan özkaynaklardan indirilerek',
            'E': 'Ayrı bir varlık olarak aktifleştirilerek ve kendi faydalı ömrüne göre amorti edilerek',
        },
        'A',
        'TMS 16 par. 12: günlük bakım maliyetleri (işçilik, sarf malzemesi, küçük parçalar) varlığın defter değerine eklenmez; oluştukları dönemde kâr veya zararda muhasebeleştirilir.',
    ),
    'std-tms16-gen-0017': std_patch(
        'Düzenli aralıklarla yapılan büyük çaplı denetim (muayene) maliyetleri nasıl ele alınır?',
        {
            'A': 'Oluştuğu dönemde tümüyle gider yazılır',
            'B': 'Karşılık ayrılarak gelecek dönemlere yayılır; önceki denetimden kalan tutar defter değerinde bırakılır',
            'C': 'Muhasebeleştirme ölçütleri karşılanıyorsa varlığın defter değerine eklenir ve önceki denetimin kalan tutarı bilanço dışı bırakılır',
            'D': 'Doğrudan özkaynaklardan indirilir',
            'E': 'Yalnızca dipnotta açıklanır',
        },
        'C',
        'TMS 16 par. 14: varlığın kullanılmaya devam edebilmesi için düzenli aralıklarla yapılan büyük çaplı denetim maliyeti, muhasebeleştirme ölçütleri karşılanıyorsa defter değerine eklenir. Önceki denetimden kalan tutar varsa bilanço dışı bırakılır.',
    ),
    'std-tms16-gen-0019': std_patch(
        'Bir maddi duran varlığın maliyetine göre önemli parçaları farklı faydalı ömürlere sahipse ne yapılır?',
        {
            'A': 'Varlığın tamamı en uzun faydalı ömre göre amorti edilir',
            'B': 'Her önemli parça ayrı ayrı amortismana tabi tutulur',
            'C': 'Varlığın tamamı en kısa faydalı ömre göre amorti edilir',
            'D': 'Parçaların ortalama faydalı ömrü kullanılır',
            'E': 'Parçalar ayrıştırılmaz; tek bir oran uygulanır',
        },
        'B',
        'TMS 16 par. 43-44: bir maddi duran varlık kaleminin toplam maliyetine göre önemli olan her parçası ayrı ayrı amortismana tabi tutulur. Bu, bileşen (parça) yaklaşımı olarak adlandırılır.',
    ),
    'std-tms16-gen-0020': std_patch(
        "Bir işletme, yalnızca kendi üretim makinesinde kullanılabilen ve birden fazla dönem kullanılması beklenen 180.000 ₺'lik yedek parçayı stoklarında izlemektedir. TMS 16'ya göre bu kalem nasıl ele alınır?",
        {
            'A': 'Maddi duran varlık olarak muhasebeleştirilir ve amortismana tabi tutulur',
            'B': 'Stok olarak izlenir ve kullanıldığında gider yazılır; kullanım süresi ölçüt olarak dikkate alınmaz',
            'C': 'Doğrudan dönem gideri olarak muhasebeleştirilir',
            'D': 'Maddi olmayan duran varlık olarak muhasebeleştirilir',
            'E': 'Yalnızca dipnotta açıklanır, tabloya alınmaz',
        },
        'A',
        'TMS 16 par. 8: yedek parçalar ve donanım malzemeleri genellikle stok olarak izlenir ve kullanıldıkça gider yazılır. Ancak maddi duran varlık tanımını karşılayan, yani birden fazla dönem kullanılması beklenen önemli yedek parçalar maddi duran varlık olarak muhasebeleştirilir ve amortismana tabi tutulur.',
    ),
    'std-tms16-gen-0023': std_patch(
        "TMS 16'ya göre amortisman neyi ifade eder?",
        {
            'A': 'Varlığın piyasa değerindeki düşüşün kayda alınmasını',
            'B': 'Varlığın yenilenmesi için ayrılan nakit fonu',
            'C': 'Varlığın vergi matrahından indirilen tutarı',
            'D': 'Varlığın gerçeğe uygun değeriyle defter değeri arasındaki farkın dönem sonunda kayda alınmasını',
            'E': 'Amortismana tabi tutarın varlığın faydalı ömrü boyunca sistematik olarak dağıtılmasını',
        },
        'E',
        'TMS 16 par. 6: amortisman, bir varlığın amortismana tabi tutarının faydalı ömrü boyunca sistematik olarak dağıtılmasıdır. Değer düşüklüğünden ve nakit fon ayırmaktan farklıdır.',
    ),
    'std-tms16-gen-0024': std_patch(
        'Amortismana tabi tutar nasıl bulunur?',
        {
            'A': 'Varlığın maliyetinden birikmiş amortismanın düşülmesiyle',
            'B': 'Varlığın maliyetinden kalıntı değerinin düşülmesiyle',
            'C': 'Varlığın gerçeğe uygun değerinden maliyetinin düşülmesiyle',
            'D': 'Varlığın maliyetine kalıntı değerinin eklenmesiyle',
            'E': 'Varlığın net defter değerinden değer düşüklüğünün düşülmesiyle',
        },
        'B',
        'TMS 16 par. 6: amortismana tabi tutar, bir varlığın maliyetinden veya maliyet yerine geçen diğer tutarlardan kalıntı değerin düşülmesiyle bulunur.',
    ),
    'std-tms16-gen-0025': std_patch(
        'Amortisman ayrılmaya ne zaman başlanır?',
        {
            'A': 'Varlık fiilen üretimde kullanılmaya başlandığında',
            'B': 'Varlığın faturası ödendiğinde',
            'C': 'Varlık işletmeye teslim edildiğinde',
            'D': 'Varlık kullanıma hazır hâle geldiğinde',
            'E': 'İzleyen hesap döneminin başında',
        },
        'D',
        'TMS 16 par. 55: amortisman, varlık kullanıma hazır olduğunda — yani yönetimin amaçladığı biçimde çalışabilmesi için gereken konum ve duruma geldiğinde — başlar. Fiilen kullanılmaya başlanması beklenmez.',
    ),
    'std-tms16-gen-0026': std_patch(
        'Boş duran ve fiilen kullanılmayan bir maddi duran varlık için ne yapılır?',
        {
            'A': 'Amortisman durdurulur ve varlık maliyetle taşınır',
            'B': 'Amortisman yarı oranda ayrılır',
            'C': 'Varlık stok hesabına aktarılır',
            'D': 'Varlık için değer düşüklüğü karşılığı ayrılır',
            'E': 'Amortisman ayrılmaya devam edilir',
        },
        'E',
        'TMS 16 par. 55: varlık kullanımdan kaldırılmadıkça veya bilanço dışı bırakılmadıkça, atıl kaldığı dönemlerde de amortisman ayrılmaya devam edilir. Yalnızca üretim miktarı yöntemi uygulanıyorsa üretim olmadığı için amortisman tutarı sıfır olabilir.',
    ),
    'std-tms16-gen-0028': std_patch(
        "Aşağıdakilerden hangisi TMS 16'ya göre kabul edilen bir amortisman yöntemi değildir?",
        {
            'A': 'Normal (doğrusal) amortisman yöntemi; amortismana tabi tutar ömre eşit dağıtılır',
            'B': 'Varlığın kullanımından elde edilen hasılata dayalı yöntem',
            'C': 'Azalan bakiyeler yöntemi',
            'D': 'Üretim miktarı yöntemi',
            'E': 'Kalan ömür toplamı yöntemi',
        },
        'B',
        'TMS 16 par. 62A: varlığın kullanımını içeren bir faaliyetten elde edilen hasılata dayalı amortisman yöntemi uygun değildir; çünkü hasılat, varlığın ekonomik yararının tüketilme biçimini değil satış fiyatı ve hacim gibi başka etkenleri yansıtır.',
    ),
    'std-tms16-gen-0029': std_patch(
        'Amortisman yöntemi ne sıklıkla gözden geçirilir ve değişiklik nasıl uygulanır?',
        {
            'A': 'İlk seçimden sonra değiştirilemez',
            'B': 'Beş yılda bir gözden geçirilir; değişiklik geriye dönük uygulanarak geçmiş dönemler düzeltilir',
            'C': 'Yalnızca varlık satıldığında gözden geçirilir',
            'D': 'Her dönem gözden geçirilir; değişiklik geriye dönük uygulanır',
            'E': 'En az her hesap dönemi sonunda gözden geçirilir; değişiklik ileriye dönük uygulanır',
        },
        'E',
        'TMS 16 par. 61: amortisman yöntemi en az her hesap dönemi sonunda gözden geçirilir. Beklenen tüketim biçiminde önemli değişiklik varsa yöntem değiştirilir ve bu, TMS 8 uyarınca muhasebe tahmini değişikliği olarak ileriye dönük uygulanır.',
    ),
    'std-tms16-gen-0030': std_patch(
        'Faydalı ömür ve kalıntı değer ne sıklıkla gözden geçirilir ve değişiklik nasıl uygulanır?',
        {
            'A': 'Yalnızca varlık satıldığında gözden geçirilir',
            'B': 'Beş yılda bir gözden geçirilir; değişiklik geriye dönük uygulanır',
            'C': 'İlk muhasebeleştirmede belirlenir ve sonradan değiştirilemez',
            'D': 'En az her hesap dönemi sonunda gözden geçirilir; değişiklik ileriye dönük uygulanır',
            'E': 'Her dönem gözden geçirilir; değişiklik geriye dönük uygulanır',
        },
        'D',
        'TMS 16 par. 51: kalıntı değer ve faydalı ömür en az her hesap dönemi sonunda gözden geçirilir. Beklentilerde farklılık varsa değişiklik TMS 8 uyarınca muhasebe tahmini değişikliği olarak ileriye dönük muhasebeleştirilir; geçmiş dönemler düzeltilmez.',
    ),
    'std-tms16-gen-0031': std_patch(
        'Bir varlığın kalıntı değeri defter değerine eşit ya da ondan büyük hâle gelirse ne olur?',
        {
            'A': 'Amortisman ayrılmaya aynı tutarla devam edilir',
            'B': 'Amortisman gideri sıfır olur; kalıntı değer defter değerinin altına düşene kadar bu böyle sürer',
            'C': 'Varlık doğrudan bilanço dışı bırakılır',
            'D': 'Aradaki fark kâr olarak kaydedilir',
            'E': 'Kalıntı değer sıfıra indirilerek amortisman ömür sonuna kadar aynı tutarla sürdürülür',
        },
        'B',
        'TMS 16 par. 54: bir varlığın kalıntı değeri defter değerine eşit veya ondan büyükse amortisman gideri sıfırdır. Kalıntı değer sonradan defter değerinin altına düşerse amortisman ayrılmasına yeniden başlanır.',
    ),
    'std-tms16-gen-0032': std_patch(
        "Aşağıdakilerden hangisi TMS 16'ya göre amortismana tabi tutulmaz?",
        {
            'A': 'Sınırsız faydalı ömre sahip arazi',
            'B': 'Arazi üzerinde bulunan bina',
            'C': 'Üretimde kullanılan makine',
            'D': 'İşletmenin kullandığı taşıtlar',
            'E': 'Ofiste kullanılan demirbaşlar',
        },
        'A',
        'TMS 16 par. 58: arazi ve binalar birlikte edinilse dahi ayrılabilir varlıklardır ve ayrı muhasebeleştirilir. Arazinin faydalı ömrü sınırsız kabul edildiğinden amortismana tabi tutulmaz; taş ocağı ve dolgu alanı gibi sınırlı ömürlü araziler bunun istisnasıdır.',
    ),
    'std-tms16-gen-0033': std_patch(
        "Bir işletme 1 Nisan 2024'te 1.200.000 ₺ maliyetle bir makine edinmiştir. Makinenin faydalı ömrü 8 yıl, kalıntı değeri 240.000 ₺ olup normal (doğrusal) amortisman yöntemi uygulanmaktadır. 31 Aralık 2025 tarihli finansal durum tablosunda görünecek birikmiş amortisman tutarı kaç ₺'dir?",
        {
            'A': '240.000 ₺',
            'B': '210.000 ₺',
            'C': '150.000 ₺',
            'D': '262.500 ₺',
            'E': '300.000 ₺',
        },
        'B',
        "Yıllık amortisman: (1.200.000 − 240.000) / 8 = 120.000 ₺. TMS 16 par. 55 uyarınca amortisman varlığın kullanıma hazır olduğu tarihte başlar; 2024'te 9 ay için 120.000 × 9/12 = 90.000 ₺, 2025'te tam yıl 120.000 ₺ ayrılır. Birikmiş amortisman 90.000 + 120.000 = 210.000 ₺.",
    ),
    'std-tms16-gen-0034': std_patch(
        "Maliyeti 900.000 ₺, kalıntı değeri 100.000 ₺ olan bir makinenin toplam üretim kapasitesi 400.000 birimdir. Makine ilk yıl 60.000 birim, ikinci yıl 90.000 birim üretmiştir. Üretim miktarı yöntemine göre ikinci yıl sonundaki birikmiş amortisman kaç ₺'dir?",
        {
            'A': '300.000 ₺',
            'B': '337.500 ₺',
            'C': '180.000 ₺',
            'D': '120.000 ₺',
            'E': '225.000 ₺',
        },
        'A',
        'Amortismana tabi tutar: 900.000 − 100.000 = 800.000 ₺. Birim başına amortisman 800.000 / 400.000 = 2 ₺. İlk yıl 60.000 × 2 = 120.000 ₺, ikinci yıl 90.000 × 2 = 180.000 ₺. Birikmiş amortisman 120.000 + 180.000 = 300.000 ₺ (TMS 16 par. 62).',
    ),
    'std-tms16-gen-0035': std_patch(
        "Bir işletme 1 Ocak 2023'te 800.000 ₺ maliyetle, faydalı ömrü 5 yıl olan ve kalıntı değeri bulunmayan bir makine almıştır. Makineye ilk iki yıl %40 oranında azalan bakiyeler yöntemine göre amortisman ayrılmış, 2025 yılından itibaren normal (doğrusal) yönteme geçilmesine karar verilmiştir. 2025 yılının amortisman gideri kaç ₺'dir?",
        {
            'A': '160.000 ₺',
            'B': '115.200 ₺',
            'C': '96.000 ₺',
            'D': '192.000 ₺',
            'E': '144.000 ₺',
        },
        'C',
        "2023: 800.000 × %40 = 320.000 ₺, net defter değeri 480.000 ₺. 2024: 480.000 × %40 = 192.000 ₺, net defter değeri 288.000 ₺. 2025'ten itibaren doğrusal yönteme geçilir; kalan faydalı ömür 3 yıldır: 288.000 / 3 = 96.000 ₺. TMS 16 par. 61: amortisman yöntemi değişikliği bir muhasebe tahmini değişikliğidir ve ileriye dönük uygulanır; geçmiş yıllar düzeltilmez.",
    ),
    'std-tms16-gen-0041': std_patch(
        'İlk muhasebeleştirme sonrasında maddi duran varlıklar için hangi ölçüm modelleri uygulanabilir?',
        {
            'A': 'Maliyet modeli veya yeniden değerleme modeli',
            'B': 'Yalnızca maliyet modeli',
            'C': 'Yalnızca yeniden değerleme modeli',
            'D': 'Maliyet modeli veya net gerçekleşebilir değer modeli',
            'E': 'Gerçeğe uygun değer modeli veya özkaynak yöntemi',
        },
        'A',
        'TMS 16 par. 29: işletme muhasebe politikası olarak maliyet modelini ya da yeniden değerleme modelini seçer ve bu politikayı ilgili maddi duran varlık sınıfının tamamına uygular.',
    ),
    'std-tms16-gen-0042': std_patch(
        'Yeniden değerleme modeli seçildiğinde uygulama kapsamı ne olur?',
        {
            'A': 'Yalnızca değeri artan varlıklara uygulanır',
            'B': 'İşletmenin seçtiği tek tek varlıklara uygulanır',
            'C': 'Tüm maddi duran varlık sınıflarına birlikte uygulanır; sınıf bazında seçim yapılamaz',
            'D': 'Yalnızca binalara uygulanır',
            'E': 'Varlığın ait olduğu maddi duran varlık sınıfının tamamına uygulanır',
        },
        'E',
        'TMS 16 par. 36-38: bir maddi duran varlık yeniden değerlendiğinde, ait olduğu sınıfın tamamı yeniden değerlenir. Bu, seçmeli değerleme yapılmasını ve farklı tarihli tutarların bir arada raporlanmasını önler.',
    ),
    'std-tms16-gen-0043': std_patch(
        'Maliyet modelinde bir maddi duran varlık hangi tutarla gösterilir?',
        {
            'A': 'Maliyetinden birikmiş amortisman ve birikmiş değer düşüklüğü zararları düşülerek',
            'B': 'Maliyet bedeliyle, hiçbir indirim yapılmadan',
            'C': 'Gerçeğe uygun değerinden birikmiş amortisman düşülerek',
            'D': 'Yeniden değerlenmiş tutarından birikmiş amortisman ve değer düşüklüğü düşülerek',
            'E': 'Net gerçekleşebilir değeriyle',
        },
        'A',
        'TMS 16 par. 30: maliyet modelinde maddi duran varlık, maliyetinden birikmiş amortisman ve birikmiş değer düşüklüğü zararları indirildikten sonraki değeriyle gösterilir.',
    ),
    'std-tms16-gen-0045': std_patch(
        'Yeniden değerleme ne sıklıkla yapılır?',
        {
            'A': 'Her hesap döneminde bir kez yapılır; gerçeğe uygun değerdeki değişimin hızı ölçüt alınmaz',
            'B': 'Beş yılda bir',
            'C': 'Yalnızca işletme yönetimi talep ettiğinde',
            'D': 'Defter değeri gerçeğe uygun değerden önemli ölçüde farklılaşmayacak sıklıkta',
            'E': 'Yalnızca varlık satışa çıkarıldığında',
        },
        'D',
        'TMS 16 par. 34: yeniden değerlemenin sıklığı gerçeğe uygun değerdeki değişimlere bağlıdır. Önemli ve dalgalı değişim gösteren varlıklarda yıllık, önemsiz değişim gösterenlerde üç-beş yılda bir yeniden değerleme yeterli olabilir.',
    ),
    'std-tms16-gen-0046': std_patch(
        'Yeniden değerleme sonucu bir varlığın defter değeri artarsa artış nereye yansıtılır?',
        {
            'A': 'Doğrudan dönemin kâr veya zararına',
            'B': 'Doğrudan geçmiş yıllar kârlarına',
            'C': 'İlgili varlığın birikmiş amortismanına; böylece net defter değeri değişmeden kalır',
            'D': 'Ertelenmiş gelir olarak yükümlülüklere',
            'E': 'Diğer kapsamlı gelire; özkaynakta yeniden değerleme fazlası olarak biriktirilir',
        },
        'E',
        'TMS 16 par. 39: yeniden değerleme sonucu defter değeri artarsa artış diğer kapsamlı gelirde muhasebeleştirilir ve özkaynakta yeniden değerleme fazlası adıyla biriktirilir. Aynı varlık için daha önce kâr veya zarara yazılmış bir azalışı tersine çevirdiği ölçüde ise kâr veya zarara yansıtılır.',
    ),
    'std-tms16-gen-0048': std_patch(
        'Yeniden değerleme sonucu bir varlığın defter değeri azalırsa azalış nereye yansıtılır?',
        {
            'A': 'Her durumda doğrudan kâr veya zarara; önceki yeniden değerleme fazlası dikkate alınmaz',
            'B': 'Her durumda diğer kapsamlı gelire',
            'C': 'Doğrudan geçmiş yıllar kârlarına',
            'D': 'İlgili varlığın maliyet bedeline',
            'E': 'Kâr veya zarara; ancak o varlığa ilişkin yeniden değerleme fazlası varsa önce ondan düşülür',
        },
        'E',
        'TMS 16 par. 40: yeniden değerleme sonucu defter değeri azalırsa azalış kâr veya zararda muhasebeleştirilir. Ancak o varlıkla ilgili yeniden değerleme fazlasında alacak bakiyesi bulunduğu ölçüde azalış önce diğer kapsamlı gelire kaydedilir ve fazlayı azaltır.',
    ),
    'std-tms16-gen-0049': std_patch(
        "Bir binanın maliyet bedeli 1.000.000 ₺, birikmiş amortismanı 400.000 ₺'dir. İşletme yeniden değerleme modeline geçmiş ve binanın yeniden değerleme tarihindeki gerçeğe uygun değerini 750.000 ₺ olarak belirlemiştir. Bina için daha önce kâr veya zarara yazılmış bir değer azalışı bulunmadığına göre TMS 16'ya göre kaydedilecek tutar ve yeri aşağıdakilerden hangisidir?",
        {
            'A': '150.000 ₺ diğer kapsamlı gelirde yeniden değerleme fazlası olarak',
            'B': '150.000 ₺ dönemin kâr veya zararında gelir olarak',
            'C': '250.000 ₺ diğer kapsamlı gelirde yeniden değerleme fazlası olarak',
            'D': '350.000 ₺ diğer kapsamlı gelirde yeniden değerleme fazlası olarak',
            'E': '150.000 ₺ doğrudan geçmiş yıllar kârlarına aktarılarak',
        },
        'A',
        "Net defter değeri: 1.000.000 − 400.000 = 600.000 ₺. Gerçeğe uygun değer 750.000 ₺ olduğundan artış 150.000 ₺'dir. TMS 16 par. 39: defter değerinin yeniden değerleme sonucu artması hâlinde artış diğer kapsamlı gelirde muhasebeleştirilir ve özkaynakta yeniden değerleme fazlası olarak biriktirilir. Daha önce kâr veya zarara yazılmış bir azalış bulunmadığından tutarın tamamı diğer kapsamlı gelire alınır.",
    ),
    'std-tms16-gen-0050': std_patch(
        'Özkaynakta biriken yeniden değerleme fazlası nasıl aktarılabilir?',
        {
            'A': 'Kâr veya zarara gelir olarak aktarılır',
            'B': 'Diğer kapsamlı gelirde bırakılır ve varlık elden çıkarılsa dahi aktarılamaz',
            'C': 'Sermayeye eklenerek kâr veya zarara yansıtılır',
            'D': 'Doğrudan geçmiş yıllar kârlarına aktarılır; kâr veya zarardan geçirilmez',
            'E': 'İlgili varlığın maliyetinden düşülür',
        },
        'D',
        'TMS 16 par. 41: yeniden değerleme fazlası, varlık bilanço dışı bırakıldığında ya da varlık kullanıldıkça (yeniden değerlenmiş amortisman ile orijinal maliyet üzerinden amortisman arasındaki fark kadar) doğrudan geçmiş yıllar kârlarına aktarılabilir. Aktarım kâr veya zarardan geçmez.',
    ),
    'std-tms16-gen-0051': std_patch(
        'Bir maddi duran varlık hangi durumda finansal durum tablosu dışı bırakılır?',
        {
            'A': 'Elden çıkarıldığında ya da kullanımından gelecekte ekonomik yarar beklenmediğinde',
            'B': 'Yalnızca satıldığında',
            'C': 'Yalnızca tamamen amorti edildiğinde',
            'D': 'Yalnızca faydalı ömrü dolduğunda',
            'E': 'Yalnızca değer düşüklüğüne uğradığında; gelecekte yarar beklentisinin kalmaması yeterli değildir',
        },
        'A',
        'TMS 16 par. 67: maddi duran varlık kalemi elden çıkarıldığında veya kullanımından ya da elden çıkarılmasından gelecekte ekonomik yarar beklenmediğinde bilanço dışı bırakılır. Tamamen amorti edilmiş olması tek başına yeterli değildir.',
    ),
    'std-tms16-gen-0053': std_patch(
        "Maliyeti 400.000 ₺ ve birikmiş amortismanı 250.000 ₺ olan bir makine 180.000 ₺'ye satılmış, satış için 5.000 ₺ komisyon ödenmiştir. TMS 16'ya göre finansal tablolara yansıyacak sonuç aşağıdakilerden hangisidir?",
        {
            'A': '30.000 ₺ kazanç; kâr veya zararda gösterilir',
            'B': '180.000 ₺ hasılat; satış gelirleri içinde gösterilir ve komisyon pazarlama gideri yazılır',
            'C': '25.000 ₺ kazanç; diğer kapsamlı gelirde gösterilir',
            'D': '25.000 ₺ kazanç; kâr veya zararda gösterilir ve hasılat olarak sınıflandırılmaz',
            'E': '20.000 ₺ zarar; kâr veya zararda gösterilir',
        },
        'D',
        'Net defter değeri: 400.000 − 250.000 = 150.000 ₺. Net tahsilat: 180.000 − 5.000 = 175.000 ₺. Kazanç 175.000 − 150.000 = 25.000 ₺. TMS 16 par. 68 ve 71: bilanço dışı bırakmadan doğan kazanç kâr veya zarara yansıtılır, ancak hasılat olarak sınıflandırılmaz.',
    ),
    'std-tms16-gen-0054': std_patch(
        "Maliyeti 700.000 ₺ ve birikmiş amortismanı 400.000 ₺ olan, yeniden değerleme modeline göre izlenen bir taşıt 260.000 ₺'ye satılmıştır. Taşıta ilişkin özkaynakta biriken yeniden değerleme fazlası 50.000 ₺'dir. TMS 16'ya göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': '10.000 ₺ kazanç kâr veya zarara yansıtılır',
            'B': '40.000 ₺ zarar kâr veya zarara yansıtılır; 50.000 ₺ fazla doğrudan geçmiş yıllar kârlarına aktarılabilir',
            'C': '40.000 ₺ zarar önce yeniden değerleme fazlasından düşülür; kalan tutar kâr veya zarara yansıtılır',
            'D': '40.000 ₺ zarar diğer kapsamlı gelire yansıtılır',
            'E': '90.000 ₺ zarar kâr veya zarara yansıtılır',
        },
        'B',
        'Net defter değeri: 700.000 − 400.000 = 300.000 ₺. Satış bedeli 260.000 ₺ olduğundan 40.000 ₺ zarar doğar ve TMS 16 par. 68 uyarınca kâr veya zarara yansıtılır. Par. 41: varlık bilanço dışı bırakıldığında yeniden değerleme fazlası doğrudan geçmiş yıllar kârlarına aktarılabilir; bu aktarım kâr veya zarardan geçmez ve satış sonucunu değiştirmez.',
    ),
    'std-tms16-gen-0057': std_patch(
        'Maddi duran varlıklarda değer düşüklüğü hangi standarda göre belirlenir?',
        {
            'A': "TMS 16'nın kendi hükümlerine göre",
            'B': "TMS 2 Stoklar'a göre",
            'C': "TMS 36 Varlıklarda Değer Düşüklüğü'ne göre",
            'D': "TFRS 13 Gerçeğe Uygun Değer Ölçümü'ne göre",
            'E': "TMS 37 Karşılıklar'a göre",
        },
        'C',
        'TMS 16 par. 63: bir maddi duran varlık kaleminin değer düşüklüğüne uğrayıp uğramadığının belirlenmesinde TMS 36 uygulanır. TFRS 13 yalnızca gerçeğe uygun değerin nasıl ölçüleceğini düzenler.',
    ),
    'std-tms16-gen-0060': std_patch(
        "Aşağıdakilerden hangisinin TMS 16'ya göre dipnotlarda açıklanması gerekli değildir?",
        {
            'A': 'Brüt defter değerinin belirlenmesinde kullanılan ölçüm esasları',
            'B': 'Kullanılan amortisman yöntemleri ile faydalı ömürler veya amortisman oranları',
            'C': 'Varlıkların satın alındığı tedarikçilerin ticaret unvanları',
            'D': 'Dönem başı ve dönem sonu brüt defter değeri ile birikmiş amortisman tutarı',
            'E': 'Dönem içindeki girişler, elden çıkarmalar ve değer düşüklüğü zararları',
        },
        'C',
        'TMS 16 par. 73: açıklanacaklar; ölçüm esasları, amortisman yöntemleri, faydalı ömürler veya oranlar, dönem başı ve sonu brüt defter değeri ile birikmiş amortisman ve dönem içi hareketlerin mutabakatıdır. Tedarikçi unvanları standartta yer almaz.',
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
            fark.append(f"{path}::{q['id']} TL→₺")
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
    print(f"1 paket / {len(PATCHES)} soru (TMS 16 bicim kalibrasyonu) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
