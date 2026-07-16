# SMMM Yeterlilik — soru üretim kuralları

Bu belge, SMMM Yeterlilik soru paketleri üretilirken uyulacak kuralları tanımlar.
Kurallar teorik değil: her biri gerçek bir hatadan öğrenildi ve gerekçesi yazılı.

**Teslim kapısı:** ürettiğin her paket şu denetimden geçmek zorunda:

```bash
python3 tools/audit.py content/yeterlilik/<dosyan>.json
```

**FATAL varsa paket yayına gidemez.** UYARI'ları da sıfırlamayı hedefle.
Denetimi sen çalıştır; "sonra bakılır" diye teslim etme.

---

## 0. SINAV STİL PROFİLİ — neyi üreteceğini bu belirler

Diğer tüm kurallar "nasıl üretilir"i anlatır. Bu bölüm **ne üretileceğini** anlatır ve
tahmine değil, gerçek kitapçığa dayanır.

### Sınav 2026/1'de klasikten çoktan seçmeliye geçti

TESMER'in 14 Ocak 2026 kararıyla sınav tipi kökten değişti:

| Dönem | Format |
|---|---|
| 2024/1 – 2025/3 (6 dönem) | **KLASİK** — açık uçlu, soru başına 10 puan |
| **2026/1** | **TEST** — 5 şıklı A-E çoktan seçmeli |

⚠️ **Yeni formatta tek çıkmış dönem var: 2026/1 (8 kitapçık / 160 soru).** Aşağıdaki
oranlar o tek dönemden ölçüldü → **küçük örneklem**. Nokta değer değil, hedef aralık
olarak kullan. 2024-2025'in 48 klasik kitapçığı soru BİÇİMİ için kullanılamaz; ama
hangi konunun ne sıklıkla sorulduğu için değerlidir.

Kaynak: `~/Downloads/smmm-yeterlilik-sinavi-2026-1-*.pdf`

### Ders bazında soru tipi dağılımı (2026/1, 160 soru — ölçülmüş)

| Ders | yevmiye | hesap | negatif kök | öncüllü | kavramsal |
|---|---|---|---|---|---|
| **Finansal Muhasebe** | **11/20 (%55)** | 0 | 0 | **0** | 9 (%45) |
| **Finansal Tablolar ve Analizi** | 0 | **8/20 (%40)** | 0 | **0** | 12 (%60) |
| **Maliyet Muhasebesi** | 0 | **5/20 (%25)** | 0 | **0** | 15 (%75) |
| **Muhasebe Denetimi** | 0 | 0 | 3/20 (%15) | **0** | 17 (%85) |
| **Hukuk** | 0 | 0 | 2/20 (%10) | 1/20 (%5) | 17 (%85) |
| **Vergi Mevzuatı** | 0 | 3/20 (%15) | 3/20 (%15) | 1/20 (%5) | 13 (%65) |
| **SPK Mevzuatı** | 0 | 0 | **6/20 (%30)** | 3/20 (%15) | 11 (%55) |
| **Meslek Hukuku** | 0 | 0 | 1/20 (%5) | 1/20 (%5) | 18 (%90) |
| **TOPLAM** | 11 (%7) | 16 (%10) | 15 (%9) | **6 (%4)** | 112 (%70) |

**Dersin karakterine uy.** Yevmiye yalnız FM'de, hesap FM dışındaki sayısal derslerde,
negatif kök ağırlıklı SPK'da, öncüllü yalnız 4 hukuk/mevzuat dersinde.

### 🔴 Mevcut içeriğimiz bu profilden sapıyor (2026-07-16 ölçümü, 1740 soru)

| Ölçüt | GERÇEK | BİZDE | Yapılacak |
|---|---|---|---|
| FM'de yevmiye kaydı | **%55** | **%1** | FM'yi yevmiye ağırlıklı yeniden yaz |
| Öncüllü (genel) | **%4** | **%13** | ~3 kat azalt |
| FM·Maliyet·Denetim·Fin.Tablolar'da öncüllü | **0** | %13-14 | **tamamen kaldır** |
| Negatif kök ("hangisi yanlıştır") | **15 soru** | **0** | ekle |
| Öncül sayısı | **3–6** | hepsi 3 | 4-5-6 öncüllü de üret |
| Maliyet'te hesap | %25-30 | %26 | ✅ tutuyor, koru |

