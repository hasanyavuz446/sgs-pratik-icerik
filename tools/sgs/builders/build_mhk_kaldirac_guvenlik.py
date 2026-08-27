# -*- coding: utf-8 -*-
"""SGS — Maliyet Muhasebesi / MHK: faaliyet kaldıracı + güvenlik marjı — 12 soru.

Kullanıcı isteği (2026-08-27): "güvenlik payı ve faaliyet kaldıracı sorularını üret".

⚠️ KAPSAM NOTU — bu üretim bilinçli bir istisnadır. 2014-2026 çıkmış sınav arşivinin
2,68 milyon karakterinde "faaliyet kaldıracı" ve "güvenlik marjı/payı" terimleri
SIFIR kez geçiyor (başabaş 7, katkı payı 8 kez geçerken). Yani bu iki alt konu
gerçek SGS profilinde yok; sorular ders bütünlüğü için üretildi, sınav frekansı
için değil. Paket profili değerlendirilirken bu 12 soru hesaba katılmalıdır.

SAHİPLİK: yalnız mmuh-mhk-gen-0061..0072. Paketin 0001-0060 aralığı
build_cost_accounting_harder_calibration.py + bakım builder'larına aittir; bu
builder onların sorularına DOKUNMAZ (§3 "her sorunun tek sahibi olur").

Paket 60 → 72 soru olur (4 test: 20/20/20/12). ⚠️ Silme yerine ekleme seçildi:
QuestionSeeder yalnız upsert eder (insertAllOnConflictUpdate), hiç silmez →
JSON'dan soru çıkarmak mevcut cihazlardan kaldırmaz, yalnız yeni kurulumlarla
eski kurulumları birbirinden ayırırdı.

Tüm hesaplar Python'da üretilir → aritmetik garanti. §5 boy kapısı tasarım
aşamasında ölçüldü: TEK-en-uzun 0/12, TEK-en-kısa 0/12, kör öğrenci %25.
"""
import argparse
import json
import os
import random
import sys

DERS, KONU = "maliyet_muhasebesi", "maliyet_hacim_kar"
PREFIX, SEED = "mmuh-mhk-gen", 20260827
ILK_NO = 61

OUT_APP = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/maliyet_muhasebesi/maliyet_hacim_kar.json"
OUT_CONTENT = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/maliyet_muhasebesi/maliyet_hacim_kar.json"

STIL_HESAP = "SGS Maliyet Muhasebesi (çok adımlı hesap; 2024-2026 sınav zorluğuna kalibre)"
STIL_KAVRAM = "SGS Maliyet Muhasebesi (kavram; sınav stiline kalibre)"


def tl(x):
    """1200000 -> '1.200.000' | 2.5 -> '2,5'"""
    if isinstance(x, float) and x != int(x):
        s = f"{x:,.2f}".rstrip("0").rstrip(".")
        return s.replace(",", "#").replace(".", ",").replace("#", ".")
    return f"{int(x):,}".replace(",", ".")


Q = []


def q(stem, correct, distractors, why, ref, stil=STIL_HESAP):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide: " + stem[:44]
    assert len(set(distractors)) == 4, "çeldirici tekrarı: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors,
                  why=why, ref=ref, stil=stil))


def gen_letters(n, seed, onceki=""):
    """Seed'li DENGELİ KARIŞIM (§6) — rotasyon değil; birleşik dizide de run≤2."""
    r = random.Random(seed)
    base = ["ABCDE"[i % 5] for i in range(n)]
    while True:
        r.shuffle(base)
        dizi = list(onceki) + base
        if all(not (dizi[i] == dizi[i - 1] == dizi[i - 2]) for i in range(2, len(dizi))):
            return base


# ─────────────────────────── FAALİYET KALDIRACI (8) ───────────────────────────

