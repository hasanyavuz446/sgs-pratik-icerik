# -*- coding: utf-8 -*-
"""muhasebe_standartlari — dosya dosya şık örüntüsü düzeltmesi.

Motor (dolgu_engine) mekanik kısmı yapar: dolgu kuyruklarını kırpar. Burada
dosyaya özel İÇERİK durur:

  atma : 24-33 kez tekrarlanan "Bu husus TMS X'te düzenlenmemiş olup işletmenin
         serbest takdirine bırakılmıştır" şıkkının yerine geçecek, O STANDARDA
         ait gerçek kavram yanılgıları. Sırayla dağıtılır ki yeni bir kalıp
         doğmasın.
  kisalt: doğrunun ALTINA yazılmış çeldiriciler. Kırpmanın tavanı var; doğru şık
         kısa kaldığında "en kısayı seç" ~%40 tutuyor. 4 çeldiricinin hepsi
         kısaltılırsa doğru EN UZUN, tek çeldirici kısaltılırsa ORTA olur.
         Hedef: en uzun ~%20 · en kısa ~%20 · ortada ~%60.
  uzat : ters kusurlu dosyalar için (doğru şık EN UZUN) — çeldirici doğrunun
         EN AZ 15 KARAKTER üstüne çıkarılır.

Kullanım:
    python3 tools/sgs/builders/rebalance_standartlar.py <dosya_anahtarı>
    python3 tools/sgs/builders/rebalance_standartlar.py <dosya_anahtarı> --rapor
        (yazmadan ölç: kırpma sonrası hangi soruda doğru en kısa/en uzun kalıyor,
         hedef uzunluk kaç — KISALT/UZAT listesini bu dökümle yaz, göz kararıyla
         değil; göz kararı önceki dosyalarda tur yaktırdı)
"""
from __future__ import annotations

import json
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from dolgu_engine import ONCUL, rapor, temizle  # noqa: E402

KOK = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/muhasebe_standartlari"

