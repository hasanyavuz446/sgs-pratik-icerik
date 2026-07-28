#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SGS Matematik — yeni konu: Limit, Türev ve Seriler.

Kalibrasyon (çıkmış kâğıtlardan ÖLÇÜLDÜ, kopya yok — URETIM_KURALLARI §1/§11):
  · limit 2014–2026 arasındaki HER dönemde var (2021 s.13, 2022 s.12/14, 2023 s.11/13,
    2025 s.8/s.10, 2026/1 s.15, 2026/2 s.12) — ders içindeki en sürekli başlık
  · türev 2026/2 s.13 (dy/dx), 2024 ve 2016-18 kâğıtlarında karma kısmi türev
  · sonsuz seri ∑ 1-2-3, 2016-18, 2022 ve 2026/2 s.14
  ⚠ 2026/2 s.12'deki (1 − cos x)/x² limiti ve s.13'teki (x + ln3x)/eˣ türevi
    BİLEREK kullanılmadı; yerine farklı katsayı ve farklı yapı kuruldu (§11 telif).

GÖSTERİM (§8 — app: stem/solution Markdown, ŞIKLAR düz Text):
  lim(x→a) önek biçimi · ∑(n=1→∞) · ∂z/∂x ve ∂²z/∂x∂y · f′(x) · üs ² ³ ⁿ ˣ
  Markdown'da * ve _ YASAK; çarpma ·, eksi − (U+2212)
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mat_common import main, make_q

Q: list[dict] = []
q = make_q(Q)

DERS, KONU = "matematik", "limit_turev_seri"
PREFIX = "mat-lts-gen"
STYLE = "SGS Matematik limit-türev-seri"
SEED = 20260729
RELATIVE_PATH = 'content/matematik/limit_turev_seri.json'
LABEL = 'Limit, Türev ve Seriler'




x, y, n, k, a = sp.symbols("x y n k a")
oo = sp.oo

# ══ A. 0/0 belirsizliği (11) ═════════════════════════════════════════════════
q("lim(x→2) (x² − 4)/(x − 2) limitinin değeri kaçtır?",
  "4", ["0", "2", "8", "Limit yoktur"],
  "Doğrudan yerine koymada 0/0 belirsizliği çıkar. Pay iki kare farkıdır: "
  "x² − 4 = (x − 2)(x + 2). Ortak çarpan sadeleşir ve x + 2 kalır; x → 2 için değer 4 olur.",
  verify=(sp.limit((x**2 - 4)/(x - 2), x, 2), 4))

q("lim(x→3) (x² − 5x + 6)/(x − 3) limitinin değeri kaçtır?",
  "1", ["0", "3", "−1", "6"],
  "0/0 belirsizliği vardır. Pay çarpanlarına ayrılır: x² − 5x + 6 = (x − 2)(x − 3). "
  "Ortak çarpan sadeleşir ve x − 2 kalır; x → 3 için değer 1 olur.",
  verify=(sp.limit((x**2 - 5*x + 6)/(x - 3), x, 3), 1))

q("lim(x→1) (x³ − 1)/(x − 1) limitinin değeri kaçtır?",
  "3", ["1", "0", "2", "Limit yoktur"],
  "0/0 belirsizliği vardır. Pay küp farkıdır: x³ − 1 = (x − 1)(x² + x + 1). Ortak çarpan "
  "sadeleşir ve x² + x + 1 kalır; x → 1 için 1 + 1 + 1 = 3 olur.",
  verify=(sp.limit((x**3 - 1)/(x - 1), x, 1), 3))

q("lim(x→−2) (x² + 5x + 6)/(x² − 4) limitinin değeri kaçtır?",
  "−1/4", ["1", "1/4", "−4", "0"],
  "0/0 belirsizliği vardır. Pay (x + 2)(x + 3), payda ise kare farkı olarak (x + 2)(x − 2) "
  "biçiminde ayrılır. Ortak çarpan sadeleşir ve (x + 3)/(x − 2) kalır; x → −2 için "
  "1/(−4) = −1/4 olur.",
  verify=(sp.limit((x**2 + 5*x + 6)/(x**2 - 4), x, -2), sp.Rational(-1, 4)))

