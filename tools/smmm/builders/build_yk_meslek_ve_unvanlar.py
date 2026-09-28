# -*- coding: utf-8 -*-
"""Meslek Hukuku · Meslek ve Unvanlar — 60 soru, 2026 test biçimi.

Dayanak (28.09.2026 kontrolü, TÜRMOB 2026 derlemesi):
  · 3568 sayılı Kanun m. 1-13 ve 45 (5786, 7104 ve 27.03.2025-7546 değişiklikleri işlenmiş)
  · SMMM ve YMM Kanunu Gereğince Yapılacak Başvurular Hakkında Yönetmelik (RG 22.05.1992)
  · SM ve SMMM'lerin Kaşe Kullanma Usul ve Esasları Hakkında Yönetmelik (RG 15.11.2002)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

P = Paket("questions_topic_meslek_ve_unvanlar_2026.json", lesson="meslek_hukuku", topic="meslek_ve_unvanlar",
          konu_adi="Meslek ve Unvanlar", seed=2026092805,
          surum="3568 s. Kanun (27.03.2025-7546 işlenmiş), Başvurular Hakkında Yön., Kaşe Kullanma Yön.; 28.09.2026 kontrolü")

K = "3568 sayılı Serbest Muhasebeci Mali Müşavirlik ve Yeminli Mali Müşavirlik Kanunu’na göre"
BY = "Serbest Muhasebecilik, Serbest Muhasebeci Mali Müşavirlik ve Yeminli Mali Müşavirlik Kanunu Gereğince Yapılacak Başvurular Hakkında Yönetmelik’e göre"
KY = "Serbest Muhasebeci ve Serbest Muhasebeci Mali Müşavirlerin Kaşe Kullanma Usul ve Esasları Hakkında Yönetmelik’e göre"

# ================================================================ amaç ve mesleğin konusu
P.q("3568 s. Kanun m. 1",
    f"{K}, aşağıdakilerden hangisi Kanunun amacı arasında sayılmamıştır?",
    "Meslek mensuplarının vergi inceleme yetkisini düzenlemek",
    ["İşletmelerde faaliyet ve işlemlerin sağlıklı ve güvenilir işleyişini sağlamak",
     "Faaliyet sonuçlarını denetleyerek gerçek durumu tarafsız biçimde sunmak",
     "Yüksek mesleki standartları gerçekleştirmek",
     "Odalar ve Birliğin kuruluşu, teşkilatı ve seçim esaslarını düzenlemek"],
    "Kanun m. 1 amaçları işlemlerin sağlıklı ve güvenilir işleyişi, sonuçların denetlenip tarafsız sunulması, yüksek "
    "mesleki standartlar ile meslekler, odalar ve Birliğin kuruluş, teşkilat, faaliyet ve seçim esaslarının "
    "düzenlenmesi olarak sayar. Vergi inceleme yetkisi bu Kanunun konusu değildir.")

P.q("3568 s. Kanun m. 2/A",
    f"{K}, aşağıdakilerden hangisi serbest muhasebeci mali müşavirlik mesleğinin konusu arasında yer almaz?",
    "Mali tablo ve beyannamelerin mevzuata uygunluğunu tasdik etmek",
    ["Defterleri tutmak, bilanço, kâr-zarar tablosu ve beyannameleri düzenlemek",
     "Muhasebe sistemlerini kurmak ve geliştirmek",
     "Belgelere dayanarak inceleme, tahlil ve denetim yapmak",
     "Tahkim ve bilirkişilik işlerini yapmak"],
    "Kanun m. 2/A SMMM'nin konusunu defter tutma, beyanname ve tablo düzenleme, sistem kurma, müşavirlik, inceleme, "
    "denetim, yazılı görüş, tahkim ve bilirkişilik olarak sayar. Tasdik m. 2/B ve m. 12'ye göre YMM'lere özgüdür.",
    zorluk="easy")

P.q("3568 s. Kanun m. 2/B",
    f"{K}, yeminli mali müşavirlerin çalışma alanına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "YMM'ler müşterilerinin defterlerini tutabilir.",
    ["Yeminli mali müşavirler muhasebe bürosu açamaz.",
     "Yeminli mali müşavirler muhasebe bürolarına ortak olamaz.",
     "Yeminli mali müşavirler inceleme, tahlil ve denetim yapabilir.",
     "Yeminli mali müşavirler tasdik işlerini yapabilir."],
    "Kanun m. 2/B'ye göre YMM'ler m. 2/A'nın (b) ve (c) bentlerindeki işleri ve tasdik işlerini yapar; muhasebe ile "
    "ilgili defter tutamaz, muhasebe bürosu açamaz ve muhasebe bürolarına ortak olamaz.",
    zorluk="easy")

P.q("3568 s. Kanun m. 3 ve 49",
    "Meslek mensubu olmayan (A), işyerinin tabelasında “Mali Danışman ve Muhasebe Müşaviri” ifadesini kullanarak "
    f"müşterilerin beyannamelerini düzenlemektedir. {K}, bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "Unvanlara karışacak ifade kullanmak yasaktır; oda durumu Cumhuriyet Savcılığına bildirir.",
    ["Kullanılan ifade Kanundaki unvanların aynısı olmadığı için herhangi bir yaptırım uygulanmaz.",
     "Durum odaya bildirilir; oda (A)'ya uyarma cezası vererek tabelanın indirilmesini ister.",
     "Durum Hazine ve Maliye Bakanlığına bildirilir; Bakanlık idari para cezası uygular.",
     "(A) odaya kaydolur ve oda genel kurulunun izniyle bu unvanı kullanmaya devam eder."],
    "Kanun m. 3'e göre yetkisi olmayanlarca meslek unvanlarının veya bunlara karışacak ya da benzer ibarelerin "
    "kullanılması yasaktır; odalar bunu öğrendiğinde Cumhuriyet Savcılığına bildirmek zorundadır. M. 49'a göre m. 3/1'e "
    "aykırılık altı aydan bir yıla kadar hapis ve adli para cezası gerektirir.",
    zorluk="hard")

# ================================================================ genel ve özel şartlar
P.q("3568 s. Kanun m. 4",
    f"Aşağıdakilerden hangisi {K.replace('’na göre', '’na göre,')} meslek mensubu olabilmenin “genel şartları”ndan biri değildir?",
    "Serbest muhasebeci mali müşavirlik sınavını kazanmış olmak",
    ["Ceza veya disiplin soruşturması sonucunda memuriyetten çıkarılmış olmamak",
     "Medeni hakları kullanma ehliyetine sahip bulunmak",
     "Kamu haklarından mahrum bulunmamak",
     "Meslek şeref ve haysiyetine uymayan durumları bulunmamak"],
    "Kanun m. 4 genel şartları T.C. vatandaşlığı, medeni hakları kullanma ehliyeti, kamu haklarından mahrum olmamak, "
    "belirli suçlardan mahkûm olmamak, memuriyetten çıkarılmamış olmak ve meslek şeref ve haysiyetine uymayan durumu "
    "bulunmamak olarak sayar. Sınavı kazanmak m. 5'teki özel şarttır.",
    zorluk="easy")

P.q("3568 s. Kanun m. 5/A",
    f"{K}, aşağıdakilerden hangisi serbest muhasebeci mali müşavir olabilmenin “özel şartları”ndan biri değildir?",
    "Medeni hakları kullanma ehliyetine sahip bulunmak",
    ["En az üç yıl staj yapmış olmak",
     "Kanunda sayılan dallarda eğitim veren fakülte ve yüksekokullardan en az lisans seviyesinde mezun olmak",
     "Serbest muhasebeci mali müşavirlik sınavını kazanmış olmak",
     "Serbest muhasebeci mali müşavirlik ruhsatını almış olmak"],
    "Kanun m. 5/A'ya göre özel şartlar belirli dallarda lisans mezuniyeti, en az üç yıl staj, SMMM sınavını kazanmak ve "
    "SMMM ruhsatını almaktır. Medeni hakları kullanma ehliyeti m. 4'teki genel şartlardandır.")

P.q("3568 s. Kanun m. 4/d",
    f"{K}, meslek mensubu olabilmek için mahkûm olunmaması gereken suçlara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kasten işlenen bir suçtan bir yıl veya daha fazla hapis cezası, TCK m. 53'teki süreler geçmiş olsa bile engeldir.",
    ["Kasten işlenen bir suçtan iki yıl veya daha fazla hapis cezası, cezanın infazından beş yıl sonra engel olmaktan çıkar.",
     "Taksirle işlenen bir suçtan alınan her türlü hapis cezası meslek mensubu olmaya engeldir.",
     "Kasten işlenen bir suçtan bir yıl veya daha fazla hapis cezası, affa uğramışsa engel oluşturmaz.",
     "Dolandırıcılık suçundan mahkûmiyet, ceza ertelenmişse meslek mensubu olmaya engel oluşturmaz."],
    "Kanun m. 4/d'ye göre TCK m. 53'teki süreler geçmiş olsa bile kasten işlenen bir suçtan bir yıl veya daha fazla hapis "
    "cezası ya da affa uğramış olsa bile devletin güvenliğine, anayasal düzene karşı suçlar ile zimmet, irtikâp, rüşvet, "
    "hırsızlık, dolandırıcılık, sahtecilik gibi suçlardan mahkûmiyet engeldir.",
    zorluk="hard")

P.q("3568 s. Kanun m. 5/A-a",
    "Mühendislik fakültesi mezunu olan (B), serbest muhasebeci mali müşavir olmak istemektedir. "
    f"{K}, (B)'nin öğrenim şartını sağlayabilmesi için aşağıdakilerden hangisi gerekir?",
    "Kanunda sayılan bilim dallarından birinde lisansüstü diploma almış olması",
    ["Bir muhasebe bürosunda en az beş yıl bağımlı çalışmış olması",
     "Mühendislik diplomasının Yükseköğretim Kurulunca iktisada denk sayılması",
     "Staj süresinin üç yıl yerine altı yıl olarak tamamlanması",
     "Temel Eğitim ve Staj Merkezinde ek bir yıllık program tamamlaması"],
    "Kanun m. 5/A-a'ya göre hukuk, iktisat, maliye, işletme, muhasebe, bankacılık, kamu yönetimi ve siyasal bilimler "
    "dışındaki öğretim kurumlarından lisans mezunu olanlar, bu dallardan lisansüstü seviyede diploma almışlarsa öğrenim "
    "şartını sağlar.",
    zorluk="hard")

P.q("3568 s. Kanun m. 5/A-c",
    f"{K}, aşağıdakilerden hangisi serbest muhasebeci mali müşavirlik sınavını kazanmış olma şartının aranmadığı durumdur?",
    "Vergi inceleme yetkisi alıp yeterlilik sınavından sonra YMM sınavını vermek",
    ["Kanunda sayılan dallarda doktora derecesi almış ve üç yıl staj yapmış olmak",
     "Bir kamu kurumunda on yıl muhasebe müdürlüğü yapmış olmak",
     "Yabancı bir ülkede muhasebecilik ruhsatı almış olmak",
     "Temel Eğitim ve Staj Merkezinin programını dereceyle bitirmiş olmak"],
    "Kanun m. 5/A-c'ye göre kanunları uyarınca vergi inceleme yetkisini almış ve mesleki yeterlilik sınavında başarılı "
    "olduktan sonra yeminli mali müşavirlik sınavını vermiş olanlarda SMMM sınavını kazanmış olma şartı aranmaz.",
    zorluk="hard")

# ================================================================ staj (Kanun m. 6) — ayrıntısı ruhsat_ve_staj konusunda
P.q("3568 s. Kanun m. 6/1",
    f"{K}, serbest muhasebeci mali müşavirlik stajına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Staj, bağımlı çalışan meslek mensubu yanında da yapılabilir.",
    ["Staj, bağımsız çalışan SMMM veya YMM yanında ya da şirketlerinde yapılır.",
     "Staja başlamak için staja giriş sınavını kazanmak şarttır.",
     "TESMER'in eğitim programını tamamlayıp başarılı olmak staja başlama şartıdır.",
     "TESMER kurs ve seminerlerinde geçen ve altı ayı aşmayan süreler stajdan sayılır."],
    "Kanun m. 6'ya göre staj bağımsız çalışan SMMM veya YMM yanında ya da şirketlerinde yapılır; staja başlamak için staja "
    "giriş sınavını kazanmak ve Temel Eğitim ve Staj Merkezinin programını başarıyla tamamlamak şarttır; bu kurslarda "
    "geçen ve altı ayı aşmayan süreler stajdan sayılır.")

P.q("3568 s. Kanun m. 6/2",
    f"{K}, aşağıdaki hizmet sürelerinden hangisi staj süresinden sayılmaz?",
    "Bir ticaret şirketinde satış müdürü olarak geçen süreler",
    ["Vergi incelemesine yetkili olanların bu yetkiyi aldıktan sonra kamu hizmetinde geçen süreleri",
     "Vergi yargısında görev yapan hâkimlerin bu görevlerde geçen süreleri",
     "Kanunda sayılan dallarda öğretim üyesi veya araştırma görevlisi olarak geçen süreler",
     "SPK'da denetime yetkili olarak çalışanların bu hizmetlerde geçen süreleri"],
    "Kanun m. 6/2 vergi inceleme elemanları, banka ve hazine denetçileri, SPK ve KGK uzmanları, vergi yargısı hâkimleri, "
    "belirli müfettiş ve kontrolörler, birinci derece imza yetkili muhasebe sorumluları ve ilgili dallarda öğretim "
    "elemanlarının sürelerini stajdan sayar. Satış müdürlüğü bu kapsamda değildir.")

# ================================================================ sınav ve yabancılar
P.q("3568 s. Kanun m. 7",
    f"{K}, serbest muhasebeci mali müşavirlik sınav komisyonuna ilişkin aşağıdaki ifadelerden hangisi doğrudur?",
    "Komisyon 7 üyeden oluşur; üyelerin 2'si Hazine ve Maliye Bakanlığını temsil eder.",
    ["Komisyon 9 üyeden oluşur; üyelerin 4'ü Hazine ve Maliye Bakanlığını temsil eder.",
     "Komisyon 5 üyeden oluşur; üyelerin tamamı Birlik Yönetim Kurulunca seçilir.",
     "Komisyon 7 üyeden oluşur; üyelerin 4'ü YÖK'ün önerdiği adaylar arasından seçilir.",
     "Komisyon 7 üyeden oluşur; üyeleri Birlik Genel Kurulu seçer ve Bakanlık onaylar."],
    "Kanun m. 7'ye göre SMMM sınav komisyonu 7 üyedir: 2 üye Bakanlığı temsil eder; 3 üye YÖK'ün teklif edeceği 5 aday, "
    "2 üye Birliğin teklif edeceği 4 aday arasından Bakan tarafından seçilir. Sınav Birlik tarafından yazılı yapılır.")

P.sayisal("3568 s. Kanun m. 7 ve 10",
    f"{K}, SMMM ve YMM sınav komisyonu üyeliklerine aday gösterileceklerin ilgili dallarda en az kaç yıl çalışmış veya öğretim üyeliği yapmış olması şarttır?",
    "15", ["5", "8", "10", "20"],
    "Kanun m. 7 ve m. 10'a göre sınav komisyonu üyeliklerine aday gösterileceklerin hukuk, iktisat, maliye, muhasebe, "
    "işletme, bankacılık veya idari bilimler dallarından mezun olup bu konularda on beş yıl çalışmış veya bu kadar süre "
    "öğretim üyeliği yapmış olmaları şarttır.")

P.q("3568 s. Kanun m. 10",
    f"{K}, yeminli mali müşavirlik sınav komisyonunun oluşumu aşağıdakilerin hangisinde doğru olarak verilmiştir?",
    "Dördü Bakanlık vergi denetim elemanı, biri YÖK'ün, ikisi Birliğin önerdiği adaylardan olmak üzere yedi üye",
    ["İkisi Bakanlık temsilcisi, üçü YÖK'ün, ikisi Birliğin önerdiği adaylardan olmak üzere yedi üye",
     "Üçü Bakanlık vergi denetim elemanı, ikisi YÖK'ün, ikisi Birliğin önerdiği adaylardan olmak üzere yedi üye",
     "Dördü Birliğin, üçü Bakanlık vergi denetim elemanları arasından seçilen yedi üye",
     "Beşi Bakanlık vergi denetim elemanı, ikisi YÖK'ün önerdiği adaylardan olmak üzere yedi üye"],
    "Kanun m. 10'a göre YMM sınav komisyonu biri başkan yedi üyedir: dördü Bakanlık vergi denetim elemanları arasından, "
    "biri YÖK'ün önereceği iki aday arasından, ikisi Birliğin önereceği dört aday arasından Bakan tarafından seçilir.",
    zorluk="hard")

P.sayisal("3568 s. Kanun m. 10 son fıkra",
    f"{K}, SMMM ve YMM sınav sonuçlarının yargıya intikal etmesi ve mahkemece bilirkişi incelemesine gerek görülmesi hâlinde kaç kişilik bir bilirkişi heyeti tayin edilir?",
    "3", ["1", "2", "5", "7"],
    "Kanun m. 10'a göre biri Bakanlık merkezi vergi denetim elemanı, biri alanında uzman meslek mensubu, biri dava edilen "
    "sınav konusunda ihtisas sahibi öğretim üyesi olmak üzere, sınav komisyonunda görev almamış üç kişilik bilirkişi "
    "heyeti tayin edilir.")

P.q("3568 s. Kanun m. 8",
    f"{K}, yabancı serbest muhasebeci mali müşavirlerin Türkiye'de mesleki faaliyette bulunabilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Karşılıklılık şartıyla ve Cumhurbaşkanının onayıyla izin verilebilir.",
    ["Birlik Yönetim Kurulunun kararıyla, karşılıklılık aranmaksızın izin verilir.",
     "Ancak Türk vatandaşlığına geçtikten sonra SMMM sınavına girerek faaliyette bulunabilirler.",
     "Hazine ve Maliye Bakanlığının izniyle ve yabancı sermayeli şirketlere hizmet vermek üzere izin verilir.",
     "İlgili oda genel kurulunun kararıyla ve bir yıllık staj şartıyla izin verilir."],
    "Kanun m. 8'e göre mesleği resmen düzenlemiş yabancı bir devletin vatandaşlarına, Türk SMMM'lerde aranan nitelikleri "
    "taşımak şartıyla ve karşılıklılık esasıyla, m. 2 kapsamındaki hizmetleri SMMM unvanı altında Türkiye'de yapmalarına "
    "Cumhurbaşkanının onayıyla izin verilebilir.")

P.q("3568 s. Kanun m. 8/A",
    f"{K}, serbest muhasebeci mali müşavirlerin KDV iadesine dayanak rapor düzenlemesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Beyannamesini imzaladıkları dönem ve mükelleflerle sınırlı olarak rapor düzenletilebilir.",
    ["Beyannamesini imzalamadıkları mükellefler için de, Bakanlık onayı alınarak rapor düzenleyebilirler.",
     "Rapor düzenleme yetkisi, SMMM'lere Birlik Yönetim Kurulu kararıyla doğrudan verilmiştir.",
     "Raporun doğru olmamasından SMMM sorumlu tutulamaz; sorumluluk mükellefe aittir.",
     "Rapor düzenleme yetkisi, ihracat istisnasından doğan iadelerle sınırlıdır."],
    "7104 sayılı Kanunla eklenen m. 8/A'ya göre Bakanlık, SMMM'lere beyannamelerini imzaladıkları dönem ve mükelleflerle "
    "sınırlı olmak kaydıyla KDV iadesine dayanak rapor düzenlettirmeye ve şartları belirlemeye yetkilidir; SMMM raporun "
    "doğruluğundan sorumludur.")

P.q("3568 s. Kanun m. 8/A/2",
    "SMMM (C)'nin düzenlediği KDV iade raporunun gerçeğe aykırı olduğu ve mükellefe fazla iade yapıldığı tespit edilmiştir. "
    f"{K}, (C)'nin sorumluluğu aşağıdakilerden hangisidir?",
    "Rapor kapsamı ile sınırlı olarak vergi ve cezalardan mükellefle müştereken ve müteselsilen sorumludur.",
    ["Raporun kapsamına bakılmaksızın mükellefin bütün vergi borçlarından müştereken ve müteselsilen sorumludur.",
     "Rapor kapsamındaki vergi aslından sorumludur; kesilecek cezalar mükellefe aittir.",
     "Disiplin sorumluluğu doğar; mali sorumluluk mükellefe aittir.",
     "Mükelleften tahsil edilemeyen tutar için ikinci derecede sorumludur."],
    "Kanun m. 8/A/2'ye göre SMMM'ler iadeye ilişkin raporların doğru olmasından sorumludur; rapor doğru değilse rapor "
    "kapsamı ile sınırlı olarak ziyaa uğratılan vergilerden ve kesilecek cezalardan mükellefle birlikte müştereken ve "
    "müteselsilen sorumlu olurlar.")

# ================================================================ YMM şartları, yemin, tasdik
P.sayisal("3568 s. Kanun m. 9",
    f"{K}, yeminli mali müşavir olabilmek için en az kaç yıl serbest muhasebeci mali müşavirlik yapmış olmak gerekir?",
    "10", ["3", "5", "7", "15"],
    "Kanun m. 9'a göre YMM olabilmek için en az 10 yıl serbest muhasebeci mali müşavirlik yapmış olmak, YMM sınavını vermiş "
    "olmak ve YMM ruhsatını almış olmak gerekir.")

P.q("3568 s. Kanun m. 9/2",
    f"{K}, aşağıdaki hizmet sürelerinden hangisi yeminli mali müşavirlik için aranan serbest muhasebeci mali müşavirlikte geçmiş süre olarak kabul edilmez?",
    "Kanunda sayılmayan bir dalda öğretim üyesi olarak geçen süreler",
    ["Vergi inceleme yetkisi alanların bu tarihten sonra kamu kurumlarında geçen süreleri",
     "YMM ve SMMM şirketlerinde geçen hizmet süreleri",
     "Bir işyerine bağlı olarak çalışan SMMM'lerin bu işyerlerinde geçen süreleri",
     "Kanunda sayılan dallarda öğretim üyeliği yapanların bu süreleri"],
    "Kanun m. 9/2'ye göre vergi inceleme elemanlarının yetki aldıktan sonraki süreleri, birinci derece imza yetkili muhasebe "
    "sorumluluğu, SMMM ve YMM şirketlerinde ve işyerine bağlı SMMM olarak geçen süreler ile hukuk, iktisat, maliye, "
    "işletme, muhasebe, bankacılık, kamu yönetimi ve siyasal bilimler dallarında öğretim üyeliği süreleri kabul edilir.")

P.q("3568 s. Kanun m. 11",
    f"{K}, yeminli mali müşavirlik mesleğine kabul edilenler görevlerine fiilen başlamadan önce nerede yemin ederler?",
    "Asliye Ticaret Mahkemesinde",
    ["Asliye Hukuk Mahkemesinde", "Sulh Hukuk Mahkemesinde", "Birlik Genel Kurulunda", "Vergi Mahkemesinde"],
    "Kanun m. 11'e göre YMM mesleğine kabul edilenler görevlerine fiilen başlamadan önce Asliye Ticaret Mahkemesinde "
    "Kanunda yazılı şekilde yemin ederler.",
    zorluk="easy")

P.q("3568 s. Kanun m. 12",
    f"{K}, yeminli mali müşavirlerin tasdikine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tasdikli mali tablolar, kamu idaresinin teftiş ve inceleme yetkisini ortadan kaldırır.",
    ["YMM'ler mali tablo ve beyannamelerin mevzuata ve standartlara uygunluğunu tasdik eder.",
     "Tasdik edilecek belgeler ve tasdik usulleri Bakanlıkça çıkarılan yönetmeliklerle belirlenir.",
     "Tasdik edilmiş mali tablolar tasdikin kapsamı ölçüsünde incelenmiş belge kabul edilir.",
     "YMM'ler tasdikin kapsamını düzenleyecekleri raporda açıkça belirtir."],
    "Kanun m. 12/3'e göre tasdik edilmiş mali tablolar kamu idaresince tasdikin kapsamı ölçüsünde incelenmiş belge kabul "
    "edilir; ancak çeşitli kanunlarla kamu idaresine tanınan teftiş ve inceleme yetkilerinin kullanılması ve tekrarı "
    "saklıdır.")

P.sayisal("3568 s. Kanun m. 12/5 (6552 s. Kanunla eklenen fıkra)",
    f"{K}, yeminli mali müşavir hakkında sorumluluk raporu yazılabilmesi için istenen yazılı savunma, savunma isteme yazısının tebliğinden itibaren kaç gün içinde yapılmazsa savunma hakkından vazgeçilmiş sayılır?",
    "30", ["7", "10", "15", "60"],
    "6552 sayılı Kanunla m. 12'ye eklenen fıkraya göre YMM'lerin tasdikten doğan mali ve disiplin sorumlulukları ayrı "
    "müstakil raporla tespit edilir; sorumluluk raporu için yazılı savunma istenir ve tebliğden itibaren otuz gün içinde "
    "savunma yapılmazsa savunma hakkından vazgeçilmiş sayılır.",
    zorluk="hard")

P.q("3568 s. Kanun m. 12/5",
    f"{K}, yeminli mali müşavirlerin tasdikten doğan mali sorumlulukları ile disiplin sorumluluklarının tespitine ilişkin aşağıdakilerden hangisi doğrudur?",
    "İki sorumluluk ayrı ayrı müstakil bir rapor ile tespit edilir.",
    ["İki sorumluluk vergi inceleme raporunun içinde birlikte tespit edilir.",
     "Mali sorumluluk mahkeme kararıyla, disiplin sorumluluğu oda kararıyla tespit edilir.",
     "Disiplin sorumluluğu tespit edilmeden mali sorumluluk raporu yazılamaz.",
     "Mali sorumluluk Birlik tarafından, disiplin sorumluluğu Bakanlık tarafından tespit edilir."],
    "Kanun m. 12'ye 6552 sayılı Kanunla eklenen fıkraya göre YMM'lerin tasdikten doğan mali sorumlulukları ile disiplin "
    "sorumlulukları ayrı ayrı müstakil bir rapor ile tespit edilir.")

P.q("3568 s. Kanun m. 13",
    f"{K}, meslek mensuplarının mesleği yapmaları yasaklanan kişilerle ilişkisine dair aşağıdakilerden hangisi doğrudur?",
    "Bu kişileri bürolarında çalıştıramaz ve onlarla mesleki işbirliği yapamazlar.",
    ["Bu kişileri, oda yönetim kurulunun izniyle yardımcı eleman olarak çalıştırabilirler.",
     "Bu kişilerle mesleki işbirliği yapabilir, ancak onları bürolarında çalıştıramazlar.",
     "Bu kişileri yasak süresi dolana kadar stajyer statüsünde çalıştırabilirler.",
     "Bu kişilerle, müşteriye bilgi vermek koşuluyla ortak iş yürütebilirler."],
    "Kanun m. 13'e göre meslek mensupları kişisel veya ortak bürolarında mesleği yapmaları yasaklananları çalıştıramaz ve "
    "bunlarla her ne şekilde olursa olsun meslekleri ile ilgili işbirliği yapamaz. M. 49'a göre aykırılık adli para "
    "cezası gerektirir.")

# ================================================================ yasaklar ve bağdaşan işler (Kanun m. 45)
P.q("3568 s. Kanun m. 45/1",
    f"{K}, meslek mensuplarına ilişkin yasaklar arasında aşağıdakilerden hangisi yer almaz?",
    "Anonim şirkette pay sahibi olmak",
    ["Unvanıyla, m. 2'deki işler için bir işyerine bağlı hizmet akdiyle çalışmak",
     "Ticari faaliyette bulunmak",
     "Meslekle ve meslek onuru ile bağdaşmayan işlerle uğraşmak",
     "İş elde etmek için reklam sayılabilecek faaliyette bulunmak"],
    "Kanun m. 45'e göre meslek mensupları unvanlarıyla m. 2'deki işler için hizmet akdiyle çalışamaz, ticari faaliyette "
    "bulunamaz, meslekle bağdaşmayan işlerle uğraşamaz ve reklam sayılabilecek faaliyette bulunamaz. Anonim şirkette "
    "pay sahibi olmak yasak değildir.")

P.q("3568 s. Kanun m. 45/2",
    "Yeminli mali müşavir (D)'ye, kardeşinin eşinin (baldızının) yönetim kurulu üyesi ve ortağı olduğu (K) A.Ş.'nin "
    f"kurumlar vergisi beyannamesini tasdik etmesi teklif edilmiştir. {K}, bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "Üçüncü dereceye kadar sıhri hısımın ortak olduğu firmanın işine bakamaz.",
    ["Sıhri hısımlık eşin kan hısımlarıyla sınırlı olduğu için tasdik yapabilir.",
     "Yönetimde görev alsa da ortaklık payı yüzde onun altındaysa tasdik yapabilir.",
     "Akrabalık ikinci dereceyi aştığı için tasdik yapmasına engel yoktur.",
     "Oda yönetim kurulundan izin alırsa tasdik yapabilir."],
    "Kanun m. 45/2'ye göre YMM'ler eşi (boşanmış dahi olsa), usul ve füruu ile 3. dereceye kadar kan ve sıhri hısımlarının "
    "veya bunların ortak oldukları firmaların işlerine bakamaz. Kardeşin eşi ikinci derece sıhri hısımdır.",
    zorluk="hard")

P.q("3568 s. Kanun m. 45/3",
    f"{K}, aşağıdaki görevlerden hangisi meslekle bağdaşmayan işler sayılmaz?",
    "Şartlarıyla bir KİT'in yönetim kurulu üyeliği",
    ["Bir ticari işletmeyi tacir sıfatıyla işletmek",
     "Bir kollektif şirkette ortak olmak",
     "Bir sigorta şirketinin acenteliğini yapmak",
     "Bir ticari işletmenin ticari mümessili olmak"],
    "Kanun m. 45/3'e göre hayri ve ilmi kuruluşlar, KİT'ler, kamu idarelerinin hissedarı olduğu kurumlar ve TMSF "
    "yönetimindeki kurumlarda, bu kurumların Kanun kapsamındaki faaliyetlerini yürütmemek şartıyla yönetim kurulu "
    "başkanlığı, üyeliği, denetçiliği ile bilirkişilik ve tasfiye memurluğu meslekle bağdaşmayan iş sayılmaz.",
    zorluk="hard")

P.q("3568 s. Kanun m. 45/4",
    f"{K}, meslek mensuplarının çalışmalarını birleştirmelerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Şirket şeklinde çalışılması hâlinde işlerden doğan cezai sorumluluk şirkete aittir.",
    ["Birden çok meslek mensubu çalışmalarını ortaklık bürosu veya şirket şeklinde birleştirebilir.",
     "Bu bürolarda yapılan faaliyetler ticari faaliyet sayılmaz.",
     "Birleşme SMMM veya YMM ortaklık bürosu ya da şirketi şeklinde olabilir.",
     "Şirket şeklinde çalışmada cezai sorumluluk işi yapan meslek mensubuna aittir."],
    "Kanun m. 45/4'e göre şirket şeklinde çalışılması hâlinde yapılan işlerden doğacak cezai sorumluluk işi yapan meslek "
    "mensubuna aittir; şirkete değil.")

P.q("3568 s. Kanun m. 45/5",
    f"{K}, meslek mensuplarının tabela ve basılı kâğıtlarında kullanabilecekleri sıfatlara ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ruhsatname ile belirlenen mesleki unvanları dışında başka sıfat kullanamazlar.",
    ["Mesleki unvanlarının yanında kamuda geçmiş görev unvanlarını kullanabilirler.",
     "Oda yönetim kurulunun izniyle ticari bir marka adı kullanabilirler.",
     "Mesleki unvan yerine “mali danışman” ifadesini tercih edebilirler.",
     "Tabela ve basılı kâğıtlarda sıfat kullanımına ilişkin bir sınırlama yoktur."],
    "Kanun m. 45/5'e göre meslek mensupları iş elde etmek için reklam sayılabilecek faaliyette bulunamaz; tabela veya "
    "basılı kâğıtlarında ruhsatname ile belirlenen mesleki unvanları dışında başka sıfat kullanamaz.")

P.q("3568 s. Kanun m. 45 son fıkra (6460 s. Kanunla eklenen)",
    "SMMM (E), kat mülkiyetine tabi bir apartmanda tapuda mesken olarak gösterilen dairesini büro olarak kullanmak "
    f"istemektedir; kat malikleri buna itiraz etmektedir. {K}, bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "Kat maliklerinin izni aranmaksızın bu bağımsız bölümde mesleki faaliyette bulunabilir.",
    ["Kat maliklerinin oybirliğiyle izin vermesi hâlinde mesleki faaliyette bulunabilir.",
     "Yönetim planında aksine hüküm varsa bu bağımsız bölümde faaliyette bulunamaz.",
     "Kat maliklerinin üçte ikisinin izniyle mesleki faaliyette bulunabilir.",
     "Mesken olarak gösterilen bağımsız bölümde mesleki faaliyet yürütülemez."],
    "6460 sayılı Kanunla m. 45'e eklenen fıkraya göre 634 sayılı Kat Mülkiyeti Kanununa göre mesken olarak gösterilen "
    "bağımsız bölümlerde kat maliklerinin izni ve benzeri şartlar aranmaksızın SMMM veya YMM faaliyetinde bulunulabilir; "
    "yönetim planındaki aksine hükümler uygulanmaz. Ev ile büronun aynı yer olamayacağına ilişkin Çalışma Usul ve "
    "Esasları hükmü ayrıca saklıdır.",
    zorluk="hard")

# ================================================================ Başvurular Yönetmeliği
P.q("Başvurular Hakkında Yön. m. 5",
    f"{BY}, serbest muhasebeci mali müşavirlik ruhsatı için başvuru nereye yapılır?",
    "İkametgâhının bulunduğu ildeki odaya",
    ["Staj yapılan meslek mensubunun kayıtlı olduğu odaya",
     "Doğrudan TÜRMOB Genel Sekreterliğine",
     "İlgilinin nüfusa kayıtlı olduğu ildeki vergi dairesine",
     "TESMER'in bölge temsilciliğine"],
    "Başvurular Yönetmeliği m. 5'e göre SMMM başvurusu ilgilinin ikametgâhının bulunduğu ildeki odaya, ilde oda "
    "bulunmuyorsa ilin bağlı olduğu odaya dilekçe ve başvuru formuyla yapılır.")

P.q("Başvurular Hakkında Yön. m. 5/3",
    f"{BY}, aşağıdakilerden hangisi serbest muhasebeci mali müşavirlik başvuru formuna eklenmesi gereken belgeler arasında yer almaz?",
    "Son üç yılın onaylı bilançoları",
    ["Onaylı nüfus cüzdanı örneği",
     "Sınav başarı belgesi ve staj bitirme belgesi",
     "Diploma veya çıkış belgesinin aslı ya da onaylı örneği",
     "Savcılıktan alınacak sabıka kaydı belgesi"],
    "Başvurular Yönetmeliği m. 5'e göre SMMM başvurusuna nüfus cüzdanı örneği, ikametgâh, sınav başarı ve staj bitirme "
    "belgesi, fotoğraf, diploma ve sabıka kaydı eklenir. Son üç yılın onaylı bilançoları m. 6'ya göre YMM başvurusunda "
    "aranır.",
    zorluk="hard")

P.sayisal("Başvurular Hakkında Yön. m. 7",
    f"{BY}, bilgi ve belgeleri tam ve doğru olan ruhsat başvuruları ilgili oda tarafından başvuru gününden en geç kaç gün içinde Birliğe gönderilir?",
    "60", ["15", "30", "45", "90"],
    "Başvurular Yönetmeliği m. 7'ye göre oda başvuru dosyasını inceler; tam ve doğru olanları başvuru gününden en geç altmış "
    "gün içinde Birliğe gönderir; eksik veya yanlış olanları aynı süre içinde gerekçesiyle Birliğe ve ilgiliye bildirir.")

P.q("Başvurular Hakkında Yön. m. 7",
    "Ruhsatı düzenlenen (F)'ye oda tarafından iadeli taahhütlü tebligat yapılmış, ancak (F) ruhsatını almamıştır. "
    f"{BY}, bu durumda uygulanacak usul aşağıdakilerden hangisidir?",
    "On beş günde alınmazsa en az on günlük ikinci süre verilir; bu sürede de alınmazsa ruhsat Birliğe iade edilir.",
    ["Otuz günde alınmazsa ruhsat iptal edilir ve (F) yeniden sınava girer.",
     "Yedi günde alınmazsa ruhsat noter aracılığıyla (F)'nin adresine gönderilir.",
     "Altmış günde alınmazsa (F) hakkında uyarma cezası verilir ve ruhsat odada saklanır.",
     "Süre sınırı yoktur; ruhsat (F) başvurana kadar odada bekletilir."],
    "Başvurular Yönetmeliği m. 7'ye göre tebliğ tarihinden itibaren on beş gün içinde ruhsatını almayanlara on günden az "
    "olmamak üzere ikinci bir süre verilir; bu süre içinde de alınmazsa ruhsat Birliğe iade olunur ve bu husus ikinci "
    "tebligatta açıkça belirtilir.",
    zorluk="hard")

P.q("Başvurular Hakkında Yön. m. 9",
    f"{BY}, Birliğin ruhsatnamenin verilemeyeceğine dair kararına karşı itiraza ilişkin aşağıdakilerden hangisi doğrudur?",
    "İtiraz mercii Bakandır; itiraz süresi tebliğden itibaren otuz gündür ve Bakanın kararı nihaidir.",
    ["İtiraz mercii Birlik Genel Kuruludur; itiraz süresi on beş gündür ve genel kurul kararı nihaidir.",
     "İtiraz mercii idare mahkemesidir; dava açma süresi altmış gündür.",
     "İtiraz mercii oda yönetim kuruludur; itiraz süresi yedi gündür ve Birliğe iletilir.",
     "İtiraz mercii Birlik Disiplin Kuruludur; itiraz süresi otuz gündür ve kurul kararı kesindir."],
    "Başvurular Yönetmeliği m. 9'a göre Birlik kararına karşı itiraz mercii Bakandır; itiraz süresi kararın tebliğinden "
    "itibaren otuz gündür; dilekçe Birliğe verilir ve Birlik dosyayı en geç on beş gün içinde Bakanlığa gönderir; "
    "Bakanın kararı nihaidir.",
    zorluk="hard")

P.q("Başvurular Hakkında Yön. m. 10",
    f"{BY}, ruhsatını alan meslek mensubunun mesleki faaliyete başlamasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "İlgili odanın çalışanlar listesine kayıt olduktan sonra faaliyete başlayabilir.",
    ["Ruhsatın Resmî Gazete'de ilan edilmesinden sonra faaliyete başlayabilir.",
     "Ruhsatın tebliğ edildiği gün, odaya kayıt aranmaksızın faaliyete başlayabilir.",
     "Vergi dairesinde mükellefiyet tesisiyle birlikte odaya kayıt aranmadan başlayabilir.",
     "Birlik Genel Kurulunun onayından sonra faaliyete başlayabilir."],
    "Başvurular Yönetmeliği m. 10'a göre ruhsatını alan meslek mensupları ilgili odanın çalışanlar listesine kayıt "
    "olduktan sonra mesleki faaliyete başlayabilir; ruhsat almayan veya listeye kaydolmayanlar faaliyette bulunamaz ve "
    "haklarında Kanunun cezai hükümleri uygulanır.")

P.q("Başvurular Hakkında Yön. m. 6",
    f"{BY}, aşağıdakilerden hangisi yeminli mali müşavirlik başvurusuna eklenmesi gereken belgelerden biridir?",
    "En az on yıllık SMMM'lik belgesi",
    ["Oda yönetim kurulundan alınacak referans mektubu",
     "Staj yapılan meslek mensubundan alınacak tezkiye belgesi",
     "Son beş yılın gelir vergisi beyannameleri",
     "TESMER eğitim programı katılım belgesi"],
    "Başvurular Yönetmeliği m. 6'ya göre YMM başvurusuna nüfus cüzdanı örneği, ikametgâh, staj bitirme ve sınav başarı "
    "belgesi, son üç yılın onaylı bilançoları, diploma, fotoğraf ve en az on yıl SMMM'lik yapıldığını gösteren belge "
    "eklenir.")

# ================================================================ Kaşe Yönetmeliği
P.q("Kaşe Kullanma Yön. m. 2 ve 5",
    f"{KY}, kaşe kullanma yükümlülüğü ve kaşenin temini ile ilgili aşağıdakilerden hangisi doğrudur?",
    "Kaşeler Birlik tarafından bedel karşılığında verilir; talep formları odalarca Birliğe gönderilir.",
    ["Kaşeler meslek mensubunca istenilen biçimde yaptırılır ve odaya bildirilir.",
     "Kaşeler vergi dairelerince ücretsiz verilir ve beş yılda bir yenilenir.",
     "Kaşe kullanma zorunluluğu ortaklık bürosu kuran meslek mensuplarına özgüdür.",
     "Kaşeler oda yönetim kurulunca yaptırılır ve Birliğe bildirilmeden verilir."],
    "Kaşe Yönetmeliği m. 2 ve 5'e göre çalışanlar listesine kayıtlı meslek mensupları ile listeye kayıtlı olmadığı hâlde "
    "çalıştığı mükellefin muhasebesinden sorumlu olup beyannamelerini imzalayanlar özel kaşe kullanır; kaşeler Birlik "
    "tarafından bedel karşılığında verilir.")

P.q("Kaşe Kullanma Yön. m. 6 ve 7",
    f"{KY}, kaşelerin şekli ve ücretine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kaşeler daire şeklindedir.",
    ["Kaşelerin en üstünde “TC” rumuzu bulunur.",
     "Kaşelerde “TÜRMOB” yazısı ve “Mm” amblemi yer alır.",
     "Kaşeler Darphane ve Damga Matbaası Genel Müdürlüğünce imal edilir.",
     "Kaşe ücretleri kaşelerin verilmesinden önce tahsil edilir."],
    "Kaşe Yönetmeliği m. 6'ya göre kaşeler kare şeklindedir; m. 7'ye göre kaşe ücretleri Birlik Genel Kurulunca tespit "
    "edilir ve kaşe verilmeden önce tahsil edilir.")

P.sayisal("Kaşe Kullanma Yön. m. 9",
    f"{KY}, ruhsatın iptali, meslekten ayrılma veya ölüm hâlinde meslek mensupları ya da mirasçıları kaşeyi kaç gün içinde bağlı oldukları odaya tutanakla iade eder?",
    "15", ["7", "10", "30", "60"],
    "Kaşe Yönetmeliği m. 9'a göre ruhsatın iptali, meslekten ayrılma, ölüm ve diğer hallerde meslek mensupları veya "
    "mirasçıları kaşeyi 15 gün içinde bağlı oldukları odalara tutanak karşılığında iade eder.")

P.q("Kaşe Kullanma Yön. m. 10, 11 ve 14",
    f"{KY}, aşağıdaki ifadelerden hangisi doğrudur?",
    "Odalar arasında nakil, kaşenin değiştirilmesini gerektirmez.",
    ["Başka bir odaya nakilde eski kaşe iade edilerek yeni numaralı kaşe alınır.",
     "Unvan değişikliğinde eski kaşe kullanılmaya devam edilir.",
     "Kaybedilen kaşe için gazete ilanı gerekmez; odaya dilekçe yeterlidir.",
     "Kaşe kaybında yeni kaşe bedelsiz olarak verilir."],
    "Kaşe Yönetmeliği m. 14'e göre odalar arasında nakil kaşenin değiştirilmesini gerektirmez. Unvan değişikliğinde eski "
    "kaşe iade edilip yenisi alınır (m. 10); kaşe kaybında 15 gün içinde gazete ilanıyla odaya başvurularak bedeli "
    "karşılığında yeni kaşe istenir (m. 11).")

P.q("Kaşe Kullanma Yön. m. 11",
    f"{KY}, kaşesini kaybeden meslek mensubunun yapması gereken aşağıdakilerden hangisidir?",
    "15 gün içinde gazetede yayımlanan kayıp ilanıyla odasına başvurarak bedeli karşılığında yeni kaşe ister.",
    ["30 gün içinde noter onaylı kayıp tutanağıyla Birliğe başvurarak ücretsiz yeni kaşe ister.",
     "Durumu vergi dairesine bildirir; vergi dairesi yeni kaşeyi resen düzenleyerek odaya gönderir.",
     "7 gün içinde karakol tutanağıyla odaya başvurur; oda kayıp kaşenin numarasını değiştirmeden yenisini verir.",
     "Kaşe yenilenmez; meslek mensubu yeni kaşe alana kadar imzasıyla belge düzenler."],
    "Kaşe Yönetmeliği m. 11'e göre kaşesini kaybeden meslek mensupları 15 gün içinde gazetede yayımlanan kayıp ilanıyla "
    "birlikte bağlı oldukları odaya başvurarak bedeli karşılığında yeni kaşe talep eder.")

# ================================================================ uygulama ve karma
P.q("3568 s. Kanun m. 2/A son fıkra",
    f"{K}, mesleğin konusuna giren işleri bir işyerine bağlı olmaksızın yapanlara ne ad verilir?",
    "Serbest muhasebeci mali müşavir",
    ["Yeminli mali müşavir", "Bağımsız denetçi", "Mali danışman", "Muhasebe uzmanı"],
    "Kanun m. 2/A'nın son fıkrasına göre muhasebecilik ve mali müşavirlik mesleğinin konusuna giren işleri bir işyerine "
    "bağlı olmaksızın yapanlara serbest muhasebeci mali müşavir denir.",
    zorluk="easy")

P.q("3568 s. Kanun m. 1 ve 2",
    f"{K}, serbest muhasebecilik unvanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "5786 sayılı Kanunla Kanundaki “serbest muhasebeci” unvanı ve ibareleri metinden çıkarılmıştır.",
    ["Serbest muhasebecilik unvanı Kanunda SMMM'nin alt kademesi olarak düzenlenmeye devam etmektedir.",
     "Serbest muhasebecilik unvanı 2025 yılında 7546 sayılı Kanunla yeniden getirilmiştir.",
     "Serbest muhasebeciler, beş yıllık deneyimle doğrudan YMM sınavına girebilir.",
     "Serbest muhasebecilik stajı, SMMM stajının ilk iki yılı olarak devam etmektedir."],
    "10.07.2008 tarihli 5786 sayılı Kanunla Kanunun adı “Serbest Muhasebeci Mali Müşavirlik ve Yeminli Mali Müşavirlik "
    "Kanunu” olarak değiştirilmiş ve metindeki “serbest muhasebeci” ibareleri çıkarılmıştır; mevcut serbest "
    "muhasebeciler geçiş hükümlerine tabidir.",
    zorluk="hard")

P.oncul("3568 s. Kanun m. 4 ve 5",
    "Meslek mensubu olmak isteyen bir kişi için aşağıdaki şartlar sayılmıştır:",
    ["T.C. vatandaşı olmak",
     "En az üç yıl staj yapmış olmak",
     "Kamu haklarından mahrum bulunmamak",
     "Serbest muhasebeci mali müşavirlik ruhsatını almış olmak"],
    f"{K}, yukarıdakilerden hangileri meslek mensubu olabilmenin genel şartlarındandır?",
    "I ve III",
    ["Yalnız I", "I ve III", "II ve IV", "I, II ve III", "II, III ve IV"],
    "Kanun m. 4'e göre T.C. vatandaşlığı ve kamu haklarından mahrum olmamak genel şartlardandır. Üç yıl staj ve SMMM "
    "ruhsatı almak m. 5/A'daki özel şartlardır.")

P.oncul("3568 s. Kanun m. 45",
    "Serbest muhasebeci mali müşavirlerin aşağıdaki faaliyetleri değerlendirilmektedir:",
    ["Bir vakfın yönetim kurulu üyeliği",
     "Mahkemece görevlendirilen bilirkişilik",
     "Tacir sıfatıyla bir mağaza işletmek",
     "İflas eden bir şirkette tasfiye memurluğu"],
    f"{K}, yukarıdakilerden hangileri meslekle bağdaşmayan iş sayılmaz?",
    "I, II ve IV",
    ["Yalnız II", "I ve III", "II ve IV", "I, II ve IV", "II, III ve IV"],
    "Kanun m. 45/3'e göre hayri kuruluşların (vakıf) yönetim kurulu üyeliği, bilirkişilik ve tasfiye memurluğu meslekle "
    "bağdaşmayan iş sayılmaz. Tacir sıfatıyla mağaza işletmek ticari faaliyet yasağı kapsamındadır.",
    zorluk="hard")

P.oncul("3568 s. Kanun m. 2/B, 9 ve 12",
    "Yeminli mali müşavirlerle ilgili aşağıdaki ifadeler verilmiştir:",
    ["Tasdik yetkisi yeminli mali müşavirlere özgüdür.",
     "Yeminli mali müşavirler muhasebe bürosu açabilir.",
     "Yeminli mali müşavir olmak için en az on yıl SMMM'lik yapmış olmak gerekir.",
     "Yeminli mali müşavirler tasdikin kapsamını raporda belirtmek zorunda değildir."],
    f"{K}, yukarıdaki ifadelerden hangileri doğrudur?",
    "I ve III",
    ["Yalnız I", "I ve II", "I ve III", "II ve IV", "I, III ve IV"],
    "Kanun m. 2/B ve 12'ye göre tasdik YMM'lere özgüdür; m. 9'a göre en az on yıl SMMM'lik gerekir. YMM'ler muhasebe "
    "bürosu açamaz ve m. 12'ye göre tasdikin kapsamını raporda açıkça belirtir.")

P.q("3568 s. Kanun m. 45/1 ve Çalışma Usul Yön. m. 61",
    "SMMM (G), bir sanayi şirketinde tam zamanlı muhasebe müdürü olarak hizmet akdiyle çalışmaya başlamış ve şirketin "
    f"beyannamelerini SMMM unvanıyla imzalamak istemektedir. {K}, bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "Unvanıyla ve m. 2'deki işler için hizmet akdiyle çalışamayacağından beyannameleri SMMM sıfatıyla imzalayamaz.",
    ["Şirketin yazılı muvafakatiyle SMMM unvanını kullanarak beyannameleri imzalayabilir.",
     "Hizmet akdi ticari faaliyet sayıldığından ruhsatı iptal edilir ve odaya kaydı silinir.",
     "Odaya bildirimde bulunursa hem şirkette çalışabilir hem de bürosunda müşteri kabul edebilir.",
     "Hizmet akdiyle çalışan meslek mensupları üzerinde herhangi bir sınırlama bulunmamaktadır."],
    "Kanun m. 45/1'e göre SMMM'ler bu unvanla m. 2'deki işlerin yürütülmesi amacıyla gerçek ve tüzel kişilere bağlı "
    "olarak hizmet akdiyle çalışamaz. Çalışma Usul ve Esasları Yönetmeliği m. 61'e göre hizmet akdiyle çalışanlar "
    "işyerinin unvanını belirterek unvanlarını kullanabilir, ancak tasdik yapamaz ve mesleki yetkilerini kullanamaz.",
    zorluk="hard")

P.q("3568 s. Kanun m. 49/2",
    f"{K}, meslek mensubunun Kanunun 13. maddesine aykırı olarak mesleği yapması yasaklanan kişiyi yanında çalıştırması hâlinde, fiil daha ağır bir suç oluşturmuyorsa uygulanacak yaptırım aşağıdakilerden hangisidir?",
    "Yüz güne kadar adli para cezası",
    ["Altı aydan bir yıla kadar hapis cezası", "Bir yıldan üç yıla kadar hapis cezası",
     "İdari para cezası", "Meslekten çıkarma cezası"],
    "Kanun m. 49/2'ye göre m. 13, 15/4, 41/2, 43/1, 43/2 ve 45'in birinci ve beşinci fıkralarına aykırı davrananlar "
    "hakkında, fiil daha ağır bir suç oluşturmadıkça yüz güne kadar adli para cezasına hükmolunur.",
    zorluk="hard")

P.q("3568 s. Kanun m. 49/3",
    f"{K}, Kanunun 12. maddesinin dördüncü fıkrasına aykırı davranarak, yani tasdiki gerçeğe aykırı yaparak ziyaa neden olan kişi hakkında fiil daha ağır bir suç oluşturmuyorsa öngörülen ceza aşağıdakilerden hangisidir?",
    "Altı aydan bir yıla kadar hapis ve adli para cezası",
    ["Yüz güne kadar adli para cezası",
     "Üç aydan altı aya kadar hapis cezası",
     "Bir yıldan beş yıla kadar hapis cezası",
     "Meslekten çıkarma cezası"],
    "Kanun m. 49/3'e göre m. 12'nin dördüncü fıkrasındaki hükme aykırı davranan kişi hakkında, fiil daha ağır cezayı "
    "gerektiren bir suç oluşturmadıkça altı aydan bir yıla kadar hapis ve adli para cezasına hükmolunur.",
    zorluk="hard")

P.q("Başvurular Hakkında Yön. m. 8",
    f"{BY}, staj süresinden sayılan hizmetlerde özel kuruluşlarda birinci derecede imzaya yetkili sayılanlar aşağıdakilerden hangisidir?",
    "Bilanço esasında muhasebe biriminin idaresinden sorumlu olanlar",
    ["İşletme hesabı esasına göre defter tutan işletmelerde fatura düzenleme yetkisi olanlar",
     "Şirketin ticaret sicilinde ortak olarak kayıtlı bulunan, yönetimde görevi olmayanlar",
     "Muhasebe biriminde en az beş yıl çalışmış, imza yetkisi bulunmayan uzman personel",
     "Satış biriminin sevk ve idaresinden sorumlu olan ve fatura onaylayan yöneticiler"],
    "Başvurular Yönetmeliği m. 8'e göre özel kuruluşlarda bilanço esasına göre defter tutan muhasebe birimlerinin sevk ve "
    "idaresinden veya mali denetiminden sorumlu olan ve gerekli vekaletnameyi haiz olanlar birinci derecede imzaya "
    "yetkili sayılır.")

P.q("3568 s. Kanun m. 9 son fıkra",
    "Vergi müfettişi olarak vergi inceleme yetkisini almış ve mesleki yeterlilik sınavını kazanmış olan (H), yeminli mali "
    f"müşavirlik sınavına girmek istemektedir. {K}, bu durumla ilgili aşağıdakilerden hangisi doğrudur?",
    "YMM sınavına girebilir; ruhsat için on yıl şartını tamamlaması gerekir.",
    ["YMM sınavına girmeden, yeterlilik sınavı belgesiyle doğrudan YMM ruhsatı alabilir.",
     "YMM sınavına girebilmesi için önce SMMM sınavını kazanması ve üç yıl staj yapması gerekir.",
     "YMM sınavına ancak kamu görevinden ayrıldıktan sonra beş yıl geçince girebilir.",
     "YMM sınavını kazanırsa on yıllık süre şartı aranmadan ruhsat alır."],
    "Kanun m. 9 son fıkraya göre vergi inceleme yetkisini almış ve mesleki yeterlilik sınavını vermiş olanlar, yeterlilik "
    "sınavını kazandıkları tarihten itibaren açılacak YMM sınavlarına genel hükümlere göre katılabilir; ancak YMM "
    "ruhsatını alabilmeleri için birinci fıkranın (a) bendindeki on yıllık süreyi tamamlamaları şarttır.",
    zorluk="hard")

P.q("3568 s. Kanun m. 11",
    f"{K}, yeminli mali müşavirlerin ettikleri yeminde aşağıdakilerden hangisi yer almaz?",
    "Mesleğimi Birlik kararları doğrultusunda yürüteceğime",
    ["Yeminli mali müşavirlik mesleğinin bir kamu hizmeti olduğunu bilerek",
     "Mesleğimi tam bir bağımsızlık, tarafsızlık ve dürüstlükle yerine getireceğime",
     "Üzerime aldığım işleri dikkat ve özenle yapacağıma",
     "Kanunlara, mesleki kurallara ve meslek ahlakına uyacağıma"],
    "Kanun m. 11'deki yemin metni mesleğin kamu hizmeti olduğunu bilerek kanunlara, mesleki kurallara ve meslek ahlakına "
    "uymayı; mesleği bağımsızlık, tarafsızlık ve dürüstlükle yerine getirmeyi ve işleri dikkat ve özenle yapmayı içerir.")

P.q("3568 s. Kanun m. 6/2-ı",
    f"{K}, kamu kuruluşlarının veya bilanço esasında defter tutan özel kuruluşların muhasebe birimlerinde görev yapan aday meslek mensuplarının sürelerinin stajdan sayılabilmesi için aşağıdakilerden hangisi gerekir?",
    "Birimde görevli SMMM veya YMM gözetiminde, oda nezdinde staj dosyası açtırmış olmak",
    ["Birimde en az beş yıl çalışmış ve birinci derece imza yetkisi almış olmak",
     "Birimdeki çalışmanın Birlik Yönetim Kurulunca her yıl onaylanması",
     "Birimin bağımsız denetime tabi bir şirket olması ve denetçinin onay vermesi",
     "Birimdeki çalışmanın oda genel kurulunca staj olarak kabul edilmesi ve tescili"],
    "Kanun m. 6/2-ı'ya göre bu birimlerde görev yapan SMMM veya YMM'lerin gözetim ve denetiminde, bunların sayısını geçmemek "
    "üzere, oda nezdinde staj dosyası açtırmış ve staja başlama sınavını kazanmış aday meslek mensuplarının, staj "
    "koşullarını yerine getirmeleri hâlinde bu hizmetlerde geçen süreleri stajdan sayılır.",
    zorluk="hard")

P.q("3568 s. Kanun m. 12/2",
    f"{K}, yeminli mali müşavirlerin tasdik edecekleri belgeler ile tasdike ilişkin usul ve esaslar aşağıdakilerden hangisi tarafından belirlenir?",
    "Hazine ve Maliye Bakanlığınca çıkarılacak yönetmeliklerle",
    ["Birlik Genel Kurulunca alınan mecburi meslek kararlarıyla",
     "Kamu Gözetimi Kurumunca yayımlanan denetim standartlarıyla",
     "YMM odalarının genel kurullarınca kabul edilen iç yönetmeliklerle",
     "Cumhurbaşkanı kararıyla her yıl yeniden belirlenen tebliğlerle"],
    "Kanun m. 12/2'ye göre tasdik edilecek belgeler, tasdik konuları ve usul ve esaslar; mükellefiyet şekilleri, iş "
    "kolları, cirolar, döviz kazandırıcı işlemler, ithalat ve ihracat ile yatırım miktarları esas alınarak Bakanlıkça "
    "çıkarılacak yönetmeliklerle belirlenir.")

P.q("3568 s. Kanun m. 3 ve Çalışma Usul Yön. m. 65",
    f"{K} ve Çalışma Usul ve Esasları Yönetmeliği’ne göre, mesleğin konusuna giren işleri meslek unvanını kazanmaksızın birden fazla müessesede yapan kişinin durumu aşağıdakilerden hangisidir?",
    "Meslek unvanlarının haksız kullanılması sayılır.",
    ["Ticari faaliyet sayılır ve vergi dairesine bildirilir.",
     "Bağımlı çalışma sayıldığından Kanunun kapsamı dışında kalır.",
     "Oda kaydı yapılmadığı sürece meslek faaliyeti sayılmaz.",
     "Stajyer statüsünde çalışma olarak kabul edilir."],
    "Çalışma Usul ve Esasları Yönetmeliği m. 65'e göre Kanun m. 2'deki işleri meslek unvanını kazanmaksızın birden fazla "
    "müessese veya kuruluşta yapanların faaliyetleri, Kanun m. 3'te hükme bağlanan meslek unvanlarının haksız kullanılması "
    "sayılır.")

P.q("3568 s. Kanun m. 45/2",
    "SMMM (İ)'nin defterlerini tuttuğu (P) Ltd. Şti.'nin kurumlar vergisi beyannamesini tasdik etmesi, (İ)'nin kardeşi olan "
    f"YMM (J)'den istenmiştir. {K}, (J)'nin durumu aşağıdakilerden hangisidir?",
    "Yakın akrabası olan SMMM'nin baktığı işi tasdik edemez.",
    ["Tasdik için (P) Ltd. Şti. ile arasında akrabalık aranır; kardeşin işi engel değildir.",
     "Kardeşlik ikinci derece olduğundan oda izniyle tasdik yapabilir.",
     "Şirket ortaklarının yazılı muvafakati alınırsa tasdik yapabilir.",
     "Tasdik yapabilir, ancak raporda akrabalık ilişkisini açıklaması gerekir."],
    "Kanun m. 45/2'ye göre YMM'ler, eşi, usul ve füruu ile üçüncü dereceye kadar kan ve sıhri hısımları olan SMMM'lerin "
    "baktığı işleri tasdik edemez. Kardeş ikinci derece kan hısmıdır.",
    zorluk="hard")

P.q("Kaşe Kullanma Yön. m. 1-2",
    f"{KY}, aşağıdaki meslek mensuplarından hangisinin özel kaşe kullanma yükümlülüğü yoktur?",
    "Mesleki faaliyette bulunmayan ve beyanname imzalamayan meslek mensubu",
    ["Çalışanlar listesine kayıtlı bağımsız çalışan meslek mensubu",
     "Çalışanlar listesine kayıtlı olmayıp çalıştığı mükellefin beyannamelerini imzalayan meslek mensubu",
     "Ortaklık bürosunda çalışanlar listesine kayıtlı olarak çalışan meslek mensubu",
     "Çalışanlar listesine kayıtlı ve mesleki şirkette ortak olan meslek mensubu"],
    "Kaşe Yönetmeliği m. 2'ye göre çalışanlar listesine kayıtlı meslek mensupları ile listeye kayıtlı olmayıp çalıştığı "
    "mükellefin muhasebesinden sorumlu olan ve beyannamelerini imzalayanlar özel kaşe kullanır. Faaliyette bulunmayan ve "
    "beyanname imzalamayan meslek mensubu kapsam dışındadır.")

P.q("3568 s. Kanun m. 12/6 ve 47",
    f"{K}, meslek mensuplarının vergi kanunlarındaki sorumluluklarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kanun hükümlerine göre meslek icra edenlerin vergi kanunlarındaki sorumlulukları saklıdır.",
    ["Kanun, meslek mensuplarının vergi kanunlarından doğan sorumluluğunu kaldırır.",
     "Meslek mensupları vergi kanunları bakımından mükellefin temsilcisi sayılır.",
     "Vergi kanunlarındaki sorumluluk ancak YMM'ler bakımından uygulanır.",
     "Vergi kanunlarındaki sorumluluk, disiplin cezası verildiyse ortadan kalkar."],
    "Kanun m. 12'nin son fıkrasına göre bu Kanun hükümlerine göre meslek icra edenlerin vergi kanunları ve diğer "
    "kanunlardaki sorumlulukları saklıdır; m. 47'ye göre görev suçlarında TCK'nın kamu görevlilerine ilişkin hükümleri "
    "uygulanır.")

if __name__ == "__main__":
    sys.exit(P.yaz())
