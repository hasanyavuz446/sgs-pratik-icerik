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

q("Doğrusal bir f fonksiyonu için f(1) = −5 ve f(4) = 1'dir. f fonksiyonunun grafiğinin x eksenini kestiği nokta ile y eksenini kestiği nokta arasındaki uzaklık kaç birimdir?",
  "7√5/2", ["7√5", "7/2", "√53", "49/4"],
  "Eğim (1 − (−5))/(4 − 1) = 2 ve f(x) = 2x − 7. Grafik x eksenini (7/2, 0), y eksenini (0, −7) noktasında keser. Uzaklık √((7/2)² + 7²) = √(245/4) = 7√5/2.",
  verify=(sp.sqrt(sp.Rational(7, 2)**2 + 7**2), 7*sp.sqrt(5)/2))

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

q("Bir fabrikanın günlük üretim maliyeti, üretilen ürün sayısı x olmak üzere M(x) = x² − 40x + 700 bin ₺ olarak modellenmiştir. Maliyetin en düşük olduğu üretim düzeyinde günlük maliyet kaç bin ₺'dir?",
  "300", ["20", "100", "400", "700"],
  "Parabolün tepe noktası x = 40/2 = 20'dir. M(20) = 400 − 800 + 700 = 300 bin ₺.",
  verify=((x**2 - 40*x + 700).subs(x, 20), 300))

q("f(2x − 1) = 6x + 5 olduğuna göre f fonksiyonunun grafiğinin x eksenini kestiği noktanın apsisi kaçtır?",
  "−8/3", ["−5/6", "8/3", "−5/2", "−3"],
  "2x − 1 = t ise x = (t + 1)/2 ve f(t) = 3(t + 1) + 5 = 3t + 8. f(x) = 0 için x = −8/3.",
  verify=(sp.solve(6*((t + 1)/2) + 5, t)[0], sp.Rational(-8, 3)))

q("Bir f fonksiyonunun birebir olması ile ilgili aşağıdakilerden hangisi doğrudur?",
  "Farklı her iki elemanın görüntüsü de farklıdır",
  ["Görüntü kümesi ile değer kümesi her durumda eşit olmak zorundadır",
   "Tanım kümesindeki her elemanın görüntüsü aynı değere eşit olmalıdır",
   "Tanım kümesi ile değer kümesinin eleman sayıları eşit olmak zorundadır",
   "Fonksiyonun grafiği her zaman orijinden geçmek durumundadır"],
  "Birebirlik tanımı: x₁ ≠ x₂ iken f(x₁) ≠ f(x₂) olmasıdır. Görüntü kümesinin değer kümesine "
  "eşit olması örtenliktir; her elemanın aynı görüntüye gitmesi ise sabit fonksiyondur.")

# ══ B. Bileşke fonksiyon (7) ═════════════════════════════════════════════════
q("f(x) = 2x + 1 ve g(x) = x² − 3 fonksiyonları veriliyor. Buna göre (g∘f)(2) ile (f∘g)(2) değerleri arasındaki fark kaçtır?",
  "19", ["0", "3", "22", "25"],
  "(f∘g)(2) = f(1) = 3 ve (g∘f)(2) = g(5) = 22. Fark 22 − 3 = 19.",
  verify=(((2*x + 1)**2 - 3).subs(x, 2) - (2*(x**2 - 3) + 1).subs(x, 2), 19))

q("f(x) = 3x − 2 ve g(x) = x + 4 olmak üzere (g∘f)(a) = (f∘g)(a) − 2a eşitliğini sağlayan a değeri kaçtır?",
  "4", ["−4", "2", "5", "8"],
  "(g∘f)(a) = 3a + 2 ve (f∘g)(a) = 3(a + 4) − 2 = 3a + 10. 3a + 2 = 3a + 10 − 2a ise 2a = 8 ve a = 4.",
  verify=(sp.solve((3*x - 2 + 4) - (3*(x + 4) - 2 - 2*x), x)[0], 4))

q("f(x) = x² + 1 ve g(x) = 2x olduğuna göre (f∘g)(x) ifadesindeki katsayılar toplamı kaçtır?",
  "5", ["3", "9", "4", "7"],
  "(f∘g)(x) = f(2x) = (2x)² + 1 = 4x² + 1 elde edilir. Katsayılar toplamı, ifadede x yerine 1 "
  "yazılarak bulunur: 4 + 1 = 5.",
  verify=(( (2*x)**2 + 1 ).subs(x, 1), 5))

