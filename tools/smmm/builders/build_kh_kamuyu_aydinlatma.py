#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM Sermaye Piyasası Mevzuatı — Kamuyu Aydınlatma, 3×20.

Dayanaklar, 17.07.2026 tarihinde SPK'nın güncel mevzuat sistemindeki II-15.1
sayılı konsolide Tebliğ, güncel Özel Durumlar Rehberi, Kurulun borsa
şirketlerinin yükümlülüklerine ilişkin açıklamaları ve 6362 sayılı Kanun
üzerinden doğrulanmıştır.
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
        "Bir ihraççı, yatırım kararını etkileyebilecek önemli bir gelişmeyi yalnız şirket içindeki yöneticilere bildirmiştir. Kamuyu aydınlatmanın amacı bakımından bu tutum yeterli midir?",
        "II-15.1 sayılı Tebliğin kamuyu aydınlatmada gözettiği temel amaç hangisidir?",
        "Hayır; yatırımcıların zamanında, tam ve doğru bilgilenmesi gerekir",
        ["Evet; bilgi yöneticilere ulaştığında piyasa da bilgilenmiş sayılır", "Evet; önemli gelişmeler yalnız şirket çalışanları arasında tutulmalıdır", "Hayır; fakat açıklamanın amacı yalnız vergi denetimini kolaylaştırmaktır", "Evet; kamuyu aydınlatma sadece işlem hacmini artırmayı amaçlar"],
        "II-15.1 sayılı Tebliğ m.1, sermaye piyasası araçlarının değerini, fiyatını veya yatırım kararlarını etkileyebilecek gelişmelerin yatırımcıları zamanında, tam ve doğru bilgilendirecek biçimde açıklanmasını amaçlar.",
        "Kamuyu aydınlatma; güvenilir, şeffaf, etkin, istikrarlı, adil ve rekabetçi bir piyasanın işleyişine hizmet eder.",
        "Özel Durumlar Tebliği (II-15.1) m.1", "easy",
    ),
    r(
        "Şirket, mevzuat gereği kamuya açıklaması gereken bilgiyi elektronik imzayla iletip herkesin erişimine açacaktır. Kullanılması gereken sistem hangisidir?",
        "Kamuyu Aydınlatma Platformunun mevzuattaki işlevi nasıl tanımlanır?",
        "Elektronik imzalı bilginin iletilip duyurulduğu KAP kullanılır",
        ["Borsadaki alım satım emirlerinin eşleştiği pazar kullanılır", "Yalnız şirket yöneticilerinin eriştiği kapalı arşiv kullanılır", "Vergi beyannamelerinin gönderildiği maliye sistemi kullanılır", "Sadece fiziki ilanların saklandığı ticaret sicili kullanılır"],
        "II-15.1 sayılı Tebliğ m.4, KAP'ı mevzuat uyarınca açıklanması gereken bilgilerin elektronik imzalı olarak iletildiği ve kamuya duyurulduğu elektronik sistem olarak tanımlar.",
        "KAP bir işlem eşleştirme pazarı değil, kamuyu aydınlatma bildirimlerinin elektronik ortamıdır.",
        "Özel Durumlar Tebliği (II-15.1) m.4/1-ı; 6362 sayılı Kanun m.15", "easy",
    ),
    r(
        "Şirketin büyük bir müşterisiyle sözleşmesini kaybettiği bilgisi henüz açıklanmamış ve makul yatırımcının kararını etkileyebilecek niteliktedir. Bu bilgi nasıl sınıflandırılır?",
        "İçsel bilginin ayırt edici iki özelliği hangileridir?",
        "Henüz kamuya açıklanmamış ve yatırım kararını etkileyebilir olmasıdır",
        ["Daha önce yayımlanmış ve yalnız geçmiş fiyatı göstermesidir", "Her durumda söylentiye dayanması ve doğrulanamamasıdır", "Şirketle ilgisiz olup yatırımcı kararını etkilememesidir", "Yalnız vergi dairesine verilmiş rutin bir form olmasıdır"],
        "İçsel bilgi, sermaye piyasası aracının değerini, fiyatını veya yatırım kararlarını etkileyebilecek henüz kamuya açıklanmamış bilgi, olay ve gelişmedir.",
        "Bilginin hem kamuya açıklanmamış olması hem de değer, fiyat veya yatırım kararları üzerinde etkili olabilmesi içsel bilgi niteliğini belirler.",
        "Özel Durumlar Tebliği (II-15.1) m.4/1-e", "easy",
    ),
    r(
        "İhraççının KAP'taki genel bilgilerinde adres değişikliği olmuştur; bu veri içsel bilgi tanımına girmese de Tebliğ uyarınca açıklanmalıdır. Bilginin türü nedir?",
        "Sürekli bilgi ile özel durum kavramları arasındaki ilişki nasıldır?",
        "Sürekli bilgidir; özel durum içsel veya sürekli bilgiyi kapsar",
        ["İçsel bilgidir; sürekli bilgi diye ayrı bir kategori bulunmaz", "Yalnız ticari sırdır; hiçbir özel durum kapsamına girmez", "İzahname özetidir; yalnız halka arz sırasında açıklanabilir", "Finansal tahmindir; açıklanması her durumda yasaktır"],
        "II-15.1 sayılı Tebliğ m.4'e göre sürekli bilgi, içsel bilgi tanımı dışında kalan bilgi, olay ve gelişmelerdir; özel durum ise içsel veya sürekli bilgiyi kapsar.",
        "Özel durum üst kavramdır. İçsel bilgi niteliği taşımayan fakat Tebliğce açıklanması gereken bilgiler sürekli bilgi olarak değerlendirilir.",
        "Özel Durumlar Tebliği (II-15.1) m.4/1-n ve p", "medium",
    ),
    r(
        "Yönetim kurulu, daha önce açıklanan önemli bir yatırımın iptal edildiğini öğrenmiş fakat ilk açıklamanın yapılmış olmasını yeterli görmüştür. Yeniden açıklama gerekir mi?",
        "İçsel bilgi ve daha önce açıklanan husustaki değişiklik ne zaman duyurulur?",
        "Evet; değişiklik ortaya çıktığında veya öğrenildiğinde açıklanır",
        ["Hayır; bir konu hakkında yalnız bir kez açıklama yapılabilir", "Evet; fakat yalnız hesap dönemi sonunda açıklanabilir", "Hayır; değişiklikler hiçbir zaman içsel bilgi oluşturamaz", "Evet; yalnız bütün yatırımcılar yazılı talepte bulunursa açıklanır"],
        "II-15.1 sayılı Tebliğ m.5/1, içsel bilgilerin ve daha önce açıklanan bu bilgilere ilişkin değişikliklerin ortaya çıktığında veya öğrenildiğinde ihraççı tarafından açıklanmasını öngörür.",
        "İlk açıklama sonraki önemli değişiklikleri duyurma yükümlülüğünü kaldırmaz; öğrenme veya ortaya çıkma anı esas alınır.",
        "Özel Durumlar Tebliği (II-15.1) m.5/1", "easy",
    ),
    r(
        "17.07.2026 tarihinde ihraççının bilgisi dışında önemli içsel bilgiyi öğrenen kişi, toplam oy haklarının %12'sine sahiptir. Açıklama sorumluluğu kime aittir?",
        "17.07.2026 itibarıyla ihraççı dışındaki pay sahibinin içsel bilgi açıklama yükümlülüğü hangi eşikte doğabilir?",
        "Bilgiyi öğrenen %10 veya üzeri pay sahibi açıklama yapar",
        ["Yalnız ihraççı açıklar; pay sahibinin yükümlülüğü hiç doğmaz", "Pay sahibi ancak sermayenin tamamına sahipse açıklama yapar", "Her yatırımcı bir pay edindiği anda bütün bilgileri açıklar", "Pay sahibi bilgiyi öğrense de yalnız borsanın izniyle açıklayabilir"],
        "İhraççının bilgisi dışında içsel bilgiyi öğrenen ve doğrudan ya da dolaylı toplam oy haklarında veya sermayede %10 ya da daha fazla paya sahip kişi açıklama yapmakla yükümlüdür.",
        "%10 eşiği yanında, bu orana bağlı olmaksızın yönetim kurulu üyesi seçme veya aday gösterme imtiyazlı paylarının %10'una sahip kişi de kapsamda olabilir.",
        "Özel Durumlar Tebliği (II-15.1) m.5/2", "medium",
    ),
    r(
        "İhraççı adına görev yapan danışman, görevin olağan ifası sırasında içsel bilgiyi gizlilik yükümlülüğü bulunmayan üçüncü kişiye aktarmıştır. İhraççı ne yapmalıdır?",
        "İçsel bilginin görevin olağan ifasında üçüncü kişiye açıklanması hangi sonucu doğurur?",
        "İhraççı bilgiyi kamuya açıklar; gizlilik yükümlülüğü istisnadır",
        ["Bilgi üçüncü kişiye geçtiği için açıklama yükümlülüğü sona erer", "Danışmanın açıklaması kendiliğinden KAP açıklaması sayılır", "İhraççı bilgiyi yalnız çalışanlarına tekrar göndermekle yetinir", "Üçüncü kişiye açıklanan bilgi hiçbir koşulda kamuya duyurulamaz"],
        "II-15.1 sayılı Tebliğ m.5/3-4, olağan görev ifasında üçüncü kişiye aktarılan içsel bilginin ihraççı tarafından açıklanmasını; yasal, esas sözleşmesel veya sözleşmesel gizlilik yükümlülüğünü ise istisna olarak düzenler.",
        "Bilginin görevin olağan akışında paylaşılması kamuyu aydınlatma borcunu kaldırmaz; alıcının bağlayıcı gizlilik yükümlülüğü olup olmadığı önem taşır.",
        "Özel Durumlar Tebliği (II-15.1) m.5/3-4", "hard",
    ),
    r(
        "Şirket birleşme görüşmelerini hemen açıklamanın meşru çıkarına zarar vereceğini düşünmektedir. Gizliliği sağlayabiliyor ve erteleme yatırımcıyı yanıltmıyorsa açıklamayı erteleyebilir mi?",
        "İçsel bilginin açıklanmasının ertelenmesi için birlikte aranacak koşullar hangileridir?",
        "Evet; meşru çıkar, yanıltmama ve gizlilik koşullarıyla erteleyebilir",
        ["Hayır; içsel bilgi hiçbir koşul altında ertelenemez", "Evet; yalnız fiyat yükselirse ve gizlilik sağlanmazsa erteleyebilir", "Evet; yatırımcıları yanıltacak olsa bile süresiz erteleyebilir", "Hayır; erteleme yalnız yatırımcıların oybirliğiyle kararlaştırılabilir"],
        "II-15.1 sayılı Tebliğ m.6/1, sorumluluk ihraççıya ait olmak üzere meşru çıkarın korunması, yatırımcının yanıltılmaması ve gizliliğin sağlanabilmesi koşullarını birlikte arar.",
        "Erteleme serbest bir susma hakkı değildir; üç koşulun birlikte bulunması ve sorumluluğun ihraççıda kalması gerekir.",
        "Özel Durumlar Tebliği (II-15.1) m.6/1", "medium",
    ),
    r(
        "Açıklaması ertelenen içsel bilginin gizliliği korunmuş, ancak erteleme sebepleri bugün ortadan kalkmıştır. İhraççının izleyeceği yol hangisidir?",
        "Erteleme sebepleri sona erdiğinde yapılacak açıklamada hangi bilgiye de yer verilir?",
        "Bilgiyi açıklar; erteleme kararını ve temel sebeplerini belirtir",
        ["Bilgiyi süresiz saklar ve erteleme kararını hiç açıklamaz", "Yalnız borsaya sözlü bilgi verir, kamuya açıklama yapmaz", "İçsel bilgiyi siler ve açıklama sorumluluğunu yatırımcıya bırakır", "Sadece yönetim kurulu tutanağını şirket içinde arşivler"],
        "Erteleme sebepleri ortadan kalkınca içsel bilgi kamuya açıklanır; açıklamada erteleme kararı ve bu kararın temelindeki sebepler de belirtilir.",
        "Erteleme geçici bir uygulamadır. Sebepler sona erince açıklama yapılır; ertelenen olay hiç gerçekleşmemişse açıklama yapılmayabilir.",
        "Özel Durumlar Tebliği (II-15.1) m.6/2", "medium",
    ),
    r(
        "Erteleme kararı alan şirket, bilgiye herkesin erişebildiği ortak klasörde tutmaya devam etmiş ve hiçbir yazılı karar oluşturmamıştır. Uygulama uygun mudur?",
        "Erteleme sürecinde gizlilik tedbirleri ve kararın belgelendirilmesi nasıl yürütülür?",
        "Hayır; erişim kontrol edilir ve gerekçeler yazılı karara bağlanır",
        ["Evet; erteleme kararı hiçbir güvenlik tedbiri gerektirmez", "Evet; sözlü karar ve herkese açık klasör yeterli kabul edilir", "Hayır; fakat yalnız yatırımcının bilgisayarı erişime kapatılır", "Evet; gizlilik yalnız bilgi KAP'ta açıklandıktan sonra başlar"],
        "İhraççı ertelenen bilgiye erişimi kontrol etmeli, yetkisiz erişimi önlemeli ve gizlilik bozulursa açıklama yapmalıdır. Erteleme gerekçeleri ile tedbirler yönetim kurulu kararına veya yetkilinin yazılı onayına bağlanır.",
        "Gizlilik hem teknik ve idari tedbirlerle korunur hem de ertelemenin meşru çıkar, yanıltmama ve gizlilik yönleri yazılı biçimde belgelenir.",
        "Özel Durumlar Tebliği (II-15.1) m.6/3-4", "hard",
    ),
    r(
        "Şirkette içsel bilgilere düzenli erişen yeni finans direktörü göreve başlamıştır. İhraççı bu değişikliği hangi kuruma ve hangi sürede bildirmelidir?",
        "İçsel bilgilere erişimi olan kişiler listesini kim saklar ve değişiklik süresi nedir?",
        "MKK'ya bildirir; liste en geç iki iş gününde güncellenir",
        ["Vergi dairesine bildirir; güncelleme süresi beş yıldır", "Yalnız borsaya sözlü bildirir; süre sınırı bulunmaz", "Ticaret siciline bildirir; listeyi yatırımcılar saklar", "Hiçbir kuruma bildirmez; liste yalnız personelde tutulur"],
        "II-15.1 sayılı Tebliğ m.7, düzenli erişimi olan kişilerin MKK'ya bildirilmesini ve değişikliklerin en geç iki iş günü içinde güncellenmesini öngörür; liste MKK tarafından saklanır.",
        "Listeye yeni kişi eklenmesi, erişim nedeninin değişmesi veya erişimin sona ermesi güncelleme gerektiren durumlardandır.",
        "Özel Durumlar Tebliği (II-15.1) m.7", "medium",
    ),
    r(
        "Şirket paylarının fiyatı ve işlem hacmi olağan piyasa koşullarıyla açıklanamayacak ölçüde değişmiş, ilgili borsa açıklama istemiştir. İhraççı nasıl davranmalıdır?",
        "Olağan dışı fiyat veya işlem hacmi hareketinde açıklama yükümlülüğü ne zaman doğar?",
        "Borsanın talebi üzerine açıklanmamış özel durumları da belirtir",
        ["Talebi reddeder; fiyat hareketi hiçbir zaman açıklama gerektirmez", "Yalnız gelecek yılın faaliyet raporunda genel bilgi verir", "Borsanın talebini beklemeden işlemleri kesin olarak iptal eder", "Sadece fiyatın yükseldiğini tekrarlar, özel durumları değerlendirmez"],
        "II-15.1 sayılı Tebliğ m.8, olağan piyasa koşullarıyla açıklanamayan fiyat veya hacim değişiminde ilgili borsanın talebi üzerine açıklama yapılmasını öngörür.",
        "Açıklamada kamuya henüz duyurulmamış özel durum bulunup bulunmadığı belirtilir; varsa erteleme hükümleri saklı kalmak üzere açıklanmamış özel durumlara yer verilir.",
        "Özel Durumlar Tebliği (II-15.1) m.8", "medium",
    ),
    r(
        "Basında şirketin değerini etkileyebilecek ve daha önce açıklanan bilgiden farklı bir haber çıkmıştır. Şirket, Kuruldan uyarı gelmediği için açıklama yapmamıştır. Bu tutum uygun mudur?",
        "Önemli haber veya söylentinin doğrulanmasına ilişkin yükümlülük nasıl yerine getirilir?",
        "Hayır; uyarı beklenmeden doğruluk ve yeterlilik açıklanır",
        ["Evet; yalnız Kurul yazılı uyarı gönderirse açıklama yapılır", "Evet; basındaki her haber kendiliğinden KAP açıklaması sayılır", "Hayır; fakat haberin doğru olup olmadığı hiçbir zaman belirtilmez", "Evet; ihraççı hakkında çıkan söylentiler mevzuat dışında kalır"],
        "II-15.1 sayılı Tebliğ m.9, değer, fiyat veya yatırım kararını etkileyebilecek önemli ve yeni ya da farklı içerikteki haber veya söylentinin doğruluk ve yeterliliğinin uyarı beklenmeden açıklanmasını gerektirir.",
        "Haber ertelenmiş bilgiye ilişkinse erteleme sebepleri sona ermiş kabul edilir. Kamuya açıklanmış verilere dayalı analiz ve tahminler ise bu yükümlülüğün dışındadır.",
        "Özel Durumlar Tebliği (II-15.1) m.9", "medium",
    ),
    r(
        "İhraççı, gelecek yılın satış beklentisini ilk kez kamuya açıklamak istemektedir. Yönetim kurulu kararı alınmadan ve KAP'a bildirim yapılmadan yalnız basın toplantısında duyuru yapılması uygun mudur?",
        "Geleceğe yönelik değerlendirmelerin açıklanması bakımından genel esas hangisidir?",
        "Hayır; yetkili yazılı karar ve KAP açıklaması gerekir",
        ["Evet; tahminler hiçbir kurala tabi olmadan duyurulabilir", "Evet; basın toplantısı KAP açıklamasının her zaman yerine geçer", "Hayır; geleceğe yönelik değerlendirme açıklamak tamamen yasaktır", "Evet; yalnız çalışanlara duyurulması kamuya açıklama sayılır"],
        "Geleceğe yönelik değerlendirme açıklamak zorunlu değildir; açıklanacaksa yönetim kurulu kararına veya yetkilinin yazılı onayına dayanmalı ve KAP'ta duyurulmalıdır.",
        "Yönetim geleceğe yönelik değerlendirmeyi yılda en fazla dört kez açıklar; önceden açıklanan değerlendirmede önemli değişiklik olursa sayı sınırından bağımsız güncelleme yapılır.",
        "Özel Durumlar Tebliği (II-15.1) m.9/4 ve m.10", "hard",
    ),
    r(
        "17.07.2026 tarihinde bir yatırımcının borsada işlem gören ihraççıdaki doğrudan payı %4,8'den %5,2'ye çıkmıştır. Mevzuattaki eşik bakımından hangi sonuç doğar?",
        "17.07.2026 itibarıyla borsada işlem gören ihraççıda sermaye veya oy hakkı değişiklikleri için kullanılan eşikler hangileridir?",
        "%5 eşiğine ulaşılmıştır; doğrudan değişiklik açıklamasını MKK yapar",
        ["Hiçbir eşik aşılmamıştır; ilk bildirim oranı yalnız %25'tir", "Yatırımcı doğrudan değişikliği beş yıl sonra açıklar", "Pay oranı %100 olmadıkça hiçbir açıklama yapılmaz", "Değişiklik yalnız şirket çalışanlarına sözlü bildirilir"],
        "II-15.1 sayılı Tebliğ m.12; %5, %10, %15, %20, %25, %33, %50, %67 ve %95 eşiklerine ulaşma veya altına düşmeyi açıklamaya bağlar. Doğrudan pay değişikliği açıklamasını MKK yapar.",
        "Birlikte hareket, dolaylı sahiplik veya oy haklarına bağlı eşik değişiminde açıklama yükümlülüğü ilgili gerçek ya da tüzel kişiye veya birlikte hareket edenlere aittir.",
        "Özel Durumlar Tebliği (II-15.1) m.12", "hard",
    ),
    r(
        "İhraççının KAP'ta yayımlanan iletişim adresi değişmiştir. Şirket, bir sonraki yıllık rapora kadar güncelleme yapmamayı planlamaktadır. Süre bakımından doğru işlem hangisidir?",
        "KAP'ta yayımlanan ihraççıya ilişkin genel bilgilerde değişiklik olursa güncelleme süresi nedir?",
        "Genel bilgi en geç iki iş günü içinde güncellenir",
        ["Güncelleme yalnız beş yılın sonunda yapılır", "Adres değişikliği hiçbir zaman güncellenmez", "Güncelleme yalnız genel kurulun on yıl sonra alacağı kararla yapılır", "Bilgi her durumda aynı gün ticaret sicilinden kendiliğinden silinir"],
        "II-15.1 sayılı Tebliğ m.20 ve Kurulun borsa şirketleri açıklamaları, KAP'taki ihraççı genel bilgilerindeki değişikliğin en geç iki iş günü içinde güncellenmesini gerektirir.",
        "Genel bilgilerdeki değişiklik için yıllık rapor beklenmez; KAP formu güncel tutulur.",
        "Özel Durumlar Tebliği (II-15.1) m.20; SPK Borsa Şirketlerinin Yükümlülükleri", "easy",
    ),
    r(
        "Payları borsada işlem gören ihraççı, özel durum açıklamasını yalnız İngilizce olarak e-posta ile yatırımcılara göndermiştir. Bildirim şekli uygun mudur?",
        "Özel durum açıklamalarının dili ve borsada işlem gören ihraççı için bildirim kanalı nedir?",
        "Türkçe açıklama KAP'taki ilgili form kullanılarak yapılır",
        ["Yalnız yabancı dilde özel e-posta gönderilmesi yeterlidir", "Açıklama sadece yönetim kurulu defterine yazılarak yapılır", "Borsada işlem gören ihraççı açıklamayı yalnız Kurula fiziken verir", "Dili ihraççı seçer ve hiçbir elektronik form kullanılamaz"],
        "II-15.1 sayılı Tebliğ m.23'e göre açıklamaların dili Türkçedir; Kurul ayrıca başka dil isteyebilir. Borsada işlem gören ihraççı açıklamayı KAP'taki ilgili form üzerinden yapar.",
        "Borsada işlem görmeyen ihraççı için açıklamanın Kurula gönderilmesi ve Kurul sitesinde duyurulması rejimi uygulanabilir; bu ayrım e-postayı resmî kanal yapmaz.",
        "Özel Durumlar Tebliği (II-15.1) m.23/1-2", "medium",
    ),
    r(
        "Şirket, derhal yapılması gereken açıklamayı bir hafta geciktirmiş ve metinde kendi kayıtlarıyla uyum konusunda sorumluluk üstlenmediğini belirtmiştir. Tebliğe uygun mudur?",
        "Özel durum açıklamasında süre ve sorumluluk beyanı bakımından hangi esas uygulanır?",
        "Hayır; kural derhal açıklama ve tamlık-doğruluk beyanıdır",
        ["Evet; bütün açıklamalar için bir haftalık genel bekleme süresi vardır", "Evet; ihraççı açıklamanın doğruluğundan sorumlu değildir", "Hayır; fakat açıklama yalnız sözlü yapılmalı ve kayıt içermemelidir", "Evet; defter ve belgelere aykırılık özellikle beyan edilmelidir"],
        "II-15.1 sayılı Tebliğ m.23, aksi belirtilmedikçe açıklamanın derhal yapılmasını ve metnin bilginin tam yansıtıldığı, kayıtlarla uyumlu olduğu, doğru bilgi için çaba gösterildiği ve sorumluluk üstlenildiği beyanını içermesini öngörür.",
        "Kamuyu aydınlatma metni yalnız olay anlatımı değildir; açıklamanın mevzuata ve kayıtlara uygunluğu konusunda sorumluluk beyanı da taşır.",
        "Özel Durumlar Tebliği (II-15.1) m.23/2", "medium",
    ),
    r(
        "İhraççı, hassas açıklama yayımlanmadan önce bilgi asimetrisinin artmasından endişe etmektedir. Borsadan sermaye piyasası aracındaki işlemleri geçici durdurmasını isteyebilir mi?",
        "Açıklama yükümlülüğünde hızlı erişim ve yatırımcılar arasında eşit işlem ilkesi nasıl desteklenebilir?",
        "Evet; açıklama öncesi borsadan geçici durdurma talep edebilir",
        ["Hayır; işlem sırasının geçici durması hiçbir zaman istenemez", "Evet; fakat yalnız açıklama beş yıl geciktirildikten sonra istenir", "Hayır; bilgiye yalnız büyük yatırımcıların erken erişmesi gerekir", "Evet; talep doğrudan yatırımcıların hesaplarını kapatır"],
        "II-15.1 sayılı Tebliğ m.23/5-6, açıklamanın hızlı erişim ve yatırımcılar arasında eşit işlem ilkesine uygun yapılmasını; açıklama öncesinde borsadan geçici işlem durdurma talep edilebilmesini düzenler.",
        "Geçici durdurma kendiliğinden gerçekleşmez; ihraççı ilgili borsaya talepte bulunabilir ve borsanın ilan ettiği usuller uygulanır.",
        "Özel Durumlar Tebliği (II-15.1) m.23/5-6", "medium",
    ),
    r(
        "Şirket daha önce duyurduğu fabrika yatırımının ilerlemesinde önemli değişiklik yaşamış, ancak 'ilk açıklama yeterlidir' diyerek güncelleme yapmamıştır. Doğru yaklaşım hangisidir?",
        "Sonuçlanmamış bir özel durum açıklamasındaki gelişmeler için güncel kural nedir?",
        "Gelişme ve değişiklikler oldukça güncellenerek duyurulur",
        ["İlk açıklamadan sonra hiçbir güncelleme yapılamaz", "Her durumda gelişme olmasa bile 60 günde bir açıklama zorunludur", "Güncelleme yalnız yatırım tamamlandıktan beş yıl sonra yapılır", "Yalnız olumsuz gelişmeler açıklanır, olumlu değişiklikler gizlenir"],
        "II-15.1 sayılı Tebliğ m.23/7, daha önce açıklanan özel durumlardaki gelişme ve değişikliklerin sürekli güncellenmesini ister.",
        "2018 değişikliğiyle gelişme olmayan konular için 60 günde bir tekrar açıklama zorunluluğu kaldırılmıştır; güncel kural gerçekleşen gelişme ve değişiklikleri duyurmaktır.",
        "Özel Durumlar Tebliği (II-15.1) m.23/7; II-15.1.c değişikliği", "hard",
    ),
    r(
        "Şirket kazandığı büyük ihaleyi açıklarken tutarı, karşı tarafı ve finansal etkileri ölçülebilir olduğu hâlde gizleyip yalnız 'çok büyük başarı' ifadesini kullanmıştır. Metin yeterli midir?",
        "Özel durum açıklamasının yatırım kararına yardım edebilmesi için hangi nitelikleri taşıması gerekir?",
        "Hayır; zamanında, doğru, tam, dolaysız, anlaşılır ve yeterli olmalıdır",
        ["Evet; övgü içeren kısa slogan bütün ayrıntıların yerine geçer", "Evet; açıklamanın belirsiz ve dolaylı olması özellikle gerekir", "Hayır; fakat karşı taraf ve ölçülebilir tutar hiçbir zaman yazılmaz", "Evet; yalnız şirket lehine bilgiler seçilerek açıklanabilir"],
        "II-15.1 sayılı Tebliğ m.24/1, açıklamanın zamanında, doğru, tam, dolaysız, anlaşılabilir ve yeterli olmasını; gerekiyorsa karşı taraf ile ölçülebilir miktar veya tutarın belirtilmesini gerektirir.",
        "Yatırımcının olayı değerlendirmesine yarayan somut unsurlar açıklanabilir olduğu ölçüde verilmelidir; pazarlama sıfatları bilgi yerine geçmez.",
        "Özel Durumlar Tebliği (II-15.1) m.24/1", "medium",
    ),
    r(
        "Şirket henüz kesinleşmemiş önemli bir ruhsat başvurusunu açıklamış, ancak belirsizliği ve sonucun ne zaman netleşeceğini belirtmemiştir. Açıklama nasıl tamamlanmalıdır?",
        "Henüz kesinleşmemiş özel durumun açıklanmasında belirsizlik nasıl ele alınır?",
        "Belirsizlik, öngörülen tarih ve gereken koşullar belirtilir",
        ["Belirsiz olay kesinleşmiş gibi sunulur ve takip açıklaması yapılmaz", "Başvuru tümüyle gizlenir; erteleme koşulları hiç değerlendirilmez", "Yalnız şirketin iyimser görüşü yazılır, koşullar açıklanmaz", "Sonuç tarihi geçmiş olsa da kamuya hiçbir bilgi verilmez"],
        "II-15.1 sayılı Tebliğ m.24/2, belirsiz özel durumun belirsizliği belirtilerek açıklanmasını; öngörülen çözüm tarihi ve gereken koşulların yazılmasını ister.",
        "Öngörülen tarihte belirsizliğin çözülüp çözülmediği de kamuya açıklanır; erteleme koşullarının bulunduğu durumlar ayrıca değerlendirilir.",
        "Özel Durumlar Tebliği (II-15.1) m.24/2", "hard",
    ),
    r(
        "İhraççı özel durum açıklamasını kesin kazanç vaat eden reklam metnine dönüştürmüş, yönetim kurulu ise açıklama prosedürü belirlememiştir. Uygulama uygun mudur?",
        "Özel durum açıklamalarında reklam yasağı ve kurumsal prosedür sorumluluğu nasıl düzenlenmiştir?",
        "Hayır; reklam yapılamaz ve prosedürü yönetim kurulu belirler",
        ["Evet; KAP açıklamasının temel amacı ürün pazarlamasıdır", "Evet; yönetim kurulunun hiçbir kamuyu aydınlatma görevi yoktur", "Hayır; fakat yalnız olumsuz açıklamalar reklam olarak kullanılabilir", "Evet; temelsiz ve abartılı ifadeler yatırımcıyı bilgilendirir"],
        "II-15.1 sayılı Tebliğ m.24/3-4, açıklamanın yanlış, yanıltıcı, temelsiz, abartılı veya eksik olmasını ve reklam amacıyla kullanılmasını yasaklar; etkin prosedürleri yönetim kurulu belirler.",
        "Kamuyu aydınlatma tarafsız ve doğrulanabilir bilgi vermeye yöneliktir; pazarlama faaliyeti değildir.",
        "Özel Durumlar Tebliği (II-15.1) m.24/3-4", "easy",
    ),
    r(
        "Payları borsada işlem gören ihraççı, KAP açıklamasını internet sitesine üç gün sonra koymuş ve bir yıl sonra silmiştir. Süreler bakımından uygun mudur?",
        "Borsada işlem gören ihraççının özel durum açıklamasını internet sitesinde ilan ve saklama süresi nedir?",
        "Hayır; sonraki iş gününe kadar ilan edilir ve beş yıl saklanır",
        ["Evet; üç gün içinde ilan ve bir yıl saklama yeterlidir", "Hayır; açıklama yalnız on yıl sonra internet sitesine konur", "Evet; KAP'ta yayımlanan açıklama internet sitesinde asla gösterilemez", "Hayır; bütün açıklamalar yayımlandığı gün kalıcı olarak silinir"],
        "II-15.1 sayılı Tebliğ m.24/5, borsada işlem gören ihraççının açıklamayı en geç kamuya açıklamadan sonraki iş günü sitesinde ilan etmesini ve beş yıl bulundurmasını gerektirir.",
        "İnternet sitesinden KAP'taki açıklamaya bağlantı verilmesi de yükümlülüğü yerine getirebilir.",
        "Özel Durumlar Tebliği (II-15.1) m.24/5", "medium",
    ),
    r(
        "Çalışan, henüz KAP'ta yayımlanmamış özel durumu arkadaş grubunda paylaşmıştır. Bilginin açıklanması gereken nitelikte olması karşısında hangi yükümlülük ihlal edilmiştir?",
        "Açıklanması gereken özel durumun kamuya duyurulmasına kadar bilgi sahiplerinin temel yükümlülüğü nedir?",
        "Bilginin kamuya duyurulmasına kadar gizliliği korunmalıdır",
        ["Bilgi önce seçilmiş yatırımcılara serbestçe dağıtılmalıdır", "Gizlilik yalnız açıklamadan beş yıl sonra başlamalıdır", "Bilgi KAP yerine söylenti kanallarıyla yayılmalıdır", "Çalışan bilgiyi kullanarak işlem yapmaya teşvik edilmelidir"],
        "II-15.1 sayılı Tebliğ m.25, açıklanması gereken özel durum hakkında bilgi sahibi olanların kamuya duyuruya kadar gizliliği korumasını zorunlu tutar.",
        "Kurul ayrıca zamanında, tam ve doğru aydınlatma için ihraççı veya ilgili taraftan açıklama ve gerektiğinde basın-yayın organlarında ilan isteyebilir.",
        "Özel Durumlar Tebliği (II-15.1) m.25-26", "easy",
    ),
    r(
        "Borsada işlem gören ortaklık, finansal tablolarını kendi seçtiği biçimde hazırlamış, bağımsız denetime göndermemiş ve kamuya açıklamamıştır. Bu yaklaşım uygun mudur?",
        "Payları borsada işlem gören ortaklıkların finansal tablo ve raporlarına ilişkin temel yükümlülük nedir?",
        "Hayır; TMS esaslı rapor hazırlanır, gerekli denetim ve açıklama yapılır",
        ["Evet; finansal raporlama halka açık ortaklık için tamamen ihtiyaridir", "Evet; finansal tabloyu yalnız Kurul hazırlar ve şirket işlem yapmaz", "Hayır; fakat finansal tabloların kamuya açıklanması kesinlikle yasaktır", "Evet; bağımsız denetim yerine şirketin reklam ajansı görüş verir"],
        "6362 sayılı Kanun m.14 ve Kurul düzenlemeleri, finansal tablo ve raporların TMS çerçevesinde zamanında, tam ve doğru hazırlanmasını, belirlenenlerin bağımsız denetimden geçirilmesini ve kamuya açıklanmasını gerektirir.",
        "Finansal raporlama da kamuyu aydınlatmanın parçasıdır; şirketin serbest biçimde seçtiği gizli bir iç raporlama süreci değildir.",
        "6362 sayılı Sermaye Piyasası Kanunu m.14; SPK Borsa Şirketlerinin Yükümlülükleri", "medium",
    ),
]


