# İçerik araçları

Araçlar sınav sahipliğine göre ayrılmıştır:

```text
tools/
  sgs/       # Claude sahipliği: SGS kuralları, üreticiler ve denetim
  smmm/      # Codex sahipliği: SMMM Yeterlilik kuralları, üreticiler ve denetim
  shared/    # Yalnız sınavdan bağımsız manifest/sahiplik yardımcıları
```

## Temel komutlar

```bash
python3 tools/sgs/audit.py --manifest content/v2/manifest.json
python3 tools/smmm/audit/audit.py --manifest content/v2/manifest.json
python3 tools/shared/check_scope.py --program sgs
python3 tools/shared/check_scope.py --program smmm
python3 tools/shared/manifest_merge.py --check
```

`content/v2/manifest.json` çalışma zamanında kullanılan birleşik dosyadır ve kaynak
manifestlerden üretilir. Program sahipleri yalnız kendi
`content/v2/manifests/<program>.json` dosyasını düzenler.