q("f ve g fonksiyonları için g(x) = 2x + 1 ve (f∘g)(x) = 6x + 7 veriliyor. Buna göre f fonksiyonunun grafiğinin y eksenini kestiği noktanın ordinatı kaçtır?",
  "4", ["1", "3", "7", "10"],
  "g(x) = t ise x = (t − 1)/2 ve f(t) = 6(t − 1)/2 + 7 = 3t + 4. Grafik y eksenini f(0) = 4 noktasında keser.",
  verify=((6*((t - 1)/2) + 7).subs(t, 0), 4))

q("h(x) = x² − 1 ve g(x) = 3x + 2 olmak üzere (h∘g)(x) = 0 denklemini sağlayan x değerlerinin toplamı kaçtır?",
  "−4/3", ["−1", "−1/3", "0", "4/3"],
  "(h∘g)(x) = (3x + 2)² − 1 = 0 ise 3x + 2 = 1 veya 3x + 2 = −1; x = −1/3 veya x = −1. Toplam −4/3.",
  verify=(sum(sp.solve((3*x + 2)**2 - 1, x)), sp.Rational(-4, 3)))

q("f(x) = 1/(x − 2) ve g(x) = x + 3 olmak üzere (f∘g)(x) fonksiyonunun tanımsız olduğu x değeri kaçtır?",
  "−1", ["−3", "1", "2", "5"],
  "(f∘g)(x) = 1/(x + 3 − 2) = 1/(x + 1); payda x = −1 için sıfır olur.",
  verify=(sp.solve(x + 3 - 2, x)[0], -1))

q("f(x) = 2x ve g(x) = x − 5 fonksiyonları veriliyor. (f∘g∘f)(a) = 2 eşitliğini sağlayan a değeri için (g∘f∘g)(a) kaçtır?",
  "−9", ["−6", "3", "6", "0"],
  "(f∘g∘f)(a) = f(g(2a)) = 2(2a − 5) = 4a − 10 = 2 ise a = 3. (g∘f∘g)(3) = g(f(−2)) = g(−4) = −9.",
  verify=((2*(3 - 5)) - 5, -9))

# ══ C. Ters fonksiyon (5) ════════════════════════════════════════════════════
q("f(x) = 3x − 9 ve g(x) = f⁻¹(x) + 2 olduğuna göre g(6) + f(g(6)) toplamı kaçtır?",
  "19", ["12", "7", "17", "21"],
  "f⁻¹(x) = (x + 9)/3 olduğundan f⁻¹(6) = 5 ve g(6) = 7. f(7) = 12. Toplam 7 + 12 = 19.",
  verify=((6 + 9)/sp.Integer(3) + 2 + 3*((6 + 9)/sp.Integer(3) + 2) - 9, 19))

q("f(x) = (2x + 1)/(x − 3) fonksiyonu için f⁻¹(a) = 4 olduğuna göre a + f⁻¹(3) toplamı kaçtır?",
  "19", ["9", "10", "13", "22"],
  "f⁻¹(a) = 4 ise a = f(4) = 9/1 = 9. f⁻¹(3) = b ise (2b + 1)/(b − 3) = 3, 2b + 1 = 3b − 9 ve b = 10. Toplam 19.",
  verify=(((2*x + 1)/(x - 3)).subs(x, 4) + sp.solve((2*x + 1) - 3*(x - 3), x)[0], 19))

q("f(x) = x³ + 2 olmak üzere f⁻¹(a) = 3 ve f(b) = 10 olduğuna göre a + b toplamı kaçtır?",
  "31", ["27", "29", "32", "35"],
  "f⁻¹(a) = 3 ise a = f(3) = 29. f(b) = 10 ise b³ = 8 ve b = 2. Toplam 31.",
  verify=((x**3 + 2).subs(x, 3) + sp.real_root(8, 3), 31))

q("Bir kırtasiye fotokopi için 7 ₺ sabit ücret ve sayfa başına 2 ₺ almaktadır. Ödenen ücreti sayfa sayısına bağlayan fonksiyon f olduğuna göre f⁻¹(x) aşağıdakilerden hangisidir?",
  "(x − 7) / 2", ["(x + 7) / 2", "2x − 7", "(x − 2) / 7", "x / 2 − 7"],
  "Sayfa sayısı x ise ücret f(x) = 2x + 7'dir. y = 2x + 7 eşitliğinden x = (y − 7)/2 bulunur; f⁻¹(x) = (x − 7)/2. Bu fonksiyon ödenen ücretten sayfa sayısını verir.",
  verify=(sp.solve(2*y + 7 - x, y)[0], (x - 7)/2))

