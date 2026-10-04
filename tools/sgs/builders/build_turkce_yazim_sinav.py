#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Türkçe — Yazım, Noktalama ve Anlatım Bozukluğu — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gerçek SGS 1-7 profiline göre baştan yazıldı (24 yazım, 18 noktalama, 18 anlatım bozukluğu); TDK Yazım Kılavuzu kurallarına dayanır. Eski pakette şıkların yarısı cevabı ele veren açıklayıcı parantez taşıyordu; iki soru birbiriyle çelişiyordu (zarf-fiil grubundan sonra virgül bir soruda yanlış, ötekinde doğru sayılıyordu) ve bir soru bozukluk olmayan cümleyi ('bütün öğrenciler ... girdiler') bozuk gösteriyordu. Yeni pakette paragraf içi ayraç noktalama, virgülün aynı görevi (numaralı cümleler), bozukluğun benzeri ve giderilme yolu soruları da var.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: SGS Türkçe 2021-2026 kitapçıkları — biçim kalibrasyonu; TDK Yazım Kılavuzu
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/turkce/yazim_noktalama_anlatim.json"
STYLE_REF = 'SGS Türkçe (gerçek sınav 1-7 profili)'
ONEK = "turkce-yazim-gen-"


def patch(stem, options, answer, solution, ref='Türkçe - yazım, noktalama, anlatım bozukluğu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        'Aşağıdaki cümlelerin hangisinde sayının yazımıyla ilgili bir yanlışlık yapılmıştır?',
        {
            'A': "Mahalle derneğinin toplantısı yarın saat 9.30'da okulun konferans salonunda başlayacak.",
            'B': 'Öğretmenimiz, ödev olarak kitabın III. bölümünü dikkatle okumamızı istedi.',
            'C': "Yazarın ilk romanı 1998'de küçük bir yayınevi tarafından yayımlandı.",
            'D': 'Kardeşim, ilçede düzenlenen satranç yarışmasında 3. olarak madalya aldı.',
            'E': "Açılış törenine beklenenin aksine 25'den fazla gazeteci ve fotoğrafçı geldi.",
        },
        'E',
        "Rakamla yazılan sayılara gelen ek, sayının okunuşuna göre yazılır: yirmi beşten → 25'ten. Diğer cümlelerde sıra sayısı, yıl ve saat yazımları doğrudur.",
    ),
    # düzey 2
    '0002': patch(
        'Aşağıdaki cümlelerin hangisinde anlamca çelişen sözcüklerin bir arada kullanılmasından kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'İş yerindeki toplantı erken biterse kesinlikle yarın akşam size gelebilirim.',
            'B': 'Hava güzel olursa yarın büyük olasılıkla bisikletle size gelirim.',
            'C': 'Önemli bir işim çıkmazsa cumartesi günkü toplantıya kesinlikle katılacağım.',
            'D': 'Yarın sabah hastaneye gideceğim için toplantıya gelemeyebilirim.',
            'E': 'Söz verdiğim gibi yarın sabah mutlaka erkenden gelir, size yardım ederim.',
        },
        'A',
        "'Kesinlikle' kesinlik, '-ebilir' olasılık bildirir; iki anlam bir arada kullanılamaz.",
    ),
    # düzey 3
    '0003': patch(
        '“Bu soruları çözmek için yeterli zaman ve dikkat göstermedi.” cümlesindeki anlatım bozukluğunun nedeni aşağıdakilerden hangisidir?',
        {
            'A': 'Gereksiz sözcük kullanılması',
            'B': 'Özne eksikliği',
            'C': 'Anlamca çelişen sözcüklerin kullanılması',
            'D': 'Ortak yüklemin ögelerden birine uymaması',
            'E': 'Zaman uyumsuzluğu',
        },
        'D',
        "'Dikkat göstermek' doğrudur ama 'zaman göstermek' denmez; ortak yüklem 'zaman' sözüne uymaz: 'yeterli zaman ayırmadı ve dikkat göstermedi' olmalıdır.",
    ),
    # düzey 2
    '0004': patch(
        'Aşağıdaki cümlelerin hangisinde sayı adının yazımı yanlıştır?',
        {
            'A': 'Mağazadaki bütün kışlık ürünlerde bu hafta sonuna kadar yüzde elli indirim var.',
            'B': 'Yaşlı adam, istasyonda kırk yıllık dostuyla karşılaşınca gözyaşlarını tutamadı.',
            'C': 'Bu yıl sınıfımızda otuz iki öğrenci var ve hepsi aynı mahallede oturuyor.',
            'D': 'Cumhuriyet, bin dokuz yüz yirmi üç yılında Türkiye Büyük Millet Meclisinde ilan edildi.',
            'E': 'Mahalle sakinlerinin düzenlediği toplantıya yirmibeş kişi katıldı ve karar alındı.',
        },
        'E',
        'Birden çok sözcükten oluşan sayı adları ayrı yazılır: yirmi beş.',
    ),
    # düzey 2
    '0005': patch(
        'Aşağıdaki cümlelerin hangisinde özne-yüklem uyumsuzluğundan kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Bu yıl düzenli çalışırsak sen ve ben üniversite sınavını mutlaka başaracaksınız.',
            'B': 'Ali ile Ayşe, dün akşam yeni açılan sinemaya birlikte gitti.',
            'C': 'Bahçemizdeki meyve ağaçları her yıl ilkbaharda bembeyaz çiçek açar.',
            'D': 'Toplantıya katılan herkes, konu hakkındaki görüşünü açıkça söyledi.',
            'E': 'Son sınıf öğrencileri, sınav sonuçlarını büyük bir heyecanla bekliyor.',
        },
        'A',
        "'Sen ve ben' öznesi birinci çoğul kişiyi (biz) karşılar; yüklem 'başaracağız' olmalıdır.",
    ),
    # düzey 2
    '0006': patch(
        'Aşağıdaki cümlelerin hangisinde nokta yanlış kullanılmıştır?',
        {
            'A': 'Okulumuzdaki bilgi yarışması bu yıl 15. Mayıs günü yapılacak.',
            'B': 'II. Dünya Savaşı 1945 yılında sona erdi ve dünya haritası yeniden çizildi.',
            'C': 'Kardeşim, okullar arası koşu yarışmasında 3. olunca çok sevindi.',
            'D': 'Konferansın açılış konuşmasını Prof. Dr. Ali Kaya yaptı.',
            'E': 'Öğretmen, kitabın 25. sayfasındaki soruları ödev olarak verdi.',
        },
        'A',
        'Nokta, sıra bildirmek için sayılardan sonra konur; tarih bildiren gün sayılarından sonra konmaz: 15 Mayıs. Diğerlerinde nokta kısaltma ve sıra sayısı için doğru kullanılmıştır.',
    ),
    # düzey 2
    '0007': patch(
        "Aşağıdaki cümlelerin hangisinde '-ken' ekinin yazımı yanlıştır?",
        {
            'A': 'Babam, yemek yerken televizyon izlemeyi pek sevmezdi.',
            'B': 'İşten eve dönerken fırına uğrayıp sıcak ekmek aldı.',
            'C': 'Çocukken her yaz dedemlerin köyündeki bu parkta oynardık.',
            'D': 'Sabah okula gider ken eski mahalleden bir arkadaşını gördü.',
            'E': 'Hava güzelken sahile inip uzun bir yürüyüşe çıkalım.',
        },
        'D',
        "'-ken' ektir ve bitişik yazılır: giderken.",
    ),
    # düzey 3
    '0008': patch(
        'Aşağıdaki cümlelerin hangisinde üç nokta, sıralanan örneklerin sürdürülebileceğini göstermek için kullanılmıştır?',
        {
            'A': 'Seni o kadar özledim ki her gün fotoğraflarına bakıp duruyorum...',
            'B': 'Ali... Ali... Neredesin, bütün bahçeyi aradım seni!',
            'C': 'Bir gün sana... Neyse, bunu şimdi konuşmanın zamanı değil.',
            'D': '“...Ne mutlu Türküm diyene!” sözünü her törende yeniden hatırlarım.',
            'E': 'Pazardan domates, biber, patlıcan... ne bulduysak aldık.',
        },
        'E',
        'Sıralanan sebzelerden sonra konan üç nokta, örneklerin sürdürülebileceğini gösterir. Diğerlerinde duygunun sözle anlatılamaması, sözün yarıda bırakılması, alıntının başının alınmaması ve seslenmenin yinelenmesi söz konusudur.',
    ),
    # düzey 3
    '0009': patch(
        'Aşağıdaki kısaltmalardan hangisinin ek alırken yazımı yanlıştır?',
        {
            'A': "kg.'dan",
            'B': "cm'den",
            'C': "TDK'nin",
            'D': "THY'ye",
            'E': "NATO'ya",
        },
        'A',
        "Ölçü kısaltmalarından sonra nokta konmaz: kg'dan. Büyük harfli kısaltmalara gelen ekler, kısaltmanın okunuşuna göre kesmeyle ayrılır (TDK'nin, THY'ye).",
    ),
    # düzey 3
    '0010': patch(
        'Aşağıdaki cümlelerin hangisinde farklı tümleç isteyen yüklemlerin ortak tümleçle kullanılmasından kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Kardeşim bu yazarın kitaplarını çok seviyor ve her fırsatta sık sık bahsediyor.',
            'B': 'Kurul, öğrencilerin hazırladığı projeyi ayrıntılı biçimde inceledi ve onayladı.',
            'C': 'Çocuk, sert mizaçlı amcasından hem korkuyor hem çekiniyordu.',
            'D': 'Kardeşim bu yazarın kitaplarını çok seviyor ve boş zamanlarında okuyor.',
            'E': 'Kardeşine her konuda güveniyor ve onu çok seviyor.',
        },
        'A',
        "'Sevmek' belirtme (-i), 'bahsetmek' ayrılma (-den) durumunda tümleç ister; ortak 'bu yazarın kitaplarını' tümleci ikinci yükleme uymaz: '...ve onlardan sık sık bahsediyor'.",
    ),
    # düzey 2
    '0011': patch(
        'Aşağıdaki cümlelerin hangisinde tarihin yazımı yanlıştır?',
        {
            'A': "Mahallemizdeki eski sinema binası 1950'li yıllarda yapılmış.",
            'B': "Türkiye Büyük Millet Meclisi 23 Nisan 1920'de Ankara'da açıldı.",
            'C': 'Veli toplantısı 5 Mayıs Pazartesi günü saat on dörtte okulda yapılacak.',
            'D': 'Okullar her yıl eylül ayında açılır, haziran ayında kapanır.',
            'E': "29 ekim 1923'te Cumhuriyet ilan edildi ve bu gün her yıl coşkuyla kutlanır.",
        },
        'E',
        "Belirli bir tarih bildiren ay adları büyük harfle başlar: 29 Ekim 1923. Belirli tarih bildirmeyen ay adı ('eylül ayında') küçük harfle yazılır.",
    ),
    # düzey 2
    '0012': patch(
        'Aşağıdaki cümlelerin hangisinde yer adının yazımı yanlıştır?',
        {
            'A': "Hafta sonu ailecek Ankara Kalesi'ni ziyaret edip çarşıda dolaştık.",
            'B': "Geçen yaz Marmara Denizi'nde yüzdük, akşamları da sahilde yürüdük.",
            'C': "Bu yaz arkadaşlarımla birlikte balonla Kapadokya'yı gezdik.",
            'D': 'Kışın arkadaşlarımla birlikte Uludağa kayak yapmaya gittik.',
            'E': "Doğu Karadeniz'in yeşil yaylaları özellikle yaz aylarında çok güzeldir.",
        },
        'D',
        "Özel adlara gelen çekim ekleri kesmeyle ayrılır: Uludağ'a. Diğer yer adları kurala uygun yazılmıştır.",
    ),
    # düzey 2
    '0013': patch(
        'Aşağıdaki cümlelerin hangisinde ses düşmesiyle ilgili bir yazım yanlışı vardır?',
        {
            'A': 'Komşumuzun büyük oğlu bu yıl askere gitti, annesi çok duygulandı.',
            'B': 'Yaşlı kadın, torununun alnına sevgiyle bir öpücük kondurdu.',
            'C': 'Soğuk havada üşüyen çocuk, burnunu cebindeki mendille sildi.',
            'D': 'Uzun yürüyüşün sonunda susuzluktan herkesin ağızı kurumuştu.',
            'E': 'Merdivenleri çıkarken göğsünde hafif bir ağrı hissetti.',
        },
        'D',
        "'Ağız' sözcüğü ünlüyle başlayan ek alınca ikinci hecedeki ünlü düşer: ağzı. 'Oğlu, burnu, göğsü, alnı' doğru yazılmıştır.",
    ),
    # düzey 2
    '0014': patch(
        'Aşağıdaki cümlelerin hangisinde büyük harflerin kullanımıyla ilgili bir yazım yanlışı vardır?',
        {
            'A': "Atatürk Caddesi'ndeki eski binalar kentsel dönüşüm kapsamında yıkılıyor.",
            'B': "Öğretmenimizin okumamızı önerdiği romanın adı Kuyucaklı Yusuf'tu.",
            'C': "Cumhuriyet Bayramı'nda okulda coşkulu bir tören yapıldı.",
            'D': 'Toplantıya üniversiteden Prof. Dr. Ayşe Yılmaz da katıldı.',
            'E': 'Geçen yaz ailecek Karadeniz bölgesini baştan sona gezdik.',
        },
        'E',
        'Coğrafi bölge adlarında her sözcük büyük harfle başlar: Karadeniz Bölgesi. Diğer cümlelerde unvan, bayram, eser ve cadde adları kurala uygun yazılmıştır.',
    ),
    # düzey 2
    '0015': patch(
        '“Herkes bu kararı yerinde buldular.” cümlesindeki anlatım bozukluğu aşağıdakilerin hangisiyle giderilebilir?',
        {
            'A': 'Cümleye özne eklenerek',
            'B': 'Yüklem tekil yapılarak',
            'C': "'bu' sözcüğü 'şu' yapılarak",
            'D': "'yerinde' sözcüğü atılarak",
            'E': "'Herkes' sözcüğü çıkarılarak",
        },
        'B',
        "'Herkes' tekil bir belgisiz zamirdir; yüklem 'buldu' biçiminde tekil olmalıdır.",
    ),
    # düzey 3
    '0016': patch(
        'Aşağıdaki cümlelerin hangisinde anlatım bozukluğu yoktur?',
        {
            'A': 'İşlerim erken biterse mutlaka bu akşam size uğrayabilirim.',
            'B': 'Bu konuyu daha önce hiç bu açıdan düşünmemiştim.',
            'C': 'Sınavdan çıkan herkes, sonuçları kapının önünde merakla bekliyorlardı.',
            'D': 'Market fiyatları her geçen gün biraz daha pahalanıyor.',
            'E': 'Bu yaz tatilde hem iyice dinlendik hem de çok eğlenceliydi.',
        },
        'B',
        "Diğer cümlelerde çelişen anlam ('mutlaka - uğrayabilirim'), özne-yüklem uyumsuzluğu ('herkes - bekliyorlardı'), yanlış sözcük ('fiyat pahalanmaz, yükselir') ve yüklem uyumsuzluğu vardır.",
    ),
    # düzey 2
    '0017': patch(
        'Aşağıdaki cümlelerin hangisinde bağlacın yanlış kullanılmasından kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Sınavdan önceki haftalarda çok çalıştı ama sınavı rahatlıkla kazandı.',
            'B': 'Sınavdan önceki haftalarda çok çalıştığı için sınavı kazandı.',
            'C': 'Hava oldukça soğuktu, yine de arkadaşlarla denize girdik.',
            'D': 'Uzun yolculuktan sonra çok yorgundu; bu yüzden erken yattı.',
            'E': 'Sabahtan beri yağmur yağıyordu ama şemsiyesini evde unutmuştu.',
        },
        'A',
        "'Ama' karşıtlık bildirir; çok çalışmak ile sınavı kazanmak arasında karşıtlık değil neden-sonuç ilişkisi vardır.",
    ),
    # düzey 2
    '0018': patch(
        'Aşağıdaki cümlelerin hangisinde noktalama yanlışı yoktur?',
        {
            'A': 'Kırtasiyeden kitap, defter, ve kalem alıp eve döndüm.',
            'B': 'Yarın görüşürüz, dedi, ve kapıyı kapatıp gitti.',
            'C': 'Eyvah, son otobüsü de kaçırdık!',
            'D': "Toplantı saat 14.00'te başladı ve akşama kadar sürdü?",
            'E': 'Bu saatte apar topar nereye gidiyorsun.',
        },
        'C',
        "Ünlemden sonra virgül ve duygu cümlesi sonunda ünlem doğru kullanılmıştır. Soru cümlesinin sonuna soru işareti konmalı, 've'den önce virgül konmamalı, bildirme cümlesi soru işaretiyle bitmemelidir.",
    ),
    # düzey 3
    '0019': patch(
        'I. Ali, kitabını bana getirir misin?\nII. Evet, bu akşam size gelirim.\nIII. Çocuk, annesini görünce koşmaya başladı.\nIV. Sınıfa girdi, öğretmeni selamladı, yerine oturdu.\nV. Hayır, bu teklifi kabul edemem.\n\nVirgül, numaralanmış cümlelerin hangilerinde aynı görevde kullanılmıştır?',
        {
            'A': 'IV ve V',
            'B': 'III ve IV',
            'C': 'I ve II',
            'D': 'II ve V',
            'E': 'I ve III',
        },
        'D',
        "II ve V'te virgül, cümle başındaki cevap sözlerinden ('Evet, Hayır') sonra kullanılmıştır. I'de hitaptan sonra, III'te özneyi belirginleştirmek için, IV'te sıralı cümleleri ayırmak için kullanılmıştır.",
    ),
    # düzey 2
    '0020': patch(
        'Aşağıdaki cümlelerin hangisinde mantık hatasından kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Sınava on dakika geç kaldığı için görevliler onu içeri almadı.',
            'B': 'Yağmur şiddetlenince hakem maçı ertelemeye karar verdi.',
            'C': 'Bütün dönem boyunca tembellik ettiği için sınıfın en başarılısı seçilip ödül aldı.',
            'D': 'Gün boyu bahçede çalışıp çok yorulduğu için erkenden yattı.',
            'E': 'Gişede bilet kalmadığı için konsere gidemedik ve eve döndük.',
        },
        'C',
        'Tembellik ödül almanın nedeni olamaz; neden-sonuç ilişkisi mantıksız kurulmuştur.',
    ),
    # düzey 3
    '0021': patch(
        'Aşağıdaki cümlelerin hangisinde birleşik fiilin yazımı yanlıştır?',
        {
            'A': 'Bana yaptığı bu haksızlıktan sonra onu asla af etmeyeceğim.',
            'B': 'Öğrenci, dönem ödevini zamanında öğretmenine teslim etti.',
            'C': 'Yolda düşen yaşlı adama hep birlikte yardım ettik.',
            'D': 'Toplantıya geç kaldığı için herkesten içtenlikle özür diledi.',
            'E': 'Kalabalık bir şehirde yaşamasına rağmen kendini çok yalnız hissetti.',
        },
        'A',
        "Birleşik fiilde ses düşmesi ya da türemesi olursa birleşik fiil bitişik yazılır: af + etmek → affetmek. 'Teslim etmek, yardım etmek' ses olayı olmadığı için ayrı; 'hissetmek' (his+etmek) bitişik yazılır.",
    ),
    # düzey 3
    '0022': patch(
        'Aşağıdaki cümlelerin hangisinde virgül, öznenin belirginleşmesini sağlamak için kullanılmıştır?',
        {
            'A': 'Genç, kadına otobüse binerken yardım etti.',
            'B': 'Evet, bu işi yarın sabah ben yapacağım.',
            'C': 'Ali, akşam yemeğe buraya gelir misin?',
            'D': 'Kırtasiyeden kitap, defter ve kalem aldı.',
            'E': 'Kapıyı yavaşça açtı, içeri sessizce girdi.',
        },
        'A',
        "Virgül konmasaydı 'genç kadın' bir sıfat tamlaması olarak anlaşılırdı. Virgül, 'genç'in özne olduğunu belirginleştirir. Diğerlerinde virgül cevap, hitap, eş görevli sözcükler ve sıralı cümleler için kullanılmıştır.",
    ),
    # düzey 2
    '0023': patch(
        'Aşağıdaki cümlelerin hangisinde ünsüz yumuşamasıyla ilgili bir yazım yanlışı vardır?',
        {
            'A': 'Sokağın sonunda çocukların oynadığı küçük bir park vardı.',
            'B': 'Okuduğu kitabı masanın üstünde unutup aceleyle çıkmış.',
            'C': 'Mutfaktaki dolabın kapağı taşınırken kırılmış.',
            'D': 'Yorulunca yaşlı ağaçın gölgesinde biraz dinlendik.',
            'E': 'Annem, yeni aldığımız halının renginden pek hoşlanmadı.',
        },
        'D',
        "'Ağaç' sözcüğü ünlüyle başlayan ek alınca sondaki 'ç' yumuşar: ağacın. Diğer sözcüklerde yumuşama doğru yansıtılmıştır.",
    ),
    # düzey 2
    '0024': patch(
        'Aşağıdaki cümlelerin hangisinde yazım yanlışı yoktur?',
        {
            'A': 'Toplantıya katılan herkes, yönetimin bu kararını doğru buldu.',
            'B': 'Herkez bu karara itiraz etti ve toplantıyı terk etti.',
            'C': 'Bu konuda hiç bir fikrim yok, istersen başkasına sor.',
            'D': 'Yarınki maçı arkadaşlarınla birlikte izleyecekmisin?',
            'E': 'Toplantı yarın saat üçde başlayacak, geç kalmayalım.',
        },
        'A',
        "'Herkez' yerine 'herkes', 'hiç bir' yerine 'hiçbir', 'üçde' yerine 'üçte', 'izleyecekmisin' yerine 'izleyecek misin' yazılmalıdır.",
    ),
    # düzey 2
    '0025': patch(
        'Aşağıdaki cümlelerin hangisinin sonuna ünlem işareti konmalıdır?',
        {
            'A': 'Yönetim kurulu toplantısı yarın saat üçte başlayacak',
            'B': 'Yarın sabah güneş doğmadan erkenden yola çıkacağız',
            'C': 'Tahtadaki bu zor soruyu sınıfta kim çözdü',
            'D': 'Eyvah, koşarak geldik ama otobüsü yine kaçırdık',
            'E': 'Okuduğum kitabı salondaki masanın üstüne bıraktım',
        },
        'D',
        "'Eyvah' ünlemiyle başlayan, şaşkınlık ve üzüntü bildiren cümlenin sonuna ünlem işareti konur.",
    ),
    # düzey 2
    '0026': patch(
        'Aşağıdaki cümlelerin hangisinde unvanın yazımı yanlıştır?',
        {
            'A': "Bu konuyu bir de muhasebeden Ahmet bey'e danışalım.",
            'B': "Fatih Sultan Mehmet, İstanbul'u 1453 yılında fethetti.",
            'C': 'Ayşe Hanım, rahatsızlığı nedeniyle toplantıya katılmadı.',
            'D': 'Acil serviste Dr. Selim Kaya hastayı hemen muayene etti.',
            'E': 'Konferansta Prof. Dr. Elif Arslan iklim değişikliği üzerine konuştu.',
        },
        'A',
        "Özel adlardan sonra gelen saygı sözleri büyük harfle başlar: Ahmet Bey'e. Diğer unvanlar kurala uygun yazılmıştır.",
    ),
    # düzey 3
    '0027': patch(
        'Aşağıdaki cümlelerin hangisinde noktalı virgül yanlış kullanılmıştır?',
        {
            'A': 'Gece boyunca uyumamıştı; yine de sabahki toplantıya katıldı.',
            'B': 'Ali, Ayşe ve Can birinci sınıfta; Elif, Deniz ve Selin ikinci sınıftaydı.',
            'C': 'Bizim takımın oyuncuları dinçti; rakip takımın oyuncuları ise yorgundu.',
            'D': 'Sınava aylarca çalıştı; ancak istediği sonucu alamadı.',
            'E': 'Baharla birlikte bahçede güller; laleler ve papatyalar açmıştı.',
        },
        'E',
        "Eş görevli sözcükleri ayırmak için noktalı virgül değil virgül kullanılır: güller, laleler ve papatyalar. Diğer cümlelerde noktalı virgül; 'ancak, yine de' öncesinde, virgüllerle ayrılmış takımlar ve karşıt yargılar arasında doğru kullanılmıştır.",
    ),
    # düzey 2
    '0028': patch(
        'Aşağıdaki cümlelerin hangisinde kalın yazılmış sözcüğün yazımı yanlıştır?',
        {
            'A': 'Sınavdaki soruların **hiçbiri** beklediğimiz kadar zor değildi.',
            'B': 'Bu konuyu sana **birçok** kez söyledim ama dinlemedin.',
            'C': 'Toplantıdan önce sana **birşey** söylemek istiyorum.',
            'D': 'Yolculuk sırasında **herhangi** bir sorun olursa beni ara.',
            'E': 'Yarışmaya katılan öğrencilerin **her biri** bir ödül aldı.',
        },
        'C',
        "'Bir şey' ayrı yazılır. 'Birçok, herhangi, hiçbiri' bitişik; 'her biri' ayrı yazılır.",
    ),
    # düzey 2
    '0029': patch(
        "Aşağıdaki cümlelerin hangisinde 'de'nin yazımı yanlıştır?",
        {
            'A': 'Annem kitapları da defterleri de çantama özenle yerleştirdi.',
            'B': 'Dün yapılan toplantıda önemli kararlar alındı.',
            'C': 'Bu akşam sen de bize gel, birlikte yemek yiyelim.',
            'D': 'Geçen ay sende kalan kitabı yarın getirir misin?',
            'E': 'Bu konuyu bende senin gibi yeni öğrendim.',
        },
        'E',
        "Cümlede 'ben de' (dahi) anlamı vardır; bağlaç olan 'de' ayrı yazılmalıdır. 'Sende kalan kitap' sözündeki '-de' bulunma durumu ekidir ve bitişik yazılır.",
    ),
    # düzey 3
    '0030': patch(
        'Eyvah ( ) anahtarı evde unuttum ( ) Şimdi ne yapacağız ( ) Kapıcıyı mı çağırsak, çilingiri mi ( )\n\nBu parçada ayraçlarla ( ) belirtilen yerlere aşağıdaki noktalama işaretlerinden hangileri sırasıyla getirilmelidir?',
        {
            'A': '(!) (.) (?) (?)',
            'B': '(,) (.) (?) (.)',
            'C': '(,) (!) (.) (?)',
            'D': '(,) (!) (?) (?)',
            'E': '(;) (!) (?) (?)',
        },
        'D',
        'Ünlemden sonra cümle küçük harfle sürdüğü için virgül, şaşkınlık bildiren cümlenin sonunda ünlem, iki soru cümlesinin sonunda soru işareti kullanılır.',
    ),
    # düzey 2
    '0031': patch(
        "Aşağıdaki cümlelerin hangisinde 'ki'nin yazımı yanlıştır?",
        {
            'A': 'Konuşma bitince salona öyleki bir sessizlik çöktü, kimse sesini çıkaramadı.',
            'B': 'Yarınki toplantıya önemli bir işim çıktığı için katılamayacağım.',
            'C': 'Bütün sorunlarına rağmen sanki her şey yolundaymış gibi davrandı.',
            'D': 'İşlerimiz erken biterse belki akşam size uğrarız.',
            'E': 'Duydum ki geçen ay yeni bir işe başlamışsın, hayırlı olsun.',
        },
        'A',
        "'Öyle ki' yapısındaki 'ki' bağlaçtır ve ayrı yazılır. 'Sanki, belki' kalıplaşmış olduğu için bitişik; 'yarınki' sözündeki '-ki' ektir.",
    ),
    # düzey 3
    '0032': patch(
        'Dünkü toplantıda üç karar alındı ( ) bütçe onaylandı ( ) yeni personel alınması kabul edildi ( ) şube açılışı ertelendi ( )\n\nBu parçada ayraçlarla ( ) belirtilen yerlere aşağıdaki noktalama işaretlerinden hangileri sırasıyla getirilmelidir?',
        {
            'A': '(:) (;) (,) (.)',
            'B': '(:) (,) (,) (.)',
            'C': '(:) (,) (,) (...)',
            'D': '(;) (,) (,) (.)',
            'E': '(.) (,) (,) (.)',
        },
        'B',
        'Açıklama niteliğindeki sıralamadan önce iki nokta, sıralanan cümleler arasında virgül, cümle sonunda nokta kullanılır. Ayraçtan sonraki sözcük küçük harfle başladığı için ilk ayraca nokta gelemez.',
    ),
    # düzey 2
    '0033': patch(
        'Aşağıdaki cümlelerin hangisinde birleşik sözcüğün yazımı yanlıştır?',
        {
            'A': 'Bayram harçlığından herkes kendi payını alıp sevinçle teşekkür etti.',
            'B': 'Ustalar bu işi birkaç günde bitirip evi bize teslim etti.',
            'C': 'Tanık, kazanın nasıl olduğunu her şeyiyle polise anlattı.',
            'D': 'Bu yaz tatilinde bir çok kitap okudum ve not aldım.',
            'E': 'Akşamüstü yola çıktık ve gece yarısı köye vardık.',
        },
        'D',
        "'Birçok' bitişik yazılır. 'Herkes, birkaç, akşamüstü' bitişik; 'her şey' ayrı yazılır.",
    ),
    # düzey 2
    '0034': patch(
        'Aşağıdaki cümlelerin hangisinde zaman uyumsuzluğundan kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Babam her sabah erkenden yürüyüş yapar, sonra kahvaltı eder.',
            'B': 'Dün akşam yoğun trafik yüzünden eve geç döndüm.',
            'C': 'Yarın erkenden kalkıp dedemlerin köyüne doğru yola çıkacağız.',
            'D': 'Geçen yıl bu okula başladım ve burada çok mutlu olacağım.',
            'E': 'Haftaya sınavımız olduğu için şimdiden düzenli çalışıyoruz.',
        },
        'D',
        "Geçmişte gerçekleşen bir olayın sonucu gelecek zamanla verilmiştir; 'çok mutlu oldum' olmalıdır.",
    ),
    # düzey 3
    '0035': patch(
        'Aşağıdaki cümlelerin hangisinde kesme işareti doğru kullanılmıştır?',
        {
            'A': "Annem'e doğum gününde en sevdiği çiçeklerden aldım.",
            'B': "Bu romanı 2015'te bir arkadaşımın önerisiyle okumuştum.",
            'C': "Kardeşim, burs için Millî Eğitim Bakanlığı'na dilekçe verdi.",
            'D': "Yabancı arkadaşımız Türkçe'yi artık çok iyi konuşuyor.",
            'E': "Bu yıl izinlerimizi birleştirip Ekim'de tatile çıkacağız.",
        },
        'B',
        "Rakamla yazılan sayılara gelen ekler kesmeyle ayrılır: 2015'te. Dil adlarına (Türkçeyi), kurum adlarına (Bakanlığına), cins isimlere (anneme) ve belirli bir tarih bildirmeyen ay adlarına (ekimde) gelen ekler kesmeyle ayrılmaz.",
    ),
    # düzey 2
    '0036': patch(
        'Aşağıdaki cümlelerin hangisinde bir yazım yanlışı vardır?',
        {
            'A': 'Yaşlı adam, kalabalık şehirde yanlız yaşamaktan hoşlanmazdı.',
            'B': 'Tatilden birkaç gün içinde döneceğimizi söyledik.',
            'C': 'Toplantıdaki herkes bu konuda aynı fikirdeydi.',
            'D': 'Yanlış anlaşılmak istemediği için sözlerini dikkatle seçti.',
            'E': 'Taşındıktan sonra mahalledeki her şey değişmiş gibiydi.',
        },
        'A',
        "Doğru yazım 'yalnız'dır. Diğer cümlelerde yazım yanlışı yoktur.",
    ),
    # düzey 3
    '0037': patch(
        'Kitapçıdan şunları aldım ( ) iki roman, bir sözlük ve bir harita ( ) Kasada ödeme yaparken satıcı sordu ( ) “Poşet ister misiniz ( )”\n\nBu parçada ayraçlarla ( ) belirtilen yerlere aşağıdaki noktalama işaretlerinden hangileri sırasıyla getirilmelidir?',
        {
            'A': '(:) (.) (,) (?)',
            'B': '(,) (.) (:) (!)',
            'C': '(:) (...) (:) (.)',
            'D': '(;) (.) (:) (?)',
            'E': '(:) (.) (:) (?)',
        },
        'E',
        "'Şunları' ile duyurulan sıralamadan önce iki nokta, cümle sonunda nokta, doğrudan aktarılan sözden önce iki nokta, aktarılan soru cümlesinin sonunda soru işareti kullanılır.",
    ),
    # düzey 2
    '0038': patch(
        '“Bu ürünün fiyatı geçen aya göre oldukça ucuzladı.” cümlesindeki anlatım bozukluğunun nedeni aşağıdakilerden hangisidir?',
        {
            'A': 'Ek eksikliği',
            'B': 'Gereksiz sözcük kullanılması',
            'C': 'Anlamca çelişen sözcüklerin kullanılması',
            'D': 'Sözcüğün yanlış anlamda kullanılması',
            'E': 'Özne-yüklem uyumsuzluğu',
        },
        'D',
        "Mal ucuzlar, fiyat düşer. 'Fiyatı ucuzladı' sözünde 'ucuzlamak' yanlış anlamda kullanılmıştır: 'fiyatı düştü' olmalıdır.",
    ),
    # düzey 2
    '0039': patch(
        '“Sevgili öğrenciler, bugün size yeni bir konu anlatacağım.” cümlesinde virgül hangi amaçla kullanılmıştır?',
        {
            'A': 'Özneyi belirginleştirmek için',
            'B': 'Seslenme sözünü ayırmak için',
            'C': 'Ara sözü ayırmak için',
            'D': 'Cevap bildiren sözü ayırmak için',
            'E': 'Sıralı cümleleri ayırmak için',
        },
        'B',
        "'Sevgili öğrenciler' bir seslenmedir (hitap); hitap sözlerinden sonra virgül konur.",
    ),
    # düzey 2
    '0040': patch(
        '“Akşam olunca kasabanın sokakları boşalır, dükkânlar kepenk indirirdi.” cümlesinde virgül hangi amaçla kullanılmıştır?',
        {
            'A': 'Ara sözü ayırmak için',
            'B': 'Cevap bildiren sözü ayırmak için',
            'C': 'Eş görevli sözcükleri ayırmak için',
            'D': 'Sıralı cümleleri ayırmak için',
            'E': 'Seslenme sözünü ayırmak için',
        },
        'D',
        "Virgül, 'sokakları boşalır' ve 'dükkânlar kepenk indirirdi' biçimindeki iki sıralı cümleyi birbirinden ayırır.",
    ),
    # düzey 3
    '0041': patch(
        '“Sınavı kazanmak için yaklaşık iki yıla yakın çalıştı.” cümlesindeki anlatım bozukluğunun benzeri aşağıdakilerin hangisinde vardır?',
        {
            'A': 'Proje hazırlandı ve kurula sundu.',
            'B': 'Kesinlikle yarın gelebilirim.',
            'C': 'Tahminen yüz kişi kadar geldi.',
            'D': 'Sen ve ben bu işi başaracaksınız.',
            'E': 'Kitabı sevdi ve sık sık bahsetti.',
        },
        'C',
        "Verilen cümlede 'yaklaşık' ile 'yakın' aynı anlamı karşılar (gereksiz sözcük). Benzer bozukluk 'tahminen' ile 'kadar' sözlerinin birlikte kullanıldığı cümlededir.",
    ),
    # düzey 2
    '0042': patch(
        'Toplantıya katılanlar şunlardı ( ) müdür, iki uzman ve sekreter.\n\nBu cümlede ayraçla gösterilen yere aşağıdaki noktalama işaretlerinden hangisi getirilmelidir?',
        {
            'A': 'Noktalı virgül',
            'B': 'Virgül',
            'C': 'Kısa çizgi',
            'D': 'Üç nokta',
            'E': 'İki nokta',
        },
        'E',
        "'Şunlardı' ile duyurulan açıklayıcı sıralamadan önce iki nokta konur.",
    ),
    # düzey 2
    '0043': patch(
        'Aşağıdaki cümlelerin hangisinde iki nokta yanlış kullanılmıştır?',
        {
            'A': 'Başarının tek bir sırrı vardır: düzenli ve sabırlı çalışmak.',
            'B': 'Yazarın konuşmasındaki son söz şuydu: Okumayan toplum ilerleyemez.',
            'C': 'Annemin getirdiği sepette şunlar vardı: elma, armut, ayva.',
            'D': 'Mutfaktan annem seslendi: “Yemek hazır, sofraya gelin!”',
            'E': 'Dünkü toplantıya: müdür, iki uzman ve ben katıldık.',
        },
        'E',
        "İki nokta, açıklama ya da örnek verilecek sözden sonra, aktarılan sözden önce kullanılır; özne ile yüklem arasına konmaz. 'Toplantıya: müdür ...' kullanımı cümlenin ögelerini böler.",
    ),
    # düzey 2
    '0044': patch(
        'Aşağıdaki cümlelerin hangisinde virgülün kullanımı yanlıştır?',
        {
            'A': 'Manavdan elma, armut ve ayva alıp eve döndük.',
            'B': 'Evet, yarın akşam işten çıkınca size uğrayacağım.',
            'C': 'Kardeşim, ve ben yıllardır aynı okula gidiyoruz.',
            'D': 'Sevgili arkadaşlar, toplantımız birazdan başlıyor.',
            'E': 'Yaşlı, yorgun adam saatlerdir kapıda bekliyordu.',
        },
        'C',
        "'Ve' bağlacından önce virgül konmaz. Diğer cümlelerde virgül cevap sözünden sonra, eş görevli sözcükler arasında ve hitaptan sonra doğru kullanılmıştır.",
    ),
    # düzey 2
    '0045': patch(
        'Aşağıdaki cümlelerin hangisinde kalın yazılmış sözün yazımında büyük harflerle ilgili bir yanlışlık yapılmıştır?',
        {
            'A': '**Ayşe Hanım** rahatsızlığı nedeniyle bugün işe gelmedi.',
            'B': '**Türk Dil Kurumu** güncellenmiş sözlüğünü geçen ay yayımladı.',
            'C': 'Bu yaz **Ege Denizi** kıyısındaki küçük bir kasabada tatil yaptık.',
            'D': '**Van Gölü** çevresinde arkadaşlarımızla iki gün kamp kurduk.',
            'E': '**Ramazan bayramı** yaklaşırken çarşılar alışveriş yapanlarla doldu.',
        },
        'E',
        "Bayram adlarındaki her sözcük büyük harfle başlar: Ramazan Bayramı. Kurum, göl, deniz adları ve özel ada eklenen 'Hanım' unvanı doğru yazılmıştır.",
    ),
    # düzey 3
    '0046': patch(
        'Aşağıdaki cümlelerin hangisinde nesne eksikliğinden kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Ödevini akşam bitirdi, sabah da öğretmenine teslim etti.',
            'B': 'Arkadaşlarını çok sever ve zor günlerde onlara güvenir.',
            'C': 'Annesine çok bağlıdır, işten çıkınca her gün arar.',
            'D': 'Kitaplarına özen gösterir, onları kirletmemeye çalışır.',
            'E': 'Sabah bahçeyi suladı, sonra çiçekleri budadı.',
        },
        'C',
        "'Annesine' yönelme durumundadır; 'arar' yüklemi belirtili nesne ister: '...her gün onu arar'.",
    ),
    # düzey 2
    '0047': patch(
        'Aşağıdaki cümlelerin hangisinde tırnak işareti yanlış kullanılmıştır?',
        {
            'A': 'Öğretmen ders bitmeden “Yarın sınav var.” diye hatırlattı.',
            'B': 'Bahçe kapısındaki levhada “Girilmez” yazıyordu.',
            'C': 'Annem telefonda “eve erken döneceğini” söyledi.',
            'D': 'Atatürk “Yurtta sulh, cihanda sulh.” sözüyle barışı vurgulamıştır.',
            'E': "Edebiyat dersinde Yahya Kemal'in “Sessiz Gemi” şiirini okuduk.",
        },
        'C',
        "Tırnak işareti başkasından olduğu gibi aktarılan sözler ve eser adları için kullanılır; dolaylı anlatım ('döneceğini söyledi') tırnak içine alınmaz.",
    ),
    # düzey 3
    '0048': patch(
        'Ah ( ) o eski günler ( ) Çocukluğumun geçtiği o köyü hiç unutamıyorum ( ) Annem sık sık şöyle derdi ( ) “Köyünü unutan, kendini unutur.”\n\nBu parçada ayraçlarla ( ) belirtilen yerlere aşağıdaki noktalama işaretlerinden hangileri sırasıyla getirilmelidir?',
        {
            'A': '(,) (...) (?) (:)',
            'B': '(,) (...) (.) (:)',
            'C': '(!) (...) (.) (,)',
            'D': '(,) (!) (,) (:)',
            'E': '(;) (.) (.) (:)',
        },
        'B',
        'Ünlemden sonra virgül, duygunun sözle tamamlanmadığı yerde üç nokta, cümle sonunda nokta, doğrudan aktarılacak sözden önce iki nokta kullanılır.',
    ),
    # düzey 3
    '0049': patch(
        'Aşağıdaki cümlelerin hangisinde dolaylı tümleç eksikliğinden kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Yeni evlerine geçen ay taşındılar ve orayı çok sevdiler.',
            'B': 'Sınava aylarca iyi hazırlandı ve sonunda başarılı oldu.',
            'C': 'Öğretmenin anlattığı konuyu dikkatle dinledi ve anladı.',
            'D': 'Ödevini akşam bitirdi ve sabah öğretmenine verdi.',
            'E': 'Bu ödülü almayı çok istiyor ve yıllardır hazırlanıyordu.',
        },
        'E',
        "'Almayı istiyor' belirtme durumunda tümleç alır; 'hazırlanıyordu' ise yönelme durumunda tümleç ister: '...ve buna yıllardır hazırlanıyordu'.",
    ),
    # düzey 2
    '0050': patch(
        'Aşağıdaki cümlelerin hangisinde soru ekinin yazımı yanlıştır?',
        {
            'A': 'Geldi mi hemen bana haber ver, birlikte çıkarız.',
            'B': 'Güzel mi güzel, bahçeli bir evde oturuyorlardı.',
            'C': 'Annem soruyor, bu akşam yemeğe bize gelecekmisin?',
            'D': 'Sana önerdiğim kitabı sonunda okudun mu?',
            'E': 'Dünkü matematik sınavı sence zor muydu?',
        },
        'C',
        "Soru eki 'mi' kendinden önceki sözcükten ayrı yazılır: gelecek misin. Diğer cümlelerde ek kurala uygun ayrı yazılmıştır.",
    ),
    # düzey 3
    '0051': patch(
        'Aşağıdaki cümlelerin hangisinde çatı uyumsuzluğundan kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Sınav sorunsuz biçimde yapıldı, sonuçlar ertesi gün açıklandı.',
            'B': 'Proje öğrenciler tarafından hazırlandı ve kurula sundu.',
            'C': 'Yeni çevre yolu açıldı ve şehir içindeki trafik rahatladı.',
            'D': 'Uzun mektubu akşam yazdı ve sabah postaya verdi.',
            'E': 'Toplantı geç saatlere kadar yapıldı ve önemli kararlar alındı.',
        },
        'B',
        "Edilgen 'hazırlandı' yüklemiyle aynı özneye bağlanan ikinci yüklem de edilgen olmalıdır: '...ve kurula sunuldu'.",
    ),
    # düzey 3
    '0052': patch(
        'Aşağıdaki cümlelerin hangisinde anlatım bozukluğu vardır?',
        {
            'A': 'Bu kitabı okuduktan sonra yazarın diğer eserlerini de merak ettim.',
            'B': 'Toplantıda alınan kararlar bütün çalışanları ilgilendirdi ve memnun oldu.',
            'C': 'Yeni müdür göreve başlar başlamaz çalışanlarla tanıştı.',
            'D': 'Ödevleri zamanında teslim edenler ek puan alacak.',
            'E': 'Alınan kararlar çalışanları memnun etti.',
        },
        'B',
        "'Memnun oldu' yükleminin öznesi 'kararlar' olamaz; memnun olan çalışanlardır. İkinci yüklemin öznesi eksiktir: '...ilgilendirdi ve çalışanlar memnun oldu'.",
    ),
    # düzey 2
    '0053': patch(
        'Aşağıdaki cümlelerin hangisinde gereksiz sözcük kullanımından kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Sabahki toplantı beklenenden uzun sürdü, iki saati geçti.',
            'B': 'Sınav sonuçları yarın öğleden sonra internetten açıklanacak.',
            'C': 'Gişenin önünde yaklaşık iki saate yakın bekledik.',
            'D': 'Bu konuyu daha önce de birkaç kez konuşmuştuk.',
            'E': 'Kalın romanı bir haftada okuyup bitirdi.',
        },
        'C',
        "'Yaklaşık' ve 'yakın' aynı anlamı karşıladığından biri gereksizdir.",
    ),
    # düzey 2
    '0054': patch(
        'Aşağıdaki cümlelerin hangisinde birleşik sözcüğün yazımı doğrudur?',
        {
            'A': 'Baş öğretmen bizi ders arasında odasına çağırdı.',
            'B': 'Akşamüstü kardeşimle sahildeki kafede buluştuk.',
            'C': 'Bir kaç gün izin alıp memleketine gitti.',
            'D': 'Toplantı boyunca hiç bir şey söylemedi.',
            'E': 'Hanım eli kokusu bütün bahçeyi sarmıştı.',
        },
        'B',
        "'Akşamüstü' bitişik yazılır. 'Birkaç, hiçbir, başöğretmen, hanımeli' de bitişik yazılmalıydı.",
    ),
    # düzey 2
    '0055': patch(
        'Aşağıdaki cümlelerin hangisinin sonuna soru işareti konmalıdır?',
        {
            'A': 'Sabah bulutluydu ama nasıl da güzel bir gün oldu',
            'B': 'Bu saatte kapıyı kimin çaldığını çok merak ediyorum',
            'C': 'Geçen hafta aldığın o kalın kitabı kime ödünç verdin',
            'D': 'Annesi, oğluna eve ne zaman döneceğini sordu',
            'E': 'Toplantının hangi salonda yapılacağını henüz bilmiyorum',
        },
        'C',
        'Doğrudan soru soran cümlenin sonuna soru işareti konur. Diğer cümleler soru sözcüğü içerse de dolaylı soru ya da ünlem cümlesidir.',
    ),
    # düzey 2
    '0056': patch(
        'Aşağıdaki cümlelerin hangisinde düzeltme işaretinin kullanımı yanlıştır?',
        {
            'A': 'Ameliyattan sonra hastanın hâli dün daha iyiydi.',
            'B': 'Miras yüzünden açılan bu dâva yıllardır sürüyor.',
            'C': 'Aradan aylar geçmesine rağmen hâlâ ondan haber bekliyoruz.',
            'D': 'Toplantıdan sonra kâğıtları masanın üstüne bırak.',
            'E': 'Şirket bu yıl ihracattan büyük kâr elde etti.',
        },
        'B',
        "'Dava' sözcüğünde düzeltme işareti kullanılmaz. 'Hâlâ, kâr, kâğıt, hâl' sözcüklerinde ise işaret, anlam ayrımı ya da ince okunuş için kullanılır.",
    ),
    # düzey 3
    '0057': patch(
        'Aşağıdaki cümlelerin hangisinde yüklem eksikliğinden kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Kardeşim hem yetenekliydi hem de derslerine çok çalışırdı.',
            'B': 'Uzun süre hazırlandığı sınavı kazandı ve çok sevindi.',
            'C': 'Yeni gelen öğrenci hem yetenekli hem de derslerine çok çalıştı.',
            'D': 'Düğünde hem şarkı söyledi hem de saatlerce dans etti.',
            'E': 'Üniversitede hem okuyor hem de yarı zamanlı çalışıyordu.',
        },
        'C',
        "'Yetenekli' sözcüğünün yüklemi yoktur; 'çalıştı' yüklemi ona uymaz: 'hem yetenekliydi hem çok çalıştı' olmalıdır.",
    ),
    # düzey 3
    '0058': patch(
        'Aşağıdaki cümlelerin hangisinde bir sözcüğün yanlış anlamda kullanılmasından kaynaklanan anlatım bozukluğu vardır?',
        {
            'A': 'Sabahtan beri yağan yağmur sonunda öğleye doğru dindi.',
            'B': 'Durakta saatlerce bekledik ama otobüs nihayet gelmedi.',
            'C': 'Uzun bir bekleyişin ardından otobüs nihayet durağa geldi.',
            'D': 'Bütün gün tarlada çalıştı, akşam yorgun düştü.',
            'E': 'Toplantı beklenenden kısa sürdü ve herkes erken çıktı.',
        },
        'B',
        "'Nihayet' (sonunda) beklenen bir şeyin gerçekleştiğini anlatır; olumsuz yüklemle ('gelmedi') kullanılamaz. Burada 'bir türlü' gibi bir söz gerekirdi.",
    ),
    # düzey 2
    '0059': patch(
        'Aşağıdaki cümlelerin hangisinde yabancı kökenli bir sözcüğün yazımı yanlıştır?',
        {
            'A': 'Evdeki eski **televizyon** sonunda tamamen bozuldu.',
            'B': "İstanbul'dan gelen **tren** kar yüzünden bir saat gecikti.",
            'C': 'Belediye, gençler için yeni bir spor **proğramı** açıkladı.',
            'D': 'Sabah saatlerinde **otobüs** yine tıklım tıklımdı.',
            'E': 'Yük taşıyan eski **kamyon** dik yokuşta yolda kaldı.',
        },
        'C',
        "Sözcüğün doğru yazımı 'program'dır. Diğer sözcükler doğru yazılmıştır.",
    ),
    # düzey 2
    '0060': patch(
        'Aşağıdaki cümlelerin hangisinde kesme işareti yanlış kullanılmıştır?',
        {
            'A': "Edebiyat dersinde Yunus Emre'nin şiirlerini okuduk.",
            'B': "Türk Dil Kurumu'nun yeni sözlüğü geçen hafta çıktı.",
            'C': "Oturduğumuz ev 1990'lı yıllarda yapılmış.",
            'D': "TBMM'nin yeni yasama yılı ekim ayında başladı.",
            'E': "Uzun yolculuğun ardından Ankara'ya akşam saatlerinde vardık.",
        },
        'B',
        'Kurum, kuruluş ve kuruluş adlarına gelen ekler kesmeyle ayrılmaz: Türk Dil Kurumunun. Kısaltmalara, sayılara, kişi ve yer adlarına gelen ekler ise kesmeyle ayrılır.',
    ),
}

