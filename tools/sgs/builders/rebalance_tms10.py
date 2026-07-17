# -*- coding: utf-8 -*-
"""muhasebe_standartlari/tms_10_sonraki_olaylar.json — dolgu temizliği (%81 → ≤%30).

⚠ BU DOSYADA KUSUR TERS YÖNDE. Vergi/Borçlar'da doğru şık EN UZUNDU; burada
EN KISA (%86). Sebep: bu dosyayı bu oturumda "doğru şıkkı kısa + çeldiricileri
uzun yaz" diye geri alınmış bir kuralla yazdım. Çeldiriciler DOLGUYLA şişirildi:
240 çeldiricinin 135'i (%56) "…zorunda bulunmaktadır" kalıbı taşıyor, doğru
şıkların SIFIRI. Doğru ortalama 59 karakter, çeldirici 76.

Bu yüzden düzeltme de ters: UZATMAK değil, DOLGUYU ATMAK. Kuyruklar kırpılınca
çeldiriciler doğrunun boyuna yaklaşır → hem dolgu tell'i hem ters boy ipucu
aynı anda kapanır.

İki geçiş:
  1) Mekanik kırpma — dolgu kuyruğu formüle bağlı; "…açıklanmak zorunda olan bir
     durumu ifade eder" → "…açıklanır". Anlam korunur, şişkinlik gider.
  2) Atma-şıkkı — "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest
     takdirine bırakılmıştır" 33 KEZ tekrarlanmış ve her seferinde yanlış; tek
     başına öğrenilir. Gerçek kavram yanılgılarıyla değiştirilir.
"""
import json
import re

P = ("/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/"
     "muhasebe_standartlari/tms_10_sonraki_olaylar.json")