q("lim(x→0) (√(x + 9) − 3)/x limitinin değeri kaçtır?",
  "1/6", ["1/3", "6", "0", "3"],
  "0/0 belirsizliği vardır. Pay ve payda eşleniği olan √(x + 9) + 3 ile çarpılır: "
  "pay x'e indirgenir ve x sadeleşir. Geriye 1/(√(x + 9) + 3) kalır; x → 0 için 1/6 olur.",
  verify=(sp.limit((sp.sqrt(x + 9) - 3)/x, x, 0), sp.Rational(1, 6)))

q("lim(x→4) (x − 4)/(√x − 2) limitinin değeri kaçtır?",
  "4", ["2", "1/4", "0", "8"],
  "0/0 belirsizliği vardır. Payda eşleniği √x + 2 ile genişletilir; payda x − 4 olur ve "
  "sadeleşme sonrası √x + 2 kalır. x → 4 için 2 + 2 = 4 bulunur.",
  verify=(sp.limit((x - 4)/(sp.sqrt(x) - 2), x, 4), 4))

q("lim(x→1) (x² − 1)/(x² + 3x − 4) limitinin değeri kaçtır?",
  "2/5", ["5/2", "1/4", "0", "2"],
  "0/0 belirsizliği vardır. Pay (x − 1)(x + 1), payda (x − 1)(x + 4) biçiminde çarpanlarına "
  "ayrılır. Ortak çarpan sadeleşir ve (x + 1)/(x + 4) kalır; x → 1 için 2/5 olur.",
  verify=(sp.limit((x**2 - 1)/(x**2 + 3*x - 4), x, 1), sp.Rational(2, 5)))

q("lim(x→0) (x² + 3x)/(2x) limitinin değeri kaçtır?",
  "3/2", ["0", "3", "1/2", "2/3"],
  "0/0 belirsizliği vardır. Payda ortak x parantezine alınır: x(x + 3)/(2x). "
  "x sadeleşir ve (x + 3)/2 kalır; x → 0 için 3/2 olur.",
  verify=(sp.limit((x**2 + 3*x)/(2*x), x, 0), sp.Rational(3, 2)))

q("lim(x→2) (x³ − 8)/(x² − 4) limitinin değeri kaçtır?",
  "3", ["12", "4", "0", "6"],
  "0/0 belirsizliği vardır. Pay küp farkı (x − 2)(x² + 2x + 4), payda kare farkı "
  "(x − 2)(x + 2) biçimindedir. Sadeleşme sonrası (x² + 2x + 4)/(x + 2) kalır; "
  "x → 2 için 12/4 = 3 olur.",
  verify=(sp.limit((x**3 - 8)/(x**2 - 4), x, 2), 3))

q("lim(x→−1) (x² + 2x + 1)/(x + 1) limitinin değeri kaçtır?",
  "0", ["1", "−1", "2", "Limit yoktur"],
  "0/0 belirsizliği vardır. Pay tam karedir: x² + 2x + 1 = (x + 1)². Sadeleşme sonrası "
  "x + 1 kalır; x → −1 için 0 olur.",
  verify=(sp.limit((x**2 + 2*x + 1)/(x + 1), x, -1), 0))

q("lim(x→1) (√x − 1)/(x − 1) limitinin değeri kaçtır?",
  "1/2", ["2", "1", "0", "1/4"],
  "0/0 belirsizliği vardır. Payda x − 1 = (√x − 1)(√x + 1) biçiminde yazılır. "
  "Ortak çarpan sadeleşir ve 1/(√x + 1) kalır; x → 1 için 1/2 olur.",
  verify=(sp.limit((sp.sqrt(x) - 1)/(x - 1), x, 1), sp.Rational(1, 2)))

# ══ B. Sonsuzda limit (5) ════════════════════════════════════════════════════
q("lim(x→∞) (3x² + 2x − 1)/(x² − 5) limitinin değeri kaçtır?",
  "3", ["0", "∞", "1/3", "2"],
  "Pay ve paydanın dereceleri eşittir. Bu durumda limit, en yüksek dereceli terimlerin "
  "katsayıları oranına eşittir: 3/1 = 3.",
  verify=(sp.limit((3*x**2 + 2*x - 1)/(x**2 - 5), x, oo), 3))

