#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KGK Bağımsız Denetim Yönetmeliği — 60 özgün konu havuzu sorusu."""
from topic_pack_builder import write_topic


def R(scenario, focus, correct, bank, why, ref, difficulty="medium"):
    return locals()


WRONG = {
    "yetki": [
        "Bağımsız denetim yetkisi ticaret siciline kayıtla kendiliğinden doğar ve Kurumun yetkilendirme veya ilan işlemi aranmaz",
        "KAYİK denetimleri herhangi bir meslek mensubunca kendi adına üstlenilebilir; denetim kuruluşu şartı bulunmaz",
        "Denetim kuruluşunun adi ortaklık olması yeterlidir ve sermaye şirketi biçiminde kurulmasına gerek yoktur",
        "Denetim kuruluşunun ortaklarının meslek mensubu olması yasaktır; bütün payların denetlenen işletmeye ait olması gerekir",
        "Bağımsız denetçi belgesi, 3568 sayılı Kanuna göre meslek mensubu olmayan herkese yalnız deneyim beyanıyla verilir",
        "Resmî sicil denetlenen işletmelerce kâğıt ortamında tutulur ve Kurum kayıtlarıyla hiçbir bağlantısı bulunmaz",
        "Denetim kuruluşunun sorumlu denetçi bulundurmasına gerek yoktur; raporu denetlenen işletmenin yönetimi imzalar",
        "Kurum belirli alanlar için ek şart getiremez ve yetkilendirilmiş kuruluşların listesini kamuya ilan edemez",
    ],
    "kalite": [
        "Kalite kontrol sistemi yalnız Kurumun dış incelemesinden ibarettir; denetimi üstlenen bünyesinde yazılı süreç oluşturmaz",
        "Kalite güvence sistemi denetim kuruluşunun kendi iç sistemi olup Kurumun inceleme ve gözetim rolü bulunmaz",
        "Mesleki etik yalnız sır saklama ilkesinden oluşur; dürüstlük, tarafsızlık ve mesleki özen kapsam dışıdır",
        "Bağımsızlık yalnız denetçinin kendi kanaatine göre değerlendirilir; makul üçüncü kişinin algısı önem taşımaz",
        "Bağımsızlık tehdidi doğduğunda önlem almak, değerlendirmeyi yazılı kayda geçirmek veya Kuruma bildirmek yasaktır",
        "Denetçi denetlenen işletmenin karar alma mekanizmasına katılarak yönetim kararlarını onaylamak zorundadır",
        "Sürekli eğitim yükümlülüğü sicile tescilden önce başlar ve yetki sona erince geçmiş dönemler için yeniden uygulanır",
        "Her denetim öncesi bağımsızlık ve sır saklama taahhüdü alınması mümkün değildir; yalnız sözlü beyan yeterlidir",
    ],
    "kisit": [
        "Denetim kuruluşu aynı işletmeyi kesintisiz ve süresiz denetleyebilir; rotasyon veya bekleme dönemi bulunmaz",
        "Denetçi aynı anda sınırsız sayıda denetim kuruluşu adına görev yapabilir ve kuruluşların tümüne ortak olabilir",
        "Denetimden ayrılan kişi ertesi gün son denetlediği işletmede kilit yönetici olabilir; soğuma süresi uygulanmaz",
        "Denetim ekibi tek kişiden oluşabilir ve sorumlu denetçi ile diğer kademeler için yedek belirlenmesi yasaktır",
        "Denetim kuruluşu, bağımsızlığı zedelese bile denetlenen işletmeye her türlü yönetim ve danışmanlık hizmetini verebilir",
        "Sonuca bağlı denetim ücreti bağımsızlığı güçlendirdiği için sözleşmede zorunlu olarak yer almalıdır",
        "Reklamda kesin olumlu görüş vaat edilmesi ve diğer denetçilerle üstünlük karşılaştırması yapılması serbesttir",
        "Mevcut iş yükü denetimin sağlıklı yürütülmesini engellese bile kuruluş yeni denetimi kabul etmek zorundadır",
    ],
    "yukum": [
        "Denetim sözleşmesi sözlü yapılabilir ve amaç, kapsam, ekip, ücret veya teslim tarihi içermesine gerek yoktur",
        "Denetim sözleşmesinde denetim hizmeti dışında her türlü hizmet aynı bedelin koşulu olarak bağlanabilir",
        "Mesleki sorumluluk sigortası yalnız son denetim tamamlandıktan sonra isteğe bağlı olarak yaptırılabilir",
        "Denetim dosyaları rapor teslim edilir edilmez imha edilir; belge ve kayıtlar için saklama yükümlülüğü bulunmaz",
        "Kurumun talep ettiği bilgi ve belgeler sır gerekçesiyle hiçbir durumda ibraz edilmez ve inceleme ortamı sağlanmaz",
        "Şeffaflık raporunu yalnız KAYİK denetimi yapmayan işletme yönetimleri hazırlar; denetim kuruluşunun görevi yoktur",
        "Kurum inceleme yapamaz; denetim dosyalarının kalite ve mevzuat yönünden gözetimi yalnız denetlenen işletmeye aittir",
        "Mevzuata aykırılığın niteliğine bakılmadan uygulanabilecek tek yaptırım sözlü tavsiyedir; izin askısı ve iptali yoktur",
    ],
}

