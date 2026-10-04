#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SGS Matematik — Sayılar ve Temel İşlemler (gerçek sınav derinliğinde yeniden yazım).

Kalibrasyon (2021-2026, 16 kitapçık, matematik 8-15. sorular): sınavda tek adımlı
işlem ('12 + 3 × 4') ya da bölünebilme kuralı ezberi sorulmaz. Sorulan: iç içe
kesirli işlem, rasyonel ifadenin sadeleştirilmesi, özdeşlikle değer bulma, üslü
denklem, basamak/rakam koşulu, işlem tanımı, karmaşık sayı. Eski paket (ortaokul
düzeyi) baştan değiştirildi; soru kimlikleri korundu.

Her sonuç sympy ile builder'dan bağımsız doğrulanır (mat_common.make_q, §8).
Gösterim: Unicode üs/kök, çarpma ·, eksi − (U+2212); Markdown * ve _ yok.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mat_common import main, make_q

Q: list[dict] = []
q = make_q(Q)
R = sp.Rational
x, a, b = sp.symbols("x a b")
I_ = sp.I

# ══ Kesirli ve ondalıklı işlemler (10) ══════════════════════════════════════
q("(1/2 + 1/3) : (1 − 1/6) işleminin sonucu kaçtır?",
  "1", ["5/6", "6/5", "2", "1/2"],
  "Pay: 1/2 + 1/3 = 5/6. Payda: 1 − 1/6 = 5/6. Bölme: (5/6) : (5/6) = 1.",
  verify=((R(1, 2) + R(1, 3)) / (1 - R(1, 6)), 1))
q("(3/4 − 1/2) · (2 + 2/3) − 1/3 işleminin sonucu kaçtır?",
  "1/3", ["2/3", "1", "1/6", "0"],
  "3/4 − 1/2 = 1/4 ve 2 + 2/3 = 8/3. Çarpım 1/4 · 8/3 = 2/3. Sonuç 2/3 − 1/3 = 1/3.",
  verify=((R(3, 4) - R(1, 2)) * (2 + R(2, 3)) - R(1, 3), R(1, 3)))
q("1 + 1/(1 + 1/(1 + 1)) işleminin sonucu kaçtır?",
  "5/3", ["3/2", "2", "4/3", "5/2"],
  "İçten dışa: 1 + 1 = 2; 1 + 1/2 = 3/2; 1/(3/2) = 2/3; 1 + 2/3 = 5/3.",
  verify=(1 + 1 / (1 + R(1, 2)), R(5, 3)))
q("(1 1/2 + 2 1/4) : 1 1/4 işleminin sonucu kaçtır?",
  "3", ["5/4", "4", "15/4", "9/4"],
  "Bileşik kesirler: 3/2 + 9/4 = 15/4. Bölen 1 1/4 = 5/4. (15/4) : (5/4) = 3.",
  verify=((R(3, 2) + R(9, 4)) / R(5, 4), 3))
q("(0,2 + 0,05) : 0,5 işleminin sonucu kaçtır?",
  "0,5", ["0,05", "5", "0,25", "2"],
  "0,2 + 0,05 = 0,25. 0,25 : 0,5 = 25/50 = 0,5.",
  verify=((R(2, 10) + R(5, 100)) / R(1, 2), R(1, 2)))
q("(1/3 − 1/4 + 1/2) : (1/6 + 1/12) işleminin sonucu kaçtır?",
  "7/3", ["7/12", "3/7", "7/4", "1/4"],
  "Payda 12'de: 4/12 − 3/12 + 6/12 = 7/12. Bölen: 2/12 + 1/12 = 3/12. (7/12) : (3/12) = 7/3.",
  verify=((R(1, 3) - R(1, 4) + R(1, 2)) / (R(1, 6) + R(1, 12)), R(7, 3)))
q("3/(1 − 2/5) − 5/(1 + 1/4) işleminin sonucu kaçtır?",
  "1", ["2", "9", "1/2", "0"],
  "1 − 2/5 = 3/5, 3 : (3/5) = 5. 1 + 1/4 = 5/4, 5 : (5/4) = 4. Sonuç 5 − 4 = 1.",
  verify=(3 / (1 - R(2, 5)) - 5 / (1 + R(1, 4)), 1))