s1, bf1, bd1, sm1 = 8000, 150, 90, 320000
satis1, dm1 = s1 * bf1, s1 * bd1
kp1, kar1 = satis1 - dm1, satis1 - dm1 - sm1
assert (kp1, kar1) == (480000, 160000) and kp1 / kar1 == 3
q(f"Bir işletme dönemde {tl(s1)} adet ürün satmıştır. Birim satış fiyatı {tl(bf1)} ₺, birim değişken "
  f"maliyeti {tl(bd1)} ₺ ve dönemin toplam sabit maliyeti {tl(sm1)} ₺'dir. Buna göre işletmenin faaliyet "
  f"kaldıraç derecesi kaçtır?",
  "3", ["1,5", "2", "2,5", "7,5"],
  f"Toplam katkı payı = {tl(satis1)} − {tl(dm1)} = {tl(kp1)} ₺. Faaliyet kârı = {tl(kp1)} − {tl(sm1)} = "
  f"{tl(kar1)} ₺. Faaliyet kaldıraç derecesi = Toplam Katkı Payı ÷ Faaliyet Kârı = {tl(kp1)} ÷ {tl(kar1)} = **3**.",
  "Maliyet muhasebesi - faaliyet kaldıracı (çok adımlı)")

q("Faaliyet kaldıraç derecesi 4 olan bir işletmenin satış hacmi gelecek dönemde %15 artacaktır. Maliyet "
  "yapısı ve birim fiyatlar değişmediğine göre işletmenin faaliyet kârı yüzde kaç artar?",
  "%60", ["%3,75", "%15", "%19", "%45"],
  "Faaliyet kaldıraç derecesi, satışlardaki yüzde değişimin kârda kaç katı değişim yarattığını gösterir: "
  "%15 × 4 = **%60**. Kaldıraç derecesi bir çarpandır; satış yüzdesine eklenmez.",
  "Maliyet muhasebesi - faaliyet kaldıracı", STIL_KAVRAM)

kar0, fkd3, art3 = 200000, 5, 8
yeni3 = int(kar0 * (1 + fkd3 * art3 / 100))
assert yeni3 == 280000
q(f"Cari dönem faaliyet kârı {tl(kar0)} ₺ ve faaliyet kaldıraç derecesi {fkd3} olan bir işletmenin "
  f"satışlarının gelecek dönemde %{art3} artması beklenmektedir. Sabit maliyetler ile birim katkı payı "
  f"değişmeyeceğine göre gelecek dönem faaliyet kârı kaç ₺ olur?",
  tl(yeni3), [tl(216000), tl(240000), tl(260000), tl(300000)],
  f"Kârdaki yüzde artış = %{art3} × {fkd3} = %{fkd3 * art3}. Yeni kâr = {tl(kar0)} × 1,40 = **{tl(yeni3)} ₺**. "
  f"Satış yüzdesini doğrudan kâra uygulamak {tl(216000)} ₺ verir ve kaldıraç etkisini yok sayar.",
  "Maliyet muhasebesi - faaliyet kaldıracı (çok adımlı)")

aS, aD, aF = 900000, 540000, 240000
bD, bF = 300000, 480000
aKP, aK = aS - aD, aS - aD - aF
bKP, bK = aS - bD, aS - bD - bF
assert aK == bK == 120000 and aKP / aK == 3 and bKP / bK == 5
artA, artB = int(aK * 3 * 0.10), int(bK * 5 * 0.10)
fark4 = artB - artA
assert (artA, artB, fark4) == (36000, 60000, 24000)
q(f"A ve B işletmelerinin dönem satış hasılatı da faaliyet kârı da aynıdır; her ikisinin satış hasılatı "
  f"{tl(aS)} ₺'dir. A işletmesinde toplam değişken maliyet {tl(aD)} ₺ ve toplam sabit maliyet {tl(aF)} ₺; "
  f"B işletmesinde toplam değişken maliyet {tl(bD)} ₺ ve toplam sabit maliyet {tl(bF)} ₺'dir. Satışlar iki "
  f"işletmede de %10 artarsa faaliyet kârlarındaki artış tutarları arasındaki fark kaç ₺ olur?",
  tl(fark4), [tl(12000), tl(36000), tl(60000), tl(96000)],
  f"A: katkı payı {tl(aKP)} ₺, kâr {tl(aK)} ₺ → kaldıraç derecesi 3; kâr artışı {tl(aK)} × 3 × %10 = {tl(artA)} ₺. "
  f"B: katkı payı {tl(bKP)} ₺, kâr {tl(bK)} ₺ → kaldıraç derecesi 5; kâr artışı {tl(bK)} × 5 × %10 = {tl(artB)} ₺. "
  f"Fark = **{tl(fark4)} ₺**. Sabit maliyet ağırlığı yüksek olan B, aynı satış artışından daha çok kâr çıkarır.",
  "Maliyet muhasebesi - faaliyet kaldıracı (karşılaştırmalı; çok adımlı)")

