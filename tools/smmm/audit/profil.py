#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM Yeterlilik sınav-sadakati ölçüleri.

Aynı ölçü fonksiyonları hem GERÇEK test kitapçıklarına hem havuzumuza uygulanır;
böylece "bizim soru gerçeğe benziyor mu" sorusu aynı cetvelle cevaplanır.

    python3 tools/smmm/audit/profil.py --hesapla <exams.json>   # bantlar.json'u yeniden üret
    python3 tools/smmm/audit/profil.py --karsilastir            # havuz ↔ gerçek tablo

`exams.json` telifli kitapçık metni içerir ve DEPOYA KONMAZ (yerel referans:
`Projects/Current/_referans/yeterlilik/`). Depoya yalnız ondan türetilen sayılar
(`bantlar.json`) girer.
"""

import collections
import glob
import json
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANTLAR = os.path.join(HERE, "bantlar.json")
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

# Uygulamadaki curriculum.json'un Yeterlilik bölümleri (sections[].subLessonIds).
BOLUM = {
    "finansal_muhasebe": "finansal_muhasebe",
    "maliyet_muhasebesi": "maliyet_muhasebesi",
    "yonetim_muhasebesi": "maliyet_muhasebesi",
    "ticaret_hukuku": "hukuk",
    "borclar_hukuku": "hukuk",
    "is_hukuku": "hukuk",
    "sosyal_guvenlik_mevzuati": "hukuk",
    "idari_yargilama_hukuku": "hukuk",
    "sermaye_piyasasi_ve_finans": "sermaye_piyasasi_mevzuati",
    "mali_tablolar_analizi": "finansal_tablolar_ve_analizi",
    "denetim": "muhasebe_denetimi",
    "vergi_usul_kanunu": "vergi_mevzuati_ve_uygulamasi",
    "vergi_hukuku": "vergi_mevzuati_ve_uygulamasi",
    "turk_vergi_sistemi": "vergi_mevzuati_ve_uygulamasi",
    "gelir_vergisi": "vergi_mevzuati_ve_uygulamasi",
    "kurumlar_vergisi": "vergi_mevzuati_ve_uygulamasi",
    "katma_deger_vergisi": "vergi_mevzuati_ve_uygulamasi",
    "meslek_hukuku": "meslek_hukuku",
}
BOLUM_ADI = {
    "finansal_muhasebe": "Finansal Muhasebe",
    "maliyet_muhasebesi": "Maliyet Muhasebesi",
    "hukuk": "Hukuk",
    "sermaye_piyasasi_mevzuati": "Sermaye Piyasası",
    "finansal_tablolar_ve_analizi": "Fin. Tablolar ve Analizi",
    "muhasebe_denetimi": "Muhasebe Denetimi",
    "vergi_mevzuati_ve_uygulamasi": "Vergi Mevzuatı",
    "meslek_hukuku": "Meslek Hukuku",
}

# Olumsuz kök: soru cümlesinin (son '?' öncesi) sonundaki olumsuz yüklem.
# Gerçek kitapçıklarda: "…biri değildir?", "…hangisi yanlıştır?", "…bakılmaz?",
# "…sayılmaz?", "…imkânı yoktur?", "…esaslı yanılma sayılmaz?".
OLUMSUZ = re.compile(
    r"(değildir|değil midir|yanlıştır|yanlış olur|yoktur|olamaz|söylenemez|mümkün değildir|"
    r"yanlış\s+\w+(?:mış|miş|muş|müş)t[ıiuü]r|"  # "…hangisinde yanlış verilmiştir?"
    # Türkçe olumsuz fiil sonları: -maz/-mez (sayılmaz, uygulanmaz, duyurulmaz),
    # -mamıştır/-memiştir (sayılmamıştır), -mamaktadır/-memektedir.
    r"\w+(?:ma|me)z|\w+(?:ma|me)(?:mış|miş)tır|\w+(?:ma|me)(?:mış|miş)tir|\w+(?:mamakta|memekte)d[ıi]r)"
    r"\s*\??\s*$",
    re.I,
)
# Mevzuat/standart atfı: "4857 sayılı İş Kanunu'na göre", "TMS 16'ya göre",
# "Bağımsız Denetim Yönetmeliği uyarınca", "TDS 320'ye göre".
ATIF = re.compile(
    r"\d{3,4}\s+sayılı|\b(?:Kanun|Yönetmeli[kğ]|Tebliğ|Yönerge|Esaslar|Standart|Tüzü[kğ]|"
    r"Kararname|KHK|Etik İlkeler)\w*|"
    r"\b(?:TMS|TFRS|TDS|BDS|KGK|SPK|VUK|GVK|KVK|KDVK|TTK|TBK|İYUK|THP|TDHP|MSUGT)\b",
)
HANGISI = re.compile(r"aşağıdaki(?:lerden)?\s+(?:\S+\s+){0,3}?hangi|ifadelerden hangi|hangisi(?:dir)?\b", re.I)
ONCUL = re.compile(r"(?m)^\s*\*{0,2}(VI|IV|V|III|II|I)[\.)]\s")
# THP hesap kodu + adı: "320 SATICILAR", "760 Pazarlama Satış ve Dağıtım Giderleri"
HESAP = re.compile(r"\b[1-7]\d\d\s+[A-ZÇĞİÖŞÜ][A-Za-zÇĞİÖŞÜçğıöşü]{2,}")
SAYI = re.compile(r"\d[\d.,]*")
SAYISAL_SIK = re.compile(r"^[\s%₺TL\d.,+\-−×x/:()]+(?:\s*(?:gün|ay|yıl|saat|kat|adet|hafta))?$", re.I)
TABLO = re.compile(r"(?m)^\s*\|.*\|\s*$")


def duz(value):
    return re.sub(r"\s+", " ", re.sub(r"[`*_]", "", str(value or ""))).strip()


def soru_cumlesi(stem):
    """Kökün son soru cümlesi (öncüllü sorularda öncüllerden sonra gelen kısım)."""
    s = duz(stem)
    parts = re.split(r"(?<=[.:])\s+", s)
    return parts[-1] if parts else s


def olc(stem, options, *, stimulus=None, stimulus_id=None):
    """Tek sorunun sınav-biçimi özellikleri. options: {harf: metin}."""
    s = duz(stem)
    opts = [duz(v) for v in options.values()]
    oncul_n = len(ONCUL.findall(str(stem))) or len(re.findall(r"(?:^|\s)(?:I|II|III|IV|V)\.\s", s))
    yevmiye = sum(len(HESAP.findall(o)) >= 2 for o in opts) >= 3
    return {
        "kok": len(s),
        "olumsuz": bool(OLUMSUZ.search(soru_cumlesi(s).rstrip("?").strip() + "?")) or bool(OLUMSUZ.search(s)),
        "atif": bool(ATIF.search(s)),
        "hangisi": bool(HANGISI.search(s)),
        "oncul": oncul_n >= 3,
        "oncul_n": oncul_n,
        "yevmiye": yevmiye,
        "sayisal_sik": all(SAYISAL_SIK.match(o) for o in opts),
        "veri": len(SAYI.findall(s)) >= 3 or bool(stimulus) or bool(stimulus_id) or bool(TABLO.search(str(stem))),
        "ortak_veri": bool(stimulus) or bool(stimulus_id),
        "sik": statistics.median(len(o) for o in opts) if opts else 0,
    }


ORAN_ALANLARI = ("olumsuz", "atif", "hangisi", "oncul", "yevmiye", "sayisal_sik", "veri")


def ozet(olcumler):
    n = len(olcumler)
    if not n:
        return {"n": 0}
    out = {"n": n,
           "kok_medyan": round(statistics.median(o["kok"] for o in olcumler)),
           "sik_medyan": round(statistics.median(o["sik"] for o in olcumler))}
    for alan in ORAN_ALANLARI:
        out[alan] = round(sum(o[alan] for o in olcumler) / n, 3)
    return out


def gercek_olcumler(exams_path):
    exams = json.load(open(exams_path, encoding="utf-8"))
    by = collections.defaultdict(list)
    for q in exams:
        by[q["section"]].append(olc(q["stem"], q["options"], stimulus=q.get("stimulus")))
    return by


def havuz_olcumler(root=REPO, *, havuz=None):
    """havuz: None=hepsi, 'konu' ya da 'bolum'."""
    by = collections.defaultdict(list)
    for path in sorted(glob.glob(os.path.join(root, "content", "yeterlilik", "*.json"))):
        if os.path.basename(path) == "stimuli.json":
            continue
        for q in json.load(open(path, encoding="utf-8")):
            if q.get("isActive") is False:
                continue
            konu = "Konu Havuzu" in (q.get("tags") or [])
            if havuz == "konu" and not konu or havuz == "bolum" and konu:
                continue
            bolum = BOLUM.get(q.get("lessonId"))
            if bolum:
                by[bolum].append(olc(q.get("question", ""), q.get("choices", {}), stimulus_id=q.get("stimulusId")))
    return by


def bantlari_hesapla(exams_path):
    by = gercek_olcumler(exams_path)
    exams = json.load(open(exams_path, encoding="utf-8"))
    donemler = sorted({q["period"] for q in exams})
    bant = {"kaynak": f"TESMER SMMM Yeterlilik test kitapçıkları {', '.join(donemler)}",
            "soru": len(exams), "bolumler": {}}
    for bolum, olcumler in sorted(by.items()):
        bant["bolumler"][bolum] = ozet(olcumler)
    json.dump(bant, open(BANTLAR, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"yazıldı: {BANTLAR} ({len(exams)} soru, {', '.join(donemler)})")


def yuzde(x):
    return f"{x*100:3.0f}"


def karsilastir(havuz=None):
    bant = json.load(open(BANTLAR, encoding="utf-8"))
    by = havuz_olcumler(havuz=havuz)
    alanlar = ("kok_medyan",) + ORAN_ALANLARI
    print(f"Gerçek: {bant['kaynak']} — hücre biçimi gerçek/havuz")
    print(f"{'bölüm':26} {'n':>9} " + " ".join(f"{a[:9]:>11}" for a in alanlar))
    for bolum, g in bant["bolumler"].items():
        h = ozet(by.get(bolum, []))
        hucre = []
        for a in alanlar:
            if a == "kok_medyan":
                hucre.append(f"{g[a]:>5}/{h.get(a, 0):<5}")
            else:
                hucre.append(f"{yuzde(g[a]):>5}/{yuzde(h.get(a, 0)):<5}")
        print(f"{BOLUM_ADI[bolum]:26} {g['n']:>4}/{h['n']:<4} " + " ".join(f"{c:>11}" for c in hucre))


if __name__ == "__main__":
    if "--hesapla" in sys.argv:
        bantlari_hesapla(sys.argv[sys.argv.index("--hesapla") + 1])
    else:
        havuz = "konu" if "--konu" in sys.argv else ("bolum" if "--bolum" in sys.argv else None)
        karsilastir(havuz)
