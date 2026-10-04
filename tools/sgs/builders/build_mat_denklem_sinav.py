#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SGS Matematik — Denklem, Eşitsizlik ve Problemler (gerçek sınav derinliğinde).

Kalibrasyon (2021-2026, 16 kitapçık): sınavda '2x + 5 = 17' türü tek adımlı
denklem sorulmaz. Sorulan: köklerle ilgili koşul (farklı iki gerçel kök için
parametre), sabit polinom katsayıları, tam sayı koşullu sistemler, denklem
kurma (masalara oturma). Eski paket baştan değiştirildi; soru kimlikleri korundu.
Her sonuç builder'dan bağımsız olarak sympy ile doğrulanır.
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
x, y, z, a, b, m = sp.symbols("x y z a b m")
oo = sp.oo
def kok(denklem, sym=x):
    s = sp.solve(denklem, sym)
    assert len(s) == 1, s
    return s[0]
def aralik(esitsizlik):
    return sp.solve_univariate_inequality(esitsizlik, x, relational=False)

# ══ Birinci derece (6) ══════════════════════════════════════════════════════
q("(a − 2)x + 3 = 2x + a denkleminin çözüm kümesi boş küme olduğuna göre a kaçtır?",
  "4", ["2", "3", "0", "−4"],
  "Denklem (a − 4)x = a − 3 biçimine gelir. Çözüm kümesinin boş olması için x'in katsayısı 0, sağ taraf 0'dan farklı olmalıdır: a = 4 (a − 3 = 1 ≠ 0).",
  verify=(kok(a - 4, a), 4))
q("Bir konserde öğrenci bileti 150 ₺, tam bilet 250 ₺'dir. Konsere 200 kişi katılmış ve bilet geliri 41.000 ₺ olmuştur. Buna göre kaç öğrenci bileti satılmıştır?",
  "90", ["80", "100", "110", "120"],
  "Öğrenci bileti sayısı s ise 150s + 250(200 − s) = 41.000; 50.000 − 100s = 41.000 ve s = 90.",
  verify=(sp.solve(150*x + 250*(200 - x) - 41000, x)[0], 90))
q("Bir babanın yaşı iki çocuğunun yaşları toplamının 3 katıdır. Çocukların yaş farkı 4'tür ve 6 yıl sonra babanın yaşı çocukların yaşları toplamının 2 katı olacaktır. Büyük çocuk bugün kaç yaşındadır?",
  "11", ["7", "9", "13", "14"],
  "Çocukların yaşları toplamı S ise 3S + 6 = 2(S + 12), S = 18. Büyük çocuk (18 + 4)/2 = 11 yaşındadır.",
  verify=((sp.solve(3*x + 6 - 2*(x + 12), x)[0] + 4) / 2, 11))
q("ax + 4 = 2x + b denkleminin çözüm kümesi gerçel sayılar kümesi olduğuna göre a + b kaçtır?",
  "6", ["2", "4", "8", "−2"],
  "Her x için sağlanması için iki taraf özdeş olmalıdır: a = 2 ve b = 4. a + b = 6.",
  verify=(2 + 4, 6))
q("Bir miras üç kardeş arasında paylaştırılmıştır. Büyük kardeş mirasın 1/2'sini, ortanca kardeş 1/3'ünü, küçük kardeş ise kalan 60.000 ₺'yi almıştır. Mirasın tamamı kaç ₺'dir?",
  "360.000", ["180.000", "240.000", "300.000", "420.000"],
  "Küçük kardeşe kalan pay 1 − 1/2 − 1/3 = 1/6'dır. Miras 60.000 : (1/6) = 360.000 ₺.",
  verify=(60000 / (1 - R(1, 2) - R(1, 3)), 360000))
