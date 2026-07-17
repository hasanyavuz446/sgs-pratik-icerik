#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kalan SGS paketlerindeki kör-tahmin şık ipuçlarını doğal biçimde giderir."""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
APP = ROOT.parent / "smmm_sgs_pratik" / "assets" / "content"


CORRECT = {
    "vergi_hukuku/vergi_denetimi_ceza_uyusmazlik.json": {
        "vh-denetim-gen-0001": "Ödül verme",
        "vh-denetim-gen-0005": "İstenen vergilendirme bilgilerini kural olarak vermek zorundadırlar",
        "vh-denetim-gen-0007": "Vergi ziyaı ve usulsüzlük idari, kaçakçılık suçu adli cezaya tabidir",
        "vh-denetim-gen-0010": "Sahte belge, defter hilesi veya gizleme gibi fiillerle işlenen hapis cezalı vergi suçudur",
        "vh-denetim-gen-0012": "İdari yollarla veya vergi mahkemesinde dava yoluyla çözülebilir",
        "vh-denetim-gen-0013": "Mükellef ile idarenin vergi veya ceza üzerinde anlaşması",
        "vh-denetim-gen-0015": "İdare tespitinden önce bildirim ve ödeme koşullarıyla vergi ziyaı cezasını önleyen kurumdur",
    },
    "ekonomi/para_banka_dis_ekonomi.json": {
        "eko-para-gen-0001": "Üretim faktörlerini üretmek",
        "eko-para-gen-0005": "Mevduatın belirli oranını Merkez Bankasında tutma yükümlülüğüdür",
        "eko-para-gen-0008": "I ve III",
        "eko-para-gen-0009": "İhracat dış satım, ithalat dış alımdır; dış ticaret dengesi aralarındaki farktır",
        "eko-para-gen-0011": "Sabit kuru otorite, dalgalı kuru piyasadaki döviz arz ve talebi belirler",
        "eko-para-gen-0013": "Ülkenin dış dünyayla ekonomik işlemlerini gösteren sistematik tablo",
        "eko-para-gen-0014": "Mal ve hizmet ticaretiyle birincil ve ikincil gelirleri kapsayan hesap",
        "eko-para-gen-0015": "II ve III",
    },
    "maliye/butce_maliye_politikasi.json": {
        "mal-butce-gen-0014": "İç borç yurt içi, dış borç yurt dışı kaynaklardan sağlanır",
    },
    "turkce/sozcukte_cumlede_anlam.json": {
        "turkce-anlam-gen-0002": "Acı haberle sarsıldık bugün.",
        "turkce-anlam-gen-0004": "İç **açılar** toplamı 180°dir.",
        "turkce-anlam-gen-0005": "Temelden ve esaslı biçimde",
        "turkce-anlam-gen-0007": "Bize karşı mesafeli davrandı.",
        "turkce-anlam-gen-0008": "Karışıklığı düzene sokmak",
        "turkce-anlam-gen-0011": "Küçük birikimler zamanla büyür.",
        "turkce-anlam-gen-0012": "Çaresiz ve şaşkın kalmak",
        "turkce-anlam-gen-0014": "Zarar gören kişi daha temkinli olur.",
        "turkce-anlam-gen-0019": "Sessiz sedasız gitti.",
        "turkce-anlam-gen-0022": "Anlaşmayı açık sözlerle yazdılar.",
    },
    "turkce/dil_bilgisi.json": {
        "turkce-dilbilgisi-gen-0002": "alnı",
        "turkce-dilbilgisi-gen-0003": "Zarf",
        "turkce-dilbilgisi-gen-0008": "Edat",
        "turkce-dilbilgisi-gen-0010": "Zarf-fiil",
        "turkce-dilbilgisi-gen-0012": "Sıfat-fiil",
    },
}


DISTRACTORS = {
    "is_ve_sosyal_guvenlik_hukuku/is_hukuku_is_sozlesmesi.json": {
        "ish-sozlesme-gen-0001": {"A": "1475 sayılı Kanun"},
        "ish-sozlesme-gen-0003": {"A": "Yalnız gerçek kişiler"},
        "ish-sozlesme-gen-0004": {"A": "İşyerindeki her işçi"},
        "ish-sozlesme-gen-0006": {"B": "Ücretsiz vekâlet sözleşmesi"},
    },
    "vergi_hukuku/vergilendirme_sureci.json": {
        "vh-surec-gen-0001": {"A": "Verginin ödenmesi"},
        "vh-surec-gen-0008": {"A": "Muhatap adreste bulunduğunda"},
    },
    "ataturk_ilkeleri/ataturk_inkilaplari.json": {
        "ait-inkilap-gen-0004": {"B": "Türk Harflerinin Kabul ve Tatbiki Hakkında Kanun"},
    },
}


FULL_OPTIONS = {
    "mali_tablolar_analizi/trend_analizi.json": {
        "mta-trend-gen-0042": {"A": "%55,0", "B": "%155,0", "C": "%64,5", "D": "%45,0", "E": "%15,5"},
        "mta-trend-gen-0044": {"A": "%60,0", "B": "%62,5", "C": "%160,0", "D": "%40,0", "E": "%16,0"},
        "mta-trend-gen-0045": {"A": "%65,0", "B": "%60,6", "C": "%35,0", "D": "%16,5", "E": "%165,0"},
        "mta-trend-gen-0047": {"A": "%80,0", "B": "%55,6", "C": "%180,0", "D": "%20,0", "E": "%18,0"},
        "mta-trend-gen-0058": {"A": "%75,0", "B": "%57,1", "C": "%25,0", "D": "%17,5", "E": "%175,0"},
    },
}


PRINCIPLE_QUESTIONS = [
    "ait-ilke-gen-0001", "ait-ilke-gen-0002", "ait-ilke-gen-0003",
    "ait-ilke-gen-0004", "ait-ilke-gen-0005", "ait-ilke-gen-0006",
    "ait-ilke-gen-0007", "ait-ilke-gen-0008", "ait-ilke-gen-0009",
    "ait-ilke-gen-0018", "ait-ilke-gen-0019",
]
PRINCIPLES = [
    "Cumhuriyetçilik", "Halkçılık", "Laiklik",
    "Devletçilik", "Milliyetçilik", "İnkılapçılık",
]


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
    for qid, replacements in FULL_OPTIONS.get(rel, {}).items():
        q = by_id[qid]
        assert set(replacements) == set("ABCDE"), qid
        for letter, new in replacements.items():
            if q["options"][letter] != new:
                q["options"][letter] = new
                changed += 1
    if rel == "ataturk_ilkeleri/ataturk_ilkeleri_dis_politika.json":
        for qid in PRINCIPLE_QUESTIONS:
            q = by_id[qid]
            answer = q["answer"]
            correct = q["options"][answer]
            assert correct in PRINCIPLES, (qid, correct)
            distractors = [p for p in PRINCIPLES if p != correct][:4]
            for letter, new in zip((x for x in "ABCDE" if x != answer), distractors):
                if q["options"][letter] != new:
                    q["options"][letter] = new
                    changed += 1
            if correct == "Laiklik" and q["options"][answer] != "Laiklik ilkesi":
                q["options"][answer] = "Laiklik ilkesi"
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
    paths = set(CORRECT) | set(DISTRACTORS) | set(FULL_OPTIONS)
    paths.add("ataturk_ilkeleri/ataturk_ilkeleri_dis_politika.json")
    for rel in sorted(paths):
        print(f"{rel}: {fix(rel)} doğal şık düzeltmesi")
