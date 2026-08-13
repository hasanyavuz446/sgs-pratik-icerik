#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TMS 7, TMS 8 ve TMS 38 - çıkmış sınav biçim kalibrasyonu.

⚠️ tms7-0049'un doğru şıkkındaki "hiçbir şekilde" pekiştireci kaldırıldı:
``fix_lexical_tell.py`` bu paketin de sahibi ve o kalıbı temizliyor; iki
builder aynı metne yazınca ``--check`` çakışıyordu. İddia olumsuz köklü
soruda zaten yanlış olduğu için sadeleşme anlamı değiştirmez.

Kapsam mevcut hâliyle güçlüydü; bu tur seri üretim izlerini temizler:

* ``... bakımından aşağıdakilerden hangisi doğrudur?`` kökleri konuya özgü,
  kısa ve doğal köklere dönüştürülür.
* Her pakete gerçek sınavda görülen olumsuz kök ve uygulama senaryoları eklenir.
* TMS 38'e maliyet modeliyle defter değeri hesabı eklenir.
* Eski ``TL`` gösterimi ``₺`` yapılır ve çözüm sonundaki mekanik
  ``Doğru cevap X.`` cümlesi kaldırılır.

Kalibrasyon kaynakları:

* 2014-2026 SGS çıkmış sınav arşivi (yalnız biçim/kazanım ölçümü)
* KGK TFRS 2026 Seti: TMS 7, TMS 8 ve TMS 38

Sorular özgündür; çıkmış soru metni kopyalanmaz.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
LESSON = "muhasebe_standartlari"
TOPICS = ("tms_7_nakit_akis", "tms_8_politikalar", "tms_38_modv")
TL = re.compile(r"(\d)\s*TL\b")
TL_WORD = re.compile(r"\bTL\b")
ANSWER_TAIL = re.compile(r"\s*Doğru\s+(?:cevap|seçenek)\s+[A-E]\.\s*$")


