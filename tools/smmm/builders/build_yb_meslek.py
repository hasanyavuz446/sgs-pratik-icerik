# -*- coding: utf-8 -*-
"""Meslek Hukuku · Bölüm Havuzu — 3 test × 20 soru, gerçek test kitapçığı düzeninde.

Her test 2026/1-2026/2 kitapçıklarının konu ağırlığını izler: Etik İlkeler ~3, Çalışma Usul /
Haksız Rekabet / Ücret ~5, 3568 s. Kanun ~3, Odalar ve TÜRMOB ~3, Disiplin ~3, Staj / Sınav /
SMGE / sorumluluk ~3. Olumsuz kök ~%55, sayı/süre sorusu 3-4, öncüllü 2.
Dayanaklar konu builder'larıyla aynıdır (build_yk_*.py başlıklarına bkz.); 28.09.2026 kontrolü.
Konu havuzundaki sorular burada tekrar edilmez; aynı hüküm farklı görevle ölçülür.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket

SURUM = ("3568 s. Kanun (2025), Etik İlkeler, Çalışma Usul (2026), Haksız Rekabet (2025), Ücret, Disiplin (2026), "
         "Odalar ve TÜRMOB (2026), Staj ve Sınav (2025), SMGE (2023/2026) yönetmelikleri; 28.09.2026 kontrolü")

def paket(dosya, seed):
    return Paket(dosya, lesson="meslek_hukuku", topic="mesleki_etik", konu_adi="Meslek Hukuku",
                 seed=seed, surum=SURUM, havuz="bolum")

K = "3568 sayılı Serbest Muhasebeci Mali Müşavirlik ve Yeminli Mali Müşavirlik Kanunu’na göre"
E = "Serbest Muhasebeci Mali Müşavirler ve Yeminli Mali Müşavirlerin Mesleki Faaliyetlerinde Uyacakları Etik İlkeler Hakkında Yönetmelik’e ekli Etik İlkeler’e göre"
CU = "Serbest Muhasebeci Mali Müşavir ve Yeminli Mali Müşavirlerin Çalışma Usul ve Esasları Hakkında Yönetmelik’e göre"
HR = "Serbest Muhasebeci Mali Müşavirlik ve Yeminli Mali Müşavirlik Mesleklerine İlişkin Haksız Rekabet ve Reklam Yasağı Yönetmeliği’ne göre"
UY = "Serbest Muhasebeci, Serbest Muhasebeci Mali Müşavir ve Yeminli Mali Müşavir Ücretlerinin Esasları Hakkında Yönetmelik’e göre"
DY = "Serbest Muhasebeci Mali Müşavirlik ve Yeminli Mali Müşavirlik Kanunu Disiplin Yönetmeliği’ne göre"
OY = "Serbest Muhasebeci Mali Müşavirler Odaları Yönetmeliği’ne göre"
TY = "Türkiye Serbest Muhasebeci Mali Müşavirler ve Yeminli Mali Müşavirler Odaları Birliği Yönetmeliği’ne göre"
SY = "Serbest Muhasebeci Mali Müşavirlik Staj Yönetmeliği’ne göre"
NY = "Yeminli Mali Müşavirlik ve Serbest Muhasebeci Mali Müşavirlik Sınav Yönetmeliği’ne göre"
GY = "Türkiye Serbest Muhasebeci Mali Müşavirler ve Yeminli Mali Müşavirler Odaları Birliği Sürekli Mesleki Geliştirme Eğitimi Yönetmeliği’ne göre"
KY = "Serbest Muhasebeci ve Serbest Muhasebeci Mali Müşavirlerin Kaşe Kullanma Usul ve Esasları Hakkında Yönetmelik’e göre"

# =============================================================================== TEST 1
T1 = paket("questions_meslek_hukuku_2026.json", 2026092811)

T1.q("Etik İlkeler İkinci Kısım m. 27-30",
     f"Aşağıdakilerden hangisi {E.replace('’e göre', '’de')} bağımsız çalışan meslek mensubu için iş çevresinde sözleşmeye özgü olarak alınabilecek önlemlerden biri değildir?",
     "Sürekli mesleki gelişim gereksinimlerinin uygulanması",
     ["Başka bir meslek mensubunun yapılan işi gözden geçirmesi",
      "Bağımsız bir üçüncü gruba danışılması",
      "Hizmetin bir kısmının başka bir firmaca yeniden yapılması",
      "Üst düzey güvence sözleşmesi ekibinin rotasyona tabi tutulması"],
     "İkinci Kısım m. 30 sözleşmeye özgü önlemleri sayar: başka meslek mensubunun gözden geçirmesi, bağımsız üçüncü "
     "gruba danışma, işin bir kısmının başka firmaca yapılması ve ekip rotasyonu bunlardandır. Sürekli mesleki gelişim "
     "gereksinimi Birinci Kısım m. 4/a'da mevzuatla oluşturulan önlemlerdendir.", topic="mesleki_etik", zorluk="hard")

T1.q("Etik İlkeler Birinci Kısım m. 14",
     f"{E}, aşağıdakilerden hangisi meslek mensubunun sahip olduğu gizli bilgileri açıklamasının gerekli veya uygun olabileceği durumlardan biri değildir?",
     "Müşterinin rakip firmasının yazılı talebi",
     ["Kanun veya müşteri izniyle yapılan açıklama",
      "Yasal süreçte belge veya kanıt sağlamak amacıyla açıklama",
      "Kanuna aykırı bir durumu kamu otoritesine açıklama",
      "Meslek odasının yürüttüğü soruşturmaya veri sağlama"],
     "Birinci Kısım m. 14 açıklamanın gerekli veya uygun olabileceği hâlleri kanun veya izinle açıklama, kanun gereği "
     "açıklama ve mesleki görev ya da hak kapsamında açıklama olarak sayar. Rakip firmanın talebi bunlardan değildir.",
     topic="mesleki_etik")

T1.q("Etik İlkeler Üçüncü Kısım m. 63-67",
     f"{E}, bağımlı çalışan meslek mensubu için aşağıdaki durumlardan hangisi yıldırma tehdidi yaratabilecek örneklerdendir?",
     "Karar verme sürecini etkilemeye yönelik baskın kişilikli bireyler",
     ["Finansal çıkar, krediler ve garantiler",
      "Şirket varlıklarının uygunsuz biçimde kişisel amaçla kullanımı",
      "Kararları veren meslek mensubunun aynı verileri incelemesi",
      "Mesleki kararları etkileyen taraflarla uzun süreli ilişki"],
     "Üçüncü Kısım m. 67'ye göre baskın kişilikli bireylerin karar sürecini etkilemesi yıldırma tehdidi örneğidir. "
     "Finansal çıkar ve varlıkların kişisel kullanımı kişisel çıkar (m. 63), kendi kararını incelemek yeniden "
     "değerlendirme (m. 64), uzun süreli ilişki yakınlık (m. 66) tehdididir.", topic="mesleki_etik", zorluk="hard")

T1.q("Çalışma Usul ve Esasları Yön. m. 23",
     "(A) Ltd. Şti.'nin defter tutma teklifi, birbirinden bağımsız iki meslek mensubu tarafından gerekçe gösterilmeden "
     f"reddedilmiştir. {CU}, bu durumda izlenecek yol aşağıdakilerden hangisidir?",
     "İş sahibi odaya başvurur ve oda kendisine bir meslek mensubu belirler.",
     ["İş sahibi Birliğe başvurur ve Birlik reddeden meslek mensuplarına uyarma cezası verir.",
      "Reddeden meslek mensupları gerekçelerini yazılı olarak vergi dairesine bildirir.",
      "İş sahibi, oda kararı olmadan üçüncü bir meslek mensubuna başvuramaz.",
      "Reddeden son meslek mensubu, oda kararıyla işi kabul etmekle yükümlü olur."],
     "Çalışma Usul ve Esasları Yönetmeliği m. 23'e göre meslek mensupları teklifi gerekçe göstermeden reddedebilir; iki "
     "meslek mensubunca reddedilen iş sahibi ilgili odaya başvurur ve oda kendisine meslek mensubu belirler.",
     topic="calisma_usulleri")

T1.sayisal("Çalışma Usul ve Esasları Yön. m. 14",
     f"{CU}, büro edinen meslek mensuplarının aldıkları Büro Tescil Belgeleri kaç yılda bir vize ettirilir?",
     "2", ["1", "3", "4", "5"],
     "Çalışma Usul ve Esasları Yönetmeliği m. 14'e göre büro edinen meslek mensupları odaya kayıttan itibaren üç ay "
     "içinde Büro Tescil Belgesi alır ve bu belge iki yılda bir vize ettirilir.", topic="calisma_usulleri")

T1.q("Çalışma Usul ve Esasları Yön. m. 43 ve 47 (14.01.2026 değişikliği)",
     f"{CU} Yasak Haller çerçevesinde, aşağıdakilerden hangisi meslek mensuplarının ticari faaliyette bulunamama yasağı kapsamında değildir?",
     "Limited şirkette ortak olmak",
     ["Ticari mümessillik yapmak", "Kollektif şirkette ortak olmak",
      "Komandit şirkette komandite ortak olmak", "Limited şirkette müdür olmak"],
     "Çalışma Usul ve Esasları Yönetmeliği m. 47'ye göre limited ve anonim şirketlerde ortak olmak meslekle bağdaşan "
     "işlerdendir. Ticari mümessillik, kollektif şirkette ortaklık, komandite ortaklık ve 2026 değişikliğiyle limited "
     "şirkette müdürlük m. 43'e göre yasaktır.", topic="calisma_usulleri")

T1.q("Haksız Rekabet ve Reklam Yasağı Yön. m. 7 ve 8",
     f"{HR}, aşağıdakilerden hangisi “reklam yoluyla haksız rekabet” örneği olarak sayılan hallerden biri değildir?",
     "Başka meslek mensubuna ücret borcu olan iş sahibine hizmet vermek",
     ["Meslek mensuplarının dürüstlüğü hakkında yanlış ve asılsız beyanda bulunmak",
      "Meslek mensuplarının hizmetlerini yanıltıcı açıklamalarla kötülemek",
      "Sahip olmadığı meslek unvanını kullanmak",
      "Mesleki ve akademik unvan dışında sahip olunan başka unvanları kullanmak"],
     "Ücret borcunu ödememiş iş sahibine hizmet vermek Yönetmelik m. 7/c'de ücret ve mali uygulamalarla haksız rekabet "
     "hâlidir. Diğer seçenekler m. 8'de reklam yoluyla haksız rekabet örnekleridir.", topic="calisma_usulleri")

T1.sayisal("Ücret Esasları Yön. m. 14",
     f"{UY}, süreli ücret sözleşmelerinin en az kaç yıllık olması şarttır?",
     "1", ["2", "3", "4", "5"],
     "Ücret Esasları Yönetmeliği m. 14'e göre ücret sözleşmeleri münferit ya da süreli yapılabilir; süreli sözleşmelerin en "
     "az bir yıllık olması şarttır.", topic="calisma_usulleri")

T1.oncul("3568 s. Kanun m. 4 ve 5/A",
     "Serbest muhasebeci mali müşavir olmak isteyen (B) için aşağıdaki şartlar değerlendirilmektedir:",
     ["T.C. vatandaşı olmak",
      "Kanunda sayılan dallarda en az lisans seviyesinde mezun olmak",
      "En az üç yıl staj yapmış olmak",
      "Kamu haklarından mahrum bulunmamak"],
     f"{K}, yukarıdakilerden hangileri serbest muhasebeci mali müşavir olabilmenin özel şartlarındandır?",
     "II ve III",
     ["Yalnız II", "I ve IV", "II ve III", "III ve IV", "I, II ve III"],
     "Kanun m. 5/A'ya göre lisans mezuniyeti ve en az üç yıl staj özel şartlardandır; T.C. vatandaşlığı ve kamu haklarından "
     "mahrum olmamak m. 4'teki genel şartlardır.", topic="meslek_ve_unvanlar")

T1.q("3568 s. Kanun m. 2/B",
     f"Aşağıdakilerden hangisi {K.replace('’na göre', '’na göre,')} yeminli mali müşavirlik mesleğinin konusu arasında yer almaz?",
     "Muhasebe defterlerini tutmak",
     ["Mali tablo ve beyannameleri tasdik etmek", "Muhasebe sistemlerini kurmak ve geliştirmek",
      "Belgelere dayanarak inceleme ve denetim yapmak", "Mali tablolarla ilgili yazılı görüş vermek"],
     "Kanun m. 2/B'ye göre YMM'ler m. 2/A'nın (b) ve (c) bentlerindeki işlerle tasdik işlerini yapar; muhasebe defteri "
     "tutamaz, muhasebe bürosu açamaz ve bu bürolara ortak olamaz.", topic="meslek_ve_unvanlar", zorluk="easy")

T1.q("3568 s. Kanun m. 45/2",
     "YMM (C)'ye, boşandığı eşinin ağabeyinin ortağı olduğu bir şirketin kurumlar vergisi beyannamesini tasdik etmesi "
     f"teklif edilmiştir. {K}, (C)'nin durumu aşağıdakilerden hangisidir?",
     "Bu şirketin işine bakamaz; boşanma bu yasağı kaldırmaz.",
     ["Boşanma nedeniyle sıhri hısımlık sona erdiğinden tasdik yapabilir.",
      "Ortaklık payı yüzde onun altındaysa tasdik yapabilir.",
      "Oda yönetim kurulundan izin alırsa tasdik yapabilir.",
      "Tasdik yapabilir; akrabalık ilişkisini raporda açıklaması yeterlidir."],
     "Kanun m. 45/2'ye göre YMM'ler eşi (boşanmış dahi olsa), usul ve füruu ile üçüncü dereceye kadar kan ve sıhri "
     "hısımlarının veya bunların ortak oldukları firmaların işlerine bakamaz. Eski eşin kardeşi ikinci derece sıhri "
     "hısımdır ve boşanma bu yasağı kaldırmaz.", topic="meslek_ve_unvanlar", zorluk="hard")

T1.sayisal("3568 s. Kanun m. 25; Odalar Yön. m. 19",
     f"{OY}, üye sayısı 50'ye kadar olan odalarda Oda Disiplin Kurulu kaç asıl üyeden oluşur?",
     "3", ["5", "7", "9", "11"],
     "Kanun m. 25 ve Odalar Yönetmeliği m. 19'a göre oda disiplin kurulu üye sayısı 50'ye kadar olan odalarda üç, "
     "50'den fazla olan odalarda beş üyedir; üç üyeli kurullarda bir, beş üyeli kurullarda üç yedek seçilir.",
     topic="oda_ve_turmob")

T1.q("3568 s. Kanun m. 34; TÜRMOB Yön. m. 13",
     f"{TY}, Birlik Genel Kurulu olağan olarak ne zaman toplanır?",
     "Üç yılda bir eylül ayında",
     ["Üç yılda bir mayıs ayında", "İki yılda bir eylül ayında",
      "Her yıl ekim ayında", "Dört yılda bir haziran ayında"],
     "Kanun m. 34 ve TÜRMOB Yönetmeliği m. 13'e göre Birlik Genel Kurulu üç yılda bir eylül ayında Birlik Yönetim Kurulu "
     "Başkanının daveti üzerine toplanır; oda genel kurulları ise üç yılda bir mayıs ayında toplanır.",
     topic="oda_ve_turmob", zorluk="easy")

T1.q("3568 s. Kanun m. 16 ve 30",
     f"{K}, odaların ve Birliğin gelirlerine ilişkin aşağıdaki eşleştirmelerden hangisi yanlıştır?",
     "Ruhsatname ücretleri – Odanın geliri",
     ["Odaya giriş ücreti – Odanın geliri",
      "Yıllık üye aidatları – Odanın geliri",
      "Odalardan alınacak paylar – Birliğin geliri",
      "Birliğe ait mal varlığından sağlanan gelirler – Birliğin geliri"],
     "Kanun m. 30'a göre ruhsatname ücretleri Birliğin gelirleridir. Giriş ücreti ve aidatlar m. 16'ya göre odanın, "
     "odalardan alınan paylar ve mal varlığı gelirleri m. 30'a göre Birliğin gelirleridir.", topic="oda_ve_turmob")

T1.q("Disiplin Yönetmeliği m. 5-9",
     f"{DY}, aşağıdaki eylemlerden hangisi uyarma cezasını gerektirir?",
     "Mevzuata aykırı tabela kullanılması",
     ["Reklam yasağına uyulmaması", "Ticari faaliyet yasağına uyulmaması",
      "Meslek ruhsatnamesinin başkasına kiraya verilmesi", "Sahip olunmayan unvanların kullanılması"],
     "Disiplin Yönetmeliği m. 5/e'ye göre mevzuata aykırı tabela kullanılması uyarma cezası gerektirir. Reklam yasağı ve "
     "sahip olunmayan unvan kınama (m. 6), ticari faaliyet yasağı alıkoyma (m. 7), ruhsat kiralama meslekten çıkarma "
     "(m. 9) cezası gerektirir.", topic="disiplin")

T1.q("Disiplin Yönetmeliği m. 14 ve 15",
     f"{DY}, disiplin soruşturmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
     "Meslek mensubunun ölümü hâlinde açılmış soruşturmaya mirasçıları hakkında devam edilir.",
     ["Soruşturma yetkisi, meslek mensubunun kayıtlı olduğu odaya aittir.",
      "Eylemin işlenmesinden itibaren beş yıl geçmişse soruşturma yapılamaz.",
      "Hükümlülükle sonuçlanan ceza davasının odaya ulaşması soruşturma sebebidir.",
      "Disiplin soruşturma ve kovuşturmasında gizlilik esastır."],
     "Disiplin Yönetmeliği m. 14'e göre meslek mensubunun ölümü veya akıl sağlığını sürekli kaybetmesi hâlinde soruşturma "
     "açılmaz, açılmış olan soruşturma veya kovuşturma düşer; mirasçılar hakkında devam edilmez.", topic="disiplin")

T1.q("Disiplin Yönetmeliği m. 29; 3568 s. Kanun m. 38",
     f"{DY}, Birlik Disiplin Kurulunun itirazların reddine ilişkin kararları aşağıdakilerden hangisiyle kesinleşir?",
     "Hazine ve Maliye Bakanlığının onayıyla",
     ["Birlik Genel Kurulunun onayıyla", "Birlik Yönetim Kurulunun onayıyla",
      "Oda disiplin kurulunun onayıyla", "Danıştayın onayıyla"],
     "Disiplin Yönetmeliği m. 29 ve Kanun m. 38'e göre Birlik Disiplin Kurulunun itirazların reddine ait kararları Hazine "
     "ve Maliye Bakanlığının onayıyla kesinleşir; ilgililer bu kararlara karşı idari yargıya başvurabilir.",
     topic="disiplin")

T1.sayisal("Sınav Yön. m. 8",
     f"{NY}, Birlik yeminli mali müşavirlik sınavlarını yılda kaç kez yapar?",
     "3", ["1", "2", "4", "6"],
     "Sınav Yönetmeliği m. 8'e göre Birlik YMM sınavlarını yılda üç kez, SMMM sınavlarını staj dönemlerini gözeterek yılda "
     "üç kez yapar; sınav günleri ve yerleri en az bir ay önce Resmî Gazete'de ilan edilir.", topic="ruhsat_ve_staj")

T1.q("Staj Yön. m. 9/a; 3568 s. Kanun m. 6",
     f"{SY}, Temel Eğitim ve Staj Merkezinin (TESMER) kurs ve seminerlerinde geçen sürelere ilişkin aşağıdakilerden hangisi doğrudur?",
     "Altı ayı aşmayan süreler staj süresinden sayılır.",
     ["Tamamı staj süresinden sayılır ve üst sınır yoktur.",
      "Bir yılı aşmayan süreler staj süresinden sayılır.",
      "Staj süresinden sayılmaz; stajdan önce tamamlanır.",
      "Üç ayı aşmayan süreler staj süresinden sayılır."],
     "Staj Yönetmeliği m. 9/a ve Kanun m. 6'ya göre TESMER'in kurs ve seminerlerinde geçen ve altı ayı aşmayan süreler "
     "staj süresinden sayılır; esasları TESMER Yönetim Kurulu belirler.", topic="ruhsat_ve_staj")

T1.oncul("5549 s. Kanun m. 4, 8 ve 10; Çalışma Usul Yön. m. 7",
     "Bir meslek mensubunun mesleki sorumluluklarına ilişkin aşağıdaki ifadeler verilmiştir:",
     ["Sır saklama yükümlülüğü mesleki faaliyete son verilse bile devam eder.",
      "Şüpheli işlem bildiriminde bulunulduğu müşteriye açıklanabilir.",
      "Kimlik tespitine ilişkin belgeler son işlemden itibaren sekiz yıl saklanır.",
      "Tanıklık sırrın ifşası sayılır."],
     "Çalışma Usul ve Esasları Yönetmeliği ve 5549 sayılı Kanun’a göre yukarıdaki ifadelerden hangileri doğrudur?",
     "I ve III",
     ["Yalnız I", "I ve III", "II ve III", "II ve IV", "I, III ve IV"],
     "Çalışma Usul ve Esasları Yönetmeliği m. 7'ye göre sır saklama faaliyete son verilse de sürer ve tanıklık sırrın "
     "ifşası sayılmaz; 5549 sayılı Kanun m. 8'e göre kimlik belgeleri sekiz yıl saklanır, m. 4'e göre bildirim yapıldığı "
     "müşteriye açıklanamaz.", topic="mesleki_sorumluluk", zorluk="hard")

# =============================================================================== TEST 2
T2 = paket("questions_meslek_hukuku_test2_2026.json", 2026092812)

T2.q("Etik İlkeler Birinci Kısım m. 1",
     f"{E}, “meslek mensubunun mevcut yasa ve yönetmeliklere uyması ve mesleğin itibarını zedeleyecek her türlü davranıştan kaçınması” hangi temel etik ilkesinin tanımıdır?",
     "Mesleki Davranış",
     ["Dürüstlük", "Tarafsızlık", "Mesleki Yeterlilik ve Özen", "Gizlilik"],
     "Birinci Kısım m. 1/d'ye göre mesleki davranış, meslek mensubunun mevcut yasa ve yönetmeliklere uymasını ve mesleğin "
     "itibarını zedeleyecek her türlü davranıştan kaçınmasını ifade eder.", topic="mesleki_etik", zorluk="easy")

T2.q("Etik İlkeler İkinci Kısım m. 21-25",
     f"Aşağıdakilerden hangisi {E.replace('’e göre', '’de')} bağımsız çalışan meslek mensubu için yakınlık tehdidi yaratabilecek durumlara verilen örneklerden biri değildir?",
     "Müşteri tarafından istihdam edilme olasılığı",
     ["Ekip üyesinin müşterinin yöneticisiyle birinci derece ailevi ilişkisi",
      "Firmanın eski ortağının müşterinin yöneticisi olması",
      "Değeri önemsiz olmayan hediye veya ayrıcalıklı hizmet alınması",
      "Üst düzey personel ile müşteri arasında uzun süreli arkadaşlık"],
     "Müşteri tarafından istihdam edilme olasılığı İkinci Kısım m. 21/d'de kişisel çıkar tehdidi örneğidir. Diğer "
     "seçenekler m. 24'te yakınlık tehdidi örnekleri olarak sayılmıştır.", topic="mesleki_etik")

T2.q("Etik İlkeler İkinci Kısım m. 33 ve 35",
     f"{E}, müşteri ve sözleşme kabulüne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
     "Tehditler giderilemese de tatmin olunmadan sözleşme kabul edilebilir.",
     ["Müşterinin para aklama gibi yasa dışı faaliyetleri temel ilkeleri tehdit eden konulardandır.",
      "Tehditler kabul edilebilir düzeye indirilemezse müşteriyi kabul etmekten kaçınılmalıdır.",
      "Yerine geçilecek meslek mensubuyla doğrudan iletişim kurulması bir önlemdir.",
      "Mevcut meslek mensubundan bilinmesi gereken gerçeklerle ilgili bilgi istenebilir."],
     "İkinci Kısım m. 35/5'e göre önlemlere rağmen tehditler giderilemiyorsa meslek mensubu, mevcut verilerden tatmin "
     "olmadıkça sözleşmenin kabulünden kaçınmalıdır. Diğer ifadeler m. 33 ve 35'te yer alır.", topic="mesleki_etik",
     zorluk="hard")

T2.q("Çalışma Usul ve Esasları Yön. m. 15",
     f"{CU}, meslek mensuplarının tabelalarında aşağıdakilerden hangisine yer verilemez?",
     "Yabancı dilde yazılmış tanıtım ifadeleri",
     ["Oda ve Birlik amblemi", "Meslek unvanı ile ad ve soyadı",
      "Varsa akademik unvan", "Büronun internet ve elektronik posta adresi"],
     "Çalışma Usul ve Esasları Yönetmeliği m. 15'e göre tabelada oda ve Birlik amblemi, meslek unvanı, ad-soyad, ortaklık "
     "veya şirket unvanı, akademik unvan, adres, telefon, internet ve e-posta adresi yer alabilir; yabancı dillerde "
     "yazılmış ifadelere yer verilemez.", topic="calisma_usulleri", zorluk="easy")

T2.q("Çalışma Usul ve Esasları Yön. m. 42",
     f"Aşağıdakilerden hangisi {CU.replace('’e göre', '’e göre,')} meslekle ve meslek onuru ile bağdaşmayan hallerden biri değildir?",
     "Devamlılık arz etmeyen mesleki gazete yazısı yazmak",
     ["Yanında çalıştırdığı kişilere karşı uygunsuz davranmak",
      "Aşırı içki ve kumar düşkünlüğü ile tanınmak",
      "Kanunlara göre yapılması yasak olan işlerden birini yapmak",
      "Mesleki etik ve mesleki bağımsızlık kurallarını ihlal etmek"],
     "Çalışma Usul ve Esasları Yönetmeliği m. 42 meslekle bağdaşmayan hâlleri sayar. Devamlılık arz etmeyen mesleki gazete "
     "yazısı m. 45 ve 47'ye göre reklam sayılmaz ve meslekle bağdaşan işlerdendir.", topic="calisma_usulleri")

T2.sayisal("Çalışma Usul ve Esasları Yön. m. 14 (24.02.2025 değişikliği)",
     f"{CU}, işyerini veya ikamet adresini değiştiren meslek mensupları yeni adreslerini kaç gün içinde bağlı oldukları odaya bildirmek zorundadır?",
     "30", ["7", "10", "15", "60"],
     "2025 değişikliğiyle Çalışma Usul ve Esasları Yönetmeliği m. 14'e göre işyerini veya ikamet adresini değiştiren meslek "
     "mensupları ile ortaklık büroları ve şirketler otuz gün içinde yeni adreslerini odaya bildirir.",
     topic="calisma_usulleri")

T2.q("Haksız Rekabet ve Reklam Yasağı Yön. m. 13",
     f"{HR}, aşağıdakilerden hangisi reklam sayılmaz?",
     "Mesleki alan dışında aldığı bir ödülün kamuya duyurulması",
     ["Büro açılışının yerel gazetede ilan yoluyla duyurulması",
      "Düzenlenen seminerin basın yoluyla üçüncü kişilere duyurulması",
      "Tanıtım broşüründe mevcut müşterilerin unvanlarına yer verilmesi",
      "Kitapta çalışılan büronun faaliyetlerinin tanıtılması"],
     "Haksız Rekabet ve Reklam Yasağı Yönetmeliği m. 13/5'e göre meslek alanı dışındaki bir faaliyetin tanıtılması veya "
     "alınan bir ödülün duyurulması reklam sayılmaz. Büro açılışının basınla duyurulması (m. 21), seminerin basınla "
     "duyurulması (m. 13/2), müşteri isimleri (m. 18) ve kitapta büro tanıtımı (m. 19) yasaktır.",
     topic="calisma_usulleri", zorluk="hard")

T2.q("Ücret Esasları Yön. m. 11 ve 13",
     f"{UY}, aşağıdaki ifadelerden hangisi yanlıştır?",
     "Dostluk ilişkisi olan müşterilere ücretsiz işlem yapılabilir.",
     ["Ücretin tespitinde tarifeye uyulması zorunludur.",
      "Tarifedeki asgari miktar altında ücretle çalışmak disiplin cezası gerektirir.",
      "Ücret sözleşmesine ortaklık payı verileceğine dair hüküm konulamaz.",
      "Yabancı firmalarla sözleşmeler yabancı dilde ve yabancı paralı yapılabilir."],
     "Ücret Esasları Yönetmeliği m. 11'e göre meslek mensupları ücretsiz işlem yapamaz; tarifeye uyulması zorunludur ve "
     "asgari miktarın altında çalışmak disiplin cezası gerektirir. Ortaklık payı yasağı ve dövizli sözleşme m. 13'tedir.",
     topic="calisma_usulleri")

T2.q("3568 s. Kanun m. 9 ve 11",
     f"{K}, yeminli mali müşavirliğe ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
     "YMM'ler göreve başladıktan sonra bir yıl içinde yemin eder.",
     ["YMM olabilmek için en az on yıl SMMM'lik yapmış olmak gerekir.",
      "YMM olabilmek için YMM sınavını vermiş olmak gerekir.",
      "YMM olabilmek için YMM ruhsatını almış olmak gerekir.",
      "YMM'ler yemini Asliye Ticaret Mahkemesinde eder."],
     "Kanun m. 11'e göre YMM mesleğine kabul edilenler görevlerine fiilen başlamadan önce Asliye Ticaret Mahkemesinde yemin "
     "eder; m. 9'a göre on yıl SMMM'lik, YMM sınavı ve ruhsat özel şartlardır.", topic="meslek_ve_unvanlar")

T2.q("3568 s. Kanun m. 3 ve 49",
     f"{K}, unvanların haksız kullanılmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
     "Aykırılığı öğrenen oda, durumu önce Birlik Disiplin Kuruluna bildirir.",
     ["Yetkisi olmayanların meslek unvanlarını kullanması yasaktır.",
      "Unvanlara karışacak veya benzer ibarelerin kullanılması da yasaktır.",
      "Cumhuriyet Savcılığınca tahkikatın sonucu odaya ve ilgililere bildirilir.",
      "Aykırılık altı aydan bir yıla kadar hapis ve adli para cezası gerektirir."],
     "Kanun m. 3'e göre odalar unvanların haksız kullanılmasını öğrendiklerinde Cumhuriyet Savcılığına bildirmek "
     "mecburiyetindedir; tahkikat sonucu odaya ve ilgililere bildirilir. M. 49/1'e göre aykırılık altı aydan bir yıla "
     "kadar hapis ve adli para cezası gerektirir.", topic="meslek_ve_unvanlar")

T2.q("3568 s. Kanun m. 45/3",
     f"Aşağıdakilerden hangisi {K.replace('’na göre', '’na göre,')} meslekle bağdaşmayan işler sayılmayan görevlerden biri değildir?",
     "Bir ticaret şirketinin tacir sıfatıyla temsilciliği",
     ["Hayri kuruluşların yönetim kurulu üyeliği",
      "İlmi kuruluşların denetçiliği",
      "Bilirkişilik",
      "Tasfiye memurluğu"],
     "Kanun m. 45/3'e göre hayri ve ilmi kuruluşların yönetim kurulu başkanlığı, üyeliği ve denetçiliği ile bilirkişilik ve "
     "tasfiye memurluğu meslekle bağdaşmayan iş sayılmaz. Tacir sıfatıyla temsilcilik ticari faaliyettir.",
     topic="meslek_ve_unvanlar", zorluk="hard")

T2.q("3568 s. Kanun m. 17 ve 31",
     f"{K}, aşağıdakilerden hangisi hem odaların hem de Birliğin organlarından biri değildir?",
     "Danışma Kurulu",
     ["Genel Kurul", "Yönetim Kurulu", "Disiplin Kurulu", "Denetleme Kurulu"],
     "Kanun m. 17 ve 31'e göre odaların ve Birliğin organları genel kurul, yönetim kurulu, disiplin kurulu ve denetleme "
     "kuruludur; danışma kurulu organ olarak sayılmamıştır.", topic="oda_ve_turmob", zorluk="easy")

T2.sayisal("3568 s. Kanun m. 21; Odalar Yön. m. 10",
     f"{OY}, üye sayısı binin altında olan odalarda Oda Yönetim Kurulu kaç asıl üyeden oluşur?",
     "5", ["3", "7", "9", "11"],
     "Oda yönetim kurulunun üye sayısı odanın büyüklüğüne göre kademelidir (Kanun m. 21, Odalar Yön. m. 10): binin "
     "altında üye bulunan odalarda beş, bin ile beş bin arasında yedi, beş bini aşan odalarda dokuz asıl üye; her "
     "kademede asıl üye sayısı kadar yedek seçilir. Üyeler üç yıl için genel kurulca seçilir.",
     topic="oda_ve_turmob")

T2.q("3568 s. Kanun m. 35; TÜRMOB Yön. m. 21-22",
     f"{TY}, Birlik Yönetim Kuruluna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
     "Yönetim kurulu başkanı, SMMM unvanlı üyeler arasından seçilir.",
     ["Yönetim kurulu dokuz asıl ve dokuz yedek üyeden oluşur.",
      "Yönetim kurulu üyelerinden beşinin YMM olması zorunludur.",
      "Başkan, en az beş yıl YMM'lik yapmış olanlar arasından seçilir.",
      "Başkanın bulunmadığı hâllerde başkan yardımcısı kurula başkanlık eder."],
     "Kanun m. 35 ve TÜRMOB Yönetmeliği m. 21-22'ye göre Birlik Yönetim Kurulu Başkanı en az beş yıl süreyle yeminli mali "
     "müşavirlik yapmış olanlar arasından seçilir.", topic="oda_ve_turmob")

T2.q("Disiplin Yönetmeliği m. 4/c; 3568 s. Kanun m. 48",
     f"{DY} “geçici olarak mesleki faaliyetten alıkoyma” cezasına göre, mesleki sıfatı saklı kalmak koşuluyla mesleki faaliyetten alıkonulma süresi aşağıdakilerin hangisinde doğru olarak verilmiştir?",
     "Altı aydan az, bir yıldan fazla olamaz.",
     ["Bir aydan az, üç aydan fazla olamaz.", "Bir aydan az, altı aydan fazla olamaz.",
      "Üç aydan az, altı aydan fazla olamaz.", "Bir yıldan az, üç yıldan fazla olamaz."],
     "Disiplin Yönetmeliği m. 4/c ve Kanun m. 48'e göre geçici olarak mesleki faaliyetten alıkoyma, mesleki sıfatı saklı "
     "kalmak koşuluyla altı aydan az, bir yıldan fazla olmamak üzere uygulanır.", topic="disiplin")

T2.q("Disiplin Yönetmeliği m. 6",
     f"{DY}, aşağıdakilerden hangisi kınama cezasını gerektiren haller arasında sayılmamıştır?",
     "Kasten vergi ziyaına sebebiyet verildiğinin mahkeme kararıyla kesinleşmesi",
     ["Asgari ücret tarifesinin altında iş kabul edilmesi",
      "Büro tescil belgesinin alınmaması",
      "Diğer meslek mensubu hakkında asılsız ihbarda bulunulması",
      "Yazılı hizmet sözleşmesi yapılmadan iş kabul edilmesi"],
     "Kasten vergi ziyaına sebebiyet verildiğinin mahkeme kararıyla kesinleşmesi Disiplin Yönetmeliği m. 9/c'ye göre "
     "meslekten çıkarma cezası gerektirir. Diğer seçenekler m. 6'da kınama hâlleridir.", topic="disiplin")

T2.sayisal("Disiplin Yönetmeliği m. 28",
     f"{DY}, oda disiplin kurulu kararlarına karşı ilgililer bildirim tarihinden itibaren kaç gün içinde Birlik Disiplin Kuruluna itiraz edebilir?",
     "30", ["7", "10", "15", "45"],
     "Disiplin Yönetmeliği m. 28'e göre oda disiplin kurulu kararlarına karşı ilgililer bildirim tarihinden itibaren 30 gün "
     "içinde ilgili oda aracılığıyla veya doğrudan Birlik Disiplin Kuruluna itiraz edebilir.", topic="disiplin")

T2.q("Staj Yön. m. 7 ve 8",
     f"{SY}, aşağıdaki ifadelerden hangisi yanlıştır?",
     "Staja giriş sınavından en az 50 puan alanlar staja başlayabilir.",
     ["Serbest muhasebeci mali müşavir adayları için staj süresi üç yıldır.",
      "Staja başlamak için Birlikçe belirlenen staj giderlerinin yatırılması gerekir.",
      "Staj, mücbir sebepler ve yurt dışı eğitim ile çalışma dışında kesintisiz yapılır.",
      "Staja başlamak için Kanundaki genel şartlar ile öğrenim şartı aranır."],
     "Staj Yönetmeliği m. 7'ye göre staja başlamak için staja giriş sınavından en az 60 puan almak gerekir; m. 8'e göre "
     "staj süresi üç yıldır ve kesintisiz yapılır.", topic="ruhsat_ve_staj")

T2.oncul("SMGE Yön. m. 13",
     "Bir meslek mensubunun üç yıllık dönemdeki diğer faaliyetleri aşağıda verilmiştir:",
     ["Birlik seminerine katılım",
      "SÜRGEM'e akredite kuruluşun konferansında konuşmacılık",
      "Stajyer mentorluğu",
      "Kişisel sosyal medya hesabında mesleki paylaşım"],
     f"{GY}, yukarıdaki faaliyetlerden hangileri sürekli mesleki geliştirme eğitimi kapsamında kredi sağlar?",
     "I, II ve III",
     ["Yalnız I", "I ve IV", "II ve III", "I, II ve III", "II, III ve IV"],
     "SMGE Yönetmeliği m. 13'e göre Birlik veya oda seminerine katılım 3, akredite kuruluşta konuşmacılık 3, stajyer "
     "mentorluğu her ay 1 kredi (yılda en fazla 7) sağlar. Kişisel sosyal medya paylaşımı kredi kaynağı değildir.",
     topic="ruhsat_ve_staj", zorluk="hard")

T2.q("VUK mük. m. 227; Çalışma Usul Yön. m. 21",
     "SMMM (D), müşterisinin defter kayıtlarına ve belgelerine uymayan bilgilerle katma değer vergisi beyannamesini "
     f"imzalamış ve vergi ziyaı doğmuştur. 213 sayılı Vergi Usul Kanunu’na göre, (D)'nin sorumluluğu aşağıdakilerden hangisidir?",
     "Vergi, ceza ve faizden mükellefle müteselsilen sorumludur.",
     ["Sorumluluğu mükellefe ait olup (D) hakkında disiplin hükümleri uygulanır.",
      "Vergi aslından değil, kesilecek cezanın yarısından sorumludur.",
      "Mükelleften tahsil edilemeyen kısımdan ikinci derecede sorumludur.",
      "Sorumluluğu beyanname ücretinin iadesiyle sınırlıdır."],
     "VUK mükerrer m. 227'ye göre beyannameyi imzalayan meslek mensupları, beyannamedeki bilgilerin defter kayıtlarına ve "
     "belgelere uygun olmamasından doğan vergi ziyaına bağlı vergi, ceza ve gecikme faizlerinden mükellefle birlikte "
     "müştereken ve müteselsilen sorumludur.", topic="mesleki_sorumluluk")

# =============================================================================== TEST 3
T3 = paket("questions_meslek_hukuku_test3_2026.json", 2026092813)

T3.q("Etik İlkeler Birinci Kısım m. 3",
     f"Aşağıdakilerden hangisi {E.replace('’e göre', '’de')} temel etik ilkelerine yönelik tehditlerin sınıflandırıldığı tehditlerden biri değildir?",
     "Bağımsızlık tehdidi",
     ["Kişisel çıkar tehdidi", "Yeniden değerlendirme tehdidi", "Taraf tutma tehdidi", "Yıldırma amaçlı tehdit"],
     "Birinci Kısım m. 3 tehditleri kişisel çıkar, yeniden değerlendirme, taraf tutma, yakınlık ve yıldırma amaçlı tehditler "
     "olarak sınıflandırır; bağımsızlık ayrı bir tehdit türü değildir.", topic="mesleki_etik", zorluk="easy")

T3.q("Etik İlkeler İkinci Kısım m. 40-43",
     f"{E}, ücretlere ve komisyonlara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
     "Müşteriyi başka meslek mensubuna gönderme karşılığında komisyon almak uygundur.",
     ["Diğer meslek mensubundan düşük ücret istemek kendi içinde etik dışı değildir.",
      "Ücret, Birlikçe belirlenip ilan edilen en az ücret düzeyinin altında olamaz.",
      "Şarta bağlı ücret tarafsızlık ilkesine yönelik kişisel çıkar tehdidi doğurabilir.",
      "Ücretin çok düşük olması mesleki yeterlilik ve özen ilkesini tehdit edebilir."],
     "İkinci Kısım m. 43'e göre müşteri gönderme bedeli veya komisyon alınması tarafsızlık ile yeterlilik ve özen ilkelerine "
     "kişisel çıkar tehdidi yaratır ve bu tür ücret ya da komisyonların alınması veya ödenmesi uygun değildir.",
     topic="mesleki_etik")

T3.q("Etik İlkeler İkinci Kısım m. 53",
     f"{E}, “fikren bağımsızlık” aşağıdakilerden hangisini ifade eder?",
     "Kararın dış etkilerden bağımsız verilmesini ve şüphecilikle davranılmasını",
     ["Bilgili üçüncü kişilerin firmanın tarafsızlığını onaylamasını",
      "Meslek mensubunun müşteriyle arasındaki finansal ilişkiyi kamuya açıklamasını",
      "Denetim ekibinin her yıl değiştirilerek raporun kamuya ilan edilmesini",
      "Meslek mensubunun ücretini müşteriden bağımsız olarak odanın belirlemesini"],
     "İkinci Kısım m. 53'e göre fikren bağımsızlık, mesleki kararın dış etkilerden bağımsız verilmesi ve meslek mensubunun "
     "dürüstlük, tarafsızlık ve mesleki şüphecilik içinde davranmasıdır; üçüncü kişilerce onay görünümde bağımsızlıktır.",
     topic="mesleki_etik", zorluk="hard")

T3.q("Çalışma Usul ve Esasları Yön. m. 24",
     f"{CU}, aşağıdaki çalışma konularından hangisinde sözleşme yapılması zorunlu tutulmamıştır?",
     "Tek bir konuda verilen sözlü danışmanlık",
     ["Defter tutmak", "Süreklilik arz eden müşavirlik hizmeti",
      "İnceleme, tahlil ve denetim yapmak", "YMM tasdik işlemleri"],
     "Çalışma Usul ve Esasları Yönetmeliği m. 24'e göre defter tutma, süreklilik arz eden müşavirlik, inceleme-tahlil-denetim "
     "ve YMM tasdik işlemlerinde sözleşme zorunludur; sürekliliği olmayan tek bir danışmanlık bu sayımda yer almaz.",
     topic="calisma_usulleri")

T3.q("Çalışma Usul ve Esasları Yön. m. 26",
     f"{CU}, meslek mensubunun sözleşmeyi feshinde haklı gerekçelerinden biri olarak açıkça sayılan aşağıdakilerden hangisidir?",
     "Tevdi edilen belgelerin güvenilir olmaması",
     ["Müşterinin başka ile taşınması", "Meslek mensubunun büro adresini değiştirmesi",
      "Müşterinin çalışan sayısının artması", "Ücret tarifesinin yeni yılda değişmesi"],
     "Çalışma Usul ve Esasları Yönetmeliği m. 26'ya göre ücretin ödenmemesi ve meslek mensubuna tevdi edilen belgelerin "
     "sağlıklı ve güvenilir olmaması fesihte meslek mensubunun haklı gerekçesidir.", topic="calisma_usulleri")

T3.q("Çalışma Usul ve Esasları Yön. m. 30",
     "Aynı unvana sahip üç SMMM, çalışmalarını tek bir ortaklık bürosunda birleştirmeyi planlamaktadır. "
     f"{CU}, ortaklık bürosu veya şirket kurarak mesleki faaliyette bulunmaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
     "Ortaklık büroları, oda yönetim kuruluna bildirerek şube açabilir.",
     ["Ortaklık bürosu aynı unvana sahip meslek mensupları arasında kurulabilir.",
      "Şirket veya ortaklık bürosu mesleki işlerde ortaklar tarafından temsil edilir.",
      "Ortaklık bürosu veya şirketin unvanında meslek unvanı açıkça kullanılır.",
      "Farklı odanın çalışanlar listesine kayıtlı meslek mensupları ortaklık bürosu kuramaz."],
     "Çalışma Usul ve Esasları Yönetmeliği m. 30/i'ye göre ortaklık büroları şube açamaz; aynı unvanda ortaklık, ortaklar "
     "tarafından temsil, unvan kullanımı ve farklı oda kaydı kuralı aynı maddededir.", topic="calisma_usulleri")

T3.sayisal("Çalışma Usul ve Esasları Yön. m. 34",
     f"{CU}, nakil talebinin başvurulan odaca reddi hâlinde meslek mensubu kararın tebliğinden itibaren kaç gün içinde Birliğe itiraz edebilir?",
     "15", ["7", "10", "30", "60"],
     "Çalışma Usul ve Esasları Yönetmeliği m. 34'e göre nakil talebinin reddine karşı meslek mensubu tebliğden itibaren on "
     "beş gün içinde Birliğe itiraz edebilir; Birlik itirazı on beş gün içinde karara bağlar ve karar nihaidir.",
     topic="calisma_usulleri")

T3.q("Haksız Rekabet ve Reklam Yasağı Yön. m. 17 ve 22",
     f"{HR}, aşağıdaki ifadelerden hangisi yanlıştır?",
     "Meslek mensupları telefon rehberinde ayırt edici sembol kullanabilir.",
     ["Telefon rehberinin meslekler kısmında alfabetik sırada bilgi yayımlatılabilir.",
      "Mesleki faaliyet için meslekiunvanı.tr uzantılı internet sitesi kurulabilir.",
      "İnternet sitesinde bağlı olunan oda ve sicil numaraları yer alır.",
      "İnternet kısa yollarıyla kullanıcıları iş sağlama amacıyla yönlendirmek yasaktır."],
     "Haksız Rekabet ve Reklam Yasağı Yönetmeliği m. 17'ye göre telefon rehberinde alfabetik sırada ve diğer meslek "
     "mensuplarından ayırt edici ifade, sembol veya işaret kullanmamak koşuluyla bilgi yayımlatılabilir.",
     topic="calisma_usulleri", zorluk="hard")

T3.q("3568 s. Kanun m. 12",
     "YMM (M), bir sanayi şirketinin kurumlar vergisi beyannamesini tasdik ederek raporunu düzenlemiştir. "
     f"{K}, yeminli mali müşavirlerin tasdikine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
     "YMM'ler tasdikin kapsamını raporda belirtmekle yükümlü değildir.",
     ["Tasdik edilmiş mali tablolar tasdikin kapsamı ölçüsünde incelenmiş belge kabul edilir.",
      "Tasdik doğru değilse YMM tasdikin kapsamıyla sınırlı olarak müteselsilen sorumludur.",
      "Tasdikten doğan mali ve disiplin sorumlulukları müstakil raporla tespit edilir.",
      "Kamu idaresinin teftiş ve inceleme yetkileri tasdike rağmen saklıdır."],
     "Kanun m. 12'ye göre YMM'ler tasdikin kapsamını düzenleyecekleri raporda açıkça belirtir. Diğer ifadeler aynı maddede "
     "yer alır.", topic="meslek_ve_unvanlar")

T3.sayisal("3568 s. Kanun m. 7",
     f"{K}, serbest muhasebeci mali müşavirlik sınav komisyonu kaç üyeden oluşur?",
     "7", ["3", "5", "9", "11"],
     "Kanun m. 7'ye göre SMMM sınav komisyonu 7 üyeden oluşur: 2 üye Bakanlığı temsil eder, 3 üye YÖK'ün 5 adayı, 2 üye "
     "Birliğin 4 adayı arasından Bakan tarafından seçilir.", topic="meslek_ve_unvanlar")

T3.q("Kaşe Kullanma Yön. m. 9-14",
     f"{KY}, aşağıdaki ifadelerden hangisi yanlıştır?",
     "Başka bir odaya nakilde kaşe değiştirilir ve yeni numara verilir.",
     ["Meslek mensupları istendiğinde kaşeyi oda veya Birliğe ibraz eder.",
      "Ruhsat iptalinde kaşe 15 gün içinde tutanakla odaya iade edilir.",
      "Unvan değişikliğinde eski kaşe iade edilerek yenisi alınır.",
      "Birliğin meslek kütüğünde kaydın yanına kaşe numarası da yazılır."],
     "Kaşe Yönetmeliği m. 14'e göre odalar arasında nakil kaşenin değiştirilmesini gerektirmez; ibraz (m. 9), 15 gün içinde "
     "iade (m. 9), unvan değişikliği (m. 10) ve meslek kütüğüne kayıt (m. 12) aynı yönetmelikte düzenlenmiştir.",
     topic="meslek_ve_unvanlar")

T3.q("3568 s. Kanun m. 19",
     "(N) Serbest Muhasebeci Mali Müşavirler Odasının olağan genel kurulunun gündemi hazırlanmaktadır. "
     f"{K}, aşağıdakilerden hangisi oda genel kurulunun görevleri arasında yer almaz?",
     "Mesleki ruhsatları vermek",
     ["Odaya yazılacak adayların giriş ücretlerini tespit etmek",
      "Bütçeyi ve kesin hesapları tasdik etmek",
      "Yönetim kurulunun çalışma raporunu incelemek ve kabul etmek",
      "Birlik temsilcilerini seçmek"],
     "Mesleki ruhsatları vermek Kanun m. 36/h'ye göre Birlik Yönetim Kurulunun görevidir. Diğer seçenekler m. 19'da oda "
     "genel kurulunun görevleri olarak sayılmıştır.", topic="oda_ve_turmob")

T3.q("3568 s. Kanun m. 38-39",
     f"{K}, Birlik Disiplin ve Denetleme Kurullarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
     "Birlik Denetleme Kurulu beş asıl ve beş yedek üyeden oluşur.",
     ["Birlik Disiplin Kurulu beş asıl ve beş yedek üyeden oluşur.",
      "Birlik Disiplin Kurulu asıl üyelerinin üçünün YMM olması mecburidir.",
      "Birlik Denetleme Kurulu üyelerinden en az birinin YMM olması zorunludur.",
      "Birlik Denetleme Kurulu üyeleri yönetim kurulu toplantılarında oy kullanamaz."],
     "Kanun m. 39'a göre Birlik Denetleme Kurulu üç asıl ve üç yedek üyeden oluşur; en az bir üye YMM olmalıdır ve üyeler "
     "yönetim kurulu toplantılarına katılabilir ama oy kullanamaz. M. 38'e göre Disiplin Kurulu beş asıl beş yedek üyedir.",
     topic="oda_ve_turmob")

T3.sayisal("3568 s. Kanun m. 15",
     f"{K}, ilçelerde oda kurulabilmesi için o ilçede kendi mesleği konusunda en az kaç meslek mensubu bulunması gerekir?",
     "250", ["50", "100", "150", "200"],
     "Kanun m. 15'e göre bölgesinde 250 meslek mensubu bulunan ilçelerde (büyükşehir belediyesi sınırları içindeki ilçeler "
     "hariç) oda kurulur; ayrıca o ilçedeki en az 100 meslek mensubunun yazılı başvurusu aranır.",
     topic="oda_ve_turmob", zorluk="hard")

T3.q("Disiplin Yönetmeliği m. 7",
     f"{DY}, aşağıdaki eylemlerden hangisi geçici olarak mesleki faaliyetten alıkoyma cezasını gerektirir?",
     "Ticari faaliyet yasağına uyulmaması",
     ["Mevzuata aykırı tabela kullanılması", "Adres değişikliğinin süresinde bildirilmemesi",
      "Reklam yasağına uyulmaması", "Büro tescil belgesinin süresinde vize ettirilmemesi"],
     "Disiplin Yönetmeliği m. 7/e'ye göre ticari faaliyet yasağına uyulmaması alıkoyma cezası gerektirir. Tabela ve adres "
     "uyarma (m. 5), reklam yasağı ve büro tescil vizesi kınama (m. 6) hâlleridir.", topic="disiplin")

T3.q("Disiplin Yönetmeliği m. 23",
     f"{DY}, disiplin kovuşturmasında savunmaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
     "Savunma, mali tatil dönemi içinde de istenebilir ve duruşma yapılabilir.",
     ["Savunması alınmadan meslek mensubuna disiplin cezası verilemez.",
      "Savunma için verilecek süre 15 günden az olamaz.",
      "Süresinde savunma yapmayan savunma hakkından vazgeçmiş sayılır.",
      "Savunma hakkını kullanmamak ayrı bir kovuşturma sebebi değildir."],
     "Disiplin Yönetmeliği m. 23'e göre mali tatil dönemi içinde savunma istenemez ve duruşma yapılamaz; diğer ifadeler aynı "
     "maddede yer alır.", topic="disiplin")

T3.oncul("Disiplin Yönetmeliği m. 15",
     "Bir meslek mensubu hakkında disiplin soruşturması başlatılmasına dayanak olabilecek başvurular değerlendirilmektedir:",
     ["İlgilinin ihbar veya şikâyeti",
      "Hazine ve Maliye Bakanlığının rapora dayanan isteği",
      "Müşterinin başka bir meslek mensubuyla sözleşme yapması",
      "Hükümlülükle sonuçlanan ceza davasının odaya ulaşması"],
     f"{DY}, yukarıdakilerden hangileri disiplin soruşturmasının dayanakları arasında sayılmıştır?",
     "I, II ve IV",
     ["Yalnız I", "I ve III", "II ve IV", "I, II ve IV", "II, III ve IV"],
     "Disiplin Yönetmeliği m. 15'e göre soruşturma ihbar veya şikâyet, oda ve Birlik kurullarının isteği, Bakanlığın veya kamu "
     "kurumlarının isteği ve hükümlülükle sonuçlanan ceza davasının odaya ulaşması üzerine yapılır. Müşterinin meslek "
     "mensubu değiştirmesi sayılmamıştır.", topic="disiplin", zorluk="hard")

T3.q("Sınav Yön. m. 16",
     f"{NY}, sınavda başarılı sayılmak için gerekli notlara ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
     "SMMM sınavında tezkiye notu ortalamaya dahil edilmez.",
     ["SMMM sınavında her konudan en az 50 almak gerekir.",
      "SMMM sınavında konuların ortalamasının en az 60 olması gerekir.",
      "YMM sınavında her konudan en az 50 almak gerekir.",
      "YMM sınavında notların ortalamasının en az 65 olması gerekir."],
     "Sınav Yönetmeliği m. 16/b'ye göre SMMM sınavında yanında staj yapılan meslek mensubunun verdiği tezkiye not ortalaması "
     "ayrı bir ders gibi ortalamaya dahil edilir.", topic="ruhsat_ve_staj")

T3.sayisal("SMGE Yön. m. 11",
     f"{GY}, eğitim kapsamındaki meslek mensubunun her üç yılda almak zorunda olduğu en az sürekli mesleki geliştirme eğitimi kredisi kaçtır?",
     "120", ["45", "60", "90", "150"],
     "SMGE Yönetmeliği m. 11'e göre meslek mensubu yılda en az 30, her üç yılda en az 120 kredi alır; yıllık en az 15, üç "
     "yılda en az 60 kredilik kısım doğrulanabilir olmalıdır.", topic="ruhsat_ve_staj")

T3.q("Defter ve Kayıtlar Yön. m. 15-16",
     "Bir YMM, eski müşterisinin talep ettiği tasdik raporu örneğini hazırlamaktadır. "
     f"Serbest Muhasebeci Mali Müşavirler ve Yeminli Mali Müşavirlerce Tutulacak Defter ve Kayıtlar ile Meslek Mensuplarının Bildirim Mecburiyeti Hakkında Yönetmelik’e göre, aşağıdaki ifadelerden hangisi yanlıştır?",
     "Tasdikli rapor örnekleri asıl rapor gibi işlem görmez.",
     ["Mali analiz, denetleme ve tasdik dosyaları gizlidir.",
      "Bu dosyalarla ilgili yazışmalar da gizli yapılır.",
      "İş sahibi firmalar önceki raporlardan örnek isteyebilir.",
      "Rapor örnekleri ücret tarifesindeki ücretin %1'i karşılığında verilir."],
     "Defter ve Kayıtlar Yönetmeliği m. 16'ya göre tasdikli rapor örnekleri asılları gibi işlem görür; dosyaların gizliliği "
     "m. 15'te, örnek verilmesi ve %1'lik bedel m. 16'da düzenlenmiştir.", topic="mesleki_sorumluluk")

if __name__ == "__main__":
    rc = 0
    for paket_ in (T1, T2, T3):
        rc |= paket_.yaz()
    sys.exit(rc)
