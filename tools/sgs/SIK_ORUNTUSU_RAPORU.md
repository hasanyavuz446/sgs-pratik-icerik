# Şık örüntüsü denetim raporu — SGS havuzu

Ölçüm tarihi: 2026-07-17  ·  Ölçen: `tools/sgs/audit.py` (`kor_ogrenci`)

**SGS toplamı: 6120 soru, kör öğrenci %37** (rastgele taban %20) — en iyi strateji: “dolguluyu ele, en uzunu seç”.

## Kör öğrenci nedir

Soruyu ve şıkları **hiç okumayan**, yalnız şıkların biçimine bakan bir aday. Dört strateji denenir (en kısayı seç · en uzunu seç · dolgu kalıplı şıkları eleyip en kısayı/en uzunu seç) ve **en yükseği** raporlanır. %20 = rastgele. Yüksek çıkması, şıkların içerikten bağımsız bir örüntü sızdırdığı anlamına gelir.

## Ders bazında

| ders | soru | kör öğrenci | strateji |
|---|---:|---:|---|
| vergi_hukuku 🔴 | 600 | %68 | en uzunu seç |
| borclar_hukuku 🔴 | 420 | %64 | dolguluyu ele, en uzunu seç |
| muhasebe_standartlari 🔴 | 1020 | %52 | dolguluyu ele, en kısayı seç |
| meslek_hukuku 🔴 | 300 | %50 | en uzunu seç |
| ticaret_hukuku 🔴 | 420 | %49 | en uzunu seç |
| turkce 🔴 | 180 | %41 | en uzunu seç |
| denetim 🟡 | 420 | %34 | en uzunu seç |
| maliye 🟡 | 180 | %30 | en uzunu seç |
| ataturk_ilkeleri 🟡 | 180 | %28 | en kısayı seç |
| ekonomi 🟡 | 180 | %28 | en uzunu seç |
| is_ve_sosyal_guvenlik_hukuku ✅ | 180 | %26 | en kısayı seç |
| yabanci_dil ✅ | 180 | %25 | en uzunu seç |
| finansal_muhasebe ✅ | 960 | %19 | en kısayı seç |
| maliyet_muhasebesi ✅ | 360 | %18 | en kısayı seç |
| matematik ✅ | 180 | %17 | en kısayı seç |
| mali_tablolar_analizi ✅ | 360 | %16 | en uzunu seç |

## Dosya bazında (FATAL eşiği %35'i aşan 53 dosya)

