#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Meslek Hukuku paketlerindeki salt şık-boy ipucunu doğal dille giderir.

Doğru önermelerin anlamı ve cevap harfi korunur. Uzun doğru seçenekler soru
kökünde zaten bulunan bağlamdan arındırılır; yapay uzun birkaç çeldirici yakın
ama yanlış kurum/ceza önermesine indirilir. İçerik ve uygulama kopyası birlikte
yazılır.
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
    "meslek_hukuku/sorumluluk_ve_yasaklar.json": {
        "sorum-gen-0001": "Meslek mensubu aynı fiil nedeniyle disiplin, hukuki ve cezai sorumluluklara tabi olabilir",
        "sorum-gen-0002": "Meslek kurallarına aykırılık, meslek örgütü önünde disiplin sorumluluğu doğurabilir",
        "sorum-gen-0003": "Mesleki kusurla müşteri veya üçüncü kişiye verilen zarar hukuki sorumluluk doğurabilir",
        "sorum-gen-0004": "Kanunda suç sayılan meslekle bağlantılı fiil cezai sorumluluk doğurabilir",
        "sorum-gen-0006": "İmzalayan meslek mensubu, beyannamedeki bilgilerin defter ve belgelere uygunluğundan sorumludur",
        "sorum-gen-0007": "YMM, tasdik aykırılığından doğan vergi ve cezalardan mükellefle birlikte sorumludur",
        "sorum-gen-0008": "Vergi idaresi, vergi ve cezanın tamamını sorumlu meslek mensubundan da isteyebilir",
        "sorum-gen-0009": "Meslek mensubu, ibraz edilen belgedeki aykırılığı bilebileceği ölçüde yaptığı işlemden sorumludur",
        "sorum-gen-0012": "Bağımsız meslek mensubu, tarafsızlıkla bağdaşmayan ticari faaliyette bulunamaz",
        "sorum-gen-0013": "Meslek mensubu vakar, onur veya bağımsızlıkla bağdaşmayan iş yapamaz",
        "sorum-gen-0014": "Meslek mensubunun başkasının işini edinmeye yönelik haksız rekabet davranışı yasaktır",
        "sorum-gen-0016": "Meslek mensubu ve çalışanları, müşteri sırlarını kanuni hâller dışında açıklayamaz",
        "sorum-gen-0017": "Meslek mensubu, mesleki faaliyetini her türlü baskıdan uzak ve bağımsız yürütmelidir",
        "sorum-gen-0018": "Meslek mensubu, mesleki değerlendirme ve kararlarında tarafsız davranmalıdır",
        "sorum-gen-0019": "Meslek mensubu sır saklar; yalnız kanunun izin verdiği hâllerde bilgi verebilir",
        "sorum-gen-0020": "Meslek mensubu müşteriyle yazılı hizmet sözleşmesi yapar ve ücreti sözleşmede belirler",
        "sorum-gen-0021": "Asgari ücret tarifesi TÜRMOB'ca hazırlanır ve Bakanlık onayıyla yürürlüğe girer",
        "sorum-gen-0022": "Meslek mensubu asgari ücret tarifesinin altında ücretle iş kabul edemez",
        "sorum-gen-0023": "Teslim alınan ve düzenlenen belgeler meslek mensubunca kanuni süre boyunca saklanmalıdır",
        "sorum-gen-0024": "(A), beyanname aykırılığından doğan vergi ziyaında (B) ile birlikte sorumlu olabilir",
        "sorum-gen-0025": "(C), tasdik aykırılığından doğan vergi ve cezada şirketle birlikte sorumludur",
        "sorum-gen-0026": "(D)'nin iş edinmeye yönelik reklamı yasağa aykırı olup disiplin sorumluluğu doğurabilir",
        "sorum-gen-0027": "(E)'nin bağımsızlıkla bağdaşmayan ticari faaliyeti meslek yasağına aykırıdır",
        "sorum-gen-0028": "(F)'nin müşteri sırrını açıklaması sır saklama yükümlülüğünü ihlal eder ve sorumluluk doğurur",
        "sorum-gen-0029": "(G), iş ücretini kural olarak yazılı hizmet sözleşmesiyle belirlemeliydi",
        "sorum-gen-0030": "(H), kural olarak asgari tarifenin altında ücretle iş kabul edemezdi",
        "sorum-gen-0032": "(K), tümüyle gizlenen ve bilemeyeceği husustan doğan vergi ziyaından sorumlu tutulamaz",
        "sorum-gen-0033": "(L), mesleki ihmaliyle müşteriye verdiği zarardan hukuken ve mali tazminatla sorumlu olabilir",
        "sorum-gen-0034": "Başka meslek mensubunun işini haksız rekabetle elde etmeye çalışmak yasaktır",
        "sorum-gen-0035": "Aynı fiil disiplin sorumluluğu yanında cezai sorumluluk da doğurabilir",
        "sorum-gen-0036": "Meslek mensubu bağımsızlığını zedeleyen çıkar çatışmalarından kaçınmalıdır",
        "sorum-gen-0037": "İdare, vergi ve cezanın tamamını mükelleften veya sorumlu meslek mensubundan isteyebilir",
        "sorum-gen-0038": "Çalışanlar da işleri sırasında öğrendikleri müşteri sırlarını saklamalıdır",
        "sorum-gen-0039": "Yükümlülük ihlali disiplin, hukuki veya cezai sorumluluk doğurabilir",
        "sorum-gen-0043": "Haklı sebeple çekilme, müşteriyi zarara uğratmayacak uygun zamanda yapılmalıdır",
        "sorum-gen-0044": "Sahte veya yanıltıcı belge düzenlemek ya da buna iştirak disiplin ve ceza sorumluluğu doğurur",
        "sorum-gen-0049": "Defter ve kayıtlar meslek mensubunca mevzuata uygun, doğru ve mesleki özenle tutulmalıdır",
        "sorum-gen-0052": "Meslek mensubu müşteri işini dürüstlük ve sadakatle yürütüp müşterinin çıkarını gözetmelidir",
        "sorum-gen-0053": "Kanuni hâllerde bazı mükelleflerin beyannamelerini meslek mensubunun imzalaması zorunludur",
    },
}


DISTRACTOR_REWRITES = {
    "meslek_hukuku/meslek_orgutu_disiplin.json": {
        "mh-orgut-gen-0003": {"A": "TOBB (Türkiye Odalar ve Borsalar Birliği)"},
        "mh-orgut-gen-0010": {"A": "Ruhsatın geri alınması"},
        "mh-orgut-gen-0013": {"B": "Yalnız yazılı uyarma cezası"},
        "mh-orgut-gen-0016": {"B": "Hazine ve Maliye Bakanlığı"},
        "mh-orgut-gen-0026": {"B": "Oda Disiplin Kurulu"},
        "mh-orgut-gen-0038": {"A": "Tekerrür disiplin cezasını etkilemez"},
    },
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
    files = sorted(set(CORRECT_REWRITES) | set(DISTRACTOR_REWRITES))
    for rel in files:
        print(f"{rel}: {fix_file(rel)} doğal şık düzeltmesi")