q("(2/3)⁻² + (1/2)⁻¹ − 1/4 işleminin sonucu kaçtır?",
  "4", ["9/4", "3", "17/4", "5"],
  "(2/3)⁻² = 9/4, (1/2)⁻¹ = 2. 9/4 + 2 − 1/4 = 8/4 + 2 = 4.",
  verify=(R(2, 3)**-2 + R(1, 2)**-1 - R(1, 4), 4))
q("√0,16 + 10·√0,0009 işleminin sonucu kaçtır?",
  "0,7", ["0,43", "0,07", "1", "0,49"],
  "√0,16 = 0,4 ve √0,0009 = 0,03. 10 · 0,03 = 0,3. Toplam 0,7.",
  verify=(sp.sqrt(R(16, 100)) + 10 * sp.sqrt(R(9, 10000)), R(7, 10)))
q("(10⁻¹ + 10⁻²) · 100 işleminin sonucu kaçtır?",
  "11", ["0,11", "1,1", "110", "10"],
  "10⁻¹ = 0,1 ve 10⁻² = 0,01; toplam 0,11. 0,11 · 100 = 11.",
  verify=((R(1, 10) + R(1, 100)) * 100, 11))

# ══ Rasyonel ifadeler (8) ═══════════════════════════════════════════════════
def ayni(ifade, beklenen):
    return (sp.simplify(ifade - beklenen), 0)
q("(x² − 9)/(x² + x − 6) ifadesinin en sade hâli aşağıdakilerden hangisidir?",
  "(x − 3)/(x − 2)", ["(x + 3)/(x − 2)", "(x − 3)/(x + 2)", "x + 3", "(x + 3)/(x + 2)"],
  "Pay (x − 3)(x + 3), payda (x + 3)(x − 2) biçiminde çarpanlarına ayrılır. Ortak çarpan (x + 3) sadeleşir: (x − 3)/(x − 2).",
  verify=ayni((x**2 - 9) / (x**2 + x - 6), (x - 3) / (x - 2)))
q("(x² − 4x + 4)/(x² − 4) · (x + 2)/x ifadesinin en sade hâli aşağıdakilerden hangisidir?",
  "(x − 2)/x", ["(x + 2)/x", "x − 2", "1/x", "(x − 2)/(x + 2)"],
  "x² − 4x + 4 = (x − 2)², x² − 4 = (x − 2)(x + 2). İlk kesir (x − 2)/(x + 2) olur; (x + 2)/x ile çarpılınca (x − 2)/x kalır.",
  verify=ayni((x**2 - 4*x + 4) / (x**2 - 4) * (x + 2) / x, (x - 2) / x))
q("(a² − b²)/(a + b) + (a² + 2ab + b²)/(a + b) ifadesinin eşiti aşağıdakilerden hangisidir?",
  "2a", ["2b", "a + b", "a − b", "2a + 2b"],
  "İlk kesir (a − b)(a + b)/(a + b) = a − b; ikinci kesir (a + b)²/(a + b) = a + b. Toplam 2a'dır.",
  verify=ayni((a**2 - b**2) / (a + b) + (a**2 + 2*a*b + b**2) / (a + b), 2*a))
q("(x³ − 8)/(x − 2) ifadesinin x = 3 için değeri kaçtır?",
  "19", ["13", "17", "25", "7"],
  "x³ − 8 = (x − 2)(x² + 2x + 4) olduğundan ifade x² + 2x + 4'e eşittir. x = 3 için 9 + 6 + 4 = 19.",
  verify=(sp.cancel((x**3 - 8) / (x - 2)).subs(x, 3), 19))
q("(1 − 1/x) · x²/(x − 1) ifadesinin en sade hâli aşağıdakilerden hangisidir?",
  "x", ["x − 1", "1/x", "x + 1", "x²"],
  "1 − 1/x = (x − 1)/x. (x − 1)/x · x²/(x − 1) çarpımında (x − 1) ve bir x sadeleşir; geriye x kalır.",
  verify=ayni((1 - 1/x) * x**2 / (x - 1), x))
