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

## 5. ÖNCÜLLÜ SORULAR (I / II / III)

Her 60 soruluk pakette **6–9 öncüllü soru** olsun (~%10–15). Şu an üretilen
Yeterlilik paketlerinde **sıfır** tane var — bu monotonluk, gerçek sınavda bu tip
soru çıkıyor.

Kurallar:

- Öncülleri `\n\n` ile ayır. **Tek `\n` markdown'da satır başı YAPMAZ**, öncüller
  tek paragrafa yapışır ve soru okunamaz hâle gelir.
- Cevabı çeşitlendir: **"I, II ve III" (hepsi) oranı ~%20–30** olsun. Sık sık bir
  öncülü kesin-yanlış yap → cevap alt küme olsun ("I ve II" gibi).
- Bir dönem bu oran %75'e çıkmıştı; aday "şüpheye düşersen hepsini işaretle"
  stratejisiyle soruları çözüyordu. 152 soru elle düzeltildi.

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

- [ ] `python3 tools/audit.py content/yeterlilik/<dosya>.json` → **FATAL 0**
- [ ] UYARI'lar sıfır ya da gerekçeli
- [ ] Harf dizisi `gen_letters()` ile üretildi, seed bu konuya özel
- [ ] Doğru şıklar kısa, çeldiriciler uzun
- [ ] 6–9 öncüllü soru var, "hepsi" oranı ~%20–30
- [ ] `explanation` içinde harf atıfı yok
- [ ] Hesap soruları python ile doğrulandı, çeldiriciler makul hata sonuçları
- [ ] `lessonId`/`topicId` curriculum.json'da mevcut
- [ ] manifest'e eklendi + `version` artırıldı
- [ ] Builder (`build_<konu>.py`) da commit edildi — sonraki konu onu kopyalayacak

> Bu kuralların hiçbiri stil tercihi değil. Her biri, yayına gitmiş ya da gitmek
> üzere olan gerçek bir kusurdan çıkarıldı. Uymadığın bir kural varsa gerekçesini
> yaz — sessizce atlama.