# ── 1. geçiş: dolgu kuyruklarını kırp (anlamı koruyarak) ──────────────────────
KIRP = [
    (r"açıklanmak zorunda olan bir durumu ifade eder", "açıklanır"),
    (r"açıklanmak zorunda kalınır", "açıklanır"),
    (r"açıklanmak zorundadır", "açıklanır"),
    (r"hiç açıklanmamak zorunda (?:kalınmaktadır|tutulmaktadır|bulunmaktadır)", "hiç açıklanmaz"),
    (r"yapılmak zorunda tutulmaktadır", "yapılır"),
    (r"yansıtılmak zorundadır", "yansıtılır"),
    (r"muhasebeleştirilmek zorundadır", "muhasebeleştirilir"),
    (r"düzeltilmek zorunda (?:bulunmaktadır|kalınmaktadır|tutulmaktadır)", "düzeltilir"),
    (r"düzeltilmek zorundadır", "düzeltilir"),
    (r"sıfırlanmak zorunda bulunmaktadır", "sıfırlanır"),
    (r"indirilmek zorundadır", "indirilir"),
    (r"silinmek zorundadır", "silinir"),
    (r"gösterilmek zorundadır", "gösterilir"),
    (r"ayrılmak zorunda (?:bulunmaktadır|kalınmaktadır)", "ayrılır"),
    (r"hazırlanmak zorunda kalınmaktadır", "hazırlanır"),
    (r"kapsamak (?:durumunda bulunmaktadır|zorunda olan bir düzenlemedir|zorundadır)", "kapsar"),
    (r"ifade etmek (?:durumundadır|zorundadır)", "ifade eder"),
    (r"karşılamak (?:durumundadır|zorundadır)", "karşılar"),
    (r"sayılmak zorunda (?:kalınmaktadır|tutulmaktadır|bulunmaktadır|kalır)", "sayılır"),
    (r"sayılmak zorundadır", "sayılır"),
    (r"tutulmak zorunda (?:kalınmaktadır|bulunmaktadır)", "tutulur"),
    (r"uygulanmak zorunda (?:tutulmuştur|tutulmaktadır|kalınmaktadır)", "uygulanır"),
    (r"bir husus niteliğinde (?:bulunmaktadır|olup belirsiz bırakılmış bulunmaktadır)",
     "bir husustur"),
    (r"dar kapsamlı bir düzenleme durumundadır", "dar kapsamlı bir düzenlemedir"),
    (r"yeniden düzenlenmek zorunda (?:kalınmaktadır|tutulmaktadır)", "yeniden düzenlenir"),
    (r";? ?ancak düzeltme izleyen dönemde yapılır", "; düzeltme izleyen döneme bırakılır"),
    # ── 2. geçiş kuyrukları: ilkinden 29 kalıp arttı; hepsi aynı iki aileden ──
    (r"açıklamak zorunda olan bir işlemi ifade eder", "açıklar"),
    (r"göstermek zorunda kalınır", "gösterir"),
    (r"gerek bulunmamak (?:durumundadır|zorundadır)", "gerek bulunmaz"),
    (r"esas alınmak zorunda kalınır", "esas alınır"),
    (r"esas alınmak durumundadır", "esas alınır"),
    (r"serbestçe seçmek durumundadır", "serbestçe seçer"),
    (r"müdahale edilmemek durumundadır", "müdahale edilmez"),
    (r"yapılmamak zorunda olan bir durumdur", "yapılmaz"),
    (r"yapılmamak durumundadır", "yapılmaz"),
    (r"yapılmamak zorunda olan bir durumu ifade etmektedir", "yapılmaz"),
    (r"düzeltilmek zorunda tutulan bir durumdur", "düzeltilir"),
    (r"düzeltilmek zorunda kalınır", "düzeltilir"),
    (r"güncellenmek zorunda tutulan bir durumdur", "güncellenir"),
    (r"yapılmak zorunda tutulan bir durumdur", "yapılır"),
    (r"alınmak zorundadır", "alınır"),
    (r"sayılmak durumundadır", "sayılır"),
    (r"sayılmak zorunda kalınır", "sayılır"),
    (r"çevrilmek zorunda kalınır", "çevrilir"),
    (r"hesaplanmak zorundadır", "hesaplanır"),
    (r"dönüşmek zorunda kalan bir durumdur", "dönüşür"),
    (r"ertelenmek zorunda tutulan bir durumdur", "ertelenir"),
    (r"dikkate alınmak zorunda tutulan bir durumdur", "dikkate alınır"),
    (r"verilmek durumundadır", "verilir"),
    (r"yeniden onaylanmak zorundadır", "yeniden onaylanır"),
    (r"belirleyici sayılmak durumundadır", "belirleyicidir"),
    # ── 4. geçiş: DOLGU regex'ine takılmayan şişkinlik ──────────────────────
    # "zorunda" içermeyen ama aynı işi gören adlaştırmalar. Bunlar dedektörün
    # kalıbına girmiyor; yine de doğru şıkkı (ort. 59) çeldiricinin (76) altında
    # bırakıyor ve "en kısayı seç" stratejisini besliyordu.
    (r"kapsayan (?:bir düzenleme niteliğindedir|dar kapsamlı bir düzenlemedir)", "kapsar"),
    (r"olayları kapsayan bir düzenleme niteliğinde bulunur", "olayları kapsar"),
    (r"kapsamaktadır", "kapsar"),
    (r"ifade etmektedir", "ifade eder"),
    (r"karşılamaktadır", "karşılar"),
    (r"bulunmaktadır", "bulunur"),
    (r"tanımlanmamış bir husus niteliğinde bulunur", "tanımlanmamıştır"),
    (r"tanımlanmamış bir husus niteliğindedir", "tanımlanmamıştır"),
    (r"düzenlenmemiş bir husus niteliğinde bulunur", "düzenlenmemiştir"),
    (r"gösteren bir belge niteliğindedir", "gösteren bir belgedir"),
    (r"olan bir durumu ifade eder", "olur"),
    (r"olan bir kalemi ifade eder", "olur"),
    (r"olan bir ölçümü (?:ifade eder|karşılar)", "olur"),
    (r"niteliğinde bulunan", ""),
    (r"\s*niteliğinde bulunur", ""),
    (r"\s*niteliğindedir", ""),
    # kalan genel kuyruklar
    (r"\s*zorunda (?:bulunmaktadır|kalınmaktadır|tutulmaktadır|olan bir durumu ifade eder)", ""),
    (r"\s*durumunda (?:bulunmaktadır|kalınmaktadır)", ""),
]

# ⚠ 1. geçişten sonra YENİ bir atma-şıkkı ortaya çıktı: kırpma sonrası 9 soruda
# "Düzeltme gerektirmeyen olaydır; ancak önemli olsa dahi hiç açıklanmaz" aynı
# metne indi. Dolguyu atarken farklı cümleleri aynı cümleye indirgemek yeni bir
# tekrar üretiyor — kırpma tek başına yetmiyor, çeşitlendirme de gerekiyor.
TEKRAR_YERINE = [
    "Düzeltme gerektirmeyen olaydır; açıklama yalnızca tutar kesin olarak ölçülebiliyorsa yapılır",
    "Düzeltme gerektirmeyen olaydır; açıklama izleyen dönemin dipnotlarına bırakılır",
    "Düzeltme gerektirmeyen olaydır; yalnızca olayın niteliği yazılır, finansal etki tahmini verilmez",
    "Düzeltme gerektirmeyen olaydır; açıklama yalnızca bağımsız denetime tabi işletmelerce yapılır",
    "Düzeltme gerektirmeyen olaydır; açıklama zorunluluğu yalnızca nakit çıkışı doğuran olaylarda doğar",
    "Düzeltme gerektirmeyen olaydır; olay dipnotta değil, yönetim kurulu faaliyet raporunda anlatılır",
    "Düzeltme gerektirmeyen olaydır; açıklama yerine izleyen dönemde karşılık ayrılır",
    "Düzeltme gerektirmeyen olaydır; önemlilik değerlendirmesi yapılmaz, her olay eşit sayılır",
    "Düzeltme gerektirmeyen olaydır; açıklama ancak olay tabloların onayından sonra sürerse yapılır",
]

