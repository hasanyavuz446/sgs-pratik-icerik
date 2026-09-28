# -*- coding: utf-8 -*-
"""Muhasebe Denetimi · Denetçi Raporu — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında görüş türleri (Yönetmelik m. 30 ile birlikte) ve rapor unsurları sorulmuştur.

Dayanak (28.09.2026 kontrolü, kgk.gov.tr güncel metinler):
  · BDS 700 (Revize) Finansal Tablolara İlişkin Görüş Oluşturma ve Raporlama
  · BDS 701 Kilit Denetim Konularının Bağımsız Denetçi Raporunda Bildirilmesi (5T: TTK denetimlerinde tüm şirketler)
  · BDS 705 Olumlu Görüş Dışında Bir Görüş Verilmesi; BDS 706 Dikkat Çekilen Hususlar ve Diğer Hususlar
  · BDS 570 İşletmenin Sürekliliği (raporlama); BDS 710 Karşılaştırmalı Bilgiler; BDS 720 Diğer Bilgiler (2T dahil)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_denetci_raporu_2026.json", lesson="denetim", topic="denetci_raporu",
          konu_adi="Denetçi Raporu", seed=2026092848,
          surum="BDS 700 (Revize), 701, 705, 706, 570, 710, 720 güncel metinleri; 28.09.2026 kontrolü")

B700 = "BDS 700 “Finansal Tablolara İlişkin Görüş Oluşturma ve Raporlama”ya göre"
B701 = "BDS 701 “Kilit Denetim Konularının Bağımsız Denetçi Raporunda Bildirilmesi”ne göre"
B705 = "BDS 705 “Bağımsız Denetçi Raporunda Olumlu Görüş Dışında Bir Görüş Verilmesi”ne göre"
B706 = "BDS 706 “Dikkat Çekilen Hususlar ve Diğer Hususlar Paragrafları”na göre"
B570 = "BDS 570 “İşletmenin Sürekliliği”ne göre"
B710 = "BDS 710 “Karşılaştırmalı Bilgiler”e göre"
B720 = "BDS 720 “Bağımsız Denetçinin Diğer Bilgilere İlişkin Sorumlulukları”na göre"

# ================================================================ BDS 700
P.q("BDS 700 prg. 11",
    f"{B700}, denetçinin makul güvence elde edip etmediğine ilişkin sonuca varırken dikkate aldığı hususlar arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Denetim ücretinin işletmeden zamanında tahsil edilip edilmediği",
    ["Yeterli ve uygun denetim kanıtının elde edilip edilmediğine ilişkin BDS 330 sonucu",
     "Düzeltilmemiş yanlışlıkların önemli olup olmadığına ilişkin BDS 450 sonucu",
     "Tabloların çerçeveye uygun hazırlanıp hazırlanmadığına ilişkin nitel değerlendirmeler",
     "Muhasebe politikalarının ve tahminlerin uygunluğuna ilişkin değerlendirmeler"],
    "BDS 700 prg. 11-13'e göre denetçi; BDS 330 uyarınca yeterli ve uygun kanıta, BDS 450 uyarınca düzeltilmemiş "
    "yanlışlıklara ilişkin sonuçlarını ve politikalar, tahminler, açıklamalar ve yönetimin taraflılığına ilişkin nitel "
    "değerlendirmeleri dikkate alır. Ücret tahsilatı görüşü etkilemez.", zorluk="easy")

P.q("BDS 700 prg. 16-17",
    f"{B700}, aşağıdaki durumlardan hangisinde denetçi olumlu görüş verir?",
    "Tablolar tüm önemli yönleriyle geçerli çerçeveye uygun hazırlanmışsa",
    ["Tablolar önemli yanlışlık içeriyor ancak yönetim bunu dipnotta kabul etmişse",
     "Yeterli ve uygun kanıt elde edilemedi, ancak yönetim yazılı açıklama vermişse",
     "Tablolardaki yanlışlık önemli ancak yaygın değilse",
     "Denetim sırasında kapsam sınırlaması olmuş ve süre dolmuşsa"],
    "BDS 700 prg. 16'ya göre denetçi, tabloların tüm önemli yönleriyle geçerli finansal raporlama çerçevesine uygun "
    "hazırlandığı sonucuna varırsa olumlu görüş verir. Prg. 17'ye göre önemli yanlışlık veya yeterli kanıt elde edilememesi "
    "BDS 705 uyarınca olumlu dışında görüş gerektirir.", zorluk="easy")

P.q("BDS 700 prg. 21-24",
    f"{B700}, bağımsız denetçi raporunun unsurlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Raporun ilk bölümü, yönetimin finansal tablolara ilişkin sorumluluklarını içerir.",
    ["Raporda “Bağımsız Denetçi Raporu” başlığı açıkça yer alır.",
     "Rapor, sözleşmede ya da mevzuatta belirtilen muhataba hitaben düzenlenir.",
     "Raporun ilk bölümü “Görüş” başlığı altında denetçi görüşünü içerir.",
     "Görüş bölümünde denetlenen işletme ve tabloları oluşturan her bir tablonun başlığı belirtilir."],
    "BDS 700 prg. 21-24'e göre raporda “Bağımsız Denetçi Raporu” başlığı yer alır, sözleşme veya mevzuattaki muhataba "
    "hitaben düzenlenir ve ilk bölüm “Görüş” başlığı altında denetçi görüşünü içerir; görüş bölümünde işletme ve tablolar "
    "belirtilir. Yönetimin sorumlulukları daha sonraki bir bölümdedir.")

P.q("BDS 700 prg. 28",
    f"{B700}, denetçi raporunda görüş bölümünü doğrudan izleyen “Görüşün Dayanağı” bölümünde yer alması gerekenler "
    "arasında aşağıdakilerden hangisi yoktur?",
    "Denetim sırasında test edilen tüm hesapların listesi",
    ["Denetimin BDS'lere uygun olarak yürütüldüğüne ilişkin ifade",
     "Denetçinin BDS'ler kapsamındaki sorumluluklarını açıklayan bölüme atıf",
     "Denetçinin etik hükümlere uygun şekilde bağımsız olduğu ve diğer etik sorumlulukları yerine getirdiği",
     "Elde edilen kanıtın görüşe dayanak oluşturmak için yeterli ve uygun olduğuna inanıldığı"],
    "BDS 700 prg. 28'e göre görüşün dayanağı bölümü; denetimin BDS'lere uygun yürütüldüğünü, denetçinin sorumluluklarını "
    "açıklayan bölüme atfı, bağımsızlık ve diğer etik sorumlulukların yerine getirildiğini ve kanıtın görüşe dayanak "
    "oluşturmak için yeterli ve uygun olduğuna inanıldığını içerir.")

P.q("BDS 700 prg. 49",
    f"{B700}, denetçi raporunun tarihine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yeterli ve uygun kanıtın elde edildiği tarihten önce olamaz.",
    ["Rapor tarihi, bilanço tarihiyle aynı gündır.",
     "Rapor tarihi, genel kurulun finansal tabloları onayladığı gün olarak belirlenir.",
     "Rapor tarihi, denetim sözleşmesinin imzalandığı tarihten itibaren otuz gündür.",
     "Rapor tarihi, yönetimin yazılı açıklamasından en az bir ay sonra olmalıdır."],
    "BDS 700 prg. 49'a göre denetçi raporu tarihi, tabloları oluşturan bütün tabloların ve açıklamaların hazırlandığına ve "
    "işletmedeki yetkili kişilerin sorumluluklarını üstlendiğini beyan ettiğine ilişkin kanıtlar dahil görüşe dayanak "
    "yeterli ve uygun kanıtın elde edildiği tarihten önce olamaz.", zorluk="hard")

P.q("BDS 700 prg. 33-34",
    f"{B700}, raporun yönetimin sorumluluklarını açıklayan bölümünde yer alan ifadeler arasında aşağıdakilerden hangisi "
    "bulunmaz?",
    "Yönetimin, denetçinin yaptığı risk değerlendirmesini onayladığı",
    ["Tabloların geçerli çerçeveye uygun hazırlanması ve gerçeğe uygun sunumu yönetimin sorumluluğundadır.",
     "Hata veya hile kaynaklı önemli yanlışlık içermeyen tablolar için gerekli iç kontrol yönetimin sorumluluğundadır.",
     "Uygun hâllerde işletmenin sürekliliğini değerlendirme ve ilgili açıklamaları yapma yönetimin sorumluluğundadır.",
     "Yönetim, işletmeyi tasfiye etme niyeti yoksa işletmenin sürekliliği esasını kullanır."],
    "BDS 700 prg. 33-34'e göre bu bölüm; tabloların çerçeveye uygun hazırlanması, gerekli iç kontrol ve işletmenin "
    "sürekliliğinin değerlendirilmesi ile süreklilik esasının kullanılmasına ilişkin yönetim sorumluluklarını açıklar. "
    "Risk değerlendirmesi denetçiye aittir.")

P.q("BDS 700 prg. 37-40",
    f"{B700}, raporun denetçinin sorumluluklarını açıklayan bölümünde yer alan ifadeler arasında aşağıdakilerden hangisi "
    "bulunmaz?",
    "Denetçinin, tablolarda yanlışlık bulunmadığını garanti ettiği",
    ["Makul güvencenin yüksek düzeyde bir güvence olduğu ancak önemli yanlışlığı tespit edeceğini garanti etmediği",
     "Denetçinin denetim boyunca mesleki muhakeme kullandığı ve mesleki şüpheciliğini sürdürdüğü",
     "Hile kaynaklı yanlışlığı tespit edememe riskinin hata kaynaklı olandan yüksek olduğu",
     "Denetçinin, iç kontrolün etkinliği hakkında görüş bildirmek amacıyla değil, prosedür tasarlamak için iç kontrolü değerlendirdiği"],
    "BDS 700 prg. 37-40'a göre bu bölüm; makul güvencenin yüksek fakat önemli yanlışlıkları tespit etmeyi garanti etmeyen "
    "güvence olduğunu, mesleki muhakeme ve şüpheciliği, hile riskinin daha yüksek olduğunu ve iç kontrolün etkinliği "
    "hakkında görüş verilmediğini açıklar. Yanlışlık bulunmadığı garanti edilmez.")

P.q("BDS 700 prg. 46",
    f"{B700}, denetçi raporunun imzası ve tarihine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Rapor, denetim ekibindeki en kıdemsiz denetçi tarafından imzalanır.",
    ["Borsada işlem gören işletmelerde raporda sorumlu denetçinin adı yer alır.",
     "Rapor imzalanır ve denetçinin adresini içerir.",
     "Rapor tarihi, yeterli ve uygun kanıtın elde edildiği tarihten önce olamaz.",
     "Rapor, denetimi üstlenen denetim şirketi adına imzalanır."],
    "BDS 700 prg. 46-49'a göre borsada işlem gören işletmelerin raporunda sorumlu denetçinin adı yer alır; rapor imzalanır, "
    "faaliyet yeri belirtilir ve tarih yeterli kanıtın elde edildiği tarihten önce olamaz. BDY m. 4 ve 28'e göre rapor, "
    "denetimi üstlenen adına yetkilendirilmiş sorumlu denetçi tarafından imzalanır.")

# ================================================================ BDS 705
P.q("BDS 705 prg. 7-a",
    "Yeterli ve uygun denetim kanıtı elde eden denetçi, stoklarda tabloların bütününü etkilemeyen, önemli ancak yaygın "
    f"olmayan bir değerleme yanlışlığı tespit etmiştir. {B705} denetçi hangi görüşü verir?",
    "Sınırlı olumlu görüş",
    ["Olumlu görüş", "Olumsuz görüş", "Görüş vermekten kaçınma", "Dikkat çekilen hususlarla olumlu görüş"],
    "BDS 705 prg. 7-a'ya göre yeterli ve uygun kanıt elde eden denetçi yanlışlıkların önemli ancak yaygın olmadığı "
    "sonucuna varırsa sınırlı olumlu görüş verir. Önemli ve yaygın ise olumsuz görüş verilir (prg. 8).", zorluk="easy")

P.q("BDS 705 prg. 8",
    "Yeterli ve uygun kanıt elde eden denetçi, işletmenin bağlı ortaklıklarını konsolide etmediğini ve bunun "
    f"tabloların neredeyse tüm kalemlerini etkilediğini tespit etmiştir. {B705} denetçi hangi görüşü verir?",
    "Olumsuz görüş",
    ["Sınırlı olumlu görüş", "Görüş vermekten kaçınma", "Olumlu görüş", "Diğer hususlarla olumlu görüş"],
    "BDS 705 prg. 8'e göre yeterli ve uygun kanıt elde eden denetçi, yanlışlıkların tek başına veya toplu olarak önemli ve "
    "yaygın olduğu sonucuna varırsa olumsuz görüş verir.", zorluk="easy")

P.q("BDS 705 prg. 9",
    "Denetçi, işletmenin muhasebe kayıtlarının büyük bölümünün bir siber saldırıda yok olması nedeniyle birçok önemli "
    f"hesap için yeterli ve uygun kanıt elde edememiştir. {B705} tespit edilemeyen yanlışlıkların muhtemel etkisi önemli "
    "ve yaygın olabilecekse denetçi ne yapar?",
    "Görüş vermekten kaçınır.",
    ["Olumsuz görüş verir.", "Sınırlı olumlu görüş verir.",
     "Olumlu görüş verip sınırlamayı açıklar.",
     "Yazılı açıklamayla olumlu görüş verir."],
    "BDS 705 prg. 9'a göre denetçi görüşüne dayanak yeterli ve uygun kanıt elde edemezse ve tespit edilemeyen "
    "yanlışlıkların muhtemel etkisinin önemli ve yaygın olabileceği sonucuna varırsa görüş vermekten kaçınır.")

P.q("BDS 705 prg. 5",
    f"{B705}, “yaygın” kavramına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yaygın etki, tablolardaki tek bir hesapla sınırlı ve tabloların küçük bir bölümünü oluşturan etkidir.",
    ["Yaygın etkiler tabloların belirli unsurları, hesapları veya kalemleriyle sınırlı değildir.",
     "Belirli unsurlarla sınırlı olsalar bile tabloların önemli bir bölümünü temsil ediyorlarsa yaygındırlar.",
     "Açıklamalarda, kullanıcıların tabloları anlaması açısından temel teşkil eden etkiler yaygındır.",
     "Yaygın kavramı, tespit edilemeyen yanlışlıkların muhtemel etkilerini tanımlamak için de kullanılır."],
    "BDS 705 prg. 5'e göre yaygın etkiler tabloların belirli unsurlarıyla sınırlı değildir; sınırlıysa tabloların önemli "
    "bir bölümünü temsil eder veya açıklamalarda anlama bakımından temel teşkil eder. Kavram, tespit edilemeyen "
    "yanlışlıkların muhtemel etkileri için de kullanılır.")

P.q("BDS 705 prg. 10",
    "Denetçi, her biri için yeterli ve uygun kanıt elde ettiği birden fazla önemli belirsizlikle karşılaşmıştır; ancak "
    f"belirsizliklerin muhtemel etkileşimi ve kümülatif etkisi nedeniyle görüş oluşturamamaktadır. {B705} denetçi ne "
    "yapar?",
    "İstisnai bu durumda görüş vermekten kaçınır.",
    ["Her belirsizlik için kanıt elde edildiğinden olumlu görüş verir.",
     "Belirsizlikleri dikkat çekilen hususlarda açıklayarak olumlu görüş verir.",
     "Belirsizlikler kanıtlandığından olumsuz görüş verir.",
     "Belirsizliklerin en önemlisi için sınırlı olumlu görüş verir."],
    "BDS 705 prg. 10'a göre birden fazla belirsizlik içeren istisnai durumlarda, her birine ilişkin yeterli ve uygun kanıt "
    "elde edilmiş olsa bile, belirsizliklerin muhtemel etkileşimi ve kümülatif etkileri nedeniyle görüş oluşturmak mümkün "
    "değilse denetçi görüş vermekten kaçınır.", zorluk="hard")

P.q("BDS 705 prg. 11-13",
    "Denetim sözleşmesinin kabulünden sonra yönetim, denetçinin önemli bir yurt dışı şubenin kayıtlarını incelemesine "
    f"izin vermeyeceğini bildirmiş ve bunun görüş vermekten kaçınmayı gerektireceği anlaşılmıştır. {B705} denetçinin "
    "yapması gerekenler arasında aşağıdakilerden hangisi yer almaz?",
    "Sınırlamayı yok sayarak olumlu görüş vermek",
    ["Yönetimden sınırlamayı kaldırmasını talep etmek",
     "Yönetim reddederse durumu üst yönetimden sorumlu olanlara bildirmek",
     "Alternatif prosedürlerle yeterli ve uygun kanıt elde edilip edilemeyeceğini belirlemek",
     "Mevzuat izin veriyorsa denetimden çekilmek veya görüş vermekten kaçınmak"],
    "BDS 705 prg. 11-13'e göre sözleşme kabulünden sonra yönetim kapsamı sınırlarsa denetçi sınırlamanın kaldırılmasını "
    "talep eder; reddedilirse üst yönetime bildirir ve alternatif prosedürleri değerlendirir. Kanıt elde edilemez ve etki "
    "önemli ve yaygın olabilirse mevzuat izin veriyorsa çekilir, aksi hâlde görüş vermekten kaçınır.")

P.q("BDS 705 prg. 15",
    f"{B705}, bir bütün olarak finansal tablolara ilişkin olumsuz görüş veya görüş vermekten kaçınma durumunda "
    "aşağıdakilerden hangisi doğrudur?",
    "Aynı raporda tek bir tabloya veya belirli bir kaleme ilişkin olumlu görüşe yer verilmez.",
    ["Olumsuz görüşle birlikte nakit akış tablosuna ayrıca ve bağımsız olarak olumlu görüş verilebilir.",
     "Görüş vermekten kaçınılsa da hasılat hesabına ilişkin olumlu görüş eklenir.",
     "Olumsuz görüş verilen raporda en az bir kaleme olumlu görüş verilmesi gerekir.",
     "Tablolar bütününe olumsuz görüş verilirse bilanço için ayrıca sınırlı görüş verilir."],
    "BDS 705 prg. 15'e göre denetçi tablolar bütününe olumsuz görüş vermeyi veya görüş vermekten kaçınmayı gerekli "
    "görürse, aynı raporda aynı çerçeve bakımından tek bir tabloya veya belirli unsur, hesap ya da kaleme ilişkin olumlu "
    "görüşe yer vermez; bu, bütüne ilişkin görüşle çelişir.", zorluk="hard")

P.q("BDS 705 prg. 16-20",
    f"{B705}, olumlu görüş dışında bir görüş verilmesi hâlinde denetçi raporunun şekline ilişkin aşağıdaki ifadelerden "
    "hangisi yanlıştır?",
    "Görüşün dayanağı bölümü kaldırılır ve görüşün nedeni sadece sözlü olarak yönetime açıklanır.",
    ["Görüş bölümü uygun şekilde “Sınırlı Olumlu Görüş”, “Olumsuz Görüş” veya “Görüş Vermekten Kaçınma” başlığını taşır.",
     "Görüşün dayanağı bölümünün başlığı da görüş türüne göre değiştirilir.",
     "Görüşün değiştirilmesine neden olan husus, dayanak bölümünde açıklanır.",
     "Mümkünse yanlışlığın tablolar üzerindeki parasal etkisi açıklanır."],
    "BDS 705 prg. 16-20'ye göre görüş ve dayanak bölümlerinin başlıkları görüş türüne göre değiştirilir; değiştirmeye neden "
    "olan husus dayanak bölümünde açıklanır ve mümkünse parasal etkisi belirtilir.")

# ================================================================ BDS 701
P.q("BDS 701 prg. 8",
    f"{B701}, “kilit denetim konuları” aşağıdakilerden hangisidir?",
    "Denetçinin muhakemesine göre cari dönem denetiminde en çok önem arz eden konular",
    ["Yönetimin finansal tablolarda en çok vurguladığı konular",
     "Tutarı genel önemliliği aşan tüm hesap bakiyeleri",
     "Denetçinin olumlu dışında görüş vermesine neden olan konuların tamamı ve bunların etkileri",
     "Önceki yıl denetim raporunda dikkat çekilen hususların tamamı"],
    "BDS 701 prg. 8'e göre kilit denetim konuları, denetçinin mesleki muhakemesine göre cari döneme ait finansal tabloların "
    "denetiminde en çok önem arz eden konulardır ve üst yönetimden sorumlu olanlara bildirilen konular arasından seçilir.",
    zorluk="easy")

P.q("BDS 701 prg. 5, 5T",
    f"{B701}, bu standardın uygulama alanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "TTK denetimlerinde denetime tabi tüm şirketlerin tablolarında uygulanır.",
    ["Sadece borsada işlem gören işletmelerde uygulanır; Türkiye'de başka istisna yoktur.",
     "Sadece bankalar ve sigorta şirketlerinin denetiminde uygulanır.",
     "Denetçi görüş vermekten kaçındığında da kilit denetim konularına yer verilir.",
     "Sadece yönetimin talep ettiği denetimlerde kilit denetim konuları bildirilir."],
    "BDS 701 prg. 5'e göre standart borsada işlem gören işletmelerin tam set genel amaçlı tablolarında, denetçinin karar "
    "verdiği ve mevzuatın zorunlu kıldığı durumlarda uygulanır. Türkiye uygulamasına ilişkin prg. 5T'ye göre TTK uyarınca "
    "yapılan denetimlerde tüm şirketlerde uygulanır. BDS 705 görüş vermekten kaçınmada KDK bildirilmesini yasaklar.",
    zorluk="hard")

P.q("BDS 701 prg. 9",
    f"{B701}, denetçinin azami düzeyde dikkat gerektiren konuları belirlerken göz önünde bulundurdukları arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Denetim ekibinin en az zaman harcadığı rutin işlem sınıfları",
    ["Önemli yanlışlık riski daha yüksek değerlendirilen veya ciddi riskli alanlar",
     "Yüksek tahmin belirsizliği içeren muhasebe tahminleri dahil önemli yönetim yargılarının bulunduğu alanlar",
     "Dönem içinde gerçekleşen önemli olay veya işlemlerin denetime etkisi",
     "Önemli denetçi yargıları gerektiren finansal tablo alanları"],
    "BDS 701 prg. 9'a göre denetçi; önemli yanlışlık riski yüksek veya ciddi riskli alanları, yüksek tahmin belirsizliği "
    "dahil önemli yönetim yargılarına ilişkin önemli denetçi yargılarını ve dönemdeki önemli olay veya işlemlerin denetime "
    "etkisini göz önünde bulundurur.")

P.q("BDS 701 prg. 12, 15",
    "Denetçi, işletmenin sürekliliğine ilişkin önemli bir belirsizlik tespit etmiş ve tablolarda yeterli açıklama yapıldığı "
    f"sonucuna varmıştır. {B701} bu hususun raporda sunumuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Nitelik olarak KDK'dır; ayrı süreklilik bölümünde raporlanır, KDK bölümünde atıf yapılır.",
    ["Kilit denetim konuları bölümünde ayrıntılı olarak açıklanır; ayrıca ayrı bir süreklilik bölümü açılmaz.",
     "Diğer hususlar paragrafında açıklanır ve kilit denetim konusu sayılmaz.",
     "Raporda açıklanmaz; sadece üst yönetime sözlü olarak bildirilir.",
     "Sınırlı olumlu görüşün dayanağı bölümünde açıklanır."],
    "BDS 701 prg. 15'e göre olumlu dışında görüşe neden olan konu ile süreklilikle ilgili önemli belirsizlik nitelikleri "
    "itibarıyla kilit denetim konularıdır; ancak KDK bölümünde açıklanmaz, ilgili BDS'ye göre raporlanır ve KDK bölümünde "
    "ilgili bölüme atıf yapılır. BDS 570 prg. 22 ayrı bölüm öngörür.", zorluk="hard")

P.q("BDS 701 prg. 13",
    f"{B701}, raporda yer verilen her bir kilit denetim konusuna ilişkin açıklamada bulunması gerekenler aşağıdakilerden "
    "hangisidir?",
    "Neden kilit konu sayıldığı ve denetimde nasıl ele alındığı",
    ["Konuya ilişkin ayrı bir denetim görüşü ve bu görüşün türü ile gerekçesi",
     "Konunun denetim ücretine etkisi ve harcanan süre",
     "Konuya ilişkin yönetimin ayrı ayrı imzaladığı beyanlar",
     "Konuyu ele alan denetçilerin adları, unvanları ve harcadıkları süre"],
    "BDS 701 prg. 13'e göre her bir kilit denetim konusu açıklaması, varsa tablolardaki ilgili açıklamaya atıf ile konunun "
    "neden kilit denetim konusu olarak belirlendiğini ve denetimde nasıl ele alındığını içerir. KDK'lar için ayrı görüş "
    "verilmez.")

P.q("BDS 701 prg. 14",
    f"{B701}, kilit denetim konusunun raporda bildirilmemesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yönetim talep ederse denetçi herhangi bir kilit denetim konusunu rapordan çıkarabilir.",
    ["Mevzuat konunun kamuya açıklanmasına izin vermiyorsa konu raporda açıklanmaz.",
     "Olumsuz sonuçların kamu yararını aşacağı makul beklenen oldukça istisnai durumlarda açıklanmayabilir.",
     "İşletme konu hakkında kamuya bilgi açıklamışsa istisnai açıklamama hükmü uygulanmaz.",
     "Açıklamama kararı, denetçinin mesleki muhakemesine dayanan istisnai bir karardır."],
    "BDS 701 prg. 14'e göre denetçi her KDK'yı raporda açıklar; mevzuatın izin vermemesi veya olumsuz sonuçların kamu "
    "yararını aşacağının makul beklendiği oldukça istisnai durumlar hariçtir. İşletme konuyu kamuya açıkladıysa bu istisna "
    "uygulanmaz. Yönetimin talebi bir istisna değildir.")

# ================================================================ BDS 706
P.q("BDS 706 prg. 7-b, 8",
    f"{B706}, “Dikkat Çekilen Hususlar” paragrafına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tablolarda uygun sunulan ve anlamada temel önemdeki bir hususa atıf yapar.",
    ["Tablolarda açıklanmayan bir hususu ilk kez kullanıcılara duyurmak için kullanılır.",
     "Olumlu dışında görüş verilmesi gereken durumlarda görüşün yerine kullanılır.",
     "Kilit denetim konusu olarak belirlenen hususların tekrar edildiği bölümdür.",
     "Denetçinin sorumluluklarına ilişkin ek açıklamaların yapıldığı bölümdür."],
    "BDS 706 prg. 7-b'ye göre DÇH paragrafı, kullanıcıların tabloları anlaması açısından temel öneme sahip olan ve "
    "tablolarda uygun şekilde sunulan veya açıklanan bir hususa atıf yapar. Prg. 8'e göre olumlu dışında görüş "
    "gerektirmemeli ve KDK olarak belirlenmemiş olmalıdır.")

P.q("BDS 706 prg. 8",
    f"{B706}, denetçinin raporuna dikkat çekilen hususlar paragrafı ekleyebilmesi için gerekli şartlar arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Hususun yönetim tarafından denetçiye yazılı olarak önerilmiş olması",
    ["Hususun tablolarda sunulmuş veya açıklanmış olması",
     "Hususun BDS 705 uyarınca olumlu dışında görüş gerektirmemesi",
     "BDS 701 uygulanıyorsa hususun kilit denetim konusu olarak belirlenmemiş olması",
     "Hususun kullanıcıların tabloları anlaması açısından temel öneme sahip olması"],
    "BDS 706 prg. 8'e göre DÇH paragrafı; tablolarda sunulan veya açıklanan, anlama açısından temel önemde bir husus "
    "için, olumlu dışında görüş gerektirmemesi ve KDK olarak belirlenmemiş olması şartıyla eklenir. Yönetim önerisi şart "
    "değildir; karar denetçinin muhakemesidir.")

P.q("BDS 706 A5",
    f"{B706}, aşağıdakilerden hangisi dikkat çekilen hususlar paragrafının eklenmesinin gerekli görülebileceği "
    "durumlara örnek değildir?",
    "Tabloların önemli yanlışlık içermesi ve yönetimin düzeltmeyi reddetmesi",
    ["İstisnai bir davanın gelecekteki sonucuna ilişkin belirsizlik",
     "Tablo tarihi ile rapor tarihi arasında gerçekleşen önemli bir sonraki olay",
     "Tablolar üzerinde önemli etkisi olan yeni bir standardın izin verildiği için erken uygulanması",
     "İşletmenin finansal durumunu önemli ölçüde etkileyen ciddi bir afet"],
    "BDS 706 A5 istisnai dava belirsizliği, önemli sonraki olay, yeni standardın erken uygulanması ve ciddi afeti örnek "
    "sayar. Tablolarda önemli yanlışlık bulunması ve düzeltilmemesi ise BDS 705 uyarınca görüşün değiştirilmesini "
    "gerektirir; DÇH paragrafı görüş değişikliğinin yerine geçmez.", zorluk="hard")

P.q("BDS 706 prg. 7-a, 10",
    "Denetçi, önceki yılın tablolarının başka bir denetçi tarafından denetlendiğini raporunda kullanıcılara bildirmek "
    f"istemektedir. Bu bilgi tablolarda yer almamaktadır. {B706} denetçi bu bilgiyi hangi bölümde vermelidir?",
    "Diğer hususlar paragrafında",
    ["Dikkat çekilen hususlar paragrafında", "Görüş bölümünde", "Kilit denetim konuları bölümünde",
     "Yönetimin sorumlulukları bölümünde"],
    "BDS 706 prg. 7-a ve 10'a göre Diğer Hususlar paragrafı, kullanıcıların denetimi, denetçinin sorumluluklarını veya "
    "raporu anlamasıyla ilgili, tablolarda sunulan veya açıklananlar dışındaki bir hususa atıf yapar. Önceki dönemin başka "
    "denetçi tarafından denetlenmesi BDS 710'da bu paragrafa örnektir.", zorluk="easy")

P.q("BDS 706 prg. 9",
    f"{B706}, rapora dikkat çekilen hususlar paragrafı eklendiğinde aşağıdaki ifadelerden hangisi yanlıştır?",
    "Paragraf, denetçinin görüşünü o husus bakımından sınırlandırır.",
    ["Paragraf “Dikkat Çekilen Hususlar” veya uygun başka bir başlık taşıyan ayrı bir bölümde yer alır.",
     "Paragrafta, hususu tam olarak açıklayan tablolardaki ilgili açıklamaya açık bir atıf yapılır.",
     "Paragrafta, denetçinin görüşünün bu husus nedeniyle değiştirilmediği belirtilir.",
     "Paragrafın rapordaki yeri, hususun göreli önemine ilişkin denetçi muhakemesine bağlıdır."],
    "BDS 706 prg. 9'a göre DÇH paragrafı ayrı bir bölümde yer alır, tablolardaki ilgili açıklamaya açıkça atıf yapar ve "
    "görüşün bu husus nedeniyle değiştirilmediğini belirtir. DÇH paragrafı görüşü değiştirmez veya sınırlandırmaz.")

# ================================================================ BDS 570 raporlama
P.q("BDS 570 prg. 22",
    f"{B570}, süreklilik esasının kullanılması uygun olduğu, önemli bir belirsizlik bulunduğu ve tablolarda yeterli açıklama "
    "yapıldığı durumda denetçi raporuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Olumlu görüş verilir ve süreklilikle ilgili önemli belirsizlik başlıklı ayrı bölüm eklenir.",
    ["Sınırlı olumlu görüş verilir ve belirsizlik dayanak bölümünde açıklanır.",
     "Olumsuz görüş verilir, çünkü süreklilik şüphesi tabloları yaygın olarak etkiler.",
     "Görüş vermekten kaçınılır, çünkü belirsizlik sonuçlanmadan görüş oluşturulamaz.",
     "Olumlu görüş verilir ve belirsizlik, dipnotlara atıf yapılmadan diğer hususlar paragrafında açıklanır."],
    "BDS 570 prg. 22'ye göre önemli belirsizliğe ilişkin yeterli açıklama yapılmışsa denetçi olumlu görüş verir ve "
    "“İşletmenin Sürekliliğiyle İlgili Önemli Belirsizlik” başlıklı ayrı bölümde ilgili dipnotlara dikkat çeker ve bu "
    "hususun görüşü değiştirmediğini belirtir.")

P.q("BDS 570 prg. 23",
    "Denetçi, işletmenin sürekliliğine ilişkin önemli bir belirsizlik bulunduğunu, ancak tablolarda bu hususun yeterince "
    f"açıklanmadığını tespit etmiştir. {B570} denetçinin vereceği görüş aşağıdakilerden hangisidir?",
    "Duruma göre sınırlı olumlu görüş veya olumsuz görüş",
    ["Olumlu görüş ve süreklilik bölümü",
     "Olumlu görüş ve dikkat çekilen hususlar paragrafı",
     "Görüş vermekten kaçınma ve diğer hususlar paragrafı",
     "Olumlu görüş ve kilit denetim konuları bölümü"],
    "BDS 570 prg. 23'e göre önemli belirsizlik tablolarda yeterince açıklanmamışsa denetçi BDS 705 uyarınca sınırlı olumlu "
    "veya olumsuz görüşten uygun olanı verir ve dayanak bölümünde önemli belirsizliğin mevcut olduğunu ve yeterince "
    "açıklanmadığını belirtir.", zorluk="hard")

P.q("BDS 570 prg. 21-24",
    f"{B570}, süreklilikle ilgili denetçi raporuna etkilere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yönetim değerlendirmeyi genişletmezse denetçi bunun rapora etkisini değerlendirmez.",
    ["Süreklilik esası kullanılmış ancak uygun değilse denetçi olumsuz görüş verir.",
     "Önemli belirsizlik yeterince açıklanmışsa görüş değişmez, ayrı bir bölüm eklenir.",
     "Önemli belirsizlik yeterince açıklanmamışsa sınırlı olumlu veya olumsuz görüş verilir.",
     "Yeterli açıklama yapılmayan belirsizlik, görüşün dayanağı bölümünde belirtilir."],
    "BDS 570 prg. 21-23 süreklilik esası uygun değilse olumsuz görüşü, yeterli açıklamada ayrı bölümü, yetersiz "
    "açıklamada sınırlı olumlu veya olumsuz görüşü düzenler. Prg. 24'e göre yönetim değerlendirme yapmaya veya genişletmeye "
    "istekli değilse denetçi bunun rapora etkilerini mütalaa eder.")

# ================================================================ BDS 710 ve 720
P.q("BDS 710 prg. 6",
    f"{B710}, önceki dönemlere ait tutar ve açıklamaların cari döneme ait tabloların ayrılmaz parçası olarak yer aldığı ve "
    "sadece cari dönem tutarlarıyla birlikte okunması amaçlanan bilgiler aşağıdakilerden hangisidir?",
    "Karşılık gelen bilgiler",
    ["Karşılaştırmalı finansal tablolar", "Diğer bilgiler", "Ara dönem finansal bilgiler", "Özet finansal tablolar"],
    "BDS 710 prg. 6-c'ye göre karşılık gelen bilgiler, önceki dönem tutar ve açıklamalarının cari dönem tablolarının "
    "ayrılmaz parçası olarak yer aldığı ve sadece cari dönemle birlikte okunması amaçlanan karşılaştırmalı bilgilerdir. "
    "Karşılaştırmalı finansal tablolarda ise denetlenmişse görüş önceki dönemi de kapsar (prg. 6-b).", zorluk="hard")

P.q("BDS 720 prg. 2T",
    f"{B720}, Türkiye uygulamasında yıllık faaliyet raporunun denetimine ilişkin aşağıdakilerden hangisi doğrudur?",
    "TTK çerçevesinde yıllık faaliyet raporu için ayrı bir denetçi raporu düzenlenir.",
    ["Yıllık faaliyet raporu denetçinin finansal tablo görüşünün bir parçası olarak değerlendirilir.",
     "Yıllık faaliyet raporu denetim kapsamında değildir; denetçi sadece okur.",
     "Yıllık faaliyet raporu hakkında görüşü denetim komitesi verir, denetçi imzalar.",
     "Yıllık faaliyet raporu sadece borsada işlem gören şirketlerde denetlenir."],
    "BDS 720 prg. 2T'ye göre diğer bilgilerin denetimi sonucunda TTK çerçevesinde ayrı bir rapor (Yönetim Kurulunun Yıllık "
    "Faaliyet Raporuna İlişkin Denetçi Raporu) düzenlenir; bu raporda faaliyet raporundaki finansal bilgilerin ve "
    "irdelemelerin denetlenen tablolarla ve denetimde elde edilen bilgilerle tutarlı olup olmadığı hakkında görüş "
    "bildirilir. Finansal tablolara ilişkin görüş diğer bilgileri kapsamaz (prg. 2).", zorluk="hard")

P.q("BDS 720 prg. 14",
    f"{B720}, denetçinin diğer bilgileri incelerken yapması gerekenler arasında aşağıdakilerden hangisi yer almaz?",
    "Diğer bilgilerdeki tüm finansal olmayan verileri kaynak belgeleriyle tek tek doğrulamak",
    ["Diğer bilgiler ile tablolar arasında önemli bir tutarsızlık olup olmadığını mütalaa etmek",
     "Tablolardaki tutarlarla aynı olması beklenen seçilmiş tutarları karşılaştırmak",
     "Diğer bilgiler ile denetimde edinilen bilgiler arasında önemli tutarsızlık olup olmadığını mütalaa etmek",
     "Önemli tutarsızlık görünen durumlarda konuyu yönetimle görüşmek"],
    "BDS 720 prg. 14'e göre denetçi diğer bilgileri inceler; tablolarla ve denetimde edinilen bilgilerle önemli tutarsızlık "
    "olup olmadığını mütalaa eder ve seçilmiş tutarları karşılaştırır. Prg. 16 tutarsızlık görünen durumlarda yönetimle "
    "görüşmeyi düzenler. BDS 720, görüş için gerekenden başka kanıt elde edilmesini zorunlu tutmaz (prg. 2).")

# ================================================================ BDY ile birlikte
P.q("BDY m. 30/2, BDS 705",
    f"KGK Bağımsız Denetim Yönetmeliği ve BDS 705’e göre, yeterli ve uygun kanıt elde edilemeyen ancak etkisi denetim "
    "konusunun genelini etkilemeyen bir durumda verilecek görüş aşağıdakilerden hangisidir?",
    "Sınırlı olumlu görüş",
    ["Olumsuz görüş", "Görüş bildirmekten kaçınma", "Olumlu görüş", "Dikkat çekilen hususlar içeren olumlu görüş"],
    "Yönetmelik m. 30/2-b ve BDS 705 prg. 7-b'ye göre yeterli ve uygun kanıt toplanamadığı, ancak bunun denetim "
    "konusunun genelini etkilemediği (yaygın olmadığı) durumlarda sınırlı olumlu görüş verilir.", zorluk="easy")

P.oncul("BDS 705 prg. 7-9",
    f"{B705} aşağıdaki eşleştirmeler değerlendirilmektedir:",
    ["Önemli ve yaygın yanlışlık (yeterli kanıt var) – Olumsuz görüş",
     "Önemli ancak yaygın olmayan yanlışlık (yeterli kanıt var) – Sınırlı olumlu görüş",
     "Kanıt elde edilemeyen, muhtemel etkisi önemli ve yaygın olabilecek husus – Olumsuz görüş",
     "Kanıt elde edilemeyen, muhtemel etkisi önemli ancak yaygın olmayan husus – Sınırlı olumlu görüş"],
    "Yukarıdaki eşleştirmelerden hangileri doğrudur?",
    "I, II ve IV",
    ["I ve II", "II ve III", "I, II ve IV", "I, III ve IV", "II, III ve IV"],
    "BDS 705 prg. 7-9'a göre kanıt varken önemli ve yaygın yanlışlık olumsuz görüş (I), önemli ancak yaygın olmayan "
    "yanlışlık sınırlı olumlu görüş (II) gerektirir. Kanıt elde edilemeyip muhtemel etkisi önemli ve yaygın olabilecekse "
    "görüş vermekten kaçınılır (III yanlış); önemli ancak yaygın değilse sınırlı olumlu görüş verilir (IV).", zorluk="hard")

P.q("BDS 700 prg. 18",
    "Gerçeğe uygun sunum çerçevesine uygun hazırlanan tabloların, çerçevenin gerektirdiği tüm açıklamalar yapılmış olmasına "
    f"rağmen gerçeğe uygun sunum sağlamadığı sonucuna varılmıştır. {B700} denetçinin yapması gereken aşağıdakilerden "
    "hangisidir?",
    "Yönetimle görüşür; çözülmezse görüş değişikliği gerekip gerekmediğine karar verir.",
    ["Çerçeveye uyulduğu için gerçeğe uygun sunumu değerlendirmeden olumlu görüş verir.",
     "Hususu sadece diğer hususlar paragrafında açıklayıp tablolara ilişkin olumlu görüş verir.",
     "Tabloları kendisi düzelterek yayımlatır ve olumlu görüş verir.",
     "Hususu yönetimin sorumluluğunda sayarak rapora yansıtmaz."],
    "BDS 700 prg. 18'e göre gerçeğe uygun sunum çerçevesine göre hazırlanan tablolar gerçeğe uygun sunum sağlamıyorsa "
    "denetçi hususu yönetimle görüşür ve çerçeve hükümlerine ve hususun nasıl çözüldüğüne bağlı olarak BDS 705 uyarınca "
    "görüşün değiştirilmesinin gerekip gerekmediğine karar verir.", zorluk="hard")

# ================================================================ ek sorular
P.q("BDS 700 prg. 25",
    f"{B700}, gerçeğe uygun sunum çerçevesine göre hazırlanan tablolara olumlu görüş verilirken kullanılan ifade "
    "aşağıdakilerden hangisidir?",
    "Tablolar, geçerli çerçeveye uygun olarak tüm önemli yönleriyle gerçeğe uygun biçimde sunulmaktadır.",
    ["Tablolar, denetçinin incelediği tüm işlemler bakımından hatasız olarak sunulmaktadır.",
     "Tablolar, yönetimin beyanlarına göre makul ölçüde doğru olarak sunulmaktadır.",
     "Tablolarda önemli yanlışlık bulunmadığı mutlak olarak garanti edilmektedir.",
     "Tablolar, vergi mevzuatına uygun olarak eksiksiz ve tam olarak düzenlenmiştir."],
    "BDS 700 prg. 25'e göre gerçeğe uygun sunum çerçevesinde olumlu görüş ifadesi, ilişikteki finansal tabloların geçerli "
    "finansal raporlama çerçevesine uygun olarak tüm önemli yönleriyle gerçeğe uygun bir biçimde sunulduğu (veya doğru ve "
    "gerçeğe uygun bir görünüm sağladığı) şeklindedir.", zorluk="easy")

P.q("BDS 700 prg. 12-13",
    f"{B700}, görüş oluşturulurken yapılan nitel değerlendirmelere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yönetimin yargılarındaki taraflılık göstergeleri görüş oluşturulurken dikkate alınmaz.",
    ["Denetçi, muhasebe politikalarının uygun şekilde açıklanıp açıklanmadığını değerlendirir.",
     "Denetçi, yönetimin yaptığı muhasebe tahminlerinin makul olup olmadığını değerlendirir.",
     "Denetçi, tablolarda sunulan bilgilerin ihtiyaca uygun, güvenilir, karşılaştırılabilir ve anlaşılabilir olup olmadığını değerlendirir.",
     "Denetçi, tabloların kullanıcıların önemli işlemlerin etkisini anlamasına imkân veren açıklamalar içerip içermediğini değerlendirir."],
    "BDS 700 prg. 12'ye göre denetçi, yönetimin yargılarındaki olası taraflılık göstergeleri dahil işletmenin muhasebe "
    "uygulamalarının nitel yönlerini değerlendirir; politikaların açıklanması, tahminlerin makullüğü, bilgilerin niteliği "
    "ve açıklamaların yeterliliği bu değerlendirmenin parçasıdır.")

P.q("BDS 700 prg. 46",
    f"{B700}, borsada işlem gören işletmelerin raporlarında sorumlu denetçinin adına ilişkin aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Sorumlu denetçinin adı, kişisel güvenliğe ciddi tehdit oluştursa dahi raporda açıklanır.",
    ["Borsada işlem gören işletmelerin raporunda sorumlu denetçinin adı yer alır.",
     "Kişisel güvenliğe ciddi tehdit bulunan istisnai durumlarda sorumlu denetçinin adı açıklanmayabilir.",
     "Rapor imzalanır ve denetçinin adresini içerir.",
     "Rapor tarihi, görüşe dayanak yeterli ve uygun kanıtın elde edildiği tarihten önce olamaz."],
    "BDS 700 prg. 46'ya göre borsada işlem gören işletmelerin raporunda sorumlu denetçinin adı yer alır; ancak bunun "
    "kişisel güvenliğe ciddi tehdit oluşturacağı istisnai durumlarda ad açıklanmaz. Prg. 47-49 imza, adres ve tarihi "
    "düzenler.", zorluk="hard")

P.q("BDS 700 prg. 43",
    "Denetçi, TTK uyarınca yönetim kurulunun defter tutma ve finansal raporlama düzenine ilişkin ek bildirimlerde "
    f"bulunmakla yükümlüdür. {B700} bu ek raporlama sorumlulukları denetçi raporunda nasıl sunulur?",
    "Ayrı bir “Mevzuattan Kaynaklanan Diğer Yükümlülükler” bölümünde",
    ["Görüş bölümünün içinde, görüşün bir parçası olarak",
     "Dikkat çekilen hususlar paragrafında",
     "Kilit denetim konuları bölümünde",
     "Yönetimin sorumlulukları bölümünde"],
    "BDS 700 prg. 43'e göre denetçi, BDS'ler kapsamındaki sorumluluklarına ek diğer raporlama sorumluluklarına raporunda "
    "yer verirse bunları “Mevzuattan Kaynaklanan Diğer Yükümlülükler” veya içeriğe uygun başka bir başlık altında ayrı bir "
    "bölümde ele alır; prg. 44 aynı bölümde sunulursa açıkça ayırt edilmesini ister.")

P.q("BDS 700 prg. 38",
    f"{B700}, denetçi raporunun denetçinin sorumlulukları bölümünde belirtilen denetçinin amaçları aşağıdakilerden "
    "hangisidir?",
    "Tabloların bütün olarak önemli yanlışlık içerip içermediğine dair makul güvence elde etmek ve görüş içeren rapor düzenlemek",
    ["İşletmenin iç kontrol sisteminin etkinliği hakkında ayrı bir görüş bildirmek ve rapor düzenlemek",
     "Yönetimin iş kararlarının etkinliği ve verimliliği hakkında öneri raporu hazırlamak",
     "İşletmenin vergi yükümlülüklerini eksiksiz yerine getirdiğini tasdik etmek",
     "İşletmenin gelecek dönemlerdeki sürekliliğini garanti ederek yatırımcılara güvence vermek"],
    "BDS 700 prg. 38-a'ya göre raporda denetçinin amaçlarının, tabloların bir bütün olarak hata veya hile kaynaklı önemli "
    "yanlışlık içerip içermediğine ilişkin makul güvence elde etmek ve denetçi görüşünü içeren bir rapor düzenlemek olduğu "
    "belirtilir.")

P.q("BDS 705 prg. 27",
    "Denetçi, stoklara ilişkin kapsam sınırlaması nedeniyle görüş vermekten kaçınmıştır. Bu arada şerefiye değer düşüklüğüne "
    f"ilişkin önemli bir yanlışlığı da tespit etmiştir. {B705} denetçinin bu yanlışlığa ilişkin yapması gereken "
    "aşağıdakilerden hangisidir?",
    "Bu yanlışlığın sebep ve etkilerini de görüşün dayanağı bölümünde açıklar.",
    ["Görüş vermekten kaçınıldığı için bu yanlışlığı raporda açıklamaz.",
     "Bu yanlışlık için ayrıca olumsuz görüş verir ve iki görüşü birlikte sunar.",
     "Yanlışlığı sadece yönetime bildirir, raporda yer vermez.",
     "Yanlışlığı kilit denetim konuları bölümünde açıklar."],
    "BDS 705 prg. 27'ye göre denetçi, olumsuz görüş vermiş veya görüş vermekten kaçınmış olsa dahi, haberdar olduğu ve "
    "olumlu dışında görüş gerektirecek diğer hususların sebep ve etkilerini görüşün dayanağı bölümünde açıklar. Prg. 29'a "
    "göre görüş vermekten kaçınmada KDK bölümüne yer verilmez.", zorluk="hard")

P.q("BDS 705 prg. 29",
    f"{B705}, görüş vermekten kaçınılan bir denetim raporuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Görüş vermekten kaçınıldığında da kilit denetim konuları bölümü rapora eklenir.",
    ["Mevzuatla aksi öngörülmedikçe Diğer Bilgiler bölümüne yer verilmez.",
     "Dayanak bölümünün başlığı “Görüş Vermekten Kaçınmanın Dayanağı” şeklinde olur.",
     "Kanıtın görüşe yeterli ve uygun dayanak oluşturduğuna ilişkin ifadeye yer verilmez.",
     "Denetçinin sorumluluklarının açıklandığı bölüm değiştirilerek sınırlı olarak sunulur."],
    "BDS 705 prg. 29'a göre görüş vermekten kaçınıldığında, mevzuatla aksi öngörülmedikçe raporda KDK bölümü ya da Diğer "
    "Bilgiler bölümü yer almaz. Prg. 20 ve 26 dayanak başlığını ve kaldırılan ifadeleri, prg. 28 sorumluluklar bölümünün "
    "değiştirilmesini düzenler.")

P.q("BDS 705 prg. 30",
    f"{B705}, raporunda olumlu dışında görüş vermeyi düşünen denetçinin üst yönetimden sorumlu olanlarla iletişimine "
    "ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bu görüşü gerektiren durumları ve önerilen görüş metnini onlara bildirir.",
    ["Görüş metnini rapor yayımlandıktan sonra üst yönetime iletir.",
     "Üst yönetime bildirim yapmaz; görüş sadece raporda yer alır.",
     "Görüşü, üst yönetimin onayı alındıktan sonra değiştirir.",
     "Sadece yönetim talep ederse görüşün gerekçelerini açıklar."],
    "BDS 705 prg. 30'a göre denetçi, olumlu dışında görüş vermeyi düşündüğünde kendisini bu görüşe sevk eden durumları ve "
    "görüş metnini üst yönetimden sorumlu olanlara bildirir.")

P.q("BDS 701 prg. 11",
    f"{B701}, kilit denetim konuları bölümünün giriş cümlesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetçi her bir kilit denetim konusu hakkında ayrı bir görüş bildirir.",
    ["Kilit denetim konularının, muhakemeye göre cari dönemde en çok önem arz eden konular olduğu belirtilir.",
     "Bu konuların tablolar bütününün denetimi kapsamında ele alındığı belirtilir.",
     "Bu konuların görüş oluşturulmasında ele alındığı belirtilir.",
     "Her kilit denetim konusu uygun bir alt başlıkla ayrı bir bölümde açıklanır."],
    "BDS 701 prg. 11'e göre KDK bölümünün giriş cümlesi, bu konuların cari dönemde en çok önem arz eden konular olduğunu "
    "ve tablolar bütününün denetimi kapsamında ve görüş oluşturulmasında ele alındığını, denetçinin bu konular hakkında "
    "ayrı bir görüş bildirmediğini belirtir.")

P.q("BDS 701 prg. 16",
    f"{B701}, bildirilecek kilit denetim konusu bulunmadığına karar verilmesi hâline ilişkin aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Bu durumda KDK başlığı rapordan tamamen çıkarılır ve üst yönetime bildirim yapılmaz.",
    ["Denetçi, “Kilit Denetim Konuları” başlığı altında bu durumun etkisine yönelik bir açıklamaya yer verir.",
     "Bildirilecek konuların sadece süreklilik belirsizliği gibi hususlar olması da benzer açıklama gerektirir.",
     "Denetçi, bildirilecek KDK bulunmadığı kararını üst yönetimden sorumlu olanlara bildirir.",
     "Bu karar işletmenin ve denetimin durum ve gerçeklerine bağlıdır."],
    "BDS 701 prg. 16'ya göre bildirilecek KDK bulunmadığına veya bunların sadece prg. 15'teki konular olduğuna karar "
    "verilirse, denetçi “Kilit Denetim Konuları” başlığı altında bu durumun etkisine yönelik açıklamaya yer verir; prg. "
    "17'ye göre bu kararı üst yönetime bildirir.", zorluk="hard")

P.q("BDS 701 prg. 17-18",
    f"{B701}, kilit denetim konularına ilişkin iletişim ve belgelendirme bakımından aşağıdakilerden hangisi doğrudur?",
    "Denetçi KDK olarak belirlediği hususları üst yönetime bildirir ve belirleme gerekçelerini belgelendirir.",
    ["KDK'lar sadece raporda yer alır; üst yönetime ayrıca bildirilmez.",
     "KDK'lar yönetimle mutabakata varılarak belirlenir ve yönetim onaylar.",
     "KDK belirleme gerekçeleri belgelendirilmez; sadece rapordaki metin saklanır.",
     "KDK'lar denetim sözleşmesi imzalanırken belirlenip sözleşmeye yazılır."],
    "BDS 701 prg. 17'ye göre denetçi KDK olarak belirlediği hususları veya uygun hâllerde bildirilecek KDK bulunmadığı "
    "kararını üst yönetime bildirir; prg. 18'e göre azami dikkat gerektiren konuları, her birinin KDK olup olmadığına "
    "ilişkin kararın gerekçesini belgelendirir.")

P.q("BDS 706 prg. 7-a, 10",
    f"{B706}, diğer hususlar paragrafına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Diğer hususlar paragrafı, tablolarda yer alan bir açıklamayı tekrar etmek için kullanılır.",
    ["Paragraf, tablolarda sunulan veya açıklananlar dışındaki bir hususa atıf yapar.",
     "Husus, kullanıcıların denetimi, denetçinin sorumluluklarını veya raporu anlamasıyla ilgilidir.",
     "Paragraf, mevzuatla yasaklanmamış olması şartıyla eklenir.",
     "BDS 701 uygulanıyorsa husus kilit denetim konusu olarak belirlenmemiş olmalıdır."],
    "BDS 706 prg. 7-a ve 10'a göre diğer hususlar paragrafı, tablolarda sunulan veya açıklananlar dışındaki ve kullanıcıların "
    "denetimi, denetçinin sorumluluklarını veya raporu anlamasıyla ilgili bir hususa atıf yapar; mevzuatla yasaklanmamış "
    "ve KDK olarak belirlenmemiş olması şartıyla eklenir. Tablolardaki hususlara dikkat çekmek DÇH paragrafının işlevidir.")

P.q("BDS 706 A6-A7",
    f"{B706}, dikkat çekilen hususlar paragrafının kullanımına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "DÇH paragrafı, olumlu dışında görüş gerektiren bir durumda görüş değişikliğinin yerine kullanılabilir.",
    ["DÇH paragraflarının yaygın kullanımı, bu bildirimlerin etkinliğini azaltabilir.",
     "DÇH paragrafının eklenmesi denetçinin görüşünü etkilemez.",
     "DÇH paragrafı, yönetimin yapması gereken açıklamaların yerini tutmaz.",
     "DÇH paragrafı, süreklilikle ilgili önemli belirsizliğin raporlanmasının yerini almaz."],
    "BDS 706 A6'ya göre DÇH paragraflarının yaygın kullanımı etkinliği azaltabilir; A7'ye göre DÇH görüşü etkilemez ve "
    "BDS 705'e göre olumlu dışında görüş verilmesinin, yönetimin yapması gereken açıklamaların veya BDS 570'e göre "
    "süreklilik raporlamasının yerini almaz.")

P.q("BDS 706 prg. 12",
    f"{B706}, rapora dikkat çekilen hususlar veya diğer hususlar paragrafı eklemeyi düşünen denetçinin yapması gereken "
    "aşağıdakilerden hangisidir?",
    "Bu düşüncesini ve önerilen paragraf metnini üst yönetimden sorumlu olanlara bildirir.",
    ["Paragraf metnini yönetimin onayına sunar ve onay alınmazsa paragrafı çıkarır.",
     "Paragrafı ekler; üst yönetime ayrıca bildirim yapmaz.",
     "Paragraf eklenmeden önce Kurumdan izin alır.",
     "Paragrafı sadece bir sonraki yılın raporuna ekler."],
    "BDS 706 prg. 12'ye göre denetçi, rapora DÇH veya DH paragrafı eklemeyi düşünüyorsa bu düşüncesini ve önerilen metni "
    "üst yönetimden sorumlu olanlara bildirir.")

P.q("BDS 570 prg. 20",
    f"{B570}, ciddi şüphe oluşturabilecek olay veya şartlar belirlenmekle birlikte önemli belirsizlik bulunmadığı sonucuna "
    "varılmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Önemli belirsizlik bulunmadığından olay ve şartlara ilişkin açıklamalar değerlendirilmez.",
    ["Denetçi, çerçevenin hükümleri ışığında bu olay ve şartlara ilişkin açıklamaların yeterliliğini değerlendirir.",
     "Bu sonuca elde edilen denetim kanıtlarına dayanılarak varılır.",
     "Olay ve şartların etkisini azaltan etkenler değerlendirmede dikkate alınır.",
     "Denetçi, olay ve şartları uygun hâllerde üst yönetimden sorumlu olanlara bildirir."],
    "BDS 570 prg. 20'ye göre ciddi şüphe oluşturabilecek olay veya şartlar belirlenmesine karşın önemli belirsizlik "
    "bulunmadığı sonucuna varılırsa denetçi, çerçeve hükümleri ışığında bu olay veya şartlara ilişkin yeterli açıklamaların "
    "sunulup sunulmadığını değerlendirir; prg. 25 üst yönetimle iletişimi düzenler.")

P.q("BDS 570 prg. 25",
    f"{B570}, sürekliliğe ilişkin olay veya şartlar hakkında üst yönetimden sorumlu olanlarla kurulacak iletişimde yer "
    "alan hususlar arasında aşağıdakilerden hangisi bulunmaz?",
    "Denetim ekibinin süreklilik değerlendirmesine harcadığı saatlerin dökümü",
    ["Olay veya şartların önemli bir belirsizlik oluşturup oluşturmadığı",
     "Süreklilik esasının kullanılmasının uygun olup olmadığı",
     "Tablolardaki ilgili açıklamaların yeterliliği",
     "Varsa olay veya şartların denetçi raporuna etkileri"],
    "BDS 570 prg. 25'e göre iletişim; olay veya şartların önemli belirsizlik oluşturup oluşturmadığını, süreklilik esasının "
    "uygunluğunu, tablolardaki açıklamaların yeterliliğini ve varsa denetçi raporuna etkilerini içerir.")

P.q("BDS 710 prg. 13",
    f"{B710}, önceki dönem tablolarının önceki denetçi tarafından denetlendiği ve atfın mevzuatla yasaklanmadığı durumda "
    "diğer hususlar paragrafında belirtilmesi gerekenler arasında aşağıdakilerden hangisi yer almaz?",
    "Önceki denetçiye ödenen denetim ücretinin tutarı",
    ["Önceki dönem tablolarının önceki denetçi tarafından denetlendiği",
     "Önceki denetçinin verdiği görüşün türü",
     "Olumlu dışında görüş verilmişse bunun nedenleri",
     "Önceki denetçi raporunun tarihi"],
    "BDS 710 prg. 13'e göre diğer hususlar paragrafında önceki dönem tablolarının önceki denetçi tarafından denetlendiği, "
    "verilen görüşün türü ve olumlu dışında görüşse nedenleri ile raporun tarihi belirtilir.")

P.q("BDS 710 prg. 14",
    f"{B710}, önceki döneme ait finansal tabloların denetlenmemiş olması durumuna ilişkin aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Bu durumun raporda açıklanması, açılış bakiyelerine ilişkin kanıt elde etme sorumluluğunu kaldırır.",
    ["Denetçi, karşılık gelen bilgilerin denetlenmediğini diğer hususlar paragrafında açıklar.",
     "Denetçi, açılış bakiyelerinin cari dönem tablolarını önemli ölçüde etkileyen yanlışlık içerip içermediğine dair kanıt elde eder.",
     "Açılış bakiyelerine ilişkin sorumluluk BDS 510 uyarınca devam eder.",
     "Karşılık gelen bilgiler sunulduğunda denetçi görüşünde genellikle bunlara atıf yapılmaz."],
    "BDS 710 prg. 14'e göre önceki dönem denetlenmemişse denetçi bunu diğer hususlar paragrafında açıklar; ancak bu açıklama "
    "açılış bakiyelerinin cari dönemi önemli ölçüde etkileyen yanlışlık içerip içermediğine ilişkin yeterli ve uygun kanıt "
    "elde etme sorumluluğunu ortadan kaldırmaz. Prg. 10'a göre karşılık gelen bilgilere görüşte genellikle atıf yapılmaz.")

P.q("BDS 720 prg. 12-a",
    f"{B720}, “diğer bilgiler” kavramı aşağıdakilerden hangisini ifade eder?",
    "Faaliyet raporundaki, tablolar ve denetçi raporu dışındaki bilgiler",
    ["Finansal tablo dipnotlarında yer alan önemli muhasebe politikaları",
     "Denetçinin çalışma kâğıtlarında yer alan ve rapora alınmayan bilgiler",
     "Yönetimin denetçiye verdiği yazılı açıklamalar",
     "Kilit denetim konuları bölümünde yer alan açıklamalar"],
    "BDS 720 prg. 12-c ve cT'ye göre diğer bilgiler, işletmenin durumu hakkındaki yönetim kurulu irdelemeleri dahil yıllık "
    "faaliyet raporunda yer alan, finansal tablolar ve denetçi raporu dışındaki finansal ve finansal olmayan bilgilerdir.")

P.q("BDY m. 30/2-ç, BDS 705",
    "Denetçi, yeterli kanıt toplamış olmasına rağmen sonradan ortaya çıkan ve görüş oluşturmayı engelleyen belirsizlikler "
    "nedeniyle denetim konusunun geneline ilişkin görüş oluşturamamaktadır. KGK Bağımsız Denetim Yönetmeliği’ne göre "
    "raporun görüş başlığı altında hangi görüş yer alır?",
    "Görüş bildirmekten kaçınma",
    ["Sınırlı olumlu görüş", "Olumsuz görüş", "Olumlu görüş", "Diğer hususlar içeren olumlu görüş"],
    "Yönetmelik m. 30/2-ç'ye göre denetim konusunun genelini etkileyen önemli hususlarda yeterli ve uygun kanıt elde "
    "edilemediği veya yeterli kanıt toplanmasına rağmen görüş oluşturmayı engelleyen belirsizliklerin sonradan ortaya "
    "çıktığı durumlarda görüş bildirmekten kaçınıldığına ilişkin görüş verilir; BDS 705 prg. 10 da benzer bir durumu "
    "düzenler.")

P.q("BDS 705 prg. 21-22",
    f"{B705}, olumlu dışında görüşe neden olan yanlışlığın raporda açıklanmasına ilişkin aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Belirli tutarlarla ilgili yanlışlıkta parasal etki ölçülebilse de dayanak bölümünde açıklanmaz.",
    ["Mümkünse yanlışlığın finansal etkilerinin açıklaması ve tutarı dayanak bölümünde yer alır.",
     "Parasal etkinin ölçülmesi mümkün değilse bu durum dayanak bölümünde belirtilir.",
     "Sayısal olmayan açıklamalardaki yanlışlıkta, yanlışlığın niteliği açıklanır.",
     "Gerekli bir açıklama yapılmamışsa, mümkün olduğunda eksik açıklamaya dayanak bölümünde yer verilir."],
    "BDS 705 prg. 21'e göre belirli tutarlarla ilgili önemli yanlışlıkta mümkünse finansal etkilerin açıklaması ve tutarı "
    "dayanak bölümünde yer alır; ölçülemiyorsa bu belirtilir. Prg. 22-23 sayısal olmayan açıklamalardaki yanlışlıkların ve "
    "eksik açıklamaların dayanak bölümünde nasıl ele alınacağını düzenler.", zorluk="hard")

P.q("BDS 701 A5, BDS 706 prg. 8-b",
    "Denetçi, borsada işlem gören bir şirkette önemli bir hasılat anlaşmasının muhasebeleştirilmesini hem kilit denetim "
    f"konusu olarak belirlemiş hem de bu konuya dikkat çekmek istemektedir. {B706} bu konu için aşağıdakilerden hangisi "
    "doğrudur?",
    "KDK olarak belirlenen husus ayrıca DÇH paragrafına konu edilmez.",
    ["Husus hem KDK bölümünde hem DÇH paragrafında aynen tekrarlanır.",
     "Husus KDK bölümünden çıkarılıp sadece DÇH paragrafında açıklanır.",
     "Husus için sınırlı olumlu görüş verilir ve KDK bölümünde açıklanır.",
     "Husus sadece diğer hususlar paragrafında açıklanır."],
    "BDS 706 prg. 8-b'ye göre BDS 701'in uygulandığı durumlarda DÇH paragrafı ancak husus KDK olarak belirlenmemişse "
    "eklenir; A1-A3'e göre KDK bölümünde yer alan bir husus DÇH paragrafının yerini tutar ve ayrıca tekrarlanmaz.",
    zorluk="hard")

P.q("BDS 705 A1",
    "Denetçi, yeterli ve uygun kanıt elde edemediği bir hususta, tespit edilemeyen yanlışlıkların muhtemel etkisinin "
    f"önemli ancak yaygın olmayabileceği sonucuna varmıştır. {B705} denetçinin vereceği görüş aşağıdakilerden hangisidir?",
    "Sınırlı olumlu görüş",
    ["Görüş vermekten kaçınma", "Olumsuz görüş", "Olumlu görüş", "Dikkat çekilen hususlarla olumlu görüş"],
    "BDS 705 prg. 7-b ve A1'deki tabloya göre yeterli ve uygun kanıt elde edilemeyen bir hususta muhtemel etki önemli "
    "ancak yaygın değilse sınırlı olumlu görüş, önemli ve yaygınsa görüş vermekten kaçınma söz konusudur.", zorluk="easy")

P.q("BDS 700 prg. 22",
    f"{B700}, bağımsız denetçi raporunun kime hitaben düzenleneceğine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Duruma göre sözleşmede ya da mevzuatta belirtilen muhataba",
    ["Sadece işletmenin genel müdürüne",
     "Kamu Gözetimi Kurumuna",
     "İşletmenin en büyük pay sahibine",
     "Denetim şirketinin yönetim kuruluna"],
    "BDS 700 prg. 22'ye göre denetçi raporu, duruma göre sözleşmede ya da mevzuatta belirtilen muhataba hitaben düzenlenir; "
    "A21'e göre bu genellikle raporun hazırlanma amacına göre pay sahipleri veya üst yönetimden sorumlu olanlardır.",
    zorluk="easy")

if __name__ == "__main__":
    sys.exit(P.yaz())
