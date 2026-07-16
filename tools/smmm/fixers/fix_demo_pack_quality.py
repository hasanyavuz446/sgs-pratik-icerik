#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM ücretsiz örnek paketini güncel içerik sözleşmesine uyarlar.

Dosya adı ve soru kimliklerindeki ``demo`` ibaresi iç sistem kimliğidir. Kullanıcıya
görünen soru, çözüm, etiket ve dönem alanlarına demo ifadesi yazılmaz.

Script:
- her soruya madde/formül düzeyinde kaynak ve ders bazlı yürürlük sürümü ekler,
- eski İş ve Sosyal Güvenlik Hukuku kimliğini güncel İş Hukuku alt dersine taşır,
- paketi konu havuzundan ayrı Bölüm Havuzu olarak işaretler,
- doğru seçenek metnini koruyarak cevap harflerini dengeli ve örüntüsüz dağıtır,
- içerik ve uygulama kopyalarını birlikte yazar.
"""
from __future__ import annotations

import json
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTENT_PATH = ROOT / "content" / "yeterlilik" / "demo_questions.json"
STIMULI_PATH = ROOT / "content" / "yeterlilik" / "stimuli.json"
APP_PATH = (
    ROOT.parent
    / "smmm_sgs_pratik"
    / "assets"
    / "content"
    / "yeterlilik"
    / "demo_questions.json"
)
APP_STIMULI_PATH = (
    ROOT.parent
    / "smmm_sgs_pratik"
    / "assets"
    / "content"
    / "yeterlilik"
    / "stimuli.json"
)
UPDATED_AT = "2026-07-17T00:00:00Z"

LESSON_ALIASES = {
    "is_ve_sosyal_guvenlik_hukuku": "is_hukuku",
}

VALID_PAIRS = {
    ("finansal_muhasebe", "temel_kavramlar"),
    ("maliyet_muhasebesi", "maliyet_temelleri"),
    ("yonetim_muhasebesi", "karar_verme"),
    ("mali_tablolar_analizi", "oran_analizi"),
    ("denetim", "denetim_temelleri"),
    ("vergi_usul_kanunu", "vergilendirme_sureci"),
    ("vergi_hukuku", "vergi_hukuku_ilkeleri"),
    ("turk_vergi_sistemi", "vergi_sistemi_yapisi"),
    ("gelir_vergisi", "gelir_unsurlari"),
    ("kurumlar_vergisi", "kurum_kazanci"),
    ("katma_deger_vergisi", "kdv_mekanizmasi"),
    ("ticaret_hukuku", "ticari_isletme"),
    ("borclar_hukuku", "borc_iliskisi"),
    ("is_hukuku", "is_sozlesmesi"),
    ("meslek_hukuku", "mesleki_etik"),
    ("sermaye_piyasasi_ve_finans", "sermaye_piyasasi_araclari"),
    ("sermaye_piyasasi_ve_finans", "ihrac_ve_halka_arz"),
}

SECTION_LABELS = {
    "finansal_muhasebe": "Finansal Muhasebe",
    "maliyet_muhasebesi": "Maliyet Muhasebesi",
    "yonetim_muhasebesi": "Maliyet Muhasebesi",
    "mali_tablolar_analizi": "Finansal Tablolar ve Analizi",
    "denetim": "Muhasebe Denetimi",
    "vergi_usul_kanunu": "Vergi Mevzuatı ve Uygulaması",
    "vergi_hukuku": "Vergi Mevzuatı ve Uygulaması",
    "turk_vergi_sistemi": "Vergi Mevzuatı ve Uygulaması",
    "gelir_vergisi": "Vergi Mevzuatı ve Uygulaması",
    "kurumlar_vergisi": "Vergi Mevzuatı ve Uygulaması",
    "katma_deger_vergisi": "Vergi Mevzuatı ve Uygulaması",
    "ticaret_hukuku": "Hukuk",
    "borclar_hukuku": "Hukuk",
    "is_hukuku": "Hukuk",
    "meslek_hukuku": "Meslek Hukuku",
    "sermaye_piyasasi_ve_finans": "Sermaye Piyasası Mevzuatı",
}

VERSION_BY_LESSON = {
    "finansal_muhasebe": "TFRS 2026 Seti (Mavi Kitap) ve yürürlükteki Tekdüzen Hesap Planı",
    "maliyet_muhasebesi": "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı",
    "yonetim_muhasebesi": "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı",
    "mali_tablolar_analizi": "TFRS 2026 Seti (Mavi Kitap) ve 2026 SMMM Yeterlilik kapsamı",
    "denetim": "KGK Türkiye Denetim Standartları 2026 Seti",
    "vergi_usul_kanunu": "213 sayılı Vergi Usul Kanunu, 17.07.2026 yürürlük durumu",
    "vergi_hukuku": "T.C. Anayasası ve vergi mevzuatı, 17.07.2026 yürürlük durumu",
    "turk_vergi_sistemi": "Türk vergi sistemi, 17.07.2026 yürürlük durumu",
    "gelir_vergisi": "193 sayılı Gelir Vergisi Kanunu, 17.07.2026 yürürlük durumu",
    "kurumlar_vergisi": "5520 sayılı Kurumlar Vergisi Kanunu, 17.07.2026 yürürlük durumu",
    "katma_deger_vergisi": "3065 sayılı Katma Değer Vergisi Kanunu, 17.07.2026 yürürlük durumu",
    "ticaret_hukuku": "6102 sayılı Türk Ticaret Kanunu, 17.07.2026 yürürlük durumu",
    "borclar_hukuku": "6098 sayılı Türk Borçlar Kanunu, 17.07.2026 yürürlük durumu",
    "is_hukuku": "4857 sayılı İş Kanunu ve 6098 sayılı TBK, 17.07.2026 yürürlük durumu",
    "meslek_hukuku": "3568 sayılı Kanun ve meslek etiği düzenlemeleri, 17.07.2026 yürürlük durumu",
    "sermaye_piyasasi_ve_finans": "6362 sayılı Sermaye Piyasası Kanunu, 17.07.2026 yürürlük durumu",
}

SOURCE_REFS = {
    "demo-finansal-001": "1 Sıra No.lu MSUGT, Muhasebenin Temel Kavramları: işletmenin kişiliği",
    "demo-finansal-002": "Tekdüzen Hesap Planı: 100, 180 ve 280 hesapları; dönemsellik kavramı",
    "demo-maliyet-001": "SMMM Maliyet Muhasebesi kapsamı – değişken maliyet davranışı",
    "demo-maliyet-002": "SMMM Maliyet Muhasebesi kapsamı – birim sabit maliyet",
    "demo-yonetim-001": "SMMM Maliyet Muhasebesi kapsamı – ilgili ve ilgisiz maliyet",
    "demo-yonetim-002": "SMMM Maliyet Muhasebesi kapsamı – fırsat maliyeti",
    "demo-analiz-001": "Finansal tablo analizi – cari oran formülü",
    "demo-analiz-002": "Finansal tablo analizi – net kâr marjı formülü",
    "demo-analiz-003": "Finansal tablo analizi – eğilim ve grafik yorumlama",
    "demo-denetim-001": "BDS 500 Bağımsız Denetim Kanıtları, par. A8 ve A31",
    "demo-denetim-002": "BDS 330 Bağımsız Denetçinin Değerlendirilmiş Risklere Karşı Yapacağı İşler, par. 5-7",
    "demo-vuk-001": "213 sayılı Vergi Usul Kanunu m. 21 – tebliğ",
    "demo-vuk-002": "213 sayılı Vergi Usul Kanunu m. 22 – tahakkuk",
    "demo-vergi-hukuku-001": "T.C. Anayasası m. 73 – verginin kanuniliği",
    "demo-vergi-hukuku-002": "T.C. Anayasası m. 10 ve m. 73 – eşitlik ve mali güce göre vergilendirme",
    "demo-tvs-001": "Türk vergi sistemi – dolaylı ve dolaysız vergi ayrımı",
    "demo-tvs-002": "Türk vergi sistemi – ekonomik kaynağına göre vergi sınıflandırması",
    "demo-gelir-001": "193 sayılı Gelir Vergisi Kanunu m. 65 – serbest meslek kazancı",
    "demo-gelir-002": "193 sayılı Gelir Vergisi Kanunu m. 61 – ücret",
    "demo-kurumlar-001": "5520 sayılı Kurumlar Vergisi Kanunu m. 6 ve m. 11 – kurum kazancı ve kabul edilmeyen indirimler",
    "demo-kurumlar-002": "5520 sayılı Kurumlar Vergisi Kanunu m. 6 – safi kurum kazancının tespiti",
    "demo-kdv-001": "3065 sayılı Katma Değer Vergisi Kanunu m. 29 – vergi indirimi",
    "demo-kdv-002": "3065 sayılı Katma Değer Vergisi Kanunu m. 29 ve Tekdüzen Hesap Planı: 191/391 hesapları",
    "demo-ticaret-001": "6102 sayılı Türk Ticaret Kanunu m. 12 – tacir",
    "demo-ticaret-002": "6102 sayılı Türk Ticaret Kanunu m. 18/2 – basiretli iş insanı gibi hareket",
    "demo-borclar-001": "6098 sayılı Türk Borçlar Kanunu, Birinci Kısım – borç ilişkisinde alacaklı",
    "demo-borclar-002": "6098 sayılı Türk Borçlar Kanunu, Birinci Kısım – edim",
    "demo-is-001": "4857 sayılı İş Kanunu m. 8 – iş sözleşmesi",
    "demo-is-002": "6098 sayılı Türk Borçlar Kanunu m. 399 – düzenleme ve talimatlara uyma borcu",
    "demo-meslek-001": "TÜRMOB Meslek Mensupları Etik İlkeleri – tarafsızlık ilkesi",
    "demo-meslek-002": "TÜRMOB Meslek Mensupları Etik İlkeleri – gizlilik ilkesi",
    "demo-sermaye-001": "6362 sayılı Sermaye Piyasası Kanunu m. 3 – sermaye piyasası araçları; pay kavramı",
    "demo-sermaye-002": "6362 sayılı Sermaye Piyasası Kanunu m. 3 ve VII-128.8 Borçlanma Araçları Tebliği",
    "demo-finans-001": "6362 sayılı Sermaye Piyasası Kanunu m. 4 – izahname",
    "demo-finans-002": "6362 sayılı Sermaye Piyasası Kanunu m. 11 – ihraç belgesi",
}

CHOICE_REPLACEMENTS = {
    "demo-finansal-001": {
        "Önemlilik": "Sosyal sorumluluk kavramı",
    },
    "demo-denetim-001": {
        "Yönetim kararı alma": "Yönetim kararlarının alınmasına doğrudan katılma",
    },
    "demo-denetim-002": {
        "Kanıt toplamayı azaltmak": "Denetim kanıtının miktarını ve kapsamını azaltmak",
    },
}

ITEM_REPLACEMENTS = {
    "demo-vergi-hukuku-002": {
        "question": (
            "Aynı hukuki durumda bulunan mükelleflerin aynı vergilendirme kurallarına "
            "tabi tutulması hangi anayasal ilkenin gereğidir?"
        ),
        "choices": {
            "A": "Verginin genelliği",
            "B": "Vergi mahremiyeti",
            "C": "Mali güce göre vergilendirme",
            "D": "Kanunların geriye yürümezliği",
            "E": "Vergilendirmede eşitlik",
        },
        "correctAnswer": "E",
        "explanation": (
            "Anayasa'nın 10'uncu maddesindeki eşitlik ilkesi, aynı hukuki durumda "
            "bulunan mükelleflere aynı kuralların uygulanmasını gerektirir. Vergilemede "
            "farklılaştırma yapılacaksa bunun nesnel ve makul bir nedene dayanması gerekir."
        ),
    },
    "demo-kurumlar-001": {
        "question": (
            "Ticari kârın hesabında gider olarak dikkate alınan ancak vergi mevzuatınca "
            "indirimi kabul edilmeyen bir tutar, mali kâra ulaşılırken nasıl düzeltilir?"
        ),
        "choices": {
            "A": "Ticari kâra eklenir",
            "B": "Ticari kârdan yeniden indirilir",
            "C": "Yalnızca öz kaynaklardan düşülür",
            "D": "Doğrudan geçmiş yıl zararına aktarılır",
            "E": "Hesaplamada hiçbir düzeltme yapılmaz",
        },
        "correctAnswer": "A",
        "explanation": (
            "Kanunen kabul edilmeyen gider ticari kârı azaltmış olsa da vergi matrahından "
            "indirilemez. Bu nedenle ticari kâra eklenerek mali kâr hesabında düzeltilir."
        ),
    },
}

EXPLANATION_REPLACEMENTS = {
    "demo-maliyet-002": (
        "Birim sabit maliyet, toplam sabit maliyetin üretim miktarına bölünmesiyle "
        "bulunur: 24.000 TL / 6.000 birim = 4 TL/birim. Üretim arttıkça toplam "
        "sabit maliyet değişmezken birim başına sabit maliyet azalır."
    ),
    "demo-kdv-002": (
        "Ödenecek KDV, hesaplanan KDV'den indirilecek KDV çıkarılarak belirlenir. "
        "8.000 TL - 5.000 TL = 3.000 TL'dir; sonuç pozitif olduğundan bu tutar "
        "vergi dairesine ödenecek KDV'yi gösterir."
    ),
}

STIMULUS_CAPTIONS = {
    "demo-analiz-tablo-001": "Aşağıdaki iki soruyu bu ortak veri tablosuna göre cevaplayınız.",
    "demo-analiz-grafik-001": "Grafiği yorumlayarak aşağıdaki soruyu cevaplayınız.",
    "demo-analiz-kapsamli-001": (
        "4–20 numaralı sorularda aksi belirtilmedikçe bu tabloyu kullanınız. "
        "2026 ortalama ticari alacakları 200 bin TL, ortalama stokları 210 bin TL "
        "ve bir yıl 360 gündür."
    ),
}


def gen_letters(count: int, seed: int) -> list[str]:
    rng = random.Random(seed)
    letters = list("ABCDE") * (count // 5)
    letters += list("ABCDE")[: count % 5]
    while True:
        rng.shuffle(letters)
        sequence = "".join(letters)
        if all(not (sequence[i] == sequence[i - 1] == sequence[i - 2]) for i in range(2, count)):
            return letters[:]


def rebuild() -> list[dict]:
    items = json.loads(CONTENT_PATH.read_text(encoding="utf-8"))
    assert len(items) == 35
    assert set(SOURCE_REFS) == {item["id"] for item in items}

    for item in items:
        item["lessonId"] = LESSON_ALIASES.get(item["lessonId"], item["lessonId"])
        pair = (item["lessonId"], item["topicId"])
        assert pair in VALID_PAIRS, (item["id"], pair)

        item.update(ITEM_REPLACEMENTS.get(item["id"], {}))
        replacements = CHOICE_REPLACEMENTS.get(item["id"], {})
        item["choices"] = {
            key: replacements.get(value, value) for key, value in item["choices"].items()
        }
        if item["id"] in EXPLANATION_REPLACEMENTS:
            item["explanation"] = EXPLANATION_REPLACEMENTS[item["id"]]

        item["source"] = {
            "kind": "generated",
            "styleRef": "2026/1 beş seçenekli test biçimi",
            "legislationRef": SOURCE_REFS[item["id"]],
        }
        item["tags"] = [
            "Özgün Soru",
            "2026 Formatı",
            "Bölüm Havuzu",
            SECTION_LABELS[item["lessonId"]],
        ]
        item["updatedAt"] = UPDATED_AT
        item["examPeriod"] = "2026 test sistemine uyumlu özgün soru"
        item["legislationVersion"] = VERSION_BY_LESSON[item["lessonId"]]
        item["sourceUpdatedAt"] = UPDATED_AT
        item["isActive"] = True

    letters = gen_letters(len(items), seed=20260821)
    for item, answer in zip(items, letters):
        old_answer = item["correctAnswer"]
        correct = item["choices"][old_answer]
        distractors = [item["choices"][key] for key in "ABCDE" if key != old_answer]
        choices = {answer: correct}
        for key, value in zip((key for key in "ABCDE" if key != answer), distractors):
            choices[key] = value
        item["choices"] = {key: choices[key] for key in "ABCDE"}
        item["correctAnswer"] = answer

    assert len({item["id"] for item in items}) == len(items)
    assert len({item["question"] for item in items}) == len(items)
    assert all("demo" not in item["question"].casefold() for item in items)
    assert all("demo" not in item["explanation"].casefold() for item in items)
    assert all("Demo Soru" not in item["tags"] for item in items)
    return items


def rebuild_stimuli() -> list[dict]:
    items = json.loads(STIMULI_PATH.read_text(encoding="utf-8"))
    found = set()
    for item in items:
        if item["id"] in STIMULUS_CAPTIONS:
            item["caption"] = STIMULUS_CAPTIONS[item["id"]]
            item["updatedAt"] = UPDATED_AT
            found.add(item["id"])

    assert found == set(STIMULUS_CAPTIONS)
    assert all("demo" not in item.get("caption", "").casefold() for item in items)
    return items


def write(path: Path, data: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    data = rebuild()
    stimuli = rebuild_stimuli()
    write(CONTENT_PATH, data)
    write(APP_PATH, data)
    write(STIMULI_PATH, stimuli)
    write(APP_STIMULI_PATH, stimuli)
    print(
        f"demo_questions.json: {len(data)} soru | "
        f"harf {''.join(item['correctAnswer'] for item in data)} | "
        f"görünür demo 0"
    )


if __name__ == "__main__":
    main()
