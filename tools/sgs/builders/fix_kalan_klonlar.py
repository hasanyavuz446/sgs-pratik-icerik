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
    # mali_duran_varliklar: build_fm_mali_duran_varliklar_cok_adimli.py devraldı (2026-09-27)

    # maliyet_hesaplari: build_fm_maliyet_hesaplari_cok_adimli.py devraldı (2026-09-27)

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
