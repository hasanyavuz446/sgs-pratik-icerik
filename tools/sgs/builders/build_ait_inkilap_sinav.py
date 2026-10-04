#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Atatürk İnkılapları — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Kör öğrenci %31'den düşürüldü: 15 soruda anlamsız ya da doğru şıkkı ele veren çeldiriciler ('Tarımı yasaklamak', 'Saltanatı geri getirmek') makul içerikle değiştirildi, şık içi parantezler kaldırıldı, mutlak dil ('tümüyle', 'yalnızca') çıkarıldı. Ezber düzeyindeki üç tarih sorusu ve ilk cumhurbaşkanı sorusu kronolojik sıralama ve olumsuz köklü sorulara çevrildi. Doğru şıkkı doğal olarak en uzun olan sorular bilerek değiştirilmedi (hepsini kısaltmak 'iki ucu ele' ipucu doğuruyor).

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
RELATIVE_PATH = "content/ataturk_ilkeleri/ataturk_inkilaplari.json"
STYLE_REF = 'SGS Atatürk İlkeleri (gerçek sınav 16-20 profili)'
ONEK = "ait-inkilap-gen-"


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
        'Aşağıdakilerden hangisi saltanatın kaldırılmasının sonuçlarından biri değildir?',
        {
            'A': 'İstanbul ile Ankara arasındaki ikili yönetimin sona ermesi',
            'B': 'Halifelik makamının kaldırılması',
            'C': 'Millî egemenliğin güçlenmesi',
            'D': "TBMM'nin tek meşru yönetim olması",
            'E': "Osmanlı Devleti'nin hukuken sona ermesi",
        },
        'B',
        "1 Kasım 1922'de saltanatın kaldırılmasıyla Osmanlı Devleti hukuken sona ermiş ve ikili yönetim bitmiştir. Halifelik ise ayrı bir kararla 3 Mart 1924'te kaldırılmıştır.",
    ),
    # düzey 2
    '0002': patch(
        'I. Saltanatın kaldırılması\nII. Cumhuriyetin ilanı\nIII. Halifeliğin kaldırılması\n\nYukarıdaki gelişmelerin kronolojik sıralaması aşağıdakilerden hangisidir?',
        {
            'A': 'I – II – III',
            'B': 'II – I – III',
            'C': 'II – III – I',
            'D': 'III – I – II',
            'E': 'I – III – II',
        },
        'A',
        "Saltanat 1 Kasım 1922'de kaldırılmış, Cumhuriyet 29 Ekim 1923'te ilan edilmiş, halifelik 3 Mart 1924'te kaldırılmıştır.",
    ),
    # düzey 2
    '0003': patch(
        'Halifeliğin kaldırılmasıyla ilgili aşağıdakilerden hangisi söylenemez?',
        {
            'A': '1924 yılında gerçekleşmiştir.',
            'B': 'Saltanatla aynı gün kaldırılmıştır.',
            'C': 'Osmanlı hanedanının yurt dışına çıkarılmasıyla aynı gün kararlaştırılmıştır.',
            'D': 'Laik devlet düzeni yolunda önemli bir adımdır.',
            'E': 'Tevhid-i Tedrisat Kanunu ile aynı gün kabul edilmiştir.',
        },
        'B',
        "Saltanat 1 Kasım 1922'de, halifelik 3 Mart 1924'te kaldırılmıştır. 3 Mart 1924'te hanedanın yurt dışına çıkarılması ve Tevhid-i Tedrisat Kanunu da kabul edilmiştir.",
    ),
    # düzey 2
    '0004': patch(
        "Ülkedeki bütün eğitim kurumlarını Millî Eğitim Bakanlığı'na bağlayan ve eğitimde birliği sağlayan kanun aşağıdakilerden hangisidir?",
        {
            'A': 'Teşvik-i Sanayi Kanunu',
            'B': 'Soyadı Kanunu',
            'C': 'Tevhid-i Tedrisat Kanunu',
            'D': 'Kabotaj Kanunu',
            'E': 'Türk Harflerinin Kabul ve Tatbiki Hakkında Kanun',
        },
        'C',
        "3 Mart 1924'te kabul edilen Tevhid-i Tedrisat (Öğretim Birliği) Kanunu ile tüm okullar tek çatı altında, Millî Eğitim Bakanlığı'na bağlanmıştır.",
    ),
    # düzey 2
    '0005': patch(
        "İsviçre'den alınarak 1926'da kabul edilen, aile ve kişi haklarını düzenleyen kanun aşağıdakilerden hangisidir?",
        {
            'A': 'Ticaret Kanunu',
            'B': 'İcra-İflas Kanunu',
            'C': 'Türk Medeni Kanunu',
            'D': 'Türk Ceza Kanunu',
            'E': 'Borçlar Kanunu',
        },
        'C',
        "1926'da İsviçre Medeni Kanunu örnek alınarak Türk Medeni Kanunu kabul edilmiştir. Bu kanun; evlilik, miras, kadın-erkek eşitliği gibi konularda çağdaş düzenlemeler getirmiştir.",
    ),
    # düzey 2
    '0006': patch(
        'Türk Medeni Kanunu ile kadınlara tanınan haklardan biri aşağıdakilerden hangisidir?',
        {
            'A': 'Belediye meclisine seçilme hakkı',
            'B': 'Milletvekili seçme hakkı',
            'C': 'Cumhurbaşkanı olma hakkı',
            'D': 'Muhtar olma hakkı',
            'E': 'Mirasta kadın-erkek eşitliği',
        },
        'E',
        'Medeni Kanun; resmî nikâh zorunluluğu, tek eşle evlilik, boşanmada eşitlik ve mirasta kadın-erkek eşitliği gibi haklar getirmiştir. Siyasi haklar ise ayrı düzenlemelerle verilmiştir.',
    ),
    # düzey 2
    '0007': patch(
        'Yeni Türk harfleri kabul edildikten sonra halka okuma yazma öğretmek amacıyla Millet Mektepleri açıldı.\n\nLatin alfabesine dayalı yeni Türk harfleri hangi yıl kabul edilmiştir?',
        {
            'A': '1928',
            'B': '1931',
            'C': '1926',
            'D': '1923',
            'E': '1934',
        },
        'A',
        "1 Kasım 1928'de yeni Türk harfleri (Latin alfabesi) kabul edilmiştir. Okuma-yazmayı yaygınlaştırmak amacıyla Millet Mektepleri açılmıştır.",
    ),
    # düzey 2
    '0008': patch(
        "Yeni harflerin öğretilmesi ve halkın okuryazar yapılması amacıyla 1928'de açılan kurum aşağıdakilerden hangisidir?",
        {
            'A': 'Darülfünun',
            'B': 'Sanat okulları',
            'C': 'Köy Enstitüleri',
            'D': 'Millet Mektepleri',
            'E': 'Halkevleri',
        },
        'D',
        'Harf İnkılabı\'nın ardından, yeni harfleri halka öğretmek için 1928\'de Millet Mektepleri açılmıştır. Atatürk, "Başöğretmen" olarak bu seferberliğe öncülük etmiştir.',
    ),
    # düzey 2
    '0009': patch(
        "Türk dilini araştırmak ve geliştirmek amacıyla 1932'de kurulan kurum aşağıdakilerden hangisidir?",
        {
            'A': 'Türk Tarih Kurumu',
            'B': 'Diyanet İşleri Başkanlığı',
            'C': 'Darülfünun',
            'D': 'Halkevleri',
            'E': 'Türk Dil Kurumu',
        },
        'E',
        "1932'de Türk Dili Tetkik Cemiyeti (sonradan Türk Dil Kurumu) kurulmuştur. Amaç, Türk dilini yabancı sözcüklerden arındırıp geliştirmektir.",
    ),
    # düzey 2
    '0010': patch(
        "Türk tarihini bilimsel yöntemlerle araştırmak amacıyla 1931'de kurulan kurum aşağıdakilerden hangisidir?",
        {
            'A': 'Köy Enstitüleri',
            'B': 'Türk Dil Kurumu',
            'C': 'Millet Mektepleri teşkilatı',
            'D': 'Türk Tarih Kurumu',
            'E': 'Halkevleri',
        },
        'D',
        "1931'de Türk Tarihi Tetkik Cemiyeti (Türk Tarih Kurumu) kurulmuştur. Amaç, Türk tarihini bilimsel temelde araştırmak ve millî bilinci güçlendirmektir.",
    ),
    # düzey 2
    '0011': patch(
        'Her Türk vatandaşının bir soyadı almasını zorunlu kılan Soyadı Kanunu hangi yıl kabul edilmiştir?',
        {
            'A': '1930',
            'B': '1925 yılı',
            'C': '1928',
            'D': '1926',
            'E': '1934',
        },
        'E',
        '1934\'te kabul edilen Soyadı Kanunu ile her vatandaşa soyadı alma zorunluluğu getirilmiştir. Aynı yıl TBMM, Mustafa Kemal\'e "Atatürk" soyadını vermiştir.',
    ),
    # düzey 2
    '0012': patch(
        'Şapka giyilmesi ve kılık-kıyafette çağdaşlaşmayı öngören Şapka Kanunu hangi yıl çıkarılmıştır?',
        {
            'A': '1930',
            'B': '1923',
            'C': '1925',
            'D': '1928',
            'E': '1934',
        },
        'C',
        "1925'te çıkarılan Şapka Kanunu ile kılık-kıyafette çağdaşlaşma amaçlanmıştır. Aynı dönemde tekke ve zaviyeler de kapatılmıştır.",
    ),
    # düzey 2
    '0013': patch(
        'Türk kadınlarına milletvekili seçme ve seçilme hakkının tanındığı yıl aşağıdakilerden hangisidir?',
        {
            'A': '1934',
            'B': '1926',
            'C': '1930',
            'D': '1923',
            'E': '1928',
        },
        'A',
        "Türk kadınlarına milletvekili seçme ve seçilme hakkı 1934'te tanınmıştır. Kadınlar, belediye seçimlerinde seçme-seçilme hakkını ise 1930'da elde etmişti.",
    ),
    # düzey 2
    '0014': patch(
        'Kadınların siyasal haklarını kazanması aşamalı bir süreç içinde gerçekleşti; önce yerel yönetimlerde, ardından muhtarlık ve milletvekilliği seçimlerinde haklar tanındı.\n\nTürk kadınlarına belediye seçimlerinde seçme ve seçilme hakkı hangi yıl tanınmıştır?',
        {
            'A': '1928',
            'B': '1930',
            'C': '1923',
            'D': '1926',
            'E': '1934',
        },
        'B',
        "Kadınlara belediye seçimlerinde seçme ve seçilme hakkı 1930'da tanınmıştır. Bu, siyasi haklar yolunda atılan ilk adımdır; genel seçme-seçilme hakkı 1934'te verilmiştir.",
    ),
    # düzey 2
    '0015': patch(
        'Türk kıyılarında yük ve yolcu taşıma hakkını yalnızca Türk gemilerine tanıyan kanun aşağıdakilerden hangisidir?',
        {
            'A': 'Şapka Kanunu',
            'B': 'Aşar Kanunu',
            'C': 'Teşvik-i Sanayi Kanunu',
            'D': 'Kabotaj Kanunu',
            'E': 'Soyadı Kanunu',
        },
        'D',
        "1926'da çıkarılan Kabotaj Kanunu ile Türk kara sularında taşımacılık hakkı Türk gemilerine verilmiştir. 1 Temmuz, Kabotaj (Denizcilik) Bayramı olarak kutlanır.",
    ),
    # düzey 2
    '0016': patch(
        'Yeni Türk Devleti\'nin ekonomik hedeflerinin belirlendiği, "Misak-ı İktisadi" kararlarının alındığı kongre aşağıdakilerden hangisidir?',
        {
            'A': 'Balıkesir Kongresi',
            'B': 'Sivas Kongresi',
            'C': 'Erzurum Kongresi',
            'D': 'İzmir İktisat Kongresi',
            'E': 'Lozan Konferansı',
        },
        'D',
        '1923\'te toplanan İzmir İktisat Kongresi\'nde millî ekonominin temel ilkeleri belirlenmiş, "Misak-ı İktisadi" (Ekonomik Ant) kararları alınmıştır.',
    ),
    # düzey 2
    '0017': patch(
        'Köylü üzerinde ağır bir yük oluşturan ve üründen alınan verginin kaldırılmasıyla ilgili düzenleme aşağıdakilerden hangisidir?',
        {
            'A': 'Teşvik-i Sanayi Kanunu',
            'B': "Tekâlif-i Milliye Emirleri'nin yayımlanması",
            'C': 'Aşar vergisinin kaldırılması',
            'D': 'Soyadı Kanunu',
            'E': 'Tevhid-i Tedrisat Kanunu',
        },
        'C',
        "1925'te köylünün en büyük yükü olan aşar (öşür) vergisi kaldırılmıştır. Bu, tarımsal üretimi ve köylünün refahını olumlu etkileyen önemli bir ekonomik adımdır.",
    ),
    # düzey 2
    '0018': patch(
        'Miladi takvim, uluslararası saat ve ölçü sistemine geçiş aşağıdaki inkılap alanlarından hangisiyle ilgilidir?',
        {
            'A': 'Siyasi alandaki inkılaplar',
            'B': 'Dinî alandaki inkılaplar',
            'C': 'Hukuk alanındaki inkılaplar',
            'D': 'Toplumsal alandaki inkılaplar',
            'E': 'Askerî alandaki inkılaplar',
        },
        'D',
        'Miladi takvimin, uluslararası saat, ölçü ve tartı sisteminin kabulü; günlük yaşamı ve toplumsal düzeni çağdaşlaştıran toplumsal alandaki inkılaplardandır.',
    ),
    # düzey 2
    '0019': patch(
        'Cumhuriyetin ilanıyla ilgili aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Halifelik makamı da aynı gün kaldırılmıştır.',
            'B': '1923 yılında gerçekleşmiştir.',
            'C': 'Mustafa Kemal ilk cumhurbaşkanı seçilmiştir.',
            'D': 'Devletin yönetim biçimi kesinlik kazanmıştır.',
            'E': 'Devlet başkanlığı sorunu çözülmüştür.',
        },
        'A',
        "Cumhuriyet 29 Ekim 1923'te ilan edilmiş, yönetim biçimi ve devlet başkanlığı sorunu çözülmüştür. Halifelik 1924'te kaldırılmıştır.",
    ),
    # düzey 2
    '0020': patch(
        "Teşkilat-ı Esasiye Kanunu, Kurtuluş Savaşı koşullarında 1921'de hazırlanmış bir olağanüstü dönem anayasasıydı; Cumhuriyetin ilanından sonra yeni ve kapsamlı bir anayasa gerekli görüldü.\n\nBuna göre Cumhuriyet döneminin ilk anayasası hangi yıl kabul edilmiştir?",
        {
            'A': '1924',
            'B': '1928',
            'C': '1921',
            'D': '1926',
            'E': '1923',
        },
        'A',
        "1924 Anayasası, Cumhuriyet döneminin ilk anayasasıdır ve 1961'e kadar yürürlükte kalmıştır. (1921 Teşkilat-ı Esasiye ise Kurtuluş Savaşı dönemine aittir.)",
    ),
    # düzey 2
    '0021': patch(
        'Cumhuriyet döneminde kurulan ilk siyasi parti aşağıdakilerden hangisidir?',
        {
            'A': 'Serbest Cumhuriyet Fırkası',
            'B': 'Cumhuriyet Halk Fırkası',
            'C': 'Demokrat Parti',
            'D': 'Terakkiperver Cumhuriyet Fırkası',
            'E': 'İttihat ve Terakki Fırkası',
        },
        'B',
        "Mustafa Kemal'in kurduğu Cumhuriyet Halk Fırkası (1923), Cumhuriyet döneminin ilk siyasi partisidir. Terakkiperver ve Serbest Fırka ise sonradan kurulan muhalefet partileridir.",
    ),
    # düzey 2
    '0022': patch(
        "Çok partili hayata geçiş denemesi olarak 1930'da kurulan ancak kısa süre sonra kapanan parti aşağıdakilerden hangisidir?",
        {
            'A': 'Demokrat Parti',
            'B': 'Cumhuriyet Halk Fırkası',
            'C': 'Serbest Cumhuriyet Fırkası',
            'D': 'İttihat ve Terakki',
            'E': 'Millet Partisi',
        },
        'C',
        "1930'da Fethi Okyar'ın kurduğu Serbest Cumhuriyet Fırkası, çok partili hayata geçiş denemesidir; ancak kısa süre sonra kendini feshetmiştir.",
    ),
    # düzey 2
    '0023': patch(
        "Şeyh Sait Ayaklanması'nın bastırılmasının ardından çıkarılan ve hükûmete geniş yetkiler veren kanun aşağıdakilerden hangisidir?",
        {
            'A': 'Kabotaj Kanunu',
            'B': 'Tevhid-i Tedrisat Kanunu',
            'C': 'Takrir-i Sükûn Kanunu',
            'D': 'Teşvik-i Sanayi Kanunu',
            'E': 'Soyadı Kanunu',
        },
        'C',
        "1925'teki Şeyh Sait Ayaklanması üzerine çıkarılan Takrir-i Sükûn (Huzurun Sağlanması) Kanunu, hükûmete olağanüstü yetkiler vermiştir. Terakkiperver Fırka da bu dönemde kapatılmıştır.",
    ),
    # düzey 2
    '0024': patch(
        "Saltanatın kaldırılmasından sonra da varlığını sürdüren halifelik makamı, yeni rejime karşı olanların umut bağladığı bir odak hâline gelmişti.\n\nBuna göre 3 Mart 1924'te halifeliğin kaldırılmasının temel amacı aşağıdakilerden hangisidir?",
        {
            'A': 'Laik devlet düzenine geçişin önünü açmak',
            'B': 'Saltanatı ve halifeliği tek makamda birleştirmek',
            'C': 'İslam ülkeleriyle siyasi ittifak kurmak',
            'D': 'Yabancı okulları denetim altına almak',
            'E': "Eğitimi Şer'iye Vekâleti'ne bağlamak",
        },
        'A',
        'Halifeliğin kaldırılması, din ile devlet işlerinin birbirinden ayrılmasını ve laik bir devlet düzenine geçişi sağlamaya yönelik bir adımdır.',
    ),
    # düzey 2
    '0025': patch(
        'Tekke, zaviye ve türbelerin kapatılmasıyla ilgili düzenlemenin temel amacı aşağıdakilerden hangisidir?',
        {
            'A': 'Kapatılan medreseleri yeniden açıp ülke genelinde yaygınlaştırmak',
            'B': 'Halifelik kurumunu güçlendirip dinî otoriteyi yönetimde egemen kılmak',
            'C': 'Akıl ve bilim dışı yolları önleyip toplumu çağdaşlaştırmak',
            'D': 'Toplumda yeni tarikatlar ve dinî cemaatler kurmayı özendirmek',
            'E': 'Kaldırılan saltanatı ve padişahlık makamını yeniden geri getirmek',
        },
        'C',
        "1925'te tekke, zaviye ve türbelerin kapatılması; akıl ve bilim dışı inanış-uygulamaların önüne geçerek toplumu çağdaşlaştırma amacı taşır.",
    ),
    # düzey 2
    '0026': patch(
        "Harf İnkılabı'nın (yeni Türk harflerinin kabulü) temel amacı aşağıdakilerden hangisidir?",
        {
            'A': 'Saltanatı geri getirmek',
            'B': 'Yabancı dil öğretimini yasaklamak',
            'C': 'Arapçayı resmî dil yapmak',
            'D': 'Okuryazarlığı yaygınlaştırıp eğitimi kolaylaştırmak',
            'E': 'Geleneksel medrese eğitimini yaygınlaştırıp güçlendirmek',
        },
        'D',
        'Latin esaslı yeni Türk harfleri, okuma-yazmayı kolaylaştırıp okuryazarlığı yaygınlaştırmak ve eğitimde çağdaşlaşmayı sağlamak amacıyla kabul edilmiştir.',
    ),
    # düzey 2
    '0027': patch(
        "Osmanlı Devleti'nde hukuk alanında şer'i ve örfi hukuk ile Batı'dan alınan kanunlar bir arada uygulanıyor, bu durum hukuk birliğinin sağlanmasını zorlaştırıyordu.\n\nAşağıdakilerden hangisi hukuk alanındaki inkılaplardan biridir?",
        {
            'A': 'Latin harflerinin kabulü',
            'B': "Şapka Kanunu'nun çıkarılması",
            'C': "Kabotaj Kanunu'nun çıkarılması",
            'D': 'Aşar vergisinin kaldırılması',
            'E': "Türk Medeni Kanunu'nun kabulü",
        },
        'E',
        "Türk Medeni Kanunu'nun kabulü hukuk alanındaki inkılaplardandır. Şapka Kanunu toplumsal, Latin harfleri eğitim-kültür, aşarın kaldırılması ise ekonomik alandaki inkılaptır.",
    ),
    # düzey 2
    '0028': patch(
        'Atatürk inkılapları siyasi, hukuki, eğitim-kültür, toplumsal ve ekonomik alanlarda gerçekleştirilmiş; siyasi alandaki düzenlemeler devletin yönetim biçimini ve egemenliğin kaynağını değiştirmeye yönelmiştir.\n\nAşağıdakilerden hangisi siyasi alandaki inkılaplardan biridir?',
        {
            'A': 'Ölçü ve tartıların değiştirilmesi',
            'B': 'Şapka Kanunu',
            'C': 'Saltanatın kaldırılması',
            'D': "Medeni Kanun'un kabulü",
            'E': 'Aşar vergisinin kaldırılması',
        },
        'C',
        'Saltanatın kaldırılması ve Cumhuriyetin ilanı gibi düzenlemeler siyasi (devlet yönetimiyle ilgili) inkılaplardandır. Diğer seçenekler hukuk, toplumsal ya da ekonomik alanla ilgilidir.',
    ),
    # düzey 2
    '0029': patch(
        'Cumhuriyetin ilk yıllarında ekonomi büyük ölçüde tarıma dayanıyor, sanayi ve ticaret alanında ulusal sermaye yetersiz kalıyordu.\n\nAşağıdakilerden hangisi ekonomik alandaki inkılaplardan biridir?',
        {
            'A': 'Halifeliğin kaldırılması',
            'B': "Teşvik-i Sanayi Kanunu'nun çıkarılması",
            'C': 'Tevhid-i Tedrisat Kanunu',
            'D': 'Kadınlara milletvekili seçme hakkının tanınması',
            'E': 'Soyadı Kanunu',
        },
        'B',
        'Sanayiyi özendirmek için çıkarılan Teşvik-i Sanayi Kanunu ekonomik bir inkılaptır. Diğerleri siyasi, eğitim ya da toplumsal alandaki inkılaplardır.',
    ),
    # düzey 2
    '0030': patch(
        "Osmanlı Devleti'nden kalan dış borçların ödenmesini denetleyen ve Lozan'da Türkiye lehine düzenlenen kurum aşağıdakilerden hangisidir?",
        {
            'A': 'Kabotaj İdaresi',
            'B': 'Teşvik-i Sanayi',
            'C': 'Düyun-u Umumiye',
            'D': 'Reji İdaresi',
            'E': 'Aşar İdaresi',
        },
        'C',
        "Düyun-u Umumiye (Genel Borçlar İdaresi), Osmanlı dış borçlarını yöneten kurumdur. Lozan'da bu borçların ödeme koşulları Türkiye lehine düzenlenmiştir.",
    ),
    # düzey 2
    '0031': patch(
        'Cumhuriyetin ilanıyla birlikte devletin yönetim biçimiyle ilgili aşağıdakilerden hangisi kesinleşmiştir?',
        {
            'A': 'Padişahın devlet başkanı olması',
            'B': 'Halifenin devleti yönetmesi',
            'C': 'Devlet başkanının cumhurbaşkanı olması',
            'D': 'Yönetimin bir kurula bırakılması',
            'E': 'Meclis başkanının padişah yetkilerini kullanması',
        },
        'C',
        'Cumhuriyetin ilanıyla devletin başında halkın seçtiği temsilcilerce belirlenen bir cumhurbaşkanının bulunması kesinleşmiştir. Böylece millî egemenliğe dayalı yönetim biçimi netleşmiştir.',
    ),
    # düzey 2
    '0032': patch(
        'Yükseköğretimde köklü bir yenilenmeyi ifade eden 1933 Üniversite Reformu ile hangi kurum yeniden yapılandırılmıştır?',
        {
            'A': 'Medreseler',
            'B': 'Yüksek Ziraat Enstitüsü',
            'C': 'Köy Enstitüleri',
            'D': 'Millet Mektepleri',
            'E': 'İstanbul Darülfünunu',
        },
        'E',
        "1933'teki üniversite reformu ile İstanbul Darülfünunu kapatılıp yerine çağdaş anlayışla İstanbul Üniversitesi kurulmuştur.",
    ),
    # düzey 2
    '0033': patch(
        'Mustafa Kemal\'e "Atatürk" soyadı hangi kanunun çıkmasının ardından verilmiştir?',
        {
            'A': 'Teşvik-i Sanayi Kanunu',
            'B': 'Şapka Kanunu',
            'C': 'Kabotaj Kanunu',
            'D': 'Soyadı Kanunu',
            'E': 'Tevhid-i Tedrisat Kanunu',
        },
        'D',
        '1934\'te Soyadı Kanunu\'nun çıkmasının ardından TBMM, Mustafa Kemal\'e "Atatürk" soyadını vermiştir. Bu soyadının başkasına verilmesi yasaklanmıştır.',
    ),
    # düzey 2
    '0034': patch(
        'Atatürk, eğitim ve kültür alanındaki düzenlemelerle toplumun okuryazarlık düzeyini yükseltmeyi ve millî kültürü güçlendirmeyi amaçlamıştır.\n\nAşağıdaki inkılaplardan hangisi eğitim ve kültür alanıyla ilgilidir?',
        {
            'A': 'Kabotaj Kanunu',
            'B': 'Saltanatın kaldırılması',
            'C': 'Cumhuriyetin ilanı',
            'D': 'Aşar vergisinin kaldırılması',
            'E': 'Latin harflerinin kabulü',
        },
        'E',
        "Latin harflerinin kabulü, Tevhid-i Tedrisat ve TDK-TTK'nın kurulması eğitim-kültür alanındaki inkılaplardandır. Diğer seçenekler siyasi ya da ekonomik alanla ilgilidir.",
    ),
    # düzey 2
    '0035': patch(
        "1937'de Türkiye Cumhuriyeti Anayasası'na girerek devletin niteliklerinden biri hâline gelen ilkeler aşağıdakilerden hangisidir?",
        {
            'A': 'Misak-ı Millî kararları',
            'B': 'Atatürk ilkeleri',
            'C': 'Sevr maddeleri',
            'D': 'Wilson ilkeleri',
            'E': 'Mondros maddeleri',
        },
        'B',
        "1937'de cumhuriyetçilik, milliyetçilik, halkçılık, devletçilik, laiklik ve inkılapçılık ilkeleri (altı ok) anayasaya girerek devletin temel nitelikleri arasına alınmıştır.",
    ),
    # düzey 3
    '0036': patch(
        'Devletin ekonomiye doğrudan yatırımlarla katıldığı, özel sektörün yetersiz kaldığı alanlarda kamu işletmelerinin kurulduğu ekonomi politikası aşağıdakilerden hangisidir?',
        {
            'A': 'Feodalizm',
            'B': 'Merkantilizm',
            'C': 'Devletçilik',
            'D': 'Liberalizm',
            'E': 'Kapitülasyon',
        },
        'C',
        'Devletçilik ilkesi doğrultusunda, özel sektörün gücünün yetmediği alanlarda devlet doğrudan yatırım yapmış; sümerbank, etibank gibi kamu işletmeleri kurulmuştur.',
    ),
    # düzey 2
    '0037': patch(
        "Cumhuriyetin ilk yıllarında ulusal sermayeyi güçlendirmek ve ekonomik kalkınmayı finanse etmek amacıyla millî bankalar kurulmasına önem verildi.\n\nAşağıdakilerden hangisi Atatürk Dönemi'nde kurulan bir bankadır?",
        {
            'A': 'Reji Bankası',
            'B': 'Galata Bankerleri',
            'C': 'Düyun-u Umumiye Bankası',
            'D': 'Türkiye İş Bankası',
            'E': 'Osmanlı Bankası',
        },
        'D',
        "1924'te kurulan Türkiye İş Bankası, millî ekonominin gelişmesine katkı sağlamak amacıyla Atatürk Dönemi'nde açılan ilk millî bankalardandır.",
    ),
    # düzey 2
    '0038': patch(
        "Cumhuriyet Dönemi'nde ölçü, tartı ve uzunluk birimlerinin uluslararası (metrik) sisteme geçirilmesi hangi amaca yöneliktir?",
        {
            'A': 'Ticaret ve günlük yaşamda çağdaş dünyayla uyum sağlamak',
            'B': 'Halktan alınan vergileri ve mali yükümlülükleri artırmak',
            'C': 'Kaldırılan saltanat düzenini ve padişahlığı yeniden geri getirmek',
            'D': 'Dış ticarette gümrük gelirlerini artırmak',
            'E': 'Arşın ve okka gibi eski ölçü birimlerini olduğu gibi korumak',
        },
        'A',
        'Metrik ölçü-tartı sistemine geçiş; ticarette ve günlük yaşamda karışıklığı önleyip uluslararası dünyayla uyum sağlamayı amaçlamıştır.',
    ),
    # düzey 2
    '0039': patch(
        'Türk kadınının siyasi haklara kavuşması hangi ilkenin uygulamalarına örnek gösterilir?',
        {
            'A': 'İnkılapçılık',
            'B': 'Devletçilik',
            'C': 'Halkçılık',
            'D': 'Laiklik',
            'E': 'Milliyetçilik',
        },
        'C',
        'Kadın-erkek eşitliğini ve toplumdaki her bireyin eşit haklara sahip olmasını savunan halkçılık ilkesi doğrultusunda, kadınlara seçme-seçilme hakkı tanınmıştır.',
    ),
    # düzey 2
    '0040': patch(
        "1 Kasım 1922'de TBMM'nin aldığı kararla saltanat ile halifelik birbirinden ayrıldı ve saltanat kaldırıldı.\n\nBuna göre saltanatın kaldırılmasıyla aşağıdakilerden hangisi sona ermiştir?",
        {
            'A': 'Halifelik kurumu',
            'B': 'Bakanlar Kurulu',
            'C': "TBMM'nin yasama ve bütçe onaylama yetkisi",
            'D': 'Osmanlı hanedanının siyasi egemenliği',
            'E': 'Cumhurbaşkanlığı makamı',
        },
        'D',
        "1 Kasım 1922'de saltanatın kaldırılmasıyla Osmanlı hanedanının siyasi egemenliği sona ermiştir. Halifelik ise ayrı bir düzenlemeyle 1924'te kaldırılmıştır.",
    ),
    # düzey 2
    '0041': patch(
        'Laiklik, din ve devlet işlerinin birbirinden ayrılmasını ve devletin bütün inançlara eşit uzaklıkta durmasını ifade eder.\n\nAşağıdaki inkılaplardan hangisi doğrudan laiklik ilkesiyle ilgilidir?',
        {
            'A': 'Ölçü sisteminin değiştirilmesi',
            'B': 'Soyadı Kanunu',
            'C': 'Aşar vergisinin kaldırılması',
            'D': 'Halifeliğin kaldırılması',
            'E': 'Kabotaj Kanunu',
        },
        'D',
        'Halifeliğin kaldırılması, tekke-zaviyelerin kapatılması ve öğretim birliği gibi düzenlemeler laiklik ilkesiyle doğrudan ilgilidir. Diğer seçenekler ekonomik ya da toplumsal alanla ilgilidir.',
    ),
    # düzey 2
    '0042': patch(
        '1924 Anayasası, Cumhuriyetin ilanından sonra devletin temel yapısını düzenleyen ilk kapsamlı anayasa olarak kabul edildi.\n\nBu anayasada benimsenen egemenlik anlayışı aşağıdakilerden hangisidir?',
        {
            'A': 'Egemenliğin yabancı devletlerde olması',
            'B': 'Egemenliğin padişah ve meclis arasında paylaşılması',
            'C': 'Egemenliğin bir kurula ait olması',
            'D': 'Egemenliğin halifede olması',
            'E': 'Egemenliğin kayıtsız şartsız millete ait olması',
        },
        'E',
        '1924 Anayasası, "Egemenlik kayıtsız şartsız milletindir" ilkesini benimsemiştir. Bu, millî egemenlik anlayışının anayasal güvenceye alınması demektir.',
    ),
    # düzey 2
    '0043': patch(
        'Aşağıdaki gelişmelerden hangisi ilk olarak (en erken) gerçekleşmiştir?',
        {
            'A': "Medeni Kanun'un kabulü",
            'B': 'Saltanatın kaldırılması',
            'C': 'Harf İnkılabı',
            'D': 'Cumhuriyetin ilanı',
            'E': 'Halifeliğin kaldırılması',
        },
        'B',
        "Saltanatın kaldırılması (1922), Cumhuriyetin ilanından (1923), halifeliğin kaldırılmasından (1924), Medeni Kanun'dan (1926) ve Harf İnkılabı'ndan (1928) öncedir; en erken gelişmedir.",
    ),
    # düzey 2
    '0044': patch(
        "Cumhuriyet Dönemi'nde demiryolu yapımına ağırlık verilmesinin temel amacı aşağıdakilerden hangisidir?",
        {
            'A': 'Ülkenin ekonomik bütünlüğünü ve ulaşımını güçlendirmek',
            'B': 'Yabancılara tanınan kapitülasyon ayrıcalıklarını olduğu gibi sürdürmek',
            'C': 'Yabancı şirketlere geniş ekonomik ayrıcalıklar ve haklar tanımak',
            'D': 'Ülkenin dış ticaretini yabancı şirketlere devretmek',
            'E': 'Kaldırılan saltanatı ve padişahlık düzenini yeniden geri getirmek',
        },
        'A',
        "Cumhuriyet Dönemi'nde demiryolları millîleştirilmiş ve yeni hatlar yapılmıştır. Amaç; ülke içi ulaşımı, ekonomik bütünlüğü ve güvenliği güçlendirmektir.",
    ),
    # düzey 2
    '0045': patch(
        "Osmanlı Devleti'nin son döneminde medreseler, Batı tarzı okullar, azınlık ve yabancı okulları farklı anlayışlarla eğitim veriyor; bu durum toplumda düşünce birliğini zayıflatıyordu.\n\nBu sorunu çözmek amacıyla 3 Mart 1924'te kabul edilen Tevhid-i Tedrisat Kanunu ile aşağıdakilerden hangisi sağlanmıştır?",
        {
            'A': 'Yabancı okulların kapatılması',
            'B': 'Eğitimin dine bağlanması',
            'C': "Üniversitelerin Şer'iye Vekâleti'ne bağlanması",
            'D': 'Öğretimin birleştirilip tek elde toplanması',
            'E': 'Eğitimin vakıflara devredilmesi',
        },
        'D',
        "Tevhid-i Tedrisat Kanunu ile farklı programlarla eğitim veren tüm okullar Millî Eğitim Bakanlığı'na bağlanarak öğretim birliği sağlanmıştır.",
    ),
    # düzey 2
    '0046': patch(
        'Aşağıdakilerden hangisi toplumsal alandaki inkılaplardan biri değildir?',
        {
            'A': 'Tekke ve zaviyelerin kapatılması',
            'B': 'Şapka ve kılık-kıyafet düzenlemesi',
            'C': "Soyadı Kanunu'nun çıkarılması",
            'D': 'Halifeliğin kaldırılması',
            'E': 'Takvim, saat ve ölçülerin değiştirilmesi',
        },
        'D',
        'Halifeliğin kaldırılması siyasi-laik nitelikli bir inkılaptır. Şapka, takvim-saat-ölçü, soyadı ve tekke-zaviye düzenlemeleri ise toplumsal alandaki inkılaplardır.',
    ),
    # düzey 3
    '0047': patch(
        "Yeni Türk Devleti'nde 1924'te kaldırılarak yerine Millî Eğitim'e bağlı okulların açıldığı, dinî eğitim veren geleneksel kurumlar aşağıdakilerden hangisidir?",
        {
            'A': 'Köy Enstitüleri',
            'B': 'Medreseler',
            'C': 'Darülfünunlar',
            'D': 'Halkevleri',
            'E': 'Millet Mektepleri',
        },
        'B',
        'Tevhid-i Tedrisat Kanunu ile geleneksel dinî eğitim veren medreseler kapatılmış; eğitim çağdaş, laik ve tek program altında toplanmıştır.',
    ),
    # düzey 2
    '0048': patch(
        "Cumhuriyetin ilanının, TBMM Hükûmeti'nin ilk döneminden farkı aşağıdakilerden hangisidir?",
        {
            'A': 'Devlet başkanlığı sorununu kesin çözüme kavuşturması',
            'B': "Millet Meclisi'ni kapatıp yetkilerini tek kişiye devretmesi",
            'C': 'Kaldırılan saltanatı ve padişahlık makamını yeniden kurması',
            'D': 'Halifelik kurumunu güçlendirip devlet başkanlığını halifeye vermesi',
            'E': 'Ülkeye yabancı bir devletin manda yönetimini getirmesi',
        },
        'A',
        'Cumhuriyetin ilanı, o güne dek belirsiz olan devlet başkanlığı (rejim) sorununu kesin biçimde çözmüş; yönetim biçimini cumhuriyet olarak netleştirmiştir.',
    ),
    # düzey 2
    '0049': patch(
        'Atatürk inkılaplarının genel amacı aşağıdakilerden hangisidir?',
        {
            'A': 'Geleneksel medrese eğitimini ülke genelinde yaygınlaştırmak',
            'B': 'Ulus bilinci yerine dinî ümmet anlayışını yeniden güçlendirmek',
            'C': 'Yabancılara tanınan kapitülasyon ayrıcalıklarını sürdürmek',
            'D': 'Kaldırılan saltanat ve padişahlık düzenini yeniden kurmak',
            'E': 'Türk toplumunu çağdaş uygarlık düzeyine ulaştırmak',
        },
        'E',
        'Atatürk inkılaplarının temel amacı; Türk toplumunu akıl ve bilim ışığında çağdaş uygarlık düzeyine ulaştırmak, bağımsız ve laik bir ulus-devlet oluşturmaktır.',
    ),
    # düzey 2
    '0050': patch(
        "17 Şubat 1926'da kabul edilen Türk Medeni Kanunu, aile hukukundan miras hukukuna kadar pek çok alanda yeni düzenlemeler getirmiştir.\n\nTürk Medeni Kanunu'nun kabulüyle aşağıdakilerden hangisi sağlanmıştır?",
        {
            'A': 'Medeni hukukta dinî kuralların korunması',
            'B': 'Hukukta birlik ve kadın-erkek eşitliği',
            'C': 'Kapitülasyonların korunması',
            'D': 'Saltanatın geri getirilmesi',
            'E': 'Halifeliğin güçlendirilmesi',
        },
        'B',
        'Medeni Kanun ile hukukta birlik sağlanmış; evlilik, boşanma ve mirasta kadın-erkek eşitliği getirilerek çağdaş bir hukuk düzenine geçilmiştir.',
    ),
    # düzey 2
    '0051': patch(
        "1926'da kabul edilen Kabotaj Kanunu'nun sağladığı temel kazanım aşağıdakilerden hangisidir?",
        {
            'A': 'Türk karasularında taşımacılığın millîleştirilmesi',
            'B': 'Aşar vergisinin artırılması',
            'C': 'Havayolu taşımacılığının başlaması',
            'D': 'Ülkedeki demiryollarının satın alınıp millîleştirilmesi',
            'E': 'Kara yollarının yapımı',
        },
        'A',
        'Kabotaj Kanunu ile Türk karasularında (limanlar arası) yük ve yolcu taşıma hakkı Türk gemilerine verilerek denizcilikte millîleşme sağlanmıştır.',
    ),
    # düzey 2
    '0052': patch(
        "Terakkiperver Cumhuriyet Fırkası'nın kapatılmasına yol açan olay aşağıdakilerden hangisidir?",
        {
            'A': 'İzmir Suikastı',
            'B': 'Şeyh Sait Ayaklanması',
            'C': 'Menemen Olayı',
            'D': 'Balkan Savaşları',
            'E': '31 Mart Olayı',
        },
        'B',
        "1925'teki Şeyh Sait Ayaklanması'nın ardından çıkarılan Takrir-i Sükûn Kanunu'na dayanılarak Terakkiperver Cumhuriyet Fırkası kapatılmıştır.",
    ),
    # düzey 2
    '0053': patch(
        'Aşağıdakilerden hangisi kadın haklarıyla ilgili gelişmelerden biri değildir?',
        {
            'A': 'Medeni Kanun ile mirasta eşitlik',
            'B': "Kabotaj Kanunu'nun çıkarılması",
            'C': "1930'da belediye seçimlerinde oy hakkı",
            'D': 'Resmî nikâh zorunluluğu',
            'E': "1934'te milletvekili seçme-seçilme hakkı",
        },
        'B',
        'Kabotaj Kanunu denizcilikle ilgili ekonomik bir düzenlemedir; kadın haklarıyla ilgisi yoktur. Diğer seçenekler kadın haklarındaki gelişmelerdir.',
    ),
    # düzey 2
    '0054': patch(
        'Yeni Türk harflerinin kabulünden sonra kültür alanında yapılan önemli çalışmalardan biri aşağıdakilerden hangisidir?',
        {
            'A': 'Medreselerin yeniden açılması',
            'B': 'Kapitülasyonların getirilmesi',
            'C': 'Saltanatın geri getirilmesi',
            'D': 'Aşar vergisinin konulması',
            'E': "Türk Dil Kurumu'nun kurulması",
        },
        'E',
        "Harf İnkılabı'nın ardından dilde sadeleşme ve gelişmeyi sağlamak için 1932'de Türk Dil Kurumu kurulmuştur; bu, kültür alanındaki inkılapları tamamlar.",
    ),
    # düzey 2
    '0055': patch(
        "Cumhuriyet Dönemi'nde çıkarılan ve çalışanlara belirli bir günü tatil hakkı tanıyan düzenleme aşağıdaki alanlardan hangisiyle ilgilidir?",
        {
            'A': 'Saltanat düzeni',
            'B': 'Toplumsal yaşam',
            'C': 'Askerî alan',
            'D': 'Halifelik kurumu',
            'E': 'Dış politika',
        },
        'B',
        'Hafta tatili ve çalışma yaşamına ilişkin düzenlemeler, toplumsal-sosyal yaşamı çağdaşlaştıran düzenlemelerdendir.',
    ),
    # düzey 2
    '0056': patch(
        'Aşağıdaki inkılaplardan hangisi hem hukuk hem de kadın hakları açısından önem taşır?',
        {
            'A': "Türk Medeni Kanunu'nun kabulü",
            'B': 'Latin harflerinin kabulü',
            'C': 'Kabotaj Kanunu',
            'D': 'Aşar vergisinin kaldırılması',
            'E': 'Şapka Kanunu',
        },
        'A',
        'Medeni Kanun hem hukukta birlik sağlaması yönüyle hukuk, hem de kadına miras-boşanma-evlilikte eşitlik getirmesiyle kadın hakları açısından önemlidir.',
    ),
    # düzey 2
    '0057': patch(
        "İzmir İktisat Kongresi'nde alınan kararların temel amacı aşağıdakilerden hangisidir?",
        {
            'A': 'Osmanlı borçlarını yeniden yapılandırmak',
            'B': 'Kapitülasyonları aşamalı olarak sürdürmek',
            'C': "Dış ticareti İtilaf Devletleri'ne açmak",
            'D': 'Tarımdan alınan vergileri artırmak',
            'E': 'Millî ve bağımsız bir ekonomi oluşturmak',
        },
        'E',
        'İzmir İktisat Kongresi kararları; yerli üretimi destekleyen, millî ve bağımsız bir ekonomi kurmayı amaçlar. Bu kararlar, ekonomik bağımsızlığın temelini oluşturur.',
    ),
    # düzey 2
    '0058': patch(
        "Aşağıdakilerden hangisi Atatürk Dönemi'nde açılan sanayi kuruluşlarına örnek gösterilebilir?",
        {
            'A': 'Sümerbank ve Etibank',
            'B': 'Reji İdaresi',
            'C': 'Düyun-u Umumiye',
            'D': 'Osmanlı Bankası',
            'E': 'Duyunu Umumiye Sandığı',
        },
        'A',
        "Devletçilik ilkesi doğrultusunda kurulan Sümerbank (dokuma-sanayi) ve Etibank (madencilik-enerji), Atatürk Dönemi'nin önemli kamu sanayi kuruluşlarındandır.",
    ),
    # düzey 2
    '0059': patch(
        'Aşağıdaki inkılaplardan hangisi "laiklik" ilkesinin doğrudan bir uygulaması değildir?',
        {
            'A': 'Öğretim birliğinin sağlanması',
            'B': 'Halifeliğin kaldırılması',
            'C': 'Tekke ve zaviyelerin kapatılması',
            'D': 'Anayasadan "devletin dini İslam\'dır" ibaresinin çıkarılması',
            'E': 'Ölçü ve tartı birimlerinin değiştirilmesi',
        },
        'E',
        'Ölçü-tartı sistemine geçiş toplumsal-ekonomik nitelikli bir düzenlemedir; laiklikle doğrudan ilgisi yoktur. Diğer seçenekler laiklik ilkesinin uygulamalarıdır.',
    ),
    # düzey 2
    '0060': patch(
        '"Devletin dini İslam\'dır" ibaresinin anayasadan çıkarılması (1928) hangi ilke yönünden önemli bir adımdır?',
        {
            'A': 'Devletçilik',
            'B': 'Milliyetçilik',
            'C': 'Halkçılık',
            'D': 'Cumhuriyetçilik',
            'E': 'Laiklik',
        },
        'E',
        '1928\'de anayasadan "Devletin dini İslam\'dır" ibaresinin çıkarılması, din ile devlet işlerinin ayrılması yönünde atılmış bir adım olup laiklik ilkesiyle ilgilidir.',
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
    print(f"1 paket / {len(PATCHES)} soru ('Atatürk İnkılapları' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
