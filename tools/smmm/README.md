# SMMM Yeterlilik araçları — Claude sahipliği (2026-09-28 devralındı)

Bu klasör yalnız SMMM Yeterlilik sınavı içindir.

- Kurallar: `tools/smmm/URETIM_KURALLARI.md`
- Üreticiler: `tools/smmm/builders/` — güncel olanlar `build_yk_*.py` (konu) ve `build_yb_*.py` (bölüm);
  ortak modüller `yet_ortak.py`, `vergi_ortak.py`, `fm_ortak.py`, `fta_ortak.py`. Eski `build_kh_*`/`build_yet_*`
  ve `fixers/fix_*_quality.py` kilitlidir (yeni içeriğin üzerine yazarlar; `ESKI_BUILDER_CALISTIR=1` ister).
- Düzelticiler: `tools/smmm/fixers/`
- Denetimler: `tools/smmm/audit/`
- Baseline: `tools/smmm/baselines/`
- Testler: `tools/smmm/tests/`

```bash
python3 tools/smmm/audit/audit.py --manifest content/v2/manifests/smmm.json
python3 -m unittest tools/smmm/tests/test_audit.py
```

Bu giriş noktaları SGS paketlerini kabul etmez.
