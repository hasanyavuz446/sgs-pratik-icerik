#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hukuk yapısal kalibrasyon boru hattı — tasarım modülünden yayına hazır builder.

Hukuk ailesinde 11 konu bu adımların HEPSİ elle yapılarak üretildi; kalan
konularda tekrar eden kısım buraya alındı. Otomatikleşen yalnız MEKANİK
adımlardır — 60 sorunun hukuki içeriği tasarım modülünde elle yazılır.

Tasarım modülünün sağlaması gerekenler:
    ONEK        : soru kimliği öneki (örn. "tic-kmb-gen-")
    KONU        : konu adı
    P           : {tam_id: {stem, correct, distractors, sol, duzey}}
    boy_denetimi(), duzey_denetimi()

Kullanım:
    python3 tools/sgs/yapisal_pipeline.py <tasarim_modulu.py> \
        --konu content/ticaret_hukuku/kambiyo_senetleri.json \
        --builder build_hukuk_kambiyo_yapisal.py \
        --baslik "Kambiyo Senetleri" [--yaz]

Adımlar:
  1. İki kapıyı çalıştır (§5 boy · §1 bilişsel düzey) — geçmezse DURUR.
  2. Cevap harflerini HEAD'den al, §6 üçlü run'ı kır, şıkları dağıt.
  3. Builder'ı üret.
  4. Sahiplik tara: bu pakette soru tutan eski builder'ları bul ve raporla.
  5. --yaz verilirse builder'ı çalıştır ve denetimi göster.
"""
from __future__ import annotations

import argparse
import collections
import importlib.util
import json
import random
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BUILDERS = ROOT / "tools" / "sgs" / "builders"


def modul_yukle(yol: Path):
    spec = importlib.util.spec_from_file_location("tasarim", yol)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["tasarim"] = mod
    spec.loader.exec_module(mod)
    return mod


def harfleri_al(konu_yolu: str, sirali: list[str], onek: str) -> dict[str, str]:
    """HEAD'deki cevap harflerini koru; §6 üçlü run varsa kır."""
    ham = subprocess.run(["git", "-C", str(ROOT), "show", f"HEAD:{konu_yolu}"],
                         capture_output=True, text=True).stdout
    veri = json.loads(ham)
    sorular = veri["questions"] if isinstance(veri, dict) else veri
    harf = {q["id"]: q["answer"] for q in sorular}
    eksik = [q for q in sirali if q not in harf]
    if eksik:
        raise SystemExit(f"HEAD'de bulunmayan soru kimlikleri: {eksik[:5]}")
    dizi = "".join(harf[q] for q in sirali)
    for m in re.finditer(r"(.)\1{2,}", dizi):
        i = m.start() + 1
        harf[sirali[i]] = next(c for c in "ABCDE" if c != m.group()[0])
    return harf


def sahiplik_tara(konu_yolu: str, onek: str) -> list[tuple[str, int, bool]]:
    """Bu pakette soru tutan eski builder'ları bul. (dosya, kayıt, --check var mı)"""
    kisa = konu_yolu.removeprefix("content/")
    bulunan = []
    for f in sorted(BUILDERS.glob("*.py")):
        s = f.read_text(encoding="utf-8")
        if konu_yolu not in s and kisa not in s and onek not in s:
            continue
        n = len(re.findall(rf"{re.escape(onek)}\d{{4}}", s))
        bulunan.append((f.name, n, bool(re.search(r"args\.check", s))))
    return bulunan


def builder_uret(mod, harf, baslik, konu_yolu, ozet, dayanak, tohum):
    sirali = sorted(mod.P)
    rnd = random.Random(tohum)
    bloklar = []
    for qid in sirali:
        f = mod.P[qid]
        L = harf[qid]
        ce = list(f["distractors"])
        rnd.shuffle(ce)
        o = {L: f["correct"]}
        for c, t in zip([c for c in "ABCDE" if c != L], ce):
            o[c] = t
        secenek = "\n".join(f"            {c!r}: {o[c]!r}," for c in "ABCDE")
        bloklar.append(
            f"    # düzey {f['duzey']}\n    {qid[len(mod.ONEK):]!r}: patch(\n"
            f"        {f['stem']!r},\n        {{\n{secenek}\n        }},\n"
            f"        {L!r},\n        {f['sol']!r},\n    ),")
    return f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""{baslik} — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

