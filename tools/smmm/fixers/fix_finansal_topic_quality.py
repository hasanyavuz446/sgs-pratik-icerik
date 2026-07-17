#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Finansal Muhasebe konu paketlerini yazılı kalite kurallarına uyarlar.

İşlem sırası:
1. Seçilen mevcut soruları, aynı kavramı ölçen öncüllü biçime dönüştürür.
2. Doğru seçenek metinlerini baseline dosyasına alır.
3. Her paket için farklı seed ile dengeli ve örüntüsüz cevap harfi üretir.
4. Doğru metni yeni harfe, çeldiricileri diğer harflere taşır.
5. Denetçinin length-tell verdiği sorularda doğru metne dokunmadan iki
   çeldiriciyi açıklayıcı yanlış önermelerle dengeler.

Script idempotenttir. --verify yalnız mevcut dosyaları baseline ile karşılaştırır.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTENT = ROOT / "content" / "yeterlilik"
BASELINE = ROOT / "tools" / "smmm" / "baselines" / "finansal_answer_baseline.json"

FILES = {
    "questions_topic_finansal_temel_kavramlar_2026.json": 20260721,
    "questions_topic_finansal_muhasebe_kayitlari_2026.json": 20260722,
    "questions_topic_finansal_stoklar_2026.json": 20260723,
    "questions_topic_finansal_donem_sonu_2026.json": 20260724,
    "questions_topic_finansal_tms_tfrs_2026.json": 20260725,
}

COMBOS = [
    "Yalnız I",
    "Yalnız II",
    "Yalnız III",
    "I ve II",
    "I ve III",
    "II ve III",
    "I, II ve III",
]


def premise(intro: str, statements: list[str], correct: str, why: str) -> dict:
    assert len(statements) == 3
    assert correct in COMBOS
    stem = (
        f"{intro}\n\n"
        f"I. {statements[0]}\n\n"
        f"II. {statements[1]}\n\n"
        f"III. {statements[2]}\n\n"
        "Buna göre hangileri doğrudur?"
    )
    distractors = [item for item in COMBOS if item != correct][:4]
    return {
        "question": stem,
        "correct": correct,
        "distractors": distractors,
        "explanation": why,
    }


