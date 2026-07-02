# SGS Pratik — İçerik

**SGS Pratik** uygulamasının OTA (mağazasız) soru bankası içeriği.

Uygulama açılışta `content/manifest.json`'daki `version`'ı kontrol eder; uzak
sürüm yerelden yeniyse paketleri indirip yerel önbelleği tazeler. Böylece yeni
soru paketleri **uygulama güncellemesi olmadan** telefona düşer.

## Yapı

```
content/
  manifest.json                 # { "version": "...", "packs": [ { "file": "..." } ] }
  <ders>/<konu>.json            # soru paketi (Question dizisi)
```

## Yeni içerik yayınlama

1. Yeni paket JSON'unu `content/<ders>/<konu>.json` olarak ekle.
2. `manifest.json`'a paketi ekle **ve `version`'ı artır** (ör. `"1"` → `"2"`).
3. `git add -A && git commit && git push` → uygulama bir sonraki açılışta çeker.

`version` her yayında artmalı; uygulama sürüm **farklıysa** indirir.

## Soru şeması

```json
{
  "id": "finmuh-<konu>-gen-0001",
  "ders": "finansal_muhasebe",
  "konu": "muhasebenin_temel_kavramlari",
  "stem": "markdown (pipe-tablo olabilir)",
  "options": { "A": "…", "B": "…", "C": "…", "D": "…", "E": "…" },
  "answer": "A",
  "solution": "markdown",
  "source": { "kind": "generated", "styleRef": "…", "legislationRef": "…" },
  "validYear": 2026,
  "mockExamId": null
}
```

Gerçek SGS 5 şıklıdır (A–E). Üretilmiş sorular mevzuata dayanır ve
`legislationRef` ile etiketlenir (oran/eşik değişince bayat soru yakalanabilir).
Gerçek sınav metni telifli — birebir kopyalanmaz.
