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
            'A': "Saat 9.30'da buluşalım.",
            'B': 'Kitabın III. bölümünü okudum.',
            'C': "Bu kitap 1998'de yayımlandı.",
            'D': 'Kardeşim yarışmada 3. oldu.',
            'E': "25'den fazla kişi geldi.",
        },
        'E',
        "Rakamla yazılan sayılara gelen ek, sayının okunuşuna göre yazılır: yirmi beşten → 25'ten. Diğer cümlelerde sıra sayısı, yıl ve saat yazımları doğrudur.",
    ),
    # düzey 2
    '0002': patch(
        'Aşağıdaki cümlelerin hangisinde anlamca çelişen sözcüklerin bir arada kullanılmasından kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Kesinlikle yarın gelebilirim.',
            'B': 'Yarın büyük olasılıkla gelirim.',
            'C': 'Toplantıya kesinlikle katılacağım.',
            'D': 'Yarın gelemeyebilirim.',
            'E': 'Mutlaka yarın gelirim.',
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
            'A': 'Bu ürünlerde yüzde elli indirim var.',
            'B': 'Kırk yıllık dostuyla karşılaştı.',
            'C': 'Sınıfta otuz iki öğrenci var.',
            'D': 'Bin dokuz yüz yirmi üç yılında ilan edildi.',
            'E': 'Toplantıya yirmibeş kişi katıldı.',
        },
        'E',
        'Birden çok sözcükten oluşan sayı adları ayrı yazılır: yirmi beş.',
    ),
    # düzey 2
    '0005': patch(
        'Aşağıdaki cümlelerin hangisinde özne-yüklem uyumsuzluğundan kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Sen ve ben başaracaksınız.',
            'B': 'Ali ile Ayşe dün sinemaya gitti.',
            'C': 'Ağaçlar ilkbaharda çiçek açar.',
            'D': 'Herkes görüşünü açıkça söyledi.',
            'E': 'Öğrenciler sınav sonuçlarını bekliyor.',
        },
        'A',
        "'Sen ve ben' öznesi birinci çoğul kişiyi (biz) karşılar; yüklem 'başaracağız' olmalıdır.",
    ),
    # düzey 2
    '0006': patch(
        'Aşağıdaki cümlelerin hangisinde nokta yanlış kullanılmıştır?',
        {
            'A': "Toplantı 15. Mayıs'ta yapılacak.",
            'B': "II. Dünya Savaşı 1945'te sona erdi.",
            'C': 'Kardeşim yarışmada 3. oldu.',
            'D': 'Prof. Dr. Ali Kaya konuşma yaptı.',
            'E': 'Kitabın 25. sayfasını açın.',
        },
        'A',
        "Nokta, sıra bildirmek için sayılardan sonra konur; tarih bildiren gün sayılarından sonra konmaz: 15 Mayıs'ta. Diğerlerinde nokta kısaltma ve sıra sayısı için doğru kullanılmıştır.",
    ),
    # düzey 2
    '0007': patch(
        "Aşağıdaki cümlelerin hangisinde '-ken' ekinin yazımı yanlıştır?",
        {
            'A': 'Yemek yerken konuşmazdı.',
            'B': 'Eve dönerken ekmek aldı.',
            'C': 'Çocukken bu parkta oynardık.',
            'D': 'Okula gider ken onu gördü.',
            'E': 'Hava güzelken yürüyüşe çıkalım.',
        },
        'D',
        "'-ken' ektir ve bitişik yazılır: giderken.",
    ),
    # düzey 3
    '0008': patch(
        'Aşağıdaki cümlelerin hangisinde üç nokta, sıralanan örneklerin sürdürülebileceğini göstermek için kullanılmıştır?',
        {
            'A': 'Seni o kadar özledim ki...',
            'B': 'Ali... Ali... Neredesin?',
            'C': 'Bir gün sana... Neyse, boş ver.',
            'D': '“...Ne mutlu Türküm diyene!” sözünü hep hatırlarım.',
            'E': 'Pazardan domates, biber, patlıcan... aldık.',
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
            'A': 'Bu kitabı çok seviyor ve sık sık bahsediyor.',
            'B': 'Projeyi inceledi ve onayladı.',
            'C': 'Ondan hem korkuyor hem çekiniyordu.',
            'D': 'Bu kitabı çok seviyor ve sık sık okuyor.',
            'E': 'Kardeşine güveniyor ve onu çok seviyor.',
        },
        'A',
        "'Sevmek' belirtme (-i), 'bahsetmek' ayrılma (-den) durumunda tümleç ister; ortak 'bu kitabı' tümleci ikinci yükleme uymaz: '...ve ondan sık sık bahsediyor'.",
    ),
    # düzey 2
    '0011': patch(
        'Aşağıdaki cümlelerin hangisinde tarihin yazımı yanlıştır?',
        {
            'A': "Bu bina 1950'li yıllarda yapıldı.",
            'B': "23 Nisan 1920'de TBMM açıldı.",
            'C': 'Toplantı 5 Mayıs Pazartesi günü yapılacak.',
            'D': 'Okullar eylül ayında açılır.',
            'E': "29 ekim 1923'te Cumhuriyet ilan edildi.",
        },
        'E',
        "Belirli bir tarih bildiren ay adları büyük harfle başlar: 29 Ekim 1923. Belirli tarih bildirmeyen ay adı ('eylül ayında') küçük harfle yazılır.",
    ),
    # düzey 2
    '0012': patch(
        'Aşağıdaki cümlelerin hangisinde yer adının yazımı yanlıştır?',
        {
            'A': "Ankara Kalesi'ni ziyaret ettik.",
            'B': "Marmara Denizi'nde yüzdük.",
            'C': "Bu yaz Kapadokya'yı gezdik.",
            'D': 'Kışın Uludağa kayak yapmaya gittik.',
            'E': "Doğu Karadeniz'in yaylaları çok güzeldir.",
        },
        'D',
        "Özel adlara gelen çekim ekleri kesmeyle ayrılır: Uludağ'a. Diğer yer adları kurala uygun yazılmıştır.",
    ),
    # düzey 2
    '0013': patch(
        'Aşağıdaki cümlelerin hangisinde ses düşmesiyle ilgili bir yazım yanlışı vardır?',
        {
            'A': 'Oğlu bu yıl askere gitti.',
            'B': 'Alnına bir öpücük kondurdu.',
            'C': 'Burnunu mendille sildi.',
            'D': 'Herkesin ağızı kurumuştu.',
            'E': 'Göğsünde bir ağrı vardı.',
        },
        'D',
        "'Ağız' sözcüğü ünlüyle başlayan ek alınca ikinci hecedeki ünlü düşer: ağzı. 'Oğlu, burnu, göğsü, alnı' doğru yazılmıştır.",
    ),
    # düzey 2
    '0014': patch(
        'Aşağıdaki cümlelerin hangisinde büyük harflerin kullanımıyla ilgili bir yazım yanlışı vardır?',
        {
            'A': "Atatürk Caddesi'ndeki eski binalar yıkılıyor.",
            'B': "Romanın adı Kuyucaklı Yusuf'tu.",
            'C': "Cumhuriyet Bayramı'nda okulda tören yapıldı.",
            'D': 'Toplantıya Prof. Dr. Ayşe Yılmaz da katıldı.',
            'E': 'Karadeniz bölgesini gezdik.',
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
            'A': 'Mutlaka bu akşam uğrayabilirim.',
            'B': 'Bu konuyu daha önce hiç düşünmemiştim.',
            'C': 'Herkes sınav sonuçlarını merakla bekliyorlardı.',
            'D': 'Fiyatlar her geçen gün biraz daha pahalanıyor.',
            'E': 'Bu yaz tatilde hem dinlendik hem de çok eğlenceliydi.',
        },
        'B',
        "Diğer cümlelerde çelişen anlam ('mutlaka - uğrayabilirim'), özne-yüklem uyumsuzluğu ('herkes - bekliyorlardı'), yanlış sözcük ('fiyat pahalanmaz, yükselir') ve yüklem uyumsuzluğu vardır.",
    ),
    # düzey 2
    '0017': patch(
        'Aşağıdaki cümlelerin hangisinde bağlacın yanlış kullanılmasından kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Çok çalıştı ama sınavı kazandı.',
            'B': 'Çok çalıştığı için sınavı kazandı.',
            'C': 'Hava soğuktu, yine de denize girdik.',
            'D': 'Yorgundu; bu yüzden erken yattı.',
            'E': 'Yağmur yağıyordu ama şemsiyesini almamıştı.',
        },
        'A',
        "'Ama' karşıtlık bildirir; çok çalışmak ile sınavı kazanmak arasında karşıtlık değil neden-sonuç ilişkisi vardır.",
    ),
    # düzey 2
    '0018': patch(
        'Aşağıdaki cümlelerin hangisinde noktalama yanlışı yoktur?',
        {
            'A': 'Kitap, defter, ve kalem aldım.',
            'B': 'Yarın görüşürüz, dedi, ve gitti.',
            'C': 'Eyvah, geç kaldık!',
            'D': "Toplantı saat 14.00'te başladı?",
            'E': 'Nereye gidiyorsun.',
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
            'A': 'Sınava geç kaldığı için içeri alınmadı.',
            'B': 'Yağmur başlayınca maç ertelendi.',
            'C': 'Tembel olduğu için ödül aldı.',
            'D': 'Çok yorulduğu için erkenden yattı.',
            'E': 'Bilet kalmadığı için konsere gidemedik.',
        },
        'C',
        'Tembellik ödül almanın nedeni olamaz; neden-sonuç ilişkisi mantıksız kurulmuştur.',
    ),
    # düzey 3
    '0021': patch(
        'Aşağıdaki cümlelerin hangisinde birleşik fiilin yazımı yanlıştır?',
        {
            'A': 'Onu asla af etmeyeceğim.',
            'B': 'Ödevini zamanında teslim etti.',
            'C': 'Yaşlı adama yolda yardım ettik.',
            'D': 'Toplantıya geç kaldığı için özür diledi.',
            'E': 'Kendini çok yalnız hissetti.',
        },
        'A',
        "Birleşik fiilde ses düşmesi ya da türemesi olursa birleşik fiil bitişik yazılır: af + etmek → affetmek. 'Teslim etmek, yardım etmek' ses olayı olmadığı için ayrı; 'hissetmek' (his+etmek) bitişik yazılır.",
    ),
    # düzey 3
    '0022': patch(
        'Aşağıdaki cümlelerin hangisinde virgül, öznenin belirginleşmesini sağlamak için kullanılmıştır?',
        {
            'A': 'Genç, kadına yardım etti.',
            'B': 'Evet, bu işi ben yapacağım.',
            'C': 'Ali, buraya gelir misin?',
            'D': 'Kitap, defter ve kalem aldı.',
            'E': 'Kapıyı açtı, içeri girdi.',
        },
        'A',
        "Virgül konmasaydı 'genç kadın' bir sıfat tamlaması olarak anlaşılırdı. Virgül, 'genç'in özne olduğunu belirginleştirir. Diğerlerinde virgül cevap, hitap, eş görevli sözcükler ve sıralı cümleler için kullanılmıştır.",
    ),
    # düzey 2
    '0023': patch(
        'Aşağıdaki cümlelerin hangisinde ünsüz yumuşamasıyla ilgili bir yazım yanlışı vardır?',
        {
            'A': 'Sokağın sonunda bir park vardı.',
            'B': 'Kitabı masanın üstünde unutmuş.',
            'C': 'Dolabın kapağı kırılmış.',
            'D': 'Ağaçın gölgesinde dinlendik.',
            'E': 'Renginden hiç hoşlanmadı.',
        },
        'D',
        "'Ağaç' sözcüğü ünlüyle başlayan ek alınca sondaki 'ç' yumuşar: ağacın. Diğer sözcüklerde yumuşama doğru yansıtılmıştır.",
    ),
    # düzey 2
    '0024': patch(
        'Aşağıdaki cümlelerin hangisinde yazım yanlışı yoktur?',
        {
            'A': 'Herkes bu kararı doğru buldu.',
            'B': 'Herkez bu karara itiraz etti.',
            'C': 'Bu konuda hiç bir fikrim yok.',
            'D': 'Yarınki maçı izleyecekmisin?',
            'E': 'Toplantı saat üçde başlayacak.',
        },
        'A',
        "'Herkez' yerine 'herkes', 'hiç bir' yerine 'hiçbir', 'üçde' yerine 'üçte', 'izleyecekmisin' yerine 'izleyecek misin' yazılmalıdır.",
    ),
    # düzey 2
    '0025': patch(
        'Aşağıdaki cümlelerin hangisinin sonuna ünlem işareti konmalıdır?',
        {
            'A': 'Toplantı saat üçte başlayacak',
            'B': 'Yarın sabah erkenden yola çıkacağız',
            'C': 'Bu soruyu kim çözdü',
            'D': 'Eyvah, otobüsü kaçırdık',
            'E': 'Kitabı masaya bıraktım',
        },
        'D',
        "'Eyvah' ünlemiyle başlayan, şaşkınlık ve üzüntü bildiren cümlenin sonuna ünlem işareti konur.",
    ),
    # düzey 2
    '0026': patch(
        'Aşağıdaki cümlelerin hangisinde unvanın yazımı yanlıştır?',
        {
            'A': "Bu konuyu Ahmet bey'e danışalım.",
            'B': "Fatih Sultan Mehmet İstanbul'u fethetti.",
            'C': 'Ayşe Hanım toplantıya katılmadı.',
            'D': 'Dr. Selim Kaya hastayı muayene etti.',
            'E': 'Prof. Dr. Elif Arslan konuşma yaptı.',
        },
        'A',
        "Özel adlardan sonra gelen saygı sözleri büyük harfle başlar: Ahmet Bey'e. Diğer unvanlar kurala uygun yazılmıştır.",
    ),
    # düzey 3
    '0027': patch(
        'Aşağıdaki cümlelerin hangisinde noktalı virgül yanlış kullanılmıştır?',
        {
            'A': 'Yorgundu; yine de toplantıya katıldı.',
            'B': 'Ali, Ayşe ve Can birinci sınıfta; Elif, Deniz ve Selin ikinci sınıftaydı.',
            'C': 'Bizim takım dinçti; rakip takımın oyuncuları ise yorgundu.',
            'D': 'Çok çalıştı; ancak istediği sonucu alamadı.',
            'E': 'Bahçede güller; laleler ve papatyalar açmıştı.',
        },
        'E',
        "Eş görevli sözcükleri ayırmak için noktalı virgül değil virgül kullanılır: güller, laleler ve papatyalar. Diğer cümlelerde noktalı virgül; 'ancak, yine de' öncesinde, virgüllerle ayrılmış takımlar ve karşıt yargılar arasında doğru kullanılmıştır.",
    ),
    # düzey 2
    '0028': patch(
        'Aşağıdaki cümlelerin hangisinde kalın yazılmış sözcüğün yazımı yanlıştır?',
        {
            'A': 'Soruların **hiçbiri** zor değildi.',
            'B': 'Bunu **birçok** kez söyledim.',
            'C': 'Sana **birşey** söylemek istiyorum.',
            'D': '**Herhangi** bir sorun olursa ara.',
            'E': 'Öğrencilerin **her biri** ödül aldı.',
        },
        'C',
        "'Bir şey' ayrı yazılır. 'Birçok, herhangi, hiçbiri' bitişik; 'her biri' ayrı yazılır.",
    ),
    # düzey 2
    '0029': patch(
        "Aşağıdaki cümlelerin hangisinde 'de'nin yazımı yanlıştır?",
        {
            'A': 'Kitapları da defterleri de çantasına koydu.',
            'B': 'Toplantıda önemli kararlar alındı.',
            'C': 'Akşam sen de bize gel.',
            'D': 'Sende kalan kitabı getirir misin?',
            'E': 'Bu konuyu bende yeni öğrendim.',
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
            'A': 'Öyleki kimse sesini çıkaramadı.',
            'B': 'Yarınki toplantıya katılamayacağım.',
            'C': 'Sanki her şey yolundaymış gibi davrandı.',
            'D': 'Belki akşam size uğrarız.',
            'E': 'Duydum ki yeni bir işe başlamışsın.',
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
            'A': 'Herkes kendi payını aldı.',
            'B': 'Bu işi birkaç günde bitirdi.',
            'C': 'Her şeyi baştan anlattı.',
            'D': 'Bir çok kitap okudum.',
            'E': 'Hiçbir sorunla karşılaşmadık.',
        },
        'D',
        "'Birçok' bitişik yazılır. 'Hiçbir, birkaç, herkes' bitişik; 'her şey' ayrı yazılır.",
    ),
    # düzey 2
    '0034': patch(
        'Aşağıdaki cümlelerin hangisinde zaman uyumsuzluğundan kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Her sabah yürüyüş yapar, sonra kahvaltı eder.',
            'B': 'Dün akşam eve geç döndüm.',
            'C': 'Yarın erkenden kalkıp yola çıkacağız.',
            'D': 'Geçen yıl bu okula başladım ve çok mutlu olacağım.',
            'E': 'Haftaya sınav olacağımız için şimdiden çalışıyoruz.',
        },
        'D',
        "Geçmişte gerçekleşen bir olayın sonucu gelecek zamanla verilmiştir; 'çok mutlu oldum' olmalıdır.",
    ),
    # düzey 3
    '0035': patch(
        'Aşağıdaki cümlelerin hangisinde kesme işareti doğru kullanılmıştır?',
        {
            'A': "Annem'e doğum gününde çiçek aldım.",
            'B': "Bu romanı 2015'te okumuştum.",
            'C': "Millî Eğitim Bakanlığı'na dilekçe verdi.",
            'D': "Türkçe'yi çok iyi konuşuyor.",
            'E': "Bu yıl Ekim'de tatile çıkacağız.",
        },
        'B',
        "Rakamla yazılan sayılara gelen ekler kesmeyle ayrılır: 2015'te. Dil adlarına (Türkçeyi), kurum adlarına (Bakanlığına), cins isimlere (anneme) ve belirli bir tarih bildirmeyen ay adlarına (ekimde) gelen ekler kesmeyle ayrılmaz.",
    ),
    # düzey 2
    '0036': patch(
        'Aşağıdaki cümlelerin hangisinde bir yazım yanlışı vardır?',
        {
            'A': 'Yanlız yaşamaktan hiç hoşlanmazdı.',
            'B': 'Birkaç gün içinde döneceğim.',
            'C': 'Herkes bu konuda aynı fikirdeydi.',
            'D': 'Yanlış anlaşılmak istemiyorum.',
            'E': 'Hiçbir şey eskisi gibi değildi.',
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
            'A': 'Başarının tek bir sırrı vardır: düzenli çalışmak.',
            'B': 'Yazarın son sözü şuydu: Okumayan toplum ilerleyemez.',
            'C': 'Sepette şunlar vardı: elma, armut, ayva.',
            'D': 'Annem seslendi: “Yemek hazır!”',
            'E': 'Toplantıya: müdür, iki uzman ve ben katıldık.',
        },
        'E',
        "İki nokta, açıklama ya da örnek verilecek sözden sonra, aktarılan sözden önce kullanılır; özne ile yüklem arasına konmaz. 'Toplantıya: müdür ...' kullanımı cümlenin ögelerini böler.",
    ),
    # düzey 2
    '0044': patch(
        'Aşağıdaki cümlelerin hangisinde virgülün kullanımı yanlıştır?',
        {
            'A': 'Elma, armut ve ayva aldık.',
            'B': 'Evet, yarın size uğrayacağım.',
            'C': 'Kardeşim, ve ben aynı okula gidiyoruz.',
            'D': 'Sevgili arkadaşlar, toplantımız başlıyor.',
            'E': 'Yaşlı, yorgun adam kapıda bekliyordu.',
        },
        'C',
        "'Ve' bağlacından önce virgül konmaz. Diğer cümlelerde virgül cevap sözünden sonra, eş görevli sözcükler arasında ve hitaptan sonra doğru kullanılmıştır.",
    ),
    # düzey 2
    '0045': patch(
        'Aşağıdaki cümlelerin hangisinde kalın yazılmış sözün yazımında büyük harflerle ilgili bir yanlışlık yapılmıştır?',
        {
            'A': '**Ayşe Hanım** bugün işe gelmedi.',
            'B': '**Türk Dil Kurumu** yeni sözlüğünü yayımladı.',
            'C': 'Bu yaz **Ege Denizi** kıyısında tatil yaptık.',
            'D': '**Van Gölü** çevresinde kamp kurduk.',
            'E': '**Ramazan bayramı** yaklaşıyor.',
        },
        'E',
        "Bayram adlarındaki her sözcük büyük harfle başlar: Ramazan Bayramı. Kurum, göl, deniz adları ve özel ada eklenen 'Hanım' unvanı doğru yazılmıştır.",
    ),
    # düzey 3
    '0046': patch(
        'Aşağıdaki cümlelerin hangisinde nesne eksikliğinden kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Ödevini bitirdi, öğretmenine teslim etti.',
            'B': 'Arkadaşlarını sever ve onlara güvenir.',
            'C': 'Annesine çok bağlıdır, her gün arar.',
            'D': 'Kitaplarına özen gösterir, onları hiç kirletmez.',
            'E': 'Bahçeyi suladı, çiçekleri budadı.',
        },
        'C',
        "'Annesine' yönelme durumundadır; 'arar' yüklemi belirtili nesne ister: '...her gün onu arar'.",
    ),
    # düzey 2
    '0047': patch(
        'Aşağıdaki cümlelerin hangisinde tırnak işareti yanlış kullanılmıştır?',
        {
            'A': 'Öğretmen “Yarın sınav var.” dedi.',
            'B': 'Kapıdaki levhada “Girilmez” yazıyordu.',
            'C': 'Annem “eve erken döneceğini” söyledi.',
            'D': 'Atatürk “Yurtta sulh, cihanda sulh.” demiştir.',
            'E': "Yahya Kemal'in “Sessiz Gemi” şiirini okuduk.",
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
            'A': 'Yeni evlerine taşındılar ve orayı çok sevdiler.',
            'B': 'Sınava iyi hazırlandı ve başarılı oldu.',
            'C': 'Konuyu dikkatle dinledi ve anladı.',
            'D': 'Ödevini bitirdi ve öğretmenine verdi.',
            'E': 'Bu ödülü almayı çok istiyor ve yıllardır hazırlanıyordu.',
        },
        'E',
        "'Almayı istiyor' belirtme durumunda tümleç alır; 'hazırlanıyordu' ise yönelme durumunda tümleç ister: '...ve buna yıllardır hazırlanıyordu'.",
    ),
    # düzey 2
    '0050': patch(
        'Aşağıdaki cümlelerin hangisinde soru ekinin yazımı yanlıştır?',
        {
            'A': 'Geldi mi hemen haber ver.',
            'B': 'Güzel mi güzel bir evdi.',
            'C': 'Bu akşam bize gelecekmisin?',
            'D': 'Kitabı okudun mu?',
            'E': 'Sınav zor muydu?',
        },
        'C',
        "Soru eki 'mi' kendinden önceki sözcükten ayrı yazılır: gelecek misin. Diğer cümlelerde ek kurala uygun ayrı yazılmıştır.",
    ),
    # düzey 3
    '0051': patch(
        'Aşağıdaki cümlelerin hangisinde çatı uyumsuzluğundan kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Sınav yapıldı, sonuçlar açıklandı.',
            'B': 'Proje hazırlandı ve kurula sundu.',
            'C': 'Yeni yol açıldı ve trafik rahatladı.',
            'D': 'Mektubu yazdı ve postaya verdi.',
            'E': 'Toplantı yapıldı ve kararlar alındı.',
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
            'A': 'Toplantı iki saatten fazla sürdü.',
            'B': 'Sınav sonuçları yarın açıklanacak.',
            'C': 'Yaklaşık iki saate yakın bekledik.',
            'D': 'Bu konuyu daha önce de konuşmuştuk.',
            'E': 'Kitabı bir haftada okuyup bitirdi.',
        },
        'C',
        "'Yaklaşık' ve 'yakın' aynı anlamı karşıladığından biri gereksizdir.",
    ),
    # düzey 2
    '0054': patch(
        'Aşağıdaki cümlelerin hangisinde birleşik sözcüğün yazımı doğrudur?',
        {
            'A': 'Baş öğretmen bizi çağırdı.',
            'B': 'Akşamüstü kardeşimle buluştuk.',
            'C': 'Bir kaç gün izin aldı.',
            'D': 'Hiç bir şey söylemedi.',
            'E': 'Hanım eli kokusu her yeri sardı.',
        },
        'B',
        "'Akşamüstü' bitişik yazılır. 'Birkaç, hiçbir, başöğretmen, hanımeli' de bitişik yazılmalıydı.",
    ),
    # düzey 2
    '0055': patch(
        'Aşağıdaki cümlelerin hangisinin sonuna soru işareti konmalıdır?',
        {
            'A': 'Nasıl da güzel bir gün',
            'B': 'Kimin geldiğini merak ediyorum',
            'C': 'Bu kitabı kime ödünç verdin',
            'D': 'Ne zaman döneceğini sordu',
            'E': 'Toplantının nerede yapılacağını bilmiyorum',
        },
        'C',
        'Doğrudan soru soran cümlenin sonuna soru işareti konur. Diğer cümleler soru sözcüğü içerse de dolaylı soru ya da ünlem cümlesidir.',
    ),
    # düzey 2
    '0056': patch(
        'Aşağıdaki cümlelerin hangisinde düzeltme işaretinin kullanımı yanlıştır?',
        {
            'A': 'Hastanın hâli dün daha iyiydi.',
            'B': 'Bu dâva yıllardır sürüyor.',
            'C': 'Hâlâ ondan haber bekliyoruz.',
            'D': 'Kâğıtları masanın üstüne bırak.',
            'E': 'Şirket bu yıl büyük kâr elde etti.',
        },
        'B',
        "'Dava' sözcüğünde düzeltme işareti kullanılmaz. 'Hâlâ, kâr, kâğıt, hâl' sözcüklerinde ise işaret, anlam ayrımı ya da ince okunuş için kullanılır.",
    ),
    # düzey 3
    '0057': patch(
        'Aşağıdaki cümlelerin hangisinde yüklem eksikliğinden kaynaklanan bir anlatım bozukluğu vardır?',
        {
            'A': 'Hem yetenekliydi hem de çok çalışırdı.',
            'B': 'Sınavı kazandı ve çok sevindi.',
            'C': 'Hem yetenekli hem çok çalıştı.',
            'D': 'Hem şarkı söyledi hem dans etti.',
            'E': 'Hem okuyor hem çalışıyordu.',
        },
        'C',
        "'Yetenekli' sözcüğünün yüklemi yoktur; 'çalıştı' yüklemi ona uymaz: 'hem yetenekliydi hem çok çalıştı' olmalıdır.",
    ),
    # düzey 3
    '0058': patch(
        'Aşağıdaki cümlelerin hangisinde bir sözcüğün yanlış anlamda kullanılmasından kaynaklanan anlatım bozukluğu vardır?',
        {
            'A': 'Yağmur sonunda dindi.',
            'B': 'Saatlerce bekledik ama otobüs nihayet gelmedi.',
            'C': 'Uzun bir bekleyişin ardından otobüs nihayet geldi.',
            'D': 'Bütün gün çalıştı, akşam yorgun düştü.',
            'E': 'Toplantı beklenenden kısa sürdü.',
        },
        'B',
        "'Nihayet' (sonunda) beklenen bir şeyin gerçekleştiğini anlatır; olumsuz yüklemle ('gelmedi') kullanılamaz. Burada 'bir türlü' gibi bir söz gerekirdi.",
    ),
    # düzey 2
    '0059': patch(
        'Aşağıdaki cümlelerin hangisinde yabancı kökenli bir sözcüğün yazımı yanlıştır?',
        {
            'A': 'Eski **televizyon** sonunda bozuldu.',
            'B': '**Tren** bir saat gecikti.',
            'C': 'Yeni bir **proğram** açıklandı.',
            'D': '**Otobüs** sabah tıklım tıklımdı.',
            'E': '**Kamyon** yokuşta yolda kaldı.',
        },
        'C',
        "Sözcüğün doğru yazımı 'program'dır. Diğer sözcükler doğru yazılmıştır.",
    ),
    # düzey 2
    '0060': patch(
        'Aşağıdaki cümlelerin hangisinde kesme işareti yanlış kullanılmıştır?',
        {
            'A': "Yunus Emre'nin şiirlerini okuduk.",
            'B': "Türk Dil Kurumu'nun sözlüğü çıktı.",
            'C': "Bu ev 1990'lı yıllarda yapılmış.",
            'D': "TBMM'nin yeni yasama yılı başladı.",
            'E': "Ankara'ya akşam saatlerinde vardık.",
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