STEMS = {
    "tms_7_nakit_akis": {
        "std-tms7-gen-0001": "TMS 7'nin temel amacı aşağıdakilerden hangisidir?",
        "std-tms7-gen-0002": "Nakit akış tablosu kullanıcılara öncelikle hangi değerlendirmeyi yapma imkânı verir?",
        "std-tms7-gen-0003": "Aşağıdaki nakit ve nakit benzeri tanımlarından hangisi TMS 7'ye uygundur?",
        "std-tms7-gen-0004": "Bir yatırımın nakit benzeri sayılabilmesi için hangi amaçla elde tutulması gerekir?",
        "std-tms7-gen-0005": "Özkaynağa dayalı bir finansal araç hangi durumda nakit benzeri kabul edilebilir?",
        "std-tms7-gen-0006": "Vadesiz hesaba bağlı ve bakiyesi sık sık artı-eksi arasında değişen borçlu cari hesap nasıl sınıflandırılabilir?",
        "std-tms7-gen-0007": "Kasadaki paranın vadesiz mevduata yatırılması nakit akış tablosunda nasıl gösterilir?",
        "std-tms7-gen-0008": "Nakit akışları hangi üç faaliyet grubunda raporlanır?",
        "std-tms7-gen-0009": "Esas faaliyetler TMS 7'de nasıl tanımlanır?",
        "std-tms7-gen-0011": "Özkaynak ve borçlanma yapısını değiştiren nakit akışları hangi faaliyet grubunda raporlanır?",
        "std-tms7-gen-0013": "Mal ve hizmet satışından doğan nakit tahsilatları hangi faaliyet grubunda yer alır?",
        "std-tms7-gen-0014": "Stok tedarikçilerine yapılan nakit ödemeler nasıl sınıflandırılır?",
        "std-tms7-gen-0015": "Üretimde kullanılacak bir makine için yapılan nakit ödeme hangi faaliyet grubundadır?",
        "std-tms7-gen-0016": "Kullanılmış bir maddi duran varlığın satışından sağlanan nakit nasıl sınıflandırılır?",
        "std-tms7-gen-0017": "Pay ihracından sağlanan nakit hangi faaliyet grubunda raporlanır?",
        "std-tms7-gen-0018": "Kredi alınması ve kredi anaparasının geri ödenmesi nakit akış tablosunda nasıl gösterilir?",
        "std-tms7-gen-0019": "Faiz ve kâr payı nakit akışlarının sınıflandırılmasında hangi ilke uygulanır?",
        "std-tms7-gen-0020": "Gelir üzerinden alınan vergilere ilişkin nakit ödemeler kural olarak hangi faaliyet grubundadır?",
        "std-tms7-gen-0021": "Ortaklara ödenen kâr payları TMS 7'ye göre nasıl sınıflandırılabilir?",
        "std-tms7-gen-0023": "Borcu pay vererek özkaynağa dönüştüren işletme bu işlemi nasıl raporlar?",
        "std-tms7-gen-0024": "Yabancı para cinsinden bir nakit akışı hangi kurla çevrilir?",
        "std-tms7-gen-0029": "Esas faaliyetlerden kaynaklanan nakit akışları hangi yöntemlerle sunulabilir?",
        "std-tms7-gen-0031": "Dolaylı yöntemde esas faaliyet nakit akışına hangi tutardan başlanır?",
        "std-tms7-gen-0032": "Dolaylı yöntemde amortisman gideri dönem kârına nasıl yansıtılır?",
        "std-tms7-gen-0033": "Ticari alacaklardaki artış dolaylı yöntem hesabını nasıl etkiler?",
        "std-tms7-gen-0034": "Ticari borçlardaki artış dolaylı yöntem hesabını nasıl etkiler?",
        "std-tms7-gen-0035": "Maddi duran varlık satış kârı dolaylı yöntemde dönem kârına nasıl uygulanır?",
        "std-tms7-gen-0041": "Yatırım ve finansman faaliyetlerindeki nakit giriş ve çıkışları için genel sunum kuralı hangisidir?",
    },
    "tms_8_politikalar": {
        "std-tms8-gen-0001": "TMS 8'e göre muhasebe politikası aşağıdakilerden hangisidir?",
        "std-tms8-gen-0002": "Bir işlemi özel olarak düzenleyen TFRS bulunduğunda muhasebe politikası nasıl belirlenir?",
        "std-tms8-gen-0003": "Bir işlem için doğrudan uygulanabilir TFRS bulunmuyorsa yönetim ne yapar?",
        "std-tms8-gen-0004": "Yönetim, muhasebe politikası geliştirirken kaynaklara hangi sırayla başvurur?",
        "std-tms8-gen-0005": "TFRS'lerle çelişmemek koşuluyla politika geliştirmede hangi ek kaynaklardan yararlanılabilir?",
        "std-tms8-gen-0006": "Benzer işlem ve olaylara ilişkin muhasebe politikaları nasıl uygulanır?",
        "std-tms8-gen-0007": "Bir TFRS farklı kalem grupları için ayrı politika kullanılmasına izin veriyorsa ne yapılır?",
        "std-tms8-gen-0009": "Önemli muhasebe politikalarına ilişkin açıklamalar nerede sunulur?",
        "std-tms8-gen-0014": "Muhasebe politikalarının tutarlı seçimi finansal tablo bilgisini nasıl etkiler?",
        "std-tms8-gen-0016": "Muhasebe politikası değişikliği kural olarak hangi yönde uygulanır?",
        "std-tms8-gen-0017": "Geriye dönük uygulama ne anlama gelir?",
        "std-tms8-gen-0018": "Politika değişikliğinde sunulan en erken dönemin açılış bakiyelerine ne yapılır?",
        "std-tms8-gen-0019": "İlk kez uygulanan bir TFRS özel geçiş hükümleri içeriyorsa hangi yol izlenir?",
        "std-tms8-gen-0020": "İlk kez uygulanan TFRS'de geçiş hükmü yoksa değişiklik nasıl muhasebeleştirilir?",
        "std-tms8-gen-0022": "Daha önce gerçekleşmemiş bir işlem için ilk defa politika belirlenmesi nasıl değerlendirilir?",
        "std-tms8-gen-0023": "Politika değişikliğinin geçmiş dönem etkisi güvenilir biçimde belirlenemiyorsa ne yapılır?",
        "std-tms8-gen-0024": "TMS 8'de 'uygulanabilir olmama' hangi durumu ifade eder?",
        "std-tms8-gen-0026": "Bir muhasebe politikası değişikliğine ilişkin hangi bilgiler açıklanır?",
        "std-tms8-gen-0029": "TMS 8'e göre muhasebe tahmini aşağıdakilerden hangisidir?",
        "std-tms8-gen-0030": "Muhasebe tahminindeki değişiklik hangi yönde uygulanır?",
        "std-tms8-gen-0031": "Yeni bilgi nedeniyle tahminin revize edilmesi nasıl değerlendirilir?",
        "std-tms8-gen-0032": "Bir değişikliğin politika mı tahmin mi olduğu ayırt edilemiyorsa nasıl işlem yapılır?",
        "std-tms8-gen-0033": "Maddi duran varlığın faydalı ömrünün değiştirilmesi hangi tür değişikliktir?",
        "std-tms8-gen-0034": "Amortisman yönteminin değiştirilmesi nasıl muhasebeleştirilir?",
        "std-tms8-gen-0035": "Şüpheli alacak karşılığının yeni bilgilerle güncellenmesi hangi tür değişikliktir?",
        "std-tms8-gen-0036": "Muhasebe tahmininde kullanılan girdiler nasıl seçilir?",
        "std-tms8-gen-0037": "Tahmin değişikliği gelecek dönemleri de etkiliyorsa etkiler hangi dönemlerde kaydedilir?",
        "std-tms8-gen-0038": "Muhasebe tahmini değişikliğinin finansal etkisi nasıl açıklanır?",
    },
    "tms_38_modv": {
        "std-tms38-gen-0002": "Maddi olmayan duran varlık tanımının üç temel unsuru hangileridir?",
        "std-tms38-gen-0003": "Bir maddi olmayan duran varlık hangi durumda tanımlanabilir kabul edilir?",
        "std-tms38-gen-0004": "Maddi olmayan duran varlık üzerindeki kontrol neyi ifade eder?",
        "std-tms38-gen-0005": "Nitelikli personel ekibi neden genellikle maddi olmayan duran varlık sayılmaz?",
        "std-tms38-gen-0006": "Bir maddi olmayan duran varlığın muhasebeleştirilmesi için hangi iki ölçüt birlikte sağlanmalıdır?",
        "std-tms38-gen-0007": "Maddi olmayan duran varlık ilk muhasebeleştirmede hangi değerle ölçülür?",
        "std-tms38-gen-0008": "İşletme birleşmesinde edinilen tanımlanabilir maddi olmayan duran varlık nasıl ölçülür?",
        "std-tms38-gen-0009": "Devlet teşvikiyle bedelsiz veya düşük bedelle edinilen maddi olmayan duran varlık nasıl ölçülebilir?",
        "std-tms38-gen-0010": "Ayrı olarak edinilen maddi olmayan duran varlığın maliyetine hangi unsurlar girer?",
        "std-tms38-gen-0015": "İşletme içinde yaratılan şerefiye finansal tablolara alınır mı?",
        "std-tms38-gen-0016": "İşletme içinde yaratılan marka ve müşteri listeleri nasıl muhasebeleştirilir?",
        "std-tms38-gen-0017": "Araştırma safhasında yapılan harcamalar nasıl muhasebeleştirilir?",
        "std-tms38-gen-0018": "Geliştirme safhasındaki harcamalar hangi durumda aktifleştirilir?",
        "std-tms38-gen-0019": "Geliştirme harcamasının aktifleştirilmesi için hangi koşulların sağlanması gerekir?",
        "std-tms38-gen-0020": "Daha önce gider yazılan bir geliştirme harcaması sonradan aktifleştirilebilir mi?",
        "std-tms38-gen-0021": "Araştırma ve geliştirme safhaları ayırt edilemiyorsa harcamalar nasıl ele alınır?",
        "std-tms38-gen-0030": "Maddi olmayan duran varlığın faydalı ömrü nasıl belirlenir?",
        "std-tms38-gen-0031": "Sınırsız faydalı ömürlü maddi olmayan duran varlık nasıl muhasebeleştirilir?",
        "std-tms38-gen-0032": "'Sınırsız faydalı ömür' ifadesi ne anlama gelir?",
        "std-tms38-gen-0033": "Sınırsız faydalı ömür değerlendirmesi ne sıklıkla gözden geçirilir?",
        "std-tms38-gen-0034": "Sınırlı faydalı ömürlü maddi olmayan duran varlık için itfa nasıl hesaplanır?",
        "std-tms38-gen-0035": "Maddi olmayan duran varlık için itfa ayırmaya ne zaman başlanır?",
        "std-tms38-gen-0036": "Maddi olmayan duran varlığın kalıntı değeri kural olarak kaç kabul edilir?",
        "std-tms38-gen-0037": "İtfa süresi ve yöntemi ne sıklıkla gözden geçirilir?",
        "std-tms38-gen-0039": "TMS 38 kapsamında hangi itfa yöntemleri kullanılabilir?",
        "std-tms38-gen-0040": "Ekonomik yararların tüketim biçimi güvenilir ölçülemiyorsa hangi itfa yöntemi uygulanır?",
        "std-tms38-gen-0046": "İlk muhasebeleştirmeden sonra hangi ölçüm modelleri kullanılabilir?",
        "std-tms38-gen-0047": "Yeniden değerleme modelinin uygulanabilmesi için hangi piyasa koşulu gerekir?",
        "std-tms38-gen-0049": "Maddi olmayan duran varlık hangi durumda finansal tablo dışı bırakılır?",
        "std-tms38-gen-0050": "Bilanço dışı bırakmadan doğan kazanç veya kayıp nasıl muhasebeleştirilir?",
    },
}


