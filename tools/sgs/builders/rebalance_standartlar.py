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

# ── TMS 37 · Karşılıklar, Koşullu Borç ve Koşullu Varlıklar ────────────────────
# 40 atma sorusu. Doğru şık ort 72 karakter → yanılgıları KASTEN ~100 yazıyorum:
# hem atma-şıkkını değiştirir hem de çoğu doğrudan uzun olduğundan boy dengesini
# kendiliğinden kurar (doğru şıkkı zaten >100 olan ~7 soru en uzun kalır ≈ %20).
# Bu, tfrs_9'da ayrı ayrı 18 uzat yazma zahmetini ortadan kaldırır. Filler yok.
TMS37_OZEL = {
    "std-tms37-gen-0001": "İşletmenin gelecekte katlanmayı planladığı, tutarı ve zamanı önceden kesin olarak bilinen olağan giderler için ayrılan bir fondur",
    "std-tms37-gen-0002": "Karşılık ile ticari borç arasında fark yoktur; ikisinde de tutar ve ödeme zamanı kesin olarak bilinir ve aynı biçimde ölçülür",
    "std-tms37-gen-0003": "Yalnızca gelecekte kaynak çıkışı olması yeterlidir; geçmiş olaydan doğan mevcut yükümlülük ve güvenilir tahmin koşulları aranmaz",
    "std-tms37-gen-0004": "Kaynak çıkışı olasılığının en az yüzde doksan düzeyinde ve neredeyse kesin sayılabilecek ölçüde yüksek olması aranır",
    "std-tms37-gen-0005": "Yalnızca sözleşme veya yasadan doğan hukuki yükümlülükleri kapsar; geçmiş uygulamalardan doğan zımni yükümlülükleri kapsamaz",
    "std-tms37-gen-0006": "Zımni yükümlülük ancak yazılı sözleşme veya yasal düzenlemeyle desteklendiğinde muhasebeleştirilir; uygulama ve açıklamalar yeterli değildir",
    "std-tms37-gen-0007": "Yükümlülük doğuran olay işletmenin gelecekteki kararlarına bağlıdır; işletme faaliyetini değiştirerek yükümlülükten her zaman kaçınabilir",
    "std-tms37-gen-0008": "İşletmenin gelecekteki faaliyetlerinden doğacak tüm maliyetler için önceden karşılık ayrılır ve ilgili dönemlere yayılır",
    "std-tms37-gen-0009": "Gelecekteki faaliyet zararları için beklenen tutar üzerinden karşılık ayrılır ve dönem sonucuna gider olarak yansıtılır",
    "std-tms37-gen-0010": "Ekonomik açıdan dezavantajlı sözleşmeler için karşılık ayrılmaz; sözleşme tamamlanana kadar herhangi bir yükümlülük muhasebeleştirilmez",
    "std-tms37-gen-0011": "Yönetimin yeniden yapılandırma niyetini içeren kararı tek başına yeterlidir; ayrıntılı plan ve geçerli beklenti yaratılması aranmaz",
    "std-tms37-gen-0012": "Yeniden yapılandırmayla ilgili olsun olmasın işletmenin süregelen tüm faaliyet maliyetleri ve personel eğitim giderleri karşılığa dâhil edilir",
    "std-tms37-gen-0016": "Yönetim kurulunun kapatma kararı almasıyla zımni yükümlülük doğar; etkilenenlere duyuru yapılmasa dahi karşılık ayrılır",
    "std-tms37-gen-0017": "Koşullu borç, gerçekleşme zamanı ve tutarı kesin bilinen ve finansal tablolara borç olarak kaydedilen mevcut bir yükümlülüktür",
    "std-tms37-gen-0018": "Koşullu borçlar tutarları tahmin edilerek finansal tablolara borç olarak yansıtılır; ayrıca dipnotta açıklama yapılmaz",
    "std-tms37-gen-0019": "Kaynak çıkışı ihtimali uzak olsa dahi tüm koşullu borçlar için ayrıntılı açıklama yapılması her hâlde zorunlu tutulur",
    "std-tms37-gen-0020": "Koşullu varlık, gerçekleşmesi kesin olan ve işletmenin kontrolündeki olaylardan doğan, finansal tablolara kaydedilen bir varlıktır",
    "std-tms37-gen-0021": "Koşullu varlıklar gelir girişi muhtemel olduğunda finansal tablolara varlık olarak kaydedilir ve gelir yazılır",
    "std-tms37-gen-0022": "Gelirin kesinleşmesi hâlinde dahi varlık koşullu olarak kalmaya devam eder ve yalnızca dipnotta açıklanır",
    "std-tms37-gen-0023": "Karşılık ile koşullu borç arasında fark yoktur; ikisinde de mevcut yükümlülük kesindir ve finansal tablolara aynı biçimde yansıtılır",
    "std-tms37-gen-0024": "Mevcut yükümlülük olsa dahi tutarın güvenilir tahmini yapılamıyorsa hiçbir açıklama yapılmaz ve yükümlülük tümüyle göz ardı edilir",
    "std-tms37-gen-0025": "Müşterek ve müteselsil sorumlulukta işletme, diğer taraflarca karşılanacak kısım dâhil yükümlülüğün tamamı için karşılık ayırır",
    "std-tms37-gen-0026": "Koşullu borçlar ilk değerlendirmeden sonra bir daha gözden geçirilmez; başlangıçtaki sınıflandırma dönemler boyunca sabit kalır",
    "std-tms37-gen-0031": "Karşılık, yükümlülüğün yerine getirilmesi için gereken azami tutar üzerinden ölçülür; belirsizlik hâlinde en yüksek olası değer alınır",
    "std-tms37-gen-0032": "En gerçekçi tahmin, geçmiş dönemlerde fiilen katlanılan benzer harcamaların basit aritmetik ortalaması alınarak belirlenir",
    "std-tms37-gen-0033": "Çok sayıda benzer kalemden oluşan karşılıkta yalnızca en yüksek tutarlı tek sonuç esas alınır; olasılıklar dikkate alınmaz",
    "std-tms37-gen-0034": "Tek bir yükümlülüğün ölçümünde tüm olası sonuçların basit aritmetik ortalaması alınır; en muhtemel sonuç dikkate alınmaz",
    "std-tms37-gen-0035": "Belirsizlik ne kadar büyükse o kadar yüksek karşılık ayrılması gerekir; aşırı ihtiyatlılık bu durumda her hâlde haklı görülür",
    "std-tms37-gen-0036": "Paranın zaman değeri ne kadar önemli olursa olsun karşılıklar bugünkü değerine indirgenmez; her zaman nominal tutarla ölçülür",
    "std-tms37-gen-0037": "Gelecekteki olaylar hiçbir koşulda karşılığın ölçümünde dikkate alınmaz; yalnızca raporlama tarihindeki mevcut koşullar esas alınır",
    "std-tms37-gen-0038": "Varlıkların elden çıkarılmasından beklenen kazançlar karşılığın ölçümünden düşülür ve karşılık tutarını azaltır",
    "std-tms37-gen-0039": "Üçüncü taraftan beklenen tazmin, elde edilmesi kesin olmasa dahi karşılıktan doğrudan düşülerek net tutar muhasebeleştirilir",
    "std-tms37-gen-0040": "Karşılığa ilişkin gider ile tazminat tutarı hiçbir hâlde netleştirilemez; ikisi de her zaman brüt olarak ayrı ayrı sunulur",
    "std-tms37-gen-0041": "Karşılıklar bir kez ölçüldükten sonra gözden geçirilmez; başlangıçta belirlenen tutar yükümlülük sona erene kadar korunur",
    "std-tms37-gen-0042": "Ayrılan karşılık, işletmenin gerekli gördüğü başka herhangi bir gider veya yükümlülük için de serbestçe kullanılabilir",
    "std-tms37-gen-0048": "Koşullu borçlara ilişkin hiçbir açıklama yapılmaz; bu bilgiler yalnızca işletmenin iç raporlarında yer alır ve dışa aktarılmaz",
    "std-tms37-gen-0049": "Açıklamanın işletmeye zarar vereceği gerekçesiyle koşullu borç ve karşılıklara ilişkin bilgiler her durumda açıklama dışı bırakılabilir",
    "std-tms37-gen-0052": "Henüz yürürlüğe girmemiş bir yasadan doğacak yükümlülük için, yürürlük neredeyse kesin olsa dahi hiçbir zaman karşılık ayrılmaz",
    "std-tms37-gen-0057": "Karşılıklar bilançoda özkaynak kalemi olarak sunulur; karşılık gideri ise doğrudan geçmiş yıl kârlarından indirilir",
    "std-tms37-gen-0058": "Genel kurul kararından önce dahi dağıtılması beklenen kâr payı için mevcut yükümlülük doğar ve karşılık ayrılır",
}