q("f(x) = 5x − 4 ve g(x) = x + 2 olduğuna göre (f∘g)⁻¹ fonksiyonunun grafiğinin x eksenini kestiği noktanın apsisi kaçtır?",
  "6", ["−6/5", "1", "3", "21"],
  "(f∘g)(x) = 5(x + 2) − 4 = 5x + 6, tersi (x − 6)/5'tir. Bu ifade x = 6 için sıfır olur.",
  verify=(sp.solve((x - 6)/5, x)[0], 6))

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
q("2ˣ⁺³ = 32 ve 3ʸ⁻¹ = 1/9 olduğuna göre x − y farkı kaçtır?",
  "3", ["1", "−1", "2", "5"],
  "2ˣ⁺³ = 2⁵ ise x = 2. 3ʸ⁻¹ = 3⁻² ise y = −1. x − y = 3.",
  verify=(sp.solve(2**(x + 3) - 32, x)[0] - sp.solve(3**(y - 1) - sp.Rational(1, 9), y)[0], 3))

q("3²ˣ⁻¹ = 27 olduğuna göre log₂(x² + 4) ifadesinin değeri kaçtır?",
  "3", ["2", "4", "5/2", "8"],
  "2x − 1 = 3 ise x = 2. log₂(4 + 4) = log₂8 = 3.",
  verify=(sp.log(sp.solve(3**(2*x - 1) - 27, x)[0]**2 + 4, 2), 3))

q("a = 2³⁰, b = 3²⁰ ve c = 5¹⁰ sayıları için aşağıdaki sıralamalardan hangisi doğrudur?",
  "c < a < b", ["a < b < c", "b < a < c", "c < b < a", "a < c < b"],
  "Üsler 10'da eşitlenir: a = 8¹⁰, b = 9¹⁰, c = 5¹⁰. 5 < 8 < 9 olduğundan c < a < b.",
  verify=(sp.Integer(5)**10 < sp.Integer(2)**30 < sp.Integer(3)**20, True))

q("Bir şehrin nüfusu her 10 yılda 3 katına çıkmaktadır. Nüfusun 9 katına çıkması için geçen süre, 27 katına çıkması için geçen sürenin kaçta kaçıdır?",
  "2/3", ["1/3", "1/2", "3/4", "3/2"],
  "Süreler log₃9 = 2 ve log₃27 = 3 dönemdir (20 ve 30 yıl). Oran 2/3.",
  verify=(sp.log(9, 3) / sp.log(27, 3), sp.Rational(2, 3)))

q("5ˣ = 3 olduğuna göre 25ˣ⁺¹ − 5ˣ⁺² ifadesinin değeri kaçtır?",
  "150", ["75", "200", "225", "25"],
  "25ˣ⁺¹ = 25 · (5ˣ)² = 25 · 9 = 225 ve 5ˣ⁺² = 25 · 3 = 75. Fark 150.",
  verify=(25 * 3**2 - 25 * 3, 150))

q("Bir ilacın kandaki miktarı her saatin sonunda bir önceki saatteki miktarın yarısına inmektedir. Başlangıçta 400 mg olan ilacın miktarı kaçıncı saatin sonunda ilk kez 30 mg'ın altına düşer?",
  "4", ["3", "5", "6", "8"],
  "Miktar n saat sonra 400 · (1/2)ⁿ olur: 200, 100, 50, 25. 30 mg'ın altına ilk kez 4. saatin sonunda düşer.",
  verify=(next(m for m in range(20) if sp.Integer(400) / 2**m < 30), 4))

q("4ˣ⁺¹ = 8ˣ⁻¹ eşitliğini sağlayan x değeri için logₓ125 ifadesinin değeri kaçtır?",
  "3", ["5", "2", "25", "1/3"],
  "2²ˣ⁺² = 2³ˣ⁻³ olduğundan 2x + 2 = 3x − 3 ve x = 5. log₅125 = 3.",
  verify=(sp.log(125, sp.solve(4**(x + 1) - 8**(x - 1), x)[0]), 3))

