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


class CozumHarfiTest(unittest.TestCase):
    def test_cozum_harfi_cevapla_uyusmuyorsa_fatal(self):
        q = soru("q1", "Kök?", {"A": "a", "B": "b", "C": "c", "D": "d", "E": "e"}, answer="C")
        q["solution"] = "Gerekçe burada. Doğru cevap B."
        self.assertTrue(any("çözüm" in f for f in audit_et([q])), audit_et([q]))

    def test_cozum_harfi_uyusuyorsa_temiz(self):
        q = soru("q1", "Kök?", {"A": "a", "B": "b", "C": "c", "D": "d", "E": "e"}, answer="C")
        q["solution"] = "Gerekçe burada. Doğru cevap C."
        self.assertEqual([f for f in audit_et([q]) if "çözüm" in f], [])

    def test_kucuk_harfli_bu_kelimesi_cevap_harfi_sanilmaz(self):
        """`re.I` ile arayan bir regex 'Doğru seçenek bu…' içindeki b'yi B sanar."""
        q = soru("q1", "Kök?", {"A": "a", "B": "b", "C": "c", "D": "d", "E": "e"}, answer="C")
        q["solution"] = "Doğru seçenek bu nedenle kapanış kuruna dayanır."
        self.assertEqual([f for f in audit_et([q]) if "çözüm" in f], [])


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


class TekrarTest(unittest.TestCase):
    """Alıştırma ↔ klon ayrımı. Kural yalnız 'aynı şablon' derse matematiği yakar."""

    def sayisal(self, qid, a, b, cevap):
        return soru(qid, f"Baz yılda {a} ₺ olan kalem {b} ₺ olmuştur. Trend yüzdesi kaçtır?",
                    {"A": cevap, "B": "%90", "C": "%150", "D": "%75", "E": "%200"}, answer="A")

    def test_ayni_sablon_ayni_cevap_klondur(self):
        """600.000/500.000 ve 960.000/800.000 → ikisi de %120: aynı işlem, aynı sonuç."""
        fatals = audit_et([self.sayisal("q1", "500.000", "600.000", "%120"),
                           self.sayisal("q2", "800.000", "960.000", "%120")])
        self.assertTrue(any("aynı şablon VE aynı cevap" in f for f in fatals), fatals)

    def test_ayni_sablon_farkli_cevap_alistirmadir(self):
        """Mekanik beceride şablon tekrarı istenen şeydir — yakılmamalı."""
        fatals = audit_et([self.sayisal("q1", "500.000", "600.000", "%120"),
                           self.sayisal("q2", "200.000", "260.000", "%130")])
        self.assertEqual([f for f in fatals if "aynı şablon" in f], [])

    def test_ilk_soru_farkli_cevapliysa_sonraki_klonlar_kacmaz(self):
        """Şablon başına yalnız İLK soruyu tutan sürüm bu çifti kaçırıyordu.

        İskelet üçünde de aynı; ilki %120, sonraki İKİSİ %130. Yalnız ilke bakan
        bir dedektör 2↔3'ü hiç karşılaştırmaz. Klonu bu yamanın kendi assertion'ı
        buldu, denetim değil.
        """
        fatals = audit_et([self.sayisal("q1", "500.000", "600.000", "%120"),
                           self.sayisal("q2", "200.000", "260.000", "%130"),
                           self.sayisal("q3", "600.000", "780.000", "%130")])
        self.assertTrue(any("q3" in f and "q2" in f for f in fatals), fatals)

    def test_artis_ve_azalis_ayni_cevap_sayilmaz(self):
        """“%10” ile “−%10” farklı cevaplardır; biri artış, öteki azalış.

        `metin()` sözcük olmayan karakteri attığı için ikisini de “10” yapıyor
        ve 4 sahte klon üretiyordu. Cevap karşılaştırması işaretleri korumalı.
        """
        fatals = audit_et([self.sayisal("q1", "400.000", "440.000", "%10"),
                           self.sayisal("q2", "400.000", "360.000", "\u2212%10")])
        self.assertEqual([f for f in fatals if "aynı şablon" in f], [])

    def test_birebir_ayni_cozum_yakalanir(self):
        ortak = "Trend yüzdesi, cari dönem tutarının baz yıl tutarına bölünüp yüz ile çarpılmasıdır."
        a = self.sayisal("q1", "500.000", "600.000", "%120"); a["solution"] = ortak
        b = self.sayisal("q2", "200.000", "260.000", "%130"); b["solution"] = ortak
        self.assertTrue(any("birebir aynı" in f for f in audit_et([a, b])))