# ── TMS 12 · Gelir Vergileri ──────────────────────────────────────────────────
# 41/60 soruda atma-şıkkı vardı (ve neredeyse hep D/E'de — konumu bile ele
# veriyordu). Yerine geçen yanılgılar standardın GERÇEK karışıklıkları:
# varlık↔borç yönü · iskonto yasağı · ilk muhasebeleştirme istisnası ·
# netleştirme koşulu · kalıcı ↔ geçici fark · oranın hangi dönemden alınacağı.
# Her biri ancak TMS 12 bilinirse elenir; bu, atma-şıkkının tam tersidir.
# ⚠ SIRA: ÖZELDEN GENELE — ilk eşleşen kazanır. İlk yazdığımda genel kurallar
# yukarıdaydı ve atamayı sessizce bozuyordu: "muhasebe kârı" kuralı mutabakat
# sorusunu (kökünde "muhasebe kârı" geçiyor), "cari vergi" kuralı da cari vergi
# NETLEŞTİRMESİ sorusunu kapıyordu. Aynı özel↔genel hatası ADLASTIRMA'da da
# çıkmıştı; kural listesi yazarken varsayılan olarak özeli üste koy.
#
# ⚠ Genel yedek nadir kalmalı. İlk denemede 6 soru yedeğe düşüyordu; tek metin
# 6 kez tekrarlanınca yedeğin kendisi yeni bir atma-şıkkına dönüşür.
TMS12_ATMA = [
    # ── yön soruları: defter değeri ↔ vergiye esas değer (en özel) ──
    (r"bir borcun defter değerinin vergiye esas değerinden YÜKSEK",
     "Vergiye tabi geçici fark doğar; ertelenmiş vergi borcu muhasebeleştirilir"),
    (r"defter değerinin vergiye esas değerinden YÜKSEK",
     "İndirilebilir geçici fark doğar; ertelenmiş vergi varlığı muhasebeleştirilir"),
    (r"defter değerinin vergiye esas değerinden DÜŞÜK",
     "Vergiye tabi geçici fark doğar; ertelenmiş vergi borcu muhasebeleştirilir"),
    (r"muhasebe amortismanının vergi amortismanından DÜŞÜK",
     "Defter değeri vergiye esas değerin altında kalır; indirilebilir fark ve ertelenmiş vergi varlığı doğar"),
    (r"muhasebe amortismanının vergi amortismanından YÜKSEK",
     "Defter değeri vergiye esas değerin üstünde kalır; vergiye tabi fark ve ertelenmiş vergi borcu doğar"),
    # ── senaryolar ──
    (r"şüpheli alacak karşılığı",
     "Vergiye tabi geçici fark doğar; ertelenmiş vergi borcu kaydedilir"),
    (r"fiilen ödendiğinde indirilebilen",
     "Kalıcı fark doğurur; bu nedenle ertelenmiş vergi hesaplanmaz"),
    (r"hiçbir zaman indirilemeyecek|kanunen kabul edilme",
     "Kalıcı fark doğurur; bu fark için de ertelenmiş vergi hesaplanır"),
    (r"geçmişte sürekli zarar etmiş",
     "Geçmiş zararlar dikkate alınmaz; ertelenmiş vergi varlığı her hâlde tam tutarıyla kaydedilir"),
    (r"gelecekte yeterli vergi",
     "Varlık defter değeriyle korunur; yeterli kâr beklentisi olmasa dahi azaltılmaz"),
    (r"bağlı ortaklık|iştirak|iş ortaklık",
     "Yatırımlara ilişkin farklar için her hâlde borç kaydedilir; kontrol ve zamanlama dikkate alınmaz"),
    (r"işletme birleşmesinde edinilen",
     "Birleşmede doğan geçici farklar için ertelenmiş vergi kaydedilmez; şerefiye bundan etkilenmez"),
    (r"şerefiyenin ilk muhasebeleştirilmesi",
     "Şerefiyenin ilk muhasebeleştirilmesinden doğan fark için ertelenmiş vergi borcu kaydedilir"),
    (r"ilk muhasebeleştirme istisnası",
     "İstisna yalnızca işletme birleşmelerinde uygulanır; birleşme dışı işlemleri kapsamaz"),
    # ── ölçüm ve sunum ──
    (r"vergi oranının değişmesi",
     "Oran değişikliği yalnızca yeni işlemlere uygulanır; mevcut bakiyeler eski oranla kalır"),
    (r"iskonto",
     "Paranın zaman değeri dikkate alınarak etkin faiz yöntemiyle bugünkü değerine indirgenir"),
    (r"geri kazanılma biçimi",
     "Geri kazanma biçimi dikkate alınmaz; satış ve kullanım için aynı oran uygulanır"),
    (r"ölçümünde kullanılacak oran",
     "Geçmiş beş yılın ortalama efektif vergi oranı esas alınarak ölçülür"),
    (r"netleştir",
     "Yasal mahsup hakkı aranmaksızın tüm bakiyeler her hâlde netleştirilerek tek satırda gösterilir"),
    (r"sınıflandır",
     "Ters dönme zamanına göre dönen ve duran varlık olarak ikiye ayrılarak gösterilir"),
    (r"mutabakat",
     "Mutabakat yalnızca vergi idaresine sunulur; finansal tablo dipnotlarında yer almaz"),
    (r"açıklamalar",
     "Yalnızca ödenecek vergi tutarı açıklanır; giderin bileşenlerine yer verilmez"),
    (r"gözden geçir",
     "Defter değeri ilk kayıttan sonra gözden geçirilmez; tutar dönem sonlarında sabit kalır"),
    (r"muhasebeleştirileceği yer",
     "Vergi, ilgili işlem nereye kaydedilirse kaydedilsin doğrudan özkaynaklarda gösterilir"),
    (r"diğer kapsamlı gelir|yeniden değerlen",
     "İlgili vergi, işlem nerede muhasebeleştirilirse muhasebeleştirilsin kâr veya zarara yazılır"),
    # ── muhasebeleştirme ölçütü ──
    (r"ertelenmiş vergi borçlarının muhasebeleştirilmesi",
     "Yalnızca ters dönmesi bir yıl içinde beklenen farklar için muhasebeleştirilir"),
    (r"ertelenmiş vergi varlıklarının muhasebeleştirilmesi",
     "Gelecekte kâr elde edilip edilmeyeceğine bakılmaksızın tam tutarıyla muhasebeleştirilir"),
    (r"mali zarar",
     "Devreden mali zararlar için hiçbir koşulda ertelenmiş vergi varlığı kaydedilemez"),
    (r"vergiye tabi kâr kaynakları",
     "Yalnızca geçmiş dönemlerde fiilen elde edilmiş kârlar dikkate alınır"),
    # ── tanımlar ──
    (r"vergiye tabi geçici fark",
     "Gelecek dönemlerde indirilebilir tutar doğurur; ertelenmiş vergi varlığı yaratır"),
    (r"indirilebilir geçici fark",
     "Gelecek dönemlerde vergiye tabi tutar doğurur; ertelenmiş vergi borcu yaratır"),
    (r"geçici fark",
     "Muhasebe kârı ile mali kâr arasında doğan ve hiçbir zaman ters dönmeyen kalıcı farklardır"),
    (r"ertelenmiş vergi borcu",
     "İndirilebilir geçici farklar üzerinden gelecekte geri kazanılacak vergi tutarıdır"),
    (r"ertelenmiş vergi varlığı",
     "Vergiye tabi geçici farklar üzerinden gelecekte ödenecek vergi tutarıdır"),
    (r"vergiye esas değer",
     "Bir varlık veya borcun raporlama tarihindeki gerçeğe uygun değerini ifade eder"),
    (r"ödenmemiş vergi",
     "Ödenen tutar borcu aşsa dahi aşan kısım doğrudan gider yazılır; varlık olarak kaydedilmez"),
    (r"dönem vergi gideri",
     "Yalnızca vergi dairesine fiilen ödenen cari vergiden oluşur; ertelenmiş vergi bu tutara girmez"),
    (r"cari vergi",
     "Gelecek dönemlerde geri kazanılacak ya da ödenecek vergi tutarını ifade eder"),
    (r"muhasebe kârı ile vergiye tabi kâr arasındaki ilişki",
     "İkisi aynı kurallara dayandığından her dönemde birbirine eşit olur"),
    (r"vergiye tabi kâr|mali kâr",
     "Finansal tablolarda raporlanan, vergi gideri düşülmeden önceki dönem kârıdır"),
    (r"muhasebe kârı",
     "Vergi mevzuatının kurallarına göre hesaplanan ve üzerinden vergi ödenen dönem kârıdır"),
    (r"amacı",
     "İşletmenin ödeyeceği vergiyi en aza indirecek yöntemleri belirlemeyi amaçlar"),
    # genel yedek — hiçbir anahtar tutmazsa
    (r"", "Ertelenmiş vergi yalnızca vergi idaresi talep ettiğinde hesaplanır; standart bunu zorunlu kılmaz"),
]