# ══ F. Logaritma ve doğal logaritma (11) ═════════════════════════════════════
q("log₂(3x − 2) = 4 ve log₃(y + 1) = 2 olduğuna göre x + y toplamı kaçtır?",
  "14", ["10", "12", "15", "16"],
  "3x − 2 = 16 ise x = 6. y + 1 = 9 ise y = 8. Toplam 14.",
  verify=(sp.solve(3*x - 2 - 16, x)[0] + sp.solve(y + 1 - 9, y)[0], 14))

q("Bir bakteri türünün sayısı her 20 dakikada 5 katına çıkmaktadır. 4 bakteriyle başlayan bir kültürde bakteri sayısı kaç dakika sonra 500 olur?",
  "60", ["40", "75", "100", "120"],
  "4 · 5ᵗ = 500 ise 5ᵗ = 125 ve t = log₅125 = 3 dönem. Her dönem 20 dakika olduğundan süre 60 dakikadır.",
  verify=(20 * sp.log(125, 5), 60))

q("log2 = a ve log3 = b olduğuna göre log12 ifadesinin a ve b türünden eşiti nedir?",
  "2a + b", ["a + 2b", "a + b", "2ab", "a·b²"],
  "12 çarpanlarına ayrılır: 12 = 2² · 3. Çarpımın logaritması toplanır, üs öne çıkar: "
  "log12 = 2log2 + log3 = 2a + b.")

q("log₃81 = a ve log₂b = a olduğuna göre log_b 4 ifadesinin değeri kaçtır?",
  "1/2", ["2", "1/4", "4", "1"],
  "a = 4 olduğundan b = 2⁴ = 16. log₁₆4 = 1/2.",
  verify=(sp.log(4, 2**sp.log(81, 3)), sp.Rational(1, 2)))

q("f(x) = ln x fonksiyonu için f(e³) + f(1/e²) − f(√e) ifadesinin değeri kaçtır?",
  "1/2", ["3/2", "1", "−1/2", "5/2"],
  "f(e³) = 3, f(1/e²) = −2 ve f(√e) = 1/2. Sonuç 3 − 2 − 1/2 = 1/2.",
  verify=(sp.log(sp.E**3) + sp.log(1 / sp.E**2) - sp.log(sp.sqrt(sp.E)), sp.Rational(1, 2)))

q("log₄x = −2 ve log_y 8 = 3/2 olduğuna göre x·y çarpımı kaçtır?",
  "1/4", ["1/16", "1/2", "1/8", "4"],
  "x = 4⁻² = 1/16. y^(3/2) = 8 = 2³ olduğundan y = 2² = 4. x·y = 4/16 = 1/4.",
  verify=(sp.Rational(1, 16) * sp.Integer(8)**sp.Rational(2, 3), sp.Rational(1, 4)))

q("f(x) = log₂x ve g(x) = log₃x olmak üzere f(8) + g(1/9) − f(g(9)) ifadesinin değeri kaçtır?",
  "0", ["1", "−1", "2", "3"],
  "f(8) = 3, g(1/9) = −2, g(9) = 2 ve f(2) = 1. Sonuç 3 − 2 − 1 = 0.",
  verify=(sp.log(8, 2) + sp.log(sp.Rational(1, 9), 3) - sp.log(sp.log(9, 3), 2), 0))

q("log₆2 = a olduğuna göre log₆54 ifadesinin a türünden eşiti aşağıdakilerden hangisidir?",
  "3 − 2a", ["3 + a", "2 − a", "3a − 1", "3 − a"],
  "log₆3 = log₆(6/2) = 1 − a. 54 = 2 · 3³ olduğundan log₆54 = a + 3(1 − a) = 3 − 2a.",
  verify=(sp.simplify(sp.log(54, 6) - (3 - 2*sp.log(2, 6))), 0))

q("Ses şiddeti düzeyi L = 10·log(I/I₀) desibel formülüyle hesaplanmaktadır. Şiddeti I₀ değerinin 10⁶ katı olan bir sesin şiddeti 100 katına çıkarılırsa yeni ses düzeyi kaç desibel olur?",
  "80", ["62", "70", "160", "600"],
  "Yeni şiddet I₀ · 10⁶ · 10² = I₀ · 10⁸'dir. L = 10 · log 10⁸ = 10 · 8 = 80 desibel.",
  verify=(10 * sp.log(10**8, 10), 80))

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
q("Doğrusal bir f fonksiyonunun grafiği (1, 5) ve (3, 11) noktalarından geçmektedir. Buna göre f(f(0)) değeri kaçtır?",
  "8", ["2", "5", "11", "14"],
  "Eğim (11 − 5)/(3 − 1) = 3 ve f(x) = 3x + 2. f(0) = 2, f(2) = 8.",
  verify=((3*x + 2).subs(x, (3*x + 2).subs(x, 0)), 8))