# Doğru cevap uzunluğunun sistematik ipucu olmaması için her kazanım
# bankasında kısa, orta ve uzun yanlış önermeler birlikte tutulur.
WRONG["yetki"].extend([
    "Yetki noter onayıyla başlar",
    "Tescil yetki için yeterlidir",
    "KAYİK'i her meslek mensubu denetler",
    "Adi ortaklık kuruluş olabilir",
    "Bütün paylar hamiline yazılı olabilir",
    "Ortakların meslek mensubu olması yasaktır",
    "Pay veya hisselerin yarısı hamiline yazılı olabilir",
    "Payların yalnız bir kısmının nama yazılı olması yeterlidir",
    "Ortakların yalnız yarısının meslek mensubu olması yeterlidir",
    "Ortakların tacir olması yeterli olup meslek ruhsatı aranmaz",
    "Kurumun ilanı gerekmeden yalnız şirket kuruluş sözleşmesiyle bağımsız denetim yetkisi kazanılır ve sınırsız biçimde kullanılır",
    "KAYİK denetimi, Kurumca denetim kuruluşu olarak yetkilendirilmemiş herhangi bir SMMM veya YMM tarafından kişisel unvanla üstlenilebilir",
])
WRONG["kalite"].extend([
    "Yalnız sözlü politika yeterlidir",
    "Bağımsızlığın tek boyutu vardır",
    "Etik ilkeler yalnız sır saklamadır",
    "Kurum kalite incelemesi yapamaz",
    "Taahhüt yalnız ilk yetkilendirmede alınır",
    "Sürekli eğitim tescille aynı gün başlar",
    "Yalnız ticari başarı ve müşteri memnuniyeti",
    "Tarafsızlık yerine yönetimin talimatına bağlılık",
    "Mesleki şüphecilik yerine kesin sonuç garantisi",
    "Yalnız sır saklama ve reklam serbestisi",
    "Kalite kontrol politikalarının Kurum düzenlemelerine aykırı olması hâlinde farklılık açıklanmaz ve eski uygulama aynen sürdürülür",
    "Makul ve bilgi sahibi üçüncü kişinin algısı bağımsızlık değerlendirmesinde hiçbir önem taşımaz; yalnız denetçinin öznel kanaati esas alınır",
])
WRONG["kisit"].extend([
    "Rotasyon süresi bir yıldır",
    "Denetim ekibi tek kişi olabilir",
    "Sonuca bağlı ücret zorunludur",
    "Denetçi iki kuruluşta çalışabilir",
    "Uzmanlar asgari denetçi sayısına eklenir",
    "Soğuma süresi hiçbir denetçiye uygulanmaz",
    "Aynı denetim ağı içindeki kuruluşların bir işletmede geçirdiği süreler rotasyon hesabında ayrı ayrı değerlendirilir ve birleştirilmez",
    "Denetim ekibindeki teknik uzmanlar karar verici olabilir, asgari üç denetçi hesabına dâhil edilir ve yedek denetçi belirlenmesi gerekmez",
])
WRONG["yukum"].extend([
    "Sözlü sözleşme yeterlidir",
    "Dosyalar iki yıl saklanır",
    "Sigorta ilk işte aranmaz",
    "Bildirimler sınırsız sürelidir",
    "Şeffaflık raporu gizli tutulur",
    "Kurumun belge isteme yetkisi yoktur",
    "Denetim sözleşmesi seçimden sonra süre sınırı olmaksızın yapılabilir ve sözleşme kurulmadan denetime devam edilmesi Kuruma bildirilmez",
    "KAYİK denetimi yapan kuruluş şeffaflık raporunu yalnız kendi arşivinde saklar; Kuruma bildirme ve internet sitesinde yayımlama yükümlülüğü yoktur",
])