q("(x² + 5x + 6)/(x² + 2x − 3) : (x + 2)/(x − 1) ifadesinin en sade hâli aşağıdakilerden hangisidir?",
  "1", ["x + 2", "(x + 2)/(x − 1)", "x − 1", "(x + 3)/(x − 1)"],
  "İlk kesir (x + 2)(x + 3)/((x + 3)(x − 1)) = (x + 2)/(x − 1). Aynı kesire bölündüğü için sonuç 1'dir.",
  verify=ayni((x**2 + 5*x + 6) / (x**2 + 2*x - 3) / ((x + 2) / (x - 1)), 1))
q("a = 2,5 ve b = 1,5 olmak üzere (a² − b²)/(a − b) + a·b ifadesinin değeri kaçtır?",
  "7,75", ["4", "6,25", "3,75", "8,5"],
  "(a² − b²)/(a − b) = a + b = 4. a·b = 2,5 · 1,5 = 3,75. Toplam 7,75.",
  verify=((lambda A, B: (A**2 - B**2) / (A - B) + A * B)(R(5, 2), R(3, 2)), R(31, 4)))
q("(x − 1/x)/(1 − 1/x) ifadesinin en sade hâli aşağıdakilerden hangisidir?",
  "x + 1", ["x − 1", "x", "1/x", "(x + 1)/x"],
  "Pay (x² − 1)/x, payda (x − 1)/x. Bölüm (x² − 1)/(x − 1) = x + 1.",
  verify=ayni((x - 1/x) / (1 - 1/x), x + 1))

# ══ Özdeşlikler (8) ═════════════════════════════════════════════════════════
q("x + 1/x = 4 olduğuna göre x² + 1/x² kaçtır?",
  "14", ["16", "18", "12", "8"],
  "(x + 1/x)² = x² + 2 + 1/x² = 16. Buradan x² + 1/x² = 14.",
  verify=(4**2 - 2, 14))
q("x − 1/x = 3 olduğuna göre x² + 1/x² kaçtır?",
  "11", ["9", "7", "3", "13"],
  "(x − 1/x)² = x² − 2 + 1/x² = 9. Buradan x² + 1/x² = 11.",
  verify=(3**2 + 2, 11))
q("a − b = 5 ve a·b = 6 olduğuna göre a² + b² kaçtır?",
  "37", ["13", "31", "25", "19"],
  "(a − b)² = a² + b² − 2ab = 25. a² + b² = 25 + 12 = 37.",
  verify=(5**2 + 2*6, 37))
q("a + b = 7 ve a² + b² = 29 olduğuna göre a·b kaçtır?",
  "10", ["20", "22", "11", "9"],
  "(a + b)² = a² + b² + 2ab → 49 = 29 + 2ab → ab = 10.",
  verify=(R(7**2 - 29, 2), 10))
q("a² − b² = 45 ve a − b = 5 olduğuna göre a kaçtır?",
  "7", ["9", "2", "14", "5"],
  "a² − b² = (a − b)(a + b) → a + b = 9. a − b = 5 ile toplanırsa 2a = 14, a = 7.",
  verify=(sp.solve([a**2 - b**2 - 45, a - b - 5], [a, b])[0][0], 7))
q("x + 1/x = 3 olduğuna göre x³ + 1/x³ kaçtır?",
  "18", ["27", "24", "9", "21"],
  "x³ + 1/x³ = (x + 1/x)³ − 3(x + 1/x) = 27 − 9 = 18.",
  verify=(3**3 - 3*3, 18))
q("x ve y pozitif gerçel sayılar, x² + y² = 20 ve x·y = 8 olduğuna göre x + y kaçtır?",
  "6", ["4", "2√7", "36", "√20"],
  "(x + y)² = x² + y² + 2xy = 20 + 16 = 36. x + y pozitif olduğundan 6'dır.",
  verify=(sp.sqrt(20 + 2*8), 6))
q("101² − 99² işleminin sonucu kaçtır?",
  "400", ["4", "200", "404", "40"],
  "İki kare farkı: (101 − 99)(101 + 99) = 2 · 200 = 400.",
  verify=(101**2 - 99**2, 400))

