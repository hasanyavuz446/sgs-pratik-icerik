#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SGS içerik yapısı ve mekanik kalite denetimi.

Bu araç yalnız SGS `{ders, konu, stem, options, answer, solution}` şemasını ve
manifestte `programIds=["sgs"]` olarak kayıtlı paketleri kabul eder. SMMM'ye özgü
soru tipi kotalarını uygulamaz.
"""
from __future__ import annotations

import collections
import json
import os
import re
import sys


LETTERS = set("ABCDE")
DEMO = re.compile(r"demo\s+(?:soru|açıklama)", re.IGNORECASE)


def load(path: str) -> list[dict]:
    data = json.load(open(path, encoding="utf-8"))
    return data if isinstance(data, list) else data.get("questions", [])


def letter_pattern(sequence: str) -> bool:
    if len(sequence) < 10:
        return False
    for period in range(1, min(11, len(sequence))):
        compared = len(sequence) - period
        matches = sum(sequence[i] == sequence[i + period] for i in range(compared))
        if compared and matches / compared >= 0.9:
            return True
    return False


def audit(path: str) -> tuple[int, list[tuple[str, str]]]:
    questions = load(path)
    issues: list[tuple[str, str]] = []
    ids: set[str] = set()
    stems: set[str] = set()
    answers = []

    for index, question in enumerate(questions, 1):
        qid = str(question.get("id") or f"#{index}")
        if qid in ids:
            issues.append(("FATAL", f"yinelenen id: {qid}"))
        ids.add(qid)

        required = ("ders", "konu", "stem", "options", "answer", "solution")
        missing = [field for field in required if not question.get(field)]
        if missing:
            issues.append(("FATAL", f"{qid}: eksik alan: {', '.join(missing)}"))
            continue

        stem = re.sub(r"\s+", " ", question["stem"]).strip().casefold()

        options = question["options"]
        if not isinstance(options, dict) or set(options) != LETTERS:
            issues.append(("FATAL", f"{qid}: seçenekler tam A–E değil"))
            continue
        if any(not isinstance(value, str) or not value.strip() for value in options.values()):
            issues.append(("FATAL", f"{qid}: boş seçenek var"))
        normalized = {re.sub(r"\s+", " ", value).strip().casefold() for value in options.values()}
        if len(normalized) != 5:
            issues.append(("FATAL", f"{qid}: yinelenen seçenek var"))

        # Kopya ölçütü kök DEĞİL, kök + şık kümesidir. Genel kökler ("Aşağıdakilerden
        # hangisi ... değildir?") farklı şıklarla meşru olarak tekrar eder; yalnız köke
        # bakmak 16 pakette 43 sahte FATAL üretiyordu. Şıklar küme olarak alındığından
        # harf permütasyonuyla çoğaltılmış gerçek kopya da yakalanır.
        signature = (stem, frozenset(normalized))
        if signature in stems:
            issues.append(("FATAL", f"yinelenen soru (kök ve şıklar aynı): {qid}"))
        stems.add(signature)

        answer = question["answer"]
        if answer not in options:
            issues.append(("FATAL", f"{qid}: cevap seçeneklerde değil"))
        else:
            answers.append(answer)

        visible = f"{question['stem']} {question['solution']}"
        if DEMO.search(visible):
            issues.append(("FATAL", f"{qid}: kullanıcıya görünen demo ifadesi"))

        source = question.get("source")
        if not isinstance(source, dict) or not str(source.get("legislationRef", "")).strip():
            issues.append(("UYARI", f"{qid}: kaynak/dayanak eksik"))

    sequence = "".join(answers)
    if letter_pattern(sequence):
        issues.append(("FATAL", "cevap harflerinde kısa periyot/örüntü var"))
    if len(sequence) >= 20:
        counts = collections.Counter(sequence)
        expected = len(sequence) / 5
        if any(abs(counts[letter] - expected) > max(2, expected * 0.35) for letter in "ABCDE"):
            issues.append(("UYARI", f"cevap harfi dağılımı dengesiz: {dict(counts)}"))

    return len(questions), issues


def manifest_paths(path: str) -> list[str]:
    manifest = json.load(open(path, encoding="utf-8"))
    base = os.path.dirname(path)
    result = []
    for pack in manifest.get("packs", []):
        if "sgs" not in pack.get("programIds", []):
            continue
        candidates = (
            os.path.join(base, pack["file"]),
            os.path.join(os.path.dirname(base), pack["file"]),
        )
        existing = next((candidate for candidate in candidates if os.path.exists(candidate)), None)
        if existing:
            result.append(existing)
    return result


def main() -> int:
    args = sys.argv[1:]
    paths = [arg for arg in args if not arg.startswith("--")]
    if "--manifest" in args:
        if not paths:
            print("--manifest için manifest yolu gerekli.")
            return 2
        paths = manifest_paths(paths[0])
    if not paths:
        print(__doc__)
        return 2

    repo = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
    content = os.path.join(repo, "content")
    forbidden = os.path.join(content, "yeterlilik")
    totals = collections.Counter()
    for path in paths:
        resolved = os.path.realpath(path)
        if os.path.commonpath((content, resolved)) != content or os.path.commonpath((forbidden, resolved)) == forbidden:
            print(f"SGS kapsamı dışında dosya reddedildi: {path}")
            return 2
        count, issues = audit(path)
        severity = collections.Counter(level for level, _ in issues)
        totals.update(severity)
        flag = "❌" if severity["FATAL"] else ("⚠️" if severity["UYARI"] else "✅")
        print(f"{flag} {os.path.basename(path):48} {count:4} soru | FATAL {severity['FATAL']:3} UYARI {severity['UYARI']:3}")
        for level, message in issues[:20]:
            print(f"    [{level}] {message}")
    print(f"TOPLAM: FATAL {totals['FATAL']} | UYARI {totals['UYARI']}")
    return 1 if totals["FATAL"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