q("lim(x→∞) (2x + 7)/(5x − 3) limitinin değeri kaçtır?",
  "2/5", ["5/2", "0", "∞", "7/3"],
  "Pay ve payda birinci derecedendir. Limit, baş katsayıların oranıdır: 2/5.",
  verify=(sp.limit((2*x + 7)/(5*x - 3), x, oo), sp.Rational(2, 5)))

q("lim(x→∞) (x² + 1)/(x³ − 4) limitinin değeri kaçtır?",
  "0", ["1", "∞", "−1/4", "1/3"],
  "Paydanın derecesi paydan büyüktür. Bu durumda oran sonsuzda sıfıra yaklaşır; limit 0'dır.",
  verify=(sp.limit((x**2 + 1)/(x**3 - 4), x, oo), 0))

q("lim(x→∞) (4x³ − x)/(2x² + 9) limitinin değeri kaçtır?",
  "∞", ["2", "0", "−∞", "4/9"],
  "Payın derecesi paydanınkinden büyüktür. Bu durumda ifade sınırsız büyür; limit ∞ olur.",
  verify=(sp.limit((4*x**3 - x)/(2*x**2 + 9), x, oo), oo))

q("lim(x→∞) (√(x² + 3x) − x) limitinin değeri kaçtır?",
  "3/2", ["0", "3", "∞", "1/2"],
  "∞ − ∞ belirsizliği vardır. İfade eşleniği √(x² + 3x) + x ile genişletilir; pay 3x olur. "
  "Payda x parantezine alınıp sadeleştirilirse 3/(√(1 + 3/x) + 1) kalır ve x → ∞ için 3/2 olur.",
  verify=(sp.limit(sp.sqrt(x**2 + 3*x) - x, x, oo), sp.Rational(3, 2)))

# ══ C. Trigonometrik limit (5) ═══════════════════════════════════════════════
q("lim(x→0) (sin 3x)/x limitinin değeri kaçtır?",
  "3", ["1", "0", "1/3", "Limit yoktur"],
  "sin u / u ifadesinin u → 0 limiti 1'dir. İfade (sin 3x)/(3x) · 3 biçiminde yazılır; "
  "birinci çarpanın limiti 1 olduğundan sonuç 3'tür.",
  verify=(sp.limit(sp.sin(3*x)/x, x, 0), 3))

q("lim(x→0) (tan 5x)/(2x) limitinin değeri kaçtır?",
  "5/2", ["2/5", "5", "1/2", "0"],
  "tan u / u ifadesinin u → 0 limiti 1'dir. İfade (tan 5x)/(5x) · (5/2) biçiminde yazılır; "
  "birinci çarpanın limiti 1 olduğundan sonuç 5/2'dir.",
  verify=(sp.limit(sp.tan(5*x)/(2*x), x, 0), sp.Rational(5, 2)))

q("lim(x→0) (1 − cos 2x)/x² limitinin değeri kaçtır?",
  "2", ["1/2", "0", "1", "4"],
  "Yarım açı özdeşliği kullanılır: 1 − cos 2x = 2sin²x. İfade 2·(sin x / x)² biçimine gelir; "
  "sin x / x limiti 1 olduğundan sonuç 2'dir.",
  verify=(sp.limit((1 - sp.cos(2*x))/x**2, x, 0), 2))

q("lim(x→0) (sin 4x)/(sin 6x) limitinin değeri kaçtır?",
  "2/3", ["3/2", "0", "24", "1"],
  "Pay ve payda kendi açılarına bölünüp çarpanla düzeltilir: (sin4x/4x)·4x ÷ (sin6x/6x)·6x. "
  "Her iki oranın limiti 1 olduğundan sonuç 4/6 = 2/3'tür.",
  verify=(sp.limit(sp.sin(4*x)/sp.sin(6*x), x, 0), sp.Rational(2, 3)))

