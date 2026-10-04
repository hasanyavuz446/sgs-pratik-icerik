#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Türkçe — Dil Bilgisi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gerçek SGS 1-7 profiline göre baştan yazıldı: öge dizilişi özdeşliği (devrik dahil), cümlede öge bulma, dizede/cümlede sözcük türü ('hangisine yer verilmemiştir'), fiilimsi sayma ve ayırma, parça içinde ses olayları, yapı (kök-ek), cümle türleri, çatı, tamlamalar, ek fiil ve kip, bağlaç/edat. Olumsuz kök %2 -> %30. Eski paketteki şık içi açıklayıcı parantezler (cevabı ele veren) kaldırıldı.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: SGS Türkçe 2021-2026 kitapçıkları — biçim kalibrasyonu; TDK dil bilgisi
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/turkce/dil_bilgisi.json"
STYLE_REF = 'SGS Türkçe (gerçek sınav 1-7 profili)'
ONEK = "turkce-dilbilgisi-gen-"


def patch(stem, options, answer, solution, ref='Türkçe - dil bilgisi'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        'Aşağıdaki cümlelerin hangisinde yer-yön zarfı vardır?',
        {
            'A': 'Sınav günü sabahleyin erkenden kalkıp kahvaltımızı aceleyle yaptık.',
            'B': 'Zil çalar çalmaz çocuklar koşarak merdivenlerden yukarı çıktı.',
            'C': 'Sınavda çıkan bu zor soruyu günlerce çok merak ettim.',
            'D': 'Elektrikler kesilince asansörü bırakıp merdivenlerle aşağıya indik.',
            'E': 'Kütüphanede yukarıdaki rafta duran dosyayı bana uzatır mısın?',
        },
        'B',
        "Ek almadan fiili yön bakımından niteleyen 'yukarı' yer-yön zarfıdır. 'Yukarıdaki' sıfat, 'aşağıya' ek aldığı için addır (dolaylı tümleç); 'sabahleyin, erkenden' zaman, 'çok' miktar zarfıdır.",
    ),
    # düzey 2
    '0002': patch(
        'Aşağıdaki cümlelerin hangisinde ünsüz yumuşaması yoktur?',
        {
            'A': 'Eski dostunu yıllardır görmemişti, bu buluşma onu çok sevindirdi.',
            'B': 'Yorulunca yaşlı ağacın serin gölgesinde biraz dinlendik.',
            'C': 'Annesi, her sabah çocuğu okula bırakıp işe gidiyordu.',
            'D': 'Annem, yeni aldığımız perdelerin renginden pek hoşlanmadı.',
            'E': 'Okuldan çıkarken matematik kitabını sırada unutmuş.',
        },
        'A',
        "'Ağaç → ağacın, kitap → kitabını, renk → renginden, al-dık → aldığımız, çocuk → çocuğu, git → gidiyordu' ünsüz yumuşamasıdır. 'Dostunu, görmemişti, buluşma, sevindirdi' sözcüklerinde yumuşama yoktur.",
    ),
    # düzey 2
    '0003': patch(
        'Aşağıdaki cümlelerin hangisinde birleşik fiil yoktur?',
        {
            'A': 'Bu konuyu yarınki toplantıda bütün yönleriyle yeniden ele alacağız.',
            'B': 'Aylarca hazırlandığı sınavı kazandığını duyunca hepimiz çok sevindik.',
            'C': 'Öğrenci, dönem boyunca hazırladığı ödevini zamanında teslim etti.',
            'D': 'Komşumuz, eşyalarımızı taşırken bize bütün gün yardım etti.',
            'E': 'Bahçede koşarken ayağı taşa takılan çocuk birden düşüverdi.',
        },
        'B',
        "'Ele almak' deyimsel, 'teslim etmek' ve 'yardım etmek' yardımcı eylemli, 'düşüvermek' kurallı birleşik fiildir. Sınavı kazanmanın sevincini anlatan cümlede birleşik fiil yoktur.",
    ),
    # düzey 2
    '0004': patch(
        'Aşağıdaki cümlelerin hangisinde sıfat tamlaması yoktur?',
        {
            'A': 'Bazı öğrenciler, yağmur yüzünden bugün derse gelmedi.',
            'B': 'Şu masayı biraz kenara çek, buraya halıyı sereceğiz.',
            'C': 'Rüzgâr sabaha kadar esince bahçenin kapısı açık kalmış.',
            'D': 'Mahallemizdeki eski evler kentsel dönüşümle tek tek yıkılıyor.',
            'E': 'Tatile çıkmadan önce kitapçıdan üç kitap aldım.',
        },
        'C',
        "'Eski evler, üç kitap, şu masa, bazı öğrenciler' sıfat tamlamasıdır. 'Bahçenin kapısı' belirtili isim tamlamasıdır; 'açık' ise yüklemin parçasıdır.",
    ),
    # düzey 3
    '0005': patch(
        'Aşağıdaki cümlelerin hangisinde zincirleme isim tamlaması vardır?',
        {
            'A': 'Bu güzel elbiseyi annem, bayram için gece geç saatlere kadar dikti.',
            'B': 'Okul müdürü, teneffüste kavga eden öğrencileri odasına çağırdı.',
            'C': 'Dün geceki fırtınada evimizin bahçe kapısı yerinden kırılmış.',
            'D': 'Kış günleri bu küçük kasabada akşamlar çok uzun geçer.',
            'E': 'Komşunun sarı kedisi üç gündür ortalarda görünmüyor.',
        },
        'C',
        "'Evimizin bahçe kapısı' sözünde tamlanan ('bahçe kapısı') kendisi bir isim tamlamasıdır; zincirleme isim tamlamasıdır.",
    ),
    # düzey 2
    '0006': patch(
        "Aşağıdaki cümlelerin hangisinde 'ki' bağlaç olarak kullanılmıştır?",
        {
            'A': 'Yarınki proje toplantısına bizim bölümden kimler katılacak?',
            'B': 'Senin bisikletin güzelmiş ama benimki biraz daha yeni.',
            'C': 'Masadaki kitap senin mi, yoksa kütüphaneden mi aldın?',
            'D': 'Sabahki otobüsü kaçırınca işe yarım saat geç kaldım.',
            'E': 'Gece boyunca öyle yorulmuştu ki eve gelir gelmez uyudu.',
        },
        'E',
        "'Öyle ... ki' yapısındaki 'ki' iki cümleyi sonuç ilişkisiyle bağlayan bağlaçtır ve ayrı yazılır. Diğerlerinde '-ki' ilgi ekidir.",
    ),
    # düzey 2
    '0007': patch(
        'Aşağıdaki cümlelerin hangisinde zarf-fiil yoktur?',
        {
            'A': 'Yaz tatilinde okunacak kitapları öğretmenimizle birlikte seçtik.',
            'B': 'Yaşlı adam, sevdiği bir şarkıyı söyleyerek parkta yürüyordu.',
            'C': 'Yemeğini aceleyle yiyip hemen otobüs durağına koştu.',
            'D': 'Toplantı salonunun kapısını çalmadan içeri girdi.',
            'E': 'Sınav günü yaklaştıkça öğrencilerin heyecanı arttı.',
        },
        'A',
        "'Çalmadan, yiyip, yaklaştıkça, söyleyerek' zarf-fiildir. 'Okunacak' ise sıfat-fiildir; bu cümlede zarf-fiil yoktur.",
    ),
    # düzey 3
    '0008': patch(
        'Ah, bu yollar ne kadar uzun\nSeni bekledim sabaha kadar\nGönlüm yorgun, umutlu\n\nYukarıdaki dizelerde aşağıdaki sözcük türlerinden hangisine yer verilmemiştir?',
        {
            'A': 'Ünlem',
            'B': 'Zarf',
            'C': 'Zamir',
            'D': 'Bağlaç',
            'E': 'Edat',
        },
        'D',
        "'Ah' ünlem, 'seni' zamir, 'sabaha kadar' öbeğindeki 'kadar' edat, 'ne kadar' (uzun) zarftır. Dizelerde bağlaç yoktur.",
    ),
    # düzey 2
    '0009': patch(
        'Kitapları rafa dizerken **eski bir fotoğraf** buldum.\n\nBu cümlede kalın yazılmış söz cümlenin hangi ögesidir?',
        {
            'A': 'Belirtili nesne',
            'B': 'Özne',
            'C': 'Dolaylı tümleç',
            'D': 'Zarf tümleci',
            'E': 'Belirtisiz nesne',
        },
        'E',
        "'Ne buldum?' sorusuna belirtme durumu eki almadan cevap veren 'eski bir fotoğraf' belirtisiz nesnedir.",
    ),
    # düzey 2
    '0010': patch(
        'Aşağıdakilerin hangisinde ünsüz benzeşmesi yoktur?',
        {
            'A': 'sokakta',
            'B': 'yurttaş',
            'C': 'kitapçı',
            'D': 'evde',
            'E': 'seçtik',
        },
        'D',
        "Sert ünsüzle biten sözcüklere gelen eklerin ilk ünsüzü sertleşir: kitap-çı, yurt-taş, seç-tik, sokak-ta. 'Evde' sözcüğünde sertleşme yoktur.",
    ),
    # düzey 2
    '0011': patch(
        "'Haberi duyunca çok sevinmiş.' cümlesindeki yüklemin kipi aşağıdakilerden hangisidir?",
        {
            'A': 'Gelecek zaman',
            'B': 'Duyulan geçmiş zaman',
            'C': 'Görülen geçmiş zaman',
            'D': 'Şimdiki zaman',
            'E': 'Geniş zaman',
        },
        'B',
        "'-miş' eki eylemin başkasından duyulduğunu ya da sonradan fark edildiğini bildirir; duyulan (öğrenilen) geçmiş zamandır.",
    ),
    # düzey 2
    '0012': patch(
        'Aşağıdaki dizelerin hangisinde ünlü daralmasına uğramış bir sözcük vardır?',
        {
            'A': 'Gönlüm hep seni arar',
            'B': 'Sabah olunca güneş doğar',
            'C': 'Yine bir rüzgâr esiyor dağlardan',
            'D': 'Kuşlar uçar mavi göklerde',
            'E': 'Gözlerim yolunu bekliyor her gün',
        },
        'E',
        "'Bekle-' fiiline '-yor' eki gelince sondaki 'e' ünlüsü daralır: bekliyor. 'Es-' ünsüzle bittiği için 'esiyor'da daralma yoktur.",
    ),
    # düzey 2
    '0013': patch(
        'Aşağıdaki cümlelerin hangisinde isim-fiil vardır?',
        {
            'A': 'Durağa koşarak son otobüse son anda yetişti.',
            'B': 'Akşam gelen misafirleri annemle birlikte kapıda karşıladık.',
            'C': 'Her sabah sahilde yürümek ona iyi geliyordu.',
            'D': 'Gece yanan ışıkları tek tek söndürüp odasına çekildi.',
            'E': 'Ders bitince bütün öğrenciler bahçeye çıktı.',
        },
        'C',
        "'Yürümek' -mek ekiyle kurulmuş isim-fiildir. 'Koşarak, bitince' zarf-fiil; 'yanan, gelen' sıfat-fiildir.",
    ),
    # düzey 2
    '0014': patch(
        'Aşağıdaki cümlelerden hangisi yapı bakımından birleşik cümledir?',
        {
            'A': 'Hava yarın da güzel olursa ailece pikniğe gideriz.',
            'B': 'Kapıyı yavaşça açtı ve içeri sessizce girdi.',
            'C': 'Çocuklar akşama kadar bahçede top oynuyordu.',
            'D': 'Hem bir fabrikada çalışıyor hem akşamları okula gidiyordu.',
            'E': 'Akşam oldu, sokaklar yavaş yavaş boşaldı.',
        },
        'A',
        "'Hava güzel olursa' koşul bildiren yan cümledir; temel cümleye bağlıdır ve cümle şartlı birleşik cümledir. Diğerleri sıralı, bağlı ya da basit cümlelerdir.",
    ),
    # düzey 2
    '0015': patch(
        'Aşağıdaki cümlelerden hangisi yükleminin türü bakımından ötekilerden farklıdır?',
        {
            'A': 'Annemin elindeki kitap, dedemden kalan çok eski bir baskıydı.',
            'B': 'Babam, işe yetişmek için her sabah erkenden kalkar.',
            'C': 'Kardeşim, kalabalık sınıfının en çalışkan öğrencisidir.',
            'D': 'Konferansın yapıldığı salon oldukça kalabalıktı.',
            'E': 'Bu yıl yağmurlar düzenli yağdığı için ürün çok bereketliydi.',
        },
        'B',
        "'Kalkar' çekimli bir fiildir; cümle fiil cümlesidir. Diğer cümlelerin yüklemleri ek fiil almış isim soylu sözcüklerdir (isim cümlesi).",
    ),
    # düzey 3
    '0016': patch(
        'Aşağıdaki cümlelerin hangisinde isimden fiil yapan bir ek almış sözcük vardır?',
        {
            'A': 'Sevgi, insanlar arasındaki her şeyin ilacıdır.',
            'B': 'Gözlükçü, babamın kırık gözlüğüne yeni camlar taktı.',
            'C': 'Yazar, imza gününe gelen okurlarına teşekkür etti.',
            'D': 'Gündüz çok sıcak olan hava akşama doğru serinledi.',
            'E': 'Çocuklar okul bahçesinde neşeyle koşuşuyor.',
        },
        'D',
        "'Serin' isim kök + '-le' isimden fiil yapım eki → serinle-. 'Sevgi, yazar, okur' fiilden isim; 'gözlükçü' isimden isim; 'koşuş-' fiilden fiil yapım eki almıştır.",
    ),
    # düzey 2
    '0017': patch(
        'Aşağıdaki cümlelerin hangisinde özne, eylemi yapan değil eylemden etkilenendir?',
        {
            'A': 'Çocuklar okul çıkışında bahçede saatlerce top oynuyor.',
            'B': 'Annem, misafirler için bize lezzetli bir kek yaptı.',
            'C': 'Kuşlar bahar sabahlarında penceremizin önünde öter.',
            'D': 'Şehrin iki yakasını birleştiren yeni yol yarın açılacak.',
            'E': 'Öğretmen, ödev sorularını tahtaya tek tek yazdı.',
        },
        'D',
        "Edilgen çatılı 'açılacak' yükleminde yolu açan belli değildir; 'yeni yol' eylemden etkilenen sözde öznedir. Diğer cümlelerde özne eylemi yapan gerçek öznedir.",
    ),
    # düzey 2
    '0018': patch(
        'Aşağıdaki cümlelerin hangisi devrik bir cümledir?',
        {
            'A': 'Yarın sabah erkenden yola çıkacağız.',
            'B': 'Kardeşim her gün parkta yürüyüş yapar.',
            'C': 'Unutmadım o günü hâlâ.',
            'D': 'Bu kitabı herkese tavsiye ederim.',
            'E': 'O günü hâlâ unutmadım.',
        },
        'C',
        "Yüklemi sonda olmayan cümle devrik cümledir. 'Unutmadım o günü hâlâ.' cümlesinde yüklem başta yer alır.",
    ),
    # düzey 2
    '0019': patch(
        'Yıllardır aynı mahallede oturan yaşlı adam, sonunda evini satmaya karar verdi.\n\nBu cümlenin öznesi aşağıdakilerden hangisidir?',
        {
            'A': 'sonunda evini',
            'B': 'evini satmaya',
            'C': 'yaşlı adam',
            'D': 'Yıllardır aynı mahallede oturan yaşlı adam',
            'E': 'aynı mahallede oturan',
        },
        'D',
        "Yükleme 'Karar veren kim?' sorusu sorulduğunda alınan cevap, sıfat-fiil öbeğiyle birlikte 'Yıllardır aynı mahallede oturan yaşlı adam'dır. Öge, öbeğin bütünüdür.",
    ),
    # düzey 3
    '0020': patch(
        'Sabah erkenden kalkıp hazırlanan çocuklar, okula gitmek için sabırsızlanıyordu.\n\nBu cümlede kaç fiilimsi vardır?',
        {
            'A': 'Üç',
            'B': 'Dört',
            'C': 'Bir',
            'D': 'İki',
            'E': 'Beş',
        },
        'A',
        "'Kalkıp' zarf-fiil, 'hazırlanan' sıfat-fiil, 'gitmek' isim-fiildir; 'sabırsızlanıyordu' çekimli fiildir. Cümlede üç fiilimsi vardır.",
    ),
    # düzey 2
    '0021': patch(
        'Aşağıdaki sözcüklerin hangisi büyük ünlü uyumuna uymaz?',
        {
            'A': 'kitap',
            'B': 'masa',
            'C': 'dağlar',
            'D': 'çocuk',
            'E': 'evler',
        },
        'A',
        "Büyük ünlü uyumunda bir sözcüğün ünlüleri ya hep kalın ya hep ince olur. 'Kitap' sözcüğünde ince 'i' ile kalın 'a' bir aradadır; uyuma uymaz.",
    ),
    # düzey 2
    '0022': patch(
        'Aşağıdaki cümlelerin hangisinde yüklem işteş çatılıdır?',
        {
            'A': 'Çocuklar okuldan sonra bahçede saklambaç oynadı.',
            'B': 'Seyirciler, maç bitince sevinçle sahaya koşuştu.',
            'C': 'Kapı, sert esen rüzgârın etkisiyle birden açıldı.',
            'D': 'Annem, düğüne gitmeden önce saçlarını özenle taradı.',
            'E': 'Öğretmen, ödevleri sınıf başkanına kontrol ettirdi.',
        },
        'B',
        "'Koşuşmak' eylemin birlikte, topluca yapıldığını bildirir; işteş çatıdır. Diğerleri etken, edilgen ve ettirgen çatılıdır.",
    ),
    # düzey 2
    '0023': patch(
        'Aşağıdaki cümlelerin hangisinde belirtili isim tamlaması vardır?',
        {
            'A': 'Rüzgârda sallanan bahçe kapısı bütün gece açık kalmış.',
            'B': 'Sonbaharda dökülen sarı yapraklar yolları kapladı.',
            'C': 'Eski evin kapısının kolu yerinden çıkmıştı.',
            'D': 'Yağmurdan sonra paslanan demir kapı gıcırdamaya başladı.',
            'E': 'Okul servisi bu sabah trafik yüzünden geç kaldı.',
        },
        'C',
        "Tamlayanı ilgi eki (-ın), tamlananı iyelik eki alan 'kapının kolu' belirtili isim tamlamasıdır. 'Bahçe kapısı, okul servisi' belirtisiz; 'sarı yapraklar' sıfat; 'demir kapı' takısız tamlamadır.",
    ),
    # düzey 2
    '0024': patch(
        "Aşağıdaki cümlelerin hangisinde 'gibi' sözcüğü benzerlik anlamında kullanılmamıştır?",
        {
            'A': 'Kızı da tıpkı annesi gibi yavaş ve tatlı konuşuyordu.',
            'B': 'Bütün gün koşturan bebek akşam bir melek gibi uyuyordu.',
            'C': 'Eve girdiği gibi doğruca mutfağa koştu.',
            'D': 'Kardeşim, ağabeyi gibi doktor olmak istiyor.',
            'E': 'Unutulan ekmek iki günde taş gibi sertleşmişti.',
        },
        'C',
        "'Girdiği gibi' sözünde 'gibi', 'girer girmez' anlamında zaman bildirir. Diğerlerinde benzerlik anlamı vardır.",
    ),
    # düzey 3
    '0025': patch(
        "'Eski mahallenin dar sokakları' söz öbeğiyle ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Tamlayanı ve tamlananı sıfat tamlaması olan belirtili isim tamlamasıdır.',
            'B': 'Tamlananı belirtisiz isim tamlaması olan zincirleme isim tamlamasıdır.',
            'C': 'Tamlayanı ve tamlananı sıfat tamlaması olan, ilgi eki almamış belirtisiz isim tamlamasıdır.',
            'D': 'İki ayrı sıfat tamlamasından oluşan zincirleme bir sıfat tamlamasıdır.',
            'E': 'Tamlayanı ilgi eki almamış takısız isim tamlamasıdır.',
        },
        'A',
        "'Eski mahalle' ilgi eki (-nin), 'dar sokak' iyelik eki (-ları) almıştır; ikisi de sıfat tamlaması olan bu öbek belirtili isim tamlamasıdır.",
    ),
    # düzey 3
    '0026': patch(
        'Bu hafta sonu kardeşimle sinemaya gideceğiz.\n\nAşağıdaki cümlelerden hangisi öge dizilişi bakımından yukarıdaki cümleyle özdeştir?',
        {
            'A': 'Akşam olunca herkes evine döndü.',
            'B': 'Sinemaya bu hafta sonu kardeşimle gideceğiz.',
            'C': 'Yarın annemle pazara gideceğim.',
            'D': 'Annem her gün pazara gider.',
            'E': 'Geçen yıl biz de oraya gitmiştik.',
        },
        'C',
        "Verilen cümlede zarf tümleci (bu hafta sonu) - zarf tümleci (kardeşimle) - dolaylı tümleç (sinemaya) - yüklem sıralanmıştır; özne gizlidir. 'Yarın - annemle - pazara - gideceğim' aynı dizilişe sahiptir.",
    ),
    # düzey 3
    '0027': patch(
        'Toplantı saati bütün çalışanlara e-postayla bildirildi.\n\nBu cümlenin yüklemiyle ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşteş çatılıdır; eylem karşılıklı yapılmıştır.',
            'B': 'Dönüşlü çatılıdır; eylemi yapan ve etkilenen aynıdır.',
            'C': 'Ettirgen çatılıdır; eylem başkasına yaptırılmıştır.',
            'D': 'Edilgen çatılıdır; cümlede sözde özne vardır.',
            'E': 'Etken çatılıdır; cümlede gizli özne vardır.',
        },
        'D',
        "'Bildir-il-' edilgenlik eki almıştır; bildiren belli değildir. 'Toplantı saati' eylemden etkilenen sözde öznedir.",
    ),
    # düzey 2
    '0028': patch(
        'Aşağıdaki sözcüklerin hangisinde ünsüz türemesi vardır?',
        {
            'A': 'gidiyor',
            'B': 'kitabı',
            'C': 'burnu',
            'D': 'başlıyor',
            'E': 'hakkı',
        },
        'E',
        "'Hak' sözcüğü ünlüyle başlayan ek alınca sondaki ünsüz ikizleşir: hak + ı → hakkı (ünsüz türemesi). 'Kitabı, gidiyor' yumuşama; 'burnu' ünlü düşmesi; 'başlıyor' ünlü daralmasıdır.",
    ),
    # düzey 2
    '0029': patch(
        'Aşağıdaki cümlelerden hangisi yalnızca özne ve yüklemden oluşmuştur?',
        {
            'A': 'Kuşlar sabah erkenden uçuştu.',
            'B': 'Çocuklar bahçede oynuyor.',
            'C': 'Bütün kuşlar uçuştu.',
            'D': 'Yolcular yavaşça indi.',
            'E': 'Annem bize kek yaptı.',
        },
        'C',
        "'Bütün kuşlar' sıfatla genişlemiş tek bir öznedir; cümlede başka öge yoktur. Diğer cümlelerde zarf tümleci, dolaylı tümleç ya da nesne bulunur.",
    ),
    # düzey 3
    '0030': patch(
        'Yıllar sonra gördüğü arkadaşına sarılınca gözleri doldu.\n\nBu cümlede aşağıdaki fiilimsi türlerinden hangileri vardır?',
        {
            'A': 'İsim-fiil ve sıfat-fiil',
            'B': 'Sıfat-fiil ve zarf-fiil',
            'C': 'İsim-fiil ve zarf-fiil',
            'D': 'Sıfat-fiil, isim-fiil ve zarf-fiil',
            'E': 'Yalnız zarf-fiil',
        },
        'B',
        "'Gördüğü' (arkadaşını niteleyen) sıfat-fiil, 'sarılınca' zaman bildiren zarf-fiildir. Cümlede isim-fiil yoktur.",
    ),
    # düzey 2
    '0031': patch(
        'Aşağıdaki sözcüklerin hangisi yapı bakımından ötekilerden farklıdır?',
        {
            'A': 'kitaplık',
            'B': 'gözlük',
            'C': 'hanımeli',
            'D': 'yolcu',
            'E': 'denizci',
        },
        'C',
        "'Gözlük, kitaplık, yolcu, denizci' yapım eki almış türemiş sözcüklerdir. 'Hanımeli' iki sözcüğün birleşmesiyle oluşmuş birleşik sözcüktür.",
    ),
    # düzey 2
    '0032': patch(
        'Aşağıdaki cümlelerin hangisinde edat kullanılmamıştır?',
        {
            'A': 'Senin için elimden gelen her şeyi yaparım, merak etme.',
            'B': 'Gece boyunca yağan yağmurdan dolayı maç ertelendi.',
            'C': 'Bu konuyu yarın sabah sınıfta arkadaşlarınla konuşursun.',
            'D': 'Akşama kadar onu durakta sabırla bekledik.',
            'E': 'Sen de tıpkı kardeşim gibi konuşuyorsun.',
        },
        'C',
        "'İçin, kadar, gibi, dolayı' edattır. 'Bu konuyu yarın sabah sınıfta arkadaşlarınla konuşursun.' cümlesinde edat yoktur; '-la' bir ektir.",
    ),
    # düzey 3
    '0033': patch(
        'Aşağıdaki cümlelerin hangisinde ek fiil, isim soylu bir sözcüğü yüklem yapmıştır?',
        {
            'A': 'Sabahki toplantıya müdür de geç kalacakmış.',
            'B': 'Dedem eskiden her gece yatmadan önce kitap okurdu.',
            'C': 'Sen geldiğinde ödevini bitirmiş miydi?',
            'D': 'Sabahtan beri durmadan yağmur yağıyordu.',
            'E': 'Evin en güzel ve en aydınlık odası burasıydı.',
        },
        'E',
        "'Burası' zamirine gelen '-ydı' ek fiili isim soylu sözcüğü yüklem yapmıştır. Diğerlerinde ek fiil, çekimli fiile gelerek birleşik zaman kurmuştur.",
    ),
    # düzey 3
    '0034': patch(
        'Kışın köye gittiğimizde dedemin evinin kapısını çaldık. Ağzımızdan çıkan buhar havada asılı kalıyordu. Kapıyı açan babaannem bizi görünce sevincinden ağlıyordu.\n\nBu parçada aşağıdaki ses olaylarından hangisinin örneği yoktur?',
        {
            'A': 'Ünlü daralması',
            'B': 'Ünsüz yumuşaması',
            'C': 'Ünlü düşmesi',
            'D': 'Ünsüz türemesi',
            'E': 'Ünsüz benzeşmesi',
        },
        'D',
        "'Ağzımızdan' (ağız) ünlü düşmesi; 'gittiğimizde, sevincinden' ünsüz yumuşaması; 'ağlıyordu' (ağla-yor) ünlü daralması; 'gittiğimizde' (-dik → -tik) ünsüz benzeşmesidir. Ünsüz türemesine (hak → hakkı gibi) örnek yoktur.",
    ),
    # düzey 3
    '0035': patch(
        'Gördüm onu dün akşam pazarda.\n\nAşağıdaki cümlelerden hangisi öge dizilişi bakımından yukarıdaki cümleyle özdeştir?',
        {
            'A': 'Onu pazarda dün akşam gördüm.',
            'B': 'Gördüm dün akşam onu pazarda.',
            'C': 'Seni saatlerce kapıda bekledik.',
            'D': 'Okudum kitabı bir solukta.',
            'E': 'Bekledik seni saatlerce kapıda.',
        },
        'E',
        "Devrik cümlenin dizilişi yüklem - belirtili nesne - zarf tümleci - dolaylı tümleçtir. 'Bekledik - seni - saatlerce - kapıda' aynı sıradadır.",
    ),
    # düzey 2
    '0036': patch(
        'Toplantıdan sonra müdür, yeni çalışanları tek tek karşıladı.\n\nBu cümlede aşağıdaki ögelerden hangisi yoktur?',
        {
            'A': 'Zarf tümleci',
            'B': 'Dolaylı tümleç',
            'C': 'Özne',
            'D': 'Belirtili nesne',
            'E': 'Yüklem',
        },
        'B',
        "Cümlenin ögeleri: 'Toplantıdan sonra' (edat öbeği; zarf tümleci), 'müdür' (özne), 'yeni çalışanları' (belirtili nesne), 'tek tek' (zarf tümleci), 'karşıladı' (yüklem). Dolaylı tümleç yoktur.",
    ),
    # düzey 3
    '0037': patch(
        'Komşumuzun oğlu geçen yıl üniversiteden mezun oldu.\n\nAşağıdaki cümlelerden hangisi öge dizilişi bakımından yukarıdaki cümleyle özdeştir?',
        {
            'A': 'Bu sabah yeni öğretmenimiz sınıfa geldi.',
            'B': 'Çocuklar bahçede akşama kadar oynadı.',
            'C': 'Yeni öğretmenimiz bu sabah sınıfa geldi.',
            'D': 'Annem pazardan taze sebzeler aldı.',
            'E': 'Geçen yıl kardeşim üniversiteyi kazandı.',
        },
        'C',
        "Verilen cümle özne (komşumuzun oğlu) - zarf tümleci (geçen yıl) - dolaylı tümleç (üniversiteden) - yüklem (mezun oldu) sırasındadır. Aynı dizilişte olan cümle 'yeni öğretmenimiz - bu sabah - sınıfa - geldi'dir.",
    ),
    # düzey 2
    '0038': patch(
        'Aşağıdaki cümlelerin hangisinde zamir yoktur?',
        {
            'A': 'Yoğun haftanın sonunda kendini çok yorgun hissediyordu.',
            'B': 'Bunu sakın kimseye söyleme, aramızda kalsın.',
            'C': 'Davetlilerin kimi geldi, kimi son anda gelmedi.',
            'D': 'Uzun yolculuktan sonra yorgun yolcular yavaşça trenden indi.',
            'E': 'Arkadaşlarının hepsi sınıfta seni sabırla bekliyordu.',
        },
        'D',
        "'Bunu, kimseye, hepsi, seni, kendini, kimi' zamirdir. 'Uzun yolculuktan sonra yorgun yolcular yavaşça trenden indi.' cümlesinde zamir yoktur.",
    ),
    # düzey 2
    '0039': patch(
        "Aşağıdaki cümlelerin hangisinde 'de' bağlaç olarak kullanılmıştır?",
        {
            'A': 'Bu akşam sen de bize gel, birlikte yemek yiyelim.',
            'B': 'Sınav başlayınca sınıfta herkes sessizce bekledi.',
            'C': 'Kapıyı çaldık ama evde kimse yoktu.',
            'D': 'Dünkü toplantıda önemli kararlar alındı.',
            'E': 'Kitabını okuldaki masada unutmuş.',
        },
        'A',
        "'Sen de' sözündeki 'de', 'dahi' anlamında bağlaçtır ve ayrı yazılır. Diğerlerinde '-da/-de' bulunma durumu ekidir.",
    ),
    # düzey 3
    '0040': patch(
        'Aşağıdaki cümlelerin hangisinde zarf, başka bir zarfı nitelemiştir?',
        {
            'A': 'Konserde genç sanatçı çok güzel bir şarkı söyledi.',
            'B': 'Taşındığımız evin salonu oldukça büyük ve aydınlık.',
            'C': 'Bitiş çizgisine yaklaşırken yarışmacı çok hızlı koşuyordu.',
            'D': 'Haftaya kardeşimle birlikte köye gideceğiz.',
            'E': 'Kırmızı, hızlı bir araba önümüzden geçip gitti.',
        },
        'C',
        "'Çok', 'koşuyordu' eylemini niteleyen 'hızlı' zarfının derecesini belirtir; zarf zarfı nitelemiştir. 'Çok güzel' ve 'oldukça büyük'te zarf sıfatı niteler.",
    ),
    # düzey 3
    '0041': patch(
        'Aşağıdaki cümlelerin hangisi anlamca olumlu, yapıca olumsuzdur?',
        {
            'A': 'Sınav sonuçları bu hafta da açıklanmadı.',
            'B': 'Yarın hasta olduğum için okula gitmeyeceğim.',
            'C': 'Toplantıya davet edilenlerden kimse katılmadı.',
            'D': 'Mahallede bu filmi izlemeyen kalmadı.',
            'E': 'Önerdiğin kitabı henüz okumadım.',
        },
        'D',
        "'Kalmadı' yüklemi olumsuz eklidir ama cümle 'herkes izledi' anlamı taşır; yapıca olumsuz, anlamca olumludur. Diğer cümleler hem yapı hem anlam bakımından olumsuzdur.",
    ),
    # düzey 2
    '0042': patch(
        'Aşağıdaki cümlelerin hangisinde dolaylı tümleç yoktur?',
        {
            'A': 'Babam sabahları erkenden işe gider.',
            'B': 'Kitabı okuduktan sonra masanın üstüne bıraktı.',
            'C': 'Bu kötü haberi uzun süre herkesten sakladı.',
            'D': 'Sınav haftası boyunca gece gündüz durmadan çalıştı.',
            'E': 'Yarın akşam yemekten sonra size uğrarız.',
        },
        'D',
        "'İşe, masanın üstüne, size, herkesten' sözleri yönelme ve ayrılma durumunda dolaylı tümleçtir. 'Sınav haftası boyunca gece gündüz durmadan çalıştı.' cümlesinde yalnız zarf tümleçleri ve yüklem bulunur.",
    ),
    # düzey 2
    '0043': patch(
        'Aşağıdaki cümlelerin hangisinde ünlü düşmesine uğramış bir sözcük vardır?',
        {
            'A': 'Yarın erkenden yola çıkacağız, hazırlıklarını bitir.',
            'B': 'Sınav başlayınca sınıfta herkes sessizce bekliyordu.',
            'C': 'Kitapları renklerine göre rafa özenle dizdi.',
            'D': 'Bahçedeki elma ağaçları bu yıl erken çiçek açtı.',
            'E': 'Komşumuzun oğlu bu yıl tıp fakültesine başladı.',
        },
        'E',
        "'Oğul' sözcüğü ünlüyle başlayan ek alınca ikinci hecedeki dar ünlüyü yitirir: oğul + u → oğlu. Diğer cümlelerde ünlü düşmesi yoktur.",
    ),
    # düzey 3
    '0044': patch(
        'Kısa bir süre sonra yorgun yolcular otobüsten indi.\n\nAşağıdaki cümlelerden hangisi öge dizilişi bakımından yukarıdaki cümleyle özdeştir?',
        {
            'A': 'Öğrenciler ders bitince kantine koştu.',
            'B': 'Akşamüstü küçük çocuklar parktan döndü.',
            'C': 'Yolcular sabah erkenden istasyona geldi.',
            'D': 'Yarın sabah toplantıyı müdür açacak.',
            'E': 'Uzun yıllar boyunca o evde yalnız yaşadı.',
        },
        'B',
        "Verilen cümle zarf tümleci (kısa bir süre sonra) - özne (yorgun yolcular) - dolaylı tümleç (otobüsten) - yüklem sırasındadır. 'Akşamüstü - küçük çocuklar - parktan - döndü' aynı dizilişe sahiptir.",
    ),
    # düzey 2
    '0045': patch(
        'Aşağıdaki cümlelerden hangisi soru eki taşıdığı hâlde soru anlamı taşımaz?',
        {
            'A': 'Sınav zor muydu?',
            'B': 'Eve geldi mi hemen yatağa uzanır.',
            'C': 'Bu kitabı okudun mu?',
            'D': 'Kapıyı kim açtı?',
            'E': 'Yarın bize gelecek misin?',
        },
        'B',
        "'Geldi mi' sözündeki 'mi' burada soru değil koşul anlamı katar ('gelince, gelirse'). Diğer cümleler gerçek soru cümleleridir.",
    ),
    # düzey 2
    '0046': patch(
        "Aşağıdaki cümlelerin hangisinde 'bir' sözcüğü belgisiz sıfat olarak kullanılmıştır?",
        {
            'A': 'Bir gün mutlaka bu kasabaya yeniden döneceğim.',
            'B': 'Bu konuda hepimiz aynı fikirde biriz, tartışmaya gerek yok.',
            'C': 'Final maçını sadece bir puan farkla kaybettik.',
            'D': 'Sepette bir elma ile iki armut kalmıştı.',
            'E': 'Konserin sonunda bütün salon bir ağızdan şarkı söyledi.',
        },
        'A',
        "'Bir gün' sözünde 'bir' sayı bildirmez, günü belirsiz olarak niteler; belgisiz sıfattır. 'Bir elma', 'bir puan' sayı sıfatıdır; diğerlerinde sıfat görevi yoktur.",
    ),
    # düzey 3
    '0047': patch(
        'Dün akşam komşumuz bize bahçesinden topladığı elmaları getirdi.\n\nAşağıdaki cümlelerden hangisi öge dizilişi bakımından yukarıdaki cümleyle özdeştir?',
        {
            'A': 'Geçen hafta müdür bize projeyi anlattı.',
            'B': 'Öğrenciler sınavdan sonra bahçede uzun süre dinlendi.',
            'C': 'Sabah erkenden annem kahvaltıyı hazırladı.',
            'D': 'Kardeşim her sabah okula bisikletiyle gider.',
            'E': 'Bu kitabı bana yıllar önce dedem hediye etmişti.',
        },
        'A',
        "Verilen cümlenin dizilişi zarf tümleci (dün akşam) - özne (komşumuz) - dolaylı tümleç (bize) - belirtili nesne (bahçesinden topladığı elmaları) - yüklemdir. Aynı diziliş 'geçen hafta - müdür - bize - projeyi - anlattı' cümlesindedir.",
    ),
    # düzey 2
    '0048': patch(
        'Aşağıdaki cümlelerin hangisinde birleşik zamanlı bir fiil vardır?',
        {
            'A': 'Kalın romanı bir günde okuyup bitirdi.',
            'B': 'Biz istasyona geldiğimizde tren çoktan kalkmıştı.',
            'C': 'Yarın sabah erkenden köye doğru yola çıkacağız.',
            'D': 'Dedem her akşam yemekten sonra yürüyüşe çıkar.',
            'E': 'Kardeşim şu anda odasında ders çalışıyor.',
        },
        'B',
        "'Kalk-mış-tı' fiilinde duyulan geçmiş zamana ek fiilin hikâyesi eklenmiştir; birleşik zamanlı fiildir. Diğer yüklemler basit zamanlıdır.",
    ),
    # düzey 2
    '0049': patch(
        'Aşağıdaki cümlelerin hangisinin yüklemi geçişsizdir?',
        {
            'A': 'Annem, askerdeki ağabeyime uzun bir mektup yazdı.',
            'B': 'Bahçıvan, sabah erkenden bütün çiçekleri suladı.',
            'C': 'Öğrenciler sınavdaki bütün soruları zamanında çözdü.',
            'D': 'Kardeşim biriktirdiği parayla yeni bir bisiklet aldı.',
            'E': 'Misafirler, yağmur başlamadan erkenden gitti.',
        },
        'E',
        "'Gitmek' nesne almayan geçişsiz bir fiildir. 'Sulamak, almak, yazmak, çözmek' nesne alabilen geçişli fiillerdir.",
    ),
    # düzey 2
    '0050': patch(
        'Aşağıdaki cümlelerin hangisinde bağlaç, cümleler arasında neden-sonuç ilişkisi kurmuştur?',
        {
            'A': 'Aylarca çok çalıştı ama sınavı yine de kazanamadı.',
            'B': 'Hafta sonu pikniğe sen de bizimle gel.',
            'C': 'Ya bugün öğleden sonra gel ya yarın sabah.',
            'D': 'Hem bir iş yerinde çalışıyor hem de akşamları okula gidiyordu.',
            'E': 'Gün boyu çok yorulmuştu, dolayısıyla erkenden yattı.',
        },
        'E',
        "'Dolayısıyla', yorgunluğu erken yatmanın nedeni olarak bağlar. Diğer bağlaçlar birliktelik, seçenek, karşıtlık ve katılma ilişkisi kurar.",
    ),
    # düzey 2
    '0051': patch(
        "Aşağıdaki cümlelerin hangisinde 'ancak' sözcüğü bağlaç olarak kullanılmıştır?",
        {
            'A': 'Toplantıya gelmek istedim ancak son anda işim çıktı.',
            'B': 'Bu kadar kısa sürede ancak bu kadarını yapabilirim.',
            'C': 'Yolculardan ancak bir hafta sonra haber alabildik.',
            'D': 'Yoğun trafik yüzünden eve ancak gece yarısı varabildik.',
            'E': 'Bu karmaşık sorunu ancak sen çözebilirsin.',
        },
        'A',
        "'Fakat' anlamında iki cümleyi karşıtlık ilişkisiyle bağlayan 'ancak' bağlaçtır. Diğerlerinde 'yalnızca, güçlükle, ancak o zaman' anlamlarında zarftır.",
    ),
    # düzey 2
    '0052': patch(
        'Aşağıdaki sözcüklerin hangisinde yapım eki yoktur?',
        {
            'A': 'sevgi',
            'B': 'kalemler',
            'C': 'yazar',
            'D': 'tuzlu',
            'E': 'gözlükçü',
        },
        'B',
        "'Kalemler' sözcüğündeki '-ler' çoğul (çekim) ekidir. 'Gözlükçü, yazar, sevgi, tuzlu' yapım eki almıştır.",
    ),
    # düzey 2
    '0053': patch(
        'Aşağıdaki cümlelerin hangisinde dönüşlülük zamiri vardır?',
        {
            'A': 'Toplantıda konuşulanları artık herkes biliyor.',
            'B': 'Yurt dışına giden oğlunu yıllardır çok özlemişti.',
            'C': 'Masadaki şu kalın kitabı bana uzatır mısın?',
            'D': 'Vitrindeki ayakkabılardan hangisini almak istersin?',
            'E': 'Yaptığı hatadan sonra kendini suçlu hissediyordu.',
        },
        'E',
        "'Kendi' sözcüğü ek alarak (kendini) dönüşlülük zamiri olur. 'Herkes' belgisiz, 'hangisini' soru zamiridir; 'şu kalın kitap' sözündeki 'şu' ise işaret sıfatıdır.",
    ),
    # düzey 2
    '0054': patch(
        'Aşağıdaki cümlelerin hangisinin yüklemi edilgen çatılıdır?',
        {
            'A': 'Annem bayram öncesi halıları bize yıkattı.',
            'B': 'Yeni kütüphane geçen ay törenle açıldı.',
            'C': 'Çocuk aynanın karşısında uzun uzun taranıyordu.',
            'D': 'İki eski dost yıllar sonra istasyonda kucaklaştı.',
            'E': 'Kardeşim akşam yemeğini çabucak bitirdi.',
        },
        'B',
        "'Açıldı' yükleminde eylemi yapan belli değildir; özne eylemden etkilenendir (edilgen). 'Taranıyordu' dönüşlü, 'kucaklaştı' işteş, 'yıkattı' ettirgen, 'bitirdi' etkendir.",
    ),
    # düzey 3
    '0055': patch(
        "'Çalışkanlık' sözcüğünün yapısıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İsim kök üzerine bir yapım eki almıştır.',
            'B': 'İsim kök üzerine iki yapım eki almıştır.',
            'C': 'Fiil kök üzerine bir yapım ve bir çekim eki almıştır.',
            'D': 'Fiil kök üzerine iki yapım eki almıştır.',
            'E': 'İki sözcüğün birleşmesiyle oluşmuş birleşik bir sözcüktür.',
        },
        'D',
        'çalış- (fiil kök) + -kan (fiilden isim yapım eki) + -lık (isimden isim yapım eki): fiil kök üzerine iki yapım eki gelmiştir.',
    ),
    # düzey 2
    '0056': patch(
        'Aşağıdaki cümlelerin hangisinde ikileme, karşıt anlamlı sözcüklerle oluşturulmuştur?',
        {
            'A': 'Bütün gün çalışan işçiler akşam yorgun argın eve döndü.',
            'B': 'Akşam serinliğinde yavaş yavaş eve doğru yürüdük.',
            'C': 'Bütün gün ufak tefek işlerle uğraştı.',
            'D': 'Köye giden eğri büğrü yolda araba sarsıldı.',
            'E': 'Toplantı başladığında aşağı yukarı herkes oradaydı.',
        },
        'E',
        "'Aşağı' ve 'yukarı' karşıt anlamlı sözcüklerdir. Diğerlerinde aynı sözcüğün tekrarı ya da biri anlamsız/yakın anlamlı sözcüklerle kurulmuş ikilemeler vardır.",
    ),
    # düzey 3
    '0057': patch(
        'Kardeşim, aldığı ilk maaşla annesine güzel bir hediye aldı.\n\nBu cümlenin ögeleri sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?',
        {
            'A': 'Özne - dolaylı tümleç - dolaylı tümleç - nesne - yüklem',
            'B': 'Özne - zarf tümleci - nesne - dolaylı tümleç - yüklem',
            'C': 'Özne - nesne - dolaylı tümleç - zarf tümleci - yüklem',
            'D': 'Özne - zarf tümleci - dolaylı tümleç - zarf tümleci - yüklem',
            'E': 'Özne - zarf tümleci - dolaylı tümleç - nesne - yüklem',
        },
        'E',
        "'Kardeşim' özne, 'aldığı ilk maaşla' araç bildiren zarf tümleci, 'annesine' dolaylı tümleç, 'güzel bir hediye' belirtisiz nesne, 'aldı' yüklemdir.",
    ),
    # düzey 2
    '0058': patch(
        'Aşağıdaki cümlelerin hangisinde kalın yazılmış sözcük zarf olarak kullanılmıştır?',
        {
            'A': 'Bu **güzeli** herkes çok sevdi.',
            'B': 'Dün **güzel** bir gün geçirdik.',
            'C': 'Hava bugün gerçekten çok **güzel**.',
            'D': 'Çocuk **güzel** konuşuyordu.',
            'E': 'Onun **güzelliği** dillere destandı.',
        },
        'D',
        "'Güzel konuşmak' sözünde 'güzel', eylemi nasıl sorusuyla niteler; zarftır. Diğerlerinde sıfat, adlaşmış sıfat, yüklem ve isim (güzellik) olarak kullanılmıştır.",
    ),
    # düzey 2
    '0059': patch(
        'Aşağıdaki cümlelerin hangisinde sıfat-fiil yoktur?',
        {
            'A': 'Eve gelince seni hemen arayacağım, bekle.',
            'B': 'Bilinmeyen bir numaradan gece yarısı aradılar.',
            'C': 'Gülen gözleriyle bize bakıp selam verdi.',
            'D': 'Kapıyı açan küçük çocuk bizi hemen tanıdı.',
            'E': 'Tatilde okunacak kitapları bir listeye yazdı.',
        },
        'A',
        "'Okunacak, gülen, açan, bilinmeyen' adları niteleyen sıfat-fiillerdir. 'Gelince' ise zarf-fiildir; bu cümlede sıfat-fiil yoktur.",
    ),
    # düzey 3
    '0060': patch(
        'Aşağıdaki cümlelerin hangisinde kalın yazılmış sözcük adlaşmış bir sıfat-fiildir?',
        {
            'A': '**Okuyan** bir adım öndedir.',
            'B': 'Kitapları **okuyarak** öğrendi.',
            'C': '**Okumak** ona büyük keyif verir.',
            'D': 'Bütün kitabı bir günde **okudu**.',
            'E': '**Okuyan** öğrenciler sınavı kazandı.',
        },
        'A',
        "'Okuyan bir adım öndedir' cümlesinde 'okuyan', 'okuyan kişi' anlamında adın yerini tutar; adlaşmış sıfat-fiildir. 'Okuyan öğrenciler'de sıfat-fiil, 'okuyarak' zarf-fiil, 'okumak' isim-fiil, 'okudu' çekimli fiildir.",
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
    print(f"1 paket / {len(PATCHES)} soru ('Türkçe — Dil Bilgisi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