PREMISES = [
    {
        "stem": "Kamuyu aydınlatma kavramları bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. KAP, elektronik imzalı açıklamaların kamuya duyurulduğu sistemdir\n\nII. Sürekli bilgi yalnız içsel bilgileri ifade eder\n\nIII. Özel durum, içsel veya sürekli bilgiyi kapsar",
        "correct": "I ve III",
        "why": "KAP elektronik imzalı kamuyu aydınlatma sistemidir ve özel durum içsel veya sürekli bilgiyi kapsar. Sürekli bilgi içsel bilgi tanımının dışında kaldığından II doğru değildir.",
        "ref": "Özel Durumlar Tebliği (II-15.1) m.4", "difficulty": "medium",
    },
    {
        "stem": "İçsel bilginin açıklanmasının ertelenmesi bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Erteleme ihraççının sorumluluğundadır\n\nII. Erteleme yatırımcıların yanıltılmasına yol açmamalıdır\n\nIII. İhraççı bilginin gizliliğini sağlayabilmelidir",
        "correct": "I, II ve III",
        "why": "Meşru çıkarın korunması amacıyla yapılabilecek ertelemede sorumluluk ihraççıdadır; yatırımcı yanıltılmamalı ve bilgi gizli tutulabilmelidir.",
        "ref": "Özel Durumlar Tebliği (II-15.1) m.6/1", "difficulty": "easy",
    },
    {
        "stem": "Erteleme sonrasında izlenecek süreç bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Erteleme sebepleri ortadan kalkınca bilgi açıklanır\n\nII. Açıklamada erteleme kararı ve temel sebepleri belirtilir\n\nIII. Gizlilik bozulsa bile açıklama süresiz ertelenebilir",
        "correct": "I ve II",
        "why": "Erteleme sebepleri kalkınca bilgi ile erteleme kararı ve temel sebepleri açıklanır. Gizliliğin sağlanamaması açıklama gerektirdiğinden III doğru değildir.",
        "ref": "Özel Durumlar Tebliği (II-15.1) m.6/2-3", "difficulty": "medium",
    },
    {
        "stem": "Haberler ve geleceğe yönelik değerlendirmeler bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Önemli ve farklı içerikteki söylenti için Kurul uyarısı beklenir\n\nII. Geleceğe yönelik değerlendirme açıklamak zorunlu değildir\n\nIII. Açıklanan tahminde önemli değişiklik olursa sayı sınırından bağımsız güncelleme yapılır",
        "correct": "II ve III",
        "why": "Geleceğe yönelik değerlendirme ihtiyaridir ve önemli değişiklikte sayı sınırından bağımsız güncellenir. Önemli söylentinin doğrulanması için Kurul uyarısı beklenmediğinden I doğru değildir.",
        "ref": "Özel Durumlar Tebliği (II-15.1) m.9-10", "difficulty": "hard",
    },
    {
        "stem": "Özel durum açıklamasının bildirim biçimi bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Açıklamaların dili Türkçedir\n\nII. Borsada işlem gören ihraççı ilgili KAP formunu kullanır\n\nIII. Aksi belirtilmedikçe açıklamanın derhal yapılması esastır",
        "correct": "I, II ve III",
        "why": "II-15.1 sayılı Tebliğ, Türkçe açıklamayı, borsada işlem gören ihraççı için ilgili KAP formunu ve aksi belirtilmedikçe derhal bildirim esasını birlikte düzenler.",
        "ref": "Özel Durumlar Tebliği (II-15.1) m.23/1-2", "difficulty": "easy",
    },
    {
        "stem": "Açıklamanın içeriği bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Açıklama yatırım kararına yardım edecek ölçüde yeterli olmalıdır\n\nII. Açıklama reklam amacıyla kullanılabilir\n\nIII. Ölçülebilir etki varsa miktar veya tutar bilgisine yer verilir",
        "correct": "I ve III",
        "why": "Açıklama yeterli olmalı ve ölçülebilir etkiyi miktar veya tutarla göstermelidir. Özel durum açıklaması reklam amacıyla kullanılamadığından II doğru değildir.",
        "ref": "Özel Durumlar Tebliği (II-15.1) m.24/1 ve 3", "difficulty": "medium",
    },
    {
        "stem": "Sürekli bilgi ve güncelleme yükümlülüğü bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. KAP'taki genel bilgi değişikliği en geç iki iş gününde güncellenir\n\nII. Önceki özel durumdaki gelişme ve değişiklikler güncellenir\n\nIII. Gelişme olmasa da her durumda 60 günde bir açıklama zorunludur",
        "correct": "I ve II",
        "why": "Genel bilgiler iki iş gününde güncellenir ve önceki açıklamadaki gelişmeler duyurulur. Gelişme olmayan konulardaki 60 günlük tekrar zorunluluğu kaldırıldığından III doğru değildir.",
        "ref": "Özel Durumlar Tebliği (II-15.1) m.20 ve m.23/7; II-15.1.c", "difficulty": "hard",
    },
    {
        "stem": "İnternet sitesi ve gizlilik bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Borsada işlem gören ihraççı açıklamayı sonraki iş gününe kadar sitesinde ilan eder\n\nII. Açıklama internet sitesinde beş yıl bulundurulur\n\nIII. Açıklama öncesinde bilgi seçilmiş yatırımcılara serbestçe dağıtılır",
        "correct": "I ve II",
        "why": "İnternet sitesinde sonraki iş gününe kadar ilan ve beş yıllık saklama doğrudur. Açıklama öncesinde bilginin gizliliği korunacağından III doğru değildir.",
        "ref": "Özel Durumlar Tebliği (II-15.1) m.24/5 ve m.25", "difficulty": "medium",
    },
]


if __name__ == "__main__":
    write_topic(
        lesson_id="sermaye_piyasasi_ve_finans",
        topic_id="kamuyu_aydinlatma",
        label="Kamuyu Aydınlatma",
        slug="kamuyu_aydinlatma",
        prefix="topic-kap",
        seed=2026071737,
        legislation_version=(
            "6362 sayılı Sermaye Piyasası Kanunu; Özel Durumlar Tebliği II-15.1; "
            "Özel Durumlar Rehberi; SPK Borsa Şirketlerinin Yükümlülükleri "
            "(17.07.2026 kontrolü)"
        ),
        rules=RULES,
        premises=PREMISES,
        wrong_banks={},
    )
