#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM Finansal Tablolar ve Analizi — Karşılaştırmalı Analiz, 3×20."""
from topic_pack_builder import write_topic


def tr(value):
    value = round(value, 2)
    if abs(value - round(value)) < 1e-9:
        return f"{int(round(value)):,}".replace(",", ".")
    return f"{value:,.2f}".replace(",", "\0").replace(".", ",").replace("\0", ".")


def n(value, unit=""):
    return f"{tr(value)}{unit}"


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
        "Analist aynı bilanço kaleminin 2025 ve 2026 tutarlarını yan yana getirip hem TL değişimini hem değişim yüzdesini hesaplamaktadır. Hangi teknik uygulanmaktadır?",
        "Karşılaştırmalı tablolar analizinin temel inceleme birimi nedir?",
        "Karşılaştırmalı yani yatay analiz",
        "Aynı kalemin dönemler arasındaki tutar ve yüzde değişimi",
        ["Dikey yüzde yöntemi", "Oran analizi", "Baz dönemli trend endeksi yöntemi", "Nakit akış bütçesi"],
        ["Aynı dönemde her kalemin toplam içindeki payı", "Bir baz yıla göre bütün dönemlerin endeksi", "İki farklı kalemin birbirine bölünmesi", "Gelecek dönemin tahmini nakit giriş ve çıkış dengesinin kurulması"],
        "Aynı kalemin dönemler arasındaki mutlak ve yüzde değişimini incelemek karşılaştırmalı, diğer adıyla yatay analizdir.",
        "Karşılaştırmalı analiz dönemler arası değişime odaklanır; aynı dönem içindeki yapısal paylar dikey analizin konusudur.",
        "Finansal tablo analizi - karşılaştırmalı analiz", "easy",
    ),
    r(
        "Cari dönem tutarından önceki dönem tutarı çıkarılmıştır. Hesaplanan büyüklük neyi gösterir?",
        "Yatay analizde artış veya azalış tutarı hangi işlemle bulunur?",
        "Mutlak değişim tutarını gösterir",
        "Cari dönem tutarından önceki dönem tutarı çıkarılır",
        ["Dikey yüzde payını gösterir", "Trend baz yılını gösterir", "Finansal kaldıraç oranını gösterir", "Nakit benzeri tutarını gösterir"],
        ["Önceki dönem cari döneme bölünür", "İki dönem tutarı birbiriyle çarpılır", "Cari dönem tutarı aynı dönemin toplam varlık veya satış tutarına bölünür", "Yalnız cari dönem tutarı yüzle çarpılır"],
        "Mutlak değişim cari dönem eksi önceki dönemdir; sonuç artışta pozitif, azalışta negatif olur.",
        "Değişim tutarı dönemler arasındaki parasal farktır ve yüzde değişimin payını oluşturur.",
        "Finansal tablo analizi - mutlak değişim", "easy",
    ),
    r(
        "Bir kalemin cari dönem artışı önceki dönem tutarına bölünüp yüzle çarpılmıştır. Sonuç neyi ifade eder?",
        "Karşılaştırmalı analizde yüzde değişimin paydası kural olarak hangi tutardır?",
        "Önceki döneme göre yüzde değişimi",
        "Önceki dönem tutarıdır",
        ["Cari dönemin dikey analiz yüzdesini", "Baz yılın trend endeksini", "Toplam varlık devir hızını", "Nakit dönüşüm süresini"],
        ["Cari dönem tutarıdır", "İki dönemin toplamıdır", "Dönemlerin aritmetik ortalamasıdır", "Toplam varlık tutarıdır"],
        "Yüzde değişim = (Cari − Önceki) / Önceki × 100 formülüyle bulunur.",
        "Önceki dönem karşılaştırmanın başlangıç noktasıdır; cari tutarı payda almak farklı bir sonuç verir.",
        "Finansal tablo analizi - yüzde değişim", "easy",
    ),
    r(
        "Bir kalem önceki dönemde sıfır, cari dönemde 200 bin TL'dir. Analist standart yüzde değişim hesaplamıştır. Bu hesap anlamlı mıdır?",
        "Önceki dönem tutarı sıfır olduğunda yatay analizde yüzde değişim için hangi yaklaşım uygundur?",
        "Hayır; sıfıra bölme nedeniyle yüzde değişim hesaplanamaz",
        "Mutlak artış gösterilir, yüzde değişim hesaplanamaz diye açıklanır",
        ["Evet; yüzde değişim otomatik olarak %100 kabul edilir", "Evet; cari tutar doğrudan yüzde değişim sayılır", "Hayır; kalem finansal tablodan tamamen çıkarılır", "Evet; önceki dönem sıfır olduğunda payda olarak toplam varlık tutarı kullanılır"],
        ["Yüzde değişim %0 yazılır", "Yüzde değişim %200 yazılır", "Cari dönem tutarı önceki döneme bölünür", "Kalem, karşılaştırma yapılabilmesi için zorunlu olarak duran varlıklara aktarılır"],
        "Önceki dönem sıfırsa standart formülün paydası sıfır olur; yüzde değişim tanımlı değildir, mutlak artış açıklanır.",
        "Kullanıcıya değişimin büyüklüğü verilir, ancak matematiksel olarak anlamsız bir yüzde üretilmez.",
        "Finansal tablo analizi - sıfır baz sorunu", "medium",
    ),
    r(
        "Önceki dönem tutarı negatif olan bir zarar kalemi cari dönemde pozitife dönmüştür. Tek başına standart yüzde değişim yorumu yeterli midir?",
        "İşaret değiştiren finansal kalemlerde karşılaştırmalı analiz sonucu nasıl sunulmalıdır?",
        "Hayır; işaret değişimi ayrıca açıklanmalı ve dikkatle yorumlanmalıdır",
        "Tutarlar ve işaret dönüşümü birlikte açıklanmalıdır",
        ["Evet; sonuç her durumda olağan satış artışı olarak yorumlanır", "Hayır; iki dönem de sıfır kabul edilmelidir", "Evet; negatif tutar mutlak değere çevrilmeden silinir", "Hayır; yalnız dikey analiz yapılması yasaktır"],
        ["Yalnız mutlak değerler kullanılarak işaret gizlenmelidir", "Önceki dönem otomatik olarak 100 kabul edilmelidir", "Cari dönem tutarı finansal tablodan çıkarılmalıdır", "Değişim her durumda olumlu performans sayılmalıdır"],
        "Negatiften pozitife veya tersine dönüşte mekanik yüzde, ekonomik değişimi yanıltabilir; tutar, işaret ve neden birlikte açıklanır.",
        "Kâr-zarar dönüşümü sıradan bir artış yüzdesi gibi sunulmamalı, nitel değişim görünür kılınmalıdır.",
        "Finansal tablo analizi - negatif baz ve yorum", "hard",
    ),
    r(
        "Satışlar %20, satışların maliyeti %35 artmıştır. Analist yalnız satış artışını olumlu görmüştür. Bu yorum yeterli midir?",
        "Karşılaştırmalı analizde ilişkili kalemlerin birlikte değerlendirilmesi neden önemlidir?",
        "Hayır; maliyet daha hızlı arttığı için brüt marj baskılanabilir",
        "Değişimin performans etkisi ilişkili kalemlerin yön ve hızına bağlıdır",
        ["Evet; satış artışı bütün maliyet etkilerini her zaman yok eder", "Hayır; maliyet artışı finansal tablolarda gösterilemez", "Evet; iki kalem arasındaki fark hiçbir bilgi taşımaz", "Hayır; satış ve maliyet yalnız bilançoda karşılaştırılır"],
        ["Her kalem bütünüyle bağımsız olduğundan aralarındaki ekonomik bağ kurulmadan ayrı yorumlanır", "Yüzde değişimler yalnız vergi matrahı için hesaplanır", "İlişkili kalemlerin tutarı aynı kabul edilmelidir", "Yalnız en yüksek yüzdeye sahip kalem raporlanır"],
        "Maliyet satıştan hızlı büyürse brüt kâr marjı daralabilir; tek kalemdeki artış performans için yeterli kanıt değildir.",
        "Satış-maliyet, alacak-satış veya borç-varlık gibi ekonomik ilişkiler değişimin sürdürülebilirliğini anlamaya yardım eder.",
        "Finansal tablo analizi - ilişkili kalem yorumu", "medium",
    ),
    r(
        "İki dönemin finansal tablolarında aynı stok işlemi farklı muhasebe politikalarıyla ölçülmüş, etkisi düzeltilmeden yatay analiz yapılmıştır. Sonuç güvenilir midir?",
        "Karşılaştırmalı analiz öncesinde muhasebe politikası ve sınıflama farklılıkları için ne yapılmalıdır?",
        "Hayır; karşılaştırılabilirlik sağlanmadan değişim yanıltıcı olabilir",
        "Mümkünse yeniden sınıflandırma veya düzeltme yapılmalı ve fark açıklanmalıdır",
        ["Evet; muhasebe politikaları dönem karşılaştırmasını etkilemez", "Hayır; bütün geçmiş tablolar yok edilmelidir", "Evet; yalnız cari dönem politikası açıklanırsa fark ortadan kalkar", "Hayır; her kalem otomatik olarak nakde çevrilmelidir"],
        ["Politika değişikliği, karşılaştırmayı etkilemediği varsayılarak yeniden sınıflandırma yapılmadan sunulmalıdır", "Yalnız cari dönem tutarı sıfırlanmalıdır", "Dönemler birbirinden bağımsız olduğu için işlem yapılmaz", "Önceki dönem bütün kalemleri özkaynağa aktarılır"],
        "Politika ve sınıflama farkları ekonomik değişim olmayan yapay sapmalar yaratabilir; karşılaştırma aynı temele getirilmelidir.",
        "Yeniden sınıflandırma mümkün değilse niteliği, nedeni ve tutarı açıklanarak kullanıcı uyarılır.",
        "TMS 1 karşılaştırmalı bilgi; finansal tablo analizi", "medium",
    ),
    r(
        "İşletme dönem içinde büyük bir şirket satın almış, varlıkları bu nedenle artmıştır. Analist artışı tamamen organik büyüme saymıştır. Doğru mudur?",
        "Yapısal değişiklikler yatay analiz sonuçlarının yorumunu nasıl etkiler?",
        "Hayır; satın alma etkisi organik değişimden ayrıştırılmalıdır",
        "Birleşme, bölünme ve faaliyet değişiklikleri ayrıca dikkate alınmalıdır",
        ["Evet; her varlık artışı satış başarısının kesin kanıtıdır", "Hayır; satın alınan varlıklar finansal tabloya alınmaz", "Evet; işletme birleşmeleri karşılaştırılabilirliği artırır", "Hayır; analiz yalnız satın alma bedeline uygulanır"],
        ["Birleşme ve bölünmeler yalnız özkaynağı etkilediğinden diğer kalemlerin dönemsel karşılaştırmasını değiştirmez", "Yalnız işletmenin unvanı değiştiğinde açıklama gerekir", "Yapısal etkiler her zaman olağan faaliyet sayılır", "Karşılaştırmalı analiz satın alma döneminde yasaktır"],
        "Birleşme gibi kapsam değişiklikleri kalem artışının kaynağını değiştirir; organik performans ile satın alma etkisi ayrılmalıdır.",
        "Yapısal olaylar dönem verilerinin aynı ekonomik kapsamı temsil edip etmediğini etkiler.",
        "Finansal tablo analizi - karşılaştırılabilirlik sınırlılıkları", "medium",
    ),
    r(
        "Yüksek enflasyon ortamında iki yılın nominal TL tutarları hiçbir düzeltme yapılmadan karşılaştırılmıştır. Yorumda hangi risk vardır?",
        "Fiyat düzeyi değişimleri karşılaştırmalı analizi hangi yönden sınırlar?",
        "Nominal artış gerçek hacim artışı sanılabilir",
        "Paranın satın alma gücü farkı dönem tutarlarını karşılaştırılamaz kılabilir",
        ["Enflasyon bütün kalemleri reel olarak aynı oranda büyütür", "Nominal tutarlar her zaman reel performansı tam gösterir", "Fiyat değişimi yalnız nakit akışlarını etkiler", "Enflasyon karşılaştırmalı analizi zorunlu olarak kaldırır"],
        ["Fiyat düzeyi yalnız cevap harflerini değiştirir", "Nominal tutarlar fiyat değişimlerinden arındırıldığı için her koşulda reel performansı eksiksiz gösterir", "Enflasyon yalnız önceki dönem dipnotlarını etkiler", "Satın alma gücü değişimi hiçbir kaleme yansımaz"],
        "Nominal tutardaki artış fiyat düzeyi artışından kaynaklanabilir; reel büyüme için karşılaştırılabilir ölçü birimi gerekir.",
        "Özellikle uzun dönemli yatay analizde farklı satın alma gücündeki paraların doğrudan karşılaştırılması yanıltıcı olabilir.",
        "Finansal tablo analizi - fiyat düzeyi etkisi", "hard",
    ),
    r(
        "Cari dönemde 40 bin TL artan küçük bir kalem %200, 2 milyon TL artan büyük bir kalem %8 büyümüştür. Yalnız en yüksek yüzdeye odaklanmak doğru mudur?",
        "Mutlak değişim ile yüzde değişim neden birlikte sunulmalıdır?",
        "Hayır; parasal büyüklük ve göreli hız birlikte değerlendirilmelidir",
        "Biri ekonomik büyüklüğü, diğeri başlangıç bazına göre değişim hızını gösterir",
        ["Evet; en yüksek yüzde her zaman en önemli etkidir", "Hayır; yüzde değişim hiçbir zaman hesaplanmaz", "Evet; mutlak tutarların finansal analizde anlamı yoktur", "Hayır; iki değişim doğrudan toplanmalıdır"],
        ["İki ölçü her durumda aynı bilgiyi verir", "Mutlak tutar yalnız oran analizinde kullanılır", "Yüzde değişim cari dönemin yapısal payını, mutlak değişim baz yıl endeksini verir", "Parasal değişim baz yıl endeksidir"],
        "Küçük baz yüksek yüzde yaratabilir; karar etkisi için mutlak büyüklük de görülmelidir.",
        "Mutlak değişim kaç TL fark olduğunu, yüzde değişim bu farkın önceki tutara göre büyüklüğünü açıklar.",
        "Finansal tablo analizi - mutlak ve göreli değişim", "medium",
    ),
]


