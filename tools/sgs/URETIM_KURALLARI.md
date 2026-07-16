# SGS Pratik — soru üretim kuralları

Bu belge yalnız **SMMM Staja Giriş Sınavı (SGS)** içindir ve Claude tarafından
geliştirilir. SMMM Yeterlilik sınavının 2026/1 ders dağılımları bu belgeye taşınmaz.

## Teslim kapısı

```bash
python3 tools/sgs/audit.py <sgs-paket.json>
python3 tools/sgs/audit.py --manifest content/v2/manifest.json
```

FATAL bulunan paket yayımlanmaz. Uyarılar insan incelemesinden geçirilir.

## Temel üretim ilkeleri

- Sorular **özgün** yazılır; TESMER veya kitap sorusu kopyalanmaz ya da yakın türevi
  üretilmez. Çıkmış sorular yalnız konu ağırlığı, dil ve zorluk kalibrasyonu içindir.
- Gerçek SGS biçimine uygun olarak her soru **A–E beş seçeneklidir**.
- Konu başına hedef 60 soru, yani 20'şer soruluk üç konu testidir. Bölüm/karma test
  havuzu ayrıca ve özgün sorulardan oluşur.
- Soru, seçenek, çözüm ve kaynak birlikte üretilir. Çözüm yalnız cevabı tekrar etmez;
  doğru yaklaşımı ve makul çeldiricilerin neden yanlış olduğunu açıklar.
- Doğru cevap harfi örüntüsüz ve dengeli atanır. Şık uzunluğu cevap anahtarını ele
  vermez; doğru seçenek sürekli en kısa veya en uzun olmaz.
- Senaryo ve hesaplama SGS'nin ilgili dersindeki gerçek soru diline göre kullanılır.
  Finansal Muhasebede TDHP hesap kodu/adı, gerektiğinde borç–alacak yönü ve hesap
  tutarlılığı doğrulanır.
- Hesap sorularında bütün ara sonuçlar kod içinde yeniden hesaplanır; yuvarlama ve
  para birimi kökte açık olur.
- Mevzuat, oran, had ve parasal sınırlar üretim tarihinde birincil resmî kaynaktan
  doğrulanır. Güncellik yalnız metadata tarihi yazılarak varsayılmaz.
- `source.legislationRef` mümkün olduğunca kanun maddesi, standart paragrafı veya
  resmî düzenleme düzeyinde belirtilir.

## SMMM Yeterlilikten ayrım

- Yeterlilikte gözlenen “Finansal Muhasebede 11/20 yevmiye” gibi ders kotaları SGS
  paketlerine uygulanmaz.
- SGS konu taksonomisi, süre ve deneme dağılımı kendi resmî sınav yapısından gelir.
- Ortak ders veya kavram bulunması, aynı sorunun iki sınava otomatik verilmesi için
  yeterli değildir.

Bu başlangıç belgesi uygulama reposundaki mevcut `CLAUDE.md` SGS ilkelerini korur;
Claude yeni resmî kitapçık incelemeleriyle ayrıntıları burada geliştirebilir.