# Çakışma yüzünden ilk eşleşen kuralın kullanılamadığı 4 soru. Motorun çakışma
# koruması sıradaki kurala düşüyor, o da KONU DIŞI bir tanım getiriyordu
# ("…gerçeğe uygun değerini ifade eder", bir "ne olur?" sorusunun altında) —
# yani atma-şıkkını başka bir bedava elemeyle değiştiriyordu. Bunlar elle.
TMS12_OZEL = {
    "std-tms12-gen-0016": "Fark yalnızca varlık satıldığında dikkate alınır; elde tutuldukça ertelenmiş vergi doğmaz",
    "std-tms12-gen-0056": "Kalıcı fark doğar; karşılık vergisel olarak hiç indirilemeyeceğinden ertelenmiş vergi hesaplanmaz",
    "std-tms12-gen-0057": "Fark doğrudan özkaynaklarda muhasebeleştirilir; kâr veya zararı hiç etkilemez",
    "std-tms12-gen-0058": "Borçlarda geçici fark doğmaz; geçici fark yalnızca varlıklar için hesaplanır",
}

# Kırpma + atma sonrası doğru şık 21/53 soruda TEK BAŞINA en uzun kalıyordu
# (%40). Hedef ~%20 → 10 soruda çeldirici doğrunun üstüne çıkarılıyor, 11'i
# kasten en uzun bırakılıyor. Uzatmalar dolguyla değil İÇERİKLE: her biri
# yanlış kuralı sonuna kadar söyleyip kendi içinde tutarlı bir yanılgı kuruyor.
TMS12_UZAT = {
    "std-tms12-gen-0001": {"B": "İşletmenin ödeyeceği vergi tutarını en aza indirecek yöntemleri belirlemek ve vergi planlamasında izlenecek adımları bir rehber olarak sunmaktır"},
    "std-tms12-gen-0003": {"C": "İşletmenin gelecekte elde etmeyi beklediği kârı ifade eder; bu tutar bütçe verilerine göre hesaplanır ve dönemin vergi matrahı olarak kullanılır"},
    "std-tms12-gen-0005": {"E": "Yalnızca vergi dairesine fiilen ödenen cari vergiden oluşur; ertelenmiş vergi bu tutara girmez ve gelir tablosunda ayrı bir kalem olarak raporlanmaz"},
    "std-tms12-gen-0013": {"C": "Cari dönemde vergi dairesine fiilen ödenmesi gereken vergi tutarını ifade eder; gelecek dönemlere sarkan indirilebilir farklar bu tanımın dışında kalır"},
    "std-tms12-gen-0018": {"E": "Gelecekte kâr elde edilip edilmeyeceğine bakılmaksızın tam tutarıyla muhasebeleştirilir; muhtemellik değerlendirmesi yalnızca ertelenmiş vergi borçları için yapılır"},
    "std-tms12-gen-0020": {"A": "Her hâlde cari dönemde geçerli olan vergi oranı kullanılır; gelecekte yürürlüğe gireceği bilinen oran değişiklikleri ölçümde hiç dikkate alınmaz"},
    "std-tms12-gen-0037": {"D": "İstisna yalnızca vergi idaresi izin verdiğinde uygulanır; izin alınmadığı sürece her işlem için ertelenmiş vergi kaydedilir ve istisna hiç işlemez"},
    "std-tms12-gen-0038": {"E": "İlgili vergi, işlem nerede muhasebeleştirilirse muhasebeleştirilsin kâr veya zarara yazılır; diğer kapsamlı gelirde vergi etkisi hiçbir hâlde gösterilmez"},
    "std-tms12-gen-0040": {"D": "Yatırımlara ilişkin farklar için her hâlde ertelenmiş vergi borcu kaydedilir; ana ortaklığın kontrolü ve farkın ne zaman ters döneceği dikkate alınmaz"},
    "std-tms12-gen-0054": {"A": "Yalnızca geçmiş dönemlerde fiilen elde edilmiş kârlar dikkate alınır; gelecekteki kâr beklentisi ve mevcut vergiye tabi farklar değerlendirmeye girmez"},
}

