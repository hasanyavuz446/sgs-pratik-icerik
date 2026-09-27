#!/usr/bin/env python3
"""SGS hukuk ve mevzuat paketlerindeki tek-doğru-öncül yamaları.

Seçilen sorular 22.07.2026 tarihinde resmî/kurumsal kaynaklarla (Adalet
Bakanlığı TBK metni, Ticaret Bakanlığı TTK metni, TÜRMOB düzenlemeleri, ÇSGB,
SGK ve GİB mevzuat sayfaları) yeniden kontrol edilmiştir.

⚠️ SAHIPLIK DEVRI (2026-08-14): content/meslek_hukuku/mesleki_degerler_etik.json,
meslek_hukuku_esaslari.json ve meslek_orgutu_disiplin.json bloklari bu dosyadan
CIKARILDI. Uc paketin de 60 sorusunun tamami yapisal kalibrasyon turunda
yeniden yazildi ve sahiplik ilgili build_hukuk_meslek_*_yapisal.py dosyalarina
gecti. Bir sorunun tek sahibi olmali.

⚠️ SAHIPLIK DEVRI (2026-08-14): meslek_hukuku/sorumluluk_ve_yasaklar.json blogu
bu dosyadan CIKARILDI. O paketin 60 sorusunun tamami yapisal kalibrasyon turunda
yeniden yazildi ve sahiplik build_hukuk_meslek_sorumluluk_yapisal.py dosyasina
gecti. Bir sorunun tek sahibi olmali.

⚠️ SAHIPLIK DEVRI (2026-08-14): meslek_hukuku/staj_ve_sinavlar.json blogu bu
dosyadan CIKARILDI; sahiplik build_hukuk_meslek_staj_yapisal.py'ye gecti.

⚠️ SAHIPLIK DEVRI (2026-08-14): ticaret_hukuku/kiymetli_evrak.json blogu bu
dosyadan CIKARILDI; sahiplik build_hukuk_kiymetli_evrak_yapisal.py'ye gecti.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def p(stem: str, answer: str, solution: str) -> dict[str, str]:
    return {"stem": stem, "answer": answer, "solution": solution}


PATCHES = {
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
