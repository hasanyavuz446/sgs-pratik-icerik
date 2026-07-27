#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SGS Matematik — yeni konu: Fonksiyonlar, Üstel-Logaritmik İfadeler ve Analitik Geometri.

Kalibrasyon (çıkmış kâğıtlardan ÖLÇÜLDÜ, kopya yok — URETIM_KURALLARI §1/§11):
  · 2026/1 s.8  logaritmik denklem · s.12 rasyonel ifade sadeleştirme · s.13 bileşke (h∘g)(π)
  · 2026/2 s.9  sabit fonksiyon → a · s.10 parçalı tanımlı işlem
  · 2024        sabit fonksiyon · 2023 s.12/s.15 doğru denklemi, çember-doğru
  · 2025 s.13   orta nokta · 2021 s.14 parabol-doğru · 1-2-3 s.13 doğru denklemi
  → 8 matematik sorusu; kök kısa, şıklar sayı/kesir/cebirsel ifade. §2: kısa kök
    matematikte kusur değil (audit SHORT_STEM_EXEMPT_LESSONS).

GÖSTERİM (§8 — app: stem/solution Markdown, ŞIKLAR düz Text):
  üs ² ³ ⁿ ˣ ⁻¹ · alt simge log₂ log₃ · √ · ∘ bileşke · f⁻¹ ters
  çarpma · · eksi − (U+2212, mevcut paketlerle aynı) · Markdown'da * ve _ YASAK
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mat_common import main, make_q

Q: list[dict] = []
q = make_q(Q)

DERS, KONU = "matematik", "fonksiyon_ustel_logaritma_analitik"
PREFIX = "mat-fonk-gen"
STYLE = "SGS Matematik fonksiyon-logaritma-analitik"
SEED = 20260728
RELATIVE_PATH = 'content/matematik/fonksiyon_ustel_logaritma_analitik.json'
LABEL = 'Fonksiyonlar, Üstel-Logaritmik İfadeler ve Analitik Geometri'




x, y, a, b, t = sp.symbols("x y a b t")

# ══ A. Fonksiyon temelleri (9) ═══════════════════════════════════════════════
q("f(x) = √(x − 3) / (x − 5) fonksiyonunun en geniş tanım kümesi aşağıdakilerden hangisidir?",
  "[3, 5) ∪ (5, ∞)", ["(3, 5) ∪ (5, ∞)", "[3, ∞)", "(5, ∞)", "[3, 5)"],
  "Karekökün içi negatif olamaz: x − 3 ≥ 0 → x ≥ 3. Payda sıfır olamaz: x − 5 ≠ 0 → x ≠ 5. "
  "İki koşul birlikte alınır: x ≥ 3 ve x ≠ 5, yani [3, 5) ∪ (5, ∞).")

q("f: ℝ → ℝ, f(x) = (a − 3)x² + (b + 2)x + 5 fonksiyonu sabit fonksiyon olduğuna göre a + b kaçtır?",
  "1", ["5", "−1", "3", "7"],
  "Sabit fonksiyonda x'li bütün terimlerin katsayısı sıfırdır: a − 3 = 0 → a = 3 ve "
  "b + 2 = 0 → b = −2. Buradan a + b = 3 + (−2) = 1.",
  verify=(3 + (-2), 1))

q("f(x) = 3x − 1 (x ≥ 2) ve f(x) = x² + 1 (x < 2) biçiminde tanımlanan f fonksiyonu için "
  "f(5) + f(−1) toplamı kaçtır?",
  "16", ["18", "14", "20", "12"],
  "5 ≥ 2 olduğundan birinci kural geçerlidir: f(5) = 3·5 − 1 = 14. "
  "−1 < 2 olduğundan ikinci kural geçerlidir: f(−1) = (−1)² + 1 = 2. Toplam 14 + 2 = 16.",
  verify=(3*5 - 1 + ((-1)**2 + 1), 16))

