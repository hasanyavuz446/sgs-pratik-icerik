#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SGS/SMMM Yeterlilik içerik kalite denetimi.

Kullanım:
    python3 tools/audit.py content/yeterlilik/questions_topic_*.json
    python3 tools/audit.py --manifest content/v2/manifest.json
    python3 tools/audit.py --manifest --all-programs content/v2/manifest.json

Araç iki şemayı da okuyabilir:
  SGS:         {ders, konu, stem, options, answer, solution}
  Yeterlilik:  {lessonId, topicId, question, choices, correctAnswer, explanation}

Başlıca kontroller:
  FATAL  şema/metadata       A-E, tekil şıklar, cevap, kaynak ve 2026 alanları
  FATAL  harf-örüntü        Rotasyon, sabit adım ve kısa periyot
  FATAL  cevap-uzunluk      Doğru cevabın sistematik en kısa/en uzun olması
  FATAL  tekrar             Birebir, sayı değişkenli şablon ve çözüm tekrarı
  FATAL  görünür-demo       Soru/çözümde Demo Soru veya Demo açıklama
  UYARI  şık-dengesi        Tek soruda doğal olmayan uzunluk farkı
  UYARI  kök-profili        Paket genelinde aşırı kısa ve çıplak kök yığılması
  UYARI  mevzuat-güncellik  Dönemsiz oran/had ve zayıf kaynak tanımı
  BİLGİ  hesap/ölçüm        İnsan incelemesi ve paket istatistikleri