### Soru tipi 1 — YEVMİYE (yalnız Finansal Muhasebe, ~%55)

İki alt biçim var, ikisini de üret:

**(a) Tablo şıklı** (~4/20). Şıklar yevmiye kaydının kendisi. Gerçek örnek:

> **1.** İşletme, kredili olarak satın aldığı ticari mallarla ilgili 4.000 ₺ + KDV(%20)
> tutarındaki taşıma gideri için nakliye şirketine satıcı adına nakit ödeme yapmıştır.
> **Bu işleme ilişkin günlük defter kaydı aşağıdakilerden hangisidir?**
>
> **A)** `320 SATICILAR 4.800 / 100 KASA 4.800` ✔
> **B)** `320 SATICILAR 4.000 · 191 İNDİRİLECEK KDV 800 / 100 KASA 4.800`
> **C)** `153 TİCARİ MALLAR 4.000 · 191 İNDİRİLECEK KDV 800 / 320 SATICILAR 4.800`

Şema `stimulus`/markdown tablo destekliyor; hesap adları **BÜYÜK HARF + kod**, ₺ sembolü.

**(b) Metin şıklı** (~7/20). Şıklar kaydı cümleyle anlatır. Gerçek örnek:

> **14.** İşletme, yaptığı kasa sayımı sonucunda kasada 12.000 ₺ bulunduğunu saptamıştır.
> Aynı anda Kasa hesabının borç kalanı 13.000 ₺'dir. Aradaki farkın, satıcılara ödendiği
> hâlde kayıtlara geçirilmeyen bir ödemeden kaynaklandığı saptanmıştır.
> **Buna göre yapılacak günlük defter kaydıyla ilgili aşağıdakilerden hangisi doğrudur?**
>
> **A)** Satıcılar hesabına 1.000 ₺ borç kayıt yapılır. ✔
> **B)** Kasa hesabına 1.000 ₺ borç kayıt yapılır.
> **C)** Sayım ve Tesellüm Fazlaları hesabına 1.000 ₺ borç kayıt yapılır.

⚠️ (b) biçiminde şıklar **doğal olarak kısa ve benzer boyda** — length-tell kuralına
(bkz. §3) uymak kolay. Bu yüzden yevmiye sorusu üretmek kaliteyi de yükseltir.

### Soru tipi 2 — NEGATİF KÖK (bizde SIFIR, gerçekte 15 soru)

"aşağıdakilerden hangisi **yanlıştır** / **değildir**" — ayrı bir beceri; adayın hiç
pratiği olmuyor. Ağırlık: SPK %30, Denetim %15, Vergi %15, Hukuk %10, Meslek H. %5.
FM · Maliyet · Fin.Tablolar'da **yok**.

⚠️ Negatif kökte **length-tell tersine döner**: doğru şık = YANLIŞ ifade. Kısa-doğru
kuralını buna göre uygula → *yanlış olan* şık kısa, *doğru olan 4 çeldirici* uzun.

### Soru tipi 3 — HESAP

FM'de **yok** (oradaki sayısal iş yevmiyeye gömülü). Fin.Tablolar %40 (oran/analiz),
Maliyet %25, Vergi %15. Kalıp: `… kaç ₺'dir?` → şıklar tek satır sayı.
Gerçek örnekte şıklar tek satıra diziliyor: `A) 18.000  B) 34.000  C) 42.000  D) 42.500  E) 60.000`

---

## 1. ALTIN KURAL: elle JSON yazma, builder yaz

Soruları doğrudan JSON'a yazma. Bir `build_<konu>.py` üret, JSON'u o üretsin.

