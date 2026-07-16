#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM audit.py için davranış testleri."""

import json
import importlib.util
import os
import random
import tempfile
import unittest


AUDIT_PATH = os.path.join(os.path.dirname(__file__), "..", "audit", "audit.py")
SPEC = importlib.util.spec_from_file_location("content_audit", AUDIT_PATH)
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


TOKENS = [
    "ambar",
    "envanter",
    "dönüştürme",
    "finansman",
    "değerleme",
    "raporlama",
    "mutabakat",
    "sınıflandırma",
    "karşılaştırma",
    "tahakkuk",
    "dönemsellik",
    "önemlilik",
    "ölçümleme",
    "sunumlama",
    "belgelendirme",
    "doğrulama",
    "gözdengeçirme",
    "yetkilendirme",
    "ilişkilendirme",
    "çözümleme",
]


def answer_letters():
    rng = random.Random(20260717)
    values = list("ABCDE") * 4
    while True:
        rng.shuffle(values)
        seq = "".join(values)
        if not any(issue[0] == "FATAL" for issue in audit.letter_pattern(seq)):
            return values[:]


def clean_pack():
    letters = answer_letters()
    result = []
    for index, token in enumerate(TOKENS):
        choices = {
            "A": f"{token} işleminin temel koşulunu açıklar",
            "B": f"{token} işleminde farklı bir kapsamı esas alır",
            "C": f"{token} işlemine bağlı ikinci ölçütü uygular",
            "D": f"{token} için alternatif değerlendirme yolunu seçer",
            "E": f"{token} sonucunu başka raporlama dönemine aktarır",
        }
        result.append({
            "id": f"quality-{index + 1:04d}",
            "lessonId": "finansal_muhasebe",
            "topicId": "temel_kavramlar",
            "question": (
                f"{token.capitalize()} sürecinde verilen koşullar birlikte değerlendirildiğinde "
                "uygulanması gereken işlem aşağıdakilerden hangisidir?"
            ),
            "choices": choices,
            "correctAnswer": letters[index],
            "explanation": (
                f"{token.capitalize()} sürecinde doğru uygulama, soruda verilen kapsam ve "
                f"dönem koşullarının birlikte değerlendirilmesine dayanır; {token} ölçütü "
                "diğer seçeneklerdeki farklı varsayımları dışarıda bırakır."
            ),
            "source": {
                "kind": "generated",
                "legislationRef": f"TMS Kavramsal Çerçeve, {token} ilkesi",
            },
            "tags": ["Özgün Soru", "2026 Formatı", "Konu Havuzu"],
            "examPeriod": "2026 test sistemine uyumlu özgün soru",
            "legislationVersion": "2026 KGK seti",
            "sourceUpdatedAt": "2026-07-17T00:00:00Z",
        })
    return result


def run_audit(items):
    path = None
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as handle:
            json.dump(items, handle, ensure_ascii=False)
            path = handle.name
        return audit.audit(path)[2]
    finally:
        if path and os.path.exists(path):
            os.unlink(path)


class AuditTest(unittest.TestCase):
    def test_clean_pack_has_no_fatal(self):
        issues = run_audit(clean_pack())
        self.assertFalse([issue for issue in issues if issue[0] == "FATAL"], issues)

    def test_systematic_short_correct_answer_is_fatal(self):
        items = clean_pack()
        for item in items:
            answer = item["correctAnswer"]
            item["choices"][answer] = "Kısa doğru ifade"
            for key in "ABCDE":
                if key != answer:
                    item["choices"][key] += " ve adayın değerlendirmesi gereken ek ayrıntılı koşulları içerir"
        issues = run_audit(items)
        self.assertTrue(
            any(level == "FATAL" and code == "cevap-uzunluk" for level, code, _ in issues),
            issues,
        )

    def test_repeated_solution_is_fatal(self):
        items = clean_pack()
        items[1]["explanation"] = items[0]["explanation"]
        issues = run_audit(items)
        self.assertTrue(
            any(level == "FATAL" and code == "çözüm-tekrarı" for level, code, _ in issues),
            issues,
        )

    def test_number_only_question_variant_is_fatal(self):
        items = clean_pack()
        items[0]["question"] = "Bir işletmede 100 birim stok varsa dönem sonu ölçümü hangisidir?"
        items[1]["question"] = "Bir işletmede 250 birim stok varsa dönem sonu ölçümü hangisidir?"
        items[0]["choices"] = {
            "A": "100 birim üzerinden ölçülür",
            "B": "90 birim üzerinden ölçülür",
            "C": "80 birim üzerinden ölçülür",
            "D": "70 birim üzerinden ölçülür",
            "E": "60 birim üzerinden ölçülür",
        }
        items[1]["choices"] = {
            "A": "250 birim üzerinden ölçülür",
            "B": "225 birim üzerinden ölçülür",
            "C": "200 birim üzerinden ölçülür",
            "D": "175 birim üzerinden ölçülür",
            "E": "150 birim üzerinden ölçülür",
        }
        issues = run_audit(items)
        self.assertTrue(
            any(level == "FATAL" and code == "soru-şablonu" for level, code, _ in issues),
            issues,
        )

    def test_visible_demo_text_is_fatal(self):
        items = clean_pack()
        items[0]["question"] = "Demo Soru: " + items[0]["question"]
        issues = run_audit(items)
        self.assertTrue(
            any(level == "FATAL" and code == "görünür-demo" for level, code, _ in issues),
            issues,
        )

    def test_periodic_answer_key_is_fatal(self):
        items = clean_pack()
        for index, item in enumerate(items):
            item["correctAnswer"] = "ABCDE"[index % 5]
        issues = run_audit(items)
        self.assertTrue(
            any(level == "FATAL" and code == "harf-örüntü" for level, code, _ in issues),
            issues,
        )


if __name__ == "__main__":
    unittest.main()
