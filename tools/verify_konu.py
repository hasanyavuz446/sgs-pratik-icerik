#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Konu havuzu paketi için tam denetim: audit.py'nin görmediklerine bakar.

Kullanım:
    python3 tools/verify_konu.py questions_topic_maliyet_unsurlari_2026.json

audit.py mekanik kaliteyi (harf örüntüsü, length-tell, şema) denetler.
Bu alet onun ÜSTÜNE bakar:
  1. İki depo özdeş mi (app assets ↔ OTA) — geçmişte iki kez atlandı
  2. İki manifest aynı sürümde ve paket kayıtlı mı
  3. topicId/lessonId curriculum.json'da tanımlı mı
  4. Konu havuzu etiketi var mı, 60 soru mu
  5. legislationRef her soruda dolu mu (mevzuat dayanağı)
  6. Bölüm havuzuyla kök çakışması (audit --manifest de bakar, burada odaklı)
  7. Elle okunacak soruları listeler: hesap + mevzuat örneklemi
"""
import json, os, re, sys, random, collections

APP = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik"
OTA = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik"
CALC = re.compile(r"\d[\d.]*\s?(TL|lira|birim|adet)\b")
MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")

def norm(s): return re.sub(r"\W+", "", s).lower()

def main():
    if len(sys.argv) < 2:
        print(__doc__); return 1
    fname = os.path.basename(sys.argv[1])
    app_f = f"{APP}/assets/content/yeterlilik/{fname}"
    ota_f = f"{OTA}/content/yeterlilik/{fname}"
    bad = []

    # 1. iki depo
    if not os.path.exists(app_f): bad.append(f"app assets'te YOK: {fname}")
    if not os.path.exists(ota_f): bad.append(f"OTA'da YOK: {fname}")
    if bad:
        for b in bad: print("🚨", b)
        return 1
    a_raw, o_raw = open(app_f, encoding="utf-8").read(), open(ota_f, encoding="utf-8").read()
    print(("✅" if a_raw == o_raw else "🚨"), "iki depo özdeş" if a_raw == o_raw else "İKİ DEPO FARKLI")
    if a_raw != o_raw: bad.append("depo farkı")

    qs = json.loads(a_raw)

    # 2. manifest
    am = json.load(open(f"{APP}/assets/content/manifest_v2.json", encoding="utf-8"))
    om = json.load(open(f"{OTA}/content/v2/manifest.json", encoding="utf-8"))
    rel = f"yeterlilik/{fname}"
    in_a = any(p.get("file") == rel for p in am["packs"])
    in_o = any(p.get("file") == rel for p in om["packs"])
    same_v = str(am["version"]) == str(om["version"])
    print(("✅" if in_a and in_o else "🚨"), f"manifest kaydı: app={in_a} ota={in_o}")
    print(("✅" if same_v else "🚨"), f"sürüm: app v{am['version']} | ota v{om['version']}")
    if not (in_a and in_o and same_v): bad.append("manifest")

    # 3. müfredat
    c = json.load(open(f"{APP}/assets/content/curriculum.json", encoding="utf-8"))
    valid = set()
    for l in c["lessons"]:
        for t in l.get("topics", []):
            if "yeterlilik" in (t.get("programIds") or l.get("programIds") or []):
                valid.add((l["id"], t["id"]))
    unknown = {(q.get("lessonId"), q.get("topicId")) for q in qs} - valid
    print(("✅" if not unknown else "🚨"), "müfredat bağı" if not unknown else f"MÜFREDATTA YOK: {unknown}")
    if unknown: bad.append("müfredat")

    # 4. sayı + etiket
    n = len(qs)
    kh = sum(1 for q in qs if "Konu Havuzu" in q.get("tags", []))
    print(("✅" if n == 60 else "🚨"), f"soru sayısı: {n}")
    print(("✅" if kh == n else "🚨"), f"'Konu Havuzu' etiketi: {kh}/{n}")
    if n != 60 or kh != n: bad.append("sayı/etiket")

    # 5. mevzuat dayanağı
    noref = [q["id"] for q in qs if not (q.get("source", {}).get("legislationRef") or "").strip()]
    print(("✅" if not noref else "🚨"), "legislationRef dolu" if not noref else f"DAYANAK YOK: {noref[:5]}")
    if noref: bad.append("legislationRef")

    # 6. bölüm havuzuyla çakışma
    bolum = {}
    for p in om["packs"]:
        if "yeterlilik" not in (p.get("programIds") or []): continue
        fp = os.path.join(f"{OTA}/content", p["file"])
        if not os.path.exists(fp) or os.path.basename(fp) == fname: continue
        for q in json.load(open(fp, encoding="utf-8")):
            if "Konu Havuzu" not in q.get("tags", []):
                bolum[norm(q.get("question") or q.get("stem", ""))] = q["id"]
    cak = [(q["id"], bolum[norm(q["question"])]) for q in qs if norm(q["question"]) in bolum]
    print(("✅" if not cak else "🚨"), "bölüm havuzuyla çakışma yok" if not cak else f"ÇAKIŞMA: {cak[:3]}")
    if cak: bad.append("havuz çakışması")

    # 7. elle okunacaklar
    hesap = [q for q in qs if CALC.search(q["question"] + " " + " ".join(q["choices"].values()))]
    onc = sum(1 for q in qs if len(MARK.findall(q["question"])) >= 2)
    print(f"\n── ELLE DOĞRULANACAK ──")
    print(f"  hesap sorusu: {len(hesap)} | öncüllü: {onc}")
    refs = collections.Counter((q.get("source", {}).get("legislationRef") or "").split(" - ")[0] for q in qs)
    print(f"  mevzuat dayanakları: {dict(refs.most_common(6))}")
    random.seed(1)
    for q in random.sample(qs, min(3, len(qs))):
        print(f"\n  [{q['id']}] {q['question'][:88]}")
        print(f"     ✔ {q['choices'][q['correctAnswer']][:88]}")
        print(f"     ref: {q.get('source',{}).get('legislationRef')}")

    print(f"\n{'❌ SORUN: ' + ', '.join(bad) if bad else '✅ MEKANİK DENETİM TEMİZ — alan denetimi elle yapılacak'}")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
