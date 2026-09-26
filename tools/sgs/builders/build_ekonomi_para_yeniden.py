#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Para, Banka ve Dış Ekonomi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gercek sinav profiline gore yeniden yazim: para ve fonksiyonlari, miktar kurami, para carpani ve parasal taban, merkez bankasi araclari ve aktarim mekanizmasi, dis ticaret teorileri, ticaret politikasi ve entegrasyon, odemeler dengesi, doviz kuru, paritler ve kur rejimleri. 16 hesap sorusu bagimsiz dogrulandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Para-banka ve uluslararasi iktisat teorisi
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/ekonomi/para_banka_dis_ekonomi.json"
STYLE_REF = 'SGS Ekonomi (gercek sinav profiline kalibre: hesap + kisa sik)'
ONEK = "eko-para-gen-"


def patch(stem, options, answer, solution, ref='Para-banka ve uluslararasi iktisat teorisi'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 1
    '0001': patch(
        'Bir işletmenin mallarının fiyatlarını, borçlarını ve kârını Türk lirası cinsinden ifade ederek karşılaştırabilmesi paranın hangi fonksiyonuyla ilgilidir?',
        {
            'A': 'Değişim aracı',
            'B': 'Hesap birimi',
            'C': 'Likidite aracı',
            'D': 'Ertelenmiş ödemeler standardı',
            'E': 'Değer saklama aracı',
        },
        'B',
        'Paranın **hesap birimi** (ortak değer ölçüsü) fonksiyonu, farklı mal ve varlıkların değerlerinin aynı birimle ifade edilip karşılaştırılmasını sağlar. Değişim aracı işlevi mübadeleye aracılık etmeyi, değer saklama işlevi satın alma gücünü geleceğe taşımayı ifade eder.',
        'Para, banka ve dış ekonomi: paranın fonksiyonları',
    ),
    # düzey 2
    '0002': patch(
        'Aşağıdakilerden hangileri M2 para arzı tanımına girer?\n\nI. Dolaşımdaki para\n\nII. Vadesiz mevduat\n\nIII. Vadeli mevduat\n\nIV. Bankaların merkez bankasındaki serbest rezervleri',
        {
            'A': 'I, II ve III',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'I, II, III ve IV',
            'E': 'I, II ve IV',
        },
        'A',
        "**M1**, dolaşımdaki para (I) ile vadesiz mevduattan (II) oluşur; **M2**, M1'e vadeli mevduatın (III) eklenmesiyle bulunur. Bankaların merkez bankasındaki rezervleri (IV) para arzına değil, dolaşımdaki parayla birlikte **parasal tabana** dâhildir.",
        'Para, banka ve dış ekonomi: para arzı tanımları',
    ),
    # düzey 2
    '0003': patch(
        'Merkez bankasının faiz koridoru uyguladığı bir sistemde bankalararası piyasada oluşan gecelik faizin koridorun üst sınırına yaklaşması aşağıdakilerden hangisini gösterir?',
        {
            'A': 'Piyasada likidite fazlası bulunduğunu',
            'B': 'Politika faizinin indirildiğini',
            'C': 'Piyasada likidite sıkılığı bulunduğunu',
            'D': 'Bankaların merkez bankasına borç verdiğini',
            'E': 'Enflasyon beklentilerinin düştüğünü',
        },
        'C',
        'Koridorun üst sınırı merkez bankasının gecelik **borç verme**, alt sınırı gecelik **borç alma** faizidir. Bankalararası faizin üst sınıra yaklaşması, bankaların fon bulmakta zorlandığını ve merkez bankasından pahalı fonlamaya yöneldiğini, yani **likidite sıkılığını** gösterir; likidite fazlasında faiz alt sınıra yaklaşır.',
        'Para, banka ve dış ekonomi: faiz koridoru',
    ),
    # düzey 2
    '0004': patch(
        "Her yıl süresiz olarak 100 ₺ faiz ödeyen bir tahvilin (konsol) fiyatı, piyasa faiz oranı %5'ten %8'e yükseldiğinde ne olur?",
        {
            'A': "2.000 ₺'de sabit kalır",
            'B': "2.000 ₺'den 1.600 ₺'ye düşer",
            'C': "1.250 ₺'den 2.000 ₺'ye yükselir",
            'D': "2.000 ₺'den 1.250 ₺'ye düşer",
            'E': "500 ₺'den 800 ₺'ye yükselir",
        },
        'D',
        'Süresiz tahvilin fiyatı = yıllık faiz ödemesi / piyasa faizi: 100 / 0,05 = 2.000 ₺ ve 100 / 0,08 = **1.250 ₺**. Tahvil fiyatı ile piyasa faizi arasında **ters** ilişki vardır; faiz yükseldiğinde mevcut tahvilin sabit ödemesi daha az cazip hâle gelir.',
        'Para, banka ve dış ekonomi: tahvil fiyatı ve faiz',
    ),
    # düzey 2
    '0005': patch(
        'Mevduat sigortası sisteminin yarattığı olası sakıncaya ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Banka hücumlarının (panik) sıklığını artırır',
            'B': 'Merkez bankasının son kredi mercii rolünü ortadan kaldırır',
            'C': 'Bankaların riskli kredi vermesini doğrudan yasaklar',
            'D': 'Mevduat faizlerinin sıfıra inmesine neden olur',
            'E': 'Ahlaki tehlike yaratarak bankaların risk iştahını artırabilir',
        },
        'E',
        'Mevduat sigortası banka hücumlarını önler, ancak mevduatları güvence altında olan tasarruf sahipleri bankanın ne kadar risk aldığını izlemeye gerek görmez; bankalar da daha riskli davranabilir. Bu **ahlaki tehlike** sorunu, sigorta primlerinin riske göre belirlenmesi ve bankacılık denetimiyle sınırlandırılır.',
        'Para, banka ve dış ekonomi: mevduat sigortası',
    ),
    # düzey 3
    '0006': patch(
        'Aşağıdaki işlemlerden hangileri parasal tabanı artırır?\n\nI. Merkez bankasının bankalardan döviz satın alması\n\nII. Hazinenin merkez bankasındaki hesabından kamu personeline maaş ödemesi\n\nIII. Bankaların merkez bankasından aldıkları repo borcunu vadesinde geri ödemesi',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'Yalnız III',
        },
        'A',
        'Merkez bankası döviz aldığında karşılığında Türk lirası öder; bankaların rezervleri artar (I). Hazinenin merkez bankasındaki mevduatı parasal tabana dâhil değildir; maaş ödemesiyle bu fonlar banka hesaplarına geçer ve bankaların merkez bankasındaki rezervleri artar (II). Repo borcunun geri ödenmesi ise bankaların rezervlerini azaltır (III).',
        'Para, banka ve dış ekonomi: parasal taban',
    ),
    # düzey 1
    '0007': patch(
        "Sermaye bakımından bol olduğu kabul edilen ABD'nin, görece emek yoğun malları ihraç ettiğini ortaya koyan ve Heckscher-Ohlin teorisiyle çelişen ampirik bulgu hangisidir?",
        {
            'A': 'Hollanda hastalığı',
            'B': 'Rybczynski teoremi',
            'C': 'Stolper-Samuelson teoremi',
            'D': 'Leontief paradoksu',
            'E': 'Marshall-Lerner koşulu',
        },
        'D',
        "**Leontief paradoksu**, 1947 verileriyle ABD'nin ihracatının ithal ikamesi mallardan daha emek yoğun olduğunu gösterir. Açıklama olarak nitelikli emek (beşerî sermaye), doğal kaynaklar ve tüketim tercihleri öne sürülmüştür.",
        'Para, banka ve dış ekonomi: Leontief paradoksu',
    ),
    # düzey 3
    '0008': patch(
        "Küçük ve açık bir ekonomide bir malın yurt içi talebi Q = 100 − 5P, yurt içi arzı Q = −10 + 3P, dünya fiyatı 10 ₺'dir. Birim başına 2 ₺ gümrük vergisi konulursa ithalat miktarı ve devletin tarife geliri aşağıdakilerden hangisidir?",
        {
            'A': 'İthalat 30 birim; tarife geliri 60 ₺',
            'B': 'İthalat 16 birim; tarife geliri 32 ₺',
            'C': 'İthalat 20 birim; tarife geliri 40 ₺',
            'D': 'İthalat 14 birim; tarife geliri 28 ₺',
            'E': 'İthalat 14 birim; tarife geliri 168 ₺',
        },
        'D',
        'Tarife sonrası yurt içi fiyat 10 + 2 = 12 ₺ olur. Talep 100 − 60 = 40, yurt içi arz −10 + 36 = 26; ithalat 40 − 26 = **14** birim. Tarife geliri 2 × 14 = **28 ₺**. Tarifeden önce fiyat 10 ₺ iken talep 50, arz 20 ve ithalat 30 birimdi.',
        'Para, banka ve dış ekonomi: gümrük tarifesi',
    ),
    # düzey 2
    '0009': patch(
        'Aşağıdaki dış ticaret kısıtlamalarından hangisinde, yurt içi fiyatın yükselmesinden doğan rant genellikle yabancı ihracatçılara kalır?',
        {
            'A': 'Açık artırmayla dağıtılan ithalat kotası',
            'B': 'İthalat sübvansiyonu',
            'C': 'Antidamping vergisi',
            'D': 'Gümrük tarifesi',
            'E': 'Gönüllü ihracat kısıtlaması',
        },
        'E',
        '**Gönüllü ihracat kısıtlamasında** ihracatçı ülke ihracatını kendisi sınırlar; yurt içi fiyat yükselir ve aradaki fark (kota rantı) ihracatçı firmalara kalır. Gümrük tarifesinde bu fark tarife geliri olarak devlete, açık artırmalı kotada ise kota lisansı gelirleri olarak devlete geçer.',
        'Para, banka ve dış ekonomi: tarife dışı engeller',
    ),
    # düzey 1
    '0010': patch(
        'Bir ülkenin bir ticaret ortağına tanıdığı en elverişli gümrük koşulunu Dünya Ticaret Örgütünün diğer bütün üyelerine de ayrım yapmadan tanımasını öngören ilke aşağıdakilerden hangisidir?',
        {
            'A': 'Özel ve farklı muamele ilkesi',
            'B': 'Şeffaflık ilkesi',
            'C': 'En çok kayırılan ülke ilkesi',
            'D': 'Ulusal muamele ilkesi',
            'E': 'Karşılıklılık ilkesi',
        },
        'C',
        '**En çok kayırılan ülke (MFN) ilkesi**, bir üyeye tanınan ticaret ayrıcalığının diğer bütün üyelere de tanınmasını öngörür. **Ulusal muamele** ilkesi ise ithal malların gümrükten geçtikten sonra yerli mallarla aynı muameleye tabi tutulmasını ifade eder.',
        'Para, banka ve dış ekonomi: DTÖ ilkeleri',
    ),
    # düzey 2
    '0011': patch(
        "Aşağıdaki işlemlerden hangisi Türkiye'nin ödemeler dengesinde cari işlemler hesabının ikincil gelir dengesi altında kaydedilir?",
        {
            'A': "Yabancı turistlerin Türkiye'deki harcamaları",
            'B': "Yabancı bir fonun Borsa İstanbul'dan hisse senedi alması",
            'C': "Türkiye'deki yabancı yatırımcıya ödenen kâr payı",
            'D': 'Türk inşaat şirketinin yurt dışında yaptığı müteahhitlik hizmeti',
            'E': 'Yurt dışındaki işçilerin ailelerine gönderdiği para',
        },
        'E',
        '**İkincil gelir** dengesi karşılıksız transferleri kapsar: işçi gelirleri (aile yardımı havaleleri) ve bağışlar bu kaleme girer. Yatırım geliri olarak ödenen kâr payı **birincil gelir**, turist harcamaları ve müteahhitlik **hizmetler**, portföy hisse alımı ise **finans hesabı** kalemidir.',
        'Para, banka ve dış ekonomi: ödemeler dengesi',
    ),
    # düzey 2
    '0012': patch(
        "Türk lirası cinsinden bir yıllık faiz oranı %12, dolar cinsinden %4'tür. Kapsanmamış faiz paritesine göre piyasanın gelecek bir yıl için beklediği TL değer kaybı yaklaşık yüzde kaçtır?",
        {
            'A': '3',
            'B': '8',
            'C': '12',
            'D': '4',
            'E': '16',
        },
        'B',
        '**Kapsanmamış faiz paritesine** göre iki para biriminin faiz farkı, beklenen kur değişimine eşit olmalıdır: beklenen TL değer kaybı ≈ 12 − 4 = **%8** (kesin hesapla 1,12 / 1,04 ≈ 1,077). Aksi hâlde yatırımcılar yüksek faizli paraya yönelerek farkı arbitrajla kapatır.',
        'Para, banka ve dış ekonomi: faiz paritesi',
    ),
    # düzey 2
    '0013': patch(
        'Aşağıdakilerden hangileri sabit kur rejiminin özelliklerindendir?\n\nI. Merkez bankası ilan edilen kuru korumak için döviz alım-satımı yapar.\n\nII. Ödemeler dengesi dengesizlikleri kur değişimleriyle giderilir.\n\nIII. Sermaye hareketleri serbestse para politikası bağımsızlığını yitirir.',
        {
            'A': 'I ve III',
            'B': 'II ve III',
            'C': 'I, II ve III',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'A',
        'Sabit kurda merkez bankası ilan edilen paritede döviz alıp satmakla yükümlüdür (I) ve sermaye hareketleri serbestse faizini kuru korumaya bağlamak zorunda kalır; para politikası bağımsızlığını yitirir (III). Dengesizliklerin kur değişimiyle giderilmesi (II) ise **esnek** kur rejiminin özelliğidir.',
        'Para, banka ve dış ekonomi: sabit kur rejimi',
    ),
    # düzey 2
    '0014': patch(
        'Para kurulu sistemine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bağımsız para politikası yürütme imkânı ortadan kalkar',
            'B': 'Ulusal para çapa paraya kanunla belirlenmiş sabit kurdan bağlanır',
            'C': 'Dolaşımdaki para döviz rezervleriyle karşılanır',
            'D': 'Merkez bankası hazinenin açıklarını avansla finanse edebilir',
            'E': 'Döviz çıkışları para tabanını doğrudan daraltır',
        },
        'D',
        '**Para kurulunda** ulusal para çapa paraya kanuni sabit kurdan bağlanır, parasal taban döviz rezervleriyle karşılanır ve para arzı döviz giriş-çıkışlarına göre genişler ya da daralır; bağımsız para politikası yürütülemez. Rezerv karşılığı olmadan para yaratılamayacağı için hazineye avans verilmesi sistemle bağdaşmaz.',
        'Para, banka ve dış ekonomi: para kurulu',
    ),
    # düzey 2
    '0015': patch(
        'Sabit kur rejiminde ve sermaye hareketlerinin serbest olduğu bir ekonomide merkez bankasının para arzını artırmaya çalışmasının sonucu aşağıdakilerden hangisidir?',
        {
            'A': 'Rezervler artar ve para arzı iki katına çıkar',
            'B': 'Faiz yükselir ve sermaye girişi olur',
            'C': 'Faiz kalıcı olarak düşer ve hasıla artar',
            'D': 'Ulusal para değer kaybeder, net ihracat artar ve hasıla genişler',
            'E': 'Sermaye çıkışı olur ve para arzı eski düzeyine döner',
        },
        'E',
        'Para arzı artışı faizi düşürme eğilimi yaratır ve sermaye çıkışına yol açar; ulusal paraya değer kaybı baskısı oluşur. Kuru korumak zorunda olan merkez bankası rezervlerinden döviz satar ve karşılığında ulusal parayı piyasadan çeker; **para arzı eski düzeyine döner**. Sabit kur ve serbest sermayede para politikası etkisizdir.',
        'Para, banka ve dış ekonomi: sabit kurda para politikası',
    ),
    # düzey 2
    '0016': patch(
        'Bir bankanın kısa vadeli mevduatlarla uzun vadeli kredi vermesinden doğan ve mevduat sahiplerinin paralarını topluca çekmek istemesi hâlinde ortaya çıkan risk aşağıdakilerden hangisidir?',
        {
            'A': 'Likidite (vade uyumsuzluğu) riski',
            'B': 'Operasyonel risk',
            'C': 'Kur riski',
            'D': 'Ülke riski',
            'E': 'Kredi riski',
        },
        'A',
        'Bankalar kısa vadeli fonlarla uzun vadeli varlık oluşturur; mevduat sahipleri paralarını beklenmedik biçimde çekmek istediğinde banka varlıklarını zamanında nakde çeviremeyebilir. Bu **likidite (vade uyumsuzluğu) riskidir**. Kredi riski borçlunun geri ödememesi, kur riski döviz pozisyonundaki değer değişimidir.',
        'Para, banka ve dış ekonomi: bankacılık',
    ),
    # düzey 3
    '0017': patch(
        "Spot kurun 1 dolar = 30 ₺, TL faizinin yıllık %40, dolar faizinin yıllık %5 olduğu bir piyasada kapsanmış faiz paritesine göre bir yıl vadeli forward kur yaklaşık kaç ₺'dir?",
        {
            'A': '42',
            'B': '28,5',
            'C': '40',
            'D': '30',
            'E': '31,5',
        },
        'C',
        'Kapsanmış faiz paritesine göre F = S × (1 + i_TL) / (1 + i_$) = 30 × 1,40 / 1,05 = **40 ₺**. Forward kur spot kurun üzerindedir; çünkü yüksek faizli para birimi vadede **iskontolu** işlem görür. 42 ₺, dolar faizinin ihmal edilmesinin sonucudur.',
        'Para, banka ve dış ekonomi: kapsanmış faiz paritesi',
    ),
    # düzey 2
    '0018': patch(
        'Aşağıdaki kur rejimi–politika etkinliği eşleştirmelerinden hangisi Mundell-Fleming modeline göre yanlıştır? (Sermaye hareketleri tam serbesttir)',
        {
            'A': 'Esnek kurda genişletici para politikası – Ulusal para değer kaybeder',
            'B': 'Esnek kur – Maliye politikası etkilidir',
            'C': 'Esnek kur – Para politikası etkilidir',
            'D': 'Sabit kur – Maliye politikası etkilidir',
            'E': 'Sabit kur – Para politikası etkisizdir',
        },
        'B',
        'Tam sermaye hareketliliğinde **esnek kurda** genişletici maliye politikası sermaye girişi ve ulusal paranın değerlenmesiyle net ihracatı dışlar; **etkisizdir**. Para politikası ise değer kaybı ve net ihracat artışı yoluyla etkilidir. Sabit kurda tersine maliye politikası etkili, para politikası etkisizdir.',
        'Para, banka ve dış ekonomi: sabit kur ve maliye politikası',
    ),
    # düzey 2
    '0019': patch(
        'Sabit kur rejiminde ödemeler dengesi fazlası veren bir ülkenin merkez bankası kuru korumak için ne yapar ve bu işlem para arzını nasıl etkiler?',
        {
            'A': 'Faizi yükseltir; para arzı değişmez',
            'B': 'Döviz satın alır; para arzı azalır',
            'C': 'Rezervleri azaltır; para arzı artar',
            'D': 'Döviz satar; para arzı azalır',
            'E': 'Döviz satın alır; para arzı artar',
        },
        'E',
        'Fazla, döviz arzını artırır ve ulusal paraya değer kazanma baskısı yaratır. Merkez bankası kuru korumak için piyasadan **döviz satın alır** ve karşılığında ulusal para öder; rezervler ve **para arzı artar**. Bu etki sterilizasyon işlemleriyle kısmen giderilebilir.',
        'Para, banka ve dış ekonomi: rezervler ve kur',
    ),
    # düzey 2
    '0020': patch(
        'Altın ve gümüşün birlikte kanuni ödeme aracı olduğu çift maden sisteminde resmî darphane oranı, gümüşü piyasa değerinin üzerinde değerlendirmektedir. Gresham kanununa göre ne olması beklenir?',
        {
            'A': 'Gümüş dolaşımdan çekilir, ödemelerde altın kullanılır',
            'B': 'İki maden de dolaşımda eşit ölçüde kalır',
            'C': 'Gümüş yurt dışına çıkar, altın yurda girer',
            'D': 'Altın dolaşımdan çekilir, ödemelerde gümüş kullanılır',
            'E': 'Altının piyasa fiyatı darphane oranına kadar düşer',
        },
        'D',
        'Darphane oranı gümüşü yüksek değerlendirdiğinde altın, para olarak piyasa değerinin altında sayılır. Bu durumda altın saklanır, eritilir veya yurt dışına çıkarılır; ödemelerde değeri yüksek gösterilen gümüş kullanılır. "Kötü para iyi parayı kovar" diye özetlenen **Gresham kanunu** budur.',
        'Para, banka ve dış ekonomi: Gresham kanunu',
    ),
    # düzey 2
    '0021': patch(
        'Miktar kuramının geçerli olduğu bir ekonomide bir yılda para arzı %12 artmış, paranın dolaşım hızı %2 azalmış ve reel hasıla %4 büyümüştür. Bu ekonomide enflasyon oranı yaklaşık yüzde kaçtır?',
        {
            'A': '8',
            'B': '14',
            'C': '10',
            'D': '18',
            'E': '6',
        },
        'E',
        'Miktar denklemi MV = PY büyüme oranlarıyla yazıldığında %ΔM + %ΔV ≈ %ΔP + %ΔY olur. Buradan enflasyon ≈ 12 + (−2) − 4 = **%6**. Dolaşım hızındaki düşüş ihmal edilirse %8, işareti ters alınırsa %10 bulunur.',
        'Para, banka ve dış ekonomi: miktar kuramı',
    ),
    # düzey 3
    '0022': patch(
        "Halkın nakit tutma oranının mevduatların %30'u olduğu ve bankaların fazla rezerv tutmadığı bir ekonomide parasal taban 500 birimdir. Merkez bankası zorunlu karşılık oranını %20'den %10'a indirirse, parasal taban değişmediği varsayımıyla para arzı kaç birim artar?",
        {
            'A': '250',
            'B': '1.625',
            'C': '325',
            'D': '650',
            'E': '2.500',
        },
        'C',
        "Para çarpanı m = (1 + c) / (c + rr)'dir. Başlangıçta m = 1,30 / 0,50 = 2,6 ve para arzı 2,6 × 500 = 1.300; indirimden sonra m = 1,30 / 0,40 = 3,25 ve para arzı 1.625 olur. Artış 1.625 − 1.300 = **325** birimdir. 1.625 yeni para arzı düzeyidir; 2.500 nakit oranını ihmal eden 1/rr çarpanıyla, 250 ise payda (1 + c) unutularak bulunur.",
        'Para, banka ve dış ekonomi: para çarpanı',
    ),
    # düzey 1
    '0023': patch(
        'Parasal taban (rezerv para) aşağıdakilerden hangisidir?',
        {
            'A': 'Dolaşımdaki para ile bankaların merkez bankasındaki rezervlerinin toplamı',
            'B': 'Bankaların verdiği kredilerin toplamı',
            'C': 'Vadesiz ve vadeli mevduatların toplamı',
            'D': 'Dolaşımdaki para ile vadesiz mevduatların toplamı',
            'E': 'Merkez bankasının döviz rezervleri ile altın stokunun toplamı',
        },
        'A',
        '**Parasal taban**, merkez bankasının doğrudan kontrol ettiği para büyüklüğüdür: halkın elindeki banknot ve madeni para (dolaşımdaki para) ile bankaların merkez bankasında tuttuğu rezervler. Para arzı, parasal tabanın para çarpanıyla çarpımına eşittir.',
        'Para, banka ve dış ekonomi: parasal taban',
    ),
    # düzey 2
    '0024': patch(
        "Keynes'in likidite tercihi teorisine göre aşağıdaki para talebi güdülerinden hangileri esas olarak faiz oranına bağlıdır?\n\nI. İşlem güdüsü\n\nII. İhtiyat güdüsü\n\nIII. Spekülasyon güdüsü",
        {
            'A': 'I, II ve III',
            'B': 'Yalnız III',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'B',
        "Keynes'e göre işlem (I) ve ihtiyat (II) güdüleriyle tutulan para esas olarak **gelir** düzeyine bağlıdır. **Spekülasyon** güdüsü (III) ise tahvil fiyatı beklentilerine ve faiz oranına bağlıdır: faiz yükseldikçe para tutmanın fırsat maliyeti artar ve spekülatif para talebi azalır.",
        'Para, banka ve dış ekonomi: para talebi güdüleri',
    ),
    # düzey 2
    '0025': patch(
        'Baumol-Tobin modeline göre işlem amaçlı para talebinin gelir esnekliği kaçtır?',
        {
            'A': '0,5',
            'B': '−0,5',
            'C': '0',
            'D': '1',
            'E': '2',
        },
        'A',
        "Baumol-Tobin modelinde optimal ortalama nakit M = √(bY / 2i)'dir; para talebi gelirin karekökü ile orantılıdır ve **gelir esnekliği 0,5**, faiz esnekliği −0,5'tir. Gelir iki katına çıktığında para talebi yaklaşık %41 artar; bu, nakit yönetiminde ölçek ekonomisi bulunduğunu gösterir.",
        'Para, banka ve dış ekonomi: para talebi',
    ),
    # düzey 2
    '0026': patch(
        'Enflasyon hedeflemesi stratejisine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Para arzı büyüme oranı ara hedef olarak ilan edilir',
            'B': 'Sayısal enflasyon hedefi kamuoyuna açıkça duyurulur',
            'C': 'Hedeften sapmalarda merkez bankası kamuoyuna hesap verir',
            'D': 'Enflasyon beklentilerinin yönetiminde iletişim önem taşır',
            'E': 'Kısa vadeli politika faizi temel araç olarak kullanılır',
        },
        'A',
        'Enflasyon hedeflemesinde nihai hedef olan enflasyon oranı açıkça ilan edilir, politika faizi temel araçtır ve merkez bankası hedeften sapmalar için hesap verir; beklenti yönetimi ve iletişim stratejinin merkezindedir. Para arzı büyümesinin ara hedef olarak ilan edilmesi ise **parasal hedefleme** stratejisinin özelliğidir.',
        'Para, banka ve dış ekonomi: enflasyon hedeflemesi',
    ),
    # düzey 3
    '0027': patch(
        'Bir saatlik emekle A ülkesi 10 metre kumaş veya 5 litre şarap, B ülkesi 6 metre kumaş veya 4 litre şarap üretebilmektedir. İki ülkenin de ticaretten kazanç sağlayabileceği dış ticaret hadleri (1 metre kumaş karşılığı şarap) aşağıdaki aralıklardan hangisindedir?',
        {
            'A': '0,67 ile 1 litre arasında',
            'B': '1,5 ile 2 litre arasında',
            'C': '2 litrenin üzerinde',
            'D': '0 ile 0,5 litre arasında',
            'E': '0,5 ile yaklaşık 0,67 litre arasında',
        },
        'E',
        "Ticaret hadleri iki ülkenin iç fırsat maliyetleri arasında olmalıdır. Kumaşın iç fiyatı A'da 0,5, B'de yaklaşık 0,67 litre şaraptır. A, kumaşı 0,5 litreden fazlasına; B ise 0,67 litreden azına satın alabildiğinde kazanır: **0,5 < ticaret hadleri < 0,67**. 1,5-2 aralığı şarabın kumaş cinsinden fiyatlarıdır.",
        'Para, banka ve dış ekonomi: dış ticaret hadleri',
    ),
    # düzey 2
    '0028': patch(
        'Stolper-Samuelson teoremine göre bir malın göreli fiyatının artması, bu malın üretiminde yoğun olarak kullanılan faktörün reel getirisini nasıl etkiler?',
        {
            'A': 'İki faktörün reel getirisini de azaltır',
            'B': 'Etkilemez',
            'C': 'İki faktörün reel getirisini de eşit oranda artırır',
            'D': 'Artırır; diğer faktörün reel getirisini azaltır',
            'E': 'Azaltır; diğer faktörün reel getirisini artırır',
        },
        'D',
        '**Stolper-Samuelson** teoremine göre bir malın göreli fiyatının artması, o malda yoğun kullanılan faktörün reel getirisini **artırır**, diğer faktörünkini **azaltır**. Bu nedenle serbest ticaret, ülkenin bol faktörünün sahiplerine kazanç, kıt faktörünün sahiplerine kayıp getirir.',
        'Para, banka ve dış ekonomi: Stolper-Samuelson teoremi',
    ),
    # düzey 1
    '0029': patch(
        'Yeni kurulan ve henüz ölçek ekonomilerinden yararlanamayan yerli sanayilerin rekabet gücü kazanana kadar geçici olarak dış rekabetten korunmasını savunan argüman aşağıdakilerden hangisidir?',
        {
            'A': 'Antidamping argümanı',
            'B': 'Optimal tarife argümanı',
            'C': 'Bebek (genç) endüstri argümanı',
            'D': 'Ucuz yabancı emek argümanı',
            'E': 'Ulusal güvenlik argümanı',
        },
        'C',
        '**Bebek endüstri argümanı** (List), gelişme potansiyeli olan yeni sanayilerin öğrenme ve ölçek ekonomileri sağlanana kadar geçici korumayla desteklenmesini savunur. Koruma kalıcı olursa sanayinin verimsiz kalma riski vardır.',
        'Para, banka ve dış ekonomi: korumacılık argümanları',
    ),
    # düzey 2
    '0030': patch(
        'Gümrük birliğine giren bir ülkenin, bir malı daha önce ithal ettiği düşük maliyetli üçüncü ülke yerine, ortak dış tarife nedeniyle daha yüksek maliyetli bir üye ülkeden ithal etmeye başlaması hangi etkiyle açıklanır?',
        {
            'A': 'Stolper-Samuelson etkisi',
            'B': 'Rybczynski etkisi',
            'C': 'Ticaret yaratıcı etki',
            'D': 'Ticaret saptırıcı etki',
            'E': 'Ölçek ekonomisi etkisi',
        },
        'D',
        "Viner'e göre **ticaret saptırıcı etki**, ithalatın daha verimli üçüncü ülkeden daha az verimli üye ülkeye kaymasıdır ve refahı azaltır. **Ticaret yaratıcı etki** ise daha pahalı yurt içi üretimin yerini daha ucuz üye ülke ithalatının almasıdır ve refahı artırır.",
        'Para, banka ve dış ekonomi: ticaret saptırıcı etki',
    ),
    # düzey 2
    '0031': patch(
        'Aşağıdakilerden hangileri Heckscher-Ohlin modelinin varsayımlarındandır?\n\nI. Ülkeler arasında üretim teknolojisi aynıdır.\n\nII. Üretim faktörleri ülkeler arasında serbestçe dolaşır.\n\nIII. Mallar ölçeğe göre artan getiriyle üretilir.',
        {
            'A': 'I ve II',
            'B': 'I ve III',
            'C': 'I, II ve III',
            'D': 'Yalnız I',
            'E': 'Yalnız II',
        },
        'D',
        'Heckscher-Ohlin modeli ülkelerin **aynı teknolojiye** sahip olduğunu (I) varsayar; böylece ticaretin kaynağı yalnızca faktör donatımı farkı olur. Model, faktörlerin ülke içinde hareketli fakat **ülkeler arasında hareketsiz** olduğunu (II) ve üretimin **ölçeğe göre sabit getiriyle** (III) yapıldığını kabul eder.',
        'Para, banka ve dış ekonomi: Heckscher-Ohlin varsayımları',
    ),
    # düzey 3
    '0032': patch(
        "Bir yılda TL/dolar nominal kuru %5 artmış, Türkiye'de enflasyon %9, ABD'de %1 olmuştur. Reel kur q = E × P* / P biçiminde tanımlandığında (E: 1 dolar karşılığı TL) Türk lirasının reel değerindeki değişim yaklaşık olarak aşağıdakilerden hangisidir?",
        {
            'A': 'TL reel olarak yaklaşık %3 değer kaybetmiştir',
            'B': 'TL reel olarak yaklaşık %3 değer kazanmıştır',
            'C': 'Reel kur değişmemiştir',
            'D': 'TL reel olarak yaklaşık %5 değer kaybetmiştir',
            'E': 'TL reel olarak yaklaşık %4 değer kazanmıştır',
        },
        'B',
        "Reel kurdaki değişim ≈ nominal kur değişimi + yurt dışı enflasyon − yurt içi enflasyon = 5 + 1 − 9 = **−%3** (kesin hesapla 1,05 × 1,01 / 1,09 ≈ 0,973). Bu tanımda q'nun düşmesi, yabancı malların yerli mallara göre ucuzlaması, yani **TL'nin reel değer kazanması** demektir. Nominal değer kaybına rağmen yurt içi enflasyon kur artışını aştığı için TL reel olarak değerlenmiştir.",
        'Para, banka ve dış ekonomi: reel döviz kuru',
    ),
    # düzey 2
    '0033': patch(
        "Bir ülkede ithalat talebinin fiyat esnekliği 0,4, ihracat talebinin fiyat esnekliği 0,5'tir (mutlak değer). Marshall-Lerner koşuluna göre ulusal paranın değer kaybetmesi uzun dönemde dış ticaret dengesini nasıl etkiler?",
        {
            'A': 'İhracat esnekliği ithalatınkinden büyük olduğu için dengeyi iyileştirir',
            'B': "Esneklikler toplamı 1'den küçük olduğu için dengeyi iyileştirir",
            'C': 'Esneklikler dış ticaret dengesini etkilemez',
            'D': "Esneklikler toplamı 1'den büyük olduğu için dengeyi iyileştirir",
            'E': "Esneklikler toplamı 1'den küçük olduğu için dengeyi kötüleştirir",
        },
        'E',
        "**Marshall-Lerner koşuluna** göre değer kaybının dış ticaret dengesini iyileştirmesi için ihracat ve ithalat talep esnekliklerinin (mutlak) toplamı **1'den büyük** olmalıdır. Burada 0,4 + 0,5 = 0,9 < 1 olduğundan fiyat etkisi miktar etkisinden büyüktür ve denge **kötüleşir**.",
        'Para, banka ve dış ekonomi: Marshall-Lerner koşulu',
    ),
    # düzey 2
    '0034': patch(
        'Hollanda hastalığına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ulusal paranın reel değer kaybı yoluyla imalat ihracatını artırır',
            'B': 'Döviz girişiyle ulusal para reel olarak değerlenir',
            'C': 'Doğal kaynak ihracatındaki hızlı artışla ortaya çıkar',
            'D': "Adını 1960'lardaki Hollanda doğal gaz keşfinden alır",
            'E': 'Kaynak sektörüne kayan emek ve sermaye imalat sanayinin daralmasına yol açar',
        },
        'A',
        '**Hollanda hastalığında** doğal kaynak ihracatındaki artış döviz girişini ve ulusal paranın reel değerini **yükseltir**; emek ve sermaye kaynak sektörüne kayar, imalat sanayi rekabet gücünü yitirir ve daralır. Ulusal paranın reel değer kaybıyla imalat ihracatının artması bu sürecin tersidir.',
        'Para, banka ve dış ekonomi: Hollanda hastalığı',
    ),
    # düzey 1
    '0035': patch(
        'Aşağıdakilerden hangileri Uluslararası Para Fonunun (IMF) görevleri arasındadır?\n\nI. Ödemeler dengesi güçlüğündeki üyelere finansman sağlamak\n\nII. Özel Çekme Hakkı (SDR) ihraç etmek\n\nIII. Üyeler arasındaki ticaret uyuşmazlıklarında bağlayıcı karar vermek',
        {
            'A': 'Yalnız I',
            'B': 'I, II ve III',
            'C': 'Yalnız III',
            'D': 'I ve III',
            'E': 'I ve II',
        },
        'E',
        '**IMF**, ödemeler dengesi güçlüğündeki üyelere program karşılığı finansman sağlar (I) ve SDR adlı uluslararası rezerv varlığını ihraç eder (II). Ticaret uyuşmazlıklarının çözümü (III) **Dünya Ticaret Örgütünün** uyuşmazlık çözüm mekanizmasına aittir.',
        'Para, banka ve dış ekonomi: uluslararası kuruluşlar',
    ),
    # düzey 2
    '0036': patch(
        'Bir ülkede ulusal paranın değer kaybından hemen sonra dış ticaret dengesinin önce kötüleşip ardından iyileşmesinin temel nedeni aşağıdakilerden hangisidir?',
        {
            'A': 'Faiz oranlarının hemen düşmesi',
            'B': 'Merkez bankası rezervlerinin artması',
            'C': 'Marshall-Lerner koşulunun kısa dönemde sağlanması',
            'D': 'Dış ticaret miktarlarının kura gecikmeyle uyum sağlaması',
            'E': 'Değer kaybının ihracat fiyatlarını yükseltmesi',
        },
        'D',
        'Değer kaybından hemen sonra ithalat ve ihracat miktarları sözleşmeler ve alışkanlıklar nedeniyle hemen değişmez; ithalatın yerli para cinsinden maliyeti ise artar ve denge **önce kötüleşir**. Zamanla miktarlar uyum sağladığında (esneklikler büyüdüğünde) denge iyileşir; bu seyir **J eğrisi** olarak gösterilir.',
        'Para, banka ve dış ekonomi: J eğrisi',
    ),
    # düzey 2
    '0037': patch(
        'Esnek kur rejimindeki bir ülkede ulusal paranın değer kaybetmesinin kısa dönemde beklenen etkilerinden hangisi yanlıştır?',
        {
            'A': 'İthal girdilerin yerli para cinsinden maliyeti düşer',
            'B': 'Turizm gelirlerinin artması beklenir',
            'C': 'Döviz cinsinden borcu olan firmaların borç yükü artar',
            'D': 'İthal malların yurt içi fiyatı yükselir',
            'E': 'İhracat mallarının yabancı para cinsinden fiyatı düşer',
        },
        'A',
        'Ulusal para değer kaybettiğinde yabancı paralar pahalılaşır: ithal mallar ve **ithal girdiler yerli para cinsinden pahalanır**, döviz borcunun yerli para karşılığı artar. Buna karşılık yerli mallar yabancılar için ucuzlar; ihracat ve turizm gelirleri artma eğilimi gösterir.',
        'Para, banka ve dış ekonomi: kur ve dış ticaret',
    ),
    # düzey 2
    '0038': patch(
        "Aşağıdaki işlemlerden hangileri Türkiye'nin ödemeler dengesinde cari işlemler hesabında yer alır?\n\nI. Türk bir şirketin yurt dışındaki bir bankadan kredi alması\n\nII. Yabancı öğrencilerin Türkiye'deki üniversitelere ödediği eğitim ücretleri\n\nIII. Türkiye'deki yabancı sahipli şirketin kârını ana şirkete aktarması",
        {
            'A': 'Yalnız I',
            'B': 'I, II ve III',
            'C': 'II ve III',
            'D': 'Yalnız II',
            'E': 'I ve III',
        },
        'C',
        'Yabancı öğrencilerin eğitim harcamaları **hizmet ihracatıdır** (II); yabancı sahipli şirketin kâr transferi yatırım geliri olarak **birincil gelir** dengesine kaydedilir (III); ikisi de cari işlemler hesabındadır. Yurt dışından kredi alınması ise **finans hesabında** borç girişidir (I).',
        'Para, banka ve dış ekonomi: ödemeler dengesi',
    ),
    # düzey 1
    '0039': patch(
        'Bir birim yabancı paranın ulusal para cinsinden fiyatı olarak tanımlanan döviz kurunun yükselmesi aşağıdakilerden hangisini gösterir?',
        {
            'A': 'Faiz oranlarının düşmesini',
            'B': 'Ulusal paranın değer kaybetmesini',
            'C': 'Ulusal paranın değer kazanmasını',
            'D': 'Yabancı paranın değer kaybetmesini',
            'E': 'Reel kurun sabit kalmasını',
        },
        'B',
        "Kur, 1 dolar = X ₺ biçiminde tanımlandığında X'in artması bir dolar için daha fazla TL ödendiği, yani **ulusal paranın değer kaybettiği** anlamına gelir. Kurun tersine tanımlandığı (1 ₺ = Y dolar) durumda ise değer kaybı Y'nin düşmesiyle görülür.",
        'Para, banka ve dış ekonomi: döviz kuru tanımı',
    ),
    # düzey 3
    '0040': patch(
        'Bir ülkenin bir yıllık ödemeler dengesi verileri (milyar dolar) şöyledir: mal ihracatı 250, mal ithalatı 320, hizmet gelirleri 60, hizmet giderleri 20, birincil gelir dengesi −15, ikincil gelir dengesi +5. Bu ülkenin cari işlemler açığı kaç milyar dolardır?',
        {
            'A': '40',
            'B': '30',
            'C': '45',
            'D': '70',
            'E': '10',
        },
        'A',
        'Dış ticaret dengesi 250 − 320 = −70; hizmetler dengesi 60 − 20 = +40; mal ve hizmet dengesi −30. Buna birincil gelir (−15) ve ikincil gelir (+5) eklenince cari işlemler dengesi −30 − 15 + 5 = **−40**, yani **40 milyar dolar açık** bulunur. 70 yalnız dış ticaret dengesidir; 45 ikincil gelirin, 30 ise gelir dengelerinin ihmal edilmesinin sonucudur.',
        'Para, banka ve dış ekonomi: cari işlemler dengesi',
    ),
    # düzey 2
    '0041': patch(
        "Bir mevduatın yıllık nominal faiz oranı %30, beklenen yıllık enflasyon %25'tir. Fisher yaklaşımına göre beklenen reel faiz oranı yaklaşık yüzde kaçtır?",
        {
            'A': '1,2',
            'B': '4',
            'C': '5',
            'D': '55',
            'E': '25',
        },
        'B',
        "Kesin Fisher ilişkisi (1 + i) = (1 + r)(1 + π)'dir: 1,30 / 1,25 = 1,04 → reel faiz **%4**. Yaklaşık formül (i − π) %5 verir; enflasyon yüksek olduğunda yaklaşık formülün hatası büyür. 55 ise oranların toplanmasının hatalı sonucudur.",
        'Para, banka ve dış ekonomi: Fisher denklemi',
    ),
    # düzey 2
    '0042': patch(
        "Zorunlu karşılık oranının %20 olduğu, halkın nakit tutmadığı ve bankaların fazla rezerv tutmadığı bir bankacılık sisteminde bir bankaya 1.000 ₺ yeni mevduat yatırılmıştır. Sistemin yaratabileceği toplam mevduat ve kaydi para sırasıyla kaç ₺'dir?",
        {
            'A': '5.000 ve 4.000',
            'B': '5.000 ve 5.000',
            'C': '4.000 ve 5.000',
            'D': '1.200 ve 200',
            'E': '2.000 ve 1.000',
        },
        'A',
        "Basit mevduat çarpanı 1 / rr = 1 / 0,20 = 5'tir; toplam mevduat 1.000 × 5 = **5.000 ₺** olur. Bunun ilk 1.000 ₺'si sisteme yatırılan mevduattır; bankaların kredi yoluyla yarattığı **kaydi para** 5.000 − 1.000 = **4.000 ₺**'dir.",
        'Para, banka ve dış ekonomi: kaydi para',
    ),
    # düzey 3
    '0043': patch(
        "Taylor kuralının i = r* + π + 0,5(π − π*) + 0,5(çıktı açığı) biçimde uygulandığı bir ekonomide denge reel faizi %2, enflasyon %6, enflasyon hedefi %4 ve çıktı açığı +%2'dir. Kurala göre politika faizi yüzde kaç olmalıdır?",
        {
            'A': '12',
            'B': '6',
            'C': '9',
            'D': '8',
            'E': '10',
        },
        'E',
        'i = 2 + 6 + 0,5 × (6 − 4) + 0,5 × 2 = 2 + 6 + 1 + 1 = **%10**. Enflasyon hedefin, üretim potansiyelin üzerinde olduğu için kural, reel faizi denge düzeyinin üzerine çıkaracak bir sıkılaştırma önerir (reel faiz %4).',
        'Para, banka ve dış ekonomi: Taylor kuralı',
    ),
    # düzey 1
    '0044': patch(
        'Türkiye Cumhuriyet Merkez Bankasının para politikası duruşunu yansıtan politika faizi olarak kullandığı oran aşağıdakilerden hangisidir?',
        {
            'A': 'Zorunlu karşılık oranı',
            'B': 'Gecelik borç verme faiz oranı',
            'C': 'Bir hafta vadeli repo ihale faiz oranı',
            'D': 'Reeskont faiz oranı',
            'E': 'Mevduat sigortası primi',
        },
        'C',
        'TCMB, **bir hafta vadeli repo ihale faiz oranını** politika faizi olarak kullanır ve likiditeyi bu oranla piyasaya sağlar. Gecelik borç verme ve borç alma faizleri faiz koridorunun üst ve alt sınırlarını oluşturur; zorunlu karşılık oranı ise bir faiz değil, rezerv yükümlülüğüdür.',
        'Para, banka ve dış ekonomi: TCMB politika faizi',
    ),
    # düzey 2
    '0045': patch(
        'Aşağıdakilerden hangileri para politikasının ekonomiye aktarım kanallarındandır?\n\nI. Faiz kanalı\n\nII. Döviz kuru kanalı\n\nIII. Kredi kanalı\n\nIV. Beklenti kanalı',
        {
            'A': 'I ve II',
            'B': 'I ve III',
            'C': 'II, III ve IV',
            'D': 'I, II ve III',
            'E': 'I, II, III ve IV',
        },
        'E',
        'Para politikası kararları ekonomiye piyasa faizleri (I), döviz kuru (II), banka kredileri (III), varlık fiyatları ve ekonomik birimlerin **beklentileri** (IV) aracılığıyla aktarılır; dördü de aktarım mekanizmasının kanallarıdır.',
        'Para, banka ve dış ekonomi: aktarım mekanizması',
    ),
    # düzey 3
    '0046': patch(
        'Bir saatlik emekle A ülkesi 10 metre kumaş veya 5 litre şarap, B ülkesi 6 metre kumaş veya 4 litre şarap üretebilmektedir. Mukayeseli üstünlükler teorisine göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'B iki malda da mutlak üstündür',
            'B': 'A kumaşta, B şarapta uzmanlaşmalıdır',
            'C': 'Fırsat maliyetleri eşit olduğu için ticaretten kazanç yoktur',
            'D': 'A şarapta, B kumaşta uzmanlaşmalıdır',
            'E': 'A iki malda da uzmanlaşmalı, ticaret yapılmamalıdır',
        },
        'B',
        "A iki malda da **mutlak** üstündür, ancak uzmanlaşmayı fırsat maliyetleri belirler. Bir metre kumaşın fırsat maliyeti A'da 5/10 = 0,5 litre, B'de 4/6 ≈ 0,67 litre şaraptır; kumaş A'da görece ucuzdur. Bir litre şarabın fırsat maliyeti A'da 2, B'de 1,5 metre kumaştır; şarap B'de görece ucuzdur. Bu nedenle **A kumaşta, B şarapta** uzmanlaşır.",
        'Para, banka ve dış ekonomi: mukayeseli üstünlük',
    ),
    # düzey 2
    '0047': patch(
        'Heckscher-Ohlin teorisine göre emek bakımından bol, sermaye bakımından kıt bir ülkenin dış ticaret yapısına ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Teknoloji farkına göre uzmanlaşır; faktör donatımı önemsizdir',
            'B': 'Emek yoğun malları hem ihraç hem ithal eder',
            'C': 'Faktör donatımı ticaret yapısını etkilemez',
            'D': 'Sermaye yoğun malları ihraç, emek yoğun malları ithal eder',
            'E': 'Emek yoğun malları ihraç, sermaye yoğun malları ithal eder',
        },
        'E',
        '**Heckscher-Ohlin** teorisine göre mukayeseli üstünlüğün kaynağı **faktör donatımı** farklılıklarıdır: bir ülke bol olan faktörü yoğun kullanan malları ihraç, kıt faktörü yoğun kullanan malları ithal eder. Ricardo modeli ise üstünlüğü emek verimliliği (teknoloji) farkına bağlar.',
        'Para, banka ve dış ekonomi: Heckscher-Ohlin teorisi',
    ),
    # düzey 1
    '0048': patch(
        "Almanya'nın Fransa'ya otomobil ihraç ederken aynı zamanda Fransa'dan otomobil ithal etmesi gibi aynı sektördeki farklılaştırılmış ürünlerin karşılıklı ticareti hangi kavramla açıklanır?",
        {
            'A': 'Transit ticaret',
            'B': 'Endüstriler arası ticaret',
            'C': 'Endüstri içi ticaret',
            'D': 'Damping',
            'E': 'Mukayeseli üstünlük',
        },
        'C',
        '**Endüstri içi ticaret**, aynı sektördeki farklılaştırılmış ürünlerin ülkeler arasında karşılıklı ticaretidir; ölçek ekonomileri ve tüketicilerin çeşit tercihiyle açıklanır. Faktör donatımı veya verimlilik farkına dayanan farklı sektörler arasındaki ticaret ise endüstriler arası ticarettir.',
        'Para, banka ve dış ekonomi: endüstri içi ticaret',
    ),
    # düzey 2
    '0049': patch(
        'Aşağıdakilerden hangileri ortak pazar aşamasındaki ekonomik entegrasyonun özelliklerindendir?\n\nI. Üyeler arası ticarette gümrük vergilerinin kaldırılması\n\nII. Üçüncü ülkelere ortak dış tarife uygulanması\n\nIII. Emek ve sermayenin üyeler arasında serbest dolaşımı\n\nIV. Ortak para birimi ve tek merkez bankası',
        {
            'A': 'I ve II',
            'B': 'I, II, III ve IV',
            'C': 'II ve IV',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'D',
        "Balassa'nın sınıflandırmasında **gümrük birliği**, üyeler arası tarifelerin kaldırılmasına (I) ortak dış tarifeyi (II) ekler. **Ortak pazar** bunlara üretim faktörlerinin serbest dolaşımını (III) katar. Ortak para ve tek merkez bankası (IV) ise **parasal birlik** aşamasının özelliğidir.",
        'Para, banka ve dış ekonomi: ekonomik entegrasyon',
    ),
    # düzey 2
    '0050': patch(
        'Bir yabancı firmanın ürününü kendi iç piyasasındaki fiyatın altında ihraç ettiğinin belirlenmesi hâlinde ithalatçı ülkenin başvurabileceği koruma aracı aşağıdakilerden hangisidir?',
        {
            'A': 'Antidamping vergisi',
            'B': 'Telafi edici vergi',
            'C': 'İhracat sübvansiyonu',
            'D': 'İthalat sübvansiyonu',
            'E': 'Gönüllü ihracat kısıtlaması',
        },
        'A',
        'Malın ihracatçı ülkedeki normal değerinin altında ihraç edilmesi **dampingdir**; yerli sanayiye zarar veriyorsa aradaki farkı gidermek üzere **antidamping vergisi** uygulanır. Telafi edici vergi ise yabancı hükümetin verdiği sübvansiyonların etkisini gidermeye yöneliktir.',
        'Para, banka ve dış ekonomi: damping',
    ),
    # düzey 3
    '0051': patch(
        'Aşağıdaki işlem–ödemeler dengesi hesabı eşleştirmelerinden hangisi yanlıştır?',
        {
            'A': "TCMB'nin döviz rezervlerindeki artış – Rezerv varlıklar",
            'B': 'Bir markanın yurt dışındaki bir şirkete devredilmesi – Sermaye hesabı',
            'C': "Yabancı şirketin Türkiye'de fabrika kurması – Cari işlemler hesabı",
            'D': 'Türk havayolunun yabancı yolculara sattığı bilet – Hizmetler dengesi',
            'E': 'Türk vatandaşının yurt dışındaki mevduatına tahakkuk eden faiz – Birincil gelir',
        },
        'C',
        "Yabancıların Türkiye'de şirket kurmak veya %10 ve üzeri ortaklık edinmek için getirdiği sermaye **doğrudan yatırım** olarak **finans hesabına** kaydedilir; cari işlemler hesabına değil. Mevduat faizi birincil gelir, marka gibi üretilmemiş finansal olmayan varlık devri sermaye hesabı, rezerv değişimi rezerv varlıklar, bilet satışı hizmet ihracatıdır.",
        'Para, banka ve dış ekonomi: ödemeler dengesi',
    ),
    # düzey 2
    '0052': patch(
        "Aynı tüketim sepeti Türkiye'de 3.000 ₺, ABD'de 100 dolardır. Piyasa döviz kuru 1 dolar = 40 ₺ ise mutlak satın alma gücü paritesine göre aşağıdakilerden hangisi söylenebilir?",
        {
            'A': "Parite kuru 30 ₺'dir; TL piyasada paritesine göre değerinin üzerindedir",
            'B': "Parite kuru 0,033 ₺'dir; kur paritede kabul edilir",
            'C': "Parite kuru 3.000 ₺'dir; TL aşırı değerlidir",
            'D': "Parite kuru 40 ₺'dir; TL paritede değerlenmektedir",
            'E': "Parite kuru 30 ₺'dir; TL piyasada paritesine göre değerinin altındadır",
        },
        'E',
        'Mutlak satın alma gücü paritesinde kur, iki ülkenin fiyat düzeyleri oranına eşittir: E = P / P* = 3.000 / 100 = **30 ₺**. Piyasa kuru (40 ₺) paritenin üzerinde olduğundan bir dolar için paritenin gerektirdiğinden fazla TL ödenmektedir; **TL değerinin altındadır** (ucuzdur).',
        'Para, banka ve dış ekonomi: satın alma gücü paritesi',
    ),
    # düzey 2
    '0053': patch(
        "Mundell'in imkânsız üçlemesine göre bir ülkenin aynı anda sahip olamayacağı üç hedef aşağıdakilerden hangisinde doğru verilmiştir?",
        {
            'A': 'Sabit kur, serbest sermaye hareketleri, bağımsız para politikası',
            'B': 'Esnek kur, cari fazla, düşük enflasyon',
            'C': 'Serbest sermaye hareketleri, düşük faiz, yüksek büyüme ve cari fazla',
            'D': 'Sabit kur, dengeli bütçe, tam istihdam ve düşük enflasyon',
            'E': 'Serbest ticaret, esnek kur, dış borçsuzluk',
        },
        'A',
        '**İmkânsız üçlemeye** göre bir ülke sabit kur, sermaye hareketlerinin serbestliği ve bağımsız para politikasından ancak ikisini aynı anda seçebilir. Örneğin sermaye serbestken kur sabit tutulursa faiz, kuru korumaya bağlanır ve para politikası bağımsızlığını yitirir.',
        'Para, banka ve dış ekonomi: imkânsız üçleme',
    ),
    # düzey 2
    '0054': patch(
        'Esnek kur rejimi uygulanan bir ülkede yabancı yatırımcıların ülkeden hızla çıkması döviz piyasasında aşağıdakilerden hangisine yol açar?',
        {
            'A': 'Döviz talebi azalır ve ulusal para değer kazanır',
            'B': 'Döviz talebi artar ve ulusal para değer kaybeder',
            'C': 'Merkez bankası döviz rezervleri artar',
            'D': 'Nominal kur sabit kalır, faizler düşer',
            'E': 'Döviz arzı artar ve ulusal para değer kazanır',
        },
        'B',
        'Yatırımcılar varlıklarını satıp dövize çevirdiğinde **döviz talebi artar**; esnek kurda bu talep artışı döviz kurunu yükseltir ve **ulusal para değer kaybeder**. Sabit kurda ise merkez bankası kuru korumak için rezerv satmak zorunda kalırdı.',
        'Para, banka ve dış ekonomi: esnek kur',
    ),
    # düzey 2
    '0055': patch(
        "İkinci Dünya Savaşı sonrasında kurulan ve 1970'lerin başına kadar süren uluslararası para sisteminin temel özelliği aşağıdakilerden hangisidir?",
        {
            'A': 'Döviz kurlarının DTÖ kararlarıyla belirlenmesi',
            'B': 'Başlıca paraların piyasada dalgalanmaya bırakılması',
            'C': 'Ülkelerin altın standardına tek başına dönmesi',
            'D': 'Doların altına, diğer paraların dolara sabit oranla bağlanması',
            'E': "Avrupa'da tek para birimine geçilmesi",
        },
        'D',
        "**Bretton Woods sisteminde** ABD doları sabit bir fiyattan (ons başına 35 dolar) altına çevrilebiliyordu; diğer paralar dolara sabit fakat ayarlanabilir kurlarla bağlandı. IMF ve Dünya Bankası bu sistem içinde kuruldu; doların altına çevrilebilirliğinin 1971'de askıya alınmasıyla sistem çöktü.",
        'Para, banka ve dış ekonomi: Bretton Woods',
    ),
    # düzey 2
    '0056': patch(
        'Merkez bankasının son kredi mercii işlevine ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Ödeme gücünü yitirmiş bankaların sermayesini tamamlamayı amaçlar.\n\nII. Panik nedeniyle likidite sıkıntısına düşen bankalara kredi sağlar.\n\nIII. Banka iflasında mevduat sahiplerine sigortalı tutarı öder.',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız II',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'B',
        '**Son kredi mercii** işlevi, ödeme gücü olan ancak geçici likidite sıkıntısı yaşayan bankalara genellikle teminat karşılığında kredi sağlanmasıdır (II). Ödeme gücünü yitirmiş bankaların sermayesinin tamamlanması (I) bu işlevin amacı değildir; iflasta mevduat sahiplerine ödeme (III) ise **mevduat sigortası** sisteminin görevidir.',
        'Para, banka ve dış ekonomi: son kredi mercii',
    ),
    # düzey 1
    '0057': patch(
        'Merkez bankasının para basma yetkisini kullanarak elde ettiği ve paranın satın alma gücü ile üretim maliyeti arasındaki farktan doğan gelir aşağıdakilerden hangisidir?',
        {
            'A': 'Kaldıraç',
            'B': 'Kupon',
            'C': 'Arbitraj',
            'D': 'Spread',
            'E': 'Senyoraj',
        },
        'E',
        '**Senyoraj**, para basma yetkisinden doğan gelirdir; merkez bankası maliyeti çok düşük olan parayı ihraç ederek karşılığında faiz getirili varlık edinir. **Arbitraj** ise fiyat farklarından risksiz kazanç sağlama işlemidir.',
        'Para, banka ve dış ekonomi: para ve banka',
    ),
    # düzey 2
    '0058': patch(
        "Mundell'in optimum para alanı kuramına göre aşağıdakilerden hangileri ortak para birimine geçişin maliyetini azaltır?\n\nI. Emeğin bölgeler arasında yüksek hareketliliği\n\nII. Ücret ve fiyatların esnekliği\n\nIII. Üye ülkelerin birbirinden farklı (asimetrik) şoklarla karşılaşması\n\nIV. Üyeler arasında yoğun ticari ilişkiler",
        {
            'A': 'I, II ve IV',
            'B': 'I, II, III ve IV',
            'C': 'I ve IV',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'A',
        'Ortak para, bağımsız kur ve para politikasından vazgeçmek demektir. Emek hareketliliği (I) ve ücret-fiyat esnekliği (II) şoklara kur olmadan uyum sağlamayı kolaylaştırır; yoğun ticaret (IV) ortak paranın işlem maliyeti kazancını büyütür. Asimetrik şoklar (III) ise ortak para politikasının üyelere uymamasına yol açarak maliyeti **artırır**.',
        'Para, banka ve dış ekonomi: optimum para alanı',
    ),
    # düzey 2
    '0059': patch(
        'Esnek (dalgalı) kur rejimine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Dış şokların bir kısmı kur hareketleriyle emilir',
            'B': 'Kur, döviz piyasasında arz ve talebe göre oluşur',
            'C': 'Merkez bankasının kuru sabit tutmasını gerektirir',
            'D': 'Para politikasına görece bağımsızlık alanı tanır',
            'E': 'Kur oynaklığı dış ticarette belirsizlik ve kur riski yaratabilir',
        },
        'C',
        'Esnek kurda kur piyasada arz ve talebe göre oluşur, dış şokların bir kısmı kur hareketleriyle karşılanır ve para politikası iç hedeflere yönelebilir; buna karşılık kur oynaklığı dış ticarette belirsizlik yaratabilir. Merkez bankası zaman zaman müdahale edebilse de kuru sabit tutma yükümlülüğü **sabit kur** rejimine aittir.',
        'Para, banka ve dış ekonomi: esnek kur rejimi',
    ),
    # düzey 2
    '0060': patch(
        'Yoğun sermaye girişiyle karşılaşan ve kuru korumak için piyasadan döviz satın alan bir merkez bankası, bu alımların para arzını artırıcı etkisini gidermek için aşağıdakilerden hangisini yapar?',
        {
            'A': 'Politika faizini indirir',
            'B': 'Bankalara reeskont kredisi açar',
            'C': 'Açık piyasada devlet tahvili satar',
            'D': 'Açık piyasada devlet tahvili satın alır',
            'E': 'Zorunlu karşılık oranlarını düşürür',
        },
        'C',
        'Döviz alımı karşılığında piyasaya verilen ulusal para, parasal tabanı artırır. Merkez bankası bu etkiyi nötrlemek için açık piyasada **tahvil satarak** fazla likiditeyi geri çeker; bu işleme **sterilizasyon** denir. Diğer seçenekler likiditeyi daha da artırır.',
        'Para, banka ve dış ekonomi: sterilizasyon',
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
    print(f"1 paket / {len(PATCHES)} soru ('Para, Banka ve Dış Ekonomi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
