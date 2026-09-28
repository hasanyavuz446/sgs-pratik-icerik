# -*- coding: utf-8 -*-
"""Muhasebe Denetimi · Bağımsız Denetim Yönetmeliği — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında denetim testinin yaklaşık yarısı bu Yönetmelikten gelir:
tanımlar, denetim kıstası, yetkilendirme, uygulamalı eğitim, sicil, etik ve bağımsızlık,
kısıtlamalar, ekipler, sözleşme, raporlama, bildirim, şeffaflık ve yaptırımlar.

Dayanak (28.09.2026 kontrolü, mevzuat.gov.tr güncel metin):
  · KGK Bağımsız Denetim Yönetmeliği (RG 26.12.2012/28509), 21.10.2014, 22.12.2015, 21.7.2017,
    23.11.2018, 11.1.2022, 17.12.2022 ve 15.6.2024 değişiklikleri işlenmiş
  · Danıştay iptalleri (m. 14/1-h, m. 14/5 ve m. 28/3'teki ibareler, m. 43/1) sorulmaz
Not: 2026/2 kitapçığı şeffaflık raporunun erişim süresini "dört yıl" kabul etmiştir; yürürlükteki
m. 36/5 beş yıl der, bu pakette güncel metin esas alınmıştır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_bagimsiz_denetim_yonetmeligi_2026.json", lesson="denetim",
          topic="bagimsiz_denetim_yonetmeligi", konu_adi="Bağımsız Denetim Yönetmeliği", seed=2026092841,
          surum="KGK Bağımsız Denetim Yönetmeliği, 15.6.2024 değişiklikleri dahil güncel metin; 28.09.2026 kontrolü")

B = "KGK Bağımsız Denetim Yönetmeliği’ne göre"

# ================================================================ tanımlar ve denetimin esasları (m. 4-10)
P.q("BDY m. 4/1-l",
    f"{B}, aşağıdakilerden hangisi Yönetmelikte doğrudan sayılan kamu yararını ilgilendiren kuruluşlar (KAYİK) arasında "
    "yer almaz?",
    "Serbest muhasebeci mali müşavirlerin kurduğu meslek şirketleri",
    ["Faktöring, finansman ve finansal kiralama şirketleri",
     "Sigorta, reasürans ve emeklilik şirketleri",
     "Varlık yönetim şirketleri ve emeklilik fonları",
     "6362 sayılı Kanunda tanımlanan ihraççılar ve sermaye piyasası kurumları"],
    "Yönetmelik m. 4/1-l'ye göre KAYİK'ler halka açık şirketler, bankalar, sigorta, reasürans ve emeklilik şirketleri, "
    "faktöring, finansman ve finansal kiralama şirketleri, varlık yönetim şirketleri, emeklilik fonları, 6362 sayılı "
    "Kanundaki ihraççılar ve sermaye piyasası kurumları ile Kurumca belirlenen diğer kuruluşlardır. Meslek şirketleri "
    "bu sayımda yer almaz.", zorluk="easy")

P.q("BDY m. 4/1-ş",
    "“Belirli bir bağımsız denetim faaliyetinin yürütülmesinden sorumlu tutulan ve bu denetime ait raporun denetimi "
    "üstlenenler adına imzalanmasına yetkili kılınan bağımsız denetçi” tanımı "
    f"{B} aşağıdakilerden hangisine aittir?",
    "Sorumlu denetçi",
    ["Başdenetçi", "Denetim üstlenen bağımsız denetçi", "Kıdemli denetçi", "Denetimin kalitesini gözden geçiren kişi"],
    "m. 4/1-ş sorumlu denetçiyi raporu denetimi üstlenenler adına imzalamaya yetkili bağımsız denetçi olarak tanımlar. "
    "Başdenetçi ve kıdemli denetçi m. 27/5'teki kıdem unvanlarıdır; denetim üstlenen bağımsız denetçi ise kendi adına "
    "denetim üstlenme onayı almış denetçidir.", zorluk="easy")

P.q("BDY m. 4/1-e",
    f"{B}, “denetim ağı” kavramına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetim ağı için kuruluşlar arasında hukuki bir ortaklık bağı bulunmalıdır.",
    ["Kâr veya maliyet paylaşımını hedefleyen işbirliği yapılanması denetim ağı oluşturabilir.",
     "Ortak kalite yönetim politikaları ve süreçleri kullanılması denetim ağının göstergelerindendir.",
     "Ortak bir marka veya unvan kullanımı denetim ağı tanımına girer.",
     "Mesleki kaynakların önemli bir kısmının ortaklaşa kullanılması da ağ ilişkisi doğurabilir."],
    "m. 4/1-e'ye göre denetim ağı, kuruluşlar arasında hukuki bir bağ olup olmadığına bakılmaksızın kâr veya maliyet "
    "paylaşımı, ortak mülkiyet, kontrol veya yönetim, ortak kalite yönetim politikaları, ortak iş stratejisi, ortak marka "
    "ya da mesleki kaynakların önemli kısmının ortak kullanımını amaçlayan işbirliği yapılanmasıdır.")

P.q("BDY m. 4/1-t",
    f"{B}, aşağıdakilerden hangisi Türkiye Denetim Standartları (TDS) kapsamında yer almaz?",
    "Büyük ve Orta Boy İşletmeler İçin Finansal Raporlama Standardı",
    ["Bağımsız denetçiler için etik kurallar",
     "Kalite yönetim standartları",
     "Sürdürülebilirlik denetimine ilişkin standartlar",
     "Bilgi sistemleri denetimine ilişkin düzenlemeler"],
    "m. 4/1-t'ye göre TDS; bilgi sistemleri ile sürdürülebilirlik denetimi dahil, uluslararası standartlarla uyumlu eğitim, "
    "etik, kalite yönetim ve denetim standartları ile diğer düzenlemelerdir. BOBİ FRS ise m. 4/1-u uyarınca Türkiye "
    "Muhasebe Standartları (TMS) kapsamındadır.")

P.q("BDY m. 5/2",
    "Bir limited şirket, ortakların talebiyle finansal tablolarını ihtiyari olarak denetletmek üzere bir denetim kuruluşuyla "
    "sözleşme imzalamıştır. Sözleşmede sağlanacak güvence seviyesine ilişkin herhangi bir hüküm bulunmamaktadır. "
    f"{B} bu denetime ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sınırlı güvence belirtilmediğinden denetim makul güvence verir.",
    ["Seviye belirtilmediğinden denetim sınırlı güvence verecek şekilde yürütülür.",
     "Güvence seviyesini sorumlu denetçi mesleki muhakemesiyle raporda belirler.",
     "Sözleşme güvence seviyesini içermediği için Kurum onayı alınmadan denetime başlanamaz.",
     "İhtiyari denetimlerde güvence verilmez; denetçi sadece tespitlerini raporlar."],
    "m. 5/2'ye göre denetim makul veya sınırlı güvence sağlar; sınırlı güvence sağlanacağı mevzuatta veya sözleşmede açıkça "
    "belirtilmemişse denetim makul güvence verecek şekilde gerçekleştirilir. Güvence seviyelerinin gerektirdiği kapsam TDS "
    "çerçevesinde belirlenir. m. 6'ya göre ihtiyari denetim de Yönetmelik kapsamındadır.")

P.q("BDY m. 5/4, m. 7",
    f"{B}, denetimin unsurları ve tarafları ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetim ücreti ve denetim süresi de denetimin unsurları arasında sayılır.",
    ["Denetimin unsurları denetimin konusu, tarafları, kıstası, kanıtları ve denetim raporudur.",
     "Denetlenen, denetimi yapan ve ilgili mevzuatında hedeflenen kullanıcılar denetimin taraflarıdır.",
     "Denetim, TDS çerçevesinde yeterli ve uygun kanıt toplanmasını, görüş oluşturulmasını ve raporlanmasını kapsar.",
     "Denetim, konu hakkında mesleki etik ilkelere bağlı kalmak ve mesleki şüphecilik içinde bulunmak suretiyle yapılır."],
    "m. 5/4'e göre denetimin unsurları konu, taraflar, kıstas, kanıtlar ve denetim raporudur; ücret ve süre unsur değildir. "
    "m. 7 tarafları denetlenen, denetimi yapan ve hedeflenen kullanıcılar olarak sayar; m. 5/3 denetimin kapsamını açıklar.")

P.q("BDY m. 8",
    "Bir anonim şirketin bağımsız denetiminde denetçi; finansal tablolar ile riskin erken saptanması ve yönetimine ilişkin "
    f"sistemi ayrı ayrı değerlendirecektir. {B} bu iki denetim konusunda esas alınacak denetim kıstasları sırasıyla "
    "aşağıdakilerden hangisidir?",
    "Türkiye Muhasebe Standartları; Türk Ticaret Kanunu ve ilgili mevzuatın kıstasa ilişkin hükümleri",
    ["Türkiye Denetim Standartları; Türk Ticaret Kanunu ve ilgili mevzuatın denetim kıstasına ilişkin hükümleri",
     "Türkiye Muhasebe Standartları; Kurumun her denetim için ayrıca ilan ettiği ölçütler",
     "Vergi Usul Kanunu ve Tekdüzen Hesap Planı; Türkiye Denetim Standartları",
     "Türkiye Denetim Standartları; Sermaye Piyasası Kanunu ve ilgili mevzuat"],
    "m. 8/1'e göre finansal tablolar açısından TMS; yıllık faaliyet raporları ile riskin erken saptanması ve yönetimine "
    "ilişkin sistem açısından Türk Ticaret Kanununun ve ilgili mevzuatın denetim kıstasına ilişkin hükümleri kıstastır. TDS "
    "denetimin nasıl yapılacağını düzenler, uyumun ölçüldüğü kıstas değildir.")

P.q("BDY m. 8/2",
    "Bir vakıf, ihtiyari olarak yaptırdığı denetimde bağış gelirlerinin kendi iç yönergesine uygun kullanılıp "
    f"kullanılmadığının değerlendirilmesini istemektedir. {B} bu denetimde denetim kıstasını belirleme yetkisi "
    "aşağıdakilerden hangisine aittir?",
    "Denetimi talep edenlere",
    ["Kamu Gözetimi Kurumuna",
     "Sorumlu denetçiye",
     "Denetim kuruluşunun yönetim organına",
     "Vakıflar Genel Müdürlüğüne"],
    "m. 8/2'ye göre diğer mevzuatta denetim öngörüldüğü hâlde kıstasın belirtilmediği durumlarda kıstası Kurum belirler; "
    "isteğe bağlı yaptırılan denetimlerde ise bu belirleme denetimi talep edenlerce yapılır.")

P.q("BDY m. 9, m. 35/3",
    f"{B}, denetim kanıtı ve denetim dosyası ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetim dosyası rapor teslim edildikten sonra da oluşturulabilir; esas olan raporun süresinde verilmesidir.",
    ["Denetim kanıtı, belirlenen güvence seviyesi için yeterli ve uygun bilgi, belge ve beyanlardır.",
     "Kanıtlar denetimin TDS çerçevesinde ve mesleki şüphecilik içinde planlanıp yürütülmesiyle elde edilir ve tevsik edilir.",
     "Her denetim çalışmasına ait elektronik ortamdakiler dahil tüm belgeler ekleriyle denetim dosyası hâline getirilir.",
     "Denetim kanıtı, konuda kıstasa göre önemli uyumsuzluk bulunup bulunmadığı hakkında görüş bildirmeye yöneliktir."],
    "m. 9 kanıtı yeterli ve uygun bilgi, belge ve beyanlar olarak tanımlar. m. 35/3'e göre her denetime ait belgeler denetim "
    "dosyası hâline getirilir ve denetim dosyalarının denetim sırasında oluşturulması esastır; sonradan oluşturma kural değildir.")

# ================================================================ yetkilendirme (m. 11-14)
P.q("BDY m. 11/3",
    "Denetim üstlenen bağımsız denetçi olarak sicile kayıtlı Serkan Bey'e, payları borsada işlem gören bir ortaklık denetim "
    f"teklifinde bulunmuştur. {B} bu teklife ilişkin aşağıdakilerden hangisi doğrudur?",
    "Teklifi kabul edemez; KAYİK'lerin denetimi sadece denetim kuruluşlarınca üstlenilebilir.",
    ["Kadrosunda en az bir sorumlu denetçi bulunduğu sürece teklifi kabul edebilir.",
     "Kurumdan o denetim için özel izin alarak teklifi kabul edebilir.",
     "Sermaye Piyasası Kurulunun listesinde yer alıyorsa teklifi kabul edebilir.",
     "Denetimi üstlenebilir, ancak raporu bir denetim kuruluşunun sorumlu denetçisiyle birlikte imzalar."],
    "m. 11/3'e göre KAYİK'lerin ve Kurumca belirlenen işletmelerin denetimi sadece denetim kuruluşlarınca, diğerlerinin "
    "denetimi ise denetim kuruluşları veya denetim üstlenen bağımsız denetçilerce üstlenilir. Halka açık şirket KAYİK'tir.")

P.q("BDY m. 11/2, m. 17/1",
    "Kurul, bir denetim kuruluşunun başvurusunu 3 Mart'ta uygun bulmuş; kuruluş 20 Mart'ta harç ve ücretleri ödeyerek tescil "
    f"talep etmiş, sicile kayıt ve Kurum internet sitesinde ilan 27 Mart'ta yapılmış, Bağımsız Denetim Kuruluşu Belgesi 2 Nisan'da teslim edilmiştir. {B} kuruluş denetim yetkisini "
    "hangi tarihten itibaren kullanabilir?",
    "27 Mart'tan itibaren",
    ["3 Mart'tan itibaren", "20 Mart'tan itibaren", "2 Nisan'dan itibaren", "Kurul kararının tebliğinden itibaren"],
    "m. 11/2'ye göre yetkilerin kullanımı yetkilendirmenin Kurum tarafından ilanıyla başlar; m. 17/1'e göre de yetkilendirme "
    "işlemleri sicile kayıt ve Kurum internet sitesinde ilanla yürürlüğe girer.")

P.q("BDY m. 13/1",
    f"{B}, denetim alanında faaliyet izni talep eden bir kuruluşta aranan şartlarla ilgili aşağıdakilerden hangisi yanlıştır?",
    "Payların veya hisselerin nama ya da hamiline yazılı olması mümkündür.",
    ["Kuruluşun sermaye şirketi olması gerekir.",
     "Ticaret unvanında “bağımsız denetim” ibaresinin bulunması gerekir.",
     "Sermayesinin ve oy haklarının yarısından fazlası denetçilerine ait olmalıdır.",
     "Kalite yönetim sistemine ilişkin politika ve süreçlerini denetim rehberleri dahil yazılı olarak oluşturmuş olmalıdır."],
    "m. 13/1'e göre kuruluşun sermaye şirketi olması, paylarının veya hisselerinin nama yazılı olması, unvanında bağımsız "
    "denetim ibaresi bulunması, sermaye ve oy haklarının yarısından fazlasının denetçilerine ait olması ve kalite yönetim "
    "sistemi politikalarını yazılı oluşturmuş olması şarttır. Hamiline yazılı pay kabul edilmez.")

P.q("BDY m. 13/1-e",
    "Faaliyet izni için başvuran ABC Bağımsız Denetim A.Ş.'nin sermayesinin %70'i Kurumca yetkilendirilmiş denetçilerine, "
    "%30'u ise yeminli mali müşavir ya da serbest muhasebeci mali müşavir olmayan bir iktisatçıya aittir. "
    f"{B} bu başvuruya ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ortaklarının tamamı meslek mensubu olmadığı için faaliyet izni verilemez.",
    ["Sermayenin yarısından fazlası denetçilere ait olduğundan izin verilebilir.",
     "İktisatçı ortağın payı %25'in altına indirilirse izin verilebilir.",
     "İktisatçı ortak yönetim organında yer almadığı sürece izin verilebilir.",
     "Oy haklarının tamamı denetçilere tanınırsa sermaye yapısı değiştirilmeden izin verilebilir."],
    "m. 13/1-e iki şartı birlikte arar: sermaye ve oy haklarının yarısından fazlasının denetçilere ait olması ve ortakların "
    "tamamının meslek mensubu olması. Meslek mensubu olmayan bir ortak bulunduğundan ikinci şart karşılanmamaktadır; "
    "m. 4/1-ç de denetim kuruluşunu ortakları meslek mensuplarından oluşan sermaye şirketi olarak tanımlar.", zorluk="hard")

P.q("BDY m. 13/2, 13/5",
    "(i) Başvuru sahibi kuruluşlardan gerekli şartları taşıdığına karar verilenler, en geç ---- içinde harç ve ücretleri "
    "ödeyip tescil talebinde bulunmaları hâlinde sicile kayıt ve ilan edilir. (ii) Ticaret unvanında bağımsız denetim "
    "ibaresi bulunmayan kuruluşlara ---- içinde unvan değişikliği yapılması ve ilan edilmesi koşuluyla faaliyet izni "
    f"verilebilir.\n\n{B} boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?",
    "(i) doksan gün (ii) üç ay",
    ["(i) otuz gün (ii) altı ay", "(i) altmış gün (ii) üç ay", "(i) doksan gün (ii) bir ay", "(i) on beş gün (ii) iki ay"],
    "m. 13/2'ye göre şartları taşıdığına karar verilen kuruluşlar en geç doksan gün içinde harç ve ücretleri ödeyip tescil "
    "talep ederse sicile kayıt ve ilan edilir. m. 13/5'e göre unvanında bağımsız denetim ibaresi bulunmayanlara üç ay "
    "içinde unvan değişikliği yapıp Türkiye Ticaret Sicili Gazetesinde ilan etmeleri koşuluyla izin verilebilir.")

P.q("BDY m. 13/3, 13/6",
    f"{B}, denetim kuruluşlarının yetkisini kullanması ve yapısal değişiklikleri ile ilgili aşağıdakilerden hangisi "
    "yanlıştır?",
    "Sorumlu denetçinin raporu imzalamasıyla denetim kuruluşunun ve kilit yöneticilerinin sorumluluğu sona erer.",
    ["Denetim kuruluşları denetim yetkisini, raporu kuruluş adına imzalamaya yetkili sorumlu denetçileri eliyle kullanır.",
     "Diğer mevzuat saklı kalmak kaydıyla denetim kuruluşlarının birleşme ve bölünme işlemleri Kurum iznine tabidir.",
     "Denetim kuruluşlarının devir ve tür değişikliği işlemleri de Kurumun iznine bağlıdır.",
     "Kurum, belirli alanlarda denetim yapacak kuruluşlar için ek şartlar belirleyip bunları listeler hâlinde ilan edebilir."],
    "m. 13/6'ya göre denetim yetkisi sorumlu denetçiler eliyle ve sorumluluğunda kullanılır; ancak bu sorumluluk denetim "
    "kuruluşunun ve kilit yöneticilerinin sorumluluğunu ortadan kaldırmaz. m. 13/3 devir, bölünme, birleşme ve tür "
    "değişikliğini Kurum iznine bağlar; m. 13/4 ek şartlı listeleri düzenler.")

P.q("BDY m. 14/1",
    f"{B}, Bağımsız Denetçi Belgesi almak isteyen bir meslek mensubunda aranan şartlar arasında aşağıdakilerden hangisi "
    "yoktur?",
    "Ruhsatını en az beş yıl önce almış olması",
    ["Türkiye'de yerleşik olması",
     "Uygulamalı mesleki eğitimi tamamlamış olması",
     "Denetçilik sınavında başarılı olması",
     "Medeni hakları kullanma ehliyetine sahip bulunması"],
    "m. 14/1 lisans eğitimi, meslek mensubu olmak, Türkiye'de yerleşik olmak, medeni hakları kullanma ehliyeti, uygulamalı "
    "mesleki eğitim, sınav başarısı, belirli suçlardan mahkûmiyet bulunmaması ve itibar şartlarını sayar; ruhsat "
    "kıdemine ilişkin bir süre öngörmez.", zorluk="easy")

P.q("BDY m. 14/1-a",
    "Endüstri mühendisliği lisans programından mezun olan ve daha sonra işletme alanında yüksek lisans diploması alan "
    f"serbest muhasebeci mali müşavir Elif Hanım denetçilik sınavına başvurmak istemektedir. {B} Elif Hanım'ın "
    "öğrenim durumuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Listede sayılan bir dalda lisansüstü diploması bulunduğu için mezuniyet şartını karşılar.",
    ["Lisansı sayılan dallardan olmadığı için yüksek lisans diploması mezuniyet şartını karşılamaz.",
     "Sınava girebilir, ancak yetkilendirme için ayrıca işletme lisansı tamamlamalıdır.",
     "Mühendislik mezunları sadece bilgi sistemleri denetimi alanında sınava girebilir.",
     "Mezuniyet şartı yeminli mali müşavirler için aranır, SMMM'ler için aranmaz."],
    "m. 14/1-a hukuk, iktisat, maliye, işletme, muhasebe, bankacılık, sigortacılık, kamu yönetimi ve siyasal bilgiler "
    "dallarından en az lisans mezuniyetini ya da diğer dallardan lisansla birlikte bu dallardan en az lisansüstü diplomayı "
    "yeterli sayar. m. 16/2'ye göre sınava girişte de bu şart aranır.")

P.q("BDY m. 14/3",
    f"{B}, bağımsız denetçilerin kendi adına denetim üstlenebilmesi için aranan şartlar arasında aşağıdakilerden hangisi "
    "yoktur?",
    "Denetim faaliyetini sermaye şirketi olarak kurduğu bir işletme üzerinden yürütmesi",
    ["Başvuranın sorumlu denetçi olabilme şartlarını karşılaması",
     "Denetim kadrosunda kendisi hariç en az bir sorumlu denetçinin bulunması",
     "Denetçilerinin tam zamanlı ve asgari bir raporlama dönemi için istihdam edilmiş olması",
     "Denetim kadrosunun asgari olarak Yönetmelikteki denetim ekiplerini oluşturabilecek genişlikte olması"],
    "m. 14/3 kendi adına denetim üstlenmek için sorumlu denetçi şartları, ekip oluşturabilecek kadro, tam zamanlı istihdam, "
    "kendisi hariç en az bir sorumlu denetçi, başka kuruluşta görev almama, yazılı kalite yönetimi politikaları ve uygun "
    "organizasyonu arar. Sermaye şirketi olma şartı m. 13'te denetim kuruluşları için öngörülmüştür.")

# ================================================================ uygulamalı eğitim ve sınav (m. 15-16)
P.q("BDY m. 15/1",
    "Serbest muhasebeci mali müşavir Can Bey, iki yıl bir denetim kuruluşunda finansal tablo denetimlerinde çalışmış, "
    "daha önce de 3568 sayılı Kanun çerçevesinde bir buçuk yıl tasdik hizmetlerinde bulunmuştur. "
    f"{B} Can Bey'in uygulamalı mesleki eğitim durumuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tasdik hizmetinde geçen süre de sayıldığından üç yıllık eğitim şartını karşılamıştır.",
    ["Tasdik hizmeti sayılmadığından bir yıl daha denetim kuruluşunda çalışmalıdır.",
     "Uygulamalı eğitim sadece denetim üstlenen bağımsız denetçi yanında alınabildiğinden süreler sayılmaz.",
     "Uygulamalı eğitim beş yıl olduğundan bir buçuk yıl daha eğitim alması gerekir.",
     "Tasdik süresinin yarısı sayılır; toplam süre iki yıl dokuz ay olduğundan şart karşılanmamıştır."],
    "m. 15/1'e göre denetçi olmak isteyenler en az 3 yıl denetim kuruluşunda veya denetim üstlenen bağımsız denetçi yanında "
    "uygulamalı eğitim alır; 3568 sayılı Kanun çerçevesinde tasdik ve vergi denetimi hizmetlerinde geçen süreler bu süreden "
    "sayılır. İki yıl ile bir buçuk yılın toplamı üç yılı aşar.")

P.sayisal("BDY m. 15/3",
    "İşletme bölümünü dört yılda bitiren Deniz Hanım 1 Ocak 2012'de 3568 sayılı Kanun kapsamındaki mesleki faaliyetlerine "
    "başlamış, 2016-2018 döneminde (üç yıl) bu faaliyetlere ara vermiş, 1 Ocak 2019'dan bu yana kesintisiz çalışmaktadır. "
    f"Ara verdiği dönemde kamu kurumunda görev almamıştır. {B} 1 Ocak 2026 itibarıyla dikkate alınacak mesleki tecrübesi "
    "kaç yıldır?",
    "16", ["11", "12", "14", "18"],
    "m. 15/3'e göre süre faaliyete başlama tarihinden hesaplanır; bir yıldan fazla ara verilirse ara verilen fazla süre "
    "dikkate alınmaz. 2012-2026 arası 14 yıldır; üç yıllık aranın iki yılı düşülür ve 12 yıl kalır. Dört yılı aşmamak ve "
    "çakışmamak şartıyla m. 14/1-a'daki dallardaki lisans süresi eklenir: 12 + 4 = 16 yıl.", zorluk="hard")

P.q("BDY m. 15/2, 15/4",
    f"{B}, uygulamalı mesleki eğitimle ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Uygulamalı eğitim alanlar bu dönemde kıdemlerine göre denetim ekiplerinde denetçi olarak görevlendirilebilir.",
    ["En az on beş yıl mesleki tecrübeye sahip olanlarda uygulamalı mesleki eğitim şartı aranmaz.",
     "Uygulamalı mesleki eğitim alanlar bu dönemde denetçi yardımcısıdır ve denetçilerin refakatinde çalışır.",
     "Refakatinde denetçi yardımcısı çalıştıranlar, yardımcıların mesleki yeterlik kazanması için her türlü tedbiri alır.",
     "Denetçi, yardımcılarının hazırladığı çalışma kâğıtlarını incelemek ve çalışmalarına nezaret etmekle yükümlüdür."],
    "m. 15/2 on beş yıl tecrübesi olanlarda eğitim şartını kaldırır. m. 15/4'e göre eğitim alanlar denetçi yardımcısıdır, "
    "denetçilerin refakatinde çalışır; m. 27/3'e göre de denetçi yardımcıları ekipte denetçi olarak görevlendirilmemek "
    "kaydıyla yer alabilir.")

P.q("BDY m. 16/3-4",
    f"Temel alanda yetkilendirilmek isteyen bir yeminli mali müşavir, {B} denetçilik sınavında hangi konulardan "
    "sınava tabi tutulur?",
    "Türkiye Muhasebe Standartları ve Türkiye Denetim Standartları",
    ["Türkiye Muhasebe Standartları, Türkiye Denetim Standartları ve Sermaye Piyasası Mevzuatı",
     "Türkiye Denetim Standartları ile Kurumsal Yönetim İlkeleri ve Finansal Yönetim",
     "Türkiye Muhasebe Standartları, Türkiye Denetim Standartları, Kurumsal Yönetim İlkeleri ve Finansal Yönetim",
     "Sadece Türkiye Denetim Standartları"],
    "m. 16/4'e göre temel alan için serbest muhasebeci mali müşavirler TMS, TDS ile Kurumsal Yönetim İlkeleri ve Finansal "
    "Yönetim konularından; yeminli mali müşavirler ise TMS ve TDS konularından sınava tabi tutulur. Sermaye piyasası gibi "
    "alanlar temel alana ek yetkilendirme içindir.")

P.q("BDY m. 16/7",
    "Denetçilik sınavının sonuçları 10 Nisan 2025 tarihinde ilan edilmiş ve Burak Bey başarılı olmuştur. "
    f"{B} Burak Bey'in sınav sonucu hangi tarihe kadar geçerlidir?",
    "31 Aralık 2028",
    ["10 Nisan 2027", "31 Aralık 2027", "10 Nisan 2028", "31 Aralık 2030"],
    "m. 16/7'ye göre sınav sonuçları ilan tarihini müteakip üçüncü takvim yılı sonuna kadar geçerlidir. 2025'te ilan edilen "
    "sonuç için izleyen üçüncü takvim yılı 2028'dir.")

# ================================================================ sicil (m. 17-18)
P.q("BDY m. 17/3-4, m. 25/7",
    "Denetçi Mert Bey, Kurumun öngördüğü sürekli eğitim yükümlülüğünü içinde bulunduğu dönemde tamamlamamıştır. "
    f"{B} bu durumun sonucu aşağıdakilerden hangisidir?",
    "Sicilde gayri faal gösterilir, tamamlayana kadar denetim yapamaz.",
    ["Sicilden silinir ve yeniden yetkilendirme başvurusu yapması gerekir.",
     "Faaliyet izni iptal edilir; iki yıl geçmeden yeniden başvuramaz.",
     "Denetim yapmaya devam eder, eksik saatleri izleyen yıl tamamlar.",
     "Sorumlu denetçi olamaz, ancak ekiplerde denetçi olarak görev alabilir."],
    "m. 17/3'e göre sürekli eğitim yükümlülüğünü yerine getirmeyenler sicilde gayri faal olarak gösterilir, sicilden "
    "silinmez; m. 17/4 gayri faal olanların denetim faaliyetinde bulunamayacağını, m. 25/7 de yükümlülük yerine "
    "getirilinceye kadar denetim yapamayacaklarını ve ekiplerde görevlendirilemeyeceklerini düzenler.")

P.q("BDY m. 18/1",
    f"{B}, Kurumca tutulan sicilde denetim kuruluşlarına ilişkin kaydedilen bilgiler arasında aşağıdakilerden hangisi "
    "yer almaz?",
    "Denetlediği her işletmeden aldığı denetim ücretlerinin dökümü",
    ["Varsa bünyesinde bulunduğu denetim ağı ve bu ağın hukuki ve yapısal niteliği",
     "Ortaklarının sermayedeki payları, pay oranları ve tutarları",
     "Denetçilerinin listesi ve sicil numaraları",
     "Denetim yapma yetkisi bulunan alana ilişkin bilgiler"],
    "m. 18/1 sicilde unvan, sicil numaraları, adresler ve denetim ağı, internet sitesi, ortaklar ve payları, yönetim organı, "
    "denetçi listesi, yurt dışı sicil kayıtları, faal ya da gayri faal olma ve yetki alanı bilgilerini sayar. İşletme bazında "
    "ücret dökümü sicil bilgisi değildir.")

# ================================================================ yükümlülükler: süreç, kalite, etik (m. 19-21)
P.q("BDY m. 19/3",
    "Denetim süreci, her bir hesap dönemi için (i)---- başlar, TDS'ye göre planlanır, programlanır, yürütülür ve "
    f"(ii)---- sona erer.\n\n{B} yukarıdaki boşlukları tamamlayan seçenek aşağıdakilerden hangisidir?",
    "(i) işletmenin iş teklifiyle (ii) denetim sonucunun raporlanmasıyla",
    ["(i) denetim sözleşmesinin imzalanmasıyla (ii) genel kurulun finansal tabloları onaylamasıyla",
     "(i) denetçinin genel kurulca seçilmesiyle (ii) raporun Kuruma bildirilmesiyle",
     "(i) işletmenin iş teklifiyle (ii) çalışma kâğıtlarının arşivlenmesiyle",
     "(i) ön planlama toplantısıyla (ii) yönetim organının raporu teslim almasıyla"],
    "m. 19/3'e göre denetim süreci her hesap dönemi için işletmenin iş teklifiyle başlar, TDS'ye göre planlanır, "
    "programlanır, yürütülür ve denetim sonucunun raporlanmasıyla sona erer; rapordan sonraki yükümlülükler saklıdır ve "
    "süreç TDS çerçevesinde belgelendirilir.")

P.q("BDY m. 20/2",
    "Bir denetçi, içinde bulunulan koşullara özgü sebeplerle, çalıştığı kuruluşun yazılı kalite yönetimi prosedürü yerine "
    f"farklı bir uygulamanın Kurum düzenlemesine uyum bakımından daha uygun olduğu kanaatine varmıştır. {B} "
    "denetçinin yapması gereken aşağıdakilerden hangisidir?",
    "Yazılı politikanın dışına çıkabilir; durumu ve nedenini yazılı olarak kuruluşa sunar ve saklar.",
    ["Yazılı politikaya uymak zorunluluğu nedeniyle farklı uygulamayı ancak izleyen yıl uygulayabilir.",
     "Kurumdan önceden yazılı onay almadan politika dışına çıkamaz.",
     "Farklı uygulamayı yapabilir, ancak durumu denetim raporunda ayrı paragrafla açıklar.",
     "Politika dışına çıkabilmesi için denetlenen işletmenin üst yönetiminin onayını alır."],
    "m. 20/2'ye göre yazılı politika ile Kurum düzenlemesi arasında farklılık varsa veya koşullara özgü sebeplerle başka bir "
    "uygulama uyum bakımından daha uygun görülürse politikanın dışına çıkılabilir; bu durumun ve nedeninin denetçi "
    "tarafından yazılı olarak kuruluşa sunulması ve saklanması gerekir.", zorluk="hard")

P.q("BDY m. 21/2",
    f"{B}, denetim kuruluşlarının denetçilerden ve denetime katılanlardan alacağı yazılı taahhütle ilgili aşağıdakilerden "
    "hangisi yanlıştır?",
    "Taahhüt, sadece denetçinin kuruluşta işe başladığı tarihte bir kez alınır.",
    ["Taahhüt her bir denetimden önce ve her hâlükârda yılda en az bir kez alınır.",
     "Taahhüt bağımsızlık, tarafsızlık ve sır saklamaya ilişkin politika ve süreçlere uyumu kapsar.",
     "Denetime başladıktan sonra bu hususları olumsuz etkileyen bir durum çıkarsa kuruluşa yazılı bildirim yapılır.",
     "Taahhüdün alınmamış olması Yönetmelikte ikaz yaptırımı gerektiren hâller arasında sayılmıştır."],
    "m. 21/2'ye göre yazılı taahhüt her bir denetimden önce ve her hâlükârda yılda en az bir kez; bağımsızlık, tarafsızlık "
    "ve sır saklamaya ilişkin politika ve süreçlere uyuma dair alınır. Sonradan ortaya çıkan olumsuz hususlar yazılı "
    "bildirilir. m. 39/A-b taahhüdün alınmamasını ikaz sebebi sayar.")

# ================================================================ bağımsızlık (m. 22)
P.q("BDY m. 22/1",
    f"{B}, denetim kuruluşunun veya denetçinin; konuya ilişkin tüm durum ve gerçekleri değerlendiren makul ve bilgi sahibi "
    "üçüncü kişilerde dürüstlük, tarafsızlık ve mesleki şüphecilikten ödün verdiği intibaını oluşturabilecek durum ve "
    "davranışlardan sakınması aşağıdakilerden hangisidir?",
    "Şekilde bağımsızlık",
    ["Esasta bağımsızlık", "Mesleki şüphecilik", "Mesleğe uygun davranış", "Tarafsızlık"],
    "m. 22/1-b bu tanımı şekilde bağımsızlık için yapar. Esasta bağımsızlık ise denetçinin mesleki muhakemesini olumsuz "
    "etkileyebilecek tesirlerden ari olarak görüş açıklamasıdır (m. 22/1-a).", zorluk="easy")

P.q("BDY m. 22/3-a",
    f"{B}, aşağıdaki durumlardan hangisi denetçinin bağımsızlığını zedeleyen veya ortadan kaldıran hâller arasında "
    "sayılmaz?",
    "Denetçinin eşinin kuzeninin denetlenen işletmede küçük bir pay sahibi olması",
    ["Denetçinin boşanmış eşinin denetlenen işletmenin ortağı olması",
     "Denetçinin yeğeninin denetlenen işletmede kilit yönetici olarak çalışması",
     "Denetçinin kayınbiraderinin denetlenen işletmeyle olağan ekonomik ilişkiler dışında borç ilişkisine girmesi",
     "Denetim kuruluşunun kilit yöneticisinin denetlenen işletmeyle menfaat ilişkisi kurması"],
    "m. 22/3-a denetçiler ile kuruluş ortakları, kilit yöneticileri, denetçileri ve bunların boşanmış olsalar dahi eşleri "
    "ile üçüncü dereceye kadar (üçüncü derece dahil) kan ve kayın hısımlarını kapsar. Yeğen üçüncü derece kan, kayınbirader "
    "ikinci derece kayın hısımıdır; eşin kuzeni ise dördüncü derece kayın hısımı olduğundan bu bendin dışında kalır.",
    zorluk="hard")

P.q("BDY m. 22/3-b, c",
    "Bir denetim kuruluşunun geçmiş yıla ait denetim ücreti, denetlenen işletme tarafından geçerli bir neden gösterilmeksizin "
    "ödenmemiştir. İşletme cari yıl için de ücretin bir kısmını denetim raporunun olumlu görüş içermesi şartına bağlamayı "
    f"önermektedir. {B} bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "Her iki durum da bağımsızlığı zedeleyen veya ortadan kaldıran hâller arasında sayılmıştır.",
    ["Ödenmeyen ücret ticari bir alacaktır; bağımsızlığı etkileyen sadece şarta bağlı ücret önerisidir.",
     "Şarta bağlı ücret denetim sözleşmesinde açıkça gösterilirse bağımsızlığı etkilemez.",
     "Geçmiş yıl ücretinin ödenmemesi, tutar önemsizse bağımsızlığı etkilemez.",
     "İki durumda da bağımsızlık korunur; denetçi sadece durumu raporunda açıklar."],
    "m. 22/3-b geçmiş yıllar ücretinin geçerli bir neden olmadan ödenmemesini, m. 22/3-c ücretin denetim sonuçlarıyla ilgili "
    "şartlara bağlanmasını bağımsızlığı zedeleyen hâller olarak sayar. m. 29/2'ye göre de ücretin ödenmesi denetim hizmeti "
    "dışında başka bir şarta bağlanamaz.")

P.q("BDY m. 22/4",
    f"{B}, bağımsızlığı tehdit eden hususlar ve bunlara karşı alınacak önlemlerle ilgili aşağıdakilerden hangisi "
    "yanlıştır?",
    "Bağımsızlık zedelendiğinde denetçi ek önlemlerle denetimi tamamlar ve durumu raporunda açıklar.",
    ["Bağımsızlığı tehdit eden hususların ortaya çıkması hâlinde bağımsızlığı koruyacak önlemler alınır.",
     "Alınan önlemler tehditleri bertaraf etmeye yetmezse bağımsızlığın zedelendiği ve ortadan kalktığı kabul edilir.",
     "Tehditler, alınan önlemler ve yapılan değerlendirmeler yazılı olarak kayda alınır ve saklanır.",
     "Bağımsızlığın zedelendiği hâller Kuruma bildirilir ve ilgili denetim sözleşmesi sonlandırılır."],
    "m. 22/4'e göre tehditlere karşı önlem alınır; önlemler yetmezse bağımsızlığın ortadan kalktığı kabul edilir. Tehditler, "
    "önlemler ve değerlendirmeler yazılı kayda alınıp saklanır; bağımsızlığın zedelendiği hâller Kuruma bildirilir ve "
    "sözleşme sonlandırılır. Denetime devam edip raporda açıklama yapmak öngörülmemiştir.")

P.q("BDY m. 22/5",
    "X Bağımsız Denetim A.Ş.'nin aynı denetim ağında yer alan danışmanlık şirketi, X'in denetlediği bir anonim şirkete "
    f"ücret bordrolarının hazırlanması ve muhasebe kayıtlarının tutulması hizmeti vermeyi teklif etmektedir. {B} "
    "bu teklif bakımından aşağıdakilerden hangisi doğrudur?",
    "Denetim dışı hizmet denetim ağındaki işletme aracılığıyla da verilemeyeceğinden teklif Yönetmeliğe aykırıdır.",
    ["Hizmeti denetim kuruluşu değil ağdaki başka bir şirket vereceğinden Yönetmeliğe aykırılık yoktur.",
     "Hizmet ücreti denetim ücretinden düşük tutulursa teklif Yönetmeliğe uygundur.",
     "Muhasebe kayıtları tasdik kapsamında sayıldığından hizmet verilebilir.",
     "Teklif, denetlenen işletmenin genel kurulu onaylarsa verilebilir."],
    "m. 22/5'e göre denetim kuruluşu ve denetçiler denetlenen işletmeye 3568 sayılı Kanun çerçevesinde tasdik, vergi "
    "danışmanlığı ve vergi denetimi dışında hizmet veremez; bunu denetim ağındaki, ilişkili kuruluş ve işletmeler "
    "aracılığıyla da yapamaz. Bu aykırılık m. 41/1-d'ye göre faaliyet izninin askıya alınması sebebidir.")

# ================================================================ reklam, haksız rekabet, sürekli eğitim (m. 23-25)
P.q("BDY m. 23",
    f"{B}, aşağıdaki faaliyetlerden hangisi denetim kuruluşları için öngörülen reklam yasağına aykırıdır?",
    "Tanıtım broşüründe raporlarını rakip kuruluşlardan daha kısa sürede teslim ettiğini karşılaştırarak belirtmek",
    ["Kurumsal tanıtıcı bilgiler içeren broşürler hazırlayıp dağıtmak",
     "Denetlediği bir işletme için eleman aramaya yönelik ilan vermek",
     "Yeni finansal raporlama standartları hakkında ücretsiz bir seminer düzenlemek",
     "Mesleki konularda bilimsel nitelikli bir makale yayımlamak"],
    "m. 23/2 tanıtıcı broşür, eleman ilanı, bilimsel yayın, seminer ve eğitim faaliyetlerine izin verir. m. 23/3-d'ye göre "
    "bu faaliyetlerde denetim kuruluşunun başka bir kuruluş veya denetçiyle karşılaştırılmaması gerekir; ayrıca somut "
    "temeli olmayan beklenti yaratılamaz.")

P.q("BDY m. 24",
    "Y Bağımsız Denetim A.Ş., başka bir denetim kuruluşuyla cari yıl için denetim sözleşmesi devam eden bir şirketten aynı "
    f"döneme ilişkin daha düşük ücretli bir denetim teklifi almıştır. {B} bu teklife ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Kurumun izin verdiği hâller dışında Y aynı döneme ilişkin denetim talebini kabul edemez.",
    ["Ücret teklifi Kurum tarifesinin altında değilse Y talebi kabul edebilir.",
     "Mevcut denetçinin yazılı muvafakati alınırsa Y talebi kabul edebilir.",
     "Denetlenen işletmenin yönetim kurulu mevcut sözleşmeyi feshetmişse Y talebi kabul edebilir.",
     "Y talebi kabul edebilir; haksız rekabet sadece reklam yoluyla gerçekleşebilir."],
    "m. 24/2'ye göre denetim kuruluşu ve denetim üstlenen bağımsız denetçiler, Kurumun izin verdiği hâller hariç, başka bir "
    "denetimi üstlenenle hizmet ilişkisi devam eden bir işletmenin aynı döneme ilişkin talebini kabul edemez. Görevden alma "
    "ise m. 29/4'e göre sadece TTK m. 399/4'teki şekilde mümkündür.")

P.q("BDY m. 25/2",
    "Denetçi Seda Hanım, Bağımsız Denetçi Belgesi için 14 Mart 2024 tarihinde sicile tescil edilmiştir. "
    f"{B} Seda Hanım'ın sürekli eğitim yükümlülüğü hangi tarihten itibaren başlar?",
    "1 Ocak 2026",
    ["14 Mart 2024", "1 Ocak 2025", "14 Mart 2025", "1 Ocak 2027"],
    "m. 25/2'ye göre sürekli eğitim yükümlülüğü denetçinin sicile tescil edildiği tarihi izleyen ikinci takvim yılının "
    "başından itibaren başlar. 2024'ü izleyen ikinci takvim yılı 2026'dır.")

# ================================================================ kısıtlamalar (m. 26)
P.q("BDY m. 26/1-ç",
    "Denetçi Oğuz Bey, 2016-2022 hesap dönemlerinde (yedi yıl) Z A.Ş.'nin denetiminde görev almıştır. "
    f"{B} Oğuz Bey, Z A.Ş.'nin denetiminde en erken hangi hesap döneminden itibaren yeniden görev alabilir?",
    "2026",
    ["2023", "2024", "2025", "2027"],
    "m. 26/1-ç'ye göre son on yılda yedi yıl denetim çalışması yürütülen işletmeye ilişkin denetimler üç yıl geçmedikçe "
    "üstlenilemez. 2023, 2024 ve 2025 dönemlerinden sonra, 2026 hesap döneminden itibaren yeniden görev alınabilir.")

P.q("BDY m. 26/2",
    "Denetçi Aslı Hanım, K A.Ş.'nin denetiminde dört yıl A Denetim A.Ş.'de, ardından üç yıl aynı denetim ağına bağlı olmayan "
    f"B Denetim A.Ş.'de görev almıştır. {B} bu sürelerin rotasyon kuralı bakımından değerlendirilmesine ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Aynı işletmede geçen süreler kuruluşa bakılmaksızın birlikte dikkate alınır; toplam yedi yıldır.",
    ["Farklı ve ağ ilişkisi olmayan kuruluşlarda geçtiğinden süreler ayrı ayrı hesaplanır.",
     "Sadece son kuruluştaki üç yıl dikkate alınır; kuruluş değişikliği rotasyon süresini yeniden başlatır.",
     "Süreler birleştirilir, ancak ilk kuruluştaki sürenin yarısı dikkate alınır.",
     "Süreler sadece aynı denetim ağındaki kuruluşlarda geçmişse birlikte dikkate alınır."],
    "m. 26/2'ye göre aynı ağdaki ve ilişkili kuruluşlardaki süreler topluca dikkate alınır; ayrıca çalıştığı denetim "
    "kuruluşuna bakılmaksızın denetçinin aynı işletmenin denetiminde geçirdiği süreler birlikte dikkate alınır.", zorluk="hard")

P.q("BDY m. 26/3-4",
    f"{B}, denetçilerin görevden ayrılmaları ve birden fazla kuruluşta çalışmaları ile ilgili aşağıdakilerden hangisi "
    "yanlıştır?",
    "Denetçiler, ayrıldıkları kuruluşun son iki yılda denetlediği işletmelerde bir yıl geçmeden kilit yönetici olamaz.",
    ["Denetçiler denetçilik görevinden ayrılmalarından itibaren iki yıl geçmedikçe bu yasağa tabidir.",
     "Yasak, denetçinin son iki yılda denetiminde bulunduğu işletmelerin bağlı ortaklıklarını da kapsar.",
     "Denetçiler sadece bir denetim kuruluşu veya denetim üstlenen bağımsız denetçi adına denetim yapabilir.",
     "İlişkisi sona ermedikçe denetçi başka bir denetim kuruluşunda ortak olamaz ve denetim faaliyetinde bulunamaz."],
    "m. 26/3'e göre denetçiler denetçilik görevinden ayrılmalarından itibaren iki yıl geçmedikçe son iki yılda denetiminde "
    "bulundukları işletmelerde ve bağlı ortaklıklarında kilit yönetici olamaz. m. 26/4 tek bir kuruluş adına denetim yapma "
    "kuralını düzenler.")

# ================================================================ ekipler ve sorumlu denetçi (m. 27-28)
P.q("BDY m. 27/1, 27/3",
    f"{B}, denetim ekipleriyle ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bilgi sistemleri uzmanları asgari denetçi sayısının hesabında dikkate alınır.",
    ["Denetim ekipleri üç denetçiden az olamaz.",
     "Sorumlu denetçi ve belirlenen diğer kademeler için en az birer yedek denetçi belirlenir.",
     "Kurum, işletmelerin özelliklerine göre farklı asgari denetçi ve yedek denetçi sayıları belirleyebilir.",
     "Teknik bilgisine başvurulan uzmanlar denetimin herhangi bir aşamasında karar verici konumda bulunamaz."],
    "m. 27/1'e göre ekipler üç denetçiden az olamaz, sorumlu denetçi ve diğer kademeler için yedek belirlenir ve Kurum "
    "farklı asgari sayılar belirleyebilir. m. 27/3'e göre uzmanlar denetçilerin gözetiminde çalışır, karar verici "
    "olamaz ve asgari denetçi sayısı hesabında dikkate alınmaz.")

P.q("BDY m. 27/5",
    "Denetçi olarak yetkilendirildiği tarihten bu yana yedi yıldır bir denetim kuruluşunda denetçilik yapan Ece Hanım'a "
    f"{B} kuruluş tarafından hangi unvan verilebilir?",
    "Kıdemli denetçi unvanı verilebilir, başdenetçi unvanı verilemez.",
    ["Başdenetçi unvanı verilebilir, kıdemli denetçi unvanına gerek yoktur.",
     "Kıdemli denetçi unvanı için on yıl gerektiğinden denetçi unvanıyla devam eder.",
     "Unvanları Kurum verdiğinden kuruluş ancak Kuruma öneride bulunabilir.",
     "Kıdemli denetçi unvanı için sorumlu denetçi onayı almış olması gerekir."],
    "m. 27/5'e göre denetim kuruluşları denetçilere denetçi, kıdemli denetçi ve başdenetçi unvanları verebilir; denetçilikte "
    "altı yılını doldurmayanlara kıdemli denetçi, on yılını doldurmayanlara başdenetçi unvanı verilemez.")

P.q("BDY m. 28/1",
    "On iki yıllık mesleki tecrübesinin dört yılında fiilen denetçi unvanıyla denetimlerde bulunan ve kuruluşunun yönetim "
    f"organınca rapor imzalamaya yetkilendirilen Tolga Bey için {B} aşağıdakilerden hangisi doğrudur?",
    "Kurum onayıyla KAYİK dışındaki denetimlerde sorumlu denetçi olarak görevlendirilebilir.",
    ["KAYİK denetimleri dahil bütün denetimlerde sorumlu denetçi olabilir.",
     "Sorumlu denetçi olabilmek için başdenetçi unvanını beklemelidir.",
     "Yönetim organının yetkilendirmesi yeterli olduğundan Kurum onayı aranmaz.",
     "Sorumlu denetçi olabilmesi için tecrübesinin en az beş yılı denetimde geçmelidir."],
    "m. 28/1'e göre sorumlu denetçi, Kurum onayıyla görevlendirilir. KAYİK'ler için 15 yıllık tecrübe ve bunun en az üç "
    "yılında fiilen denetim; diğer denetimler için 10 yıllık tecrübe ve en az iki yılında fiilen denetim ile rapor "
    "imzalamaya yetkilendirilmiş olma aranır.", zorluk="hard")

# ================================================================ sözleşme (m. 29)
P.q("BDY m. 29/1-2",
    f"{B}, aşağıdakilerden hangisi denetim sözleşmesinde yer alması gereken asgari hususlardan biri değildir?",
    "Denetlenen işletmeye ayrıca verilecek vergi danışmanlığı hizmetinin kapsamı ve ücreti",
    ["Denetim ekibindeki denetçilerin yedekleri dahil isim ve unvanları ile öngörülen çalışma süreleri",
     "Denetimle ilgili istenen her türlü kayıt ve bilgiye sınırsız erişimin sağlanacağına ilişkin hüküm",
     "Mesleki sorumluluk sigortası yapılacağına ilişkin hüküm",
     "Sözleşmenin ancak mevzuat uyarınca feshedilebileceğine ilişkin hüküm"],
    "m. 29/1 ekip, süre ve ücret dökümü, sınırsız erişim, sigorta ve feshin mevzuata bağlı olduğu hükümlerini asgari içerik "
    "sayar. m. 29/2'ye göre sözleşmede denetim hizmeti dışında başka bir hizmet yapılması öngörülemez.")

P.q("BDY m. 29/3",
    "Bir anonim şirketin genel kurulu 15 Mart'ta denetim kuruluşunu seçmiş, ancak şirket kuruluşun yazılı ihtarına rağmen "
    f"sözleşme imzalamaktan kaçınmıştır. {B} bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sözleşme seçimden itibaren en geç 60 gün içinde yapılmalı; yapılmazsa kuruluş izleyen 10 gün içinde Kuruma bildirir.",
    ["Sözleşme 30 gün içinde yapılmalı; yapılmazsa kuruluş durumu ticaret sicil müdürlüğüne bildirir.",
     "Sözleşme 90 gün içinde yapılmalı; yapılmazsa seçim kararı kendi kendine hükümsüz olur.",
     "Sözleşme 60 gün içinde yapılmalı; yapılmazsa kuruluş denetimi sözleşmesiz yürütür.",
     "Sözleşme süresi genel kurul kararında belirlenir; kaçınma hâlinde kuruluş mahkemeye başvurur."],
    "m. 29/3'e göre sözleşme, denetimi üstlenenin seçiminden itibaren en geç 60 gün içinde yapılır; bu sürede yazılı ihtara "
    "rağmen işletme sözleşme yapmaktan kaçınırsa denetimi üstlenen durumu izleyen 10 gün içinde Kuruma bildirir.")

P.q("BDY m. 29/4-5",
    f"{B}, denetim sözleşmesinin feshi ile ilgili aşağıdakilerden hangisi yanlıştır?",
    "Denetimi üstlenen, sözleşmeyi dönem sonundan en az otuz gün önce bildirmek şartıyla gerekçesiz feshedebilir.",
    ["Denetimi üstlenen, sözleşmeyi sadece haklı bir sebep varsa veya görevden alınma davası açılmışsa feshedebilir.",
     "Fesih ve gerekçeleri denetimi üstlenen tarafından yazılı olarak 10 gün içerisinde Kuruma bildirilir.",
     "Fesih hâlinde çalışma notları ve gerekli tüm bilgiler yerine geçecek denetimi üstlenene teslim edilir.",
     "Denetim görevi, TTK m. 399/4'te öngörüldüğü şekilde ve başka bir denetçi atanmışsa geri alınabilir."],
    "m. 29/4'e göre görev sadece TTK m. 399/4'teki şekilde ve başka denetçi atanmışsa geri alınabilir; denetimi üstlenen "
    "sözleşmeyi sadece haklı sebeple veya görevden alınma davası açılmışsa fesheder ve 10 gün içinde Kuruma bildirir. "
    "m. 29/5 çalışma notlarının teslimini zorunlu kılar. Gerekçesiz fesih öngörülmemiştir.")

# ================================================================ raporlama ve olaylar (m. 30-31)
P.q("BDY m. 30/2",
    "Denetçi yeterli ve uygun denetim kanıtı elde etmiş; ticari alacaklarda önemli bir değerleme aykırılığı tespit etmiştir. "
    f"Aykırılık önemlidir, ancak finansal tabloların genelini etkilememektedir. {B} denetim raporunun görüş başlığı "
    "altında hangi görüş verilir?",
    "Sınırlı olumlu görüş",
    ["Olumlu görüş", "Olumsuz görüş", "Görüş bildirmekten kaçınıldığına ilişkin görüş", "Şartlı olumlu görüş"],
    "m. 30/2-b'ye göre önemli uyumsuzluklar bulunduğu ya da yeterli kanıt toplanamadığı, ancak bunların denetim konusunun "
    "genelini etkilemediği durumlarda sınırlı olumlu görüş verilir. Genelini etkileyen aykırılıkta olumsuz görüş, genelini "
    "etkileyen kanıt eksikliğinde görüş bildirmekten kaçınma söz konusudur.")

P.q("BDY m. 30/3",
    f"Türk Ticaret Kanunu uyarınca yapılan bir denetimde {B} denetim raporu denetlenen işletmenin yönetim organına en geç "
    "ne zaman teslim edilmelidir?",
    "Olağan genel kuruldan en az 20 gün önce ve Kanundaki azami sürenin sonuna kadar",
    ["Olağan genel kuruldan en az 15 gün önce",
     "Hesap döneminin kapanışını izleyen dördüncü ayın sonuna kadar",
     "Olağan genel kuruldan en az 30 gün önce ve her hâlükârda hesap dönemini izleyen mayıs ayının sonuna kadar",
     "Genel kurul toplantı ilanıyla aynı gün"],
    "m. 30/3'e göre TTK uyarınca yapılan denetimlerde rapor, finansal tabloların ait olduğu döneme ilişkin olağan genel "
    "kurul toplantısından en az 20 gün önce ve her durumda Kanunda olağan genel kurul için öngörülen azami sürenin sonuna "
    "kadar yönetim organına teslim edilir.")

# ================================================================ ücret, sigorta, bildirim, saklama (m. 32-35)
P.q("BDY m. 32",
    f"{B}, denetim ücretiyle ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetlenen işletmeye izin verilen vergi danışmanlığı hizmeti de veriliyorsa denetim ücreti buna göre indirilebilir.",
    ["Denetim ücreti denetimin bağımsızlığını, tarafsızlığını ve kalitesini sağlayacak şekilde belirlenir.",
     "Denetim hizmetleri için Kurum tarafından ilgili yıl için ücret tarifeleri belirlenebilir.",
     "Tarife belirlenmemiş yıllarda önceki yıl tutarları, Hazine ve Maliye Bakanlığınca ilan edilen yeniden değerleme oranında artırılarak uygulanır.",
     "Kurumca belirlenen ücret tarifesine uyulmaması uyarı yaptırımı gerektiren hâller arasındadır."],
    "m. 32/1'e göre ücret bağımsızlık, tarafsızlık ve kaliteyi sağlayacak şekilde belirlenir ve izin verilen hizmetlerin "
    "sağlanması durumunda denetim ücreti bundan etkilenmez. m. 32/2-3 tarife ve yeniden değerleme kuralını düzenler; "
    "m. 40/1-ı tarifeye uyulmamasını uyarı sebebi sayar.")

P.q("BDY m. 34",
    f"{B}, denetim kuruluşlarının Kuruma yapacağı bildirimlerin süreleriyle ilgili aşağıdakilerden hangisi yanlıştır?",
    "Sicil bilgilerindeki değişiklikler, değişikliği izleyen günden itibaren en geç 30 gün içinde bildirilir.",
    ["Denetim sözleşmeleri ve denetim raporları imza tarihinden itibaren en geç 30 gün içinde bildirilir.",
     "TTK m. 399 uyarınca görevden alma ve fesih işlemleri işlem tarihini izleyen günden itibaren en geç 10 gün içinde bildirilir.",
     "Mesleki sorumluluk sigortası poliçesi düzenlenme tarihini izleyen günden itibaren en geç 30 gün içinde bildirilir.",
     "Son takvim yılına ait gelirler Kurumca belirlenen şekle uygun olarak mayıs ayının on beşinci günü sonuna kadar bildirilir."],
    "m. 34/1-a'ya göre sicil bilgileri dahil Kuruma bildirilmiş bilgilerdeki değişiklikler izleyen günden itibaren en geç 10 "
    "gün içinde bildirilir. Sözleşme ve raporlar 30 gün, görevden alma ve fesih 10 gün, sigorta poliçesi 30 gün içinde; "
    "gelirler 15 Mayıs sonuna kadar bildirilir.", zorluk="hard")

P.sayisal("BDY m. 35/1",
    f"{B}, denetim kuruluşları ticari defterlerini, düzenlenen denetim raporlarını ve denetim çalışmalarına ve kalite "
    "yönetim sistemine ilişkin her türlü belgeyi ekleriyle birlikte kaç yıl süreyle saklamak zorundadır?",
    "10", ["3", "5", "7", "15"],
    "m. 35/1'e göre denetim kuruluşları ve denetim üstlenen bağımsız denetçiler bu belgeleri elektronik ortamda "
    "tutulanlar dahil on yıl süreyle saklar ve m. 35/2 uyarınca Kurum görevlilerine ibraz eder.", zorluk="easy")

# ================================================================ şeffaflık ve TTK yükümlülükleri (m. 36-37)
P.q("BDY m. 36",
    f"{B}, şeffaflık raporuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Rapor, kuruluşun sorumlu denetçilerinden biri tarafından imzalanarak yayımlanır.",
    ["Bir takvim yılında KAYİK denetimi yapan kuruluşlar raporu izleyen yılın dördüncü ayı sonuna kadar Kuruma bildirir.",
     "Rapor, bir önceki yılda denetim hizmeti verilen KAYİK'lerin listesini içerir.",
     "Rapor ile güncellenmiş hâlleri ayrı ayrı beş yıl süreyle kamunun erişimine açık tutulur.",
     "KAYİK listesinde olup yıl içinde KAYİK denetimi yapmayan kuruluşlar bunu internet sitelerinde açıklar."],
    "m. 36/1'e göre rapor, KAYİK denetimi yapılan takvim yılını izleyen dördüncü ayın sonuna kadar bildirilir ve internet "
    "sitesinde yayımlanır; m. 36/2'ye göre yönetim organı başkanı tarafından imzalanır ve KAYİK listesini içerir. "
    "m. 36/4 KAYİK denetimi yapmayanların açıklamasını, m. 36/5 beş yıllık erişim süresini düzenler.")

# ================================================================ inceleme ve yaptırımlar (m. 38-45)
P.q("BDY m. 38/3",
    "Kurumun kalite güvence sistemi kapsamında yaptığı incelemeler, ilk denetim sözleşmesi imza tarihinden itibaren "
    f"KAYİK'leri denetleyen kuruluşlar için asgari (i)----, diğerleri için asgari (ii)---- yapılır.\n\n{B} boşluklara "
    "sırasıyla aşağıdakilerden hangisi gelmelidir?",
    "(i) üç yılda bir (ii) altı yılda bir",
    ["(i) iki yılda bir (ii) dört yılda bir", "(i) üç yılda bir (ii) beş yılda bir", "(i) yılda bir (ii) üç yılda bir",
     "(i) altı yılda bir (ii) on yılda bir"],
    "m. 38/3'e göre incelemeler KAYİK'leri denetleyen kuruluşlar için asgari üç yılda bir, diğerleri için asgari altı yılda "
    "bir yapılır; izleyen incelemelerde süre önceki incelemeye ilişkin Kurul kararını izleyen takvim yılından başlar. Denetim "
    "üstlenen bağımsız denetçilerde Kurumca gerek görüldüğünde inceleme yapılır.")

P.q("BDY m. 39/1",
    f"{B}, “faaliyetlerinde düzeltilmesi gereken mevzuata aykırılıkların bulunduğu hususunun denetim kuruluşları ve "
    "denetçilere bildirilmesi” şeklinde tanımlanan idari yaptırım aşağıdakilerden hangisidir?",
    "Uyarı",
    ["İkaz", "Faaliyetin kısıtlanması", "Faaliyet izninin askıya alınması", "Durdurma"],
    "m. 39/1-b uyarıyı düzeltilmesi gereken aykırılıkların bildirilmesi olarak tanımlar. İkaz ise faaliyetlerde daha dikkatli "
    "davranılması gerektiğinin bildirilmesidir (m. 39/1-a). Durdurma m. 43/9'da düzenlenen ayrı bir tedbirdir.", zorluk="easy")

P.q("BDY m. 39/A, 40, 40/A",
    f"{B}, aşağıdaki eşleştirmelerden hangisi aykırılık ile öngörülen yaptırım bakımından yanlıştır?",
    "Mesleki sorumluluk sigortasının yaptırılmaması – faaliyet izninin askıya alınması",
    ["Yazılı bağımsızlık taahhüdünün alınmamış olması – ikaz",
     "Şeffaflık raporunun zamanında Kuruma bildirilmemesi – uyarı",
     "Reklam yasağına uyulmaması – faaliyetin kısıtlanması",
     "Haksız rekabete ilişkin hükümlere aykırı hareket edilmesi – faaliyetin kısıtlanması"],
    "m. 39/A-b yazılı taahhüdün alınmamasını ikaz; m. 40/1-e sigortanın yaptırılmamasını, m. 40/1-g şeffaflık raporuna "
    "aykırılığı uyarı; m. 40/A-b ve c reklam yasağı ile haksız rekabet aykırılıklarını faaliyetin kısıtlanması sebebi sayar.",
    zorluk="hard")

P.q("BDY m. 41",
    f"{B}, aşağıdaki aykırılıklardan hangisi faaliyet izninin askıya alınmasını gerektiren hâller arasında yer alır?",
    "Denetlenen işletmeye tasdik, vergi danışmanlığı ve vergi denetimi dışında hizmet verilmesi",
    ["Kuruma yapılacak bildirimlerin zamanında yerine getirilmemesi",
     "Yetki belgesinin kasten yanıltıcı beyanla alınması",
     "Kalite yönetim sisteminin etkin bir şekilde işletilmemesi",
     "Kurumca belirlenen ücret tarifesine uyulmaması"],
    "m. 41/1-d m. 22/5'e aykırı hizmet verilmesini askı sebebi sayar. Bildirim, kalite yönetim sistemi ve ücret tarifesi "
    "aykırılıkları m. 40'a göre uyarı; yetki belgesinin kasten yanıltıcı beyanla alınması m. 42/1-b'ye göre iptal sebebidir.")

P.q("BDY m. 41, 42",
    "Faaliyet izni, bağımsızlık kurallarına aykırılık nedeniyle bir yıl süreyle askıya alınan ve bu yaptırım kesinleşen bir "
    f"denetim kuruluşu, kesinleşmeden on dört ay sonra aynı fiili tekrar işlemiştir. {B} bu duruma ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "İki yıl içinde tekerrür gerçekleştiğinden faaliyet izni süresiz olarak iptal edilir.",
    ["Tekerrür için üç yıl gerektiğinden faaliyet izni yeniden iki yıla kadar askıya alınır.",
     "Faaliyet izni iptal edilir, ancak kuruluş bir yıl sonra yeniden yetkilendirme başvurusu yapabilir.",
     "Fiilin ikinci kez işlenmesi faaliyetin kısıtlanması yaptırımını gerektirir.",
     "Askı süresi bittiğinden tekerrür hükümleri uygulanmaz; uyarı yaptırımı verilir."],
    "m. 42/1-a'ya göre askıyı gerektiren fiilin yaptırımın kesinleşmesinden itibaren iki yıl içinde tekerrürü iptal "
    "sebebidir. m. 42/2'ye göre izni (c) bendi dışındaki nedenlerle iptal edilenler yeniden yetkilendirme başvurusunda "
    "bulunamaz.", zorluk="hard")

P.q("BDY m. 43",
    f"{B}, idari yaptırımlara ilişkin diğer hükümlerle ilgili aşağıdakilerden hangisi yanlıştır?",
    "Kurul kararlarına tebliğden itibaren otuz gün içinde Kurul nezdinde itiraz edilebilir.",
    ["İlgililere savunma yapmaları için on günden az olmamak üzere süre verilir.",
     "Kurul, fiilin ağırlığını dikkate alıp gerekçesini belirterek daha hafif bir yaptırım uygulayabilir.",
     "Kurul kararları ilgilinin siciline işlenir.",
     "Kurul, belirli hâllerde denetim faaliyetini en fazla bir yıl süreyle durdurabilir."],
    "m. 43/2 on günlük asgari savunma süresini, m. 43/3 daha hafif yaptırım yetkisini düzenler. m. 43/4'e göre yargı yolu "
    "açık olmak üzere Kurul kararları kesindir, itiraz edilemez ve sicile işlenir. m. 43/9 en fazla bir yıllık durdurmayı "
    "öngörür.")

# ================================================================ öncüllü ve karma
P.oncul("BDY m. 23, 24, 26",
    f"{B} denetim kuruluşları için aşağıdaki durumlar değerlendirilmektedir:",
    ["Kuruluş, mesleki konularda ücretli bir eğitim programı düzenlemektedir.",
     "Kuruluş, mevcut iş yükü nedeniyle sağlıklı biçimde yürütemeyeceği bir denetimi kabul etmiştir.",
     "Kuruluş, tabelasında akademik ve mesleki unvanları dışında “Türkiye'nin lider denetim şirketi” ifadesine yer vermiştir.",
     "Kuruluş, denetlediği işletmenin muhasebe müdürü pozisyonu için gazetede ilan vermiştir."],
    "Yukarıdakilerden hangileri Yönetmeliğe aykırıdır?",
    "II ve III",
    ["I ve II", "II ve III", "III ve IV", "I, II ve III", "II, III ve IV"],
    "m. 23/2 eğitim vermeye ve denetlenen işletmeler için eleman ilanına izin verir (I ve IV uygundur). m. 26/1-e iş yükü "
    "nedeniyle sağlıklı yürütülemeyecek denetimi yasaklar (II). m. 23/1 tabela ve basılı kâğıtlarda mesleki ve akademik "
    "unvanlar dışında unvan veya sıfat kullanılmasını yasaklar (III).")

P.oncul("BDY m. 13/1, 14/1",
    f"{B} aşağıdaki şartlar değerlendirilmektedir:",
    ["Faaliyet izninin daha önce Kurum tarafından yetkilendirme şartlarının sonradan kaybedilmesi dışındaki bir nedenle "
     "iptal edilmemiş olması",
     "Faaliyet konusunun bağımsız denetime veya bununla birlikte 3568 sayılı Kanun kapsamındaki mesleki alana münhasır olması",
     "Türkiye'de yerleşik olması",
     "Denetçilerinin tam zamanlı ve asgari bir raporlama dönemi için istihdam edilmiş olması"],
    "Yukarıdakilerden hangileri hem denetim kuruluşlarının hem de denetçilerin yetkilendirilmesinde aranan şartlar "
    "arasındadır?",
    "Yalnız I",
    ["Yalnız I", "I ve III", "II ve IV", "I, II ve IV", "I, III ve IV"],
    "İznin m. 42/1-c dışındaki bir nedenle iptal edilmemiş olması şartı hem m. 13/1-l'de kuruluşlar hem m. 14/1-g'de "
    "denetçiler için aranır. Faaliyet konusu ve tam zamanlı istihdam m. 13/1'de sadece kuruluşlar için, Türkiye'de "
    "yerleşik olma m. 14/1-c'de sadece denetçiler için öngörülür.", zorluk="hard")

P.q("BDY m. 43/8-9",
    f"{B}, Kurulun denetim faaliyetini durdurma kararıyla ilgili aşağıdakilerden hangisi yanlıştır?",
    "Durdurma kararı süresi dolmadan kaldırılamaz; faaliyete sebep ortadan kalksa da en az bir yıl ara verilir.",
    ["Denetçinin gaiplik veya kısıtlılık gibi nedenlerle fiil ehliyetini kaybetmesi durdurma sebebidir.",
     "Faaliyete devamın telafisi zor zararlara yol açacağı ihtimali varsa ilk değerlendirme sonucunda durdurma kararı verilebilir.",
     "Denetim faaliyeti durdurulanlar karar devam ettiği sürece yeni sözleşme yapamaz ve denetimlerde görev alamaz.",
     "Kurul, devam eden denetim işlerinin tamamlanmasıyla sınırlı olarak faaliyetin devamına karar verebilir."],
    "m. 43/9'a göre faaliyet en fazla bir yıl süreyle durdurulabilir; m. 43/10'a göre gerekli idari işlemin tesisi veya "
    "sebebin sona ermesi hâlinde sürenin dolması beklenmeksizin karar kaldırılır. m. 43/8 yeni sözleşme yasağını ve devam "
    "eden işlerle sınırlı istisnayı düzenler.", zorluk="hard")

if __name__ == "__main__":
    sys.exit(P.yaz())
