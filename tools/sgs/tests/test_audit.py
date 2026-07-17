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


def havuz(uzunluklar, answer_index):
    """Verilen karakter uzunluklarında 5 şıklı 30 soruluk havuz üretir.

    `answer_index`, doğru cevabın `uzunluklar` içindeki konumudur; şıklar
    A–E'ye sırayla dağıtılır, doğru harf her soruda kaydırılarak harf dizisi
    dengeli tutulur (harf örüntüsü dedektörünü tetiklememesi için).
    """
    questions = []
    for i in range(30):
        kaydir = i % 5
        metinler = uzunluklar[-kaydir:] + uzunluklar[:-kaydir] if kaydir else list(uzunluklar)
        yer = (answer_index + kaydir) % 5
        options = {harf: f"{'x' * metinler[j]} {i}" for j, harf in enumerate("ABCDE")}
        questions.append(soru(f"q{i}", f"{i}. soru kökü nedir?", options, answer="ABCDE"[yer]))
    return questions


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


class KorOgrenciTest(unittest.TestCase):
    """Şıkların içerikten bağımsız örüntü sızdırması — soru okumadan çözülebilirlik."""

    def test_dogru_hep_en_uzunsa_yakalanir(self):
        """Babanın en baştaki şikâyeti. Eski dedektör 1.5× eşiğinin altını kaçırıyordu."""
        # 150 ↔ 100: oran 1.5'in ALTINDA, yani eski dedektör bunu onaylardı.
        fatals = audit_et(havuz([150, 100, 100, 100, 100], answer_index=0))
        self.assertTrue(any("kör öğrenci" in f for f in fatals), fatals)

    def test_dogru_hep_en_kisaysa_da_yakalanir(self):
        """Ters yön de aynı derecede zararlı: 'en kısayı işaretle' de bir kuraldır."""
        fatals = audit_et(havuz([60, 100, 100, 100, 100], answer_index=0))
        self.assertTrue(any("kör öğrenci" in f for f in fatals), fatals)

    def test_boy_dengeliyse_temiz(self):
        """Doğru şık boy sıralamasında gezinirse örüntü yoktur — yanlış alarm olmamalı."""
        fatals = audit_et(havuz([140, 120, 100, 80, 60], answer_index=2))
        self.assertEqual([f for f in fatals if "kör öğrenci" in f], [])

    def test_dolgu_yalniz_celdiricideyse_yakalanir(self):
        """Dolgu kalıbı yalnız çeldiricilerde ise kalıp 'yanlış' işareti olur."""
        questions = []
        for i in range(30):
            yer = i % 5
            options = {}
            for j, harf in enumerate("ABCDE"):
                options[harf] = (f"{i}. doğru önerme burada yer alır" if j == yer
                                 else f"{i}-{j}. önerme her hâlde uygulanmak zorunda bulunmaktadır")
            questions.append(soru(f"q{i}", f"{i}. soru kökü nedir?", options, answer="ABCDE"[yer]))
        fatals = audit_et(questions)
        self.assertTrue(any("kör öğrenci" in f for f in fatals), fatals)

    def test_oncul_secicileri_atma_sikki_sayilmaz(self):
        """'Yalnız I', 'II ve III' meşru olarak tekrar eder — atma-şıkkı değildir."""
        questions = []
        for i in range(30):
            yer = i % 5
            metinler = ["I ve II", "I, II ve III", "Yalnız I", "II ve III", "I ve III"]
            options = {harf: metinler[j] for j, harf in enumerate("ABCDE")}
            questions.append(soru(f"q{i}", f"{i}. hangileri doğrudur?\n\nI. a\n\nII. b\n\nIII. c",
                                  options, answer="ABCDE"[yer]))
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
            json.dump(questions, fh, ensure_ascii=False)
            path = fh.name
        try:
            _, issues = audit.audit(path)
        finally:
            os.unlink(path)
        self.assertEqual([m for _, m in issues if "atma-şıkkı" in m], [])


if __name__ == "__main__":
    unittest.main()