Sebebi mekanik: harf ataması, şık yerleşimi ve çözüm metni **tek geçişte birlikte**
üretilirse, aralarında tutarsızlık çıkması *imkânsız* hâle gelir. Elle yazılan
JSON'da bu tutarsızlıklar kaçınılmaz olarak birikiyor.

### Kopyala-kullan iskelet

```python
# -*- coding: utf-8 -*-
"""<Konu adı> — 60 soru. Doğru şık KISA, çeldiriciler UZUN."""
import json, random

Q = []
def q(stem, correct, distractors, why, ref, difficulty="medium"):
    """correct = doğru şıkkın METNİ (harf DEĞİL). distractors = 4 yanlış metin."""
    assert len(distractors) == 4, stem[:40]
    Q.append({"stem": stem, "correct": correct, "distractors": distractors,
              "why": why, "ref": ref, "difficulty": difficulty})

# ── Sorular ────────────────────────────────────────────────────────────────
q("TMS 2'ye göre aşağıdakilerden hangisi stok tanımına girer?",
  "Olağan iş akışında satılmak üzere elde tutulan ticari mallar",          # KISA
  ["İşletmenin yönetim faaliyetlerinde kullanılmak üzere edinilen hizmet binası",  # UZUN
   "Uzun vadeli değer artışı beklentisiyle yatırım amacıyla satın alınan arsa",
   "Çalışanlara verilen ve ileride tahsil edilecek olan personel avansları",
   "İşletmenin ortaklarına karşı yükümlülüğünü gösteren ihraç edilmiş sermaye"],
  "Olağan faaliyet kapsamında satılmak üzere elde tutulan varlıklar stoktur. "
  "Yönetim binası ve yatırım amaçlı arsa farklı standartların kapsamındadır.",
  "TMS 2 Stoklar - stok tanımı", difficulty="easy")

# ── Harf dizisi: seed'li DENGELİ KARIŞIM (round-robin DEĞİL) ───────────────
def gen_letters(n_each=12, seed=20260715):
    """Her harften n_each tane, aynı harf en fazla 2 kez ardışık, örüntüsüz."""
    r = random.Random(seed)
    while True:
        seq = list("ABCDE") * n_each
        r.shuffle(seq)
        if all(not (seq[i] == seq[i-1] == seq[i-2]) for i in range(2, len(seq))):
            return seq

def build():
    assert len(Q) == 60, f"60 olmalı, şu an {len(Q)}"
    letters = gen_letters()
    out = []
    for i, item in enumerate(Q):
        ans = letters[i]
        choices = {ans: item["correct"]}
        for k, d in zip([k for k in "ABCDE" if k != ans], item["distractors"]):
            choices[k] = d
        out.append({
            "id": f"topic-<kisaltma>-{i+1:04d}",
            "lessonId": "<curriculum.json'daki lessonId>",
            "topicId": "<curriculum.json'daki topicId>",
            "question": item["stem"],
            "choices": choices,
            "correctAnswer": ans,
            "explanation": item["why"],          # ← harfe ATIF YOK (bkz. §4)
            "source": {"kind": "generated",
                       "styleRef": "2026 SMMM beş seçenekli test",
                       "legislationRef": item["ref"]},
            "tags": ["Demo Soru", "2026 Formatı", "Konu Havuzu", "<Konu etiketi>"],
            "difficulty": item["difficulty"],
            "updatedAt": "2026-07-15T00:00:00Z",
            "examPeriod": "2026 test sistemine uyumlu özgün soru",
            "legislationVersion": "TFRS 2026 Seti",
            "sourceUpdatedAt": "2026-07-15T00:00:00Z",
            "isPremium": False,
            "isActive": True,
        })
    return out

if __name__ == "__main__":
    F = "content/yeterlilik/questions_topic_<konu>_2026.json"
    json.dump(build(), open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("yazıldı:", F)
```

Her yeni konuda `seed` değerini **değiştir** (yoksa tüm dosyalar aynı harf dizisini
paylaşır → dosyalar arası örüntü doğar).

---

## 2. HARF DİZİSİ — FATAL

Doğru cevap harfleri **seed'li dengeli karışım** olmalı. Yani:

- 60 soruda her harften 12 tane (±%25 tolerans)
- Aynı harf en fazla **2 kez** ardışık
- **Hiçbir örüntü yok**: rotasyon, sabit adım, kısa periyot

### ❌ Bunu yapma

```
ABCDEABCDEABCDEABCDE...   ← her harften tam 12 tane, ardışık tekrar yok, AMA FATAL
```

**Gerçekten üretildi.** 240 sorunun tamamı bu diziydi. "Kusursuz dağılım" gibi
görünüyor, aslında felaket: 10 soru çözen aday örüntüyü fark eder ve kalan 50 soruyu
**okumadan** işaretler. Rastgele atmaktan beterdir, çünkü rastgelede %20 tutturur,
burada %100.

`gen_letters()` kullan. Kendi harf sıranı uydurma.

> Not: eski dedektörümüz "12'şer + ardışık≤2" kontrolü yapıyordu ve bu diziyi
> **onaylıyordu**. `tools/audit.py` artık rotasyon, periyot ve bigram çeşitliliğine
> bakıyor. Bu yüzden bu kural artık FATAL.

---

## 3. ŞIK UZUNLUĞU — en yüksek getirili kural

**Doğru şıkkı KISA yaz (≤ ~110 karakter). Çeldiricileri UZUN yaz (~90–115 karakter).**

Sebebi: doğru cevap genelde bir tanım olduğu için doğal olarak uzun yazılır;
çeldiriciler ise "yanlış" diye kısa geçilir. Sonuç: aday şıkları okumadan, sadece
en uzunu seçerek soruyu çözer. Uygulamanın sahibi bu kusuru bizzat şöyle bildirdi:
*"iki uzun cümleli şık var, cevap genelde onlardan biri, diğerlerine bakmadan
çözülüyor."*

### Kanıt

| Yaklaşım | Sonuç |
|---|---|
| Doğru şık uzun tanım olarak yazıldı | **42 length-tell** + 3 tur elle düzeltme |
| Aynı oturumda kısa-doğru / uzun-çeldirici kuralıyla yazıldı | **ilk çalıştırmada 0**, düzeltme yok |

Yani bu kural sana sonradan saatler kazandırıyor. Builder'ın en başına yaz.

### Ölçüt

Denetim şunu işaretler: doğru şık tek başına en uzunsa ve 2. en uzunun 1,5 katıysa;
ya da "2 uzun + 3 kısa" deseni varsa. Pratik hedef: beş şıkkın uzunlukları
birbirine yakın olsun, doğru şık **ortalarda** kalsın.

---

## 4. ÇÖZÜMDE HARF GEÇMESİN

`explanation` içinde **"Doğru cevap A"** gibi bir harf atıfı YAZMA. Çözüm, doğru
cevabı *içerik olarak* anlatsın.

Sebebi: SGS tarafında bu atıf yazılıyordu ve şıklar sonradan permüte edilince
46 soruda çözüm harfi cevapla uyumsuz kaldı — sınav uygulamasında bundan daha
güven kırıcı bir hata yok. Yeterlilik şeması bu atfı hiç kullanmıyor; **bu iyi bir
kural, koru.** Harften bahsetmeyen çözüm, permütasyondan etkilenmez.

---

## 5. ÖNCÜLLÜ SORULAR (I / II / III …)

> 🔴 **BU KURAL 2026-07-17'DE DÜZELTİLDİ.** Eskiden "her 60'lık pakette 6–9 öncüllü
> soru (~%10–15)" yazıyordu ve bu **yanlıştı** — gerçek sınav ölçülmeden, tahminle
> yazılmıştı. 2026/1 kitapçıkları ölçüldüğünde gerçek oranın **%4** olduğu ve dört
> derste **hiç bulunmadığı** görüldü. Bu yanlış kurala uyularak üretilen 228 öncüllü
> soru (bizde %13) fazladır ve azaltılacaktır.