# ── TMS 21 · Kur Değişimi ─────────────────────────────────────────────────────
# 34 soruda atma-şıkkı; her biri ayrı alt konu olduğu için tek tek yanılgı
# yazıldı (anahtar-kelime havuzu yerine soru-başına, çakışma riski sıfır).
# Her metin TMS 21'in gerçek bir karışıklığı: parasal↔parasal olmayan · işlem
# tarihi↔kapanış kuru · kâr-zarar↔diğer kapsamlı gelir · çevrim yönü.
TMS21_OZEL = {
    "std-tms21-gen-0001": "İşletmenin kayıtlı bulunduğu ülkenin resmî para birimidir",
    "std-tms21-gen-0002": "Her hâlde işletmenin geçerli para birimiyle aynı olmak zorundadır",
    "std-tms21-gen-0003": "İşletmenin bulunduğu ülke dışındaki tüm ülkelerin para birimleridir",
    "std-tms21-gen-0006": "En yüksek işlem hacmine sahip para birimi kendiliğinden geçerli sayılır",
    "std-tms21-gen-0007": "Değişiklik geriye dönük uygulanır ve önceki dönemler yeniden düzenlenir",
    "std-tms21-gen-0008": "Gelecekte mal veya hizmet olarak alınacak tüm kalemleri kapsar",
    "std-tms21-gen-0013": "Her hâlde ana ortaklığın geçerli para birimi esas alınır",
    "std-tms21-gen-0016": "Geçmiş dönem karşılaştırmalı tutarları da yeni para birimine çevrilir",
    "std-tms21-gen-0017": "İşlem tarihindeki değil, raporlama dönemi sonundaki kapanış kuru uygulanır",
    "std-tms21-gen-0018": "Her hâlde raporlama dönemi sonundaki kapanış kuru kullanılır",
    "std-tms21-gen-0019": "İşlem tarihindeki tarihî kur kullanılarak çevrilir ve değişmez",
    "std-tms21-gen-0020": "Raporlama dönemi sonundaki kapanış kuru kullanılarak çevrilir",
    "std-tms21-gen-0021": "İşlem tarihindeki tarihî kur kullanılarak çevrilir",
    "std-tms21-gen-0023": "İlgili kur farkı her hâlde kâr veya zarara yansıtılır",
    "std-tms21-gen-0027": "Makine parasal kalem sayılır; kapanış kuruyla çevrilir ve kur farkı doğar",
    "std-tms21-gen-0029": "Doğrudan dönemin kâr veya zararında muhasebeleştirilir",
    "std-tms21-gen-0030": "Yalnızca yabancı para cinsinden nakit tahsilat ve ödemeleri kapsar",
    "std-tms21-gen-0031": "İşlem tarihindeki tarihî kurlarla çevrilir",
    "std-tms21-gen-0032": "Kapanış kuru kullanılarak çevrilir",
    "std-tms21-gen-0033": "Doğrudan dönemin kâr veya zararında muhasebeleştirilir",
    "std-tms21-gen-0034": "Özkaynakta biriken kur farkları özkaynakta kalır; kâr veya zarara aktarılmaz",
    "std-tms21-gen-0035": "Şerefiye raporlayan işletmenin para biriminde sabitlenir; çevrilmez",
    "std-tms21-gen-0037": "İşletme geçerli para birimini raporlama para birimine eşitlemek zorundadır",
    "std-tms21-gen-0038": "Düzeltme yapılmadan doğrudan kapanış kuruyla çevrilir",
    "std-tms21-gen-0041": "Gerçekleşen kur farkı doğrudan özkaynakta muhasebeleştirilir",
    "std-tms21-gen-0043": "TFRS 9 kapsamındaki türev işlemler de dâhil tüm yabancı para kalemlerini kapsar",
    "std-tms21-gen-0048": "Alacak ve borç netleştirilir; net tutar üzerinden tek kur farkı hesaplanır",
    "std-tms21-gen-0049": "Parasal kalemdir; kapanış kuruyla çevrilir ve kur farkı doğar",
    "std-tms21-gen-0050": "Parasal kalemdir; her dönem sonu kapanış kuruyla yeniden çevrilir",
    "std-tms21-gen-0053": "Yine de tüm kalemler kapanış kuruyla yeniden çevrilir",
    "std-tms21-gen-0054": "Ödemenin fiilen yapıldığı tarihteki kur esas alınır",
    "std-tms21-gen-0056": "İşlem tarihindeki tarihî kurla çevrilir; kur farkı doğmaz",
    "std-tms21-gen-0058": "TMS 21 kur farklarının ilgili varlığın maliyetine eklenmesini zorunlu kılar",
    "std-tms21-gen-0060": "Bağlı ortaklığın tabloları çevrilmez; ana ortaklığın para biriminde düzenlenir",
}