q("f(x) = 2x − 7 fonksiyonunda f(a) = 9 olduğuna göre a kaçtır?",
  "8", ["1", "11", "2", "16"],
  "f(a) = 2a − 7 = 9 yazılır. İki tarafa 7 eklenir: 2a = 16. İki taraf 2'ye bölünür: a = 8.",
  verify=(sp.solve(sp.Eq(2*a - 7, 9), a)[0], 8))

q("f(x) = ax + b doğrusal fonksiyonunda f(1) = 5 ve f(3) = 11 olduğuna göre f(6) kaçtır?",
  "20", ["17", "23", "18", "14"],
  "f(1) = a + b = 5 ve f(3) = 3a + b = 11 denklemleri taraf tarafa çıkarılır: 2a = 6 → a = 3. "
  "Buradan b = 5 − 3 = 2 bulunur. f(6) = 3·6 + 2 = 20.",
  verify=(3*6 + 2, 20))

q("Tanım kümesi {−1, 0, 2} olan f(x) = 3x + 1 fonksiyonunun görüntü kümesindeki elemanların "
  "toplamı kaçtır?",
  "6", ["9", "3", "12", "5"],
  "Her elemanın görüntüsü hesaplanır: f(−1) = −2, f(0) = 1, f(2) = 7. "
  "Görüntü kümesi {−2, 1, 7} olup elemanlar toplamı −2 + 1 + 7 = 6.",
  verify=(3*(-1)+1 + 1 + (3*2+1), 6))

q("f(x) = x² − 4x + 7 fonksiyonunun alabileceği en küçük değer kaçtır?",
  "3", ["7", "2", "4", "−3"],
  "İfade tam kareye tamamlanır: x² − 4x + 7 = (x − 2)² + 3. Kare terim en küçük değerini "
  "x = 2 için sıfır olarak alır; bu durumda fonksiyonun değeri 3 olur.",
  verify=(sp.minimum(x**2 - 4*x + 7, x, sp.Reals), 3))

q("f(2x − 1) = 6x + 5 olduğuna göre f(3) kaçtır?",
  "17", ["23", "11", "13", "29"],
  "İçerideki ifadenin 3 olması istenir: 2x − 1 = 3 → x = 2. Aynı x değeri sağ tarafta "
  "yerine konur: f(3) = 6·2 + 5 = 17.",
  verify=(6*2 + 5, 17))

q("Bir f fonksiyonunun birebir olması ile ilgili aşağıdakilerden hangisi doğrudur?",
  "Farklı her iki elemanın görüntüsü de farklıdır",
  ["Görüntü kümesi ile değer kümesi her durumda eşit olmak zorundadır",
   "Tanım kümesindeki her elemanın görüntüsü aynı değere eşit olmalıdır",
   "Tanım kümesi ile değer kümesinin eleman sayıları eşit olmak zorundadır",
   "Fonksiyonun grafiği her zaman orijinden geçmek durumundadır"],
  "Birebirlik tanımı: x₁ ≠ x₂ iken f(x₁) ≠ f(x₂) olmasıdır. Görüntü kümesinin değer kümesine "
  "eşit olması örtenliktir; her elemanın aynı görüntüye gitmesi ise sabit fonksiyondur.")

# ══ B. Bileşke fonksiyon (7) ═════════════════════════════════════════════════
q("f(x) = 2x + 1 ve g(x) = x² − 3 olduğuna göre (f∘g)(2) değeri kaçtır?",
  "3", ["7", "22", "6", "11"],
  "Önce içteki fonksiyon hesaplanır: g(2) = 2² − 3 = 1. Sonuç dıştaki fonksiyonda kullanılır: "
  "f(1) = 2·1 + 1 = 3.",
  verify=(2*(2**2 - 3) + 1, 3))