q("Bir işi Ali tek başına 12 günde, Ayşe tek başına 18 günde bitirebilmektedir. İkisi birlikte 4 gün çalıştıktan sonra Ali işi bırakmıştır. Kalan işi Ayşe kaç günde bitirir?",
  "8", ["4", "6", "9", "10"],
  "Birlikte günlük iş 1/12 + 1/18 = 5/36'dır; 4 günde 20/36 = 5/9 biter. Kalan 4/9'luk işi Ayşe 4/9 · 18 = 8 günde bitirir.",
  verify=((1 - 4*(R(1, 12) + R(1, 18))) * 18, 8))

# ══ İkinci derece (10) ══════════════════════════════════════════════════════
q("x² − 7x + 10 = 0 denkleminin kökleri x₁ ve x₂ olduğuna göre x₁² + x₂² kaçtır?",
  "29", ["49", "39", "20", "25"],
  "x₁ + x₂ = 7, x₁·x₂ = 10. x₁² + x₂² = (x₁ + x₂)² − 2x₁x₂ = 49 − 20 = 29.",
  verify=(sum(r**2 for r in sp.solve(x**2 - 7*x + 10, x)), 29))
q("x² + 2x + a = 0 denkleminin farklı iki gerçel kökü olduğuna göre a'nın alabileceği en büyük tam sayı değeri kaçtır?",
  "0", ["1", "−1", "2", "4"],
  "Farklı iki gerçel kök için Δ = 4 − 4a > 0 olmalıdır → a < 1. En büyük tam sayı 0'dır.",
  verify=(max(t for t in range(-10, 10) if 4 - 4*t > 0), 0))
q("x² − (m + 1)x + 12 = 0 denkleminin köklerinden biri 3 olduğuna göre m kaçtır?",
  "6", ["7", "4", "5", "3"],
  "x = 3 yazılır: 9 − 3(m + 1) + 12 = 0 → 18 − 3m = 0 → m = 6.",
  verify=(kok(9 - 3*(m + 1) + 12, m), 6))
q("x² − 6x + k = 0 denkleminin birbirine eşit iki gerçel kökü olduğuna göre k kaçtır?",
  "9", ["6", "36", "3", "−9"],
  "Eşit (çakışık) kök için Δ = 36 − 4k = 0 → k = 9.",
  verify=(kok(36 - 4*a, a), 9))
q("Kökleri −2 ve 5 olan ikinci dereceden denklem aşağıdakilerden hangisidir?",
  "x² − 3x − 10 = 0", ["x² + 3x − 10 = 0", "x² − 3x + 10 = 0", "x² + 7x + 10 = 0", "x² − 7x − 10 = 0"],
  "Kökler toplamı 3, çarpımı −10'dur. Denklem x² − (toplam)x + (çarpım) = 0 → x² − 3x − 10 = 0.",
  verify=(sp.expand((x + 2)*(x - 5)) - (x**2 - 3*x - 10), 0))
q("x² − 5x + 3 = 0 denkleminin kökleri x₁ ve x₂ olduğuna göre 1/x₁ + 1/x₂ kaçtır?",
  "5/3", ["3/5", "5", "−5/3", "1/3"],
  "1/x₁ + 1/x₂ = (x₁ + x₂)/(x₁·x₂) = 5/3.",
  verify=(sum(1/r for r in sp.solve(x**2 - 5*x + 3, x)), R(5, 3)))
q("2x² − 8x + m = 0 denkleminin kökleri arasında x₁ = 3x₂ bağıntısı olduğuna göre m kaçtır?",
  "6", ["3", "8", "12", "4"],
  "Kökler toplamı 4: 3x₂ + x₂ = 4 → x₂ = 1, x₁ = 3. Kökler çarpımı m/2 = 3 → m = 6.",
  verify=(2 * 3 * 1, 6))
q("Bir dikdörtgenin kısa kenarı uzun kenarından 5 cm kısadır. Dikdörtgenin alanı 84 cm² olduğuna göre çevresi kaç cm'dir?",
  "38", ["34", "40", "42", "46"],
  "Kısa kenar x ise x(x + 5) = 84, x² + 5x − 84 = 0 ve (x − 7)(x + 12) = 0. x = 7, uzun kenar 12; çevre 2(7 + 12) = 38 cm.",
  verify=(2 * (max(sp.solve(x*(x + 5) - 84, x)) * 2 + 5), 38))
