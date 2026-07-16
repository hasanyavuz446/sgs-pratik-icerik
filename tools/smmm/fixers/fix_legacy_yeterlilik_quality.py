#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Eski Yeterlilik bölüm paketlerinin cevap ve şık kalitesini düzeltir.

Kapsam yalnız DUZELTME_PROMPT_2.md'deki 7 dosyadır. Konu paketlerine, SGS
içeriğine ve eski content/manifest.json dosyasına dokunmaz.

İşlemler:
- Her dosyaya özgü seed ile dengeli ve örüntüsüz cevap harfi üretir.
- Doğru cevap metnini yeni harfe, çeldiricileri diğer harflere taşır.
- Dosya başına üç mevcut soruyu aynı kavramı koruyan öncüllü biçime çevirir.
- Length-tell görülen kalan sorularda doğru metne dokunmadan iki çeldiriciyi
  anlamı değiştirmeyen nötr tamamlayıcılarla dengeler.
- İlk çalıştırmada özgün ve dönüşüm sonrası doğru metin baseline'ını kaydeder.

--verify mevcut paketleri baseline ve dağılım kurallarıyla karşılaştırır.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTENT = ROOT / "content" / "yeterlilik"
BASELINE = ROOT / "tools" / "smmm" / "baselines" / "legacy_yeterlilik_answer_baseline.json"

FILES = {
    "questions_finansal_muhasebe_2026.json": (18, 20260731),
    "questions_finansal_muhasebe_test2_2026.json": (20, 20260732),
    "questions_finansal_muhasebe_test3_2026.json": (20, 20260733),
    "questions_maliyet_muhasebesi_test2_2026.json": (20, 20260734),
    "questions_maliyet_muhasebesi_test3_2026.json": (20, 20260735),
    "questions_sermaye_piyasasi_2026.json": (18, 20260736),
    "questions_muhasebe_denetimi_2026.json": (18, 20260737),
}

COMBO_DISTRACTORS = {
    "I, II ve III": ["Yalnız I", "Yalnız II", "I ve II", "I ve III"],
    "I ve II": ["Yalnız I", "Yalnız II", "I ve III", "I, II ve III"],
    "I ve III": ["Yalnız I", "Yalnız III", "I ve II", "I, II ve III"],
    "II ve III": ["Yalnız II", "Yalnız III", "I ve II", "I, II ve III"],
    "Yalnız I": ["Yalnız II", "Yalnız III", "I ve II", "I, II ve III"],
}


def premise(intro: str, statements: list[str], correct: str, why: str) -> dict:
    assert len(statements) == 3
    assert correct in COMBO_DISTRACTORS
    return {
        "question": (
            f"Demo Soru: {intro}\n\n"
            f"I. {statements[0]}\n\n"
            f"II. {statements[1]}\n\n"
            f"III. {statements[2]}\n\n"
            "Buna göre hangileri doğrudur?"
        ),
        "correct": correct,
        "distractors": COMBO_DISTRACTORS[correct],
        "explanation": f"Demo açıklama: {why}",
    }


