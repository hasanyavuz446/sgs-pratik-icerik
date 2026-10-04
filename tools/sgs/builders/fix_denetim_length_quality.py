#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Denetim paketlerindeki şık-boy ipucunu doğal ve öz seçeneklerle giderir."""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
APP = ROOT.parent / "smmm_sgs_pratik" / "assets" / "content"


CORRECT = {
}


DISTRACTORS = {
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
    for rel in sorted(set(CORRECT) | set(DISTRACTORS)):
        print(f"{rel}: {fix(rel)} doğal şık düzeltmesi")
