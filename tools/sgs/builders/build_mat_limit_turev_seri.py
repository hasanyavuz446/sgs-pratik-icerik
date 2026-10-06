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
q("Bir ilacın kandaki yoğunluğu, ilaç alındıktan t saat sonra C(t) = 12t / (t² + 4) mg/L olarak modellenmektedir (t > 0). Buna göre kandaki ilaç yoğunluğunun en yüksek olduğu andaki yoğunluk kaç mg/L'dir?",
  "3", ["2", "6", "4", "12/5"],
  "C′(t) = 12(4 − t²) / (t² + 4)² = 0 → t = 2 saat. Bu anda C(2) = 24 / 8 = 3 mg/L'dir; t = 2 değerini yoğunluk sanmak 2 verir.",
  verify=(sp.Rational(12, 1) * 2 / (2**2 + 4) if sp.solve(sp.diff(12 * x / (x**2 + 4), x), x) == [-2, 2] else 0, 3))

q("lim(x→3) (x² − 5x + 6)/(x − 3) limitinin değeri kaçtır?",
  "1", ["0", "3", "−1", "6"],
  "0/0 belirsizliği vardır. Pay çarpanlarına ayrılır: x² − 5x + 6 = (x − 2)(x − 3). "
  "Ortak çarpan sadeleşir ve x − 2 kalır; x → 3 için değer 1 olur.",
  verify=(sp.limit((x**2 - 5*x + 6)/(x - 3), x, 3), 1))

q("Bir fabrikanın x adet ürün için toplam maliyeti M(x) = x³ − 6x² + 15x + 100 ₺ olarak modellenmiştir. Marjinal maliyet M′(x) ile ifade edildiğine göre marjinal maliyetin en düşük olduğu üretim miktarındaki marjinal maliyet kaç ₺'dir?",
  "3", ["2", "15", "6", "12"],
  "M′(x) = 3x² − 12x + 15 bir paraboldür; en küçük değeri M″(x) = 6x − 12 = 0 → x = 2'de alır. M′(2) = 12 − 24 + 15 = 3 ₺.",
  verify=(sp.diff(x**3 - 6 * x**2 + 15 * x + 100, x).subs(x, sp.solve(sp.diff(x**3 - 6 * x**2 + 15 * x + 100, x, 2), x)[0]), 3))

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

q("Doğrusal bir yolda hareket eden bir aracın t. saniyedeki konumu s(t) = t³ − 9t² + 24t metre olarak verilmiştir (t ≥ 0). Buna göre aracın hızının sıfır olduğu anlardan ikincisinde aracın ivmesi kaç m/s²'dir?",
  "6", ["−6", "0", "4", "16"],
  "Hız v(t) = s′(t) = 3t² − 18t + 24 = 3(t − 2)(t − 4); hız t = 2 ve t = 4 saniyede sıfırdır. İvme a(t) = 6t − 18; t = 4 için a = 6 m/s². Birinci anda ivme −6'dır.",
  verify=(sp.diff(x**3 - 9 * x**2 + 24 * x, x, 2).subs(x, max(sp.solve(sp.diff(x**3 - 9 * x**2 + 24 * x, x), x))), 6))

q("lim(x→2) (x³ − 8)/(x² − 4) limitinin değeri kaçtır?",
  "3", ["12", "4", "0", "6"],
  "0/0 belirsizliği vardır. Pay küp farkı (x − 2)(x² + 2x + 4), payda kare farkı "
  "(x − 2)(x + 2) biçimindedir. Sadeleşme sonrası (x² + 2x + 4)/(x + 2) kalır; "
  "x → 2 için 12/4 = 3 olur.",
  verify=(sp.limit((x**3 - 8)/(x**2 - 4), x, 2), 3))

