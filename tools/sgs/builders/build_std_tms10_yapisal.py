#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TMS 10 Raporlama Doneminden Sonraki Olaylar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gercek sinav profiliyle yeniden yazim (senaryo kok + kisa sik). Eski surum 64 mutlak ifadeli celdirici tasiyordu (kor %38). Kapsam: onay tarihi ve donemin sinirlari (denetim kurulu, kar duyurusu), duzeltme gerektiren olaylar (dava sonucu ve uzlasma, iflas, stoklarin sonraki satisi ve NGD, ikramiye, maliyet/satis bedelinin belirlenmesi, hile/hata, garanti), duzeltme gerektirmeyen olaylar (piyasa dususu, kar payi, yangin/sel, birlesme, vergi orani, kur, yeniden yapilandirma, kamulastirma, davalar), sureklilik, aciklamalar; TMS 1 p. 74, TMS 8 ve TMS 12 ile sinirlar. Gercek sinavin en sik kalibi (stok NGD + onaydan once satis) farkli tutar ve yapilarla islendi. 19 hesap sorusu modulde hesaplandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: TMS 10 Raporlama Doneminden Sonraki Olaylar (KGK); TMS 1, TMS 2, TMS 8, TMS 12, TMS 37 ilgili paragraflar
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/tms_10_sonraki_olaylar.json"
STYLE_REF = 'SGS Muhasebe Standartlari (gercek sinav profiline kalibre: senaryo kok + kisa sik)'
ONEK = "std-tms10-gen-"


