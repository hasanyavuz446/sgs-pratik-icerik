#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Denetim paketlerindeki şık-boy ipucunu doğal ve öz seçeneklerle giderir."""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
APP = ROOT.parent / "smmm_sgs_pratik" / "assets" / "content"


CORRECT = {
    "denetim/denetim_kaniti.json": {
        "den-kanit-gen-0001": "Denetçi görüşüne dayanak oluşturan bilgi ve belgeler",
        "den-kanit-gen-0003": "Kanıtın ilgili iddiayla ilgililiği ve güvenilirliği",
        "den-kanit-gen-0004": "Bağımsız dış kaynaktan doğrudan alınan kanıt daha güvenilirdir",
        "den-kanit-gen-0012": "Tek başına sınırlı kanıttır; başka tekniklerle doğrulanmalıdır",
        "den-kanit-gen-0016": "Kayıt ve belgelerin içerik ve tutar yönünden incelenmesini",
        "den-kanit-gen-0017": "Planlama, esas inceleme ve sonuçlandırma aşamalarında kullanılabilir",
        "den-kanit-gen-0018": "Denetçinin elde ettiği veya bağımsız dış kaynaktan gelen kanıt",
        "den-kanit-gen-0019": "Borçluya teyit gönderip doğrudan yazılı yanıt almak",
        "den-kanit-gen-0024": "Maddi doğrulama bakiyeyi, kontrol testi kontrol etkinliğini sınar",
        "den-kanit-gen-0027": "Kontrol riski düştükçe gereken esas prosedür kanıtı azalabilir",
        "den-kanit-gen-0029": "Sonraki tahsilat ile sevk ve fatura belgelerini incelemek",
        "den-kanit-gen-0030": "Kanıtın test edilen iddiayı destekleme veya çürütme gücü",
        "den-kanit-gen-0034": "Kontrol testlerinde gözlem, inceleme, soruşturma ve yeniden uygulama kullanılabilir",
        "den-kanit-gen-0057": "Tahminin varsayım, yöntem ve verilerinin makullüğünü kanıtla test etmek",
    },
    "denetim/denetim_riski.json": {
        "den-risk-gen-0001": "Önemli yanlışlık varken uygun olmayan görüş verme riski",
        "den-risk-gen-0002": "Yapısal risk × kontrol riski × tespit riski",
        "den-risk-gen-0004": "İç kontrolün yanlışlığı önleyememe veya düzeltememe riski",
        "den-risk-gen-0006": "Yapısal risk ile kontrol riski",
        "den-risk-gen-0007": "Yapısal risk ile kontrol riskinin bileşimi",
        "den-risk-gen-0016": "Kontrol riski düştükçe kabul edilebilir tespit riski yükseltilebilir",
    },
}


DISTRACTORS = {
    "denetim/denetim_standartlari_etik.json": {
        "den-standart-gen-0007": {"B": "Vergi oranlarını saptamak"},
        "den-standart-gen-0017": {"A": "Özen"},
        "den-standart-gen-0019": {"A": "Özen"},
        "den-standart-gen-0029": {"A": "Tehditleri yok saymak"},
        "den-standart-gen-0039": {"A": "Gizlilik"},
        "den-standart-gen-0043": {"A": "Yıldırma tehdidi; bağımsızlık ihlalidir"},
        "den-standart-gen-0044": {"B": "Kararı yönetime bırakmalıdır"},
        "den-standart-gen-0052": {"A": "İşletmenin iç yönetmeliği"},
        "den-standart-gen-0053": {"C": "Yalnız gizlilik ilkesi"},
        "den-standart-gen-0055": {"A": "Bağımsızlığı etkilemez"},
    },
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
    for rel in sorted(set(CORRECT) | set(DISTRACTORS)):
        print(f"{rel}: {fix(rel)} doğal şık düzeltmesi")
