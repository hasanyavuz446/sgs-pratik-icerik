#!/usr/bin/env python3
"""SGS seçenek kalitesi için uzman incelemeli bakım yamaları.

Bu yamalar doğru cevap, kök ve çözümü değiştirmez. Tekrarlanan yapay
çeldiricileri bağlama özgü seçeneklerle değiştirir; ayrıca bir pakette
``en uzun``/``en kısa`` seçeneğin sistematik biçimde doğru olmasını engeller.
``--check`` iki repodaki yayımlanan kopyaların bu kaynakla eşleştiğini sınar.

⚠️ SAHIPLIK DEVRI (2026-08-14): meslek_hukuku/sorumluluk_ve_yasaklar.json blogu
bu dosyadan CIKARILDI. O paketin 60 sorusunun tamami yapisal kalibrasyon turunda
yeniden yazildi ve sahiplik build_hukuk_meslek_sorumluluk_yapisal.py dosyasina
gecti. Bir sorunun tek sahibi olmali.

⚠️ SAHIPLIK DEVRI (2026-08-14): ticaret_hukuku/kiymetli_evrak.json blogu bu
dosyadan CIKARILDI; sahiplik build_hukuk_kiymetli_evrak_yapisal.py'ye gecti.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"


PATCHES: dict[str, dict[str, dict[str, str]]] = {
    "content/maliyet_muhasebesi/maliyet_hacim_kar.json": {
        "mmuh-mhk-gen-0011": {"C": "Birim katkı payı ÷ sabit maliyet"},
    },
    "content/denetim/denetim_kaniti.json": {
        "den-kanit-gen-0041": {
            "A": "Analitik prosedür (tutarın geçmiş dönem eğilimi ve önceki yıl tutarıyla karşılaştırılması)"
        },
    },
    "content/denetim/denetim_ornekleme.json": {
        "den-ornek-gen-0021": {
            "B": "Kütlenin tabakalanması (benzer birimlere göre alt gruplara ayrılması ve ayrı değerlendirilmesi)"
        },
        "den-ornek-gen-0053": {
            "C": "Çalışma kâğıtlarının kamuoyuna eksiksiz açıklanmasını ve herkesçe erişilebilir olmasını sağlamak"
        },
    },
}


def load_questions(path: Path) -> tuple[object, list[dict]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data, data["questions"] if isinstance(data, dict) else data


def apply_or_check(path: Path, patches: dict[str, dict[str, str]], write: bool) -> list[str]:
    data, questions = load_questions(path)
    by_id = {question["id"]: question for question in questions}
    mismatches: list[str] = []
    for question_id, option_patches in patches.items():
        question = by_id.get(question_id)
        if question is None:
            raise SystemExit(f"Soru bulunamadı: {path}::{question_id}")
        for letter, expected in option_patches.items():
            if letter == question["answer"]:
                raise SystemExit(f"Doğru seçeneğe dokunulamaz: {path}::{question_id}.{letter}")
            if question["options"].get(letter) != expected:
                mismatches.append(f"{path}::{question_id}.{letter}")
                if write:
                    question["options"][letter] = expected
        if len(set(question["options"].values())) != 5:
            raise SystemExit(f"Seçenek çakışması: {path}::{question_id}")
    if write:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return mismatches


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()

    mismatches: list[str] = []
    for relative_path, patches in PATCHES.items():
        content_path = ROOT / relative_path
        app_path = APP_ROOT / relative_path
        mismatches.extend(apply_or_check(content_path, patches, args.write))
        mismatches.extend(apply_or_check(app_path, patches, args.write))
    if args.check and mismatches:
        print("Bakım builder'ıyla eşleşmeyen alanlar:")
        for mismatch in mismatches:
            print(f"- {mismatch}")
        return 1
    count = sum(len(options) for questions in PATCHES.values() for options in questions.values())
    print(f"{len(PATCHES)} paket / {count} seçenek iki repoda doğrulandı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
