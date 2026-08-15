# SGS Pratik — soru üretim ve kalite standardı

Bu belge yalnız **SMMM Staja Giriş Sınavı (SGS)** içindir ve Codex tarafından
yönetilir. Amaç şemaya uyan JSON üretmek değil; **özgün, güncel, müfredata bağlı,
tek doğru cevaplı ve gerçek sınavın düşünme biçimine yakın** bir soru bankasıdır.

Otomatik denetim alan uzmanı incelemesinin yerini tutmaz. Bir paket şu üç kapıyı da
geçmeden yayıma hazır sayılmaz:

1. Builder ve aritmetik kontrolleri,
2. Otomatik içerik denetimi (`tools/sgs/audit.py`),
3. Cevap, dayanak ve sınav uygunluğu için insan incelemesi.

SMMM Yeterlilik kuralları için `tools/smmm/URETIM_KURALLARI.md`. İki programın
kuralları ayrıdır; ortak ders adı, sorunun iki programda kullanılabileceği anlamına
gelmez. **Ancak §5–§7'deki kalite doktrini programdan bağımsızdır ve iki belgede de
aynıdır** — bilerek eşitlenmiştir.

---

## 0. Teslim kapısı

```bash
python3 tools/sgs/audit.py content/<ders>/<konu>.json
python3 tools/sgs/audit.py --manifest content/v2/manifest.json
python3 tools/sgs/tests/test_audit.py          # denetimin kendi regresyon testleri
```

- **FATAL:** Paket yayıma gidemez.
- **UYARI:** Ya düzeltilir ya da neden güvenli olduğu inceleme notuna yazılır.

Denetim yalnız SGS şemasını (`ders/konu/stem/options/answer/solution`) ve içerik
reposundaki yolları kabul eder; `content/yeterlilik` ve repo dışı yolları reddeder.

`FATAL 0` görmek kalite onayı değildir. Denetim; mevzuat yorumunun doğruluğunu,
çeldiricilerin makullüğünü veya bir sorunun gerçekten özgün olduğunu kanıtlayamaz.

---

## 1. Resmî sınav sözleşmesi

Güncel SGS tek oturumda **130 soru / 165 dakika**, her soru **A–E beş seçenekli**.
Yanlış cevaplar doğru cevapları azaltmaz.

Arşiv iki ayrı döneme ayrılır:

- **2014–2018:** 120 soru / 150 dakika; 20 genel kültür-yetenek + 100 alan bilgisi.
- **2019–2026:** 130 soru / 165 dakika; yabancı dilin eklenmesiyle ilk blok 30,
  alan bilgisi yine 100 sorudur.

2026/1 ve 2026/2 kitapçıklarında ölçülen güncel dış dağılım:

| Soru | Ders/alan | Adet |
|---|---|---:|
| 1–7 | Türkçe | 7 |
| 8–15 | Matematik | 8 |
| 16–20 | Atatürk İlkeleri | 5 |
| 21–30 | Yabancı Dil | 10 |
| 31–56 | Finansal muhasebe, standartlar ve yakın muhasebe alanları | 26 |
| 57–64 | Maliyet Muhasebesi | 8 |
| 65–72 | Mali Tablolar Analizi | 8 |
| 73–88 | Denetim | 16 |
| 89–94 | Ekonomi | 6 |
| 95–100 | Maliye | 6 |
| 101–130 | Meslek · İş/SGK · Vergi · Ticaret · Borçlar | 5 × 6 |

### 31–56 bloğunun iç dağılımı

`Finansal Muhasebe 20 + Muhasebe Standartları 6`, uygulamanın dengeli deneme
üretmek için kullandığı bir **modeldir**; değişmez bir resmî alt kota değildir.

- 2026/1: 31–48 çekirdek finansal muhasebe, 49–54 standartlar, 55 muhasebe bilgi
  sistemi, 56 uluslararası etik kuruluşu.
- 2026/2: 31–48 çekirdek finansal muhasebe, 49–55 standartlar, 56 muhasebe bilgi
  sistemi.

Bu nedenle resmî sözleşme 31–56 arasındaki 26 soruluk muhasebe ekosistemidir.
Uygulamadaki `lib/features/deneme/exam_blueprint.dart` dağılımı son sınavlar geldikçe
kontrol edilir; değişiklikte `test/deneme_test.dart` birlikte güncellenir.

### Çıkmış kâğıtların kullanımı

2014–2026 arasındaki **38 sınav / 4.790 soru**, `~/Desktop/sgs çıkmış sorular/`
altındadır ve **yalnız konu ağırlığı, dil ve zorluk kalibrasyonu** içindir (bkz.
§11). Ayrıntılı envanter ve bulgular:
`reports/SGS_CIKMIS_SORULAR_ANALIZI_2026-07-22.md`.

⚠️ Metin çıkarırken `pdftotext -layout` **kullanma**. İki sütunlu kitapçıklarda
soruların ~%25'ini düşürür; akış sırası (`pdftotext dosya.pdf -`) gerekir.

Kalibrasyon, tahminin yerini alır. Bir konuyu yazmadan önce o standardın/konunun
gerçek kâğıtlarda nasıl sorulduğu çıkarılır. Ölçülmüş örnekler:

- **TMS 21** — 2025 s.53 ve 2024 s.50, ikisi de "geçerli para biriminin tespiti" ve
  **negatif kök**. Hesap sorusu değil.
- **TMS 10** — iki yük merkezi: tarih aralığı tanımı (2016-18, 2020) ve tarihli
  senaryo (2023 ×2). 2023'ün şıkları **2×2 çapraz** kurulu (düzeltme gerektiren/
  gerektirmeyen × karşılık düzeltilir/düzeltilmez) — aday iki ekseni de bilmeden
  bulamaz. Çapraz şıklar doğal olarak denk boyda olduğu için §5 açısından da iyidir.
- **TMS 23** — 2026/1 s.50: aktifleştirme oranı × harcama × süre.
- **TMS 20** — incelenen 38 sınavda **hiç sorulmamış**. Ders ağırlığı ölçülerek belirlenir,
  standart listesine bakarak değil.
- **2026/2** — TFRS 15, TFRS 3, TMS 41 ve ilk kez TSRS 1–2 görünür hâle geldi.
  Güncel standart paketi yalnız eski frekansa bakılarak dondurulamaz.
