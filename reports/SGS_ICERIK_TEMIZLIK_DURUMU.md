# SGS içerik kalite temizliği — PROGRAM DURUMU (tüm SGS)

Son güncelleme: 23 Temmuz 2026

> Bu rapor artık yalnız Finansal Muhasebe değil, **manifestteki tüm SGS programının**
> (`content/v2/manifest.json`, programIds=["sgs"]) kalite temizliği ilerleme kaydıdır.
> Yöntem: her ders için kapsam denetimi → soru havuzu denetimi (tüm sorular) → çıkmış
> soru biçim karşılaştırması → düzeltme (idempotent builder / güvenli yama) → zorunlu
> doğrulamalar. Kaynaklar: `tools/sgs/URETIM_KURALLARI.md`,
> `reports/SGS_CIKMIS_SORULAR_ANALIZI_2026-07-22.md`, `~/Desktop/sgs çıkmış sorular/`.

## Genel SGS tamamlanma

**16 ders · 104 konu · 6240 soru.** Tamamlanan: **35 / 104 konu = %33,7**
(finansal_muhasebe 16 ✅ · mali_tablolar_analizi 6 ✅ · maliyet_muhasebesi 6 ✅ · denetim 7 ✅).
Yaklaşım dersin doğasına göre seçiliyor: sayısal derslerde **harder (çok-adımlı) kalibrasyon**,
kavram ağırlıklı derslerde **profil kalibrasyonu** (olumsuz kök + öncül oranı) ve anlamsal denetim.

| # | Ders | Konu | Tamamlanan | Durum |
|---|---|---:|---:|---|
| 1 | finansal_muhasebe | 16 | 16 | ✅ TAM (ilk anlamsal tur; OTA v166) |
| 2 | mali_tablolar_analizi | 6 | 6 | ✅ İNCELENDİ — SOLİD, 0 değişiklik (aritmetik+kalite doğrulandı) |
| 3 | maliyet_muhasebesi | 6 | 6 | ✅ **TAM** — 6/6 konu harder-kalibrasyondan geçti (builder 6 paket/125 soru); 11 ATIF kusuru giderildi |
| 4 | denetim | 7 | 7 | ✅ **TAM** — 7/7 konu profil kalibrasyonundan geçti (builder 7 paket/149 soru); ders ort. olumsuz %5→**%37**, öncüllü %6→**%11**, kör 25-30→**21-26** |
| 5 | muhasebe_standartlari | 17 | 0 | ⬜ |
| 6 | borclar_hukuku | 8 | 0 | ⬜ |
| 7 | ticaret_hukuku | 7 | 0 | ⬜ |
| 8 | meslek_hukuku | 5 | 0 | ⬜ (mesleki_degerler_etik yalnız boy-cilası, v167) |
| 9 | is_ve_sosyal_guvenlik_hukuku | 3 | 0 | ⬜ |
| 10 | vergi_hukuku | 11 | 0 | ⬜ |
| 11 | ekonomi | 3 | 0 | ⬜ |
| 12 | maliye | 3 | 0 | ⬜ |
| 13 | turkce | 3 | 0 | ⬜ |
| 14 | matematik | 3 | 0 | ⬜ |
| 15 | ataturk_ilkeleri | 3 | 0 | ⬜ |
| 16 | yabanci_dil | 3 | 0 | ⬜ |

Canlı OTA: **v167** (FM Kur+KDV v166 + denetim_raporu/mesleki_degerler_etik boy-cilası v167).

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

**Sonraki ders:** #5 **muhasebe_standartlari** (17 konu — programın en büyük dersi).

Not — kullanılan teknik dersler: (1) öncüllü sorularda seçenek metni kombinasyon olduğu için
harf permütasyonu yapılmaz, hedef harf tasarımda sabitlenir; (2) kombinasyon tespitinde
`startswith("Yalnız")` kırılgandır — "**Yalnızca** büro içi…" gibi normal şıkları yanlış pozitif
yakalar, tam-eşleşen regex gerekir; (3) **§5 boy dengesi üç turda öğrenildi:** yanlış ifadeyi
gerekçesiyle yazmak → "en uzunu seç" tell'i; hepsini kısaltmak → "en kısayı seç" tell'i; hepsini
ortalamak → "iki ucu ele, ortadan tahmin et" tell'i. Doğru yaklaşım **dağılımdır** (bir kısmı uzun,
bir kısmı kısa, kalanı orta) ve tasarım betiğine "doğru şık tek-en-uzun/tek-en-kısa mı?" ön kontrolü
eklenmelidir.

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