q("lim(x→0) (x · sin x)/(1 − cos x) limitinin değeri kaçtır?",
  "2", ["1", "0", "1/2", "∞"],
  "Payda 1 − cos x = 2sin²(x/2) yazılır; pay ve payda x² ile normalleştirilir. "
  "Payın x² ile oranı 1'e, paydanınki 1/2'ye gider; sonuç 1 ÷ (1/2) = 2 olur.",
  verify=(sp.limit(x*sp.sin(x)/(1 - sp.cos(x)), x, 0), 2))

# ══ D. Üstel ve logaritmik limit (5) ═════════════════════════════════════════
q("lim(x→0) (e³ˣ − 1)/x limitinin değeri kaçtır?",
  "3", ["1", "0", "1/3", "e³"],
  "(eᵘ − 1)/u ifadesinin u → 0 limiti 1'dir. İfade (e³ˣ − 1)/(3x) · 3 biçiminde yazılır; "
  "birinci çarpanın limiti 1 olduğundan sonuç 3'tür.",
  verify=(sp.limit((sp.exp(3*x) - 1)/x, x, 0), 3))

q("lim(x→∞) (1 + 2/x)ˣ limitinin değeri kaçtır?",
  "e²", ["e", "1", "2e", "∞"],
  "(1 + a/x)ˣ ifadesinin x → ∞ limiti eᵃ'dır. Burada a = 2 olduğundan sonuç e²'dir.",
  verify=(sp.limit((1 + 2/x)**x, x, oo), sp.exp(2)))

q("lim(x→0) ln(1 + 5x)/x limitinin değeri kaçtır?",
  "5", ["1", "0", "1/5", "ln5"],
  "ln(1 + u)/u ifadesinin u → 0 limiti 1'dir. İfade ln(1 + 5x)/(5x) · 5 biçiminde yazılır; "
  "birinci çarpanın limiti 1 olduğundan sonuç 5'tir.",
  verify=(sp.limit(sp.log(1 + 5*x)/x, x, 0), 5))

q("lim(x→1) (ln x)/(x − 1) limitinin değeri kaçtır?",
  "1", ["0", "e", "∞", "−1"],
  "x − 1 = u dönüşümü yapılırsa ifade ln(1 + u)/u biçimine gelir ve u → 0 olur. "
  "Bu ifadenin limiti 1'dir.",
  verify=(sp.limit(sp.log(x)/(x - 1), x, 1), 1))

q("lim(x→∞) [ln(3x + 1) − ln x] limitinin değeri kaçtır?",
  "ln3", ["0", "∞", "3", "ln4"],
  "Logaritma farkı bölümün logaritmasıdır: ln((3x + 1)/x). Parantez içindeki oranın "
  "x → ∞ limiti 3 olduğundan sonuç ln3'tür.",
  verify=(sp.limit(sp.log(3*x + 1) - sp.log(x), x, oo), sp.log(3)))

# ══ E. Tek yönlü limit, parçalı fonksiyon, süreklilik (6) ════════════════════
q("f(x) = 2x + 1 (x < 3) ve f(x) = ax − 2 (x ≥ 3) biçiminde tanımlanan f fonksiyonu x = 3 "
  "noktasında sürekli olduğuna göre a kaçtır?",
  "3", ["2", "5", "7/3", "9"],
  "Süreklilik için soldan ve sağdan limitler eşit olmalıdır. Soldan limit 2·3 + 1 = 7; "
  "sağdan limit 3a − 2'dir. 3a − 2 = 7 → 3a = 9 → a = 3.",
  verify=(sp.solve(sp.Eq(3*a - 2, 2*3 + 1), a)[0], 3))

q("f(x) = |x − 2| / (x − 2) fonksiyonunun x = 2 noktasındaki limiti için aşağıdakilerden "
  "hangisi doğrudur?",
  "Soldan ve sağdan limitler farklı olduğundan limit yoktur",
  ["Soldan ve sağdan limitler eşit olduğundan limit 1'e eşittir",
   "Soldan ve sağdan limitler eşit olduğundan limit 0'a eşittir",
   "Fonksiyon x = 2 noktasında tanımlı olmadığından limit sıfırdır",
   "Soldan limit sağdan limitten büyük olduğundan limit −1'e eşittir"],
  "x < 2 için |x − 2| = 2 − x olduğundan soldan limit −1; x > 2 için |x − 2| = x − 2 "
  "olduğundan sağdan limit 1'dir. İki tek yönlü limit eşit olmadığından limit yoktur.")