q("(4x² − 12xy + 9y²) / (2x² − xy − 3y²) ifadesinin sadeleştirilmiş biçimi hangisidir?",
  "(2x − 3y) / (x + y)", ["(2x + 3y) / (x + y)", "(2x − 3y) / (x − y)", "(x + y) / (2x − 3y)",
                          "(2x − 3y) / (x + 3y)"],
  "Pay tam karedir: 4x² − 12xy + 9y² = (2x − 3y)². Payda çarpanlarına ayrılır: "
  "2x² − xy − 3y² = (2x − 3y)(x + y). Ortak çarpan sadeleşir ve (2x − 3y)/(x + y) kalır.",
  verify=(sp.simplify((4*x**2 - 12*x*y + 9*y**2)/(2*x**2 - x*y - 3*y**2) - (2*x - 3*y)/(x + y)), 0))

q("Bir taksi açılış ücreti olarak 40 ₺, her kilometre için 12 ₺ almaktadır. Ödenen ücretin gidilen kilometreye bağlı fonksiyonu f olmak üzere f⁻¹(280) değeri kaçtır?",
  "20", ["18", "23", "24", "25"],
  "f(x) = 12x + 40 olduğundan f⁻¹(x) = (x − 40)/12. f⁻¹(280) = 240/12 = 20; yani 280 ₺ ödeyen yolcu 20 km gitmiştir.",
  verify=(sp.solve(12*x + 40 - 280, x)[0], 20))

q("A(−1, 2) ve B(5, 6) noktaları veriliyor. [AB] doğru parçasının orta dikmesinin y eksenini kestiği noktanın ordinatı kaçtır?",
  "7", ["4", "1", "10", "13/2"],
  "Orta nokta (2, 4), AB'nin eğimi 4/6 = 2/3, orta dikmenin eğimi −3/2'dir. y − 4 = −3/2 (x − 2) doğrusunda x = 0 için y = 7.",
  verify=(4 + sp.Rational(-3, 2) * (0 - 2), 7))

q("Bir işletmenin x adet ürün için toplam maliyeti M(x) = 2x² + 40x + 600 ₺, ürünün birim satış fiyatı 140 ₺'dir. Kârın en büyük olması için kaç adet ürün üretilip satılmalıdır?",
  "25", ["20", "30", "35", "50"],
  "Kâr K(x) = 140x − (2x² + 40x + 600) = −2x² + 100x − 600'dür. Parabolün tepe noktası x = −100/(2 · (−2)) = 25.",
  verify=(sp.solve(sp.diff(140*x - (2*x**2 + 40*x + 600), x), x)[0], 25))

# ══ H. Analitik geometri (12) ════════════════════════════════════════════════
q("Analitik düzlemde A(2, −1) ve B(6, 2) noktaları veriliyor. [AB] doğru parçasını çap kabul eden çemberin alanı kaç birim karedir?",
  "25π/4", ["5π/2", "5π", "25π/2", "25π"],
  "|AB| = √(4² + 3²) = 5, yarıçap 5/2'dir. Alan π(5/2)² = 25π/4.",
  verify=(sp.pi*(sp.sqrt(4**2 + 3**2)/2)**2, 25*sp.pi/4))

q("Analitik düzlemde A(−3, 4) ve B(5, −2) noktalarını birleştiren doğru parçasının orta "
  "noktasının koordinatları hangisidir?",
  "(1, 1)", ["(2, 2)", "(1, 3)", "(4, −3)", "(−1, 1)"],
  "Orta nokta koordinatları uç noktaların ortalamasıdır: x = (−3 + 5)/2 = 1 ve "
  "y = (4 + (−2))/2 = 1. Orta nokta (1, 1) olur.",
  verify=(sp.Rational(-3 + 5, 2) + sp.Rational(4 - 2, 2), 2))

q("3x − 4y + 12 = 0 doğrusunun koordinat eksenleriyle oluşturduğu üçgenin alanı kaç birim karedir?",
  "6", ["5", "7", "12", "24"],
  "y = 0 için x = −4, x = 0 için y = 3. Eksenlerle oluşan dik üçgenin dik kenarları 4 ve 3 birimdir; alan 4 · 3 / 2 = 6.",
  verify=(sp.Abs(sp.solve(3*x + 12, x)[0]) * sp.Abs(sp.solve(-4*y + 12, y)[0]) / 2, 6))