**Ders bazında hedef** (2026/1'den ölçülmüş, bkz. §0):

| Ders | 60 soruluk pakette öncüllü |
|---|---|
| Finansal Muhasebe · Maliyet · Muhasebe Denetimi · Finansal Tablolar | **0 — hiç üretme** |
| Hukuk · Vergi · Meslek Hukuku | **~3** (%5) |
| SPK Mevzuatı | **~9** (%15) |

Kurallar:

- **Öncül sayısı 3 değil, 3–6.** Gerçek sınavda dağılım: 3, 4, 5 ve **6** öncül.
  Bizim 228 öncüllü sorunun tamamı 3 öncüllü — bu monotonluk. 6 öncüllü gerçek örnek
  (Hukuk 2026/1, s.18): *I. Kooperatif · II. Kollektif · III. Adi Komandit ·
  IV. Sermayesi Paylara Bölünmüş Komandit · V. Limited · VI. Anonim →
  "hangileri sermaye şirketidir?"* → cevap **D) III, IV ve VI**.
- Kök kalıbı iki türlü: `…hangileri` veya `…hangisi/hangileri doğrudur?` (ikisi de gerçek).
- Öncülleri `\n\n` ile ayır. **Tek `\n` markdown'da satır başı YAPMAZ**, öncüller
  tek paragrafa yapışır ve soru okunamaz hâle gelir.
- Cevabı çeşitlendir: **"hepsi" oranı ~%20–30** olsun. Sık sık bir öncülü kesin-yanlış
  yap → cevap alt küme olsun ("I ve II" gibi).
- Bir dönem bu oran %75'e çıkmıştı; aday "şüpheye düşersen hepsini işaretle"
  stratejisiyle soruları çözüyordu. 152 soru elle düzeltildi.
- 4+ öncülde şık biçimi: `A) Yalnız I`, `B) I ve III`, `C) II ve IV`, `D) III, IV ve VI`.

```python
q("Aşağıdakilerden hangileri TMS 2'ye göre stok maliyetine dâhildir?"
  "\n\nI. Satın alma bedeli\n\nII. Dönüştürme maliyetleri"
  "\n\nIII. Depolama sonrası genel yönetim giderleri",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Satın alma bedeli ve dönüştürme maliyetleri stok maliyetine girer; "
  "genel yönetim giderleri stok maliyetine alınmaz, dönem gideridir.",
  "TMS 2 - stok maliyeti")
```

---

## 6. YILA BAĞLI ORAN / TUTAR

Amaç: soru bir oran değişince **bayatlamasın**.

| Durum | Karar |
|---|---|
| Oran soru **kökünde veriliyor** — "5.000 TL **+ %20 KDV**" | ✅ **GÜVENLİ**. Ölçülen şey kayıt (191 mi 391 mi), oran değil. Oran değişse soru kendi içinde tutarlı kalır. |
| Senaryo tutarı — "Maliyeti 210.000 TL, ömrü 6 yıl" | ✅ serbest |
| Oran **şıkta**, yani cevabın kendisi — "KDV oranı kaçtır? A) %18 B) %20" | ❌ **İHLAL** |
| Kök oranı vermiyor, bilinmesini bekliyor — "genel oranda KDV'ye tabi" | ❌ **İHLAL** |
| İstisna haddi, gelir vergisi dilimi, yeniden değerleme oranı, asgari ücret | ❌ **İHLAL** (her yıl değişir) |
| Kanunda sabit yapısal sayı — 50 ortak sınırı, YK 3 yıl, çekte 10 gün ibraz | ✅ serbest |

Kısacası: **oranı sen ver, adaydan isteme.**

---

## 7. ARİTMETİĞİ PYTHON İLE DOĞRULA

Hesap içeren her soruda sayıları builder içinde hesapla; kafadan yazma.

```python
maliyet, kalinti, omur = 210_000, 30_000, 6
yillik = (maliyet - kalinti) // omur          # 30.000
q(f"Maliyeti {maliyet:,} TL, kalıntı değeri {kalinti:,} TL ve yararlı ömrü {omur} yıl "
  f"olan varlığın doğrusal yöntemle yıllık amortismanı kaç TL'dir?".replace(",", "."),
  f"{yillik:,} TL".replace(",", "."),
  [...],
  f"Amortismana tabi tutar {maliyet-kalinti:,} TL'dir; {omur} yıla bölününce "
  f"yıllık {yillik:,} TL bulunur.".replace(",", "."),
  "TMS 16 - doğrusal amortisman")
```

