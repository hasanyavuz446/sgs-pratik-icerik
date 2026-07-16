# Claude çalışma kapsamı

Claude bu depoda varsayılan olarak yalnız SGS alanının sahibidir:

- `tools/sgs/**`
- `content/yeterlilik` dışındaki SGS içerik klasörleri
- `content/v2/manifests/sgs.json`

SMMM Yeterlilik yolları (`tools/smmm/**` ve `content/yeterlilik/**`) Codex'e aittir.
Kullanıcı açıkça istemedikçe Claude bu dosyalara yazmaz. Ortak dosyalar için
`tools/OWNERSHIP.md` kuralları uygulanır ve iki denetim çalıştırılır.
