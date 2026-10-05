"""Sayısal şıklarda doğru cevabın BÜYÜKLÜK sırasını dengeler (ortanca tell'i).

Kullanım: python3 tools/sgs/sayisal_sira_dengele.py <content/...json> <builder.py> [--yaz]
(--yaz olmadan yalnız planı yazdırır.) Sonra builder `--write` ile çalıştırılır.

Çeldiriciler "doğru değerin biraz altı / biraz üstü" diye üretilince doğru cevap
ortanca kalır; 2026-10-05'te havuzun 1.268 sayısal sorusunda sıra [74,293,398,274,78]
idi. `audit.kor_ogrenci` bunu "sayısal: ortanca değeri seç" stratejisiyle ölçer.

Yöntem: bir çeldirici doğru değere göre AYNALANIR (yeni = 2·doğru − eski); bu, doğru
cevabın sırasını tam bir basamak kaydırır, harf konumu ve öteki şıklar değişmez.
Hedef paket içinde eşit sıra dağılımıdır; bir soruda en çok iki şık değişir.
Korunanlar: çözümde/kökte ARA DEĞER olarak geçen çeldirici (kısmi hesap hatası —
en değerli çeldiricidir), 0 değeri (çoğu zaman "vergi doğmaz" gibi anlamlı şık),
negatif sonuç (şıklar negatif değilse). Çakışmada değerin yuvarlaklığı korunarak
en yakın boş değere kayılır. Değişiklik builder kaynağında, sorunun bloğunda yapılır.
"""
import json, re, sys, collections
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit import SAYI, sayisal_degerler

pack, builder = sys.argv[1], sys.argv[2]; yaz = '--yaz' in sys.argv
Q = json.load(open(pack)); src = open(builder).read()

def parcala(v):
    m = SAYI.fullmatch(v.strip().replace("−", "-"))
    return m.group(1), m.group(2), m.group(3) or "", m.group(4)

def deger(v):
    on, tam, ond, birim = parcala(v)
    return F(tam.replace(".", "") + ond.replace(",", ".")) if ond else F(tam.replace(".", ""))

def bicim(x, sablonlar, ornek):
    """x'i sorunun şık biçimiyle yaz (ondalık, binlik ayırıcı, önek, birim, boşluk)."""
    ond = max(len(parcala(s)[2]) - 1 if parcala(s)[2] else 0 for s in sablonlar)
    grup = any("." in parcala(s)[1] for s in sablonlar)
    if x.denominator != 1 and ond == 0:
        return None
    q = x * 10 ** ond
    if q.denominator != 1:
        return None
    neg = x < 0; x = abs(x)
    tam = int(x); kesir = x - tam
    t = f"{tam:,}".replace(",", ".") if grup and tam >= 1000 else str(tam)
    if ond:
        k = round(kesir * 10 ** ond)
        t += "," + str(k).rjust(ond, "0")
        # 12,00 / 14,50 gibi sıfırla doldurulmuş hane ya da tüm şıklarda aynı hane → sabit tut
        sabit = (len({len(parcala(s)[2]) for s in sablonlar}) == 1
                 or parcala(ornek)[2].endswith("0"))
        if not sabit:
            t = re.sub(r"(,\d*?)0+$", r"\1", t).rstrip(",")
    on, _, _, birim = parcala(ornek)
    ara = re.search(r"\d(\s*)(?:₺|TL|adet|gün|saat|ay|yıl|kg|birim|kişi)$", ornek)
    eksi = "−" if any("−" in x for x in sablonlar) else "-"
    return f"{on}{eksi if neg else ''}{t}" + ((ara.group(1) + birim) if birim else "")

sayisal = []
for q in Q:
    d = sayisal_degerler(q["options"])
    if not d: continue
    s = sorted(d, key=d.get); sayisal.append((q, s.index(q["answer"])))