PREMISES = {
    # Temel Kavramlar — 8 soru, "hepsi" 2/8.
    "topic-finansal-temel-014": premise(
        "İşletme kişiliği kavramına ilişkin aşağıdaki ifadeleri değerlendiriniz.",
        [
            "Sahibin işletmeye koyduğu değer faaliyet hasılatı değil özkaynak artışıdır.",
            "Sahibin kişisel işlemleri işletmenin faaliyet gideri sayılır.",
            "İşletmenin borç ve alacakları sahibinkilerden ayrı izlenir.",
        ],
        "I ve III",
        "İşletme, sahibinden ayrı bir muhasebe kişiliğidir. Sermaye koyma özkaynak "
        "işlemidir ve işletmenin ilişkileri ayrı izlenir; kişisel harcamalar faaliyet gideri değildir.",
    ),
    "topic-finansal-temel-020": premise(
        "İhtiyatlılık kavramının uygulanmasına ilişkin aşağıdaki ifadeleri değerlendiriniz.",
        [
            "Belirsizlik altında temkinli fakat tarafsız yargı kullanılmasını gerektirir.",
            "Varlıkların bilinçli biçimde düşük gösterilmesini gerektirir.",
            "Gizli yedek oluşturmak amacıyla borçların sürekli yüksek ölçülmesine izin verir.",
        ],
        "Yalnız I",
        "İhtiyatlılık temkinli ve tarafsız yargıdır; kasıtlı eksik ya da fazla ölçüm ve "
        "gizli yedek oluşturulması bu kavramla bağdaşmaz.",
    ),
    "topic-finansal-temel-023": premise(
        "Maliyet esası kavramına ilişkin aşağıdaki ifadeleri değerlendiriniz.",
        [
            "Edinilen bir varlık ilk kayıtta kural olarak elde etme maliyetiyle ölçülür.",
            "Varlığı kullanıma hazır duruma getiren doğrudan giderler maliyetin parçası olabilir.",
            "Özel bir ölçüm hükmü yoksa piyasa değerindeki her artış kendiliğinden kayda alınmaz.",
        ],
        "I, II ve III",
        "Maliyet esası ilk kayıtta elde etme maliyetini temel alır; doğrudan maliyetleri "
        "kapsayabilir ve kendiliğinden piyasa değerine geçilmesini gerektirmez.",
    ),
    "topic-finansal-temel-030": premise(
        "Garanti yükümlülüğü tahmininde ihtiyatlılığa uygun uygulamaları değerlendiriniz.",
        [
            "Mevcut güvenilir bilgiler kullanılır.",
            "Belirsizlik temkinli fakat tarafsız biçimde değerlendirilir.",
            "Olası tutarlar arasından koşulsuz olarak en yüksek olan seçilir.",
        ],
        "I ve II",
        "Tahmin güncel ve güvenilir bilgiye dayanmalı, temkinli ama tarafsız olmalıdır; "
        "koşulsuz biçimde en yüksek tutarı seçmek yanlı ölçüm yaratır.",
    ),
    "topic-finansal-temel-045": premise(
        "Tutarlılık kavramına ilişkin aşağıdaki ifadeleri değerlendiriniz.",
        [
            "Benzer olaylarda aynı muhasebe politikalarının dönemler boyunca uygulanması esastır.",
            "Muhasebe politikaları hiçbir koşulda değiştirilemez.",
            "Haklı politika değişikliklerinin niteliği ve etkileri açıklanır.",
        ],
        "I ve III",
        "Tutarlılık karşılaştırılabilirliği destekler; daha güvenilir bilgi sağlayan haklı "
        "değişikliklere gerekli açıklamalar yapılmak koşuluyla engel değildir.",
    ),
    "topic-finansal-temel-051": premise(
        "İşletmenin sürekliliği değerlendirmesine ilişkin aşağıdaki ifadeleri değerlendiriniz.",
        [
            "Yönetim geleceğe ilişkin mevcut bilgileri dikkate alır.",
            "Geçmiş dönemde kâr edilmiş olması değerlendirmeyi gereksiz kılar.",
            "Önemli süreklilik belirsizlikleri finansal tablolarda açıklanır.",
        ],
        "I ve III",
        "Süreklilik değerlendirmesi geleceğe yönelik mevcut bilgilere dayanır; geçmiş kâr "
        "tek başına yeterli değildir ve önemli belirsizlikler açıklanır.",
    ),
    "topic-finansal-temel-055": premise(
        "Özün önceliği kavramına ilişkin aşağıdaki ifadeleri değerlendiriniz.",
        [
            "İşlemin ekonomik etkisi muhasebeleştirmede dikkate alınır.",
            "Hukuki belgeler her durumda tamamen yok sayılır.",
            "İşlemden doğan hak ve yükümlülükler hukuki adın yanında incelenir.",
        ],
        "I ve III",
        "Özün önceliği hukuki belgeleri yok saymaz; hukuki biçimle birlikte gerçek ekonomik "
        "etkiyi, hakları ve yükümlülükleri esas alır.",
    ),
    "topic-finansal-temel-059": premise(
        "Önemlilik değerlendirmesine ilişkin aşağıdaki unsurları değerlendiriniz.",
        [
            "Kalemin parasal büyüklüğü",
            "Kalemin niteliği",
            "İşletmeye özgü koşullar ve kullanıcı kararlarına olası etkisi",
        ],
        "I, II ve III",
        "Önemlilik yalnız sabit bir parasal eşiğe indirgenemez; büyüklük, nitelik ve "
        "işletmeye özgü koşullar kullanıcı kararlarına etkisiyle birlikte değerlendirilir.",
    ),

    # Muhasebe Kayıtları — 8 soru, "hepsi" 2/8.
    "topic-finansal-kayit-005": premise(
        "Yevmiye maddelerinin sınıflandırılmasına ilişkin aşağıdaki ifadeleri değerlendiriniz.",
        [
            "Bir hesabın borç, bir hesabın alacak tarafında olduğu kayıt karma maddedir.",
            "Bir hesap borçlandırılıp birden fazla hesap alacaklandırılırsa bileşik madde oluşur.",
            "Birden fazla hesap hem borç hem alacak tarafındaysa karma madde oluşur.",
        ],
        "II ve III",
        "Tek borçlu ve tek alacaklı kayıt basit; taraflardan biri çok hesaplıysa bileşik; "
        "iki taraf da çok hesaplıysa karma maddedir.",
    ),
    "topic-finansal-kayit-018": premise(
        "KDV dâhil 18.000 TL bedel ve %20 KDV oranı için aşağıdaki hesaplamaları değerlendiriniz.",
        [
            "KDV hariç bedel 15.000 TL'dir.",
            "KDV tutarı 3.000 TL'dir.",
            "KDV hariç bedel, 18.000 TL'nin 1,20'ye bölünmesiyle bulunur.",
        ],
        "I, II ve III",
        "18.000 / 1,20 = 15.000 TL matrah ve 18.000 - 15.000 = 3.000 TL KDV bulunur.",
    ),
    "topic-finansal-kayit-024": premise(
        "1 Kasım'da altı aylık 60.000 TL kira peşin ödenmiştir. 31 Aralık düzeltmesine ilişkin ifadeleri değerlendiriniz.",
        [
            "Aylık kira gideri 10.000 TL'dir.",
            "Kasım ve aralık aylarına ait toplam gider 20.000 TL'dir.",
            "Düzeltmede 180 Gelecek Aylara Ait Giderler hesabı borçlandırılır.",
        ],
        "I ve II",
        "Aylık tutar 60.000 / 6 = 10.000 TL, iki aylık gider 20.000 TL'dir; düzeltmede "
        "gider hesabı borçlandırılır, 180 hesap alacaklandırılır.",
    ),
    "topic-finansal-kayit-034": premise(
        "Şüpheli ticari alacağın tamamı için karşılık ayrılmasına ilişkin ifadeleri değerlendiriniz.",
        [
            "654 Karşılık Giderleri hesabı borçlandırılır.",
            "129 Şüpheli Ticari Alacaklar Karşılığı hesabı alacaklandırılır.",
            "128 Şüpheli Ticari Alacaklar hesabı karşılık kaydında kapatılır.",
        ],
        "I ve II",
        "Karşılık kaydında 654 hesap borç, 129 düzenleyici hesap alacak çalışır; alacağın "
        "kendisi 128 hesapta izlenmeye devam eder.",
    ),
    "topic-finansal-kayit-040": premise(
        "191 İndirilecek KDV 26.000 TL, 391 Hesaplanan KDV 21.000 TL'dir. Mahsup işlemine ilişkin ifadeleri değerlendiriniz.",
        [
            "İndirilecek KDV, hesaplanan KDV'den 5.000 TL fazladır.",
            "Mahsup sonrasında ödenecek KDV doğmaz.",
            "5.000 TL, 190 Devreden KDV hesabında borç bakiyesiyle izlenir.",
        ],
        "I, II ve III",
        "26.000 - 21.000 = 5.000 TL indirilecek KDV fazlası vardır; bu tutar sonraki "
        "döneme devreden KDV olarak borç bakiyesi verir.",
    ),
    "topic-finansal-kayit-048": premise(
        "Yanlışlıkla 760 hesaba borç yazılan 10.000 TL büro giderinin düzeltilmesine ilişkin ifadeleri değerlendiriniz.",
        [
            "İlk kayıttaki doğru alacak hesabı düzeltme kaydında yeniden kullanılmalıdır.",
            "Yanlış borçlandırılan 760 hesap alacaklandırılarak kapatılır.",
            "Doğru 770 Genel Yönetim Giderleri hesabı borçlandırılır.",
        ],
        "II ve III",
        "Alacak tarafı zaten doğru olduğundan yalnız gider hesapları düzeltilir: 770 hesap "
        "borçlandırılır, yanlış kullanılan 760 hesap alacaklandırılır.",
    ),
    "topic-finansal-kayit-054": premise(
        "Brüt 50.000 TL kira için 10.000 TL vergi kesilmiş, 40.000 TL bankadan ödenmiştir. Kayda ilişkin ifadeleri değerlendiriniz.",
        [
            "Kira gideri brüt 50.000 TL üzerinden borçlandırılır.",
            "10.000 TL kesinti vergi varlığı olarak borçlandırılır.",
            "102 Bankalar hesabı 40.000 TL alacaklandırılır.",
        ],
        "I ve III",
        "Brüt gider 50.000 TL'dir; 40.000 TL banka çıkışı ile 10.000 TL ödenecek vergi "
        "yükümlülüğü alacak tarafında yer alır.",
    ),
    "topic-finansal-kayit-060": premise(
        "102 Bankalar hesabındaki 35.000 TL kredi niteliğindeki alacak bakiyeye ilişkin ifadeleri değerlendiriniz.",
        [
            "Bu bakiye işletme açısından banka borcu niteliğindedir.",
            "Dönem sonunda 300 Banka Kredileri hesabına aktarılır.",
            "Finansal tablolarda negatif nakit olarak varlık grubunda bırakılır.",
        ],
        "I ve II",
        "Kredi hesabından kaynaklanan alacak bakiye nakit azalması değil finansal borçtur; "
        "300 Banka Kredileri hesabına aktarılır.",
    ),

    # Stoklar — 8 soru, "hepsi" 2/8.
    "topic-finansal-stok-001": premise(
        "TMS 2'deki stok tanımına göre aşağıdaki varlıkları değerlendiriniz.",
        [
            "Olağan iş akışında satılmak üzere elde tutulan ticari mallar",
            "Satılmak üzere üretilmekte olan yarı mamuller",
            "Üretim veya hizmet sunumunda tüketilecek ilk madde ve malzemeler",
        ],
        "I, II ve III",
        "Satış için tutulan mallar, üretim sürecindeki varlıklar ve üretimde veya hizmette "
        "tüketilecek ilk madde ve malzemeler stok tanımına girer.",
    ),
    "topic-finansal-stok-007": premise(
        "Stok alımındaki vergilerin maliyete etkisine ilişkin ifadeleri değerlendiriniz.",
        [
            "Vergi idaresinden indirilebilen KDV stok maliyetine alınmaz.",
            "İade alınamayan satın alma vergileri stok maliyetine dâhil olabilir.",
            "Bütün vergiler geri alınabilir olup olmadığına bakılmadan maliyete eklenir.",
        ],
        "I ve II",
        "Geri alınabilir veya indirilebilir vergiler maliyet dışında tutulur; geri alınamayan "
        "satın alma vergileri maliyetin bir unsuru olabilir.",
    ),
    "topic-finansal-stok-012": premise(
        "Mamul için yapılan reklam harcamasına ilişkin ifadeleri değerlendiriniz.",
        [
            "Satış ve pazarlama gideri niteliğindedir.",
            "Mamul satışından önce yapıldığı için stok maliyetine alınır.",
            "Üretim maliyetine değil, gerçekleştiği dönemin sonucuna yansır.",
        ],
        "I ve III",
        "Reklam harcaması satış ve pazarlama gideridir; satıştan önce yapılması onu stok "
        "maliyetine dönüştürmez ve gerçekleştiği dönemde giderleştirilir.",
    ),
    "topic-finansal-stok-013": premise(
        "Stokların dönüştürme maliyetlerine ilişkin ifadeleri değerlendiriniz.",
        [
            "Direkt işçilik maliyetlerini içerir.",
            "Sabit ve değişken genel üretim giderlerinin sistematik dağıtımını içerir.",
            "Reklam ve satış komisyonlarının tamamını içerir.",
        ],
        "I ve II",
        "Dönüştürme maliyetleri direkt işçilik ile üretime ilişkin genel gider paylarını "
        "kapsar; reklam ve satış giderleri kapsam dışındadır.",
    ),
    "topic-finansal-stok-018": premise(
        "Ortak üretim maliyetlerinin dağıtımına ilişkin ifadeleri değerlendiriniz.",
        [
            "Dağıtım makul ve tutarlı bir temele dayanmalıdır.",
            "Ürünlerin nispi satış değerleri dağıtım anahtarı olarak kullanılamaz.",
            "Ortak maliyetin tamamı her durumda en yüksek miktarlı ürüne yüklenir.",
        ],
        "Yalnız I",
        "Ortak maliyet makul ve tutarlı bir temelle dağıtılır. Nispi satış değeri uygun bir "
        "anahtar olabilir; maliyetin tamamını tek ürüne yüklemek kural değildir.",
    ),
    "topic-finansal-stok-020": premise(
        "Olağan kredi koşullarını aşan vadeli stok alımına ilişkin ifadeleri değerlendiriniz.",
        [
            "Peşin fiyat eşdeğeri stok maliyetinin temelidir.",
            "Peşin fiyat ile vadeli tutar arasındaki finansman unsuru süre boyunca faiz gideridir.",
            "Vadeli tutarın tamamı koşulsuz olarak ilk gün stok maliyetine alınır.",
        ],
        "I ve II",
        "Uzun vadeli finansman unsuru ayrıştırılır; stok peşin fiyat eşdeğeriyle ölçülür, "
        "aradaki fark finansman süresince faiz gideri olur.",
    ),
    "topic-finansal-stok-023": premise(
        "Ağırlıklı ortalama maliyet yöntemine ilişkin ifadeleri değerlendiriniz.",
        [
            "Dönem başı stok ile dönem içi girişlerin maliyet ve miktarlarını dikkate alır.",
            "Toplam ağırlıklandırılmış maliyet toplam miktara bölünerek birim maliyet bulunur.",
            "Ortalama, koşullara göre dönemsel olarak veya her yeni giriş sonrasında hesaplanabilir.",
        ],
        "I, II ve III",
        "Ağırlıklı ortalama maliyet, mevcut ve yeni stokların maliyetlerini miktarlarıyla "
        "ağırlıklandırır; dönemsel veya hareketli biçimde hesaplanabilir.",
    ),
    "topic-finansal-stok-024": premise(
        "TMS 2'de maliyet formüllerinin tutarlı kullanımına ilişkin ifadeleri değerlendiriniz.",
        [
            "Benzer nitelik ve kullanıma sahip stoklarda aynı maliyet formülü kullanılır.",
            "Farklı nitelik veya kullanım, farklı maliyet formülünü haklı kılabilir.",
            "Bütün stoklarda yalnız FIFO yönteminin kullanılması zorunludur.",
        ],
        "I ve II",
        "Benzer stoklarda aynı formül tutarlı uygulanır; farklı nitelik veya kullanım farklı "
        "formülü haklı kılabilir ve TMS 2 yalnız FIFO'yu zorunlu tutmaz.",
    ),

    # Dönem Sonu İşlemleri — 8 soru, "hepsi" 2/8.
    "topic-finansal-donem-002": premise(
        "TMS 16'da amortismanın başlamasına ilişkin ifadeleri değerlendiriniz.",
        [
            "Varlık yönetimin amaçladığı kullanıma hazır olduğunda amortisman başlar.",
            "Siparişin verildiği tarihte varlık kullanıma hazır olmasa da amortisman başlar.",
            "Bedelin tamamen ödenmiş olması başlangıç için zorunlu değildir.",
        ],
        "I ve III",
        "Amortisman, varlık amaçlanan yer ve durumda kullanıma hazır olduğunda başlar; "
        "ödeme veya sipariş tarihi tek başına belirleyici değildir.",
    ),
    "topic-finansal-donem-008": premise(
        "TMS 16'da amortisman yöntemine ilişkin ifadeleri değerlendiriniz.",
        [
            "Yöntem ekonomik yararların beklenen tüketim biçimini yansıtmalıdır.",
            "Yöntem en az her hesap dönemi sonunda gözden geçirilir.",
            "Tüketim biçiminde önemli değişiklik varsa yöntem tahmin değişikliği olarak değiştirilir.",
        ],
        "I, II ve III",
        "Amortisman yöntemi tüketim biçimini yansıtır, düzenli gözden geçirilir ve önemli "
        "değişiklik ortaya çıkarsa ileriye yönelik tahmin değişikliği olarak güncellenir.",
    ),
    "topic-finansal-donem-010": premise(
        "257 Birikmiş Amortismanlar hesabına ilişkin ifadeleri değerlendiriniz.",
        [
            "Maddi duran varlıkları düzenleyici aktif karakterli bir hesaptır.",
            "Varlık hesabı gibi artışlarında borçlandırılır.",
            "Kural olarak alacak bakiyesi verir.",
        ],
        "I ve III",
        "Birikmiş amortisman varlığın maliyetinden düşülen düzenleyici hesaptır ve normal "
        "koşullarda alacak bakiyesi verir.",
    ),
    "topic-finansal-donem-014": premise(
        "Bir maddi duran varlığın elden çıkarılma kaydına ilişkin ifadeleri değerlendiriniz.",
        [
            "Varlığın maliyet hesabı alacaklandırılarak kapatılır.",
            "Varlığa ait birikmiş amortisman hesabı borçlandırılarak kapatılır.",
            "Elden çıkarma farkı her durumda doğrudan sermayeye eklenir.",
        ],
        "I ve II",
        "Elden çıkarmada maliyet ve birikmiş amortisman hesapları kapatılır; net bedel ile "
        "defter değeri arasındaki fark koşullarına göre kâr veya zarardır.",
    ),
    "topic-finansal-donem-037": premise(
        "Henüz teslim edilmemiş mal için müşteriden alınan tutara ilişkin ifadeleri değerlendiriniz.",
        [
            "Malın devrine ilişkin edim henüz yerine getirilmemiştir.",
            "Tahsilat müşteriye karşı avans veya sözleşme yükümlülüğü doğurur.",
            "Bedelin banka yoluyla tahsil edilmesi tek başına satış hasılatı doğurur.",
        ],
        "I ve II",
        "Edim yerine getirilmeden alınan tutar hasılat değil müşteriye karşı yükümlülüktür; "
        "ödeme aracının banka olması sonucu değiştirmez.",
    ),
    "topic-finansal-donem-046": premise(
        "TMS 37'ye göre karşılık muhasebeleştirme koşullarını değerlendiriniz.",
        [
            "Geçmiş bir olaydan kaynaklanan mevcut yükümlülük bulunması",
            "Yükümlülüğün yerine getirilmesi için kaynak çıkışının muhtemel olması",
            "Yükümlülük tutarının güvenilir biçimde tahmin edilebilmesi",
        ],
        "I, II ve III",
        "Karşılık kaydı için geçmiş olaydan doğan mevcut yükümlülük, muhtemel kaynak çıkışı "
        "ve güvenilir ölçüm koşullarının birlikte bulunması gerekir.",
    ),
    "topic-finansal-donem-050": premise(
        "Paranın zaman değerinin önemli olduğu uzun vadeli karşılığa ilişkin ifadeleri değerlendiriniz.",
        [
            "Beklenen harcamalar uygun oranla bugünkü değere indirilir.",
            "İskontonun zamanla çözülmesi borçlanma maliyeti olarak muhasebeleştirilir.",
            "Karşılık her durumda iskonto edilmeksizin nominal tutarla bırakılır.",
        ],
        "I ve II",
        "Zaman değeri önemliyse karşılık bugünkü değerle ölçülür; iskonto etkisinin zamanla "
        "çözülmesi finansman maliyeti niteliğindedir.",
    ),
    "topic-finansal-donem-057": premise(
        "Önemli bir önceki dönem hatasının düzeltilmesine ilişkin ifadeleri değerlendiriniz.",
        [
            "Uygulanabilir olduğu ölçüde geriye dönük düzeltme yapılır.",
            "Karşılaştırmalı tutarlar veya en erken dönemin açılış bakiyeleri yeniden düzenlenir.",
            "Hata her durumda yalnız cari ve gelecek dönemlere ileriye yönelik dağıtılır.",
        ],
        "I ve II",
        "Önemli önceki dönem hataları uygulanamazlık dışında geriye dönük düzeltilir; "
        "karşılaştırmalı bilgiler veya açılış bakiyeleri yeniden düzenlenir.",
    ),

    # TMS/TFRS Uygulamaları — 8 soru, "hepsi" 2/8.
    "topic-finansal-tfrs-003": premise(
        "TMS 7'ye göre nakit benzeri bir yatırımın özelliklerini değerlendiriniz.",
        [
            "Belirli bir nakit tutarına kolayca çevrilebilir.",
            "Değer değişim riski önemsizdir.",
            "Edinim tarihinden itibaren genellikle üç ay veya daha kısa vadelidir.",
        ],
        "I, II ve III",
        "Nakit benzeri; yüksek likiditeli, belirli bir nakde kolayca çevrilebilen, önemsiz "
        "değer değişim riski taşıyan ve genellikle en çok üç ay vadeli yatırımdır.",
    ),
    "topic-finansal-tfrs-008": premise(
        "TMS 16'ya göre makinenin ilk maliyetine ilişkin ifadeleri değerlendiriniz.",
        [
            "Ticari iskontolar düşüldükten sonraki satın alma bedeli maliyete dâhildir.",
            "Kullanıma hazır olduktan sonraki olağan bakım giderleri ilk maliyete eklenir.",
            "Makineyi gerekli yere ve çalışabilir duruma getiren doğrudan giderler maliyete dâhildir.",
        ],
        "I ve III",
        "Satın alma bedeli ile varlığı gerekli yer ve duruma getiren doğrudan giderler ilk "
        "maliyettir; kullanıma hazır olduktan sonraki olağan bakım dönem gideridir.",
    ),
    "topic-finansal-tfrs-012": premise(
        "TMS 23'te özellikli varlık ve borçlanma maliyetlerine ilişkin ifadeleri değerlendiriniz.",
        [
            "Özellikli varlığın kullanıma veya satışa hazır hâle gelmesi önemli zaman gerektirir.",
            "Doğrudan ilişkilendirilebilen uygun borçlanma maliyetleri varlık maliyetine alınabilir.",
            "Edinildiğinde hemen kullanıma hazır olan varlıklar normalde özellikli varlık değildir.",
        ],
        "I, II ve III",
        "Özellikli varlık önemli hazırlık süresi gerektirir; doğrudan ilişkilendirilebilen "
        "borçlanma maliyetleri aktifleştirilir, hemen hazır varlıklar normalde kapsam dışıdır.",
    ),
    "topic-finansal-tfrs-017": premise(
        "TMS 37'de koşullu yükümlülüğe ilişkin ifadeleri değerlendiriniz.",
        [
            "Karşılık kaydı koşulları oluşmadığında finansal tablolara yükümlülük olarak alınmaz.",
            "Her koşullu yükümlülük için kesin borç kaydı yapılır.",
            "Kaynak çıkışı ihtimali uzak değilse dipnotlarda açıklanır.",
        ],
        "I ve III",
        "Karşılık koşulları oluşmamış olası yükümlülük kaydedilmez; çıkış ihtimali uzak "
        "değilse niteliği ve mümkünse finansal etkisi açıklanır.",
    ),
    "topic-finansal-tfrs-030": premise(
        "TFRS 13'te gerçeğe uygun değer ölçümüne ilişkin ifadeleri değerlendiriniz.",
        [
            "Ölçüm tarihindeki piyasa katılımcıları arasındaki olağan işlem esas alınır.",
            "Varlığın satışında elde edilecek veya yükümlülüğün devrinde ödenecek çıkış fiyatıdır.",
            "İşletmenin varlığı geçmişte edinirken ödediği özel giriş fiyatıdır.",
        ],
        "I ve II",
        "Gerçeğe uygun değer piyasa katılımcıları arasındaki olağan işlemde oluşan piyasa "
        "temelli çıkış fiyatıdır; işletmeye özgü geçmiş maliyet değildir.",
    ),
    "topic-finansal-tfrs-041": premise(
        "TFRS 10'daki kontrol değerlendirmesine ilişkin ifadeleri değerlendiriniz.",
        [
            "Yatırım yapılan işletme üzerinde güç bulunması gerekir.",
            "Yatırımcı değişken getirilere maruz kalmalı veya bu getirilerde hak sahibi olmalıdır.",
            "Kontrol için her durumda oy haklarının yüzde ellisinden fazlası zorunludur.",
        ],
        "I ve II",
        "Kontrol güç, değişken getiriler ve gücü getirileri etkilemek için kullanabilme "
        "bağlantısına dayanır; oy çoğunluğu her durumda zorunlu değildir.",
    ),
    "topic-finansal-tfrs-045": premise(
        "TFRS 12 kapsamındaki açıklamalara ilişkin ifadeleri değerlendiriniz.",
        [
            "Diğer işletmelerdeki payların niteliğini anlamaya yardımcı olur.",
            "Bu paylarla ilişkili risklerin değerlendirilmesini sağlar.",
            "Bütün müşterilerin kimlik bilgilerinin açıklanmasını zorunlu kılar.",
        ],
        "I ve II",
        "TFRS 12 diğer işletmelerdeki payların niteliği, riskleri ve finansal etkilerine "
        "odaklanır; bütün müşterilerin kimliklerinin açıklanmasını istemez.",
    ),
    "topic-finansal-tfrs-057": premise(
        "TMS 37'de yeniden yapılandırma karşılığına ilişkin ifadeleri değerlendiriniz.",
        [
            "Ayrıntılı resmî planın bulunması tek başına her durumda yeterli değildir.",
            "Uygulamanın başlaması veya duyuru yoluyla etkilenenlerde geçerli beklenti oluşması gerekir.",
            "Gelecekte yürütülecek faaliyetlerin bütün zararları karşılığa eklenir.",
        ],
        "I ve II",
        "Yapısal yükümlülük için ayrıntılı planın yanında uygulama başlangıcı veya geçerli "
        "beklenti yaratan duyuru gerekir; gelecekteki faaliyet zararları karşılığa alınmaz.",
    ),
}

