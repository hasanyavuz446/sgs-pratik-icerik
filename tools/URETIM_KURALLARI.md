# SMMM Yeterlilik — soru üretim ve kalite standardı

Bu belge, SMMM Yeterlilik için üretilecek bölüm ve konu sorularının bağlayıcı
standardıdır. Amaç yalnızca şemaya uyan JSON üretmek değil; **özgün, güncel,
müfredata bağlı, tek doğru cevaplı ve gerçek sınavın düşünme biçimine yakın** bir
soru bankası oluşturmaktır.

Otomatik denetim alan uzmanı incelemesinin yerini tutmaz. Bir paketin yayıma hazır
sayılması için aşağıdaki üç kapının da geçilmesi gerekir:

1. Builder ve aritmetik kontrolleri,
2. Otomatik içerik denetimi,
3. Cevap, dayanak ve sınav uygunluğu için insan incelemesi.

## 0. Teslim kapısı

Yeni veya değiştirilen paket için:

```bash
python3 tools/audit.py content/yeterlilik/<dosya>.json
```

Manifestteki bütün Yeterlilik paketleriyle çapraz kontrol için:

```bash
python3 tools/audit.py --manifest content/v2/manifest.json
```

Konu paketi uygulama deposuna da kopyalandıysa:

```bash
python3 tools/verify_konu.py <dosya_adı>.json
```

- **FATAL:** Paket yayıma gidemez.
- **UYARI:** Ya düzeltilir ya da neden güvenli olduğu inceleme notuna yazılır.
- **BİLGİ:** Otomasyonun doğrulayamadığı, insan kontrolü isteyen içeriktir.

Yalnız `FATAL 0` görmek kalite onayı değildir. Denetim; mevzuat yorumunun doğruluğunu,
çeldiricilerin alan bilgisi bakımından makullüğünü veya bir sorunun gerçekten özgün
olduğunu tek başına kanıtlayamaz.

---

## 1. Resmî sınav sözleşmesi ve 2026 biçimi

14.01.2026 tarihli değişiklik işlenmiş TESMER yönergesine göre SMMM Yeterlilik:

- sekiz resmî sınav konusundan oluşur,
- her konu için ayrı **20 soruluk** sınav uygulanır,
- her soru **A–E olmak üzere beş seçeneklidir**,
- her dersin süresi **45 dakikadır**.

