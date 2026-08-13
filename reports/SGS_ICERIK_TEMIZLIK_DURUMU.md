# SGS içerik kalite temizliği — PROGRAM DURUMU (tüm SGS)

Son güncelleme: 29 Temmuz 2026

> Bu rapor artık yalnız Finansal Muhasebe değil, **manifestteki tüm SGS programının**
> (`content/v2/manifest.json`, programIds=["sgs"]) kalite temizliği ilerleme kaydıdır.
> Yöntem: her ders için kapsam denetimi → soru havuzu denetimi (tüm sorular) → çıkmış
> soru biçim karşılaştırması → düzeltme (idempotent builder / güvenli yama) → zorunlu
> doğrulamalar. Kaynaklar: `tools/sgs/URETIM_KURALLARI.md`,
> `reports/SGS_CIKMIS_SORULAR_ANALIZI_2026-07-22.md`, `~/Desktop/sgs çıkmış sorular/`.

## Genel SGS tamamlanma

**16 ders · 107 konu · 6420 soru.** Tamamlanan: **46 / 107 konu = %43,0**
(finansal_muhasebe 16 ✅ · mali_tablolar_analizi 6 ✅ · maliyet_muhasebesi 6 ✅ · denetim 7 ✅ ·
muhasebe_standartlari 9/18 🔵 · matematik 2 yeni konu ✅).

⚠️ Toplam 104 → **107**: matematikte kapsam açığı kapatılırken iki, muhasebe
standartlarında güncel kapsam tamamlanırken bir yeni konu açıldı. Yeni üretilen konular
hâlihazırdaki kalite standardına göre yazıldığı için tamamlanmış sayılır.
Yaklaşım dersin doğasına göre seçiliyor: sayısal derslerde **harder (çok-adımlı) kalibrasyon**,
kavram ağırlıklı derslerde **profil kalibrasyonu** (olumsuz kök + öncül oranı) ve anlamsal denetim.

| # | Ders | Konu | Tamamlanan | Durum |
|---|---|---:|---:|---|
| 1 | finansal_muhasebe | 16 | 16 | ✅ TAM (ilk anlamsal tur; OTA v166) |
| 2 | mali_tablolar_analizi | 6 | 6 | ✅ İNCELENDİ — SOLİD, 0 değişiklik (aritmetik+kalite doğrulandı) |
| 3 | maliyet_muhasebesi | 6 | 6 | ✅ **TAM** — 6/6 konu harder-kalibrasyondan geçti (builder 6 paket/125 soru); 11 ATIF kusuru giderildi |
| 4 | denetim | 7 | 7 | ✅ **TAM** — 7/7 konu profil kalibrasyonundan geçti (builder 7 paket/149 soru); ders ort. olumsuz %5→**%37**, öncüllü %6→**%11**, kör 25-30→**21-26** |
| 5 | muhasebe_standartlari | 18 | 9 | 🔵 kavramsal_cerceve (20) + tms_1_sunulus (19) sayısal kalibrasyon · tms_21_kur_degisimi (35) kalıp-dolgu+profil · **diger_guncel_standartlar YENİ KONU (60 soru)** · tms_2_stoklar (33) + tms_16_mdv (34) biçim kalibrasyonu · **tms_7_nakit_akis + tms_8_politikalar + tms_38_modv** çıkmış sınav biçim kalibrasyonu (180 soru); 9 konu kaldı |
| 6 | borclar_hukuku | 8 | 0 | ⬜ |
| 7 | ticaret_hukuku | 7 | 0 | ⬜ |
| 8 | meslek_hukuku | 5 | 0 | ⬜ (mesleki_degerler_etik yalnız boy-cilası, v167) |
| 9 | is_ve_sosyal_guvenlik_hukuku | 3 | 0 | ⬜ |
| 10 | vergi_hukuku | 11 | 0 | ⬜ |
| 11 | ekonomi | 3 | 0 | ⬜ |
| 12 | maliye | 3 | 0 | ⬜ |
| 13 | turkce | 3 | 0 | ⬜ (kör %28-30, öncüllü %0 — profil kalibrasyonu bekliyor) |
| 14 | matematik | 5 | 2 | ✅ **KAPSAM AÇIĞI KAPATILDI** — 2 yeni konu / 120 soru (ileri matematik); mevcut 3 konu ölçüldü, zaten temiz (kör %19-21, boy 1/0) |
| 15 | ataturk_ilkeleri | 3 | 0 | ⬜ |
| 16 | yabanci_dil | 3 | 0 | ⬜ |

Canlı OTA: **v174** (tms_16_mdv biçim kalibrasyonu: TL→₺, olumsuz kök %6→%10,
çok adımlı hesap senaryoları, kök kalıbı 43→16).
⚠️ **Sahiplik çakışması (bu turda giderildi):** `tms_7-0049`'un doğru şıkkına
"hiçbir şekilde" pekiştireci geri gelmişti; `fix_lexical_tell.py` bu paketin de sahibi
olduğu için iki builder aynı metne yazıyor ve `--check` çakışıyordu. İfade sadeleştirildi
(olumsuz köklü soruda iddia zaten yanlış olduğundan anlam değişmedi) ve sahip builder'a
gerekçe notu düşüldü. **Ders: aynı pakete iki builder yazmamalı.**

🔎 **Bulgu — tms_7'de üçlü harf run'ı:** 0042-0044 arka arkaya D. §6 "aynı harf üç kez
art arda gelmez" der ama `audit.py::letter_pattern` yalnız sabit adımlı rotasyona bakıyor,
üçlü run'ı görmüyor. Bu run bu turdan ÖNCE de vardı (0042-0044'e hiç dokunulmadı), yani
yeni bir kusur değil. Dedektör açığı + tek soruluk düzeltme ayrı tura bırakıldı.
Önceki: v173 (tms_2_stoklar biçim kalibrasyonu: TL→₺, olumsuz kök %0→%10,
çok adımlı hesap senaryoları, kök kalıbı 38→18).
Önceki: v172 (`diger_guncel_standartlar` yeni konusu — TFRS 5 · TFRS 15 · TMS 41 ·
TFRS 3 · TFRS 13 · TMS 34, 60 soru).
Önceki: v171 (kombine ölçüt açıldı: `audit.py`'nin eleme adımı geniş kümeye
taşındı, eşiği aşan 6 paket daha temizlendi — kurumlar_vergisi %35→%21,
kambiyo_senetleri %33→%23, gelir_vergisi/sozlesme_turleri/haksiz_rekabet/
kiymetli_evrak %31→%20-25. **Havuzda ≤%30 hedefini aşan paket kalmadı.**)
Önceki: v170 (kalıp-dolgu sözcük tell'i: 71 paket mekanik + 11 paket elle denge +
tms_21 profil kalibrasyonu). Önceki: v169 (matematik
2 yeni ileri konu + kavramsal_cerceve/tms_1_sunulus), commit `6693b85`, uygulama
reposu `278ac08`.
⚠️ Yeni matematik konularının telefonda görünmesi için ayrıca **yeni binary** gerekir
(curriculum OTA'dan inmez); OTA yalnız kazanım/soru paketlerini taşır.

## Açık mimari kararı (kullanıcıya)

Manifestte **ayrı bölüm/karma/deneme soru havuzu YOK** — paketler yalnız konu bazlı
(`{ders, konu, file}`); Karışık Test ve Tam Deneme, konu havuzlarından **dinamik**
derleniyor (`lib/features/quiz`, `deneme`). Talimatın "konu testi ile bölüm/karma test
aynı havuzu paylaşmamalı" şartı bu mimaride **veri olarak zaten yok** (bölüm havuzu
mevcut değil); ayrı bölüm havuzu üretmek her ders için ek özgün soru = büyük genişleme
ve app tarafı değişikliği gerektirir. **Karar kullanıcıya bırakıldı.**

---

## Ders 1 — Finansal Muhasebe: 16/16 ✅ TAM

İlk anlamsal temizlik turu tamamlandı (bakım builder
`build_financial_accounting_semantic_cleanup.py`, **16 paket / 356 soru**). Son iki
konu bu turda: **Kur Farkları 26** + **KDV Muhasebesi 30** revizyon; iade kuralı
(satış iadesi→391, alış iadesi→191) pekiştirildi; cevap dağılımları doğallaştırıldı.
Denetlenen 960 soru; değiştirilen 356; korunan 604. Kaynak: TDHP/MSUGT, VUK, 3065 KDVK
(madde düzeyi), 2024-2026 çıkmış soru kalibrasyonu. Testler: SGS+SMMM audit FATAL0/UYARI0,
29 audit regresyon, 85 flutter testi — hepsi geçti. **OTA v166 canlı.**