q("x⁴ − 13x² + 36 = 0 denkleminin gerçel kökleri sayı doğrusunda işaretlendiğinde en büyük kök ile en küçük kök arasındaki uzaklık kaç birimdir?",
  "6", ["1", "4", "5", "13"],
  "x² = t dönüşümüyle t² − 13t + 36 = 0, t = 4 veya t = 9. Kökler −3, −2, 2, 3; uzaklık 3 − (−3) = 6.",
  verify=(max(sp.solve(x**4 - 13*x**2 + 36, x)) - min(sp.solve(x**4 - 13*x**2 + 36, x)), 6))
q("x² + bx + c = 0 denkleminin kökleri 1 − √2 ve 1 + √2 olduğuna göre b + c kaçtır?",
  "−3", ["1", "−1", "3", "−2"],
  "Kökler toplamı 2 = −b → b = −2. Kökler çarpımı 1 − 2 = −1 = c. b + c = −3.",
  verify=(-((1 - sp.sqrt(2)) + (1 + sp.sqrt(2))) + (1 - sp.sqrt(2))*(1 + sp.sqrt(2)), -3))

# ══ Polinomlar (10) ═════════════════════════════════════════════════════════
q("P(x) = x³ − 2x² + ax + 4 polinomu x − 2 ile tam bölünebildiğine göre a kaçtır?",
  "−2", ["2", "−4", "4", "0"],
  "Tam bölünebilme için P(2) = 0: 8 − 8 + 2a + 4 = 0 → a = −2.",
  verify=(kok(8 - 8 + 2*a + 4, a), -2))
q("P(x) = 2x³ + x² − 5x + 7 polinomunun x + 1 ile bölümünden kalan kaçtır?",
  "11", ["5", "3", "7", "−1"],
  "Kalan P(−1) = −2 + 1 + 5 + 7 = 11.",
  verify=(sp.rem(2*x**3 + x**2 - 5*x + 7, x + 1, x), 11))
q("P(x) = (2x − 1)³ + (x + 2)² polinomunun katsayılar toplamı a, sabit terimi b olduğuna göre a − b farkı kaçtır?",
  "7", ["3", "6", "10", "13"],
  "Katsayılar toplamı P(1) = 1 + 9 = 10, sabit terim P(0) = −1 + 4 = 3. Fark 7.",
  verify=(((2*x - 1)**3 + (x + 2)**2).subs(x, 1) - ((2*x - 1)**3 + (x + 2)**2).subs(x, 0), 7))
q("P(x) = (a − 2)x² + (b + 3)x + 5 bir sabit polinom olduğuna göre a + b kaçtır?",
  "−1", ["5", "1", "−5", "2"],
  "Sabit polinomda x'li terimlerin katsayıları 0'dır: a = 2, b = −3. a + b = −1.",
  verify=(2 + (-3), -1))
q("P(x + 1) = x² + 3x + 4 olduğuna göre P(x) polinomunun x − 3 ile bölümünden kalan kaçtır?",
  "14", ["4", "8", "18", "22"],
  "Kalan P(3)'tür. x + 1 = 3 için x = 2: P(3) = 4 + 6 + 4 = 14.",
  verify=((x**2 + 3*x + 4).subs(x, 2), 14))
q("P(x) polinomunun x − 3 ile bölümünden kalan 5'tir. Buna göre P(2x + 1) polinomunun x − 1 ile bölümünden kalan kaçtır?",
  "5", ["3", "11", "1", "7"],
  "Kalan, x = 1 yazılarak bulunur: P(2·1 + 1) = P(3) = 5.",
  verify=(2*1 + 1, 3))
