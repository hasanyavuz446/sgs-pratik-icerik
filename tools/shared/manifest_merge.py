#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SGS ve SMMM kaynak manifestlerini çalışma zamanı manifestinde birleştirir.

Kaynaklar:
  content/v2/manifests/sgs.json
  content/v2/manifests/smmm.json

Çıktı:
  content/v2/manifest.json

`--split` mevcut birleşik manifesti ilk kez iki kaynağa ayırır.
`--check` kaynakların mevcut birleşik manifestle semantik olarak aynı olduğunu denetler.
`--write` birleşik manifesti yeniden üretir; içerik yayını sırasında benzersiz bir
`--version` verilmesi önerilir. Sürüm verilmezse mevcut çalışma zamanı sürümü korunur.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME = ROOT / "content/v2/manifest.json"
SOURCE_DIR = ROOT / "content/v2/manifests"
SOURCES = {
    "sgs": SOURCE_DIR / "sgs.json",
    "yeterlilik": SOURCE_DIR / "smmm.json",
}


def read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def validate_source(program: str, source: dict) -> None:
    assert source.get("program") == program, (program, source.get("program"))
    assert source.get("schemaVersion") == 2, (program, source.get("schemaVersion"))
    for pack in source.get("packs", []):
        assert pack.get("programIds") == [program], (program, pack)


def split() -> None:
    runtime = read(RUNTIME)
    for program, path in SOURCES.items():
        source = {
            "revision": runtime["version"],
            "schemaVersion": runtime["schemaVersion"],
            "program": program,
            "packs": [
                pack for pack in runtime["packs"]
                if pack.get("programIds") == [program]
            ],
        }
        if program == "yeterlilik" and runtime.get("stimuli"):
            source["stimuli"] = runtime["stimuli"]
        validate_source(program, source)
        dump(path, source)
        print(f"ayrıldı: {path.relative_to(ROOT)} ({len(source['packs'])} paket)")


def merged(version: str | None = None) -> dict:
    sources = {program: read(path) for program, path in SOURCES.items()}
    for program, source in sources.items():
        validate_source(program, source)

    runtime_version = version
    if runtime_version is None and RUNTIME.exists():
        runtime_version = str(read(RUNTIME)["version"])
    if runtime_version is None:
        runtime_version = "initial"

    packs = sources["sgs"]["packs"] + sources["yeterlilik"]["packs"]
    keys = [(pack["programIds"][0], pack["file"]) for pack in packs]
    assert len(keys) == len(set(keys)), "Kaynak manifestlerde yinelenen program/dosya var."
    return {
        "version": runtime_version,
        "schemaVersion": 2,
        "programs": ["sgs", "yeterlilik"],
        "stimuli": sources["yeterlilik"].get("stimuli", "yeterlilik/stimuli.json"),
        "packs": packs,
    }


def comparable(manifest: dict) -> dict:
    """Biçimden bağımsız, çalışma zamanı anlamını karşılaştırır."""
    return {
        "version": str(manifest.get("version")),
        "schemaVersion": manifest.get("schemaVersion"),
        "programs": manifest.get("programs"),
        "stimuli": manifest.get("stimuli"),
        "packs": manifest.get("packs"),
    }


def check() -> None:
    expected = merged()
    actual = read(RUNTIME)
    assert comparable(expected) == comparable(actual), (
        "Kaynak manifestler ile content/v2/manifest.json farklı. "
        "Yayımdan önce --write ve benzersiz --version kullanın."
    )
    print(
        f"manifest uyumlu: {len(expected['packs'])} paket | "
        f"SGS {len(read(SOURCES['sgs'])['packs'])} | "
        f"SMMM {len(read(SOURCES['yeterlilik'])['packs'])} | "
        f"sürüm {expected['version']}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--split", action="store_true")
    action.add_argument("--check", action="store_true")
    action.add_argument("--write", action="store_true")
    parser.add_argument("--version")
    args = parser.parse_args()

    if args.split:
        split()
    elif args.check:
        check()
    else:
        result = merged(args.version)
        dump(RUNTIME, result)
        print(f"birleştirildi: {RUNTIME.relative_to(ROOT)} ({len(result['packs'])} paket)")


if __name__ == "__main__":
    main()
