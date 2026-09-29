# -*- coding: utf-8 -*-
"""Vergi · Gelir Vergisi · Beyan ve Kazanç Tespiti — 60 soru, 2026 test biçimi.

Gerçek 2026/1-2026/2 kitapçıklarında gelir vergisi soruları tarife kökte verilerek hesap (matrah, ödenecek vergi,
yurt dışı vergi mahsubu), beyan edilmeyecek gelirler (md. 86), indirimler (md. 89) ve vergiye uyumlu mükellef
indirimi (mük. md. 121) üzerinden sorulmuştur.

Dayanak (29.09.2026 kontrolü, mevzuat.gov.tr güncel metin): 193 sayılı GVK md. 18, 21, 22, 63, 74, 85-92, 94, 103,
117, 119, mük. 120, mük. 121, 121, 123. Yıla bağlı tutarlar (tarife, istisna ve beyan sınırları) soru kökünde verilir;
doğru cevaplar vergi_ortak.py ile hesaplanır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import TARIFE_2025, gv2025, tl, secenekler

P = Paket("questions_topic_beyan_ve_tespit_2026.json", lesson="gelir_vergisi", topic="beyan_ve_tespit",
          konu_adi="Beyan ve Kazanç Tespiti", seed=2026092901,
          surum="193 sayılı GVK güncel metni (7524 ve sonraki değişiklikler dahil); 2025 tutarları kökte; 29.09.2026 kontrolü")

K = "193 sayılı Gelir Vergisi Kanunu’na göre"
K26 = "193 sayılı Gelir Vergisi Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"
SINIR = ("(2025 yılı için tarifenin ikinci gelir dilimindeki tutar 330.000 ₺, üçüncü dilimde ücret gelirleri için yer alan "
         "tutar 1.200.000 ₺, dördüncü gelir dilimindeki tutar 4.300.000 ₺’dir.)")
KIRA_IST = "(2025 yılı için konut kira geliri istisna tutarı 47.000 ₺ olarak alınacaktır.)"

# ================================================================ md. 86: beyan edilmeyecek gelirler (hesap)
m = 420_000 * 0.85
P.sayisal("GVK md. 86/1-b, 74",
    "Tam mükellef Bay (D)’nin tamamı üzerinden tevkifat yapılmış olan 2025 takvim yılı gelirleri şöyledir: birinci "
    "işverenden alınan safi ücret 3.800.000 ₺, ikinci işverenden alınan safi ücret 280.000 ₺. Bay (D) ayrıca bir "
    "dükkânını kiraya vermiş ve tevkifat yapılmış 420.000 ₺ brüt kira elde etmiştir; safi iradın tespitinde götürü gider "
    f"yöntemini seçmiştir. {SINIR}\n\n{K}, Bay (D)’nin 2025 yılı gelir vergisi beyannamesine dahil edeceği gelirlerin "
    "toplamı kaç ₺’dir?",
    tl(m), secenekler(m, 420_000, 280_000 + m, 3_800_000 + 280_000 + m, 3_800_000 + m, 4_080_000),
    "Md. 86/1-b'ye göre birden fazla işverenden ücret alınıp ikinciden sonraki işverenlerden alınanların toplamı "
    "(280.000 ₺) ikinci dilim tutarını (330.000 ₺), birinci işverenden alınan dahil toplam ücret (4.080.000 ₺) dördüncü "
    "dilim tutarını (4.300.000 ₺) aşmadığından tevkif edilmiş ücretler beyan edilmez. İşyeri kira geliri beyan edilir: "
    "md. 74'e göre %15 götürü gider düşülerek 420.000 × 0,85 = 357.000 ₺.", zorluk="medium")

P.sayisal("GVK md. 86/1-b",
    "Tam mükellef Bayan (E) 2025 yılında iki ayrı işverenden, tamamı tevkif suretiyle vergilendirilmiş ücret almıştır: "
    "birinci işverenden 3.600.000 ₺, ikinci işverenden 420.000 ₺ safi ücret. Bayan (E)’nin başka geliri yoktur. "
    f"{SINIR}\n\n{K}, Bayan (E)’nin 2025 yılı için beyan etmesi gereken ücret geliri toplamı kaç ₺’dir?",
    tl(4_020_000), secenekler(4_020_000, 0, 420_000, 3_600_000, 90_000, 4_300_000),
    "Md. 86/1-b'ye göre birinciden sonraki işverenlerden alınan ücretlerin toplamı ikinci dilim tutarını (330.000 ₺) "
    "aştığından (420.000 ₺) istisnai beyan dışı kalma şartı sağlanmaz; bu durumda birinci işverenden alınan dahil tüm "
    "ücretler beyan edilir: 3.600.000 + 420.000 = 4.020.000 ₺.", zorluk="hard")

P.q("GVK md. 86/1-b",
    "Tam mükellef Bay (F)’nin 2025 yılında tek işverenden aldığı ve tamamı tevkif suretiyle vergilendirilmiş brüt ücreti "
    "4.600.000 ₺’dir. Bay (F)’nin başka geliri yoktur. (2025 yılı için tarifenin dördüncü gelir dilimindeki tutar "
    f"4.300.000 ₺’dir.)\n\n{K}, Bay (F)’nin ücret gelirinin beyanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ücretin tamamı beyan edilir; tevkif edilen vergi mahsup edilir.",
    ["Tek işverenden alındığı için tutarına bakılmaksızın beyan edilmez.",
     "Sadece 4.300.000 ₺’yi aşan 300.000 ₺ beyan edilir.",
     "Ücret beyan edilir, ancak tevkif edilen vergi mahsup edilmez.",
     "Tevkif edilen vergi nihai vergi olduğundan beyan edilmez."],
    "Md. 86/1-b tek işverenden alınan ve tevkif suretiyle vergilendirilen ücretleri, dördüncü dilim tutarını aşmamak "
    "şartıyla beyan dışında bırakır. 4.600.000 ₺ bu tutarı aştığından ücretin tamamı beyan edilir; md. 121'e göre "
    "kesilen vergiler beyanname üzerinden hesaplanan vergiden mahsup edilir.")

P.q("GVK md. 86/1-c",
    "Tam mükellef Bayan (G) 2025 yılında tam mükellef bir anonim şirketten 500.000 ₺ brüt kâr payı almış, kâr payı "
    "üzerinden tevkifat yapılmıştır. Ayrıca tek işverenden tamamı tevkif suretiyle vergilendirilmiş 900.000 ₺ ücret "
    "almıştır. (2025 yılı için tarifenin ikinci gelir dilimindeki tutar 330.000 ₺, dördüncü dilimdeki tutar 4.300.000 ₺’dir.)"
    f"\n\n{K}, Bayan (G)’nin 2025 yılı beyanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kâr payının yarısı olan 250.000 ₺ ikinci dilim tutarını aşmadığından beyanname verilmez.",
    ["Kâr payının tamamı olan 500.000 ₺ ücretle birlikte beyan edilir.",
     "Ücret ve kâr payının yarısı toplamı 1.150.000 ₺ beyan edilir.",
     "Sadece ücret geliri beyan edilir; kâr payı beyan edilmez.",
     "Kâr payının yarısı beyan edilir, ücret ise beyan edilmez."],
    "Md. 22/3'e göre tam mükellef kurumlardan elde edilen kâr paylarının yarısı istisnadır; vergiye tabi kısım 250.000 ₺'dir. "
    "Md. 86/1-c'ye göre (a) ve (b) bentlerindekiler hariç vergiye tabi gelir toplamı ikinci dilim tutarını aşmıyorsa "
    "tevkifata tabi menkul sermaye iratları beyan edilmez. Tek işverenden alınan ücret (b) bendi kapsamında olduğundan "
    "bu toplama katılmaz.", zorluk="hard")

m = 700_000 / 2
P.sayisal("GVK md. 18, 22/3, 86/1-c",
    "Tam mükellef Bay (H), 2025 yılında Kültür ve Turizm Bakanlığınca tescilli bir romanının yayın haklarını devrederek "
    "4.500.000 ₺ elde etmiş, bu ödemeler üzerinden tevkifat yapılmıştır. Ayrıca tam mükellef bir anonim şirketten "
    "tevkifata tabi 700.000 ₺ brüt kâr payı almıştır. (2025 yılı için tarifenin ikinci gelir dilimindeki tutar 330.000 ₺, "
    f"dördüncü dilimdeki tutar 4.300.000 ₺’dir.)\n\n{K}, Bay (H)’nin 2025 yılı gelir vergisi matrahı (vergiye tabi "
    "geliri) kaç ₺’dir?",
    tl(4_500_000 + m), secenekler(4_500_000 + m, m, 4_500_000, 4_500_000 + 700_000, 700_000, 4_300_000),
    "Md. 18'e göre telif kazançları istisnası, bu kapsamdaki kazanç toplamı dördüncü dilim tutarını (4.300.000 ₺) "
    "aşarsa uygulanmaz; 4.500.000 ₺ beyan edilir. Md. 22/3'e göre kâr payının yarısı (350.000 ₺) istisnadır; kalan "
    "350.000 ₺ ikinci dilim tutarını aştığından md. 86/1-c'ye göre beyan edilir. Matrah 4.850.000 ₺'dir.", zorluk="hard")

P.q("GVK md. 86/1-d",
    "Tam mükellef Bayan (K), 2025 yılında yurt dışındaki bir bankada bulunan mevduatından Türkiye'de tevkifata tabi "
    "tutulmamış 18.000 ₺ faiz elde etmiştir; başka geliri yoktur. (Soruda md. 86/1-d’deki beyan sınırı 2025 yılı için "
    f"22.000 ₺ olarak alınacaktır.)\n\n{K}, bu gelirin beyanına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Toplam sınırı aşmadığından yıllık beyanname verilmez.",
    ["Yurt dışından elde edildiği için tutarına bakılmaksızın beyan edilir.",
     "Tevkifat yapılmadığı için 18.000 ₺’nin tamamı ayrıca muhtasar beyannameyle bildirilir.",
     "Menkul sermaye iradı olduğundan yarısı istisna, kalanı beyan edilir.",
     "Faiz gelirleri beyan edilmez; kesilen vergiler nihaidir."],
    "Md. 86/1-d'ye göre bir takvim yılında elde edilen ve toplamı kanunda belirtilen tutarı (soruda 22.000 ₺) aşmayan, "
    "tevkifata ve istisna uygulamasına konu olmayan menkul ve gayrimenkul sermaye iratları için beyanname verilmez.")

# ================================================================ md. 21 ve 74: kira geliri
m = (300_000 - 47_000) * 0.85
P.sayisal("GVK md. 21, 74",
    "Emekli olan Bay (L)’nin tek geliri, 2025 yılında bir dairesini konut olarak kiraya vermesinden elde ettiği 300.000 ₺ "
    "kira geliridir; Bay (L) götürü gider yöntemini seçmiştir. Emekli aylığı dışında ücret, menkul sermaye iradı veya başka "
    f"bir geliri yoktur. {KIRA_IST}\n\n{K}, Bay (L)’nin beyan edeceği safi kira geliri kaç ₺’dir?",
    tl(m), secenekler(m, 300_000 * 0.85, 300_000 - 47_000, 300_000 * 0.85 - 47_000, 300_000, 47_000 * 0.85),
    "Md. 21'e göre konut kira hasılatının istisna tutarı (47.000 ₺) düşülür: 300.000 − 47.000 = 253.000 ₺. Md. 74'e göre "
    "götürü gider hasılattan %15 oranında indirilir: 253.000 × 0,85 = 215.050 ₺. Emekli aylığı md. 23/18 uyarınca "
    "istisnadır.")

m = 360_000 * 0.85
P.sayisal("GVK md. 21/2",
    "Bay (M) 2025 yılında tek işverenden, tamamı tevkif suretiyle vergilendirilmiş 1.500.000 ₺ brüt ücret almıştır. Ayrıca "
    "bir konutunu kiraya vererek 360.000 ₺ kira geliri elde etmiş ve götürü gider yöntemini seçmiştir. (2025 yılı için konut "
    "kira istisnası 47.000 ₺; tarifenin üçüncü diliminde ücret gelirleri için yer alan tutar 1.200.000 ₺, dördüncü dilim "
    f"tutarı 4.300.000 ₺’dir.)\n\n{K}, Bay (M)’nin 2025 yılı beyannamesinde yer alacak safi kira geliri kaç ₺’dir?",
    tl(m), secenekler(m, (360_000 - 47_000) * 0.85, 360_000, 360_000 - 47_000, 1_500_000 + m, 360_000 * 0.85 - 47_000),
    "Md. 21/2'ye göre ücret, menkul ve gayrimenkul sermaye iratlarının gayrisafi toplamı tarifenin üçüncü diliminde ücret "
    "gelirleri için yer alan tutarı (1.200.000 ₺) aşanlar istisnadan yararlanamaz (beyan gerekip gerekmediğine "
    "bakılmaz). Ücret md. 86/1-b gereği beyan edilmez; kira geliri istisnasız beyan edilir: 360.000 × 0,85 = 306.000 ₺.",
    zorluk="hard")

gider_ist = 80_000 * 47_000 / 400_000
m = 400_000 - 47_000 - (80_000 - gider_ist)
P.sayisal("GVK md. 74/1",
    "Bayan (N), 2025 yılında bir konutunu kiraya vererek 400.000 ₺ kira hasılatı elde etmiştir. Başka geliri yoktur. Bayan "
    "(N) gerçek gider yöntemini seçmiş olup konutla ilgili belgelendirilmiş toplam gideri (onarım, sigorta, emlak vergisi) "
    f"80.000 ₺’dir. {KIRA_IST}\n\n{K}, Bayan (N)’nin beyan edeceği safi kira geliri kaç ₺’dir?",
    tl(m), secenekler(m, 400_000 - 47_000 - 80_000, (400_000 - 47_000) * 0.85, 400_000 * 0.85 - 80_000, 400_000 - 47_000),
    "Md. 74/1'e göre safi iratta, md. 21'e göre istisna edilen hasılata isabet eden giderler indirilemez. İstisnaya isabet "
    "eden gider: 80.000 × 47.000 / 400.000 = 9.400 ₺; indirilecek gider 70.600 ₺. Safi irat: 400.000 − 47.000 − 70.600 "
    "= 282.400 ₺.", zorluk="hard")

P.q("GVK md. 21",
    f"{K26}, konut kira geliri istisnasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İstisna haddini aşan hasılatı beyan etmeyen mükellef, istisna tutarını düşerek eksik vergi öder.",
    ["İstisna sadece binaların mesken olarak kiraya verilmesinden elde edilen hasılata uygulanır.",
     "Ticari, zirai veya mesleki kazancını yıllık beyannameyle bildirmekle yükümlü olanlar istisnadan yararlanamaz.",
     "İstisna haddi üzerinde hasılat elde edilip eksik beyan edilmesi hâlinde istisnadan yararlanılamaz.",
     "İşyeri olarak kiraya verilen gayrimenkulün kira geliri bu istisnanın kapsamında değildir."],
    "Md. 21'e göre istisna mesken kira hasılatına uygulanır; ticari, zirai veya mesleki kazancını beyan etmek zorunda "
    "olanlar ve gelir toplamı kanundaki tutarı aşanlar yararlanamaz. İstisna haddi üzerinde hasılat elde edilip beyan "
    "edilmemesi veya eksik beyan edilmesi hâlinde istisnadan yararlanılamaz.")

P.q("GVK md. 74",
    f"{K26}, gayrimenkul sermaye iratlarında götürü gider yöntemine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Hakların kiraya verilmesinde de hasılatın %15’i götürü gider olarak indirilebilir.",
    ["Götürü gider oranı hasılatın %15’idir.",
     "Götürü gider yöntemini seçenler iki yıl geçmedikçe bu yöntemden dönemez.",
     "Götürü gider, kanunda sayılan gerçek giderlere karşılık olmak üzere indirilir.",
     "Para cezaları ve vergi cezaları hasılattan gider olarak indirilemez."],
    "Md. 74'e göre mükellefler (hakları kiraya verenler hariç) hasılatın %15'ini götürü gider olarak indirebilir ve bu "
    "usulü seçenler iki yıl geçmedikçe dönemez. Para ve vergi cezaları hasılattan indirilemez.")

P.q("GVK md. 74/1-4",
    "Bay (P) 2025 yılında, 2023 yılında satın aldığı tek konutunu kiraya vermiş ve gerçek gider yöntemini seçmiştir. "
    f"{K}, Bay (P)’nin bu konut için gayrisafi hasılattan indirebileceği giderler arasında aşağıdakilerden hangisi "
    "yer almaz?",
    "Konutun alımı için kullanılan kredinin 2025 yılında ödenen faizi",
    ["Konutun iktisap bedelinin %5’i (iktisap yılından itibaren beş yıl süreyle)",
     "Kiraya verilen konut için ödenen emlak vergisi",
     "Kiraya veren tarafından yaptırılan onarım gideri",
     "Kiraya verilen konuta ait sigorta gideri"],
    "Md. 74/1-4'e göre konutlar hariç kiraya verilen mal ve haklar için yapılan borçların faizleri indirilir; konut olarak "
    "kiraya verilen bir gayrimenkulde faiz yerine iktisap bedelinin %5'i beş yıl süreyle indirilebilir. Vergiler (bent 5), "
    "onarım (bent 7) ve sigorta (bent 3) giderleri indirilebilir.", zorluk="hard")

# ================================================================ md. 88-89: zarar ve indirimler (hesap)
beyan = 2_000_000 - 100_000
m = beyan - min(300_000, beyan * 0.10)
P.sayisal("GVK md. 89/1-2",
    "Tam mükellef ve birinci sınıf tüccar Bay (R)’nin 2025 yılında elde ettiği ticari kazanç, işletmesi adına ödediği ve "
    "gider yazdığı 100.000 ₺ Bağ-Kur primi düşüldükten sonra 1.900.000 ₺’dir. Bay (R) ayrıca küçük çocuğunun Türkiye’deki "
    f"özel okulu için fatura karşılığı 300.000 ₺ eğitim harcaması yapmıştır.\n\n{K}, Bay (R)’nin 2025 yılı gelir vergisi "
    "matrahı kaç ₺’dir?",
    tl(m), secenekler(m, 1_900_000 - 300_000, 1_900_000, 2_000_000 - 200_000, 1_900_000 - 95_000, 1_710_000 - 100_000),
    "Md. 89/1-2'ye göre Türkiye'de yapılan ve belgelendirilen eğitim ve sağlık harcamaları beyan edilen gelirin %10'unu "
    "aşmamak üzere indirilir. Beyan edilen gelir 1.900.000 ₺; indirim sınırı 190.000 ₺. Matrah 1.900.000 − 190.000 = "
    "1.710.000 ₺.")

bg = 3_000_000
m = bg - min(400_000, bg * 0.10) - min(200_000, bg * 0.05)
P.sayisal("GVK md. 89/1-2, 89/1-4",
    "Serbest meslek erbabı Bayan (S)’nin 2025 yılında beyan ettiği serbest meslek kazancı 3.000.000 ₺’dir. Bayan (S) aynı "
    "yıl Türkiye’deki bir hastanede kendisi için yaptırdığı tedavi nedeniyle belgelendirilmiş 400.000 ₺ sağlık harcaması "
    "yapmış, kalkınmada öncelikli yöre dışında bulunan ve kamu yararına çalışan bir derneğe makbuz karşılığı 200.000 ₺ "
    f"bağışta bulunmuştur.\n\n{K}, Bayan (S)’nin 2025 yılı gelir vergisi matrahı kaç ₺’dir?",
    tl(m), secenekler(m, bg - 400_000 - 200_000, bg - 300_000 - 200_000, bg - 400_000 - 150_000, bg - 300_000, bg),
    "Md. 89/1-2'ye göre sağlık harcaması beyan edilen gelirin %10'u (300.000 ₺), md. 89/1-4'e göre kamu yararına çalışan "
    "derneğe bağış %5'i (150.000 ₺) ile sınırlıdır. Matrah: 3.000.000 − 300.000 − 150.000 = 2.550.000 ₺.")

bg = 1_000_000
prim = 200_000 * 0.5 + 80_000
m = bg - min(prim, bg * 0.15, 312_066)
P.sayisal("GVK md. 89/1-1",
    "Tam mükellef Bay (T)’nin 2025 yılında beyan ettiği ticari kazanç 1.000.000 ₺’dir. Bay (T) aynı yıl Türkiye’de "
    "merkezi bulunan bir sigorta şirketine kendisi için 200.000 ₺ hayat sigortası primi ve 80.000 ₺ özel sağlık "
    "sigortası primi ödemiştir. (2025 yılı için asgari ücretin yıllık brüt tutarı 312.066 ₺ olarak alınacaktır.)"
    f"\n\n{K}, Bay (T)’nin 2025 yılı gelir vergisi matrahı kaç ₺’dir?",
    tl(m), secenekler(m, bg - prim, bg - 280_000, bg - 100_000, bg - 80_000, bg - 312_066),
    "Md. 89/1-1'e göre hayat sigortası primlerinin %50'si (100.000 ₺) ile şahıs sigorta primleri (80.000 ₺) toplamı "
    "180.000 ₺'dir; indirim beyan edilen gelirin %15'i (150.000 ₺) ve asgari ücretin yıllık tutarı (312.066 ₺) ile "
    "sınırlıdır. Matrah: 1.000.000 − 150.000 = 850.000 ₺.", zorluk="hard")

m = 900_000 - 350_000
P.sayisal("GVK md. 88",
    "Bay (U) 2025 yılında ticari faaliyetinden 350.000 ₺ zarar etmiş, aynı yıl işyeri olarak kiraya verdiği dükkândan "
    "götürü gider düşüldükten sonra 900.000 ₺ safi kira geliri elde etmiştir. Önceki yıllardan devreden zararı yoktur."
    f"\n\n{K}, Bay (U)’nun 2025 yılı gelir vergisi matrahı kaç ₺’dir?",
    tl(m), secenekler(m, 900_000, 900_000 + 350_000, 900_000 - 175_000, 350_000, 900_000 * 0.85 - 350_000),
    "Md. 88'e göre gelirin toplanmasında gelir kaynaklarının bir kısmından doğan zararlar (80. maddedeki diğer kazanç ve "
    "iratlardan doğanlar hariç) diğer kaynakların kazanç ve iratlarına mahsup edilir: 900.000 − 350.000 = 550.000 ₺.")

P.q("GVK md. 88",
    f"{K}, zararların mahsubuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Mahsup edilemeyen zarar bakiyesi, süre sınırı olmaksızın izleyen yılların gelirinden indirilir.",
    ["Diğer kazanç ve iratlardan (md. 80) doğan zararlar diğer kaynakların kazançlarına mahsup edilmez.",
     "Menkul ve gayrimenkul sermaye iratlarında, gider fazlalığı dışındaki sermaye eksilmeleri zarar sayılmaz.",
     "Türkiye'de istisna edilen kazançlarla ilgili yurt dışı zararlar yurt içi kazançlardan mahsup edilmez.",
     "Yurt dışı zararlar, kanunda öngörülen rapor ve onay şartları sağlanırsa mahsup edilebilir."],
    "Md. 88'e göre mahsup neticesinde kapatılmayan zarar müteakip yılların gelirinden indirilir; ancak arka arkaya beş "
    "yıl içinde mahsup edilmeyen zarar bakiyesi sonraki yıllara nakledilemez. Diğer ifadeler maddeye uygundur.")

P.q("GVK md. 89",
    f"{K26}, beyan edilen gelirden yapılacak indirimlere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Eğitim harcamasının indirilebilmesi için harcamanın yurt dışında yapılmış olması engel değildir.",
    ["Eğitim ve sağlık harcamaları mükellefin kendisi, eşi ve küçük çocuklarına ilişkin olmalıdır.",
     "Eğitim ve sağlık harcamaları gelir veya kurumlar vergisi mükelleflerinden alınan belgelerle tevsik edilmelidir.",
     "Hayat sigortası primlerinin %50’si, şahıs sigortası primlerinin ise tamamı indirim hesabına katılır.",
     "Belediyelere bağışlanan okul veya sağlık tesisi inşası harcamalarının tamamı indirilebilir."],
    "Md. 89/1-2'ye göre eğitim ve sağlık harcamaları beyan edilen gelirin %10'unu aşmamak, Türkiye'de yapılmak ve gelir "
    "veya kurumlar vergisi mükelleflerinden alınan belgelerle tevsik edilmek şartıyla indirilir. Sigorta primleri bent 1, "
    "okul ve sağlık tesisi bağışları bent 5 kapsamındadır.")

P.q("GVK md. 89/1-3, md. 31",
    "Serbest meslek erbabı olan Bay (V), çalışma gücünün %65’ini kaybetmiş olup ikinci derece engellidir. Bay (V) 2025 "
    f"yılında serbest meslek kazancını yıllık beyannameyle beyan edecektir.\n\n{K}, Bay (V)’nin engellilik indirimine "
    "ilişkin aşağıdakilerden hangisi doğrudur?",
    "Md. 31’deki esaslara göre hesaplanan yıllık indirimi beyan ettiği gelirden indirebilir.",
    ["Engellilik indirimi sadece hizmet erbabının ücretlerine uygulanır, serbest meslek erbabı yararlanamaz.",
     "İndirim, ikinci derece engelliler için birinci derece tutarının iki katı olarak uygulanır.",
     "İndirim, beyan edilen gelirin %10’unu aşmamak şartıyla eğitim harcaması gibi uygulanır.",
     "Engellilik indirimi sadece geçici vergi beyannamelerinde dikkate alınır."],
    "Md. 89/1-3'e göre serbest meslek faaliyetinde bulunan engellilerin beyan edilen gelirlerine md. 31'deki esaslara göre "
    "hesaplanan yıllık indirim uygulanır; md. 31'e göre çalışma gücünün asgari %60'ını kaybeden ikinci derece engellidir. "
    "Bakmakla yükümlü olduğu engelli bulunan serbest meslek erbabı da yararlanabilir.")

# ================================================================ tarife ve ödenecek vergi
m = 900_000
v = gv2025(m)
P.sayisal("GVK md. 103",
    f"{TARIFE_2025}\n\nBayan (Y)’nin 2025 yılı gelir vergisi matrahı ticari kazançtan oluşan 900.000 ₺’dir. {K}, Bayan "
    "(Y)’nin 2025 yılı için hesaplanan gelir vergisi kaç ₺’dir?",
    tl(v), secenekler(v, gv2025(m, True), 900_000 * 0.27, 900_000 * 0.35, 185_000, 58_100 + 570_000 * 0.35),
    "Ücret dışı gelirde 800.000 ₺ için 185.000 ₺, aşan 100.000 ₺ için %35 = 35.000 ₺ vergi hesaplanır; toplam 220.000 ₺. "
    "Ücret tarifesi uygulansaydı 800.000 ₺'lik dilim sınırı 1.200.000 ₺ olacaktı.", zorluk="easy")

v = gv2025(5_000_000, True)
P.sayisal("GVK md. 103, 121",
    f"{TARIFE_2025}\n\nBay (Z)’nin 2025 yılında tek işverenden aldığı safi ücret 5.000.000 ₺’dir ve beyan edilmesi "
    "gerekmektedir. Yıl içinde işveren tarafından 1.640.000 ₺ gelir vergisi tevkif edilmiştir; başka geliri yoktur."
    f"\n\n{K}, Bay (Z)’nin yıllık beyanname üzerinden ödeyeceği gelir vergisi kaç ₺’dir?",
    tl(v - 1_640_000), secenekler(v - 1_640_000, gv2025(5_000_000) - 1_640_000, v, 1_640_000, 5_000_000 * 0.40 - 1_640_000),
    "Ücret tarifesiyle: 4.300.000 ₺ için 1.378.000 ₺ + 700.000 × %40 = 280.000 ₺; hesaplanan vergi 1.658.000 ₺. Md. 121'e "
    "göre tevkif edilen 1.640.000 ₺ mahsup edilir; ödenecek vergi 18.000 ₺'dir.", zorluk="hard")

v = gv2025(4_000_000)
isabet = v * 1_000_000 / 4_000_000
mahsup = min(400_000, isabet)
od = v - mahsup - 500_000
P.sayisal("GVK md. 123, mük. 120",
    f"{TARIFE_2025}\n\nİstanbul’da ikamet eden Bay (A) 2025 yılında Türkiye’deki ticari faaliyetinden 3.000.000 ₺, "
    "Almanya’daki şubesinden ₺ karşılığı 1.000.000 ticari kazanç elde etmiş; Almanya’da bu kazanç için ₺ karşılığı "
    "400.000 gelir vergisi ödemiş ve bunu konsoloslukça tasdikli belgeyle tevsik etmiştir. Yıl içinde 500.000 ₺ geçici "
    f"vergi ödemiştir.\n\n{K}, Bay (A)’nın 2025 yılı için ödeyeceği gelir vergisi kaç ₺’dir?",
    tl(od), secenekler(od, v - 400_000 - 500_000, v - 500_000, v - isabet, gv2025(3_000_000) - 500_000),
    "Toplam matrah 4.000.000 ₺: 185.000 + 3.200.000 × %35 = 1.305.000 ₺. Md. 123'e göre yurt dışı vergi, Türkiye'de "
    "hesaplanan verginin yurt dışı kazanca isabet eden kısmıyla sınırlıdır: 1.305.000 × 1/4 = 326.250 ₺ (ödenen 400.000 ₺ "
    "yerine). Mük. 120'ye göre geçici vergi mahsup edilir: 1.305.000 − 326.250 − 500.000 = 478.750 ₺.", zorluk="hard")

P.q("GVK md. 123",
    f"{K}, yabancı memlekette ödenen vergilerin Türkiye’de hesaplanan gelir vergisinden indirilmesine ilişkin aşağıdaki "
    "ifadelerden hangisi yanlıştır?",
    "Yurt dışında ödenen verginin tamamı, Türkiye’de hesaplanan vergiden fazla olsa da iade edilir.",
    ["İndirim için yurt dışında ödenen verginin gelir üzerinden alınan şahsi bir vergi olması gerekir.",
     "Ödenen vergi, mahallindeki Türk elçilik veya konsolosluklarınca tasdikli belgelerle tevsik edilir.",
     "Belgeler taksit zamanına kadar gelmezse yurt dışı kazanca isabet eden vergi bir yıl süreyle ertelenir.",
     "İndirilecek tutar, Türkiye’de hesaplanan verginin yurt dışı kazanç ve iratlara isabet eden kısmıyla sınırlıdır."],
    "Md. 123'e göre indirilecek miktar, gelir vergisinin yurt dışı kazanç ve iratlara isabet eden kısmından fazla olursa "
    "aradaki fark nazara alınmaz; fark iade edilmez. Şahsi vergi olma, konsolosluk tasdiki ve bir yıllık erteleme "
    "şartları maddede yer alır.")

P.q("GVK md. 85",
    "Tam mükellef Bay (B)’nin 2025 yılında Kazakistan’daki işinden hak ettiği kazanç, o ülkenin döviz transfer "
    "kısıtlaması nedeniyle ancak 2026 yılında Türkiye’deki hesaplarına aktarılabilmiştir. Bay (B) kısıtlamanın kendi "
    f"iradesi dışında olduğunu belgelemektedir.\n\n{K}, bu kazanç hangi yılda elde edilmiş sayılır?",
    "Mükellefin bu kazanca tasarruf edebildiği yılda",
    ["Kazancın yurt dışında hak edildiği 2025 yılında",
     "Kazancın elde edildiği ülkenin vergi yılı sonunda",
     "Kazancın Türkiye’de beyan edilmesini mükellefin seçtiği yılda",
     "Kazancın döviz olarak yurt dışında tahsil edildiği tarihte"],
    "Md. 85'e göre yabancı memleketlerde elde edilen kazanç ve iratlar, mükellefin bunları Türkiye'de hesaplarına intikal "
    "ettirdiği yılda; Türkiye'de hesaplara intikal ettirilmemesinin mükellefin iradesi dışındaki sebeplerden ileri geldiği "
    "tevsik olunan hâllerde bunlara tasarruf edebildiği yılda elde edilmiş sayılır.", zorluk="hard")

# ================================================================ beyan zamanı, ödeme, tevkifat
P.q("GVK md. 92",
    f"{K}, yıllık gelir vergisi beyannamesinin verilme zamanına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bir takvim yılına ait beyanname, izleyen yılın Nisan ayının sonuna kadar verilir.",
    ["Beyanname izleyen yılın Mart ayının başından yirmi beşinci günü akşamına kadar verilir.",
     "Takvim yılı içinde memleketi terk edenler beyannamelerini terkten önceki 15 gün içinde verir.",
     "Ölüm hâlinde beyanname, ölüm tarihinden itibaren 4 ay içinde verilir.",
     "Tam mükellefiyette beyanname vergiyi tarha yetkili vergi dairesine verilir."],
    "Md. 92'ye göre yıllık beyanname izleyen yılın Mart ayının başından yirmi beşinci günü akşamına kadar verilir; "
    "memleketi terkte terkten önceki 15 gün, ölümde ölüm tarihinden itibaren 4 ay içinde verilir.", zorluk="easy")

P.q("GVK md. 117",
    "Bayan (C) 2025 yılı gelirleri için yıllık beyannamesini Mart 2026’da süresinde vermiş ve 600.000 ₺ gelir vergisi "
    f"tahakkuk etmiştir.\n\n{K}, bu verginin ödenmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Mart ve Temmuz aylarında olmak üzere iki eşit taksitte ödenir.",
    ["Beyannamenin verildiği ay tek seferde ödenir.",
     "Mart, Haziran ve Eylül aylarında üç eşit taksitte ödenir.",
     "Mart ve Kasım aylarında iki eşit taksitte ödenir.",
     "Aylık eşit taksitlerle yıl sonuna kadar ödenir."],
    "Md. 117'ye göre yıllık beyanname ile bildirilen gelir üzerinden tahakkuk eden gelir vergisi Mart ve Temmuz aylarında "
    "olmak üzere iki eşit taksitte ödenir.", zorluk="easy")

P.q("GVK md. 94",
    f"{K}, aşağıdakilerden hangisi md. 94 kapsamında vergi tevkifatı yapmaya mecbur olanlar arasında sayılmaz?",
    "Gerçek gelirini beyan etmeyen ve basit usulde vergilendirilen esnaf",
    ["Kamu idare ve müesseseleri",
     "Ticaret şirketleri ve kooperatifler",
     "Gerçek gelirlerini beyan etmeye mecbur olan serbest meslek erbabı",
     "Zirai kazancını bilanço veya zirai işletme hesabı esasına göre tespit eden çiftçiler"],
    "Md. 94'e göre kamu idareleri, iktisadi kamu müesseseleri, ticaret şirketleri, iş ortaklıkları, dernek ve vakıflar, "
    "kooperatifler, gerçek gelirlerini beyan etmeye mecbur ticaret ve serbest meslek erbabı ile bilanço veya zirai işletme "
    "hesabı esasına tabi çiftçiler tevkifat yapar. Basit usulde vergilendirilenler sayılmaz.")

P.q("GVK md. 119",
    "(S) Ltd. Şti. Mayıs 2025’te çalışanlarına ödediği ücretler üzerinden gelir vergisi tevkifatı yapmış ve bu tevkifatı "
    f"Haziran 2025’te muhtasar ve prim hizmet beyannamesiyle beyan edecektir.\n\n{K}, tevkif edilen verginin vergi "
    "dairesine yatırılma süresi aşağıdakilerden hangisidir?",
    "Beyannamenin verileceği ayın yirmi altıncı günü akşamına kadar",
    ["Ücretin ödendiği ayın son günü akşamına kadar",
     "Beyannamenin verileceği ayın on beşinci günü akşamına kadar",
     "Tevkifatın yapıldığı tarihten itibaren yedi gün içinde",
     "Yılı izleyen Mart ayının yirmi beşinci günü akşamına kadar"],
    "Md. 119'a göre md. 94 gereğince yapılan tevkifat, vergi kesenlerce beyanname verecekleri ayın yirmi altıncı günü "
    "akşamına kadar bağlı oldukları vergi dairesine yatırılır.")

P.q("GVK md. 121",
    "Bay (D) yıllık beyannamesine dahil ettiği serbest meslek kazancı üzerinden yıl içinde 180.000 ₺ tevkifat yapılmış, "
    f"beyanname üzerinden ise 120.000 ₺ gelir vergisi hesaplanmıştır.\n\n{K}, bu duruma ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Aradaki 60.000 ₺ vergi dairesince mükellefe iade edilir.",
    ["Fazla tevkifat terkin edilir, mükellefe iade edilmez.",
     "Fazla tevkifat izleyen yılın geçici vergisinden mahsup edilir.",
     "Hesaplanan vergi tevkifattan az olduğu için beyanname hükümsüz sayılır.",
     "Mahsup sadece hesaplanan vergi kadar yapılır, kalan tutar hazineye gelir kaydedilir."],
    "Md. 121'e göre yıllık beyannamedeki gelire dahil kazanç ve iratlardan kesilen vergiler beyanname üzerinden hesaplanan "
    "vergiye mahsup edilir; mahsubu yapılan miktar gelir vergisinden fazlaysa aradaki fark vergi dairesince mükellefe "
    "red ve iade olunur.")

# ================================================================ geçici vergi
P.sayisal("GVK mük. 120",
    "Serbest meslek erbabı Bayan (E)’nin 2025 yılının ilk dokuz aylık döneminde (1 Ocak-30 Eylül) elde ettiği kümülatif "
    "serbest meslek kazancı 1.200.000 ₺’dir. İlk iki dönem için toplam 100.000 ₺ geçici vergi tahakkuk etmiştir; dönem "
    "içinde tevkif edilen gelir vergisi yoktur. (Tarifenin ilk gelir dilimine uygulanan oran %15’tir.)"
    f"\n\n{K}, Bayan (E)’nin 2025 yılı üçüncü geçici vergi döneminde ödeyeceği geçici vergi kaç ₺’dir?",
    tl(1_200_000 * 0.15 - 100_000), secenekler(80_000, 180_000, 1_200_000 * 0.20 - 100_000, 60_000, 100_000),
    "Mük. 120'ye göre geçici vergi, üçer aylık dönem kazançları üzerinden tarifenin ilk dilimine uygulanan oranda (%15) "
    "hesaplanır; kümülatif hesapta önceki dönemlerde hesaplanan geçici vergi düşülür: 1.200.000 × %15 = 180.000; "
    "180.000 − 100.000 = 80.000 ₺.")

P.q("GVK mük. 120",
    f"{K26}, geçici vergiye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Geçici vergi, üçer aylık kazançlar üzerinden artan oranlı tarifeye göre hesaplanır.",
    ["Ticari kazanç sahipleri ile serbest meslek erbabı geçici vergi öder.",
     "Birden fazla takvim yılına yaygın inşaat ve onarma işlerinden (md. 42) elde edilen kazançlar matraha dahil edilmez.",
     "Geçici vergi, üç aylık dönemi izleyen ikinci ayın on dördüncü günü akşamına kadar beyan edilir.",
     "Geçmiş dönem geçici vergisinin %10’u aşan tutarda eksik beyan edildiği tespit edilirse re’sen veya ikmalen tarh edilir."],
    "Mük. 120'ye göre geçici vergi tarifenin ilk dilimine uygulanan oranda (%15) hesaplanır; artan oranlı değildir. "
    "Md. 42 kazançları ve noterlik kazançları dahil edilmez; beyan izleyen ikinci ayın 14'ü, ödeme 17'si akşamına kadardır.")

P.q("GVK mük. 120",
    "Bay (F) 2025 yılı için dört dönem boyunca toplam 700.000 ₺ geçici vergi ödemiş, yıllık beyannamesinde ise 450.000 ₺ "
    f"gelir vergisi hesaplanmıştır. Başka vergi borcu yoktur.\n\n{K}, mahsup edilemeyen geçici vergiye ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Kalan tutar yıl sonuna kadar yazılı talep edilirse iade edilir.",
    ["Kalan 250.000 ₺ talep aranmaksızın izleyen yılın gelir vergisinden mahsup edilir.",
     "Geçici vergi kesin vergi olduğundan fazlası iade edilmez.",
     "Kalan tutar ancak vergi mahkemesinde dava açılırsa iade edilebilir.",
     "Kalan tutar beş yıl içinde talep edilirse faiziyle birlikte iade edilir."],
    "Mük. 120'ye göre geçici vergi yıllık beyanname üzerinden hesaplanan vergiden, mahsup edilemeyen tutar diğer vergi "
    "borçlarından mahsup edilir; kalan tutar o yılın sonuna kadar yazılı olarak talep edilirse red ve iade edilir.", zorluk="hard")

# ================================================================ vergiye uyumlu mükellef indirimi
v = 1_000_000
ind = min(v * 0.05 * 0.8, 9_900_000)
P.sayisal("GVK mük. 121",
    "Vergiye uyumlu mükellef şartlarını taşıyan Bay (G)’nin 2025 yılı gelir vergisi matrahının %80’i ticari kazançtan, "
    "%20’si gayrimenkul sermaye iradından oluşmaktadır. Beyanname üzerinden hesaplanan gelir vergisi 1.000.000 ₺’dir. "
    "(İndirim tutarı sınırı 2025 yılı için 9.900.000 ₺ olarak alınacaktır.)"
    f"\n\n{K}, Bay (G)’nin yararlanacağı vergi indirimi kaç ₺’dir?",
    tl(ind), secenekler(ind, 50_000, 10_000, 800_000 * 0.05 * 0.8, 1_000_000 * 0.10),
    "Mük. 121'e göre indirim, hesaplanan verginin %5'idir; gelir vergisi mükelleflerinde ticari, zirai veya mesleki "
    "kazançların toplam matrah içindeki oranı dikkate alınarak hesaplanır: 1.000.000 × %80 × %5 = 40.000 ₺.")

P.q("GVK mük. 121",
    f"{K}, aşağıdakilerden hangisi vergiye uyumlu mükellef indiriminden yararlanabilmek için aranan şartlardan biri "
    "değildir?",
    "İndirimin hesaplanacağı yılda ticari kazancın bir önceki yıla göre artmış olması",
    ["Beyannamenin ait olduğu yıl ile önceki iki yıla ait beyannamelerin kanuni süresinde verilmiş olması",
     "Bu süre içinde kesinleşmiş ikmalen, re’sen veya idarece yapılmış bir tarhiyatın bulunmaması",
     "Beyannamenin verildiği tarih itibarıyla söz konusu beyannameler üzerine tahakkuk eden vergilerin ödenmiş olması",
     "Beyannamenin verildiği tarih itibarıyla kanunda belirtilen tutarı aşan vadesi geçmiş borcun bulunmaması"],
    "Mük. 121'e göre şartlar; son üç yıl beyannamelerinin süresinde verilmesi, kesinleşmiş tarhiyat bulunmaması, tahakkuk "
    "eden vergilerin ödenmesi, vadesi geçmiş borç bulunmaması ve beş yıl içinde VUK 359'daki fiillerin işlenmemiş "
    "olmasıdır. Kazanç artışı şart değildir.")

P.q("GVK mük. 121",
    f"{K26}, vergiye uyumlu mükellef indirimine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bankacılık sektöründe faaliyet gösteren kurumlar vergisi mükellefleri de indirimden yararlanabilir.",
    ["İndirim, yıllık beyanname üzerinden hesaplanan verginin %5’idir.",
     "Hesaplanan indirim tutarı kanunda belirtilen üst sınırı aşamaz.",
     "Ödenmesi gereken vergiden fazla olan indirim tutarı, izleyen bir tam yıl içinde diğer vergilerden mahsup edilebilir.",
     "Bu süre içinde mahsup edilemeyen indirim tutarları red ve iade edilmez."],
    "Mük. 121'e göre finans ve bankacılık sektörü, sigorta, reasürans ve emeklilik şirketleri ile emeklilik yatırım fonları "
    "indirimden yararlanamaz. Oran %5'tir, üst sınır vardır; fazlası bir tam yıl içinde diğer vergilerden mahsup edilir, "
    "mahsup edilemeyen iade edilmez.")

P.q("GVK mük. 121",
    "Bayan (H) 2023, 2024 ve 2025 yıllarına ait tüm beyannamelerini süresinde vermiş, 2024 yılı beyannamesinde tespit "
    "ettiği bir hatayı 2025 yılında kanuni süreden sonra pişmanlıkla verdiği düzeltme beyannamesiyle gidermiştir. Diğer "
    f"şartları taşımaktadır.\n\n{K}, Bayan (H)’nin 2025 yılı için vergiye uyumlu mükellef indiriminden yararlanmasına "
    "ilişkin aşağıdakilerden hangisi doğrudur?",
    "Pişmanlıkla düzeltme şart ihlali sayılmadığından yararlanabilir.",
    ["Kanuni süreden sonra beyanname verdiği için indirimden yararlanamaz.",
     "Sadece 2024 yılı için hesaplanan kısım kadar indirimden yararlanamaz.",
     "Pişmanlıkla beyanname verenler beş yıl süreyle indirimden yararlanamaz.",
     "İndirimden yararlanabilmesi için vergi dairesinden ayrıca izin alması gerekir."],
    "Mük. 121/2-1'e göre kanuni süresinde verilen bir beyannameye ilişkin olarak kanuni süresinden sonra düzeltme amacıyla "
    "veya pişmanlıkla verilen beyannameler bu şartın ihlali sayılmaz.", zorluk="hard")

# ================================================================ öncül ve karma
P.oncul("GVK md. 86",
    f"{K} aşağıdaki gelirler değerlendirilmektedir:",
    ["Gerçek usulde vergilendirilmeyen zirai kazançlar",
     "Tek işverenden alınan, tevkifata tabi ve dördüncü dilim tutarını aşmayan ücretler",
     "Beyanı gereken ticari kazanç",
     "Kazanç ve iratların istisna hadleri içinde kalan kısmı"],
    "Yukarıdakilerden hangileri için yıllık beyanname verilmez?",
    "I, II ve IV",
    ["I ve II", "II ve III", "I, II ve IV", "I, III ve IV", "II, III ve IV"],
    "Md. 86/1-a gerçek usulde vergilendirilmeyen zirai kazançları ve istisna hadleri içinde kalan kazanç ve iratları, "
    "86/1-b tek işverenden alınan ve dördüncü dilim tutarını aşmayan tevkifatlı ücretleri beyan dışında bırakır. "
    "Ticari kazanç md. 85 gereği beyan edilir.", zorluk="hard")

P.q("GVK md. 90",
    "Tüccar Bay (K) 2025 yılında işletmesiyle ilgili olarak 40.000 ₺ trafik para cezası, 25.000 ₺ vergi ziyaı cezası ve "
    f"6183 sayılı Kanuna göre 15.000 ₺ gecikme zammı ödemiş ve bunları gider yazmıştır.\n\n{K}, bu ödemelerin matrahın "
    "tespitine etkisine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Ödemelerin tamamı matrahtan ve gelir unsurlarından indirilemeyecek giderdir.",
    ["Sadece gecikme zammı işletmeyle ilgili olduğundan indirilebilir.",
     "Trafik para cezası işletme aracıyla ilgiliyse indirilebilir, diğerleri indirilemez.",
     "Tamamı işletmeyle ilgili olduğundan ticari kazançtan indirilebilir.",
     "Vergi ziyaı cezası indirilebilir, para cezası ve gecikme zammı indirilemez."],
    "Md. 90'a göre gelir vergisi ve diğer şahsi vergiler ile her ne şekilde olursa olsun vergi cezaları, para cezaları ve "
    "6183 sayılı Kanuna göre ödenen cezalar, gecikme zamları ve faizler matrahtan ve gelir unsurlarından indirilemez.")

v2 = gv2025(2_000_000)
P.sayisal("GVK md. 103, 121, mük. 120",
    f"{TARIFE_2025}\n\nTicari kazanç sahibi Bayan (L)’nin 2025 yılı gelir vergisi matrahı 2.000.000 ₺’dir. Yıl içinde "
    "toplam 280.000 ₺ geçici vergi ödemiş, kazancına dahil bir hakediş üzerinden de 40.000 ₺ tevkifat yapılmıştır. "
    f"\n\n{K}, Bayan (L)’nin yıllık beyanname üzerinden ödeyeceği gelir vergisi kaç ₺’dir?",
    tl(v2 - 280_000 - 40_000), secenekler(v2 - 320_000, v2 - 280_000, v2 - 40_000, v2, gv2025(2_000_000, True) - 320_000),
    "Hesaplanan vergi: 185.000 + 1.200.000 × %35 = 605.000 ₺. Mük. 120'ye göre geçici vergi, md. 121'e göre tevkifat "
    "mahsup edilir: 605.000 − 280.000 − 40.000 = 285.000 ₺.", zorluk="medium")

P.q("GVK md. 22/3",
    f"{K}, tam mükellef kurumlardan elde edilen kâr paylarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kâr payının istisna edilen yarısından tevkifat yapılmaz; sadece vergiye tabi yarısından kesilir.",
    ["Tam mükellef kurumlardan elde edilen kâr paylarının yarısı gelir vergisinden müstesnadır.",
     "Kâr payı beyan edilirse tevkif edilen verginin tamamı beyanname üzerinden hesaplanan vergiden mahsup edilir.",
     "İstisna, kâr payının beyanname verilmesini gerektirip gerektirmediğinin tespitinde de dikkate alınır.",
     "Kâr payının vergiye tabi yarısı beyan sınırını aşarsa yıllık beyannameyle bildirilir."],
    "Md. 22/3'e göre kâr paylarının yarısı istisnadır; istisna edilen tutar üzerinden de md. 94 uyarınca tevkifat yapılır ve "
    "kâr payı beyan edilirse tevkif edilen verginin tamamı mahsup edilir.")

P.q("GVK md. 63",
    f"{K}, ücretin gerçek safi değerinin tespitinde brüt ücretten indirilecekler arasında aşağıdakilerden hangisi "
    "yer almaz?",
    "Hizmet erbabının kendi adına ödediği kira bedeli",
    ["Kanunla kurulan emekli sandıklarına ödenen aidat ve primler",
     "Ordu Yardımlaşma Kurumu ve benzeri kamu kurumları için yapılan kanuni kesintiler",
     "Kanunda belirtilen sınırlar içinde hizmet erbabının ödediği şahıs sigorta primleri",
     "Sendikalara ödenen aidatlar"],
    "Md. 63'e göre ücretin safi değeri; OYAK ve benzeri kurumlar için kanuni kesintiler, kanunla kurulan emekli "
    "sandıklarına ödenen aidat ve primler, sınırlar dahilinde şahıs sigorta primleri ve sendika aidatları düşülerek bulunur. Hizmet "
    "erbabının kira gideri indirilmez.")

bg = 2_400_000
m = bg - min(500_000, bg * 0.05) - 150_000
P.sayisal("GVK md. 89/1-4, 89/1-5",
    "Serbest meslek erbabı Bay (M)’nin 2025 yılında beyan ettiği kazanç 2.400.000 ₺’dir. Bay (M) aynı yıl kalkınmada öncelikli "
    "yöre dışındaki bir belediyeye makbuz karşılığı 500.000 ₺ nakdi bağışta bulunmuş, ayrıca başka bir belediyenin "
    "yaptırdığı okul inşaatı için 150.000 ₺ bağış yapmıştır.\n\n"
    f"{K}, Bay (M)’nin 2025 yılı gelir vergisi matrahı kaç ₺’dir?",
    tl(m), secenekler(m, bg - 500_000 - 150_000, bg - 120_000, bg - 650_000 * 0.05, bg - 500_000, bg - 240_000 - 150_000),
    "Md. 89/1-4'e göre belediyelere yapılan bağışlar beyan edilen gelirin %5'i (120.000 ₺) ile sınırlıdır. Md. 89/1-5'e "
    "göre belediyelere bağışlanan okul inşaatı için yapılan bağışların tamamı (150.000 ₺) indirilir: 2.400.000 − 120.000 "
    "− 150.000 = 2.130.000 ₺.", zorluk="hard")

P.q("GVK md. 21, 86/1-a",
    "Emekli Bayan (N)’nin 2025 yılındaki tek geliri, bir konutunu kiraya vermesinden elde ettiği 45.000 ₺ kira "
    f"hasılatıdır. {KIRA_IST}\n\n{K}, Bayan (N)’nin bu gelir için yükümlülüğüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "Hasılat istisna tutarını aşmadığından beyanname vermez.",
    ["Hasılatın %15 götürü gider düşülmüş tutarı için beyanname verir.",
     "İstisnadan yararlanmak için beyanname vermesi şarttır.",
     "Emekli olduğu için istisnadan yararlanamaz ve tamamını beyan eder.",
     "Kira geliri tevkifata tabi olmadığından muhtasar beyanname verir."],
    "Md. 21'e göre konut kira hasılatının istisna tutarı (47.000 ₺) kadar kısmı istisnadır; md. 86/1-a'ya göre istisna "
    "hadleri içinde kalan kazanç ve iratlar için beyanname verilmez.", zorluk="easy")

P.q("GVK md. 86/2",
    "Almanya’da yerleşik dar mükellef Bay (P), 2025 yılında Türkiye’de bir şirkete verdiği danışmanlık hizmeti karşılığı "
    f"serbest meslek kazancı elde etmiş, ödemelerin tamamı Türkiye’de tevkif suretiyle vergilendirilmiştir.\n\n{K}, Bay "
    "(P)’nin bu kazanç için beyan yükümlülüğüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "Tamamı Türkiye’de tevkif suretiyle vergilendirildiğinden yıllık beyanname vermez.",
    ["Dar mükellefler Türkiye’deki kazançlarını yıllık beyannameyle bildirir.",
     "Kazancın yarısı istisna, kalanı yıllık beyannameyle beyan edilir.",
     "Sadece dördüncü dilim tutarını aşan kısım beyan edilir.",
     "Bay (P) Almanya’da vergilendirileceği için Türkiye’de tevkifat yapılmaz."],
    "Md. 86/2'ye göre dar mükellefiyette tamamı Türkiye'de tevkif suretiyle vergilendirilmiş ücretler, serbest meslek "
    "kazançları, menkul ve gayrimenkul sermaye iratları ile diğer kazanç ve iratlar için beyanname verilmez.")

# ================================================================ ek hesap soruları
m = 500_000 * 0.85 + 300_000 * 0.85
P.sayisal("GVK md. 74, 86/1-c",
    "Bay (R)’nin 2025 yılında tevkifata tabi tutulmuş gelirleri şunlardır: iki ayrı kiracıdan aldığı işyeri kira gelirleri "
    "500.000 ₺ ve 300.000 ₺ (brüt). Başka geliri yoktur; götürü gider yöntemini seçmiştir. (2025 yılı için tarifenin ikinci "
    f"gelir dilimindeki tutar 330.000 ₺’dir.)\n\n{K}, Bay (R)’nin beyan edeceği safi kira geliri kaç ₺’dir?",
    tl(m), secenekler(m, 800_000, 500_000 * 0.85, 800_000 - 330_000, 0),
    "Md. 86/1-c'ye göre tevkifata tabi gayrimenkul sermaye iratlarının toplamı (800.000 ₺) ikinci dilim tutarını aştığından "
    "beyan edilir. Md. 74'e göre %15 götürü gider düşülür: 800.000 × 0,85 = 680.000 ₺; tevkif edilen vergiler mahsup edilir.")

v = gv2025(1_500_000)
P.sayisal("GVK md. 103",
    f"{TARIFE_2025}\n\nSerbest meslek erbabı Bay (S)’nin 2025 yılı gelir vergisi matrahı 1.500.000 ₺’dir. {K}, Bay (S) için "
    "hesaplanan gelir vergisi kaç ₺’dir?",
    tl(v), secenekler(v, gv2025(1_500_000, True), 1_500_000 * 0.35, 1_500_000 * 0.27, 185_000 + 1_500_000 * 0.35),
    "Ücret dışı gelirde 800.000 ₺ için 185.000 ₺, aşan 700.000 ₺ için %35 = 245.000 ₺; toplam 430.000 ₺.", zorluk="easy")

vu = gv2025(1_500_000, True)
P.sayisal("GVK md. 103",
    f"{TARIFE_2025}\n\nBayan (T)’nin 2025 yılında beyan etmesi gereken ve tek kaynağı ücret olan gelir vergisi matrahı "
    f"1.500.000 ₺’dir. {K}, Bayan (T) için yıllık beyanname üzerinden hesaplanan gelir vergisi (mahsuplardan önce) kaç "
    "₺’dir?",
    tl(vu), secenekler(vu, gv2025(1_500_000), 1_500_000 * 0.27, 58_100 + 1_170_000 * 0.27, 1_500_000 * 0.35),
    "Ücret gelirlerinde 1.200.000 ₺ için 293.000 ₺, aşan 300.000 ₺ için %35 = 105.000 ₺; toplam 398.000 ₺. Ücret dışı "
    "tarife uygulansaydı 430.000 ₺ bulunurdu.")

# ================================================================ olumsuz karma
P.q("GVK md. 86/1-c",
    f"{K}, md. 86/1-c kapsamında beyan edilmeyecek gelirlere ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tevkifatsız gayrimenkul sermaye iratları da bu bent kapsamındadır.",
    ["Bent, Türkiye’de tevkifata tabi tutulmuş gelirleri kapsar.",
     "Birden fazla işverenden elde edilen ücretler bu bentte sayılan gelirlerdendir.",
     "Vergiye tabi gelir toplamının ikinci dilim tutarını aşmaması şarttır.",
     "Hesaplamada (a) ve (b) bentlerinde belirtilen gelirler dikkate alınmaz."],
    "Md. 86/1-c, (a) ve (b) bentlerindekiler hariç vergiye tabi gelir toplamı ikinci dilim tutarını aşmamak koşuluyla "
    "Türkiye'de tevkifata tabi tutulmuş birden fazla işverenden alınan ücretler, menkul ve gayrimenkul sermaye iratlarını "
    "beyan dışında bırakır. Tevkifatsız iratlar (d) bendinde ayrıca düzenlenir.", zorluk="hard")

P.q("GVK md. 18",
    f"{K}, telif kazançları istisnasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İstisna kapsamındaki ödemeler üzerinden, kazanç toplamı ne olursa olsun tevkifat yapılmaz.",
    ["Eserlerin neşir, temsil, icra ve teşhir gibi suretlerle değerlendirilmesi karşılığı alınan bedeller istisnaya dahildir.",
     "Kazançların arızi olarak elde edilmesi istisnanın uygulanmasına engel değildir.",
     "Bu kapsamdaki kazançlar toplamı dördüncü dilim tutarını aşanlar istisnadan faydalanamaz.",
     "Bilgisayar programcılarının yazılım satışından elde ettikleri hasılat istisna kapsamındadır."],
    "Md. 18'e göre istisna, md. 94 uyarınca tevkif suretiyle ödenecek vergiyi kapsamaz; yani istisna kapsamındaki "
    "ödemelerden tevkifat yapılır. Kazanç toplamı dördüncü dilimi aşanlar istisnadan yararlanamaz ve bunlar için tevkifat "
    "yükümlülüğü aranmaz.", zorluk="hard")

P.q("GVK md. 92, 85",
    f"{K}, yıllık beyannameye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ticari faaliyetinden kazanç elde etmeyen tacir o yıl için yıllık beyanname vermez.",
    ["Beyanı gereken gelirlerin yıllık beyannamede toplanması zorunludur.",
     "Kollektif şirket ortakları şirketin tasfiye döneminde de yıllık beyanname verir.",
     "Serbest meslek erbabı kazanç temin etmemiş olsa bile yıllık beyanname verir.",
     "Dar mükellefiyette vergi muhatabı varsa beyanname onun oturduğu yer vergi dairesine verilir."],
    "Md. 85'e göre tacirler, çiftçiler ve serbest meslek erbabı faaliyetlerinden kazanç temin etmemiş olsalar bile yıllık "
    "beyanname verir; bu hüküm kollektif şirket ortakları ve komanditeler için tasfiye dönemini de kapsar. Md. 92 dar "
    "mükellefiyette beyannamenin verileceği yeri düzenler.")

P.q("GVK mük. 120",
    "Bay (U) 2025 yılının Haziran ayında ticari faaliyetini bırakmış ve işi terk ettiğini vergi dairesine bildirmiştir. "
    f"{K}, Bay (U)’nun 2025 yılı geçici vergi yükümlülüğüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "İşin bırakıldığı dönemi izleyen dönemlerde geçici vergi ödenmez.",
    ["Yıl sonuna kadar kalan tüm dönemler için geçici vergi beyannamesi vermeye devam eder.",
     "İşi bıraktığı dönem dahil o yıl geçici vergi ödemez.",
     "İşi bıraktığı dönemin geçici vergisi yıllık beyannameyle birlikte ödenir.",
     "Kalan dönemler için geçici vergi, önceki dönem ortalamasına göre re’sen tarh edilir."],
    "Mük. 120'ye göre işin bırakılması hâlinde, işin bırakıldığı dönemi izleyen dönemlerde geçici vergi ödenmez.")

# ================================================================ bir hesap sorusu daha
bg = 1_600_000
m = bg - min(250_000, bg * 0.10) - min(120_000, bg * 0.05)
P.sayisal("GVK md. 89/1-2, 89/1-4",
    "Tüccar Bayan (V)’nin 2025 yılında beyan ettiği ticari kazanç 1.600.000 ₺’dir. Bayan (V) aynı yıl kendisi ve eşi için "
    "Türkiye’deki özel hastanelerde belgelendirilmiş 250.000 ₺ sağlık harcaması yapmış; kalkınmada öncelikli yöre dışında "
    "kamu yararına çalışan bir derneğe makbuz karşılığı 120.000 ₺ bağışta bulunmuştur.\n\n"
    f"{K}, Bayan (V)’nin 2025 yılı gelir vergisi matrahı kaç ₺’dir?",
    tl(m), secenekler(m, bg - 250_000 - 120_000, bg - 160_000 - 120_000, bg - 250_000 - 80_000, bg - 160_000),
    "Md. 89/1-2'ye göre sağlık harcaması beyan edilen gelirin %10'u (160.000 ₺), md. 89/1-4'e göre bağış %5'i (80.000 ₺) "
    "ile sınırlıdır: 1.600.000 − 160.000 − 80.000 = 1.360.000 ₺.")

# ================================================================ ek olumsuz sorular
P.q("GVK md. 106",
    f"{K}, gelir vergisinin tarh yerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tam mükellefin gelir vergisi, kazancın en yüksek olduğu yerin vergi dairesince tarh edilir.",
    ["Gelir vergisi kural olarak mükellefin ikametgâhının bulunduğu yer vergi dairesince tarh edilir.",
     "İş yeri ve ikametgâhı ayrı vergi daireleri bölgesinde olanların vergisi, Bakanlıkça uygun görülür ve önceden bildirilirse iş yerinin bulunduğu yerde tarh edilebilir.",
     "Dar mükelleflerin vergisi, beyannamelerini vermeye mecbur oldukları yerin vergi dairesince tarh edilir.",
     "Gezici olarak çalışanların vergisi, ikametgâhlarında tarh edilmemişse faaliyet yerlerinde tarh edilir."],
    "Md. 106'ya göre gelir vergisi mükellefin ikametgâhının bulunduğu yer vergi dairesince tarh edilir; iş yeri ayrı "
    "bölgede olanlar, gezici çalışanlar ve dar mükellefler için özel tarh yerleri öngörülür. Kazancın büyüklüğü tarh yerini "
    "belirlemez.")

P.q("GVK md. 89/1-1",
    f"{K26}, beyan edilen gelirden indirilebilecek sigorta primlerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Merkezi yurt dışında bulunan bir sigorta şirketine ödenen şahıs sigorta primleri de indirilebilir.",
    ["Hayat sigortası primlerinin %50’si indirim hesabına katılır.",
     "Primlerin gelirin elde edildiği yılda ödenmiş olması gerekir.",
     "İndirim, beyan edilen gelirin %15’ini ve asgari ücretin yıllık tutarını aşamaz.",
     "Eş veya çocuklar ayrı beyanname veriyorsa onlara ait primler kendi gelirlerinden indirilir."],
    "Md. 89/1-1'e göre sigortanın Türkiye'de kâin ve merkezi Türkiye'de bulunan bir emeklilik veya sigorta şirketi "
    "nezdinde akdedilmiş olması şarttır. Hayat sigortasında %50, %15 ve asgari ücret sınırı, primlerin o yıl ödenmesi ve "
    "ayrı beyanname hâli maddede düzenlenir.")

P.q("GVK md. 74/1-10",
    "Bay (R) sahibi olduğu daireyi konut olarak kiraya vermiş, kendisi ise ailesiyle birlikte kira ödeyerek başka bir "
    f"konutta oturmaktadır. Gerçek gider yöntemini seçmiştir.\n\n{K}, Bay (R)’nin safi kira gelirinin tespitine ilişkin "
    "aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kiracı olarak oturduğu konut için ödediği kira bedeli gider olarak indirilemez.",
    ["Kiraya verdiği konut için ödediği emlak vergisi indirilebilir.",
     "Kiraya verdiği konuta yaptırdığı onarım gideri indirilebilir.",
     "Oturduğu konutun kira bedeli, diğer giderler düşüldükten sonra kalan tutardan indirilir.",
     "Kira indiriminin indirilemeyen kısmı gider fazlalığı sayılmaz."],
    "Md. 74/1-10'a göre sahibi bulundukları konutları kiraya verenlerin kira ile oturdukları konutun kira bedeli, diğer "
    "giderler düşüldükten sonra kalan miktardan indirilebilir; indirilemeyen kısım md. 88'deki gider fazlalığı sayılmaz.")

P.q("GVK md. 31",
    f"{K26}, engellilik derecelerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Çalışma gücünün %60’ını kaybeden hizmet erbabı üçüncü derece engelli sayılır.",
    ["Çalışma gücünün asgari %80’ini kaybeden hizmet erbabı birinci derece engelli sayılır.",
     "Çalışma gücünün asgari %40’ını kaybeden hizmet erbabı üçüncü derece engelli sayılır.",
     "Engellilik indirimi, derecelere göre belirlenen aylık tutarlar olarak ücretten indirilir.",
     "Engellilik derecelerinin tespitine ilişkin usuller yönetmelikle belirlenir."],
    "Md. 31'e göre çalışma gücünün asgari %80'ini kaybeden birinci, asgari %60'ını kaybeden ikinci, asgari %40'ını "
    "kaybeden üçüncü derece engelli sayılır; indirim aylık tutarlar olarak uygulanır ve tespit usulleri yönetmelikle "
    "belirlenir.", zorluk="easy")

P.q("GVK md. 86/1-b",
    f"{K}, birden fazla işverenden ücret alanların beyan durumuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "İkinci işverenden alınan ücret ikinci dilim tutarını aşsa da toplam ücret dördüncü dilimi aşmıyorsa beyan edilmez.",
    ["Ücretlerin tamamının tevkif suretiyle vergilendirilmiş olması gerekir.",
     "Birinciden sonraki işverenlerden alınan ücretlerin toplamının ikinci dilim tutarını aşmaması gerekir.",
     "Birinci işverenden alınan dahil ücret toplamının dördüncü dilim tutarını aşmaması gerekir.",
     "Şartlar sağlanırsa ücretler için yıllık beyanname verilmez."],
    "Md. 86/1-b'ye göre birden fazla işverenden ücret alanlarda beyan dışında kalma için ücretlerin tamamının tevkifata "
    "tabi olması, ikinciden sonraki işverenlerden alınanların toplamının ikinci dilim ve toplam ücretin dördüncü dilim "
    "tutarını aşmaması birlikte aranır.", zorluk="hard")

P.q("GVK mük. 120",
    "Serbest meslek erbabı Bayan (S)’ye yapılan ödemelerden 2025 yılının ikinci üç aylık döneminde 30.000 ₺ gelir vergisi "
    f"tevkif edilmiştir.\n\n{K}, bu tevkifatın geçici vergi hesabındaki etkisine ilişkin aşağıdaki ifadelerden hangisi "
    "yanlıştır?",
    "Tevkif edilen vergi geçici vergiden mahsup edilemez; sadece yıllık beyannamede dikkate alınır.",
    ["Aynı dönem içinde tevkif edilen gelir vergisi hesaplanan geçici vergiden mahsup edilir.",
     "Md. 42 kapsamındaki kazançlardan yapılan tevkifat geçici vergiden mahsup edilmez.",
     "Geçici vergi, ilgili dönemi izleyen ikinci ayın on yedinci günü akşamına kadar ödenir.",
     "Geçici vergi matrahında VUK’un değerlemeye ait hükümleri dikkate alınır."],
    "Mük. 120'ye göre aynı dönem içinde tevkif edilen gelir vergisi (md. 42 kazançlarından yapılan tevkifat hariç) "
    "hesaplanan geçici vergiden mahsup edilir; geçici vergi izleyen ikinci ayın 17'si akşamına kadar ödenir ve matrahta "
    "değerleme hükümleri uygulanır.")

P.q("GVK md. 21/2",
    f"{K}, konut kira geliri istisnasından yararlanamayanların tespitine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Gelir toplamının hesabında sadece beyanı gereken ücret ve iratlar dikkate alınır.",
    ["Ticari, zirai veya mesleki kazancını yıllık beyannameyle bildirmekle yükümlü olanlar yararlanamaz.",
     "Ücret, menkul ve gayrimenkul sermaye iratlarının gayrisafi tutarları toplamı dikkate alınır.",
     "Karşılaştırmada tarifenin üçüncü diliminde ücret gelirleri için yer alan tutar esas alınır.",
     "Bu gelirler ayrı ayrı veya birlikte elde edilmiş olabilir."],
    "Md. 21/2'ye göre ticari, zirai veya mesleki kazancını beyan etmekle yükümlü olanlar ile ücret, menkul ve gayrimenkul "
    "sermaye iratları ve diğer kazançlarının gayrisafi toplamı üçüncü dilimin ücret tutarını aşanlar, beyanı gerekip "
    "gerekmediğine bakılmaksızın istisnadan yararlanamaz.", zorluk="hard")

P.q("GVK md. 86/1-d",
    f"{K}, md. 86/1-d kapsamındaki beyan sınırına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Sınır, tevkifata tabi tutulmuş mevduat faizleri için de uygulanır ve toplam hesabına katılır.",
    ["Bent, tevkifata ve istisna uygulamasına konu olmayan iratları kapsar.",
     "Menkul ve gayrimenkul sermaye iratlarının toplamı dikkate alınır.",
     "Toplamın kanunda belirtilen tutarı aşmaması hâlinde beyanname verilmez.",
     "Tutar bir takvim yılı içinde elde edilen iratlar esas alınarak hesaplanır."],
    "Md. 86/1-d'ye göre bir takvim yılında elde edilen ve toplamı kanundaki tutarı aşmayan, tevkifata ve istisna "
    "uygulamasına konu olmayan menkul ve gayrimenkul sermaye iratları için beyanname verilmez. Tevkifata tabi iratlar bu "
    "bendin değil (c) bendinin konusudur.", zorluk="hard")

if __name__ == "__main__":
    sys.exit(P.yaz())