def patch(stem, options, answer, solution, ref='TMS 10 Raporlama Doneminden Sonraki Olaylar'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Bir işletmenin 31.12.2025 tarihli finansal tabloları yönetim kurulunca 12 Mart 2026'da yayımlanmak üzere onaylanmış; tablolar 20 Mart'ta kamuya açıklanmış ve 25 Nisan 2026'daki genel kurulda kabul edilmiştir. Raporlama döneminden sonraki olaylar dönemi hangi tarihte sona erer?",
        {
            'A': '31 Mart 2026',
            'B': '31 Aralık 2025',
            'C': '12 Mart 2026',
            'D': '25 Nisan 2026',
            'E': '20 Mart 2026',
        },
        'C',
        "TMS 10 p. 3 ve 5'e göre raporlama döneminden sonraki olaylar, raporlama dönemi sonu ile **finansal tabloların yayımlanmak üzere onaylandığı tarih** arasında meydana gelir. Genel kurul onayı sonra olsa da onay tarihi yönetim kurulunun tabloları yayıma onayladığı tarihtir.",
        'TMS 10 p. 3, 5',
    ),
    # düzey 3
    '0002': patch(
        "Bir işletme 31.12.2025 itibarıyla maliyeti 240.000 ₺ olan bir stok kalemi için net gerçekleşebilir değeri 200.000 ₺ tahmin etmiş ve 40.000 ₺ değer düşüklüğü karşılığı ayırmıştır. Stok, tablolar onaylanmadan önce Ocak 2026'da 215.000 ₺'ye satılmış ve 5.000 ₺ satış gideri katlanılmıştır. 31.12.2025 tablolarında olması gereken değer düşüklüğü karşılığı kaç ₺'dir?",
        {
            'A': '35.000',
            'B': '0',
            'C': '45.000',
            'D': '40.000',
            'E': '30.000',
        },
        'E',
        "TMS 10 p. 9(b)(ii)'ye göre raporlama döneminden sonra stokların satışı, dönem sonundaki net gerçekleşebilir değere ilişkin kanıt sağlayan **düzeltme gerektiren olaydır**. NGD 215.000 − 5.000 = 210.000 ₺; karşılık 240.000 − 210.000 = **30.000 ₺** olmalıdır (ayrılan karşılık -10.000 ₺ azaltılır).",
        'TMS 10 p. 9(b)(ii); TMS 2 p. 30',
    ),
    # düzey 3
    '0003': patch(
        "Bir işletmenin 31.12.2025 itibarıyla bir müşteriden 300.000 ₺ alacağı vardır ve bunun için 30.000 ₺ değer düşüklüğü karşılığı ayrılmıştır. Müşterinin mali durumu yıl sonundan önce bozulmaya başlamış; Şubat 2026'da tablolar onaylanmadan önce iflas etmiştir ve alacağın yalnızca %20'sinin tahsil edilebileceği anlaşılmıştır. 31.12.2025 tablolarındaki karşılık kaç ₺ olmalıdır?",
        {
            'A': '300.000',
            'B': '60.000',
            'C': '240.000',
            'D': '30.000',
            'E': '210.000',
        },
        'C',
        "TMS 10 p. 9(b)(i)'ye göre raporlama döneminden sonra bir müşterinin iflası, **raporlama dönemi sonunda alacağın değer düşüklüğüne uğramış olduğunu** gösterir ve düzeltme gerektirir: karşılık 300.000 × %80 = **240.000 ₺** olmalıdır.",
        'TMS 10 p. 9(b)(i)',
    ),
    # düzey 3
    '0004': patch(
        "Bir işletmenin GUDKZ olarak ölçtüğü hisse senetlerinin 31.12.2025'teki gerçeğe uygun değeri 1.000.000 ₺'dir. Ocak 2026'da piyasadaki genel bir düşüş nedeniyle değer 700.000 ₺'ye inmiştir; tablolar henüz onaylanmamıştır. 31.12.2025 tablolarında hisseler kaç ₺ ile gösterilir?",
        {
            'A': '300.000',
            'B': '1.000.000',
            'C': '0',
            'D': '700.000',
            'E': '850.000',
        },
        'B',
        "TMS 10 p. 11'e göre yatırımların piyasa değerinin raporlama döneminden sonra düşmesi, dönem sonundaki durumla değil **sonradan ortaya çıkan koşullarla** ilgilidir; düzeltme gerektirmez. Hisseler **1.000.000 ₺** ile gösterilir, önemliyse düşüş açıklanır.",
        'TMS 10 p. 11',
    ),
    # düzey 2
    '0005': patch(
        "Bir işletmenin ana deposu 20 Ocak 2026'da çıkan yangında tamamen yanmıştır; tablolar onaylanmamıştır ve kayıp önemlidir. Yangın dönem sonundaki koşullarla ilişkili değildir. Bu olay TMS 10'a göre nasıl sınıflandırılır?",
        {
            'A': 'Düzeltme gerektirmeyen olay',
            'B': 'Tahmin değişikliği',
            'C': 'Önceki dönem hatası düzeltmesi',
            'D': 'Düzeltme gerektiren olay',
            'E': 'Olağanüstü kalem',
        },
        'A',
        "TMS 10 p. 22(d)'ye göre raporlama döneminden sonra **yangın gibi bir felaket sonucu önemli bir üretim tesisinin yok olması** düzeltme gerektirmeyen olaydır; niteliği ve tahmini finansal etkisi açıklanır.",
        'TMS 10 p. 22(d)',
    ),
    # düzey 2
    '0006': patch(
        "Bir işletme 31.12.2025'ten sonra, tablolar onaylanmadan önce önemli bir yeniden yapılandırma planını ilan etmiş ve uygulamaya başlamıştır; yıl sonunda böyle bir plan veya zımni mükellefiyet yoktu. 31.12.2025 tablolarında yeniden yapılandırma karşılığı ayrılır mı?",
        {
            'A': 'Ayrılmaz, açıklanır',
            'B': 'Yarısı ayrılır',
            'C': 'Özkaynakta gösterilir',
            'D': 'Koşullu borç olarak tanınır',
            'E': 'Ayrılır',
        },
        'A',
        "TMS 10 p. 22(e)'ye göre raporlama döneminden sonra önemli bir yeniden yapılandırmanın ilan edilmesi veya başlatılması **düzeltme gerektirmeyen olaydır**; dönem sonunda mevcut mükellefiyet olmadığından TMS 37'ye göre karşılık ayrılmaz, olay açıklanır.",
        'TMS 10 p. 22(e)',
    ),
    # düzey 2
    '0007': patch(
        'Bir işletme finansal tablolarının dipnotlarında tabloların hangi tarihte ve kim tarafından yayımlanmak üzere onaylandığını belirtmektedir. Ayrıca ortakların tabloları yayımdan sonra değiştirme yetkisi bulunmaktadır. Bu yetki hakkında ne yapılır?',
        {
            'A': 'Karşılık ayrılır',
            'B': 'Açıklanmaz',
            'C': 'Tablolar yayımlanmaz',
            'D': 'Açıklanır',
            'E': 'Tablolar yeniden onaylanır',
        },
        'D',
        "TMS 10 p. 17'ye göre işletme finansal tabloların **yayımlanmak üzere onaylandığı tarihi ve onaylayanı** açıklar; işletmenin ortakları veya başkaları yayımdan sonra tabloları değiştirme yetkisine sahipse **bu durumu da açıklar**.",
        'TMS 10 p. 17',
    ),
    # düzey 3
    '0008': patch(
        'Bir işletmenin yıl sonunda maliyetle değerlediği stoklarının fiyatı, raporlama döneminden sonra, tablolar onaylanmadan önce ortaya çıkan ve yıl sonunda hiçbir işareti bulunmayan yeni bir rakip ürün nedeniyle hızla düşmüştür. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Olay düzeltme gerektirmez',
            'B': 'Önemliyse olayın niteliği açıklanır',
            'C': 'Düşüş sonradan ortaya çıkan koşullardan kaynaklanır',
            'D': 'Tahmini finansal etki açıklanır',
            'E': 'Stok değer düşüklüğü 31.12.2025 tablolarına yansıtılır',
        },
        'E',
        "TMS 10 p. 9(b)(ii) ve 11'e göre stokların sonraki satışı ancak **dönem sonundaki koşullara kanıt sağlıyorsa** düzeltme gerektirir. Fiyat düşüşü yıl sonunda var olmayan yeni bir koşuldan kaynaklandığından düzeltme gerektirmez; önemliyse açıklanır.",
        'TMS 10 p. 9(b)(ii), 11',
    ),
    # düzey 2
    '0009': patch(
        'Bir işletme raporlama döneminden sonra, tablolar onaylanmadan önce önemli bir faaliyet bölümünü satmak için plan yapıp ilan etmiştir; yıl sonunda böyle bir plan yoktu. Bu olay hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tahmin değişikliği',
            'B': 'Düzeltme gerektirmeyen olay',
            'C': 'Sonraki yıl olayı değildir',
            'D': 'Düzeltme gerektiren olay',
            'E': 'Önceki dönem hatası düzeltmesi',
        },
        'B',
        "TMS 10 p. 22(b)'ye göre raporlama döneminden sonra **bir faaliyetin durdurulmasına yönelik planın ilan edilmesi** düzeltme gerektirmeyen olaydır; TFRS 5 sınıflaması dönem sonunda sağlanmadığından yapılmaz.",
        'TMS 10 p. 22(b)',
    ),
    # düzey 3
    '0010': patch(
        "Bir işletme Aralık 2025'te defter değeri 460.000 ₺ olan bir makineyi satmış ve kontrolünü devretmiştir; satış bedeli sözleşme gereği Ocak 2026'daki bağımsız ekspertizle belirlenecek ve 520.000 ₺ olarak kesinleşmiştir. Tablolar henüz onaylanmamıştır. 2025 yılı kâr veya zararına yansıyacak satış kazancı kaç ₺'dir?",
        {
            'A': '460.000',
            'B': '520.000',
            'C': '60.000',
            'D': '0',
            'E': '980.000',
        },
        'C',
        "TMS 10 p. 9(c)'ye göre raporlama döneminden önce satılan varlıklardan elde edilen tutarın **raporlama döneminden sonra belirlenmesi** düzeltme gerektirir: 520.000 − 460.000 = **60.000 ₺**.",
        'TMS 10 p. 9(c)',
    ),
    # düzey 3
    '0011': patch(
        "Bir işletme 31.12.2025'te maliyeti 320.000 ₺ olan stoklar için NGD'yi 290.000 ₺ tahmin ederek 30.000 ₺ karşılık ayırmıştır. Stoklar tablolar onaylanmadan önce satış giderisiz 330.000 ₺'ye satılmıştır ve fiyatı etkileyen yeni bir koşul yoktur. 31.12.2025 tablolarında stoklar kaç ₺ ile gösterilir?",
        {
            'A': '30.000',
            'B': '320.000',
            'C': '290.000',
            'D': '330.000',
            'E': '300.000',
        },
        'B',
        "Satış dönem sonu NGD'sinin maliyetin üzerinde olduğunu gösterir (**düzeltme gerektiren olay**); TMS 2 p. 9'a göre stoklar maliyet ile NGD'nin düşük olanıyla, yani **320.000 ₺** maliyetle gösterilir ve karşılık iptal edilir.",
        'TMS 10 p. 9(b)(ii); TMS 2 p. 9',
    ),
    # düzey 2
    '0012': patch(
        "Bir işletmenin 31.12.2025 tabloları 10 Mart 2026'da yayımlanmak üzere onaylanmıştır. 20 Mart 2026'da, 2025'te başlamış bir dava işletme aleyhine sonuçlanmıştır. Bu olay 31.12.2025 tabloları bakımından nasıl değerlendirilir?",
        {
            'A': 'TMS 10 kapsamı dışındadır',
            'B': 'Tablolar yeniden onaylanır',
            'C': 'Düzeltme gerektirmeyen olay',
            'D': 'Düzeltme gerektiren olay',
            'E': "Karşılık 2025'e alınır",
        },
        'A',
        "TMS 10 p. 3'e göre sonraki olaylar yalnızca **onay tarihine kadar** gerçekleşen olaylardır. Onay tarihinden sonra gerçekleşen olay onaylanmış tabloları düzeltmez; 2026 tablolarında dikkate alınır.",
        'TMS 10 p. 3, 17',
    ),
    # düzey 3
    '0013': patch(
        "Bir işletmenin 31.12.2025 tabloları Mart 2026'da onaylanıp yayımlanmıştır. Eylül 2026'da, 2025 amortisman hesabında önemli bir matematiksel hata yapıldığı anlaşılmıştır. Bu hata hangi standarda göre ele alınır?",
        {
            'A': 'TMS 8',
            'B': 'TMS 1',
            'C': 'TFRS 5',
            'D': 'TMS 37',
            'E': 'TMS 10',
        },
        'A',
        "Hata tabloların onayından **sonra** bulunduğundan TMS 10 kapsamında değildir; **TMS 8**'e göre önceki dönem hatası olarak 2026 tablolarında karşılaştırmalı tutarlar yeniden düzenlenerek düzeltilir. Onaydan önce bulunsaydı TMS 10 p. 9(e) uyarınca 2025 tabloları düzeltilirdi.",
        'TMS 10 p. 3; TMS 8 p. 41-42',
    ),
    # düzey 3
    '0014': patch(
        "Bir işletmenin yıl sonunda çalışanlarına ikramiye ödeme yönünde hiçbir sözleşmesi, uygulaması veya taahhüdü yoktur. Yönetim kurulu Şubat 2026'da, tablolar onaylanmadan önce, 2025 performansını ödüllendirmek için ilk kez ikramiye dağıtılmasına karar vermiştir. Bu ikramiye nasıl muhasebeleştirilir?",
        {
            'A': '2025 karşılığı olarak',
            'B': 'Özkaynaktan indirilerek',
            'C': '2026 gideri olarak',
            'D': '2025 borcu olarak',
            'E': 'Önceki dönem hatası olarak',
        },
        'C',
        "TMS 10 p. 9(d)'ye göre ikramiye tutarının sonradan belirlenmesi ancak işletmenin **raporlama dönemi sonunda yasal veya zımni mükellefiyeti** varsa düzeltme gerektirir. Dönem sonunda mükellefiyet olmadığından ikramiye karar dönemi olan 2026'nın gideridir.",
        'TMS 10 p. 9(d)',
    ),
    # düzey 2
    '0015': patch(
        "TMS 10'a göre işletmenin, finansal tabloların yayımlanmak üzere onaylandığı tarihi açıklaması kullanıcılar için hangi bilgiyi sağlar?",
        {
            'A': 'Vergi beyan tarihini',
            'B': 'Kâr dağıtım tarihini',
            'C': 'Denetçinin görüş tarihini',
            'D': 'Genel kurul tarihini',
            'E': 'Olayların yansıtıldığı son tarihi',
        },
        'E',
        "TMS 10 p. 18'e göre tabloların onay tarihinin bilinmesi kullanıcılar için önemlidir; çünkü finansal tablolar **bu tarihten sonraki olayları yansıtmaz**.",
        'TMS 10 p. 18',
    ),
    # düzey 3
    '0016': patch(
        "Bir işletme 31.12.2025'te maliyeti 60.000 ₺ olan bir stok kalemi için NGD'nin maliyetin üzerinde olduğunu düşünerek karşılık ayırmamıştır. Stok, yıl sonunda zaten var olan teknik bir kusur nedeniyle tablolar onaylanmadan önce satış giderisiz 48.000 ₺'ye satılabilmiştir. 31.12.2025 tablolarında ayrılması gereken karşılık kaç ₺'dir?",
        {
            'A': '60.000',
            'B': '12.000',
            'C': '0',
            'D': '48.000',
            'E': '108.000',
        },
        'B',
        "Kusur dönem sonunda mevcut olduğundan sonraki satış dönem sonu NGD'sine kanıt sağlar (**düzeltme gerektiren olay**): 60.000 − 48.000 = **12.000 ₺** karşılık ayrılır.",
        'TMS 10 p. 9(b)(ii)',
    ),
    # düzey 3
    '0017': patch(
        "Bir işletmenin 31.12.2025'te birim maliyeti 100 ₺ olan 1.000 birim ürünü vardır. Tablolar onaylanmadan önce 600 birim, yıl sonunda zaten var olan pazar koşulları nedeniyle birimi 90 ₺'den satış giderisiz satılmıştır; kalan 400 birimin de aynı fiyatla satılması beklenmektedir. 31.12.2025 tablolarında ayrılacak toplam karşılık kaç ₺'dir?",
        {
            'A': '90.000',
            'B': '0',
            'C': '4.000',
            'D': '10.000',
            'E': '6.000',
        },
        'D',
        "Sonraki satışlar dönem sonu NGD'sine kanıt sağlar ve aynı koşullar kalan birimler için de geçerlidir: 1.000 × (100 − 90) = **10.000 ₺**.",
        'TMS 10 p. 9(b)(ii); TMS 2 p. 29',
    ),
    # düzey 3
    '0018': patch(
        'Bir işletme raporlama döneminden sonra, tablolar onaylanmadan önce gerçekleşen önemli bir düzeltme gerektirmeyen olayı değerlendirmektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Finansal etkisinin tahmini açıklanır',
            'B': 'Tutarlar tablolara yansıtılır',
            'C': 'Tahmin yapılamıyorsa bu durum açıklanır',
            'D': 'Olayın niteliği açıklanır',
            'E': 'Olay dönem sonu koşullarına kanıt sağlamaz',
        },
        'B',
        "TMS 10 p. 10'a göre işletme finansal tablolarındaki tutarları **düzeltme gerektirmeyen olayları yansıtacak şekilde düzeltmez**; p. 21'e göre önemli olaylar için niteliği ve finansal etkisinin tahmini ya da tahminin yapılamayacağı açıklanır.",
        'TMS 10 p. 10, 21',
    ),
    # düzey 2
    '0019': patch(
        'Aşağıdakilerden hangileri düzeltme gerektiren olaylardandır?\n\nI. Dönem sonunda var olan bir davanın onaydan önce sonuçlanması\n\nII. Onaydan önce ilan edilen kâr payı\n\nIII. Onaydan önce ortaya çıkan ve tabloların hatalı olduğunu gösteren hile',
        {
            'A': 'I ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'Yalnız III',
            'E': 'I, II ve III',
        },
        'A',
        "TMS 10 p. 9(a) ve 9(e)'ye göre dava sonucu (I) ve hile/hata (III) düzeltme gerektirir. p. 12'ye göre sonradan ilan edilen kâr payı **borç olarak tanınmaz** (II düzeltme gerektirmez).",
        'TMS 10 p. 9, 22',
    ),
    # düzey 3
    '0020': patch(
        "Aşağıdakilerden hangileri doğrudur?\n\nI. Müşterinin dönem sonrası iflası, nedeni ne olursa olsun düzeltme gerektirir\n\nII. Dönem sonrası stok satışı dönem sonu NGD'sine kanıt sağlayabilir\n\nIII. Dönem sonrası piyasa değeri düşüşü açıklanabilir, ancak düzeltme gerektirmez",
        {
            'A': 'I ve II',
            'B': 'I ve III',
            'C': 'II ve III',
            'D': 'Yalnız II',
            'E': 'I, II ve III',
        },
        'C',
        "TMS 10 p. 9(b)'ye göre stok satışı dönem sonu NGD'sine kanıt sağlayabilir (II); p. 11'e göre piyasa değeri düşüşü düzeltme gerektirmez (III). İflas ancak **dönem sonunda var olan** bir duruma kanıt sağlıyorsa düzeltme gerektirir; dönem sonrası bir felaketten kaynaklanıyorsa gerektirmez (I yanlış).",
        'TMS 10 p. 9(b), 10-11',
    ),
    # düzey 3
    '0021': patch(
        "Bir işletmenin yönetimi finansal tabloları 5 Mart 2026'da, yönetimden bağımsız üyelerden oluşan denetim kuruluna sunulmak üzere onaylamış; denetim kurulu tabloları 18 Mart 2026'da onaylamış ve tablolar 25 Mart'ta yayımlanmıştır. Sonraki olaylar dönemi hangi tarihte sona erer?",
        {
            'A': '18 Mart 2026',
            'B': '5 Mart 2026',
            'C': '25 Mart 2026',
            'D': '31 Aralık 2025',
            'E': '1 Nisan 2026',
        },
        'B',
        "TMS 10 p. 6'ya göre işletme yönetiminin finansal tabloları, yönetimden bağımsız üyelerden oluşan bir denetim kuruluna sunulmak üzere onaylaması gerekiyorsa, finansal tablolar **yönetimin denetim kuruluna sunmak üzere onayladığı tarihte** yayımlanmak üzere onaylanmış sayılır.",
        'TMS 10 p. 6',
    ),
    # düzey 3
    '0022': patch(
        "Bir işletme 31.12.2025 itibarıyla aleyhine açılmış ve 2025'te meydana gelen bir iş kazasına ilişkin dava için 150.000 ₺ karşılık ayırmıştır. Tablolar onaylanmadan önce mahkeme işletmeyi 220.000 ₺ tazminat ödemeye mahkûm etmiştir. 31.12.2025 tablolarında dava karşılığı kaç ₺ olmalıdır?",
        {
            'A': '60.000',
            'B': '220.000',
            'C': '0',
            'D': '150.000',
            'E': '70.000',
        },
        'B',
        "TMS 10 p. 9(a)'ya göre raporlama döneminden sonra sonuçlanan ve işletmenin **raporlama dönemi sonunda mevcut bir yükümlülüğü olduğunu teyit eden** dava düzeltme gerektiren olaydır; karşılık TMS 37'ye göre güncellenir: **220.000 ₺** (ek 70.000 ₺).",
        'TMS 10 p. 9(a)',
    ),
    # düzey 2
    '0023': patch(
        "Bir işletme, 2025 yılı performansına dayalı olarak çalışanlarına ikramiye ödemeyi yıl sonundan önce taahhüt etmiş; tutar Şubat 2026'da, tablolar onaylanmadan önce 90.000 ₺ olarak kesinleşmiştir. Bu tutar 31.12.2025 tablolarında nasıl yer alır?",
        {
            'A': 'Özkaynaktan indirilir',
            'B': 'Dipnotta açıklanır',
            'C': 'Borç olarak tanınır',
            'D': 'Tanınmaz',
            'E': '2026 gideri olur',
        },
        'C',
        "TMS 10 p. 9(d)'ye göre işletmenin raporlama dönemi sonunda bu tür ödemeleri yapmak için **yasal veya zımni mükellefiyeti** varsa, kâr paylaşımı veya ikramiye tutarının raporlama döneminden sonra belirlenmesi düzeltme gerektiren olaydır; tutar borç ve gider olarak tanınır.",
        'TMS 10 p. 9(d)',
    ),
    # düzey 2
    '0024': patch(
        "Bir işletmenin yönetim kurulu, 31.12.2025 tarihli tablolar onaylanmadan önce 2025 kârından 500.000 ₺ kâr payı dağıtılmasını önermiştir. 31.12.2025 finansal durum tablosunda bu kâr payı için tanınacak borç kaç ₺'dir?",
        {
            'A': '500.000',
            'B': '0',
            'C': 'Kâr payının bugünkü değeri',
            'D': '250.000',
            'E': 'Kâr payının vergi sonrası tutarı',
        },
        'B',
        "TMS 10 p. 12-13'e göre raporlama döneminden sonra dağıtılacağı ilan edilen kâr payları, raporlama dönemi sonunda mevcut bir yükümlülük olmadığından **borç olarak tanınmaz**; TMS 1 uyarınca dipnotlarda açıklanır.",
        'TMS 10 p. 12-13',
    ),
    # düzey 2
    '0025': patch(
        "Bir işletme, tablolar onaylanmadan önce Şubat 2026'da önemli bir rakibini satın alarak büyük bir işletme birleşmesi gerçekleştirmiştir. Birleşmenin finansal etkisi tahmin edilebilmektedir. TMS 10'a göre işletme ne yapar?",
        {
            'A': 'Niteliği ve etkisini açıklar',
            'B': 'Karşılık ayırır',
            'C': 'Bir işlem yapmaz',
            'D': 'Birleşmeyi 2025 tablolarına yansıtarak düzeltir',
            'E': 'Şerefiye tanır',
        },
        'A',
        "TMS 10 p. 21 ve 22(a)'ya göre raporlama döneminden sonraki önemli bir işletme birleşmesi düzeltme gerektirmeyen olaydır; önemli düzeltme gerektirmeyen olayların her biri için **olayın niteliği ve finansal etkisinin tahmini** ya da tahminin yapılamayacağı açıklanır.",
        'TMS 10 p. 21',
    ),
    # düzey 2
    '0026': patch(
        "Bir işletme aleyhine, tamamen raporlama döneminden sonra meydana gelen bir olay nedeniyle Şubat 2026'da önemli bir tazminat davası açılmıştır; tablolar onaylanmamıştır. Bu olay TMS 10'a göre nasıl sınıflandırılır?",
        {
            'A': 'Tahmin değişikliği',
            'B': 'Önceki dönem hatası düzeltmesi',
            'C': 'Koşullu varlık',
            'D': 'Düzeltme gerektiren olay',
            'E': 'Düzeltme gerektirmeyen olay',
        },
        'E',
        "TMS 10 p. 22(k)'ye göre **yalnızca raporlama döneminden sonra meydana gelen olaylardan doğan** önemli davaların başlatılması düzeltme gerektirmeyen olaydır. Dava dönem sonundaki bir olaya dayansaydı durum farklı değerlendirilirdi.",
        'TMS 10 p. 22(k)',
    ),
    # düzey 2
    '0027': patch(
        'Bir işletme dönem sonunda mevcut olan bir koşulla ilgili olarak, tablolar onaylanmadan önce yeni bilgiler edinmiştir; bilgi tablolarda tanınan tutarları etkilemese de dipnottaki koşullu borç açıklamasını değiştirmektedir. Bu bilgi hakkında ne yapılır?',
        {
            'A': 'Gelecek yıl açıklanır',
            'B': 'Tahmin değişikliği yapılır',
            'C': 'Bir işlem yapılmaz',
            'D': 'Açıklamalar güncellenir',
            'E': 'Tablolar yeniden onaylanır',
        },
        'D',
        "TMS 10 p. 19-20'ye göre işletme, raporlama dönemi sonunda mevcut olan koşullar hakkında raporlama döneminden sonra yeni bilgi edinirse, **bu koşullara ilişkin açıklamaları yeni bilgiler ışığında günceller**.",
        'TMS 10 p. 19-20',
    ),
    # düzey 3
    '0028': patch(
        "Bir işletmenin 31.12.2025 tablolarının onayından önce şu olaylar gerçekleşmiştir: yıl sonunda var olan bir davanın sonuçlanması, yıl sonunda satılamayan stokun maliyetin altında satılması, Ocak'ta yaşanan sel felaketi, bir müşterinin yıl sonundan önce başlayan mali sıkıntı sonucu iflası ve 2025'e ait bir hatanın bulunması. Bunlardan hangisi düzeltme gerektirmeyen olaydır?",
        {
            'A': 'Stokun maliyetin altında satılması',
            'B': 'Hatanın bulunması',
            'C': 'Davanın sonuçlanması',
            'D': 'Müşterinin iflası',
            'E': "Ocak'taki sel felaketi",
        },
        'E',
        "TMS 10 p. 3'e göre düzeltme gerektiren olaylar **raporlama dönemi sonunda var olan koşullara** kanıt sağlar. Dava, stok satışı, iflas ve hata bu niteliktedir (p. 9). Dönem sonrasında ortaya çıkan sel felaketi **sonradan doğan koşuldur** ve düzeltme gerektirmez (p. 22(d)).",
        'TMS 10 p. 3, 8-11',
    ),
    # düzey 3
    '0029': patch(
        "Bir işletme 31.12.2025 itibarıyla maliyeti 180.000 ₺ olan ticari malları için NGD'yi 150.000 ₺ tahmin ederek 30.000 ₺ karşılık ayırmıştır. Mallar tablolar onaylanmadan önce satış giderisiz 175.000 ₺'ye satılmış; fiyat artışını sağlayan bir koşul değişikliği yoktur. Ayrılan karşılık kaç ₺ azaltılmalıdır?",
        {
            'A': '35.000',
            'B': '30.000',
            'C': '5.000',
            'D': '0',
            'E': '25.000',
        },
        'E',
        "Onaydan önceki satış dönem sonu NGD'sine kanıt sağlar: olması gereken karşılık 180.000 − 175.000 = 5.000 ₺; ayrılan 30.000 ₺ karşılık **25.000 ₺ azaltılır**.",
        'TMS 10 p. 9(b)(ii); TMS 2 p. 33',
    ),
    # düzey 3
    '0030': patch(
        "Bir işletme, 2025'te bir müşterisine teslim ettiği ayıplı ürünler nedeniyle yıl sonunda herhangi bir karşılık ayırmamıştır; müşteri ayıbı Kasım 2025'te bildirmişti. Şubat 2026'da tablolar onaylanmadan önce taraflar 80.000 ₺ tazminatta uzlaşmıştır. 31.12.2025 tablolarında tanınacak karşılık kaç ₺'dir?",
        {
            'A': 'Dipnotla yetinilir',
            'B': '80.000',
            'C': '0',
            'D': '40.000',
            'E': '160.000',
        },
        'B',
        "Ayıp ve bildirim dönem sonundan önce olduğundan işletmenin raporlama dönemi sonunda **mevcut bir yükümlülüğü** vardır; sonraki uzlaşma bunu teyit eder ve TMS 10 p. 9(a)'ya göre **80.000 ₺** karşılık tanınır.",
        'TMS 10 p. 3, 9(a)',
    ),
    # düzey 3
    '0031': patch(
        "Bir işletme 2025'te meydana gelen bir olay nedeniyle açılan dava için 31.12.2025'te 200.000 ₺ karşılık ayırmıştır. Tablolar onaylanmadan önce taraflar 120.000 ₺ ödemede uzlaşmıştır. 31.12.2025 tablolarındaki karşılık kaç ₺ olmalıdır?",
        {
            'A': '80.000',
            'B': '0',
            'C': '200.000',
            'D': '120.000',
            'E': '320.000',
        },
        'D',
        "Uzlaşma dönem sonundaki mükellefiyetin tutarına kanıt sağlar (**düzeltme gerektiren olay**); karşılık **120.000 ₺**'ye indirilir (80.000 ₺ azaltılır).",
        'TMS 10 p. 9(a); TMS 37 p. 59',
    ),
    # düzey 3
    '0032': patch(
        "Bir işletmenin 5 yıl vadeli kredisinde 31.12.2025 itibarıyla sözleşme koşulu ihlal edilmiş ve banka ödemeyi hemen talep edebilir hâle gelmiştir. Banka Şubat 2026'da, tablolar onaylanmadan önce, ödeme talep etmeyeceğini bildirmiştir. Kredi 31.12.2025 tablolarında nasıl sınıflandırılır?",
        {
            'A': 'Kısa vadeli borç',
            'B': 'Uzun vadeli borç',
            'C': 'Koşullu borç',
            'D': 'Karşılık',
            'E': 'Özkaynak',
        },
        'A',
        "TMS 1 p. 74'e göre dönem sonunda talep edildiğinde ödenecek borç, raporlama döneminden sonra kreditör ödeme talep etmemeyi kabul etse de **kısa vadeli** sınıflandırılır; p. 76 uyarınca bankanın sonraki kararı **düzeltme gerektirmeyen olay** olarak açıklanır.",
        'TMS 10 p. 21; TMS 1 p. 74, 76',
    ),
    # düzey 2
    '0033': patch(
        'Bir işletmenin önemli bir fabrika binası raporlama döneminden sonra, tablolar onaylanmadan önce kamu idaresince kamulaştırılmıştır; yıl sonunda böyle bir işlem başlatılmamıştı. Bu olay nasıl sınıflandırılır?',
        {
            'A': 'Düzeltme gerektirmeyen olay',
            'B': 'Önceki dönem hatası düzeltmesi',
            'C': 'Koşullu varlık',
            'D': 'Düzeltme gerektiren olay',
            'E': 'Tahmin değişikliği',
        },
        'A',
        "TMS 10 p. 22(c)'ye göre raporlama döneminden sonra **önemli varlık alımları, TFRS 5 kapsamında satış amaçlı sınıflandırmalar, diğer elden çıkarmalar veya varlıkların devlet tarafından kamulaştırılması** düzeltme gerektirmeyen olaylardır.",
        'TMS 10 p. 22(c)',
    ),
    # düzey 3
    '0034': patch(
        "Bir fabrikada Aralık 2025'te meydana gelen bir kazada komşu işletmenin mülkü zarar görmüştür. Komşu işletme Şubat 2026'da, tablolar onaylanmadan önce tazminat davası açmıştır; hukuk müşavirine göre davanın kaybedilmesi kuvvetle muhtemeldir ve tutar güvenilir tahmin edilebilmektedir. Bu olay nasıl değerlendirilir?",
        {
            'A': 'TMS 10 kapsamı dışında',
            'B': 'Koşullu varlık',
            'C': 'Önceki dönem hatası',
            'D': 'Düzeltme gerektiren olay',
            'E': 'Düzeltme gerektirmeyen olay',
        },
        'D',
        'Davayı doğuran kaza **raporlama dönemi sonundan önce** gerçekleştiğinden işletmenin dönem sonunda mevcut bir yükümlülüğü vardır; davanın sonradan açılması bu koşula kanıt sağlar ve düzeltme gerektirir. Sadece dönem sonrasındaki olaylardan doğan davalar düzeltme gerektirmez (p. 22(k)).',
        'TMS 10 p. 3, 9(a)',
    ),
    # düzey 3
    '0035': patch(
        'Bir işletmenin faaliyet sonuçları raporlama döneminden sonra kötüleşmiş; yönetim tasfiye niyeti olmadığını, ancak sürekliliğe ilişkin önemli şüphe doğuran bir belirsizlik bulunduğunu değerlendirmiştir. Tablolar henüz onaylanmamıştır. Bu durumda ne yapılır?',
        {
            'A': 'Tasfiye esasına geçilir',
            'B': 'Karşılık ayrılır',
            'C': 'Belirsizlik açıklanır',
            'D': 'Tabloların onayı ertelenir',
            'E': 'Tablolar düzeltilmez ve açıklanmaz',
        },
        'C',
        "TMS 10 p. 16'ya göre sonraki olaylar sürekliliğe ilişkin önemli belirsizlik doğuruyorsa TMS 1 p. 25 uyarınca **bu belirsizlikler açıklanır**; tasfiye kararı veya zorunluluğu yoksa süreklilik esası korunur.",
        'TMS 10 p. 16; TMS 1 p. 25',
    ),
    # düzey 1
    '0036': patch(
        "Bir işletme raporlama döneminden sonra, tablolar onaylanmadan önce bankadan 5 milyon ₺ yeni kredi kullanmıştır. Bu olay TMS 10'a göre nasıl sınıflandırılır?",
        {
            'A': 'Tahmin değişikliği',
            'B': 'Koşullu borç',
            'C': 'Düzeltme gerektiren olay',
            'D': 'Düzeltme gerektirmeyen olay',
            'E': 'Önceki dönem hatası düzeltmesi',
        },
        'D',
        'Yeni kredi kullanımı raporlama döneminden sonra ortaya çıkan bir işlemdir ve dönem sonundaki koşullara kanıt sağlamaz; **düzeltme gerektirmez**, önemliyse açıklanır.',
        'TMS 10 p. 22(i)',
    ),
    # düzey 2
    '0037': patch(
        "Bir işletme Ocak 2026'da, 31.12.2025 tabloları onaylanmadan önce yeni bir müşteriye mal satmıştır; müşteri Şubat 2026'da iflas etmiş ve alacak tahsil edilemez hâle gelmiştir. Bu durum 31.12.2025 tablolarını nasıl etkiler?",
        {
            'A': "Satış 2025'e alınır",
            'B': 'Alacak karşılığı ayrılır',
            'C': 'Hata düzeltmesi yapılır',
            'D': 'Etkilemez',
            'E': 'Tablolar yeniden düzenlenir',
        },
        'D',
        'Satış ve alacak **raporlama döneminden sonra** doğmuştur; 31.12.2025 finansal durum tablosunda böyle bir alacak yoktur. Olay 2026 tablolarının konusudur ve 2025 tablolarını etkilemez.',
        'TMS 10 p. 3',
    ),
    # düzey 3
    '0038': patch(
        "Vergi idaresi Şubat 2026'da, tablolar onaylanmadan önce, işletmenin 2024 yılı işlemlerine ilişkin ek vergi ve gecikme faizi tarh etmiştir; işletme bu riskin farkındaydı ve tarhiyatın kesinleşeceğini değerlendirmektedir. Bu olay 31.12.2025 tabloları bakımından nasıl sınıflandırılır?",
        {
            'A': 'TMS 10 kapsamı dışında',
            'B': 'Düzeltme gerektiren olay',
            'C': '2026 gideri',
            'D': 'Koşullu varlık',
            'E': 'Düzeltme gerektirmeyen olay',
        },
        'B',
        'Vergi borcunu doğuran işlemler raporlama dönemi sonundan önce gerçekleşmiştir; tarhiyat dönem sonunda **var olan bir yükümlülüğe kanıt sağlar** ve düzeltme gerektirir. Tutar TMS 12 ve TMS 37 çerçevesinde tanınır.',
        'TMS 10 p. 3, 9',
    ),
    # düzey 2
    '0039': patch(
        "Aşağıdakilerden hangileri TMS 10'a göre doğrudur?\n\nI. Tabloların onay tarihi ve onaylayan açıklanır\n\nII. Sonraki olaylar dönemi genel kurul tarihinde sona erer\n\nIII. Kâr tahmininin kamuya duyurulması sonraki olaylar dönemini sona erdirmez",
        {
            'A': 'I ve III',
            'B': 'I ve II',
            'C': 'Yalnız I',
            'D': 'Yalnız III',
            'E': 'II ve III',
        },
        'A',
        "TMS 10 p. 17'ye göre onay tarihi ve onaylayan açıklanır (I); p. 7'ye göre kâr bilgisinin duyurulması dönemi sona erdirmez (III). p. 3 ve 5'e göre dönem **yayım için onay tarihinde** sona erer; genel kurul tarihi belirleyici değildir (II yanlış).",
        'TMS 10 p. 3, 6, 17',
    ),
    # düzey 3
    '0040': patch(
        "Aşağıdakilerden hangileri TMS 10'a göre doğrudur?\n\nI. Sonradan tasfiye kararı alınsa da 31.12.2025 tabloları süreklilik esasıyla hazırlanır\n\nII. Onaydan önce önerilen kâr payı dipnotlarda açıklanır\n\nIII. Onaydan önce ilan edilen kâr payı raporlama dönemi sonunda borç olarak tanınır",
        {
            'A': 'II ve III',
            'B': 'I, II ve III',
            'C': 'Yalnız II',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'C',
        "TMS 10 p. 13 ve TMS 1 p. 137'ye göre önerilen kâr payı dipnotta açıklanır (II). p. 14'e göre tasfiye kararı süreklilik esasını **ortadan kaldırır** (I yanlış); p. 12'ye göre bu kâr payı **borç olarak tanınmaz** (III yanlış).",
        'TMS 10 p. 12-15',
    ),
    # düzey 2
    '0041': patch(
        "Bir işletme, finansal tablolarının onayından önce, 15 Şubat 2026'da yıllık kâr tahminini ve bazı seçilmiş finansal bilgilerini basın yoluyla kamuya duyurmuştur; tablolar 10 Mart'ta onaylanmıştır. 20 Şubat'ta meydana gelen bir olay hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': '2026 yılının olayı olarak kapsam dışıdır',
            'B': 'Kapsam dışındadır',
            'C': 'Gelecek yıl olayıdır',
            'D': 'Sonraki olaylar kapsamındadır',
            'E': 'Hata düzeltmesidir',
        },
        'D',
        "TMS 10 p. 7'ye göre raporlama döneminden sonraki olaylar, kâr veya diğer seçilmiş finansal bilgilerin kamuya duyurulmasından **sonra meydana gelse bile finansal tabloların onay tarihine kadar olan** bütün olayları kapsar.",
        'TMS 10 p. 7',
    ),
    # düzey 3
    '0042': patch(
        "Bir işletme 31.12.2025 itibarıyla iki stok kalemini değerlemiştir: A kalemi maliyeti 150.000 ₺, tahmini NGD 130.000 ₺; B kalemi maliyeti 90.000 ₺, tahmini NGD 90.000 ₺. Tablolar onaylanmadan önce A kalemi 145.000 ₺'ye, B kalemi 70.000 ₺'ye satış giderisiz olarak satılmıştır. Kalem bazında 31.12.2025 tablolarında olması gereken toplam stok değer düşüklüğü karşılığı kaç ₺'dir?",
        {
            'A': '10.000',
            'B': '0',
            'C': '25.000',
            'D': '5.000',
            'E': '20.000',
        },
        'C',
        "Onaydan önceki satışlar dönem sonu NGD'sine kanıt sağlar (**düzeltme gerektiren olay**) ve TMS 2 p. 29'a göre değerleme kalem bazında yapılır: A için 150.000 − 145.000 = 5.000 ₺, B için 90.000 − 70.000 = 20.000 ₺; toplam **25.000 ₺**.",
        'TMS 10 p. 9(b)(ii); TMS 2 p. 29',
    ),
    # düzey 2
    '0043': patch(
        "Bir işletme Aralık 2025'te bir makine satın almış, ancak nihai bedel tedarikçiyle yapılan görüşmeler sonucunda Ocak 2026'da, tablolar onaylanmadan önce belirlenmiştir. Bu olay TMS 10'a göre nasıl sınıflandırılır?",
        {
            'A': 'Düzeltme gerektiren olay',
            'B': 'Önceki dönem hatası',
            'C': 'Düzeltme gerektirmeyen olay',
            'D': 'Koşullu varlık',
            'E': 'Tahmin değişikliği',
        },
        'A',
        "TMS 10 p. 9(c)'ye göre **raporlama döneminden önce satın alınan varlıkların maliyetinin** veya satılan varlıklardan elde edilen tutarın raporlama döneminden sonra belirlenmesi düzeltme gerektiren olaydır.",
        'TMS 10 p. 9(c)',
    ),
    # düzey 3
    '0044': patch(
        'Bir işletme, tablolar onaylanmadan önce yapılan iç denetimde bir çalışanın 2025 yılında sahte faturalarla önemli tutarda stok kaydettiğini tespit etmiştir. Bu durum 31.12.2025 tabloları için nasıl ele alınır?',
        {
            'A': 'Dipnotla açıklanır',
            'B': 'Tahmin değişikliği yapılır',
            'C': 'Tablolar düzeltilir',
            'D': 'Bir işlem yapılmaz',
            'E': "2026'da düzeltilir",
        },
        'C',
        "TMS 10 p. 9(e)'ye göre **finansal tabloların hatalı olduğunu gösteren hile veya hataların** raporlama döneminden sonra ortaya çıkması düzeltme gerektiren olaydır; 31.12.2025 tabloları onaylanmadan düzeltilir.",
        'TMS 10 p. 9(e)',
    ),
    # düzey 3
    '0045': patch(
        'Raporlama döneminden sonra, tablolar onaylanmadan önce yasalaşan bir düzenlemeyle kurumlar vergisi oranı değiştirilmiştir; değişiklik ertelenmiş vergi bakiyelerini önemli ölçüde etkileyecektir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Dönem sonunda yürürlükteki oran kullanılır',
            'B': 'Tahmini finansal etki açıklanır',
            'C': 'Olay düzeltme gerektirmez',
            'D': 'Olayın niteliği açıklanır',
            'E': 'Ertelenmiş vergi yeni oranla ölçülür',
        },
        'E',
        "TMS 10 p. 22(h)'ye göre raporlama döneminden sonra **vergi oranlarında veya vergi kanunlarında yürürlüğe giren ya da ilan edilen değişiklikler** düzeltme gerektirmeyen olaydır; TMS 12 uyarınca dönem sonunda yürürlükte olan veya yasalaşmış olan oran kullanılır ve önemli etki açıklanır.",
        'TMS 10 p. 22(h)',
    ),
    # düzey 2
    '0046': patch(
        'Raporlama döneminden sonra, tablolar onaylanmadan önce Türk lirası ABD doları karşısında önemli ölçüde değer kaybetmiştir. İşletmenin önemli döviz borçları vardır. Bu kur değişimi 31.12.2025 tablolarını nasıl etkiler?',
        {
            'A': 'Karşılık ayrılır',
            'B': 'Döviz borçları onay tarihindeki kurla değerlenir',
            'C': 'Düzeltme gerektirmez, açıklanır',
            'D': 'Özkaynakta gösterilir',
            'E': 'Kur farkı 2025 gideri olur',
        },
        'C',
        "TMS 10 p. 22(g)'ye göre raporlama döneminden sonra **döviz kurlarındaki olağandışı büyük değişiklikler** düzeltme gerektirmeyen olaydır; parasal kalemler dönem sonu kuruyla çevrilir, önemli etki açıklanır.",
        'TMS 10 p. 22(g)',
    ),
    # düzey 2
    '0047': patch(
        'Bir işletmenin faaliyet sonuçları ve finansal durumu raporlama döneminden sonra hızla kötüleşmiş; yönetim tablolar onaylanmadan önce işletmeyi tasfiye etmeye karar vermiştir. 31.12.2025 tabloları hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Süreklilik esası kullanılamaz',
            'B': 'Tasfiye 2026 olayı sayılır',
            'C': 'Süreklilik esası korunur ve dipnotta açıklanır',
            'D': "Tablolar 2026'da düzeltilir",
            'E': 'Dipnot açıklaması yeterlidir',
        },
        'A',
        "TMS 10 p. 14-15'e göre yönetim raporlama döneminden sonra işletmeyi tasfiye etmeye veya faaliyetlerine son vermeye karar verirse ya da başka gerçekçi bir seçeneği kalmazsa, finansal tablolar **işletmenin sürekliliği esasına göre hazırlanmaz**; bu, muhasebe esasında temel bir değişikliktir.",
        'TMS 10 p. 14-15',
    ),
    # düzey 2
    '0048': patch(
        "Bir işletme, raporlama döneminden sonra meydana gelen ve dönem sonunda var olan koşullara ilişkin kanıt sağlayan bir olayı tespit etmiştir. TMS 10'a göre bu tür bir olay karşısında işletme ne yapar?",
        {
            'A': 'Tabloların onayını geri çeker',
            'B': "Olayı 2026'ya kaydeder",
            'C': 'Tanınan tutarları düzeltir',
            'D': 'Olayı açıklamakla yetinir',
            'E': 'Olayı yok sayar',
        },
        'C',
        "TMS 10 p. 8'e göre işletme, **düzeltme gerektiren olayları** yansıtmak için finansal tablolarında muhasebeleştirdiği tutarları düzeltir ve daha önce tanımadığı kalemleri tanır.",
        'TMS 10 p. 8',
    ),
    # düzey 2
    '0049': patch(
        'Bir işletme raporlama döneminden sonra, tablolar onaylanmadan önce önemli bir sermaye artırımı yapmış ve büyük bir makine alım taahhüdüne girmiştir. Bu olaylar 31.12.2025 tablolarında nasıl ele alınır?',
        {
            'A': 'Bir işlem yapılmaz, açıklanmaz',
            'B': "Sermaye 2025'e alınır",
            'C': 'Tablolar düzeltilir',
            'D': 'Açıklanır, düzeltilmez',
            'E': 'Karşılık ayrılır',
        },
        'D',
        "TMS 10 p. 22(f) ve (i)'ye göre raporlama döneminden sonraki **önemli adi hisse senedi işlemleri** ve **önemli taahhütlere girilmesi** düzeltme gerektirmeyen olaylardır; önemliyse niteliği ve etkisi açıklanır.",
        'TMS 10 p. 22(f), (i)',
    ),
    # düzey 3
    '0050': patch(
        "Bir işletmenin 31.12.2025 itibarıyla bir bayisinden 400.000 ₺ alacağı vardır ve bunun için 40.000 ₺ karşılık ayrılmıştır. Bayinin yıl sonunda başlamış olan ödeme güçlüğü sonucu Şubat 2026'da yapılan uzlaşmayla alacağın %35'inin tahsil edilemeyeceği kesinleşmiştir. 31.12.2025 tablolarına yansıtılacak ek değer düşüklüğü gideri kaç ₺'dir?",
        {
            'A': '40.000',
            'B': '100.000',
            'C': '140.000',
            'D': '260.000',
            'E': '0',
        },
        'B',
        'Ödeme güçlüğü dönem sonunda mevcut olduğundan olay **düzeltme gerektirir**; gerekli karşılık 400.000 × %35 = 140.000 ₺, ek gider 140.000 − 40.000 = **100.000 ₺**.',
        'TMS 10 p. 9(b)(i)',
    ),
    # düzey 3
    '0051': patch(
        "Bir işletme 31.12.2025'te maliyeti 500.000 ₺ olan mamulleri için NGD'yi 440.000 ₺ tahmin etmiştir. Mamuller tablolar onaylanmadan önce 470.000 ₺'ye satılmış ve satış tutarının %4'ü oranında komisyon ödenmiştir. 31.12.2025 tablolarında olması gereken stok değer düşüklüğü karşılığı kaç ₺'dir?",
        {
            'A': '77.600',
            'B': '78.800',
            'C': '67.600',
            'D': '48.800',
            'E': '60.000',
        },
        'D',
        "Onaydan önceki satış dönem sonu NGD'sine kanıt sağlar; TMS 2 p. 6'ya göre NGD, tahmini satış fiyatından satış için gerekli maliyetler düşülerek bulunur: 470.000 × %96 = 451.200 ₺; karşılık 500.000 − 451.200 = **48.800 ₺**.",
        'TMS 10 p. 9(b)(ii); TMS 2 p. 6',
    ),
    # düzey 3
    '0052': patch(
        "Bir işletme 31.12.2025'te, aleyhine açılmış bir davayı kaybetme olasılığını düşük görerek karşılık ayırmamış, yalnızca koşullu borç olarak açıklamıştır. Tablolar onaylanmadan önce mahkeme, dava konusu olayın 2025'te gerçekleştiğini ve işletmenin tazminat ödemesi gerektiğini karara bağlamıştır. Bu durumda ne yapılır?",
        {
            'A': 'Bir işlem yapılmaz',
            'B': 'Özkaynaktan düşülür',
            'C': '2026 gideri yazılır',
            'D': 'Koşullu borç açıklaması korunur',
            'E': 'Karşılık tanınır',
        },
        'E',
        "TMS 10 p. 9(a)'ya göre mahkeme kararı işletmenin **raporlama dönemi sonunda mevcut bir yükümlülüğü olduğunu teyit eder**; işletme yalnızca koşullu borç açıklamasıyla yetinmez, TMS 37'ye göre karşılık tanır.",
        'TMS 10 p. 9(a)',
    ),
    # düzey 3
    '0053': patch(
        "Bir işletmenin 31.12.2025 itibarıyla 1.000.000 ₺ vergilendirilebilir geçici farkı vardır; yıl sonunda yasalaşmış kurumlar vergisi oranı %25'tir. Şubat 2026'da, tablolar onaylanmadan önce oran %30'a çıkarılmıştır. 31.12.2025 tablolarında ertelenmiş vergi borcu kaç ₺'dir?",
        {
            'A': '250.000',
            'B': '300.000',
            'C': '550.000',
            'D': '50.000',
            'E': '0',
        },
        'A',
        "TMS 12 p. 47'ye göre ertelenmiş vergi, **raporlama dönemi sonunda yasalaşmış** oranlarla ölçülür; TMS 10 p. 22(h)'ye göre sonraki oran değişikliği düzeltme gerektirmez: 1.000.000 × %25 = **250.000 ₺**; yeni oranın etkisi açıklanır.",
        'TMS 10 p. 22(h); TMS 12 p. 47',
    ),
    # düzey 2
    '0054': patch(
        'Bir işletmede tablolar onaylanmadan önce şu olaylar gerçekleşmiştir: yıl sonu ikramiye tutarının mevcut taahhüde göre kesinleşmesi, yıl sonundan önce alınan bir makinenin maliyetinin belirlenmesi, yıl sonu alacağının borçlunun yıl sonunda başlamış iflas süreci nedeniyle tahsil edilemeyeceğinin anlaşılması, 2025 tablolarında bir hatanın bulunması ve önemli bir şirketin satın alınması. Hangisi düzeltme gerektiren olay değildir?',
        {
            'A': 'Makine maliyetinin belirlenmesi',
            'B': 'Hatanın bulunması',
            'C': 'İkramiye tutarının kesinleşmesi',
            'D': 'Önemli bir şirketin satın alınması',
            'E': 'Alacağın tahsil edilemeyeceğinin anlaşılması',
        },
        'D',
        "TMS 10 p. 9'daki örnekler (ikramiye, maliyet belirlenmesi, iflas, hata) düzeltme gerektiren olaylardır. p. 22(a)'ya göre raporlama döneminden sonraki **önemli işletme birleşmesi** düzeltme gerektirmez.",
        'TMS 10 p. 9, 22',
    ),
    # düzey 3
    '0055': patch(
        "Bir işletmenin genel kurulu Kasım 2025'te ortaklara 200.000 ₺ ara kâr payı dağıtılmasına karar vermiş, bu tutar yıl sonunda henüz ödenmemiştir. Yönetim kurulu ayrıca Şubat 2026'da, tablolar onaylanmadan önce, 2025 kârından 300.000 ₺ kâr payı dağıtılmasını önermiştir. 31.12.2025 tablolarında ödenecek kâr payı borcu kaç ₺'dir?",
        {
            'A': '300.000',
            'B': '500.000',
            'C': '200.000',
            'D': '0',
            'E': '100.000',
        },
        'C',
        "Kasım 2025'teki genel kurul kararıyla dönem sonunda **200.000 ₺ mevcut yükümlülük** vardır ve borç olarak tanınır. TMS 10 p. 12'ye göre dönem sonrasında önerilen 300.000 ₺ kâr payı borç olarak tanınmaz, dipnotta açıklanır.",
        'TMS 10 p. 12-13',
    ),
    # düzey 3
    '0056': patch(
        "Bir işletmenin 31.12.2025 itibarıyla mali durumu güçlü bir müşterisinden 250.000 ₺ alacağı vardır; alacak için genel kredi riski nedeniyle 5.000 ₺ karşılık ayrılmıştır. Müşterinin tek deposu Ocak 2026'da sel felaketinde yok olmuş ve müşteri iflas etmiştir; tablolar onaylanmamıştır. 31.12.2025 tablolarındaki karşılık kaç ₺ olmalıdır?",
        {
            'A': '0',
            'B': '5.000',
            'C': '125.000',
            'D': '245.000',
            'E': '250.000',
        },
        'B',
        'Müşterinin iflasına yol açan olay **raporlama döneminden sonra** gerçekleşmiştir ve dönem sonundaki durumu yansıtmaz; düzeltme gerektirmez. Karşılık **5.000 ₺** olarak kalır, önemli etki açıklanır.',
        'TMS 10 p. 10, 21',
    ),
    # düzey 3
    '0057': patch(
        "Bir işletme 31.12.2025'te 2025 satışlarına ilişkin garanti karşılığını 50.000 ₺ olarak tahmin etmiştir. Tablolar onaylanmadan önce gelen arıza bildirimleri ve teknik incelemeler, 2025'te satılan ürünlerde yıl sonunda var olan bir üretim hatası nedeniyle garanti maliyetinin 70.000 ₺ olacağını göstermiştir. 31.12.2025 tablolarındaki garanti karşılığı kaç ₺ olmalıdır?",
        {
            'A': '20.000',
            'B': '0',
            'C': '70.000',
            'D': '50.000',
            'E': '120.000',
        },
        'C',
        "Bilgi, raporlama dönemi sonunda **var olan bir koşula** (üretim hatası) kanıt sağladığından düzeltme gerektirir; karşılık **70.000 ₺**'ye çıkarılır (ek 20.000 ₺).",
        'TMS 10 p. 9, 10',
    ),
    # düzey 2
    '0058': patch(
        "Bir üretim işletmesinin ana hammadde tedarikçisinde Şubat 2026'da başlayan grev nedeniyle işletmenin üretimi tablolar onaylanmadan önce iki hafta durmuştur; yıl sonunda böyle bir risk öngörülmemişti. Bu olay nasıl sınıflandırılır?",
        {
            'A': 'Düzeltme gerektiren olay',
            'B': 'Koşullu borç',
            'C': 'Düzeltme gerektirmeyen olay',
            'D': 'Tahmin değişikliği',
            'E': 'Önceki dönem hatası düzeltmesi',
        },
        'C',
        "Grev ve üretimin durması **raporlama döneminden sonra ortaya çıkan koşullardır**; TMS 10 p. 10'a göre düzeltme gerektirmez, önemliyse p. 21 uyarınca niteliği ve etkisi açıklanır.",
        'TMS 10 p. 10, 21',
    ),
    # düzey 3
    '0059': patch(
        'Aşağıdakilerden hangileri düzeltme gerektirmeyen olaylardandır?\n\nI. Raporlama döneminden sonra hisse senedi fiyatlarındaki genel düşüş\n\nII. Raporlama döneminden sonra yeniden yapılandırma planının ilan edilmesi\n\nIII. Raporlama döneminden sonra döviz kurlarında olağandışı büyük değişiklik',
        {
            'A': 'I ve II',
            'B': 'I, II ve III',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'Yalnız I',
        },
        'B',
        "TMS 10 p. 11 ve 22(e), (g)'ye göre piyasa değerindeki düşüş (I), yeniden yapılandırmanın ilanı (II) ve kurlardaki olağandışı değişiklik (III) sonradan ortaya çıkan koşullardır ve düzeltme gerektirmez.",
        'TMS 10 p. 11, 22',
    ),
    # düzey 2
    '0060': patch(
        'Önemli düzeltme gerektirmeyen olaylar için aşağıdakilerden hangileri açıklanır?\n\nI. Olayın niteliği\n\nII. Finansal etkisinin tahmini veya tahmin yapılamadığı\n\nIII. Olayın cari dönem tablolarına kaydedilen tutarı',
        {
            'A': 'I ve III',
            'B': 'Yalnız II',
            'C': 'I, II ve III',
            'D': 'Yalnız I',
            'E': 'I ve II',
        },
        'E',
        "TMS 10 p. 21'e göre önemli düzeltme gerektirmeyen olayların **niteliği** (I) ve **finansal etkisinin tahmini veya tahminin yapılamayacağı** (II) açıklanır. Bu olaylar tablolara kaydedilmez (III yanlış).",
        'TMS 10 p. 21-22',
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
    print(f"1 paket / {len(PATCHES)} soru ('TMS 10 Raporlama Doneminden Sonraki Olaylar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