# ══ Üslü ve köklü ifadeler (8) ══════════════════════════════════════════════
q("2ˣ⁺¹ + 2ˣ = 96 olduğuna göre x kaçtır?",
  "5", ["4", "6", "32", "3"],
  "2ˣ⁺¹ = 2·2ˣ olduğundan 3·2ˣ = 96, 2ˣ = 32 = 2⁵. x = 5.",
  verify=(sp.solve(2**(x + 1) + 2**x - 96, x)[0], 5))
q("3ˣ⁺² − 3ˣ = 72 olduğuna göre x kaçtır?",
  "2", ["3", "1", "9", "4"],
  "3ˣ⁺² = 9·3ˣ olduğundan 8·3ˣ = 72, 3ˣ = 9. x = 2.",
  verify=(sp.solve(3**(x + 2) - 3**x - 72, x)[0], 2))
q("√12 + √27 − √48 işleminin sonucu kaçtır?",
  "√3", ["0", "2√3", "−√3", "5√3"],
  "√12 = 2√3, √27 = 3√3, √48 = 4√3. 2√3 + 3√3 − 4√3 = √3.",
  verify=(sp.sqrt(12) + sp.sqrt(27) - sp.sqrt(48), sp.sqrt(3)))
q("(√5 − √2)(√5 + √2) + (√3 − 1)² işleminin sonucu aşağıdakilerden hangisidir?",
  "7 − 2√3", ["7", "5 − 2√3", "3", "7 + 2√3"],
  "İlk çarpım iki kare farkıdır: 5 − 2 = 3. (√3 − 1)² = 3 − 2√3 + 1 = 4 − 2√3. Toplam 7 − 2√3.",
  verify=((sp.sqrt(5) - sp.sqrt(2)) * (sp.sqrt(5) + sp.sqrt(2)) + (sp.sqrt(3) - 1)**2, 7 - 2*sp.sqrt(3)))
q("16^(3/4) · 27^(−1/3) işleminin sonucu kaçtır?",
  "8/3", ["24", "8", "4/9", "2"],
  "16^(3/4) = (2⁴)^(3/4) = 2³ = 8. 27^(−1/3) = 1/3. Çarpım 8/3.",
  verify=(sp.Integer(16)**R(3, 4) * sp.Integer(27)**R(-1, 3), R(8, 3)))
q("1/(√3 − √2) − √2 işleminin sonucu aşağıdakilerden hangisidir?",
  "√3", ["√2", "√3 − 2√2", "2√2 + √3", "1"],
  "Payda eşleniğiyle genişletilir: 1/(√3 − √2) = (√3 + √2)/(3 − 2) = √3 + √2. √2 çıkarılınca √3 kalır.",
  verify=(1 / (sp.sqrt(3) - sp.sqrt(2)) - sp.sqrt(2), sp.sqrt(3)))
q("(0,25)^(−3/2) işleminin sonucu kaçtır?",
  "8", ["1/8", "4", "16", "2"],
  "0,25 = 1/4. (1/4)^(−3/2) = 4^(3/2) = (√4)³ = 8.",
  verify=(R(1, 4)**R(-3, 2), 8))
q("4ˣ = 8 olduğuna göre 2ˣ⁻¹ kaçtır?",
  "√2", ["2", "1", "2√2", "1/2"],
  "4ˣ = 2²ˣ = 2³ → x = 3/2. 2ˣ⁻¹ = 2^(1/2) = √2.",
  verify=(2**(sp.solve(4**x - 8, x)[0] - 1), sp.sqrt(2)))

# ══ Basamak, bölünebilme, EBOB-EKOK (10) ════════════════════════════════════
q("AB ve BA iki basamaklı doğal sayılardır. AB + BA = 132 ve A − B = 4 olduğuna göre AB sayısı kaçtır?",
  "84", ["48", "66", "75", "93"],
  "AB + BA = 11(A + B) = 132 → A + B = 12. A − B = 4 ile birlikte A = 8, B = 4; AB = 84.",
  verify=(next(10*A + B for A in range(1, 10) for B in range(1, 10) if 11*(A + B) == 132 and A - B == 4), 84))
