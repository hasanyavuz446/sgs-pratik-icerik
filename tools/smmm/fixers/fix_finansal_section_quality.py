#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Finansal Muhasebe bölüm testlerini 2026/1 biçim profiline yaklaştırır.

Hedefler:
- 3 test × 20 soru,
- test başına 11 kayıt/yevmiye sorusu,
- test başına 0 öncüllü soru,
- eksiksiz kaynak ve sürüm alanları,
- dengeli, periyodik olmayan cevap harfleri,
- konu havuzundan ayrı Bölüm Havuzu etiketi,
- içerik ve uygulama kopyalarının özdeş tutulması.

Script idempotenttir; mevcut iyi soruları korur, yalnız REPLACEMENTS içindeki
soruları yeniden kurar ve ilk teste iki özgün soru ekler.
"""
from __future__ import annotations

import json
import random
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTENT = ROOT / "content" / "yeterlilik"
APP_CONTENT = ROOT.parent / "smmm_sgs_pratik" / "assets" / "content" / "yeterlilik"

FILES = {
    "questions_finansal_muhasebe_2026.json": 20260731,
    "questions_finansal_muhasebe_test2_2026.json": 20260801,
    "questions_finansal_muhasebe_test3_2026.json": 20260802,
}

JOURNAL_IDS = {
    "questions_finansal_muhasebe_2026.json": {
        "demo-finansal-003", "demo-finansal-004", "demo-finansal-005",
        "demo-finansal-006", "demo-finansal-007", "demo-finansal-008",
        "demo-finansal-012", "demo-finansal-013", "demo-finansal-014",
        "demo-finansal-015", "yet-finansal-t1-0019",
    },
    "questions_finansal_muhasebe_test2_2026.json": {
        "demo-finansal-022", "demo-finansal-024", "demo-finansal-025",
        "demo-finansal-026", "demo-finansal-027", "demo-finansal-028",
        "demo-finansal-029", "demo-finansal-030", "demo-finansal-036",
        "demo-finansal-037", "demo-finansal-038",
    },
    "questions_finansal_muhasebe_test3_2026.json": {
        "demo-finansal-043", "demo-finansal-044", "demo-finansal-046",
        "demo-finansal-047", "demo-finansal-048", "demo-finansal-049",
        "demo-finansal-050", "demo-finansal-051", "demo-finansal-054",
        "demo-finansal-055", "demo-finansal-057",
    },
}

LEGISLATION_VERSION = (
    "TFRS 2026 Seti (Mavi Kitap) ve yürürlükteki Tekdüzen Hesap Planı"
)
UPDATED_AT = "2026-07-17T00:00:00Z"
PREMISE_MARK = re.compile(r"(?m)^\s*(?:IV|I{1,3}|V)[\.)]\s")
VALID_TOPIC_IDS = {
    "temel_kavramlar",
    "muhasebe_kayitlari",
    "finansal_stoklar",
    "donem_sonu_islemleri",
    "tms_tfrs",
}
TOPIC_ALIASES = {
    "stok_degerleme_maliyet": "finansal_stoklar",
    "tms_tfrs_uygulamalari": "tms_tfrs",
}


def journal(*lines: str) -> str:
    return "```text\n" + "\n".join(lines) + "\n```"


def spec(
    question: str,
    correct: str,
    distractors: list[str],
    explanation: str,
    legislation_ref: str,
    topic_id: str,
    difficulty: str = "medium",
) -> dict:
    assert len(distractors) == 4
    assert len({correct, *distractors}) == 5
    return {
        "question": question,
        "choices": dict(zip("ABCDE", [correct, *distractors])),
        "correctAnswer": "A",
        "explanation": explanation,
        "source": {
            "kind": "generated",
            "styleRef": "2026/1 beş seçenekli test biçimi",
            "legislationRef": legislation_ref,
        },
        "topicId": topic_id,
        "difficulty": difficulty,
    }


REPLACEMENTS = {
    "demo-finansal-003": spec(
        "İşletme, 10.000 TL + %20 KDV tutarındaki ticari malı peşin satın almıştır. Yapılacak kayıt hangisidir?",
        journal(
            "153 TİCARİ MALLAR          10.000",
            "191 İNDİRİLECEK KDV         2.000",
            "    100 KASA                       12.000",
        ),
        [
            journal("153 TİCARİ MALLAR          12.000", "    100 KASA                       12.000"),
            journal("153 TİCARİ MALLAR          10.000", "391 HESAPLANAN KDV          2.000", "    100 KASA                       12.000"),
            journal("100 KASA                    12.000", "    153 TİCARİ MALLAR              10.000", "    191 İNDİRİLECEK KDV             2.000"),
            journal("153 TİCARİ MALLAR          10.000", "    320 SATICILAR                   10.000"),
        ],
        "Mal bedeli stok maliyetine, indirilebilir KDV 191 hesaba borç kaydedilir. Peşin ödenen KDV dâhil 12.000 TL nedeniyle 100 Kasa hesabı alacaklandırılır.",
        "Tekdüzen Hesap Planı: 100, 153 ve 191 hesapları",
        "muhasebe_kayitlari",
        "easy",
    ),
    "demo-finansal-010": spec(
        "100 birimi 10 TL ve 100 birimi 14 TL maliyetli stokların tartılı ortalama birim maliyeti kaç TL'dir?",
        "12 TL",
        ["10 TL", "11 TL", "13 TL", "14 TL"],
        "Toplam maliyet 100 × 10 + 100 × 14 = 2.400 TL, toplam miktar 200 birimdir. Tartılı ortalama birim maliyet 2.400 / 200 = 12 TL'dir.",
        "TMS 2 Stoklar, par. 25 ve 27",
        "finansal_stoklar",
        "easy",
    ),
    "demo-finansal-015": spec(
        "Dönem sonunda 391 Hesaplanan KDV hesabı 30.000 TL, 191 İndirilecek KDV hesabı 18.000 TL bakiyelidir. KDV mahsubu kaydı hangisidir?",
        journal(
            "391 HESAPLANAN KDV         30.000",
            "    191 İNDİRİLECEK KDV            18.000",
            "    360 ÖDENECEK VERGİ VE FONLAR    12.000",
        ),
        [
            journal("191 İNDİRİLECEK KDV        18.000", "190 DEVREDEN KDV            12.000", "    391 HESAPLANAN KDV             30.000"),
            journal("391 HESAPLANAN KDV         30.000", "    190 DEVREDEN KDV               12.000", "    191 İNDİRİLECEK KDV            18.000"),
            journal("191 İNDİRİLECEK KDV        18.000", "360 ÖDENECEK VERGİ VE FONLAR 12.000", "    391 HESAPLANAN KDV             30.000"),
            journal("391 HESAPLANAN KDV         30.000", "    191 İNDİRİLECEK KDV            30.000"),
        ],
        "391 hesap 30.000 TL borçlandırılarak kapatılır; 191 hesap 18.000 TL alacaklandırılır. Hesaplanan KDV fazlası olan 12.000 TL, 360 hesapta ödenecek vergi olarak alacak izlenir.",
        "Tekdüzen Hesap Planı: 191, 360 ve 391 hesapları",
        "donem_sonu_islemleri",
    ),
    "demo-finansal-020": spec(
        "Geçici mizanın borç toplamı 90.000 TL, alacak toplamı 88.000 TL'dir. Bu durumda öncelikle ne yapılmalıdır?",
        "2.000 TL'lik farkın kaynağı yevmiye, büyük defter ve aktarma kayıtlarında araştırılmalıdır.",
        [
            "2.000 TL doğrudan sermaye hesabına alacak yazılarak mizan eşitlenmelidir.",
            "Borç toplamı esas alınmalı ve alacak toplamındaki fark dönem kârına eklenmelidir.",
            "Alacak toplamı esas alınmalı ve borç tarafındaki fark kasa noksanı sayılmalıdır.",
            "Mizan toplamlarının eşit olması gerekmediğinden herhangi bir düzeltme yapılmamalıdır.",
        ],
        "Çift taraflı kayıtta mizan borç ve alacak toplamları eşit olmalıdır. Fark, kendiliğinden bir sonuç hesabına aktarılmaz; kayıt ve aktarma zinciri incelenerek hatanın kaynağı bulunur.",
        "Tekdüzen Hesap Planı ve çift taraflı kayıt sistemi",
        "temel_kavramlar",
        "easy",
    ),
    "demo-finansal-021": spec(
        "Varlıkları 420.000 TL, borçları 170.000 TL olan işletmenin özkaynakları kaç TL'dir?",
        "250.000 TL",
        ["170.000 TL", "420.000 TL", "590.000 TL", "714.000 TL"],
        "Temel muhasebe denklemi Varlıklar = Borçlar + Özkaynaklar biçimindedir. Özkaynaklar 420.000 − 170.000 = 250.000 TL'dir.",
        "Finansal Raporlamaya İlişkin Kavramsal Çerçeve, varlık-borç-özkaynak tanımları",
        "temel_kavramlar",
        "easy",
    ),
    "demo-finansal-022": spec(
        "İşletme aralık ayında tamamladığı 45.000 TL tutarındaki danışmanlık hizmetini henüz faturalandırmamış ve tahsil etmemiştir. 31 Aralık tahakkuk kaydı hangisidir?",
        journal("181 GELİR TAHAKKUKLARI     45.000", "    600 YURT İÇİ SATIŞLAR         45.000"),
        [
            journal("102 BANKALAR              45.000", "    600 YURT İÇİ SATIŞLAR         45.000"),
            journal("600 YURT İÇİ SATIŞLAR     45.000", "    181 GELİR TAHAKKUKLARI        45.000"),
            journal("120 ALICILAR              45.000", "    340 ALINAN SİPARİŞ AVANSLARI  45.000"),
            journal("180 GELECEK AYLARA AİT GİD. 45.000", "    102 BANKALAR                  45.000"),
        ],
        "Hizmet aralık ayında tamamlandığı için gelir tahakkuk etmiştir. Henüz fatura ve tahsilat bulunmadığından 181 Gelir Tahakkukları borç, 600 Yurt İçi Satışlar alacak kaydedilir.",
        "Tekdüzen Hesap Planı: 181 ve 600 hesapları; tahakkuk esası",
        "donem_sonu_islemleri",
    ),
    "demo-finansal-030": spec(
        "İşletme gelecek ay teslim edeceği mallar için müşteriden banka yoluyla 40.000 TL avans almıştır. Tahsilat tarihinde yapılacak kayıt hangisidir?",
        journal("102 BANKALAR              40.000", "    340 ALINAN SİPARİŞ AVANSLARI  40.000"),
        [
            journal("102 BANKALAR              40.000", "    600 YURT İÇİ SATIŞLAR         40.000"),
            journal("340 ALINAN SİPARİŞ AVANSLARI 40.000", "    102 BANKALAR                  40.000"),
            journal("120 ALICILAR              40.000", "    600 YURT İÇİ SATIŞLAR         40.000"),
            journal("153 TİCARİ MALLAR         40.000", "    102 BANKALAR                  40.000"),
        ],
        "Mal henüz teslim edilmediğinden hasılat doğmamıştır. Banka mevcudu artarken müşteriye karşı teslim yükümlülüğü 340 Alınan Sipariş Avansları hesabında izlenir.",
        "TFRS 15, edim yükümlülüğü ilkesi; Tekdüzen Hesap Planı: 102 ve 340 hesapları",
        "muhasebe_kayitlari",
    ),
    "demo-finansal-037": spec(
        "İşletme 1 Ekim'de bir yıllık yönetim binası sigortası için 24.000 TL ödemiş ve tutarın tamamını 180 Gelecek Aylara Ait Giderler hesabına kaydetmiştir. 31 Aralık düzeltme kaydı hangisidir?",
        journal("770 GENEL YÖNETİM GİDERLERİ  6.000", "    180 GELECEK AYLARA AİT GİD.   6.000"),
        [
            journal("770 GENEL YÖNETİM GİDERLERİ 24.000", "    180 GELECEK AYLARA AİT GİD.  24.000"),
            journal("180 GELECEK AYLARA AİT GİD.  6.000", "    770 GENEL YÖNETİM GİDERLERİ   6.000"),
            journal("280 GELECEK YILLARA AİT GİD. 18.000", "    180 GELECEK AYLARA AİT GİD.  18.000"),
            journal("770 GENEL YÖNETİM GİDERLERİ  2.000", "    102 BANKALAR                   2.000"),
        ],
        "Aylık sigorta gideri 24.000 / 12 = 2.000 TL'dir. Ekim-aralık dönemine ait 6.000 TL giderleştirilir; 180 hesap aynı tutarda azaltılır.",
        "Tekdüzen Hesap Planı: 180 ve 770 hesapları; dönemsellik kavramı",
        "donem_sonu_islemleri",
    ),
    "demo-finansal-038": spec(
        "İşletme, 10.000 TL tutarındaki ticari alacağını şüpheli ticari alacak hesabına aktarmış ve tamamı için karşılık ayırmıştır. Birbirini izleyen iki kayıt hangisidir?",
        journal(
            "128 ŞÜPHELİ TİCARİ ALACAKLAR 10.000",
            "    120 ALICILAR                    10.000",
            "654 KARŞILIK GİDERLERİ       10.000",
            "    129 ŞÜPHELİ TİCARİ ALACAK KARŞ. 10.000",
        ),
        [
            journal("120 ALICILAR              10.000", "    128 ŞÜPHELİ TİCARİ ALACAKLAR 10.000", "129 ŞÜPHELİ TİCARİ ALACAK KARŞ. 10.000", "    654 KARŞILIK GİDERLERİ      10.000"),
            journal("128 ŞÜPHELİ TİCARİ ALACAKLAR 10.000", "    120 ALICILAR                10.000", "100 KASA                    10.000", "    128 ŞÜPHELİ TİCARİ ALACAKLAR 10.000"),
            journal("654 KARŞILIK GİDERLERİ    10.000", "    120 ALICILAR                 10.000"),
            journal("129 ŞÜPHELİ TİCARİ ALACAK KARŞ. 10.000", "    128 ŞÜPHELİ TİCARİ ALACAKLAR 10.000"),
        ],
        "Önce ticari alacak 120 hesaptan 128 hesaba aktarılır. Ardından gider 654 hesaba borç, varlığı düzenleyen karşılık 129 hesaba alacak kaydedilir.",
        "Tekdüzen Hesap Planı: 120, 128, 129 ve 654 hesapları",
        "donem_sonu_islemleri",
    ),
    "demo-finansal-040": spec(
        "TMS 16'ya göre toplam maliyeti içinde önemli olan ve yararlı ömrü ana varlıktan farklı bulunan bir parçanın amortismanında hangi yaklaşım uygulanır?",
        "Önemli parça ayrı amortismana tabi tutulur ve kendi yararlı ömrü esas alınır.",
        [
            "Bütün parçalar önemine bakılmadan ana varlığın tek oranıyla amorti edilir.",
            "Önemli parça varlıktan ayrılır ancak hiçbir dönemde amortisman ayrılmaz.",
            "Parçanın yararlı ömrü yerine yalnız ana varlığın kalıntı değeri esas alınır.",
            "Farklı yararlı ömür yalnız vergi matrahında izlenir, finansal raporlamaya yansımaz.",
        ],
        "Bir maddi duran varlık kaleminin toplam maliyetine göre önemli her parçası ayrı amortismana tabi tutulur. Böylece tüketim biçimi ve yararlı ömür farklılığı finansal tablolara yansıtılır.",
        "TMS 16 Maddi Duran Varlıklar, par. 43-47",
        "tms_tfrs",
    ),
    "demo-finansal-043": spec(
        "Yönetim binasının aralık ayı elektrik tüketimine ilişkin 12.000 TL tutarındaki fatura ocak ayında gelecektir. 31 Aralık'ta yapılacak kayıt hangisidir?",
        journal("770 GENEL YÖNETİM GİDERLERİ 12.000", "    381 GİDER TAHAKKUKLARI        12.000"),
        [
            journal("381 GİDER TAHAKKUKLARI     12.000", "    770 GENEL YÖNETİM GİDERLERİ  12.000"),
            journal("770 GENEL YÖNETİM GİDERLERİ 12.000", "    102 BANKALAR                  12.000"),
            journal("180 GELECEK AYLARA AİT GİD. 12.000", "    102 BANKALAR                  12.000"),
            journal("181 GELİR TAHAKKUKLARI     12.000", "    649 DİĞER OLAĞAN GELİR VE KÂR. 12.000"),
        ],
        "Elektrik aralık ayında tüketildiği için gider aynı dönemde tahakkuk eder. Henüz fatura ve ödeme bulunmadığından 770 hesap borç, 381 Gider Tahakkukları alacak kaydedilir.",
        "Tekdüzen Hesap Planı: 381 ve 770 hesapları; tahakkuk esası",
        "donem_sonu_islemleri",
    ),
    "demo-finansal-044": spec(
        "Şirket ortağı kişisel ihtiyacı için kasadan 15.000 TL çekmiş ve tutarın ortak cari hesabında izlenmesine karar verilmiştir. Yapılacak kayıt hangisidir?",
        journal("131 ORTAKLARDAN ALACAKLAR   15.000", "    100 KASA                       15.000"),
        [
            journal("770 GENEL YÖNETİM GİDERLERİ 15.000", "    100 KASA                       15.000"),
            journal("100 KASA                  15.000", "    131 ORTAKLARDAN ALACAKLAR     15.000"),
            journal("500 SERMAYE               15.000", "    600 YURT İÇİ SATIŞLAR         15.000"),
            journal("120 ALICILAR              15.000", "    102 BANKALAR                  15.000"),
        ],
        "Ortağın kişisel çekişi işletmenin faaliyet gideri değildir. Ortaktan tahsil edilecek tutar 131 hesaba borç, kasa çıkışı 100 hesaba alacak kaydedilir.",
        "Tekdüzen Hesap Planı: 100 ve 131 hesapları; işletme kişiliği kavramı",
        "muhasebe_kayitlari",
    ),
    "demo-finansal-046": spec(
        "İşletme 50.000 TL nominal değerli alacak senedini vadesinden önce bankaya devretmiştir. Tahsil riski bütünüyle bankaya geçmiş, işletmenin geri ödeme yükümlülüğü kalmamış ve banka 3.000 TL keserek 47.000 TL yatırmıştır. Kayıt hangisidir?",
        journal("102 BANKALAR              47.000", "780 FİNANSMAN GİDERLERİ    3.000", "    121 ALACAK SENETLERİ          50.000"),
        [
            journal("102 BANKALAR              50.000", "    121 ALACAK SENETLERİ          47.000", "    642 FAİZ GELİRLERİ             3.000"),
            journal("121 ALACAK SENETLERİ      50.000", "    102 BANKALAR                  47.000", "    780 FİNANSMAN GİDERLERİ        3.000"),
            journal("102 BANKALAR              47.000", "    121 ALACAK SENETLERİ          47.000"),
            journal("102 BANKALAR              47.000", "180 GELECEK AYLARA AİT GİD. 3.000", "    121 ALACAK SENETLERİ          50.000"),
        ],
        "Risk ve getiriler bütünüyle devredildiği için senet kayıttan çıkarılır. Bankaya giren 47.000 TL ile nominal tutar arasındaki 3.000 TL finansman gideridir.",
        "TFRS 9 finansal varlıkların bilanço dışı bırakılması; Tekdüzen Hesap Planı: 102, 121 ve 780 hesapları",
        "muhasebe_kayitlari",
        "hard",
    ),
    "demo-finansal-045": spec(
        "Borç ve alacak toplamları eşit olan bir mizan, aşağıdaki hatalardan hangisini tek başına ortaya çıkaramaz?",
        "Doğru tutarın hem borç hem alacak tarafında yanlış hesaplara kaydedilmesini",
        [
            "Yevmiye maddesinin yalnız borç tarafının büyük deftere aktarılmasını",
            "Borç tarafına 18.000 TL, alacak tarafına 81.000 TL aktarılmasını",
            "Bir hesabın borç sütunu toplamında aritmetik hata yapılmasını",
            "Alacak bakiyeli bir hesabın mizanın borç sütununa yazılmasını",
        ],
        "Bir işlem eşit tutarla yanlış hesapların borç ve alacağına kaydedilirse toplamlar yine eşit kalır; mizan bu sınıflandırma hatasını göstermez. Tek taraflı aktarma, tutar farkı ve toplama/sütun hataları ise dengeyi bozar.",
        "Tekdüzen Hesap Planı; çift taraflı kayıt ve mizan kontrolü",
        "temel_kavramlar",
    ),
    "demo-finansal-047": spec(
        "İşletme, satıcıya olan 30.000 TL borcu için çek düzenleyip vermiştir. Çekin verilmesi tarihinde yapılacak kayıt hangisidir?",
        journal("320 SATICILAR             30.000", "    103 VERİLEN ÇEKLER VE ÖDEME EMİRLERİ 30.000"),
        [
            journal("103 VERİLEN ÇEKLER VE ÖDEME EMİRLERİ 30.000", "    320 SATICILAR                 30.000"),
            journal("320 SATICILAR             30.000", "    101 ALINAN ÇEKLER             30.000"),
            journal("120 ALICILAR              30.000", "    103 VERİLEN ÇEKLER VE ÖDEME EMİRLERİ 30.000"),
            journal("320 SATICILAR             30.000", "    102 BANKALAR                  30.000"),
        ],
        "Satıcıya olan borç 320 hesabın borcuna kaydedilerek azaltılır. Düzenlenip verilen çek, ödeme gerçekleşinceye kadar 103 Verilen Çekler ve Ödeme Emirleri hesabında alacak izlenir.",
        "Tekdüzen Hesap Planı: 103 ve 320 hesapları",
        "muhasebe_kayitlari",
    ),
    "demo-finansal-049": spec(
        "Banka kredisinin bilanço tarihine kadar işlemiş ancak henüz ödenmemiş 7.500 TL faizi için hangi kayıt yapılır?",
        journal("780 FİNANSMAN GİDERLERİ    7.500", "    381 GİDER TAHAKKUKLARI         7.500"),
        [
            journal("381 GİDER TAHAKKUKLARI     7.500", "    780 FİNANSMAN GİDERLERİ        7.500"),
            journal("780 FİNANSMAN GİDERLERİ    7.500", "    102 BANKALAR                   7.500"),
            journal("180 GELECEK AYLARA AİT GİD. 7.500", "    102 BANKALAR                  7.500"),
            journal("300 BANKA KREDİLERİ        7.500", "    102 BANKALAR                   7.500"),
        ],
        "Faiz bilanço tarihine kadar doğduğu için tahakkuk esasına göre gider yazılır. Henüz ödenmeyen tutar 381 Gider Tahakkukları hesabında yükümlülük olarak alacak izlenir.",
        "Tekdüzen Hesap Planı: 381 ve 780 hesapları; tahakkuk esası",
        "donem_sonu_islemleri",
    ),
    "demo-finansal-050": spec(
        "Müşteri, daha önce kredili satın aldığı 12.000 TL tutarındaki malı işletmeye iade etmiştir. KDV ve maliyet kaydı dikkate alınmayacaktır. Hasılat yönünden kayıt hangisidir?",
        journal("610 SATIŞTAN İADELER       12.000", "    120 ALICILAR                   12.000"),
        [
            journal("120 ALICILAR              12.000", "    610 SATIŞTAN İADELER          12.000"),
            journal("120 ALICILAR              12.000", "    600 YURT İÇİ SATIŞLAR        12.000"),
            journal("153 TİCARİ MALLAR         12.000", "    320 SATICILAR                  12.000"),
            journal("610 SATIŞTAN İADELER      12.000", "    102 BANKALAR                  12.000"),
        ],
        "Kredili satışın iadesinde hasılatı azaltan 610 Satıştan İadeler hesabı borçlandırılır; müşteriden olan alacak 120 Alıcılar hesabı alacaklandırılarak azaltılır.",
        "Tekdüzen Hesap Planı: 120 ve 610 hesapları",
        "muhasebe_kayitlari",
    ),
    "demo-finansal-051": spec(
        "Önceki dönemde stok için ayrılan 8.000 TL değer düşüklüğü karşılığının tamamı, TMS 2'deki koşullar sağlandığı için bu dönemde iptal edilecektir. Tekdüzen Hesap Planına göre kayıt hangisidir?",
        journal("158 STOK DEĞER DÜŞÜKLÜĞÜ KARŞ. 8.000", "    644 KONUSU KALMAYAN KARŞILIKLAR 8.000"),
        [
            journal("654 KARŞILIK GİDERLERİ      8.000", "    158 STOK DEĞER DÜŞÜKLÜĞÜ KARŞ. 8.000"),
            journal("644 KONUSU KALMAYAN KARŞILIKLAR 8.000", "    158 STOK DEĞER DÜŞÜKLÜĞÜ KARŞ. 8.000"),
            journal("153 TİCARİ MALLAR           8.000", "    600 YURT İÇİ SATIŞLAR          8.000"),
            journal("158 STOK DEĞER DÜŞÜKLÜĞÜ KARŞ. 8.000", "    153 TİCARİ MALLAR               8.000"),
        ],
        "Karşılık iptalinde düzenleyici 158 hesap borçlandırılarak azaltılır; konusu kalmayan karşılık 644 hesaba alacak kaydedilir. İptal, daha önce kaydedilen değer düşüklüğünü aşamaz.",
        "TMS 2 Stoklar, par. 33-34; Tekdüzen Hesap Planı: 158 ve 644 hesapları",
        "finansal_stoklar",
        "hard",
    ),
    "demo-finansal-054": spec(
        "Yönetim faaliyetinde kullanılan bir cihazın maliyeti 120.000 TL, kalıntı değeri 20.000 TL ve yararlı ömrü 5 yıldır. Doğrusal yönteme göre yıllık amortisman kaydı hangisidir?",
        journal("770 GENEL YÖNETİM GİDERLERİ 20.000", "    257 BİRİKMİŞ AMORTİSMANLAR    20.000"),
        [
            journal("770 GENEL YÖNETİM GİDERLERİ 24.000", "    257 BİRİKMİŞ AMORTİSMANLAR    24.000"),
            journal("257 BİRİKMİŞ AMORTİSMANLAR 20.000", "    255 DEMİRBAŞLAR               20.000"),
            journal("730 GENEL ÜRETİM GİDERLERİ 20.000", "    257 BİRİKMİŞ AMORTİSMANLAR    20.000"),
            journal("770 GENEL YÖNETİM GİDERLERİ 20.000", "    255 DEMİRBAŞLAR               20.000"),
        ],
        "Amortismana tabi tutar 120.000 − 20.000 = 100.000 TL, yıllık amortisman 100.000 / 5 = 20.000 TL'dir. Yönetimde kullanılan cihazın gideri 770, birikmiş amortismanı 257 hesapta izlenir.",
        "TMS 16 Maddi Duran Varlıklar, par. 50-53; Tekdüzen Hesap Planı: 257 ve 770 hesapları",
        "donem_sonu_islemleri",
    ),
    "demo-finansal-055": spec(
        "Maliyeti 90.000 TL, birikmiş amortismanı 60.000 TL olan makine KDV dikkate alınmadan 38.000 TL'ye satılmış ve bedel bankaya yatırılmıştır. Satış kaydı hangisidir?",
        journal("102 BANKALAR              38.000", "257 BİRİKMİŞ AMORTİSMANLAR 60.000", "    253 TESİS, MAKİNE VE CİHAZLAR 90.000", "    679 DİĞER OLAĞANDIŞI GELİR VE KÂR. 8.000"),
        [
            journal("102 BANKALAR              38.000", "257 BİRİKMİŞ AMORTİSMANLAR 60.000", "689 DİĞER OLAĞANDIŞI GİDER VE ZAR. 8.000", "    253 TESİS, MAKİNE VE CİHAZLAR 106.000"),
            journal("102 BANKALAR              38.000", "    253 TESİS, MAKİNE VE CİHAZLAR 30.000", "    679 DİĞER OLAĞANDIŞI GELİR VE KÂR. 8.000"),
            journal("253 TESİS, MAKİNE VE CİHAZLAR 90.000", "    102 BANKALAR                  38.000", "    257 BİRİKMİŞ AMORTİSMANLAR    60.000", "    679 DİĞER OLAĞANDIŞI GELİR VE KÂR. 8.000"),
            journal("102 BANKALAR              38.000", "257 BİRİKMİŞ AMORTİSMANLAR 60.000", "    253 TESİS, MAKİNE VE CİHAZLAR 90.000", "    649 DİĞER OLAĞAN GELİR VE KÂR. 8.000"),
        ],
        "Makinenin defter değeri 90.000 − 60.000 = 30.000 TL'dir. 38.000 TL satış bedeli ile defter değeri arasındaki 8.000 TL kârdır; varlığın maliyeti ve birikmiş amortismanı kayıttan çıkarılır.",
        "TMS 16 Maddi Duran Varlıklar, par. 67-71; Tekdüzen Hesap Planı: 102, 253, 257 ve 679 hesapları",
        "donem_sonu_islemleri",
        "hard",
    ),
    "demo-finansal-056": spec(
        "TMS 38'e göre yararlı ömrü belirsiz olarak değerlendirilen bir maddi olmayan duran varlık için hangi uygulama doğrudur?",
        "Amortisman ayrılmaz; en az yıllık değer düşüklüğü testi yapılır.",
        [
            "Varlık beş yılda tamamen amorti edilir; ayrıca yıllık değer düşüklüğü testi uygulanmaz.",
            "Amortisman ayrılmaz; yalnız elden çıkarılacağı yılda değer düşüklüğü testi yapılır.",
            "Varlık maliyetinde süresiz bırakılır; herhangi bir değer düşüklüğü değerlendirmesi yapılmaz.",
            "Yararlı ömür belirsiz olduğunda bütün maliyet ilk kayıtta doğrudan dönem giderine aktarılır.",
        ],
        "Belirsiz yararlı ömür, ömrün sonsuz olduğu anlamına gelmez. Bu varlık amorti edilmez; değer düşüklüğü testi en az yıllık olarak ve ayrıca gösterge bulunduğunda uygulanır.",
        "TMS 38 Maddi Olmayan Duran Varlıklar, par. 107-110; TMS 36, par. 10",
        "tms_tfrs",
    ),
    "demo-finansal-057": spec(
        "İşletme yeni bir teknolojiye ilişkin araştırma aşamasında 70.000 TL harcamış ve tutarı banka hesabından ödemiştir. TMS 38 ve Tekdüzen Hesap Planına göre kayıt hangisidir?",
        journal("750 ARAŞTIRMA VE GELİŞTİRME GİD. 70.000", "    102 BANKALAR                  70.000"),
        [
            journal("263 ARAŞTIRMA VE GELİŞTİRME GİD. 70.000", "    102 BANKALAR                  70.000"),
            journal("102 BANKALAR              70.000", "    750 ARAŞTIRMA VE GELİŞTİRME GİD. 70.000"),
            journal("150 İLK MADDE VE MALZEME  70.000", "    102 BANKALAR                  70.000"),
            journal("260 HAKLAR                 70.000", "    500 SERMAYE                   70.000"),
        ],
        "Araştırma safhasında gelecekte ekonomik yarar sağlayacak belirlenebilir bir varlık bulunduğu henüz gösterilemez; harcama gerçekleştiği dönemde giderleştirilir. Banka ödemesi 102 hesaba alacak kaydedilir.",
        "TMS 38 Maddi Olmayan Duran Varlıklar, par. 54; Tekdüzen Hesap Planı: 102 ve 750 hesapları",
        "tms_tfrs",
    ),
    "demo-finansal-058": spec(
        "TMS 38'e göre geliştirme aşamasındaki bir proje için yapılan harcamalar hangi durumda maddi olmayan duran varlık olarak aktifleştirilmeye başlanır?",
        "TMS 38'deki geliştirme ölçütlerinin tümü birlikte kanıtlandığında",
        [
            "Yönetim projeyi başlatmaya karar verdiği anda, teknik ve ekonomik koşullar ayrıca kanıtlanmadan",
            "Araştırma aşamasındaki ilk harcamanın yapıldığı tarihten itibaren geriye dönük biçimde",
            "Proje için ilk nakit ödeme yapıldığında, teknik ve ticari değerlendirmeden bağımsız olarak",
            "Proje hukuken tescil edildiğinde, maliyetlerin güvenilir ölçülmesi koşulu aranmadan",
        ],
        "Geliştirme harcaması ancak TMS 38'de sayılan altı koşulun birlikte gösterilebildiği tarihten itibaren aktifleştirilir. Önceki araştırma harcamaları sonradan varlık maliyetine geri alınmaz.",
        "TMS 38 Maddi Olmayan Duran Varlıklar, par. 57 ve 71",
        "tms_tfrs",
        "hard",
    ),
}


ADDITIONS = [
    {
        "id": "yet-finansal-t1-0019",
        **spec(
            "İşletme KDV dâhil 36.000 TL tutarındaki ticari malı peşin satmıştır. KDV oranı %20'dir; satışın maliyet kaydı dikkate alınmayacaktır. Hasılat kaydı hangisidir?",
            journal("100 KASA                  36.000", "    600 YURT İÇİ SATIŞLAR        30.000", "    391 HESAPLANAN KDV             6.000"),
            [
                journal("100 KASA                  36.000", "    600 YURT İÇİ SATIŞLAR        36.000"),
                journal("120 ALICILAR              36.000", "    600 YURT İÇİ SATIŞLAR        30.000", "    391 HESAPLANAN KDV             6.000"),
                journal("600 YURT İÇİ SATIŞLAR     30.000", "191 İNDİRİLECEK KDV        6.000", "    100 KASA                      36.000"),
                journal("100 KASA                  30.000", "191 İNDİRİLECEK KDV        6.000", "    600 YURT İÇİ SATIŞLAR        36.000"),
            ],
            "KDV dâhil tutar 1,20'ye bölünerek matrah bulunur: 36.000 / 1,20 = 30.000 TL. Tahsil edilen 36.000 TL kasa hesabına borç; hasılat 600 ve 6.000 TL hesaplanan KDV 391 hesaba alacak kaydedilir.",
            "Tekdüzen Hesap Planı: 100, 391 ve 600 hesapları",
            "muhasebe_kayitlari",
        ),
        "lessonId": "finansal_muhasebe",
        "isPremium": False,
        "isActive": True,
    },
    {
        "id": "yet-finansal-t1-0020",
        **spec(
            "İşletme üretimde kullanacağı makineyi 240.000 TL + %20 indirilebilir KDV ile satın almış; 12.000 TL taşıma ve 18.000 TL montaj giderine katlanmıştır. TMS 16'ya göre makinenin ilk kayda alma maliyeti kaç TL'dir?",
            "270.000 TL",
            ["240.000 TL", "288.000 TL", "318.000 TL", "324.000 TL"],
            "Makinenin maliyeti satın alma bedeli ile doğrudan ilişkilendirilebilir taşıma ve montaj giderlerinden oluşur: 240.000 + 12.000 + 18.000 = 270.000 TL. İndirilebilir KDV maliyete eklenmez.",
            "TMS 16 Maddi Duran Varlıklar, par. 16-17",
            "tms_tfrs",
            "medium",
        ),
        "lessonId": "finansal_muhasebe",
        "isPremium": False,
        "isActive": True,
    },
]


MISSING_REFS = {
    "demo-finansal-004": "Tekdüzen Hesap Planı: 120, 391 ve 600 hesapları",
    "demo-finansal-005": "TMS 2 Stoklar, par. 10-11; Tekdüzen Hesap Planı: 100, 153 ve 191 hesapları",
    "demo-finansal-006": "Tekdüzen Hesap Planı: 102 ve 120 hesapları",
    "demo-finansal-007": "Tekdüzen Hesap Planı: 121 ve 642 hesapları",
    "demo-finansal-008": "Tekdüzen Hesap Planı: 120, 128, 129 ve 654 hesapları",
    "demo-finansal-009": "TMS 2 Stoklar, par. 25 ve 27",
    "demo-finansal-011": "TMS 2 Stoklar; dönemsel stok maliyeti eşitliği",
    "demo-finansal-012": "TMS 16, par. 50; Tekdüzen Hesap Planı: 257 ve 760 hesapları",
    "demo-finansal-013": "Tekdüzen Hesap Planı: 180 ve 760 hesapları; dönemsellik kavramı",
    "demo-finansal-014": "Tekdüzen Hesap Planı: 181 ve 642 hesapları; tahakkuk esası",
    "demo-finansal-016": "TMS 2 Stoklar, par. 28-33",
    "demo-finansal-017": "TMS 16 Maddi Duran Varlıklar, par. 39",
    "demo-finansal-018": "TMS 38 Maddi Olmayan Duran Varlıklar, par. 54 ve 57",
    "demo-finansal-019": "1 Sıra No.lu MSUGT, Muhasebenin Temel Kavramları: ihtiyatlılık",
}

# Mevcut iyi soruların doğru metnini değiştirmeden, çeldiricileri aynı kavramsal
# kategori ve dil yapısında dengeler. Amaç karakter doldurmak değil, seçeneklerin
# ölçtüğü hatayı karşılaştırılabilir biçimde ifade etmektir.
BALANCED_DISTRACTORS = {
    "demo-finansal-024": [
        "Bankalar borç, Tesis Makine ve Cihazlar alacak",
        "Genel Yönetim Giderleri borç, Bankalar alacak",
        "Ticari Mallar borç, Bankalar alacak",
        "Tesis Makine ve Cihazlar borç, Sermaye alacak",
    ],
    "demo-finansal-033": [
        "48.000 TL üzerinden ölçülür ve değer düşüklüğü kaydı yapılmaz",
        "43.000 TL üzerinden ölçülür fakat değer düşüklüğü kaydı yapılmaz",
        "48.000 TL üzerinden ölçülür ve 5.000 TL değer düşüklüğü ayrılır",
        "5.000 TL üzerinden ölçülür ve 43.000 TL değer düşüklüğü ayrılır",
    ],
    "demo-finansal-034": [
        "Normal kapasiteye göre dağıtılan sabit genel üretim giderleri",
        "Stokları mevcut konumuna getiren doğrudan taşıma giderleri",
        "Üretimle doğrudan ilişkili ilk madde ve işçilik giderleri",
        "Üretimin zorunlu parçası olan değişken genel üretim giderleri",
    ],
    "demo-finansal-042": [
        "Muhasebenin dönemsellik varsayımı",
        "Finansal raporlamada ihtiyatlılık ilkesi",
        "Raporlama işletmesi kavramı",
        "Finansal bilginin önemlilik özelliği",
    ],
}


def gen_letters(seed: int) -> list[str]:
    rng = random.Random(seed)
    letters = list("ABCDE") * 4
    while True:
        rng.shuffle(letters)
        seq = "".join(letters)
        if not any(seq[i] == seq[i - 1] == seq[i - 2] for i in range(2, len(seq))):
            return letters[:]


def assert_balanced_journal(item: dict) -> None:
    """Doğru şık tam yevmiye biçimindeyse borç/alacak toplamını doğrular."""
    answer = item["choices"][item["correctAnswer"]]
    if not answer.startswith("```text\n"):
        return

    debit = 0
    credit = 0
    for line in answer.removeprefix("```text\n").removesuffix("\n```").splitlines():
        match = re.search(r"([0-9][0-9.]*)\s*$", line)
        assert match, (item["id"], line)
        amount = int(match.group(1).replace(".", ""))
        if line.startswith("    "):
            credit += amount
        else:
            debit += amount
    assert debit == credit, (item["id"], debit, credit)


def normalize(item: dict, journal_question: bool) -> None:
    item["lessonId"] = "finansal_muhasebe"
    item["topicId"] = TOPIC_ALIASES.get(item["topicId"], item["topicId"])
    source = item.setdefault("source", {})
    source["kind"] = "generated"
    source["styleRef"] = "2026/1 beş seçenekli test biçimi"
    if not source.get("legislationRef"):
        source["legislationRef"] = MISSING_REFS.get(item["id"], "Finansal Muhasebe müfredatı ve yürürlükteki mesleki düzenlemeler")

    tags = ["Özgün Soru", "2026 Formatı", "Bölüm Havuzu", "Finansal Muhasebe"]
    if journal_question:
        tags.append("kayıt")
    item["tags"] = tags
    item["updatedAt"] = UPDATED_AT
    item["examPeriod"] = "2026 test sistemine uyumlu özgün soru"
    item["legislationVersion"] = LEGISLATION_VERSION
    item["sourceUpdatedAt"] = UPDATED_AT
    item["isActive"] = True


def rebuild(filename: str, seed: int) -> list[dict]:
    path = CONTENT / filename
    items = json.loads(path.read_text(encoding="utf-8"))
    by_id = {item["id"]: item for item in items}

    for question_id, replacement in REPLACEMENTS.items():
        if question_id not in by_id:
            continue
        preserved = {
            "id": question_id,
            "lessonId": by_id[question_id].get("lessonId", "finansal_muhasebe"),
            "isPremium": by_id[question_id].get("isPremium", False),
            "isActive": True,
        }
        by_id[question_id].clear()
        by_id[question_id].update(preserved)
        by_id[question_id].update(replacement)

    if filename == "questions_finansal_muhasebe_2026.json":
        known = set(by_id)
        for addition in ADDITIONS:
            if addition["id"] not in known:
                items.append(dict(addition))
                by_id[addition["id"]] = items[-1]

    for item in items:
        if item["id"] not in BALANCED_DISTRACTORS:
            continue
        correct = item["choices"][item["correctAnswer"]]
        distractors = BALANCED_DISTRACTORS[item["id"]]
        assert len({correct, *distractors}) == 5
        item["choices"] = dict(zip("ABCDE", [correct, *distractors]))
        item["correctAnswer"] = "A"

    journal_ids = JOURNAL_IDS[filename]
    for item in items:
        normalize(item, item["id"] in journal_ids)

    letters = gen_letters(seed)
    for item, answer in zip(items, letters):
        old_answer = item["correctAnswer"]
        correct = item["choices"][old_answer]
        distractors = [item["choices"][key] for key in "ABCDE" if key != old_answer]
        choices = {answer: correct}
        for key, value in zip((key for key in "ABCDE" if key != answer), distractors):
            choices[key] = value
        item["choices"] = {key: choices[key] for key in "ABCDE"}
        item["correctAnswer"] = answer
        assert_balanced_journal(item)

    assert len(items) == 20, (filename, len(items))
    assert len(journal_ids) == 11
    assert sum("kayıt" in item["tags"] for item in items) == 11
    assert not [item["id"] for item in items if PREMISE_MARK.search(item["question"])]
    assert len({item["id"] for item in items}) == 20
    assert len({item["question"] for item in items}) == 20
    assert all(item["topicId"] in VALID_TOPIC_IDS for item in items)
    assert all("Konu Havuzu" not in item["tags"] for item in items)
    return items


def write(path: Path, data: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    all_ids: set[str] = set()
    all_questions: set[str] = set()
    for filename, seed in FILES.items():
        data = rebuild(filename, seed)
        ids = {item["id"] for item in data}
        questions = {item["question"] for item in data}
        assert not all_ids.intersection(ids), (filename, all_ids.intersection(ids))
        assert not all_questions.intersection(questions), (filename, all_questions.intersection(questions))
        all_ids.update(ids)
        all_questions.update(questions)
        write(CONTENT / filename, data)
        write(APP_CONTENT / filename, data)
        print(
            f"{filename}: {len(data)} soru | "
            f"kayıt {sum('kayıt' in item['tags'] for item in data)} | "
            f"öncüllü {sum(bool(PREMISE_MARK.search(item['question'])) for item in data)} | "
            f"harf {''.join(item['correctAnswer'] for item in data)}"
        )


if __name__ == "__main__":
    main()