q("Bir çiftçi elindeki 40 m tel ile dikdörtgen biçimli bir alanı çevirecektir. Alanın bir kenarı bir duvara dayanacağı için o kenara tel çekilmeyecek, telin tamamı diğer üç kenarda kullanılacaktır. Buna göre çevrilebilecek en büyük alan kaç m²'dir?",
  "200", ["100", "400", "150", "225"],
  "Duvara dik kenarlar y, duvara paralel kenar 40 − 2y olsun. A(y) = y(40 − 2y); A′(y) = 40 − 4y = 0 → y = 10. En büyük alan 10 · 20 = 200 m². Duvar olmasaydı kare için 100 m² bulunurdu.",
  verify=(sp.maximum(x * (40 - 2 * x), x, sp.Interval(0, 20)), 200))

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

q("Bir ürünün t. aydaki satış miktarı S(t) = (900t + 400) / (3t + 2) bin adet olarak modellenmektedir. Uzun vadede (t → ∞) aylık satışın yaklaşacağı değer ile ilk aydaki (t = 1) satış miktarı arasındaki fark kaç bin adettir?",
  "40", ["300", "260", "200", "60"],
  "lim(t→∞) (900t + 400)/(3t + 2) = 900/3 = 300 bin adettir. S(1) = 1.300 / 5 = 260 bin adet. Fark 300 − 260 = 40 bin adet.",
  verify=(sp.limit((900 * x + 400) / (3 * x + 2), x, sp.oo) - sp.Rational(900 + 400, 3 + 2), 40))

q("Kenar uzunluğu 12 cm olan kare biçimli bir kartonun her köşesinden kenar uzunluğu x cm olan eş kareler kesilip kenarlar yukarı katlanarak üstü açık bir kutu yapılacaktır. Kutunun hacminin en büyük olması için x kaç cm olmalıdır?",
  "2", ["3", "6", "4", "1"],
  "V(x) = x(12 − 2x)², 0 < x < 6. V′(x) = (12 − 2x)(12 − 6x) = 0 → x = 2 (x = 6 kutuyu yok eder). En büyük hacim V(2) = 2 · 64 = 128 cm³'tür.",
  verify=(sp.solve(sp.diff(x * (12 - 2 * x)**2, x), x)[0], 2))

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
q("a bir gerçel sayı olmak üzere lim(x→0) (sin ax)/(x² + 2x) = 3 olduğuna göre a kaçtır?",
  "6", ["3", "3/2", "9", "12"],
  "x → 0 iken sin ax ≈ ax ve x² + 2x = x(x + 2). Limit a/(0 + 2) = a/2 = 3, buradan a = 6.",
  verify=(sp.limit(sp.sin(6*x)/(x**2 + 2*x), x, 0), 3))

q("lim(x→0) (tan 5x + sin 3x)/(2x) limitinin değeri kaçtır?",
  "4", ["5/2", "3/2", "8", "15/2"],
  "x → 0 iken tan 5x ≈ 5x ve sin 3x ≈ 3x. Limit (5x + 3x)/(2x) = 8/2 = 4.",
  verify=(sp.limit((sp.tan(5*x) + sp.sin(3*x))/(2*x), x, 0), 4))

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
q("a bir gerçel sayı olmak üzere lim(x→0) (eᵃˣ − 1)/sin 2x = 2 olduğuna göre a kaçtır?",
  "4", ["2", "1", "6", "8"],
  "x → 0 iken eᵃˣ − 1 ≈ ax ve sin 2x ≈ 2x. Limit a/2 = 2, buradan a = 4.",
  verify=(sp.limit((sp.exp(4*x) - 1)/sp.sin(2*x), x, 0), 2))

q("a bir gerçel sayı olmak üzere lim(x→∞) (1 + a/x)^(3x) = e⁶ olduğuna göre a kaçtır?",
  "2", ["3", "6", "1/2", "18"],
  "lim(x→∞) (1 + a/x)ˣ = eᵃ olduğundan verilen limit e^(3a)'dır. 3a = 6 ve a = 2.",
  verify=(sp.limit((1 + 2/x)**(3*x), x, oo), sp.exp(6)))