PREMISES = {
    # Finansal Muhasebe Test 1 — 3 öncüllü, 1/3 hepsi.
    "demo-finansal-003": premise(
        "10.000 TL + %20 KDV tutarındaki ticari malın peşin alınmasına ilişkin kayıt unsurlarını değerlendiriniz.",
        [
            "153 Ticari Mallar hesabı 10.000 TL borçlandırılır.",
            "191 İndirilecek KDV hesabı 2.000 TL borçlandırılır.",
            "100 Kasa hesabı toplam 12.000 TL alacaklandırılır.",
        ],
        "I, II ve III",
        "Mal bedeli 153 hesaba, indirilebilir KDV 191 hesaba borç; toplam ödeme 100 "
        "Kasa hesabına alacak kaydedilir.",
    ),
    "demo-finansal-010": premise(
        "100 birim 10 TL ve 100 birim 14 TL maliyetli stokların tartılı ortalamasına ilişkin ifadeleri değerlendiriniz.",
        [
            "Toplam stok maliyeti 2.400 TL'dir.",
            "Toplam stok miktarı 200 birimdir.",
            "Tartılı ortalama birim maliyet 14 TL'dir.",
        ],
        "I ve II",
        "Toplam maliyet 100×10 + 100×14 = 2.400 TL, toplam miktar 200 birim ve "
        "ortalama birim maliyet 12 TL'dir.",
    ),
    "demo-finansal-020": premise(
        "Borç toplamı 90.000 TL, alacak toplamı 88.000 TL olan geçici mizana ilişkin ifadeleri değerlendiriniz.",
        [
            "Mizanın borç ve alacak toplamları eşit değildir.",
            "2.000 TL farkın kaynağı kayıt ve aktarmalarda araştırılmalıdır.",
            "Fark araştırılmadan doğrudan sermaye hesabına aktarılmalıdır.",
        ],
        "I ve II",
        "Çift taraflı kayıtta mizan toplamları eşit olmalıdır; 2.000 TL farkın kaynağı "
        "bulunmadan sonuç veya sermaye hesabına aktarma yapılamaz.",
    ),

    # Finansal Muhasebe Test 2 — 3 öncüllü, 1/3 hepsi.
    "demo-finansal-021": premise(
        "Varlıkları 420.000 TL, borçları 170.000 TL olan işletmenin temel denklemine ilişkin ifadeleri değerlendiriniz.",
        [
            "Öz kaynak 250.000 TL'dir.",
            "Temel denklem Varlıklar = Borçlar + Öz Kaynaklar biçimindedir.",
            "420.000 = 170.000 + 250.000 eşitliği sağlanır.",
        ],
        "I, II ve III",
        "Öz kaynak 420.000 - 170.000 = 250.000 TL'dir ve temel muhasebe denklemi dengededir.",
    ),
    "demo-finansal-030": premise(
        "Gelecek ay verilecek hizmet için bu ay tahsil edilen 40.000 TL'ye ilişkin ifadeleri değerlendiriniz.",
        [
            "Hizmet edimi henüz yerine getirilmemiştir.",
            "Tahsilat, alınan avans niteliğinde bir yükümlülük doğurur.",
            "Tutar tahsil edildiği anda koşulsuz olarak hasılat kaydedilir.",
        ],
        "I ve II",
        "Hizmet henüz verilmediği için gelir kazanılmamıştır; tutar hizmet sunulana kadar "
        "müşteriye karşı yükümlülüktür.",
    ),
    "demo-finansal-040": premise(
        "TMS 16'nın önemli maddi duran varlık parçalarına yaklaşımına ilişkin ifadeleri değerlendiriniz.",
        [
            "Toplam maliyete göre önemli parça ayrı belirlenir.",
            "Yararlı ömrü farklı önemli parça kendi yararlı ömrü üzerinden amorti edilir.",
            "Bütün parçaların zorunlu olarak tek amortisman oranı kullanması gerekir.",
        ],
        "I ve II",
        "Bileşen yaklaşımında önemli ve farklı yararlı ömürlü parçalar ayrı amortismana "
        "tabi tutulur; tek oran zorunluluğu yoktur.",
    ),

    # Finansal Muhasebe Test 3 — 3 öncüllü, 1/3 hepsi.
    "demo-finansal-044": premise(
        "İşletme sahibinin kişisel ihtiyacı için kasadan 15.000 TL çekmesine ilişkin ifadeleri değerlendiriniz.",
        [
            "Kasa varlığı azalır.",
            "İşletmenin öz kaynağı azalır.",
            "İşletme açısından faaliyet gideri oluşmaz.",
        ],
        "I, II ve III",
        "Sahibin kişisel çekişi kasa ve öz kaynağı azaltır; işletmenin faaliyet gideri değildir.",
    ),
    "demo-finansal-056": premise(
        "TMS 38'e göre yararlı ömrü belirsiz maddi olmayan duran varlığa ilişkin ifadeleri değerlendiriniz.",
        [
            "Varlık amortismana tabi tutulmaz.",
            "Her yıl değer düşüklüğü testine tabi tutulur.",
            "Zorunlu olarak beş yılda tamamen amorti edilir.",
        ],
        "I ve II",
        "Yararlı ömrü belirsiz maddi olmayan duran varlık amortismana tabi değildir ve "
        "yıllık değer düşüklüğü testi gerekir.",
    ),
    "demo-finansal-058": premise(
        "TMS 38'de geliştirme harcamalarının aktifleştirilmesine ilişkin ifadeleri değerlendiriniz.",
        [
            "Teknik yapılabilirliğin gösterilmesi gerekir.",
            "Tamamlama niyeti, yeterli kaynak ve ekonomik yarar olasılığı değerlendirilir.",
            "Araştırma aşamasındaki bütün harcamalar koşulsuz olarak aktifleştirilir.",
        ],
        "I ve II",
        "Geliştirme harcamaları teknik, ticari ve güvenilir ölçüm koşulları sağlandığında "
        "aktifleştirilebilir; araştırma harcamaları koşulsuz aktifleştirilmez.",
    ),

    # Maliyet Muhasebesi Test 2 — 3 öncüllü, 1/3 hepsi.
    "demo-maliyet-025": premise(
        "Direkt ilk madde 80.000 TL, direkt işçilik 50.000 TL ve genel üretim gideri 30.000 TL olan üretime ilişkin ifadeleri değerlendiriniz.",
        [
            "Direkt ilk madde üretim maliyetinin unsurudur.",
            "Direkt işçilik üretim maliyetinin unsurudur.",
            "Toplam üretim maliyeti 160.000 TL'dir.",
        ],
        "I, II ve III",
        "Üç üretim maliyeti unsuru birlikte 80.000 + 50.000 + 30.000 = 160.000 TL'dir.",
    ),
    "demo-maliyet-035": premise(
        "Yan ürünün beklenen net satış gelirinin ana ürün maliyetinden indirilmesine ilişkin ifadeleri değerlendiriniz.",
        [
            "Yan ürünün net değeri ortak maliyetten indirilebilir.",
            "Ana ürünlere yüklenen net ortak maliyet azalır.",
            "Ana ürün maliyeti aynı tutarda artar.",
        ],
        "I ve II",
        "Yan ürünün net gerçekleşebilir değeri ortak maliyetten indirildiğinde ana ürünlere "
        "yüklenen maliyet azalır.",
    ),
    "demo-maliyet-040": premise(
        "Standart süre 1.200 saat, fiilî süre 1.100 saat ve standart ücret 15 TL iken işçilik süre sapmasına ilişkin ifadeleri değerlendiriniz.",
        [
            "Fiilî süre ile standart süre farkı 100 saattir.",
            "Sapma tutarı 100 × 15 = 1.500 TL'dir.",
            "Fiilî süre daha düşük olduğundan sapma olumsuzdur.",
        ],
        "I ve II",
        "Fiilî süre standarttan 100 saat azdır; 100×15 = 1.500 TL tutarındaki süre "
        "sapması olumludur.",
    ),

    # Maliyet Muhasebesi Test 3 — oranlar kökteki verilerden hesaplanır.
    "demo-maliyet-041": premise(
        "Satış fiyatı 80 TL, birim değişken maliyeti 50 TL olan ürüne ilişkin ifadeleri değerlendiriniz.",
        [
            "Birim katkı payı 30 TL'dir.",
            "Katkı payı satış fiyatından birim değişken maliyet çıkarılarak bulunur.",
            "Katkı payı oranı 30/80 = %37,5'tir.",
        ],
        "I, II ve III",
        "Birim katkı payı 80 - 50 = 30 TL, katkı payı oranı 30/80 = %37,5'tir.",
    ),
    "demo-maliyet-042": premise(
        "Satışları 500.000 TL, değişken maliyetleri 300.000 TL olan işletmeye ilişkin ifadeleri değerlendiriniz.",
        [
            "Toplam katkı payı 200.000 TL'dir.",
            "Katkı payı oranı %40'tır.",
            "Değişken maliyet oranı katkı payı oranıyla aynı olup %40'tır.",
        ],
        "I ve II",
        "Katkı payı 500.000 - 300.000 = 200.000 TL ve oranı 200.000/500.000 = "
        "%40'tır; değişken maliyet oranı %60'tır.",
    ),
    "demo-maliyet-045": premise(
        "Fiilî satışları 800.000 TL, başabaş satışları 600.000 TL olan işletmeye ilişkin ifadeleri değerlendiriniz.",
        [
            "Güvenlik payı tutarı 200.000 TL'dir.",
            "Güvenlik payı oranı %25'tir.",
            "Başabaş satışının fiilî satışa oranı olan %75, güvenlik payı oranıdır.",
        ],
        "I ve II",
        "Güvenlik payı 800.000 - 600.000 = 200.000 TL, oranı 200.000/800.000 = "
        "%25'tir; %75 başabaş satış oranıdır.",
    ),

    # Sermaye Piyasası — 3 öncüllü, 1/3 hepsi.
    "demo-sermaye-003": premise(
        "6362 sayılı Sermaye Piyasası Kanunu'nun amaçlarına ilişkin ifadeleri değerlendiriniz.",
        [
            "Sermaye piyasasının güvenilir, şeffaf ve etkin işlemesini desteklemek",
            "Yatırımcıların hak ve menfaatlerini korumak",
            "Sermaye piyasasının istikrarlı, adil ve rekabetçi biçimde gelişmesini sağlamak",
        ],
        "I, II ve III",
        "Kanun; piyasanın güvenilir, şeffaf, etkin, istikrarlı, adil ve rekabetçi "
        "işleyişi ile yatırımcıların korunmasını amaçlar.",
    ),
    "demo-sermaye-008": premise(
        "Halka arz kavramına ilişkin ifadeleri değerlendiriniz.",
        [
            "Sermaye piyasası araçlarının satın alınması için genel çağrıyı kapsar.",
            "Genel çağrı devamında yapılan satışı kapsar.",
            "Yalnız mevcut iki ortak arasındaki özel pay devrinden ibarettir.",
        ],
        "I ve II",
        "Halka arz, sermaye piyasası araçlarının satın alınmasına yönelik genel çağrı ve "
        "bu çağrı sonrasındaki satıştır; özel ortak devri tek başına halka arz değildir.",
    ),
    "demo-sermaye-013": premise(
        "İçsel bilgi kavramına ilişkin ifadeleri değerlendiriniz.",
        [
            "Henüz kamuya açıklanmamış somut bilgi, olay veya gelişmedir.",
            "Aracın değerini, fiyatını veya yatırımcı kararını etkileyebilir.",
            "Kamuya açık her tarihî veri kendiliğinden içsel bilgidir.",
        ],
        "I ve II",
        "İçsel bilgi kamuya açıklanmamış, somut ve aracın değeri, fiyatı veya yatırımcı "
        "kararı üzerinde etkili olabilecek bilgidir.",
    ),

    # Muhasebe Denetimi — 3 öncüllü, 1/3 hepsi.
    "demo-denetim-004": premise(
        "Mesleki şüpheciliğin gerektirdiği davranışları değerlendiriniz.",
        [
            "Sorgulayıcı bir zihinle hareket etmek",
            "Muhtemel yanlışlığa işaret eden durumlara karşı dikkatli olmak",
            "Denetim kanıtlarını eleştirel biçimde değerlendirmek",
        ],
        "I, II ve III",
        "Mesleki şüphecilik sorgulayıcı yaklaşımı, yanlışlık göstergelerine karşı dikkati "
        "ve kanıtların eleştirel değerlendirilmesini birlikte gerektirir.",
    ),
    "demo-denetim-008": premise(
        "BDS 315 kapsamındaki risk değerlendirme prosedürlerine ilişkin ifadeleri değerlendiriniz.",
        [
            "İşletme ve çevresi hakkında anlayış edinmeye yardımcı olur.",
            "Finansal tablo ve yönetim beyanı düzeyindeki önemli yanlışlık risklerini belirlemeyi sağlar.",
            "Yeterli kanıt toplamadan denetçi raporunun yazılmasını amaçlar.",
        ],
        "I ve II",
        "Risk değerlendirme prosedürleri işletme, çevresi ve iç kontrol hakkında anlayış "
        "edinerek önemli yanlışlık risklerini belirlemek ve değerlendirmek için uygulanır.",
    ),
    "demo-denetim-015": premise(
        "Bir yanlışlığın önemliliğinin değerlendirilmesine ilişkin ifadeleri değerlendiriniz.",
        [
            "Yanlışlığın büyüklüğü önemlilik değerlendirmesinde etkili olabilir.",
            "Yanlışlığın niteliği ve oluştuğu koşullar da dikkate alınır.",
            "Yönetimin yanlışlığı kabul etmesi tek başına önemliliği belirler.",
        ],
        "I ve II",
        "Önemlilik büyüklük, nitelik, koşullar ve kullanıcı kararlarına olası etkiyle "
        "değerlendirilir; yönetimin kabulü tek başına belirleyici değildir.",
    ),
}