class GuncellikTest(unittest.TestCase):
    def test_ciplak_mevzuat_orani_cevapsa_uyari(self):
        q = soru("q1", "Türkiye'de teslim edilen mallarda KDV oranı yüzde kaçtır?",
                 {"A": "%20", "B": "%1", "C": "%10", "D": "%8", "E": "%18"}, answer="A")
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
            json.dump([q], fh, ensure_ascii=False)
            path = fh.name
        try:
            _, issues = audit.audit(path)
        finally:
            os.unlink(path)
        self.assertTrue(any("mevzuat oranı" in m for _, m in issues), issues)

    def test_turetilmis_oran_uyari_degildir(self):
        """'4 yıllık ömrün amortisman oranı %25' türetilmiştir; mevzuat değişse bayatlamaz."""
        q = soru("q1", "Faydalı ömrü 4 yıl olan bir varlığın yıllık amortisman oranı yüzde kaçtır?",
                 {"A": "%25", "B": "%10", "C": "%40", "D": "%50", "E": "%20"}, answer="A")
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
            json.dump([q], fh, ensure_ascii=False)
            path = fh.name
        try:
            _, issues = audit.audit(path)
        finally:
            os.unlink(path)
        self.assertEqual([m for _, m in issues if "mevzuat oranı" in m], [])

    def test_cari_oran_finansal_rasyodur_uyari_degildir(self):
        """“Cari oran” = current ratio; “hâlihazırda geçerli oran” değil.

        İlk sürüm bunu kalıba alıp Mali Tablolar Analizi'nin temel terimini
        10 kez mevzuat ihlali sandı.
        """
        q = soru("q1", "Cari oran aşağıdakilerden hangisiyle hesaplanır?",
                 {"A": "Dönen Varlıklar ÷ Kısa Vadeli Yabancı Kaynaklar",
                  "B": "Dönen Varlıklar ÷ Toplam Varlıklar", "C": "Öz Kaynaklar ÷ Toplam Varlıklar",
                  "D": "Net Satışlar ÷ Stoklar", "E": "Duran Varlıklar ÷ Öz Kaynaklar"}, answer="A")
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
            json.dump([q], fh, ensure_ascii=False)
            path = fh.name
        try:
            _, issues = audit.audit(path)
        finally:
            os.unlink(path)
        self.assertEqual([m for _, m in issues if "dönem/oran vermeden" in m], [])

    def test_yururlukteki_oran_uyaridir(self):
        q = soru("q1", "Bir teslimde yürürlükteki oran üzerinden hesaplanacak vergi nedir?",
                 {"A": "Katma Değer Vergisi", "B": "Damga Vergisi", "C": "Emlak Vergisi",
                  "D": "Motorlu Taşıtlar Vergisi", "E": "Veraset Vergisi"}, answer="A")
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
            json.dump([q], fh, ensure_ascii=False)
            path = fh.name
        try:
            _, issues = audit.audit(path)
        finally:
            os.unlink(path)
        self.assertTrue(any("dönem/oran vermeden" in m for _, m in issues), issues)

    def test_kokte_verilen_oran_uyari_degildir(self):
        """Oran kökte verilmişse ölçülen kayıttır; soru kendi içinde tutarlı kalır."""
        q = soru("q1", "5.000 ₺ + %20 KDV ile satılan malın toplam tutarı kaç ₺'dir?",
                 {"A": "6.000 ₺", "B": "5.000 ₺", "C": "5.200 ₺", "D": "4.000 ₺", "E": "6.500 ₺"},
                 answer="A")
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
            json.dump([q], fh, ensure_ascii=False)
            path = fh.name
        try:
            _, issues = audit.audit(path)
        finally:
            os.unlink(path)
        self.assertEqual([m for _, m in issues if "mevzuat oranı" in m], [])


if __name__ == "__main__":
    unittest.main()