# 18 soruda doğru tek başına en uzun; ~11'i uzatılıp 7'si en uzun bırakılıyor
# (hedef ~%20). Uzatmalar DOLGU SÖZCÜĞÜ İÇERMEZ — yoksa "dolguyu ele, en uzunu
# seç" stratejisi onları atar ve boy dengesi kâğıt üstünde kalır.
TMS21_UZAT = {
    "std-tms21-gen-0005": {"A": "Geçerli para birimi belirlenirken yalnızca finansman faaliyetlerinden sağlanan fonların hangi para biriminde olduğuna bakılır; satış fiyatları ve maliyet göstergeleri hiç dikkate alınmaz"},
    "std-tms21-gen-0007": {"C": "Geçerli para birimi bir kez belirlendikten sonra hiçbir hâlde değiştirilemez; temel ekonomik çevre değişse dahi ilk belirleme kalıcı olarak geçerli kalır"},
    "std-tms21-gen-0008": {"D": "İşletmenin gelecekte mal veya hizmet olarak teslim edeceği ya da teslim alacağı, tutarı sözleşmeyle önceden belirlenmiş bütün varlık ve borçları kapsayan geniş bir tanımdır"},
    "std-tms21-gen-0016": {"B": "Değişiklik hâlinde geçmişe dönük tam bir yeniden düzenleme yapılır; önceki tüm dönemlerin tutarları yeni geçerli para birimi cinsinden baştan hesaplanır"},
    "std-tms21-gen-0032": {"B": "Gelir ve giderler her hâlde dönem başındaki açılış kuru kullanılarak çevrilir; işlem tarihleri ve dönemin ortalama kuru bu çevrimde hiç dikkate alınmaz"},
    "std-tms21-gen-0037": {"D": "İşletme bu durumda geçerli para birimini terk eder ve tüm kayıtlarını raporlama para birimi üzerinden yeniden oluşturarak karşılaştırmalı dönemleri de bu birime göre düzeltir"},
    "std-tms21-gen-0039": {"E": "Yabancı para kredinin vadesinde ödenmesi sırasında ortaya çıkan kur farkı, kredinin finanse ettiği varlığın maliyetine eklenir ve dönemin giderlerine hiç yansıtılmaz"},
    "std-tms21-gen-0048": {"C": "Alacak ve borç eşit tutarda olduğundan birbirini tümüyle götürür; hiçbir kur farkı doğmaz ve finansal tablolara herhangi bir etki yansımaz"},
    "std-tms21-gen-0056": {"B": "Yeniden değerleme modeliyle ölçülen arsa her hâlde ilk işlem tarihindeki tarihî kur ile çevrilir; değerlemeden doğan kur farkı hiçbir zaman muhasebeleştirilmez"},
    "std-tms21-gen-0058": {"B": "Ortaya çıkan tüm kur farkları, tutarı ne olursa olsun ilgili varlığın maliyetine eklenir ve hiçbir hâlde doğrudan dönemin kâr veya zararına yansıtılmaz"},
    "std-tms21-gen-0060": {"C": "Bağlı ortaklığın finansal tabloları hiçbir çevrime tabi tutulmadan, doğrudan ana ortaklığın geçerli para birimi cinsinden yeni baştan düzenlenerek konsolide edilir"},
}

