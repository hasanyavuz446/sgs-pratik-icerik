# SGS içerik temizliği — çalışma durumu

Son güncelleme: 23 Temmuz 2026

## Tamamlanan kapsam

Finansal Muhasebe dersindeki 16 konu paketinin ilk 14'ü insan incelemeli anlamsal
temizlikten geçirildi. Aynı kazanımı aynı yönden ölçen tekrarlar azaltıldı; seçilen
sorular 2024-2026 SGS dili, uygulama yoğunluğu ve yürürlükteki dayanaklar gözetilerek
yenilendi.

Son yayın grubunda tamamlanan konular:

1. Mali Duran Varlıklar
2. Yabancı Kaynaklar
3. Özkaynaklar
4. Gelir Tablosu Hesapları
5. Maliyet Hesapları
6. Dönem Sonu İşlemleri

Bakım builder'ı toplam **14 paket / 300 uzman revizyonlu soru**yu içerik ve uygulama
repolarında eş zamanlı tutmaktadır.

## Doğrulama durumu

- SGS tam havuz denetimi: FATAL 0, UYARI 0
- Flutter `content_quality_test.dart`: geçti
- Flutter tam test paketi: 85 test geçti
- İçerik ve uygulama kopyaları: birebir eşit

## Devam noktası

Sıradaki konu: **Kur Farkları** (`content/finansal_muhasebe/kur_farklari.json`).

Kur Farkları tamamlandıktan sonra **KDV Muhasebesi** ele alınacak. Böylece Finansal
Muhasebe dersindeki 16 konu paketinin ilk anlamsal temizlik turu tamamlanmış olacak.

Yeni çalışmaya başlarken:

1. `tools/sgs/builders/build_financial_accounting_semantic_cleanup.py --check`
2. Kur Farkları paketindeki 60 soruyu tekrar kümeleri ve güncel SGS örüntüsü açısından incele
3. Seçilen revizyonları aynı builder'a ayrı bir `PERIOD...` benzeri paket olarak ekle
4. İki repoyu eşitle; SGS denetimi ve Flutter testlerini yeniden çalıştır
