#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Atatürk İlkeleri ve Dış Politika — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gerçek SGS 16-20 profiline göre baştan yazıldı. Eski pakette soruların yarısından çoğu ilke tanımıydı (gerçek sınavda payı %5) ve çeldiricilere eklenen açıklayıcı parantezler doğru şıkkı ele veriyordu. Yeni dağılım: ilkeler 18 (uygulama eşleştirme, öncüllü), dış politika 24 (Lozan'dan kalan sorunlar, Musul, mübadele ve etabli, yabancı okullar, borçlar, Boğazlar ve Montrö, Milletler Cemiyeti, Briand-Kellogg, Balkan Antantı, Sadabat, Hatay, Türk-Sovyet ve Türk-Yunan ilişkileri), iç politika, eserler ve ekonomi 18. Olumsuz kök yaklaşık %30.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: SGS Atatürk İlkeleri ve İnkılap Tarihi 2021-2026 kitapçıkları — biçim kalibrasyonu
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/ataturk_ilkeleri/ataturk_ilkeleri_dis_politika.json"
STYLE_REF = 'SGS Atatürk İlkeleri (gerçek sınav 16-20 profili)'
ONEK = "ait-ilke-gen-"


def patch(stem, options, answer, solution, ref='Atatürk İlkeleri ve İnkılap Tarihi'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Aşağıdaki ilkelerden hangisi, yapılan yeniliklerin korunmasını ve geliştirilerek sürdürülmesini öngörür?',
        {
            'A': 'Milliyetçilik',
            'B': 'İnkılapçılık',
            'C': 'Cumhuriyetçilik',
            'D': 'Halkçılık',
            'E': 'Devletçilik',
        },
        'B',
        'İnkılapçılık, gerçekleştirilen inkılapların korunmasını ve çağın gereklerine göre geliştirilmesini öngörür.',
    ),
    # düzey 2
    '0002': patch(
        'Türk karasularında taşımacılık hakkını Türk gemilerine veren Kabotaj Kanunu hangi yıl yürürlüğe girmiştir?',
        {
            'A': '1926',
            'B': '1923',
            'C': '1938',
            'D': '1933',
            'E': '1929',
        },
        'A',
        "Kabotaj Kanunu 1926'da yürürlüğe girmiş ve 1 Temmuz Denizcilik ve Kabotaj Bayramı olarak kutlanmaktadır.",
    ),
    # düzey 2
    '0003': patch(
        "Aşağıdakilerden hangisi Atatürk'ün kaleme aldığı eserlerden biri değildir?",
        {
            'A': 'Nutuk',
            'B': 'Çankaya',
            'C': 'Geometri',
            'D': 'Zabit ve Kumandan ile Hasbihal',
            'E': 'Vatandaş İçin Medeni Bilgiler',
        },
        'B',
        "Çankaya, Falih Rıfkı Atay'ın anı kitabıdır.",
    ),
    # düzey 3
    '0004': patch(
        "I. Halifeliğin kaldırılması\nII. Tekke ve zaviyelerin kapatılması\nIII. Kabotaj Kanunu'nun çıkarılması\nIV. 'Devletin dini İslam'dır' ibaresinin anayasadan çıkarılması\n\nYukarıdakilerden hangileri laiklik ilkesiyle ilgilidir?",
        {
            'A': 'I, II, III ve IV',
            'B': 'I, III ve IV',
            'C': 'I, II ve IV',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'C',
        'Halifeliğin kaldırılması, tekke ve zaviyelerin kapatılması ve devlet dinine ilişkin hükmün anayasadan çıkarılması laiklikle ilgilidir. Kabotaj Kanunu ekonomik bağımsızlıkla ilgilidir.',
    ),
    # düzey 2
    '0005': patch(
        'Devletçilik anlayışıyla hazırlanan Birinci Beş Yıllık Sanayi Planı hangi yıl uygulamaya konmuştur?',
        {
            'A': '1938',
            'B': '1946',
            'C': '1934',
            'D': '1929',
            'E': '1923',
        },
        'C',
        "Birinci Beş Yıllık Sanayi Planı 1934'te uygulamaya konmuş ve Sümerbank, Etibank gibi kuruluşlarla yürütülmüştür.",
    ),
    # düzey 2
    '0006': patch(
        "Cumhuriyetin ilk yıllarında çok partili hayata geçiş denemeleri yapılmış, bazı milletvekilleri Cumhuriyet Halk Fırkası'ndan ayrılarak yeni bir parti kurmuştur.\n\nCumhuriyet döneminde kurulan ilk muhalefet partisi aşağıdakilerden hangisidir?",
        {
            'A': 'Demokrat Parti',
            'B': 'Cumhuriyet Halk Fırkası',
            'C': 'Serbest Cumhuriyet Fırkası',
            'D': 'Ahali Cumhuriyet Fırkası',
            'E': 'Terakkiperver Cumhuriyet Fırkası',
        },
        'E',
        "1924'te kurulan Terakkiperver Cumhuriyet Fırkası, Cumhuriyet döneminin ilk muhalefet partisidir.",
    ),
    # düzey 3
    '0007': patch(
        "I. Cumhuriyetin ilanı\nII. Tekke ve zaviyelerin kapatılması\nIII. Serbest Cumhuriyet Fırkası'nın kurulması\n\nYukarıdakilerden hangileri cumhuriyetçilik ilkesiyle ilgilidir?",
        {
            'A': 'I ve III',
            'B': 'I, II ve III',
            'C': 'I ve II',
            'D': 'Yalnız I',
            'E': 'II ve III',
        },
        'A',
        'Cumhuriyetin ilanı yönetim biçimini, çok partili hayat denemesi olan Serbest Cumhuriyet Fırkası millî iradenin yönetime yansımasını ilgilendirir. Tekke ve zaviyelerin kapatılması laiklikle ilgilidir.',
    ),
    # düzey 2
    '0008': patch(
        "Fransa'nın Suriye'den çekilme kararı üzerine Hatay sorunu gündeme gelmiş ve 1938'de bağımsız Hatay Devleti kurulmuştu.\n\nHatay Meclisi Türkiye'ye katılma kararını hangi yıl almıştır?",
        {
            'A': '1936',
            'B': '1940',
            'C': '1937',
            'D': '1939',
            'E': '1938',
        },
        'D',
        "Hatay Devleti Meclisi 1939'da Türkiye'ye katılma kararı almıştır; bu, Atatürk'ün ölümünden sonra gerçekleşmiştir.",
    ),
    # düzey 2
    '0009': patch(
        "Balkan Antantı, 1934 yılında Balkan devletleri arasında imzalanan ve bölgedeki mevcut sınırların korunmasını amaçlayan bir ittifaktır.\n\nBalkan Antantı'nın kurulmasında aşağıdakilerden hangisi etkili olmuştur?",
        {
            'A': 'Musul sorununun çözülmesi',
            'B': "Sovyetler Birliği'nin dağılması",
            'C': "Hatay'ın Türkiye'ye katılması",
            'D': "II. Dünya Savaşı'nın sona ermesi",
            'E': "İtalya'nın yayılmacı politikası",
        },
        'E',
        "1930'larda İtalya'nın yayılmacı politikası Balkan devletlerini ortak güvenlik arayışına yöneltmiştir. Hatay'ın katılması (1939) Antant'tan sonradır.",
    ),
    # düzey 2
    '0010': patch(
        "Atatürk'ün 'Hayatta en hakiki mürşit ilimdir.' sözü aşağıdaki bütünleyici ilkelerden hangisiyle ilgilidir?",
        {
            'A': 'İnsan ve insanlık sevgisi',
            'B': 'Millî birlik ve beraberlik',
            'C': 'Millî egemenlik',
            'D': 'Akılcılık ve bilimsellik',
            'E': 'Yurtta sulh, cihanda sulh',
        },
        'D',
        'Söz, yol göstericinin bilim olduğunu vurgular; akılcılık ve bilimsellik ilkesiyle ilgilidir.',
    ),
    # düzey 3
    '0011': patch(
        "I. Balkan Antantı\nII. Varşova Paktı\nIII. Sadabat Paktı\n\nYukarıdakilerden hangileri Atatürk döneminde Türkiye'nin taraf olduğu antlaşmalardandır?",
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I ve III',
        },
        'E',
        "Balkan Antantı (1934) ve Sadabat Paktı (1937) Atatürk dönemindedir. Varşova Paktı 1955'te Sovyet bloku devletlerince kurulmuştur; Türkiye taraf değildir.",
    ),
    # düzey 2
    '0012': patch(
        'Aşağıdakilerden hangisi Atatürk dönemi Türk dış politikasında temel alınan ilkelerden biri değildir?',
        {
            'A': 'Uluslararası hukuka saygı',
            'B': 'Tam bağımsızlık',
            'C': 'Yayılmacılık',
            'D': 'Barışçılık',
            'E': 'Gerçekçilik',
        },
        'C',
        'Atatürk dönemi dış politikası barışçı, gerçekçi ve tam bağımsızlığı esas alan bir politikadır; yayılmacılık reddedilmiştir.',
    ),
    # düzey 3
    '0013': patch(
        "Serbest Cumhuriyet Fırkası'nın kendini feshetmesinden kısa süre sonra yaşanan ve çok partili hayata geçişin ertelenmesinde etkili olan olay aşağıdakilerden hangisidir?",
        {
            'A': 'Menemen Olayı',
            'B': 'Şeyh Sait Ayaklanması',
            'C': 'Ağrı Ayaklanması',
            'D': '31 Mart Vakası',
            'E': 'İzmir Suikast Girişimi',
        },
        'A',
        "Serbest Cumhuriyet Fırkası Kasım 1930'da kapandı; Aralık 1930'daki Menemen Olayı rejime yönelik tehdidin sürdüğünü göstererek çok partili hayatın ertelenmesinde etkili oldu.",
    ),
    # düzey 2
    '0014': patch(
        'Millî ekonominin esaslarının belirlendiği İzmir İktisat Kongresi hangi yıl toplanmıştır?',
        {
            'A': '1931',
            'B': '1923',
            'C': '1927',
            'D': '1924',
            'E': '1920',
        },
        'B',
        "İzmir İktisat Kongresi, Lozan görüşmeleri sürerken 1923'te toplanmıştır.",
    ),
    # düzey 2
    '0015': patch(
        "Aşağıdakilerden hangisi Lozan Barış Antlaşması'nda çözüme kavuşturulamayan sorunlardandır?",
        {
            'A': 'Azınlıkların statüsü',
            'B': 'Doğu Trakya sınırı',
            'C': 'Savaş tazminatı',
            'D': 'Musul sorunu',
            'E': 'Kapitülasyonlar',
        },
        'D',
        "Musul sorununun Türkiye ile İngiltere arasında ikili görüşmelerle çözülmesi kararlaştırılmıştı. Kapitülasyonlar kaldırılmış, savaş tazminatı ve Doğu Trakya sınırı Lozan'da çözülmüştür.",
    ),
    # düzey 2
    '0016': patch(
        "Türkiye ile Sovyetler Birliği arasında 1925'te imzalanan antlaşma aşağıdakilerden hangisidir?",
        {
            'A': 'Moskova Antlaşması',
            'B': 'Kars Antlaşması',
            'C': 'Sadabat Paktı',
            'D': 'Dostluk ve Tarafsızlık Antlaşması',
            'E': 'Balkan Antantı',
        },
        'D',
        '1925 Dostluk ve Tarafsızlık Antlaşması iki ülke ilişkilerini güçlendirmiştir. Moskova ve Kars antlaşmaları 1921 tarihlidir.',
    ),
    # düzey 2
    '0017': patch(
        "Aşağıdaki devletlerden hangisi Balkan Antantı'nı imzalayanlar arasında yer almaz?",
        {
            'A': 'Türkiye',
            'B': 'Yunanistan',
            'C': 'Bulgaristan',
            'D': 'Yugoslavya',
            'E': 'Romanya',
        },
        'C',
        "1934'te imzalanan Balkan Antantı'na Türkiye, Yunanistan, Yugoslavya ve Romanya katılmış; Bulgaristan katılmamıştır.",
    ),
    # düzey 2
    '0018': patch(
        "Lozan Antlaşması'yla Boğazlar uluslararası bir komisyonun denetimine bırakılmış ve bölge askerden arındırılmıştı. 1930'larda artan savaş tehlikesi, Türkiye'yi bu düzeni değiştirmek için girişimde bulunmaya yöneltti.\n\nMontrö Boğazlar Sözleşmesi ile ilgili aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Boğazlar bölgesinin silahlandırılmasına izin verilmiştir.',
            'B': 'Sözleşme 1936 yılında imzalanmıştır.',
            'C': "Boğazların yönetimi Türkiye'ye bırakılmıştır.",
            'D': "Boğazlar Komisyonu'nun yetkileri genişletilmiştir.",
            'E': 'Uluslararası Boğazlar Komisyonu kaldırılmıştır.',
        },
        'D',
        "Montrö ile Boğazlar Komisyonu kaldırılmış, yetkileri Türkiye'ye geçmiştir.",
    ),
    # düzey 2
    '0019': patch(
        "Lozan'da kabul edilen nüfus mübadelesinin dışında tutulan gruplar aşağıdakilerden hangisidir?",
        {
            'A': 'İstanbul Rumları ile Batı Trakya Türkleri',
            'B': 'Kapadokya Rumları ile Atina Türkleri',
            'C': 'Trabzon Rumları ile Makedonya Türkleri',
            'D': 'İzmir Rumları ile Selanik Türkleri',
            'E': 'Anadolu Rumları ile Girit Türkleri',
        },
        'A',
        "Lozan'da İstanbul'daki Rumlar ile Batı Trakya'daki Türkler mübadele dışında bırakılmıştır.",
    ),
    # düzey 2
    '0020': patch(
        "Atatürk'ün 1919-1927 yılları arasındaki olayları anlattığı ve 1927'de Cumhuriyet Halk Fırkası Kurultayı'nda okuduğu eser aşağıdakilerden hangisidir?",
        {
            'A': 'Nutuk',
            'B': 'Zabit ve Kumandan ile Hasbihal',
            'C': 'Geometri',
            'D': 'Vatandaş İçin Medeni Bilgiler',
            'E': 'Takımın Muharebe Talimi',
        },
        'A',
        "Nutuk, 1927'deki kurultayda okunmuş ve Millî Mücadele ile Cumhuriyet'in ilk yıllarını anlatır.",
    ),
    # düzey 2
    '0021': patch(
        'Atatürk milliyetçiliğiyle ilgili aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Dil, kültür ve ülkü birliğine dayanır.',
            'B': 'Irk birliğini esas alır.',
            'C': 'Başka milletlerin haklarına saygılıdır.',
            'D': 'Millî birlik ve beraberliği amaçlar.',
            'E': 'Akıl ve bilimi yol gösterici sayar.',
        },
        'B',
        'Atatürk milliyetçiliği ırkçılığa dayanmaz; ortak dil, kültür, tarih ve ülküye dayanan birleştirici bir anlayıştır.',
    ),
    # düzey 2
    '0022': patch(
        "1926 Ankara Antlaşması'na göre Musul petrol gelirlerinin yüzde onu Türkiye'ye kaç yıl süreyle verilecektir?",
        {
            'A': '10',
            'B': '15',
            'C': '25',
            'D': '50',
            'E': '99',
        },
        'C',
        "Antlaşmaya göre Musul petrollerinden elde edilecek gelirin %10'u 25 yıl süreyle Türkiye'ye ödenecekti.",
    ),
    # düzey 2
    '0023': patch(
        'Devletçilik politikasıyla sanayi yatırımlarını yürütmek üzere Sümerbank hangi yıl kurulmuştur?',
        {
            'A': '1925',
            'B': '1930',
            'C': '1933',
            'D': '1938',
            'E': '1935',
        },
        'C',
        "Sümerbank 1933'te kurulmuştur; Etibank 1935 tarihlidir.",
    ),
    # düzey 2
    '0024': patch(
        "Milletler Cemiyeti, I. Dünya Savaşı'ndan sonra uluslararası barışı korumak amacıyla kurulmuştu; Türkiye ise barışçı dış politikası doğrultusunda bu örgüte davet üzerine katıldı.\n\nTürkiye Milletler Cemiyeti'ne hangi yıl üye olmuştur?",
        {
            'A': '1932',
            'B': '1923',
            'C': '1926',
            'D': '1945',
            'E': '1936',
        },
        'A',
        "Türkiye 1932'de Milletler Cemiyeti'ne üye olmuştur.",
    ),
    # düzey 2
    '0025': patch(
        'Aşağıdakilerden hangisi Atatürk ilkelerinin ortak özelliklerinden biri değildir?',
        {
            'A': 'Bağımsızlığı esas alması',
            'B': 'Akıl ve bilime dayanması',
            'C': 'Değişmez ve sorgulanamaz kurallara dayanması',
            'D': 'Millî tarih ve kültürden beslenmesi',
            'E': 'Birbirini tamamlayan bir bütün oluşturması',
        },
        'C',
        'Atatürk ilkeleri akla ve bilime dayanır; dogmatik değildir, gelişmeye açıktır.',
    ),
    # düzey 2
    '0026': patch(
        "Lozan Barış Konferansı'nda çözülemeyen Musul sorununun İngiltere ile ikili görüşmelerle çözülmesi kararlaştırılmış, sonuç alınamayınca konu Milletler Cemiyeti'ne götürülmüştü.\n\nMusul sorunu hangi antlaşmayla sonuçlanmıştır?",
        {
            'A': 'Mudanya Ateşkes Antlaşması',
            'B': 'Lozan Barış Antlaşması',
            'C': 'Montrö Boğazlar Sözleşmesi',
            'D': '1926 Ankara Antlaşması',
            'E': '1921 Ankara Antlaşması',
        },
        'D',
        "Musul, İngiltere ile imzalanan 1926 Ankara Antlaşması'yla Irak'a bırakılmıştır. 1921 Ankara Antlaşması Fransa ile imzalanmıştır.",
    ),
    # düzey 2
    '0027': patch(
        'Aşağıdakilerden hangisi devletçilik anlayışıyla kurulan kuruluşlardan biri değildir?',
        {
            'A': 'Türkiye Cumhuriyet Merkez Bankası',
            'B': 'Etibank',
            'C': 'Devlet Demiryolları',
            'D': 'Sümerbank',
            'E': 'Türkiye İş Bankası',
        },
        'E',
        "Türkiye İş Bankası 1924'te özel sermayeyle kurulmuştur. Sümerbank, Etibank, Merkez Bankası ve Devlet Demiryolları devletin ekonomideki öncülüğünün ürünüdür.",
    ),
    # düzey 2
    '0028': patch(
        'Laiklik ilkesi, halifeliğin kaldırılmasıyla başlayan bir süreç sonunda devletin temel niteliklerinden biri olarak anayasada da yer aldı.\n\nLaiklik ilkesi hangi yıl anayasaya girmiştir?',
        {
            'A': '1934',
            'B': '1924',
            'C': '1937',
            'D': '1928',
            'E': '1946',
        },
        'C',
        "1928'de devlet dinine ilişkin hüküm anayasadan çıkarılmış, laiklik ise diğer ilkelerle birlikte 1937'de anayasaya eklenmiştir.",
    ),
    # düzey 2
    '0029': patch(
        "Lozan Barış Antlaşması'nda Boğazlar için kabul edilen düzenleme aşağıdakilerden hangisidir?",
        {
            'A': 'Boğazların tamamen Türk egemenliğine bırakılması',
            'B': 'Başkanı Türk olan uluslararası bir komisyonun kurulması',
            'C': "Boğazların İngiltere'nin denetimine verilmesi",
            'D': 'Boğazların Yunanistan ile ortak yönetilmesi',
            'E': 'Boğazların savaş gemilerine sürekli kapatılması',
        },
        'B',
        "Lozan'da Boğazlar bölgesi silahsızlandırılmış ve başkanı Türk olan uluslararası bir Boğazlar Komisyonu kurulmuştur. Boğazlar 1936'da Montrö ile Türk egemenliğine geçmiştir.",
    ),
    # düzey 2
    '0030': patch(
        "Aşağıdakilerden hangisi Lozan'dan sonra çözülmesi gereken sorunlardan biri değildir?",
        {
            'A': 'Musul sorunu',
            'B': 'Yabancı okullar sorunu',
            'C': 'Kapitülasyonlar',
            'D': 'Osmanlı borçları',
            'E': 'Boğazlar sorunu',
        },
        'C',
        "Kapitülasyonlar Lozan'da tamamen kaldırılmıştır. Musul, yabancı okullar, borçların ödenmesi ve Boğazların yönetimi sonraki yıllarda çözülmüştür.",
    ),
    # düzey 3
    '0031': patch(
        'Aşağıdakilerden hangisi halifeliğin kaldırıldığı gün (3 Mart 1924) kabul edilen düzenlemelerden biri değildir?',
        {
            'A': "Şer'iye ve Evkaf Vekâleti'nin kaldırılması",
            'B': 'Tevhid-i Tedrisat Kanunu',
            'C': 'Şapka Kanunu',
            'D': "Erkân-ı Harbiye Vekâleti'nin kaldırılması",
            'E': 'Osmanlı hanedanının yurt dışına çıkarılması',
        },
        'C',
        "3 Mart 1924'te halifelikle birlikte Şer'iye ve Evkaf ile Erkân-ı Harbiye vekâletleri kaldırılmış, Tevhid-i Tedrisat Kanunu çıkarılmış ve hanedan yurt dışına çıkarılmıştır. Şapka Kanunu 1925 tarihlidir.",
    ),
    # düzey 2
    '0032': patch(
        "Devletçilik ilkesinin 1930'lu yıllarda ekonomi politikasına egemen olmasında aşağıdakilerden hangisi etkili olmuştur?",
        {
            'A': "II. Dünya Savaşı'nın sona ermesi",
            'B': 'Musul sorununun çözülmesi',
            'C': 'Marshall Planı yardımları',
            'D': "İzmir İktisat Kongresi'nde alınan kararlar",
            'E': '1929 Dünya Ekonomik Bunalımı',
        },
        'E',
        '1929 bunalımı ve özel sermayenin yetersizliği, devletin ekonomiye doğrudan katılmasını zorunlu kılmıştır. İzmir İktisat Kongresi (1923) özel girişimi öne çıkaran bir model benimsemişti; diğer seçenekler dönem dışıdır.',
    ),
    # düzey 3
    '0033': patch(
        "Aşağıdakilerden hangisi 1930'lu yıllarda gerçekleşen gelişmelerden biri değildir?",
        {
            'A': 'Montrö Boğazlar Sözleşmesi',
            'B': "Milletler Cemiyeti'ne üyelik",
            'C': 'Kadınlara milletvekili seçme hakkının tanınması',
            'D': "Türk Medeni Kanunu'nun kabulü",
            'E': "Soyadı Kanunu'nun çıkarılması",
        },
        'D',
        "Türk Medeni Kanunu 1926'da kabul edilmiştir. Diğerleri 1932-1936 yılları arasındadır.",
    ),
    # düzey 3
    '0034': patch(
        "I. Aşar vergisinin kaldırılması\nII. Soyadı Kanunu'nun çıkarılması\nIII. Kadınlara seçme ve seçilme hakkının tanınması\n\nYukarıdakilerden hangileri halkçılık ilkesiyle doğrudan ilgilidir?",
        {
            'A': 'I ve III',
            'B': 'I ve II',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'E',
        'Aşar vergisinin kaldırılması köylünün yükünü hafifletmiş, Soyadı Kanunu ayrıcalık bildiren lakapları ortadan kaldırmış, kadınlara siyasi haklar tanınması yurttaşlar arasında eşitliği sağlamıştır. Üçü de halkçılıkla ilgilidir.',
    ),
    # düzey 2
    '0035': patch(
        'Aşağıdakilerden hangisi milliyetçilik ilkesinin uygulamalarından biridir?',
        {
            'A': "Türk Medeni Kanunu'nun kabulü",
            'B': "Türk Tarih Kurumu'nun kurulması",
            'C': 'Halifeliğin kaldırılması',
            'D': "Tevhid-i Tedrisat Kanunu'nun çıkarılması",
            'E': 'Aşar vergisinin kaldırılması',
        },
        'B',
        "Türk tarihini bilimsel yöntemlerle araştırmak amacıyla Türk Tarih Kurumu'nun kurulması milliyetçilikle ilgilidir. Diğerleri laiklik ve halkçılık uygulamalarıdır.",
    ),
    # düzey 2
    '0036': patch(
        'Aşağıdakilerden hangisi cumhuriyetçilik ilkesinin doğrudan bir sonucu değildir?',
        {
            'A': 'Çok partili hayata geçiş denemeleri',
            'B': 'Saltanatın kaldırılması',
            'C': "Soyadı Kanunu'nun kabul edilmesi",
            'D': 'Cumhuriyetin ilan edilmesi',
            'E': "1924 Anayasası'nın kabul edilmesi",
        },
        'C',
        'Saltanatın kaldırılması, cumhuriyetin ilanı, 1924 Anayasası ve çok partili hayat denemeleri yönetim biçimiyle ilgilidir. Soyadı Kanunu toplumsal alanda eşitliği amaçlayan, halkçılıkla ilgili bir düzenlemedir.',
    ),
    # düzey 3
    '0037': patch(
        'Aşağıdaki gelişmelerden hangisi diğerlerinden önce gerçekleşmiştir?',
        {
            'A': "Şapka Kanunu'nun çıkarılması",
            'B': 'Kadınlara milletvekili seçme ve seçilme hakkının tanınması',
            'C': "Soyadı Kanunu'nun kabulü",
            'D': 'Halifeliğin kaldırılması',
            'E': 'Harf İnkılabı',
        },
        'D',
        "Halifelik 1924'te kaldırılmıştır. Şapka Kanunu 1925, Harf İnkılabı 1928, Soyadı Kanunu ve kadınların milletvekili seçme hakkı 1934 tarihlidir.",
    ),
    # düzey 2
    '0038': patch(
        "Altı ilkenin tamamının ('altı ok') Cumhuriyet Halk Fırkası programında yer alması hangi yıl gerçekleşmiştir?",
        {
            'A': '1931',
            'B': '1937',
            'C': '1923',
            'D': '1924',
            'E': '1927',
        },
        'A',
        "1931'deki kurultayda devletçilik ve inkılapçılık da programa eklenmiş, altı ilke birlikte yer almıştır. İlkeler 1937'de anayasaya girmiştir.",
    ),
    # düzey 2
    '0039': patch(
        "Kapitülasyonlar döneminde yabancı okullar Osmanlı Devleti'nin denetimi dışında kalmış, bazıları siyasi faaliyetlerin merkezi hâline gelmişti.\n\nLozan'dan sonra gündeme gelen yabancı okullar sorunu nasıl çözülmüştür?",
        {
            'A': 'Okullar uluslararası bir komisyona devredilmiştir.',
            'B': "Okullar Milletler Cemiyeti'nin denetimine bırakılmıştır.",
            'C': 'Okullar Türk kanunlarına ve denetimine bağlanmıştır.',
            'D': 'Okullara Türk eğitim sisteminden muafiyet tanınmıştır.',
            'E': 'Okulların tamamı kapatılmıştır.',
        },
        'C',
        'Yabancı okullar, Tevhid-i Tedrisat Kanunu ile Türk eğitim sisteminin ve Türk kanunlarının denetimine bağlanmıştır.',
    ),
    # düzey 2
    '0040': patch(
        'Mübadele dışında kalan İstanbul Rumlarından hangilerinin yerleşik (etabli) sayılacağı konusundaki anlaşmazlık aşağıdakilerden hangisiyle çözülmüştür?',
        {
            'A': 'Montrö Boğazlar Sözleşmesi',
            'B': 'Sadabat Paktı',
            'C': 'Mudanya Ateşkes Antlaşması',
            'D': '1930 Türk-Yunan Ankara Antlaşması',
            'E': 'Balkan Antantı',
        },
        'D',
        "Etabli sorunu, Türk-Yunan yakınlaşmasını başlatan 1930 Ankara Antlaşması'yla çözülmüştür.",
    ),
    # düzey 2
    '0041': patch(
        "Türkiye ile Yunanistan arasında 1930'da imzalanan Ankara Antlaşması'nın sonucu aşağıdakilerden hangisidir?",
        {
            'A': "Boğazlar Komisyonu'nun kaldırılması",
            'B': 'Musul sorununun çözülmesi',
            'C': "Batı Trakya'nın Türkiye'ye katılması",
            'D': 'İki ülke arasında dostluk ve iş birliği döneminin başlaması',
            'E': 'Nüfus mübadelesinin başlaması',
        },
        'D',
        "1930 Ankara Antlaşması mübadele sorunlarını çözerek Türk-Yunan yakınlaşmasını başlatmıştır. Mübadele 1923'te başlamış, Boğazlar Komisyonu 1936'da kaldırılmıştır.",
    ),
    # düzey 3
    '0042': patch(
        "Musul sorununun Türkiye'nin aleyhine sonuçlanmasında etkili olan iç gelişme aşağıdakilerden hangisidir?",
        {
            'A': 'Menemen Olayı',
            'B': 'İzmir Suikast Girişimi',
            'C': 'Harf İnkılabı',
            'D': "Serbest Cumhuriyet Fırkası'nın kurulması",
            'E': 'Şeyh Sait Ayaklanması',
        },
        'E',
        "1925'teki Şeyh Sait Ayaklanması Türkiye'nin Musul konusundaki elini zayıflatmıştır. Menemen Olayı (1930) ve Serbest Cumhuriyet Fırkası (1930) sorunun çözümünden sonradır.",
    ),
    # düzey 3
    '0043': patch(
        "Montrö Boğazlar Sözleşmesi ile Türkiye'ye aşağıdaki haklardan hangisi tanınmıştır?",
        {
            'A': "Karadeniz'e kıyısı olmayan devletlerin savaş gemilerine sınırsız geçiş izni verebilme",
            'B': 'Savaş ya da savaş tehlikesi durumunda savaş gemilerinin geçişine karar verebilme',
            'C': "Uluslararası Boğazlar Komisyonu'nun başkanlığını üstlenebilme",
            'D': 'Boğazlardan geçen ticaret gemilerinden gümrük vergisi alabilme',
            'E': 'Boğazları barış zamanında ticaret gemilerine kapatabilme',
        },
        'B',
        'Montrö ile Türkiye, savaş ya da savaş tehlikesi hâlinde savaş gemilerinin geçişini düzenleme yetkisi kazanmıştır. Barışta ticaret gemilerinin geçişi serbesttir; Boğazlar Komisyonu ise kaldırılmıştır.',
    ),
    # düzey 3
    '0044': patch(
        'Hatay sorunuyla ilgili gelişmelerin kronolojik sıralaması aşağıdakilerden hangisidir?',
        {
            'A': "Fransa-Suriye Antlaşması → Hatay Devleti'nin kurulması → Hatay'ın Türkiye'ye katılması",
            'B': "Fransa-Suriye Antlaşması → Hatay'ın Türkiye'ye katılması → Hatay Devleti'nin kurulması",
            'C': "Hatay Devleti'nin kurulması → Fransa-Suriye Antlaşması → Hatay'ın Türkiye'ye katılması",
            'D': "Hatay'ın Türkiye'ye katılması → Hatay Devleti'nin kurulması → Fransa-Suriye Antlaşması",
            'E': "Hatay Devleti'nin kurulması → Hatay'ın Türkiye'ye katılması → Fransa-Suriye Antlaşması",
        },
        'A',
        "1936 Fransa-Suriye Antlaşması sorunu başlatmış, 1938'de Hatay Devleti kurulmuş, 1939'da Hatay Türkiye'ye katılmıştır.",
    ),
    # düzey 2
    '0045': patch(
        "29 Ekim 1923'te Cumhuriyetin ilan edilmesinin ardından Mustafa Kemal cumhurbaşkanı seçildi ve yeni hükümetin kurulması için çalışmalar başladı.\n\nCumhuriyet'in ilk başbakanı aşağıdakilerden hangisidir?",
        {
            'A': 'Refik Saydam',
            'B': 'Kâzım Karabekir',
            'C': 'Ali Fuat Cebesoy',
            'D': 'İsmet Paşa',
            'E': 'Celal Bayar',
        },
        'D',
        "Cumhuriyetin ilanından sonra kurulan ilk hükûmetin başbakanı İsmet (İnönü) Paşa'dır.",
    ),
    # düzey 2
    '0046': patch(
        "Rejime karşı bazı çevreler, Mustafa Kemal'in bir yurt gezisi sırasında ona yönelik bir suikast planı hazırladı; plan, uygulanmadan önce ortaya çıkarıldı.\n\nMustafa Kemal'e yönelik İzmir Suikast Girişimi hangi yıl ortaya çıkarılmıştır?",
        {
            'A': '1934',
            'B': '1925',
            'C': '1923',
            'D': '1926',
            'E': '1930',
        },
        'D',
        "İzmir Suikast Girişimi 1926'da ortaya çıkarılmıştır.",
    ),
    # düzey 2
    '0047': patch(
        "Atatürk'ün geometri terimlerini Türkçeleştirdiği ve 1936-1937 yıllarında yazdığı eser aşağıdakilerden hangisidir?",
        {
            'A': 'Zabit ve Kumandan ile Hasbihal',
            'B': 'Geometri',
            'C': 'Takımın Muharebe Talimi',
            'D': 'Nutuk',
            'E': 'Vatandaş İçin Medeni Bilgiler',
        },
        'B',
        'Geometri kitabında açı, üçgen, çap gibi terimler Türkçeleştirilmiştir.',
    ),
    # düzey 2
    '0048': patch(
        "Türkiye'nin 1929'da katıldığı ve savaşı ulusal politika aracı olmaktan çıkarmayı amaçlayan antlaşma aşağıdakilerden hangisidir?",
        {
            'A': 'Briand-Kellogg Paktı',
            'B': 'Montrö Boğazlar Sözleşmesi',
            'C': 'Balkan Antantı',
            'D': 'Sadabat Paktı',
            'E': 'Locarno Antlaşması',
        },
        'A',
        "Briand-Kellogg Paktı uyuşmazlıkların barışçı yollarla çözülmesini öngörür; Türkiye 1929'da katılmıştır.",
    ),
    # düzey 2
    '0049': patch(
        'Atatürk döneminde çok partili hayata geçiş denemelerinin başarısız olmasının nedenlerinden biri aşağıdakilerden hangisidir?',
        {
            'A': 'Yabancı devletlerin baskı yapması',
            'B': 'Halkın siyasete hiç ilgi göstermemesi',
            'C': 'Ekonomik kalkınmanın tamamlanmış olması',
            'D': 'Anayasanın parti kurmayı yasaklaması',
            'E': 'Muhalefet partilerinin rejim karşıtlarınca istismar edilmesi',
        },
        'E',
        'Terakkiperver ve Serbest Cumhuriyet fırkaları rejim karşıtlarının toplandığı odaklar hâline gelince kapanmıştır.',
    ),
    # düzey 2
    '0050': patch(
        "Lozan'da paylaştırılan Osmanlı borçlarından Türkiye'ye düşen bölümün son taksiti hangi yıl ödenmiştir?",
        {
            'A': '1946',
            'B': '1954',
            'C': '1960',
            'D': '1938',
            'E': '1929',
        },
        'B',
        "Borçların ilk taksiti 1929'da ödenmiş, son taksit 1954'te ödenerek borç kapatılmıştır.",
    ),
    # düzey 3
    '0051': patch(
        "Türk Medeni Kanunu, aile ve miras hukukunu dinî kurallardan ayırarak kadın ile erkeğe eşit haklar tanımıştır.\n\nTürk Medeni Kanunu'nun kabulü aşağıdaki ilkelerden hangisiyle en az ilgilidir?",
        {
            'A': 'Devletçilik',
            'B': 'Milliyetçilik',
            'C': 'İnkılapçılık',
            'D': 'Halkçılık',
            'E': 'Laiklik',
        },
        'A',
        'Medeni Kanun hukukun dinî kurallardan ayrılmasını (laiklik), kadın-erkek eşitliğini (halkçılık), çağdaşlaşmayı (inkılapçılık) ve hukuk birliğini sağlamıştır; ekonomik bir düzenleme olmadığından devletçilikle ilgisi en azdır.',
    ),
    # düzey 2
    '0052': patch(
        'Sanayi yatırımlarını özendirmek amacıyla çıkarılan Teşvik-i Sanayi Kanunu hangi yıl kabul edilmiştir?',
        {
            'A': '1933',
            'B': '1927',
            'C': '1929',
            'D': '1938',
            'E': '1923',
        },
        'B',
        "Teşvik-i Sanayi Kanunu 1927'de kabul edilmiştir.",
    ),
    # düzey 3
    '0053': patch(
        "1930'lu yıllarda uygulanan devletçilik politikasıyla ilgili aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Devlet sanayi yatırımlarına doğrudan katılmıştır.',
            'B': 'Özel sektörün ekonomideki faaliyetlerine son verilmiştir.',
            'C': 'Sanayileşme planlı biçimde yürütülmüştür.',
            'D': 'Dünya Ekonomik Bunalımı bu politikaya yönelişte etkili olmuştur.',
            'E': 'Kamu iktisadi kuruluşları açılmıştır.',
        },
        'B',
        'Devletçilik, özel girişimin yetersiz kaldığı alanlarda devletin ekonomiye katılmasıdır; özel sektörü ortadan kaldırmamıştır.',
    ),
    # düzey 3
    '0054': patch(
        '1924 Anayasası ile ilgili aşağıdakilerden hangisi söylenemez?',
        {
            'A': "1937'de Atatürk ilkeleri anayasaya eklenmiştir.",
            'B': 'Egemenliğin kayıtsız şartsız millete ait olduğunu belirtmiştir.',
            'C': "1928'de devletin dinine ilişkin hüküm metinden çıkarılmıştır.",
            'D': 'Cumhuriyet döneminin ilk anayasasıdır.',
            'E': 'İlk kabul edildiği hâliyle kadınlara seçme ve seçilme hakkı tanımıştır.',
        },
        'E',
        "Kadınlara milletvekili seçme ve seçilme hakkı 1934'teki değişiklikle tanınmıştır; anayasanın ilk metninde yoktur.",
    ),
    # düzey 2
    '0055': patch(
        'Aşağıdakilerden hangisi Atatürk döneminde ekonomik alanda gerçekleştirilenlerden biri değildir?',
        {
            'A': "Birinci Beş Yıllık Sanayi Planı'nın uygulanması",
            'B': "Marshall Planı'ndan yardım alınması",
            'C': 'Aşar vergisinin kaldırılması',
            'D': "Teşvik-i Sanayi Kanunu'nun çıkarılması",
            'E': 'Demiryollarının millîleştirilmesi',
        },
        'B',
        "Marshall Planı yardımları 1948'den sonradır. Diğerleri Atatürk döneminin ekonomik uygulamalarıdır.",
    ),
    # düzey 2
    '0056': patch(
        'Aşağıdakilerden hangisi Atatürk ilkelerini bütünleyen ilkelerden biri değildir?',
        {
            'A': 'Ümmetçilik',
            'B': 'Yurtta sulh, cihanda sulh',
            'C': 'Millî egemenlik',
            'D': 'Akılcılık ve bilimsellik',
            'E': 'Millî birlik ve beraberlik',
        },
        'A',
        "Ümmetçilik, Osmanlı Devleti'nin son döneminde savunulan bir fikir akımıdır. Diğerleri bütünleyici ilkelerdendir.",
    ),
    # düzey 2
    '0057': patch(
        "Hatay'ın Türkiye'ye katılmasının Türk dış politikası açısından önemi aşağıdakilerden hangisidir?",
        {
            'A': "Musul'un da Türkiye'ye katılmasının yolunu açması",
            'B': "Türkiye'nin Milletler Cemiyeti'nden ayrılmasına yol açması",
            'C': "Balkan Antantı'nın dağılmasına neden olması",
            'D': 'Fransa ile savaş hâline girilmesine neden olması',
            'E': 'Misak-ı Millî sınırları içindeki bir sorunun barışçı yollarla çözülmesi',
        },
        'E',
        "Hatay, Misak-ı Millî sınırları içinde olup savaşa başvurulmadan, diplomasi yoluyla Türkiye'ye katılmıştır.",
    ),
    # düzey 2
    '0058': patch(
        "Aşağıdaki devletlerden hangisi Sadabat Paktı'nı imzalayanlar arasında yer almaz?",
        {
            'A': 'Suriye',
            'B': 'İran',
            'C': 'Türkiye',
            'D': 'Irak',
            'E': 'Afganistan',
        },
        'A',
        "1937'de imzalanan Sadabat Paktı'na Türkiye, İran, Irak ve Afganistan katılmıştır.",
    ),
    # düzey 2
    '0059': patch(
        'Kurtuluş Savaşı boyunca millî mücadelenin merkezi olan Ankara, hem güvenli konumu hem de ulaşım imkânları nedeniyle yeni devletin yönetim merkezi olarak öne çıkıyordu.\n\nAnkara hangi tarihte yeni Türk devletinin başkenti olmuştur?',
        {
            'A': '3 Mart 1924',
            'B': '29 Ekim 1923',
            'C': '1 Kasım 1922',
            'D': '23 Nisan 1920',
            'E': '13 Ekim 1923',
        },
        'E',
        "Ankara, cumhuriyetin ilanından kısa süre önce, 13 Ekim 1923'te başkent ilan edilmiştir.",
    ),
    # düzey 2
    '0060': patch(
        'Halkçılık, toplumda kişiye, aileye ya da zümreye ayrıcalık tanınmamasını ve devlet yönetiminin halkın yararına işlemesini esas alır.\n\nAşağıdakilerden hangisi halkçılık ilkesinin amaçlarından biri değildir?',
        {
            'A': 'Sınıf ayrıcalıklarını ortadan kaldırmak',
            'B': 'Toplumsal dayanışmayı güçlendirmek',
            'C': 'Halkın yönetime katılmasını sağlamak',
            'D': 'Kanun önünde eşitliği sağlamak',
            'E': 'Ekonomide devletin öncülüğünü sağlamak',
        },
        'E',
        'Ekonomide devletin öncülüğü devletçilik ilkesinin konusudur.',
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
    print(f"1 paket / {len(PATCHES)} soru ('Atatürk İlkeleri ve Dış Politika' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