LEGACY_PAD_SUFFIXES = [
    "işlem bu aşamada kesinleşmiş sayılır ve ayrıca dönem sonu değerlendirmesi yapılmaz",
    "ilgili tutar izleyen dönemlerde de aynı hesapta herhangi bir değişiklik yapılmadan korunur",
    "bu sınıflandırma işlem koşullarından bağımsız olarak bütün işletmelerde zorunlu uygulanır",
    "sonraki ölçümde ortaya çıkan farklar finansal tablolara hiçbir koşulda yansıtılmaz",
    "uygulamada ekonomik öz ve gerçekleşme zamanı ayrıca değerlendirmeye alınmaz",
    "bu nedenle tutarın tamamı doğrudan cari dönemin faaliyet sonucuyla ilişkilendirilir",
    "işlem yalnız ödeme tarihindeki hukuki biçimine göre kesin olarak muhasebeleştirilir",
    "aynı yöntem işletmenin faaliyet yapısına bakılmaksızın sonraki dönemlerde de sürdürülür",
]

PAD_SUFFIXES = [
    "bu değerlendirme ilgili işlemin muhasebeleştirilmesinde esas alınır",
    "ilgili kalem finansal tablolarda bu yaklaşım kullanılarak sunulur",
    "işlemin dönem sonu kaydı bu yöntem esas alınarak tamamlanır",
    "söz konusu tutar bu sınıflandırma çerçevesinde raporlanır",
    "uygulama benzer nitelikteki işlemlere de aynı biçimde yansıtılır",
    "bu ölçüt ilgili kalemin sonraki muhasebeleştirmesinde de dikkate alınır",
    "finansal tablo sunumunda bu sonuca göre işlem yapılır",
    "ilgili hesap veya kalem bu esasa göre belirlenir",
]

