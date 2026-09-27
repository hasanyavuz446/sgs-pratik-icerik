#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TMS 12 Gelir Vergileri — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gercek sinav profiliyle yeniden yazim (senaryo kok + kisa tutar/terim sik). Gercek sinavdaki TMS 12 sorulari neredeyse tamamen gecici fark hesabidir; bu kalip farkli kalem ve tutarlarla islendi: vergiye esas deger (varlik, pesin gelir, tahakkuk), vergilendirilebilir/indirilebilir farklar (amortisman, karsiliklar, faiz, YAG, yeniden degerleme, hisse degerlemesi, arastirma gideri), kalici farklar, serefiye ve ilk tanima istisnasi (2021 kiralama degisikligi), vergi zararlari ve EVV degerlendirmesi, oran secimi ve degisikligi, iskonto yasagi, cari vergi ve toplam vergi gideri, DKG'deki vergi, netlestirme, siniflandirma, aciklama. Eski surum 70 mutlak ifadeli celdirici tasiyordu (kor %36). 30 hesap sorusu modulde hesaplandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: TMS 12 Gelir Vergileri (KGK, 2021 degisikligi dahil); TMS 1 p. 56, TMS 10
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/tms_12_gelir_vergileri.json"
STYLE_REF = 'SGS Muhasebe Standartlari (gercek sinav profiline kalibre: senaryo kok + kisa sik)'
ONEK = "std-tms12-gen-"


