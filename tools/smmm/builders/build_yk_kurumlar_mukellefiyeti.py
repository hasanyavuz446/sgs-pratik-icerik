# -*- coding: utf-8 -*-
"""Vergi · Kurumlar Vergisi · Kurumlar Mükellefiyeti — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında mükellefiyet; kimlerin kurumlar vergisi mükellefi olduğu, tam/dar mükellefiyet,
tasfiye beyannamesi süresi ve sermaye azaltımı gibi olay ve süre soruları üzerinden sorulmuştur.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 5520 sayılı KVK md. 1-4, 14, 15, 17-27, 30.
Cumhurbaşkanı kararıyla değişebilen kesinti oranları soru kökünde verilir; hesaplar vergi_ortak.py ile yapılır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

P = Paket("questions_topic_kurumlar_mukellefiyeti_2026.json", lesson="kurumlar_vergisi", topic="kurumlar_mukellefiyeti",
          konu_adi="Kurumlar Mükellefiyeti", seed=2026092904,
          surum="5520 sayılı KVK güncel metni; kesinti oranları kökte; 29.09.2026 kontrolü")

K = "5520 sayılı Kurumlar Vergisi Kanunu’na göre"
K26 = "5520 sayılı Kurumlar Vergisi Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"

t1 = (3_000_000 + 3_500_000) - (5_000_000 + 200_000 + 100_000)
P.sayisal("KVK md. 17/4",
    "Tasfiye hâlindeki (LMN) A.Ş.’nin tasfiye dönemi başındaki servet değeri 5.000.000 ₺, dönem sonundaki servet değeri "
    "3.000.000 ₺’dir. Tasfiye sırasında ortaklara avans olarak 3.500.000 ₺ ödenmiş; ortaklar sermayeye ilave olarak "
    "200.000 ₺ ödeme yapmış; tasfiye sırasında vergiden istisna 100.000 ₺ kazanç elde edilmiştir. Tasfiye dönemi 2025 "
    f"takvim yılı içinde başlayıp bitmiştir.\n\n{K}, (LMN) A.Ş.’nin tasfiye kârı kaç ₺’dir?",
    tl(t1), secenekler(t1, 3_500_000 - 2_000_000, 1_500_000 - 100_000, 1_500_000 - 200_000, 1_500_000 + 300_000),
    "Md. 17/4'e göre tasfiye kârı, dönem sonu ve dönem başı servet değerleri arasındaki olumlu farktır; ortaklara yapılan "
    "ödemeler dönem sonu servetine, ortakların ilave ödemeleri ile istisna kazançlar dönem başı servetine eklenir: "
    "(3.000.000 + 3.500.000) − (5.000.000 + 200.000 + 100.000) = 1.200.000 ₺.", zorluk="hard")

P.q("KVK md. 1-2",
    "Bir vergi dairesi müdürlüğü, bölgesinde yeni faaliyete başlayan kuruluşların hangi vergi türünden mükellefiyet kaydı "
    "açılacağını belirlemektedir. Kuruluşlar arasında şirketler, kooperatifler, kamu işletmeleri ve ortaklıklar "
    f"bulunmaktadır.\n\n{K}, aşağıdakilerden hangisi kurumlar vergisi mükellefi değildir?",
    "Ortakları gerçek kişi olan adi ortaklık",
    ["Sermaye Piyasası Kurulunun düzenleme ve denetimine tabi yatırım fonu",
     "Belediyeye ait ve faaliyeti devamlı bulunan ticari işletme",
     "Kooperatifler Kanunu’na göre kurulan tarımsal kalkınma kooperatifi",
     "Sermayesi paylara bölünmüş komandit şirket"],
    "Md. 1'e göre sermaye şirketleri, kooperatifler, iktisadi kamu kuruluşları, dernek ve vakıflara ait iktisadi işletmeler "
    "ile iş ortaklıkları kurumlar vergisi mükellefidir; md. 2'ye göre SPK denetimindeki fonlar sermaye şirketi sayılır. Adi "
    "ortaklıkta ortaklar kendi paylarına düşen kazanç için gelir vergisi mükellefidir.", zorluk="easy")

P.q("KVK md. 2/5",
    "Bir işçi sendikası, üyelerine indirimli fiyatla hizmet vermek amacıyla devamlı olarak faaliyet gösteren bir otel "
    "işletmektedir. Ayrıca bir cemaat, mülkiyetindeki işyerlerini devamlı olarak kiraya veren bir işletme kurmuştur."
    f"\n\n{K}, bu işletmelerin durumuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sendika dernek, cemaat vakıf sayıldığından işletmeleri iktisadi işletme olarak mükelleftir.",
    ["Sendikalar ve cemaatler kurumlar vergisinin kapsamı dışında olduğundan işletmeleri mükellef değildir.",
     "Sadece cemaatin işletmesi mükelleftir; sendikaların işletmeleri muaftır.",
     "Mal ve hizmet bedeli maliyeti karşıladığı için işletmeler iktisadi nitelik taşımaz.",
     "İşletmelerin tüzel kişiliği olmadığından ancak gerçek kişi olarak gelir vergisine tabi olurlar."],
    "Md. 2/5'e göre Kanunun uygulanmasında sendikalar dernek, cemaatler vakıf sayılır; bunlara ait devamlı ticari "
    "işletmeler iktisadi işletmedir. Md. 2/6'ya göre tüzel kişiliğin olmaması veya bedelin maliyeti karşılayacak kadar olması "
    "mükellefiyeti etkilemez.", zorluk="hard")

t2 = 2_400_000 * 0.25
P.sayisal("KVK md. 17/4, 32",
    "Tasfiye hâlindeki (OPR) Ltd. Şti.’nin 2025 yılında başlayıp aynı yıl sona eren tasfiye döneminde dönem başı servet "
    "değeri 4.000.000 ₺, dönem sonu servet değeri 1.000.000 ₺’dir. Tasfiye sırasında ortaklara dağıtılan değerler toplamı "
    f"5.400.000 ₺’dir; başka düzeltme yoktur ve genel oran uygulanacaktır.\n\n{K}, tasfiye kârı üzerinden hesaplanacak "
    "kurumlar vergisi kaç ₺’dir?",
    tl(t2), secenekler(t2, 5_400_000 * 0.25, 3_000_000 * 0.25, 1_400_000 * 0.25, 2_400_000 * 0.20),
    "Tasfiye kârı: (1.000.000 + 5.400.000) − 4.000.000 = 2.400.000 ₺. Kurumlar vergisi: 2.400.000 × %25 = 600.000 ₺.")

P.q("KVK md. 2/6",
    f"{K}, iktisadi kamu kuruluşları ile dernek ve vakıf iktisadi işletmelerinin mükellefiyetine ilişkin aşağıdaki "
    "ifadelerden hangisi yanlıştır?",
    "Kârın kuruluş amaçlarına tahsis edilmesi bunların iktisadi niteliğini ortadan kaldırır.",
    ["Kazanç amacı gütmemeleri mükellefiyetlerini etkilemez.",
     "Tüzel kişiliklerinin olmaması mükellefiyetlerini etkilemez.",
     "Bağımsız muhasebelerinin bulunmaması mükellefiyetlerini etkilemez.",
     "Faaliyetlerinin kanunla verilmiş görevler arasında bulunması mükellefiyetlerini etkilemez."],
    "Md. 2/6'ya göre kazanç amacı gütmemeleri, faaliyetlerinin kanunla verilmiş görevler arasında olması, tüzel "
    "kişiliklerinin, bağımsız muhasebelerinin ve ayrılmış sermayelerinin bulunmaması mükellefiyeti etkilemez; bedelin "
    "maliyeti karşılayacak kadar olması, kâr edilmemesi veya kârın kuruluş amaçlarına tahsisi iktisadi niteliği değiştirmez.")

P.q("KVK md. 2/7",
    "(ABC) A.Ş. ile mühendis Bay (K), bir köprü inşaatını birlikte üstlenmek ve kazancını paylaşmak amacıyla ortaklık "
    f"kurmuşlardır. Ortaklığın tüzel kişiliği yoktur.\n\n{K}, bu ortaklığın kurumlar vergisi mükellefiyetine ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Mükellefiyet tesisini talep ederse iş ortaklığı olarak mükellef olur.",
    ["Tüzel kişiliği olmadığından kurumlar vergisi mükellefi olamaz.",
     "Ortaklardan biri gerçek kişi olduğundan ortaklık gelir vergisi mükellefi olur.",
     "Kurumlar vergisi mükellefiyeti talep aranmaksızın resen doğar.",
     "Ortaklık sadece inşaat bitince tasfiye kârı üzerinden vergilendirilir."],
    "Md. 2/7'ye göre kurumların kendi aralarında veya şahıs ortaklıkları ya da gerçek kişilerle belli bir işi birlikte "
    "yapmak ve kazancını paylaşmak amacıyla kurdukları ortaklıklardan bu şekilde mükellefiyet tesis edilmesini talep edenler "
    "iş ortaklığıdır; tüzel kişiliklerinin olmaması mükellefiyeti etkilemez.")

P.sayisal("KVK md. 17/1-a",
    "(STU) A.Ş.’nin tasfiyeye girmesine ilişkin genel kurul kararı 15 Ekim 2024’te tescil edilmiş, tasfiyenin sona erdiğine "
    f"ilişkin karar 10 Mart 2026’da tescil edilmiştir.\n\n{K}, (STU) A.Ş. için kaç bağımsız tasfiye dönemi oluşur?",
    "3", ["1", "2", "4", "5"],
    "Md. 17/1-a'ya göre başlangıçtan aynı takvim yılı sonuna kadar olan dönem (15.10-31.12.2024), sonraki her takvim yılı "
    "(2025) ve tasfiyenin sona erdiği yıl başından bitiş tarihine kadar olan dönem (01.01-10.03.2026) ayrı tasfiye "
    "dönemidir: 3 dönem.")

P.q("KVK md. 2/3-4",
    f"{K}, iktisadi kamu kuruluşlarına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yabancı devletlere ait ticari işletmeler iktisadi kamu kuruluşu gibi değerlendirilir.",
    ["Belediyelere ait işletmeler faaliyetleri devamlı olsa da iktisadi kamu kuruluşu sayılmaz.",
     "Sermaye şirketi şeklinde kurulan kamu işletmeleri iktisadi kamu kuruluşu olarak vergilendirilir.",
     "Sadece Devlete ait işletmeler iktisadi kamu kuruluşu sayılır.",
     "Faaliyeti devamlı olmayan kamu işletmeleri de iktisadi kamu kuruluşu sayılır."],
    "Md. 2/3'e göre Devlete, il özel idarelerine, belediyelere ve diğer kamu idarelerine ait, faaliyeti devamlı olan ve "
    "sermaye şirketi ya da kooperatif dışında kalan ticari, sınai ve zirai işletmeler iktisadi kamu kuruluşudur; md. 2/4'e "
    "göre yabancı devletlere ait bu nitelikteki işletmeler de iktisadi kamu kuruluşu gibi değerlendirilir.")

P.q("KVK md. 3",
    "(DEF) Ltd., kanuni merkezi Hollanda’da olan bir şirkettir. Ancak şirketin yönetim kurulu toplantıları İstanbul’da "
    "yapılmakta, işlemleri fiilen İstanbul’daki ofisten yönetilmektedir."
    f"\n\n{K}, (DEF) Ltd.’nin mükellefiyetine ilişkin aşağıdakilerden hangisi doğrudur?",
    "İş merkezi Türkiye’de olduğundan tam mükelleftir.",
    ["Kanuni merkezi yurt dışında olduğundan dar mükelleftir.",
     "Kanuni ve iş merkezinin ikisi de Türkiye’de olmadığından muaftır.",
     "Hem Türkiye’de hem Hollanda’da dar mükellef olarak vergilendirilir.",
     "Sadece Türkiye’deki ofisinin kazancı için tam mükelleftir."],
    "Md. 3/1'e göre kanuni veya iş merkezi Türkiye'de bulunan kurumlar tam mükelleftir; md. 3/6'ya göre iş merkezi, iş "
    "bakımından işlemlerin fiilen toplandığı ve yönetildiği merkezdir. Dar mükellefiyet için ikisinin de Türkiye dışında "
    "olması gerekir.", zorluk="hard")

t3 = 1_000_000 * 0.25 - (1_000_000 - 400_000) * 0.25
P.sayisal("KVK md. 17/1-c",
    "(VYZ) A.Ş.’nin 2024 yılında başlayan tasfiyesi 2025 yılında sona ermiştir. Birinci tasfiye döneminde 1.000.000 ₺ tasfiye "
    "kârı beyan edilip %25 oranında vergi ödenmiş, son tasfiye dönemi ise 400.000 ₺ zararla kapanmıştır."
    f"\n\n{K}, (VYZ) A.Ş.’ye iade edilecek kurumlar vergisi kaç ₺’dir?",
    tl(t3), secenekler(t3, 250_000, 400_000, 150_000, 400_000 * 0.20),
    "Md. 17/1-c'ye göre tasfiyenin zararla kapanması hâlinde tasfiye sonucu önceki tasfiye dönemlerine doğru düzeltilir ve "
    "fazla ödenen vergi iade edilir. Düzeltilmiş kâr 600.000 ₺, vergi 150.000 ₺; ödenen 250.000 ₺ ile arasındaki 100.000 ₺ "
    "iade edilir.", zorluk="hard")

P.q("KVK md. 3/3",
    "Kanuni ve iş merkezi Almanya’da bulunan (GHI) GmbH, Türkiye’de işyeri açmıştır. Şirket Türkiye’deki işyeri aracılığıyla "
    "satın aldığı halıları Türkiye’de satmaksızın doğrudan Almanya’ya göndermektedir; ayrıca işyeri aracılığıyla Türkiye’de "
    f"yerli müşterilere mobilya satmaktadır.\n\n{K}, bu kazançların vergilendirilmesine ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Mobilya satışı kazancı Türkiye’de elde edilmiş sayılır; halı ihracatı kazancı sayılmaz.",
    ["Her iki kazanç da işyeri vasıtasıyla elde edildiğinden Türkiye’de vergilendirilir.",
     "Dar mükellef olduğundan kazançları Türkiye’de vergi dışıdır.",
     "Halı ihracatından doğan kazanç Türkiye’de, mobilya satış kazancı Almanya’da vergilendirilir.",
     "Kazançların tamamı tam mükellef gibi dünya geliri esasına göre vergilendirilir."],
    "Md. 3/3-a'ya göre işyeri veya daimi temsilci vasıtasıyla yapılan işlerden elde edilen ticari kazançlar Türkiye'de elde "
    "edilmiş sayılır; ancak ihraç edilmek üzere Türkiye'de satın alınan malların Türkiye'de satılmaksızın yabancı ülkelere "
    "gönderilmesinden doğan kazançlar Türkiye'de elde edilmiş sayılmaz.", zorluk="hard")

P.q("KVK md. 3/5-6",
    f"{K}, kanuni merkez ve iş merkezine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İş merkezi, kurumun ana sözleşmesinde gösterilen merkezdir.",
    ["Kanuni merkez, kuruluş kanunu, tüzük, ana statü veya sözleşmede gösterilen merkezdir.",
     "İş merkezi, iş bakımından işlemlerin fiilen toplandığı ve yönetildiği merkezdir.",
     "Kanuni veya iş merkezinden biri Türkiye’de olan kurum tam mükelleftir.",
     "Kanuni ve iş merkezinin her ikisi de Türkiye dışında olan kurum dar mükelleftir."],
    "Md. 3/5'e göre kanuni merkez kuruluş kanunu, tüzük, ana statü veya sözleşmede gösterilen merkezdir; md. 3/6'ya göre iş "
    "merkezi işlemlerin fiilen toplandığı ve yönetildiği merkezdir. Ana sözleşmedeki merkez kanuni merkezi ifade eder.",
    zorluk="easy")

bk = 9_000_000 - 6_000_000
P.sayisal("KVK md. 18",
    "(ABC) A.Ş., devir şartlarını taşımayan bir birleşme sonucunda (DEF) A.Ş. bünyesinde infisah etmiştir. Birleşme "
    "döneminin başında (ABC) A.Ş.’nin servet değeri 6.000.000 ₺’dir. (DEF) A.Ş. tarafından (ABC) A.Ş. ortaklarına "
    f"verilen değerlerin VUK’a göre değeri 9.000.000 ₺’dir; başka düzeltme yoktur.\n\n{K}, (ABC) A.Ş.’nin birleşme kârı "
    "kaç ₺’dir?",
    tl(bk), secenekler(bk, 9_000_000, 6_000_000, 15_000_000, 1_500_000),
    "Md. 18'e göre birleşme tasfiye hükmündedir ve birleşme kârı tasfiye kârı esaslarına göre bulunur; birleşilen kurumca "
    "ortaklara verilen değerler tasfiyede dağıtılan değerlerin yerine geçer: 9.000.000 − 6.000.000 = 3.000.000 ₺.")

P.q("KVK md. 3/3",
    f"{K}, dar mükellefiyette kurum kazancını oluşturan kazanç ve iratlar arasında aşağıdakilerden hangisi yer almaz?",
    "Yurt dışındaki bir gayrimenkulün yurt dışında kiralanmasından doğan irat",
    ["Türkiye’deki işyeri aracılığıyla elde edilen ticari kazanç",
     "Türkiye’de bulunan zirai işletmeden elde edilen kazanç",
     "Türkiye’de elde edilen serbest meslek kazancı",
     "Taşınmazların Türkiye’de kiralanmasından elde edilen irat"],
    "Md. 3/3'e göre dar mükellefiyette kurum kazancı, Türkiye'deki işyeri veya daimi temsilci vasıtasıyla elde edilen ticari "
    "kazanç, Türkiye'deki zirai işletme kazancı, Türkiye'de elde edilen serbest meslek kazancı, mal ve hakların Türkiye'de "
    "kiralanmasından doğan iratlar, menkul sermaye iratları ve diğer kazançlardan oluşur.")

P.q("KVK md. 4",
    "Bir belediye; kanal ve boru yoluyla su dağıtan bir işletme, belediye sınırları içinde yolcu taşıyan bir otobüs "
    "işletmesi, kesim ve muhafaza işleriyle sınırlı bir mezbaha ve halka açık bir düğün salonu işletmektedir."
    f"\n\n{K}, bu işletmelerden hangisi kurumlar vergisinden muaf değildir?",
    "Halka açık düğün salonu",
    ["Kanal ve boru yoluyla dağıtım yapan su işletmesi",
     "Belediye sınırları içindeki yolcu taşıma işletmesi",
     "Kesim, taşıma ve muhafaza işleriyle sınırlı mezbaha",
     "Bu işletmelerin hepsi muaftır"],
    "Md. 4/1-ı'ya göre il özel idareleri, belediyeler ve köyler tarafından işletilen su işletmeleri, belediye sınırları "
    "içindeki yolcu taşıma işletmeleri ve kesim, taşıma ve muhafaza işleriyle sınırlı mezbahalar muaftır. Düğün salonu bu "
    "sayılanlar arasında değildir; iktisadi kamu kuruluşu olarak mükelleftir.")

yu = 20_000_000 * 0.15 * 0.25
P.sayisal("KVK md. 23",
    "Kanuni ve iş merkezi Yunanistan’da olan bir deniz taşımacılığı şirketinin, Türkiye’deki limanlardan yabancı limanlara "
    "yaptığı taşımalardan 2025 yılında Türkiye’de elde edilmiş sayılan hasılatı 20.000.000 ₺’dir. Kurumlar vergisi oranı "
    f"%25 olarak alınacaktır.\n\n{K}, bu şirketin 2025 yılı için hesaplanacak kurumlar vergisi kaç ₺’dir?",
    tl(yu), secenekler(yu, 20_000_000 * 0.12 * 0.25, 20_000_000 * 0.25, 20_000_000 * 0.15, 20_000_000 * 0.05 * 0.25),
    "Md. 23'e göre yabancı ulaştırma kurumlarının kazancı hasılata ortalama emsal oranı uygulanarak bulunur; deniz "
    "taşımacılığında oran %15'tir: 20.000.000 × %15 = 3.000.000 ₺ kazanç; 3.000.000 × %25 = 750.000 ₺.")

P.q("KVK md. 4/1-k",
    f"{K}, kooperatiflerin kurumlar vergisi muafiyetine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tüketim ve taşımacılık kooperatifleri de şartlara uyarsa muaftır.",
    ["Ana sözleşmede sermaye üzerinden kazanç dağıtılmaması hükmü bulunmalıdır.",
     "Yönetim kurulu başkan ve üyelerine kazanç üzerinden pay verilmemesi gerekir.",
     "Yedek akçelerin ortaklara dağıtılmaması gerekir.",
     "Kooperatiflerin ortak dışı işlemleri nedeniyle ayrı bir iktisadi işletme oluşmuş kabul edilir."],
    "Md. 4/1-k'ye göre tüketim ve taşımacılık kooperatifleri hariç olmak üzere, ana sözleşmesinde sermaye üzerinden kazanç "
    "dağıtılmaması, yöneticilere kazançtan pay verilmemesi, yedek akçelerin dağıtılmaması ve sadece ortaklarla iş görülmesi "
    "hükümleri bulunan ve bunlara fiilen uyan kooperatifler muaftır.", zorluk="hard")

P.q("KVK md. 4",
    f"{K}, aşağıdakilerden hangisi kurumlar vergisinden muaf kurumlar arasında yer almaz?",
    "Kamuya ait olup sermaye şirketi şeklinde kurulan otel işletmesi",
    ["Kanunla kurulan emekli ve yardım sandıkları",
     "Yaptıkları iş karşılığında resim ve harç alan kamu kuruluşları",
     "Sadece idman ve spor faaliyetlerinde bulunan anonim şirketler",
     "Münhasıran bilimsel araştırma ve geliştirme faaliyetinde bulunan kuruluşlar"],
    "Md. 4'e göre kanunla kurulan emekli ve yardım sandıkları, resim ve harç alan kamu kuruluşları, sadece idman ve spor "
    "faaliyetlerinde bulunan anonim şirketler ve münhasıran Ar-Ge faaliyetinde bulunan kuruluşlar muaftır. Kamuya ait olsa "
    "da sermaye şirketi şeklinde kurulan otel işletmesi sermaye şirketi olarak mükelleftir.", zorluk="hard")

yk = 8_000_000 * 0.12
P.sayisal("KVK md. 23",
    "Kanuni ve iş merkezi Bulgaristan’da olan bir kara taşımacılığı şirketinin 2025 yılında Türkiye sınırları içinde yaptığı "
    f"taşımalardan elde ettiği hasılat 8.000.000 ₺’dir.\n\n{K}, bu şirketin 2025 yılı kurumlar vergisi matrahı kaç ₺’dir?",
    tl(yk), secenekler(yk, 8_000_000 * 0.15, 8_000_000 * 0.05, 8_000_000 * 0.25, 8_000_000 * 0.10),
    "Md. 23/2'ye göre ortalama emsal oranı kara taşımacılığında %12'dir: 8.000.000 × %12 = 960.000 ₺.")

P.q("KVK md. 4/1-b",
    "Sağlık Bakanlığına bağlı bir devlet hastanesi, teşhis ve tedaviye yönelik olarak başka bir kamu hastanesine laboratuvar "
    "hizmeti satmakta ve binasının bir bölümünü kafeterya olarak kiraya vermektedir."
    f"\n\n{K}, bu hastanenin muafiyetine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Bu işlemler hastanenin muafiyetini ortadan kaldırmaz.",
    ["Laboratuvar hizmeti satışı muafiyeti ortadan kaldırır.",
     "Kafeterya kiralaması nedeniyle hastanenin tamamı mükellef olur.",
     "Kamu hastaneleri muafiyetten yararlanmaz.",
     "Her iki işlem de hastaneyi kurumlar vergisi mükellefi yapar."],
    "Md. 4/1-b'ye göre kamu idare ve kuruluşlarınca işletilen hastaneler muaftır; sağlık hizmeti sunanların teşhis ve tedaviye "
    "yönelik birbirlerine yapacakları mal ve hizmet satışları ile Sağlık Bakanlığına bağlı hastanelerin GVK md. 70'teki mal ve "
    "hakları kiralaması bu muafiyeti ortadan kaldırmaz.")

P.q("KVK md. 14",
    "Merkezi Ankara’da bulunan (JKL) A.Ş.’nin İzmir ve Bursa’da bağımsız muhasebesi ve ayrılmış sermayesi bulunan iki şubesi "
    f"vardır.\n\n{K}, (JKL) A.Ş.’nin kurumlar vergisi beyanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Şubeler için ayrı beyanname verilmez; kazancın tamamı için tek beyanname verilir.",
    ["Bağımsız muhasebesi olan her şube için ayrı beyanname verilir.",
     "Şubeler bağlı oldukları vergi dairelerine ayrı ayrı beyanname verir.",
     "Merkez ve şubeler için ortak beyanname verilir, ancak şubeler ayrıca muhtasar beyan verir.",
     "Ayrılmış sermayesi olan şubeler ayrı kurum sayılır."],
    "Md. 14/2 ve 14/4'e göre her mükellef vergiye tabi kazancının tamamı için bir beyanname verir; şubeler, ajanslar ve diğer "
    "işyerleri için bağımsız muhasebeleri ve ayrılmış sermayeleri olsa dahi ayrı beyanname verilmez.", zorluk="easy")

yh = 30_000_000 * 0.05 * 0.25
P.sayisal("KVK md. 23",
    "Kanuni ve iş merkezi Katar’da olan bir havayolu şirketinin 2025 yılında Türkiye’deki havalimanlarından yurt dışına "
    "yaptığı taşımalardan Türkiye’de elde edilmiş sayılan hasılatı 30.000.000 ₺’dir. Kurumlar vergisi oranı %25 olarak "
    f"alınacaktır.\n\n{K}, bu şirketin 2025 yılı için hesaplanacak kurumlar vergisi kaç ₺’dir?",
    tl(yh), secenekler(yh, 30_000_000 * 0.15 * 0.25, 30_000_000 * 0.12 * 0.25, 30_000_000 * 0.05, 30_000_000 * 0.10 * 0.25),
    "Md. 23/2'ye göre hava taşımacılığında ortalama emsal oranı %5'tir: 30.000.000 × %5 = 1.500.000 ₺ kazanç; "
    "1.500.000 × %25 = 375.000 ₺.")

P.q("KVK md. 14/2",
    "Bir büyükşehir belediyesinin tüzel kişiliği bulunmayan üç ayrı iktisadi işletmesi (otopark, sosyal tesis ve kafeterya) "
    f"bulunmaktadır.\n\n{K}, bu işletmelerin beyanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Her biri için bağlı oldukları belediye tarafından ayrı beyanname verilir.",
    ["Üç işletmenin kazancı için belediye tarafından tek beyanname verilir.",
     "Tüzel kişilikleri olmadığından beyanname vermezler.",
     "Her işletmenin müdürü kendi adına gelir vergisi beyannamesi verir.",
     "Sadece kâr eden işletme için beyanname verilir."],
    "Md. 14/2'ye göre tüzel kişiliği bulunmayan iktisadi kamu kuruluşları ile dernek ve vakıflara ait iktisadi işletmelerden "
    "her biri için, bunların bağlı olduğu kamu tüzel kişileri ile dernek ve vakıflar tarafından ayrı beyanname verilir.")

P.q("KVK md. 14/3, 21",
    "(MNO) A.Ş.’ye Maliye Bakanlığınca 1 Temmuz – 30 Haziran özel hesap dönemi tayin edilmiştir. Şirket 1 Temmuz 2025 – "
    f"30 Haziran 2026 hesap dönemine ait kurumlar vergisi beyannamesini verecektir.\n\n{K}, bu beyannamenin verilmesi ve "
    "verginin ödenmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Beyanname 1-25 Ekim 2026 tarihleri arasında verilir, vergi Ekim 2026 sonuna kadar ödenir.",
    ["Beyanname 1-25 Nisan 2027 tarihleri arasında verilir, vergi Nisan 2027 sonuna kadar ödenir.",
     "Beyanname 1-30 Eylül 2026 tarihleri arasında verilir, vergi aynı ay sonuna kadar ödenir.",
     "Beyanname 1-25 Ekim 2026 tarihleri arasında verilir, vergi iki eşit taksitte ödenir.",
     "Beyanname Temmuz 2026 içinde verilir, vergi Ağustos 2026 sonuna kadar ödenir."],
    "Md. 14/3'e göre beyanname hesap döneminin kapandığı ayı izleyen dördüncü ayın birinci gününden yirmibeşinci günü "
    "akşamına kadar verilir: dönem Haziran'da kapandığından Ekim 1-25. Md. 21/1'e göre vergi beyannamenin verildiği ayın "
    "sonuna kadar ödenir.", zorluk="hard")

sb = (10_000_000 - 10_000_000 * 0.25) * 0.15
P.sayisal("KVK md. 30/6",
    "Kanuni ve iş merkezi Fransa’da olan (GHI) SA’nın Türkiye şubesinin 2025 yılı indirim ve istisnalar düşülmeden önceki "
    "kurum kazancı 10.000.000 ₺, hesaplanan kurumlar vergisi 2.500.000 ₺’dir. Şube, vergi sonrası kazancın tamamını ana "
    f"merkeze aktarmıştır. Çifte vergilendirmeyi önleme anlaşması hükümleri dikkate alınmayacaktır.\n\n{K}, ana merkeze "
    "aktarılan tutar üzerinden yapılacak kurumlar vergisi kesintisi kaç ₺’dir?",
    tl(sb), secenekler(sb, 10_000_000 * 0.15, 2_500_000 * 0.15, 7_500_000 * 0.10, 7_500_000 * 0.25),
    "Md. 30/6'ya göre yıllık beyanname veren dar mükellef kurumların, indirim ve istisnalar öncesi kazançtan hesaplanan "
    "kurumlar vergisi düşüldükten sonra ana merkeze aktardıkları tutar üzerinden %15 kesinti yapılır: 7.500.000 × %15 = "
    "1.125.000 ₺.", zorluk="hard")

P.q("KVK md. 14/5",
    "(PRS) Konut Yapı Kooperatifi’nin 2025 yılındaki tek geliri, kurumlar vergisi mükellefi olan bir şirkete kiraladığı ve "
    f"kiracı tarafından vergi kesintisi yapılan dükkân kira gelirinden ibarettir.\n\n{K}, kooperatifin beyan "
    "yükümlülüğüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "Gelirleri kesintiye tabi taşınmaz kira gelirinden ibaret olduğundan beyanname vermez.",
    ["Kira gelirinin tamamı için kurumlar vergisi beyannamesi vermek yükümlüdür.",
     "Kira geliri için gelir vergisi beyannamesi verir.",
     "Kesinti yapılmış olsa da kira gelirini geçici vergi beyannamesiyle bildirir.",
     "Kooperatif muaf olduğundan kiracı kesinti yapamaz."],
    "Md. 14/5'e göre kooperatiflerin gelirlerinin vergi kesintisine tabi tutulan taşınmaz kira gelirlerinden ibaret olması "
    "halinde bu gelirler için beyanname verilmez; md. 15/1-b kooperatiflere yapılan kira ödemelerinden kesinti öngörür.")

P.q("KVK md. 17",
    f"{K}, tasfiye hâlindeki kurumların vergilendirilmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tasfiye, tasfiye kararının alındığı genel kurul toplantısı tarihinde başlar.",
    ["Tasfiye hâlindeki kurumlarda hesap dönemi yerine tasfiye dönemi geçerli olur.",
     "Tasfiyenin zararla kapanması hâlinde sonuç önceki tasfiye dönemlerine doğru düzeltilir.",
     "Bir yıldan fazla süren tasfiyelerde tarh zamanaşımı tasfiyenin sona erdiği dönemi izleyen yıldan başlar.",
     "Tasfiye hâlindeki kurumların vergi matrahı tasfiye kârıdır."],
    "Md. 17/1-a'ya göre tasfiye, kurumun tasfiyeye girmesine ilişkin genel kurul kararının tescil edildiği tarihte başlar ve "
    "tasfiye kararının tescil edildiği tarihte sona erer. Diğer ifadeler md. 17'ye uygundur.", zorluk="hard")

kk = 425_000 / 0.85 * 0.15
P.sayisal("KVK md. 15/1-b, 15/7",
    "(JKL) A.Ş., bir yapı kooperatifinden kiraladığı dükkân için 2025 yılında kooperatife net 425.000 ₺ kira ödemiş ve "
    "kesilmesi gereken vergiyi kendisi üstlenmiştir. (Uygulanacak kesinti oranı %15 olarak alınacaktır.)"
    f"\n\n{K}, (JKL) A.Ş.’nin yapması gereken vergi kesintisi kaç ₺’dir?",
    tl(kk), secenekler(kk, 425_000 * 0.15, 425_000 * 0.20, 500_000, 425_000 * 0.85 * 0.15),
    "Md. 15/7'ye göre kesilmesi gereken verginin ödemeyi yapan tarafından üstlenilmesi hâlinde kesinti, ödenen tutar ile "
    "üstlenilen verginin toplamı üzerinden hesaplanır: brüt kira 425.000 / 0,85 = 500.000 ₺; kesinti 500.000 × %15 = "
    "75.000 ₺.", zorluk="hard")

P.q("KVK md. 17/1-d",
    "(TUV) A.Ş. 2025 yılı Mart ayında tasfiyeye girmiş ve bu karar tescil edilmiştir. Tasfiye sürerken 2026 yılı Mayıs ayında "
    f"genel kurul tasfiyeden vazgeçme kararı almıştır.\n\n{K}, bu duruma ilişkin aşağıdakilerden hangisi doğrudur?",
    "Vazgeçmeye kadar verilen tasfiye beyannameleri normal beyanname yerine geçer.",
    ["Vazgeçme kararı geçmişe yürüyerek tasfiyenin başladığı tarihten itibaren hüküm doğurur.",
     "Tasfiye dönemi beyannameleri iptal edilir, normal beyannameler yeniden verilir.",
     "Tasfiyeye giren kurum tasfiyeden vazgeçemez ve tasfiyeyi tamamlar.",
     "Geçici vergi yükümlülüğü vazgeçme kararını izleyen hesap döneminden itibaren başlar."],
    "Md. 17/1-d'ye göre tasfiyeden vazgeçme kararı, kararın alındığı dönemin başından itibaren geçerli olur; o tarihe kadar "
    "verilen tasfiye dönemi beyannameleri normal faaliyet beyannamelerinin yerine geçer. Geçici vergi yükümlülüğü kararın "
    "alındığı tarihi kapsayan geçici vergi dönemi başından itibaren başlar.", zorluk="hard")

P.q("KVK md. 17/2-3",
    f"{K}, tasfiye beyannamelerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tasfiye beyannameleri kurumun yönetim kurulu başkanı tarafından verilir.",
    ["Ara tasfiye dönemlerine ait beyannameler md. 14’teki sürelerde verilir.",
     "Beyannamelere bilanço ve gelir tablosu eklenir.",
     "Tasfiye bilançosuna göre ortaklara dağıtılan değerlerin ayrıntılı listesi beyannameye eklenir.",
     "Tasfiyenin sona erdiği döneme ait beyanname kurumun bağlı olduğu vergi dairesine verilir."],
    "Md. 17/2'ye göre tasfiye beyannameleri tasfiye memurları tarafından verilir; ara dönem beyannameleri md. 14'teki "
    "sürelerde, son dönem beyannamesi tasfiyenin sonuçlandığı tarihten itibaren belirli süre içinde verilir. Md. 17/3'e göre "
    "bilanço, gelir tablosu ve dağıtılan değerlerin listesi eklenir.")

mk = 2_000_000 * 0.15
P.sayisal("KVK md. 15/2",
    "Tam mükellef (MNO) A.Ş., 2025 yılında kurumlar vergisinden muaf bir vakfa 2.000.000 ₺ nakit kâr payı dağıtmış, ayrıca "
    "vakfın payına düşen 1.000.000 ₺ kârı sermayeye eklemiştir. (Uygulanacak kesinti oranı %15 olarak alınacaktır.)"
    f"\n\n{K}, (MNO) A.Ş.’nin bu işlemler nedeniyle yapacağı vergi kesintisi kaç ₺’dir?",
    tl(mk), secenekler(mk, 3_000_000 * 0.15, 0, 1_000_000 * 0.15, 2_000_000 * 0.10),
    "Md. 15/2'ye göre vergiden muaf kurumlara dağıtılan kâr payları üzerinden kesinti yapılır; kârın sermayeye eklenmesi kâr "
    "dağıtımı sayılmaz: 2.000.000 × %15 = 300.000 ₺.")

P.q("KVK md. 18-19",
    "Kanuni merkezi İstanbul’da olan (WXY) A.Ş., kanuni ve iş merkezi Fransa’da olan (ZAB) SA ile birleşmiş ve birleşme "
    f"sonucunda infisah etmiştir.\n\n{K}, bu birleşmenin vergilendirilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Birleşme devir sayılmaz; birleşme kârı vergilendirilir.",
    ["Birleşme şarta bağlı olmaksızın devir hükmündedir ve birleşme kârı hesaplanmaz.",
     "Münfesih kurum birleşmeden sonra tasfiye kârı üzerinden vergilendirilir.",
     "Birleşme işlemi vergilendirmeye konu olmaz; sadece ticaret siciline bildirilir.",
     "Birleşme kârının yarısı istisnadır."],
    "Md. 19/1-a'ya göre birleşmenin devir hükmünde olması için infisah eden ve birleşilen kurumun kanuni veya iş "
    "merkezlerinin Türkiye'de bulunması gerekir. Şart sağlanmadığından md. 18 uygulanır: birleşme tasfiye hükmündedir ve "
    "tasfiye kârı yerine birleşme kârı vergilendirilir.", zorluk="hard")

P.q("KVK md. 19-20",
    f"{K}, devir hükmündeki birleşmelerin sonuçlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Münfesih kurumun devir tarihine kadar elde ettiği kazançlar da vergilendirilmez.",
    ["Birleşmeden doğan kârlar hesaplanmaz ve vergilendirilmez.",
     "Devir tarihi, devir kararının ticaret sicilinde tescil edildiği tarihtir.",
     "Beyanname münfesih ve birleşilen kurumlarca müştereken imzalanır.",
     "Birleşilen kurum, münfesih kurumun vergi borçlarını ödeyeceğini taahhüt eder."],
    "Md. 20/1'e göre devirlerde münfesih kurumun sadece devir tarihine kadar elde ettiği kazançlar vergilendirilir; birleşmeden "
    "doğan kârlar hesaplanmaz. Devir tarihi tescil tarihidir, beyanname müştereken imzalanır ve birleşilen kurum taahhütname "
    "verir.")

dk = 4_000_000 * 0.15
P.sayisal("KVK md. 30/3",
    "Tam mükellef (PRS) A.Ş., Türkiye’de işyeri ve daimi temsilcisi bulunmayan dar mükellef ortağı (TUV) GmbH’ye 2025 "
    "yılında 4.000.000 ₺ nakit kâr payı dağıtmış, ayrıca ortağın payına düşen 1.500.000 ₺ kârı sermayeye eklemiştir. "
    f"(Uygulanacak kesinti oranı %15 olarak alınacaktır.)\n\n{K}, yapılacak kurumlar vergisi kesintisi kaç ₺’dir?",
    tl(dk), secenekler(dk, 5_500_000 * 0.15, 1_500_000 * 0.15, 4_000_000 * 0.10, 0),
    "Md. 30/3'e göre tam mükellef kurumlarca dar mükellef kurumlara dağıtılan kâr payları üzerinden kesinti yapılır; kârın "
    "sermayeye eklenmesi dağıtım sayılmaz: 4.000.000 × %15 = 600.000 ₺.")

P.q("KVK md. 19/2",
    "(CDE) Ltd. Şti., bilanço değerlerini aynen devralacak şekilde anonim şirkete dönüşmüştür. Her iki şirketin kanuni ve iş "
    f"merkezi Türkiye’dedir.\n\n{K}, bu tür değiştirmenin vergilendirilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tür değiştirme devir hükmünde olduğundan tasfiye kârı hesaplanmaz.",
    ["Tür değiştirme tasfiye hükmündedir ve tasfiye kârı vergilendirilir.",
     "Tür değiştirmede birleşme kârı hesaplanır.",
     "Limited şirket kapanış beyannamesi vermeden faaliyetini sona erdirir.",
     "Tür değiştirme ancak Maliye Bakanlığının izniyle devir sayılır."],
    "Md. 19/2'ye göre kurumların md. 19/1'deki şartlar dahilinde tür değiştirmeleri de devir hükmündedir; md. 20 uyarınca devir "
    "tarihine kadar elde edilen kazanç vergilendirilir, tasfiye veya birleşme kârı hesaplanmaz.")

P.q("KVK md. 19/3",
    f"{K26}, bölünme işlemlerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tam bölünmede devredilen şirket tasfiye edilerek sona erer.",
    ["Tam bölünmede bütün malvarlığı kayıtlı değerler üzerinden en az iki sermaye şirketine devredilir.",
     "Tam bölünmede verilecek iştirak hisselerinin itibari değerinin %10’una kadar nakit ödeme yapılabilir.",
     "Kısmi bölünmeye konu iştirak hisselerinin en az iki tam yıl elde tutulmuş olması gerekir.",
     "Tam bölünmede devralan şirketin hisseleri devredilen şirketin ortaklarına verilir."],
    "Md. 19/3-a'ya göre tam bölünmede tam mükellef sermaye şirketi tasfiyesiz olarak infisah eder ve bütün malvarlığını kayıtlı "
    "değerleri üzerinden iki veya daha fazla sermaye şirketine devreder; hisselerin itibari değerinin %10'una kadar nakit "
    "ödeme bölünmeye engel değildir.", zorluk="hard")

P.sayisal("KVK md. 20/1",
    "(WXY) A.Ş. ile (ZAB) A.Ş.’nin devir hükmündeki birleşmesi 2026 yılı Haziran ayında ticaret siciline tescil edilmiş ve "
    f"Ticaret Sicili Gazetesinde ilan edilmiştir.\n\n{K}, münfesih kuruma ait ve müştereken imzalanan kurumlar vergisi "
    "beyannamesi, birleşmenin ilanından itibaren en geç kaç gün içinde verilmelidir?",
    "30", ["15", "20", "45", "60"],
    "Md. 20/1-a'ya göre münfesih ve birleşilen kurum, devir tarihi itibarıyla hazırlayıp müştereken imzalayacakları "
    "beyannameyi birleşmenin Ticaret Sicili Gazetesinde ilan edildiği tarihten itibaren otuz gün içinde münfesih kurumun "
    "bağlı olduğu vergi dairesine verir.")

P.q("KVK md. 22/3",
    "Kanuni ve iş merkezi İtalya’da olan (FGH) SpA’nın Türkiye şubesi, 2025 yılında ana merkeze şube hesabına yaptığı "
    "alım-satımlar için komisyon ödemiş ve ana merkezin genel yönetim giderlerine katılma payı ayırmıştır."
    f"\n\n{K}, şubenin kazancının tespitine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ana merkeze alım-satımlar için verilen komisyonlar indirilemez.",
    ["Ana merkeze ödenen komisyonlar emsale uygun olduğu sürece indirilebilir.",
     "Ana merkezin genel yönetim giderlerine katılma payları sınırsız olarak indirilebilir.",
     "Dar mükellef şubelerin tüm giderleri tam mükelleflerden farklı olarak götürü tespit edilir.",
     "Şube kazancı ana merkezin kazancından bağımsız olarak İtalya’da tespit edilir."],
    "Md. 22/3'e göre dar mükellef kurumların bu kurumlar hesabına yaptıkları alım-satımlar için ana merkeze veya Türkiye "
    "dışındaki şubelere verilen faizler, komisyonlar ve benzerleri indirilemez; genel yönetim giderlerine katılma payları da "
    "emsallere uygun dağıtım anahtarlarıyla ayrılanlar dışında indirilemez.", zorluk="hard")

P.q("KVK md. 26-27",
    "Türkiye’de işyeri ve daimi temsilcisi bulunmayan dar mükellef (IJK) Ltd., Türkiye’de arızi olarak bir ticari işleme "
    f"aracılık ederek kazanç elde etmiştir.\n\n{K}, bu kazancın beyanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kazanç, faaliyetin yapıldığı yerin vergi dairesine özel beyanname ile bildirilir.",
    ["Kazanç yıllık kurumlar vergisi beyannamesiyle bildirilir.",
     "Kazanç, yabancı kurumun merkezinin bulunduğu ülkede beyan edilir.",
     "Kazanç, ödemeyi yapanın muhtasar beyannamesiyle bildirilir ve başka beyan gerekmez.",
     "Kazanç, İstanbul’daki büyük mükellefler vergi dairesine yıllık beyanla bildirilir."],
    "Md. 26'ya göre dar mükellef kurumların kazancı diğer kazanç ve iratlardan ibaretse elde edilme tarihinden itibaren "
    "belirli süre içinde özel beyanname ile bildirilir; md. 27/1-ç'ye göre arızi ticari işlem ve aracılık kazançlarında "
    "beyanname faaliyetin yapıldığı yerin vergi dairesine verilir.")

P.sayisal("KVK md. 26",
    "Türkiye’de işyeri ve daimi temsilcisi bulunmayan dar mükellef (CDE) BV, Türkiye’deki bir işletmenin faaliyetini "
    "durdurması karşılığında 12 Mart 2026’da tazminat almıştır. Bu kazanç diğer kazanç ve irat niteliğindedir."
    f"\n\n{K}, (CDE) BV bu kazancı elde edilme tarihinden itibaren en geç kaç gün içinde beyan etmelidir?",
    "15", ["7", "10", "20", "30"],
    "Md. 26/1'e göre dar mükellef yabancı kurumun vergiye tabi kazancı diğer kazanç ve iratlardan ibaretse, bu kazançlar "
    "elde edilme tarihinden itibaren on beş gün içinde md. 27'de belirtilen vergi dairesine beyanname ile bildirilir.")

P.q("KVK md. 25",
    f"{K}, dar mükellef kurumların vergilendirme dönemine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Özel beyannameyle bildirilen kazançlarda vergilendirme dönemi hesap dönemidir.",
    ["Yıllık beyan esasında vergilendirilenlerin vergilendirme dönemi hesap dönemidir.",
     "Özel hesap dönemi tayin edilenlerin vergilendirme dönemi özel hesap dönemleridir.",
     "Kesinti yoluyla vergilendirilen ve beyan edilmeyen kazançlarda kesintinin ilgili olduğu dönem vergilendirme dönemidir.",
     "Tarhiyat muhatabının Türkiye’yi terk etmesi hâlinde beyanname terkten önceki on beş gün içinde verilir."],
    "Md. 25/3'e göre md. 26 uyarınca özel beyanname ile bildirilen kazançların vergilendirilmesinde vergilendirme dönemi "
    "yerine kazancın elde edilme tarihi esas alınır. Diğer ifadeler md. 25'e uygundur.", zorluk="hard")

P.oncul("KVK md. 1-2",
    f"{K} aşağıdaki kuruluşlar değerlendirilmektedir:",
    ["Borsa yatırım fonu", "Kollektif şirket", "Yapı kooperatifi", "Adi komandit şirket"],
    "Yukarıdakilerden hangileri kurumlar vergisi mükellefi olabilir?",
    "I ve III",
    ["I ve II", "I ve III", "II ve IV", "I, II ve III", "II, III ve IV"],
    "Md. 2'ye göre SPK denetimine tabi fonlar sermaye şirketi sayılır (I) ve kooperatifler (III) mükelleftir; yapı "
    "kooperatifleri şartları sağlarsa md. 4/1-k ile muaf olabilir ama mükellef sayılan kurumlardandır. Kollektif ve adi "
    "komandit şirketler şahıs şirketidir; ortakları gelir vergisine tabidir.", zorluk="hard")

P.sayisal("KVK md. 19/3-b",
    "(FGH) A.Ş., bilançosunda yer alan iştirak hisselerini kısmi bölünme yoluyla yeni kurulacak bir sermaye şirketine "
    f"devretmeyi planlamaktadır.\n\n{K}, kısmi bölünmeye konu iştirak hisselerinin en az kaç tam yıl süreyle elde tutulmuş "
    "olması gerekir?",
    "2", ["1", "3", "4", "5"],
    "Md. 19/3-b'ye göre kısmi bölünmeye konu iştirak hisselerinin bilançoda en az iki tam yıl süreyle elde tutulması gerekir; "
    "üretim veya hizmet işletmelerinin kısmi bölünmesinde ise bölünen işletme bir bütün hâlinde devredilir.")

P.q("KVK md. 3, 5/1-b",
    "Kanuni merkezi Türkiye’de olan (IJK) A.Ş.’nin Azerbaycan’da şubesi vardır ve bu şube 2025 yılında kazanç elde etmiştir."
    f"\n\n{K}, şube kazancının Türkiye’de vergilendirilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tam mükellef olduğundan yurt dışı şube kazancı da kurum kazancına dahildir.",
    ["Dar mükellef olduğundan sadece Türkiye’deki kazancı vergilendirilir.",
     "Yurt dışı şube kazançları şarta bağlı olmaksızın Türkiye’de vergilendirilmez.",
     "Şube kazancı Azerbaycan’da vergilendirildiğinden Türkiye’de beyan edilmez.",
     "Şube ayrı bir kurum sayılır ve ayrı beyanname verir."],
    "Md. 3/1'e göre kanuni veya iş merkezi Türkiye'de bulunan kurumlar Türkiye içinde ve dışında elde ettikleri kazançların "
    "tamamı üzerinden vergilendirilir; yurt dışı şube kazançları md. 5/1-g'deki şartlar sağlanırsa istisna olabilir, ama "
    "kural olarak kurum kazancına dahildir.")

P.q("KVK md. 17/2",
    "(KLM) A.Ş.’nin tasfiyesi 20 Mayıs 2026’da sonuçlanmış ve tasfiye memuru son tasfiye dönemine ait beyannameyi "
    f"hazırlamaktadır.\n\n{K}, bu beyannamenin verilme süresine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tasfiyenin sonuçlandığı tarihten itibaren otuz gün içinde verilir.",
    ["Tasfiye dönemini izleyen yılın Nisan ayının 25. günü akşamına kadar verilir.",
     "Tasfiyenin sonuçlandığı ayı izleyen dördüncü ayın 1-25’i arasında verilir.",
     "Tasfiyenin sonuçlandığı tarihten itibaren on beş gün içinde verilir.",
     "Tasfiye kararının tescilinden itibaren doksan gün içinde verilir."],
    "Md. 17/2'ye göre ara tasfiye dönemi beyannameleri md. 14'teki sürelerde verilir; tasfiyenin sona erdiği döneme ilişkin "
    "beyanname ise tasfiyenin sonuçlandığı tarihten itibaren otuz gün içinde kurumun bağlı olduğu vergi dairesine verilir.",
    zorluk="easy")

di = 800_000 * 0.25
P.sayisal("KVK md. 1, 2/5, 32",
    "Bir derneğe ait ve devamlı faaliyet gösteren (Dernek Kafeteryası) iktisadi işletmesinin 2025 hesap dönemi kurum kazancı "
    "800.000 ₺’dir. İşletmenin tüzel kişiliği yoktur; kâr dernek amaçlarına harcanmaktadır. Genel oran uygulanacaktır."
    f"\n\n{K}, bu işletme için hesaplanacak kurumlar vergisi kaç ₺’dir?",
    tl(di), secenekler(di, 0, 800_000 * 0.20, 800_000 * 0.15, 800_000 * 0.30),
    "Md. 1 ve 2/5'e göre dernek veya vakıflara ait devamlı ticari işletmeler kurumlar vergisi mükellefidir; md. 2/6'ya göre "
    "tüzel kişiliğin olmaması veya kârın kuruluş amaçlarına tahsisi mükellefiyeti etkilemez: 800.000 × %25 = 200.000 ₺.",
    zorluk="easy")

P.q("KVK md. 21/2",
    f"{K}, tasfiye ve birleşme hâlinde verginin ödenmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tasfiye veya birleşme kârı üzerinden tarh olunan vergiler beyanname verme süresi içinde ödenir.",
    ["Tasfiye kârı üzerinden tarh olunan vergi iki eşit taksitte ödenir.",
     "Vadesi gelmemiş vergiler tasfiye bitiminden sonraki yılın sonuna kadar ödenir.",
     "Birleşme kârı üzerinden tarh olunan vergi birleşilen kurumun yıllık beyannamesiyle ödenir.",
     "Tasfiye kârı üzerinden vergi tarh edilmez, sadece ortaklar gelir vergisi öder."],
    "Md. 21/2'ye göre tasfiye ve birleşme hâlinde, tasfiye veya birleşme kârı üzerinden tarh olunan vergiler ile henüz vadesi "
    "gelmemiş vergiler, infisah eden kuruma ait kurumlar vergisi beyannamesinin verilme süresi içinde ödenir.")

P.q("KVK md. 4/1-j",
    "Bir futbol kulübü derneğinin sadece idman ve spor faaliyetinde bulunan iktisadi işletmesi ile kulübün stadyumda restoran "
    f"işleten ayrı bir iktisadi işletmesi bulunmaktadır.\n\n{K}, bu işletmelerin durumuna ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "İdman ve spor işletmesi muaftır; restoran işletmesi mükelleftir.",
    ["Her iki işletme de spor kulübüne ait olduğundan muaftır.",
     "Her iki işletme de kurumlar vergisi mükellefidir.",
     "Restoran işletmesi muaf, idman ve spor işletmesi mükelleftir.",
     "Sadece anonim şirket şeklinde kurulan spor işletmeleri muafiyetten yararlanır."],
    "Md. 4/1-j'ye göre tescilli spor kulüplerinin idman ve spor faaliyetlerinde bulunan iktisadi işletmeleri ile sadece idman "
    "ve spor faaliyetlerinde bulunan anonim şirketler muaftır; kulübün restoran gibi diğer ticari işletmeleri muafiyet dışıdır.")

ob = 3_000_000 * 0.25
P.sayisal("KVK md. 26/2, 32",
    "Türkiye’de işyeri ve daimi temsilcisi bulunmayan dar mükellef (LMN) GmbH, 2015 yılında satın aldığı ve ticari "
    "faaliyetinde kullanmadığı İstanbul’daki bir daireyi 2026 yılında satarak 3.000.000 ₺ kazanç elde etmiştir. Kurumlar "
    f"vergisi oranı %25 olarak alınacaktır.\n\n{K}, bu kazanç için özel beyannameyle hesaplanacak kurumlar vergisi kaç ₺’dir?",
    tl(ob), secenekler(ob, 0, 3_000_000 * 0.15, (3_000_000 - 150_000) * 0.25, 3_000_000 * 0.20),
    "Md. 26/2'ye göre dar mükellef kurumların diğer kazanç ve iratlarında GVK'daki vergilendirmeme hususundaki istisna, kayıt, "
    "şart ve süre sınırlamaları dikkate alınmaz; gerçek kişiler için geçerli beş yıl şartı ve değer artışı istisnası "
    "uygulanmaz: 3.000.000 × %25 = 750.000 ₺.", zorluk="hard")

P.q("KVK md. 4/1-n",
    "Bir organize sanayi bölgesi tüzel kişiliği, bölgedeki sanayicilere altyapı hizmeti vermekte, arsa tahsis etmekte ve "
    "elektrik dağıtmaktadır. Ayrıca bölgede halka açık bir alışveriş merkezi işletmektedir."
    f"\n\n{K}, OSB’nin muafiyetine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Altyapı ve bölgedekilere yönelik hizmetler muaf, alışveriş merkezi mükelleftir.",
    ["OSB tüzel kişiliğinin bütün faaliyetleri muaftır.",
     "OSB’ler kurumlar vergisinin konusuna girmez.",
     "OSB’nin sadece elektrik dağıtımı muaf olup arsa tahsisi dahil diğer tüm hizmetleri vergiye tabidir.",
     "Alışveriş merkezi işletmesi de bölge içinde olduğu için muaftır."],
    "Md. 4/1-n'ye göre organize sanayi bölgeleri ile küçük sanayi sitelerinin altyapılarını hazırlamak ve buralarda faaliyette "
    "bulunanların arsa, elektrik, su ve benzeri ihtiyaçlarını karşılamak üzere kurulan kurumlar muaftır; bu amaç dışındaki "
    "halka açık ticari faaliyetler muafiyet dışıdır.")

P.q("KVK md. 14/6-7",
    f"{K}, kurumlar vergisi mükelleflerinin bağlı olduğu vergi dairesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Mükellefin bağlı olduğu vergi dairesi kanuni veya iş merkezinin bulunduğu yerin vergi dairesidir.",
    ["Mükellefin bağlı olduğu vergi dairesi sadece ortakların ikametgâhına göre belirlenir.",
     "Şubesi olan kurumlar her şube için ayrı vergi dairesine bağlı olur.",
     "Maliye Bakanlığı mükelleflerin vergi dairesini belirleme yetkisine sahip değildir.",
     "Vergi dairesi kurumun en fazla hasılat elde ettiği ilde belirlenir."],
    "Md. 14/6'ya göre mükellefin bağlı olduğu vergi dairesi, kurumun kanuni veya iş merkezinin bulunduğu yerin vergi "
    "dairesidir; md. 14/7'ye göre Maliye Bakanlığı bağlı olunacak vergi dairesini kanuni veya iş merkezine bakmaksızın "
    "belirlemeye yetkilidir.", zorluk="easy")

t4 = (2_000_000 + 1_000_000) - (2_500_000 + 300_000)
P.sayisal("KVK md. 17/4",
    "Tasfiye hâlindeki (OPR) A.Ş.’nin 2025 yılında başlayıp aynı yıl biten tasfiye döneminde dönem başı servet değeri "
    "2.500.000 ₺, dönem sonu servet değeri 2.000.000 ₺’dir. Tasfiye sırasında ortaklara 1.000.000 ₺ avans ödenmiş ve "
    f"tam mükellef bir iştirakten 300.000 ₺ kâr payı elde edilmiştir.\n\n{K}, (OPR) A.Ş.’nin tasfiye kârı kaç ₺’dir?",
    tl(t4), secenekler(t4, 500_000, 800_000, 1_000_000, 3_000_000 - 2_500_000 - 300_000 + 1_000_000),
    "Md. 17/4'e göre ortaklara yapılan avanslar dönem sonu servetine, tasfiye sırasında elde edilen istisna kazançlar (iştirak "
    "kazancı) dönem başı servetine eklenir: (2.000.000 + 1.000.000) − (2.500.000 + 300.000) = 200.000 ₺.")

P.q("KVK md. 4/1-ç, d",
    f"{K}, kamu idareleriyle ilgili muafiyetlere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kamuya ait kreş ve konukevleri üçüncü kişilere kiralansa da muaftır.",
    ["Kamu idarelerince yetkili makamların izniyle açılan fuar ve panayırlar muaftır.",
     "Kamu idarelerince işletilen kütüphaneler, müzeler ve tiyatrolar muaftır.",
     "Kamu idarelerince işletilen öğrenci yurtları ve pansiyonlar muaftır.",
     "Askeri kışlalardaki kantinler muaftır."],
    "Md. 4/1-d'ye göre genel yönetim kapsamındaki kamu idarelerine ait kreş ve konukevlerinin muafiyeti; sadece kamu "
    "görevlilerine hizmet vermeleri, kâr amacı gütmemeleri ve üçüncü kişilere kiralanmamaları şartına bağlıdır.",
    zorluk="hard")

yd = 10_000_000 * 0.15 + 5_000_000 * 0.12
P.sayisal("KVK md. 23",
    "Kanuni ve iş merkezi Gürcistan’da olan (PRS) LLC, 2025 yılında hem Türkiye limanlarından yurt dışına deniz taşımacılığı "
    "hem de Türkiye sınırları içinde kara taşımacılığı yapmıştır. Türkiye’de elde edilmiş sayılan hasılat deniz "
    f"taşımacılığında 10.000.000 ₺, kara taşımacılığında 5.000.000 ₺’dir.\n\n{K}, (PRS) LLC’nin 2025 yılı kurumlar vergisi "
    "matrahı kaç ₺’dir?",
    tl(yd), secenekler(yd, 15_000_000 * 0.15, 15_000_000 * 0.12, 10_000_000 * 0.12 + 5_000_000 * 0.15, 15_000_000 * 0.05),
    "Md. 23'e göre ortalama emsal oranları deniz taşımacılığında %15, kara taşımacılığında %12'dir: 10.000.000 × %15 + "
    "5.000.000 × %12 = 1.500.000 + 600.000 = 2.100.000 ₺.")

P.q("KVK md. 3/3-a",
    "Kanuni ve iş merkezi Japonya’da olan (CDE) KK, Türkiye’deki işyeri aracılığıyla elde ettiği kazançların bir kısmının "
    "Türkiye’de satış sayılıp sayılmayacağını tartışmaktadır."
    f"\n\n{K}, dar mükellefiyette “Türkiye’de satmak” ifadesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Alıcı veya satıcının Türkiye’de olması ya da sözleşmenin Türkiye’de yapılmasıdır.",
    ["Satılan malın alıcıya fiziken Türkiye sınırları içinde teslim edilmesidir.",
     "Satış bedelinin Türkiye’deki bir banka hesabında tahsil edilmesidir.",
     "Satışa konu malın Türkiye’de üretilmiş veya işlenmiş olmasıdır.",
     "Satış faturasının Türkiye’de ve Türk lirası üzerinden düzenlenmesidir."],
    "Md. 3/3-a'ya göre Türkiye'de satmaktan maksat, alıcı veya satıcının ya da her ikisinin Türkiye'de olması veya satış "
    "sözleşmesinin Türkiye'de yapılmasıdır.")

dv = 800_000
P.sayisal("KVK md. 19-20",
    "Kanuni merkezleri Türkiye’de olan (STU) A.Ş., (VYZ) A.Ş. bünyesinde devir hükmündeki şartlarla birleşmiştir. (STU) "
    "A.Ş.’nin hesap dönemi başından devir tarihine kadar elde ettiği kurum kazancı 800.000 ₺’dir; birleşme nedeniyle "
    "ortaklarına verilen değerler ile servet değeri arasındaki fark 3.000.000 ₺’dir."
    f"\n\n{K}, (STU) A.Ş. adına verilecek beyannamede kurumlar vergisi matrahı kaç ₺’dir?",
    tl(dv), secenekler(dv, 3_800_000, 3_000_000, 0, 2_200_000),
    "Md. 20/1'e göre devir şartlarına uyulduğunda münfesih kurumun sadece devir tarihine kadar elde ettiği kazançlar "
    "vergilendirilir; birleşmeden doğan kârlar hesaplanmaz ve vergilendirilmez: matrah 800.000 ₺.")

P.q("KVK md. 17/1-b",
    "(FGH) Ltd. Şti.’nin tasfiyesi 3 Şubat 2025’te tescil edilerek başlamış ve 28 Kasım 2025’te tasfiyenin sona erdiği "
    f"tescil edilmiştir.\n\n{K}, (FGH) Ltd. Şti.’nin tasfiye dönemine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tasfiye dönemi 3 Şubat 2025’ten 28 Kasım 2025’e kadar tek dönemdir.",
    ["1 Ocak – 3 Şubat 2025 ve 3 Şubat – 28 Kasım 2025 olmak üzere iki tasfiye dönemi vardır.",
     "Tasfiye dönemi 1 Ocak – 31 Aralık 2025 takvim yılıdır.",
     "Tasfiye dönemi 3 Şubat 2025’te başlar ve 31 Aralık 2025’te sona erer.",
     "Tasfiye aynı yıl bittiği için tasfiye dönemi oluşmaz, normal hesap dönemi uygulanır."],
    "Md. 17/1-b'ye göre tasfiyenin başladığı takvim yılı içinde sona ermesi hâlinde tasfiye dönemi, kurumun tasfiyeye girdiği "
    "tarihten başlar ve tasfiyenin bittiği tarihe kadar devam eder.")

nb = 5_000_000 * 0.10
P.sayisal("KVK md. 19/3-a",
    "(WXY) A.Ş., tam bölünme yoluyla bütün malvarlığını kayıtlı değerleri üzerinden iki tam mükellef sermaye şirketine "
    "devretmektedir. Devralan şirketlerin, (WXY) A.Ş. ortaklarına vereceği iştirak hisselerinin toplam itibari değeri "
    f"5.000.000 ₺’dir.\n\n{K26}, işlemin tam bölünme sayılmasına engel olmaksızın ortaklara nakit olarak ödenebilecek "
    "azami tutar kaç ₺’dir?",
    tl(nb), secenekler(nb, 5_000_000 * 0.05, 5_000_000 * 0.20, 5_000_000 * 0.25, 5_000_000 * 0.15),
    "Md. 19/3-a'ya göre devredilen şirketin ortaklarına verilecek iştirak hisselerinin itibari değerinin %10'una kadarlık "
    "kısmının nakit ödenmesi işlemin bölünme sayılmasına engel değildir: 5.000.000 × %10 = 500.000 ₺.")

P.q("KVK md. 4/1-h",
    f"{K}, Darphane ve Damga Matbaası Genel Müdürlüğü ile askeri fabrika ve atölyelerin muafiyetine ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Muafiyet kuruluşlarındaki amaca uygun işlerle sınırlıdır.",
    ["Muafiyet, bu kuruluşların yaptığı her türlü ticari faaliyeti kapsar.",
     "Bu kuruluşlar kurumlar vergisi mükellefidir, muafiyetleri yoktur.",
     "Muafiyet sadece Darphane için geçerlidir, askeri fabrikalar mükelleftir.",
     "Muafiyet, kâr elde edilmemesi şartına bağlı olarak tanınır."],
    "Md. 4/1-h'ye göre Darphane ve Damga Matbaası Genel Müdürlüğü ile askeri fabrika ve atölyeler, kuruluşlarındaki amaca "
    "uygun işlerle sınırlı olmak şartıyla kurumlar vergisinden muaftır.", zorluk="easy")

P.sayisal("KVK md. 21/4",
    "(ZAB) A.Ş., Mart 2026 döneminde yaptığı kira ödemelerinden kestiği kurumlar vergisini Nisan 2026’da verdiği muhtasar "
    f"beyanname ile bildirmiştir.\n\n{K}, bu vergi Nisan 2026’nın en geç kaçıncı günü akşamına kadar ödenmelidir?",
    "26", ["20", "23", "25", "30"],
    "Md. 21/4'e göre muhtasar beyanname ile bildirilen vergiler, beyannamenin verildiği ayın yirmialtıncı günü akşamına kadar "
    "ödenir.")

if __name__ == "__main__":
    sys.exit(P.yaz())
