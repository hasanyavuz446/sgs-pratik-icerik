# -*- coding: utf-8 -*-
"""Muhasebe Denetimi · Önemlilik ve Örnekleme — 60 soru, 2026 test biçimi.

Gerçek 2026/1 kitapçığında BDS 200/320 önemlilik tanımından (“bütün açısından önemli olmayan yanlışlıkların tespitinden
sorumlu değildir”) “hangisi yanlıştır” biçiminde soru sorulmuştur.

Dayanak (28.09.2026 kontrolü, kgk.gov.tr güncel metinler):
  · BDS 320 Bağımsız Denetimin Planlanması ve Yürütülmesinde Önemlilik
  · BDS 450 Bağımsız Denetimin Yürütülmesi Sırasında Belirlenen Yanlışlıkların Değerlendirilmesi
  · BDS 530 Bağımsız Denetimde Örnekleme
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_onemlilik_ve_ornekleme_2026.json", lesson="denetim", topic="onemlilik_ve_ornekleme",
          konu_adi="Önemlilik ve Örnekleme", seed=2026092847,
          surum="BDS 320, BDS 450, BDS 530 güncel metinleri; 28.09.2026 kontrolü")

B320 = "BDS 320 “Bağımsız Denetimin Planlanması ve Yürütülmesinde Önemlilik”e göre"
B450 = "BDS 450 “Denetim Sırasında Belirlenen Yanlışlıkların Değerlendirilmesi”ne göre"
B530 = "BDS 530 “Bağımsız Denetimde Örnekleme”ye göre"

# ================================================================ BDS 320
P.q("BDS 320 prg. 2",
    f"{B320}, önemlilik kavramına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Önemlilik sadece yanlışlığın tutarına göre belirlenir; niteliği dikkate alınmaz.",
    ["Yanlışlıklar kullanıcıların ekonomik kararlarını etkilemesi makul ölçüde bekleniyorsa önemlidir.",
     "Önemliliğe ilişkin yargılara içinde bulunulan şartlar ışığında ulaşılır.",
     "Önemlilik yargıları, kullanıcıların finansal bilgi ihtiyaçlarına ilişkin algıdan etkilenir.",
     "Kullanıcıların ortak finansal bilgi ihtiyaçları grup olarak dikkate alınır."],
    "BDS 320 prg. 2'ye göre yanlışlıklar kullanıcıların ekonomik kararlarını etkilemesi makul ölçüde bekleniyorsa önemlidir; "
    "yargılara şartlar ışığında ulaşılır ve bunlar yanlışlığın büyüklüğünden, niteliğinden veya ikisinin birleşiminden "
    "etkilenir. Kullanıcıların ortak bilgi ihtiyaçları grup olarak dikkate alınır.")

P.q("BDS 320 prg. 4",
    f"{B320}, önemliliğin belirlenmesinde denetçinin dikkate aldığı “kullanıcılar”a ilişkin varsayımlar arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Kullanıcıların finansal tabloları sadece vergi beyanı amacıyla incelediği",
    ["İşletme faaliyetleri ile muhasebe hakkında makul bilgiye sahip oldukları",
     "Tabloları makul bir özenle incelemeye istekli oldukları",
     "Tabloların önemlilik düzeylerine göre hazırlanıp denetlendiğini anladıkları",
     "Tahminlerin belirsizlik içerdiğini ve gelecekteki olaylara bağlı olduğunu anladıkları"],
    "BDS 320 prg. 4'e göre denetçi kullanıcıların işletme faaliyetleri ve muhasebe hakkında makul bilgiye sahip olduğunu, "
    "tabloları özenle incelemeye istekli olduğunu, önemlilik düzeyine göre hazırlama ve denetimi anladığını, tahminlerin "
    "belirsizlik içerdiğini kabul ettiğini ve tablolara dayanarak makul ekonomik kararlar aldığını varsayar.")

P.q("BDS 320 prg. 9",
    f"{B320}, “performans önemliliği” aşağıdakilerden hangisidir?",
    "Toplam yanlışlığın genel önemliliği aşma ihtimalini düşürmek için belirlenen daha düşük tutar",
    ["Bir bütün olarak finansal tablolar için belirlenen en yüksek kabul edilebilir yanlışlık tutarı",
     "Altında kalan yanlışlıkların bir araya getirilmediği tutar",
     "Denetim ekibinin performansını ölçmek için belirlenen saat ve maliyet sınırı",
     "Yönetimin düzeltmeyi reddettiği yanlışlıkların toplam tutarı"],
    "BDS 320 prg. 9'a göre performans önemliliği, düzeltilmemiş ve tespit edilmemiş yanlışlıklar toplamının bütün olarak "
    "tablolar için belirlenen önemliliği aşması ihtimalini uygun bir düşük seviyeye indirmek için, önemlilikten düşük olarak "
    "belirlenen tutar veya tutarlardır.", zorluk="easy")

P.q("BDS 320 prg. 10",
    f"{B320}, genel önemlilikten daha düşük tutarlardaki yanlışlıkların bile kullanıcı kararlarını etkileyebileceği "
    "özel işlem sınıfları için denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Bu kalemler için ayrıca önemlilik düzeyi belirler.",
    ["Bu kalemleri denetim kapsamından çıkarır ve yönetime bildirir.",
     "Genel önemliliği bu kalemlerin tutarına göre yeniden yükseltir.",
     "Bu kalemler için önemlilik belirlemez; tüm işlemleri inceler.",
     "Bu kalemlerin önemliliğini yönetimin belirlemesini ister."],
    "BDS 320 prg. 10'a göre kullanıcıların kararlarını etkileyeceği makul şekilde beklenen, genel önemlilikten düşük "
    "tutarlardaki yanlışlıkları içerebilecek işlem sınıfı, bakiye veya açıklamalar varsa denetçi bunlara uygulanmak üzere "
    "ayrıca önemlilik düzeyi veya düzeyleri belirler (ör. ilişkili taraf işlemleri, üst yönetim ücretleri).")

P.q("BDS 320 prg. 10",
    f"{B320}, genel denetim stratejisi oluşturulurken bir bütün olarak finansal tablolar için önemliliği kimin "
    "belirlemesi gerekir?",
    "Denetçinin",
    ["Yönetimin", "Üst yönetimin", "KGK'nın", "Denetim komitesinin"],
    "BDS 320 prg. 10'a göre denetçi genel denetim stratejisini oluştururken bir bütün olarak finansal tablolar için "
    "önemliliği belirler; A3'e göre bu belirleme mesleki muhakeme gerektirir.", zorluk="easy")

P.q("BDS 320 prg. 11, A12",
    f"{B320}, performans önemliliği belirlenmesinin gerekçesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Münferit önemsiz yanlışlıklar toplandığında tabloları önemli ölçüde yanlış gösterebilir.",
    ["Performans önemliliği sadece yönetimin talebi üzerine belirlenir.",
     "Performans önemliliği, tespit edilmemiş yanlışlıkların dikkate alınmamasını sağlar.",
     "Denetimi sadece münferit önemli yanlışlıklara yönelik planlamak yeterli olduğundan belirlenir.",
     "Performans önemliliği genel önemlilikten daha yüksek belirlenir."],
    "BDS 320 A12'ye göre denetimi sadece münferit olarak önemli yanlışlıkları tespit edecek şekilde planlamak, münferit "
    "önemsiz yanlışlıkların toplu olarak önemli olabileceğini göz ardı eder ve tespit edilmemiş yanlışlıklar için marj "
    "bırakmaz; performans önemliliği bu nedenle önemlilikten düşük belirlenir.")

P.q("BDS 320 A3",
    f"{B320}, önemliliğin belirlenmesinde uygun kıyaslama noktasının seçimini etkileyen faktörler arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Denetim şirketinin önceki yıl bu müşteriden aldığı ücret",
    ["Varlıklar, borçlar, özkaynak ve hasılat gibi tablo unsurları",
     "Kullanıcıların dikkatinin odaklandığı kalemlerin bulunup bulunmadığı",
     "İşletmenin niteliği, yaşam döngüsündeki yeri ve faaliyet gösterdiği sektör",
     "İşletmenin ortaklık yapısı ve nasıl finanse edildiği"],
    "BDS 320 A3'e göre kıyaslama noktası seçimini tablo unsurları, kullanıcıların odaklandığı kalemler, işletmenin niteliği "
    "ve yaşam döngüsü, sektör ve ekonomik çevre, ortaklık ve finansman yapısı ile kıyaslama noktasının göreli "
    "değişkenliği etkiler. Denetim ücreti bu faktörlerden değildir.")

P.sayisal("BDS 320 A7",
    "Üretim sektöründe faaliyet gösteren kâr amaçlı bir işletmenin sürdürülen faaliyetlerden elde ettiği vergi öncesi "
    f"kârı 12.400.000 ₺'dir. {B320} uygulama hükümlerinde örnek olarak verilen oran esas alınırsa bir bütün olarak "
    "finansal tablolar için önemlilik kaç ₺ olur?",
    "620.000 ₺", ["124.000 ₺", "310.000 ₺", "1.240.000 ₺", "248.000 ₺"],
    "BDS 320 A7'de örnek olarak üretim sektöründeki kâr amaçlı bir işletme için sürdürülen faaliyetlerden elde edilen vergi "
    "öncesi kârın yüzde beşinin esas alınabileceği belirtilir: 12.400.000 × %5 = 620.000 ₺. Oran mesleki muhakemeye "
    "bağlıdır; şartlara göre daha yüksek veya düşük oran da uygun olabilir.", zorluk="easy")

P.q("BDS 320 A7",
    f"{B320}, önemlilik için kıyaslama noktasına uygulanacak oranın belirlenmesine ilişkin aşağıdaki ifadelerden "
    "hangisi yanlıştır?",
    "Hasılata uygulanan oran, kâra uygulanan orandan genellikle yüksektir.",
    ["Oranın belirlenmesi mesleki muhakeme kullanılmasını gerektirir.",
     "Uygulanacak oran ile seçilen kıyaslama noktası arasında bir ilişki vardır.",
     "Kâr amacı gütmeyen işletmelerde toplam hasılatın veya giderlerin yüzde biri uygun olabilir.",
     "Şartlara göre örnekte verilenden daha yüksek veya daha düşük oranlar da kabul edilebilir."],
    "BDS 320 A7'ye göre oranın belirlenmesi mesleki muhakemedir ve kıyaslama noktasıyla ilişkilidir: vergi öncesi kâra "
    "uygulanan oran toplam hasılata uygulanan orandan genellikle daha yüksektir (ör. kârın %5'i, kâr amacı gütmeyenlerde "
    "hasılatın veya giderlerin %1'i). Şartlara göre farklı oranlar da uygun olabilir.", zorluk="hard")

P.q("BDS 320 A4",
    f"{B320}, sürdürülen faaliyetlerden elde edilen vergi öncesi kârı yıldan yıla büyük dalgalanma gösteren bir işletmede "
    "önemliliğin belirlenmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Brüt kâr veya toplam hasılat gibi farklı bir kıyaslama noktası uygun olabilir.",
    ["Kâr değişken olsa da vergi öncesi kâr kıyaslama noktası olarak kullanılmakır.",
     "Zarar eden işletmelerde önemlilik belirlenmez ve tüm işlemler incelenir.",
     "Önemlilik, bir önceki yılın denetim raporundaki tutar aynen alınarak belirlenir.",
     "Önemlilik, işletmenin ödenmiş sermayesinin sabit bir yüzdesi olarak belirlenir."],
    "BDS 320 A4'e göre vergi öncesi kâr genellikle kâr amaçlı işletmelerde kullanılır; kâr değişkense brüt kâr veya "
    "toplam hasılat gibi diğer kıyaslama noktaları daha uygun olabilir. A5'e göre kıyaslama noktası için önceki dönem "
    "sonuçları ve bütçeler de kullanılabilir.")

P.q("BDS 320 prg. 12-13",
    "Denetim sırasında denetçi, işletmenin planlamada kullanılan tahmini kârının gerçekleşen kârın iki katı olduğunu "
    f"öğrenmiştir. {B320} denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Önemliliği değiştirir ve prosedürlerin uygunluğunu yeniden değerlendirir.",
    ["Planlama tamamlandığından önemliliği değiştirmez ve farkı gelecek yıla not eder.",
     "Önemliliği yükselterek test edilecek kalemleri azaltır.",
     "Önemliliği değiştirmez, ancak raporunda bu durumu açıklar.",
     "Önemliliğin yeniden belirlenmesi için yönetimin onayını alır."],
    "BDS 320 prg. 12'ye göre başlangıçta farklı bir önemlilik belirlemesine yol açacak bilgi edinilirse önemlilik "
    "değiştirilir. Prg. 13'e göre daha düşük önemlilik uygunsa performans önemliliğinin ve uygulanan veya uygulanacak "
    "prosedürlerin niteliği, zamanlaması ve kapsamının hâlâ uygun olup olmadığına karar verilir.", zorluk="hard")

P.q("BDS 320 prg. 14",
    f"{B320}, aşağıdakilerden hangisi önemliliğe ilişkin çalışma kâğıtlarına dahil edilmesi gerekenler arasında "
    "yer almaz?",
    "Önemliliğin yönetim tarafından onaylandığını gösteren imzalı belge",
    ["Bir bütün olarak finansal tablolar için belirlenen önemlilik",
     "Uygun hâllerde belirli kalemler için belirlenen önemlilik düzeyleri",
     "Performans önemliliği",
     "Denetim yürütülürken bu tutarlarda yapılan değişiklikler"],
    "BDS 320 prg. 14'e göre denetçi; bütün olarak tablolar için önemliliği, belirli kalemler için önemlilik düzeylerini, "
    "performans önemliliğini, denetim sırasındaki değişiklikleri ve bunların belirlenmesinde dikkate alınan faktörleri "
    "belgelendirir. Önemlilik denetçinin muhakemesidir; yönetim onayı gerekmez.")

P.q("BDS 320 prg. 5",
    f"{B320}, denetçinin belirlediği önemlilik ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Önemliliğin altında kalan düzeltilmemiş yanlışlıklar, niteliklerine bakılmaksızın önemsiz kabul edilir.",
    ["Önemlilik, denetimin planlanması ve yürütülmesinde ve yanlışlıkların etkisinin değerlendirilmesinde uygulanır.",
     "Planlamada belirlenen önemlilik, düzeltilmemiş yanlışlıkların önemsiz olarak değerlendirileceği bir tutar değildir.",
     "Önemliliğin altında olsa bile bazı yanlışlıklar koşulları nedeniyle önemli sayılabilir.",
     "Denetçinin önemliliği belirlemesi mesleki muhakeme gerektirir."],
    "BDS 320 prg. 5-6'ya göre önemlilik planlama, yürütme ve yanlışlıkların değerlendirilmesinde uygulanır. Planlamada "
    "belirlenen önemlilik, altındaki düzeltilmemiş yanlışlıkların her zaman önemsiz sayılacağı bir tutar değildir; bazı "
    "yanlışlıklar koşulları nedeniyle tutarı düşük olsa da önemli olabilir (BDS 450 A16).")

# ================================================================ BDS 450
P.q("BDS 450 prg. 5",
    f"{B450}, denetim boyunca belirlenen yanlışlıkların bir araya getirilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bariz biçimde önemsiz olanlar dışındakiler bir araya getirilir.",
    ["Sadece önemliliği aşan yanlışlıklar bir araya getirilir.",
     "Tüm yanlışlıklar, tutarına bakılmaksızın ayrı ayrı raporlanır.",
     "Sadece yönetimin kabul ettiği yanlışlıklar bir araya getirilir.",
     "Yanlışlıklar sadece denetimin sonunda bir kez bir araya getirilir."],
    "BDS 450 prg. 5'e göre denetçi, denetim boyunca belirlediği bariz biçimde önemsiz sayılanlar dışındaki yanlışlıkları "
    "bir araya getirir; prg. 15-a'ya göre bu eşik tutarı belgelendirilir.", zorluk="easy")

P.q("BDS 450 A2",
    f"{B450}, “bariz biçimde önemsiz” yanlışlıklara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bariz biçimde önemsiz, “önemli değil” ifadesiyle aynı anlamdadır.",
    ["Bariz biçimde önemsiz yanlışlıklar, önemlilikten tamamen farklı ve daha küçük büyüklükteki yanlışlıklardır.",
     "Bu yanlışlıklar tek başına veya toplu olarak tablolar üzerinde açıkça sonuçsuzdur.",
     "Bir yanlışlığın bariz biçimde önemsiz olup olmadığı konusunda belirsizlik varsa önemsiz sayılmaz.",
     "Bariz biçimde önemsiz tutarın altındaki yanlışlıkların bir araya getirilmesi gerekmez."],
    "BDS 450 A2'ye göre bariz biçimde önemsiz, “önemli değil” ile aynı anlama gelmez; önemlilikten tamamen farklı ve daha "
    "küçük büyüklükteki, tek başına veya toplu olarak açıkça sonuçsuz yanlışlıkları ifade eder. Belirsizlik varsa "
    "yanlışlık bariz biçimde önemsiz sayılmaz.", zorluk="hard")

P.q("BDS 450 prg. 6",
    f"{B450}, aşağıdaki durumlardan hangisinde denetçi genel denetim stratejisi ile denetim planının revize edilmesinin "
    "gerekip gerekmediğine karar verir?",
    "Bir araya getirilen yanlışlıklar toplamının önemliliğe yaklaşması",
    ["Yönetimin bir yanlışlığı düzeltmeyi kabul etmesi",
     "Bariz biçimde önemsiz bir yanlışlığın tespit edilmesi",
     "Denetim ekibinden bir denetçinin izne ayrılması ve yerine yedeğin geçmesi",
     "Önceki yıl denetim raporunun olumlu görüş içermesi"],
    "BDS 450 prg. 6'ya göre yanlışlıkların niteliği ve şartları toplanınca önemli olabilecek başka yanlışlıklar "
    "bulunabileceğini gösteriyorsa veya bir araya getirilen yanlışlıklar toplamı önemliliğe yaklaşıyorsa denetçi, strateji "
    "ve planın revize edilmesinin gerekip gerekmediğine karar verir.")

P.q("BDS 450 prg. 7",
    "Denetçinin talebi üzerine yönetim, ticari alacaklar hesabını yeniden incelemiş ve tespit ettiği yanlışlıkları "
    f"düzeltmiştir. {B450} bu durumda denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Kalan yanlışlık için ilave prosedür uygular.",
    ["Yönetimin düzeltmesini yeterli sayar ve hesabı ek test yapmadan kapatır.",
     "Hesabı yeniden test etmez; sadece yazılı açıklama alır.",
     "Düzeltmeleri kendisi yeniden kaydederek hesabı onaylar.",
     "Düzeltme yapıldığı için hesabı denetim kapsamından çıkarır."],
    "BDS 450 prg. 7'ye göre talebi üzerine yönetimin bir işlem sınıfını, hesap bakiyesini veya açıklamayı inceleyip tespit "
    "ettiği yanlışlıkları düzeltmesi hâlinde denetçi, yanlışlıkların kalıp kalmadığına karar vermek için ilave denetim "
    "prosedürleri uygular.")

P.q("BDS 450 prg. 8-9",
    f"{B450}, yanlışlıkların bildirilmesi ve düzeltilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yönetim düzeltmeyi reddederse denetçi gerekçeleri sormadan olumsuz görüş verir.",
    ["Mevzuat yasaklamadıkça bir araya getirilen tüm yanlışlıklar yönetimin uygun kademesine zamanında bildirilir.",
     "Denetçi, yönetimden bildirilen yanlışlıkları düzeltmesini talep eder.",
     "Yönetim düzeltmeyi reddederse denetçi düzeltmeme gerekçelerini anlar.",
     "Denetçi, tabloların önemli yanlışlık içerip içermediğini değerlendirirken yönetimin gerekçelerini dikkate alır."],
    "BDS 450 prg. 8'e göre mevzuat yasaklamadıkça tüm yanlışlıklar yönetimin uygun kademesine zamanında bildirilir ve "
    "düzeltme talep edilir. Prg. 9'a göre yönetim reddederse denetçi gerekçeleri anlar ve bunu tabloların önemli yanlışlık "
    "içerip içermediğini değerlendirirken dikkate alır; görüş, düzeltilmemiş yanlışlıkların önemine göre belirlenir.")

P.q("BDS 450 prg. 10",
    f"{B450}, düzeltilmemiş yanlışlıkların etkisini değerlendirmeden önce denetçinin yapması gereken aşağıdakilerden "
    "hangisidir?",
    "Önemliliğin fiili sonuçlara göre hâlâ geçerli olup olmadığını yeniden değerlendirmek",
    ["Düzeltilmemiş yanlışlıkları yönetimin onayına sunarak önemsiz olduğunu kabul ettirmek",
     "Önemliliği, düzeltilmemiş yanlışlıkların toplamından daha yüksek olacak şekilde artırmak",
     "Önceki yılın düzeltilmemiş yanlışlıklarını değerlendirme dışında bırakmak",
     "Düzeltilmemiş yanlışlıkları bir sonraki yılın denetimine devretmek"],
    "BDS 450 prg. 10'a göre denetçi, düzeltilmemiş yanlışlıkların etkisini değerlendirmeden önce BDS 320'ye göre "
    "belirlenen önemliliğin işletmenin fiili finansal sonuçları kapsamında hâlâ geçerli olup olmadığını doğrulamak için "
    "önemliliği yeniden değerlendirir.")

P.q("BDS 450 prg. 11",
    f"{B450}, düzeltilmemiş yanlışlıkların önemli olup olmadığına karar verirken denetçinin mütalaa ettiği hususlar "
    "arasında aşağıdakilerden hangisi yer almaz?",
    "Yanlışlığı yapan personelin işletmedeki kıdemi ve ücret düzeyi",
    ["Yanlışlıkların belirli kalemler ve tablolar açısından büyüklüğü ve niteliği",
     "Yanlışlıkların meydana geldiği belirli şartlar",
     "Önceki dönemlere ilişkin düzeltilmemiş yanlışlıkların ilgili kalemlere etkisi",
     "Önceki dönem düzeltilmemiş yanlışlıklarının tablolar bütünü üzerindeki etkisi"],
    "BDS 450 prg. 11'e göre denetçi; yanlışlıkların belirli kalemler ve tablolar bütünü açısından büyüklüğünü, niteliğini "
    "ve meydana geldiği şartları ile önceki dönem düzeltilmemiş yanlışlıklarının etkisini mütalaa eder. Kişinin ücret "
    "düzeyi bu kapsamda değildir; ancak şartlar (ör. hile) nitelik değerlendirmesini etkileyebilir.")

P.q("BDS 450 A16",
    "Denetçi, tutarı önemliliğin altında olan bir yanlışlığın düzeltilmemesi hâlinde işletmenin kredi sözleşmesindeki "
    f"bir finansal oran şartını ihlal edeceğini tespit etmiştir. {B450} bu yanlışlığa ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Şartları nedeniyle önemlilik altında olsa da önemli sayılabilir.",
    ["Tutarı önemliliğin altında olduğundan önemsiz kabul edilir.",
     "Sözleşme ihlali denetçiyi ilgilendirmediğinden değerlendirilmez.",
     "Yanlışlık bariz biçimde önemsiz sayılarak bir araya getirilmez.",
     "Yanlışlık sadece bir sonraki yılın önemliliğini etkiler."],
    "BDS 450 A16'ya göre bazı yanlışlıklar tutarı önemliliğin altında olsa bile, sözleşme şartlarına veya mevzuata "
    "uygunluğu etkilemesi, bir kazanç eğilimini maskelemesi gibi şartlar nedeniyle önemli olarak değerlendirilebilir.",
    zorluk="hard")

P.q("BDS 450 prg. 12-13",
    f"{B450}, düzeltilmemiş yanlışlıklar hakkında üst yönetimden sorumlu olanlarla kurulacak iletişime ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Önemli olanlar münferit olarak tanımlanır ve düzeltilmeleri talep edilir.",
    ["Düzeltilmemiş yanlışlıklar üst yönetime değil, sadece yönetime bildirilir.",
     "Sadece toplam tutar bildirilir; yanlışlıklar ayrı ayrı belirtilmez.",
     "Önceki dönem düzeltilmemiş yanlışlıklarının etkisi bildirilmez.",
     "Bildirim sadece denetim raporu yayımlandıktan sonra yapılır."],
    "BDS 450 prg. 12'ye göre mevzuat yasaklamadıkça denetçi düzeltilmemiş yanlışlıkları ve görüşe olası etkisini üst "
    "yönetime bildirir, önemli olanları münferit olarak tanımlar ve düzeltilmelerini talep eder. Prg. 13'e göre önceki "
    "dönem düzeltilmemiş yanlışlıklarının etkisi de bildirilir.")

P.q("BDS 450 prg. 14",
    f"{B450}, düzeltilmemiş yanlışlıklara ilişkin yönetimden talep edilecek yazılı açıklama aşağıdakilerden hangisidir?",
    "Etkinin tablolar bütünü için önemsiz olduğu kanaatine varılıp varılmadığı",
    ["Denetçinin tespit ettiği tüm yanlışlıkların yönetimce kabul edildiği ve düzeltileceği",
     "Düzeltilmemiş yanlışlıkların bir sonraki yıl düzeltileceği taahhüdü",
     "Denetçinin önemlilik düzeyini doğru belirlediğinin onaylanması",
     "Düzeltilmemiş yanlışlıkların vergi matrahını etkilemediği"],
    "BDS 450 prg. 14'e göre denetçi, yönetimden ve uygun hâllerde üst yönetimden, düzeltilmemiş yanlışlıkların tek başına "
    "ve toplu hâlde tablolar bütünü üzerindeki etkisinin önemsiz olduğu kanaatine varıp varmadıklarına ilişkin yazılı "
    "açıklama talep eder; açıklamada veya ekinde bu kalemlerin özeti yer alır.")

P.q("BDS 450 prg. 15",
    f"{B450}, aşağıdakilerden hangisi yanlışlıkların değerlendirilmesine ilişkin çalışma kâğıtlarına dahil edilmesi "
    "gerekenler arasında yer almaz?",
    "Yanlışlıkları yapan çalışanların kimlikleri ve disiplin işlemleri",
    ["Altında kalan yanlışlıkların bariz biçimde önemsiz sayılacağı tutar",
     "Bir araya getirilen tüm yanlışlıklar ve bunların düzeltilip düzeltilmediği",
     "Düzeltilmemiş yanlışlıkların önemli olup olmadığına ilişkin sonuç",
     "Düzeltilmemiş yanlışlıklara ilişkin sonucun gerekçesi"],
    "BDS 450 prg. 15'e göre denetçi, bariz biçimde önemsiz tutarı, bir araya getirilen tüm yanlışlıkları ve düzeltilip "
    "düzeltilmediklerini ve düzeltilmemiş yanlışlıkların önemli olup olmadığına dair sonucunu ve gerekçesini belgelendirir.")

P.q("BDS 450 prg. 4-b",
    f"{B450}, aşağıdakilerden hangisi “yanlışlık” kapsamında değerlendirilmez?",
    "Denetçinin, çerçeveye uygun bir muhasebe politikası seçimini beğenmemesi",
    ["Bir kalemin tutarının çerçeveye göre olması gerekenden farklı olması",
     "Bir kalemin tabloda yanlış sınıflandırılması",
     "Çerçevenin gerektirdiği bir açıklamanın yapılmaması",
     "Gerçeğe uygun sunum için gerekli olduğu düşünülen tutar ve açıklama düzeltmeleri"],
    "BDS 450 prg. 4-b'ye göre yanlışlık; raporlanan kalemin tutarı, sınıflandırılması, sunumu veya açıklaması ile çerçeveye "
    "göre olması gereken arasındaki farktır; gerçeğe uygun sunum için gerekli görülen düzeltmeler de bu kapsamdadır. "
    "Çerçeveye uygun bir tercihin beğenilmemesi yanlışlık değildir.")

# ================================================================ BDS 530
P.q("BDS 530 prg. 5-c",
    f"{B530}, “denetim örneklemesi”nin tanımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Birimlere seçilme şansı verip kalemlerin %100'ünden azına prosedür uygulanmasıdır.",
    ["Sadece yüksek tutarlı kalemlerin seçilerek incelenmesidir.",
     "Yönetimin önerdiği kalemlerin denetçi tarafından test edilmesidir.",
     "Anakitlenin tamamının bilgisayar destekli denetim teknikleriyle eksiksiz incelenmesidir.",
     "Sadece istatistiki yöntemlerle yapılan seçimleri ifade eder."],
    "BDS 530 prg. 5-c'ye göre denetim örneklemesi, denetçinin anakitlenin tamamı hakkında sonuca varması için makul bir "
    "dayanak oluşturmak üzere, tüm örnekleme birimlerine seçilme şansı sağlayarak anakitledeki kalemlerin %100'ünden "
    "azına prosedür uygulanmasıdır; istatistiki veya istatistiki olmayan yaklaşımla yapılabilir.")

P.q("BDS 530 prg. 5-g",
    "Denetçi, örneklem sonuçlarına dayanarak bir kontrolün etkin işlediği sonucuna varmıştır; oysa anakitlenin tamamı "
    f"test edilseydi kontrolün etkin olmadığı anlaşılacaktı. {B530} bu durum aşağıdakilerden hangisidir?",
    "Denetimin etkinliğini etkileyen örnekleme riski",
    ["Denetimin verimliliğini etkileyen örnekleme riski",
     "Örnekleme dışı risk",
     "Yapısal risk",
     "Kabul edilebilir sapma oranı"],
    "BDS 530 prg. 5-g'ye göre örnekleme riski, örnekleme dayalı sonucun anakitlenin tamamına uygulansaydı varılacak "
    "sonuçtan farklı olması riskidir. Kontrolün gerçekte olduğundan daha etkin görülmesi denetimin etkinliğini etkiler ve "
    "uygun olmayan görüşe yol açabileceğinden denetçi öncelikle bu tür hatalı sonuçları ele alır.", zorluk="hard")

P.q("BDS 530 prg. 5-g",
    f"{B530}, örnekleme riskinin denetimin verimliliğini etkileyen türüne örnek aşağıdakilerden hangisidir?",
    "Önemli yanlışlık yokken detay testinde yanlışlık bulunduğu sonucuna varılması",
    ["Kontrolün gerçekte olduğundan daha etkin olduğu sonucuna varılması",
     "Önemli yanlışlık varken detay testinde yanlışlık bulunmadığı sonucuna varılması",
     "Denetçinin uygun olmayan bir prosedür seçmesi",
     "Denetçinin bir yanlışlığı gözden kaçırarak yanlış yorumlaması"],
    "BDS 530 prg. 5-g-ii'ye göre kontrollerin olduğundan daha az etkin görülmesi veya önemli yanlışlık yokken yanlışlık "
    "bulunduğu sonucuna varılması, genellikle ilave çalışmaya yol açtığından denetimin verimliliğini etkiler. Uygun olmayan "
    "prosedür seçimi ve yanlışlığın gözden kaçırılması örnekleme dışı risktir.")

P.q("BDS 530 prg. 5-f, A1",
    f"{B530}, aşağıdakilerden hangisi örnekleme dışı riske örnektir?",
    "Uygun olmayan bir denetim prosedürü kullanılması",
    ["Örneklemin anakitleyi temsil etmemesi",
     "Rastgele seçilen kalemlerin tesadüfen hatasız çıkması",
     "Örneklem büyüklüğünün istatistiki olarak yetersiz kalması",
     "Seçilen örneklem sonuçlarının anakitleden farklı sonuç vermesi"],
    "BDS 530 prg. 5-f'ye göre örnekleme dışı risk, örnekleme riskiyle ilgili olmayan bir sebepten hatalı sonuca "
    "ulaşılmasıdır. A1'e göre uygun olmayan prosedür kullanılması veya denetim kanıtının yanlış yorumlanması ve bir "
    "yanlışlığın ya da sapmanın fark edilmemesi örnektir.")

P.q("BDS 530 prg. 5-d",
    f"{B530}, istatistiki örnekleme yaklaşımının özellikleri aşağıdakilerin hangisinde doğru verilmiştir?",
    "Kalemlerin rastgele seçilmesi ve sonuçların olasılık teorisiyle değerlendirilmesi",
    ["Kalemlerin denetçinin muhakemesiyle seçilmesi ve sonuçların sezgiyle değerlendirilmesi",
     "Sadece yüksek tutarlı kalemlerin seçilmesi ve kalanların analitik incelenmesi",
     "Kalemlerin sistematik seçilmesi ve sonuçların yönetimle birlikte değerlendirilmesi",
     "Anakitlenin tamamının incelenmesi ve olasılık teorisinin kullanılmaması"],
    "BDS 530 prg. 5-d'ye göre istatistiki örnekleme, örneklem kalemlerinin rastgele seçilmesi ve örnekleme riskinin ölçümü "
    "dahil sonuçların değerlendirilmesinde olasılık teorisinin kullanılması özelliklerini taşır; bu özellikleri taşımayan "
    "yaklaşım istatistiki olmayan örneklemedir.")

P.q("BDS 530 prg. 5-ç",
    f"{B530}, bir anakitlenin, her biri benzer özelliklere (çoğunlukla parasal değere) sahip örnekleme birimi "
    "gruplarından oluşan alt gruplara bölünmesi süreci aşağıdakilerden hangisidir?",
    "Gruplandırma",
    ["Anomali", "Örnekleme birimi", "Kabul edilebilir yanlışlık", "Sistematik seçim"],
    "BDS 530 prg. 5-ç'ye göre bu süreç gruplandırmadır (tabakalama). Gruplandırma, alt gruplar içindeki değişkenliği "
    "azaltarak örneklem büyüklüğünü artırmadan etkinliği yükseltebilir (A8).", zorluk="easy")

P.q("BDS 530 prg. 5-b, 13",
    f"{B530}, örneklemde tespit edilen bir yanlışlığın anomali (aykırılık) olarak değerlendirilmesine ilişkin "
    "aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetçi, anomali sayılan yanlışlıkları ek prosedür uygulamadan anakitle öngörüsünden çıkarabilir.",
    ["Anomali, anakitlede bulunan yanlışlıkları açıkça temsil etmeyen bir yanlışlık veya sapmadır.",
     "Bir yanlışlığın anomali olarak değerlendirilmesi çok ender durumlarda söz konusudur.",
     "Denetçinin yanlışlığın anakitleyi temsil etmediğine dair kesinlik derecesi yüksek bir kanaati olmalıdır.",
     "Bu kanaat, kalan anakitlenin etkilenmediğine dair ilave prosedürlerle elde edilen kanıta dayanır."],
    "BDS 530 prg. 5-b anomaliyi anakitledeki yanlışlıkları açıkça temsil etmeyen yanlışlık olarak tanımlar. Prg. 13'e göre "
    "anomali değerlendirmesi çok ender durumlarda yapılır ve yanlışlığın anakitlenin kalanını etkilemediğine dair ilave "
    "prosedürlerle elde edilen yeterli ve uygun kanıta dayanan yüksek kesinlikte bir kanaat gerektirir.", zorluk="hard")

P.q("BDS 530 prg. 5-h, A3",
    f"{B530}, kabul edilebilir yanlışlık ile performans önemliliği arasındaki ilişkiye dair aşağıdakilerden hangisi "
    "doğrudur?",
    "Kabul edilebilir yanlışlık, performans önemliliğine eşit veya ondan düşük olabilir.",
    ["Kabul edilebilir yanlışlık genellikle performans önemliliğinden yüksektir.",
     "Kabul edilebilir yanlışlık, genel önemliliğin iki katı olarak belirlenir.",
     "Kabul edilebilir yanlışlık, yönetimin kabul ettiği yanlışlıkların toplamıdır.",
     "Kabul edilebilir yanlışlık kontrol testlerinde kullanılır, detay testlerinde kullanılmaz."],
    "BDS 530 prg. 5-h'ye göre kabul edilebilir yanlışlık, anakitledeki fiili yanlışlığın aşmayacağına dair uygun güvence için "
    "belirlenen parasal tutardır. A3'e göre bu, performans önemliliğinin belirli bir örnekleme prosedürüne uygulanmasıdır ve "
    "performans önemliliğine eşit veya ondan düşük olabilir; detay testlerinde kullanılır.")

P.q("BDS 530 prg. 5-ğ",
    f"{B530}, kontrol testlerinde denetçi tarafından belirlenen ve anakitledeki gerçek sapma oranının aşmayacağına dair "
    "uygun güvence elde edilmek istenen oran aşağıdakilerden hangisidir?",
    "Kabul edilebilir sapma oranı",
    ["Beklenen yanlışlık oranı", "Örnekleme riski oranı", "Anomali oranı", "Performans önemliliği oranı"],
    "BDS 530 prg. 5-ğ'ye göre kabul edilebilir sapma oranı, öngörülen iç kontrol prosedürlerinden sapma oranı olup "
    "anakitledeki gerçek sapma oranının bu oranı aşmayacağına dair uygun güvence elde etmek için belirlenir.", zorluk="easy")

P.q("BDS 530 prg. 7-8",
    f"{B530}, örneklem büyüklüğü ve kalemlerin seçilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetçi, anakitledeki bazı birimlerin seçilme şansı olmayacak şekilde kalem seçebilir.",
    ["Örneklem büyüklüğü, örnekleme riskini kabul edilebilir düşük seviyeye indirmeye yetecek şekilde belirlenir.",
     "Denetçi örneklemi tasarlarken prosedürün amacını ve anakitlenin özelliklerini mütalaa eder.",
     "Kalemler, anakitledeki her örnekleme biriminin seçilme şansı olacak şekilde seçilir.",
     "Denetçinin kabul edebileceği risk düştükçe gereken örneklem büyüklüğü artar."],
    "BDS 530 prg. 6'ya göre örneklem tasarlanırken amaç ve anakitle özellikleri, prg. 7'ye göre örnekleme riskini kabul "
    "edilebilir düşük seviyeye indirecek büyüklük dikkate alınır. Prg. 8'e göre her örnekleme biriminin seçilme şansı "
    "olacak şekilde seçim yapılır; A10'a göre kabul edilebilir risk düştükçe örneklem büyür.")

P.q("BDS 530 prg. 10-11",
    "Denetçi, alacak teyidi için seçtiği bir faturanın belgesine ulaşamamış ve uygun bir alternatif prosedür de "
    f"uygulayamamıştır. {B530} bu kalem için aşağıdakilerden hangisi doğrudur?",
    "Kalem, detay testi bakımından yanlışlık sayılır.",
    ["Kalem örneklemden çıkarılır ve yerine başka kalem seçilmez.",
     "Kalem hatasız kabul edilerek sonuç değerlendirmesine alınır.",
     "Kalem için yönetimden sözlü açıklama alınarak test tamamlanır.",
     "Kalem anomali olarak değerlendirilip öngörüden çıkarılır."],
    "BDS 530 prg. 10'a göre prosedür seçilen kaleme uygulanamazsa yerini alan başka bir kaleme uygulanır (ör. hatalı "
    "seçilen iptal edilmiş çek). Prg. 11'e göre tasarlanan veya uygun alternatif prosedür uygulanamıyorsa kalem, kontrol "
    "testinde sapma, detay testinde yanlışlık olarak kabul edilir.", zorluk="hard")

P.sayisal("BDS 530 prg. 14",
    "Denetçi, toplamı 4.800.000 ₺ olan ticari alacaklar anakitlesinden toplamı 600.000 ₺ olan bir örneklem seçmiş ve "
    "örneklemde 9.000 ₺ tutarında fazla gösterim yanlışlığı tespit etmiştir. Denetçi, bulunan yanlışlığın anakitleye "
    f"tutar oranında yansıyacağını varsayan oran yöntemini kullanmaktadır. {B530} yanlışlığın anakitle için öngörülen "
    "tutarı kaç ₺'dir?",
    "72.000 ₺", ["9.000 ₺", "36.000 ₺", "54.000 ₺", "81.000 ₺"],
    "BDS 530 prg. 14'e göre detay testlerinde denetçi, örneklemde bulduğu yanlışlıkları anakitlenin geneli için öngörür. "
    "Oran yönteminde örneklemdeki yanlışlık oranı 9.000 / 600.000 = %1,5'tir; anakitleye uygulandığında "
    "4.800.000 × %1,5 = 72.000 ₺ öngörülen yanlışlık bulunur.", zorluk="hard")

P.q("BDS 530 prg. 15",
    f"{B530}, örneklem sonuçlarının değerlendirilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sonuçları ve örneklemenin anakitle için makul dayanak sağlayıp sağlamadığını değerlendirir.",
    ["Örneklemde yanlışlık çıkmazsa anakitlenin hatasız olduğu sonucuna varılır.",
     "Örneklem sonuçları sadece yönetimin onayıyla anakitleye yansıtılır.",
     "Öngörülen yanlışlık kabul edilebilir yanlışlığı aşsa da denetçinin ek işlem yapması gerekmez.",
     "Değerlendirme sadece istatistiki örnekleme yapıldığında gerekir."],
    "BDS 530 prg. 15'e göre denetçi, örneklem sonuçlarını ve denetim örneklemesinin kullanılmasının test edilen anakitle "
    "hakkında makul bir dayanak sağlayıp sağlamadığını değerlendirir; sağlamıyorsa ilave kanıt veya alternatif prosedürler "
    "gerekebilir (A23).")

P.q("BDS 530 prg. 12",
    f"{B530}, örneklemde belirlenen sapma veya yanlışlıklara ilişkin denetçinin yapması gereken aşağıdakilerden "
    "hangisidir?",
    "Her birinin nitelik ve sebebini araştırır, olası etkilerini değerlendirir.",
    ["Sadece tutarı önemliliği aşan yanlışlıkları araştırır.",
     "Yanlışlıkları yönetime bildirir ve yönetim düzelttiyse ayrıca değerlendirmez.",
     "Sapmaları rastlantısal kabul ederek sonuçlara dahil etmez.",
     "Yanlışlıkların nedenini araştırmaz, sadece toplam tutarı hesaplar."],
    "BDS 530 prg. 12'ye göre denetçi belirlediği her bir sapma veya yanlışlığın nitelik ve sebebini araştırır ve bunların "
    "denetim prosedürünün amacı ve denetimin diğer alanları üzerindeki muhtemel etkilerini değerlendirir.")

P.q("BDS 530 prg. 5-a, 5-e",
    f"{B530}, anakitle ve örnekleme birimine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Örnekleme birimi, anakitleden bağımsız olarak denetçinin belirlediği yeni bir veri setidir.",
    ["Anakitle, içinden örneklem seçilen ve hakkında sonuca varılmak istenen veri setinin tamamıdır.",
     "Örnekleme birimi, anakitleyi oluşturan bağımsız kalemlerin her biridir.",
     "Örnekleme birimleri, parasal birimler veya çekler gibi fiziki kalemler olabilir.",
     "Anakitle, prosedürün amacı bakımından uygun ve eksiksiz olmalıdır."],
    "BDS 530 prg. 5-a anakitleyi hakkında sonuca varılmak istenen veri setinin tamamı, prg. 5-e örnekleme birimini "
    "anakitleyi oluşturan bağımsız kalemlerin her biri olarak tanımlar; A2'ye göre bunlar fiziki kalemler veya parasal "
    "birimler olabilir. A7'ye göre anakitlenin uygun ve eksiksiz olması gerekir.")

P.oncul("BDS 530 prg. 5",
    f"{B530} aşağıdaki ifadeler değerlendirilmektedir:",
    ["Örnekleme riski, örneklem sonucunun tüm anakitleye uygulanan prosedür sonucundan farklı olması riskidir.",
     "Örnekleme dışı risk, denetçinin örnekleme dışındaki bir sebepten hatalı sonuca ulaşmasıdır.",
     "İstatistiki olmayan örnekleme BDS'lere göre kabul edilmez.",
     "Kabul edilebilir yanlışlık, parasal bir tutardır."],
    "Yukarıdaki ifadelerden hangileri doğrudur?",
    "I, II ve IV",
    ["I ve II", "II ve III", "I, II ve IV", "I, III ve IV", "II, III ve IV"],
    "BDS 530 prg. 5-g örnekleme riskini (I), prg. 5-f örnekleme dışı riski (II) tanımlar; prg. 5-h'ye göre kabul edilebilir "
    "yanlışlık parasal bir tutardır (IV). Prg. 5-d ve A9'a göre istatistiki veya istatistiki olmayan yaklaşım denetçinin "
    "muhakemesine bağlıdır; ikisi de kabul edilir (III yanlış).", zorluk="hard")

P.q("BDS 530 A12-A13",
    f"{B530}, aşağıdaki seçim yöntemlerinden hangisi denetim örneklemesi açısından uygun kabul edilmez?",
    "Denetçinin kolayca ulaştığı kalemlerle sınırlı seçim",
    ["Rastgele sayı üreticileriyle yapılan rastgele seçim",
     "Başlangıç noktası rastgele belirlenen sistematik seçim",
     "Parasal birim örneklemesi",
     "Yanlılıktan kaçınılarak yapılan gelişigüzel seçim"],
    "BDS 530 prg. 8 ve A12-A13'e göre temel amaç her birimin seçilme şansı olmasıdır; rastgele, sistematik ve parasal birim "
    "seçimi ile yanlılıktan kaçınılarak yapılan gelişigüzel seçim yöntemleri kullanılabilir. Kolay ulaşılan kalemlerle "
    "sınırlı seçim yanlılık içerir ve örneklemenin temsil edici olmasını engeller.")

# ================================================================ ek sorular
P.q("BDS 320 prg. 12, A13",
    f"{B320}, önemliliğin denetim sırasında değiştirilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Önemlilik, planlamada belirlendikten sonra denetim boyunca değiştirilemez.",
    ["İşletmenin işinin önemli bir bölümünü elden çıkarma kararı önemliliğin değiştirilmesini gerektirebilir.",
     "Yeni bilgiler veya işletmeye ilişkin anlayışın değişmesi önemliliği değiştirebilir.",
     "Gerçekleşen sonuçlar beklenenlerden büyük farklılık gösterirse önemlilik yeniden belirlenebilir.",
     "Önemlilikteki değişiklikler ve bunların gerekçeleri belgelendirilir."],
    "BDS 320 prg. 12 ve A13'e göre şartlardaki değişiklik (ör. işin önemli bölümünün elden çıkarılması), yeni bilgiler "
    "veya anlayıştaki değişiklik ya da gerçekleşen sonuçların beklenenden büyük farklılık göstermesi önemliliğin "
    "değiştirilmesini gerektirebilir; prg. 14 değişikliklerin belgelendirilmesini ister.")

P.q("BDS 320 A4",
    f"{B320}, aşağıdakilerden hangisi önemliliğin belirlenmesinde kullanılabilecek kıyaslama noktalarına örnek "
    "değildir?",
    "Önceki yıl denetim şirketine ödenen denetim ücreti",
    ["Sürdürülen faaliyetlerden elde edilen vergi öncesi kâr", "Toplam hasılat",
     "Brüt kâr veya toplam giderler", "Toplam özkaynak veya net varlık değeri"],
    "BDS 320 A4'e göre kıyaslama noktalarına vergi öncesi kâr, toplam hasılat, brüt kâr, toplam giderler, toplam özkaynak "
    "veya net varlık değeri örnek verilebilir. Denetim ücreti kullanıcıların kararlarıyla ilgili bir kıyaslama noktası "
    "değildir.", zorluk="easy")

P.q("BDS 320 A10",
    f"{B320}, belirli işlem sınıfları için genel önemlilikten düşük önemlilik düzeyi belirlenmesini gerektirebilecek "
    "durumlara örnek aşağıdakilerden hangisi değildir?",
    "Kalemin tablolardaki en büyük tutarlı bakiye olması",
    ["Üst yönetime ödenen ücretler gibi kullanıcı beklentisi yüksek açıklamalar",
     "İlişkili taraf işlemleri",
     "İlaç şirketinde araştırma ve geliştirme maliyetleri gibi sektöre özgü açıklamalar",
     "Tablolarda ayrı açıklanan yeni satın alınan bir işletmeye kullanıcıların dikkat etmesi"],
    "BDS 320 A10'a göre mevzuat veya çerçevenin kullanıcı beklentilerini etkilediği kalemler (üst yönetim ücretleri, "
    "ilişkili taraf işlemleri), sektöre ilişkin esas açıklamalar (ör. Ar-Ge) ve kullanıcıların dikkatinin odaklandığı "
    "özel alanlar (ör. yeni edinilen işletme) örnek verilir. Bakiyenin büyüklüğü tek başına bu kapsamda değildir.")

P.q("BDS 320 A12",
    f"{B320}, performans önemliliğinin belirlenmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Performans önemliliği, genel önemliliğin sabit bir yüzdesi olarak mekanik biçimde hesaplanır.",
    ["Performans önemliliği mesleki muhakemeden etkilenir.",
     "Denetçinin işletmeye ilişkin, risk değerlendirmesiyle güncellenen anlayışı belirlemeyi etkiler.",
     "Önceki denetimlerde belirlenen yanlışlıkların niteliği ve kapsamı dikkate alınır.",
     "Cari dönemde beklenen yanlışlıklara ilişkin beklentiler de performans önemliliğini etkiler."],
    "BDS 320 A12'ye göre performans önemliliğinin belirlenmesi basit mekanik bir hesaplama değildir, mesleki muhakeme "
    "gerektirir; işletmeye ilişkin anlayıştan, önceki denetimlerde belirlenen yanlışlıkların niteliği ve kapsamından ve "
    "cari döneme ilişkin yanlışlık beklentilerinden etkilenir.", zorluk="hard")

P.q("BDS 450 prg. 11-b, 13",
    f"{B450}, önceki dönemlere ilişkin düzeltilmemiş yanlışlıklara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Önceki dönem düzeltilmemiş yanlışlıkları, cari dönem değerlendirmesinde dikkate alınmaz.",
    ["Önceki dönem düzeltilmemiş yanlışlıklarının ilgili kalemlere etkisi mütalaa edilir.",
     "Önceki dönem düzeltilmemiş yanlışlıklarının tablolar bütünü üzerindeki etkisi mütalaa edilir.",
     "Önceki dönem düzeltilmemiş yanlışlıklarının etkisi üst yönetimden sorumlu olanlara bildirilir.",
     "Önceki dönemlerde önemsiz görülen yanlışlıklar birikerek cari dönemde önemli hâle gelebilir."],
    "BDS 450 prg. 11-b'ye göre denetçi, önceki dönem düzeltilmemiş yanlışlıklarının ilgili kalemler ve tablolar bütünü "
    "üzerindeki etkisini mütalaa eder; prg. 13'e göre bu etkiyi üst yönetime bildirir. Birikim etkisi cari dönemde "
    "önemli bir yanlışlığa yol açabilir (A18).")

P.q("BDS 450 A16",
    f"{B450}, önemliliğin altındaki bir yanlışlığın önemli olarak değerlendirilmesine yol açabilecek durumlar arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Yanlışlığın düzeltilmesinin denetim süresini birkaç gün uzatacak olması",
    ["Yanlışlığın mevzuat hükümlerine uygunluğu etkilemesi",
     "Yanlışlığın borç sözleşmelerindeki şartları etkilemesi",
     "Yanlışlığın kazançlardaki bir eğilim değişikliğini gizlemesi",
     "Yanlışlığın gelecek dönemlerde önemli etki yaratacak bir muhasebe politikası seçimiyle ilgili olması"],
    "BDS 450 A16'ya göre mevzuata uygunluğu veya borç sözleşmelerini etkilemesi, gelecek dönemlerde önemli etki yapacak "
    "yanlış bir politika seçimiyle ilgili olması ve kazanç eğilimini gizlemesi gibi durumlar önemliliğin altındaki bir "
    "yanlışlığı önemli kılabilir. Denetim süresinin uzaması bu kapsamda değildir.")

P.q("BDS 450 A3",
    "Denetçi, yönetimin garanti karşılığı tahmininin makul aralığın dışında kaldığı sonucuna varmış ve kendi makul "
    f"aralığının en yakın noktasıyla arasındaki farkı yanlışlık olarak dikkate almıştır. {B450} uygulama hükümlerindeki "
    "sınıflandırmaya göre bu yanlışlık türü aşağıdakilerden hangisidir?",
    "Muhakeme yanlışlığı",
    ["Fiili yanlışlık", "Öngörülen yanlışlık", "Anomali", "Bariz biçimde önemsiz yanlışlık"],
    "BDS 450 A3'e göre fiili yanlışlıklar hakkında şüphe bulunmayan yanlışlıklardır; muhakeme yanlışlıkları, yönetimin "
    "tahminlere ilişkin makul bulunmayan muhakemelerinden veya uygun bulunmayan politika seçiminden kaynaklanır; "
    "öngörülen yanlışlıklar ise örneklemde bulunan yanlışlıkların anakitleye yansıtılmasıdır.", zorluk="hard")

P.q("BDS 450 prg. 12",
    f"{B450}, düzeltilmemiş yanlışlıkların üst yönetimden sorumlu olanlara bildirilmesine ilişkin aşağıdaki ifadelerden "
    "hangisi yanlıştır?",
    "Mevzuat yasaklasa dahi düzeltilmemiş yanlışlıklar üst yönetime bildirilir.",
    ["Bildirim, yanlışlıkların görüş üzerinde yapabileceği etkiyi de kapsar.",
     "Düzeltilmemiş önemli yanlışlıklar münferit olarak tanımlanır.",
     "Denetçi, üst yönetimden düzeltilmemiş yanlışlıkların düzeltilmesini talep eder.",
     "Önceki dönem düzeltilmemiş yanlışlıklarının etkisi de ayrıca bildirilir."],
    "BDS 450 prg. 12'ye göre denetçi, mevzuat tarafından yasaklanmadığı sürece düzeltilmemiş yanlışlıkları ve görüşe "
    "olası etkisini üst yönetime bildirir, önemli olanları münferit tanımlar ve düzeltme talep eder; prg. 13 önceki dönem "
    "yanlışlıklarının etkisinin bildirilmesini ister.")

P.q("BDS 530 prg. 1, A52",
    f"{B530}, aşağıdaki seçim yaklaşımlarından hangisi denetim örneklemesi sayılmaz?",
    "Tutarı belirli bir sınırın üzerindeki kalemlerin tamamının seçilmesi",
    ["Her örnekleme birimine seçilme şansı veren rastgele seçim",
     "Rastgele bir başlangıç noktasıyla yapılan sistematik seçim",
     "Parasal birimlere dayalı değer ağırlıklı seçim",
     "Anakitleyi gruplara ayırıp her gruptan temsilî seçim yapılması"],
    "BDS 530 prg. 5-c'ye göre örnekleme, tüm birimlere seçilme şansı sağlanarak kalemlerin %100'ünden azına prosedür "
    "uygulanmasıdır. BDS 500 A52-A56'ya göre belirli kalemlerin (ör. belirli tutarın üzerindekilerin) seçilmesi etkin bir "
    "yöntemdir; ancak denetim örneklemesi değildir ve sonuçlar kalan anakitleye öngörülemez.", zorluk="hard")

P.q("BDS 530 Ek 1",
    f"{B530}, gruplandırmaya (tabakalama) ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bir alt gruptan elde edilen sonuç, doğrudan anakitlenin tamamına öngörülür.",
    ["Gruplandırma, alt gruplar içindeki değişkenliği azaltarak etkinliği artırabilir.",
     "Alt gruplar çoğunlukla parasal değer gibi benzer özelliklere göre oluşturulur.",
     "Alt gruptaki kalemlere uygulanan prosedürlerin sonuçları sadece o alt gruba öngörülür.",
     "Anakitlenin tamamına ilişkin sonuç için alt gruplardaki sonuçlar birlikte değerlendirilir."],
    "BDS 530 Ek 1'e göre gruplandırma, alt gruplardaki değişkenliği azaltarak örneklem büyüklüğünü artırmadan etkinliği "
    "yükseltebilir. Bir alt gruba uygulanan prosedürlerin sonuçları sadece o alt gruba öngörülür; anakitlenin tamamı "
    "hakkında sonuca varmak için tüm alt grupların sonuçları birlikte değerlendirilir.", zorluk="hard")

P.q("BDS 530 prg. 14, A20",
    f"{B530}, yanlışlık ve sapmaların anakitleye öngörülmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kontrol testlerinde örneklem sapma oranı ayrıca ve açık bir yöntemle anakitleye öngörülmelidir.",
    ["Detay testlerinde örneklemde bulunan yanlışlıklar anakitlenin geneli için öngörülür.",
     "Kontrol testlerinde örneklem sapma oranı aynı zamanda anakitle için öngörülen sapma oranıdır.",
     "Anomali sayılan yanlışlık öngörüde dikkate alınmayabilir; düzeltilmezse etkisi ayrıca dikkate alınır.",
     "Öngörülen yanlışlık ile anomali toplamı, denetçinin anakitle için en iyi yanlışlık tahminidir."],
    "BDS 530 prg. 14'e göre detay testlerinde yanlışlıklar anakitleye öngörülür; A20'ye göre kontrol testlerinde örneklem "
    "sapma oranı aynı zamanda anakitle için öngörülen sapma oranı olduğundan açık bir öngörü gerekmez. A19-A22 anomalinin "
    "ve en iyi tahminin nasıl ele alınacağını açıklar.", zorluk="hard")

P.q("BDS 530 A22",
    f"{B530}, detay testinde öngörülen yanlışlık ile anomali toplamının kabul edilebilir yanlışlığı aşması durumuna "
    "ilişkin aşağıdakilerden hangisi doğrudur?",
    "Örneklem, anakitle hakkında sonuç için makul dayanak sağlamaz.",
    ["Anakitlede önemli yanlışlık bulunmadığı sonucuna varılır.",
     "Kabul edilebilir yanlışlık tutarı öngörülen tutara eşitlenerek test tamamlanır.",
     "Anomaliler toplama dahil edilmeyerek kabul edilebilir düzeyin altına inilir.",
     "Yanlışlıklar yönetime bildirilmeden bir sonraki döneme devredilir."],
    "BDS 530 A22'ye göre öngörülen yanlışlık ve varsa anomali toplamı denetçinin en iyi tahminidir; bu toplam kabul "
    "edilebilir yanlışlığı aşarsa örneklem, test edilen anakitle hakkındaki sonuçlar için makul bir dayanak sağlamaz ve "
    "ilave prosedür veya yönetimden inceleme talebi gerekebilir (A23).")

P.q("BDS 530 A21",
    "Denetçi, satın alma onay kontrolünü test etmek için seçtiği 60 kalemden 5'inde onay olmadığını tespit etmiştir. "
    f"Planlamada beklenen sapma oranı %1, kabul edilebilir sapma oranı ise %5'tir. {B530} bu sonuca ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Beklenmeyen yüksek sapma oranı, ek kanıt yoksa önemli yanlışlık riskini artırabilir.",
    ["Sapma oranı kabul edilebilir sapma oranının altında olduğundan kontrole tam güvenilir.",
     "Sapmalar anomali sayılarak değerlendirmeden çıkarılır ve test tamamlanır.",
     "Sapma oranı hesaplanmaz; beş kalemin tutarı önemliliğin altındaysa sonuç etkilenmez.",
     "Sapma oranı anakitleye ayrıca öngörülmeden değerlendirilemeyeceği için test geçersizdir."],
    "Örneklem sapma oranı 5/60 ≈ %8,3'tür ve kabul edilebilir sapma oranını (%5) aşmaktadır. BDS 530 A21'e göre başlangıç "
    "değerlendirmesini destekleyen ilave kanıt elde edilmedikçe beklenmeyen yüksek sapma oranı değerlendirilmiş önemli "
    "yanlışlık riskini artırabilir; BDS 330 prg. 17'deki adımlar uygulanır.", zorluk="hard")

P.q("BDS 530 A9, A12",
    f"{B530}, istatistiki olmayan örneklemeye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Örneklem büyüklüğü, istatistiki ve istatistiki olmayan yaklaşımları ayırmada geçerli bir kriterdir.",
    ["İstatistiki olmayan yöntemde kalemlerin seçiminde mesleki muhakeme kullanılır.",
     "Hangi yaklaşımın kullanılacağı denetçinin mesleki muhakemesine dayanır.",
     "Her iki yaklaşımda da yanlılıktan uzak ve temsil edici bir örneklem seçilmesi önemlidir.",
     "Örneklem büyüklüğünü etkileyen faktörlerin etkisi iki yaklaşımda benzerdir."],
    "BDS 530 A9'a göre yaklaşım seçimi mesleki muhakemeye dayanır ve örneklem büyüklüğü iki yaklaşımı ayırmada geçerli bir "
    "kriter değildir. A11-A12'ye göre faktörlerin etkisi benzerdir; istatistiki olmayan yöntemde seçimde muhakeme "
    "kullanılır, ancak temsil edici ve yanlılıktan uzak örneklem seçilmesi her iki yaklaşımda önemlidir.")

P.q("BDS 530 A10",
    f"{B530}, örneklem büyüklüğüne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetçinin kabul etmek istediği örnekleme riski azaldıkça gerekli örneklem büyüklüğü de azalır.",
    ["Örneklem büyüklüğüne istatistiki bir formülle veya mesleki muhakemeyle karar verilebilir.",
     "Kabul edilebilir örnekleme riski düzeyi gerekli örneklem büyüklüğünü etkiler.",
     "Örneklem büyüklüğü, örnekleme riskini kabul edilebilir düşük seviyeye indirecek şekilde belirlenir.",
     "Örneklem büyüklüğünü etkileyen faktörler BDS 530 eklerinde açıklanmıştır."],
    "BDS 530 A10'a göre denetçinin kabul etmek istediği risk düzeyi azaldıkça gerekli örneklem büyüklüğü artar. A11'e göre "
    "büyüklüğe formülle veya muhakemeyle karar verilebilir; prg. 7'ye göre büyüklük riski kabul edilebilir düşük seviyeye "
    "indirecek şekilde belirlenir. Faktörler Ek 2 ve Ek 3'te yer alır.")

P.q("BDS 320 prg. 6",
    f"{B320}, planlamada belirlenen önemlilik ile yanlışlıkların değerlendirilmesi arasındaki ilişkiye dair aşağıdakilerden "
    "hangisi doğrudur?",
    "Değerlendirmede tutarın yanında yanlışlıkların niteliği ve şartları da dikkate alınır.",
    ["Planlamada belirlenen önemliliğin altındaki tüm yanlışlıklar değerlendirme dışı kalır.",
     "Planlama önemliliği sadece örneklem büyüklüğünü belirlemek için kullanılır.",
     "Değerlendirmede sadece yanlışlığın tutarı esas alınır; nitelik önem taşımaz.",
     "Planlamada belirlenen önemlilik değerlendirme aşamasında kullanılmaz."],
    "BDS 320 prg. 6'ya göre planlamada belirlenen önemlilik, düzeltilmemiş yanlışlıkların önemsiz sayılacağı bir tutar "
    "değildir; denetçi düzeltilmemiş yanlışlıkları değerlendirirken tutarın yanında niteliklerini ve ortaya çıktıkları "
    "özel şartları da dikkate alır (BDS 450 prg. 11 ve A16).")

P.q("BDS 530 prg. 13",
    "Denetçi, örneklemde bulduğu bir yanlışlığın, yıl içinde tek bir gün devrede olan ve sonradan düzeltilen hatalı bir "
    f"yazılım güncellemesinden kaynaklandığını düşünmektedir. {B530} bu yanlışlığı anomali olarak değerlendirebilmesi "
    "için aşağıdakilerden hangisi gereklidir?",
    "Kalan anakitlenin etkilenmediğine dair ilave prosedürlerle yeterli kanıt elde etmek",
    ["Yönetimden yanlışlığın münferit olduğuna dair sözlü açıklama almak",
     "Yanlışlık tutarının bariz biçimde önemsiz eşiğin altında olması",
     "Yanlışlığın örneklemdeki tek yanlışlık olması",
     "Yazılım firmasından hatanın düzeltildiğine dair fatura almak"],
    "BDS 530 prg. 13'e göre yanlışlığın anomali olarak değerlendirildiği çok ender durumlarda denetçinin, yanlışlığın "
    "anakitleyi temsil etmediğine dair yüksek kesinlikte kanaati olmalıdır; bu kanaat, anakitlenin kalanını etkilemediğine "
    "dair ilave prosedürlerle elde edilen yeterli ve uygun kanıta dayanır.")

P.q("BDS 450 prg. 6-a",
    "Denetçi, bir şubenin satış kesim işlemlerinde yıl sonuna ait sevkiyatların ertesi yıla kaydedildiğini ve bunun "
    f"şubedeki sistematik bir uygulamadan kaynaklandığını tespit etmiştir. {B450} bu durumda denetçinin yapması gereken "
    "aşağıdakilerden hangisidir?",
    "Başka önemli yanlışlıklar olabileceğinden strateji ve planın revize edilmesi gerekip gerekmediğine karar verir.",
    ["Yanlışlık bir şubeye ait olduğundan diğer şubeler için ek değerlendirme yapmaz.",
     "Yanlışlığı anomali kabul ederek toplam değerlendirmeden çıkarır.",
     "Tespit edilen tutarı düzelttirerek kesim testini tamamlanmış sayar.",
     "Yanlışlığı bariz biçimde önemsiz sayarak bir araya getirmez."],
    "BDS 450 prg. 6-a ve A4'e göre belirlenen yanlışlığın niteliği ve şartları (ör. iç kontrol eksikliği veya yaygın bir "
    "uygulama) başka yanlışlıklar bulunabileceğini gösteriyorsa denetçi genel denetim stratejisi ve planının revize "
    "edilmesinin gerekip gerekmediğine karar verir.", zorluk="hard")

if __name__ == "__main__":
    sys.exit(P.yaz())