# ── TFRS 9 · Finansal Araçlar ─────────────────────────────────────────────────
# 41 soruda atma-şıkkı; alt konular tümüyle ayrı (sınıflandırma · ölçüm · etkin
# faiz · beklenen kredi zararı · bilanço dışı bırakma · korunma) → soru-başına
# gerçek TFRS 9 yanılgısı. Sık karışıklıklar: gerçekleşmiş↔beklenen kredi zararı
# modeli · brüt↔net defter değeri · kâr-zarar↔diğer kapsamlı gelir · özkaynak
# GUDDKG'de kâr-zarara yeniden sınıflandırma YOK.
TFRS9_OZEL = {
    "std-tfrs9-gen-0001": "Yalnızca borsada işlem gören menkul kıymetleri kapsayan dar bir kavramdır",
    "std-tfrs9-gen-0003": "İşletmenin gelecekte mal veya hizmet sunma yükümlülüklerini de kapsar",
    "std-tfrs9-gen-0004": "Finansal varlık ancak nakit ödemesi fiilen yapıldığında muhasebeleştirilir",
    "std-tfrs9-gen-0005": "Her sınıfta işlem maliyetleri gider yazılır; hiçbir hâlde maliyete eklenmez",
    "std-tfrs9-gen-0006": "İşlem maliyetleri finansal varlığın maliyetine eklenir ve sonradan itfa edilir",
    "std-tfrs9-gen-0007": "Yalnızca yönetimin varlığı elde tutma süresi ile kalan vade dikkate alınır",
    "std-tfrs9-gen-0008": "İtfa edilmiş maliyet ve gerçeğe uygun değer olmak üzere yalnızca iki ölçüm sınıfı vardır",
    "std-tfrs9-gen-0009": "İş modeline bakılmaksızın tüm borçlanma araçları itfa edilmiş maliyetle ölçülür",
    "std-tfrs9-gen-0010": "Yalnızca ticari amaçla elde tutulan varlıklar için uygulanır",
    "std-tfrs9-gen-0011": "Yalnızca özkaynağa dayalı finansal araçlar bu sınıfa girer",
    "std-tfrs9-gen-0014": "Nakit akışlarının sabit bir getiri sağlaması yeterlidir; anapara ve faiz olması aranmaz",
    "std-tfrs9-gen-0015": "Faiz geliri, etkin faiz oranı net defter değerine uygulanarak hesaplanır",
    "std-tfrs9-gen-0016": "Sözleşmedeki nominal faiz oranıdır; tahmini nakit akışları dikkate alınmaz",
    "std-tfrs9-gen-0017": "Değer değişimi doğrudan dönemin kâr veya zararında muhasebeleştirilir",
    "std-tfrs9-gen-0018": "Diğer kapsamlı gelirde biriken tutar özkaynakta kalır; kâr veya zarara aktarılmaz",
    "std-tfrs9-gen-0019": "Kural olarak itfa edilmiş maliyetle ölçülür",
    "std-tfrs9-gen-0020": "Her raporlama döneminde serbestçe geri alınabilen bir tercihtir",
    "std-tfrs9-gen-0021": "Diğer kapsamlı gelirde biriken tutar satışta kâr veya zarara yeniden sınıflandırılır",
    "std-tfrs9-gen-0022": "Kâr payları özkaynakta biriktirilir ve varlık satıldığında kâr veya zarara aktarılır",
    "std-tfrs9-gen-0023": "Tüm finansal borçlar gerçeğe uygun değer farkı kâr veya zarara yansıtılarak ölçülür",
    "std-tfrs9-gen-0024": "Kendi kredi riskindeki değişimden kaynaklanan kısım doğrudan kâr veya zarara yansıtılır",
    "std-tfrs9-gen-0030": "Gerçekleşmiş kredi zararı modelidir; karşılık ancak zarar fiilen doğduğunda ayrılır",
    "std-tfrs9-gen-0031": "En kötü senaryoda ortaya çıkabilecek azami kredi zararı tutarıdır",
    "std-tfrs9-gen-0032": "Yalnızca geçmiş temerrüt verilerinin basit ortalaması alınır; paranın zaman değeri göz ardı edilir",
    "std-tfrs9-gen-0033": "Aşamalar yalnızca varlık fiilen temerrüde düştükten sonra uygulanmaya başlar",
    "std-tfrs9-gen-0034": "Raporlama tarihinden sonraki 12 ay içinde ödenmesi beklenen faiz tutarıdır",
    "std-tfrs9-gen-0035": "Yalnızca varlık fiilen temerrüde düştüğünde kredi riskinde önemli artış kabul edilir",
    "std-tfrs9-gen-0036": "Ticari alacaklara genel üç aşamalı model uygulanır; basitleştirilmiş yaklaşım kullanılamaz",
    "std-tfrs9-gen-0037": "GUDFK ile ölçülen finansal varlıklar da dâhil tüm varlıklara uygulanır",
    "std-tfrs9-gen-0038": "Zarar karşılığı diğer kapsamlı gelire yansıtılır ve varlığın defter değeri azaltılır",
    "std-tfrs9-gen-0041": "Etkin faiz oranı brüt defter değerine uygulanmaya devam eder",
    "std-tfrs9-gen-0042": "Yalnızca vadesi geçmiş ticari alacaklar için zarar karşılığı ayrılır",
    "std-tfrs9-gen-0045": "Yalnızca varlık fiziksel olarak devredildiğinde bilanço dışı bırakılır",
    "std-tfrs9-gen-0046": "Risk ve getiriler elde tutulsa dahi sözleşme devredilmişse bilanço dışı bırakılır",
    "std-tfrs9-gen-0047": "Borcun defter değeri önemli ölçüde değiştiğinde bilanço dışı bırakılır",
    "std-tfrs9-gen-0048": "Yönetim gerekli gördüğünde her dönem serbestçe yeniden sınıflandırılabilir",
    "std-tfrs9-gen-0049": "İş modeli değiştiğinde finansal borçlar da yeniden sınıflandırılır",
    "std-tfrs9-gen-0050": "Koşullar sağlandığında riskten korunma muhasebesinin uygulanması zorunludur",
    "std-tfrs9-gen-0052": "Yalnızca gerçeğe uygun değer ve nakit akış riskinden korunma olmak üzere iki tür vardır",
    "std-tfrs9-gen-0058": "Alacaklar devredildiğinden her hâlde bilanço dışı bırakılır; risk ve getiri dikkate alınmaz",
    "std-tfrs9-gen-0060": "Açıklama hükümleri TFRS 9'un kendi metninde düzenlenmiştir",
}

