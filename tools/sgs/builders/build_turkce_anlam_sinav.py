#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Türkçe — Sözcükte ve Cümlede Anlam — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Önceki onarımdan (build_turkce_anlam_onarim.py) 45 sağlam soru aynen korundu; 15 soru gerçek SGS 1-7 tiplerine göre değiştirildi: deyim ve atasözünün bağlama uygunluğu (olumsuz), yakın anlamlı ikileme, olasılık/kesinlik, kaç farklı anlam, gerekçeli yargı, dolaylama, ad aktarması, sözlük anlamı verilen sözcük, neden-sonuç/amaç ayrımı, sitem ve varsayım yokluğu, öznel yargı yokluğu, parçada mecaz sözcük çifti. Zıt anlamlı/soyut sözcük gibi düşük düzeyli ve belirsiz eş sesli sorusu çıkarıldı.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: SGS Türkçe 2021-2026 kitapçıkları — biçim kalibrasyonu
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/turkce/sozcukte_cumlede_anlam.json"
STYLE_REF = 'SGS Türkçe (gerçek sınav 1-7 profili)'
ONEK = "turkce-anlam-gen-"


def patch(stem, options, answer, solution, ref='Türkçe - sözcükte ve cümlede anlam'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        '"Bu ustanın yaptığı türküler, dinleyenin yüreğine **işliyor**." cümlesinde altı çizili sözcüğün kattığı anlam aşağıdakilerden hangisidir?',
        {
            'A': 'Sıkça yinelenip durmak',
            'B': 'İnsanı derinden etkilemek',
            'C': 'Bir yüzeye oyularak çizilmek',
            'D': 'Ustalıkla süslenerek bezenmek',
            'E': 'Yavaş yavaş ilerlemek',
        },
        'B',
        '"İşlemek" sözcüğü burada gerçek anlamıyla (bir yüzeyi oymak, nakış yapmak) değil, mecaz anlamıyla kullanılmıştır: türkünün insanı içten, derinden etkilemesi. Bu yüzden doğru karşılık "insanı derinden etkilemek"tir; diğer seçenekler sözcüğün gerçek anlamına ya da ilgisiz anlamlara yöneliktir.',
    ),
    # düzey 2
    '0002': patch(
        'Aşağıdaki cümlelerin hangisinde altı çizili sözcük terim anlamıyla kullanılmıştır?',
        {
            'A': 'Geometri dersinde öğretmen, bir üçgenin iç **açıları** toplamının 180 derece olduğunu gösterdi.',
            'B': 'Sınav sonuçlarını öğrenen çocuğun **yüzü**, kapıdan girer girmez sevinçle aydınlandı.',
            'C': 'Gece yarısına kadar ders çalışınca yorgunluktan **gözleri** kapanmaya başlamıştı.',
            'D': 'Annemin bahçeye diktiği **güller**, bu yıl beklenenden çok daha erken açmıştı.',
            'E': 'Bayram tatilinde ailecek sabah erkenden **yola** çıkıp dedemlerin köyüne gittik.',
        },
        'A',
        'Terim, bir bilim ya da sanat dalına özgü anlamdır. "Açı", geometriye özgü bir kavram olarak kullanıldığından terim anlamı taşır. Diğer seçeneklerdeki sözcükler günlük, gerçek anlamlarıyla geçmiştir.',
    ),
    # düzey 3
    '0003': patch(
        '"Onun **soğuk** tavırları herkesi rahatsız ediyordu." cümlesindeki "soğuk" sözcüğüyle aşağıdakilerden hangisinde "soğuk" aynı anlamda kullanılmıştır?',
        {
            'A': 'Bu kış o kadar **soğuk** günler yaşadık ki göl kıyısından ortasına kadar dondu.',
            'B': 'Yıllar sonra karşılaştığımız eski komşumuz, bize nedense oldukça **soğuk** davrandı.',
            'C': 'Uzun koşunun ardından buzdolabındaki **soğuk** ayranı bir dikişte içti.',
            'D': 'Kuzeyden esen **soğuk** rüzgâr yüzünden o gün çocukları dışarı çıkarmadık.',
            'E': 'Sabahları uykusunu açmak için yüzünü **soğuk** suyla yıkamayı alışkanlık edinmişti.',
        },
        'B',
        'Örnek cümlede "soğuk", sevgisiz-ilgisiz, mesafeli tutum anlamıyla (mecaz) kullanılmıştır. Aynı anlam eski komşunun "soğuk davrandığı" cümlede vardır. Diğerlerinde sözcük ısı azlığı (gerçek anlam) bildirir.',
    ),
    # düzey 2
    '0004': patch(
        '"Damlaya damlaya göl olur." atasözüyle aşağıdakilerden hangisi anlamca aynı doğrultudadır?',
        {
            'A': 'Bir elin nesi var, iki elin sesi var.',
            'B': 'Sakla samanı, gelir zamanı.',
            'C': 'Küçük birikimler zamanla büyür.',
            'D': 'Bugünün işini yarına bırakma.',
            'E': 'Ateş düştüğü yeri yakar.',
        },
        'C',
        '"Damlaya damlaya göl olur", küçük birikimlerin zamanla büyük bir bütün oluşturduğunu anlatır. Birikimin çoğalmasını vurgulayan seçenek anlamca aynı doğrultudadır; diğerleri farklı iletiler taşır.',
    ),
    # düzey 2
    '0005': patch(
        'Aşağıdaki cümlelerin hangisinde altı çizili sözcük gerçek anlamıyla kullanılmıştır?',
        {
            'A': 'Akşam gelen beklenmedik haber, bayram sofrasında hepimizin ağzının tadını **kaçırdı**.',
            'B': 'Zor koşullarda elde ettiği başarı, onu çevresindekilerin gözünde iyice **büyüttü**.',
            'C': 'Yıkanan çamaşırları iyice sıktıktan sonra balkondaki ipe tek tek **astı**.',
            'D': 'Toplantıda söz almak isteyen genç memuru, müdür sert bakışlarıyla adeta **dondurdu**.',
            'E': 'Yaşlı kadının yalnızlığını anlattığı sözler, dinleyen herkesin içini **burktu**.',
        },
        'C',
        '"Çamaşırı ipe asmak" cümlesinde "asmak" sözcüğü gerçek (temel) anlamıyla kullanılmıştır. Diğer seçeneklerdeki altı çizili sözcükler mecaz anlam taşımaktadır.',
    ),
    # düzey 3
    '0006': patch(
        'Aşağıdaki cümlelerin hangisinde deyim, anlamına uygun bir bağlamda kullanılmamıştır?',
        {
            'A': 'Yeni işinde kısa sürede kendini gösterdi ve terfi aldı.',
            'B': 'Yıllarca biriktirdiği parayı bir gecede har vurup harman savurdu.',
            'C': 'Müdürünü kapıda görünce dili tutuldu, tek kelime edemedi.',
            'D': 'Arkadaşının başarısını duyunca gözleri parladı.',
            'E': 'Sınavı kazanınca etekleri tutuştu, havalara uçtu.',
        },
        'E',
        "'Etekleri tutuşmak' çok telaşlanmak, korkuya kapılmak demektir; sevinç bildiren bir bağlamda kullanılamaz. Diğer deyimler anlamlarına uygun kullanılmıştır.",
    ),
    # düzey 2
    '0007': patch(
        'Aşağıdaki cümlelerin hangisindeki ikileme, yakın anlamlı sözcüklerle oluşturulmuştur?',
        {
            'A': 'Bütün gün tarlada çalışan işçiler, akşam yorgun argın köye döndüler.',
            'B': 'Dağ köyüne giden eğri büğrü yolda eski araba birkaç kez yan yatacak gibi oldu.',
            'C': 'Kapıyı yavaş yavaş aralayıp odada uyuyan kardeşini uyandırmamaya çalıştı.',
            'D': 'Bankadaki sıra o kadar uzundu ki aşağı yukarı iki saat bekledik.',
            'E': 'Yalanlarını ne kadar gizlemeye çalışsa da er geç her şey ortaya çıkar.',
        },
        'A',
        "'Argın' da 'yorgun' anlamındadır; ikileme yakın anlamlı sözcüklerle kurulmuştur. 'Aşağı yukarı' ve 'er geç' karşıt anlamlı, 'yavaş yavaş' aynı sözcüğün tekrarı, 'eğri büğrü' anlamlı-anlamsız sözcükle kurulmuştur.",
    ),
    # düzey 3
    '0008': patch(
        '"Toplantıda herkes düşüncesini **açık** bir dille anlattı." cümlesindeki "açık" sözcüğüyle aşağıdakilerden hangisinde "açık" aynı anlamda kullanılmıştır?',
        {
            'A': 'Sabah yağmur yağmasına rağmen öğleden sonra hava **açık** ve güneşli oldu.',
            'B': 'Düğüne gitmek için üstüne **açık** renk bir gömlek ile lacivert bir ceket giymişti.',
            'C': 'Odayı havalandırmak için açtığın kapıyı akşam **açık** bırakma, üşürüz.',
            'D': 'İki şirket, yanlış anlaşılmaları önlemek için anlaşmayı **açık** sözlerle yazdı.',
            'E': 'Mahalledeki fırın, bayram günlerinde de sabahın erken saatlerinde **açık** olur.',
        },
        'D',
        'Örnek cümlede "açık", anlaşılır-net anlamındadır. Aynı anlam "açık, anlaşılır sözler" kullanımında vardır. Diğerlerinde sözcük kapalı olmayan, bulutsuz, faal ya da koyu olmayan renk anlamlarıyla geçmiştir.',
    ),
    # düzey 2
    '0009': patch(
        'Aşağıdaki cümlelerin hangisinde "göz" sözcüğü bir organ anlamı dışında kullanılmıştır?',
        {
            'A': 'Rüzgârlı havada yürürken **gözüne** bir toz kaçınca bir süre kenarda durdu.',
            'B': 'Uykusuz geçen gecenin ardından yorgunluktan **gözleri** kıpkırmızı olmuştu.',
            'C': 'Nöbetçi asker, sabaha kadar **gözlerini** bir an olsun kapatmadan bekledi.',
            'D': 'Güneş tam karşıdan vurunca **gözlerini** kısarak uzaktaki tekneye baktı.',
            'E': 'Kışlık giysileri yerleştirdikten sonra dolabın alt **gözüne** kitaplarını koydu.',
        },
        'E',
        'Diğer cümlelerde "göz" görme organını anlatır. "Dolabın gözü" ise bölme-çekmece anlamındadır; organ anlamı taşımadığından bu kullanım diğerlerinden ayrılır.',
    ),
    # düzey 2
    '0010': patch(
        '"Taşıma su ile değirmen dönmez." atasözünün anlamı aşağıdakilerden hangisidir?',
        {
            'A': 'Yeterince emek harcanmadan, çalışılmadan kalıcı başarı sağlanamaz.',
            'B': 'İnsanlar birlik olup güçlerini birleştirdiğinde her işin üstesinden gelir.',
            'C': 'Herkes ancak kendi gücünün yettiği işe girişmeli, fazlasına kalkışmamalıdır.',
            'D': 'Sürekli olmayan, dışarıdan sağlanan kaynakla bir iş yürütülemez.',
            'E': 'Sabırla bekleyip doğru zamanı kollayan kişi eninde sonunda amacına ulaşır.',
        },
        'D',
        'Bu atasözü, kalıcı-kendine ait olmayan, dışarıdan taşınan kaynakla bir işin sürdürülemeyeceğini anlatır. Doğru yorum, süreksiz-dış kaynağın işi yürütemeyeceğini belirten seçenektir.',
    ),
    # düzey 3
    '0011': patch(
        '"Sınavı kazanmış; ancak sonucu hâlâ öğrenememişti." cümlesinden kesin olarak çıkarılabilecek yargı aşağıdakilerden hangisidir?',
        {
            'A': 'Sonucu başkalarından öğrenecektir.',
            'B': 'Sonucu öğrenmek için çaba göstermemiştir.',
            'C': 'Sınav çok zor bir sınavdır.',
            'D': 'Sınav sonuçları geç açıklanmıştır.',
            'E': 'Kişi sınavda başarılı olmuştur.',
        },
        'E',
        'Cümlede kişinin sınavı kazandığı doğrudan belirtilmiştir; bu, kesin bir bilgidir. Sonucun neden öğrenilemediği, sınavın zorluğu ya da sonucun nasıl öğrenileceği cümlede yer almaz; bunlar çıkarılamaz.',
    ),
    # düzey 2
    '0012': patch(
        'Aşağıdaki cümlelerin hangisinde öznel bir yargı yoktur?',
        {
            'A': 'Yazarın son romanı, sade diliyle her yaştan okura seslenebilen bir eser olmuş.',
            'B': 'Romanın son bölümleri, ilk bölümlerin aksine fazlasıyla aceleye getirilmiş.',
            'C': "Kitabın ilk baskısı 1998 yılında İstanbul'daki küçük bir yayınevinde yapıldı.",
            'D': 'Yazarın bugüne kadar yazdığı en akıcı ve en olgun eser kuşkusuz bu romandır.',
            'E': 'Romanın kahramanları o kadar inandırıcı çizilmiş ki onları tanıyor gibi oluyoruz.',
        },
        'C',
        'Kitabın yayımlandığı yıl ve yer, doğruluğu araştırılarak kanıtlanabilecek nesnel bir bilgidir. Diğer cümleler kişisel değerlendirme içerir.',
    ),
    # düzey 2
    '0013': patch(
        'Aşağıdaki cümlelerin hangisinde sitem yoktur?',
        {
            'A': 'Bu güzel hediye için sana ne kadar teşekkür etsem az.',
            'B': 'Bir telefon edecek kadar da mı vaktin olmadı?',
            'C': 'Doğum günümü yine unutmuşsun, oysa ben seninkini hep hatırlarım.',
            'D': 'Bunca yıllık dostluğumuzdan sonra bunu bana nasıl yaparsın?',
            'E': 'Hastanede yatarken bir kez olsun arayıp sormadın.',
        },
        'A',
        'Sitem, kırgınlığın yakınma yoluyla dile getirilmesidir. Teşekkür bildiren cümlede kırgınlık değil minnet vardır; diğerleri karşıdakinin ilgisizliğinden yakınır.',
    ),
    # düzey 2
    '0014': patch(
        'Aşağıdaki cümlelerden hangisi olasılık anlamı taşımaz?',
        {
            'A': 'Arabanın kapısını kilitledim ama galiba anahtarı kontakta unuttum.',
            'B': 'Yönetim kurulu toplantısı yarın saat üçte şirketin merkez binasında başlayacak.',
            'C': 'Hava durumu öğleden sonra sağanak yağabileceğini söylüyor, şemsiyeni yanına al.',
            'D': 'Hafta sonu işlerimizi erken bitirirsek belki biz de akşam size uğrarız.',
            'E': 'Sabah yedide evden çıktığına göre bu saatte çoktan şehre varmış olmalı.',
        },
        'B',
        "'Olmalı, belki, -abilir, galiba' ifadeleri cümlelere olasılık anlamı katar. Toplantının saatini bildiren cümlede olasılık değil kesinlik vardır.",
    ),
    # düzey 2
    '0015': patch(
        '"O, konuşmasıyla değil, yaptıklarıyla saygı gördü." cümlesinden aşağıdakilerden hangisi çıkarılabilir?',
        {
            'A': 'Kişi konuşmayı sevmez, her ortamda susmayı yeğlerdi.',
            'B': 'Kişi, çevresindeki insanlarla ve olup bitenlerle ilgilenmezdi.',
            'C': 'Kişi, çevresinden gerçek bir saygı görmemiştir.',
            'D': 'Kişi, sözleriyle değil davranışlarıyla değer kazanmıştır.',
            'E': 'Kişi, güzel ve etkili konuşmasıyla herkesçe tanınır.',
        },
        'D',
        'Cümlede saygının kaynağı olarak konuşma değil, yapılan işler gösterilir. Doğru çıkarım, kişinin davranışlarıyla değer kazandığını belirten seçenektir; diğerleri cümleyle çelişir.',
    ),
    # düzey 3
    '0016': patch(
        '"Bu filmi izlemek için sinemaya değil, adeta bir yarışa gider gibi koştu." cümlesinde altı çizili bölümle anlatılmak istenen aşağıdakilerden hangisidir?',
        {
            'A': 'Sinemanın çok uzak olduğu',
            'B': 'Spor yapmayı çok sevdiği',
            'C': 'Filmi izlemeyi aslında istemediği, gönülsüz davrandığı',
            'D': 'Filme büyük bir heves ve acelesi olduğu',
            'E': 'Filmin çoktan başladığı',
        },
        'D',
        '"Yarışa gider gibi koşmak" benzetmesi, kişinin filme karşı büyük bir istek ve acele içinde olduğunu anlatır. Doğru seçenek, bu hevesi ve aceleyi belirten ifadedir.',
    ),
    # düzey 2
    '0017': patch(
        'Aşağıdaki cümlelerin hangisinde "abartma" söz konusudur?',
        {
            'A': 'Sınav haftası olduğu için bugün kütüphanede iki saat aralıksız çalıştım.',
            'B': 'Sabah servisi kalabalık olduğundan otobüs durakta beş dakika fazla bekledi.',
            'C': 'Kapıdan girer girmez o içten gülüşü bütün odayı aydınlatıyordu.',
            'D': 'Kış yaklaştığı için çarşıya inip kendine kalın bir ceket satın aldı.',
            'E': 'Ertelenen toplantı, yöneticilerin isteğiyle öğleden sonra yapıldı.',
        },
        'C',
        '"Gülüşün bütün odayı aydınlatması", gerçekte olamayacak bir durumu güçlü bir etki için söylemektir; bu abartmadır. Diğer cümleler olağan, gerçekçi bilgiler içerir.',
    ),
    # düzey 2
    '0018': patch(
        'Aşağıdaki cümlelerin hangisi hem neden hem sonuç bildiren bir yapıdadır?',
        {
            'A': 'Yarın sabah güneş doğmadan kalkıp köye doğru yola çıkacağız.',
            'B': 'Küçük kardeşim, odasını her gün özenle toplar ve kitaplarını rafa dizerdi.',
            'C': 'Denizin suyu, sabahki serin havaya rağmen bugün oldukça ılıktı.',
            'D': 'Sınavdan önceki haftalarda düzenli çalıştığı için yüksek bir puan aldı.',
            'E': 'Bu kitabı geçen yaz tatilinde, sahildeki küçük bir kafede okumuştum.',
        },
        'D',
        'Cümlede "iyi hazırlanmak" neden, "yüksek puan almak" sonuçtur; "...için" bağlacı neden-sonuç ilişkisi kurar. Diğer cümlelerde böyle bir neden-sonuç bağı bulunmaz.',
    ),
    # düzey 3
    '0019': patch(
        '"Sözlerinde en küçük bir abartıya bile yer vermez, hep gördüğünü yazardı." cümlesinde yazarın hangi özelliği anlatılmaktadır?',
        {
            'A': 'Gerçekçi ve nesnel bir tutum benimsediği',
            'B': 'Okurları kolayca etkilediği',
            'C': 'Eserlerini ağır bir dille yazdığı',
            'D': 'Kendi yaşamını anlattığı',
            'E': 'Hayal gücünün çok geniş olduğu',
        },
        'A',
        'Yazarın abartıya yer vermeyip "hep gördüğünü" yazması, gerçeğe bağlı, nesnel bir tutum benimsediğini gösterir. Doğru seçenek bu gerçekçi tutumu belirtir; diğerleri cümlede yer almaz.',
    ),
    # düzey 2
    '0020': patch(
        'Aşağıdaki cümlelerin hangisinde bir "koşula bağlılık" söz konusu değildir?',
        {
            'A': 'Yağmur başlayınca bahçedeki masayı toplayıp hep birlikte içeri girdik.',
            'B': 'Bu gece erken yatarsan sabah sınava çok daha dinç kalkarsın.',
            'C': 'Annenden izin alırsan hafta sonu bizimle kampa gelebilirsin.',
            'D': 'Biraz acele etmezsen son otobüse yetişemeyeceğiz, haberin olsun.',
            'E': 'Düzenli çalışırsan yıl sonundaki sınavı rahatlıkla başarırsın.',
        },
        'A',
        'Diğer cümlelerde bir durum, bir koşulun gerçekleşmesine bağlanmıştır ("-sa/-se": yatarsan, alırsan, etmezsen, çalışırsan). "Yağmur başlayınca içeri girdik" ise bir koşulu değil, gerçekleşmiş bir zaman ilişkisini anlatır; koşula bağlılık yoktur.',
    ),
    # düzey 3
    '0021': patch(
        "I. Bu yıl domatesler çok **tuttu**.\nII. Çocuk annesinin elini sıkıca **tuttu**.\nIII. Ankara'dan Konya'ya yolculuk üç saat **tuttu**.\nIV. Kar yağdı ama yere **tutmadı**.\nV. Yaşlı adamın kolunu **tutup** karşıya geçirdi.\n\nNumaralanmış cümlelerde kalın yazılmış sözcük kaç farklı anlamda kullanılmıştır?",
        {
            'A': 'İki',
            'B': 'Dört',
            'C': 'Üç',
            'D': 'Bir',
            'E': 'Beş',
        },
        'B',
        "I'de 'verim vermek, iyi sonuç vermek', II ve V'te 'elle kavramak', III'te 'sürmek, zaman almak', IV'te 'yere yerleşmek, birikmek' anlamındadır. II ile V aynı anlamda olduğundan dört farklı anlam vardır.",
    ),
    # düzey 3
    '0022': patch(
        '"Uzun yıllar sonra memleketine dönünce **köklü** bir değişimle karşılaştı." cümlesindeki "köklü" sözcüğünün anlamı aşağıdakilerden hangisidir?',
        {
            'A': 'Beklenmedik biçimde gelişen',
            'B': 'Geçici ve yüzeysel olan',
            'C': 'Temelden ve esaslı biçimde',
            'D': 'Başkalarınca yönlendirilen',
            'E': 'Yavaş yavaş ilerleyen',
        },
        'C',
        '"Köklü değişim", yüzeyde kalmayan, temele inen, esaslı bir değişimi anlatır. "Geçici ve yüzeysel" seçeneği tam karşıt anlamı verdiğinden yanlıştır; diğerleri de sözcüğün anlamını karşılamaz.',
    ),
    # düzey 2
    '0023': patch(
        '"Yeni müdür, işleri kısa sürede **yoluna koydu**." cümlesindeki altı çizili deyimin anlamı aşağıdakilerden hangisidir?',
        {
            'A': 'Bir işi sürekli ertelemek',
            'B': 'Yolculuğa hazırlık yapmak',
            'C': 'Karışıklığı düzene sokmak',
            'D': 'Bir işi başkasına devretmek',
            'E': 'Herkesle tartışmaya girmek',
        },
        'C',
        '"Yoluna koymak" deyimi, aksayan ya da karışık bir işi düzene sokmak, yolunda gitmesini sağlamak demektir. Bu nedenle doğru karşılık "karışık bir durumu düzene sokmak"tır.',
    ),
    # düzey 3
    '0024': patch(
        'Yaşlı balıkçı sabah (I) **erkenden** kayığına bindi. Denizin (II) **sessizliği**, onun yorgun (III) **yüreğine** iyi geliyordu. Ağlarını attıktan sonra (IV) **kıyıya** baktı; yıllar önce kaybettiği eşinin (V) **gölgesi** hâlâ oradaydı sanki.\n\nBu parçada numaralanmış sözcüklerden hangi ikisi gerçek anlamı dışında kullanılmıştır?',
        {
            'A': 'III ve V',
            'B': 'I ve II',
            'C': 'II ve IV',
            'D': 'IV ve V',
            'E': 'I ve IV',
        },
        'A',
        "'Yorgun yüreği' sözünde yürek, organ anlamında değil 'gönül, duygular' anlamında; 'eşinin gölgesi' sözünde gölge 'hayali, anısı' anlamında kullanılmıştır. Diğer sözcükler gerçek anlamlarındadır.",
    ),
    # düzey 2
    '0025': patch(
        '"Sütten ağzı yanan yoğurdu üfleyerek yer." atasözünün anlamı aşağıdakilerden hangisidir?',
        {
            'A': 'Herkes kendi çıkarını düşünür.',
            'B': 'Küçük sorunlar zamanla büyür.',
            'C': 'Zarar gören kişi daha temkinli olur.',
            'D': 'Tecrübeli kişi her işin üstesinden gelir.',
            'E': 'Emek verilmeyen işten sonuç alınmaz.',
        },
        'C',
        'Bu atasözü, bir olaydan zarar gören kişinin benzer durumlarda aşırı dikkatli, temkinli davrandığını anlatır. Doğru yorum, geçmiş zararın kişiyi temkinli kıldığını belirten seçenektir.',
    ),
    # düzey 2
    '0026': patch(
        'Aşağıdaki cümlelerin hangisinde gerekçeli bir yargı vardır?',
        {
            'A': 'Yol, belediye ekiplerinin karı temizlemesinin ardından ulaşıma açıldı.',
            'B': 'Fırtınanın ardından yolun yeniden kapanıp kapanmayacağını kimse bilmiyor.',
            'C': 'Kış aylarında bu dağ yolundan geçmek isteyen sürücü sayısı oldukça azdır.',
            'D': 'Bu dağ yolu kış aylarında genellikle kapanır, çünkü bölgeye çok kar yağar.',
            'E': 'Belediye, kapanan yolu yarın sabah iş makineleriyle yeniden açmayı planlıyor.',
        },
        'D',
        "Gerekçeli yargıda bir yargı nedeniyle birlikte verilir. Yolun kapanması yargısının gerekçesi 'çünkü çok kar yağar' sözüyle belirtilmiştir.",
    ),
    # düzey 2
    '0027': patch(
        '"Ağır" sözcüğü aşağıdaki cümlelerin hangisinde "ölçülü, ağırbaşlı" anlamında kullanılmıştır?',
        {
            'A': 'Toplantıda söylediği o **ağır** sözler, genç arkadaşımızı derinden kırdı.',
            'B': 'Dedem geçen yıl **ağır** bir hastalık geçirdi ama şimdi oldukça iyi.',
            'C': 'Tatil dönüşü valiz o kadar **ağırdı** ki merdivenlerden zor taşıdım.',
            'D': 'Gece yediğimiz **ağır** yemekler yüzünden sabaha kadar uyuyamadım.',
            'E': 'Komşumuz Ahmet Bey, az konuşan, **ağır** ve oturaklı bir insandır.',
        },
        'E',
        '"Ağır, oturaklı insan" tamlamasında sözcük, davranışları ölçülü, ağırbaşlı anlamındadır. Diğerlerinde "ağır", tartıca fazla, ciddi/şiddetli ya da kırıcı anlamlarıyla geçmiştir.',
    ),
    # düzey 3
    '0028': patch(
        'Aşağıdaki cümlelerin hangisinde dolaylama vardır?',
        {
            'A': 'Altın fiyatları bu hafta yeniden yükselişe geçti.',
            'B': 'Bölgenin ekonomisi büyük ölçüde pamuk üretimine dayanıyor.',
            'C': 'Bölgenin ekonomisi büyük ölçüde beyaz altına dayanıyor.',
            'D': 'Tarlada çalışanların sayısı her yıl biraz daha azalıyor.',
            'E': 'Beyaz eşya üretimi geçen yıl belirgin biçimde arttı.',
        },
        'C',
        "Dolaylama, bir kavramı onu çağrıştıran birden çok sözcükle anlatmaktır. 'Beyaz altın' pamuğu dolaylı yoldan anlatır. 'Beyaz eşya' ve 'altın fiyatları' kendi anlamlarıyla kullanılmıştır.",
    ),
    # düzey 3
    '0029': patch(
        '"Onun için para, mutluluğun tek **anahtarı**ydı." cümlesindeki "anahtar" sözcüğünün kullanımı aşağıdakilerden hangisiyle özdeştir?',
        {
            'A': 'Tatile çıkmadan önce evin yedek **anahtarını** alt kattaki komşuya bıraktık.',
            'B': 'Öğretmenimize göre her alanda başarının **anahtarı** sabırlı ve düzenli çalışmaktır.',
            'C': 'Kontaktaki **anahtarı** çevirince eski arabanın motoru öksürerek çalıştı.',
            'D': 'Babasının anahtarlığında farklı kapılara ait birçok **anahtar** vardı.',
            'E': 'Okuldan dönünce evin **anahtarını** çantasında unuttuğunu fark etti.',
        },
        'B',
        'Örnek cümlede "anahtar", bir sonuca ulaştıran yol-araç anlamında mecaz olarak kullanılmıştır. Aynı mecaz "başarının anahtarı" kullanımında vardır. Diğerlerinde sözcük gerçek anlamıyla (kilit açan araç) geçmiştir.',
    ),
    # düzey 2
    '0030': patch(
        'Aşağıdaki cümlelerin hangisinde altı çizili sözcük mecaz anlamıyla kullanılmıştır?',
        {
            'A': 'Gece yarısı **kara** bir kedi sessizce bahçenin duvarından atladı.',
            'B': 'Sabahtan beri gökyüzünde **kara** bulutlar toplanıyor, rüzgâr sertleşiyordu.',
            'C': 'Akşam gelen o **kara** haber, bayram sevincimizi bir anda yok etti.',
            'D': 'Öğretmen, sorunun çözümünü **kara** tahtaya adım adım yazarak anlattı.',
            'E': 'Soğuk havada üstüne kalın, **kara** bir palto giyip öyle çıktı.',
        },
        'C',
        '"Kara haber" tamlamasında "kara", renk anlamını değil, kötü-üzücü anlamını taşır; bu mecaz kullanımdır. Diğer seçeneklerde "kara" gerçek renk anlamıyla geçmiştir.',
    ),
    # düzey 2
    '0031': patch(
        'Aşağıdaki cümlelerin hangisinde amaç-sonuç ilişkisi vardır?',
        {
            'A': 'Gece boyunca yağan yağmur yüzünden sabah bütün sokaklar ıslaktı.',
            'B': 'Hava akşamüstü iyice soğuduğundan salondaki sobayı yaktık.',
            'C': 'Üniversite sınavını kazanmak için aylarca gece gündüz çalıştı.',
            'D': 'Düzenli çalıştığı için sınavı beklenenden çok daha rahat kazandı.',
            'E': 'Uzun yolculuktan çok yorulmuştu, bu yüzden akşam erkenden yattı.',
        },
        'C',
        '"Sınavı kazanmak için" ifadesi bir amacı, "gece gündüz çalıştı" bunun için yapılan eylemi verir; böylece amaç-sonuç ilişkisi kurulur. Diğer cümlelerde neden-sonuç ya da koşul ilişkisi bulunur.',
    ),
    # düzey 2
    '0032': patch(
        'Aşağıdaki cümlelerin hangisi nesnel bir yargı içerir?',
        {
            'A': 'Annemin yaptığı bu yemek, bence ülkenin en lezzetli yemeklerinden biridir.',
            'B': 'Filmin hüzünlü müzikleri, izleyen herkesin içini derinden burkuyor.',
            'C': 'Bu şehrin en keyifli ve en renkli mevsimi kuşkusuz ilkbahardır.',
            'D': 'Konserde şarkı söyleyen genç kadının sesi hepimizi büyüledi.',
            'E': 'Şehir, üç büyük akarsuyun birleştiği geniş bir ovanın kenarına kurulmuştur.',
        },
        'E',
        'Şehrin üç akarsuyun birleştiği bir ovanın kenarına kurulmuş olması gözlemle ve belgeyle doğrulanabilen bir olgudur; bu nesnel yargıdır. Diğer seçenekler beğeni ve değerlendirme bildiren öznel yargılardır.',
    ),
    # düzey 2
    '0033': patch(
        'Aşağıdaki cümlelerin hangisinde kesinlik anlamı vardır?',
        {
            'A': 'Herkesin korktuğu bu sınav, sanıldığı kadar zor olmayabilir.',
            'B': 'İşlerimiz yetişirse belki hafta sonu size de uğrayabiliriz.',
            'C': 'Akşam altıda işten çıktığına göre bu saatte evde olmalı.',
            'D': 'Deniz seviyesinde saf su, yüz santigrat derecede kaynar.',
            'E': 'Gökyüzündeki bulutlara bakılırsa galiba yarın yağmur yağacak.',
        },
        'D',
        "Suyun kaynama sıcaklığı kesin bir bilgidir. Diğer cümlelerde 'galiba, olmalı, belki, -abilir' sözleriyle olasılık ya da tahmin anlatılır.",
    ),
    # düzey 2
    '0034': patch(
        '"Çalışkan olduğu kadar da alçakgönüllü bir öğrenciydi." cümlesinden aşağıdakilerden hangisi çıkarılabilir?',
        {
            'A': 'Öğrenci çalışkandır ama alçakgönüllü değildir.',
            'B': 'Öğrenci çalışkan olsa da başarısızdır.',
            'C': 'Alçakgönüllülüğü çalışkanlığını gölgelemiştir.',
            'D': 'Öğrenci alçakgönüllü değil, kibirlidir.',
            'E': 'Öğrenci hem çalışkan hem alçakgönüllüdür.',
        },
        'E',
        '"Çalışkan olduğu kadar alçakgönüllü" ifadesi, öğrencide bu iki özelliğin birlikte ve dengeli biçimde bulunduğunu anlatır. Doğru çıkarım, her iki niteliğin de var olduğunu belirten seçenektir.',
    ),
    # düzey 2
    '0035': patch(
        'Aşağıdaki cümlelerin hangisinde varsayım yoktur?',
        {
            'A': 'Tut ki bu iş planladığın gibi gitmedi, o zaman ne yapacaksın?',
            'B': 'Yarın sabah erkenden yola çıkacağız, akşama doğru köye varmış oluruz.',
            'C': 'Farz edelim ki sınavdaki bütün sorulara doğru cevap verdin.',
            'D': 'Diyelim ki son trene de yetişemedik, geceyi nerede geçireceğiz?',
            'E': 'Varsayalım ki önümüzdeki ay bütün fiyatlar yarı yarıya düştü.',
        },
        'B',
        "'Diyelim ki, farz edelim ki, tut ki, varsayalım ki' ifadeleri bir durumu gerçekleşmiş gibi kabul ederek varsayım bildirir. Yola çıkma planını bildiren cümlede varsayım yoktur.",
    ),
    # düzey 2
    '0036': patch(
        '"Az konuşan, çok dinleyen biriydi; bu yüzden herkes ona güvenirdi." cümlesinden aşağıdakilerden hangisi çıkarılamaz?',
        {
            'A': 'Kişi az konuşan biridir.',
            'B': 'Kişi iyi bir dinleyicidir.',
            'C': 'Güven, konuşkanlığından kaynaklanır.',
            'D': 'İnsanlar ona güven duyar.',
            'E': 'Suskunluğu güven kazanmasında etkilidir.',
        },
        'C',
        'Cümleye göre güven, kişinin az konuşup çok dinlemesinden kaynaklanır; konuşkanlığından değil. "Güven konuşkanlığından kaynaklanır" yargısı cümleyle çelişir ve çıkarılamaz.',
    ),
    # düzey 2
    '0037': patch(
        '"Ödevini bitirdikten sonra dışarı çıkabilirsin." cümlesinden aşağıdakilerden hangisi çıkarılır?',
        {
            'A': 'Dışarı çıkmak yasaktır.',
            'B': 'Ödev zaten bitirilmiştir.',
            'C': 'Ödev bitirilse de dışarı çıkılamaz.',
            'D': 'Dışarı çıkmak ödevin bitmesine bağlıdır.',
            'E': 'Dışarı çıkmak ödevden önce olmalıdır.',
        },
        'D',
        'Cümlede dışarı çıkma izni, ödevin bitirilmesi koşuluna bağlanmıştır. Doğru çıkarım, dışarı çıkmanın ödevin bitirilmesine bağlı olduğunu belirten seçenektir.',
    ),
    # düzey 2
    '0038': patch(
        '"Bu şiiri anlamak için birkaç kez okumak gerekir." cümlesinde şiirle ilgili aşağıdakilerden hangisi vurgulanır?',
        {
            'A': 'Kolayca anlaşılamayacak kadar kapalı olduğu',
            'B': 'Sözcüklerinin ezberlenmesinin son derece güç olduğu',
            'C': 'Yeni yazılmış olduğu',
            'D': 'Çok uzun olduğu',
            'E': 'Sesli okunması gerektiği',
        },
        'A',
        'Şiiri anlamak için birkaç kez okumanın gerekmesi, onun ilk okuyuşta kolayca çözülemeyen, kapalı bir anlatıma sahip olduğunu gösterir. Doğru seçenek bu kapalılığı belirtir.',
    ),
    # düzey 3
    '0039': patch(
        'Aşağıdaki cümlelerin hangisinde ad aktarması (mecazımürsel) yapılmıştır?',
        {
            'A': 'Konser için satışa çıkarılan biletler günler önceden tükenmişti.',
            'B': 'Sanatçı sahneye çıktığı anda salonun ışıkları yavaşça söndü.',
            'C': 'Konserin sonunda bütün salon ayağa kalkıp sanatçıyı dakikalarca alkışladı.',
            'D': 'Konser başladığında salonda yaklaşık bin beş yüz kişi bulunuyordu.',
            'E': 'Konser salonunun duvarları yaz tatilinde açık renge boyanmıştı.',
        },
        'C',
        "Ayağa kalkıp alkışlayan salon değil, salondaki insanlardır; 'salon' sözcüğü içinde bulunanları anlatmak için kullanılmıştır. Bu, benzetme amacı gütmeden yapılan ad aktarmasıdır.",
    ),
    # düzey 2
    '0040': patch(
        '"Bu başarıyı yalnız ona borçluyuz." cümlesinden kesin olarak çıkarılabilecek yargı aşağıdakilerden hangisidir?',
        {
            'A': 'Başarı beklenenden küçüktür.',
            'B': 'Başarıya birçok kişi katkı sunmuştur.',
            'C': 'Başarı ekibin ortak emeğidir.',
            'D': 'Başarıda tek pay sahibi o kişidir.',
            'E': 'O kişi başarıya engel olmuştur.',
        },
        'D',
        '"Yalnız ona borçluyuz" ifadesi, başarının tek nedeni-pay sahibi olarak o kişiyi gösterir. Doğru çıkarım, başarıda tek pay sahibinin o kişi olduğunu belirten seçenektir; diğerleri cümleyle çelişir.',
    ),
    # düzey 3
    '0041': patch(
        '"Dağın eteğinde kurulmuş küçük bir köydü burası." cümlesindeki "etek" sözcüğüyle aşağıdakilerden hangisinde "etek" aynı anlamda kullanılmıştır?',
        {
            'A': 'Annesinin doğum gününde aldığı yeni **etek** ona çok yakışmıştı.',
            'B': 'Uzun masa örtüsünün **etekleri** neredeyse yere değiyordu.',
            'C': 'Yağmur başlayınca **eteklerini** toplayıp evin yolunu tuttu.',
            'D': 'Sabah erkenden yola çıkıp tepenin **eteğine** kadar yürüdük.',
            'E': 'Annem ütü yaparken dalgınlıkla en sevdiği **eteğini** biraz yaktı.',
        },
        'D',
        'Örnek cümlede "etek", bir yükseltinin alt bölümü anlamındadır. Aynı anlam "tepenin eteği" kullanımında vardır. Diğerlerinde sözcük giysi ya da bir şeyin alt-sarkan kısmı anlamıyla geçmektedir.',
    ),
    # düzey 2
    '0042': patch(
        'Aşağıdaki cümlelerin hangisinde "yüz" sözcüğü diğerlerinden farklı bir anlamda kullanılmıştır?',
        {
            'A': 'Durgun suyun **yüzünde** sonbahardan kalan sarı yapraklar süzülüyordu.',
            'B': 'Uzun süre kullanılmayan masanın **yüzü** kalın bir toz tabakasıyla kaplanmıştı.',
            'C': 'Fırtınanın ardından denizin **yüzü** bugün ayna gibi durgundu.',
            'D': 'Gece yarısı gölün **yüzü** ay ışığıyla gümüş gibi parlıyordu.',
            'E': 'Annem misafir odasındaki yastıkların **yüzünü** yenileriyle değiştirdi.',
        },
        'E',
        'Diğer cümlelerde "yüz", bir şeyin üst-dış bölümü anlamındadır (suyun yüzü, denizin yüzü gibi). Yastığın "yüzü" ise üzerine geçirilen kılıf anlamındadır; bu kılıf anlamı sözcüğü diğerlerinden ayırır.',
    ),
    # düzey 2
    '0043': patch(
        'Aşağıdaki deyimlerden hangisinin açıklaması yanlış verilmiştir?',
        {
            'A': 'Burun kıvırmak: küçümsemek, beğenmemek',
            'B': 'Ağzı kulaklarına varmak: çok üzülmek',
            'C': 'Göz yummak: bir kusuru görmezden gelmek',
            'D': 'Etekleri zil çalmak: çok sevinmek',
            'E': 'Kulak kabartmak: gizlice dinlemeye çalışmak',
        },
        'B',
        '"Ağzı kulaklarına varmak" deyimi çok sevinmek, sevinçten yüzü gülmek anlamındadır; "çok üzülmek" açıklaması yanlıştır. Diğer seçeneklerdeki deyim-açıklama eşleştirmeleri doğrudur.',
    ),
    # düzey 2
    '0044': patch(
        '"Ağaç yaşken eğilir." atasözüyle anlatılmak istenen aşağıdakilerden hangisidir?',
        {
            'A': 'Eğitim küçük yaşta, karakter oturmadan verilmelidir.',
            'B': 'Acele edilen işten hayır gelmez.',
            'C': 'Doğa koşulları insanı zorlar.',
            'D': 'Yardımlaşmak insanı güçlü kılar.',
            'E': 'Herkes, yaptığı iyi ya da kötü her işin karşılığını mutlaka görür.',
        },
        'A',
        'Bu atasözü, insanın eğitilip yönlendirilmesinin küçük yaşta, kişilik henüz biçimlenmeden yapılması gerektiğini anlatır. Doğru yorum, erken yaşta eğitimin önemine değinen seçenektir.',
    ),
    # düzey 2
    '0045': patch(
        'Aşağıdaki cümlelerin hangisinde bir deyim cümleye "çok dikkatli ve tedbirli davranmak" anlamı katmıştır?',
        {
            'A': 'Söylediklerimize kulak asmadan kendi bildiğini okumaya devam etti.',
            'B': 'Bu sorunu çözmek için günlerce kafa yordu, uzun uzun düşündü.',
            'C': 'Yıllardır tanıdığı arkadaşına güvenip bütün sırlarını açtı.',
            'D': 'Yeni işinde hata yapmamak için her adımını ölçüp biçerek atıyordu.',
            'E': 'Bu ay işinin başından aşkın olduğunu, tatile çıkamayacağını söyledi.',
        },
        'D',
        '"Adımını ölçüp biçmek", her hareketini dikkatle, tedbirli biçimde yapmayı anlatan bir deyimdir. Bu anlam yalnızca ilgili seçenekte vardır; diğer cümlelerdeki deyimler farklı anlamlar taşır.',
    ),
    # düzey 3
    '0046': patch(
        '"Bu roman, savaşın insan ruhunda açtığı **derin** yaraları anlatıyor." cümlesindeki "derin" sözcüğünün anlamı aşağıdakilerden hangisidir?',
        {
            'A': 'Kolayca unutulup geçen',
            'B': 'Herkesçe bilinen, sıradan olan',
            'C': 'Dibi yüzeyden çok aşağıda olan',
            'D': 'Etkisi güçlü ve kalıcı olan',
            'E': 'Yeni ortaya çıkmış olan',
        },
        'D',
        'Burada "derin", fiziksel bir ölçüyü değil, etkisi güçlü ve kalıcı olan anlamını taşır (mecaz). "Dibi yüzeyden aşağıda olan" gerçek anlam olduğu için bağlama uymaz; diğerleri de sözcüğü karşılamaz.',
    ),
    # düzey 2
    '0047': patch(
        'Aşağıdaki cümlelerin hangisinde yakın anlamlı iki sözcük bir arada kullanılmıştır?',
        {
            'A': 'Ne kadar saklamaya çalışsalar da er geç gerçek ortaya çıkacak.',
            'B': 'Kimseye haber vermeden, sessiz sedasız şehirden ayrılıp gitti.',
            'C': 'Misafirler gelmeden önce içeri girip dışarı çıktı, yerinde duramadı.',
            'D': 'Zor zamanlarda iyi günde kötü günde hep yanımda olan tek dosttu.',
            'E': 'Bilgisayar konusunda az çok bilgim var, istersen yardımcı olurum.',
        },
        'B',
        '"Sessiz" ile "sedasız" yakın (eş) anlamlı sözcüklerdir ve pekiştirme için bir arada kullanılmıştır. Diğer seçeneklerdeki ikililer (iyi-kötü, az-çok, içeri-dışarı, er-geç) karşıt anlamlıdır.',
    ),
    # düzey 2
    '0048': patch(
        'Aşağıdaki cümlelerin hangisinde "düşmek" sözcüğü "payına ayrılmak, isabet etmek" anlamında kullanılmıştır?',
        {
            'A': 'Babasından kalan mirastan ona yalnızca küçük bir tarla düştü.',
            'B': 'İlacını içtikten sonra çocuğun ateşi akşama doğru biraz düştü.',
            'C': 'Sonbahar rüzgârıyla ağaçlardaki yapraklar bir bir yere düştü.',
            'D': 'Kaldırımdaki buzu fark etmeyince dengesini kaybedip düştü.',
            'E': 'Hasat başlayınca sebze fiyatları geçen aya göre belirgin biçimde düştü.',
        },
        'A',
        '"Mirastan pay düşmek" kullanımında "düşmek", birine ayrılmak, isabet etmek anlamındadır. Diğerlerinde sözcük yukarıdan aşağıya inmek, azalmak ya da yere kapanmak anlamlarıyla geçmiştir.',
    ),
    # düzey 2
    '0049': patch(
        '**sürmek:** Bir süre devam etmek.\n\nYukarıda anlamı verilen sözcük aşağıdaki cümlelerin hangisinde bu anlamıyla kullanılmıştır?',
        {
            'A': 'Şirket, uzun süredir üzerinde çalıştığı yeni ürünlerini piyasaya sürdü.',
            'B': 'Köylüler, yağmurdan sonra tarlayı sabah erkenden traktörle sürdüler.',
            'C': 'Yağmurlu havada arabayı virajlarda son derece dikkatli sürüyordu.',
            'D': 'Kahvaltıda kızarmış ekmeğine bolca tereyağı ve bal sürdü.',
            'E': 'Bütçe görüşmeleri beklenenden çok uzun sürdü, öğle arası bile verilemedi.',
        },
        'E',
        "Toplantının uzun sürmesi, belli bir zaman devam etmesidir. Diğer cümlelerde 'sürmek' toprağı işlemek, yaymak, satışa çıkarmak ve araç kullanmak anlamlarındadır.",
    ),
    # düzey 2
    '0050': patch(
        '"Yıllarca bu konuda **kılı kırk yardı**." cümlesindeki altı çizili deyimin anlamı aşağıdakilerden hangisidir?',
        {
            'A': 'Kolay yoldan sonuç almak',
            'B': 'Çok ince eleyip titizlikle davranmak',
            'C': 'Sürekli sözünden dönmek',
            'D': 'Herkesle didişip durmak',
            'E': 'Bir işi özensizce, baştan savma biçimde yapıp geçmek',
        },
        'B',
        '"Kılı kırk yarmak", bir işi çok ince ayrıntısına kadar, titizlikle ele almak anlamındadır. Doğru karşılık, incelik ve titizliği belirten seçenektir.',
    ),
    # düzey 2
    '0051': patch(
        'Aşağıdaki cümlelerin hangisinde neden-sonuç ilişkisi yoktur?',
        {
            'A': 'Sınava zamanında yetişmek için sabah erkenden evden çıktı.',
            'B': 'Gece boyunca yağan yoğun yağmur yüzünden maç ertelendi.',
            'C': 'Hammadde fiyatları arttı, bu yüzden firmanın satışları düştü.',
            'D': 'Gün boyu çok yorulduğundan akşam erkenden uyuyakaldı.',
            'E': 'Yollar buz tuttuğu için valilik okulları bir gün tatil etti.',
        },
        'A',
        "'Sınava zamanında yetişmek için' erken çıkmanın amacını bildirir; cümlede amaç-sonuç ilişkisi vardır. Diğer cümlelerde eylemin nedeni verilmiştir.",
    ),
    # düzey 2
    '0052': patch(
        '"Bu kitabı okursan olayları çok daha iyi anlarsın." cümlesinde aşağıdaki anlam ilişkilerinden hangisi vardır?',
        {
            'A': 'Beğeni',
            'B': 'Koşul-sonuç',
            'C': 'Amaç-sonuç',
            'D': 'Karşılaştırma',
            'E': 'Neden-sonuç',
        },
        'B',
        'Olayları daha iyi anlamanın gerçekleşmesi, kitabın okunması koşuluna bağlanmıştır ("...okursan..."). Bu, koşul-sonuç ilişkisidir; neden ya da amaç bildiren bir yapı yoktur.',
    ),
    # düzey 2
    '0053': patch(
        '"Keşke o gün ona o sözleri hiç söylemeseydim." cümlesinde aşağıdaki duygulardan hangisi ağır basar?',
        {
            'A': 'Özlem',
            'B': 'Pişmanlık',
            'C': 'Umut',
            'D': 'Derin şaşkınlık',
            'E': 'Öfke',
        },
        'B',
        '"Keşke ... söylemeseydim" kalıbı, yapılan bir davranıştan duyulan üzüntüyü, yani pişmanlığı anlatır. Cümlede özlem, şaşkınlık ya da umut sezdiren bir öğe yoktur.',
    ),
    # düzey 2
    '0054': patch(
        '"Bu sözler bir yazara değil, ancak yılların ustasına yakışır." cümlesinde aşağıdakilerden hangisi vurgulanmaktadır?',
        {
            'A': 'Ustalığın öğrenilemeyeceği',
            'B': 'Sözlerin yanlış anlaşıldığı',
            'C': 'Sözlerin sıradan olduğu',
            'D': 'Yazarlığın kolay bir uğraş olduğu',
            'E': 'Sözleri söyleyenin çok deneyimli olduğu',
        },
        'E',
        'Cümlede sözlerin ancak "yılların ustasına" yakışacağı belirtilerek, bunları söyleyenin uzun deneyime sahip, usta biri olduğu vurgulanır. Doğru seçenek, söyleyenin deneyimini öne çıkaran ifadedir.',
    ),
    # düzey 2
    '0055': patch(
        '"Ne kadar erken çıkarsak, o kadar rahat ederiz." cümlesinde anlamca aşağıdakilerden hangisi vurgulanır?',
        {
            'A': 'Rahat etmenin olanaksız olduğu',
            'B': 'İki durum arasında doğru orantı bulunduğu',
            'C': 'Erken çıkmanın gereksiz olduğu',
            'D': 'Yolculuğun çok uzun süreceği',
            'E': 'Geç çıkmanın yolculuk için daha uygun olacağı',
        },
        'B',
        '"Ne kadar ... o kadar ..." kalıbı, erken çıkma ile rahat etme arasında doğru orantılı bir ilişki kurar: biri arttıkça öteki de artar. Doğru seçenek bu orantıyı belirtir.',
    ),
    # düzey 2
    '0056': patch(
        '"Denemelerinde yalın bir dil kullanır, süslü anlatımdan kaçınır." cümlesinde yazarın hangi yönü belirtilmiştir?',
        {
            'A': 'Yapmacıksız, sade bir anlatımı benimsediği',
            'B': 'Okurları güldürmeyi amaçladığı',
            'C': 'Eserlerini çok uzun tuttuğu',
            'D': 'Şiir türünde de ürünler verdiği',
            'E': 'Konularını güncel olaylardan seçtiği',
        },
        'A',
        'Cümlede yazarın "yalın bir dil" kullandığı ve "süslü anlatımdan kaçındığı" belirtilir; bu, sade ve yapmacıksız bir anlatımı benimsediğini gösterir. Diğer seçenekler cümlede yer almayan bilgilerdir.',
    ),
    # düzey 2
    '0057': patch(
        '"Onu görür görmez tanıdım." cümlesinde "görür görmez" ifadesiyle anlatılmak istenen aşağıdakilerden hangisidir?',
        {
            'A': 'Tanıma işinin gerçekleşmediği',
            'B': 'Görmenin çok güç olduğu',
            'C': 'İki eylemin arasından uzun zaman geçtiği',
            'D': 'Görme eyleminin gerçekleşmediği',
            'E': 'Bir eylemin hemen ardından ötekinin olduğu',
        },
        'E',
        '"Görür görmez" kalıbı, görme eyleminin hemen ardından tanıma eyleminin gerçekleştiğini, iki eylemin art arda olduğunu anlatır. Doğru seçenek bu "hemen ardından olma" anlamını verir.',
    ),
    # düzey 2
    '0058': patch(
        '"Yalnız bu konuda değil, hemen her konuda titiz davranırdı." cümlesinden aşağıdakilerden hangisi çıkarılır?',
        {
            'A': 'Titizliği pek çok alanı kapsar.',
            'B': 'Kişi titiz biri değildir.',
            'C': 'Kişi bu konuda özensizdir.',
            'D': 'Kişi tek bir konuda titizdir.',
            'E': 'Kişi titizliği sonradan kazanmıştır.',
        },
        'A',
        '"Yalnız bu konuda değil, hemen her konuda" ifadesi, kişinin titizliğinin tek bir alanla sınırlı olmayıp geniş bir alanı kapsadığını anlatır. Doğru çıkarım bu yaygınlığı belirten seçenektir.',
    ),
    # düzey 3
    '0059': patch(
        'Aşağıdaki cümlelerin hangisinde atasözü, anlamına uygun bir durumu anlatmak için kullanılmamıştır?',
        {
            'A': 'Çocuğuna kitap okuma alışkanlığını küçük yaşta kazandırdı; ağaç yaşken eğilir.',
            'B': 'Önemsemediği küçük borç sonunda başını yaktı; ummadığın taş baş yarar.',
            'C': 'Bir kez dolandırılınca her teklife şüpheyle bakar oldu; sütten ağzı yanan yoğurdu üfleyerek yer.',
            'D': 'Her gün biraz biriktirerek sonunda ev sahibi oldu; damlaya damlaya göl olur.',
            'E': 'Herkes ona yardım edince işi bir günde bitirdi; ağaç yaşken eğilir.',
        },
        'E',
        "'Ağaç yaşken eğilir' eğitimin küçük yaşta verilmesi gerektiğini anlatır; yardımlaşmayla işin çabuk bitmesi bu atasözüyle anlatılamaz. Diğer cümlelerde atasözleri anlamlarına uygun durumlar için kullanılmıştır.",
    ),
    # düzey 2
    '0060': patch(
        '"Ne yaparsan yap, onu bu kararından döndüremezsin." cümlesinde aşağıdakilerden hangisi vurgulanır?',
        {
            'A': 'Kişinin kararsız olduğu',
            'B': 'Kişinin başkalarınca kolayca ikna edilebildiği',
            'C': 'Kararın henüz verilmediği',
            'D': 'Kararın yanlış olduğu',
            'E': 'Kişinin kararında son derece direndiği',
        },
        'E',
        '"Ne yaparsan yap ... döndüremezsin" ifadesi, hiçbir çabanın kişiyi kararından vazgeçiremeyeceğini, yani onun kararında kesin bir kararlılıkla direndiğini anlatır. Doğru seçenek bu direnci belirtir.',
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
    print(f"1 paket / {len(PATCHES)} soru ('Türkçe — Sözcükte ve Cümlede Anlam' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
