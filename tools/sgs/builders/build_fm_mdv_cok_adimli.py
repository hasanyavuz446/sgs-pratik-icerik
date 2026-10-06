#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Maddi Duran Varliklar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gercek SGS finansal muhasebe profiline (376 soru; medyan kok 270, kokte 3+ tutar %35, olumsuz %16) gore sifirdan yazildi. Eski paket medyan kok 179, 3+ tutar %15, olumsuz %3 idi ve 15 TMS 16 sorusu tasiyordu (TMS 16 kendi paketinde). VUK/THP agirlikli: amortisman yontemleri ve AB->normal gecis, kist amortisman, yenileme fonu (VUK 328) olusumu ve mahsubu, sigorta/hurda/kayip cikislari, avans mahsubu, yapilmakta olan yatirimlar, satis kar/zarar kayitlari. Kayit sorulari gercek sinav kalibinda ('hangi hesabin kullanimi dogrudur/yanlistir', 'kayitta hangisi yer almaz'). Tutarlar modulde hesaplandi ve bagimsiz olarak ikinci kez dogrulandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: VUK m. 262, 269-272, 313-320, 328-329 · Tekduzen Hesap Plani (25 grubu, 257, 259, 549, 679, 689) · 1 Sira No'lu MSUGT
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/finansal_muhasebe/maddi_duran_varliklar.json"
STYLE_REF = 'SGS Finansal Muhasebe (çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "finmuh-mdv-gen-"


