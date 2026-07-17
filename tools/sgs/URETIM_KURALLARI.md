# SGS Pratik — soru üretim ve kalite standardı

Bu belge yalnız **SMMM Staja Giriş Sınavı (SGS)** içindir ve Claude tarafından
geliştirilir. Amaç şemaya uyan JSON üretmek değil; **özgün, güncel, müfredata bağlı,
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

SGS tek oturumda **130 soru / 165 dakika**, her soru **A–E beş seçenekli**.

Ders dağılımı, 2026/1 kitapçığındaki soru sınırlarından ölçülmüştür
(`sgs_2026_1_lisans_a_grubu_ingilizce.pdf`) ve uygulamada
`lib/features/deneme/exam_blueprint.dart` içinde kodludur — ikisi birlikte değişir:

| Bölüm | Ders | Soru |
|---|---|---:|
| Genel Kültür | Türkçe · Matematik · Atatürk İlkeleri · Yabancı Dil | 7 · 8 · 5 · 10 |
| Muhasebe-Denetim | Finansal Muhasebe · Muhasebe Standartları · Maliyet · Mali Tablolar · Denetim | 20 · 6 · 8 · 8 · 16 |
| Ekonomi-Maliye | Ekonomi · Maliye | 6 · 6 |
| Hukuk | Meslek · İş ve Sosyal Güvenlik · Vergi · Ticaret · Borçlar | 6 · 6 · 6 · 6 · 6 |

Muhasebe Standartları, Finansal Muhasebe bloğunun içindedir (s. 49–54); ayrı bir
blok değildir. Blueprint'i değiştirirken `test/deneme_test.dart` içindeki
"130 soru, ders dağılımı blueprint ile birebir" testi işlevsel kanıttır.

### Çıkmış kâğıtların kullanımı

12 yıllık kitapçık `~/Desktop/sgs çıkmış sorular/` altındadır ve **yalnız konu
ağırlığı, dil ve zorluk kalibrasyonu** içindir (bkz. §11).

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
- **TMS 20** — 12 yılda **hiç sorulmamış**. Ders ağırlığı ölçülerek belirlenir,
  standart listesine bakarak değil.

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
bakarak alabildiği en yüksek puanı ölçer (dört strateji: en kısayı seç · en uzunu seç ·
dolgu kalıplılarını eleyip aynısı).

| | |
|---|---|
| **Hedef** | ~%20 (rastgele taban) |
| **UYARI** | ≥%28 |
| **FATAL** | ≥%35 |

Alt ölçüt: doğru şık en-uzun ~%20 **ve** en-kısa ~%20 (`boy_egilimi`).

Temiz örnek: hesap ağırlıklı dersler (`finansal_muhasebe` %19, `matematik` %17) —
şıklar sayı olduğu için biçim ipucu doğmaz.

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
- Dengeli dağılım amaçlanır; aynı harf üç kez art arda gelmez.

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

---

## 9. Mevzuat ve standart güncelliği

Her sorunun doğru cevabı üretim tarihinde birincil kaynaktan doğrulanır. Kaynak
önceliği: Resmî Gazete / Mevzuat Bilgi Sistemi → KGK'nın yürürlükteki TMS/TFRS seti →
TESMER, TÜRMOB, SPK resmî metinleri → ikincil kaynak (yalnız açıklama; doğru cevabın
tek dayanağı olamaz).

`source.legislationRef` genel başlık değil, madde/paragraf düzeyinde olur:
`TMS 2 par. 16`, `6102 sayılı TTK m. 124`.

### Değişken oran, tutar ve süreler

**Yıla bağlı oran/eşik/tutar sorma.** KDV oranı, gelir vergisi dilimleri, istisna
hadleri, asgari sermaye tutarları değişir → sorunun güncelliği sıfırlanır. Bunun
yerine kanunda sabit olan **yapısal-kavramsal** olanı sor: konu · mükellef · vergiyi
doğuran olay · istisna türü · matrah mantığı · beyan usulü.

⚠️ **İnce ayrım — oranın kökte verilmesi güvenlidir.** "5.000 ₺ + %20 KDV" ölçtüğü
şey kayıt becerisidir, oran bilgisi değil; oran değişse de soru kendi içinde tutarlı
kalır. İhlal olan iki durum:

1. cevap **çıplak bir mevzuat oranı** ve kök oranı vermiyor
   ("KDV oranı yüzde kaçtır?" → "%20"),
2. kök oranı vermeyip "yürürlükteki oran üzerinden" deyip adayın bilmesini beklemek.

⚠️⚠️ **Cevabın oran olması tek başına ihlal DEĞİLDİR.** Bu kuralda üç kez yanlış
pozitif ürettim; üçü de aynı hatanın çeşidiydi — kalıba bakıp anlama bakmamak:

- "Faydalı ömrü 4 yıl olanın amortisman oranı" → **%25** — türetilmiş orandır (1/4),
  mevzuat değişse bayatlamaz.
- "242 İştirakler'de sahiplik oranı" → **%10-50** — TDHP'nin yapısal sınırıdır.
- "**Cari oran** hangisiyle hesaplanır?" — "cari oran" *current ratio*'dur,
  bir rasyonun **adı**; "hâlihazırda geçerli oran" demek değildir. Bu kalıp Mali
  Tablolar Analizi'nin en temel terimini 10 kez ihlal sandı.

Denetim yalnız en bariz hâli yakalar (`guncellik_sorunlari`); ayrım semantiktir,
gerisi insan işidir.

Senaryoda varsayımsal tutar (10.000 ₺, 6.000 ₺) serbesttir. Kanunda sabit yapısal
sayılar da serbesttir (50 ortak, 3 yıl, 10 gün/1 ay ibraz süresi) — ama madde
değişikliğine karşı kaynakla doğrulanır.

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
  (`source.kind: "book"`). Claude hafızasından telifli soru üretmez.

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

---

## 14. Teslim kontrol listesi

### İçerik

- [ ] Konunun gerçek sınavdaki kalıbı çıkmış kâğıtlardan çıkarıldı (§1)
- [ ] 3 test × 20 soru ve üretim matrisi tamamlandı
- [ ] Her soru özgün bir görev veya farklı bilişsel işlem ölçüyor
- [ ] Tek doğru cevap ve dört makul, dolgusuz çeldirici var (§5)
- [ ] Yıla bağlı oran/tutar sorulmadı; kökteki oranlar meşru (§9)
- [ ] Hesaplar builder'dan **bağımsız** olarak ikinci kez doğrulandı (§8)
- [ ] Çözümler özgün ve gerekçeli; harf atfı varsa cevapla tutarlı (§10)

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
