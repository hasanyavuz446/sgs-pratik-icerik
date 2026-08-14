#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Meslek Hukuku paketlerindeki salt şık-boy ipucunu doğal dille giderir.

Doğru önermelerin anlamı ve cevap harfi korunur. Uzun doğru seçenekler soru
kökünde zaten bulunan bağlamdan arındırılır; yapay uzun birkaç çeldirici yakın
ama yanlış kurum/ceza önermesine indirilir. İçerik ve uygulama kopyası birlikte
yazılır.

⚠️ SAHIPLIK DEVRI (2026-08-14): meslek_hukuku/sorumluluk_ve_yasaklar.json blogu
bu dosyadan CIKARILDI. O paketin 60 sorusunun tamami yapisal kalibrasyon turunda
yeniden yazildi ve sahiplik build_hukuk_meslek_sorumluluk_yapisal.py dosyasina
gecti. Bir sorunun tek sahibi olmali.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
APP = ROOT.parent / "smmm_sgs_pratik" / "assets" / "content"


CORRECT_REWRITES = {
    "meslek_hukuku/staj_ve_sinavlar.json": {
        "staj-gen-0001": "Vatandaşlık, medeni hak ehliyeti ve kamu haklarından yasaklı olmama genel şartlardandır",
        "staj-gen-0002": "İlgili hukuk ve iktisadi alanlarda en az lisans düzeyinde öğrenim görmüş olmak gerekir",
        "staj-gen-0003": "Öğrenim şartını taşıyan adayın kanunda belirlenen süre boyunca staj yapması gerekir",
        "staj-gen-0004": "Öğrenim ve stajı tamamlayan aday meslek yeterlilik sınavını da geçmelidir",
        "staj-gen-0006": "Staj, izinli meslek mensubu yanında veya kanunda öngörülen kurumlarda yapılabilir",
        "staj-gen-0007": "TESMER, TÜRMOB bünyesinde aday eğitimi ve staj işlemlerini yürüten merkezdir",
        "staj-gen-0008": "Aday, staja başlamadan önce öngörülen staja giriş sınavını başarmalıdır",
        "staj-gen-0009": "Staj kanuni esaslarla yürütülür; uygun önceki hizmetler stajdan sayılabilir",
        "staj-gen-0011": "Staja giriş sınavı, staj öncesi temel bilgiyi ölçmek üzere TÜRMOB/TESMER tarafından yapılır",
        "staj-gen-0012": "Stajını tamamlayan aday, SMMM unvanı için meslek yeterlilik sınavını da başarmalıdır",
        "staj-gen-0013": "Başarısız adaya, mevzuattaki sayı ve süre sınırları içinde yeniden sınav hakkı tanınır",
        "staj-gen-0014": "Sınavlar muhasebe, vergi, hukuk ve meslek mevzuatı gibi temel mesleki alanları kapsar",
        "staj-gen-0016": "YMM için on yıl SMMM'lik, YMM sınavında başarı ve yemin şarttır",
        "staj-gen-0017": "Şartları taşıyıp sınavı geçen aday ruhsat alır ve bölgesindeki meslek odasına kaydolur",
        "staj-gen-0018": "Ruhsatlı meslek mensubu, faaliyet için bölgesindeki ilgili odaya kaydolmalıdır",
        "staj-gen-0019": "YMM için aranan on yıllık süre, kişinin SMMM olarak fiilen çalıştığı süredir",
        "staj-gen-0020": "3568 sayılı Kanun, mesleğe girecekler için SMMM ve YMM unvanlarını öngörür",
        "staj-gen-0021": "Kamu haklarından yasaklılık ve kanunda sayılan suçlardan mahkûmiyet mesleğe engel olabilir",
        "staj-gen-0022": "Ruhsat ve oda kaydı sonrası meslek, bağımsız veya bağımlı biçimde yürütülebilir",
        "staj-gen-0024": "(A), giriş sınavını geçtiği için mevzuattaki süre ve esaslarla stajına başlayabilir",
        "staj-gen-0025": "(B), stajı bitirse de yeterlilik sınavını geçmeden SMMM unvanı ve ruhsatı alamaz",
        "staj-gen-0026": "(C), on yıllık SMMM süresini tamamlayıp YMM sınavı ve yemin şartıyla YMM olabilir",
        "staj-gen-0027": "(D), başarısız olsa da mevzuattaki sayı ve süre sınırları içinde sınava yeniden girebilir",
        "staj-gen-0028": "(E)'nin izinli meslek mensubu gözetimindeki stajı kanuni süreden sayılır",
        "staj-gen-0029": "Şartlardan birini yitiren kişinin ruhsatı, şartlar devamlı olduğundan iptal edilebilir",
        "staj-gen-0030": "Staj uygulamalı deneyim kazandırır; yeterlilik sınavı mesleki bilgi düzeyini ölçer",
        "staj-gen-0032": "(F), staj ve yeterlilik sınavını bitirip ruhsat alınca meslek mensubu olur",
        "staj-gen-0033": "Temel eğitim, adayın mesleki bilgi ve becerilerini geliştirerek onu mesleğe hazırlar",
        "staj-gen-0034": "Staj, yönetmelikteki koşulları taşıyan izinli meslek mensubu yanında yapılır",
        "staj-gen-0035": "Öğrenim, staj ve sınav aşamaları mesleğe nitelikli kişilerin kabulünü sağlar",
        "staj-gen-0036": "İlgili alanda lisans öğrenimi şartını taşımayan aday staja giriş sınavına kabul edilemez",
        "staj-gen-0037": "(G), ruhsat sonrasında da kanundaki etik, disiplin ve mesleki yükümlülüklere uymalıdır",
        "staj-gen-0038": "Meslek mensubu kendi hesabına bağımsız veya bir işverene bağlı olarak çalışabilir",
        "staj-gen-0039": "Ruhsatsız biçimde SMMM veya YMM unvanını kullanmak ya da çağrıştırmak yasaktır",
        "staj-gen-0040": "Ruhsat kişiye bağlı meslek yetkisi belgesidir ve şartların kaybında iptal edilebilir",
        "staj-gen-0041": "YMM sınavını geçen kişi göreve başlamadan önce yetkili merci önünde yemin eder",
        "staj-gen-0042": "Mevzuatta öngörülen mesleki içerikli görevlerde geçen süreler stajdan sayılabilir",
    },
}


