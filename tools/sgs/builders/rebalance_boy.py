#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Salt BOY dengeleme — atma-şıkkı OLMAYAN dosyalar için (#68/#69).

muhasebe_standartlari'nın kusuru atma-şıkkıydı; onu dolgu_engine + rebalance_
standartlar çözdü. Havuzun geri kalanındaki (meslek·ticaret·türkçe·denetim·
dağınık) FATAL'lar ise SALT BOY: doğru şık sistematik olarak en uzun ya da en
kısa. Bu araç dolgu motorunu ÇALIŞTIRMAZ (kırpacak dolgu yok); yalnız elle
yazılmış uzat/kisalt yamalarını uygular ve dokunulmazları doğrular.

    rebalance_boy.py <klasör/dosya> --rapor   → doğru-en-uzun / en-kısa dökümü
    rebalance_boy.py <klasör/dosya>           → KONFIG'deki yamayı uygula

Kural (rebalance_standartlar ile aynı):
  · uzat  : çeldiriciyi doğrunun EN AZ 15 KARAKTER üstüne yaz (assert)
  · kisalt: çeldiriciyi doğrunun ALTINA yaz (assert)
  · doğru cevaba/köke/çözüme/harfe DOKUNMA → 0/0/0/0 doğrulanır
  · dolgu sözcüğü (zorunda/…maktadır) YAZMA — "dolguyu ele" stratejisini besler
  · sayısal/kısa-kategori/süre şıklı soruları zorlama
"""
from __future__ import annotations

import json
import re
import sys

KOK = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content"
ONCUL = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
DOLGU = re.compile(r"(zorunda|durumundadır|bulunmaktadır|kalınmaktadır|tutulmaktadır)", re.I)
SAYISAL = re.compile(r"\d[\d.,]*\s*(TL|₺|%)|^\s*[-+]?\d")

# ad → {"uzat": {qid: {harf: metin}}, "kisalt": {...}}
KONFIG: dict[str, dict] = {}


def _oncullu(q):
    return len(ONCUL.findall(q["stem"])) >= 2


def dokum(path: str):
    qs = json.load(open(path, encoding="utf-8"))
    uzun, kisa = [], []
    for q in qs:
        if _oncullu(q):
            continue
        o = q["options"]
        d = len(o[q["answer"]])
        L = [len(v) for v in o.values()]
        if d == max(L) and L.count(max(L)) == 1:
            cs = [(h, v) for h, v in o.items() if h != q["answer"] and not DOLGU.search(v)]
            if cs:
                h, v = max(cs, key=lambda t: len(t[1]))
                uzun.append((q["id"], d, h, v))
        elif d == min(L) and L.count(min(L)) == 1 and not SAYISAL.search(o[q["answer"]]) and d >= 32:
            h = next(x for x in "ABCDE" if x != q["answer"])
            kisa.append((q["id"], d, h, o[q["answer"]]))
    print(f"{path.split('/')[-1]}: doğru-en-uzun {len(uzun)} · doğru-en-kısa {len(kisa)}")
    if uzun:
        print("── UZAT adayları (uzun çeldiriciyi doğrunun üstüne çıkar) ──")
        for qid, d, h, v in sorted(uzun, key=lambda t: -t[1]):
            print(f'    "{qid}": {{"{h}": ""}},  # d={d} ≥{d+15} | {v[:60]}')
    if kisa:
        print("── KISALT adayları (kısa yanlış, doğrunun altına) ──")
        for qid, d, h, v in sorted(kisa, key=lambda t: t[1]):
            print(f'    "{qid}": {{"{h}": ""}},  # d={d} <{d} | ✓{v[:52]}')


def calistir(ad: str):
    path = f"{KOK}/{ad}.json"
    cfg = KONFIG[ad]
    qs = json.load(open(path, encoding="utf-8"))
    onceki = {q["id"]: q for q in json.loads(json.dumps(qs))}
    idx = {q["id"]: q for q in qs}

    for qid, degisim in cfg.get("uzat", {}).items():
        q = idx[qid]
        d = len(q["options"][q["answer"]])
        for harf, yeni in degisim.items():
            assert harf != q["answer"], f"{qid}: DOĞRU şıkka dokunulamaz ({harf})"
            assert len(yeni) >= d + 15, f"{qid}/{harf}: {len(yeni)} < doğru {d}+15"
            assert not DOLGU.search(yeni), f"{qid}/{harf}: dolgu sözcüğü var"
            q["options"][harf] = yeni
    for qid, degisim in cfg.get("kisalt", {}).items():
        q = idx[qid]
        d = len(q["options"][q["answer"]])
        for harf, yeni in degisim.items():
            assert harf != q["answer"], f"{qid}: DOĞRU şıkka dokunulamaz ({harf})"
            assert len(yeni) < d, f"{qid}/{harf}: {len(yeni)} ≥ doğru {d}"
            q["options"][harf] = yeni

    for q in qs:
        assert len(set(q["options"].values())) == 5, f"{q['id']}: şık çakışması"

    kok = coz = dgr = hrf = 0
    for q in qs:
        o = onceki[q["id"]]
        kok += q["stem"] != o["stem"]
        coz += q.get("solution") != o.get("solution")
        hrf += q["answer"] != o["answer"]
        dgr += q["options"][q["answer"]] != o["options"][o["answer"]]
    assert (kok, coz, dgr, hrf) == (0, 0, 0, 0), \
        f"DOKUNULMAZ DEĞİŞTİ kök/çözüm/doğru/harf: {kok}/{coz}/{dgr}/{hrf}"

    json.dump(qs, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    n = len(cfg.get("uzat", {})) + len(cfg.get("kisalt", {}))
    print(f"{ad}: {n} yama uygulandı · kök/çözüm/doğru/harf 0/0/0/0")


if __name__ == "__main__":
    ad = sys.argv[1]
    if "--rapor" in sys.argv:
        dokum(f"{KOK}/{ad}.json")
    else:
        calistir(ad)