| dosya | soru | kör | strateji | doğru en uzun | doğru en kısa |
|---|---:|---:|---|---:|---:|
| `meslek_hukuku/staj_ve_sinavlar.json` | 60 | **%91** | en uzunu seç | %98 | %0 |
| `vergi_hukuku/damga_vergisi.json` | 60 | **%88** | en uzunu seç | %96 | %0 |
| `vergi_hukuku/kdv.json` | 60 | **%85** | en uzunu seç | %96 | %1 |
| `vergi_hukuku/mtv.json` | 60 | **%85** | en uzunu seç | %94 | %1 |
| `meslek_hukuku/sorumluluk_ve_yasaklar.json` | 60 | **%85** | en uzunu seç | %92 | %1 |
| `vergi_hukuku/amme_alacaklari.json` | 60 | **%83** | en uzunu seç | %89 | %5 |
| `ticaret_hukuku/haksiz_rekabet.json` | 60 | **%83** | en uzunu seç | %88 | %9 |
| `vergi_hukuku/emlak_vergisi.json` | 60 | **%81** | en uzunu seç | %90 | %0 |
| `muhasebe_standartlari/tms_10_sonraki_olaylar.json` | 60 | **%81** | dolguluyu ele, en kısayı seç | %10 | %86 |
| `borclar_hukuku/temerrut_tazminat.json` | 60 | **%80** | en uzunu seç | %88 | %5 |
| `vergi_hukuku/gelir_vergisi.json` | 60 | **%78** | en uzunu seç | %84 | %3 |
| `vergi_hukuku/kurumlar_vergisi.json` | 60 | **%76** | en uzunu seç | %84 | %11 |
| `ticaret_hukuku/anonim_sirket.json` | 60 | **%73** | en uzunu seç | %79 | %7 |
| `borclar_hukuku/haksiz_fiil.json` | 60 | **%71** | en uzunu seç | %82 | %11 |
| `borclar_hukuku/ozel_durumlar.json` | 60 | **%71** | en uzunu seç | %80 | %5 |
| `denetim/denetim_raporu.json` | 60 | **%70** | en uzunu seç | %75 | %1 |
| `borclar_hukuku/borc_iliskisi_kaynaklari.json` | 60 | **%70** | en uzunu seç | %74 | %0 |
| `borclar_hukuku/sebepsiz_zenginlesme.json` | 60 | **%70** | en uzunu seç | %72 | %14 |
| `muhasebe_standartlari/tms_12_gelir_vergileri.json` | 60 | **%70** | dolguluyu ele, en kısayı seç | %41 | %41 |
| `muhasebe_standartlari/tms_21_kur_degisimi.json` | 60 | **%70** | dolguluyu ele, en kısayı seç | %26 | %64 |
| `muhasebe_standartlari/tfrs_9_finansal_arac.json` | 60 | **%66** | dolguluyu ele, en kısayı seç | %50 | %38 |
| `muhasebe_standartlari/tms_37_karsiliklar.json` | 60 | **%65** | dolguluyu ele, en kısayı seç | %42 | %46 |
| `muhasebe_standartlari/tms_8_politikalar.json` | 60 | **%63** | dolguluyu ele, en kısayı seç | %26 | %59 |
| `muhasebe_standartlari/tms_23_borclanma_maliyetleri.json` | 60 | **%61** | dolguluyu ele, en kısayı seç | %38 | %51 |
| `muhasebe_standartlari/tms_1_sunulus.json` | 60 | **%58** | en uzunu seç | %64 | %27 |
| `ticaret_hukuku/limited_sahis_sirketleri.json` | 60 | **%58** | en uzunu seç | %61 | %20 |
| `muhasebe_standartlari/tms_40_yatirim_amacli.json` | 60 | **%58** | dolguluyu ele, en kısayı seç | %36 | %50 |
| `denetim/denetim_kaniti.json` | 60 | **%55** | en uzunu seç | %60 | %7 |
| `muhasebe_standartlari/tfrs_16_kiralamalar.json` | 60 | **%55** | dolguluyu ele, en uzunu seç | %59 | %32 |
| `muhasebe_standartlari/tms_38_modv.json` | 60 | **%53** | en kısayı seç | %37 | %49 |
| `denetim/denetim_ornekleme.json` | 60 | **%51** | en uzunu seç | %54 | %14 |
| `ataturk_ilkeleri/ataturk_ilkeleri_dis_politika.json` | 60 | **%51** | en kısayı seç | %18 | %56 |
| `borclar_hukuku/sozlesmenin_kurulmasi.json` | 60 | **%50** | en uzunu seç | %52 | %3 |
| `turkce/sozcukte_cumlede_anlam.json` | 60 | **%50** | en uzunu seç | %51 | %10 |
| `muhasebe_standartlari/tms_7_nakit_akis.json` | 60 | **%50** | dolguluyu ele, en uzunu seç | %62 | %36 |
| `muhasebe_standartlari/tms_36_deger_dusuklugu.json` | 60 | **%50** | dolguluyu ele, en kısayı seç | %46 | %38 |
| `muhasebe_standartlari/kavramsal_cerceve.json` | 60 | **%48** | en uzunu seç | %52 | %26 |
| `muhasebe_standartlari/tms_2_stoklar.json` | 60 | **%46** | en uzunu seç | %62 | %23 |
| `muhasebe_standartlari/tms_20_devlet_tesvik.json` | 60 | **%46** | dolguluyu ele, en uzunu seç | %57 | %36 |
| `ticaret_hukuku/kambiyo_senetleri.json` | 60 | **%45** | en kısayı seç | %33 | %44 |
| `denetim/denetim_standartlari_etik.json` | 60 | **%45** | en kısayı seç | %8 | %48 |
| `muhasebe_standartlari/tms_16_mdv.json` | 60 | **%43** | en uzunu seç | %51 | %38 |
| `vergi_hukuku/vergi_denetimi_ceza_uyusmazlik.json` | 60 | **%43** | en uzunu seç | %50 | %14 |
| `ekonomi/para_banka_dis_ekonomi.json` | 60 | **%43** | en uzunu seç | %46 | %16 |
| `meslek_hukuku/meslek_orgutu_disiplin.json` | 60 | **%43** | en kısayı seç | %22 | %47 |
| `denetim/denetim_riski.json` | 60 | **%41** | en uzunu seç | %59 | %8 |
| `turkce/dil_bilgisi.json` | 60 | **%41** | en uzunu seç | %48 | %13 |
| `is_ve_sosyal_guvenlik_hukuku/is_hukuku_is_sozlesmesi.json` | 60 | **%40** | en kısayı seç | %20 | %43 |
| `ticaret_hukuku/kiymetli_evrak.json` | 60 | **%38** | en uzunu seç | %40 | %22 |
| `vergi_hukuku/vergilendirme_sureci.json` | 60 | **%36** | en kısayı seç | %29 | %41 |
| `borclar_hukuku/borcun_ifasi_sona_ermesi.json` | 60 | **%36** | dolguluyu ele, en uzunu seç | %37 | %11 |
| `ataturk_ilkeleri/ataturk_inkilaplari.json` | 60 | **%35** | en uzunu seç | %43 | %25 |
| `maliyet_muhasebesi/birlesik_maliyet.json` | 60 | **%35** | en kısayı seç | %33 | %52 |

