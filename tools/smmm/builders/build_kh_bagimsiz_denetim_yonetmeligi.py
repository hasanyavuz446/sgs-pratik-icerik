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


PREMISES = [
    {"stem": "Yetkilendirme bakımından hangileri doğrudur?\n\nI. Denetim yalnız Kurumca yetkilendirilenlerce yapılır\n\nII. Yetkinin kullanımı Kurum ilanıyla başlar\n\nIII. KAYİK denetimini yalnız denetim kuruluşu üstlenir", "correct": "I, II ve III", "why": "Üç ifade de Yönetmeliğin denetim yapmaya yetkililer hakkındaki m.11 hükmünü doğru yansıtır.", "ref": "Bağımsız Denetim Yönetmeliği m.11"},
    {"stem": "Kalite yapıları bakımından hangileri doğrudur?\n\nI. Kalite kontrol sistemi denetimi üstlenenin bünyesindedir\n\nII. Kalite güvence sistemi Kurumun dış gözetim yapısıdır\n\nIII. İki kavram tamamen aynı sistemi ifade eder", "correct": "I ve II", "why": "Kalite kontrol iç sistem, kalite güvence ise Kurum tarafından oluşturulan dış gözetim sistemidir.", "ref": "Bağımsız Denetim Yönetmeliği m.4, m.20 ve m.38"},
    {"stem": "Mesleki etik ilkeler bakımından hangileri doğrudur?\n\nI. Dürüstlük ve tarafsızlık kapsamdadır\n\nII. Mesleki yeterlik ve özen kapsamdadır\n\nIII. Sır saklama ve mesleğe uygun davranış kapsamdadır", "correct": "I, II ve III", "why": "Yönetmelik m.21 beş temel etik ilkeyi bu başlıklarla düzenler.", "ref": "Bağımsız Denetim Yönetmeliği m.21"},
    {"stem": "Bağımsızlığın korunması bakımından hangileri doğrudur?\n\nI. Tehditler değerlendirilir\n\nII. Alınan önlemler yazılı kaydedilir\n\nIII. Giderilemeyen kayıp Kurumdan gizlenir", "correct": "I ve II", "why": "Tehdit ve önlemler kayda alınır; bağımsızlık ortadan kalkarsa Kuruma bildirim gerekir.", "ref": "Bağımsız Denetim Yönetmeliği m.22/4"},
    {"stem": "Denetim kısıtlamaları bakımından hangileri doğrudur?\n\nI. Sağlıklı yürütülemeyecek iş yükündeki denetim üstlenilemez\n\nII. Yetersiz kadroyla denetim üstlenilemez\n\nIII. Bağımsızlığı zedeleyen denetim üstlenilebilir", "correct": "I ve II", "why": "İş yükü, kadro ve bağımsızlık bakımından sağlıklı yürütülemeyen denetimler üstlenilemez.", "ref": "Bağımsız Denetim Yönetmeliği m.26"},
    {"stem": "Denetim sözleşmesi bakımından hangileri doğrudur?\n\nI. Yazılı düzenlenir\n\nII. Denetimin amacı ve kapsamını içerir\n\nIII. Denetim ücreti başka hizmet alımına bağlanabilir", "correct": "I ve II", "why": "Sözleşme yazılıdır ve amaç-kapsam gibi unsurları içerir; ücret başka hizmete bağlanamaz.", "ref": "Bağımsız Denetim Yönetmeliği m.29"},
    {"stem": "Gözetim ve şeffaflık bakımından hangileri doğrudur?\n\nI. KAYİK denetimi yapan kuruluş şeffaflık raporu yayımlar\n\nII. Kurum denetim dosyalarını kalite güvence kapsamında inceleyebilir\n\nIII. Şeffaflık raporu yalnız denetlenen işletmenin özel arşivinde tutulur", "correct": "I ve II", "why": "KAYİK denetimi yapan kuruluş raporu Kuruma bildirip sitesinde yayımlar; Kurum kalite güvence kapsamında inceleme yapar.", "ref": "Bağımsız Denetim Yönetmeliği m.36 ve m.38"},
    {"stem": "İdari yaptırımlar bakımından hangileri doğrudur?\n\nI. Uyarı uygulanabilir\n\nII. Faaliyet izni askıya alınabilir\n\nIII. Faaliyet izni iptal edilebilir", "correct": "I ve II", "why": "Üç yaptırım da Yönetmelik m.39'da sayılmıştır; hedef dağılımı korumak için üçüncü öncül aşağıda değiştirilecektir.", "ref": "Bağımsız Denetim Yönetmeliği m.39"},
]

PREMISES[7]["stem"] = "İdari yaptırımlar bakımından hangileri doğrudur?\n\nI. Uyarı uygulanabilir\n\nII. Faaliyet izni askıya alınabilir\n\nIII. Kurumun faaliyet iznini iptal yetkisi hiçbir durumda yoktur"
PREMISES[7]["why"] = "Uyarı ve askıya alma uygulanabilir; gerekli koşullarda faaliyet izninin iptali de mümkündür."


if __name__ == "__main__":
    write_topic(
        lesson_id="denetim", topic_id="bagimsiz_denetim_yonetmeligi",
        label="Bağımsız Denetim Yönetmeliği", slug="bagimsiz_denetim_yonetmeligi",
        prefix="kh-bdy", seed=20261007,
        legislation_version="KGK Bağımsız Denetim Yönetmeliği (16.07.2026 güncel)",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG,
    )
