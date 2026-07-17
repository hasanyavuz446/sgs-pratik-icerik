# -*- coding: utf-8 -*-
"""Kalan 16 şablon klonunu giderir (8 dosya, 11 farklı formül).

Bu dosyalarda klon sayısı 1-4 arasında; her birine ayrı builder yazmak aşırı
olurdu. Onun yerine hedefli yama: girdi değiştirilir, cevap farklılaşır, doğru
şıkkın metni güncellenir.

★ Neden çeldiriciler KORUNUYOR? trend/yatay/denetim_riski'nde çeldiriciler
formülden türetiliyordu ve sayı değişince anlamsızlaşıyorlardı; orada builder
yazmak zorunlu oldu. Buradaki dosyalarda çeldiriciler zaten "yakın yanlış sayı"
niteliğinde (bölme hatası, ters oran, ondalık kayması) ve girdi değişince de
makul kalıyorlar. Bu yüzden yalnız doğru şık güncelleniyor.
⚠ Riski assertion kapatıyor: yeni cevap bir çeldiriciyle çakışırsa yama durur.
   Nitekim ilk denemede 4 çakışma çıktı (oran-0054 → 5, dikey-0045 → %40,
   dikey-0056 → %30, mhk-0051 → 3.000 zaten şıktaydı) ve değerler değiştirildi.

Her yama önce ESKİ hesabı doğrular; tutmuyorsa durur (kör düzeltme yapmamak için).
"""
import json
import re

KOK = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/"


def tr(n):
    return f"{int(n):,}".replace(",", ".")


# id → (dosya, eski_cevap, yeni_cevap, kök dönüşümü, yeni çözüm)
# Kökteki sayılar tam metin eşlemesiyle değişir; kalan ifade korunur.
YAMA = [
    # ── mali_duran_varliklar: pay ÷ sermaye → oran + TDHP sınıflaması
    ("finansal_muhasebe/mali_duran_varliklar.json", "finmuh-malidv-gen-0049",
     "%40 – İştirak (242)", "%20 – İştirak (242)",
     [("300.000", "150.000")],
     "Sahiplik oranı = 150.000 ÷ 750.000 = **%20** → %10–%50 aralığında olduğundan "
     "**İştirak (242)**."),

    # ── maliyet_hesaplari: toplam maliyet ÷ üretim miktarı
    ("finansal_muhasebe/maliyet_hesaplari.json", "finmuh-mlh-gen-0051",
     "300", "320",
     [("750.000", "800.000")],
     "Birim maliyet = 800.000 ÷ 2.500 = **320 ₺/birim**."),

    # ── oran_analizi: net kâr marjı · stok devir hızı · cari oran
    ("mali_tablolar_analizi/oran_analizi.json", "mta-oran-gen-0052",
     "%15", "%20",
     [("120.000", "160.000")],
     "Net Kâr Marjı = (160.000 ÷ 800.000) × 100 = **%20**."),
    ("mali_tablolar_analizi/oran_analizi.json", "mta-oran-gen-0054",
     "6", "3",
     [("125.000", "250.000")],
     "Stok Devir Hızı = 750.000 ÷ 250.000 = **3**. Bölen ORTALAMA STOKTUR."),
    ("mali_tablolar_analizi/oran_analizi.json", "mta-oran-gen-0055",
     "2,0", "2,5",
     [("350.000", "280.000")],
     "Cari Oran = 700.000 ÷ 280.000 = **2,5**."),

    # ── dikey_analiz: kalem ÷ net satışlar
    ("mali_tablolar_analizi/dikey_analiz.json", "mta-dikey-gen-0045",
     "%60", "%50",
     [("450.000", "375.000")],
     "Dikey Yüzde = (375.000 ÷ 750.000) × 100 = **%50**."),
    ("mali_tablolar_analizi/dikey_analiz.json", "mta-dikey-gen-0046",
     "%15", "%25",
     [("120.000", "200.000")],
     "Dikey Yüzde = (200.000 ÷ 800.000) × 100 = **%25**."),
    ("mali_tablolar_analizi/dikey_analiz.json", "mta-dikey-gen-0053",
     "%15", "%10",
     [("45.000", "30.000")],
     "Dikey Yüzde = (30.000 ÷ 300.000) × 100 = **%10**."),
    ("mali_tablolar_analizi/dikey_analiz.json", "mta-dikey-gen-0056",
     "%20", "%25",
     [("180.000", "225.000")],
     "Dikey Yüzde = (225.000 ÷ 900.000) × 100 = **%25**."),

    # ── fon_akim: net kâr + nakit çıkışı gerektirmeyen giderler
    ("mali_tablolar_analizi/fon_akim_analizi.json", "mta-fon-gen-0042",
     "200.000", "160.000",
     [("90.000", "50.000")],
     "Faaliyetlerden Fon = 100.000 + 50.000 + 10.000 = **160.000 ₺**. Amortisman ve "
     "karşılık giderleri nakit çıkışı gerektirmediğinden kâra eklenir."),

    # ── nakit_akim: dönem sonu nakit · net nakit akışı
    ("mali_tablolar_analizi/nakit_akim_analizi.json", "mta-nakit-gen-0029",
     "200.000", "180.000",
     [("80.000", "60.000")],
     "Dönem Sonu Nakit = 120.000 + 60.000 = **180.000 ₺**."),
    ("mali_tablolar_analizi/nakit_akim_analizi.json", "mta-nakit-gen-0053",
     "150.000", "200.000",
     [("350.000", "300.000")],
     "Net Nakit Akışı = 500.000 − 300.000 = **+200.000 ₺**."),

    # ── maliyet_hacim_kar: başabaş = sabit maliyet ÷ birim katkı payı
    ("maliyet_muhasebesi/maliyet_hacim_kar.json", "mmuh-mhk-gen-0027",
     "5.000", "7.000",
     [("160.000", "210.000"), ("32 ₺", "30 ₺")],
     "Başabaş Noktası = 210.000 ÷ 30 = **7.000 birim**."),
    ("maliyet_muhasebesi/maliyet_hacim_kar.json", "mmuh-mhk-gen-0037",
     "5.000", "8.000",
     [("48 ₺", "30 ₺")],
     "Başabaş Noktası = 240.000 ÷ 30 = **8.000 birim**."),
    ("maliyet_muhasebesi/maliyet_hacim_kar.json", "mmuh-mhk-gen-0051",
     "5.000", "10.000",
     [("24 ₺", "12 ₺")],
     "Başabaş Noktası = 120.000 ÷ 12 = **10.000 birim**."),

    # ── safha_maliyeti: toplam maliyet ÷ eşdeğer birim
    ("maliyet_muhasebesi/safha_maliyeti.json", "mmuh-safha-gen-0041",
     "50", "55",
     [("900.000", "990.000")],
     "Eşdeğer ürün = 15.000 + (6.000 × %50) = 18.000 birim. Eşdeğer birim maliyet = "
     "990.000 ÷ 18.000 = **55 ₺/birim**."),
]