q("f(x) = 3x − 2 ve g(x) = x + 4 olduğuna göre (g∘f)(5) değeri kaçtır?",
  "17", ["23", "13", "27", "11"],
  "İçteki fonksiyon f'tir: f(5) = 3·5 − 2 = 13. Bu değer g'de yerine konur: g(13) = 13 + 4 = 17.",
  verify=((3*5 - 2) + 4, 17))

q("f(x) = x² + 1 ve g(x) = 2x olduğuna göre (f∘g)(x) ifadesindeki katsayılar toplamı kaçtır?",
  "5", ["3", "9", "4", "7"],
  "(f∘g)(x) = f(2x) = (2x)² + 1 = 4x² + 1 elde edilir. Katsayılar toplamı, ifadede x yerine 1 "
  "yazılarak bulunur: 4 + 1 = 5.",
  verify=(( (2*x)**2 + 1 ).subs(x, 1), 5))

q("(f∘g)(x) = 6x + 7 ve g(x) = 2x + 1 olduğuna göre f(2) kaçtır?",
  "10", ["19", "13", "7", "16"],
  "f(2x + 1) = 6x + 7 yazılır. İçerideki ifadenin 2 olması için 2x + 1 = 2 → x = 1/2 alınır. "
  "Bu değer sağ tarafta yerine konur: f(2) = 6·(1/2) + 7 = 10.",
  verify=(6*sp.Rational(1, 2) + 7, 10))

q("h(x) = x² − 1 ve g(x) = 3x + 2 olduğuna göre (h∘g)(−1) değeri kaçtır?",
  "0", ["4", "−1", "3", "8"],
  "İçteki fonksiyon hesaplanır: g(−1) = 3·(−1) + 2 = −1. Bu değer h'de yerine konur: "
  "h(−1) = (−1)² − 1 = 0.",
  verify=((3*(-1) + 2)**2 - 1, 0))

q("f(x) = 1 / (x − 2) ve g(x) = x + 3 olduğuna göre (f∘g)(4) değeri kaçtır?",
  "1/5", ["1/2", "1/7", "5", "1/4"],
  "İçteki fonksiyon hesaplanır: g(4) = 4 + 3 = 7. Bu değer f'te yerine konur: "
  "f(7) = 1 / (7 − 2) = 1/5.",
  verify=(sp.Rational(1, (4 + 3) - 2), sp.Rational(1, 5)))

q("f(x) = 2x ve g(x) = x − 5 olduğuna göre (f∘g∘f)(3) değeri kaçtır?",
  "2", ["8", "−4", "1", "12"],
  "Bileşke içten dışa uygulanır: f(3) = 6, ardından g(6) = 6 − 5 = 1, en son f(1) = 2·1 = 2.",
  verify=(2*((2*3) - 5), 2))

# ══ C. Ters fonksiyon (5) ════════════════════════════════════════════════════
q("f(x) = 3x − 9 olduğuna göre f⁻¹(6) değeri kaçtır?",
  "5", ["9", "3", "15", "1"],
  "f⁻¹(6) aranırken f(x) = 6 denklemi çözülür: 3x − 9 = 6 → 3x = 15 → x = 5.",
  verify=(sp.solve(sp.Eq(3*x - 9, 6), x)[0], 5))

q("f(x) = (2x + 1) / (x − 3) olduğuna göre f⁻¹(3) değeri kaçtır?",
  "10", ["7", "2", "−10", "5"],
  "f(x) = 3 denklemi kurulur: (2x + 1) / (x − 3) = 3. İçler dışlar çarpılır: 2x + 1 = 3x − 9. "
  "Buradan x = 10 bulunur.",
  verify=(sp.solve(sp.Eq((2*x + 1)/(x - 3), 3), x)[0], 10))

q("f(x) = x³ + 2 olduğuna göre f⁻¹(29) değeri kaçtır?",
  "3", ["27", "9", "31", "5"],
  "f(x) = 29 denklemi çözülür: x³ + 2 = 29 → x³ = 27 → x = 3.",
  verify=(sp.real_roots(x**3 + 2 - 29)[0], 3))