# tfrs_16 doğru şıkları uzun (ort 83); 34 atma sonrası hâlâ %42 doğru-en-uzun
# → 8 soruda çeldirici içerikle üstüne çıkarıldı.
TFRS16_UZAT = {
    "std-tfrs16-gen-0050": {"E": "Devrin satış sayıldığı işlemde satıcı-kiracı, varlığın tümüne ilişkin kazancın tamamını hemen kâra yansıtır ve elde tuttuğu kullanım hakkıyla sınırlı kazanç ayrımını hiç yapmaz"},
    "std-tfrs16-gen-0017": {"E": "Kira ödemeleri her hâlde piyasadaki güncel gösterge faiz oranıyla iskonto edilir; kiralamadaki zımni faiz oranı kolayca belirlenebilse dahi hiçbir koşulda kullanılmaz"},
    "std-tfrs16-gen-0023": {"D": "Kira ödemeleri yalnızca sabit ödemeleri kapsar; endekse bağlı değişken ödemeler, kalıntı değer taahhütleri ve satın alma opsiyonu bedelleri hiçbir hâlde kapsama girmez"},
    "std-tfrs16-gen-0057": {"D": "Kiralamada yapılan her değişiklik, kapsam ve bedeldeki etkisine bakılmaksızın her hâlde ayrı bir yeni kiralama olarak baştan muhasebeleştirilir"},
    "std-tfrs16-gen-0053": {"C": "Bina her hâlde bilançoda tutulmaya devam edilir; devrin satış sayılıp sayılmadığına bakılmaksızın varlık hiçbir zaman bilançodan çıkarılmaz"},
    "std-tfrs16-gen-0004": {"E": "Tedarikçinin varlığı istediği zaman eşdeğeriyle ikame etme hakkı bulunsa dahi varlık tanımlanmış sayılır ve kiralama kapsamında değerlendirilir"},
    "std-tfrs16-gen-0060": {"B": "Kiracının varlık ve yükümlülükleri azalır; kiralama işlemi hem varlık hem borç tarafını küçülterek toplam bilanço büyüklüğünü düşürür"},
    "std-tfrs16-gen-0003": {"E": "Kullanımdan sağlanacak ekonomik yararların yalnızca küçük bir kısmını elde etme hakkı, varlığın kullanımını kontrol etmek için yeterli sayılır"},
}