RULES = [
    R("Bir meslek mensubu Kurumca yetkilendirilmeden bağımsız denetim raporu imzalamak istemektedir. Bu mümkün müdür?", "Bağımsız denetim yapmaya yetkili kişileri belirleyen temel kural hangisidir?", "Denetim yalnız Kurumca yetkilendirilenlerce yapılır", "yetki", "Bağımsız denetim sadece Kurumca yetkilendirilen denetim kuruluşları veya denetçiler tarafından yetkileri çerçevesinde yapılır.", "Bağımsız Denetim Yönetmeliği m.11/1", "easy"),
    R("Bir kamu yararını ilgilendiren kuruluşun bağımsız denetimi üstlenilecektir. Hangi yapı yetkilidir?", "KAYİK denetimlerinin üstlenilmesine ilişkin özel kural hangisidir?", "Yalnız yetkili denetim kuruluşu üstlenebilir", "yetki", "KAYİK'lerin ve Kurumca belirlenen işletmelerin denetimi yalnız denetim kuruluşları tarafından üstlenilir.", "Bağımsız Denetim Yönetmeliği m.11/3"),
    R("Bağımsız denetim kuruluşu olarak yetki isteyen bir adi ortaklık başvurmuştur. Kuruluş türü koşulu nedir?", "Denetim kuruluşunun hukuki biçimi bakımından aranan temel şart hangisidir?", "Sermaye şirketi olması", "yetki", "Denetim kuruluşu olarak yetkilendirilecek yapının sermaye şirketi olması gerekir.", "Bağımsız Denetim Yönetmeliği m.13/1-a", "easy"),
    R("Denetim kuruluşunda sermaye ve oy haklarının çoğunluğu denetçi olmayan kişilere bırakılmıştır. Yetkilendirme koşulu nedir?", "Denetim kuruluşunun sermaye, oy ve ortaklık yapısına ilişkin koşul hangisidir?", "Sermaye ve oyların yarıdan fazlası denetçilere ait olmalıdır", "yetki", "Sermaye ve oy haklarının yarısından fazlası kuruluşun denetçilerine ait; ortakların tamamı meslek mensubu olmalıdır.", "Bağımsız Denetim Yönetmeliği m.13/1-e"),
    R("Bağımsız denetçi olmak isteyen kişi meslek mensubu değildir ancak yalnız şirketlerde çalışmıştır. Temel koşul bakımından sonuç nedir?", "Bağımsız denetçi yetkilendirmesinde 3568 bağlantılı temel mesleki koşul hangisidir?", "SMMM veya YMM ruhsatlı meslek mensubu olmak", "yetki", "Bağımsız denetçi, 3568 sayılı Kanuna göre SMMM veya YMM ruhsatı almış meslek mensupları arasından yetkilendirilir.", "Bağımsız Denetim Yönetmeliği m.4/a ve m.14/1-b"),
    R("Denetçi ve denetim kuruluşlarına ait resmî kayıtlar elektronik ortamda izlenmektedir. Bu kayıt sistemi hangisidir?", "Kurum tarafından elektronik ortamda tutulan resmî kayıt yapısı hangisidir?", "Bağımsız Denetim Resmî Sicili", "yetki", "Resmî sicil, denetim kuruluşları ve denetçilerin kayıtlarının Kurumca elektronik ortamda izlendiği yapıdır.", "Bağımsız Denetim Yönetmeliği m.4/d ve m.17-18", "easy"),
    R("Denetim kuruluşu, faaliyetlerini yönetmek için Kurum düzenlemelerine uygun yazılı politika ve süreçler oluşturmaktadır. Bu sistem hangisidir?", "Denetimi üstlenenin kendi bünyesinde oluşturduğu yazılı kalite sistemi hangisidir?", "Kalite kontrol sistemi", "kalite", "Kalite kontrol sistemi, denetim kuruluşu veya denetim üstlenen bağımsız denetçinin kendi bünyesinde oluşturduğu yazılı politika ve süreçlerdir.", "Bağımsız Denetim Yönetmeliği m.4/j ve m.20"),
    R("Kurum, denetim çalışmalarının standartlara uygunluğunu dış gözetim kapsamında incelemektedir. Bu yapı hangisidir?", "Kurum tarafından kamu güvenini sağlamak amacıyla oluşturulan dış sistem hangisidir?", "Kalite güvence sistemi", "kalite", "Kalite güvence sistemi, denetim kalitesi ve kamu güveni için Kurum tarafından oluşturulan gözetim sistemidir.", "Bağımsız Denetim Yönetmeliği m.4/i ve m.38"),
    R("Denetçi çıkar çatışmasının muhakemesini etkilemesine izin vermemiş ve bilgileri yetkisiz açıklamamıştır. Hangi yükümlülük grubuna uymuştur?", "Dürüstlük, tarafsızlık, yeterlik ve özen, sır saklama ile mesleğe uygun davranış hangi gruptur?", "Mesleki etik ilkeler", "kalite", "Yönetmelik bu beş temel etik ilkeye uyulmasını zorunlu kılar.", "Bağımsız Denetim Yönetmeliği m.21/1", "easy"),
    R("Denetim ekibinden bağımsızlık ve sır saklama politikalarına uyacağına ilişkin belge alınacaktır. Zamanlama kuralı nedir?", "Denetime katılanlardan yazılı etik taahhüdü alma sıklığı hangisidir?", "Her denetimden önce ve her hâlde yılda en az bir kez", "kalite", "Denetçiler ve katılanlardan her denetim öncesinde ve her hâlde yılda en az bir defa yazılı taahhüt alınır.", "Bağımsız Denetim Yönetmeliği m.21/2"),
    R("Denetçi tarafsız karar verse de makul üçüncü kişide bağımsızlıktan ödün verildiği izlenimini doğuran ilişki içindedir. Hangi boyut sorunludur?", "Makul ve bilgili üçüncü kişinin algısıyla değerlendirilen bağımsızlık boyutu hangisidir?", "Şekilde bağımsızlık", "kalite", "Şekilde bağımsızlık, makul ve bilgili üçüncü kişilerde dürüstlük ve tarafsızlıktan ödün verildiği izlenimini doğuracak durumlardan kaçınmayı gerektirir.", "Bağımsız Denetim Yönetmeliği m.22/1-b"),
    R("Denetçi mesleki muhakemesini etkileyen baskılardan uzak biçimde görüş oluşturmaktadır. Bu hangi bağımsızlık boyutudur?", "Mesleki muhakemenin olumsuz etkilerden arındırılmasını ifade eden bağımsızlık boyutu hangisidir?", "Esasta bağımsızlık", "kalite", "Esasta bağımsızlık, denetçinin dürüstlük, tarafsızlık ve şüphecilik içinde, muhakemesini bozan etkilerden uzak görüş açıklamasıdır.", "Bağımsız Denetim Yönetmeliği m.22/1-a"),
    R("Denetçi, denetlenen işletmenin yatırım kararını veren komiteye oy hakkıyla katılmaktadır. Yönetmeliğe uygun mudur?", "Denetçinin denetlenen işletmenin karar alma mekanizmasına katılması bakımından kural nedir?", "Karar alma mekanizmasına katılamaz", "kalite", "Denetim kuruluşu ve denetçiler denetlenen işletmenin karar alma mekanizmalarına hiçbir şekilde katılamaz.", "Bağımsız Denetim Yönetmeliği m.22/2"),
    R("Denetim sırasında bağımsızlık tehdidi belirlenmiştir. Önlemler tehdidi ortadan kaldırmaya yetmemektedir. Ne yapılır?", "Giderilemeyen bağımsızlık tehdidinde izlenecek temel süreç hangisidir?", "Tehdit kaydedilir, Kuruma bildirilir ve onayla sözleşme sonlandırılır", "kalite", "Tehditler ve önlemler yazılı kaydedilir; bağımsızlık ortadan kalkarsa Kuruma bildirilip onayla sözleşme sona erdirilir.", "Bağımsız Denetim Yönetmeliği m.22/4", "hard"),
    R("Denetim kuruluşu denetlediği işletmeye aynı ağ üzerinden yönetim danışmanlığı sunmak istemektedir. Genel kural nedir?", "Denetlenen işletmeye denetim dışı hizmet verilmesine ilişkin temel kısıtlama hangisidir?", "Tasdik ve vergi alanındaki sayılı istisnalar dışında verilemez", "kisit", "3568 kapsamındaki tasdik, vergi danışmanlığı ve vergi denetimi dışındaki danışmanlık veya başka hizmetler denetlenen işletmeye verilemez.", "Bağımsız Denetim Yönetmeliği m.22/5"),
    R("Denetim kuruluşu ilanında kesin olumlu görüş garantisi vermek ve rakipleriyle üstünlük karşılaştırması yapmak istemektedir. Sonuç nedir?", "Bağımsız denetim faaliyetinde reklam ve sonuç vaadi bakımından kural hangisidir?", "Reklam, sonuç vaadi ve karşılaştırma yasaktır", "kisit", "Doğrudan veya dolaylı reklam yapılamaz; tanıtıcı faaliyette sonuç vaadi ve diğer denetçilerle karşılaştırma yapılamaz.", "Bağımsız Denetim Yönetmeliği m.23"),
    R("Denetçi 2024 yılında sicile tescil edilmiştir. Sürekli eğitim yükümlülüğü hangi dönemde başlar?", "Sürekli eğitim yükümlülüğünün başlangıç kuralı hangisidir?", "Tescili izleyen ikinci takvim yılının başı", "kalite", "Sürekli eğitim yükümlülüğü denetçinin sicile tescil edildiği tarihi izleyen ikinci takvim yılının başında başlar.", "Bağımsız Denetim Yönetmeliği m.25/2"),
    R("Bir denetim kuruluşu aynı işletmede son on yılda yedi yıl denetim yürütmüştür. Yeniden üstlenme için hangi kural uygulanır?", "Denetim kuruluşunun işletme bazındaki rotasyon kuralı hangisidir?", "Üç yıl geçmedikçe yeniden denetim üstlenemez", "kisit", "Denetim kuruluşu son on yılda yedi yıl denetlediği işletmeyi üç yıl geçmedikçe yeniden denetleyemez.", "Bağımsız Denetim Yönetmeliği m.26/1-ç", "hard"),
    R("Bir denetçi aynı işletmede son yedi yılda beş yıl çalışmıştır. Yeniden bu işletmenin denetimine katılabilmesi için ne gerekir?", "Denetçiler için işletme bazındaki rotasyon kuralı hangisidir?", "Üç yıllık ara verilmesi", "kisit", "Denetçi son yedi yılda beş yıl denetim yürüttüğü işletmede üç yıl geçmedikçe yeniden denetim yapamaz.", "Bağımsız Denetim Yönetmeliği m.26/1-ç", "hard"),
    R("Denetçi görevden ayrıldıktan hemen sonra son iki yılda denetlediği işletmede finans direktörü olmak istemektedir. Kısıtlama nedir?", "Denetçinin eski müşteride kilit yönetici olmasına ilişkin soğuma süresi kaç yıldır?", "İki yıl", "kisit", "Denetçi görevden ayrılmasından itibaren iki yıl geçmedikçe son iki yılda denetlediği işletmede ve bağlı ortaklığında kilit yönetici olamaz.", "Bağımsız Denetim Yönetmeliği m.26/3"),
    R("Denetçi iki farklı denetim kuruluşu adına aynı dönemde denetim yapmak istemektedir. Yönetmelik ne öngörür?", "Denetçinin kuruluş bağlantısına ilişkin temel kısıtlama hangisidir?", "Yalnız bir kuruluş veya denetim üstlenen adına çalışabilir", "kisit", "Denetçiler yalnız bir denetim kuruluşu veya denetim üstlenen bağımsız denetçi adına denetim yapabilir.", "Bağımsız Denetim Yönetmeliği m.26/4"),
    R("Denetim ekibi iki denetçiden kurulmuş ve hiçbir yedek belirlenmemiştir. Asgari ekip kuralı nedir?", "Bağımsız denetim ekibinin asgari yapısı hangisidir?", "En az üç denetçi ve gerekli kademeler için yedek", "kisit", "Denetim ekibi en az üç denetçiden oluşur; sorumlu denetçi ve belirlenen diğer kademeler için en az birer yedek belirlenir.", "Bağımsız Denetim Yönetmeliği m.27/1"),
    R("Denetlenen işletme ile denetimi üstlenen arasında yalnız sözlü mutabakat vardır. Yönetmelik hangi şekli arar?", "Denetim sözleşmesinin geçerlilik ve ispat bakımından zorunlu şekli hangisidir?", "Yazılı denetim sözleşmesi", "yukum", "Denetim sözleşmesi yazılı düzenlenmeli; amaç, kapsam, kıstas, sorumluluk, ekip, ücret ve tarihler gibi asgari unsurları içermelidir.", "Bağımsız Denetim Yönetmeliği m.29/1"),
    R("Denetim sözleşmesinde danışmanlık hizmeti alınması, denetim ücretinin ödenmesi için koşul yapılmıştır. Bu mümkün müdür?", "Denetim sözleşmesinde başka hizmet ve ücrete ilişkin kısıtlama hangisidir?", "Başka hizmet öngörülemez ve ücret başka şarta bağlanamaz", "yukum", "Sözleşmede denetim dışı hizmet öngörülemez; denetim ücretinin ödenmesi başka bir hizmet koşuluna bağlanamaz.", "Bağımsız Denetim Yönetmeliği m.29/2"),
    R("Denetim kuruluşu ilk denetim işini üstlenmiştir ancak mesleki sorumluluk sigortası yaptırmamıştır. Yükümlülük ne zaman başlar?", "Mesleki sorumluluk sigortasının kapsam ve başlangıç kuralı hangisidir?", "İlk denetim işiyle başlar ve tüm denetimleri kapsar", "yukum", "Denetim kuruluşu ve denetim üstlenen bağımsız denetçi, ilk işten itibaren tüm denetimleri kapsayan mesleki sorumluluk sigortası yaptırır.", "Bağımsız Denetim Yönetmeliği m.33"),
    R("Denetim kuruluşu tamamlanan dosyaları iki yıl sonra imha etmek istemektedir. Saklama süresi nedir?", "Denetim çalışmaları ve kalite kontrol belgelerinin saklama yükümlülüğü kaç yıldır?", "On yıl", "yukum", "Ticari defterler, raporlar, denetim çalışmaları ve kalite kontrol sistemine ilişkin belgeler ekleriyle on yıl saklanır.", "Bağımsız Denetim Yönetmeliği m.35/1"),
]