q("f(x) = 2x + 7 olduğuna göre f⁻¹(x) aşağıdakilerden hangisidir?",
  "(x − 7) / 2", ["(x + 7) / 2", "2x − 7", "1 / (2x + 7)", "(7 − x) / 2"],
  "y = 2x + 7 eşitliğinde x çekilir: 2x = y − 7 → x = (y − 7) / 2. Değişken adı x'e çevrilir: "
  "f⁻¹(x) = (x − 7) / 2.")

q("f(x) = 5x − 4 ve g(x) = x + 2 olduğuna göre (f∘g)⁻¹(21) değeri kaçtır?",
  "3", ["5", "1", "7", "9"],
  "Önce bileşke yazılır: (f∘g)(x) = 5(x + 2) − 4 = 5x + 6. Sonra 5x + 6 = 21 denklemi çözülür: "
  "5x = 15 → x = 3.",
  verify=(sp.solve(sp.Eq(5*(x + 2) - 4, 21), x)[0], 3))

# ══ D. Tanımlı (özel) işlem (4) ══════════════════════════════════════════════
q("Her a, b gerçel sayısı için a ⊗ b = a² − 2b biçiminde tanımlanan işleme göre 3 ⊗ 5 kaçtır?",
  "−1", ["19", "1", "−4", "11"],
  "Tanımda a yerine 3, b yerine 5 yazılır: 3 ⊗ 5 = 3² − 2·5 = 9 − 10 = −1.",
  verify=(3**2 - 2*5, -1))

q("a △ b işlemi, a > b için a² + b; a ≤ b için 2b − a biçiminde tanımlanmıştır. "
  "Buna göre (5 △ 2) + (1 △ 4) toplamı kaçtır?",
  "34", ["30", "36", "27", "41"],
  "5 > 2 olduğundan birinci kural: 5 △ 2 = 5² + 2 = 27. 1 ≤ 4 olduğundan ikinci kural: "
  "1 △ 4 = 2·4 − 1 = 7. Toplam 27 + 7 = 34.",
  verify=((5**2 + 2) + (2*4 - 1), 34))

q("x ≠ y olmak üzere x ✻ y = (x + y) / (x − y) biçiminde tanımlanan işleme göre 7 ✻ 3 kaçtır?",
  "5/2", ["2/5", "10", "4/10", "−5/2"],
  "Tanımda x yerine 7, y yerine 3 yazılır: 7 ✻ 3 = (7 + 3) / (7 − 3) = 10/4 = 5/2.",
  verify=(sp.Rational(7 + 3, 7 - 3), sp.Rational(5, 2)))

q("a ⊙ b = 3a − 2b biçiminde tanımlanan işlemde a ⊙ 4 = 7 olduğuna göre a kaçtır?",
  "5", ["1", "3", "−5", "15"],
  "Tanım uygulanır: 3a − 2·4 = 7 → 3a − 8 = 7 → 3a = 15 → a = 5.",
  verify=(sp.solve(sp.Eq(3*a - 2*4, 7), a)[0], 5))

# ══ E. Üslü ifadeler ve üstel denklem (7) ════════════════════════════════════
q("2ˣ⁺³ = 32 denklemini sağlayan x kaçtır?",
  "2", ["5", "3", "8", "4"],
  "Sağ taraf aynı tabana çevrilir: 32 = 2⁵. Tabanlar eşit olduğundan üsler eşitlenir: "
  "x + 3 = 5 → x = 2.",
  verify=(sp.solve(sp.Eq(x + 3, 5), x)[0], 2))

q("3²ˣ⁻¹ = 27 denklemini sağlayan x kaçtır?",
  "2", ["1", "3", "4", "5"],
  "27 = 3³ yazılır. Tabanlar eşit olduğundan üsler eşitlenir: 2x − 1 = 3 → 2x = 4 → x = 2.",
  verify=(sp.solve(sp.Eq(2*x - 1, 3), x)[0], 2))

