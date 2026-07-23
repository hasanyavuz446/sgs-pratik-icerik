# SGS içerik temizliği — çalışma durumu

Son güncelleme: 23 Temmuz 2026

## Tamamlanan kapsam

**Finansal Muhasebe dersindeki 16 konu paketinin tamamı** insan incelemeli anlamsal
temizlikten geçti; dersin ilk anlamsal temizlik turu tamamlandı. Aynı kazanımı aynı
yönden ölçen tekrarlar azaltıldı; seçilen sorular 2024-2026 SGS dili, uygulama
yoğunluğu ve yürürlükteki dayanaklar gözetilerek yenilendi.

Önceki yayın gruplarında tamamlanan 14 konu: Muhasebenin Temel Kavramları, Muhasebe
Süreci ve Hesap Planı, Hazır Değerler, Stoklar, Ticari Alacaklar, Menkul Kıymetler,
Maddi Duran Varlıklar, Maddi Olmayan Duran Varlıklar, Mali Duran Varlıklar, Yabancı
Kaynaklar, Özkaynaklar, Gelir Tablosu Hesapları, Maliyet Hesapları, Dönem Sonu
İşlemleri.

Bu turda tamamlanan son iki konu:

15. **Kur Farkları** — 26 soru revize edildi.
16. **KDV Muhasebesi** — 30 soru revize edildi.

Bakım builder'ı (`build_financial_accounting_semantic_cleanup.py`) artık toplam
**16 paket / 356 uzman revizyonlu soru**yu içerik ve uygulama repolarında eş zamanlı
tutmaktadır (14 paket / 300 soru → 16 paket / 356 soru).

### Kur Farkları (26 revizyon)

Havuz "kur yükselirse alacakta kâr / borçta zarar" mantığını ve basit
`döviz tutarı × kur değişimi` işlemini defalarca tekrarlıyordu; çok sayıda ters soru
(sonuçtan kur/tutar bulma) aynı fikri ölçüyordu. Korunan çekirdek: tanımlar
(MB döviz alış kuru, 646/656), yön kuralları, gerçekleşmiş/gerçekleşmemiş ayrımı,
MDV aktifleştirme öncesi/sonrası zamanlaması, öncüllü sorular ve en iyi çok dönemli
örnekler. Eklenen yeni beceriler: kısmi tahsilat/kısmi ödeme, önceki dönem
değerlemesi sonrası tahsilat/ödeme, ihracat/ithalat çok tarihli senaryolar, döviz
kasası/mevduatı ve efektif ↔ döviz kuru ayrımı (efektif alış vs döviz alış), yanlış
hesap/ters borç-alacak ayırt ettiren yevmiye seçenekleri, çok kalemli net etki
(kayıtlar ayrı) ve çok adımlı ters sorular. TMS 21'in fonksiyonel para/çevrim
ayrıntılarına girilmedi (ayrı paket).

### KDV Muhasebesi (30 revizyon)

Havuzda basit `matrah × oran`, KDV dahil→hariç iç yüzde matematiği ve hesap tanımları
aşırı tekrarlıydı; cevap dağılımı yapaydı (her harf 12). Korunan çekirdek:
191/391/190/360 işleyişi, temel alış/satış ve ay sonu mahsup kayıtları ve **iade
kuralı** (satış iadesi → 391 borçlandırılır; alış iadesi → 191 alacaklandırılır).
Eklenen yeni beceriler: senetli ve çekli alış/satış, mala ilişkin nakliyenin maliyete
eklenmesi, hizmet/KKEG gideri, ithalat ve gümrük KDV'si, perakende (dahil bedelden iç
yüzde), önceki dönem devreden KDV ile cari mahsup, aynı ayda çok alış/çok satıştan net
KDV, tam mahsup yevmiyesi ve **eksik/ters kayıt bulma** (iade kuralını sınayan). KDV
oranları soru kökünde açıkça verildi; 2026 genel oranı %20 esas alındı. Vergi hukuku
kapsamı (beyan süreleri, istisnalar) muhasebe kaydına çekildi; ayrıntı ayrı KDV Vergi
Hukuku paketindedir.

## Doğrulama durumu

- Tek paket denetimi — `kur_farklari.json`: FATAL 0, UYARI 0
- Tek paket denetimi — `kdv_muhasebesi.json`: FATAL 0, UYARI 0
- SGS tam havuz denetimi (`--manifest content/v2/manifest.json`): FATAL 0, UYARI 0
- Denetim regresyon testleri (`tools/sgs/tests/test_audit.py`): 29 test geçti
- `manifest_merge.py --check`: uyumlu (201 paket; sürüm 165 değişmedi)
- `check_scope.py --program sgs`: kapsam temiz (3 SGS dosyası)
- Builder `--check`: 16 paket / 356 soru iki repoda doğrulandı
- `git diff --check` (iki repo): temiz
- Flutter `content_quality_test.dart`: geçti
- Flutter tam test paketi: 85 test geçti
- İçerik ve uygulama kopyaları: her iki dosyada birebir eşit
- Her iki pakette 60/60 benzersiz id ve kök; tüm sorular `validYear=2026`,
  `source.kind=generated`, madde/fıkra düzeyinde dayanak
- Cevap dağılımları doğal: Kur Farkları A11 B13 C11 D13 E12; KDV A13 B11 C12 D11 E13
  (mekanik örüntü ve yapay eşitlik yok)

## Devam noktası

Finansal Muhasebe dersinin ilk anlamsal temizlik turu tamamlandı. Sıradaki mantıklı
alan, `tools/sgs/SIK_ORUNTUSU_RAPORU.md` ve denetim uyarılarına göre **şık örüntüsü
(kör öğrenci) yüksek olan derslerin temizliği**dir; özellikle Muhasebe Standartları
(ölçülen kör öğrenci ~%52), Borçlar Hukuku (~%64) ve Muhasebe Standartları'ndaki
dolgu/atma-şıkkı örüntüsü. Alternatif olarak çıkmış soru analizindeki kapsam açıkları
(ileri matematik, muhasebe bilgi sistemleri, güncel TMS/TFRS ve sürdürülebilirlik
raporlaması) yeni konu paketi olarak değerlendirilebilir.

Yeni çalışmaya başlarken:

1. `tools/sgs/builders/build_financial_accounting_semantic_cleanup.py --check`
2. Hedef paketteki 60 soruyu tekrar kümeleri ve güncel SGS örüntüsü açısından incele
3. Şık örüntüsü temizliği için ayrı bir bakım builder'ı veya ilgili konunun kendi
   üreticisi kullanılır; her revizyonun aritmetiği builder'dan bağımsız doğrulanır
4. İki repoyu eşitle; tek paket + tam havuz denetimi ve Flutter testlerini çalıştır