q("lim(x→0⁺) 1/x limitinin değeri kaçtır?",
  "∞", ["0", "−∞", "1", "Limit 1'e eşittir"],
  "x sıfıra sağdan yaklaşırken pozitif ve giderek küçülür; 1/x sınırsız büyür. "
  "Bu nedenle sağdan limit ∞'dur.",
  verify=(sp.limit(1/x, x, 0, "+"), oo))

q("x ≠ 3 için f(x) = (x² − 9)/(x − 3) ve f(3) = k biçiminde tanımlanan f fonksiyonu x = 3 "
  "noktasında sürekli olduğuna göre k kaçtır?",
  "6", ["0", "3", "9", "−6"],
  "Sadeleştirme sonrası x ≠ 3 için f(x) = x + 3 olur ve x → 3 limiti 6'dır. Süreklilik için "
  "fonksiyon değeri limite eşit olmalıdır: k = 6.",
  verify=(sp.limit((x**2 - 9)/(x - 3), x, 3), 6))

q("lim(x→3⁻) (x − 3)/|x − 3| limitinin değeri kaçtır?",
  "−1", ["1", "0", "∞", "Limit yoktur"],
  "x sola, yani 3'ten küçük değerlerden yaklaşır. Bu durumda x − 3 < 0 ve |x − 3| = 3 − x "
  "olur; oran (x − 3)/(3 − x) = −1 değerini alır.",
  verify=(sp.limit((x - 3)/sp.Abs(x - 3), x, 3, "-"), -1))

q("Bir f fonksiyonunun x = a noktasında sürekli olması için aşağıdakilerden hangisi "
  "gereklidir?",
  "f(a) tanımlı, limit mevcut ve limit f(a)'ya eşit olmalıdır",
  ["Fonksiyonun o noktada türevinin bulunması tek başına yeterli olmayıp gereksizdir",
   "Fonksiyonun bütün gerçel sayılarda tanımlı olması tek başına yeterli sayılmaktadır",
   "Soldan limitin bulunması tek başına süreklilik için yeterli kabul edilmektedir",
   "Fonksiyonun grafiğinin o noktada eksenleri kesmesi koşulu aranmaktadır"],
  "Bir noktada süreklilik üç koşulun birlikte sağlanmasıdır: fonksiyon o noktada tanımlıdır, "
  "o noktadaki limiti vardır ve limit değeri fonksiyon değerine eşittir.")

# ══ F. Türev kuralları (12) ══════════════════════════════════════════════════
q("f(x) = x⁴ − 3x² + 5 olduğuna göre f′(2) kaçtır?",
  "20", ["32", "12", "8", "44"],
  "Kuvvet kuralı uygulanır: f′(x) = 4x³ − 6x. x = 2 yerine konur: 4·8 − 6·2 = 32 − 12 = 20.",
  verify=(sp.diff(x**4 - 3*x**2 + 5, x).subs(x, 2), 20))

q("f(x) = (2x + 1)(x − 3) olduğuna göre f′(1) kaçtır?",
  "−1", ["1", "3", "−3", "5"],
  "Çarpım kuralı uygulanır: f′(x) = 2(x − 3) + (2x + 1)·1 = 4x − 5. "
  "x = 1 yerine konur: 4 − 5 = −1.",
  verify=(sp.diff((2*x + 1)*(x - 3), x).subs(x, 1), -1))

q("f(x) = (3x − 1)/(x + 2) olduğuna göre f′(1) kaçtır?",
  "7/9", ["7/3", "3", "1/9", "−7/9"],
  "Bölüm kuralı uygulanır: f′(x) = [3(x + 2) − (3x − 1)] / (x + 2)² = 7/(x + 2)². "
  "x = 1 yerine konur: 7/9.",
  verify=(sp.diff((3*x - 1)/(x + 2), x).subs(x, 1), sp.Rational(7, 9)))