def F(correct, focus, focus_correct, focus_why, focus_ref=None, focus_difficulty=None):
    item = {
        "correct": correct,
        "focus": focus,
        "focus_correct": focus_correct,
        "focus_why": focus_why,
    }
    if focus_ref:
        item["focus_ref"] = focus_ref
    if focus_difficulty:
        item["focus_difficulty"] = focus_difficulty
    return item


VARIANTS = [
    F(
        "Hayır; bağımsız denetim yalnız Kurumca yetkilendirilenler tarafından yapılabilir",
        "Kurum tarafından yetkilendirilen denetim kuruluşu veya denetçi, bağımsız denetim yetkisini hangi olaydan sonra kullanmaya başlayabilir?",
        "Yetkilendirmenin Kurum tarafından ilan edilmesinden sonra",
        "Denetim kuruluşları ve denetçiler yetkilerini, yetkilendirmenin Kurum tarafından ilanıyla kullanmaya başlar.",
        "Bağımsız Denetim Yönetmeliği m.11/2",
        "easy",
    ),
    F(
        "KAYİK denetimini yalnız Kurumca yetkilendirilmiş bir denetim kuruluşu üstlenebilir",
        "KAYİK ve Kurumca ayrıca belirlenen işletmeler dışındaki işletmelerin bağımsız denetimini kim üstlenebilir?",
        "Denetim kuruluşu veya Kurumca onaylanan denetim üstlenen bağımsız denetçi",
        "KAYİK dışındaki işletmelerin denetimi, yetkileri çerçevesinde denetim kuruluşu ya da denetim üstlenen bağımsız denetçi tarafından üstlenilebilir.",
        "Bağımsız Denetim Yönetmeliği m.11/3",
        "hard",
    ),
    F(
        "Adi ortaklık uygun değildir; denetim kuruluşunun sermaye şirketi olması gerekir",
        "Denetim kuruluşu olarak yetkilendirilecek sermaye şirketinin pay veya hisseleri hangi biçimde olmalıdır?",
        "Pay veya hisselerin tamamı nama yazılı olmalıdır",
        "Yetkilendirme şartlarından biri şirket pay veya hisselerinin tamamının nama yazılı olmasıdır.",
        "Bağımsız Denetim Yönetmeliği m.13/1-b",
        "easy",
    ),
    F(
        "Sermaye ve oy haklarının yarısından fazlası kuruluşun denetçilerine ait olmalıdır",
        "Denetim kuruluşunun ortaklarının mesleki niteliğine ilişkin yetkilendirme şartı hangisidir?",
        "Ortakların tamamı meslek mensubu olmalıdır",
        "Sermaye ve oy çoğunluğunun denetçilere ait olması yanında ortakların tamamının 3568 kapsamında meslek mensubu olması gerekir.",
        "Bağımsız Denetim Yönetmeliği m.13/1-e",
    ),
    F(
        "Meslek mensubu olmadığı için yalnız şirket deneyimiyle bağımsız denetçi yetkisi alamaz",
        "Bağımsız denetçi yetkilendirmesinde meslek ruhsatına ek olarak aranan temel koşulların doğru özeti hangisidir?",
        "Uygun eğitim, Türkiye'de yerleşiklik, uygulamalı eğitim ve sınav başarısı",
        "Yönetmelik; uygun lisans veya lisansüstü eğitim, Türkiye'de yerleşiklik, uygulamalı mesleki eğitim ve denetçilik sınavı başarısı gibi koşulları birlikte arar.",
        "Bağımsız Denetim Yönetmeliği m.14/1",
        "hard",
    ),
    F(
        "Bu elektronik kayıt yapısı Bağımsız Denetim Resmî Sicilidir",
        "Ortak marka, kalite politikası, iş stratejisi veya önemli mesleki kaynakları paylaşmayı amaçlayan iş birliği yapısı nasıl adlandırılır?",
        "Bu iş birliği yapılanması denetim ağı olarak adlandırılır",
        "Hukuki bağ bulunmasa bile ortak marka, strateji, kalite politikası veya önemli kaynak paylaşımını amaçlayan yapılanma denetim ağıdır.",
        "Bağımsız Denetim Yönetmeliği m.4/e",
        "easy",
    ),
    F(
        "Kuruluş bünyesindeki yazılı politika ve süreçler kalite kontrol sistemini oluşturur",
        "Kalite kontrol politikaları ile Kurum düzenlemesi arasında farklılık oluşursa denetimi üstlenenin temel yükümlülüğü nedir?",
        "Farklılığı gerekçelendirmek, belgelemek ve uygulamanın Kurum düzenlemesine uyumunu göstermek",
        "Yazılı politika veya farklı uygulama Kurum düzenlemesinden ayrılıyorsa bu durum gerekçesiyle belgelenmeli ve uyumun nasıl sağlandığı gösterilmelidir.",
        "Bağımsız Denetim Yönetmeliği m.20/2",
        "hard",
    ),
    F(
        "Kurumun dış inceleme ve gözetim yapısı kalite güvence sistemidir",
        "Yönetmeliğe göre Kurumun olağan inceleme sıklığı KAYİK denetleyen kuruluşlar ile diğer denetim kuruluşlarında en az kaç yılda birdir?",
        "KAYİK denetleyenlerde üç, diğer denetim kuruluşlarında altı yılda bir",
        "Kurum KAYİK denetleyen kuruluşları asgari üç yılda bir, diğer denetim kuruluşlarını asgari altı yılda bir inceler.",
        "Bağımsız Denetim Yönetmeliği m.38/3",
        "hard",
    ),
    F(
        "Tarafsızlığı ve sır saklamayı koruyan davranış mesleki etik ilkelere uygundur",
        "Bağımsız Denetim Yönetmeliği'nde birlikte sayılan beş temel mesleki etik ilke hangileridir?",
        "Dürüstlük, tarafsızlık, mesleki yeterlik ve özen, sır saklama ve mesleğe uygun davranış",
        "M.21; dürüstlük, tarafsızlık, mesleki yeterlik ve özen, sır saklama ile mesleğe uygun davranışı temel etik ilkeler olarak sayar.",
        "Bağımsız Denetim Yönetmeliği m.21/1",
    ),
    F(
        "Yazılı taahhüt her denetimden önce ve her hâlde yılda en az bir kez alınmalıdır",
        "Denetime başladıktan sonra bağımsızlık, tarafsızlık veya sır saklamayı olumsuz etkileyebilecek bir husus ortaya çıkarsa ekip üyesi ne yapmalıdır?",
        "Durumu denetimi üstlenene yazılı olarak bildirmelidir",
        "Denetçiler ve denetime katılanlar, etik ilkeleri olumsuz etkileyebilecek yeni hususları denetim kuruluşuna veya denetimi üstlenene yazılı bildirir.",
        "Bağımsız Denetim Yönetmeliği m.21/2",
        "hard",
    ),
    F(
        "Makul ve bilgili üçüncü kişide oluşan bağımsızlık izlenimi şekilde bağımsızlığı etkiler",
        "Şekilde bağımsızlık değerlendirilirken olay ve ilişkiler kimin bakış açısından değerlendirilir?",
        "Konuya ilişkin gerçekleri değerlendiren makul ve bilgi sahibi üçüncü kişinin",
        "Şekilde bağımsızlık, tüm durum ve gerçekleri değerlendiren makul ve bilgi sahibi üçüncü kişinin algısını esas alır.",
        "Bağımsız Denetim Yönetmeliği m.22/1-b",
    ),
    F(
        "Mesleki muhakemeyi bozabilecek etkilerden uzak görüş oluşturmak esasta bağımsızlıktır",
        "Esasta bağımsızlık denetçinin hangi üç mesleki niteliği koruyarak görüş açıklamasını gerektirir?",
        "Dürüstlük, tarafsızlık ve mesleki şüphecilik",
        "Esasta bağımsızlık denetçinin dürüstlük, tarafsızlık ve mesleki şüphecilik içinde, olumsuz etkilerden uzak görüş açıklamasıdır.",
        "Bağımsız Denetim Yönetmeliği m.22/1-a",
    ),
    F(
        "Uygun değildir; denetçi denetlenen işletmenin karar alma mekanizmasına katılamaz",
        "Denetçi, denetlenen işletmenin muhasebe politikası seçimini işletme adına yapıp yönetim sorumluluğu üstlenebilir mi?",
        "Hayır; işletmenin karar ve yönetim sorumluluğunu üstlenemez",
        "Bağımsızlık, denetçinin denetlenen işletme adına karar almamasını ve yönetim sorumluluğu üstlenmemesini gerektirir.",
        "Bağımsız Denetim Yönetmeliği m.22/2",
        "hard",
    ),
    F(
        "Tehdit kaydedilip Kuruma bildirilir ve Kurum onayıyla denetim sözleşmesi sona erdirilir",
        "Bağımsızlığa yönelik tehditler ile bunları kabul edilebilir düzeye indirmek için alınan önlemler nasıl izlenmelidir?",
        "Değerlendirme ve önlemler yazılı olarak kayda alınmalıdır",
        "Bağımsızlık tehditleri, bunların değerlendirilmesi ve alınan önlemler denetim dosyasında yazılı biçimde kayıt altına alınır.",
        "Bağımsız Denetim Yönetmeliği m.22/4",
    ),
    F(
        "İzin verilen tasdik ve vergi hizmetleri dışındaki danışmanlık hizmeti denetlenen işletmeye verilemez",
        "Denetim ücretinin sonucu olumlu görüşe veya izin verilen başka bir hizmetin satın alınmasına bağlanması mümkün müdür?",
        "Hayır; ücret denetim sonucuna veya başka hizmete bağlanamaz",
        "Denetim ücreti bağımsızlık ve kaliteyi koruyacak şekilde belirlenir; denetim sonucuna veya başka hizmete bağlı olamaz.",
        "Bağımsız Denetim Yönetmeliği m.29/2 ve m.32",
        "hard",
    ),
    F(
        "Reklam, kesin denetim sonucu vaadi ve diğer denetçilerle üstünlük karşılaştırması yasaktır",
        "Başka bir denetimi üstlenenle hizmet ilişkisi devam eden işletmenin aynı döneme ait denetim talebi kural olarak kabul edilebilir mi?",
        "Hayır; Kurumun izin verdiği hâller dışında aynı dönem talebi kabul edilemez",
        "Haksız rekabet yasağı kapsamında, başka denetimi üstlenenle ilişkisi süren müşterinin aynı dönem talebi Kurumca izin verilmedikçe kabul edilemez.",
        "Bağımsız Denetim Yönetmeliği m.24/2",
        "hard",
    ),
    F(
        "Sürekli eğitim tescili izleyen ikinci takvim yılının başında başlar",
        "Sürekli eğitim yükümlülüğü başladıktan sonra denetçi hangi dönemler için Kurumun öngördüğü koşulları karşılamalıdır?",
        "Her yıl ile üçer yıllık dönemler için",
        "Denetçiler sürekli eğitim yükümlülüğünün başlamasından itibaren hem yıllık hem de üçer yıllık dönemler için belirlenen koşulları karşılar.",
        "Bağımsız Denetim Yönetmeliği m.25/3",
    ),
    F(
        "Son on yılda yedi yıl denetlenen işletme için üç yıl geçmeden kuruluş yeniden denetim üstlenemez",
        "Denetim kuruluşunun rotasyon süresi hesaplanırken aynı denetim ağındaki ve ilişkili kuruluşların çalışmalarına nasıl yaklaşılır?",
        "Aynı işletmedeki denetim süreleri topluca dikkate alınır",
        "Rotasyon hesabında aynı denetim ağında bulunan ve ilişkili denetim kuruluşlarının aynı işletmedeki süreleri birlikte değerlendirilir.",
        "Bağımsız Denetim Yönetmeliği m.26/2",
        "hard",
    ),
    F(
        "Son yedi yılda beş yıl denetime katılan denetçi aynı işletmeye üç yıllık aradan sonra dönebilir",
        "Bir denetçi farklı denetim kuruluşlarında çalışmışsa aynı işletmede geçirdiği süreler rotasyon hesabında nasıl ele alınır?",
        "Çalıştığı kuruluşlara bakılmaksızın sürelerin tamamı birlikte dikkate alınır",
        "Denetçinin aynı işletmede geçirdiği süreler, hangi denetim kuruluşunda çalıştığına bakılmaksızın rotasyon hesabında birleştirilir.",
        "Bağımsız Denetim Yönetmeliği m.26/2",
        "hard",
    ),
    F(
        "Denetçi ayrılışından sonra iki yıl geçmeden son iki yılda denetlediği işletmede kilit yönetici olamaz",
        "Denetçinin iki yıllık kilit yönetici olma yasağı yalnız denetlenen işletmeye mi uygulanır?",
        "Hayır; denetlenen işletmenin bağlı ortaklıklarını da kapsar",
        "Soğuma kuralı, son iki yılda denetlenen işletmenin yanı sıra onun bağlı ortaklıklarında kilit yönetici olmayı da kapsar.",
        "Bağımsız Denetim Yönetmeliği m.26/3",
        "hard",
    ),
    F(
        "Denetçi aynı dönemde yalnız bir denetim kuruluşu veya denetim üstlenen adına denetim yapabilir",
        "Denetçinin mevcut denetim kuruluşuyla ilişkisi sürerken başka bir denetim kuruluşuna ortak olması veya onun denetiminde görev alması mümkün müdür?",
        "Hayır; mevcut ilişkisi sona ermeden diğer kuruluşta ortak olamaz veya görev alamaz",
        "Denetçi mevcut kuruluşla ilişkisi sona ermedikçe başka kuruluşta ortak olamaz, denetim yapamaz veya onun üstlendiği denetimde görev alamaz.",
        "Bağımsız Denetim Yönetmeliği m.26/4",
        "hard",
    ),
    F(
        "Ekip en az üç denetçiden oluşmalı ve gerekli kademeler için nitelikli yedekler belirlenmelidir",
        "Denetim ekibindeki teknik uzmanlar ve denetçi yardımcıları asgari denetçi sayısı ile karar yetkisi bakımından nasıl değerlendirilir?",
        "Asgari sayıya dâhil edilmezler ve karar verici konumda bulunamazlar",
        "Uzmanlar ve yardımcı kişiler denetçi olarak görevlendirilmedikçe asgari denetçi sayısına katılmaz ve karar verici olamaz.",
        "Bağımsız Denetim Yönetmeliği m.27/3",
        "hard",
    ),
    F(
        "Denetlenen işletmeyle denetimi üstlenen arasında yazılı denetim sözleşmesi kurulmalıdır",
        "TTK uyarınca seçilen denetimi üstlenenle sözleşme seçimden itibaren kaç gün içinde yapılır; işletme ihtara rağmen kaçınırsa bildirim süresi nedir?",
        "Sözleşme 60 günde yapılır; kaçınma izleyen 10 gün içinde Kuruma bildirilir",
        "Denetim sözleşmesi seçimden itibaren en geç 60 günde yapılır; yazılı ihtara rağmen kaçınılırsa durum izleyen 10 günde Kuruma bildirilir.",
        "Bağımsız Denetim Yönetmeliği m.29/3",
        "hard",
    ),
    F(
        "Sözleşmede denetim dışı hizmet öngörülemez ve denetim ücreti başka hizmet koşuluna bağlanamaz",
        "Denetimi üstlenen denetim sözleşmesini hangi hâllerde feshedebilir ve feshi Kuruma ne kadar sürede bildirir?",
        "Haklı sebep veya görevden alma davasında feshedebilir; gerekçeyi 10 günde bildirir",
        "Denetimi üstlenen yalnız haklı sebep veya görevden alma davası hâlinde feshedebilir ve fesihle gerekçelerini 10 gün içinde Kuruma yazılı bildirir.",
        "Bağımsız Denetim Yönetmeliği m.29/4",
        "hard",
    ),
    F(
        "Mesleki sorumluluk sigortası ilk denetim işiyle başlar ve üstlenilen bütün denetimleri kapsar",
        "Mesleki sorumluluk sigortası poliçesinin düzenlenmesi veya poliçe ve sigorta şirketi değişikliği Kuruma ne kadar sürede bildirilir?",
        "İlgili tarihi takip eden günden itibaren en geç 30 gün içinde",
        "Poliçenin düzenlenme tarihi ile poliçe veya sigorta şirketindeki değişiklikler takip eden günden itibaren en geç 30 günde Kuruma bildirilir.",
        "Bağımsız Denetim Yönetmeliği m.34/1-ç",
        "hard",
    ),
    F(
        "Denetim ve kalite kontrol belgeleri ekleriyle birlikte on yıl süreyle saklanmalıdır",
        "Bir takvim yılında KAYİK denetimi yapan kuruluş yıllık şeffaflık raporunu ne zaman ve nasıl duyurur?",
        "İzleyen dördüncü ay sonuna kadar Kuruma bildirir ve internet sitesinde yayımlar",
        "KAYİK denetimi yapan kuruluş izleyen dördüncü ayın sonuna kadar raporu Kuruma bildirir ve kendi internet sitesinde yayımlar.",
        "Bağımsız Denetim Yönetmeliği m.36/1",
        "hard",
    ),
]

