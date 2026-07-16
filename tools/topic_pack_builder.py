#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yeterlilik konu havuzları için ortak, deterministik builder.

Her konu builder'ı 26 yapısal kuralı iki farklı kökle ve 8 öncüllü soruyu
tanımlar. Böylece 60 özgün soru; dengeli, örüntüsüz harf dağılımıyla üretilir.
"""
from __future__ import annotations

import json
import random
from pathlib import Path


APP_ROOT = Path("/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik")


def balanced_letters(seed: int) -> list[str]:
    rnd = random.Random(seed)
    while True:
        seq = list("ABCDE") * 12
        rnd.shuffle(seq)
        if all(not (seq[i] == seq[i - 1] == seq[i - 2]) for i in range(2, 60)):
            return seq


def premise_options(correct: str) -> list[str]:
    universe = ["Yalnız I", "Yalnız II", "Yalnız III", "I ve II", "I ve III", "II ve III", "I, II ve III"]
    assert correct in universe
    preferred = ["I, II ve III", "I ve II", "I ve III", "II ve III", "Yalnız I", "Yalnız II", "Yalnız III"]
    return [x for x in preferred if x != correct][:4]


def build_topic(
    *, lesson_id: str, topic_id: str, label: str, slug: str, prefix: str,
    seed: int, legislation_version: str, rules: list[dict], premises: list[dict],
    wrong_banks: dict[str, list[str]],
) -> list[dict]:
    assert len(rules) == 26, f"{label}: 26 kural olmalı, {len(rules)} var"
    assert len(premises) == 8, f"{label}: 8 öncüllü soru olmalı"
    assert sum(p["correct"] == "I, II ve III" for p in premises) == 2

    raw: list[dict] = []
    for idx, rule in enumerate(rules):
        if rule.get("distractors"):
            distractors = rule["distractors"]
        else:
            assert rule["correct"] not in wrong_banks[rule["bank"]]
            bank = wrong_banks[rule["bank"]]
            assert len(set(bank)) >= 6
            start = (idx * 3 + seed) % len(bank)
            distractors = []
            for offset in range(len(bank)):
                candidate = bank[(start + offset) % len(bank)]
                if candidate != rule["correct"] and candidate not in distractors:
                    distractors.append(candidate)
                if len(distractors) == 4:
                    break
        assert len(distractors) == 4
        assert len(set(distractors)) == 4
        for stem_key in ("scenario", "focus"):
            raw.append({
                "stem": rule[stem_key], "correct": rule["correct"],
                "distractors": distractors, "why": rule["why"],
                "ref": rule["ref"], "difficulty": rule.get("difficulty", "medium"),
            })

    for p in premises:
        raw.append({
            "stem": p["stem"], "correct": p["correct"],
            "distractors": premise_options(p["correct"]), "why": p["why"],
            "ref": p["ref"], "difficulty": p.get("difficulty", "hard"),
        })

    assert len(raw) == 60
    letters = balanced_letters(seed)
    out = []
    for i, (item, answer) in enumerate(zip(raw, letters), 1):
        assert len(item["distractors"]) == 4
        assert item["correct"] not in item["distractors"]
        choices = {answer: item["correct"]}
        other_letters = [letter for letter in "ABCDE" if letter != answer]
        for letter, distractor in zip(other_letters, item["distractors"]):
            choices[letter] = distractor
        assert set(choices) == set("ABCDE")
        assert len(set(choices.values())) == 5
        out.append({
            "id": f"{prefix}-{i:04d}",
            "lessonId": lesson_id,
            "topicId": topic_id,
            "question": item["stem"],
            "choices": choices,
            "correctAnswer": answer,
            "explanation": item["why"],
            "source": {
                "kind": "generated",
                "styleRef": "2026 SMMM beş seçenekli test",
                "legislationRef": item["ref"],
            },
            "tags": ["Demo Soru", "2026 Formatı", "Konu Havuzu", label],
            "difficulty": item["difficulty"],
            "updatedAt": "2026-07-16T00:00:00Z",
            "examPeriod": "2026 test sistemine uyumlu özgün soru",
            "legislationVersion": legislation_version,
            "sourceUpdatedAt": "2026-07-16T00:00:00Z",
            "isPremium": False,
            "isActive": True,
        })
    return out


def write_topic(*, slug: str, **kwargs) -> Path:
    data = build_topic(slug=slug, **kwargs)
    target = APP_ROOT / "assets/content/yeterlilik" / f"questions_topic_{slug}_2026.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"yazıldı: {target} ({len(data)} soru)")
    return target