# ── TFRS 16 · Kiralamalar ─────────────────────────────────────────────────────
TFRS16_OZEL = {
    "std-tfrs16-gen-0001": "Bir varlığın mülkiyetinin belirli bir bedel karşılığında kalıcı olarak devredilmesini sağlayan sözleşmedir",
    "std-tfrs16-gen-0002": "Bir sözleşmenin kiralama sayılması için tedarikçinin varlığı işletme adına işletmesi ve bakımını üstlenmesi yeterlidir",
    "std-tfrs16-gen-0003": "Kullanımdan sağlanacak ekonomik yararların yalnızca küçük bir kısmını elde etme hakkı kontrol için yeterlidir",
    "std-tfrs16-gen-0004": "Tedarikçinin varlığı istediği zaman eşdeğeriyle ikame etme hakkı bulunsa dahi varlık tanımlanmış sayılır",
    "std-tfrs16-gen-0005": "Kiracı, kiralamalarını finansal kiralama ve faaliyet kiralaması olarak ikiye ayırır ve farklı biçimde muhasebeleştirir",
    "std-tfrs16-gen-0006": "Kiraya veren de kiracı gibi tüm kiralamalar için tek bir model uygular; finansal-faaliyet ayrımı yapmaz",
    "std-tfrs16-gen-0007": "Kiracı yalnızca uzun vadeli ve yüksek değerli kiralamalar için muafiyet uygulayabilir",
    "std-tfrs16-gen-0008": "Kısa vadeli kiralama, başlangıçta süresi yirmi dört ay veya daha kısa olan ve satın alma opsiyonu içeren kiralamadır",
    "std-tfrs16-gen-0010": "Düşük değerli varlık muafiyeti yalnızca işletme genelinde tüm kiralamalara bir bütün olarak birlikte uygulanabilir",
    "std-tfrs16-gen-0011": "Kısa vadeli kiralama muafiyeti kiralama bazında tek tek yapılan bir tercihtir",
    "std-tfrs16-gen-0016": "Başlangıç tarihinde ödenecek kira ödemelerinin toplam nominal tutarıyla ölçülür; iskonto yapılmaz",
    "std-tfrs16-gen-0017": "Kira ödemeleri her hâlde piyasadaki güncel gösterge faiz oranıyla iskonto edilir; zımni faiz oranı kullanılmaz",
    "std-tfrs16-gen-0018": "Kullanım hakkı varlığı başlangıçta gerçeğe uygun değeriyle ölçülür",
    "std-tfrs16-gen-0019": "Kullanım hakkı varlığının maliyeti yalnızca ilk kira ödemesinden oluşur; doğrudan maliyet ve restorasyon tutarları hariçtir",
    "std-tfrs16-gen-0022": "Başlangıçtaki doğrudan maliyetler oluştukları dönemde doğrudan gider yazılır; kullanım hakkı varlığına eklenmez",
    "std-tfrs16-gen-0023": "Kira ödemeleri yalnızca sabit ödemeleri kapsar; endekse bağlı ödemeler ve kalıntı değer taahhütleri kapsam dışıdır",
    "std-tfrs16-gen-0024": "Endekse bağlı olmayan değişken kira ödemeleri de kira yükümlülüğünün ilk ölçümüne dâhil edilir",
    "std-tfrs16-gen-0025": "Kiralama süresi yalnızca iptal edilemeyen dönemdir; uzatma ve sonlandırma opsiyonları hiçbir hâlde dikkate alınmaz",
    "std-tfrs16-gen-0026": "Kiralama ve kiralama dışı bileşenler hiçbir hâlde ayrıştırılmaz; sözleşme bedeli tümüyle kiralama olarak muhasebeleştirilir",
    "std-tfrs16-gen-0030": "Kullanım hakkı varlığı her hâlde gerçeğe uygun değer modeliyle ölçülür; maliyet modeli kullanılamaz",
    "std-tfrs16-gen-0031": "Kullanım hakkı varlığı her hâlde dayanak varlığın faydalı ömrü boyunca amortismana tabi tutulur",
    "std-tfrs16-gen-0033": "Kira yükümlülüğünün defter değeri her dönem sabit kalır; faiz ve ödemeler defter değerini değiştirmez",
    "std-tfrs16-gen-0036": "Kiracının toplam kiralama gideri, kiralama süresi boyunca her yıl eşit tutarda dağıtılır",
    "std-tfrs16-gen-0037": "Kira yükümlülüğü ilk ölçümden sonra hiçbir koşulda yeniden ölçülmez; süre veya ödeme değişse dahi sabit kalır",
    "std-tfrs16-gen-0039": "Kullanım hakkı varlığı her hâlde finansal borç olarak sınıflandırılıp finansal durum tablosunda sunulur",
    "std-tfrs16-gen-0040": "Kira yükümlülüğünün anapara kısmı işletme faaliyetlerinden nakit akışı olarak sunulur",
    "std-tfrs16-gen-0041": "Kullanım hakkı varlığı ile kira yükümlülüğünün defter değerleri kiralama süresi boyunca her zaman birbirine eşit kalır",
    "std-tfrs16-gen-0044": "Kiraya veren, mülkiyet risk ve getirilerini elinde tutsa dahi kiralamayı her hâlde finansal kiralama olarak sınıflandırır",
    "std-tfrs16-gen-0048": "Kiraya veren, faaliyet kiralamasındaki dayanak varlık için hiçbir hâlde amortisman ayırmaz",
    "std-tfrs16-gen-0049": "Satış ve geri kiralamada devrin satış olup olmadığı yalnızca sözleşmenin adına bakılarak belirlenir",
    "std-tfrs16-gen-0050": "Devrin satış sayıldığı işlemde satıcı-kiracı, varlığın tümüne ilişkin kazancın tamamını hemen kâra yansıtır",
    "std-tfrs16-gen-0051": "Devrin satış sayılmadığı işlemde satıcı-kiracı varlığı bilançodan çıkarır ve devir bedelini gelir yazar",
    "std-tfrs16-gen-0052": "Kiraya verenin faaliyet kiralamasındaki başlangıç doğrudan maliyetleri oluştukları dönemde doğrudan gider yazılır",
    "std-tfrs16-gen-0057": "Kiralamada yapılan her değişiklik, her hâlde ayrı bir yeni kiralama olarak muhasebeleştirilir",
}

# ── Kavramsal Çerçeve ─────────────────────────────────────────────────────────
KAVRAM_OZEL = {
    "std-cerceve-gen-0021": "İşletmenin sürekliliği varsayımı yalnızca büyük ölçekli işletmeler için geçerlidir; küçük işletmelerde bu varsayım aranmaz",
}
KAVRAM_UZAT = {
    "std-cerceve-gen-0001": {"A": "Her işlem için ayrıntılı muhasebe kuralları koyar ve işletmelerin uygulayacağı tek tip kayıt yöntemlerini belirler; genel amaçlı raporlamanın kavramsal temellerini oluşturmak Çerçeve'nin amacı değildir"},
    "std-cerceve-gen-0005": {"A": "Yalnızca işletme yönetiminin iç kararlarına hizmet eden bilgiler sağlar; dış kullanıcıların yatırım ve kredi kararları genel amaçlı finansal raporlamanın kapsamı dışındadır"},
    "std-cerceve-gen-0055": {"B": "Tüm gelir ve giderler her hâlde diğer kapsamlı gelirde raporlanır; kâr veya zarar tablosu yalnızca özet bir bölüm olarak sunulur ve asıl performans dışa aktarılmaz"},
    "std-cerceve-gen-0045": {"A": "Varlığın edinilmesi sırasında ödenen bedel her hâlde ölçüm esası olarak kullanılır; sonraki dönemlerde güncel değer ölçüleri hiçbir koşulda uygulanmaz"},
    "std-cerceve-gen-0015": {"B": "İhtiyatlılık, varlık ve gelirlerin sistematik olarak olduğundan yüksek, borç ve giderlerin düşük gösterilmesini gerektirir; bu, tarafsızlığın bir gereği sayılır"},
    "std-cerceve-gen-0025": {"B": "Finansal tablolar yalnızca gelecek tahminlerinden oluşur; geçmiş işlemlere ve mevcut duruma ilişkin bilgiler raporlama kapsamının tümüyle dışında bırakılır"},
    "std-cerceve-gen-0046": {"A": "Piyasa katılımcıları arasındaki olağan işlemde oluşan fiyat dışlanır; gerçeğe uygun değer yerine her zaman işletmenin kendi belirlediği iç değer esas alınır"},
    "std-cerceve-gen-0050": {"A": "Gerçeğe uygun değer işletmeye özgü varsayımları esas alır; piyasa katılımcılarının bakış açısı ve piyasa koşulları ölçümde hiçbir biçimde dikkate alınmaz"},
    "std-cerceve-gen-0038": {"A": "Bir varlık, kontrol devam etse dahi işletmenin ihtiyaç duymadığına karar vermesiyle finansal tablo dışı bırakılır; kontrolün sona ermesi koşulu aranmaz"},
    "std-cerceve-gen-0004": {"A": "İşletme böyle bir konuda hiçbir kayıt yapmaz ve işlemi tümüyle göz ardı eder; işlemin özü ve ekonomik gerçekliği muhasebeleştirmede dikkate alınmaz"},
    "std-cerceve-gen-0016": {"E": "Karşılaştırılabilirlik, bilginin yalnızca aynı işletmenin tek bir dönemine ilişkin olmasını gerektirir; dönemler ve işletmeler arası karşılaştırma amaçlanmaz"},
    "std-cerceve-gen-0048": {"D": "Ölçüm esası yalnızca vergi idaresince belirlenir; işletmenin tarihi maliyet veya güncel değer arasında bir seçim yapması söz konusu değildir"},
    "std-cerceve-gen-0022": {"E": "Raporlayan işletme yalnızca borsada işlem gören şirketlerdir; borsa dışı işletmeler ve konsolide gruplar raporlayan işletme tanımının kapsamına girmez"},
    "std-cerceve-gen-0037": {"B": "Unsur tanımını karşılayan her kalem, başka hiçbir koşul aranmaksızın doğrudan muhasebeleştirilir; ölçülebilme ve olasılık gibi ölçütler dikkate alınmaz"},
    "std-cerceve-gen-0012": {"E": "Önemlilik, işletmenin kâr etme olasılığını ölçen sabit bir eşiktir; bilginin kullanıcı kararlarını etkileyip etkilemediğiyle bir ilgisi bulunmaz"},
    "std-cerceve-gen-0017": {"B": "Bilginin hiçbir dış kaynakla karşılaştırılamaması doğrulanabilirliği artırır; farklı gözlemcilerin aynı sonuca ulaşması gerçeğe uygunluğun ölçütü değildir"},
}

