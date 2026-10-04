#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kalan SGS paketlerindeki kör-tahmin şık ipuçlarını doğal biçimde giderir.
⚠️ SAHIPLIK DEVRI: vergi_hukuku/vergilendirme_sureci.json bloku bu dosyadan CIKARILDI; sahiplik
build_hukuk_vergi_surec_yapisal.py dosyasina gecti. Bir sorunun tek sahibi olmali.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
APP = ROOT.parent / "smmm_sgs_pratik" / "assets" / "content"


CORRECT = {
}


DISTRACTORS = {
    "ataturk_ilkeleri/ataturk_inkilaplari.json": {
        "ait-inkilap-gen-0004": {"B": "Türk Harflerinin Kabul ve Tatbiki Hakkında Kanun"},
    },
}


FULL_OPTIONS = {
}


def fix(rel: str) -> int:
    source = ROOT / "content" / rel
    data = json.loads(source.read_text(encoding="utf-8"))
    by_id = {q["id"]: q for q in data}
    changed = 0
    for qid, new in CORRECT.get(rel, {}).items():
        q = by_id[qid]
        if q["options"][q["answer"]] != new:
            q["options"][q["answer"]] = new
            changed += 1
    for qid, replacements in DISTRACTORS.get(rel, {}).items():
        q = by_id[qid]
        for letter, new in replacements.items():
            assert letter != q["answer"], qid
            if q["options"][letter] != new:
                q["options"][letter] = new
                changed += 1
    for qid, replacements in FULL_OPTIONS.get(rel, {}).items():
        q = by_id[qid]
        assert set(replacements) == set("ABCDE"), qid
        for letter, new in replacements.items():
            if q["options"][letter] != new:
                q["options"][letter] = new
                changed += 1
    for q in data:
        assert set(q["options"]) == set("ABCDE"), q["id"]
        assert len(set(q["options"].values())) == 5, q["id"]
    payload = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    source.write_text(payload, encoding="utf-8")
    target = APP / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(payload, encoding="utf-8")
    return changed


if __name__ == "__main__":
    # ⚠️ Bu builder --check DESTEKLEMEZ ve calistiginda dogrudan YAZAR.
    # Toplu dogrulama donguleri onu "--check" ile cagirdiginda argumani sessizce
    # yok sayip yayinlanmis icerigi geri yazar. Artik arguman verilirse yazmadan
    # hata verip cikar.
    import sys
    if sys.argv[1:]:
        print("HATA: bu builder arguman kabul etmez ve calistiginda dogrudan YAZAR.")
        print("Dogrulama icin git diff kullanin; yazmak icin argumansiz calistirin.")
        raise SystemExit(2)
    paths = set(CORRECT) | set(DISTRACTORS) | set(FULL_OPTIONS)
    for rel in sorted(paths):
        print(f"{rel}: {fix(rel)} doğal şık düzeltmesi")
