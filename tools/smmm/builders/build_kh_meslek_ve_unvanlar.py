#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM Meslek Hukuku — Meslek ve Unvanlar, 3×20."""
from topic_pack_builder import write_topic


SHORT = {
    "SMMM ve YMM meslekleriyle kuruluşlarını düzenlemek": "SMMM ve YMM meslek düzenini kurmak",
    "Serbest muhasebeci mali müşavir ve yeminli mali müşavir": "Ruhsatlı SMMM ve YMM unvanları",
    "Evet; SMMM mesleğinin konusundadır": "Evet; SMMM meslek kapsamındadır",
    "Evet; SMMM meslek konusu içindedir": "Evet; ruhsatlı SMMM bu işi yapabilir",
    "Evet; SMMM bu faaliyetleri yapabilir": "Evet; bu faaliyette SMMM yetkilidir",
    "Görev meslek konusuyla uyumludur": "Evet; bu görev meslek konusundadır",
    "Evet; m. 2/A'nın b ve c bentlerindeki işleri yapabilir": "Evet; YMM bu işleri yapabilir",
    "Kanuna aykırı unvan kullanımıdır": "Haksız unvan kullanımıdır",
    "Evet; benzer ibare ve remizler de yasaktır": "Evet; benzer ifadeler de yasaktır",
    "Hayır; önce kanuni yeminini etmelidir": "Hayır; önce yemin etmelidir",
    "Yetkili memurlarca incelenmiş belge sayılır": "İncelenmiş belge kabul edilir",
    "Tasdikinin doğruluğundan sorumludur": "Tasdik doğruluğundan sorumludur",
    "Tasdik kapsamıyla sınırlı müşterek ve müteselsil sorumluluk": "Sınırlı müşterek ve müteselsil sorumluluk",
    "Mesleki ortaklık mümkündür ve faaliyet ticari sayılmaz": "Ortaklık mümkündür; ticari sayılmaz",
    "Serbest muhasebeci mali müşavirde": "Serbest çalışan SMMM'de",
    "Serbest muhasebeci mali müşavir": "Bağımsız çalışan SMMM",
    "İşyerine bağlı olmaksızın mesleki işi yapmak": "Mesleki işi işyerine bağlı olmadan yapmak",
    "Sistem-müşavirlik ile inceleme ve raporlama işleri": "Müşavirlik ve raporlama işleri",
    "Yalnız kanunen kullanmaya yetkili olanlar": "Ruhsatlı meslek mensupları",
    "Hayır; karışabilecek benzer ifadeleri de kapsar": "Hayır; benzer ifadeler de korunur",
    "Yeminli mali müşavirlik tasdikidir": "YMM tasdik işlemidir",
    "Mevzuat, muhasebe ilkeleri ve standartlarına uygunluk incelemesi": "Standartlara uygunluk incelemesi",
    "Hayır; çalıştıramaz ve işbirliği yapamaz": "Hayır; mesleki işbirliği yasaktır",
    "Hayır; kanundaki ortaklık faaliyeti ticari sayılmaz": "Hayır; mesleki ortaklık ticari sayılmaz",
    "İşi yapan meslek mensubuna": "İşi yapan kişiye",
}


def r(scenario, focus, correct, distractors, why, ref, difficulty="medium",
      focus_correct=None, focus_distractors=None, focus_why=None):
    correct = SHORT.get(correct, correct)
    focus_correct = SHORT.get(focus_correct or correct, focus_correct or correct)
    if correct == "Asliye ticaret mahkemesinde":
        distractors = [
            "Vergi mahkemesi başkanlığında",
            "Asliye hukuk mahkemesinde",
            "Oda disiplin kurulu önünde",
            "TÜRMOB yönetim kurulu önünde",
        ]
        focus_distractors = distractors
    return {
        "scenario": scenario, "focus": focus, "correct": correct,
        "focus_correct": focus_correct,
        "distractors": list(distractors),
        "focus_distractors": list(focus_distractors or distractors),
        "why": why,
        "focus_why": focus_why or f"Kuralın odak noktası şudur: {why}",
        "ref": ref,
        "difficulty": difficulty,
    }