# ── TMS 7 · Nakit Akış Tablosu ────────────────────────────────────────────────
TMS7_OZEL = {
    "std-tms7-gen-0003": "Nakit yalnızca kasadaki fiziki parayı ifade eder; vadesiz mevduat ve nakit benzerleri bu kapsama girmez",
    "std-tms7-gen-0005": "Özkaynağa dayalı finansal araçlar her hâlde nakit benzeri sayılır ve nakit akış tablosuna dâhil edilir",
    "std-tms7-gen-0009": "İşletme faaliyetleri, işletmenin yalnızca duran varlık alım ve satımından doğan nakit akışlarını kapsar",
    "std-tms7-gen-0011": "Finansman faaliyetleri, işletmenin esas gelir getirici mal ve hizmet satışlarından doğan nakit akışlarıdır",
    "std-tms7-gen-0019": "Faiz ve kâr payı akışları her hâlde işletme faaliyeti olarak sınıflandırılır; başka bir sınıfa alınamaz",
    "std-tms7-gen-0022": "Nakit gerektirmeyen yatırım ve finansman işlemleri de nakit akış tablosunun ilgili bölümlerinde gösterilir",
    "std-tms7-gen-0029": "İşletme faaliyetlerinden nakit akışları yalnızca dolaylı yöntemle sunulabilir; doğrudan yönteme izin verilmez",
    "std-tms7-gen-0030": "Doğrudan yöntemde dönem kârı, gayrinakdi kalemler için düzeltilerek nakit akışına ulaşılır",
    "std-tms7-gen-0041": "Nakit akışları kural olarak netleştirilerek tek bir tutar hâlinde raporlanır; brüt gösterim istisnadır",
    "std-tms7-gen-0048": "Nakit akış tablosundaki tutarlar ile finansal durum tablosundaki nakit kalemlerinin uzlaştırılması gerekmez",
    "std-tms7-gen-0049": "Grup tarafından kullanılamayan nakit de serbestçe kullanılabilir nakit gibi tabloya dâhil edilir ve ayrıca açıklanmaz",
}
TMS7_UZAT = {  # doğru şıklar çok uzun (ort 83); 20 en-uzundan 11'i dengelendi
    "std-tms7-gen-0005": {"E": "Özkaynağa dayalı finansal araçlar her hâlde nakit benzeri sayılır ve edinim tarihindeki vadesine bakılmaksızın nakit ve nakit benzerleri kapsamına dâhil edilir"},
    "std-tms7-gen-0052": {"B": "İşletme faaliyetlerinden nakit akışı, işletmenin performansını yansıtan tek göstergedir; yatırım ve finansman akışları bu değerlendirmede hiçbir biçimde dikkate alınmaz"},
    "std-tms7-gen-0006": {"C": "Banka kredileri nakit akış tablosunda hiçbir biçimde yer almaz; yalnızca finansal durum tablosunda gösterilir ve nakit hareketleri tabloya hiç yansıtılmaz"},
    "std-tms7-gen-0010": {"C": "İşletmenin yalnızca stok alım ve satımını kapsayan dar bir bölümdür; hizmet üretimi ve esas faaliyetten doğan gelirler işletme faaliyeti olarak sayılmaz"},
    "std-tms7-gen-0020": {"B": "Gelir vergisi ödemeleri her hâlde ve istisnasız finansman faaliyeti olarak sınıflandırılır; işletme faaliyetiyle ilişkilendirilmeleri hiçbir koşulda mümkün değildir"},
    "std-tms7-gen-0025": {"B": "Kur farkı yatırım faaliyeti olarak sınıflandırılır; gerçekleşmemiş kur farkları da nakit hareketi sayılarak ayrı bir kalemde nakit akış olarak raporlanır"},
    "std-tms7-gen-0051": {"B": "Nakit akış tablosu düzenlenmesi tümüyle isteğe bağlıdır; işletme bu tabloyu hazırlamak yerine yalnızca dipnotlarda özet bilgi vermeyi tercih edebilir"},
    "std-tms7-gen-0047": {"A": "Finansal kuruluşlarda faiz akışları her hâlde finansman faaliyeti olarak sınıflandırılır; bu kuruluşların esas faaliyetiyle ilişkilendirilmeleri kabul edilmez"},
    "std-tms7-gen-0031": {"D": "Yalnızca finansman faaliyetlerinde kullanılabilen nakit tutarlarını ifade eder; işletme ve yatırım faaliyetleri bu tanımın tümüyle dışında kalır"},
    "std-tms7-gen-0050": {"A": "Nakit akış tablosu diğer tablolardan tümüyle bağımsızdır; finansal durum tablosu ve gelir tablosuyla herhangi bir uzlaştırma ya da bağ kurulması gerekmez"},
    "std-tms7-gen-0019": {"E": "Faiz ve kâr payı akışları her hâlde işletme faaliyeti olarak sınıflandırılır; yatırım veya finansman faaliyeti olarak gösterilmelerine hiçbir koşulda izin verilmez"},
}