q("f(x) = ln(1 + 5x) ve g(x) = eˣ − 1 fonksiyonları için lim(x→0) f(x)/g(x) limitinin değeri kaçtır?",
  "5", ["1/5", "1", "0", "e⁵"],
  "x → 0 iken ln(1 + 5x) ≈ 5x ve eˣ − 1 ≈ x. Limit 5x/x = 5.",
  verify=(sp.limit(sp.log(1 + 5*x)/(sp.exp(x) - 1), x, 0), 5))

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

q("f(x) = (x + 1)/(x² − 1) fonksiyonu için lim(x→1⁺) f(x) ve lim(x→−1) f(x) limitleri sırasıyla aşağıdakilerden hangisidir?",
  "∞ ve −1/2", ["−∞ ve −1/2", "∞ ve 0", "1/2 ve −1/2", "−∞ ve 1/2"],
  "x ≠ −1 için f(x) = 1/(x − 1)'dir. x 1'e sağdan yaklaşırken payda pozitif kalarak sıfıra gider, limit ∞ olur. x → −1 için 1/(−1 − 1) = −1/2.",
  verify=(sp.limit((x + 1)/(x**2 - 1), x, 1, "+"), oo))

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
q("f(x) = x⁴ − 3x² + 5 fonksiyonunun türevinin sıfır olduğu noktalardaki fonksiyon değerlerinin toplamı kaçtır?",
  "21/2", ["5", "11/4", "13/2", "27/4"],
  "f′(x) = 4x³ − 6x = 2x(2x² − 3) = 0 ise x = 0 veya x² = 3/2. f(0) = 5; x² = 3/2 için f = 9/4 − 9/2 + 5 = 11/4. İki simetrik nokta olduğundan toplam 5 + 2 · 11/4 = 21/2.",
  verify=(sum((x**4 - 3*x**2 + 5).subs(x, r) for r in sp.solve(sp.diff(x**4 - 3*x**2 + 5, x), x)), sp.Rational(21, 2)))

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

q("f(x) = (x² + 1)⁵ ve g(x) = f(x)/(x² + 1)⁴ olduğuna göre f′(1) + g′(1) toplamı kaçtır?",
  "162", ["160", "158", "82", "2"],
  "f′(x) = 5(x² + 1)⁴ · 2x, f′(1) = 5 · 16 · 2 = 160. g(x) = x² + 1 olduğundan g′(1) = 2. Toplam 162.",
  verify=(sp.diff((x**2 + 1)**5, x).subs(x, 1) + sp.diff(x**2 + 1, x).subs(x, 1), 162))

q("f(x) = √(3x + 4) olmak üzere f(a) = 5 olduğuna göre f′(a) kaçtır?",
  "3/10", ["3/8", "1/10", "3/5", "5/3"],
  "3a + 4 = 25 olduğundan a = 7. f′(x) = 3/(2√(3x + 4)) ve f′(7) = 3/(2 · 5) = 3/10.",
  verify=(sp.diff(sp.sqrt(3*x + 4), x).subs(x, 7), sp.Rational(3, 10)))

q("f(x) = x³(x − 2) fonksiyonunun yerel minimum değeri kaçtır?",
  "−27/16", ["−1", "0", "−27/8", "3/2"],
  "f′(x) = 4x³ − 6x² = 2x²(2x − 3). x = 0'da türev işaret değiştirmez; x = 3/2'de negatiften pozitife geçer. f(3/2) = (27/8)(−1/2) = −27/16.",
  verify=((x**3*(x - 2)).subs(x, sp.Rational(3, 2)), sp.Rational(-27, 16)))

q("f(x) = 1/x² eğrisine x = 1 apsisli noktada çizilen teğetin eğimi m, x = 2 apsisli noktada çizilen teğetin eğimi n olduğuna göre m/n oranı kaçtır?",
  "8", ["4", "−8", "1/8", "2"],
  "f′(x) = −2/x³. m = f′(1) = −2 ve n = f′(2) = −1/4. m/n = (−2)/(−1/4) = 8.",
  verify=(sp.diff(1/x**2, x).subs(x, 1) / sp.diff(1/x**2, x).subs(x, 2), 8))

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