# ── 2. geçiş: 33 kez tekrarlanan atma-şıkkı yerine gerçek kavram yanılgıları ──
# Her biri TMS 10'un bir hükmünü YANLIŞ uygular; sırayla dağıtılır ki tek bir
# yeni kalıp doğmasın.
ATMA_YERINE = [
    "Olayın düzeltme gerektirip gerektirmediği, tutarının önemlilik düzeyini aşıp aşmadığına bakılarak belirlenir",
    "Ayrım, olayın işletmenin lehine mi yoksa aleyhine mi sonuç doğurduğuna göre yapılır",
    "Belirleyici olan, olayın yönetim tarafından hangi tarihte öğrenildiğidir",
    "Sonraki olaylar penceresi, finansal tabloların ticaret sicilinde ilan edildiği tarihte kapanır",
    "Düzeltme gerektiren olaylarda tutarlar düzeltilmez; yalnızca dipnot açıklaması güncellenir",
    "Onay tarihi, bağımsız denetçinin denetim raporunu imzaladığı tarih olarak belirlenir",
    "Kâr payı, dönem sonundan sonra ilan edilse bile dönem sonu bilançosunda borç gösterilir",
    "Sonraki olaylar yalnızca tutarı ölçülebilen ve nakit çıkışı doğuran olayları kapsar",
    "Düzeltme gerektirmeyen olaylar, izleyen dönemin tablolarında geriye dönük düzeltilir",
    "Süreklilik ortadan kalkarsa tutarlar düzeltilir; muhasebe esası ise değişmeden kalır",
    "Hile veya hatanın sonradan bulunması düzeltme gerektirmeyen olay sayılır",
    "Ölçüt, olayın dönem sonundan önceki mi sonraki mi bir tarihte öğrenildiğidir",
]

# ── 5. geçiş: doğrunun ALTINA yazılmış çeldirici ────────────────────────────
# ⚠ Kırpmanın bir tavanı var. Dolguyu tamamen attıktan sonra bile çeldiriciler
# doğrudan uzun kalıyordu (ort. 80 ↔ 70): çünkü çeldirici bir yanılgıyı ADIYLA
# söylemek zorunda, doğru şık ise kısa ve kesin. Sonuç: "en kısayı seç" %40.
# Doğru şıkka dokunamadığımıza göre tek çıkış, bir bölüm çeldiriciyi doğrunun
# ALTINA yazmak — böylece doğrunun boy sırası iki uca da dağılıyor.
#
# Hedef dağılım: doğru en uzun ~%20 · en kısa ~%20 · ortada ~%60 (ortadaki
# 3 aday üzerinden beklenen değer ≈ %20 = rastgele taban).
#   · 4 çeldiricinin HEPSİ kısaltılan 3 soru → doğru EN UZUN olur
#   · tek çeldirici kısaltılan 7 soru        → doğru ORTAYA düşer
# Kalan 10 soruda doğru en kısa kalır (kasten — bkz. %20 kuralı).
KISALT = {
    # ── hepsi kısalır: doğru en uzun olur ──
    "std-tms10-gen-0001": {
        "A": "Raporlama dönemi sonu ile ilk geçici vergi beyannamesi arasında",
        "B": "Raporlama dönemi sonu ile denetim sözleşmesinin imzası arasında",
        "D": "Raporlama dönemi sonu ile beyannamenin verildiği tarih arasında",
        "E": "Raporlama dönemi sonu ile izleyen hesap döneminin sonu arasında",
    },
    "std-tms10-gen-0022": {
        "A": "Raporlama döneminden sonra bir işletme birleşmesi yapılması",
        "C": "Raporlama döneminden sonra çıkan yangında binanın yanması",
        "D": "Raporlama döneminden sonra önemli tutarda sermaye artırımı",
        "E": "Raporlama döneminden sonra kurlarda olağandışı dalgalanma",
    },
    "std-tms10-gen-0038": {
        "A": "Süren davanın sonradan mevcut yükümlülüğü teyit etmesi",
        "C": "Alınan bilginin varlığın dönem sonunda değersizleştiğini göstermesi",
        "D": "Tabloların yanlış olduğunu gösteren bir hilenin bulunması",
        "E": "Dönem sonundan önce alınan varlığın maliyetinin belirlenmesi",
    },
    # ── tek çeldirici kısalır: doğru ortaya düşer ──
    "std-tms10-gen-0012": {"D": "Sonraki koşullara ilişkin, işletme aleyhine olan olay"},
    "std-tms10-gen-0016": {"A": "Düzeltme gerektirmeyen olaydır; açıklanmaz"},
    "std-tms10-gen-0030": {"A": "Düzeltme gerektiren olaydır; değer düzeltilir"},
    "std-tms10-gen-0045": {"D": "Belirleyici olan, olayın öğrenildiği tarihtir"},
    "std-tms10-gen-0054": {"B": "Tabloların sicilde ilan edildiği tarih"},
    "std-tms10-gen-0057": {"A": "Yalnızca tutarlar düzeltilir"},
    "std-tms10-gen-0058": {"E": "Olayın nakit çıkışı doğurup doğurmadığı"},
}