Not — şık örüntüsü/boy: SGS havuzunun tamamı ≤%30 kör hedefinde (0 UYARI). Ayrıntı +
tekrar-dolgu tell bulgusu (432 çeldirici/20 dosya, naif kaldırma tuzağı, ertelendi):
`tools/sgs/SIK_ORUNTUSU_RAPORU.md`.

## Ders 2 — Mali Tablolar Analizi: 6/6 ✅ İNCELENDİ (SOLİD, 0 değişiklik)

Kapsam denetimi: 6 konu (dikey · karşılaştırmalı/yatay · trend · oran · nakit akım ·
fon akım) resmî mali analiz teknikleriyle tam örtüşüyor; eksik/fazla/yanlış-konumlu konu
yok. Denetlenen 360 soru · değiştirilen **0** · korunan 360.

Doğrulama: 6/6 FATAL0/UYARI0; klon 0; şık-çakışması 0; boş-cevap/"ilgili mevzuata göre"
0; demo 0; harf-atfı 0. **Aritmetik:** trend (32/32), dikey, karşılaştırmalı (yüzde
değişim `(fark/baz)×100` — negatifler dâhil doğru), oran — sayısal sorular bağımsız
formülle doğrulandı, hata yok. Çıplak kökler (fon/nakit/oran'da 6 adet: "hangisi fon
kaynağı DEĞİLDİR", "cari oran nasıl hesaplanır" vb.) §4 kapsamında meşru — ayırt edici
içerik şıklarda. Boy/kör rakamları (trend %30 vb.) **sayısal artefakt** (şıklar 1 karakter
farkla eşit-uzunlukta sayı; §5 gereği sömürülemez), gerçek kusur değil. Not: karşılaştırmalı
0053/55/56/58 çözümlerinde ara "Değişim=" değeri eksi işaretsiz yazılmış (sonuç doğru) —
notasyon nüansı, düzeltme gerektirmez.

Sonuç: ders zaten yüksek kaliteli; direktif gereği güçlü sorular **korundu**.

## Ders 3 — Maliyet Muhasebesi: 6/6 ✅ İNCELENDİ (doğru/temiz; ⚠️kalibrasyon açık)

Kapsam: 6 konu (birleşik maliyet · gider dağıtımı · maliyet-hacim-kâr · safha · sipariş ·
standart maliyet) — resmî maliyet muhasebesi kapsamıyla örtüşüyor, eksik/fazla yok.
Denetlenen 360 soru: 6/6 FATAL0/UYARI0; klon/boş/demo/harf/dup 0. **Aritmetik: her konudan
hesaplı örnekler bağımsız doğrulandı — hepsi doğru** (dağıtım oranları, katkı payı/başabaş/
güvenlik marjı, safha eşdeğer ürün, sipariş DİMM+DİG+GÜG, standart sapma yön+tutar). Çözümler
adım-adım, doğru formül, ₺/aleyhte-lehte etiketli, kontrol satırlı.

⚠️ **KALİBRASYON BULGUSU (program-düzeyi karar):** sorular **tek-adımlı ve kısa**
(ör. 120.000 × 0,5 = 60.000). Oysa çıkmış analizine göre gerçek SGS maliyet soruları
**medyan 482 karakter, çok-adımlı senaryo** (%100 sayısal). Yani doğru/temiz ama **gerçek
sınavın altında zorlukta** — [[harder-question-calibration]] (baba "biraz basit" dedi) +
direktifin "aşırı kolay" maddesiyle örtüşür. Aynı durum mali_tablolar ve diğer sayısal
dersler için de olası. Harder-kalibrasyon = büyük yeniden-üretim; mevcut sorular doğru/
kullanılabilir olduğundan bu bir **iyileştirme kararı** (kusur değil).

**KARAR (kullanıcı): tüm sayısal derslere harder (çok-adımlı) tur.** İlk pilot tamamlandı:
`maliyet_hacim_kar` — 21 tek-adımlı hesap, ham veriden (fiyat/değişken/sabit) başlayıp
katkı payı → başabaş/hedef kâr/güvenlik marjı/faaliyet kaldıracı/vergili hedef/duyarlılık
zinciri kuran **çok adımlı** senaryolara çevrildi (kavram+öncüllü korundu; kök medyanı ~65→120).
Klon/near-dup üretmemek için 15+ farklı arketip + ters-hesap kullanıldı; aritmetik bağımsız
doğrulandı; cevap dağılımı A12 B13 C11 D12 E12. İdempotent builder:
`tools/sgs/builders/build_cost_accounting_harder_calibration.py` (--check temiz).
FATAL0/UYARI0, iki repo eşit, flutter content_quality geçti.

**birlesik_maliyet (18 soru)** — aynı yöntem: satış değeri (qty×fiyat) → dağıt → birim/brüt kâr ·
NGD (nihai satış − ilave işleme) → dağıt · yan ürün net maliyet → birim · ilave işleme kararı
(incremental) · iki yöntem karşılaştırma (fark) · ters-hesap (pay → birleşik maliyet). Ayrıca
aynı veri setini A/B/C için ayrı ayrı soran tekrar (0021-23, 0026-28) giderildi. Kör %23,
dağılım A11 B12 C12 D13 E12, tekrar 0, kök medyanı ~90→121.

**gider_dagitimi (19 soru)** — I. + II. dağıtım zinciri (esas yerin toplam GÜG'ü) · kademeli
(basamaklı) dağıtım · doğrudan (basit) yöntem · yükleme oranı (makine saati / DİG esaslı) ·
mamule yükleme → toplam/birim maliyet · kapasite (bütçelenen oran × fiili saat) · iki anahtar
karşılaştırma (alan vs işçi) · oranlı (3:2:1) dağıtım + birim · ters-hesaplar. Tekrarlı veri
setleri (0009/0010, 0024/0025, 0050/0051/0052) giderildi. Kör %22, dağılım A10 B12 C13 D12 E13,
tekrar 0, kök medyanı ~95→146.

**safha_maliyeti (23 soru)** — burada **gerçek bir kusur** da giderildi: 9 soru önceki soruya
atıf yapıyordu ("Önceki soruda…", "Aynı safhada…", "Yukarıdaki üretimde…"). Uygulama konu
testlerini 20'şer böldüğü ve Karışık Test'te sırayı karıştırdığı için bu atıflar kullanıcıda
**bağlamsız** görünüyordu (§4: çözüm için gereken tüm veri kökte olmalı). Dokuzu da kendi
kendine yeterli çok-adımlı soruya dönüştürüldü (kalan atıf: **0**). Arketipler: eşdeğer ürün →
eşdeğer birim maliyet → tamamlanan/dönem sonu yarı mamul maliyeti · iki maliyet unsuru ayrı
eşdeğer (DİMM %100 / dönüştürme kısmi) → tam birim maliyet · maliyet dağıtım kontrolü ·
normal fire (sağlama yüklenir) ve anormal fire (zarar yazılır) · safhalar arası devir ·
ters-hesaplar (tamamlanma derecesi, toplam maliyet). Kör %22, dağılım A12 B12 C12 D11 E13,
tekrar 0, kök medyanı ~110→**178**.

**siparis_maliyeti (20 soru)** — tekrarlı veri setleri (0008/0009, 0010/0011, 0023/0024,
0038/0039, 0045/0046, 0050/0051 aynı siparişi iki kez soruyordu) giderildi. Arketipler: yükleme
oranı türetme (tahmini GÜG ÷ makine saati / DİS / DİG tutarı) → siparişe yükleme → toplam/birim ·
**yükleme farkı** (fazla/eksik yüklenmiş GÜG) ve satılan mamul maliyeti düzeltmesi · dönüştürme
(DİG+GÜG) ile birincil (DİMM+DİG) maliyet ayrımı ve farkı · satış brüt kârı / dönem sonu stok
değeri · kâr marjıyla fiyat · tamamlanan (152 MAMULLER) vs devam eden (151 YARI MAMULLER) ·
ters-hesaplar (toplamdan GÜG → makine saati; fazla yüklemeden fiili saat). Kör %26, dağılım
A12 B13 C11 D13 E11, tekrar 0, kök medyanı ~105→**169**.

**standart_maliyet (24 yama)** — 2 ATIF kusuru (0012, 0016 "Yukarıdaki üretimde…") giderildi ve
tekrarlı veri setleri (0023/0024/0025, 0032/0033, 0043/0044/0045, 0052/0053) ayrıştırıldı. Sorular
artık ham veriden (üretim adedi + birim standart + standart fiyat + fiili miktar + fiili fiyat)
başlıyor; standart miktar → fiyat/miktar (veya ücret/süre) sapması → toplam sapma zinciri ve
**yön (lehte/aleyhte)** birlikte ölçülüyor. Çeldiriciler tipik hatalardan üretildi: fiyat
sapmasında standart miktar kullanmak, miktar sapmasında fiili fiyat kullanmak. Ayrıca GÜG toplam
sapması ve ters-hesaplar (fiili fiyat, fiili süre, birim standart miktar) eklendi. 24. yama
**yalnız harf permütasyonu**: baseline'da mevcut olan 0019-0020-0021 üçlü "E" run'ı (§6 ihlali)
içerik değiştirilmeden giderildi. Kör %20, dağılım A12 B12 C13 D12 E11, tekrar 0, atıf 0.

Builder: **6 paket / 125 soru** (`--check` temiz, idempotent). Her batch sonrası paket audit,
SGS tam havuz, test_audit, manifest_merge, iki repo `cmp`, `git diff --check` ve flutter
content_quality **geçti**.

### Ders 3 kapanış doğrulaması (6/6 konu · 125 revizyon)

Denetlenen 360 soru · değiştirilen **125** · korunan 235 (kavram + öncüllü sorular). Toplam
**11 ATIF kusuru** giderildi (safha 9 + standart 2). Çalıştırılan kontroller ve sonuçları:
builder `--check` 6 paket/125 ✓ · 6 paketin tek tek audit'i FATAL 0/UYARI 0 ✓ · SGS tam havuz
FATAL 0/UYARI 0 ✓ · audit regresyon 29 test OK ✓ · `manifest_merge --check` uyumlu (201 paket,
sürüm 167 — değişmedi) ✓ · `check_scope --program sgs` temiz ✓ · 6 konuda iki repo `cmp` birebir
eşit ✓ · `git diff --check` iki repoda temiz ✓ · flutter `content_quality_test` geçti ✓ ·
**flutter tam paket 85 test geçti** ✓.

Kaynak: 1 Sıra No'lu MSUGT / TDHP maliyet hesapları (7/A), maliyet muhasebesi standart
teknikleri (başabaş-katkı payı, birleşik maliyet dağıtımı, gider dağıtımı I./II. dağıtım, safha
eşdeğer ürün, sipariş maliyet kartı, standart maliyet sapma analizi), 2024-2026 SGS çıkmış soru
biçim kalibrasyonu (`reports/SGS_CIKMIS_SORULAR_ANALIZI_2026-07-22.md`).

Sayısal derslerde kalan harder işi: mali_tablolar_analizi ve finansal_muhasebe hesap soruları
(ikisi de doğruluk açısından temiz; zorluk turu ileride değerlendirilecek).

## Ders 4 — Denetim: 1/7 🔵 PROFİL KALİBRASYONU

Kapsam denetimi: 7 konu (denetim kavramı · standartlar-etik · iç kontrol · denetim kanıtı ·
denetim riski · denetim raporu · örnekleme) resmî denetim müfredatıyla örtüşüyor; eksik/fazla
konu yok. Triyaj: 7/7 paket FATAL 0/UYARI 0, klon 0, harf atfı 0, gerçek ATIF kusuru 0
("aynı denetimde" ifadeleri yanlış pozitif çıktı).

⚠️ **Ölçülen profil sapması (bu dersin asıl kusuru):** 2026 SGS denetim bloğunda **olumsuz kök
%46,9** ve **öncüllü %12,5** iken bizim paketlerde olumsuz kök yalnız **%1-8**, öncüllü **%5-8**.
Yani havuz gerçek sınavın en belirgin biçim özelliğini taşımıyordu. §2 bu oranların "katı kota
değil kalibrasyon bandı" olduğunu belirttiği için hedef mekanik olarak %47 değil, **anlamlı
yaklaşma** olarak belirlendi.

**denetim_kavrami (20 yama)** — 17 soru olumsuz köke (4 doğru ifade + 1 yanlış ifade) ve 3 soru
öncüllü yapıya dönüştürüldü. Sonuç: olumsuz kök **%8 → %36**, öncüllü **%5 → %10**, kör öğrenci
**%28 → %25** (iyileşti), boy 3/14 → 20/12 (dengelendi), dağılım A13 B10 C12 D12 E13, tekrar 0.
Öncül dağılımı denetimi **0 uyarı**: kombinasyonlar çeşitli (I ve III ×2, I ve II ×2, II ve III,
Yalnız II) ve **"Yalnız X" bir soruda doğru** — bu, havuzun bilinen "Yalnız X hiç doğru değil"
kusurunu bu pakette gideriyor. İçerik dayanağı: denetim tanımı/unsurları, makul güvence ve
sınırları, tür sınıflandırmaları (konu/statü), KGK yetkilendirmesi, iç ↔ bağımsız denetim ayrımı,
mesleki şüphecilik, hata ↔ hile, 3E. İdempotent builder:
`tools/sgs/builders/build_audit_profile_calibration.py` (`--check` temiz).

**denetim_standartlari_etik (21 yama)** — 18 olumsuz kök + 3 öncüllü. Sonuç: olumsuz kök
**%7 → %38**, öncüllü **%7 → %11**, kör öğrenci **%28 → %21**, boy 5/25 → 18/15 (dengelendi),
dağılım A14 B13 C14 D9 E10, tekrar 0, öncül uyarısı **0** ("Yalnız II" doğru olan soru eklendi).
İçerik dayanağı: BDS'nin KGK tarafından yayımlanması ve ISA uyumu, genel kabul görmüş
standartların üç grubu (genel / çalışma alanı / raporlama) ve gruplar arası karışıklığın
ölçülmesi, meslek etiğinin beş temel ilkesi (dürüstlük, tarafsızlık, mesleki yeterlik ve özen,
gizlilik, mesleki davranış), gizliliğin istisnaları, bağımsızlığa yönelik beş tehdit ve
önlemlerin "kabul edilebilir düzey" mantığı, denetçi rotasyonu, şarta bağlı ücret yasağı, kalite
kontrol sistemi ve mesleki muhakemenin sınırları.

**ic_kontrol (21 yama)** — 17 olumsuz kök + 4 öncüllü. Sonuç: olumsuz kök **%10 → %38**, öncüllü
**%5 → %11**, kör öğrenci **%30 → %22**, boy 8/29 → 15/13, dağılım A9 B14 C10 D13 E14, tekrar 0,
öncül uyarısı 0 ("Yalnız II" doğru). İçerik dayanağı: COSO'nun beş bileşeni ve **bileşenler arası
karışıklığın ölçülmesi** (kontrol ortamı ↔ kontrol faaliyeti; banka mutabakatı bir kontrol
faaliyetidir, kontrol ortamı unsuru değil), iç kontrolün üç amacı, doğal kısıtlar (insan hatası,
muvazaa, yönetimin kontrolleri aşması, maliyet-fayda), görevler ayrılığı ve muvazaa karşısındaki
sınırı, önleyici ↔ ortaya çıkarıcı kontroller, **kontrol riskinin işletmeye ait olması** (denetçi
doğrudan azaltamaz; tespit riskini yönetir), kontrol testi ↔ maddi doğrulama testi ayrımı,
tone at the top.

**denetim_kaniti (23 yama)** — 20 olumsuz kök + 3 öncüllü. Sonuç: olumsuz kök **%5 → %38**,
öncüllü **%6 → %11**, kör öğrenci **%30 → %21**, boy 30/26 → 18/16 (havuzun en dengesiz dosyasıydı),
tekrar 0, öncül uyarısı 0 ("Yalnız I" doğru). İçerik dayanağı: yeterlilik (miktar) ↔ uygunluk
(ilgililik + güvenilirlik) ayrımı ve **miktarın kaliteyi telafi etmemesi**, güvenilirlik hiyerarşisi
(dış kaynak > iç, asıl > fotokopi, yazılı > sözlü, iç kontrol zayıfsa iç belge de zayıf), sekiz
teknik, **fiziki sayımın mevcudiyet için güçlü / tamlık için zayıf olması**, kontrol testi ↔ maddi
doğrulama, pozitif ↔ negatif teyit (yanıt gelmemesi doğrulama değildir), analitik prosedürde
sapmanın sonuç değil araştırma gerekçesi olması, yönetim beyan mektubunun tek başına yetmemesi,
uzman kullanımında sorumluluğun denetçide kalması.

⚠️ **Bu batch'te yakalanan hata (§5 dersi):** ilk denemede olumsuz köklü soruların "yanlış ifade"
şıkkını gerekçe ekleyerek yazdığım için doğru şık sistematik olarak **en uzun** kaldı; kör öğrenci
%30'dan **%31'e yükseldi** (UYARI eşiği). Düzeltme padding değil **sadeleştirme** oldu: 6 sorudaki
yanlış ifade kısaltılıp diğer şıklarla eş boya getirildi → kör %21, boy 18/16. Ders: olumsuz kök
üretirken yanlış ifadeyi "açıklayarak" yazmak boy tell'i doğurur; yanlışlık kısa ve iddialı olmalı.

**denetim_riski (24 yama)** — 20 olumsuz kök + 4 öncüllü. Sonuç: olumsuz kök **%5 → %38**, öncüllü
**%5 → %11**, kör öğrenci **%30 → %21**, boy 28/14 → **13/11** (iki yönde de düşük), tekrar 0,
öncül uyarısı 0. Ek kazanım: dosyada **~15 soru aynı iki formülü** (kabul edilebilir tespit riski /
toplam denetim riski) tekrarlıyordu; bunların bir kısmı kavramsal-öncüllü yapıya çevrilerek tekrar
azaltıldı, hesap soruları öğretici çekirdek olarak korundu. İçerik dayanağı: DR = YR × KR × TR ve
ÖYR = YR × KR ilişkisi, **hangi bileşenin kime ait olduğu** (yapısal ve kontrol riski işletmeye,
tespit riski denetçiye), risk ↔ kanıt ters ilişkisi, önemliliğin nicel/nitel boyutu, performans
önemliliğinin daha düşük belirlenmesi, önemlilik ↔ kanıt ters ilişkisi, riskin sıfırlanamaması.

⚠️ **İkinci §5 dersi (yön değiştiren tell):** denetim_kaniti'ndeki hatadan sonra bu dosyada yanlış
ifadeleri baştan kısa yazdım — bu kez doğru şık sistematik olarak **en kısa** oldu (boy 13/26, kör
%28; tell yön değiştirdi). Çözüm ne uzatma ne kısaltma; **orta boy**: 8 ifade ikinci en kısa ile
üçüncü arasına getirildi → boy 13/11, kör %21. §5'in "yön önemsizdir" uyarısı bu iki turda pratik
olarak doğrulandı; artık tasarım betiğine "doğru şık tek-en-uzun mu?" ön kontrolü eklendi.

**denetim_raporu (19 yama)** — 16 olumsuz kök + 3 öncüllü. Sonuç: olumsuz kök **%11 → %36**,
öncüllü **%6 → %11**, kör öğrenci %25 (baseline düzeyinde korundu), boy 0/23 → **7/11**, tekrar 0,
öncül uyarısı 0. Seçim, **v167 boy-cilasında değiştirilen 17 soruya dokunmadan** yapıldı (çakışma
önlendi). İçerik dayanağı: BDS 700-706 rapor unsurları, dört görüş türü ve **önemlilik × yaygınlık
matrisi** (yanlışlık → şartlı/olumsuz; kanıt sınırlaması → şartlı/kaçınma), dikkat çekme ↔ diğer
husus paragrafı, kilit denetim konularının ayrı görüş olmaması, rapor tarihi kuralları, yönetim ↔
denetçi sorumluluk ayrımı.

⚠️ **Üçüncü §5 dersi (orta-boy tuzağı):** önceki iki dosyanın dersiyle tüm yanlış ifadeleri orta
boya getirince bu kez **"iki ucu ele, ortadan tahmin et"** stratejisi güçlendi (18 yamanın doğru
şıkkı ortada kaldı → kör %28). Doğru çözüm tekdüzelik değil **dağılım**: 4 soruda doğru şık en
uzun, 4 soruda en kısa, kalanı ortada olacak biçimde yeniden yazıldı → boy 7/11, kör %25. §5'in
"doğru cevabın uzunluk sırası paket boyunca farklı konumlara dağılır" ilkesi bu turda ölçülerek
doğrulandı.

**denetim_ornekleme (21 yama)** — 19 olumsuz kök + 2 öncüllü. Sonuç: olumsuz kök **%5 → %36**,
öncüllü **%8 → %11**, kör öğrenci **%30 → %26**, boy 29/29 → **24/22**, tekrar 0, öncül uyarısı 0.
Boy dağılımı bu kez **baştan planlandı** (3 en uzun / 3 en kısa / 15 orta) ve korunan 39 sorunun
taşıdığı baseline dengesizliği yamalarla telafi edildi. İçerik dayanağı: örnekleme riski ↔
örnekleme dışı risk ayrımı, istatistiki ↔ takdiri örnekleme, seçim yöntemleri ve temsil gücü,
örneklem büyüklüğü etkenleri, tolere edilebilir oran ↔ örneklem hata oranı, nitelik ↔ değişken
örneklemesi, parasal birim örneklemesi, çalışma kâğıtlarının mülkiyeti/gizliliği/saklanması,
sürekli ↔ cari dosya, dokümantasyonun yeterlilik ölçütü.

### Ders 4 kapanış doğrulaması (7/7 konu · 149 revizyon)

Denetlenen 420 soru · değiştirilen **149** · korunan 271. Ders ortalaması: olumsuz kök **%5 → %37**
(2026 sınavı %46,9 bandına anlamlı yaklaşma), öncüllü **%6 → %11** (%12,5), kör öğrenci **25-30 →
21-26** (yani kalibrasyon kör öğrenciyi kötüleştirmeden yapıldı, çoğu dosyada iyileştirdi).
Çalıştırılan kontroller: builder `--check` 7 paket/149 ✓ · 7 paketin tek tek audit'i FATAL 0/UYARI 0 ✓ ·
SGS tam havuz FATAL 0/UYARI 0 ✓ · audit regresyon 29 test OK ✓ · `manifest_merge --check` uyumlu
(201 paket, sürüm 167 değişmedi) ✓ · `check_scope --program sgs` temiz ✓ · 7 konuda iki repo `cmp`
birebir eşit ✓ · `git diff --check` iki repoda temiz ✓ · flutter `content_quality_test` geçti ✓ ·
**flutter tam paket 85 test geçti** ✓.

Kaynak: BDS/ISA seti (denetim standartlarının üç grubu, BDS 700-706 raporlama), meslek etiği beş
temel ilke ve bağımsızlık tehditleri, COSO iç kontrol çerçevesi, denetim riski modeli ve önemlilik,
denetim kanıtı ve teknikleri, örnekleme ile dokümantasyon; biçim kalibrasyonu için
`reports/SGS_CIKMIS_SORULAR_ANALIZI_2026-07-22.md`.

## Ders 5 — Muhasebe Standartları: 1/17 🔵 SAYISAL KALİBRASYON

Kapsam denetimi: 17 konu (kavramsal çerçeve + 16 TMS/TFRS) mekanik olarak temiz — 17/17 paket
FATAL 0/UYARI 0, klon 0, kör %20-30.

⚠️ **Ölçülen profil sapması (bu dersin asıl kusuru, denetimdekinden farklı):**

| Ölçüt | Havuzda | 2026 SGS (FM + standartlar bloğu) |
|---|---:|---:|
| Sayısal senaryo | **%6** | **%57,7** |
| Öncüllü | %15 | %3,8 |
| Olumsuz kök | %0 | %9,6 |
| Medyan kök | ~105 | 295 |

Yani bu derste kusur **hesap/uygulama eksikliğidir**: gerçek sınavda standart soruları ağırlıklı
olarak sayısal uygulama iken havuz neredeyse tümüyle tanım/kavram sorusundan oluşuyor. Bu nedenle
denetimdeki "olumsuz kök" reçetesi değil, **sayısal senaryo kalibrasyonu** uygulanıyor: kavram
soruları, standardın hükmünü **uygulatan** hesap senaryolarına çevriliyor ve öncül oranı düşürülüyor.

**kavramsal_cerceve (20 yama)** — 16 kavram sorusu sayısal senaryoya, 4 öncüllü soru tekil yapıya
çevrildi. Sonuç: sayısal senaryo **%0 → %30**, öncüllü **%16 → %10**, medyan kök 82 → 100,
kör öğrenci %22 (korundu), boy 20/16 → **14/12**, tekrar 0. Sayısal alanlar konunun **gerçek
uygulama alanlarından** seçildi (zorlama yapılmadı): sermayenin korunması (finansal ↔ fiziki kâr
farkı ve 2.000 ₺'lik özkaynak düzeltmesi), dört ölçüm esasının aynı varlık üzerinde ayrıştırılması
(tarihi maliyet / gerçeğe uygun değer — işlem maliyeti düşülmez / kullanım değeri — işletmeye özgü /
cari maliyet — giriş fiyatı + işlem maliyeti), özkaynak = varlık − borç, gelir-gider tanımından
dönem kârı (ortak katkı ve dağıtımları düzeltilerek), 2018 Çerçevesi'nin **olasılık eşiği içermeyen**
muhasebeleştirme ölçütü, kontrol kaybında tablo dışı bırakma ve kazanç, netleştirme yasağı.
Konunun doğası gereği %57,7 hedeflenmedi; hedef anlamlı yaklaşmaydı. İdempotent builder:
`tools/sgs/builders/build_standards_numeric_calibration.py` (`--check` temiz).

**tms_1_sunulus (19 yama)** — 12 kavram sorusu sayısal senaryoya, 6 öncüllü soru tekil yapıya
çevrildi; ayrıca öncül dağılımı uyarısını gidermek için 1 öncüllü soru **"Yalnız X" doğru** olacak
biçimde yeniden yazıldı. Sonuç: sayısal senaryo **%0 → %21**, öncüllü **%20 → %10** (havuzun en
yüksek öncül oranıydı), medyan kök 88 → 116, kör öğrenci %21 (korundu), boy 18/12 → **16/11**,
tekrar 0, öncül uyarısı **0**. Sayısal alanlar TMS 1'in gerçek uygulama noktalarından seçildi:
dönen varlık ve **kısa vadeli yükümlülük toplamı** (uzun vadeli kredinin **cari taksiti** kısa
vadeye alınır — klasik tuzak), 18 aylık **faaliyet döngüsünde** 12 ayı aşan stokun dönen sayılması,
**ertelenmiş verginin dönen olarak sınıflandırılamaması**, toplam kapsamlı gelir, DKG'nin
**yeniden sınıflandırılacak ↔ sınıflandırılmayacak** ayrımı, işlev esaslı sunumdan faaliyet kârı
(finansman gideri hariç), kâr/zararın **ana ortaklık ↔ kontrol gücü olmayan paylar** dağılımı,
özkaynak değişim tablosundan dönem sonu özkaynak, netleştirme yasağı ↔ hasılattan iade düşülmesi.

⚠️ **Ölçüt notu:** "sayısal" oranı, cevabı rakam içeren soruları sayan dar bir ölçüttür. Kökünde
en az iki ₺ tutarı bulunan (yani öğrenciye gerçek hesap yaptıran) soru oranı kavramsal_cerceve'de
**%30**, tms_1_sunulus'ta **%21**'dir; cevabı kavramsal ifade olan uygulama soruları bu sayıma
girmez. Raporlanan oranlar bu nedenle gerçek uygulama ağırlığının alt sınırıdır.

**Sonraki konu:** `tms_21_kur_degisimi` (sayısal %0, kör %30).

Not — kullanılan teknik dersler: (1) öncüllü sorularda seçenek metni kombinasyon olduğu için
harf permütasyonu yapılmaz, hedef harf tasarımda sabitlenir; (2) kombinasyon tespitinde
`startswith("Yalnız")` kırılgandır — "**Yalnızca** büro içi…" gibi normal şıkları yanlış pozitif
yakalar, tam-eşleşen regex gerekir; (3) **§5 boy dengesi üç turda öğrenildi:** yanlış ifadeyi
gerekçesiyle yazmak → "en uzunu seç" tell'i; hepsini kısaltmak → "en kısayı seç" tell'i; hepsini
ortalamak → "iki ucu ele, ortadan tahmin et" tell'i. Doğru yaklaşım **dağılımdır** (bir kısmı uzun,
bir kısmı kısa, kalanı orta) ve tasarım betiğine "doğru şık tek-en-uzun/tek-en-kısa mı?" ön kontrolü
eklenmelidir.

### tms_7_nakit_akis + tms_8_politikalar + tms_38_modv — üçlü biçim kalibrasyonu

Üç paketin kapsamı çıkmış sınavlarla örtüşüyordu; güçlü sorular ve kazanım dağılımı
korundu. Temel kusur, eski üreticilerin aynı `... bakımından aşağıdakilerden hangisi
doğrudur?` kökünü seri hâlde kullanması ve bütün çözümleri mekanik `Doğru cevap X.`
cümlesiyle bitirmesiydi. 2014-2026 arşivi ve KGK TFRS 2026 Seti yeniden kontrol edildi.

| ölçüm | TMS 7 | TMS 8 | TMS 38 |
|---|---:|---:|---:|
| tekrarlı kök kalıbı | 43→**10** | 40→**14** | 41→**9** |
| olumsuz kök | 1→**6** | 3→**6** | 3→**7** |
| `TL` kullanan soru | 7→**0** | 5→**0** | 5→**0** |
| mekanik çözüm sonu | 60→**0** | 60→**0** | 60→**0** |
| kör öğrenci | %21→**%23** | %26→**%25** | %23→**%21** |

**TMS 7:** yatırım/esas/finansman sınıflandırması, nakit yaratmayan işlemler, yabancı
para nakit üzerindeki kur etkisi, doğrudan yöntem ve kısıtlı nakit açıklamaları için beş
özgün olumsuz/uygulamalı soru yenilendi. **TMS 8:** politika değişikliğinin meşru
nedenleri, yürürlüğe girmemiş standart ve geçmiş dönem hatasının düzeltilmesi üç özgün
uygulama sorusuyla güçlendirildi. **TMS 38:** tanım, araştırma-geliştirme ayrımı,
hasılata dayalı itfa, maliyet modeliyle defter değeri ve zorunlu açıklamalar beş özgün
uygulama sorusuyla kalibre edildi.

Toplam 86 kök ve 13 tam soru kalibrasyonu; 180 çözüm sonu temizliği. Builder:
`build_std_tms7_tms8_tms38_kalibrasyon.py`. Builderdan bağımsız 17 aritmetik kontrol,
204 paketlik havuzda FATAL0/UYARI0, 31 audit regresyonu, 86 Flutter testi ve iki repo
eşitliği doğrulandı.


### tms_21_kur_degisimi (35 yama) — kalıp-dolgu temizliği + profil

⚠️ **Bu konuda sayısal oran ARTIRILMADI.** Kural §1'in TMS 21 notu ("Hesap sorusu değil")
2014-2026 arşivinin 11 dosyasında doğrulandı: TMS 21 hesap sorusu olarak **hiç sorulmamış**.
Ölçülen yük merkezleri: geçerli para birimi tespiti (2024 s.50 + 2025 s.53, **ikisi de olumsuz
kök**), öncüllü faktör listesi (2021, 2025 s.48), parasal ↔ parasal olmayan ayrımı ve hangi kur
(2016-18 s.40/41/44, şıklar KISA kalem adları), yüksek enflasyon (2023 s.50), kur farkının
sunumu (2016-18 s.43). Mevcut 8 hesap sorusu öğretici olduğu için korundu, üzerine eklenmedi.

**🔴 YENİ KUSUR SINIFI — kalıp-dolgu sözcük tell'i (audit görmüyor).** 34 soruda 81 çeldirici
şu kalıplarla şişirilmişti ve bu ifadeler **doğru şıkta hiç geçmiyordu**:

| işaret | çeldiricide | doğru şıkta |
|---|---:|---:|
| `zorunda` | 39 | **0** |
| `Her hâlde` | 31 | **0** |
| `…bir ölçümü ifade eder / karşılar` | 29 | **0** |
| `hiçbir` | 25 | **0** |
| `niteliğinde` | 12 | **0** |

Kör öğrenci bu işaretleri taşıyan şıkları eleyip kalanlardan seçtiğinde isabet **%34**'e çıkıyordu
(rastgele %20). Ölçek dürüstçe: bu, `audit.py::kor_ogrenci`'nin ölçtüğü boy tell'inden (%30)
**güçlü değil, aynı mertebede** — ama audit bunu hiç görmüyor. Havuz taraması: 106 SGS
paketinin **8'i ≥%30** (tms_37 %34 · tms_21 %34 · tfrs_9 %34 · tms_40 %33 · tms_12 %31 ·
limited_sahis_sirketleri %30 · tms_20 %30 · tfrs_16 %30), havuz ortalaması %23,
muhasebe_standartlari ortalaması %28. **Bu ders bu kalıpla üretilmiş.**

**Uygulanan reçete** — dolgu silinmedi, §5'in ertelenmiş talimatı uygulandı: uygun boyutta
**gerçek içerikle değiştirildi**. Parasal/parasal olmayan sorularında beş şık da kısa kalem adına
indirildi (2016-18 üslubu); "hangi kur" sorularında beş şık da somut kur adı oldu; 3 kök olumsuza
çevrildi (0017, 0022, 0036 — 4 doğru + 1 yanlış ifade).

⚠️ **§5 tuzağı yine devreye girdi ve raporun kendi reçetesiyle çözüldü.** Dolgu temizliği ilk
turda eleme tell'ini %34→%20'ye indirdi **ama kör'ü %30→%43'e fırlattı** ("en uzunu seç", boy
48/50): çeldiriciler kısa gerçek iddialara inince doğru şık sistematik en uzun kaldı. Düzeltme
doğru şıkkı kısaltmak değil, **14 soruda çeldiricilere gerçek içerik eklemek** oldu (yanlış iddianın
sonuç cümlesi — soruyu da zorlaştırır). Sonuç:

| Ölçüm | Önce | Sonra |
|---|---:|---:|
| Kör öğrenci (audit) | %30 "en kısayı seç" | **%23** |
| Eleme stratejisi (sözcük tell'i) | %34 | **%20** (rastgele düzeyi) |
| Boy eğilimi (uzun/kısa, n=50) | 14 / 32 | **24 / 24** |
| Olumsuz kök | %16 | **%21** |
| Harf dağılımı | A12 B11 C12 D9 E16 | **12/12/12/12/12** |
| Kalıp-dolgulu çeldirici | 81 | **0** |

Olumsuz kök %33'e değil %21'e çekildi: ders bandı %9,6 (FM+standartlar), TMS 21 ise olumsuza
yatkın. İki gerçek veri noktası üzerine %33'e çıkmak bandı aşırı döndürmek olurdu; %21 ikisinin
arasında kalıyor. Öncüllü %16 ve sayısal %18 bilerek değiştirilmedi (arşivle uyumlu).
Builder: `build_standards_profile_calibration.py` (1 paket / 35 soru, `--check` temiz).

### tms_16_mdv (34 yama) — biçim kalibrasyonu

TMS 16, arşivde 7 dosya / 16 geçişle ikinci en sık standart. **Kapsam yine tamdı**;
kusur tms_2'dekiyle aynı ailedendi ama daha belirgindi.

| ölçüm | önce | sonra |
|---|---:|---:|
| kökünde ≥2 tutar | %0 | **%11** |
| aynı kök kalıbı | 43/60 | **16/60** |
| `TL` kullanan soru | 8 | **0** |
| olumsuz kök | %6 | **%10** |
| kör öğrenci | %28 | **%25** |

**Kalibrasyon:** gerçek sınav TMS 16'yı ağırlıkla hesap sorusu olarak soruyor. Ölçülen
tipler ve eklenen senaryolar: **azalan bakiyeler → normal amortismana geçiş** (2014-16,
2023, 2024 — üç kez sorulmuş; 800.000 ₺, ilk iki yıl %40, üçüncü yıl 96.000 ₺) · kıst
amortisman ve **birikmiş amortisman** (2025 s.43 + 2026/1 tipi; 1 Nisan alım, 210.000 ₺) ·
üretim miktarı yöntemi (iki dönemlik) · maliyet bedeli (montaj ve deneme üretimi dâhil,
personel eğitimi ve açılış tanıtımı hariç) · sökme yükümlülüğünün bugünkü değeri ·
yeniden değerleme (2022 s.34 tipi) · satış kazanç/zararı + yeniden değerleme fazlasının
geçmiş yıllar kârlarına aktarımı.

⚠️ **Aynı §5 tuzağına üçüncü kez düştüm.** İlk turda kör %28→**%45** çıktı (boy 44/52):
doğru şıkları açıklayıcı, çeldiricileri terse yazma refleksi. 17 çeldirici genişletmesiyle
%25'e indi. Bu artık öngörülebilir bir hata — **yeni soru yazarken boy dağılımı tasarım
aşamasında ölçülmeli**, üretim sonrası değil.

§8 bağımsız aritmetik doğrulaması bu turda temiz geçti (9 hesap kontrolü).


### tms_2_stoklar (33 yama) — biçim kalibrasyonu

TMS 2 havuzdaki en sık sorulan standart (arşivde 10 dosya / 18 geçiş). **İçerik kapsamı
zaten tamdı** — amaç, tanım, ölçüm, NGD, kapsam, maliyet unsurları, GÜG dağıtımı,
yöntemler, değer düşüklüğü, iptal ve dipnotlar eksiksiz. Kusur biçimdeydi:

| ölçüm | önce | sonra | gerekçe |
|---|---:|---:|---|
| `TL` kullanan soru | 13 | **0** | §8: "₺ sembolü kullanılır" |
| olumsuz kök | %0 | **%10** | gerçek sınav bandı %9,6; TMS 2'de 3 ölçülmüş örnek |
| kökünde ≥2 tutar | %0 | **%20** | gerçek sınav TMS 2'yi hesap sorusu olarak soruyor |
| aynı kök kalıbı | 38/60 | **18/60** | §2: "aynı kök kalıbı seri üretimde kullanılmaz" |
| kör öğrenci | %23 | **%21** | |

**Kalibrasyon** (kopya yok, §11): 2016-18 s.39 "satın alma maliyetinde dikkate ALINMAZ" ·
2014-16 s.39 "yöntemlerden biri DEĞİLDİR" · 1-2-3 s.52 "açıklamalardan hangisi GEREKLİ
DEĞİLDİR" · 2022 "kurabiyelerin stok maliyeti kaç ₺" · 2025 pirinç NGD toplam değeri ·
2023 s.49 değer düşüklüğü · 2024 kalem bazında ölçüm · 2021/2026-2 FIFO ↔ ağırlıklı
ortalama karşılaştırması.

Çok adımlı senaryolara çevrilen hesaplar: NGD toplam değeri (4.000 kg buğday) · satın
alma maliyeti (6 kalemli) · sabit GÜG dağıtımı + dağıtılmayan tutar · dönem stok maliyeti
(fire ve satış gideri hariç) · FIFO 3 katman · ağırlıklı ortalama · kalem bazında ölçüm
(3 mal) · indirgeme iptali (maliyet tavanı).

⚠️ **§8 bağımsız aritmetik doğrulaması iki hata yakaladı:** 0033'te toplama yanlıştı
(8.000+15.000+6.000 = 29.000, ben 28.000 yazmıştım) ve 0034'te rakam devirmiştim
(1.600 × 44,40 = 71.040, ben 70.400 yazmıştım). İkisi de düzeltildi; çeldiriciler de
belgelenmiş hatalara (FIFO ↔ LIFO ↔ ağırlıklı ortalama sonuçları) oturtuldu.

⚠️ **Atıf kusuru üretim sırasında yakalandı:** 0034'ü ilk yazışımda "Yukarıdaki işletme
aynı verilerle…" diye kurmuştum. Karışık Test soruları karıştırdığı için atıf yasak
(maliyet dersinde 11 ATIF kusuru bu yüzden giderilmişti); soru kendi verisini taşıyacak
biçimde yeniden yazıldı.

**Havuz geneli bulgu — `TL` kullanımı:** §8 `₺` diyor ama havuzda 847 soru `₺`, **88 soru
`TL`** kullanıyordu. tms_2'nin 13'ü giderildi; **75 soru / 16 dosyada kaldı** (ağırlıkla
muhasebe_standartlari: tms_12 9, tms_16 8, tms_7 7, tms_36 7…). Mekanik ve düşük riskli
bir düzeltme, ancak dosyaların sahibi başka builder'lar olduğu için sahiplik çakışmasına
düşmemek adına ayrı bir tur olarak bırakıldı.


### diger_guncel_standartlar (YENİ KONU · 60 soru)

Kullanıcı "tms_34'ten devam" dedi; ölçüm ayrı konu açmaya karşı çıktı. §2 "Konu açma
önceliği" gereği 2014-2026 arşivinin 11 dosyasında frekans ölçüldü:

| standart | geçtiği dosya | toplam geçiş |
|---|---:|---:|
| TFRS 5 Satış Amaçlı | 5 | 12 |
| TFRS 15 Hasılat | 4 | 9 |
| TMS 41 Tarımsal | 5 | 8 |
| TFRS 3 İşletme Birleşmeleri | 3 | 5 |
| TFRS 13 GUD Ölçümü | 2 | 4 |
| **TMS 34 Ara Dönem** | **1** | **2** |
| *kıyas: TMS 2 (konusu var)* | *10* | *18* |

TMS 34'e ayrı 60 soruluk konu açmak, 2 kez geçen bir standarda TMS 2 ile aynı ağırlığı
verirdi — analiz raporunun uyardığı sapma. **Kullanıcı birleşik konuyu seçti.** Altı
başlık birlikte 40 geçişi karşılar; ağırlık frekansa göre dağıtıldı: TFRS 5 14 ·
TFRS 15 12 · TMS 41 10 · TFRS 3 9 · TFRS 13 8 · TMS 34 7.

**Kalibrasyon** (kopya yok, §11): 2026/2 s.49 TFRS 5 sayısal senaryo · 2026/1 s.52
ölçüm · 2024 s.53 TFRS 15 "beş adımdan biri DEĞİLDİR" · 2024 asil-vekil 36.000/3.600 ₺ ·
2021 bağımsız satış fiyatı · 2026/2 s.50 gayri nakdî bedel · 2021 s.54 TMS 41 ilk ölçüm ·
2023 s.50 + 2025 s.52 + 2026/2 s.51 TFRS 3 · 2022 TFRS 13 değerleme yöntemleri ·
2026/1 TMS 34 karşılaştırma dönemi.

**Ölçüm:** kör %23 · boy 21/5 · dağılım 12/12/12/12/12 · klon 0 · öncül uyarısı 0 ·
audit FATAL 0 / UYARI 0. Builder `build_std_diger_guncel.py`.

⚠️ **İlk turda kör %66 çıktı.** Doğru şıkları açıklayıcı, çeldiricileri terse yazmıştım —
40/60 soruda doğru şık tek en uzundu. Yerleşik reçete uygulandı (çeldiriciye gerçek
içerik ekle, 29 genişletme) → %23. Bu tuzağa sıfırdan üretimde de düşülüyor; yeni konu
yazarken boy dağılımı tasarım aşamasında kontrol edilmeli.

⚠️ Yeni konu `curriculum.json`'a eklendi → **telefonda görünmesi için yeni binary
gerekir** (matematik konularıyla aynı durum). Test sayıları manifestten ölçülerek
güncellendi: content_quality 11168 → **11228**, SGS 6360 → **6420**, curriculum konu
106 → **107**.


### Sözcük tell'i — havuz genelinde giderildi (`fix_lexical_tell.py`)

tms_21'de bulunan kusur tüm havuzda ölçüldü ve düzeltildi. Ölçüt önce eksikti (regex
büyük harfli `Her hâlde` arıyordu, cümle içindeki 866 küçük harfli geçişi kaçırıyordu);
düzeltilmiş ölçütle asimetri: `her hâlde` 866 çeldirici / 5 doğru şık = **173×**,
`hiçbir <pekiştireç>` 217/1 = **217×**, `zorunda` 279/21, `niteliğinde` 130/17.

**Karar dayanağı — ev artefaktı, üslup değil:** 2014-2026 arşivinden çıkarılan **12.436
gerçek sınav şıkkında** `hiçbir` %0,2 · `Her hâlde` %0,0 · `zorunda` %0,0 · `ifade eder`
%0,0. Bizim havuzda ~%9. Temizlik soruları gerçek sınava **yaklaştırır**.

| ölçüm | önce | sonra |
|---|---:|---:|
| eleme ≥%30 olan paket | 11 | **0** |
| eleme ≥%25 olan paket | 18 | **2** |
| havuz ortalaması | %23 | **%20** (rastgele düzeyi) |
| işaretli şık | 2566 | **676** |
| kör ≥%31 (UYARI) | 0 | **0** |
| kör ≥%30 olan paket | 23 | **13** |
| ortalama kör | %25 | **%24** |

Kalan 676 işaret ağırlıkla `zorunda` ve `niteliğinde`nin **anlamlı** kullanımlarıdır
("tazmin etmek zorundadır", "eksik borç niteliğinde") — gerçek sınavda da geçer.

Kaldırılanlar zarf tümleci olduğu için anlam korunur ("hiçbir biçimde kayda alınmaz" →
"kayda alınmaz"); `-mek zorunda olan bir X ifade eder` kuyruğu çekimli fiile indirilir.
Dönüştürücü dilbilgisi korumaları taşır ve koruma tetiklenirse metni değiştirmez.
Anlamın parçası olan `hiçbir istisna / fark / etkisi / ilgisi / sorumluluk` korunur.

Dosya başına seviye: **TAM 64** paket (`fix_lexical_tell.py`) · **TEMEL 7** (cümle içi
`her hâlde` bırakıldı, kör yükselmesin diye) · **ELLE DENGE 11**
(`fix_bekleyen_denge.py`, 107 dondurulmuş yama).

**Elle denge turu — 11 paket tamamlandı.** Mekanik temizlik bu paketlerde kör'ü %26'dan
%45'e kadar çıkarıyordu. tms_21 reçetesi uygulandı: doğru şıkkı kısaltmak yerine
**çeldiriciye gerçek içerik eklendi** (yanlış iddianın kendi mantıksal sonucu — dolgu
değil, çeldiriciyi daha inandırıcı yapan bir ek). Sonuç kör: temerrut_tazminat %26→%23 ·
sebepsiz_zenginlesme %28→%23 · ozel_durumlar %28→%23 · haksiz_fiil %26→%21 ·
sosyal_guvenlik_hukuku %21→%21 · butce_maliye_politikasi %30→%22 · kamu_gelir_gider
%28→%21 · sorumluluk_ve_yasaklar %30→%23 · limited_sahis_sirketleri %30→%22 ·
vergi_denetimi_ceza_uyusmazlik %30→%25 · vergi_hukuku_temel_kavramlar %30→%20.

⚠️ **Adayların tamamını uygulamak yanlış:** 25 adayın 25'i uygulandığında doğru şık bu
kez sistematik ORTADA kaldı ve "iki ucu ele, ortadan tahmin et" öne geçti (kör %30).
Her pakette kör'ü en aza indiren **alt küme** ölçümle seçildi (7-16 / 12-25) ve
builder'da donduruldu. İki maliye paketinde ikinci dolgu ailesi ("…bu ilişki
piyasa/politika koşulları ne olursa olsun değişmez") uzatma yerine gerçek içerikle
değiştirildi; bu arada 6 çeldiricide önceden var olan bozuk Türkçe de düzeltildi.

Ayrıntı: `tools/sgs/SIK_ORUNTUSU_RAPORU.md`.

**Sahiplik kuralı (bu turda öğrenildi):** her sorunun tek sahibi olmalı. Leksik temizlik
başta 440 soruda başka builder'ların metnine dokunuyordu; `tms_21` leksik listeden
çıkarıldı (sahibi profil builder'ı), kalan örtüşmelerde sahip builder'ın beklenen metni
aynı dönüşümden geçirildi. ⚠️ `tools/sgs/builders/` altında `--check` DESTEKLEMEYEN eski
tek-seferlik scriptler var (`build_std_*.py`, `rebalance_*.py`, `fix_*_boy.py`);
argümansız çalıştırılınca içeriği yeniden yazarlar. Toplu doğrulama döngüsü yalnız
`add_argument("--check")` taşıyan builder'ları çalıştırmalıdır.

**audit.py'ye eklendi (2026-07-28).** `kor_ogrenci`'ye altıncı strateji: *işaretliyi
ele, kalandan tahmin et*. Ayrıca 3. ve 4. stratejilerin (ele + en kısa/uzun) eleme
adımı dar dolgu kümesinden **geniş kümeye** taşındı — bu, boy ve sözcük ipuçlarının
birleşimini ölçer ve 6 paketi daha açığa çıkardı; hepsi temizlendi.

Dedektörün dişi doğrulandı: temizlik öncesi hâle (commit `9be971c^`) uygulandığında
11 paketi FATAL'la yakalıyordu (%35-42). Eşikler null modelle yeniden kalibre edildi
ve 31/35 → **32/36** oldu — gevşetme değil, ölçüt güçlenince rastgele tabanı da
yükseldiği için (95./99. yüzdelik %30/%33 → %31/%35). Paketler eşiğe değil **≤%30
kalite hedefine** kadar temizlendi; havuzda hedefi aşan paket kalmadı.

---

## Ders 14 — Matematik: KAPSAM AÇIĞI KAPATILDI (2 yeni konu · 120 yeni soru)

Bu ders için yapılan iş **kalite temizliği değil, kapsam üretimidir**. Havuzdaki üç konu
(temel işlemler, oran-orantı, denklem) ölçüldüğünde zaten temizdi: kör %19-21, boy 1/0,
%100 sayısal. Sorun soruların kalitesi değil, **sınavın sorduğu alanın havuzda hiç
bulunmamasıydı** (`SGS_CIKMIS_SORULAR_ANALIZI_2026-07-22.md` → "Yüksek öncelik: Matematik").

**Kapsam ölçümü (§2'nin üç ölçütü — 2014-2026 arşivi, 11 dosya):**

| başlık | görüldüğü kâğıtlar | havuzda |
|---|---|---|
| limit | 2021, 2022 ×2, 2023 ×2, 2025 ×3, 2026/1, 2026/2 — **her dönemde** | yoktu |
| analitik geometri (doğru, parabol, çember, orta nokta) | 1-2-3, 2021, 2022, 2023 ×3, 2025 | yoktu |
| logaritma | 2021'den bu yana kesintisiz, 2026/1 s.8 | yoktu |
| sonsuz seri ∑ | 1-2-3, 2016-18, 2022, 2026/2 s.14 | yoktu |
| fonksiyon (sabit, bileşke) | 2024 s.12, 2026/1 s.13, 2026/2 s.9 | yoktu |
| türev / karma kısmi türev | 2016-18, 2024, 2026/2 s.13 | yoktu |

**Açılan konular** (analizin önerdiği iki başlık):

- `fonksiyon_ustel_logaritma_analitik` — Fonksiyonlar, Üstel-Logaritmik İfadeler ve
  Analitik Geometri (60 soru): fonksiyon temelleri 9 · bileşke 7 · ters fonksiyon 5 ·
  tanımlı işlem 4 · üslü-üstel 7 · logaritma ve ln 11 · çarpanlara ayırma/sadeleştirme 5 ·
  analitik geometri 12. Builder `build_mat_fonksiyon_analitik.py`.
- `limit_turev_seri` — Limit, Türev ve Seriler (60 soru): 0/0 belirsizliği 11 ·
  sonsuzda limit 5 · trigonometrik limit 5 · üstel-logaritmik limit 5 · tek yönlü limit
  ve süreklilik 6 · türev kuralları 12 · üstel/log/trig türev, teğet, ekstremum 8 ·
  kısmi ve karma kısmi türev 4 · seriler 4. Builder `build_mat_limit_turev_seri.py`.

**Ölçüm (iki paket de):** dağılım 12/12/12/12/12 · kör öğrenci %23 ve %21 · boy eğilimi
0/1 ve 1/3 · harf örüntüsü yok, üçlü tekrar yok · klon 0 · audit FATAL 0 / UYARI 0.

**§8 bağımsız doğrulama:** 120 sorunun her sayısal sonucu **sympy** ile builder'dan
bağımsız ikinci kez doğrulanır (`sp.limit`, `sp.diff`, `sp.summation`, `sp.solve`);
doğrulama `--write` için zorunludur, sympy yoksa builder çalışmaz. Üretim sırasında
bu doğrulama bir FATAL klon yakaladı (aynı şablon + aynı cevap: iki farklı 0/0
belirsizliği de 1 veriyordu) — soru farklı bir işleme dönüştürülerek düzeltildi.

**§11 telif:** 2026/2'nin s.12 (1 − cos x)/x² limiti ile s.13 (x + ln3x)/eˣ türevi ve
2026/1'in s.8 log₃(4x + 1) = 2 denklemi **bilerek kullanılmadı**; aynı beceriyi ölçen
farklı katsayı ve yapılar kuruldu. Çıkmış kâğıtlar yalnız kapsam, dil ve zorluk
kalibrasyonu için okundu.

**§8 gösterim standardı** (uygulamada soru kökü/çözüm Markdown, şıklar düz metin):
üst simge `x² xⁿ eˣ f⁻¹` · alt simge `log₂ log₃` · `√` · bileşke `∘` · türev `f′ ∂z/∂x
∂²z/∂x∂y` · limit `lim(x→2)` önek biçimi · seri `∑(n=1→∞)` · çarpma `·` · eksi `−`
(U+2212, mevcut paketlerle aynı). Markdown'ı bozduğu için `*` ve `_` kullanılmaz.
Gösterim `test/math_notation_render_test.dart` ile 320 px ve 768 px genişlikte
doğrulanır (120 sorunun kökü + çözümü + 5 şıkkı = 840 widget, iki boyutta);
test ayrıca mutlak değer çubuğunun (`|x − 2|`) GFM tablo ayıracı sanılıp metni
yutmadığını denetler — sonuç: 0 Table, çubuk render edilen metinde korunuyor,
hiçbir genişlikte taşma yok. Tam süit 86 test / 5,4 saniye.

⚠️ **Test yazarken tuzak:** 840 widget'ı tek ağaca koymak çalışıyor (pump ≈ 600 ms)
ama o ağacı bir sonraki `pumpWidget` **dispose** ederken test dakikalarca asılı
kalıyor; aynı dosyada büyük ağaç kuran bir testten sonra gelen ikinci `testWidgets`
de asılıyor. Çözüm: soruları **10'luk dilimler** hâlinde render etmek ve bütün
denetimleri **tek testte** toplamak. Bu bir içerik kusuru değil, flutter_test
davranışıdır; eşik düşürülerek değil test yapısı değiştirilerek çözüldü.

### Şık sırası — bilinçli karar

Gerçek kitapçık sayısal şıkları **artan sıraya** dizer (2026/1 s.8: "A) 1 B) 2 C) 3 D) 4
E) 5"). Yeni konular bunu **uygulamıyor**, çünkü mevcut üç matematik paketinin 180
sorusunun tamamı sıralanmamış ve dağılımı 12/12/12/12/12'dir; yalnız yeni konularda
sıralama, Karışık Test'te iki farklı şık düzenini yan yana getirirdi. Ayrıca ölçüldü:
artan sıralama uygulandığında doğru cevabın **%43'ü C'ye düşüyor** (çeldiriciler doğru
değeri simetrik kuşattığı için) — bu, körü %20'den %43'e çıkaran gerçek bir tell'dir.
Sıralamaya geçilecekse **dersin tamamında** ve çeldirici değerleri rank dengesine göre
yeniden seçilerek yapılmalıdır; ayrı bir iş olarak ertelendi.

### Bağlama ve sırasında bulunan sapma

`sgs.json` + `manifest_merge.py --write --version 169` + `curriculum.json` zinciri
işletildi. Uygulama asset'ine güncel manifest kopyalanırken **önceden var olan bir
sapma** ortaya çıktı: gömülü `assets/content/manifest_v2.json` **v162 / 199 pakette**
kalmışken içerik reposu v168 / 201'deydi. `borclar_hukuku/sozlesme_turleri.json` ve
`vergi_hukuku/vergi_usul_kanunu.json` paketleri OTA'da canlı olmasına rağmen gömülü
asset manifestine hiç girmemişti; yeni kurulan bir cihaz ilk OTA senkronuna kadar bu iki
konuyu görmüyordu. Manifest tazelenince bu da düzeldi (SGS gömülü soru 6120 → 6360).

⚠️ **Yeni konular telefonda ancak yeni binary ile görünür.** `curriculum.json`
`rootBundle`'dan okunur ve OTA yalnız `v2/manifest.json` ile paket dosyalarını indirir
(`content_repository.dart`); konu listesi OTA'dan gelmez.

Test sayıları manifestten **ölçülerek** güncellendi (§12: tahmin etme):
`content_quality_test` 10928 → **11168** ve SGS 6120 → **6360**;
`curriculum_test` konu sayısı 104 → **106**.

---

## Zorunlu doğrulama komutları (her ders sonu)

```bash
python3 tools/sgs/builders/<ilgili_builder>.py --check
python3 tools/sgs/audit.py content/<ders>/<konu>.json         # her paket
python3 tools/sgs/audit.py --manifest content/v2/manifest.json
python3 tools/sgs/tests/test_audit.py
python3 tools/shared/manifest_merge.py --check
python3 tools/shared/check_scope.py --program sgs
cmp -s content/<...> ../smmm_sgs_pratik/assets/content/<...>   # iki repo eşitliği
git diff --check
~/.tools/flutter/bin/flutter test test/content_quality_test.dart   # app repoda
```

Git/OTA: kullanıcı açıkça istemeden commit/push/OTA YOK. ANDROID_YAYIN_DURUMU.md ve
SMMM/Yeterlilik dosyalarına dokunma. OTA'da `content/v2/manifest.json` kullan.