q("Analitik düzlemde (0, 3) ve (−2, 0) noktalarından geçen doğrunun denklemi hangisidir?",
  "3x − 2y + 6 = 0", ["3x + 2y − 6 = 0", "2x − 3y + 6 = 0", "3x − 2y − 6 = 0", "2x + 3y − 6 = 0"],
  "Eğim hesaplanır: m = (3 − 0) / (0 − (−2)) = 3/2. y kesişimi 3 olduğundan y = (3/2)x + 3 "
  "yazılır. İki taraf 2 ile çarpılıp düzenlenirse 3x − 2y + 6 = 0 elde edilir.",
  verify=(sp.Rational(3 - 0, 0 - (-2)), sp.Rational(3, 2)))

q("Analitik düzlemde A(1, 2) ve B(5, 5) noktalarından geçen doğrunun C(4, −2) noktasına uzaklığı kaç birimdir?",
  "5", ["3", "4", "7/5", "25"],
  "AB'nin eğimi 3/4'tür; doğru 3x − 4y + 5 = 0 olur. C noktasının uzaklığı |3·4 − 4·(−2) + 5| / √(9 + 16) = 25/5 = 5.",
  verify=(sp.Abs(3*4 - 4*(-2) + 5)/sp.sqrt(3**2 + 4**2), 5))

q("y = 2x − 5 doğrusuna paralel olan ve (1, 4) noktasından geçen doğrunun y eksenini kestiği "
  "noktanın ordinatı kaçtır?",
  "2", ["−5", "4", "6", "−2"],
  "Paralel doğruların eğimleri eşittir: m = 2. Doğru y = 2x + n biçimindedir; (1, 4) yerine "
  "konur: 4 = 2 + n → n = 2. y eksenini (0, 2) noktasında keser.",
  verify=(4 - 2*1, 2))

q("A(1, 2) noktasından geçen ve 2x − 6y + 5 = 0 doğrusuna dik olan doğrunun y eksenini kestiği noktanın ordinatı kaçtır?",
  "5", ["−1", "2", "3", "7"],
  "Verilen doğrunun eğimi 2/6 = 1/3, dik doğrunun eğimi −3'tür. y − 2 = −3(x − 1) ise y = −3x + 5; y eksenini 5'te keser.",
  verify=(2 + (-3) * (0 - 1), 5))

q("x² + y² − 6x + 8y = 0 çemberinin merkezinin 3x + 4y + 2 = 0 doğrusuna uzaklığı kaç birimdir?",
  "1", ["2", "3", "5", "7/5"],
  "Çember (x − 3)² + (y + 4)² = 25 biçiminde yazılır; merkez (3, −4). Uzaklık |3·3 + 4·(−4) + 2| / √(9 + 16) = 5/5 = 1.",
  verify=(sp.Abs(3*3 + 4*(-4) + 2) / sp.sqrt(3**2 + 4**2), 1))

q("y = x² − 6x + 5 parabolünün tepe noktası ile parabolün x eksenini kestiği noktaların oluşturduğu üçgenin alanı kaç birim karedir?",
  "8", ["4", "10", "12", "16"],
  "x² − 6x + 5 = 0 ise x = 1 veya x = 5; taban 4 birimdir. Tepe noktası (3, −4) olduğundan yükseklik 4'tür. Alan 4 · 4 / 2 = 8.",
  verify=((5 - 1) * sp.Abs((x**2 - 6*x + 5).subs(x, 3)) / 2, 8))

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

q("Analitik düzlemde 2x + 3y = 12 doğrusu ile x − y = 1 doğrusunun kesişim noktasının orijine uzaklığı kaç birimdir?",
  "√13", ["3", "√5", "5", "13"],
  "x = y + 1 ilk denklemde yerine yazılırsa 2y + 2 + 3y = 12, y = 2 ve x = 3. Kesişim (3, 2) noktasıdır; orijine uzaklığı √(9 + 4) = √13.",
  verify=(sp.sqrt(sum(v**2 for v in sp.solve([2*x + 3*y - 12, x - y - 1], [x, y]).values())), sp.sqrt(13)))


if __name__ == "__main__":
    raise SystemExit(main(
        Q, prefix=PREFIX, ders=DERS, konu=KONU, style=STYLE, seed=SEED,
        relative_path=RELATIVE_PATH, label=LABEL,
    ))