# TFRS 9 doğru şıkları uzun (ort 82); 28 soruda doğru en uzundu. 18'inde
# çeldirici içerikle doğrunun üstüne çıkarıldı, 10'u en uzun bırakıldı (~%20).
# Hepsi dolgusuz — "dolguyu ele, en uzunu seç" stratejisini de kırar.
TFRS9_UZAT = {
    "std-tfrs9-gen-0009": {"E": "İş modeline ve nakit akışı özelliklerine bakılmaksızın tüm borçlanma araçları itfa edilmiş maliyetle ölçülür; sınıflandırmada yalnızca varlığın hukuki biçimi ve vadesi belirleyicidir"},
    "std-tfrs9-gen-0052": {"B": "Yalnızca nakit akış riskinden korunma bulunur; gerçeğe uygun değer riskinden korunma ile yurtdışı işletmedeki net yatırım riskinden korunma TFRS 9 kapsamında tanınmaz"},
    "std-tfrs9-gen-0010": {"C": "Yalnızca yönetimin bu yönde karar verdiği varlıklar bu sınıfta ölçülür; iş modeli ve sözleşmeye bağlı nakit akışı özellikleri sınıflandırmada hiç rol oynamaz"},
    "std-tfrs9-gen-0034": {"A": "Yalnızca gelecek 12 ayda tahsil edilemeyecek anaparanın tamamını ifade eder; temerrüt olasılığı ve paranın zaman değeri bu tutarın belirlenmesinde dikkate alınmaz"},
    "std-tfrs9-gen-0045": {"C": "Yalnızca vergi idaresi izin verdiğinde bilanço dışı bırakılabilir; sözleşmeye bağlı hakların sona ermesi ya da varlığın devredilmesi tek başına yeterli sayılmaz"},
    "std-tfrs9-gen-0033": {"A": "Tüm finansal varlıklar için her hâlde ömür boyu beklenen kredi zararı ayrılır; kredi riskinde önemli artış olup olmadığına dair aşamalı bir değerlendirme yapılmaz"},
    "std-tfrs9-gen-0019": {"D": "Her hâlde maliyet bedeliyle ölçülür; gerçeğe uygun değer hiç kullanılmaz ve piyasa fiyatındaki değişimler finansal tablolara hiçbir biçimde yansıtılmaz"},
    "std-tfrs9-gen-0014": {"D": "Nakit akışı özellikleri hiçbir hâlde dikkate alınmaz; sınıflandırmada yalnızca iş modeli esas alınır ve anapara ile faiz ölçütü hiç uygulanmaz"},
    "std-tfrs9-gen-0017": {"D": "Hiçbir değer değişimi kayda alınmaz; değişimler yalnızca dipnotlarda açıklanır ve finansal durum tablosuna hiçbir biçimde yansıtılmaz"},
    "std-tfrs9-gen-0021": {"E": "Diğer kapsamlı gelirde biriken tutar satışta kâr veya zarara yeniden sınıflandırılır ve gerçekleşen kazanç dönemin sonucuna dâhil edilir"},
    "std-tfrs9-gen-0024": {"E": "Kendi kredi riskindeki değişimden kaynaklanan kısım doğrudan kâr veya zarara yansıtılır; diğer kapsamlı gelirde gösterim hiçbir hâlde söz konusu olmaz"},
    "std-tfrs9-gen-0036": {"E": "Ticari alacaklara genel üç aşamalı model uygulanır; basitleştirilmiş yaklaşım kullanılmaz ve her alacak için kredi riski aşaması ayrı ayrı izlenir"},
    "std-tfrs9-gen-0001": {"B": "Yalnızca borsada işlem gören hisse senetlerini kapsayan dar bir kavramdır; sözleşmeye dayalı alacak ve borçlar finansal araç tanımının dışında kalır"},
    "std-tfrs9-gen-0047": {"D": "Borç, işletmenin dilediği zaman bilanço dışı bırakabileceği bir kalemdir; yükümlülüğün ortadan kalkması ya da ifa edilmesi koşulu hiç aranmaz"},
    "std-tfrs9-gen-0032": {"E": "Yalnızca geçmiş temerrüt verilerinin basit ortalaması alınır; paranın zaman değeri ve geleceğe yönelik makroekonomik tahminler ölçüme hiç dâhil edilmez"},
    "std-tfrs9-gen-0037": {"D": "Hiçbir finansal varlığa uygulanmayan, yalnızca biçimsel nitelikte kalan ve uygulamada karşılığı bulunmayan hükümlerdir; ölçüm sınıflarıyla ilişkisi yoktur"},
    "std-tfrs9-gen-0046": {"D": "Devredilen varlıklar hiçbir hâlde bilanço dışı bırakılamaz; risk ve getiriler devredilmiş olsa dahi varlık süresiz olarak kayıtlarda kalır"},
    "std-tfrs9-gen-0053": {"C": "Yalnızca finansal borçların ölçümünü değiştirir; finansal varlıkların sınıflandırma ve ölçüm esaslarına hiçbir biçimde dokunmamıştır"},
}