def patch(stem, options, answer, solution, ref='VUK m. 313-320'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        "İşletme üretimde kullanmak üzere liste fiyatı 480.000 ₺ olan bir makineyi fatura üzerinde %5 ticari iskontoyla satın almıştır (KDV %20). Makinenin fabrikaya taşınması için 12.000 ₺, montajı için 18.000 ₺ ve kullanıma hazır hâle getirilmeden önceki deneme üretimi için 6.000 ₺ ödenmiştir. Makine kullanılmaya başlandıktan sonra operatörlerin eğitimi için 5.000 ₺ ve ilk ayın elektrik gideri olarak 3.000 ₺ harcanmıştır. Buna göre makinenin maliyet bedeli kaç ₺'dir?",
        {
            'A': '590.400 ₺',
            'B': '497.000 ₺',
            'C': '500.000 ₺',
            'D': '492.000 ₺',
            'E': '516.000 ₺',
        },
        'D',
        'Alış bedeli = 480.000 × %95 = 456.000 ₺. Kullanıma hazır hâle getirene kadarki nakliye, montaj ve deneme üretimi maliyete eklenir: 456.000 + 12.000 + 18.000 + 6.000 = **492.000 ₺**. Kullanıma başladıktan sonraki eğitim ve elektrik dönem gideridir; indirilecek KDV maliyete girmez; ticari iskonto alış bedelinden düşülür.',
        "VUK m. 262, 269; 1 Sıra No'lu MSUGT (MDV)",
    ),
    # düzey 3
    '0002': patch(
        "İşletme fabrika kurmak amacıyla üzerinde kullanılamaz durumda eski bir yapı bulunan arsayı 800.000 ₺'ye satın almış, alım için emlak aracısına 20.000 ₺ komisyon ödemiştir. Eski yapı 40.000 ₺ harcanarak yıktırılmış, yıkımdan çıkan enkaz 15.000 ₺'ye satılmıştır. Buna göre arsanın maliyet bedeli kaç ₺'dir?",
        {
            'A': '845.000 ₺',
            'B': '830.000 ₺',
            'C': '825.000 ₺',
            'D': '805.000 ₺',
            'E': '875.000 ₺',
        },
        'A',
        'Arsayı amaçlanan kullanıma hazırlamak için katlanılan yıkım gideri arsanın maliyetine eklenir, enkaz satış geliri bu maliyetten düşülür; alım komisyonu da maliyet unsurudur: 800.000 + 40.000 − 15.000 + 20.000 = **845.000 ₺**. Arsa amortismana tabi olmadığından bu tutar varlık elden çıkarılana kadar aktifte kalır.',
        "VUK m. 270; 1 Sıra No'lu MSUGT (MDV maliyet unsurları)",
    ),
    # düzey 2
    '0003': patch(
        "Üretimde kullanılan bir makineye yıl içinde iki harcama yapılmıştır: makinenin üretim kapasitesini kalıcı olarak artıran 60.000 ₺'lik revizyon ve makinenin mevcut durumunu korumaya yönelik 8.000 ₺'lik olağan bakım. Harcamalar bankadan ödenmiştir (KDV ihmal). Bu harcamaların muhasebeleştirilmesiyle ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': "İkisi de 253'e eklenerek amortismana tabi tutulur",
            'B': "Revizyon 253'e eklenir, bakım 730'a gider yazılır",
            'C': "Revizyon 257'nin borcuna yazılarak amortismanı azaltır",
            'D': "Revizyon 730'a gider yazılır, bakım 253'e eklenir",
            'E': "İkisi de 730'a gider olarak yazılır",
        },
        'B',
        "Varlığın kapasitesini, verimini veya ömrünü artıran harcamalar maliyete eklenir (aktifleştirilir) ve kalan süre içinde amortismana tabi tutulur: 60.000 ₺ 253'ün borcuna. Mevcut durumu koruyan olağan bakım-onarım dönem gideridir: 8.000 ₺ üretimle ilgili olduğundan 730 Genel Üretim Giderleri'ne.",
        'VUK m. 272; THP 253, 730',
    ),
    # düzey 3
    '0004': patch(
        "İşletme yılbaşında 400.000 ₺'ye aldığı ve faydalı ömrü 5 yıl olan bir makine için azalan bakiyeler yöntemini uygulamış ve üç yıl boyunca amortisman ayırmıştır. Makine dördüncü yılın başında 150.000 ₺ + %20 KDV bedelle peşin satılmıştır. Satış yılında amortisman ayrılmamıştır.\n\nBuna göre makinenin satışından doğan kâr kaç ₺'dir?",
        {
            'A': '6.000',
            'B': '86.400',
            'C': '63.600',
            'D': '30.000',
            'E': '53.600',
        },
        'C',
        "Azalan bakiyeler oranı normal oranın iki katıdır: %20 × 2 = %40. Amortismanlar: 1. yıl 160.000 ₺, 2. yıl 240.000 × %40 = 96.000 ₺, 3. yıl 144.000 × %40 = 57.600 ₺; birikmiş 313.600 ₺. Net defter değeri 86.400 ₺; satış kârı 150.000 − 86.400 = 63.600 ₺ (679). KDV satış bedelinin parçası değildir, 391'e yazılır.",
        'VUK m. 316',
    ),
    # düzey 2
    '0005': patch(
        "Bir işletme faydalı ömrü 3 yıl olarak belirlenmiş bir bilgisayar sistemi için azalan bakiyeler yöntemini seçmiştir. Normal amortisman oranı %33,33'tür. Buna göre uygulanacak azalan bakiyeler oranı yüzde kaçtır?",
        {
            'A': '%33,33',
            'B': '%66,67',
            'C': '%40',
            'D': '%60',
            'E': '%50',
        },
        'E',
        "Azalan bakiyeler oranı normal oranın iki katıdır; ancak VUK m. 316 uyarınca bu oran **%50'yi geçemez**. %33,33 × 2 = %66,67 sınırı aştığından **%50** uygulanır.",
        'VUK m. 316',
    ),
    # düzey 2
    '0006': patch(
        "Azalan bakiyeler yöntemi uygulanan bir makinenin faydalı ömrünün son yılına gelinmiştir. Makinenin bu yılın başındaki net defter değeri 21.600 ₺'dir. Bu yıl için amortisman nasıl ayrılır?",
        {
            'A': 'Maliyet bedeli üzerinden normal oran uygulanır',
            'B': "Kalan 21.600 ₺'nin tamamı amortisman olarak ayrılır",
            'C': 'Kalan değer iz bedeli olarak aktifte bırakılır',
            'D': 'Son yılda amortisman ayrılmaz',
            'E': 'Kalan değere azalan bakiyeler oranı uygulanır',
        },
        'B',
        'Azalan bakiyeler yönteminde her yıl oran kalan değere uygulandığından değer sıfıra inmez; bu nedenle **faydalı ömrün son yılında kalan değerin tamamı** amortisman olarak ayrılır.',
        'VUK m. 316',
    ),
    # düzey 3
    '0007': patch(
        "İşletme yönetim binası olarak kullanmak üzere üzerinde bina bulunan bir gayrimenkulü 500.000 ₺'ye satın almıştır. Bedelin 100.000 ₺'si arsaya, kalanı binaya isabet etmektedir. Binanın faydalı ömrü 50 yıl olup normal amortisman uygulanmaktadır. Buna göre yıllık amortisman tutarı kaç ₺'dir?",
        {
            'A': '16.000 ₺',
            'B': '10.000 ₺',
            'C': '14.000 ₺',
            'D': '8.000 ₺',
            'E': '12.000 ₺',
        },
        'D',
        'Arsa (250) amortismana tabi değildir; yalnız bina (252) amortismana tabidir: (500.000 − 100.000) / 50 = **8.000 ₺**.',
        'VUK m. 315; THP 250, 252',
    ),
    # düzey 3
    '0008': patch(
        'Kayıtlı değeri 250.000 ₺ ve birikmiş amortismanı 150.000 ₺ olan bir üretim makinesi çıkan yangında tamamen kullanılamaz hâle gelmiştir. Sigorta şirketi 120.000 ₺ tazminat ödeyeceğini bildirmiş, işletme tazminat farkını yenileme fonuna almamaya karar vermiştir. Buna göre yapılacak kayıtta alacak tarafına yazılacak hesaplar aşağıdakilerden hangisidir?',
        {
            'A': '253 250.000 ₺ ve 689 20.000 ₺',
            'B': '257 150.000 ₺ ve 679 20.000 ₺',
            'C': '253 250.000 ₺ ve 679 20.000 ₺',
            'D': '253 250.000 ₺ ve 136 120.000 ₺',
            'E': '253 100.000 ₺ ve 679 20.000 ₺',
        },
        'C',
        "Kayıt: 136 Diğer Çeşitli Alacaklar (borç) 120.000 + 257 Birikmiş Amortismanlar (borç) 150.000 / 253 Tesis, Makine ve Cihazlar (alacak) 250.000 + 679 Diğer Olağandışı Gelir ve Kârlar (alacak) 20.000. Net değer 100.000 ₺, tazminat 120.000 ₺ olduğundan fark kârdır. Tazminat alacağı 136'nın borcuna, birikmiş amortisman 257'nin borcuna yazılır.",
        'THP 136 Diğer Çeşitli Alacaklar; 679; VUK m. 329',
    ),
    # düzey 3
    '0009': patch(
        "Maliyet bedeli 300.000 ₺ ve faydalı ömrü 10 yıl olan bir makine için normal amortisman yöntemiyle dört tam yıl amortisman ayrılmıştır. Beşinci yıl içinde makine 200.000 ₺'ye (KDV hariç) satılmıştır. Buna göre satış sonucu aşağıdakilerden hangisidir?",
        {
            'A': '20.000 ₺ zarar',
            'B': '80.000 ₺ kâr',
            'C': '50.000 ₺ kâr',
            'D': '100.000 ₺ zarar',
            'E': '20.000 ₺ kâr',
        },
        'E',
        'Birikmiş amortisman 4 × 30.000 = 120.000 ₺; net defter değeri 180.000 ₺. Satış yılında amortisman ayrılmaz. Kâr 200.000 − 180.000 = **20.000 ₺** (679).',
        'VUK m. 315; THP 679',
    ),
    # düzey 2
    '0010': patch(
        'Bir işletme, yenileme amacıyla sattığı makinenin kârını 549 Özel Fonlar hesabına almıştır. Aradan üç yıl geçmesine rağmen yeni bir varlık alınmamıştır ve alınmasından da vazgeçilmiştir. Buna göre fonla ilgili yapılacak işlem aşağıdakilerden hangisidir?',
        {
            'A': "Fon 549'un borcuna yazılarak 679 aracılığıyla kâra eklenir",
            'B': "Fon 522 MDV Yeniden Değerleme Artışları'na aktarılır",
            'C': "Fon sermayeye eklenerek 500'ün alacağına yazılır",
            'D': "Fon 257'nin alacağına yazılarak amortismana eklenir",
            'E': "Fon süresiz olarak 549'da bekletilir",
        },
        'A',
        'VUK m. 328 uyarınca yenileme fonu üç yıl içinde kullanılmazsa veya yenilemeden vazgeçilirse **kâra eklenir**: 549 Özel Fonlar (borç) / 679 Diğer Olağandışı Gelir ve Kârlar (alacak). Böylece ertelenmiş kâr vergilendirilir.',
        'VUK m. 328',
    ),
    # düzey 3
    '0011': patch(
        'Yenileme fonu uygulaması ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Fon, yenilenmek amacıyla satılan varlığın satış kârından ayrılır.\n\nII. Fon, alınan yeni varlığın amortismanına tahsis edilir.\n\nIII. Fon, varlığın satıldığı yılın gelir tablosunda olağandışı gelir olarak gösterilir.',
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'Yalnız I',
            'D': 'I, II ve III',
            'E': 'Yalnız II',
        },
        'B',
        "I ve II doğrudur. III yanlıştır: yenileme amacıyla satışta kâr gelir tablosuna aktarılmaz, pasifte 549 Özel Fonlar'da bekletilir; ancak üç yıl içinde kullanılmazsa kâra eklenir.",
        'VUK m. 328',
    ),
    # düzey 2
    '0012': patch(
        'Aşağıdaki maddi duran varlıklardan hangileri amortismana tabidir?\n\nI. İşletmenin fabrika arsası\n\nII. Yönetim binası\n\nIII. Üretim makinesi',
        {
            'A': 'Yalnız I',
            'B': 'I, II ve III',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'Yalnız III',
        },
        'C',
        'Arsalar süreklidir, aşınıp yıpranmaz; amortismana tabi değildir. **Bina ve makine** kullanımla değer kaybeder ve amortismana tabidir.',
        'VUK m. 313-315',
    ),
    # düzey 2
    '0013': patch(
        'Bir işletme dönem içinde kullandığı makineler için yıl sonunda amortisman ayırmamış, makinelerin maliyetinin tamamını satıldıkları yılda gider yazmayı tercih etmiştir. Bu uygulama aşağıdaki temel kavramlardan hangisine aykırıdır?',
        {
            'A': 'Parayla ölçülme',
            'B': 'Sosyal sorumluluk',
            'C': 'Kişilik',
            'D': 'İşletmenin sürekliliği',
            'E': 'Dönemsellik',
        },
        'E',
        "Dönemsellik kavramı gelir ve giderlerin ilgili olduğu dönemde tahakkuk ettirilmesini gerektirir. MDV'nin maliyeti kullanıldığı dönemlere **amortisman yoluyla** dağıtılmalıdır; tamamını satış yılında gider yazmak dönemselliğe aykırıdır.",
        'Muhasebenin temel kavramları (dönemsellik)',
    ),
    # düzey 2
    '0014': patch(
        'Önceki dönemlerde amortisman ayrılmış bir makine satılmaktadır. Satış kaydında makineye ait 257 Birikmiş Amortismanlar hesabının kalanı ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Alacaklandırılarak kapatılır',
            'B': 'Satıştan sonra da aktifte kalır',
            'C': "549'a aktarılarak fon olarak bekletilir",
            'D': 'Borçlandırılarak kapatılır',
            'E': "689'a aktarılarak gider yazılır",
        },
        'D',
        "Satılan varlığın maliyeti ilgili MDV hesabının alacağına yazılırken, o varlığa ait birikmiş amortisman **257'nin borcuna** yazılarak kapatılır; aradaki fark satış bedeliyle karşılaştırılarak kâr veya zarar bulunur.",
        'THP 257 Birikmiş Amortismanlar',
    ),
    # düzey 3
    '0015': patch(
        'Maddi duran varlıklarla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Normal amortisman yönteminden azalan bakiyeler yöntemine geçilebilir.\n\nII. Satış yılında satılan varlık için amortisman ayrılmaz.\n\nIII. Yenileme fonu yeni varlık için ayrılan amortismana tahsis edilir.',
        {
            'A': 'II ve III',
            'B': 'I, II ve III',
            'C': 'Yalnız III',
            'D': 'I ve II',
            'E': 'Yalnız II',
        },
        'A',
        "II ve III doğrudur. I yanlıştır: VUK'ta azalan bakiyelerden normal yönteme geçilebilir, **tersi mümkün değildir**.",
        'VUK m. 313, 316, 328',
    ),
    # düzey 3
    '0016': patch(
        'İşletme kayıtlı değeri 160.000 ₺, birikmiş amortismanı 100.000 ₺ olan bir makineyi 70.000 ₺ + %20 KDV bedelle satmış, bedel banka hesabına yatırılmıştır (yenileme fonu ayrılmayacaktır). Buna göre satış kaydında aşağıdakilerden hangisi yer almaz?',
        {
            'A': '679 Diğer Olağandışı Gelir ve Kârlar hesabı 10.000 ₺ alacaklandırılır',
            'B': '257 Birikmiş Amortismanlar hesabı 100.000 ₺ borçlandırılır',
            'C': '102 Bankalar hesabı 84.000 ₺ borçlandırılır',
            'D': '689 Diğer Olağandışı Gider ve Zararlar hesabı 10.000 ₺ borçlandırılır',
            'E': '391 Hesaplanan KDV hesabı 14.000 ₺ alacaklandırılır',
        },
        'D',
        'Net değer 60.000 ₺ < satış bedeli 70.000 ₺ olduğundan **kâr** doğar: 102 Bankalar (borç) 84.000 + 257 Birikmiş Amortismanlar (borç) 100.000 / 253 Tesis, Makine ve Cihazlar (alacak) 160.000 + 391 Hesaplanan KDV (alacak) 14.000 + 679 Diğer Olağandışı Gelir ve Kârlar (alacak) 10.000. Zarar hesabı 689 kullanılmaz.',
        'THP 102, 257, 253, 391, 679',
    ),
    # düzey 2
    '0017': patch(
        'Bir üretim işletmesi yıl içinde makineleriyle ilgili şu harcamaları yapmıştır: kapasiteyi artıran ilave ünite, makinenin ömrünü önemli ölçüde uzatan motor değişimi, montaj ve ayar gideri, olağan yağlama ve periyodik bakım, yeni makinenin fabrikaya nakliyesi. Buna göre aşağıdakilerden hangisi aktifleştirilmez?',
        {
            'A': 'Yeni makinenin nakliyesi',
            'B': 'Montaj ve ayar gideri',
            'C': 'Ömrü uzatan motor değişimi',
            'D': 'Kapasiteyi kalıcı olarak artıran ilave ünite',
            'E': 'Olağan yağlama ve periyodik bakım',
        },
        'E',
        'Kapasite veya ömrü artıran harcamalar ile varlığı kullanıma hazırlayan nakliye ve montaj maliyete eklenir. **Olağan bakım** mevcut durumu korur; dönem gideridir (730).',
        'VUK m. 272; THP 730',
    ),
    # düzey 3
    '0018': patch(
        'İşletme 250.000 ₺ + %20 KDV bedelli bir makine için satıcıya bankadan 50.000 ₺ avans ödemiştir. Makine teslim alınmış, avans mahsup edildikten sonra kalan borç banka havalesiyle ödenmiştir. Buna göre teslim kaydıyla ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': '191 İndirilecek KDV hesabı 50.000 ₺ borçlandırılır',
            'B': '102 Bankalar hesabı 300.000 ₺ alacaklandırılır',
            'C': '253 Tesis, Makine ve Cihazlar hesabı 250.000 ₺ borçlandırılır',
            'D': "Borç ve alacak toplamları 300.000 ₺'dir",
            'E': '259 Verilen Avanslar hesabı 50.000 ₺ alacaklandırılır',
        },
        'B',
        'Kayıt: 253 Tesis, Makine ve Cihazlar (borç) 250.000 + 191 İndirilecek KDV (borç) 50.000 / 259 Verilen Avanslar (alacak) 50.000 + 102 Bankalar (alacak) **250.000**. Bankadan ödenen tutar avans düşüldükten sonraki kısımdır; KDV dâhil toplam değildir.',
        'THP 259, 253, 191, 102',
    ),
    # düzey 2
    '0019': patch(
        "İşletme 1 Ekim'de satın aldığı binek otomobil için ilk yıl kıst amortisman ayırmıştır. Faydalı ömür 5 yıl olup normal amortisman uygulanmaktadır. İlk yıl ayrılamayan dokuz aylık amortisman tutarıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Beş yıla eşit dağıtılarak her yıla eklenir',
            'B': 'İkinci yılın amortismanına eklenir',
            'C': 'Faydalı ömrün sonunu izleyen yılda ayrılır',
            'D': "İlk yılın sonunda 689'a zarar yazılır",
            'E': "Gider yazılmaz, 549'a aktarılır",
        },
        'C',
        'VUK m. 320 uyarınca binek otomobillerde ilk yıl kıst amortisman ayrılır; ilk yıl ayrılamayan kısım **faydalı ömrün sonunu izleyen yılda** (son yıl) amortisman olarak ayrılır. Böylece maliyetin tamamı itfa edilir.',
        'VUK m. 320',
    ),
    # düzey 3
    '0020': patch(
        'Kayıtlı değeri 320.000 ₺, birikmiş amortismanı 200.000 ₺ olan bir kamyon 100.000 ₺ + %20 KDV bedelle satılmış, bedelin tamamı için alıcıdan üç ay vadeli senet alınmıştır. Buna göre satış kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '121 Alacak Senetleri hesabı 120.000 ₺ borçlandırılır',
            'B': '121 Alacak Senetleri hesabı 100.000 ₺ borçlandırılır',
            'C': '679 Diğer Olağandışı Gelir ve Kârlar hesabı 20.000 ₺ alacaklandırılır',
            'D': '257 Birikmiş Amortismanlar hesabı 200.000 ₺ alacaklandırılır',
            'E': '254 Taşıtlar hesabı 120.000 ₺ alacaklandırılır',
        },
        'A',
        'Net değer 120.000 ₺ > satış bedeli 100.000 ₺; 20.000 ₺ **zarar** (689). Kayıt: 121 Alacak Senetleri (borç) **120.000** + 257 Birikmiş Amortismanlar (borç) 200.000 + 689 Diğer Olağandışı Gider ve Zararlar (borç) 20.000 / 254 Taşıtlar (alacak) 320.000 + 391 Hesaplanan KDV (alacak) 20.000. Senet KDV dâhil tutar üzerinden alınır.',
        'THP 121 Alacak Senetleri; 689',
    ),
    # düzey 3
    '0021': patch(
        'İşletme 300.000 ₺ + %20 KDV bedelli bir üretim makinesi sipariş etmiş ve sipariş sırasında satıcıya banka hesabından 60.000 ₺ avans göndermiştir. Makine teslim alındığında avans mahsup edilmiş, kalan tutar için işletme kendi keşide ettiği çeki satıcıya vermiştir. Teslim tarihinde yapılacak kayıtla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '259 Verilen Avanslar hesabı 60.000 ₺ borçlandırılır',
            'B': '259 Verilen Avanslar hesabı 60.000 ₺ alacaklandırılır',
            'C': '191 İndirilecek KDV hesabı 72.000 ₺ borçlandırılır',
            'D': '103 Verilen Çekler ve Ödeme Emirleri hesabı 360.000 ₺ alacaklandırılır',
            'E': '253 Tesis, Makine ve Cihazlar hesabı 360.000 ₺ borçlandırılır',
        },
        'B',
        "Kayıt: 253 Tesis, Makine ve Cihazlar (borç) 300.000 + 191 İndirilecek KDV (borç) 60.000 / 259 Verilen Avanslar (alacak) 60.000 + 103 Verilen Çekler ve Ödeme Emirleri (alacak) 300.000. Avans teslimde **259'un alacağına** yazılarak kapatılır; çekle ödenen tutar KDV dâhil toplamdan avans düşülerek bulunur: 360.000 − 60.000 = 300.000 ₺. Makine KDV hariç bedelle aktifleştirilir.",
        'THP 259 Verilen Avanslar; 103 Verilen Çekler',
    ),
    # düzey 2
    '0022': patch(
        'Bir işletme üretim hattı için yurt dışından makine ithal etmiştir. İthalat sırasında ve sonrasında şu harcamalar yapılmıştır: gümrük vergisi, fabrikaya kadar nakliye, montaj ve ayar, ithalatta ödenen ve indirim konusu yapılacak KDV, kullanıma hazır hâle gelmeden önceki deneme çalışması. Buna göre aşağıdakilerden hangisi makinenin maliyet bedeline eklenmez?',
        {
            'A': 'Fabrikaya kadar nakliye',
            'B': 'Kullanım öncesi deneme çalışması',
            'C': 'İndirim konusu yapılacak KDV',
            'D': 'Gümrük vergisi',
            'E': 'Montaj ve ayar gideri',
        },
        'C',
        "İndirim konusu yapılacak KDV **191 İndirilecek KDV**'de izlenir ve hesaplanan KDV'den indirilir; maliyete girmez. Gümrük vergisi, nakliye, montaj ve kullanım öncesi deneme varlığı kullanıma hazır hâle getirmek için katlanılan maliyetlerdir.",
        'VUK m. 262, 269; KDV Kanunu m. 29',
    ),
    # düzey 3
    '0023': patch(
        "İşletme yönetim biriminde kullanmak üzere 1 Eylül'de 360.000 ₺'ye (KDV hariç) bir binek otomobil satın almıştır. Faydalı ömrü 5 yıl olan otomobil için normal amortisman yöntemi uygulanacaktır. Buna göre alım yılında ayrılacak amortisman tutarı kaç ₺'dir?",
        {
            'A': '48.000 ₺',
            'B': '72.000 ₺',
            'C': '30.000 ₺',
            'D': '24.000 ₺',
            'E': '18.000 ₺',
        },
        'D',
        'Binek otomobillerde ilk yıl amortismanı **kıst** (ay esasına göre) ayrılır. Yıllık amortisman 360.000 / 5 = 72.000 ₺; Eylül-Aralık 4 ay: 72.000 × 4/12 = **24.000 ₺**. Ayrılamayan kısım faydalı ömrün sonunda ayrılır.',
        'VUK m. 320 (binek otomobillerde kıst amortisman)',
    ),
    # düzey 2
    '0024': patch(
        'İşletme toplantı salonunda birlikte kullanılmak üzere tanesi 8.000 ₺ (KDV hariç) olan 4 adet koltuktan oluşan bir oturma grubu satın almıştır. Doğrudan gider yazılabilecek tutar sınırının bu dönem için 12.000 ₺ olduğu varsayılmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Her koltuk 8.000 ₺ olduğundan bedel doğrudan gider yazılabilir',
            'B': 'Koltuklardan üçü gider, biri 255 Demirbaşlar olarak kaydedilir',
            'C': 'Oturma grubu 153 Ticari Mallar hesabında izlenir',
            'D': "Bedel satın alma yılında 770'e, izleyen yıllarda 257'ye yazılır",
            'E': 'Toplam bedel sınırı aştığından amortismana tabidir',
        },
        'E',
        "VUK m. 313'e göre birlikte kullanılan veya bir bütünün parçası niteliğindeki kıymetlerde sınır, **toplam bedel** üzerinden değerlendirilir. 4 × 8.000 = 32.000 ₺ varsayılan sınırı aştığından oturma grubu 255 Demirbaşlar'a kaydedilip amortismana tabi tutulur.",
        'VUK m. 313',
    ),
    # düzey 3
    '0025': patch(
        "Maliyet bedeli 600.000 ₺ ve faydalı ömrü 5 yıl olan bir makine için ilk iki yıl azalan bakiyeler yöntemiyle amortisman ayrılmış, üçüncü yıldan itibaren normal amortisman yöntemine geçilmiştir. Buna göre üçüncü yıl ayrılacak amortisman tutarı kaç ₺'dir?",
        {
            'A': '72.000 ₺',
            'B': '120.000 ₺',
            'C': '108.000 ₺',
            'D': '86.400 ₺',
            'E': '43.200 ₺',
        },
        'A',
        '1. yıl 600.000 × %40 = 240.000 ₺; 2. yıl (600.000 − 240.000) × %40 = 144.000 ₺. Kalan değer 600.000 − 240.000 − 144.000 = 216.000 ₺. Normal yönteme geçişte kalan değer **kalan faydalı ömre** (3 yıl) eşit bölünür: 216.000 / 3 = **72.000 ₺**.',
        'VUK m. 316 (azalan bakiyelerden normal yönteme geçiş)',
    ),
    # düzey 3
    '0026': patch(
        "İşletmenin sahip olduğu binanın %60'ı üretim, %30'u yönetim ve %10'u pazarlama bölümlerince kullanılmaktadır. Binanın yıllık amortismanı 200.000 ₺'dir ve işletme 7/A seçeneğini uygulamaktadır. Dönem sonu amortisman kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '730 Genel Üretim Giderleri hesabı 60.000 ₺ borçlandırılır',
            'B': '760 Pazarlama Satış ve Dağıtım Giderleri hesabı 60.000 ₺ borçlandırılır',
            'C': '252 Binalar hesabı 200.000 ₺ alacaklandırılır',
            'D': '770 Genel Yönetim Giderleri hesabı 60.000 ₺ borçlandırılır',
            'E': '257 Birikmiş Amortismanlar hesabı 200.000 ₺ borçlandırılır',
        },
        'D',
        "Kayıt: 730 Genel Üretim Giderleri (borç) 120.000 + 770 Genel Yönetim Giderleri (borç) 60.000 + 760 Pazarlama Satış ve Dağıtım Giderleri (borç) 20.000 / 257 Birikmiş Amortismanlar (alacak) 200.000. Amortisman gideri kullanım yerine göre dağıtılır; karşılığı varlık hesabı değil, düzenleyici **257 Birikmiş Amortismanlar**'ın alacağıdır.",
        'THP 7/A seçeneği; 257 Birikmiş Amortismanlar',
    ),
    # düzey 3
    '0027': patch(
        'Kayıtlı değeri 400.000 ₺, birikmiş amortismanı 280.000 ₺ olan bir makine 150.000 ₺ + %20 KDV bedelle satılmış; karşılığında müşteriden çek alınmıştır (yenileme fonu ayrılmayacaktır). Satış kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '679 Diğer Olağandışı Gelir ve Kârlar hesabı 30.000 ₺ alacaklandırılır',
            'B': '391 Hesaplanan KDV hesabı 30.000 ₺ borçlandırılır',
            'C': '689 Diğer Olağandışı Gider ve Zararlar hesabı 30.000 ₺ borçlandırılır',
            'D': '257 Birikmiş Amortismanlar hesabı 280.000 ₺ alacaklandırılır',
            'E': '101 Alınan Çekler hesabı 150.000 ₺ borçlandırılır',
        },
        'A',
        "Net defter değeri 400.000 − 280.000 = 120.000 ₺; satış kârı 150.000 − 120.000 = 30.000 ₺. Kayıt: 101 Alınan Çekler (borç) 180.000 + 257 Birikmiş Amortismanlar (borç) 280.000 / 253 Tesis, Makine ve Cihazlar (alacak) 400.000 + 391 Hesaplanan KDV (alacak) 30.000 + 679 Diğer Olağandışı Gelir ve Kârlar (alacak) **30.000**. Birikmiş amortisman borçlandırılarak kapatılır, KDV 391'in alacağına yazılır.",
        'THP 679; 391 Hesaplanan KDV',
    ),
    # düzey 3
    '0028': patch(
        "Kayıtlı değeri 180.000 ₺ ve birikmiş amortismanı 126.000 ₺ olan bir pres makinesi teknik arıza nedeniyle kullanılamaz hâle gelmiş ve hurdacıya 10.000 ₺'ye peşin satılmıştır (KDV ihmal). Buna göre işletmenin gelir tablosuna yansıyacak zarar kaç ₺'dir?",
        {
            'A': '116.000 ₺',
            'B': '44.000 ₺',
            'C': '170.000 ₺',
            'D': '54.000 ₺',
            'E': '64.000 ₺',
        },
        'B',
        "Net defter değeri 180.000 − 126.000 = 54.000 ₺. Hurda satış bedeli düşülünce zarar 54.000 − 10.000 = **44.000 ₺** olur ve 689 Diğer Olağandışı Gider ve Zararlar'a yazılır.",
        'VUK m. 317; THP 689',
    ),
    # düzey 2
    '0029': patch(
        'Maliyet bedeli 75.000 ₺ ve birikmiş amortismanı 45.000 ₺ olan bir dizüstü bilgisayar personelin sorumluluğundayken kaybolmuştur. Net defter değerinin personelden tahsil edilmesine karar verilmiştir. Bu karara ilişkin kayıt aşağıdakilerden hangisidir?',
        {
            'A': '257 (borç) 45.000 + 689 (borç) 30.000 / 255 (alacak) 75.000',
            'B': '255 (borç) 75.000 / 257 (alacak) 45.000 + 135 (alacak) 30.000',
            'C': '257 (borç) 45.000 + 135 (borç) 30.000 / 255 (alacak) 75.000',
            'D': '135 (borç) 75.000 / 255 (alacak) 75.000',
            'E': '135 (borç) 30.000 / 257 (alacak) 30.000',
        },
        'C',
        "Varlık aktiften çıkarılırken maliyeti 255'in alacağına, birikmiş amortismanı 257'nin borcuna yazılır; personelden tahsil edilecek net değer (75.000 − 45.000 = 30.000 ₺) **135 Personelden Alacaklar**'ın borcuna yazılır. Tahsil kararı olduğu için zarar hesabı kullanılmaz.",
        'THP 135 Personelden Alacaklar',
    ),
    # düzey 3
    '0030': patch(
        "İşletme kayıtlı değeri 180.000 ₺, birikmiş amortismanı 120.000 ₺ olan bir makineyi yenilemek amacıyla 85.000 ₺'ye (KDV hariç) satmıştır. Satış kârı yenileme fonuna alınacaktır. Satış kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '522 MDV Yeniden Değerleme Artışları hesabı 25.000 ₺ alacaklandırılır',
            'B': '679 Diğer Olağandışı Gelir ve Kârlar hesabı 25.000 ₺ alacaklandırılır',
            'C': '549 Özel Fonlar hesabı 25.000 ₺ borçlandırılır',
            'D': '570 Geçmiş Yıllar Kârları hesabı 25.000 ₺ alacaklandırılır',
            'E': '549 Özel Fonlar hesabı 25.000 ₺ alacaklandırılır',
        },
        'E',
        "Net değer 60.000 ₺, kâr 85.000 − 60.000 = 25.000 ₺. Yenileme amacıyla satışta kâr gelir hesabı yerine pasifteki özkaynak hesabı **549 Özel Fonlar**'ın alacağına yazılır; fon yeni varlığın amortismanına mahsup edilir.",
        'VUK m. 328; THP 549 Özel Fonlar',
    ),
    # düzey 2
    '0031': patch(
        'Bir üretim işletmesinin bilançosunda aşağıdaki kalemler bulunmaktadır: fabrika binası, üretim bandı, yöneticilerin kullandığı binek otomobiller, satılmak üzere üretilmiş ürünler ve inşaatı süren depo. Buna göre aşağıdakilerden hangisi 25 Maddi Duran Varlıklar grubunda yer almaz?',
        {
            'A': 'Fabrika binası',
            'B': 'Yöneticilerin kullandığı binek otomobiller',
            'C': 'Satılmak üzere üretilmiş ürünler',
            'D': 'İnşaatı süren depo',
            'E': 'Üretim bandı',
        },
        'C',
        "Satılmak üzere üretilen ürünler **152 Mamuller** hesabında (15 Stoklar) izlenir. Bina 252'de, üretim bandı 253'te, binek otomobiller 254'te, inşaatı süren depo 258 Yapılmakta Olan Yatırımlar'da 25 grubundadır.",
        'THP 25 Maddi Duran Varlıklar',
    ),
    # düzey 2
    '0032': patch(
        'Bir işletmenin mizanında 257 Birikmiş Amortismanlar hesabının kalanı 340.000 ₺ olarak görünmektedir. Bu hesabın niteliği ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Pasif karakterli bir borç hesabıdır',
            'B': "Gider hesabı olup dönem sonunda 690 Dönem Kârı veya Zararı'na devredilir",
            'C': 'Özkaynak hesabı olup kâr dağıtımında kullanılır',
            'D': 'Aktifi düzenleyici bir hesaptır ve alacak kalanı verir',
            'E': 'Aktif karakterli olup borç kalanı verir',
        },
        'D',
        '257 Birikmiş Amortismanlar, ilgili MDV hesaplarının değerini düzenleyen **aktifi düzenleyici** (kontr aktif) hesaptır; bilançoda aktifte eksi olarak gösterilir ve alacak kalanı verir.',
        'THP 257 Birikmiş Amortismanlar',
    ),
    # düzey 1
    '0033': patch(
        "İşletme kendi kullanımı için bir üretim tesisi kurmaktadır ve tesis yıl sonunda henüz kullanıma hazır değildir. Yıl içinde müteahhide 900.000 ₺ hakediş ödenmiş, yatırımın finansmanı için kullanılan özel krediye ait 60.000 ₺ faiz tahakkuk etmiş, tesisin projelendirilmesi için mühendislik firmasına 40.000 ₺ ödenmiştir. Ayrıca temel atma töreni için 15.000 ₺ ve tesiste çalışacak personelin eğitimi için 10.000 ₺ harcanmıştır. KDV ihmal edilecektir.\n\nBuna göre yıl sonunda '258 Yapılmakta Olan Yatırımlar' hesabının kalanı kaç ₺'dir?",
        {
            'A': '1.000.000',
            'B': '1.025.000',
            'C': '940.000',
            'D': '1.015.000',
            'E': '960.000',
        },
        'A',
        "Tesis kullanıma hazır hâle gelene kadar onu bu duruma getiren harcamalar 258'de birikir: hakediş 900.000 ₺, yatırım dönemine ait kredi faizi 60.000 ₺ ve proje bedeli 40.000 ₺; toplam 1.000.000 ₺. Tören ve personel eğitimi tesisi kullanıma hazır hâle getiren harcamalar değildir, dönem gideridir.",
        'THP 258 Yapılmakta Olan Yatırımlar',
    ),
    # düzey 2
    '0034': patch(
        'Bir işletme demirbaşlarının faydalı ömürlerini ve amortisman oranlarını belirlemek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tüm varlıklara %20 oran uygulanır',
            'B': 'Faydalı ömürler Bakanlıkça ilan edilen listelere göre belirlenir',
            'C': 'Faydalı ömür satın alma bedeline göre belirlenir',
            'D': 'Faydalı ömürleri her işletme dilediği gibi belirler',
            'E': 'Faydalı ömür denetçinin onayıyla belirlenir',
        },
        'B',
        'VUK m. 315 uyarınca iktisadi kıymetlerin faydalı ömürleri ve amortisman oranları **Hazine ve Maliye Bakanlığınca ilan edilen listelerle** belirlenir; mükellef bu oranları uygular.',
        'VUK m. 315',
    ),
    # düzey 2
    '0035': patch(
        "İşletme kullanmadığı bir makineyi %20 KDV'li olarak satmış, aynı ay içinde yeni bir makineyi de %20 KDV'li olarak satın almıştır. Bu iki işlemin KDV'sinin kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': "İki işlemin KDV'si de 391'in alacağına yazılır",
            'B': "İki işlemin KDV'si de 191'in borcuna yazılır",
            'C': "KDV'ler makinelerin maliyetine eklenir, ayrıca kaydedilmez",
            'D': "Satıştaki KDV 191'in alacağına, alıştaki KDV 391'in borcuna yazılır",
            'E': "Satıştaki KDV 391'in alacağına, alıştaki KDV 191'in borcuna yazılır",
        },
        'E',
        "MDV satışında hesaplanan KDV **391 Hesaplanan KDV**'nin alacağına, alımında ödenen ve indirim konusu yapılacak KDV **191 İndirilecek KDV**'nin borcuna yazılır; ay sonunda mahsup edilir.",
        'THP 391 Hesaplanan KDV; 191 İndirilecek KDV',
    ),
    # düzey 3
    '0036': patch(
        'Amortisman uygulaması ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Azalan bakiyeler yönteminde oran her yıl kalan değere uygulanır.\n\nII. Normal amortisman yönteminde her yıl maliyet bedeli üzerinden eşit tutar ayrılır.\n\nIII. Ayrılan amortisman varlık hesabının alacağına yazılarak varlığın kayıtlı değeri doğrudan azaltılır.',
        {
            'A': 'I ve II',
            'B': 'I ve III',
            'C': 'II ve III',
            'D': 'Yalnız II',
            'E': 'Yalnız I',
        },
        'A',
        'I ve II doğrudur. III yanlıştır: amortisman varlık hesabı değil, düzenleyici **257 Birikmiş Amortismanlar** hesabının alacağına yazılır; varlığın kayıtlı değeri maliyetle kalır.',
        'VUK m. 315-316; THP 257',
    ),
    # düzey 3
    '0037': patch(
        'Kayıtlı değeri 220.000 ₺, birikmiş amortismanı 160.000 ₺ olan bir makine sel sonucu kullanılamaz hâle gelmiştir. Sigorta şirketi 45.000 ₺ tazminat ödeyeceğini bildirmiştir. Buna göre yapılacak kayıtta aşağıdakilerden hangisi yer almaz?',
        {
            'A': '689 Diğer Olağandışı Gider ve Zararlar hesabı 15.000 ₺ borçlandırılır',
            'B': '136 Diğer Çeşitli Alacaklar hesabı 45.000 ₺ borçlandırılır',
            'C': '257 Birikmiş Amortismanlar hesabı 160.000 ₺ borçlandırılır',
            'D': '679 Diğer Olağandışı Gelir ve Kârlar hesabı 15.000 ₺ alacaklandırılır',
            'E': '253 Tesis, Makine ve Cihazlar hesabı 220.000 ₺ alacaklandırılır',
        },
        'D',
        'Net değer 60.000 ₺, tazminat 45.000 ₺; fark **zarardır**: 136 Diğer Çeşitli Alacaklar (borç) 45.000 + 257 Birikmiş Amortismanlar (borç) 160.000 + 689 Diğer Olağandışı Gider ve Zararlar (borç) 15.000 / 253 Tesis, Makine ve Cihazlar (alacak) 220.000. Kâr hesabı 679 kullanılmaz.',
        'THP 136, 257, 253, 689',
    ),
    # düzey 2
    '0038': patch(
        'Bir işletme yenileme fonu uygulamasını değerlendirmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Fon, yenilenmek amacıyla satılan varlığın satış kârından ayrılır',
            'B': 'Üç yıl içinde kullanılmayan fon kâra eklenir',
            'C': 'Fon, satış yılının gelir tablosunda kâr olarak gösterilir',
            'D': 'Fon, yeni varlığın amortismanına tahsis edilir',
            'E': 'Fon, 549 Özel Fonlar hesabında izlenir',
        },
        'C',
        "Yenileme amacıyla satışta kâr satış yılında gelir yazılmaz; **549 Özel Fonlar**'da (özkaynak) bekletilir, yeni varlığın amortismanına tahsis edilir ve üç yıl içinde kullanılmazsa kâra eklenir.",
        'VUK m. 328-329',
    ),
    # düzey 3
    '0039': patch(
        "İşletme yenilemek amacıyla sattığı eski makinesinin 36.000 ₺ tutarındaki satış kârını 549 Özel Fonlar hesabına almıştır. İzleyen yılın başında 150.000 ₺'ye faydalı ömrü 5 yıl olan yeni bir üretim makinesi alınmış ve normal amortisman uygulanmıştır. Fon, yeni makinenin amortismanına tahsis edilmektedir. Buna göre yeni makinenin ikinci yıl amortisman kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '549 Özel Fonlar hesabı 6.000 ₺ alacaklandırılır',
            'B': '549 Özel Fonlar hesabı 30.000 ₺ borçlandırılır',
            'C': '730 Genel Üretim Giderleri hesabı 30.000 ₺ borçlandırılır',
            'D': '679 Diğer Olağandışı Gelir ve Kârlar hesabı 6.000 ₺ alacaklandırılır',
            'E': '549 Özel Fonlar hesabı 6.000 ₺ borçlandırılır',
        },
        'E',
        'Yıllık amortisman 150.000 / 5 = 30.000 ₺. 1. yıl amortismanın tamamı fondan karşılanır; fonda 36.000 − 30.000 = 6.000 ₺ kalır. 2. yıl kaydı: 549 Özel Fonlar (borç) **6.000** + 730 Genel Üretim Giderleri (borç) 24.000 / 257 Birikmiş Amortismanlar (alacak) 30.000.',
        'VUK m. 328',
    ),
    # düzey 2
    '0040': patch(
        'Yeni yönetim binası inşaatını üstlenen yüklenici 400.000 ₺ + %20 KDV tutarında hakediş faturası düzenlemiş, işletme bedeli banka havalesiyle ödemiştir. İnşaat sürmektedir. Buna göre hakediş kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '252 Binalar hesabı 400.000 ₺ borçlandırılır',
            'B': '258 Yapılmakta Olan Yatırımlar hesabı 400.000 ₺ borçlandırılır',
            'C': '258 Yapılmakta Olan Yatırımlar hesabı 480.000 ₺ borçlandırılır',
            'D': '191 İndirilecek KDV hesabı 80.000 ₺ alacaklandırılır',
            'E': '259 Verilen Avanslar hesabı 400.000 ₺ borçlandırılır',
        },
        'B',
        "İnşaat tamamlanmadığı için harcama **258 Yapılmakta Olan Yatırımlar**'da biriktirilir: 258 Yapılmakta Olan Yatırımlar (borç) 400.000 + 191 İndirilecek KDV (borç) 80.000 / 102 Bankalar (alacak) 480.000. KDV maliyete girmez; bina tamamlanınca 252'ye aktarılır.",
        'THP 258, 191, 102',
    ),
    # düzey 3
    '0041': patch(
        "İşletme 40.000 ₺ + %20 KDV bedelle büro mobilyası satın almıştır. Bedelin 10.000 ₺'lik kısmı kasadan ödenmiş, kalan tutar için daha önce müşterisinden aldığı bir çek satıcıya ciro edilmiştir. Buna göre aşağıdakilerden kayıtla ilgili hangisi yanlıştır?",
        {
            'A': '100 Kasa hesabı 10.000 ₺ alacaklandırılır',
            'B': '191 İndirilecek KDV hesabı 8.000 ₺ borçlandırılır',
            'C': "Kaydın borç ve alacak toplamları 48.000 ₺'dir",
            'D': '255 Demirbaşlar hesabı 40.000 ₺ borçlandırılır',
            'E': '103 Verilen Çekler ve Ödeme Emirleri hesabı 38.000 ₺ alacaklandırılır',
        },
        'E',
        "Kayıt: 255 Demirbaşlar (borç) 40.000 + 191 İndirilecek KDV (borç) 8.000 / 100 Kasa (alacak) 10.000 + 101 Alınan Çekler (alacak) 38.000. Müşteriden alınıp ciro edilen çek **101 Alınan Çekler**'in alacağına yazılır; 103 işletmenin kendi keşide ettiği çekler içindir.",
        'THP 101 Alınan Çekler; 255 Demirbaşlar',
    ),
    # düzey 2
    '0042': patch(
        'İşletmenin yeni fabrika binası inşaatı için yüklenici firmaya yıl içinde üç hakediş ödemesi yapılmıştır: 250.000 ₺, 400.000 ₺ ve 350.000 ₺ (KDV ayrıca kaydedilmiştir). İnşaat tamamlanmış ve bina geçici kabulle teslim alınarak kullanıma hazır hâle gelmiştir. Buna göre teslim alma kaydı aşağıdakilerden hangisidir?',
        {
            'A': '252 Binalar (borç) 1.000.000 / 258 Yapılmakta Olan Yatırımlar (alacak) 1.000.000',
            'B': '258 Yapılmakta Olan Yatırımlar (borç) 1.000.000 / 252 Binalar (alacak) 1.000.000',
            'C': '252 Binalar (borç) 1.000.000 / 259 Verilen Avanslar (alacak) 1.000.000',
            'D': '252 Binalar (borç) 350.000 / 258 Yapılmakta Olan Yatırımlar (alacak) 350.000',
            'E': '252 Binalar (borç) 1.000.000 / 102 Bankalar (alacak) 1.000.000',
        },
        'A',
        "Yapım süresince yapılan harcamalar **258 Yapılmakta Olan Yatırımlar**'da toplanır. Varlık kullanıma hazır hâle gelince toplam (250.000 + 400.000 + 350.000 = 1.000.000 ₺) 258'in alacağına yazılarak ilgili MDV hesabına (252 Binalar) aktarılır. Ödemeler zaten yapıldığı için bu aşamada banka hareketi yoktur.",
        'THP 258 Yapılmakta Olan Yatırımlar; 252 Binalar',
    ),
    # düzey 3
    '0043': patch(
        "İşletme üretimde kullanmak üzere 20 Aralık 2025'te 120.000 ₺'ye (KDV hariç) bir makine satın alıp aynı gün kullanmaya başlamıştır. Faydalı ömür 5 yıl olup normal amortisman yöntemi uygulanmaktadır ve varlık binek otomobil değildir. Buna göre 2025 yılı için ayrılacak amortisman kaç ₺'dir?",
        {
            'A': 'Amortisman ayrılmaz',
            'B': '24.000 ₺',
            'C': '12.000 ₺',
            'D': '48.000 ₺',
            'E': '2.000 ₺',
        },
        'B',
        "VUK'a göre amortisman varlığın aktife girdiği yıldan başlar ve binek otomobiller dışında **yıllık tam** ayrılır; kıst amortisman yalnız binek otomobillerde uygulanır. Bu nedenle 2025 için 120.000 / 5 = **24.000 ₺** amortisman ayrılır.",
        'VUK m. 315, 320',
    ),
    # düzey 3
    '0044': patch(
        "İşletme 1 Ocak 2023'te 250.000 ₺'ye aldığı ve aynı gün kullanmaya başladığı bir makine için normal amortisman yöntemini uygulamaktadır; faydalı ömür 5 yıldır. Makine için her yıl amortisman ayrılmıştır. Buna göre makinenin 31 Aralık 2025 tarihli bilançodaki net defter değeri kaç ₺'dir?",
        {
            'A': '100.000 ₺',
            'B': '250.000 ₺',
            'C': '150.000 ₺',
            'D': '125.000 ₺',
            'E': '50.000 ₺',
        },
        'A',
        'Yıllık amortisman 250.000 / 5 = 50.000 ₺. 2023, 2024 ve 2025 için üç yıl: birikmiş amortisman 150.000 ₺. Net defter değeri 250.000 − 150.000 = **100.000 ₺**.',
        'VUK m. 315',
    ),
    # düzey 3
    '0045': patch(
        "Faydalı ömrü 10 yıl olan ve 500.000 ₺'ye alınan bir tesis için azalan bakiyeler yöntemiyle amortisman ayrılmaktadır. Buna göre dört yıllık amortisman ayrıldıktan sonra tesisin net defter değeri kaç ₺'dir?",
        {
            'A': '100.000 ₺',
            'B': '163.840 ₺',
            'C': '204.800 ₺',
            'D': '300.000 ₺',
            'E': '256.000 ₺',
        },
        'C',
        'Oran: normal %10 × 2 = %20. Net değerler: 1. yıl sonu 400.000; 2. yıl 320.000; 3. yıl 256.000; 4. yıl 256.000 × %80 = **204.800 ₺**. Normal yöntemle 4 yıl sonunda 300.000 ₺ olurdu.',
        'VUK m. 316',
    ),
    # düzey 2
    '0046': patch(
        'Bir işletmenin muhasebe müdürü amortisman yöntemleri ve uygulama esasları hakkında ekibine bilgi vermektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Normal yöntemden azalan bakiyeler yöntemine geçilebilir',
            'B': "Azalan bakiyeler oranı %50'yi geçemez",
            'C': 'Arsa amortismana tabi tutulmaz',
            'D': 'Azalan bakiyeler yönteminden normal yönteme geçilebilir',
            'E': 'Binek otomobillerde ilk yıl kıst amortisman ayrılır',
        },
        'A',
        "VUK'ta azalan bakiyeler yönteminden normal yönteme geçiş mümkündür; **normal yöntemden azalan bakiyelere geçilemez**. Azalan bakiyeler oranı normal oranın iki katıdır ve %50'yi aşamaz; arsalar amortismana tabi değildir; binek otomobillerde ilk yıl kıst amortisman uygulanır.",
        'VUK m. 315-316, 320',
    ),
    # düzey 2
    '0047': patch(
        'Normal amortisman uygulanan ve binek otomobil olmayan bir makine, hesap döneminin 30 Haziran tarihinde yenilenmek amacı taşımaksızın satılmıştır. Makine için önceki yıllarda düzenli amortisman ayrılmıştır. Satış yılının amortismanıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Satış yılı için altı aylık kıst amortisman ayrılır',
            'B': 'Satış yılının amortismanı alıcı işletmece ayrılır',
            'C': 'Satış yılında makine için amortisman ayrılmaz',
            'D': 'Satış yılı için tam yıl amortisman ayrılır',
            'E': 'Kalan net değerin tamamı satış yılında amortisman olarak ayrılır',
        },
        'C',
        "VUK'ta amortisman yıllık ve tam yıl esasına dayanır; dönem içinde elden çıkarılan varlık için **satış yılında amortisman ayrılmaz**. Satış kâr veya zararı, satış bedeli ile satış tarihindeki net defter değeri karşılaştırılarak bulunur.",
        'VUK m. 320 (tam yıl esası)',
    ),
    # düzey 3
    '0048': patch(
        'Kayıtlı değeri 90.000 ₺ ve birikmiş amortismanı 54.000 ₺ olan bir demirbaş 30.000 ₺ + %20 KDV bedelle peşin satılmıştır. Buna göre satıştan doğan sonuç ve kullanılacak hesap aşağıdakilerden hangisidir?',
        {
            'A': '36.000 ₺ zarar; 689 borçlandırılır',
            'B': 'Kâr veya zarar doğmaz; 391 alacaklandırılır',
            'C': '60.000 ₺ zarar; 689 borçlandırılır',
            'D': '6.000 ₺ kâr; 679 alacaklandırılır',
            'E': '6.000 ₺ zarar; 689 borçlandırılır',
        },
        'E',
        "Net defter değeri 90.000 − 54.000 = 36.000 ₺; satış bedeli (KDV hariç) 30.000 ₺. Zarar 36.000 − 30.000 = **6.000 ₺** ve **689**'un borcuna yazılır. KDV dâhil tutarla (36.000 ₺) karşılaştırmak hatalıdır; KDV satış bedeli değil, devlete olan borçtur.",
        'THP 689 Diğer Olağandışı Gider ve Zararlar',
    ),
    # düzey 3
    '0049': patch(
        'K İşletmesi kayıtlı değeri 120.000 ₺, birikmiş amortismanı 90.000 ₺ olan kamyonetini net defter değeri üzerinden %40 kârla M İşletmesine satmıştır; bedelin tamamı vadeli olup KDV ihmal edilecektir. Buna göre kamyoneti satın alan M İşletmesinin kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '257 Birikmiş Amortismanlar hesabı 90.000 ₺ alacaklandırılır',
            'B': '679 Diğer Olağandışı Gelir ve Kârlar hesabı 12.000 ₺ alacaklandırılır',
            'C': '254 Taşıtlar hesabı 120.000 ₺ borçlandırılır',
            'D': '254 Taşıtlar hesabı 42.000 ₺ borçlandırılır',
            'E': '120 Alıcılar hesabı 42.000 ₺ borçlandırılır',
        },
        'D',
        "Satış bedeli: (120.000 − 90.000) × 1,40 = 42.000 ₺. Alıcı M için bu tutar **maliyet bedelidir**: 254 Taşıtlar (borç) 42.000 / 320 Satıcılar (alacak) 42.000. Satıcının kayıtlı değeri, birikmiş amortismanı ve kârı M'nin kayıtlarına girmez; satış kârı K'nin 679 hesabındadır.",
        'THP 254 Taşıtlar; 320 Satıcılar',
    ),
    # düzey 2
    '0050': patch(
        "İşletme, kayıtlı değeri 200.000 ₺ olan arsası ile üzerindeki maliyeti 800.000 ₺, birikmiş amortismanı 320.000 ₺ olan binasını birlikte 900.000 ₺'ye satmış ve bedeli banka havalesiyle tahsil etmiştir. Satış sözleşmesinde bedelin 300.000 ₺'si arsaya, 600.000 ₺'si binaya ayrılmıştır. Vergi ihmal edilecektir.\n\nBuna göre satış kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '679 Diğer Olağandışı Gelir ve Kârlar hesabına 100.000 ₺ alacak yazılır',
            'B': '679 Diğer Olağandışı Gelir ve Kârlar hesabına 220.000 ₺ alacak yazılır',
            'C': '252 Binalar hesabı 480.000 ₺ alacaklandırılır',
            'D': '257 Birikmiş Amortismanlar hesabı 320.000 ₺ alacaklandırılır',
            'E': '102 Bankalar hesabı 680.000 ₺ borçlandırılır',
        },
        'B',
        'Arsa: 300.000 − 200.000 = 100.000 ₺ kâr. Bina: net defter değeri 800.000 − 320.000 = 480.000 ₺; 600.000 − 480.000 = 120.000 ₺ kâr. Kayıt: 102 Bankalar 900.000 ₺ ve 257 Birikmiş Amortismanlar 320.000 ₺ borç / 250 Arazi ve Arsalar 200.000 ₺, 252 Binalar 800.000 ₺ ve 679 220.000 ₺ alacak.',
        'THP 250; 679',
    ),
    # düzey 3
    '0051': patch(
        "İşletmenin 549 Özel Fonlar hesabında yenileme amacıyla ayrılmış 30.000 ₺ fon bulunmaktadır. Ertesi yıl üretimde kullanılmak üzere 200.000 ₺'ye faydalı ömrü 5 yıl olan yeni bir makine alınmış ve normal amortisman uygulanmıştır. Buna göre yeni makinenin ilk yıl amortismanından gider hesabına yazılacak tutar kaç ₺'dir?",
        {
            'A': '30.000 ₺',
            'B': '70.000 ₺',
            'C': '10.000 ₺',
            'D': '40.000 ₺',
            'E': 'Gider yazılmaz',
        },
        'C',
        'Yıllık amortisman 200.000 / 5 = 40.000 ₺. Yenileme fonu yeni varlığın amortismanına tahsis edilir: 549 Özel Fonlar (borç) 30.000 + 730 Genel Üretim Giderleri (borç) **10.000** / 257 Birikmiş Amortismanlar (alacak) 40.000. Fonu aşan kısım gider yazılır.',
        'VUK m. 328',
    ),
    # düzey 2
    '0052': patch(
        'İşletme, ileride teslim alacağı bir kaynak makinesi için sözleşme imzalamış ve bedelin bir kısmını satıcıya peşin ödemiştir. Makine henüz teslim alınmamıştır. Ödenen tutar teslimata kadar hangi hesapta izlenir?',
        {
            'A': '159 Verilen Sipariş Avansları',
            'B': '340 Alınan Sipariş Avansları',
            'C': '258 Yapılmakta Olan Yatırımlar',
            'D': '259 Verilen Avanslar',
            'E': '253 Tesis, Makine ve Cihazlar',
        },
        'D',
        "MDV alımı için ödenen avanslar **259 Verilen Avanslar**'da izlenir; 159 stok alımı içindir, 340 ise müşterilerden alınan avanslar içindir. Teslimde 259 alacaklandırılarak kapatılır.",
        'THP 259 Verilen Avanslar',
    ),
    # düzey 2
    '0053': patch(
        "VUK'ta kıst (ay esasına göre) amortisman uygulaması aşağıdaki varlıklardan hangisi için öngörülmüştür?",
        {
            'A': 'Kamyon ve kamyonetler',
            'B': 'Binek otomobiller',
            'C': 'Demirbaşlar',
            'D': 'Binalar',
            'E': 'Üretim makineleri',
        },
        'B',
        'VUK m. 320 uyarınca **binek otomobillerde** ilk yıl amortisman kıst olarak ayrılır; diğer varlıklarda amortisman aktife girilen yıl için tam yıl ayrılır.',
        'VUK m. 320',
    ),
    # düzey 2
    '0054': patch(
        'Maliyetinin tamamı amortisman yoluyla itfa edilmiş bir demirbaş işletmede kullanılmaya devam etmektedir. İşletme varlığın kayıtlarda görünmesini sağlamak için sembolik bir tutar bırakmak istemektedir. Bu sembolik tutara ne ad verilir?',
        {
            'A': 'Yeniden değerleme artışı',
            'B': 'Hurda değeri',
            'C': 'Net gerçekleşebilir değer',
            'D': 'Yenileme fonu',
            'E': 'İz bedeli',
        },
        'E',
        'Tamamen amortize edilmiş ancak kullanımda olan varlığın kayıtlarda izlenebilmesi için bırakılan sembolik tutar **iz bedeli**dir.',
        'Tekdüzen Muhasebe Sistemi (iz bedeli)',
    ),
    # düzey 3
    '0055': patch(
        "İşletme 900.000 ₺'ye (KDV hariç) aldığı makinenin bedelini banka kredisiyle ödemiştir. Makine kurulum sonrasında kullanıma hazır hâle gelene kadar krediye 18.000 ₺ faiz tahakkuk etmiş, kullanıma hazır hâle geldikten sonra yıl sonuna kadar ise 42.000 ₺ faiz işlemiştir. Buna göre makinenin maliyet bedeli kaç ₺'dir?",
        {
            'A': '918.000 ₺',
            'B': '942.000 ₺',
            'C': '960.000 ₺',
            'D': '900.000 ₺',
            'E': '1.098.000 ₺',
        },
        'A',
        'Varlık kullanıma hazır hâle gelene kadar (aktife alınana kadar) oluşan finansman gideri maliyete eklenir: 900.000 + 18.000 = **918.000 ₺**. Sonraki 42.000 ₺ faiz dönem gideridir (780 Finansman Giderleri).',
        "1 Sıra No'lu MSUGT; THP 253, 780",
    ),
    # düzey 3
    '0056': patch(
        'Maddi duran varlıklarla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Azalan bakiyeler oranı normal oranın üç katıdır.\n\nII. Arsalar, faydalı ömürleri boyunca normal amortismana tabi tutulur.\n\nIII. Tamamen amortize edilmiş ancak kullanılan varlık için iz bedeli bırakılabilir.',
        {
            'A': 'I ve III',
            'B': 'I ve II',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'Yalnız III',
        },
        'E',
        'Yalnız III doğrudur. Azalan bakiyeler oranı normal oranın **iki** katıdır (en çok %50); arsalar amortismana tabi değildir.',
        'VUK m. 316; THP 257',
    ),
    # düzey 2
    '0057': patch(
        "Maliyeti 150.000 ₺ olan ve faydalı ömrü dolduğu için birikmiş amortismanı 150.000 ₺'ye ulaşan bir demirbaş işletmede kullanılmaya devam etmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Demirbaşın net defter değeri sıfırdır',
            'B': 'Demirbaş için amortisman ayrılmaya devam edilir',
            'C': 'Satılırsa bedelin tamamı kâr olarak kaydedilir',
            'D': 'Demirbaş kayıtlardan çıkarılmadan kullanılabilir',
            'E': 'Kayıtlarda iz bedeli bırakılabilir',
        },
        'B',
        'Birikmiş amortisman maliyete (150.000 ₺) ulaştığında varlık tamamen itfa edilmiştir; **artık amortisman ayrılmaz**. Net defter değeri sıfır olduğundan satışta bedelin tamamı kârdır; kullanım sürerken iz bedeli bırakılabilir.',
        'Tekdüzen Muhasebe Sistemi; VUK m. 315',
    ),
    # düzey 3
    '0058': patch(
        'Maliyet bedeli 100.000 ₺ ve faydalı ömrü 4 yıl olan bir makine için azalan bakiyeler yöntemi uygulanmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Birinci yıl amortismanı 50.000 ₺'dir",
            'B': 'Normal yöntemde yıllık amortisman 25.000 ₺ olurdu',
            'C': "İkinci yıl amortismanı 25.000 ₺'dir",
            'D': "İkinci yıl sonunda net defter değeri 50.000 ₺'dir",
            'E': "Uygulanacak oran %50'dir",
        },
        'D',
        "Normal oran %25, azalan bakiyeler oranı bunun iki katı %50'dir (sınırı aşmaz). 1. yıl 100.000 × %50 = 50.000 ₺; 2. yıl 50.000 × %50 = 25.000 ₺. İkinci yıl sonunda net defter değeri 100.000 − 50.000 − 25.000 = **25.000 ₺**'dir; 50.000 ₺ birinci yıl sonundaki değerdir. Normal yöntemde yıllık amortisman 100.000 / 4 = 25.000 ₺ olurdu.",
        'VUK m. 315-316',
    ),
    # düzey 3
    '0059': patch(
        "İşletme 250.000 ₺'ye aldığı ve faydalı ömrü 5 yıl olan bir makine için iki yıl azalan bakiyeler yöntemiyle amortisman ayırmış, üçüncü yıldan itibaren normal amortisman yöntemine geçmiştir. Buna göre üçüncü yılın sonunda makinenin bilançodaki net defter değeri kaç ₺'dir?",
        {
            'A': '100.000 ₺',
            'B': '40.000 ₺',
            'C': '60.000 ₺',
            'D': '90.000 ₺',
            'E': '54.000 ₺',
        },
        'C',
        '1. yıl 100.000 ₺, 2. yıl 60.000 ₺; kalan 90.000 ₺. Geçişte kalan değer kalan 3 yıla bölünür: 90.000 / 3 = 30.000 ₺. Üçüncü yıl sonu net değer 90.000 − 30.000 = **60.000 ₺**.',
        'VUK m. 316',
    ),
    # düzey 2
    '0060': patch(
        'Bir işletmenin muhasebe elemanı maddi duran varlıklarını hesaplara şöyle eşleştirmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Şirket kamyoneti – 254',
            'B': 'Yönetim katındaki büro mobilyası – 255',
            'C': 'Üretim bandı – 253',
            'D': 'Tamamlanıp kullanılan fabrika binası – 258',
            'E': 'Fabrikanın üzerinde bulunduğu arsa – 250',
        },
        'D',
        "Tamamlanıp kullanıma alınan bina **252 Binalar**'da izlenir; 258 yalnız henüz tamamlanmamış yatırımlar içindir. Arsa 250, taşıtlar 254, demirbaşlar 255, makine ve tesisler 253'te izlenir.",
        'THP 25 Maddi Duran Varlıklar',
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
    print(f"1 paket / {len(PATCHES)} soru ('Maddi Duran Varliklar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