# ── TMS 23 · Borçlanma Maliyetleri ────────────────────────────────────────────
TMS23_OZEL = {
    "std-tms23-gen-0001": "İşletmenin tüm faaliyetlerinden doğan genel yönetim ve finansman giderlerinin tamamını kapsayan geniş bir kavramdır",
    "std-tms23-gen-0003": "Kısa sürede kullanıma veya satışa hazır hâle gelen, herhangi bir hazırlık süreci gerektirmeyen varlıklardır",
    "std-tms23-gen-0006": "Finansal varlıklar ve gerçeğe uygun değerle ölçülen biyolojik varlıklar özellikli varlık sayılır; maliyetleri aktifleştirilir",
    "std-tms23-gen-0007": "Borçlanma maliyetleri yalnızca banka kredilerinin nominal faizini kapsar; kira faizi ve etkin faiz düzeltmeleri kapsam dışıdır",
    "std-tms23-gen-0008": "Yabancı para borçlanmalarından doğan kur farkları hiçbir hâlde borçlanma maliyeti sayılmaz ve aktifleştirilmez",
    "std-tms23-gen-0009": "Doğrudan ilişkilendirilebilen borçlanma maliyeti, işletmenin toplam borçlanma maliyetinin varlık sayısına bölünmesiyle bulunur",
    "std-tms23-gen-0012": "Elde edildiği anda kullanıma hazır olan makine de özellikli varlık sayılır; borçlanma maliyetleri maliyetine eklenir",
    "std-tms23-gen-0013": "Özellikli varlıkla ilişkili borçlanma maliyetleri her hâlde oluştukları dönemde doğrudan gider olarak yazılır",
    "std-tms23-gen-0014": "Diğer borçlanma maliyetleri de özellikli varlığın maliyetine eklenerek aktifleştirilir; gider yazılmaz",
    "std-tms23-gen-0015": "Yüksek enflasyonlu ekonomilerde borçlanma maliyetlerinin tamamı her hâlde aktifleştirilir; hiçbir kısmı gider yazılmaz",
    "std-tms23-gen-0017": "Özel borçlanmada, fonların geçici yatırımından elde edilen gelir aktifleştirilecek tutara eklenir",
    "std-tms23-gen-0018": "Genel borçlanmalarda harcamalara aktifleştirme oranı uygulanmaz; tüm genel borçlanma maliyeti doğrudan aktifleştirilir",
    "std-tms23-gen-0019": "Aktifleştirme oranı, işletmenin özel borçlanmalarına ilişkin faiz oranlarının basit ortalamasıdır",
    "std-tms23-gen-0020": "Özellikli varlık için yapılan özel borçlanmalar da aktifleştirme oranı hesabına dâhil edilir",
    "std-tms23-gen-0021": "Aktifleştirilen tutarın üst sınırı yoktur; oluşan borçlanma maliyetini aşan tutarlar da aktifleştirilebilir",
    "std-tms23-gen-0026": "Özellikli varlığa ilişkin harcamalar yalnızca nakit ödemeleri kapsar; varlık transferi ve faizli borçlar harcama sayılmaz",
    "std-tms23-gen-0027": "Aktifleştirme oranı, dönem başındaki toplam harcama tutarına uygulanır; ağırlıklı ortalama dikkate alınmaz",
    "std-tms23-gen-0028": "Özel kredinin geçici yatırımından elde edilen faiz geliri, aktifleştirilecek borçlanma maliyetine eklenir",
    "std-tms23-gen-0030": "Aktifleştirme oranının hesaplanamadığı karmaşık durumlarda hiçbir borçlanma maliyeti aktifleştirilmez",
    "std-tms23-gen-0031": "Aktifleştirmeye başlamak için yalnızca borçlanma maliyetinin oluşması yeterlidir; harcama ve hazırlık faaliyeti aranmaz",
    "std-tms23-gen-0032": "Hazır hâle getirme faaliyetleri yalnızca fiziki inşaatı kapsar; izin alma gibi teknik ve idari çalışmalar buna girmez",
    "std-tms23-gen-0033": "İnşaat yapılmaksızın sadece elde tutulan arsanın borçlanma maliyetleri de bu dönemde aktifleştirilir",
    "std-tms23-gen-0034": "Faaliyete ara verilen uzun süreli dönemlerde de borçlanma maliyetlerinin aktifleştirilmesi kesintisiz sürdürülür",
    "std-tms23-gen-0036": "Önemli teknik ve idari çalışmaların sürdüğü dönemlerde de aktifleştirmeye her hâlde ara verilir",
    "std-tms23-gen-0037": "Aktifleştirme, varlığın fiziken tamamlandığı değil, fiilen satıldığı tarihte sona erer",
    "std-tms23-gen-0038": "Yalnızca rutin idari işlerin kaldığı varlık henüz tamamlanmamış sayılır; aktifleştirme sürdürülür",
    "std-tms23-gen-0039": "Kısımlar hâlinde tamamlanan varlıklarda aktifleştirme, ancak varlığın tamamı bittiğinde sona erer",
    "std-tms23-gen-0040": "Bütün olarak tamamlanması gereken varlıkta her kısım tamamlandıkça aktifleştirme ayrı ayrı sona erer",
    "std-tms23-gen-0041": "Bağımsız bölümleri sırayla tamamlanan iş merkezinde aktifleştirme yalnızca son bölüm bittiğinde sona erer",
    "std-tms23-gen-0044": "Köprü inşaatındaki yüksek su seviyesi kaynaklı gecikmede borçlanma maliyetlerinin aktifleştirilmesine ara verilir",
    "std-tms23-gen-0045": "Özellikli varlığın defter değeri geri kazanılabilir tutarı aşsa dahi değer düşüklüğü zararı yazılmaz",
    "std-tms23-gen-0048": "Uygulama doğrudur; özellikli varlık borçlanma maliyetlerinin doğrudan gider yazılması standarda uygundur",
    "std-tms23-gen-0049": "Aktifleştirilen borçlanma maliyeti maddi duran varlığın maliyetine girmez; ayrı bir varlık olarak izlenir",
    "std-tms23-gen-0050": "Gerçeğe uygun değerle ölçülen özellikli varlıklarda borçlanma maliyetlerinin aktifleştirilmesi her hâlde zorunlu tutulur",
    "std-tms23-gen-0051": "Tekrarlanan biçimde çok sayıda üretilen stoklar özellikli varlık sayılır; borçlanma maliyeti aktifleştirilir",
    "std-tms23-gen-0053": "Hem özel hem genel kredi kullanıldığında, tüm borçlanma maliyetine tek bir aktifleştirme oranı uygulanır",
    "std-tms23-gen-0056": "Aktifleştirme oranı, özellikli varlığa ilişkin toplam harcamanın en yüksek tutarına uygulanır",
    "std-tms23-gen-0057": "Özellikli varlık inşaatına başlanması, henüz harcama yapılmasa dahi aktifleştirmeye başlamak için yeterlidir",
    "std-tms23-gen-0059": "Harcama özel krediyi aşmasa dahi genel borçlanmadan da borçlanma maliyeti aktifleştirilir",
}