q("Rakamları farklı üç basamaklı en büyük çift sayı ile rakamları farklı üç basamaklı en küçük tek sayının farkı kaçtır?",
  "883", ["885", "896", "884", "873"],
  "Rakamları farklı en büyük üç basamaklı çift sayı 986, en küçük tek sayı 103'tür. Fark 883.",
  verify=(max(n for n in range(100, 1000) if n % 2 == 0 and len(set(str(n))) == 3)
          - min(n for n in range(100, 1000) if n % 2 == 1 and len(set(str(n))) == 3), 883))
q("İki basamaklı AB sayısı, rakamları toplamının 7 katına eşittir. Buna göre A·B çarpımının alabileceği en büyük değer kaçtır?",
  "32", ["18", "8", "24", "36"],
  "10A + B = 7(A + B) → 3A = 6B → A = 2B. Olası sayılar 21, 42, 63, 84; en büyük çarpım 8 · 4 = 32.",
  verify=(max(A*B for A in range(1, 10) for B in range(10) if 10*A + B == 7*(A + B)), 32))
q("Üç basamaklı 4A7 sayısı 9 ile tam bölünebildiğine göre A rakamı kaçtır?",
  "7", ["16", "9", "2", "0"],
  "Rakamlar toplamı 4 + A + 7 = 11 + A, 9'un katı olmalıdır. A bir rakam olduğundan 11 + A = 18, A = 7.",
  verify=(sum(A for A in range(10) if (400 + 10*A + 7) % 9 == 0), 7))
q("Dört basamaklı 3A4B sayısı 5 ve 9 ile tam bölünebildiğine göre A'nın alabileceği değerlerin toplamı kaçtır?",
  "8", ["6", "2", "11", "13"],
  "5 ile bölünebilme için B = 0 ya da 5. B = 0 ise 7 + A, 9'un katı → A = 2. B = 5 ise 12 + A → A = 6. Toplam 8.",
  verify=(sum({A for A in range(10) for B in (0, 5) if (3000 + 100*A + 40 + B) % 45 == 0}), 8))
q("EBOB(84, 120) + EKOK(12, 18) işleminin sonucu kaçtır?",
  "48", ["42", "60", "24", "72"],
  "EBOB(84, 120) = 12, EKOK(12, 18) = 36. Toplam 48.",
  verify=(sp.gcd(84, 120) + sp.lcm(12, 18), 48))
q("Kenar uzunlukları 84 m ve 60 m olan dikdörtgen biçimli bir arazinin çevresine, her köşeye birer tane gelecek ve aralıkları eşit olacak biçimde ağaç dikilecektir. Buna göre en az kaç ağaç gerekir?",
  "24", ["12", "48", "25", "22"],
  "Aralık 84 ile 60'ın ortak böleni olmalı; en az ağaç için en büyüğü alınır: EBOB = 12 m. Kapalı çevrede ağaç sayısı çevre/aralık = 288/12 = 24.",
  verify=(2*(84 + 60) / sp.gcd(84, 60), 24))