q("x³ − 8 ifadesinin çarpanlarından biri aşağıdakilerden hangisidir?",
  "x² + 2x + 4", ["x² − 2x + 4", "x + 2", "x² + 4", "x² − 4x + 4"],
  "İki küp farkı: x³ − 8 = (x − 2)(x² + 2x + 4).",
  verify=(sp.rem(x**3 - 8, x**2 + 2*x + 4, x), 0))
q("P(x) = x³ + ax² + bx − 6 polinomunun iki kökü 1 ve 2'dir. Buna göre polinomun üçüncü kökü kaçtır?",
  "3", ["−3", "6", "−6", "2"],
  "Üçüncü dereceden polinomda kökler çarpımı −(−6)/1 = 6'dır. 1 · 2 · r = 6 → r = 3.",
  verify=(R(6, 1 * 2), 3))
q("P(x) = x² + mx + 9 polinomu bir tam kare olduğuna göre m'nin pozitif değeri kaçtır?",
  "6", ["3", "9", "18", "12"],
  "x² + mx + 9 = (x + 3)² = x² + 6x + 9 için m = 6.",
  verify=(sp.expand((x + 3)**2).coeff(x, 1), 6))
q("x² − 3x + 2 ve x² − 4 polinomlarının ortak çarpanı aşağıdakilerden hangisidir?",
  "x − 2", ["x + 2", "x − 1", "x + 1", "x − 4"],
  "x² − 3x + 2 = (x − 1)(x − 2) ve x² − 4 = (x − 2)(x + 2). Ortak çarpan x − 2'dir.",
  verify=(sp.gcd(x**2 - 3*x + 2, x**2 - 4) - (x - 2), 0))

# ══ Denklem sistemleri (6) ══════════════════════════════════════════════════
q("Bir kafede 2 çay ile 3 simidin toplam fiyatı 130 ₺, 3 çay ile 1 simidin toplam fiyatı 90 ₺'dir. Buna göre 1 çay ile 1 simidin toplam fiyatı kaç ₺'dir?",
  "50", ["40", "45", "55", "60"],
  "2ç + 3s = 130 ve 3ç + s = 90. İkinciden s = 90 − 3ç; yerine yazılırsa 7ç = 140, ç = 20 ve s = 30. Toplam 50 ₺.",
  verify=(sum(sp.solve([2*x + 3*y - 130, 3*x + y - 90], [x, y]).values()), 50))
q("a, b ve c pozitif gerçel sayılardır. a·b = 12, b·c = 20 ve a·c = 15 olduğuna göre a + b + c kaçtır?",
  "12", ["47", "10", "15", "60"],
  "Üç eşitlik çarpılır: (abc)² = 3.600 → abc = 60. a = 60/20 = 3, b = 60/15 = 4, c = 60/12 = 5. Toplam 12.",
  verify=(R(60, 20) + R(60, 15) + R(60, 12), 12))
q("Ali, Berk ve Can'ın yaşları toplamı 36'dır. Ali ile Berk'in yaşları toplamı 22, Berk ile Can'ın yaşları toplamı 26 olduğuna göre Ali kaç yaşındadır?",
  "10", ["8", "11", "12", "14"],
  "Can'ın yaşı 36 − 22 = 14, Berk'in yaşı 26 − 14 = 12, Ali'nin yaşı 22 − 12 = 10.",
  verify=(sp.solve([x + y + z - 36, x + y - 22, y + z - 26], [x, y, z])[x], 10))
q("Aralarında 360 km bulunan iki şehirden iki araç aynı anda birbirine doğru hareket etmiştir. Araçlardan birinin hızı diğerinden 20 km/sa fazladır. Araçlar 3 saat sonra karşılaştığına göre hızlı aracın hızı kaç km/sa'tir?",
  "70", ["50", "60", "65", "80"],
  "Yavaş aracın hızı v ise 3(v + v + 20) = 360, 2v + 20 = 120 ve v = 50. Hızlı aracın hızı 70 km/sa.",
  verify=(sp.solve(3*(2*x + 20) - 360, x)[0] + 20, 70))
