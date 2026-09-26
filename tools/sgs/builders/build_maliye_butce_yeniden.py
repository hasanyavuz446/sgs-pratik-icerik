#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Butce ve Maliye Politikasi — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gercek sinav profiline gore yeniden yazim: butce islevleri ve ilkeleri, butce sistemleri, 5018 kapsami ve cetveller, butce takvimi (OVP, cagri, teklif, gecici/ek butce, kesinhesap 6 ay / GUB 75 gun), odenek aktarma/yedek/ortulu odenek/yuklenme, acik olculeri (birincil, operasyonel, yapisal, KKBG), borc dinamigi, carpanlar, dislama, Mundell-Fleming, gecikmeler, mali kurallar.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 5018 sayili KMYKK guncel metni ve ekli cetveller; Anayasa m.161 (6771 ile degisik, m.162-164 mulga); kamu maliyesi teorisi
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/maliye/butce_maliye_politikasi.json"
STYLE_REF = 'SGS Maliye (gercek sinav profiline kalibre: kisa sik + olay/hesap)'
ONEK = "mal-butce-gen-"


def patch(stem, options, answer, solution, ref='5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Bütçe kanunuyla kamu idarelerine yalnız kanunda gösterilen tutar ve amaçlar için harcama yapma izni verilmesi ve bu iznin dışına çıkılamaması, bütçenin öncelikle hangi işlevini yansıtır?',
        {
            'A': 'İstatistiki işlevi',
            'B': 'Hukuki işlevi',
            'C': 'Yönetsel planlama işlevi',
            'D': 'Ekonomik işlevi',
            'E': 'Sosyal işlevi',
        },
        'B',
        'Bütçe kanunu, yasama organının yürütmeye gelir toplama ve harcama yapma **izni ve yetkisi** verdiği bir hukuki işlemdir; ödenekler harcamanın üst sınırını ve amacını bağlayıcı biçimde belirler. Bütçenin ekonomik işlevi kaynak dağılımı, istikrar ve büyüme üzerindeki etkisiyle, sosyal işlevi ise gelir dağılımına etkisiyle ilgilidir.',
        'Kamu maliyesi teorisi: bütçenin işlevleri',
    ),
    # düzey 2
    '0002': patch(
        "Aşağıdakilerden hangisi 5018 sayılı Kanun'un 13. maddesinde sayılan bütçe ilkelerinden biri değildir?",
        {
            'A': 'Kamu idarelerinin kendi gelirlerini doğrudan kendi giderlerine ayırması',
            'B': 'Bütçelerin ait olduğu yıl başlamadan onaylanmadıkça uygulanmaması',
            'C': 'Bütçelerde bütçeyi ilgilendirmeyen hususlara yer verilmemesi',
            'D': 'Ödeneklerin belirli amaçları gerçekleştirmek üzere tahsis edilmesi',
            'E': 'Bütçelerin izleyen iki yılın tahminleriyle birlikte görüşülmesi',
        },
        'A',
        "5018 m. 13, bütçelerin izleyen iki yılın tahminleriyle birlikte görüşülmesini (d), bütçeyi ilgilendirmeyen hususlara yer verilmemesini (j), yıl başlamadan onaylanmadıkça uygulanmamasını (i) ve ödeneklerin belirli amaçlara tahsisini (o) ilke olarak sayar. Gelirlerin doğrudan belirli giderlere ayrılması ise m. 13/g'deki ademi tahsis ilkesine aykırıdır.",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 13',
    ),
    # düzey 1
    '0003': patch(
        "5018 sayılı Kanun'la benimsenen ve kamu idarelerinin stratejik planları, performans hedefleri ve göstergeleriyle kaynak tahsisini ilişkilendiren bütçe yaklaşımı aşağıdakilerden hangisidir?",
        {
            'A': 'Sıfır tabanlı bütçe',
            'B': 'Artımsal bütçe',
            'C': 'Performans esaslı bütçeleme',
            'D': 'Klasik kalem bütçe',
            'E': 'Gayrisafi bütçe',
        },
        'C',
        '5018 sayılı Kanun kamu idarelerinin **stratejik plan** hazırlamasını, bütçelerin stratejik planlar ve performans ölçütlerine göre hazırlanmasını (m. 9, m. 13/c) öngörerek **performans esaslı bütçeleme** anlayışını getirmiştir. Gayrisafilik bir bütçe ilkesidir, bütçe sistemi değildir.',
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 9, m. 13/c',
    ),
    # düzey 2
    '0004': patch(
        "Aşağıdaki kamu idarelerinden hangisinin bütçesi 5018 sayılı Kanun'a ekli (IV) sayılı cetvelde yer alır ve bu nedenle merkezî yönetim bütçesine dahil değildir?",
        {
            'A': 'Devlet Su İşleri Genel Müdürlüğü',
            'B': 'Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu',
            'C': 'Türkiye İstatistik Kurumu',
            'D': 'Türkiye İş Kurumu Genel Müdürlüğü',
            'E': 'Gelir İdaresi Başkanlığı',
        },
        'D',
        '(IV) sayılı cetvel **sosyal güvenlik kurumlarını** sayar: Sosyal Güvenlik Kurumu ve **Türkiye İş Kurumu Genel Müdürlüğü**. TÜİK ve DSİ (II) sayılı cetvelde özel bütçeli idare, KGK (III) sayılı cetvelde düzenleyici ve denetleyici kurum, Gelir İdaresi Başkanlığı ise (I) sayılı cetvelde genel bütçeli idaredir.',
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu (IV) sayılı cetvel',
    ),
    # düzey 2
    '0005': patch(
        "Genel yönetim kapsamındaki kamu idarelerinin sağladığı teşvik ve desteklerin bir yılı geçmemek üzere belirli dönemler itibarıyla kamuoyuna açıklanması 5018'deki hangi ilkenin gereğidir?",
        {
            'A': 'Ademi tahsis',
            'B': 'Hazine birliği',
            'C': 'Mali disiplin',
            'D': 'Hesap verme sorumluluğu',
            'E': 'Mali saydamlık',
        },
        'E',
        "5018 m. 7'deki **mali saydamlık** ilkesi, kamu kaynağının elde edilmesi ve kullanılmasında denetimin sağlanması için kamuoyunun zamanında bilgilendirilmesini ister; teşvik ve desteklemelerin bir yılı geçmeyen dönemlerle açıklanması bu maddenin (c) bendidir. **Hesap verme sorumluluğu** (m. 8) kaynak kullanan yetkililerin yetkili mercilere hesap vermesidir.",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 7-8',
    ),
    # düzey 3
    '0006': patch(
        'Bir yılın bütçe kanunu mali yılbaşına kadar kabul edilememiş, geçici bütçe kanunu da çıkarılamamıştır. Bu durumda yeni bütçe kanunu kabul edilinceye kadar ne uygulanır?',
        {
            'A': 'Önceki yılın bütçesi yeniden değerleme oranına göre artırılarak',
            'B': 'Orta vadeli programdaki ödenek teklif tavanları',
            'C': 'Önceki yılın bütçesi TÜFE artışı oranında artırılarak',
            'D': 'Önceki yılın bütçesi aynı tutarlarla',
            'E': 'Cumhurbaşkanlığı kararnamesiyle belirlenen harcama tavanları',
        },
        'A',
        "Anayasa m. 161 ve 5018 m. 19'a göre bütçe süresinde yürürlüğe konulamazsa önce **geçici bütçe kanunu** çıkarılır; o da çıkarılamazsa yeni bütçe kabul edilinceye kadar **bir önceki yılın bütçesi yeniden değerleme oranına göre artırılarak** uygulanır. Kullanılacak oran TÜFE değil, VUK'taki yeniden değerleme oranıdır.",
        '2709 sayili T.C. Anayasasi m. 161; 5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 19',
    ),
    # düzey 2
    '0007': patch(
        "2026 mali yılına ait merkezî yönetim kesinhesap kanunu teklifi ile Sayıştayın genel uygunluk bildirimine ilişkin süreler Anayasa'ya göre hangisinde doğru verilmiştir?",
        {
            'A': "Teklif en geç 31 Mart 2027'ye kadar sunulur; bildirim tekliften itibaren 75 gün içinde verilir",
            'B': "Teklif en geç 30 Haziran 2027'ye kadar sunulur; bildirim tekliften itibaren 55 gün içinde verilir",
            'C': "Teklif en geç 31 Mart 2027'ye kadar sunulur; bildirim tekliften itibaren 55 gün içinde verilir",
            'D': "Teklif en geç 30 Haziran 2027'ye kadar sunulur; bildirim tekliften itibaren 75 gün içinde verilir",
            'E': "Teklif en geç 31 Aralık 2027'ye kadar sunulur; bildirim tekliften itibaren 75 gün içinde verilir",
        },
        'D',
        "Anayasa m. 161'e göre kesinhesap kanunu teklifi ilgili mali yılın sonundan başlayarak **en geç altı ay** sonra (2026 için 30 Haziran 2027) Cumhurbaşkanınca TBMM'ye sunulur; Sayıştay genel uygunluk bildirimini teklifin verilmesinden başlayarak **en geç 75 gün** içinde Meclise sunar. Kesinhesap teklifi yeni yıl bütçesiyle birlikte görüşülür.",
        '2709 sayili T.C. Anayasasi m. 161',
    ),
    # düzey 2
    '0008': patch(
        "5018 sayılı Kanun'a göre kamu idarelerinin kendi bütçeleri içindeki ödenek aktarmalarına ilişkin aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Yedek ödenekten aktarma yapılmış tertiplerden diğer tertiplere aktarma yapılamaz',
            'B': 'Personel giderleri tertiplerinden diğer tertiplere aktarma yapılabilir',
            'C': 'Tertipteki ödeneğin yüzde yirmisine kadar kurum içi aktarma yapılabilir',
            'D': 'Kurumlar arası ödenek aktarmaları kanunla yapılır',
            'E': 'Aktarma yapılmış tertiplerden başka tertiplere aktarma yapılamaz',
        },
        'B',
        "5018 m. 21'e göre idarelerin bütçeleri içinde **personel giderleri tertiplerinden**, aktarma yapılmış tertiplerden ve yedek ödenekten aktarma yapılmış tertiplerden diğer tertiplere **ödenek aktarılamaz** (yatırım programına ek cetvellerdeki proje değişiklikleri hariç). Kurum içi aktarma sınırı tertip ödeneğinin %20'si, kurumlar arası aktarma ise kanunla yapılır.",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 21',
    ),
    # düzey 1
    '0009': patch(
        "5018 sayılı Kanun'a göre cari yılda kullanılmayan ödeneklerin durumu aşağıdakilerden hangisidir?",
        {
            'A': 'İzleyen yıla devreder',
            'B': 'Yedek ödeneğe eklenir',
            'C': 'Örtülü ödeneğe aktarılır',
            'D': 'Emanet hesaplarına alınır',
            'E': 'Yıl sonunda iptal edilir',
        },
        'E',
        "5018 m. 20/f'ye göre **cari yılda kullanılmayan ödenekler yıl sonunda iptal edilir**. Bu, bütçenin yıllık olma ilkesinin sonucudur; ödenekler kural olarak ait oldukları mali yıl içinde kullanılabilir.",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 20',
    ),
    # düzey 3
    '0010': patch(
        "Bir yılda kamu gelirleri 900, faiz dışı harcamalar 950 ve nominal faiz ödemeleri 120 birimdir. Borç stoku 1.000 birim, enflasyon oranı %8'dir. Operasyonel açık kaç birimdir?",
        {
            'A': '90',
            'B': '130',
            'C': '120',
            'D': '170',
            'E': '50',
        },
        'A',
        "Faiz dışı (birincil) açık = 950 − 900 = 50. Faiz ödemelerinin enflasyonu telafi eden kısmı = 1.000 × %8 = 80; reel faiz = 120 − 80 = 40. **Operasyonel açık** = birincil açık + reel faiz = 50 + 40 = **90**. Toplam (nominal) açık ise 50 + 120 = 170'tir; operasyonel açık, enflasyon nedeniyle şişen nominal faizi ayıklar.",
        'Kamu maliyesi teorisi: bütçe açığı ölçüleri',
    ),
    # düzey 2
    '0011': patch(
        'Kısa vadeli (dalgalı) kamu borçlarının, alacaklıların rızası alınarak uzun vadeli borçlara dönüştürülmesine ne ad verilir?',
        {
            'A': 'Konversiyon',
            'B': 'Moratoryum',
            'C': 'Borç swapı',
            'D': 'Borcun itfası',
            'E': 'Konsolidasyon',
        },
        'E',
        '**Konsolidasyon** (tahkim), kısa vadeli borçların uzun vadeli borçlara dönüştürülmesidir. **Konversiyon** ise mevcut borcun faiz oranının (genellikle düşürülerek) değiştirilmesidir; moratoryum borç ödemelerinin durdurulması, itfa borcun anapara olarak geri ödenmesidir.',
        'Kamu maliyesi teorisi: kamu borçları',
    ),
    # düzey 2
    '0012': patch(
        'Kamu borçlanmasının türüne göre etkilerine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İç borcun faiz ödemeleri ülke içinde gelir dağılımını etkiler',
            'B': 'Dış borcun geri ödenmesi ülkenin kullanabileceği kaynakları azaltmaz',
            'C': 'Dış borç, borçlanma döneminde ülkenin kullanabileceği toplam kaynakları artırır',
            'D': 'Dış borcun geri ödenmesi ülkeden net kaynak çıkışına yol açar',
            'E': 'İç borç, ekonomideki satın alma gücünü özel kesimden kamu kesimine aktarır',
        },
        'B',
        'Dış borç, borçlanma döneminde yurt dışından kaynak girişi sağlayarak kullanılabilir kaynakları artırır; **geri ödeme döneminde** ise ülkeden net kaynak çıkışı doğurur ve milli gelirden pay almayı gerektirir. İç borç ise kaynakları ülke içinde el değiştirir; faiz ödemeleri vergi mükelleflerinden tahvil sahiplerine gelir aktarır.',
        'Kamu maliyesi teorisi: iç ve dış borç',
    ),
    # düzey 2
    '0013': patch(
        'Ekonomi durgunluğa girdiğinde, hükümet yeni bir karar almadan artan oranlı gelir vergisi hasılatının düşmesi ve işsizlik sigortası ödemelerinin artması hangi mekanizmanın işleyişidir?',
        {
            'A': 'Otomatik stabilizatörler',
            'B': 'Formül esnekliği',
            'C': 'İhtiyari maliye politikası',
            'D': 'Mali sürüklenme',
            'E': 'Dışlama etkisi',
        },
        'A',
        '**Otomatik stabilizatörler**, konjonktüre göre yeni bir karar gerekmeden kendiliğinden devreye giren vergi ve harcama unsurlarıdır: durgunlukta artan oranlı vergi hasılatı düşer, işsizlik ödemeleri artar ve harcanabilir gelirdeki düşüş sınırlanır. İhtiyari politika ise hükümetin bilinçli kararıyla uygulanır.',
        'Kamu maliyesi teorisi: otomatik stabilizatörler',
    ),
    # düzey 3
    '0014': patch(
        'Sermaye hareketlerinin tam serbest olduğu ve sabit kur rejiminin uygulandığı küçük bir açık ekonomide genişletici maliye politikasının sonucuna ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Maliye politikası etkisizdir; ulusal para değer kazanıp net ihracat düşer',
            'B': 'Maliye politikası etkisizdir; faiz artışı yatırımları tümden dışlar',
            'C': 'Maliye politikası etkilidir; para arzı değişmeden faiz kalıcı olarak yükselir',
            'D': 'Maliye politikası etkilidir; merkez bankası kuru korurken para arzı artar',
            'E': 'Maliye politikası etkisizdir; merkez bankası para arzını azaltır',
        },
        'D',
        'Genişletici maliye politikası faizi yükseltme eğilimi yaratır ve sermaye girişine yol açar. **Sabit kurda** merkez bankası, ulusal paranın değer kazanmasını önlemek için döviz alır; para arzı artar, faiz dünya düzeyine döner ve gelir artışı büyür: **maliye politikası etkilidir**. Esnek kurda ise ulusal para değer kazanır, net ihracat düşer ve maliye politikası etkisiz kalır.',
        'Kamu maliyesi teorisi: Mundell-Fleming',
    ),
    # düzey 2
    '0015': patch(
        'Aşırı talep kaynaklı enflasyonla mücadele eden bir hükümetin uygulaması beklenen maliye politikası bileşimi aşağıdakilerden hangisidir?',
        {
            'A': 'Transfer harcamalarını artırıp bütçe açığı vermek',
            'B': 'Kamu harcamalarını artırmak ve vergileri düşürmek',
            'C': 'Kamu harcamalarını kısmak ve vergileri artırmak',
            'D': 'Merkez bankasından borçlanarak yatırımları artırmak',
            'E': 'Vergileri düşürüp açığı para basarak finanse etmek',
        },
        'C',
        'Talep enflasyonunda toplam talebi kısmak gerekir: **daraltıcı maliye politikası** kamu harcamalarını azaltır, vergileri artırır ve bütçe fazlası verir. Harcama artışı, vergi indirimi ve merkez bankası kaynaklı finansman talebi ve para arzını artırarak enflasyonu körükler.',
        'Kamu maliyesi teorisi: maliye politikası',
    ),
    # düzey 2
    '0016': patch(
        'Bütçe açığının finansman yöntemlerinin enflasyonist etkisine ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Merkez bankası kaynağıyla finansman, halktan borçlanmaya göre daha enflasyonisttir',
            'B': 'Vergiyle finansman, para basmaya göre daha enflasyonisttir',
            'C': 'Finansman yöntemi enflasyon üzerinde fark yaratmaz',
            'D': 'Dış borçlanma, döviz girişi yoluyla para arzını merkez bankası finansmanından daha fazla artırır',
            'E': 'Halktan borçlanma, merkez bankası kaynağına göre daha enflasyonisttir',
        },
        'A',
        'Merkez bankası kaynağıyla (para basarak) finansman ekonomiye yeni satın alma gücü ekler ve para arzını doğrudan artırır; bu nedenle en enflasyonist yöntemdir. Halktan (iç piyasadan) borçlanmada ise mevcut satın alma gücü özel kesimden kamuya aktarılır; para arzı değişmez, faiz yükselebilir.',
        'Kamu maliyesi teorisi: kamu borçlanmasının para arzına etkisi',
    ),
    # düzey 2
    '0017': patch(
        'Klasik ve Keynesyen görüşlerin kamu borcunun yüküne ilişkin değerlendirmesinde, iç borcun yükünün gelecek kuşaklara aktarılmadığını savunan temel argüman aşağıdakilerden hangisidir?',
        {
            'A': 'İç borcun çoğunlukla yabancılarca tutulması nedeniyle',
            'B': 'Borcun faizlerinin vergilerden yüksek olması nedeniyle',
            'C': 'Borç ülke içinde el değiştirdiği için toplum kendi kendine borçludur',
            'D': 'İç borç ödenmediği sürece ekonomide kaynak kullanılmadığı için',
            'E': 'Borçlanma para arzını azaltarak enflasyonu önlediği için',
        },
        'C',
        'Keynesyen yaklaşımda iç borçta alacaklı ve borçlu aynı toplumun üyeleridir: geri ödeme, vergi mükelleflerinden tahvil sahiplerine bir **transferdir** ve toplumun toplam kaynakları azalmaz; bu nedenle yük gelecek kuşaklara aktarılmaz. Buchanan gibi eleştirmenler ise yükün, borçlanma kararına katılmayan gelecek mükelleflere geçtiğini savunur.',
        'Kamu maliyesi teorisi: Ricardo denkliği ve borç',
    ),
    # düzey 2
    '0018': patch(
        'Haavelmo teoremine ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Harcama ve götürü vergi aynı tutarda artırıldığında milli gelir değişmez',
            'B': 'Harcama ve götürü vergi aynı tutarda artırıldığında milli gelir bu tutar kadar artar',
            'C': 'Denk bütçe çarpanı marjinal tüketim eğilimine eşittir',
            'D': 'Vergi artışı harcama artışından daha genişletici etki yapar',
            'E': 'Denk bütçeli genişleme milli geliri azaltır',
        },
        'B',
        "**Haavelmo (denk bütçe) teoremine** göre basit Keynesyen modelde harcama ile götürü vergi aynı tutarda artırıldığında harcama çarpanı 1/(1−c) ile vergi çarpanı −c/(1−c)'nin toplamı 1 olur; milli gelir, bütçe büyüklüğündeki artış kadar artar. Bütçe denk kalsa da ekonomi genişler.",
        'Kamu maliyesi teorisi: Haavelmo teoremi',
    ),
    # düzey 2
    '0019': patch(
        'İhtiyari (bilinçli) maliye politikasının otomatik stabilizatörlere göre dezavantajı aşağıdakilerden hangisidir?',
        {
            'A': 'Bütçe dengesini etkilememesi',
            'B': 'Konjonktüre tepki verememesi',
            'C': 'Etkisinin gelir dağılımıyla sınırlı kalması',
            'D': 'Etkisinin büyüklüğünün küçük kalması',
            'E': 'Tanıma ve karar süreçleri nedeniyle zamanlamasının gecikebilmesi',
        },
        'E',
        'İhtiyari politikada sorunun fark edilmesi, önlemin tasarlanıp yasalaşması ve uygulamaya konması zaman alır; önlem ekonomiye ulaştığında konjonktür değişmiş olabilir ve politika istikrarsızlaştırıcı hâle gelebilir. Buna karşın büyüklüğü ve yönü duruma göre ayarlanabildiği için güçlü etki yaratabilir.',
        'Kamu maliyesi teorisi: ihtiyari politika',
    ),
    # düzey 2
    '0020': patch(
        'Geçici bütçe ile ek bütçe arasındaki farka ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İkisi de asıl bütçe kabul edilemediğinde başvurulan yollardır',
            'B': 'Geçici bütçe ödenekleri yıl sonuna kadar kullanılır ve asıl bütçeye dahil edilmez',
            'C': 'Geçici bütçe Cumhurbaşkanlığı kararnamesiyle, ek bütçe kanunla yapılır',
            'D': 'Geçici bütçe asıl bütçe yetişmediğinde, ek bütçe asıl bütçe yetersiz kaldığında yapılır',
            'E': 'Ek bütçe mali yılbaşından önce, geçici bütçe mali yıl içinde yapılır',
        },
        'D',
        '**Geçici bütçe**, bütçe kanunu süresinde yürürlüğe konulamadığında belirli bir dönem için çıkarılır ve asıl bütçe yürürlüğe girince sona erer; bu dönemdeki harcamalar cari yıl bütçesine dahil edilir (5018 m. 19). **Ek bütçe** ise yürürlükteki bütçenin ödenekleri yetersiz kaldığında veya öngörülmeyen hizmetler için karşılığı gelir gösterilerek kanunla yapılır.',
        'Kamu maliyesi teorisi: ek bütçe ve geçici bütçe',
    ),
    # düzey 1
    '0021': patch(
        'Halkın temsilcilerinin vergi koyma ve kamu harcamalarına izin verme yetkisini ifade eden bütçe hakkının tarihsel başlangıcı olarak kabul edilen belge aşağıdakilerden hangisidir?',
        {
            'A': 'İnsan ve Yurttaş Hakları Bildirisi (1789)',
            'B': 'Kanun-i Esasi (1876)',
            'C': 'Tanzimat Fermanı (1839)',
            'D': 'Magna Carta (1215)',
            'E': 'Westfalya Antlaşması (1648)',
        },
        'D',
        "**Magna Carta** (1215), İngiltere'de kralın vergi ve benzeri yükümlülükleri ancak ülke konseyinin rızasıyla koyabileceği ilkesini getirerek vergilendirmede rıza ve bütçe hakkının başlangıcı sayılır. Bütçe hakkı zamanla harcamalara izin verme ve bütçeyi denetleme yetkisini de kapsayacak biçimde gelişmiştir.",
        'Kamu maliyesi teorisi: bütçe hakkı',
    ),
    # düzey 2
    '0022': patch(
        "Bir kamu idaresinin elde ettiği 100 milyon ₺ hasılattan bu hasılatı elde etmek için yaptığı 20 milyon ₺ gideri düşerek bütçeye yalnız 80 milyon ₺ net gelir yazması, 5018 sayılı Kanun'daki hangi bütçe ilkesine aykırıdır?",
        {
            'A': 'Gelir ve gider denkliğinin sağlanması',
            'B': 'Belirli gelirlerin belirli giderlere tahsis edilmemesi',
            'C': 'Gelir ve giderlerin gayrisafi gösterilmesi',
            'D': 'Bütçeyi ilgilendirmeyen hususlara yer verilmemesi',
            'E': 'Bütçenin önceden onaylanması',
        },
        'C',
        "5018 m. 13/f'ye göre **tüm gelir ve giderler gayrisafi** olarak bütçede gösterilir; gelirler kendilerini elde etmek için yapılan giderlerle mahsup edilip net tutarla yazılamaz. Gayrisafi (brüt) bütçe usulü, idarenin gerçek harcama büyüklüğünün saydam biçimde görülmesini sağlar.",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 13/f',
    ),
    # düzey 2
    '0023': patch(
        'Harcamaların personel, kırtasiye, yakıt gibi satın alınan girdiler itibarıyla ayrıntılı gösterildiği ve asıl amacı harcamaların yasama organınca denetlenmesi olan bütçe sistemi aşağıdakilerden hangisidir?',
        {
            'A': 'Klasik (kalem) bütçe',
            'B': 'Performans esaslı bütçe',
            'C': 'Sıfır tabanlı bütçe',
            'D': 'Planlama-programlama-bütçeleme sistemi',
            'E': 'Program bütçe',
        },
        'A',
        '**Klasik (kalem) bütçe** harcamaları girdiler (kalemler) itibarıyla sınıflandırır ve ödenek aşımını engelleyen hukuki denetimi öne çıkarır; harcamanın hangi sonucu ürettiği sorusuna cevap vermez. Program ve performans bütçeleri ise harcamayı amaç, faaliyet ve sonuçlarla ilişkilendirir.',
        'Kamu maliyesi teorisi: bütçe sistemleri',
    ),
    # düzey 2
    '0024': patch(
        "Bir bakanlığa bağlı veya ilgili olarak kurulan, kendisine gelir tahsis edilen ve bu gelirlerden harcama yapma yetkisi bulunan Karayolları Genel Müdürlüğünün bütçesi 5018'e göre hangi türdendir?",
        {
            'A': 'Düzenleyici ve denetleyici kurum bütçesi',
            'B': 'Özel bütçe',
            'C': 'Sosyal güvenlik kurumu bütçesi',
            'D': 'Mahallî idare bütçesi',
            'E': 'Genel bütçe',
        },
        'B',
        "5018 m. 12'ye göre **özel bütçe**, bir bakanlığa bağlı veya ilgili olarak belirli bir kamu hizmetini yürütmek üzere kurulan, gelir tahsis edilen ve bu gelirlerden harcama yapma yetkisi verilen idarelerin bütçesidir; Karayolları Genel Müdürlüğü (II) sayılı cetvelde yer alır. Genel bütçe Devlet tüzel kişiliğine dahil idarelerin bütçesidir.",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 12, (II) sayılı cetvel',
    ),
    # düzey 2
    '0025': patch(
        "5018 sayılı Kanun'a göre merkezî yönetim bütçe kanun teklifine, TBMM'deki görüşmelerde dikkate alınmak üzere Cumhurbaşkanlığınca eklenen belgeler arasında aşağıdakilerden hangisi yer almaz?",
        {
            'A': 'Orta vadeli programı da içeren bütçe gerekçesi',
            'B': 'Vergi muafiyet ve istisnaları nedeniyle vazgeçilen kamu gelirleri cetveli',
            'C': 'Kamu borç yönetimi raporu',
            'D': 'Sayıştayın genel uygunluk bildirimi',
            'E': 'Yıllık ekonomik rapor',
        },
        'D',
        "5018 m. 18'e göre bütçe kanun teklifine bütçe gerekçesi (orta vadeli programı da içeren), yıllık ekonomik rapor, vazgeçilen kamu gelirleri cetveli, kamu borç yönetimi raporu, genel yönetim bütçe gerçekleşme ve tahminleri, mahallî idareler ile sosyal güvenlik kurumlarının bütçe tahminleri ve merkezî yönetim bütçesinden yardım alan kuruluşların listesi eklenir. **Genel uygunluk bildirimi** ise Sayıştayca kesinhesap kanunu teklifiyle ilişkili olarak Meclise sunulur.",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 18',
    ),
    # düzey 1
    '0026': patch(
        'Merkezî yönetim kapsamındaki bir idarenin ödeneklerinin yıl içinde yetersiz kalması veya öngörülmeyen bir hizmetin ortaya çıkması hâlinde, karşılığı gelir gösterilmek kaydıyla hangi yola başvurulabilir?',
        {
            'A': 'Kurum içi tertipler arasında sınırsız aktarma',
            'B': 'Kanunla ek bütçe yapılması',
            'C': 'Örtülü ödenekten doğrudan harcama',
            'D': 'Cumhurbaşkanlığı kararnamesiyle ödenek artırılması',
            'E': 'Geçici bütçe kanunu çıkarılması',
        },
        'B',
        "5018 m. 19'a göre ödeneklerin yetersiz kalması veya öngörülmeyen hizmetler için, karşılığı gelir gösterilmek kaydıyla **kanunla ek bütçe** yapılabilir. Anayasa m. 161, ödeneğin harcanabilecek tutarın sınırı olduğunu ve bu sınırın Cumhurbaşkanlığı kararnamesiyle aşılabileceğine dair bütçe kanununa hüküm konulamayacağını belirtir.",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 19',
    ),
    # düzey 2
    '0027': patch(
        "5018 sayılı Kanun'a göre aşağıdaki kurumlardan hangisi bütçesini Cumhurbaşkanlığına değil, Eylül ayı sonuna kadar doğrudan TBMM'ye gönderir?",
        {
            'A': 'Gelir İdaresi Başkanlığı',
            'B': 'Türkiye İstatistik Kurumu',
            'C': 'Karayolları Genel Müdürlüğü',
            'D': 'Sosyal Güvenlik Kurumu',
            'E': 'Sayıştay',
        },
        'E',
        "5018 m. 18'e göre **TBMM, Sayıştay ve düzenleyici ve denetleyici kurumlar** bütçelerini Eylül ayı sonuna kadar doğrudan TBMM'ye gönderir, bir örneğini de Cumhurbaşkanlığına iletir. Diğer merkezî yönetim idareleri tekliflerini Cumhurbaşkanlığına sunar; bütçeyi Cumhurbaşkanlığı hazırlayıp TBMM'ye sunar.",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 18',
    ),
    # düzey 2
    '0028': patch(
        'Merkezî yönetim bütçe kanununda öngörülmeyen hizmetler veya ödenek yetersizliği için konulan yedek ödeneğe ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': "Genel bütçe ödeneklerinin %10'una kadar konulur; aktarma yetkisi TBMM'dedir",
            'B': "Genel bütçe ödeneklerinin %20'sine kadar konulur; aktarma yetkisi Cumhurbaşkanındadır",
            'C': "Genel bütçe ödeneklerinin %2'sine kadar konulur; aktarma yetkisi ilgili bakandadır",
            'D': "Genel bütçe ödeneklerinin %2'sine kadar konulur; aktarma yetkisi Cumhurbaşkanındadır",
            'E': "Genel bütçe ödeneklerinin binde 5'ine kadar konulur; aktarma yetkisi Sayıştaydadır",
        },
        'D',
        "5018 m. 23'e göre yedek ödenek **genel bütçe ödeneklerinin yüzde ikisine kadar** konulabilir ve bu ödenekten aktarma yapmaya **Cumhurbaşkanı** yetkilidir; yapılan aktarmaların dağılımı yılın bitimini izleyen 15 gün içinde ilan edilir. Binde beş sınırı örtülü ödeneğe aittir.",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 23',
    ),
    # düzey 3
    '0029': patch(
        "Bir kamu idaresi, bütçesinde yemek hizmeti için 4 milyon ₺ ödenek bulunan bir iş için, niteliği gereği mali yılla sınırlı tutulamadığından ertesi yıla geçen yüklenmeye girişmek istemektedir. 5018'e göre bu yüklenmenin sınırları aşağıdakilerden hangisidir?",
        {
            'A': 'En fazla 2 milyon ₺; izleyen yılın Mart ayını ve altı aylık süreyi aşmamak üzere',
            'B': 'En fazla 800 bin ₺; izleyen yılın Haziran ayını aşmamak üzere',
            'C': 'En fazla 2 milyon ₺; izleyen yılın Haziran ayını ve 12 ayı aşmamak üzere',
            'D': 'En fazla 1 milyon ₺; izleyen yılın Aralık ayını aşmamak üzere',
            'E': 'En fazla 4 milyon ₺; izleyen yılın sonunu aşmamak üzere',
        },
        'C',
        "5018 m. 27'ye göre sürekliliği bulunan ve mali yılla sınırlı tutulamayan işler (yemek hizmeti dahil) için, bütçedeki ödeneğin **yüzde ellisini**, izleyen yılın **Haziran** ayını geçmemek ve yüklenme süresi **on iki ayı** aşmamak üzere üst yönetici onayıyla ertesi yıla geçen yüklenmeye girişilebilir: 4 × %50 = 2 milyon ₺.",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 27',
    ),
    # düzey 2
    '0030': patch(
        'Ekonomik dalgalanmaların vergi gelirleri ve işsizlik ödemeleri üzerindeki otomatik etkileri ayıklanarak, ekonomi potansiyel düzeyinde üretim yapsaydı oluşacak bütçe dengesi aşağıdakilerden hangisidir?',
        {
            'A': 'Faiz dışı denge',
            'B': 'Yapısal bütçe dengesi',
            'C': 'Kamu kesimi borçlanma gereği',
            'D': 'Nakit bazlı denge',
            'E': 'Operasyonel denge',
        },
        'B',
        '**Yapısal (konjonktürden arındırılmış, tam istihdam) bütçe dengesi**, gerçekleşen dengeden konjonktürel bileşeni çıkarır. Durgunlukta vergi hasılatı düşüp transferler arttığı için gerçekleşen açık büyür; yapısal denge ise bu otomatik etkiden bağımsız olarak hükümetin bilinçli (ihtiyari) politika duruşunu gösterir.',
        'Kamu maliyesi teorisi: yapısal denge',
    ),
    # düzey 2
    '0031': patch(
        'Faiz oranlarının piyasada düştüğü bir dönemde hükümetin, yüksek faizli eski tahvillerini daha düşük faizli yeni tahvillerle değiştirmesi hangi işlemdir?',
        {
            'A': 'Moratoryum',
            'B': 'Konsolidasyon',
            'C': 'Monetizasyon',
            'D': 'Konversiyon',
            'E': 'Borç reddi',
        },
        'D',
        'Borcun faiz oranının değiştirilmesi **konversiyondur**; piyasa faizleri düştüğünde yüksek faizli borç düşük faizliyle değiştirilerek faiz yükü azaltılır. Konsolidasyon vadeyi uzatır, monetizasyon ise borcun merkez bankası kaynağıyla (para basarak) finansmanıdır.',
        'Kamu maliyesi teorisi: kamu borçları',
    ),
    # düzey 3
    '0032': patch(
        'Marjinal tüketim eğiliminin 0,8 olduğu kapalı ve vergilerin götürü olduğu basit bir Keynesyen modelde, hükümet harcamaları 100 birim artırılıp aynı dönemde götürü vergiler de 100 birim artırılırsa denge milli gelir ne kadar değişir?',
        {
            'A': '400 birim azalır',
            'B': '100 birim artar',
            'C': 'Değişmez',
            'D': '500 birim artar',
            'E': '900 birim artar',
        },
        'B',
        "Harcama çarpanı 1 / (1 − 0,8) = 5, götürü vergi çarpanı −0,8 / (1 − 0,8) = −4'tür. Harcama artışının etkisi 5 × 100 = 500, vergi artışının etkisi −4 × 100 = −400; net etki **+100**. Bu sonuç **denk bütçe çarpanının 1** olduğunu gösterir (Haavelmo teoremi).",
        'Kamu maliyesi teorisi: çarpanlar',
    ),
    # düzey 2
    '0033': patch(
        'IS-LM modelinde borçlanmayla finanse edilen kamu harcaması artışının faiz oranını yükseltmesi sonucunda özel yatırımların azalmasına ne ad verilir ve bu etki hangi durumda ortaya çıkmaz?',
        {
            'A': 'Çarpan etkisi; yatırımlar faize duyarsızsa ortaya çıkmaz',
            'B': 'Dışlama etkisi; LM eğrisi dikeyse ve para talebi faize duyarsızsa ortaya çıkmaz',
            'C': 'İçleme etkisi; ekonomi tam istihdamdaysa ortaya çıkmaz',
            'D': 'İçleme etkisi; LM eğrisi dikeyse ortaya çıkmaz',
            'E': 'Dışlama etkisi; ekonomi likidite tuzağındaysa ortaya çıkmaz',
        },
        'E',
        'Kamu harcaması artışı gelir ve para talebini artırır, faiz yükselir ve faize duyarlı özel yatırımlar azalır: **dışlama etkisi**. LM yatay olduğunda (**likidite tuzağı**) faiz yükselmez ve dışlama oluşmaz; maliye politikası en etkili hâlindedir. LM dikey olduğunda ise dışlama tam olur ve maliye politikası etkisizleşir.',
        'Kamu maliyesi teorisi: dışlama etkisi',
    ),
    # düzey 2
    '0034': patch(
        'Durgunlukla mücadele eden bir ülkede ekonomi yönetimi aşağıdaki önlemleri açıklamıştır. Bunlardan hangisi maliye politikası değil, para politikası önlemidir?',
        {
            'A': 'Merkez bankasının zorunlu karşılık oranlarını düşürmesi',
            'B': 'İşverenlere sigorta primi desteğinin bütçeden karşılanması',
            'C': 'Kamu yatırım ödeneklerinin artırılması',
            'D': 'Düşük gelirli hanelere bütçeden nakit transfer yapılması',
            'E': 'Katma değer vergisi oranının geçici olarak indirilmesi',
        },
        'A',
        'Zorunlu karşılık oranları, açık piyasa işlemleri ve politika faizi merkez bankasının **para politikası** araçlarıdır. Kamu yatırım harcamaları, vergi oranları, transferler ve bütçeden karşılanan prim destekleri ise bütçe aracılığıyla uygulanan **maliye politikası** önlemleridir.',
        'Kamu maliyesi teorisi: maliye ve para politikası',
    ),
    # düzey 2
    '0035': patch(
        'Bütçe açığı, borç stoku veya harcama artışı gibi büyüklükler için kalıcı sayısal sınırlar koyarak hükümetin takdir yetkisini daraltan ve mali disiplini güçlendirmeyi amaçlayan düzenlemelere ne ad verilir?',
        {
            'A': 'Formül esnekliği',
            'B': 'Fonksiyonel maliye',
            'C': 'Otomatik stabilizatörler',
            'D': 'Ricardo denkliği',
            'E': 'Mali kurallar',
        },
        'E',
        '**Mali kurallar**, bütçe dengesi, borç, harcama veya gelir büyüklüklerine sayısal sınırlar koyan kalıcı düzenlemelerdir; seçim döngüsü ve açık eğilimi gibi kamu tercihi sorunlarına karşı mali disiplini güvenceye almayı amaçlar. Formül esnekliği ise önceden belirlenmiş göstergelere bağlı olarak vergi ve harcamaların otomatik ayarlanmasıdır.',
        'Kamu maliyesi teorisi: mali kurallar',
    ),
    # düzey 2
    '0036': patch(
        "Anayasa'nın 161. maddesine göre aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Bütçe kanununa bütçe ile ilgili hükümler dışında hüküm konulamaz.\n\nII. Merkezî yönetim bütçesiyle verilen ödenek, harcanabilecek tutarın sınırını gösterir.\n\nIII. Kesinhesap kanunu teklifi, yeni yıl bütçe kanunu teklifinden ayrı bir takvimle görüşülür.\n\nIV. Cari yıl ödenek artışı öngören tekliflerde öngörülen giderleri karşılayacak mali kaynak gösterilmesi zorunludur.",
        {
            'A': 'I, III ve IV',
            'B': 'I, II, III ve IV',
            'C': 'II ve III',
            'D': 'I, II ve IV',
            'E': 'I ve II',
        },
        'D',
        "Anayasa m. 161'e göre bütçe kanununa bütçe dışı hüküm konulamaz (I); ödenek harcanabilecek tutarın sınırıdır ve Cumhurbaşkanlığı kararnamesiyle aşılabileceğine dair hüküm konulamaz (II); cari yıl ödenek artışı öngören veya mali yük getiren tekliflerde kaynak gösterilmesi zorunludur (IV). Kesinhesap kanunu teklifi ise **yeni yıl bütçe kanunu teklifiyle birlikte** görüşülür ve karara bağlanır (III yanlış).",
        '2709 sayili T.C. Anayasasi m. 161',
    ),
    # düzey 2
    '0037': patch(
        'Bir hükümetin durgunluk döneminde bütçe açığını artırarak toplam talebi desteklemesi, bütçe anlayışı bakımından hangi yaklaşımı yansıtır?',
        {
            'A': 'Konjonktür dengeli bütçe anlayışı',
            'B': 'Gayrisafi bütçe anlayışı',
            'C': 'Yıllık denk bütçe kuralı',
            'D': 'Kalem bütçe anlayışı',
            'E': 'Her yıl denk bütçe öngören klasik anlayış',
        },
        'A',
        'Keynesyen **fonksiyonel / konjonktür dengeli** bütçe anlayışında denklik her yıl aranmaz; durgunlukta açık, genişlemede fazla verilerek bütçe konjonktür boyunca dengelenir ve istikrar aracı olarak kullanılır. Klasik anlayış ise her yıl denk bütçeyi savunur.',
        'Kamu maliyesi teorisi: bütçenin ekonomik etkileri',
    ),
    # düzey 1
    '0038': patch(
        'Bütçe döngüsünün aşamaları aşağıdakilerden hangisinde doğru sıralanmıştır?',
        {
            'A': 'Hazırlık – Denetim – Onay – Uygulama',
            'B': 'Onay – Hazırlık – Uygulama – Denetim',
            'C': 'Hazırlık – Görüşme ve onay – Uygulama – Denetim',
            'D': 'Denetim – Hazırlık – Onay – Uygulama',
            'E': 'Hazırlık – Uygulama – Görüşme ve onay – Denetim',
        },
        'C',
        'Bütçe döngüsü yürütme organının **hazırlığıyla** başlar, yasama organında **görüşülüp onaylanır**, yürütme tarafından **uygulanır** ve sonunda iç denetim, Sayıştay denetimi ve kesinhesap kanunuyla yasama **denetimi** yapılır. Önceden izin ilkesi gereği uygulama onaydan önce gelemez.',
        'Kamu maliyesi teorisi: bütçe süreci',
    ),
    # düzey 2
    '0039': patch(
        "Nominal değeri 1.000 ₺ olan, bir yıl vadeli ve kuponsuz bir hazine bonosu ihalede 800 ₺'ye satılmıştır. Bonoyu vadeye kadar elde tutan yatırımcının yıllık basit getiri oranı kaçtır?",
        {
            'A': '%125',
            'B': '%25',
            'C': '%12,5',
            'D': '%80',
            'E': '%20',
        },
        'B',
        "Yatırımcı bugün 800 ₺ öder, vadede 1.000 ₺ tahsil eder; kazanç 200 ₺'dir. Getiri, ödenen tutara göre hesaplanır: 200 / 800 = **%25**. %20, kazancın yanlışlıkla nominal değere (1.000 ₺) bölünmesinin sonucudur. İskontolu satışta devletin ödediği fark (200 ₺) 5018 m. 3'e göre kamu gideridir.",
        'Kamu maliyesi teorisi: iskontolu borçlanma',
    ),
    # düzey 2
    '0040': patch(
        "5018 sayılı Kanun'a göre genel yönetim kapsamındaki idarelerin bütçelerine ilişkin aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Genel bütçe Devlet tüzel kişiliğine dahil idarelerin bütçesidir',
            'B': 'Sosyal güvenlik kurumu bütçeleri (IV) sayılı cetvelde yer alan idarelerin bütçeleridir',
            'C': 'Merkezî yönetim bütçesi, sosyal güvenlik kurumları ve mahallî idareler bütçeleri olarak hazırlanır',
            'D': 'Kamu idareleri ihtiyaç hâlinde bunlar dışında ayrı adlarla bütçe oluşturabilir',
            'E': 'Mahallî idare bütçesi belediye ve il özel idareleri gibi idarelerin bütçesidir',
        },
        'D',
        "5018 m. 12'ye göre genel yönetim kapsamındaki idarelerin bütçeleri merkezî yönetim, sosyal güvenlik kurumları ve mahallî idareler bütçeleri olarak hazırlanır ve **kamu idarelerince bunlar dışında herhangi bir ad altında bütçe oluşturulamaz**. Diğer ifadeler maddedeki tanımlardır.",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 12',
    ),
    # düzey 2
    '0041': patch(
        'Bir bakanlığın kendi hizmetinden elde ettiği gelirin, yalnız o bakanlığın personel giderlerinin karşılanmasında kullanılmak üzere ayrılması hangi bütçe ilkesine aykırıdır?',
        {
            'A': 'Açıklık ilkesi',
            'B': 'Ademi tahsis ilkesi',
            'C': 'Doğruluk (samimiyet) ilkesi',
            'D': 'Önceden izin ilkesi',
            'E': 'Yıllık olma ilkesi',
        },
        'B',
        "**Ademi tahsis** ilkesine göre belirli gelirler belirli giderlere bağlanmaz; bütün gelirler bir havuzda toplanır ve bütün giderler bu havuzdan karşılanır. 5018 m. 13/g bu ilkeyi 'belirli gelirlerin belirli giderlere tahsis edilmemesi esastır' diye düzenler. Önceden izin ilkesi ise bütçenin yıl başlamadan onaylanmasını gerektirir.",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 13/g',
    ),
    # düzey 2
    '0042': patch(
        'Her yıl bütün harcama kalemlerinin geçmiş yıl ödeneği esas alınmadan baştan gerekçelendirilmesini ve karar paketleri hâlinde önceliklendirilmesini öngören bütçe sistemi hangisidir?',
        {
            'A': 'Sıfır tabanlı bütçe',
            'B': 'Planlama-programlama-bütçeleme sistemi',
            'C': 'Artımsal bütçe',
            'D': 'Performans esaslı bütçe',
            'E': 'Klasik (kalem) bütçe',
        },
        'A',
        '**Sıfır tabanlı bütçede** önceki yılın ödeneği kazanılmış hak sayılmaz; her faaliyet karar paketleri hâlinde sıfırdan gerekçelendirilip sıralanır. Artımsal (kalem) bütçede ise geçmiş yıl ödeneği temel alınıp üzerine artış eklenir; performans esaslı bütçe çıktı ve sonuçları ödenekle ilişkilendirir.',
        'Kamu maliyesi teorisi: bütçe sistemleri',
    ),
    # düzey 2
    '0043': patch(
        "5018 sayılı Kanun'a göre merkezî yönetim bütçesinin kapsamına ilişkin aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Devlet tüzel kişiliğine dahil idarelerin bütçeleriyle sınırlıdır',
            'B': 'Merkezî yönetim idareleri ile sosyal güvenlik ve mahallî idare bütçelerinden oluşur',
            'C': 'Genel bütçe ve mahallî idare bütçelerinden oluşur',
            'D': 'Genel bütçe, özel bütçe ve sosyal güvenlik kurumu bütçelerinden oluşur',
            'E': 'Genel bütçe, özel bütçe ve düzenleyici-denetleyici kurum bütçelerinden oluşur',
        },
        'E',
        "5018 m. 12'ye göre merkezî yönetim bütçesi (I) sayılı cetveldeki **genel bütçeli**, (II) sayılı cetveldeki **özel bütçeli** ve (III) sayılı cetveldeki **düzenleyici ve denetleyici** kurumların bütçelerinden oluşur. Sosyal güvenlik kurumları (IV) ve mahallî idareler ise merkezî yönetimle birlikte **genel yönetim** kapsamını oluşturur.",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 3, m. 12, ekli cetveller',
    ),
    # düzey 1
    '0044': patch(
        "5018 sayılı Kanun'a göre (I) sayılı cetvelde yer alan genel bütçeli idarelerin tüm gelirlerinin Hazine veznelerine girmesi, giderlerin bu veznelerden ödenmesi ve bu idarelerin özel vezne açamaması hangi ilkenin gereğidir?",
        {
            'A': 'Hesap verme sorumluluğu',
            'B': 'Gayrisafilik',
            'C': 'Hazine birliği',
            'D': 'Mali saydamlık',
            'E': 'Ademi tahsis',
        },
        'C',
        '5018 m. 6, merkezî yönetim kapsamındaki idarelerin gelir, gider, tahsilat, ödeme, nakit planlaması ve borç yönetiminin **Hazine birliğini** sağlayacak biçimde yürütülmesini öngörür; genel bütçeli idareler özel vezne açamaz. Mali saydamlık kamuoyunun zamanında bilgilendirilmesini, hesap verme sorumluluğu ise kaynak kullananların hesap vermesini ifade eder.',
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 6',
    ),
    # düzey 3
    '0045': patch(
        "5018 sayılı Kanun'a göre aşağıdaki bütçe hazırlık adımlarının kanuni son tarihlerine göre sıralaması hangisinde doğru verilmiştir?\n\nI. Kamu idarelerinin bütçe tekliflerini Cumhurbaşkanlığına göndermesi\n\nII. Orta vadeli programın Resmî Gazete'de yayımlanması\n\nIII. Bütçe Çağrısı ve Bütçe Hazırlama Rehberinin yayımlanması\n\nIV. Bütçe kanun teklifinin TBMM'ye sunulması",
        {
            'A': 'II – III – IV – I',
            'B': 'II – III – I – IV',
            'C': 'II – I – III – IV',
            'D': 'III – II – I – IV',
            'E': 'I – II – III – IV',
        },
        'B',
        "Orta vadeli program en geç **Eylül'ün ilk haftası sonuna** kadar (m. 16/2), Bütçe Çağrısı ve Bütçe Hazırlama Rehberi en geç **15 Eylül'e** kadar (m. 16/4) yayımlanır; kamu idareleri tekliflerini en geç **Eylül sonuna** kadar Cumhurbaşkanlığına gönderir (m. 17); teklif mali yılbaşından en az **75 gün önce** TBMM'ye sunulur (m. 18).",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 16-18',
    ),
    # düzey 2
    '0046': patch(
        "Anayasa'nın 161. maddesine göre bütçenin TBMM'de görüşülmesine ilişkin aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Kamu idare bütçeleri ile değişiklik önergeleri ayrıca görüşülmeden okunup oylanır',
            'B': 'Milletvekilleri Genel Kurulda gider artırıcı önergeler verebilir',
            'C': 'Genel Kurul bütçeyi mali yılbaşına kadar karara bağlar',
            'D': 'Teklif önce Bütçe Komisyonunda görüşülür',
            'E': 'Komisyonun elli beş gün içinde kabul ettiği metin Genel Kurulda görüşülür',
        },
        'B',
        "Anayasa m. 161'e göre TBMM üyeleri Genel Kurulda kamu idare bütçeleri hakkındaki düşüncelerini açıklar, ancak **gider artırıcı veya gelir azaltıcı önerilerde bulunamazlar**. Teklif Bütçe Komisyonunda görüşülür, Komisyonun 55 gün içinde kabul ettiği metin Genel Kurulda mali yılbaşına kadar karara bağlanır.",
        '2709 sayili T.C. Anayasasi m. 161',
    ),
    # düzey 1
    '0047': patch(
        "5018 sayılı Kanun'a göre kamu yatırım programı, merkezî yönetim bütçe kanununun yürürlüğe girdiği tarihten itibaren kaç gün içinde Cumhurbaşkanı kararıyla Resmî Gazete'de yayımlanır?",
        {
            'A': '60',
            'B': '30',
            'C': '7',
            'D': '45',
            'E': '15',
        },
        'E',
        "5018 m. 19/2'ye göre kamu yatırım programı, bütçe kanununa uygun olarak ve bu kanunun yürürlüğe girdiği tarihten itibaren **on beş gün** içinde Cumhurbaşkanı kararıyla Resmî Gazete'de yayımlanır.",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 19',
    ),
    # düzey 2
    '0048': patch(
        "Bir genel müdürlük, bütçesindeki 'mal ve hizmet alım giderleri' tertibinde 10 milyon ₺ ödenek bulunan bir kaleme, kendi bütçesi içindeki başka tertiplerden ödenek aktarmak istemektedir. İdarenin kendi yetkisiyle bu tertibe en fazla ne kadar aktarma yapabilir?",
        {
            'A': 'Kurum içi aktarma da kanunla yapılır',
            'B': '10 milyon ₺',
            'C': '2 milyon ₺',
            'D': '1 milyon ₺',
            'E': '5 milyon ₺',
        },
        'C',
        "5018 m. 21'e göre merkezî yönetim kapsamındaki idareler, **aktarma yapılacak tertipteki ödeneğin yüzde yirmisine kadar** kendi bütçeleri içinde aktarma yapabilir: 10 × %20 = 2 milyon ₺. Kurumlar **arası** aktarmalar ise kanunla yapılır (bütçe kanununda genel bütçe ödeneklerinin %10'unu geçmemek üzere yetki verilebilir).",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 21',
    ),
    # düzey 2
    '0049': patch(
        "5018 sayılı Kanun'a göre örtülü ödeneğe ilişkin aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Cumhurbaşkanlığı bütçesine konulur',
            'B': 'Toplamı genel bütçe başlangıç ödeneklerinin binde beşini geçemez',
            'C': 'Kapalı istihbarat ve kapalı savunma hizmetleri için kullanılabilir',
            'D': 'Siyasi partilerin seçim ihtiyaçları için kullanılabilir',
            'E': 'Kullanım esasları Cumhurbaşkanınca belirlenir',
        },
        'D',
        "5018 m. 24'e göre örtülü ödenek Cumhurbaşkanlığı bütçesine konulur; toplamı genel bütçe başlangıç ödeneklerinin **binde beşini** geçemez ve kapalı istihbarat, kapalı savunma, Devletin yüksek menfaatleri gibi amaçlarla kullanılır. Cumhurbaşkanının ve ailesinin kişisel harcamaları ile **siyasi partilerin** idare, propaganda ve seçim ihtiyaçları için **kullanılamaz**.",
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 24',
    ),
    # düzey 2
    '0050': patch(
        'Bütçe dengesinden faiz ödemelerinin çıkarılmasıyla elde edilen ve hükümetin mevcut dönemdeki maliye politikası duruşunu geçmiş borçların yükünden arındırarak gösteren ölçü hangisidir?',
        {
            'A': 'Operasyonel denge',
            'B': 'Cari denge',
            'C': 'Faiz dışı (birincil) denge',
            'D': 'Kamu kesimi borçlanma gereği',
            'E': 'Yapısal (tam istihdam) dengesi',
        },
        'C',
        '**Faiz dışı (birincil) denge**, gelirler ile faiz dışı harcamalar arasındaki farktır; geçmiş borçlanma kararlarından kaynaklanan faiz yükünü dışarıda bıraktığı için mevcut politikanın sürdürülebilirliğini değerlendirmede kullanılır. Operasyonel denge faizin yalnız enflasyon bileşenini ayıklar.',
        'Kamu maliyesi teorisi: bütçe açığı ölçüleri',
    ),
    # düzey 3
    '0051': patch(
        "Borç stokunun GSYH'ye oranı %50, borcun reel faiz oranı %10, reel büyüme oranı %6 olan bir ekonomide borç/GSYH oranının sabit kalması için yaklaşık olarak GSYH'nin yüzde kaçı kadar faiz dışı fazla verilmelidir?",
        {
            'A': '%4',
            'B': '%0',
            'C': '%2',
            'D': '%8',
            'E': '%5',
        },
        'C',
        'Borç dinamiği yaklaşık olarak Δb ≈ (r − g) × b − s biçiminde yazılır (b: borç/GSYH, s: faiz dışı fazla/GSYH). Oranın sabit kalması için s ≈ (0,10 − 0,06) × 0,50 = **%2**. Faiz oranı büyüme oranını aştığı sürece borç oranını sabit tutmak faiz dışı fazla gerektirir; r = g olsaydı faiz dışı dengenin sıfır olması yeterdi.',
        'Kamu maliyesi teorisi: borç dinamiği',
    ),
    # düzey 2
    '0052': patch(
        'Basit Keynesyen modelde hükümet harcama çarpanının götürü vergi çarpanından (mutlak değerce) büyük olmasının nedeni aşağıdakilerden hangisidir?',
        {
            'A': 'Vergi indiriminin marjinal tüketim eğilimini sıfıra indirmesi',
            'B': 'Vergilerin yatırımları, harcamaların ise tüketimi etkilemesi',
            'C': 'Harcamaların faiz oranını düşürerek yatırımı artırması',
            'D': 'Vergi indiriminin tamamının ithalata yönelmesi',
            'E': 'Vergi indiriminin bir kısmının tasarrufa gitmesi, harcamanın ise tamamının ilk turda talep olması',
        },
        'E',
        "Hükümet harcaması ilk turda doğrudan toplam talebe eklenir. Vergi indirimi ise önce hanehalkının harcanabilir gelirini artırır; bunun ancak marjinal tüketim eğilimi kadarı (ör. %80'i) harcamaya dönüşür, kalanı tasarruf edilir. Bu nedenle vergi çarpanı −c / (1 − c), harcama çarpanı 1 / (1 − c) olur ve harcama çarpanı daha büyüktür.",
        'Kamu maliyesi teorisi: çarpanlar',
    ),
    # düzey 2
    '0053': patch(
        'Otomatik stabilizatörlerin ihtiyari maliye politikasına göre en önemli üstünlüğü, aşağıdaki gecikmelerden hangilerini ortadan kaldırmasıdır?\n\nI. Tanıma gecikmesi\n\nII. Karar (yönetsel) gecikmesi\n\nIII. Etki (dış) gecikmesi',
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'I, II ve III',
            'D': 'Yalnız III',
            'E': 'II ve III',
        },
        'A',
        'Otomatik stabilizatörler yeni bir karar gerektirmediği için sorunun fark edilmesi (**tanıma**) ve politika kararının alınıp yasalaşması (**karar**) gecikmelerini ortadan kaldırır. Ancak politika uygulandıktan sonra ekonomide etkisini göstermesi için geçen **etki (dış) gecikmesi** devam eder.',
        'Kamu maliyesi teorisi: politika gecikmeleri',
    ),
    # düzey 2
    '0054': patch(
        'Enflasyon ile işsizliğin birlikte yükseldiği bir ekonomide talep yönlü maliye politikasının sınırlılığına ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Maliye politikası stagflasyonda enflasyonu etkilemez',
            'B': 'Talebi genişletmek enflasyonu, daraltmak işsizliği artırma riski taşır',
            'C': 'Daraltıcı politika iki sorunu birlikte çözer',
            'D': 'Stagflasyon toplam talep fazlasından kaynaklandığı için daraltma yeterlidir',
            'E': 'Genişletici politika iki sorunu birlikte çözer',
        },
        'B',
        '**Stagflasyon** çoğunlukla arz şoklarından (maliyet artışları) kaynaklanır. Toplam talebi genişletmek işsizliği azaltabilir ama enflasyonu artırır; daraltmak enflasyonu düşürebilir ama işsizliği artırır. Bu nedenle arz yönlü önlemler ve gelir (ücret-fiyat) politikaları gündeme gelir.',
        'Kamu maliyesi teorisi: stagflasyon',
    ),
    # düzey 2
    '0055': patch(
        'İşsizlik oranı belirli bir eşiği aştığında vergi oranlarının önceden kanunla belirlenen ölçüde kendiliğinden indirilmesini öngören yöntem aşağıdakilerden hangisidir?',
        {
            'A': 'İhtiyari maliye politikası',
            'B': 'Fonksiyonel maliye',
            'C': 'Otomatik stabilizatör',
            'D': 'Formül esnekliği',
            'E': 'Mali kural',
        },
        'D',
        '**Formül esnekliği**, ihtiyari politika ile otomatik stabilizatörler arasında yer alır: hangi göstergede hangi değişikliğin yapılacağı önceden kanunla belirlenir ve gösterge eşiği aştığında uygulama başlar. Otomatik stabilizatörler ise vergi ve transferlerin yapısı gereği sürekli işler; bir eşik ya da tetikleyici gerektirmez.',
        'Kamu maliyesi teorisi: formül esnekliği',
    ),
    # düzey 2
    '0056': patch(
        'IS-LM modelinde yatırımların faize duyarlılığının çok düşük olduğu durumda maliye politikasının etkinliği için aşağıdakilerden hangisi söylenebilir?',
        {
            'A': 'IS eğrisi yataylaşır, dışlama güçlenir ve maliye politikası etkisiz kalır',
            'B': 'IS eğrisi dikleşir, dışlama zayıflar ve maliye politikası etkili olur',
            'C': 'IS eğrisi dikleşir ve para politikası maliye politikasından daha etkili olur',
            'D': 'Faiz duyarlılığı maliye politikasının etkinliğini değiştirmez',
            'E': 'LM eğrisi dikleşir ve maliye politikası etkisiz kalır',
        },
        'B',
        'Yatırımlar faize duyarsızsa IS eğrisi **dikleşir**; kamu harcaması faizi yükseltse de özel yatırım pek azalmaz, yani dışlama zayıftır ve **maliye politikası etkilidir**. Aynı durumda para politikası, faizi düşürse bile yatırımı artıramadığı için etkisizleşir.',
        'Kamu maliyesi teorisi: maliye politikasının etkinliği',
    ),
    # düzey 2
    '0057': patch(
        'Kamu kesimi borçlanma gereğine (KKBG) ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Konjonktürel etkilerden arındırılmış yapısal açıktır',
            'B': 'Merkezî yönetim açığının enflasyonun faiz ödemelerindeki etkisinden arındırılmış hâlidir',
            'C': 'Faiz ödemelerini dışlayan bir faiz dışı denge ölçüsüdür',
            'D': 'Genel bütçeli idarelerin nakit açığıyla sınırlıdır',
            'E': "Mahallî idareler, sosyal güvenlik ve KİT'ler dahil geniş kamu kesiminin açığını kapsar",
        },
        'E',
        '**KKBG**, merkezî yönetim bütçesiyle sınırlı kalmaz; mahallî idareler, sosyal güvenlik kurumları, fonlar ve kamu iktisadi teşebbüslerini de içeren geniş kamu kesiminin toplam finansman ihtiyacını gösterir. Faiz dışı denge, operasyonel açık ve yapısal denge ise farklı açık ölçüleridir.',
        'Kamu maliyesi teorisi: kamu kesimi borçlanma gereği',
    ),
    # düzey 2
    '0058': patch(
        'Bütçe uygulamasının Sayıştay tarafından TBMM adına yapılan denetimi ve kesinhesap kanunuyla Meclisin bütçeyi fiilen uygulandığı biçimde onaylaması aşağıdakilerden hangisidir?',
        {
            'A': 'Dış (yasama ve yargısal) denetim',
            'B': 'Ön mali kontrol',
            'C': 'İç denetim',
            'D': 'Hiyerarşik denetim',
            'E': 'Performans programı değerlendirmesi',
        },
        'A',
        "Sayıştay'ın TBMM adına yaptığı denetim ve kesinhesap kanunuyla yasamanın bütçe uygulamasını onaylaması yürütme dışındaki organların yaptığı **dış denetimdir**. İç denetim ve ön mali kontrol ise idarelerin kendi bünyesinde yürütülen denetim ve kontrol faaliyetleridir.",
        'Kamu maliyesi teorisi: bütçe denetimi',
    ),
    # düzey 2
    '0059': patch(
        'Aşağıdakilerden hangisi bütçenin önceden izin ilkesiyle doğrudan ilişkilidir?',
        {
            'A': 'Tüm gelir ve giderlerin gayrisafi olarak bütçede gösterilmesi',
            'B': 'Bütçede tahmin edilen gelir ve gider toplamlarının denk tutulması',
            'C': 'Bütçenin ait olduğu yıl başlamadan onaylanmadıkça uygulanamaması',
            'D': 'Belirli gelirlerin belirli giderlere ayrılmaması',
            'E': 'Bütçeye bütçeyle ilgisi olmayan hükümlerin konulmaması',
        },
        'C',
        '**Önceden izin** ilkesine göre yürütme, yasamanın izni olmadan gelir toplayamaz ve harcama yapamaz; bu nedenle bütçe ait olduğu yıl başlamadan onaylanmalıdır (5018 m. 13/i). Gayrisafilik, ademi tahsis, denklik ve bütçeye ilgisiz hüküm konulmaması (Anayasa m. 161) ayrı ilkelerdir.',
        '5018 sayili Kamu Mali Yonetimi ve Kontrol Kanunu m. 13; 2709 sayili T.C. Anayasasi m. 161',
    ),
    # düzey 1
    '0060': patch(
        "Harcamaları amaçlara göre programlar ve alt programlar hâlinde gruplandıran ve planlama ile bütçeleme arasında bağ kuran, ABD'de 1960'larda savunma bütçesinde uygulanmaya başlanan sistem hangisidir?",
        {
            'A': 'Performans programı',
            'B': 'Klasik kalem bütçe',
            'C': 'Artımsal bütçe',
            'D': 'Planlama-programlama-bütçeleme sistemi',
            'E': 'Karar paketlerine dayalı sıfır tabanlı bütçe',
        },
        'D',
        "**Planlama-programlama-bütçeleme sistemi (PPBS)**, amaçların belirlenmesi, bu amaçlara ulaşacak programların seçilmesi ve kaynakların programlara göre tahsisini sistematik biçimde birleştirir; ABD Savunma Bakanlığında 1960'larda uygulanmış, sonra diğer idarelere yaygınlaştırılmıştır. Sıfır tabanlı bütçe 1970'lerde yaygınlaşmıştır.",
        'Kamu maliyesi teorisi: bütçe türleri',
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
    print(f"1 paket / {len(PATCHES)} soru ('Butce ve Maliye Politikasi' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
