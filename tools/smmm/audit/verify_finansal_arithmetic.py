#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Finansal Muhasebe paketlerindeki sayısal vakaları doğrular.

audit.py'nin CALC deseni, gerçek hesap sorularının yanında yalnız hesap kodu veya
senaryo tutarı içeren kayıt/sınıflandırma sorularını da "hesap" sayar. Düzeltme
öncesindeki 112 vakanın tamamı burada envantere alınır:

- Her 112 vakada doğru seçenek metni baseline ile karşılaştırılır.
- Sonucu aritmetik işlemle bulunan 33 vakada sonuç Python ile yeniden hesaplanır
  ve çözümdeki ara sonuçların varlığı doğrulanır.
- Kalan 79 vaka, tutarı yalnız kayıt veya sınıflandırma bağlamı olarak kullanan
  sayısal bağlam sorularıdır; doğru metin koruma kontrolüne tabidir.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTENT = ROOT / "content" / "yeterlilik"
BASELINE = ROOT / "tools" / "smmm" / "baselines" / "finansal_answer_baseline.json"
FILES = sorted(CONTENT.glob("questions_topic_finansal_*.json"))


def ids(prefix: str, values: list[int]) -> set[str]:
    return {f"topic-finansal-{prefix}-{value:03d}" for value in values}


ORIGINAL_AUDIT_IDS = set()
ORIGINAL_AUDIT_IDS |= ids("temel", [6, 14, 26, 48, 49, 59])
ORIGINAL_AUDIT_IDS |= ids(
    "kayit",
    list(range(6, 45))
    + [46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 59, 60],
)
ORIGINAL_AUDIT_IDS |= ids(
    "stok",
    [3, 6, 16, 28, 29, 30, 31, 32, 33, 34, 35, 36, 41, 42, 43, 60],
)
ORIGINAL_AUDIT_IDS |= ids(
    "donem",
    [6, 7, 12, 13, 16, 17, 18, 19, 21, 22, 24, 26, 27, 28, 29, 32,
     33, 36, 38, 39, 40, 41, 44, 45, 49, 51, 52, 54],
)
ORIGINAL_AUDIT_IDS |= ids(
    "tfrs",
    [7, 14, 16, 18, 20, 21, 23, 51, 52, 54],
)
assert len(ORIGINAL_AUDIT_IDS) == 112


def money(value: float | int) -> str:
    return f"{value:,.0f}".replace(",", ".") + " TL"


def check(answer: str, *fragments: str) -> tuple[str, tuple[str, ...]]:
    return answer, fragments