def full(stem: str, options: dict[str, str], answer: str, solution: str, standard: str) -> dict:
    return {
        "stem": stem,
        "options": options,
        "answer": answer,
        "solution": solution,
        "source": {
            "kind": "generated",
            "styleRef": f"SGS Muhasebe Standartlari {standard}",
            "legislationRef": standard,
        },
        "validYear": 2026,
        "mockExamId": None,
    }


FULL_PATCHES = {
    "tms_7_nakit_akis": {
        "std-tms7-gen-0010": full(
            "Aşağıdakilerden hangisi TMS 7'ye göre yatırım faaliyetlerinden kaynaklanan nakit akışı DEĞİLDİR?",
            {
                "A": "Üretimde kullanılacak makinenin peşin bedeli",
                "B": "Patent edinimi için yapılan nakit ödeme",
                "C": "Finansal kuruluş olmayan işletmenin üçüncü kişiye verdiği nakit avans",
                "D": "Uzun vadeli yatırımın satışından sağlanan nakit",
                "E": "Satılmak üzere alınan stoklar için tedarikçiye yapılan ödeme",
            },
            "E",
            "TMS 7 par. 14-16 uyarınca stok tedarikçisine yapılan ödeme esas faaliyet nakit akışıdır. Makine ve patent edinimi, uzun vadeli yatırım satışı ile finansal kuruluş olmayan bir işletmenin üçüncü kişilere verdiği avanslar yatırım faaliyeti kapsamında değerlendirilir.",
            "TMS 7 Nakit Akis Tablosu",
        ),
        "std-tms7-gen-0022": full(
            "Aşağıdakilerden hangisi nakit akışı yaratmayan yatırım veya finansman işlemi DEĞİLDİR?",
            {
                "A": "Makinenin işletmenin çıkardığı paylar karşılığında edinilmesi",
                "B": "Finansal borcun özkaynağa dönüştürülmesi",
                "C": "Bir varlığın kiralama yoluyla edinilmesi",
                "D": "Üretim makinesinin bedelinin banka hesabından ödenmesi",
                "E": "Başka bir işletmenin yalnızca pay ihracı yoluyla edinilmesi",
            },
            "D",
            "TMS 7 par. 43-44: pay ihracıyla varlık edinimi, borcun özkaynağa dönüşmesi, kiralama yoluyla edinim ve pay ihracıyla işletme edinimi nakit kullanmaz; nakit akış tablosu dışında açıklanır. Makine bedelinin banka hesabından ödenmesi ise yatırım faaliyetinden nakit çıkışıdır.",
            "TMS 7 Nakit Akis Tablosu",
        ),
        "std-tms7-gen-0025": full(
            "Yabancı para nakit üzerindeki kur etkisinin sunumuna ilişkin aşağıdakilerden hangisi YANLIŞTIR?",
            {
                "A": "Kur değişiminden doğan gerçekleşmemiş fark finansman faaliyetinden nakit akışıdır",
                "B": "Kur etkisi esas, yatırım ve finansman nakit akışlarından ayrı gösterilir",
                "C": "Kur etkisi dönem başı ve dönem sonu nakdin uzlaştırılmasına dâhil edilir",
                "D": "Gerçekleşmemiş kur farkı kendi başına nakit akışı değildir",
                "E": "Yabancı para nakit akışı işlem tarihindeki kura yakın bir kurla çevrilebilir",
            },
            "A",
            "TMS 7 par. 25-28: yabancı para nakit akışları işlem tarihindeki kurla çevrilir. Kur değişiminin yabancı para nakit ve nakit benzerleri üzerindeki gerçekleşmemiş etkisi nakit akışı değildir; uzlaştırma amacıyla üç faaliyet grubundan ayrı sunulur.",
            "TMS 7 Nakit Akis Tablosu",
        ),
        "std-tms7-gen-0030": full(
            "Doğrudan yöntemle ilgili aşağıdakilerden hangisi YANLIŞTIR?",
            {
                "A": "Brüt nakit tahsilat ve ödemelerin ana grupları açıklanır",
                "B": "Gerekli bilgiler işletmenin muhasebe kayıtlarından elde edilebilir",
                "C": "Satışlar ve satışların maliyeti işletme sermayesi değişimlerine göre düzeltilebilir",
                "D": "Dönem kârına amortisman ve işletme sermayesi düzeltmeleri uygulanarak sonuca ulaşılır",
                "E": "TMS 7 doğrudan yöntemin kullanılmasını teşvik eder",
            },
            "D",
            "Dönem kârına amortisman, tahakkuk ve işletme sermayesi düzeltmeleri uygulanması dolaylı yöntemin özelliğidir. TMS 7 par. 18-19 uyarınca doğrudan yöntemde brüt nakit tahsilat ve ödeme grupları açıklanır ve bu yöntemin kullanılması teşvik edilir.",
            "TMS 7 Nakit Akis Tablosu",
        ),
        "std-tms7-gen-0049": full(
            "Grup tarafından kullanılamayan önemli nakit bakiyelerine ilişkin aşağıdakilerden hangisi YANLIŞTIR?",
            {
                "A": "Tutar finansal tablolarda açıklanır",
                "B": "Kullanımı engelleyen koşullar hakkında bilgi verilir",
                "C": "Kambiyo kontrolü veya yasal kısıtlama kullanım engeline örnek olabilir",
                "D": "Nakit tanımını karşıladığı için kullanım kısıtı açıklanmaz",
                "E": "Açıklama, kullanıcıların işletmenin likiditesini değerlendirmesine yardımcı olur",
            },
            "D",
            "TMS 7 par. 48-49, grup tarafından kullanılamayan önemli nakit ve nakit benzeri bakiyelerinin tutarı ile yönetimin açıklamasının sunulmasını ister. Kambiyo kontrolleri ve yasal kısıtlamalar bu duruma örnek olabilir.",
            "TMS 7 Nakit Akis Tablosu",
        ),
    },
    "tms_8_politikalar": {
        "std-tms8-gen-0015": full(
            "Aşağıdakilerden hangisi muhasebe politikasını değiştirmek için tek başına yeterli bir neden DEĞİLDİR?",
            {
                "A": "Yeni bir TFRS'nin değişikliği zorunlu kılması",
                "B": "Yeni politikanın işlemlerin etkisi hakkında daha güvenilir bilgi sağlaması",
                "C": "Yönetimin belirli bir dönemde daha yüksek kâr göstermek istemesi",
                "D": "Yeni politikanın finansal tablo kullanıcılarına daha ihtiyaca uygun bilgi vermesi",
                "E": "İlgili standardın geçiş hükümlerinde politika değişikliği öngörülmesi",
            },
            "C",
            "TMS 8 par. 14 uyarınca politika ancak bir TFRS gerektirdiğinde veya daha güvenilir ve ihtiyaca uygun bilgi sağladığında değiştirilir. Belirli bir dönemde raporlanan kârı artırma isteği bu ölçütleri karşılamaz.",
            "TMS 8 Muhasebe Politikalari, Muhasebe Tahminlerinde Degisiklikler ve Hatalar",
        ),
        "std-tms8-gen-0025": full(
            "Yayımlanmış ancak henüz yürürlüğe girmemiş bir TFRS için aşağıdakilerden hangisi YANLIŞTIR?",
            {
                "A": "İşletme standardı henüz uygulamamışsa bu durumu açıklar",
                "B": "Bilinen veya makul biçimde tahmin edilebilen olası etki hakkında bilgi verir",
                "C": "Erken uygulamaya izin veriliyorsa işletme bu seçeneği değerlendirebilir",
                "D": "Yürürlük tarihine kadar standardın olası etkisi hakkında hiçbir açıklama yapılmaz",
                "E": "Etki tahmin edilemiyorsa bu durum açıklanır",
            },
            "D",
            "TMS 8 par. 30-31 uyarınca işletme, yayımlanmış fakat henüz yürürlüğe girmemiş standardı uygulamadığını ve ilk uygulamanın finansal tablolar üzerindeki bilinen veya makul biçimde tahmin edilebilen etkisini açıklar; etki tahmin edilemiyorsa bunu belirtir.",
            "TMS 8 Muhasebe Politikalari, Muhasebe Tahminlerinde Degisiklikler ve Hatalar",
        ),
        "std-tms8-gen-0050": full(
            "Önemli bir geçmiş dönem hatasının düzeltilmesine ilişkin aşağıdakilerden hangisi doğru bir uygulama DEĞİLDİR?",
            {
                "A": "Hatanın oluştuğu dönemin karşılaştırmalı tutarları yeniden düzenlenir",
                "B": "Hata en erken sunulan dönemden önceyse açılış bakiyeleri düzeltilir",
                "C": "Geriye dönük düzeltme mümkün değilse mümkün olan en erken tarih kullanılır",
                "D": "Düzeltme tutarı hata tespit edildiği dönemin kâr veya zararına eklenir",
                "E": "Hatanın niteliği ve ilgili finansal tablo kalemlerine etkisi açıklanır",
            },
            "D",
            "TMS 8 par. 42-49: önemli geçmiş dönem hataları geriye dönük yeniden düzenlenir ve düzeltme, hatanın tespit edildiği dönemin kâr veya zararına dâhil edilmez. Hatanın niteliği ile karşılaştırmalı kalemlere ve açılış bakiyelerine etkileri açıklanır.",
            "TMS 8 Muhasebe Politikalari, Muhasebe Tahminlerinde Degisiklikler ve Hatalar",
        ),
    },
    "tms_38_modv": {
        "std-tms38-gen-0001": full(
            "Aşağıdakilerden hangisi TMS 38'deki maddi olmayan duran varlık tanımını KARŞILAMAZ?",
            {
                "A": "İşletmenin kontrol ettiği ve sözleşmeden doğan patent hakkı",
                "B": "Ayrılabilir ve lisanslanabilir bilgisayar yazılımı",
                "C": "Belirli tutarda para alma hakkı veren vadeli mevduat",
                "D": "Satın alınmış ve tanımlanabilir yayın hakkı",
                "E": "İşletme birleşmesinde edinilen tanımlanabilir müşteri ilişkisi",
            },
            "C",
            "TMS 38 par. 8-13 uyarınca maddi olmayan duran varlık fiziksel niteliği olmayan, tanımlanabilir ve parasal olmayan bir varlıktır. Vadeli mevduat belirli tutarda para alma hakkı verdiği için parasal finansal varlıktır; TMS 38 kapsamındaki maddi olmayan duran varlık değildir.",
            "TMS 38 Maddi Olmayan Duran Varliklar",
        ),
        "std-tms38-gen-0025": full(
            "Aşağıdakilerden hangisi TMS 38'e göre araştırma faaliyeti örneği DEĞİLDİR?",
            {
                "A": "Yeni bilgi elde etmeye yönelik özgün inceleme",
                "B": "Araştırma bulguları için alternatif uygulamaların araştırılması",
                "C": "Yeni malzeme ve süreç alternatiflerinin değerlendirilmesi",
                "D": "Ticari üretim öncesi seçilmiş yeni ürün tasarımının denenmesi",
                "E": "Olası yeni ürün seçeneklerinin oluşturulması ve seçimi",
            },
            "D",
            "TMS 38 par. 56-59: yeni bilgi edinme, alternatif araştırma ve seçenek oluşturma araştırma safhasına örnektir. Ticari üretimden önce seçilmiş ürün tasarımının denenmesi ise geliştirme faaliyetidir.",
            "TMS 38 Maddi Olmayan Duran Varliklar",
        ),
        "std-tms38-gen-0038": full(
            "Hasılata dayalı itfa yöntemiyle ilgili aşağıdakilerden hangisi YANLIŞTIR?",
            {
                "A": "Varlığın tüketimini her durumda en iyi yansıttığı kabul edilir",
                "B": "Hasılat çoğu zaman varlığın ekonomik yararının tüketiminden başka etkenleri de yansıtır",
                "C": "Bu yöntemin uygun olmadığına ilişkin aksi kanıtlanabilir bir varsayım vardır",
                "D": "Varlık hakkı önceden belirlenmiş bir hasılat eşiğiyle sınırlıysa istisna gündeme gelebilir",
                "E": "İtfa yöntemi ekonomik yararların beklenen tüketim biçimini yansıtmalıdır",
            },
            "A",
            "TMS 38 par. 97-98C: itfa yöntemi ekonomik yararların tüketim biçimini yansıtır. Hasılat fiyat ve satış hacmi gibi başka etkenlerden de etkilendiğinden hasılata dayalı yöntemin uygun olmadığı varsayılır; standartta dar istisnalar bulunur.",
            "TMS 38 Maddi Olmayan Duran Varliklar",
        ),
        "std-tms38-gen-0048": full(
            "Bir işletmenin film telif hakkının maliyeti 720.000 ₺, birikmiş itfa payı 210.000 ₺ ve birikmiş değer düşüklüğü zararı 60.000 ₺'dir. TMS 38'deki maliyet modeline göre telif hakkı finansal durum tablosunda kaç ₺ ile gösterilir?",
            {
                "A": "450.000 ₺",
                "B": "510.000 ₺",
                "C": "660.000 ₺",
                "D": "720.000 ₺",
                "E": "390.000 ₺",
            },
            "A",
            "TMS 38 par. 74 uyarınca maliyet modelinde defter değeri, maliyetten birikmiş itfa ve birikmiş değer düşüklüğü zararları düşülerek bulunur: 720.000 - 210.000 - 60.000 = 450.000 ₺.",
            "TMS 38 Maddi Olmayan Duran Varliklar",
        ),
        "std-tms38-gen-0055": full(
            "Aşağıdakilerden hangisinin TMS 38 kapsamında dipnotlarda açıklanması GEREKMEZ?",
            {
                "A": "Sınırsız veya sınırlı faydalı ömür ayrımı",
                "B": "Kullanılan itfa yöntemleri ve faydalı ömürler",
                "C": "Dönem başı ve dönem sonu defter değerinin mutabakatı",
                "D": "Dönemde gider yazılan araştırma ve geliştirme harcamaları",
                "E": "Varlığın satın alındığı tedarikçinin ticaret unvanı",
            },
            "E",
            "TMS 38 par. 118 ve 126; faydalı ömürleri, itfa yöntemlerini, defter değeri mutabakatını ve giderleşen araştırma-geliştirme harcamalarını açıklama konusu yapar. Tedarikçinin ticaret unvanı zorunlu açıklamalar arasında değildir.",
            "TMS 38 Maddi Olmayan Duran Varliklar",
        ),
    },
}


