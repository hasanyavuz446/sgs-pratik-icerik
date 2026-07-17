#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM Hukuk — Haksız Fiil konu havuzu (3×20).

Dayanak, 17.07.2026 tarihinde mevzuat.gov.tr'den alınan güncel 6098 sayılı
TBK m.49–76 metnidir. Paket kusur sorumluluğu, tazminat, hukuka uygunluk,
kusursuz sorumluluk, zamanaşımı ve yargılama hükümlerini kapsar.
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
        "A, kusurlu ve hukuka aykırı davranışıyla B'nin malvarlığında zarara yol açmıştır. Genel haksız fiil sorumluluğu bakımından A'nın yükümlülüğü nedir?",
        "TBK m.49'un ilk fıkrasındaki genel haksız fiil sorumluluğunun temel unsurları hangileridir?",
        "Kusurlu ve hukuka aykırı fiille verilen zarar giderilmelidir",
        ["Kusurlu fiil zarara yol açsa bile tazmin yükümlülüğü doğurmaz", "Zarar doğması tek başına her davranışı ceza sözleşmesine dönüştürür", "Hukuka aykırılık varsa zarar ve nedensellik hiçbir zaman aranmaz", "Yalnız sözleşme tarafları birbirine karşı haksız fiilden sorumlu olur"],
        "TBK m.49/1, kusurlu ve hukuka aykırı fiille başkasına zarar vereni bu zararı gidermekle yükümlü tutar.",
        "Genel kural; fiil, hukuka aykırılık, kusur, zarar ve uygun nedensellik bağı üzerine kurulur. Somut olayda bu unsurlar birlikte değerlendirilir.",
        "6098 sayılı TBK m.49/1", "easy",
    ),
    r(
        "A'nın davranışını açıkça yasaklayan özel bir hukuk kuralı yoktur; ancak A ahlaka aykırı davranışla B'ye kasten zarar vermiştir. Sorumluluk doğar mı?",
        "Zarar verici fiili yasaklayan özel kural bulunmasa bile ahlaka aykırı fiil ne zaman tazmin borcu doğurur?",
        "Ahlaka aykırı fiille başkasına kasten zarar verilirse sorumluluk doğar",
        ["Ahlaka aykırı davranış hiçbir koşulda özel hukuk sorumluluğu doğurmaz", "Özel yasak yoksa zarar verenin kastı dahi tamamen sonuçsuz kalır", "Sorumluluk için zarar görenin aynı fiile önceden kusuruyla katılması zorunludur", "Ahlaka aykırılık yalnız davranış bir sözleşmenin başlığında yazılıysa önem taşır"],
        "TBK m.49/2, yasaklayan hukuk kuralı bulunmasa bile ahlaka aykırı fiille kasten zarar vereni sorumlu tutar.",
        "Bu özel yol kastı arar. Salt ahlaka aykırılık veya salt zarar yeterli olmayıp zarar verme kastının da bulunması gerekir.",
        "6098 sayılı TBK m.49/2", "medium",
    ),
    r(
        "Zarar gören, haksız fiil davasında zararın varlığını ileri sürmüş fakat zarar verenin kusurunu ispatlamamıştır. Genel ispat yükü bakımından hangisi doğrudur?",
        "Genel haksız fiil sorumluluğunda zarar ve kusuru ispat yükü kural olarak kime aittir?",
        "Zarar gören hem zararını hem zarar verenin kusurunu ispatlamalıdır",
        ["Zarar veren her olayda zarar görenin bütün iddialarını kendiliğinden ispatlar", "Kusur hiçbir haksız fiil davasında ispat konusu yapılmaz", "İspat yükü yalnız fiille ilgisi olmayan üçüncü kişiye aittir", "Zarar gören yalnız sözleşme bulunduğunu ispat ederek tüm unsurları tamamlar"],
        "TBK m.50/1 genel kural olarak zararı ve zarar verenin kusurunu ispat yükünü zarar görene verir.",
        "Kusursuz sorumluluk hâllerinde kusur aranmayabilir. Ancak genel kusur sorumluluğunda davacı zarar ve kusur olgularını ortaya koyar.",
        "6098 sayılı TBK m.50/1", "easy",
    ),
    r(
        "Zararın doğduğu kesin olmakla birlikte miktarı tüm ayrıntılarıyla kanıtlanamamaktadır. Dosyada olayların olağan akışı ve alınan önlemler görülebilmektedir. Hâkim ne yapabilir?",
        "Uğranılan zararın miktarı tam olarak ispat edilemiyorsa hâkimin belirleme ölçütü nedir?",
        "Olağan akış ve alınan önlemler gözetilerek zarar hakkaniyetle belirlenir",
        ["Miktar tam ispatlanamazsa zarar gerçekleşmemiş kabul edilmek zorundadır", "Hâkim yalnız zarar verenin tek taraflı açıkladığı tutarı esas alabilir", "Zarar miktarı rastgele seçilir ve olayın akışı kesinlikle incelenemez", "Eksik ispat davacının bütün diğer haklarını kendiliğinden sona erdirir"],
        "TBK m.50/2, tam miktar ispatı mümkün değilse hâkime olağan akış ve zarar görenin önlemlerini gözeterek hakkaniyetle belirleme yetkisi verir.",
        "Zararın varlığı ile kesin miktarının kanıtlanması ayrılır. Hüküm, ispat güçlüğünün gerçek zararı tümüyle sonuçsuz bırakmasını önler.",
        "6098 sayılı TBK m.50/2", "medium",
    ),
    r(
        "Hâkim, tazminatın kapsamı ile toplu veya dönemsel ödeme biçimini belirleyecektir. Özellikle hangi hususu dikkate almalıdır?",
        "Tazminatın kapsamı ve ödenme biçimi belirlenirken TBK m.51 hangi temel ölçütleri öne çıkarır?",
        "Durumun gereği ve özellikle kusurun ağırlığı dikkate alınır",
        ["Yalnız zarar verenin kişisel tercihi bağlayıcı ölçüt sayılır", "Kusurun ağırlığının tazminatla hiçbir ilgisi bulunmaz", "Tazminat her olayda aynı tutar ve aynı ödeme biçiminde belirlenir", "Hâkim yalnız ceza davasındaki talep sonucuyla sınırlı değerlendirme yapar"],
        "TBK m.51, tazminatın kapsamı ve ödenme biçiminde durumun gereğini ve özellikle kusurun ağırlığını esas alır.",
        "İrat biçiminde tazminata hükmedilirse borçlu güvence göstermek zorundadır. Hâkim somut olayın özelliklerine göre ödeme şeklini de belirler.",
        "6098 sayılı TBK m.51", "medium",
    ),
    r(
        "Zarar gören, zararı doğuran fiile geçerli biçimde razı olmuş ve zararın artmasında da etkili davranmıştır. Bu durum tazminatı nasıl etkileyebilir?",
        "Zarar görenin rızası veya zararın doğması ya da artmasındaki etkisi hâkime hangi yetkiyi verir?",
        "Hâkim tazminatı indirebilir veya tamamen kaldırabilir",
        ["Rıza tazminatı her durumda otomatik olarak iki katına çıkarır", "Zarar görenin ortak etkisi tazminat hesabında asla değerlendirilemez", "Hâkim yalnız zarar verenin istemi olmadan hiçbir indirim yapamaz", "Zararın artmasına katkı bütün sorumluluğu ilgisiz üçüncü kişiye geçirir"],
        "TBK m.52/1, rıza, zararın doğmasına veya artmasına katkı ya da yükümlünün durumunu ağırlaştırma hâlinde indirim veya kaldırmaya izin verir.",
        "Müterafik davranış nedensel ve hakkaniyete dayalı bir indirim sebebidir. Sonuç otomatik değil, somut olayın ağırlığına göre hâkimin takdirindedir.",
        "6098 sayılı TBK m.52/1", "medium",
    ),
    r(
        "Zarara hafif kusuruyla sebep olan kişi tazminatı ödediğinde yoksulluğa düşecektir. Olayda hakkaniyet de indirimi gerektirmektedir. Hâkim ne yapabilir?",
        "Tazminat yükümlüsünün ödeme sonucunda yoksulluğa düşmesi hangi ek koşullarla indirim nedeni olabilir?",
        "Hafif kusur ve hakkaniyet koşulları da varsa tazminat indirilebilir",
        ["Yoksulluk iddiası ağır kastla verilen zararı da zorunlu olarak tamamen kaldırır", "Tazminat yükümlüsünün ekonomik durumu hiçbir olayda değerlendirilemez", "İndirim için zarar görenin kusurunun yüzde yüz olması tek koşuldur", "Hâkim yoksulluk hâlinde zararı devlet bütçesine borç olarak kaydeder"],
        "TBK m.52/2; hafif kusur, ödeme hâlinde yoksulluğa düşme ve hakkaniyetin gerektirmesi koşullarını birlikte arar.",
        "Hüküm olağanüstü bir hakkaniyet düzeltmesidir. Ağır kusurda veya hakkaniyet gerektirmiyorsa sırf ekonomik güçlük indirim sağlamaz.",
        "6098 sayılı TBK m.52/2", "hard",
    ),
    r(
        "Haksız fiil sonucu ölen kişinin düzenli destek sağladığı yakını bu desteği kaybetmiştir. Yakının talep edebileceği maddi zarar kalemi hangisidir?",
        "Ölüm hâlinde TBK m.53 kapsamında sayılan zarar kalemlerinden biri hangisidir?",
        "Destekten yoksun kalanların bu nedenle uğradığı kayıp",
        ["Ölenin hiç sahip olmadığı varsayımsal şirketin bütün gelecek kârları", "Zarar verenin aile üyelerinin ilgisiz kişisel harcamaları", "Ölümle bağlantısı bulunmayan önceki sözleşme borçlarının tamamı", "Yalnız ölümden yıllar sonra doğan ve nedensiz vergi giderleri"],
        "TBK m.53 ölüm hâlinde cenaze giderlerini, ölüm hemen değilse tedavi ve çalışma gücü kayıplarını, ayrıca destekten yoksun kalma zararını sayar.",
        "Destekten yoksun kalma, mirasçılıktan bağımsız biçimde fiilî ve düzenli desteğin kaybını karşılamayı amaçlar.",
        "6098 sayılı TBK m.53", "easy",
    ),
    r(
        "Haksız fiil nedeniyle kişinin çalışma gücü azalmış ve gelecekteki kazanç kapasitesi etkilenmiştir. Aşağıdakilerden hangisi bedensel zarar kalemidir?",
        "TBK m.54'e göre bedensel zarar kapsamında hangi ekonomik kayıplar istenebilir?",
        "Çalışma gücü kaybı ve ekonomik geleceğin sarsılmasından doğan kayıplar",
        ["Zarar verenin olayla ilgisiz bütün kişisel borçlarının zarar görene devri", "Yalnız zarar görenin daha önce bağışladığı malların varsayımsal değeri", "Bedensel zararla nedensellik bağı bulunmayan üçüncü kişi giderleri", "Tedaviyle ilgisiz ve zarar doğmadan önce yapılmış tatil harcamaları"],
        "TBK m.54 tedavi gideri, kazanç kaybı, çalışma gücü azalması veya yitirilmesi ve ekonomik geleceğin sarsılmasını bedensel zarar kalemleri arasında sayar.",
        "Bedensel zarar yalnız mevcut tedavi faturasından ibaret değildir; gelecekteki çalışma ve ekonomik kapasite kaybı da tazmin edilir.",
        "6098 sayılı TBK m.54", "medium",
    ),
    r(
        "Bedensel zarar hesabında zarar görene yapılmış, kısmen veya tamamen rücu edilemeyen sosyal güvenlik ödemesi bulunmaktadır. Bu ödeme tazminattan düşülebilir mi?",
        "Rücu edilemeyen sosyal güvenlik ödemeleri bedensel zarar ve destekten yoksun kalma hesabında nasıl ele alınır?",
        "Bu ödemeler zarar veya tazminattan indirilemez",
        ["Bu ödemeler her durumda indirilir", "Sosyal güvenlik ödemesi yalnız zarar verenin kusurunu artırmak için kullanılır", "Rücu edilemeyen ödeme zarar veren adına yeni bir alacak hakkı doğurur", "Ödemenin varlığı bedensel zararı sözleşmeden doğan ceza koşuluna çevirir"],
        "TBK m.55, rücu edilemeyen sosyal güvenlik ve ifa amacı taşımayan ödemelerin zarar veya tazminattan indirilemeyeceğini düzenler.",
        "Zarar hesabı sorumluluk hukuku ilkeleriyle yapılır. Hesaplanan tutar salt hakkaniyet düşüncesiyle miktar esas alınarak artırılamaz veya azaltılamaz.",
        "6098 sayılı TBK m.55", "hard",
    ),
    r(
        "Kişi ağır bedensel zarara uğramış, yakınları da olay nedeniyle ciddi manevi acı yaşamıştır. Yakınların manevi tazminat istemi bakımından hangisi doğrudur?",
        "Ağır bedensel zarar veya ölüm hâlinde manevi tazminat kimler lehine hükmedilebilir?",
        "Zarar görenin veya ölenin yakınlarına da uygun manevi tazminat verilebilir",
        ["Yakınlar hiçbir ağır bedensel zarar veya ölüm olayında manevi tazminat isteyemez", "Manevi tazminat yalnız zarar verenin şirket ortaklarına ödenebilir", "Yakınların talebi maddi zararın bulunmadığı her durumda kesin olarak yasaktır", "Manevi tazminat yalnız cenaze gideri belgesindeki tutarla sınırlı olabilir"],
        "TBK m.56, bedensel bütünlüğü zedelenene; ağır bedensel zarar veya ölüm hâlinde zarar görenin ya da ölenin yakınlarına uygun manevi tazminata izin verir.",
        "Yakınların talebi her bedensel zararda değil, ağır bedensel zarar veya ölüm hâlinde gündeme gelir. Miktar olayın özelliklerine göre belirlenir.",
        "6098 sayılı TBK m.56", "medium",
    ),
    r(
        "A'nın kişilik hakkı hukuka aykırı saldırıyla zedelenmiştir. A yalnız para değil, saldırıyı kınayan kararın yayımlanmasını da istemektedir. Hâkimin yetkisi nedir?",
        "Kişilik hakkının zedelenmesinde hâkim para dışında hangi giderim biçimine karar verebilir?",
        "Saldırıyı kınayan karar verip bunun yayımlanmasına hükmedebilir",
        ["Hâkim yalnız maddi eşyanın aynen teslimine karar verebilir", "Kişilik hakkı ihlalinde manevi giderim yolu hiçbir zaman kullanılamaz", "Kararın yayımlanması yalnız zarar veren isterse ve tazminat yerine geçmezse mümkündür", "Zedelenme bütün kişilik haklarını geçmişe etkili olarak sona erdirir"],
        "TBK m.58, manevi tazminat yerine veya ona ek başka giderim biçimleri; özellikle kınama kararı ve yayımlanmasını öngörür.",
        "Hâkim olayın niteliğine uygun giderimi seçebilir. Para tek araç değildir; ihlalin kamusal etkisini azaltacak kararın duyurulması da mümkündür.",
        "6098 sayılı TBK m.58", "medium",
    ),
    r(
        "Kişi ayırt etme gücünü geçici olarak kaybettiği sırada başkasına zarar vermiştir. Bu kayıpta kusuru bulunmadığını ispat edememiştir. Sorumluluğu nedir?",
        "Ayırt etme gücünü geçici kaybeden kişi verdiği zarardan hangi durumda kurtulabilir?",
        "Ayırt etme gücünü kaybetmede kusursuz olduğunu ispat ederse kurtulur",
        ["Geçici kayıp bütün zararları her durumda zarar görenin üzerinde bırakır", "Kişi yalnız zararın miktarını bilmediğini ileri sürerek sorumluluktan kurtulur", "Kusursuzluk ispatı geçici kayıp hâlinde hiçbir hukuki sonuç doğurmaz", "Ayırt etme gücü kaybı zararı otomatik olarak sözleşme borcuna dönüştürür"],
        "TBK m.59 geçici ayırt etme gücü kaybında sorumluluğu kural kabul eder; kişi kayıpta kusursuzluğunu ispat ederek kurtulabilir.",
        "Kural, kişinin kendi kusuruyla oluşturduğu geçici bilinç kaybının riskini zarar görene yüklememesini sağlar.",
        "6098 sayılı TBK m.59", "medium",
    ),
    r(
        "Aynı zarar hem sözleşmeye aykırılık hem haksız fiil hükümlerine dayandırılabilmektedir. Zarar gören özel bir tercih bildirmemiştir. Hâkim hangi esasa göre karar verir?",
        "Bir kişinin sorumluluğu birden çok sebebe dayanıyorsa ve zarar gören aksini istememişse hangi sebep uygulanır?",
        "Zarar görene en iyi giderim imkânı sağlayan sorumluluk sebebi uygulanır",
        ["Hâkim daima zarar gören için en az giderim sağlayan sebebi seçer", "Birden çok sebep bulunması bütün sorumluluk yollarını hükümsüz kılar", "Sadece kronolojik olarak en eski kanun hükmü uygulanabilir", "Zarar görenin tercihinin ve özel kanun hükmünün hiçbir önemi yoktur"],
        "TBK m.60, zarar gören aksini istemedikçe veya kanunda aksi olmadıkça en iyi giderimi sağlayan sorumluluk sebebini uygulatır.",
        "Sebeplerin yarışması zarar göreni koruyan bir seçim yaklaşımıdır. Zarar görenin iradesi ve özel kanuni düzenleme saklıdır.",
        "6098 sayılı TBK m.60", "hard",
    ),
    r(
        "Üç kişi birlikte hareket ederek tek bir zarara sebep olmuştur. Zarar görenin bu kişilere yönelteceği istemde dış ilişki bakımından hangi rejim uygulanır?",
        "Birden çok kişinin birlikte zarara sebep olması veya aynı zarardan çeşitli sebeplerle sorumlu olması hangi sorumluluğu doğurur?",
        "Zarar verenler hakkında müteselsil sorumluluk hükümleri uygulanır",
        ["Her zarar veren yalnız zarar görenin belirlemediği hayalî paydan sorumsuz olur", "Birlikte zarar verme bütün tazminat istemlerini kendiliğinden sona erdirir", "Sorumluluk yalnız faillerden yaşça en büyük olan kişiye yüklenebilir", "Zarar gören tüm sorumlulara karşı aynı anda hiçbir istem ileri süremez"],
        "TBK m.61, birlikte zarar veren veya aynı zarardan farklı sebeplerle sorumlu olanlar hakkında müteselsil sorumluluk hükümlerini uygular.",
        "Dış ilişkide zarar gören alacağın tamamını sorumlulardan birinden isteyebilir. İç paylaşım daha sonra m.62 ölçütleriyle yapılır.",
        "6098 sayılı TBK m.61", "easy",
    ),
    r(
        "Müteselsil sorumlulardan biri kendi iç payından fazla tazminat ödemiştir. Diğer sorumlulara dönmek istemektedir. Hangi hakka sahiptir?",
        "Aynı zarardan sorumlu kişiler arasındaki iç paylaşımda hangi ölçütler ve sonuç uygulanır?",
        "Fazla ödeyen diğer sorumlulara rücu eder ve zarar görenin haklarına halef olur",
        ["Fazla ödeme yapan kişi hiçbir koşulda diğer sorumlulara başvuramaz", "İç paylaşım yalnız sorumluların yaşlarına göre eşit olmayan kura ile yapılır", "Kusur ağırlığı ve yaratılan tehlike iç ilişkide kesinlikle dikkate alınmaz", "Fazla ödeme zarar görenin aynı tutarı yeniden istemesini zorunlu kılar"],
        "TBK m.62, iç paylaşımda bütün koşulları, kusur ağırlığını ve tehlike yoğunluğunu gözetir; fazla ödeyene rücu ve halefiyet verir.",
        "Müteselsil sorumluluk zarar göreni korur, nihai yükü rastgele dağıtmaz. İç ilişkide her sorumlunun katkısı ve tehlikesi değerlendirilir.",
        "6098 sayılı TBK m.62", "hard",
    ),
    r(
        "Kamu görevlisi kanunun verdiği yetkiyi sınırları içinde kullanmış ve bu sırada zarar doğmuştur. Fiilin hukuka aykırılığı bakımından hangisi doğrudur?",
        "Kanunun verdiği yetkiye dayanan fiilin hukuka uygun sayılması için hangi koşul aranır?",
        "Fiil kanuni yetkinin sınırları içinde kalmalıdır",
        ["Yetki aşımı da hukuka uygundur", "Yetkiye dayanan fiil zarar doğurursa mutlaka haksız fiile dönüşür", "Hukuka uygunluk yalnız zarar verenin içinden izin verdiğini düşünmesine bağlıdır", "Kanuni yetki sadece taraflar arasında sözleşme varsa kullanılabilir"],
        "TBK m.63, kanunun verdiği yetkiye dayanan ve yetkinin sınırları içinde kalan fiili, zarar doğsa bile hukuka aykırı saymaz.",
        "Yetkinin varlığı kadar sınırlarına uyulması da gerekir. Rıza, üstün yarar, haklı savunma ve zorunluluk da diğer hukuka uygunluk nedenleridir.",
        "6098 sayılı TBK m.63", "easy",
    ),
    r(
        "A, kendisine yönelen devam eden saldırıyı orantılı biçimde savuştururken saldıranın malına zarar vermiştir. Haklı savunma koşulları oluşmuştur. A sorumlu mudur?",
        "Haklı savunmada saldıranın şahsına veya mallarına verilen zarar bakımından temel kural nedir?",
        "Haklı savunmada bulunan bu zarardan sorumlu tutulamaz",
        ["Haklı savunma saldıranın bütün zararlarını iki kat tazmin yükümlülüğü doğurur", "Savunma koşulları oluşsa bile fiil daima kesin hukuka aykırıdır", "Zarar yalnız saldırıyla ilgisiz üçüncü kişi onaylarsa hukuka uygun olur", "Haklı savunma sadece sözleşmeden doğan para borçlarında kullanılabilir"],
        "TBK m.64/1, haklı savunmada bulunanı saldıranın şahsına veya mallarına verdiği zarardan sorumlu tutmaz.",
        "Zorunluluk hâlinde başkasının malına verilen zararda ise sonuç farklıdır; giderim yükünü hâkim hakkaniyete göre belirler.",
        "6098 sayılı TBK m.64", "medium",
    ),
    r(
        "Ayırt etme gücü bulunmayan kişi başkasına zarar vermiş; olayın ekonomik ve sosyal koşulları zararın kısmen giderilmesini hakkaniyet gereği göstermektedir. Hâkim ne yapabilir?",
        "Ayırt etme gücü bulunmayan kişinin verdiği zarar için hakkaniyet sorumluluğu nasıl uygulanır?",
        "Hâkim zararın tamamen veya kısmen giderilmesine karar verebilir",
        ["Ayırt etme gücü yoksa hâkim hiçbir koşulda giderime karar veremez", "Zarar gören ayırt etme gücü olmayan kişiye her durumda tazminat öder", "Hakkaniyet sorumluluğu yalnız taraflar önceden yazılı sözleşme yapmışsa doğar", "Hâkim zararı olayla ilgisiz üçüncü kişilere eşit olarak dağıtmak zorundadır"],
        "TBK m.65, hakkaniyet gerektiriyorsa ayırt etme gücü bulunmayanın zararının tamamen veya kısmen giderilmesine izin verir.",
        "Bu kusur sorumluluğu değildir. Tarafların ekonomik durumları ve olayın özellikleri hakkaniyet temelinde değerlendirilir.",
        "6098 sayılı TBK m.65", "medium",
    ),
    r(
        "Çalışan, kendisine verilen işi yaparken üçüncü kişiye zarar vermiştir. Adam çalıştıran seçim, talimat ve gözetimde gerekli özeni gösterdiğini ispatlayamamıştır. Sonuç nedir?",
        "Adam çalıştıranın çalışanın iş sırasında verdiği zarardan kurtuluş kanıtı hangi özen alanlarını kapsar?",
        "Seçim, talimat, gözetim ve denetimde gerekli özenin gösterildiği ispatlanmalıdır",
        ["Adam çalıştıran yalnız çalışanın işe geç geldiğini ispatlayarak her zarardan kurtulur", "Çalışanın işi yaparken verdiği zarar hiçbir zaman adam çalıştırana yüklenemez", "Kurtuluş kanıtı zarar görenin başka işte çalıştığını göstermeye bağlıdır", "İşletme düzeninin zararı önlemeye elverişsiz olması sorumluluğu kesin kaldırır"],
        "TBK m.66, çalışan iş sırasında zarar verirse adam çalıştıranı sorumlu tutar; seçim, talimat, gözetim ve denetim özenini ispat kurtuluş sağlayabilir.",
        "İşletmeler için ayrıca çalışma düzeninin zararı önlemeye elverişli olduğu ispatlanmalıdır. Rücu, çalışanın bizzat sorumlu olduğu ölçüdedir.",
        "6098 sayılı TBK m.66", "hard",
    ),
    r(
        "Bir hayvanın bakımını geçici olarak üstlenen kişi, hayvanın üçüncü kişiye verdiği zarar bakımından gerekli tüm özeni gösterdiğini ispatlamıştır. Sorumluluğu nedir?",
        "Hayvan bulunduranın sorumluluktan kurtulabilmesi için hangi olguyu ispat etmesi gerekir?",
        "Zararın doğmasını engellemek için gerekli özeni gösterdiğini ispatlamalıdır",
        ["Hayvanın kendisine ait olmadığını söylemesi her durumda tek başına yeterlidir", "Hayvan bulunduran hiçbir özen kanıtıyla sorumluluktan kurtulamaz", "Sorumluluk yalnız hayvanın ekonomik değeri zarar tutarından yüksekse doğar", "Geçici bakım üstlenen kişi kanunen hayvan bulunduran kabul edilemez"],
        "TBK m.67, sürekli veya geçici bakım ve yönetimi üstleneni sorumlu tutar; gerekli özeni ispat eden hayvan bulunduran kurtulur.",
        "Mülkiyet şart değildir; bakım ve yönetim ilişkisi yeterlidir. Hayvan başkası tarafından ürkütülmüşse rücu hakkı saklıdır.",
        "6098 sayılı TBK m.67", "medium",
    ),
    r(
        "Bir binanın bakım eksikliği nedeniyle yoldan geçen kişi zarar görmüştür. Binanın maliki kusursuz olduğunu ileri sürmektedir. Yapı malikinin sorumluluğu nedir?",
        "Bina veya diğer yapı eserinin yapım bozukluğu ya da bakım eksikliğinden doğan zarardan kim sorumludur?",
        "Yapı maliki zararı gidermekle yükümlüdür",
        ["Malik yapım bozukluğundan sorumsuzdur", "Zarar yalnız yoldan geçen kişinin ailesine yüklenir", "Bakım eksikliği sadece binanın kiracısını kusursuz sorumlu yapar", "Malik ancak zarar görenle satış sözleşmesi varsa sorumlu olur"],
        "TBK m.69, yapım bozukluğu veya bakım eksikliğinden doğan zararı yapı malikine yükler. İntifa ve oturma hakkı sahipleri bakım eksikliğinde birlikte sorumlu olabilir.",
        "Yapı malikinin sorumluluğu kusursuz sorumluluktur. Sorumluların, kendilerine karşı sorumlu olan kişilere rücu hakkı saklıdır.",
        "6098 sayılı TBK m.69", "easy",
    ),
    r(
        "Önemli ölçüde tehlike arz eden işletmenin tipik faaliyeti zarara yol açmıştır. İşletme sahibi, tüm özenin gösterildiğini savunmaktadır. Temel sorumluluk kime aittir?",
        "Önemli ölçüde tehlike arz eden işletmenin faaliyetinden doğan zararda kimler müteselsilen sorumludur?",
        "İşletme sahibi ve varsa işleten müteselsilen sorumludur",
        ["İşleten hiçbir zaman sorumlu olmaz", "Tüm özen gösterilmesi tehlike sorumluluğunu her durumda kesin kaldırır", "Tehlikeli faaliyete izin verilmesi zarar görenin denkleştirme hakkını yok eder", "İşletmenin önemli tehlike taşıması hiçbir özel sorumluluk sonucu doğurmaz"],
        "TBK m.71, önemli ölçüde tehlike arz eden işletmenin faaliyet zararından işletme sahibi ile varsa işleteni müteselsilen sorumlu tutar.",
        "Tehlike sorumluluğu olağan özenle dahi sık veya ağır zarar üretme kapasitesine dayanır. Faaliyete izin verilmiş olması uygun denkleştirme istemini engellemez.",
        "6098 sayılı TBK m.71", "hard",
    ),
    r(
        "Zarar gören, zararı ve tazminat yükümlüsünü 1 Mart 2026'da öğrenmiştir; fiil daha önce gerçekleşmiştir ve daha uzun ceza zamanaşımı yoktur. Nispi süre ne kadardır?",
        "Haksız fiil tazminatında zarar ve yükümlünün öğrenilmesinden başlayan genel zamanaşımı süresi kaç yıldır?",
        "Öğrenmeden başlayarak iki yıl; fiilden başlayarak her hâlde on yıldır",
        ["Öğrenmeden başlayan süre yalnız bir ay, mutlak süre ise altı aydır", "Tazminat istemi hiçbir süreye bağlı olmadan sonsuza kadar kullanılabilir", "Her iki süre de yalnız zarar verenin yazılı kabulünden sonra işlemeye başlar", "Zamanaşımı daima sözleşme kurulmasından önce ve geriye doğru hesaplanır"],
        "TBK m.72, öğrenmeden itibaren iki yıllık nispi ve fiilden itibaren on yıllık mutlak süre öngörür; daha uzun ceza zamanaşımı saklıdır.",
        "Öğrenme hem zararı hem tazminat yükümlüsünü kapsar. Fiil aynı zamanda daha uzun süreli cezayı gerektiriyorsa ceza zamanaşımı uygulanabilir.",
        "6098 sayılı TBK m.72", "medium",
    ),
    r(
        "Haksız fiil aynı zamanda ceza yargılamasına konu olmuş ve sanık beraat etmiştir. Hukuk hâkimi kusuru değerlendirirken beraat kararıyla bağlı mıdır?",
        "Hukuk hâkiminin kusur ve ayırt etme gücü değerlendirmesinde ceza hukuku kararıyla ilişkisi nasıldır?",
        "Hukuk hâkimi beraat kararıyla ve ceza hâkiminin kusur değerlendirmesiyle bağlı değildir",
        ["Beraat kararı hukuk davasını her durumda ve bütün yönleriyle kesin olarak bitirir", "Hukuk hâkimi yalnız ceza hâkiminin tazminat hesabını aynen kopyalayabilir", "Ceza hukuku hükümleri özel hukuk kusurunu hiçbir inceleme olmadan belirler", "Hukuk hâkimi ayırt etme gücü konusunda delil değerlendirmesi yapamaz"],
        "TBK m.74 hukuk hâkimini ceza hukukunun sorumluluk hükümleri, beraat kararı, kusur ve zarar değerlendirmesiyle bağlı tutmaz.",
        "Ceza ve özel hukuk sorumluluğunun amaçları ve ispat ölçüleri farklıdır. Hukuk hâkimi kendi dosyasındaki delillerle bağımsız değerlendirme yapar.",
        "6098 sayılı TBK m.74", "hard",
    ),
    r(
        "Zarar gören inandırıcı kanıtlarla iddiasının haklılığını göstermiş ve ekonomik durumu acil desteği gerektirmektedir. Dava sürerken hâkim neye karar verebilir?",
        "Haksız fiil davasında geçici ödeme kararı verilebilmesi için hangi koşullar birlikte aranır?",
        "İnandırıcı kanıt ve ekonomik gereklilik varsa istem üzerine geçici ödeme verilebilir",
        ["Geçici ödeme yalnız kesin hükümden on yıl sonra kendiliğinden yapılabilir", "İddianın haklılığına ilişkin hiçbir kanıt bulunmasa da ödeme zorunludur", "Ekonomik durum geçici ödeme değerlendirmesinde kesinlikle dikkate alınamaz", "Geçici ödeme hiçbir zaman nihai tazminata mahsup edilemez"],
        "TBK m.76, inandırıcı kanıt ve ekonomik gereklilik varsa istem üzerine davalının geçici ödeme yapmasına karar verilebileceğini düzenler.",
        "Geçici ödeme nihai tazminata mahsup edilir. Tazminata hükmedilmezse alınan tutar yasal faiziyle geri verilir.",
        "6098 sayılı TBK m.76", "medium",
    ),
]