assert len(VARIANTS) == len(RULES) == 26
for rule, variant in zip(RULES, VARIANTS):
    rule.update(variant)


def length_balanced_distractors(correct, bank):
    """Doğru cevabın iki yanında ikişer uzunlukta çeldirici seçer."""
    shorter = sorted((x for x in bank if len(x) < len(correct)), key=len, reverse=True)
    longer = sorted((x for x in bank if len(x) > len(correct)), key=len)
    assert len(shorter) >= 2 and len(longer) >= 2, correct
    return shorter[:2] + longer[:2]


for rule in RULES:
    bank = WRONG[rule["bank"]]
    rule["scenario_distractors"] = length_balanced_distractors(rule["correct"], bank)
    rule["focus_distractors"] = length_balanced_distractors(rule["focus_correct"], bank)


PREMISES = [
    {"stem": "Yetkilendirme bakımından hangileri doğrudur?\n\nI. Denetim yalnız Kurumca yetkilendirilenlerce yapılır\n\nII. Yetkinin kullanımı Kurum ilanıyla başlar\n\nIII. KAYİK denetimini yalnız denetim kuruluşu üstlenir", "correct": "I, II ve III", "why": "Üç ifade de Yönetmeliğin denetim yapmaya yetkililer ve KAYİK denetimleri hakkındaki m.11 hükmünü doğru yansıtır.", "ref": "Bağımsız Denetim Yönetmeliği m.11"},
    {"stem": "Sorumlu denetçi koşulları bakımından hangileri doğrudur?\n\nI. KAYİK denetiminde on beş yıllık mesleki tecrübe aranır\n\nII. Bu sürenin en az üç yılında fiilen denetim tecrübesi bulunmalıdır\n\nIII. Koşulları taşıyan denetçi Kurum onayıyla görevlendirilir", "correct": "I, II ve III", "why": "KAYİK sorumlu denetçisinde on beş yıllık mesleki tecrübe, bunun en az üç yılında fiilî denetim ve Kurum onayı birlikte aranır.", "ref": "Bağımsız Denetim Yönetmeliği m.28/1-a"},
    {"stem": "Bağımsızlık bakımından hangileri doğrudur?\n\nI. Denetim esasen ve şeklen bağımsız yürütülür\n\nII. Makul ve bilgi sahibi üçüncü kişinin algısı şekilde bağımsızlıkta önemsizdir\n\nIII. Denetçi işletmenin karar alma mekanizmasına katılamaz", "correct": "I ve III", "why": "Denetim esasen ve şeklen bağımsızdır ve denetçi karar mekanizmasına katılamaz; üçüncü kişinin algısı şekilde bağımsızlıkta önemlidir.", "ref": "Bağımsız Denetim Yönetmeliği m.22/1-2"},
    {"stem": "Rotasyon ve denetim kısıtlamaları bakımından hangileri doğrudur?\n\nI. Kuruluş son on yılda altı yıl denetlediği işletmeye zorunlu olarak üç yıl ara verir\n\nII. Denetçi son yedi yılda beş yıl çalıştığı işletmede üç yıl geçmeden yeniden görev alamaz\n\nIII. Aynı denetim ağındaki kuruluşların süreleri birlikte dikkate alınır", "correct": "II ve III", "why": "Kuruluş için eşik son on yılda yedi yıldır; denetçi için beş yıl eşiği ve ağ sürelerinin toplu hesabı doğrudur.", "ref": "Bağımsız Denetim Yönetmeliği m.26/1-2"},
    {"stem": "Sözleşme ve raporlama bakımından hangileri doğrudur?\n\nI. TTK kapsamındaki sözleşme seçimden itibaren en geç altmış günde yapılır\n\nII. Denetim raporu olağan genel kuruldan en az yirmi gün önce yönetim organına teslim edilir\n\nIII. Yaygın kanıt yetersizliğinde olumsuz görüş verilir", "correct": "I ve II", "why": "İlk iki süre doğrudur; denetim konusunun geneline yayılan kanıt yetersizliği görüş vermekten kaçınmayı gerektirir.", "ref": "Bağımsız Denetim Yönetmeliği m.29/3 ve m.30/2-3"},
    {"stem": "Kuruma yapılacak bildirimler bakımından hangileri doğrudur?\n\nI. Daha önce bildirilmiş bilgilerdeki değişiklik otuz günde bildirilir\n\nII. Sigorta poliçesi değişikliği en geç otuz günde bildirilir\n\nIII. Son takvim yılı gelirleri haziran sonuna kadar bildirilir", "correct": "Yalnız II", "why": "Poliçe değişikliği otuz günde bildirilir; genel bilgi değişikliği on gündür ve son yıl gelirleri 15 Mayıs sonuna kadar bildirilir.", "ref": "Bağımsız Denetim Yönetmeliği m.34/1"},
    {"stem": "Şeffaflık ve Kurum incelemesi bakımından hangileri doğrudur?\n\nI. KAYİK denetimi yapan kuruluş raporu izleyen dördüncü ay sonuna kadar yayımlar\n\nII. Şeffaflık raporu yalnız bir yıl kamunun erişimine açık tutulur\n\nIII. KAYİK denetleyen kuruluşlar asgari üç yılda bir incelenir", "correct": "I ve III", "why": "Rapor izleyen dördüncü ay sonuna kadar yayımlanır ve KAYİK denetleyen kuruluş asgari üç yılda bir incelenir; rapor beş yıl erişime açık tutulur.", "ref": "Bağımsız Denetim Yönetmeliği m.36/1, m.36/5 ve m.38/3"},
    {"stem": "İdari yaptırımlar bakımından hangileri doğrudur?\n\nI. Mevzuata aykırılıkta uygulanabilecek tek yaptırım sözlü tavsiyedir\n\nII. Uyarı, faaliyet iznini askıya alma ve iptal yaptırımları uygulanabilir\n\nIII. Bu yaptırımlardan birine karar verilmesi ayrıca idari para cezasına engel olmaz", "correct": "II ve III", "why": "Yönetmelik uyarı, askıya alma ve iptali sayar; bunların uygulanması ayrıca idari para cezasına karar verilmesini engellemez.", "ref": "Bağımsız Denetim Yönetmeliği m.39"},
]


if __name__ == "__main__":
    write_topic(
        lesson_id="denetim", topic_id="bagimsiz_denetim_yonetmeligi",
        label="Bağımsız Denetim Yönetmeliği", slug="bagimsiz_denetim_yonetmeligi",
        prefix="kh-bdy", seed=20261007,
        legislation_version="KGK Bağımsız Denetim Yönetmeliği (17.07.2026 güncel metin)",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG,
    )