- **Muhasebe bilgi sistemleri** — dokuz ayrı dönem dosyasında görülür ve 2026'nın
  iki sınavında da sorulmuştur; bağımsız kapsam olarak izlenir.

---

## 2. Üretimden önce soru planı hazırla

Konu başına hedef **60 soru = 20'şer soruluk 3 test**. 60 soru, sayıları değiştirilmiş
20 sorunun üç kopyası değildir. Yazmadan önce üretim matrisi hazırlanır: alt kapsam ·
soru türü (kavram/uygulama/hesap/kayıt/istisna/karşılaştırma) · ölçülen bilişsel işlem ·
zorluk · doğru cevabın dayanağı · her çeldiricinin temsil ettiği kavram yanılgısı.

- Aynı bilgi, ancak **farklı bir zihinsel işlem** ölçüyorsa tekrar kullanılabilir.
  Eş anlamlı kelime, kişi adı veya sayı değişikliği yeni soru sayılmaz.
- Her test kendi içinde kapsam ve zorluk dengesi taşır (kullanıcı 20'şer çözer).
- Aynı kök kalıbı + aynı çözüm + aynı çeldirici mantığı seri üretimde kullanılmaz.

### Ders bazlı gerçek sınav profili

Her derse tek bir “ideal soru” kalıbı uygulanmaz. 2026'nın 260 sorusundan ölçülen
profil üretim matrisinin başlangıç noktasıdır:

| Alan | Medyan kök | Olumsuz kök | Öncüllü | Sayısal senaryo |
|---|---:|---:|---:|---:|
| İlk 30 soru | 109 karakter | %6,7 | %1,7 | düşük/değişken |
| Finansal muhasebe + standartlar | 295 | %9,6 | %3,8 | %57,7 |
| Maliyet Muhasebesi | 482 | %12,5 | %0 | %100 |
| Mali Tablolar Analizi | 228 | %0 | %0 | %81,2 |
| Denetim | 212 | %46,9 | %12,5 | düşük |
| Ekonomi + Maliye | 216 | %12,5 | %16,7 | %8,3 |
| Hukuk | **257** | **%41,5** | %14,3 | düşük |

⚠️ **Hukuk bandı 2026-08-13'te yeniden ölçüldü.** Eski satır (175 / %48,3 / %20)
yalnız 2026'nın 30 hukuk sorusuna dayanıyordu ve örneklem çok küçüktü. Yeni bant
**2014–2026 arşivinden çıkarılan 629 gerçek hukuk sorusuna** dayanır.

### 🔴 Hukuk: gerçek sınav sorusu tanım sormaz, kural uygular

Bu ders ailesinin kalite açığı biçimsel değil **yapısaldır** — 2026-08-13 ölçümü:

| Ölçüt | Gerçek sınav (629 soru) | Havuzumuz (2040 soru) |
|---|---:|---:|
| Medyan kök | **257 karakter** | 109 (2,4× kısa) |
| Olumsuz kök | **%41,5** | %2,4 (17× az) |
| Düz tanım sorusu | **%6,2** | %30,2 (5× fazla) |
| Olay örgülü kök (tarih/tutar/süre) | **%16,2** | %5,8 |
| 257 karakteri aşan kök | **%50** | %6,2 |
| Öncüllü | %14,3 | %10,9 ✅ |

Gerçek hukuk kökü ortalama **3,5 cümledir** ve şu iskeleti taşır:

> **kural veya olay anlatımı** → (çoğu kez I-II-III öncül listesi) →
> **"Buna göre …"** köprüsü (uzun köklerin %33'ünde) → **olumsuz soru** (%29-41)

Uzun köklerin içinde ölçülen somut veri: tutar %24,2 · tarih %15,9 · süre %6,4.

**Yasak refleks:** "X nedir?" / "X'in tanımı aşağıdakilerden hangisidir?".
Aday tek kavramı tanıyınca soruyu bitirir; gerçek sınav beş seçeneğin
**hepsinin** hukuki sonucunu bilmeyi ister. Doğru form, kuralı olaya uygulatmak
ve çoğunlukla "hangisi **yanlıştır**" diye sormaktır.

⚠️ Kökü uzatmak **dolgu eklemek değildir**: eklenen her cümle ya olayın hukuken
anlamlı bir unsurunu (taraf, tarih, süre, tutar, sıfat) ya da uygulanacak kuralı
taşır. Gereksiz betimleme (§4) ve atıf (“yukarıdaki işletme…”, Karışık Test
karıştırdığı için yasak) eklenmez.

Bu yüzdeler paket başına katı kota değildir; 2026 biçimini gösteren kalibrasyon
bandıdır. Son üç yıl ana ağırlık, eski sınavlar konu sürekliliği kontrolüdür.

#### Hukuk için bilişsel zorluk kapısı

Kökün uzun olması veya olumsuz kurulması soruyu kendiliğinden zorlaştırmaz. Uzun bir
senaryonun sonunda yalnız “4/1-(a) nedir?” soruluyorsa soru hâlâ tek bilgi tanımayla
çözülür. Gerçek sınav düzeyi ayrıca **kaç hükmün birlikte işletildiği** ve yanlış
seçeneklerin ne kadar yakın hukuki ayrımlara dayandığı üzerinden denetlenir.

Her hukuk sorusu üretim matrisinde şu bilişsel sınıflardan biriyle işaretlenir:

| Düzey | Ölçülen işlem | Kullanım |
|---|---|---|
| 0 — tanıma | Tek tanımı/kurumu/kanunu hatırlama | Yalnız öğretici ısınma; paketin en fazla %10'u |
| 1 — tek kural uygulama | Bir olaya tek süre, statü, yasak veya şart uygulama | Paketin en fazla %30'u |
| 2 — çoklu ayrım | Beş yakın hükmü karşılaştırma veya en az iki koşulu birlikte değerlendirme | Paketin omurgası; en az %40 |
| 3 — bütünleşik olay | İstisna + süre/statü/sonuç zinciri ya da birden çok taraf/işlem | En az %20 |

Hedef dağılım mekanik bir soru kotası değil, **kolay soruya yığılmayı durduran teslim
kapısıdır**: 60 soruluk hukuk paketinde düzey 0 en çok 6, düzey 0+1 birlikte en çok
24 soru olmalıdır. Her 20 soruluk test kendi içinde en az 8 düzey-2 ve en az 4
düzey-3 soru taşımalıdır. Bir paket bu ölçümü yapmadan “gerçek sınava kalibre” diye
raporlanmaz.

Zorluk şu yollarla artırılır:

- aynı olayda statü + bildirim + hukuki sonuç gibi iki veya daha çok hükmü işletmek,
- her seçeneği ayrı ve makul bir hukuki önerme olarak kurmak,
- süre/oran/eşik bilgisini olayın diğer koşullarıyla birlikte değerlendirtmek,
- ana kural ile istisnayı aynı soruda ayırt ettirmek,
- birbirine yakın kurum, dava yolu, sorumluluk veya sigorta kolunu karşılaştırmak.

**Yasak sahte zorluk:** gereksiz isim/tarih/tutar eklemek, cümleyi uzatmak, iki
olumsuzluk kullanmak, mevzuat dışı ayrıntıyla adayı yormak veya çeldiriciyi açıkça
saçmalaştırmak. Zor soru daha uzun olduğu için değil, doğru sonuca ulaşmak için daha
fazla doğru hukuki ayrım gerektiği için zordur.

- Finansal muhasebe: kayıt, hesap kodu, işlem zinciri ve çok verili senaryo bulunur.
- Maliyet ve mali tablolar: hesap/tablo soruları paketin omurgasıdır; yalnız tanım
  sorularıyla 60'a tamamlanmaz.
- Denetim ve hukuk: olumsuz kök gerçek sınavın doğal parçasıdır. Genel bir “olumsuz
  kökü azalt” hedefi konmaz; kök açık ve tek anlamlı tutulur.
- Matematik: kısa kök tek başına kalite kusuru değildir. Formül, fonksiyon, limit,
  türev, seri ve analitik geometri gibi gösterimin içerdiği bilişsel yük hesaba
  katılır.
- Yabancı dil: kısa cümle tamamlama ve kelime sorusu doğaldır; yapay öykü eklenmez.

### Konu açma önceliği

Yeni konu yalnız “müfredatta adı var” diye açılmaz. Üç ölçüm birlikte yapılır:

1. son üç sınavdaki görünürlük,
2. 2014–2026 arşivindeki tekrar/frekans,
3. mevcut havuzun gerçekten kapsayıp kapsamadığı.

2026-07-22 denetiminde öncelikli açıklar: ileri matematik, muhasebe bilgi sistemleri,
diğer güncel TMS/TFRS ve sürdürülebilirlik raporlamasıdır. Nadir her standarda ayrı
60 soru açmak yerine sınav ağırlığını bozmayacak birleşik konu paketi değerlendirilir.

### Alıştırma ↔ klon ayrımı (denetimli)

`audit.py::tekrar_sorunlari` bunu ölçer ve ayrım **ham cevap** üzerinden kurulur:

| durum | hüküm |
|---|---|
| aynı şablon + **farklı** cevap | **alıştırma** — mekanik beceride istenen şeydir; matematikte 52 denklem sorusu meşrudur |
| aynı şablon + **aynı** cevap | **FATAL klon** — sayı değişmiş ama sorulan işlem ve sonuç aynı |

Gerçek örnek: `trend_analizi`'nde 260/200, 1300/1000 ve 780/600 → **üçü de %130**.
Aday birini çözünce diğer ikisini tanır; bu üç soru değil, bir sorudur.

⚠️ SMMM'nin denetimindeki "aynı şablon = FATAL" kuralı SGS'ye **olduğu gibi
alınamaz** — sayılar maskelendiğinde matematik alıştırmasının kökü zaten şablondur.

Ayrıca ölçülür: çözüm birebir tekrarı (FATAL), yalnız sayı değişmiş çözüm şablonu
(UYARI) ve `difflib` yakın-tekrar (UYARI, elle karşılaştırılır).

---

## 3. Builder kullan; JSON'u elle yazma

Sorular doğrudan JSON'a yazılmaz. Her konu için
`tools/sgs/builders/build_<konu>.py` oluşturulur. Böylece doğru metin, harf ataması,
şıklar, çözüm ve kaynak **tek geçişte birlikte** üretilir; harf permütasyonu ile çözüm
metni birbirinden ayrı düşemez.

```python
Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

def gen_letters(n, seed):
    """Seed'li DENGELİ KARIŞIM — rotasyon değil (bkz. §6)."""
    r = random.Random(seed)
    base = ["ABCDE"[i % 5] for i in range(n)]
    while True:
        r.shuffle(base)
        if all(not (base[i] == base[i-1] == base[i-2]) for i in range(2, len(base))):
            return base

# emit: opts = {ans: correct} + çeldiriciler kalan harflere
#       assert len(set(opts.values())) == 5      # şık tekrarı yok
```

**Builder assertion'ları gerçek hata bulur, süs değildir.** Muhasebe Standartları
üretiminde `correct not in distractors` beş ayrı çeldirici çakışması yakaladı — farklı
formüllerin tesadüfen aynı sayıyı vermesi. Bir konuda assertion daha derin bir kusuru
açığa çıkardı: seçilen sayılarla ağırlıklı ortalama (%9,6) ve basit ortalama (%10)
aynı değere yuvarlanıyordu, yani soru öğretmek istediği ayrımı yok ediyordu. Sayılar
`assert agirlikli != basit` eklenerek yeniden seçildi.

Builder'ın sonunda §5–§7 ölçütleri assert'lenir; §7'deki öncül dağılımı assert'i
TMS 10'da elle yakaladığım kusuru kendiliğinden yakaladı.

### 🔴 Her sorunun TEK sahibi olur — devralınca eski bloğu çıkar

Bir paket baştan yazıldığında, o paketin sorularını tutan **eski bakım
builder'larının blokları çıkarılır**. Aksi hâlde iki builder aynı metne yazar,
`--check` sıraya bağımlı hâle gelir ve eski builder yenisinin üstüne yazabilir.

Devralmadan önce sahiplik taranır:

```bash
grep -ln "<paket_adı>\|<id_öneki>-gen-" tools/sgs/builders/*.py
```

Hukuk paketlerinde tipik sahipler: `build_legal_oncul_cleanup` (paket başına bir
öncüllü soru), `fix_meslek_length_quality` / `fix_*_length_quality`,
`build_option_balance_cleanup`, `fix_bekleyen_denge`, `fix_lexical_tell`.

### 🔴 `--check` desteklemeyen builder ARGÜMANI YOK SAYIP YAZAR

`tools/sgs/builders/` altındaki builder'ların bir kısmı argparse kullanmaz;
`if __name__ == "__main__":` bloğunda doğrudan yazar. Bunları `--check` ile
çağırmak **doğrulama değildir** — argüman sessizce yok sayılır ve dosya
üzerine yazılır.

**2026-08-14'te bu gerçekleşti:** beş bakım builder'ı `--check` ile çağıran bir
döngü, `fix_meslek_length_quality`'nin argümanı yok saymasıyla yayınlanmış
`meslek_orgutu_disiplin.json` içeriğinin 6 şıkkını eski hâline geri yazdı. Hasar
`git diff` ile görüldü ve `git checkout` ile onarıldı.

Toplu doğrulama döngüsü **yalnız** şu koşulu sağlayanları çalıştırır:

```bash
grep -l 'args.check' tools/sgs/builders/*.py
```

⚠️ İki yanıltıcı desen var: `add_argument("--check")` fazla dardır (argparse
çağrısı çok satıra bölünmüş olabilir), `"--check"` ise fazla geniştir — koruma
metninde bu dizeyi taşıyan builder'ları da yakalar. Ölçüt **`args.check`
kullanımıdır**; onu kullanan builder gerçekten doğrulama yapıyordur.

Desteklemeyen builder'lara, argümanla çağrıldığında yazmadan çıkan bir koruma
eklenir (`fix_meslek_length_quality` örneği).

---

## 4. Soru kökü standardı

- Soru tek, açık ve tartışmasız bir görev ister.
- Çözüm için gereken bütün veri kökte bulunur. ⚠️ Bir soruda kökte "bugünkü değer
  faktörü 2,4869" verilip cevap tam iskontoyla hesaplanmıştı; kökü izleyen aday
  cevabı bulamıyordu. **Kök hangi veriyi veriyorsa hesap ondan yürür.**
- Gereksiz öykü ve yapay uzunluk eklenmez; ama çıplak tanım sorularına da yığılma
  yapılmaz — SGS uygulama ve yorum ölçer.
- "Hangisi doğrudur?" gibi jenerik kök kullanılabilir; ayırt edici içerik o zaman
  seçeneklerde bulunur.
- Olumsuz kök yalnız dersin doğası ve ölçülmüş sınav profili gerektiriyorsa kullanılır
  (§1'deki TMS 21 örneği). `değildir` / `yanlıştır` görünür ve tek anlamlı olur.
- Bir soruda iki olumsuzluk veya cevabı etkileyen eksik varsayım bulunmaz.

---

## 5. Şıklar ve doğru cevap sızıntısını önleme

> Bu bölüm bu deponun en pahalı dersidir. 2026-07-17'de ölçüldüğünde SGS havuzunun
> **%37'si soru okunmadan çözülebiliyordu** ve 102 dosyanın 53'ü eşiği aşıyordu.
> Ayrıntı: `tools/sgs/SIK_ORUNTUSU_RAPORU.md`.

### Temel ilke

**Doğru cevap kısa ya da uzun olacak diye yazılmaz.** Beş seçenek aynı dilbilgisel
yapıda, aynı kavramsal düzeyde ve doğal uzunlukta olur. Doğru cevabın uzunluk sırası
paket boyunca farklı konumlara dağılır.

- Doğru şık sürekli en kısa **veya** en uzun olamaz. **Yön önemsizdir.**
- Olumsuz kökte de doğru şık (yanlış ifade) uzunluk/ayrıntı bakımından ayrılmaz.
- Seçenekler aynı kategoriye ait olur: hesap adıyla süre, kurumla yaptırım veya
  oranla tanım karıştırılmaz.
- Dilbilgisel uyum, noktalama, birim, kesinlik düzeyi ipucu vermez.
- "Her zaman", "yalnızca", "kesinlikle" gibi mutlak ifadeler yalnız yanlış şıklara
  serpiştirilmez.
- Beş seçenek birbirinden farklıdır ve yalnız biri tam doğrudur.

### Kör öğrenci ölçütü

`audit.py::kor_ogrenci`, soruyu **hiç okumayan** bir adayın yalnız şık biçimine
bakarak alabildiği en yüksek puanı ölçer. **Altı strateji**, her biri bir aday kümesi
döndürür; puan = küme doğruyu içeriyorsa 1/|küme|:

1. en kısayı seç · 2. en uzunu seç · 3. işaretliyi ele + en kısayı seç ·
4. işaretliyi ele + en uzunu seç · 5. iki ucu ele, ortadan tahmin et ·
6. **işaretliyi ele, kalandan tahmin et** (2026-07-28 eklendi)

"İşaretli" = `audit.py::ELEME_ISARETI` (mutlak dil kalıpları). 3 ve 4 numaralı
stratejiler eskiden yalnız dar bir dolgu kümesi kullanıyordu; 2026-07-28'de aynı
geniş kümeye taşındılar.

| | |
|---|---|
| **Taban** | ~%24 (en iyi strateji alındığı için %20 değil) |
| **Kalite hedefi** | **≤%30** — paketler eşiğe değil buraya kadar temizlenir |
| **UYARI** | ≥%32 (null modelin 95. yüzdeliği %31) |
| **FATAL** | ≥%36 (99. yüzdelik %35) |

⚠️ Eşikler 2026-07-28'de 31/35 → **32/36** oldu. **Bu bir gevşetme değildir:** eleme
adımı geniş kümeye taşınınca ölçüt güçlendi ve rastgele tabanı da birlikte yükseldi
(95. yüzdelik %30 → %31). Eşik sabit bırakılsaydı kusursuz paketlerin %5'i boşuna
uyarı alırdı. Eşiğin anlamı sabittir: "rastgeleden ayırt edilebilir". Kalite hedefi
ayrı ve daha sıkıdır.

Eşikler **null modelle** kalibre edilir: gerçek şık metinleri kullanılıp doğru cevap
rastgele atanır (boy ve sözcük dağılımı gerçekçi kalır, gerçek sinyal kalmaz), 60
soruluk 400 paket. ⚠️ **Strateji eklendiğinde kalibrasyon yenilenir** — daha çok
stratejinin en iyisini almak tabanı yükseltir.

Alt ölçüt: doğru şık en-uzun ~%20 **ve** en-kısa ~%20 (`boy_egilimi`).

Temiz örnek: hesap ağırlıklı dersler (`finansal_muhasebe` %19, `matematik` %17) —
şıklar sayı olduğu için biçim ipucu doğmaz.

### ⭐ Boy dağılımını ÜRETİMDEN ÖNCE ölç (zorunlu adım)

`audit.py` boy tuzağını **üretimden sonra** yakalar; o noktada düzeltme, yazılmış
60 sorunun yeniden elden geçirilmesi demektir. Aynı hata dört turda üst üste
tekrarlandı — `diger_guncel_standartlar` sıfırdan üretimde kör **%66**, `tms_16`
temizlik sonrası %28→**%45**, `tms_21` %30→**%43**, leksik temizlik havuz genelinde
%26→**%45**. Bu artık tesadüf değil, **öngörülebilir bir refleks**: doğru şıkkı
açıklayıcı, çeldiricileri terse yazmak.

Bu yüzden yamalar önce **ayrı bir tasarım modülünde** yazılır ve şu ölçü alınır:

```python
def boy_denetimi(P, esik=1/3):
    """Doğru şık kaç yamada TEK-EN-UZUN? Üçte biri aşarsa üretimi DURDUR."""
    tek_uzun = [q for q, f in P.items()
                if len(f["correct"]) > max(len(x) for x in f["distractors"])]
    if len(tek_uzun) / len(P) > esik:
        raise SystemExit("§5 BOY TUZAĞI: çeldiricilere gerçek içerik ekle")
```

`tms_36` turunda bu kontrol ilk tasarımda **19/28 (%68)** ölçtü ve üretimi durdurdu;
çeldiricilere gerçek içerik eklendikten sonra 2/28 (%7) oldu ve paket ilk denetimde
FATAL 0 / UYARI 0, kör %24 (rastgele taban) ile geçti — hiç yeniden çalışma olmadan.

**Üç yönlü tuzak.** Tek bir yönü kapatmak yenisini açar:

| Refleks | Doğan tell |
|---|---|
| Yanlış ifadeyi gerekçeli yaz | "en uzunu seç" |
| Hepsini kısalt | "en kısayı seç" |
| Hepsini ortala | "iki ucu ele, ortadan tahmin et" |

Doğrusu **dağılımdır**: doğru şık bazen en uzun, bazen en kısa, çoğunlukla arada.
`tms_36`'da ulaşılan dağılım — en uzun 9 · 2. 23 · 3. 13 · 4. 6 · en kısa 9.

⚠️ **Çare doğru şıkkı kısaltmak değil, çeldiriciye gerçek içerik eklemektir** —
yanlış iddianın kendi sonucunu yazdır ("…kaydedilir **ve varlık 455.000 ₺'ye
indirilir**"). Mekanik kısaltma boyu düzeltir, bilgiyi götürür.

#### 🔴 "Hangisi yanlıştır" kalıbı doğru şıkkı EN KISA yapar

Hukuk turunda §1 için olumsuz kök oranı yükseltilirken tuzağın **ters ucu** açıldı:
"hangisi yanlıştır" sorusunda doğru şık *yanlış* ifadedir; yanlış ifade tek cümlelik
bir iddia, dört çeldirici ise gerekçeli doğru kurallardır. Sonuç sistematik olarak
"en kısayı seç". `limited_sahis_sirketleri`'nde 23 soru olumsuz köke çevrilince
en-kısa **25/60** oldu ve audit FATAL verdi (kör %38).

Bu yüzden tasarım modülünde **iki yön birlikte** ölçülür:

```python
uzun = [q for q, f in P.items() if len(f["correct"]) >= max(len(x) for x in f["distractors"])]
kisa = [q for q, f in P.items() if len(f["correct"]) <= min(len(x) for x in f["distractors"])]
```

⚠️ **Düzeltirken tek yöne yüklenme.** Aynı pakette 16 doğru şık genişletilince
en-kısa 25→6 indi ama en-uzun 13→**28**'e fırladı; bir FATAL'ı diğeriyle
değiştirmiş olduk. İşe yarayan çözüm: doğru şık genişletildikten sonra **her
soruda BİR çeldiriciye** gerçek içerik eklemek → 14 uzun / 6 kısa, kör %23.

⚠️ **Öncüllü sorularda seçicinin kendisi boy tell'idir.** `"I ve II"` (7 karakter)
her seçici kümesinin en kısasıdır; doğru seçici hep o olursa aday soruyu okumadan
en kısa seçiciyi işaretler. Doğru seçiciyi `Yalnız III` (10), `II ve III` (9) ve
`I ve III` (8) arasında dağıt; `I, II ve III` (12) ise kümenin en uzunudur.

### 🔴 Yasak: mutlak dil (eleme ipucu)

Yanlış bir iddiayı "her hâlde / hiçbir biçimde / …mak zorundadır" diye yazmak doğal bir
reflekstir, ama 60 soru boyunca sürdürülünce bu sözcükler **"ben yanlış şıkım" rozetine**
dönüşür: aday onları eleyip kalandan seçer. Boy ölçen stratejiler bunu göremez; altıncı
strateji bunun içindir.

**Bu bir üslup tercihi değil, ev artefaktıdır — ölçüldü.** 2014-2026 arşivinden çıkarılan
**12.436 gerçek sınav şıkkında**: `hiçbir` %0,2 · `her hâlde` %0,0 · `zorunda` %0,0 ·
`ifade eder` %0,0 · `niteliğinde` %0,1. Bizim havuzda ~%9'du. 2026-07-28 temizliğinden
önce 11 paket bu ölçütten FATAL alıyordu (%35-42, çoğu `muhasebe_standartlari`).

İşaret kümesi `audit.py::ELEME_ISARETI`. **Anlamın parçası olan kullanımlar hariç:**
`hiçbir istisna`, `hiçbir fark`, `hiçbir etkisi` — bunlar iddianın kendisidir.

⚠️ Temizlerken **doğru şıkkı kısaltma**: dolgu kaldırılınca çeldirici ~15 karakter
kısalır ve doğru şık sistematik en uzun kalır (ölçüldü: kör %26→%45). Çare
**çeldiriciye gerçek içerik eklemek** — yanlış iddianın kendi mantıksal sonucu. Ama
adayların TAMAMINI uygulama: o zaman doğru şık ORTADA kalır ve 5. strateji öne geçer.
Kör'ü en aza indiren **alt küme** ölçümle seçilir (`fix_bekleyen_denge.py` bunu yapar).

### 🔴 Yasak: dolguyla uzatma

Çeldiriciyi hacim kazansın diye kalıp cümleyle şişirme
("…zorunda bulunmaktadır", "…ifade etmek durumundadır", "…niteliğinde bulunmaktadır").

**Neden yasak:** dolgu doğru şıkta hiç geçmediği için kalıbın kendisi %100 güvenilir
bir "yanlış" işaretine dönüşür — ipucu boydan **üsluba** taşınır ve keskinleşir.
`muhasebe_standartlari`'nda çeldiricilerin %37'si (bazı dosyada %61) dolgu taşıyor,
doğru şıkların %0'ı; kör öğrenci %52, TMS 10'da %81.

Bu kusur, "doğru şıkkı kısa + çeldiricileri uzun yaz" diye benimsenmiş bir kuraldan
doğdu. O kural **geri alınmıştır**; length-tell'i susturuyor ama yerine daha kötüsünü
koyuyordu.

### 🔴 Yasak: atma-şıkkı tekrarı

"Bu husus standartta düzenlenmemiş olup işletmenin takdirine bırakılmıştır" gibi
doldurma şıkkını tekrar tekrar kullanma. Her seferinde yanlış olduğu için tek başına
öğrenilir; tek dosyada 24-33 kez geçtiği ölçüldü. `audit.py` aynı çeldiricinin
dosya içi tekrarını sayar (öncül seçicileri — "Yalnız I", "II ve III" — hariç).

### Çeldirici standardı

Her çeldirici, doğru şıkla **aynı registerde, kısa ve iddialı** olur — gerçekten
savunulabilir ama yanlış bir önerme. Dolgu değil, içerik. Her biri:

- konuya ait gerçek bir kavram yanılgısını,
- hesap sorusunda makul ve belgelenebilir bir işlem hatasını,
- mevzuat sorusunda yakın fakat farklı bir yetki, süre veya şartı,
- kayıt sorusunda makul bir hesap/taraf/borç-alacak hatasını

temsil eder. Rastgele sayı, alakasız kurum ve açıkça saçma ifade kullanılmaz.

⚠️ Eşiği geçmek için anlamsız kelime eklemek, soruyu yapay uzatmak veya her şıkkı
aynı karakter sayısına getirmek **ayrıca kalite ihlalidir**. Ölçüt mekanik kusuru
yakalamak içindir; amaç doğal ve dengeli şık yazmaktır.

---

## 6. Cevap harfleri

- Harfler **seed'li ve örüntüsüz** karıştırılır (`gen_letters`, §3).
- `ABCDEABCDE…`, sabit adım ve kısa periyot **FATAL**.
- Dengeli dağılım, **tam eşit dağılım** demek değildir. Örneğin 60 soruda
  `13-13-12-11-11` gibi küçük sapmalar doğaldır; sırf her harf 12 kez çıksın diye
  cevapların yeri mekanik biçimde değiştirilmez.
- Belirgin bir harf yığılması olmamalı; aynı harf üç kez art arda gelmez.

⚠️ **"12'şer + run≤2" yetmez.** Bir üretimde 240 sorunun harf dizisi birebir
`ABCDEABCDE…` rotasyonuydu ve o günkü dedektör bunu onaylıyordu (run=1 olduğu için).
Rastgeleden beterdir: 10 soru çözen aday örüntüyü görüp gerisini okumadan işaretler.
`audit.py::letter_pattern` artık sabit adımlı rotasyona ve kısa periyoda bakar.

---

## 7. Öncüllü ve olumsuz köklü sorular

Öncüllü soru kota doldurmak için üretilmez; konu birden çok hükmü birlikte
sınıflandırmayı gerektiriyorsa kullanılır.

- Öncüller **`\n\n`** ile ayrılır. Tek `\n` markdown'da satır başı yapmaz.
- **Doğru kombinasyon aynı kalıba yığılmaz.** Tek bir cevap ("I ve II" gibi)
  öncüllülerin %40'ını aşmamalıdır — builder'da assert'le. TMS 10'da 10 öncüllünün
  9'u "I ve II" çıkmıştı; bu, "hepsi" yığılmasından daha keskin bir ipucudur.
- "Hepsi" (`I, II ve III`) ~%20 civarında tutulur; ne %75'e yığılır ne sıfırlanır.
  Sık sık bir öncülü kesin yanlış yaparak alt-küme cevap üret.
- Kombinasyon seçenekleri çakışmaz; doğru küme seçeneklerde tam olarak bulunur.
- Bir öncül yalnız dilinden veya uzunluğundan yanlış anlaşılan tuzak olmaz.

⚠️ Öncüllü soruları taramada şıkları **tam-eşleme yapma** — parantez son-eki olabilir
("… (her üç ifade de doğrudur)"). `(...)` at, Roman rakamı kümesini karşılaştır.

Olumsuz kökte doğru seçenek yanlış ifadeyi taşır; diğer dördünden uzunluk, ayrıntı
veya dil bakımından ayrılmaz (§5).

---

## 8. Hesap ve yevmiye soruları

### Hesap

- Bütün ara sonuçlar builder içinde hesaplanır ve **builder'dan bağımsız** olarak
  ikinci kez doğrulanır. ⚠️ Bu doğrulamada iki kez benim hesabım yanlış çıktı,
  builder'ınki doğruydu — uyuşmazlıkta ikisini de elle kontrol et, birine güvenme.
- Doğru sonuç tek olmalı; aynı değeri veren iki seçenek bulunmamalı.
- Yuvarlama yöntemi kökte belirtilir veya mevzuattaki yönteme dayanır.
- Çeldiriciler belgelenebilir hata sonuçlarıdır (yön hatası, eksik kıst, ters oran).

### Yevmiye

- Hesap kodu ve adı Tekdüzen Hesap Planına uygun olur; ₺ sembolü kullanılır.
- Borç ve alacak toplamları builder assertion'ı ile eşitlenir.
- KDV ve diğer oranlar senaryoda verilir (§9).

### Tablo, formül ve uygulamada görünüm

Gerçek kitapçık; çok satırlı yevmiye seçenekleri, borç/alacak sütunları, maliyet ve
stok tabloları, öncüller, fonksiyonlar ve matematiksel gösterimler kullanır.

- Kullanıcıya ham kod çiti (örneğin üç ters tırnakla başlayan `text` etiketi),
  kaçış karakteri veya üretim etiketi
  gösterilmez.
- Çok satırlı seçenekler uygulamanın desteklediği düz metin/Markdown biçiminde
  yazılır; builder çıktısı gerçek cihazda en az bir kez açılır.
- Borç/alacak hizası yalnız boşluk sayısına güvenmez; dar iPhone ekranında da anlam
  kaybolmamalıdır.
- Matematik ifadesi PDF'den kopyalanmış bozuk glif olarak değil, uygulamanın
  desteklediği tutarlı gösterimle yazılır.
- Yeni görsel biçim OTA'ya girmeden önce küçük ve büyük ekran render kontrolünden
  geçer.

---

## 9. Mevzuat ve standart güncelliği

Her sorunun doğru cevabı üretim tarihinde birincil kaynaktan doğrulanır. Kaynak
önceliği: Resmî Gazete / Mevzuat Bilgi Sistemi → KGK'nın yürürlükteki TMS/TFRS seti →
TESMER, TÜRMOB, SPK resmî metinleri → ikincil kaynak (yalnız açıklama; doğru cevabın
tek dayanağı olamaz).

`source.legislationRef` genel başlık değil, madde/paragraf düzeyinde olur:
`TMS 2 par. 16`, `6102 sayılı TTK m. 124`.

### Sayısal mevzuat bilgisi: süre, ceza, oran ve tutar

Gerçek kullanıcı geri bildirimi ve çıkmış sorular birlikte gösteriyor: SGS yalnız
“ilgili mevzuata göre işlem yapılır” düzeyinde kavram sormaz; mevzuattaki **süreyi,
cezayı, artırım oranını, sınırı ve sayısal sonucu doğrudan** da sorar. Bu nedenle
sayısal mevzuat sorusu yasak değildir.

Üç ayrı sınıf kullanılır:

1. **Yapısal/sabit sayı:** kanundaki süre, ortak sayısı, başvuru koşulu, ceza türü
   veya kalıcı oran. Doğrudan sorulabilir; madde/fıkra düzeyinde doğrulanır.
2. **Dönemsel/değişken sayı:** vergi oranı, tarife, istisna haddi, parasal sınır,
   yeniden değerleme veya artırım oranı. Gerçek sınav profili gerektiriyorsa
   doğrudan sorulabilir; `validYear` zorunludur, birincil kaynak ve yürürlük tarihi
   kaydedilir, her OTA öncesi güncellik listesinde yeniden kontrol edilir.
3. **Senaryoda verilen sayı:** “5.000 ₺ + %20 KDV” gibi oran/tutar kökte veriliyorsa
   ölçülen şey kayıt veya hesap becerisidir; mevzuat ezberi değildir ve serbesttir.

#### Sayısal mevzuat sorusunun zorunlu kayıtları

- `validYear` sınav yılıyla aynı olmalı.
- `source.legislationRef` madde/fıkra/karar düzeyinde olmalı.
- Dönemsel veride mümkünse yürürlük tarihi veya karar/tebliğ numarası bulunmalı.
- Çözüm yalnız sayıyı tekrarlamamalı; sayının hangi koşulda uygulandığını açıklamalı.
- Değişken sayı eskiyince soru sessizce kalmamalı: güncellenir veya havuzdan çekilir.

“Yürürlükteki oran” deyip hangi yılın kastedildiğini belirsiz bırakmak yasaktır.
Ancak uygulama yalnız güncel yıl havuzunu sunuyorsa, kökte her seferinde “2026 yılı
itibarıyla” yazmak zorunlu değildir; `validYear` ve yayın öncesi güncellik kontrolü
bu bağı kurar.

⚠️ **Cevabın oran olması tek başına değişken mevzuat demek değildir:** faydalı ömürden
türetilen amortisman oranı, TDHP'nin yapısal sahiplik sınırı ve “cari oran” adlı
finansal rasyo ayrı değerlendirilir. Denetim yalnız mekanik riskleri yakalar;
nihai ayrım insan incelemesidir.

### Güncellik kontrol listesi

Her OTA öncesi oran, süre, ceza, parasal had ve yaptırım içeren sorular ayrıca
taranır. Kaynak metin değişmişse yalnız doğru şık değil; çeldiriciler ve çözüm de
yeniden doğrulanır. “Cevap hâlâ aynı” olması tek başına güncellik onayı değildir.

---

## 10. Çözüm standardı

Çözüm:

- doğru ilke, işlem veya maddeyi açıklar,
- hesap sorusunda ara adımları gösterir,
- gerektiğinde yakın çeldiricinin **neden** yanlış olduğunu ayırt eder,
- soru ve şıklardaki bilgiyi aynen tekrar etmekle yetinmez,
- başka bir çözümün sayı/kelime değiştirilmiş kopyası olmaz,
- yer tutucu, yarım cümle veya `Demo açıklama` içermez.

### Harf atfı

**Hedef: çözüm harf atfı içermez** ("Doğru cevap C." yazma); doğru cevabı içerik
üzerinden açıklar. Harf atfı, çözümü şık harflerine kırılgan biçimde bağlar: harf
ataması sonradan değişince çözüm sessizce yanlış kalır. Bir konuda tam **46 soruda**
böyle olmuştu; örnek soru okunurken fark edildi.

Mevcut durum: SGS havuzundaki 6120 çözümün **2040'ı harf atıflı, 4080'i harfsiz**
(uyumsuz 0). Yani içeriğin üçte ikisi zaten hedefe uygun. Kalan 2040'ın atfı içerik
düzeltme oturumunda temizlenecek.

O güne kadar: atıf varsa **tutarlı olmak zorundadır** — `audit.py` uyumsuzluğu FATAL
verir. Builder harf atamasını ve çözüm harfini **tek geçişte** üretmelidir (§3);
sonradan yamamak bu hatayı üreten yoldur.

⚠️ Uyumu tararken regex'i `re.I` ile kurma — "Doğru seçenek **bu** nedenle…"
içindeki `b`'yi cevap harfi `B` sanar. Büyük harf + kelime sınırı ara.

---

## 11. Özgünlük ve telif

- TESMER kitapçığından veya üçüncü taraf soru bankasından kök, seçenek ya da çözüm
  **kopyalanmaz**; yakın türevi de üretilmez.
- Çıkmış sorular yalnız biçim, kapsam ve bilişsel düzey analizi için kullanılır (§1).
  Ölçülen kalıp taklit edilebilir; **metin taklit edilemez**.
- Kurgusal işletme ve özgün sayılar kullanılır.
- `source.kind` daima `generated`; bu etiket tek başına özgünlük kanıtı değildir.
- Kişisel kullanım için kitaptan telifli soru **kullanıcı sağlarsa** eklenebilir
  (`source.kind: "book"`). Codex hafızasından telifli soru üretmez.

---

## 12. Şema, manifest ve havuz

SGS şeması:

```json
{"id": "...", "ders": "...", "konu": "...", "stem": "...",
 "options": {"A": "...", "B": "...", "C": "...", "D": "...", "E": "..."},
 "answer": "C", "solution": "...",
 "source": {"kind": "generated", "styleRef": "...", "legislationRef": "..."},
 "validYear": 2026, "mockExamId": null}
```

- `ders` ve `konu`, uygulamadaki `assets/content/curriculum.json` ile eşleşir.
- Beş seçenek A–E eksiksiz; seçenek metinleri benzersiz; `answer` mevcut bir seçenek.
- `id` ve soru fikri paketler arasında da benzersiz.

⚠️ **`programIds` soru JSON'unda YOK** — manifest paket girdisinden gelir
(`content_repository.dart` → `Question.fromJson(programIds:)`). JSON'dan okumaya
çalışırsan doğrulaman yanlış olur (bu hataya düşüp 21 sahte uyumsuzluk raporlamıştım).

### Yeni konu bağlama

```bash
# 1. sgs.json'a paket girdisi ekle (konu akış sırasına göre)
# 2. birleşik manifesti ÜRET — elle düzenleme
python3 tools/shared/manifest_merge.py --write --version <N+1>
# 3. app'e kopyala + curriculum.json'a konuyu ekle
# 4. testlerdeki sayıları MANIFESTTEN ÖLÇEREK güncelle, tahmin etme
```

⚠️ **`content/manifest.json` (eski yol) asla değişmez** — App Store'daki canlı build
onu çeker. Yeni yol `content/v2/`.

⚠️ Manifest `version` alanı **string**'dir (`"105"`). `m["version"] + 1` TypeError
verir ve `json.dump`'tan **önce** patlar; dosya yazılmaz ama sonraki `diff` "aynı"
der ve seni yanlış yere güvendirir. `str(int(v) + 1)` kullan ve yazdıktan sonra
içeriği doğrula.

---

## 13. İnsan incelemesi

Yayımdan önce paketteki **her soru** en az bir kez içerik açısından okunur.
İnceleyen; tek doğru cevap bulunduğunu, çeldiricilerin makul fakat yanlış olduğunu,
dayanağın yürürlükte olduğunu, çözümün cevapla uyumlu olduğunu, sorunun konu sınırında
kaldığını ve zorluğun gerçek sınava uygun olduğunu onaylar.

### Gerçek aday geri bildirimi

Uygulamayı fiilen sınava hazırlanırken kullanan adayın geri bildirimi ayrı bir kalite
kapısıdır. “Çıkmış sınav doğrudan süre/ceza/artırım oranı soruyor, uygulama yalnız
genel mevzuat ifadesi soruyor” türü geri bildirim, kişisel üslup tercihi değil
**kapsam ve bilişsel düzey sapmasıdır**.

- Geri bildirim önce ilgili çıkmış sorularla doğrulanır.
- Doğrulanırsa tek soruyu yamamakla kalınmaz; aynı konu paketinin üretim matrisi
  gözden geçirilir.
- Aday geri bildirimi otomatik denetimden bağımsızdır. `FATAL 0`, gerçek sınavdan
  düşük veya farklı düzeyde soru yazıldığını göstermez.
- Yeni/yenilenen paketten en az bir 20 soruluk test, mümkünse gerçek bir aday
  tarafından cihazda çözülür; anlaşılmayan ifade, yapay çeldirici ve görünüm sorunu
  inceleme notuna kaydedilir.

---

## 14. Teslim kontrol listesi

### İçerik

- [ ] Konunun gerçek sınavdaki kalıbı çıkmış kâğıtlardan çıkarıldı (§1)
- [ ] Ders bazlı soru biçimi, 2026 kalibrasyon bandıyla karşılaştırıldı (§2)
- [ ] 3 test × 20 soru ve üretim matrisi tamamlandı
- [ ] Her soru özgün bir görev veya farklı bilişsel işlem ölçüyor
- [ ] Tek doğru cevap ve dört makul, dolgusuz çeldirici var (§5)
- [ ] Süre/ceza/oran/tutar soruları `validYear` ve birincil kaynakla güncel (§9)
- [ ] Hesaplar builder'dan **bağımsız** olarak ikinci kez doğrulandı (§8)
- [ ] Tablo, yevmiye ve formüller gerçek cihazda doğru görünüyor (§8)
- [ ] Çözümler özgün ve gerekçeli; harf atfı varsa cevapla tutarlı (§10)
- [ ] Gerçek aday geri bildirimi veya aday gözüyle 20 soruluk cihaz testi yapıldı (§13)

### Teknik

- [ ] `audit.py <paket>` → **FATAL 0**
- [ ] Kör öğrenci ~%20 (≥%35 FATAL) · boy ipucu iki yönde de ~%20 (§5)
- [ ] Öncüllerde tek cevap %40'ı aşmıyor; "hepsi" ~%20 (§7)
- [ ] Harf dizisi seed'li karışım, örüntüsüz (§6)
- [ ] `ders`/`konu` curriculum'da mevcut; `id`'ler benzersiz
- [ ] Builder, JSON ve `manifests/sgs.json` birlikte güncellendi; birleşik manifest
      `manifest_merge.py` ile üretildi (§12)
- [ ] OTA ve uygulama kopyaları özdeş; testlerdeki sayılar **ölçülerek** güncellendi
- [ ] `flutter analyze` + `flutter test` temiz
- [ ] İnsan incelemesi tamamlandı

Bu standarttaki sayısal eşikler, adayın fark edebileceği mekanik kusurları yakalamak
içindir. Eşiği geçmek amacıyla anlamsız kelime eklemek, soruyu yapay biçimde uzatmak
veya aynı fikri yüzeysel olarak yeniden yazmak ayrıca kalite ihlalidir.
