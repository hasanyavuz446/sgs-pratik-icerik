#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM Finansal Tablolar ve Analizi — Trend Analizi, 3×20."""
from topic_pack_builder import write_topic


def r(scenario, focus, correct, focus_correct, distractors, focus_distractors,
      why, focus_why, ref, difficulty="medium"):
    return {
        "scenario": scenario, "focus": focus,
        "correct": correct, "focus_correct": focus_correct,
        "distractors": distractors, "focus_distractors": focus_distractors,
        "why": why, "focus_why": focus_why, "ref": ref,
        "difficulty": difficulty,
    }


RULES = [
    r(
        "Analist 2022'yi baz yıl seçmiş, her finansal tablo kaleminin sonraki dört yıldaki tutarını 2022 tutarına oranlayarak endeksler oluşturmuştur. Hangi teknik uygulanmaktadır?",
        "Trend yüzdeleri yönteminin temel inceleme birimi nedir?",
        "Trend yani eğilim yüzdeleri analizi",
        "Aynı kalemin sabit bir baz yıla göre çok dönemli seyri",
        ["Dikey yüzde analizi", "Karşılaştırmalı tabloların iki dönemli değişim analizi", "Finansal oran analizi", "Nakit bütçesi analizi"],
        ["Aynı dönemde her kalemin toplam varlık veya satış içindeki yapısal payı", "Yalnız iki ardışık dönemin mutlak farkı", "İlişkili iki kalemin birbirine bölümü", "Gelecek dönemin tahmini nakit açığı"],
        "Sabit bir baz yıla göre birden çok dönemin endekslenmesi trend analizidir.",
        "Trend analizi, tek bir kalemin zaman içindeki uzun dönemli yönünü baz yıl karşısında gösterir.",
        "Finansal tablo analizi - trend yüzdeleri", "easy",
    ),
    r(
        "Baz yıl stok tutarı 100 kabul edilerek sonraki yılların stok endeksleri hesaplanmıştır. Trend yüzdesinin genel formülü hangisidir?",
        "Trend analizinde baz yıl endeksi kural olarak kaç kabul edilir?",
        "İlgili yıl tutarı / baz yıl tutarı × 100",
        "100 kabul edilir",
        ["Baz yıl tutarı / ilgili yıl tutarı × 100", "İlgili yıl eksi baz yıl", "Kalem tutarı / toplam varlık × 100", "Cari yıl tutarı / önceki yıl tutarı × 100"],
        ["0 kabul edilir", "1 kabul edilir", "50 kabul edilir", "İlgili kaleme göre değişken kabul edilir"],
        "Her dönem tutarı sabit baz yıl tutarına bölünür ve yüzle çarpılır.",
        "Baz yıl kendisine bölündüğü için endeksi 100'dür; 100'ün üzeri artışı, altı azalışı gösterir.",
        "Finansal tablo analizi - trend endeksi formülü", "easy",
    ),
    r(
        "İşletme olağan dışı düşük satış yaptığı grev yılını baz yıl seçmiştir. Sonraki dönem endeksleri çok yüksek çıkmıştır. Baz yıl seçimi uygun mudur?",
        "Sağlıklı trend analizi için baz yılın hangi özelliği taşıması beklenir?",
        "Hayır; olağan dışı baz, eğilimi abartılı gösterebilir",
        "Normal faaliyet koşullarını temsil eden karşılaştırılabilir bir dönem olması",
        ["Evet; en düşük tutarlı yıl daima en uygun karşılaştırma bazını oluşturur", "Evet; baz yılın ekonomik niteliği sonucu etkilemez", "Hayır; yalnız en son yıl baz seçilebilir", "Hayır; baz yıl endeksi sıfır olmalıdır"],
        ["Bütün kalemlerin sıfır olduğu bir dönem olması", "Mutlaka en yüksek kârın gerçekleştiği ve diğer dönemlerden ayrıştığı yıl olması", "Her analizde takvimdeki ilk yıl olması", "Sadece fiyatların en hızlı arttığı yıl olması"],
        "Anormal baz tutarı, sonraki dönemlerin göreli değişimini olduğundan büyük veya küçük gösterebilir.",
        "Baz yıl, işletmenin olağan yapısını ve karşılaştırılabilir muhasebe temelini mümkün olduğunca temsil etmelidir.",
        "Finansal tablo analizi - baz yıl seçimi", "medium",
    ),
    r(
        "Aynı finansal tablo kalemi beş dönem boyunca izlenmiştir. Bu nedenle trend analizi zaman boyutu bakımından nasıl sınıflandırılır?",
        "Trend analizi neden dinamik analiz niteliğindedir?",
        "Dinamik analiz",
        "Birden çok dönemdeki gelişimi ve yönü birlikte incelediği için",
        ["Statik analiz", "Kesit analizi", "Tek dönem analizi", "Dikey yapı analizi"],
        ["Bir kalemin birden çok dönemdeki değişim yönünü ve sürekliliğini izlediği için", "Kalemleri aynı dönem toplamına oranladığı için", "Gelecek sonucu kesinleştirdiği için", "Bütün tutarları parasal değerden çıkardığı için"],
        "Çok dönemli gelişmeyi inceleyen yöntemler dinamik analiz kapsamındadır.",
        "Trend dizisi, değişimin yalnız düzeyini değil sürekliliğini ve yönünü görmeyi sağlar.",
        "Finansal tablo analizi - dinamik analiz", "easy",
    ),
    r(
        "2024 baz yılından sonra 2025 ve 2026 tutarları ayrı ayrı 2024 tutarına bölünmüştür. 2026 hesabında 2025 tutarı payda yapılmamıştır. Bu uygulama doğru mudur?",
        "Sabit bazlı trend yüzdesi ile zincirleme değişim oranı arasındaki temel fark nedir?",
        "Evet; trend hesabında bütün dönemler aynı baz yıla oranlanır",
        "Trend sabit, zincirleme oran bir önceki dönemi baz alır",
        ["Hayır; her dönem yalnız kendisinden hemen önceki dönemin tutarına bölünmelidir", "Hayır; 2026 tutarı toplam varlığa bölünmelidir", "Evet; ancak baz yıl her dönemde değiştirilmelidir", "Hayır; trend hesabında tutarlar çıkarılır"],
        ["İki yöntem de her zaman aynı paydayı kullanır", "Trend yalnız tutar farkı, zincirleme oran yalnız dikey yüzde verir", "Zincirleme oran sabit baz, trend hareketli baz kullanır", "Trend sadece tek döneme uygulanabilir"],
        "Trend endekslerinin ortak paydası seçilen baz yıl tutarıdır.",
        "Sabit baz endeksleri uzun dönemli ortak referans sağlar; zincirleme oranlar ardışık dönem değişimini ölçer.",
        "Finansal tablo analizi - sabit baz ve zincirleme oran", "medium",
    ),
    r(
        "Net satışların trend endeksi 135 olarak hesaplanmıştır. Bu değer nasıl yorumlanır?",
        "Bir kalemin trend yüzdesinin 100'ün üzerinde olması neyi gösterir?",
        "Net satışlar baz yıla göre %35 artmıştır",
        "Kalem tutarının baz yıl düzeyinin üzerinde olduğunu",
        ["Net satışlar önceki yıla göre kesin olarak %135 artmıştır", "Net satışların toplam varlık payı %35'tir", "Net satışlar baz yıla göre %65 azalmıştır", "Baz yıl satışları cari yılın %135'idir"],
        ["Kalemin baz yıla göre artmış olsa bile mutlaka kâr yarattığını", "İlgili yıl tutarının sıfır olduğunu", "Kalemin toplam içindeki payının %100'ü aştığını", "Baz yılın bir önceki yıldan küçük olduğunu"],
        "135 endeksi, cari düzeyin baz yılın %135'i olduğunu; dolayısıyla %35 artışı ifade eder.",
        "100 üzerindeki endeks baz yıl tutarının aşıldığını gösterir, ancak ekonomik sonucu tek başına açıklamaz.",
        "Finansal tablo analizi - trend endeksi yorumu", "easy",
    ),
    r(
        "Nakit mevcudunun trend endeksi 72'dir. Baz yıla göre değişim nasıl ifade edilir?",
        "Trend yüzdesi 100'ün altında olan bir kalemin baz yıla göre azalış oranı nasıl bulunur?",
        "%28 azalış",
        "100'den trend endeksi çıkarılır",
        ["%72 artış", "%28 artış", "%72 azalış", "%172 artış"],
        ["Trend endeksinden 100 çıkarılır", "Endeks 100'e bölünmeden tutar sayılır", "Baz yıl endeksi cari endekse eklenir", "Kalem toplam varlığa bölünür"],
        "72 endeksi baz yıl düzeyinin %72'sine düşüldüğünü, yani %28 azalışı gösterir.",
        "Endeks 100'ün altındaysa baz yıla göre azalış 100 − endeks işlemidir.",
        "Finansal tablo analizi - azalan trend", "easy",
    ),
    r(
        "Baz yıldan sonra muhasebe politikası değiştirilmiş, eski dönem düzeltilmeden trend endeksleri hesaplanmıştır. Seri güvenilir midir?",
        "Trend serisinde muhasebe politikası, sınıflama veya kapsam değişiklikleri için hangi yaklaşım gerekir?",
        "Hayır; karşılaştırılabilirlik sağlanmadan eğilim yanıltıcı olabilir",
        "Veriler aynı temele getirilir veya fark açıklanır",
        ["Evet; endeksleme bütün muhasebe politikası ve kapsam farklarını otomatik olarak giderir", "Hayır; politika değişince hiçbir dönem analiz edilemez", "Evet; yalnız baz yıl tutarını ikiyle çarpmak yeterlidir", "Hayır; bütün endeksler 100 yapılmalıdır"],
        ["Değişiklik gizlenerek seri kesintisiz gösterilir", "Yalnız cari dönem tutarı sıfırlanır", "Baz yıl her değişiklikte rastgele seçilir", "Farklı kapsamlar aynı kabul edilerek işlem yapılmaz"],
        "Trend yöntemi ölçekleme yapar, farklı muhasebe temellerini kendiliğinden uyumlu hâle getirmez.",
        "Uzun dönemli seride yapay kırılmayı gerçek ekonomik eğilimden ayırmak için düzeltme veya açıklama gerekir.",
        "TMS 1 karşılaştırılabilirlik; finansal tablo analizi", "hard",
    ),
    r(
        "Satışların trend endeksi 140, satışların maliyetinin endeksi 170'tir. Analist yalnız satış artışını olumlu yorumlamıştır. Değerlendirme yeterli midir?",
        "Trend analizinde ilişkili kalemlerin endeksleri neden birlikte değerlendirilir?",
        "Hayır; maliyetin daha hızlı büyümesi brüt kârlılığı baskılayabilir",
        "Kalemlerin göreli büyüme hızları performansın yönünü açıklayabilir",
        ["Evet; satış endeksi 100'ü geçtiğinde maliyet hızından bağımsız olarak bütün sonuçlar olumludur", "Hayır; maliyet kalemine trend analizi uygulanamaz", "Evet; iki endeks arasındaki fark ekonomik anlam taşımaz", "Hayır; yalnız dikey yüzdeler birlikte incelenebilir"],
        ["Her kalem diğerlerinden tamamen bağımsız olduğu için endeks hızları birlikte yorumlanmaz", "Endeksler yalnız vergi hesabında kullanılır", "En büyük endeks her durumda en olumlu kalemdir", "İlişkili kalemlerin baz tutarı eşit olmak zorundadır"],
        "Maliyet satıştan hızlı artıyorsa satış büyümesine rağmen marj daralabilir.",
        "Satış-maliyet, alacak-satış ve stok-satış gibi ilişkiler trendin niteliğini anlamaya yardım eder.",
        "Finansal tablo analizi - ilişkili trendler", "medium",
    ),
    r(
        "Baz yıl tutarı sıfır olan yeni bir hesap için sonraki yıl trend endeksi hesaplanmak istenmiştir. Standart formül uygulanabilir mi?",
        "Baz yıl tutarı negatif olan zarar kalemlerinde trend endeksi nasıl değerlendirilmelidir?",
        "Hayır; sıfır paydayla trend yüzdesi tanımlı değildir",
        "İşaret dönüşümü açıklanır; mekanik endeks ihtiyatla yorumlanır",
        ["Evet; sonraki yıl endeksi otomatik olarak 100 kabul edilerek seri kesintisiz sürdürülür", "Evet; cari tutar doğrudan endeks kabul edilir", "Hayır; kalem finansal tablodan çıkarılır", "Evet; payda olarak toplam varlık kullanılır"],
        ["Negatif tutar mutlak değere çevrilerek işaret bilgisi gizlenir ve olağan artış gibi yorumlanır", "Endeks her durumda olumlu performans sayılır", "Baz tutar sıfır kabul edilip 100 yazılır", "Kalem yalnız net satışlara oranlanır"],
        "Baz tutarı sıfırsa bölme işlemi tanımsızdır; tutarsal gelişim ayrıca açıklanır.",
        "Negatiften pozitife veya tersine geçiş sıradan artış endeksi gibi yorumlanamaz; yön ve neden görünür kılınır.",
        "Finansal tablo analizi - sorunlu trend bazları", "hard",
    ),
]