fi5, be5 = 20000, 15000
gmo5 = (fi5 - be5) / fi5
assert gmo5 == 0.25 and 1 / gmo5 == 4
q(f"Bir işletmenin dönem içindeki fiili satışları {tl(fi5)} adet, başabaş noktası satışları ise {tl(be5)} "
  f"adettir. Buna göre işletmenin faaliyet kaldıraç derecesi kaçtır?",
  "4", ["0,25", "1,25", "2,5", "5"],
  f"Güvenlik marjı oranı = ({tl(fi5)} − {tl(be5)}) ÷ {tl(fi5)} = %25. Faaliyet kaldıraç derecesi bu oranın "
  f"tersidir: 1 ÷ 0,25 = **4**. İki ölçü aynı bilgiyi verir; güvenlik marjı daraldıkça kaldıraç büyür.",
  "Maliyet muhasebesi - faaliyet kaldıracı ↔ güvenlik marjı (çok adımlı)")

q("Faaliyet kaldıraç derecesi 2,5 olan bir işletmenin faaliyet kârı bir önceki döneme göre %30 artmıştır. "
  "Birim satış fiyatı, birim değişken maliyet ve toplam sabit maliyet değişmediğine göre işletmenin satış "
  "hacmi yüzde kaç artmıştır?",
  "%12", ["%7,5", "%27,5", "%30", "%75"],
  "Kârdaki yüzde değişim = satıştaki yüzde değişim × kaldıraç derecesi. Buradan satıştaki değişim = "
  "%30 ÷ 2,5 = **%12**. %75 sonucu, bölme yerine çarpma yapıldığında ortaya çıkar.",
  "Maliyet muhasebesi - faaliyet kaldıracı (ters; çok adımlı)")

bf7, bd7, sm7 = 60, 36, 240000
bkp7 = bf7 - bd7
k12, k20 = 12000 * bkp7 - sm7, 20000 * bkp7 - sm7
assert (12000 * bkp7) / k12 == 6 and (20000 * bkp7) / k20 == 2
q(f"Birim satış fiyatı {tl(bf7)} ₺, birim değişken maliyeti {tl(bd7)} ₺ ve toplam sabit maliyeti {tl(sm7)} ₺ "
  f"olan bir işletmenin satışları {tl(12000)} adetten {tl(20000)} adede çıkmıştır. İşletmenin faaliyet "
  f"kaldıraç derecesi bu değişimle birlikte nasıl olmuştur?",
  "6'dan 2'ye düşmüştür",
  ["2'den 6'ya yükselmiştir", "4'ten 2'ye düşmüştür", "3'ten 5'e yükselmiştir", "6 düzeyinde sabit kalmıştır"],
  f"Birim katkı payı {tl(bkp7)} ₺'dir. {tl(12000)} adette kâr = {tl(12000 * bkp7)} − {tl(sm7)} = {tl(k12)} ₺ → "
  f"kaldıraç = {tl(12000 * bkp7)} ÷ {tl(k12)} = 6. {tl(20000)} adette kâr = {tl(20000 * bkp7)} − {tl(sm7)} = "
  f"{tl(k20)} ₺ → kaldıraç = {tl(20000 * bkp7)} ÷ {tl(k20)} = 2. İşletme başabaş noktasından uzaklaştıkça "
  f"kaldıraç derecesi **küçülür**.",
  "Maliyet muhasebesi - faaliyet kaldıracı (hacim etkisi; çok adımlı)")

