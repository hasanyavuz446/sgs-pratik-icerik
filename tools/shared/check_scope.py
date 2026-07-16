#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çalışma ağacındaki değişikliklerin program sahipliği sınırında kaldığını denetler."""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def changed_paths() -> list[str]:
    result = subprocess.run(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    paths = []
    for line in result.stdout.splitlines():
        path = line[3:]
        if " -> " in path:
            old, new = path.split(" -> ", 1)
            paths.extend((old, new))
        else:
            paths.append(path)
    return sorted(set(paths))


def owner(path: str) -> str:
    if path.startswith("tools/sgs/") or path == "content/v2/manifests/sgs.json":
        return "sgs"
    if path.startswith("tools/smmm/") or path.startswith("content/yeterlilik/") or path == "content/v2/manifests/smmm.json":
        return "smmm"
    if path.startswith("tools/shared/") or path in {
        "AGENTS.md", "CLAUDE.md", "tools/README.md", "tools/OWNERSHIP.md",
        "tools/URETIM_KURALLARI.md", "content/v2/manifest.json",
    }:
        return "shared"
    if path.startswith("content/"):
        return "sgs"
    return "shared"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--program", choices=("sgs", "smmm"), required=True)
    parser.add_argument("--allow-shared", action="store_true")
    args = parser.parse_args()

    allowed = {args.program}
    if args.allow_shared:
        allowed.add("shared")
    violations = [(path, owner(path)) for path in changed_paths() if owner(path) not in allowed]
    if violations:
        print(f"{args.program} kapsamı dışındaki değişiklikler:")
        for path, path_owner in violations:
            print(f"  - {path} ({path_owner})")
        return 1
    print(f"kapsam temiz: {args.program} | {len(changed_paths())} değişiklik")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
