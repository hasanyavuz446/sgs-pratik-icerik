#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Maliyet Muhasebesi — çok adımlı (harder) kalibrasyon yamaları.

Tek-adımlı hesap sorularını ham veriden başlayan çok adımlı senaryolara dönüştürür
(katkı payı → başabaş/hedef kâr/güvenlik marjı/faaliyet kaldıracı; birleşik maliyette
satış değeri/NGD dağıtımı → birim/kâr, yan ürün, ilave işleme kararı, karşılaştırma,
ters-hesap). Aritmetik builder dışında bağımsız doğrulanmıştır. Kavram+öncüllü korunur;
ID'ler değişmez.  --check / --write
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
MHK_RELATIVE_PATH = "content/maliyet_muhasebesi/maliyet_hacim_kar.json"
BIRLESIK_RELATIVE_PATH = "content/maliyet_muhasebesi/birlesik_maliyet.json"
# gider_dagitimi.json -> build_mmuh_gider_dagitimi_tablolu.py (tek sahip)
SAFHA_RELATIVE_PATH = "content/maliyet_muhasebesi/safha_maliyeti.json"
# siparis_maliyeti.json -> build_siparis_maliyeti_onarim.py (tek sahip)
STANDART_RELATIVE_PATH = "content/maliyet_muhasebesi/standart_maliyet.json"
STYLE_REF = 'SGS Maliyet Muhasebesi (çok adımlı hesap; 2024-2026 sınav zorluğuna kalibre)'


def cost_patch(stem, options, answer, solution, legislation_ref):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF, "legislationRef": legislation_ref},
        "validYear": 2026, "mockExamId": None,
    }