CALCS = [
    ("Ticari alacaklar", 400, 520, "Önceki dönem ticari alacak 400 bin TL, cari dönem 520 bin TL'dir. Mutlak artış kaç bin TL'dir?", "Ticari alacaklardaki artış %30 ve önceki tutar 400 bin TL ise cari tutar kaç bin TL'dir?", n(120," bin TL"), n(520," bin TL"), [n(80," bin TL"),n(100," bin TL"),n(400," bin TL"),n(920," bin TL")], [n(120," bin TL"),n(430," bin TL"),n(480," bin TL"),n(700," bin TL")]),
    ("Stoklar", 600, 510, "Stoklar 600 bin TL'den 510 bin TL'ye gerilemiştir. Yatay analizde yüzde değişim kaçtır?", "Stoklardaki azalış 90 bin TL ve azalış oranı %15 ise önceki dönem stoku kaç bin TL'dir?", n(-15,"%"), n(600," bin TL"), [n(-20,"%"),n(-12.5,"%"),n(17.65,"%"),n(85,"%")], [n(90," bin TL"),n(510," bin TL"),n(690," bin TL"),n(765," bin TL")]),
    ("Net satışlar", 2400, 3000, "Net satışlar 2.400 bin TL'den 3.000 bin TL'ye çıkmıştır. Artış yüzdesi kaçtır?", "Net satışların cari tutarı 3.000 bin TL ve artış oranı %25 ise önceki dönem tutarı kaç bin TL'dir?", n(25,"%"), n(2400," bin TL"), [n(20,"%"),n(60,"%"),n(80,"%"),n(125,"%")], [n(600," bin TL"),n(2250," bin TL"),n(2500," bin TL"),n(3750," bin TL")]),
    ("Satışların maliyeti", 1500, 1950, "Satışların maliyeti iki dönem arasında 450 bin TL artarak 1.950 bin TL olmuştur. Önceki dönem tutarı kaç bin TL'dir?", "Önceki dönem satışların maliyeti 1.500 bin TL, cari dönem 1.950 bin TL ise mutlak ve yüzde artış hangi seçenektedir?", n(1500," bin TL"), "450 bin TL ve %30", [n(450," bin TL"),n(1050," bin TL"),n(1950," bin TL"),n(3450," bin TL")], ["300 bin TL ve %20","450 bin TL ve %23,08","1.500 bin TL ve %30","1.950 bin TL ve %130"]),
    ("Brüt kâr", 900, 1050, "Brüt kâr önceki dönemde 900 bin TL, cari dönemde 1.050 bin TL'dir. Mutlak değişim kaç bin TL'dir?", "Brüt kâr 150 bin TL artarak 1.050 bin TL olmuşsa artış oranı yüzde kaçtır?", n(150," bin TL"), n(150/900*100,"%"), [n(50," bin TL"),n(900," bin TL"),n(1050," bin TL"),n(1950," bin TL")], [n(14.29,"%"),n(15,"%"),n(85.71,"%"),n(116.67,"%")]),
    ("Faaliyet giderleri", 480, 600, "Faaliyet giderlerindeki 120 bin TL artış önceki dönem tutarı 480 bin TL'ye göre yüzde kaçtır?", "Faaliyet giderleri %25 artarak 600 bin TL olmuşsa artış tutarı kaç bin TL'dir?", n(25,"%"), n(120," bin TL"), [n(20,"%"),n(80,"%"),n(120,"%"),n(125,"%")], [n(25," bin TL"),n(100," bin TL"),n(480," bin TL"),n(750," bin TL")]),
    ("Net dönem kârı", 300, 390, "Net dönem kârının 300 bin TL'den 390 bin TL'ye çıkması kaç bin TL artış demektir?", "Net dönem kârı %30 yükselerek 390 bin TL'ye ulaştıysa önceki dönem kârı kaç bin TL'dir?", n(90," bin TL"), n(300," bin TL"), [n(30," bin TL"),n(90.3," bin TL"),n(300," bin TL"),n(690," bin TL")], [n(90," bin TL"),n(273," bin TL"),n(360," bin TL"),n(507," bin TL")]),
    ("Dönen varlıklar", 1200, 1500, "Dönen varlıkların dönemler arasındaki artış oranı için 1.200 ve 1.500 bin TL verileri kullanılacaktır. Sonuç kaçtır?", "Dönen varlıklar 300 bin TL ve %25 artmışsa cari dönem tutarı kaç bin TL'dir?", n(25,"%"), n(1500," bin TL"), [n(20,"%"),n(30,"%"),n(80,"%"),n(125,"%")], [n(300," bin TL"),n(1200," bin TL"),n(1800," bin TL"),n(7500," bin TL")]),
    ("Kısa vadeli borçlar", 800, 920, "Kısa vadeli yabancı kaynaklar 800 bin TL iken sonraki dönemde 920 bin TL olmuştur. Yüzde değişim kaçtır?", "Kısa vadeli borçlardaki %15 artış 120 bin TL ise cari dönem borcu kaç bin TL'dir?", n(15,"%"), n(920," bin TL"), [n(13.04,"%"),n(20,"%"),n(85,"%"),n(115,"%")], [n(120," bin TL"),n(800," bin TL"),n(938," bin TL"),n(1707," bin TL")]),
    ("Net işletme sermayesi", 400, 580, "Net işletme sermayesi 400 bin TL'den 580 bin TL'ye çıkmıştır. Mutlak artış kaç bin TL'dir?", "Net işletme sermayesindeki 180 bin TL artış %45 ise önceki dönem tutarı kaç bin TL'dir?", n(180," bin TL"), n(400," bin TL"), [n(45," bin TL"),n(145," bin TL"),n(400," bin TL"),n(980," bin TL")], [n(180," bin TL"),n(261," bin TL"),n(580," bin TL"),n(800," bin TL")]),
    ("Maddi duran varlıklar", 1600, 1840, "Maddi duran varlıklar önceki döneme göre 240 bin TL artmış ve 1.840 bin TL olmuştur. Artış yüzdesi kaçtır?", "Maddi duran varlıkların önceki tutarı 1.600 bin TL ve artış oranı %15 ise artış tutarı kaç bin TL'dir?", n(15,"%"), n(240," bin TL"), [n(13.04,"%"),n(24,"%"),n(85,"%"),n(115,"%")], [n(15," bin TL"),n(160," bin TL"),n(276," bin TL"),n(1840," bin TL")]),
    ("Toplam yabancı kaynaklar", 1400, 1750, "Toplam borçlar 1.400 bin TL'den 1.750 bin TL'ye yükselmiştir. Hem tutar hem yüzde değişim nedir?", "Toplam borç %25 artarak 1.750 bin TL olduysa önceki borç ve artış tutarı nedir?", "350 bin TL ve %25", "1.400 bin TL ve 350 bin TL", ["250 bin TL ve %20","350 bin TL ve %20","1.400 bin TL ve %25","1.750 bin TL ve %125"], ["350 bin TL ve 1.400 bin TL","1.400 bin TL ve 250 bin TL","1.500 bin TL ve 250 bin TL","1.750 bin TL ve 350 bin TL"]),
    ("Özkaynaklar", 1000, 1300, "Özkaynaklardaki 300 bin TL artışın önceki 1.000 bin TL'ye oranı kaçtır?", "Özkaynaklar %30 artmış ve önceki dönem 1.000 bin TL ise cari özkaynak kaç bin TL'dir?", n(30,"%"), n(1300," bin TL"), [n(23.08,"%"),n(70,"%"),n(100,"%"),n(130,"%")], [n(300," bin TL"),n(1030," bin TL"),n(1330," bin TL"),n(3000," bin TL")]),
    ("Nakit", 500, 425, "Nakit ve nakit benzerleri 500 bin TL'den 425 bin TL'ye düşmüştür. Yatay analizde yüzde değişim kaçtır?", "Nakit mevcudu %15 azalarak 425 bin TL olduysa azalış tutarı kaç bin TL'dir?", n(-15,"%"), n(75," bin TL"), [n(-20,"%"),n(-12.5,"%"),n(17.65,"%"),n(85,"%")], [n(15," bin TL"),n(64," bin TL"),n(425," bin TL"),n(500," bin TL")]),
    ("Finansman giderleri", 200, 310, "Finansman giderleri 200 bin TL iken 310 bin TL olmuştur. Artış oranı kaçtır?", "Finansman giderlerindeki artış oranı %55 ve cari tutar 310 bin TL ise önceki tutar kaç bin TL'dir?", n(55,"%"), n(200," bin TL"), [n(35.48,"%"),n(64.52,"%"),n(110,"%"),n(155,"%")], [n(110," bin TL"),n(171," bin TL"),n(255," bin TL"),n(481," bin TL")]),
    ("Vergi gideri", 180, 216, "Vergi giderinin 180 bin TL'den 216 bin TL'ye değişmesi yüzde kaç artıştır?", "Vergi gideri %20 artmış ve artış 36 bin TL ise cari dönem vergi gideri kaç bin TL'dir?", n(20,"%"), n(216," bin TL"), [n(16.67,"%"),n(36,"%"),n(80,"%"),n(120,"%")], [n(36," bin TL"),n(180," bin TL"),n(200," bin TL"),n(252," bin TL")]),
]

