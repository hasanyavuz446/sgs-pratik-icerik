# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / TMS 7 Nakit Akış Tabloları — 60 soru.
Kaynak: KGK TMS 7. Aritmetik python'da hesaplanır.
Doğru şık KISA, çeldiriciler UZUN."""
import json, random, re

DERS, KONU = "muhasebe_standartlari", "tms_7_nakit_akis"
PREFIX, SEED = "std-tms7-gen", 20260923
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/tms_7_nakit_akis.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9: v = round(v)
    return f"{v:,}".replace(",", ".")

# ── A. Amaç, kapsam, tanımlar (12) ─────────────────────────────────────────
q("TMS 7'nin amacı bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit ve nakit benzerlerindeki değişimler hakkında nakit akış tablosu aracılığıyla bilgi verilmesini sağlamaktır",
  ["İşletmenin kâr veya zararının nasıl hesaplanacağını gösteren bir gelir tablosu standardıdır",
   "İşletmenin varlık ve kaynaklarının belirli bir tarihteki durumunu düzenleyen bir bilanço standardıdır",
   "İşletmenin gelecekteki nakit ihtiyacını tahmin eden bir bütçeleme yöntemi standardı niteliğindedir",
   "İşletmenin banka hesaplarının nasıl açılacağını düzenleyen bir bankacılık standardı olarak yayımlanmıştır"],
  "TMS 7: bu Standardın amacı, işletmenin nakit ve nakit benzerlerindeki tarihi değişikliklere ilişkin bilginin, dönem içindeki nakit akışlarını sınıflandıran bir nakit akış tablosu aracılığıyla verilmesini sağlamaktır.",
  "TMS 7 - amaç")

q("Nakit akış tablosunun kullanıcılara sağladığı fayda bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin nakit yaratma kabiliyetini ve nakit ihtiyacını değerlendirmeye imkân verir",
  ["İşletmenin piyasa değerini kesin ve tartışmasız biçimde ortaya koyan bir gösterge sunmaktadır",
   "İşletmenin gelecekteki kârını kesin olarak öngören bir tahmin aracı niteliğinde bilgi verir",
   "Yalnızca işletmenin vergi borcunu hesaplamaya yarayan bir bilgi kaynağı olarak kullanılmaktadır",
   "Yalnızca ortaklara dağıtılacak kâr payının tutarını gösteren bir hesaplama tablosu niteliğindedir"],
  "TMS 7: nakit akış bilgisi, kullanıcıların işletmenin nakit ve nakit benzeri yaratma kabiliyetini ve bu nakit akışlarını kullanma ihtiyacını değerlendirmesine imkân verir.",
  "TMS 7 - faydası")

q("Nakit ve nakit benzerleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit, kasadaki para ile vadesiz mevduattır; nakit benzeri ise değer riski önemsiz kısa vadeli yatırımdır",
  ["Nakit benzeri, işletmenin sahip olduğu tüm menkul kıymetleri kapsayan geniş bir kavram niteliğindedir",
   "Nakit yalnızca kasadaki fiziki parayı ifade eder; banka mevduatı hiçbir hâlde nakit sayılmaz",
   "Nakit benzeri, işletmenin uzun vadeli yatırım amacıyla elde tuttuğu hisse senetlerini kapsamaktadır",
   "Nakit ve nakit benzeri kavramları TMS 7'de tanımlanmamış olup uygulamada kullanılmamaktadır"],
  "TMS 7: nakit, işletmedeki nakit ile vadesiz mevduatı ifade eder. Nakit benzerleri, tutarı belirli bir nakde kolayca çevrilebilen, değer değişim riski önemsiz olan kısa vadeli ve yüksek likiditeye sahip yatırımlardır.",
  "TMS 7 - nakit ve nakit benzeri")

q("Nakit benzeri sayılma ölçütü bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit benzerleri yatırım amacıyla değil, kısa vadeli nakit taahhütleri karşılamak için elde tutulur",
  ["Nakit benzerleri uzun vadeli yatırım ve değer artışı amacıyla elde tutulan varlıkları ifade eder",
   "Nakit benzeri sayılmak için varlığın en az beş yıl vadeli olması şartı aranmaktadır",
   "Her türlü menkul kıymet, vadesine bakılmaksızın nakit benzeri olarak sınıflandırılmaktadır",
   "Nakit benzeri sayılmak için varlığın değerinde önemli dalgalanma olması gerekmektedir"],
  "TMS 7: nakit benzerleri, yatırım amacıyla veya diğer amaçlarla değil, kısa vadeli nakit taahhütlerini yerine getirmek amacıyla elde tutulur. Bu nedenle vadesi kısa ve değer değişim riski önemsiz olmalıdır.",
  "TMS 7 - nakit benzeri ölçütü")

q("Özkaynağa dayalı finansal araçların nakit benzeri sayılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Özkaynağa dayalı araçlar kural olarak nakit benzeri sayılmaz; ancak vadesine yakın alınan imtiyazlı paylar gibi istisnalar olabilir",
  ["Tüm özkaynağa dayalı finansal araçlar her hâlde nakit benzeri olarak sınıflandırılmak zorundadır",
   "Özkaynağa dayalı araçlar hiçbir istisna olmaksızın ve kesin biçimde nakit benzeri sayılamamaktadır",
   "Özkaynağa dayalı araçlar yalnızca borsada işlem görüyorsa her hâlde nakit benzeri sayılır",
   "Özkaynağa dayalı araçların sınıflandırılması TMS 7'de düzenlenmemiş olup serbest bırakılmıştır"],
  "TMS 7: özkaynağa dayalı finansal araçlara yapılan yatırımlar, esas itibarıyla nakit benzeri değildir. Ancak vadesine kısa süre kalmış ve itfa tarihi belirli imtiyazlı paylar gibi durumlar istisna oluşturabilir.",
  "TMS 7 - özkaynak araçları")

q("Bankalardan alınan kısa vadeli krediler bakımından aşağıdakilerden hangisi doğrudur?",
  "Banka borçları genellikle finansman faaliyetidir; vadesiz hesaba bağlı borçlu cari hesaplar ise nakit benzerine dâhil edilebilir",
  ["Tüm banka kredileri her hâlde nakit benzeri olarak sınıflandırılmak zorunda tutulmaktadır",
   "Tüm banka kredileri her hâlde işletme faaliyeti olarak sınıflandırılmak zorunda bulunmaktadır",
   "Banka kredileri nakit akış tablosunda hiçbir biçimde gösterilmez; yalnızca dipnotta açıklanır",
   "Banka kredileri yalnızca yatırım faaliyeti olarak sınıflandırılabilen bir kalem niteliğindedir"],
  "TMS 7: banka borçlanmaları genellikle finansman faaliyeti sayılır. Ancak bazı ülkelerde vadesiz mevduat hesaplarına bağlı ve bakiyesi sıklıkla artı-eksi arasında dalgalanan borçlu cari hesaplar, işletmenin nakit yönetiminin ayrılmaz parçasıysa nakit ve nakit benzerlerine dâhil edilir.",
  "TMS 7 - borçlu cari hesap")

q("Nakit ve nakit benzeri kalemler arasındaki hareketler bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit yönetiminin parçası olan bu hareketler nakit akışı sayılmaz; tabloda gösterilmez",
  ["Bu hareketler her hâlde işletme faaliyetinden nakit akışı olarak tabloda gösterilmek zorundadır",
   "Bu hareketler yatırım faaliyeti olarak sınıflandırılıp tabloda ayrıca raporlanmak zorunda tutulur",
   "Bu hareketler finansman faaliyeti sayılır ve nakit akış tablosunda ayrı bölümde sunulmaktadır",
   "Bu hareketler nakit akışı sayılır ve her biri brüt olarak tabloda gösterilmek zorunda bulunur"],
  "TMS 7: nakit ve nakit benzerleri kalemleri arasındaki hareketler (nakdin vadesiz mevduata yatırılması gibi), işletmenin nakit yönetiminin bir parçası olduğundan nakit akışı sayılmaz ve tabloda gösterilmez.",
  "TMS 7 - nakit içi hareketler")

q("Nakit akış tablosunun bölümleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit akışları işletme, yatırım ve finansman faaliyetleri olmak üzere üç bölümde raporlanır",
  ["Nakit akışları yalnızca tahsilat ve ödeme olarak iki bölümde toplanarak raporlanmaktadır",
   "Nakit akışları dönen ve duran varlıklar biçiminde ikiye ayrılarak bilanço düzeninde sunulur",
   "Nakit akış tablosunda hiçbir bölüm ayrımı yapılmaz; tüm hareketler tek toplam hâlinde gösterilir",
   "Nakit akışları kısa ve uzun vadeli olmak üzere vade esasına göre iki bölümde raporlanmaktadır"],
  "TMS 7: nakit akış tablosu, dönem içindeki nakit akışlarını işletme, yatırım ve finansman faaliyetleri bazında sınıflandırarak raporlar.",
  "TMS 7 - bölümler")

q("İşletme faaliyetleri bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin esas gelir getirici faaliyetleri ile yatırım ve finansman dışında kalan diğer faaliyetlerdir",
  ["İşletmenin uzun vadeli varlık edinim ve elden çıkarma faaliyetlerini ifade eden bölümdür",
   "İşletmenin özkaynak ve borçlanma yapısındaki değişimleri gösteren faaliyetleri kapsamaktadır",
   "İşletmenin yalnızca ortaklarıyla yaptığı sermaye işlemlerini kapsayan bir faaliyet türüdür",
   "İşletme faaliyetleri kavramı TMS 7'de tanımlanmamış olup uygulamada kullanılmamaktadır"],
  "TMS 7: işletme faaliyetleri, işletmenin esas gelir getirici faaliyetleri ile yatırım veya finansman faaliyeti olmayan diğer faaliyetlerdir. Bu bölümden gelen nakit akışı, işletmenin dış kaynağa başvurmadan nakit yaratma derecesini gösterir.",
  "TMS 7 - işletme faaliyetleri")

q("Yatırım faaliyetleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Uzun vadeli varlıkların ve nakit benzeri sayılmayan diğer yatırımların edinilmesi ile elden çıkarılmasına ilişkin faaliyetlerdir",
  ["İşletmenin esas gelir getirici faaliyetlerini ve olağan ticari işlemlerini kapsayan bölümdür",
   "İşletmenin özkaynak ve borçlanma yapısındaki değişiklikleri gösteren faaliyetleri ifade eder",
   "İşletmenin yalnızca stok alım ve satımını kapsayan bir faaliyet grubu olarak tanımlanmaktadır",
   "Yatırım faaliyetleri yalnızca ortaklara kâr payı ödemesini kapsayan bir bölümü ifade etmektedir"],
  "TMS 7: yatırım faaliyetleri, uzun vadeli varlıkların ve nakit benzeri sayılmayan diğer yatırımların edinilmesi ve elden çıkarılmasına ilişkin faaliyetlerdir. Gelecekte gelir ve nakit akışı yaratması amaçlanan harcamaları gösterir.",
  "TMS 7 - yatırım faaliyetleri")

q("Finansman faaliyetleri bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin özkaynağının ve borçlanmalarının büyüklüğünde ve bileşiminde değişiklik doğuran faaliyetlerdir",
  ["İşletmenin uzun vadeli varlık edinim ve satışlarını kapsayan bir faaliyet grubunu ifade eder",
   "İşletmenin esas gelir getirici faaliyetlerini ve olağan ticari işlemlerini kapsayan bölümdür",
   "Finansman faaliyetleri yalnızca stok alımını ve satıcılara yapılan ödemeleri kapsamaktadır",
   "Finansman faaliyetleri kavramı TMS 7'de düzenlenmemiş olup uygulamada kullanılmamaktadır"],
  "TMS 7: finansman faaliyetleri, işletmenin özkaynağının ve borçlanmalarının büyüklüğünde ve bileşiminde değişiklik meydana getiren faaliyetlerdir. Sermayeyi sağlayanların gelecekteki nakit akışı taleplerinin öngörülmesine yardımcı olur.",
  "TMS 7 - finansman faaliyetleri")

q("Aşağıdakilerden hangileri nakit akış tablosunun bölümlerindendir?\n\nI. İşletme faaliyetleri\n\nII. Pazarlama faaliyetleri\n\nIII. Üretim faaliyetleri",
  "Yalnız I",
  ["I, II ve III", "I ve II", "II ve III", "Yalnız III"],
  "TMS 7 nakit akışlarını işletme, yatırım ve finansman faaliyetleri olarak sınıflandırır. Bu nedenle işletme faaliyetleri (I) bir bölümken pazarlama (II) ve üretim (III) ayrı bölüm adları değildir.",
  "TMS 7 - bölümler")

# ── B. Faaliyet sınıflandırması (16) ───────────────────────────────────────
q("Mal ve hizmet satışından elde edilen nakit girişleri bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme faaliyetlerinden nakit girişi olarak sınıflandırılır",
  ["Yatırım faaliyetlerinden nakit girişi olarak sınıflandırılmak zorunda tutulan bir kalemdir",
   "Finansman faaliyetlerinden nakit girişi olarak raporlanan bir hareketi ifade etmektedir",
   "Nakit akış tablosunda hiçbir biçimde gösterilmez; yalnızca gelir tablosunda yer almaktadır",
   "İşletme faaliyetlerinden nakit çıkışı olarak gösterilir; satış nakit azalışı doğurmaktadır"],
  "TMS 7: mal satışı ve hizmet sunumundan elde edilen nakit girişleri, işletmenin esas gelir getirici faaliyetlerinden kaynaklandığından işletme faaliyeti olarak sınıflandırılır.",
  "TMS 7 - işletme faaliyeti")

q("Mal ve hizmet alımları için satıcılara yapılan ödemeler bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme faaliyetlerinden nakit çıkışı olarak sınıflandırılır",
  ["Yatırım faaliyetlerinden nakit çıkışı olarak sınıflandırılmak zorunda olan bir kalemdir",
   "Finansman faaliyetlerinden nakit çıkışı olarak raporlanan bir hareketi ifade etmektedir",
   "Nakit akış tablosunda gösterilmez; yalnızca bilançoda borç azalışı olarak izlenmektedir",
   "İşletme faaliyetlerinden nakit girişi olarak gösterilir; ödeme nakit artışı doğurmaktadır"],
  "TMS 7: mal ve hizmet alımları için satıcılara yapılan ödemeler işletmenin esas faaliyetiyle ilgili olduğundan işletme faaliyetlerinden nakit çıkışıdır.",
  "TMS 7 - işletme faaliyeti")

q("Maddi duran varlık satın alınması bakımından aşağıdakilerden hangisi doğrudur?",
  "Yatırım faaliyetlerinden nakit çıkışı olarak sınıflandırılır",
  ["İşletme faaliyetlerinden nakit çıkışı olarak sınıflandırılmak zorunda tutulan bir kalemdir",
   "Finansman faaliyetlerinden nakit çıkışı olarak raporlanan bir hareket niteliğindedir",
   "Nakit akış tablosunda hiç gösterilmez; yalnızca bilançoda varlık artışı olarak izlenmektedir",
   "Yatırım faaliyetlerinden nakit girişi olarak gösterilir; varlık edinimi giriş doğurmaktadır"],
  "TMS 7: maddi ve maddi olmayan duran varlıklar ile diğer uzun vadeli varlıkların edinimi için yapılan nakit ödemeler yatırım faaliyetlerinden nakit çıkışıdır.",
  "TMS 7 - yatırım faaliyeti")

q("Maddi duran varlık satışından elde edilen nakit bakımından aşağıdakilerden hangisi doğrudur?",
  "Yatırım faaliyetlerinden nakit girişi olarak sınıflandırılır",
  ["İşletme faaliyetlerinden nakit girişi olarak sınıflandırılmak zorunda tutulan bir kalemdir",
   "Finansman faaliyetlerinden nakit girişi olarak raporlanan bir hareketi ifade etmektedir",
   "Nakit akış tablosunda hiç gösterilmez; yalnızca gelir tablosunda satış kârı olarak izlenir",
   "Satış kârı işletme faaliyeti, satış bedeli ise finansman faaliyeti olarak ayrı sınıflandırılır"],
  "TMS 7: maddi ve maddi olmayan duran varlıkların ve diğer uzun vadeli varlıkların satışından sağlanan nakit girişleri yatırım faaliyetidir.",
  "TMS 7 - yatırım faaliyeti")

q("Pay ihracından sağlanan nakit bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansman faaliyetlerinden nakit girişi olarak sınıflandırılır",
  ["İşletme faaliyetlerinden nakit girişi olarak sınıflandırılmak zorunda olan bir kalemdir",
   "Yatırım faaliyetlerinden nakit girişi olarak raporlanan bir hareketi ifade etmektedir",
   "Nakit akış tablosunda gösterilmez; yalnızca özkaynak değişim tablosunda izlenmektedir",
   "Pay ihracı hasılat olarak kaydedilir ve işletme faaliyeti bölümünde raporlanmaktadır"],
  "TMS 7: pay ve diğer özkaynağa dayalı araçların ihracından sağlanan nakit girişleri finansman faaliyetidir; işletmenin özkaynak büyüklüğünü değiştirir.",
  "TMS 7 - finansman faaliyeti")

q("Kredi alınması ve kredi anaparasının geri ödenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İkisi de finansman faaliyeti olarak sınıflandırılır",
  ["Kredi alınması finansman, anapara ödemesi ise işletme faaliyeti olarak ayrı sınıflandırılır",
   "İkisi de işletme faaliyeti olarak sınıflandırılır; borçlanma olağan faaliyet sayılmaktadır",
   "İkisi de yatırım faaliyeti olarak sınıflandırılır; kredi bir yatırım hareketi kabul edilir",
   "Kredi hareketleri nakit akış tablosunda gösterilmez; yalnızca dipnotta açıklanmaktadır"],
  "TMS 7: borçlanma araçlarının ihracı ve kredi alınmasından sağlanan nakit girişleri ile borç anaparasının geri ödenmesine ilişkin nakit çıkışları finansman faaliyetidir; ikisi de borçlanma yapısını değiştirir.",
  "TMS 7 - finansman faaliyeti")

q("Faiz ve kâr payı akışlarının sınıflandırılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Her dönem tutarlı biçimde sınıflandırılmak koşuluyla işletme, yatırım veya finansman faaliyeti olarak sunulabilir",
  ["Faiz ve kâr payı her hâlde yalnızca işletme faaliyeti olarak sınıflandırılmak zorunda tutulmuştur",
   "Faiz ve kâr payı akışları nakit akış tablosunda hiçbir biçimde gösterilmez; dipnotta açıklanır",
   "Faiz ve kâr payı her dönem farklı bölümde sınıflandırılmak zorunda olup tutarlılık aranmaz",
   "Faiz ve kâr payının sınıflandırılması TMS 7'de düzenlenmemiş olup tümüyle serbest bırakılmıştır"],
  "TMS 7: faiz ve kâr payı tahsilat ve ödemelerinden kaynaklanan nakit akışları ayrı ayrı açıklanır ve her dönem tutarlı biçimde işletme, yatırım veya finansman faaliyeti olarak sınıflandırılır.",
  "TMS 7 - faiz ve kâr payı")

q("Gelir vergisi ödemelerinin sınıflandırılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Kural olarak işletme faaliyeti olarak sınıflandırılır; yatırım veya finansmanla ilişkilendirilebiliyorsa o bölümde gösterilir",
  ["Gelir vergisi ödemeleri her hâlde ve istisnasız finansman faaliyeti olarak sınıflandırılmaktadır",
   "Gelir vergisi ödemeleri her hâlde yatırım faaliyeti olarak sınıflandırılmak zorunda tutulmuştur",
   "Gelir vergisi ödemeleri nakit akış tablosunda gösterilmez; yalnızca gelir tablosunda yer alır",
   "Gelir vergisi ödemeleri üç bölüme eşit olarak paylaştırılarak raporlanmak zorunda bulunmaktadır"],
  "TMS 7: gelir vergilerinden kaynaklanan nakit akışları ayrı olarak açıklanır ve finansman ya da yatırım faaliyetiyle özellikle ilişkilendirilemiyorsa işletme faaliyeti olarak sınıflandırılır.",
  "TMS 7 - gelir vergisi")

q("Ortaklara ödenen kâr payları bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansman faaliyeti olarak sınıflandırılabilir; işletme faaliyeti olarak sunulması da mümkündür",
  ["Ortaklara ödenen kâr payı her hâlde yatırım faaliyeti olarak sınıflandırılmak zorundadır",
   "Ortaklara ödenen kâr payı nakit akış tablosunda hiçbir biçimde gösterilmemektedir",
   "Ortaklara ödenen kâr payı her hâlde gelir tablosunda gider olarak raporlanmak zorundadır",
   "Ortaklara ödenen kâr payının sınıflandırılması her dönem değiştirilmek zorunda tutulmuştur"],
  "TMS 7: ödenen kâr payları finansman faaliyeti olarak sınıflandırılabilir; çünkü finansman kaynağı elde etme maliyetidir. Kullanıcıların işletme faaliyetlerinden kâr payı ödeme kabiliyetini değerlendirmesine yardımcı olmak için işletme faaliyeti olarak da sınıflandırılabilir.",
  "TMS 7 - ödenen kâr payı")

q("Nakit içermeyen işlemler bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit gerektirmeyen yatırım ve finansman işlemleri nakit akış tablosuna dâhil edilmez; dipnotlarda açıklanır",
  ["Nakit içermeyen işlemler de her hâlde nakit akış tablosunda gösterilmek zorunda tutulmaktadır",
   "Nakit içermeyen işlemler hiçbir yerde raporlanmaz; ne tabloda ne dipnotta yer almamaktadır",
   "Nakit içermeyen işlemler yalnızca gelir tablosunda gösterilir; başka hiçbir yerde açıklanmaz",
   "Nakit içermeyen işlem kavramı TMS 7'de düzenlenmemiş olup uygulamada kullanılmamaktadır"],
  "TMS 7: nakit veya nakit benzeri kullanımını gerektirmeyen yatırım ve finansman işlemleri (borcun özkaynağa dönüştürülmesi, varlığın takasla edinimi gibi) nakit akış tablosuna dâhil edilmez; bu işlemler dipnotlarda açıklanır.",
  "TMS 7 - nakit içermeyen işlemler")

q("Bir işletme, kredi borcunu ortaklara pay verilerek özkaynağa dönüştürmüştür. TMS 7 bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit kullanımı gerektirmeyen bu işlem tabloya dâhil edilmez; dipnotlarda açıklanır",
  ["İşlem finansman faaliyetinden nakit girişi ve çıkışı olarak brüt biçimde gösterilmek zorundadır",
   "İşlem işletme faaliyetinden nakit akışı olarak raporlanır ve dönem nakdini artırmaktadır",
   "İşlem hiçbir yerde raporlanmaz; ne tabloda ne dipnotta açıklama yapılmasına gerek vardır",
   "İşlem yatırım faaliyeti olarak sınıflandırılır ve nakit çıkışı biçiminde gösterilmektedir"],
  "TMS 7: borcun özkaynağa dönüştürülmesi nakit veya nakit benzeri kullanımını gerektirmeyen bir finansman işlemidir; nakit akış tablosuna dâhil edilmez, dipnotlarda açıklanır.",
  "TMS 7 - nakit içermeyen işlem (senaryo)")

q("Yabancı para cinsinden işlemlerden kaynaklanan nakit akışları bakımından aşağıdakilerden hangisi doğrudur?",
  "İşlem tarihindeki kur kullanılarak işletmenin geçerli para birimine çevrilir",
  ["Yabancı para nakit akışları hiçbir biçimde çevrilmez; yabancı para olarak raporlanmaktadır",
   "Yabancı para nakit akışları her hâlde dönem başındaki kur kullanılarak çevrilmek zorundadır",
   "Yabancı para nakit akışları nakit akış tablosunda gösterilmez; yalnızca dipnotta açıklanır",
   "Yabancı para nakit akışları için işletme dilediği kuru serbestçe seçip uygulayabilmektedir"],
  "TMS 7: yabancı para birimi cinsinden işlemlerden kaynaklanan nakit akışları, yabancı para tutarına nakit akışının gerçekleştiği tarihteki geçerli para birimi ile yabancı para arasındaki kur uygulanmak suretiyle çevrilir.",
  "TMS 7 - yabancı para")

q("Kur değişiminin nakit üzerindeki etkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Yabancı para nakit mevcudundaki kur farkı nakit akışı değildir; ancak nakit değişimini uzlaştırmak için tabloda ayrı sunulur",
  ["Kur farkı her hâlde işletme faaliyetinden nakit akışı olarak raporlanmak zorunda tutulmaktadır",
   "Kur farkı yatırım faaliyeti olarak sınıflandırılır ve nakit giriş çıkışı biçiminde gösterilir",
   "Kur farkı hiçbir yerde gösterilmez; nakit akış tablosunda uzlaştırma yapılmasına gerek yoktur",
   "Kur farkı finansman faaliyetinden nakit girişi olarak raporlanan bir kalem niteliğindedir"],
  "TMS 7: yabancı para cinsinden nakit ve nakit benzerlerine ilişkin kur değişim etkisi nakit akışı değildir. Ancak dönem başı ve sonu nakit mevcudunu uzlaştırmak amacıyla, işletme/yatırım/finansman akışlarından ayrı olarak nakit akış tablosunda sunulur.",
  "TMS 7 - kur etkisi")

q("Aşağıdakilerden hangileri TMS 7'ye göre yatırım faaliyeti sayılır?\n\nI. Maddi duran varlık satın alınması\n\nII. Maddi duran varlık satılması\n\nIII. Kredi anaparasının ödenmesi",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Uzun vadeli varlıkların edinimi (I) ve elden çıkarılması (II) yatırım faaliyetidir. Kredi anaparasının ödenmesi (III) ise borçlanma yapısını değiştirdiğinden finansman faaliyetidir; bu nedenle yanlıştır.",
  "TMS 7 - faaliyet sınıflandırması")

q("Aşağıdakilerden hangileri TMS 7'ye göre finansman faaliyeti sayılır?\n\nI. Pay ihracından sağlanan nakit\n\nII. Kredi alınmasından sağlanan nakit\n\nIII. Kredi anaparasının geri ödenmesi",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Pay ihracı (I), kredi alınması (II) ve kredi anaparasının ödenmesi (III) işletmenin özkaynak ve borçlanma yapısını değiştirdiğinden finansman faaliyetidir. Üçü de doğrudur.",
  "TMS 7 - finansman faaliyeti")

q("Aşağıdaki ifadelerden hangileri TMS 7 bakımından doğrudur?\n\nI. Faiz ve kâr payı akışları tutarlı biçimde sınıflandırılır\n\nII. Gelir vergisi kural olarak işletme faaliyetidir\n\nIII. Nakit içermeyen işlemler tabloda gösterilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Faiz/kâr payı tutarlı sınıflandırılır (I) ve gelir vergisi kural olarak işletme faaliyetidir (II). Nakit içermeyen işlemler ise tabloya dâhil edilmez, dipnotta açıklanır; bu nedenle III yanlıştır.",
  "TMS 7 - sınıflandırma")

# ── C. Doğrudan ve dolaylı yöntem (16) ─────────────────────────────────────
q("İşletme faaliyetlerinden nakit akışlarının sunum yöntemleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Doğrudan yöntem veya dolaylı yöntem kullanılabilir; doğrudan yöntemin kullanılması teşvik edilir",
  ["Yalnızca dolaylı yöntem kullanılabilir; doğrudan yöntem TMS 7'de kabul edilmemiş bulunmaktadır",
   "Yalnızca doğrudan yöntem kullanılabilir; dolaylı yöntem kesin olarak yasaklanmış durumdadır",
   "İki yöntem de aynı anda ve birlikte kullanılmak zorunda olup tek yöntem yeterli görülmemektedir",
   "Yöntem seçimi TMS 7'de düzenlenmemiş olup işletme her dönem farklı yöntem kullanabilmektedir"],
  "TMS 7: işletme, işletme faaliyetlerinden nakit akışlarını doğrudan yöntem (brüt nakit giriş ve çıkış sınıflarının belirtildiği) veya dolaylı yöntem (kâr/zararın düzeltildiği) kullanarak raporlar. Standart doğrudan yöntemin kullanılmasını teşvik eder.",
  "TMS 7 - yöntemler")

q("Doğrudan yöntem bakımından aşağıdakilerden hangisi doğrudur?",
  "Brüt nakit girişleri ve brüt nakit çıkışları ana sınıflar itibarıyla ayrı ayrı gösterilir",
  ["Dönem kâr veya zararı, gayrinakdi kalemler için düzeltilerek nakit akışına ulaşılan bir yöntemdir",
   "Yalnızca dönem sonundaki nakit bakiyesinin gösterildiği ve hareketlerin sunulmadığı bir yöntemdir",
   "Yalnızca yatırım faaliyetlerinde kullanılabilen ve işletme faaliyetlerinde uygulanmayan bir yöntemdir",
   "Doğrudan yöntem TMS 7'de tanımlanmamış olup uygulamada hiç kullanılmayan bir yöntemdir"],
  "TMS 7: doğrudan yöntemde brüt nakit girişleri ve brüt nakit çıkışlarına ilişkin ana gruplar belirtilir (müşterilerden tahsilatlar, tedarikçilere ödemeler gibi).",
  "TMS 7 - doğrudan yöntem")

q("Dolaylı yöntem bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönem kâr veya zararı; gayrinakdi işlemler, işletme sermayesi değişimleri ve yatırım/finansman kalemleri için düzeltilir",
  ["Brüt nakit giriş ve çıkışlarının ana sınıflar itibarıyla ayrı ayrı gösterildiği bir yöntemdir",
   "Yalnızca dönem sonu nakit bakiyesinin raporlandığı ve düzeltme yapılmayan bir yöntem niteliğindedir",
   "Yalnızca finansman faaliyetlerinde kullanılabilen ve işletme faaliyetlerinde uygulanmayan yöntemdir",
   "Dolaylı yöntem TMS 7'de kabul edilmeyen ve kullanılması yasaklanmış bir yöntemi ifade eder"],
  "TMS 7: dolaylı yöntemde işletme faaliyetlerinden nakit akışı; dönem kâr veya zararının gayrinakdi işlemler, geçmiş/gelecek nakit akışlarına ilişkin ertelemeler ve tahakkuklar ile yatırım/finansman nakit akışlarıyla ilgili gelir/gider kalemlerinin etkileri için düzeltilmesiyle bulunur.",
  "TMS 7 - dolaylı yöntem")

q("Dolaylı yöntemde amortisman gideri bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit çıkışı gerektirmediğinden dönem kârına eklenir",
  ["Nakit çıkışı gerektirdiğinden dönem kârından ayrıca düşülmek zorunda olan bir kalemdir",
   "Amortisman gideri dolaylı yöntemde hiçbir düzeltmeye konu edilmez; göz ardı edilmektedir",
   "Amortisman gideri yatırım faaliyetinden nakit çıkışı olarak ayrıca raporlanmak zorundadır",
   "Amortisman gideri finansman faaliyetinden nakit çıkışı olarak sınıflandırılan bir kalemdir"],
  "TMS 7: dolaylı yöntemde amortisman gibi gayrinakdi giderler, kâr/zararı azaltmış ancak nakit çıkışı doğurmamış olduğundan dönem kârına geri eklenir.",
  "TMS 7 - dolaylı yöntem düzeltmesi")

q("Dolaylı yöntemde ticari alacaklardaki artış bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakde dönüşmemiş hasılatı gösterdiğinden dönem kârından düşülür",
  ["Nakit girişi doğurduğundan dönem kârına eklenmek zorunda olan bir düzeltme kalemidir",
   "Ticari alacaklardaki değişim dolaylı yöntemde hiçbir düzeltmeye konu edilmemektedir",
   "Ticari alacaklardaki artış yatırım faaliyetinden nakit girişi olarak raporlanmaktadır",
   "Ticari alacaklardaki artış finansman faaliyeti olarak sınıflandırılan bir hareketi ifade eder"],
  "Dolaylı yöntemde ticari alacaklardaki artış, hasılatın tahsil edilmemiş kısmını gösterir; kârda yer aldığı hâlde nakde dönüşmediğinden dönem kârından düşülür.",
  "TMS 7 - işletme sermayesi düzeltmesi")

q("Dolaylı yöntemde ticari borçlardaki artış bakımından aşağıdakilerden hangisi doğrudur?",
  "Henüz ödenmemiş gideri gösterdiğinden dönem kârına eklenir",
  ["Nakit çıkışı doğurduğundan dönem kârından düşülmek zorunda olan bir düzeltme kalemidir",
   "Ticari borçlardaki değişim dolaylı yöntemde hiçbir düzeltmeye konu edilmemektedir",
   "Ticari borçlardaki artış finansman faaliyetinden nakit girişi olarak raporlanmak zorundadır",
   "Ticari borçlardaki artış yatırım faaliyeti olarak sınıflandırılan bir hareketi ifade etmektedir"],
  "Dolaylı yöntemde ticari borçlardaki artış, giderin kâra yansıdığı ancak henüz ödenmediğini gösterir; bu nedenle dönem kârına eklenir.",
  "TMS 7 - işletme sermayesi düzeltmesi")

q("Dolaylı yöntemde maddi duran varlık satış kârı bakımından aşağıdakilerden hangisi doğrudur?",
  "Yatırım faaliyetiyle ilgili olduğundan işletme faaliyeti bölümünde dönem kârından düşülür",
  ["Dönem kârına eklenmek zorunda olan bir düzeltme kalemi olarak işletme bölümünde gösterilir",
   "Satış kârı dolaylı yöntemde hiçbir düzeltmeye konu edilmez; olduğu gibi bırakılmaktadır",
   "Satış kârı finansman faaliyetinden nakit girişi olarak ayrıca raporlanmak zorunda tutulmuştur",
   "Satış kârı hiçbir bölümde gösterilmez; yalnızca dipnotlarda açıklanmak zorunda bulunmaktadır"],
  "TMS 7: duran varlık satış kârı yatırım faaliyetiyle ilgili bir gelir kalemidir; kâr içinde yer aldığından işletme faaliyeti bölümünde düşülür, satıştan sağlanan nakdin tamamı yatırım bölümünde gösterilir.",
  "TMS 7 - yatırım kalemi düzeltmesi")

nk, amort, alacak_artis = 200_000, 60_000, 40_000
v = nk + amort - alacak_artis
q(f"Dönem net kârı {tr(nk)} TL, amortisman gideri {tr(amort)} TL ve ticari alacaklardaki artış {tr(alacak_artis)} TL'dir. Başka düzeltme yoksa dolaylı yönteme göre işletme faaliyetlerinden nakit akışı kaç TL'dir?",
  f"{tr(v)} TL",
  [f"{tr(nk - amort - alacak_artis)} TL", f"{tr(nk + amort + alacak_artis)} TL", f"{tr(nk - amort + alacak_artis)} TL", f"{tr(nk)} TL"],
  f"Amortisman nakit çıkışı gerektirmediğinden eklenir; alacak artışı nakde dönüşmemiş hasılatı gösterdiğinden düşülür: {tr(nk)} + {tr(amort)} − {tr(alacak_artis)} = {tr(v)} TL.",
  "TMS 7 - dolaylı yöntem")

nk2, amort2, stok_azalis, borc_artis = 150_000, 40_000, 25_000, 30_000
v2 = nk2 + amort2 + stok_azalis + borc_artis
q(f"Dönem net kârı {tr(nk2)} TL, amortisman {tr(amort2)} TL, stoklarda azalış {tr(stok_azalis)} TL ve ticari borçlarda artış {tr(borc_artis)} TL'dir. Dolaylı yönteme göre işletme faaliyetlerinden nakit akışı kaç TL'dir?",
  f"{tr(v2)} TL",
  [f"{tr(nk2 + amort2 - stok_azalis - borc_artis)} TL", f"{tr(nk2 - amort2 + stok_azalis + borc_artis)} TL",
   f"{tr(nk2 + amort2 - stok_azalis + borc_artis)} TL", f"{tr(nk2)} TL"],
  f"Amortisman eklenir; stoklardaki azalış nakde dönüşen varlığı, borçlardaki artış ise ödenmemiş gideri gösterdiğinden ikisi de eklenir: {tr(nk2)} + {tr(amort2)} + {tr(stok_azalis)} + {tr(borc_artis)} = {tr(v2)} TL.",
  "TMS 7 - dolaylı yöntem")

nk3, satis_kari, amort3 = 180_000, 20_000, 35_000
v3 = nk3 - satis_kari + amort3
q(f"Dönem net kârı {tr(nk3)} TL olup içinde {tr(satis_kari)} TL maddi duran varlık satış kârı bulunmaktadır. Amortisman gideri {tr(amort3)} TL'dir. Başka düzeltme yoksa işletme faaliyetlerinden nakit akışı kaç TL'dir?",
  f"{tr(v3)} TL",
  [f"{tr(nk3 + satis_kari + amort3)} TL", f"{tr(nk3 + satis_kari - amort3)} TL", f"{tr(nk3 - satis_kari - amort3)} TL", f"{tr(nk3)} TL"],
  f"Duran varlık satış kârı yatırım faaliyetiyle ilgili olduğundan işletme bölümünde düşülür; amortisman gayrinakdi olduğundan eklenir: {tr(nk3)} − {tr(satis_kari)} + {tr(amort3)} = {tr(v3)} TL.",
  "TMS 7 - yatırım kalemi düzeltmesi")

isl, yat, fin, bas = 320_000, -180_000, -60_000, 90_000
son = bas + isl + yat + fin
q(f"İşletme faaliyetlerinden nakit akışı {tr(isl)} TL, yatırım faaliyetlerinden {tr(abs(yat))} TL çıkış, finansman faaliyetlerinden {tr(abs(fin))} TL çıkış olmuştur. Dönem başı nakit {tr(bas)} TL ise dönem sonu nakit kaç TL'dir?",
  f"{tr(son)} TL",
  [f"{tr(bas + isl + abs(yat) + abs(fin))} TL", f"{tr(isl + yat + fin)} TL", f"{tr(bas + isl)} TL", f"{tr(bas - isl + yat + fin)} TL"],
  f"Dönem sonu nakit = Dönem başı + İşletme + Yatırım + Finansman = {tr(bas)} + {tr(isl)} − {tr(abs(yat))} − {tr(abs(fin))} = {tr(son)} TL.",
  "TMS 7 - net nakit değişimi")

satis, alacak_art = 900_000, 70_000
tahsilat = satis - alacak_art
q(f"Dönem net satışları {tr(satis)} TL ve ticari alacaklardaki artış {tr(alacak_art)} TL'dir. Doğrudan yönteme göre müşterilerden yapılan tahsilat kaç TL'dir?",
  f"{tr(tahsilat)} TL",
  [f"{tr(satis + alacak_art)} TL", f"{tr(satis)} TL", f"{tr(alacak_art)} TL", f"{tr(satis - alacak_art*2)} TL"],
  f"Müşterilerden tahsilat = Net satışlar − Ticari alacaklardaki artış = {tr(satis)} − {tr(alacak_art)} = {tr(tahsilat)} TL. Alacak arttıysa satışın bir kısmı henüz tahsil edilmemiştir.",
  "TMS 7 - doğrudan yöntem")

q("Nakit akışlarının brüt gösterimi bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit akışları kural olarak brüt esasa göre ayrı ayrı raporlanır; kanunda sayılan hâllerde net gösterilebilir",
  ["Tüm nakit akışları her hâlde net tutar üzerinden gösterilmek zorunda olup brüt gösterim yasaktır",
   "Nakit akışlarının gösterim biçimi TMS 7'de düzenlenmemiş olup tümüyle serbest bırakılmıştır",
   "Nakit akışları yalnızca dönem sonunda tek bir toplam olarak raporlanmak zorunda tutulmuştur",
   "Brüt gösterim yalnızca işletme faaliyetlerinde zorunlu olup diğer bölümlerde uygulanmamaktadır"],
  "TMS 7: yatırım ve finansman faaliyetlerinden kaynaklanan brüt nakit girişleri ve brüt nakit çıkışları ana gruplar itibarıyla ayrı ayrı raporlanır. Ancak müşteri adına yapılan tahsilat/ödemeler ile devir hızı yüksek, tutarı büyük ve vadesi kısa kalemler net olarak raporlanabilir.",
  "TMS 7 - brüt gösterim")

q("Aşağıdaki ifadelerden hangileri dolaylı yöntem düzeltmeleri bakımından doğrudur?\n\nI. Amortisman dönem kârına eklenir\n\nII. Ticari alacaklardaki artış dönem kârından düşülür\n\nIII. Ticari borçlardaki artış dönem kârından düşülür",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Amortisman eklenir (I) ve alacaklardaki artış düşülür (II). Ancak ticari borçlardaki artış, ödenmemiş gideri gösterdiğinden kâra EKLENİR; bu nedenle III yanlıştır.",
  "TMS 7 - dolaylı yöntem düzeltmeleri")

q("Aşağıdakilerden hangileri işletme faaliyetlerinden nakit akışının sunumunda kullanılabilir?\n\nI. Doğrudan yöntem\n\nII. Dolaylı yöntem\n\nIII. Yalnızca dönem sonu bakiye gösterimi",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "TMS 7 işletme faaliyetlerinde doğrudan (I) ve dolaylı (II) yöntemlere izin verir; doğrudan yöntem teşvik edilir. Yalnızca bakiye gösterimi (III) bir sunum yöntemi değildir.",
  "TMS 7 - yöntemler")

q("Aşağıdaki ifadelerden hangileri TMS 7 bakımından doğrudur?\n\nI. Doğrudan yöntemin kullanılması teşvik edilir\n\nII. Kur farkı nakit akışı değildir ama uzlaştırma için sunulur\n\nIII. Nakit benzerleri uzun vadeli yatırım amacıyla elde tutulur",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Doğrudan yöntem teşvik edilir (I) ve kur farkı nakit akışı olmasa da uzlaştırma için sunulur (II). Nakit benzerleri ise yatırım amacıyla değil, kısa vadeli nakit taahhütleri karşılamak için tutulur; bu nedenle III yanlıştır.",
  "TMS 7 - genel")

# ── D. Özel konular ve açıklamalar (16) ────────────────────────────────────
q("Bağlı ortaklık ve diğer işletmelerin edinimi veya elden çıkarılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Bu işlemlerden kaynaklanan nakit akışları ayrı olarak sunulur ve yatırım faaliyeti olarak sınıflandırılır",
  ["Bu işlemler her hâlde işletme faaliyeti olarak sınıflandırılmak zorunda tutulan hareketlerdir",
   "Bu işlemler finansman faaliyeti olarak sınıflandırılır ve özkaynak yapısını değiştirmektedir",
   "Bu işlemler nakit akış tablosunda hiçbir biçimde gösterilmez; yalnızca dipnotta açıklanmaktadır",
   "Bu işlemler diğer yatırım hareketleriyle birleştirilerek tek bir toplam hâlinde sunulmak zorundadır"],
  "TMS 7: bağlı ortaklıkların ve diğer işletmelerin edinimi veya elden çıkarılmasından kaynaklanan toplam nakit akışları ayrı olarak sunulur ve yatırım faaliyeti olarak sınıflandırılır.",
  "TMS 7 - bağlı ortaklık edinimi")

q("Bağlı ortaklık ediniminde ödenen bedel bakımından aşağıdakilerden hangisi doğrudur?",
  "Ödenen bedelden edinilen nakit ve nakit benzerleri düşülerek net tutar gösterilir",
  ["Ödenen bedelin tamamı brüt olarak gösterilir; edinilen nakit hiçbir hâlde düşülmemektedir",
   "Ödenen bedel hiç gösterilmez; yalnızca edinilen varlıkların toplamı raporlanmak zorundadır",
   "Ödenen bedel finansman faaliyeti olarak sınıflandırılıp özkaynak bölümünde gösterilmektedir",
   "Ödenen bedel işletme faaliyetinden nakit çıkışı olarak raporlanmak zorunda tutulmaktadır"],
  "TMS 7: bağlı ortaklık veya diğer işletmelerin ediniminden kaynaklanan nakit akışları, edinilen nakit ve nakit benzerleri düşülerek net olarak sunulur.",
  "TMS 7 - edinimde net gösterim")

q("Finansal kuruluşlarda faiz akışları bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal kuruluşlarda ödenen ve tahsil edilen faizler ile kâr payları genellikle işletme faaliyeti olarak sınıflandırılır",
  ["Finansal kuruluşlarda faiz akışları her hâlde finansman faaliyeti olarak sınıflandırılmaktadır",
   "Finansal kuruluşlarda faiz akışları her hâlde yatırım faaliyeti olarak raporlanmak zorundadır",
   "Finansal kuruluşlar nakit akış tablosu düzenlemekten tümüyle muaf tutulmuş bulunmaktadır",
   "Finansal kuruluşlarda faiz akışları hiçbir bölümde gösterilmez; dipnotta açıklanmaktadır"],
  "TMS 7: finansal kuruluşlar açısından ödenen ve tahsil edilen faizler ile kâr payları genellikle işletme faaliyetleri olarak sınıflandırılır; çünkü bunlar esas gelir getirici faaliyetlerinin parçasıdır.",
  "TMS 7 - finansal kuruluşlarda faiz")

q("Nakit akış tablosunda nakit mevcudunun uzlaştırılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit akış tablosundaki tutarlar ile finansal durum tablosundaki nakit kalemleri uzlaştırılarak açıklanır",
  ["Nakit akış tablosu ile bilanço arasında hiçbir uzlaştırma yapılmasına gerek bulunmamaktadır",
   "Uzlaştırma yalnızca vergi idaresi talep ettiğinde ve onun belirlediği biçimde yapılmaktadır",
   "Uzlaştırma yalnızca doğrudan yöntem kullanan işletmelerde zorunlu olup dolaylıda aranmaz",
   "Uzlaştırma kavramı TMS 7'de düzenlenmemiş olup uygulamada hiç yapılmayan bir işlemdir"],
  "TMS 7: işletme, nakit akış tablosundaki nakit ve nakit benzerleri tutarları ile finansal durum tablosunda raporlanan ilgili kalemleri uzlaştırarak açıklar.",
  "TMS 7 - uzlaştırma")

q("Kullanıma hazır olmayan nakit bakımından aşağıdakilerden hangisi doğrudur?",
  "Grup tarafından kullanılamayan önemli nakit ve nakit benzeri tutarları yönetimin açıklamasıyla birlikte belirtilir",
  ["Kullanıma hazır olmayan nakit hiçbir biçimde açıklanmaz; tüm nakit tek toplam gösterilmektedir",
   "Kullanıma hazır olmayan nakit, nakit ve nakit benzerlerinden tümüyle çıkarılmak zorunda tutulmuştur",
   "Kullanıma hazır olmayan nakit yatırım faaliyeti olarak sınıflandırılıp ayrı bölümde raporlanır",
   "Kullanıma hazır olmayan nakit kavramı TMS 7'de düzenlenmemiş olup uygulanmamaktadır"],
  "TMS 7: işletme, grup tarafından kullanılamayan önemli tutardaki nakit ve nakit benzerlerini yönetimin görüşüyle birlikte açıklar (kambiyo kısıtı bulunan ülkelerdeki bağlı ortaklık nakdi gibi).",
  "TMS 7 - kullanılamayan nakit")

q("Nakit akış tablosunun diğer tablolarla ilişkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Diğer finansal tablolarla birlikte kullanıldığında net varlıklardaki değişimi ve likiditeyi değerlendirmeye imkân verir",
  ["Nakit akış tablosu diğer tablolardan tümüyle bağımsızdır ve onlarla birlikte kullanılamamaktadır",
   "Nakit akış tablosu bilançonun yerine geçer; bilanço ayrıca düzenlenmesine gerek bırakmaz",
   "Nakit akış tablosu yalnızca gelir tablosunun bir eki olup bağımsız bir tablo niteliği taşımaz",
   "Nakit akış tablosu yalnızca vergi beyannamesine ek olarak düzenlenen bir belge niteliğindedir"],
  "TMS 7: nakit akış tablosu, diğer finansal tablolarla birlikte kullanıldığında net varlıklardaki değişimi, finansal yapıyı (likidite ve borç ödeme gücü dâhil) ve nakit akışlarının tutar ve zamanlamasını etkileme kabiliyetini değerlendirmeye imkân verir.",
  "TMS 7 - diğer tablolarla ilişki")

q("Nakit akış tablosu düzenleme zorunluluğu bakımından aşağıdakilerden hangisi doğrudur?",
  "TMS 7 uygulayan tüm işletmeler nakit akış tablosu düzenler ve bunu tam finansal tablo setinin ayrılmaz parçası olarak sunar",
  ["Nakit akış tablosu yalnızca büyük ölçekli işletmelerce düzenlenir; küçükler bundan muaftır",
   "Nakit akış tablosu düzenlenmesi tümüyle isteğe bağlı olup hiçbir işletme için zorunlu değildir",
   "Nakit akış tablosu yalnızca finansal kuruluşlarca düzenlenir; diğer sektörler kapsam dışıdır",
   "Nakit akış tablosu yalnızca işletme zarar ettiğinde düzenlenmek zorunda tutulan bir tablodur"],
  "TMS 7: işletme, bu Standarda uygun olarak nakit akış tablosu düzenler ve bunu finansal tabloların sunulduğu her dönem için tam finansal tablo setinin ayrılmaz bir parçası olarak sunar.",
  "TMS 7 - düzenleme zorunluluğu")

q("İşletme faaliyetlerinden nakit akışının önemi bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin dış finansmana başvurmadan borç ödeme, kapasite koruma ve kâr payı dağıtma kabiliyetini gösteren temel bir göstergedir",
  ["İşletme faaliyetlerinden nakit akışı, işletmenin piyasa değerini kesin biçimde ortaya koymaktadır",
   "İşletme faaliyetlerinden nakit akışı yalnızca vergi matrahını hesaplamak için kullanılmaktadır",
   "İşletme faaliyetlerinden nakit akışının hiçbir analitik değeri bulunmayıp yalnızca biçimseldir",
   "İşletme faaliyetlerinden nakit akışı, dönem kârıyla her hâlde birebir aynı tutarı göstermektedir"],
  "TMS 7: işletme faaliyetlerinden kaynaklanan nakit akışlarının tutarı, işletmenin dış finansman kaynaklarına başvurmadan borçlarını ödeyip ödeyemeyeceğinin, faaliyet kapasitesini koruyup koruyamayacağının ve kâr payı dağıtıp dağıtamayacağının temel göstergesidir.",
  "TMS 7 - işletme nakit akışının önemi")

q("Bir işletme, satın aldığı makinenin bedelini nakit ödemek yerine kendi çıkardığı payları vererek karşılamıştır. TMS 7 bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit kullanımı olmadığından işlem tabloya alınmaz; dipnotlarda açıklanır",
  ["İşlem yatırım faaliyetinden nakit çıkışı ve finansman faaliyetinden nakit girişi olarak gösterilir",
   "İşlem yalnızca yatırım faaliyeti bölümünde nakit çıkışı olarak raporlanmak zorunda tutulmuştur",
   "İşlem işletme faaliyeti olarak sınıflandırılıp dönem nakdini azaltan bir kalem olarak gösterilir",
   "İşlem hiçbir yerde raporlanmaz; dipnotta dahi açıklanmasına gerek bulunmamaktadır"],
  "TMS 7: varlıkların pay ihracıyla veya takas yoluyla edinilmesi nakit kullanımı gerektirmeyen bir işlemdir; nakit akış tablosuna dâhil edilmez, dipnotlarda açıklanır.",
  "TMS 7 - nakit içermeyen işlem (senaryo)")

q("Bir işletmenin vadesiz mevduatındaki parayı kasaya çekmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit ve nakit benzerleri arasındaki hareket olduğundan nakit akışı sayılmaz ve tabloda gösterilmez",
  ["İşletme faaliyetlerinden nakit girişi olarak raporlanır ve dönem nakdini artırmaktadır",
   "Yatırım faaliyetlerinden nakit çıkışı olarak sınıflandırılıp tabloda gösterilmek zorundadır",
   "Finansman faaliyeti olarak sınıflandırılır; nakit yapısını değiştiren bir hareket sayılmaktadır",
   "İşlem brüt olarak hem giriş hem çıkış biçiminde tabloda iki kez gösterilmek zorunda kalır"],
  "TMS 7: nakit ve nakit benzerleri kalemleri arasındaki hareketler işletmenin nakit yönetiminin parçası olduğundan nakit akışı sayılmaz; nakit akış tablosunda gösterilmez.",
  "TMS 7 - nakit içi hareket (senaryo)")

q("Bir işletme faiz ödemelerini geçen yıl finansman faaliyeti olarak sınıflandırmış, bu yıl işletme faaliyetine almak istemektedir. TMS 7 bakımından aşağıdakilerden hangisi doğrudur?",
  "Faiz akışları her dönem tutarlı biçimde sınıflandırılmalıdır; keyfî değiştirilmesi uygun değildir",
  ["İşletme faiz sınıflandırmasını her dönem serbestçe ve gerekçesiz olarak değiştirebilmektedir",
   "Faiz ödemeleri her hâlde yalnızca finansman faaliyeti olarak sınıflandırılmak zorunda tutulur",
   "Faiz ödemeleri nakit akış tablosunda hiç gösterilmez; yalnızca gelir tablosunda yer almaktadır",
   "Faiz ödemeleri her yıl farklı bölümde gösterilmek zorunda olup tutarlılık aranmamaktadır"],
  "TMS 7: faiz ve kâr payı akışlarının her biri ayrı açıklanır ve dönemler itibarıyla tutarlı biçimde işletme, yatırım veya finansman faaliyeti olarak sınıflandırılır. Tutarlılık esastır.",
  "TMS 7 - faiz tutarlılığı (senaryo)")

q("Aşağıdakilerden hangileri TMS 7'ye göre dipnotlarda açıklanır?\n\nI. Nakit içermeyen yatırım ve finansman işlemleri\n\nII. Nakit akış tablosu ile bilanço nakit kalemlerinin uzlaştırılması\n\nIII. Grup tarafından kullanılamayan önemli nakit tutarları",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 7: nakit içermeyen işlemler (I), nakit ve nakit benzerlerinin uzlaştırılması (II) ve kullanılamayan önemli nakit tutarları (III) dipnotlarda açıklanır. Üçü de doğrudur.",
  "TMS 7 - açıklamalar")

q("Aşağıdaki ifadelerden hangileri TMS 7 bakımından doğrudur?\n\nI. Bağlı ortaklık edinimi yatırım faaliyetidir\n\nII. Edinimde ödenen bedelden edinilen nakit düşülerek net gösterilir\n\nIII. Nakit akış tablosu isteğe bağlı bir tablodur",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Bağlı ortaklık edinimi yatırım faaliyetidir (I) ve edinilen nakit düşülerek net gösterilir (II). Nakit akış tablosu ise tam finansal tablo setinin ayrılmaz parçasıdır, isteğe bağlı değildir; bu nedenle III yanlıştır.",
  "TMS 7 - genel")

alis, stok_art, borc_azalis = 600_000, 50_000, 30_000
odeme = alis + stok_art + borc_azalis
q(f"Dönem satışların maliyeti {tr(alis)} TL, stoklarda artış {tr(stok_art)} TL ve ticari borçlarda azalış {tr(borc_azalis)} TL'dir. Doğrudan yönteme göre satıcılara yapılan ödeme kaç TL'dir?",
  f"{tr(odeme)} TL",
  [f"{tr(alis - stok_art - borc_azalis)} TL", f"{tr(alis + stok_art - borc_azalis)} TL", f"{tr(alis)} TL", f"{tr(stok_art + borc_azalis)} TL"],
  f"Satıcılara ödeme = SMM + Stok artışı + Borç azalışı = {tr(alis)} + {tr(stok_art)} + {tr(borc_azalis)} = {tr(odeme)} TL. Stok artışı ek alımı, borç azalışı ise geçmiş borcun ödendiğini gösterir.",
  "TMS 7 - doğrudan yöntem")

isl2, yat2, fin2, bas2, kur = 250_000, -400_000, 300_000, 60_000, 15_000
son2 = bas2 + isl2 + yat2 + fin2 + kur
q(f"İşletme faaliyetlerinden {tr(isl2)} TL giriş, yatırımdan {tr(abs(yat2))} TL çıkış, finansmandan {tr(fin2)} TL giriş olmuştur. Dönem başı nakit {tr(bas2)} TL ve yabancı para nakit üzerindeki kur etkisi {tr(kur)} TL artıştır. Dönem sonu nakit kaç TL'dir?",
  f"{tr(son2)} TL",
  [f"{tr(bas2 + isl2 + yat2 + fin2)} TL", f"{tr(bas2 + isl2 + yat2 + fin2 - kur)} TL", f"{tr(isl2 + yat2 + fin2)} TL", f"{tr(bas2 + kur)} TL"],
  f"Kur etkisi nakit akışı değildir; ancak dönem başı ve sonu nakdi uzlaştırmak için ayrı sunulur: {tr(bas2)} + {tr(isl2)} − {tr(abs(yat2))} + {tr(fin2)} + {tr(kur)} = {tr(son2)} TL.",
  "TMS 7 - kur etkisiyle uzlaştırma")

q("Aşağıdakilerden hangileri TMS 7'ye göre işletme faaliyeti sayılır?\n\nI. Mal satışından tahsilat\n\nII. Satıcılara yapılan ödemeler\n\nIII. Pay ihracından sağlanan nakit",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Mal satışından tahsilat (I) ve satıcılara ödemeler (II) esas gelir getirici faaliyetlerdendir, işletme faaliyetidir. Pay ihracı (III) ise özkaynak yapısını değiştirdiğinden finansman faaliyetidir.",
  "TMS 7 - faaliyet sınıflandırması")

print("TOPLAM:", len(Q))

# ══ BUILD ═════════════════════════════════════════════════════════════════
def gen_letters(n, seed):
    r = random.Random(seed)
    base = ["ABCDE"[i % 5] for i in range(n)]
    while True:
        r.shuffle(base)
        if all(not (base[i] == base[i-1] == base[i-2]) for i in range(2, len(base))):
            return base

if __name__ == "__main__":
    assert len(Q) == 60, f"60 olmalı, şu an {len(Q)}"
    letters = gen_letters(len(Q), SEED)
    out = []
    for i, it in enumerate(Q):
        ans = letters[i]
        opts = {ans: it["correct"]}
        for k, d in zip([k for k in "ABCDE" if k != ans], it["distractors"]):
            opts[k] = d
        assert len(set(opts.values())) == 5, f"{PREFIX}-{i+1}: şık tekrarı"
        out.append({
            "id": f"{PREFIX}-{i+1:04d}", "ders": DERS, "konu": KONU,
            "stem": it["stem"], "options": opts, "answer": ans,
            "solution": it["why"] + f" Doğru cevap {ans}.",
            "source": {"kind": "generated",
                       "styleRef": "SGS Muhasebe Standartları (TMS 7; yapısal)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    hepsi = sum(1 for x in onc if x["options"][x["answer"]].strip() == "I, II ve III")
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} hepsi {hepsi} | harf {''.join(x['answer'] for x in out)[:40]}…")
