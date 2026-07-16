# SMMM Yeterlilik araçları — Codex sahipliği

Bu klasör yalnız SMMM Yeterlilik sınavı içindir.

- Kurallar: `tools/smmm/URETIM_KURALLARI.md`
- Üreticiler: `tools/smmm/builders/`
- Düzelticiler: `tools/smmm/fixers/`
- Denetimler: `tools/smmm/audit/`
- Baseline: `tools/smmm/baselines/`
- Testler: `tools/smmm/tests/`

```bash
python3 tools/smmm/audit/audit.py --manifest content/v2/manifests/smmm.json
python3 -m unittest tools/smmm/tests/test_audit.py
```

Bu giriş noktaları SGS paketlerini kabul etmez.
