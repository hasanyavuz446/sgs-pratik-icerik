# -*- coding: utf-8 -*-
"""Hukuk · Bölüm Havuzu — 3 test × 20 soru, gerçek test kitapçığı düzeninde.

Her test 2026/1-2026/2 kitapçıklarının ağırlığını izler: 5510 sayılı Kanun ~5, İş Kanunu ~4, TBK ~4, TTK (kıymetli evrak
ve taşıma dahil) ~4, İYUK ~3; yaklaşık dörtte biri süre veya sayı sorar. Konu havuzundaki kökler tekrar edilmez; aynı hüküm
farklı olayla ölçülür. Dayanaklar konu builder'larıyla aynıdır (build_yk_*.py başlıklarına bkz.); 29.09.2026 kontrolü.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import Paket
from vergi_ortak import tl, secenekler

SURUM = ("4857 İK, 5510 SSGSSK, 6098 TBK, 6102 TTK, 2577 İYUK, 6701 TİHEK güncel metinleri (7578, 7588, 7589 s. Kanun "
         "değişiklikleri dahil); 29.09.2026 kontrolü")

def paket(dosya, seed, ek=()):
    return Paket(dosya, lesson="is_hukuku", topic="is_sozlesmesi", konu_adi="Hukuk", seed=seed, surum=SURUM,
                 havuz="bolum", ek_idler=ek)

IK = "4857 sayılı İş Kanunu’na göre"
IK26 = "4857 sayılı İş Kanunu’nun 2026 yılında yürürlükte olan hükümlerine göre"
SG = "5510 sayılı Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu’na göre"
SG26 = ("5510 sayılı Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu’nun 2026 yılında yürürlükte olan hükümlerine "
        "göre")
BK = "6098 sayılı Türk Borçlar Kanunu’na göre"
TK = "6102 sayılı Türk Ticaret Kanunu’na göre"
IY = "2577 sayılı İdari Yargılama Usulü Kanunu’na göre"

L_IS, L_SG, L_BK, L_TK, L_IY = ("is_hukuku", "sosyal_guvenlik_mevzuati", "borclar_hukuku", "ticaret_hukuku",
                                "idari_yargilama_hukuku")

ek1 = [f"demo-hukuk-{n:03d}" for n in range(21, 27)]

# =============================================================================== TEST 1
T1 = paket("questions_hukuk_2026.json", 2026093051, ek1)

T1.sayisal("SGK md. 8",
    "Bir inşaat şirketi, yeni işe aldığı sigortalıyı 12 Mayıs sabahı şantiyede çalıştırmaya başlatacaktır."
    f"\n\n{SG}, işe giriş bildirgesinin süresinde verilmiş sayılması için en geç hangi gün Kuruma verilmesi gerekir? (Mayıs "
    "ayının günü)",
    "12", ["10", "11", "13", "15"],
    "Md. 8'e göre inşaat, balıkçılık ve tarım işyerlerinde işe giriş bildirgesi en geç sigortalının çalışmaya başlatıldığı gün "
    "verilirse süresinde verilmiş sayılır.", lesson=L_SG, topic="sosyal_guvenlik", zorluk="hard")

T1.q("SGK md. 4",
    "Bir ilçede çeşitli kişilerin sigortalılık statüsü belirlenmektedir."
    f"\n\n{SG}, aşağıdakilerden hangisi 4/b kapsamında sigortalı sayılır?",
    "Mahalle muhtarı",
    ["Hizmet akdiyle çalışan muhasebeci",
     "Kadrolu devlet memuru",
     "Belediye başkanı",
     "Sözleşmeli kamu personeli"],
    "Md. 4/1-b'ye göre köy ve mahalle muhtarları ile bağımsız çalışanlar 4/b kapsamındadır; hizmet akdiyle çalışanlar 4/a, "
    "kadrolu ve sözleşmeli kamu personeli ile belediye başkanları 4/c hükümlerine tabidir.", lesson=L_SG, topic="sosyal_guvenlik")

T1.q("SGK md. 16",
    f"{SG}, aşağıdakilerden hangisi hastalık sigortasından sigortalıya sağlanan haklardan biridir?",
    "Geçici iş göremezlik ödeneği",
    ["Sürekli iş göremezlik geliri",
     "Malullük aylığı",
     "Yaşlılık aylığı",
     "Ölüm toptan ödemesi"],
    "Md. 16'ya göre hastalık ve analık sigortasından iş göremezlik süresince geçici iş göremezlik ödeneği verilir; diğer haklar "
    "iş kazası veya uzun vadeli sigorta kollarından sağlanır.", lesson=L_SG, topic="primler_ve_sigorta_kollari", zorluk="easy")

T1.q("SGK md. 102",
    "Bir işverene, işe giriş bildirgesini geç verdiği için idari para cezası tebliğ edilmiştir."
    f"\n\n{SG26}, bu cezaya ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kuruma itiraz, takibi durdurmaz.",
    ["Cezalar tebliğ ile tahakkuk eder.",
     "Tebliğden itibaren on beş gün içinde ödenir.",
     "Peşin ödemede dörtte üçü tahsil edilir.",
     "Cezalar on yıllık zamanaşımına tabidir."],
    "Md. 102'ye göre idari para cezasına karşı tebliğden itibaren on beş gün içinde Kuruma itiraz edilebilir ve itiraz takibi "
    "durdurur; mahkemeye başvuru ise takibi durdurmaz.", lesson=L_SG, topic="sosyal_guvenlik", zorluk="hard")

T1.q("SGK md. 13",
    "Sigortalı işçi, işverence sağlanan servis aracıyla evinden işyerine giderken trafik kazası geçirmiştir."
    f"\n\n{SG}, bu olay hakkında aşağıdakilerden hangisi doğrudur?",
    "İş kazası olarak kabul edilir.",
    ["İş kazası sayılmaz.",
     "Sadece meslek hastalığı sayılır.",
     "Sadece işveren kusurluysa iş kazasıdır.",
     "Olay sadece trafik sigortasını ilgilendirir."],
    "Md. 13/e'ye göre sigortalıların işverence sağlanan bir taşıtla işin yapıldığı yere gidiş gelişi sırasında meydana gelen "
    "olay iş kazasıdır.", lesson=L_SG, topic="sosyal_guvenlik")

T1.sayisal("İK md. 17",
    "İşyerinde bir yıl iki aydır çalışan işçinin belirsiz süreli iş sözleşmesi işveren tarafından bildirimli feshedilecektir."
    f"\n\n{IK}, işverenin uyması gereken asgari bildirim süresi kaç haftadır?",
    "4", ["2", "6", "8", "10"],
    "Md. 17'ye göre işi altı aydan bir buçuk yıla kadar sürmüş işçi için bildirim süresi dört haftadır.",
    lesson=L_IS, topic="is_sozlesmesinin_sona_ermesi_yeterlilik")

T1.q("İK md. 41",
    "Bir işyerinde haftalık çalışma süresi 45 saattir; işveren bir işçiye, işçinin onayını almadan hafta sonu fazla çalışma "
    f"yaptırmak istemektedir.\n\n{IK26}, bu durum hakkında aşağıdakilerden hangisi doğrudur?",
    "Fazla çalışma için işçinin onayı gerekir.",
    ["İşveren onay almadan fazla çalışma yaptırabilir.",
     "Onay sadece gece çalışmasında gerekir.",
     "Onay sadece kadın işçilerden alınır.",
     "Onay yerine sendikaya yazılı bilgi verilmesi yeterli sayılır."],
    "Md. 41'e göre fazla saatlerle çalışmak için işçinin onayının alınması gerekir.", lesson=L_IS, topic="calisma_sureleri",
    zorluk="easy")

T1.q("İK md. 56",
    f"{IK}, on sekiz günlük yıllık izni olan işçinin iznini bölümler hâlinde kullanmasına ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Anlaşmayla, bir bölüm en az on gün olur.",
    ["İşveren izni tek taraflı olarak bölebilir.",
     "İzin en fazla iki güne bölünebilir.",
     "Yıllık izin bölünemez.",
     "Bölümlerin her biri beş günden az olamaz."],
    "Md. 56'ya göre yıllık izin işveren tarafından bölünemez; ancak tarafların anlaşmasıyla bir bölümü on günden aşağı olmamak "
    "üzere bölümler hâlinde kullanılabilir.", lesson=L_IS, topic="yillik_izin")

T1.q("İK md. 5",
    f"{IK}, aşağıdakilerden hangisi eşit davranma ilkesine aykırı değildir?",
    "Kıdem farkına göre farklı ikramiye ödenmesi",
    ["Cinsiyet nedeniyle düşük ücret ödenmesi",
     "Gebelik nedeniyle sözleşmenin feshedilmesi",
     "Kısmi süreli işçiye sebepsiz düşük menfaat",
     "Siyasi görüş nedeniyle terfi verilmemesi"],
    "Md. 5'e göre dil, ırk, cinsiyet, siyasi görüş gibi sebeplere dayalı ayrım ile esaslı sebep olmadan kısmi süreli veya belirli "
    "süreli işçiye farklı işlem yasaktır; kıdem gibi nesnel bir ölçüte dayalı fark ayrım değildir.", lesson=L_IS,
    topic="esit_davranma", zorluk="hard")

T1.q("TBK md. 12",
    f"{BK}, kanunda yazılı şekle bağlanan bir sözleşmenin bu şekle uyulmadan yapılmasının sonucu aşağıdakilerden "
    "hangisidir?",
    "Sözleşme hüküm doğurmaz.",
    ["Sözleşme geçerlidir.",
     "Sözleşme iptal edilebilir.",
     "Sözleşme sadece ispat edilemez.",
     "Tanıkla ispatlanırsa geçerli olur."],
    "Md. 12'ye göre kanunda öngörülen şekil kural olarak geçerlilik şeklidir; öngörülen şekle uyulmadan kurulan sözleşmeler hüküm "
    "doğurmaz.", lesson=L_BK, topic="sozlesmenin_kurulmasi", zorluk="easy")

T1.q("TBK md. 49",
    f"{BK}, haksız bir fiilden doğan sorumluluğa ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Zarar gören kusursuzluğu ispatlar.",
    ["Kusurlu ve hukuka aykırı fiil zararı gerektirir.",
     "Ahlaka aykırı kasıtlı zarar da giderilir.",
     "Zarar gören zararını ispatlar.",
     "Hâkim tazminatta kusurun ağırlığını gözetir."],
    "Md. 49 ve 50'ye göre zarar gören, zararını ve zarar verenin kusurunu ispat yükü altındadır; kusursuzluğu ispat etmek zarar "
    "görenin yükü değildir.", lesson=L_BK, topic="haksiz_fiil")

T1.sayisal("TBK md. 147",
    f"{BK}, otel konaklama bedeline ilişkin alacak kaç yıllık zamanaşımına tabidir?",
    "5", ["1", "2", "3", "10"],
    "Md. 147'ye göre otel, motel, pansiyon ve tatil köyü gibi yerlerdeki konaklama bedelleri beş yıllık zamanaşımına tabidir.",
    lesson=L_BK, topic="borc_iliskisi")

T1.q("TBK md. 162",
    f"{BK}, “Birden çok borçludan her biri, alacaklıya karşı borcun tamamından sorumlu olmayı kabul ettiğini bildirirse” "
    "hangi borç ilişkisi doğar?",
    "Müteselsil borçluluk",
    ["Kısmi borçluluk", "Bölünemeyen borç", "Seçimlik borç", "Çeşit borcu"],
    "Md. 162'ye göre borçlulardan her birinin borcun tamamından sorumlu olmayı kabul ettiğini bildirmesiyle müteselsil "
    "borçluluk doğar; bildirim yoksa ancak kanunda öngörülen hâllerde doğar.", lesson=L_BK, topic="borc_iliskisi")

T1.q("TTK md. 5",
    f"{TK}, dava olunan şeyin değerine bakılmaksızın ticari davalara bakmakla görevli mahkeme aşağıdakilerden hangisidir?",
    "Asliye ticaret mahkemesi",
    ["Sulh hukuk mahkemesi", "Tüketici mahkemesi", "İcra hukuk mahkemesi", "Asliye ceza mahkemesi"],
    "Asliye ticaret mahkemesi, dava değerinden bağımsız olarak ticari davalara bakar (md. 5/1); asliye hukuk mahkemesiyle "
    "arasındaki ilişki görev ilişkisidir.", lesson=L_TK, topic="ticari_isletme", zorluk="easy")

T1.q("TTK md. 651",
    "Hamile yazılı bir senet, hak sahibi (A)’nın çantasının çalınmasıyla zayi olmuştur."
    f"\n\n{TK}, (A) senet üzerindeki hakkını korumak için hangi mercie başvurmalıdır?",
    "Mahkemeye, iptal kararı için",
    ["Notere, yeni senet düzenlemesi için",
     "Ticaret sicili müdürlüğüne, tescil için",
     "Borçluya, ödemenin durdurulması için",
     "Kolluğa, senedin iptali ve yenisinin verilmesi için"],
    "Md. 651'e göre kıymetli evrak zayi olduğunda mahkeme tarafından iptaline karar verilebilir; iptal kararıyla hak sahibi "
    "hakkını senetsiz ileri sürebilir veya yeni senet isteyebilir.", lesson=L_TK, topic="ticari_isletme", zorluk="hard")

T1.oncul("TTK md. 124",
    f"{TK} aşağıdaki şirketler değerlendirilmektedir:",
    ["Anonim şirket", "Kollektif şirket", "Limited şirket", "Adi komandit şirket"],
    "Yukarıdakilerden hangileri şahıs şirketidir?",
    "II ve IV",
    ["I ve II", "I ve III", "II ve IV", "I, III ve IV", "II, III ve IV"],
    "Md. 124/2'ye göre kollektif (II) ve komandit (IV) şirketler şahıs şirketi; anonim (I) ve limited (III) şirketler sermaye "
    "şirketidir.", lesson=L_TK, topic="ticaret_sirketleri")

T1.q("TTK md. 21",
    f"{TK}, fatura alan kişinin içeriğe itiraz etmemesinin sonucuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sekiz günde itiraz etmezse kabul etmiş sayılır.",
    ["Süre sınırı olmadan itiraz edebilir.",
     "Otuz gün içinde itiraz etmezse kabul etmiş sayılır.",
     "İtiraz etmemek bir sonuç doğurmaz.",
     "Faturanın içeriği ancak noter onayıyla kesinleşir."],
    "Md. 21/2'ye göre fatura alan kişi aldığı tarihten itibaren sekiz gün içinde faturanın içeriği hakkında itirazda "
    "bulunmamışsa bu içeriği kabul etmiş sayılır.", lesson=L_TK, topic="tacir_yukumluluklari")

T1.sayisal("İYUK md. 7",
    "Bir memur, kendisine 3 Mart’ta tebliğ edilen disiplin cezasına karşı idare mahkemesinde dava açacaktır; özel kanunda "
    f"ayrı süre öngörülmemiştir.\n\n{IY}, dava açma süresi kaç gündür?",
    "60", ["15", "30", "45", "90"],
    "Md. 7/1'e göre özel kanunlarda ayrı süre gösterilmeyen hâllerde idare mahkemelerinde dava açma süresi altmış gündür; süre "
    "tebliği izleyen günden başlar.", lesson=L_IY, topic="idari_yargida_sureler_kanun_yollari", zorluk="easy")

T1.q("İYUK md. 14",
    f"{IY}, dava dilekçelerinin ilk incelemesinde aşağıdaki hususlardan hangisi incelenmez?",
    "Tanık beyanlarının doğruluğu",
    ["İdari merci tecavüzü",
     "Davacının ehliyeti",
     "Husumetin doğru gösterilmesi",
     "Kesin ve yürütülmesi gereken işlem"],
    "Md. 14/3'e göre ilk incelemede görev ve yetki, idari merci tecavüzü, ehliyet, kesin ve yürütülmesi gereken işlem, süre aşımı, "
    "husumet ve md. 3-5'e uygunluk incelenir.", lesson=L_IY, topic="idari_yargi_gorev_yetki")

T1.q("İYUK md. 27",
    f"{IY}, yürütmenin durdurulması kararına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Kural olarak teminatsız verilir.",
    ["İdareden teminat alınmaz.",
     "Açık hukuka aykırılık aranır.",
     "Telafisi güç zarar aranır.",
     "Karara bir defa itiraz edilebilir."],
    "Md. 27/6'ya göre yürütmenin durdurulması kararları teminat karşılığında verilir; ancak durumun gereklerine göre teminat "
    "aranmayabilir.", lesson=L_IY, topic="idari_dava_turleri", zorluk="hard")

# =============================================================================== TEST 2
T2 = paket("questions_hukuk_test2_2026.json", 2026093052)

T2.sayisal("SGK md. 26",
    "Sigortalı Bay (A), on iki yıldır sigortalıdır ve adına toplam 1.600 gün malullük, yaşlılık ve ölüm sigortası primi "
    f"bildirilmiştir.\n\n{SG}, malullük aylığı bağlanabilmesi için Bay (A) adına en az kaç gün daha prim bildirilmelidir?",
    "200", ["100", "400", "600", "2.000"],
    "Md. 26'ya göre malullük aylığı için en az on yıl sigortalılık ve toplam 1800 gün prim gerekir: 1.800 − 1.600 = 200 gün.",
    lesson=L_SG, topic="primler_ve_sigorta_kollari", zorluk="hard")

T2.q("SGK md. 6",
    f"{SG}, aşağıdakilerden hangisi kısa ve uzun vadeli sigorta kolları bakımından sigortalı sayılır?",
    "Ücretle çalışan işveren eşi",
    ["Er olarak askerlik yapan",
     "İşverenin işyerinde ücretsiz çalışan eşi",
     "Rehabilite edilen hasta",
     "Yedek astsubay okulu öğrencisi"],
    "Md. 6'ya göre işverenin işyerinde ücretsiz çalışan eşi, er ve erbaşlar, rehabilite edilenler ve yedek subay-astsubay okulu "
    "öğrencileri sigortalı sayılmaz; ücretle çalışan eş bu istisnanın dışındadır.", lesson=L_SG, topic="sosyal_guvenlik",
    zorluk="hard")

T2.q("SGK md. 81",
    f"{SG26}, aşağıdaki primlerden hangisinin tamamı işveren tarafından ödenir?",
    "Kısa vadeli sigorta kolları primi",
    ["Genel sağlık sigortası primi",
     "Malullük, yaşlılık ve ölüm primi",
     "İşsizlik sigortası primi",
     "Sigortalı hissesi dahil tüm uzun vadeli primler"],
    "Md. 81/c'ye göre kısa vadeli sigorta kolları primi prime esas kazancın %2,25'idir ve tamamını işveren öder; MYÖ ve GSS "
    "primlerinde sigortalı ve işveren hissesi vardır.", lesson=L_SG, topic="primler_ve_sigorta_kollari")

T2.q("SGK md. 3",
    f"{SG}, aşağıdakilerden hangisi uzun vadeli sigorta kollarından biri değildir?",
    "Analık sigortası",
    ["Malullük sigortası", "Yaşlılık sigortası", "Ölüm sigortası", "Malullük ve ölüm sigortası"],
    "Md. 3'e göre uzun vadeli sigorta kolları malullük, yaşlılık ve ölüm sigortalarıdır; analık sigortası kısa vadeli sigorta "
    "koludur.", lesson=L_SG, topic="primler_ve_sigorta_kollari", zorluk="easy")

T2.q("SGK md. 59",
    f"{SG}, Kurumun denetim memurlarının tespitlerinin dayandırılabileceği delillere ilişkin aşağıdakilerden hangisi "
    "doğrudur?",
    "Yemin hariç her türlü delile dayandırılabilir.",
    ["Sadece yazılı belgelere dayandırılabilir.",
     "Sadece tanık beyanına dayandırılabilir.",
     "Yemin dahil her türlü delile dayandırılabilir.",
     "Sadece işverenin beyanına dayandırılabilir."],
    "Md. 59'a göre denetim memurlarının tespit ettikleri Kurum alacağını doğuran olay ve işlemler yemin hariç her türlü delile "
    "dayandırılabilir.", lesson=L_SG, topic="sosyal_guvenlik", zorluk="hard")

T2.sayisal("İK md. 15",
    "Bir işletmede uygulanan toplu iş sözleşmesi deneme süresine ilişkin hüküm içermektedir."
    f"\n\n{IK}, deneme süresi toplu iş sözleşmesiyle en fazla kaç aya kadar uzatılabilir?",
    "4", ["2", "3", "6", "12"],
    "Deneme süresi kanunda en çok iki ay olarak öngörülmüştür (md. 15); toplu iş sözleşmesi bu süreyi en çok dört aya "
    "çıkarabilir.", lesson=L_IS, topic="is_sozlesmesi")

T2.q("İK md. 74",
    f"{IK26}, doğum sonrası analık izni sırasında annenin ölümü hâlinde kullanılamayan sürelere ilişkin aşağıdakilerden "
    "hangisi doğrudur?",
    "Kalan süreler babaya kullandırılır.",
    ["Kalan süreler düşer.",
     "Kalan süreler büyükanneye kullandırılır.",
     "Kalan süreler işverenin takdirine bırakılır.",
     "Kalan süreler ücretli izin olarak mirasçılara ödenir."],
    "Annenin doğumda veya sonrasında ölmesi hâlinde, doğum sonrası kullanılamayan analık izni süreleri md. 74 uyarınca "
    "babaya kullandırılır.", lesson=L_IS, topic="yillik_izin")

T2.q("İK md. 25",
    f"{IK}, aşağıdakilerden hangisi işverene ahlak ve iyiniyet kurallarına uymayan hâl nedeniyle derhal fesih hakkı "
    "verir?",
    "İşçinin işyerinde uyuşturucu kullanması",
    ["İşçinin yıllık izne çıkması",
     "İşçinin sendikaya üye olması",
     "İşçinin raporlu olması",
     "İşçinin ücret alacağını dava etmesi"],
    "Md. 25/II-d'ye göre işçinin işyerine sarhoş yahut uyuşturucu madde almış olarak gelmesi veya işyerinde bu maddeleri "
    "kullanması derhal fesih sebebidir.", lesson=L_IS, topic="is_sozlesmesinin_sona_ermesi_yeterlilik", zorluk="easy")

T2.q("İK md. 63",
    "Bir fabrikada haftalık çalışma düzeni belirlenirken işçi temsilcisi İş Kanunu hükümlerini sormaktadır."
    f"\n\n{IK}, bu düzenlemeye ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Denkleştirme süresi kural olarak altı aydır.",
    ["Genel olarak haftalık süre en çok kırk beş saattir.",
     "Farklı dağıtımda günlük süre on bir saati aşamaz.",
     "Denkleştirme süresi TİS ile dört aya çıkarılabilir.",
     "Turizmde denkleştirme süresi dört aydır."],
    "Md. 63'e göre denkleştirme süresi kural olarak iki aydır; toplu iş sözleşmeleriyle dört aya, turizm sektöründe altı aya "
    "kadar artırılabilir.", lesson=L_IS, topic="calisma_sureleri", zorluk="hard")

T2.q("TBK md. 36",
    f"{BK}, aldatma sonucu sözleşme yapan tarafa ilişkin aşağıdakilerden hangisi doğrudur?",
    "Yanılması esaslı olmasa da bağlı değildir.",
    ["Sadece esaslı yanılmada bağlı değildir.",
     "Sözleşme baştan geçersizdir.",
     "Sadece bedel indirimi isteyebilir.",
     "Aldatmayı öğrendikten sonra beş yıl içinde dava açmalıdır."],
    "Md. 36'ya göre taraflardan biri diğerinin aldatması sonucu sözleşme yapmışsa, yanılması esaslı olmasa bile sözleşmeyle bağlı "
    "değildir.", lesson=L_BK, topic="sozlesmenin_kurulmasi")

T2.sayisal("TBK md. 72",
    "Trafik kazası sonucu zarar gören (B), zararı ve tazminat yükümlüsünü 10 Ocak 2025’te öğrenmiştir; fiil ceza "
    f"kanunlarında daha uzun zamanaşımı gerektirmemektedir.\n\n{BK}, (B)’nin tazminat istemi en geç hangi yıl zamanaşımına "
    "uğrar?",
    "2027", ["2026", "2028", "2030", "2035"],
    "Md. 72'ye göre tazminat istemi zararı ve yükümlüyü öğrenmeden itibaren iki yıl geçmekle zamanaşımına uğrar: 10 Ocak 2025 + "
    "2 yıl = 10 Ocak 2027.", lesson=L_BK, topic="haksiz_fiil", zorluk="hard")

T2.q("TBK md. 117",
    f"{BK}, muaccel bir borcun borçlusunun temerrüde düşmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Belirlenen ifa gününün geçmesine rağmen ihtar gerekir.",
    ["Kural olarak alacaklının ihtarı gerekir.",
     "Haksız fiilde fiil anında temerrüt oluşur.",
     "İyiniyetli zenginleşende bildirim şarttır.",
     "Kötüniyetli zenginleşende zenginleşme anında temerrüt oluşur."],
    "Md. 117'ye göre ifa günü birlikte belirlenmişse bu günün geçmesiyle borçlu ihtara gerek olmaksızın temerrüde düşer.",
    lesson=L_BK, topic="borcun_ifasi", zorluk="hard")

T2.q("TBK md. 183",
    "Alacaklı (C), borçlu (D)’den olan alacağını, borçlunun onayını almadan ve yazılı sözleşmeyle (E)’ye devretmiştir; "
    f"sözleşmede devir yasağı yoktur.\n\n{BK}, bu devir hakkında aşağıdakilerden hangisi doğrudur?",
    "Borçlunun rızası olmadan geçerlidir.",
    ["Borçlunun rızası olmadığı için geçersizdir.",
     "Devir ancak noter onayıyla geçerlidir.",
     "Devir sadece mahkeme kararıyla olur.",
     "Devir için borçlunun hem rızası hem imzası şarttır."],
    "Md. 183-184'e göre kanun, sözleşme veya işin niteliği engel olmadıkça alacaklı borçlunun rızasını aramaksızın alacağını "
    "devredebilir; devrin geçerliliği yazılı şekle bağlıdır.", lesson=L_BK, topic="borc_iliskisi")

T2.q("TTK md. 647",
    f"{TK}, emre yazılı bir kıymetli evrakın devri için aşağıdakilerden hangisi gereklidir?",
    "Ciro ve senedin zilyetliğinin devri",
    ["Sadece sözlü anlaşma",
     "Borçlunun yazılı onayı",
     "Ticaret siciline tescil",
     "Noter onaylı devir sözleşmesi ve tescil"],
    "Md. 647-648'e göre kıymetli evrakın devri için her hâlde senet üzerindeki zilyetliğin devri şarttır; emre yazılı senetlerde "
    "ayrıca ciro gerekir.", lesson=L_TK, topic="ticari_isletme")

T2.q("TTK md. 855",
    "Taşıyıcı (L), Tacir (N)’ye ait eşyayı geç teslim etmiş ve Tacir (N) bu nedenle zarara uğramıştır; yolcu taşıması söz "
    f"konusu değildir.\n\n{TK}, (N)’nin bu zarara ilişkin istemi kaç yılda zamanaşımına uğrar?",
    "1 yılda",
    ["2 yılda", "3 yılda", "5 yılda", "10 yılda"],
    "Md. 855'e göre yolcunun ölümü veya bedensel zararında istem hakları on yılda, diğer zararlarda bir yılda zamanaşımına uğrar; "
    "süre eşyanın teslimiyle başlar.", lesson=L_TK, topic="ticari_isletme", zorluk="hard")

T2.q("TTK md. 574",
    f"{TK}, limited şirkete ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Ortak sayısı yüzü aşamaz.",
    ["Tek ortakla kurulabilir.",
     "Ortaklar şirket borçlarından sorumlu değildir.",
     "Tüzel kişiler de ortak olabilir.",
     "Pay devri için kural olarak genel kurul onayı gerekir."],
    "Md. 574'e göre limited şirkette ortakların sayısı elliyi aşamaz.", lesson=L_TK, topic="ticaret_sirketleri")

T2.sayisal("İYUK md. 45",
    "İdare mahkemesinin iptal kararı davalı idareye 5 Ekim’de tebliğ edilmiştir; karar kesin nitelikte değildir."
    f"\n\n{IY}, idare kararın tebliğinden itibaren kaç gün içinde istinaf yoluna başvurabilir?",
    "30", ["7", "15", "45", "60"],
    "Md. 45/1'e göre idare ve vergi mahkemelerinin kararlarına karşı tebliğden itibaren otuz gün içinde bölge idare mahkemesine "
    "istinaf yoluna başvurulabilir.", lesson=L_IY, topic="idari_yargida_sureler_kanun_yollari")

T2.q("İYUK md. 34",
    "Ankara’daki bir genel müdürlük, Antalya’daki bir otel için verilen yapı ruhsatını iptal etmiştir."
    f"\n\n{IY}, bu işleme karşı açılacak davada yetkili mahkeme aşağıdakilerden hangisidir?",
    "Antalya İdare Mahkemesi",
    ["Ankara İdare Mahkemesi", "Danıştay", "Davacının ikametgâhı mahkemesi", "İstanbul Bölge İdare Mahkemesi"],
    "Md. 34/1'e göre imar, ruhsat ve iskân gibi taşınmazlarla ilgili davalarda yetkili mahkeme taşınmazın bulunduğu yer idare "
    "mahkemesidir.", lesson=L_IY, topic="idari_yargi_gorev_yetki")

T2.q("İYUK md. 2",
    f"{IY}, idari dava türlerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Tam yargı sadece menfaat ihlalinde açılır.",
    ["İptal davası menfaati ihlal edilenlerce açılır.",
     "Tam yargı davası kişisel hakkı ihlal edilenlerce açılır.",
     "İdari sözleşme uyuşmazlıkları idari davadır.",
     "İptal davası hukuka aykırılık yönleriyle açılır."],
    "Md. 2/1'e göre tam yargı davaları idari eylem ve işlemlerden dolayı kişisel hakları doğrudan muhtel olanlar tarafından "
    "açılır; menfaat ihlali iptal davasının koşuludur.", lesson=L_IY, topic="idari_dava_turleri", zorluk="hard")

T2.q("TBK md. 29",
    "(A) ile (B), ileride (A)’ya ait bir arsanın (B)’ye satılması konusunda sözlü olarak anlaşmış ve bir önsözleşme yapmıştır."
    f"\n\n{BK}, bu önsözleşmenin geçerliliği hakkında aşağıdakilerden hangisi doğrudur?",
    "Geçerli değildir.",
    ["Sözlü olduğu için geçerlidir.",
     "Tanıkla ispatlanırsa geçerlidir.",
     "Taraflar imzalarsa ileride geçerli olur.",
     "Sadece tacirler arasında geçerlidir."],
    "Md. 29'a göre önsözleşmenin geçerliliği, kanundaki istisnalar dışında ileride kurulacak sözleşmenin şekline bağlıdır; "
    "taşınmaz satışı resmî şekle tabi olduğundan sözlü önsözleşme geçerli değildir.", lesson=L_BK,
    topic="sozlesmenin_kurulmasi", zorluk="hard")

# =============================================================================== TEST 3
T3 = paket("questions_hukuk_test3_2026.json", 2026093053)

T3.sayisal("SGK md. 28",
    "İlk defa bu Kanuna tabi olarak 4/b kapsamında sigortalı olan ve yaş şartını taşıyan bir kişi adına 7.500 gün "
    f"malullük, yaşlılık ve ölüm sigortaları primi bildirilmiştir.\n\n{SG}, bu kişinin yaşlılık aylığı için en az kaç gün daha "
    "prim bildirilmesi gerekir?",
    "1.500", ["0", "300", "1.800", "2.100"],
    "Md. 28'e göre ilk defa bu Kanuna tabi olanlarda yaşlılık aylığı için 9000 gün prim aranır; 7200 gün şartı sadece 4/a "
    "sigortalıları için uygulanır: 9.000 − 7.500 = 1.500 gün.", lesson=L_SG, topic="primler_ve_sigorta_kollari", zorluk="hard")

T3.q("SGK md. 21",
    f"{SG}, iş kazasının işverenin iş güvenliği mevzuatına aykırı hareketi sonucu meydana gelmesi hâlinde aşağıdakilerden "
    "hangisi doğrudur?",
    "Kurumun yaptığı ödemeler işverene ödettirilir.",
    ["Sigortalıya ödeme yapılmaz.",
     "Ödemeler sigortalıdan geri alınır.",
     "İşverenin kusuru dikkate alınmaz.",
     "Ödemelerin tamamı sigortalının hak sahiplerine yüklenir."],
    "Md. 21'e göre iş kazası işverenin kastı veya iş sağlığı ve güvenliği mevzuatına aykırı hareketi sonucu meydana gelmişse Kurumca "
    "yapılan ödemeler ve gelirin ilk peşin sermaye değeri işverene ödettirilir.", lesson=L_SG, topic="primler_ve_sigorta_kollari")

T3.q("SGK md. 12",
    f"{SG}, alt işverenin sigortalıları hakkında asıl işverenin sorumluluğuna ilişkin aşağıdakilerden hangisi doğrudur?",
    "Asıl işveren alt işverenle birlikte sorumludur.",
    ["Asıl işveren sorumlu değildir.",
     "Sadece alt işveren iflas ederse sorumludur.",
     "Sorumluluk alt işveren sözleşmesiyle kaldırılabilir.",
     "Asıl işveren sadece iş kazasından doğan primlerden sorumludur."],
    "Md. 12'ye göre sigortalılar üçüncü bir kişinin aracılığıyla işe girmiş olsalar dahi asıl işveren, Kanunun işverene yüklediği "
    "yükümlülüklerden dolayı alt işverenle birlikte sorumludur.", lesson=L_SG, topic="sosyal_guvenlik", zorluk="easy")

T3.q("SGK md. 3",
    "Genel sağlık sigortalısı Bay (A)’nın 22 yaşındaki, lise öğrenimi gören ve evli olmayan oğlu vardır; oğlunun kendi "
    f"sigortalılığı yoktur.\n\n{SG}, oğul hakkında aşağıdakilerden hangisi doğrudur?",
    "Bakmakla yükümlü olunan kişi değildir.",
    ["Bakmakla yükümlü olunan kişidir.",
     "Yirmi beş yaşına kadar kapsamdadır.",
     "Evli olmadığı sürece yaşa bakılmaz.",
     "Sadece anne sigortalıysa kapsamdadır."],
    "Md. 3/10'a göre lise ve dengi öğrenim gören evli olmayan çocuk yirmi yaşını doldurana kadar bakmakla yükümlü olunan kişidir; "
    "yirmi beş yaş sınırı yüksek öğrenim içindir.", lesson=L_SG, topic="sosyal_guvenlik", zorluk="hard")

T3.q("SGK md. 88",
    f"{SG}, 4/a sigortalısının primlerinin ödenmesine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Sigortalı hissesini işveren ücretten keserek öder.",
    ["Sigortalı hissesini sigortalı kendisi yatırır.",
     "Primler yıl sonunda toplu ödenir.",
     "Hak edilip ödenmeyen ücretlerin primi alınmaz.",
     "Primleri sigortalının bankası doğrudan Kuruma aktarır."],
    "Md. 88'e göre işveren sigortalı hissesi prim tutarlarını ücretlerden keserek ve kendi hissesini ekleyerek Kurumca belirlenen "
    "günün sonuna kadar öder.", lesson=L_SG, topic="primler_ve_sigorta_kollari")

T3.sayisal("İK md. 32",
    f"{IK}, işçi ücreti en geç kaç ayda bir ödenir?",
    "1", ["2", "3", "4", "6"],
    "Md. 32'ye göre ücret en geç ayda bir ödenir; iş sözleşmeleri veya toplu iş sözleşmeleriyle ödeme süresi bir haftaya kadar "
    "indirilebilir.", lesson=L_IS, topic="is_sozlesmesi", zorluk="easy")

T3.q("İK md. 27",
    f"{IK}, bildirim süresi içinde yeni iş arama iznine ilişkin aşağıdakilerden hangisi doğrudur?",
    "Günde en az iki saat, ücret kesilmeden verilir.",
    ["İşçinin ücretinden kesilerek verilir.",
     "Sadece işçinin talebiyle haftada bir gün verilir.",
     "İzin iş saatleri dışında verilir.",
     "İzin toplu olarak kullanılamaz."],
    "Md. 27'ye göre iş arama izni iş saatleri içinde ve ücret kesintisi yapılmadan günde en az iki saat olarak verilir; işçi "
    "isterse toplu kullanabilir.", lesson=L_IS, topic="is_sozlesmesinin_sona_ermesi_yeterlilik")

T3.q("İK md. 69",
    f"{IK26}, işçilerin gece çalışmasına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Gece çalışmasında fazla çalışma yaptırılabilir.",
    ["Gece çalışması kural olarak yedi buçuk saati geçemez.",
     "Turizmde yazılı onayla yedi buçuk saat aşılabilir.",
     "Gece en fazla on bir saat süren dönemdir.",
     "Posta değişiminde on bir saat dinlenme verilir."],
    "Md. 41 ve 69'a göre md. 69'da belirtilen gece çalışmasında fazla çalışma yapılamaz; gece çalışması kural olarak yedi buçuk "
    "saati geçemez.", lesson=L_IS, topic="calisma_sureleri", zorluk="hard")

T3.q("İK md. 53",
    "Otuz yaşındaki işçi, aynı işyerinde tam beş yıldır çalışmaktadır ve sözleşmesinde daha uzun izin öngörülmemiştir."
    f"\n\n{IK26}, bu işçiye verilecek yıllık ücretli izin en az kaç gündür?",
    "14 gün",
    ["20 gün", "26 gün", "18 gün", "12 gün"],
    "Md. 53'e göre hizmet süresi bir yıldan beş yıla kadar (beş yıl dahil) olanlara on dört günden az izin verilemez; tam beş yıl "
    "bu dilime girer.", lesson=L_IS, topic="yillik_izin", zorluk="hard")

T3.q("TBK md. 27",
    f"{BK}, aşağıdaki sözleşmelerden hangisi kesin hükümsüzdür?",
    "Kişilik haklarına aykırı sözleşme",
    ["Aldatma sonucu yapılan sözleşme",
     "Korkutma sonucu yapılan sözleşme",
     "Esaslı yanılmayla yapılan sözleşme",
     "Aşırı yararlanma içeren ve oransız edimli sözleşme"],
    "Md. 27'ye göre kanunun emredici hükümlerine, ahlaka, kamu düzenine, kişilik haklarına aykırı veya konusu imkânsız sözleşmeler "
    "kesin hükümsüzdür; irade bozuklukları ve aşırı yararlanma iptal edilebilirlik doğurur.", lesson=L_BK,
    topic="sozlesmenin_kurulmasi")

T3.q("TBK md. 66",
    "Bir inşaat şirketinin işçisi, iş sırasında kullandığı vinçle yoldan geçen bir kişiye zarar vermiştir."
    f"\n\n{BK}, şirketin sorumluluğuna ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Özen ispatıyla da kurtulamaz.",
    ["Çalışanın iş sırasında verdiği zarardan sorumludur.",
     "Seçme ve denetimde özeni ispatlarsa kurtulur.",
     "Çalışana bizzat sorumlu olduğu ölçüde rücu eder.",
     "İşletmede çalışma düzeninin elverişliliği aranır."],
    "Md. 66'ya göre adam çalıştıran, çalışanını seçerken, talimat verirken ve denetlerken gerekli özeni gösterdiğini ispat ederse "
    "sorumlu olmaz.", lesson=L_BK, topic="haksiz_fiil")

T3.sayisal("TBK md. 178",
    "Sözleşme yapılırken (K), (M)’den 25.000 ₺ cayma parası almıştır. (K) sonradan sözleşmeden caymıştır."
    f"\n\n{BK}, (K) (M)’ye kaç ₺ geri vermelidir?",
    "50.000", ["12.500", "25.000", "37.500", "75.000"],
    "Md. 178'e göre cayma parası kararlaştırılmışsa parayı alan taraf cayarsa aldığının iki katını geri verir: 25.000 × 2 = 50.000 ₺.",
    lesson=L_BK, topic="borc_iliskisi", zorluk="hard")

T3.q("TBK md. 89",
    f"{BK}, aksine anlaşma yoksa aşağıdaki borçlardan hangisi alacaklının ödeme zamanındaki yerleşim yerinde ifa edilir?",
    "Para borcu",
    ["Parça borcu", "Çeşit borcu", "Yapma borcu", "Belirli bir taşınmazın teslimi borcu"],
    "Md. 89'a göre para borçları alacaklının ödeme zamanındaki yerleşim yerinde, parça borçları borç konusunun bulunduğu yerde, "
    "diğer borçlar borçlunun yerleşim yerinde ifa edilir.", lesson=L_BK, topic="borcun_ifasi", zorluk="easy")

T3.q("TTK md. 55",
    f"{TK}, aşağıdakilerden hangisi dürüstlük kuralına aykırı davranış ve ticari uygulamalardan biri değildir?",
    "Rakipten daha kaliteli ürünü doğru tanıtmak",
    ["Rakibi yanıltıcı açıklamalarla kötülemek",
     "Almadığı ödülü almış gibi davranmak",
     "Müşteriyi saldırgan satış yöntemiyle sınırlamak",
     "Başkasının ürünüyle karıştırılmaya yol açmak"],
    "Md. 55'e göre kötüleme, gerçek dışı ödül iddiası, saldırgan satış ve karıştırılmaya yol açma haksız rekabettir; ürünü doğru "
    "bilgilerle tanıtmak dürüstlüğe aykırı değildir.", lesson=L_TK, topic="tacir_yukumluluklari")

T3.q("TTK md. 645",
    f"{TK}, kıymetli evrakın tanımına ilişkin aşağıdakilerden hangisi doğrudur?",
    "İçerdiği hak senetten ayrı ileri sürülemez.",
    ["Hak senetsiz de ileri sürülebilir.",
     "Senet sadece ispat belgesidir.",
     "Hak senetten bağımsız devredilir.",
     "Kıymetli evrak sadece bankalarca düzenlenebilir."],
    "Md. 645'e göre kıymetli evrak, içerdikleri hak senetten ayrı olarak ileri sürülemeyen ve başkalarına devredilemeyen "
    "senetlerdir.", lesson=L_TK, topic="ticari_isletme")

T3.q("TTK md. 82",
    f"{TK}, tacirin saklama yükümlülüğüne ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Alınan ticari mektuplar saklanmaz.",
    ["Ticari defterler on yıl saklanır.",
     "Gönderilen mektupların suretleri saklanır.",
     "Kayıtların dayandığı belgeler saklanır.",
     "Süre ilgili takvim yılının bitişiyle başlar."],
    "Md. 82/1'e göre tacir alınan ticari mektupları da sınıflandırılmış şekilde saklamakla yükümlüdür.", lesson=L_TK,
    topic="ticari_defterler", zorluk="easy")

T3.sayisal("İYUK md. 20/B",
    "ÖSYM’nin düzenlediği bir sınavın sonucu 14 Haziran’da açıklanmış ve adaya aynı gün duyurulmuştur."
    f"\n\n{IY}, aday sonuca karşı en geç Haziran ayının kaçıncı günü dava açabilir?",
    "24", ["21", "28", "29", "14"],
    "Md. 20/B'ye göre MEB ve ÖSYM tarafından yapılan merkezî sınavlara ilişkin davalarda dava açma süresi on gündür; md. 8'e göre "
    "süre bildirimi izleyen günden başlar: 14 + 10 = 24 Haziran.", lesson=L_IY, topic="idari_dava_turleri", zorluk="hard")

T3.q("İYUK md. 49",
    "Bölge idare mahkemesinin temyize açık bir kararı Danıştayda temyiz edilmiştir."
    f"\n\n{IY}, Danıştayın bu kararı bozabilmesi için aranan sebepler arasında aşağıdakilerden hangisi yer almaz?",
    "Kararın kısa gerekçeli olması",
    ["Görev dışında bir işe bakılması",
     "Yetki dışında bir işe bakılması",
     "Hukuka aykırı karar verilmesi",
     "Kararı etkileyen usul hatası"],
    "Md. 49/2'ye göre görev ve yetki dışında işe bakılması, hukuka aykırı karar ve kararı etkileyebilecek usul hatası veya "
    "eksikliği bozma sebebidir.", lesson=L_IY, topic="idari_yargida_sureler_kanun_yollari")

T3.q("İYUK md. 43",
    f"{IY}, görev ve yetki uyuşmazlıklarına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?",
    "Uyuşmazlık kararlarına karşı istinafa gidilebilir.",
    ["Aynı bölgede bölge idare mahkemesi çözer.",
     "Farklı bölgelerde Danıştay çözer.",
     "Yeniden açılan davada harç alınmaz.",
     "Kararlar taraflara tebliğ olunur."],
    "Md. 43/3'e göre görev ve yetki uyuşmazlıklarına ilişkin Danıştay ve bölge idare mahkemesi kararları kesindir.",
    lesson=L_IY, topic="idari_yargi_gorev_yetki", zorluk="hard")

T3.sayisal("İK md. 29",
    "Bir fabrikada 400 işçi çalışmaktadır ve işveren yapısal nedenlerle işçi çıkarmayı planlamaktadır."
    f"\n\n{IK}, bir aylık süre içinde en az kaç işçinin işine son verilmesi toplu işçi çıkarma sayılır?",
    "30", ["10", "20", "40", "50"],
    "Md. 29'a göre 301 ve daha fazla işçi çalışan işyerlerinde en az otuz işçinin bir aylık süre içinde işine son verilmesi "
    "toplu işçi çıkarma sayılır.", lesson=L_IS, topic="is_sozlesmesinin_sona_ermesi_yeterlilik", zorluk="hard")

if __name__ == "__main__":
    rc = 0
    for paket_ in (T1, T2, T3):
        rc |= paket_.yaz()
    sys.exit(rc)