for name, previous, current, scenario, focus, correct, focus_correct, distractors, focus_distractors in CALCS:
    RULES.append(r(
        scenario, focus, correct, focus_correct, distractors, focus_distractors,
        f"{name} için yatay analiz sonucu cari ve önceki dönem verilerinin farkı ile önceki dönem bazına göre hesaplanır.",
        f"{name} için bilinmeyen tutar, değişim tutarı ve yüzde değişim ilişkisi tersine kurularak bulunur.",
        f"Finansal tablo analizi - karşılaştırmalı analiz: {name}",
    ))


PREMISES = [
    {"stem":"Karşılaştırmalı analiz bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Aynı kalemin dönemler arası değişimi incelenir\n\nII. Mutlak ve yüzde değişim birlikte kullanılabilir\n\nIII. Önceki dönem kural olarak yüzde hesabının bazıdır","correct":"I, II ve III","why":"Üç ifade de yatay analizin dönemler arası değişim yaklaşımını doğru açıklar.","ref":"Finansal tablo analizi - karşılaştırmalı analiz","difficulty":"easy"},
    {"stem":"Yüzde değişim hesabı bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Cari tutardan önceki tutar çıkarılır\n\nII. Fark önceki dönem tutarına bölünür\n\nIII. Sonuç yüzle çarpılır","correct":"I, II ve III","why":"Yüzde değişim, cari-önceki farkının önceki dönem tutarına bölünüp yüzle çarpılmasıdır.","ref":"Finansal tablo analizi - yüzde değişim","difficulty":"easy"},
    {"stem":"Karşılaştırılabilirlik bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Muhasebe politikası farkları dikkate alınır\n\nII. Sınıflama değişiklikleri açıklanır\n\nIII. Birleşme etkisi her zaman organik büyüme sayılır","correct":"I ve II","why":"Politika ve sınıflama farkları düzeltilir veya açıklanır. Birleşme etkisi organik büyüme değildir; III yanlıştır.","ref":"TMS 1 karşılaştırmalı bilgi","difficulty":"medium"},
    {"stem":"Yatay analiz yorumu bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yalnız en yüksek yüzdeye bakmak yeterlidir\n\nII. Mutlak tutar değişimi önemlidir\n\nIII. İlişkili kalemler birlikte incelenmelidir","correct":"II ve III","why":"Yüzde tek başına yeterli değildir; mutlak büyüklük ve ilişkili kalemler birlikte değerlendirilir.","ref":"Finansal tablo analizi - yorum","difficulty":"medium"},
    {"stem":"Sorunlu bazlar bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Önceki tutar sıfırsa standart yüzde hesaplanamaz\n\nII. Sıfır bazda yüzde değişim zorunlu olarak %100'dür\n\nIII. Negatiften pozitife dönüş ayrıca açıklanmalıdır","correct":"I ve III","why":"Sıfır payda yüzde hesabını olanaksız kılar; işaret dönüşümü ayrıca yorumlanır. II yanlıştır.","ref":"Finansal tablo analizi - baz sorunları","difficulty":"hard"},
    {"stem":"Enflasyon etkisi bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Enflasyon bütün kalemlerde aynı reel sonucu garanti eder\n\nII. Nominal artış reel büyüme olmayabilir\n\nIII. Satın alma gücü farkı karşılaştırmayı etkiler","correct":"II ve III","why":"Fiyat düzeyi değişimi nominal ve reel büyümeyi ayrıştırmayı gerektirir. I yanlıştır.","ref":"Finansal tablo analizi - fiyat düzeyi","difficulty":"medium"},
    {"stem":"Analiz teknikleri bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yatay analiz dönem değişimini inceler\n\nII. Dikey analiz bütün dönemleri bir baz yıla göre endeksler\n\nIII. Trend analizi baz yıl endeksi kullanır","correct":"I ve III","why":"Yatay analiz dönem değişimini, trend analizi baz yıl eğilimini ölçer. Dikey analiz ise aynı dönemde toplam içindeki payı gösterdiğinden II yanlıştır.","ref":"Finansal tablo analizi - teknikler","difficulty":"easy"},
    {"stem":"Satış ve maliyet değişimi bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Maliyet satıştan hızlı artarsa brüt marj baskılanabilir\n\nII. Satış artışı tek başına kârlılık artışını garanti etmez\n\nIII. Satış ve maliyet birbiriyle ilişkisiz yorumlanmalıdır","correct":"I ve II","why":"Satış ve maliyetin göreli değişimi brüt kârlılığı belirler; birlikte incelenmeleri gerekir. III yanlıştır.","ref":"Finansal tablo analizi - ilişkili kalemler","difficulty":"medium"},
]


if __name__ == "__main__":
    write_topic(
        lesson_id="mali_tablolar_analizi", topic_id="karsilastirmali_analiz",
        label="Karşılaştırmalı Analiz", slug="karsilastirmali_analiz",
        prefix="topic-kya", seed=2026071743,
        legislation_version="SMMM Finansal Tablolar ve Analizi müfredatı; karşılaştırmalı tablolar analizi (17.07.2026 kontrolü)",
        rules=RULES, premises=PREMISES, wrong_banks={},
    )