q("(2³ · 2⁵) / 2⁶ işleminin sonucu kaçtır?",
  "4", ["2", "8", "16", "64"],
  "Çarpmada üsler toplanır: 2³ · 2⁵ = 2⁸. Bölmede üsler çıkarılır: 2⁸ / 2⁶ = 2² = 4.",
  verify=(sp.Integer(2**3 * 2**5) / 2**6, 4))

q("9ˣ = 27 denklemini sağlayan x kaçtır?",
  "3/2", ["2/3", "3", "1/3", "9/2"],
  "İki taraf 3 tabanına çevrilir: (3²)ˣ = 3³ → 3²ˣ = 3³. Üsler eşitlenir: 2x = 3 → x = 3/2.",
  verify=(sp.solve(sp.Eq(2*x, 3), x)[0], sp.Rational(3, 2)))

q("5ˣ = 3 olduğuna göre 25ˣ değeri kaçtır?",
  "9", ["6", "15", "10", "27"],
  "25 = 5² olduğundan 25ˣ = (5²)ˣ = (5ˣ)² yazılır. Verilen değer yerine konur: 3² = 9.",
  verify=(sp.Integer(3)**2, 9))

q("(0,2)⁻² işleminin sonucu kaçtır?",
  "25", ["0,04", "−25", "1/25", "5"],
  "0,2 = 1/5 yazılır. Negatif üs ters çevirir: (1/5)⁻² = 5² = 25.",
  verify=(sp.Rational(1, 5)**-2, 25))

q("4ˣ⁺¹ = 8ˣ⁻¹ denklemini sağlayan x kaçtır?",
  "5", ["1", "2", "3", "7"],
  "İki taraf 2 tabanına çevrilir: 2^(2x+2) = 2^(3x−3). Üsler eşitlenir: 2x + 2 = 3x − 3 → x = 5.",
  verify=(sp.solve(sp.Eq(2*x + 2, 3*x - 3), x)[0], 5))

# ══ F. Logaritma ve doğal logaritma (11) ═════════════════════════════════════
q("log₂(3x − 2) = 4 denklemini sağlayan x kaçtır?",
  "6", ["2", "4", "8", "3"],
  "Logaritma üstel biçime çevrilir: 3x − 2 = 2⁴ = 16. Buradan 3x = 18 → x = 6.",
  verify=(sp.solve(sp.Eq(3*x - 2, 16), x)[0], 6))

q("log₅125 işleminin sonucu kaçtır?",
  "3", ["5", "25", "1/3", "2"],
  "125 = 5³ olduğundan log₅125 = log₅5³ = 3 bulunur.",
  verify=(sp.log(125, 5), 3))

q("log2 = a ve log3 = b olduğuna göre log12 ifadesinin a ve b türünden eşiti nedir?",
  "2a + b", ["a + 2b", "a + b", "2ab", "a·b²"],
  "12 çarpanlarına ayrılır: 12 = 2² · 3. Çarpımın logaritması toplanır, üs öne çıkar: "
  "log12 = 2log2 + log3 = 2a + b.")

q("log₃81 − log₂16 işleminin sonucu kaçtır?",
  "0", ["4", "2", "−4", "8"],
  "81 = 3⁴ olduğundan log₃81 = 4; 16 = 2⁴ olduğundan log₂16 = 4. Fark 4 − 4 = 0.",
  verify=(sp.log(81, 3) - sp.log(16, 2), 0))

q("ln(1/e³) işleminin sonucu kaçtır?",
  "−3", ["3", "1/3", "−1/3", "e³"],
  "Negatif üs kuralı uygulanır: 1/e³ = e⁻³. Doğal logaritmanın tabanı e olduğundan "
  "ln e⁻³ = −3 bulunur.",
  verify=(sp.log(sp.exp(-3)), -3))

