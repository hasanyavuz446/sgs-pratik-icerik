# -*- coding: utf-8 -*-
"""Vergi Mevzuatı ve Uygulaması · Bölüm Havuzu — 3 test × 20 soru, gerçek test kitapçığı düzeninde.

Her test 2026/1-2026/2 kitapçıklarının ağırlığını izler: GVK ~5, KVK ~4, KDVK ~4, VUK (ödev, ceza) ~3, 6183 ve
uyuşmazlık ~2, diğer vergiler (Damga, VİV, Emlak, ÖTV, MTV) ~2; yaklaşık %40'ı hesaplamalıdır. Konu havuzundaki kökler
tekrar edilmez; aynı hüküm farklı olay ve rakamla ölçülür. Dayanaklar konu builder'larıyla aynıdır (build_yk_*.py
başlıklarına bkz.); 29.09.2026 kontrolü. Yıla bağlı tutarlar kökte verilir; hesaplar vergi_ortak.py ile yapılır.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler, gv2025, TARIFE_2025

SURUM = ("GVK, KVK (7582 dahil), KDVK (7577 dahil), VUK (7524, 7587 dahil), 6183, İYUK, DVK, VİVK, EVK, MTVK, ÖTVK "
         "güncel metinleri; 29.09.2026 kontrolü")

def paket(dosya, seed, ek=()):
    return Paket(dosya, lesson="vergi_usul_kanunu", topic="vergilendirme_sureci",
                 konu_adi="Vergi Mevzuatı ve Uygulaması", seed=seed, surum=SURUM, havuz="bolum", ek_idler=ek)

G = "193 sayılı Gelir Vergisi Kanunu’na göre"
G26 = "193 sayılı Gelir Vergisi Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"
KV = "5520 sayılı Kurumlar Vergisi Kanunu’na göre"
KV26 = "5520 sayılı Kurumlar Vergisi Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"
KD = "3065 sayılı Katma Değer Vergisi Kanunu’na göre"
V = "213 sayılı Vergi Usul Kanunu’na göre"
V26 = "213 sayılı Vergi Usul Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"
A = "6183 sayılı Amme Alacaklarının Tahsil Usulü Hakkında Kanun’a göre"
DA = "488 sayılı Damga Vergisi Kanunu’na göre"
VI = "7338 sayılı Veraset ve İntikal Vergisi Kanunu’na göre"
EM = "1319 sayılı Emlak Vergisi Kanunu’na göre"
OT = "4760 sayılı Özel Tüketim Vergisi Kanunu’na göre"
I = "2577 sayılı İdari Yargılama Usulü Kanunu’na göre"
ORAN = "(KDV oranı %20 olarak alınacaktır.)"
SINIR = ("(2025 yılı için gelir vergisi tarifesinin ikinci gelir dilimi tutarı 330.000 ₺, dördüncü gelir dilimi tutarı "
         "4.300.000 ₺ olarak alınacaktır.)")

GV, KVG, KDV, VUK, VH, TVS = ("gelir_vergisi", "kurumlar_vergisi", "katma_deger_vergisi", "vergi_usul_kanunu",
                              "vergi_hukuku", "turk_vergi_sistemi")

ek1 = [f"demo-vergi-{n:03d}" for n in range(21, 33)]

# =============================================================================== TEST 1
T1 = paket("questions_vergi_2026.json", 2026092951, ek1)

u1 = 3_500_000 + 450_000
T1.sayisal("GVK md. 86",
    "Tam mükellef Bay (K) 2025 yılında iki işverenden ücret almış ve ücretlerinin tamamı tevkif suretiyle vergilendirilmiştir. "
    "Birinci işverenden aldığı safi ücret 3.500.000 ₺, ikinci işverenden aldığı safi ücret 450.000 ₺’dir. Başka geliri "
    f"yoktur. {SINIR}\n\n{G}, Bay (K)’nın 2025 yılı beyannamesine dahil edeceği ücret toplamı kaç ₺’dir?",
    tl(u1), secenekler(u1, 0, 450_000, 3_500_000, 4_300_000),
    "Md. 86/1-b'ye göre birden fazla işverenden ücret alanlarda birinciden sonraki ücretlerin toplamı ikinci dilim tutarını ve "
    "ücretlerin toplamı dördüncü dilim tutarını aşmıyorsa beyan gerekmez. İkinci işverenden alınan 450.000 ₺ ikinci dilim "
    "tutarını aştığından ücretlerin tamamı (3.950.000 ₺) beyan edilir.", lesson=GV, topic="beyan_ve_tespit", zorluk="hard")

gm1 = 600_000 * 0.85
T1.sayisal("GVK md. 70, 74",
    "Bayan (L), 2025 yılında sahibi olduğu dükkânı bir şirkete işyeri olarak kiralamış ve brüt 600.000 ₺ kira elde etmiştir. "
    "Kira ödemeleri üzerinden tevkifat yapılmıştır. Bayan (L) safi iradın tespitinde götürü gider yöntemini seçmiştir; başka "
    f"geliri yoktur.\n\n{G}, Bayan (L)’nin 2025 yılı safi gayrimenkul sermaye iradı kaç ₺’dir?",
    tl(gm1), secenekler(gm1, 600_000, 600_000 * 0.75, 600_000 * 0.80, 600_000 * 0.70),
    "Md. 74'e göre götürü gider yönteminde gayrisafi hasılatın %15'i gider olarak indirilir; işyeri kirasına md. 21'deki "
    "konut istisnası uygulanmaz: 600.000 × 0,85 = 510.000 ₺.", lesson=GV, topic="gelir_unsurlari")

T1.q("GVK md. 94",
    "Bir vergi dairesi, bölgesindeki kişi ve kuruluşların yaptıkları ödemelerden gelir vergisi tevkifatı yapmakla yükümlü "
    f"olup olmadıklarını incelemektedir.\n\n{G}, aşağıdakilerden hangisi tevkifat yapmakla yükümlü olanlar arasında yer "
    "almaz?",
    "Kazancı basit usulde tespit edilen esnaf",
    ["Ticaret şirketleri", "Dernek ve vakıfların iktisadi işletmeleri",
     "Gerçek gelirlerini beyan etmeye mecbur serbest meslek erbabı",
     "Zirai kazancını bilanço esasına göre tespit eden çiftçiler"],
    "Md. 94'e göre kamu idareleri, ticaret şirketleri, iş ortaklıkları, dernek ve vakıflar ile bunların iktisadi işletmeleri, "
    "gerçek gelirlerini beyana mecbur ticaret ve serbest meslek erbabı ile zirai kazancını bilanço veya zirai işletme hesabı "
    "esasına göre tespit eden çiftçiler tevkifat yapar. Basit usul mükellefleri sayılmamıştır.", lesson=GV,
    topic="beyan_ve_tespit")

T1.q("GVK mük. 120",
    "Serbest muhasebeci mali müşavir Bayan (M), 2026 yılının ikinci geçici vergi dönemine ilişkin yükümlülüklerini "
    f"planlamaktadır.\n\n{G26}, geçici vergiye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Yıllara yaygın inşaat kazançları da geçici vergi matrahına dahil edilir.",
    ["Geçici vergi üçer aylık dönem kazançları üzerinden hesaplanır.",
     "Oran tarifenin ilk gelir dilimine uygulanan orandır.",
     "Beyan dönemi izleyen ikinci ayın on dördüncü günü akşamına kadar yapılır.",
     "Hesaplanan geçici vergi, cari yılın gelir vergisinden mahsup edilir."],
    "Mük. 120'ye göre ticari kazanç sahipleri ve serbest meslek erbabı üçer aylık dönem kazançları üzerinden ilk dilim "
    "oranında geçici vergi öder; beyan izleyen ikinci ayın 14'ü, ödeme 17'si akşamına kadardır. Md. 42 kapsamındaki yıllara "
    "yaygın inşaat kazançları geçici vergi matrahına dahil edilmez.", lesson=GV, topic="beyan_ve_tespit", zorluk="hard")

T1.q("GVK md. 88",
    "Tüccar Bay (N), 2020 yılında büyük bir ticari zarar etmiş ve bu zararı sonraki yıllarda kısmen mahsup edebilmiştir."
    f"\n\n{G}, zarar mahsubuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Mahsup edilemeyen zararlar süre sınırı olmaksızın sonraki yıllara devreder.",
    ["Ticari faaliyetten doğan zarar diğer gelir unsurlarından mahsup edilebilir.",
     "Mahsup edilemeyen zarar beş yıl süreyle sonraki yıllara devredebilir.",
     "Türkiye’de istisna edilen kazançlarla ilgili yurt dışı zararlar mahsup edilmez.",
     "Zararların mahsubu yıllık beyanname üzerinde yapılır."],
    "Md. 88'e göre gelir unsurlarından doğan zararlar diğer unsurların kazanç ve iratlarından indirilir; kapatılamayan zararlar "
    "beş yıldan fazla nakledilmemek şartıyla sonraki yılların gelirinden indirilir.", lesson=GV, topic="beyan_ve_tespit")

yd1 = 6_000_000 - 2_000_000 * 0.50
T1.sayisal("KVK md. 5/1-b",
    "Tam mükellef (ABC) A.Ş., Hollanda’daki bir limited şirketin ödenmiş sermayesinin %60’ına sahiptir. Şirket 2025 yılında bu "
    "iştirakinden 2.000.000 ₺ kâr payı almış ve beyanname verme süresi içinde Türkiye’ye transfer etmiştir; iştirakin vergi "
    "yükü şartı sağlanmamaktadır. Kâr payı dahil ticari bilanço kârı 6.000.000 ₺’dir; başka düzeltme yoktur."
    f"\n\n{KV26}, (ABC) A.Ş.’nin 2025 hesap dönemi kurumlar vergisi matrahı kaç ₺’dir?",
    tl(yd1), secenekler(yd1, 6_000_000, 4_000_000, 6_000_000 - 1_500_000, 5_500_000),
    "Md. 5/1-b'ye eklenen hükme göre yurt dışı iştirakin ödenmiş sermayesinin en az %50'sine sahip olunması ve kazancın "
    "beyanname süresine kadar transferi şartıyla, diğer şartlar aranmaksızın iştirak kazancının %50'si istisnadır: "
    "6.000.000 − 1.000.000 = 5.000.000 ₺.", lesson=KVG, topic="kurum_kazanci", zorluk="hard")

fg1 = 2_000_000 * 6 / 10 * 0.10
T1.sayisal("KVK md. 11/1-i",
    "Mobilya üreticisi (DEF) A.Ş.’nin 2025 hesap dönemi sonunda öz kaynakları 4.000.000 ₺, kullandığı yabancı kaynakları "
    "10.000.000 ₺’dir. Yatırım maliyetine eklenmeyen finansman giderleri 2.000.000 ₺’dir. (Cumhurbaşkanınca belirlenen oran "
    f"%10 olarak alınacaktır.)\n\n{KV}, (DEF) A.Ş.’nin finansman gideri kısıtlaması nedeniyle kanunen kabul edilmeyen gider "
    "olarak dikkate alacağı tutar kaç ₺’dir?",
    tl(fg1), secenekler(fg1, 200_000, 1_200_000, 80_000, 60_000),
    "Md. 11/1-i'ye göre yabancı kaynakların öz kaynakları aşan kısmına (6.000.000 ₺) isabet eden finansman gideri "
    "2.000.000 × 6/10 = 1.200.000 ₺'dir; bunun %10'u olan 120.000 ₺ indirilemez.", lesson=KVG, topic="kurum_kazanci",
    zorluk="hard")

T1.q("KVK md. 5/1-a",
    "Tam mükellef (GHI) A.Ş., 2025 yılının Kasım ayında satın aldığı tam mükellef (JKL) A.Ş. hisselerinden aynı yılın Aralık "
    f"ayında kâr payı almıştır; payı %2’dir.\n\n{KV}, bu kâr payına iştirak kazançları istisnası uygulanmasına ilişkin "
    "aşağıdakilerden hangisi doğrudur?",
    "Elde tutma süresi ve iştirak oranı aranmadan istisnadır.",
    ["Hisse bir yıl elde tutulmadığından istisna uygulanmaz.",
     "İştirak oranı %10’un altında olduğundan istisna uygulanmaz.",
     "Kâr payının sadece %75’i istisnadır.",
     "İstisna ancak kâr payı sermayeye eklenirse uygulanır."],
    "Md. 5/1-a'ya göre tam mükellef kurumların sermayesine katılımdan elde edilen kâr payları istisnadır; yurt dışı iştiraklerden "
    "farklı olarak elde tutma süresi veya asgari iştirak oranı şartı yoktur.", lesson=KVG, topic="kurum_kazanci")

T1.q("KVK md. 14",
    "Hesap dönemi takvim yılı olan (MNO) A.Ş., 2025 hesap dönemine ait kurumlar vergisi beyannamesini hazırlamaktadır; "
    f"şirkete özel hesap dönemi tayin edilmemiştir.\n\n{KV}, beyanname hangi süre içinde verilmelidir?",
    "1-25 Nisan 2026 tarihleri arasında",
    ["1-31 Mart 2026 tarihleri arasında",
     "1-25 Şubat 2026 tarihleri arasında",
     "1-30 Mayıs 2026 tarihleri arasında",
     "1-26 Ocak 2026 tarihleri arasında"],
    "Md. 14/3'e göre kurumlar vergisi beyannamesi hesap döneminin kapandığı ayı izleyen dördüncü ayın birinci gününden "
    "yirmi beşinci günü akşamına kadar verilir; Aralık'ı izleyen dördüncü ay Nisan'dır.", lesson=KVG,
    topic="kurumlar_mukellefiyeti", zorluk="easy")

kd1 = 1_200_000 * 0.20 - (180_000 - 40_000)
T1.sayisal("KDVK md. 29, 30",
    "Tekstil toptancısı (PRS) A.Ş.’nin 2026/Nisan dönemi işlemleri: yurt içi teslimler 1.200.000 ₺ (KDV hariç); kanuni "
    "defterlere kaydedilen alış faturalarındaki KDV toplamı 180.000 ₺ olup bunun 40.000 ₺’si şirket müdürünün kullanımı "
    "için satın alınan binek otomobile aittir; ayrıca depremde zayi olan ve KDV’si daha önce indirilmiş emtiaya ait 5.000 ₺ "
    f"KDV bulunmaktadır. {ORAN}\n\n{KD}, (PRS) A.Ş.’nin 2026/Nisan dönemi ödenecek KDV tutarı kaç ₺’dir?",
    tl(kd1), secenekler(kd1, 240_000 - 180_000, 105_000, 95_000, 140_000),
    "Hesaplanan KDV 1.200.000 × %20 = 240.000 ₺. Md. 30/b'ye göre binek otomobil KDV'si (40.000 ₺) indirilemez; md. 30/c'ye "
    "göre depremde zayi olan malların KDV'si için düzeltme gerekmez: 240.000 − 140.000 = 100.000 ₺.", lesson=KDV,
    topic="kdv_mekanizmasi", zorluk="hard")

te1 = min(1_500_000 * 0.20, (500_000 + 1_500_000) * 0.20 - 250_000)
T1.sayisal("KDVK md. 11/1-c",
    "İmalatçı (TUV) Ltd. Şti. 2026/Mayıs döneminde yurt içinde 500.000 ₺ normal teslim, ihracatçıya ihraç kaydıyla "
    f"1.500.000 ₺ teslim yapmıştır. Dönemin indirilecek KDV’si 250.000 ₺’dir. {ORAN}\n\n{KD}, şirketin 2026/Mayıs "
    "döneminde tecil edilecek KDV tutarı kaç ₺’dir?",
    tl(te1), secenekler(te1, 300_000, 400_000, 100_000, 250_000),
    "Tecil edilebilir KDV ihraç kaydıyla teslim bedeline isabet eden vergidir: 1.500.000 × %20 = 300.000 ₺. Ödenmesi gereken "
    "KDV (2.000.000 × %20) − 250.000 = 150.000 ₺; tecil edilecek KDV ikisinden küçük olan 150.000 ₺'dir.", lesson=KDV,
    topic="kdv_teslim_ve_indirim", zorluk="hard")

T1.q("KDVK md. 17/4-d",
    "Emekli Bay (P)’nin ticari işletmesi yoktur; sahibi olduğu bir daireyi konut olarak, bir dükkânı da işyeri olarak kiraya "
    f"vermiştir. Ayrıca bir ticaret şirketi, aktifindeki bir binayı kiraya vermiştir.\n\n{KD}, bu kiralamalardan hangileri "
    "KDV’den istisnadır?",
    "Bay (P)’nin iki kiralaması",
    ["Sadece Bay (P)’nin daire kiralaması",
     "Sadece şirketin bina kiralaması",
     "Kiralamaların tamamı",
     "Kiralamaların tamamı vergilidir"],
    "Md. 17/4-d'ye göre iktisadi işletmelere dahil olmayan gayrimenkullerin kiralanması istisnadır; bu istisna konut veya "
    "işyeri ayrımı yapmaz. Ticari işletmeye dahil binanın kiralanması KDV'ye tabidir.", lesson=KDV,
    topic="kdv_teslim_ve_indirim", zorluk="hard")

T1.q("KDVK md. 1/3-g",
    "Bir belediye, kendisine ait bir sosyal tesiste halka açık restoran işletmekte ve yemek satışı yapmaktadır."
    f"\n\n{KD}, bu satışların KDV karşısındaki durumuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Belediyelerin ticari nitelikteki teslimleri KDV’ye tabidir.",
    ["Belediyelerin tüm faaliyetleri KDV’den istisnadır.",
     "Satışlar kamu hizmeti olduğundan KDV’nin konusu dışındadır.",
     "Sadece belediye meclis kararı varsa KDV hesaplanır.",
     "KDV’yi restoranın müşterileri sorumlu sıfatıyla öder."],
    "Md. 1/3-g'ye göre belediyelere ait veya bunlarca işletilen müesseselerin ticari, sınai, zirai ve mesleki nitelikteki "
    "teslim ve hizmetleri KDV'ye tabidir.", lesson=KDV, topic="kdv_teslim_ve_indirim")

vz1 = 80_000 + 80_000 / 2
T1.sayisal("VUK md. 376",
    "(VYZ) A.Ş. adına ikmalen 80.000 ₺ vergi tarh edilmiş ve 80.000 ₺ vergi ziyaı cezası kesilmiştir. Şirket ihbarnamenin "
    "tebliğinden itibaren otuz gün içinde başvurarak vergiyi ve indirimli cezayı vadesinde ödeyeceğini bildirmiş ve "
    f"ödemiştir; dava açmamıştır.\n\n{V26}, şirketin ödediği toplam tutar kaç ₺’dir?",
    tl(vz1), secenekler(vz1, 160_000, 80_000, 100_000, 140_000),
    "Md. 376'ya göre vergi ve cezanın yarısını süresinde ödeyeceğini bildirip ödeyen mükellefin cezasının yarısı indirilir: "
    "80.000 + 40.000 = 120.000 ₺.", lesson=VUK, topic="vergi_cezalari")

T1.q("VUK md. 359",
    "Vergi incelemesinde, bir işletmenin ödeme kaydedici cihazının yetkisiz kişilerce mührünün kaldırıldığı ve yazılımının "
    f"satışları eksik gösterecek şekilde değiştirildiği tespit edilmiştir.\n\n{V}, bu fiile ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Fiil kaçakçılık suçudur.",
    ["Fiil sadece özel usulsüzlük cezasını gerektirir.",
     "Fiil ancak vergi ziyaı doğarsa cezalandırılır.",
     "Fiil ikinci derece usulsüzlüktür.",
     "Fiil için sadece cihazın satıcısı sorumludur."],
    "Md. 359/ç'ye göre Bakanlıkça yetkilendirilmediği hâlde ödeme kaydedici cihaz mührünü kaldıran, donanım veya yazılımını "
    "değiştirenler kaçakçılık suçu kapsamında hapis cezası ile cezalandırılır.", lesson=VUK, topic="vergi_cezalari",
    zorluk="hard")

T1.q("VUK md. 371",
    "Bay (R), 2025 yılı gelir vergisi beyannamesinde bir kira gelirini eksik beyan ettiğini, hakkında herhangi bir inceleme "
    f"veya ihbar yokken kendiliğinden dilekçeyle vergi dairesine bildirmiştir.\n\n{V}, Bay (R)’nin pişmanlıktan "
    "yararlanabilmesi için aşağıdakilerden hangisi gereklidir?",
    "Beyanını 15 gün içinde düzeltip vergiyi zamla ödemesi",
    ["Beyanını 30 gün içinde düzeltmesi, ödeme için süre olmaması",
     "Vergi dairesi müdürünün yazılı onayını alması",
     "Uzlaşma komisyonuna başvurması",
     "Vergiyi bir yıl içinde taksitle ödemesi"],
    "Md. 371'e göre eksik veya yanlış beyan haber verme tarihinden itibaren 15 gün içinde düzeltilmeli ve vergi pişmanlık "
    "zammıyla aynı süre içinde ödenmelidir.", lesson=VUK, topic="vergi_cezalari")

tm1 = (2_400_000 - 1_000_000) / 2
T1.sayisal("6183 md. 48",
    "(ZAB) Ltd. Şti., tahsil dairesindeki toplam 2.400.000 ₺ vergi borcunun tecilini talep etmiştir. (Kanundaki teminat "
    f"tutarlarının Cumhurbaşkanınca değiştirilmediği kabul edilecektir.)\n\n{A}, şirketin göstermesi gereken teminat tutarı "
    "kaç ₺’dir?",
    tl(tm1), secenekler(tm1, 2_400_000, 1_400_000, 1_200_000, 0),
    "6183 md. 48'e göre tecil edilen borçların toplamı bir milyon Türk lirasını aşarsa gösterilmesi zorunlu teminat, bir milyon "
    "Türk lirasını aşan kısmın yarısıdır: (2.400.000 − 1.000.000) / 2 = 700.000 ₺.", lesson=VUK, topic="vergilendirme_sureci")

dk1 = 50_000 * 12 * 0.00189
T1.sayisal("DVK md. 1, (1) sayılı tablo",
    "(CDE) A.Ş., bir işyerini aylık 50.000 ₺ bedelle 12 ay süreyle kiralamış ve kira sözleşmesini iki nüsha olarak "
    f"düzenlemiştir. (Kira sözleşmelerinde oran binde 1,89 olarak alınacaktır.)\n\n{DA}, bu sözleşme için ödenecek damga "
    "vergisi kaç ₺’dir?",
    tl(dk1), secenekler(dk1, dk1 * 2, 50_000 * 0.00189, 50_000 * 12 * 0.00948, dk1 / 12 * 2),
    "(1) sayılı tabloya göre kira sözleşmelerinde vergi, sözleşme süresine göre kira bedeli üzerinden alınır; md. 5'e göre "
    "nispi vergiye tabi kâğıtların sadece bir nüshası vergilendirilir: 600.000 × binde 1,89 = 1.134 ₺.", lesson=TVS,
    topic="vergi_sistemi_yapisi", zorluk="hard")

T1.sayisal("VİVK md. 9",
    "Bay (S), 2026 yılının Şubat ayında Türkiye’de vefat etmiştir. Tüm mirasçıları ölüm tarihinde Türkiye’de "
    f"bulunmaktadır.\n\n{VI}, mirasçılar beyannameyi ölüm tarihini takip eden kaç ay içinde vermelidir?",
    "4", ["1", "3", "6", "8"],
    "VİVK md. 9/1-a'ya göre ölüm Türkiye'de vuku bulmuş ve mükellefler Türkiye'de ise beyanname ölüm tarihini takip eden dört "
    "ay içinde verilir.", lesson=TVS, topic="vergi_sistemi_yapisi", zorluk="easy")

T1.q("DVK md. 3",
    "Almanya’da düzenlenip imzalanan bir alım-satım sözleşmesi, Türkiye’de bir tapu müdürlüğüne ibraz edilerek hükmünden "
    f"yararlanılmıştır.\n\n{DA}, bu kâğıdın damga vergisini kim öder?",
    "Kâğıdı Türkiye’de resmi daireye ibraz eden",
    ["Sözleşmeyi Almanya’da imzalayan yabancı taraf",
     "Tapu müdürlüğü",
     "Almanya’daki Türkiye konsolosluğu",
     "Kâğıt yurt dışında düzenlendiğinden vergi alınmaz"],
    "DVK md. 1 ve 3'e göre yabancı memleketlerde düzenlenen kâğıtlar Türkiye'de resmi dairelere ibraz edildiğinde vergiye tabi "
    "olur ve vergiyi bu kâğıtları ibraz edenler, devir veya ciro işlemi yapanlar ya da hükümlerinden faydalananlar öder.",
    lesson=TVS, topic="vergi_sistemi_yapisi", zorluk="hard")

# =============================================================================== TEST 2
T2 = paket("questions_vergi_test2_2026.json", 2026092952)

sm2 = 2_000_000 - 400_000 - 37_000 * 12
T2.sayisal("GVK md. 68/5",
    "Avukat Bayan (A), 2025 yılında mesleğinde kullanmak üzere aylık 50.000 ₺ bedelle bir binek otomobil kiralamıştır. Aynı "
    "yıl tahsil ettiği serbest meslek hasılatı 2.000.000 ₺, kira dışındaki belgeli mesleki giderleri 400.000 ₺’dir. (2025 "
    f"yılı binek otomobil aylık kira gider sınırı 37.000 ₺ olarak alınacaktır.)\n\n{G26}, Bayan (A)’nın 2025 yılı serbest "
    "meslek kazancı kaç ₺’dir?",
    tl(sm2), secenekler(sm2, 2_000_000 - 400_000 - 600_000, 2_000_000 - 400_000, 2_000_000 - 400_000 - 600_000 * 0.70,
                        2_000_000 - 600_000),
    "Md. 68/5'e göre kiralanan binek otomobillerde aylık kira bedelinin Kanundaki sınırı aşan kısmı indirilemez: 37.000 × 12 = "
    "444.000 ₺ indirilebilir; kazanç 2.000.000 − 400.000 − 444.000 = 1.156.000 ₺.", lesson=GV, topic="gelir_unsurlari",
    zorluk="hard")

da2 = (300_000 - 120_000) + (400_000 - 280_000)
T2.sayisal("GVK mük. 80, md. 82",
    "Bay (B), 2025 yılında üç yıl önce aldığı bir daireyi satarak endekslemeden sonra 300.000 ₺ değer artışı kazancı elde "
    "etmiş, ayrıca arızi olarak bir partiden aldığı malları satarak 400.000 ₺ kazanç sağlamıştır. (2025 yılı için değer artışı "
    f"istisnası 120.000 ₺, arızi kazanç istisnası 280.000 ₺ olarak alınacaktır.)\n\n{G}, Bay (B)’nin beyan edeceği vergiye "
    "tabi değer artışı ve arızi kazanç toplamı kaç ₺’dir?",
    tl(da2), secenekler(da2, 700_000, 700_000 - 280_000, 700_000 - 120_000, 700_000 - 400_000 - 120_000),
    "Mük. 80'e göre değer artışı kazancının 120.000 ₺'si, md. 82'ye göre arızi kazancın 280.000 ₺'si istisnadır; istisnalar "
    "ayrı ayrı uygulanır: 180.000 + 120.000 = 300.000 ₺.", lesson=GV, topic="gelir_unsurlari", zorluk="hard")

T2.q("GVK md. 89",
    "Tam mükellef Bay (C), 2025 yılı gelir vergisi beyannamesini hazırlarken yaptığı çeşitli harcamaları beyan edilen "
    f"gelirden indirmek istemektedir.\n\n{G}, aşağıdakilerden hangisi beyan edilen gelirden indirilemez?",
    "Kendi özel otomobili için ödediği kasko primi",
    ["Kendisi için ödediği kanuni sınırlar içindeki şahıs sigortası primi",
     "Türkiye’de yaptığı ve belgelendirdiği eğitim ve sağlık harcamaları",
     "Kamu yararına çalışan derneğe makbuz karşılığı yaptığı bağış",
     "Engellilik indirimi"],
    "Md. 89'a göre şahıs sigorta primleri (sınırlı), belgeli eğitim ve sağlık harcamaları (sınırlı), belirli bağış ve yardımlar "
    "ile engellilik indirimi beyan edilen gelirden indirilir; özel otomobil kaskosu şahıs sigortası değildir.", lesson=GV,
    topic="beyan_ve_tespit")

T2.q("GVK md. 85",
    "Tüccar Bay (D), 2025 yılında ticari faaliyetinden zarar etmiş ve hiç kazanç elde etmemiştir."
    f"\n\n{G}, Bay (D)’nin beyan yükümlülüğüne ilişkin aşağıdakilerden hangisi doğrudur?",
    "Beyanname vermekle yükümlüdür.",
    ["Kazancı olmadığı için beyanname vermez.",
     "Sadece geçici vergi beyannamesi verir.",
     "Zararını bildirmek için muhtasar beyanname verir.",
     "Beyanname vermesi vergi dairesinin davetine bağlıdır."],
    "Md. 85'e göre ticari, zirai ve mesleki kazançlarını beyan etmeye mecbur olanlar kazanç elde edilmese dahi yıllık "
    "beyanname vermekle yükümlüdür; zarar da beyanname ile tespit edilir.", lesson=GV, topic="beyan_ve_tespit",
    zorluk="easy")

T2.q("GVK md. 40",
    "Tüccar Bayan (E), müşterisiyle sözleşme görüşmesi için yaptığı yurt içi iş seyahatinde otel ve ulaşım giderlerini "
    f"belgelendirmiştir.\n\n{G}, bu giderlerin ticari kazancın tespitindeki durumu hakkında aşağıdakilerden hangisi "
    "doğrudur?",
    "İşle ilgili seyahat ve ikamet giderleri indirilebilir.",
    ["Seyahat giderleri kanunen kabul edilmeyen giderdir.",
     "Sadece ulaşım gideri indirilebilir, otel gideri indirilemez.",
     "Giderler ancak yurt dışı seyahatlerde indirilebilir.",
     "Giderlerin yarısı indirilebilir."],
    "Md. 40/4'e göre işle ilgili olmak ve işin önem ve genişliğiyle mütenasip bulunmak şartıyla seyahat ve ikamet giderleri "
    "ticari kazancın tespitinde indirilebilir.", lesson=GV, topic="gelir_unsurlari", zorluk="easy")

ak2 = 12_000_000 * 0.10
T2.sayisal("KVK md. 5/1-e, 32/C",
    "Tam mükellef (FGH) A.Ş.’nin 2025 ticari bilanço kârı 12.000.000 ₺ olup bunun 10.000.000 ₺’si üç yıldır aktifinde bulunan "
    "iştirak hisselerinin satış kazancıdır. Şirket istisna şartlarını sağlamaktadır; KKEG ve zarar yoktur. Şirket 2012’den "
    f"beri faaliyettedir.\n\n{KV}, (FGH) A.Ş.’nin 2025 hesap dönemi için ödeyeceği kurumlar vergisi kaç ₺’dir?",
    tl(ak2), secenekler(ak2, 4_500_000 * 0.25, 2_000_000 * 0.25, 12_000_000 * 0.25, 4_500_000 * 0.10),
    "Md. 5/1-e'ye göre satış kazancının %75'i (7.500.000 ₺) istisnadır; normal matrah 4.500.000 ₺, vergi 1.125.000 ₺. Md. "
    "32/C'ye göre asgari vergi (ticari kâr + KKEG) × %10 = 1.200.000 ₺'dir ve md. 5/1-e istisnası asgari vergi matrahından "
    "düşülebilecekler arasında sayılmaz; yüksek olan 1.200.000 ₺ ödenir.", lesson=KVG, topic="kurum_kazanci", zorluk="hard")

T2.sayisal("KVK md. 12",
    "Tam mükellef (IJK) A.Ş.’nin 2025 hesap dönemi başı öz sermayesi 1.000.000 ₺’dir. Şirket yıl içinde ortağı Bay (F)’den "
    "2.000.000 ₺ borç almış; ayrıca iştiraki (LMN) A.Ş.’nin bankadan temin edip aynı şartlarla kullandırdığı 3.000.000 ₺ "
    f"kredi kullanmıştır.\n\n{KV}, (IJK) A.Ş.’nin 2025 hesap dönemi için örtülü sermaye tutarı kaç ₺’dir?",
    tl(0), secenekler(0, 2_000_000, 5_000_000 - 3_000_000 + 1_000_000, 1_000_000, 500_000),
    "Md. 12/6'ya göre iştiraklerin bankalardan temin ederek aynı şartlarla kullandırdığı borçlanmalar örtülü sermaye sayılmaz. "
    "Dikkate alınan borç 2.000.000 ₺ olup öz sermayenin üç katını (3.000.000 ₺) aşmadığından örtülü sermaye oluşmaz.",
    lesson=KVG, topic="kurum_kazanci", zorluk="hard")

T2.q("KVK md. 11/1-j, k",
    "(OPR) A.Ş. 2026 yılında çeşitli reklam giderlerine katlanmıştır: bir televizyon kanalında gıda ürünü reklamı, hakkında "
    "reklam yasağı uygulanan bir yabancı sosyal ağ sağlayıcısına verilen reklam ve bir bahis sitesinin sponsorluk reklamı."
    f"\n\n{KV26}, bu giderlerden hangisi kurum kazancından indirilebilir?",
    "Televizyonda yayınlanan gıda ürünü reklamı",
    ["Reklam yasağı uygulanan sosyal ağ sağlayıcısına verilen reklam",
     "Bahis sitesine ait sponsorluk reklamı",
     "Reklam giderlerinin tamamı KKEG sayılır",
     "Sadece yabancı ağ sağlayıcısına verilen reklam"],
    "Md. 11/1-j'ye göre 5651 sayılı Kanun kapsamında reklam yasağı uygulananlara verilen reklamların giderleri, md. 11/1-k'ye "
    "göre her türlü şans ve bahis oyunlarına ait ilan ve reklam giderleri indirilemez; olağan ürün reklamı indirilebilir.",
    lesson=KVG, topic="kurum_kazanci", zorluk="hard")

T2.q("KVK md. 17/1-ç",
    "(PRS) A.Ş.’nin tasfiyesi 2023 yılında başlamış ve 2026 yılında sona ermiştir. Vergi dairesi tasfiye dönemlerine ilişkin "
    f"tarhiyat yapmak istemektedir.\n\n{KV}, bu tasfiyede tarh zamanaşımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Zamanaşımı tasfiyenin sona erdiği dönemi izleyen yıldan başlar.",
    ["Zamanaşımı her tasfiye dönemi için ayrı ayrı o dönemden başlar.",
     "Tasfiye hâlindeki kurumlar için zamanaşımı işlemez.",
     "Zamanaşımı tasfiyenin başladığı yıldan itibaren başlar.",
     "Zamanaşımı süresi tasfiyede iki yıla iner."],
    "Md. 17/1-ç'ye göre bir yıldan fazla süren tasfiyelerde tarh zamanaşımı, tasfiyenin sona erdiği dönemi izleyen yıldan "
    "itibaren başlar.", lesson=KVG, topic="kurumlar_mukellefiyeti", zorluk="hard")

ty2 = 1_000_000 * 0.20 * 0.4
T2.sayisal("KDVK md. 9",
    "(TUV) A.Ş., bir yüklenici firmadan 2026/Mart döneminde KDV hariç 1.000.000 ₺ bedelli yapım işi hizmeti almıştır. Hizmet "
    "Maliye Bakanlığınca belirlenen kısmi tevkifat kapsamındadır. (KDV oranı %20, tevkifat oranı 4/10 olarak alınacaktır.)"
    f"\n\n{KD}, (TUV) A.Ş.’nin sorumlu sıfatıyla beyan edeceği KDV kaç ₺’dir?",
    tl(ty2), secenekler(ty2, 200_000, 120_000, 180_000, 40_000),
    "Md. 9'a göre Bakanlık işlemlere taraf olanları verginin ödenmesinden sorumlu tutabilir. Hesaplanan KDV 200.000 ₺'nin "
    "4/10'u (80.000 ₺) alıcı tarafından sorumlu sıfatıyla beyan edilir; kalan 120.000 ₺'yi yüklenici beyan eder.",
    lesson=KDV, topic="kdv_mekanizmasi")

it2 = (500_000 + 50_000 + 100_000) * 0.20
T2.sayisal("KDVK md. 21",
    "(VYZ) A.Ş. 2026 yılında gümrük vergisi tarhına esas kıymeti 500.000 ₺ olan bir makine ithal etmiştir. İthalat "
    "sırasında 50.000 ₺ gümrük vergisi ve 100.000 ₺ özel tüketim vergisi ödenmiştir; tescilden önce başka gider yoktur. "
    f"{ORAN}\n\n{KD}, bu ithalat için hesaplanacak KDV kaç ₺’dir?",
    tl(it2), secenekler(it2, 100_000, 110_000, 120_000, 150_000),
    "Md. 21'e göre ithalatta matrah, gümrük vergisine esas kıymete ithalat sırasında ödenen her türlü vergi, resim ve harçların "
    "eklenmesiyle bulunur: (500.000 + 50.000 + 100.000) × %20 = 130.000 ₺.", lesson=KDV, topic="kdv_mekanizmasi")

T2.q("KDVK md. 20",
    "(ZAB) Ltd. Şti., Mart 2026’da sattığı malı alıcıya teslim etmiş; alıcı bedeli üç ay sonra ödemeyi taahhüt ederek şirkete "
    f"borçlanmıştır.\n\n{KD}, bu teslimin KDV matrahına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Borçlanılan tutar da bedel sayılır; matrah Mart’ta oluşur.",
    ["Bedel tahsil edilmedikçe KDV hesaplanmaz.",
     "Matrah, bedelin tahsil edildiği Haziran’da oluşur.",
     "Vadeli satışlarda KDV sadece peşin kısım üzerinden hesaplanır.",
     "Borçlanılan tutar bedel sayılmaz, emsal bedel esas alınır."],
    "Md. 20/2'ye göre bedel, alıcıdan alınan veya borçlanılan para, mal ve menfaatlerin toplamıdır; md. 10'a göre vergiyi "
    "doğuran olay malın teslimidir. Tahsilatın ertelenmesi matrahı değiştirmez.", lesson=KDV, topic="kdv_mekanizmasi")

T2.q("KDVK md. 13/c",
    "Bir altın madeni işletmesine, madenin zenginleştirme tesisinde kullanılmak üzere makine teslimi ve montaj hizmeti "
    f"verilmiştir.\n\n{KD}, bu teslim ve hizmetin KDV karşısındaki durumu nedir?",
    "Teslim ve hizmet KDV’den istisnadır.",
    ["Genel oranda KDV’ye tabidir.",
     "Sadece montaj hizmeti istisnadır, makine teslimi vergilidir.",
     "Sadece makine teslimi istisnadır, montaj vergilidir.",
     "İndirimli oranda KDV’ye tabidir."],
    "Md. 13/c'ye göre altın, gümüş ve platin arama, işletme, zenginleştirme ve rafinaj faaliyetlerine ilişkin olarak bu "
    "faaliyetleri yürütenlere yapılan teslim ve hizmetler KDV'den istisnadır.", lesson=KDV, topic="kdv_teslim_ve_indirim",
    zorluk="hard")

us2 = 2_000 * 2 + 2_000 * 2 / 4
T2.sayisal("VUK md. 337, 352",
    "(CDE) A.Ş. 2026 yılı içinde, Kanunun 352. maddesindeki aynı derece ve fıkraya giren ve her biri resen takdiri gerektiren "
    "iki ayrı usulsüzlük fiili işlemiştir. (Fiil için 1 sayılı cetvelde yer alan ceza 2.000 ₺ olarak alınacaktır.)"
    f"\n\n{V26}, bu iki fiil için kesilecek toplam usulsüzlük cezası kaç ₺’dir?",
    tl(us2), secenekler(us2, 8_000, 4_000, 2_500, 6_000),
    "Md. 352'ye göre resen takdiri gerektiren usulsüzlüklerde cetveldeki ceza iki kat uygulanır (4.000 ₺). Md. 337'ye göre aynı "
    "yıl içinde aynı nevi ikinci fiil için birincinin cezasının dörtte biri kesilir (1.000 ₺): toplam 5.000 ₺.", lesson=VUK,
    topic="vergi_cezalari", zorluk="hard")

T2.q("VUK md. 114",
    "Bir şirket 2018 yılında düzenlediği ve damga vergisi ödenmemiş bir sözleşmeyi, tarh zamanaşımı süresi dolduktan sonra "
    f"2026 yılında bir mahkemeye delil olarak sunmuştur.\n\n{V}, bu durumda damga vergisi alacağı hakkında aşağıdakilerden "
    "hangisi doğrudur?",
    "Evrakın vergi alacağı yeniden doğar.",
    ["Zamanaşımı dolduğundan vergi alacağı doğmaz.",
     "Vergi sadece ceza olmadan yarısı oranında alınır.",
     "Vergi, mahkeme harcına dahil edilerek tahsil edilir.",
     "Damga vergisinde zamanaşımı uygulanmaz."],
    "Md. 114'e göre damga vergisine tabi olup vergi ve cezası zamanaşımına uğrayan evrakın hükmünden tarh zamanaşımı süresi "
    "dolduktan sonra faydalanılırsa bu evraka ait vergi alacağı yeniden doğar.", lesson=VUK, topic="vergilendirme_sureci",
    zorluk="hard")

T2.sayisal("6183 md. 102-103",
    "Vadesi 2020 yılında olan bir amme alacağı 2023 yılında teminata bağlanmış; teminat 2025 yılında kalkmıştır. Başka bir "
    f"kesme sebebi yoktur.\n\n{A}, bu alacak en geç hangi yılın sonunda zamanaşımına uğrar?",
    "2030", ["2025", "2028", "2029", "2031"],
    "6183 md. 103'e göre amme alacağının teminata bağlanması zamanaşımını keser; bu hâlde zamanaşımı başlangıcı teminatın "
    "kalktığı tarihin rastladığı yılı takip eden yıl başıdır: 2026-2030.", lesson=VUK, topic="vergilendirme_sureci",
    zorluk="hard")

T2.q("İYUK md. 7",
    "Bayan (G), bir kira sözleşmesinin damga vergisini pul ve makbuz karşılığı ödemiş, daha sonra verginin fazla alındığını "
    f"düşünerek dava açmak istemiştir.\n\n{I}, tahakkuku tahsile bağlı bu vergide dava açma süresi ne zaman başlar?",
    "Tahsilatın yapıldığı tarihi izleyen gün",
    ["Sözleşmenin imzalandığı yılın sonu",
     "Vergi dairesinin ihbarname tebliğ ettiği tarih",
     "Sözleşmenin sona erdiği tarih",
     "Mükellefin hatayı fark ettiği tarih"],
    "İYUK md. 7/2-b'ye göre tahakkuku tahsile bağlı olan vergilerde dava açma süresi tahsilatın yapıldığı tarihi izleyen "
    "günden başlar.", lesson=VH, topic="vergi_uyusmazliklari")

T2.q("ÖTVK md. 3",
    "Bir otomotiv bayisi, Nisan 2026’da teslim edeceği yeni bir otomobil için Mart 2026’da alıcının talebiyle fatura "
    f"düzenlemiştir.\n\n{OT}, bu işlemde vergiyi doğuran olay ne zaman meydana gelir?",
    "Mart’ta, faturadaki miktarla sınırlı olarak",
    ["Aracın fiilen teslim edildiği Nisan 2026’da, tutarın tamamı için",
     "Aracın trafiğe tescil edildiği tarihte",
     "Bedelin tamamen tahsil edildiği tarihte",
     "Aracın ilk kez kullanıldığı tarihte"],
    "ÖTVK md. 3/b'ye göre malın tesliminden önce fatura veya benzeri belge verilmesi hâllerinde, belgede gösterilen miktarla "
    "sınırlı olmak üzere vergiyi doğuran olay faturanın düzenlenmesiyle meydana gelir.", lesson=TVS,
    topic="vergi_sistemi_yapisi", zorluk="hard")

T2.q("DVK md. 6",
    "Bir kredi sözleşmesinde, borçlunun borcuna aynı kâğıt üzerinde üç ayrı kişi adi kefil olmuştur."
    f"\n\n{DA}, bu kefaletler için damga vergisi nasıl alınır?",
    "Kefaletlerden sadece biri için vergi alınır.",
    ["Her kefalet için ayrı ayrı vergi alınır.",
     "Kefaletler için vergi alınmaz.",
     "Kefalet vergisi kredi tutarının üç katı üzerinden alınır.",
     "Sadece en yüksek tutarlı kefalet vergiden istisnadır."],
    "DVK md. 6'ya 6728 sayılı Kanunla eklenen cümleye göre bir kâğıt üzerinde birden fazla adi kefalet ve garanti taahhüdü "
    "bulunması hâlinde bunlardan sadece birinden damga vergisi alınır.", lesson=TVS,
    topic="vergi_sistemi_yapisi", zorluk="hard")

ar2 = 2_000_000 * 0.003
T2.sayisal("EVK md. 18",
    "Bay (H), büyükşehir belediyesi bulunmayan bir ilde vergi değeri 2.000.000 ₺ olan bir arsanın sahibidir."
    f"\n\n{EM}, Bay (H)’nin yıllık arazi vergisi kaç ₺’dir?",
    tl(ar2), secenekler(ar2, 2_000, 12_000, 4_000, 3_000),
    "EVK md. 18'e göre arsalarda vergi oranı binde üçtür; büyükşehir belediye sınırları dışında artırım uygulanmaz: "
    "2.000.000 × binde 3 = 6.000 ₺.", lesson=TVS, topic="vergi_sistemi_yapisi", zorluk="easy")

# =============================================================================== TEST 3
T3 = paket("questions_vergi_test3_2026.json", 2026092953)

gt3 = gv2025(1_000_000)
T3.sayisal("GVK md. 103",
    "Tam mükellef tüccar Bay (K)’nın 2025 yılı gelir vergisi matrahı, ticari kazancından oluşan 1.000.000 ₺’dir; ücret geliri "
    f"yoktur. ({TARIFE_2025})\n\n{G}, Bay (K)’nın 2025 yılı için hesaplanan gelir vergisi kaç ₺’dir?",
    tl(gt3), secenekler(gt3, 1_000_000 * 0.27, 185_000, 1_000_000 * 0.35, 58_100 + 670_000 * 0.27),
    "Md. 103'e göre ücret dışı gelirlerde 800.000 ₺'ye kadar olan kısım için 185.000 ₺, aşan 200.000 ₺ için %35 uygulanır: "
    "185.000 + 70.000 = 255.000 ₺.", lesson=GV, topic="beyan_ve_tespit", zorluk="hard")

gu3 = gv2025(1_500_000, ucret=True)
T3.sayisal("GVK md. 103",
    "Tek işverenden ücret alan Bayan (L), ücretinin yanında işyeri kira geliri de elde ettiği için yıllık beyanname vermiştir; "
    f"beyana konu ücret gelirinden oluşan matrahı 1.500.000 ₺’dir. ({TARIFE_2025})\n\n{G}, bu matrah için ücret tarifesine "
    "göre hesaplanan gelir vergisi kaç ₺’dir?",
    tl(gu3), secenekler(gu3, gv2025(1_500_000), 1_500_000 * 0.35, 293_000, 1_500_000 * 0.27),
    "Md. 103'e göre ücret gelirlerinde üçüncü dilim 1.200.000 ₺'ye kadar uzanır: 1.200.000 ₺ için 293.000 ₺, aşan 300.000 ₺ "
    "için %35: 293.000 + 105.000 = 398.000 ₺.", lesson=GV, topic="beyan_ve_tespit", zorluk="hard")

T3.q("GVK md. 61",
    "Bir anonim şirket, çalışanlarına 2025 yılında nakit ücretlerinin yanında şirket lojmanında ücretsiz konut, özel sağlık "
    f"sigortası ve bayram hediyesi olarak alışveriş çeki vermiştir.\n\n{G}, bu menfaatlerin vergilendirilmesine ilişkin "
    "aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ayni menfaatler ücret sayılmaz, vergi dışıdır.",
    ["Para ile temsil edilebilen menfaatler ücret sayılır.",
     "Ödemenin adı veya şekli ücret niteliğini değiştirmez.",
     "Ücret istisnaları Kanunda sayılanlarla sınırlıdır.",
     "Hizmet karşılığı verilen ayınlar da ücret kapsamındadır."],
    "Md. 61'e göre ücret, işverene tabi çalışanlara hizmet karşılığı verilen para ve ayınlar ile sağlanan ve para ile temsil "
    "edilebilen menfaatlerdir; ödemenin ayni olması ücret niteliğini değiştirmez (istisnalar md. 23'te sayılanlarla "
    "sınırlıdır).", lesson=GV, topic="gelir_unsurlari")

T3.q("GVK md. 7",
    "Kanuni ve iş merkezi Almanya’da olan bir danışman, Türkiye’de işyeri bulunmaksızın Almanya’dan Türkiye’deki bir şirkete "
    f"danışmanlık hizmeti vermiş ve şirket hizmetten Türkiye’de yararlanmıştır.\n\n{G}, bu serbest meslek kazancının "
    "Türkiye’de elde edilmiş sayılmasına ilişkin aşağıdakilerden hangisi doğrudur?",
    "Türkiye’de değerlendirildiğinden elde edilmiş sayılır.",
    ["İşyeri olmadığından Türkiye’de elde edilmiş sayılmaz.",
     "Ödeme yurt dışında yapılırsa Türkiye’de elde edilmiş sayılır.",
     "Hizmet sadece Türkiye’de fiilen ifa edilirse vergilendirilir.",
     "Serbest meslek kazançları dar mükellefiyette vergilendirilmez."],
    "Md. 7/4'e göre dar mükelleflerin serbest meslek kazançlarında, serbest meslek faaliyetinin Türkiye'de icra edilmesi veya "
    "Türkiye'de değerlendirilmesi Türkiye'de elde edilme şartıdır; değerlendirme, ödemenin Türkiye'de yapılması veya yabancı "
    "memlekette yapılmışsa Türkiye'deki işletmenin hesaplarına intikal ettirilmesidir.", lesson=GV, topic="gelir_unsurlari",
    zorluk="hard")

bn3 = 10_000_000 * 0.30
T3.sayisal("KVK md. 32",
    "Mevduat bankası olarak faaliyet gösteren (MNO) Bankası A.Ş.’nin 2025 hesap dönemi kurumlar vergisi matrahı 10.000.000 "
    f"₺’dir; indirimli oran uygulaması yoktur.\n\n{KV}, bankanın 2025 hesap dönemi kurumlar vergisi kaç ₺’dir?",
    tl(bn3), secenekler(bn3, 10_000_000 * 0.25, 10_000_000 * 0.20, 10_000_000 * 0.35, 10_000_000 * 0.15),
    "Md. 32/1'e göre kurumlar vergisi genel oranı %25'tir; ancak bankalar, finansman şirketleri, sigorta şirketleri ve benzeri "
    "kurumlarda oran %30'dur: 10.000.000 × %30 = 3.000.000 ₺.", lesson=KVG, topic="kurum_kazanci", zorluk="easy")

tf3 = (4_000_000 + 2_500_000) - (5_500_000 + 150_000)
T3.sayisal("KVK md. 17/4",
    "2025 yılında başlayıp aynı yıl biten tasfiye sürecinde (PRS) Ltd. Şti.’nin tasfiye başı servet değeri 5.500.000 ₺, tasfiye "
    "sonu servet değeri 4.000.000 ₺’dir. Tasfiye sırasında ortaklara 2.500.000 ₺ ödeme yapılmış, 150.000 ₺ vergiden istisna "
    f"kazanç elde edilmiştir.\n\n{KV}, şirketin tasfiye kârı kaç ₺’dir?",
    tl(tf3), secenekler(tf3, 1_000_000, 1_000_000 + 150_000, 2_500_000, 0),
    "Md. 17/4'e göre ortaklara yapılan ödemeler dönem sonu servetine, istisna kazançlar dönem başı servetine eklenir: "
    "(4.000.000 + 2.500.000) − (5.500.000 + 150.000) = 850.000 ₺.", lesson=KVG, topic="kurumlar_mukellefiyeti",
    zorluk="hard")

T3.q("KVK md. 12, 13",
    "(TUV) A.Ş.’nin ortağının %25 payla ortak olduğu (VYZ) Ltd. Şti., (TUV) A.Ş.’ye emsallere aykırı düşük faizli borç vermiş "
    f"ve (TUV) A.Ş.’den emsalin üzerinde bedelle mal almıştır.\n\n{KV26}, bu işlemlere ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "İlişkili kişi olduğundan emsale uygunluk aranır.",
    ["Ortağın payı %50’nin altında olduğundan ilişki yoktur.",
     "Sadece borç işlemi değerlendirilir, mal satışı dikkate alınmaz.",
     "Örtülü kazanç dağıtımı sadece dar mükelleflerde söz konusudur.",
     "İlişkili kişi işlemleri vergi incelemesine konu olamaz."],
    "Md. 12/3 ve 13'e göre ortağın en az %10 oranında ortağı olduğu kurum ilişkili kişi sayılır; ilişkili kişilerle mal ve "
    "hizmet alım satımında emsallere uygunluk ilkesi uygulanır ve aykırılık örtülü kazanç dağıtımı sonucunu doğurur.",
    lesson=KVG, topic="kurum_kazanci", zorluk="hard")

T3.q("KVK md. 32/C",
    "2025 yılında kurulan ve aynı yıl faaliyete başlayan (ZAB) A.Ş., 2027 hesap döneminde yüksek tutarlı istisna kazanç elde "
    f"etmeyi planlamaktadır.\n\n{KV26}, şirketin yurt içi asgari kurumlar vergisi karşısındaki durumu hakkında "
    "aşağıdakilerden hangisi doğrudur?",
    "Üç hesap dönemi boyunca asgari vergi uygulanmaz.",
    ["Asgari vergi 2026 yılından itibaren uygulanır.",
     "Asgari vergi sadece 2025 yılında uygulanmaz.",
     "Yeni kurulan şirketlere asgari vergi süresiz uygulanmaz.",
     "Asgari vergi kuruluş yılında iki kat uygulanır."],
    "Md. 32/C/5'e göre ilk defa faaliyete başlayan kurumlar hakkında faaliyete başlanılan hesap döneminden itibaren üç hesap "
    "dönemi boyunca bu madde uygulanmaz: 2025, 2026 ve 2027.", lesson=KVG, topic="kurum_kazanci")

kd3 = 900_000 * 0.20 - 100_000 - 120_000 * 20 / 120
T3.sayisal("KDVK md. 29/4",
    "(CDE) A.Ş.’nin 2026/Haziran dönemi işlemleri: yurt içi teslimler 900.000 ₺ (KDV hariç); indirilecek KDV 100.000 ₺. Aynı "
    "dönemde, KDV’si daha önce beyan edilip ödenmiş KDV dahil 120.000 ₺ tutarındaki bir alacak VUK md. 322 uyarınca değersiz "
    f"hâle gelmiş ve zarar yazılmıştır; karşılık ayrılmamıştır. {ORAN}\n\n{KD}, şirketin 2026/Haziran dönemi ödenecek "
    "KDV’si kaç ₺’dir?",
    tl(kd3), secenekler(kd3, 80_000, 180_000 - 100_000 - 24_000, 100_000, 180_000),
    "Hesaplanan KDV 900.000 × %20 = 180.000 ₺. Md. 29/4'e göre değersiz alacağa ilişkin beyan edilen KDV (120.000 × 20/120 = "
    "20.000 ₺) alacağın zarar yazıldığı dönemde indirilebilir: 180.000 − 100.000 − 20.000 = 60.000 ₺.", lesson=KDV,
    topic="kdv_mekanizmasi", zorluk="hard")

ie3 = (1_300_000 - 1_050_000) * 0.20
T3.sayisal("KDVK md. 23/f",
    "İkinci el otomobil ticareti yapan (FGH) Otomotiv A.Ş., KDV mükellefi olmayan bir kişiden 1.050.000 ₺’ye aldığı aracı, "
    f"vasfında esaslı değişiklik yapmadan 1.300.000 ₺’ye satmıştır. {ORAN}\n\n{KD}, bu satış için hesaplanacak KDV kaç "
    "₺’dir?",
    tl(ie3), secenekler(ie3, 1_300_000 * 0.20, 1_050_000 * 0.20, 250_000 * 0.18, 250_000),
    "Md. 23/f'ye göre ikinci el motorlu kara taşıtı ticareti yapanlarca KDV mükellefi olmayanlardan alınıp vasfında esaslı "
    "değişiklik yapılmadan satılan taşıtlarda matrah, alış bedeli düşüldükten sonra kalan tutardır: 250.000 × %20 = "
    "50.000 ₺.", lesson=KDV, topic="kdv_mekanizmasi")

T3.q("KDVK md. 30/a",
    "Serbest bölgede faaliyet gösteren müşterilerine hizmet veren (IJK) A.Ş., bu istisnalı hizmetler için yüklendiği KDV’yi "
    f"indirim konusu yapmak istemektedir.\n\n{KD}, bu durum hakkında aşağıdakilerden hangisi doğrudur?",
    "Bu KDV indirim yasağının dışındadır.",
    ["İstisnalı işlemlere ait tüm KDV’ler kural olarak indirilemez.",
     "KDV sadece gider yazılabilir.",
     "KDV iade edilmez, sonraki yıllara devreder ve silinir.",
     "Serbest bölge hizmetleri KDV’nin konusu dışındadır."],
    "Md. 30/a'ya göre istisna işlemlere ait KDV kural olarak indirilemez; ancak md. 17/4-ı kapsamında serbest bölgelerde "
    "verilen hizmetler ile ihraç amaçlı yük taşımaları gibi sayılan istisnalar bu yasağın dışındadır.", lesson=KDV,
    topic="kdv_teslim_ve_indirim", zorluk="hard")

T3.q("KDVK md. 2/1",
    "(LMN) A.Ş., sattığı malları alıcının talimatıyla doğrudan alıcının Konya’daki bayisinin deposuna teslim etmiştir."
    f"\n\n{KD}, bu işlem hakkında aşağıdakilerden hangisi doğrudur?",
    "Malın alıcının gösterdiği yere tevdii teslim hükmündedir.",
    ["Mal alıcıya bizzat verilmediği için teslim gerçekleşmemiştir.",
     "İşlem hizmet sayılır ve hizmet hükümlerine tabidir.",
     "Teslim, bayinin malı üçüncü kişiye sattığı anda gerçekleşir.",
     "Bayinin deposuna teslim KDV’nin konusu dışındadır."],
    "Md. 2/1'e göre teslim, mal üzerindeki tasarruf hakkının alıcıya devredilmesidir; malın alıcının veya onun adına hareket "
    "edenlerin gösterdiği yere veya kişilere tevdii de teslim hükmündedir.", lesson=KDV, topic="kdv_teslim_ve_indirim",
    zorluk="easy")

vc3 = 60_000 * 0.50
T3.sayisal("VUK md. 344",
    "Bay (M), 2025 yılı beyannamesini kanuni süresinden sonra, hakkında inceleme başlamadan kendiliğinden vermiş; ancak "
    "pişmanlık dilekçesi vermediği için pişmanlık hükümlerinden yararlanamamıştır. Beyanname üzerine tahakkuk eden vergi "
    f"60.000 ₺’dir.\n\n{V26}, Bay (M) adına kesilecek vergi ziyaı cezası kaç ₺’dir?",
    tl(vc3), secenekler(vc3, 60_000, 12_000, 180_000, 0),
    "Md. 344'e göre inceleme ve takdire sevkten önce kanuni süresinden sonra verilen beyannameler için vergi ziyaı cezası "
    "yüzde elli oranında uygulanır: 60.000 × %50 = 30.000 ₺.", lesson=VUK, topic="vergi_cezalari")

T3.q("VUK md. 370",
    "Gelir İdaresi, (OPR) Ltd. Şti.’nin sahte fatura kullanmış olabileceğine dair bir ön tespit yapmıştır."
    f"\n\n{V26}, bu şirketin izaha davet edilmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Kural olarak izaha davet edilmez.",
    ["Tüm ön tespitlerde mükellef izaha davet edilir.",
     "İzaha davet edilirse ceza %10 oranında kesilir.",
     "İzaha davet yazısı tebliğ edilse de pişmanlık hakkı saklıdır.",
     "İzaha davet vergi incelemesi sırasında yapılır."],
    "Md. 370/b'ye göre ön tespitin verginin md. 359'daki fiillerle ziyaa uğratılmış olabileceğine ilişkin olması hâlinde "
    "mükellefler kural olarak izaha davet edilmez; sahte veya yanıltıcı belge kullanmaya ilişkin sınırlı bir istisna vardır.",
    lesson=VUK, topic="vergi_cezalari", zorluk="hard")

T3.sayisal("VUK md. 219",
    "(ABC) Ltd. Şti., 3 Mart 2026’da gerçekleştirdiği bir satış işlemini yevmiye defterine kaydedecektir; işletme muhasebe "
    f"fişi sistemi kullanmamaktadır.\n\n{V}, bu kaydın geciktirilebileceği azami süre kaç gündür?",
    "10", ["5", "15", "30", "45"],
    "Md. 219/a'ya göre muamelelerin muhasebenin intizamını bozmayacak bir süre içinde kaydedilmesi şarttır ve kayıtlar on "
    "günden fazla geciktirilemez; mazbut vesikalara dayanan kayıtlarda esas deftere intikal süresi 45 gündür.", lesson=VUK,
    topic="mukellef_odevleri")

hc3 = 90_000 / 3
T3.sayisal("6183 md. 71",
    "Amme borçlusu Bay (N)’nin 2026 yılındaki aylık net emekli aylığı 90.000 ₺ olup asgari ücretin üzerindedir. Tahsil dairesi bu aylığa "
    f"haciz koyacaktır.\n\n{A}, aylıktan haczedilebilecek en yüksek tutar kaç ₺’dir?",
    tl(hc3), secenekler(hc3, 90_000 / 4, 9_000, 45_000, 90_000),
    "6183 md. 71'e göre emeklilik aylıkları kısmen haczolunabilir; haczolunacak miktar üçte birden çok, dörtte birden az "
    "olamaz: en fazla 90.000 / 3 = 30.000 ₺.", lesson=VUK, topic="vergilendirme_sureci", zorluk="hard")

T3.q("VUK Ek md. 1",
    "(DEF) A.Ş. hakkında yapılan ön tespit üzerine izaha davet edilmiş, izah yetersiz bulunmuş ve şartlar yerine getirilerek "
    f"%20 oranında vergi ziyaı cezası kesilmiştir.\n\n{V26}, bu cezanın uzlaşmaya konu edilmesi hakkında aşağıdakilerden "
    "hangisi doğrudur?",
    "Bu ceza uzlaşmaya konu edilemez.",
    ["Ceza tarhiyat sonrası uzlaşmaya konu edilebilir.",
     "Ceza sadece tarhiyat öncesi uzlaşmaya konu edilebilir.",
     "Ceza uzlaşmada tamamen kaldırılır.",
     "Ceza uzlaşmada yarı oranında indirilir."],
    "Ek md. 1'e göre md. 370/b kapsamında ön tespite ilişkin yazı tebliğ edilen mükelleflere bu maddeye göre kesilen ceza "
    "uzlaşma kapsamı dışında tutulmuştur.", lesson=VH, topic="vergi_uyusmazliklari", zorluk="hard")

dk3 = 20_000 * 24 * 0.00189
T3.sayisal("DVK (1) sayılı tablo",
    "Bayan (P), bir şirketle 24 ay süreli ve aylık 20.000 ₺ bedelli bir işyeri kira sözleşmesi imzalamıştır. (Kira "
    f"sözleşmelerinde damga vergisi oranı binde 1,89 olarak alınacaktır.)\n\n{DA}, bu sözleşme için ödenecek damga vergisi "
    "kaç ₺’dir?",
    tl(dk3), secenekler(dk3, 20_000 * 12 * 0.00189, 20_000 * 0.00189, 20_000 * 24 * 0.00948, dk3 * 2),
    "(1) sayılı tabloya göre kira sözleşmelerinde vergi sözleşme süresine göre kira bedeli üzerinden alınır: 20.000 × 24 = "
    "480.000 ₺; 480.000 × binde 1,89 = 907,20 ₺.", lesson=TVS, topic="vergi_sistemi_yapisi")

T3.q("VİVK md. 7",
    "Bay (R), bir şans oyununda büyük ikramiye kazanmış ve ikramiyesinden vergi kesilerek kalan tutar kendisine ödenmiştir."
    f"\n\n{VI}, bu ikramiyeye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Bay (R) ayrıca veraset ve intikal vergisi beyannamesi verir.",
    ["İkramiye ivazsız intikal olarak vergiye tabidir.",
     "Vergi, ikramiyeden kesinti yoluyla alınır.",
     "Kesilen vergiyi oyunu düzenleyen kuruluş beyan eder.",
     "Tevkifata tabi ikramiye için kazanan beyanname vermez."],
    "VİVK md. 1 ve 7'ye göre ikramiyeler ivazsız intikal olarak vergiye tabidir; ikramiyelerden kesilen vergiler oyunu veya "
    "yarışmayı düzenleyenlerce beyan edilir ve md. 16'ya göre tevkifat yapılan ikramiyeler için kazananlar ayrıca beyanname "
    "vermez.", lesson=TVS,
    topic="vergi_sistemi_yapisi")

T3.q("EVK md. 8",
    "Bir belediye başkanı, bölgedeki emlak vergisi yükünü azaltmak için oranların düşürülmesini talep etmektedir."
    f"\n\n1319 sayılı Emlak Vergisi Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre, emlak vergisi oranlarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Belediye meclisi oranları kendi kararıyla belirler.",
    ["Meskenlerde bina vergisi oranı binde birdir.",
     "Arsalarda arazi vergisi oranı binde üçtür.",
     "Büyükşehirlerde oranlar %100 artırımlı uygulanır.",
     "Cumhurbaşkanı oranları yarısına indirip üç katına çıkarabilir."],
    "EVK md. 8 ve 18'e göre bina vergisi meskenlerde binde bir, arsalarda binde üçtür; büyükşehirlerde %100 artırımlı "
    "uygulanır. Cumhurbaşkanı oranları yarısına kadar indirmeye veya üç katına kadar artırmaya yetkilidir; belediye meclisinin "
    "böyle bir yetkisi yoktur.", lesson=TVS, topic="vergi_sistemi_yapisi")

if __name__ == "__main__":
    rc = 0
    for paket_ in (T1, T2, T3):
        rc |= paket_.yaz()
    sys.exit(rc)