q("f(x) = (2x² − x)³ fonksiyonunun grafiğine x = 1 apsisli noktada çizilen teğetin denklemi aşağıdakilerden hangisidir?",
  "y = 9x − 8", ["y = 9x + 1", "y = 3x − 2", "y = 9x − 1", "y = x + 8"],
  "f(1) = 1. f′(x) = 3(2x² − x)²(4x − 1) ve f′(1) = 3 · 1 · 3 = 9. Teğet y − 1 = 9(x − 1), yani y = 9x − 8.",
  verify=(sp.diff((2*x**2 - x)**3, x).subs(x, 1), 9))

# ══ G. Üstel/logaritmik/trigonometrik türev, teğet, ekstremum (8) ════════════
q("f(x) = e²ˣ fonksiyonunun grafiğine x = 0 apsisli noktada çizilen teğet doğrusunun y eksenini kestiği noktanın ordinatı ile x eksenini kestiği noktanın apsisinin toplamı kaçtır?",
  "1/2", ["1", "3/2", "−1/2", "2"],
  "f(0) = 1 ve f′(x) = 2e²ˣ olduğundan f′(0) = 2. Teğet y = 2x + 1'dir. y eksenini 1'de, x eksenini −1/2'de keser. Toplam 1 − 1/2 = 1/2.",
  verify=(1 - sp.exp(0) / sp.diff(sp.exp(2*x), x).subs(x, 0), sp.Rational(1, 2)))

q("a bir gerçel sayı olmak üzere f(x) = ln(3x) + a·x fonksiyonu için f′(2) = 5/2 olduğuna göre a kaçtır?",
  "2", ["5/2", "3", "1", "3/2"],
  "ln(3x) = ln 3 + ln x olduğundan türevi 1/x'tir. f′(x) = 1/x + a ve f′(2) = 1/2 + a = 5/2, buradan a = 2.",
  verify=(sp.solve(sp.diff(sp.log(3*x) + a*x, x).subs(x, 2) - sp.Rational(5, 2), a)[0], 2))

q("f(x) = x·eˣ fonksiyonunun azalan olduğu en geniş aralık aşağıdakilerden hangisidir?",
  "(−∞, −1)", ["(−1, ∞)", "(−∞, 0)", "(0, ∞)", "(−∞, 1)"],
  "f′(x) = eˣ + x·eˣ = (x + 1)eˣ. eˣ her zaman pozitif olduğundan f′(x) < 0 koşulu x + 1 < 0, yani x < −1 ile sağlanır.",
  verify=(sp.solve(sp.diff(x*sp.exp(x), x), x)[0], -1))

q("f(x) = x²·ln x fonksiyonunun yerel minimum noktasının apsisi aşağıdakilerden hangisidir?",
  "1/√e", ["1/e", "√e", "e", "1"],
  "f′(x) = 2x·ln x + x = x(2ln x + 1). x > 0 için f′(x) = 0 ise ln x = −1/2 ve x = e^(−1/2) = 1/√e. Bu noktada türev negatiften pozitife geçtiği için yerel minimumdur.",
  verify=(sp.solve(2*sp.log(x) + 1, x)[0], sp.exp(-sp.Rational(1, 2))))

q("f(x) = sin 2x + cos 2x fonksiyonunun [0, π/2] aralığındaki en büyük değeri kaçtır?",
  "√2", ["1", "2", "√3", "1/2"],
  "f′(x) = 2cos 2x − 2sin 2x = 0 ise tan 2x = 1 ve x = π/8. f(π/8) = √2/2 + √2/2 = √2; uç noktalarda f(0) = 1 ve f(π/2) = −1 olduğundan en büyük değer √2'dir.",
  verify=(sp.sin(2*sp.pi/8) + sp.cos(2*sp.pi/8), sp.sqrt(2)))