q("log₄x = −2 olduğuna göre x kaçtır?",
  "1/16", ["16", "−16", "1/8", "−1/16"],
  "Üstel biçime geçilir: x = 4⁻². Negatif üs ters çevirir: x = 1/4² = 1/16.",
  verify=(sp.Integer(4)**-2, sp.Rational(1, 16)))

q("log₂8 + log₃(1/9) işleminin sonucu kaçtır?",
  "1", ["5", "−1", "3", "0"],
  "8 = 2³ olduğundan log₂8 = 3. 1/9 = 3⁻² olduğundan log₃(1/9) = −2. Toplam 3 + (−2) = 1.",
  verify=(sp.log(8, 2) + sp.log(sp.Rational(1, 9), 3), 1))

q("log₆2 + log₆3 işleminin sonucu kaçtır?",
  "1", ["6", "log₆5", "0", "5"],
  "Aynı tabanlı logaritmaların toplamı, çarpımın logaritmasına eşittir: "
  "log₆2 + log₆3 = log₆(2·3) = log₆6 = 1.",
  verify=(sp.log(2, 6) + sp.log(3, 6), 1))

q("log x = 3 olduğuna göre log(100x) değeri kaçtır?",
  "5", ["6", "300", "4", "103"],
  "Çarpımın logaritması toplanır: log(100x) = log100 + log x. On tabanında log100 = 2 "
  "olduğundan sonuç 2 + 3 = 5.",
  verify=(2 + 3, 5))

q("log₂(x² − 3x) = 2 denklemini sağlayan x değerlerinin toplamı kaçtır?",
  "3", ["4", "−1", "5", "1"],
  "Üstel biçime geçilir: x² − 3x = 2² = 4 → x² − 3x − 4 = 0. Kökler x = 4 ve x = −1 olup "
  "her ikisi de x² − 3x > 0 koşulunu sağlar. Toplamları 4 + (−1) = 3.",
  verify=(sum(sp.solve(sp.Eq(x**2 - 3*x, 4), x)), 3))

q("log₃(x + 1) + log₃(x − 1) = 1 denklemini sağlayan x kaçtır?",
  "2", ["4", "−2", "3", "1"],
  "Toplam tek logaritmada birleştirilir: log₃(x² − 1) = 1 → x² − 1 = 3 → x² = 4. "
  "Kökler ±2'dir; logaritmanın tanımlı olması için x > 1 gerektiğinden x = 2 alınır.",
  verify=([s for s in sp.solve(sp.Eq(x**2 - 1, 3), x) if s > 1][0], 2))

# ══ G. Çarpanlara ayırma ve rasyonel ifade (5) ═══════════════════════════════
q("(x² − 9) / (x² − x − 6) ifadesinin sadeleştirilmiş biçimi aşağıdakilerden hangisidir?",
  "(x + 3) / (x + 2)", ["(x − 3) / (x + 2)", "(x + 3) / (x − 2)", "(x + 2) / (x + 3)",
                        "(x − 3) / (x − 2)"],
  "Pay iki kare farkıdır: x² − 9 = (x − 3)(x + 3). Payda çarpanlarına ayrılır: "
  "x² − x − 6 = (x − 3)(x + 2). Ortak (x − 3) çarpanı sadeleşir ve (x + 3)/(x + 2) kalır.",
  verify=(sp.simplify((x**2 - 9)/(x**2 - x - 6) - (x + 3)/(x + 2)), 0))

q("(4x² − 12xy + 9y²) / (2x² − xy − 3y²) ifadesinin sadeleştirilmiş biçimi hangisidir?",
  "(2x − 3y) / (x + y)", ["(2x + 3y) / (x + y)", "(2x − 3y) / (x − y)", "(x + y) / (2x − 3y)",
                          "(2x − 3y) / (x + 3y)"],
  "Pay tam karedir: 4x² − 12xy + 9y² = (2x − 3y)². Payda çarpanlarına ayrılır: "
  "2x² − xy − 3y² = (2x − 3y)(x + y). Ortak çarpan sadeleşir ve (2x − 3y)/(x + y) kalır.",
  verify=(sp.simplify((4*x**2 - 12*x*y + 9*y**2)/(2*x**2 - x*y - 3*y**2) - (2*x - 3*y)/(x + y)), 0))