# Denetim eşiklerini geçmek için anlamsız dolgu kullanmak yerine soru bağlamına
# özgü, elle yazılmış yakın çeldiriciler ve kısa hesap kodu seçenekleri kullanılır.
CURATED_REPLACEMENTS = {
    "topic-finansal-temel-002": {
        "Önemlilik": "İşletmenin sürekliliği",
    },
    "topic-finansal-temel-005": {
        "Tutarlılık": "Sosyal sorumluluk",
    },
    "topic-finansal-temel-013": {
        "Süreklilik": "İşletmenin sürekliliği",
    },
    "topic-finansal-temel-028": {
        "Süreklilik": "İşletmenin sürekliliği",
    },
    "topic-finansal-temel-041": {
        "Süreklilik": "İşletmenin sürekliliği",
    },
    "topic-finansal-kayit-043": {
        "591 Dönem Net Zararı": "591 hesabı",
        "692 Dönem Net Kârı veya Zararı": "692 hesabı",
        "590 Dönem Net Kârı": "590 hesabı",
        "570 Geçmiş Yıllar Kârları": "570 hesabı",
        "691 Dönem Kârı Vergi ve Diğer Yasal Yükümlülük Karşılıkları": "691 hesabı",
    },
    "topic-finansal-donem-005": {
        "En azından her hesap dönemi sonunda": "Her hesap dönemi sonunda",
    },
    "topic-finansal-donem-030": {
        "Gelecek dönem gelirini artırmak için": "Gelecek dönemin gelir ve kârını artırmak için",
        "Elektriği duran varlık yapmak için": "Elektrik bedelini maddi duran varlık maliyetine aktarmak için",
    },
    "topic-finansal-donem-036": {
        "Varlıkları azaltır, borçları artırır.": "Varlıkları azaltıp finansal borçları ve dönem giderini artırır.",
        "Finansal tabloları etkilemez.": "Tahsilat yapılmadığı için finansal tablolarda hiçbir etki doğurmaz.",
    },
    "topic-finansal-donem-041": {
        "Alacak azalır, kambiyo zararı doğar.": "Ticari alacak azalır ve 14.000 TL kambiyo zararı doğar.",
        "Stok maliyeti artar.": "Stok maliyeti ve dönem gideri 14.000 TL artar.",
    },
    "topic-finansal-donem-042": {
        "Borç azalır, gelir artar.": "Borç azalır ve kambiyo geliri artar.",
        "Borç ve kambiyo kârı artar.": "Borç artar ve kambiyo kârı doğar.",
    },
    "topic-finansal-donem-045": {
        "Daha önce ayrılan değer düşüklüğü ve maliyet sınırı": "Daha önce ayrılan 10.000 TL",
    },
    "topic-finansal-tfrs-015": {
        "Yıllık rapordaki bütün dipnotların aynen tekrarlanması zorunludur.": "Ara dönem raporunda yıllık finansal rapordaki bütün tablo ve dipnotların değişmeden tekrarlanması zorunludur.",
        "Sadece yönetim kurulu faaliyet raporu yeterlidir.": "Ara dönem için yalnız yönetim kurulu faaliyet raporunun yayımlanması finansal raporlama bakımından yeterlidir.",
    },
    "topic-finansal-tfrs-018": {
        "Süresiz ömürlü varlık kaydetmek": "Süresiz yararlı ömürlü maddi olmayan duran varlık olarak aktifleştirmek",
        "Şerefiye olarak aktifleştirmek": "İşletme birleşmesinden doğan şerefiye olarak aktifleştirmek",
    },
    "topic-finansal-tfrs-026": {
        "Daima finansal varlığın maliyetine eklenir.": "İşlem maliyetlerini finansal varlığın ilk defter değerine ekleyip vadesi boyunca itfa etmek",
        "Özkaynakta süresiz bekletilir.": "İşlem maliyetlerini özkaynakta ayrı bir yedek hesabında süresiz olarak bekletmek",
    },
    "topic-finansal-tfrs-047": {
        "Hizmet koşulu önemsenmez ve bütün gider korunur.": "Hizmet koşulunun gerçekleşmemesi hak kazanmayı etkilemez; çalışan ayrılsa da önceki ve gelecekteki tüm hizmet giderleri korunur.",
        "Gider yalnız vergi beyannamesine yazılır.": "Çalışanın ayrılması yalnız vergi beyannamesini etkiler; TFRS 2 kapsamında kümülatif giderlerde düzeltme yapılmaz.",
    },
}