if __name__ == "__main__":
    qs = json.load(open(P, encoding="utf-8"))
    idx2 = {q["id"]: q for q in qs}
    D = re.compile(r"(zorunda|durumundadır|bulunmaktadır|kalınmaktadır|tutulmaktadır)", re.I)

    kirpilan = atma = 0
    sira = 0
    for q in qs:
        for harf, v in list(q["options"].items()):
            if harf == q["answer"]:
                continue
            # atma-şıkkı → gerçek yanılgı
            if "düzenlenmemiş olup" in v and "serbest takdir" in v:
                q["options"][harf] = ATMA_YERINE[sira % len(ATMA_YERINE)]
                sira += 1
                atma += 1
                continue
            yeni = v
            for bul, koy in KIRP:
                yeni = re.sub(bul, koy, yeni)
            yeni = re.sub(r"\s+", " ", yeni).strip().rstrip(";").strip()
            if yeni != v:
                q["options"][harf] = yeni
                kirpilan += 1

    # ── 3. geçiş: kırpma sonrası aynı metne inen tekrarları çeşitlendir ──
    import collections
    sayac = collections.Counter(v for q in qs for h, v in q["options"].items()
                                if h != q["answer"])
    tekrarli = {v for v, n in sayac.items() if n >= 4 and len(v) > 40}
    cesit = 0
    idx = 0
    for q in qs:
        for harf, v in list(q["options"].items()):
            if harf == q["answer"] or v not in tekrarli:
                continue
            aday = TEKRAR_YERINE[idx % len(TEKRAR_YERINE)]
            idx += 1
            if aday not in q["options"].values():
                q["options"][harf] = aday
                cesit += 1

    # ── 5. geçiş: doğrunun ALTINA yazılmış çeldirici ────────────────────────
    for qid, degisim in KISALT.items():
        q = idx2[qid]
        d = len(q["options"][q["answer"]])
        for harf, yeni in degisim.items():
            assert harf != q["answer"], f"{qid}: DOĞRU şıkka dokunulamaz ({harf})"
            assert len(yeni) < d, f"{qid}/{harf}: {len(yeni)} ≥ doğru {d} — kısalmamış"
            q["options"][harf] = yeni

    for q in qs:
        assert len(set(q["options"].values())) == 5, f"{q['id']}: şık çakışması"

    # self-check: hedeflenen 3 soruda doğru EN UZUN, 7 soruda ORTADA olmalı
    hata = []
    for qid, degisim in KISALT.items():
        q = idx2[qid]
        o = q["options"]
        d = len(o[q["answer"]])
        bekle = "uzun" if len(degisim) == 4 else "orta"
        oldu = ("uzun" if d == max(len(v) for v in o.values())
                else "kısa" if d == min(len(v) for v in o.values()) else "orta")
        if oldu != bekle:
            hata.append((qid, bekle, oldu, d))
    if hata:
        print(f"⚠ {len(hata)} soru hedeflenen konuma gelmedi:")
        for qid, bekle, oldu, d in hata:
            print(f"   {qid}: beklenen '{bekle}' ↔ olan '{oldu}'  (doğru {d})")

    json.dump(qs, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    kalan = sum(1 for q in qs for h, v in q["options"].items()
                if h != q["answer"] and D.search(v))
    print(f"kırpılan dolgu: {kirpilan} | atma-şıkkı: {atma} | çeşitlendirilen tekrar: {cesit} "
          f"| kısaltılan çeldirici: {sum(len(v) for v in KISALT.values())} "
          f"| kalan kalıp: {kalan}")
