#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SGS/Yeterlilik içerik denetim aleti.

Kullanım:
    python3 tools/audit.py content/yeterlilik/questions_topic_*.json
    python3 tools/audit.py --manifest content/v2/manifest.json

Codex'in ürettiği soru paketlerini bizim kalite ölçütlerimize göre denetler.
Hem SGS ({ders,konu,stem,options,answer,solution}) hem Yeterlilik
({lessonId,topicId,question,choices,correctAnswer,explanation}) şemasını okur.

ÖLÇÜTLER (ihlal = FATAL ise yayına gidemez):
  FATAL  harf-örüntü   Doğru cevap dizisi rotasyon/periyodik olamaz (ABCDEABCDE…)
  FATAL  şema          5 şık A-E, answer ∈ options, boş şık yok, id/kök tekrarsız
  FATAL  çözüm-harf    "Doğru cevap X" varsa answer ile eşleşmeli
  UYARI  harf-dağılım  Her harf ~n/5 (±%25), ardışık tekrar ≤2
  UYARI  length-tell   Doğru şık tek-en-uzun ya da "2 uzun + 3 kısa"dan biri olmasın
  UYARI  öncüllü       "hepsi (I,II ve III)" oranı ~%20-30; öncüller \n\n ile ayrık
  UYARI  yıla-bağlı    Oran/eşik/had sorulmasın (senaryo tutarı serbest)
  BİLGİ  hesap         Aritmetik içeren sorular elle doğrulama ister
"""
import json, re, sys, os, collections, itertools

MARK = re.compile(r"(?m)^\s*\*{0,2}(IV|I{1,3}|V)[\.\)]\s")
SOLLETTER = re.compile(r"Doğru cevap ([A-E])\b")
# Yıla bağlı: yüzde oranı, "had/istisna/tarife/dilim" + sayı
RATE = re.compile(r"%\s?\d|\d\s?%")
THRESHOLD = re.compile(r"(istisna haddi|istisna tutarı|tarife|vergi dilimi|asgari ücret|yeniden değerleme oranı)", re.I)
# Kök oranı vermeden "genel oran/yürürlükteki oran" deyip bilinmesini bekliyorsa ihlal.
IMPLICIT_RATE = re.compile(r"(genel oran|yürürlükteki oran|cari oran[ıi]|geçerli KDV oran)", re.I)
CALC = re.compile(r"\d[\d.]*\s?(TL|lira|birim|adet)\b")


def load(path):
    d = json.load(open(path, encoding="utf-8"))
    return d if isinstance(d, list) else d.get("questions", [])


def norm(q):
    """İki şemayı tek biçime indirger."""
    return {
        "id": q.get("id"),
        "stem": q.get("question") or q.get("stem") or "",
        "opts": q.get("choices") or q.get("options") or {},
        "ans": q.get("correctAnswer") or q.get("answer"),
        "sol": q.get("explanation") or q.get("solution") or "",
        "tags": q.get("tags", []),
    }


def sm(s):
    return re.sub(r"\*{1,2}", "", s).strip()


def letter_pattern(seq):
    """Rotasyon/periyodik örüntü tespiti. Bizim eski dedektör bunu kaçırıyordu:
    ABCDEABCDE… dizisi '12'şer dağılım + run≤2' kontrolünü sorunsuz geçer."""
    issues = []
    if len(seq) < 10:
        return issues
    idx = ["ABCDE".index(c) for c in seq]

    # 1) Sabit adımlı rotasyon (ABCDE… veya ACEBD… gibi)
    steps = {(idx[i + 1] - idx[i]) % 5 for i in range(len(idx) - 1)}
    if len(steps) == 1:
        issues.append(("FATAL", "harf-örüntü",
                       f"Doğru cevap dizisi sabit adımlı rotasyon (adım={steps.pop()}): {seq[:15]}…"))
        return issues

    # 2) Kısa periyot (seq[i] == seq[i+p] büyük oranda)
    for p in range(1, 11):
        match = sum(1 for i in range(len(seq) - p) if seq[i] == seq[i + p])
        if match / (len(seq) - p) >= 0.9:
            issues.append(("FATAL", "harf-örüntü",
                           f"Doğru cevap dizisi {p} periyotlu tekrar ediyor: {seq[:15]}…"))
            return issues

    # 3) Bigram çeşitliliği: sağlıklı karışımda 25 bigramın çoğu görülür
    bigrams = {seq[i:i + 2] for i in range(len(seq) - 1)}
    if len(seq) >= 40 and len(bigrams) < 13:
        issues.append(("UYARI", "harf-örüntü",
                       f"Harf geçişleri fazla düzenli: 25 bigramdan yalnız {len(bigrams)} farklı"))
    return issues


