# -*- coding: utf-8 -*-
"""Hukuk · İş Hukuku · Eşit Davranma ve Ayrımcılık Yasağı — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında İş Kanunu ve ilgili mevzuat soruları kanun adıyla başlayan, tanım ve süre soran
kısa köklerle gelmiştir.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 4857 sayılı İş Kanunu md. 5 ve 18; 6701 sayılı Türkiye İnsan
Hakları ve Eşitlik Kurumu Kanunu md. 2-7, 17-18, 21, 25; 6098 sayılı TBK md. 417. Yeniden değerlemeye tabi idari para
cezası tutarları soru konusu yapılmamıştır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_esit_davranma_2026.json", lesson="is_hukuku", topic="esit_davranma",
          konu_adi="Eşit Davranma", seed=2026093018,
          surum="4857 s. İş Kanunu, 6701 s. TİHEK Kanunu ve 6098 s. TBK güncel metinleri; 29.09.2026 kontrolü")

K = "4857 sayılı İş Kanunu’na göre"
T = "6701 sayılı Türkiye İnsan Hakları ve Eşitlik Kurumu Kanunu’na göre"
B = "6098 sayılı Türk Borçlar Kanunu’na göre"

P.sayisal("İK md. 5",
    f"{K}, iş ilişkisinde eşit davranma ilkesine aykırı davranıldığında işçi, yoksun bırakıldığı haklarından başka en çok "
    "kaç aylık ücreti tutarında tazminat isteyebilir?",
    "4", ["2", "3", "6", "8"],
    "Md. 5'e göre eşit davranma ilkesine aykırılıkta işçi dört aya kadar ücreti tutarındaki uygun bir tazminattan başka yoksun "
    "bırakıldığı haklarını da talep edebilir.", zorluk="easy")

P.q("İK md. 5",
    f"{K}, iş ilişkisinde yasaklanan ayrım sebepleri arasında aşağıdakilerden hangisi sayılmamıştır?",
    "İşçinin mesleki yeterliliği",
    ["Dil", "Siyasal düşünce", "Engellilik", "Din ve mezhep"],
    "Md. 5'e göre iş ilişkisinde dil, ırk, renk, cinsiyet, engellilik, siyasal düşünce, felsefi inanç, din ve mezhep ve benzeri "
    "sebeplere dayalı ayrım yapılamaz; mesleki yeterlilik meşru bir değerlendirme ölçütüdür.", zorluk="easy")

P.q("İK md. 5",
    f"{K}, eşit davranma ilkesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kısmi süreli işçiye esaslı sebep olmadan farklı işlem yapılabilir.",
    ["Belirli süreli işçiye esaslı sebep olmadan farklı işlem yapılamaz.",
     "Gebelik nedeniyle farklı işlem yapılamaz.",
     "Eşit değerde iş için cinsiyetle düşük ücret kararlaştırılamaz.",
     "Özel koruyucu hükümler düşük ücreti haklı kılmaz."],
    "Md. 5'e göre işveren esaslı sebepler olmadıkça tam süreli işçi karşısında kısmi süreli işçiye, belirsiz süreli karşısında "
    "belirli süreli işçiye farklı işlem yapamaz.")

ta = 45_000 * 4
P.sayisal("İK md. 5",
    "Aylık ücreti 45.000 ₺ olan kadın işçiye, aynı işi yapan erkek işçilere göre cinsiyeti nedeniyle daha düşük ücret "
    f"ödenmiştir.\n\n{K}, işçinin ayrımcılık tazminatı olarak isteyebileceği en yüksek tutar kaç ₺’dir?",
    tl(ta), secenekler(ta, 90_000, 135_000, 270_000, 360_000),
    "Md. 5'e göre ayrımcılık tazminatı dört aya kadar ücret tutarındadır: 45.000 × 4 = 180.000 ₺; yoksun bırakılan ücret farkı "
    "ayrıca istenebilir.", zorluk="hard")

P.q("İK md. 5",
    f"{K}, cinsiyet veya gebelik nedeniyle farklı işlem yasağının uygulandığı aşamalar arasında aşağıdakilerden hangisi yer "
    "almaz?",
    "Emeklilik sonrası özel yaşam",
    ["İş sözleşmesinin yapılması",
     "Çalışma şartlarının oluşturulması",
     "Sözleşmenin uygulanması",
     "Sözleşmenin sona ermesi"],
    "Md. 5'e göre işveren biyolojik veya işin niteliğine ilişkin sebepler zorunlu kılmadıkça iş sözleşmesinin yapılması, "
    "şartlarının oluşturulması, uygulanması ve sona ermesinde cinsiyet veya gebelik nedeniyle farklı işlem yapamaz.")

P.q("İK md. 5",
    f"{K}, cinsiyet nedeniyle farklı işlem yapılabilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Biyolojik veya işin niteliği zorunlu kılarsa",
    ["İşverenin tercihine göre sınırsız",
     "İşyeri toplu iş sözleşmesinde açıkça öngörülmüşse",
     "İşçi yazılı olarak kabul etmişse",
     "Aynı işyerinde çalışan sayısı azsa"],
    "Md. 5'e göre cinsiyet veya gebelik nedeniyle farklı işlem ancak biyolojik veya işin niteliğine ilişkin sebeplerin zorunlu "
    "kılması hâlinde yapılabilir.", zorluk="hard")

P.sayisal("TİHEK md. 17",
    "Ayrımcılığa uğradığını ileri süren kişi, Kuruma başvurmadan önce uygulamanın düzeltilmesini ilgili taraftan istemiş, "
    f"cevap alamamıştır.\n\n{T}, talebe kaç gün içinde cevap verilmezse Kuruma başvurulabilir?",
    "30", ["7", "15", "45", "60"],
    "Md. 17/2'ye göre ilgililer önce uygulamanın düzeltilmesini ilgili taraftan ister; talebin reddedilmesi veya otuz gün "
    "içinde cevap verilmemesi hâlinde Kuruma başvurabilir.", zorluk="hard")

P.q("İK md. 5",
    f"{K}, eşit davranma ilkesine aykırılığın ispatına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Güçlü ihtimal gösterilirse ispat yer değiştirir.",
    ["İşçi ispatla yükümlü değildir.",
     "İspat yükü davanın her aşamasında sadece işverendedir.",
     "İspat yükü sendikaya aittir.",
     "Mahkeme ispat aramaksızın karar verir."],
    "Md. 5'e göre aykırılığı işçi ispatla yükümlüdür; ancak işçi ihlal ihtimalini güçlü biçimde gösteren bir durumu ortaya "
    "koyarsa işveren ihlalin bulunmadığını ispatla yükümlü olur.", zorluk="hard")

P.q("İK md. 5",
    "Bir işveren, aynı işi yapan ve aynı kıdeme sahip erkek ve kadın işçilere cinsiyet farkı nedeniyle farklı ücret "
    f"ödemektedir; kadın işçiler için özel koruyucu hükümler uygulandığını ileri sürmektedir.\n\n{K}, bu savunma hakkında "
    "aşağıdakilerden hangisi doğrudur?",
    "Daha düşük ücreti haklı kılmaz.",
    ["Ücret farkını haklı kılar.",
     "Farkı yarı oranında haklı kılar.",
     "Sadece gece çalışmasında haklı kılar.",
     "İşçinin onayı varsa haklı kılar."],
    "Md. 5'e göre işçinin cinsiyeti nedeniyle özel koruyucu hükümlerin uygulanması, daha düşük bir ücretin uygulanmasını haklı "
    "kılmaz.")

P.sayisal("TİHEK md. 18",
    f"{T}, Kurum başvuruları başvuru tarihinden itibaren en geç kaç ay içinde sonuçlandırır?",
    "3", ["1", "2", "4", "6"],
    "Md. 18/1'e göre Kurum başvuruları ve resen incelemeleri en geç üç ay içinde sonuçlandırır; süre Başkanca bir defaya mahsus "
    "en fazla üç ay uzatılabilir.")

P.q("İK md. 18",
    f"{K}, aşağıdakilerden hangisi fesih için geçerli sebep oluşturmaz?",
    "İşçinin aile yükümlülükleri",
    ["İşçinin verimsizliği",
     "İşçinin sık sık geç kalması",
     "İşletmenin küçülme gereği",
     "İşçinin iş yetersizliği"],
    "Md. 18/3-d'ye göre ırk, renk, cinsiyet, medeni hâl, aile yükümlülükleri, hamilelik, doğum, din, siyasi görüş ve benzeri "
    "nedenler fesih için geçerli sebep oluşturmaz.", zorluk="easy")

P.q("İK md. 18",
    f"{K}, geçerli fesih sebebi sayılmayan hâllere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İzinsiz iş saati sendikal faaliyeti de korunur.",
    ["Sendika üyeliği geçerli sebep değildir.",
     "Hamilelik geçerli sebep değildir.",
     "İşveren aleyhine yargıya başvurmak geçerli sebep değildir.",
     "Analık izninde işe gelmemek geçerli sebep değildir."],
    "Md. 18/3-a'ya göre çalışma saatleri dışında veya işverenin rızasıyla çalışma saatleri içinde sendikal faaliyetlere katılmak "
    "geçerli sebep oluşturmaz; izinsiz olarak çalışma saatinde faaliyet bu korumaya girmez.", zorluk="hard")

P.sayisal("TİHEK md. 18",
    f"{T}, ihlal iddiasına muhatap taraf yazılı görüşünü istemin tebliğinden itibaren kaç gün içinde Kuruma ulaştırır?",
    "15", ["7", "10", "30", "45"],
    "Md. 18/2'ye göre yazılı görüş istemin tebliğinden itibaren on beş gün içinde Kuruma ulaştırılır; Başkan bu süreyi bir defaya "
    "mahsus on beş gün uzatabilir.", zorluk="hard")

P.q("TİHEK md. 3",
    f"{T}, ayrımcılık yasağının temelleri arasında aşağıdakilerden hangisi sayılmamıştır?",
    "Mesleki performans",
    ["Kişinin serveti", "Kişinin medeni hâli", "Kişinin sağlık durumu", "Kişinin yaşı"],
    "Md. 3/2'ye göre cinsiyet, ırk, renk, dil, din, inanç, mezhep, felsefi ve siyasi görüş, etnik köken, servet, doğum, medeni "
    "hâl, sağlık durumu, engellilik ve yaş temellerine dayalı ayrımcılık yasaktır.", zorluk="easy")

P.q("TİHEK md. 2",
    f"{T}, ayrımcı uygulamanın birden fazla ayrımcılık temeliyle ilişkili olması aşağıdaki kavramlardan hangisiyle "
    "ifade edilir?",
    "Çoklu ayrımcılık",
    ["Dolaylı ayrımcılık", "Ayrı tutma", "Taciz", "Varsayılan temele dayalı ayrımcılık"],
    "Md. 2/ç'ye göre ayrımcı uygulamanın birden fazla ayrımcılık temeli ile ilişkili olması çoklu ayrımcılıktır.")

P.sayisal("TİHEK md. 18",
    f"{T}, Başkanın davetiyle başlayan uzlaşma süreci en geç kaç ay içinde sonuçlandırılır?",
    "1", ["2", "3", "4", "6"],
    "Md. 18/3'e göre uzlaşma en geç bir ay içinde sonuçlandırılır; müzakerelerde yapılan açıklamalar delil olarak kullanılamaz.",
    zorluk="hard")

P.q("TİHEK md. 2",
    "Bir işyerinde, görünüşte herkese eşit uygulanan bir kural, engelli çalışanları nesnel olarak haklılaştırılamayan "
    f"dezavantajlı bir konuma sokmaktadır.\n\n{T}, bu durum hangi ayrımcılık türüdür?",
    "Dolaylı ayrımcılık",
    ["Doğrudan ayrımcılık", "Çoklu ayrımcılık", "Ayrımcılık talimatı", "Ayrı tutma"],
    "Md. 2/e'ye göre görünüşte ayrımcı olmayan eylem, işlem ve uygulamalar sonucunda ayrımcılık temelleriyle bağlantılı olarak "
    "nesnel olarak haklılaştırılamayan dezavantajlı konuma sokma dolaylı ayrımcılıktır.")

P.q("TİHEK md. 2",
    "Bir işveren, gerçekte başka bir dine mensup olan işçiyi belirli bir dinden olduğunu sanarak terfi dışı bırakmıştır."
    f"\n\n{T}, bu durum hangi ayrımcılık türüdür?",
    "Varsayılan temele dayalı ayrımcılık",
    ["Çoklu ayrımcılık", "Dolaylı ayrımcılık", "Makul düzenleme yapmama", "Ayrı tutma"],
    "Md. 2/m'ye göre kişinin ayrımcılık temellerinden biriyle gerçekte ilgisi olmamasına rağmen o temeli taşıdığı sanılarak "
    "ayrımcı muameleye maruz kalması varsayılan temele dayalı ayrımcılıktır.", zorluk="hard")

P.sayisal("TİHEK md. 25",
    f"{T}, Kurulun verdiği idari para cezaları tebliğinden itibaren kaç ay içinde ödenir?",
    "1", ["2", "3", "6", "12"],
    "Md. 25/5'e göre Kanuna göre verilen idari para cezaları tebliğinden itibaren bir ay içinde ödenir.")

P.q("TİHEK md. 2",
    f"{T}, işyerinde yıldırmanın tanımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kasıtlı eylemlerdir.",
    ["İşverenin her türlü disiplin cezasıdır.",
     "Sadece fiziksel şiddet içeren eylemlerdir.",
     "Kasıt aranmayan ihmal hâlleridir.",
     "Sadece üst yöneticinin sözlü uyarısıdır."],
    "Md. 2/g'ye göre işyerinde yıldırma, Kanunda sayılan ayrımcılık temellerine dayanılarak kişiyi işinden soğutmak, dışlamak, "
    "bıktırmak amacıyla kasıtlı olarak yapılan eylemlerdir.")

P.q("TİHEK md. 2",
    f"{T}, makul düzenlemenin tanımına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Mali imkânlara bakılmaksızın uygulanır.",
    ["Engellilerin eşit yararlanmasını amaçlar.",
     "Belirli bir durumda ihtiyaç duyulan tedbirlerdir.",
     "Ölçülü, gerekli ve uygun olmalıdır.",
     "Mali imkânlar nispetinde yapılır."],
    "Md. 2/i'ye göre makul düzenleme mali imkânlar nispetinde, ölçülü, gerekli ve uygun değişiklik ve tedbirlerdir.",
    zorluk="hard")

P.sayisal("TİHEK md. 25",
    "Kurul, ayrımcılık yasağını ihlal eden işverenin idari para cezasını uyarı cezasına dönüştürmüş; işveren daha sonra "
    f"ayrımcı fiili tekrarlamıştır.\n\n{T}, işverene verilecek ceza yüzde kaç oranında artırılır?",
    "50", ["10", "25", "75", "100"],
    "Md. 25/4'e göre hakkında uyarı cezası verilen kişinin ayrımcı fiilinin tekrarı hâlinde alacağı ceza yüzde elli oranında "
    "artırılır; artış ceza üst sınırını aşamaz.", zorluk="hard")

P.q("TİHEK md. 2",
    f"{T}, tacizin tanımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Psikolojik ve cinsel türlerini de kapsar.",
    ["Sadece fiziksel temas içeren davranıştır.",
     "Sadece iş dışında yapılan davranıştır.",
     "Ayrımcılık temeli aranmaz.",
     "Sadece tekrarlanan davranışlar tacizdir."],
    "Md. 2/j'ye göre taciz, psikolojik ve cinsel türleri de dahil olmak üzere ayrımcılık temellerinden birine dayanılarak insan "
    "onurunu çiğneyen, yıldırıcı, onur kırıcı, aşağılayıcı veya utandırıcı her türlü davranıştır.")

P.q("TİHEK md. 4",
    f"{T}, aşağıdakilerden hangisi Kanun kapsamındaki ayrımcılık türlerinden biri değildir?",
    "Meşru performans ölçümü",
    ["Kişilerin ayrı tutulması", "Ayrımcılık talimatı verme", "Makul düzenleme yapmama", "İşyerinde yıldırma"],
    "Md. 4'e göre ayrı tutma, ayrımcılık talimatı, çoklu, doğrudan ve dolaylı ayrımcılık, işyerinde yıldırma, makul düzenleme "
    "yapmama, taciz ve varsayılan temele dayalı ayrımcılık Kanun kapsamındaki türlerdir.", zorluk="easy")

P.sayisal("TİHEK md. 18",
    f"{T}, Kurumun başvuruyu sonuçlandırma süresi Başkan tarafından bir defaya mahsus en fazla kaç ay uzatılabilir?",
    "3", ["1", "2", "4", "6"],
    "Md. 18/1'e göre üç aylık sonuçlandırma süresi Başkan tarafından bir defaya mahsus olmak üzere en fazla üç ay uzatılabilir.",
    zorluk="hard")

P.q("TİHEK md. 4",
    "Bir işçi, işyerindeki ayrımcılığa ilişkin idari süreçte tanıklık yaptığı için işverence olumsuz muameleye maruz "
    f"kalmıştır.\n\n{T}, bu muamele hakkında aşağıdakilerden hangisi doğrudur?",
    "Ayrımcılık teşkil eder.",
    ["Ayrımcılık sayılmaz.",
     "Sadece disiplin konusudur.",
     "Sadece işçi sendikalıysa ayrımcılıktır.",
     "Sadece yargı süreçlerinde ayrımcılıktır."],
    "Md. 4/2'ye göre eşit muamele ilkesine uyulması veya ayrımcılığın önlenmesi amacıyla idari ya da adli süreçleri başlatan "
    "veya bu süreçlere katılan kişilerin bu nedenle maruz kaldıkları olumsuz muameleler de ayrımcılık teşkil eder.",
    zorluk="hard")

P.q("TİHEK md. 6",
    f"{T}, istihdamda ayrımcılık yasağına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yasak sadece İş Kanunu işlerini kapsar.",
    ["İş ilanı ve işe alım süreçlerini kapsar.",
     "Gebelik gerekçesiyle başvuru reddedilemez.",
     "Serbest mesleğe kabulde de uygulanır.",
     "Kamu kurumlarında istihdamı da kapsar."],
    "Md. 6/5'e göre 4857 sayılı İş Kanunu kapsamına girmeyen her türlü iş ve iş görme sözleşmeleri de bu madde kapsamındadır.")

P.sayisal("TİHEK md. 18",
    f"{T}, uzlaşmayla sonuçlanmayan başvurulara ilişkin rapor müzekkeresi kaç gün içinde Kurula sunulur?",
    "20", ["7", "10", "15", "30"],
    "Md. 18/4'e göre uzlaşma yoluyla sonuçlandırılamayan başvurular ve incelemeler hakkında ilgili rapora ilişkin müzekkere yirmi "
    "gün içinde Kurula sunulur.", zorluk="hard")

P.q("TİHEK md. 6",
    f"{T}, işverenin istihdam başvurusunu reddedemeyeceği gerekçeler arasında aşağıdakilerden hangisi açıkça "
    "sayılmıştır?",
    "Gebelik, annelik ve çocuk bakımı",
    ["Mesleki yetersizlik",
     "Aranan diplomanın bulunmaması",
     "Deneme çalışmasındaki başarısızlık",
     "İlan edilen kadronun dolması"],
    "Md. 6/3'e göre işveren istihdam başvurusunu gebelik, annelik ve çocuk bakımı gerekçeleriyle reddedemez.")

P.q("TİHEK md. 6",
    f"{T}, istihdamda ayrımcılık yasağının kapsamına aşağıdakilerden hangisi girmez?",
    "İşverenin kişisel dostluk ilişkileri",
    ["Mesleki eğitime erişim",
     "Meslekte yükselme",
     "Hizmet içi eğitim",
     "Sosyal menfaatler"],
    "Md. 6/2'ye göre yasak iş ilanı, işyeri, çalışma şartları, mesleki rehberlik ve eğitim, meslekte yükselme, hizmet içi eğitim "
    "ve sosyal menfaatler gibi hususları da kapsar.")

P.q("TİHEK md. 7",
    f"{T}, aşağıdakilerden hangisi ayrımcılık iddiasının ileri sürülemeyeceği hâllerden biri değildir?",
    "İşverenin kişisel tercihine dayalı işe almama",
    ["Zorunlu mesleki gereklilikle orantılı farklı muamele",
     "Sadece belli cinsiyetin istihdamını zorunlu kılan durum",
     "Hizmetin zorunluluğuyla orantılı yaş sınırı",
     "Dini kurumda din eğitimi için aynı dinden istihdam"],
    "Md. 7'ye göre zorunlu mesleki gereklilik, belli cinsiyeti zorunlu kılan durumlar, orantılı yaş sınırı ve dini kurumlarda din "
    "hizmeti için aynı dinden istihdam gibi hâllerde ayrımcılık iddiası ileri sürülemez; kişisel tercih bu hâllerden değildir.")

P.q("TİHEK md. 7",
    f"{T}, eşitsizlikleri ortadan kaldırmaya yönelik farklı muameleye ilişkin aşağıdakilerden hangisi doğrudur?",
    "Meşru sayılır.",
    ["Kural olarak ayrımcılıktır.",
     "Sadece kamu kurumlarında mümkündür.",
     "Sadece yaşa dayalı olabilir.",
     "Kurul izniyle ayrımcılık sayılmaz."],
    "Md. 7/f'ye göre eşitsizlikleri ortadan kaldırmaya yönelik, gerekli, amaca uygun ve orantılı farklı muamele hâlinde "
    "ayrımcılık iddiası ileri sürülemez.")

P.q("TİHEK md. 17",
    f"{T}, Kuruma başvuruya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Başvurular için başvuru harcı alınır.",
    ["Başvuru valilik aracılığıyla yapılabilir.",
     "Başvuru kaymakamlık aracılığıyla yapılabilir.",
     "Tüzel kişiler de başvurabilir.",
     "Başvuru dava açma süresini durdurur."],
    "Md. 17/1'e göre ayrımcılıktan zarar gördüğünü iddia eden her gerçek ve tüzel kişi Kuruma başvurabilir; başvurulardan "
    "herhangi bir ücret alınmaz.", zorluk="easy")

P.q("TİHEK md. 17",
    f"{T}, aşağıdakilerden hangisi Kuruma başvurunun konusu olamaz?",
    "Hâkimler ve Savcılar Kurulu kararları",
    ["İşverenin işe alım kararı",
     "Otelin konaklama hizmetini reddetmesi",
     "Kiraya verenin ayrımcı reddi",
     "Derneğin üyelik reddi"],
    "Md. 17/4'e göre yasama ve yargı yetkisinin kullanılmasına ilişkin işlemler, Hâkimler ve Savcılar Yüksek Kurulu kararları ve "
    "Anayasanın yargı denetimi dışında bıraktığı işlemler başvurunun konusu olamaz.", zorluk="hard")

P.q("TİHEK md. 17",
    f"{T}, İş Kanunu md. 5 kapsamındaki ayrımcılık iddialarıyla Kuruma başvuruya ilişkin aşağıdakilerden hangisi doğrudur?",
    "Şikâyet usulü izlenip sonuç alınamazsa yapılır.",
    ["Doğrudan ve ilk olarak Kuruma yapılır.",
     "Kuruma başvuru yapılamaz.",
     "Sadece sendika aracılığıyla yapılır.",
     "Sadece iş mahkemesi kararından sonra yapılır."],
    "Md. 17/5'e göre 4857 sayılı Kanunun 5. maddesi kapsamındaki ayrımcılık iddialarına ilişkin başvurular, o Kanundaki şikâyet "
    "usulleri izlendikten sonra yaptırım kararı alınmadığı hâllerde yapılabilir.", zorluk="hard")

P.q("TİHEK md. 17",
    f"{T}, telafisi güç zarar ihtimali bulunan hâllerde Kurumun başvuruyu kabulüne ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Düzeltme talebi şartı aranmayabilir.",
    ["Başvuru kabul edilemez.",
     "Önce dava açılması şarttır.",
     "Başvuru için ücret alınır.",
     "Başvuru sadece Başkanlıkça sözlü alınır."],
    "Md. 17/2'ye göre Kurum, telafisi güç veya imkânsız zararların doğması ihtimali bulunan hâllerde önce ilgili taraftan "
    "düzeltme istenmesi şartını aramadan başvuruları kabul edebilir.")

P.q("TİHEK md. 18",
    f"{T}, uzlaşmaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Uzlaşma beyanları davada delil olabilir.",
    ["Başkan tarafları uzlaşmaya davet edebilir.",
     "Uzlaşma mağdura tazminat ödenmesini içerebilir.",
     "Uzlaşma bir ay içinde sonuçlandırılır.",
     "Uzlaşma ihlale son verilmesini içerebilir."],
    "Md. 18/3'e göre uzlaşma müzakereleri sırasında yapılan tespitler, beyanlar veya açıklamalar herhangi bir soruşturma, "
    "kovuşturma veya davada delil olarak kullanılamaz.", zorluk="hard")

P.q("TİHEK md. 18",
    f"{T}, Kurul, konusu suç teşkil eden bir ayrımcılık yasağı ihlali tespit ederse ne yapar?",
    "Suç duyurusunda bulunur.",
    ["Failin tutuklanmasına karar verir.",
     "Sadece uyarı yazısı gönderir.",
     "Dosyayı kapatır.",
     "Hapis cezası verir ve kararı ilan eder."],
    "Md. 18/5'e göre Kurul konusu suç teşkil eden insan hakları veya ayrımcılık yasağı ihlallerini tespit ederse suç duyurusunda "
    "bulunur.")

P.q("TİHEK md. 21",
    f"{T}, münhasıran ayrımcılık yasağının ihlali iddiasıyla yapılan başvurularda ispat yüküne ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Kuvvetli emarede ispat karşı tarafa geçer.",
    ["İspat yükü sadece başvurandadır.",
     "İspat yükü inceleme yapan Kurum personelindedir.",
     "İspat aranmaz.",
     "Başvuranın tanık göstermesi yeterlidir."],
    "Md. 21'e göre başvuranın kuvvetli emareleri ve karine oluşturan olguları ortaya koyması hâlinde karşı tarafın ayrımcılık "
    "yasağını ve eşit muamele ilkesini ihlal etmediğini ispat etmesi gerekir.")

P.q("TİHEK md. 25",
    f"{T}, idari para cezasının belirlenmesinde dikkate alınan unsurlar arasında aşağıdakilerden hangisi yer almaz?",
    "Mağdurun siyasi görüşü",
    ["İhlalin etki ve sonuçlarının ağırlığı",
     "Failin ekonomik durumu",
     "Çoklu ayrımcılığın ağırlaştırıcı etkisi",
     "İhlalin sonuçlarının ağırlığı"],
    "Md. 25/1'e göre idari para cezasında ihlalin etki ve sonuçlarının ağırlığı, failin ekonomik durumu ve çoklu ayrımcılığın "
    "ağırlaştırıcı etkisi dikkate alınır.")

P.q("TİHEK md. 25",
    f"{T}, kamu kurumlarına verilen idari para cezasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Rücu edilir.",
    ["Kamu kurumlarına ceza verilemez.",
     "Ceza Hazine tarafından affedilir.",
     "Ceza mağdura ödenir.",
     "Ceza sadece uyarıya dönüştürülür."],
    "Md. 25/2'ye göre kamu kurum ve kuruluşlarına uygulanan idari para cezası, ayrımcı uygulamaya kusuruyla sebebiyet veren "
    "memur ve diğer kamu görevlilerine rücu edilir.")

P.q("TİHEK md. 25",
    f"{T}, Kanunda hüküm bulunmayan hâllerde idari yaptırımlara hangi kanun hükümleri uygulanır?",
    "Kabahatler Kanunu",
    ["Türk Ceza Kanunu", "Vergi Usul Kanunu", "İdari Yargılama Usulü Kanunu", "Hukuk Muhakemeleri Kanunu"],
    "Md. 25/6'ya göre Kanunda hüküm bulunmayan hâllerde idari yaptırımlara ilişkin olarak 5326 sayılı Kabahatler Kanunu "
    "hükümleri uygulanır.", zorluk="easy")

P.q("TİHEK md. 5",
    f"{T}, ayrımcılık yasağının kapsamına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kamuya açık binalara erişim kapsam dışıdır.",
    ["Sağlık hizmeti sunanlar ayrımcılık yapamaz.",
     "Konut kiralanmasında ayrımcılık yapılamaz.",
     "Sendika üyeliğinde ayrımcılık yapılamaz.",
     "Engellilerin ihtiyaçları dikkate alınır."],
    "Md. 5/1'e göre ayrımcılık yasağı kamuya açık hizmetlerin sunulduğu alanlar ve binalara erişimi de kapsar.")

P.q("TİHEK md. 3",
    f"{T}, ayrımcılık yasağının ihlali hâlinde görevli kamu kurumlarının yükümlülükleri arasında aşağıdakilerden hangisi "
    "yer almaz?",
    "Mağdura kendi bütçesinden maaş bağlamak",
    ["İhlalin sona erdirilmesi",
     "Sonuçlarının giderilmesi",
     "Tekrarlanmasının önlenmesi",
     "Adli ve idari yoldan takibi"],
    "Md. 3/3'e göre görevli kamu kurumları ihlalin sona erdirilmesi, sonuçlarının giderilmesi, tekrarlanmasının önlenmesi ve adli "
    "ve idari yoldan takibi için gerekli tedbirleri almakla yükümlüdür.")

P.q("TBK md. 417",
    f"{B}, işverenin işçinin kişiliğini koruma borcuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Psikolojik ve cinsel tacize karşı önlem almalıdır.",
    ["Sadece fiziksel güvenliği sağlamakla yükümlüdür.",
     "Taciz iş dışında olursa önlem alamaz.",
     "Önlem alma yükümlülüğü sendikaya aittir.",
     "Önlem yükümlülüğü sadece kamu işverenlerine aittir."],
    "Md. 417'ye göre işveren işçinin kişiliğini korumak, dürüstlüğe uygun bir düzen sağlamak ve özellikle psikolojik ve cinsel "
    "tacize karşı gerekli önlemleri almakla yükümlüdür.")

P.q("TBK md. 417",
    f"{B}, işverenin kanuna ve sözleşmeye aykırı davranışı nedeniyle işçinin kişilik haklarının ihlaline bağlı zararların "
    "tazmini hangi sorumluluk hükümlerine tabidir?",
    "Sözleşmeye aykırılık hükümlerine",
    ["Haksız fiil hükümlerine",
     "Sebepsiz zenginleşme hükümlerine",
     "Kusursuz sorumluluk hükümlerine",
     "Vekâletsiz iş görme hükümlerine"],
    "Md. 417'ye göre işverenin kanuna ve sözleşmeye aykırı davranışı nedeniyle işçinin ölümü, vücut bütünlüğünün zedelenmesi veya "
    "kişilik haklarının ihlaline bağlı zararların tazmini sözleşmeye aykırılıktan doğan sorumluluk hükümlerine tabidir.",
    zorluk="hard")

P.q("TBK md. 417",
    f"{B}, iş sağlığı ve güvenliğine ilişkin yükümlülüklere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İşçi alınan güvenlik önlemlerine uymakla yükümlü değildir.",
    ["İşveren gerekli her türlü önlemi alır.",
     "İşveren araç ve gereçleri noksansız bulundurur.",
     "İşçi alınan önlemlere uymakla yükümlüdür.",
     "İşveren tacize uğrayanın daha fazla zarar görmesini önler."],
    "Md. 417'ye göre işveren iş sağlığı ve güvenliği için gerekli her türlü önlemi alır; işçiler de alınan her türlü önleme "
    "uymakla yükümlüdür.")

P.oncul("TİHEK md. 2",
    f"{T} aşağıdaki kavramlar değerlendirilmektedir:",
    ["Doğrudan ayrımcılık", "Performans primi", "Ayrı tutma", "Kıdem tazminatı"],
    "Yukarıdakilerden hangileri Kanunda tanımlanan ayrımcılık kavramlarıdır?",
    "I ve III",
    ["Yalnız I", "I ve II", "I ve III", "II ve IV", "I, III ve IV"],
    "Md. 2 ve 4'e göre doğrudan ayrımcılık (I) ve ayrı tutma (III) Kanunda tanımlanan ayrımcılık türleridir; performans primi (II) "
    "ve kıdem tazminatı (IV) bu kavramlardan değildir.")

P.q("İK md. 5",
    "Bir işyerinde belirli süreli iş sözleşmesiyle çalışan işçiye, aynı işi yapan belirsiz süreli işçilere tanınan yemek "
    f"yardımı esaslı bir sebep olmaksızın verilmemektedir.\n\n{K}, bu uygulama hakkında aşağıdakilerden hangisi doğrudur?",
    "Eşit davranma ilkesine aykırıdır.",
    ["İşverenin takdir hakkıdır.",
     "Sadece toplu sözleşme varsa aykırıdır.",
     "Belirli süreli işçiye yardım verilmez.",
     "İşçi talep etmedikçe sorun yoktur."],
    "Md. 5'e göre işveren esaslı sebepler olmadıkça belirsiz süreli çalışan işçi karşısında belirli süreli çalışan işçiye farklı "
    "işlem yapamaz.")

P.q("TİHEK md. 6",
    f"{T}, serbest meslek alanında ayrımcılık yasağının kapsamına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kabul, ruhsat ve disiplinde yasak vardır.",
    ["Serbest meslek yasağın kapsamı dışındadır.",
     "Sadece ruhsatta ayrımcılık yasaktır.",
     "Disiplin işlemleri kapsam dışıdır.",
     "Sadece kamu görevlileri kapsamdadır."],
    "Md. 6/4'e göre serbest mesleğe kabul, ruhsat, kayıt, disiplin ve benzeri hususlar bakımından ayrımcılık yapılamaz.")

P.q("TİHEK md. 7",
    f"{T}, vatandaş olmayanlara ilişkin farklı muameleye ilişkin aşağıdakilerden hangisi doğrudur?",
    "Giriş-ikamet şartı farkı meşrudur.",
    ["Her türlü farklı muamele ayrımcılıktır.",
     "Vatandaş olmayanlar Kanun kapsamı dışındadır.",
     "Sadece çalışma izni farkı meşrudur.",
     "Kurul izni olmadan bir fark yapılamaz."],
    "Md. 7/g'ye göre vatandaş olmayanların ülkeye giriş ve ikametlerine ilişkin şartlarından ve hukuki statülerinden kaynaklanan "
    "farklı muamele hâlinde ayrımcılık iddiası ileri sürülemez.")

P.q("TİHEK md. 5",
    f"{T}, dernek, vakıf ve sendikalara üyelikte ayrımcılık yasağına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tüzük istisnaları dışında yasaktır.",
    ["Bu kuruluşlar yasak kapsamı dışındadır.",
     "Sadece organlara seçilmede yasak vardır.",
     "Üyeliğin sonlandırılması kapsam dışıdır.",
     "Sadece siyasi partiler kapsamdadır."],
    "Md. 5/4'e göre dernek, vakıf, sendika, siyasi parti ve meslek örgütlerine üye olma, organlara seçilme, üyelikten yararlanma "
    "ve üyeliğin sonlandırılmasında mevzuat veya tüzükteki istisnalar dışında ayrımcılık yapılamaz.")

P.q("TİHEK md. 17",
    f"{T}, dava açma süresi içinde Kuruma yapılan başvurunun dava açma süresine etkisi nedir?",
    "Süreyi durdurur.",
    ["Süreyi keser ve yeniden başlatır.",
     "Süreye etkisi yoktur.",
     "Süreyi iki katına çıkarır.",
     "Dava hakkını ortadan kaldırır."],
    "Md. 17/3'e göre dava açma süresi içinde Kuruma yapılan başvurular işlemeye başlamış olan dava açma süresini durdurur.")

P.q("TİHEK md. 2",
    f"{T}, bir kişinin kendi adına işlem yapmaya yetkili kıldığı kişilere ayrımcılık yapılmasına yönelik talimat vermesi "
    "hangi kavramla ifade edilir?",
    "Ayrımcılık talimatı",
    ["Doğrudan ayrımcılık", "Ayrı tutma", "Çoklu ayrımcılık", "Makul düzenleme yapmama"],
    "Md. 2/b'ye göre bir kişinin kendi nam veya hesabına işlem yapmaya yetkili kıldığı kişilere veya kamu görevlisinin diğer "
    "kişilere verdiği ayrımcılık yapılmasına yönelik talimat ayrımcılık talimatıdır.")

P.q("TİHEK md. 2",
    f"{T}, doğrudan ayrımcılığa ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ayrımcılık temeline dayalı her türlü farklı muameledir.",
    ["Görünüşte tarafsız uygulamanın sonucudur.",
     "Sadece kamu görevlilerince yapılabilir.",
     "Birden fazla temel içermesi şarttır.",
     "Sadece iş ilişkisinde söz konusu olur."],
    "Md. 2/d'ye göre doğrudan ayrımcılık, karşılaştırılabilir durumdakilere kıyasla eşit yararlanmayı Kanundaki ayrımcılık "
    "temellerine dayanarak engelleyen veya zorlaştıran her türlü farklı muameledir.")

P.q("TİHEK md. 6",
    f"{T}, uygulamalı iş deneyimi edinmek üzere işyerinde bulunan kişiye ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ayrımcılık yasağı bu kişiyi de korur.",
    ["İşçi olmadığı için korunmaz.",
     "Sadece stajyer sözleşmesi varsa korunur.",
     "Sadece kamu işyerlerinde korunur.",
     "Sadece yazılı başvurusu varsa korunur."],
    "Md. 6/1'e göre işveren, uygulamalı iş deneyimi edinmek üzere işyerinde bulunan veya bu amaçla başvuran kişi aleyhine de "
    "işle ilgili süreçlerin herhangi birinde ayrımcılık yapamaz.")

P.q("TİHEK md. 17",
    f"{T}, resen yapılan incelemelerde mağdurun açık rızasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Mağdur belirlenebilir olsa da rıza aranmaz.",
    ["Belirlenebilir mağdurun açık rızası alınır.",
     "Kanuni temsilcinin rızası da alınabilir.",
     "Çocuğun yüksek yararında temsilci rızası aranmaz.",
     "Rıza açık olmalıdır."],
    "Md. 17/6'ya göre resen incelemelerde ihlal mağdurunun şahsen belirlenebildiği durumlarda kendisinin veya kanuni "
    "temsilcisinin açık rızası şarttır; çocuğun yüksek yararı gerektirirse temsilci rızası aranmaz.", zorluk="hard")

P.q("TİHEK md. 9",
    f"{T}, Türkiye İnsan Hakları ve Eşitlik Kurumunun görevleri arasında aşağıdakilerden hangisi yer almaz?",
    "Ayrımcılık davalarında hüküm kurmak",
    ["Ayrımcılık yasağı ihlallerini incelemek",
     "Ulusal önleme mekanizması olarak görev yapmak",
     "Başvuranlara hukuki süreçlerde yol göstermek",
     "Yıllık insan hakları raporları hazırlamak"],
    "Md. 9'a göre Kurum ihlalleri inceler, karara bağlar, ulusal önleme mekanizması olarak görev yapar, başvuranlara yol gösterir "
    "ve rapor hazırlar; yargısal hüküm kurmak mahkemelerin görevidir.")

P.q("İK md. 5",
    f"{K}, eşit davranma ilkesine aykırılık iddiasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sendikal ayrımcılık hükümleri saklıdır.",
    ["Sendikal ayrımcılık bu maddeyle kaldırılmıştır.",
     "Tazminat sınırsızdır.",
     "Sadece kadın işçiler için geçerlidir.",
     "İspat yükü baştan işverendedir."],
    "Md. 5'e göre sendikal ayrımcılığa ilişkin özel hükümler saklıdır; eşit davranma tazminatı dört aylık ücrete kadardır.",
    zorluk="hard")

P.q("TİHEK md. 3",
    f"{T}, ayrımcılık yasağı bakımından gerçek ve özel hukuk tüzel kişilerinin yükümlülüğüne ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Yetki alanlarında eşitliği sağlayıcı tedbir alırlar.",
    ["Sadece kamu kurumları yükümlüdür.",
     "Sadece Kurumun talebiyle yükümlüdürler.",
     "Sadece yazılı şikâyet varsa yükümlüdürler.",
     "Sadece ceza soruşturmasında yükümlüdürler."],
    "Md. 3/4'e göre ayrımcılık yasağı bakımından sorumluluk altındaki gerçek ve özel hukuk tüzel kişileri yetki alanlarındaki "
    "konularda ayrımcılığın tespiti, ortadan kaldırılması ve eşitliğin sağlanması için gerekli tedbirleri almakla yükümlüdür.")

if __name__ == "__main__":
    sys.exit(P.yaz())
