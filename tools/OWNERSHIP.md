# Program sahipliği

| Alan | Sahip | Yazılabilir yollar |
|---|---|---|
| SGS | Codex | `tools/sgs/**`, SGS içerik klasörleri, `content/v2/manifests/sgs.json` |
| SMMM Yeterlilik | Codex | `tools/smmm/**`, `content/yeterlilik/**`, `content/v2/manifests/smmm.json` |
| Ortak altyapı | Koordineli | `tools/shared/**`, kök talimat dosyaları, üretilen birleşik manifest |

Kurallar:

1. SGS ve Yeterlilik aynı sahipte olsa da ayrı üretim kuralları, builder'lar ve
   denetimlerle yönetilir; bir programın içeriği diğerine toplu olarak taşınmaz.
2. `content/v2/manifest.json` elle düzenlenmez; `manifest_merge.py` üretir.
3. Aynı soru iki programa doğrudan bağlanmaz. Önce her iki sınavın kurallarından geçer.
4. Uygulamanın ortak Flutter kodu program içeriği sayılmaz; değişiklik öncesinde iki
   akışın da geriye dönük uyumluluğu kontrol edilir.
5. Klasör/araç refaktörü soru JSON metinlerini değiştiremez.
