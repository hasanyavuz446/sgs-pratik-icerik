# Codex çalışma kapsamı

Codex bu depodaki iki sınav programının da sahibidir. İçerikler tek uygulamada
sunulsa da iki ayrı ürün gibi yönetilir:

- **SGS:** `tools/sgs/**`, SGS içerik klasörleri ve
  `content/v2/manifests/sgs.json`
- **SMMM Yeterlilik:** `tools/smmm/**`, `content/yeterlilik/**` ve
  `content/v2/manifests/smmm.json`

Bir programda yapılan kural, builder veya içerik değişikliği diğer programa
kendiliğinden uygulanmaz. Ortak dosyalar için `tools/OWNERSHIP.md` kuralları
uygulanır; ortak altyapı değişikliğinde iki programın denetimi de çalıştırılır.