kp8, kar8 = 500000, 100000
assert kp8 / kar8 == 5
q(f"Bir işletmenin dönem toplam katkı payı {tl(kp8)} ₺, faaliyet kârı ise {tl(kar8)} ₺'dir. Buna göre "
  f"işletmenin faaliyet kaldıracı ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
  f"Satışlar %10 azalırsa faaliyet kârı da %10 azalarak {tl(90000)} ₺'ye iner",
  [f"Satışlar %10 artarsa faaliyet kârı %50 artarak {tl(150000)} ₺'ye yükselir",
   "Faaliyet kaldıraç derecesi 5 olup toplam katkı payının faaliyet kârına bölünmesiyle bulunur",
   "İşletme başabaş noktasına yaklaştıkça faaliyet kaldıraç derecesi büyür",
   "Sabit maliyetlerin toplam maliyet içindeki payı arttıkça aynı satış düzeyinde kaldıraç derecesi yükselir"],
  f"Kaldıraç derecesi = {tl(kp8)} ÷ {tl(kar8)} = 5. Satışlardaki %10 azalma kârı %10 değil, 5 katı yani "
  f"**%50** azaltır; kâr {tl(kar8)} ₺'den {tl(50000)} ₺'ye iner. Kaldıraç iki yönde de çarpan olarak işler.",
  "Maliyet muhasebesi - faaliyet kaldıracı (olumsuz kök)")

# ──────────────────────────── GÜVENLİK MARJI (4) ────────────────────────────

beT, gmO = 800000, 0.20
fiiliT = int(beT / (1 - gmO))
assert fiiliT == 1000000
q(f"Bir işletmenin başabaş noktası satış tutarı {tl(beT)} ₺ ve güvenlik marjı oranı %20'dir. Buna göre "
  f"işletmenin dönem içindeki fiili satış hasılatı kaç ₺'dir?",
  tl(fiiliT), [tl(640000), tl(960000), tl(1200000), tl(4000000)],
  f"Güvenlik marjı oranı fiili satışlar üzerinden hesaplanır; başabaş satışları fiili satışların %80'ine "
  f"karşılık gelir. Fiili satış = {tl(beT)} ÷ 0,80 = **{tl(fiiliT)} ₺**. {tl(960000)} ₺ sonucu, oranın "
  f"yanlışlıkla başabaş tutarına eklenmesiyle bulunur.",
  "Maliyet muhasebesi - güvenlik marjı (ters; çok adımlı)")

satisG, kpO, gmO2 = 2000000, 0.40, 0.30
gmTutar = int(satisG * gmO2)
karG = int(satisG * kpO * gmO2)
assert (gmTutar, karG) == (600000, 240000)
q(f"Dönem satış hasılatı {tl(satisG)} ₺ olan bir işletmenin katkı payı oranı %40, güvenlik marjı oranı ise "
  f"%30'dur. Buna göre işletmenin dönem faaliyet kârı kaç ₺'dir?",
  tl(karG), [tl(140000), tl(280000), tl(600000), tl(800000)],
  f"Başabaş noktasının üzerindeki satışların katkı payı doğrudan kâra dönüşür. Güvenlik marjı tutarı = "
  f"{tl(satisG)} × %30 = {tl(gmTutar)} ₺; bunun katkı payı = {tl(gmTutar)} × %40 = **{tl(karG)} ₺**. "
  f"Kısaca kâr marjı = katkı payı oranı × güvenlik marjı oranı = %12.",
  "Maliyet muhasebesi - güvenlik marjı × katkı payı oranı (çok adımlı)")

bf3, bd3, sm3a, sm3b, fi3 = 80, 50, 300000, 360000, 16000
kp3 = bf3 - bd3
be3a, be3b = sm3a // kp3, sm3b // kp3
gm3a, gm3b = (fi3 - be3a) / fi3, (fi3 - be3b) / fi3
assert (be3a, be3b) == (10000, 12000) and gm3a == 0.375 and gm3b == 0.25
q(f"Birim satış fiyatı {tl(bf3)} ₺, birim değişken maliyeti {tl(bd3)} ₺ olan bir işletme dönemde {tl(fi3)} "
  f"adet satmaktadır. İşletmenin toplam sabit maliyeti {tl(sm3a)} ₺'den {tl(sm3b)} ₺'ye yükselmiştir. Satış "
  f"miktarı ile birim değerler değişmediğine göre işletmenin güvenlik marjı oranı kaç puan azalır?",
  "12,5", ["6,25", "10", "15", "20"],
  f"Birim katkı payı {tl(kp3)} ₺'dir. Başabaş noktası {tl(sm3a)} ÷ {tl(kp3)} = {tl(be3a)} adetten "
  f"{tl(sm3b)} ÷ {tl(kp3)} = {tl(be3b)} adede çıkar. Güvenlik marjı oranı ({tl(fi3)}−{tl(be3a)})÷{tl(fi3)} = "
  f"%37,5 iken ({tl(fi3)}−{tl(be3b)})÷{tl(fi3)} = %25 olur; azalış **12,5 puandır**.",
  "Maliyet muhasebesi - güvenlik marjı (sabit maliyet etkisi; çok adımlı)")