n = len(sayisal)
once = collections.Counter(r for _, r in sayisal)
hedef = {r: n // 5 + (1 if r < n % 5 else 0) for r in range(5)}
# ortayı (2) en sona bırak: fazlalıklar önce uçlara gitsin
say = collections.Counter(once)
plan = []
for q, r in sorted(sayisal, key=lambda t: t[0]["id"]):
    if say[r] <= hedef[r]: continue
    adaylar = sorted((t for t in range(5) if say[t] < hedef[t] and abs(t - r) <= 2), key=lambda t: (abs(t - r), -(hedef[t] - say[t]), t))
    for t in adaylar:
        o = q["options"]; c = deger(o[q["answer"]])
        dv = {k: deger(v) for k, v in o.items()}
        # aşağı kaydır (t<r): doğrunun altındaki (r−t) çeldiriciyi yukarı aynala; tersi yukarı
        # Çözümde/kökte ara değer olarak geçen çeldirici gerçek bir hata yolundan gelir
        # (kısmi hesap) — en değerli çeldiricidir, aynalanmaz; önce ötekiler kullanılır.
        metin = q["solution"] + " " + q["stem"]
        def anilan(k):
            return bool(re.search(rf"(?<![\d.,]){re.escape(o[k].split(' ')[0])}(?![\d,]|\.\d)", metin))
        if t < r:
            alt = sorted((k for k in dv if dv[k] < c), key=lambda k: (anilan(k), c - dv[k]))
            sec = alt[:r - t]
        else:
            ust = sorted((k for k in dv if dv[k] > c), key=lambda k: (anilan(k), dv[k] - c))
            sec = ust[:t - r]
        if any(anilan(k) or dv[k] == 0 for k in sec): continue
        degis = {}; ok = True
        from math import gcd
        farklar = [abs(v - c) for v in dv.values() if v != c]
        olc = max(x.denominator for x in farklar)
        birim = F(0)
        for x in farklar: birim = F(gcd(int(birim * olc), int(x * olc)), olc)
        for k in sec:
            yon = 1 if dv[k] < c else -1
            adim = birim
            if dv[k].denominator == 1 and dv[k] != 0:
                yuv = 1
                while int(dv[k]) % (yuv * 10) == 0 and (yuv * 10) <= abs(int(dv[k])): yuv *= 10
                if yuv > adim: adim = F(yuv)
            aday = [2 * c - dv[k]] + [2 * c - dv[k] + yon * i * adim for i in range(1, 6)] + [2 * c - dv[k] - yon * i * adim for i in range(1, 4)]
            s = None
            for yeni in aday:
                if (yeni - c) * yon <= 0: continue
                if yeni < 0 and all(v >= 0 for v in dv.values()): continue
                if yeni == 0: continue
                s2 = bicim(yeni, list(o.values()), o[k])
                if s2 is None or s2 in o.values() or s2 in degis.values(): continue
                s = s2; break
            if s is None: ok = False; break
            degis[k] = s
        if ok:
            plan.append((q, r, t, degis)); say[r] -= 1; say[t] += 1; break

print(pack.split('/')[-1], "n", n, "önce", [once[i] for i in range(5)], "sonra", [say[i] for i in range(5)], "değişen soru", len(plan))

# builder'a uygula
def blok(q):
    kid = q["id"][-4:]
    m = re.search(rf"['\"]{kid}['\"]\s*:\s*patch\(", src)
    if m:
        son = re.compile(r"\n    ['\"]\d{4}['\"]\s*:\s*patch\(|\n}\n").search(src, m.end())
        return m.start(), son.start()
    on = q["stem"].split("\n")[0][:40]
    for cand in (on, on.replace("'", "\\'"), on.replace('"', '\\"')):
        i = src.find(cand)
        if i >= 0:
            j = src.find("\nq(", i)
            return i, (j if j > 0 else len(src))
    raise SystemExit(f"blok bulunamadı: {q['id']}")

for q, r, t, degis in plan:
    a, b = blok(q); parca = src[a:b]
    for k, yeni in degis.items():
        eski = q["options"][k]
        bul = [m for m in re.finditer(rf"(['\"]){re.escape(eski)}\1", parca)]
        # patch bloklarında harf anahtarına bağlı olanı seç
        anahtarli = [m for m in bul if re.search(rf"['\"]{k}['\"]\s*:\s*$", parca[:m.start()])]
        if anahtarli: bul = anahtarli
        if len(bul) != 1:
            raise SystemExit(f"{q['id']} {k} '{eski}': blokta {len(bul)} eşleşme")
        m = bul[0]; parca = parca[:m.start()] + m.group(1) + yeni + m.group(1) + parca[m.end():]
        if not yaz: print(f"  {q['id'][-4:]} sıra {r}→{t}  {k}: {eski} → {yeni}  (doğru {q['options'][q['answer']]})")
    src = src[:a] + parca + src[b:]
if yaz:
    open(builder, "w").write(src); print("builder yazıldı")
