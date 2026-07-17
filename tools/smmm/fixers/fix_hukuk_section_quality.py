#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Legacy Hukuk bölüm paketindeki hedefli şık dengesi düzeltmesini uygular."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
TARGETS = (
    ROOT / "content" / "yeterlilik" / "questions_hukuk_2026.json",
    ROOT.parent / "smmm_sgs_pratik" / "assets" / "content" / "yeterlilik" / "questions_hukuk_2026.json",
)
QUESTION_ID = "demo-is-007"
OLD = "Yalnız kamu idarelerinde kadrolu çalışanlar"
NEW = "Yalnız kamu idarelerinde memur statüsünde ve kadrolu olarak çalışanlar"
LESSON_IDS = {
    "demo-is-003": "is_hukuku",
    "demo-is-004": "is_hukuku",
    "demo-is-005": "is_hukuku",
    "demo-is-006": "is_hukuku",
    "demo-is-007": "sosyal_guvenlik_mevzuati",
}


def update(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    data = json.loads(original)
    question = next(item for item in data if item["id"] == QUESTION_ID)
    current = question["choices"]["B"]
    updated = original
    if current == OLD:
        updated = updated.replace(f'"B":"{OLD}"', f'"B":"{NEW}"', 1)
    elif current != NEW:
        raise AssertionError(f"Beklenmeyen mevcut şık: {current!r}")

    for question_id, lesson_id in LESSON_IDS.items():
        lines = updated.splitlines(keepends=True)
        index = next(i for i, line in enumerate(lines) if f'"id":"{question_id}"' in line)
        line = lines[index]
        line = re.sub(r'"lessonId":"[^"]+"', f'"lessonId":"{lesson_id}"', line, count=1)
        lines[index] = line
        updated = "".join(lines)

    parsed = json.loads(updated)
    changed = next(item for item in parsed if item["id"] == QUESTION_ID)
    assert changed["choices"]["B"] == NEW
    for question_id, lesson_id in LESSON_IDS.items():
        normalized = next(item for item in parsed if item["id"] == question_id)
        assert normalized["lessonId"] == lesson_id
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


if __name__ == "__main__":
    results = [update(path) for path in TARGETS]
    print(f"Hukuk paketleri güncellendi: {sum(results)}/{len(TARGETS)}")