q("3ˣ · 9ʸ = 81 ve 2ˣ : 4ʸ = 1/2 olduğuna göre x · y çarpımı kaçtır?",
  "15/8", ["3/2", "5/4", "2", "15/4"],
  "3ˣ⁺²ʸ = 3⁴ ise x + 2y = 4; 2ˣ⁻²ʸ = 2⁻¹ ise x − 2y = −1. Toplanırsa 2x = 3, x = 3/2 ve y = 5/4. Çarpım 15/8.",
  verify=(sp.Rational(3, 2) * sp.Rational(5, 4), R(15, 8)))
q("Bir otoparkta bulunan otomobil ve motosikletlerin toplam sayısı 40, tekerlek sayısı 130'dur. Otoparkta kaç otomobil vardır?",
  "25", ["15", "20", "30", "35"],
  "Otomobil o, motosiklet 40 − o: 4o + 2(40 − o) = 130 → 2o = 50 → o = 25.",
  verify=(kok(4*x + 2*(40 - x) - 130), 25))

# ══ Eşitsizlikler (10) ══════════════════════════════════════════════════════
q("3 − 2x ≥ 7 eşitsizliğinin çözüm kümesi aşağıdakilerden hangisidir?",
  "(−∞, −2]", ["[−2, ∞)", "(−∞, −2)", "(−∞, 2]", "[2, ∞)"],
  "−2x ≥ 4 → x ≤ −2 (negatif sayıyla bölünce yön değişir). Çözüm kümesi (−∞, −2].",
  verify=(aralik(3 - 2*x >= 7) == sp.Interval(-oo, -2), True))
q("Bir otopark ilk saat için 60 ₺, sonraki her saat için 25 ₺ ücret almaktadır. Ödenen ücretin 160 ₺'den fazla ve 260 ₺'den az olması için araç otoparkta kaç farklı tam saat süre kalmış olabilir?",
  "3", ["2", "4", "5", "6"],
  "n saatlik ücret 60 + 25(n − 1) = 25n + 35'tir. 160 < 25n + 35 < 260 ise 5 < n < 9; n = 6, 7, 8 olmak üzere 3 farklı süre vardır.",
  verify=(len([n_ for n_ in range(1, 30) if 160 < 25*n_ + 35 < 260]), 3))
q("Yerden atılan bir topun t saniye sonraki yüksekliği h(t) = −5t² + 20t + 25 metredir. Topun yüksekliğinin 40 metreden fazla olduğu zaman aralığı kaç saniye sürer?",
  "2", ["1", "3", "4", "5/2"],
  "−5t² + 20t + 25 > 40 ise t² − 4t + 3 < 0, yani (t − 1)(t − 3) < 0 ve 1 < t < 3. Süre 2 saniyedir.",
  verify=(max(sp.solve(-5*x**2 + 20*x + 25 - 40, x)) - min(sp.solve(-5*x**2 + 20*x + 25 - 40, x)), 2))
q("(x − 1)/(x + 3) ≤ 0 eşitsizliğinin çözüm kümesi aşağıdakilerden hangisidir?",
  "(−3, 1]", ["[−3, 1]", "(−3, 1)", "(−∞, −3) ∪ [1, ∞)", "[−3, 1)"],
  "Pay ile payda zıt işaretli ya da pay sıfır olmalıdır: −3 < x ≤ 1. Payda sıfır olamayacağından −3 dâhil değildir.",
  verify=(aralik((x - 1)/(x + 3) <= 0) == sp.Interval.Lopen(-3, 1), True))
q("x² − 4x + m > 0 eşitsizliği her x gerçel sayısı için sağlandığına göre m'nin alabileceği en küçük tam sayı değeri kaçtır?",
  "5", ["4", "3", "16", "2"],
  "Başkatsayı pozitif ve ifade her zaman pozitif olacaksa Δ < 0 olmalıdır: 16 − 4m < 0 → m > 4. En küçük tam sayı 5.",
  verify=(min(t for t in range(-20, 20) if 16 - 4*t < 0), 5))