PAD_SUFFIXES = [
    "bu değerlendirme ilgili işlemin muhasebeleştirilmesinde esas alınır",
    "ilgili kalem finansal tablolarda bu yaklaşım kullanılarak sunulur",
    "işlemin dönem sonu kaydı bu yöntem esas alınarak tamamlanır",
    "söz konusu tutar bu sınıflandırma çerçevesinde raporlanır",
    "uygulama benzer nitelikteki işlemlere de aynı biçimde yansıtılır",
    "bu ölçüt ilgili kalemin sonraki muhasebeleştirmesinde de dikkate alınır",
    "finansal tablo sunumunda bu sonuca göre işlem yapılır",
    "ilgili hesap veya kalem bu esasa göre belirlenir",
]


def gen_letters(n: int, seed: int) -> list[str]:
    """n soru için dengeli, örüntüsüz ve en fazla iki ardışık aynı harf."""
    rng = random.Random(seed)
    base = ["ABCDE"[index % 5] for index in range(n)]
    while True:
        seq = base.copy()
        rng.shuffle(seq)
        if any(
            seq[index] == seq[index - 1] == seq[index - 2]
            for index in range(2, n)
        ):
            continue
        indexes = ["ABCDE".index(letter) for letter in seq]
        steps = {
            (indexes[index + 1] - indexes[index]) % 5
            for index in range(n - 1)
        }
        if len(steps) == 1:
            continue
        periodic = any(
            sum(seq[index] == seq[index + period] for index in range(n - period))
            / (n - period)
            >= 0.9
            for period in range(1, min(10, n - 1) + 1)
        )
        if not periodic:
            return seq