def gen_letters(seed: int, n_each: int = 12) -> list[str]:
    """Her harften 12; run en fazla 2; kısa periyot ve düşük bigram yok."""
    rng = random.Random(seed)
    while True:
        seq = list("ABCDE") * n_each
        rng.shuffle(seq)
        runs_ok = all(
            not (seq[i] == seq[i - 1] == seq[i - 2])
            for i in range(2, len(seq))
        )
        periodic = any(
            sum(seq[i] == seq[i + p] for i in range(len(seq) - p))
            / (len(seq) - p)
            >= 0.9
            for p in range(1, 11)
        )
        bigrams = {seq[i] + seq[i + 1] for i in range(len(seq) - 1)}
        if runs_ok and not periodic and len(bigrams) >= 13:
            return seq


def normalized_length(text: str) -> int:
    return len(re.sub(r"\*{1,2}", "", text).strip())


def has_premises(question: str) -> bool:
    return len(re.findall(r"(?m)^\s*(?:IV|I{1,3}|V)[.)]\s", question)) >= 2


def is_length_tell(question: dict) -> bool:
    if has_premises(question["question"]):
        return False
    lengths = {
        key: normalized_length(value)
        for key, value in question["choices"].items()
    }
    answer_length = lengths[question["correctAnswer"]]
    ordered = sorted(lengths.values(), reverse=True)
    return (
        answer_length == ordered[0]
        and answer_length >= 1.5 * ordered[1]
        and answer_length >= 45
    ) or (
        ordered[1] >= 1.7 * ordered[2]
        and ordered[1] >= 45
        and answer_length >= ordered[1]
    )


