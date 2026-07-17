# SGS araçları — Claude sahipliği

Bu klasör yalnız SMMM Staja Giriş Sınavı içindir.

- **Kurallar:** `tools/sgs/URETIM_KURALLARI.md` — bağlayıcı üretim ve kalite standardı.
  Yeni konuya başlamadan önce en az §5 (şık sızıntısı) ve §9 (güncellik) okunur.
- **Üreticiler:** `tools/sgs/builders/build_<konu>.py` — JSON elle yazılmaz.
- **Açık kusur raporu:** `tools/sgs/SIK_ORUNTUSU_RAPORU.md` — 53 dosyada şık örüntüsü;
  içerik düzeltmesi bekliyor.

```bash
python3 tools/sgs/audit.py content/<ders>/<konu>.json      # tek paket
python3 tools/sgs/audit.py --manifest content/v2/manifest.json
python3 tools/sgs/tests/test_audit.py                      # denetimin regresyon testleri
```

SMMM Yeterlilik biçim kotaları, konu yapısı ve denetim kararları burada uygulanmaz.
Ancak iki programın **kalite doktrini ortaktır**: `URETIM_KURALLARI.md` §5–§7 ile
`tools/smmm/URETIM_KURALLARI.md` §5–§7 bilerek eşitlenmiştir. Birinde bir kural
değişiyorsa diğerinde de değerlendirilir.