RULES = [
    r("İşletme sonuçlarının gerçek durumu yansıtacak biçimde tarafsız sunulmasını ve yüksek mesleki standartları hedefleyen kanun hangisidir?", "3568 sayılı Kanunun temel amacı aşağıdakilerden hangisini içerir?", "SMMM ve YMM meslekleriyle kuruluşlarını düzenlemek", ["Yalnız vergi oranlarını belirlemek", "Sadece şirket kuruluşunu tescil etmek", "Kamu personelinin maaşını düzenlemek", "Bankaların kredi politikasını belirlemek"], "Kanun, SMMM ve YMM meslekleri ile odaları ve TÜRMOB'un kuruluş ve işleyişini düzenleyerek yüksek mesleki standartları amaçlar.", "3568 sayılı Kanun m. 1", "easy"),
    r("3568 sayılı Kanuna göre ruhsatla kullanılan güncel meslek unvanları hangileridir?", "Kanunun düzenlediği iki temel meslek unvanı hangisidir?", "Serbest muhasebeci mali müşavir ve yeminli mali müşavir", ["Serbest muhasebeci ve bağımsız denetçi", "Mali müşavir adayı ve vergi müfettişi", "Muhasebe uzmanı ve şirket denetçisi", "Defterdar ve gelir uzmanı"], "Kanun, meslek icrasına hak kazananları SMMM ve YMM olarak adlandırır.", "3568 sayılı Kanun m. 1", "easy"),
    r("Bir SMMM, işletmenin genel kabul görmüş muhasebe ilkelerine göre defterlerini tutup bilançosunu düzenlemiştir. Bu iş mesleğin konusu içinde midir?", "Defter tutma, bilanço ve beyanname düzenleme görevi hangi unvanın meslek konusu içindedir?", "Evet; SMMM mesleğinin konusundadır", ["Hayır; yalnız noter yapabilir", "Hayır; sadece YMM tasdik görevidir", "Yalnız vergi idaresi yapabilir", "Sadece bağımsız denetim kuruluşu yapabilir"], "Defter tutma ile bilanço, kâr-zarar tablosu ve beyanname düzenleme SMMM mesleğinin konusundadır.", "3568 sayılı Kanun m. 2/A-a", "easy", focus_correct="Serbest muhasebeci mali müşavir"),
    r("İşletme muhasebe sistemini kurmak ve mali mevzuat uygulamalarında danışmanlık almak istemektedir. SMMM bu işi yapabilir mi?", "Muhasebe sistemini kurma, geliştirme ve mali mevzuat müşavirliği hangi kapsamda yer alır?", "Evet; SMMM meslek konusu içindedir", ["Hayır; yalnız mahkeme bilirkişisi yapabilir", "Hayır; sadece banka müfettişi yapabilir", "Yalnız noterlik hizmetidir", "Sadece gümrük müşaviri yapabilir"], "Muhasebe sistemlerini kurmak, geliştirmek ve mali mevzuat müşavirliği yapmak SMMM meslek konusundadır.", "3568 sayılı Kanun m. 2/A-b", "easy", focus_correct="SMMM'nin danışmanlık ve sistem kurma işleri"),
    r("Meslek mensubu belgelere dayanarak mali inceleme yapmış ve yazılı görüş raporu hazırlamıştır. Bu faaliyet SMMM meslek konusu içinde midir?", "Mali tablo ve beyannameler hakkında inceleme, tahlil ve yazılı görüş verme yetkisi kimdedir?", "Evet; SMMM bu faaliyetleri yapabilir", ["Hayır; yalnız savcı yapabilir", "Sadece ticaret sicili yapabilir", "Yalnız noter yapabilir", "Hiçbir meslek mensubu yapamaz"], "Belgelere dayalı inceleme, tahlil, denetim, rapor ve yazılı görüş SMMM meslek konusundadır.", "3568 sayılı Kanun m. 2/A-c", "medium", focus_correct="Serbest muhasebeci mali müşavirde"),
    r("Bir uyuşmazlıkta mali konuda tahkim ve bilirkişilik görevi önerilen SMMM görevi kabul etmiştir. Yetki bakımından sonuç nedir?", "Tahkim ve bilirkişilik 3568 sayılı Kanundaki meslek konusu içinde sayılmış mıdır?", "Görev meslek konusuyla uyumludur", ["Görev yalnız hâkimlere özgüdür", "SMMM'nin ruhsatını kendiliğinden düşürür", "Yalnız YMM yeminiyle yapılabilir", "Meslekle bütünüyle ilgisizdir"], "Mali konularda tahkim, bilirkişilik ve benzeri işler SMMM meslek konusu içinde sayılmıştır.", "3568 sayılı Kanun m. 2/A-c", "medium", focus_correct="Evet; meslek konusu içinde sayılmıştır"),
    r("Muhasebe ve mali müşavirlik işlerini bir işyerine bağlı olmaksızın yapan ruhsatlı kişi hangi unvanı taşır?", "SMMM tanımında çalışma biçimi bakımından aranan unsur hangisidir?", "Serbest muhasebeci mali müşavir", ["Yeminli tercüman", "Vergi müfettişi", "Şirket murakıbı", "Gelir uzmanı"], "Kanun, m. 2/A'daki işleri bir işyerine bağlı olmaksızın yapan kişiyi SMMM olarak tanımlar.", "3568 sayılı Kanun m. 2/A", "easy", focus_correct="İşyerine bağlı olmaksızın mesleki işi yapmak", focus_distractors=["Mutlaka kamu görevlisi olarak çalışmak", "Yalnız ticaret şirketi ortağı olmak", "Hiç ruhsat almadan danışmanlık yapmak", "Sadece vergi incelemesi yürütmek"]),
    r("YMM, SMMM'nin sistem kurma ve inceleme işlerini yapmak istemektedir. Kanuni görev alanı buna izin verir mi?", "YMM'ler SMMM meslek konusundaki hangi işleri yapabilir?", "Evet; m. 2/A'nın b ve c bentlerindeki işleri yapabilir", ["Hayır; yalnız yemin ederler", "Sadece defter tutabilirler", "Yalnız bordro düzenleyebilirler", "Hiçbir müşavirlik işi yapamazlar"], "YMM'ler sistem kurma ve müşavirlik ile inceleme, tahlil, denetim ve raporlama işlerini yapabilir.", "3568 sayılı Kanun m. 2/B", "medium", focus_correct="Sistem-müşavirlik ile inceleme ve raporlama işleri"),
    r("Bir mali tablonun mevzuata ve muhasebe standartlarına uygunluğunun tasdiki istenmektedir. Tasdik yetkisi hangi unvana aittir?", "3568 sayılı Kanuna göre tasdik işi kimin meslek konusudur?", "Yeminli mali müşavirin", ["Herhangi bir muhasebe çalışanının", "Ruhsatsız danışmanın", "Yalnız şirket ortağının", "Stajyer meslek mensubunun"], "Tasdik, YMM mesleğinin SMMM görevlerine ek özel yetkisidir.", "3568 sayılı Kanun m. 2/B ve 12", "easy"),
    r("YMM bir müşterinin muhasebe defterlerini tutmak için sözleşme yapmak istemektedir. Kanuni sınır bakımından sonuç nedir?", "YMM'lerin defter tutma yetkisi bakımından temel kural hangisidir?", "YMM muhasebe defteri tutamaz", ["YMM bütün müşterilerin defterini tutabilir", "Yalnız ücret almadan tutabilir", "Sadece akrabasının defterini tutabilir", "Oda izniyle sınırsız tutabilir"], "YMM'lerin muhasebe ile ilgili defter tutması yasaktır.", "3568 sayılı Kanun m. 2/B", "easy"),
    r("YMM, tasdik hizmetinin yanında kendi adına muhasebe bürosu açmayı planlamaktadır. Bu mümkün müdür?", "YMM'nin muhasebe bürosu açması veya böyle bir büroya ortak olması hakkında kural nedir?", "Hayır; açamaz ve ortak olamaz", ["Evet; hiçbir sınırlama yoktur", "Yalnız başka ilde açabilir", "Sadece anonim şirket biçiminde açabilir", "Oda kaydı olmadan açabilir"], "YMM muhasebe bürosu açamaz ve muhasebe bürosuna ortak olamaz.", "3568 sayılı Kanun m. 2/B", "easy"),
    r("Ruhsatı olmayan kişi tabelasında 'serbest muhasebeci mali müşavir' ibaresini kullanmıştır. Fiilin niteliği nedir?", "SMMM ve YMM unvanlarını kimler kullanabilir?", "Kanuna aykırı unvan kullanımıdır", ["Serbest bir ticari tanıtımdır", "Oda kaydı gerektirmeyen kullanımdır", "Yalnız vergi idaresini ilgilendiren işlemdir", "Ruhsat yerine geçen kullanımdır"], "Kanunen yetkili olmayanların SMMM veya YMM unvanını kullanması yasaktır.", "3568 sayılı Kanun m. 3", "easy", focus_correct="Yalnız kanunen kullanmaya yetkili olanlar", focus_distractors=["Dileyen bütün şirket çalışanları", "En az bir yıl muhasebe yapan herkes", "Herhangi bir lisans mezunu", "Yalnız işverenin izin verdiği kişiler"]),
    r("Ruhsatsız danışman, doğrudan SMMM yazmasa da bu unvanla karışabilecek benzer bir kısaltma kullanmıştır. Yasak kapsamına girer mi?", "Unvan yasağı yalnız SMMM ve YMM ibarelerinin birebir kullanımına mı ilişkindir?", "Evet; benzer ibare ve remizler de yasaktır", ["Hayır; benzer kısaltmalar tamamen serbesttir", "Yalnız yabancı dilde kullanım yasaktır", "Sadece kamu kurumlarında yasaktır", "Oda bölgesi dışında serbesttir"], "Yasak, unvanların yanında bunlarla karışabilecek benzer unvan, ibare ve remizleri de kapsar.", "3568 sayılı Kanun m. 3", "medium", focus_correct="Hayır; karışabilecek benzer ifadeleri de kapsar"),
    r("Oda, ruhsatsız bir kişinin YMM unvanını kullandığını öğrenmiştir. Odanın kanuni görevi nedir?", "Meslek unvanının haksız kullanıldığını öğrenen oda hangi makama bildirim yapar?", "Cumhuriyet savcılığına bildirmek", ["Yalnız kişiye sözlü uyarı vermek", "Dosyayı süresiz bekletmek", "Ticaret odasına ruhsat vermek", "Kişiyi kendiliğinden YMM kaydetmek"], "Odalar haksız unvan kullanımını öğrendiklerinde Cumhuriyet savcılığına bildirmek zorundadır.", "3568 sayılı Kanun m. 3", "medium", focus_correct="Cumhuriyet savcılığına"),
    r("YMM ruhsatını alan kişi fiilen göreve başlamadan önce yemin etmemiştir. Göreve başlayabilir mi?", "YMM yemini hangi aşamada yapılmalıdır?", "Hayır; önce kanuni yeminini etmelidir", ["Evet; yemin yalnız emeklilikte gerekir", "Evet; yemin tamamen isteğe bağlıdır", "Yemin yalnız SMMM için zorunludur", "Yemin yerine müşteri onayı yeterlidir"], "YMM mesleğine kabul edilenler fiilen göreve başlamadan önce yemin eder.", "3568 sayılı Kanun m. 11", "easy", focus_correct="Fiilen göreve başlamadan önce"),
    r("YMM adayı kanuni yeminini noter huzurunda yapmak istemektedir. Yetkili yer bakımından doğru seçenek hangisidir?", "YMM yemini hangi merci önünde yapılır?", "Asliye ticaret mahkemesinde", ["Vergi dairesinde", "Noterlikte", "Belediye meclisinde", "Ticaret odasında"], "Kanun, YMM yemininin Asliye Ticaret Mahkemesinde yapılmasını öngörür.", "3568 sayılı Kanun m. 11", "easy"),
    r("YMM, mali tablo ve beyannamelerin mevzuat ile standartlara uygunluğunu incelediğini onaylamıştır. Bu işlem nedir?", "Tasdik işlemi hangi uygunluk ve incelemeyi ifade eder?", "Yeminli mali müşavirlik tasdikidir", ["Sadece noter onayıdır", "Yalnız ticaret sicili tescilidir", "Vergi mahkemesi kararıdır", "Staj değerlendirmesidir"], "Tasdik; mali tablo ve beyannamelerin mevzuat, muhasebe ilkeleri ve standartlarına uygunluğunun denetim standartlarına göre incelendiğinin onaylanmasıdır.", "3568 sayılı Kanun m. 12", "medium", focus_correct="Mevzuat, muhasebe ilkeleri ve standartlarına uygunluk incelemesi"),
    r("YMM tasdik raporunda hangi hesap ve belgeleri incelediğini belirtmemiştir. Kanuni yükümlülük bakımından eksik olan nedir?", "YMM, yaptığı tasdikin kapsamını nerede açıkça göstermelidir?", "Tasdik kapsamını raporda açıklamak", ["Yalnız müşteriye sözlü bildirmek", "Kapsamı hiçbir yerde göstermemek", "Sadece ücret makbuzuna yazmak", "Oda seçiminde açıklamak"], "YMM yaptığı tasdikin kapsamını düzenlediği raporda açıkça belirtir.", "3568 sayılı Kanun m. 12", "medium", focus_correct="Düzenleyeceği tasdik raporunda"),
    r("Kamu idaresine sunulan tasdikli mali tablo, tasdik kapsamı ölçüsünde nasıl kabul edilir?", "YMM tasdikli belgenin kamu idaresindeki kanuni etkisi hangisidir?", "Yetkili memurlarca incelenmiş belge sayılır", ["Kesinleşmiş mahkeme kararı sayılır", "Hiç incelenmemiş belge sayılır", "Vergi borcunu kendiliğinden siler", "Mükellefiyeti sona erdirir"], "Tasdikli mali tablo, tasdik kapsamı ölçüsünde yetkili kamu görevlilerince incelenmiş belge kabul edilir.", "3568 sayılı Kanun m. 12", "hard"),
    r("Tasdikli mali tablo sunulması üzerine kamu idaresinin kanuni inceleme yetkisinin tamamen kalktığı ileri sürülmüştür. Bu doğru mudur?", "YMM tasdiki, kamu idaresinin teftiş ve inceleme yetkisini ortadan kaldırır mı?", "Hayır; inceleme yetkileri saklıdır", ["Evet; bütün kamu denetimi sona erer", "Yalnız ceza soruşturması sona erer", "Sadece mükellefin izniyle sürer", "Tasdik bütün yargı yollarını kapatır"], "Tasdik, kamu idaresine tanınan teftiş ve inceleme yetkilerinin kullanılmasını veya gerektiğinde tekrarını engellemez.", "3568 sayılı Kanun m. 12", "hard"),
    r("YMM'nin tasdik ettiği beyanname gerçeğe aykırı çıkmıştır. YMM'nin temel mesleki yükümlülüğü nedir?", "YMM yaptığı tasdik bakımından neden sorumludur?", "Tasdikinin doğruluğundan sorumludur", ["Yalnız ücretin tahsilinden sorumludur", "Hiçbir sonuçtan sorumlu değildir", "Sadece mükellefin kuruluşundan sorumludur", "Yalnız oda aidatından sorumludur"], "YMM, yaptığı tasdikin doğruluğundan sorumludur.", "3568 sayılı Kanun m. 12", "medium"),
    r("Yanlış tasdik nedeniyle vergi ziyaı ve ceza doğmuştur. YMM'nin mali sorumluluğunun niteliği nedir?", "Gerçeğe aykırı tasdikte YMM hangi sınır ve biçimde sorumlu olur?", "Tasdik kapsamıyla sınırlı müşterek ve müteselsil sorumluluk", ["Bütün mükellefler için sınırsız tek başına sorumluluk", "Yalnız disiplin uyarısı", "Sadece ücret iadesi", "Hiçbir mali sorumluluk bulunmaması"], "YMM, tasdik kapsamıyla sınırlı olarak ziyaa uğratılan vergi ve cezalardan mükellefle müştereken ve müteselsilen sorumludur.", "3568 sayılı Kanun m. 12", "hard"),
    r("YMM hakkında tasdik sorumluluk raporu düzenlenmeden önce kendisinden açıklama alınmamıştır. Usul bakımından eksik olan nedir?", "YMM hakkında sorumluluk raporu yazılabilmesi için hangi güvence sağlanır?", "Yazılı savunmasının istenmesi", ["Ruhsatının savunmasız iptal edilmesi", "Müşterinin tek başına karar vermesi", "Savunma hakkının peşinen kaldırılması", "Yalnız sözlü söylentiye dayanılması"], "Sorumluluk raporu yazılmadan önce YMM'nin yazılı savunması istenir.", "3568 sayılı Kanun m. 12", "hard"),
    r("Mesleği yapması yasaklanmış kişi bir SMMM bürosunda mesleki işlerde çalıştırılmak istenmektedir. Bu mümkün müdür?", "Meslek mensubu, mesleği yapması yasaklananlarla mesleki işbirliği kurabilir mi?", "Hayır; çalıştıramaz ve işbirliği yapamaz", ["Evet; her durumda çalıştırabilir", "Yalnız müşteri onayıyla çalıştırabilir", "Sadece ücretsiz çalıştırabilir", "Oda kaydı olmadan ortak yapabilir"], "Meslek mensupları, mesleği yapması yasaklananları bürolarında çalıştıramaz ve onlarla mesleki işbirliği yapamaz.", "3568 sayılı Kanun m. 13", "medium"),
    r("Birden çok SMMM faaliyetlerini ortaklık bürosunda birleştirmiştir. Bu faaliyetin kanuni niteliği nedir?", "SMMM veya YMM ortaklık bürosunda yürütülen mesleki faaliyet ticari faaliyet sayılır mı?", "Mesleki ortaklık mümkündür ve faaliyet ticari sayılmaz", ["Ortak çalışma kesinlikle yasaktır", "Faaliyet otomatik anonim şirket ticaretidir", "Ruhsatlar kendiliğinden iptal olur", "Yalnız YMM ile SMMM karışık büro kurabilir"], "Aynı unvandaki meslek mensupları ortaklık bürosu veya şirket kurabilir; bu bürolardaki mesleki faaliyet ticari faaliyet sayılmaz.", "3568 sayılı Kanun m. 45", "medium", focus_correct="Hayır; kanundaki ortaklık faaliyeti ticari sayılmaz"),
    r("Meslek şirketinde hatalı işi belirli bir meslek mensubu yapmıştır. Cezai sorumluluğun aidiyeti bakımından kural nedir?", "Şirket biçiminde mesleki çalışmada işten doğan cezai sorumluluk kime aittir?", "İşi yapan meslek mensubuna", ["Hiç kimseye", "Yalnız bütün müşterilere", "Sadece oda başkanına", "Her durumda stajyere"], "Meslek şirketinde yapılan işten doğan cezai sorumluluk, işi yapan meslek mensubuna aittir.", "3568 sayılı Kanun m. 45", "hard"),
]