Birincil biçim kaynağı:
[TESMER 2026 Staj ve Sınavlara İlişkin Uygulama Yönergesi](https://www.tesmer.org.tr/wp-content/uploads/2026/01/TESMER-Staj-ve-Sinavlara-Iliskin-Uygulama-Yonergesi-2026.pdf)

### 2026/1 kitapçığı nasıl kullanılacak?

2026/1, yeni test biçimindeki ilk ve şu an için tek çıkmış dönemdir. Sekiz kitapçık
ve 160 soru çok değerlidir; ancak tek dönem olduğu için kesin ve kalıcı yüzde üretmez.

2026/1'de gözlenen belirgin biçim özellikleri şunlardır:

| Resmî ders | 2026/1'de gözlenen belirgin özellik |
|---|---|
| Finansal Muhasebe | 20 sorunun 11'i kayıt/yevmiye ağırlıklı; negatif ve öncüllü kök yok |
| Finansal Tablolar ve Analizi | Ortak tablo/veri üzerinden yorum ve hesaplama ağırlığı yüksek |
| Maliyet Muhasebesi | Kavram ile sayısal uygulama birlikte; öncüllü kök yok |
| Muhasebe Denetimi | 3 negatif kök, öncüllü kök yok |
| Hukuk | 2 negatif kök, 1 öncüllü soru |
| Vergi Mevzuatı ve Uygulaması | 3 negatif kök, 1 öncüllü soru |
| Sermaye Piyasası Mevzuatı | 6 negatif kök, 3 öncüllü soru |
| Meslek Hukuku | 1 negatif kök, 1 öncüllü soru |

Bu sayılar yalnız **ders/bölüm havuzunun toplam biçim dengesi** için referanstır.
Her konu paketi, kendi doğasına göre üretilir. Örneğin Finansal Muhasebe içindeki
“Temel Kavramlar” paketinin yarısını yapay biçimde yevmiye sorusuna çevirmek veya her
hukuk alt konusunda aynı sayıda öncüllü soru zorlamak doğru değildir.

Yeni test dönemleri yayımlandıkça profil yeniden ölçülür. Tek dönemde görülmeyen bir
soru türü “sınavda hiçbir zaman çıkmaz” şeklinde kalıcı yasak sayılmaz.

### Klasik sınavlardan yararlanma sınırı

2024–2025 klasik kitapçıkları konu kapsamı, önem sırası ve kullanılan mesleki dil için
yararlıdır. Beş seçenekli soru biçimi, şık yapısı veya süre baskısı için örnek alınmaz.
Çıkmış hiçbir soru, şık ya da çözüm metni kopyalanmaz.

---

## 2. Üretimden önce soru planı hazırla

60 soruluk bir konu paketi, sonradan kelimeleri ve sayıları değiştirilmiş 20 sorunun
üç kopyası değildir. Yazmaya başlamadan önce bir üretim matrisi hazırlanır. Her satırda
en az şu bilgiler bulunur:

- kazanım veya alt kapsam,
- soru türü: kavram, uygulama, hesap, kayıt, istisna, karşılaştırma vb.,
- ölçülen bilişsel işlem: bilme, ayırt etme, uygulama, yorumlama,
- zorluk,
- doğru cevabın dayanağı,
- çeldiricilerin temsil ettiği makul hata veya kavram yanılgısı.

Kurallar:

- Üç testin her biri 20 sorudur; her test kendi içinde kapsam ve zorluk dengesi taşır.
- Aynı bilgi farklı sorularda ancak **farklı bir zihinsel işlem** ölçüyorsa tekrar
  kullanılabilir. Eş anlamlı kelime, kişi adı veya sayı değişikliği yeni soru sayılmaz.
- Aynı kök kalıbı, aynı çözüm ve aynı çeldirici mantığı seri üretimde kullanılmaz.
- Konu havuzu ile bölüm havuzu birbirinden bağımsızdır. Kullanıcı konu testinde
  gördüğü soruyu bölüm testinde yeniden görmez.
- Bölüm sorusu dersin farklı alt konularını karıştırabilir; fakat kendisi özgün olur.

---

## 3. Builder kullan; JSON'u elle yazma

Sorular doğrudan JSON'a yazılmaz. Her konu için `build_<konu>.py` oluşturulur ve
JSON bu dosyadan üretilir. Böylece doğru metin, harf ataması, şıklar, çözüm ve kaynak
tek geçişte birlikte oluşturulur.

### Önerilen iskelet

```python
# -*- coding: utf-8 -*-
"""<Konu adı> — 3 test × 20 özgün soru."""
import json, random

Q = []

def q(stem, correct, distractors, why, ref, outcome,
      qtype="concept", difficulty="medium"):
    assert len(distractors) == 4
    assert correct.strip()
    assert all(d.strip() for d in distractors)
    assert len({correct.strip(), *(d.strip() for d in distractors)}) == 5
    Q.append({
        "stem": stem,
        "correct": correct,
        "distractors": distractors,
        "why": why,
        "ref": ref,
        "outcome": outcome,
        "qtype": qtype,
        "difficulty": difficulty,
    })

q(
    "TMS 2'ye göre aşağıdaki varlıklardan hangisi stok tanımına girer?",
    "Olağan iş akışında satılmak üzere elde tutulan ticari mallar",
    [
        "İdari faaliyetlerde kullanılmak üzere işletmenin edindiği hizmet binası",
        "Uzun vadeli değer artışı amacıyla elde tutulan yatırım amaçlı arsa",
        "Çalışana verilmiş ve daha sonra tahsil edilecek personel avansı",
        "İşletmenin ortaklarına karşı hakkı temsil eden ödenmiş sermaye payı",
    ],
    "Olağan faaliyet içinde satılmak üzere elde tutulan varlıklar TMS 2 kapsamında "
    "stoktur. Diğer seçenekler stok tanımındaki satış, üretim veya tüketim amacını taşımaz.",
    "TMS 2 Stoklar, par. 6",
    "Stok tanımındaki üç kullanım amacını ayırt eder.",
    difficulty="easy",
)

def gen_letters(n, seed):
    """Dengeli fakat periyodik olmayan cevap dizisi üretir."""
    r = random.Random(seed)
    base = list("ABCDE") * (n // 5) + list("ABCDE")[: n % 5]
    while True:
        r.shuffle(base)
        if all(not (base[i] == base[i-1] == base[i-2] == base[i-3])
               for i in range(3, len(base))):
            return base[:]

def build():
    assert len(Q) == 60, f"60 soru olmalı; şu an {len(Q)}"
    letters = gen_letters(len(Q), seed=20260717)  # her pakette farklı seed
    out = []
    for i, item in enumerate(Q):
        answer = letters[i]
        choices = {answer: item["correct"]}
        for key, value in zip(
            [key for key in "ABCDE" if key != answer], item["distractors"]
        ):
            choices[key] = value
        out.append({
            "id": f"topic-<kisaltma>-{i+1:04d}",
            "lessonId": "<curriculum.json lessonId>",
            "topicId": "<curriculum.json topicId>",
            "question": item["stem"],
            "choices": choices,
            "correctAnswer": answer,
            "explanation": item["why"],
            "source": {
                "kind": "generated",
                "styleRef": "2026 SMMM beş seçenekli test",
                "legislationRef": item["ref"],
            },
            "tags": ["Özgün Soru", "2026 Formatı", "Konu Havuzu", "<konu>"],
            "difficulty": item["difficulty"],
            "updatedAt": "2026-07-17T00:00:00Z",
            "examPeriod": "2026 test sistemine uyumlu özgün soru",
            "legislationVersion": "<kontrol edilen kaynak ve sürüm>",
            "sourceUpdatedAt": "2026-07-17T00:00:00Z",
            "isPremium": False,
            "isActive": True,
        })
    return out

if __name__ == "__main__":
    path = "content/yeterlilik/questions_topic_<konu>_2026.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(build(), f, ensure_ascii=False, indent=2)
    print("yazıldı:", path)
```

Builder da paketle birlikte saklanır. Yeni pakette farklı `seed`, farklı kimlik ön eki
ve gerçek kaynak kontrol tarihi kullanılır.

---

## 4. Soru kökü standardı

- Soru tek, açık ve tartışmasız bir görev ister.
- Adayın çözüm için ihtiyaç duyduğu veri kökte veya bağlı uyaranda bulunur.
- Gereksiz öykü ve yapay uzunluk eklenmez; ancak gerçek sınavdaki uygulama ve yorum
  düzeyini kaybettirecek kadar çıplak tanım sorularına da yığılma yapılmaz.
- “Hangisi doğrudur?” gibi jenerik kök kullanılabilir; ayırt edici içerik bu durumda
  seçeneklerde bulunmalıdır.
- Olumsuz kökler yalnız dersin doğası ve sınav profili gerektiriyorsa kullanılır.
  `değildir`, `yanlıştır` veya `beklenmez` ifadesi görünür ve tek anlamlı olmalıdır.
- Bir soruda iki olumsuzluk, belirsiz zaman ifadesi veya cevabı etkileyen eksik varsayım
  bulunmaz.
- Gerçek sınavın mesleki dili kullanılır; ders kitabı tanımını ezberden tamamlatan yapay
  cümleler yerine bilgi uygulaması ve ayırt etme ölçülür.

Kök uzunluğu tek başına kalite ölçütü değildir. Paket genelinde çok sayıda 1–2 cümlelik
çıplak tanım oluşması veya resmî sınava kıyasla belirgin biçimde kısa kalınması uyarıdır;
çözüm, anlamsız kelime eklemek değil daha gerçekçi görev üretmektir.

---

## 5. Şıklar ve doğru cevap sızıntısını önleme

### Temel ilke

**Doğru cevap kısa ya da uzun olacak diye yazılmaz.** Beş seçenek aynı dilbilgisel
yapıda, aynı kavramsal düzeyde ve doğal uzunlukta olmalıdır. Doğru cevabın uzunluk
sırası paket boyunca farklı konumlara dağılmalıdır.

- Doğru şık sürekli en kısa veya en uzun olamaz.
- Olumsuz kökte de yanlış ifade özellikle kısa ya da uzun yapılmaz.
- Bir seçenek, diğerlerinden belirgin ölçüde ayrıntılı veya kesin yazılarak işaret
  vermez.
- Seçenekler aynı kategoriye ait olur: hesap adıyla süre, kurumla yaptırım veya oranla
  tanım karıştırılmaz.
- Dilbilgisel uyum, noktalama, birim, büyük/küçük harf ve kesinlik düzeyi cevap hakkında
  ipucu vermez.
- “Her zaman”, “yalnızca”, “kesinlikle” gibi mutlak ifadeler ancak içerik gerektiriyorsa
  kullanılır; yalnız yanlış şıklara serpiştirilmez.
- Beş seçenek birbirinden farklıdır ve yalnız biri tam doğrudur.

Denetim paket genelinde doğru cevabın benzersiz en kısa/en uzun olma oranını ve uzunluk
sırasını ölçer. Hedef, resmî sınavdaki gibi belirgin yönsel kalıp oluşmamasıdır; yapay
olarak her şıkkı aynı karakter sayısına getirmek değildir.

### Çeldirici standardı

Her çeldirici:

- konuya ait gerçek bir kavram yanılgısını,
- hesap sorusunda makul bir işlem hatasını,
- mevzuat sorusunda yakın fakat farklı bir yetki, süre veya şartı,
- kayıt sorusunda makul bir hesap/taraf/borç-alacak hatasını

temsil eder. Rastgele sayı, alakasız kurum ve açıkça saçma ifade kullanılmaz.

---

## 6. Cevap harfleri

- Harfler seed'li ve örüntüsüz karıştırılır.
- `ABCDEABCDE...`, sabit adım ve kısa periyot kesinlikle yasaktır.
- Dengeli dağılım amaçlanır; adayın fark edebileceği mekanik rotasyon üretilmez.
- Aynı harfin dört veya daha fazla kez art arda gelmesinden kaçınılır.
- Şıkların harfleri sonradan değişse bile çözüm bozulmamalıdır.

Çözüm metninde “Doğru cevap A'dır” gibi harf atfı kullanılmaz. Çözüm doğru cevabı
içerik üzerinden açıklar.

---

## 7. Öncüllü ve olumsuz köklü sorular

Öncüllü soru sırf çeşitlilik kotası doldurmak için üretilmez. Konu birden fazla hükmü
birlikte sınıflandırmayı gerektiriyorsa kullanılır.

- Öncül sayısı doğal gereksinime göre 3–6 olabilir.
- Öncüller `\n\n` ile ayrılır.
- Doğru kombinasyon aynı kalıba yığılmaz; “hepsi” için yapay sabit yüzde konmaz.
- Kombinasyon seçenekleri çakışmaz ve doğru küme seçeneklerde tam olarak bulunur.
- Bir öncül yalnız dilinden veya uzunluğundan yanlış olduğu anlaşılan tuzak olmaz.

2026/1'de öncüllü sorular hukuk/mevzuat derslerinde görülmüştür. Bu gözlem ders
havuzu için referanstır; her hukuk alt konusuna öncüllü soru yerleştirme zorunluluğu
değildir.

Olumsuz kökteki doğru seçenek yanlış ifadeyi taşır; fakat diğer dört seçenekten
uzunluk, ayrıntı veya dil bakımından ayrılmaz.

---

## 8. Hesap, tablo ve yevmiye soruları

### Hesap

- Bütün ara sonuçlar builder içinde hesaplanır.
- Para ve oran hesaplarında gerektiğinde `Decimal` kullanılır; kayan nokta sonucu veya
  bilinçsiz `//` yuvarlaması kullanılmaz.
- Yuvarlama yöntemi kökte belirtilir veya mevzuat/standarttaki yönteme dayanır.
- Doğru sonuç tek olmalı; aynı değeri veren iki seçenek bulunmamalıdır.
- Çeldiriciler belgelenebilir hata sonuçlarıdır.

### Tablo ve ortak uyaran

- Tablo, grafik veya ortak finansal veri okunabilir ve tek başına yeterlidir.
- Birim, dönem, para birimi ve varsa yuvarlama açıklanır.
- Aynı uyaran birden çok soruda kullanılıyorsa sorular farklı bilgi veya işlem ölçer.

### Yevmiye

- Hesap kodu ve adı birlikte kullanılıyorsa Tekdüzen Hesap Planına uygun olur.
- Borç ve alacak toplamları builder assertion'ı ile eşitlenir.
- KDV ve diğer oranlar ya senaryoda verilir ya da açık dönemli mevzuat sorusudur.
- Metin şıklı ve kayıt/tablo şıklı biçimler ders havuzunda dengeli kullanılır.

---

## 9. Mevzuat ve standart güncelliği

`sourceUpdatedAt` alanına tarih yazmak, kaynak kontrolü yapıldığı anlamına gelmez.
Her sorunun doğru cevabı üretim tarihinde birincil kaynaktan doğrulanır.

Kaynak önceliği:

1. Resmî Gazete ve Mevzuat Bilgi Sistemi,
2. KGK'nın yürürlükteki TMS/TFRS ve denetim standartları,
3. SPK, TESMER, TÜRMOB ve ilgili kamu kurumlarının resmî metinleri,
4. Yalnız açıklama için ikincil kaynak; doğru cevabın tek dayanağı olamaz.

`source.legislationRef` genel başlık değil, mümkün olduğunca madde/paragraf düzeyinde
olur: `TMS 2 par. 16`, `6102 sayılı TTK m. 124` gibi. `legislationVersion` kontrol
edilen seti veya yürürlük tarihini, `sourceUpdatedAt` ise **gerçek kontrol tarihini**
gösterir.

### Değişken oran, tutar ve süreler

- Hesaplama becerisi ölçülüyorsa değişken oran kökte verilir.
- Güncel oranın/haddin kendisi müfredat gereği ölçülüyorsa soru açık dönem taşır:
  “2026 takvim yılında...” gibi. Dayanak ve kontrol tarihi zorunludur.
- “Cari oran”, “yürürlükteki tutar” veya “bugünkü had” gibi dönem belirtmeyen kökler
  kullanılmaz.
- İstisna tutarı, vergi tarifesi, asgari ücret ve yeniden değerleme oranı gibi sorular
  güncellik listesine eklenir ve mevzuat değişikliğinde yeniden doğrulanır.
- Kanunda sabit görünen sayılar da madde değişikliğine karşı kaynakla doğrulanır.

---

## 10. Çözüm standardı

Çözüm:

- doğru ilke, işlem veya maddeyi açıklar,
- hesap sorusunda ara adımları gösterir,
- gerekli olduğunda yakın çeldiricinin neden yanlış olduğunu ayırt eder,
- soru ve şıklardaki bilgiyi aynen tekrar etmekle yetinmez,
- cevap harfi içermez,
- başka bir soruyla aynı şablon çözümün sayı/kelime değiştirilmiş kopyası olmaz,
- `Demo açıklama`, yer tutucu, yarım cümle veya içi doldurulmamış şablon içermez.

Çözümün uzunluğu konuya göre değişebilir; fakat adayın neden doğru yaptığını öğrenmesini
sağlayacak kadar gerekçeli olmalıdır.

---

## 11. Özgünlük ve telif

- TESMER kitapçığından veya üçüncü taraf soru bankasından kök, seçenek ya da çözüm
  kopyalanmaz.
- Çıkmış sorular yalnız biçim, kapsam ve bilişsel düzey analizi için kullanılır.
- Kurgusal kişi/işletme ve özgün sayılar kullanılır.
- Kaynak metindeki bir cümleyi seçenek yapmak zorunluysa kısa ve gerekli kısmı yeniden
  ifade edilir; soru bütünü özgün bir ölçme görevi olur.
- `source.kind` daima `generated` olur. Bu etiket tek başına özgünlük kanıtı değildir.

Otomatik denetim birebir, şablon ve yüksek benzerlikli tekrarları arar. Telif ve gerçek
anlamsal özgünlük ayrıca insan tarafından kontrol edilir.

---

## 12. Şema, etiket ve havuz ayrımı

- `lessonId` ve `topicId`, uygulamadaki `assets/content/curriculum.json` ile eşleşir.
- Beş seçenek A–E eksiksizdir; seçenek metinleri benzersizdir.
- `correctAnswer` mevcut bir seçenektir.
- `id`, soru kökü ve soru fikri paketler arasında da benzersizdir.
- Yeni üretimde soru veya çözüm metnine **Demo Soru / Demo açıklama** yazılmaz.
- Yeni üretimde `Demo Soru` etiketi kullanılmaz; bunun yerine `Özgün Soru` kullanılır.
- Konu sorusu `Konu Havuzu` etiketi taşır.
- Bölüm sorusu `Konu Havuzu` etiketi taşımaz; isterse `Bölüm Havuzu` etiketi taşır.
- Bir soru iki havuza birden ait olamaz.
- `2026 Formatı` varsa `examPeriod` ve `sourceUpdatedAt` doludur.

Yeni paket iki manifestte de kayıtlı olur ve sürümler aynı artırılır:

```json
{"file": "yeterlilik/questions_topic_<konu>_2026.json", "programIds": ["yeterlilik"]}
```

---

## 13. İnsan incelemesi

Yayımdan önce paketteki **her soru** en az bir kez içerik açısından okunur. Mevzuat,
standart, yevmiye ve hesap soruları ayrıca dayanağı üzerinden doğrulanır.

İnceleyen kişi şunları onaylar:

- yalnız bir doğru cevap bulunduğunu,
- çeldiricilerin makul fakat yanlış olduğunu,
- dayanağın yürürlükte ve soruyla ilgili olduğunu,
- çözüm ile doğru cevabın uyumlu olduğunu,
- sorunun atandığı konu sınırında kaldığını,
- çıkmış soru veya başka paketle anlam bakımından tekrar olmadığını,
- zorluk ve dilin gerçek sınava uygun olduğunu.

---

## 14. Teslim kontrol listesi

### İçerik

- [ ] 3 test × 20 soru ve üretim matrisi tamamlandı
- [ ] Her soru özgün bir görev veya farklı bilişsel işlem ölçüyor
- [ ] Bölüm ve konu havuzu kesişmiyor
- [ ] Tek doğru cevap ve dört makul çeldirici var
- [ ] Doğru cevap uzunluk/dil ipucuyla ayırt edilemiyor
- [ ] Çözümler özgün, gerekçeli ve harf atıfsız
- [ ] Hesaplar builder ile doğrulandı
- [ ] Mevzuat/standart dayanakları birincil kaynaktan kontrol edildi
- [ ] Kullanıcıya görünen metinde demo veya şablon artığı yok

### Teknik

- [ ] `audit.py <paket>` → FATAL 0
- [ ] `audit.py --manifest ...` → yeni çapraz tekrar yok
- [ ] Uyarılar düzeltildi veya inceleme notunda gerekçelendirildi
- [ ] `lessonId`/`topicId` müfredatta mevcut
- [ ] `Konu Havuzu` / bölüm havuzu ayrımı doğru
- [ ] Builder, JSON ve iki manifest birlikte güncellendi
- [ ] OTA ve uygulama kopyaları özdeş
- [ ] İnsan incelemesi tamamlandı

Bu standarttaki sayısal eşikler, adayın fark edebileceği mekanik kusurları yakalamak
içindir. Eşiği geçmek amacıyla anlamsız kelime eklemek, soruyu yapay biçimde uzatmak
veya aynı fikri yüzeysel olarak yeniden yazmak ayrıca kalite ihlalidir.