q("a + b = 7 ve a·b = 10 olduğuna göre a² + b² kaçtır?",
  "29", ["49", "39", "19", "24"],
  "Özdeşlik kullanılır: (a + b)² = a² + 2ab + b². Buradan a² + b² = (a + b)² − 2ab yazılır: "
  "7² − 2·10 = 49 − 20 = 29.",
  verify=(7**2 - 2*10, 29))

q("x − 1/x = 3 olduğuna göre x² + 1/x² kaçtır?",
  "11", ["9", "7", "12", "6"],
  "Verilen eşitliğin karesi alınır: (x − 1/x)² = x² − 2 + 1/x² = 9. "
  "Buradan x² + 1/x² = 9 + 2 = 11.",
  verify=(3**2 + 2, 11))

q("(x³ − 8) / (x − 2) ifadesinin x = 1 için değeri kaçtır?",
  "7", ["3", "1", "−7", "5"],
  "Pay küp farkıdır: x³ − 8 = (x − 2)(x² + 2x + 4). Ortak çarpan sadeleşir ve x² + 2x + 4 "
  "kalır. x = 1 için 1 + 2 + 4 = 7.",
  verify=(((x**3 - 8)/(x - 2)).simplify().subs(x, 1), 7))

# ══ H. Analitik geometri (12) ════════════════════════════════════════════════
q("Analitik düzlemde A(2, −1) ve B(6, 2) noktaları arasındaki uzaklık kaç birimdir?",
  "5", ["7", "√7", "25", "√13"],
  "Uzaklık formülü uygulanır: |AB| = √((6 − 2)² + (2 − (−1))²) = √(16 + 9) = √25 = 5.",
  verify=(sp.sqrt((6 - 2)**2 + (2 - (-1))**2), 5))

q("Analitik düzlemde A(−3, 4) ve B(5, −2) noktalarını birleştiren doğru parçasının orta "
  "noktasının koordinatları hangisidir?",
  "(1, 1)", ["(2, 2)", "(1, 3)", "(4, −3)", "(−1, 1)"],
  "Orta nokta koordinatları uç noktaların ortalamasıdır: x = (−3 + 5)/2 = 1 ve "
  "y = (4 + (−2))/2 = 1. Orta nokta (1, 1) olur.",
  verify=(sp.Rational(-3 + 5, 2) + sp.Rational(4 - 2, 2), 2))

q("3x − 4y + 12 = 0 doğrusunun eğimi kaçtır?",
  "3/4", ["−3/4", "4/3", "−4/3", "3"],
  "Denklemde y yalnız bırakılır: 4y = 3x + 12 → y = (3/4)x + 3. Eğim, x'in katsayısı olan 3/4'tür.",
  verify=(sp.Rational(3, 4), sp.Rational(3, 4)))

q("Analitik düzlemde (0, 3) ve (−2, 0) noktalarından geçen doğrunun denklemi hangisidir?",
  "3x − 2y + 6 = 0", ["3x + 2y − 6 = 0", "2x − 3y + 6 = 0", "3x − 2y − 6 = 0", "2x + 3y − 6 = 0"],
  "Eğim hesaplanır: m = (3 − 0) / (0 − (−2)) = 3/2. y kesişimi 3 olduğundan y = (3/2)x + 3 "
  "yazılır. İki taraf 2 ile çarpılıp düzenlenirse 3x − 2y + 6 = 0 elde edilir.",
  verify=(sp.Rational(3 - 0, 0 - (-2)), sp.Rational(3, 2)))