MHK_HARDER_PATCHES = {
    'mmuh-mhk-gen-0007': cost_patch(
        "Bir işletme ürününü birim 150 ₺'ye satmakta; birim değişken maliyeti 90 ₺, aylık toplam sabit maliyeti 300.000 ₺'dir. Başabaş noktası satış miktarı kaç adettir?",
        {
            'A': '5.000',
            'B': '2.000',
            'C': '3.333',
            'D': '10.000',
            'E': '4.000',
        },
        'A',
        'Birim katkı payı = 150 − 90 = **60 ₺**. Başabaş miktar = Toplam sabit maliyet ÷ birim katkı payı = 300.000 ÷ 60 = **5.000 adet**. (Fiyata bölmek 2.000, değişkene bölmek 3.333 verir — ikisi de yanlış; bölen katkı payıdır.)',
        'Maliyet muhasebesi - başabaş (çok adımlı)',
    ),
    'mmuh-mhk-gen-0009': cost_patch(
        "Birim satış fiyatı 200 ₺, birim değişken maliyeti 120 ₺ ve toplam sabit maliyeti 480.000 ₺ olan bir işletmenin başabaş noktası satış TUTARI kaç ₺'dir?",
        {
            'A': '6.000',
            'B': '1.200.000',
            'C': '480.000',
            'D': '2.400.000',
            'E': '800.000',
        },
        'B',
        'Birim katkı payı = 200 − 120 = 80 ₺; katkı payı oranı = 80 ÷ 200 = %40. Başabaş tutar = Sabit maliyet ÷ katkı payı oranı = 480.000 ÷ 0,40 = **1.200.000 ₺**. (Başabaş adet = 480.000 ÷ 80 = 6.000; tutar = 6.000 × 200 = 1.200.000 ₺ ile aynı.)',
        'Maliyet muhasebesi - başabaş tutar (çok adımlı)',
    ),
    'mmuh-mhk-gen-0012': cost_patch(
        'Birim satış fiyatı 100 ₺, birim değişken maliyeti 60 ₺, toplam sabit maliyeti 200.000 ₺ olan bir işletme dönem sonunda 120.000 ₺ kâr hedeflemektedir. Bu hedef için satması gereken miktar kaç adettir?',
        {
            'A': '8.000',
            'B': '5.000',
            'C': '3.000',
            'D': '3.200',
            'E': '800.000',
        },
        'A',
        'Birim katkı payı = 100 − 60 = 40 ₺. Hedef kâr için miktar = (Sabit maliyet + Hedef kâr) ÷ katkı payı = (200.000 + 120.000) ÷ 40 = 320.000 ÷ 40 = **8.000 adet**. (Yalnız başabaş 5.000; yalnız kârı bölmek 3.000 verir.)',
        'Maliyet muhasebesi - hedef kâr (çok adımlı)',
    ),
    'mmuh-mhk-gen-0014': cost_patch(
        "Birim satış fiyatı 80 ₺, birim değişken maliyeti 50 ₺, toplam sabit maliyeti 150.000 ₺ olan bir işletme dönemde 8.000 adet satmıştır. Dönem kârı kaç ₺'dir?",
        {
            'A': '240.000',
            'B': '490.000',
            'C': '10.000',
            'D': '150.000',
            'E': '90.000',
        },
        'E',
        'Birim katkı payı = 80 − 50 = 30 ₺. Toplam katkı payı = 8.000 × 30 = 240.000 ₺. Kâr = Toplam katkı payı − Sabit maliyet = 240.000 − 150.000 = **90.000 ₺**. (Sabiti düşmemek 240.000; değişkeni ihmal edip 8.000 × 80 − 150.000 = 490.000 verir — ikisi de yanlış.)',
        'Maliyet muhasebesi - kâr (çok adımlı)',
    ),
    'mmuh-mhk-gen-0019': cost_patch(
        'Birim satış fiyatı 120 ₺, birim değişken maliyeti 80 ₺, toplam sabit maliyeti 320.000 ₺ olan bir işletme cari dönemde 12.000 adet satmıştır. Güvenlik marjı (adet) kaçtır?',
        {
            'A': '8.000',
            'B': '4.000',
            'C': '12.000',
            'D': '2.667',
            'E': '6.000',
        },
        'B',
        'Birim katkı payı = 120 − 80 = 40 ₺. Başabaş miktar = 320.000 ÷ 40 = 8.000 adet. Güvenlik marjı = Fiili satış − Başabaş satış = 12.000 − 8.000 = **4.000 adet**. (Başabaşın kendisi 8.000; fiili satış 12.000 değil.)',
        'Maliyet muhasebesi - güvenlik marjı (çok adımlı)',
    ),
    'mmuh-mhk-gen-0022': cost_patch(
        'Birim katkı payı 50 ₺, toplam sabit maliyeti 400.000 ₺ olan bir işletme, vergi oranının %20 olarak dikkate alınacağı bir dönemde vergi SONRASI 160.000 ₺ net kâr hedeflemektedir. Gereken satış miktarı kaç adettir?',
        {
            'A': '12.000',
            'B': '11.200',
            'C': '8.000',
            'D': '4.000',
            'E': '10.000',
        },
        'A',
        'Vergi öncesi (brüt) hedef kâr = Net kâr ÷ (1 − vergi oranı) = 160.000 ÷ 0,80 = 200.000 ₺. Gereken miktar = (Sabit + brüt kâr) ÷ katkı payı = (400.000 + 200.000) ÷ 50 = **12.000 adet**. (Vergiyi ihmal edip 160.000 kullanmak 11.200 verir — yanlış.)',
        'Maliyet muhasebesi - vergili hedef kâr (çok adımlı)',
    ),
    'mmuh-mhk-gen-0023': cost_patch(
        "Birim satış fiyatı 60 ₺, birim değişken maliyeti 36 ₺, toplam sabit maliyeti 180.000 ₺ olan bir işletme dönemde 10.000 adet satmıştır. Dönem kârı kaç ₺'dir?",
        {
            'A': '240.000',
            'B': '420.000',
            'C': '60.000',
            'D': '24.000',
            'E': '180.000',
        },
        'C',
        'Birim katkı payı = 60 − 36 = 24 ₺. Toplam katkı payı = 10.000 × 24 = 240.000 ₺. Kâr = 240.000 − 180.000 = **60.000 ₺**. (Sabiti düşmemek 240.000; değişkeni ihmal 600.000 − 180.000 = 420.000 verir.)',
        'Maliyet muhasebesi - kâr (çok adımlı)',
    ),
    'mmuh-mhk-gen-0027': cost_patch(
        "Birim satış fiyatı 250 ₺, birim değişken maliyeti 150 ₺, toplam sabit maliyeti 600.000 ₺ olan bir işletme 300.000 ₺ kâr hedeflemektedir. Gereken satış TUTARI kaç ₺'dir?",
        {
            'A': '9.000',
            'B': '2.250.000',
            'C': '1.500.000',
            'D': '900.000',
            'E': '3.750.000',
        },
        'B',
        "Birim katkı payı = 250 − 150 = 100 ₺; oran = 100 ÷ 250 = %40. Gereken tutar = (Sabit + Hedef kâr) ÷ katkı payı oranı = (600.000 + 300.000) ÷ 0,40 = **2.250.000 ₺**. (Yalnız başabaş tutarı 1.500.000 ₺'dir.)",
        'Maliyet muhasebesi - hedef kâr tutar (çok adımlı)',
    ),
    'mmuh-mhk-gen-0028': cost_patch(
        "Birim satış fiyatı 40 ₺, birim değişken maliyeti 24 ₺, toplam sabit maliyeti 240.000 ₺ olan bir işletme 120.000 ₺ kâr hedeflemektedir. Gereken satış TUTARI kaç ₺'dir?",
        {
            'A': '900.000',
            'B': '600.000',
            'C': '360.000',
            'D': '1.500.000',
            'E': '562.500',
        },
        'A',
        'Birim katkı payı = 40 − 24 = 16 ₺; oran = 16 ÷ 40 = %40. Gereken tutar = (Sabit + Hedef kâr) ÷ katkı payı oranı = (240.000 + 120.000) ÷ 0,40 = **900.000 ₺**. (Yalnız başabaş tutarı 240.000 ÷ 0,40 = 600.000.)',
        'Maliyet muhasebesi - hedef kâr tutar (çok adımlı)',
    ),
    'mmuh-mhk-gen-0032': cost_patch(
        "Birim satış fiyatı 100 ₺, birim değişken maliyeti 60 ₺, toplam sabit maliyeti 200.000 ₺ olan bir işletmede sabit maliyet 250.000 ₺'ye yükselmiştir. Diğer koşullar sabitken başabaş noktası satış miktarı kaç adet ARTAR?",
        {
            'A': '6.250',
            'B': '5.000',
            'C': '50.000',
            'D': '1.250',
            'E': '625',
        },
        'D',
        'Birim katkı payı = 100 − 60 = 40 ₺. Eski başabaş = 200.000 ÷ 40 = 5.000; yeni başabaş = 250.000 ÷ 40 = 6.250. Artış = 6.250 − 5.000 = **1.250 adet**. (6.250 yeni başabaşın kendisi, artış değil.)',
        'Maliyet muhasebesi - başabaş duyarlılık (çok adımlı)',
    ),
    'mmuh-mhk-gen-0037': cost_patch(
        "Bir ürünün satış fiyatı 200 ₺ ve katkı payı oranı %35'tir. İşletmenin toplam sabit maliyeti 490.000 ₺ olduğuna göre başabaş noktası satış miktarı kaç adettir?",
        {
            'A': '2.450',
            'B': '7.000',
            'C': '3.500',
            'D': '14.000',
            'E': '4.900',
        },
        'B',
        "Birim katkı payı = Fiyat × katkı payı oranı = 200 × %35 = 70 ₺. Başabaş miktar = 490.000 ÷ 70 = **7.000 adet**. (Fiyata bölmek 2.450 verir; katkı payı 70 ₺'dir.)",
        'Maliyet muhasebesi - başabaş (orandan; çok adımlı)',
    ),
    'mmuh-mhk-gen-0038': cost_patch(
        "Birim satış fiyatı 100 ₺, birim değişken maliyeti 60 ₺, toplam sabit maliyeti 240.000 ₺ olan bir işletmede birim değişken maliyet 68 ₺'ye yükselmiştir. Diğer koşullar sabitken yeni başabaş noktası satış miktarı kaç adettir?",
        {
            'A': '6.000',
            'B': '1.500',
            'C': '3.529',
            'D': '8.000',
            'E': '7.500',
        },
        'E',
        'Yeni birim katkı payı = 100 − 68 = 32 ₺ (eskisi 40 ₺ idi). Yeni başabaş miktar = 240.000 ÷ 32 = **7.500 adet**. (Eski başabaş 240.000 ÷ 40 = 6.000 idi; değişken maliyet artışı katkı payını düşürüp başabaşı yükseltir.)',
        'Maliyet muhasebesi - başabaş duyarlılık (çok adımlı)',
    ),
    'mmuh-mhk-gen-0039': cost_patch(
        "Bir işletme ürününü birim 150 ₺'ye satmakta ve toplam sabit maliyeti 300.000 ₺'dir. Dönemde 6.000 adet satıp 60.000 ₺ kâr elde ettiğine göre ürünün birim değişken maliyeti kaç ₺'dir?",
        {
            'A': '90',
            'B': '60',
            'C': '100',
            'D': '110',
            'E': '50',
        },
        'A',
        'Kâr = Toplam katkı payı − Sabit maliyet olduğundan toplam katkı payı = 60.000 + 300.000 = 360.000 ₺. Birim katkı payı = 360.000 ÷ 6.000 = 60 ₺. Birim değişken maliyet = Satış fiyatı − katkı payı = 150 − 60 = **90 ₺**.',
        'Maliyet muhasebesi - birim değişken (ters; çok adımlı)',
    ),
    'mmuh-mhk-gen-0042': cost_patch(
        'Birim satış fiyatı 50 ₺, birim değişken maliyeti 30 ₺, toplam sabit maliyeti 240.000 ₺ olan bir işletme dönemde 16.000 adet satmıştır. Güvenlik marjı ORANI yüzde kaçtır?',
        {
            'A': '%75',
            'B': '%33,33',
            'C': '%25',
            'D': '%20',
            'E': '%40',
        },
        'C',
        "Birim katkı payı = 50 − 30 = 20 ₺. Başabaş = 240.000 ÷ 20 = 12.000 adet. Güvenlik marjı = 16.000 − 12.000 = 4.000 adet; oran = 4.000 ÷ 16.000 = **%25**. (Başabaşın satışa oranı %75'tir, güvenlik marjı değil.)",
        'Maliyet muhasebesi - güvenlik marjı oranı (çok adımlı)',
    ),
    'mmuh-mhk-gen-0044': cost_patch(
        "Bir işletmenin başabaş noktası 5.000 adet, birim katkı payı 10 ₺'dir. İşletme dönemde başabaş noktasının 3.000 adet üzerinde (toplam 8.000 adet) satış yapmıştır. Dönem kârı kaç ₺'dir?",
        {
            'A': '80.000',
            'B': '30.000',
            'C': '50.000',
            'D': '3.000',
            'E': '20.000',
        },
        'B',
        'Başabaş noktasından sonraki her birimin katkı payı doğrudan kâra dönüşür (sabit maliyet zaten karşılanmıştır). Kâr = Başabaş üzeri miktar × birim katkı payı = 3.000 × 10 = **30.000 ₺**.',
        'Maliyet muhasebesi - güvenlik marjı × katkı payı (çok adımlı)',
    ),
    'mmuh-mhk-gen-0046': cost_patch(
        "Bir işletmenin dönem toplam katkı payı 360.000 ₺, dönem kârı ise 60.000 ₺'dir. İşletmenin faaliyet (çalışma) kaldıracı derecesi kaçtır?",
        {
            'A': '5',
            'B': '0,17',
            'C': '420.000',
            'D': '6',
            'E': '300.000',
        },
        'D',
        'Faaliyet kaldıracı derecesi = Toplam katkı payı ÷ Kâr = 360.000 ÷ 60.000 = **6**. Yani satışlar %1 arttığında kâr yaklaşık %6 artar; kaldıraç, kârın satış değişimine duyarlılığını gösterir.',
        'Maliyet muhasebesi - faaliyet kaldıracı (çok adımlı)',
    ),
    'mmuh-mhk-gen-0049': cost_patch(
        "Katkı payı oranı %40, toplam sabit maliyeti 480.000 ₺ olan bir işletme, vergi oranının %25 dikkate alınacağı bir dönemde vergi SONRASI 270.000 ₺ net kâr hedeflemektedir. Gereken satış TUTARI kaç ₺'dir?",
        {
            'A': '2.100.000',
            'B': '1.875.000',
            'C': '1.200.000',
            'D': '900.000',
            'E': '2.400.000',
        },
        'A',
        'Vergi öncesi kâr = 270.000 ÷ (1 − 0,25) = 270.000 ÷ 0,75 = 360.000 ₺. Gereken tutar = (Sabit + brüt kâr) ÷ katkı payı oranı = (480.000 + 360.000) ÷ 0,40 = **2.100.000 ₺**. (Vergiyi ihmal edip 270.000 kullanmak 1.875.000 verir.)',
        'Maliyet muhasebesi - vergili hedef kâr tutar (çok adımlı)',
    ),
    'mmuh-mhk-gen-0051': cost_patch(
        "Bir işletmenin katkı payı oranı %20 ve başabaş noktası satış TUTARI 600.000 ₺'dir. Buna göre işletmenin toplam sabit maliyeti kaç ₺'dir?",
        {
            'A': '600.000',
            'B': '120.000',
            'C': '3.000.000',
            'D': '480.000',
            'E': '150.000',
        },
        'B',
        'Başabaş tutar = Sabit maliyet ÷ katkı payı oranı olduğundan Sabit maliyet = Başabaş tutar × katkı payı oranı = 600.000 × 0,20 = **120.000 ₺**. (Oranı bölmek 3.000.000 verir — ters işlem, yanlış.)',
        'Maliyet muhasebesi - sabit maliyet (ters; çok adımlı)',
    ),
    'mmuh-mhk-gen-0052': cost_patch(
        "Birim satış fiyatı 100 ₺, birim değişken maliyeti 76 ₺, toplam sabit maliyeti 120.000 ₺ olan bir işletme dönemde 8.000 adet satmıştır. Dönem kârı kaç ₺'dir?",
        {
            'A': '192.000',
            'B': '680.000',
            'C': '24.000',
            'D': '120.000',
            'E': '72.000',
        },
        'E',
        'Birim katkı payı = 100 − 76 = 24 ₺. Toplam katkı payı = 8.000 × 24 = 192.000 ₺. Kâr = 192.000 − 120.000 = **72.000 ₺**.',
        'Maliyet muhasebesi - kâr (çok adımlı)',
    ),
    'mmuh-mhk-gen-0057': cost_patch(
        'Birim satış fiyatı 90 ₺, birim değişken maliyeti 60 ₺, toplam sabit maliyeti 180.000 ₺ olan bir işletmenin başabaş noktası satış miktarı kaç adettir?',
        {
            'A': '2.000',
            'B': '3.000',
            'C': '6.000',
            'D': '12.000',
            'E': '5.000',
        },
        'C',
        'Birim katkı payı = 90 − 60 = 30 ₺. Başabaş miktar = 180.000 ÷ 30 = **6.000 adet**.',
        'Maliyet muhasebesi - başabaş (çok adımlı)',
    ),
    'mmuh-mhk-gen-0058': cost_patch(
        'Birim satış fiyatı 120 ₺, birim değişken maliyeti 90 ₺, toplam sabit maliyeti 180.000 ₺ olan bir işletme 90.000 ₺ kâr hedeflemektedir. Gereken satış miktarı kaç adettir?',
        {
            'A': '6.000',
            'B': '3.000',
            'C': '2.250',
            'D': '9.000',
            'E': '7.500',
        },
        'D',
        'Birim katkı payı = 120 − 90 = 30 ₺. Gereken miktar = (180.000 + 90.000) ÷ 30 = **9.000 adet**. (Yalnız başabaş 6.000.)',
        'Maliyet muhasebesi - hedef kâr (çok adımlı)',
    ),
}