CALCS = [
    r("Baz yıl net satışları 1.000 bin TL, 2026 net satışları 1.300 bin TL'dir. 2026 trend yüzdesi kaçtır?", "Baz yıl satışları 1.000 bin TL ve 2026 trend endeksi 130 ise 2026 satışları kaç bin TL'dir?", "%130", "1.300 bin TL", ["%30", "%76,92", "%100", "%230"], ["300 bin TL", "770 bin TL", "1.030 bin TL", "2.300 bin TL"], "Trend endeksi 1.300 / 1.000 × 100 = 130'dur.", "2026 satışları 1.000 × 1,30 = 1.300 bin TL'dir.", "Finansal tablo analizi - satış trendi", "easy"),
    r("Baz yıl stokları 800 bin TL, 2026 stokları 680 bin TL'dir. Stok trend endeksi kaçtır?", "2026 stokları 680 bin TL ve trend endeksi 85 ise baz yıl stokları kaç bin TL'dir?", "%85", "800 bin TL", ["%15", "%82,35", "%117,65", "%185"], ["102 bin TL", "578 bin TL", "765 bin TL", "1.480 bin TL"], "Stok endeksi 680 / 800 × 100 = 85'tir.", "Baz yıl stoku 680 / 0,85 = 800 bin TL'dir.", "Finansal tablo analizi - stok trendi", "easy"),
    r("Ticari alacaklar baz yılda 500 bin TL, 2026'da 750 bin TL'dir. Alacak trend yüzdesi kaçtır?", "Ticari alacak endeksi 150 ise baz yıla göre artış oranı yüzde kaçtır?", "%150", "%50", ["%33,33", "%50", "%100", "%250"], ["%25", "%33,33", "%100", "%150"], "Alacak endeksi 750 / 500 × 100 = 150'dir.", "150 endeksi baz yıl düzeyinin %50 aşıldığını gösterir.", "Finansal tablo analizi - alacak trendi", "easy"),
    r("Satışların maliyeti baz yılda 1.800 bin TL, 2026'da 2.340 bin TL'dir. Trend endeksi kaçtır?", "Aynı baz yılda satış endeksi 118, maliyet endeksi 130 ise hangi sonuç daha güçlüdür?", "%130", "Maliyet satıştan hızlı artmış; brüt marj baskılanabilir", ["%30", "%76,92", "%100", "%230"], ["Satış maliyetten hızlı artmış ve brüt marj kesin olarak yükselmiştir", "Brüt marj kesin olarak yükselmiştir", "İki kalem aynı hızda değişmiştir", "Endeksler farklı bazlarla hesaplanmak zorundadır"], "Maliyet endeksi 2.340 / 1.800 × 100 = 130'dur.", "Ortak bazda maliyet endeksinin satış endeksini aşması, maliyetlerin daha hızlı büyüdüğünü gösterir.", "Finansal tablo analizi - satış maliyeti trendi", "medium"),
    r("Brüt kâr baz yılda 600 bin TL, 2026'da 900 bin TL'dir. Brüt kâr endeksi kaçtır?", "Brüt kâr trend endeksi 150 ve 2026 brüt kârı 900 bin TL ise baz yıl brüt kârı kaç bin TL'dir?", "%150", "600 bin TL", ["%50", "%66,67", "%100", "%250"], ["450 bin TL", "750 bin TL", "1.050 bin TL", "1.350 bin TL"], "Brüt kâr endeksi 900 / 600 × 100 = 150'dir.", "Baz yıl kârı 900 / 1,50 = 600 bin TL'dir.", "Finansal tablo analizi - brüt kâr trendi", "easy"),
    r("Faaliyet giderleri baz yılda 400 bin TL, 2026'da 520 bin TL'dir. Gider trend endeksi kaçtır?", "Faaliyet gideri endeksi 130, satış endeksi 145 ise satışların giderlerden kaç endeks puanı daha hızlı geliştiği görülür?", "%130", "15 endeks puanı", ["%30", "%76,92", "%120", "%230"], ["10 endeks puanı", "30 endeks puanı", "45 endeks puanı", "275 endeks puanı"], "Gider endeksi 520 / 400 × 100 = 130'dur.", "Ortak bazlı endeks farkı 145 − 130 = 15 puandır.", "Finansal tablo analizi - faaliyet gideri trendi", "medium"),
    r("Net dönem kârı baz yılda 300 bin TL, 2026'da 240 bin TL'dir. Kâr trend endeksi kaçtır?", "Net kâr endeksi 80 olduğunda baz yıla göre değişim nasıl ifade edilir?", "%80", "%20 azalış", ["%20", "%60", "%120", "%180"], ["%20 artış", "%80 artış", "%80 azalış", "%180 artış"], "Net kâr endeksi 240 / 300 × 100 = 80'dir.", "80 endeksi kârın baz yılın %80'ine indiğini, yani %20 azaldığını gösterir.", "Finansal tablo analizi - kâr trendi", "easy"),
    r("Toplam varlıklar baz yılda 2.000 bin TL, 2026'da 3.000 bin TL'dir. Varlık trend endeksi kaçtır?", "Toplam varlık endeksi 150 ve baz yıl tutarı 2.000 bin TL ise artış tutarı kaç bin TL'dir?", "%150", "1.000 bin TL", ["%50", "%66,67", "%100", "%250"], ["500 bin TL", "1.500 bin TL", "2.000 bin TL", "3.000 bin TL"], "Varlık endeksi 3.000 / 2.000 × 100 = 150'dir.", "%50 artış, 2.000 × 0,50 = 1.000 bin TL'dir.", "Finansal tablo analizi - varlık trendi", "easy"),
    r("Dönen varlıklar baz yılda 1.200 bin TL iken 2026 endeksi 125 olmuştur. 2026 dönen varlık tutarı kaç bin TL'dir?", "2026 dönen varlık tutarı 1.500 bin TL ve baz yıla göre artış 300 bin TL ise trend endeksi kaçtır?", "1.500 bin TL", "%125", ["300 bin TL", "960 bin TL", "1.325 bin TL", "2.700 bin TL"], ["%20", "%80", "%120", "%500"], "2026 tutarı 1.200 × 1,25 = 1.500 bin TL'dir.", "Baz tutar 1.200 bin TL olduğundan endeks 1.500 / 1.200 × 100 = 125'tir.", "Finansal tablo analizi - dönen varlık trendi", "medium"),
    r("Toplam borçların trend endeksi 160, toplam varlıkların endeksi 130'dur. Ortak baz yıl karşısında hangi yorum yapılabilir?", "Baz yıl borcu 1.000 bin TL, borç endeksi 160 ve 2026 varlığı 2.600 bin TL ise 2026 borçların varlıklara oranı kaçtır?", "Borçlar varlıklardan daha hızlı büyümüş, finansal risk artmış olabilir", "%61,54", ["Varlıklar borçlardan 30 puan hızlı büyümüş ve finansal risk kesin olarak azalmıştır", "Borçların tutarı varlıkların kesin olarak üzerindedir", "İki kalem aynı oranda değişmiştir", "Borç endeksi yalnız dikey payı gösterir"], ["%38,46", "%60", "%62,5", "%160"], "Endeks hızı borçlarda daha yüksektir; ancak düzey ve risk yorumu diğer verilerle desteklenmelidir.", "2026 borç 1.000 × 1,60 = 1.600 bin TL; oran 1.600 / 2.600 × 100 = %61,54'tür.", "Finansal tablo analizi - borç trendi", "hard"),
    r("Özkaynaklar baz yılda 1.500 bin TL, 2026'da 1.800 bin TL'dir. Özkaynak trend endeksi kaçtır?", "Özkaynak endeksi 120 ise baz yıla göre artış oranı ve 1.800 bin TL cari tutardan baz tutar sırasıyla nedir?", "%120", "%20 ve 1.500 bin TL", ["%20", "%83,33", "%100", "%220"], ["%20 ve 300 bin TL", "%80 ve 1.440 bin TL", "%120 ve 1.500 bin TL", "%220 ve 3.960 bin TL"], "Özkaynak endeksi 1.800 / 1.500 × 100 = 120'dir.", "120 endeksi %20 artış demektir; baz tutar 1.800 / 1,20 = 1.500 bin TL'dir.", "Finansal tablo analizi - özkaynak trendi", "medium"),
    r("Nakit baz yılda 400 bin TL, 2026'da 300 bin TL'dir. Nakit trend endeksi kaçtır?", "Nakit endeksi 75 iken ticari borç endeksi 140 ise likidite açısından hangi ön bulgu elde edilir?", "%75", "Nakit azalırken borçların artması ödeme baskısına işaret edebilir", ["%25", "%100", "%125", "%175"], ["Nakit borçlardan daha hızlı artmış, ödeme kapasitesi kesin olarak güçlenmiştir", "Her iki kalem %15 azalmıştır", "Borçların nakde eşit olduğu kesinleşmiştir", "Endeksler likidite hakkında hiçbir ön bilgi vermez"], "Nakit endeksi 300 / 400 × 100 = 75'tir.", "Nakit %25 azalırken borçların %40 artması ödeme kapasitesi bakımından olumsuz bir yön göstergesidir.", "Finansal tablo analizi - nakit ve borç trendi", "hard"),
    r("Bir kalemin baz yıl tutarı 1.000, ikinci yıl 1.200, üçüncü yıl 900 bin TL'dir. Sabit bazlı ikinci ve üçüncü yıl endeksleri nedir?", "İkinci yıl 1.200 bin TL'den üçüncü yıl 900 bin TL'ye inen kalemin iki yıl arasındaki değişim oranı kaçtır?", "%120 ve %90", "%25 azalış", ["%120 ve %75", "%100 ve %90", "%20 ve %-10", "%220 ve %190"], ["%10 azalış", "%20 azalış", "%25 artış", "%30 azalış"], "Sabit baz endeksleri sırasıyla 1.200 / 1.000 × 100 = 120 ve 900 / 1.000 × 100 = 90'dır.", "Ardışık değişim (900 − 1.200) / 1.200 × 100 = %-25'tir; bu, 90 − 120 endeks puanından farklıdır.", "Finansal tablo analizi - sabit baz ve dönem değişimi", "hard"),
    r("Satış trend endeksi 140, satışların maliyeti endeksi 155'tir. Ortak baz yıl kullanıldığına göre hangi kalem daha hızlı artmıştır?", "Baz yıl satışları 5.000, maliyeti 3.000 bin TL; endeksler sırasıyla 140 ve 155 ise 2026 brüt kârı kaç bin TL'dir?", "Satışların maliyeti 15 endeks puanı daha hızlı artmıştır", "2.350 bin TL", ["Satışlar 15 endeks puanı daha hızlı artmış ve brüt marj kesin yükselmiştir", "İki kalem aynı hızda artmıştır", "Maliyet satışlardan %95 daha hızlı artmıştır", "Tutarlar bilinmeden endeks hızı karşılaştırılamaz"], ["1.650 bin TL", "2.000 bin TL", "3.500 bin TL", "4.650 bin TL"], "155 maliyet endeksi, 140 satış endeksinden 15 puan yüksektir.", "2026 satış 7.000, maliyet 4.650 bin TL; brüt kâr 2.350 bin TL'dir.", "Finansal tablo analizi - ilişkili kalem trendi", "hard"),
    r("2024 satışları 1.000, 2025 satışları 1.200 ve 2026 satışları 1.500 bin TL'dir. 2024 bazlı 2025 ve 2026 endeksleri nedir?", "2025'ten 2026'ya satışların zincirleme artış oranı kaçtır?", "%120 ve %150", "%25", ["%120 ve %125", "%100 ve %150", "%20 ve %50", "%220 ve %250"], ["%20", "%30", "%50", "%125"], "Sabit bazlı endeksler 1.200 / 1.000 = 120 ve 1.500 / 1.000 = 150'dir.", "Ardışık dönem artışı (1.500 − 1.200) / 1.200 × 100 = %25'tir.", "Finansal tablo analizi - trend ve zincirleme değişim", "hard"),
    r("Baz yıl finansman gideri 200 bin TL, 2026 tutarı 310 bin TL'dir. Trend endeksi kaçtır?", "Finansman gideri endeksi 155, faaliyet kârı endeksi 115 ise hangi yönsel değerlendirme yapılabilir?", "%155", "Finansman yükü faaliyet kârından daha hızlı artmıştır", ["%55", "%64,52", "%100", "%255"], ["Faaliyet kârı finansman yükünden 40 puan daha hızlı artmış ve baskı azalmıştır", "İki kalem aynı hızda büyümüştür", "Finansman gideri baz yıla göre azalmıştır", "Endeksler yalnız tutarların eşit olduğunu gösterir"], "Finansman gideri endeksi 310 / 200 × 100 = 155'tir.", "Finansman giderinin endeks hızı faaliyet kârından 40 puan yüksektir; bu durum kârlılık baskısı yaratabilir.", "Finansal tablo analizi - finansman gideri trendi", "medium"),
]

