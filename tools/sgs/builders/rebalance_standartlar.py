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

KONFIG: dict[str, dict] = {}


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
    sonuc = temizle(path, atma_yerine=cfg.get("atma"), kisalt=cfg.get("kisalt"))
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
