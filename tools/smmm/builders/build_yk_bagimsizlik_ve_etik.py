# -*- coding: utf-8 -*-
"""Muhasebe Denetimi · Bağımsızlık ve Etik — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında etik ve kalite yönetimi soruları; temel ilkelerin tanımı,
mevzuatın daha kısıtlayıcı olduğu durum, KYS 1 unsurları ve nihai sorumluluk, KYS 2 kalitenin
gözden geçirilmesi üzerine kuruludur.

Dayanak (28.09.2026 kontrolü, kgk.gov.tr güncel metinler):
  · Bağımsız Denetçiler İçin Etik Kurallar (Bağımsızlık Standartları Dâhil), 11.08.2025 tarihli güncel metin
  · KYS 1 Bağımsız Denetim Şirketleri İçin Kalite Yönetimi; KYS 2 Denetimin Kalitesinin Gözden Geçirilmesi
    (KGK Ocak 2023 duyurusu; 31.12.2023'ten itibaren uygulanır)
Bağımsızlığa ilişkin Yönetmelik hükümleri build_yk_bagimsiz_denetim_yonetmeligi.py'dedir; burada sadece
Etik Kurallarla karşılaştırmalı olarak kullanılır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_bagimsizlik_ve_etik_2026.json", lesson="denetim", topic="bagimsizlik_ve_etik",
          konu_adi="Bağımsızlık ve Etik", seed=2026092842,
          surum="Bağımsız Denetçiler İçin Etik Kurallar (11.08.2025 metni); KYS 1 ve KYS 2; 28.09.2026 kontrolü")

E = "Bağımsız Denetçiler İçin Etik Kurallar (Bağımsızlık Standartları Dâhil)’a göre"
K1 = "Kalite Yönetim Standardı 1’e (KYS 1) göre"
K2 = "Kalite Yönetim Standardı 2’ye (KYS 2) göre"

# ================================================================ temel ilkeler
P.q("Etik Kurallar 110.1 U1",
    f"{E}, aşağıdakilerden hangisi denetçiler için belirlenen beş temel etik ilkeden biri değildir?",
    "Bağımsızlık",
    ["Dürüstlük", "Mesleki yeterlik ve özen", "Sır saklama (gizlilik)", "Mesleğe uygun davranış"],
    "Etik Kurallar 110.1 U1 beş temel ilkeyi dürüstlük, tarafsızlık, mesleki yeterlik ve özen, sır saklama ve mesleğe "
    "uygun davranış olarak sayar. Bağımsızlık ayrı bir ilke değildir; Bağımsızlık Standartlarında düzenlenir ve "
    "tarafsızlık ile dürüstlük ilkeleriyle bağlantılıdır.", zorluk="easy")

P.q("Etik Kurallar 110.1 U1-b",
    "Bir denetçi, müşterinin kullandığı yapay zekâ destekli bir değerleme aracının sonuçlarını hiçbir sorgulama yapmadan "
    f"kabul etmiş ve kendi muhakemesini bu araca bırakmıştır. {E} bu davranış öncelikle hangi temel ilkeye uyumu "
    "zedeler?",
    "Tarafsızlık",
    ["Sır saklama", "Mesleğe uygun davranış", "Dürüstlük", "Bağımsızlık"],
    "110.1 U1-b'ye göre tarafsızlık; muhakeme ve kararları önyargı ve temayüllerden, çıkar çatışmalarından ve bireyler, "
    "kuruluşlar, teknoloji veya diğer etkenlere gereğinden fazla güvenilmesinden ya da bunların nüfuzlarının kötüye "
    "kullanılmasından etkilenmeden uygulamaktır. Teknolojiye aşırı güven bu unsurun kapsamındadır.", zorluk="hard")

P.q("Etik Kurallar 110.1 U1-d",
    "(i) İlgili mevzuata uymak, (ii) tüm mesleki faaliyetlerde ve iş ilişkilerinde denetim mesleğinin kamu yararına hareket "
    "etme sorumluluğuyla tutarlı olacak şekilde davranmak ve (iii) mesleğin itibarını zedeleyici tutum ve davranışlardan "
    f"kaçınmak.\n\n{E} yukarıdaki unsurlar hangi temel ilkeyi oluşturur?",
    "Mesleğe uygun davranış",
    ["Dürüstlük", "Mesleki yeterlik ve özen", "Tarafsızlık", "Sır saklama"],
    "110.1 U1-d'ye göre mesleğe uygun davranış; ilgili mevzuata uymayı, kamu yararına hareket etme sorumluluğuyla tutarlı "
    "davranmayı ve mesleğin itibarını zedeleyici tutum ve davranışlardan kaçınmayı içerir.", zorluk="easy")

P.q("Etik Kurallar A114.2",
    f"{E}, sır saklama ilkesiyle ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Gizli bir bilgi kamuya açık hâle geldiğinde denetçi bu bilgiyi serbest olarak kullanabilir.",
    ["Denetçi, mesleğin icrası sırasında edindiği gizli bilgileri kendisinin veya üçüncü kişilerin çıkarına kullanamaz.",
     "Sır saklama yükümlülüğü, müşteriyle ilişki sona erdikten sonra da devam eder.",
     "Gizliliğin korunması, bilgilerin toplanması, saklanması ve mevzuata uygun imhası sırasında uygun adımları içerir.",
     "Gizli bilgilerin açıklanması için yasal veya mesleki bir hak ya da görevin bulunduğu durumlar saklıdır."],
    "A114.2'ye göre denetçi gizli bilgileri açıklayamaz, kendisinin veya üçüncü kişilerin çıkarına kullanamaz, ilişki "
    "sona erdikten sonra da kullanamaz ve bu bilgiler uygun veya uygun olmayan şekilde kamuya açık hâle gelmiş olsa da "
    "kullanamaz veya açıklayamaz. 114.1 U1 gizliliğin bilgi yaşam döngüsü boyunca korunmasını ister.")

P.q("Etik Kurallar 100.1",
    "Bir ülkenin mevzuatı, Etik Kurallarda belirli şartlarla izin verilen bir hizmetin denetim müşterisine sunulmasını "
    f"istisnasız biçimde yasaklamaktadır. {E} denetçinin bu durumda izlemesi gereken yol aşağıdakilerden hangisidir?",
    "Daha kısıtlayıcı olan mevzuata uyar; Kuralların diğer hükümlerine de uymaya devam eder.",
    ["Etik Kurallar uluslararası standart olduğundan Kuralların izin verdiği şekilde hareket eder.",
     "Durumu üst yönetimden sorumlu olanlara açıklayarak hizmeti Kurallara uygun biçimde sunar.",
     "Hizmeti sunar, ancak bağımsızlık tehdidini azaltan önlemleri yazılı olarak kayda alır.",
     "Hangi düzenlemenin uygulanacağına ilişkin görüş almak üzere KGK'ya başvurur ve cevabı bekler."],
    "Etik Kurallar 100.1'e göre mevzuatın Kurallardaki hükümlerden daha kısıtlayıcı hükümler öngörmesi hâlinde denetçi "
    "söz konusu mevzuata uymak zorundadır; Kuralların belirli hükümlerine uyulması mevzuatla yasaklanmışsa denetçi "
    "Kuralların diğer bütün hükümlerine uyar.")

P.q("Etik Kurallar 110.2 U2",
    "Bir denetçi, bir temel ilkeye uymasının başka bir temel ilkeyle çatışmasına yol açtığı bir durumla karşılaşmıştır. "
    f"{E} bu duruma ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denetçinin danıştığı kişi, çatışmanın çözümüne ilişkin sorumluluğu da üstlenmiş olur.",
    ["Denetçi gerektiğinde herhangi bir isim vermeksizin denetim şirketindeki diğer kişilere danışabilir.",
     "Denetçi üst yönetimden sorumlu olanlara, yetkili mercie veya bir hukuk müşavirine danışmayı değerlendirebilir.",
     "Mevzuatla yasaklanmadıkça denetçi gerektiğinde çatışmaya yol açan hususla ilişkisini sonlandırabilir.",
     "Denetçi çatışmayı çözmek için mesleki muhakemede bulunma sorumluluğunu taşımaya devam eder."],
    "110.2 U2'ye göre denetçi gerektiğinde isim vermeksizin şirket içindeki kişilere, üst yönetimden sorumlu olanlara, "
    "yetkili mercie, düzenleyici otoriteye veya hukuk müşavirine danışabilir. Ancak danışmanlık, denetçinin mesleki "
    "muhakemede bulunma veya gerektiğinde ilişkisini sonlandırma sorumluluğunu ortadan kaldırmaz.")

# ================================================================ kavramsal çerçeve ve tehditler
P.q("Etik Kurallar A120.3",
    f"{E}, denetçinin temel ilkelere uyumu engelleyen tehditler karşısında kavramsal çerçeveyi uygularken izlediği "
    "adımlar aşağıdakilerin hangisinde doğru sırayla verilmiştir?",
    "Tehditleri belirlemek, değerlendirmek ve kabul edilebilir düzeye indirerek ele almak",
    ["Tehditleri raporlamak, üst yönetimle görüşmek ve denetim sözleşmesini yeniden düzenlemek",
     "Önlemleri belirlemek, tehditleri ölçmek ve kalan tehdidi denetim raporunda açıklamak",
     "Tehditleri değerlendirmek, önlemleri Kuruma bildirmek ve onay alarak işe devam etmek",
     "Tehditleri belirlemek, kabul edilebilir düzeyde olup olmadığını üst yönetime sormak ve kayda almak"],
    "A120.3'e göre denetçi temel ilkelere uyumu engelleyen tehditleri belirlemek, değerlendirmek ve bunlara ilişkin önlem "
    "almak üzere kavramsal çerçeveyi uygular; tehditler ortadan kaldırılarak veya kabul edilebilir düzeye indirilerek ele "
    "alınır.")

P.q("Etik Kurallar 120.6 U3-b",
    "Bir denetim şirketi geçen yıl müşterisinin maliyet muhasebesi sistemini tasarlamış ve kurmuştur. Aynı şirket bu yıl, "
    f"bu sistemden elde edilen stok maliyetlerinin yer aldığı finansal tabloları denetlemektedir. {E} bu durum hangi "
    "tehdidi oluşturur?",
    "Kendi kendini denetleme tehdidi",
    ["Taraf tutma tehdidi", "Yakınlık tehdidi", "Yıldırma tehdidi", "Kişisel çıkar tehdidi"],
    "120.6 U3-b'ye göre kendi kendini denetleme tehdidi, denetçinin kendisi veya şirketindeki bir başka kişi tarafından "
    "varılan bir yargının ya da gerçekleştirilen bir faaliyetin sonuçlarını cari dönemdeki çalışmasında dayanak olarak "
    "kullanırken bu sonuçları uygun şekilde değerlendirememesi tehdididir.")

P.q("Etik Kurallar 120.6 U3-d",
    "Denetlenen şirketin genel müdürü, sorumlu denetçiye ertelenmiş vergi varlığının muhasebeleştirilmesine itiraz "
    f"etmesi hâlinde gelecek yıl denetçinin değiştirileceğini söylemiştir. {E} bu durum hangi tehdidi oluşturur?",
    "Yıldırma tehdidi",
    ["Kendi kendini denetleme tehdidi", "Taraf tutma tehdidi", "Yakınlık tehdidi", "Kişisel çıkar tehdidi"],
    "120.6 U3-d'ye göre yıldırma tehdidi, başkalarının nüfuzlarını kötüye kullanma çabaları dahil, denetçinin mevcut veya "
    "hissettiği baskılar nedeniyle tarafsız hareket edebilmesinin engellenmesi tehdididir. Denetçinin görevden alınması "
    "tehdidi bu türün tipik örneğidir.", zorluk="easy")

P.q("Etik Kurallar 120.6 U3-c",
    "Bir denetim şirketinin ortağı, denetim müşterisinin vergi idaresiyle yaşadığı uyuşmazlıkta müşterinin savunmasını "
    f"üstlenerek onun tezini vergi mahkemesi önünde desteklemektedir. {E} bu durum öncelikle hangi tehdidi oluşturur?",
    "Taraf tutma tehdidi",
    ["Yakınlık tehdidi", "Yıldırma tehdidi", "Kendi kendini denetleme tehdidi", "Kişisel çıkar tehdidi"],
    "120.6 U3-c'ye göre taraf tutma tehdidi, denetçinin bir müşterinin pozisyonunu kendi tarafsızlığından taviz verecek "
    "şekilde desteklemesi tehdididir. Müşteriyi bir uyuşmazlıkta savunmak bu tehdidin örneğidir.")

P.q("Etik Kurallar 120.6 U3-ç",
    f"{E}, “yakınlık tehdidi” aşağıdakilerden hangisinde doğru tanımlanmıştır?",
    "Uzun süreli veya yakın ilişki nedeniyle müşterinin çıkarları lehine fazlasıyla temayül gösterme tehdidi",
    ["Finansal veya finansal olmayan bir çıkarın denetçinin muhakemesini uygun olmayan şekilde etkilemesi tehdidi",
     "Denetçinin kendi yargısının sonuçlarını cari dönemde uygun şekilde değerlendirememesi tehdidi",
     "Denetçinin bir müşterinin pozisyonunu tarafsızlığından taviz verecek şekilde desteklemesi tehdidi",
     "Denetçinin mevcut veya hissettiği baskılardan dolayı tarafsız hareket edememesi tehdidi"],
    "120.6 U3-ç'ye göre yakınlık tehdidi, müşteriyle uzun süreli veya yakın ilişki nedeniyle denetçinin onun çıkarları "
    "lehine fazlasıyla temayül göstermesi veya çalışmalarına fazlasıyla kabul eder bir yaklaşım sergilemesi tehdididir. "
    "Diğer seçenekler sırasıyla kişisel çıkar, kendi kendini denetleme, taraf tutma ve yıldırma tehditlerini tanımlar.")

P.q("Etik Kurallar 120.6 U4",
    f"{E}, tehditlerle ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bir durum sadece tek bir tehdit türü oluşturur; bu tehdit de tek bir temel ilkeyi etkiler.",
    ["Tehditler kabul edilebilir düzeyde değilse denetçi bunları ortadan kaldırarak veya azaltarak ele alır.",
     "Tehditlerin düzeyi değerlendirilirken nicel etkenlerin yanında nitel etkenler de göz önünde bulundurulur.",
     "Birden fazla tehdidin bulunduğu durumlarda bunların toplam etkisi değerlendirmeyle ilgilidir.",
     "Denetim müşterisinin ücret ödemesi kişisel çıkar tehdidi yanında yıldırma tehdidi de oluşturabilir."],
    "120.6 U4'e göre bir durum birden fazla tehdit oluşturabilir ve bir tehdit birden fazla temel ilkeye uyumu "
    "etkileyebilir. 120.8 U1 nicel ve nitel etkenleri ve toplam etkiyi, 410.4 U1 ücretin kişisel çıkar ve yıldırma "
    "tehdidi oluşturabileceğini düzenler.")

P.q("Etik Kurallar 120.7 U1, 120.5 U9",
    f"{E}, tehditlerin “kabul edilebilir düzey”de olup olmadığının belirlenmesine ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Makul üçüncü taraf testini kullanan denetçinin temel ilkelere uyduğu sonucuna varmasının daha muhtemel olduğu düzeydir.",
    ["Denetlenen işletmenin üst yönetiminin, denetçinin tarafsızlığından şüphe duymadığını yazılı olarak beyan ettiği düzeydir.",
     "Denetim şirketinin kalite yönetim sisteminde her tehdit türü için sayısal olarak belirlenen eşiğin altındaki düzeydir.",
     "Tehdidin ortadan kalktığının, bir başka denetim şirketinden alınan görüşle teyit edildiği düzeydir.",
     "Kurumun inceleme sonuçlarında aykırılık tespit edilmemiş olması hâlinde ulaşılmış kabul edilen düzeydir."],
    "120.7 U1'e göre kabul edilebilir düzey, gerekli bilgiye sahip makul üçüncü taraf testini kullanan bir denetçinin "
    "temel ilkelere uyduğu sonucuna varmasının daha muhtemel olduğu düzeydir. Bu test, aynı sonuca başka bir tarafça "
    "ulaşılmasının muhtemel olup olmadığına ilişkin değerlendirmedir (120.5 U9).", zorluk="hard")

P.q("Etik Kurallar 120.5 U9",
    f"{E}, “gerekli bilgiye sahip makul üçüncü taraf” ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Değerlendirmenin geçerli olması için bu üçüncü tarafın da bağımsız denetçi olması gerekir.",
    ["Test, aynı sonuçlara başka bir tarafça ulaşılmasının muhtemel olup olmadığına ilişkin bir değerlendirmedir.",
     "Değerlendirme, denetçinin sonuca ulaştığı anda bildiği veya bilmesi beklenebilecek durum ve gerçekler esas alınarak yapılır.",
     "Üçüncü tarafın, denetçinin sonuçlarının uygunluğunu tarafsız anlayacak bilgi ve deneyime sahip olması gerekir.",
     "Değerlendirme, denetçi tarafından bu üçüncü tarafın bakış açısıyla yapılır."],
    "120.5 U9'a göre gerekli bilgiye sahip makul üçüncü tarafın denetçi olması gerekmez; ancak denetçinin sonuçlarının "
    "uygunluğunu tarafsız biçimde anlamak ve değerlendirmek için ilgili bilgi ve deneyime sahip olması gerekir.")

P.q("Etik Kurallar 120.15 U1",
    f"{E}, bağımsızlığın unsurlarıyla ilgili aşağıdakilerden hangisi doğrudur?",
    "Esasta bağımsızlık, muhakemeyi olumsuz etkileyebilecek tesirlerden ari olarak görüş açıklamaktır.",
    ["Şekilde bağımsızlık, denetçinin denetlenen işletmeyle ticari ilişkisinin bulunmaması demektir.",
     "Esasta bağımsızlık, makul üçüncü kişilerde tarafsızlıktan ödün verildiği intibaının oluşmamasıdır.",
     "Bağımsızlık, sır saklama ve mesleki yeterlik ilkeleriyle bağlantılı ayrı bir temel ilkedir.",
     "Şekilde bağımsızlık sadece denetim ekibinin üyeleri için aranır, denetim şirketi için ayrıca aranmaz."],
    "120.15 U1'e göre bağımsızlık esasta bağımsızlık (mesleki muhakemeyi olumsuz etkileyebilecek tesirlerden ari olarak "
    "görüş açıklama) ve şekilde bağımsızlıktan (makul ve bilgi sahibi üçüncü kişilerde ödün verildiği intibaını "
    "oluşturabilecek durumlardan sakınma) oluşur; tarafsızlık ve dürüstlük ilkeleriyle bağlantılıdır ve şirket, denetçi ve "
    "ekip üyeleri için aranır.")

P.q("Etik Kurallar 120.16",
    f"{E}, mesleki şüphecilik ile temel ilkeler arasındaki ilişkiye dair aşağıdakilerden hangisi doğrudur?",
    "Temel ilkelere uyum, finansal tablo denetiminde mesleki şüpheciliğin kullanılmasını destekler.",
    ["Mesleki şüphecilik sadece hile riskinin yüksek olduğu denetimlerde kullanılan ayrı bir temel ilkedir.",
     "Mesleki şüphecilik ile temel ilkeler birbirinden bağımsız olup aralarında bir ilişki kurulmamıştır.",
     "Mesleki şüphecilik, müşterinin sunduğu tüm belgelerin sahte olduğu varsayımıyla hareket etmeyi gerektirir.",
     "Temel ilkelere uyum sağlanmışsa denetçinin ayrıca mesleki şüphecilik kullanmasına gerek kalmaz."],
    "120.16 U1-U2'ye göre denetçiler bağımsız denetimleri planlarken ve yürütürken mesleki şüpheciliği kullanmak "
    "zorundadır; mesleki şüphecilik ve temel ilkeler birbiriyle ilişkili kavramlardır ve temel ilkelere uyum mesleki "
    "şüpheciliğin kullanılmasını destekler.")

# ================================================================ ücretler, hediye, iletişim
P.q("Etik Kurallar 410.8 U1, A410.9",
    "Bir denetim şirketi, müşterisiyle yaptığı sözleşmede denetim ücretinin bir kısmının, şirketin yıl sonunda banka "
    f"kredisi alabilmesi için gerekli olumlu görüşün verilmesi hâlinde ödenmesini kararlaştırmıştır. {E} bu ücret "
    "düzenlemesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Şarta bağlı ücrettir; denetim işiyle ilgili doğrudan veya dolaylı şarta bağlı ücret talep edilemez.",
    ["Şarta bağlı ücrettir; önlemler alınıp kayda geçirilirse denetim işinde de uygulanabilir.",
     "Ücret mahkeme kararına dayanmadığı için şarta bağlı ücret sayılmaz ve kabul edilebilir.",
     "Ücretin sadece bir kısmı koşula bağlandığından bağımsızlığa yönelik bir tehdit oluşmaz.",
     "Şarta bağlı ücrettir; üst yönetimden sorumlu olanlar yazılı onay verirse denetim işinde de talep edilebilir."],
    "410.8 U1'e göre şarta bağlı ücret, bir işlemin çıktısıyla veya sunulan hizmetin sonucuyla ilgili önceden belirlenmiş "
    "bir esasa göre hesaplanan ücrettir; mahkeme veya kamu idaresince belirlenen ücretler bu kapsamda değildir. A410.9'a "
    "göre denetim işiyle ilgili doğrudan veya dolaylı şarta bağlı ücret talep edilemez.")

P.q("Etik Kurallar A410.18, A410.20",
    "Bir denetim şirketinin KAYİK olan tek bir müşteriden aldığı toplam ücretler, birbirini izleyen yıllarda şirketin "
    f"toplam ücret gelirlerinin %15'ini aşmaktadır. {E} bu duruma ilişkin aşağıdakilerden hangisi yanlıştır?",
    "Durum birbirini izleyen üç yıl sürerse şirket üçüncü yıla ilişkin görüşü yayımladıktan sonra denetçiliği bırakır.",
    ["İki yıl üst üste aşılmışsa ikinci yılın görüşü yayımlanmadan önce yayımlanma öncesi incelemenin önlem olup olmadığı değerlendirilir.",
     "Yayımlanma öncesi inceleme, görüş bildiren şirketin üyesi olmayan bir denetçi tarafından yapılır.",
     "Durum beş yıl sürerse şirket kural olarak beşinci yılın görüşünü yayımladıktan sonra denetçiliği bırakır.",
     "Kamu yararı gereği mecburi bir sebep varsa düzenleyici kurumun mutabakatıyla hizmet sürdürülebilir."],
    "A410.18'e göre iki yılın her birinde %15 aşılırsa ikinci yılın görüşünden önce yayımlanma öncesi inceleme "
    "değerlendirilir. A410.20'ye göre durum birbirini takip eden beş yıl sürerse şirket beşinci yılın görüşünü "
    "yayımladıktan sonra denetçiliği bırakır; A410.21 düzenleyici kurumla mutabakat ve yayımlanma öncesi inceleme şartıyla "
    "istisna tanır. Üç yıllık bir sınır yoktur.", zorluk="hard")

P.q("Etik Kurallar A410.15",
    "KAYİK olmayan bir denetim müşterisinden alınan toplam ücretler, birbirini takip eden beş yılın her birinde denetim "
    f"şirketinin toplam ücretlerinin %35'ini oluşturmuştur. {E} şirketin atabileceği adımlardan biri aşağıdakilerden "
    "hangisidir?",
    "Şirket dışından bir denetçinin beşinci yılın denetim çalışmalarını gözden geçirmesi",
    ["Beşinci yıla ait görüşü yayımladıktan sonra müşterinin denetçiliğini bırakması",
     "Denetim ücretini, toplam gelirlerin %30'unun altına inecek şekilde indirmesi",
     "Ücret bağımlılığını denetim raporunda ayrı bir paragrafta açıklayarak görüşünü sınırlı olumlu olarak vermesi",
     "Müşterinin denetimini aynı denetim ağındaki başka bir şirkete devretmesi"],
    "A410.15'e göre KAYİK olmayan müşterilerde ücretler beş yıl üst üste %30'u aşarsa şirket, beşinci yılın görüşünden "
    "önce veya sonra şirket dışından bir denetçinin (ya da yetkili mercinin) beşinci yılın çalışmalarını gözden geçirmesinin "
    "önlem olup olamayacağına karar verir. Denetçiliği bırakma kuralı KAYİK müşteriler içindir (A410.20); ücreti indirmek "
    "kalite ve bağımsızlık bakımından ayrı bir tehdit yaratır.", zorluk="hard")

P.q("Etik Kurallar A420.3, 420.3 U2",
    "Denetim ekibindeki bir kıdemli denetçiye, denetim müşterisi bayram vesilesiyle ekibin tüm üyelerine gönderdiği "
    "logolu bir ajanda vermiştir. Aynı dönemde müşteri, sorumlu denetçiye de tartışmalı bir karşılık tutarı konuşulurken "
    f"küçük değerli bir hediye çeki sunmuştur. {E} bu iki durum için aşağıdakilerden hangisi doğrudur?",
    "Ajanda kabul edilebilir; hediye çeki küçük de olsa davranışı etkileme niyeti taşıdığından kabul edilemez.",
    ["İki hediye de küçük değerli olduğundan kabul edilebilir.",
     "İki hediye de denetim müşterisinden geldiği için değerine ve verilme amacına bakılmaksızın kabul edilemez.",
     "Ajanda kabul edilemez; hediye çeki değeri küçük olduğu için kabul edilebilir.",
     "Hediyeler üst yönetimden sorumlu olanlara bildirilir ve denetim dosyasında belgelenirse ikisi de kabul edilebilir."],
    "A420.3'e göre denetim şirketi ve ekip üyeleri, küçük ve önemsiz değerde olmadıkça müşterinin hediyesini kabul edemez. "
    "420.3 U2'ye göre davranışı uygunsuz şekilde etkileme niyeti bulunduğunda küçük ve önemsiz değerdeki hediyeler de "
    "kabul edilemez.", zorluk="hard")

P.q("Etik Kurallar 320.5 U1, A320.6",
    "Yeni bir denetim teklifi alan bir denetim şirketi, müşterinin önceki denetçisiyle görüşerek denetçi değişikliğinin "
    f"nedenlerini öğrenmek istemektedir. {E} bu görüşmeye ilişkin aşağıdakilerden hangisi doğrudur?",
    "Görüşmeye başlamak için genelde müşteriden, tercihen yazılı izin alınması gerekir.",
    ["Önceki denetçi, müşterinin izni aranmaksızın dosyasındaki her bilgiyi paylaşır.",
     "Görüşme sadece KGK aracılığıyla ve Kurumun yazılı izniyle yapılabilir.",
     "Önceki denetçiyle iletişim kurulamazsa teklif reddedilir; başka kaynaklardan bilgi alınamaz.",
     "Önceki denetçiyle görüşme, sır saklama ilkesi nedeniyle yapılamaz."],
    "320.5 U1'e göre işin teklif edildiği denetçinin mevcut veya önceki denetçiyle görüşmelere başlaması için genelde "
    "müşteriden, tercihen yazılı izin alması gerekir. A320.6'ya göre iletişime geçilemezse muhtemel tehditlere ilişkin "
    "bilgi başka adımlarla edinilir. Önceki denetçi talebi düzenleyen mevzuata uyar (A320.7).")

# ================================================================ rotasyon (KAYİK)
P.q("Etik Kurallar A540.5",
    f"{E}, KAYİK olan bir denetim müşterisinde kilit denetçilerin rotasyonuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bir kişi kilit denetçi rollerini, tek tek veya birlikte, kümülatif yedi yıldan fazla üstlenemez.",
    ["Rotasyon sadece sorumlu denetçi için öngörülmüş olup kaliteyi gözden geçiren kişiye uygulanmaz.",
     "Kilit denetçi, ardışık beş yıldan sonra bir yıl ara vererek aynı denetimde yeniden görev alabilir.",
     "Farklı kilit denetçi rollerinde geçen süreler birbirinden ayrı hesaplanır.",
     "Rotasyon süresi, müşterinin halka açık olduğu yıllar dikkate alınmadan on yıl olarak uygulanır."],
    "A540.5'e göre KAYİK denetiminde bir kişi kümülatif olarak yedi yıldan (azami denetlenebilir dönem) fazla sorumlu "
    "denetçi, kaliteyi gözden geçiren kişi veya diğer kilit denetçi rolünü ya da bunların bileşimini üstlenemez; ardından "
    "ara verme süresi geçirir.")

P.sayisal("Etik Kurallar A540.14",
    "KAYİK olan bir ortaklığın denetiminde yedi yıl boyunca sorumlu denetçi olarak görev yapan Hakan Bey, azami "
    f"denetlenebilir dönemi doldurmuştur. {E} Hakan Bey'in bu denetimden ayrı kalması gereken ara verme süresi "
    "birbirini takip eden kaç yıldır?",
    "5", ["1", "2", "3", "7"],
    "A540.14'e göre kişinin sorumlu denetçi sıfatıyla kümülatif olarak dört veya daha fazla yıl hizmet vermesi durumunda "
    "ara verme süresi birbirini takip eden beş yıldır. Kaliteyi gözden geçiren kişi olarak dört yıl veya fazlası için üç "
    "yıl (A540.15), diğer durumlarda iki yıl (A540.17) uygulanır.")

P.q("Etik Kurallar A540.15, A540.17",
    "KAYİK olan bir bankanın denetiminde Selin Hanım yedi yıl kaliteyi gözden geçiren kişi olarak, Burak Bey ise yedi yıl "
    f"sorumlu denetçi dışındaki bir kilit denetçi rolünde görev yapmıştır. {E} ara verme süreleri aşağıdakilerden "
    "hangisinde doğru verilmiştir?",
    "Selin Hanım üç yıl, Burak Bey iki yıl",
    ["Selin Hanım beş yıl, Burak Bey üç yıl", "Selin Hanım iki yıl, Burak Bey iki yıl",
     "Selin Hanım üç yıl, Burak Bey beş yıl", "Selin Hanım beş yıl, Burak Bey iki yıl"],
    "A540.15'e göre kaliteyi gözden geçiren kişi sıfatıyla kümülatif dört veya daha fazla yıl hizmet verende ara verme "
    "süresi birbirini takip eden üç yıl; A540.17'ye göre bunların dışındaki kilit denetçi rollerinde iki yıldır.", zorluk="hard")

P.q("Etik Kurallar A540.8",
    "Bir şirketin denetiminde dört yıldır sorumlu denetçi olarak görev yapan Nazlı Hanım'ın müşterisi, paylarının borsada "
    f"işlem görmeye başlamasıyla KAYİK hâline gelmiştir. {E} Nazlı Hanım rotasyona tabi tutulmadan önce bu sıfatla en "
    "fazla kaç yıl daha hizmet verebilir?",
    "Üç yıl",
    ["Bir yıl", "İki yıl", "Beş yıl", "Yedi yıl"],
    "A540.8'e göre müşteri KAYİK hâline geldiğinde önceki kilit denetçilik süresi beş yıl veya daha az ise kalan süre yedi "
    "yıldan hizmet verilen yıl sayısı çıkarılarak hesaplanır: 7 − 4 = 3 yıl. Önceki süre altı yıl veya daha fazlaysa üst "
    "yönetimden sorumlu olanların mutabakatıyla azami iki yıl daha hizmet verilebilir.", zorluk="hard")

P.q("Etik Kurallar Tanımlar",
    f"{E}, aşağıdakilerden hangisi “kilit denetçi” kapsamında yer almaz?",
    "Talimatla örnek seçen ve yeniden hesaplama yapan denetçi yardımcısı",
    ["Denetim raporunu şirket adına imzalayan sorumlu denetçi",
     "Denetimin kalitesinin gözden geçirilmesinden sorumlu kişi",
     "Önemli hususlarda kilit kararlar alan iş ekibindeki diğer ortaklar",
     "Önemli konularda muhakemede bulunan iş ekibindeki kilit yöneticiler"],
    "Etik Kurallar tanımlarına göre kilit denetçi; sorumlu denetçi, denetimin kalitesinin gözden geçirilmesinden sorumlu "
    "kişi ve görüş bildirilecek tabloların denetiminde önemli hususlarda kilit kararlar alan veya muhakemede bulunan diğer "
    "ortaklar ve kilit yöneticilerdir. Talimatla prosedür uygulayan yardımcılar bu kapsamda değildir.")

# ================================================================ Etik Kurallar – Yönetmelik ilişkisi
P.q("Etik Kurallar 100.1, BDY m. 22/5",
    "Etik Kurallar, KAYİK olmayan bir denetim müşterisine belirli şartlarla bazı denetim dışı hizmetlerin sunulmasına izin "
    "vermektedir. Buna karşılık KGK Bağımsız Denetim Yönetmeliği denetlenen işletmeye tasdik, vergi danışmanlığı ve vergi "
    "denetimi dışında hizmet verilmesini yasaklar. Bu durumda Etik Kurallara göre denetim şirketi nasıl hareket etmelidir?",
    "Yönetmelik daha kısıtlayıcı olduğundan izin verilen üç hizmet dışında hizmet sunmaz.",
    ["Etik Kurallarda izin verilen hizmetleri önlem alarak sunabilir.",
     "KAYİK olmayan müşterilere Etik Kuralları, KAYİK'lere Yönetmeliği uygular.",
     "Hizmeti, denetim ekibinde yer almayan ve denetim ağındaki başka bir şirket aracılığıyla sunabilir.",
     "Hizmet ücreti denetim ücretini aşmadığı sürece Etik Kurallara göre hareket eder."],
    "Etik Kurallar 100.1'e göre mevzuat daha kısıtlayıcı hükümler öngörüyorsa denetçi mevzuata uyar. Yönetmelik m. 22/5 "
    "tasdik, vergi danışmanlığı ve vergi denetimi dışındaki hizmetleri, denetim ağı ve ilişkili işletmeler aracılığıyla "
    "sunulmasını da dahil ederek yasaklar.")

# ================================================================ KYS 1
P.q("KYS 1 prg. 6",
    f"{K1}, aşağıdakilerden hangisi bir denetim şirketinin kalite yönetim sistemini oluşturan sekiz unsurdan biri "
    "değildir?",
    "Mesleki sorumluluk sigortası",
    ["Bilgi ve iletişim", "Kaynaklar", "Denetim veya hizmetin yürütülmesi", "İzleme ve düzeltme süreci"],
    "KYS 1 prg. 6'ya göre kalite yönetim sistemi; şirketin risk değerlendirme süreci, üst yönetim ve liderlik, etik "
    "hükümler, müşteri ilişkisinin ve sözleşmenin kabulü ve devamı, denetim veya hizmetin yürütülmesi, kaynaklar, bilgi "
    "ve iletişim ile izleme ve düzeltme sürecinden oluşur. Sigorta bu unsurlar arasında sayılmaz.", zorluk="easy")

P.q("KYS 1 prg. 7-8",
    f"{K1}, kalite yönetim sistemine uygulanan risk esaslı yaklaşımın adımları aşağıdakilerin hangisinde doğru sırayla "
    "verilmiştir?",
    "Kalite hedeflerini belirlemek, kalite risklerini belirleyip değerlendirmek ve bu risklere karşılık tasarlayıp uygulamak",
    ["Kalite risklerinin belirlenmesi, kalite hedeflerinin bu risklere göre yeniden yazılması ve sonuçların Kuruma bildirilmesi",
     "Denetim dosyalarının incelenmesi, bulunan eksikliklerin raporlanması ve denetçilere yaptırım uygulanması",
     "Karşılıkların tasarlanması, kalite hedeflerinin belirlenmesi ve kalite risklerinin sonradan ölçülmesi",
     "Kalite hedeflerinin belirlenmesi, denetim ücretlerinin güncellenmesi ve risklerin yıllık raporlanması"],
    "KYS 1 prg. 7-8 ve 23'e göre risk esaslı yaklaşım; kalite hedeflerinin belirlenmesi, bu hedeflere ulaşılmasını "
    "engelleyebilecek kalite risklerinin belirlenip değerlendirilmesi ve kalite risklerine karşı yapılacak işlerin "
    "tasarlanıp uygulanması yoluyla işler.")

P.q("KYS 1 prg. 16-r",
    f"{K1}, “kalite riski” aşağıdakilerden hangisinde doğru tanımlanmıştır?",
    "Makul düzeyde gerçekleşme ve bir veya daha fazla kalite hedefine ulaşılmasını olumsuz etkileme olasılığı olan risk",
    ["Denetçinin, finansal tablolar önemli yanlışlık içerdiğinde bu duruma uygun olmayan bir denetim görüşü bildirmesi riski",
     "Bir yönetim beyanındaki önemli olabilecek bir yanlışlığın işletmenin kontrolleriyle zamanında önlenememesi veya tespit edilememesi riski",
     "Denetim şirketinin Kurum incelemesinde idari yaptırımla karşılaşma olasılığı",
     "Denetim şirketinin gelirlerinin tek bir müşteriye bağımlı hâle gelmesi riski"],
    "KYS 1 prg. 16-r kalite riskini, makul bir düzeyde gerçekleşme ve tek başına veya diğer risklerle birlikte bir veya "
    "daha fazla kalite hedefine ulaşılmasını olumsuz yönde etkileme olasılığı bulunan risk olarak tanımlar. Diğer "
    "seçenekler denetim riski ve kontrol riskini ya da ilgisiz durumları anlatır.", zorluk="hard")

P.q("KYS 1 prg. 16-x, 16-s",
    f"{K1}, kalite yönetim sisteminin amacına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Sistem, denetimlerin standartlara uygun yürütüldüğü konusunda şirkete mutlak güvence sağlamak üzere tasarlanır.",
    ["Sistem, şirketin ve personelin sorumluluklarını standartlara ve mevzuata uygun yerine getirdiğine dair makul güvence amaçlar.",
     "Sistem, şirket tarafından düzenlenen raporların içinde bulunulan şartlara uygun olduğuna dair makul güvence amaçlar.",
     "KYS'ler çerçevesinde makul güvence, yüksek ancak mutlak olmayan bir güvence seviyesidir.",
     "Sistemin tasarımı, şirketin niteliğine ve yürüttüğü denetimlerin niteliğine göre farklılık gösterir."],
    "KYS 1 prg. 16-x'e göre kalite yönetim sistemi, sorumlulukların standartlara ve mevzuata uygun yerine getirildiği ve "
    "raporların şartlara uygun olduğu hususlarında makul güvence sağlamak amacıyla tasarlanır; prg. 16-s makul güvenceyi "
    "yüksek ancak mutlak olmayan güvence olarak tanımlar. Ölçeklenebilirlik prg. 10'dadır.")

P.q("KYS 1 prg. 20",
    f"{K1}, aşağıdakilerden hangisi denetim şirketinin kalite yönetim sistemine ilişkin sorumlulukları arasında "
    "yer almaz?",
    "Kalite yönetim sistemi için nihai sorumluluğu sorumlu denetçilerin tamamına eşit olarak dağıtmak",
    ["Nihai sorumluluk ve hesap verme yükümlülüğünü genel müdüre, yönetici ortağa veya uygun hâllerde yönetim kuruluna vermek",
     "Kalite yönetim sisteminin işleyişinden sorumlu olanları görevlendirmek",
     "Bağımsızlık hükümlerine uygunluğun işleyişinden sorumlu olanları görevlendirmek",
     "İzleme ve düzeltme sürecinin işleyişinden sorumlu olanları görevlendirmek"],
    "KYS 1 prg. 20'ye göre şirket nihai sorumluluk ve hesap verme yükümlülüğünü genel müdüre veya yönetici ortağa (ya da "
    "eşdeğerine) veya uygun hâllerde yönetim kuruluna verir; sistemin işleyişinden, bağımsızlık hükümlerine uygunluktan ve "
    "izleme ve düzeltme sürecinden sorumlu olanları görevlendirir.")

P.q("KYS 1 prg. 9, 53-54",
    f"{K1}, kalite yönetim sisteminin değerlendirilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Nihai sorumluluk verilen kişi sistemi yılda en az bir kez değerlendirip sonuca varır.",
    ["Sistem, üç yılda bir Kurum tarafından değerlendirilir ve sonuç şirkete bildirilir.",
     "Sistemin değerlendirmesini her denetimde kaliteyi gözden geçiren kişi yapar.",
     "Değerlendirme, sorumlu denetçilerin her biri tarafından kendi denetimleri için yapılır.",
     "Sistem sadece önemli bir eksiklik tespit edildiğinde değerlendirilir."],
    "KYS 1 prg. 9 ve 53-54'e göre nihai sorumluluk ve hesap verme yükümlülüğü verilen kişi veya kişiler, sistemi yılda en "
    "az bir kez değerlendirir ve sistemin hedeflere ulaşıldığına dair makul güvence sağlayıp sağlamadığı konusunda "
    "şirket adına sonuca varır.")

P.q("KYS 1 prg. 54",
    f"{K1}, kalite yönetim sisteminin yıllık değerlendirmesi sonucunda ulaşılabilecek sonuçlardan biri aşağıdakilerden "
    "hangisidir?",
    "Ciddi ancak yaygın olmayan etkisi olan eksiklikler dışında sistemin makul güvence sağladığı",
    ["Sistemin denetim şirketine mutlak güvence sağladığı",
     "Sistemin sadece KAYİK denetimleri bakımından makul güvence sağladığı",
     "Sistemin makul güvence sağlayıp sağlamadığına dair görüş bildirmekten kaçınıldığı",
     "Sistemin, önceki yılın Kurum incelemesinde aykırılık bulunmadığı için değerlendirmeye gerek olmadığı"],
    "KYS 1 prg. 54'e göre üç sonuca ulaşılabilir: sistemin makul güvence sağladığı; ciddi ancak yaygın olmayan etkiye "
    "sahip eksiklikler dışında makul güvence sağladığı; ya da makul güvence sağlamadığı.", zorluk="hard")

P.q("KYS 1 prg. 34-f",
    f"{K1}, denetim şirketinin politika veya prosedürlerinde kalitesinin gözden geçirilmesini zorunlu tutması gereken "
    "işler arasında aşağıdakilerden hangisi yer almaz?",
    "Bütün küçük ve orta büyüklükteki işletmelerin finansal tablolarının sınırlı bağımsız denetimleri",
    ["Borsada işlem gören işletmelerin finansal tablolarının bağımsız denetimleri",
     "Mevzuatta kalitenin gözden geçirilmesinin zorunlu tutulduğu denetimler",
     "Şirketin, bir kalite riskine karşı uygun iş olarak kalitenin gözden geçirilmesini belirlediği denetimler",
     "Şirketin, bir kalite riskine karşı kalitenin gözden geçirilmesini uygun gördüğü diğer hizmetler"],
    "KYS 1 prg. 34-f'ye göre kalitenin gözden geçirilmesi borsada işlem gören işletmelerin bağımsız denetimlerinde, "
    "mevzuatın zorunlu tuttuğu işlerde ve şirketin bir veya daha fazla kalite riskine karşı uygun gördüğü işlerde zorunlu "
    "tutulur. Büyüklüğe bağlı genel bir zorunluluk öngörülmemiştir.")

P.q("KYS 1 prg. 34-b",
    f"{K1}, etik hükümler uyarınca bağımsız olması gereken personelden alınacak bağımsızlık taahhüdüne ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Yazılı olarak, her denetimden önce ve her hâlükârda yılda en az bir kez alınır.",
    ["Taahhüt sözlü olarak, sadece yeni bir müşteriyle ilk denetim öncesinde alınır.",
     "Taahhüt, sadece sorumlu denetçi ve kaliteyi gözden geçiren kişiden alınır.",
     "Taahhüt yazılı olarak, sadece personelin işe başladığı tarihte bir kez alınır.",
     "Taahhüt, denetim raporu tarihinde denetim ekibinden toplu olarak alınır."],
    "KYS 1 prg. 34-b'ye göre şirket, etik hükümler uyarınca bağımsız olması gereken tüm personelinden her bir denetimden "
    "önce ve her hâlükârda yılda en az bir kez bağımsızlık hükümlerine uyduklarını ve uyacaklarını bildiren yazılı bir "
    "taahhüt alır.")

P.q("KYS 1 prg. 34-d",
    "Bir denetim şirketi, bir müşteriyle sözleşmeyi kabul ettikten sonra, önceden bilseydi müşteriyi kabul etmemesine yol "
    f"açacak bir bilgi (yönetimin dürüstlüğüne ilişkin ciddi bir şüphe) edinmiştir. {K1} şirketin bu duruma ilişkin "
    "yükümlülüğü aşağıdakilerden hangisidir?",
    "Bu tür durumları ele alan politika veya prosedürler oluşturup bunlara göre hareket etmek",
    ["Sözleşmeyi derhâl feshedip durumu gerekçeleriyle birlikte müşterinin genel kuruluna yazılı olarak bildirmek",
     "Sözleşmeyi sürdürmek; kabul kararı verildikten sonra yeni bilgilerin bir önemi yoktur",
     "Bilgiyi denetim raporunun diğer hususlar paragrafında açıklamak",
     "Durumu yeni bir sözleşme imzalanana kadar gizli tutarak denetime devam etmek"],
    "KYS 1 prg. 34-d'ye göre şirket, müşteri ilişkisini veya sözleşmeyi kabul ettikten sonra, önceden bilseydi reddetmesine "
    "sebep olabilecek bir bilgi edinmesi ile mevzuat gereği kabul yükümlülüğü bulunan durumları ele alan politika veya "
    "prosedürler oluşturur. Feshin mümkün olup olmadığı ayrıca mevzuata bağlıdır.")

P.q("KYS 1 prg. 34-e",
    f"Borsada işlem gören işletmelerin finansal tablolarını denetleyen bir denetim şirketi, {K1} kalite yönetim sistemi "
    "hakkında kimle iletişim kurulmasını zorunlu kılan politika veya prosedürler oluşturur?",
    "Denetlenen işletmenin üst yönetiminden sorumlu olanlar",
    ["Sermaye Piyasası Kurulu ve Borsa İstanbul yönetimi", "Denetlenen işletmenin pay sahipleri ve yatırımcıları",
     "Denetim ağındaki diğer denetim şirketleri", "Denetlenen işletmenin iç denetim birimi ve risk yönetimi müdürlüğü"],
    "KYS 1 prg. 34-e(i)'ye göre borsada işlem gören işletmelerin denetiminde, kalite yönetim sisteminin kaliteli denetimin "
    "tutarlı biçimde yürütülmesini nasıl desteklediğine ilişkin üst yönetimden sorumlu olanlarla iletişim kurulmasını "
    "zorunlu kılan politika ve prosedürler oluşturulur.")

P.q("KYS 1 prg. 10",
    f"{K1}, kalite yönetim sisteminin ölçeklenebilirliği ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    "Standart, her büyüklükteki şirketin aynı yöntemleri uygulayan birbirinin aynısı bir sistem kurmasını gerektirir.",
    ["Şirket risk esaslı yaklaşımı uygularken kendi niteliğini ve içinde bulunduğu şartları dikkate alır.",
     "Yürütülen denetim veya hizmetin niteliği ve şartları da sistemin tasarımını etkiler.",
     "Borsada işlem gören işletmeleri denetleyen şirketin sistemi, derleme işi yapan şirketinkinden karmaşık olabilir.",
     "Sistemin karmaşıklığı ve uyguladığı yöntemler şirketten şirkete farklılık gösterir."],
    "KYS 1 prg. 10'a göre şirket risk esaslı yaklaşım uygularken kendi niteliğini ve yürüttüğü işlerin niteliğini dikkate "
    "alır; bu nedenle sistemin tasarımı, karmaşıklığı ve yöntemleri farklılık gösterir. Borsada işlem gören işletmeleri "
    "denetleyen şirketin daha karmaşık bir sisteme ihtiyacı olabilir.")

P.q("KYS 1 prg. 34-c",
    f"{K1}, denetim şirketinin yaptığı çalışmaların mesleki standartlara aykırı olduğuna ilişkin dışarıdan gelen bir "
    "şikâyet karşısındaki yükümlülüğü aşağıdakilerden hangisidir?",
    "Şikâyet ve iddiaları, oluşturduğu politika veya prosedürlere göre alıp araştırmak ve çözmek",
    ["Şikâyeti işleme almadan KGK'ya iletmek ve Kurumun kararını beklemek",
     "Şikâyet eden kişinin kimliği belirlenemiyorsa şikâyeti dikkate almamak",
     "Şikâyeti bir sonraki yıllık değerlendirmeye kadar bekletmek",
     "Şikâyete konu denetimin sorumlu denetçisinin yazılı savunmasını alarak dosyayı başkaca inceleme yapmadan kapatmak"],
    "KYS 1 prg. 34-c'ye göre şirket, çalışmalarının mesleki standartlara ve mevzuata veya kendi politika ve prosedürlerine "
    "aykırı olduğuna ilişkin şikâyet ve iddiaların alınması, araştırılması ve çözülmesi için politika veya prosedürler "
    "oluşturur.")

# ================================================================ KYS 2
P.q("KYS 2 prg. 12-b",
    f"{K2}, aşağıdakilerden hangisi kaliteyi gözden geçiren kişi olarak görevlendirilebilecekler arasında yer almaz?",
    "Aynı denetimin ekibinde kıdemli denetçi olarak görev yapan kişi",
    ["Denetim şirketindeki başka bir denetimin sorumlu denetçisi", "Denetim şirketindeki diğer bir bağımsız denetçi",
     "Denetim şirketi dışından, liyakat kıstaslarını karşılayan bir kişi", "Liyakat kıstaslarını karşılayan başka bir ortak"],
    "KYS 2 prg. 12-b'ye göre kaliteyi gözden geçiren kişi, şirket tarafından görevlendirilen sorumlu denetçi, şirketteki "
    "diğer bir bağımsız denetçi veya şirket dışından bir kişidir. Prg. 9 ve 18'e göre bu kişi denetim ekibinin bir üyesi "
    "olamaz.", zorluk="easy")

P.q("KYS 2 prg. 19",
    "Bir denetim şirketi, geçen yıl X A.Ş.'nin sorumlu denetçisi olan Levent Bey'i bu yıl aynı denetimin kalitesini gözden "
    f"geçiren kişi olarak atamak istemektedir. {K2} bu atamaya ilişkin aşağıdakilerden hangisi doğrudur?",
    "Etik hükümler daha uzun süre öngörmedikçe iki yıllık ara vermeden sonra atanabilir.",
    ["Levent Bey denetimi en iyi bilen kişi olduğu için hemen atanabilir.",
     "Levent Bey bir yıllık ara vermeden sonra atanabilir.",
     "Levent Bey, sorumlu denetçilik yaptığı bir işletmede bu göreve daha sonra da atanamaz.",
     "Levent Bey, üst yönetimden sorumlu olanların onayıyla hemen atanabilir."],
    "KYS 2 prg. 19'a göre şirketin politika veya prosedürleri, önceden sorumlu denetçi olarak görev yapan kişinin kaliteyi "
    "gözden geçiren kişi olarak atanmasından doğan tarafsızlık tehditlerini ele alır ve iki yıllık veya etik hükümler "
    "gerektiriyorsa daha uzun bir ara verme süresi belirler.")

P.q("KYS 2 prg. 8-9",
    f"{K2}, kalitenin gözden geçirilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Gözden geçirme, denetimin tamamının standartlara ve şirket politikalarına uygunluğunu değerlendirir.",
    ["Kalitenin gözden geçirilmesi, rapor tarihinde veya öncesinde tamamlanır.",
     "Denetim ekibinin yaptığı önemli muhakemeler ve ulaşılan sonuçlar tarafsız bir şekilde değerlendirilir.",
     "Kalitenin gözden geçirilmesi, sorumlu denetçinin denetimin yönetilmesine ilişkin sorumluluklarını değiştirmez.",
     "Kaliteyi gözden geçiren kişinin görüşü desteklemek için kanıt toplamasına gerek yoktur."],
    "KYS 2 prg. 8'e göre kalitenin gözden geçirilmesi önemli muhakemeler ve sonuçların tarafsız değerlendirilmesidir ve "
    "denetimin tamamının standartlara, mevzuata veya şirket politikalarına uygunluğunu değerlendirme amacı taşımaz. Prg. 9 "
    "sorumlu denetçinin sorumluluklarının değişmediğini ve kanıt toplama gerekmediğini belirtir.")

P.q("KYS 2 prg. 24-b, 27",
    f"{K2}, sorumlu denetçinin denetim raporuna tarih atmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Gözden geçirmenin tamamlandığı bildirilene kadar sorumlu denetçi rapora tarih vermez.",
    ["Sorumlu denetçi rapora tarih verir; kalitenin gözden geçirilmesi rapor tarihinden sonra tamamlanabilir.",
     "Rapor tarihini, kalitenin gözden geçirilmesini yapan kişi belirler ve raporu birlikte imzalar.",
     "Rapor tarihi, kaliteyi gözden geçiren kişinin denetim kanıtlarını yeniden topladığı tarihtir.",
     "Kalitenin gözden geçirilmesi tamamlanmasa da, üst yönetim onay verirse rapor tarihlendirilebilir."],
    "KYS 2 prg. 24-b ve 27'ye göre şirket politikaları, kaliteyi gözden geçiren kişiden gözden geçirmenin tamamlandığına "
    "dair bildirim alınana kadar sorumlu denetçinin rapora tarih vermemesini kapsar; prg. 8'e göre gözden geçirme rapor "
    "tarihinde veya öncesinde tamamlanır.")

P.q("KYS 2 prg. 26",
    "Kaliteyi gözden geçiren kişi, stok değer düşüklüğüne ilişkin önemli bir muhakemenin uygun olmadığı endişesini "
    f"sorumlu denetçiye iletmiş, ancak endişe ikna edici biçimde çözümlenememiştir. {K2} kaliteyi gözden geçiren "
    "kişinin yapması gereken aşağıdakilerden hangisidir?",
    "Uygun kişilere kalitenin gözden geçirilmesinin tamamlanamadığını bildirir.",
    ["Denetim raporunu sorumlu denetçi yerine kendisi imzalar ve görüşü değiştirir.",
     "Endişesini denetlenen işletmenin üst yönetimine doğrudan yazılı olarak bildirir.",
     "Sorumlu denetçinin muhakemesi esas olduğundan endişesini kayda alıp gözden geçirmeyi tamamlar.",
     "Ek kanıt toplamak üzere denetim ekibine katılır ve ilgili prosedürleri kendisi uygular."],
    "KYS 2 prg. 26'ya göre kaliteyi gözden geçiren kişi endişelerini sorumlu denetçiye bildirir; ikna edici şekilde "
    "çözümlenemezse şirketteki uygun kişi veya kişilere gözden geçirmenin tamamlanamadığını bildirir. Bu kişi ekip üyesi "
    "olmadığından kanıt toplamaz ve raporu imzalamaz.", zorluk="hard")

P.q("KYS 2 prg. 18",
    f"{K2}, denetim şirketinin kaliteyi gözden geçiren kişinin liyakatine ilişkin belirlediği kıstaslar arasında "
    "aşağıdakilerden hangisi yer almaz?",
    "Gözden geçirilen işletmenin sektöründe en az on yıl yöneticilik yapmış olması",
    ["Denetim ekibinin bir üyesi olmaması",
     "Gözden geçirme için yeterli zaman dahil yetkinlik, kabiliyet ve uygun yetkiye sahip olması",
     "Tarafsızlık ve bağımsızlık tehditleriyle ilişkili olanlar dahil etik hükümlere uyması",
     "Liyakatiyle ilgili varsa mevzuat hükümlerine uyması"],
    "KYS 2 prg. 18 liyakat kıstası olarak ekip üyesi olmamayı, yeterli zaman dahil yetkinlik, kabiliyet ve yetkiyi, etik "
    "hükümlere uymayı ve varsa mevzuat hükümlerine uymayı sayar; sektör yöneticiliği gibi bir süre şartı yoktur.")

P.q("KYS 2 prg. 20",
    f"{K2}, kaliteyi gözden geçiren kişiye yardımcı olacak kişilerle ilgili aşağıdakilerden hangisi doğrudur?",
    "Yardımcılar da ekip üyesi olamaz ve görevleri için yeterli yetkinliğe sahip olmalıdır.",
    ["Yardımcılar, zaman kazandırmak için aynı denetimin ekibinden seçilir.",
     "Kaliteyi gözden geçiren kişi, gözden geçirmede yardımcı kullanamaz.",
     "Yardımcıların liyakatine ilişkin kıstasları Kurum her denetim için ayrıca belirler.",
     "Yardımcılar, gözden geçirmenin tamamlandığını sorumlu denetçiye bildirmekle görevlidir."],
    "KYS 2 prg. 20'ye göre şirket, kaliteyi gözden geçiren kişiye yardımcı olacakların liyakatine ilişkin kıstasları "
    "belirler; bu kişiler denetim ekibi üyesi olamaz ve verilen görevleri yerine getirecek yetkinliğe sahip olmalıdır. "
    "Tamamlanma bildirimi kaliteyi gözden geçiren kişiye aittir.")

P.q("KYS 2 prg. 30",
    f"{K2}, kalitenin gözden geçirilmesine ilişkin belgelendirmenin yeterliliği hangi ölçüte göre belirlenir?",
    "Denetimle önceden bağlantısı olmayan tecrübeli bir denetçinin prosedür ve sonuçları anlayabilmesi",
    ["Belgelerin, denetlenen işletmenin üst yönetimi tarafından imzalanmış olması",
     "Gözden geçirmenin, denetim raporuyla birlikte kamuya açıklanabilecek ayrıntıda olması",
     "Belgelerin, gözden geçiren kişinin denetim ekibinden bağımsız olarak topladığı ek denetim kanıtlarını içermesi",
     "Belgelerin, KGK'ya denetim raporuyla birlikte gönderilecek biçimde hazırlanması"],
    "KYS 2 prg. 30'a göre belgelendirme; kaliteyi gözden geçiren kişi ve yardımcıları tarafından uygulanan prosedürlerin "
    "niteliği, zamanlaması ve kapsamı ile ulaşılan sonuçları, denetimle önceden bağlantısı bulunmayan tecrübeli bir "
    "denetçinin anlayabilmesine olanak sağlayacak yeterlilikte olmalıdır.")

# ================================================================ öncüllü ve karma
P.oncul("Etik Kurallar 120.6 U3",
    f"{E} aşağıdaki durumlar değerlendirilmektedir:",
    ["Sorumlu denetçinin eşinin denetim müşterisinde önemli miktarda pay sahibi olması",
     "Denetim ekibindeki bir denetçinin kız kardeşinin müşterinin finans müdürü olması",
     "Müşterinin genel müdürünün, önerilen düzeltme kaydında ısrar edilirse denetçiyi değiştireceğini söylemesi",
     "Denetim şirketinin geçen yıl hazırladığı değerleme raporunun bu yılki tablolarda kullanılması"],
    "Yukarıdaki durumlardan hangileri kişisel çıkar ya da yakınlık tehdidi oluşturur?",
    "I ve II",
    ["Yalnız I", "I ve II", "II ve III", "I, II ve IV", "I, III ve IV"],
    "120.6 U3'e göre eşin müşterideki finansal çıkarı kişisel çıkar, yakın akrabanın müşteride kilit görevde bulunması "
    "yakınlık tehdidi oluşturur. Denetçiyi değiştirme baskısı yıldırma, şirketin kendi hazırladığı değerleme raporunun "
    "sonuçlarına dayanması kendi kendini denetleme tehdididir.", zorluk="hard")

P.oncul("KYS 1 prg. 6, 34",
    f"{K1} aşağıdaki ifadeler değerlendirilmektedir:",
    ["Etik hükümler, kalite yönetim sisteminin sekiz unsurundan biridir.",
     "Denetlenen işletmenin iç kontrol sistemi, denetim şirketinin kalite yönetim sisteminin bir unsurudur.",
     "Kalitenin gözden geçirilmesi, KYS 1 uyarınca bazı denetimlerde zorunlu tutulan bir karşılıktır.",
     "Kalite yönetim sistemi, izleme ve düzeltme sürecini de kapsar."],
    "Yukarıdaki ifadelerden hangileri doğrudur?",
    "I, III ve IV",
    ["I ve II", "II ve IV", "I, II ve III", "I, III ve IV", "II, III ve IV"],
    "KYS 1 prg. 6'ya göre etik hükümler ile izleme ve düzeltme süreci sistemin unsurlarıdır (I ve IV). Prg. 34-f'ye göre "
    "kalitenin gözden geçirilmesi belirli işlerde zorunlu tutulur (III). Denetlenen işletmenin iç kontrol sistemi denetim "
    "şirketinin kalite yönetim sisteminin unsuru değildir (II yanlış).")

P.q("Etik Kurallar A540.9, A540.7",
    f"{E}, KAYİK denetiminde kilit denetçi rotasyonunun istisnalarına ilişkin aşağıdakilerden hangisi yanlıştır?",
    "Denetim şirketi, müşterinin talebi üzerine gerekçe göstermeden kilit denetçinin süresini uzatabilir.",
    ["Öngörülemeyen şartlardan kaynaklanan ender durumlarda üst yönetimden sorumlu olanların mutabakatıyla süre uzatılabilir.",
     "Bu tür bir uzatmada oluşan tehditleri azaltacak önlemlere ihtiyaç olup olmadığı değerlendirilir.",
     "Gerekli bilgi ve deneyime sahip kişi sayısı az olan şirketlerde yetkili merciin muafiyeti söz konusu olabilir.",
     "Muafiyet hâlinde Kurum, düzenli bağımsız dış inceleme gibi diğer zorunlulukları belirleyebilir."],
    "A540.7'ye göre istisna, denetimin kalitesi açısından devamı önem arz eden kilit denetçiler için şirketin kontrolü "
    "dışındaki öngörülemeyen şartlardan kaynaklanan ender durumlarda ve üst yönetimden sorumlu olanların mutabakatıyla "
    "tanınır. A540.9 az sayıda uzman bulunan şirketler için yetkili merci muafiyetini ve Kurumun belirleyeceği diğer "
    "zorunlulukları düzenler. Müşteri talebiyle gerekçesiz uzatma yoktur.", zorluk="hard")

P.q("KYS 1 prg. 22",
    f"{K1}, kalite yönetim sisteminin işleyişinden, bağımsızlık hükümlerine uygunluktan ve izleme ve düzeltme sürecinden "
    "sorumlu olarak görevlendirilen kişilerle ilgili aşağıdakilerden hangisi doğrudur?",
    "Şirket, bu kişilerin nihai sorumlularla doğrudan iletişim kurabileceği bir ortam oluşturur.",
    ["Bu kişiler sadece KGK'ya karşı sorumludur ve şirket yönetimine rapor vermez.",
     "Bu kişilerin şirketin ortakları arasından seçilmesi zorunlu tutulmuştur.",
     "Bu görevler aynı kişiye verilemez; her biri için ayrı bir yönetim kurulu üyesi atanır.",
     "Bu kişiler görevlerini ancak nihai sorumluluk verilen kişinin yazılı talimatıyla yerine getirebilir."],
    "KYS 1 prg. 22'ye göre şirket; sistemin, bağımsızlık hükümlerine uygunluğun ve izleme ve düzeltme sürecinin "
    "işleyişinden sorumlu olan kişilerin, nihai sorumluluk verilen kişi veya kişilerle doğrudan iletişim kurabileceği bir "
    "ortam oluşturur. Prg. 21 bu kişilerin deneyim, bilgi, etki ve yetkiye sahip olmasını ister.")

P.q("Etik Kurallar 110.1 U1-c",
    f"{E}, “mesleki yeterlik ve özen” ilkesinin içeriğine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Güncel standart ve mevzuata uygun hizmet için gereken bilgi ve beceriyi elde edip korumayı ve özenli davranmayı içerir.",
    ["Bütün mesleki ve iş ilişkilerinde dürüst, açık, doğru ve güvenilir olmayı ifade eder.",
     "Mesleğin icrası sırasında elde edilen bilgilerin gizliliğine riayet etmeyi ve bunları kendi çıkarına kullanmamayı ifade eder.",
     "Muhakeme ve kararların önyargılardan, çıkar çatışmalarından ve başkalarının nüfuzundan etkilenmemesini ifade eder.",
     "Denetim mesleğinin itibarını zedeleyici tutum ve davranışlardan kaçınmayı ifade eder."],
    "110.1 U1-c'ye göre mesleki yeterlik ve özen; güncel teknik ve mesleki standartlar ile mevzuata uygun olarak yeterli "
    "mesleki hizmet sunmayı temin edecek bilgi ve beceriyi elde etmeyi ve korumayı ve standartlara uygun şekilde özen "
    "içinde hareket etmeyi kapsar. Diğer seçenekler dürüstlük, sır saklama, tarafsızlık ve mesleğe uygun davranışı anlatır.")

# ================================================================ ek sorular
P.q("Etik Kurallar A111.2",
    "Bir denetçi, müşterisinin kredi başvurusuna eklenecek bir raporda önemli düzeyde yanıltıcı bilgi bulunduğunu "
    f"düşünmesine rağmen bu raporla bilerek ilişkilendirilmeyi kabul etmiştir. {E} bu davranış öncelikle hangi temel "
    "ilkenin ihlalidir?",
    "Dürüstlük",
    ["Sır saklama", "Tarafsızlık", "Mesleki yeterlik ve özen", "Mesleğe uygun davranış"],
    "A111.2'ye göre denetçi, önemli düzeyde yanlış veya yanıltıcı beyan içerdiğini, dikkatsizce sunulduğunu ya da gerekli "
    "bilgileri gizlediğini düşündüğü raporlar ve diğer bilgilerle bilerek ilişkilendirilmez; bu hüküm dürüstlük ilkesinin "
    "parçasıdır. 111.2 U1'e göre olumlu görüş dışında bir görüş içeren rapor sunan denetçi bu hükmü ihlal etmiş sayılmaz.",
    zorluk="easy")

P.q("Etik Kurallar A120.5",
    f"{E}, aşağıdakilerden hangisi denetçinin kavramsal çerçeveyi uygularken yapması gerekenler arasında yer almaz?",
    "Tehditleri ortadan kaldırmak için müşteriden ek ücret talep etmek",
    ["Sorgulayıcı bir yaklaşımla hareket etmek",
     "Mesleki muhakemesini kullanmak",
     "Gerekli bilgiye sahip makul üçüncü taraf testini kullanmak",
     "Konunun ortaya çıktığı veya çıkabileceği bağlamı dikkate almak"],
    "A120.4 ve A120.5'e göre denetçi etik bir konuyla ilgilenirken bağlamı dikkate alır; kavramsal çerçeveyi uygularken "
    "sorgulayıcı bir yaklaşımla hareket eder, mesleki muhakemesini kullanır ve makul üçüncü taraf testini uygular. Ek ücret "
    "talebi bir önlem değil, kişisel çıkar tehdidini artırabilecek bir durumdur.")

P.q("KYS 1 prg. 1",
    f"{K1}, bu Standart denetim şirketlerinin hangi işlere ilişkin kalite yönetim sistemi sorumluluklarını düzenler?",
    "Bağımsız ve sınırlı bağımsız denetimler, diğer güvence denetimleri ve ilgili hizmetler",
    ["Sadece KAYİK'lerin finansal tablolarının bağımsız denetimleri",
     "Sadece Türk Ticaret Kanunu uyarınca yapılan zorunlu bağımsız denetimler",
     "Bağımsız denetimler ile denetlenen işletmelere verilen vergi danışmanlığı hizmetleri",
     "Sadece makul güvence sağlayan finansal tablo denetimleri"],
    "KYS 1 prg. 1'e göre Standart; finansal tabloların bağımsız denetim ve sınırlı bağımsız denetimleri ile diğer güvence "
    "denetimleri ve ilgili hizmetlere ilişkin kalite yönetim sistemi tasarlama, yürütme ve uygulama sorumluluklarını "
    "düzenler.")

P.q("KYS 2 prg. 24-a",
    f"{K2}, kaliteyi gözden geçiren kişinin prosedürlerini ne zaman uygulaması gerekir?",
    "Denetim esnasında uygun zamanlarda",
    ["Denetim raporu imzalandıktan sonra",
     "Sadece planlama aşamasının sonunda",
     "Finansal tabloların genel kurulda onaylanmasından sonra",
     "Kurum incelemesi başlamadan hemen önce"],
    "KYS 2 prg. 24-a'ya göre şirket politikaları, önemli muhakemeler ve sonuçların tarafsız değerlendirilmesi için uygun "
    "dayanağı sağlamak üzere kaliteyi gözden geçiren kişinin prosedürleri denetim esnasında uygun zamanlarda uygulama "
    "sorumluluğunu ele alır; gözden geçirme rapor tarihinde veya öncesinde tamamlanır.", zorluk="easy")

P.sayisal("Etik Kurallar A540.8",
    "Bir şirketin denetiminde altı yıldır sorumlu denetçi olarak görev yapan Cem Bey'in müşterisi KAYİK hâline gelmiştir. "
    f"{E} Cem Bey, üst yönetimden sorumlu olanların mutabakatıyla rotasyona tabi tutulmadan önce aynı sıfatla azami "
    "kaç yıl daha hizmet verebilir?",
    "2", ["0", "1", "3", "4"],
    "A540.8'e göre müşteri KAYİK hâline geldiğinde önceki kilit denetçilik süresi altı yıl veya daha fazla ise kişi, üst "
    "yönetimden sorumlu olanların mutabakatıyla azami iki yıl daha aynı sıfatla hizmet verebilir. Beş yıl veya daha az "
    "sürede kalan süre yedi yıldan hizmet süresi çıkarılarak bulunur.", zorluk="hard")

P.q("KYS 1 prg. 41",
    f"{K1}, izleme sürecinde kalite yönetim sistemine ilişkin eksiklikler tespit eden denetim şirketinin bu eksiklikleri "
    "değerlendirirken yapması gereken aşağıdakilerden hangisidir?",
    "Eksikliklerin kök nedenlerini araştırır ve etkisini tek başına ve toplu olarak değerlendirir.",
    ["Eksiklikleri ilgili denetçilerin kişisel sicillerine işler ve değerlendirmeyi sonlandırır.",
     "Eksiklikleri sadece KAYİK denetimlerinde ortaya çıkmışsa değerlendirmeye alır.",
     "Eksiklikleri Kurumun bir sonraki incelemesine kadar kayıt altına alıp bekletir.",
     "Eksiklikleri önemsiz kabul eder; kök neden analizi sadece Kurum incelemesinde yapılır."],
    "KYS 1 prg. 41'e göre şirket tespit edilen eksikliklerin kök nedenlerini araştırır; araştırma prosedürlerinin "
    "niteliğini eksikliğin niteliği ve olası ciddiyetine göre belirler ve eksikliklerin sistem üzerindeki etkisini tek "
    "başına ve toplu hâlde değerlendirir. Prg. 42 eksikliklere karşılık verilmesini düzenler.")

P.q("Etik Kurallar A114.3",
    f"{E}, aşağıdaki durumlardan hangisinde denetçinin müşteri bilgisini açıklaması sır saklama ilkesine aykırılık "
    "oluşturmaz?",
    "Kurumun inceleme görevlilerine, mevzuat uyarınca talep edilen çalışma kâğıtlarının ibraz edilmesi",
    ["Aynı sektördeki başka bir müşteriye, rakibinin maliyet yapısının örnek olarak anlatılması",
     "Denetim ilişkisi sona erdikten sonra müşterinin ticari sırlarının bir makalede kullanılması",
     "Müşterinin kamuya açıklanmamış birleşme planının denetçinin yakın akrabasıyla paylaşılması",
     "Müşterinin yatırım kararına ilişkin gizli bilginin denetçinin kendi pay alımında kullanılması"],
    "A114.3'e göre bilginin açıklanmasının mevzuatça gerekli olduğu veya izin verildiği ve mesleki bir görev ya da hakkın "
    "bulunduğu durumlar (ör. düzenleyici kurum incelemesine uyum) sır saklama ilkesine aykırı değildir. Diğer seçenekler "
    "gizli bilginin açıklanmasını veya kişisel çıkara kullanılmasını içerir (A114.2).")

if __name__ == "__main__":
    sys.exit(P.yaz())
