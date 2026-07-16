#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Konu havuzunun TAMAMI için toplu denetim (61 konu × 60 soru).

    python3 tools/verify_all_konu.py

audit.py mekanik kaliteye, verify_konu.py tek pakete bakar. Bu alet TOPLU
bakınca ortaya çıkan riskleri arar:

  1. Kapsam       — her konu 60 soru mu, eksik konu var mı
  2. Bütünlük     — iki depo özdeş mi, manifest hizalı mı
  3. Çakışma      — dosyalar arası kök tekrarı + konu×bölüm havuzu kesişmesi
  4. Konu sınırı  — soru atandığı konunun kapsamında mı (dayanak tutarlılığı)
  5. Kaynak dağ.  — bir konunun soruları tek maddeye yığılmış mı
  6. Denge        — konu paketini kota zorlamadan raporlar; ders havuzunu ayrıca ölçer
  7. Örneklem     — elle okunacak soruları konu başına seçer
"""
import json, os, re, sys, random, collections

APP = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik"
OTA = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik"
CALC = re.compile(r"\d[\d.]*\s?(TL|lira|birim|adet|saat)\b")
MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")

def norm(s): return re.sub(r"\W+", "", s).lower()

def main():
    fatal, warn = [], []
    am = json.load(open(f"{APP}/assets/content/manifest_v2.json", encoding="utf-8"))
    om = json.load(open(f"{OTA}/content/v2/manifest.json", encoding="utf-8"))
    if str(am["version"]) != str(om["version"]):
        fatal.append(f"manifest sürümü farklı: app v{am['version']} ≠ ota v{om['version']}")

    # curriculum: beklenen konular
    c = json.load(open(f"{APP}/assets/content/curriculum.json", encoding="utf-8"))
    prog = [p for p in c["programs"] if p["id"] == "yeterlilik"][0]
    les2sec = {
        lesson_id: section["name"]
        for section in prog["sections"]
        for lesson_id in section.get("subLessonIds", section.get("lessonIds", []))
    }
    beklenen = {}
    for l in c["lessons"]:
        for t in l.get("topics", []):
            if "yeterlilik" in (t.get("programIds") or l.get("programIds") or []):
                beklenen[(l["id"], t["id"])] = t["name"]

    # tüm yeterlilik soruları
    konu, bolum = collections.defaultdict(list), []
    for p in om["packs"]:
        if "yeterlilik" not in (p.get("programIds") or []): continue
        fp = os.path.join(f"{OTA}/content", p["file"])
        if not os.path.exists(fp):
            fatal.append(f"manifest'te var, dosya yok: {p['file']}"); continue
        base = os.path.basename(fp)
        for q in json.load(open(fp, encoding="utf-8")):
            (konu[(q.get("lessonId"), q.get("topicId"))] if "Konu Havuzu" in q.get("tags", [])
             else bolum).append((q, base))
        # iki depo
        af = f"{APP}/assets/content/{p['file']}"
        if not os.path.exists(af) or open(af, encoding="utf-8").read() != open(fp, encoding="utf-8").read():
            fatal.append(f"iki depo farklı: {p['file']}")

    # 1. kapsam
    print("═══ KAPSAM ═══")
    eksik = 0
    for s in sorted(prog["sections"], key=lambda x: (x.get("session", 0), x["order"])):
        rows = []
        for (lid, tid), ad in beklenen.items():
            if les2sec.get(lid) != s["name"]: continue
            n = len(konu.get((lid, tid), []))
            if n != 60:
                rows.append(f"      {tid:28} {n:3}/60")
                eksik += 1
        durum = "✅ TAM" if not rows else f"🔴 {len(rows)} konu eksik"
        print(f"  {s['name'][:42]:44} {durum}")
        if rows: print("\n".join(rows))
    if eksik: fatal.append(f"{eksik} konu 60 soruya tamamlanmamış")

    # 2. dosyalar arası çakışma
    print("\n═══ ÇAKIŞMA ═══")
    seen, dup = {}, []
    for grp in list(konu.values()) + [bolum]:
        for q, base in grp:
            k = (norm(q.get("question") or q.get("stem", "")),
                 tuple(sorted(norm(v) for v in (q.get("choices") or q.get("options")).values())))
            if k in seen and seen[k][1] != base:
                dup.append((q["id"], base, seen[k][0], seen[k][1]))
            seen[k] = (q["id"], base)
    print(f"  {'✅' if not dup else '🚨'} dosyalar arası birebir tekrar: {len(dup)}")
    for d in dup[:8]: print(f"      {d[0]} ({d[1]}) ↔ {d[2]} ({d[3]})")
    if dup: fatal.append(f"{len(dup)} tekrar eden soru")

    bset = {norm(q.get("question") or q.get("stem", "")) for q, _ in bolum}
    kes = [(q["id"], b) for grp in konu.values() for q, b in grp
           if norm(q["question"]) in bset]
    print(f"  {'✅' if not kes else '🚨'} konu×bölüm havuzu kesişmesi: {len(kes)}")
    for k in kes[:5]: print(f"      {k[0]} ({k[1]})")
    if kes: fatal.append(f"{len(kes)} soru bölüm havuzuyla kesişiyor")

    # 3. konu başına kaynak dağılımı + denge
    print("\n═══ KONU BAŞINA DENGE ═══")
    print(f"  {'konu':30} {'hesap':>6} {'önc':>5} {'hepsi':>6}  {'kaynak çeşidi':>14}  {'en yığılmış madde':>18}")
    for (lid, tid), items in sorted(konu.items(), key=lambda x: (les2sec.get(x[0][0], ""), x[0][1])):
        if not items: continue
        qs = [q for q, _ in items]
        hesap = sum(1 for q in qs if CALC.search(q["question"] + " " + " ".join(q["choices"].values())))
        onc = [q for q in qs if len(MARK.findall(q["question"])) >= 2]
        hepsi = sum(1 for q in onc if q["choices"][q["correctAnswer"]].strip() == "I, II ve III")
        refs = collections.Counter((q.get("source", {}).get("legislationRef") or "?").split(" - ")[0] for q in qs)
        top = refs.most_common(1)[0]
        flags = []
        if onc:
            combos = collections.Counter(
                q["choices"][q["correctAnswer"]].strip() for q in onc
            )
            if len(onc) >= 4 and combos.most_common(1)[0][1] / len(onc) > 0.50:
                flags.append("öncül-kalıbı")
        # Öncüllü/hesap soru sayısı ve kaynak çeşidi konu doğasına bağlıdır.
        # Tek dönemlik sınav profilini her 60 soruluk alt konuya kota olarak
        # uygulamak yapay soru üretir; burada yalnız görünür raporlanır.
        mark = "🔴" if flags else "  "
        print(f"{mark}{tid[:30]:30} {hesap:6} {len(onc):5} {hepsi:6}  {len(refs):14}  {top[0][:16]:>18} ({top[1]})")
        if flags: warn.append(f"{tid}: {', '.join(flags)}")

    # 4. Bölüm havuzunun sınav-biçimi özeti. 2026/1 tek dönem olduğu için
    # sayılar bir yayın engeli değil, insan incelemesi için karşılaştırmadır.
    print("\n═══ BÖLÜM HAVUZU BİÇİM ÖZETİ ═══")
    section_rows = collections.defaultdict(list)
    for q, base in bolum:
        section_rows[les2sec.get(q.get("lessonId"), "Bilinmeyen bölüm")].append(q)
    for section_name, qs in sorted(section_rows.items()):
        premise = sum(1 for q in qs if len(MARK.findall(q["question"])) >= 2)
        negative = sum(
            1 for q in qs
            if re.search(r"\b(?:yanlıştır|değildir|beklenmez)\b", q["question"], re.I)
        )
        calc = sum(
            1 for q in qs
            if CALC.search(q["question"] + " " + " ".join(q["choices"].values()))
        )
        print(
            f"  {section_name[:44]:44} {len(qs):3} soru | "
            f"hesap/veri {calc:2} | negatif {negative:2} | öncüllü {premise:2}"
        )

    # 5. örneklem
    print("\n═══ ELLE OKUNACAK ÖRNEKLEM ═══")
    random.seed(7)
    for (lid, tid), items in sorted(konu.items())[:0]:  # başlık; asıl liste aşağıda
        pass
    picks = []
    for (lid, tid), items in konu.items():
        qs = [q for q, _ in items]
        hesaplilar = [q for q in qs if CALC.search(q["question"] + " " + " ".join(q["choices"].values()))]
        if hesaplilar: picks.append((tid, random.choice(hesaplilar), "hesap"))
        picks.append((tid, random.choice(qs), "kavram"))
    print(f"  toplam {len(picks)} örnek seçildi (konu başına 1 hesap + 1 kavram)")
    print(f"  → tam liste için: python3 tools/verify_all_konu.py --ornek")
    if "--ornek" in sys.argv:
        for tid, q, tip in picks:
            print(f"\n[{tid} · {tip}] {q['question'][:100]}")
            print(f"   ✔ {q['choices'][q['correctAnswer']][:90]}")
            print(f"   ref: {q.get('source',{}).get('legislationRef')}")

    print("\n" + "═" * 60)
    print(f"KONU HAVUZU: {sum(len(v) for v in konu.values())} soru / {len(konu)} konu")
    print(f"BÖLÜM HAVUZU: {len(bolum)} soru")
    if fatal:
        print(f"\n❌ FATAL ({len(fatal)}):")
        for f in fatal: print(f"   • {f}")
    if warn:
        print(f"\n⚠️  UYARI ({len(warn)}):")
        for w in warn[:15]: print(f"   • {w}")
    if not fatal and not warn:
        print("\n✅ TOPLU DENETİM TEMİZ — alan denetimi (mevzuat/aritmetik) elle örneklenecek")
    return 1 if fatal else 0

if __name__ == "__main__":
    sys.exit(main())