def normalized_length(text: str) -> int:
    return len(re.sub(r"\*{1,2}", "", text).strip())


def has_premises(question: str) -> bool:
    return len(re.findall(r"(?m)^\s*(?:IV|I{1,3}|V)[.)]\s", question)) >= 2


def is_length_tell(question: dict) -> bool:
    if has_premises(question["question"]):
        return False
    lengths = {
        letter: normalized_length(text)
        for letter, text in question["choices"].items()
    }
    answer_length = lengths[question["correctAnswer"]]
    ordered = sorted(lengths.values(), reverse=True)
    return (
        answer_length == ordered[0]
        and answer_length >= 1.5 * ordered[1]
        and answer_length >= 45
    ) or (
        ordered[1] >= 1.7 * ordered[2]
        and ordered[1] >= 45
        and answer_length >= ordered[1]
    )


def strip_generated_padding(text: str) -> str:
    while True:
        matched = False
        for suffix in PAD_SUFFIXES:
            token = f"; {suffix}."
            if text.endswith(token):
                text = text[:-len(token)].rstrip() + "."
                matched = True
                break
        if not matched:
            return text


def add_padding(text: str, suffix: str) -> str:
    return f"{text.rstrip().rstrip('.')}; {suffix}."


def balance_distractor_lengths(question: dict) -> None:
    if not is_length_tell(question):
        return
    answer = question["correctAnswer"]
    answer_length = normalized_length(question["choices"][answer])
    target = min(145, max(55, math.ceil(answer_length * 0.76)))
    letters = [letter for letter in "ABCDE" if letter != answer]
    letters.sort(
        key=lambda letter: normalized_length(question["choices"][letter]),
        reverse=True,
    )
    used = set()
    for letter in letters[:2]:
        suffix_index = int(
            hashlib.sha256(f"{question['id']}:{letter}".encode()).hexdigest()[:8],
            16,
        ) % len(PAD_SUFFIXES)
        while normalized_length(question["choices"][letter]) < target:
            while PAD_SUFFIXES[suffix_index % len(PAD_SUFFIXES)] in used:
                suffix_index += 1
            suffix = PAD_SUFFIXES[suffix_index % len(PAD_SUFFIXES)]
            question["choices"][letter] = add_padding(
                question["choices"][letter],
                suffix,
            )
            used.add(suffix)
            suffix_index += 1
    assert not is_length_tell(question), question["id"]


