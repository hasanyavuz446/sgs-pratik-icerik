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

KONFIG: dict[str, dict] = {
    "tms_12_gelir_vergileri": {"atma": TMS12_ATMA, "atma_ozel": TMS12_OZEL,
                               "uzat": TMS12_UZAT},
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
