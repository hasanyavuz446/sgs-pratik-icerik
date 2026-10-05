#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TMS 7 Nakit Akis Tablosu — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

60 soru korunarak onarildi: genisletilmis ELEME_ISARETI olcutune gore 62 mutlak ifadeli celdirici ayni dogruluk degerini koruyacak bicimde yeniden yazildi, sisirilmis celdiriciler sadelestirildi; gerekce tasiyan 11 dogru sik kisaltildi. Kor ogrenci %35 -> %22 (UYARI kapandi).

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: KGK TMS 7 Nakit Akis Tablolari
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/tms_7_nakit_akis.json"
STYLE_REF = 'SGS Muhasebe Standartları (TMS 7; yapısal)'
ONEK = "std-tms7-gen-"


def patch(stem, options, answer, solution, ref='TMS 7 Nakit Akis Tablolari'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "TMS 7'nin temel amacı aşağıdakilerden hangisidir?",
        {
            'A': 'İşletmenin banka hesaplarının nasıl açılacağını düzenleyen bir bankacılık standardı olarak yayımlanmıştır',
            'B': 'İşletmenin gelecekteki nakit ihtiyacını tahmin eden bir bütçeleme yöntemi standardı',
            'C': 'Nakit ve nakit benzerlerindeki değişimler hakkında bilgi verilmesini sağlamaktır',
            'D': 'İşletmenin varlık ve kaynaklarının belirli bir tarihteki durumunu düzenleyen bir bilanço standardıdır',
            'E': 'İşletmenin kâr veya zararının nasıl hesaplanacağını gösteren bir gelir tablosu standardıdır',
        },
        'C',
        'TMS 7: bu Standardın amacı, işletmenin nakit ve nakit benzerlerindeki tarihi değişikliklere ilişkin bilginin, dönem içindeki nakit akışlarını sınıflandıran bir nakit akış tablosu aracılığıyla verilmesini sağlamaktır.',
        'TMS 7 - amaç',
    ),
    # düzey 2
    '0002': patch(
        'Bir yatırımın nakit benzeri sayılabilmesi için hangi amaçla elde tutulması gerekir?',
        {
            'A': 'Nakit benzeri sayılmak için varlığın en az beş yıl vadeli olması şartı aranmaktadır',
            'B': 'Nakit benzerleri uzun vadeli yatırım ve değer artışı amacıyla elde tutulan varlıkları ifade eder',
            'C': 'Nakit benzeri sayılmak için varlığın değerinde önemli dalgalanma olması gerekmektedir',
            'D': 'Her türlü menkul kıymet, vadesine bakılmaksızın nakit benzeri olarak sınıflandırılmaktadır',
            'E': 'Nakit benzerleri yatırım amacıyla değil, kısa vadeli nakit taahhütleri karşılamak için elde tutulur',
        },
        'E',
        'TMS 7: nakit benzerleri, yatırım amacıyla veya diğer amaçlarla değil, kısa vadeli nakit taahhütlerini yerine getirmek amacıyla elde tutulur. Bu nedenle vadesi kısa ve değer değişim riski önemsiz olmalıdır.',
        'TMS 7 - nakit benzeri ölçütü',
    ),
    # düzey 2
    '0003': patch(
        'Kasadaki paranın vadesiz mevduata yatırılması nakit akış tablosunda nasıl gösterilir?',
        {
            'A': 'Bu hareketler işletme faaliyetinden nakit akışı olarak tabloda gösterilir',
            'B': 'Nakit yönetiminin parçası olan bu hareketler nakit akışı sayılmaz; tabloda gösterilmez',
            'C': 'Bu hareketler finansman faaliyeti sayılır ve nakit akış tablosunda ayrı bölümde sunulmaktadır',
            'D': 'Bu hareketler nakit akışı sayılır ve her biri brüt olarak tabloda gösterilir',
            'E': 'Bu hareketler yatırım faaliyeti olarak sınıflandırılıp tabloda ayrıca raporlanır',
        },
        'B',
        'TMS 7: nakit ve nakit benzerleri kalemleri arasındaki hareketler (nakdin vadesiz mevduata yatırılması gibi), işletmenin nakit yönetiminin bir parçası olduğundan nakit akışı sayılmaz ve tabloda gösterilmez.',
        'TMS 7 - nakit içi hareketler',
    ),
    # düzey 3
    '0004': patch(
        "Aşağıdakilerden hangisi TMS 7'ye göre yatırım faaliyetlerinden kaynaklanan nakit akışı DEĞİLDİR?",
        {
            'A': 'Üretimde kullanılacak makinenin peşin bedeli',
            'B': 'Uzun vadeli yatırımın satışından sağlanan nakit',
            'C': 'Finansal kuruluş olmayan işletmenin üçüncü kişiye verdiği nakit avans',
            'D': 'Satılmak üzere alınan stoklar için tedarikçiye yapılan ödeme',
            'E': 'Patent edinimi için yapılan nakit ödeme',
        },
        'D',
        'TMS 7 par. 14-16 uyarınca stok tedarikçisine yapılan ödeme esas faaliyet nakit akışıdır. Makine ve patent edinimi, uzun vadeli yatırım satışı ile finansal kuruluş olmayan bir işletmenin üçüncü kişilere verdiği avanslar yatırım faaliyeti kapsamında değerlendirilir.',
        'TMS 7 Nakit Akis Tablosu',
    ),
    # düzey 2
    '0005': patch(
        'Mal ve hizmet satışından doğan nakit tahsilatları hangi faaliyet grubunda yer alır?',
        {
            'A': 'Yatırım faaliyetlerinden nakit girişi olarak sınıflandırılır',
            'B': 'İşletme faaliyetlerinden nakit çıkışı olarak gösterilir; satış nakit azalışı doğurmaktadır',
            'C': 'Nakit akış tablosunda değil, gelir tablosunda yer alır',
            'D': 'İşletme faaliyetlerinden nakit girişi olarak sınıflandırılır',
            'E': 'Finansman faaliyetlerinden nakit girişi olarak raporlanan bir hareketi ifade eder',
        },
        'D',
        'TMS 7: mal satışı ve hizmet sunumundan elde edilen nakit girişleri, işletmenin esas gelir getirici faaliyetlerinden kaynaklandığından işletme faaliyeti olarak sınıflandırılır.',
        'TMS 7 - işletme faaliyeti',
    ),
    # düzey 2
    '0006': patch(
        'Kullanılmış bir maddi duran varlığın satışından sağlanan nakit nasıl sınıflandırılır?',
        {
            'A': 'Nakit akış tablosunda değil, gelir tablosunda satış kârı olarak izlenir',
            'B': 'Satış kârı işletme faaliyeti, satış bedeli ise finansman faaliyeti olarak ayrı sınıflandırılır',
            'C': 'İşletme faaliyetlerinden nakit girişi olarak sınıflandırılır',
            'D': 'Finansman faaliyetlerinden nakit girişi olarak raporlanan bir hareketi ifade eder',
            'E': 'Yatırım faaliyetlerinden nakit girişi olarak sınıflandırılır',
        },
        'E',
        'TMS 7: maddi ve maddi olmayan duran varlıkların ve diğer uzun vadeli varlıkların satışından sağlanan nakit girişleri yatırım faaliyetidir.',
        'TMS 7 - yatırım faaliyeti',
    ),
    # düzey 2
    '0007': patch(
        'Faiz ve kâr payı nakit akışlarının sınıflandırılmasında hangi ilke uygulanır?',
        {
            'A': 'Her dönem tutarlı biçimde sınıflandırılmak koşuluyla işletme, yatırım veya finansman faaliyeti olarak sunulabilir',
            'B': 'Faiz ve kâr payı her işletmede işletme faaliyeti olarak sınıflandırılır',
            'C': 'Faiz ve kâr payı akışları nakit akış tablosunda gösterilmez; dipnotta açıklanır',
            'D': 'Faiz ve kâr payı akışları işletme faaliyeti olarak sınıflandırılır; yatırım veya finansman faaliyeti olarak gösterilmelerine izin verilmez',
            'E': 'Faiz ve kâr payı her dönem farklı bölümde sınıflandırılır; tutarlılık aranmaz',
        },
        'A',
        'TMS 7: faiz ve kâr payı tahsilat ve ödemelerinden kaynaklanan nakit akışları ayrı ayrı açıklanır ve her dönem tutarlı biçimde işletme, yatırım veya finansman faaliyeti olarak sınıflandırılır.',
        'TMS 7 - faiz ve kâr payı',
    ),
    # düzey 2
    '0008': patch(
        'Borcu pay vererek özkaynağa dönüştüren işletme bu işlemi nasıl raporlar?',
        {
            'A': 'İşlem yatırım faaliyeti olarak sınıflandırılır ve nakit çıkışı biçiminde gösterilmektedir',
            'B': 'Nakit kullanımı gerektirmeyen bu işlem tabloya dâhil edilmez; dipnotlarda açıklanır',
            'C': 'İşlem finansman faaliyetinden nakit girişi ve çıkışı olarak brüt biçimde gösterilir',
            'D': 'İşlem ne tabloda ne dipnotta raporlanır',
            'E': 'İşlem işletme faaliyetinden nakit akışı olarak raporlanır ve dönem nakdini artırmaktadır',
        },
        'B',
        'TMS 7: borcun özkaynağa dönüştürülmesi nakit veya nakit benzeri kullanımını gerektirmeyen bir finansman işlemidir; nakit akış tablosuna dâhil edilmez, dipnotlarda açıklanır.',
        'TMS 7 - nakit içermeyen işlem (senaryo)',
    ),
    # düzey 3
    '0009': patch(
        "Aşağıdakilerden hangileri TMS 7'ye göre yatırım faaliyeti sayılır?\n\nI. Kredi anaparasının ödenmesi\n\nII. Maddi duran varlık satın alınması\n\nIII. Maddi duran varlık satılması",
        {
            'A': 'II ve III',
            'B': 'Yalnız III',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'A',
        'Uzun vadeli varlıkların edinimi (II) ve elden çıkarılması (III) yatırım faaliyetidir. Kredi anaparasının ödenmesi (I) ise borçlanma yapısını değiştirdiğinden finansman faaliyetidir; bu nedenle yanlıştır.',
        'TMS 7 - faaliyet sınıflandırması',
    ),
    # düzey 3
    '0010': patch(
        'Aşağıdaki ifadelerden hangileri TMS 7 bakımından doğrudur?\n\nI. Faiz ve kâr payı akışları tutarlı biçimde sınıflandırılır\n\nII. Gelir vergisi kural olarak işletme faaliyetidir\n\nIII. Nakit içermeyen işlemler tabloda gösterilir',
        {
            'A': 'Yalnız I',
            'B': 'Yalnız III',
            'C': 'I, II ve III',
            'D': 'II ve III',
            'E': 'I ve II',
        },
        'E',
        'Faiz/kâr payı tutarlı sınıflandırılır (I) ve gelir vergisi kural olarak işletme faaliyetidir (II). Nakit içermeyen işlemler ise tabloya dâhil edilmez, dipnotta açıklanır; bu nedenle III yanlıştır.',
        'TMS 7 - sınıflandırma',
    ),
    # düzey 2
    '0011': patch(
        'Dolaylı yöntemde amortisman gideri dönem kârına nasıl yansıtılır?',
        {
            'A': 'Nakit çıkışı gerektirmediğinden dönem kârına eklenir',
            'B': 'Amortisman gideri dolaylı yöntemde düzeltmeye konu edilmez',
            'C': 'Amortisman gideri yatırım faaliyetinden nakit çıkışı olarak ayrıca raporlanır',
            'D': 'Nakit çıkışı gerektirdiğinden dönem kârından ayrıca düşülür',
            'E': 'Amortisman gideri finansman faaliyetinden nakit çıkışı olarak sınıflandırılan bir kalemdir',
        },
        'A',
        'TMS 7: dolaylı yöntemde amortisman gibi gayrinakdi giderler, kâr/zararı azaltmış ancak nakit çıkışı doğurmamış olduğundan dönem kârına geri eklenir.',
        'TMS 7 - dolaylı yöntem düzeltmesi',
    ),
    # düzey 2
    '0012': patch(
        'Maddi duran varlık satış kârı dolaylı yöntemde dönem kârına nasıl uygulanır?',
        {
            'A': 'Yatırım faaliyetiyle ilgili olduğundan işletme faaliyeti bölümünde dönem kârından düşülür',
            'B': 'İşletme faaliyeti bölümünde dönem kârına eklenir',
            'C': 'Satış kârı dolaylı yöntemde düzeltmeye konu edilmez',
            'D': 'Satış kârı finansman faaliyetinden nakit girişi olarak ayrıca raporlanır',
            'E': 'Satış kârı tabloda gösterilmez, dipnotlarda açıklanır',
        },
        'A',
        'TMS 7: duran varlık satış kârı yatırım faaliyetiyle ilgili bir gelir kalemidir; kâr içinde yer aldığından işletme faaliyeti bölümünde düşülür, satıştan sağlanan nakdin tamamı yatırım bölümünde gösterilir.',
        'TMS 7 - yatırım kalemi düzeltmesi',
    ),
    # düzey 3
    '0013': patch(
        "Dönem net kârı 180.000 ₺ olup içinde 20.000 ₺ maddi duran varlık satış kârı bulunmaktadır. Amortisman gideri 35.000 ₺'dir. Başka düzeltme yoksa işletme faaliyetlerinden nakit akışı kaç ₺'dir?",
        {
            'A': '225.000 ₺',
            'B': '235.000 ₺',
            'C': '195.000 ₺',
            'D': '265.000 ₺',
            'E': '180.000 ₺',
        },
        'C',
        'Duran varlık satış kârı yatırım faaliyetiyle ilgili olduğundan işletme bölümünde düşülür; amortisman gayrinakdi olduğundan eklenir: 180.000 − 20.000 + 35.000 = 195.000 ₺.',
        'TMS 7 - yatırım kalemi düzeltmesi',
    ),
    # düzey 2
    '0014': patch(
        'Yatırım ve finansman faaliyetlerindeki nakit giriş ve çıkışları için genel sunum kuralı hangisidir?',
        {
            'A': 'Kural olarak brüt raporlanır; standartta sayılan hâllerde net gösterilebilir',
            'B': 'Tüm nakit akışları net tutar üzerinden gösterilir; brüt gösterim yasaktır',
            'C': 'Nakit akışları dönem sonunda tek bir net toplam olarak raporlanır',
            'D': 'Nakit akışları kural olarak netleştirilerek tek bir tutar hâlinde raporlanır; brüt gösterim istisnadır',
            'E': 'Brüt gösterim işletme faaliyetlerine özgü olup diğer bölümlerde uygulanmaz',
        },
        'A',
        'TMS 7: yatırım ve finansman faaliyetlerinden kaynaklanan brüt nakit girişleri ve brüt nakit çıkışları ana gruplar itibarıyla ayrı ayrı raporlanır. Ancak müşteri adına yapılan tahsilat/ödemeler ile devir hızı yüksek, tutarı büyük ve vadesi kısa kalemler net olarak raporlanabilir.',
        'TMS 7 - brüt gösterim',
    ),
    # düzey 3
    '0015': patch(
        'Aşağıdakilerden hangileri işletme faaliyetlerinden nakit akışının sunumunda kullanılabilir?\n\nI. Doğrudan yöntem\n\nII. Dolaylı yöntem\n\nIII. Yalnızca dönem sonu bakiye gösterimi',
        {
            'A': 'I, II ve III',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'Yalnız III',
            'E': 'Yalnız I',
        },
        'B',
        'TMS 7 işletme faaliyetlerinde doğrudan (I) ve dolaylı (II) yöntemlere izin verir; doğrudan yöntem teşvik edilir. Yalnızca bakiye gösterimi (III) bir sunum yöntemi değildir.',
        'TMS 7 - yöntemler',
    ),
    # düzey 2
    '0016': patch(
        'Nakit akış tablosunda nakit mevcudunun uzlaştırılması bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Uzlaştırma vergi idaresi talep ettiğinde yapılır',
            'B': 'Uzlaştırma doğrudan yöntemde aranır, dolaylı yöntemde aranmaz',
            'C': 'Nakit akış tablosundaki tutarlar ile finansal durum tablosundaki nakit kalemlerinin uzlaştırılması gerekmez',
            'D': 'Nakit akış tablosundaki tutarlar ile finansal durum tablosundaki nakit kalemleri uzlaştırılarak açıklanır',
            'E': 'Nakit akış tablosu ile bilanço arasında uzlaştırma yapılmaz',
        },
        'D',
        'TMS 7: işletme, nakit akış tablosundaki nakit ve nakit benzerleri tutarları ile finansal durum tablosunda raporlanan ilgili kalemleri uzlaştırarak açıklar.',
        'TMS 7 - uzlaştırma',
    ),
    # düzey 3
    '0017': patch(
        'Grup tarafından kullanılamayan önemli nakit bakiyelerine ilişkin aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'Kullanımı engelleyen koşullar hakkında bilgi verilir',
            'B': 'Açıklama, kullanıcıların işletmenin likiditesini değerlendirmesine yardımcı olur',
            'C': 'Tutar finansal tablolarda açıklanır',
            'D': 'Nakit tanımını karşıladığı için kullanım kısıtı açıklanmaz',
            'E': 'Kambiyo kontrolü veya yasal kısıtlama kullanım engeline örnek olabilir',
        },
        'D',
        'TMS 7 par. 48-49, grup tarafından kullanılamayan önemli nakit ve nakit benzeri bakiyelerinin tutarı ile yönetimin açıklamasının sunulmasını ister. Kambiyo kontrolleri ve yasal kısıtlamalar bu duruma örnek olabilir.',
        'TMS 7 Nakit Akis Tablosu',
    ),
    # düzey 2
    '0018': patch(
        'İşletme faaliyetlerinden nakit akışının önemi bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşletme faaliyetlerinden nakit akışı vergi matrahını hesaplamak için kullanılır',
            'B': 'İşletme faaliyetlerinden nakit akışı, dönem kârıyla birebir aynı tutarı gösterir',
            'C': 'İşletmenin dış finansmana başvurmadan borç ödeme, kapasite koruma ve kâr payı dağıtma kabiliyetini gösteren temel bir göstergedir',
            'D': 'İşletme faaliyetlerinden nakit akışının analitik değeri yoktur, biçimseldir',
            'E': 'İşletme faaliyetlerinden nakit akışı, işletmenin performansını yansıtan tek göstergedir; yatırım ve finansman akışları bu değerlendirmede dikkate alınmaz',
        },
        'C',
        'TMS 7: işletme faaliyetlerinden kaynaklanan nakit akışlarının tutarı, işletmenin dış finansman kaynaklarına başvurmadan borçlarını ödeyip ödeyemeyeceğinin, faaliyet kapasitesini koruyup koruyamayacağının ve kâr payı dağıtıp dağıtamayacağının temel göstergesidir.',
        'TMS 7 - işletme nakit akışının önemi',
    ),
    # düzey 3
    '0019': patch(
        'Bir işletme faiz ödemelerini geçen yıl finansman faaliyeti olarak sınıflandırmış, bu yıl işletme faaliyetine almak istemektedir. TMS 7 bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Faiz akışları dönemler arasında tutarlı biçimde sınıflandırılmalıdır',
            'B': 'Faiz ödemeleri bundan sonra finansman faaliyetinde kalmalıdır',
            'C': 'Faiz ödemeleri tabloda gösterilmez, gelir tablosunda yer alır',
            'D': 'Faiz ödemeleri her yıl farklı bölümde gösterilir; tutarlılık aranmamaktadır',
            'E': 'İşletme faiz sınıflandırmasını her dönem gerekçesiz değiştirebilir',
        },
        'A',
        'TMS 7: faiz ve kâr payı akışlarının her biri ayrı açıklanır ve dönemler itibarıyla tutarlı biçimde işletme, yatırım veya finansman faaliyeti olarak sınıflandırılır. Tutarlılık esastır.',
        'TMS 7 - faiz tutarlılığı (senaryo)',
    ),
    # düzey 3
    '0020': patch(
        "Dönem satışların maliyeti 600.000 ₺, stoklarda artış 50.000 ₺ ve ticari borçlarda azalış 30.000 ₺'dir. Doğrudan yönteme göre satıcılara yapılan ödeme kaç ₺'dir?",
        {
            'A': '680.000 ₺',
            'B': '600.000 ₺',
            'C': '520.000 ₺',
            'D': '620.000 ₺',
            'E': '80.000 ₺',
        },
        'A',
        'Satıcılara ödeme = SMM + Stok artışı + Borç azalışı = 600.000 + 50.000 + 30.000 = 680.000 ₺. Stok artışı ek alımı, borç azalışı ise geçmiş borcun ödendiğini gösterir.',
        'TMS 7 - doğrudan yöntem',
    ),
    # düzey 2
    '0021': patch(
        'Nakit akış tablosu kullanıcılara öncelikle hangi değerlendirmeyi yapma imkânı verir?',
        {
            'A': 'İşletmenin piyasa değerini kesin ve tartışmasız biçimde ortaya koyan bir gösterge sunmaktadır',
            'B': 'İşletmenin gelecekteki kârını öngören bir tahmin aracı olarak bilgi verir',
            'C': 'Ortaklara dağıtılacak kâr payının tutarını gösteren bir hesaplama tablosudur',
            'D': 'İşletmenin vergi borcunu hesaplamaya yarayan bir bilgi kaynağıdır',
            'E': 'İşletmenin nakit yaratma kabiliyetini ve nakit ihtiyacını değerlendirmeye imkân verir',
        },
        'E',
        'TMS 7: nakit akış bilgisi, kullanıcıların işletmenin nakit ve nakit benzeri yaratma kabiliyetini ve bu nakit akışlarını kullanma ihtiyacını değerlendirmesine imkân verir.',
        'TMS 7 - faydası',
    ),
    # düzey 2
    '0022': patch(
        'Özkaynağa dayalı bir finansal araç hangi durumda nakit benzeri kabul edilebilir?',
        {
            'A': 'Özkaynağa dayalı araçlar hiçbir istisna olmaksızın ve kesin biçimde nakit benzeri sayılamamaktadır',
            'B': 'Özkaynağa dayalı araçlar borsada işlem görüyorsa nakit benzeri sayılır',
            'C': 'Özkaynağa dayalı finansal araçlar nakit benzeri sayılır ve edinim tarihindeki vadesine bakılmaksızın nakit ve nakit benzerleri kapsamına dâhil edilir',
            'D': 'Özkaynağa dayalı araçlar kural olarak nakit benzeri sayılmaz; ancak vadesine yakın alınan imtiyazlı paylar gibi istisnalar olabilir',
            'E': 'Tüm özkaynağa dayalı finansal araçlar nakit benzeri olarak sınıflandırılır',
        },
        'D',
        'TMS 7: özkaynağa dayalı finansal araçlara yapılan yatırımlar, esas itibarıyla nakit benzeri değildir. Ancak vadesine kısa süre kalmış ve itfa tarihi belirli imtiyazlı paylar gibi durumlar istisna oluşturabilir.',
        'TMS 7 - özkaynak araçları',
    ),
    # düzey 2
    '0023': patch(
        'Nakit akışları hangi üç faaliyet grubunda raporlanır?',
        {
            'A': 'Nakit akışları kısa ve uzun vadeli olmak üzere vade esasına göre iki bölümde raporlanmaktadır',
            'B': 'Nakit akışları tahsilat ve ödeme olarak iki bölümde raporlanır',
            'C': 'Nakit akışları dönen ve duran varlıklar biçiminde ikiye ayrılarak bilanço düzeninde sunulur',
            'D': 'Bölüm ayrımı yapılmaz; tüm hareketler tek toplam hâlinde gösterilir',
            'E': 'Nakit akışları işletme, yatırım ve finansman faaliyetleri olmak üzere üç bölümde raporlanır',
        },
        'E',
        'TMS 7: nakit akış tablosu, dönem içindeki nakit akışlarını işletme, yatırım ve finansman faaliyetleri bazında sınıflandırarak raporlar.',
        'TMS 7 - bölümler',
    ),
    # düzey 2
    '0024': patch(
        'Özkaynak ve borçlanma yapısını değiştiren nakit akışları hangi faaliyet grubunda raporlanır?',
        {
            'A': 'İşletmenin uzun vadeli varlık edinim ve satışlarını kapsayan bir faaliyet grubunu ifade eder',
            'B': 'Stok alımını ve satıcılara yapılan ödemeleri kapsayan faaliyetlerdir',
            'C': 'İşletmenin esas gelir getirici faaliyetlerini ve olağan ticari işlemlerini kapsayan bölümdür',
            'D': 'Finansman faaliyetleri, işletmenin esas gelir getirici mal ve hizmet satışlarından doğan nakit akışlarıdır',
            'E': 'İşletmenin özkaynağının ve borçlanmalarının büyüklüğünde ve bileşiminde değişiklik doğuran faaliyetlerdir',
        },
        'E',
        'TMS 7: finansman faaliyetleri, işletmenin özkaynağının ve borçlanmalarının büyüklüğünde ve bileşiminde değişiklik meydana getiren faaliyetlerdir. Sermayeyi sağlayanların gelecekteki nakit akışı taleplerinin öngörülmesine yardımcı olur.',
        'TMS 7 - finansman faaliyetleri',
    ),
    # düzey 2
    '0025': patch(
        'Üretimde kullanılacak bir makine için yapılan nakit ödeme hangi faaliyet grubundadır?',
        {
            'A': 'Yatırım faaliyetlerinden nakit çıkışı olarak sınıflandırılır',
            'B': 'Nakit akış tablosunda değil, bilançoda varlık artışı olarak izlenir',
            'C': 'Yatırım faaliyetlerinden nakit girişi olarak gösterilir; varlık edinimi giriş doğurmaktadır',
            'D': 'Finansman faaliyetlerinden nakit çıkışı olarak raporlanan bir hareket',
            'E': 'İşletme faaliyetlerinden nakit çıkışı olarak sınıflandırılır',
        },
        'A',
        'TMS 7: maddi ve maddi olmayan duran varlıklar ile diğer uzun vadeli varlıkların edinimi için yapılan nakit ödemeler yatırım faaliyetlerinden nakit çıkışıdır.',
        'TMS 7 - yatırım faaliyeti',
    ),
    # düzey 2
    '0026': patch(
        'Kredi alınması ve kredi anaparasının geri ödenmesi nakit akış tablosunda nasıl gösterilir?',
        {
            'A': 'Kredi alınması finansman, anapara ödemesi ise işletme faaliyeti olarak ayrı sınıflandırılır',
            'B': 'Kredi hareketleri tabloda gösterilmez, dipnotta açıklanır',
            'C': 'İkisi de finansman faaliyeti olarak sınıflandırılır',
            'D': 'İkisi de işletme faaliyeti olarak sınıflandırılır; borçlanma olağan faaliyet sayılır',
            'E': 'İkisi de yatırım faaliyeti olarak sınıflandırılır; kredi bir yatırım hareketi kabul edilir',
        },
        'C',
        'TMS 7: borçlanma araçlarının ihracı ve kredi alınmasından sağlanan nakit girişleri ile borç anaparasının geri ödenmesine ilişkin nakit çıkışları finansman faaliyetidir; ikisi de borçlanma yapısını değiştirir.',
        'TMS 7 - finansman faaliyeti',
    ),
    # düzey 2
    '0027': patch(
        "Ortaklara ödenen kâr payları TMS 7'ye göre nasıl sınıflandırılabilir?",
        {
            'A': 'Ortaklara ödenen kâr payı nakit akış tablosunda gösterilmemektedir',
            'B': 'Finansman faaliyeti olarak sınıflandırılabilir; işletme faaliyeti olarak sunulması da mümkündür',
            'C': 'Ortaklara ödenen kâr payı gelir tablosunda gider olarak raporlanır',
            'D': 'Ortaklara ödenen kâr payı yatırım faaliyeti olarak sınıflandırılır',
            'E': 'Ortaklara ödenen kâr payının sınıflandırılması her dönem değiştirilir',
        },
        'B',
        'TMS 7: ödenen kâr payları finansman faaliyeti olarak sınıflandırılabilir; çünkü finansman kaynağı elde etme maliyetidir. Kullanıcıların işletme faaliyetlerinden kâr payı ödeme kabiliyetini değerlendirmesine yardımcı olmak için işletme faaliyeti olarak da sınıflandırılabilir.',
        'TMS 7 - ödenen kâr payı',
    ),
    # düzey 3
    '0028': patch(
        'Aşağıdakilerden hangisi nakit akışı yaratmayan yatırım veya finansman işlemi DEĞİLDİR?',
        {
            'A': 'Finansal borcun özkaynağa dönüştürülmesi',
            'B': 'Bir varlığın kiralama yoluyla edinilmesi',
            'C': 'Üretim makinesinin bedelinin banka hesabından ödenmesi',
            'D': 'Başka bir işletmenin pay ihracı karşılığında edinilmesi',
            'E': 'Makinenin işletmenin çıkardığı paylar karşılığında edinilmesi',
        },
        'C',
        'TMS 7 par. 43-44: pay ihracıyla varlık edinimi, borcun özkaynağa dönüşmesi, kiralama yoluyla edinim ve pay ihracıyla işletme edinimi nakit kullanmaz; nakit akış tablosu dışında açıklanır. Makine bedelinin banka hesabından ödenmesi ise yatırım faaliyetinden nakit çıkışıdır.',
        'TMS 7 Nakit Akis Tablosu',
    ),
    # düzey 3
    '0029': patch(
        "Aşağıdakilerden hangileri TMS 7'ye göre finansman faaliyeti sayılır?\n\nI. Pay ihracından sağlanan nakit\n\nII. Kredi alınmasından sağlanan nakit\n\nIII. Kredi anaparasının geri ödenmesi",
        {
            'A': 'I, II ve III',
            'B': 'Yalnız III',
            'C': 'II ve III',
            'D': 'Yalnız I',
            'E': 'I ve II',
        },
        'A',
        'Pay ihracı (I), kredi alınması (II) ve kredi anaparasının ödenmesi (III) işletmenin özkaynak ve borçlanma yapısını değiştirdiğinden finansman faaliyetidir. Üçü de doğrudur.',
        'TMS 7 - finansman faaliyeti',
    ),
    # düzey 2
    '0030': patch(
        'Esas faaliyetlerden kaynaklanan nakit akışları hangi yöntemlerle sunulabilir?',
        {
            'A': 'İki yöntem de aynı anda ve birlikte kullanılır; tek yöntem yeterli görülmemektedir',
            'B': 'Doğrudan yöntem kullanılır; dolaylı yöntem yasaklanmıştır',
            'C': "Dolaylı yöntem kullanılır; doğrudan yöntem TMS 7'de kabul edilmez",
            'D': 'Doğrudan veya dolaylı yöntem kullanılabilir; doğrudan yöntem teşvik edilir',
            'E': 'Büyük işletmeler dolaylı, küçük işletmeler doğrudan yöntemi kullanır',
        },
        'D',
        'TMS 7: işletme, işletme faaliyetlerinden nakit akışlarını doğrudan yöntem (brüt nakit giriş ve çıkış sınıflarının belirtildiği) veya dolaylı yöntem (kâr/zararın düzeltildiği) kullanarak raporlar. Standart doğrudan yöntemin kullanılmasını teşvik eder.',
        'TMS 7 - yöntemler',
    ),
    # düzey 2
    '0031': patch(
        'Ticari alacaklardaki artış dolaylı yöntem hesabını nasıl etkiler?',
        {
            'A': 'Nakit girişi doğurduğundan dönem kârına eklenir',
            'B': 'Nakde dönüşmemiş hasılatı gösterdiğinden dönem kârından düşülür',
            'C': 'Ticari alacaklardaki artış finansman faaliyeti olarak sınıflandırılan bir hareketi ifade eder',
            'D': 'Ticari alacaklardaki artış yatırım faaliyetinden nakit girişi olarak raporlanmaktadır',
            'E': 'Ticari alacaklardaki değişim düzeltmeye konu edilmez',
        },
        'B',
        'Dolaylı yöntemde ticari alacaklardaki artış, hasılatın tahsil edilmemiş kısmını gösterir; kârda yer aldığı hâlde nakde dönüşmediğinden dönem kârından düşülür.',
        'TMS 7 - işletme sermayesi düzeltmesi',
    ),
    # düzey 3
    '0032': patch(
        "Dönem net kârı 200.000 ₺, amortisman gideri 60.000 ₺ ve ticari alacaklardaki artış 40.000 ₺'dir. Başka düzeltme yoksa dolaylı yönteme göre işletme faaliyetlerinden nakit akışı kaç ₺'dir?",
        {
            'A': '300.000 ₺',
            'B': '180.000 ₺',
            'C': '220.000 ₺',
            'D': '100.000 ₺',
            'E': '200.000 ₺',
        },
        'C',
        'Amortisman nakit çıkışı gerektirmediğinden eklenir; alacak artışı nakde dönüşmemiş hasılatı gösterdiğinden düşülür: 200.000 + 60.000 − 40.000 = 220.000 ₺.',
        'TMS 7 - dolaylı yöntem',
    ),
    # düzey 3
    '0033': patch(
        "İşletme faaliyetlerinden nakit akışı 320.000 ₺, yatırım faaliyetlerinden 180.000 ₺ çıkış, finansman faaliyetlerinden 60.000 ₺ çıkış olmuştur. Dönem başı nakit 90.000 ₺ ise dönem sonu nakit kaç ₺'dir?",
        {
            'A': '-470.000 ₺',
            'B': '170.000 ₺',
            'C': '260.000 ₺',
            'D': '650.000 ₺',
            'E': '410.000 ₺',
        },
        'B',
        'Dönem sonu nakit = Dönem başı + İşletme + Yatırım + Finansman = 90.000 + 320.000 − 180.000 − 60.000 = 170.000 ₺.',
        'TMS 7 - net nakit değişimi',
    ),
    # düzey 3
    '0034': patch(
        'Aşağıdaki ifadelerden hangileri dolaylı yöntem düzeltmeleri bakımından doğrudur?\n\nI. Ticari borçlardaki artış dönem kârından düşülür\n\nII. Amortisman dönem kârına eklenir\n\nIII. Ticari alacaklardaki artış dönem kârından düşülür',
        {
            'A': 'Yalnız III',
            'B': 'II ve III',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'B',
        'Amortisman eklenir (II) ve alacaklardaki artış düşülür (III). Ancak ticari borçlardaki artış, ödenmemiş gideri gösterdiğinden kâra EKLENİR; bu nedenle I yanlıştır.',
        'TMS 7 - dolaylı yöntem düzeltmeleri',
    ),
    # düzey 3
    '0035': patch(
        'Aşağıdaki ifadelerden hangileri TMS 7 bakımından doğrudur?\n\nI. Nakit benzerleri uzun vadeli yatırım amacıyla elde tutulur\n\nII. Doğrudan yöntemin kullanılması teşvik edilir\n\nIII. Kur farkı nakit akışı değildir ama uzlaştırma için sunulur',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'Yalnız III',
            'D': 'I, II ve III',
            'E': 'II ve III',
        },
        'E',
        'Doğrudan yöntem teşvik edilir (II) ve kur farkı nakit akışı olmasa da uzlaştırma için sunulur (III). Nakit benzerleri ise yatırım amacıyla değil, kısa vadeli nakit taahhütleri karşılamak için tutulur; bu nedenle I yanlıştır.',
        'TMS 7 - genel',
    ),
    # düzey 2
    '0036': patch(
        'Bağlı ortaklık ediniminde ödenen bedel bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ödenen bedel gösterilmez; edinilen varlıkların toplamı raporlanır',
            'B': 'Ödenen bedelin tamamı brüt olarak gösterilir; edinilen nakit düşülmemektedir',
            'C': 'Ödenen bedel finansman faaliyeti olarak sınıflandırılıp özkaynak bölümünde gösterilmektedir',
            'D': 'Ödenen bedelden edinilen nakit ve nakit benzerleri düşülerek net tutar gösterilir',
            'E': 'Ödenen bedel işletme faaliyetinden nakit çıkışı olarak raporlanır',
        },
        'D',
        'TMS 7: bağlı ortaklık veya diğer işletmelerin ediniminden kaynaklanan nakit akışları, edinilen nakit ve nakit benzerleri düşülerek net olarak sunulur.',
        'TMS 7 - edinimde net gösterim',
    ),
    # düzey 2
    '0037': patch(
        'Nakit akış tablosunun diğer tablolarla ilişkisi bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Nakit akış tablosu vergi beyannamesine ek olarak düzenlenir',
            'B': 'Nakit akış tablosu gelir tablosunun bir ekidir, bağımsız tablo değildir',
            'C': 'Diğer tablolarla birlikte likiditeyi ve net varlık değişimini değerlendirmeye yarar',
            'D': 'Nakit akış tablosu bilançonun yerine geçer; bilanço ayrıca düzenlenmesine gerek bırakmaz',
            'E': 'Nakit akış tablosu diğer tablolardan bağımsızdır; aralarında bağ kurulmaz',
        },
        'C',
        'TMS 7: nakit akış tablosu, diğer finansal tablolarla birlikte kullanıldığında net varlıklardaki değişimi, finansal yapıyı (likidite ve borç ödeme gücü dâhil) ve nakit akışlarının tutar ve zamanlamasını etkileme kabiliyetini değerlendirmeye imkân verir.',
        'TMS 7 - diğer tablolarla ilişki',
    ),
    # düzey 2
    '0038': patch(
        'Bir işletmenin vadesiz mevduatındaki parayı kasaya çekmesi bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşletme faaliyetlerinden nakit girişi olarak raporlanır ve dönem nakdini artırmaktadır',
            'B': 'Finansman faaliyeti olarak sınıflandırılır; nakit yapısını değiştiren bir hareket sayılır',
            'C': 'Yatırım faaliyetlerinden nakit çıkışı olarak sınıflandırılıp tabloda gösterilir',
            'D': 'Nakit ve nakit benzerleri arasındaki hareket olduğundan nakit akışı sayılmaz ve tabloda gösterilmez',
            'E': 'İşlem brüt olarak hem giriş hem çıkış biçiminde tabloda iki kez gösterilir',
        },
        'D',
        'TMS 7: nakit ve nakit benzerleri kalemleri arasındaki hareketler işletmenin nakit yönetiminin parçası olduğundan nakit akışı sayılmaz; nakit akış tablosunda gösterilmez.',
        'TMS 7 - nakit içi hareket (senaryo)',
    ),
    # düzey 3
    '0039': patch(
        "Aşağıdakilerden hangileri TMS 7'ye göre dipnotlarda açıklanır?\n\nI. Nakit içermeyen yatırım ve finansman işlemleri\n\nII. Nakit akış tablosu ile bilanço nakit kalemlerinin uzlaştırılması\n\nIII. Grup tarafından kullanılamayan önemli nakit tutarları",
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'Yalnız III',
        },
        'A',
        'TMS 7: nakit içermeyen işlemler (I), nakit ve nakit benzerlerinin uzlaştırılması (II) ve kullanılamayan önemli nakit tutarları (III) dipnotlarda açıklanır. Üçü de doğrudur.',
        'TMS 7 - açıklamalar',
    ),
    # düzey 3
    '0040': patch(
        "İşletme faaliyetlerinden 250.000 ₺ giriş, yatırımdan 400.000 ₺ çıkış, finansmandan 300.000 ₺ giriş olmuştur. Dönem başı nakit 60.000 ₺ ve yabancı para nakit üzerindeki kur etkisi 15.000 ₺ artıştır. Dönem sonu nakit kaç ₺'dir?",
        {
            'A': '210.000 ₺',
            'B': '225.000 ₺',
            'C': '150.000 ₺',
            'D': '195.000 ₺',
            'E': '75.000 ₺',
        },
        'B',
        'Kur etkisi nakit akışı değildir; ancak dönem başı ve sonu nakdi uzlaştırmak için ayrı sunulur: 60.000 + 250.000 − 400.000 + 300.000 + 15.000 = 225.000 ₺.',
        'TMS 7 - kur etkisiyle uzlaştırma',
    ),
    # düzey 2
    '0041': patch(
        "Aşağıdaki nakit ve nakit benzeri tanımlarından hangisi TMS 7'ye uygundur?",
        {
            'A': 'Nakit kasa ve vadesiz mevduattır; nakit benzeri değer riski önemsiz kısa vadeli yatırımdır',
            'B': 'Nakit kasadaki fiziki paradır; banka mevduatı nakit sayılmaz',
            'C': 'Nakit benzeri, vadesi bir yılı aşmayan her türlü menkul kıymettir',
            'D': 'Nakit benzeri, işletmenin uzun vadeli yatırım amacıyla elde tuttuğu hisse senetlerini kapsar',
            'E': 'Nakit benzeri, işletmenin sahip olduğu tüm menkul kıymetleri kapsayan geniş bir kavram',
        },
        'A',
        'TMS 7: nakit, işletmedeki nakit ile vadesiz mevduatı ifade eder. Nakit benzerleri, tutarı belirli bir nakde kolayca çevrilebilen, değer değişim riski önemsiz olan kısa vadeli ve yüksek likiditeye sahip yatırımlardır.',
        'TMS 7 - nakit ve nakit benzeri',
    ),
    # düzey 2
    '0042': patch(
        'Vadesiz hesaba bağlı ve bakiyesi sık sık artı-eksi arasında değişen borçlu cari hesap nasıl sınıflandırılabilir?',
        {
            'A': 'Tüm banka kredileri nakit benzeri olarak sınıflandırılır',
            'B': 'Banka kredileri nakit akış tablosunda yer almaz, finansal durum tablosunda gösterilir',
            'C': 'Banka kredileri yatırım faaliyeti olarak sınıflandırılır',
            'D': 'Nakit yönetiminin parçası olduğundan nakit ve nakit benzerlerine dâhil edilebilir',
            'E': 'Tüm banka kredileri işletme faaliyeti olarak sınıflandırılır',
        },
        'D',
        'TMS 7: banka borçlanmaları genellikle finansman faaliyeti sayılır. Ancak bazı ülkelerde vadesiz mevduat hesaplarına bağlı ve bakiyesi sıklıkla artı-eksi arasında dalgalanan borçlu cari hesaplar, işletmenin nakit yönetiminin ayrılmaz parçasıysa nakit ve nakit benzerlerine dâhil edilir.',
        'TMS 7 - borçlu cari hesap',
    ),
    # düzey 2
    '0043': patch(
        "Esas faaliyetler TMS 7'de nasıl tanımlanır?",
        {
            'A': 'Esas gelir getirici faaliyetler ile yatırım ve finansman dışındaki faaliyetlerdir',
            'B': 'Duran varlık alım ve satımından doğan nakit akışlarını kapsayan faaliyetlerdir',
            'C': 'İşletmenin özkaynak ve borçlanma yapısındaki değişimleri gösteren faaliyetleri kapsar',
            'D': 'İşletmenin uzun vadeli varlık edinim ve elden çıkarma faaliyetlerini ifade eden bölümdür',
            'E': 'İşletmenin ortaklarıyla yaptığı sermaye işlemlerini kapsayan faaliyetlerdir',
        },
        'A',
        'TMS 7: işletme faaliyetleri, işletmenin esas gelir getirici faaliyetleri ile yatırım veya finansman faaliyeti olmayan diğer faaliyetlerdir. Bu bölümden gelen nakit akışı, işletmenin dış kaynağa başvurmadan nakit yaratma derecesini gösterir.',
        'TMS 7 - işletme faaliyetleri',
    ),
    # düzey 3
    '0044': patch(
        'Aşağıdakilerden hangileri nakit akış tablosunun bölümlerindendir?\n\nI. İşletme faaliyetleri\n\nII. Pazarlama faaliyetleri\n\nIII. Üretim faaliyetleri',
        {
            'A': 'II ve III',
            'B': 'Yalnız III',
            'C': 'I ve II',
            'D': 'Yalnız I',
            'E': 'I, II ve III',
        },
        'D',
        'TMS 7 nakit akışlarını işletme, yatırım ve finansman faaliyetleri olarak sınıflandırır. Bu nedenle işletme faaliyetleri (I) bir bölümken pazarlama (II) ve üretim (III) ayrı bölüm adları değildir.',
        'TMS 7 - bölümler',
    ),
    # düzey 2
    '0045': patch(
        'Stok tedarikçilerine yapılan nakit ödemeler nasıl sınıflandırılır?',
        {
            'A': 'Finansman faaliyetlerinden nakit çıkışı olarak raporlanan bir hareketi ifade eder',
            'B': 'İşletme faaliyetlerinden nakit çıkışı olarak sınıflandırılır',
            'C': 'Nakit akış tablosunda değil, bilançoda borç azalışı olarak izlenir',
            'D': 'İşletme faaliyetlerinden nakit girişi olarak gösterilir; ödeme nakit artışı doğurmaktadır',
            'E': 'Yatırım faaliyetlerinden nakit çıkışı olarak sınıflandırılır',
        },
        'B',
        'TMS 7: mal ve hizmet alımları için satıcılara yapılan ödemeler işletmenin esas faaliyetiyle ilgili olduğundan işletme faaliyetlerinden nakit çıkışıdır.',
        'TMS 7 - işletme faaliyeti',
    ),
    # düzey 2
    '0046': patch(
        'Pay ihracından sağlanan nakit hangi faaliyet grubunda raporlanır?',
        {
            'A': 'İşletme faaliyetlerinden nakit girişi olarak sınıflandırılır',
            'B': 'Nakit akış tablosunda değil, özkaynak değişim tablosunda izlenir',
            'C': 'Finansman faaliyetlerinden nakit girişi olarak sınıflandırılır',
            'D': 'Yatırım faaliyetlerinden nakit girişi olarak raporlanan bir hareketi ifade eder',
            'E': 'Pay ihracı hasılat olarak kaydedilir ve işletme faaliyeti bölümünde raporlanmaktadır',
        },
        'C',
        'TMS 7: pay ve diğer özkaynağa dayalı araçların ihracından sağlanan nakit girişleri finansman faaliyetidir; işletmenin özkaynak büyüklüğünü değiştirir.',
        'TMS 7 - finansman faaliyeti',
    ),
    # düzey 2
    '0047': patch(
        'Gelir üzerinden alınan vergilere ilişkin nakit ödemeler kural olarak hangi faaliyet grubundadır?',
        {
            'A': 'Gelir vergisi ödemeleri yatırım faaliyeti olarak sınıflandırılır',
            'B': 'Kural olarak işletme faaliyeti olarak sınıflandırılır; yatırım veya finansmanla ilişkilendirilebiliyorsa o bölümde gösterilir',
            'C': 'Gelir vergisi ödemeleri ve istisnasız finansman faaliyeti olarak sınıflandırılır; işletme faaliyetiyle ilişkilendirilmeleri mümkün değildir',
            'D': 'Gelir vergisi ödemeleri tabloda gösterilmez, gelir tablosunda yer alır',
            'E': 'Gelir vergisi ödemeleri üç bölüme eşit olarak paylaştırılarak raporlanır',
        },
        'B',
        'TMS 7: gelir vergilerinden kaynaklanan nakit akışları ayrı olarak açıklanır ve finansman ya da yatırım faaliyetiyle özellikle ilişkilendirilemiyorsa işletme faaliyeti olarak sınıflandırılır.',
        'TMS 7 - gelir vergisi',
    ),
    # düzey 2
    '0048': patch(
        'Yabancı para cinsinden bir nakit akışı hangi kurla çevrilir?',
        {
            'A': 'Yabancı para nakit akışları tabloda gösterilmez, dipnotta açıklanır',
            'B': 'Yabancı para nakit akışları dönem başındaki kur kullanılarak çevrilir',
            'C': 'Yabancı para nakit akışları çevrilmez; yabancı para olarak raporlanmaktadır',
            'D': 'İşlem tarihindeki kur kullanılarak işletmenin geçerli para birimine çevrilir',
            'E': 'Yabancı para nakit akışları dönem sonu kuruyla çevrilir',
        },
        'D',
        'TMS 7: yabancı para birimi cinsinden işlemlerden kaynaklanan nakit akışları, yabancı para tutarına nakit akışının gerçekleştiği tarihteki geçerli para birimi ile yabancı para arasındaki kur uygulanmak suretiyle çevrilir.',
        'TMS 7 - yabancı para',
    ),
    # düzey 3
    '0049': patch(
        'Yabancı para nakit üzerindeki kur etkisinin sunumuna ilişkin aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'Kur etkisi esas, yatırım ve finansman nakit akışlarından ayrı gösterilir',
            'B': 'Gerçekleşmemiş kur farkı kendi başına nakit akışı değildir',
            'C': 'Yabancı para nakit akışı işlem tarihindeki kura yakın bir kurla çevrilebilir',
            'D': 'Kur değişiminden doğan gerçekleşmemiş fark finansman faaliyetinden nakit akışıdır',
            'E': 'Kur etkisi dönem başı ve dönem sonu nakdin uzlaştırılmasına dâhil edilir',
        },
        'D',
        'TMS 7 par. 25-28: yabancı para nakit akışları işlem tarihindeki kurla çevrilir. Kur değişiminin yabancı para nakit ve nakit benzerleri üzerindeki gerçekleşmemiş etkisi nakit akışı değildir; uzlaştırma amacıyla üç faaliyet grubundan ayrı sunulur.',
        'TMS 7 Nakit Akis Tablosu',
    ),
    # düzey 3
    '0050': patch(
        'Doğrudan yöntemle ilgili aşağıdakilerden hangisi YANLIŞTIR?',
        {
            'A': 'TMS 7 doğrudan yöntemin kullanılmasını teşvik eder',
            'B': 'Satışlar ve satışların maliyeti işletme sermayesi değişimlerine göre düzeltilebilir',
            'C': 'Dönem kârına amortisman ve işletme sermayesi düzeltmeleri uygulanarak sonuca ulaşılır',
            'D': 'Brüt nakit tahsilat ve ödemelerin ana grupları açıklanır',
            'E': 'Gerekli bilgiler işletmenin muhasebe kayıtlarından elde edilebilir',
        },
        'C',
        'Dönem kârına amortisman, tahakkuk ve işletme sermayesi düzeltmeleri uygulanması dolaylı yöntemin özelliğidir. TMS 7 par. 18-19 uyarınca doğrudan yöntemde brüt nakit tahsilat ve ödeme grupları açıklanır ve bu yöntemin kullanılması teşvik edilir.',
        'TMS 7 Nakit Akis Tablosu',
    ),
    # düzey 2
    '0051': patch(
        'Dolaylı yöntemde esas faaliyet nakit akışına hangi tutardan başlanır?',
        {
            'A': "Dolaylı yöntem TMS 7'de kabul edilmeyen ve kullanılması yasaklanmış bir yöntemi ifade eder",
            'B': 'Brüt nakit giriş ve çıkışlarının ana sınıflar itibarıyla ayrı ayrı gösterildiği bir yöntemdir',
            'C': 'Hasılattan başlanır; gayrinakdi giderler hesaba katılmaz',
            'D': 'Dönem sonu nakit bakiyesinden başlanır ve düzeltme yapılmaz',
            'E': 'Dönem kâr veya zararından başlanır ve gayrinakdi kalemler için düzeltilir',
        },
        'E',
        'TMS 7: dolaylı yöntemde işletme faaliyetlerinden nakit akışı; dönem kâr veya zararının gayrinakdi işlemler, geçmiş/gelecek nakit akışlarına ilişkin ertelemeler ve tahakkuklar ile yatırım/finansman nakit akışlarıyla ilgili gelir/gider kalemlerinin etkileri için düzeltilmesiyle bulunur.',
        'TMS 7 - dolaylı yöntem',
    ),
    # düzey 2
    '0052': patch(
        'Ticari borçlardaki artış dolaylı yöntem hesabını nasıl etkiler?',
        {
            'A': 'Henüz ödenmemiş gideri gösterdiğinden dönem kârına eklenir',
            'B': 'Ticari borçlardaki artış yatırım faaliyeti olarak sınıflandırılan bir hareketi ifade eder',
            'C': 'Nakit çıkışı doğurduğundan dönem kârından düşülür',
            'D': 'Ticari borçlardaki artış finansman faaliyetinden nakit girişi olarak raporlanır',
            'E': 'Ticari borçlardaki değişim düzeltmeye konu edilmez',
        },
        'A',
        'Dolaylı yöntemde ticari borçlardaki artış, giderin kâra yansıdığı ancak henüz ödenmediğini gösterir; bu nedenle dönem kârına eklenir.',
        'TMS 7 - işletme sermayesi düzeltmesi',
    ),
    # düzey 3
    '0053': patch(
        "Dönem net kârı 150.000 ₺, amortisman 40.000 ₺, stoklarda azalış 25.000 ₺ ve ticari borçlarda artış 30.000 ₺'dir. Dolaylı yönteme göre işletme faaliyetlerinden nakit akışı kaç ₺'dir?",
        {
            'A': '135.000 ₺',
            'B': '195.000 ₺',
            'C': '245.000 ₺',
            'D': '150.000 ₺',
            'E': '165.000 ₺',
        },
        'C',
        'Amortisman eklenir; stoklardaki azalış nakde dönüşen varlığı, borçlardaki artış ise ödenmemiş gideri gösterdiğinden ikisi de eklenir: 150.000 + 40.000 + 25.000 + 30.000 = 245.000 ₺.',
        'TMS 7 - dolaylı yöntem',
    ),
    # düzey 3
    '0054': patch(
        "Dönem net satışları 900.000 ₺ ve ticari alacaklardaki artış 70.000 ₺'dir. Doğrudan yönteme göre müşterilerden yapılan tahsilat kaç ₺'dir?",
        {
            'A': '760.000 ₺',
            'B': '900.000 ₺',
            'C': '70.000 ₺',
            'D': '970.000 ₺',
            'E': '830.000 ₺',
        },
        'E',
        'Müşterilerden tahsilat = Net satışlar − Ticari alacaklardaki artış = 900.000 − 70.000 = 830.000 ₺. Alacak arttıysa satışın bir kısmı henüz tahsil edilmemiştir.',
        'TMS 7 - doğrudan yöntem',
    ),
    # düzey 2
    '0055': patch(
        'Bağlı ortaklık ve diğer işletmelerin edinimi veya elden çıkarılması bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bu işlemler tabloda gösterilmez, dipnotta açıklanır',
            'B': 'Bu işlemler finansman faaliyeti olarak sınıflandırılır ve özkaynak yapısını değiştirmektedir',
            'C': 'Bu işlemler işletme faaliyeti olarak sınıflandırılır',
            'D': 'Ayrı olarak sunulur ve yatırım faaliyeti olarak sınıflandırılır',
            'E': 'Bu işlemler diğer yatırım hareketleriyle birleştirilerek tek bir toplam hâlinde sunulur',
        },
        'D',
        'TMS 7: bağlı ortaklıkların ve diğer işletmelerin edinimi veya elden çıkarılmasından kaynaklanan toplam nakit akışları ayrı olarak sunulur ve yatırım faaliyeti olarak sınıflandırılır.',
        'TMS 7 - bağlı ortaklık edinimi',
    ),
    # düzey 2
    '0056': patch(
        'Finansal kuruluşlarda faiz akışları bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Finansal kuruluşlarda faiz akışları yatırım faaliyeti olarak raporlanır',
            'B': 'Finansal kuruluşlarda faiz akışları finansman faaliyeti olarak sınıflandırılır; bu kuruluşların esas faaliyetiyle ilişkilendirilmeleri kabul edilmez',
            'C': 'Finansal kuruluşlarda faiz akışları tabloda gösterilmez, dipnotta açıklanır',
            'D': 'Finansal kuruluşlar nakit akış tablosu düzenlemekten muaftır',
            'E': 'Finansal kuruluşlarda ödenen ve tahsil edilen faizler ile kâr payları genellikle işletme faaliyeti olarak sınıflandırılır',
        },
        'E',
        'TMS 7: finansal kuruluşlar açısından ödenen ve tahsil edilen faizler ile kâr payları genellikle işletme faaliyetleri olarak sınıflandırılır; çünkü bunlar esas gelir getirici faaliyetlerinin parçasıdır.',
        'TMS 7 - finansal kuruluşlarda faiz',
    ),
    # düzey 2
    '0057': patch(
        'Nakit akış tablosu düzenleme zorunluluğu bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Nakit akış tablosunu büyük ölçekli işletmeler düzenler; küçükler muaftır',
            'B': 'TMS 7 uygulayan işletmeler bu tabloyu tam finansal tablo setinin parçası olarak sunar',
            'C': 'Nakit akış tablosu işletme zarar ettiği dönemlerde düzenlenir',
            'D': 'Nakit akış tablosunu finansal kuruluşlar düzenler; diğer sektörler kapsam dışıdır',
            'E': 'Tablo isteğe bağlıdır; işletme dipnotlarda özet bilgi vermeyi seçebilir',
        },
        'B',
        'TMS 7: işletme, bu Standarda uygun olarak nakit akış tablosu düzenler ve bunu finansal tabloların sunulduğu her dönem için tam finansal tablo setinin ayrılmaz bir parçası olarak sunar.',
        'TMS 7 - düzenleme zorunluluğu',
    ),
    # düzey 3
    '0058': patch(
        'Bir işletme, satın aldığı makinenin bedelini nakit ödemek yerine kendi çıkardığı payları vererek karşılamıştır. TMS 7 bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Nakit kullanımı olmadığından işlem tabloya alınmaz; dipnotlarda açıklanır',
            'B': 'İşlem işletme faaliyeti olarak sınıflandırılıp dönem nakdini azaltan bir kalem olarak gösterilir',
            'C': 'İşlem raporlanmaz; dipnotta da açıklanmaz',
            'D': 'İşlem yatırım faaliyeti bölümünde nakit çıkışı olarak raporlanır',
            'E': 'İşlem yatırım faaliyetinden nakit çıkışı ve finansman faaliyetinden nakit girişi olarak gösterilir',
        },
        'A',
        'TMS 7: varlıkların pay ihracıyla veya takas yoluyla edinilmesi nakit kullanımı gerektirmeyen bir işlemdir; nakit akış tablosuna dâhil edilmez, dipnotlarda açıklanır.',
        'TMS 7 - nakit içermeyen işlem (senaryo)',
    ),
    # düzey 3
    '0059': patch(
        'Aşağıdaki ifadelerden hangileri TMS 7 bakımından doğrudur?\n\nI. Bağlı ortaklık edinimi yatırım faaliyetidir\n\nII. Edinimde ödenen bedelden edinilen nakit düşülerek net gösterilir\n\nIII. Nakit akış tablosu isteğe bağlı bir tablodur',
        {
            'A': 'Yalnız I',
            'B': 'I, II ve III',
            'C': 'Yalnız III',
            'D': 'II ve III',
            'E': 'I ve II',
        },
        'E',
        'Bağlı ortaklık edinimi yatırım faaliyetidir (I) ve edinilen nakit düşülerek net gösterilir (II). Nakit akış tablosu ise tam finansal tablo setinin ayrılmaz parçasıdır, isteğe bağlı değildir; bu nedenle III yanlıştır.',
        'TMS 7 - genel',
    ),
    # düzey 3
    '0060': patch(
        "Aşağıdakilerden hangileri TMS 7'ye göre işletme faaliyeti sayılır?\n\nI. Pay ihracından sağlanan nakit\n\nII. Mal satışından tahsilat\n\nIII. Satıcılara yapılan ödemeler",
        {
            'A': 'I ve II',
            'B': 'Yalnız III',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'D',
        'Mal satışından tahsilat (II) ve satıcılara ödemeler (III) esas gelir getirici faaliyetlerdendir, işletme faaliyetidir. Pay ihracı (I) ise özkaynak yapısını değiştirdiğinden finansman faaliyetidir.',
        'TMS 7 - faaliyet sınıflandırması',
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
    print(f"1 paket / {len(PATCHES)} soru ('TMS 7 Nakit Akis Tablosu' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