q("y = x² + 3x eğrisine (1, 4) noktasında çizilen teğetin eğimi kaçtır?",
  "5", ["4", "2", "3", "1"],
  "Teğetin eğimi o noktadaki türev değeridir: y′ = 2x + 3. x = 1 yerine konur: 2 + 3 = 5.",
  verify=(sp.diff(x**2 + 3*x, x).subs(x, 1), 5))

q("f(x) = x³ − 3x fonksiyonunun yerel maksimum değeri kaçtır?",
  "2", ["−2", "0", "1", "3"],
  "Türev sıfırlanır: f′(x) = 3x² − 3 = 0 → x = ±1. İkinci türev f″(x) = 6x olup x = −1 için "
  "negatiftir; bu nokta yerel maksimumdur. Değer f(−1) = −1 + 3 = 2'dir.",
  verify=((x**3 - 3*x).subs(x, -1), 2))

q("g(x) = e^(x²) ve h(x) = g(2x − 1) olduğuna göre h′(1) kaçtır?",
  "4e", ["2e", "e", "4", "8e"],
  "Zincir kuralıyla h′(x) = 2·g′(2x − 1) ve g′(t) = 2t·e^(t²). x = 1 için t = 1: h′(1) = 2 · 2 · 1 · e = 4e.",
  verify=(sp.diff(sp.exp((2*x - 1)**2), x).subs(x, 1), 4*sp.E))

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
q("Yerden 9 m yükseklikten serbest bırakılan bir top, yere her çarpışından sonra bir önceki düşüş yüksekliğinin 1/3'ü kadar yükselmektedir. Top duruncaya kadar düşey doğrultuda toplam kaç metre yol alır?",
  "18", ["27", "27/2", "12", "15"],
  "İlk düşüş 9 m'dir. Sonraki her yükseliş ve düşüş eşittir: 3 + 1 + 1/3 + … = 3/(1 − 1/3) = 9/2. Toplam 9 + 2 · 9/2 = 18 m.",
  verify=(9 + 2*sp.summation(9*sp.Rational(1, 3)**n, (n, 1, oo)), 18))

q("0,272727… biçiminde 27 devreden ondalık sayı ∑(n=1→∞) 27/100ⁿ toplamı olarak yazılabilir. Bu sayının rasyonel karşılığı aşağıdakilerden hangisidir?",
  "3/11", ["27/100", "9/11", "3/10", "1/4"],
  "Geometrik seri: ilk terim 27/100, ortak oran 1/100. Toplam (27/100)/(1 − 1/100) = 27/99 = 3/11.",
  verify=(sp.summation(27/sp.Integer(100)**n, (n, 1, oo)), sp.Rational(3, 11)))

q("a bir gerçel sayı olmak üzere ∑(n=1→∞) a/3ⁿ = 3 olduğuna göre ∑(n=1→∞) a/4ⁿ toplamı kaçtır?",
  "2", ["3/2", "3", "6", "9/4"],
  "∑(n=1→∞) 1/3ⁿ = (1/3)/(1 − 1/3) = 1/2 olduğundan a/2 = 3 ve a = 6. ∑(n=1→∞) 1/4ⁿ = 1/3 olduğundan istenen toplam 6/3 = 2.",
  verify=(sp.summation(6/sp.Integer(4)**n, (n, 1, oo)), 2))

q("Bir amfitiyatronun ilk sırasında 12 koltuk vardır ve her sırada bir önceki sıradan 3 fazla koltuk bulunmaktadır. Amfitiyatroda 10 sıra olduğuna göre toplam koltuk sayısı kaçtır?",
  "255", ["315", "300", "270", "285"],
  "Koltuk sayıları ilk terimi 12, ortak farkı 3 olan aritmetik dizidir. ∑(k=1→10) (12 + 3(k − 1)) = 10/2 · (2·12 + 9·3) = 5 · 51 = 255.",
  verify=(sp.summation(12 + 3*(k - 1), (k, 1, 10)), 255))


if __name__ == "__main__":
    raise SystemExit(main(
        Q, prefix=PREFIX, ders=DERS, konu=KONU, style=STYLE, seed=SEED,
        relative_path=RELATIVE_PATH, label=LABEL,
    ))
