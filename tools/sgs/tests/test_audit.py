#!/usr/bin/env python3
import importlib.util
import json
import os
import tempfile
import unittest


AUDIT_PATH = os.path.join(os.path.dirname(__file__), "..", "audit.py")
SPEC = importlib.util.spec_from_file_location("sgs_audit", AUDIT_PATH)
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)

GENEL_KOK = "Aşağıdakilerden hangisi muhasebenin temel kavramlarından biri değildir?"


def soru(qid, stem, options, answer="A"):
    return {
        "id": qid,
        "ders": "finansal_muhasebe",
        "konu": "muhasebenin_temel_kavramlari",
        "stem": stem,
        "options": options,
        "answer": answer,
        "solution": f"Gerekçe. Doğru cevap {answer}.",
    }


def audit_et(questions):
    """Geçici dosyaya yazıp audit'i çalıştırır, FATAL listesini döndürür."""
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
        json.dump(questions, fh, ensure_ascii=False)
        path = fh.name
    try:
        _, issues = audit.audit(path)
        return [msg for level, msg in issues if level == "FATAL"]
    finally:
        os.unlink(path)


class SgsAuditTest(unittest.TestCase):
    def test_short_nonperiodic_sequence_is_allowed(self):
        self.assertFalse(audit.letter_pattern("ABCDEBACDE"))

    def test_repeating_sequence_is_rejected(self):
        self.assertTrue(audit.letter_pattern("ABCDEABCDEABCDE"))

    def test_ayni_kok_farkli_siklar_kopya_sayilmaz(self):
        """Genel kök farklı şıklarla meşru olarak tekrar eder — 43 sahte FATAL'ın kaynağı."""
        fatals = audit_et([
            soru("q1", GENEL_KOK, {"A": "Tarafsızlık", "B": "Sosyal Sorumluluk",
                                   "C": "Parayla Ölçülme", "D": "Vergiye mutlak uygunluk",
                                   "E": "İhtiyatlılık"}, answer="D"),
            soru("q2", GENEL_KOK, {"A": "Tam Açıklama", "B": "Gizlilik", "C": "Özün Önceliği",
                                   "D": "Tutarlılık", "E": "Önemlilik"}, answer="B"),
        ])
        self.assertEqual([f for f in fatals if "yinelenen soru" in f], [])

    def test_ayni_kok_ayni_siklar_kopya_sayilir(self):
        """Gerçek kopya hâlâ yakalanmalı."""
        secenekler = {"A": "Tam Açıklama", "B": "Gizlilik", "C": "Özün Önceliği",
                      "D": "Tutarlılık", "E": "Önemlilik"}
        fatals = audit_et([
            soru("q1", GENEL_KOK, dict(secenekler), answer="B"),
            soru("q2", GENEL_KOK, dict(secenekler), answer="B"),
        ])
        self.assertTrue(any("yinelenen soru" in f and "q2" in f for f in fatals), fatals)

    def test_siklari_permute_edilmis_kopya_yakalanir(self):
        """Aynı şıklar harf sırası değiştirilerek çoğaltılmışsa yine kopyadır."""
        fatals = audit_et([
            soru("q1", GENEL_KOK, {"A": "Tam Açıklama", "B": "Gizlilik", "C": "Özün Önceliği",
                                   "D": "Tutarlılık", "E": "Önemlilik"}, answer="B"),
            soru("q2", GENEL_KOK, {"A": "Gizlilik", "B": "Tam Açıklama", "C": "Tutarlılık",
                                   "D": "Özün Önceliği", "E": "Önemlilik"}, answer="A"),
        ])
        self.assertTrue(any("yinelenen soru" in f and "q2" in f for f in fatals), fatals)


if __name__ == "__main__":
    unittest.main()
