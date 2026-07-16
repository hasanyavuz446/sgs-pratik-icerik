# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / TMS 1 Finansal Tabloların Sunuluşu — 60 soru.
Kaynak: KGK, TMS 1 (2026 seti). SGS seviyesi: tanım, kapsam, temel ilke.
Doğru şık KISA, çeldiriciler UZUN."""
import json, random, re

DERS, KONU = "muhasebe_standartlari", "tms_1_sunulus"
PREFIX, SEED = "std-tms1-gen", 20260921
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/tms_1_sunulus.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

# ── A. Amaç, kapsam, tam set (10) ──────────────────────────────────────────
q("TMS 1'in amacı bakımından aşağıdakilerden hangisi doğrudur?",
  "Genel amaçlı finansal tabloların sunuluşuna ilişkin esasları belirlemektir",
  ["Her işlem için ayrıntılı muhasebeleştirme ve ölçüm kuralları koymayı amaçlayan bir standarttır",
   "İşletmenin vergi matrahının hesaplanmasına ilişkin usulleri belirleyen bir düzenlemedir",
   "Bağımsız denetçinin denetim programını nasıl hazırlayacağını gösteren bir denetim standardıdır",
   "Yalnızca nakit akış tablosunun düzenlenmesine ilişkin esasları belirleyen bir standarttır"],
  "TMS 1: bu Standardın amacı, genel amaçlı finansal tabloların; önceki dönemlerle ve diğer işletmelerin finansal tablolarıyla karşılaştırılabilir olmasını sağlamak üzere sunuluş esaslarını belirlemektir.",
  "TMS 1 - amaç")

q("Genel amaçlı finansal tablolar bakımından aşağıdakilerden hangisi doğrudur?",
  "Kendi ihtiyacına göre rapor hazırlanmasını isteyemeyecek durumdaki kullanıcıların ihtiyaçlarını karşılamak üzere sunulan tablolardır",
  ["Yalnızca işletme yönetiminin iç kararları için hazırlanan ve dışarıya açıklanmayan raporlardır",
   "Yalnızca vergi idaresine sunulmak üzere hazırlanan beyanname ve eklerini ifade etmektedir",
   "Yalnızca bankaların kredi değerlendirmesi için özel olarak hazırladığı raporları kapsamaktadır",
   "Her kullanıcının kendi isteğine göre özel biçimde hazırlattığı raporlar genel amaçlı sayılır"],
  "TMS 1: genel amaçlı finansal tablolar, özel raporlar hazırlanmasını talep edebilecek konumda olmayan kullanıcıların ihtiyaçlarını karşılamak amacıyla sunulan tablolardır.",
  "TMS 1 - genel amaçlı tablolar")

q("TMS 1'e göre tam bir finansal tablo seti bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal durum tablosu, kâr veya zarar ve diğer kapsamlı gelir tablosu, özkaynak değişim tablosu, nakit akış tablosu ve dipnotlardan oluşur",
  ["Yalnızca finansal durum tablosu ile kâr veya zarar tablosundan oluşur; diğerleri isteğe bağlıdır",
   "Yalnızca nakit akış tablosu ile dipnotlardan oluşan iki belgelik bir seti ifade etmektedir",
   "Dipnotlar setin parçası değildir; yalnızca isteğe bağlı bir ek açıklama metni niteliğindedir",
   "Tam set kavramı TMS 1'de tanımlanmamış olup her işletme dilediği tabloyu sunabilmektedir"],
  "TMS 1: tam bir finansal tablo seti; dönem sonu finansal durum tablosu, döneme ait kâr veya zarar ve diğer kapsamlı gelir tablosu, özkaynak değişim tablosu, nakit akış tablosu, dipnotlar ve gerekli hâllerde en erken karşılaştırmalı dönemin başındaki finansal durum tablosundan oluşur.",
  "TMS 1 - tam set")

q("Finansal tabloların amacı bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin finansal durumu, finansal performansı ve nakit akışları hakkında bilgi sunmaktır",
  ["Yalnızca işletmenin nakit mevcudunu göstermek amacıyla hazırlanan bir belge niteliğindedir",
   "İşletmenin piyasa değerini kesin ve tartışmasız biçimde ortaya koymayı amaçlamaktadır",
   "Yalnızca ortaklara dağıtılacak kâr payını hesaplamak üzere düzenlenen bir hesaplama aracıdır",
   "İşletmenin gelecekteki kârını kesin olarak öngörmeyi amaçlayan bir tahmin belgesidir"],
  "TMS 1: finansal tablolar, işletmenin finansal durumu, finansal performansı ve nakit akışları hakkında geniş bir kitleye faydalı bilgi sunmayı ve yönetimin kaynakları etkin kullanımına ilişkin hesap verebilirliğini göstermeyi amaçlar.",
  "TMS 1 - finansal tabloların amacı")

q("Özkaynak değişim tablosunun işlevi bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönem başı ve dönem sonu özkaynak tutarları arasındaki değişimin kaynaklarını gösterir",
  ["İşletmenin dönem içindeki nakit giriş ve çıkışlarını faaliyet türlerine ayırarak göstermektedir",
   "İşletmenin belirli bir tarihteki varlık ve kaynak durumunu özetleyerek raporlayan tablodur",
   "İşletmenin yalnızca ödediği vergileri ve vergi karşılıklarını ayrıntılı biçimde göstermektedir",
   "İşletmenin gelecek dönemlere ilişkin bütçe ve kâr hedeflerini ortaya koyan bir tablodur"],
  "TMS 1: özkaynak değişim tablosu, dönem başı ve dönem sonu özkaynak tutarları arasındaki değişimi; toplam kapsamlı gelir, ortak işlemleri ve muhasebe politikası değişikliği/hata düzeltmesi etkileri gibi kalemler bazında gösterir.",
  "TMS 1 - özkaynak değişim tablosu")

q("Finansal tabloların sunum sıklığı bakımından aşağıdakilerden hangisi doğrudur?",
  "Tam bir finansal tablo seti en az yıllık olarak sunulur; dönem değişirse bu durum açıklanır",
  ["Finansal tablolar yalnızca işletmenin kurulduğu yıl bir kez sunulur; sonraki yıllarda sunulmaz",
   "Finansal tablolar her ay tam set hâlinde sunulmak zorunda olup yıllık sunum yeterli değildir",
   "Finansal tabloların sunum sıklığı standartlarda düzenlenmemiş olup tümüyle serbest bırakılmıştır",
   "Finansal tablolar beş yılda bir sunulur; ara dönemlerde hiçbir raporlama yapılmamaktadır"],
  "TMS 1: işletme tam bir finansal tablo setini (karşılaştırmalı bilgi dâhil) en az yıllık olarak sunar. Raporlama dönemi sonu değişir ve tablolar bir yıldan farklı dönem için sunulursa; dönem, nedeni ve tutarların tam karşılaştırılabilir olmadığı açıklanır.",
  "TMS 1 - sunum sıklığı")

q("TMS 1'e göre finansal tablo başlıklarının kullanılması bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme, Standartta kullanılanlardan farklı tablo başlıkları kullanabilir",
  ["İşletme her hâlde Standartta yer alan başlıkları birebir kullanmak zorunda olup değiştiremez",
   "İşletme tablolara hiçbir başlık koymaz; tablolar başlıksız olarak sunulmak zorundadır",
   "Tablo başlıkları yalnızca vergi idaresi tarafından belirlenir ve her yıl yeniden ilan edilir",
   "Tablo başlığı değiştirilirse finansal tablolar kendiliğinden geçersiz hâle gelmektedir"],
  "TMS 1: işletme, bu Standartta kullanılanlardan farklı tablo başlıkları kullanabilir. Örneğin 'finansal durum tablosu' yerine 'bilanço' başlığı kullanılabilir.",
  "TMS 1 - tablo başlıkları")

q("TMS 1'in kapsamı bakımından aşağıdakilerden hangisi doğrudur?",
  "Genel amaçlı finansal tabloların sunuluşunda uygulanır; ara dönem özet tablolara TMS 34 uygulanır",
  ["TMS 1 yalnızca ara dönem finansal tablolarda uygulanır; yıllık tablolarda hiç uygulanmamaktadır",
   "TMS 1 yalnızca kâr amacı gütmeyen kuruluşlara uygulanan özel bir standart niteliğindedir",
   "TMS 1 yalnızca bankalar ve sigorta şirketleri tarafından uygulanabilen bir düzenlemedir",
   "TMS 1 finansal tabloların sunuluşunu değil, yalnızca ölçüm esaslarını düzenleyen bir standarttır"],
  "TMS 1: bu Standart, TFRS'lere uygun olarak hazırlanan genel amaçlı finansal tabloların sunuluşunda uygulanır. TMS 34 kapsamında hazırlanan ara dönem özet finansal tablolara uygulanmaz (bazı hükümleri hariç).",
  "TMS 1 - kapsam")

q("Aşağıdakilerden hangileri TMS 1'e göre tam finansal tablo setinde yer alır?\n\nI. Finansal durum tablosu\n\nII. Nakit akış tablosu\n\nIII. Dipnotlar",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Tam set; finansal durum tablosu (I), nakit akış tablosu (II) ve dipnotların (III) yanı sıra kâr veya zarar ve diğer kapsamlı gelir tablosu ile özkaynak değişim tablosunu içerir. Üçü de sette yer alır.",
  "TMS 1 - tam set")

q("Aşağıdaki ifadelerden hangileri TMS 1 bakımından doğrudur?\n\nI. Tam set en az yıllık sunulur\n\nII. Standarttan farklı tablo başlıkları kullanılabilir\n\nIII. Dipnotlar tam setin parçası değildir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Tam set en az yıllık sunulur (I) ve farklı başlıklar kullanılabilir (II). Dipnotlar ise tam setin ayrılmaz parçasıdır; bu nedenle III yanlıştır.",
  "TMS 1 - tam set ve sunum")

# ── B. Genel özellikler (14) ───────────────────────────────────────────────
q("TFRS'lere uygunluk beyanı bakımından aşağıdakilerden hangisi doğrudur?",
  "TFRS'lerin tümüne uyan işletme, uygunluk beyanını dipnotlarda açık ve koşulsuz olarak belirtir",
  ["İşletme bazı standartlara uymasa dahi uygunluk beyanında bulunabilir ve bu beyan geçerli sayılır",
   "Uygunluk beyanı yalnızca sözlü olarak yapılır; dipnotlarda yazılı biçimde yer verilmemektedir",
   "Uygunluk beyanı yalnızca denetçi tarafından yapılır; işletmenin böyle bir beyanı bulunmamaktadır",
   "Uygunluk beyanı yapılması yasaktır; işletmeler standartlara uygunluğu hiçbir hâlde belirtemez"],
  "TMS 1: TFRS'lere uygun finansal tablo düzenleyen işletme, bu uygunluğu dipnotlarda açık ve koşulsuz olarak belirtir. Tüm hükümlere uyulmadıkça tabloların TFRS'lere uygun olduğu belirtilemez.",
  "TMS 1 - uygunluk beyanı")

q("İşletmenin sürekliliği bakımından aşağıdakilerden hangisi doğrudur?",
  "Tablolar süreklilik esasına göre hazırlanır; süreklilik varsayımı uygun değilse bu durum ve kullanılan esas açıklanır",
  ["Tablolar her hâlde tasfiye esasına göre hazırlanır; süreklilik varsayımı hiç kullanılmamaktadır",
   "Süreklilik konusunda ciddi şüphe doğsa dahi hiçbir açıklama yapılmasına gerek bulunmamaktadır",
   "Süreklilik varsayımı yalnızca halka açık şirketleri bağlar; diğer işletmeler bundan muaftır",
   "Süreklilik varsayımı, işletmenin gelecekte kâr edeceğinin garanti edilmesi anlamına gelmektedir"],
  "TMS 1: yönetim, tabloları hazırlarken işletmenin sürekliliğini değerlendirir. Süreklilikle ilgili ciddi şüphe doğuran önemli belirsizlikler varsa açıklanır; süreklilik esası uygun değilse tablolar başka esasa göre hazırlanır, bu esas ve neden açıklanır.",
  "TMS 1 - işletmenin sürekliliği")

q("Muhasebenin tahakkuk esası bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit akış tablosu dışındaki tüm finansal tablolar tahakkuk esasına göre hazırlanır",
  ["Tüm finansal tablolar nakit esasına göre, yalnızca tahsilat ve ödemeler dikkate alınarak hazırlanır",
   "Nakit akış tablosu tahakkuk esasına, diğer tüm tablolar ise nakit esasına göre düzenlenmektedir",
   "Tahakkuk esası yalnızca vergi hesaplamasında kullanılır; finansal raporlamada uygulanmamaktadır",
   "Tahakkuk ve nakit esası arasında hiçbir fark bulunmadığından bu ayrım anlamsız kabul edilir"],
  "TMS 1: işletme, nakit akış bilgileri hariç finansal tablolarını muhasebenin tahakkuk esasına göre düzenler. Kalemler, unsur tanımlarını ve muhasebeleştirme ölçütlerini karşıladıklarında finansal tablolara alınır.",
  "TMS 1 - tahakkuk esası")

q("Önemlilik ve birleştirme bakımından aşağıdakilerden hangisi doğrudur?",
  "Benzer kalemlerden oluşan her önemli sınıf ayrı sunulur; farklı nitelikteki kalemler önemsiz olmadıkça ayrı sunulur",
  ["Tüm kalemler her hâlde tek bir toplam hâlinde birleştirilerek sunulmak zorunda tutulmaktadır",
   "Tüm kalemler her hâlde ayrı ayrı sunulur; önemsiz olsa dahi hiçbir birleştirme yapılamamaktadır",
   "Önemlilik kavramı TMS 1'de yer almaz; yalnızca denetim standartlarının konusunu oluşturur",
   "Kalemlerin sunumu tümüyle işletmenin keyfine bırakılmış olup hiçbir ölçüt bulunmamaktadır"],
  "TMS 1: işletme, benzer kalemlerden oluşan her önemli sınıfı finansal tablolarda ayrı olarak sunar. Farklı nitelikteki veya işlevdeki kalemler, önemsiz olmadıkça ayrı sunulur.",
  "TMS 1 - önemlilik ve birleştirme")

q("Netleştirme (mahsup) bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir TFRS gerektirmedikçe veya izin vermedikçe varlıklar ile borçlar, gelirler ile giderler netleştirilmez",
  ["Varlıklar ile borçlar her hâlde net tutar üzerinden gösterilmek zorunda olup brüt gösterim yasaktır",
   "Netleştirme tümüyle serbest olup işletme dilediği kalemleri netleştirerek sunabilmektedir",
   "Netleştirme yasağı yalnızca gelir ve giderler için geçerli olup varlık ve borçları kapsamaz",
   "Netleştirme kavramı TMS 1'de düzenlenmemiş olup yalnızca vergi mevzuatının konusudur"],
  "TMS 1: bir TFRS gerektirmedikçe veya izin vermedikçe varlıklar ile borçlar, gelirler ile giderler netleştirilmez. Ancak stok değer düşüklüğü karşılığı gibi düzeltici hesapların indirilmesi netleştirme sayılmaz.",
  "TMS 1 - netleştirme")

q("Karşılaştırmalı bilgi bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir TFRS aksini öngörmedikçe, cari dönemde raporlanan tüm tutarlar için önceki döneme ait karşılaştırmalı bilgi sunulur",
  ["Finansal tablolarda yalnızca cari dönem verileri sunulur; önceki dönem bilgisi hiç verilmemektedir",
   "Karşılaştırmalı bilgi verilmesi tümüyle işletmenin takdirinde olup standartlarda düzenlenmemiştir",
   "Karşılaştırmalı bilgi yalnızca finansal durum tablosunda verilir; gelir tablosunda verilmemektedir",
   "Karşılaştırmalı bilgi verilirken önceki dönem tutarları cari dönemle toplanarak gösterilmektedir"],
  "TMS 1: bir TFRS aksine izin vermedikçe veya gerektirmedikçe, cari dönem finansal tablolarında raporlanan tüm tutarlar için önceki döneme ilişkin karşılaştırmalı bilgi sunulur. Anlaşılabilirlik için gerekliyse anlatısal bilgi de karşılaştırmalı verilir.",
  "TMS 1 - karşılaştırmalı bilgi")

q("Sunumun tutarlılığı bakımından aşağıdakilerden hangisi doğrudur?",
  "Kalemlerin sunumu ve sınıflandırması dönemler arasında aynı şekilde sürdürülür; ancak haklı sebeple değiştirilebilir",
  ["Sunum ve sınıflandırma her dönem rastgele değiştirilmek zorunda olup tutarlılık aranmamaktadır",
   "Sunum ve sınıflandırma hiçbir koşulda değiştirilemez; ilk seçilen biçim sonsuza kadar sürdürülür",
   "Tutarlılık ilkesi TMS 1'de yer almaz; her dönem farklı sunum yapılması serbest bırakılmıştır",
   "Sunumun tutarlılığı yalnızca vergi idaresinin izniyle sağlanabilen bir uygulama niteliğindedir"],
  "TMS 1: finansal tablolardaki kalemlerin sunumu ve sınıflandırması dönemden döneme aynı şekilde sürdürülür. Ancak faaliyetlerin niteliğinde önemli değişiklik olması veya başka bir sunumun daha uygun olduğunun anlaşılması gibi hâllerde değiştirilebilir; bu durumda karşılaştırmalı tutarlar yeniden sınıflandırılır.",
  "TMS 1 - sunumun tutarlılığı")

q("Gerçeğe uygun sunum bakımından aşağıdakilerden hangisi doğrudur?",
  "TFRS'lere uygunluk, gerçeğe uygun sunumu sağlar; gerekirse ilave açıklama yapılır",
  ["TFRS'lere uygunluk gerçeğe uygun sunum için yeterli değildir; her hâlde farklı bir esas aranır",
   "Gerçeğe uygun sunum, işletmenin istediği sonucu gösterecek biçimde tablo düzenlemesini ifade eder",
   "Gerçeğe uygun sunum yalnızca vergi mevzuatına uygunluğu ifade eden bir kavram niteliğindedir",
   "Gerçeğe uygun sunum kavramı TMS 1'de düzenlenmemiş olup uygulamada kullanılmamaktadır"],
  "TMS 1: finansal tablolar işletmenin finansal durumunu, performansını ve nakit akışlarını gerçeğe uygun olarak sunar. TFRS'lerin uygulanması ve gerekli durumlarda ilave açıklama yapılması, gerçeğe uygun sunumu sağlar.",
  "TMS 1 - gerçeğe uygun sunum")

q("Finansal tabloların belirlenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal tablolar açıkça tanımlanır ve aynı belgedeki diğer bilgilerden ayırt edilir",
  ["Finansal tablolar diğer bilgilerle karıştırılabilir; ayırt edilmelerine gerek bulunmamaktadır",
   "Finansal tablolarda işletmenin adı belirtilmez; anonim biçimde sunulmak zorunda tutulmuştur",
   "Finansal tablolarda raporlama dönemi belirtilmez; yalnızca tutarlar gösterilmektedir",
   "Finansal tabloların tanımlanması yalnızca denetçinin sorumluluğunda olan bir işlemdir"],
  "TMS 1: işletme finansal tabloları açıkça tanımlar ve aynı belgede yer alan diğer bilgilerden ayırt eder. Raporlayan işletmenin adı, tabloların bireysel/konsolide olduğu, raporlama dönemi, para birimi ve yuvarlama derecesi açıkça belirtilir.",
  "TMS 1 - tabloların tanımlanması")

q("Bir işletme, bir varlığı ve buna karşılık gelen bir borcu net tutar olarak tek satırda göstermek istemektedir. TMS 1 bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir TFRS izin vermedikçe netleştirme yapılamaz; varlık ve borç brüt olarak ayrı gösterilir",
  ["Netleştirme her hâlde serbesttir; işletme dilediği kalemleri net olarak gösterebilmektedir",
   "Netleştirme yalnızca tutarlar eşitse yapılabilir; farklı tutarlarda netleştirme yasaklanmıştır",
   "Netleştirme yapılırsa finansal tablolar kendiliğinden geçersiz sayılır ve yeniden düzenlenir",
   "Netleştirme yalnızca denetçinin onayıyla ve her yıl yeniden izin alınarak yapılabilmektedir"],
  "TMS 1: bir TFRS gerektirmedikçe veya izin vermedikçe varlıklar ile borçlar netleştirilmez. Netleştirme, kullanıcıların işlemleri anlama ve gelecekteki nakit akışlarını değerlendirme yeteneğini azaltır.",
  "TMS 1 - netleştirme (senaryo)")

q("Bir işletme TFRS'lerin çoğuna uymuş ancak bir standardın hükmünü uygulamamıştır. TMS 1 bakımından aşağıdakilerden hangisi doğrudur?",
  "Tüm hükümlere uyulmadıkça tabloların TFRS'lere uygun olduğu belirtilemez",
  ["İşletme çoğu standarda uyduğu için uygunluk beyanında bulunabilir ve bu beyan geçerli olur",
   "İşletme uymadığı standardı dipnotta belirtmek koşuluyla uygunluk beyanı yapabilmektedir",
   "Uygunluk beyanı standartlara uyumla ilgili değildir; her hâlde ve koşulsuz yapılabilmektedir",
   "İşletme bu durumda finansal tablo düzenlemekten tümüyle muaf tutulmuş olmaktadır"],
  "TMS 1: finansal tablolar, TFRS'lerin tüm hükümlerine uymadıkça TFRS'lere uygun olarak nitelendirilemez. Uygunluk beyanı açık ve koşulsuz olmalıdır.",
  "TMS 1 - uygunluk beyanı (senaryo)")

q("Aşağıdakilerden hangileri TMS 1'de düzenlenen genel özelliklerdendir?\n\nI. Gerçeğe uygun sunum ve TFRS'lere uygunluk\n\nII. İşletmenin sürekliliği\n\nIII. Tahakkuk esası",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 1'in genel özellikleri; gerçeğe uygun sunum ve TFRS'lere uygunluk (I), işletmenin sürekliliği (II), tahakkuk esası (III), önemlilik ve birleştirme, netleştirme, sunum sıklığı, karşılaştırmalı bilgi ve tutarlılıktır. Üçü de doğrudur.",
  "TMS 1 - genel özellikler")

q("Aşağıdaki ifadelerden hangileri TMS 1 bakımından doğrudur?\n\nI. Karşılaştırmalı bilgi sunulur\n\nII. Sunum dönemler arasında tutarlı sürdürülür\n\nIII. Varlık ve borçlar kural olarak netleştirilerek gösterilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Karşılaştırmalı bilgi sunulur (I) ve sunum tutarlı sürdürülür (II). Ancak bir TFRS izin vermedikçe netleştirme yapılmaz; brüt gösterim esastır, bu nedenle III yanlıştır.",
  "TMS 1 - genel özellikler")

q("Aşağıdaki ifadelerden hangileri finansal tabloların tanımlanmasına ilişkin doğrudur?\n\nI. Raporlayan işletmenin adı belirtilir\n\nII. Raporlama dönemi belirtilir\n\nIII. Sunum para birimi belirtilmez",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "İşletmenin adı (I) ve raporlama dönemi (II) belirtilir. Sunum para birimi de belirtilmek zorundadır; bu nedenle III yanlıştır.",
  "TMS 1 - tabloların tanımlanması")

# ── C. Finansal durum tablosu (14) ─────────────────────────────────────────
q("Finansal durum tablosunda dönen/duran ayrımı bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme, likidite esasına göre sunum daha uygun bilgi vermedikçe dönen/duran ve kısa/uzun vadeli ayrımı yapar",
  ["İşletme her hâlde likidite esasına göre sunum yapmak zorunda olup dönen/duran ayrımı yasaktır",
   "Dönen/duran ayrımı yalnızca üretim işletmelerinde yapılır; ticaret işletmeleri bundan muaftır",
   "Tüm varlıklar duran varlık olarak sınıflandırılır; dönen varlık kategorisi bulunmamaktadır",
   "Dönen/duran ayrımı standartta düzenlenmemiş olup her işletme serbestçe karar vermektedir"],
  "TMS 1: işletme, likidite esasına göre sunumun daha uygun ve ihtiyaca daha uygun bilgi sağladığı durumlar hariç, finansal durum tablosunda dönen/duran varlıklar ile kısa/uzun vadeli yükümlülükleri ayrı sınıflar hâlinde sunar.",
  "TMS 1 - dönen/duran ayrımı")

q("Dönen varlık sınıflandırması bakımından aşağıdakilerden hangisi doğrudur?",
  "Normal faaliyet döngüsünde ya da on iki ay içinde paraya çevrilmesi beklenen varlıklar dönen varlıktır",
  ["Varlığın dönen sayılması yalnızca fiziken taşınabilir olmasına bağlı olan bir ölçüttür",
   "Yalnızca nakit ve nakit benzerleri dönen varlık sayılır; stoklar ve alacaklar duran varlıktır",
   "Dönen varlık ayrımı yalnızca stoklar için geçerli olup diğer kalemleri hiç kapsamamaktadır",
   "Varlıkların dönen ya da duran olması işletmenin her yıl serbestçe değiştirdiği bir tercihtir"],
  "TMS 1: bir varlık; normal faaliyet döngüsü içinde paraya çevrilmesi/satılması/tüketilmesi bekleniyorsa, öncelikle ticari amaçla elde tutuluyorsa, raporlama döneminden sonra on iki ay içinde paraya çevrilmesi bekleniyorsa ya da nakit/nakit benzeri ise dönen varlıktır.",
  "TMS 1 - dönen varlık")

q("Kısa vadeli yükümlülük sınıflandırması bakımından aşağıdakilerden hangisi doğrudur?",
  "Normal faaliyet döngüsü içinde ödenmesi beklenen veya raporlama döneminden sonraki on iki ayda ödenecek yükümlülükler kısa vadelidir",
  ["Tüm yükümlülükler uzun vadeli sayılır; kısa vadeli yükümlülük kategorisi bulunmamaktadır",
   "Yükümlülüğün kısa vadeli sayılması yalnızca tutarının küçük olmasına bağlı bir ölçüttür",
   "Kısa vadeli yükümlülük yalnızca banka kredilerini kapsar; ticari borçlar bu kapsamda değildir",
   "Yükümlülüklerin vade ayrımı standartta düzenlenmemiş olup her işletme serbestçe belirler"],
  "TMS 1: bir yükümlülük; normal faaliyet döngüsü içinde ödenmesi bekleniyorsa, öncelikle ticari amaçla elde tutuluyorsa, raporlama döneminden sonra on iki ay içinde ödenecekse ya da ödemenin en az on iki ay ertelenmesine ilişkin koşulsuz hakkı yoksa kısa vadelidir.",
  "TMS 1 - kısa vadeli yükümlülük")

q("Normal faaliyet döngüsü bakımından aşağıdakilerden hangisi doğrudur?",
  "İşleme tabi tutulacak varlıkların tedarikinden nakde çevrilmesine kadar geçen süredir; açıkça belirlenemiyorsa on iki ay varsayılır",
  ["Normal faaliyet döngüsü her hâlde ve istisnasız olarak on iki ay şeklinde kanunla sabitlenmiştir",
   "Normal faaliyet döngüsü, işletmenin kurulduğu tarihten tasfiye edildiği tarihe kadar geçen süredir",
   "Normal faaliyet döngüsü kavramı TMS 1'de yer almayan ve uygulanmayan bir kavram niteliğindedir",
   "Normal faaliyet döngüsü yalnızca hizmet işletmelerinde kullanılan bir kavram olarak tanımlanır"],
  "TMS 1: normal faaliyet döngüsü, işleme tabi tutulmak üzere edinilen varlıkların işlenip nakit veya nakit benzerine çevrilmesi arasında geçen süredir. Açıkça belirlenemediğinde on iki ay olduğu varsayılır.",
  "TMS 1 - faaliyet döngüsü")

q("Finansal durum tablosunda sunulacak kalemler bakımından aşağıdakilerden hangisi doğrudur?",
  "Standart asgari kalemleri sayar; işletme ihtiyaca uygunsa ilave kalem, başlık ve ara toplam sunar",
  ["Standart tüm kalemleri tek tek ve kesin biçimde sayar; ilave kalem sunulması yasaklanmıştır",
   "Standart hiçbir kalem saymaz; tablo düzeni tümüyle işletmenin serbest tercihine bırakılmıştır",
   "Tablo düzeni yalnızca vergi idaresince belirlenir; işletmenin hiçbir takdir yetkisi bulunmaz",
   "İlave kalem sunulması hâlinde finansal tablolar TFRS'lere aykırı hâle gelmiş sayılmaktadır"],
  "TMS 1: Standart finansal durum tablosunda sunulacak asgari kalemleri belirler. İşletmenin finansal durumunun anlaşılması bakımından ihtiyaca uygunsa ilave kalemler, başlıklar ve ara toplamlar sunulur.",
  "TMS 1 - sunulacak kalemler")

q("Ertelenmiş vergi varlık ve yükümlülüklerinin sınıflandırılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönen/duran ayrımı yapan işletmelerde ertelenmiş vergi varlık ve yükümlülükleri dönen/kısa vadeli olarak sınıflandırılmaz",
  ["Ertelenmiş vergi varlıkları her hâlde dönen varlık olarak sınıflandırılmak zorunda tutulmuştur",
   "Ertelenmiş vergi yükümlülükleri her hâlde kısa vadeli yükümlülük olarak gösterilmektedir",
   "Ertelenmiş vergi kalemleri finansal durum tablosunda hiçbir biçimde gösterilmemektedir",
   "Ertelenmiş vergi kalemlerinin sınıflandırılması tümüyle işletmenin serbest tercihindedir"],
  "TMS 1: dönen/duran ve kısa/uzun vadeli ayrımı yapan bir işletme, ertelenmiş vergi varlıklarını (yükümlülüklerini) dönen varlık (kısa vadeli yükümlülük) olarak sınıflandıramaz.",
  "TMS 1 - ertelenmiş vergi sınıflandırması")

q("Bir işletmenin raporlama döneminden sonra on beş ay içinde ödeyeceği ve ödemeyi erteleme konusunda koşulsuz hakkı bulunan borcu bakımından aşağıdakilerden hangisi doğrudur?",
  "Borç uzun vadeli yükümlülük olarak sınıflandırılır",
  ["Borç her hâlde kısa vadeli yükümlülük olarak sınıflandırılmak zorunda tutulmaktadır",
   "Borç finansal durum tablosunda hiçbir biçimde gösterilmez; yalnızca dipnotta açıklanır",
   "Borç özkaynak içinde gösterilir; yabancı kaynaklarda sınıflandırılması mümkün değildir",
   "Borcun sınıflandırılması işletmenin o yılki tercihine göre serbestçe belirlenebilmektedir"],
  "TMS 1: yükümlülük raporlama döneminden sonra en az on iki ay süreyle ödemeyi erteleme konusunda koşulsuz hakka sahipse uzun vadeli sınıflandırılır. On beş ay vade ve koşulsuz erteleme hakkı bu ölçütü karşılar.",
  "TMS 1 - vade sınıflandırması (senaryo)")

q("Özkaynak kalemlerinin sunumu bakımından aşağıdakilerden hangisi doğrudur?",
  "Ödenmiş sermaye ve yedekler gibi özkaynak sınıfları finansal durum tablosunda veya dipnotlarda gösterilir",
  ["Özkaynak tek bir toplam olarak gösterilir; alt sınıflara hiçbir hâlde ayrılamamaktadır",
   "Özkaynak kalemleri yalnızca nakit akış tablosunda gösterilir; bilançoda yer almamaktadır",
   "Özkaynak kalemlerinin sunumu standartta düzenlenmemiş olup uygulamada gösterilmemektedir",
   "Özkaynak kalemleri yabancı kaynaklarla birlikte tek bir toplam hâlinde sunulmak zorundadır"],
  "TMS 1: işletme, ödenmiş sermaye ve yedekler gibi özkaynak sınıflarını finansal durum tablosunda veya özkaynak değişim tablosunda ya da dipnotlarda gösterir.",
  "TMS 1 - özkaynak sunumu")

q("Karşılaştırmalı dönem başı finansal durum tablosu bakımından aşağıdakilerden hangisi doğrudur?",
  "Geriye dönük muhasebe politikası uygulaması, yeniden düzenleme veya yeniden sınıflandırma önemli etki doğuruyorsa üçüncü bir tablo sunulur",
  ["Her hâlde ve istisnasız olarak üç dönemlik finansal durum tablosu sunulmak zorunda tutulmuştur",
   "Üçüncü tablo hiçbir koşulda sunulmaz; yalnızca iki dönem gösterilmesi mümkün bulunmaktadır",
   "Üçüncü tablo yalnızca işletme kâr ettiğinde ve dağıtım yapıldığında sunulmak zorundadır",
   "Üçüncü tablonun sunulup sunulmayacağı tümüyle denetçinin takdirine bırakılmış durumdadır"],
  "TMS 1: işletme bir muhasebe politikasını geriye dönük uygular, kalemleri geriye dönük yeniden düzenler ya da yeniden sınıflandırırsa ve bu, en erken karşılaştırmalı dönemin başındaki finansal durum tablosunda önemli etki doğuruyorsa, o tarihli üçüncü bir finansal durum tablosu da sunar.",
  "TMS 1 - üçüncü tablo")

q("Bir işletme stoklarını normal faaliyet döngüsü on sekiz ay olduğu için on iki ayı aşan sürede paraya çevirmektedir. TMS 1 bakımından aşağıdakilerden hangisi doğrudur?",
  "Stoklar normal faaliyet döngüsü içinde paraya çevrildiğinden dönen varlık olarak sınıflandırılır",
  ["Stoklar on iki ayı aştığı için her hâlde duran varlık olarak sınıflandırılmak zorundadır",
   "Stoklar bu durumda finansal durum tablosunda hiçbir biçimde gösterilmemektedir",
   "Stoklar yarısı dönen yarısı duran varlık olacak biçimde ikiye bölünerek gösterilmelidir",
   "Stokların sınıflandırılması işletmenin serbest tercihine bırakılmış bir konu niteliğindedir"],
  "TMS 1: normal faaliyet döngüsü içinde satılması, tüketilmesi veya paraya çevrilmesi beklenen stoklar ve ticari alacaklar, on iki aydan uzun sürede paraya çevrilecek olsa dahi dönen varlık olarak sınıflandırılır.",
  "TMS 1 - dönen varlık (senaryo)")

q("Likidite esasına göre sunum bakımından aşağıdakilerden hangisi doğrudur?",
  "Likidite esasına göre sunum daha güvenilir ve ihtiyaca uygun bilgi sağlıyorsa varlık ve borçlar likidite sırasına göre sunulur",
  ["Likidite esasına göre sunum yasaktır; her hâlde dönen/duran ayrımı yapılmak zorundadır",
   "Likidite esası yalnızca üretim işletmelerinde kullanılabilen özel bir sunum biçimidir",
   "Likidite esası, varlıkların büyükten küçüğe tutar sırasına göre sunulmasını ifade etmektedir",
   "Likidite esası yalnızca vergi idaresinin izniyle uygulanabilen bir sunum yöntemidir"],
  "TMS 1: likidite esasına göre sunum güvenilir ve daha ihtiyaca uygun bilgi sağlıyorsa (bankalar gibi finansal kuruluşlarda olduğu üzere), işletme tüm varlık ve borçlarını likidite sırasına göre sunar.",
  "TMS 1 - likidite esası")

q("Aşağıdakilerden hangileri TMS 1'e göre dönen varlık sayılır?\n\nI. Normal faaliyet döngüsünde satılması beklenen stok\n\nII. Nakit ve nakit benzerleri\n\nIII. Uzun vadeli kullanım amaçlı fabrika binası",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Normal faaliyet döngüsünde satılacak stok (I) ve nakit/nakit benzerleri (II) dönen varlıktır. Uzun vadeli kullanım amaçlı fabrika binası (III) ise duran varlıktır; bu nedenle yanlıştır.",
  "TMS 1 - dönen varlık")

q("Aşağıdaki ifadelerden hangileri TMS 1'in finansal durum tablosu hükümleri bakımından doğrudur?\n\nI. Kural olarak dönen/duran ayrımı yapılır\n\nII. Standart asgari kalemleri belirler\n\nIII. Ertelenmiş vergi varlıkları dönen varlık olarak sınıflandırılır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Kural olarak dönen/duran ayrımı yapılır (I) ve Standart asgari kalemleri belirler (II). Ancak ertelenmiş vergi varlıkları dönen varlık olarak sınıflandırılamaz; bu nedenle III yanlıştır.",
  "TMS 1 - finansal durum tablosu")

q("Aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Normal faaliyet döngüsü belirlenemiyorsa on iki ay varsayılır\n\nII. Ticari alacaklar döngü içindeyse on iki ayı aşsa da dönen varlıktır\n\nIII. Likidite esasına göre sunum hiçbir hâlde yapılamaz",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Döngü belirlenemiyorsa on iki ay varsayılır (I) ve döngü içindeki ticari alacaklar on iki ayı aşsa da dönen varlıktır (II). Likidite esası ise daha uygun bilgi sağlıyorsa uygulanabilir; bu nedenle III yanlıştır.",
  "TMS 1 - sınıflandırma")

# ── D. Kâr veya zarar ve diğer kapsamlı gelir (12) ─────────────────────────
q("Kapsamlı gelir kavramı bakımından aşağıdakilerden hangisi doğrudur?",
  "Toplam kapsamlı gelir, kâr veya zarar ile diğer kapsamlı gelirin toplamından oluşur",
  ["Toplam kapsamlı gelir yalnızca kâr veya zarardan oluşur; diğer kapsamlı gelir dâhil değildir",
   "Toplam kapsamlı gelir yalnızca diğer kapsamlı gelirden oluşur; kâr veya zarar hariç tutulur",
   "Kapsamlı gelir kavramı TMS 1'de yer almayan ve uygulanmayan bir kavram niteliğindedir",
   "Toplam kapsamlı gelir, ortakların koyduğu sermayeyi de içeren bir toplam olarak hesaplanır"],
  "TMS 1: toplam kapsamlı gelir, ortakların katkı ve dağıtımları dışındaki işlemler nedeniyle bir dönemde özkaynakta meydana gelen değişimdir ve kâr veya zarar ile diğer kapsamlı gelirin toplamına eşittir.",
  "TMS 1 - kapsamlı gelir")

q("Diğer kapsamlı gelir bakımından aşağıdakilerden hangisi doğrudur?",
  "Diğer TFRS'lerin kâr veya zarar dışında muhasebeleştirilmesini gerektirdiği gelir ve gider kalemlerini içerir",
  ["Tüm gelir ve gider kalemlerini içerir; kâr veya zarar tablosu hiç kullanılmamaktadır",
   "İşletmenin dilediği gelir ve gideri koyabileceği serbest bir bölüm olarak düzenlenmiştir",
   "Yalnızca ortakların koyduğu sermayeyi gösteren bir özkaynak bölümü niteliğindedir",
   "Diğer kapsamlı gelir kavramı TMS 1'de düzenlenmemiş olup uygulamada kullanılmamaktadır"],
  "TMS 1: diğer kapsamlı gelir, diğer TFRS'lerin kâr veya zarara dâhil edilmemesini gerektirdiği veya izin verdiği gelir ve gider kalemlerini içerir (yeniden değerleme fazlası, bazı yabancı para çevrim farkları gibi).",
  "TMS 1 - diğer kapsamlı gelir")

q("Kâr veya zarar ile diğer kapsamlı gelirin sunumu bakımından aşağıdakilerden hangisi doğrudur?",
  "Tek bir tabloda veya kâr/zarar tablosu ile onu takip eden kapsamlı gelir tablosu olmak üzere iki tabloda sunulabilir",
  ["Yalnızca tek bir tabloda sunulabilir; iki tablo seçeneği kesin olarak yasaklanmıştır",
   "Yalnızca iki ayrı tabloda sunulabilir; tek tablo seçeneği hiçbir hâlde kullanılamamaktadır",
   "Sunum biçimi yalnızca vergi idaresince belirlenir; işletmenin bir seçim hakkı bulunmaz",
   "Kâr veya zarar hiçbir tabloda sunulmaz; yalnızca dipnotlarda açıklanmak zorundadır"],
  "TMS 1: işletme, bir dönemdeki tüm gelir ve gider kalemlerini tek bir kâr veya zarar ve diğer kapsamlı gelir tablosunda ya da iki ayrı tabloda (kâr veya zarar tablosu ve onunla başlayan kapsamlı gelir tablosu) sunabilir.",
  "TMS 1 - sunum seçeneği")

q("Diğer kapsamlı gelir kalemlerinin gruplandırılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Sonradan kâr veya zarara yeniden sınıflandırılacak olanlar ile sınıflandırılmayacak olanlar ayrı gruplanır",
  ["Tüm diğer kapsamlı gelir kalemleri her hâlde sonradan kâr veya zarara aktarılmak zorundadır",
   "Diğer kapsamlı gelir kalemleri hiçbir biçimde gruplandırılmaz; tek toplam hâlinde sunulur",
   "Gruplandırma yalnızca vergi mevzuatına göre yapılır; standartların bu konuda hükmü yoktur",
   "Diğer kapsamlı gelir kalemlerinin hiçbiri sonradan kâr veya zarara aktarılamamaktadır"],
  "TMS 1: diğer kapsamlı gelir bölümündeki kalemler; (a) sonradan kâr veya zarara yeniden sınıflandırılmayacak olanlar ve (b) belirli koşullar sağlandığında sonradan kâr veya zarara yeniden sınıflandırılacak olanlar biçiminde gruplandırılır.",
  "TMS 1 - DKG gruplandırması")

q("Olağanüstü kalem sunumu bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme hiçbir gelir veya gider kalemini olağanüstü kalem olarak sunamaz",
  ["İşletme olağandışı gelir ve giderleri olağanüstü kalem başlığı altında sunmak zorundadır",
   "Olağanüstü kalem sunumu yalnızca büyük tutarlı işlemler için zorunlu tutulmuş bir uygulamadır",
   "Olağanüstü kalemler yalnızca dipnotlarda gösterilir; tablolarda hiçbir biçimde yer almaz",
   "Olağanüstü kalem sunulup sunulmayacağı tümüyle işletmenin serbest tercihine bırakılmıştır"],
  "TMS 1: işletme hiçbir gelir ve gider kalemini kâr veya zarar tablosunda, diğer kapsamlı gelir bölümünde veya dipnotlarda olağanüstü kalem olarak sunamaz.",
  "TMS 1 - olağanüstü kalem yasağı")

q("Giderlerin sunum biçimi bakımından aşağıdakilerden hangisi doğrudur?",
  "Giderler, niteliklerine göre veya işlevlerine göre yapılan sınıflandırmadan güvenilir ve daha uygun olanına göre sunulur",
  ["Giderler yalnızca niteliklerine göre sunulabilir; işlevsel sınıflandırma yasaklanmış durumdadır",
   "Giderler yalnızca işlevlerine göre sunulabilir; nitelik esaslı sunum hiç kullanılamamaktadır",
   "Giderlerin sunum biçimi standartta düzenlenmemiş olup her işletme rastgele karar vermektedir",
   "Giderler hiçbir sınıflandırma yapılmaksızın tek bir toplam olarak sunulmak zorunda tutulmuştur"],
  "TMS 1: işletme giderlerin analizini, güvenilir ve daha ihtiyaca uygun olduğuna bağlı olarak giderlerin niteliğine (amortisman, hammadde, personel gideri) veya işletme içindeki işlevine (satışların maliyeti, pazarlama, genel yönetim) göre yapılan sınıflandırmayı esas alarak sunar.",
  "TMS 1 - gider sunumu")

q("Giderlerin işlevine göre sunum yapan işletme bakımından aşağıdakilerden hangisi doğrudur?",
  "Amortisman ve personel giderleri dâhil giderlerin niteliğine ilişkin ilave bilgi açıklar",
  ["Giderlerin niteliğine ilişkin hiçbir ilave bilgi açıklamasına gerek bulunmamaktadır",
   "İşlevsel sunum yapan işletme ayrıca nitelik esaslı tam bir gelir tablosu daha düzenlemelidir",
   "İşlevsel sunum yapılırsa amortisman gideri hiçbir yerde gösterilmez ve açıklanmaz",
   "İşlevsel sunum yapan işletme finansal tablo dipnotu düzenlemekten muaf tutulmaktadır"],
  "TMS 1: giderleri işlevlerine göre sınıflandıran işletme, amortisman ve itfa giderleri ile çalışanlara sağlanan fayda giderleri dâhil olmak üzere giderlerin niteliğine ilişkin ilave bilgi açıklar.",
  "TMS 1 - işlevsel sunum ve ek açıklama")

q("Kâr veya zarar bölümünde sunulacak bilgiler bakımından aşağıdakilerden hangisi doğrudur?",
  "Hasılat, finansman maliyetleri ve vergi gideri gibi asgari kalemler kâr veya zarar bölümünde sunulur",
  ["Kâr veya zarar bölümünde yalnızca tek bir net kâr rakamı sunulur; hiçbir alt kalem gösterilmez",
   "Kâr veya zarar bölümünde sunulacak kalemler standartta belirlenmemiş olup serbest bırakılmıştır",
   "Kâr veya zarar bölümünde yalnızca vergi gideri sunulur; hasılat bu bölümde gösterilmemektedir",
   "Kâr veya zarar bölümü tablolarda yer almaz; yalnızca dipnotlarda açıklanmak zorundadır"],
  "TMS 1: kâr veya zarar bölümünde hasılat, finansman maliyetleri, özkaynak yöntemiyle muhasebeleştirilen yatırımların kâr/zarar payları, vergi gideri gibi asgari kalemler sunulur.",
  "TMS 1 - kâr/zarar bölümü kalemleri")

q("Kâr veya zararın dağılımının sunumu bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönem kâr veya zararı; kontrol gücü olmayan paylara ve ana ortaklık sahiplerine ait kısımlar olarak gösterilir",
  ["Dönem kârı tek bir toplam olarak gösterilir; hiçbir biçimde dağılımı sunulmamaktadır",
   "Dönem kârı yalnızca kontrol gücü olmayan paylara ait kısım olarak gösterilmek zorundadır",
   "Kâr dağılımı yalnızca özkaynak değişim tablosunda gösterilir; gelir tablosunda gösterilmez",
   "Kârın dağılımının sunulması yalnızca vergi idaresinin talebi hâlinde zorunlu tutulmaktadır"],
  "TMS 1: işletme, dönem kâr veya zararı ile toplam kapsamlı geliri; kontrol gücü olmayan paylara ve ana ortaklık sahiplerine atfedilen tutarlar olarak ayrıştırıp sunar.",
  "TMS 1 - kârın dağılımı")

q("Aşağıdakilerden hangileri TMS 1'e göre doğrudur?\n\nI. Toplam kapsamlı gelir, kâr/zarar ile diğer kapsamlı gelirin toplamıdır\n\nII. Gelir ve giderler tek tabloda veya iki tabloda sunulabilir\n\nIII. Olağanüstü kalem başlığı altında sunum yapılabilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Toplam kapsamlı gelir kâr/zarar ile DKG toplamıdır (I) ve sunum tek ya da iki tabloyla yapılabilir (II). Ancak hiçbir kalem olağanüstü kalem olarak sunulamaz; bu nedenle III yanlıştır.",
  "TMS 1 - kapsamlı gelir")

q("Aşağıdaki ifadelerden hangileri gider sunumu bakımından doğrudur?\n\nI. Giderler niteliğine göre sunulabilir\n\nII. Giderler işlevine göre sunulabilir\n\nIII. İşlevsel sunumda nitelik bilgisi ayrıca açıklanır",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Giderler niteliğine (I) veya işlevine (II) göre sunulabilir; işlevsel sunum yapılırsa amortisman ve personel gideri gibi nitelik bilgisi ayrıca açıklanır (III). Üçü de doğrudur.",
  "TMS 1 - gider sunumu")

q("Bir işletme yeniden değerleme fazlasını gelir tablosunda kâr olarak göstermek istemektedir. TMS 1 bakımından aşağıdakilerden hangisi doğrudur?",
  "İlgili TFRS bu kalemi diğer kapsamlı gelirde göstermeyi gerektiriyorsa kâr veya zarara dâhil edilemez",
  ["Yeniden değerleme fazlası her hâlde kâr veya zarara dâhil edilerek dönem kârını artırmaktadır",
   "İşletme dilediği kalemi kâr veya zarara ya da diğer kapsamlı gelire serbestçe koyabilmektedir",
   "Yeniden değerleme fazlası hiçbir tabloda gösterilmez; yalnızca dipnotta açıklanmak zorundadır",
   "Yeniden değerleme fazlası doğrudan borç olarak sınıflandırılır ve yabancı kaynaklarda gösterilir"],
  "TMS 1: gelir ve gider kalemleri, diğer TFRS'ler aksini gerektirmedikçe kâr veya zarara dâhil edilir. TMS 16 uyarınca yeniden değerleme fazlası diğer kapsamlı gelirde muhasebeleştirilir; işletmenin serbest tercihi yoktur.",
  "TMS 1 - DKG (senaryo)")

# ── E. Dipnotlar (10) ──────────────────────────────────────────────────────
q("Dipnotların işlevi bakımından aşağıdakilerden hangisi doğrudur?",
  "Tabloların hazırlanma esaslarını, uygulanan muhasebe politikalarını ve tablolarda sunulmayan diğer bilgileri açıklar",
  ["Dipnotlar yalnızca işletmenin reklam ve tanıtım bilgilerini içeren bir bölüm niteliğindedir",
   "Dipnotlar finansal tabloların parçası değildir; yalnızca isteğe bağlı bir ek belgedir",
   "Dipnotlarda yalnızca gelecek dönem tahminleri yer alır; geçmiş bilgiler hiç açıklanmaz",
   "Dipnotların içeriği standartta düzenlenmemiş olup her işletme dilediğini yazabilmektedir"],
  "TMS 1: dipnotlar; finansal tabloların hazırlanma esasları ile uygulanan muhasebe politikalarına ilişkin bilgileri, TFRS'lerin gerektirdiği ancak tablolarda sunulmayan bilgileri ve tabloların anlaşılması için gerekli diğer bilgileri sunar.",
  "TMS 1 - dipnotların işlevi")

q("Dipnotların sunum sırası bakımından aşağıdakilerden hangisi doğrudur?",
  "Dipnotlar uygulanabilir olduğu ölçüde sistematik biçimde sunulur ve her kalem ilgili dipnota çapraz referans verir",
  ["Dipnotlar hiçbir düzen gözetmeksizin rastgele sıralanır ve çapraz referans verilmemektedir",
   "Dipnotlar yalnızca alfabetik sıraya göre dizilmek zorunda olup başka bir düzen kullanılamaz",
   "Dipnotların sırası vergi idaresince her yıl yeniden belirlenip işletmelere bildirilmektedir",
   "Dipnotlarda çapraz referans verilmesi finansal tabloları geçersiz kılan bir uygulamadır"],
  "TMS 1: işletme dipnotları, uygulanabilir olduğu ölçüde sistematik biçimde sunar ve finansal tablolardaki her kalem için ilgili dipnota çapraz referans verir.",
  "TMS 1 - dipnot düzeni")

q("Önemli muhasebe politikası bilgilerinin açıklanması bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme önemli muhasebe politikası bilgilerini açıklar; politika bilgisi işlemin niteliği veya tutarı nedeniyle önemli olabilir",
  ["İşletme hiçbir muhasebe politikasını açıklamaz; politikalar gizli tutulmak zorundadır",
   "İşletme tüm muhasebe politikalarını önemli olup olmadığına bakmaksızın açıklamak zorundadır",
   "Muhasebe politikaları yalnızca denetçiye bildirilir; dipnotlarda açıklanmamaktadır",
   "Muhasebe politikası açıklaması yalnızca politika değiştiğinde yapılır; ilk yıl açıklanmaz"],
  "TMS 1: işletme önemli muhasebe politikası bilgilerini açıklar. Muhasebe politikası bilgisi, ilgili olduğu işlemlerin/olayların tutarı nedeniyle veya niteliği nedeniyle önemli olabilir.",
  "TMS 1 - muhasebe politikalarının açıklanması")

q("Muhasebe politikası uygularken yapılan muhakemelerin açıklanması bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal tablolardaki tutarlar üzerinde en önemli etkisi olan muhakemeler açıklanır",
  ["Yönetimin yaptığı muhakemeler hiçbir hâlde açıklanmaz; yalnızca sonuç tutarlar gösterilir",
   "Yönetimin her türlü muhakemesi, önemsiz olanlar dâhil eksiksiz biçimde açıklanmak zorundadır",
   "Muhakemeler yalnızca vergi idaresine bildirilir; finansal tablo kullanıcılarına açıklanmaz",
   "Muhakeme yapılması yasaktır; tüm tutarlar kesin ve muhakemesiz belirlenmek zorundadır"],
  "TMS 1: işletme, muhasebe politikalarını uygularken yönetimin yaptığı ve finansal tablolara alınan tutarlar üzerinde en önemli etkisi olan muhakemeleri (tahminleri içerenler hariç) önemli muhasebe politikası bilgileriyle birlikte açıklar.",
  "TMS 1 - muhakemelerin açıklanması")

q("Tahmin belirsizliği kaynaklarının açıklanması bakımından aşağıdakilerden hangisi doğrudur?",
  "Sonraki dönemde önemli düzeltme riski taşıyan varsayımlara ve belirsizlik kaynaklarına ilişkin bilgi açıklanır",
  ["Tahmin belirsizlikleri hiçbir biçimde açıklanmaz; yalnızca kesin tutarlar raporlanmaktadır",
   "Tahmin belirsizliği yalnızca işletme zarar ettiğinde açıklanır; kâr hâlinde açıklanmamaktadır",
   "Tahmin belirsizliği açıklaması yalnızca denetçinin raporunda yer alır; dipnotlarda bulunmaz",
   "Tahmin yapılması standartlarda yasaklanmış olup tüm tutarlar kesin biçimde ölçülmektedir"],
  "TMS 1: işletme, sonraki dönemde varlık ve borçların defter değerlerinde önemli düzeltme riski oluşturan geleceğe ilişkin varsayımlar ve tahmin belirsizliğinin diğer önemli kaynaklarına ilişkin bilgi açıklar.",
  "TMS 1 - tahmin belirsizliği")

q("Sermayenin yönetimine ilişkin açıklama bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme, sermayeyi yönetme amaç, politika ve süreçlerini değerlendirebilmeleri için kullanıcılara bilgi açıklar",
  ["Sermaye yönetimine ilişkin hiçbir bilgi açıklanmaz; bu bilgi ticari sır kabul edilmektedir",
   "Sermaye yönetimi bilgisi yalnızca ortaklara sözlü olarak bildirilir; dipnotta yer almaz",
   "Sermaye yönetimi açıklaması yalnızca işletme sermaye artırımı yaptığında zorunlu tutulmuştur",
   "Sermaye yönetimi kavramı TMS 1'de düzenlenmemiş olup uygulamada kullanılmamaktadır"],
  "TMS 1: işletme, kullanıcıların sermayeyi yönetme amaç, politika ve süreçlerini değerlendirebilmesini sağlayacak bilgi açıklar.",
  "TMS 1 - sermaye yönetimi açıklaması")

q("Kâr payına ilişkin açıklama bakımından aşağıdakilerden hangisi doğrudur?",
  "Tabloların yayımı için onaylanmadan önce teklif edilen ancak dönemde dağıtım olarak muhasebeleştirilmeyen kâr payı tutarı açıklanır",
  ["Kâr payına ilişkin hiçbir bilgi açıklanmaz; kâr dağıtımı finansal tabloları ilgilendirmez",
   "Teklif edilen kâr payı her hâlde dönemin gideri olarak kâr veya zarara yansıtılmak zorundadır",
   "Kâr payı bilgisi yalnızca vergi idaresine bildirilir; dipnotlarda açıklanmamaktadır",
   "Kâr payı yalnızca dağıtıldıktan on yıl sonra ve geriye dönük olarak açıklanabilmektedir"],
  "TMS 1: işletme, finansal tabloların yayımı için onaylanmadan önce teklif edilen veya ilan edilen ancak dönem içinde ortaklara dağıtım olarak muhasebeleştirilmeyen kâr payı tutarını ve bunun pay başına tutarını açıklar.",
  "TMS 1 - kâr payı açıklaması")

q("Aşağıdakilerden hangileri TMS 1'e göre dipnotlarda açıklanır?\n\nI. Uygulanan önemli muhasebe politikaları\n\nII. Tahmin belirsizliğinin önemli kaynakları\n\nIII. Sermaye yönetimine ilişkin bilgiler",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Dipnotlarda; önemli muhasebe politikaları (I), tahmin belirsizliğinin önemli kaynakları (II) ve sermaye yönetimine ilişkin bilgiler (III) açıklanır. Üçü de doğrudur.",
  "TMS 1 - dipnot açıklamaları")

q("Aşağıdaki ifadelerden hangileri dipnotlar bakımından doğrudur?\n\nI. Dipnotlar sistematik biçimde sunulur\n\nII. Tablolardaki kalemler ilgili dipnota çapraz referans verir\n\nIII. Dipnotlar finansal tablo setinin parçası değildir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Dipnotlar sistematik sunulur (I) ve kalemler çapraz referans verir (II). Dipnotlar tam finansal tablo setinin ayrılmaz parçasıdır; bu nedenle III yanlıştır.",
  "TMS 1 - dipnotlar")

q("Bir işletme, önemli olmayan bir muhasebe politikası bilgisini dipnotlarda açıklamamıştır. TMS 1 bakımından aşağıdakilerden hangisi doğrudur?",
  "Önemli olmayan muhasebe politikası bilgisinin açıklanması zorunlu değildir",
  ["Tüm muhasebe politikaları, önemsiz olanlar dâhil her hâlde açıklanmak zorunda tutulmuştur",
   "Politika açıklanmadığı için finansal tablolar kendiliğinden geçersiz hâle gelmektedir",
   "Önemsiz politikalar açıklanmazsa TFRS'lere uygunluk beyanı yapılması yasaklanmaktadır",
   "Muhasebe politikalarının açıklanması yalnızca denetçinin talebine bağlı bir uygulamadır"],
  "TMS 1: işletme önemli muhasebe politikası bilgilerini açıklar. Önemli olmayan muhasebe politikası bilgisinin açıklanması gerekmez; ancak önemsiz bilgi, önemli bilgiyi gizleyecek biçimde sunulmamalıdır.",
  "TMS 1 - önemlilik (senaryo)")

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
                       "styleRef": "SGS Muhasebe Standartları (TMS 1; yapısal)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    hepsi = sum(1 for x in onc if x["options"][x["answer"]].strip() == "I, II ve III")
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} hepsi {hepsi} | harf {''.join(x['answer'] for x in out)[:40]}…")