q("Bir duraktan A hattının otobüsleri 12 dakikada, B hattının otobüsleri 18 dakikada bir kalkmaktadır. İki hattın otobüsleri saat 08.00'de birlikte kalktığına göre 12.00'ye kadar (12.00 dâhil) kaç kez daha birlikte kalkarlar?",
  "6", ["7", "5", "8", "4"],
  "Birlikte kalkışlar EKOK(12, 18) = 36 dakikada bir tekrarlanır. 4 saatte 240 dakika vardır; 240 içinde 36'nın katları 36, 72, ..., 216 olmak üzere 6 tanedir.",
  verify=(240 // sp.lcm(12, 18), 6))
q("Bir sepetteki yumurtalar 6'şar sayıldığında 4, 8'er sayıldığında 6, 9'ar sayıldığında 7 yumurta artmaktadır. Sepette en az kaç yumurta vardır?",
  "70", ["72", "74", "142", "68"],
  "Her durumda 2 yumurta eksiktir: n + 2 sayısı 6, 8 ve 9'un ortak katıdır. En küçük ortak kat 72 → n = 70.",
  verify=(min(n for n in range(1, 500) if n % 6 == 4 and n % 8 == 6 and n % 9 == 7), 70))
q("a ve b pozitif tam sayılar, a < b, EBOB(a, b) = 6 ve EKOK(a, b) = 72 olduğuna göre a + b toplamının alabileceği en küçük değer kaçtır?",
  "42", ["78", "36", "48", "54"],
  "a = 6m, b = 6n ve m ile n aralarında asal, m·n = 72/6 = 12. Olası (m, n): (1, 12) → 6 + 72 = 78; (3, 4) → 18 + 24 = 42. En küçük toplam 42.",
  verify=(min(A + B for A in range(1, 73) for B in range(A + 1, 73) if sp.gcd(A, B) == 6 and sp.lcm(A, B) == 72), 42))

# ══ Mutlak değer ve bölme (6) ═══════════════════════════════════════════════
q("|x − 3| = 5 denklemini sağlayan x değerlerinin toplamı kaçtır?",
  "6", ["8", "−2", "10", "16"],
  "x − 3 = 5 → x = 8; x − 3 = −5 → x = −2. Toplam 6.",
  verify=(sum(sp.solve(sp.Abs(sp.Symbol('t', real=True) - 3) - 5)), 6))
q("x < 0 < y olmak üzere |x − y| + |x| − |y| ifadesinin eşiti aşağıdakilerden hangisidir?",
  "−2x", ["2y", "0", "2x − 2y", "−2y"],
  "x − y negatif olduğundan |x − y| = y − x; |x| = −x; |y| = y. Toplam y − x − x − y = −2x.",
  verify=(((lambda X, Y: abs(X - Y) + abs(X) - abs(Y))(-3, 5)), 6))
q("|2x − 1| < 7 eşitsizliğini sağlayan kaç tam sayı vardır?",
  "6", ["7", "5", "8", "4"],
  "−7 < 2x − 1 < 7 → −6 < 2x < 8 → −3 < x < 4. Tam sayılar −2, −1, 0, 1, 2, 3: altı tane.",
  verify=(len([t for t in range(-20, 20) if abs(2*t - 1) < 7]), 6))
q("|x + 2| + |x − 4| ifadesinin alabileceği en küçük değer kaçtır?",
  "6", ["2", "4", "0", "8"],
  "İki mutlak değerin toplamı, x sayı doğrusunda −2 ile 4 arasındayken en küçüktür ve bu aralığın uzunluğuna eşittir: 4 − (−2) = 6.",
  verify=(min(abs(R(t, 10) + 2) + abs(R(t, 10) - 4) for t in range(-100, 100)), 6))
q("n bir doğal sayıdır. n'nin 6 ile bölümünden kalan 4 olduğuna göre 2n + 5 sayısının 6 ile bölümünden kalan kaçtır?",
  "1", ["3", "5", "2", "4"],
  "n = 6k + 4 → 2n + 5 = 12k + 13 = 6(2k + 2) + 1. Kalan 1.",
  verify=((2*4 + 5) % 6, 1))
q("x pozitif tam sayı olmak üzere 72/x ifadesi tam sayı olacak biçimde x'in alabileceği kaç farklı değer vardır?",
  "12", ["10", "11", "8", "6"],
  "x, 72'nin pozitif bölenlerinden biri olmalıdır. 72 = 2³ · 3² → bölen sayısı (3 + 1)(2 + 1) = 12.",
  verify=(len(sp.divisors(72)), 12))

# ══ İşlem tanımı (6) ════════════════════════════════════════════════════════
q("Gerçel sayılar kümesinde a ∗ b = a + b − 2ab işlemi tanımlanıyor. Buna göre 3 ∗ (1 ∗ 2) kaçtır?",
  "8", ["−1", "4", "−8", "2"],
  "1 ∗ 2 = 1 + 2 − 4 = −1. 3 ∗ (−1) = 3 − 1 + 6 = 8.",
  verify=((lambda f: f(3, f(1, 2)))(lambda p, r: p + r - 2*p*r), 8))
q("a △ b = a² − 3b işlemi tanımlanıyor. Buna göre (2 △ 1) △ 3 kaçtır?",
  "−8", ["8", "−2", "1", "−5"],
  "2 △ 1 = 4 − 3 = 1. 1 △ 3 = 1 − 9 = −8.",
  verify=((lambda f: f(f(2, 1), 3))(lambda p, r: p**2 - 3*r), -8))
q("a ⊕ b = (a + b)/(a − b) işlemi tanımlanıyor. x ⊕ 2 = 3 olduğuna göre x kaçtır?",
  "4", ["2", "6", "8", "3"],
  "(x + 2)/(x − 2) = 3 → x + 2 = 3x − 6 → 2x = 8 → x = 4.",
  verify=(sp.solve((x + 2) / (x - 2) - 3, x)[0], 4))
q("Gerçel sayılar kümesinde a ∗ b = a + b + ab işlemi tanımlanıyor. Bu işleme göre 2'nin tersi kaçtır?",
  "−2/3", ["2/3", "−1/2", "−2", "1/3"],
  "Etkisiz eleman e: a + e + ae = a → e(1 + a) = 0 → e = 0. 2'nin tersi t: 2 + t + 2t = 0 → t = −2/3.",
  verify=(sp.solve(2 + x + 2*x, x)[0], R(-2, 3)))
q("x ⊗ y = x·y − x − y + 2 işlemi tanımlanıyor. Buna göre 3 ⊗ (2 ⊗ 4) kaçtır?",
  "7", ["4", "9", "5", "6"],
  "2 ⊗ 4 = 8 − 2 − 4 + 2 = 4. 3 ⊗ 4 = 12 − 3 − 4 + 2 = 7.",
  verify=((lambda f: f(3, f(2, 4)))(lambda p, r: p*r - p - r + 2), 7))
q("Pozitif tam sayılar kümesinde a ∗ b = EKOK(a, b) − EBOB(a, b) işlemi tanımlanıyor. Buna göre (6 ∗ 8) ∗ 10 kaçtır?",
  "108", ["22", "110", "106", "88"],
  "6 ∗ 8 = 24 − 2 = 22. 22 ∗ 10 = EKOK(22, 10) − EBOB(22, 10) = 110 − 2 = 108.",
  verify=((lambda f: f(f(6, 8), 10))(lambda p, r: sp.lcm(p, r) - sp.gcd(p, r)), 108))

# ══ Karmaşık sayılar (4) ════════════════════════════════════════════════════
q("z₁ = 3 − 2i ve z₂ = 1 + 4i olduğuna göre z₁·z₂ karmaşık sayısının gerçel kısmı kaçtır?",
  "11", ["−5", "10", "3", "14"],
  "(3 − 2i)(1 + 4i) = 3 + 12i − 2i − 8i². i² = −1 olduğundan 3 + 8 + 10i = 11 + 10i. Gerçel kısım 11.",
  verify=(sp.re(sp.expand((3 - 2*I_) * (1 + 4*I_))), 11))
q("z = (2 + i)/(1 − i) karmaşık sayısının sanal kısmı kaçtır?",
  "3/2", ["1/2", "3", "−3/2", "1"],
  "Pay ve payda (1 + i) ile çarpılır: (2 + i)(1 + i)/2 = (2 + 3i + i²)/2 = (1 + 3i)/2. Sanal kısım 3/2.",
  verify=(sp.im(sp.simplify((2 + I_) / (1 - I_))), R(3, 2)))
q("i⁴¹ + i⁴² + i⁴³ toplamı aşağıdakilerden hangisidir? (i² = −1)",
  "−1", ["1", "i", "−i", "0"],
  "i'nin kuvvetleri 4'te bir tekrar eder: i⁴¹ = i, i⁴² = −1, i⁴³ = −i. Toplam −1.",
  verify=(I_**41 + I_**42 + I_**43, -1))
q("|3 − 4i| + |5 + 12i| toplamı kaçtır?",
  "18", ["16", "8", "26", "12"],
  "|3 − 4i| = √(9 + 16) = 5, |5 + 12i| = √(25 + 144) = 13. Toplam 18.",
  verify=(sp.Abs(3 - 4*I_) + sp.Abs(5 + 12*I_), 18))

assert len(Q) == 60, len(Q)

if __name__ == "__main__":
    raise SystemExit(main(
        Q, prefix="mat-sayilar-gen", ders="matematik", konu="sayilar_temel_islemler",
        style="SGS Matematik (gerçek sınav 8-15 derinliği)", seed=20261004,
        relative_path="content/matematik/sayilar_temel_islemler.json", label="Sayılar ve Temel İşlemler",
    ))