PREMISES = [
    {"stem":"Meslek unvanları bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kanunda SMMM ve YMM unvanları düzenlenir\n\nII. Ruhsatsız kişi benzer unvanı serbestçe kullanabilir\n\nIII. Haksız unvan kullanımını öğrenen oda savcılığa bildirir","correct":"I ve III","why":"Unvanlar SMMM ve YMM'dir; benzer ibareler de korunur ve oda aykırılığı savcılığa bildirir.","ref":"3568 sayılı Kanun m. 1 ve 3","difficulty":"medium"},
    {"stem":"SMMM meslek konusu bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Defter ve beyanname düzenleyebilir\n\nII. Muhasebe sistemi kurup danışmanlık yapabilir\n\nIII. Belgelere dayalı inceleme ve raporlama yapabilir","correct":"I, II ve III","why":"Üç faaliyet de Kanunun m. 2/A hükmünde SMMM meslek konusu olarak sayılmıştır.","ref":"3568 sayılı Kanun m. 2/A","difficulty":"easy"},
    {"stem":"YMM görev alanı bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Tasdik işi yapabilir\n\nII. Müşterinin muhasebe defterini tutabilir\n\nIII. Muhasebe bürosuna ortak olabilir","correct":"Yalnız I","why":"YMM tasdik yapabilir; defter tutamaz, muhasebe bürosu açamaz veya bu büroya ortak olamaz.","ref":"3568 sayılı Kanun m. 2/B ve 12","difficulty":"medium"},
    {"stem":"YMM yemini bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Fiilen göreve başlamadan önce edilir\n\nII. Asliye Ticaret Mahkemesinde yapılır\n\nIII. Bağımsızlık ve dürüstlük yeminin unsurlarıdır","correct":"I, II ve III","why":"Yemin zamanı, mercii ve metindeki mesleki değerler Kanunun m. 11 hükmünde düzenlenmiştir.","ref":"3568 sayılı Kanun m. 11","difficulty":"easy"},
    {"stem":"Tasdik işlemi bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Uygunluk denetim standartlarına göre incelenir\n\nII. Tasdik kapsamı raporda belirtilmez\n\nIII. Kamu idaresinin inceleme yetkileri saklıdır","correct":"I ve III","why":"Tasdik uygunluk incelemesine dayanır ve kapsam raporda açıklanır; kamu inceleme yetkileri saklıdır.","ref":"3568 sayılı Kanun m. 12","difficulty":"hard"},
    {"stem":"Tasdik sorumluluğu bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. YMM tasdikin doğruluğundan sorumlu değildir\n\nII. Mali sorumluluk tasdik kapsamıyla sınırlıdır\n\nIII. Sorumluluk raporu savunma istenmeden yazılır","correct":"Yalnız II","why":"YMM tasdikin doğruluğundan sorumludur ve sorumluluk raporundan önce savunması istenir; yalnız II doğrudur.","ref":"3568 sayılı Kanun m. 12","difficulty":"hard"},
    {"stem":"Mesleki ortaklık bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Meslek mensupları ortaklık bürosu kurabilir\n\nII. Büro faaliyeti her durumda ticari faaliyet sayılır\n\nIII. Şirkette cezai sorumluluk işi yapan meslek mensubuna aittir","correct":"I ve III","why":"Mesleki ortaklık mümkündür ve ticari sayılmaz; cezai sorumluluk işi yapana aittir.","ref":"3568 sayılı Kanun m. 45","difficulty":"hard"},
    {"stem":"Meslek sınırları bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. SMMM'nin tasdik yetkisi YMM ile aynıdır\n\nII. YMM sistem kurma ve raporlama işi yapabilir\n\nIII. YMM muhasebe defteri tutamaz","correct":"II ve III","why":"Tasdik YMM'ye özgüdür; YMM sistem-müşavirlik ve raporlama işlerini yapabilir, defter tutamaz.","ref":"3568 sayılı Kanun m. 2","difficulty":"medium"},
]


if __name__ == "__main__":
    write_topic(
        lesson_id="meslek_hukuku", topic_id="meslek_ve_unvanlar",
        label="Meslek ve Unvanlar", slug="meslek_ve_unvanlar",
        prefix="topic-mh-mu", seed=170741,
        legislation_version="3568 sayılı Kanun, 17.07.2026 tarihinde yürürlükteki metin",
        rules=RULES, premises=PREMISES, wrong_banks={},
    )