q("f(x) = (x² + 1)⁵ olduğuna göre f′(1) kaçtır?",
  "160", ["80", "32", "10", "320"],
  "Zincir kuralı uygulanır: f′(x) = 5(x² + 1)⁴ · 2x = 10x(x² + 1)⁴. "
  "x = 1 yerine konur: 10·1·2⁴ = 10·16 = 160.",
  verify=(sp.diff((x**2 + 1)**5, x).subs(x, 1), 160))

q("f(x) = √(3x + 4) olduğuna göre f′(4) kaçtır?",
  "3/8", ["3/4", "1/8", "4", "8/3"],
  "Zincir kuralı uygulanır: f′(x) = 3 / (2√(3x + 4)). x = 4 için içerideki ifade 16 olur ve "
  "karekökü 4'tür: f′(4) = 3/(2·4) = 3/8.",
  verify=(sp.diff(sp.sqrt(3*x + 4), x).subs(x, 4), sp.Rational(3, 8)))

q("f(x) = x³(x − 2) olduğuna göre f′(2) kaçtır?",
  "8", ["24", "12", "0", "32"],
  "İfade açılır: f(x) = x⁴ − 2x³ ve türevi f′(x) = 4x³ − 6x²'dir. "
  "x = 2 yerine konur: 32 − 24 = 8.",
  verify=(sp.diff(x**3*(x - 2), x).subs(x, 2), 8))

q("f(x) = 1/x² olduğuna göre f′(2) kaçtır?",
  "−1/4", ["1/4", "−1/2", "−4", "1/8"],
  "İfade üslü biçimde yazılır: f(x) = x⁻². Kuvvet kuralı: f′(x) = −2x⁻³ = −2/x³. "
  "x = 2 yerine konur: −2/8 = −1/4.",
  verify=(sp.diff(x**-2, x).subs(x, 2), sp.Rational(-1, 4)))

q("f(x) = (x − 1)/(x + 1) olduğuna göre f′(0) kaçtır?",
  "2", ["1", "−1", "1/2", "−2"],
  "Bölüm kuralı uygulanır: f′(x) = [(x + 1) − (x − 1)] / (x + 1)² = 2/(x + 1)². "
  "x = 0 yerine konur: 2/1 = 2.",
  verify=(sp.diff((x - 1)/(x + 1), x).subs(x, 0), 2))

q("f(x) = x⁵ − 5x fonksiyonunun türevinin sıfır olduğu x değerlerinin çarpımı kaçtır?",
  "−1", ["1", "0", "5", "−5"],
  "Türev alınır: f′(x) = 5x⁴ − 5. Sıfıra eşitlenir: 5(x⁴ − 1) = 0 → x⁴ = 1. "
  "Gerçel kökler x = 1 ve x = −1 olup çarpımları −1'dir.",
  verify=(sp.prod([r for r in sp.solve(sp.diff(x**5 - 5*x, x), x) if r.is_real]), -1))

q("f(x) = 2x³ + 3x² − 12x fonksiyonunun yerel minimum noktasının apsisi kaçtır?",
  "1", ["−2", "0", "2", "−1"],
  "Türev sıfırlanır: f′(x) = 6x² + 6x − 12 = 6(x + 2)(x − 1) → x = −2 ve x = 1. "
  "İkinci türev f″(x) = 12x + 6 olup x = 1 için pozitiftir; bu nokta yerel minimumdur.",
  verify=(sp.diff(2*x**3 + 3*x**2 - 12*x, x, 2).subs(x, 1) > 0, sp.true))

q("f(x) = √x · (x + 3) olduğuna göre f′(1) kaçtır?",
  "3", ["4", "2", "1/2", "5"],
  "Çarpım kuralı uygulanır: f′(x) = (x + 3)/(2√x) + √x. x = 1 yerine konur: "
  "4/2 + 1 = 2 + 1 = 3.",
  verify=(sp.diff(sp.sqrt(x)*(x + 3), x).subs(x, 1), 3))

