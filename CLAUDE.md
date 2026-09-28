# Claude çalışma kapsamı

Claude bu depoda iki programın da sahibidir:

- SGS: `tools/sgs/**`, `content/yeterlilik` dışındaki SGS içerik klasörleri,
  `content/v2/manifests/sgs.json`
- SMMM Yeterlilik (2026-09-28'de kullanıcı kararıyla Codex'ten devralındı):
  `tools/smmm/**`, `content/yeterlilik/**`, `content/v2/manifests/smmm.json`

İki program ayrı kurallar, builder'lar ve denetimlerle yönetilir
(`tools/sgs/URETIM_KURALLARI.md`, `tools/smmm/URETIM_KURALLARI.md`). Ortak dosyalar
için `tools/OWNERSHIP.md` kuralları uygulanır ve iki denetim çalıştırılır.