{ozet}

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: {dayanak}
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "{konu_yolu}"
STYLE_REF = "SGS Hukuk (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "{mod.ONEK}"


def patch(stem, options, answer, solution):
    return {{
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {{"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": {dayanak_ref!r}}},
        "validYear": 2026, "mockExamId": None,
    }}


_PATCHES = {{
{chr(10).join(bloklar)}
}}

PATCHES = {{ONEK + k: v for k, v in _PATCHES.items()}}


def apply_or_check(path, write):
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    by_id = {{q["id"]: q for q in questions}}
    fark = []
    for qid, alanlar in PATCHES.items():
        q = by_id.get(qid)
        if q is None:
            raise SystemExit(f"Soru bulunamadi: {{path}}::{{qid}}")
        for alan, beklenen in alanlar.items():
            if q.get(alan) != beklenen:
                fark.append(f"{{path}}::{{qid}}.{{alan}}")
                if write:
                    q[alan] = beklenen
        if write:
            if len(set(q["options"].values())) != 5:
                raise SystemExit(f"Secenek cakismasi: {{path}}::{{qid}}")
            if q["answer"] not in q["options"]:
                raise SystemExit(f"Cevap secenekte yok: {{path}}::{{qid}}")
    if write:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8")
    return fark


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--write", action="store_true")
    args = ap.parse_args()
    fark = []
    for path in (ROOT / RELATIVE_PATH, APP_ROOT / RELATIVE_PATH):
        fark.extend(apply_or_check(path, args.write))
    if args.check and fark:
        print("Eslesmeyen alanlar:")
        for f in fark[:20]:
            print(f"- {{f}}")
        return 1
    print(f"1 paket / {{len(PATCHES)}} soru ({baslik!r} yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tasarim")
    ap.add_argument("--konu", required=True)
    ap.add_argument("--builder", required=True)
    ap.add_argument("--baslik", required=True)
    ap.add_argument("--ozet", default="")
    ap.add_argument("--dayanak", default="")
    ap.add_argument("--dayanak-ref", default="6102 sayili Turk Ticaret Kanunu")
    ap.add_argument("--tohum", type=int, default=2026)
    ap.add_argument("--yaz", action="store_true")
    a = ap.parse_args()

    mod = modul_yukle(Path(a.tasarim))
    print(f"tasarım modülü: {len(mod.P)} yama")

    # 1) iki kapı
    n, t = mod.boy_denetimi()
    duzey = mod.duzey_denetimi()
    print(f"✅ §5 boy: {n}/{t} (%{n/t*100:.0f})   ✅ §1 düzey: {duzey}")

    # 2) harfler
    sirali = sorted(mod.P)
    harf = harfleri_al(a.konu, sirali, mod.ONEK)
    dizi = "".join(harf[q] for q in sirali)
    runs = [m.group() for m in re.finditer(r"(.)\1{2,}", dizi)]
    print(f"§6 harf: {dict(sorted(collections.Counter(dizi).items()))} · üçlü run: {runs or 'yok'}")

    # 3) builder
    global dayanak_ref
    dayanak_ref = a.dayanak_ref
    kod = builder_uret(mod, harf, a.baslik, a.konu, a.ozet, a.dayanak, a.tohum)
    hedef = BUILDERS / a.builder
    hedef.write_text(kod, encoding="utf-8")
    print(f"builder yazıldı: {hedef.name}")

    # 4) sahiplik
    sahip = [(f, k, c) for f, k, c in sahiplik_tara(a.konu, mod.ONEK) if f != a.builder]
    if sahip:
        print("⚠️  SAHİPLİK — bu pakette soru tutan eski builder'lar:")
        for f, k, c in sahip:
            print(f"     {f:38} {k:3} kayıt   --check:{'var' if c else 'YOK → YAZAR'}")
    else:
        print("sahiplik: devir gerekmiyor")

    # 5) yaz + denetle
    if a.yaz:
        subprocess.run([sys.executable, str(hedef), "--write"], check=True)
        subprocess.run([sys.executable, str(ROOT / "tools/sgs/audit.py"), a.konu], check=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
