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
    "denetim/denetim_raporu.json": {
        "den-rapor-gen-0001": "Finansal tablolar hakkındaki denetçi görüşünü içeren yazılı rapor",
        "den-rapor-gen-0003": "Tablolar tüm önemli yönleriyle geçerli çerçeveye uygun sunulduğunda verilir",
        "den-rapor-gen-0004": "Tabloların önemli yanlışlık içermediğine ilişkin makul güvenceyi ifade eder",
        "den-rapor-gen-0006": "Önemli fakat yaygın olmayan yanlışlık veya kanıt sınırlamasında verilir",
        "den-rapor-gen-0007": "Yeterli kanıt yoksa ve olası etkiler önemli ve yaygınsa verilir",
        "den-rapor-gen-0008": "Sorunun niteliği ile finansal tablolara yaygınlığı",
        "den-rapor-gen-0009": "Etkilerin finansal tabloların geneline yayılma derecesi",
        "den-rapor-gen-0012": "Olumsuz (aykırı) görüş",
        "den-rapor-gen-0014": "Önemli ve yaygın değilse şartlı, önemli ve yaygınsa olumsuz görüş verilir",
        "den-rapor-gen-0015": "Önemli ve yaygın değilse şartlı görüş, yaygınsa görüşten kaçınma söz konusudur",
        "den-rapor-gen-0017": "Cari dönem denetiminde en çok önem taşıyan konular",
        "den-rapor-gen-0018": "Görüşü değiştirmeden, süreklilik belirsizliğine ilgili bölümde dikkat çeker",
        "den-rapor-gen-0019": "Tabloları hazırlamak ve iç kontrolü kurmak yönetimin sorumluluğudur",
        "den-rapor-gen-0021": "Görüş değişikliğinin nedenini açıklayan Görüşün Dayanağı bölümü",
        "den-rapor-gen-0022": "Belirtilen husus dışında tabloların çerçeveye uygun olduğunu bildirir",
        "den-rapor-gen-0023": "Önemli fakat yaygın olmayan yanlışlık için sınırlı olumlu görüş",
        "den-rapor-gen-0024": "Yaygın yanlışlık nedeniyle olumsuz görüş",
        "den-rapor-gen-0025": "Standartlara uygun denetimle makul güvence sağlayıp görüş bildirmek",
        "den-rapor-gen-0026": "Rapor tarihi, yeterli ve uygun kanıtın elde edildiği tarihten önce olamaz",
        "den-rapor-gen-0027": "Dikkat çekme tablodaki, diğer hususlar tablolarda yer almayan konuya ilişkindir",
        "den-rapor-gen-0028": "Önemli yanlışlık veya yeterli kanıt bulunmaması",
        "den-rapor-gen-0029": "Rapor, denetimi yaptıranlara hitaben düzenlenir",
        "den-rapor-gen-0031": "Olumlu görüş güvenceyi, olumsuz görüş tabloların yanlışlığını bildirir",
        "den-rapor-gen-0032": "Tablolar tüm önemli yönleriyle geçerli çerçeveye uygunsa",
        "den-rapor-gen-0033": "Tabloların çerçeveye uygun sunulup sunulmadığına ilişkin görüş",
    },
    "denetim/denetim_ornekleme.json": {
        "den-ornek-gen-0001": "Kütlenin tamamından azını test ederek bütünü hakkında sonuç çıkarma",
        "den-ornek-gen-0003": "Örneklem nedeniyle tüm kütle incelenseydi ulaşılacak sonuçtan sapma riski",
        "den-ornek-gen-0008": "Örneklem kütleyi temsil etmeli ve kütleye ilişkin sonuç sağlamalıdır",
        "den-ornek-gen-0009": "Az sayıda, büyük tutarlı veya tek tek önemli birimlerin bulunduğu durumlarda",
        "den-ornek-gen-0016": "Kabul edilebilir risk ve tolere edilebilir hata azaldıkça örneklem büyür",
        "den-ornek-gen-0017": "Kütle sonucunu değiştirmeden kabul edilebilecek en yüksek sapma",
        "den-ornek-gen-0018": "Kontrolün işleyip işlemediğini sınayan nitelik örneklemesi",
        "den-ornek-gen-0019": "Parasal yanlışlığı sınayan değişken örneklemesi",
        "den-ornek-gen-0023": "Kontrol riskini yükseltip maddi doğrulamayı artırabilir",
        "den-ornek-gen-0029": "Örneklemin kütleyi temsil etmemesi",
        "den-ornek-gen-0030": "Sapma oranı sınırın altındaysa kontrole güveni destekler",
        "den-ornek-gen-0031": "Uygulanan prosedür, elde edilen kanıt ve sonuçları belgeleyen kayıtlar",
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
    "denetim/denetim_raporu.json": {
        "den-rapor-gen-0001": {"A": "Gelecek dönem kâr tahminleri"},
        "den-rapor-gen-0007": {"A": "Tablolar önemli yanlışlık içermiyorsa"},
        "den-rapor-gen-0008": {"A": "Denetim ücreti ve süresi"},
        "den-rapor-gen-0009": {"A": "Raporun yayımlanma alanı"},
        "den-rapor-gen-0017": {"A": "Gelecek yılın hedefleri"},
        "den-rapor-gen-0021": {"B": "Yönetimin kâr projeksiyonu"},
        "den-rapor-gen-0023": {"A": "Olumlu görüş"},
        "den-rapor-gen-0024": {"A": "Olumlu görüş"},
        "den-rapor-gen-0028": {"B": "Dikkat çekme paragrafı"},
        "den-rapor-gen-0029": {"A": "En büyük müşteriye"},
        "den-rapor-gen-0032": {"A": "Yaygın kanıt eksikliği varsa"},
        "den-rapor-gen-0033": {"B": "Gelecek dönem kâr tahmini"},
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
