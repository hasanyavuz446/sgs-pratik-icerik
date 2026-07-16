#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Finansal Stoklar paketindeki şık ve öncül dağılımını deterministik düzeltir."""
from __future__ import annotations

import json
from pathlib import Path

from fix_finansal_topic_quality import BASELINE, PREMISES


ROOT = Path(__file__).resolve().parents[3]
FILENAME = "questions_topic_finansal_stoklar_2026.json"
TARGETS = [
    ROOT / "content/yeterlilik" / FILENAME,
    ROOT.parent / "smmm_sgs_pratik/assets/content/yeterlilik" / FILENAME,
]


# Doğru metne dokunmadan iki doğal, fakat yanlış seçeneği aynı ayrıntı
# düzeyine getirir. Böylece doğru cevap sistematik biçimde tek en uzun kalmaz.
DISTRACTOR_REWRITES = {
    "topic-finansal-stok-002": [
        ("Maliyet ve kullanım değeri", "Maliyet ile işletmeye özgü kullanım değerinden düşük olanı"),
        ("Satış fiyatı ve gerçeğe uygun değer", "Satış fiyatı ile gerçeğe uygun değerden düşük olanı"),
    ],
    "topic-finansal-stok-004": [
        ("Gerçeğe uygun değer işletmenin kendi tahmin ettiği satış tutarıdır.", "Net gerçekleşebilir değer piyasa katılımcılarının, gerçeğe uygun değer ise yalnız işletme yönetiminin tahminine dayanır."),
        ("Net gerçekleşebilir değer yalnız duran varlıklarda kullanılır.", "Net gerçekleşebilir değer yalnız duran varlıklarda, gerçeğe uygun değer ise yalnız stoklarda kullanılan ölçüdür."),
    ],
    "topic-finansal-stok-005": [
        ("Üretim maliyetleri ile genel yönetim giderlerinin tamamı", "Üretim maliyetleri ile stok satıldıktan sonra ortaya çıkan pazarlama ve genel yönetim giderlerinin tamamı"),
        ("Satın alma fiyatı ile finansman giderlerinin tamamı", "Satın alma bedeli, olağan kredi süresini aşan finansman unsuru ve işletmenin bütün dönem giderleri"),
    ],
    "topic-finansal-stok-008": [
        (("Daima finansman gideri olur.", "Olağan finansman gideri sayılarak ödeme süresince faiz hesabında izlenir."), "Doğrudan finansman gideri sayılır."),
        (("Satış gideri olarak kaydedilir.", "Stokla ilişkisiz satış ve pazarlama gideri olarak doğrudan dönem sonucuna aktarılır.", "Satış ve pazarlama gideri yazılır."), "Satış ve pazarlama giderine kaydedilir."),
    ],
    "topic-finansal-stok-009": [
        ("Gelecek yıllara ait gider olarak bekletilir.", "Anormal kayıp tutarı gelecek dönemlere ait gider kabul edilerek aktifte bekletilir."),
        ("Mamul maliyetine sınırsız biçimde yüklenir.", "Anormal kaybın tamamı normal üretim maliyeti sayılarak satılıncaya kadar stokta izlenir."),
    ],
    "topic-finansal-stok-010": [
        ("Her durumda stok maliyetidir.", "Üretimin sonraki aşaması için zorunlu olmasa da her durumda stok maliyetine eklenir."),
        ("Net gerçekleşebilir değere eklenir.", "Depolama gideri stokun net gerçekleşebilir değerine eklenerek değer düşüklüğünü azaltır."),
    ],
    "topic-finansal-stok-014": [
        ("Genel yönetim gideri", "Genel yönetim personeli gideri"),
        ("Satış gideri", "Pazarlama ve satış personeli gideri"),
    ],
    "topic-finansal-stok-015": [
        ("Yalnız fiilî düşük üretim", "Dönemde gerçekleşen düşük üretim düzeyi ve kullanılmayan kapasite toplamı"),
        ("Azami teorik kapasite", "Hiç duruş yaşanmadığı varsayımıyla hesaplanan azami teorik üretim kapasitesi"),
    ],
    "topic-finansal-stok-017": [
        ("Sabit giderlerin tamamı öz kaynağa alınır.", "Olağan dışı yüksek üretimin yarattığı farkın tamamı doğrudan özkaynak hesaplarında izlenir."),
        ("Bütün sabit giderler dönem gideri yapılır.", "Üretim düzeyine bakılmadan sabit genel üretim giderlerinin tamamı dönem gideri yapılır."),
    ],
    "topic-finansal-stok-021": [
        (("Hareketli ortalama zorunluluğu", "Birbirleriyle ikame edilmeyen bütün kalemlerde hareketli ağırlıklı ortalama zorunluluğu", "Hareketli ağırlıklı ortalama yöntemi"), "Hareketli ağırlıklı ortalama maliyet yöntemi"),
        (("Yalnız perakende yöntemi", "Özel projeye ayrılmış stoklarda yalnız perakende satış fiyatı yönteminin uygulanması"), "Perakende satış fiyatı yöntemi"),
    ],
    "topic-finansal-stok-022": [
        ("En pahalı stokun önce satıldığı", "Satın alma tarihine bakılmadan birim maliyeti en yüksek stok kaleminin önce satıldığı"),
        ("Son alınan stokların önce satıldığı", "Dönem içinde en son alınan veya üretilen stok kalemlerinin önce satışa konu edildiği"),
    ],
}


