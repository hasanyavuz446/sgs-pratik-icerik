#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Maliyet Muhasebesi bölüm testlerini 2026/1 biçim profiline uyarlar.

Hedefler:
- 3 test × 20 soru,
- test başına 0 öncüllü soru,
- maliyet ve yönetim muhasebesi alt derslerinin bölüm testlerinde karışık temsili,
- konu havuzundan ayrı Bölüm Havuzu etiketi,
- eksiksiz kaynak/sürüm alanları ve geçerli müfredat kimlikleri,
- dengeli, periyodik olmayan cevap harfleri,
- içerik ve uygulama kopyalarının özdeş tutulması.

Script idempotenttir. Mevcut doğru soruları korur; yalnız REPLACEMENTS içindeki
soruları yeniden kurar ve ilk teste dört özgün soru ekler.
"""
from __future__ import annotations

import json
import random
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTENT = ROOT / "content" / "yeterlilik"
APP_CONTENT = ROOT.parent / "smmm_sgs_pratik" / "assets" / "content" / "yeterlilik"

FILES = {
    "questions_maliyet_muhasebesi_2026.json": 20260811,
    "questions_maliyet_muhasebesi_test2_2026.json": 20260812,
    "questions_maliyet_muhasebesi_test3_2026.json": 20260813,
}

VALID_TOPICS = {
    "maliyet_muhasebesi": {
        "maliyet_temelleri",
        "maliyet_unsurlari",
        "gider_dagitimlari",
        "maliyet_sistemleri",
        "uretim_kayiplari",
        "standart_maliyet",
    },
    "yonetim_muhasebesi": {
        "karar_verme",
        "maliyet_hacim_kar",
        "butceleme_planlama_kontrol",
    },
}

LEGISLATION_VERSION = (
    "TFRS 2026 Seti (Mavi Kitap) ve 2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı"
)
UPDATED_AT = "2026-07-17T00:00:00Z"
PREMISE_MARK = re.compile(r"(?m)^\s*(?:IV|I{1,3}|V)[\.)]\s")


def tr(value: int) -> str:
    return f"{value:,}".replace(",", ".")


def spec(
    question: str,
    correct: str,
    distractors: list[str],
    explanation: str,
    source_ref: str,
    lesson_id: str,
    topic_id: str,
    difficulty: str = "medium",
) -> dict:
    assert len(distractors) == 4
    assert len({correct, *distractors}) == 5
    assert topic_id in VALID_TOPICS[lesson_id]
    return {
        "lessonId": lesson_id,
        "topicId": topic_id,
        "question": question,
        "choices": dict(zip("ABCDE", [correct, *distractors])),
        "correctAnswer": "A",
        "explanation": explanation,
        "source": {
            "kind": "generated",
            "styleRef": "2026/1 beş seçenekli test biçimi",
            "legislationRef": source_ref,
        },
        "difficulty": difficulty,
    }


# Hesaplar metne gömülmeden önce Python'da doğrulanır.
_high_units, _high_cost = 10_000, 86_000
_low_units, _low_cost = 6_000, 62_000
_variable_rate = (_high_cost - _low_cost) // (_high_units - _low_units)
_fixed_cost = _high_cost - _variable_rate * _high_units
assert (_variable_rate, _fixed_cost) == (6, 26_000)

_production_budget = 10_000 + 1_400 - 1_100
assert _production_budget == 10_300

_cash_ending = 40_000 + 180_000 - 150_000
assert _cash_ending == 70_000

_normal_loss = 20_000 * 2 // 100
_abnormal_loss = 500 - _normal_loss
assert (_normal_loss, _abnormal_loss) == (400, 100)

_special_order_profit = 4_000 * (52 - 38) - 30_000
assert _special_order_profit == 26_000

_break_even_sales = 90_000 * 100 // 30
assert _break_even_sales == 300_000

_cash_budget = 25_000 + 140_000 - 155_000
assert _cash_budget == 10_000

_conversion_equivalent = 4_600 + 800 * 50 // 100
assert _conversion_equivalent == 5_000

_labor_efficiency = (600 - 550) * 30
assert _labor_efficiency == 1_500

_variable_oh_efficiency = (3_200 - 3_000) * 4
assert _variable_oh_efficiency == 800

_fixed_oh_rate = 300_000 // 15_000
_allocated_fixed_oh = _fixed_oh_rate * 10_000
_unallocated_fixed_oh = 300_000 - _allocated_fixed_oh
assert (_fixed_oh_rate, _unallocated_fixed_oh) == (20, 100_000)


REPLACEMENTS = {
    "demo-maliyet-022": spec(
        "İşletme gelecek ay 5.000 birim ürün satmayı planlamaktadır. Bütçelenen birim satış fiyatı 120 TL ise satış bütçesi tutarı kaç TL'dir?",
        "600.000 TL",
        ["500.000 TL", "605.000 TL", "620.000 TL", "720.000 TL"],
        "Satış bütçesi, planlanan satış miktarı ile bütçelenen birim satış fiyatının çarpımıdır: 5.000 × 120 = 600.000 TL.",
        "SMMM Maliyet Muhasebesi kapsamı – satış bütçesi",
        "yonetim_muhasebesi",
        "butceleme_planlama_kontrol",
        "easy",
    ),
    "demo-maliyet-023": spec(
        "Toplam sabit maliyeti 90.000 TL ve katkı payı oranı %30 olan işletmenin başabaş satış tutarı kaç TL'dir?",
        f"{tr(_break_even_sales)} TL",
        ["27.000 TL", "120.000 TL", "270.000 TL", "390.000 TL"],
        "Başabaş satış tutarı = Sabit maliyet / Katkı payı oranı = 90.000 / 0,30 = 300.000 TL'dir.",
        "SMMM Maliyet Muhasebesi kapsamı – maliyet-hacim-kâr analizi",
        "yonetim_muhasebesi",
        "maliyet_hacim_kar",
    ),
    "demo-maliyet-025": spec(
        "Direkt ilk madde ve malzeme gideri 80.000 TL, direkt işçilik gideri 50.000 TL ve genel üretim gideri 30.000 TL olan üretimin toplam maliyeti kaç TL'dir?",
        "160.000 TL",
        ["80.000 TL", "110.000 TL", "130.000 TL", "190.000 TL"],
        "Üretim maliyeti üç temel unsurun toplamıdır: 80.000 + 50.000 + 30.000 = 160.000 TL.",
        "SMMM Maliyet Muhasebesi kapsamı – üretim maliyeti unsurları",
        "maliyet_muhasebesi",
        "maliyet_unsurlari",
        "easy",
    ),
    "demo-maliyet-035": spec(
        "Atıl kapasitesi bulunan işletme 4.000 birimlik özel siparişi birim başına 52 TL'den alabilecektir. Birim değişken maliyet 38 TL, siparişe özgü ek sabit maliyet 30.000 TL ve fırsat maliyeti sıfırdır. Siparişin toplam kâra etkisi nedir?",
        f"{tr(_special_order_profit)} TL artış",
        ["30.000 TL azalış", "56.000 TL artış", "152.000 TL artış", "208.000 TL artış"],
        "Ek katkı 4.000 × (52 − 38) = 56.000 TL'dir. Siparişe özgü 30.000 TL sabit maliyet düşülünce toplam kâr 26.000 TL artar.",
        "SMMM Maliyet Muhasebesi kapsamı – özel sipariş kararı ve ilgili maliyet",
        "yonetim_muhasebesi",
        "karar_verme",
        "hard",
    ),
    "demo-maliyet-040": spec(
        "Nakit bütçesinde dönem başı nakit 25.000 TL, bütçelenen nakit tahsilatları 140.000 TL ve nakit ödemeleri 155.000 TL'dir. Finansman işlemi yoksa dönem sonu nakit mevcudu kaç TL'dir?",
        f"{tr(_cash_budget)} TL",
        ["15.000 TL açık", "25.000 TL", "35.000 TL", "320.000 TL"],
        "Dönem sonu nakit = 25.000 + 140.000 − 155.000 = 10.000 TL'dir. Sonuç pozitif olduğu için finansman öncesi nakit açığı yoktur.",
        "SMMM Maliyet Muhasebesi kapsamı – nakit bütçesi",
        "yonetim_muhasebesi",
        "butceleme_planlama_kontrol",
    ),
    "demo-maliyet-041": spec(
        "Satış fiyatı 80 TL, birim değişken maliyeti 50 TL olan ürünün katkı payı oranı yüzde kaçtır?",
        "%37,5",
        ["%30", "%50", "%60", "%62,5"],
        "Birim katkı payı 80 − 50 = 30 TL'dir. Katkı payı oranı 30 / 80 = %37,5 olarak bulunur.",
        "SMMM Maliyet Muhasebesi kapsamı – katkı payı oranı",
        "yonetim_muhasebesi",
        "maliyet_hacim_kar",
        "easy",
    ),
    "demo-maliyet-042": spec(
        "Satışları 500.000 TL ve değişken maliyetleri 300.000 TL olan işletmenin katkı payı oranı yüzde kaçtır?",
        "%40",
        ["%20", "%30", "%50", "%60"],
        "Toplam katkı payı 500.000 − 300.000 = 200.000 TL'dir. Katkı payı oranı 200.000 / 500.000 = %40'tır.",
        "SMMM Maliyet Muhasebesi kapsamı – toplam katkı payı",
        "yonetim_muhasebesi",
        "maliyet_hacim_kar",
        "easy",
    ),
    "demo-maliyet-045": spec(
        "Fiilî satışları 800.000 TL, başabaş satış tutarı 600.000 TL olan işletmenin güvenlik payı oranı yüzde kaçtır?",
        "%25",
        ["%20", "%33,3", "%60", "%75"],
        "Güvenlik payı 800.000 − 600.000 = 200.000 TL'dir. Güvenlik payı oranı 200.000 / 800.000 = %25'tir.",
        "SMMM Maliyet Muhasebesi kapsamı – güvenlik payı oranı",
        "yonetim_muhasebesi",
        "maliyet_hacim_kar",
    ),
    "demo-maliyet-047": spec(
        "Normal maliyet yöntemini kullanan sipariş maliyet sisteminde genel üretim giderleri siparişlere hangi esasla yüklenir?",
        "Fiilî faaliyet ölçüsü ile önceden belirlenmiş genel üretim gideri yükleme oranının çarpımıyla",
        [
            "Yalnız sipariş tamamlandığında ortaya çıkan fiilî genel üretim giderinin tamamıyla",
            "Direkt ilk madde giderinin her siparişte sabit kabul edilen yüzde yüzüyle",
            "Dönem satış hasılatının sipariş sayısına eşit olarak bölünmesiyle",
            "Siparişin satış fiyatından hedeflenen brüt kârın çıkarılmasıyla",
        ],
        "Normal maliyet yönteminde direkt giderler fiilî tutarlarıyla izlenir; genel üretim gideri ise gerçekleşen faaliyet ölçüsü ile önceden belirlenen yükleme oranı çarpılarak siparişe aktarılır.",
        "SMMM Maliyet Muhasebesi kapsamı – sipariş maliyeti ve normal maliyet yöntemi",
        "maliyet_muhasebesi",
        "maliyet_sistemleri",
    ),
    "demo-maliyet-048": spec(
        "Ağırlıklı ortalama yönteminde dönemde 4.600 birim tamamlanıp devredilmiş, dönem sonundaki 800 birim yarı mamul dönüşüm maliyetleri bakımından %50 tamamlanmıştır. Dönüşüm maliyeti eşdeğer birim sayısı kaçtır?",
        tr(_conversion_equivalent),
        ["4.600", "4.800", "5.200", "5.400"],
        "Tamamlanıp devredilen 4.600 birime, dönem sonu yarı mamulün 800 × %50 = 400 eşdeğer birimi eklenir: toplam 5.000 eşdeğer birim.",
        "SMMM Maliyet Muhasebesi kapsamı – safha maliyeti ve eşdeğer birim",
        "maliyet_muhasebesi",
        "maliyet_sistemleri",
    ),
    "demo-maliyet-050": spec(
        "Yardımcı gider yerleri arasındaki karşılıklı hizmetleri dikkate almadan, her yardımcı gider yerinin maliyetini doğrudan esas üretim gider yerlerine dağıtan yöntem hangisidir?",
        "Doğrudan dağıtım yöntemi",
        ["Kademeli dağıtım yöntemi", "Matematiksel dağıtım yöntemi", "Standart maliyet yöntemi", "Safha maliyeti yöntemi"],
        "Doğrudan dağıtım yöntemi, yardımcı gider yerlerinin birbirlerine sundukları hizmetleri yok sayar ve birikmiş maliyetleri doğrudan esas üretim gider yerlerine dağıtır.",
        "SMMM Maliyet Muhasebesi kapsamı – yardımcı gider yerlerinde ikinci dağıtım",
        "maliyet_muhasebesi",
        "gider_dagitimlari",
        "easy",
    ),
    "demo-maliyet-052": spec(
        "Gerçekleşen üretim için standart direkt işçilik süresi 550 saat, fiilî süre 600 saat ve standart saat ücreti 30 TL'dir. Direkt işçilik süre sapması hangisidir?",
        f"{tr(_labor_efficiency)} TL olumsuz",
        ["1.500 TL olumlu", "15.000 TL olumsuz", "16.500 TL olumlu", "18.000 TL olumsuz"],
        "Süre sapması = (Fiilî süre − Standart süre) × Standart ücret = (600 − 550) × 30 = 1.500 TL olumsuzdur.",
        "SMMM Maliyet Muhasebesi kapsamı – direkt işçilik süre sapması",
        "maliyet_muhasebesi",
        "standart_maliyet",
    ),
    "demo-maliyet-053": spec(
        "Fiilî üretimde 3.200 makine saati kullanılmış, bu üretim için standart süre 3.000 saat ve standart değişken genel üretim gideri oranı saat başına 4 TL'dir. Değişken genel üretim gideri verim sapması hangisidir?",
        f"{tr(_variable_oh_efficiency)} TL olumsuz",
        ["800 TL olumlu", "12.000 TL olumsuz", "12.800 TL olumlu", "24.800 TL olumsuz"],
        "Verim sapması = (Fiilî saat − Standart saat) × Standart değişken GÜG oranı = (3.200 − 3.000) × 4 = 800 TL olumsuzdur.",
        "SMMM Maliyet Muhasebesi kapsamı – değişken genel üretim gideri verim sapması",
        "maliyet_muhasebesi",
        "standart_maliyet",
        "hard",
    ),
    "demo-maliyet-055": spec(
        "TMS 2 kapsamında bütçelenen sabit genel üretim gideri 300.000 TL ve normal kapasite 15.000 birimdir. Dönemde geçici düşük üretim nedeniyle 10.000 birim üretilmiştir. Başka fark yoksa stok maliyetine dağıtılmayıp dönem gideri yazılacak sabit genel üretim gideri kaç TL'dir?",
        f"{tr(_unallocated_fixed_oh)} TL",
        ["0 TL", "20.000 TL", "200.000 TL", "300.000 TL"],
        "Normal kapasiteye göre sabit GÜG oranı 300.000 / 15.000 = 20 TL/birimdir. 10.000 birime 200.000 TL yüklenir; dağıtılmayan 100.000 TL dönem gideridir.",
        "TMS 2 Stoklar, par. 13 – sabit genel üretim giderlerinin normal kapasiteye göre dağıtımı",
        "maliyet_muhasebesi",
        "gider_dagitimlari",
        "hard",
    ),
}


ADDITIONS = [
    {
        "id": "yet-maliyet-t1-0017",
        **spec(
            "Toplam maliyet 10.000 birim faaliyet düzeyinde 86.000 TL, 6.000 birim faaliyet düzeyinde 62.000 TL'dir. Yüksek-düşük yöntemine göre toplam sabit maliyet kaç TL'dir?",
            f"{tr(_fixed_cost)} TL",
            ["6.000 TL", "24.000 TL", "36.000 TL", "60.000 TL"],
            "Birim değişken maliyet (86.000 − 62.000) / (10.000 − 6.000) = 6 TL'dir. Sabit maliyet 86.000 − 10.000 × 6 = 26.000 TL bulunur.",
            "SMMM Maliyet Muhasebesi kapsamı – yüksek-düşük yöntemi",
            "maliyet_muhasebesi",
            "maliyet_temelleri",
        ),
        "isPremium": False,
        "isActive": True,
    },
    {
        "id": "yet-maliyet-t1-0018",
        **spec(
            "Nakit bütçesinde dönem başı nakit 40.000 TL, bütçelenen nakit tahsilatları 180.000 TL ve nakit ödemeleri 150.000 TL'dir. Finansman işlemi yoksa dönem sonu nakit kaç TL'dir?",
            f"{tr(_cash_ending)} TL",
            ["30.000 TL", "40.000 TL", "110.000 TL", "370.000 TL"],
            "Dönem sonu nakit = 40.000 + 180.000 − 150.000 = 70.000 TL'dir.",
            "SMMM Maliyet Muhasebesi kapsamı – nakit bütçesi",
            "yonetim_muhasebesi",
            "butceleme_planlama_kontrol",
        ),
        "isPremium": False,
        "isActive": True,
    },
    {
        "id": "yet-maliyet-t1-0019",
        **spec(
            "Gelecek dönem için satış tahmini 10.000 birim, istenen dönem sonu mamul stoku 1.400 birim ve dönem başı mamul stoku 1.100 birimdir. Üretim bütçesi kaç birimdir?",
            tr(_production_budget),
            ["8.900", "9.700", "10.000", "12.500"],
            "Bütçelenen üretim = Satışlar + İstenen dönem sonu stoku − Dönem başı stoku = 10.000 + 1.400 − 1.100 = 10.300 birimdir.",
            "SMMM Maliyet Muhasebesi kapsamı – üretim bütçesi",
            "yonetim_muhasebesi",
            "butceleme_planlama_kontrol",
        ),
        "isPremium": False,
        "isActive": True,
    },
    {
        "id": "yet-maliyet-t1-0020",
        **spec(
            "Üretime 20.000 birim girilmiş, normal kayıp oranı %2 ve fiilî kayıp 500 birim olmuştur. Anormal kayıp miktarı kaç birimdir?",
            tr(_abnormal_loss),
            ["400", "500", "600", "900"],
            "Normal kayıp 20.000 × %2 = 400 birimdir. Fiilî kaybın normal sınırı aşan 500 − 400 = 100 birimi anormal kayıptır.",
            "SMMM Maliyet Muhasebesi kapsamı – normal ve anormal üretim kayıpları",
            "maliyet_muhasebesi",
            "uretim_kayiplari",
        ),
        "isPremium": False,
        "isActive": True,
    },
]


MISSING_REFS = {
    "demo-maliyet-003": "SMMM Maliyet Muhasebesi kapsamı – birincil maliyet",
    "demo-maliyet-004": "SMMM Maliyet Muhasebesi kapsamı – dönüşüm maliyeti",
    "demo-maliyet-005": "SMMM Maliyet Muhasebesi kapsamı – genel üretim gideri yükleme oranı",
    "demo-maliyet-006": "SMMM Maliyet Muhasebesi kapsamı – yardımcı gider yeri dağıtımı",
    "demo-maliyet-007": "SMMM Maliyet Muhasebesi kapsamı – sipariş maliyet sistemi",
    "demo-maliyet-008": "SMMM Maliyet Muhasebesi kapsamı – dönüşüm eşdeğer birimi",
    "demo-maliyet-009": "SMMM Maliyet Muhasebesi kapsamı – sipariş toplam maliyeti",
    "demo-maliyet-010": "SMMM Maliyet Muhasebesi kapsamı – safha maliyeti ve eşdeğer birim",
    "demo-maliyet-011": "SMMM Maliyet Muhasebesi kapsamı – normal fire",
    "demo-maliyet-012": "SMMM Maliyet Muhasebesi kapsamı – malzeme fiyat sapması",
    "demo-maliyet-013": "SMMM Maliyet Muhasebesi kapsamı – malzeme miktar sapması",
    "demo-maliyet-014": "SMMM Maliyet Muhasebesi kapsamı – üretilen mamul maliyeti",
    "demo-yonetim-003": "SMMM Maliyet Muhasebesi kapsamı – başabaş satış miktarı",
    "demo-yonetim-004": "SMMM Maliyet Muhasebesi kapsamı – güvenlik payı",
    "demo-yonetim-005": "SMMM Maliyet Muhasebesi kapsamı – özel sipariş kararı",
    "demo-yonetim-006": "SMMM Maliyet Muhasebesi kapsamı – üret veya satın al kararı",
}


def gen_letters(seed: int) -> list[str]:
    rng = random.Random(seed)
    letters = list("ABCDE") * 4
    while True:
        rng.shuffle(letters)
        sequence = "".join(letters)
        if not any(sequence[i] == sequence[i - 1] == sequence[i - 2] for i in range(2, len(sequence))):
            return letters[:]


def normalize(item: dict) -> None:
    assert item["topicId"] in VALID_TOPICS[item["lessonId"]], (item["id"], item["lessonId"], item["topicId"])
    source = item.setdefault("source", {})
    source["kind"] = "generated"
    source["styleRef"] = "2026/1 beş seçenekli test biçimi"
    if not source.get("legislationRef"):
        source["legislationRef"] = MISSING_REFS.get(
            item["id"],
            "SMMM Yeterlilik Maliyet Muhasebesi kapsamı",
        )
    item["tags"] = ["Özgün Soru", "2026 Formatı", "Bölüm Havuzu", "Maliyet Muhasebesi"]
    item["updatedAt"] = UPDATED_AT
    item["examPeriod"] = "2026 test sistemine uyumlu özgün soru"
    item["legislationVersion"] = LEGISLATION_VERSION
    item["sourceUpdatedAt"] = UPDATED_AT
    item["isActive"] = True


def rebuild(filename: str, seed: int) -> list[dict]:
    path = CONTENT / filename
    items = json.loads(path.read_text(encoding="utf-8"))
    by_id = {item["id"]: item for item in items}

    for question_id, replacement in REPLACEMENTS.items():
        if question_id not in by_id:
            continue
        preserved = {
            "id": question_id,
            "isPremium": by_id[question_id].get("isPremium", False),
            "isActive": True,
        }
        by_id[question_id].clear()
        by_id[question_id].update(preserved)
        by_id[question_id].update(replacement)

    if filename == "questions_maliyet_muhasebesi_2026.json":
        known = set(by_id)
        for addition in ADDITIONS:
            if addition["id"] not in known:
                items.append(dict(addition))
                by_id[addition["id"]] = items[-1]

    for item in items:
        normalize(item)

    letters = gen_letters(seed)
    for item, answer in zip(items, letters):
        old_answer = item["correctAnswer"]
        correct = item["choices"][old_answer]
        distractors = [item["choices"][key] for key in "ABCDE" if key != old_answer]
        choices = {answer: correct}
        for key, value in zip((key for key in "ABCDE" if key != answer), distractors):
            choices[key] = value
        item["choices"] = {key: choices[key] for key in "ABCDE"}
        item["correctAnswer"] = answer

    assert len(items) == 20, (filename, len(items))
    assert not [item["id"] for item in items if PREMISE_MARK.search(item["question"])]
    assert len({item["id"] for item in items}) == 20
    assert len({item["question"] for item in items}) == 20
    assert all("Konu Havuzu" not in item["tags"] for item in items)
    lessons = {item["lessonId"] for item in items}
    assert lessons == {"maliyet_muhasebesi", "yonetim_muhasebesi"}, (filename, lessons)
    return items


def write(path: Path, data: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    all_ids: set[str] = set()
    all_questions: set[str] = set()
    for filename, seed in FILES.items():
        data = rebuild(filename, seed)
        ids = {item["id"] for item in data}
        questions = {item["question"] for item in data}
        assert not all_ids.intersection(ids), (filename, all_ids.intersection(ids))
        assert not all_questions.intersection(questions), (filename, all_questions.intersection(questions))
        all_ids.update(ids)
        all_questions.update(questions)
        write(CONTENT / filename, data)
        write(APP_CONTENT / filename, data)
        lesson_counts = {
            lesson: sum(item["lessonId"] == lesson for item in data)
            for lesson in sorted(VALID_TOPICS)
        }
        print(
            f"{filename}: {len(data)} soru | öncüllü 0 | "
            f"alt ders {lesson_counts} | "
            f"harf {''.join(item['correctAnswer'] for item in data)}"
        )


if __name__ == "__main__":
    main()