Çeldiriciler **makul hata sonuçları** olsun (kalıntı değeri düşmeyi unutmak,
yanlış ömre bölmek gibi) — rastgele sayı değil.

---

## 8. TELİF — sorular ÖZGÜN olacak

TESMER soru kitapçığından, çıkmış sınavdan veya üçüncü taraf soru bankasından
metin, şık veya çözüm **kopyalama**. Gerçek sınav yalnız *biçim, süre ve konu
dağılımı* için referanstır. Gerçek kişi/şirket adı kullanma, kurgusal ad ve veri üret.

`source.kind` daima `"generated"` olacak (denetim başka değer kabul etmez).

---

## 9. ŞEMA VE MÜFREDAT BAĞI

- `lessonId` ve `topicId` **`smmm_sgs_pratik/assets/content/curriculum.json`'da
  tanımlı olmak zorunda.** Uydurma; yoksa denetim `unknown_lesson` verir.
- `tags` içinde **`Demo Soru`** zorunlu (validator arıyor).
- `2026 Formatı` etiketi varsa `examPeriod` ve `sourceUpdatedAt` dolu olmalı.
- Havuz ayrımı — bir soru ikisinden **yalnız birine** ait:
  - `Konu Havuzu` → konu testlerinde çıkar
  - etiketsiz → bölüm havuzu, ders testlerinde çıkar
  - Aynı soru iki test türünde görünmemeli.
- `id` ve soru kökü **tekrarsız** olacak (paketler arası da).
- Beş şık A–E, hepsi dolu, `correctAnswer` şıklardan biri.

Yeni paketi manifest'e ekle:

```json
{"file": "yeterlilik/questions_topic_<konu>_2026.json", "programIds": ["yeterlilik"]}
```

ve `content/v2/manifest.json` içindeki `version` değerini **artır**.

---

## 10. TESLİM ÖNCESİ KONTROL LİSTESİ

**Stil (§0 — sınav sadakati):**

- [ ] Dersin soru tipi dağılımı §0'daki tabloya uyuyor
- [ ] **Finansal Muhasebe ise:** soruların ~yarısı yevmiye (tablo + metin şıklı karışık)
- [ ] **FM · Maliyet · Denetim · Fin.Tablolar ise:** öncüllü soru **SIFIR**
- [ ] **Hukuk/Vergi/Meslek ~3, SPK ~9** öncüllü; öncül sayıları 3-6 arasında değişiyor
- [ ] Negatif kök ("hangisi yanlıştır/değildir") dersin oranınca var — ve o sorularda
      length-tell TERS uygulandı (yanlış olan şık kısa)

**Mekanik:**

- [ ] `python3 tools/audit.py content/yeterlilik/<dosya>.json` → **FATAL 0**
- [ ] UYARI'lar sıfır ya da gerekçeli
- [ ] Harf dizisi `gen_letters()` ile üretildi, seed bu konuya özel
- [ ] Doğru şıklar kısa, çeldiriciler uzun (negatif kökte tersi)
- [ ] "hepsi" oranı ~%20–30
- [ ] `explanation` içinde harf atıfı yok
- [ ] Hesap soruları python ile doğrulandı, çeldiriciler makul hata sonuçları
- [ ] `lessonId`/`topicId` curriculum.json'da mevcut
- [ ] manifest'e eklendi + `version` artırıldı
- [ ] Builder (`build_<konu>.py`) da commit edildi — sonraki konu onu kopyalayacak

> Bu kuralların hiçbiri stil tercihi değil. Her biri, yayına gitmiş ya da gitmek
> üzere olan gerçek bir kusurdan çıkarıldı. Uymadığın bir kural varsa gerekçesini
> yaz — sessizce atlama.