q("|x − 2| ≤ 5 ve x > 0 koşullarını birlikte sağlayan kaç tam sayı vardır?",
  "7", ["11", "8", "6", "10"],
  "|x − 2| ≤ 5 → −3 ≤ x ≤ 7. x > 0 ile birlikte 1, 2, ..., 7: yedi tam sayı.",
  verify=(len([t for t in range(-20, 20) if abs(t - 2) <= 5 and t > 0]), 7))
q("a < b < 0 olduğuna göre aşağıdakilerden hangisi kesinlikle doğrudur?",
  "a² > b²", ["a·b < 0", "1/a < 1/b", "a + b > 0", "b − a < 0"],
  "İki negatif sayıdan küçük olanın mutlak değeri büyüktür; bu yüzden a² > b². a·b pozitiftir, 1/a > 1/b, a + b negatif, b − a pozitiftir.",
  verify=(((-3)**2 > (-1)**2) and ((-5)**2 > (-2)**2), True))
q("2 ≤ x ≤ 5 ve −3 ≤ y ≤ 1 olduğuna göre x·y çarpımının alabileceği en küçük değer kaçtır?",
  "−15", ["−6", "−5", "5", "−2"],
  "Uç değerlerin çarpımları: 2·(−3) = −6, 2·1 = 2, 5·(−3) = −15, 5·1 = 5. En küçük değer −15.",
  verify=(min(p*r for p in (2, 5) for r in (-3, 1)), -15))
q("x² ≤ 9 ve x² ≥ 4 eşitsizliklerini birlikte sağlayan tam sayıların toplamı kaçtır?",
  "0", ["5", "10", "−5", "4"],
  "Koşulu sağlayan tam sayılar −3, −2, 2, 3'tür. Toplamları 0.",
  verify=(sum(t for t in range(-10, 10) if 4 <= t**2 <= 9), 0))
q("(x − 3)(x + 1)² ≤ 0 eşitsizliğini sağlayan en büyük tam sayı kaçtır?",
  "3", ["−1", "2", "4", "1"],
  "(x + 1)² negatif olamaz; ifade x ≤ 3 için sıfır ya da negatiftir. En büyük tam sayı 3.",
  verify=(max(t for t in range(-20, 20) if (t - 3)*(t + 1)**2 <= 0), 3))

# ══ Köklü ve rasyonel denklemler (4) ════════════════════════════════════════
q("√(x + 7) = x + 1 denkleminin çözüm kümesi aşağıdakilerden hangisidir?",
  "{2}", ["{−3, 2}", "{−3}", "{3}", "∅"],
  "Kare alınır: x + 7 = x² + 2x + 1 → x² + x − 6 = 0 → x = 2 ya da x = −3. x = −3 için sağ taraf −2 olur ve kök negatif olamaz; çözüm kümesi {2}.",
  verify=(kok(sp.sqrt(x + 7) - (x + 1)), 2))
q("3/(x − 1) − 2/(x + 1) = 1 denkleminin kökleri x₁ ve x₂ olduğuna göre x₁² + x₂² toplamı kaçtır?",
  "13", ["1", "5", "9", "25"],
  "Paydalar eşitlenirse 3(x + 1) − 2(x − 1) = x² − 1, yani x² − x − 6 = 0. Kökler 3 ve −2'dir; ikisi de paydayı sıfır yapmaz. 9 + 4 = 13.",
  verify=(sum(r**2 for r in sp.solve(3/(x - 1) - 2/(x + 1) - 1, x)), 13))
q("√(2x − 1) + 3 = x denkleminin kökü aşağıdakilerden hangisidir?",
  "4 + √6", ["4 − √6", "5", "2 + √6", "3"],
  "√(2x − 1) = x − 3 → 2x − 1 = x² − 6x + 9 → x² − 8x + 10 = 0 → x = 4 ± √6. Kökün sağ tarafı x − 3 ≥ 0 olmalıdır; 4 − √6 < 3 olduğundan yalnız 4 + √6 sağlar.",
  verify=(sp.solve(sp.sqrt(2*x - 1) + 3 - x, x)[0], 4 + sp.sqrt(6)))
