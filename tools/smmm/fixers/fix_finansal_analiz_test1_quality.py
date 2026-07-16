#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Finansal Tablolar ve Analizi birinci bölüm testinin 17 sorusunu temizler.

İlk testin ücretsiz paketteki 3 soruyu izleyen 17 sorusu bu dosyadadır. Script:
- ortak tablodaki verilerden doğru sonuçları Decimal ile yeniden hesaplar,
- dikey, trend ve karşılaştırmalı analiz sorularını doğru alt konuya taşır,
- her soruya formül düzeyinde kaynak ve gerçek 2026 kontrol sürümü ekler,
- bölüm/konu havuzu ayrımını etiketlerde açıkça korur,
- içerik ile uygulama kopyasını özdeş yazar.
"""
from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTENT_PATH = (
    ROOT / "content" / "yeterlilik" / "questions_finansal_analiz_2026.json"
)
STIMULI_PATH = ROOT / "content" / "yeterlilik" / "stimuli.json"
DEMO_PATH = ROOT / "content" / "yeterlilik" / "demo_questions.json"
APP_PATH = (
    ROOT.parent
    / "smmm_sgs_pratik"
    / "assets"
    / "content"
    / "yeterlilik"
    / "questions_finansal_analiz_2026.json"
)

UPDATED_AT = "2026-07-17T00:00:00Z"
LEGISLATION_VERSION = (
    "TESMER 2026 Staj ve Sınavlara İlişkin Uygulama Yönergesi §13.1-13.2; "
    "KGK TFRS 2026 Seti (Mavi Kitap)"
)

D = Decimal
DATA = {
    2024: {"toplam": D("1200"), "satis": D("800")},
    2025: {
        "toplam": D("1400"),
        "satis": D("1000"),
    },
    2026: {
        "hazir": D("120"),
        "alacak": D("240"),
        "stok": D("240"),
        "diger_dv": D("120"),
        "dv": D("720"),
        "duran": D("880"),
        "toplam": D("1600"),
        "kvyk": D("480"),
        "uvyk": D("320"),
        "ozkaynak": D("800"),
        "satis": D("1200"),
        "smm": D("840"),
        "brut": D("360"),
        "net_kar": D("120"),
    },
}

SOURCE_REFS = {
    "demo-analiz-004": "Finansal tablo analizi — Net işletme sermayesi = Dönen varlıklar − KVYK",
    "demo-analiz-005": "Finansal tablo analizi — Cari oran = Dönen varlıklar / KVYK",
    "demo-analiz-006": "Finansal tablo analizi — Asit-test oranı = (Dönen varlıklar − Stoklar) / KVYK",
    "demo-analiz-007": "Finansal tablo analizi — Nakit oranı = Hazır değerler / KVYK",
    "demo-analiz-008": "Finansal tablo analizi — Yabancı kaynak oranı = Toplam yabancı kaynaklar / Toplam varlıklar",
    "demo-analiz-009": "Finansal tablo analizi — Özkaynak oranı = Özkaynaklar / Toplam varlıklar",
    "demo-analiz-010": "Finansal tablo analizi — Net kâr marjı = Dönem net kârı / Net satışlar",
    "demo-analiz-011": "Finansal tablo analizi — Brüt satış kârlılığı = Brüt satış kârı / Net satışlar",
    "demo-analiz-012": "Finansal tablo analizi — Varlık devir hızı = Net satışlar / Ortalama toplam varlıklar",
    "demo-analiz-013": "Finansal tablo analizi — Ticari alacak devir hızı = Kredili net satışlar / Ortalama ticari alacaklar",
    "demo-analiz-014": "Finansal tablo analizi — Ortalama tahsil süresi = 360 / Ticari alacak devir hızı",
    "demo-analiz-015": "Finansal tablo analizi — Stok devir hızı = Satışların maliyeti / Ortalama stok",
    "demo-analiz-016": "Finansal tablo analizi — Ortalama stokta kalma süresi = 360 / Stok devir hızı",
    "demo-analiz-017": "Dikey analiz — Kalemin grup toplamı içindeki yüzde payı",
    "demo-analiz-018": "Trend analizi — İncelenen dönem / Baz dönem × 100",
    "demo-analiz-019": "Karşılaştırmalı analiz — (Cari dönem − Önceki dönem) / Önceki dönem × 100",
    "demo-analiz-020": "Finansal tablo analizi — Hedef dönen varlıklar = Hedef cari oran × KVYK",
}

TOPIC_OVERRIDES = {
    "demo-analiz-017": "dikey_analiz",
    "demo-analiz-018": "trend_analizi",
    "demo-analiz-019": "karsilastirmali_analiz",
}


def expected_results() -> dict[str, Decimal]:
    a, b, c = DATA[2024], DATA[2025], DATA[2026]
    alacak_ortalama = D("200")
    stok_ortalama = D("210")
    alacak_devir = c["satis"] / alacak_ortalama
    stok_devir = c["smm"] / stok_ortalama
    return {
        "demo-analiz-004": c["dv"] - c["kvyk"],
        "demo-analiz-005": c["dv"] / c["kvyk"],
        "demo-analiz-006": (c["dv"] - c["stok"]) / c["kvyk"],
        "demo-analiz-007": c["hazir"] / c["kvyk"],
        "demo-analiz-008": (c["kvyk"] + c["uvyk"]) / c["toplam"] * 100,
        "demo-analiz-009": c["ozkaynak"] / c["toplam"] * 100,
        "demo-analiz-010": c["net_kar"] / c["satis"] * 100,
        "demo-analiz-011": c["brut"] / c["satis"] * 100,
        "demo-analiz-012": c["satis"] / ((b["toplam"] + c["toplam"]) / 2),
        "demo-analiz-013": alacak_devir,
        "demo-analiz-014": D("360") / alacak_devir,
        "demo-analiz-015": stok_devir,
        "demo-analiz-016": D("360") / stok_devir,
        "demo-analiz-017": c["stok"] / c["dv"] * 100,
        "demo-analiz-018": c["satis"] / a["satis"] * 100,
        "demo-analiz-019": (c["satis"] - b["satis"]) / b["satis"] * 100,
        "demo-analiz-020": c["kvyk"] * D("1.80") - c["dv"],
    }


def parse_tr_number(value: str) -> Decimal:
    return D(value.replace(".", "").replace(",", "."))


def validate_stimulus() -> None:
    stimuli = json.loads(STIMULI_PATH.read_text(encoding="utf-8"))
    stimulus = next(
        item for item in stimuli if item["id"] == "demo-analiz-kapsamli-001"
    )
    body = stimulus["bodyMarkdown"]
    required = (
        "| Kalem (bin TL) | 2024 | 2025 | 2026 |",
        "| Dönen Varlıklar | 500 | 600 | 720 |",
        "| Toplam Varlıklar | 1.200 | 1.400 | 1.600 |",
        "| Kısa Vadeli Yabancı Kaynaklar | 400 | 450 | 480 |",
        "| Net Satışlar | 800 | 1.000 | 1.200 |",
        "| Satışların Maliyeti | 560 | 700 | 840 |",
    )
    assert all(fragment in body for fragment in required)
    assert "ortalama ticari alacakları 200 bin TL" in stimulus["caption"]
    assert "ortalama stokları 210 bin TL" in stimulus["caption"]
    assert "bir yıl 360 gündür" in stimulus["caption"]


def rebuild() -> list[dict]:
    validate_stimulus()
    items = json.loads(CONTENT_PATH.read_text(encoding="utf-8"))
    results = expected_results()
    assert len(items) == 17
    assert set(SOURCE_REFS) == set(results) == {item["id"] for item in items}

    c = DATA[2026]
    assert c["hazir"] + c["alacak"] + c["stok"] + c["diger_dv"] == c["dv"]
    assert c["dv"] + c["duran"] == c["toplam"]
    assert c["kvyk"] + c["uvyk"] + c["ozkaynak"] == c["toplam"]
    assert c["satis"] - c["smm"] == c["brut"]

    for item in items:
        answer_text = item["choices"][item["correctAnswer"]]
        actual = parse_tr_number(answer_text)
        expected = results[item["id"]]
        if item["id"] == "demo-analiz-017":
            expected = expected.quantize(D("0.01"))
        assert actual == expected, (item["id"], actual, expected)

        item["lessonId"] = "mali_tablolar_analizi"
        item["topicId"] = TOPIC_OVERRIDES.get(item["id"], "oran_analizi")
        item["source"] = {
            "kind": "generated",
            "styleRef": "2026/1 beş seçenekli test biçimi",
            "legislationRef": SOURCE_REFS[item["id"]],
        }
        item["tags"] = [
            "Özgün Soru",
            "2026 Formatı",
            "Bölüm Havuzu",
            "Finansal Tablolar ve Analizi",
        ]
        item["updatedAt"] = UPDATED_AT
        item["examPeriod"] = "2026 test sistemine uyumlu özgün soru"
        item["legislationVersion"] = LEGISLATION_VERSION
        item["sourceUpdatedAt"] = UPDATED_AT
        item["isActive"] = True

    assert all("demo" not in item["question"].casefold() for item in items)
    assert all("demo" not in item["explanation"].casefold() for item in items)
    assert all("Demo Soru" not in item["tags"] for item in items)

    demo_items = json.loads(DEMO_PATH.read_text(encoding="utf-8"))
    first_test_ids = {
        item["id"]
        for item in demo_items + items
        if item["id"].startswith("demo-analiz-")
        and item["id"] != "demo-analiz-kapsamli-001"
    }
    assert first_test_ids == {f"demo-analiz-{number:03d}" for number in range(1, 21)}
    return items


def write(path: Path, data: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    items = rebuild()
    write(CONTENT_PATH, items)
    write(APP_PATH, items)
    print(
        f"questions_finansal_analiz_2026.json: {len(items)} soru | "
        "17/17 hesap doğrulandı | 3 + 17 = 20 soruluk ilk test"
    )


if __name__ == "__main__":
    main()
