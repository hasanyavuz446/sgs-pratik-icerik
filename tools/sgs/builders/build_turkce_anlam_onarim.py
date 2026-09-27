#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sozcukte ve Cumlede Anlam — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

60 soru korunarak onarildi: 16 mutlak ifadeli celdirici ayni dogruluk degerini koruyacak bicimde yeniden yazildi; ornek cumle secenekli sorularda dogru cumleyi kisaltmak yerine bir celdirici cumleye dogal sozcuk eklendi. Kor ogrenci %33 -> %26 (UYARI kapandi).

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Turkce - sozcukte ve cumlede anlam
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/turkce/sozcukte_cumlede_anlam.json"
STYLE_REF = 'SGS Türkçe sözcükte anlam'
ONEK = "turkce-anlam-gen-"


def patch(stem, options, answer, solution, ref='Türkçe - sözcükte ve cümlede anlam'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        '"Bu ustanın yaptığı türküler, dinleyenin yüreğine **işliyor**." cümlesinde altı çizili sözcüğün kattığı anlam aşağıdakilerden hangisidir?',
        {
            'A': 'Yavaş yavaş ilerlemek',
            'B': 'İnsanı derinden etkilemek',
            'C': 'Ustalıkla süslenerek bezenmek',
            'D': 'Sıkça yinelenip durmak',
            'E': 'Bir yüzeye oyularak çizilmek',
        },
        'B',
        '"İşlemek" sözcüğü burada gerçek anlamıyla (bir yüzeyi oymak, nakış yapmak) değil, mecaz anlamıyla kullanılmıştır: türkünün insanı içten, derinden etkilemesi. Bu yüzden doğru karşılık "insanı derinden etkilemek"tir; diğer seçenekler sözcüğün gerçek anlamına ya da ilgisiz anlamlara yöneliktir.',
    ),
    # düzey 2
    '0002': patch(
        'Aşağıdaki cümlelerin hangisinde altı çizili sözcük terim anlamıyla kullanılmıştır?',
        {
            'A': 'İç **açılar** toplamı 180°dir.',
            'B': 'Çocuğun **yüzü** sevinçle aydınlandı.',
            'C': 'Sabah erkenden **yola** çıktılar.',
            'D': 'Bahçedeki **gül**ler yeni açmıştı.',
            'E': 'Yorgunluktan **gözleri** kapanıyordu.',
        },
        'A',
        'Terim, bir bilim ya da sanat dalına özgü anlamdır. "Açı", geometriye özgü bir kavram olarak kullanıldığından terim anlamı taşır. Diğer seçeneklerdeki sözcükler günlük, gerçek anlamlarıyla geçmiştir.',
    ),
    # düzey 2
    '0003': patch(
        '"Onun **soğuk** tavırları herkesi rahatsız ediyordu." cümlesindeki "soğuk" sözcüğüyle aşağıdakilerden hangisinde "soğuk" aynı anlamda kullanılmıştır?',
        {
            'A': 'Bu kış çok soğuk günler yaşadık.',
            'B': 'Bize karşı mesafeli davrandı.',
            'C': 'Yemek soğumadan sofraya oturalım.',
            'D': 'Soğuk havada dışarı çıkmadı.',
            'E': 'Soğuk suyla yüzünü yıkadı.',
        },
        'B',
        'Örnek cümlede "soğuk", sevgisiz-ilgisiz, mesafeli tutum anlamıyla (mecaz) kullanılmıştır. Aynı anlam "mesafeli, soğuk davrandı" seçeneğinde vardır. Diğerlerinde sözcük ısı azlığı (gerçek anlam) bildirir.',
    ),
    # düzey 2
    '0004': patch(
        '"Damlaya damlaya göl olur." atasözüyle aşağıdakilerden hangisi anlamca aynı doğrultudadır?',
        {
            'A': 'Bugünün işini yarına bırakma.',
            'B': 'Ateş düştüğü yeri yakar.',
            'C': 'Küçük birikimler zamanla büyür.',
            'D': 'Sakla samanı, gelir zamanı.',
            'E': 'Bir elin nesi var, iki elin sesi var.',
        },
        'C',
        '"Damlaya damlaya göl olur", küçük birikimlerin zamanla büyük bir bütün oluşturduğunu anlatır. Birikimin çoğalmasını vurgulayan seçenek anlamca aynı doğrultudadır; diğerleri farklı iletiler taşır.',
    ),
    # düzey 2
    '0005': patch(
        'Aşağıdaki cümlelerin hangisinde altı çizili sözcük gerçek anlamıyla kullanılmıştır?',
        {
            'A': 'Sözleri hepimizin içini **burktu**.',
            'B': 'Bakışlarıyla beni resmen **dondurdu**.',
            'C': 'Çamaşırı iyice sıkıp ipe **astı**.',
            'D': 'Bu haber ağzımızın tadını **kaçırdı**.',
            'E': 'Başarısı gözümüzde onu **büyüttü**.',
        },
        'C',
        '"Çamaşırı ipe asmak" cümlesinde "asmak" sözcüğü gerçek (temel) anlamıyla kullanılmıştır. Diğer seçeneklerdeki altı çizili sözcükler mecaz anlam taşımaktadır.',
    ),
    # düzey 2
    '0006': patch(
        '"Cömert" sözcüğünün karşıt (zıt) anlamlısı aşağıdakilerden hangisidir?',
        {
            'A': 'Alçakgönüllü',
            'B': 'Görgülü',
            'C': 'Eli açık',
            'D': 'Yardımsever',
            'E': 'Cimri',
        },
        'E',
        '"Cömert", elindekini kolayca veren demektir; karşıtı, veremeyen-esirgeyen anlamındaki "cimri"dir. "Eli açık" ve "yardımsever" ise cömertle yakın anlamlıdır, karşıtı değildir.',
    ),
    # düzey 2
    '0007': patch(
        'Aşağıdaki sözcüklerden hangisi soyut anlamlıdır?',
        {
            'A': 'Özgürlük',
            'B': 'Deniz',
            'C': 'Pencere',
            'D': 'Kalem',
            'E': 'Ağaç',
        },
        'A',
        'Soyut kavramlar, beş duyuyla algılanamayan; yalnızca akılla, düşünceyle kavranan varlıklardır. "Özgürlük" böyle bir kavramdır. Diğer seçenekler duyularla algılanabilen somut varlıklardır.',
    ),
    # düzey 3
    '0008': patch(
        '"Toplantıda herkes düşüncesini **açık** bir dille anlattı." cümlesindeki "açık" sözcüğüyle aşağıdakilerden hangisinde "açık" aynı anlamda kullanılmıştır?',
        {
            'A': 'Bugün hava açık ve güneşli.',
            'B': 'Kapıyı açık bırakma, üşürüz.',
            'C': 'Mağaza sabah dokuzda açık olur.',
            'D': 'Anlaşmayı açık sözlerle yazdılar.',
            'E': 'Üstüne açık renk bir gömlek giymişti.',
        },
        'D',
        'Örnek cümlede "açık", anlaşılır-net anlamındadır. Aynı anlam "açık, anlaşılır sözler" kullanımında vardır. Diğerlerinde sözcük kapalı olmayan, bulutsuz, faal ya da koyu olmayan renk anlamlarıyla geçmiştir.',
    ),
    # düzey 2
    '0009': patch(
        'Aşağıdaki cümlelerin hangisinde "göz" sözcüğü bir organ anlamı dışında kullanılmıştır?',
        {
            'A': 'Yorgunluktan gözleri kızarmıştı.',
            'B': 'Gözüne bir toz kaçmış olmalı.',
            'C': 'Nöbet boyunca gözlerini bir an bile kapatmadı.',
            'D': 'Gözlerini kısarak uzağa baktı.',
            'E': 'Dolabın alt gözüne kitaplarını koydu.',
        },
        'E',
        'Diğer cümlelerde "göz" görme organını anlatır. "Dolabın gözü" ise bölme-çekmece anlamındadır; organ anlamı taşımadığından bu kullanım diğerlerinden ayrılır.',
    ),
    # düzey 2
    '0010': patch(
        '"Taşıma su ile değirmen dönmez." atasözünün anlamı aşağıdakilerden hangisidir?',
        {
            'A': 'Herkes ancak kendi gücünün yettiği işe girişmeli, fazlasına kalkışmamalıdır.',
            'B': 'İnsanlar birlik olup güçlerini birleştirdiğinde her işin üstesinden gelir.',
            'C': 'Sabırla bekleyip doğru zamanı kollayan kişi eninde sonunda amacına ulaşır.',
            'D': 'Sürekli olmayan, dışarıdan sağlanan kaynakla bir iş yürütülemez.',
            'E': 'Yeterince emek harcanmadan, çalışılmadan kalıcı başarı sağlanamaz.',
        },
        'D',
        'Bu atasözü, kalıcı-kendine ait olmayan, dışarıdan taşınan kaynakla bir işin sürdürülemeyeceğini anlatır. Doğru yorum, süreksiz-dış kaynağın işi yürütemeyeceğini belirten seçenektir.',
    ),
    # düzey 3
    '0011': patch(
        '"Sınavı kazanmış; ancak sonucu hâlâ öğrenememişti." cümlesinden kesin olarak çıkarılabilecek yargı aşağıdakilerden hangisidir?',
        {
            'A': 'Sonucu öğrenmek için çaba göstermemiştir.',
            'B': 'Sınav çok zor bir sınavdır.',
            'C': 'Sınav sonuçları geç açıklanmıştır.',
            'D': 'Sonucu başkalarından öğrenecektir.',
            'E': 'Kişi sınavda başarılı olmuştur.',
        },
        'E',
        'Cümlede kişinin sınavı kazandığı doğrudan belirtilmiştir; bu, kesin bir bilgidir. Sonucun neden öğrenilemediği, sınavın zorluğu ya da sonucun nasıl öğrenileceği cümlede yer almaz; bunlar çıkarılamaz.',
    ),
    # düzey 2
    '0012': patch(
        'Aşağıdaki cümlelerin hangisi öznel bir yargı içerir?',
        {
            'A': 'Kitap, iki dile çevrilmiştir.',
            'B': "Kitap, ilk kez 1998 yılında İstanbul'da yayımlanmış.",
            'C': 'Yazarın en akıcı, en güzel eseri budur.',
            'D': 'Eser, on iki bölüme ayrılmış.',
            'E': 'Roman, üç yüz sayfadan oluşuyor.',
        },
        'C',
        '"En akıcı, en güzel eser" değerlendirmesi kişiden kişiye değişebilen, kanıtlanamayan bir görüştür; bu yüzden özneldir. Diğer seçenekler sayı ve olgu bildiren, doğrulanabilir nesnel yargılardır.',
    ),
    # düzey 2
    '0013': patch(
        '"Sen de bir arasan, bir sorsan ne kaybederdin sanki?" cümlesinde ağır basan duygu aşağıdakilerden hangisidir?',
        {
            'A': 'Sitem',
            'B': 'Sevinç',
            'C': 'Korku',
            'D': 'Merak',
            'E': 'Hayranlık',
        },
        'A',
        'Cümlede, karşıdaki kişinin ilgisizliğinden duyulan kırgınlık ve yakınma vardır; bu duygu sitemdir. Sevinç, korku ya da hayranlık sezdiren bir ifade bulunmaz.',
    ),
    # düzey 2
    '0014': patch(
        'Aşağıdaki cümlelerin hangisinde bir olasılık (ihtimal) anlamı vardır?',
        {
            'A': 'Kitabı dün akşam bitirdim.',
            'B': 'Bu saatte gelmiş olmalı.',
            'C': 'Toplantı iki saat sürdü.',
            'D': 'Sabah tam sekizde yola çıktık.',
            'E': 'Yarın yağmur yağacak.',
        },
        'B',
        '"Gelmiş olmalı" ifadesi kesinlik değil, tahmine dayalı bir olasılık bildirir. Diğer cümleler kesinlik ya da gerçekleşmiş olgu bildirir; olasılık taşımaz.',
    ),
    # düzey 3
    '0015': patch(
        '"O, konuşmasıyla değil, yaptıklarıyla saygı gördü." cümlesinden aşağıdakilerden hangisi çıkarılabilir?',
        {
            'A': 'Kişi, güzel ve etkili konuşmasıyla herkesçe tanınır.',
            'B': 'Kişi, çevresinden gerçek bir saygı görmemiştir.',
            'C': 'Kişi, çevresindeki insanlarla ve olup bitenlerle ilgilenmezdi.',
            'D': 'Kişi, sözleriyle değil davranışlarıyla değer kazanmıştır.',
            'E': 'Kişi konuşmayı sevmez, her ortamda susmayı yeğlerdi.',
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
            'A': 'Bugün kütüphanede iki saat çalıştım.',
            'B': 'Otobüs durakta beş dakika bekledi.',
            'C': 'Gülüşü bütün odayı aydınlatıyordu.',
            'D': 'Yeni bir ceket satın aldı.',
            'E': 'Toplantı öğleden sonra yapıldı.',
        },
        'C',
        '"Gülüşün bütün odayı aydınlatması", gerçekte olamayacak bir durumu güçlü bir etki için söylemektir; bu abartmadır. Diğer cümleler olağan, gerçekçi bilgiler içerir.',
    ),
    # düzey 2
    '0018': patch(
        'Aşağıdaki cümlelerin hangisi hem neden hem sonuç bildiren bir yapıdadır?',
        {
            'A': 'Bu kitabı geçen yaz okumuştum.',
            'B': 'Yarın sabah güneş doğmadan erkenden yola çıkacağız.',
            'C': 'Denizin suyu bugün oldukça ılıktı.',
            'D': 'Sınava iyi hazırlandığı için yüksek puan aldı.',
            'E': 'Odasını her gün düzenli tutardı.',
        },
        'D',
        'Cümlede "iyi hazırlanmak" neden, "yüksek puan almak" sonuçtur; "...için" bağlacı neden-sonuç ilişkisi kurar. Diğer cümlelerde böyle bir neden-sonuç bağı bulunmaz.',
    ),
    # düzey 2
    '0019': patch(
        '"Sözlerinde en küçük bir abartıya bile yer vermez, hep gördüğünü yazardı." cümlesinde yazarın hangi özelliği anlatılmaktadır?',
        {
            'A': 'Gerçekçi ve nesnel bir tutum benimsediği',
            'B': 'Kendi yaşamını anlattığı',
            'C': 'Hayal gücünün çok geniş olduğu',
            'D': 'Eserlerini ağır bir dille yazdığı',
            'E': 'Okurları kolayca etkilediği',
        },
        'A',
        'Yazarın abartıya yer vermeyip "hep gördüğünü" yazması, gerçeğe bağlı, nesnel bir tutum benimsediğini gösterir. Doğru seçenek bu gerçekçi tutumu belirtir; diğerleri cümlede yer almaz.',
    ),
    # düzey 3
    '0020': patch(
        'Aşağıdaki cümlelerin hangisinde bir "koşula bağlılık" söz konusu değildir?',
        {
            'A': 'Yağmur yağınca içeri girdik.',
            'B': 'İznini alırsan gelebilirsin.',
            'C': 'Acele etmezsen yetişemezsin.',
            'D': 'Erken yatarsan sabah dinç kalkarsın.',
            'E': 'Çalışırsan başarırsın.',
        },
        'A',
        'Diğer cümlelerde bir durum, bir koşulun gerçekleşmesine bağlanmıştır ("-sa/-se, -ırsan": yatarsan, çalışırsan, alırsan, etmezsen). "Yağmur yağınca içeri girdik" ise bir koşulu değil, gerçekleşmiş bir zaman-neden ilişkisini anlatır; koşula bağlılık yoktur.',
    ),
    # düzey 2
    '0021': patch(
        'Aşağıdaki cümlelerin hangisinde "acı" sözcüğü mecaz anlamıyla kullanılmıştır?',
        {
            'A': 'Turşunun suyu acımış.',
            'B': 'Acı haberle sarsıldık bugün.',
            'C': 'Kahvesini hep acı içerdi.',
            'D': 'Biberin acısı dilimi yaktı.',
            'E': 'İlacın acı tadını zor bastırdı.',
        },
        'B',
        '"Acı haber" tamlamasında sözcük tat anlamını değil, üzücü-yürek yakan anlamını taşır; bu mecaz kullanımdır. Öteki seçeneklerde "acı" doğrudan tat (gerçek anlam) bildirir.',
    ),
    # düzey 2
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
            'D': 'Herkesle tartışmaya girmek',
            'E': 'Bir işi başkasına devretmek',
        },
        'C',
        '"Yoluna koymak" deyimi, aksayan ya da karışık bir işi düzene sokmak, yolunda gitmesini sağlamak demektir. Bu nedenle doğru karşılık "karışık bir durumu düzene sokmak"tır.',
    ),
    # düzey 3
    '0024': patch(
        '"İşten çıkarılınca **eli böğründe** kaldı." cümlesindeki altı çizili deyimin anlamı aşağıdakilerden hangisidir?',
        {
            'A': 'Çaresiz ve şaşkın kalmak',
            'B': 'Sevincini gizleyememek',
            'C': 'Başkalarına muhtaç olmamak',
            'D': 'Bir işe hemen girişmek',
            'E': 'Öfkeden ne yapacağını bilememek',
        },
        'A',
        '"Eli böğründe kalmak", umduğunu bulamayıp çaresiz, ne yapacağını bilemez durumda kalmayı anlatır. Doğru karşılık, çaresizlik ve şaşkınlığı içeren seçenektir.',
    ),
    # düzey 2
    '0025': patch(
        '"Sütten ağzı yanan yoğurdu üfleyerek yer." atasözünün anlamı aşağıdakilerden hangisidir?',
        {
            'A': 'Küçük sorunlar zamanla büyür.',
            'B': 'Tecrübeli kişi her işin üstesinden gelir.',
            'C': 'Zarar gören kişi daha temkinli olur.',
            'D': 'Herkes kendi çıkarını düşünür.',
            'E': 'Emek verilmeyen işten sonuç alınmaz.',
        },
        'C',
        'Bu atasözü, bir olaydan zarar gören kişinin benzer durumlarda aşırı dikkatli, temkinli davrandığını anlatır. Doğru yorum, geçmiş zararın kişiyi temkinli kıldığını belirten seçenektir.',
    ),
    # düzey 2
    '0026': patch(
        'Aşağıdaki cümlelerin hangisinde eş sesli (sesteş) bir sözcük yoktur?',
        {
            'A': 'Kırdaki yürüyüşte ayağı taşa takıldı.',
            'B': 'Bu yaz köye gitmeyi düşünüyoruz.',
            'C': 'Gül dalından koparılınca solar.',
            'D': 'Sınıfın en çalışkanı oydu.',
            'E': 'Çayı bahçenin kenarından geçiyordu.',
        },
        'D',
        '"Yaz" (mevsim/yazmak), "gül" (çiçek/gülmek), "çay" (dere/içecek), "taş" gibi sözcüklerin sesteşleri vardır. "Sınıfın en çalışkanı oydu" cümlesindeki sözcüklerin yazılışı-okunuşu aynı, anlamı farklı bir sesteşi yoktur.',
    ),
    # düzey 2
    '0027': patch(
        '"Ağır" sözcüğü aşağıdaki cümlelerin hangisinde "ölçülü, ağırbaşlı" anlamında kullanılmıştır?',
        {
            'A': 'Ağır yemekler midemi rahatsız etti.',
            'B': 'Ağır bir hastalık geçirdi geçen yıl.',
            'C': 'Bu ağır sözler onu çok kırdı.',
            'D': 'Valizi o kadar ağırdı ki taşıyamadım.',
            'E': 'Çok ağır, oturaklı bir insandır o.',
        },
        'E',
        '"Ağır, oturaklı insan" tamlamasında sözcük, davranışları ölçülü, ağırbaşlı anlamındadır. Diğerlerinde "ağır", tartıca fazla, ciddi/şiddetli ya da kırıcı anlamlarıyla geçmiştir.',
    ),
    # düzey 2
    '0028': patch(
        '"Kalabalık" sözcüğü aşağıdaki cümlelerin hangisinde ötekilerden farklı türde (nitelik olarak) kullanılmıştır?',
        {
            'A': 'Kalabalık bir aileden geliyordu.',
            'B': 'Kalabalık sınıfları ikiye böldüler.',
            'C': 'Kalabalığın arasında onu kaybettik.',
            'D': 'Kalabalık sokaklardan geçtik.',
            'E': 'Meydan bugün çok kalabalıktı.',
        },
        'C',
        'Diğer cümlelerde "kalabalık" bir varlığı niteleyen sıfattır (kalabalık aile, kalabalık sokak gibi). "Kalabalığın arasında" kullanımında ise sözcük çok sayıda insan topluluğu anlamıyla ad olarak geçtiğinden diğerlerinden ayrılır.',
    ),
    # düzey 2
    '0029': patch(
        '"Onun için para, mutluluğun tek **anahtarı**ydı." cümlesindeki "anahtar" sözcüğünün kullanımı aşağıdakilerden hangisiyle özdeştir?',
        {
            'A': 'Yedek anahtarı komşuya bıraktık.',
            'B': 'Başarının anahtarı sabırlı çalışmaktır.',
            'C': 'Anahtarı çevirince motor çalıştı.',
            'D': 'Evin kapısının anahtarını çantasında unutmuş.',
            'E': 'Anahtarlığında birçok anahtar vardı.',
        },
        'B',
        'Örnek cümlede "anahtar", bir sonuca ulaştıran yol-araç anlamında mecaz olarak kullanılmıştır. Aynı mecaz "başarının anahtarı" kullanımında vardır. Diğerlerinde sözcük gerçek anlamıyla (kilit açan araç) geçmiştir.',
    ),
    # düzey 2
    '0030': patch(
        'Aşağıdaki cümlelerin hangisinde altı çizili sözcük mecaz anlamıyla kullanılmıştır?',
        {
            'A': '**Kara** kedi bahçeden geçti.',
            'B': 'Sabahtan beri **kara** bulutlar toplanıyordu.',
            'C': 'Bu **kara** haber hepimizi yıktı.',
            'D': '**Kara** tahtaya sorunun çözümünü yazdı.',
            'E': 'Üstüne **kara** bir palto giymişti.',
        },
        'C',
        '"Kara haber" tamlamasında "kara", renk anlamını değil, kötü-üzücü anlamını taşır; bu mecaz kullanımdır. Diğer seçeneklerde "kara" gerçek renk anlamıyla geçmiştir.',
    ),
    # düzey 2
    '0031': patch(
        'Aşağıdaki cümlelerin hangisinde amaç-sonuç ilişkisi vardır?',
        {
            'A': 'Hava soğuduğundan sobayı yaktık.',
            'B': 'Yağmur yağınca sokaklar ıslandı.',
            'C': 'Sınavı kazanmak için gece gündüz çalıştı.',
            'D': 'Çok çalıştığı için sınavı rahatlıkla kazandı.',
            'E': 'Yorulmuştu, bu yüzden erken yattı.',
        },
        'C',
        '"Sınavı kazanmak için" ifadesi bir amacı, "gece gündüz çalıştı" bunun için yapılan eylemi verir; böylece amaç-sonuç ilişkisi kurulur. Diğer cümlelerde neden-sonuç ya da koşul ilişkisi bulunur.',
    ),
    # düzey 2
    '0032': patch(
        'Aşağıdaki cümlelerin hangisi nesnel bir yargı içerir?',
        {
            'A': 'Bu yemek, ülkenin en lezzetli yemeğidir.',
            'B': 'Bu şehrin en keyifli ve en renkli mevsimi ilkbahardır.',
            'C': 'Onun sesi hepimizi büyüledi.',
            'D': 'Filmin müzikleri insanın içini burkuyor.',
            'E': 'Şehir, üç büyük akarsuyun kıyısına kurulmuştur.',
        },
        'E',
        'Şehrin üç akarsuyun kıyısına kurulmuş olması gözlemle-belgeyle doğrulanabilen bir olgudur; bu nesnel yargıdır. Diğer seçenekler beğeni ve değerlendirme bildiren öznel yargılardır.',
    ),
    # düzey 2
    '0033': patch(
        'Aşağıdaki cümlelerin hangisinde bir karşılaştırma yapılmıştır?',
        {
            'A': 'Akşam olunca eve döndüler.',
            'B': 'Bu yıl kışın çok kar yağdı.',
            'C': 'Kitabı okuyup bitirince arkadaşına verdi.',
            'D': 'Ablası, ondan daha sabırlı biriydi.',
            'E': 'Sabahları erken kalkardı hep.',
        },
        'D',
        '"Ondan daha sabırlı" ifadesi iki kişiyi sabır yönünden karşılaştırır; "daha" sözcüğü karşılaştırma bildirir. Diğer cümlelerde bir kıyaslama yoktur.',
    ),
    # düzey 3
    '0034': patch(
        '"Çalışkan olduğu kadar da alçakgönüllü bir öğrenciydi." cümlesinden aşağıdakilerden hangisi çıkarılabilir?',
        {
            'A': 'Alçakgönüllülüğü çalışkanlığını gölgelemiştir.',
            'B': 'Öğrenci çalışkan olsa da başarısızdır.',
            'C': 'Öğrenci çalışkandır ama alçakgönüllü değildir.',
            'D': 'Öğrenci alçakgönüllü değil, kibirlidir.',
            'E': 'Öğrenci hem çalışkan hem alçakgönüllüdür.',
        },
        'E',
        '"Çalışkan olduğu kadar alçakgönüllü" ifadesi, öğrencide bu iki özelliğin birlikte ve dengeli biçimde bulunduğunu anlatır. Doğru çıkarım, her iki niteliğin de var olduğunu belirten seçenektir.',
    ),
    # düzey 2
    '0035': patch(
        'Aşağıdaki cümlelerin hangisinde bir "varsayım" söz konusudur?',
        {
            'A': 'Sabahtan beri durmadan çalıştı.',
            'B': 'Diyelim ki bu işi zamanında bitiremedik.',
            'C': 'Bugün hava gerçekten çok güzel.',
            'D': 'Bu kitabı geçen hafta okudum.',
            'E': 'Toplantıya herkes katıldı.',
        },
        'B',
        '"Diyelim ki" ifadesi, gerçekleşmemiş bir durumu gerçekmiş gibi kabul etmeyi, yani varsayımı bildirir. Diğer cümleler gerçekleşmiş ya da gözlenen durumları anlatır.',
    ),
    # düzey 3
    '0036': patch(
        '"Az konuşan, çok dinleyen biriydi; bu yüzden herkes ona güvenirdi." cümlesinden aşağıdakilerden hangisi çıkarılamaz?',
        {
            'A': 'Kişi iyi bir dinleyicidir.',
            'B': 'İnsanlar ona güven duyar.',
            'C': 'Güven, konuşkanlığından kaynaklanır.',
            'D': 'Kişi az konuşan biridir.',
            'E': 'Suskunluğu güven kazanmasında etkilidir.',
        },
        'C',
        'Cümleye göre güven, kişinin az konuşup çok dinlemesinden kaynaklanır; konuşkanlığından değil. "Güven konuşkanlığından kaynaklanır" yargısı cümleyle çelişir ve çıkarılamaz.',
    ),
    # düzey 3
    '0037': patch(
        '"Ödevini bitirdikten sonra dışarı çıkabilirsin." cümlesinden aşağıdakilerden hangisi çıkarılır?',
        {
            'A': 'Dışarı çıkmak yasaktır.',
            'B': 'Dışarı çıkmak ödevden önce olmalıdır.',
            'C': 'Ödev bitirilse de dışarı çıkılamaz.',
            'D': 'Dışarı çıkmak ödevin bitmesine bağlıdır.',
            'E': 'Ödev zaten bitirilmiştir.',
        },
        'D',
        'Cümlede dışarı çıkma izni, ödevin bitirilmesi koşuluna bağlanmıştır. Doğru çıkarım, dışarı çıkmanın ödevin bitirilmesine bağlı olduğunu belirten seçenektir.',
    ),
    # düzey 2
    '0038': patch(
        '"Bu şiiri anlamak için birkaç kez okumak gerekir." cümlesinde şiirle ilgili aşağıdakilerden hangisi vurgulanır?',
        {
            'A': 'Kolayca anlaşılamayacak kadar kapalı olduğu',
            'B': 'Yeni yazılmış olduğu',
            'C': 'Sesli okunması gerektiği',
            'D': 'Sözcüklerinin ezberlenmesinin son derece güç olduğu',
            'E': 'Çok uzun olduğu',
        },
        'A',
        'Şiiri anlamak için birkaç kez okumanın gerekmesi, onun ilk okuyuşta kolayca çözülemeyen, kapalı bir anlatıma sahip olduğunu gösterir. Doğru seçenek bu kapalılığı belirtir.',
    ),
    # düzey 2
    '0039': patch(
        '"İşi bilene sor." sözüyle anlatılmak istenen aşağıdakilerden hangisidir?',
        {
            'A': 'Soru sormanın zaman kaybı olduğu',
            'B': 'Herkesin her işi bildiği',
            'C': 'Her işte uzmana danışılması gerektiği',
            'D': 'Bilgili kişilere güvenilemeyeceği',
            'E': 'İşlerin tek başına yapılması gerektiği',
        },
        'C',
        'Bu söz, bir konuda doğru bilgiyi ancak o işi bilen-uzman kişiden almanın gerektiğini anlatır. Doğru yorum, işin uzmanına danışılması gerektiğini belirten seçenektir.',
    ),
    # düzey 3
    '0040': patch(
        '"Bu başarıyı yalnız ona borçluyuz." cümlesinden kesin olarak çıkarılabilecek yargı aşağıdakilerden hangisidir?',
        {
            'A': 'O kişi başarıya engel olmuştur.',
            'B': 'Başarı beklenenden küçüktür.',
            'C': 'Başarı ekibin ortak emeğidir.',
            'D': 'Başarıda tek pay sahibi o kişidir.',
            'E': 'Başarıya birçok kişi katkı sunmuştur.',
        },
        'D',
        '"Yalnız ona borçluyuz" ifadesi, başarının tek nedeni-pay sahibi olarak o kişiyi gösterir. Doğru çıkarım, başarıda tek pay sahibinin o kişi olduğunu belirten seçenektir; diğerleri cümleyle çelişir.',
    ),
    # düzey 2
    '0041': patch(
        '"Dağın eteğinde kurulmuş küçük bir köydü burası." cümlesindeki "etek" sözcüğüyle aşağıdakilerden hangisinde "etek" aynı anlamda kullanılmıştır?',
        {
            'A': 'Eteklerini toplayıp koşmaya başladı.',
            'B': 'Ütüde eteğini biraz yaktı.',
            'C': 'Masanın örtüsü eteklerinden sarkıyordu.',
            'D': 'Tepenin eteğine kadar yürüdük.',
            'E': 'Yeni aldığı eteği çok yakışmış.',
        },
        'D',
        'Örnek cümlede "etek", bir yükseltinin alt bölümü anlamındadır. Aynı anlam "tepenin eteği" kullanımında vardır. Diğerlerinde sözcük giysi ya da bir şeyin alt-sarkan kısmı anlamıyla geçmektedir.',
    ),
    # düzey 2
    '0042': patch(
        'Aşağıdaki cümlelerin hangisinde "yüz" sözcüğü diğerlerinden farklı bir anlamda kullanılmıştır?',
        {
            'A': 'Suyun yüzünde yapraklar süzülüyordu.',
            'B': 'Masanın yüzü tozla kaplanmıştı.',
            'C': 'Gölün yüzü ay ışığıyla parlıyordu.',
            'D': 'Denizin yüzü bugün durgundu.',
            'E': 'Yastığın yüzünü yeni değiştirdi.',
        },
        'E',
        'Diğer cümlelerde "yüz", bir şeyin üst-dış bölümü anlamındadır (suyun yüzü, denizin yüzü gibi). Yastığın "yüzü" ise üzerine geçirilen kılıf anlamındadır; bu kılıf anlamı sözcüğü diğerlerinden ayırır.',
    ),
    # düzey 3
    '0043': patch(
        'Aşağıdaki deyimlerden hangisinin açıklaması yanlış verilmiştir?',
        {
            'A': 'Etekleri zil çalmak: çok sevinmek',
            'B': 'Ağzı kulaklarına varmak: çok üzülmek',
            'C': 'Kulak kabartmak: gizlice dinlemeye çalışmak',
            'D': 'Burun kıvırmak: küçümsemek, beğenmemek',
            'E': 'Göz yummak: bir kusuru görmezden gelmek',
        },
        'B',
        '"Ağzı kulaklarına varmak" deyimi çok sevinmek, sevinçten yüzü gülmek anlamındadır; "çok üzülmek" açıklaması yanlıştır. Diğer seçeneklerdeki deyim-açıklama eşleştirmeleri doğrudur.',
    ),
    # düzey 2
    '0044': patch(
        '"Ağaç yaşken eğilir." atasözüyle anlatılmak istenen aşağıdakilerden hangisidir?',
        {
            'A': 'Eğitim küçük yaşta, karakter oturmadan verilmelidir.',
            'B': 'Doğa koşulları insanı zorlar.',
            'C': 'Acele edilen işten hayır gelmez.',
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
            'A': 'Bu konuda epey kafa yordu, uzun uzun düşündü.',
            'B': 'İşi başından aşkın olduğunu söyledi.',
            'C': 'Söylediklerine kulak asmadı bile.',
            'D': 'Her adımını ölçüp biçerek atıyordu.',
            'E': 'Ona güvenip bütün sırlarını açtı.',
        },
        'D',
        '"Adımını ölçüp biçmek", her hareketini dikkatle, tedbirli biçimde yapmayı anlatan bir deyimdir. Bu anlam yalnızca ilgili seçenekte vardır; diğer cümlelerdeki deyimler farklı anlamlar taşır.',
    ),
    # düzey 2
    '0046': patch(
        '"Bu roman, savaşın insan ruhunda açtığı **derin** yaraları anlatıyor." cümlesindeki "derin" sözcüğünün anlamı aşağıdakilerden hangisidir?',
        {
            'A': 'Dibi yüzeyden çok aşağıda olan',
            'B': 'Herkesçe bilinen, sıradan olan',
            'C': 'Yeni ortaya çıkmış olan',
            'D': 'Etkisi güçlü ve kalıcı olan',
            'E': 'Kolayca unutulup geçen',
        },
        'D',
        'Burada "derin", fiziksel bir ölçüyü değil, etkisi güçlü ve kalıcı olan anlamını taşır (mecaz). "Dibi yüzeyden aşağıda olan" gerçek anlam olduğu için bağlama uymaz; diğerleri de sözcüğü karşılamaz.',
    ),
    # düzey 2
    '0047': patch(
        'Aşağıdaki cümlelerin hangisinde yakın anlamlı iki sözcük bir arada kullanılmıştır?',
        {
            'A': 'İyi günde kötü günde yanımdaydı.',
            'B': 'Sessiz sedasız gitti.',
            'C': 'Az çok bu işten anlıyorum.',
            'D': 'Er geç gerçek ortaya çıkacak.',
            'E': 'İçeri girip dışarı çıktı durdu.',
        },
        'B',
        '"Sessiz" ile "sedasız" yakın (eş) anlamlı sözcüklerdir ve pekiştirme için bir arada kullanılmıştır. Diğer seçeneklerdeki ikililer (iyi-kötü, az-çok, içeri-dışarı, er-geç) karşıt anlamlıdır.',
    ),
    # düzey 2
    '0048': patch(
        'Aşağıdaki cümlelerin hangisinde "düşmek" sözcüğü "payına ayrılmak, isabet etmek" anlamında kullanılmıştır?',
        {
            'A': 'Mirastan ona küçük bir pay düştü.',
            'B': 'Yapraklar bir bir yere düştü.',
            'C': 'Yürürken buzda düştü.',
            'D': 'Ateşi akşama doğru düştü.',
            'E': 'Sebze fiyatları geçen aya göre biraz düştü.',
        },
        'A',
        '"Mirastan pay düşmek" kullanımında "düşmek", birine ayrılmak, isabet etmek anlamındadır. Diğerlerinde sözcük yukarıdan aşağıya inmek, azalmak ya da yere kapanmak anlamlarıyla geçmiştir.',
    ),
    # düzey 3
    '0049': patch(
        '"Bu kararı vermek benim **haddim** değil." cümlesindeki "had" sözcüğü aşağıdakilerden hangisiyle anlamca ilişkilidir?',
        {
            'A': 'İstek ve dilek',
            'B': 'Alışkanlık',
            'C': 'Cesaret',
            'D': 'Yorgunluk',
            'E': 'Sınır, yetki',
        },
        'E',
        '"Haddim değil" kullanımında "had", bir kişinin yetki ve sınırlarını anlatır. Bu nedenle sözcük "sınır, yetki" ile anlamca ilişkilidir; diğer seçenekler bu anlamı karşılamaz.',
    ),
    # düzey 2
    '0050': patch(
        '"Yıllarca bu konuda **kılı kırk yardı**." cümlesindeki altı çizili deyimin anlamı aşağıdakilerden hangisidir?',
        {
            'A': 'Bir işi özensizce, baştan savma biçimde yapıp geçmek',
            'B': 'Çok ince eleyip titizlikle davranmak',
            'C': 'Herkesle didişip durmak',
            'D': 'Kolay yoldan sonuç almak',
            'E': 'Sürekli sözünden dönmek',
        },
        'B',
        '"Kılı kırk yarmak", bir işi çok ince ayrıntısına kadar, titizlikle ele almak anlamındadır. Doğru karşılık, incelik ve titizliği belirten seçenektir.',
    ),
    # düzey 2
    '0051': patch(
        '"Yolları kapatan kar yüzünden okullar tatil edildi." cümlesinde aşağıdaki anlam ilişkilerinden hangisi vardır?',
        {
            'A': 'Neden-sonuç',
            'B': 'Olasılık',
            'C': 'Karşılaştırma',
            'D': 'Koşul-sonuç',
            'E': 'Amaç-sonuç',
        },
        'A',
        'Cümlede okulların tatil edilmesi (sonuç), yolları kapatan kar (neden) yüzünden gerçekleşmiştir. "...yüzünden" ifadesi neden-sonuç ilişkisi kurar; koşul ya da amaç bildiren bir yapı yoktur.',
    ),
    # düzey 2
    '0052': patch(
        '"Bu kitabı okursan olayları çok daha iyi anlarsın." cümlesinde aşağıdaki anlam ilişkilerinden hangisi vardır?',
        {
            'A': 'Neden-sonuç',
            'B': 'Koşul-sonuç',
            'C': 'Amaç-sonuç',
            'D': 'Beğeni',
            'E': 'Karşılaştırma',
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
            'D': 'Öfke',
            'E': 'Derin şaşkınlık',
        },
        'B',
        '"Keşke ... söylemeseydim" kalıbı, yapılan bir davranıştan duyulan üzüntüyü, yani pişmanlığı anlatır. Cümlede özlem, şaşkınlık ya da umut sezdiren bir öğe yoktur.',
    ),
    # düzey 3
    '0054': patch(
        '"Bu sözler bir yazara değil, ancak yılların ustasına yakışır." cümlesinde aşağıdakilerden hangisi vurgulanmaktadır?',
        {
            'A': 'Sözlerin yanlış anlaşıldığı',
            'B': 'Sözlerin sıradan olduğu',
            'C': 'Ustalığın öğrenilemeyeceği',
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
            'A': 'Erken çıkmanın gereksiz olduğu',
            'B': 'İki durum arasında doğru orantı bulunduğu',
            'C': 'Yolculuğun çok uzun süreceği',
            'D': 'Rahat etmenin olanaksız olduğu',
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
            'B': 'Eserlerini çok uzun tuttuğu',
            'C': 'Konularını güncel olaylardan seçtiği',
            'D': 'Şiir türünde de ürünler verdiği',
            'E': 'Okurları güldürmeyi amaçladığı',
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
    # düzey 3
    '0058': patch(
        '"Yalnız bu konuda değil, hemen her konuda titiz davranırdı." cümlesinden aşağıdakilerden hangisi çıkarılır?',
        {
            'A': 'Titizliği pek çok alanı kapsar.',
            'B': 'Kişi bu konuda özensizdir.',
            'C': 'Kişi titiz biri değildir.',
            'D': 'Kişi tek bir konuda titizdir.',
            'E': 'Kişi titizliği sonradan kazanmıştır.',
        },
        'A',
        '"Yalnız bu konuda değil, hemen her konuda" ifadesi, kişinin titizliğinin tek bir alanla sınırlı olmayıp geniş bir alanı kapsadığını anlatır. Doğru çıkarım bu yaygınlığı belirten seçenektir.',
    ),
    # düzey 2
    '0059': patch(
        '"Ummadığın taş baş yarar." atasözünün anlamı aşağıdakilerden hangisidir?',
        {
            'A': 'İnsan kötü günde dostunu tanır.',
            'B': 'Herkes ektiğini biçer.',
            'C': 'Güçlü olan kazanır.',
            'D': 'Zamanında yapılmayan iş sonradan yapılmaz.',
            'E': 'Önemsiz sanılan şey beklenmedik zarar verebilir.',
        },
        'E',
        'Bu atasözü, hiç önemsenmeyen, beklenmeyen bir şeyin insana büyük zarar verebileceğini anlatır. Doğru yorum, önemsiz sanılanın beklenmedik zarar verebileceğini belirten seçenektir.',
    ),
    # düzey 2
    '0060': patch(
        '"Ne yaparsan yap, onu bu kararından döndüremezsin." cümlesinde aşağıdakilerden hangisi vurgulanır?',
        {
            'A': 'Kararın yanlış olduğu',
            'B': 'Kişinin kararsız olduğu',
            'C': 'Kişinin başkalarınca kolayca ikna edilebildiği',
            'D': 'Kararın henüz verilmediği',
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
    print(f"1 paket / {len(PATCHES)} soru ('Sozcukte ve Cumlede Anlam' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