def set_premise(question: dict, replacement: dict) -> None:
    answer = question["correctAnswer"]
    question["question"] = replacement["question"]
    question["explanation"] = replacement["explanation"]
    choices = {answer: replacement["correct"]}
    other_letters = [letter for letter in "ABCDE" if letter != answer]
    choices.update(dict(zip(other_letters, replacement["distractors"])))
    question["choices"] = choices


def main() -> None:
    questions = json.loads(TARGETS[0].read_text(encoding="utf-8"))
    by_id = {question["id"]: question for question in questions}

    for question_id, replacements in DISTRACTOR_REWRITES.items():
        question = by_id[question_id]
        for old, new in replacements:
            if new in question["choices"].values():
                continue
            accepted = (old,) if isinstance(old, str) else old
            assert question["choices"][question["correctAnswer"]] not in accepted
            letters = [letter for letter, value in question["choices"].items() if value in accepted]
            assert len(letters) == 1, (question_id, old)
            question["choices"][letters[0]] = new

    # Mekanik uzatma kalıntısı yerine kısa ve makul FOB çeldiricileri kullanılır.
    fob = by_id["topic-finansal-stok-037"]
    fob["choices"] = {
        "A": "Hiçbir tarafa",
        "B": "Alıcıya, çünkü kontrol 29 Aralık'ta geçmiştir.",
        "C": "Taşıyıcıya",
        "D": "Alıcı ile satıcıya eşit paylarla",
        "E": "Satıcıya, çünkü fiziksel teslim ancak 3 Ocak tarihinde yapılmıştır.",
    }
    assert fob["correctAnswer"] == "B"

    for question_id in ("topic-finansal-stok-012", "topic-finansal-stok-018"):
        set_premise(by_id[question_id], PREMISES[question_id])

    # Doğru seçenek baseline'ı, öncül kombinasyonu değişen iki soru için güncellenir.
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    for question_id in ("topic-finansal-stok-012", "topic-finansal-stok-018"):
        question = by_id[question_id]
        baseline[question_id] = question["choices"][question["correctAnswer"]]
    BASELINE.write_text(json.dumps(baseline, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    payload = json.dumps(questions, ensure_ascii=False, indent=2) + "\n"
    for target in TARGETS:
        target.write_text(payload, encoding="utf-8")
        print(f"yazıldı: {target} ({len(questions)} soru)")


if __name__ == "__main__":
    main()
