#!/usr/bin/env python3
"""SGS yakın-tekrar uyarıları için uzman incelemeli bakım yamaları.

Her kayıt, yalnız sayıları değiştirilmiş eski bir soruyu aynı kazanımı farklı
bir yönden ölçen soruya dönüştürür. ``--check`` yayımlanan içeriğin bu kaynakla
eşleştiğini doğrular; ``--write`` gerektiğinde yamaları yeniden uygular.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]

PATCHES = {
    "content/finansal_muhasebe/mali_duran_varliklar.json": {
        "finmuh-malidv-gen-0049": {
            "stem": "Bir işletme, başka bir şirketin finansal ve faaliyet politikalarına katılma gücüne sahip olmakla birlikte bu şirketi kontrol etmemektedir. Bu uzun vadeli yatırım Tekdüzen Hesap Planı'nda hangi hesapta izlenir?",
            "options": {
                "A": "242 İştirakler",
                "B": "245 Bağlı Ortaklıklar",
                "C": "240 Bağlı Menkul Kıymetler",
                "D": "110 Hisse Senetleri",
                "E": "500 Sermaye",
            },
            "answer": "A",
            "solution": "Başka bir işletmenin finansal ve faaliyet politikalarına katılma gücü önemli etkiyi gösterir. Kontrol bulunmayan bu uzun vadeli yatırım **242 İştirakler** hesabında izlenir.",
        },
        "finmuh-malidv-gen-0050": {
            "stem": "Bir işletme, başka bir şirketin oy haklarının %60'ını elde tutarak bu şirket üzerinde kontrol sağlamıştır. Bu yatırım hangi hesapta izlenir?",
            "options": {
                "A": "240 Bağlı Menkul Kıymetler",
                "B": "242 İştirakler",
                "C": "110 Hisse Senetleri",
                "D": "500 Sermaye",
                "E": "245 Bağlı Ortaklıklar",
            },
            "answer": "E",
            "solution": "Oy haklarının %60'ının elde tutulması kontrol gücü sağlar. Bu nedenle yatırım **245 Bağlı Ortaklıklar** hesabında izlenir.",
        },
    },
    "content/finansal_muhasebe/yabanci_kaynaklar.json": {
        "finmuh-yk-gen-0058": {
            "stem": "İşletme 1 Ekim'de yıllık %18 faizli, 600.000 ₺ tutarında dört ay vadeli banka kredisi kullanmıştır. 31 Aralık'ta üç aylık dönem için tahakkuk ettirilecek faiz kaç ₺'dir?",
            "options": {
                "A": "27.000",
                "B": "36.000",
                "C": "108.000",
                "D": "18.000",
                "E": "54.000",
            },
            "answer": "A",
            "solution": "Dönem sonuna kadar üç aylık faiz tahakkuk etmiştir: 600.000 × %18 × 3/12 = **27.000 ₺**.",
        },
    },
    "content/finansal_muhasebe/ozkaynaklar.json": {
        "finmuh-ozk-gen-0050": {
            "stem": "Ortaklarca taahhüt edilmiş ancak henüz ödenmemiş sermaye tutarı Tekdüzen Hesap Planı'nda hangi hesapta izlenir?",
            "options": {
                "A": "500 Sermaye",
                "B": "520 Hisse Senedi İhraç Primleri",
                "C": "540 Yasal Yedekler",
                "D": "590 Dönem Net Kârı",
                "E": "501 Ödenmemiş Sermaye (-)",
            },
            "answer": "E",
            "solution": "Taahhüt edildiği hâlde ortaklarca henüz ödenmemiş sermaye, özkaynakları azaltan **501 Ödenmemiş Sermaye (-)** hesabında izlenir.",
        },
    },
    "content/finansal_muhasebe/donem_sonu_islemleri.json": {
        "finmuh-dsi-gen-0042": {
            "stem": "Gelir ve gider hesaplarının devrinden sonra 690 Dönem Kârı veya Zararı hesabı 160.000 ₺ alacak kalanı vermiştir. Bu bakiye neyi gösterir?",
            "options": {
                "A": "160.000 ₺ vergi öncesi dönem zararı",
                "B": "600.000 ₺ brüt satış kârı",
                "C": "440.000 ₺ faaliyet gideri",
                "D": "Gelir ve giderlerin birbirine eşit olduğunu",
                "E": "160.000 ₺ vergi öncesi dönem kârı",
            },
            "answer": "E",
            "solution": "690 Dönem Kârı veya Zararı hesabının alacak kalanı, gelirlerin giderleri aştığını ve **160.000 ₺ vergi öncesi dönem kârı** oluştuğunu gösterir.",
        },
    },
    "content/mali_tablolar_analizi/trend_analizi.json": {
        "mta-trend-gen-0038": {
            "stem": "İlgili yılda tutarı 900.000 ₺ ve trend yüzdesi %150 olan bir kalemin baz yıl tutarı kaç ₺'dir?",
            "options": {
                "A": "750.000",
                "B": "600.000",
                "C": "1.350.000",
                "D": "150.000",
                "E": "900.000",
            },
            "answer": "B",
            "solution": "Baz yıl tutarı = İlgili yıl tutarı ÷ (Trend yüzdesi/100) = 900.000 ÷ 1,50 = **600.000 ₺**.",
        },
        "mta-trend-gen-0057": {
            "stem": "Bir kalemin baz yıl tutarı 800.000 ₺, ilgili yıldaki tutarı 1.000.000 ₺'dir. İlgili yılın trend yüzdesi kaçtır?",
            "options": {
                "A": "%125",
                "B": "%80",
                "C": "%25",
                "D": "%120",
                "E": "%150",
            },
            "answer": "A",
            "solution": "Trend yüzdesi = 1.000.000 ÷ 800.000 × 100 = **%125**.",
        },
    },
    "content/maliyet_muhasebesi/gider_dagitimi.json": {
        "mmuh-dagitim-gen-0051": {
            "stem": "200.000 ₺ tutarındaki kira gideri alanlara göre dağıtılacaktır (A: 250 m², B: 150 m², C: 100 m²). B gider yerinin dağıtım anahtarındaki payı yüzde kaçtır?",
            "options": {"A": "%50", "B": "%20", "C": "%30", "D": "%40", "E": "%60"},
            "answer": "C",
            "solution": "Toplam alan 250 + 150 + 100 = 500 m²'dir. B'nin payı = 150 ÷ 500 × 100 = **%30**.",
        },
    },
    "content/maliyet_muhasebesi/siparis_maliyeti.json": {
        "mmuh-siparis-gen-0050": {
            "stem": "130 no'lu siparişin direkt işçilik gideri 100.000 ₺'dir. Genel üretim giderleri direkt işçiliğin %60'ı oranında yükleniyorsa siparişe yüklenecek GÜG kaç ₺'dir?",
            "options": {"A": "60.000", "B": "100.000", "C": "160.000", "D": "200.000", "E": "360.000"},
            "answer": "A",
            "solution": "Yüklenecek genel üretim gideri = 100.000 × %60 = **60.000 ₺**.",
        },
    },
    "content/maliyet_muhasebesi/safha_maliyeti.json": {
        "mmuh-safha-gen-0012": {
            "stem": "Dönem sonu yarı mamulü 4.000 birim ve tamamlanma derecesi %50'dir. Dönem sonu yarı mamulün eşdeğer ürün miktarı kaç birimdir?",
            "options": {"A": "4.000", "B": "8.000", "C": "2.000", "D": "10.000", "E": "12.000"},
            "answer": "C",
            "solution": "Dönem sonu yarı mamulün eşdeğer ürün miktarı = 4.000 × %50 = **2.000 birim**.",
        },
        "mmuh-safha-gen-0013": {
            "stem": "Dönem sonu yarı mamulü 4.000 fiziksel birim, bunun eşdeğer ürün miktarı 1.000 birimdir. Tamamlanma derecesi yüzde kaçtır?",
            "options": {"A": "%25", "B": "%20", "C": "%40", "D": "%50", "E": "%75"},
            "answer": "A",
            "solution": "Tamamlanma derecesi = 1.000 eşdeğer birim ÷ 4.000 fiziksel birim × 100 = **%25**.",
        },
        "mmuh-safha-gen-0019": {
            "stem": "Dönem sonu yarı mamulün eşdeğer ürün miktarı 3.000 birim ve tamamlanma derecesi %50'dir. Dönem sonu yarı mamulün fiziksel miktarı kaç birimdir?",
            "options": {"A": "1.500", "B": "3.000", "C": "5.000", "D": "10.000", "E": "6.000"},
            "answer": "E",
            "solution": "Fiziksel miktar = 3.000 eşdeğer birim ÷ %50 = **6.000 birim**.",
        },
        "mmuh-safha-gen-0057": {
            "stem": "Eşdeğer birim maliyet 40 ₺ ve dönem sonu yarı mamulün eşdeğer ürün miktarı 2.000 birimdir. Dönem sonu yarı mamul maliyeti kaç ₺'dir?",
            "options": {"A": "720.000", "B": "800.000", "C": "40", "D": "2.000", "E": "80.000"},
            "answer": "E",
            "solution": "Dönem sonu yarı mamul maliyeti = 2.000 eşdeğer birim × 40 ₺ = **80.000 ₺**.",
        },
    },
    "content/maliyet_muhasebesi/standart_maliyet.json": {
        "mmuh-standart-gen-0017": {
            "stem": "Toplam direkt işçilik gideri sapması 6.200 ₺ aleyhte, standart direkt işçilik maliyeti 40.000 ₺'dir. Fiilî direkt işçilik maliyeti kaç ₺'dir?",
            "options": {"A": "46.200", "B": "33.800", "C": "40.000", "D": "6.200", "E": "53.200"},
            "answer": "A",
            "solution": "Aleyhte sapmada fiilî maliyet standart maliyetten yüksektir. Fiilî maliyet = 40.000 + 6.200 = **46.200 ₺**.",
        },
    },
    "content/denetim/denetim_riski.json": {
        "den-risk-gen-0031": {
            "stem": "Bir denetimde yapısal risk %100, kontrol riski %60 ve kabul edilebilir tespit riski %10'dur. Bu bileşenlere göre denetim riski yüzde kaçtır?",
            "options": {"A": "%6", "B": "%10", "C": "%16", "D": "%20", "E": "%60"},
            "answer": "A",
            "solution": "Denetim riski = Yapısal risk × Kontrol riski × Tespit riski = 1,00 × 0,60 × 0,10 = 0,06 = **%6**.",
        },
    },
}


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()

    mismatches: list[str] = []
    for relative_path, question_patches in PATCHES.items():
        path = ROOT / relative_path
        data = json.loads(path.read_text(encoding="utf-8"))
        questions = data["questions"] if isinstance(data, dict) else data
        by_id = {question["id"]: question for question in questions}
        for question_id, fields in question_patches.items():
            question = by_id.get(question_id)
            if question is None:
                raise SystemExit(f"Soru bulunamadı: {relative_path}::{question_id}")
            for field, expected in fields.items():
                if question.get(field) != expected:
                    mismatches.append(f"{relative_path}::{question_id}.{field}")
                    if args.write:
                        question[field] = expected
        if args.write:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if args.check and mismatches:
        print("Bakım builder'ıyla eşleşmeyen alanlar:")
        for mismatch in mismatches:
            print(f"- {mismatch}")
        return 1
    print(f"{len(PATCHES)} paket / {sum(map(len, PATCHES.values()))} soru doğrulandı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
