#!/usr/bin/env python3
"""Aynı paketteki soruların ortak veri setini raporlar (kapı değil, rapor).

audit.py'nin yakın-benzerlik denetimi metne bakar; farklı şey soran ama aynı
tutarları kullanan iki soru (ör. aynı ücret bordrosu, aynı mizan kalanları)
oradan geçer. Bu araç her paket içinde kökteki tutarları (hesap kodları hariç,
binlik ayraçlı veya ondalıklı sayılar) karşılaştırır.

Kullanım:
    python3 tools/sgs/veri_tekrari.py [--manifest content/v2/manifest.json] [--esik 5] [--oran 0.6]
"""
from __future__ import annotations

import argparse
import itertools
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audit  # noqa: E402

TUTAR = re.compile(r"\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+,\d+")


def tutarlar(metin: str) -> set[str]:
    return set(TUTAR.findall(metin))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="content/v2/manifest.json")
    ap.add_argument("--esik", type=int, default=5, help="en az ortak tutar sayısı")
    ap.add_argument("--oran", type=float, default=0.6, help="küçük kümeye göre ortaklık oranı")
    a = ap.parse_args()
    toplam = 0
    for yol in audit.manifest_paths(a.manifest):
        sorular = audit.load(yol)
        veri = [(q["id"], tutarlar(q["stem"])) for q in sorular]
        for (i, ti), (j, tj) in itertools.combinations(veri, 2):
            ortak = ti & tj
            if len(ortak) >= a.esik and len(ortak) / max(1, min(len(ti), len(tj))) >= a.oran:
                toplam += 1
                print(f"{yol.split('content/')[-1]}  {i}  {j}  ortak {len(ortak)}: {', '.join(sorted(ortak)[:8])}")
    print(f"TOPLAM: {toplam} çift")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