def transformed(question: dict, topic: str) -> dict:
    result = json.loads(json.dumps(question, ensure_ascii=False))
    qid = result["id"]

    if qid in STEMS[topic]:
        result["stem"] = STEMS[topic][qid]
    if qid in FULL_PATCHES[topic]:
        result.update(FULL_PATCHES[topic][qid])

    result["stem"] = TL_WORD.sub("₺", TL.sub(r"\1 ₺", result["stem"]))
    result["solution"] = ANSWER_TAIL.sub(
        "", TL_WORD.sub("₺", TL.sub(r"\1 ₺", result["solution"]))
    ).strip()
    result["options"] = {
        letter: TL_WORD.sub("₺", TL.sub(r"\1 ₺", text))
        for letter, text in result["options"].items()
    }
    return result


def apply_or_check(path: Path, topic: str, write: bool) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    differences: list[str] = []

    for index, question in enumerate(questions):
        expected = transformed(question, topic)
        if question != expected:
            differences.append(f"{path}::{question['id']}")
            if write:
                questions[index] = expected

    if write:
        for question in questions:
            assert set(question["options"]) == set("ABCDE"), question["id"]
            assert len(set(question["options"].values())) == 5, question["id"]
            assert question["answer"] in question["options"], question["id"]
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return differences


def main() -> int:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--check", action="store_true")
    action.add_argument("--write", action="store_true")
    args = parser.parse_args()

    differences: list[str] = []
    for topic in TOPICS:
        relative = Path("content") / LESSON / f"{topic}.json"
        for path in (ROOT / relative, APP_ROOT / relative):
            differences.extend(apply_or_check(path, topic, args.write))

    if args.check and differences:
        print("Eslesmeyen sorular:")
        for difference in differences[:30]:
            print(f"- {difference}")
        return 1

    stem_count = sum(len(values) for values in STEMS.values())
    full_count = sum(len(values) for values in FULL_PATCHES.values())
    print(
        f"3 paket / {stem_count} kok + {full_count} tam soru kalibrasyonu "
        "iki repoda dogrulandi."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