PATCHES = {ONEK + k: v for k, v in _PATCHES.items()}


def apply_or_check(path, write):
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    by_id = {q["id"]: q for q in questions}
    fark = []
    for qid, alanlar in PATCHES.items():
        q = by_id.get(qid)
        if q is None:
            raise SystemExit(f"Soru bulunamadi: {path}::{qid}")
        for alan, beklenen in alanlar.items():
            if q.get(alan) != beklenen:
                fark.append(f"{path}::{qid}.{alan}")
                if write:
                    q[alan] = beklenen
        if write:
            if len(set(q["options"].values())) != 5:
                raise SystemExit(f"Secenek cakismasi: {path}::{qid}")
            if q["answer"] not in q["options"]:
                raise SystemExit(f"Cevap secenekte yok: {path}::{qid}")
    if write:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return fark


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--write", action="store_true")
    args = ap.parse_args()
    fark = []
    for path in (ROOT / RELATIVE_PATH, APP_ROOT / RELATIVE_PATH):
        fark.extend(apply_or_check(path, args.write))
    if args.check and fark:
        print("Eslesmeyen alanlar:")
        for f in fark[:20]:
            print(f"- {f}")
        return 1
    print(f"1 paket / {len(PATCHES)} soru ('Türkçe — Yazım, Noktalama ve Anlatım Bozukluğu' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
