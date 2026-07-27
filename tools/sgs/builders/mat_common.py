#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SGS matematik konu üreticileri için ortak çatı.

İki yeni ileri matematik konusu (`build_mat_fonksiyon_analitik.py` ve
`build_mat_limit_turev_seri.py`) bu modülü kullanır.

Tasarım kararları (URETIM_KURALLARI):
  §3  JSON elle yazılmaz; paket bu builder'dan üretilir, `--check` ile doğrulanır.
  §5  Doğru cevabın harfi hedef diziden gelir; dizi harf başına eşit ve üçlü
      tekrarsızdır. Şıklar artan sıraya DİZİLMEZ — mevcut üç matematik paketinin
      ev üslubu budur (60/60'ı sıralanmamış, dağılım 12/12/12/12/12). Karışık
      Test'te iki farklı şık düzeni yan yana gelmesin diye aynısı sürdürülür.
  §8  Her sayısal sonuç sympy ile builder'dan BAĞIMSIZ ikinci kez doğrulanır.
      sympy yoksa `--write` çalışmaz; sessizce atlanmaz.
"""
from __future__ import annotations

import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"

try:
    import sympy as sp
except ModuleNotFoundError:  # pragma: no cover
    sp = None


def make_q(store):
    """Soru ekleyen ve eklerken doğrulayan bir `q` işlevi döndürür."""

    def q(stem, correct, distractors, sol, verify=None):
        assert len(distractors) == 4, stem[:50]
        options = [correct] + list(distractors)
        assert len(set(options)) == 5, ("çakışan şık", stem[:50])
        if verify is not None:
            if sp is None:
                raise SystemExit(
                    "sympy kurulu değil; §8 bağımsız doğrulaması yapılamadan paket "
                    "üretilemez. Kurulum: pip3 install sympy"
                )
            got, expected = (sp.sympify(v) for v in verify)
            if got.is_infinite or expected.is_infinite or got in (sp.true, sp.false):
                ok = got == expected  # ∞ − ∞ = nan; sonsuzda doğrudan eşitlik aranır
            else:
                ok = sp.simplify(sp.nsimplify(got) - sp.nsimplify(expected)) == 0
            assert ok, ("DOĞRULAMA", stem[:50], got, expected)
        store.append(
            {"stem": stem, "correct": correct, "distractors": list(distractors), "sol": sol}
        )

    return q


def letter_pattern(sequence: str) -> bool:
    """audit.py ile aynı ölçüt: sabit adımlı harf örüntüsü var mı?"""
    letters = "ABCDE"
    for step in range(1, 5):
        expected = "".join(letters[(letters.index(sequence[0]) + i * step) % 5]
                           for i in range(len(sequence)))
        if sequence == expected:
            return True
    return False


def targets(n: int, seed: int) -> list[str]:
    """Harf başına eşit, üçlü tekrar ve sabit adım içermeyen hedef dizi."""
    rnd = random.Random(seed)
    base = list("ABCDE") * (n // 5)
    assert len(base) == n, "soru sayısı 5'in katı olmalı"
    for _ in range(10000):
        rnd.shuffle(base)
        seq = "".join(base)
        if not re.search(r"(.)\1{2}", seq) and not letter_pattern(seq):
            return base
    raise SystemExit("hedef harf dizisi kurulamadı")


def build_package(store, prefix, ders, konu, style, seed):
    tgts = targets(len(store), seed)
    questions = []
    for index, (fields, target) in enumerate(zip(store, tgts), 1):
        rest = list(fields["distractors"])
        ordered = [fields["correct"] if L == target else rest.pop(0) for L in "ABCDE"]
        options = dict(zip("ABCDE", ordered))
        answer = next(L for L, v in options.items() if v == fields["correct"])
        questions.append({
            "id": f"{prefix}-{index:04d}",
            "ders": ders,
            "konu": konu,
            "stem": fields["stem"],
            "options": options,
            "answer": answer,
            "solution": fields["sol"],
            "source": {"kind": "generated", "styleRef": style, "legislationRef": None},
            "validYear": 2026,
            "mockExamId": None,
        })
    ids = [q["id"] for q in questions]
    assert len(set(ids)) == len(ids), "yinelenen id"
    return questions


def write_or_check(relative_path, questions, write):
    """İçerik ve uygulama repolarına yazar veya ikisini de karşılaştırır."""
    payload = json.dumps(questions, ensure_ascii=False, indent=2) + "\n"
    mismatches = []
    for path in (ROOT / relative_path, APP_ROOT / relative_path):
        if write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(payload, encoding="utf-8")
        elif not path.exists():
            mismatches.append(f"{path} yok")
        elif path.read_text(encoding="utf-8") != payload:
            mismatches.append(f"{path} builder çıktısından farklı")
    return mismatches


def main(store, *, prefix, ders, konu, style, seed, relative_path, label):
    import argparse

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--write", action="store_true")
    args = parser.parse_args()

    questions = build_package(store, prefix, ders, konu, style, seed)
    mismatches = write_or_check(relative_path, questions, args.write)
    if mismatches:
        print("Eşleşmeyen dosyalar:")
        for m in mismatches:
            print(f"- {m}")
        return 1
    print(f"{len(questions)} soru ({label}) iki repoda doğrulandı.")
    return 0