RULES.extend(CALCS)


PREMISES = [
    {"stem":"Trend analizi bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Sabit bir baz yıl seçilir\n\nII. Aynı kalemin çok dönemli seyri izlenir\n\nIII. Baz yıl endeksi 100 kabul edilir","correct":"I, II ve III","why":"Trend analizinin sabit baz, çok dönem ve 100 endeksli üç temel özelliği de doğrudur.","ref":"Finansal tablo analizi - trend yüzdeleri","difficulty":"easy"},
    {"stem":"Trend endeksi hesabı bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İlgili yıl tutarı baz yıl tutarına bölünür\n\nII. Sonuç yüzle çarpılır\n\nIII. Bütün yıllarda aynı baz tutar kullanılır","correct":"I, II ve III","why":"Sabit bazlı trend dizisi her dönemi aynı baz yıl tutarına oranlar.","ref":"Finansal tablo analizi - trend formülü","difficulty":"easy"},
    {"stem":"Baz yıl seçimi bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Olağan faaliyet koşullarını temsil etmelidir\n\nII. Karşılaştırılabilir veri sunmalıdır\n\nIII. Her zaman en düşük tutarlı yıl seçilmelidir","correct":"I ve II","why":"Temsil gücü ve karşılaştırılabilirlik aranır; en düşük tutarın seçilmesi diye bir kural yoktur.","ref":"Finansal tablo analizi - baz yıl seçimi","difficulty":"medium"},
    {"stem":"Trend endeksi yorumu bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. 130 endeksi %130 artış demektir\n\nII. 130 endeksi baz yıla göre %30 artışı gösterir\n\nIII. 75 endeksi baz yıla göre %25 azalışı gösterir","correct":"II ve III","why":"Endeksteki 100'ü aşan veya eksik kalan bölüm değişim oranıdır; I bu nedenle yanlıştır.","ref":"Finansal tablo analizi - endeks yorumu","difficulty":"medium"},
    {"stem":"Trend serisinin karşılaştırılabilirliği bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Muhasebe politikası farkları dikkate alınır\n\nII. Endeksleme bütün kapsam farklarını kendiliğinden giderir\n\nIII. Yapısal kırılmalar açıklanır","correct":"I ve III","why":"Politika ve kapsam farkları gerçek eğilimi bozabilir; endeksleme bunları otomatik olarak düzeltmez.","ref":"TMS 1 karşılaştırılabilirlik; finansal tablo analizi","difficulty":"hard"},
    {"stem":"İlişkili kalemlerin trendleri bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Her yüksek endeks tek başına olumlu sonuçtur\n\nII. Satış ve maliyet büyüme hızları birlikte incelenir\n\nIII. Alacakların satıştan hızlı artması tahsilat riski gösterebilir","correct":"II ve III","why":"Endeksin anlamı kalemin niteliğine ve ilişkilerine bağlıdır; yüksek maliyet veya alacak endeksi tek başına olumlu değildir.","ref":"Finansal tablo analizi - ilişkili trendler","difficulty":"hard"},
    {"stem":"Sabit ve hareketli baz karşılaştırması bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Trend endeksi her dönemi ortak baz yıla oranlar\n\nII. Zincirleme oran ardışık dönemleri karşılaştırır\n\nIII. İki yöntem her durumda aynı sonucu verir","correct":"I ve II","why":"Paydalar farklı olduğu için sabit baz endeksi ile ardışık değişim oranı aynı ölçü değildir.","ref":"Finansal tablo analizi - sabit baz ve zincirleme oran","difficulty":"medium"},
    {"stem":"Sorunlu trend bazları bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Sıfır baz tutarı standart endeksi tanımsız kılar\n\nII. Negatif baz her durumda olağan büyüme gibi yorumlanır\n\nIII. İşaret dönüşümü ayrıca açıklanmalıdır","correct":"I ve III","why":"Sıfır payda hesaplamayı engeller; negatif veya işaret değiştiren kalemlerde mekanik yorum yanıltıcıdır.","ref":"Finansal tablo analizi - sorunlu trend bazları","difficulty":"hard"},
]


if __name__ == "__main__":
    write_topic(
        lesson_id="mali_tablolar_analizi", topic_id="trend_analizi",
        label="Trend Analizi", slug="trend_analizi", prefix="topic-tra",
        seed=2026071745,
        legislation_version="SMMM Finansal Tablolar ve Analizi müfredatı; trend (eğilim yüzdeleri) analizi (17.07.2026 kontrolü)",
        rules=RULES, premises=PREMISES, wrong_banks={},
    )