def add_padding(text: str, suffix: str) -> str:
    return f"{text.rstrip().rstrip('.')}; {suffix}."


def strip_generated_padding(text: str) -> str:
    """Önceki çalıştırmalarda eklenen mekanik tamamlayıcıları geri söker."""
    suffixes = LEGACY_PAD_SUFFIXES + PAD_SUFFIXES
    while True:
        matched = False
        for suffix in suffixes:
            token = f"; {suffix}."
            if text.endswith(token):
                text = text[:-len(token)].rstrip() + "."
                matched = True
                break
        if not matched:
            return text


def apply_curated_replacements(question: dict) -> None:
    replacements = CURATED_REPLACEMENTS.get(question["id"], {})
    for old, new in replacements.items():
        matching = [
            letter for letter, text in question["choices"].items()
            if text == old
        ]
        if matching:
            assert len(matching) == 1, (question["id"], old, matching)
            question["choices"][matching[0]] = new
            continue
        if new in question["choices"].values():
            continue
        raise AssertionError(
            f"{question['id']}: hedef seçenek bulunamadı: {old!r}"
        )


def balance_distractor_lengths(question: dict) -> None:
    if not is_length_tell(question):
        return
    answer = question["correctAnswer"]
    answer_length = normalized_length(question["choices"][answer])
    target = min(145, max(55, math.ceil(answer_length * 0.76)))
    distractor_letters = [letter for letter in "ABCDE" if letter != answer]
    distractor_letters.sort(
        key=lambda letter: normalized_length(question["choices"][letter]),
        reverse=True,
    )
    chosen = distractor_letters[:2]
    used_suffixes = set()
    for position, letter in enumerate(chosen):
        suffix_index = int(
            hashlib.sha256(f"{question['id']}:{letter}".encode()).hexdigest()[:8],
            16,
        ) % len(PAD_SUFFIXES)
        while normalized_length(question["choices"][letter]) < target:
            while PAD_SUFFIXES[suffix_index % len(PAD_SUFFIXES)] in used_suffixes:
                suffix_index += 1
            suffix = PAD_SUFFIXES[(suffix_index + position) % len(PAD_SUFFIXES)]
            while suffix in used_suffixes:
                suffix_index += 1
                suffix = PAD_SUFFIXES[(suffix_index + position) % len(PAD_SUFFIXES)]
            question["choices"][letter] = add_padding(
                question["choices"][letter],
                suffix,
            )
            used_suffixes.add(suffix)
            suffix_index += 1
    assert not is_length_tell(question), question["id"]