def apply_premise(question: dict) -> None:
    replacement = PREMISES.get(question["id"])
    if replacement is None:
        return
    question["question"] = replacement["question"]
    question["explanation"] = replacement["explanation"]
    question["_correct_text"] = replacement["correct"]
    question["_distractors"] = replacement["distractors"]


def permute(question: dict, answer_letter: str, seed: int) -> None:
    correct_text = question.pop(
        "_correct_text",
        question["choices"][question["correctAnswer"]],
    )
    distractors = question.pop(
        "_distractors",
        [
            text
            for letter, text in question["choices"].items()
            if letter != question["correctAnswer"]
        ],
    )
    distractors = sorted(distractors)
    rng = random.Random(
        seed
        + int(hashlib.sha256(question["id"].encode()).hexdigest()[:8], 16)
    )
    rng.shuffle(distractors)
    choices = {}
    distractor_iter = iter(distractors)
    for letter in "ABCDE":
        choices[letter] = correct_text if letter == answer_letter else next(distractor_iter)
    question["choices"] = choices
    question["correctAnswer"] = answer_letter
    assert question["choices"][answer_letter] == correct_text


def load_packages() -> dict[str, list[dict]]:
    return {
        filename: json.loads((CONTENT / filename).read_text(encoding="utf-8"))
        for filename in FILES
    }