Bu araç alan uzmanı değildir. Doğru cevabın hukuken/mesleki olarak doğruluğunu,
çeldiricilerin makullüğünü ve telif özgünlüğünü insan ayrıca denetler.
"""

import collections
import datetime as dt
import difflib
import itertools
import json
import os
import re
import statistics
import sys


LETTERS = set("ABCDE")
ROMAN = re.compile(r"(?m)^\s*\*{0,2}(VI|IV|V|III|II|I)[\.)]\s")
SOLUTION_LETTER = re.compile(
    r"\b(?:doğru\s+(?:cevap|seçenek|şık)|cevap)\s*[:\-]?\s*([A-E])\b",
    re.IGNORECASE,
)
VISIBLE_DEMO = re.compile(r"^\s*demo\s+(?:soru|açıklama)\s*:", re.IGNORECASE)
PLACEHOLDER = re.compile(
    r"<[^>]+>|\b(?:TODO|TBD|LOREM IPSUM)\b|\[\s*(?:DOLDUR|EKLE|TODO)\s*\]",
    re.IGNORECASE,
)
RATE = re.compile(r"%\s?\d+(?:[,.]\d+)?|\d+(?:[,.]\d+)?\s?%")
THRESHOLD = re.compile(
    r"istisna\s+(?:haddi|tutarı)|vergi\s+dilimi|asgari\s+ücret|"
    r"yeniden\s+değerleme\s+oranı|tarife",
    re.IGNORECASE,
)
IMPLICIT_CURRENT = re.compile(
    r"genel\s+oran|yürürlükteki\s+(?:oran|tutar|had)|geçerli\s+KDV\s+oranı|"
    r"cari\s+(?:oran|tutar|had)|bugünkü\s+(?:oran|tutar|had)",
    re.IGNORECASE,
)
EXPLICIT_YEAR = re.compile(r"\b20\d{2}\b")
CALCULATION = re.compile(r"\d[\d.]*\s?(?:TL|₺|lira|birim|adet|saat|gün)\b", re.I)
NUMERIC_CHOICE = re.compile(r"^[\s%₺TL\d.,+\-×x/:()]+$", re.IGNORECASE)

VOLATILE_LESSONS = {
    "vergi_hukuku",
    "vergi_usul_kanunu",
    "turk_vergi_sistemi",
    "gelir_vergisi",
    "kurumlar_vergisi",
    "katma_deger_vergisi",
    "ticaret_hukuku",
    "borclar_hukuku",
    "is_hukuku",
    "sosyal_guvenlik_mevzuati",
    "idari_yargilama_hukuku",
    "meslek_hukuku",
    "sermaye_piyasasi_ve_finans",
}


def load(path):
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    return data if isinstance(data, list) else data.get("questions", [])


def norm(raw):
    """İki JSON şemasını güvenli tek biçime indirger."""
    source = raw.get("source") if isinstance(raw.get("source"), dict) else {}
    opts = raw.get("choices") or raw.get("options") or {}
    is_yeterlilik = "question" in raw or "correctAnswer" in raw
    return {
        "raw": raw,
        "is_yeterlilik": is_yeterlilik,
        "id": raw.get("id"),
        "lesson": raw.get("lessonId") or raw.get("ders") or "",
        "topic": raw.get("topicId") or raw.get("konu") or "",
        "stem": raw.get("question") or raw.get("stem") or "",
        "opts": opts if isinstance(opts, dict) else {},
        "ans": raw.get("correctAnswer") or raw.get("answer"),
        "sol": raw.get("explanation") or raw.get("solution") or "",
        "tags": raw.get("tags") if isinstance(raw.get("tags"), list) else [],
        "source_kind": source.get("kind"),
        "source_ref": source.get("legislationRef") or "",
        "exam_period": raw.get("examPeriod") or "",
        "legislation_version": raw.get("legislationVersion") or "",
        "source_updated_at": raw.get("sourceUpdatedAt") or "",
    }


def plain(value):
    """Markdown vurgusunu kaldırıp ölçüm için düz metin döndürür."""
    return re.sub(r"[`*_]", "", str(value or "")).strip()


def text_key(value, *, template=False):
    value = plain(value).lower()
    if template:
        value = re.sub(r"\b\d[\d.,]*\b", " # ", value)
    return " ".join(re.findall(r"[\wçğıöşü#]+", value, flags=re.UNICODE))


def compact_key(value, *, template=False):
    return text_key(value, template=template).replace(" ", "")


def option_key(opts, *, template=False):
    return tuple(sorted(text_key(v, template=template) for v in opts.values()))


def full_key(q, *, template=False):
    return (text_key(q["stem"], template=template), option_key(q["opts"], template=template))


def combined_template(q):
    return " | ".join((text_key(q["stem"], template=True), *option_key(q["opts"], template=True)))


def token_jaccard(a, b):
    left, right = set(a.split()), set(b.split())
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def parse_iso_date(value):
    if not value:
        return None
    try:
        return dt.datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return False


def letter_pattern(seq):
    """Cevap anahtarındaki adayın fark edebileceği mekanik örüntüleri bulur."""
    issues = []
    if len(seq) < 10:
        return issues
    idx = ["ABCDE".index(char) for char in seq]

    steps = {(idx[i + 1] - idx[i]) % 5 for i in range(len(idx) - 1)}
    if len(steps) == 1:
        issues.append((
            "FATAL",
            "harf-örüntü",
            f"Doğru cevap dizisi sabit adımlı (adım={steps.pop()}): {seq[:15]}…",
        ))
        return issues

    for period in range(1, 11):
        match = sum(seq[i] == seq[i + period] for i in range(len(seq) - period))
        if match / (len(seq) - period) >= 0.90:
            issues.append((
                "FATAL",
                "harf-örüntü",
                f"Doğru cevap dizisi {period} periyotlu tekrar ediyor: {seq[:15]}…",
            ))
            return issues

    bigrams = {seq[i:i + 2] for i in range(len(seq) - 1)}
    if len(seq) >= 40 and len(bigrams) < 13:
        issues.append((
            "UYARI",
            "harf-örüntü",
            f"25 olası geçişten yalnız {len(bigrams)} farklı harf geçişi var.",
        ))
    return issues


def add_semantic_repeat_issues(qs, out):
    """Aynı dosyadaki çözüm, sayı şablonu ve yüksek benzerlik tekrarlarını arar."""
    seen_solution = {}
    seen_solution_template = {}
    seen_full_template = {}

    for q in qs:
        qid = q["id"] or "<idsiz>"
        solution = text_key(q["sol"])
        solution_template = text_key(q["sol"], template=True)
        template = full_key(q, template=True)
        exact_solution_repeat = solution in seen_solution

        if len(solution) >= 45:
            if exact_solution_repeat:
                out.append((
                    "FATAL",
                    "çözüm-tekrarı",
                    f"{qid}: çözüm {seen_solution[solution]} ile birebir aynı.",
                ))
            else:
                seen_solution[solution] = qid

        if len(solution_template) >= 60:
            previous = seen_solution_template.get(solution_template)
            if previous and not exact_solution_repeat:
                out.append((
                    "UYARI",
                    "çözüm-şablonu",
                    f"{qid}: çözüm yalnız sayı/tutar değiştirilerek {previous} ile aynı şablona düşüyor.",
                ))
            else:
                seen_solution_template[solution_template] = qid

        previous = seen_full_template.get(template)
        if previous:
            out.append((
                "FATAL",
                "soru-şablonu",
                f"{qid}: kök ve şık yapısı yalnız sayı değişimiyle {previous} ile aynı.",
            ))
        else:
            seen_full_template[template] = qid

    # Yüksek benzerlik pahalıdır; aynı ders/konu içinde ve makul metinlerde çalıştırılır.
    for left_index, left in enumerate(qs):
        left_text = combined_template(left)
        if len(left_text) < 100:
            continue
        for right in qs[left_index + 1:]:
            if (left["lesson"], left["topic"]) != (right["lesson"], right["topic"]):
                continue
            if full_key(left, template=True) == full_key(right, template=True):
                # Yüksek güvenli sayı-şablonu denetimi bu çifti zaten FATAL yaptı.
                continue
            right_text = combined_template(right)
            if len(right_text) < 100:
                continue
            jaccard = token_jaccard(left_text, right_text)
            if jaccard < 0.80:
                continue
            ratio = difflib.SequenceMatcher(None, left_text, right_text, autojunk=False).ratio()
            if ratio < 0.90:
                continue
            if ratio >= 0.97 and jaccard >= 0.90:
                out.append((
                    "FATAL",
                    "yakın-tekrar",
                    f"{right['id']}: {left['id']} ile çok yüksek benzerlik "
                    f"(dizi %{ratio*100:.0f}, sözcük %{jaccard*100:.0f}).",
                ))
            elif jaccard >= 0.80:
                out.append((
                    "UYARI",
                    "yakın-tekrar",
                    f"{right['id']}: {left['id']} ile yüksek benzerlik "
                    f"(dizi %{ratio*100:.0f}, sözcük %{jaccard*100:.0f}); elle karşılaştır.",
                ))


def add_length_profile_issues(rows, out):
    """Doğru cevabın uzunluğundan tahmin edilmesini paket düzeyinde engeller."""
    if not rows:
        return

    unique_shortest = 0
    unique_longest = 0
    ranks = []
    for qid, lengths, answer in rows:
        values = list(lengths.values())
        correct = lengths[answer]
        if values.count(min(values)) == 1 and correct == min(values):
            unique_shortest += 1
            second = sorted(values)[1]
            if second - correct >= 25 and second >= max(1, correct) * 1.5:
                out.append((
                    "UYARI",
                    "şık-ipucu",
                    f"{qid}: doğru şık belirgin biçimde tek en kısa ({correct}/{second} karakter).",
                ))
        if values.count(max(values)) == 1 and correct == max(values):
            unique_longest += 1
            second = sorted(values, reverse=True)[1]
            if correct - second >= 25 and correct >= max(1, second) * 1.5:
                out.append((
                    "UYARI",
                    "şık-ipucu",
                    f"{qid}: doğru şık belirgin biçimde tek en uzun ({correct}/{second} karakter).",
                ))

        below = sum(value < correct for value in values)
        equal = sum(value == correct for value in values)
        ranks.append(below + (equal + 1) / 2)

    count = len(rows)
    shortest_rate = unique_shortest / count
    longest_rate = unique_longest / count
    mean_rank = statistics.mean(ranks)
    out.append((
        "BİLGİ",
        "şık-ölçümü",
        f"ölçülen {count} soruda doğru tek-en-kısa %{shortest_rate*100:.1f}, "
        f"tek-en-uzun %{longest_rate*100:.1f}, ortalama uzunluk sırası {mean_rank:.2f}/5.",
    ))

    if count < 15:
        return

    for rate, label in ((shortest_rate, "en kısa"), (longest_rate, "en uzun")):
        if rate > 0.40:
            out.append((
                "FATAL",
                "cevap-uzunluk",
                f"Doğru cevap %{rate*100:.1f} oranında tek {label}; uzunluk cevap anahtarını ele veriyor.",
            ))
        elif rate > 0.25:
            out.append((
                "UYARI",
                "cevap-uzunluk",
                f"Doğru cevap %{rate*100:.1f} oranında tek {label}; yönsel kalıbı azalt.",
            ))

    if mean_rank < 2.0 or mean_rank > 4.0:
        out.append((
            "FATAL",
            "cevap-uzunluk",
            f"Doğru cevapların ortalama uzunluk sırası {mean_rank:.2f}/5; belirgin yönsel kalıp var.",
        ))
    elif mean_rank < 2.4 or mean_rank > 3.6:
        out.append((
            "UYARI",
            "cevap-uzunluk",
            f"Doğru cevapların ortalama uzunluk sırası {mean_rank:.2f}/5; 3 çevresinde dengelenmeli.",
        ))


def audit(path):
    qs = [norm(raw) for raw in load(path)]
    out = []
    seen_ids = {}
    seen_stems = {}
    seen_full = {}
    length_rows = []
    stem_lengths = []
    legacy_demo_ids = []
    legacy_solution_letter_ids = []

    for q in qs:
        qid = q["id"] or "<idsiz>"
        opts = q["opts"]

        # Temel şema
        if not isinstance(q["id"], str) or not q["id"].strip():
            out.append(("FATAL", "şema", "Soru kimliği boş veya metin değil."))
        elif q["id"] in seen_ids:
            out.append(("FATAL", "şema", f"{qid}: id {seen_ids[q['id']]} ile tekrarlanıyor."))
        else:
            seen_ids[q["id"]] = qid

        if not isinstance(q["stem"], str) or not q["stem"].strip():
            out.append(("FATAL", "şema", f"{qid}: soru kökü boş."))
        if set(opts) != LETTERS:
            out.append(("FATAL", "şema", f"{qid}: şıklar A-E değil ({sorted(opts)})."))
        if q["ans"] not in opts:
            out.append(("FATAL", "şema", f"{qid}: doğru cevap mevcut şıklardan biri değil."))

        option_values = []
        for key, value in opts.items():
            if not isinstance(value, str) or not value.strip():
                out.append(("FATAL", "şema", f"{qid}: {key} şıkkı boş veya metin değil."))
            else:
                option_values.append(text_key(value))
        if len(option_values) != len(set(option_values)):
            out.append(("FATAL", "şema", f"{qid}: aynı metni taşıyan birden fazla şık var."))

        if not isinstance(q["sol"], str) or not q["sol"].strip():
            out.append(("FATAL", "şema", f"{qid}: çözüm boş."))
        elif len(plain(q["sol"])) < 35:
            out.append(("UYARI", "çözüm", f"{qid}: çözüm çok kısa; gerekçeyi kontrol et."))

        stem_key = text_key(q["stem"])
        if stem_key in seen_stems:
            out.append((
                "FATAL",
                "kök-tekrarı",
                f"{qid}: kök {seen_stems[stem_key]} ile aynı.",
            ))
        else:
            seen_stems[stem_key] = qid

        exact = full_key(q)
        if exact in seen_full:
            out.append((
                "FATAL",
                "soru-tekrarı",
                f"{qid}: {seen_full[exact]} ile birebir aynı soru.",
            ))
        else:
            seen_full[exact] = qid

        # Görünür üretim artıkları
        if VISIBLE_DEMO.search(q["stem"]) or VISIBLE_DEMO.search(q["sol"]):
            out.append((
                "FATAL",
                "görünür-demo",
                f"{qid}: kullanıcı metninde Demo Soru/Demo açıklama bulunuyor.",
            ))
        if "Demo Soru" in q["tags"]:
            legacy_demo_ids.append(qid)
        for field_name, value in (("kök", q["stem"]), ("çözüm", q["sol"])):
            if PLACEHOLDER.search(value):
                out.append(("FATAL", "şablon-artığı", f"{qid}: {field_name} yer tutucu içeriyor."))

        # Çözüm harften bağımsız olmalı.
        match = SOLUTION_LETTER.search(q["sol"])
        if match:
            mentioned = match.group(1).upper()
            if q["is_yeterlilik"] or mentioned != q["ans"]:
                detail = "Yeterlilik çözümü harften bağımsız olmalı"
                if not q["is_yeterlilik"] and mentioned != q["ans"]:
                    detail = f"çözüm {mentioned}, cevap anahtarı {q['ans']} diyor"
                out.append(("FATAL", "çözüm-harf", f"{qid}: {detail}."))
            else:
                legacy_solution_letter_ids.append(qid)

        # Kaynak ve 2026 metadata sözleşmesi
        if q["is_yeterlilik"]:
            if q["source_kind"] != "generated":
                out.append((
                    "FATAL",
                    "kaynak",
                    f"{qid}: source.kind 'generated' olmalı ({q['source_kind']!r}).",
                ))
            if not str(q["source_ref"]).strip():
                out.append(("FATAL", "kaynak", f"{qid}: source.legislationRef boş."))
            elif len(text_key(q["source_ref"])) < 7:
                out.append(("UYARI", "kaynak", f"{qid}: mevzuat/standart dayanağı fazla genel."))
            if not str(q["legislation_version"]).strip():
                out.append(("FATAL", "kaynak", f"{qid}: legislationVersion boş."))

        if "2026 Formatı" in q["tags"]:
            if not str(q["exam_period"]).strip():
                out.append(("FATAL", "metadata", f"{qid}: examPeriod boş."))
            parsed = parse_iso_date(q["source_updated_at"])
            if parsed is None:
                out.append(("FATAL", "metadata", f"{qid}: sourceUpdatedAt boş."))
            elif parsed is False:
                out.append(("FATAL", "metadata", f"{qid}: sourceUpdatedAt geçerli ISO tarih değil."))
            else:
                today = dt.datetime.now(dt.timezone.utc) + dt.timedelta(days=1)
                comparable = parsed if parsed.tzinfo else parsed.replace(tzinfo=dt.timezone.utc)
                if comparable > today:
                    out.append(("FATAL", "metadata", f"{qid}: sourceUpdatedAt gelecekte."))

        if "Konu Havuzu" in q["tags"] and "Bölüm Havuzu" in q["tags"]:
            out.append(("FATAL", "havuz", f"{qid}: aynı anda konu ve bölüm havuzunda."))

        # Tek soru şık uzunluk dengesi ve paket profili için veri
        markers = ROMAN.findall(q["stem"])
        valid_lengths = q["ans"] in opts and all(isinstance(v, str) for v in opts.values())
        numeric_only = valid_lengths and all(NUMERIC_CHOICE.fullmatch(plain(v)) for v in opts.values())
        if valid_lengths and len(markers) < 2 and not numeric_only:
            lengths = {key: len(plain(value)) for key, value in opts.items()}
            values = list(lengths.values())
            median = statistics.median(values)
            if max(values) - min(values) >= 40 and max(values) > max(1, median) * 2.2:
                out.append((
                    "UYARI",
                    "şık-dengesi",
                    f"{qid}: seçenek uzunlukları doğal olmayan ölçüde ayrışıyor "
                    f"({min(values)}–{max(values)} karakter).",
                ))
            length_rows.append((qid, lengths, q["ans"]))

        if q["is_yeterlilik"]:
            stem_lengths.append(len(plain(q["stem"])))

        # Mevzuat güncelliği ve hesap işaretleri
        option_blob = " ".join(str(value) for value in opts.values())
        blob = f"{q['stem']} {option_blob}"
        if q["lesson"] in VOLATILE_LESSONS:
            asks_volatile_value = RATE.search(option_blob) or THRESHOLD.search(blob) or IMPLICIT_CURRENT.search(q["stem"])
            if asks_volatile_value and not EXPLICIT_YEAR.search(q["stem"]):
                out.append((
                    "UYARI",
                    "mevzuat-güncellik",
                    f"{qid}: değişebilen oran/had için soru kökünde açık dönem yok.",
                ))
        if CALCULATION.search(blob):
            out.append(("BİLGİ", "hesap", f"{qid}: aritmetik ve yuvarlama insan tarafından doğrulanmalı."))

    if legacy_demo_ids:
        out.append((
            "UYARI",
            "eski-demo-etiketi",
            f"{len(legacy_demo_ids)} soruda eski 'Demo Soru' etiketi var; "
            "yeni üretimde 'Özgün Soru' kullanılmalı.",
        ))
    if legacy_solution_letter_ids:
        out.append((
            "UYARI",
            "eski-çözüm-harfi",
            f"{len(legacy_solution_letter_ids)} SGS çözümünde cevap harfi var; "
            "yeni üretimde çözüm harften bağımsız olmalı.",
        ))

    add_semantic_repeat_issues(qs, out)
    add_length_profile_issues(length_rows, out)

    # Cevap anahtarı dağılımı
    seq = "".join(q["ans"] for q in qs if q["ans"] in LETTERS)
    out.extend(letter_pattern(seq))
    counts = collections.Counter(seq)
    target = len(seq) / 5 if seq else 0
    for key in "ABCDE":
        if target and abs(counts.get(key, 0) - target) > max(3, target * 0.55):
            out.append((
                "UYARI",
                "harf-dağılım",
                f"{key} harfi {counts.get(key, 0)} kez; beklenen denge yaklaşık {target:.1f}.",
            ))
    max_run = max((sum(1 for _ in group) for _, group in itertools.groupby(seq)), default=0)
    if max_run > 3:
        out.append(("UYARI", "harf-dağılım", f"Aynı doğru cevap harfi {max_run} kez art arda geliyor."))

    # Öncüllü soru biçimi; sabit kota dayatılmaz.
    premise_questions = [q for q in qs if len(ROMAN.findall(q["stem"])) >= 2]
    combinations = collections.Counter()
    for q in premise_questions:
        qid = q["id"] or "<idsiz>"
        marker_count = len(ROMAN.findall(q["stem"]))
        if not 3 <= marker_count <= 6:
            out.append(("UYARI", "öncüllü", f"{qid}: {marker_count} öncül var; 3–6 aralığını gözden geçir."))
        if "\n\n" not in q["stem"]:
            out.append(("UYARI", "öncüllü", f"{qid}: öncüller \\n\\n ile ayrılmamış."))
        if q["ans"] in q["opts"]:
            combinations[text_key(q["opts"][q["ans"]])] += 1
    if len(premise_questions) >= 4 and combinations:
        combination, count = combinations.most_common(1)[0]
        if count / len(premise_questions) > 0.50:
            out.append((
                "UYARI",
                "öncüllü",
                f"Aynı doğru öncül kombinasyonu {count}/{len(premise_questions)} kez kullanılmış: {combination!r}.",
            ))

    if len(stem_lengths) >= 20:
        median = statistics.median(stem_lengths)
        short_rate = sum(length < 80 for length in stem_lengths) / len(stem_lengths)
        out.append((
            "BİLGİ",
            "kök-ölçümü",
            f"medyan kök {median:.0f} karakter; 80 karakterden kısa kök %{short_rate*100:.1f}.",
        ))
        if median < 100 and short_rate > 0.45:
            out.append((
                "UYARI",
                "kök-profili",
                "Paket kısa/çıplak köklere yığılmış; sınav düzeyinde uygulama ve yorum görevlerini artır.",
            ))

    return len(qs), len(premise_questions), out


def manifest_paths(manifest_path, program_id="yeterlilik"):
    with open(manifest_path, encoding="utf-8") as handle:
        manifest = json.load(handle)
    base = os.path.dirname(manifest_path)
    result = []
    for pack in manifest.get("packs", []):
        if program_id and program_id not in pack.get("programIds", []):
            continue
        for candidate in (
            os.path.join(base, pack["file"]),
            os.path.join(os.path.dirname(base), pack["file"]),
        ):
            if os.path.exists(candidate):
                result.append(candidate)
                break
    return result


def cross_file_issues(paths):
    """Manifest denetiminde paketler arası birebir/şablon/çözüm tekrarını bulur."""
    seen_id = {}
    seen_exact = {}
    seen_template = {}
    seen_solution = {}
    issues = []
    emitted = set()

    def emit(code, qid, previous, current):
        key = (code, qid, previous, current)
        if key not in emitted:
            emitted.add(key)
            issues.append(("FATAL", code, f"{qid} ({current}) ↔ {previous}"))

    for path in paths:
        base = os.path.basename(path)
        for raw in load(path):
            q = norm(raw)
            qid = q["id"] or "<idsiz>"
            if qid in seen_id and seen_id[qid] != base:
                emit("dosyalar-arası-id", qid, seen_id[qid], base)
            else:
                seen_id[qid] = base

            exact = full_key(q)
            if exact in seen_exact and seen_exact[exact][1] != base:
                previous_id, previous_base = seen_exact[exact]
                emit("dosyalar-arası-soru", qid, f"{previous_id} ({previous_base})", base)
            else:
                seen_exact[exact] = (qid, base)

            template = full_key(q, template=True)
            if template in seen_template and seen_template[template][1] != base:
                previous_id, previous_base = seen_template[template]
                emit("dosyalar-arası-şablon", qid, f"{previous_id} ({previous_base})", base)
            else:
                seen_template[template] = (qid, base)

            solution = text_key(q["sol"])
            solution_scope = (q["lesson"], q["topic"], solution)
            if len(solution) >= 45 and solution_scope in seen_solution and seen_solution[solution_scope][1] != base:
                previous_id, previous_base = seen_solution[solution_scope]
                emit("dosyalar-arası-çözüm", qid, f"{previous_id} ({previous_base})", base)
            else:
                seen_solution[solution_scope] = (qid, base)
    return issues


def main():
    args = sys.argv[1:]
    paths = [arg for arg in args if not arg.startswith("--")]
    if "--manifest" in args:
        if not paths:
            print("--manifest için manifest yolu gerekli.")
            return 2
        program_id = None if "--all-programs" in args else "yeterlilik"
        paths = manifest_paths(paths[0], program_id=program_id)
    if not paths:
        print(__doc__)
        return 2

    grand = collections.Counter()
    fatal_files = []
    for path in paths:
        count, premise_count, issues = audit(path)
        severity = collections.Counter(issue[0] for issue in issues)
        grand.update(severity)
        name = os.path.basename(path)
        flag = "❌" if severity["FATAL"] else ("⚠️ " if severity["UYARI"] else "✅")
        print(
            f"{flag} {name:52} {count:4} soru | öncüllü {premise_count:2} | "
            f"FATAL {severity['FATAL']:3} UYARI {severity['UYARI']:4} BİLGİ {severity['BİLGİ']:4}"
        )
        if severity["FATAL"]:
            fatal_files.append(name)

        reportable = sorted(
            (issue for issue in issues if issue[0] in ("FATAL", "UYARI")),
            key=lambda issue: (0 if issue[0] == "FATAL" else 1, issue[1], issue[2]),
        )
        for level, code, message in reportable[:40]:
            print(f"      [{level}] {code}: {message}")
        if len(reportable) > 40:
            print(f"      … {len(reportable) - 40} ek FATAL/UYARI gösterilmedi.")

    cross = cross_file_issues(paths) if len(paths) > 1 else []
    if cross:
        print(f"\n❌ DOSYALAR ARASI: {len(cross)}")
        for level, code, message in cross[:40]:
            print(f"      [{level}] {code}: {message}")
        if len(cross) > 40:
            print(f"      … {len(cross) - 40} ek tekrar gösterilmedi.")
        grand.update(issue[0] for issue in cross)

    print(
        f"\nTOPLAM: FATAL {grand['FATAL']} | UYARI {grand['UYARI']} | BİLGİ {grand['BİLGİ']}"
    )
    if fatal_files:
        print("YAYINA GİDEMEZ:", ", ".join(fatal_files))
    return 1 if grand["FATAL"] else 0


if __name__ == "__main__":
    sys.exit(main())
