#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Eski Yeterlilik paketlerindeki kullanıcı/metaveri demo izlerini temizler.

Bu araç yalnız mekanik ve anlam-korumalı dönüşümler yapar:
  - "Demo Soru:" soru önekini kaldırır,
  - "Demo açıklama:" çözüm önekini kaldırır,
  - tam "Demo Soru" etiketini "Özgün Soru" olarak değiştirir,
  - examPeriod içindeki eski "demo" kelimesini kaldırır.

Soru, şık, cevap, çözümün geri kalanı ve kaynak alanları değiştirilmez. JSON'un
mevcut satır düzeni korunur; dosyanın tamamı yeniden biçimlendirilmez.

Kullanım:
    python3 tools/smmm/fixers/cleanup_legacy_yeterlilik.py --check
    python3 tools/smmm/fixers/cleanup_legacy_yeterlilik.py
"""

from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path


REPO = Path(__file__).resolve().parents[3]
DEFAULT_ROOTS = (
    REPO / "content" / "yeterlilik",
    REPO.parent / "smmm_sgs_pratik" / "assets" / "content" / "yeterlilik",
)

STEM_PREFIX = re.compile(
    r'((?:"question"|"stem")\s*:\s*")Demo\s+Soru:\s*',
    re.IGNORECASE,
)
SOLUTION_PREFIX = re.compile(
    r'((?:"explanation"|"solution")\s*:\s*")Demo\s+açıklama:\s*',
    re.IGNORECASE,
)
DEMO_TAG = re.compile(r'"Demo Soru"')
EXAM_PERIOD = re.compile(r'("examPeriod"\s*:\s*")([^"\\]*)(")')


def clean_period(match: re.Match[str]) -> str:
    value = match.group(2)
    cleaned = re.sub(r"\bdemo\b", "", value, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    if cleaned.casefold() == "2026/1 uyumlu".casefold():
        cleaned = "2026/1 formatına uyumlu"
    return f"{match.group(1)}{cleaned}{match.group(3)}"


def transform(text: str) -> tuple[str, collections.Counter[str]]:
    counts: collections.Counter[str] = collections.Counter()

    text, count = STEM_PREFIX.subn(r"\1", text)
    counts["soru_öneki"] += count

    text, count = SOLUTION_PREFIX.subn(r"\1", text)
    counts["çözüm_öneki"] += count

    text, count = DEMO_TAG.subn('"Özgün Soru"', text)
    counts["etiket"] += count

    def period_replacement(match: re.Match[str]) -> str:
        replacement = clean_period(match)
        if replacement != match.group(0):
            counts["sınav_dönemi"] += 1
        return replacement

    text = EXAM_PERIOD.sub(period_replacement, text)
    return text, counts


def process_root(root: Path, *, check: bool) -> tuple[int, collections.Counter[str]]:
    changed_files = 0
    totals: collections.Counter[str] = collections.Counter()
    for path in sorted(root.glob("*.json")):
        original = path.read_text(encoding="utf-8")
        updated, counts = transform(original)
        if updated == original:
            continue

        # Yazmadan önce dönüşümün JSON yapısını bozmadığını kanıtla.
        json.loads(updated)
        changed_files += 1
        totals.update(counts)
        if not check:
            path.write_text(updated, encoding="utf-8")
    return changed_files, totals


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Değişiklik yapmadan kapsamı raporla.")
    parser.add_argument("--root", action="append", type=Path, help="Varsayılan yerine işlenecek kök.")
    args = parser.parse_args()

    roots = tuple(args.root) if args.root else DEFAULT_ROOTS
    missing = [root for root in roots if not root.is_dir()]
    if missing:
        for root in missing:
            print("Kök bulunamadı:", root)
        return 2

    mode = "KONTROL" if args.check else "UYGULANDI"
    grand: collections.Counter[str] = collections.Counter()
    for root in roots:
        files, totals = process_root(root, check=args.check)
        grand.update(totals)
        print(f"{mode}: {root} | {files} dosya | {dict(totals)}")
    print(f"TOPLAM: {dict(grand)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
