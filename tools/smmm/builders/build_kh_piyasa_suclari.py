#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM Sermaye Piyasası Mevzuatı — Piyasa Suçları, 3×20.

Dayanaklar 17.07.2026 tarihinde 6362 sayılı Kanunun güncel metni üzerinden
doğrulanmıştır. Güncel metinde bilgi suistimali m.105, piyasa dolandırıcılığı
m.106, bunların istisnaları m.107 ve piyasa bozucu eylemler m.103'tedir.
"""
from topic_pack_builder import write_topic


def r(scenario, focus, correct, distractors, why, focus_why, ref, difficulty="medium"):
    return {
        "scenario": scenario, "focus": focus, "correct": correct,
        "distractors": distractors,
        "focus_distractors": distractors[2:] + distractors[:2],
        "why": why, "focus_why": focus_why, "ref": ref,
        "difficulty": difficulty,
    }


RULES = [
    r(
        "Yatırımcı, suçun unsurlarını oluşturmayan ancak meşru bir gerekçeyle açıklanamayan işlemlerle piyasanın güvenli ve istikrarlı işleyişini bozmuştur. Fiilin hukuki niteliği nedir?",
        "Piyasa bozucu eylem ile sermaye piyasası suçu arasındaki temel yaptırım farkı nedir?",
        "Piyasa bozucu eylemdir ve kural olarak idari yaptırıma tabidir",
        ["Her durumda yalnız disiplin uyarısı gerektiren meslek kuralıdır", "Piyasa suçu sayılır ve yalnız tazminat yaptırımı doğurur", "Hukuka uygun işlemdir ve hiçbir yaptırım uygulanamaz", "Yalnız borsa üyeliğini kendiliğinden sona erdiren özel borçtur"],
        "Kanun m.103, borsanın güven, açıklık ve istikrarını bozan eylemleri başka bir suça vücut vermemeleri kaydıyla piyasa bozucu eylem sayar ve idari para cezasına bağlar.",
        "Suçun kanuni unsurları oluşursa ceza hukuku hükümleri uygulanır; oluşmazsa eylem yine m.103 kapsamında idari yaptırım doğurabilir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.103", "easy",
    ),
    r(
        "Bir kişi gerçek ekonomik el değiştirme amacı olmadan kendi hesapları arasında alım satım yaparak piyasada yoğun talep görünümü oluşturmuştur. Suç oluşmadığı varsayımında hangi kategori gündeme gelir?",
        "Meşru ekonomik gerekçesi bulunmayan kendinden kendine veya karşılıklı işlemler nasıl değerlendirilir?",
        "Piyasa bozucu eylem olarak idari yaptırım da gündeme gelir",
        ["Her zaman fiyat istikrarı işlemi sayılarak istisna uygulanır", "Yalnız muhasebe kaydı sayılır ve piyasa etkisi incelenmez", "Sadece temettü dağıtımı kabul edilir ve işlem geçerli kalır", "Otomatik olarak yatırım fonu katılma payı ihracına dönüşür"],
        "Kanun m.103/1-a, meşru ekonomik veya finansal gerekçeyle açıklanamayan kendinden kendine ve karşılıklı işlemleri, suç oluşturmadıkları takdirde piyasa bozucu eylem sayar.",
        "İşlemin görünürde iki taraflı olması yeterli değildir; ekonomik gerçeklik, hesap bağlantıları ve piyasada yarattığı görünüm birlikte değerlendirilir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.103/1-a", "medium",
    ),
    r(
        "Yatırımcı, ekonomik gerekçe olmaksızın yalnız açılış fiyatını yukarı çekmek amacıyla çok sayıda emir vermiş; fiil suç düzeyine ulaşmamıştır. Sonuç nedir?",
        "Açılış, kapanış, gün sonu veya vade sonu fiyatını etkilemeye yönelik emirler suç oluşturmadığında hangi kapsamdadır?",
        "Piyasa bozucu eylem kapsamında değerlendirilir",
        ["Meşru piyasa yapıcılığı sayılır", "Yalnız yatırım danışmanlığı faaliyeti kabul edilir", "Hiçbir piyasa kuralıyla ilişkili olmadığı varsayılır", "Sadece ihraççının pay defteri kaydı olarak görülür"],
        "Kanun m.103/1-b, meşru gerekçesi bulunmayan ve açılış, kapanış, gün sonu veya vade sonu fiyatlarını etkilemeye yönelik emirleri suç oluşmadığında piyasa bozucu eylem sayar.",
        "Emrin mutlaka gerçekleşmesi şart değildir; fiyat oluşumunu etkilemeye yönelik emir verme davranışı idari değerlendirmeye konu olabilir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.103/1-b", "medium",
    ),
    r(
        "Bir yatırımcı süreklilik gösterecek biçimde çok küçük miktarlı alımlarla fiyatı kademeli yükseltmiş ve bunu meşru gerekçeyle açıklayamamıştır. Suç oluşmadığında nitelendirme nedir?",
        "Sürekli küçük miktarlı fiyat yükseltici veya düşürücü işlemler hangi şartla piyasa bozucu eylem sayılır?",
        "Meşru gerekçe yoksa ve suç oluşmamışsa bu kapsamdadır",
        ["Küçük miktar her durumda hukuka uygundur", "Fiyat yükselmişse otomatik olarak geri alım programı sayılır", "Yalnız tek sefer yapılırsa süreklilik şartı gerçekleşmiş olur", "İşlem yatırımcıya zarar verdiyse hiçbir inceleme yapılamaz"],
        "Kanun m.103/1-c, meşru ekonomik veya finansal gerekçe olmaksızın süreklilik arz eden küçük miktarlı fiyat yükseltici ya da düşürücü alım satımları kapsar.",
        "Miktarın küçük olması tek başına güvenli alan yaratmaz; süreklilik, yönsel fiyat etkisi, gerekçe ve suç unsurlarının bulunup bulunmadığı incelenir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.103/1-c", "hard",
    ),
    r(
        "Kurul idari para cezası uygulamadan önce ilgiliden savunma istemiş; ilgili 17.07.2026 tarihinde tebliğden sonra on beş gün boyunca cevap vermemiştir. Sonuç nedir?",
        "17.07.2026 itibarıyla sermaye piyasası idari para cezasından önce savunma usulü nasıl işler?",
        "Savunma alınır; süresinde verilmezse haktan feragat edilmiş sayılır",
        ["Savunma istenmeden her durumda kesin hapis cezası verilir", "Süre geçince idari süreç kendiliğinden ve kesin olarak düşer", "Savunma yalnız borsa genel kurulunda sözlü yapılabilir", "Cevap verilmemesi fiilin hukuka uygun olduğunu kanıtlar"],
        "Kanun m.104, idari para cezasından önce savunma alınmasını; tebliğden itibaren on beş gün içinde savunma verilmezse savunma hakkından feragat edilmiş sayılmasını düzenler.",
        "Savunma istemi idari yaptırım usulünün parçasıdır. Süresinde cevap verilmemesi dosyayı düşürmez; feragat sonucu doğurur.",
        "6362 sayılı Sermaye Piyasası Kanunu m.104/1", "medium",
    ),
    r(
        "Şirket birleşmesinin henüz açıklanmamış ve pay fiyatını etkileyebilecek kesin bilgisini kullanan yönetici, kendi hesabına pay alarak menfaat sağlamıştır. Hangi suç oluşur?",
        "Bilgi suistimali suçunun temel maddi unsurları hangileridir?",
        "Kamuya açıklanmamış etkili bilgiyi kullanarak menfaat sağlama",
        ["Kamuya açıklanmış eski fiyatları inceleyerek yatırım kararı verme", "Yanlış söylenti yaymadan yalnız genel ekonomik veriyi yorumlama", "Onaylı izahnameyi mevzuata uygun biçimde yayımlama", "Piyasa fiyatı düşen her araçta zarar etmiş olma"],
        "Kanun m.105/1, araç veya ihraççı hakkında fiyatı, değeri ya da yatırımcı kararını etkileyebilecek ve henüz açıklanmamış bilgiyi kullanarak menfaat sağlamayı bilgi suistimali sayar.",
        "Bilginin kamuya açıklanmamış ve etkili nitelikte olması, kullanılması ve bu kullanım yoluyla menfaat elde edilmesi birlikte aranır.",
        "6362 sayılı Sermaye Piyasası Kanunu m.105/1", "easy",
    ),
    r(
        "Yönetici, herkesin KAP üzerinden bildiği bir açıklamayı okuyup işlem yapmış ve kâr elde etmiştir. Yalnız bu olgularla bilgi suistimali oluşur mu?",
        "Bilgi suistimaline konu bilginin kamuya açıklanmış olması suç değerlendirmesini nasıl etkiler?",
        "Hayır; suç için henüz kamuya duyurulmamış bilgi gerekir",
        ["Evet; kamuya açıklanan her bilgi içsel bilgi sayılır", "Evet; işlemde kâr varsa bilginin niteliği önem taşımaz", "Hayır; fakat yalnız yabancı yatırımcılar bu suçu işleyebilir", "Evet; KAP açıklaması bilgiyi süresiz olarak gizli hâle getirir"],
        "Kanun m.105, henüz kamuya duyurulmamış nitelikli bilginin kullanılmasını arar. Herkesçe erişilebilir KAP açıklaması tek başına bu unsuru karşılamaz.",
        "Kamuya açıklama, bilginin asimetrik niteliğini kural olarak sona erdirir; başka manipülatif fiiller varsa onlar ayrıca değerlendirilir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.105/1", "easy",
    ),
    r(
        "Çalışan açıklanmamış fiyat etkili bilgiyi kullanarak emir vermiş, fakat işlem sonucunda herhangi bir menfaat sağlamamıştır. Kanundaki temel tanım bakımından ne söylenir?",
        "Bilgi suistimalinin tamamlanması bakımından yalnız bilgiye sahip olmak veya emir vermek yeterli midir?",
        "Hayır; kanuni tanım menfaat elde edilmesini ayrıca arar",
        ["Evet; hiçbir işlem ve menfaat olmadan suç tamamlanır", "Evet; yalnız şirkette çalışmak mahkûmiyet için yeterlidir", "Hayır; çünkü açıklanmamış bilgi hiçbir suçta kullanılamaz", "Evet; aracın fiyatı değişmese bile menfaat varsayılır"],
        "Kanun m.105/1-2, nitelikli bilgiyi kullanarak emir verme, değiştirme veya iptal etme suretiyle menfaat elde edilmesini bilgi suistimali kapsamında düzenler.",
        "Bilgiye erişim tek başına tamamlanmış suç değildir. Kullanım ve menfaat unsurları somut olayda gösterilmelidir; diğer ihlaller saklıdır.",
        "6362 sayılı Sermaye Piyasası Kanunu m.105/1-2", "medium",
    ),
    r(
        "Bir danışman işinin icrası sırasında açıklanmamış fiyat etkili bilgiye ulaşmış, bilginin niteliğini bilerek kendi hesabına işlem yapmış ve menfaat sağlamıştır. Fail kapsamına girer mi?",
        "Bilgi suistimali yalnız ihraççı yöneticileri tarafından mı işlenebilir?",
        "Evet; işi nedeniyle bilgi edinen danışman da fail olabilir",
        ["Hayır; fail yalnız ihraççının yönetim kurulu başkanı olabilir", "Hayır; danışmanların bilgiyi kullanması her durumda serbesttir", "Evet; ancak yalnız kamuya açıklanmış bilgi kullanırsa suç oluşur", "Hayır; fail olabilmek için mutlaka pay sahibi olmak gerekir"],
        "Kanun m.105/2; yönetici ve pay sahiplerinin yanında işi, mesleği veya görevi nedeniyle bilgi edinenleri ve bilginin niteliğini bilen ya da bilmesi gereken kişileri de kapsar.",
        "Fail çevresi unvana göre kapalı değildir; bilgiye erişim yolu, bilginin niteliğine ilişkin farkındalık, kullanım ve menfaat önem taşır.",
        "6362 sayılı Sermaye Piyasası Kanunu m.105/2", "medium",
    ),
    r(
        "Pay sahibi açıklanmamış bilgiyi öğrendikten sonra mevcut satış emrini iptal etmiş ve böylece beklenen kayıptan kaçınarak menfaat elde etmiştir. İşlem türü kapsamda mıdır?",
        "Bilgi suistimalinde nitelikli bilgi kullanılarak hangi emir davranışları menfaatle sonuçlandığında kapsama girer?",
        "Emir verme yanında emri değiştirme veya iptal etme de kapsamdadır",
        ["Yalnız fiziki senet basımı ve imhası kapsama girer", "Sadece gerçekleşen alım emri, iptal hiçbir zaman kapsama girmez", "Yalnız ihraççının genel kurulda oy kullanması kapsamdadır", "Emir davranışı değil yalnız temettü tahsili bu suçu oluşturur"],
        "Kanun m.105/2, açıklanmamış bilgiyi kullanarak alım veya satım emri vermenin yanı sıra verilmiş emri değiştirme veya iptal etme yoluyla menfaat sağlamayı da kapsar.",
        "Menfaat yalnız doğrudan satış kârı değildir; bilgi sayesinde emri değiştirerek veya iptal ederek kayıptan kaçınma da somut olayda değerlendirilebilir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.105/2", "hard",
    ),
    r(
        "Yönetici, görevin olağan icrası dışında açıklanmamış etkili bilgiyi arkadaşına aktarmış; arkadaş bu bilgiyle işlem yapıp menfaat sağlamıştır. Yöneticinin fiili nasıl değerlendirilir?",
        "Açıklanmamış etkili bilginin üçüncü kişiye açıklanması hangi koşullarda bilgi suistimali kapsamına girer?",
        "Olağan görev dışı aktarım ve üçüncü kişinin menfaatiyle kapsam oluşur",
        ["Bilgi üçüncü kişiye aktarılınca her durumda kamuya açıklanmış sayılır", "Arkadaşlık ilişkisi varsa bütün aktarımlar kanuni istisnadır", "Yönetici kendisi işlem yapmadığı için hiçbir sorumluluk doğmaz", "Aktarım yalnız yazılı yapılırsa hukuken yok kabul edilir"],
        "Kanun m.105/3, olağan iş, meslek veya görev açıklaması dışında bilgiyi üçüncü kişiye açıklama ya da erişim sağlama fiilini; üçüncü kişinin işlemle menfaat sağlaması halinde kapsar.",
        "Yöneticinin kendi adına emir vermemesi sorumluluğu otomatik kaldırmaz; bilginin aktarım amacı, olağan görev istisnası ve üçüncü kişinin işlemi incelenir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.105/3", "hard",
    ),
    r(
        "İçsel bilgi sahibi, bilgiyi açıklamadan arkadaşına ilgili payı almasını telkin etmiş; arkadaş telkin doğrultusunda işlem yapıp menfaat sağlamıştır. Hangi hüküm uygulanır?",
        "Açıklanmamış bilgiye dayanılarak üçüncü kişiye alım veya satım tavsiyesi verilmesi ne zaman bilgi suistimali olur?",
        "Telkin üzerine işlem ve menfaat gerçekleştiğinde kapsam doğar",
        ["Tavsiye sözlü ise hiçbir zaman sermaye piyasası ihlali oluşmaz", "Arkadaş tavsiyeyi dinlemezse menfaat sağladığı kabul edilir", "Yalnız payın fiyatı düştüğünde tavsiye kanunen zorunlu olur", "Bilgiyi bilen kişi işlem yapmayınca bütün telkinler serbesttir"],
        "Kanun m.105/3, açıklanmamış bilgiye dayanarak üçüncü kişiye ilgili aracı edinmesi veya elden çıkarması için tavsiye ya da telkini, üçüncü kişinin işlemle menfaat sağlaması halinde kapsar.",
        "Tavsiye ile bilgi suistimali bağlantısı için nitelikli bilgi, telkin, telkin doğrultusunda işlem ve menfaat zinciri değerlendirilir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.105/3", "hard",
    ),
    r(
        "Kurul bilgi suistimali tespit ettiği kişiye, kanundaki istisna gruplarında olmaması şartıyla elde edilen menfaatin belirli katını YTM'ye ödeme imkânını hatırlatmıştır. Ödeme ne sonuç doğurabilir?",
        "Bilgi suistimalinde YTM'ye ödeme yoluyla suç duyurusunda bulunulmaması imkânı kimler için kapalıdır?",
        "Şartlar sağlanırsa Kurul suç duyurusunda bulunmayabilir",
        ["Ödeme her durumda kesinleşmiş mahkûmiyeti kendiliğinden siler", "İmkân örgüt kuranlar ve önceki mahkûmiyeti olanlara da zorunludur", "YTM'ye ödeme yalnız yatırımcı hesabını kapatmaya yarar", "Ödeme yapılırsa fiil piyasa yapıcılığına dönüşür"],
        "Kanun m.105/4, daha önce kesinleşmiş Kanun mahkûmiyeti bulunanlar ile bu suç için örgüt kuran, yöneten veya üye olanlar hariç, belirlenen ödemenin yapılması halinde Kurulca suç duyurusu yapılmamasını öngörür.",
        "Bu mekanizma mahkeme hükmünü silen genel af değildir; Kurul tespiti, kişi bakımından istisna bulunmaması ve YTM'ye kanunda öngörülen ödemenin nakden yapılması şartlarına bağlıdır.",
        "6362 sayılı Sermaye Piyasası Kanunu m.105/4", "hard",
    ),
    r(
        "İhraççı yöneticisi Kurulun belirlediği dönemde içsel bilgi bulunmaksızın pay alım satımından net kazanç elde etmiştir. 17.07.2026 itibarıyla yükümlülüğü nedir?",
        "17.07.2026 itibarıyla ihraççı yönetim kurulu üyesinin belirlenen dönemdeki net alım satım kazancı için hangi esas uygulanır?",
        "Net kazancı ihraççıya vermesi gerekir",
        ["Kazancı MKK personeline kişisel bağış olarak ödemesi gerekir", "Kazancı hiçbir koşulda açıklamaması ve saklaması gerekir", "Bütün paylarını bedelsiz olarak borsaya devretmesi gerekir", "Net kazanç oluşsa da hiçbir yükümlülük doğmaz"],
        "Kanun m.105/5, Kurulca izin verilen haller dışında belirlenen dönemde ilgili araçlardan kazanç sağlayan yönetim kurulu üyesi ve yöneticinin net kazancı ihraççıya vermesini öngörür.",
        "Bu yükümlülük için mutlaka açıklanmamış bilgi bulunması aranmaz; kısa dönemli yönetici kazancının ihraççıya iadesi ayrı bir koruma mekanizmasıdır.",
        "6362 sayılı Sermaye Piyasası Kanunu m.105/5", "medium",
    ),
    r(
        "Bir grup, meşru ekonomik gerekçe olmadan koordineli emir ve hesap hareketleriyle payın arz ve talebi hakkında yanıltıcı görünüm oluşturmuştur. Hangi suç tipi gündeme gelir?",
        "İşlem bazlı piyasa dolandırıcılığında hangi davranışlar yanlış veya yanıltıcı izlenim amacıyla kullanılır?",
        "İşlem bazlı piyasa dolandırıcılığı oluşabilir",
        ["Yalnız usulsüz halka arz suçu oluşabilir", "Her durumda bilgi suistimali istisnası uygulanır", "Sadece bağımsız denetim sözleşmesi ihlali oluşur", "Bu davranışlar sermaye piyasasıyla ilgisiz sayılır"],
        "Kanun m.106/1-a, meşru gerekçe olmadan fiyat, fiyat değişimi, arz veya talep hakkında yanlış ya da yanıltıcı izlenim yaratacak alım satım, emir, emir iptali ve hesap hareketlerini kapsar.",
        "Fiil tek başına veya birlikte hareket edenlerce gerçekleştirilebilir. İşlemin ekonomik gerçekliği ve yanıltıcı piyasa görünümü suç ayrımında önemlidir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.106/1-a", "easy",
    ),
    r(
        "Yatırımcı gerçek bir portföy ihtiyacı nedeniyle pay satmış ve piyasa fiyatı düşmüştür. Yalnız fiyat etkisi, işlem bazlı piyasa dolandırıcılığı için yeterli midir?",
        "İşlem bazlı piyasa dolandırıcılığında meşru gerekçe ve yanıltıcı izlenim nasıl değerlendirilir?",
        "Hayır; meşru gerekçesizlik ve yanıltıcı görünüm birlikte incelenir",
        ["Evet; fiyatı etkileyen her işlem otomatik olarak suçtur", "Evet; yatırımcının portföy ihtiyacı kanunen yasaktır", "Hayır; ancak suç için mutlaka fiziki senet basılması gerekir", "Evet; yalnız zarar doğması manevi unsuru kanıtlar"],
        "Kanun m.106/1-a, meşru ekonomik veya finansal gerekçe bulunmaksızın yanıltıcı izlenim yaratacak işlem ve emirleri yaptırıma bağlar.",
        "Normal arz ve talebin fiyatı etkilemesi tek başına suç değildir; işlemin amacı, gerekçesi, örüntüsü ve piyasa görünümündeki yanıltıcılık araştırılır.",
        "6362 sayılı Sermaye Piyasası Kanunu m.106/1-a", "medium",
    ),
    r(
        "Sosyal medya hesabı, pay fiyatını ve yatırımcı kararlarını etkilemek amacıyla gerçeğe aykırı birleşme haberi üretip geniş kitlelere yaymıştır. Hangi suç tipi gündeme gelir?",
        "Bilgi bazlı piyasa dolandırıcılığında iletişim aracı ve içerik bakımından hangi unsurlar aranır?",
        "Yanıltıcı bilgi yaymaya dayalı piyasa dolandırıcılığı",
        ["Yalnız yatırımcı blokajı ihlali", "Mevzuata uygun fiyat istikrarı işlemi", "Sadece genel kurul çağrı usulsüzlüğü", "Kaydi sisteme fiziki belge teslimi"],
        "Kanun m.106/1-b, fiyatı, değeri veya yatırımcı kararını etkileme amacıyla yalan, yanlış ve yanıltıcı bilgi, söylenti, haber, yorum veya rapor hazırlayıp internet dahil medya yoluyla yaymayı kapsar.",
        "Sosyal medya da kanundaki her türlü medya kapsamındadır; bilginin yanıltıcılığı ve piyasayı etkileme amacı somut olayda belirlenir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.106/1-b", "easy",
    ),
    r(
        "İhraççı açıklamak zorunda olduğu olumsuz bilgiyi zamanında açıklamamış; bu sırada yöneticileri birlikte hareket ederek satış emirlerini değiştirmiştir. Nitelendirme nedir?",
        "Zorunlu bilginin açıklanmaması veya geciktirilmesi hangi işlem davranışlarıyla birleşirse piyasa dolandırıcılığı kapsamına girebilir?",
        "Açıklamama ile bağlantılı piyasa dolandırıcılığı gündeme gelir",
        ["Bilginin gizlenmesi bütün işlemleri otomatik olarak meşru kılar", "Yalnız temettü ödeme tarihi değişmiş sayılır", "İşlem yapıldığı için açıklama yükümlülüğü kendiliğinden kalkar", "Bu davranış yalnız kaydi hesap açma usulsüzlüğüdür"],
        "Kanun m.106/1-c, mevzuat gereği açıklanması gereken bilgiyi açıklamayan veya geciktirenlerin bu sırada işlem, emir, değişiklik, iptal ya da hesap hareketi yapmasını ve birlikte hareketi kapsar.",
        "Salt geç açıklama başka ihlaller doğurabilir; bu suç tipinde açıklamama ile kanunda sayılan piyasa işlemi arasında somut bağ aranır.",
        "6362 sayılı Sermaye Piyasası Kanunu m.106/1-c", "hard",
    ),
    r(
        "TCMB para ve döviz kuru politikasını uygulamak amacıyla yetkisi içinde piyasada işlem yapmıştır. Bu işlem bilgi suistimali veya piyasa dolandırıcılığı sayılır mı?",
        "Resmî kurumların para, kur veya kamu borç yönetimi politikası işlemleri hangi güvenli alan kapsamında yer alır?",
        "Hayır; kanunda açıkça sayılan istisnalardandır",
        ["Evet; kamusal amaçla yapılan her işlem otomatik olarak suçtur", "Hayır; fakat yalnız fiziki senet basılırsa istisna uygulanır", "Evet; işlem yapan kurumun yetkili olması sonucu değiştirmez", "Hayır; çünkü TCMB hiçbir sermaye piyasası işlemi yapamaz"],
        "Kanun m.107/1-a, TCMB veya yetkilendirilmiş resmi kurumların para, döviz kuru ya da kamu borç yönetimi politikalarını uygulama amacıyla yaptığı işlemleri istisna sayar.",
        "İstisna kurum adına hareket edenleri de kapsayabilir; işlemin gerçekten belirtilen kamu politikası amacı ve yetki içinde yapılması gerekir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.107/1-a", "easy",
    ),
    r(
        "Halka açık ortaklık, pay geri alım programını Kurul düzenlemelerine tam uygun biçimde uygulamıştır. Sırf fiyat üzerinde etkisi bulunduğu için piyasa dolandırıcılığı oluşur mu?",
        "Geri alım ve çalışanlara pay edindirme programları ne zaman bilgi suistimali veya piyasa dolandırıcılığı sayılmaz?",
        "Kurul düzenlemelerine uygun yürütülürse kanuni istisnadır",
        ["Her geri alım programı düzenlemeye bakılmadan suç oluşturur", "Yalnız yönetici gizli bilgiyle işlem yaparsa istisna doğar", "Programın yazılı olması bütün Kurul kurallarını etkisiz kılar", "Çalışanlara pay tahsisi sermaye piyasasında tamamen yasaktır"],
        "Kanun m.107/1-b, Kurul düzenlemelerine uygun geri alım programları ile çalışanlara pay edindirme ve belirli pay tahsis programlarını istisna kapsamına alır.",
        "Güvenli alan sınırsız değildir; programın Kurul düzenlemelerine uygunluğu ve işlemlerin program kapsamında yapılması gerekir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.107/1-b", "medium",
    ),
    r(
        "İhraç sonrasında fiyat istikrarı işlemleri, önceden belirlenmiş sürede ve Kurulun piyasa yapıcılığı düzenlemelerine uygun yürütülmüştür. Hukuki sonuç nedir?",
        "Fiyat istikrarı ve piyasa yapıcılığı işlemlerinin kanuni istisnadan yararlanması hangi koşula bağlıdır?",
        "Kurul düzenlemelerine uygunluk ve belirlenmiş destek amacı gerekir",
        ["Fiyatın her koşulda sürekli yükselmesi ve hiç düşmemesi gerekir", "İşlemlerin hiçbir kayıt bırakmadan gizlice yapılması gerekir", "Yalnız ihraççı yöneticisinin kişisel hesabı kullanılmalıdır", "Programın süresiz ve kuralsız biçimde yürütülmesi gerekir"],
        "Kanun m.107/1-c, Kurul düzenlemelerine uygun fiyat istikrarı ve piyasa yapıcılığı kapsamında önceden belirlenmiş süreyle fiyat desteği amaçlı işlem ve emirleri istisna sayar.",
        "Her fiyat destekleme girişimi güvenli alan değildir; düzenlemeye uygunluk, münhasır destek amacı ve önceden belirlenmiş süre birlikte aranır.",
        "6362 sayılı Sermaye Piyasası Kanunu m.107/1-c", "medium",
    ),
    r(
        "Şirket onaylı izahname yayımlamadan araçlarını halka arz etmiş; başka bir kişi de Kurul izni olmadan yatırım hizmeti sunmuştur. Hangi suç tipi gündeme gelir?",
        "Usulsüz halka arz ve izinsiz sermaye piyasası faaliyeti bakımından hangi davranışlar suçtur?",
        "Her iki davranış da Kanunda ayrı suç kapsamında düzenlenir",
        ["Yalnız halka arz suçtur; izinsiz faaliyet her durumda serbesttir", "Her iki davranış yalnız özel hukuk sözleşmesini hükümsüz kılar", "Onaysız arz yalnız paylar yükselirse suç sayılır", "İzinsiz faaliyeti yalnız yatırımcı şikâyeti suç hâline getirir"],
        "Kanun m.108, onaylı izahname yayımlamadan halka arzı ve sermaye piyasasında izinsiz faaliyeti, bunlarla birlikte hareket edenleri de kapsayacak biçimde suç sayar.",
        "Halka arzın ve yatırım hizmetinin düzenleyici izin koşulları yatırımcı korunmasının temelidir; fiili zarar doğması suç tanımının zorunlu unsuru değildir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.108", "easy",
    ),
    r(
        "Yatırım kuruluşu yetkilisi, müşterinin saklanan nakdini kendisinin menfaatine kullanmış ve eylemi gizlemek için elektronik kayıtları değiştirmiştir. Hangi suç oluşur?",
        "Sermaye piyasasında güveni kötüye kullanma suçunun koruduğu varlıklar ve yasak fiiller nelerdir?",
        "Güveni kötüye kullanma suçu oluşur",
        ["Yalnız bilgi suistimali istisnası oluşur", "Sadece piyasa yapıcılığı faaliyeti oluşur", "Müşteri varlığı üyenin olduğu için suç oluşmaz", "Yalnız genel kurul usul ihlali oluşur"],
        "Kanun m.109, yatırım kuruluşuna veya belirli fon ve teminat sorumlularına teslim edilen araç, nakit ve kıymetleri menfaate satma, kullanma, rehin, gizleme veya inkâr ile kayıtları bozmayı kapsar.",
        "Müşteri varlığı görevin sağladığı zilyetlik nedeniyle korunur; yetkilinin kurumdaki konumu bu varlığı kendi yararına kullanma hakkı vermez.",
        "6362 sayılı Sermaye Piyasası Kanunu m.109", "easy",
    ),
    r(
        "Kurul denetiminde istenen elektronik kayıtları süresinde vermeyen şirket, bazı belgeleri de gerçeğe aykırı sunarak incelemeyi engellemiştir. Hangi suç tipi gündeme gelir?",
        "Kurula bilgi ve belge vermeme ile denetimi engelleme suçunun fiilleri nelerdir?",
        "Bilgi-belge vermeme ve denetimi engelleme suçu oluşabilir",
        ["Yalnız yatırımcı blokajı kaldırma işlemi oluşur", "Belgeler elektronikse hiçbir yükümlülük bulunmaz", "Sadece halka arz fiyatı değişmiş sayılır", "Denetim engellenince Kurulun yetkisi kendiliğinden sona erer"],
        "Kanun m.111/1; istenen bilgi, belge ve elektronik kayıtları süresinde ve uygun ortamda vermeme, gizleme, yok etme, eksik veya gerçeğe aykırı verme ile görevi engellemeyi suç sayar.",
        "Yükümlülük kâğıt belgelerle sınırlı değildir. Elektronik kayıtların bütünlüğü ve denetim görevlilerinin fiilen çalışabilmesi de korunur.",
        "6362 sayılı Sermaye Piyasası Kanunu m.111/1", "medium",
    ),
    r(
        "Sermaye piyasası kurumu çalışanı, görevi nedeniyle öğrendiği müşteri sırrını kanunen yetkili olmayan bir kişiye açıklamış ve bundan yarar sağlamıştır. Hangi sonuç doğar?",
        "Sır saklama suçunda korunan bilgiler ile yarar sağlama amacı arasındaki ilişki nedir?",
        "Sır saklama suçu oluşur ve yarar amacı cezayı artırır",
        ["Müşteri sırrı açıklanabilir; yarar amacı hukuken önemsizdir", "Yalnız kamuya açıklanmış fiyat verisi sır sayılır", "Açıklama sözlü yapılırsa hiçbir suç oluşmaz", "Çalışanın görevi bütün sırları üçüncü kişiye verme yetkisi sağlar"],
        "Kanun m.112; ticari sır, bankacılık sırrı, müşteri sırrı ve Kurul denetim bilgilerini yetkisiz kişiye açıklamayı suç sayar; yarar sağlama amacı cezayı artırır.",
        "Bilginin görev nedeniyle edinilmesi ve kanunen yetkili olmayan mercie açıklanması esastır. Kişisel yarar amacı ayrıca nitelikli sonuç doğurur.",
        "6362 sayılı Sermaye Piyasası Kanunu m.112", "medium",
    ),
    r(
        "Savcılık, 6362 sayılı Kanunda düzenlenen bir sermaye piyasası suçu için Kurulun yazılı başvurusu olmadan kendiliğinden soruşturma başlatmıştır. Özel usule uygun mudur?",
        "6362 sayılı Kanundaki suçların soruşturulmasında Kurulun yazılı başvurusunun hukuki niteliği nedir?",
        "Hayır; Kurulun yazılı başvurusu soruşturma şartıdır",
        ["Evet; Kurulun sermaye piyasası suçlarında hiçbir rolü yoktur", "Hayır; yalnız borsa genel kurulunun oybirliği yeterlidir", "Evet; başvuru sadece özel hukuk tazminatı için gerekir", "Hayır; soruşturma yalnız yatırımcıların noter dilekçesiyle başlar"],
        "Kanun m.115/1, Kanunda yer alan suçlar için soruşturmayı Kurulun Cumhuriyet Başsavcılığına yazılı başvurusuna bağlar ve bu başvuruyu soruşturma şartı olarak niteler.",
        "Kurulun başvurusu yapılınca Kurul aynı zamanda katılan sıfatını kazanır; bu usul savcının ve mahkemenin ceza muhakemesi görevlerini ortadan kaldırmaz.",
        "6362 sayılı Sermaye Piyasası Kanunu m.115/1", "hard",
    ),
]


PREMISES = [
    {
        "stem": "Bilgi suistimali bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Bilginin henüz kamuya açıklanmamış olması gerekir\n\nII. Bilgi fiyatı, değeri veya yatırımcı kararını etkileyebilecek nitelikte olmalıdır\n\nIII. Bilginin kullanılmasıyla menfaat elde edilmesi aranır",
        "correct": "I, II ve III",
        "why": "Bilgi suistimali; kamuya açıklanmamış, fiyatı, değeri veya yatırımcı kararını etkileyebilecek bilginin kullanılması ve bu yolla menfaat sağlanması unsurlarını birlikte içerir.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.105/1", "difficulty": "easy",
    },
    {
        "stem": "Piyasa dolandırıcılığı bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yanıltıcı görünüm yaratan işlemler kapsama girebilir\n\nII. Yanlış bilginin internetten yayılması kapsama girebilir\n\nIII. Zorunlu bilginin açıklanmayıp bu sırada işlem yapılması kapsama girebilir",
        "correct": "I, II ve III",
        "why": "Güncel Kanun işlem bazlı, bilgi yaymaya dayalı ve zorunlu açıklamanın yapılmamasıyla bağlantılı işlem davranışlarını piyasa dolandırıcılığı kapsamında düzenler.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.106/1", "difficulty": "medium",
    },
    {
        "stem": "Piyasa bozucu eylemler bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Başka bir suça vücut vermemeleri gerekir\n\nII. Meşru gerekçeyle açıklanamayan belirli işlem örüntülerini kapsar\n\nIII. Yaptırımı yalnız hapis cezasıdır",
        "correct": "I ve II",
        "why": "Piyasa bozucu eylem suç oluşturmayan ve meşru gerekçeyle açıklanamayan belirli piyasa davranışlarını kapsar; idari yaptırıma tabi olduğundan III doğru değildir.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.103", "difficulty": "medium",
    },
    {
        "stem": "Bilgi suistimalinin faili bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yalnız ihraççı yönetim kurulu başkanı fail olabilir\n\nII. İşi veya mesleği nedeniyle bilgi edinen kişi fail olabilir\n\nIII. Bilginin niteliğini bilen ya da bilmesi gereken kişi fail olabilir",
        "correct": "II ve III",
        "why": "Fail çevresi yalnız yönetim kurulu başkanına özgülenmemiştir. İşi veya mesleği nedeniyle bilgi edinenler ile bilginin niteliğini bilen ya da bilmesi gereken kişiler kapsama girebilir; I yanlıştır.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.105/2", "difficulty": "medium",
    },
    {
        "stem": "Bilgi suistimali veya piyasa dolandırıcılığı sayılmayan haller bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yetkili resmî kurumun para politikası işlemi istisna olabilir\n\nII. Düzenlemeye aykırı her geri alım programı istisnadır\n\nIII. Kurul düzenlemelerine uygun fiyat istikrarı işlemi istisna olabilir",
        "correct": "I ve III",
        "why": "Yetkili resmî kurumun politika işlemleri ve düzenlemeye uygun fiyat istikrarı işlemleri istisna olabilir. Aykırı geri alım programı güvenli alandan yararlanamayacağı için II yanlıştır.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.107", "difficulty": "medium",
    },
    {
        "stem": "Sermaye piyasasında diğer suçlar bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Onaylı izahname olmadan halka arz suç oluşturabilir\n\nII. Müşteri varlığını kişisel menfaate kullanmak güveni kötüye kullanmadır\n\nIII. Elektronik kayıtları gizleme amacıyla bozmak yaptırım dışıdır",
        "correct": "I ve II",
        "why": "Onaylı izahname olmadan halka arz ve müşteri varlığını menfaate kullanma suç olabilir. Güveni kötüye kullanmayı gizlemek için elektronik kayıtları bozmak da açıkça kapsandığından III yanlıştır.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.108-109", "difficulty": "easy",
    },
    {
        "stem": "Şüpheli işlem bildirimi bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yatırım kuruluşu bilgi suistimali şüphesini gecikmeksizin Kurula bildirir\n\nII. Bildirim yapılan kişi hakkında işlem taraflarına serbestçe bilgi verilir\n\nIII. Bildirim yükümlülüğünün ihlali Kurul tedbirlerini doğurabilir",
        "correct": "I ve III",
        "why": "Şüphe gecikmeksizin Kurula bildirilir ve ihlal Kurul tedbirlerini doğurabilir. Bildirim ve bildirilen kişi hakkındaki bilgi mahkeme dışında üçüncü kişilere verilemeyeceğinden II yanlıştır.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.101", "difficulty": "hard",
    },
    {
        "stem": "Sermaye piyasası suçlarının soruşturulması bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kurulun yazılı başvurusu aranmadan özel usul tamamlanır\n\nII. Kurulun yazılı başvurusu soruşturma şartıdır\n\nIII. Başvuruyla Kurul katılan sıfatını kazanır",
        "correct": "II ve III",
        "why": "Kurulun Cumhuriyet Başsavcılığına yazılı başvurusu soruşturma şartıdır ve Kurul başvuruyla katılan sıfatını kazanır. Bu nedenle I yanlış, II ve III doğrudur.",
        "ref": "6362 sayılı Sermaye Piyasası Kanunu m.115/1", "difficulty": "hard",
    },
]


if __name__ == "__main__":
    write_topic(
        lesson_id="sermaye_piyasasi_ve_finans",
        topic_id="piyasa_suclari",
        label="Piyasa Suçları ve Bozucu Eylemler",
        slug="piyasa_suclari",
        prefix="topic-psb",
        seed=2026071740,
        legislation_version=(
            "6362 sayılı Sermaye Piyasası Kanunu m.100-115 güncel metin; "
            "bilgi suistimali m.105, piyasa dolandırıcılığı m.106, istisnalar "
            "m.107 ve piyasa bozucu eylemler m.103 (17.07.2026 kontrolü)"
        ),
        rules=RULES,
        premises=PREMISES,
        wrong_banks={},
    )
