# SGS araçları — Codex sahipliği

Bu klasör yalnız SMMM Staja Giriş Sınavı içindir.

- **Kurallar:** `tools/sgs/URETIM_KURALLARI.md` — bağlayıcı üretim ve kalite standardı.
  Yeni konuya başlamadan önce en az §5 (şık sızıntısı) ve §9 (güncellik) okunur.
- **Çıkmış soru analizi:** `reports/SGS_CIKMIS_SORULAR_ANALIZI_2026-07-22.md` —
  2014–2026 arasındaki 38 sınavın yapı, biçim ve kapsam bulguları.
- **Üreticiler:** `tools/sgs/builders/build_<konu>.py` — JSON elle yazılmaz.
- **Uzman bakım yamaları:** `build_*_cleanup.py` dosyaları — eski üreticiler yeniden
  çalıştırıldığında öncül, yakın-tekrar ve seçenek dengesi düzeltmelerinin geri
  alınmadığını `--check` ile doğrular.

```bash
python3 tools/sgs/audit.py content/<ders>/<konu>.json      # tek paket
python3 tools/sgs/audit.py --manifest content/v2/manifest.json
python3 tools/sgs/tests/test_audit.py                      # denetimin regresyon testleri
python3 tools/sgs/builders/build_oncul_single_correct_cleanup.py --check
python3 tools/sgs/builders/build_near_duplicate_cleanup.py --check
python3 tools/sgs/builders/build_legal_oncul_cleanup.py --check
python3 tools/sgs/builders/build_option_balance_cleanup.py --check
python3 tools/sgs/builders/build_financial_accounting_semantic_cleanup.py --check
```

SMMM Yeterlilik biçim kotaları, konu yapısı ve denetim kararları burada uygulanmaz.
Ancak iki programın **kalite doktrini ortaktır**: `URETIM_KURALLARI.md` §5–§7 ile
`tools/smmm/URETIM_KURALLARI.md` §5–§7 bilerek eşitlenmiştir. Birinde bir kural
değişiyorsa diğerinde de değerlendirilir.
