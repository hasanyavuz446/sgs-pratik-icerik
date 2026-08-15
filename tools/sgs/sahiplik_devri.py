#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yeniden yazılan bir paketin sahipliğini eski bakım builder'larından devral.

Bir paket baştan yazıldığında, o paketin sorularını tutan eski builder'ların
blokları çıkarılmalıdır (§3 "Her sorunun TEK sahibi olur"). Aksi hâlde iki
builder aynı metne yazar, `--check` sıraya bağımlı hâle gelir ve eski builder
yenisinin üstüne yazabilir — 2026-08-14'te fix_meslek_length_quality ile tam
olarak bu yaşandı.

Kullanım:
    python3 tools/sgs/sahiplik_devri.py \
        --konu content/ticaret_hukuku/kambiyo_senetleri.json \
        --onek kmb-gen- \
        --yeni build_hukuk_kambiyo_yapisal.py [--yaz]

--yaz verilmezse yalnız rapor eder.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BUILDERS = ROOT / "tools" / "sgs" / "builders"

ARGV_KORUMASI = '''    # ⚠️ Bu builder --check DESTEKLEMEZ ve calistiginda dogrudan YAZAR.
    # Toplu dogrulama donguleri onu "--check" ile cagirdiginda argumani sessizce
    # yok sayip yayinlanmis icerigi geri yazar. Artik arguman verilirse yazmadan
    # hata verip cikar.
    import sys
    if sys.argv[1:]:
        print("HATA: bu builder arguman kabul etmez ve calistiginda dogrudan YAZAR.")
        print("Dogrulama icin git diff kullanin; yazmak icin argumansiz calistirin.")
        raise SystemExit(2)
'''


def blok_cikar(metin: str, anahtar: str, onek: str) -> tuple[str, int]:
    """`"<anahtar>": { ... },` bloğunu çıkar; kaç kayıt gittiğini döndür."""
    toplam = 0
    while f'"{anahtar}": {{' in metin:
        i = metin.index(f'    "{anahtar}": {{')
        m = re.compile(r"\n    \},?\n").search(metin, i)
        if not m:
            break
        j = m.end()
        toplam += len(re.findall(rf"{re.escape(onek)}\d{{4}}", metin[i:j])) or \
                  len(re.findall(r'"\d{4}\|[A-E]"', metin[i:j]))
        metin = metin[:i] + metin[j:]
    return metin, toplam


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--konu", required=True)
    ap.add_argument("--onek", required=True)
    ap.add_argument("--yeni", required=True)
    ap.add_argument("--yaz", action="store_true")
    a = ap.parse_args()

    kisa = a.konu.removeprefix("content/")
    notu = (f"\n⚠️ SAHIPLIK DEVRI: {kisa} bloku bu dosyadan CIKARILDI; sahiplik\n"
            f"{a.yeni} dosyasina gecti. Bir sorunun tek sahibi olmali.\n")
    toplam = 0
    for f in sorted(BUILDERS.glob("*.py")):
        if f.name == a.yeni:
            continue
        s = ilk = f.read_text(encoding="utf-8")
        if a.konu not in s and kisa not in s and a.onek not in s:
            continue
        n = 0
        for anahtar in (a.konu, kisa):
            s, k = blok_cikar(s, anahtar, a.onek)
            n += k
        korumali = bool(re.search(r"args\.check", s))
        if not korumali and "arguman kabul etmez" not in s:
            m = re.search(r'^if __name__ == "__main__":\n', s, re.M)
            if m:
                s = s[:m.end()] + ARGV_KORUMASI + s[m.end():]
                print(f"     + {f.name}: argv koruması eklendi (--check yok)")
        if n and "SAHIPLIK DEVRI" not in s:
            k = s.index('"""', s.index('"""') + 3)
            s = s[:k] + notu + s[k:]
        if s != ilk:
            toplam += n
            print(f"  {'✅' if a.yaz else '·'} {f.name}: {n} kayıt")
            if a.yaz:
                f.write_text(s, encoding="utf-8")
    print(f"toplam {toplam} kayıt" + ("" if a.yaz else "  (rapor modu — --yaz ile uygula)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