q("f(x) = (2x² − x)³ olduğuna göre f′(1) kaçtır?",
  "9", ["3", "27", "6", "12"],
  "Zincir kuralı uygulanır: f′(x) = 3(2x² − x)²·(4x − 1). x = 1 için parantez içi 1, "
  "son çarpan 3 olur: 3·1·3 = 9.",
  verify=(sp.diff((2*x**2 - x)**3, x).subs(x, 1), 9))

# ══ G. Üstel/logaritmik/trigonometrik türev, teğet, ekstremum (8) ════════════
q("y = e²ˣ olduğuna göre y′(0) kaçtır?",
  "2", ["1", "0", "e²", "2e"],
  "Zincir kuralı uygulanır: y′ = 2e²ˣ. x = 0 için e⁰ = 1 olduğundan y′(0) = 2'dir.",
  verify=(sp.diff(sp.exp(2*x), x).subs(x, 0), 2))

q("y = ln(3x) olduğuna göre y′(2) kaçtır?",
  "1/2", ["3/2", "1/6", "3", "1/3"],
  "Logaritma özelliğinden ln(3x) = ln3 + ln x yazılır; sabitin türevi sıfırdır ve y′ = 1/x "
  "olur. x = 2 yerine konur: 1/2.",
  verify=(sp.diff(sp.log(3*x), x).subs(x, 2), sp.Rational(1, 2)))

q("y = x·eˣ olduğuna göre y′(0) kaçtır?",
  "1", ["0", "2", "e", "−1"],
  "Çarpım kuralı uygulanır: y′ = eˣ + x·eˣ = eˣ(1 + x). x = 0 için e⁰ = 1 ve parantez 1 "
  "olduğundan y′(0) = 1'dir.",
  verify=(sp.diff(x*sp.exp(x), x).subs(x, 0), 1))

q("y = x²·ln x olduğuna göre y′(1) kaçtır?",
  "1", ["0", "2", "e", "1/2"],
  "Çarpım kuralı uygulanır: y′ = 2x·ln x + x²·(1/x) = 2x·ln x + x. x = 1 için ln1 = 0 "
  "olduğundan y′(1) = 0 + 1 = 1'dir.",
  verify=(sp.diff(x**2*sp.log(x), x).subs(x, 1), 1))

q("y = sin 2x olduğuna göre y′(0) kaçtır?",
  "2", ["0", "1", "−2", "1/2"],
  "Zincir kuralı uygulanır: y′ = 2cos 2x. x = 0 için cos0 = 1 olduğundan y′(0) = 2'dir.",
  verify=(sp.diff(sp.sin(2*x), x).subs(x, 0), 2))

q("y = x² + 3x eğrisine (1, 4) noktasında çizilen teğetin eğimi kaçtır?",
  "5", ["4", "2", "3", "7"],
  "Teğetin eğimi o noktadaki türev değeridir: y′ = 2x + 3. x = 1 yerine konur: 2 + 3 = 5.",
  verify=(sp.diff(x**2 + 3*x, x).subs(x, 1), 5))

q("f(x) = x³ − 3x fonksiyonunun yerel maksimum değeri kaçtır?",
  "2", ["−2", "0", "1", "3"],
  "Türev sıfırlanır: f′(x) = 3x² − 3 = 0 → x = ±1. İkinci türev f″(x) = 6x olup x = −1 için "
  "negatiftir; bu nokta yerel maksimumdur. Değer f(−1) = −1 + 3 = 2'dir.",
  verify=((x**3 - 3*x).subs(x, -1), 2))

q("y = e^(x²) olduğuna göre y′(1) kaçtır?",
  "2e", ["e", "2", "e²", "2e²"],
  "Zincir kuralı uygulanır: y′ = 2x·e^(x²). x = 1 yerine konur: 2·1·e¹ = 2e.",
  verify=(sp.diff(sp.exp(x**2), x).subs(x, 1), 2*sp.E))