def answer_map(packages: dict[str, list[dict]]) -> dict[str, str]:
    return {
        question["id"]: question["choices"][question["correctAnswer"]]
        for questions in packages.values()
        for question in questions
    }


def verify(packages: dict[str, list[dict]]) -> None:
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    actual = answer_map(packages)
    expected = {
        question_id: record["expectedCorrect"]
        for question_id, record in baseline.items()
    }
    assert actual == expected, "Doğru cevap metinleri baseline ile eşleşmiyor."

    unchanged = 0
    converted = 0
    for question_id, record in baseline.items():
        if record["premiseConverted"]:
            converted += 1
        else:
            assert record["originalCorrect"] == record["expectedCorrect"], question_id
            unchanged += 1

    for filename, (expected_count, seed) in FILES.items():
        questions = packages[filename]
        assert len(questions) == expected_count, filename
        premise_questions = [q for q in questions if has_premises(q["question"])]
        assert len(premise_questions) == 3, (filename, len(premise_questions))
        all_answers = sum(
            q["choices"][q["correctAnswer"]] == "I, II ve III"
            for q in premise_questions
        )
        assert all_answers == 1, (filename, all_answers)
        expected_letters = gen_letters(expected_count, seed)
        assert [q["correctAnswer"] for q in questions] == expected_letters, filename
        assert all(not is_length_tell(q) for q in questions), filename

    print(f"Doğru metni aynen korunan soru: {unchanged}")
    print(f"Aynı kavramla öncüllüye dönüştürülen soru: {converted}")
    print(f"Son doğru seçenek baseline doğrulaması: {len(actual)}/{len(actual)}")
    print("Her dosyada 3 öncüllü soru; 'hepsi' 1/3 (%33,3, mümkün en yakın oran)")
    print("Length-tell: 0")


def write_packages(packages: dict[str, list[dict]]) -> None:
    for filename, questions in packages.items():
        (CONTENT / filename).write_text(
            json.dumps(questions, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    packages = load_packages()
    if args.verify:
        verify(packages)
        return

    original_answers = answer_map(packages)
    for questions in packages.values():
        for question in questions:
            question["choices"] = {
                letter: strip_generated_padding(text)
                for letter, text in question["choices"].items()
            }
            apply_premise(question)

    expected_answers = {
        question["id"]: question.get(
            "_correct_text",
            question["choices"][question["correctAnswer"]],
        )
        for questions in packages.values()
        for question in questions
    }

    for filename, (expected_count, seed) in FILES.items():
        questions = packages[filename]
        assert len(questions) == expected_count, filename
        letters = gen_letters(expected_count, seed)
        for question, answer_letter in zip(questions, letters):
            permute(question, answer_letter, seed)
            assert (
                question["choices"][question["correctAnswer"]]
                == expected_answers[question["id"]]
            )
            balance_distractor_lengths(question)

    if not BASELINE.exists():
        baseline = {
            question_id: {
                "originalCorrect": original_answers[question_id],
                "expectedCorrect": expected_answers[question_id],
                "premiseConverted": question_id in PREMISES,
            }
            for question_id in sorted(expected_answers)
        }
        BASELINE.write_text(
            json.dumps(baseline, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    write_packages(packages)
    verify(load_packages())


if __name__ == "__main__":
    main()