DISTRACTOR_REWRITES = {
}


def fix_file(rel: str) -> int:
    src = ROOT / "content" / rel
    data = json.loads(src.read_text(encoding="utf-8"))
    by_id = {q["id"]: q for q in data}
    changed = 0

    for qid, new in CORRECT_REWRITES.get(rel, {}).items():
        q = by_id[qid]
        answer = q["answer"]
        if q["options"][answer] != new:
            q["options"][answer] = new
            changed += 1

    for qid, replacements in DISTRACTOR_REWRITES.get(rel, {}).items():
        q = by_id[qid]
        for letter, new in replacements.items():
            assert letter != q["answer"], f"{qid}: doğru şık değiştirilemez"
            if q["options"][letter] != new:
                q["options"][letter] = new
                changed += 1

    for q in data:
        assert len(q["options"]) == 5
        assert len(set(q["options"].values())) == 5, q["id"]
        assert q["answer"] in q["options"], q["id"]

    payload = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    src.write_text(payload, encoding="utf-8")
    target = APP / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(payload, encoding="utf-8")
    return changed


if __name__ == "__main__":
    # ⚠️ Bu builder --check DESTEKLEMEZ ve calistiginda dogrudan YAZAR.
    # Toplu dogrulama donguleri onu "--check" ile cagirdiginda argumani sessizce
    # yok sayip yayinlanmis icerigi geri yaziyordu (2026-08-14'te
    # meslek_orgutu_disiplin.json'da gerceklesti). Artik argumanla cagrilirsa
    # yazmadan hata verir.
    import sys
    if sys.argv[1:]:
        print("HATA: bu builder arguman kabul etmez ve calistiginda dogrudan YAZAR.")
        print("Dogrulama icin git diff kullanin; yazmak icin argumansiz calistirin.")
        raise SystemExit(2)
    files = sorted(set(CORRECT_REWRITES) | set(DISTRACTOR_REWRITES))
    for rel in files:
        print(f"{rel}: {fix_file(rel)} doğal şık düzeltmesi")