KONFIG: dict[str, dict] = {
    "tms_12_gelir_vergileri": {"atma": TMS12_ATMA, "atma_ozel": TMS12_OZEL,
                               "uzat": TMS12_UZAT},
    "tms_21_kur_degisimi": {"atma_ozel": TMS21_OZEL, "uzat": TMS21_UZAT},
    "tfrs_9_finansal_arac": {"atma_ozel": TFRS9_OZEL, "uzat": TFRS9_UZAT},
}


def dokum(path: str) -> None:
    """Kırpma SONRASI durumu ölç — dosyaya özel listeler bu döküme göre yazılır."""
    sonuc = temizle(path, yaz=False)
    qs = sonuc["qs"]
    print(rapor(qs))
    print(f"kırpılan {sonuc['kirpilan']} · kalan dolgu {sonuc['kalan_dolgu']} "
          f"· kalan atma-şıkkı {sonuc['kalan_atma']}\n")
    for q in qs:
        if len(ONCUL.findall(q["stem"])) >= 2:
            continue
        o = q["options"]
        d = len(o[q["answer"]])
        L = [len(v) for v in o.values()]
        if d == min(L):
            en_kisa = min(((h, v) for h, v in o.items() if h != q["answer"]),
                          key=lambda t: len(t[1]))
            print(f"{q['id']}  doğru {q['answer']}({d}) EN KISA → hedef <{d}")
            print(f"    kök: {q['stem'][:88]}")
            print(f"    doğru: {o[q['answer']]}")
            print(f"    en kısa çeldirici {en_kisa[0]}({len(en_kisa[1])}): {en_kisa[1]}")
        elif d == max(L):
            print(f"{q['id']}  doğru {q['answer']}({d}) EN UZUN → hedef >{d + 15}")
            print(f"    kök: {q['stem'][:88]}")
            print(f"    doğru: {o[q['answer']]}")


def calistir(anahtar: str) -> None:
    path = f"{KOK}/{anahtar}.json"
    cfg = KONFIG.get(anahtar, {})
    onceki = {q["id"]: q for q in json.load(open(path, encoding="utf-8"))}
    sonuc = temizle(path, atma_yerine=cfg.get("atma"), atma_ozel=cfg.get("atma_ozel"),
                    uzat=cfg.get("uzat"), kisalt=cfg.get("kisalt"))
    qs = sonuc["qs"]

    # 0/0/0/0 — kök · çözüm · doğru şık metni · harf hiç değişmemeli
    kok = coz = dgr = hrf = 0
    for q in qs:
        o = onceki[q["id"]]
        kok += q["stem"] != o["stem"]
        coz += q.get("solution") != o.get("solution")
        hrf += q["answer"] != o["answer"]
        dgr += q["options"][q["answer"]] != o["options"][o["answer"]]
    assert (kok, coz, dgr, hrf) == (0, 0, 0, 0), \
        f"DOKUNULMAZ ALAN DEĞİŞTİ — kök/çözüm/doğru/harf: {kok}/{coz}/{dgr}/{hrf}"

    print(f"{anahtar}: kırpılan {sonuc['kirpilan']} · atma {sonuc['atma']} "
          f"· kalan dolgu {sonuc['kalan_dolgu']} · kalan atma {sonuc['kalan_atma']}")
    print(f"  {rapor(qs)}")
    print(f"  kök/çözüm/doğru şık/harf: {kok}/{coz}/{dgr}/{hrf}")


if __name__ == "__main__":
    ad = sys.argv[1]
    if "--rapor" in sys.argv:
        dokum(f"{KOK}/{ad}.json")
    else:
        calistir(ad)