def patch(stem, options, answer, solution, ref='TMS 12 Gelir Vergileri'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Bir işletmenin makinesinin maliyeti 800.000 ₺'dir; vergi mevzuatına göre bugüne kadar 300.000 ₺ amortisman indirilmiştir ve makinenin kullanımından elde edilecek gelirler vergilendirilecektir. Makinenin vergiye esas değeri kaç ₺'dir?",
        {
            'A': '500.000',
            'B': '300.000',
            'C': '0',
            'D': '800.000',
            'E': '1.100.000',
        },
        'A',
        "TMS 12 p. 7'ye göre bir varlığın vergiye esas değeri, varlığın defter değerini geri kazanırken elde edilecek vergilendirilebilir ekonomik faydalardan **vergi açısından indirilebilecek tutardır**: 800.000 − 300.000 = **500.000 ₺**.",
        'TMS 12 p. 7',
    ),
    # düzey 3
    '0002': patch(
        "Bir işletmenin bir makinesinin finansal tablolardaki defter değeri 500.000 ₺, vergiye esas değeri 380.000 ₺'dir; vergi oranı %25'tir. İlk tanıma istisnası söz konusu değildir. Bu makine için tanınacak ertelenmiş vergi hangisidir?",
        {
            'A': '30.000 ₺ ertelenmiş vergi yükümlülüğü',
            'B': '125.000 ₺ ertelenmiş vergi yükümlülüğü',
            'C': '120.000 ₺ ertelenmiş vergi yükümlülüğü',
            'D': '30.000 ₺ ertelenmiş vergi varlığı',
            'E': 'Ertelenmiş vergi doğmaz',
        },
        'A',
        "Varlığın defter değeri vergiye esas değerinden büyük olduğundan **vergilendirilebilir geçici fark** vardır: 500.000 − 380.000 = 120.000 ₺. TMS 12 p. 15'e göre **ertelenmiş vergi yükümlülüğü**: 120.000 × %25 = **30.000 ₺**.",
        'TMS 12 p. 5, 15',
    ),
    # düzey 3
    '0003': patch(
        "Bir işletmenin 120.000 ₺ peşin tahsil edilmiş kira geliri vardır; tutar vergi mevzuatına göre tahsil edildiği dönemde vergilendirilmiştir. Vergi oranı %25'tir ve gelecekte yeterli kâr beklenmektedir. Bu kalem için tanınacak ertelenmiş vergi hangisidir?",
        {
            'A': '120.000 ₺ ertelenmiş vergi varlığı',
            'B': 'Ertelenmiş vergi doğmaz',
            'C': '30.000 ₺ ertelenmiş vergi yükümlülüğü',
            'D': '15.000 ₺ ertelenmiş vergi varlığı',
            'E': '30.000 ₺ ertelenmiş vergi varlığı',
        },
        'E',
        "Ertelenmiş gelirin (borç) defter değeri 120.000 ₺, vergiye esas değeri 0'dır; borçta defter değeri büyük olduğundan **indirilebilir geçici fark** vardır: 120.000 × %25 = **30.000 ₺ ertelenmiş vergi varlığı**; gelir muhasebede tanındığında vergi zaten ödenmiş olacaktır.",
        'TMS 12 p. 8, 24',
    ),
    # düzey 3
    '0004': patch(
        "Bir işletme gerçeğe uygun değer modeliyle ölçtüğü bir binada dönem sonunda 200.000 ₺ değer artışı kazancı tanımıştır; kazanç vergi mevzuatında dikkate alınmamakta, bina satılana kadar vergiye esas değer maliyet üzerinden kalmaktadır. Vergi oranı %20'dir. Değer artışının ertelenmiş vergi etkisi hangisidir?",
        {
            'A': 'Ertelenmiş vergi doğmaz',
            'B': "40.000 ₺ yükümlülük, DKG'de",
            'C': '40.000 ₺ varlık, kâr veya zararda',
            'D': '200.000 ₺ yükümlülük, kâr veya zararda',
            'E': '40.000 ₺ yükümlülük, kâr veya zararda',
        },
        'E',
        'Değer artışı binanın defter değerini vergiye esas değerin üzerine çıkarır; **vergilendirilebilir geçici fark** 200.000 ₺ oluşur. Kazanç kâr veya zararda tanındığından ertelenmiş vergi de kâr veya zarara yansır: **40.000 ₺ yükümlülük**.',
        'TMS 12 p. 17, 51B',
    ),
    # düzey 2
    '0005': patch(
        'Bir işletme bir işletme birleşmesinde 500.000 ₺ şerefiye tanımıştır; vergi mevzuatına göre şerefiye hiçbir dönemde gider olarak indirilemeyecektir. Şerefiyenin ilk tanınması için ertelenmiş vergi yükümlülüğü hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Diğer kapsamlı gelirde tanınır',
            'B': 'Tanınmaz',
            'C': 'Yarısı tanınır',
            'D': 'Tanınır',
            'E': 'Özkaynakta tanınır',
        },
        'B',
        "TMS 12 p. 15(a) ve 21'e göre **şerefiyenin ilk muhasebeleştirilmesinden** kaynaklanan vergilendirilebilir geçici fark için ertelenmiş vergi yükümlülüğü tanınmaz; aksi hâlde şerefiye artar ve döngüsel bir etki oluşur.",
        'TMS 12 p. 15(a), 21',
    ),
    # düzey 3
    '0006': patch(
        "Bir işletmenin gelecek yıllara devreden 800.000 ₺ kullanılmamış mali zararı vardır. İşletme, zararın mahsup süresi içinde 600.000 ₺ vergilendirilebilir kâr elde etmesinin muhtemel olduğunu öngörmektedir. Vergi oranı %25'tir. Tanınacak ertelenmiş vergi varlığı kaç ₺'dir?",
        {
            'A': '200.000',
            'B': '50.000',
            'C': '800.000',
            'D': '150.000',
            'E': '0',
        },
        'D',
        "TMS 12 p. 34'e göre kullanılmamış vergi zararları için ertelenmiş vergi varlığı, **gelecekte vergilendirilebilir kâr elde edilmesinin muhtemel olduğu ölçüde** tanınır: 600.000 × %25 = **150.000 ₺**.",
        'TMS 12 p. 34-36',
    ),
    # düzey 2
    '0007': patch(
        "Bir işletmenin ertelenmiş vergi yükümlülüğünün 10 yıl içinde kademeli olarak tersine dönmesi beklenmektedir. Yönetim, paranın zaman değerini yansıtmak için yükümlülüğü bugünkü değerine indirgemek istemektedir. TMS 12'ye göre bu uygulama hakkında ne söylenebilir?",
        {
            'A': 'Denetçi onayıyla yapılır',
            'B': 'Vergi öncesi oranla iskonto yapılır',
            'C': 'İskonto yapılır',
            'D': 'Uzun vadeli kısım iskonto edilir',
            'E': 'İskonto yapılmaz',
        },
        'E',
        "TMS 12 p. 53'e göre **ertelenmiş vergi varlık ve yükümlülükleri iskonto edilmez**; tersine dönme zamanlamasının güvenilir biçimde belirlenmesi pratik olmadığından iskonto karşılaştırılabilirliği bozar.",
        'TMS 12 p. 53',
    ),
    # düzey 3
    '0008': patch(
        'Bir işletme bir binayı satarak geri kazanmayı bekliyorsa %20, kullanarak geri kazanmayı bekliyorsa %25 vergi oranı uygulanmaktadır. İşletme binayı satmayı planlamaktadır. Ertelenmiş vergi ölçümünde hangi oran kullanılır?',
        {
            'A': '%22,5',
            'B': 'Oranların toplamı',
            'C': '%25',
            'D': '%20',
            'E': 'Cari yılın oranı',
        },
        'D',
        "TMS 12 p. 51-51A'ya göre ertelenmiş vergi, işletmenin raporlama dönemi sonunda varlığın defter değerini **geri kazanmayı beklediği yönteme** göre doğacak vergi sonuçlarını yansıtır; satış beklendiğinden satışa uygulanan **%20** oranı kullanılır.",
        'TMS 12 p. 51-51A',
    ),
    # düzey 3
    '0009': patch(
        "Bir işletmenin muhasebe kârı (vergi öncesi) 900.000 ₺'dir. Kârın hesaplanmasında 60.000 ₺ kanunen kabul edilmeyen gider düşülmüş, 100.000 ₺ vergiden istisna iştirak kazancı eklenmiştir; geçici fark yoktur. Vergi oranı %25'tir. Cari vergi gideri kaç ₺'dir?",
        {
            'A': '225.000',
            'B': '235.000',
            'C': '215.000',
            'D': '240.000',
            'E': '200.000',
        },
        'C',
        'Vergilendirilebilir kâr: 900.000 + 60.000 (KKEG) − 100.000 (istisna) = 860.000 ₺. Cari vergi: 860.000 × %25 = **215.000 ₺**. Bu kalıcı farklar ertelenmiş vergi doğurmaz.',
        'TMS 12 p. 5, 12',
    ),
    # düzey 3
    '0010': patch(
        'Bir işletmenin aynı vergi idaresine karşı 80.000 ₺ ertelenmiş vergi varlığı ve 120.000 ₺ ertelenmiş vergi yükümlülüğü vardır; cari vergi varlık ve borçlarını mahsup etmek için yasal hakkı bulunmaktadır. Finansal durum tablosunda ne gösterilir?',
        {
            'A': '40.000 ₺ net ertelenmiş vergi yükümlülüğü',
            'B': 'Bir şey gösterilmez',
            'C': '80.000 ₺ varlık ve 120.000 ₺ yükümlülük',
            'D': '40.000 ₺ net ertelenmiş vergi varlığı',
            'E': '200.000 ₺ yükümlülük',
        },
        'A',
        "TMS 12 p. 74'e göre işletme cari vergi varlık ve borçlarını mahsup etmek için **yasal hakka** sahipse ve ertelenmiş vergiler **aynı vergi idaresince** aynı vergiye tabi işletmeden alınan gelir vergileriyle ilgiliyse, ertelenmiş vergi varlık ve yükümlülüklerini netleştirir: **40.000 ₺ net yükümlülük**.",
        'TMS 12 p. 74',
    ),
    # düzey 2
    '0011': patch(
        "TMS 12'ye göre, gelecek dönemlerde vergilendirilebilir kâr belirlenirken vergiye tabi tutarlar doğuracak geçici farklar nasıl adlandırılır?",
        {
            'A': 'Vergi alacakları',
            'B': 'Kullanılmamış vergi zararları',
            'C': 'Kalıcı farklar',
            'D': 'İndirilebilir geçici farklar',
            'E': 'Vergilendirilebilir geçici farklar',
        },
        'E',
        "TMS 12 p. 5'e göre **vergilendirilebilir geçici farklar**, varlık veya borcun defter değerinin geri kazanılması ya da ödenmesi sırasında gelecek dönemlerin vergilendirilebilir kârına eklenecek tutarlar doğuran farklardır ve ertelenmiş vergi yükümlülüğü yaratır.",
        'TMS 12 p. 5',
    ),
    # düzey 2
    '0012': patch(
        'Bir ana ortaklık, bağlı ortaklığındaki yatırımının defter değeri ile vergiye esas değeri arasında vergilendirilebilir geçici fark bulunduğunu belirlemiştir. Ana ortaklık farkın tersine dönme zamanını kontrol edebilmekte ve yakın gelecekte tersine dönmemesi muhtemeldir. Ertelenmiş vergi yükümlülüğü hakkında ne söylenebilir?',
        {
            'A': 'Tanınır',
            'B': 'Tanınmaz',
            'C': 'Diğer kapsamlı gelirde tanınır',
            'D': 'Şerefiyeye eklenir',
            'E': 'Yarısı tanınır',
        },
        'B',
        "TMS 12 p. 39'a göre bağlı ortaklıklardaki yatırımlara ilişkin vergilendirilebilir geçici farklar için, ana ortaklık **tersine dönme zamanını kontrol edebiliyorsa** ve farkın **yakın gelecekte tersine dönmemesi muhtemelse** ertelenmiş vergi yükümlülüğü tanınmaz.",
        'TMS 12 p. 39, 44',
    ),
    # düzey 3
    '0013': patch(
        'Raporlama döneminden sonra, finansal tablolar onaylanmadan önce kurumlar vergisi oranı yükseltilmiştir; yıl sonunda bu değişiklik yasalaşmamış ve yasalaşması kesinleşmemişti. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Ertelenmiş vergi yeni oranla ölçülür',
            'B': 'Önemli etki dipnotta açıklanır',
            'C': 'Yıl sonunda yasalaşmış oran kullanılır',
            'D': 'Yeni oran sonraki dönem ölçümlerinde kullanılır',
            'E': "Değişiklik TMS 10'a göre düzeltme gerektirmez",
        },
        'A',
        "TMS 12 p. 46-47'ye göre cari ve ertelenmiş vergi, **raporlama dönemi sonunda yasalaşmış veya yasalaşması kesinleşmiş** oranlarla ölçülür; sonradan yasalaşan oran değişikliği TMS 10'a göre düzeltme gerektirmeyen olaydır ve açıklanır.",
        'TMS 12 p. 46-47',
    ),
    # düzey 2
    '0014': patch(
        "Bir işletme stokları için 40.000 ₺ değer düşüklüğü ayırmıştır; vergi mevzuatı bu tutarı stoklar satılıncaya kadar gider olarak kabul etmemektedir. Vergi oranı %25'tir ve yeterli kâr beklenmektedir. Tanınacak ertelenmiş vergi hangisidir?",
        {
            'A': '30.000 ₺ ertelenmiş vergi varlığı',
            'B': '10.000 ₺ ertelenmiş vergi varlığı',
            'C': '40.000 ₺ ertelenmiş vergi varlığı',
            'D': 'Ertelenmiş vergi doğmaz',
            'E': '10.000 ₺ ertelenmiş vergi yükümlülüğü',
        },
        'B',
        'Stokların defter değeri vergiye esas değerinden 40.000 ₺ düşüktür; **indirilebilir geçici fark** oluşur: 40.000 × %25 = **10.000 ₺ ertelenmiş vergi varlığı**.',
        'TMS 12 p. 24, 26(d)',
    ),
    # düzey 3
    '0015': patch(
        "Bir işletmenin vergi öncesi muhasebe kârı 800.000 ₺'dir. Muhasebede gider yazılan ancak vergide ödendiğinde indirilecek 50.000 ₺ karşılık vardır; ayrıca vergide muhasebeye göre 30.000 ₺ fazla amortisman indirilmiştir. Kalıcı fark yoktur ve vergi oranı %25'tir. Cari vergi gideri kaç ₺'dir?",
        {
            'A': '195.000',
            'B': '192.500',
            'C': '205.000',
            'D': '200.000',
            'E': '220.000',
        },
        'C',
        'Vergilendirilebilir kâr: 800.000 + 50.000 (henüz indirilemeyen karşılık) − 30.000 (fazla vergi amortismanı) = 820.000 ₺. Cari vergi: 820.000 × %25 = **205.000 ₺**.',
        'TMS 12 p. 5, 12',
    ),
    # düzey 2
    '0016': patch(
        "Bir işletmenin kâr veya zarar tablosundaki toplam vergi gideri 280.000 ₺, vergi öncesi muhasebe kârı 1.000.000 ₺'dir. TMS 12'ye göre açıklanabilecek ortalama etkin vergi oranı yüzde kaçtır?",
        {
            'A': '30',
            'B': '28',
            'C': '25',
            'D': '22',
            'E': '20',
        },
        'B',
        "TMS 12 p. 86'ya göre ortalama etkin vergi oranı, **vergi giderinin muhasebe kârına bölünmesiyle** bulunur: 280.000 / 1.000.000 = **%28**.",
        'TMS 12 p. 86',
    ),
    # düzey 3
    '0017': patch(
        'Bir ülkenin vergi mevzuatı, cari yıl vergi zararının önceki yılda ödenen verginin iadesi için geriye taşınmasına izin vermektedir. Bir işletme cari yılda vergi zararı etmiş ve önceki yılda ödediği vergiden 90.000 ₺ iade hakkı doğmuştur. Bu hak nasıl muhasebeleştirilir?',
        {
            'A': 'Özkaynakta',
            'B': 'Koşullu varlık olarak',
            'C': 'Önceki yılın düzeltilmesiyle',
            'D': 'Cari yılda varlık olarak',
            'E': 'Muhasebeleştirilmez',
        },
        'D',
        "TMS 12 p. 13-14'e göre önceki dönemin cari vergisinin geri alınması amacıyla geriye taşınabilen vergi zararına ilişkin fayda **varlık olarak** tanınır; fayda güvenilir ölçülebildiğinden zararın oluştuğu dönemde muhasebeleştirilir.",
        'TMS 12 p. 13-14',
    ),
    # düzey 3
    '0018': patch(
        "Bir işletme 2021 değişikliği sonrasında bir kiralamada 1.000.000 ₺ kullanım hakkı varlığı ve aynı tutarda kira yükümlülüğü tanımıştır; vergide kira ödendiğinde gider yazılmaktadır. Vergi oranı %20'dir ve gelecekte yeterli kâr beklenmektedir. Başlangıçta brüt olarak tanınacak ertelenmiş vergi yükümlülüğü kaç ₺'dir?",
        {
            'A': '100.000',
            'B': '0',
            'C': '200.000',
            'D': '1.000.000',
            'E': '400.000',
        },
        'C',
        "Kullanım hakkı varlığının vergiye esas değeri 0 olduğundan 1.000.000 ₺ vergilendirilebilir, kira yükümlülüğünün vergiye esas değeri 0 olduğundan 1.000.000 ₺ indirilebilir geçici fark doğar. p. 22A'ya göre ilk tanıma istisnası uygulanmaz: brüt **200.000 ₺ EVY** ve aynı tutarda EVV tanınır (p. 74 koşullarıyla netleştirilebilir).",
        'TMS 12 p. 15(b), 22A, 24',
    ),
    # düzey 2
    '0019': patch(
        "Aşağıdakilerden hangileri TMS 12'ye göre doğrudur?\n\nI. Fazla ödenen cari vergi varlık olarak tanınır\n\nII. Kullanılmamış vergi zararları için muhtemel kâr ölçüsünde ertelenmiş vergi varlığı tanınır\n\nIII. Ertelenmiş vergi varlığının defter değeri her dönem gözden geçirilir",
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'I ve III',
        },
        'A',
        "TMS 12 p. 12'ye göre fazla ödeme varlıktır (I); p. 34'e göre vergi zararları için muhtemel kâr ölçüsünde EVV tanınır (II); p. 56'ya göre EVV'nin defter değeri her dönem gözden geçirilir (III).",
        'TMS 12 p. 12, 34, 56',
    ),
    # düzey 3
    '0020': patch(
        'Aşağıdakilerden hangileri doğrudur?\n\nI. Yakın geçmişte vergi zararı olan işletme ikna edici kanıt olmadan EVV tanımaz\n\nII. Tersine dönme zamanı kontrol edilen ve yakın gelecekte dönmeyecek bağlı ortaklık farkları için EVY tanınmaz\n\nIII. Vergi oranı değişikliği geriye dönük olarak önceki yılları düzeltir',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'Yalnız II',
            'E': 'I ve III',
        },
        'C',
        "TMS 12 p. 35'e göre yakın geçmişte zarar eden işletme ikna edici kanıt olmadan EVV tanımaz (I); p. 39'a göre ana ortaklığın tersine dönme zamanını kontrol ettiği ve yakın gelecekte dönmeyecek farklarda EVY tanınmaz (II). Oran değişikliği **cari dönemde** ertelenmiş vergiyi yeniden ölçer, önceki yılları düzeltmez (III yanlış).",
        'TMS 12 p. 35, 39',
    ),
    # düzey 3
    '0021': patch(
        "Bir işletmenin finansal durum tablosunda 120.000 ₺ peşin tahsil edilmiş kira geliri (ertelenmiş gelir) vardır; vergi mevzuatına göre bu tutar tahsil edildiği dönemde vergilendirilmiştir. Bu borcun vergiye esas değeri kaç ₺'dir?",
        {
            'A': '30.000',
            'B': '60.000',
            'C': '120.000',
            'D': '240.000',
            'E': '0',
        },
        'E',
        "TMS 12 p. 8'e göre peşin tahsil edilen gelirde borcun vergiye esas değeri, defter değerinden **gelecek dönemlerde vergilendirilmeyecek gelir tutarı** düşülerek bulunur. Tutarın tamamı tahsilde vergilendirildiğinden vergiye esas değer **0 ₺**'dir.",
        'TMS 12 p. 8',
    ),
    # düzey 2
    '0022': patch(
        "Bir işletme 300.000 ₺ kıdem tazminatı karşılığı ayırmıştır; vergi mevzuatına göre bu tutar ancak ödendiğinde gider olarak indirilebilecektir. Vergi oranı %25'tir ve gelecekte yeterli vergilendirilebilir kâr beklenmektedir. Tanınacak ertelenmiş vergi kaç ₺'dir ve türü nedir?",
        {
            'A': '300.000 ₺ ertelenmiş vergi varlığı',
            'B': '225.000 ₺ ertelenmiş vergi varlığı',
            'C': 'Ertelenmiş vergi doğmaz',
            'D': '75.000 ₺ ertelenmiş vergi varlığı',
            'E': '75.000 ₺ ertelenmiş vergi yükümlülüğü',
        },
        'D',
        "Borcun defter değeri 300.000 ₺, vergiye esas değeri 0'dır (gelecekte tamamı indirilecek); borçta defter değeri vergiye esas değerden büyük olduğundan **indirilebilir geçici fark** doğar: 300.000 × %25 = **75.000 ₺ ertelenmiş vergi varlığı**.",
        'TMS 12 p. 24, 26(a)',
    ),
    # düzey 2
    '0023': patch(
        "Bir işletme mevduatına ilişkin 50.000 ₺ faizi tahakkuk esasına göre gelir yazmıştır; vergi mevzuatına göre faiz tahsil edildiğinde vergilendirilecektir. Vergi oranı %20'dir. Tanınacak ertelenmiş vergi hangisidir?",
        {
            'A': '10.000 ₺ ertelenmiş vergi varlığı',
            'B': '10.000 ₺ ertelenmiş vergi yükümlülüğü',
            'C': 'Ertelenmiş vergi doğmaz',
            'D': '50.000 ₺ ertelenmiş vergi yükümlülüğü',
            'E': '40.000 ₺ ertelenmiş vergi yükümlülüğü',
        },
        'B',
        "Faiz alacağının defter değeri 50.000 ₺, vergiye esas değeri 0'dır; varlıkta defter değeri büyük olduğundan TMS 12 p. 17(a) uyarınca **vergilendirilebilir geçici fark** doğar: 50.000 × %20 = **10.000 ₺ ertelenmiş vergi yükümlülüğü**.",
        'TMS 12 p. 17(a)',
    ),
    # düzey 3
    '0024': patch(
        "Bir işletme arsasını yeniden değerleme modeliyle ölçmüş ve 400.000 ₺ değer artışı tanımıştır; vergi mevzuatında bu artış dikkate alınmamakta ve vergiye esas değer değişmemektedir. Vergi oranı %25'tir. Doğan ertelenmiş vergi yükümlülüğü kaç ₺'dir ve karşı tarafı nerede tanınır?",
        {
            'A': 'Ertelenmiş vergi doğmaz',
            'B': '100.000 ₺, kâr veya zararda',
            'C': '100.000 ₺, diğer kapsamlı gelirde',
            'D': '400.000 ₺, diğer kapsamlı gelirde',
            'E': '100.000 ₺, geçmiş yıllar kârlarında',
        },
        'C',
        "TMS 12 p. 20'ye göre yeniden değerleme, vergiye esas değer düzeltilmezse **vergilendirilebilir geçici fark** doğurur. p. 61A'ya göre kâr veya zarar dışında muhasebeleştirilen kalemlere ilişkin vergi de aynı yerde tanınır: 400.000 × %25 = **100.000 ₺**, **diğer kapsamlı gelirde**.",
        'TMS 12 p. 20, 61A',
    ),
    # düzey 3
    '0025': patch(
        'Bir işletmenin şu kalemleri vardır: vergi mevzuatınca kabul edilmeyen dava karşılığı, vergide daha hızlı amortismana tabi makine, peşin tahsil edilip vergilendirilen gelir, vergiden tamamen istisna iştirak kazancı ve vergide ödendiğinde indirilecek izin karşılığı. Bunlardan hangisi ertelenmiş vergi doğurmaz?',
        {
            'A': 'İstisna iştirak kazancı',
            'B': 'Hızlı amortismanlı makine',
            'C': 'Dava karşılığı',
            'D': 'Peşin tahsil edilen gelir',
            'E': 'İzin karşılığı',
        },
        'A',
        'Vergiden **tamamen ve kalıcı olarak istisna** edilen iştirak kazancı hiçbir dönemde vergilendirilmeyeceğinden kalıcı farktır ve ertelenmiş vergi doğurmaz. Diğer kalemler gelecekte tersine dönecek **geçici farklardır**.',
        'TMS 12 p. 5, 15, 24',
    ),
    # düzey 3
    '0026': patch(
        'Bir işletme, vergi mevzuatına göre hiçbir zaman amortismanı indirilemeyecek bir varlığı işletme birleşmesi dışında satın almıştır; işlem anında ne muhasebe kârı ne vergi kârı etkilenmiş ve eşit tutarda indirilebilir geçici fark doğmamıştır. Bu varlığın ilk tanınmasından doğan geçici fark için ne yapılır?',
        {
            'A': 'Ertelenmiş vergi varlığı tanınır',
            'B': 'Ertelenmiş vergi yükümlülüğü tanınır',
            'C': 'Ertelenmiş vergi tanınmaz',
            'D': 'Varlık maliyeti artırılır',
            'E': 'Fark kâr veya zarara yazılır',
        },
        'C',
        "TMS 12 p. 15(b) ve 22(c)'ye göre işletme birleşmesi olmayan, işlem anında ne muhasebe ne vergi kârını etkileyen ve eşit geçici farklar doğurmayan bir işlemde varlığın **ilk muhasebeleştirilmesinden** doğan geçici fark için ertelenmiş vergi tanınmaz (ilk tanıma istisnası).",
        'TMS 12 p. 15(b), 22(c)',
    ),
    # düzey 3
    '0027': patch(
        "Bir işletmenin raporlama dönemi sonunda 200.000 ₺ vergilendirilebilir geçici farkı vardır. Cari vergi oranı %20 olmakla birlikte, geçici farkın tersine döneceği yıllarda uygulanacak %25 oran raporlama döneminden önce yasalaşmıştır. Ertelenmiş vergi yükümlülüğü kaç ₺'dir?",
        {
            'A': '40.000',
            'B': '200.000',
            'C': '50.000',
            'D': '10.000',
            'E': '45.000',
        },
        'C',
        "TMS 12 p. 47'ye göre ertelenmiş vergi, **varlığın gerçekleşeceği veya borcun ödeneceği dönemde uygulanması beklenen** ve raporlama dönemi sonunda yasalaşmış oranlarla ölçülür: 200.000 × %25 = **50.000 ₺**.",
        'TMS 12 p. 47',
    ),
    # düzey 2
    '0028': patch(
        "Bir işletmenin cari dönem kurumlar vergisi 250.000 ₺'dir; dönem içinde geçici vergi olarak 180.000 ₺ ödenmiştir. Finansal durum tablosunda gösterilecek cari dönem vergi borcu kaç ₺'dir?",
        {
            'A': '430.000',
            'B': '70.000',
            'C': '250.000',
            'D': '180.000',
            'E': '0',
        },
        'B',
        "TMS 12 p. 12'ye göre cari ve önceki dönemlere ait cari vergi, **ödenmemiş olduğu ölçüde** borç olarak tanınır: 250.000 − 180.000 = **70.000 ₺**. Ödenen tutar vergiyi aşsaydı fazlalık varlık olarak tanınırdı.",
        'TMS 12 p. 12',
    ),
    # düzey 2
    '0029': patch(
        "Bir işletmenin cari dönem kurumlar vergisi 250.000 ₺'dir; dönem içinde geçici vergi olarak 290.000 ₺ ödenmiştir ve fazla ödenen tutar iade veya mahsup edilebilecektir. Finansal durum tablosunda ne gösterilir?",
        {
            'A': 'Bir şey gösterilmez',
            'B': '40.000 ₺ cari vergi varlığı',
            'C': '290.000 ₺ cari vergi varlığı',
            'D': '40.000 ₺ cari vergi borcu',
            'E': '250.000 ₺ cari vergi borcu',
        },
        'B',
        "TMS 12 p. 12'ye göre cari ve önceki dönemler için ödenmiş tutar bu dönemlere ilişkin borcu aşarsa **fazlalık varlık olarak** tanınır: 290.000 − 250.000 = **40.000 ₺**.",
        'TMS 12 p. 12',
    ),
    # düzey 3
    '0030': patch(
        'Bir işletme, gerçeğe uygun değer değişimlerini diğer kapsamlı gelirde sunduğu özkaynak araçlarında 80.000 ₺ değer artışı tanımış ve bu artış için 16.000 ₺ ertelenmiş vergi yükümlülüğü hesaplamıştır. Ertelenmiş vergi nerede muhasebeleştirilir?',
        {
            'A': 'Geçmiş yıllar kârlarında',
            'B': 'Kâr veya zararda',
            'C': 'Hasılattan düşülerek',
            'D': 'Diğer kapsamlı gelirde',
            'E': 'Sermayede',
        },
        'D',
        "TMS 12 p. 61A'ya göre kâr veya zarar dışında (DKG veya doğrudan özkaynakta) muhasebeleştirilen kalemlere ilişkin cari ve ertelenmiş vergi de **aynı şekilde kâr veya zarar dışında** muhasebeleştirilir.",
        'TMS 12 p. 61A',
    ),
    # düzey 3
    '0031': patch(
        "Bir işletme 70.000 ₺ garanti karşılığı ayırmıştır; vergi mevzuatına göre garanti harcamaları ancak yapıldığında indirilebilecektir. Vergi oranı %20'dir ve yeterli gelecek kâr beklenmektedir. Dönem başında garanti karşılığı yoktu. Bu kalem nedeniyle dönemin ertelenmiş vergi gideri veya geliri kaç ₺'dir?",
        {
            'A': '14.000 ₺ ertelenmiş vergi geliri',
            'B': 'Etki yok',
            'C': '70.000 ₺ ertelenmiş vergi geliri',
            'D': '56.000 ₺ ertelenmiş vergi geliri',
            'E': '14.000 ₺ ertelenmiş vergi gideri',
        },
        'A',
        'Karşılık indirilebilir geçici fark yaratır ve 70.000 × %20 = 14.000 ₺ **ertelenmiş vergi varlığı** tanınır. Varlıktaki artış kâr veya zararda **ertelenmiş vergi geliri** (vergi giderini azaltan kalem) olarak gösterilir.',
        'TMS 12 p. 24, 26(a)',
    ),
    # düzey 2
    '0032': patch(
        "TMS 12'ye göre bir döneme ait kâr veya zararın belirlenmesinde dâhil edilen cari vergi ile ertelenmiş verginin toplamı hangi kavramla ifade edilir?",
        {
            'A': 'Vergilendirilebilir kâr',
            'B': 'Cari vergi',
            'C': 'Vergi gideri',
            'D': 'Ertelenmiş vergi',
            'E': 'Muhasebe kârı',
        },
        'C',
        "TMS 12 p. 5'e göre **vergi gideri (geliri)**, döneme ait kâr veya zararın belirlenmesinde dâhil edilen cari vergi ile ertelenmiş vergi toplamıdır.",
        'TMS 12 p. 5',
    ),
    # düzey 2
    '0033': patch(
        'Bir işletmenin dönem içinde ertelenmiş vergi yükümlülüğündeki artış, tamamen kâr veya zararda tanınan işlemlerden kaynaklanmaktadır. Bu artış kâr veya zarar tablosunda nasıl gösterilir?',
        {
            'A': 'Cari vergi geliri',
            'B': 'Ertelenmiş vergi gideri',
            'C': 'Finansman gideri',
            'D': 'Ertelenmiş vergi geliri',
            'E': 'Diğer kapsamlı gelir',
        },
        'B',
        "TMS 12 p. 58'e göre cari ve ertelenmiş vergi, kâr veya zarar dışında muhasebeleştirilen işlemlerden kaynaklanmadıkça gelir veya gider olarak kâr veya zarara dâhil edilir; yükümlülükteki artış **ertelenmiş vergi gideridir**.",
        'TMS 12 p. 58',
    ),
    # düzey 2
    '0034': patch(
        "Bir işletmenin makinesinin defter değeri 700.000 ₺, vergi mevzuatına göre daha yavaş amortisman ayrıldığı için vergiye esas değeri 760.000 ₺'dir. Vergi oranı %20'dir ve yeterli kâr beklenmektedir. Tanınacak ertelenmiş vergi hangisidir?",
        {
            'A': '60.000 ₺ ertelenmiş vergi varlığı',
            'B': 'Ertelenmiş vergi doğmaz',
            'C': '140.000 ₺ ertelenmiş vergi varlığı',
            'D': '12.000 ₺ ertelenmiş vergi yükümlülüğü',
            'E': '12.000 ₺ ertelenmiş vergi varlığı',
        },
        'E',
        'Varlığın defter değeri vergiye esas değerinden küçük olduğundan **indirilebilir geçici fark** vardır: (760.000 − 700.000) × %20 = **12.000 ₺ ertelenmiş vergi varlığı**.',
        'TMS 12 p. 24',
    ),
    # düzey 3
    '0035': patch(
        "Bir işletmenin ertelenmiş vergi yükümlülüğü dönem içinde 40.000 ₺ artmıştır. Artışın 15.000 ₺'lik kısmı maddi duran varlık yeniden değerleme artışından, kalanı vergide hızlı amortismandan kaynaklanmaktadır. Kâr veya zarar tablosuna yansıyacak ertelenmiş vergi gideri kaç ₺'dir?",
        {
            'A': '55.000',
            'B': '40.000',
            'C': '15.000',
            'D': '25.000',
            'E': '0',
        },
        'D',
        "TMS 12 p. 61A'ya göre yeniden değerlemeye ilişkin 15.000 ₺ **diğer kapsamlı gelirde** tanınır; hızlı amortismandan kaynaklanan kısım kâr veya zarara yansır: 40.000 − 15.000 = **25.000 ₺**.",
        'TMS 12 p. 58, 61A',
    ),
    # düzey 3
    '0036': patch(
        'Bir işletme birleşmesinde edinilen bir markanın gerçeğe uygun değeri 1.000.000 ₺, edinilen işletmedeki vergiye esas değeri sıfırdır; oluşan geçici fark için ertelenmiş vergi yükümlülüğü tanınmıştır. Bu ertelenmiş vergi yükümlülüğü birleşme muhasebesini nasıl etkiler?',
        {
            'A': 'Şerefiyeyi artırır',
            'B': 'Diğer kapsamlı gelire alınır',
            'C': 'Kâr veya zarara gider yazılır',
            'D': 'Şerefiyeyi azaltır',
            'E': 'Etkilemez',
        },
        'A',
        "TMS 12 p. 19 ve 66'ya göre işletme birleşmesinde tanımlanabilir varlıkların gerçeğe uygun değeri ile vergiye esas değeri arasındaki farklar ertelenmiş vergi doğurur; bu ertelenmiş vergi **tanımlanabilir net varlıkları azalttığı için şerefiyeyi artırır**.",
        'TMS 12 p. 19, 66',
    ),
    # düzey 3
    '0037': patch(
        "Bir işletmenin dönem başında 200.000 ₺ vergilendirilebilir geçici farkı ve %20 oranla ölçülmüş 40.000 ₺ ertelenmiş vergi yükümlülüğü vardır. Dönem içinde geçici fark değişmemiş, ancak geri çevrilme dönemine ilişkin oran %25'e yükseltilerek yasalaşmıştır. Oran değişikliğinin kâr veya zarar etkisi hangisidir?",
        {
            'A': 'Etki yok',
            'B': '10.000 ₺ ertelenmiş vergi gideri',
            'C': '50.000 ₺ ertelenmiş vergi gideri',
            'D': '10.000 ₺ ertelenmiş vergi geliri',
            'E': '10.000 ₺ geçmiş yıllar düzeltmesi',
        },
        'B',
        "Yükümlülük yeni oranla 200.000 × %25 = 50.000 ₺'ye yükselir. TMS 12 p. 60'a göre oran değişikliğinden doğan değişim, ilgili kalem kâr veya zararda tanındıysa **kâr veya zarara** yansır: **10.000 ₺ gider**.",
        'TMS 12 p. 47, 60',
    ),
    # düzey 3
    '0038': patch(
        'Bir bağlı ortaklık, ana ortaklığa dağıttığı kâr payı üzerinden kaynakta vergi kesintisi (stopaj) yapmıştır; bu vergi ana ortaklığın elde ettiği kâr payı üzerinden alınan bir vergidir. Bu stopaj vergisi hangi standardın kapsamındadır?',
        {
            'A': 'TMS 37',
            'B': 'TFRS 9',
            'C': 'TMS 12',
            'D': 'TMS 19',
            'E': 'TMS 20',
        },
        'C',
        "TMS 12 p. 2'ye göre gelir vergileri, vergilendirilebilir kâr üzerinden alınan bütün yurt içi ve yurt dışı vergileri ve **bağlı ortaklık, iştirak veya iş ortaklıklarının raporlayan işletmeye dağıttığı kâr payları üzerinden ödenecek stopaj vergileri** gibi vergileri kapsar.",
        'TMS 12 p. 2',
    ),
    # düzey 3
    '0039': patch(
        "Aşağıdakilerden hangileri TMS 12'ye göre doğrudur?\n\nI. Ertelenmiş vergi, raporlama tarihinden sonra yasalaşan oranla ölçülür\n\nII. Yeniden değerleme artışının vergisi diğer kapsamlı gelirde tanınır\n\nIII. Koşullar sağlanırsa ertelenmiş vergi varlık ve yükümlülükleri netleştirilir",
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'Yalnız II',
            'D': 'Yalnız III',
            'E': 'I, II ve III',
        },
        'A',
        "TMS 12 p. 61A'ya göre DKG kalemlerinin vergisi DKG'de tanınır (II); p. 74'e göre koşullar sağlanırsa netleştirme yapılır (III). p. 47'ye göre ölçüm **raporlama dönemi sonunda yasalaşmış** oranla yapılır (I yanlış).",
        'TMS 12 p. 47, 61A, 74',
    ),
    # düzey 2
    '0040': patch(
        'Aşağıdakilerden hangileri doğrudur?\n\nI. Peşin tahsil edilip vergilendirilen gelirin vergiye esas değeri sıfırdır\n\nII. Vergide indirilmiş tahakkuk etmiş ücret borcu indirilebilir geçici fark doğurur\n\nIII. 2021 değişikliğiyle kiralamalarda ilk tanıma istisnası uygulanır',
        {
            'A': 'Yalnız II',
            'B': 'I ve III',
            'C': 'I, II ve III',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'E',
        "TMS 12 p. 8'e göre peşin tahsil edilip vergilendirilen gelirin vergiye esas değeri sıfırdır (I). Vergide zaten indirilmiş ücret borcunda **geçici fark yoktur** (II yanlış); p. 22A'ya göre eşit geçici fark doğuran kiralamalarda ilk tanıma istisnası **uygulanmaz** (III yanlış).",
        'TMS 12 p. 7-8, 15(b)',
    ),
    # düzey 2
    '0041': patch(
        'Bir işletmenin tahakkuk eden ancak ödenmemiş 90.000 ₺ ücret borcu vardır; bu tutar vergi mevzuatına göre de tahakkuk ettiği dönemde gider olarak indirilmiştir. Borcun vergiye esas değeri ve geçici fark hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Vergiye esas değer 45.000 ₺',
            'B': 'Geçici fark 90.000 ₺',
            'C': 'Vergiye esas değer 0, vergilendirilebilir fark var',
            'D': 'Vergiye esas değer 90.000 ₺, geçici fark yok',
            'E': 'Vergiye esas değer 0, indirilebilir fark var',
        },
        'D',
        "TMS 12 p. 8'e göre borcun vergiye esas değeri, defter değerinden gelecek dönemlerde vergi açısından **indirilecek tutar** düşülerek bulunur. Gider zaten indirildiğinden gelecekte indirilecek tutar yoktur; vergiye esas değer 90.000 ₺'dir ve **geçici fark oluşmaz**.",
        'TMS 12 p. 7-8',
    ),
    # düzey 3
    '0042': patch(
        "Bir işletme brüt tutarı 1.000.000 ₺ olan ticari alacakları için 100.000 ₺ beklenen kredi zararı karşılığı ayırmıştır; vergi mevzuatı bu karşılığı alacak kesinleşinceye kadar gider olarak kabul etmemektedir. Vergi oranı %20'dir ve gelecekte yeterli vergilendirilebilir kâr beklenmektedir. Tanınacak ertelenmiş vergi hangisidir?",
        {
            'A': 'Ertelenmiş vergi doğmaz',
            'B': '100.000 ₺ ertelenmiş vergi varlığı',
            'C': '20.000 ₺ ertelenmiş vergi yükümlülüğü',
            'D': '200.000 ₺ ertelenmiş vergi varlığı',
            'E': '20.000 ₺ ertelenmiş vergi varlığı',
        },
        'E',
        "Alacağın defter değeri 900.000 ₺, vergiye esas değeri 1.000.000 ₺'dir; varlığın defter değeri daha küçük olduğundan **indirilebilir geçici fark** 100.000 ₺ vardır. TMS 12 p. 24'e göre **ertelenmiş vergi varlığı**: 100.000 × %20 = **20.000 ₺**.",
        'TMS 12 p. 5, 24',
    ),
    # düzey 3
    '0043': patch(
        "Bir işletme 600.000 ₺'ye aldığı ve kalıntı değeri olmayan bir makineyi muhasebede 10 yıl, vergide 5 yıl üzerinden doğrusal amortismana tabi tutmaktadır. Vergi oranı %20'dir. 2. yılın sonunda finansal durum tablosunda yer alacak ertelenmiş vergi hangisidir?",
        {
            'A': '120.000 ₺ ertelenmiş vergi yükümlülüğü',
            'B': '48.000 ₺ ertelenmiş vergi yükümlülüğü',
            'C': '24.000 ₺ ertelenmiş vergi yükümlülüğü',
            'D': '12.000 ₺ ertelenmiş vergi yükümlülüğü',
            'E': '24.000 ₺ ertelenmiş vergi varlığı',
        },
        'C',
        "2. yıl sonunda defter değeri 600.000 − 120.000 = 480.000 ₺, vergiye esas değer 600.000 − 240.000 = 360.000 ₺'dir. Vergide hızlı amortisman **vergilendirilebilir geçici fark** yaratır: (480.000 − 360.000) × %20 = **24.000 ₺ ertelenmiş vergi yükümlülüğü**.",
        'TMS 12 p. 17(b)',
    ),
    # düzey 2
    '0044': patch(
        'Bir işletmenin kâr veya zarar tablosunda gider olarak yazılan, ancak vergi mevzuatına göre hiçbir dönemde indirilemeyecek 50.000 ₺ kanunen kabul edilmeyen gider (örneğin vergi cezası) bulunmaktadır. Bu kalem için ertelenmiş vergi hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ertelenmiş vergi doğmaz',
            'B': 'Ertelenmiş vergi yükümlülüğü doğar',
            'C': 'Ertelenmiş vergi varlığı doğar',
            'D': 'Diğer kapsamlı gelirde vergi doğar',
            'E': 'Gelecek yıl ertelenmiş vergi doğar',
        },
        'A',
        "TMS 12 p. 5'e göre geçici farklar, defter değeri ile vergiye esas değer arasındaki ve **gelecekte tersine dönecek** farklardır. Hiçbir dönemde indirilemeyecek giderler kalıcı farktır; **ertelenmiş vergi doğurmaz**.",
        'TMS 12 p. 5',
    ),
    # düzey 3
    '0045': patch(
        'Bir işletme bir kiralamanın başlangıcında 1.000.000 ₺ kullanım hakkı varlığı ve aynı tutarda kira yükümlülüğü tanımıştır; vergi mevzuatında kira ödemeleri ödendikçe gider yazılmaktadır. İşlem ne muhasebe kârını ne vergi kârını etkilemiştir ve eşit tutarda vergilendirilebilir ve indirilebilir geçici fark doğmuştur. 2021 değişikliğine göre ne yapılır?',
        {
            'A': 'Varlık tanınır, yükümlülük tanınmaz',
            'B': 'Yükümlülük tanınır, varlık tanınmaz',
            'C': 'Ertelenmiş vergi tanınmaz',
            'D': 'İlk tanıma istisnası uygulanır',
            'E': 'Ertelenmiş vergi varlığı ve yükümlülüğü tanınır',
        },
        'E',
        "TMS 12 p. 15(b) ve 22A'ya göre (2021 değişikliği) ilk tanıma istisnası, işlem anında **eşit tutarda vergilendirilebilir ve indirilebilir geçici fark doğuran** işlemlere (kiralamalar, söküm yükümlülükleri) uygulanmaz; ertelenmiş vergi varlığı ve yükümlülüğü ayrı ayrı tanınır.",
        'TMS 12 p. 15(b), 22A',
    ),
    # düzey 2
    '0046': patch(
        'Bir işletme son üç yıldır üst üste vergi zararı açıklamıştır ve gelecekte vergilendirilebilir kâr elde edeceğine dair ikna edici kanıt yoktur; yeterli vergilendirilebilir geçici farkı da bulunmamaktadır. Kullanılmamış vergi zararları için ertelenmiş vergi varlığı hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Diğer kapsamlı gelirde tanınır',
            'B': 'Tanınmaz',
            'C': 'Tamamı tanınır',
            'D': 'Özkaynakta tanınır',
            'E': 'Yarısı tanınır',
        },
        'B',
        "TMS 12 p. 35'e göre kullanılmamış vergi zararlarının varlığı gelecekte kâr elde edilemeyebileceğinin güçlü kanıtıdır; yakın geçmişte zarar eden işletme ancak **yeterli vergilendirilebilir geçici farkı veya ikna edici başka kanıtı** varsa ertelenmiş vergi varlığı tanır.",
        'TMS 12 p. 35',
    ),
    # düzey 3
    '0047': patch(
        'Bir işletme geçmiş yıllarda 200.000 ₺ ertelenmiş vergi varlığı tanımıştır. Bu yıl sonunda, gelecekte bu varlığın bir kısmından yararlanmaya yetecek vergilendirilebilir kâr elde edilmesinin muhtemel olduğunu belirlemiştir. İşletme ne yapar?',
        {
            'A': 'Varlığı artırır',
            'B': 'Varlığı korur',
            'C': 'Varlığı özkaynağa aktarır',
            'D': 'Varlığın defter değerini azaltır',
            'E': 'Önceki yılları düzeltir',
        },
        'D',
        "TMS 12 p. 56'ya göre ertelenmiş vergi varlığının defter değeri her raporlama döneminde gözden geçirilir; varlığın bir kısmından veya tamamından yararlanmaya **yetecek vergilendirilebilir kârın muhtemel olmadığı ölçüde** defter değeri azaltılır; koşullar düzelirse azaltım iptal edilir.",
        'TMS 12 p. 56',
    ),
    # düzey 3
    '0048': patch(
        "Bir işletmenin dönemin vergilendirilebilir kârı 1.000.000 ₺, vergi oranı %25'tir. Ertelenmiş vergi yükümlülüğü dönem başında 40.000 ₺, dönem sonunda 55.000 ₺'dir; değişimin tamamı kâr veya zarardaki kalemlerden kaynaklanmaktadır. Kâr veya zarar tablosundaki toplam vergi gideri kaç ₺'dir?",
        {
            'A': '235.000',
            'B': '305.000',
            'C': '265.000',
            'D': '15.000',
            'E': '250.000',
        },
        'C',
        'Cari vergi gideri 1.000.000 × %25 = 250.000 ₺; ertelenmiş vergi yükümlülüğündeki artış 55.000 − 40.000 = 15.000 ₺ ertelenmiş vergi gideridir. Toplam: **265.000 ₺**.',
        'TMS 12 p. 58, 77',
    ),
    # düzey 3
    '0049': patch(
        "Bir işletmenin muhasebe kârı 1.000.000 ₺, kâr veya zarardaki toplam vergi gideri 280.000 ₺'dir; yasal vergi oranı %25'tir. Aradaki fark kanunen kabul edilmeyen giderlerden kaynaklanmaktadır. TMS 12'ye göre işletmenin bu farkı açıklaması hangi açıklama türüdür?",
        {
            'A': 'Bölümlere göre raporlama',
            'B': 'Sermaye yönetimi açıklaması',
            'C': 'Kâr payı açıklaması',
            'D': 'Hisse başına kazanç açıklaması',
            'E': 'Vergi gideri ile muhasebe kârı mutabakatı',
        },
        'E',
        "TMS 12 p. 81(c)'ye göre işletme, vergi gideri ile **muhasebe kârının uygulanabilir vergi oranıyla çarpımı** arasında sayısal mutabakat (veya etkin vergi oranı mutabakatı) sunar; kalıcı farklar bu mutabakatta gösterilir.",
        'TMS 12 p. 81(c)',
    ),
    # düzey 2
    '0050': patch(
        "Bir işletmenin 150.000 ₺ ertelenmiş vergi varlığının 60.000 ₺'lik kısmının gelecek 12 ay içinde gerçekleşmesi beklenmektedir. Ertelenmiş vergi varlığı finansal durum tablosunda nasıl sınıflandırılır?",
        {
            'A': '60.000 ₺ dönen, 90.000 ₺ duran',
            'B': 'Kısa vadeli borçtan düşülür',
            'C': 'Özkaynak kalemi',
            'D': 'Tamamı dönen varlık',
            'E': 'Tamamı duran varlık',
        },
        'E',
        "TMS 1 p. 56'ya göre işletme dönen/duran ayrımı yaptığında **ertelenmiş vergi varlıklarını dönen varlık olarak sınıflandırmaz**; tamamı duran varlıktır.",
        'TMS 12 p. 71; TMS 1 p. 56',
    ),
    # düzey 2
    '0051': patch(
        'Bir işletme maddi duran varlıklarını yeniden değerlemiş ve vergi mevzuatı da aynı tarihte vergiye esas değeri aynı tutarda yükseltmiştir. Yeniden değerleme için geçici fark hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İndirilebilir geçici fark doğar',
            'B': 'Vergi zararı doğar',
            'C': 'Vergilendirilebilir geçici fark doğar',
            'D': 'Geçici fark doğmaz',
            'E': 'Kalıcı fark doğar',
        },
        'D',
        "TMS 12 p. 20'ye göre yeniden değerleme vergi amacıyla da yapılır ve **vergiye esas değer aynı tutarda düzeltilirse** defter değeri ile vergiye esas değer arasında fark oluşmaz; ertelenmiş vergi doğmaz.",
        'TMS 12 p. 17, 20',
    ),
    # düzey 3
    '0052': patch(
        "Bir işletme araştırma giderlerini TMS 38'e göre oluştuğu dönemde gider yazmıştır; vergi mevzuatı bu 60.000 ₺'yi gelecek üç yılda eşit indirmeye izin vermektedir. Vergi oranı %25'tir ve yeterli kâr beklenmektedir. Tanınacak ertelenmiş vergi hangisidir?",
        {
            'A': '5.000 ₺ ertelenmiş vergi varlığı',
            'B': '15.000 ₺ ertelenmiş vergi varlığı',
            'C': '60.000 ₺ ertelenmiş vergi varlığı',
            'D': 'Ertelenmiş vergi doğmaz',
            'E': '15.000 ₺ ertelenmiş vergi yükümlülüğü',
        },
        'B',
        "TMS 12 p. 9 ve 26(b)'ye göre finansal durum tablosunda varlık olarak tanınmayan ancak vergiye esas değeri olan kalemler (vergide gelecekte indirilecek araştırma gideri) **indirilebilir geçici fark** yaratır: 60.000 × %25 = **15.000 ₺ ertelenmiş vergi varlığı**.",
        'TMS 12 p. 26(b)',
    ),
    # düzey 3
    '0053': patch(
        "Bir işletmenin ertelenmiş vergi varlığı dönem başında 90.000 ₺, dönem sonunda 60.000 ₺'dir; değişim kâr veya zarardaki kalemlerden kaynaklanmaktadır ve başka ertelenmiş vergi kalemi yoktur. Dönemin ertelenmiş vergi etkisi hangisidir?",
        {
            'A': '60.000 ₺ ertelenmiş vergi gideri',
            'B': 'Etki yok',
            'C': '90.000 ₺ ertelenmiş vergi gideri',
            'D': '30.000 ₺ ertelenmiş vergi gideri',
            'E': '30.000 ₺ ertelenmiş vergi geliri',
        },
        'D',
        "Ertelenmiş vergi varlığının 90.000 ₺'den 60.000 ₺'ye **azalması**, önceki dönemlerde tanınan vergi avantajının kullanıldığını gösterir ve **30.000 ₺ ertelenmiş vergi gideri** doğurur.",
        'TMS 12 p. 58',
    ),
    # düzey 2
    '0054': patch(
        "Bir işletme GUDKZ olarak ölçtüğü hisse senetlerinde 150.000 ₺ değer artışı kazancı tanımıştır; vergi mevzuatına göre kazanç hisseler satıldığında vergilendirilecektir. Vergi oranı %20'dir. Ertelenmiş vergi etkisi hangisidir?",
        {
            'A': "30.000 ₺ yükümlülük, DKG'de",
            'B': '30.000 ₺ yükümlülük, kâr veya zararda',
            'C': 'Ertelenmiş vergi doğmaz',
            'D': '30.000 ₺ varlık, kâr veya zararda',
            'E': '150.000 ₺ yükümlülük, kâr veya zararda',
        },
        'B',
        "Değer artışı varlığın defter değerini vergiye esas değerin üzerine çıkarır (**vergilendirilebilir geçici fark**); kazanç kâr veya zararda tanındığından TMS 12 p. 58'e göre ertelenmiş vergi de kâr veya zarara yansır: 150.000 × %20 = **30.000 ₺ yükümlülük**.",
        'TMS 12 p. 17, 58',
    ),
    # düzey 3
    '0055': patch(
        "Bir işletmede muhasebe kârı 800.000 ₺, vergide henüz indirilemeyen 50.000 ₺ karşılık, vergide 30.000 ₺ fazla amortisman, oran %25 iken başka bir kalem yoksa, kâr veya zarar tablosundaki toplam vergi gideri kaç ₺'dir?",
        {
            'A': '205.000',
            'B': '212.500',
            'C': '200.000',
            'D': '185.000',
            'E': '217.500',
        },
        'C',
        "Cari vergi 205.000 ₺; karşılık için 12.500 ₺ ertelenmiş vergi geliri, amortisman için 7.500 ₺ ertelenmiş vergi gideri doğar. Toplam: 205.000 − 12.500 + 7.500 = **200.000 ₺**; yalnız geçici farklar olduğunda toplam gider muhasebe kârı × oran'a eşittir.",
        'TMS 12 p. 5, 58',
    ),
    # düzey 1
    '0056': patch(
        "TMS 12'ye göre bir döneme ait vergilendirilebilir kâr üzerinden ödenecek gelir vergisi tutarı hangi kavramla ifade edilir?",
        {
            'A': 'Vergiye esas değer',
            'B': 'Geçici fark',
            'C': 'Ertelenmiş vergi',
            'D': 'Vergi gideri',
            'E': 'Cari vergi',
        },
        'E',
        "TMS 12 p. 5'e göre **cari vergi**, bir döneme ait vergilendirilebilir kâr (vergi zararı) üzerinden ödenecek (geri alınacak) gelir vergisi tutarıdır.",
        'TMS 12 p. 5',
    ),
    # düzey 3
    '0057': patch(
        'Bir işletme, ertelenmiş vergi varlığının geri kazanılabilirliğini değerlendirirken vergilendirilebilir kârı artıracak bir satış ve geri kiralama işlemini gerçekleştirebileceğini belirlemiştir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Gelecek vergilendirilebilir kâr tahmini yapılır',
            'B': 'Fırsatlar gerçekçi ve uygulanabilir olmalıdır',
            'C': 'Vergi planlama fırsatları değerlendirmede dikkate alınamaz',
            'D': 'Mevcut vergilendirilebilir geçici farklar da değerlendirilir',
            'E': 'Vergi planlama fırsatları dikkate alınabilir',
        },
        'C',
        "TMS 12 p. 29(b) ve 30'a göre işletme, ertelenmiş vergi varlığı için yeterli vergilendirilebilir kâr bulunup bulunmadığını değerlendirirken, uygun dönemlerde vergilendirilebilir kâr yaratacak **vergi planlama fırsatlarını** dikkate alabilir.",
        'TMS 12 p. 29(b), 30',
    ),
    # düzey 2
    '0058': patch(
        'Aşağıdaki kalemlerden hangisi indirilebilir geçici fark doğurmaz?',
        {
            'A': 'Vergide kabul edilmeyen stok karşılığı',
            'B': 'Vergide kabul edilmeyen garanti karşılığı',
            'C': 'Ödendiğinde indirilecek kıdem karşılığı',
            'D': 'Vergide daha hızlı ayrılan amortisman',
            'E': 'Peşin tahsil edilip vergilendirilen gelir',
        },
        'D',
        'Vergide daha hızlı amortisman, varlığın defter değerini vergiye esas değerinin üzerinde bırakır ve **vergilendirilebilir** geçici fark doğurur. Diğer kalemler indirilebilir geçici fark doğurarak ertelenmiş vergi varlığına yol açar.',
        'TMS 12 p. 15, 24',
    ),
    # düzey 2
    '0059': patch(
        'Aşağıdakilerden hangileri ertelenmiş vergi yükümlülüğü doğurur?\n\nI. Vergide muhasebeye göre daha hızlı ayrılan amortisman\n\nII. Vergide ödendiğinde indirilecek kıdem tazminatı karşılığı\n\nIII. Tahakkuk ettirilip vergide tahsilde vergilendirilecek faiz geliri',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'Yalnız III',
        },
        'D',
        'Hızlı vergi amortismanı (I) ve tahakkuk eden ancak tahsilde vergilendirilecek faiz (III) varlıkların defter değerini vergiye esas değerin üzerinde bırakır ve **vergilendirilebilir geçici fark** yaratır. Kıdem tazminatı karşılığı (II) **indirilebilir** geçici farktır ve ertelenmiş vergi varlığı doğurur.',
        'TMS 12 p. 15, 24',
    ),
    # düzey 3
    '0060': patch(
        "Aşağıdakilerden hangileri TMS 12'ye göre doğrudur?\n\nI. Şerefiyenin ilk tanınmasından doğan fark için ertelenmiş vergi yükümlülüğü tanınmaz\n\nII. Ertelenmiş vergi yükümlülükleri bugünkü değerine iskonto edilir\n\nIII. Kalıcı farklar ertelenmiş vergi doğurmaz",
        {
            'A': 'I ve III',
            'B': 'Yalnız III',
            'C': 'I ve II',
            'D': 'Yalnız I',
            'E': 'II ve III',
        },
        'A',
        "TMS 12 p. 15(a) ve 21'e göre şerefiyenin ilk tanınmasında EVY tanınmaz (I); kalıcı farklar geçici fark olmadığından ertelenmiş vergi doğurmaz (III). p. 53'e göre ertelenmiş vergi **iskonto edilmez** (II yanlış).",
        'TMS 12 p. 15, 21, 53',
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
    print(f"1 paket / {len(PATCHES)} soru ('TMS 12 Gelir Vergileri' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