# ── TMS 40 · Yatırım Amaçlı Gayrimenkuller ────────────────────────────────────
TMS40_OZEL = {
    "std-tms40-gen-0001": "Üretimde, hizmet arzında veya idari amaçla kullanılmak üzere elde tutulan gayrimenkuldür",
    "std-tms40-gen-0002": "Yatırım amaçlı gayrimenkul ile sahibi tarafından kullanılan gayrimenkul arasında fark yoktur; ikisi de aynı biçimde muhasebeleştirilir",
    "std-tms40-gen-0003": "Yatırım amaçlı gayrimenkul, işletmenin diğer varlıklarıyla birlikte ortak nakit akışı yaratır; bağımsız nakit akışı üretmez",
    "std-tms40-gen-0005": "Gelecekteki kullanımı belirlenmemiş arsa her hâlde stok olarak sınıflandırılır; yatırım amaçlı gayrimenkul sayılmaz",
    "std-tms40-gen-0006": "Faaliyet kiralamasıyla kiraya verilen bina her hâlde TMS 16 kapsamında sahibi tarafından kullanılan gayrimenkul sayılır",
    "std-tms40-gen-0007": "Kiraya verilmek üzere elde tutulan boş bina, kiralama fiilen başlayana kadar stok olarak muhasebeleştirilir",
    "std-tms40-gen-0009": "Sahibi tarafından kullanılan gayrimenkul de yatırım amaçlı gayrimenkul kapsamında değerlendirilir",
    "std-tms40-gen-0010": "Finansal kiralamayla verilen gayrimenkul, kiraya verenin yatırım amaçlı gayrimenkulü olarak bilançosunda kalmaya devam eder",
    "std-tms40-gen-0011": "Bir gayrimenkulün kısımları farklı amaçlarla kullanılsa dahi tamamı her hâlde yatırım amaçlı gayrimenkul sayılır",
    "std-tms40-gen-0012": "Sunulan tamamlayıcı hizmetlerin önemi ne olursa olsun gayrimenkul her hâlde yatırım amaçlı gayrimenkul olarak sınıflandırılır",
    "std-tms40-gen-0013": "Ana ortaklığın bağlı ortaklığına kiraladığı bina hem bireysel hem konsolide tablolarda yatırım amaçlı gayrimenkul sayılır",
    "std-tms40-gen-0016": "Gelecekteki ekonomik yarar ve güvenilir ölçüm koşulları aranmaz; edinilen her gayrimenkul doğrudan muhasebeleştirilir",
    "std-tms40-gen-0017": "Gerçeğe uygun değeriyle ölçülür; edinimle ilgili işlem maliyetleri doğrudan gider olarak yazılır",
    "std-tms40-gen-0018": "İşletme açılış giderleri ve normal kayıp niteliğindeki tutarlar da yatırım amaçlı gayrimenkulün maliyetine dâhil edilir",
    "std-tms40-gen-0020": "İşletme her yatırım amaçlı gayrimenkul için ölçüm yöntemini serbestçe ve dönemden döneme değiştirerek seçebilir",
    "std-tms40-gen-0021": "Seçilen ölçüm yöntemi yalnızca yeni edinilen gayrimenkullere uygulanır; mevcut gayrimenkuller eski yöntemle ölçülür",
    "std-tms40-gen-0022": "Gerçeğe uygun değerdeki değişimden doğan kazanç veya kayıp diğer kapsamlı gelirde muhasebeleştirilir",
    "std-tms40-gen-0023": "Gerçeğe uygun değer yönteminde gayrimenkul için ayrıca amortisman ayrılır ve dönem gideri olarak yazılır",
    "std-tms40-gen-0024": "Maliyet yönteminde gayrimenkul her raporlama döneminde gerçeğe uygun değerine getirilerek yeniden ölçülür",
    "std-tms40-gen-0025": "Gerçeğe uygun değer yönteminden maliyet yöntemine geçiş serbesttir ve her zaman daha uygun bir sunum sağlar",
    "std-tms40-gen-0026": "Gerçeğe uygun değer güvenilir ölçülemese dahi gayrimenkul her hâlde gerçeğe uygun değer yöntemiyle ölçülmeye devam eder",
    "std-tms40-gen-0030": "Uygulama doğrudur; gerçeğe uygun değer yönteminde amortisman ayrılması standarda tümüyle uygundur",
    "std-tms40-gen-0033": "Transferler işletmenin yönetim niyetindeki değişikliğe göre yapılır; kullanımda fiili bir değişiklik aranmaz",
    "std-tms40-gen-0034": "Sahibi tarafından kullanılmaya başlanan yatırım amaçlı gayrimenkul stoklara transfer edilir",
    "std-tms40-gen-0035": "Satış amacıyla geliştirilmeye başlanan gayrimenkul TMS 16 kapsamındaki maddi duran varlıklara transfer edilir",
    "std-tms40-gen-0036": "Sahibi tarafından kullanımına son verilen gayrimenkul her hâlde stoklara transfer edilir",
    "std-tms40-gen-0037": "Bir yatırım amaçlı gayrimenkul satış amacıyla geliştirilmeye başlandığında hemen stoklara transfer edilir",
    "std-tms40-gen-0038": "Yatırım amaçlıdan sahibi tarafından kullanılana transferde varlığın ilk maliyet bedeli sonraki muhasebeleştirmeye esas alınır",
    "std-tms40-gen-0039": "Sahibi tarafından kullanılandan gerçeğe uygun değere transferde ortaya çıkan fark doğrudan kâr veya zarara yazılır",
    "std-tms40-gen-0040": "Stoklardan yatırım amaçlıya transferde gerçeğe uygun değer ile önceki defter değeri farkı doğrudan özkaynağa yansıtılır",
    "std-tms40-gen-0041": "Maliyet yöntemi uygulanan işletmede transferler gayrimenkulün defter değerini gerçeğe uygun değerine getirir",
    "std-tms40-gen-0046": "Yönetimin ileride kullanma niyeti oluştuğu anda gayrimenkul, fiili kullanım başlamasa dahi TMS 16'ya transfer edilir",
    "std-tms40-gen-0047": "Yatırım amaçlı gayrimenkul yalnızca fiziksel olarak yıkıldığında finansal tablo dışı bırakılır",
    "std-tms40-gen-0048": "Elden çıkarmadan doğan kazanç veya kayıp doğrudan özkaynakta muhasebeleştirilir; kâr veya zarara yansıtılmaz",
    "std-tms40-gen-0051": "Maliyet yöntemini uygulayan işletme, gerçeğe uygun değeri dipnotlarda hiçbir hâlde açıklamaz",
    "std-tms40-gen-0052": "Yatırım amaçlı gayrimenkullerin ölçümünde bağımsız değerleme uzmanı kullanılması her durumda gereklidir",
    "std-tms40-gen-0053": "Uygulama doğrudur; gerçeğe uygun değerdeki artışın özkaynakta gösterilmesi standarda uygundur",
    "std-tms40-gen-0054": "TMS 40 ile TMS 16 gerçeğe uygun değer yaklaşımları aynıdır; ikisinde de değer değişimi diğer kapsamlı gelirde gösterilir",
    "std-tms40-gen-0055": "Yatırım amaçlı gayrimenkulün gerçeğe uygun değeri işletmenin kendi iç tahminlerine göre ölçülür; TFRS 13 uygulanmaz",
    "std-tms40-gen-0056": "Yatırım amaçlı gayrimenkulle ilgili tüm sonraki harcamalar oluştukları dönemde doğrudan gider olarak yazılır",
    "std-tms40-gen-0057": "İnşa veya geliştirme aşamasındaki gayrimenkul her hâlde stok olarak sınıflandırılır; yatırım amaçlı sayılmaz",
    "std-tms40-gen-0059": "Otel binası, sunulan konaklama hizmetleri önemli olsa dahi her hâlde yatırım amaçlı gayrimenkul sayılır",
}

