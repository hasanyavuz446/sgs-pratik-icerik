# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / Kavramsal Çerçeve (2018 sürümü) — 60 soru.
Kaynak: KGK, Finansal Raporlamaya İlişkin Kavramsal Çerçeve (2018).
SGS seviyesi: tanım, kapsam, temel ilke. Doğru şık KISA, çeldiriciler UZUN.
SGS şeması: ders/konu/stem/options/answer/solution + "Doğru cevap X." çözümde.
"""
import json, random, re

DERS, KONU = "muhasebe_standartlari", "kavramsal_cerceve"
PREFIX, SEED = "std-cerceve-gen", 20260920
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/kavramsal_cerceve.json"

Q = []
def q(stem, correct, distractors, why, ref, onculu=False):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref, onculu=onculu))

# ── A. Çerçevenin amacı ve statüsü (8) ─────────────────────────────────────
q("Finansal Raporlamaya İlişkin Kavramsal Çerçeve'nin amacı bakımından aşağıdakilerden hangisi doğrudur?",
  "Standart geliştirmeye temel oluşturmak, standart bulunmayan konularda politika belirlemeye yardımcı olmak ve ilgilileri standartları anlamada desteklemektir",
  ["Her işlem için ayrıntılı muhasebe kuralları koyarak standartların yerine geçmeyi amaçlayan bir düzenlemedir",
   "İşletmelerin vergi matrahını belirlemeye yönelik hesaplama yöntemlerini gösteren bir rehber niteliğindedir",
   "Yalnızca bağımsız denetçilerin denetim programını hazırlamasına yardımcı olan bir denetim standardıdır",
   "İşletmelerin gelecekteki kârlılığını tahmin etmeye yarayan bir finansal analiz yöntemleri kılavuzudur"],
  "Kavramsal Çerçeve; standart geliştirilmesine temel oluşturmak, belirli bir standardın bulunmadığı durumlarda muhasebe politikası geliştirilmesine yardımcı olmak ve ilgililerin standartları anlamasına ve yorumlamasına destek olmak amacını taşır.",
  "Kavramsal Çerçeve (2018) - amaç")

q("Kavramsal Çerçeve'nin hukuki statüsü bakımından aşağıdakilerden hangisi doğrudur?",
  "Kavramsal Çerçeve bir standart değildir ve hiçbir standardın hükmünü geçersiz kılmaz",
  ["Kavramsal Çerçeve bir standart olup diğer tüm standartların üzerinde bağlayıcı hüküm ifade etmektedir",
   "Kavramsal Çerçeve ile bir standart çeliştiğinde her hâlde Kavramsal Çerçeve hükmü uygulanmaktadır",
   "Kavramsal Çerçeve yalnızca akademik bir metin olup uygulamada hiçbir işlevi bulunmamaktadır",
   "Kavramsal Çerçeve her işletmenin kendi muhasebe kurallarını serbestçe belirlemesine izin verir"],
  "Kavramsal Çerçeve bir standart değildir; hiçbir standardın hükmünün yerine geçmez veya onu geçersiz kılmaz. Standart ile Çerçeve çelişirse standart uygulanır.",
  "Kavramsal Çerçeve (2018) - statü")

q("Kavramsal Çerçeve'nin 2018 sürümü bakımından aşağıdakilerden hangisi doğrudur?",
  "Önceki sürümdeki boşlukları gidermiş, ölçüm ve raporlayan işletme gibi konuları güncellemiştir",
  ["Önceki sürümü aynen tekrarlamış olup hiçbir konuda değişiklik veya güncelleme getirmemektedir",
   "Kavramsal Çerçeve'yi tümüyle yürürlükten kaldırmış ve yerine hiçbir metin koymamış bulunmaktadır",
   "Yalnızca vergi mevzuatına ilişkin düzenlemeler getirmiş olup finansal raporlamayla ilgisi yoktur",
   "Yalnızca denetim standartlarını düzenlemiş olup muhasebe standartlarını hiç ele almamaktadır"],
  "2018 sürümü; ölçüm, sunum ve açıklama, raporlayan işletme ile finansal tablo dışı bırakma gibi konularda önceki sürümdeki boşlukları gidermiş ve tanımları güncellemiştir.",
  "Kavramsal Çerçeve (2018) - 2018 güncellemesi")

q("Standart bulunmayan bir konuda muhasebe politikası belirlenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme, benzer konulardaki standartlara ve Kavramsal Çerçeve'deki kavramlara başvurarak politika geliştirir",
  ["İşletme böyle bir konuda hiçbir kayıt yapmaz ve işlemi finansal tablolara hiç yansıtmamaktadır",
   "İşletme dilediği yöntemi hiçbir dayanak aramaksızın ve tümüyle serbestçe seçebilmektedir",
   "İşletme her hâlde vergi mevzuatındaki düzenlemeyi esas alarak politikasını belirlemek zorundadır",
   "İşletme bu durumda finansal tablo düzenlemekten tümüyle muaf tutulmuş olmaktadır"],
  "TMS 8 ve Kavramsal Çerçeve: belirli bir işleme uygulanacak standart yoksa yönetim; benzer konulardaki standartların hükümlerine ve Kavramsal Çerçeve'deki kavram, tanım ve ölçütlere başvurarak muhasebe politikası geliştirir.",
  "Kavramsal Çerçeve (2018) - politika geliştirme")

q("Genel amaçlı finansal raporlamanın amacı bakımından aşağıdakilerden hangisi doğrudur?",
  "Mevcut ve potansiyel yatırımcılar, borç verenler ve diğer kredi verenlere kaynak sağlama kararlarında yararlı finansal bilgi sunmaktır",
  ["Yalnızca işletme yönetiminin iç kararlarına hizmet eden ayrıntılı raporlar üretmeyi amaçlamaktadır",
   "Yalnızca vergi idaresinin matrah tespitine yönelik bilgi üretmeyi ve beyanname hazırlamayı amaçlar",
   "İşletmenin piyasa değerini doğrudan ve kesin biçimde göstermeyi amaçlayan bir değerleme aracıdır",
   "Yalnızca işletmenin çalışanlarına ücret bilgisi sunmayı amaçlayan bir raporlama biçimidir"],
  "Kavramsal Çerçeve: genel amaçlı finansal raporlamanın amacı; mevcut ve potansiyel yatırımcılara, borç verenlere ve diğer kredi verenlere işletmeye kaynak sağlama kararlarında yararlı olacak finansal bilgiyi sunmaktır.",
  "Kavramsal Çerçeve (2018) - raporlamanın amacı")

q("Genel amaçlı finansal raporların birincil kullanıcıları bakımından aşağıdakilerden hangisi doğrudur?",
  "Mevcut ve potansiyel yatırımcılar, borç verenler ve diğer kredi verenler birincil kullanıcılardır",
  ["Birincil kullanıcılar yalnızca işletmenin yöneticileri olup dış taraflar kapsam dışında bırakılmıştır",
   "Birincil kullanıcı yalnızca vergi idaresidir; diğer taraflar finansal raporlardan yararlanamamaktadır",
   "Birincil kullanıcılar kanunda sayılmamış olup her işletme kendi kullanıcısını serbestçe belirler",
   "Birincil kullanıcı yalnızca işletmenin bağımsız denetçisi olup başka bir taraf söz konusu değildir"],
  "Kavramsal Çerçeve: birincil kullanıcılar mevcut ve potansiyel yatırımcılar, borç verenler ve diğer kredi verenlerdir. Yönetim ve düzenleyiciler genel amaçlı raporlara dayanmak zorunda olmadığından birincil kullanıcı sayılmaz.",
  "Kavramsal Çerçeve (2018) - kullanıcılar")

q("Genel amaçlı finansal raporların sınırları bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal raporlar kullanıcıların ihtiyaç duyduğu tüm bilgiyi sağlamaz ve işletmenin değerini göstermez",
  ["Finansal raporlar kullanıcıların ihtiyaç duyduğu her türlü bilgiyi eksiksiz biçimde sağlamaktadır",
   "Finansal raporlar işletmenin piyasa değerini kesin ve tartışmasız biçimde ortaya koymaktadır",
   "Finansal raporlar gelecekteki nakit akışlarını kesin olarak öngören bir tahmin aracı niteliğindedir",
   "Finansal raporlar hiçbir sınırlama taşımaz; her kullanıcının her sorusuna yanıt vermektedir"],
  "Kavramsal Çerçeve: genel amaçlı finansal raporlar kullanıcıların ihtiyaç duyduğu tüm bilgiyi sağlamaz ve işletmenin değerini göstermeyi amaçlamaz; kullanıcıların işletme değerini tahmin etmesine yardımcı olur.",
  "Kavramsal Çerçeve (2018) - raporların sınırı")

q("Kavramsal Çerçeve bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kavramsal Çerçeve bir standart değildir\n\nII. Standart geliştirmeye temel oluşturur\n\nIII. Bir standartla çeliştiğinde Çerçeve hükmü uygulanır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Kavramsal Çerçeve bir standart değildir (I) ve standart geliştirmeye temel oluşturur (II). Ancak hiçbir standardın hükmünü geçersiz kılmaz; çelişki hâlinde standart uygulanır, bu nedenle III yanlıştır.",
  "Kavramsal Çerçeve (2018) - statü", onculu=True)

# ── B. Niteliksel özellikler (12) ──────────────────────────────────────────
q("Finansal bilginin temel niteliksel özellikleri bakımından aşağıdakilerden hangisi doğrudur?",
  "İhtiyaca uygunluk ve gerçeğe uygun şekilde sunum temel niteliksel özelliklerdir",
  ["Karşılaştırılabilirlik ve doğrulanabilirlik temel niteliksel özellikler olarak kabul edilmektedir",
   "Zamanında sunum ve anlaşılabilirlik temel niteliksel özellikleri oluşturan iki unsurdur",
   "Temel niteliksel özellik tek olup yalnızca ihtiyaca uygunluktan ibaret bulunmaktadır",
   "Niteliksel özellikler kavramı Çerçeve'de düzenlenmemiş olup uygulamada kullanılmamaktadır"],
  "Kavramsal Çerçeve: temel (asli) niteliksel özellikler ihtiyaca uygunluk ve gerçeğe uygun şekilde sunumdur. Karşılaştırılabilirlik, doğrulanabilirlik, zamanında sunum ve anlaşılabilirlik ise destekleyici özelliklerdir.",
  "Kavramsal Çerçeve (2018) - niteliksel özellikler")

q("İhtiyaca uygunluk bakımından aşağıdakilerden hangisi doğrudur?",
  "İhtiyaca uygun bilgi, kullanıcıların kararlarında fark yaratabilen bilgidir",
  ["İhtiyaca uygun bilgi, kullanıcıların kararlarını hiçbir biçimde etkilemeyen tarafsız bilgidir",
   "İhtiyaca uygunluk yalnızca bilginin hatasız olmasını ifade eden teknik bir ölçüt niteliğindedir",
   "İhtiyaca uygunluk yalnızca bilginin zamanında sunulmasını ifade eden bir kavram olarak tanımlanır",
   "İhtiyaca uygunluk yalnızca işletmenin geçmiş dönem verilerinin sunulmasını ifade etmektedir"],
  "Kavramsal Çerçeve: ihtiyaca uygun finansal bilgi, kullanıcıların verdiği kararlarda fark yaratabilen bilgidir. Tahmini değer, teyit edici değer veya her ikisini taşıyorsa kararlarda fark yaratabilir.",
  "Kavramsal Çerçeve (2018) - ihtiyaca uygunluk")

q("İhtiyaca uygunluğun unsurları bakımından aşağıdakilerden hangisi doğrudur?",
  "Tahmini değer ve teyit edici değer, bilginin kararlarda fark yaratmasını sağlayan unsurlardır",
  ["Tarafsızlık ve tam olma, ihtiyaca uygunluğun iki temel unsurunu oluşturan ölçütlerdir",
   "Doğrulanabilirlik ve karşılaştırılabilirlik, ihtiyaca uygunluğun unsurları olarak sayılmaktadır",
   "İhtiyaca uygunluğun hiçbir unsuru bulunmayıp tek başına değerlendirilen bir kavramdır",
   "Anlaşılabilirlik ve zamanında sunum, ihtiyaca uygunluğun unsurlarını oluşturmaktadır"],
  "Kavramsal Çerçeve: finansal bilgi, tahmini değere (gelecek sonuçları öngörmede girdi) veya teyit edici değere (önceki değerlendirmeleri doğrulama/değiştirme) ya da her ikisine sahipse kararlarda fark yaratabilir.",
  "Kavramsal Çerçeve (2018) - tahmini/teyit edici değer")

q("Önemlilik kavramı bakımından aşağıdakilerden hangisi doğrudur?",
  "Önemlilik, ihtiyaca uygunluğun işletmeye özgü bir boyutudur ve önceden belirlenmiş bir eşik değeri yoktur",
  ["Önemlilik, tüm işletmeler için geçerli sabit bir tutar olarak Çerçeve'de açıkça belirlenmiştir",
   "Önemlilik yalnızca bilginin tarafsız sunulmasını ifade eden bir gerçeğe uygun sunum unsurudur",
   "Önemlilik yalnızca denetim standartlarının konusu olup Kavramsal Çerçeve'de hiç yer almamaktadır",
   "Önemlilik, işletmenin kâr etme olasılığını ölçen bir finansal performans göstergesi niteliğindedir"],
  "Kavramsal Çerçeve: bilginin verilmemesi, yanlış verilmesi veya gizlenmesi kullanıcıların kararlarını etkileyebiliyorsa o bilgi önemlidir. Önemlilik işletmeye özgüdür; niceliksel bir eşik belirlenmemiştir.",
  "Kavramsal Çerçeve (2018) - önemlilik")

q("Gerçeğe uygun şekilde sunum bakımından aşağıdakilerden hangisi doğrudur?",
  "Bilginin tam, tarafsız ve hatasız olmasını gerektirir",
  ["Bilginin yalnızca hatasız olmasını gerektirir; tam ve tarafsız olması aranmamaktadır",
   "Bilginin işletme yönetiminin istediği sonucu gösterecek biçimde sunulmasını ifade etmektedir",
   "Bilginin her yönüyle kesin ve mutlak doğru olmasını gerektirir; hiçbir tahmine izin verilmez",
   "Bilginin yalnızca hukuki biçimine göre sunulmasını gerektiren bir şekil şartını ifade eder"],
  "Kavramsal Çerçeve: gerçeğe uygun sunum için bilginin tam, tarafsız ve hatasız olması gerekir. Bu, her yönüyle kesin doğruluk anlamına gelmez; tahmin içeren tutarlarda süreç ve girdilerin doğru tanımlanması aranır.",
  "Kavramsal Çerçeve (2018) - gerçeğe uygun sunum")

q("Özün önceliği bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal bilgi, işlemin hukuki biçimini değil ekonomik özünü yansıtmalıdır",
  ["Finansal bilgi her hâlde işlemin hukuki biçimine göre sunulmalı; ekonomik öz dikkate alınmamalıdır",
   "Özün önceliği yalnızca vergi mevzuatının konusu olup finansal raporlamada uygulanmamaktadır",
   "Hukuki biçim ile ekonomik öz her zaman aynıdır; bu nedenle böyle bir ilkeye gerek duyulmamıştır",
   "Özün önceliği, işletmenin dilediği sunum biçimini seçebilmesi anlamına gelen bir serbestidir"],
  "Kavramsal Çerçeve: gerçeğe uygun sunum, işlemin yalnızca hukuki biçimini değil ekonomik özünü yansıtmayı gerektirir. Biçim ile öz farklıysa yalnızca biçime dayalı sunum gerçeğe uygun olmaz.",
  "Kavramsal Çerçeve (2018) - özün önceliği")

q("Tarafsızlık ve ihtiyatlılık ilişkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Tarafsızlık ihtiyatlılıkla desteklenir; ihtiyatlılık belirsizlik altında dikkatli olmaktır, gizli yedek yaratmak değildir",
  ["İhtiyatlılık, varlıkların ve gelirlerin sistematik olarak olduğundan düşük gösterilmesini gerektirir",
   "İhtiyatlılık ile tarafsızlık birbirinin tam zıddı olup ikisi bir arada hiçbir hâlde bulunamaz",
   "İhtiyatlılık, borçların ve giderlerin sistematik olarak olduğundan düşük gösterilmesini ifade eder",
   "İhtiyatlılık kavramı 2018 Çerçevesi'nde tümüyle kaldırılmış olup artık hiç uygulanmamaktadır"],
  "Kavramsal Çerçeve (2018): tarafsızlık ihtiyatlılıkla desteklenir. İhtiyatlılık, belirsizlik koşullarında muhakemede dikkatli olmaktır; varlık/gelirin düşük, borç/giderin yüksek gösterilmesine izin vermez.",
  "Kavramsal Çerçeve (2018) - ihtiyatlılık")

q("Karşılaştırılabilirlik bakımından aşağıdakilerden hangisi doğrudur?",
  "Kullanıcıların kalemler arasındaki benzerlik ve farklılıkları görebilmesini sağlayan destekleyici özelliktir",
  ["Tüm işletmelerin aynı muhasebe politikasını kullanmasını zorunlu kılan bir tekdüzelik kuralıdır",
   "Bilginin kullanıcıların kararlarında fark yaratmasını sağlayan temel niteliksel özelliktir",
   "Bilginin tam, tarafsız ve hatasız olmasını gerektiren gerçeğe uygun sunum unsurudur",
   "Karşılaştırılabilirlik, bilginin yalnızca aynı işletmenin cari dönemi için sunulmasını ifade eder"],
  "Kavramsal Çerçeve: karşılaştırılabilirlik destekleyici bir niteliksel özelliktir; kullanıcıların kalemler arasındaki benzerlik ve farklılıkları belirlemesini sağlar. Tekdüzelik değildir; farklı şeyler farklı gösterilmelidir.",
  "Kavramsal Çerçeve (2018) - karşılaştırılabilirlik")

q("Doğrulanabilirlik bakımından aşağıdakilerden hangisi doğrudur?",
  "Bilgili ve bağımsız gözlemcilerin, sunumun gerçeğe uygun olduğu konusunda görüş birliğine varabilmesidir",
  ["Bilginin yalnızca işletme yönetimi tarafından onaylanmasını ifade eden bir iç kontrol ölçütüdür",
   "Bilginin hiçbir dış kaynakla karşılaştırılamamasını ve yalnızca kayıtlara dayanmasını ifade eder",
   "Bilginin karar verme sürecinde fark yaratmasını sağlayan temel niteliksel özelliği ifade eder",
   "Doğrulanabilirlik yalnızca denetçilerin görev alanına giren bir kavram olup Çerçeve'de yer almaz"],
  "Kavramsal Çerçeve: doğrulanabilirlik, bilgili ve bağımsız farklı gözlemcilerin belirli bir sunumun gerçeğe uygun olduğu konusunda tam olmasa da görüş birliğine varabilmesidir. Doğrudan veya dolaylı olabilir.",
  "Kavramsal Çerçeve (2018) - doğrulanabilirlik")

q("Anlaşılabilirlik bakımından aşağıdakilerden hangisi doğrudur?",
  "Bilginin açık ve öz sunulmasıdır; karmaşık bilgi anlaşılması güç diye rapor dışında bırakılamaz",
  ["Karmaşık bilgiler anlaşılması güç olduğu için finansal raporlardan çıkarılmak zorundadır",
   "Anlaşılabilirlik, raporun hiçbir bilgi birikimi olmayan kişilerce dahi kavranmasını gerektirir",
   "Anlaşılabilirlik temel niteliksel özellik olup ihtiyaca uygunluktan önce gelmektedir",
   "Anlaşılabilirlik yalnızca raporun yazı tipini ve sayfa düzenini ifade eden biçimsel bir ölçüttür"],
  "Kavramsal Çerçeve: anlaşılabilirlik bilginin açık ve öz sunulmasıdır. Bazı olgular doğası gereği karmaşıktır; anlaşılması güç diye rapor dışında bırakılırsa rapor eksik ve yanıltıcı olur. Raporlar, makul bilgiye sahip kullanıcılar için hazırlanır.",
  "Kavramsal Çerçeve (2018) - anlaşılabilirlik")

q("Aşağıdakilerden hangileri finansal bilginin TEMEL niteliksel özelliklerindendir?\n\nI. İhtiyaca uygunluk\n\nII. Karşılaştırılabilirlik\n\nIII. Anlaşılabilirlik",
  "Yalnız I",
  ["I, II ve III", "I ve II", "II ve III", "Yalnız III"],
  "İhtiyaca uygunluk (I) temel niteliksel özelliktir. Karşılaştırılabilirlik (II) ve anlaşılabilirlik (III) ise destekleyici niteliksel özelliklerdir.",
  "Kavramsal Çerçeve (2018) - niteliksel özellikler", onculu=True)

q("Aşağıdakilerden hangileri DESTEKLEYİCİ niteliksel özelliklerdendir?\n\nI. Karşılaştırılabilirlik\n\nII. Doğrulanabilirlik\n\nIII. Zamanında sunum",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Destekleyici niteliksel özellikler; karşılaştırılabilirlik (I), doğrulanabilirlik (II), zamanında sunum (III) ve anlaşılabilirliktir. Üçü de destekleyici özelliktir.",
  "Kavramsal Çerçeve (2018) - destekleyici özellikler", onculu=True)

# ── C. Temel varsayım ve raporlayan işletme (6) ────────────────────────────
q("İşletmenin sürekliliği varsayımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal tablolar, işletmenin faaliyetlerini öngörülebilir gelecekte sürdüreceği varsayımıyla hazırlanır",
  ["Finansal tablolar her hâlde işletmenin yakın gelecekte tasfiye edileceği varsayımıyla hazırlanır",
   "Süreklilik varsayımı yalnızca büyük ölçekli işletmeleri bağlar; küçük işletmeler bundan muaftır",
   "Süreklilik varsayımı Kavramsal Çerçeve'de düzenlenmemiş olup yalnızca denetimin konusudur",
   "Süreklilik varsayımı, işletmenin gelecekte kâr edeceğinin garanti edildiği anlamına gelmektedir"],
  "Kavramsal Çerçeve: finansal tablolar normalde işletmenin sürekliliği varsayımıyla, yani faaliyetlerini öngörülebilir gelecekte sürdüreceği varsayımıyla hazırlanır. Bu niyet veya zorunluluk yoksa farklı esas uygulanır ve açıklanır.",
  "Kavramsal Çerçeve (2018) - süreklilik")

q("Raporlayan işletme kavramı bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal tablo hazırlaması gereken veya hazırlamayı tercih eden işletmedir; tüzel kişi olması şart değildir",
  ["Raporlayan işletme her hâlde tek bir tüzel kişilik olmak zorunda olup başka biçimde olamaz",
   "Raporlayan işletme yalnızca ana ortaklık olabilir; bağlı ortaklıklar raporlayan işletme sayılmaz",
   "Raporlayan işletme kavramı yalnızca vergi mevzuatının konusu olup Çerçeve'de yer almamaktadır",
   "Raporlayan işletme yalnızca borsada işlem gören şirketleri kapsayan dar bir kavram niteliğindedir"],
  "Kavramsal Çerçeve (2018): raporlayan işletme, finansal tablo hazırlaması gereken ya da hazırlamayı tercih eden işletmedir. Tek bir tüzel kişi olabileceği gibi bir kısmı ya da birden fazla işletmeden oluşan bir yapı da olabilir.",
  "Kavramsal Çerçeve (2018) - raporlayan işletme")

q("Konsolide ve bireysel finansal tablolar bakımından aşağıdakilerden hangisi doğrudur?",
  "Konsolide tablolar ana ortaklık ve bağlı ortaklıklarını tek bir raporlayan işletme olarak sunar",
  ["Konsolide tablolar yalnızca ana ortaklığın kendi verilerini sunar; bağlı ortaklıklar dâhil edilmez",
   "Bireysel tablolar ana ortaklık ve bağlı ortaklıkların verilerini birleştirerek sunmaktadır",
   "Konsolide ve bireysel tablolar arasında kapsam bakımından hiçbir fark bulunmamaktadır",
   "Konsolide tablo düzenlenmesi Kavramsal Çerçeve'de yasaklanmış bir uygulama niteliğindedir"],
  "Kavramsal Çerçeve: raporlayan işletme ana ortaklık ve bağlı ortaklıklarından oluşuyorsa hazırlanan tablolar konsolide finansal tablolardır; yalnız ana ortaklığın kendisinden oluşuyorsa bireysel finansal tablolardır.",
  "Kavramsal Çerçeve (2018) - konsolide/bireysel")

q("Finansal tabloların hazırlanma dönemi bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal tablolar belirli bir döneme ilişkin hazırlanır ve karşılaştırmalı bilgi sunar",
  ["Finansal tablolar dönem kavramı olmaksızın işletmenin tüm ömrü için tek seferde hazırlanır",
   "Finansal tablolarda yalnızca cari dönem verisi sunulur; karşılaştırmalı bilgi hiç verilmez",
   "Finansal tabloların dönemi her işletme tarafından her yıl serbestçe değiştirilmek zorundadır",
   "Finansal tablolar yalnızca gelecek dönemlere ilişkin tahminleri gösteren belgelerdir"],
  "Kavramsal Çerçeve: finansal tablolar belirli bir döneme (raporlama dönemi) ilişkin hazırlanır ve en az bir önceki döneme ait karşılaştırmalı bilgi sunar.",
  "Kavramsal Çerçeve (2018) - raporlama dönemi")

q("Finansal tablolarda gelecek dönem bilgisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Kullanıcılara yararlı olması hâlinde geleceğe yönelik bilgiye yer verilebilir; ancak tablolar geçmiş işlemleri esas alır",
  ["Finansal tablolarda geleceğe ilişkin hiçbir bilgiye hiçbir hâlde yer verilmesi mümkün değildir",
   "Finansal tablolar yalnızca gelecek tahminlerinden oluşur; geçmiş işlemler hiç raporlanmamaktadır",
   "Geleceğe yönelik bilgi verilmesi hâlinde finansal tablolar kendiliğinden geçersiz sayılmaktadır",
   "Finansal tablolarda gelecek bilgisi yalnızca vergi idaresinin izniyle sunulabilmektedir"],
  "Kavramsal Çerçeve: finansal tablolar raporlama dönemindeki işlem ve olayları esas alır; ancak kullanıcılara yararlı olacaksa gelecekteki olası işlemlere ilişkin bilgiye de yer verilebilir.",
  "Kavramsal Çerçeve (2018) - geleceğe yönelik bilgi")

q("Aşağıdakilerden hangileri finansal tabloların hazırlanmasına ilişkin doğru ifadelerdendir?\n\nI. Süreklilik varsayımıyla hazırlanır\n\nII. Belirli bir döneme ilişkin hazırlanır\n\nIII. Raporlayan işletmenin tüzel kişi olması zorunludur",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Tablolar süreklilik varsayımıyla (I) ve belirli bir döneme ilişkin (II) hazırlanır. Raporlayan işletmenin tüzel kişi olması zorunlu değildir; bir işletmenin bir kısmı da raporlayan işletme olabilir, bu nedenle III yanlıştır.",
  "Kavramsal Çerçeve (2018) - finansal tablolar", onculu=True)

# ── D. Finansal tablo unsurları (16) ───────────────────────────────────────
q("Kavramsal Çerçeve'ye göre varlık tanımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Geçmiş olaylar sonucunda işletme tarafından kontrol edilen mevcut ekonomik kaynaktır",
  ["Gelecekte edinilmesi planlanan ve henüz işletmenin kontrolüne girmemiş olan her türlü kaynaktır",
   "İşletmenin gelecekte ödemekle yükümlü olduğu ve kaynak çıkışı doğuracak mevcut yükümlülüktür",
   "İşletmenin ortaklarına dağıtacağı kâr payının toplam tutarını gösteren bir özkaynak kalemidir",
   "İşletmenin bir dönemde elde ettiği ve özkaynağı artıran hasılat tutarını ifade eden unsurdur"],
  "Kavramsal Çerçeve (2018): varlık, geçmiş olaylar sonucunda işletme tarafından kontrol edilen mevcut bir ekonomik kaynaktır. Ekonomik kaynak ise ekonomik fayda yaratma potansiyeline sahip bir haktır.",
  "Kavramsal Çerçeve (2018) - varlık tanımı")

q("2018 Kavramsal Çerçevesi'nde ekonomik kaynak bakımından aşağıdakilerden hangisi doğrudur?",
  "Ekonomik fayda yaratma potansiyeline sahip bir haktır; faydanın kesin olması aranmaz",
  ["Ekonomik kaynağın gelecekte kesin olarak fayda sağlaması ve bunun garanti edilmesi gerekmektedir",
   "Ekonomik kaynak yalnızca fiziki varlıkları kapsar; haklar bu kapsamda değerlendirilmemektedir",
   "Ekonomik kaynak, işletmenin gelecekte katlanacağı yükümlülükleri ifade eden bir kavramdır",
   "Ekonomik kaynak kavramı Çerçeve'de tanımlanmamış olup uygulamada kullanılmamaktadır"],
  "Kavramsal Çerçeve (2018): ekonomik kaynak, ekonomik fayda yaratma potansiyeline sahip bir haktır. Potansiyelin kesin olması ya da yüksek olasılıklı olması gerekmez; hakkın mevcut olması yeterlidir.",
  "Kavramsal Çerçeve (2018) - ekonomik kaynak")

q("Kavramsal Çerçeve'ye göre borç tanımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Geçmiş olaylardan kaynaklanan, ekonomik kaynak aktarma yönündeki mevcut yükümlülüktür",
  ["Gelecekte doğması muhtemel olan ve henüz mevcut olmayan her türlü ödeme taahhüdünü ifade eder",
   "Geçmiş olaylar sonucunda işletme tarafından kontrol edilen mevcut ekonomik kaynağı ifade eder",
   "İşletmenin varlıklarından borçları düşüldükten sonra kalan payı gösteren bir kalem niteliğindedir",
   "İşletmenin bir dönemde katlandığı ve özkaynağı azaltan gider tutarını ifade eden unsurdur"],
  "Kavramsal Çerçeve (2018): borç, geçmiş olayların sonucu olarak işletmenin ekonomik kaynak aktarımı yönündeki mevcut yükümlülüğüdür. Yükümlülüğün kaçınılamaz olması ve mevcut olması gerekir.",
  "Kavramsal Çerçeve (2018) - borç tanımı")

q("Özkaynak tanımı bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin varlıklarından tüm borçları düşüldükten sonra kalan payıdır",
  ["İşletmenin sahip olduğu tüm varlıkların toplam tutarını ifade eden bir kalem niteliğindedir",
   "İşletmenin üçüncü kişilere olan tüm borçlarının toplam tutarını gösteren bir unsurdur",
   "İşletmenin bir dönemde elde ettiği hasılatın toplam tutarını ifade eden gelir kalemidir",
   "Özkaynak Çerçeve'de tanımlanmamış olup yalnızca ticaret hukukunun konusunu oluşturur"],
  "Kavramsal Çerçeve: özkaynak, işletmenin tüm borçları düşüldükten sonra varlıkları üzerinde kalan paydır (Varlıklar − Borçlar = Özkaynak).",
  "Kavramsal Çerçeve (2018) - özkaynak")

q("Gelir tanımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Özkaynakta artışa neden olan varlık artışları veya borç azalışlarıdır; ortakların katkıları hariçtir",
  ["Ortakların işletmeye koyduğu sermaye de gelir sayılır ve dönem kârına dâhil edilmektedir",
   "Özkaynakta azalışa neden olan varlık azalışları veya borç artışlarını ifade eden bir unsurdur",
   "Gelir yalnızca nakit tahsil edildiğinde doğar; tahakkuk esasına göre gelir kaydı yapılmaz",
   "Gelir, işletmenin varlıklarından borçları düşüldükten sonra kalan payını ifade etmektedir"],
  "Kavramsal Çerçeve: gelirler, özkaynakta artışa neden olan varlık artışları veya borç azalışlarıdır; ancak ortakların sermaye katkılarından kaynaklananlar gelir sayılmaz.",
  "Kavramsal Çerçeve (2018) - gelir tanımı")

q("Gider tanımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Özkaynakta azalışa neden olan varlık azalışları veya borç artışlarıdır; ortaklara dağıtımlar hariçtir",
  ["Ortaklara dağıtılan kâr payları da gider sayılır ve dönem sonucuna gider olarak yansıtılır",
   "Özkaynakta artışa neden olan varlık artışları veya borç azalışlarını ifade eden bir unsurdur",
   "Gider yalnızca nakit ödendiğinde doğar; tahakkuk esasına göre gider kaydı yapılmamaktadır",
   "Gider, geçmiş olaylar sonucunda işletmece kontrol edilen ekonomik kaynağı ifade etmektedir"],
  "Kavramsal Çerçeve: giderler, özkaynakta azalışa neden olan varlık azalışları veya borç artışlarıdır; ancak ortaklara yapılan dağıtımlardan kaynaklananlar gider sayılmaz.",
  "Kavramsal Çerçeve (2018) - gider tanımı")

q("Varlık tanımında 'kontrol' unsuru bakımından aşağıdakilerden hangisi doğrudur?",
  "Kontrol, ekonomik kaynağın kullanımını yönlendirme ve faydalarını elde etme gücüdür",
  ["Kontrol yalnızca hukuki mülkiyeti ifade eder; mülkiyet yoksa varlık kaydı hiçbir hâlde yapılamaz",
   "Kontrol, işletmenin varlığı fiziken elinde bulundurmasını gerektiren bir zilyetlik ölçütüdür",
   "Kontrol unsuru varlık tanımında yer almaz; yalnızca borç tanımında aranan bir koşuldur",
   "Kontrol, varlığın gelecekte kesin fayda sağlayacağının garanti edilmesi anlamına gelmektedir"],
  "Kavramsal Çerçeve: bir işletme, ekonomik kaynağın kullanımını yönlendirme ve ondan doğabilecek ekonomik faydaları elde etme mevcut gücüne sahipse kaynağı kontrol eder. Hukuki mülkiyet kontrolün tek göstergesi değildir (özün önceliği).",
  "Kavramsal Çerçeve (2018) - kontrol")

q("Borç tanımında 'mevcut yükümlülük' bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin kaynak aktarımından kaçınmak için uygulanabilir bir imkânının bulunmaması gerekir",
  ["İşletmenin gelecekte doğması muhtemel her taahhüdü mevcut yükümlülük olarak kabul edilmektedir",
   "Mevcut yükümlülük yalnızca yazılı sözleşmeden doğabilir; başka hiçbir kaynaktan doğamamaktadır",
   "Mevcut yükümlülük için işletmenin kaynak aktarımından her zaman kaçınabilmesi gerekmektedir",
   "Mevcut yükümlülük kavramı Çerçeve'de tanımlanmamış olup uygulamada kullanılmamaktadır"],
  "Kavramsal Çerçeve (2018): yükümlülüğün mevcut olması için işletmenin ekonomik kaynak aktarımından kaçınmak amacıyla uygulanabilir bir imkânının bulunmaması gerekir. Yükümlülük sözleşmeden, mevzuattan veya zımni kabulden doğabilir.",
  "Kavramsal Çerçeve (2018) - mevcut yükümlülük")

q("İşletme sahiplerinin katkı ve dağıtımları bakımından aşağıdakilerden hangisi doğrudur?",
  "Ortakların sermaye katkıları gelir, ortaklara yapılan dağıtımlar ise gider sayılmaz",
  ["Ortakların sermaye katkıları gelir, ortaklara yapılan dağıtımlar ise gider olarak kaydedilir",
   "Ortakların sermaye katkıları borç olarak sınıflandırılır ve yabancı kaynaklarda gösterilir",
   "Ortaklara yapılan dağıtımlar işletmenin varlıklarını artıran bir gelir unsuru niteliğindedir",
   "Ortakların katkı ve dağıtımları finansal tablolara hiçbir biçimde yansıtılmamaktadır"],
  "Kavramsal Çerçeve: gelir ve gider tanımları ortakların katkılarını ve ortaklara yapılan dağıtımları kapsam dışında bırakır. Bunlar özkaynak hareketidir; kâr veya zarara yansıtılmaz.",
  "Kavramsal Çerçeve (2018) - ortak işlemleri")

q("Bir işletme, kiraladığı bir binayı sözleşme süresince kullanma hakkına sahiptir ancak binanın hukuki maliki değildir. Kavramsal Çerçeve bakımından aşağıdakilerden hangisi doğrudur?",
  "Kullanım hakkı ekonomik kaynak niteliği taşıyabilir; hukuki mülkiyet varlık tanımı için zorunlu değildir",
  ["Hukuki mülkiyet bulunmadığı için hiçbir varlık kaydı yapılması mümkün değildir",
   "Kullanım hakkı her hâlde borç olarak sınıflandırılır; varlık kaydı söz konusu olamamaktadır",
   "Kiralanan varlık her hâlde kiraya verenin ve kiracının tablolarında birlikte gösterilmektedir",
   "Kullanım hakkı yalnızca ortakların katkısı sayılır ve doğrudan özkaynakta gösterilmektedir"],
  "Kavramsal Çerçeve: varlık, kontrol edilen ekonomik kaynaktır ve ekonomik kaynak bir haktır. Bir varlığı kullanma hakkı da ekonomik kaynak olabilir; hukuki mülkiyet varlık tanımının zorunlu unsuru değildir (özün önceliği).",
  "Kavramsal Çerçeve (2018) - varlık tanımı (senaryo)")

q("Finansal tablolara alma (muhasebeleştirme) ölçütleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Unsur tanımını karşılayan kalem, ihtiyaca uygun ve gerçeğe uygun bilgi sağlıyorsa finansal tablolara alınır",
  ["Unsur tanımını karşılayan her kalem, başka hiçbir ölçüt aranmaksızın her hâlde tablolara alınır",
   "Finansal tablolara alma için yalnızca nakit tahsilat veya ödeme yapılmış olması gerekmektedir",
   "Finansal tablolara alma ölçütü yalnızca fayda elde edilmesinin kesin olmasını gerektirmektedir",
   "Finansal tablolara alma yalnızca vergi idaresinin onayına bağlı olarak gerçekleşebilmektedir"],
  "Kavramsal Çerçeve (2018): bir kalem yalnızca unsur tanımını karşılıyorsa ve finansal tablolara alınması kullanıcılara ihtiyaca uygun ile gerçeğe uygun şekilde sunulmuş bilgi sağlıyorsa tablolara alınır.",
  "Kavramsal Çerçeve (2018) - finansal tablolara alma")

q("Finansal tablo dışı bırakma bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme varlık üzerindeki kontrolünü ya da borca ilişkin mevcut yükümlülüğünü kaybettiğinde tablo dışı bırakılır",
  ["Bir varlık, kontrol devam etse dahi işletmenin isteğine bağlı olarak istenildiği zaman çıkarılabilir",
   "Finansal tablo dışı bırakma diye bir kavram bulunmayıp kalemler süresiz olarak tabloda kalır",
   "Bir borç, yükümlülük devam ederken dahi tablolardan serbestçe çıkarılabilmektedir",
   "Tablo dışı bırakma yalnızca vergi idaresinin talebi üzerine ve onun kararıyla yapılabilir"],
  "Kavramsal Çerçeve (2018): tablo dışı bırakma, işletmenin varlık üzerindeki kontrolünün tamamını veya bir kısmını kaybettiğinde; borç için ise mevcut yükümlülüğünün tamamı ya da bir kısmı ortadan kalktığında gerçekleşir.",
  "Kavramsal Çerçeve (2018) - tablo dışı bırakma")

q("Aşağıdakilerden hangileri Kavramsal Çerçeve'ye göre finansal durum tablosu (bilanço) unsurlarındandır?\n\nI. Varlık\n\nII. Borç\n\nIII. Özkaynak",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Finansal durum ile ilgili unsurlar varlık (I), borç (II) ve özkaynaktır (III). Gelir ve giderler ise finansal performansla ilgili unsurlardır. Üçü de doğrudur.",
  "Kavramsal Çerçeve (2018) - unsurlar", onculu=True)

q("Aşağıdaki ifadelerden hangileri Kavramsal Çerçeve'nin varlık tanımına uygundur?\n\nI. Geçmiş olaylardan kaynaklanır\n\nII. İşletme tarafından kontrol edilir\n\nIII. İşletmenin hukuki maliki olması zorunludur",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Varlık geçmiş olaylardan kaynaklanır (I) ve işletmece kontrol edilir (II). Hukuki mülkiyet ise zorunlu değildir; kullanım hakkı da kontrol edilen ekonomik kaynak olabilir. Bu nedenle III yanlıştır.",
  "Kavramsal Çerçeve (2018) - varlık tanımı", onculu=True)

q("Aşağıdaki ifadelerden hangileri gelir ve gider tanımlarına uygundur?\n\nI. Gelir özkaynakta artışa neden olur\n\nII. Gider özkaynakta azalışa neden olur\n\nIII. Ortaklara dağıtılan kâr payı gider sayılır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Gelir özkaynakta artışa (I), gider ise azalışa (II) neden olur. Ancak ortaklara yapılan dağıtımlar gider tanımının dışında bırakılmıştır; bu nedenle III yanlıştır.",
  "Kavramsal Çerçeve (2018) - gelir/gider", onculu=True)

q("Bir işletme, henüz sipariş vermediği ancak gelecek yıl satın almayı planladığı bir makineyi finansal tablolarına almak istemektedir. Aşağıdakilerden hangisi doğrudur?",
  "Geçmiş bir olay ve mevcut kontrol bulunmadığından varlık tanımı karşılanmaz; tablolara alınamaz",
  ["Gelecekte edinilmesi planlanan varlıklar da her hâlde finansal tablolara alınmak zorundadır",
   "Planlanan alım her hâlde borç olarak kaydedilir ve yabancı kaynaklarda gösterilmektedir",
   "Planlanan alım doğrudan özkaynakta gösterilir; varlık veya borç kaydı yapılmamaktadır",
   "Planlanan alım gelir olarak kaydedilir ve dönem kârını artıran bir unsur olarak raporlanır"],
  "Kavramsal Çerçeve: varlık, geçmiş olaylar sonucunda kontrol edilen mevcut ekonomik kaynaktır. Henüz gerçekleşmemiş bir alım planında geçmiş olay ve mevcut kontrol bulunmadığından varlık tanımı karşılanmaz.",
  "Kavramsal Çerçeve (2018) - varlık tanımı (senaryo)")

# ── E. Ölçüm (10) ──────────────────────────────────────────────────────────
q("Kavramsal Çerçeve'ye göre ölçüm esasları bakımından aşağıdakilerden hangisi doğrudur?",
  "Ölçüm esasları tarihi maliyet ve cari değer olmak üzere iki ana grupta ele alınır",
  ["Tek bir ölçüm esası bulunmakta olup tüm varlık ve borçlar yalnızca tarihi maliyetle ölçülmektedir",
   "Ölçüm esasları Çerçeve'de düzenlenmemiş olup her işletme kendi ölçüsünü serbestçe belirlemektedir",
   "Ölçüm yalnızca nominal değer üzerinden yapılır; başka hiçbir ölçüm esası kabul edilmemektedir",
   "Ölçüm esası her hâlde varlığın vergi mevzuatındaki değerine göre belirlenmek zorundadır"],
  "Kavramsal Çerçeve (2018): ölçüm esasları tarihi maliyet ve cari değer olarak iki grupta ele alınır. Cari değer; gerçeğe uygun değer, kullanım değeri (borçlarda yerine getirme değeri) ve cari maliyeti kapsar.",
  "Kavramsal Çerçeve (2018) - ölçüm esasları")

q("Tarihi maliyet esası bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlığın edinilmesi sırasında katlanılan maliyeti esas alır ve fiyat değişimlerini yansıtmaz",
  ["Varlığın raporlama tarihindeki güncel piyasa değerini esas alan bir ölçüm yöntemidir",
   "Varlığın gelecekte sağlayacağı nakit akışlarının bugünkü değerini esas alan bir ölçümdür",
   "Varlığın benzerinin bugün edinilmesi için gereken bedeli esas alan bir cari maliyet ölçümüdür",
   "Tarihi maliyet 2018 Çerçevesi'nde tümüyle kaldırılmış olup artık hiç kullanılmamaktadır"],
  "Kavramsal Çerçeve: tarihi maliyet, varlığın edinilmesi veya borcun üstlenilmesi sırasında katlanılan maliyeti (işlem maliyetleri dâhil) esas alır; sonraki fiyat değişimlerini yansıtmaz, ancak itfa ve değer düşüklüğü için güncellenir.",
  "Kavramsal Çerçeve (2018) - tarihi maliyet")

q("Gerçeğe uygun değer bakımından aşağıdakilerden hangisi doğrudur?",
  "Piyasa katılımcıları arasındaki olağan bir işlemde varlığın satışından elde edilecek veya borcun devrinde ödenecek fiyattır",
  ["Varlığın işletme tarafından edinilmesi sırasında fiilen katlanılan tarihi maliyeti ifade eder",
   "Varlığın işletmeye özgü koşullarda sağlayacağı nakit akışlarının bugünkü değerini gösterir",
   "Varlığın muhasebe kayıtlarındaki defter değerini ifade eden ve değişmeyen bir tutardır",
   "Gerçeğe uygun değer yalnızca vergi mevzuatının konusu olup Çerçeve'de yer almamaktadır"],
  "Kavramsal Çerçeve: gerçeğe uygun değer, ölçüm tarihinde piyasa katılımcıları arasındaki olağan bir işlemde bir varlığın satışından elde edilecek veya bir borcun devrinde ödenecek fiyattır. İşletmeye özgü değil, piyasa bakış açısını yansıtır.",
  "Kavramsal Çerçeve (2018) - gerçeğe uygun değer")

q("Kullanım değeri bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlığın kullanımından ve elden çıkarılmasından işletmenin elde etmeyi beklediği nakit akışlarının bugünkü değeridir",
  ["Piyasa katılımcıları arasındaki olağan işlemde oluşacak fiyatı gösteren piyasa temelli bir ölçümdür",
   "Varlığın edinilmesi sırasında fiilen katlanılan maliyeti gösteren tarihi bir ölçüm esasıdır",
   "Varlığın benzerinin bugün edinilmesi için ödenecek bedeli gösteren cari maliyet ölçümüdür",
   "Kullanım değeri yalnızca borçlar için hesaplanır; varlıklarda hiçbir hâlde kullanılmamaktadır"],
  "Kavramsal Çerçeve: kullanım değeri, bir varlığın kullanımından ve nihai olarak elden çıkarılmasından işletmenin elde etmeyi beklediği nakit akışlarının bugünkü değeridir. İşletmeye özgü varsayımları yansıtır (borçlarda karşılığı yerine getirme değeridir).",
  "Kavramsal Çerçeve (2018) - kullanım değeri")

q("Cari maliyet bakımından aşağıdakilerden hangisi doğrudur?",
  "Ölçüm tarihinde eşdeğer bir varlığın edinilmesi için ödenecek bedeli yansıtır",
  ["Varlığın geçmişte edinilmesi sırasında fiilen ödenen bedeli yansıtan tarihi bir ölçümdür",
   "Varlığın satışından elde edilecek fiyatı yansıtan bir çıkış değeri ölçümü niteliğindedir",
   "Varlığın işletmeye özgü kullanımından beklenen nakit akışlarının bugünkü değerini gösterir",
   "Cari maliyet Çerçeve'de tanımlanmamış olup uygulamada hiç kullanılmayan bir kavramdır"],
  "Kavramsal Çerçeve: cari maliyet, ölçüm tarihinde eşdeğer bir varlığın edinilmesi için ödenecek bedeli (işlem maliyetleri dâhil) yansıtan bir giriş değeridir; gerçeğe uygun değer ise çıkış değeridir.",
  "Kavramsal Çerçeve (2018) - cari maliyet")

q("Ölçüm esasının seçilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Ölçüm esası seçilirken bilginin ihtiyaca uygunluğu ve gerçeğe uygun sunumu ile maliyet kısıtı dikkate alınır",
  ["Ölçüm esası her hâlde tarihi maliyet olarak seçilmek zorunda olup başka seçenek bulunmamaktadır",
   "Ölçüm esası işletmenin kârını en yüksek gösterecek biçimde serbestçe seçilebilmektedir",
   "Ölçüm esasının seçiminde hiçbir ölçüt bulunmayıp konu tümüyle rastlantıya bırakılmıştır",
   "Ölçüm esası yalnızca vergi idaresince belirlenir; işletmenin bu konuda hiçbir rolü yoktur"],
  "Kavramsal Çerçeve: ölçüm esası seçilirken sağlanacak bilginin niteliksel özellikleri (ihtiyaca uygunluk, gerçeğe uygun sunum) ile maliyet kısıtı birlikte değerlendirilir.",
  "Kavramsal Çerçeve (2018) - ölçüm esasının seçimi")

q("Aşağıdakilerden hangileri cari değer ölçüm esasları arasında yer alır?\n\nI. Gerçeğe uygun değer\n\nII. Kullanım değeri\n\nIII. Cari maliyet",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Cari değer ölçüm esasları; gerçeğe uygun değer (I), kullanım değeri/yerine getirme değeri (II) ve cari maliyeti (III) kapsar. Tarihi maliyet ise ayrı bir ölçüm esasıdır. Üçü de cari değer kapsamındadır.",
  "Kavramsal Çerçeve (2018) - cari değer", onculu=True)

q("Gerçeğe uygun değer ile kullanım değeri arasındaki fark bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçeğe uygun değer piyasa katılımcılarının bakış açısını, kullanım değeri ise işletmeye özgü varsayımları yansıtır",
  ["Gerçeğe uygun değer işletmeye özgü varsayımları, kullanım değeri ise piyasa bakışını yansıtmaktadır",
   "İkisi arasında hiçbir fark bulunmayıp aynı tutarı ifade eden eş anlamlı kavramlar niteliğindedir",
   "Gerçeğe uygun değer geçmiş maliyeti, kullanım değeri ise gelecekteki satış fiyatını göstermektedir",
   "İkisi de tarihi maliyet esasının alt türü olup cari değerle hiçbir ilgileri bulunmamaktadır"],
  "Kavramsal Çerçeve: gerçeğe uygun değer piyasa katılımcılarının bakış açısını yansıtan piyasa temelli bir ölçümdür; kullanım değeri ise işletmenin kendi beklenti ve varsayımlarını yansıtan işletmeye özgü bir ölçümdür.",
  "Kavramsal Çerçeve (2018) - GUD/kullanım değeri farkı")

q("Ölçümde maliyet kısıtı bakımından aşağıdakilerden hangisi doğrudur?",
  "Bilgi sağlamanın maliyeti, sağlanan faydayı aşmamalıdır",
  ["Bilgi sağlamanın maliyeti hiçbir biçimde dikkate alınmaz; her bilgi her hâlde üretilmek zorundadır",
   "Maliyet kısıtı yalnızca küçük işletmeler için geçerli olup büyük işletmeleri hiç bağlamamaktadır",
   "Maliyet kısıtı, işletmenin üretim maliyetlerini düşürmesini gerektiren bir verimlilik ölçütüdür",
   "Maliyet kısıtı Çerçeve'de yer almayan ve uygulamada hiç dikkate alınmayan bir kavramdır"],
  "Kavramsal Çerçeve: maliyet, finansal raporlamada sunulabilecek bilgi üzerinde yaygın bir kısıttır. Bilgi sağlamanın maliyeti, o bilginin sağlayacağı faydayla dengelenmelidir.",
  "Kavramsal Çerçeve (2018) - maliyet kısıtı")

q("Aşağıdaki ifadelerden hangileri ölçüm bakımından doğrudur?\n\nI. Tarihi maliyet, edinme sırasındaki maliyeti esas alır\n\nII. Gerçeğe uygun değer piyasa temelli bir ölçümdür\n\nIII. Çerçeve tüm varlıklar için tek bir ölçüm esasını zorunlu kılar",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Tarihi maliyet edinme maliyetini esas alır (I) ve gerçeğe uygun değer piyasa temellidir (II). Çerçeve tek bir ölçüm esasını zorunlu kılmaz; farklı esaslar farklı kalemler için uygun olabilir, bu nedenle III yanlıştır.",
  "Kavramsal Çerçeve (2018) - ölçüm", onculu=True)

# ── F. Sunum, açıklama ve sermayenin korunması (8) ─────────────────────────
q("Sunum ve açıklama bakımından aşağıdakilerden hangisi doğrudur?",
  "Bilgiler benzer kalemler bir araya getirilerek, farklı kalemler ise ayrıştırılarak sunulur",
  ["Tüm kalemler her hâlde tek bir toplam hâlinde birleştirilerek sunulmak zorunda tutulmaktadır",
   "Tüm kalemler her hâlde ayrı ayrı sunulur; hiçbir biçimde birleştirme yapılması mümkün değildir",
   "Sunum ve açıklama Çerçeve'de düzenlenmemiş olup yalnızca işletmenin takdirine bırakılmıştır",
   "Sunum yalnızca vergi idaresinin belirlediği formata göre yapılmak zorunda bulunmaktadır"],
  "Kavramsal Çerçeve (2018): etkin sunum ve açıklama için benzer özellikteki kalemler sınıflandırılıp bir araya getirilir (birleştirme), farklı özellikteki kalemler ise ayrıştırılır. Amaç, bilginin anlaşılabilir ve karşılaştırılabilir olmasıdır.",
  "Kavramsal Çerçeve (2018) - sunum ve açıklama")

q("Sınıflandırma bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlık, borç, özkaynak, gelir ve giderler benzer özelliklerine göre sınıflandırılarak sunulur",
  ["Sınıflandırma yapılmaz; tüm kalemler oluş sırasına göre ve ayrım gözetmeksizin listelenir",
   "Sınıflandırma yalnızca gelir ve giderler için yapılır; bilanço kalemleri sınıflandırılmaz",
   "Sınıflandırma her yıl rastgele değiştirilmek zorunda olup tutarlılık aranmamaktadır",
   "Sınıflandırma yalnızca borsada işlem gören şirketler için zorunlu tutulmuş bir uygulamadır"],
  "Kavramsal Çerçeve: sınıflandırma, varlık, borç, özkaynak, gelir ve giderlerin paylaşılan özelliklerine göre ayrılmasıdır; farklı özellikteki kalemlerin birlikte sınıflandırılması bilgiyi gizleyebilir.",
  "Kavramsal Çerçeve (2018) - sınıflandırma")

q("Kâr veya zarar ile diğer kapsamlı gelir ayrımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelir ve giderler kural olarak kâr veya zarara dâhil edilir; standartların öngördüğü hâllerde diğer kapsamlı gelirde sunulur",
  ["Tüm gelir ve giderler her hâlde diğer kapsamlı gelirde sunulur; kâr veya zarar tablosu kullanılmaz",
   "Kâr veya zarar ile diğer kapsamlı gelir arasında hiçbir fark bulunmayıp ikisi aynı kavramdır",
   "Diğer kapsamlı gelir kavramı Çerçeve'de yer almayan ve uygulanmayan bir kavram niteliğindedir",
   "Gelir ve giderlerin hangi bölümde sunulacağı işletmenin serbest tercihine bırakılmış durumdadır"],
  "Kavramsal Çerçeve: gelir ve giderler kural olarak kâr veya zarara dâhil edilir. Ancak standartların öngördüğü sınırlı hâllerde (bazı yeniden değerleme farkları gibi) diğer kapsamlı gelirde sunulur.",
  "Kavramsal Çerçeve (2018) - kâr/zarar ve DKG")

q("Mahsup (netleştirme) bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlık ve borçların birbirinden ayrı unsurlar olması nedeniyle mahsup genellikle uygun değildir",
  ["Varlık ve borçlar her hâlde net tutar üzerinden mahsup edilerek gösterilmek zorundadır",
   "Mahsup tümüyle serbest olup işletme dilediği kalemleri netleştirerek sunabilmektedir",
   "Mahsup yalnızca gelir ve giderler için yasaktır; varlık ve borçlar serbestçe netleştirilebilir",
   "Mahsup kavramı Çerçeve'de düzenlenmemiş olup yalnızca vergi mevzuatının konusudur"],
  "Kavramsal Çerçeve: mahsup, işletmenin bir varlık ile bir borcu ayrı unsurlar olmasına rağmen tek bir net tutar olarak sınıflandırmasıdır; farklı kalemleri bir araya getirdiğinden genellikle uygun değildir.",
  "Kavramsal Çerçeve (2018) - mahsup")

q("Sermayenin korunması kavramları bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakdi (finansal) sermayenin korunması ve fiziki sermayenin korunması olmak üzere iki kavram vardır",
  ["Tek bir sermaye koruma kavramı bulunmakta olup yalnızca nakdi sermaye esas alınmaktadır",
   "Sermayenin korunması kavramı Çerçeve'de yer almayan ve uygulanmayan bir kavram niteliğindedir",
   "Sermayenin korunması yalnızca ticaret hukukunun konusu olup muhasebeyle ilgisi bulunmamaktadır",
   "Sermayenin korunması, ortakların sermaye taahhüdünü ödemesini ifade eden hukuki bir kavramdır"],
  "Kavramsal Çerçeve: sermayenin korunmasına ilişkin iki kavram vardır: nakdi (finansal) sermayenin korunması ve fiziki sermayenin korunması. Kâr, ancak dönem başındaki sermaye korunduktan sonra kalan tutardır.",
  "Kavramsal Çerçeve (2018) - sermayenin korunması")

q("Nakdi (finansal) sermayenin korunması bakımından aşağıdakilerden hangisi doğrudur?",
  "Kâr, dönem sonu net varlıkların parasal tutarı dönem başındakini aştığı ölçüde elde edilmiş sayılır",
  ["Kâr, işletmenin fiziki üretim kapasitesi arttığı ölçüde elde edilmiş kabul edilen bir tutardır",
   "Kâr, işletmenin nakit mevcudu arttığı ölçüde ve yalnızca nakit esasına göre hesaplanmaktadır",
   "Nakdi sermayenin korunmasında kâr kavramı bulunmaz; yalnızca hasılat toplamı raporlanır",
   "Nakdi sermayenin korunması yalnızca yabancı para işlemlerinde uygulanan bir yöntemdir"],
  "Kavramsal Çerçeve: nakdi (finansal) sermayenin korunmasında kâr, dönem sonundaki net varlıkların parasal tutarı, ortak işlemleri hariç tutulduktan sonra dönem başındaki tutarı aştığı ölçüde elde edilmiş sayılır.",
  "Kavramsal Çerçeve (2018) - nakdi sermayenin korunması")

q("Fiziki sermayenin korunması bakımından aşağıdakilerden hangisi doğrudur?",
  "Kâr, dönem sonu fiziki üretim kapasitesi dönem başındakini aştığı ölçüde elde edilmiş sayılır",
  ["Kâr, net varlıkların parasal tutarındaki artış ölçüsünde elde edilmiş kabul edilen bir tutardır",
   "Fiziki sermayenin korunmasında kâr kavramı bulunmayıp yalnızca üretim miktarı raporlanır",
   "Fiziki sermayenin korunması yalnızca hizmet işletmelerinde uygulanabilen bir yöntemdir",
   "Fiziki sermayenin korunması Çerçeve'de yer almayan ve uygulanmayan bir kavram niteliğindedir"],
  "Kavramsal Çerçeve: fiziki sermayenin korunmasında kâr, dönem sonundaki fiziki üretim kapasitesi (faaliyet kapasitesi), ortak işlemleri hariç tutulduktan sonra dönem başındakini aştığı ölçüde elde edilmiş sayılır.",
  "Kavramsal Çerçeve (2018) - fiziki sermayenin korunması")

q("Aşağıdaki ifadelerden hangileri sunum ve açıklama bakımından doğrudur?\n\nI. Benzer kalemler bir araya getirilerek sunulur\n\nII. Farklı özellikteki kalemler ayrıştırılır\n\nIII. Varlık ve borçların mahsubu genellikle uygundur",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Benzer kalemler birleştirilir (I) ve farklı kalemler ayrıştırılır (II). Ancak mahsup, ayrı unsurları tek tutara indirdiğinden genellikle uygun değildir; bu nedenle III yanlıştır.",
  "Kavramsal Çerçeve (2018) - sunum", onculu=True)

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
                       "styleRef": "SGS Muhasebe Standartları (Kavramsal Çerçeve; yapısal)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    hepsi = sum(1 for x in onc if x["options"][x["answer"]].strip() == "I, II ve III")
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} hepsi {hepsi} | harf {''.join(x['answer'] for x in out)[:40]}…")