def apply_premise(question: dict) -> None:
    replacement = PREMISES.get(question["id"])
    if replacement is None:
        return
    question["question"] = replacement["question"]
    question["explanation"] = replacement["explanation"]
    question["_correct_text"] = replacement["correct"]
    question["_distractors"] = replacement["distractors"]


def permute(question: dict, answer_letter: str, seed: int) -> None:
    correct_text = question.pop(
        "_correct_text",
        question["choices"][question["correctAnswer"]],
    )
    distractors = question.pop(
        "_distractors",
        [
            text
            for letter, text in question["choices"].items()
            if letter != question["correctAnswer"]
        ],
    )
    distractors = sorted(distractors)
    rng = random.Random(
        seed
        + int(hashlib.sha256(question["id"].encode()).hexdigest()[:8], 16)
    )
    rng.shuffle(distractors)
    choices = {}
    distractor_iter = iter(distractors)
    for letter in "ABCDE":
        choices[letter] = correct_text if letter == answer_letter else next(distractor_iter)
    question["choices"] = choices
    question["correctAnswer"] = answer_letter
    assert question["choices"][question["correctAnswer"]] == correct_text


def load_packages() -> dict[str, list[dict]]:
    return {
        filename: json.loads((CONTENT / filename).read_text(encoding="utf-8"))
        for filename in FILES
    }