# tms_40'ta uzun-atma doğruyu %36 en-kısa yaptı; 10 soruda doğrunun altına
# kısa-çarpıcı yanlış eklenerek denge kuruldu (sayısal/kısa-kategori dokunulmadı).
TMS40_KISALT = {
    "std-tms40-gen-0003": {"A": "Diğer varlıklarla ortak nakit akışı yaratır"},
    "std-tms40-gen-0004": {"A": "Stok olarak sınıflandırılır"},
    "std-tms40-gen-0008": {"A": "Yatırım amaçlı gayrimenkuldür"},
    "std-tms40-gen-0009": {"B": "Yatırım amaçlı gayrimenkuldür"},
    "std-tms40-gen-0017": {"A": "Gerçeğe uygun değerle ölçülür"},
    "std-tms40-gen-0021": {"A": "Yalnızca yeni edinilenlere uygulanır"},
    "std-tms40-gen-0023": {"A": "Normal amortisman ayrılır"},
    "std-tms40-gen-0033": {"A": "Her raporlama döneminde yapılır"},
    "std-tms40-gen-0036": {"A": "Stoklara transfer edilir"},
    "std-tms40-gen-0055": {"A": "İşletmenin iç tahminine göre ölçülür"},
}

# ── TMS 1 · Finansal Tabloların Sunuluşu ──────────────────────────────────────
TMS1_OZEL = {
    "std-tms1-gen-0003": "Tam finansal tablo seti yalnızca finansal durum tablosu ile kâr veya zarar tablosundan oluşur; nakit akış tablosu ve dipnotlar zorunlu değildir",
    "std-tms1-gen-0015": "Varlıklar ile borçlar ve gelirler ile giderler her hâlde netleştirilerek finansal tablolarda tek bir net tutar biçiminde sunulur",
    "std-tms1-gen-0018": "Gerçeğe uygun sunum ancak TFRS hükümlerinden sapılarak sağlanır; TFRS'lere tam uyum tek başına gerçeğe uygun sunumu güvence altına almaz",
    "std-tms1-gen-0025": "Finansal durum tablosunda her hâlde likidite esasına göre sunum yapılır; dönen ve duran varlık ayrımına hiçbir koşulda izin verilmez",
    "std-tms1-gen-0027": "Bir yükümlülük yalnızca raporlama tarihinden sonraki on iki ay içinde ödenecekse kısa vadeli sayılır; normal faaliyet döngüsü ölçütü uygulanmaz",
    "std-tms1-gen-0032": "Ödenmiş sermaye ve yedekler gibi özkaynak kalemleri finansal durum tablosunda değil, yalnızca dipnotlarda gösterilir",
    "std-tms1-gen-0040": "Diğer kapsamlı gelir kalemleri her hâlde doğrudan kâr veya zarar tablosunda gösterilir; ayrı bir kapsamlı gelir bölümü kullanılmaz",
    "std-tms1-gen-0044": "Giderler yalnızca işlevlerine göre sınıflandırılarak sunulur; niteliklerine göre sunuma TMS 1 hiçbir hâlde izin vermez",
    "std-tms1-gen-0046": "Kâr veya zarar bölümünde asgari kalem sunma koşulu yoktur; işletme istediği kalemleri istediği ayrıntıda serbestçe sunar",
    "std-tms1-gen-0051": "Dipnotlar yalnızca sayısal tabloların bir özetini içerir; muhasebe politikaları ve hazırlama esasları dipnotlarda yer almaz",
    "std-tms1-gen-0056": "İşletme, sermayesini yönetme amaç ve politikalarına ilişkin hiçbir açıklama yapmaz; bu bilgiler ticari sır kapsamında tutulur",
}

# tms_1 doğru şıkları çok uzun (ort 102); yalnız 11 atma var, asıl kusur boy.
# 22 soruda doğru en uzundu; 13'ünde çeldirici içerikle üstüne çıkarıldı.
TMS1_UZAT = {
    "std-tms1-gen-0033": {"E": "Üçüncü tablonun sunulup sunulmayacağı tümüyle denetçinin takdirindedir; geriye dönük düzeltme veya yeniden sınıflandırma yapılsa dahi ek bir finansal durum tablosu hiçbir hâlde sunulmaz"},
    "std-tms1-gen-0002": {"A": "Yalnızca işletme yönetiminin iç kararları için hazırlanan ve dışa açıklanmayan belgelerdir; genel amaçlı finansal tablolar dış kullanıcıların bilgi ihtiyacını hiç gözetmez"},
    "std-tms1-gen-0028": {"C": "Normal faaliyet döngüsü, işletmenin kurulduğu tarihten tasfiye edildiği tarihe kadar geçen toplam süredir; varlıkların nakde dönüşme süresiyle hiçbir ilgisi yoktur"},
    "std-tms1-gen-0057": {"B": "Kâr payına ilişkin hiçbir bilgi açıklanmaz; kâr dağıtımı yalnızca ortakları ilgilendirdiğinden finansal tablo kullanıcılarına herhangi bir açıklama sunulmaz"},
    "std-tms1-gen-0053": {"E": "Muhasebe politikası açıklaması yalnızca politika değiştiğinde yapılır; değişiklik olmayan dönemlerde uygulanan politikalara ilişkin hiçbir açıklamaya yer verilmez"},
    "std-tms1-gen-0035": {"D": "Likidite esası, varlıkların büyükten küçüğe tutar sırasına göre dizilmesidir; kalemlerin nakde dönüşme hızı bu sıralamada hiçbir biçimde dikkate alınmaz"},
    "std-tms1-gen-0030": {"C": "Ertelenmiş vergi yükümlülükleri her hâlde kısa vadeli yükümlülük olarak sınıflandırılır; vade veya faaliyet döngüsü ölçütleri bunlara hiçbir koşulda uygulanmaz"},
    "std-tms1-gen-0044": {"D": "Giderler yalnızca işlevlerine göre sınıflandırılarak sunulur; niteliklerine göre sunum seçeneği kaldırılmış olup işletmeye bu konuda hiçbir tercih hakkı tanınmaz"},
    "std-tms1-gen-0016": {"A": "Finansal tablolarda yalnızca cari dönem verileri sunulur; önceki döneme ait karşılaştırmalı bilgilerin sunulması hiçbir hâlde gerekli görülmez ve karşılaştırma yapılmaz"},
    "std-tms1-gen-0012": {"B": "Tablolar her hâlde tasfiye esasına göre hazırlanır; işletmenin sürekliliği varsayımı yalnızca kamu kurumları için geçerli olup özel işletmelere uygulanmaz"},
    "std-tms1-gen-0017": {"B": "Sunum ve sınıflandırma hiçbir koşulda değiştirilemez; ilk dönemde seçilen biçim, daha uygun bir sunum ortaya çıksa dahi sonraki tüm dönemlerde aynen korunur"},
    "std-tms1-gen-0041": {"C": "Kapsamlı gelir yalnızca iki ayrı tabloda sunulabilir; tek bir kapsamlı gelir tablosunda sunum seçeneği TMS 1 tarafından hiçbir biçimde tanınmaz"},
    "std-tms1-gen-0014": {"B": "Tüm kalemler her hâlde ayrı ayrı sunulur; önemsiz olsa dahi hiçbir kalem benzerleriyle gruplandırılamaz ve tablolar aşırı ayrıntıyla doldurulur"},
}

