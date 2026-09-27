#!/usr/bin/env python3
"""SGS öncüllü soru örüntüsü için izlenebilir içerik düzeltmeleri.

Bu dosya yeni soru üretmez. Denetimde ``Yalnız I/II/III`` seçeneği bulunduğu
halde tek öncüllü doğru cevabı olmayan eski paketlerde, uzman incelemesiyle
seçilen soruları günceller. Her yama eski değeri de taşıdığı için yanlış dosyaya
veya daha sonra değişmiş içeriğe sessizce uygulanamaz.

Kullanım:
    python3 tools/sgs/builders/build_oncul_single_correct_cleanup.py --check
    python3 tools/sgs/builders/build_oncul_single_correct_cleanup.py --write

⚠️ SAHIPLIK DEVRI: maliye/kamu_maliyesi_temel.json bloku bu dosyadan CIKARILDI; sahiplik
build_maliye_temel_yeniden.py dosyasina gecti. Bir sorunun tek sahibi olmali.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]

PATCHES = {
    "content/mali_tablolar_analizi/fon_akim_analizi.json": {
        "mta-fon-gen-0020": {
            "stem": (
                "Aşağıdaki işlemlerden hangileri fon KULLANIMIdır?\n\n"
                "I. Ortaklara temettü ödenmesi\n\n"
                "II. Nakit sermaye artırımı\n\n"
                "III. Uzun vadeli borçlanma yoluyla nakit sağlanması"
            ),
            "answer": "A",
            "solution": (
                "**I (temettü ödemesi)** işletmeden fon çıkışına yol açtığı için "
                "fon kullanımıdır. **II (nakit sermaye artırımı)** ve **III (uzun "
                "vadeli borçlanma)** ise işletmeye fon sağlayan kaynaklardır. "
                "Doğru cevap **Yalnız I**."
            ),
        },
    },
}


def load_questions(path: Path) -> tuple[dict | list, list[dict]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    return data, questions


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()

    mismatches: list[str] = []
    for relative_path, question_patches in PATCHES.items():
        path = ROOT / relative_path
        data, questions = load_questions(path)
        by_id = {question["id"]: question for question in questions}

        for question_id, fields in question_patches.items():
            if question_id not in by_id:
                raise SystemExit(f"Soru bulunamadı: {relative_path}::{question_id}")
            question = by_id[question_id]
            for field, expected in fields.items():
                if question.get(field) != expected:
                    mismatches.append(f"{relative_path}::{question_id}.{field}")
                    if args.write:
                        question[field] = expected

        if args.write:
            path.write_text(
                json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

    if args.check and mismatches:
        print("Bakım builder'ıyla eşleşmeyen alanlar:")
        for mismatch in mismatches:
            print(f"- {mismatch}")
        return 1

    print(f"{len(PATCHES)} paket / {sum(map(len, PATCHES.values()))} soru doğrulandı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