q("İki basamaklı bir sayının rakamları toplamı 11'dir. Rakamların yerleri değiştirildiğinde elde edilen sayı ilk sayıdan 27 fazladır. Buna göre ilk sayı kaçtır?",
  "47", ["29", "38", "56", "74"],
  "Sayı 10a + b ise a + b = 11 ve (10b + a) − (10a + b) = 9(b − a) = 27, yani b − a = 3. a = 4, b = 7; sayı 47.",
  verify=(10*sp.solve([x + y - 11, y - x - 3], [x, y])[x] + sp.solve([x + y - 11, y - x - 3], [x, y])[y], 47))

# ══ Denklem kurma (14) ══════════════════════════════════════════════════════
q("Bir davette misafirler masalara 5'er kişi oturduğunda 8 kişi ayakta kalıyor; 7'şer kişi oturduğunda ise 2 masa boş kalıyor. Davette kaç misafir vardır?",
  "63", ["55", "70", "49", "77"],
  "Masa sayısı m: 5m + 8 = 7(m − 2) → 2m = 22 → m = 11. Misafir sayısı 5 · 11 + 8 = 63.",
  verify=(5 * kok(5*x + 8 - 7*(x - 2)) + 8, 63))
q("Ardışık üç çift sayının toplamı 78 olduğuna göre bu sayıların en büyüğü kaçtır?",
  "28", ["26", "24", "30", "32"],
  "Sayılar n − 2, n, n + 2: 3n = 78 → n = 26. En büyüğü 28.",
  verify=(R(78, 3) + 2, 28))
q("Bir kitapçı tanesi 40 ₺ olan romanlardan ve tanesi 25 ₺ olan dergilerden toplam 30 adet satarak 1.020 ₺ gelir elde etmiştir. Kaç roman satılmıştır?",
  "18", ["12", "20", "15", "24"],
  "40r + 25(30 − r) = 1.020 → 15r + 750 = 1.020 → r = 18.",
  verify=(kok(40*x + 25*(30 - x) - 1020), 18))
q("Bir sınıftaki öğrenciler sıralara 2'şer oturursa 6 öğrenci ayakta kalıyor, 3'er oturursa 4 sıra boş kalıyor. Sınıfta kaç öğrenci vardır?",
  "42", ["36", "48", "40", "54"],
  "Sıra sayısı s: 2s + 6 = 3(s − 4) → s = 18. Öğrenci sayısı 2 · 18 + 6 = 42.",
  verify=(2 * kok(2*x + 6 - 3*(x - 4)) + 6, 42))
q("İki doğal sayının toplamı 50'dir. Büyük sayı küçük sayıya bölündüğünde bölüm 3, kalan 2'dir. Büyük sayı kaçtır?",
  "38", ["36", "12", "40", "37"],
  "Küçük k ise büyük 3k + 2'dir. 4k + 2 = 50 → k = 12; büyük sayı 38.",
  verify=(3 * kok(4*x + 2 - 50) + 2, 38))
q("Bir otobüsteki kadın yolcuların sayısı erkek yolcuların sayısının 2 katıdır. Bir durakta 6 kadın inip 3 erkek bindiğinde kadın ve erkek yolcu sayıları eşitleniyor. Başlangıçta otobüste kaç yolcu vardı?",
  "27", ["18", "24", "30", "36"],
  "Erkek e, kadın 2e: 2e − 6 = e + 3 → e = 9. Başlangıçta 9 + 18 = 27 yolcu vardı.",
  verify=(3 * kok(2*x - 6 - (x + 3)), 27))