if __name__ == "__main__":
    dosyalar = {}
    for yol, qid, eski, yeni, degisim, cozum in YAMA:
        qs = dosyalar.setdefault(yol, json.load(open(KOK + yol, encoding="utf-8")))
        q = next(x for x in qs if x["id"] == qid)

        # Kör düzeltme yapma: önce eski hâlin beklediğimiz gibi olduğunu doğrula.
        assert q["options"][q["answer"]] == eski, \
            f"{qid}: eski cevap {q['options'][q['answer']]!r} bekleniyordu {eski!r}"

        kok = q["stem"]
        for bul, koy in degisim:
            assert bul in kok, f"{qid}: kökte {bul!r} yok"
            kok = kok.replace(bul, koy, 1)
        q["stem"] = kok
        q["options"][q["answer"]] = yeni          # harf korunur → dağılım bozulmaz
        q["solution"] = cozum
        assert len(set(q["options"].values())) == 5, \
            f"{qid}: yeni cevap {yeni!r} bir çeldiriciyle çakıştı: {q['options']}"

    for yol, qs in dosyalar.items():
        gorulen = {}
        for q in qs:
            anahtar = (re.sub(r"[\d.,]+", "#", q["stem"]), q["options"][q["answer"]])
            assert anahtar not in gorulen, f"HÂLÂ KLON: {q['id']} ↔ {gorulen[anahtar]}"
            gorulen[anahtar] = q["id"]
        json.dump(qs, open(KOK + yol, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print(f"düzeltilen klon: {len(YAMA)} | dosya: {len(dosyalar)}")
