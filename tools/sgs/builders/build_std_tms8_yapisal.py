#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TMS 8 Muhasebe Politikalari, Tahminlerde Degisiklikler ve Hatalar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gercek sinav profiliyle yeniden yazim (senaryo kok + kisa terim/tutar sik). Eski surum tanim agirlikliydi ve 98 mutlak ifadeli celdirici tasiyordu (kor %45). Kapsam: politika secimi hiyerarsisi ve tutarlilik, politika degisikligi kosullari ve istisnalari (p. 16-17, erken uygulama), geriye donuk uygulama ve uygulanabilir olmama, 2021 tahmin tanimi ve tahmin degisikligi (faydali omur, kalinti deger, yontem, garanti, dava), onceki donem hatalari ve geriye donuk yeniden duzenleme, vergi etkisi, aciklamalar. 12 hesap sorusu modulde hesaplandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: TMS 8 Muhasebe Politikalari, Muhasebe Tahminlerinde Degisiklikler ve Hatalar (KGK, 2021 degisikligi dahil); TMS 16 p. 51, 61-62; TMS 10 p. 3
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/tms_8_politikalar.json"
STYLE_REF = 'SGS Muhasebe Standartlari (gercek sinav profiline kalibre: senaryo kok + kisa sik)'
ONEK = "std-tms8-gen-"