# ══ H. Kısmi türev (4) ═══════════════════════════════════════════════════════
q("z = x³y² olduğuna göre ∂z/∂x kısmi türevinin (1, 2) noktasındaki değeri kaçtır?",
  "12", ["4", "6", "24", "3"],
  "y sabit kabul edilerek x'e göre türev alınır: ∂z/∂x = 3x²y². "
  "x = 1 ve y = 2 yerine konur: 3·1·4 = 12.",
  verify=(sp.diff(x**3*y**2, x).subs({x: 1, y: 2}), 12))

q("z = x²y + 3xy³ olduğuna göre ∂z/∂y kısmi türevinin (1, 1) noktasındaki değeri kaçtır?",
  "10", ["4", "11", "2", "9"],
  "x sabit kabul edilerek y'ye göre türev alınır: ∂z/∂y = x² + 9xy². "
  "x = 1 ve y = 1 yerine konur: 1 + 9 = 10.",
  verify=(sp.diff(x**2*y + 3*x*y**3, y).subs({x: 1, y: 1}), 10))

q("z = x²y³ olduğuna göre ∂²z/∂x∂y karma kısmi türevinin (1, 1) noktasındaki değeri kaçtır?",
  "6", ["2", "3", "12", "9"],
  "Önce x'e göre türev alınır: ∂z/∂x = 2xy³. Sonra bu ifadenin y'ye göre türevi alınır: "
  "∂²z/∂x∂y = 6xy². (1, 1) noktasında değer 6'dır.",
  verify=(sp.diff(x**2*y**3, x, y).subs({x: 1, y: 1}), 6))

q("z = e^(xy) olduğuna göre ∂z/∂x kısmi türevinin (0, 3) noktasındaki değeri kaçtır?",
  "3", ["0", "1", "e³", "3e³"],
  "y sabit kabul edilerek x'e göre türev alınır: ∂z/∂x = y·e^(xy). x = 0 için üs sıfır ve "
  "e⁰ = 1 olduğundan değer 3·1 = 3'tür.",
  verify=(sp.diff(sp.exp(x*y), x).subs({x: 0, y: 3}), 3))

# ══ I. Seriler (4) ═══════════════════════════════════════════════════════════
q("∑(n=1→∞) 1/2ⁿ toplamının değeri kaçtır?",
  "1", ["2", "1/2", "∞", "3/2"],
  "Bu, ilk terimi 1/2 ve ortak oranı 1/2 olan sonsuz geometrik seridir. |r| < 1 olduğundan "
  "toplam a/(1 − r) formülüyle bulunur: (1/2)/(1 − 1/2) = 1.",
  verify=(sp.summation(sp.Rational(1, 2)**n, (n, 1, oo)), 1))

q("∑(n=0→∞) (1/3)ⁿ toplamının değeri kaçtır?",
  "3/2", ["1/2", "3", "2/3", "1"],
  "İlk terim n = 0 için 1, ortak oran 1/3'tür. Sonsuz geometrik seri toplamı "
  "a/(1 − r) = 1/(1 − 1/3) = 3/2 olur.",
  verify=(sp.summation(sp.Rational(1, 3)**n, (n, 0, oo)), sp.Rational(3, 2)))

q("∑(n=1→∞) 2/3ⁿ toplamının değeri kaçtır?",
  "1", ["2/3", "3", "2", "1/3"],
  "Sabit 2 toplam dışına alınır: 2·∑(1/3)ⁿ (n = 1'den başlar). Bu serinin toplamı "
  "(1/3)/(1 − 1/3) = 1/2'dir. Sonuç 2·(1/2) = 1 olur.",
  verify=(sp.summation(2*sp.Rational(1, 3)**n, (n, 1, oo)), 1))

q("∑(k=1→5) (2k − 1) toplamının değeri kaçtır?",
  "25", ["24", "20", "30", "15"],
  "Terimler yazılır: 1 + 3 + 5 + 7 + 9. Bu ilk beş tek sayının toplamıdır ve "
  "sonucu 25'tir.",
  verify=(sp.summation(2*k - 1, (k, 1, 5)), 25))


if __name__ == "__main__":
    raise SystemExit(main(
        Q, prefix=PREFIX, ders=DERS, konu=KONU, style=STYLE, seed=SEED,
        relative_path=RELATIVE_PATH, label=LABEL,
    ))
