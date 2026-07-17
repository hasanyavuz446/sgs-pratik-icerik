#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SGS içerik yapısı ve mekanik kalite denetimi.

Bu araç yalnız SGS `{ders, konu, stem, options, answer, solution}` şemasını ve
manifestte `programIds=["sgs"]` olarak kayıtlı paketleri kabul eder. SMMM'ye özgü
soru tipi kotalarını uygulamaz.
"""
from __future__ import annotations

import collections
import json
import os
import re
import sys


LETTERS = set("ABCDE")
DEMO = re.compile(r"demo\s+(?:soru|açıklama)", re.IGNORECASE)

# Çeldiricileri şişirmek için kullanılan dolgu kalıpları. Yalnız çeldiricilerde
# görünürlerse kalıbın kendisi güvenilir bir "yanlış" işaretine dönüşür.
DOLGU = re.compile(r"(zorunda|durumundadır|bulunmaktadır|kalınmaktadır|tutulmaktadır)", re.I)
# Öncüllü (I/II/III "hangileri") sorularda şık boyu doğal olarak eşit → boy ölçümü dışı.
ONCUL = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")


def kor_ogrenci(questions: list[dict]) -> tuple[int, str]:
    """Soruyu HİÇ OKUMADAN alınabilen EN İYİ puan (%) ve onu veren strateji.

    Rastgele taban %20'dir. Yüksek çıkması, şıkların içerikten bağımsız bir
    örüntü sızdırdığı anlamına gelir — öğrenci soruyu okumadan çözebiliyordur.

    ⚠ Ölçüt İKİ YÖNLÜ olmalı. İlk sürümü yalnız "en kısayı seç" deniyordu ve
    "doğru hep en UZUN" yazılmış dersleri temiz gösteriyordu; oysa öğrencinin
    öğreneceği kural hangi yönde olursa olsun aynı derecede zararlıdır.
    """
    if not questions:
        return 0, "-"
    stratejiler = {
        "en kısayı seç": lambda o: min(o, key=lambda k: (len(o[k]), k)),
        "en uzunu seç": lambda o: max(o, key=lambda k: (len(o[k]), k)),
        "dolguluyu ele, en kısayı seç": lambda o: (
            lambda r: min(r, key=lambda k: (len(r[k]), k))
        )({k: v for k, v in o.items() if not DOLGU.search(v)} or o),
        "dolguluyu ele, en uzunu seç": lambda o: (
            lambda r: max(r, key=lambda k: (len(r[k]), k))
        )({k: v for k, v in o.items() if not DOLGU.search(v)} or o),
    }
    en_iyi = (0, "-")
    for ad, sec in stratejiler.items():
        dogru = sum(sec(q["options"]) == q["answer"] for q in questions)
        puan = dogru * 100 // len(questions)
        if puan > en_iyi[0]:
            en_iyi = (puan, ad)
    return en_iyi


def boy_egilimi(questions: list[dict]) -> tuple[int, int, int]:
    """(en-uzun%, en-kısa%, ölçülen) — doğru şıkkın boy sıralamasındaki yeri.

    İkisi de ~%20 olmalı. Biri baskınsa boy ipucu vardır; YÖNÜ ÖNEMSİZ —
    "doğru hep en uzun" kadar "doğru hep en kısa" da okumadan çözdürür.
    """
    olcum = [q for q in questions if len(ONCUL.findall(q["stem"])) < 2]
    if not olcum:
        return 0, 0, 0
    uzun = kisa = 0
    for question in olcum:
        lengths = [len(v) for v in question["options"].values()]
        answer_length = len(question["options"][question["answer"]])
        uzun += answer_length == max(lengths)
        kisa += answer_length == min(lengths)
    return uzun * 100 // len(olcum), kisa * 100 // len(olcum), len(olcum)


def load(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    return data if isinstance(data, list) else data.get("questions", [])


def letter_pattern(sequence: str) -> bool:
    if len(sequence) < 10:
        return False
    for period in range(1, min(11, len(sequence))):
        compared = len(sequence) - period
        matches = sum(sequence[i] == sequence[i + period] for i in range(compared))
        if compared and matches / compared >= 0.9:
            return True
    return False


def audit(path: str) -> tuple[int, list[tuple[str, str]]]:
    questions = load(path)
    issues: list[tuple[str, str]] = []
    ids: set[str] = set()
    stems: set[str] = set()
    answers = []

    for index, question in enumerate(questions, 1):
        qid = str(question.get("id") or f"#{index}")
        if qid in ids:
            issues.append(("FATAL", f"yinelenen id: {qid}"))
        ids.add(qid)

        required = ("ders", "konu", "stem", "options", "answer", "solution")
        missing = [field for field in required if not question.get(field)]
        if missing:
            issues.append(("FATAL", f"{qid}: eksik alan: {', '.join(missing)}"))
            continue

        stem = re.sub(r"\s+", " ", question["stem"]).strip().casefold()

        options = question["options"]
        if not isinstance(options, dict) or set(options) != LETTERS:
            issues.append(("FATAL", f"{qid}: seçenekler tam A–E değil"))
            continue
        if any(not isinstance(value, str) or not value.strip() for value in options.values()):
            issues.append(("FATAL", f"{qid}: boş seçenek var"))
        normalized = {re.sub(r"\s+", " ", value).strip().casefold() for value in options.values()}
        if len(normalized) != 5:
            issues.append(("FATAL", f"{qid}: yinelenen seçenek var"))

        # Kopya ölçütü kök DEĞİL, kök + şık kümesidir. Genel kökler ("Aşağıdakilerden
        # hangisi ... değildir?") farklı şıklarla meşru olarak tekrar eder; yalnız köke
        # bakmak 16 pakette 43 sahte FATAL üretiyordu. Şıklar küme olarak alındığından
        # harf permütasyonuyla çoğaltılmış gerçek kopya da yakalanır.
        signature = (stem, frozenset(normalized))
        if signature in stems:
            issues.append(("FATAL", f"yinelenen soru (kök ve şıklar aynı): {qid}"))
        stems.add(signature)

        answer = question["answer"]
        if answer not in options:
            issues.append(("FATAL", f"{qid}: cevap seçeneklerde değil"))
        else:
            answers.append(answer)

        visible = f"{question['stem']} {question['solution']}"
        if DEMO.search(visible):
            issues.append(("FATAL", f"{qid}: kullanıcıya görünen demo ifadesi"))

        source = question.get("source")
        if not isinstance(source, dict) or not str(source.get("legislationRef", "")).strip():
            issues.append(("UYARI", f"{qid}: kaynak/dayanak eksik"))

    sequence = "".join(answers)
    if letter_pattern(sequence):
        issues.append(("FATAL", "cevap harflerinde kısa periyot/örüntü var"))
    if len(sequence) >= 20:
        counts = collections.Counter(sequence)
        expected = len(sequence) / 5
        if any(abs(counts[letter] - expected) > max(2, expected * 0.35) for letter in "ABCDE"):
            issues.append(("UYARI", f"cevap harfi dağılımı dengesiz: {dict(counts)}"))

    # Şıklardan sızan örüntü. Harf dizisi kusursuz olsa bile şıkların KENDİSİ
    # cevabı ele verebilir; eski dedektör yalnız "doğru şık en uzun mu" bakıp
    # bunu kaçırıyordu (Muhasebe Standartları'nda kör öğrenci %54 alıyordu).
    saglam = [q for q in questions
              if isinstance(q.get("options"), dict) and set(q.get("options", {})) == LETTERS
              and q.get("answer") in q.get("options", {})]
    if len(saglam) >= 20:
        kor, strateji = kor_ogrenci(saglam)
        if kor >= 35:
            issues.append(("FATAL", f"kör öğrenci soruyu okumadan %{kor} alıyor (taban %20) — "
                                    f"strateji: “{strateji}”"))
        elif kor >= 28:
            issues.append(("UYARI", f"kör öğrenci %{kor} alıyor (taban %20) — “{strateji}”"))

        uzun, kisa, olcum = boy_egilimi(saglam)
        if olcum >= 20 and max(uzun, kisa) >= 45:
            yon = "en UZUN" if uzun >= kisa else "en KISA"
            issues.append(("UYARI", f"boy ipucu: doğru şık %{max(uzun, kisa)} oranında {yon} "
                                    f"({olcum} öncüllü-olmayan soruda; hedef ~%20)"))

        # Aynı çeldiricinin dosya boyunca tekrarı ("bu husus standartta düzenlenmemiştir"
        # gibi atma-şıkları): her seferinde yanlış olduğu için tek başına öğrenilir.
        # Öncül seçicileri ("Yalnız I", "II ve III") meşru olarak tekrar eder — sayma.
        secici = re.compile(r"^(yalnız\s+)?(i{1,3}|iv|v)(\s*(,|ve)\s*(i{1,3}|iv|v))*$", re.I)
        celdirici = collections.Counter(
            re.sub(r"\s+", " ", v).strip().casefold()
            for q in saglam for k, v in q["options"].items()
            if k != q["answer"] and not secici.match(re.sub(r"\s+", " ", v).strip())
        )
        for metin, adet in celdirici.most_common(3):
            if adet >= max(6, len(saglam) * 0.15):
                issues.append(("UYARI", f"atma-şıkkı {adet} kez tekrarlanmış (hep yanlış): "
                                        f"“{metin[:58]}…”"))

    return len(questions), issues


def manifest_paths(path: str) -> list[str]:
    manifest = json.load(open(path, encoding="utf-8"))
    base = os.path.dirname(path)
    result = []
    for pack in manifest.get("packs", []):
        if "sgs" not in pack.get("programIds", []):
            continue
        candidates = (
            os.path.join(base, pack["file"]),
            os.path.join(os.path.dirname(base), pack["file"]),
        )
        existing = next((candidate for candidate in candidates if os.path.exists(candidate)), None)
        if existing:
            result.append(existing)
    return result


def main() -> int:
    args = sys.argv[1:]
    paths = [arg for arg in args if not arg.startswith("--")]
    if "--manifest" in args:
        if not paths:
            print("--manifest için manifest yolu gerekli.")
            return 2
        paths = manifest_paths(paths[0])
    if not paths:
        print(__doc__)
        return 2

    repo = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
    content = os.path.join(repo, "content")
    forbidden = os.path.join(content, "yeterlilik")
    totals = collections.Counter()
    for path in paths:
        resolved = os.path.realpath(path)
        if os.path.commonpath((content, resolved)) != content or os.path.commonpath((forbidden, resolved)) == forbidden:
            print(f"SGS kapsamı dışında dosya reddedildi: {path}")
            return 2
        count, issues = audit(path)
        severity = collections.Counter(level for level, _ in issues)
        totals.update(severity)
        flag = "❌" if severity["FATAL"] else ("⚠️" if severity["UYARI"] else "✅")
        print(f"{flag} {os.path.basename(path):48} {count:4} soru | FATAL {severity['FATAL']:3} UYARI {severity['UYARI']:3}")
        for level, message in issues[:20]:
            print(f"    [{level}] {message}")
    print(f"TOPLAM: FATAL {totals['FATAL']} | UYARI {totals['UYARI']}")
    return 1 if totals["FATAL"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