PREMISES = [
    {
        "stem": "Genel haksız fiil sorumluluğuyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kusurlu ve hukuka aykırı fiille verilen zarar giderilmelidir.\n\nII. Zarar gören kural olarak zararını ve zarar verenin kusurunu ispatlar.\n\nIII. Tam miktar ispatlanamıyorsa hâkim zararı hakkaniyetle belirleyebilir.",
        "correct": "I, II ve III", "why": "TBK m.49 ve 50 uyarınca üç ifade de doğrudur.",
        "ref": "6098 sayılı TBK m.49-50", "difficulty": "medium",
    },
    {
        "stem": "Ölüm ve bedensel zararla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Cenaze giderleri ölüm zararları arasındadır.\n\nII. Kazanç kaybı bedensel zarar kalemi olabilir.\n\nIII. Ağır bedensel zararda yakınlara manevi tazminat verilebilir.",
        "correct": "I, II ve III", "why": "TBK m.53, 54 ve 56 uyarınca üç ifade de doğrudur.",
        "ref": "6098 sayılı TBK m.53-56", "difficulty": "medium",
    },
    {
        "stem": "Tazminatın belirlenmesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kusurun ağırlığı tazminatın kapsamı belirlenirken gözetilir.\n\nII. Zarar görenin zararın artmasına etkisi indirim nedeni olabilir.\n\nIII. Zarar görenin rızası tazminatı her durumda iki katına çıkarır.",
        "correct": "I ve II", "why": "TBK m.51 ve 52 nedeniyle I ve II doğrudur. Rıza indirim veya kaldırma nedeni olabildiğinden III yanlıştır.",
        "ref": "6098 sayılı TBK m.51-52", "difficulty": "medium",
    },
    {
        "stem": "Hukuka uygunluk nedenleriyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kanuni yetki sınırları içinde kullanılan fiil hukuka aykırı sayılmaz.\n\nII. Haklı savunmada bulunan, saldırana verdiği zarardan her durumda sorumlu tutulur.\n\nIII. Zorunluluk hâlinde başkasının malına verilen zararda hâkim hakkaniyeti gözetebilir.",
        "correct": "I ve III", "why": "TBK m.63 nedeniyle I, m.64 nedeniyle III doğrudur. Haklı savunmada saldırana verilen zarardan sorumluluk doğmadığı için II yanlıştır.",
        "ref": "6098 sayılı TBK m.63-64", "difficulty": "medium",
    },
    {
        "stem": "Kusursuz sorumlulukla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Adam çalıştıran özen kanıtıyla sorumluluktan kurtulabilir.\n\nII. Hayvan bulunduran gerekli özeni ispat ederse kurtulabilir.\n\nIII. Yapı malikinin sorumluluğu yalnız zarar görenle sözleşme varsa doğar.",
        "correct": "I ve II", "why": "TBK m.66 ve 67 nedeniyle I ve II doğrudur. Yapı maliki sorumluluğu sözleşmeye bağlı olmadığından III yanlıştır.",
        "ref": "6098 sayılı TBK m.66-69", "difficulty": "hard",
    },
    {
        "stem": "Müteselsil sorumlulukla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Birlikte zarar verenlere müteselsil sorumluluk uygulanabilir.\n\nII. İç paylaşımda kusur ağırlığı dikkate alınmaz.\n\nIII. Payından fazla ödeyen diğer sorumlulara rücu edebilir.",
        "correct": "I ve III", "why": "TBK m.61 nedeniyle I, m.62 nedeniyle III doğrudur. İç paylaşımda kusur ağırlığı gözetildiği için II yanlıştır.",
        "ref": "6098 sayılı TBK m.61-62", "difficulty": "hard",
    },
    {
        "stem": "Haksız fiil zamanaşımıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Öğrenmeden başlayan genel süre iki yıldır.\n\nII. Fiilden başlayan genel mutlak süre on yıldır.\n\nIII. Daha uzun ceza zamanaşımı hiçbir durumda uygulanmaz.",
        "correct": "I ve II", "why": "TBK m.72 nedeniyle I ve II doğrudur. Daha uzun ceza zamanaşımı uygulanabildiğinden III yanlıştır.",
        "ref": "6098 sayılı TBK m.72", "difficulty": "medium",
    },
    {
        "stem": "Yargılamayla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Hukuk hâkimi beraat kararıyla bağlı değildir.\n\nII. Geçici ödeme nihai tazminata mahsup edilir.\n\nIII. Tazminata hükmedilmezse geçici ödeme hiçbir zaman geri verilmez.",
        "correct": "I ve II", "why": "TBK m.74 nedeniyle I, m.76 nedeniyle II doğrudur. Tazminat verilmezse geçici ödeme yasal faiziyle geri verilir; III yanlıştır.",
        "ref": "6098 sayılı TBK m.74 ve 76", "difficulty": "hard",
    },
]


WRONG_BANKS = {"unused": ["a", "b", "c", "d", "e", "f"]}


if __name__ == "__main__":
    write_topic(
        lesson_id="borclar_hukuku", topic_id="haksiz_fiil",
        label="Haksız Fiil", slug="haksiz_fiil",
        prefix="kh-haksiz", seed=20260727,
        legislation_version="6098 sayılı TBK m.49–76 — 17.07.2026 güncel metin",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG_BANKS,
    )
