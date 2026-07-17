# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / TMS 10 Raporlama Döneminden Sonraki Olaylar — 60 soru.
Kaynak: KGK TMS 10.

★ Gerçek sınav kalibrasyonu (5 dosyada 7 geçiş — en çok sorulan üçüncü standart):
  · 2016-18 — "raporlama tarihinden sonraki olaylar, hangi TARİH ARALIĞINDA ortaya çıkan
               olayları ifade eder?"
  · 2020    — "yılsonundan (31.12.2019) itibaren HANGİ TARİHE KADAR gerçekleşen olaylar ...
               kabul edilmektedir?"
  · 2021    — "aşağıdakilerden hangisi doğrudur?"
  · 2023 ×2 — "04.02.2023 tarihinde yapılması gereken DÜZELTME İŞLEMİ hangisidir?" /
               "4 Şubat 2023 İTİBARIYLA aşağıdakilerden hangisi doğrudur?"
  → İki yük merkezi: (1) TARİH ARALIĞI tanımı, (2) TARİHLİ SENARYO.

★ 2023 arketipi — şıklar 2×2 ÇAPRAZ kurulu:
     "Düzeltme gerektiren bir olaydır ve karşılık düzeltilir"
     "Düzeltme gerektirmeyen bir olaydır, ancak ... karşılık düzeltilir"
     "Düzeltme gerektirmeyen bir olaydır ve karşılık düzeltilmez"
     "Düzeltme gerektiren bir olaydır, ancak ... karşılık düzeltilmez"
  Öğrenci iki ekseni de bilmeden bulamaz. Bu yapı taklit edildi (senaryolar özgün).
  Yan fayda: çapraz şıklar doğal olarak denk boyda → length-tell riski düşük.

