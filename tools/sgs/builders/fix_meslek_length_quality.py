#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Meslek Hukuku paketlerindeki salt şık-boy ipucunu doğal dille giderir.

Doğru önermelerin anlamı ve cevap harfi korunur. Uzun doğru seçenekler soru
kökünde zaten bulunan bağlamdan arındırılır; yapay uzun birkaç çeldirici yakın
ama yanlış kurum/ceza önermesine indirilir. İçerik ve uygulama kopyası birlikte
yazılır.

⚠️ SAHIPLIK DEVRI (2026-08-14): meslek_hukuku/sorumluluk_ve_yasaklar.json blogu
bu dosyadan CIKARILDI. O paketin 60 sorusunun tamami yapisal kalibrasyon turunda
yeniden yazildi ve sahiplik build_hukuk_meslek_sorumluluk_yapisal.py dosyasina
gecti. Bir sorunun tek sahibi olmali.

⚠️ SAHIPLIK DEVRI (2026-08-14): meslek_hukuku/staj_ve_sinavlar.json blogu bu
dosyadan CIKARILDI; sahiplik build_hukuk_meslek_staj_yapisal.py'ye gecti.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
APP = ROOT.parent / "smmm_sgs_pratik" / "assets" / "content"


CORRECT_REWRITES = {
}


DISTRACTOR_REWRITES = {
}


def fix_file(rel: str) -> int:
    src = ROOT / "content" / rel
    data = json.loads(src.read_text(encoding="utf-8"))
    by_id = {q["id"]: q for q in data}
    changed = 0

    for qid, new in CORRECT_REWRITES.get(rel, {}).items():
        q = by_id[qid]
        answer = q["answer"]
        if q["options"][answer] != new:
            q["options"][answer] = new
            changed += 1

    for qid, replacements in DISTRACTOR_REWRITES.get(rel, {}).items():
        q = by_id[qid]
        for letter, new in replacements.items():
            assert letter != q["answer"], f"{qid}: doğru şık değiştirilemez"
            if q["options"][letter] != new:
                q["options"][letter] = new
                changed += 1

    for q in data:
        assert len(q["options"]) == 5
        assert len(set(q["options"].values())) == 5, q["id"]
        assert q["answer"] in q["options"], q["id"]

    payload = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    src.write_text(payload, encoding="utf-8")
    target = APP / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(payload, encoding="utf-8")
    return changed


if __name__ == "__main__":
    # ⚠️ Bu builder --check DESTEKLEMEZ ve calistiginda dogrudan YAZAR.
    # Toplu dogrulama donguleri onu "--check" ile cagirdiginda argumani sessizce
    # yok sayip yayinlanmis icerigi geri yaziyordu (2026-08-14'te
    # meslek_orgutu_disiplin.json'da gerceklesti). Artik argumanla cagrilirsa
    # yazmadan hata verir.
    import sys
    if sys.argv[1:]:
        print("HATA: bu builder arguman kabul etmez ve calistiginda dogrudan YAZAR.")
        print("Dogrulama icin git diff kullanin; yazmak icin argumansiz calistirin.")
        raise SystemExit(2)
    files = sorted(set(CORRECT_REWRITES) | set(DISTRACTOR_REWRITES))
    for rel in files:
        print(f"{rel}: {fix_file(rel)} doğal şık düzeltmesi")