def audit(path):
    qs = [norm(q) for q in load(path)]
    n = len(qs)
    out = []
    seen_ids, seen_stems = {}, {}

    for q in qs:
        qid = q["id"]
        # şema
        if set(q["opts"].keys()) != set("ABCDE"):
            out.append(("FATAL", "şema", f"{qid}: şıklar A-E değil ({sorted(q['opts'])})"))
        if q["ans"] not in q["opts"]:
            out.append(("FATAL", "şema", f"{qid}: doğru cevap şıklarda yok"))
        for k, v in q["opts"].items():
            if not v.strip():
                out.append(("FATAL", "şema", f"{qid}: {k} şıkkı boş"))
        if not q["sol"].strip():
            out.append(("FATAL", "şema", f"{qid}: çözüm boş"))
        if qid in seen_ids:
            out.append(("FATAL", "şema", f"{qid}: id tekrarlanıyor"))
        seen_ids[qid] = 1
        key = re.sub(r"\W+", "", q["stem"]).lower()
        if key in seen_stems:
            out.append(("FATAL", "şema", f"{qid}: soru kökü {seen_stems[key]} ile aynı"))
        seen_stems[key] = qid

        # çözüm-harf senkronu
        m = SOLLETTER.search(q["sol"])
        if m and m.group(1) != q["ans"]:
            out.append(("FATAL", "çözüm-harf",
                        f"{qid}: çözüm '{m.group(1)}' diyor, answer '{q['ans']}'"))

        # length-tell (öncüllüler hariç)
        if len(MARK.findall(q["stem"])) < 2 and q["ans"] in q["opts"]:
            L = {k: len(sm(v)) for k, v in q["opts"].items()}
            a = L[q["ans"]]
            s = sorted(L.values(), reverse=True)
            if (a == s[0] and a >= 1.5 * s[1] and a >= 45) or \
               (s[1] >= 1.7 * s[2] and s[1] >= 45 and a >= s[1]):
                out.append(("UYARI", "length-tell", f"{qid}: doğru şık {a} kr, 2.uzun {s[1]} kr"))

        # Yıla bağlı oran/eşik. DİKKAT: oranın soru KÖKÜNDE verilmesi güvenlidir
        # ("5.000 TL + %20 KDV" → ölçülen şey kayıt, oran değil; oran değişse
        # soru yine kendi içinde tutarlı). İhlal, oranın CEVAP olmasıdır ya da
        # kökün oranı vermeyip öğrencinin bilmesini beklemesidir.
        opts_blob = " ".join(q["opts"].values())
        blob = q["stem"] + " " + opts_blob
        if RATE.search(opts_blob):
            out.append(("UYARI", "yıla-bağlı", f"{qid}: oran ŞIKTA — oranın kendisi sorulmuş"))
        elif THRESHOLD.search(blob):
            out.append(("UYARI", "yıla-bağlı", f"{qid}: had/tarife/dilim geçiyor — güncellik riski"))
        elif IMPLICIT_RATE.search(q["stem"]):
            out.append(("UYARI", "yıla-bağlı",
                        f"{qid}: oran kökte verilmemiş, bilinmesi bekleniyor"))
        elif CALC.search(blob):
            out.append(("BİLGİ", "hesap", f"{qid}: aritmetik — elle doğrulama gerek"))

    # harf dizisi
    seq = "".join(q["ans"] for q in qs if q["ans"] in "ABCDE")
    out += letter_pattern(seq)
    c = collections.Counter(seq)
    hedef = n / 5
    for k in "ABCDE":
        if abs(c.get(k, 0) - hedef) > hedef * 0.25:
            out.append(("UYARI", "harf-dağılım", f"{k} harfi {c.get(k,0)} kez (hedef ~{hedef:.0f})"))
    mx = max((sum(1 for _ in g) for _, g in itertools.groupby(seq)), default=0)
    if mx > 2:
        out.append(("UYARI", "harf-dağılım", f"aynı harf {mx} kez ardışık"))

    # öncüllü
    onc = [q for q in qs if len(MARK.findall(q["stem"])) >= 2]
    if onc:
        hepsi = sum(1 for q in onc
                    if re.sub(r"\s*\(.*?\)\s*$", "", q["opts"][q["ans"]]).strip() == "I, II ve III")
        oran = hepsi / len(onc)
        if oran > 0.35:
            out.append(("UYARI", "öncüllü",
                        f"'hepsi' cevabı {hepsi}/{len(onc)} (%{oran*100:.0f}) — hedef ~%20-30"))
        for q in onc:
            if "\n\n" not in q["stem"]:
                out.append(("UYARI", "öncüllü", f"{q['id']}: öncüller \\n\\n ile ayrılmamış"))
    return n, len(onc), out


def main():
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--manifest" in sys.argv:
        mp = paths[0]
        base = os.path.dirname(mp)
        m = json.load(open(mp, encoding="utf-8"))
        paths = []
        for p in m["packs"]:
            for cand in (os.path.join(base, p["file"]),
                         os.path.join(os.path.dirname(base), p["file"])):
                if os.path.exists(cand):
                    paths.append(cand)
                    break
    grand = collections.Counter()
    fatal_files = []
    for path in paths:
        n, onc, issues = audit(path)
        sev = collections.Counter(i[0] for i in issues)
        grand.update(sev)
        name = os.path.basename(path)
        flag = "❌" if sev["FATAL"] else ("⚠️ " if sev["UYARI"] else "✅")
        print(f"{flag} {name:52} {n:3} soru | öncüllü {onc:2} | "
              f"FATAL {sev['FATAL']:2} UYARI {sev['UYARI']:3} hesap {sev['BİLGİ']:3}")
        if sev["FATAL"]:
            fatal_files.append(name)
        for s, code, msg in issues:
            if s in ("FATAL", "UYARI"):
                print(f"      [{s}] {code}: {msg}")
    print(f"\nTOPLAM: FATAL {grand['FATAL']} | UYARI {grand['UYARI']} | "
          f"elle doğrulanacak hesap sorusu {grand['BİLGİ']}")
    if fatal_files:
        print("YAYINA GİDEMEZ:", ", ".join(fatal_files))
    return 1 if grand["FATAL"] else 0


if __name__ == "__main__":
    sys.exit(main())