## Kök neden

İki ayrı katman üst üste binmiş:

1. **Boy ipucu (yaygın olan).** Kavramsal derslerde doğru şık neredeyse hep en uzun yazılmış (ör. `vergi_hukuku/kdv.json` %85). Bu, kullanıcının en baştan bildirdiği şikâyet. v49'daki 688 soruluk düzeltme bunu **gidermedi**; yalnızca o günkü dedektörün eşiğinin (`en uzun ≥ 1.5 × ikinci`) altına itti — çeldiriciler doğru cevabın hemen altına kadar uzatılınca ölçüt sustu, örüntü kaldı.

2. **Üslup ipucu (yalnız `muhasebe_standartlari`).** Çeldiriciler dolgu kalıbıyla (“…zorunda bulunmaktadır”) şişirilmiş; kalıp doğru şıkta hiç geçmediği için %100 güvenilir bir “yanlış” işareti olmuş. Ayrıca “bu husus standartta düzenlenmemiştir” atma-şıkkı dosya başına 24-33 kez tekrarlanmış, hep yanlış.

## Hedef ve ölçüt

Hedef: her dosyada kör öğrenci **~%20**. Alt ölçüt: doğru şık en-uzun ~%20 **ve** en-kısa ~%20 (yön fark etmez — “en uzunu seç” de “en kısayı seç” de öğrenilebilir bir kuraldır).

Doğru reçete: çeldirici, doğru şıkla **aynı registerde, kısa ve iddialı** — gerçekten savunulabilir ama yanlış bir önerme. Dolgu değil, içerik. Temiz örnek: hesap ağırlıklı dersler (`finansal_muhasebe` %19, `matematik` %17) — şıklar sayı olduğu için boy ipucu doğmuyor.

## Denetim

```
python3 tools/sgs/audit.py content/<ders>/<konu>.json
python3 tools/sgs/audit.py --manifest content/v2/manifest.json
```

Kör öğrenci ≥%35 **FATAL**, ≥%28 UYARI. Boy ipucu ≥%45 UYARI. Regresyon testleri: `python3 tools/sgs/tests/test_audit.py`.

---

## Ek: şablon klonu (2026-07-17, denetime 4 kural eklendikten sonra)

`audit.py` artık kopya/güncellik ailesini de ölçüyor. **Şablon klonu = aynı kök-şık iskeleti VE aynı cevap** — sayılar değişmiş ama sorulan işlem ve sonuç aynı; adayın birini çözünce diğerini tanıdığı sorular.

⚠️ Bu ölçüt alıştırmayı klondan ayırır: aynı şablon + FARKLI cevap **kusur değildir** (matematikte mekanik alıştırma istenen şeydir; 52 denklem sorusu meşrudur). Ayrımı ham cevap kurar.

| dosya | klon |
|---|---:|
| `trend_analizi.json` | 18 |
| `karsilastirmali_analiz.json` | 10 |
| `denetim_riski.json` | 7 |
| `dikey_analiz.json` | 4 |
| `oran_analizi.json` | 3 |
| `nakit_akim_analizi.json` | 3 |
| `maliyet_hacim_kar.json` | 3 |
| `mali_duran_varliklar.json` | 1 |
| `maliyet_hesaplari.json` | 1 |
| `fon_akim_analizi.json` | 1 |
| `safha_maliyeti.json` | 1 |

**Toplam 52 klon / 11 dosya.** Ayrıca 18 yakın-tekrar UYARI'sı (elle karşılaştırılacak).

Bu kurallarda **temiz çıkanlar**: çözüm birebir tekrarı 0, çözüm şablonu 0, mevzuat oranı 0 — içerik bu üç kurala zaten uyuyormuş; kural yazılıydı, yalnız ölçen yoktu.

> ⚠️ Bu sayı bir kez düzeltildi: dedektörün ilk sürümü şablon başına yalnız İLK
> soruyu tutuyordu, bu yüzden ilk soru farklı cevaplıysa sonraki klonlar hiç
> karşılaştırılmıyordu. **20 → 52.** Hatayı denetim değil, düzeltme yamasının kendi
> assertion'ı buldu (`den-risk-gen-0012 ↔ 0026`).
