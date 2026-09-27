#!/usr/bin/env python3
"""SGS yakın-tekrar uyarıları için uzman incelemeli bakım yamaları.

Her kayıt, yalnız sayıları değiştirilmiş eski bir soruyu aynı kazanımı farklı
bir yönden ölçen soruya dönüştürür. ``--check`` yayımlanan içeriğin bu kaynakla
eşleştiğini doğrular; ``--write`` gerektiğinde yamaları yeniden uygular.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]

PATCHES = {
    "content/mali_tablolar_analizi/trend_analizi.json": {
        "mta-trend-gen-0038": {
            "stem": "İlgili yılda tutarı 900.000 ₺ ve trend yüzdesi %150 olan bir kalemin baz yıl tutarı kaç ₺'dir?",
            "options": {
                "A": "750.000",
                "B": "600.000",
                "C": "1.350.000",
                "D": "150.000",
                "E": "900.000",
            },
            "answer": "B",
            "solution": "Baz yıl tutarı = İlgili yıl tutarı ÷ (Trend yüzdesi/100) = 900.000 ÷ 1,50 = **600.000 ₺**.",
        },
        "mta-trend-gen-0057": {
            "stem": "Bir kalemin baz yıl tutarı 800.000 ₺, ilgili yıldaki tutarı 1.000.000 ₺'dir. İlgili yılın trend yüzdesi kaçtır?",
            "options": {
                "A": "%125",
                "B": "%80",
                "C": "%25",
                "D": "%120",
                "E": "%150",
            },
            "answer": "A",
            "solution": "Trend yüzdesi = 1.000.000 ÷ 800.000 × 100 = **%125**.",
        },
    },
    "content/maliyet_muhasebesi/standart_maliyet.json": {
        "mmuh-standart-gen-0017": {
            "stem": "Toplam direkt işçilik gideri sapması 6.200 ₺ aleyhte, standart direkt işçilik maliyeti 40.000 ₺'dir. Fiilî direkt işçilik maliyeti kaç ₺'dir?",
            "options": {"A": "46.200", "B": "33.800", "C": "40.000", "D": "6.200", "E": "53.200"},
            "answer": "A",
            "solution": "Aleyhte sapmada fiilî maliyet standart maliyetten yüksektir. Fiilî maliyet = 40.000 + 6.200 = **46.200 ₺**.",
        },
    },
    "content/denetim/denetim_riski.json": {
        "den-risk-gen-0031": {
            "stem": "Bir denetimde yapısal risk %100, kontrol riski %60 ve kabul edilebilir tespit riski %10'dur. Bu bileşenlere göre denetim riski yüzde kaçtır?",
            "options": {"A": "%6", "B": "%10", "C": "%16", "D": "%20", "E": "%60"},
            "answer": "A",
            "solution": "Denetim riski = Yapısal risk × Kontrol riski × Tespit riski = 1,00 × 0,60 × 0,10 = 0,06 = **%6**.",
        },
    },
}


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()

    mismatches: list[str] = []
    for relative_path, question_patches in PATCHES.items():
        path = ROOT / relative_path
        data = json.loads(path.read_text(encoding="utf-8"))
        questions = data["questions"] if isinstance(data, dict) else data
        by_id = {question["id"]: question for question in questions}
        for question_id, fields in question_patches.items():
            question = by_id.get(question_id)
            if question is None:
                raise SystemExit(f"Soru bulunamadı: {relative_path}::{question_id}")
            for field, expected in fields.items():
                if question.get(field) != expected:
                    mismatches.append(f"{relative_path}::{question_id}.{field}")
                    if args.write:
                        question[field] = expected
        if args.write:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if args.check and mismatches:
        print("Bakım builder'ıyla eşleşmeyen alanlar:")
        for mismatch in mismatches:
            print(f"- {mismatch}")
        return 1
    print(f"{len(PATCHES)} paket / {sum(map(len, PATCHES.values()))} soru doğrulandı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