# ── TMS 8 · Muhasebe Politikaları, Tahminler ve Hatalar ───────────────────────
TMS8_OZEL = {
    "std-tms8-gen-0002": "İşletme yönetimi, ilgili bir TFRS bulunsa dahi her işlem için en uygun gördüğü muhasebe politikasını serbestçe belirleyebilir",
    "std-tms8-gen-0006": "Benzer işlemler için her dönem farklı politikalar seçilebilir; tutarlılık koşulu yalnızca aynı raporlama dönemi içinde aranır",
    "std-tms8-gen-0017": "Yeni politika yalnızca değişiklik tarihinden sonraki işlemlere uygulanır; geçmiş dönem tutarları hiçbir hâlde yeniden düzenlenmez",
    "std-tms8-gen-0024": "Uygulanabilir olmama, işletmenin bir hükmü uygulamayı maliyetli ya da zahmetli bulması durumunu ifade eden bir kavramdır",
    "std-tms8-gen-0029": "Muhasebe tahminleri, ölçüm belirsizliği içermeyen ve geçmiş verilerden kesin olarak hesaplanabilen parasal tutarlardır",
    "std-tms8-gen-0036": "İşletme tahmin geliştirirken yalnızca geçmiş dönem verilerini kullanır; makul gelecek beklentileri ve güncel bilgiler dikkate alınmaz",
    "std-tms8-gen-0045": "Önceki dönem hataları yalnızca kasıtlı yapılan yanlışlıkları kapsar; dikkatsizlik veya ihmalden doğan yanlışlıklar hata sayılmaz",
    "std-tms8-gen-0047": "Önceki dönem hatasının düzeltmesi, keşfedildiği cari dönemin kâr veya zararına gider ya da gelir olarak yansıtılır",
    "std-tms8-gen-0050": "Önemsiz sayılabilecek kasıtlı hatalar içeren finansal tablolar da TFRS'lere tümüyle uygun kabul edilir ve düzeltme gerektirmez",
    "std-tms8-gen-0051": "Hatalar yalnızca matematiksel yanlışlıklardan doğar; politikaların yanlış uygulanması veya bilgilerin yanlış yorumlanması hata sayılmaz",
}

# tms_8'de yalnız 10 atma var; asıl kusur doğru şıkların kısa olması (24 soruda
# en kısa). 14 soruda doğrunun ALTINA kısa-çarpıcı çeldirici (doğrunun tersi,
# aynı register). Kalan 10 en-kısa bırakılır (~%20). Motor len<doğru assert eder.
TMS8_KISALT = {
    "std-tms8-gen-0030": {"B": "Geriye dönük uygulanır"},
    "std-tms8-gen-0054": {"B": "Stok hatası bulunmamaktadır"},
    "std-tms8-gen-0016": {"A": "İleriye dönük uygulanır"},
    "std-tms8-gen-0050": {"A": "Tablolar TFRS'lere uygundur"},
    "std-tms8-gen-0020": {"E": "İleriye dönük uygulanır"},
    "std-tms8-gen-0019": {"B": "İleriye dönük uygulanır"},
    "std-tms8-gen-0022": {"D": "Politika değişikliğidir"},
    "std-tms8-gen-0046": {"C": "Cari dönemde düzeltilir"},
    "std-tms8-gen-0010": {"D": "Bir muhasebe tahminidir"},
    "std-tms8-gen-0047": {"A": "Cari dönem zararına yazılır"},
    "std-tms8-gen-0033": {"A": "Politika değişikliğidir; geriye dönük uygulanır"},
    "std-tms8-gen-0032": {"A": "Politika değişikliği sayılır"},
    "std-tms8-gen-0002": {"C": "Vergi mevzuatına göre belirlenir"},
    "std-tms8-gen-0007": {"A": "Tek bir ortak politika seçilir"},
}

KONFIG: dict[str, dict] = {
    "tms_12_gelir_vergileri": {"atma": TMS12_ATMA, "atma_ozel": TMS12_OZEL,
                               "uzat": TMS12_UZAT},
    "tms_21_kur_degisimi": {"atma_ozel": TMS21_OZEL, "uzat": TMS21_UZAT},
    "tfrs_9_finansal_arac": {"atma_ozel": TFRS9_OZEL, "uzat": TFRS9_UZAT},
    "tms_37_karsiliklar": {"atma_ozel": TMS37_OZEL},
    "tms_8_politikalar": {"atma_ozel": TMS8_OZEL, "kisalt": TMS8_KISALT},
    "tms_1_sunulus": {"atma_ozel": TMS1_OZEL, "uzat": TMS1_UZAT},
    "tms_40_yatirim_amacli": {"atma_ozel": TMS40_OZEL, "kisalt": TMS40_KISALT},
    "tms_23_borclanma_maliyetleri": {"atma_ozel": TMS23_OZEL},
    "tfrs_16_kiralamalar": {"atma_ozel": TFRS16_OZEL, "uzat": TFRS16_UZAT},
    "tms_7_nakit_akis": {"atma_ozel": TMS7_OZEL, "uzat": TMS7_UZAT},
    "kavramsal_cerceve": {"atma_ozel": KAVRAM_OZEL, "uzat": KAVRAM_UZAT},
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