def patch(stem, options, answer, solution, ref='TMS 8 Muhasebe Politikalari, Muhasebe Tahminlerinde Degisiklikler ve Hatalar'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Bir işletme, müşteri sadakat programı için TFRS 15'in öngördüğü muhasebeleştirmeyi uygulamak yerine, sektördeki birçok şirketin yaptığı gibi puanları satış anında gider olarak kaydetmek istemektedir. İşlemi doğrudan düzenleyen bir TFRS vardır. Muhasebe politikası nasıl belirlenir?",
        {
            'A': 'İlgili TFRS uygulanarak',
            'B': 'Sektör uygulamasına göre',
            'C': "Kavramsal Çerçeve'ye göre",
            'D': 'Vergi mevzuatına göre',
            'E': 'Yönetimin tercihine göre',
        },
        'A',
        "TMS 8 p. 7'ye göre bir TFRS belirli bir işlem, diğer olay veya duruma özel olarak uygulanıyorsa, o kaleme uygulanacak muhasebe politikası **o TFRS uygulanarak** belirlenir.",
        'TMS 8 p. 7',
    ),
    # düzey 2
    '0002': patch(
        'Bir işletme bu yıl ilk kez uzun vadeli inşaat sözleşmesi imzalamış ve bu sözleşmeler için bir muhasebe politikası belirlemiştir. Önceki yıllarda bu tür bir işlemi olmamıştır. Bu durum TMS 8 bakımından nasıl değerlendirilir?',
        {
            'A': 'Politika değişikliğidir',
            'B': 'Politika değişikliği sayılmaz',
            'C': 'Yeniden sınıflandırmadır',
            'D': 'Hata düzeltmesidir',
            'E': 'Tahmin değişikliğidir',
        },
        'B',
        "TMS 8 p. 16(b)'ye göre **daha önce gerçekleşmemiş** veya önemli olmayan işlem, olay veya durumlar için yeni bir muhasebe politikası uygulanması **politika değişikliği değildir**.",
        'TMS 8 p. 16',
    ),
    # düzey 3
    '0003': patch(
        'Bir işletme 2026 yılında, daha ihtiyaca uygun bilgi sağladığı için stok maliyet yöntemini isteğe bağlı olarak değiştirmiştir. İşletme 2026 finansal tablolarında 2025 yılına ait karşılaştırmalı bilgi sunmaktadır. Değişikliğin geçmiş dönemlere ilişkin birikmiş etkisi hangi tarihli özkaynak açılış bakiyesine yansıtılır?',
        {
            'A': '1 Ocak 2026',
            'B': '31 Aralık 2025',
            'C': '31 Aralık 2026',
            'D': '1 Ocak 2024',
            'E': '1 Ocak 2025',
        },
        'E',
        "TMS 8 p. 19(b) ve 22'ye göre isteğe bağlı politika değişikliği **geriye dönük** uygulanır; işletme **sunulan en erken dönemin** etkilenen özkaynak kalemlerinin açılış bakiyesini düzeltir. Karşılaştırmalı dönem 2025 olduğundan düzeltme **1 Ocak 2025** bakiyesine yapılır.",
        'TMS 8 p. 19, 22',
    ),
    # düzey 3
    '0004': patch(
        'Bir işletme politika değişikliğini geriye dönük uygulamak istemektedir; ancak 2019 öncesi kayıtlar bir yangında yok olduğundan o yıllara ait etkiyi belirlemek, bütün makul çabalara rağmen mümkün değildir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Yeni politika uygulanabilir en erken tarihten itibaren uygulanır',
            'B': 'Uygulanabilir olmama durumu açıklanır',
            'C': 'Bu durum uygulanabilir olmama kavramıyla açıklanır',
            'D': 'Değişiklik uygulanamaz ve eski politikaya devam edilir',
            'E': 'Birikmiş etki uygulanabilir en erken dönemin başına yansıtılır',
        },
        'D',
        "TMS 8 p. 24-25'e göre geriye dönük uygulamanın bazı dönemler için **uygulanabilir olmaması** hâlinde yeni politika **uygulanabilir en erken tarihten** itibaren uygulanır ve bu durum açıklanır; değişiklikten vazgeçilmesi öngörülmez. p. 5'e göre bütün makul çabalara rağmen uygulanamayan bir hüküm 'uygulanabilir değildir'.",
        'TMS 8 p. 23-25',
    ),
    # düzey 2
    '0005': patch(
        "Bir işletme, bir yükümlülüğün ölçümünde yaptığı bir değişikliğin muhasebe politikası değişikliği mi yoksa muhasebe tahmini değişikliği mi olduğunu, bütün analizlere rağmen ayırt edememektedir. TMS 8'e göre bu değişiklik nasıl ele alınır?",
        {
            'A': 'Tahmin değişikliği olarak',
            'B': 'Hata düzeltmesi olarak',
            'C': 'Değişiklik yapılmaz',
            'D': 'Politika değişikliği olarak',
            'E': 'Yeniden sınıflandırma olarak',
        },
        'A',
        "TMS 8 p. 35'e göre bir muhasebe politikası değişikliğini muhasebe tahmininde değişiklikten ayırt etmenin zor olduğu durumlarda değişiklik **muhasebe tahmininde değişiklik** olarak ele alınır.",
        'TMS 8 p. 35',
    ),
    # düzey 2
    '0006': patch(
        "Bir işletme, cari yılın ortasında ürün garantisi karşılığı hesaplamasında kullandığı arıza oranını, yeni saha verilerine dayanarak %3'ten %5'e çıkarmıştır. Bu değişikliğin etkisi hangi dönemin kâr veya zararına yansıtılır?",
        {
            'A': 'Önceki dönem',
            'B': 'Diğer kapsamlı gelir',
            'C': 'Geçmiş yıllar kârları',
            'D': 'Cari dönem',
            'E': 'Sunulan en erken dönem',
        },
        'D',
        "TMS 8 p. 36'ya göre muhasebe tahminindeki değişikliğin etkisi, yalnız o dönemi etkiliyorsa **değişikliğin yapıldığı dönemin**, gelecek dönemleri de etkiliyorsa değişikliğin yapıldığı dönem ve gelecek dönemlerin kâr veya zararına **ileriye dönük** olarak yansıtılır.",
        'TMS 8 p. 36-37',
    ),
    # düzey 3
    '0007': patch(
        "Maliyeti 800.000 ₺, kalıntı değeri 50.000 ₺, faydalı ömrü 10 yıl olan bir makine doğrusal yöntemle amortismana tabi tutulmaktadır. 3 yıl sonunda yapılan incelemede kalıntı değerin 110.000 ₺, kalan faydalı ömrün 5 yıl olduğu belirlenmiştir. İzleyen yılın amortisman gideri kaç ₺'dir?",
        {
            'A': '81.000',
            'B': '75.000',
            'C': '138.000',
            'D': '93.000',
            'E': '86.250',
        },
        'D',
        'Birikmiş amortisman 75.000 × 3 = 225.000 ₺, defter değeri 575.000 ₺. Yeni tahminlerle: (575.000 − 110.000) / 5 = **93.000 ₺**; değişiklik ileriye dönüktür.',
        'TMS 8 p. 36; TMS 16 p. 51',
    ),
    # düzey 3
    '0008': patch(
        'Bir işletme 2026 yılında, 2025 yılı finansal tablolarında önemli bir hata yapıldığını fark etmiştir. 2026 finansal tablolarında 2025 karşılaştırmalı bilgisi sunulmaktadır. Hata aşağıdakilerden hangisi yoluyla düzeltilir?',
        {
            'A': 'Dipnotta açıklanıp düzeltilmemesi',
            'B': 'Karşılaştırmalı tutarların yeniden düzenlenmesi',
            'C': 'Gelecek dönemlere yayılması',
            'D': 'Hatanın cari dönem kâr veya zararına gider yazılması',
            'E': 'Diğer kapsamlı gelire alınması',
        },
        'B',
        "TMS 8 p. 42'ye göre önemli önceki dönem hataları, keşfedildikten sonra onaylanan ilk finansal tablolarda **hatanın oluştuğu önceki dönem(ler)e ait karşılaştırmalı tutarlar yeniden düzenlenerek** geriye dönük düzeltilir; cari dönem kâr veya zararına alınmaz.",
        'TMS 8 p. 42',
    ),
    # düzey 3
    '0009': patch(
        "Bir işletme 2025 yılında 60.000 ₺ tutarındaki olağan bakım giderini yanlışlıkla makine maliyetine eklemiş ve bu tutar üzerinden 2025 yılında 6.000 ₺ amortisman ayırmıştır. Hata önemlidir ve 2026'da fark edilmiştir. Vergi etkisi ihmal edildiğinde 2025 karşılaştırmalı net kârı kaç ₺ azaltılarak yeniden düzenlenir?",
        {
            'A': '30.000',
            'B': '54.000',
            'C': '6.000',
            'D': '66.000',
            'E': '60.000',
        },
        'B',
        'Bakım gideri 60.000 ₺ olarak giderleşmeliydi; buna karşılık bu tutar üzerinden ayrılan 6.000 ₺ amortisman olmamalıydı. 2025 kârı net **54.000 ₺ fazla** gösterilmiştir ve bu tutar kadar azaltılır.',
        'TMS 8 p. 42',
    ),
    # düzey 3
    '0010': patch(
        "Bir işletme geçen yıl şüpheli alacak karşılığını hesaplarken, finansal tablolar onaylandığı sırada muhasebe servisinde mevcut olan bir müşterinin iflas kararını dikkate almayı unutmuştur. Bu yıl durumu fark etmiştir; tutar önemlidir. TMS 8'e göre bu düzeltme nasıl nitelendirilir?",
        {
            'A': 'Yeniden sınıflandırma',
            'B': 'Sonraki olay',
            'C': 'Önceki dönem hatası',
            'D': 'Politika değişikliği',
            'E': 'Tahmin değişikliği',
        },
        'C',
        "Karşılık bir tahmin olsa da TMS 8 p. 5'e göre tablolar yayımlandığında **mevcut olan ve dikkate alınması beklenebilecek bilginin kullanılmaması** önceki dönem hatasıdır. Yeni bilgiye dayanan revizyon ise tahmin değişikliği olurdu (p. 34).",
        'TMS 8 p. 5, 32, 41',
    ),
    # düzey 2
    '0011': patch(
        "TMS 8'deki tanımlara göre işletmenin finansal tablolarını hazırlarken ve sunarken uyguladığı belirli ilkeler, esaslar, gelenekler, kurallar ve uygulamalar hangi kavramla ifade edilir?",
        {
            'A': 'Muhasebe politikaları',
            'B': 'Raporlama kuralları',
            'C': 'Kavramsal ilkeler',
            'D': 'Ölçüm teknikleri',
            'E': 'Muhasebe tahminleri',
        },
        'A',
        "TMS 8 p. 5'e göre **muhasebe politikaları**, işletme tarafından finansal tabloların hazırlanması ve sunulmasında uygulanan belirli ilkeler, esaslar, gelenekler, kurallar ve uygulamalardır.",
        'TMS 8 p. 5',
    ),
    # düzey 3
    '0012': patch(
        "Bir işletme 2026 yılında stok maliyet yöntemini FIFO'dan ağırlıklı ortalamaya geriye dönük olarak değiştirmiştir. Stoklar 31.12.2024'te FIFO'ya göre 520.000 ₺, ağırlıklı ortalamaya göre 490.000 ₺; 31.12.2025'te FIFO'ya göre 610.000 ₺, ağırlıklı ortalamaya göre 560.000 ₺'dir. Vergi etkisi ihmal edildiğinde karşılaştırmalı olarak sunulan 2025 net kârı kaç ₺ azaltılır?",
        {
            'A': '80.000',
            'B': '20.000',
            'C': '50.000',
            'D': '0',
            'E': '30.000',
        },
        'B',
        'Kapanış stoku 50.000 ₺ düşer, bu satışların maliyetini artırır; açılış stoku 30.000 ₺ düştüğü için maliyet aynı tutarda azalır. 2025 kârına net etki: 50.000 − 30.000 = **20.000 ₺ azalış**. Açılış farkı 1 Ocak 2025 geçmiş yıllar kârlarına yansıtılır.',
        'TMS 8 p. 22',
    ),
    # düzey 2
    '0013': patch(
        'Bir işletmenin dönem içinde yaptığı değişiklikler şunlardır: stok maliyet yönteminin değiştirilmesi, yatırım amaçlı gayrimenkul ölçüm modelinin değiştirilmesi, stok değer düşüklüğü oranının yeni fiyat verileriyle güncellenmesi, borçlanma maliyetlerinin aktifleştirilmesine ilişkin politikanın yeniden belirlenmesi ve finansal durum tablosunda kalemlerin sınıflandırmasının değiştirilmesi. Bunlardan hangisi tahmin değişikliğidir?',
        {
            'A': 'Sınıflandırmanın değiştirilmesi',
            'B': 'Ölçüm modelinin değiştirilmesi',
            'C': 'Borçlanma maliyeti aktifleştirme politikasının belirlenmesi',
            'D': 'Stok değer düşüklüğü oranının güncellenmesi',
            'E': 'Stok maliyet yönteminin değiştirilmesi',
        },
        'D',
        "TMS 8 p. 5 ve 32'ye göre ölçüm belirsizliğine tabi bir tutarın **yeni bilgilerle güncellenmesi** tahmin değişikliğidir. Maliyet yöntemi ve ölçüm modeli değişiklikleri politika değişikliği, sınıflandırma değişikliği ise TMS 1 kapsamında sunum değişikliğidir.",
        'TMS 8 p. 5, 32',
    ),
    # düzey 2
    '0014': patch(
        "Bir işletme, önceki dönemlerde hiç hata yapılmamış gibi finansal tablo unsurlarının tutarlarını, muhasebeleştirilmesini, ölçümünü ve açıklamalarını düzeltmektedir. TMS 8'de bu işlem hangi kavramla ifade edilir?",
        {
            'A': 'Tahmin değişikliği',
            'B': 'İleriye dönük uygulama',
            'C': 'Geriye dönük yeniden düzenleme',
            'D': 'Geriye dönük uygulama',
            'E': 'Yeniden sınıflandırma',
        },
        'C',
        "TMS 8 p. 5'e göre **geriye dönük yeniden düzenleme**, önceki dönem hatası hiç oluşmamış gibi finansal tablo unsurlarının muhasebeleştirilmesi, ölçümü ve açıklanmasına ilişkin tutarların düzeltilmesidir.",
        'TMS 8 p. 5',
    ),
    # düzey 3
    '0015': patch(
        'Bir işletme, yıllardır kendi idari binası olarak kullandığı ve maliyet modeliyle ölçtüğü binayı boşaltmış ve tamamen üçüncü kişilere kiraya vermiştir. Bina artık yatırım amaçlı gayrimenkul politikasıyla ölçülecektir. TMS 8 bakımından bu durum nasıl değerlendirilir?',
        {
            'A': 'Olağanüstü kalemdir',
            'B': 'Geriye dönük politika değişikliğidir',
            'C': 'Politika değişikliği sayılmaz',
            'D': 'Tahmin değişikliğidir',
            'E': 'Hata düzeltmesidir',
        },
        'C',
        "TMS 8 p. 16(a)'ya göre daha önce gerçekleşenlerden **özü farklı olan işlem, olay veya durumlar** için bir muhasebe politikasının uygulanması politika değişikliği değildir. Kullanım amacının değişmesi yeni bir durumdur; transfer TMS 40 hükümlerine göre yapılır.",
        'TMS 8 p. 16',
    ),
    # düzey 1
    '0016': patch(
        "TMS 8'e göre finansal tablolardaki ölçüm belirsizliğine tabi parasal tutarlar hangi kavramla ifade edilir?",
        {
            'A': 'Muhasebe politikaları',
            'B': 'Muhasebe tahminleri',
            'C': 'Geçiş hükümleri',
            'D': 'Açıklama ilkeleri',
            'E': 'Önceki dönem hataları',
        },
        'B',
        "TMS 8 p. 5'e göre (2021 değişikliği) **muhasebe tahminleri**, finansal tablolardaki ölçüm belirsizliğine tabi parasal tutarlardır.",
        'TMS 8 p. 5',
    ),
    # düzey 3
    '0017': patch(
        "Bir işletme yıl içinde 2.000.000 ₺ garantili satış yapmıştır. Yıl sonunda garanti karşılığını, yeni saha verilerine göre satışların %3'ü yerine %5'i olarak belirlemiştir. Eski oranla karşılaştırıldığında bu tahmin değişikliği cari yılın kârını kaç ₺ azaltır?",
        {
            'A': '60.000',
            'B': '0',
            'C': '100.000',
            'D': '160.000',
            'E': '40.000',
        },
        'E',
        'Tahmin değişikliği cari döneme yansır: 2.000.000 × (%5 − %3) = **40.000 ₺** ek karşılık gideri; önceki dönemler düzeltilmez.',
        'TMS 8 p. 36',
    ),
    # düzey 2
    '0018': patch(
        "Aşağıdakilerden hangisi TMS 8'e göre önceki dönem hatalarının kaynakları arasında sayılmaz?",
        {
            'A': 'Muhasebe politikalarının hatalı veya yanlış uygulanması',
            'B': 'Hileli işlemler',
            'C': 'Yeni bilgiyle garanti tahmininin artırılması',
            'D': 'Olguların gözden kaçırılması',
            'E': 'Matematiksel toplama yanlışı',
        },
        'C',
        "TMS 8 p. 5'e göre önceki dönem hataları; **matematiksel hatalar, muhasebe politikalarının uygulanmasındaki yanlışlıklar, olguların gözden kaçırılması veya yanlış yorumlanması ve hileler**in etkilerini kapsar. Yeni bilgiye dayanan tahmin revizyonu hata değildir.",
        'TMS 8 p. 5, 41',
    ),
    # düzey 3
    '0019': patch(
        "Bir işletme, birim maliyeti çok düşük olan el aletlerini maddi duran varlık olarak aktifleştirip amortismana tabi tutmak yerine alındıkları dönemde gider yazmaktadır. Bu uygulamanın toplam etkisi önemsizdir ve belirli bir sunum amacı taşımamaktadır. TMS 8'e göre bu uygulama hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Yasaktır',
            'B': 'Önceki dönem hatasıdır',
            'C': 'Politika değişikliğidir',
            'D': 'Kabul edilebilir',
            'E': 'Tahmin değişikliğidir',
        },
        'D',
        "TMS 8 p. 8'e göre TFRS'lerde belirlenen muhasebe politikalarının **etkisi önemli olmadığında uygulanması gerekmez**; ancak işletmenin finansal durumunu belirli bir şekilde sunmak için TFRS'lerden önemsiz de olsa kasten sapması uygun değildir.",
        'TMS 8 p. 8',
    ),
    # düzey 3
    '0020': patch(
        'Muhasebe tahminlerine ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Tahminin yeni bilgiyle revize edilmesi önceki dönem hatasıdır\n\nII. Tahmin değişikliğinin etkisi geçmiş yıllar kârlarına aktarılır\n\nIII. Politika mı tahmin mi olduğu ayırt edilemeyen değişiklik tahmin değişikliği sayılır',
        {
            'A': 'I ve III',
            'B': 'Yalnız I',
            'C': 'II ve III',
            'D': 'Yalnız III',
            'E': 'I ve II',
        },
        'D',
        "TMS 8 p. 35'e göre ayırt edilemeyen değişiklik tahmin değişikliğidir (III). p. 34 ve 48'e göre yeni bilgiye dayanan revizyon **hata değildir** (I yanlış); p. 36'ya göre tahmin değişikliği **cari ve gelecek dönemlerin kâr veya zararına** yansır (II yanlış).",
        'TMS 8 p. 34-36, 48',
    ),
    # düzey 3
    '0021': patch(
        "Bir işletme, hiçbir TFRS'nin düzenlemediği yeni bir dijital varlık türünü edinmiştir. Yönetim politika geliştirirken önce benzer konuları düzenleyen TFRS'leri, ardından Kavramsal Çerçeve'yi incelemiş; son olarak benzer kavramsal çerçeveyi kullanan başka bir standart koyucunun güncel düzenlemesini de dikkate almak istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Yönetim ihtiyaca uygun ve güvenilir bilgi sağlayan politika geliştirir',
            'B': "Diğer kaynaklar TFRS'lerle çelişmedikçe kullanılabilir",
            'C': "Diğer standart koyucuların düzenlemeleri TFRS'lere üstün gelir",
            'D': "Önce benzer konuları düzenleyen TFRS'lere başvurulur",
            'E': "Kavramsal Çerçeve'deki tanımlar dikkate alınır",
        },
        'C',
        "TMS 8 p. 10-11'e göre yönetim ihtiyaca uygun ve güvenilir bilgi sağlayan politika geliştirir; önce benzer konulardaki TFRS'lere, sonra Kavramsal Çerçeve'ye bakar. p. 12'ye göre diğer standart koyucuların düzenlemeleri ve sektör uygulamaları **ancak bu kaynaklarla çelişmedikçe** dikkate alınabilir.",
        'TMS 8 p. 10-12',
    ),
    # düzey 2
    '0022': patch(
        "Bir işletmenin yönetimi, raporlanan kârı yükseltmek amacıyla stok maliyet yöntemini değiştirmek istemektedir; yeni yöntem daha güvenilir veya daha ihtiyaca uygun bilgi sağlamamaktadır ve bir TFRS de değişikliği gerektirmemektedir. TMS 8'e göre bu değişiklik hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Dipnotta açıklanarak yapılır',
            'B': 'İleriye dönük yapılır',
            'C': 'Yapılamaz',
            'D': 'Denetçi onayıyla yapılır',
            'E': 'Geriye dönük yapılır',
        },
        'C',
        "TMS 8 p. 14'e göre işletme muhasebe politikasını **ancak bir TFRS gerektiriyorsa** veya değişiklik **daha güvenilir ve daha ihtiyaca uygun bilgi** sağlıyorsa değiştirir. Kârı yükseltme amacı tek başına yeterli değildir.",
        'TMS 8 p. 14',
    ),
    # düzey 2
    '0023': patch(
        "Yeni yürürlüğe giren bir TFRS'yi ilk kez uygulayan bir işletme, standardın kendi içinde ayrıntılı geçiş hükümleri bulunduğunu görmüştür. Bu politika değişikliği nasıl uygulanır?",
        {
            'A': 'Geçiş hükümlerine göre',
            'B': 'Cari dönemde tek seferde',
            'C': 'Geriye dönük',
            'D': 'İleriye dönük',
            'E': 'Yönetimin seçtiği şekilde',
        },
        'A',
        "TMS 8 p. 19(a)'ya göre bir TFRS'nin ilk kez uygulanmasından kaynaklanan politika değişikliği, varsa **o TFRS'nin özel geçiş hükümlerine** göre; geçiş hükmü yoksa geriye dönük olarak uygulanır.",
        'TMS 8 p. 19',
    ),
    # düzey 2
    '0024': patch(
        "Bir işletme, yayımlanmış ancak henüz yürürlüğe girmemiş ve erken uygulamayı da tercih etmediği yeni bir TFRS'nin finansal tabloları önemli ölçüde etkileyeceğini öngörmektedir. TMS 8'e göre bu konuda ne yapılır?",
        {
            'A': 'Geriye dönük düzeltme yapılır',
            'B': 'Olası etki açıklanır',
            'C': 'Karşılık ayrılır',
            'D': 'Standart hemen uygulanır',
            'E': 'Bir işlem yapılmaz',
        },
        'B',
        "TMS 8 p. 30'a göre işletme, **yayımlanmış ancak henüz yürürlüğe girmemiş** bir TFRS'yi uygulamadığında bu durumu ve yeni TFRS'nin ilk uygulama döneminde finansal tablolar üzerindeki **olası etkisini** değerlendirmeye yarayan bilgileri açıklar.",
        'TMS 8 p. 30',
    ),
    # düzey 3
    '0025': patch(
        "Bir işletme, makinelerinin amortismanını doğrusal yöntemden üretim miktarı yöntemine geçirmiştir; çünkü makinelerin ekonomik faydalarının tüketim biçimine ilişkin yeni bilgi edinmiştir. Bu değişiklik TMS 8'e göre nasıl nitelendirilir?",
        {
            'A': 'Yeniden sınıflandırma',
            'B': 'Politika değişikliği',
            'C': 'Hata düzeltmesi',
            'D': 'Tahmin değişikliği',
            'E': 'Geçiş hükmü uygulaması',
        },
        'D',
        "TMS 8 p. 32B ve 34'e göre muhasebe tahmini geliştirmede kullanılan bir **ölçüm tekniğindeki veya girdideki değişikliğin** etkileri, önceki dönem hatasından kaynaklanmıyorsa **tahmin değişikliğidir**; TMS 16 p. 61 de amortisman yöntemi değişikliğini tahmin değişikliği sayar.",
        'TMS 8 p. 32B, 34',
    ),
    # düzey 3
    '0026': patch(
        'Bir işletme geçen yıl finansal tablolarını onaylarken o tarihte mevcut en iyi bilgilerle bir dava karşılığı ayırmıştır. Bu yıl davada yeni bir bilirkişi raporu gelmiş ve karşılığın artırılması gerekmiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Karşılaştırmalı tutarlar yeniden düzenlenmez',
            'B': 'Tahmin değişikliğidir',
            'C': 'Yeni bilgiye dayanan revizyon önceki dönem hatası sayılmaz',
            'D': 'Etkisi cari dönem kâr veya zararına yansır',
            'E': 'Önceki dönem hatası olarak geriye dönük düzeltilir',
        },
        'E',
        "TMS 8 p. 34 ve 48'e göre tahminin **yeni bilgi veya gelişmelere** dayanarak revize edilmesi geçmiş dönemlerle ilgili değildir ve **hata düzeltmesi değildir**; tahmin değişikliği olarak ileriye dönük muhasebeleştirilir.",
        'TMS 8 p. 34, 48',
    ),
    # düzey 3
    '0027': patch(
        "Bir işletme, defter değeri 600.000 ₺ olan bir makinenin amortisman yöntemini cari yılın başında doğrusal yöntemden üretim miktarı yöntemine geçirmiştir. Makinenin kalan ömrü boyunca 150.000 birim üretim yapması beklenmektedir; cari yılda 30.000 birim üretilmiştir. Kalıntı değer yoktur. Cari yılın amortisman gideri kaç ₺'dir?",
        {
            'A': '140.000',
            'B': '240.000',
            'C': '480.000',
            'D': '120.000',
            'E': '150.000',
        },
        'D',
        'Amortisman yöntemi değişikliği tahmin değişikliğidir ve **cari yılın başındaki defter değeri** üzerinden ileriye dönük uygulanır: 600.000 × 30.000 / 150.000 = **120.000 ₺**.',
        'TMS 8 p. 32B, 36; TMS 16 p. 62',
    ),
    # düzey 3
    '0028': patch(
        "Bir işletme 2026 yılında, 2025 yılı sonu stok sayımında stokların 40.000 ₺ fazla sayıldığını tespit etmiştir; hata önemlidir. 2025 yılı için daha önce raporlanan net kâr 300.000 ₺'dir. Vergi etkisi ihmal edildiğinde 2026 finansal tablolarında karşılaştırmalı olarak sunulacak düzeltilmiş 2025 net kârı kaç ₺'dir?",
        {
            'A': '220.000',
            'B': '260.000',
            'C': '340.000',
            'D': '300.000',
            'E': '40.000',
        },
        'B',
        'Dönem sonu stokunun 40.000 ₺ fazla sayılması satışların maliyetini aynı tutarda düşük, kârı yüksek gösterir. 2025 karşılaştırmalı tutarı yeniden düzenlenir: 300.000 − 40.000 = **260.000 ₺**.',
        'TMS 8 p. 42',
    ),
    # düzey 2
    '0029': patch(
        "Bir işletme, cari yılın ara dönem çalışmaları sırasında, aynı yıl içinde yapılmış önemli bir kayıt hatasını cari yılın finansal tabloları onaylanmadan önce bulmuştur. TMS 8'e göre bu hata nasıl ele alınır?",
        {
            'A': 'Cari dönem tabloları onaylanmadan düzeltilir',
            'B': 'Dipnotta açıklanıp bırakılır',
            'C': 'Tahmin değişikliği olarak işlenir',
            'D': 'Gelecek yılın tablolarında düzeltilir',
            'E': 'Önceki dönem hatası olarak düzeltilir',
        },
        'A',
        "TMS 8 p. 41'e göre cari dönemde ortaya çıkan olası hatalar, **finansal tablolar onaylanmadan önce cari dönemde düzeltilir**. Geriye dönük yeniden düzenleme, sonraki dönemde keşfedilen önceki dönem hataları içindir.",
        'TMS 8 p. 41',
    ),
    # düzey 2
    '0030': patch(
        "Bir işletme, belirli bir finansal performans hedefine ulaşmış görünmek için bilerek yapılan ancak tutarı önemli olmayan bir sınıflandırma hatasını düzeltmeden bırakmıştır. TMS 8'e göre bu finansal tablolar hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': "TFRS'ye uygundur",
            'B': 'Dipnot açıklamasıyla uygundur',
            'C': 'Denetçi onayıyla uygundur',
            'D': 'Önemsiz olduğu için uygundur',
            'E': "TFRS'ye uygun değildir",
        },
        'E',
        "TMS 8 p. 41'e göre finansal tablolar, işletmenin finansal durumunu, performansını veya nakit akışlarını belirli bir biçimde sunmak için **kasten yapılmış önemli veya önemsiz hatalar** içeriyorsa **TFRS'ye uygun değildir**.",
        'TMS 8 p. 41',
    ),
    # düzey 3
    '0031': patch(
        'Bir işletmede dönem içinde üç değişiklik yapılmıştır: yatırım amaçlı gayrimenkullerin ölçümü maliyet modelinden gerçeğe uygun değer modeline geçirilmiştir (daha ihtiyaca uygun bilgi sağladığı için); makinelerin faydalı ömrü 8 yıldan 6 yıla indirilmiştir; ilk kez yapılan inşaat işleri için bir politika belirlenmiştir. Bunlardan hangisi TMS 8 kapsamında geriye dönük uygulanır?',
        {
            'A': 'Hiçbiri',
            'B': 'Yatırım amaçlı gayrimenkul ölçüm modeli',
            'C': 'Makinelerin faydalı ömrünün değiştirilmesi',
            'D': 'İnşaat işleri politikası',
            'E': 'Üçü de',
        },
        'B',
        "TMS 8 p. 14 ve 19'a göre daha ihtiyaca uygun bilgi sağlayan isteğe bağlı politika değişikliği (TMS 40'ta model değişikliği) **geriye dönük** uygulanır. Faydalı ömür değişikliği tahmin değişikliğidir, ileriye dönüktür; daha önce olmayan işlem için politika belirlenmesi p. 16'ya göre politika değişikliği sayılmaz.",
        'TMS 8 p. 14, 16, 32B',
    ),
    # düzey 2
    '0032': patch(
        "Bir işletme, makinelerinin faydalı ömrüne ilişkin tahmin değişikliğinin cari döneme etkisini açıklamış; ancak gelecek dönemlere etkisini tahmin etmenin uygulanabilir olmadığını belirlemiştir. TMS 8'e göre gelecek dönem etkisi için ne yapılır?",
        {
            'A': 'Geriye dönük düzeltme yapılır',
            'B': 'Bu durum açıklanır',
            'C': 'Karşılık ayrılır',
            'D': 'Tahmin değişikliği yapılmaz',
            'E': 'Etki uydurma tutarla açıklanır',
        },
        'B',
        "TMS 8 p. 39-40'a göre işletme tahmin değişikliğinin niteliğini ve cari döneme etkisini açıklar; gelecek dönemlere etkisini tahmin etmek **uygulanabilir değilse bu durumu açıklar**.",
        'TMS 8 p. 39-40',
    ),
    # düzey 3
    '0033': patch(
        'Bir işletme 2026 yılında, 31.12.2024 tarihli stok sayımında stokların 30.000 ₺ eksik sayıldığını tespit etmiştir; 2025 sonu sayımı doğrudur ve hata önemlidir. 2026 finansal tablolarında 2025 karşılaştırmalı bilgisi sunulmaktadır. Vergi etkisi ihmal edildiğinde 2025 yılı net kârına yapılacak düzeltme hangisidir?',
        {
            'A': '60.000 ₺ azaltılır',
            'B': '30.000 ₺ artırılır',
            'C': 'Düzeltme yapılmaz',
            'D': '30.000 ₺ azaltılır',
            'E': '15.000 ₺ artırılır',
        },
        'D',
        '2024 kapanış stoku eksik olduğundan 2024 kârı 30.000 ₺ düşük; aynı tutar 2025 açılış stokunu düşük, 2025 satışların maliyetini düşük ve **2025 kârını 30.000 ₺ yüksek** göstermiştir. Karşılaştırmalı 2025 kârı **30.000 ₺ azaltılır**; 1 Ocak 2025 geçmiş yıllar kârları ise 30.000 ₺ artırılır.',
        'TMS 8 p. 42',
    ),
    # düzey 3
    '0034': patch(
        "Bir işletme, tutarı toplam varlıklarının binde biri olan ve bilerek yapılmamış bir önceki dönem sınıflandırma hatasını cari yılda fark etmiştir. Hata kullanıcıların kararlarını etkileyecek nitelikte değildir. TMS 8'e göre bu hata için geriye dönük yeniden düzenleme hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Zorunludur',
            'B': 'Vergi idaresine bildirilir',
            'C': 'Denetçi onayına bağlıdır',
            'D': 'Yasaktır',
            'E': 'Zorunlu değildir',
        },
        'E',
        "TMS 8 p. 42'deki geriye dönük yeniden düzenleme **önemli** önceki dönem hataları içindir; p. 8'e göre TFRS'ler etkisi önemli olmayan durumlarda uygulanmak zorunda değildir. Ancak p. 41'e göre belirli bir sunum amacıyla **kasten** yapılan hatalar önemsiz olsa da kabul edilmez.",
        'TMS 8 p. 8, 41',
    ),
    # düzey 2
    '0035': patch(
        'Bir işletme hem muhasebe politikası değişikliği hem de önceki dönem hatası düzeltmesi yapmıştır; her iki işlemin ertelenmiş vergi etkileri de önemlidir. Bu vergi etkileri hangi standarda göre muhasebeleştirilir?',
        {
            'A': 'TMS 12',
            'B': 'TMS 37',
            'C': 'TMS 8',
            'D': 'TMS 10',
            'E': 'TMS 1',
        },
        'A',
        "TMS 8 p. 4'e göre geriye dönük uygulama ve geriye dönük yeniden düzenlemelerin **vergi etkileri TMS 12 Gelir Vergileri** uyarınca muhasebeleştirilir ve açıklanır.",
        'TMS 8 p. 4',
    ),
    # düzey 3
    '0036': patch(
        "Bir işletme 2026 yılında, 2025 yılında bir hasılatın erken tanınması nedeniyle 2025 vergi öncesi kârının 100.000 ₺ fazla gösterildiğini tespit etmiştir; vergi oranı %25'tir ve hata vergi kayıtlarını da etkilemiştir. Karşılaştırmalı 2025 net kârı kaç ₺ azaltılır?",
        {
            'A': '125.000',
            'B': '37.500',
            'C': '100.000',
            'D': '25.000',
            'E': '75.000',
        },
        'E',
        "Vergi öncesi kâr 100.000 ₺ azalırken vergi gideri %25 oranında, 25.000 ₺ azalır. Net kâr düzeltmesi: 100.000 − 25.000 = **75.000 ₺**; vergi etkisi TMS 12'ye göre hesaplanır.",
        'TMS 8 p. 42; TMS 12',
    ),
    # düzey 3
    '0037': patch(
        "Bir işletme 2025 finansal tablolarında, o tarihteki bütün bilgilerle makul biçimde tahmin ederek 200.000 ₺ dava karşılığı ayırmıştır. Dava 2026'da işletme aleyhine 260.000 ₺ olarak kesinleşmiştir. Aradaki fark hangi dönemin kâr veya zararına ve kaç ₺ olarak yansıtılır?",
        {
            'A': '2025, 260.000 ₺ gider',
            'B': '2026, 60.000 ₺ gider',
            'C': '2025, 60.000 ₺ gider',
            'D': '2026, 260.000 ₺ gider',
            'E': 'Geçmiş yıllar kârları',
        },
        'B',
        "Karşılık yayımlandığı tarihteki bilgilerle makul olarak tahmin edildiğinden fark **hata değil tahmin değişikliğidir**; TMS 8 p. 36'ya göre değişikliğin olduğu dönemin kâr veya zararına yansır: 260.000 − 200.000 = **60.000 ₺**.",
        'TMS 8 p. 34, 36, 48',
    ),
    # düzey 2
    '0038': patch(
        "Aşağıdakilerden hangileri doğrudur?\n\nI. Önemli önceki dönem hataları cari dönem kâr veya zararına alınarak düzeltilir\n\nII. Bir TFRS'nin erken uygulanması isteğe bağlı politika değişikliği değildir\n\nIII. Amortisman yöntemindeki değişiklik politika değişikliğidir",
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'II ve III',
            'D': 'Yalnız I',
            'E': 'Yalnız II',
        },
        'E',
        "TMS 8 p. 20'ye göre erken uygulama isteğe bağlı politika değişikliği değildir (II). p. 42'ye göre önemli hatalar **geriye dönük** düzeltilir (I yanlış); amortisman yöntemi değişikliği **tahmin değişikliğidir** (III yanlış).",
        'TMS 8 p. 20, 36, 42',
    ),
    # düzey 2
    '0039': patch(
        "Aşağıdakilerden hangileri TMS 8'e göre geriye dönük uygulanır?\n\nI. Geçiş hükmü bulunmayan bir TFRS'nin ilk uygulanmasından doğan politika değişikliği\n\nII. Makinenin kalıntı değer tahmininin değişmesi\n\nIII. Önemli bir önceki dönem hatasının düzeltilmesi",
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'I ve III',
            'D': 'Yalnız III',
            'E': 'Yalnız I',
        },
        'C',
        "TMS 8 p. 19'a göre geçiş hükmü olmayan politika değişikliği (I) ve p. 42'ye göre önemli önceki dönem hatası (III) geriye dönük uygulanır. p. 36'ya göre tahmin değişikliği (II) **ileriye dönüktür**.",
        'TMS 8 p. 19, 36, 42',
    ),
    # düzey 3
    '0040': patch(
        "Aşağıdakilerden hangileri TMS 8'e göre doğrudur?\n\nI. İşlemi doğrudan düzenleyen TFRS varsa politika o TFRS'ye göre belirlenir\n\nII. Benzer işlemler için politikalar tutarlı uygulanır\n\nIII. Bir TFRS gerektirdiğinde muhasebe politikası değiştirilir",
        {
            'A': 'I, II ve III',
            'B': 'II ve III',
            'C': 'Yalnız I',
            'D': 'I ve III',
            'E': 'I ve II',
        },
        'A',
        "TMS 8 p. 7'ye göre ilgili TFRS uygulanır (I); p. 13'e göre tutarlılık esastır (II); p. 14(a)'ya göre bir TFRS gerektirdiğinde politika değiştirilir (III).",
        'TMS 8 p. 7, 13, 14',
    ),
    # düzey 2
    '0041': patch(
        "Bir işletme bazı hammadde stoklarında FIFO, niteliği ve kullanımı tamamen aynı olan diğer hammadde stoklarında ağırlıklı ortalama yöntemini kullanmaktadır; hiçbir TFRS bu kalemleri ayrı gruplandırmayı gerektirmemektedir. Bu uygulama TMS 8'in hangi hükmüne aykırıdır?",
        {
            'A': 'Önemlilik',
            'B': 'Politikaların tutarlı uygulanması',
            'C': 'İleriye dönük uygulama',
            'D': 'Geriye dönük uygulama',
            'E': 'Hata düzeltmesi',
        },
        'B',
        "TMS 8 p. 13'e göre bir TFRS farklı politikalar uygulanabilecek kalem grupları belirlemedikçe veya buna izin vermedikçe işletme, **benzer işlem, olay ve durumlar için muhasebe politikalarını tutarlı olarak seçer ve uygular**.",
        'TMS 8 p. 13',
    ),
    # düzey 2
    '0042': patch(
        "Bir işletme, maddi duran varlıklarını bu yıl ilk kez maliyet modeli yerine yeniden değerleme modeliyle ölçmeye başlamıştır. TMS 8'e göre bu değişiklik nasıl ele alınır?",
        {
            'A': 'Hata düzeltmesi olarak',
            'B': 'Tahmin değişikliği olarak',
            'C': "TMS 16'ya göre yeniden değerleme olarak",
            'D': 'Olağanüstü kalem olarak',
            'E': 'Geriye dönük politika değişikliği olarak',
        },
        'C',
        "TMS 8 p. 17'ye göre varlıkların TMS 16 veya TMS 38'e göre **ilk kez yeniden değerleme modeliyle ölçülmesi** bir muhasebe politikası değişikliğidir; ancak TMS 8'e göre geriye dönük değil, **TMS 16 veya TMS 38 uyarınca yeniden değerleme olarak** ele alınır.",
        'TMS 8 p. 17',
    ),
    # düzey 3
    '0043': patch(
        "Bir işletme 2026 yılında stok maliyet yöntemini FIFO'dan ağırlıklı ortalamaya değiştirmiştir (isteğe bağlı politika değişikliği). 31 Aralık 2024 tarihli stoklar FIFO'ya göre 520.000 ₺, ağırlıklı ortalamaya göre 490.000 ₺'dir. Vergi etkisi ihmal edildiğinde 1 Ocak 2025 tarihli geçmiş yıllar kârları hangi yönde ve kaç ₺ düzeltilir?",
        {
            'A': 'Düzeltilmez',
            'B': '30.000 ₺ artırılır',
            'C': '30.000 ₺ azaltılır',
            'D': '15.000 ₺ azaltılır',
            'E': '490.000 ₺ azaltılır',
        },
        'C',
        "TMS 8 p. 22'ye göre geriye dönük uygulamada yeni politika her zaman uygulanıyormuş gibi davranılır; açılış stoku 520.000 ₺ yerine 490.000 ₺ olacağından geçmiş dönem kârları **30.000 ₺ azaltılır**.",
        'TMS 8 p. 22',
    ),
    # düzey 2
    '0044': patch(
        "Bir işletme, zorunlu yürürlük tarihi 2027 olan yeni bir TFRS'yi 2026 yılında erken uygulamaya karar vermiştir. TMS 8'e göre bu erken uygulama nasıl nitelendirilir?",
        {
            'A': 'Hata düzeltmesidir',
            'B': 'Yeniden sınıflandırmadır',
            'C': 'Tahmin değişikliğidir',
            'D': 'İsteğe bağlı politika değişikliğidir',
            'E': 'İsteğe bağlı politika değişikliği değildir',
        },
        'E',
        "TMS 8 p. 20'ye göre **bir TFRS'nin erken uygulanması, bu standart bakımından isteğe bağlı bir muhasebe politikası değişikliği değildir**; ilgili TFRS'nin geçiş hükümlerine göre uygulanır.",
        'TMS 8 p. 20',
    ),
    # düzey 3
    '0045': patch(
        "Bir işletme, finansal tablolarında aşağıdaki tutarları belirlemektedir: stokların net gerçekleşebilir değeri, garanti yükümlülüğü, dava karşılığı, ticari alacakların beklenen kredi zararı ve kasadaki nakit mevcudu. TMS 8'e göre bunlardan hangisi muhasebe tahmini değildir?",
        {
            'A': 'Dava karşılığı',
            'B': 'Stokların net gerçekleşebilir değeri',
            'C': 'Beklenen kredi zararı',
            'D': 'Garanti yükümlülüğü',
            'E': 'Kasadaki nakit mevcudu',
        },
        'E',
        "TMS 8 p. 5'e göre muhasebe tahminleri **ölçüm belirsizliğine tabi** finansal tablo tutarlarıdır. Net gerçekleşebilir değer, garanti ve dava karşılıkları ile beklenen kredi zararları tahmin gerektirir; sayılarak belirlenen kasa mevcudunda ölçüm belirsizliği yoktur.",
        'TMS 8 p. 5, 32-32A',
    ),
    # düzey 3
    '0046': patch(
        "Maliyeti 500.000 ₺ olan bir makine, kalıntı değeri sıfır kabul edilerek 10 yıl faydalı ömürle doğrusal yöntemle amortismana tabi tutulmaktadır. 4 yıl sonunda, 5. yılın başında, makinenin kalan faydalı ömrünün 4 yıl olduğu belirlenmiştir. 5. yılın amortisman gideri kaç ₺'dir?",
        {
            'A': '75.000',
            'B': '87.500',
            'C': '100.000',
            'D': '125.000',
            'E': '112.500',
        },
        'A',
        "Tahmin değişikliği ileriye dönük uygulanır. 4 yıl sonunda birikmiş amortisman 200.000 ₺, defter değeri 300.000 ₺'dir. Kalan 4 yıla dağıtılır: 300.000 / 4 = **75.000 ₺**. Geçmiş yıllar düzeltilmez.",
        'TMS 8 p. 36; TMS 16 p. 51',
    ),
    # düzey 2
    '0047': patch(
        "Bir işletmede önceki yılın finansal tablolarında, o tarihte elde edilebilir olan bilgiler gözden kaçırılarak bir faturanın iki kez gider yazıldığı bu yıl anlaşılmıştır; tutar önemlidir. TMS 8'e göre bu durum nasıl nitelendirilir?",
        {
            'A': 'Sonraki olay',
            'B': 'Önceki dönem hatası',
            'C': 'Tahmin değişikliği',
            'D': 'Olağanüstü kalem',
            'E': 'Politika değişikliği',
        },
        'B',
        "TMS 8 p. 5'e göre önceki dönem hataları, finansal tablolar yayımlandığında **mevcut olan ve elde edilmesi ve dikkate alınması makul olarak beklenebilecek güvenilir bilginin** kullanılmamasından veya yanlış kullanılmasından kaynaklanan eksiklik ve yanlışlıklardır; matematiksel hatalar ve gözden kaçırma dâhildir.",
        'TMS 8 p. 5, 41',
    ),
    # düzey 3
    '0048': patch(
        'Bir işletme 2026 yılında, 2023 yılında yapılmış önemli bir hatayı fark etmiştir. İşletme 2026 finansal tablolarında yalnız 2025 yılına ait karşılaştırmalı bilgi sunmaktadır. Hatanın 2025 öncesine ait birikmiş etkisi hangi tarihli açılış bakiyelerine yansıtılır?',
        {
            'A': '1 Ocak 2026',
            'B': '31 Aralık 2026',
            'C': '31 Aralık 2023',
            'D': '1 Ocak 2025',
            'E': '1 Ocak 2023',
        },
        'D',
        "TMS 8 p. 42(b)'ye göre hata **sunulan en erken dönemden önce** oluşmuşsa, sunulan en erken dönemin varlık, borç ve özkaynak **açılış bakiyeleri** yeniden düzenlenir; burada en erken dönem 2025'tir.",
        'TMS 8 p. 42(b)',
    ),
    # düzey 3
    '0049': patch(
        'Bir işletme önemli bir önceki dönem hatasının belirli bir döneme ait etkisini belirleyebilmekte, ancak bu hatanın geçmiş dönemlere ait birikmiş etkisini bütün makul çabalara rağmen belirleyememektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Geriye dönük yeniden düzenleme ilkesinden vazgeçilmez',
            'B': 'Karşılaştırmalı bilgi uygulanabildiği ölçüde yeniden düzenlenir',
            'C': 'Hata uygulanabilir en erken tarihten itibaren düzeltilir',
            'D': 'Uygulanabilir olmama durumu açıklanır',
            'E': 'Hata cari dönem kâr veya zararına gider yazılır',
        },
        'E',
        "TMS 8 p. 43-45'e göre hatanın belirli dönem veya birikmiş etkisinin belirlenmesi uygulanabilir değilse, karşılaştırmalı bilgi **uygulanabilir en erken tarihten** itibaren ileriye doğru yeniden düzenlenir ve bu durum açıklanır; hatanın cari dönem kâr veya zararına alınması öngörülmez.",
        'TMS 8 p. 43-45',
    ),
    # düzey 2
    '0050': patch(
        "Bir işletme 2026 yılında, 2025 yılına ait önemli bir hatayı geriye dönük olarak düzeltmiştir. TMS 8'e göre işletmenin açıklaması gereken bilgilerden biri aşağıdakilerden hangisidir?",
        {
            'A': 'Denetçinin görüşü',
            'B': 'Hatayı yapan çalışanın adı',
            'C': 'Yönetim kurulu kararı',
            'D': 'Hatanın niteliği',
            'E': 'Vergi cezası tutarı',
        },
        'D',
        "TMS 8 p. 49'a göre işletme; **önceki dönem hatasının niteliğini**, sunulan her önceki dönem için etkilenen kalemlerdeki düzeltme tutarını, sunulan en erken dönemin başındaki düzeltme tutarını ve gerekirse uygulanabilir olmama nedenlerini açıklar.",
        'TMS 8 p. 49',
    ),
    # düzey 3
    '0051': patch(
        "Bir işletme, stoklarını TMS 2'ye göre maliyet ile net gerçekleşebilir değerin düşük olanıyla ölçmektedir (muhasebe politikası). Net gerçekleşebilir değer belirlenirken tahmini satış fiyatı ve tahmini satış maliyetleri kullanılmaktadır. Bu ilişki TMS 8 bakımından aşağıdakilerden hangisiyle açıklanır?",
        {
            'A': 'Politikanın amacına tahminle ulaşılır',
            'B': 'Tahmin politikanın yerini alır',
            'C': 'İkisi aynı kavramdır',
            'D': 'Tahmin değişikliği politika değişikliğidir',
            'E': 'Politika tahmini gereksiz kılar',
        },
        'A',
        "TMS 8 p. 32A'ya göre muhasebe politikası bir kalemin ölçüm belirsizliği içeren parasal tutarla ölçülmesini gerektirebilir; bu durumda işletme **muhasebe politikasının belirlediği amaca ulaşmak için muhasebe tahmini** geliştirir.",
        'TMS 8 p. 32A',
    ),
    # düzey 2
    '0052': patch(
        "Bir işletme, geçiş hükümleri bulunan yeni bir TFRS'yi ilk kez uygulamış ve bu uygulama cari dönemi etkilemiştir. TMS 8'e göre işletmenin açıklaması gereken bilgilerden biri aşağıdakilerden hangisidir?",
        {
            'A': 'Sektör ortalaması',
            'B': 'Yönetimin ücret politikası',
            'C': 'Denetçinin adı',
            'D': 'Standart koyucunun gerekçesi',
            'E': "Uygulanan TFRS'nin adı",
        },
        'E',
        "TMS 8 p. 28'e göre bir TFRS'nin ilk uygulanması cari veya önceki dönemleri etkiliyorsa işletme **TFRS'nin adını**, değişikliğin geçiş hükümlerine göre yapıldığını, politika değişikliğinin niteliğini ve düzeltme tutarlarını açıklar.",
        'TMS 8 p. 28',
    ),
    # düzey 3
    '0053': patch(
        "Bir işletmenin 2025 finansal tabloları Mart 2026'da onaylanıp yayımlanmıştır. Ekim 2026'da, onay tarihinde muhasebe servisinde bulunan ancak kayda alınması unutulan önemli bir satış faturası bulunmuştur. Bu durum 2026 finansal tablolarında nasıl ele alınır?",
        {
            'A': 'Cari dönem geliri olarak',
            'B': 'Politika değişikliği olarak',
            'C': 'Tahmin değişikliği olarak',
            'D': 'Düzeltme gerektiren sonraki olay olarak',
            'E': 'Önceki dönem hatası olarak',
        },
        'E',
        "TMS 10 yalnız raporlama dönemi sonu ile tabloların onay tarihi arasındaki olayları kapsar. Onaydan sonra anlaşılan ve **onay tarihinde mevcut olan bilginin kullanılmamasından** doğan yanlışlık, TMS 8 p. 5'e göre önceki dönem hatasıdır ve geriye dönük düzeltilir.",
        'TMS 8 p. 5, 41; TMS 10 p. 3',
    ),
    # düzey 2
    '0054': patch(
        "TMS 8'de, bir işlem, diğer olay veya duruma yeni bir muhasebe politikasının, o politika her zaman uygulanıyormuş gibi uygulanması hangi kavramla ifade edilir?",
        {
            'A': 'Yeniden değerleme',
            'B': 'Yeniden sınıflandırma',
            'C': 'İleriye dönük uygulama',
            'D': 'Geriye dönük uygulama',
            'E': 'Geriye dönük yeniden düzenleme',
        },
        'D',
        "TMS 8 p. 5'e göre **geriye dönük uygulama**, yeni bir muhasebe politikasının her zaman uygulanıyormuş gibi uygulanmasıdır. Hataların düzeltilmesinde kullanılan kavram ise geriye dönük yeniden düzenlemedir.",
        'TMS 8 p. 5',
    ),
    # düzey 3
    '0055': patch(
        "Bir işletme cari yılın başında bir makinenin kalan faydalı ömrünü kısaltmış; bu nedenle yıllık amortisman 50.000 ₺'den 75.000 ₺'ye çıkmıştır. Tahmin değişikliğinin cari dönem kâr veya zararına etkisi kaç ₺'dir?",
        {
            'A': '25.000 ₺ azalış',
            'B': 'Etki yok',
            'C': '50.000 ₺ azalış',
            'D': '75.000 ₺ azalış',
            'E': '25.000 ₺ artış',
        },
        'A',
        "TMS 8 p. 36'ya göre tahmin değişikliği ileriye dönük uygulanır ve cari dönemden başlayarak kâr veya zararı etkiler; p. 39 uyarınca etkisi açıklanır: 75.000 − 50.000 = **25.000 ₺ ek gider**.",
        'TMS 8 p. 36, 39',
    ),
    # düzey 3
    '0056': patch(
        "Bir işletme 2026'da isteğe bağlı bir politika değişikliği yapmıştır; ancak yeni politikanın önceki bütün dönemlere birikmiş etkisini cari dönemin başı itibarıyla belirlemek uygulanabilir değildir. TMS 8'e göre yeni politika nasıl uygulanır?",
        {
            'A': 'Uygulanmaz',
            'B': 'Önceki dönem hatası olarak',
            'C': 'Geçmiş yıllar kârları düzeltilerek',
            'D': 'Uygulanabilir en erken tarihten ileriye dönük',
            'E': 'Sunulan en erken dönemin başından geriye dönük',
        },
        'D',
        "TMS 8 p. 25'e göre yeni politikanın önceki bütün dönemlere birikmiş etkisini cari dönemin başında belirlemek uygulanabilir değilse işletme, karşılaştırmalı bilgiyi yeni politikayı **uygulanabilir en erken tarihten itibaren ileriye dönük** uygulayacak şekilde düzeltir.",
        'TMS 8 p. 25',
    ),
    # düzey 2
    '0057': patch(
        'Bir işletme önemli bir önceki dönem hatasını geriye dönük olarak düzeltmiştir. İşletme TMS 33 kapsamında pay başına kazanç açıklamaktadır. Aşağıdakilerden hangisinin önceki dönem tutarı için de düzeltme tutarı açıklanır?',
        {
            'A': 'Yönetim hedefleri',
            'B': 'Pay başına kazanç',
            'C': 'Bütçelenen satışlar',
            'D': 'Vergi beyannamesi',
            'E': 'Çalışan sayısı',
        },
        'B',
        "TMS 8 p. 49(b)'ye göre işletme, sunulan her önceki dönem için etkilenen her finansal tablo kalemindeki ve TMS 33 uygulanıyorsa **temel ve seyreltilmiş pay başına kazançtaki** düzeltme tutarını açıklar.",
        'TMS 8 p. 49',
    ),
    # düzey 3
    '0058': patch(
        "Bir işletme politika değişikliğini geriye dönük uygularken 2024 yılına ait bir tahmini yeniden yapmakta ve 2024 tabloları onaylandıktan sonra, 2026'da öğrendiği bir piyasa gelişmesini bu tahmine dâhil etmek istemektedir. TMS 8'e göre bu bilgi hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Cari döneme alınır',
            'B': 'Dipnotta kullanılır',
            'C': 'Tahmine dâhil edilmelidir',
            'D': 'Sonradan edinilen bilgi kullanılamaz',
            'E': 'Hata düzeltmesi sayılır',
        },
        'D',
        "TMS 8 p. 53'e göre geriye dönük uygulama veya yeniden düzenlemede, önceki dönemde ne tür varsayımlar yapılacağına ilişkin olarak **sonradan edinilen bilgiler (sonradan görme) kullanılmaz**; o tarihte mevcut olan bilgiler esas alınır.",
        'TMS 8 p. 53',
    ),
    # düzey 3
    '0059': patch(
        "Aşağıdakilerden hangileri TMS 8'e göre muhasebe politikası değişikliği sayılmaz?\n\nI. Özü farklı işlemler için farklı bir politika uygulanması\n\nII. Önemli olmayan işlemler için yeni bir politika uygulanması\n\nIII. Daha güvenilir bilgi sağlayan stok maliyet yöntemine isteğe bağlı geçiş",
        {
            'A': 'Yalnız II',
            'B': 'Yalnız I',
            'C': 'I, II ve III',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'D',
        "TMS 8 p. 16'ya göre özü farklı işlemler için politika (I) ve önemsiz işlemler için yeni politika (II) politika değişikliği sayılmaz. p. 14(b)'ye göre daha güvenilir ve ihtiyaca uygun bilgi sağlayan yönteme isteğe bağlı geçiş (III) **politika değişikliğidir**.",
        'TMS 8 p. 16-17, 20',
    ),
    # düzey 2
    '0060': patch(
        'Önceki dönem hatalarına ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Önemli hatalar karşılaştırmalı tutarlar yeniden düzenlenerek düzeltilir\n\nII. Hatanın niteliği açıklanır\n\nIII. Önemli hatalar keşfedildiği dönemin kâr veya zararına alınır',
        {
            'A': 'I ve II',
            'B': 'I ve III',
            'C': 'Yalnız II',
            'D': 'II ve III',
            'E': 'Yalnız I',
        },
        'A',
        "TMS 8 p. 42'ye göre önemli hatalar karşılaştırmalı tutarlar yeniden düzenlenerek düzeltilir (I); p. 49'a göre hatanın niteliği açıklanır (II). Hata **cari dönem kâr veya zararına alınmaz** (III yanlış).",
        'TMS 8 p. 41-42, 49',
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
    print(f"1 paket / {len(PATCHES)} soru ('TMS 8 Muhasebe Politikalari, Tahminlerde Degisiklikler ve Hatalar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