PATCHES_BY_PATH = {
    MHK_RELATIVE_PATH: MHK_HARDER_PATCHES,
}


def apply_or_check(path, patches, write):
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    by_id = {q["id"]: q for q in questions}
    mismatches = []
    for qid, fields in patches.items():
        q = by_id.get(qid)
        if q is None:
            raise SystemExit(f"Soru bulunamadı: {path}::{qid}")
        for field, expected in fields.items():
            if q.get(field) != expected:
                mismatches.append(f"{path}::{qid}.{field}")
                if write:
                    q[field] = expected
        if write and len(set(q["options"].values())) != 5:
            raise SystemExit(f"Seçenek çakışması: {path}::{qid}")
    if write:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return mismatches


def main():
    ap = argparse.ArgumentParser(); g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true"); g.add_argument("--write", action="store_true")
    args = ap.parse_args()
    mismatches = []
    for rel, patches in PATCHES_BY_PATH.items():
        for path in (ROOT / rel, APP_ROOT / rel):
            mismatches.extend(apply_or_check(path, patches, args.write))
    if args.check and mismatches:
        print("Eşleşmeyen alanlar:")
        for m in mismatches: print(f"- {m}")
        return 1
    total = sum(len(p) for p in PATCHES_BY_PATH.values())
    print(f"{len(PATCHES_BY_PATH)} paket / {total} soru (harder) iki repoda doğrulandı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