KURAL: doğru şık KISA (≤~110), çeldiriciler UZUN (~90-115).
⚠ Çapraz-matris ve negatif köklerde bu ters teper → oralarda şıklar denk boyda yazıldı.
⚠ Tarihler senaryoya özgü ve kökte veriliyor → yıla bağlı değil.
"""
import collections, json, random, re

DERS, KONU = "muhasebe_standartlari", "tms_10_sonraki_olaylar"
PREFIX, SEED = "std-tms10-gen", 20260804
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/tms_10_sonraki_olaylar.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

# ── A. Tanım ve tarih aralığı — sınavın 1. yük merkezi (14) ────────────────
q("TMS 10'a göre raporlama döneminden sonraki olaylar hangi tarih aralığında ortaya çıkan olaylardır?",
  "Raporlama dönemi sonu ile finansal tabloların yayımı için onaylandığı tarih arasında",
  ["Raporlama dönemi sonu ile izleyen dönemin ilk geçici vergi beyannamesi arasında kalan sürede",
   "Raporlama dönemi sonu ile bağımsız denetim sözleşmesinin imzalandığı tarih arasında kalan sürede",
   "Raporlama dönemi sonu ile finansal tabloların vergi dairesine verildiği tarih arasında geçen sürede",
   "Raporlama dönemi sonu ile izleyen hesap döneminin sona erdiği tarih arasında kalan tüm süre boyunca"],
  "TMS 10: raporlama döneminden sonraki olaylar, raporlama dönemi sonu ile finansal tabloların yayımı için onaylandığı tarih arasında ortaya çıkan lehte veya aleyhteki olaylardır. Ölçüt beyanname, denetim sözleşmesi veya izleyen dönem sonu değil, YAYIM İÇİN ONAY tarihidir.",
  "TMS 10 - tanım (tarih aralığı)")

q("Hesap dönemi 31 Aralık 2025'te biten bir işletmenin finansal tabloları, yönetim kurulunca 10 Mart 2026'da yayımlanmak üzere onaylanmış ve 25 Mart 2026'da genel kurulda kabul edilmiştir. TMS 10'a göre sonraki olaylar dönemi hangi tarihte sona erer?",
  "10 Mart 2026",
  ["25 Mart 2026", "31 Aralık 2025", "31 Aralık 2026", "1 Ocak 2026"],
  "TMS 10: sonraki olaylar dönemi, finansal tabloların YAYIM İÇİN ONAYLANDIĞI tarihte sona erer — burada yönetim kurulunun onay tarihi olan 10 Mart 2026. Genel kurulun tabloları sonradan kabul etmesi (25 Mart) bu tarihi ötelemez; tablolar zaten yayım için onaylanmıştır.",
  "TMS 10 - onay tarihi (senaryo)")

q("TMS 10'a göre raporlama döneminden sonraki olaylar bakımından aşağıdakilerden hangisi doğrudur?",
  "Hem lehte hem aleyhte olayları kapsar",
  ["Yalnızca işletmenin aleyhine olan ve zarar doğuran olayları kapsamak durumunda bulunmaktadır",
   "Yalnızca işletmenin lehine olan ve kazanç doğuran olayları kapsayan bir düzenleme niteliğindedir",
   "Yalnızca nakit hareketi doğuran olayları kapsayan dar kapsamlı bir düzenleme durumundadır",
   "Yalnızca tutarı önceden kesin olarak bilinen olayları kapsamak zorunda olan bir düzenlemedir"],
  "TMS 10: raporlama döneminden sonraki olaylar, ilgili dönemde ortaya çıkan LEHTE VEYA ALEYHTEKİ tüm olaylardır. Lehte olaylar da kapsamdadır.",
  "TMS 10 - kapsam")

q("TMS 10'a göre düzeltme gerektiren olay bakımından aşağıdakilerden hangisi doğrudur?",
  "Raporlama dönemi sonu itibarıyla var olan durumlara ilişkin kanıt sağlayan olaylardır",
  ["Raporlama döneminden sonra ortaya çıkan yeni koşullara ilişkin olayları ifade etmek durumundadır",
   "Yalnızca tutarı önemlilik düzeyini aşan ve nakit çıkışı gerektiren olayları ifade etmektedir",
   "Yalnızca işletmenin aleyhine sonuç doğuran ve zarar yazılmasını gerektiren olayları karşılar",
   "Düzeltme gerektiren olay kavramı TMS 10'da tanımlanmamış bir husus niteliğinde bulunmaktadır"],
  "TMS 10: düzeltme gerektiren olaylar, raporlama dönemi sonu İTİBARIYLA VAR OLAN durumlara ilişkin kanıt sağlayan olaylardır. Ölçüt olayın ne zaman öğrenildiği değil, ilgili durumun dönem sonunda var olup olmadığıdır.",
  "TMS 10 - düzeltme gerektiren olay")

q("TMS 10'a göre düzeltme gerektirmeyen olay bakımından aşağıdakilerden hangisi doğrudur?",
  "Raporlama döneminden sonra ortaya çıkan koşullara ilişkin olaylardır",
  ["Raporlama dönemi sonu itibarıyla var olan durumlara kanıt sağlayan olayları ifade etmektedir",
   "Yalnızca tutarı önemlilik düzeyinin altında kalan ve önemsiz sayılan olayları karşılamaktadır",
   "Yalnızca işletmenin lehine sonuç doğuran ve gelir yazılmasını gerektiren olayları ifade eder",
   "Düzeltme gerektirmeyen olay kavramı TMS 10'da tanımlanmamış bir husus niteliğinde bulunur"],
  "TMS 10: düzeltme gerektirmeyen olaylar, raporlama döneminden SONRA ortaya çıkan koşullara ilişkin olaylardır. Tutarları düzeltilmez; ancak önemliyse dipnotlarda açıklanır.",
  "TMS 10 - düzeltme gerektirmeyen olay")

q("Düzeltme gerektiren bir olayın ortaya çıkması hâlinde işletme ne yapar?",
  "Finansal tablolardaki tutarları bu olayı yansıtacak biçimde düzeltir",
  ["Tutarları düzeltmez; olayı yalnızca dipnotlarda açıklamak zorunda olan bir işlemi ifade eder",
   "Tutarları düzeltmez; olayı izleyen dönemin finansal tablolarında göstermek zorunda kalınır",
   "Finansal tabloları tümüyle yeniden düzenler ve önceki dönemleri de yeniden ifade etmek zorundadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: işletme, düzeltme gerektiren olayların ortaya çıkması durumunda finansal tablolara alınan tutarları bu yeni duruma uygun biçimde DÜZELTİR. Yeni bir kalemin muhasebeleştirilmesi de gerekebilir.",
  "TMS 10 - düzeltmenin sonucu")

q("Düzeltme gerektirmeyen ancak önemli olan bir olay bakımından aşağıdakilerden hangisi doğrudur?",
  "Tutarlar düzeltilmez; olayın niteliği ve finansal etkisinin tahmini açıklanır",
  ["Tutarlar düzeltilir ve ayrıca olayın niteliği dipnotlarda açıklanmak zorunda tutulmaktadır",
   "Tutarlar düzeltilmez ve olay hakkında hiçbir açıklama yapılmasına gerek bulunmamaktadır",
   "Finansal tablolar tümüyle yeniden düzenlenmek ve yeniden yayımlanmak zorunda kalınmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: düzeltme gerektirmeyen olaylar için tutarlar düzeltilmez. Ancak önemli olması hâlinde açıklanmaması kullanıcıların kararlarını etkileyebileceğinden, işletme olayın NİTELİĞİNİ ve finansal etkisinin TAHMİNİNİ (tahmin yapılamıyorsa buna ilişkin açıklamayı) dipnotlarda verir.",
  "TMS 10 - açıklama yükümlülüğü")

q("TMS 10'a göre finansal tabloların yayımı için onaylandığı tarih bakımından aşağıdakilerden hangisi doğrudur?",
  "Bu tarih ve onayı verenler açıklanır; ortaklar tabloları sonradan değiştirebiliyorsa bu da açıklanır",
  ["Onay tarihinin açıklanmasına gerek bulunmamakta olup yalnızca dönem sonu tarihi verilmektedir",
   "Yalnızca onay tarihi açıklanır; onayı veren organın belirtilmesine gerek bulunmamak durumundadır",
   "Onay tarihi yalnızca bağımsız denetime tabi işletmelerce açıklanmak zorunda tutulmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: işletme, finansal tabloların yayımı için onaylandığı tarihi ve bu onayı kimin verdiğini açıklar. İşletmenin ortaklarının veya diğer kişilerin finansal tabloları yayımlandıktan sonra değiştirme yetkisi varsa, işletme bu durumu da açıklar.",
  "TMS 10 - onay tarihinin açıklanması")

q("Aşağıdaki ifadelerden hangileri TMS 10 bakımından doğrudur?\n\nI. Sonraki olaylar dönemi, raporlama dönemi sonunda başlar\n\nII. Sonraki olaylar dönemi, tabloların yayımı için onaylandığı tarihte sona erer\n\nIII. Sonraki olaylar yalnızca aleyhteki olayları kapsar",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "I ve III"],
  "Sonraki olaylar dönemi raporlama dönemi sonunda başlar (I) ve tabloların yayımı için onaylandığı tarihte sona erer (II). Sonraki olaylar LEHTE VE ALEYHTE tüm olayları kapsar; bu nedenle III yanlıştır.",
  "TMS 10 - tarih aralığı")

q("Finansal tabloların onaylanma süreci bakımından aşağıdakilerden hangisi doğrudur?",
  "Onay birden fazla aşamalıysa esas alınan tarih, tabloların ilk kez yayıma onaylandığı tarihtir",
  ["Onay birden fazla aşamalıysa her hâlde en son onay tarihi esas alınmak zorunda tutulmaktadır",
   "Onay birden fazla aşamalıysa her hâlde vergi beyannamesi tarihi esas alınmak zorunda kalınır",
   "Onay birden fazla aşamalıysa işletme dilediği aşamanın tarihini serbestçe seçmek durumundadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: finansal tabloların yayımı için onaylandığı tarih, tabloların ilgili organca yayıma onaylandığı tarihtir. Tabloların önce yönetimce hazırlanıp bir denetim/gözetim kuruluna ya da ortaklara sunulduğu hâllerde de esas alınan tarih, YAYIM İÇİN ONAYIN VERİLDİĞİ tarihtir; sonraki kabul işlemleri bu tarihi ötelemez.",
  "TMS 10 - onay süreci")

q("Bir işletmenin yönetimi, 31 Aralık 2025 tarihli finansal tabloları 5 Şubat 2026'da yayım için onaylamıştır. 20 Şubat 2026'da önemli bir olay gerçekleşmiştir. TMS 10 bakımından aşağıdakilerden hangisi doğrudur?",
  "Olay sonraki olaylar döneminin dışında kaldığından 2025 tablolarını etkilemez",
  ["Olay düzeltme gerektiren olay sayılır ve 2025 tablolarındaki tutarlar düzeltilmek zorundadır",
   "Olay düzeltme gerektirmeyen olay sayılır ve 2025 tablolarının dipnotlarında açıklanmak zorundadır",
   "Olay nedeniyle 2025 finansal tabloları tümüyle yeniden düzenlenmek zorunda tutulmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: sonraki olaylar dönemi, tabloların yayım için onaylandığı 5 Şubat 2026'da SONA ERMİŞTİR. 20 Şubat'taki olay bu pencerenin dışındadır; ne düzeltme gerektiren ne de düzeltme gerektirmeyen sonraki olaydır — 2025 tablolarını hiç etkilemez, izleyen dönemin olayıdır.",
  "TMS 10 - pencere dışı olay (senaryo)")

q("Aşağıdakilerden hangisi TMS 10'a göre raporlama döneminden sonraki olay DEĞİLDİR?",
  "Finansal tabloların yayımı için onaylanmasından sonra gerçekleşen olay",
  ["Raporlama dönemi sonu itibarıyla var olan bir duruma kanıt sağlayan ve sonradan öğrenilen olay",
   "Raporlama döneminden sonra ortaya çıkan koşullara ilişkin bulunan ve işletme lehine olan olay",
   "Raporlama döneminden sonra ortaya çıkan koşullara ilişkin bulunan ve işletme aleyhine olan olay",
   "Raporlama dönemi sonu ile yayım onayı arasında gerçekleşen ve tutarı önemli olmayan olay"],
  "TMS 10: sonraki olaylar penceresi raporlama dönemi sonunda başlar ve YAYIM İÇİN ONAY tarihinde biter. Onaydan sonraki olaylar bu pencerenin dışındadır; diğer şıkların hepsi pencere içindedir (lehte/aleyhte, önemli/önemsiz ayrımı pencereyi değiştirmez).",
  "TMS 10 - pencere dışı")

q("TMS 10 ile TMS 8 arasındaki ilişki bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönem sonu itibarıyla var olan bir hatanın sonradan ortaya çıkması düzeltme gerektiren olaydır",
  ["Hataların sonradan ortaya çıkması her hâlde düzeltme gerektirmeyen olay sayılmak zorundadır",
   "Hataların sonradan ortaya çıkması hâlinde finansal tablolara hiç müdahale edilmemek durumundadır",
   "Hatalar yalnızca izleyen dönemin finansal tablolarında düzeltilmek zorunda tutulmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: düzeltme gerektiren olay örnekleri arasında, finansal tabloların yanlış olduğunu gösteren hile veya hataların ortaya çıkarılması sayılır. Hata dönem sonunda ZATEN VARDIR; sonradan öğrenilmesi onu sonraki döneme ait yapmaz. Tablolar henüz yayıma onaylanmadığından doğrudan düzeltilir.",
  "TMS 10 - hilenin/hatanın ortaya çıkması")

q("Aşağıdaki ifadelerden hangileri düzeltme gerektiren ↔ gerektirmeyen ayrımı bakımından doğrudur?\n\nI. Ölçüt, olayın işletmece ne zaman öğrenildiğidir\n\nII. Ölçüt, ilgili durumun raporlama dönemi sonunda var olup olmadığıdır\n\nIII. Düzeltme gerektirmeyen olaylar önemliyse açıklanır",
  "II ve III",
  ["I, II ve III", "Yalnız II", "I ve II", "I ve III"],
  "Ayrımın ölçütü, ilgili durumun raporlama dönemi sonunda VAR OLUP OLMADIĞIDIR (II); düzeltme gerektirmeyen olaylar önemliyse açıklanır (III). Olayın ne zaman ÖĞRENİLDİĞİ ölçüt değildir (I) — dönem sonunda var olan bir durum sonradan öğrenilse de düzeltme gerektirir.",
  "TMS 10 - ayrımın ölçütü")

# ── B. Düzeltme GEREKTİREN olaylar (15) ────────────────────────────────────
q("Raporlama döneminden sonra sonuçlanan ve dönem sonunda işletmenin mevcut bir yükümlülüğü bulunduğunu teyit eden dava bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektiren olaydır; karşılık muhasebeleştirilir veya mevcut karşılık düzeltilir",
  ["Düzeltme gerektirmeyen olaydır; yalnızca dipnotlarda açıklanmak zorunda olan bir durumu ifade eder",
   "Düzeltme gerektirmeyen olaydır; hiçbir açıklama dahi yapılmamak zorunda olan bir durumdur",
   "Düzeltme gerektiren olaydır; ancak karşılık yerine koşullu varlık muhasebeleştirilmek zorundadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: raporlama döneminden sonra bir mahkeme davasının sonuçlanması, dönem sonunda işletmenin mevcut bir yükümlülüğünün bulunduğunu teyit ediyorsa DÜZELTME GEREKTİREN olaydır. İşletme TMS 37 uyarınca daha önce ayırdığı karşılığı düzeltir veya karşılık ayırır — koşullu borç açıklamasıyla yetinmez.",
  "TMS 10 - dava sonucu")

q("Raporlama döneminden sonra bir müşterinin iflas etmesi ve bunun dönem sonunda alacağın değer düşüklüğüne uğradığını göstermesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektiren olaydır; alacağın defter değeri düzeltilir",
  ["Düzeltme gerektirmeyen olaydır; yalnızca dipnotlarda açıklanmak zorunda olan bir durumu ifade eder",
   "Düzeltme gerektirmeyen olaydır; iflas dönem sonundan sonra gerçekleştiğinden düzeltme yapılmaz",
   "Düzeltme gerektiren olaydır; ancak düzeltme izleyen dönemde yapılmak zorunda tutulmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: raporlama döneminden sonra bir müşterinin iflas etmesi genellikle, dönem sonunda ilgili ticari alacağın değer düşüklüğüne uğramış olduğunu teyit eder — müşterinin mali durumu dönem sonunda ZATEN bozuktur. Düzeltme gerektiren olaydır; alacağın defter değeri düzeltilir.",
  "TMS 10 - müşterinin iflası")

q("Raporlama döneminden sonra stokların satış fiyatının, dönem sonundaki net gerçekleşebilir değere ilişkin kanıt sağlaması bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektiren olaydır; stokun değeri net gerçekleşebilir değere indirilir",
  ["Düzeltme gerektirmeyen olaydır; satış dönem sonundan sonra yapıldığından düzeltme yapılmamaktadır",
   "Düzeltme gerektirmeyen olaydır; yalnızca dipnotlarda açıklanmak zorunda olan bir durumu ifade eder",
   "Düzeltme gerektiren olaydır; ancak stok yerine satış hasılatı düzeltilmek zorunda tutulmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: raporlama döneminden sonra stokların satışı, dönem sonundaki net gerçekleşebilir değerlerine ilişkin kanıt sağlayabilir. Stokun düşük değerli oluşu dönem sonunda zaten mevcuttur; düzeltme gerektiren olaydır ve TMS 2 uyarınca değer düşüklüğü muhasebeleştirilir.",
  "TMS 10 - stokun NGD kanıtı")

q("Raporlama döneminden önce satın alınan varlıkların maliyetinin dönem sonundan sonra belirlenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektiren olaydır; maliyet belirlenen tutara göre düzeltilir",
  ["Düzeltme gerektirmeyen olaydır; tutar dönem sonundan sonra belirlendiğinden düzeltme yapılmaz",
   "Düzeltme gerektirmeyen olaydır; yalnızca dipnotlarda açıklanmak zorunda olan bir durumu ifade eder",
   "Düzeltme gerektiren olaydır; ancak düzeltme izleyen dönemde yapılmak zorunda tutulmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: raporlama döneminden önce satın alınan varlıkların maliyetinin veya satılan varlıkların hasılatının dönem sonundan sonra belirlenmesi, düzeltme gerektiren olay örneğidir. Alım işlemi dönem sonundan ÖNCE gerçekleşmiştir; sonradan belirlenen yalnızca tutardır.",
  "TMS 10 - maliyetin sonradan belirlenmesi")

q("Dönem sonunda çalışanlara prim ödeme yönünde mevcut bir hukuki veya zımni yükümlülüğü bulunan işletmede, prim tutarının dönem sonundan sonra kesinleşmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektiren olaydır; kesinleşen tutara göre borç muhasebeleştirilir",
  ["Düzeltme gerektirmeyen olaydır; tutar dönem sonundan sonra kesinleştiğinden düzeltme yapılmaz",
   "Düzeltme gerektirmeyen olaydır; yalnızca dipnotlarda açıklanmak zorunda olan bir durumu ifade eder",
   "Düzeltme gerektiren olaydır; ancak borç yerine koşullu borç açıklanmak zorunda tutulmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: dönem sonundan önceki olaylar nedeniyle işletmenin kâr paylaşımı veya prim ödemek üzere dönem sonunda mevcut bir hukuki ya da zımni yükümlülüğü varsa, tutarın dönem sonundan sonra kesinleşmesi düzeltme gerektiren olaydır (TMS 19). Yükümlülük dönem sonunda VARDIR.",
  "TMS 10 - prim yükümlülüğü")

q("Bir işletme, 31 Aralık 2025 itibarıyla süren bir tazminat davası için 200.000 ₺ karşılık ayırmıştır. Mahkeme 12 Şubat 2026'da 260.000 ₺ tazminata hükmetmiş, tablolar 5 Mart 2026'da onaylanmıştır. TMS 10'a göre aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektiren bir olaydır ve karşılık 260.000 ₺'ye yükseltilir",
  ["Düzeltme gerektirmeyen bir olaydır ve ayrılan karşılık tutarı düzeltilmeyecek durumda kalmaktadır",
   "Düzeltme gerektirmeyen bir olaydır, ancak karar verildiği için karşılık tutarı düzeltilmek zorundadır",
   "Düzeltme gerektiren bir olaydır, ancak karar sonraki dönemde verildiğinden karşılık düzeltilmez",
   "Düzeltme gerektiren bir olaydır ve karşılık iptal edilerek yerine koşullu borç açıklanmak zorundadır"],
  "TMS 10: mahkeme kararı, dönem sonunda mevcut olan yükümlülüğü TEYİT ETMEKTEDİR — dava 31 Aralık'ta zaten sürmektedir. Düzeltme gerektiren olaydır; karar 5 Mart onayından önce (12 Şubat) verildiğinden pencere içindedir ve karşılık 260.000 ₺'ye düzeltilir.",
  "TMS 10 - dava senaryosu (2×2 çapraz)")

q("Bir işletmenin 31 Aralık 2025 tarihli bilançosunda bir müşteriden 150.000 ₺ alacağı vardır. Müşteri 20 Ocak 2026'da iflas etmiş, iflasın nedeni olan mali sıkıntının dönem sonunda da mevcut olduğu belirlenmiştir. Tablolar 1 Mart 2026'da onaylanmıştır. TMS 10'a göre aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektiren bir olaydır ve alacak için değer düşüklüğü muhasebeleştirilir",
  ["Düzeltme gerektirmeyen bir olaydır ve alacağın defter değeri düzeltilmeyecek durumda kalmaktadır",
   "Düzeltme gerektirmeyen bir olaydır, ancak iflas gerçekleştiğinden alacak tümüyle silinmek zorundadır",
   "Düzeltme gerektiren bir olaydır, ancak iflas sonraki dönemde olduğundan alacak düzeltilmez",
   "Düzeltme gerektiren bir olaydır ve alacak yerine koşullu varlık muhasebeleştirilmek zorundadır"],
  "TMS 10: müşterinin iflasına yol açan mali sıkıntı dönem sonunda ZATEN VARDIR; iflas bunu teyit eden kanıttır. Düzeltme gerektiren olaydır ve 1 Mart onayından önce gerçekleştiğinden pencere içindedir — alacağın değer düşüklüğü 2025 tablolarına yansıtılır.",
  "TMS 10 - alacak senaryosu (2×2 çapraz)")

q("Aşağıdakilerden hangisi TMS 10'a göre düzeltme gerektiren olaydır?",
  "Finansal tabloların yanlış olduğunu gösteren bir hilenin ortaya çıkarılması",
  ["Raporlama döneminden sonra işletmenin önemli bir işletme birleşmesi gerçekleştirmiş olması durumu",
   "Raporlama döneminden sonra çıkan yangın sonucu işletme binasının tümüyle yanmış olması durumu",
   "Raporlama döneminden sonra işletmenin önemli tutarda sermaye artırımına gitmiş olması durumu",
   "Raporlama döneminden sonra kur değişimlerinde olağandışı bir dalgalanmanın yaşanmış olması"],
  "TMS 10: finansal tabloların yanlış olduğunu gösteren hile veya hataların ortaya çıkarılması düzeltme gerektiren olaydır — hata dönem sonunda zaten vardır. Diğer şıkların hepsi dönem sonundan SONRAKİ koşullara ilişkindir; düzeltme gerektirmeyen olaylardır.",
  "TMS 10 - düzeltme gerektiren örnek")

q("Aşağıdakilerden hangileri TMS 10'a göre düzeltme gerektiren olaydır?\n\nI. Dönem sonunda süren davanın sonraki dönemde sonuçlanması\n\nII. Dönem sonundan sonra müşterinin iflasının, alacağın dönem sonunda değersizleştiğini göstermesi\n\nIII. Dönem sonundan sonra işletmenin yeni bir bağlı ortaklık satın alması",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "I ve III"],
  "Dönem sonunda süren davanın sonuçlanması (I) ve müşterinin iflasının dönem sonundaki değer düşüklüğünü teyit etmesi (II) düzeltme gerektiren olaylardır — ikisinde de ilgili durum dönem sonunda vardır. Bağlı ortaklık satın alınması (III) dönem sonundan sonraki yeni bir koşuldur; düzeltme gerektirmez, açıklanır.",
  "TMS 10 - düzeltme gerektiren olaylar")

q("Raporlama döneminden sonra satılan bir varlığın hasılatının, dönem sonundaki değer düşüklüğüne kanıt sağlaması bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektiren olaydır; varlığın dönem sonu değeri düzeltilir",
  ["Düzeltme gerektirmeyen olaydır; satış dönem sonundan sonra yapıldığından düzeltme yapılmamaktadır",
   "Düzeltme gerektirmeyen olaydır; yalnızca dipnotlarda açıklanmak zorunda olan bir durumu ifade eder",
   "Düzeltme gerektiren olaydır; ancak yalnızca satış kârı düzeltilmek zorunda tutulan bir durumdur",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: dönem sonundan sonraki satış, varlığın dönem sonundaki değerine ilişkin kanıt sağlıyorsa düzeltme gerektiren olaydır — değer düşüklüğü dönem sonunda zaten mevcuttur; satış yalnızca bunu görünür kılmıştır.",
  "TMS 10 - satışın değer kanıtı")

q("Dönem sonu itibarıyla var olan bir duruma ilişkin dipnot açıklamalarının, sonraki olaylar döneminde yeni bilgi alınması hâlinde durumu bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme, yeni bilgiyi yansıtacak biçimde ilgili açıklamaları günceller",
  ["Açıklamalar hiçbir hâlde güncellenmez; ilk hâliyle bırakılmak zorunda olan bir durumu ifade eder",
   "Açıklamalar yalnızca izleyen dönemin tablolarında güncellenmek zorunda tutulan bir durumdur",
   "Yeni bilgi alınması hâlinde finansal tablolar tümüyle yeniden düzenlenmek zorunda kalınmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: raporlama dönemi sonunda var olan bir duruma ilişkin olarak sonraki olaylar döneminde bilgi alınması hâlinde işletme, bu yeni bilgi ışığında söz konusu duruma ilişkin açıklamalarını GÜNCELLER. Bu, tutar düzeltmesi gerekmese bile geçerlidir.",
  "TMS 10 - açıklamaların güncellenmesi")

q("Aşağıdaki ifadelerden hangileri düzeltme gerektiren olaylar bakımından doğrudur?\n\nI. Dönem sonunda var olan bir hatanın sonradan bulunması düzeltme gerektirir\n\nII. Tutarları düzeltmek yerine yalnızca açıklama yapmak yeterlidir\n\nIII. Yeni bir kalemin finansal tablolara alınması da gerekebilir",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "II ve III"],
  "Dönem sonunda var olan hatanın sonradan bulunması düzeltme gerektirir (I) ve düzeltme kapsamında yeni bir kalemin tablolara alınması gerekebilir (III). Düzeltme gerektiren olaylarda tutarlar DÜZELTİLİR; açıklamayla yetinmek yeterli değildir — bu nedenle II yanlıştır.",
  "TMS 10 - düzeltmenin kapsamı")

q("Bir işletme, dönem sonunda devam eden bir vergi incelemesi için karşılık ayırmamıştır. İnceleme, tabloların onayından önce işletme aleyhine sonuçlanmış ve dönem sonu itibarıyla mevcut bir yükümlülük bulunduğu anlaşılmıştır. TMS 10'a göre aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektiren olaydır; daha önce ayrılmamış olsa da karşılık muhasebeleştirilir",
  ["Düzeltme gerektirmeyen olaydır; daha önce karşılık ayrılmadığından yeni kayıt yapılmamaktadır",
   "Düzeltme gerektirmeyen olaydır; yalnızca dipnotlarda koşullu borç açıklanmak zorunda kalınır",
   "Düzeltme gerektiren olaydır; ancak yalnızca mevcut karşılıklar düzeltilebilir, yenisi ayrılamaz",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: düzeltme gerektiren olay, mevcut tutarların düzeltilmesinin yanı sıra YENİ BİR KALEMİN finansal tablolara alınmasını da gerektirebilir. Yükümlülük dönem sonunda vardır; daha önce karşılık ayrılmamış olması karşılık ayrılmasına engel değildir.",
  "TMS 10 - yeni kalem (senaryo)")

q("Dönem sonundan sonra alınan ve dönem sonunda var olan bir varlığın değerinin düştüğünü gösteren bilgi bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektiren olaydır; değer düşüklüğü zararı dönem sonu tablolarına yansıtılır",
  ["Düzeltme gerektirmeyen olaydır; bilgi dönem sonundan sonra alındığından düzeltme yapılmamaktadır",
   "Düzeltme gerektirmeyen olaydır; yalnızca dipnotlarda açıklanmak zorunda olan bir durumu ifade eder",
   "Düzeltme gerektiren olaydır; ancak düzeltme izleyen dönemde yapılmak zorunda tutulan bir durumdur",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: dönem sonundan sonra alınan ve bir varlığın dönem sonunda değer düşüklüğüne uğradığını ya da daha önce muhasebeleştirilen değer düşüklüğü zararının düzeltilmesi gerektiğini gösteren bilgi, düzeltme gerektiren olaydır. Bilginin ALINMA zamanı değil, durumun VAR OLMA zamanı belirleyicidir.",
  "TMS 10 - değer düşüklüğü kanıtı")

q("Dönem sonundan sonra sonuçlanan bir davanın, dönem sonunda mevcut bir yükümlülük BULUNMADIĞINI göstermesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektiren olaydır; daha önce ayrılan karşılık iptal edilir",
  ["Düzeltme gerektirmeyen olaydır; lehte sonuç doğduğundan hiçbir düzeltme yapılmamak durumundadır",
   "Düzeltme gerektirmeyen olaydır; yalnızca dipnotlarda açıklanmak zorunda olan bir durumu ifade eder",
   "Düzeltme gerektiren olaydır; ancak karşılık iptal edilmeyip aynen korunmak zorunda tutulmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: sonraki olaylar LEHTE olanları da kapsar. Dava sonucu dönem sonunda mevcut bir yükümlülük bulunmadığını gösteriyorsa bu da dönem sonundaki duruma kanıttır; düzeltme gerektiren olaydır ve gereksiz kalan karşılık iptal edilir.",
  "TMS 10 - lehte düzeltme")

# ── C. Düzeltme GEREKTİRMEYEN olaylar (15) ─────────────────────────────────
q("Raporlama döneminden sonra yatırım amaçlı gayrimenkulün piyasa değerinde meydana gelen düşüş bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektirmeyen olaydır; önemliyse açıklanır",
  ["Düzeltme gerektiren olaydır; gayrimenkulün dönem sonu değeri düzeltilmek zorunda bulunmaktadır",
   "Düzeltme gerektiren olaydır; değer düşüklüğü zararı dönem sonu tablolarına yansıtılmak zorundadır",
   "Düzeltme gerektirmeyen olaydır; ancak önemli olsa dahi hiç açıklanmamak zorunda kalınmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: raporlama döneminden sonra yatırımların piyasa değerinde meydana gelen düşüş, düzeltme gerektirmeyen olay örneği olarak sayılır. Düşüş normalde dönem sonundaki koşullara değil, SONRAKİ koşullara ilişkindir; tutarlar düzeltilmez, önemliyse açıklanır.",
  "TMS 10 - piyasa değerindeki düşüş")

q("Raporlama döneminden sonra gerçekleşen önemli bir işletme birleşmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektirmeyen olaydır; önemliyse niteliği ve etkisi açıklanır",
  ["Düzeltme gerektiren olaydır; birleşmenin etkileri dönem sonu tablolarına yansıtılmak zorundadır",
   "Düzeltme gerektiren olaydır; birleşen işletmenin varlıkları dönem sonu tablosuna alınmak zorundadır",
   "Düzeltme gerektirmeyen olaydır; ancak önemli olsa dahi hiç açıklanmamak zorunda kalınmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: raporlama döneminden sonra gerçekleşen önemli bir işletme birleşmesi ya da önemli bir bağlı ortaklığın elden çıkarılması, düzeltme gerektirmeyen olay örneğidir; TFRS 3 uyarınca açıklama yapılır. Birleşme dönem sonunda YOKTUR.",
  "TMS 10 - işletme birleşmesi")

q("Raporlama döneminden sonra çıkan yangın sonucunda üretim tesisinin yok olması bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektirmeyen olaydır; önemliyse niteliği ve etkisi açıklanır",
  ["Düzeltme gerektiren olaydır; tesisin dönem sonu defter değeri sıfırlanmak zorunda bulunmaktadır",
   "Düzeltme gerektiren olaydır; değer düşüklüğü zararı dönem sonu tablolarına yansıtılmak zorundadır",
   "Düzeltme gerektirmeyen olaydır; ancak önemli olsa dahi hiç açıklanmamak zorunda kalınmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: raporlama döneminden sonra varlıkların yangın sonucu yok olması, düzeltme gerektirmeyen olay örneğidir. Tesis dönem sonunda SAĞLAM olduğundan dönem sonu tutarları düzeltilmez; olay önemliyse niteliği ve finansal etkisinin tahmini açıklanır.",
  "TMS 10 - yangın")

q("Raporlama döneminden sonra ilan edilen kâr payı (temettü) bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönem sonunda borç olarak muhasebeleştirilmez; düzeltme gerektirmeyen olaydır",
  ["Dönem sonunda borç olarak muhasebeleştirilir; düzeltme gerektiren olay sayılmak zorundadır",
   "Dönem sonunda özkaynaklardan indirilir; düzeltme gerektiren olay sayılmak zorunda kalınmaktadır",
   "Dönem sonunda gider olarak muhasebeleştirilir; düzeltme gerektiren olay sayılmak durumundadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: raporlama döneminden sonra işletmenin özkaynağa dayalı finansal araçlarını elinde bulunduranlara kâr payı ilan edilmesi durumunda, bu kâr payları dönem sonu itibarıyla BORÇ OLARAK MUHASEBELEŞTİRİLMEZ — dönem sonunda mevcut bir yükümlülük yoktur (TMS 32). Düzeltme gerektirmeyen olaydır; TMS 1 uyarınca açıklanır.",
  "TMS 10 - temettü (sınav klasiği)")

q("Bir işletmenin genel kurulu, 31 Aralık 2025 tarihli tablolar 10 Mart 2026'da onaylanmadan önce, 20 Şubat 2026'da 500.000 ₺ kâr payı dağıtımına karar vermiştir. TMS 10'a göre aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektirmeyen olaydır; 2025 bilançosunda borç olarak gösterilmez, açıklanır",
  ["Düzeltme gerektiren olaydır ve 500.000 ₺ 2025 bilançosunda borç olarak gösterilmek zorundadır",
   "Düzeltme gerektirmeyen olaydır, ancak karar onaydan önce alındığından borç olarak gösterilmelidir",
   "Düzeltme gerektiren olaydır, ancak tutar dönem sonundan sonra ilan edildiğinden borç gösterilmez",
   "Düzeltme gerektiren olaydır ve 500.000 ₺ 2025 gelir tablosunda gider olarak gösterilmek zorundadır"],
  "TMS 10: kâr payı dönem sonundan SONRA ilan edilmiştir; 31 Aralık 2025 itibarıyla işletmenin mevcut bir yükümlülüğü YOKTUR. İlanın yayım onayından önce olması bunu değiştirmez — düzeltme gerektirmeyen olaydır. 2025 bilançosunda borç gösterilmez; TMS 1 uyarınca açıklanır.",
  "TMS 10 - temettü senaryosu (2×2 çapraz)")

q("Raporlama döneminden sonra işletmenin önemli tutarda sermaye artırımına gitmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektirmeyen olaydır; önemliyse açıklanır",
  ["Düzeltme gerektiren olaydır; artırılan sermaye dönem sonu bilançosuna yansıtılmak zorundadır",
   "Düzeltme gerektiren olaydır; özkaynak toplamı dönem sonu itibarıyla düzeltilmek zorunda kalınır",
   "Düzeltme gerektirmeyen olaydır; ancak önemli olsa dahi hiç açıklanmamak zorunda tutulmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: raporlama döneminden sonra gerçekleştirilen sermaye ve borç ihraçları gibi büyük tutarlı işlemler, düzeltme gerektirmeyen olay örneğidir. Sermaye dönem sonunda henüz artırılmamıştır; tutar düzeltilmez, önemliyse açıklanır.",
  "TMS 10 - sermaye artırımı")

q("Raporlama döneminden sonra kur değişimlerinde olağandışı büyüklükte dalgalanma yaşanması bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektirmeyen olaydır; önemliyse açıklanır",
  ["Düzeltme gerektiren olaydır; yabancı para kalemler yeni kurla yeniden çevrilmek zorunda kalınır",
   "Düzeltme gerektiren olaydır; kur farkı dönem sonu tablolarına yansıtılmak zorunda tutulmaktadır",
   "Düzeltme gerektirmeyen olaydır; ancak önemli olsa dahi hiç açıklanmamak zorunda bulunmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: raporlama döneminden sonra döviz kurlarında olağandışı büyüklükte değişiklikler olması, düzeltme gerektirmeyen olay örneğidir. Dönem sonu çevrimi KAPANIŞ kuruyla yapılır (TMS 21); sonraki dalgalanma dönem sonu tutarlarını değiştirmez, önemliyse açıklanır.",
  "TMS 10 - kur dalgalanması")

q("Raporlama döneminden sonra başlatılan ve tümüyle sonraki olaylardan kaynaklanan bir dava bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektirmeyen olaydır; önemliyse açıklanır",
  ["Düzeltme gerektiren olaydır; dönem sonu tablolarında karşılık ayrılmak zorunda bulunmaktadır",
   "Düzeltme gerektiren olaydır; dönem sonu itibarıyla koşullu borç muhasebeleştirilmek zorundadır",
   "Düzeltme gerektirmeyen olaydır; ancak önemli olsa dahi hiç açıklanmamak zorunda kalınmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: raporlama döneminden sonra ortaya çıkan olaylardan kaynaklanan davaların başlaması, düzeltme gerektirmeyen olay örneğidir. Davanın dayandığı olay dönem sonunda YOKTUR; dönem sonunda mevcut bir yükümlülük doğmaz — karşılık ayrılmaz, önemliyse açıklanır.",
  "TMS 10 - sonraki olaydan doğan dava")

q("Aşağıdakilerden hangisi TMS 10'a göre düzeltme gerektirmeyen olaydır?",
  "Raporlama döneminden sonra önemli bir bağlı ortaklığın elden çıkarılması",
  ["Dönem sonunda süren davanın sonraki dönemde sonuçlanarak mevcut yükümlülüğü teyit etmiş olması",
   "Dönem sonundan sonra alınan bilginin varlığın dönem sonunda değersizleştiğini göstermiş olması",
   "Finansal tabloların yanlış olduğunu ortaya koyan bir hilenin sonraki dönemde bulunmuş olması",
   "Dönem sonundan önce alınan varlıkların maliyetinin sonraki dönemde kesin olarak belirlenmesi"],
  "TMS 10: önemli bir bağlı ortaklığın elden çıkarılması dönem sonundan SONRAKİ bir koşuldur; düzeltme gerektirmez, açıklanır. Diğer şıkların hepsinde ilgili durum dönem sonunda ZATEN VARDIR; hepsi düzeltme gerektiren olaydır.",
  "TMS 10 - düzeltme gerektirmeyen örnek")

q("Aşağıdakilerden hangileri TMS 10'a göre düzeltme gerektirmeyen olaydır?\n\nI. Dönem sonundan sonra çıkan yangında fabrikanın yok olması\n\nII. Dönem sonundan sonra ilan edilen kâr payı\n\nIII. Dönem sonundan sonra yatırımların piyasa değerinin düşmesi",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "I ve III"],
  "Üçü de düzeltme gerektirmeyen olaydır: yangın (I), dönem sonundan sonra ilan edilen kâr payı (II) ve yatırımların piyasa değerindeki düşüş (III). Üçünde de ilgili koşul dönem sonundan SONRA ortaya çıkmıştır; tutarlar düzeltilmez, önemliyse açıklanır.",
  "TMS 10 - düzeltme gerektirmeyen olaylar")

q("Bir işletmenin 31 Aralık 2025 tarihli bilançosunda 800.000 ₺ değerle izlenen deposu, 15 Ocak 2026'da çıkan selde tümüyle kullanılamaz hâle gelmiştir. Tablolar 3 Mart 2026'da onaylanmıştır. TMS 10'a göre aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektirmeyen bir olaydır ve deponun 2025 defter değeri düzeltilmez",
  ["Düzeltme gerektiren bir olaydır ve deponun 2025 defter değeri sıfırlanmak zorunda bulunmaktadır",
   "Düzeltme gerektirmeyen bir olaydır, ancak sel gerçekleştiğinden defter değeri düzeltilmek zorundadır",
   "Düzeltme gerektiren bir olaydır, ancak sel sonraki dönemde olduğundan defter değeri düzeltilmez",
   "Düzeltme gerektiren bir olaydır ve deponun değeri net gerçekleşebilir değere indirilmek zorundadır"],
  "TMS 10: depo 31 Aralık 2025'te SAĞLAMDIR; sel dönem sonundan sonraki bir koşuldur. Düzeltme gerektirmeyen olaydır — 2025 defter değeri 800.000 ₺ olarak kalır. Olay önemli olduğundan niteliği ve finansal etkisinin tahmini dipnotlarda açıklanır ve süreklilik değerlendirmesi ayrıca yapılır.",
  "TMS 10 - afet senaryosu (2×2 çapraz)")

q("Düzeltme gerektirmeyen bir olayın finansal etkisinin tahmin edilememesi hâlinde aşağıdakilerden hangisi doğrudur?",
  "Olayın niteliği ve etkinin tahmin edilemediği açıklanır",
  ["Etki tahmin edilemiyorsa hiçbir açıklama yapılmamak zorunda olan bir durumu ifade etmektedir",
   "Etki tahmin edilemiyorsa olay düzeltme gerektiren olaya dönüşmek zorunda kalan bir durumdur",
   "Etki tahmin edilemiyorsa finansal tabloların yayımı ertelenmek zorunda tutulan bir durumdur",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: işletme, düzeltme gerektirmeyen önemli her olay için olayın niteliğini ve finansal etkisinin tahminini açıklar; bu TAHMİNİN YAPILAMAMASI durumunda ise bu duruma ilişkin açıklamayı yapar. Açıklama yükümlülüğü ortadan kalkmaz.",
  "TMS 10 - tahmin edilemeyen etki")

q("Aşağıdaki ifadelerden hangileri düzeltme gerektirmeyen olaylar bakımından doğrudur?\n\nI. Dönem sonu tutarları düzeltilmez\n\nII. Önemli olsa bile hiçbir açıklama yapılmaz\n\nIII. Önemliyse niteliği ve finansal etkisinin tahmini açıklanır",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "II ve III"],
  "Düzeltme gerektirmeyen olaylarda dönem sonu tutarları düzeltilmez (I) ve olay önemliyse niteliği ile finansal etkisinin tahmini açıklanır (III). II, III ile çelişir: önemli olaylar AÇIKLANIR; açıklanmaması kullanıcıların kararlarını etkileyebilir.",
  "TMS 10 - düzeltme gerektirmeyen olaylar")

q("Raporlama döneminden sonra duran varlıkların elden çıkarılmasına ilişkin plan açıklanması bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektirmeyen olaydır; önemliyse açıklanır",
  ["Düzeltme gerektiren olaydır; varlıklar dönem sonu bilançosunda satış amaçlı sınıflandırılmalıdır",
   "Düzeltme gerektiren olaydır; varlıkların dönem sonu değeri gerçeğe uygun değere indirilmelidir",
   "Düzeltme gerektirmeyen olaydır; ancak önemli olsa dahi hiç açıklanmamak zorunda kalınmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: raporlama döneminden sonra faaliyetin durdurulmasına yönelik plan açıklanması veya varlıkların elden çıkarılması, düzeltme gerektirmeyen olay örneğidir. Plan dönem sonunda YOKTUR; TFRS 5 sınıflandırma koşulları dönem sonunda sağlanmamıştır — tutarlar düzeltilmez, önemliyse açıklanır.",
  "TMS 10 - elden çıkarma planı")

q("Raporlama döneminden sonra vergi oranlarında veya vergi kanunlarında yapılan değişikliğin yürürlüğe girmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektirmeyen olaydır; dönem sonu vergi tutarları düzeltilmez, önemliyse açıklanır",
  ["Düzeltme gerektiren olaydır; dönem sonu ertelenmiş vergi tutarları düzeltilmek zorunda kalınır",
   "Düzeltme gerektiren olaydır; dönem vergi gideri yeni orana göre yeniden hesaplanmak zorundadır",
   "Düzeltme gerektirmeyen olaydır; ancak önemli olsa dahi hiç açıklanmamak zorunda bulunmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: raporlama döneminden sonra vergi oranlarında veya vergi kanunlarında yürürlüğe giren ya da açıklanan ve dönem vergisi ile ertelenmiş vergi varlık/borçlarını önemli ölçüde etkileyen değişiklikler, düzeltme gerektirmeyen olay örneğidir. Dönem sonu tutarları düzeltilmez, önemliyse açıklanır.",
  "TMS 10 - vergi mevzuatı değişikliği")

# ── D. İşletmenin sürekliliği ve genel hükümler (16) ───────────────────────
q("Raporlama döneminden sonra yönetimin işletmeyi tasfiye etme niyetinde olması hâlinde aşağıdakilerden hangisi doğrudur?",
  "Finansal tablolar işletmenin sürekliliği esasına göre hazırlanmaz",
  ["Finansal tablolar süreklilik esasına göre hazırlanır; durum yalnızca dipnotlarda açıklanmaktadır",
   "Finansal tablolar süreklilik esasına göre hazırlanır; tasfiye yalnızca izleyen dönemi etkiler",
   "Finansal tablolar değişmez; tasfiye kararı düzeltme gerektirmeyen olay sayılmak zorundadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: raporlama döneminden sonra yönetim, işletmeyi tasfiye etme veya ticari faaliyetine son verme niyetinde olduğunu belirlemişse ya da bunlara mecbursa, finansal tablolar İŞLETMENİN SÜREKLİLİĞİ ESASINA GÖRE HAZIRLANMAZ. Bu, düzeltme gerektiren/gerektirmeyen ayrımının dışında, muhasebenin ESASINI değiştiren bir hükümdür.",
  "TMS 10 - süreklilik (temel hüküm)")

q("Sürekliliğin ortadan kalkması hâlinde TMS 10'un öngördüğü yaklaşım bakımından aşağıdakilerden hangisi doğrudur?",
  "Etki o kadar yaygındır ki muhasebe esası değişir; yalnızca tutarları düzeltmek yeterli değildir",
  ["Yalnızca ilgili varlık ve borç tutarlarının düzeltilmesi yeterli sayılmak zorunda bulunmaktadır",
   "Yalnızca dipnotlarda kapsamlı bir açıklama yapılması yeterli sayılmak zorunda tutulmaktadır",
   "Yalnızca izleyen dönemin finansal tablolarında gerekli değişiklikler yapılmak zorunda kalınır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: sürekliliğin ortadan kalkmasının etkisi o kadar yaygındır ki, Standart tutarların düzeltilmesini değil, MUHASEBE ESASININ TEMELDEN DEĞİŞTİRİLMESİNİ gerektirir. Süreklilik esası terk edilir.",
  "TMS 10 - süreklilik yaklaşımı")

q("Raporlama döneminden sonra faaliyet sonuçlarında ve mali durumda ortaya çıkan bozulmanın süreklilik açısından değerlendirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin süreklilik varsayımının hâlâ geçerli olup olmadığı yeniden değerlendirilir",
  ["Bozulma her hâlde göz ardı edilir; süreklilik yalnızca dönem sonu verilerine göre değerlendirilir",
   "Bozulma her hâlde düzeltme gerektiren olay sayılır ve tüm tutarlar düzeltilmek zorunda kalınır",
   "Bozulma yalnızca izleyen dönemin tablolarında dikkate alınmak zorunda tutulan bir durumdur",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: raporlama döneminden sonra faaliyet sonuçları ile finansal durumda meydana gelen bozulma, işletmenin süreklilik varsayımının hâlâ uygun olup olmadığının yeniden değerlendirilmesini gerektirebilir. Bu değerlendirme dönem sonu verileriyle sınırlı kalmaz.",
  "TMS 10 - sürekliliğin yeniden değerlendirilmesi")

q("Aşağıdaki ifadelerden hangileri işletmenin sürekliliği bakımından doğrudur?\n\nI. Süreklilik ortadan kalkarsa tablolar süreklilik esasına göre hazırlanmaz\n\nII. Etkisi yaygın olduğundan muhasebe esası değişir\n\nIII. Yalnızca dipnot açıklaması yapılması yeterlidir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "I ve III"],
  "Süreklilik ortadan kalkarsa tablolar süreklilik esasına göre hazırlanmaz (I) ve etkisi yaygın olduğundan muhasebe esası temelden değişir (II). Yalnızca dipnot açıklamasıyla yetinmek YETERLİ DEĞİLDİR; bu nedenle III yanlıştır.",
  "TMS 10 - süreklilik")

q("Bir işletmenin tek üretim tesisi, 31 Aralık 2025 dönem sonundan sonra kamulaştırılmış ve yönetim başka faaliyet alanı bulunmadığından işletmeyi tasfiye etme kararı almıştır. Tablolar henüz onaylanmamıştır. TMS 10'a göre aşağıdakilerden hangisi doğrudur?",
  "2025 finansal tabloları işletmenin sürekliliği esasına göre hazırlanmaz",
  ["2025 tabloları süreklilik esasına göre hazırlanır; olay yalnızca dipnotlarda açıklanmak zorundadır",
   "2025 tabloları süreklilik esasına göre hazırlanır; tasfiye kararı yalnızca 2026'yı etkilemektedir",
   "2025 tablolarında yalnızca üretim tesisinin defter değeri sıfırlanmak zorunda bulunmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: yönetim dönem sonundan sonra işletmeyi tasfiye etme niyetini belirlemişse, finansal tablolar süreklilik esasına göre hazırlanmaz. Olay dönem sonundan sonra gerçekleşmiş olsa bile sonuç değişmez — bu, düzeltme gerektiren/gerektirmeyen ayrımının DIŞINDA özel bir hükümdür; etkisi yaygın olduğundan muhasebe esasının kendisi değişir.",
  "TMS 10 - süreklilik senaryosu")

q("TMS 10'un amacı bakımından aşağıdakilerden hangisi doğrudur?",
  "Sonraki olaylar için tabloların ne zaman düzeltileceğini ve hangi açıklamaların yapılacağını belirlemek",
  ["Yalnızca finansal tabloların hangi tarihte yayımlanacağını belirlemeyi amaçlayan bir düzenlemedir",
   "Yalnızca işletmenin sürekliliğinin nasıl değerlendirileceğini belirlemeyi amaçlayan bir düzenlemedir",
   "Yalnızca karşılıkların nasıl ölçüleceğini belirlemeyi amaçlayan dar kapsamlı bir düzenlemedir",
   "TMS 10'un amacı Standartta belirtilmemiş bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 10'un amacı: bir işletmenin, raporlama döneminden sonraki olaylar dolayısıyla finansal tablolarını ne zaman düzelteceğini ve tabloların yayımı için onaylandığı tarihe ilişkin olarak hangi açıklamaları yapacağını belirlemektir.",
  "TMS 10 - amaç")

q("Aşağıdaki ifadelerden hangileri TMS 10 bakımından doğrudur?\n\nI. Dönem sonundan sonra ilan edilen kâr payı dönem sonunda borç olarak muhasebeleştirilir\n\nII. Onay tarihi ve onayı veren açıklanır\n\nIII. Düzeltme gerektiren olaylarda tutarlar düzeltilir",
  "II ve III",
  ["I, II ve III", "Yalnız II", "I ve II", "I ve III"],
  "Onay tarihi ile onayı verenin açıklanması (II) ve düzeltme gerektiren olaylarda tutarların düzeltilmesi (III) doğrudur. Dönem sonundan sonra ilan edilen kâr payı ise dönem sonunda BORÇ OLARAK MUHASEBELEŞTİRİLMEZ (TMS 32: dönem sonunda mevcut yükümlülük yoktur); bu nedenle I yanlıştır.",
  "TMS 10 - genel hükümler")

q("Ortakların finansal tabloları yayımlandıktan sonra değiştirme yetkisine sahip olması hâlinde aşağıdakilerden hangisi doğrudur?",
  "Bu durum açıklanır; onay tarihi yine yayım için onayın verildiği tarihtir",
  ["Bu durumda onay tarihi ortakların onayladığı tarihe ötelenmek zorunda olan bir durumu ifade eder",
   "Bu durumda finansal tablolar hiçbir hâlde yayımlanamaz; onay beklenmek zorunda kalınmaktadır",
   "Bu durumun açıklanmasına gerek bulunmamakta olup yalnızca onay tarihi verilmek durumundadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: işletmenin ortaklarının veya diğer kişilerin finansal tabloları yayımlandıktan sonra değiştirmeye yetkisi bulunuyorsa, işletme bu durumu AÇIKLAR. Ancak esas alınan tarih yine tabloların YAYIM İÇİN ONAYLANDIĞI tarihtir; sonraki değiştirme yetkisi bu tarihi ötelemez.",
  "TMS 10 - ortakların değiştirme yetkisi")

q("Bir işletmenin yönetimi, 31 Aralık 2025 tarihli tabloları 20 Şubat 2026'da yayım için onaylamış; ancak 25 Şubat 2026'da düzeltme gerektiren önemli bir olay öğrenilmiştir. TMS 10 bakımından aşağıdakilerden hangisi doğrudur?",
  "Olay onay tarihinden sonra öğrenildiğinden 2025 tablolarında düzeltme yapılmaz",
  ["Olay her hâlde düzeltme gerektiren olay sayılır ve 2025 tabloları düzeltilmek zorunda kalınmaktadır",
   "Olay düzeltme gerektirmeyen olay sayılır ve 2025 tablolarının dipnotlarında açıklanmak zorundadır",
   "Olay nedeniyle 2025 tablolarının onayı geri alınmak ve tablolar yeniden onaylanmak zorundadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: sonraki olaylar penceresi 20 Şubat'taki YAYIM ONAYIYLA kapanmıştır. 25 Şubat'ta öğrenilen olay — niteliği düzeltme gerektiren türden olsa bile — bu pencerenin dışındadır ve 2025 tablolarını etkilemez. Pencere, olayın niteliğinden önce gelen bir ön koşuldur.",
  "TMS 10 - pencerenin önceliği (senaryo)")

q("Aşağıdakilerden hangisi TMS 10'a göre finansal tabloların yayımı için onaylandığı tarihi belirlerken esas alınır?",
  "Tabloların ilgili organca yayıma onaylandığı tarih",
  ["Finansal tabloların bağımsız denetçi tarafından denetlenmeye başlandığı tarih esas alınmaktadır",
   "Finansal tabloların ticaret sicilinde ilan edilerek yayımlandığı tarih esas alınmak durumundadır",
   "Finansal tabloların kurumlar vergisi beyannamesine eklenerek verildiği tarih esas alınmaktadır",
   "Finansal tabloların ilgili hesap döneminin sona erdiği ve kapanış kaydının yapıldığı tarih"],
  "TMS 10: esas alınan tarih, finansal tabloların yayımı için ONAYLANDIĞI tarihtir — yani yetkili organın tabloları yayıma onayladığı tarih. Denetimin başlaması, sicil ilanı, beyanname tarihi veya dönem sonu bu tarihi belirlemez.",
  "TMS 10 - onay tarihinin belirlenmesi")

q("Aşağıdaki ifadelerden hangileri TMS 10'un amacı ve kapsamı bakımından doğrudur?\n\nI. Tabloların ne zaman düzeltileceğini belirler\n\nII. Yalnızca aleyhteki olayları kapsar\n\nIII. Onay tarihine ilişkin açıklamaları belirler",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "II ve III"],
  "TMS 10, sonraki olaylar nedeniyle tabloların ne zaman düzeltileceğini (I) ve onay tarihine ilişkin hangi açıklamaların yapılacağını (III) belirler. Standart LEHTE VE ALEYHTE tüm olayları kapsar; bu nedenle II yanlıştır.",
  "TMS 10 - amaç ve kapsam")

q("Bir işletmenin dönem sonundaki stoklarının maliyeti 400.000 ₺'dir. Bu stoklar 10 Ocak 2026'da 340.000 ₺'ye satılmış ve satış fiyatı dönem sonundaki net gerçekleşebilir değere kanıt oluşturmuştur. Tablolar 2 Mart 2026'da onaylanmıştır. TMS 10'a göre 2025 bilançosunda stoklar kaç ₺ ile gösterilir?",
  "340.000 ₺",
  ["400.000 ₺", "60.000 ₺", "740.000 ₺", "370.000 ₺"],
  "TMS 10: dönem sonundan sonraki satış, stokun dönem sonundaki net gerçekleşebilir değerine kanıt sağladığından DÜZELTME GEREKTİREN olaydır. TMS 2 uyarınca stoklar maliyet (400.000 ₺) ile NGD (340.000 ₺) karşılaştırılıp DÜŞÜĞÜ ile ölçülür: 340.000 ₺. Ayrıca 400.000 − 340.000 = 60.000 ₺ değer düşüklüğü zararı 2025 kâr/zararına yazılır.",
  "TMS 10 - stok değerleme (hesap)")

q("Düzeltme gerektiren bir olayın finansal tablolara etkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Hem tutarlar düzeltilir hem de ilgili açıklamalar güncellenir",
  ["Yalnızca tutarlar düzeltilir; açıklamaların güncellenmesine gerek bulunmamak durumundadır",
   "Yalnızca açıklamalar güncellenir; tutarların düzeltilmesine gerek bulunmamak zorundadır",
   "Ne tutarlar düzeltilir ne de açıklamalar güncellenir; olay izleyen döneme bırakılmaktadır",
   "Bu husus TMS 10'da düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 10: düzeltme gerektiren olaylarda işletme tutarları düzeltir; ayrıca dönem sonunda var olan bir duruma ilişkin sonradan bilgi alınması hâlinde ilgili AÇIKLAMALARINI da bu yeni bilgi ışığında günceller. İkisi birlikte yapılır.",
  "TMS 10 - düzeltmenin bütünü")

q("Aşağıdakilerden hangisi TMS 10'a göre düzeltme gerektiren ↔ gerektirmeyen ayrımında belirleyicidir?",
  "İlgili durumun raporlama dönemi sonunda var olup olmadığı",
  ["Olayın işletme yönetimince hangi tarihte öğrenilmiş olduğu hususu belirleyici sayılmaktadır",
   "Olayın işletmenin lehine mi yoksa aleyhine mi sonuç doğurduğu hususu belirleyici olmaktadır",
   "Olayın tutarının önemlilik düzeyini aşıp aşmadığı hususu belirleyici sayılmak durumundadır",
   "Olayın nakit çıkışı gerektirip gerektirmediği hususu belirleyici sayılmak zorunda bulunmaktadır"],
  "TMS 10: ayrımın tek ölçütü, olayın ilişkin olduğu DURUMUN raporlama dönemi sonunda var olup olmadığıdır. Öğrenme tarihi, lehte/aleyhte oluş, önemlilik ve nakit etkisi bu ayrımı değiştirmez — önemlilik yalnızca AÇIKLAMA yükümlülüğünü etkiler.",
  "TMS 10 - ayrımın ölçütü")

q("Bir işletme, 31 Aralık 2025 itibarıyla şüpheli hâle gelmemiş 90.000 ₺ alacağını, borçlunun 5 Şubat 2026'da beklenmedik bir yangında tüm varlıklarını kaybetmesi üzerine tahsil edemeyecek duruma gelmiştir. TMS 10'a göre aşağıdakilerden hangisi doğrudur?",
  "Düzeltme gerektirmeyen olaydır; 2025 alacağı düzeltilmez, önemliyse açıklanır",
  ["Düzeltme gerektiren olaydır; 2025 alacağı için değer düşüklüğü muhasebeleştirilmek zorundadır",
   "Düzeltme gerektiren olaydır; alacak 2025 bilançosundan tümüyle çıkarılmak zorunda kalınmaktadır",
   "Düzeltme gerektirmeyen olaydır; ancak önemli olsa dahi hiç açıklanmamak zorunda tutulmaktadır",
   "Düzeltme gerektiren olaydır; ancak yangın sonraki dönemde olduğundan alacak düzeltilmez"],
  "⚠ Bu, müşterinin iflası örneğinin AYNASIDIR ve ayrımın ölçütünü sınar. Borçlu 31 Aralık'ta ÖDEME GÜCÜNE SAHİPTİR; tahsil edilemezliğin nedeni dönem sonundan SONRAKİ yangındır. Dönem sonunda var olan bir duruma kanıt sağlanmadığından düzeltme gerektirmeyen olaydır. (İflas örneğinde ise mali sıkıntı dönem sonunda zaten vardır → düzeltme gerektirir.)",
  "TMS 10 - iflasın aynası (ayrım sınaması)")

q("Aşağıdakilerden hangileri TMS 10'a göre raporlama döneminden sonraki olaylara örnektir?\n\nI. Dönem sonundan sonra ilan edilen kâr payı\n\nII. Dönem sonunda süren davanın sonraki dönemde sonuçlanması\n\nIII. Dönem sonundan sonra gerçekleşen işletme birleşmesi",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "I ve III"],
  "Üçü de raporlama döneminden sonraki olaydır — sonraki olay olmak için pencere içinde gerçekleşmek yeterlidir. Aralarındaki fark düzeltme gerektirip gerektirmemeleridir: dava (II) düzeltme gerektirir; kâr payı (I) ve işletme birleşmesi (III) düzeltme gerektirmez, açıklanır.",
  "TMS 10 - sonraki olay örnekleri")

print("TOPLAM:", len(Q))

# ══ BUILD ═════════════════════════════════════════════════════════════════
def gen_letters(n, seed):
    r = random.Random(seed)
    base = ["ABCDE"[i % 5] for i in range(n)]
    while True:
        r.shuffle(base)
        if all(not (base[i] == base[i-1] == base[i-2]) for i in range(2, len(base))):
            return base

if __name__ == "__main__":
    assert len(Q) == 60, f"60 olmalı, şu an {len(Q)}"
    letters = gen_letters(len(Q), SEED)
    out = []
    for i, it in enumerate(Q):
        ans = letters[i]
        opts = {ans: it["correct"]}
        for k, d in zip([k for k in "ABCDE" if k != ans], it["distractors"]):
            opts[k] = d
        assert len(set(opts.values())) == 5, f"{PREFIX}-{i+1}: şık tekrarı"
        out.append({
            "id": f"{PREFIX}-{i+1:04d}", "ders": DERS, "konu": KONU,
            "stem": it["stem"], "options": opts, "answer": ans,
            "solution": it["why"] + f" Doğru cevap {ans}.",
            "source": {"kind": "generated",
                       "styleRef": "SGS Muhasebe Standartları (TMS 10; 2023/2021/2020/2016-18 kalıbına kalibre)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    dagilim = collections.Counter(x["options"][x["answer"]].strip() for x in onc)
    hepsi = dagilim["I, II ve III"]
    en_cok = dagilim.most_common(1)[0] if dagilim else ("-", 0)
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} | hepsi {hepsi} (%{hepsi*100//max(len(onc),1)}) "
          f"| en çok tekrar eden öncül cevabı: {en_cok[0]!r} ×{en_cok[1]}")
    print("   öncül cevap dağılımı:", dict(dagilim))
    assert en_cok[1] <= len(onc) * 0.4, f"öncüllerde örüntü: {en_cok}"
    assert 0.1 <= hepsi / max(len(onc), 1) <= 0.3, f"'hepsi' oranı {hepsi}/{len(onc)}"
    print("   harf:", "".join(x["answer"] for x in out))