def calculation_checks() -> dict[str, tuple[str, tuple[str, ...]]]:
    """Tüm sonuçlar sabit cevap yazmak yerine girdilerden yeniden hesaplanır."""
    checks = {
        # Muhasebe kayıtları
        "topic-finansal-kayit-018": check(
            "I, II ve III",
            money(18_000 / 1.20),
            money(18_000 - 18_000 / 1.20),
        ),
        "topic-finansal-kayit-024": check(
            "I ve II",
            money(60_000 / 6),
            money((60_000 / 6) * 2),
        ),
        "topic-finansal-kayit-040": check(
            "I, II ve III",
            money(26_000 - 21_000),
        ),
        "topic-finansal-kayit-047": check(
            "Fark 9'a tam bölünebilir.",
            str(540 - 450),
        ),
        "topic-finansal-kayit-054": check(
            "I ve III",
            money(50_000),
            money(50_000 - 10_000),
            money(10_000),
        ),

        # Stoklar
        "topic-finansal-stok-003": check(
            money(80_000 - 6_000 - 4_000),
            money(80_000 - 6_000 - 4_000),
        ),
        "topic-finansal-stok-006": check(
            money(120_000 - 10_000),
            money(120_000 - 10_000),
        ),
        "topic-finansal-stok-028": check(
            money((100 * 20 + 100 * 30) / 200),
            money(100 * 20 + 100 * 30),
            money((100 * 20 + 100 * 30) / 200),
        ),
        "topic-finansal-stok-029": check(
            money(80 * 10 + 20 * 15),
            money(80 * 10 + 20 * 15),
        ),
        "topic-finansal-stok-030": check(
            money(((50 * 12 + 50 * 18) / 100) * 40),
            money((50 * 12 + 50 * 18) / 100),
            money(((50 * 12 + 50 * 18) / 100) * 40),
        ),
        "topic-finansal-stok-031": check(
            money(30_000 + 140_000 - 45_000),
            money(30_000 + 140_000 - 45_000),
        ),
        "topic-finansal-stok-032": check(
            money(200_000 - 12_000 - 8_000),
            money(200_000 - 12_000 - 8_000),
        ),
        "topic-finansal-stok-033": check(
            money(25_000 + 90_000 + 5_000),
            money(25_000 + 90_000 + 5_000),
        ),
        "topic-finansal-stok-034": check(
            money(4_000),
            money(4_000),
        ),
        "topic-finansal-stok-041": check(
            money(min(48_000, 52_000 - 3_000 - 4_000)),
            money(52_000 - 3_000 - 4_000),
        ),
        "topic-finansal-stok-042": check(
            money(70_000 - 62_000),
            money(70_000 - 62_000),
        ),
        "topic-finansal-stok-043": check(
            money(min(90_000, 85_000)),
            money(min(90_000, 85_000)),
        ),
        "topic-finansal-stok-060": check(
            f"Stok {money(40_000 - 2_000 - 3_000)}'ye indirilir ve "
            f"{money(36_000 - (40_000 - 2_000 - 3_000))} gider yazılır.",
            money(40_000 - 2_000 - 3_000),
            money(36_000 - (40_000 - 2_000 - 3_000)),
        ),

        # Dönem sonu işlemleri
        "topic-finansal-donem-006": check(
            money((210_000 - 30_000) / 6),
            money(210_000 - 30_000),
            money((210_000 - 30_000) / 6),
        ),
        "topic-finansal-donem-007": check(
            money((120_000 / 60_000) * 15_000),
            money((120_000 / 60_000) * 15_000),
        ),
        "topic-finansal-donem-013": check(
            f"{money(50_000 - 44_000)} kâr",
            money(50_000 - 44_000),
        ),
        "topic-finansal-donem-018": check(
            money((70 - 66) * 500),
            money((70 - 66) * 500),
        ),
        "topic-finansal-donem-022": check(
            money((48_000 / 12) * 3),
            money(48_000 / 12),
            money((48_000 / 12) * 3),
        ),
        "topic-finansal-donem-028": check(
            money(120_000 * 0.20 * 3 / 12),
            money(120_000 * 0.20 * 3 / 12),
        ),
        "topic-finansal-donem-039": check(
            f"{money((100_000 / 10) * 2)} ve {money((100_000 / 10) * 8)}",
            money(100_000 / 10),
            money((100_000 / 10) * 2),
            money((100_000 / 10) * 8),
        ),
        "topic-finansal-donem-040": check(
            f"{money(72_000 / 6)} ve {money((72_000 / 6) * 5)}",
            money(72_000 / 6),
            money((72_000 / 6) * 5),
        ),
        "topic-finansal-donem-044": check(
            money(min(55_000, 49_000)),
            money(min(55_000, 49_000)),
            money(55_000 - 49_000),
        ),
        "topic-finansal-donem-051": check(
            money(44_000 - 29_000),
            money(44_000 - 29_000),
        ),

        # TMS/TFRS uygulamaları
        "topic-finansal-tfrs-014": check(
            f"{(900_000 - 100_000) / 400_000:.2f}".replace(".", ",") + " TL",
            money(900_000 - 100_000),
            f"{(900_000 - 100_000) / 400_000:.2f}".replace(".", ",") + " TL",
        ),
        "topic-finansal-tfrs-016": check(
            money(max(750_000, 780_000)),
            money(max(750_000, 780_000)),
        ),
        "topic-finansal-tfrs-020": check(
            money(500_000 - 20_000),
            money(500_000 - 20_000),
        ),
        "topic-finansal-tfrs-021": check(
            money(1_200_000 + 200_000 - 1_100_000),
            f"{1_200_000 + 200_000:,.0f}".replace(",", "."),
            money(1_200_000 + 200_000 - 1_100_000),
        ),
        "topic-finansal-tfrs-051": check(
            money(1_000_000 * 0.25),
            money(1_000_000 * 0.25),
        ),
    }
    assert len(checks) == 33
    assert set(checks) <= ORIGINAL_AUDIT_IDS
    return checks


def load_questions() -> dict[str, dict]:
    result = {}
    for path in FILES:
        for question in json.loads(path.read_text(encoding="utf-8")):
            assert question["id"] not in result
            result[question["id"]] = question
    return result


def main() -> None:
    questions = load_questions()
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    missing = ORIGINAL_AUDIT_IDS - set(questions)
    assert not missing, f"Eksik sayısal vaka: {sorted(missing)}"

    for question_id in ORIGINAL_AUDIT_IDS:
        question = questions[question_id]
        actual = question["choices"][question["correctAnswer"]]
        assert actual == baseline[question_id], question_id

    checks = calculation_checks()
    for question_id, (expected_answer, fragments) in checks.items():
        question = questions[question_id]
        actual = question["choices"][question["correctAnswer"]]
        assert actual == expected_answer, (
            question_id,
            expected_answer,
            actual,
        )
        for fragment in fragments:
            assert fragment in question["explanation"], (
                question_id,
                fragment,
                question["explanation"],
            )

    contextual = ORIGINAL_AUDIT_IDS - set(checks)
    print(f"Önceki denetimdeki sayısal vaka: {len(ORIGINAL_AUDIT_IDS)}")
    print(f"Python formülüyle doğrulanan gerçek hesap: {len(checks)}")
    print(f"Doğru-metin baseline ile doğrulanan sayısal bağlam: {len(contextual)}")
    print("Aritmetik ve ara sonuç kontrolleri başarılı.")


if __name__ == "__main__":
    main()