fi4, be4, bkp4 = 25000, 20000, 12
gm4 = (fi4 - be4) / fi4
assert gm4 == 0.20 and 1 / gm4 == 5 and (fi4 - be4) * bkp4 == 60000
q(f"Bir işletmenin fiili satışları {tl(fi4)} adet, başabaş noktası satışları {tl(be4)} adet ve birim katkı "
  f"payı {tl(bkp4)} ₺'dir. Buna göre aşağıdaki ifadelerden hangisi yanlıştır?",
  "Güvenlik marjı oranı %25 olup satışların bu oranda azalması işletmeyi başabaş noktasına indirir",
  [f"Güvenlik marjı {tl(5000)} adet olup bu satışların ortadan kalkması kârı {tl(60000)} ₺ azaltır",
   f"Dönem faaliyet kârı {tl(60000)} ₺'dir; çünkü başabaş üzerindeki her adet birim katkı payı kadar kâr getirir",
   f"Satışlar {tl(be4)} adede indiğinde işletme ne kâr ne de zarar eder",
   "Güvenlik marjı oranı faaliyet kaldıraç derecesinin tersi olduğundan buradaki kaldıraç derecesi 5'tir"],
  f"Güvenlik marjı = {tl(fi4)} − {tl(be4)} = {tl(5000)} adet; oran = {tl(5000)} ÷ {tl(fi4)} = **%20**, %25 değil. "
  f"Diğer ifadeler tutarlıdır: kâr = {tl(5000)} × {tl(bkp4)} = {tl(60000)} ₺ ve kaldıraç derecesi = 1 ÷ 0,20 = 5.",
  "Maliyet muhasebesi - güvenlik marjı (olumsuz kök)")

assert len(Q) == 12, len(Q)


def uret():
    mevcut = json.load(open(OUT_APP, encoding="utf-8"))
    benim = {f"{PREFIX}-{ILK_NO + i:04d}" for i in range(len(Q))}
    korunan = [x for x in mevcut if x["id"] not in benim]
    onceki = "".join(x["answer"] for x in sorted(korunan, key=lambda z: z["id"]))
    harfler = gen_letters(len(Q), SEED, onceki=onceki)

    yeni = []
    for i, (f, ans) in enumerate(zip(Q, harfler)):
        kalan = [h for h in "ABCDE" if h != ans]
        opts = {ans: f["correct"]}
        for h, d in zip(kalan, f["distractors"]):
            opts[h] = d
        assert len(set(opts.values())) == 5, f["stem"][:44]
        yeni.append({
            "id": f"{PREFIX}-{ILK_NO + i:04d}",
            "ders": DERS, "konu": KONU,
            "stem": f["stem"],
            "options": {h: opts[h] for h in "ABCDE"},
            "answer": ans,
            "solution": f["why"],
            "source": {"kind": "generated", "styleRef": f["stil"], "legislationRef": f["ref"]},
            "validYear": 2026,
            "mockExamId": None,
        })
    return sorted(korunan + yeni, key=lambda z: z["id"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="yazma; dosyadaki içerik builder çıktısıyla aynı mı doğrula")
    args = ap.parse_args()
    out = uret()
    if args.check:
        mevcut = json.load(open(OUT_APP, encoding="utf-8"))
        if mevcut != out:
            print(f"FARK VAR: {OUT_APP}")
            return 1
        print(f"✅ {os.path.basename(OUT_APP)} builder çıktısıyla aynı ({len(out)} soru)")
        return 0
    for path in (OUT_APP, OUT_CONTENT):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(out, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
    print(f"yazıldı: {len(out)} soru (12 yeni) → 2 depo")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
