#!/usr/bin/env python3
"""SGS hukuk ve mevzuat paketlerindeki tek-doğru-öncül yamaları.

Seçilen sorular 22.07.2026 tarihinde resmî/kurumsal kaynaklarla (Adalet
Bakanlığı TBK metni, Ticaret Bakanlığı TTK metni, TÜRMOB düzenlemeleri, ÇSGB,
SGK ve GİB mevzuat sayfaları) yeniden kontrol edilmiştir.

⚠️ SAHIPLIK DEVRI (2026-08-14): content/meslek_hukuku/mesleki_degerler_etik.json,
meslek_hukuku_esaslari.json ve meslek_orgutu_disiplin.json bloklari bu dosyadan
CIKARILDI. Uc paketin de 60 sorusunun tamami yapisal kalibrasyon turunda
yeniden yazildi ve sahiplik ilgili build_hukuk_meslek_*_yapisal.py dosyalarina
gecti. Bir sorunun tek sahibi olmali.

⚠️ SAHIPLIK DEVRI (2026-08-14): meslek_hukuku/sorumluluk_ve_yasaklar.json blogu
bu dosyadan CIKARILDI. O paketin 60 sorusunun tamami yapisal kalibrasyon turunda
yeniden yazildi ve sahiplik build_hukuk_meslek_sorumluluk_yapisal.py dosyasina
gecti. Bir sorunun tek sahibi olmali.

⚠️ SAHIPLIK DEVRI (2026-08-14): meslek_hukuku/staj_ve_sinavlar.json blogu bu
dosyadan CIKARILDI; sahiplik build_hukuk_meslek_staj_yapisal.py'ye gecti.

⚠️ SAHIPLIK DEVRI (2026-08-14): ticaret_hukuku/kiymetli_evrak.json blogu bu
dosyadan CIKARILDI; sahiplik build_hukuk_kiymetli_evrak_yapisal.py'ye gecti.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def p(stem: str, answer: str, solution: str) -> dict[str, str]:
    return {"stem": stem, "answer": answer, "solution": solution}


PATCHES = {
    "content/borclar_hukuku/temerrut_tazminat.json": {
        "temerrut-gen-0017": p(
            "Aşağıdakilerden hangileri borçlunun ayrıca ihtara gerek kalmadan temerrüde düşebileceği hâllerdendir?\n\nI. İfa gününün taraflarca kesin olarak belirlenmiş olması\n\nII. Borçlunun yalnızca ödeme güçlüğü içinde bulunması\n\nIII. Alacaklının ileride ihtar göndermeyi planlaması",
            "A",
            "Kesin vade varsa borçlu ayrıca ihtar gerekmeksizin temerrüde düşebilir (I). Ödeme güçlüğü tek başına ihtarın yerini tutmaz (II); alacaklının ileride ihtar göndermeyi planlaması da temerrüt doğurmaz (III). Doğru cevap **Yalnız I**.",
        ),
    },
    "content/borclar_hukuku/ozel_durumlar.json": {
        "ozeldurum-gen-0024": p(
            "Cezai şartla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Cezai şart asıl borca bağlı fer'i bir borçtur\n\nII. Alacaklı cezai şartı isteyebilmek için uğradığı zararı mutlaka ispat etmelidir\n\nIII. Hâkim aşırı cezai şartı yalnızca borçlunun talebi üzerine indirebilir",
            "C",
            "Cezai şart asıl borca bağlı fer'i bir borçtur (I). Alacaklı zarara uğramamış olsa da kararlaştırılan cezayı isteyebileceğinden II; hâkim aşırı gördüğü cezayı kendiliğinden indirebildiğinden III yanlıştır. Doğru cevap **Yalnız I**.",
        ),
    },
    "content/borclar_hukuku/haksiz_fiil.json": {
        "hakfiil-gen-0001": p(
            "Aşağıdakilerden hangileri kusura dayanan haksız fiil sorumluluğunun unsurlarındandır?\n\nI. Hukuka aykırı bir fiil\n\nII. Zararın hiç doğmamış olması\n\nIII. Zarar veren ile zarar gören arasında önceden kurulmuş geçerli bir sözleşme",
            "B",
            "Hukuka aykırı fiil sorumluluğun unsurlarındandır (I). Sorumluluk için zararın doğması gerekir; zararın hiç doğmaması unsur değildir (II). Haksız fiil sözleşme dışı bir borç kaynağı olduğundan önceden sözleşme bulunması aranmaz (III). Doğru cevap **Yalnız I**.",
        ),
    },
    "content/borclar_hukuku/sebepsiz_zenginlesme.json": {
        "sebzen-gen-0028": p(
            "Aşağıdakilerden hangileri sebepsiz zenginleşmenin unsurlarındandır?\n\nI. Bir tarafın zenginleşmesi\n\nII. Zenginleşenin mutlaka kusurlu olması\n\nIII. Zenginleşenin haksız fiil işlemiş olması",
            "A",
            "Bir tarafın zenginleşmesi sebepsiz zenginleşmenin unsurudur (I). İade borcu için zenginleşenin kusurlu olması (II) veya haksız fiil işlemesi (III) aranmaz. Doğru cevap **Yalnız I**.",
        ),
    },
    "content/vergi_hukuku/vergi_hukuku_temel_kavramlar.json": {
        "vh-kavram-gen-0011": p(
            "Vergi hukukunun temel kavramlarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Mükellef, kendisine vergi borcu düşen kişidir.\n\nII. Vergi, Bakanlık genelgesiyle konulup kaldırılabilir.\n\nIII. Vergi mükellefi olabilmek için tam fiil ehliyetine sahip olmak şarttır.",
            "A",
            "Mükellef, vergi kanunlarına göre kendisine vergi borcu düşen kişidir (I). Vergi kanunla konulup kaldırıldığından II; vergi ehliyeti için tam fiil ehliyeti aranmadığından III yanlıştır. Doğru cevap **Yalnız I**.",
        ),
    },
    "content/vergi_hukuku/emlak_vergisi.json": {
        "emlak-gen-0007": p(
            "Aşağıdakilerden hangileri bina vergisinin konusuna girebilecek yapılardandır?\n\nI. Konut olarak kullanılan bir daire\n\nII. Kolayca taşınabilen seyyar satış tezgâhı\n\nIII. Motorlu kara taşıtı",
            "A",
            "Konut olarak kullanılan daire bina vergisinin konusuna girebilir (I). Seyyar satış tezgâhı bina niteliğinde değildir (II); motorlu kara taşıtı da emlak vergisinin konusuna girmez (III). Doğru cevap **Yalnız I**.",
        ),
    },
    "content/vergi_hukuku/mtv.json": {
        "mtv-gen-0012": p(
            "Motorlu taşıtlar vergisiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Mükellefiyet, taşıtı fiilen kullanan kişinin adına doğar.\n\nII. Mükellef, satış sözleşmesini imzalayan fakat adına tescil bulunmayan kişidir.\n\nIII. Vergiyi doğuran olay, taşıtın ilgili sicile kayıt ve tescilidir.",
            "D",
            "Mükellefiyet fiilî kullanıma göre değil adına kayıt ve tescil bulunan kişi bakımından doğar; bu nedenle I ve II yanlıştır. Taşıtın ilgili sicile kayıt ve tescili vergiyi doğuran olaydır (III). Doğru cevap **Yalnız III**.",
        ),
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