def current_answers(packages: dict[str, list[dict]]) -> dict[str, str]:
    return {
        question["id"]: question["choices"][question["correctAnswer"]]
        for questions in packages.values()
        for question in questions
    }


def verify(packages: dict[str, list[dict]]) -> None:
    expected = json.loads(BASELINE.read_text(encoding="utf-8"))
    actual = current_answers(packages)
    assert actual == expected, "Doğru seçenek metinleri baseline ile eşleşmiyor."
    for filename, questions in packages.items():
        assert len(questions) == 60, filename
        premise_questions = [q for q in questions if has_premises(q["question"])]
        assert len(premise_questions) == 8, (filename, len(premise_questions))
        all_answers = sum(
            q["choices"][q["correctAnswer"]] == "I, II ve III"
            for q in premise_questions
        )
        assert all_answers == 2, (filename, all_answers)
        assert all(not is_length_tell(q) for q in questions), filename
    print(f"Doğru metin doğrulandı: {len(actual)} soru")
    print("Öncüllü dağılım: her pakette 8 soru, 'hepsi' 2/8 (%25)")
    print("Length-tell: 0")


def write_packages(packages: dict[str, list[dict]]) -> None:
    roots = (
        CONTENT,
        ROOT.parent / "smmm_sgs_pratik" / "assets" / "content" / "yeterlilik",
    )
    for root in roots:
        root.mkdir(parents=True, exist_ok=True)
        for filename, questions in packages.items():
            (root / filename).write_text(
                json.dumps(questions, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    packages = load_packages()
    if args.verify:
        verify(packages)
        return

    for questions in packages.values():
        for question in questions:
            question["choices"] = {
                letter: strip_generated_padding(text)
                for letter, text in question["choices"].items()
            }
            apply_premise(question)
            apply_curated_replacements(question)

    pre_shuffle_answers = {
        question["id"]: question.get(
            "_correct_text",
            question["choices"][question["correctAnswer"]],
        )
        for questions in packages.values()
        for question in questions
    }

    for filename, questions in packages.items():
        letters = gen_letters(FILES[filename])
        assert len(questions) == len(letters), filename
        for question, answer_letter in zip(questions, letters):
            permute(question, answer_letter, FILES[filename])
            assert (
                question["choices"][question["correctAnswer"]]
                == pre_shuffle_answers[question["id"]]
            )
            balance_distractor_lengths(question)

    BASELINE.write_text(
        json.dumps(pre_shuffle_answers, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_packages(packages)
    verify(load_packages())


if __name__ == "__main__":
    main()
