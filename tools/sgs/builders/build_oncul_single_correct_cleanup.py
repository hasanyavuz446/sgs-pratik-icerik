#!/usr/bin/env python3
"""SGS öncüllü soru örüntüsü için izlenebilir içerik düzeltmeleri.

Bu dosya yeni soru üretmez. Denetimde ``Yalnız I/II/III`` seçeneği bulunduğu
halde tek öncüllü doğru cevabı olmayan eski paketlerde, uzman incelemesiyle
seçilen soruları günceller. Her yama eski değeri de taşıdığı için yanlış dosyaya
veya daha sonra değişmiş içeriğe sessizce uygulanamaz.

Kullanım:
    python3 tools/sgs/builders/build_oncul_single_correct_cleanup.py --check
    python3 tools/sgs/builders/build_oncul_single_correct_cleanup.py --write

⚠️ SAHIPLIK DEVRI: maliye/kamu_maliyesi_temel.json bloku bu dosyadan CIKARILDI; sahiplik
build_maliye_temel_yeniden.py dosyasina gecti. Bir sorunun tek sahibi olmali.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]

PATCHES = {
    "content/mali_tablolar_analizi/fon_akim_analizi.json": {
        "mta-fon-gen-0020": {
            "stem": (
                "Aşağıdaki işlemlerden hangileri fon KULLANIMIdır?\n\n"
                "I. Ortaklara temettü ödenmesi\n\n"
                "II. Nakit sermaye artırımı\n\n"
                "III. Uzun vadeli borçlanma yoluyla nakit sağlanması"
            ),
            "answer": "A",
            "solution": (
                "**I (temettü ödemesi)** işletmeden fon çıkışına yol açtığı için "
                "fon kullanımıdır. **II (nakit sermaye artırımı)** ve **III (uzun "
                "vadeli borçlanma)** ise işletmeye fon sağlayan kaynaklardır. "
                "Doğru cevap **Yalnız I**."
            ),
        },
    },
    "content/mali_tablolar_analizi/nakit_akim_analizi.json": {
        "mta-nakit-gen-0031": {
            "stem": (
                "Aşağıdaki nakit akışlarından hangileri YATIRIM faaliyeti "
                "kapsamındadır?\n\n"
                "I. Maddi duran varlık alımı için ödeme\n\n"
                "II. Ortaklara temettü ödemesi\n\n"
                "III. Mal satışından tahsilat"
            ),
            "answer": "A",
            "solution": (
                "**I (maddi duran varlık alımı)** yatırım faaliyetidir. "
                "**II (ortaklara temettü ödemesi)** finansman, **III (mal "
                "satışından tahsilat)** ise işletme faaliyetidir. Doğru cevap "
                "**Yalnız I**."
            ),
        },
    },
    "content/ekonomi/mikroekonomi.json": {
        "eko-mikro-gen-0020": {
            "stem": (
                "Esneklik ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\n"
                "I. Esneklik 1'den büyükse talep esnektir.\n\n"
                "II. Gelir esnekliği negatif olan mallar normal maldır.\n\n"
                "III. Çapraz esneklik pozitif olan mallar tamamlayıcı maldır."
            ),
            "answer": "A",
            "solution": (
                "**I doğrudur:** Talebin fiyat esnekliği 1'den büyükse talep "
                "esnektir. **II yanlıştır:** Gelir esnekliği negatif olan mallar "
                "düşük maldır. **III yanlıştır:** Pozitif çapraz esneklik ikame "
                "malları gösterir. Doğru cevap: **Yalnız I**."
            ),
        },
    },
    "content/ekonomi/makroekonomi.json": {
        "eko-makro-gen-0020": {
            "stem": (
                "Enflasyon ve fiyat hareketleri ile ilgili aşağıdaki ifadelerden "
                "hangileri doğrudur?\n\n"
                "I. Deflasyon genel fiyat düzeyinin düşmesidir.\n\n"
                "II. Dezenflasyon genel fiyat düzeyinin sürekli düşmesidir.\n\n"
                "III. Stagflasyon, yüksek büyüme ile düşük enflasyonun bir arada "
                "görülmesidir."
            ),
            "answer": "A",
            "solution": (
                "**I doğrudur:** Deflasyon genel fiyat düzeyindeki düşüştür. "
                "**II yanlıştır:** Dezenflasyon fiyatların düşmesi değil, enflasyon "
                "oranının gerilemesidir. **III yanlıştır:** Stagflasyon durgunluk "
                "ile enflasyonun birlikte görülmesidir. Doğru cevap: **Yalnız I**."
            ),
        },
    },
    "content/ekonomi/para_banka_dis_ekonomi.json": {
        "eko-para-gen-0025": {
            "stem": (
                "Para, banka ve dış ekonomi ile ilgili aşağıdaki ifadelerden "
                "hangileri doğrudur?\n\n"
                "I. Daraltıcı para politikası enflasyonla mücadelede "
                "kullanılabilir.\n\n"
                "II. Dalgalı kurda ulusal paranın piyasa koşullarıyla değer "
                "kaybetmesine devalüasyon denir.\n\n"
                "III. Genişletici para politikası para arzını azaltır."
            ),
            "answer": "A",
            "solution": (
                "**I doğrudur:** Daraltıcı para politikası toplam talebi ve "
                "enflasyon baskısını azaltmak için kullanılabilir. **II "
                "yanlıştır:** Devalüasyon sabit kur sistemindeki resmî değer "
                "düşürmedir; dalgalı kurdaki piyasa kaynaklı düşüş değer kaybıdır. "
                "**III yanlıştır:** Genişletici politika para arzını artırır. "
                "Doğru cevap: **Yalnız I**."
            ),
        },
    },
    "content/maliye/butce_maliye_politikasi.json": {
        "mal-butce-gen-0010": {
            "stem": (
                "Bütçe ve süreci ile ilgili aşağıdaki ifadelerden hangileri "
                "doğrudur?\n\n"
                "I. Bütçe belirli bir dönem için gelir-gider tahminlerini gösterir "
                "ve yürütmeye yetki verir.\n\n"
                "II. Bütçe süreci yalnızca hazırlık ve uygulama aşamalarından "
                "oluşur.\n\n"
                "III. Bütçenin görüşülüp kabul edilmesi yürütme organına aittir."
            ),
            "answer": "A",
            "solution": (
                "**I doğrudur:** Bütçe belirli bir dönem için gelir ve gider "
                "tahminlerini içerir ve yürütmeye yetki verir. **II yanlıştır:** "
                "Süreç hazırlık, görüşülüp onaylanma, uygulama ve denetim "
                "aşamalarını kapsar. **III yanlıştır:** Bütçeyi görüşüp kabul etme "
                "yetkisi yasama organına aittir. Doğru cevap: **Yalnız I**."
            ),
        },
    },
}


def load_questions(path: Path) -> tuple[dict | list, list[dict]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    return data, questions


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()

    mismatches: list[str] = []
    for relative_path, question_patches in PATCHES.items():
        path = ROOT / relative_path
        data, questions = load_questions(path)
        by_id = {question["id"]: question for question in questions}

        for question_id, fields in question_patches.items():
            if question_id not in by_id:
                raise SystemExit(f"Soru bulunamadı: {relative_path}::{question_id}")
            question = by_id[question_id]
            for field, expected in fields.items():
                if question.get(field) != expected:
                    mismatches.append(f"{relative_path}::{question_id}.{field}")
                    if args.write:
                        question[field] = expected

        if args.write:
            path.write_text(
                json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

    if args.check and mismatches:
        print("Bakım builder'ıyla eşleşmeyen alanlar:")
        for mismatch in mismatches:
            print(f"- {mismatch}")
        return 1

    print(f"{len(PATCHES)} paket / {sum(map(len, PATCHES.values()))} soru doğrulandı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