q("P(2, 3) noktasının 3x + 4y − 11 = 0 doğrusuna uzaklığı kaç birimdir?",
  "7/5", ["7", "5/7", "1/5", "7/25"],
  "Noktadan doğruya uzaklık formülü uygulanır: |3·2 + 4·3 − 11| / √(3² + 4²) = "
  "|6 + 12 − 11| / 5 = 7/5.",
  verify=(sp.Abs(3*2 + 4*3 - 11)/sp.sqrt(3**2 + 4**2), sp.Rational(7, 5)))

q("y = 2x − 5 doğrusuna paralel olan ve (1, 4) noktasından geçen doğrunun y eksenini kestiği "
  "noktanın ordinatı kaçtır?",
  "2", ["−5", "4", "6", "−2"],
  "Paralel doğruların eğimleri eşittir: m = 2. Doğru y = 2x + n biçimindedir; (1, 4) yerine "
  "konur: 4 = 2 + n → n = 2. y eksenini (0, 2) noktasında keser.",
  verify=(4 - 2*1, 2))

q("Eğimi −1/3 olan bir doğruya dik olan doğrunun eğimi kaçtır?",
  "3", ["−3", "1/3", "−1/3", "1"],
  "Dik doğruların eğimleri çarpımı −1'dir: (−1/3)·m = −1 → m = 3.",
  verify=(sp.solve(sp.Eq(sp.Rational(-1, 3)*a, -1), a)[0], 3))

q("x² + y² − 6x + 8y = 0 çemberinin yarıçapı kaç birimdir?",
  "5", ["25", "7", "√7", "10"],
  "İfade tam kareye tamamlanır: (x − 3)² + (y + 4)² = 9 + 16 = 25. Sağ taraf r² olduğundan "
  "r = √25 = 5 bulunur.",
  verify=(sp.sqrt(9 + 16), 5))

q("y = x² − 6x + 5 parabolünün tepe noktasının koordinatları hangisidir?",
  "(3, −4)", ["(3, 4)", "(−3, −4)", "(6, 5)", "(3, 5)"],
  "Tepe noktasının apsisi x = −b/(2a) = 6/2 = 3'tür. Ordinat için x = 3 yerine konur: "
  "y = 9 − 18 + 5 = −4. Tepe noktası (3, −4) olur.",
  verify=((x**2 - 6*x + 5).subs(x, 3), -4))

q("y = x² − 4 parabolünün x eksenini kestiği iki nokta arasındaki uzaklık kaç birimdir?",
  "4", ["2", "8", "16", "√4"],
  "x eksenini kesim için y = 0 alınır: x² − 4 = 0 → x = −2 ve x = 2. İki nokta arasındaki "
  "uzaklık |2 − (−2)| = 4 birimdir.",
  verify=(max(sp.solve(x**2 - 4, x)) - min(sp.solve(x**2 - 4, x)), 4))

q("Köşeleri A(1, 2), B(5, 2) ve C(5, 6) olan üçgenin alanı kaç birim karedir?",
  "8", ["16", "4", "12", "10"],
  "AB kenarı yataydır ve uzunluğu 5 − 1 = 4'tür; BC kenarı düşeydir ve uzunluğu 6 − 2 = 4'tür. "
  "Bu iki kenar B köşesinde diktir, dolayısıyla alan (4·4)/2 = 8 birim karedir.",
  verify=(sp.Rational((5 - 1)*(6 - 2), 2), 8))

q("2x + 3y = 12 doğrusunun eksenlerle oluşturduğu üçgenin alanı kaç birim karedir?",
  "12", ["24", "6", "10", "18"],
  "y = 0 için 2x = 12 → x = 6; x = 0 için 3y = 12 → y = 4. Dik kenarları 6 ve 4 olan üçgenin "
  "alanı (6·4)/2 = 12 birim karedir.",
  verify=(sp.Rational(6*4, 2), 12))


if __name__ == "__main__":
    raise SystemExit(main(
        Q, prefix=PREFIX, ders=DERS, konu=KONU, style=STYLE, seed=SEED,
        relative_path=RELATIVE_PATH, label=LABEL,
    ))
