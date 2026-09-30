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
python3 tools/smmm/audit/audit.py content/yeterlilik/<dosya>.json
```

Manifestteki bütün Yeterlilik paketleriyle çapraz kontrol için:

```bash
python3 tools/smmm/audit/audit.py --manifest content/v2/manifests/smmm.json
```

Konu paketi uygulama deposuna da kopyalandıysa:

```bash
python3 tools/smmm/audit/verify_konu.py <dosya_adı>.json
```

- **FATAL:** Paket yayıma gidemez. Kör öğrenci (soruyu okumadan) ≥%36, çeldiricilerde
  mutlak dil >%8 ve ders profilinin gerçek sınavdan belirgin sapması da FATAL'dır.
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

### Gerçek test kitapçıkları: ölçülen profil (2026/1 + 2026/2)

Test biçiminde iki dönem yayımlandı: **2026/1 ve 2026/2, 8 ders × 20 = 320 soru**.
Kitapçıklar ayrıştırılıp (cevap anahtarı dahil) aynı cetvelle ölçüldü; sayılar
`tools/smmm/audit/bantlar.json`'dadır ve `audit.py` bunlarla denetler. Kitapçık
metni telifli olduğundan depoya girmez (yerel referans:
`Projects/Current/_referans/yeterlilik/`, yeniden üretim `profil.py --hesapla`).

| Ders | Medyan kök | Olumsuz kök | Kökte mevzuat atfı | Öncüllü | Yevmiye şıklı | Sayısal şıklı | Veri/tablo |
|---|---:|---:|---:|---:|---:|---:|---:|
| Finansal Muhasebe | 270 | %2 | %15 | %0 | %28 | %5 | %48 |
| Fin. Tablolar ve Analizi | 92* | %2 | %5 | %0 | %0 | %85 | %85 |
| Hukuk | 168 | %38 | %100 | %5 | %0 | %22 | %8 |
| Maliyet Muhasebesi | 308 | %12 | %8 | %2 | %2 | %38 | %57 |
| Meslek Hukuku | 239 | %50 | %65 | %10 | %0 | %18 | %2 |
| Muhasebe Denetimi | 178 | %42 | %90 | %2 | %0 | %2 | %0 |
| Sermaye Piyasası | 263 | %40 | %92 | %20 | %0 | %18 | %0 |
| Vergi Mevzuatı | 324 | %32 | %98 | %2 | %0 | %40 | %40 |

\* Fin. Tablolar'da sorular ortak bilanço/gelir tablosuna (15-20 soruya tek veri)
bağlıdır; kök kısa, veri ortak uyarandadır.

Bu profilden çıkan bağlayıcı sonuçlar:

- **Mevzuat derslerinde kök mevzuatı adıyla anar**: “4857 sayılı İş Kanunu’na göre,
  …”, “Bağımsız Denetim Yönetmeliği uyarınca …”, “213 sayılı VUK’a göre …”.
  “Denetçi ne yapmalıdır?” gibi dayanaksız kısa soru gerçek sınavda yoktur.
- **Olumsuz kök gerçek sınavın omurgasıdır**: Meslek %50, Denetim %42, SPK %40,
  Hukuk %38, Vergi %32 — “…aşağıdakilerden hangisi … biri değildir?” /
  “…ilgili aşağıdakilerden hangisi yanlıştır?”. (Eski tabloda Meslek için “1 negatif
  kök” yazıyordu; gerçekte 2026/1'de 14/20'dir. Havuz bu yanlış sayıya göre üretildi.)
- **Vergi soruların %40'ı çok kalemli hesaptır**: gelir unsurları dökümü, beyan
  sınırı, KDV devri, iştirak kazancı istisnası, örtülü sermaye, finansman gider
  kısıtlaması… Tarife/had gerekiyorsa gerçek sınav gibi **kökte verilir**.
- **Hukuk/Meslek/SPK'da süre ve sayı soruları** (“en fazla kaç ay”, “kaç gün
  içinde”) %18-22'dir; şıklar yalnız sayıdır.
- **Finansal Muhasebe'de şıklar yevmiye kaydıdır** (%28 tam kayıt tablosu, ayrıca
  “… hesabına … borç kaydedilir” metin şıkları); kök bir işlem senaryosudur.
- **Mutlak dil şıklarda yoktur**: 1.600 gerçek şıkkın %1'inde “yalnızca, hiçbir
  hâlde, zorunda, her zaman” gibi ifade geçer. Çeldiriciyi bu sözcüklerle yanlış
  yapmak adaya eleme ipucu verir (havuzda %26 idi; Hukuk'ta kör öğrenci %48).

Paket düzeyinde yalnız olumsuz kök ve mevzuat atfı zorlanır; hesap, yevmiye ve
öncül payı konunun doğasına göre değişir ve **ders toplamında** denetlenir. Konu
havuzu ile bölüm havuzu ayrı ayrı ders profiline uymalıdır.

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

## 3.0 Güncel yöntem: `yet_ortak.Paket` (2026-09-28'den itibaren zorunlu)

Yeni ve yeniden yazılan paketler `tools/smmm/builders/yet_ortak.py` ile üretilir
(örnek: `build_yk_disiplin.py`, bölüm testleri için `build_yb_meslek.py`). Modül,
JSON yazılmadan önce şunları durdurur:

- şıkta mutlak dil (`audit.ELEME_ISARETI`: yalnız, zorunda, hiçbir, kendiliğinden…);
  mevzuat metninde geçse bile şıkta sadeleştirilir ("başlamak zorundadır" → "başlar"),
- çözümde harf atfı, tekrar eden şık, 60/60'tan sapma, kimlik sayısı uyuşmazlığı,
- şık uzunluğu: doğru şık tek-en-uzun veya tek-en-kısa > %25, iki uçtan biri < %8,
  ortalama uzunluk sırası 2,45–3,55 dışı,
- kör öğrenci ≥ %32, öncül seçici yığılması, aynı harfin üç kez art arda gelmesi.

Sayısal şıklar `P.sayisal()` ile artan sırada, öncüllü sorular `P.oncul()` ile
gerçek kitapçıktaki gibi sabit seçici sırasıyla yazılır; harfleri değer/sıra belirler.
Kimlikler mevcut dosyadan alınır: uygulama silinen soruyu telefondan silmez, aynı
kimliğin üzerine yazmak eski metni temizler. Programda aynı soru kökü iki kez
bulunamaz (uygulama `ContentValidator` ve `audit.py --manifest` FATAL verir).

Yazım sırasında sık düşülen üç tuzak: kesin hükmü eksiksiz yazınca doğru şık
sistematik olarak en uzun olur (yazdıktan sonra kısalt, bazı sorularda çeldiriciye
gerçek içerik ekle); aşırı kısaltmada en kısa uca kayar; olumsuz kök oranı kendiliğinden
düşük kalır (mevzuat derslerinde baştan ~%50 hedefle).

Mevcut dosyada tasarımdan az soru varsa (ör. 18 soruluk bölüm testi 20'ye çıkıyorsa)
`Paket(..., ek_idler=["demo-sermaye-021", ...])` ile yeni kimlikler eklenir; eski
kimlikler korunur. Bir bölüm testini karıştıran eski demo sorusu silinmez,
`demo_questions.json` içinde `isActive: false` yapılır (cihazdan böyle kalkar).
Toplu metin değişikliği yapan yardımcı betiklerde bir soru bloğunun sonunu sadece
"sonraki `P.` satırı" ile arama: arada bölüm yorumu varsa sonraki soru da yutulur;
değişiklikten sonra soru sayısını mutlaka say. Şıklarda `"…".replace(...)` gibi
kod içi dönüşüm bırakma; şık düz metin olmalıdır.

Yeniden yazılan bir dosyanın sahibi artık `build_yk_*` / `build_yb_*` builder'ıdır.
Aynı dosyayı yazan eski `build_kh_*`, `build_yet_*` builder'ları ve
`fixers/fix_legacy_yeterlilik_quality.py` çalıştırılmaz (yeni içeriğin üzerine eski
metni yazarlar). Toplu doğrulama sadece `from yet_ortak import` içeren builder'larla
`--check` kipinde yapılır.

Serbest yazımda soru sayısı kendiliğinden 40-55 arasında kalıyor (Denetim dersinde
sekiz pakette de oldu). Yazmaya başlamadan 60 maddelik bir dayanak listesi çıkar;
ilk taramada eksik kalan soruları olumsuz kökle tamamlamak olumsuz oranını da düzeltir.
Denetim sorularında atıf kalıbı "Standardı / KYS / Etik Kurallar" yazımlarını da tanır
(`profil.ATIF`); kalite yönetimi sorularında kök "Kalite Yönetim Standardı 1’e (KYS 1)
göre" biçiminde yazılır.

Vergi dersinde (2026-09-29) öğrenilenler:
- Yıla bağlı tutar (tarife, istisna, beyan sınırı, azami damga tutarı, kesinti oranı) kökte
  "(2025 yılı için … olarak alınacaktır.)" diye verilir; şıkta oran veya had varsa kökte açık
  yıl bulunur (`K26 = "… 2026 yılında yürürlükte olan hükümlerine göre"`), yoksa audit
  mevzuat-güncellik UYARI verir. Hesaplar `vergi_ortak.py` (`gv2025`, `tl`, `secenekler`)
  ile yapılır; `secenekler()` eşit çeldiricide durur, adayı değiştir.
- Kanun metnini tam oku: yarım okunan maddede iki kez hata çıktı (md. 262 finansman faizi
  "envantere alındığı hesap dönemi sonuna kadar", 6183 md. 23 "takas" değil reddiyatın
  mahsubu). Güncel metinle son kitapçık çelişiyorsa (6183 md. 15/58 başvuru mercii) mercii
  değil, ortak olan süreyi sor.
- 7524/7577/7582/7587/7589 değişiklikleri: uzlaşma sadece cezalara, md. 376 indirimi yarı,
  KVK md. 11/1-k (şans-bahis reklamı), KDVK md. 17/4-ğ (kamulaştırma), VUK md. 107/A,
  İYUK md. 45-46 parasal sınırları. 2026 dönemi hesaplarını 7582 nedeniyle 2025 üzerinden kur.
- Sayısal ağırlıklı paketlerde (%35-40) sabit harfler art arda yığılır; sayısal ve sözel
  soruları dönüşümlü diz (üçlü aynı harf "harf dizisi kurulamadı" hatası verir).
- `yet_ortak` artık `updatedAt`/`sourceUpdatedAt` farkını yok sayar: içerik aynıysa dosya
  yeniden yazılmaz, `--check` "aynı" der (önceden her gün tüm paketler "FARKLI" görünüyordu).
- Anayasa atfı da mevzuat atfı sayılır (`profil.ATIF`).

Hukuk dersinde (2026-09-30) öğrenilenler:
- 2026'da yürürlüğe giren değişiklikler soruya girer, köke `K26` konur: 7578 (22.4.2026;
  analık izni 8+16=24 hafta, doğum öncesi çalışma iki haftaya kadar, eşin doğumunda 10 gün,
  koruyucu aileye 10 gün ücretsiz izin; 5510 md. 15/18 aynı süreler), 7566 (MYÖ primi %21,
  işveren hissesi %12), 7589 (TBK md. 55 faiz başlangıcı ve mahsup; İYUK md. 45-46), 7588
  (İYUK md. 28 göreve iade kararları kesinleşince), 7553 (turizm konaklama hafta tatili
  dört gün içinde), 7331 (İYUK md. 10, 11, 13'te cevap süresi otuz gün).
- Yeniden değerlemeye veya Cumhurbaşkanı kararına bağlı tutarlar sorulmaz: İYUK istinaf-
  temyiz parasal sınırları, TTK ve 5510 idari para cezası tutarları, AŞ/Ltd. asgari sermaye.
  5510 cezaları "asgari ücretin … katı" oranıyla sorulabilir.
- mevzuat.gov.tr zaman zaman komut satırından (curl) erişilemiyor; uygulama içi tarayıcıda
  `anasayfa/MevzuatFihristDetayIframe?MevzuatTur=1&MevzuatNo=<no>&MevzuatTertip=5` açılıp
  metin `document.body.innerText` ile okunabiliyor.
- "Aşağıdakilerden hangisi … değildir" liste sorularında tek sözcüklük çeldiriciler ("Dil",
  "Servet") doğru şıkkı sistematik olarak en uzun bırakır; çeldiricileri tam ifade yaz
  ("Kişinin serveti"). Ters yönde aşırıya kaçma: 60+ karakterlik tek çeldirici "şık-dengesi"
  UYARI'sı verir (en kısa/en uzun oranı).
- `"…".replace(" zorundadır", "…")` gibi zincirleme kısayollar bozuk Türkçe üretti
  ("etmekmek"); mutlak dili doğrudan düzgün cümleyle yaz, kısayol bırakma.
- Bölüm testi kökleri konu paketleriyle birebir aynı olursa `dosyalar-arası-kök` FATAL verir;
  aynı hükmü sorarken köke kısa bir olay girişi ekle, çözümü farklı cümleyle yaz. Aynı durum
  farklı dersler arasında da olur (İYUK konusu ↔ Vergi uyuşmazlıkları).
- Bölüm havuzunu kirleten eski aktif demoları (`demo_questions.json`) pasifleştir; bölüm
  testinin 20'ye tamamlanması için `ek_idler` ile yeni `demo-<ders>-0NN` kimliği ver.

Finansal Muhasebe dersinde (2026-09-30) öğrenilenler:
- Gerçek bant (40 soru): medyan kök 270, yevmiye şıklı %27,5, veri/tablo %47,5, atıf %15,
  olumsuz %5, öncül %0, sayısal şık %5. Çıplak tanım neredeyse yok; kavram bile olay ve tutarla
  sorulur. Şıkların çoğu tam yevmiye kaydı ya da "X hesabının borç/alacak tarafına N ₺ kaydedilir".
- Yevmiye ve taraf şıkları `builders/fm_ortak.py` ile kurulur: `kayit()` uygulamanın yevmiye
  biçimini (kod çitli, alacak satırı dört boşluk girintili) üretir ve borç=alacak eşitliğini
  kuruşta denetler; float kur çarpımı artıkları kuruşta eşitlenir. Bu denetim gerçek hata yakaladı.
- Aynı adlı THP hesapları (257/268, 263/750, 370/691, 120/220, 121/221, 300/400, 372/472)
  kodsuz `taraf()` şıklarında birebir aynı metne düşer ("5 farklı şık yok"). Soru bu ayrımı
  ölçüyorsa kodlu `kayit()` biçimi kullan.
- Sayısal verilerde çeldiricilerin doğru değere denk gelip gelmediğini kontrol et: ağırlıklı
  ortalama tam 21 ₺ çıkınca "3.200 × 21" çeldiricisi doğru şıkla aynı oldu; veriyi değiştir.
- Yevmiye payı kolayca %50'yi aşar (bant +%23 tolerans). Tek bir tutarı ölçen kayıtları
  "taraf" biçimine çevirerek %35-40'a indir.
- Atıf: TMS/TFRS konusunda da kökte standart adını her soruda anma; olay üzerinden sor, yaklaşık
  %15-20 oranında "TMS 16’ya göre" gibi ifade kullan. "Standartları" büyük harfle ATIF sayılır.
- VUK md. 219 kayıt süresi (10 gün, belge muhasebeciye verilince 45 gün üst sınır) gibi ikili
  kurallarda olayı iki süreyi de aşacak ya da açıkça birine düşecek biçimde kur; aradaki
  gecikme şıkkı tartışmalı yapar.

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

Gerçek sınavda öncüllü soru SPK'da %20, Meslek %10, Hukuk %5'tir; muhasebe
derslerinde yok denecek kadar azdır. Her alt konuya öncüllü soru yerleştirme
zorunluluğu yoktur; ders toplamı bantta kalmalıdır.

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