q("Bir sınavda her doğru cevap 4 puan kazandırmakta, her yanlış cevap 1 puan götürmektedir. 50 sorunun tamamını cevaplayan bir öğrenci 125 puan almıştır. Öğrenci kaç soruyu doğru cevaplamıştır?",
  "35", ["30", "40", "25", "32"],
  "4d − (50 − d) = 125 → 5d = 175 → d = 35.",
  verify=(kok(4*x - (50 - x) - 125), 35))
q("Bir kumbarada yalnız 1 ₺'lik ve 5 ₺'lik madeni paralar vardır. 1 ₺'liklerin sayısı 5 ₺'liklerin sayısının 3 katıdır. Kumbaradaki toplam para 96 ₺ olduğuna göre kaç tane 5 ₺'lik vardır?",
  "12", ["36", "16", "24", "8"],
  "5 ₺'lik sayısı f ise 1 ₺'likler 3f'dir: 3f + 5f = 8f = 96 → f = 12.",
  verify=(kok(3*x + 5*x - 96), 12))
q("Bir sayının 3 katının 7 eksiği, aynı sayının 2 katının 5 fazlasına eşittir. Bu sayının karesi kaçtır?",
  "144", ["12", "24", "36", "121"],
  "3n − 7 = 2n + 5 → n = 12. Karesi 144.",
  verify=(kok(3*x - 7 - (2*x + 5))**2, 144))
q("Bir dikdörtgenin uzun kenarı kısa kenarından 4 cm fazladır. Dikdörtgenin çevresi 40 cm olduğuna göre alanı kaç cm²'dir?",
  "96", ["80", "100", "120", "84"],
  "Kısa kenar k: 2(k + k + 4) = 40 → k = 8. Kenarlar 8 ve 12; alan 96 cm².",
  verify=((lambda k: k*(k + 4))(kok(2*(2*x + 4) - 40)), 96))
q("Bir tiyatroda ön sıra biletleri 150 ₺, arka sıra biletleri 90 ₺'dir. Satılan 200 biletten 21.600 ₺ elde edildiğine göre kaç ön sıra bileti satılmıştır?",
  "60", ["40", "80", "120", "144"],
  "150o + 90(200 − o) = 21.600 → 60o + 18.000 = 21.600 → o = 60.",
  verify=(kok(150*x + 90*(200 - x) - 21600), 60))
q("Ardışık iki tek sayının karelerinin farkı 56 olduğuna göre küçük sayı kaçtır?",
  "13", ["15", "11", "14", "7"],
  "(n + 2)² − n² = 4n + 4 = 56 → n = 13.",
  verify=(kok((x + 2)**2 - x**2 - 56), 13))
q("Bir depodaki yükün yarısının 20 kg fazlası alınıyor; ardından kalanın yarısının 10 kg fazlası daha alınıyor. Depoda 25 kg yük kaldığına göre başlangıçta kaç kg yük vardı?",
  "180", ["140", "160", "200", "120"],
  "Sondan başa: ikinci alımdan önce kalan K için K/2 − 10 = 25 → K = 70. İlk alımda L/2 − 20 = 70 → L = 180 kg.",
  verify=(kok((x/2 - 20)/2 - 10 - 25), 180))
q("x ve y pozitif tam sayılardır. 3x + 5y = 47 eşitliğini sağlayan kaç farklı (x, y) ikilisi vardır?",
  "3", ["2", "4", "5", "9"],
  "y = 1 → x = 14; y = 4 → x = 9; y = 7 → x = 4. y = 10 için x negatif olur. Üç ikili vardır.",
  verify=(len([(p, r) for p in range(1, 50) for r in range(1, 50) if 3*p + 5*r == 47]), 3))

assert len(Q) == 60, len(Q)

if __name__ == "__main__":
    raise SystemExit(main(
        Q, prefix="mat-denklem-gen", ders="matematik", konu="denklem_esitsizlik_problemler",
        style="SGS Matematik (gerçek sınav 8-15 derinliği)", seed=20261006,
        relative_path="content/matematik/denklem_esitsizlik_problemler.json", label="Denklem, Eşitsizlik ve Problemler",
    ))
