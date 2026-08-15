#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ticaret Hukuku paketlerindeki şık-boy ipucunu doğal seçeneklerle giderir.
⚠️ SAHIPLIK DEVRI (2026-08-14): ticaret_hukuku/ticari_isletme_tacir.json bloklari
bu dosyadan CIKARILDI; sahiplik build_hukuk_ticari_isletme_yapisal.py'ye gecti.

⚠️ SAHIPLIK DEVRI (2026-08-14): ticaret_hukuku/kiymetli_evrak.json blogu bu
dosyadan CIKARILDI; sahiplik build_hukuk_kiymetli_evrak_yapisal.py'ye gecti.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
APP = ROOT.parent / "smmm_sgs_pratik" / "assets" / "content"


CORRECT = {
    "ticaret_hukuku/haksiz_rekabet.json": {
        "hakrek-gen-0002": "Aldatıcı veya dürüstlüğe aykırı ticari uygulamalar haksız rekabettir",
        "hakrek-gen-0006": "Başkalarını veya ürünlerini yanlış, yanıltıcı ya da gereksiz incitici açıklamalarla kötülemek",
        "hakrek-gen-0007": "Kendisini, işletmesini veya malını yanıltıcı açıklamalarla öne çıkarmak haksız rekabettir",
        "hakrek-gen-0008": "Başkasının malı, ürünü veya işletmesiyle karıştırılmaya yol açan önlem almak",
        "hakrek-gen-0009": "Sahip olunmayan unvan, diploma veya ödülle üstünlük sağlamaya çalışmak",
        "hakrek-gen-0010": "Maliyetin altındaki seçilmiş mallarla müşteri ve rakipleri yanıltmak haksız rekabet olabilir",
        "hakrek-gen-0011": "Saldırgan satış yöntemiyle müşterinin karar özgürlüğünü sınırlamak haksız rekabettir",
        "hakrek-gen-0013": "Ek edimin gerçek değeri konusunda müşteriyi yanıltmak haksız rekabet olabilir",
        "hakrek-gen-0014": "Çalışanı işvereninin üretim veya iş sırrını açıklamaya yöneltmek haksız rekabettir",
        "hakrek-gen-0015": "Müşteriyi sözleşmeye aykırılığa veya haksız feshe yöneltmek haksız rekabettir",
        "hakrek-gen-0016": "Emanet edilen teklif, hesap veya plandan yetkisiz yararlanmak haksız rekabettir",
        "hakrek-gen-0017": "Hukuka aykırı edinilen üretim veya iş sırrını kullanmak ya da açıklamak haksız rekabettir",
        "hakrek-gen-0018": "Ortak iş şartlarına uymamak veya dürüstlüğe aykırı şart kullanmak haksız rekabettir",
        "hakrek-gen-0020": "Tespit davası, davranışın haksız rekabet niteliğini belirler",
        "hakrek-gen-0021": "Men davası, haksız rekabet fiilinin durdurulmasını amaçlar",
        "hakrek-gen-0022": "Düzeltme davası, haksız rekabetin doğurduğu maddi durumu giderir",
        "hakrek-gen-0023": "Zarar gören, fail kusurluysa maddi zararının tazminini isteyebilir",
        "hakrek-gen-0024": "Koşulları varsa manevi tazminata ve failin kazancının devrine karar verilebilir",
        "hakrek-gen-0027": "Müşterisi, kredisi veya ticari itibarı zarar gören kişi dava açabilir",
        "hakrek-gen-0029": "Dava, öğrenmeden bir ve her hâlde fiilin doğumundan üç yıl sonra zamanaşımına uğrar",
        "hakrek-gen-0030": "Mahkeme, kazananın talebiyle ve karşı tarafın gideriyle kararın ilanına hükmedebilir",
        "hakrek-gen-0031": "Kanundaki fiiller, hak sahibinin şikâyeti üzerine cezai yaptırıma tabi olabilir",
        "hakrek-gen-0032": "Hak sahibi mahkemeden haksız rekabeti önleyici ihtiyati tedbir isteyebilir",
        "hakrek-gen-0034": "(A)'nın kötülemesi haksız rekabettir; (B) tespit, men ve düzeltme davaları açabilir",
        "hakrek-gen-0035": "(C)'nin iltibasa yol açan davranışı haksız rekabettir; (D) hukuki dava açabilir",
        "hakrek-gen-0036": "(E)'nin çalışanı iş sırrını açıklamaya yöneltmesi haksız rekabettir",
        "hakrek-gen-0037": "Öğrenmeden itibaren bir yıl geçtiği için zamanaşımı def'i davayı sonuçsuz bırakabilir",
        "hakrek-gen-0038": "Çalışanın görevdeki fiili nedeniyle (H), istihdam eden (G)'ye de dava açabilir",
        "hakrek-gen-0039": "(K)'nin sahip olmadığı ödülü kullanması haksız rekabettir; zarar görenler dava açabilir",
        "hakrek-gen-0040": "Kusur olmasa da tespit, men ve düzeltme davaları açılabilir",
        "hakrek-gen-0050": "(N)'nin yanıltıcı ve rakipleri dışlayıcı maliyet altı satışı haksız rekabet oluşturabilir",
        "hakrek-gen-0051": "Asılsız kötüleme haksız rekabettir; zarar gören rakip dava açabilir",
        "hakrek-gen-0052": "Kişilik hakkı zedelenmişse haksız rekabet nedeniyle manevi tazminat istenebilir",
        "hakrek-gen-0059": "Hükümler, dürüst rekabeti etkileyen davranışlara katılan herkesi kapsar",
    },
}


DISTRACTORS = {
}


def fix(rel: str) -> int:
    source = ROOT / "content" / rel
    data = json.loads(source.read_text(encoding="utf-8"))
    by_id = {q["id"]: q for q in data}
    changed = 0
    for qid, new in CORRECT.get(rel, {}).items():
        q = by_id[qid]
        if q["options"][q["answer"]] != new:
            q["options"][q["answer"]] = new
            changed += 1
    for qid, replacements in DISTRACTORS.get(rel, {}).items():
        q = by_id[qid]
        for letter, new in replacements.items():
            assert letter != q["answer"], qid
            if q["options"][letter] != new:
                q["options"][letter] = new
                changed += 1
    for q in data:
        assert set(q["options"]) == set("ABCDE"), q["id"]
        assert len(set(q["options"].values())) == 5, q["id"]
    payload = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    source.write_text(payload, encoding="utf-8")
    target = APP / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(payload, encoding="utf-8")
    return changed


if __name__ == "__main__":
    # ⚠️ Bu builder --check DESTEKLEMEZ ve calistiginda dogrudan YAZAR.
    # Toplu dogrulama donguleri onu "--check" ile cagirdiginda argumani sessizce
    # yok sayip yayinlanmis icerigi geri yazar (2026-08-14'te
    # fix_meslek_length_quality ile ayni sey yasandi). Artik arguman verilirse
    # yazmadan hata verip cikar.
    import sys
    if sys.argv[1:]:
        print("HATA: bu builder arguman kabul etmez ve calistiginda dogrudan YAZAR.")
        print("Dogrulama icin git diff kullanin; yazmak icin argumansiz calistirin.")
        raise SystemExit(2)
    for rel in sorted(set(CORRECT) | set(DISTRACTORS)):
        print(f"{rel}: {fix(rel)} doğal şık düzeltmesi")
