#!/usr/bin/env python3
"""Finansal Muhasebe için uzman incelemeli anlamsal kalite yamaları.

İlk on altı konu paketindeki aynı kazanımı aynı yönden ölçen tekrarları daha
uygulamalı ve ayırt edici senaryolara dönüştürür; incelemede bulunan maddi
hataları düzeltir. Sorular 1 Sıra No'lu MSUGT, TMS 7 ve 2024-2026 SGS soru
dili esas alınarak özgün yazılmıştır.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/finansal_muhasebe/muhasebenin_temel_kavramlari.json"
PROCESS_RELATIVE_PATH = "content/finansal_muhasebe/muhasebe_sureci_hesap_plani.json"
# hazir_degerler.json -> build_fm_hazir_degerler_cok_adimli.py (tek sahip)
# stoklar.json -> build_fm_stoklar_cok_adimli.py (tek sahip)
# ticari_alacaklar.json -> build_fm_ticari_alacaklar_cok_adimli.py (tek sahip)
# menkul_kiymetler.json -> build_fm_menkul_kiymetler_cok_adimli.py (tek sahip)
# maddi_duran_varliklar.json -> build_fm_mdv_cok_adimli.py (tek sahip)
INTANGIBLE_RELATIVE_PATH = "content/finansal_muhasebe/maddi_olmayan_duran_varliklar.json"
FINANCIAL_INVESTMENT_RELATIVE_PATH = "content/finansal_muhasebe/mali_duran_varliklar.json"
# yabanci_kaynaklar.json -> build_fm_yabanci_kaynaklar_cok_adimli.py (tek sahip)
# ozkaynaklar.json -> build_fm_ozkaynaklar_cok_adimli.py (tek sahip)
INCOME_STATEMENT_RELATIVE_PATH = "content/finansal_muhasebe/gelir_tablosu_hesaplari.json"
COST_ACCOUNTS_RELATIVE_PATH = "content/finansal_muhasebe/maliyet_hesaplari.json"
# donem_sonu_islemleri.json -> build_fm_donem_sonu_cok_adimli.py (tek sahip)
CURRENCY_DIFFERENCES_RELATIVE_PATH = "content/finansal_muhasebe/kur_farklari.json"
# kdv_muhasebesi.json -> build_fm_kdv_cok_adimli.py (tek sahip)


def patch(stem: str, options: dict[str, str], answer: str, solution: str, concept: str) -> dict:
    return {
        "stem": stem,
        "options": options,
        "answer": answer,
        "solution": solution,
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (uygulama ve yorum; 2024-2026 sınav diline kalibre)",
            "legislationRef": f"1 Sıra No'lu MSUGT - Muhasebenin Temel Kavramları ({concept})",
        },
        "validYear": 2026,
        "mockExamId": None,
    }


def ppe_patch(
    stem: str,
    options: dict[str, str],
    answer: str,
    solution: str,
    legislation_ref: str,
) -> dict:
    return {
        "stem": stem,
        "options": options,
        "answer": answer,
        "solution": solution,
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (MDV uygulama ve yorum; 2024-2026 sınav diline kalibre)",
            "legislationRef": legislation_ref,
        },
        "validYear": 2026,
        "mockExamId": None,
    }


def intangible_patch(
    stem: str,
    options: dict[str, str],
    answer: str,
    solution: str,
    legislation_ref: str,
) -> dict:
    return {
        "stem": stem,
        "options": options,
        "answer": answer,
        "solution": solution,
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (MODV uygulama ve yorum; 2024-2026 sınav diline kalibre)",
            "legislationRef": legislation_ref,
        },
        "validYear": 2026,
        "mockExamId": None,
    }


def financial_investment_patch(
    stem: str,
    options: dict[str, str],
    answer: str,
    solution: str,
    legislation_ref: str,
) -> dict:
    return {
        "stem": stem,
        "options": options,
        "answer": answer,
        "solution": solution,
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (Mali Duran Varlıklar uygulama ve yorum; 2024-2026 sınav diline kalibre)",
            "legislationRef": legislation_ref,
        },
        "validYear": 2026,
        "mockExamId": None,
    }


def liability_patch(
    stem: str,
    options: dict[str, str],
    answer: str,
    solution: str,
    legislation_ref: str,
) -> dict:
    return {
        "stem": stem,
        "options": options,
        "answer": answer,
        "solution": solution,
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (Yabancı Kaynaklar uygulama ve yorum; 2024-2026 sınav diline kalibre)",
            "legislationRef": legislation_ref,
        },
        "validYear": 2026,
        "mockExamId": None,
    }


def equity_patch(
    stem: str,
    options: dict[str, str],
    answer: str,
    solution: str,
    legislation_ref: str,
) -> dict:
    return {
        "stem": stem,
        "options": options,
        "answer": answer,
        "solution": solution,
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (Özkaynaklar uygulama ve yorum; 2024-2026 sınav diline kalibre)",
            "legislationRef": legislation_ref,
        },
        "validYear": 2026,
        "mockExamId": None,
    }


def income_statement_patch(
    stem: str,
    options: dict[str, str],
    answer: str,
    solution: str,
    legislation_ref: str,
) -> dict:
    return {
        "stem": stem,
        "options": options,
        "answer": answer,
        "solution": solution,
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (Gelir Tablosu uygulama ve yorum; 2024-2026 sınav diline kalibre)",
            "legislationRef": legislation_ref,
        },
        "validYear": 2026,
        "mockExamId": None,
    }


def cost_accounts_patch(
    stem: str,
    options: dict[str, str],
    answer: str,
    solution: str,
    legislation_ref: str,
) -> dict:
    return {
        "stem": stem,
        "options": options,
        "answer": answer,
        "solution": solution,
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (Maliyet Hesapları uygulama ve yorum; 2024-2026 sınav diline kalibre)",
            "legislationRef": legislation_ref,
        },
        "validYear": 2026,
        "mockExamId": None,
    }


def period_end_patch(
    stem: str,
    options: dict[str, str],
    answer: str,
    solution: str,
    legislation_ref: str,
) -> dict:
    return {
        "stem": stem,
        "options": options,
        "answer": answer,
        "solution": solution,
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (Dönem Sonu İşlemleri uygulama ve yorum; 2024-2026 sınav diline kalibre)",
            "legislationRef": legislation_ref,
        },
        "validYear": 2026,
        "mockExamId": None,
    }


def currency_differences_patch(
    stem: str,
    options: dict[str, str],
    answer: str,
    solution: str,
    legislation_ref: str,
) -> dict:
    return {
        "stem": stem,
        "options": options,
        "answer": answer,
        "solution": solution,
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (Kur Farkları uygulama ve yorum; 2024-2026 sınav diline kalibre)",
            "legislationRef": legislation_ref,
        },
        "validYear": 2026,
        "mockExamId": None,
    }


def kdv_accounting_patch(
    stem: str,
    options: dict[str, str],
    answer: str,
    solution: str,
    legislation_ref: str,
) -> dict:
    return {
        "stem": stem,
        "options": options,
        "answer": answer,
        "solution": solution,
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (KDV Muhasebesi uygulama ve yorum; 2024-2026 sınav diline kalibre)",
            "legislationRef": legislation_ref,
        },
        "validYear": 2026,
        "mockExamId": None,
    }


PATCHES = {
    "finmuh-temelkavram-gen-0024": patch(
        "İşletme yönetimi, kredi başvurusunda daha güçlü görünmek için dönem giderlerinin bir bölümünün gelecek döneme aktarılmasını istemektedir. Muhasebe sorumlusu, yalnız işletme sahibinin çıkarını değil kredi verenler ve diğer bilgi kullanıcılarını da gözeterek bu talebi reddetmiştir.\n\nBu tutum öncelikle hangi kavramın gereğidir?",
        {
            "A": "Sosyal Sorumluluk",
            "B": "Maliyet Esası",
            "C": "Kişilik",
            "D": "Süreklilik",
            "E": "Parayla Ölçülme",
        },
        "A",
        "Muhasebe yalnız işletme sahibinin değil, kredi verenler dâhil bütün bilgi kullanıcılarının çıkarını gözeterek güvenilir bilgi üretmelidir. Kârı güçlü göstermek amacıyla gideri ertelemeyi reddetmek **Sosyal Sorumluluk Kavramı**nın gereğidir.",
        "Sosyal Sorumluluk",
    ),
    "finmuh-temelkavram-gen-0031": patch(
        "Toplam varlıkları 80.000.000 ₺ olan bir işletme, yönetim kurulu başkanına 25.000 ₺ tutarında faizsiz borç vermiştir. Tutar işletme ölçeğine göre küçük olsa da işlemin ilişkili tarafla yapılması, kullanıcıların değerlendirmesini etkileyebilecek niteliktedir.\n\nBu işlemin yalnız tutarına bakılarak önemsiz sayılmaması hangi kavramla açıklanır?",
        {
            "A": "Maliyet Esası",
            "B": "Önemlilik",
            "C": "Dönemsellik",
            "D": "Süreklilik",
            "E": "Parayla Ölçülme",
        },
        "B",
        "Önemlilik yalnız parasal büyüklüğe göre belirlenmez. İlişkili taraf işlemi, tutarı küçük olsa bile niteliği nedeniyle kullanıcı kararlarını etkileyebilir. Bu nedenle işlem **Önemlilik Kavramı** kapsamında değerlendirilir.",
        "Önemlilik",
    ),
    "finmuh-temelkavram-gen-0032": patch(
        "Bir hizmet giderine ait fatura henüz işletmeye ulaşmamıştır. Muhasebe sorumlusu, yalnız yöneticinin sözlü beyanıyla kayıt yapmak yerine imzalı sözleşmeyi, hizmet kabul tutanağını, banka ödeme kaydını ve karşı taraf teyidini inceleyerek işlemi doğrulamıştır.\n\nBu yaklaşım öncelikle hangi kavramın gereğidir?",
        {
            "A": "Tutarlılık",
            "B": "Tam Açıklama",
            "C": "İhtiyatlılık",
            "D": "Tarafsızlık ve Belgelendirme",
            "E": "Maliyet Esası",
        },
        "D",
        "Bir işlemin kanıtı yalnız faturadan ibaret değildir; sözleşme, kabul tutanağı, banka kaydı ve teyit gibi objektif belgeler de işlemi destekleyebilir. Kaydın kişisel beyan yerine doğrulanabilir kanıta dayanması **Tarafsızlık ve Belgelendirme Kavramı**nın gereğidir.",
        "Tarafsızlık ve Belgelendirme",
    ),
    "finmuh-temelkavram-gen-0033": patch(
        "İşletme, stok maliyetlerini daha güvenilir sunan yeni bir yönteme geçmek için haklı bir gerekçe belirlemiş; değişikliğin nedenini ve mali tablolara etkisini dipnotlarda açıklamıştır.\n\nBu uygulama Tutarlılık Kavramı bakımından nasıl değerlendirilir?",
        {
            "A": "Yöntem değişikliği yapılamayacağından kavrama aykırıdır.",
            "B": "Yalnız vergi matrahı azalıyorsa yöntem değişikliği yapılabilir.",
            "C": "Haklı neden ve açıklama bulunduğu için kavramla uyumludur.",
            "D": "Her dönem farklı yöntem seçmek Tutarlılık Kavramının gereğidir.",
            "E": "Tutarlılık yalnız kasa ve banka hesapları için geçerlidir.",
        },
        "C",
        "Tutarlılık, muhasebe yöntemlerinin keyfî biçimde değiştirilmesini önler; haklı bir neden varsa değişiklik yapılmasına engel değildir. Nedenin ve finansal etkinin açıklanması hâlinde uygulama **Tutarlılık Kavramı**yla uyumludur.",
        "Tutarlılık",
    ),
    "finmuh-temelkavram-gen-0040": patch(
        "Aralık ayına ait elektrik gideri belgeye bağlanmıştır. Yönetici dönem kârını yüksek göstermek için kaydın ocak ayına bırakılmasını istemesine rağmen muhasebe sorumlusu, kişisel hedeften etkilenmeden belge ve gerçekleşen hizmet dönemini esas almıştır.\n\nKayıtta yönetimin kâr hedefinden etkilenilmemesi öncelikle hangi kavramla ilgilidir?",
        {
            "A": "Tarafsızlık ve Belgelendirme",
            "B": "Kişilik",
            "C": "Maliyet Esası",
            "D": "Süreklilik",
            "E": "Parayla Ölçülme",
        },
        "A",
        "Muhasebe kayıtları yönetimin dönem kârına ilişkin isteğine göre değil, gerçek durumu gösteren objektif belgelere göre yapılmalıdır. Bu tarafsız tutum **Tarafsızlık ve Belgelendirme Kavramı**nın gereğidir. Giderin aralık dönemine yazılması ayrıca dönemsellikle uyumludur.",
        "Tarafsızlık ve Belgelendirme",
    ),
    "finmuh-temelkavram-gen-0041": patch(
        "Bir üretim işletmesinin çevreyi eski hâline getirme yükümlülüğü finansal durumunu etkileyebilecek düzeydedir. İşletme sahibi bu bilginin gizlenmesini istemiş; muhasebe sorumlusu ise yatırımcılar, çalışanlar, kredi verenler, devlet ve kamuoyunun güvenilir bilgi ihtiyacını gözetmiştir.\n\nYükümlülüğün nasıl ölçüleceğinden bağımsız olarak, bütün ilgili kesimlerin çıkarının gözetilmesi hangi kavramdır?",
        {
            "A": "Özün Önceliği",
            "B": "Sosyal Sorumluluk",
            "C": "Maliyet Esası",
            "D": "Kişilik",
            "E": "Tutarlılık",
        },
        "B",
        "Muhasebenin bilgi üretirken yalnız işletme sahibini değil, işletmeyle ilgili bütün kesimleri ve kamu yararını gözetmesi **Sosyal Sorumluluk Kavramı**dır. Soru yükümlülüğün ölçümünü değil, bilgi kullanıcılarına karşı sorumluluğu ölçmektedir.",
        "Sosyal Sorumluluk",
    ),
    "finmuh-temelkavram-gen-0049": patch(
        "Bir muhasebe hatası, 100.000.000 ₺ toplam varlığa sahip işletmede yalnız 8.000 ₺ tutarındadır; ancak düzeltilmediğinde 3.000 ₺ dönem kârı, 5.000 ₺ dönem zararına dönüşmektedir.\n\nÖnemlilik Kavramına göre en uygun değerlendirme hangisidir?",
        {
            "A": "Tutar toplam varlıklara göre küçük olduğu için hata önemli değildir.",
            "B": "Kârı zarara dönüştürdüğü için hata niteliği bakımından önemli kabul edilebilir.",
            "C": "Yalnız nakit işlemlerindeki hatalar önemli sayılabilir.",
            "D": "Önemlilik yalnız belgenin kaç sayfa olduğuna göre belirlenir.",
            "E": "Hata tutarı ne olursa olsun bütün hatalar mali tabloları aynı ölçüde etkiler.",
        },
        "B",
        "Bir kalemin önemi yalnız büyüklüğüne değil, kullanıcı kararını etkileyebilecek **niteliğine** de bağlıdır. Hatanın sonucu kârdan zarara çevirmesi kararları etkileyebileceğinden, 8.000 ₺ tutarındaki hata **önemli** kabul edilebilir.",
        "Önemlilik",
    ),
    "finmuh-temelkavram-gen-0053": patch(
        "Bir perakendecinin deposunda, satılıncaya kadar mülkiyeti ve başlıca riskleri tedarikçide kalan konsinye mallar bulunmaktadır. Mallar fiziksel olarak depoda olsa da perakendeci bunları kendi stoku olarak kaydetmemiştir.\n\nBu uygulama hangi kavrama dayanır?",
        {
            "A": "Kişilik",
            "B": "Dönemsellik",
            "C": "Maliyet Esası",
            "D": "Özün Önceliği",
            "E": "Önemlilik",
        },
        "D",
        "Malın işletmenin deposunda bulunması tek başına ekonomik sahipliği göstermez. Mülkiyet ve başlıca riskler tedarikçide kaldığından, işlemin fiziksel görünümü yerine ekonomik özü esas alınır. Bu, **Özün Önceliği Kavramı**dır.",
        "Özün Önceliği",
    ),
    "finmuh-temelkavram-gen-0057": patch(
        "İşletme, hâkim ortağına ait bir taşınmazı piyasa koşullarından önemli ölçüde farklı bir bedelle kiralamıştır. İşlem yasal defterlere kaydedilmiş; kullanıcıların işlemin niteliğini değerlendirebilmesi için ilişkili taraf, bedel ve temel koşullar dipnotlarda ayrıca açıklanmıştır.\n\nDipnot açıklaması öncelikle hangi kavramın gereğidir?",
        {
            "A": "Süreklilik",
            "B": "Parayla Ölçülme",
            "C": "Tam Açıklama",
            "D": "Maliyet Esası",
            "E": "Kişilik",
        },
        "C",
        "Kayıtlı tutar tek başına, ilişkili tarafla yapılan işlemin kullanıcı açısından taşıdığı anlamı göstermeyebilir. İşlemin tarafı ve koşullarının dipnotta sunulması, kullanıcıya yeterli bilgi verilmesini amaçlayan **Tam Açıklama Kavramı**nın gereğidir.",
        "Tam Açıklama",
    ),
    "finmuh-temelkavram-gen-0060": patch(
        "Sosyal Sorumluluk Kavramıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Muhasebe bilgisi hazırlanırken yalnız işletme sahibinin kısa vadeli çıkarı gözetilir.\n\nII. Yatırımcı, çalışan, kredi veren, devlet ve kamuoyu gibi ilgili kesimlerin güvenilir bilgi ihtiyacı dikkate alınır.\n\nIII. İşletme aleyhine olan önemli bilgiler, yaptırım beklenmiyorsa kullanıcılardan gizlenebilir.",
        {
            "A": "Yalnız I",
            "B": "Yalnız II",
            "C": "I ve II",
            "D": "II ve III",
            "E": "I, II ve III",
        },
        "B",
        "Sosyal sorumluluk, yalnız işletme sahibinin çıkarını değil bütün ilgili kesimlerin güvenilir bilgi ihtiyacını gözetir; bu nedenle **II doğrudur**. Bilgiyi sahibin kısa vadeli çıkarına göre hazırlamak (I) ve önemli olumsuz bilgiyi gizlemek (III) kavrama aykırıdır. Doğru cevap **Yalnız II**dir.",
        "Sosyal Sorumluluk",
    ),
}


PROCESS_PATCHES = {
    "finmuh-surec-gen-0032": {
        "stem": "İşletmenin 400 BANKA KREDİLERİ hesabında izlenen uzun vadeli kredisinin 90.000 ₺ tutarındaki anapara taksiti, bilanço tarihinden itibaren gelecek on iki ay içinde ödenecektir. Dönem sonundaki vade aktarımı için aşağıdaki kayıtlardan hangisi uygundur?",
        "options": {
            "A": "303 Uzun Vadeli Kredilerin Anapara Taksitleri ve Faizleri (B) 90.000 / 400 Banka Kredileri (A) 90.000",
            "B": "400 Banka Kredileri (B) 90.000 / 303 Uzun Vadeli Kredilerin Anapara Taksitleri ve Faizleri (A) 90.000",
            "C": "300 Banka Kredileri (B) 90.000 / 400 Banka Kredileri (A) 90.000",
            "D": "780 Finansman Giderleri (B) 90.000 / 400 Banka Kredileri (A) 90.000",
            "E": "400 Banka Kredileri (B) 90.000 / 102 Bankalar (A) 90.000",
        },
        "answer": "B",
        "solution": "Gelecek on iki ayda ödenecek uzun vadeli kredi taksiti artık kısa vadeli yabancı kaynak niteliğindedir. Bu nedenle **400 Banka Kredileri borçlandırılarak azaltılır**, **303 Uzun Vadeli Kredilerin Anapara Taksitleri ve Faizleri alacaklandırılarak artırılır**. Henüz ödeme yapılmadığı için 102 Bankalar kullanılmaz.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (vade sınıflaması ve yevmiye kaydı)",
            "legislationRef": "1 Sıra No'lu MSUGT - Tekdüzen Hesap Planı (303 ve 400 hesapları)",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-surec-gen-0035": {
        "stem": "Bir alış işlemi yevmiye defterine hiç kaydedilmemiştir. İşlemin hem borç hem alacak tarafı birlikte eksik kaldığından dönem sonunda düzenlenen mizanın borç ve alacak toplamları yine eşit çıkmıştır.\n\nBu durum mizan kontrolü bakımından neyi gösterir?",
        "options": {
            "A": "Mizan eşitse bütün işlemlerin eksiksiz kaydedildiği kesinleşir.",
            "B": "Mizan yalnızca kasa hesabındaki hataları ortaya çıkarır.",
            "C": "Eşitlik, her hesabın doğru hesap koduyla kullanıldığını kanıtlar.",
            "D": "İki tarafı birlikte etkileyen eksiklikler eşitliği bozmayabilir; mizan tek başına tam doğruluk kanıtı değildir.",
            "E": "Borç ve alacak toplamlarının eşit olması muhasebe sisteminde hata bulunduğunu gösterir.",
        },
        "answer": "D",
        "solution": "Bir işlem tamamen atlanırsa borç ve alacak tarafları aynı tutarda eksik kalır; bu nedenle mizan eşitliği bozulmayabilir. Mizan, aritmetik eşitliği sınar ancak **işlem atlama, yanlış hesap kullanma veya iki tarafı eşit etkileyen hataları tek başına ortaya çıkaramaz**.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (mizan kontrolü ve hata analizi)",
            "legislationRef": "1 Sıra No'lu MSUGT - Muhasebe Süreci ve Mizan",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-surec-gen-0037": {
        "stem": "Tekdüzen Hesap Planı'ndaki 253 TESİS, MAKİNE VE CİHAZLAR hesabının kod yapısıyla ilgili aşağıdaki ifadelerden hangisi doğrudur?",
        "options": {
            "A": "İlk rakam olan 2 hesap sınıfını, ilk iki rakam olan 25 hesap grubunu, 253 ise büyük defter hesabını gösterir.",
            "B": "İlk rakam muavin hesabı, son rakam hesap sınıfını gösterir.",
            "C": "25 kodu gelir tablosu hesap sınıfını gösterir.",
            "D": "253 yalnızca nazım hesaplarda kullanılabilen serbest bir koddur.",
            "E": "Hesap kodundaki rakamların sınıf, grup ve hesap bakımından herhangi bir anlamı yoktur.",
        },
        "answer": "A",
        "solution": "Tekdüzen Hesap Planı hiyerarşiktir: **2 Duran Varlıklar** hesap sınıfını, **25 Maddi Duran Varlıklar** hesap grubunu, **253 Tesis, Makine ve Cihazlar** ise büyük defter hesabını gösterir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (hesap kodu hiyerarşisi)",
            "legislationRef": "1 Sıra No'lu MSUGT - Tekdüzen Hesap Çerçevesi ve Hesap Planı",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-surec-gen-0041": {
        "stem": "Bir satış faturası sisteme bir kez girildiğinde satış geliri, ticari alacak ve stok kayıtları yetkiler çerçevesinde otomatik olarak güncellenmektedir. Aynı verinin farklı birimlerde yeniden girilmesi gerekmemektedir.\n\nBu yapı muhasebe bilgi sistemi açısından öncelikle hangi yararı sağlar?",
        "options": {
            "A": "Her birimin aynı işlemi bağımsız ve farklı tutarlarla kaydetmesini sağlar.",
            "B": "Belge ve kullanıcı kontrollerine ihtiyaç bırakmadan bütün kayıtları kendiliğinden doğru kabul eder.",
            "C": "Tekrarlı veri girişini azaltır; kayıtlar arasındaki bütünlük ve tutarlılığı destekler.",
            "D": "Muhasebe kayıtlarının yalnız dönem sonunda topluca yapılmasını zorunlu kılar.",
            "E": "Satış işlemlerinin finansal tablolara aktarılmasını engeller.",
        },
        "answer": "C",
        "solution": "Bir işlemin kaynağında bir kez kaydedilip ilgili alt sistemlere aktarılması, tekrarlı veri girişini ve aktarım hatalarını azaltır. Entegrasyon böylece **veri bütünlüğünü ve kayıtlar arası tutarlılığı** destekler; yetkilendirme ve diğer kontroller yine gereklidir.",
        "source": {
            "kind": "generated",
            "styleRef": "2026 SGS muhasebe bilgi sistemi kazanımı (özgün uygulama)",
            "legislationRef": "Muhasebe Bilgi Sistemleri - bütünleşik işlem işleme ve veri bütünlüğü",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-surec-gen-0042": {
        "stem": "İşletme, yönetim biriminde kullanılan bir demirbaş için dönem sonunda 8.000 ₺ amortisman ayırmıştır. Birikmiş amortisman hesabının kullanıldığı yönteme ve gider yerine göre bu işlemin kaydı aşağıdakilerden hangisidir?",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (yevmiye kaydı; amortisman)",
            "legislationRef": "1 Sıra No'lu MSUGT - 255, 257 ve 770 hesaplarının işleyişi",
        },
    },
    "finmuh-surec-gen-0057": {
        "stem": "Bir işletmede aynı kullanıcı yeni satıcı kartı açabilmekte, bu satıcı adına faturayı sisteme girebilmekte ve ödemeyi de tek başına onaylayabilmektedir.\n\nBu durumdaki temel iç kontrol zayıflığı aşağıdakilerden hangisidir?",
        "options": {
            "A": "Numaralandırılmış belge kullanılmaması",
            "B": "Görevlerin ayrılığı ilkesine uyulmaması",
            "C": "Dönemsellik kavramının uygulanması",
            "D": "Çift taraflı kayıt yönteminin kullanılması",
            "E": "Hesap planında muavin hesap açılması",
        },
        "answer": "B",
        "solution": "Satıcı tanımlama, borç kaydı oluşturma ve ödeme onayı görevlerinin aynı kişide birleşmesi, sahte satıcı ve yetkisiz ödeme riskini artırır. Yetki ve sorumlulukların farklı kişilere dağıtılması **görevlerin ayrılığı** kontrolüdür.",
        "source": {
            "kind": "generated",
            "styleRef": "2026 SGS muhasebe bilgi sistemi kazanımı (özgün iç kontrol senaryosu)",
            "legislationRef": "Muhasebe Bilgi Sistemleri - erişim kontrolleri ve görevlerin ayrılığı",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-surec-gen-0059": {
        "stem": "Muhasebe bilgi sisteminde her kaydın belge numarası, kaydı oluşturan kullanıcı, tarih-saat bilgisi ve sonradan yapılan değişiklikleri saklanmaktadır.\n\nBu bilgilerin birlikte tutulması aşağıdakilerden hangisini sağlar?",
        "options": {
            "A": "Kayıtların kaynağından mali tablolara ve geriye doğru izlenebilmesini sağlayan denetim izi",
            "B": "Kullanıcıların geçmiş kayıtları iz bırakmadan değiştirebilmesi",
            "C": "Her işlemin yalnız sözlü beyana dayanarak kaydedilmesi",
            "D": "Borç ve alacak eşitliği aranmadan tek taraflı kayıt yapılması",
            "E": "Kaynak belgelerin sistemden bağımsız olarak yok edilmesi",
        },
        "answer": "A",
        "solution": "Belge numarası, kullanıcı, zaman damgası ve değişiklik geçmişi; işlemin kaynağından rapora, rapordan kaynak belgeye kadar izlenmesini sağlar. Bu kayıt zinciri **denetim izi (audit trail)** olarak adlandırılır.",
        "source": {
            "kind": "generated",
            "styleRef": "2026 SGS muhasebe bilgi sistemi kazanımı (özgün denetim izi senaryosu)",
            "legislationRef": "Muhasebe Bilgi Sistemleri - işlem kayıtları ve denetim izi",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-surec-gen-0060": {
        "stem": "İşletme 120.000 ₺ tutarındaki bir makineyi satın almış; bedelin 40.000 ₺'sini bankadan ödemiş, kalan 80.000 ₺ için satıcıya borçlanmıştır. KDV ihmal edilecektir.\n\nBu işlemin temel muhasebe eşitliğine etkisi hangisidir?",
        "options": {
            "A": "Varlıklar 120.000 ₺, özkaynaklar 120.000 ₺ artar; borçlar değişmez.",
            "B": "Varlıklar 40.000 ₺ azalır, borçlar 80.000 ₺ artar; özkaynaklar 120.000 ₺ azalır.",
            "C": "Varlıklar ve borçlar 120.000 ₺ artar; banka hesabındaki azalış dikkate alınmaz.",
            "D": "Varlıklar net 80.000 ₺, yabancı kaynaklar 80.000 ₺ artar; özkaynaklar değişmez.",
            "E": "Yalnız varlıkların bileşimi değişir; toplam varlık ve borçlar değişmez.",
        },
        "answer": "D",
        "solution": "Makine 120.000 ₺ artarken banka 40.000 ₺ azalır; varlıklardaki **net artış 80.000 ₺**dir. Satıcıya 80.000 ₺ borç doğduğundan yabancı kaynaklar da 80.000 ₺ artar. İşlem gelir veya gider yaratmadığı için özkaynak değişmez.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (çok adımlı işlem etkisi)",
            "legislationRef": "1 Sıra No'lu MSUGT - temel muhasebe eşitliği ve hesapların işleyişi",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
}


INTANGIBLE_PATCHES = {
    "finmuh-modv-gen-0003": intangible_patch(
        "Bilgisayar kontrollü bir üretim makinesi, kendisine özgü yazılım olmadan çalışamamaktadır. Yazılım makineden bağımsız kullanılamamaktadır. TMS 38 ve TMS 16'ya göre yazılım nasıl sınıflandırılır?",
        {
            "A": "Donanımdan ayrı kullanılıp kullanılamadığına bakılmaksızın, fiziksel niteliği bulunmadığı için her durumda ayrı maddi olmayan duran varlık olarak",
            "B": "Araştırma gideri olarak",
            "C": "Makinenin önemli bir parçası olarak maddi duran varlık kapsamında",
            "D": "Ticari mal stoku olarak",
            "E": "Şerefiye olarak",
        },
        "C",
        "Bir yazılım ilgili donanımın ayrılmaz ve çalışması için zorunlu bir parçasıysa ayrı maddi olmayan duran varlık değil, **donanımla birlikte TMS 16 kapsamında maddi duran varlık** olarak değerlendirilir. Donanımdan bağımsız çalışan yazılım ise TMS 38 kapsamındadır.",
        "TMS 38 Maddi Olmayan Duran Varlıklar, par. 4",
    ),
    "finmuh-modv-gen-0005": intangible_patch(
        "İşletme, kendi markasının tanınırlığını artırmak için 400.000 ₺ reklam harcaması yapmış ve marka değerinin yükseldiğini güvenilir bir değerleme raporuyla ileri sürmüştür. TMS 38'e göre nasıl işlem yapılır?",
        {
            "A": "400.000 ₺ 260 Haklar hesabına aktifleştirilir.",
            "B": "Tutar 261 Şerefiye hesabında süresiz taşınır.",
            "C": "Aktif piyasa bulunup bulunmadığı araştırılmadan, değerleme raporundaki tahmini marka artışının tamamı diğer kapsamlı gelire ve özkaynağa alınır.",
            "D": "İşletme içi yaratılan marka aktifleştirilmez; reklam harcaması gerçekleştiğinde gider yazılır.",
            "E": "Marka değeri her dönem satış hasılatına eklenir.",
        },
        "D",
        "İşletme içi yaratılan markalar, bunlara ilişkin harcamalar işletmenin bütününü geliştirme harcamalarından ayrıştırılamadığı için maddi olmayan duran varlık olarak muhasebeleştirilmez. Reklam harcaması da hizmet alındığında **gider** yazılır.",
        "TMS 38, par. 63-64 ve 69(c)",
    ),
    "finmuh-modv-gen-0007": intangible_patch(
        "Bir yazılım projesinin teknik olarak tamamlanabilir olduğu, kullanılacağı, ekonomik fayda sağlayacağı ve maliyetinin güvenilir ölçülebildiği kanıtlanmıştır. Ancak işletmenin projeyi tamamlayacak finansmanı ve teknik personeli bulunmamaktadır. TMS 38'e göre geliştirme harcamaları nasıl muhasebeleştirilir?",
        {
            "A": "Altı ölçütün çoğunun sağlanması yeterli kabul edilir; finansman ve teknik personel daha sonra bulunabileceğinden mevcut harcamaların tamamı aktifleştirilir.",
            "B": "Şerefiye olarak kaydedilir.",
            "C": "Gerekli kaynakların varlığı da zorunlu olduğundan koşulların tamamı sağlanıncaya kadar gider yazılır.",
            "D": "Yalnız personel giderleri aktifleştirilir.",
            "E": "Finansman sağlanıp sağlanmadığı muhasebeleştirmeyi etkilemez.",
        },
        "C",
        "Geliştirme harcamalarının aktifleştirilebilmesi için TMS 38'deki **altı koşulun tamamı** sağlanmalıdır. Projeyi tamamlamak için yeterli teknik, mali ve diğer kaynaklar bulunmadığından muhasebeleştirme ölçütleri henüz tamamlanmamıştır; harcamalar gider yazılır.",
        "TMS 38, par. 57(a)-(f)",
    ),
    "finmuh-modv-gen-0010": intangible_patch(
        "TMS 38'e göre fiziksel niteliği olmayan bir kaynağın şerefiyeden ayrı, tanımlanabilir bir maddi olmayan duran varlık sayılabilmesi için hangi ölçüt yeterlidir?",
        {
            "A": "Ayrılabilir olması veya sözleşmeden ya da diğer yasal haklardan kaynaklanması",
            "B": "Mutlaka işletme içinde oluşturulmuş olması",
            "C": "Her yıl piyasa fiyatının yükselmesi",
            "D": "Bir yıl içinde nakde çevrilmesinin planlanması, aktif piyasada her gün fiyatının oluşması ve işletmenin satış niyetini yönetim kurulu kararıyla belgelemesi",
            "E": "Fiziksel bir taşıyıcıya hiç sahip olmaması",
        },
        "A",
        "Tanımlanabilirlik, varlığın **ayrılabilir** olması ya da işletmeden ayrılabilir olup olmadığına bakılmaksızın **sözleşmeden veya diğer yasal haklardan kaynaklanmasıyla** sağlanır. Fiziksel taşıyıcının bulunması tek başına sınıflandırmayı belirlemez.",
        "TMS 38, par. 11-12",
    ),
    "finmuh-modv-gen-0013": intangible_patch(
        "TMS 38 uygulayan işletmenin ayrı olarak satın aldığı bir lisansın maliyeti 100.000 ₺, tahmini kalıntı değeri 10.000 ₺ ve yararlı ömrü 5 yıldır. Doğrusal yönteme göre yıllık itfa payı kaç ₺'dir?",
        {
            "A": "10.000",
            "B": "20.000",
            "C": "18.000",
            "D": "22.000",
            "E": "90.000",
        },
        "C",
        "İtfaya tabi tutar = Maliyet − Kalıntı değer = 100.000 − 10.000 = **90.000 ₺**. Doğrusal yöntemde yıllık itfa payı 90.000 ÷ 5 = **18.000 ₺**dir.",
        "TMS 38, par. 97 ve 100-101",
    ),
    "finmuh-modv-gen-0014": intangible_patch(
        "Bir lisansın değer düşüklüğü öncesi defter değeri 200.000 ₺, TMS 36'ya göre geri kazanılabilir tutarı 150.000 ₺'dir. Değer düşüklüğü zararı ve işlem sonrası defter değeri sırasıyla kaç ₺ olur?",
        {
            "A": "150.000; 50.000",
            "B": "200.000; 150.000",
            "C": "50.000; 200.000",
            "D": "50.000; 150.000",
            "E": "Zarar oluşmaz; 200.000",
        },
        "D",
        "Defter değeri geri kazanılabilir tutarı 200.000 − 150.000 = **50.000 ₺** aşmaktadır. Bu tutar değer düşüklüğü zararı olarak muhasebeleştirilir ve varlığın yeni defter değeri **150.000 ₺** olur.",
        "TMS 38, par. 111; TMS 36 Varlıklarda Değer Düşüklüğü",
    ),
    "finmuh-modv-gen-0017": intangible_patch(
        "TMS 38'e göre sınırlı ve sınırsız yararlı ömre sahip maddi olmayan duran varlıkların sonraki dönem muhasebesiyle ilgili doğru ifade hangisidir?",
        {
            "A": "Her ikisi de zorunlu olarak beş yılda itfa edilir.",
            "B": "Sınırsız yararlı ömür, varlığın sonsuza kadar kesin gelir sağlayacağı anlamına gelir; bu nedenle varlık ne itfa edilir ne değer düşüklüğü testine alınır ne de ömür değerlendirmesi yeniden gözden geçirilir.",
            "C": "Sınırlı ömürlü varlık itfa edilmez, sınırsız ömürlü varlık itfa edilir.",
            "D": "Sınırlı ömürlü varlık sistematik olarak itfa edilir; sınırsız ömürlü varlık itfa edilmez ve yıllık değer düşüklüğü testine tabi tutulur.",
            "E": "Sınırsız ömürlü varlık değer düşüklüğüne uğramaz.",
        },
        "D",
        "Sınırlı yararlı ömre sahip maddi olmayan duran varlığın itfaya tabi tutarı yararlı ömrüne dağıtılır. Sınırsız yararlı ömürlü varlık **itfa edilmez**; yıllık olarak ve değer düşüklüğü belirtisi ortaya çıktığında TMS 36 kapsamında test edilir.",
        "TMS 38, par. 88-89 ve 107-109",
    ),
    "finmuh-modv-gen-0019": intangible_patch(
        "İşletme, satın aldığı benzersiz bir markayı dönem sonunda bağımsız değerleme raporundaki gerçeğe uygun değerine yükseltmek istemektedir. Marka için aktif piyasa bulunmamaktadır. TMS 38'e göre doğru işlem hangisidir?",
        {
            "A": "Bağımsız değerleme raporu gerçeğe uygun değeri tek başına kanıtladığından, aktif piyasa bulunmasa bile artış doğrudan satış geliri olarak muhasebeleştirilir.",
            "B": "Marka her yıl zorunlu olarak rayiç değere yükseltilir.",
            "C": "Artış 261 Şerefiye hesabına aktarılır.",
            "D": "Aktif piyasa bulunmadığından yeniden değerleme modeli uygulanamaz; marka maliyet modelinde izlenir.",
            "E": "Marka finansal tablo dışı bırakılır.",
        },
        "D",
        "TMS 38'de yeniden değerleme için gerçeğe uygun değerin **aktif bir piyasa** referans alınarak ölçülmesi gerekir. Benzersiz marka ve patentler için aktif piyasa bulunması olağan değildir; yalnız değerleme raporu yeniden değerleme modeli için yeterli değildir.",
        "TMS 38, par. 75 ve 78",
    ),
    "finmuh-modv-gen-0020": intangible_patch(
        "TMS 38'e göre maddi olmayan duran varlıkların ilk muhasebeleştirmeden sonraki ölçümünde hangi muhasebe politikaları seçilebilir?",
        {
            "A": "Maliyet modeli veya aktif piyasa şartını sağlayan yeniden değerleme modeli",
            "B": "Yalnız nominal değer modeli",
            "C": "Aktif piyasa koşulu aranmadan, yönetimin belirlediği tahmini satış fiyatına göre her dönem serbestçe değiştirilebilen gerçeğe uygun değer modeli",
            "D": "Sadece net gerçekleşebilir değer modeli",
            "E": "Yalnız vergi değeri modeli",
        },
        "A",
        "TMS 38, **maliyet modeli** ile aktif piyasa üzerinden uygulanabilen **yeniden değerleme modeli** arasında politika seçimine izin verir. Yeniden değerleme modeli tek tek seçilmiş varlıklara değil, kural olarak ilgili sınıfa uygulanır.",
        "TMS 38, par. 72-75",
    ),
    "finmuh-modv-gen-0021": intangible_patch(
        "İşletme 120.000 ₺'ye beş yıllık lisans edinmiştir. Lisansın üç yıl daha yenilenmesi mümkündür ve işletmenin önemli maliyete katlanmadan yenileyeceğine ilişkin güvenilir kanıt bulunmaktadır. Başka sınırlama ve kalıntı değer yoksa TMS 38'e göre yıllık doğrusal itfa payı kaç ₺'dir?",
        {
            "A": "30.000",
            "B": "24.000",
            "C": "20.000",
            "D": "15.000",
            "E": "Lisans itfa edilmez.",
        },
        "D",
        "Yenilemenin önemli maliyet olmadan yapılacağına ilişkin kanıt varsa yenileme dönemi yararlı ömre dâhil edilir. Toplam yararlı ömür 5 + 3 = **8 yıl**, yıllık itfa 120.000 ÷ 8 = **15.000 ₺**dir.",
        "TMS 38, par. 94-96",
    ),
    "finmuh-modv-gen-0025": intangible_patch(
        "Bir yazılım için normal kredi vadelerini aşan iki yıl vadeli toplam 460.000 ₺ ödeme yapılacaktır. Yazılımın peşin fiyat eşdeğeri 400.000 ₺'dir. TMS 38'e göre ilk kayıtta yazılımın maliyeti ve vade farkının işlemi hangisidir?",
        {
            "A": "Maliyet, ödeme vadelerine bakılmadan toplam sözleşme bedeli olan 460.000 ₺'dir; peşin fiyatla arasındaki vade farkı ayrıştırılmaz ve kredi süresince faiz gideri kaydedilmez.",
            "B": "Maliyet 60.000 ₺; kalan tutar şerefiye yazılır.",
            "C": "Maliyet sıfır; bütün ödeme iki yılda gider yazılır.",
            "D": "Maliyet 400.000 ₺; 60.000 ₺ ilk gün tamamen gider yazılır.",
            "E": "Maliyet 400.000 ₺; 60.000 ₺ TMS 23 istisnası dışında kredi süresince faiz gideridir.",
        },
        "E",
        "Normal kredi vadelerini aşan ertelenmiş ödemede maliyet **peşin fiyat eşdeğeri 400.000 ₺**dir. Toplam ödeme ile peşin değer arasındaki **60.000 ₺ fark**, TMS 23 kapsamında aktifleştirilmediği sürece iki yıllık kredi döneminde faiz gideri olarak muhasebeleştirilir.",
        "TMS 38, par. 32",
    ),
    "finmuh-modv-gen-0026": intangible_patch(
        "Aşağıdaki yazılım harcamalarından hangisi TMS 38 yerine TMS 16 kapsamında maddi duran varlığın maliyetinin parçası olarak değerlendirilir?",
        {
            "A": "Donanımdan bağımsız kullanılan muhasebe yazılımı lisansı",
            "B": "İnternet üzerinden sunulan ve işletmenin yazılımın kendisini kontrol etmediği abonelik hizmeti için sözleşme boyunca yapılan aylık hizmet ödemeleri",
            "C": "Satılmak üzere geliştirilen standart yazılım stoku",
            "D": "Bilgisayar kontrollü makinenin onsuz çalışamadığı, makineye özgü yazılım",
            "E": "Araştırma safhasındaki alternatif yazılım tasarımları",
        },
        "D",
        "Donanımın onsuz çalışamadığı ve ondan ayrı kullanılamayan yazılım, donanımın önemli bir parçasıdır ve **TMS 16 kapsamında maddi duran varlığın maliyetine** dâhil edilir. Bağımsız yazılım lisansı ise TMS 38 kapsamında olabilir.",
        "TMS 38, par. 4",
    ),
    "finmuh-modv-gen-0027": intangible_patch(
        "Üretim sürecini yöneten bir yazılımın dönem itfa payı, üretilen fakat henüz satılmamış mamullerle doğrudan ilgilidir. TMS 38 ve TMS 2'ye göre itfa payı öncelikle nasıl muhasebeleştirilir?",
        {
            "A": "Daima finansman gideri olarak",
            "B": "Doğrudan geçmiş yıl zararlarına aktarılarak",
            "C": "Mamul stoklarının dönüştürme maliyetine dâhil edilerek",
            "D": "Birikmiş itfa hesabı kullanılmadan, yazılımın brüt maliyetinden doğrudan düşülerek ve mamuller satılıncaya kadar gelir tablosuyla hiç ilişkilendirilmeyerek",
            "E": "Mamul satılana kadar hiç kaydedilmeyerek",
        },
        "C",
        "Bir maddi olmayan duran varlığın kullanımı başka bir varlığın üretimine katkı sağlıyorsa itfa payı o varlığın maliyetine dâhil edilir. Üretim yazılımının itfa payı, ilgili mamullerin **dönüştürme maliyetinin** unsurudur.",
        "TMS 38, par. 97; TMS 2 Stoklar",
    ),
    "finmuh-modv-gen-0029": intangible_patch(
        "Bir işletme birleşmesinde devralınanın daha önce kayda almadığı, sözleşmeden doğan ve gerçeğe uygun değeri güvenilir ölçülebilen müşteri ilişkileri edinilmiştir. TFRS 3 ve TMS 38'e göre devralan nasıl işlem yapar?",
        {
            "A": "Devralınan işletme kendi finansal tablolarında bu müşteri ilişkilerini daha önce muhasebeleştirmediği için devralan da birleşme tarihinde ayrı varlık kaydedemez ve bütün değeri şerefiyeye ekler.",
            "B": "Tutarın tamamını maddi duran varlığa aktarır.",
            "C": "Yalnız nakit tahsil edildiğinde varlık kaydeder.",
            "D": "Müşteri ilişkilerini stok olarak sınıflandırır.",
            "E": "Tanımlanabilir maddi olmayan duran varlığı birleşme tarihindeki gerçeğe uygun değeriyle şerefiyeden ayrı kaydeder.",
        },
        "E",
        "Birleşmede edinilen varlık ayrılabilir veya sözleşmeden/yasal haktan kaynaklanıyorsa ve gerçeğe uygun değeri ölçülebiliyorsa, devralınanın önceki kaydından bağımsız olarak **şerefiyeden ayrı maddi olmayan duran varlık** şeklinde muhasebeleştirilir.",
        "TMS 38, par. 33-34; TFRS 3 İşletme Birleşmeleri",
    ),
    "finmuh-modv-gen-0030": intangible_patch(
        "İşletme içi bir yazılım projesinde araştırma safhasında 100.000 ₺, geliştirme safhasında aktifleştirme koşulları sağlanmadan önce 40.000 ₺ ve koşulların tamamı sağlandıktan sonra 160.000 ₺ harcanmıştır. TMS 38'e göre aktifleştirilecek tutar kaç ₺'dir?",
        {
            "A": "300.000",
            "B": "160.000",
            "C": "200.000",
            "D": "140.000",
            "E": "40.000",
        },
        "B",
        "Araştırma harcamaları ve geliştirme aşamasında ölçütler sağlanmadan önce oluşan tutarlar giderdir. Maliyet, muhasebeleştirme ölçütlerinin **ilk sağlandığı tarihten itibaren** birikir. Bu nedenle yalnız sonraki **160.000 ₺** aktifleştirilir.",
        "TMS 38, par. 54, 57 ve 65",
    ),
    "finmuh-modv-gen-0031": intangible_patch(
        "Bir proje için geçen yıl araştırma safhasında yapılan 80.000 ₺ harcama gider yazılmıştır. Bu yıl proje geliştirme ölçütlerini sağlamış ve başarı beklentisi yükselmiştir. TMS 38'e göre geçen yıl gider yazılan 80.000 ₺ için ne yapılır?",
        {
            "A": "Tamamı bu yıl 263 hesabına aktarılır.",
            "B": "Yarısı aktifleştirilir, yarısı gider kalır.",
            "C": "Şerefiye hesabına alınır.",
            "D": "Geçmişte gider yazılan tutar sonradan varlık maliyetine geri alınamaz.",
            "E": "Projenin geliştirme aşamasında başarılı olması geçmişteki araştırma harcamasının niteliğini değiştirir; tutar önce dönem geliri yazılıp ardından yeni varlığın maliyetine aktarılır.",
        },
        "D",
        "Başlangıçta gider olarak muhasebeleştirilen maddi olmayan duran varlıkla ilgili harcama, sonraki bir tarihte ölçütler sağlansa bile varlık maliyetine **geri alınamaz**. Yalnız ölçütlerin sağlandığı tarihten sonraki uygun harcamalar aktifleştirilebilir.",
        "TMS 38, par. 65 ve 71",
    ),
    "finmuh-modv-gen-0032": intangible_patch(
        "TMS 38 uygulayan işletmenin yeni şube açılışı için yaptığı personel eğitimi, reklam ve açılış organizasyonu harcamaları nasıl muhasebeleştirilir?",
        {
            "A": "Gelecek dönemlerde şubenin satışlarını artırması beklendiğinden eğitim, reklam ve açılış organizasyonu harcamalarının tamamı sınırsız yararlı ömürlü tek bir maddi olmayan duran varlık olarak",
            "B": "Tanımlanabilir bir varlık oluşturmadıklarından hizmet alındığında gider olarak",
            "C": "Şerefiye hesabında",
            "D": "Maddi duran varlık maliyetinde",
            "E": "Yalnız şube kâr ederse aktifleştirilerek",
        },
        "B",
        "Kuruluş ve açılış öncesi maliyetleri, eğitim ile reklam ve promosyon harcamaları TMS 38'de ayrıca tanımlanabilir bir varlık oluşturmadıklarından **gerçekleştikleri veya hizmet alındığı anda gider** olarak muhasebeleştirilir.",
        "TMS 38, par. 69(a)-(c)",
    ),
    "finmuh-modv-gen-0034": intangible_patch(
        "TMS 38'e göre yararlı ömrü sınırsız kabul edilen bir lisansın sonraki dönem muhasebesiyle ilgili doğru ifade hangisidir?",
        {
            "A": "Her yıl zorunlu olarak %20 itfa edilir.",
            "B": "Değer düşüklüğü yalnız lisans satılırken hesaplanır.",
            "C": "İtfa edilmez; yıllık ve belirti olduğunda değer düşüklüğü testine alınır, ömür değerlendirmesi her dönem gözden geçirilir.",
            "D": "Defter değeri her yıl satış hasılatına aktarılır.",
            "E": "Sınırsız ömür değerlendirmesi ilk muhasebeleştirmede kesinleşir; teknolojik, hukuki ve ticari koşullar değişse bile daha sonra sınırlı ömre çevrilemez ve değer düşüklüğü göstergesi sayılmaz.",
        },
        "C",
        "Sınırsız yararlı ömürlü maddi olmayan duran varlık **itfa edilmez**. Geri kazanılabilir tutarı yıllık olarak ve değer düşüklüğü belirtisi doğduğunda defter değeriyle karşılaştırılır; sınırsız ömrü destekleyen koşullar da her dönem yeniden değerlendirilir.",
        "TMS 38, par. 107-109; TMS 36",
    ),
    "finmuh-modv-gen-0035": intangible_patch(
        "Bir yazılımın dönem başı defter değeri 180.000 ₺, kalıntı değeri sıfırdır. Teknolojik gelişmeler nedeniyle kalan yararlı ömür 3 yıl olarak revize edilmiştir. TMS 38 ve TMS 8'e göre cari yıl itfa payı kaç ₺ olur ve değişiklik nasıl uygulanır?",
        {
            "A": "180.000 ₺; geçmiş dönemlere geriye dönük",
            "B": "30.000 ₺; yalnız dipnotta",
            "C": "90.000 ₺; geçmiş yıllar düzeltilerek",
            "D": "İtfa ayrılmaz; ilk muhasebeleştirmede belirlenen yararlı ömür sözleşme süresi boyunca değiştirilemez ve yeni teknolojik bilgiler yalnız dipnot açıklaması olarak kalır.",
            "E": "60.000 ₺; cari ve gelecek dönemlere ileriye yönelik",
        },
        "E",
        "Yararlı ömür değişikliği muhasebe tahmini değişikliğidir ve **ileriye yönelik** uygulanır. Yeni yıllık itfa payı 180.000 ÷ 3 = **60.000 ₺**dir; önceki dönem finansal tabloları geriye dönük düzeltilmez.",
        "TMS 38, par. 104; TMS 8",
    ),
    "finmuh-modv-gen-0036": intangible_patch(
        "İşletme, aktif piyasası bulunan üretim kotalarında yeniden değerleme modelini uygulamaktadır. Aynı sınıftaki yalnız değeri yükselen iki kotayı yeniden değerlemek istemektedir. TMS 38'e göre doğru işlem hangisidir?",
        {
            "A": "Yalnız değeri yükselen kotalar yeniden değerlenebilir.",
            "B": "Seçici uygulama yapılamaz; aktif piyasası bulunan ilgili sınıftaki varlıklar aynı yöntemle ve eş zamanlı değerlenir.",
            "C": "Yeniden değerleme yalnız şerefiyede uygulanabilir.",
            "D": "Bütün kotalar stok hesabına aktarılır.",
            "E": "Maddi olmayan duran varlıklar benzersiz kabul edildiğinden aktif piyasa bulunsa bile yeniden değerleme mümkün değildir; bütün sınıf yalnız maliyet modelinde tutulur.",
        },
        "B",
        "Yeniden değerleme modeli aktif piyasa koşuluyla uygulanabilir. Bir sınıfın içinden yalnız değer artışı olan kalemleri seçmek farklı tarihlere ait tutarların birlikte sunulmasına yol açacağından, ilgili sınıf **aynı yöntemle ve eş zamanlı** yeniden değerlenir.",
        "TMS 38, par. 72-75",
    ),
    "finmuh-modv-gen-0043": intangible_patch(
        "TMS 38'e göre maddi olmayan duran varlıkların itfasında hasılata dayalı yöntem kullanılmasıyla ilgili genel yaklaşım hangisidir?",
        {
            "A": "Genellikle uygun olmadığı yönünde aksi ispat edilebilir bir karine vardır; yalnız sınırlı koşullarda kullanılabilir.",
            "B": "Hasılat tüketim biçimini her durumda doğrudan yansıttığından bütün sınırlı yararlı ömürlü maddi olmayan duran varlıklarda kullanılması zorunlu olan tek yöntemdir.",
            "C": "Yalnız maliyet modelinde kesinlikle zorunludur.",
            "D": "Hasılat değiştikçe yararlı ömür kendiliğinden sınırsız olur.",
            "E": "Hasılata dayalı yöntem yalnız araştırma giderlerinde kullanılır.",
        },
        "A",
        "Hasılat satış fiyatı, diğer girdiler ve enflasyon gibi varlığın ekonomik yararlarının tüketiminden bağımsız unsurlardan etkilenebilir. Bu nedenle hasılata dayalı itfanın uygun olmadığı yönünde **aksi ispat edilebilir bir karine** vardır; TMS 38 yalnız sınırlı istisnalar tanır.",
        "TMS 38, par. 98A-98C",
    ),
    "finmuh-modv-gen-0048": intangible_patch(
        "İşletme, kendi pazarlama faaliyetleriyle oluşturduğu müşteri listesinin gelecekte gelir sağlayacağını öngörmektedir. Liste sözleşmeye veya devredilebilir bir hakka dayanmamaktadır. TMS 38'e göre nasıl işlem yapılır?",
        {
            "A": "Tahmini gelirlerin tamamı varlık kaydedilir.",
            "B": "Liste 261 Şerefiye hesabında aktifleştirilir.",
            "C": "Müşteri sayısı kadar nominal değerle kaydedilir.",
            "D": "Yönetim kurulu gelecekteki müşteri gelirlerini güvenilir bir bütçeyle tahmin ettiği anda, ayrılabilirlik veya kontrol koşulu aranmaksızın bu tahmini tutarla aktifleştirilir.",
            "E": "İşletme içi yaratılan müşteri listesi maddi olmayan duran varlık olarak muhasebeleştirilmez.",
        },
        "E",
        "İşletme içi yaratılan müşteri listeleriyle ilgili harcamalar, işin bütününü geliştiren harcamalardan ayrıştırılamadığından TMS 38 kapsamında maddi olmayan duran varlık olarak muhasebeleştirilmez; ilgili harcamalar gider yazılır.",
        "TMS 38, par. 63-64",
    ),
    "finmuh-modv-gen-0051": intangible_patch(
        "İşletme bir yazılım lisansı için 100.000 ₺ liste fiyatı üzerinden 10.000 ₺ ticari iskonto almış; lisansı kullanıma hazır hâle getiren hukuki danışmanlık için 5.000 ₺, çalışma testi için 3.000 ₺ ve kullanıcı eğitimi için 8.000 ₺ ödemiştir. TMS 38'e göre yazılımın maliyeti kaç ₺'dir?",
        {
            "A": "98.000",
            "B": "90.000",
            "C": "106.000",
            "D": "108.000",
            "E": "116.000",
        },
        "A",
        "Maliyet; iskontolu satın alma fiyatı 90.000 ₺ ile kullanıma hazırlamaya doğrudan bağlı danışmanlık 5.000 ₺ ve test 3.000 ₺ toplamıdır: **98.000 ₺**. Kullanıcı eğitimi varlığı çalışabilir duruma getiren maliyet değildir ve gider yazılır.",
        "TMS 38, par. 27-29",
    ),
    "finmuh-modv-gen-0052": intangible_patch(
        "TMS 38'e göre sınırlı yararlı ömre sahip bir maddi olmayan duran varlığın kalıntı değeri hangi durumda sıfırdan farklı kabul edilebilir?",
        {
            "A": "Yönetim gelecekte yüksek kâr beklediğinde",
            "B": "Varlığın reklamı yapıldığında",
            "C": "Üçüncü tarafın satın alma taahhüdü varsa veya ömür sonunda da bulunması muhtemel aktif piyasa değeri varsa",
            "D": "Varlık işletme içinde oluşturulduğunda",
            "E": "Yönetim gelecekte varlığı elden çıkarmayı düşünüyorsa, üçüncü taraf taahhüdü veya aktif piyasa kanıtı aranmadan her maddi olmayan duran varlıkta zorunlu olarak",
        },
        "C",
        "Sınırlı ömürlü maddi olmayan duran varlığın kalıntı değeri kural olarak **sıfırdır**. Ancak üçüncü tarafın satın alma taahhüdü varsa veya değer aktif piyasadan belirlenebiliyor ve piyasanın yararlı ömür sonunda da bulunması muhtemelse sıfırdan farklı olabilir.",
        "TMS 38, par. 100",
    ),
    "finmuh-modv-gen-0055": intangible_patch(
        "İşletme, çalışanlarına verdiği yoğun eğitim sayesinde gelecekte önemli ekonomik fayda beklemektedir; ancak çalışanların işletmede kalmasını veya becerilerini yalnız işletme yararına kullanmasını sağlayan bir hakkı yoktur. TMS 38'e göre eğitim harcaması nasıl muhasebeleştirilir?",
        {
            "A": "260 Haklar hesabında süresiz olarak",
            "B": "261 Şerefiye hesabında",
            "C": "Çalışan sayısına göre maddi duran varlık olarak",
            "D": "Gelecekteki yararlar üzerinde yeterli kontrol bulunmadığından gider olarak",
            "E": "Eğitim çalışanların bilgi düzeyini artırdığı için işletmenin çalışanlar üzerinde hukuki kontrolü bulunup bulunmadığına bakılmadan önce varlıklaştırılıp yalnız çalışan ayrılırsa gider olarak",
        },
        "D",
        "İşletme, çalışanların becerilerinden yarar beklese de genellikle çalışanların işletmede kalmasını ve bu yararlara başkalarının erişimini kısıtlayamaz. Bu nedenle kontrol ölçütü sağlanmaz; **eğitim harcaması gider** olarak muhasebeleştirilir.",
        "TMS 38, par. 13-15 ve 69(b)",
    ),
    "finmuh-modv-gen-0058": intangible_patch(
        "Maliyeti 120.000 ₺, kalıntı değeri sıfır olan bir yazılımdan yararlı ömrü boyunca 240.000 işlem gerçekleştirilmesi beklenmektedir. Cari dönemde 60.000 işlem yapıldığına göre üretim birimleri yönteminde itfa payı kaç ₺'dir?",
        {
            "A": "15.000",
            "B": "20.000",
            "C": "30.000",
            "D": "60.000",
            "E": "120.000",
        },
        "C",
        "Cari dönemde toplam beklenen kullanımın 60.000/240.000 = **%25'i** gerçekleşmiştir. Üretim birimleri yöntemine göre itfa payı 120.000 × %25 = **30.000 ₺**dir.",
        "TMS 38, par. 97-98",
    ),
}


FINANCIAL_INVESTMENT_PATCHES = {
    "finmuh-malidv-gen-0003": financial_investment_patch(
        "Tekdüzen Hesap Planı'ndaki 242 İştirakler hesabının kapsamı ile TMS 28'deki önemli etki değerlendirmesi karşılaştırıldığında aşağıdakilerden hangisi doğrudur?",
        {
            "A": "242 hesabı yalnız oy hakkının %20 ile %50 arasında olduğu yatırımları kapsar; yönetim kurulunda temsil veya politika kararlarına katılma gibi başka kanıtlar dikkate alınmaz.",
            "B": "Sermaye payı %50'yi aşmayan bütün uzun vadeli paylar, yönetime katılma hakkı aranmaksızın 242 hesabında izlenir.",
            "C": "Tekdüzen Hesap Planı'nda en az %10 oy veya yönetime katılma hakkı aranır; TMS 28'de %20 oy hakkı aksi kanıtlanabilir önemli etki varsayımıdır.",
            "D": "Tekdüzen Hesap Planı'ndaki %10 eşiği aşıldığında yatırım her durumda bağlı ortaklık sayılır.",
            "E": "Tekdüzen Hesap Planı ile TMS 28 aynı yüzdeyi ve aynı değerlendirme ölçütünü kullanır.",
        },
        "C",
        "İki düzenlemenin eşiği aynı değildir. Tekdüzen Hesap Planı açıklamasında **242 İştirakler** için yönetim ve politikaya katılma ile en az **%10 oy veya yönetime katılma hakkı** aranır; pay en çok %50 olabilir. TMS 28'de ise **%20 oy hakkı**, aksi açıkça ortaya konulabilen bir **önemli etki varsayımıdır**; tek başına kesin sınıflama değildir.",
        "1 Sıra No'lu MSUGT - 242 İştirakler; TMS 28, par. 5-6",
    ),
    "finmuh-malidv-gen-0007": financial_investment_patch(
        "İşletme banka hesabından; kısa sürede fiyat farkından yararlanmak amacıyla 120.000 ₺'lik borsa payı ve yönetimine katılmak amacıyla başka bir şirketin oy haklarının %25'ini temsil eden 360.000 ₺'lik pay satın almıştır. Ayrıca alış bedellerinden ayrı 8.000 ₺ aracı kurum komisyonu ödemiştir. VUK esaslı yasal kayıtta doğru kayıt aşağıdakilerden hangisidir?",
        {
            "A": "110 Hisse Senetleri 120.000, 242 İştirakler 360.000 ve 653 Komisyon Giderleri 8.000 borç; 102 Bankalar 488.000 alacak",
            "B": "240 Bağlı Menkul Kıymetler 488.000 borç; 102 Bankalar 488.000 alacak",
            "C": "110 Hisse Senetleri 120.000, 245 Bağlı Ortaklıklar 360.000 ve 653 Komisyon Giderleri 8.000 borç; 102 Bankalar 488.000 alacak",
            "D": "242 İştirakler 488.000 borç; 102 Bankalar 488.000 alacak",
            "E": "110 Hisse Senetleri 128.000 ve 242 İştirakler 360.000 borç; 102 Bankalar 488.000 alacak",
        },
        "A",
        "Kısa vadeli alım **110 Hisse Senetleri**ne, yönetime katılma amacı taşıyan %25'lik uzun vadeli pay **242 İştirakler**e kaydedilir. VUK'ta hisse senetlerinin alış bedeli, satın alma tutarıdır; alışla ilgili diğer giderler bu bedele dahil edilmez. Ayrı ödenen 8.000 ₺ komisyon gider yazılır ve bankadan toplam **488.000 ₺** çıkar.",
        "1 Sıra No'lu MSUGT - 110/242/653; VUK m. 268/A ve 279",
    ),
    "finmuh-malidv-gen-0013": financial_investment_patch(
        "TMS 27'ye göre bireysel finansal tablolarda bağlı ortaklık, iş ortaklığı ve iştirak yatırımlarının muhasebeleştirilmesiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            "A": "Yatırımlar maliyet bedeliyle muhasebeleştirilebilir.",
            "B": "Yatırımlar TFRS 9 hükümlerine göre muhasebeleştirilebilir.",
            "C": "Yatırımlar, TMS 28'de tanımlanan özkaynak yöntemi kullanılarak da bireysel finansal tablolarda muhasebeleştirilebilir.",
            "D": "Seçilen esas, her bir yatırım kategorisi içinde tutarlı uygulanır.",
            "E": "Aynı kategorideki her yatırım için dönemden döneme serbestçe farklı bir yöntem seçilebilir.",
        },
        "E",
        "TMS 27; bireysel finansal tablolarda maliyet, TFRS 9 veya özkaynak yöntemine izin verir. Ancak işletme seçtiği muhasebeleştirme esasını **her bir yatırım kategorisi için aynı şekilde** uygulamalıdır; aynı kategoride yatırım bazında keyfî yöntem değişikliği yapılamaz.",
        "TMS 27 Bireysel Finansal Tablolar, par. 10",
    ),
    "finmuh-malidv-gen-0016": financial_investment_patch(
        "TFRS 10'a göre bir yatırımcının yatırım yaptığı işletmeyi kontrol ettiğinin kabul edilmesi için aşağıdaki unsurlardan hangilerinin birlikte bulunması gerekir?",
        {
            "A": "Yalnız oy haklarının salt çoğunluğuna sahip olma, yönetim kurulunun çoğunu atama, yatırımı uzun süre elde tutma ve düzenli temettü tahsil etme",
            "B": "Güç, değişken getirilere maruz kalma veya hak ve gücü getirileri etkilemekte kullanabilme",
            "C": "En az %20 oy hakkına ve yönetim kurulunda bir üyeye sahip olma",
            "D": "Uzun vadeli yatırım amacı ve payların borsada işlem görmemesi",
            "E": "Sermayenin en az %10'una sahip olma ve önemli ticari işlemler gerçekleştirme",
        },
        "B",
        "TFRS 10'da kontrol üç unsurun **birlikte** bulunmasına bağlıdır: yatırım yapılan işletme üzerinde güç, değişken getirilere maruz kalma veya bu getirilerde hak sahibi olma ve mevcut gücü getirileri etkilemek amacıyla kullanabilme. Tek bir sahiplik yüzdesi kontrolün evrensel tanımı değildir.",
        "TFRS 10 Konsolide Finansal Tablolar, par. 6-7",
    ),
    "finmuh-malidv-gen-0017": financial_investment_patch(
        "Bir işletme başka bir şirketin oy haklarının %22'sini elinde tutmaktadır. Aksini açıkça gösteren herhangi bir kanıt bulunmamaktadır. TMS 28'e göre bu yatırım için öncelikle hangi sonuca ulaşılır?",
        {
            "A": "Oy hakkı %50'yi aşmadığından önemli etki kesinlikle yoktur.",
            "B": "Oy hakkı %10'u aştığı için sözleşmeler ve diğer haklar ayrıca incelenmeden kontrolün bulunduğu kesin kabul edilir.",
            "C": "Yalnız payların uzun vadeli tutulması hâlinde önemli etki vardır.",
            "D": "Aksi açıkça ortaya konulmadıkça önemli etkinin bulunduğu varsayılır.",
            "E": "Yatırım doğrudan TFRS 10 kapsamında bağlı ortaklık sayılır.",
        },
        "D",
        "TMS 28'e göre doğrudan veya dolaylı **%20 ya da daha fazla oy hakkı**, aksi açıkça ortaya konulmadıkça önemli etkinin bulunduğuna ilişkin bir varsayım oluşturur. Bu varsayım kesin ve çürütülemez değildir.",
        "TMS 28 İştiraklerdeki ve İş Ortaklıklarındaki Yatırımlar, par. 5",
    ),
    "finmuh-malidv-gen-0020": financial_investment_patch(
        "Bir yatırımcı, bir şirketin oy haklarının yalnız %35'ine sahiptir. Ancak yürürlükteki sözleşme yatırımcıya şirketin getirilerini en çok etkileyen üretim ve fiyatlama kararlarını tek başına yönetme hakkı vermektedir. Yatırımcı değişken getirilere maruzdur ve bu hakkını getirileri etkilemek için kullanabilmektedir. TFRS 10'a göre sonuç nedir?",
        {
            "A": "Üç kontrol unsuru birlikte bulunduğundan, oy hakkı %50'nin altında olsa da yatırımcı kontrol sahibidir.",
            "B": "Oy hakkı %50'nin altında olduğundan kontrol kurulamaz.",
            "C": "Yatırımcı yalnız %10 eşiğini geçtiği için otomatik olarak iştirak sayılır; sözleşmeden doğan yönetim hakkı ve getirileri etkileme imkânı dikkate alınmaz.",
            "D": "Sözleşmeden doğan haklar yalnız bilanço tarihinde kullanılmışsa kontrol doğar.",
            "E": "Değişken getirilere maruz kalmak tek başına müşterek kontrol yaratır.",
        },
        "A",
        "Kontrol yalnız sermaye veya oy oranıyla belirlenmez. Sözleşmeden doğan mevcut haklar yatırımcıya ilgili faaliyetleri yönetme **gücü** veriyor, yatırımcı **değişken getirilere** maruz kalıyor ve gücünü bu getirileri etkilemek için kullanabiliyorsa TFRS 10'daki kontrol koşulları sağlanır.",
        "TFRS 10, par. 7 ve 10-11",
    ),
    "finmuh-malidv-gen-0021": financial_investment_patch(
        "Bir işletme yatırım yapılan şirketin oy haklarının %15'ine sahiptir. Buna karşılık yönetim kurulunda temsil edilmekte, temettü politikası kararlarına katılmakta ve şirkete gerekli teknik bilgiyi sağlamaktadır. TMS 28'e göre en uygun değerlendirme hangisidir?",
        {
            "A": "Oy hakkı %20'nin altında olduğundan yönetim kurulundaki temsil, politika kararlarına katılma ve teknik bilgi sağlama kanıtları incelenmeden önemli etki reddedilir.",
            "B": "Teknik bilgi sağlanması yatırımcıyı otomatik olarak ana ortaklık yapar.",
            "C": "Oy hakkı %20'nin altında olsa da mevcut göstergeler önemli etkinin bulunduğunu açıkça ortaya koyabilir.",
            "D": "Yalnız sermaye payı dikkate alınır; yönetim kurulundaki temsil önemsizdir.",
            "E": "Bu koşullar yalnız müşterek kontrol bulunduğunu gösterir.",
        },
        "C",
        "%20'nin altındaki oy hakkı önemli etkinin bulunmadığına ilişkin bir varsayımdır; fakat aksi açıkça kanıtlanabilir. **Yönetim kurulunda temsil, politika belirleme süreçlerine katılma ve gerekli teknik bilginin sağlanması** TMS 28'de önemli etki göstergeleri arasında sayılmıştır.",
        "TMS 28, par. 5-6",
    ),
    "finmuh-malidv-gen-0022": financial_investment_patch(
        "TMS 28'e göre aşağıdakilerden hangisi tek başına önemli etkinin varlığına ilişkin standartta sayılan göstergelerden biri değildir?",
        {
            "A": "Yatırım yapılan işletmenin yönetim kurulunda temsil edilme",
            "B": "Temettü kararları dâhil politika belirleme süreçlerine katılma",
            "C": "Yatırımcı ile yatırım yapılan işletme arasında önemli işlemler bulunması",
            "D": "İşletmeler arasında yönetici personel değişimi yapılması",
            "E": "İki işletmenin uzun yıllardır aynı reklam ajansıyla çalışması",
        },
        "E",
        "TMS 28; yönetim kurulunda temsil, politika süreçlerine katılma, önemli işlemler, yönetici personel değişimi ve gerekli teknik bilgi sağlanmasını önemli etki göstergeleri olarak sayar. **Aynı reklam ajansıyla çalışmak** bu göstergelerden biri değildir.",
        "TMS 28, par. 6",
    ),
    "finmuh-malidv-gen-0025": financial_investment_patch(
        "İşletme, %30 pay sahibi olduğu iştirak yatırımını özkaynak yöntemiyle 500.000 ₺ maliyetle kaydetmiştir. İştirak dönem içinde 200.000 ₺ kâr açıklamış ve toplam 100.000 ₺ temettü dağıtmıştır. Başka değişiklik yoksa yatırımın dönem sonu defter değeri kaç ₺'dir?",
        {
            "A": "500.000",
            "B": "530.000",
            "C": "560.000",
            "D": "590.000",
            "E": "470.000",
        },
        "B",
        "Kârdan pay 200.000 × %30 = **60.000 ₺** olup yatırımın defter değerini artırır. Dağıtılan temettüden pay 100.000 × %30 = **30.000 ₺** olup defter değerini azaltır. Son değer 500.000 + 60.000 − 30.000 = **530.000 ₺**dir.",
        "TMS 28, par. 10",
    ),
    "finmuh-malidv-gen-0028": financial_investment_patch(
        "İşletmenin uzun vadeli amaçla edindiği üç yatırım şöyledir: K şirketinde yönetime katılma hakkı bulunmayan %8 pay, L şirketinde yönetime katılma amacı taşıyan %30 pay ve M şirketinde kontrol sağlayan %70 pay. Tekdüzen Hesap Planı'na göre doğru hesap sıralaması hangisidir?",
        {
            "A": "110 Hisse Senetleri - 240 Bağlı Menkul Kıymetler - 242 İştirakler",
            "B": "242 İştirakler - 245 Bağlı Ortaklıklar - 248 Diğer Mali Duran Varlıklar",
            "C": "240 Bağlı Menkul Kıymetler - 245 Bağlı Ortaklıklar - 242 İştirakler",
            "D": "240 Bağlı Menkul Kıymetler - 242 İştirakler - 245 Bağlı Ortaklıklar",
            "E": "110 Hisse Senetleri - 242 İştirakler - 245 Bağlı Ortaklıklar",
        },
        "D",
        "Yönetime katılma hakkı vermeyen %8'lik uzun vadeli pay **240**, yönetime katılma amacı taşıyan %30'luk pay **242**, kontrol sağlayan %70'lik pay ise **245** hesabında izlenir.",
        "1 Sıra No'lu MSUGT - 240/242/245 hesap açıklamaları",
    ),
    "finmuh-malidv-gen-0029": financial_investment_patch(
        "Bir banka, kredi verdiği işletmede yalnızca borçlunun olağan faaliyetini kökten değiştiren işlemleri engelleme hakkına sahiptir. Bu hak kredinin tahsilini korumak için tasarlanmış olup bankaya günlük faaliyetleri yönetme imkânı vermemektedir. TFRS 10'a göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Hak koruyucu niteliktedir; bu hak tek başına bankaya güç ve kontrol sağlamaz.",
            "B": "Her veto hakkı, yalnız alacaklının menfaatini korumak için tasarlanmış olsa ve olağan kararları kapsamasa bile ilgili faaliyetleri yönetme gücü verir.",
            "C": "Banka kredi getirisine maruz kaldığı için işletmeyi mutlaka kontrol eder.",
            "D": "Koruyucu hak, bankayı yatırım işletmesi yapar.",
            "E": "İşletmenin yönetimi veto hakkını hiç kullanmamışsa hak kendiliğinden asli hakka dönüşür.",
        },
        "A",
        "İşletmenin faaliyetlerine ilişkin temel değişikliklerde alacaklının menfaatini koruyan, fakat ilgili faaliyetleri yönetme imkânı vermeyen haklar **koruyucu hak** niteliğindedir. Sadece koruyucu haklara sahip olmak TFRS 10 anlamında güç ve kontrol doğurmaz.",
        "TFRS 10, par. 14 ve B26-B28",
    ),
    "finmuh-malidv-gen-0032": financial_investment_patch(
        "İşletme, iştirak amacıyla edindiği hisse senetleri için satıcıya 400.000 ₺, aracı kuruma ayrıca 12.000 ₺ komisyon ödemiştir. VUK'a göre hisse senetlerinin değerlemesine esas alış bedeli kaç ₺'dir?",
        {
            "A": "388.000",
            "B": "412.000",
            "C": "400.000",
            "D": "12.000",
            "E": "Gerçeğe uygun değeri bilinmediği için belirlenemez.",
        },
        "C",
        "VUK'ta alış bedeli, iktisadi kıymetin satın alma bedelidir; iktisapla ilgili diğer giderler alış bedeline dahil değildir. Bu nedenle hisse senetlerinin değerlemesine esas tutar **400.000 ₺**dir; ayrıca ödenen 12.000 ₺ komisyon bu tutara eklenmez.",
        "VUK m. 268/A ve 279",
    ),
    "finmuh-malidv-gen-0033": financial_investment_patch(
        "Bir işletme TMS 27 kapsamında bireysel finansal tablo hazırlamakta ve aynı yatırım kategorisinde iki iştirak bulundurmaktadır. İşletme ilk iştiraki maliyet bedeliyle, ikinci iştiraki ise geçerli bir neden göstermeksizin özkaynak yöntemiyle izlemek istemektedir. En uygun değerlendirme hangisidir?",
        {
            "A": "Her iki iştirak farklı şirkete ait olduğundan yöntemler serbestçe farklı olabilir.",
            "B": "Aynı yatırım kategorisi için aynı muhasebeleştirme esası uygulanmalıdır.",
            "C": "Bireysel finansal tablolarda iştirakler yalnız TFRS 9'a göre ölçülebilir.",
            "D": "İkinci iştirakin oy hakkı %20'yi aşıyorsa mutlaka maliyet yöntemi uygulanır.",
            "E": "Yöntem tutarlılığı yalnız bağlı ortaklıklar için aranır.",
        },
        "B",
        "TMS 27 üç muhasebeleştirme esasına izin verse de işletme **her bir yatırım kategorisi için aynı esası** uygular. Aynı kategoride bulunan iki iştirak için yatırım bazında maliyet ve özkaynak yöntemlerinin keyfî biçimde farklılaştırılması uygun değildir.",
        "TMS 27, par. 10",
    ),
    "finmuh-malidv-gen-0037": financial_investment_patch(
        "İşletme %25 pay sahibi olduğu iştirak yatırımını özkaynak yöntemiyle 400.000 ₺'den izlemeye başlamıştır. İştirak 160.000 ₺ dönem kârı açıklamış ve daha sonra toplam 80.000 ₺ temettü dağıtmıştır. Başka değişiklik yoksa yatırımın yeni defter değeri kaç ₺ olur?",
        {
            "A": "380.000",
            "B": "400.000",
            "C": "440.000",
            "D": "420.000",
            "E": "460.000",
        },
        "D",
        "Kârdan pay 160.000 × %25 = **40.000 ₺** ile yatırım artar; temettü payı 80.000 × %25 = **20.000 ₺** ile yatırım azalır. Yeni defter değeri 400.000 + 40.000 − 20.000 = **420.000 ₺**dir.",
        "TMS 28, par. 10",
    ),
    "finmuh-malidv-gen-0039": financial_investment_patch(
        "TFRS 10'a göre bir yatırımcının elinde yalnız yatırım yaptığı işletmedeki payını korumaya yönelik koruyucu hakların bulunması hangi sonucu doğurur?",
        {
            "A": "Koruyucu haklar tek başına yatırım yapılan işletme üzerinde güç sağlamaz.",
            "B": "Yatırımcının oy oranı ne olursa olsun kontrol bulunduğu kabul edilir.",
            "C": "Yatırımcı önemli faaliyetleri yönetmiş sayılır.",
            "D": "Koruyucu haklar müşterek kontrolün kesin kanıtıdır.",
            "E": "Yatırım doğrudan bağlı ortaklık olarak konsolide edilir.",
        },
        "A",
        "Koruyucu haklar, sahibinin menfaatini korumak üzere tasarlanır; ilgili faaliyetleri yönetme imkânı vermez. Bu nedenle yalnız koruyucu haklara sahip bir yatırımcı, bu haklar nedeniyle yatırım yapılan işletme üzerinde **güç sahibi olmaz**.",
        "TFRS 10, par. 14 ve B27",
    ),
    "finmuh-malidv-gen-0041": financial_investment_patch(
        "Bir işletme yatırım yapılan şirketin oy haklarının %18'ine sahiptir. İşletmenin yönetim kurulunda daimi temsilcisi bulunmakta ve iki şirket arasında önemli hacimde işlemler yapılmaktadır. TMS 28'e göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "%20'nin altındaki oy oranına rağmen mevcut kanıtlar önemli etkinin bulunduğunu gösterebilir.",
            "B": "%20'nin altında kalındığı için yönetim kurulunda temsil ve işletmeler arasındaki önemli işlem hacmi gibi kanıtlar dikkate alınmadan önemli etki reddedilir.",
            "C": "Önemli işlemlerin bulunması yalnız kontrolün kanıtıdır.",
            "D": "Yönetim kurulunda temsil edilme, önemli etki değerlendirmesinde dikkate alınmaz.",
            "E": "%18 oy hakkı yatırımcıyı otomatik olarak bağlı ortaklık sahibi yapar.",
        },
        "A",
        "%20'nin altında oy hakkı bulunması önemli etkinin olmadığına ilişkin aksi ispat edilebilir bir varsayımdır. **Yönetim kurulunda temsil** ve yatırım yapılan işletmeyle **önemli işlemler** bulunması, önemli etkinin varlığını açıkça gösterebilir.",
        "TMS 28, par. 5-6",
    ),
    "finmuh-malidv-gen-0042": financial_investment_patch(
        "İşletme, %30 pay sahibi olduğu iştirak yatırımını özkaynak yöntemiyle 600.000 ₺'den izlemektedir. İştirak 300.000 ₺ dönem kârı, 50.000 ₺ diğer kapsamlı gelir açıklamış ve toplam 100.000 ₺ temettü dağıtmıştır. Başka değişiklik yoksa aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Yatırımın defter değeri 690.000 ₺, kâr veya zarara alınan pay 60.000 ₺'dir.",
            "B": "Yatırımın defter değeri 645.000 ₺, diğer kapsamlı gelire alınan pay 30.000 ₺'dir.",
            "C": "Yatırımın defter değeri 705.000 ₺ olur; kâr payı 90.000 ₺, diğer kapsamlı gelir payı 15.000 ₺ ve temettü geliri 30.000 ₺ ayrıca raporlanır.",
            "D": "Yatırımın defter değeri 660.000 ₺, diğer kapsamlı gelir payı dikkate alınmaz.",
            "E": "Yatırımın defter değeri 675.000 ₺; kâr veya zarara 90.000 ₺, diğer kapsamlı gelire 15.000 ₺ pay yansıtılır.",
        },
        "E",
        "Kâr payı 300.000 × %30 = **90.000 ₺**, diğer kapsamlı gelir payı 50.000 × %30 = **15.000 ₺** ve temettü payı 100.000 × %30 = **30.000 ₺**dir. Defter değeri 600.000 + 90.000 + 15.000 − 30.000 = **675.000 ₺** olur.",
        "TMS 28, par. 10",
    ),
    "finmuh-malidv-gen-0043": financial_investment_patch(
        "TMS 27 kapsamında bireysel finansal tablo hazırlayan bir işletme, bağlı ortaklık yatırımlarını maliyet bedeliyle; iştirak yatırımlarını ise özkaynak yöntemiyle muhasebeleştirmeyi seçmiştir. Bu uygulama için en uygun ifade hangisidir?",
        {
            "A": "Bağlı ortaklık, iş ortaklığı ve iştiraklerin tamamında tek bir yöntem uygulanması zorunlu olduğundan kategoriler ayrı ayrı tutarlı olsa bile bu uygulama mümkün değildir.",
            "B": "Her yatırım kategorisi kendi içinde tutarlı olmak şartıyla farklı kategoriler için farklı esaslar seçilebilir.",
            "C": "Bağlı ortaklıklar bireysel finansal tablolarda yalnız konsolide edilerek gösterilir.",
            "D": "İştirak yatırımlarında özkaynak yöntemi TMS 27 tarafından yasaklanmıştır.",
            "E": "Maliyet bedeli yalnız iş ortaklıklarında kullanılabilir.",
        },
        "B",
        "TMS 27'de tutarlılık **her bir yatırım kategorisi** bakımından aranır. Bu nedenle bağlı ortaklık kategorisinin tamamında maliyet, iştirak kategorisinin tamamında özkaynak yöntemi uygulanması mümkündür.",
        "TMS 27, par. 10",
    ),
    "finmuh-malidv-gen-0044": financial_investment_patch(
        "Özkaynak yöntemiyle izlenen bir iştirak yatırımının defter değerine edinimde ortaya çıkan şerefiye de dâhildir. Değer düşüklüğüne ilişkin tarafsız kanıt bulunduğunda TMS 28'e göre nasıl test yapılır?",
        {
            "A": "Şerefiye yatırımdan ayrıştırılarak ayrı bir varlık gibi her yıl amortismana ve ayrıca bağımsız değer düşüklüğü testine tabi tutulur.",
            "B": "Yalnız iştirakin dağıttığı temettü tutarı test edilir.",
            "C": "Yatırımın defter değeri azaltılmadan sadece dipnot açıklaması yapılır.",
            "D": "Şerefiye ayrıca ayrıştırılmadan yatırımın net tamamı TMS 36 kapsamında tek bir varlık gibi test edilir.",
            "E": "Değer düşüklüğü testi yalnız oy oranı %50'yi aşarsa yapılır.",
        },
        "D",
        "İştirakle ilgili şerefiye yatırımın defter değerine dâhildir ve ayrı olarak muhasebeleştirilmez. Değer düşüklüğü göstergesi varsa yatırımın **net tamamı**, şerefiye ayrıştırılmadan TMS 36 kapsamında tek bir varlık gibi test edilir.",
        "TMS 28, par. 32 ve 40-42; TMS 36",
    ),
    "finmuh-malidv-gen-0045": financial_investment_patch(
        "İşletmenin özkaynak yöntemiyle izlediği iştirak yatırımının defter değeri 100.000 ₺, net yatırımın parçası olan uzun vadeli alacağının defter değeri 30.000 ₺'dir. İştirak zararından işletmeye düşen pay 150.000 ₺ olup işletmenin iştirak adına ödeme yükümlülüğü yoktur. TMS 28'e göre kaç ₺ zarar finansal tablolara yansıtılır?",
        {
            "A": "130.000",
            "B": "150.000",
            "C": "100.000",
            "D": "30.000",
            "E": "20.000",
        },
        "A",
        "Zarar payı önce iştirak yatırımına, sonra net yatırımın parçası olan diğer uzun vadeli haklara uygulanır. Toplam net yatırım **130.000 ₺** olduğundan bu tutara kadar zarar yansıtılır. İşletmenin yasal veya zımni yükümlülüğü bulunmadığı için kalan **20.000 ₺** muhasebeleştirilmez.",
        "TMS 28, par. 38-39",
    ),
    "finmuh-malidv-gen-0046": financial_investment_patch(
        "İşletme özkaynak yöntemiyle izlediği %30'luk iştirak payının bir bölümünü satmış ve kalan %8 pay üzerinde önemli etkisini kaybetmiştir. Kalan pay bağlı ortaklık veya iş ortaklığı niteliğinde değildir. TMS 28'e göre kalan pay için nasıl işlem yapılır?",
        {
            "A": "Kalan pay yalnız %8 olmasına ve önemli etki sona ermesine rağmen önceki defter değeri üzerinden özkaynak yöntemine süresiz biçimde devam edilir.",
            "B": "Kalan pay sıfır bedelle kayıtlardan çıkarılır.",
            "C": "Kalan pay gerçeğe uygun değerle ölçülür; ilgili fark TMS 28'de belirtilen esaslarla kâr veya zarara yansıtılır.",
            "D": "Kalan pay yalnız nominal değerle 242 İştirakler hesabında tutulur.",
            "E": "Önemli etki kaybı ancak pay sıfıra indiğinde muhasebeleştirilir.",
        },
        "C",
        "Yatırım iştirak niteliğini kaybettiğinde özkaynak yöntemi bırakılır. Kalan pay bir finansal varlıksa **gerçeğe uygun değerle** ölçülür; elden çıkarma geliri ile kalan payın gerçeğe uygun değeri toplamının önceki defter değeriyle farkı kâr veya zarara yansıtılır.",
        "TMS 28, par. 22",
    ),
    "finmuh-malidv-gen-0048": financial_investment_patch(
        "TMS 27 kapsamında bireysel finansal tablolarda bir iştirak yatırımından alınan temettünün muhasebeleştirilmesi, seçilen yönteme göre nasıl farklılaşır?",
        {
            "A": "Hem maliyet hem özkaynak yönteminde yatırımın defter değerini artırır.",
            "B": "Her iki yöntemde de doğrudan diğer kapsamlı gelire alınır.",
            "C": "Maliyet yönteminde yatırımın defter değeri azaltılıp temettü ayrıca diğer kapsamlı gelire alınır; özkaynak yönteminde ise dağıtımın tamamı hasılat yazılır.",
            "D": "Özkaynak yöntemi seçilmemişse hak doğduğunda kâr veya zarara alınır; özkaynak yönteminde yatırımın defter değerini azaltır.",
            "E": "Temettü hiçbir yöntemde finansal tablolara yansıtılmaz.",
        },
        "D",
        "TMS 27'ye göre temettü alma hakkı doğduğunda, **özkaynak yöntemi seçilmemişse** temettü kâr veya zarara yansıtılır. **Özkaynak yöntemi seçilmişse** dağıtım yatırımın defter değerini azaltır; ayrıca temettü geliri olarak ikinci kez kâr yazılmaz.",
        "TMS 27, par. 12; TMS 28, par. 10",
    ),
    "finmuh-malidv-gen-0049": financial_investment_patch(
        "Bir yatırımcı, hâlen kullanılabilir durumda olan ve kullanıldığında yatırım yapılan işletmede ilave oy hakkı sağlayacak pay alım opsiyonlarına sahiptir. TMS 28'e göre önemli etki değerlendirmesinde bu haklar için hangi işlem yapılır?",
        {
            "A": "Mevcut durumda kullanılabilir potansiyel oy haklarının varlığı ve etkisi değerlendirmede dikkate alınır.",
            "B": "Potansiyel oy hakları dikkate alınmaz.",
            "C": "Yalnız yönetimin opsiyonu kullanma niyeti varsa önemli etki doğar.",
            "D": "Opsiyonlar otomatik olarak yatırımcıya kontrol sağlar.",
            "E": "Potansiyel oy hakları raporlama tarihinde kullanılabilir durumda olsa bile ancak fiilen kullanıldıktan sonraki hesap döneminin önemli etki değerlendirmesine alınır.",
        },
        "A",
        "TMS 28, **hâlen kullanılabilir veya dönüştürülebilir** potansiyel oy haklarının önemli etki değerlendirmesinde dikkate alınmasını ister. Yönetimin bu hakları kullanma isteği veya finansal yeterliliği tek başına belirleyici değildir.",
        "TMS 28, par. 7-8",
    ),
    "finmuh-malidv-gen-0050": financial_investment_patch(
        "TFRS 10'a göre kontrolün değerlendirilmesiyle ilgili aşağıdaki ifadelerden hangisi doğrudur?",
        {
            "A": "Kontrol yalnız sermaye payı %50'yi aştığında doğabilir.",
            "B": "Yatırım yapılan işletmenin değişken getirilerine maruz kalmak, ilgili faaliyetleri yönetme gücü veya bu gücü getirileri etkilemekte kullanma imkânı bulunmasa da tek başına kontrol için yeterlidir.",
            "C": "Yatırımın uzun vadeli tutulması kontrolün kesin kanıtıdır.",
            "D": "En az %20 oy hakkı bulunan bütün yatırımlar bağlı ortaklıktır.",
            "E": "Güç sözleşmeden de doğabilir; güç, değişken getiriler ve gücü getirileri etkilemekte kullanabilme birlikte aranır.",
        },
        "E",
        "TFRS 10 kontrolü tek bir sahiplik eşiğine indirgemez. Güç oy haklarından veya **sözleşmeye dayalı mevcut haklardan** doğabilir; güç, değişken getiriler ve gücü bu getirileri etkilemek için kullanabilme unsurları birlikte bulunmalıdır.",
        "TFRS 10, par. 6-7 ve 10-11",
    ),
    "finmuh-malidv-gen-0052": financial_investment_patch(
        "TMS 28'deki önemli etki kavramını en doğru açıklayan ifade hangisidir?",
        {
            "A": "Finansal ve faaliyet politikası kararlarına katılma gücüdür; tek başına veya müşterek kontrol değildir.",
            "B": "Yatırım yapılan işletmenin bütün ilgili faaliyetlerini tek başına yönetme gücüdür.",
            "C": "Yalnız sermaye payının %10 ile %50 arasında olmasıdır.",
            "D": "Yatırım yapılan işletmenin borçlarını ödeme yükümlülüğüdür.",
            "E": "Yatırım yapılan işletmenin getirilerini önemli ölçüde etkileyen faaliyetlere ilişkin kararların iki veya daha fazla tarafın oy birliğiyle alınmasını gerektiren müşterek kontroldür.",
        },
        "A",
        "Önemli etki, yatırım yapılan işletmenin finansal ve faaliyet politikalarıyla ilgili kararlarına **katılma gücüdür**; bu politikaları tek başına veya bir başka tarafla müştereken kontrol etme gücü değildir. Tekdüzen Hesap Planı'ndaki hesap eşiği, TMS 28 tanımının yerine geçmez.",
        "TMS 28, par. 3",
    ),
    "finmuh-malidv-gen-0053": financial_investment_patch(
        "İşletme, özkaynak yöntemiyle izlediği iştirakte %25 pay sahibidir. İştirak dönem içinde 120.000 ₺ tutarında diğer kapsamlı gelir muhasebeleştirmiştir. Başka değişiklik yoksa yatırımcı hangi işlemi yapar?",
        {
            "A": "120.000 ₺'nin tamamını temettü geliri yazar.",
            "B": "30.000 ₺'yi yalnız kâr veya zararda iştirak kazancı olarak muhasebeleştirir; diğer kapsamlı gelire hiçbir pay yansıtmaz ve yatırımın defter değerini değiştirmez.",
            "C": "Diğer kapsamlı gelir yatırımcıyı etkilemediği için kayıt yapmaz.",
            "D": "30.000 ₺'yi kendi diğer kapsamlı gelirine yansıtır ve yatırımın defter değerini aynı tutarda artırır.",
            "E": "120.000 ₺'yi yatırımın defter değerinden düşer.",
        },
        "D",
        "Yatırımcı, iştirakin diğer kapsamlı gelirinden payına düşen 120.000 × %25 = **30.000 ₺**yi kendi diğer kapsamlı gelirinde muhasebeleştirir. Bu tutar aynı zamanda özkaynak yöntemiyle izlenen yatırımın defter değerini artırır.",
        "TMS 28, par. 10",
    ),
    "finmuh-malidv-gen-0054": financial_investment_patch(
        "VUK'un menkul kıymetlerin değerlemesine ilişkin hükmüne göre, iştirak amacıyla elde tutulan hisse senetleri dönem sonunda hangi değerle değerlenir?",
        {
            "A": "Her durumda borsa rayiciyle",
            "B": "Nominal değerle",
            "C": "Alış bedeliyle",
            "D": "Tasarruf değeriyle",
            "E": "İtfa edilmiş maliyetle",
        },
        "C",
        "VUK 279 uyarınca **hisse senetleri alış bedeliyle** değerlenir. Bu vergi değerleme kuralı, TFRS finansal tablolarında uygulanabilecek ölçüm esaslarıyla karıştırılmamalıdır.",
        "VUK m. 279",
    ),
    "finmuh-malidv-gen-0055": financial_investment_patch(
        "İşletme aynı iştirake ait paylardan önce 100 adedini birim 80 ₺'ye, daha sonra 100 adedini birim 100 ₺'ye almıştır. Payların 120 adedi birim 130 ₺'ye satılmıştır. Kısmi satışta ilk giren ilk çıkar yöntemi uygulandığına göre satılan payların maliyeti kaç ₺'dir?",
        {
            "A": "10.000",
            "B": "9.600",
            "C": "10.800",
            "D": "12.000",
            "E": "15.600",
        },
        "A",
        "İlk giren ilk çıkar yönteminde önce ilk alınan 100 payın 100 × 80 = **8.000 ₺**, sonra ikinci partiden 20 payın 20 × 100 = **2.000 ₺** maliyeti satışa verilir. Toplam maliyet **10.000 ₺**dir.",
        "VUK m. 279; GİB iştirak hissesi kısmi satışlarında maliyet tespiti görüşü",
    ),
    "finmuh-malidv-gen-0059": financial_investment_patch(
        "Bir ana ortaklık, bağlı ortaklığının kontrolünü 1 Nisan'da elde etmiş ve 30 Eylül'de kaybetmiştir. TFRS 10'a göre bağlı ortaklığın gelir ve giderleri hangi dönem için konsolide finansal tablolara dâhil edilir?",
        {
            "A": "Kontrol yılın yalnız bir bölümünde bulunmuş olsa da 1 Ocak-31 Aralık arasındaki tüm hesap dönemi için",
            "B": "Kontrolün elde edildiği 1 Nisan'dan kaybedildiği 30 Eylül'e kadar",
            "C": "Yalnız 30 Eylül tarihindeki bir günlük dönem için",
            "D": "Kontrol kaybedildikten sonraki dönem için",
            "E": "Yalnız pay oranı %100 ise 1 Nisan-30 Eylül arası için",
        },
        "B",
        "TFRS 10'a göre bağlı ortaklığın gelir ve giderleri, ana ortaklığın **kontrol sahibi olduğu tarihten kontrolü kaybettiği tarihe kadar** konsolide finansal tablolara alınır. Bu nedenle dönem 1 Nisan-30 Eylül'dür.",
        "TFRS 10, B88",
    ),
    "finmuh-malidv-gen-0060": financial_investment_patch(
        "Mali duran varlık sınıflaması ve finansal raporlama standartlarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Tekdüzen Hesap Planı'nda 242 İştirakler hesabı için en az %10 oy veya yönetime katılma hakkı ölçütü bulunur.\n\nII. TMS 28'de %20 veya daha fazla oy hakkı, aksi açıkça ortaya konulmadıkça önemli etki varsayımı oluşturur.\n\nIII. TFRS 10'da kontrol yalnız oy haklarının %50'yi aşmasıyla kurulabilir.",
        {
            "A": "Yalnız I",
            "B": "Yalnız II",
            "C": "Yalnız III",
            "D": "I ve II",
            "E": "I, II ve III",
        },
        "D",
        "I ve II doğrudur. Tekdüzen Hesap Planı'nın **hesap sınıflama ölçütü** ile TMS 28'in **aksi kanıtlanabilir önemli etki varsayımı** farklıdır. III yanlıştır; TFRS 10'da kontrol güç, değişken getiriler ve gücü getirileri etkilemek için kullanabilme unsurlarına bağlıdır ve sözleşmeye dayalı haklardan da doğabilir.",
        "1 Sıra No'lu MSUGT - 242; TMS 28, par. 5; TFRS 10, par. 6-7",
    ),
}


INCOME_STATEMENT_PATCHES = {
    "finmuh-gt-gen-0009": income_statement_patch(
        "Bir işletmenin brüt satışları 920.000 ₺, satıştan iadeleri 46.000 ₺ ve satış iskontoları 24.000 ₺'dir. Başka satış indirimi bulunmamaktadır.\n\nİşletmenin net satışları kaç ₺'dir?",
        {
            "A": "874.000",
            "B": "850.000",
            "C": "896.000",
            "D": "966.000",
            "E": "990.000",
        },
        "B",
        "Net satışlar = brüt satışlar − satıştan iadeler − satış iskontolarıdır. Buna göre 920.000 − 46.000 − 24.000 = **850.000 ₺** net satışa ulaşılır.",
        "1 Sıra No'lu MSUGT - Gelir tablosu biçimi ve 60/61 hesap grupları",
    ),
    "finmuh-gt-gen-0011": income_statement_patch(
        "Net satışları 600.000 ₺ olan işletmenin brüt satış kârı oranı %30'dur.\n\nİşletmenin satışlarının maliyeti kaç ₺'dir?",
        {
            "A": "180.000",
            "B": "300.000",
            "C": "390.000",
            "D": "420.000",
            "E": "780.000",
        },
        "D",
        "Brüt satış kârı 600.000 × %30 = 180.000 ₺'dir. Satışların maliyeti = net satışlar − brüt satış kârı olduğundan 600.000 − 180.000 = **420.000 ₺** bulunur.",
        "1 Sıra No'lu MSUGT - Brüt satış kârı; 2024-2025 SGS dikey yüzde soru örüntüsü",
    ),
    "finmuh-gt-gen-0013": income_statement_patch(
        "Bir işletmenin ortalama stokları 40.000 ₺, stok devir hızı 3 ve brüt satış kârı oranı %40'tır. Dönemin faaliyet giderleri toplamı 35.000 ₺'dir.\n\nBuna göre işletmenin faaliyet kârı kaç ₺'dir?",
        {
            "A": "45.000",
            "B": "35.000",
            "C": "65.000",
            "D": "80.000",
            "E": "85.000",
        },
        "A",
        "Satışların maliyeti = 40.000 × 3 = 120.000 ₺'dir. Brüt kâr oranı %40 ise maliyet net satışların %60'ıdır; net satışlar 120.000 / %60 = 200.000 ₺, brüt kâr 80.000 ₺ olur. Faaliyet kârı 80.000 − 35.000 = **45.000 ₺**'dir.",
        "1 Sıra No'lu MSUGT - Faaliyet kârı; 2025 SGS stok devir hızı ve brüt kâr oranı soru örüntüsü",
    ),
    "finmuh-gt-gen-0022": income_statement_patch(
        "Sürekli envanter yöntemini kullanan işletmede, daha önce kredili satılan malın 12.000 ₺ + %20 KDV tutarındaki kısmı müşteri tarafından iade edilmiştir. İade edilen malın maliyeti 8.000 ₺'dir.\n\nİade tarihinde yapılması gereken kayıtlar hangisidir?",
        {
            "A": "120 Alıcılar 14.400 ₺ borç / 600 Yurt İçi Satışlar 12.000 ₺ ve 391 Hesaplanan KDV 2.400 ₺ alacak",
            "B": "610 Satıştan İadeler 12.000 ₺ borç / 120 Alıcılar 12.000 ₺ alacak; maliyet kaydı yapılmaz",
            "C": "610 Satıştan İadeler 14.400 ₺ borç / 120 Alıcılar 14.400 ₺ alacak; 621 Satılan Ticari Mallar Maliyeti 8.000 ₺ borç / 153 Ticari Mallar 8.000 ₺ alacak",
            "D": "153 Ticari Mallar 12.000 ₺ borç / 610 Satıştan İadeler 12.000 ₺ alacak; 391 Hesaplanan KDV 2.400 ₺ borç / 120 Alıcılar 2.400 ₺ alacak",
            "E": "610 Satıştan İadeler 12.000 ₺ ve 391 Hesaplanan KDV 2.400 ₺ borç / 120 Alıcılar 14.400 ₺ alacak; 153 Ticari Mallar 8.000 ₺ borç / 621 Satılan Ticari Mallar Maliyeti 8.000 ₺ alacak",
        },
        "E",
        "Satış iadesi hasılatı ve satışta doğan KDV'yi tersine çevirir: 610 ve 391 borç, 120 alacak kaydedilir. Sürekli envanter yönteminde mal yeniden stoka girdiği için ayrıca **153 borç / 621 alacak 8.000 ₺** kaydı yapılır.",
        "1 Sıra No'lu MSUGT - 120/153/391/610/621",
    ),
    "finmuh-gt-gen-0023": income_statement_patch(
        "İşletme, daha önce 100.000 ₺ + %20 KDV ile kredili sattığı mal için müşterisine 10.000 ₺ + %20 KDV tutarında satış iskontosu yapmıştır. İskonto tutarı müşterinin borcundan düşülmüştür.\n\nİskonto kaydı hangisidir?",
        {
            "A": "120 Alıcılar 12.000 ₺ borç / 611 Satış İskontoları 10.000 ₺ ve 391 Hesaplanan KDV 2.000 ₺ alacak",
            "B": "611 Satış İskontoları 12.000 ₺ borç / 120 Alıcılar 12.000 ₺ alacak",
            "C": "611 Satış İskontoları 10.000 ₺ ve 391 Hesaplanan KDV 2.000 ₺ borç / 120 Alıcılar 12.000 ₺ alacak",
            "D": "612 Diğer İndirimler 10.000 ₺ ve 191 İndirilecek KDV 2.000 ₺ borç / 120 Alıcılar 12.000 ₺ alacak",
            "E": "611 Satış İskontoları 10.000 ₺ borç / 120 Alıcılar 10.000 ₺ alacak; KDV için kayıt yapılmaz",
        },
        "C",
        "Satış iskontosu net satışları azaltan 611 hesaba borç yazılır. İskontoya isabet eden hesaplanan KDV de 391 hesabın borcuna alınır; müşteri borcu toplam **12.000 ₺** azaltılır.",
        "1 Sıra No'lu MSUGT - 120/391/611",
    ),
    "finmuh-gt-gen-0024": income_statement_patch(
        "Aralıklı envanter yöntemini kullanan bir ticaret işletmesinin dönem başı mal mevcudu 70.000 ₺, dönem içi mal alışları 400.000 ₺, alış iadeleri 20.000 ₺ ve alışlara ait taşıma giderleri 10.000 ₺'dir. Dönem sonu mal mevcudu 90.000 ₺'dir.\n\nSatılan ticari malların maliyeti kaç ₺'dir?",
        {
            "A": "350.000",
            "B": "370.000",
            "C": "390.000",
            "D": "410.000",
            "E": "460.000",
        },
        "B",
        "Net alışlar = 400.000 − 20.000 + 10.000 = 390.000 ₺'dir. Satılan ticari mallar maliyeti = 70.000 + 390.000 − 90.000 = **370.000 ₺** olarak hesaplanır.",
        "1 Sıra No'lu MSUGT - 153/621; aralıklı envanter maliyet akışı",
    ),
    "finmuh-gt-gen-0025": income_statement_patch(
        "Bir işletmenin brüt satışları 500.000 ₺, satıştan iadeleri 20.000 ₺, satış iskontoları 10.000 ₺ ve satışların maliyeti 300.000 ₺'dir. Pazarlama, satış ve dağıtım giderleri 60.000 ₺; genel yönetim giderleri 40.000 ₺'dir.\n\nİşletmenin faaliyet kârı kaç ₺'dir?",
        {
            "A": "30.000",
            "B": "40.000",
            "C": "100.000",
            "D": "170.000",
            "E": "70.000",
        },
        "E",
        "Net satışlar 500.000 − 20.000 − 10.000 = 470.000 ₺; brüt satış kârı 470.000 − 300.000 = 170.000 ₺'dir. Faaliyet kârı 170.000 − 60.000 − 40.000 = **70.000 ₺** olur.",
        "1 Sıra No'lu MSUGT - Net satışlardan faaliyet kârına geçiş",
    ),
    "finmuh-gt-gen-0026": income_statement_patch(
        "Faaliyet kârı 160.000 ₺ olan işletmenin faiz gelirleri 25.000 ₺, kambiyo kârları 15.000 ₺, kambiyo zararları 20.000 ₺ ve finansman giderleri 30.000 ₺'dir. Başka olağan gelir veya gider yoktur.\n\nİşletmenin olağan kârı kaç ₺'dir?",
        {
            "A": "150.000",
            "B": "130.000",
            "C": "140.000",
            "D": "170.000",
            "E": "200.000",
        },
        "A",
        "Olağan kâr = 160.000 + 25.000 + 15.000 − 20.000 − 30.000 = **150.000 ₺**'dir. 642 ve 646 olağan geliri; 656 ile finansman giderleri olağan sonucu azaltan kalemleri temsil eder.",
        "1 Sıra No'lu MSUGT - 642/646/656/66 hesap grubu",
    ),
    "finmuh-gt-gen-0027": income_statement_patch(
        "Maliyeti 200.000 ₺, birikmiş amortismanı 140.000 ₺ olan makine, esas faaliyet konusu duran varlık ticareti olmayan işletme tarafından 80.000 ₺ + %20 KDV ile kredili satılmıştır.\n\nSatış kaydında 679 Diğer Olağandışı Gelir ve Kârlar hesabına yazılacak tutar kaç ₺'dir?",
        {
            "A": "80.000",
            "B": "16.000",
            "C": "60.000",
            "D": "20.000",
            "E": "140.000",
        },
        "D",
        "Makinenin net defter değeri 200.000 − 140.000 = 60.000 ₺'dir. KDV hariç satış bedeli 80.000 ₺ olduğundan duran varlık satış kârı 80.000 − 60.000 = **20.000 ₺**'dir ve 679 hesaba alacak kaydedilir.",
        "1 Sıra No'lu MSUGT - 120/253/257/391/679; 2025-2026 SGS duran varlık satışı soru örüntüsü",
    ),
    "finmuh-gt-gen-0028": income_statement_patch(
        "Bir işletmenin brüt satışları 90.000 ₺, satıştan iadeleri 10.000 ₺ ve satışların maliyeti 32.000 ₺'dir. Brüt satış kârı, dönem net kârının üç katıdır.\n\nİşletmenin dönem net kârı kaç ₺'dir?",
        {
            "A": "12.000",
            "B": "14.000",
            "C": "16.000",
            "D": "24.000",
            "E": "48.000",
        },
        "C",
        "Net satışlar 90.000 − 10.000 = 80.000 ₺; brüt satış kârı 80.000 − 32.000 = 48.000 ₺'dir. Brüt kâr net kârın üç katı olduğundan dönem net kârı 48.000 / 3 = **16.000 ₺** bulunur.",
        "1 Sıra No'lu MSUGT - Gelir tablosu kâr basamakları; 13 Temmuz 2024 SGS soru örüntüsü",
    ),
    "finmuh-gt-gen-0036": income_statement_patch(
        "Esas faaliyet konusu taşınmaz kiralama olmayan işletmenin, başka bir işletmeye kiraya verdiği deposuna ait 18.000 ₺ tutarındaki cari dönem kira geliri dönem sonunda tahakkuk etmiş; bedel henüz tahsil edilmemiştir.\n\nYapılacak kayıt hangisidir?",
        {
            "A": "102 Bankalar 18.000 ₺ borç / 600 Yurt İçi Satışlar 18.000 ₺ alacak",
            "B": "181 Gelir Tahakkukları 18.000 ₺ borç / 649 Diğer Olağan Gelir ve Kârlar 18.000 ₺ alacak",
            "C": "649 Diğer Olağan Gelir ve Kârlar 18.000 ₺ borç / 181 Gelir Tahakkukları 18.000 ₺ alacak",
            "D": "180 Gelecek Aylara Ait Giderler 18.000 ₺ borç / 649 Diğer Olağan Gelir ve Kârlar 18.000 ₺ alacak",
            "E": "181 Gelir Tahakkukları 18.000 ₺ borç / 679 Diğer Olağandışı Gelir ve Kârlar 18.000 ₺ alacak",
        },
        "B",
        "Cari döneme ait fakat henüz tahsil edilmemiş gelir **181 Gelir Tahakkukları** hesabında varlık olarak izlenir. Esas faaliyet dışında olmakla birlikte olağan nitelikteki kira geliri **649 Diğer Olağan Gelir ve Kârlar** hesabına alacak yazılır.",
        "1 Sıra No'lu MSUGT - 181/649",
    ),
    "finmuh-gt-gen-0037": income_statement_patch(
        "Bir işletmenin satışlarının maliyeti 90.000 ₺, brüt satış kârı oranı %25 ve faaliyet giderleri 18.000 ₺'dir. Başka faaliyet geliri veya gideri yoktur.\n\nİşletmenin faaliyet kârı kaç ₺'dir?",
        {
            "A": "7.500",
            "B": "18.000",
            "C": "22.500",
            "D": "30.000",
            "E": "12.000",
        },
        "E",
        "Brüt kâr oranı %25 ise maliyet net satışların %75'idir. Net satışlar 90.000 / %75 = 120.000 ₺, brüt kâr 30.000 ₺ olur. Faaliyet kârı 30.000 − 18.000 = **12.000 ₺**'dir.",
        "1 Sıra No'lu MSUGT - Brüt ve faaliyet kârı; 2024-2025 SGS dikey yüzde soru örüntüsü",
    ),
    "finmuh-gt-gen-0038": income_statement_patch(
        "Faaliyet kârı 120.000 ₺ olan işletmenin diğer faaliyetlerden olağan gelirleri 30.000 ₺, diğer faaliyetlerden olağan giderleri 10.000 ₺ ve finansman giderleri 25.000 ₺'dir. Ayrıca 8.000 ₺ olağandışı gelir ve 3.000 ₺ olağandışı gider bulunmaktadır.\n\nİşletmenin olağan kârı ile vergi öncesi dönem kârı sırasıyla kaç ₺'dir?",
        {
            "A": "115.000 ve 120.000",
            "B": "120.000 ve 115.000",
            "C": "140.000 ve 145.000",
            "D": "115.000 ve 112.000",
            "E": "145.000 ve 150.000",
        },
        "A",
        "Olağan kâr = 120.000 + 30.000 − 10.000 − 25.000 = **115.000 ₺**'dir. Vergi öncesi dönem kârı = 115.000 + 8.000 − 3.000 = **120.000 ₺** olur.",
        "1 Sıra No'lu MSUGT - Gelir tablosu kâr basamakları",
    ),
    "finmuh-gt-gen-0040": income_statement_patch(
        "Dönem sonunda 600 Yurt İçi Satışlar hesabı 500.000 ₺, 642 Faiz Gelirleri hesabı 20.000 ₺ ve 679 Diğer Olağandışı Gelir ve Kârlar hesabı 10.000 ₺ alacak kalanı vermektedir.\n\nBu gelir hesaplarının 690 Dönem Kârı veya Zararı hesabına devrinde yapılacak kayıt hangisidir?",
        {
            "A": "690 Dönem Kârı veya Zararı 530.000 ₺ borç / 600, 642 ve 679 hesapları toplam 530.000 ₺ alacak",
            "B": "600, 642 ve 679 hesapları toplam 530.000 ₺ borç / 692 Dönem Net Kârı veya Zararı 530.000 ₺ alacak",
            "C": "600, 642 ve 679 hesapları toplam 530.000 ₺ borç / 690 Dönem Kârı veya Zararı 530.000 ₺ alacak",
            "D": "600 Yurt İçi Satışlar 500.000 ₺ borç / 690 Dönem Kârı veya Zararı 500.000 ₺ alacak; diğer gelirler devredilmez",
            "E": "690 Dönem Kârı veya Zararı 530.000 ₺ borç / 692 Dönem Net Kârı veya Zararı 530.000 ₺ alacak",
        },
        "C",
        "Alacak kalanı veren gelir hesapları kapatılırken **borçlandırılır**; toplam 500.000 + 20.000 + 10.000 = **530.000 ₺**, 690 hesabın alacağına devredilir.",
        "1 Sıra No'lu MSUGT - Gelir hesaplarının 690 hesaba devri",
    ),
    "finmuh-gt-gen-0041": income_statement_patch(
        "Dönem sonunda 621 Satılan Ticari Mallar Maliyeti 280.000 ₺, 632 Genel Yönetim Giderleri 50.000 ₺, 656 Kambiyo Zararları 15.000 ₺ ve 660 Kısa Vadeli Borçlanma Giderleri 20.000 ₺ borç kalanı vermektedir.\n\nBu gider hesaplarının dönem sonu devrine ilişkin doğru kayıt hangisidir?",
        {
            "A": "621, 632, 656 ve 660 hesapları toplam 365.000 ₺ borç / 690 Dönem Kârı veya Zararı 365.000 ₺ alacak",
            "B": "690 Dönem Kârı veya Zararı 350.000 ₺ borç / 621, 632 ve 660 hesapları 350.000 ₺ alacak; 656 devredilmez",
            "C": "692 Dönem Net Kârı veya Zararı 365.000 ₺ borç / gider hesapları toplam 365.000 ₺ alacak",
            "D": "690 Dönem Kârı veya Zararı 365.000 ₺ borç / 621, 632, 656 ve 660 hesapları toplam 365.000 ₺ alacak",
            "E": "Gider hesapları sonraki döneme devrettiği için kapanış kaydı yapılmaz",
        },
        "D",
        "Borç kalanı veren gider hesapları kapatılırken alacaklandırılır. Toplam gider 280.000 + 50.000 + 15.000 + 20.000 = **365.000 ₺** olduğundan aynı tutar 690 hesabın borcuna yazılır.",
        "1 Sıra No'lu MSUGT - Gider hesaplarının 690 hesaba devri",
    ),
    "finmuh-gt-gen-0042": income_statement_patch(
        "Dönem sonu aktarmalarından sonra 690 Dönem Kârı veya Zararı hesabı 260.000 ₺ alacak kalanı, 691 Dönem Kârı Vergi ve Diğer Yasal Yükümlülük Karşılıkları hesabı ise 65.000 ₺ borç kalanı vermektedir.\n\nHer iki hesap 692 hesaba devredildiğinde 692 Dönem Net Kârı veya Zararı hesabı hangi kalanı verir?",
        {
            "A": "65.000 ₺ borç kalanı",
            "B": "195.000 ₺ alacak kalanı",
            "C": "260.000 ₺ alacak kalanı",
            "D": "325.000 ₺ alacak kalanı",
            "E": "195.000 ₺ borç kalanı",
        },
        "B",
        "690 hesabın alacak kalanı vergi öncesi kârı, 691 hesabın borç kalanı vergi ve yasal yükümlülük karşılığını gösterir. Net tutar 260.000 − 65.000 = **195.000 ₺** olup 692 hesap alacak kalanı verir.",
        "1 Sıra No'lu MSUGT - 690/691/692",
    ),
    "finmuh-gt-gen-0043": income_statement_patch(
        "Dönem sonunda 692 Dönem Net Kârı veya Zararı hesabı 40.000 ₺ borç kalanı vermiştir.\n\nBu hesabın kapatılmasında yapılacak kayıt hangisidir?",
        {
            "A": "692 Dönem Net Kârı veya Zararı 40.000 ₺ borç / 590 Dönem Net Kârı 40.000 ₺ alacak",
            "B": "690 Dönem Kârı veya Zararı 40.000 ₺ borç / 591 Dönem Net Zararı 40.000 ₺ alacak",
            "C": "692 Dönem Net Kârı veya Zararı 40.000 ₺ borç / 591 Dönem Net Zararı 40.000 ₺ alacak",
            "D": "590 Dönem Net Kârı 40.000 ₺ borç / 692 Dönem Net Kârı veya Zararı 40.000 ₺ alacak",
            "E": "591 Dönem Net Zararı 40.000 ₺ borç / 692 Dönem Net Kârı veya Zararı 40.000 ₺ alacak",
        },
        "E",
        "692 hesabın borç kalanı net zararı gösterir. Bu nedenle **591 Dönem Net Zararı borçlandırılır**, 692 hesap alacaklandırılarak kapatılır. Bu kapanış biçimi 18 Temmuz 2026 SGS'de de doğrudan ölçülmüştür.",
        "1 Sıra No'lu MSUGT - 692/591; 18 Temmuz 2026 SGS soru örüntüsü",
    ),
    "finmuh-gt-gen-0044": income_statement_patch(
        "2025 hesap dönemi kapandıktan sonra, o dönemde sunulmuş ancak kayda alınmamış 30.000 ₺ tutarındaki danışmanlık hizmeti geliri 2026 yılında tespit edilmiştir. Tutar müşteriden alacaklıdır.\n\nTekdüzen Hesap Planı'na göre 2026 yılında yapılacak kayıt hangisidir?",
        {
            "A": "120 Alıcılar 30.000 ₺ borç / 671 Önceki Dönem Gelir ve Kârlar 30.000 ₺ alacak",
            "B": "120 Alıcılar 30.000 ₺ borç / 600 Yurt İçi Satışlar 30.000 ₺ alacak",
            "C": "671 Önceki Dönem Gelir ve Kârlar 30.000 ₺ borç / 120 Alıcılar 30.000 ₺ alacak",
            "D": "181 Gelir Tahakkukları 30.000 ₺ borç / 649 Diğer Olağan Gelir ve Kârlar 30.000 ₺ alacak",
            "E": "120 Alıcılar 30.000 ₺ borç / 679 Diğer Olağandışı Gelir ve Kârlar 30.000 ₺ alacak",
        },
        "A",
        "Gelir cari dönem faaliyetinden değil, kapanmış olan **önceki hesap döneminden** kaynaklanmaktadır. Tekdüzen Hesap Planı uygulamasında alacak 120 hesaba, önceki dönem geliri ise **671 hesaba** kaydedilir.",
        "1 Sıra No'lu MSUGT - 120/671",
    ),
    "finmuh-gt-gen-0045": income_statement_patch(
        "İşletme 1 Ekim 2025'te açtığı bir yıl vadeli mevduatın 31 Aralık 2025'e kadar işlemiş faizini 181 Gelir Tahakkukları hesabına kaydetmiştir. Mevduat 30 Nisan 2026'da vadesinden önce kapatılmış ve banka faiz ödememiştir.\n\n2025'te kaydedilen faiz tahakkukunun iptalinde yapılacak kayıt hangisidir?",
        {
            "A": "181 Gelir Tahakkukları borç / 681 Önceki Dönem Gider ve Zararları alacak",
            "B": "681 Önceki Dönem Gider ve Zararları borç / 181 Gelir Tahakkukları alacak",
            "C": "642 Faiz Gelirleri borç / 181 Gelir Tahakkukları alacak",
            "D": "671 Önceki Dönem Gelir ve Kârlar borç / 181 Gelir Tahakkukları alacak",
            "E": "681 Önceki Dönem Gider ve Zararları borç / 642 Faiz Gelirleri alacak",
        },
        "B",
        "2025'te varlık olarak kaydedilen faiz alacağı erken kapama nedeniyle ortadan kalkmıştır. Önceki dönemde kayda alınan bu tutar 2026'da **681 Önceki Dönem Gider ve Zararları borç / 181 Gelir Tahakkukları alacak** kaydıyla iptal edilir.",
        "1 Sıra No'lu MSUGT - 181/681; 18 Temmuz 2026 SGS soru örüntüsü",
    ),
    "finmuh-gt-gen-0046": income_statement_patch(
        "Maliyeti 100.000 ₺, ayrılmış değer düşüklüğü karşılığı 15.000 ₺ olan hisse senetleri 120.000 ₺'ye banka aracılığıyla satılmıştır. Banka 2.000 ₺ komisyon keserek kalanı hesaba aktarmıştır.\n\nSatış kaydında yer alacak hesap ve tutarlarla ilgili doğru seçenek hangisidir?",
        {
            "A": "102 Bankalar 120.000 ₺ borç; 110 Hisse Senetleri 100.000 ₺ ve 645 Menkul Kıymet Satış Kârları 20.000 ₺ alacak",
            "B": "102 Bankalar 118.000 ₺ ve 653 Komisyon Giderleri 2.000 ₺ borç; 110 Hisse Senetleri 100.000 ₺ ve 645 Menkul Kıymet Satış Kârları 20.000 ₺ alacak; karşılık kapatılmaz",
            "C": "102 Bankalar 118.000 ₺, 119 Menkul Kıymetler Değer Düşüklüğü Karşılığı 15.000 ₺ ve 645 Menkul Kıymet Satış Kârları 20.000 ₺ borç; 110 Hisse Senetleri 153.000 ₺ alacak",
            "D": "102 Bankalar 118.000 ₺, 119 Menkul Kıymetler Değer Düşüklüğü Karşılığı 15.000 ₺ ve 653 Komisyon Giderleri 2.000 ₺ borç; 110 Hisse Senetleri 100.000 ₺, 644 Konusu Kalmayan Karşılıklar 15.000 ₺ ve 645 Menkul Kıymet Satış Kârları 20.000 ₺ alacak",
            "E": "102 Bankalar 118.000 ₺ ve 119 Menkul Kıymetler Değer Düşüklüğü Karşılığı 15.000 ₺ borç; 110 Hisse Senetleri 100.000 ₺ ve 649 Diğer Olağan Gelir ve Kârlar 33.000 ₺ alacak",
        },
        "D",
        "Bankaya net 118.000 ₺ girer ve 2.000 ₺ komisyon 653 hesaba borç yazılır. Satılan menkul kıymete ait 15.000 ₺ karşılık 119 borç / 644 alacak kaydıyla kapatılır. Satış bedeli ile maliyet arasındaki **20.000 ₺** fark 645 hesaba alacak kaydedilir.",
        "1 Sıra No'lu MSUGT - 102/110/119/644/645/653; 2024-2026 SGS menkul kıymet satışı soru örüntüsü",
    ),
    "finmuh-gt-gen-0047": income_statement_patch(
        "İşletme, 400.000 ₺ tutarında ve yıllık %18 faizli banka kredisini beş ay kullanmıştır. Faiz basit faiz yöntemiyle hesaplanacak ve tamamı kısa vadeli borçlanma gideri olarak gelir tablosuna yansıtılacaktır.\n\n660 Kısa Vadeli Borçlanma Giderleri hesabına aktarılacak tutar kaç ₺'dir?",
        {
            "A": "24.000",
            "B": "27.000",
            "C": "30.000",
            "D": "36.000",
            "E": "72.000",
        },
        "C",
        "Basit faiz = anapara × yıllık oran × süredir. 400.000 × %18 × 5/12 = **30.000 ₺** faiz gideri hesaplanır ve kısa vadeli borçlanmaya ait olduğu için 660 hesaba aktarılır.",
        "1 Sıra No'lu MSUGT - 660 Kısa Vadeli Borçlanma Giderleri",
    ),
    "finmuh-gt-gen-0051": income_statement_patch(
        "İşletmenin 1 Ekim'de bankaya yatırdığı 300.000 ₺, yıllık %20 faizli vadeli mevduatın faizi vade sonunda tahsil edilecektir. 31 Aralık'ta üç aylık faiz tahakkuku yapılacaktır.\n\nYapılacak kayıt hangisidir?",
        {
            "A": "102 Bankalar 15.000 ₺ borç / 642 Faiz Gelirleri 15.000 ₺ alacak",
            "B": "181 Gelir Tahakkukları 60.000 ₺ borç / 642 Faiz Gelirleri 60.000 ₺ alacak",
            "C": "642 Faiz Gelirleri 15.000 ₺ borç / 181 Gelir Tahakkukları 15.000 ₺ alacak",
            "D": "181 Gelir Tahakkukları 15.000 ₺ borç / 671 Önceki Dönem Gelir ve Kârlar 15.000 ₺ alacak",
            "E": "181 Gelir Tahakkukları 15.000 ₺ borç / 642 Faiz Gelirleri 15.000 ₺ alacak",
        },
        "E",
        "Üç aylık faiz 300.000 × %20 × 3/12 = **15.000 ₺**'dir. Faiz cari dönemde kazanılmış ancak henüz tahsil edilmemiştir; bu nedenle 181 borçlandırılır, 642 alacaklandırılır.",
        "1 Sıra No'lu MSUGT - 181/642; dönemsellik kavramı",
    ),
    "finmuh-gt-gen-0052": income_statement_patch(
        "Dönem sonu gelir ve gider aktarmaları tamamlandığında 690 Dönem Kârı veya Zararı hesabı 300.000 ₺ alacak kalanı vermiştir. Hesaplanan dönem kârı vergi ve diğer yasal yükümlülük karşılığı 75.000 ₺'dir.\n\nKarşılık kaydından ve 690 ile 691 hesaplarının devrinden sonra 692 hesabın durumu hangisidir?",
        {
            "A": "225.000 ₺ alacak kalanı verir.",
            "B": "225.000 ₺ borç kalanı verir.",
            "C": "300.000 ₺ alacak kalanı verir.",
            "D": "75.000 ₺ borç kalanı verir.",
            "E": "375.000 ₺ alacak kalanı verir.",
        },
        "A",
        "Vergi karşılığı 691 borç / 370 alacak kaydedilir. 690'daki 300.000 ₺ vergi öncesi kâr ile 691'deki 75.000 ₺ karşılık 692 hesaba devredildiğinde net kâr 300.000 − 75.000 = **225.000 ₺** olur ve 692 hesap alacak kalanı verir.",
        "1 Sıra No'lu MSUGT - 370/690/691/692",
    ),
    "finmuh-gt-gen-0053": income_statement_patch(
        "Bir işletmenin ortalama stokları 50.000 ₺ ve stok devir hızı 2,4'tür. Brüt satış kârı oranı %40, faaliyet giderleri toplamı 95.000 ₺'dir.\n\nİşletmenin faaliyet sonucu aşağıdakilerden hangisidir?",
        {
            "A": "5.000 ₺ kâr",
            "B": "15.000 ₺ kâr",
            "C": "15.000 ₺ zarar",
            "D": "25.000 ₺ zarar",
            "E": "80.000 ₺ zarar",
        },
        "C",
        "Satışların maliyeti 50.000 × 2,4 = 120.000 ₺'dir. Maliyet, net satışların %60'ı olduğundan net satışlar 200.000 ₺ ve brüt kâr 80.000 ₺'dir. Faaliyet sonucu 80.000 − 95.000 = **15.000 ₺ zarar**dır.",
        "1 Sıra No'lu MSUGT - Faaliyet sonucu; 2025 SGS stok devir hızı soru örüntüsü",
    ),
    "finmuh-gt-gen-0054": income_statement_patch(
        "İşletme, defter değeri 600.000 ₺ olan kısa vadeli yabancı para kredisini 630.000 ₺ karşılığında kapatmış ve ayrıca 25.000 ₺ faiz ödemiştir. Faizin tamamı cari döneme aittir.\n\nGelir tablosuna yansıtılacak tutarlar hangi seçenekte doğru verilmiştir?",
        {
            "A": "646 Kambiyo Kârları 30.000 ₺; 642 Faiz Gelirleri 25.000 ₺",
            "B": "656 Kambiyo Zararları 30.000 ₺; 660 Kısa Vadeli Borçlanma Giderleri 25.000 ₺",
            "C": "660 Kısa Vadeli Borçlanma Giderleri 55.000 ₺; kambiyo sonucu oluşmaz",
            "D": "656 Kambiyo Zararları 55.000 ₺; finansman gideri oluşmaz",
            "E": "681 Önceki Dönem Gider ve Zararları 30.000 ₺; 661 Uzun Vadeli Borçlanma Giderleri 25.000 ₺",
        },
        "B",
        "Kredinin TL karşılığındaki 630.000 − 600.000 = **30.000 ₺** artış kambiyo zararıdır ve 656 hesapta izlenir. Ayrıca ödenen **25.000 ₺ faiz**, kısa vadeli borçlanmaya ait finansman gideridir ve gelir tablosunda 660 hesaba yansıtılır.",
        "1 Sıra No'lu MSUGT - 656/660",
    ),
    "finmuh-gt-gen-0056": income_statement_patch(
        "Bir işletmenin dönem içinde sattığı mamullerin maliyeti 120.000 ₺, ticari malların maliyeti 180.000 ₺ ve sunduğu hizmetlerin maliyeti 40.000 ₺'dir.\n\nGelir tablosunda 'Satışların Maliyeti' grubunda raporlanacak toplam tutar kaç ₺'dir?",
        {
            "A": "120.000",
            "B": "180.000",
            "C": "220.000",
            "D": "300.000",
            "E": "340.000",
        },
        "E",
        "620 Satılan Mamuller Maliyeti, 621 Satılan Ticari Mallar Maliyeti ve 622 Satılan Hizmet Maliyeti, 62 Satışların Maliyeti grubunda birlikte raporlanır. Toplam 120.000 + 180.000 + 40.000 = **340.000 ₺**'dir.",
        "1 Sıra No'lu MSUGT - 620/621/622",
    ),
    "finmuh-gt-gen-0057": income_statement_patch(
        "Bir işletmenin gelir tablosu verileri aşağıdaki gibidir:\n\n2025: Net satışlar 400.000 ₺, brüt satış kârı 120.000 ₺, faaliyet giderleri 80.000 ₺.\n2026: Net satışlar 500.000 ₺, brüt satış kârı 150.000 ₺, faaliyet giderleri 105.000 ₺.\n\nBu verilere göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Brüt kâr marjı 2026'da %5 azalmıştır.",
            "B": "Faaliyet kârı tutarı 2026'da azalmıştır.",
            "C": "Faaliyet giderlerinin net satışlara oranı iki yılda da aynıdır.",
            "D": "Brüt kâr marjı sabit kalırken faaliyet kâr marjı düşmüştür.",
            "E": "2026'da faaliyet kârı oluşmamıştır.",
        },
        "D",
        "Brüt kâr marjı her iki yılda da %30'dur. Faaliyet kârı 2025'te 40.000 ₺ ve marjı %10; 2026'da 45.000 ₺ ve marjı %9'dur. Dolayısıyla brüt marj sabit kalmış, faaliyet kârı tutarı artsa da **faaliyet kâr marjı düşmüştür**.",
        "1 Sıra No'lu MSUGT - Gelir tablosu kârlılık basamakları; 2025 SGS yatay analiz soru örüntüsü",
    ),
    "finmuh-gt-gen-0058": income_statement_patch(
        "Bir işletmenin brüt satışları 700.000 ₺, satıştan iadeleri 30.000 ₺, satış iskontoları 20.000 ₺ ve satışların maliyeti 390.000 ₺'dir. Faaliyet giderleri 120.000 ₺, faiz gelirleri 20.000 ₺, kambiyo kârları 10.000 ₺, reeskont faiz giderleri 5.000 ₺ ve finansman giderleri 35.000 ₺'dir.\n\nİşletmenin olağan kârı kaç ₺'dir?",
        {
            "A": "130.000",
            "B": "125.000",
            "C": "140.000",
            "D": "160.000",
            "E": "260.000",
        },
        "A",
        "Net satışlar 700.000 − 30.000 − 20.000 = 650.000 ₺; brüt kâr 650.000 − 390.000 = 260.000 ₺ ve faaliyet kârı 260.000 − 120.000 = 140.000 ₺'dir. Olağan kâr 140.000 + 20.000 + 10.000 − 5.000 − 35.000 = **130.000 ₺** olur.",
        "1 Sıra No'lu MSUGT - 60/61/62/63/64/65/66 hesap grupları",
    ),
    "finmuh-gt-gen-0059": income_statement_patch(
        "Esas faaliyet konusu makine üretip satmak olan işletme, ürettiği bir makineyi 250.000 ₺ + %20 KDV ile kredili satmıştır. Makinenin maliyeti 170.000 ₺'dir.\n\nSatış hasılatının kaydında kullanılacak gelir hesabı hangisidir?",
        {
            "A": "645 Menkul Kıymet Satış Kârları",
            "B": "649 Diğer Olağan Gelir ve Kârlar",
            "C": "600 Yurt İçi Satışlar",
            "D": "671 Önceki Dönem Gelir ve Kârlar",
            "E": "679 Diğer Olağandışı Gelir ve Kârlar",
        },
        "C",
        "Makine işletmenin kullanılan duran varlığı değil, **esas faaliyet kapsamında üretilip satılan mamulüdür**. Bu nedenle KDV hariç 250.000 ₺ satış hasılatı 600 Yurt İçi Satışlar hesabına alacak kaydedilir; 679 kullanılmaz.",
        "1 Sıra No'lu MSUGT - 120/391/600; hasılat ile duran varlık satış kârı ayrımı",
    ),
    "finmuh-gt-gen-0060": income_statement_patch(
        "Gelir tablosu ve dönem sonu hesaplarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Net satışlar, brüt satışlardan satış indirimlerinin düşülmesiyle bulunur.\n\nII. 621 Satılan Ticari Mallar Maliyeti faaliyet gideri değil, satışların maliyeti grubundadır.\n\nIII. 690 hesabın alacak kalanı vergi öncesi kârı gösterir; 691 hesabın borç kalanı net kâra ulaşılırken bu tutarı azaltır.\n\nIV. 692 hesabın borç kalanı 591 Dönem Net Zararı hesabına devredilir.",
        {
            "A": "I ve II",
            "B": "I, II, III ve IV",
            "C": "II ve III",
            "D": "I, III ve IV",
            "E": "Yalnız IV",
        },
        "B",
        "Dört ifade de doğrudur. 61 grubu brüt satışlardan düşülür; 621 hesabı 62 grubundadır. 690'ın alacak kalanı vergi öncesi kârı, 691'in borç kalanı vergi karşılığını gösterir. 692 borç kalanı verdiğinde net zarar 591 hesaba devredilir.",
        "1 Sıra No'lu MSUGT - 61/62/690/691/692/591",
    ),
}


COST_ACCOUNTS_PATCHES = {
    "finmuh-mlh-gen-0008": cost_accounts_patch(
        "Bir üretim işletmesinde döneme ait giderler şöyledir: endirekt malzeme 55.000 ₺, endirekt işçilik 90.000 ₺, fabrika binası kirası 70.000 ₺, üretim makinelerinin amortismanı 45.000 ₺ ve genel müdürlük personeli ücreti 60.000 ₺.\n\n730 Genel Üretim Giderleri hesabında toplanacak tutar kaç ₺'dir?",
        {
            "A": "200.000",
            "B": "215.000",
            "C": "260.000",
            "D": "275.000",
            "E": "320.000",
        },
        "C",
        "Endirekt malzeme, endirekt işçilik, fabrika kirası ve üretim makinelerinin amortismanı genel üretim gideridir: 55.000 + 90.000 + 70.000 + 45.000 = **260.000 ₺**. Genel müdürlük personeli ücreti 770 Genel Yönetim Giderlerinde izlenir.",
        "1 Sıra No'lu MSUGT - 730 Genel Üretim Giderleri; 18 Nisan 2026 SGS gider sınıflandırma soru örüntüsü",
    ),
    "finmuh-mlh-gen-0014": cost_accounts_patch(
        "Normal maliyet yöntemini kullanan işletmede direkt ilk madde ve malzeme giderleri 360.000 ₺, direkt işçilik giderleri 240.000 ₺, değişken genel üretim giderleri 180.000 ₺ ve sabit genel üretim giderleri 300.000 ₺'dir. Normal kapasite 10.000 birim, fiilî üretim 8.000 birimdir.\n\nStok maliyetine yüklenecek toplam üretim maliyeti kaç ₺'dir?",
        {
            "A": "1.020.000",
            "B": "960.000",
            "C": "1.080.000",
            "D": "840.000",
            "E": "780.000",
        },
        "A",
        "Direkt giderler ile değişken GÜG'nin tamamı maliyete girer. Sabit GÜG'nin yüklenecek kısmı 300.000 × 8.000/10.000 = 240.000 ₺'dir. Toplam maliyet 360.000 + 240.000 + 180.000 + 240.000 = **1.020.000 ₺**; dağıtılmayan 60.000 ₺ dönem gideridir.",
        "TMS 2 Stoklar, par. 12-13; normal kapasiteye göre sabit genel üretim gideri",
    ),
    "finmuh-mlh-gen-0021": cost_accounts_patch(
        "7/A seçeneğini kullanan bir üretim işletmesi, ambardan üretime 200.000 ₺ direkt hammadde ve 30.000 ₺ işletme malzemesi vermiştir. İşletme malzemesi endirekt niteliktedir.\n\nMalzemelerin üretime verilmesine ilişkin kayıt hangisidir?",
        {
            "A": "710 Direkt İlk Madde ve Malzeme Giderleri 230.000 ₺ borç / 150 İlk Madde ve Malzeme 230.000 ₺ alacak",
            "B": "151 Yarı Mamuller - Üretim 230.000 ₺ borç / 150 İlk Madde ve Malzeme 230.000 ₺ alacak",
            "C": "710 Direkt İlk Madde ve Malzeme Giderleri 200.000 ₺ ve 770 Genel Yönetim Giderleri 30.000 ₺ borç / 150 İlk Madde ve Malzeme 230.000 ₺ alacak",
            "D": "150 İlk Madde ve Malzeme 230.000 ₺ borç / 710 Direkt İlk Madde ve Malzeme Giderleri 200.000 ₺ ve 730 Genel Üretim Giderleri 30.000 ₺ alacak",
            "E": "710 Direkt İlk Madde ve Malzeme Giderleri 200.000 ₺ ve 730 Genel Üretim Giderleri 30.000 ₺ borç / 150 İlk Madde ve Malzeme 230.000 ₺ alacak",
        },
        "E",
        "Mamule doğrudan izlenebilen 200.000 ₺ hammadde **710** hesaba, endirekt nitelikteki 30.000 ₺ işletme malzemesi **730** hesaba borç kaydedilir. Stoktan toplam 230.000 ₺ çıktığı için 150 hesap alacaklandırılır.",
        "1 Sıra No'lu MSUGT - 150/710/730; 18 Temmuz 2026 SGS 7/A malzeme kullanımı soru örüntüsü",
    ),
    "finmuh-mlh-gen-0022": cost_accounts_patch(
        "Dönemde tahakkuk eden brüt ücretlerin 250.000 ₺'si mamul üzerinde doğrudan çalışan işçilere, 50.000 ₺'si fabrika ustabaşılarına, 40.000 ₺'si satış personeline ve 30.000 ₺'si genel yönetim personeline aittir. İşletme 7/A seçeneğini kullanmaktadır.\n\nÜcret tahakkukunda borçlandırılacak hesaplar hangisidir?",
        {
            "A": "720 hesabı 300.000 ₺; 760 hesabı 40.000 ₺; 770 hesabı 30.000 ₺",
            "B": "720 hesabı 250.000 ₺; 730 hesabı 50.000 ₺; 760 hesabı 40.000 ₺; 770 hesabı 30.000 ₺",
            "C": "720 hesabı 250.000 ₺; 730 hesabı 120.000 ₺",
            "D": "730 hesabı 300.000 ₺; 760 hesabı 40.000 ₺; 770 hesabı 30.000 ₺",
            "E": "791 hesabı 370.000 ₺",
        },
        "B",
        "Doğrudan üretim işçiliği **720**, ustabaşı gibi endirekt üretim işçiliği **730**, satış personeli **760** ve genel yönetim personeli **770** hesapta izlenir. 791 hesabı 7/B seçeneğine aittir.",
        "1 Sıra No'lu MSUGT - 720/730/760/770",
    ),
    "finmuh-mlh-gen-0023": cost_accounts_patch(
        "7/A seçeneğini kullanan işletmede dönemin üretim giderleri 710 hesapta 150.000 ₺, 720 hesapta 100.000 ₺ ve 730 hesapta 80.000 ₺ olarak birikmiştir. Giderlerin tamamı yarı mamul maliyetine yansıtılacaktır.\n\n151 Yarı Mamuller - Üretim hesabının borçlandırıldığı yansıtma kaydında hangi hesaplar alacaklandırılır?",
        {
            "A": "710 hesabı 150.000 ₺, 720 hesabı 100.000 ₺ ve 730 hesabı 80.000 ₺",
            "B": "150 hesabı 150.000 ₺, 335 hesabı 100.000 ₺ ve 381 hesabı 80.000 ₺",
            "C": "711 hesabı 330.000 ₺; 721 ve 731 hesapları kullanılmaz",
            "D": "711 hesabı 150.000 ₺, 721 hesabı 100.000 ₺ ve 731 hesabı 80.000 ₺",
            "E": "620 hesabı 150.000 ₺, 621 hesabı 100.000 ₺ ve 622 hesabı 80.000 ₺",
        },
        "D",
        "7/A'da giderler önce fonksiyon hesaplarında toplanır, üretim maliyetine ise ilgili **yansıtma hesapları** aracılığıyla aktarılır. Bu nedenle 151 hesap 330.000 ₺ borçlandırılır; 711, 721 ve 731 hesapları sırasıyla 150.000, 100.000 ve 80.000 ₺ alacaklandırılır.",
        "1 Sıra No'lu MSUGT - 151/711/721/731",
    ),
    "finmuh-mlh-gen-0027": cost_accounts_patch(
        "Bir üretim işletmesinde dönem başı ilk madde ve malzeme stoku 50.000 ₺, dönem içi alışlar 300.000 ₺ ve dönem sonu stok 40.000 ₺'dir. Kullanılan malzemenin 20.000 ₺'si endirekt olup 140.000 ₺ tutarındaki genel üretim giderine dâhildir. Direkt işçilik 180.000 ₺; dönem başı ve sonu yarı mamul stokları sırasıyla 60.000 ve 90.000 ₺; dönem başı ve sonu mamul stokları ise 70.000 ve 50.000 ₺'dir.\n\nTamamlanan mamul maliyeti ile satılan mamuller maliyeti sırasıyla kaç ₺'dir?",
        {
            "A": "560.000 ve 580.000",
            "B": "580.000 ve 560.000",
            "C": "580.000 ve 600.000",
            "D": "600.000 ve 580.000",
            "E": "610.000 ve 630.000",
        },
        "C",
        "Kullanılan toplam malzeme 50.000 + 300.000 − 40.000 = 310.000 ₺; direkt kısmı 290.000 ₺'dir. Üretim giderleri 290.000 + 180.000 + 140.000 = 610.000 ₺; tamamlanan mamul maliyeti 60.000 + 610.000 − 90.000 = **580.000 ₺**'dir. Satılan mamuller maliyeti 70.000 + 580.000 − 50.000 = **600.000 ₺** olur.",
        "1 Sıra No'lu MSUGT - Satışların Maliyeti Tablosu; 2025-2026 SGS tablo akışı soru örüntüsü",
    ),
    "finmuh-mlh-gen-0031": cost_accounts_patch(
        "Standart maliyet yöntemini uygulayan işletmede 711 Direkt İlk Madde ve Malzeme Giderleri Yansıtma Hesabı 500.000 ₺'dir. Dönemde 20.000 ₺ olumlu fiyat farkı ve 35.000 ₺ olumsuz miktar farkı oluşmuştur.\n\n710 Direkt İlk Madde ve Malzeme Giderleri hesabının fiilî tutarı kaç ₺'dir?",
        {
            "A": "515.000",
            "B": "485.000",
            "C": "500.000",
            "D": "535.000",
            "E": "555.000",
        },
        "A",
        "Fiilî maliyet = standart maliyet − olumlu fark + olumsuz fark olarak bulunur. 500.000 − 20.000 + 35.000 = **515.000 ₺**'dir. Olumlu fiyat farkı maliyeti azaltırken olumsuz miktar farkı artırır.",
        "1 Sıra No'lu MSUGT - 710/711/712/713; 2024-2026 SGS standart maliyet kapanışı soru örüntüsü",
    ),
    "finmuh-mlh-gen-0032": cost_accounts_patch(
        "Bir üretim işletmesinde fabrika müdürü ücreti 70.000 ₺, bakım işçiliği 30.000 ₺, üretim makinelerinin amortismanı 40.000 ₺, fabrika elektrik gideri 25.000 ₺ ve pazarlama bölümü kirası 35.000 ₺'dir.\n\nGenel üretim giderleri toplamı kaç ₺'dir?",
        {
            "A": "130.000",
            "B": "140.000",
            "C": "150.000",
            "D": "165.000",
            "E": "200.000",
        },
        "D",
        "Fabrika müdürü, bakım işçiliği, üretim makinesi amortismanı ve fabrika elektriği GÜG'dür: 70.000 + 30.000 + 40.000 + 25.000 = **165.000 ₺**. Pazarlama bölümü kirası 760 hesapta dönem gideridir.",
        "1 Sıra No'lu MSUGT - 730/760",
    ),
    "finmuh-mlh-gen-0034": cost_accounts_patch(
        "7/B seçeneğinde gider çeşidi hesaplarında biriken giderlerin 300.000 ₺'lık kısmı üretim faaliyetine aittir. Bu tutar üretim maliyetine yansıtılacaktır.\n\nYansıtma kaydında kullanılacak hesaplar hangisidir?",
        {
            "A": "151 Yarı Mamuller - Üretim borç / 790 İlk Madde ve Malzeme Giderleri alacak",
            "B": "798 Gider Çeşitleri Yansıtma borç / 799 Üretim Maliyet Hesabı alacak",
            "C": "710 Direkt İlk Madde ve Malzeme Giderleri borç / 711 Direkt İlk Madde ve Malzeme Giderleri Yansıtma alacak",
            "D": "799 Üretim Maliyet Hesabı borç / 790 İlk Madde ve Malzeme Giderleri alacak",
            "E": "799 Üretim Maliyet Hesabı borç / 798 Gider Çeşitleri Yansıtma Hesabı alacak",
        },
        "E",
        "7/B'de giderler 790-797 gider çeşidi hesaplarında izlenir. Üretimle ilgili kısım **799 Üretim Maliyet Hesabına borç**, gider çeşitlerinin yansıtılması ise **798 hesaba alacak** kaydedilir.",
        "1 Sıra No'lu MSUGT - 7/B seçeneği, 798/799",
    ),
    "finmuh-mlh-gen-0035": cost_accounts_patch(
        "Normal kapasitesi 20.000 birim olan işletmenin sabit genel üretim giderleri 400.000 ₺'dir. Dönemde olağan nedenlerle 15.000 birim üretilmiştir.\n\nTMS 2'ye göre sabit genel üretim giderinin stok maliyetine yüklenecek ve dönem gideri yazılacak kısımları sırasıyla kaç ₺'dir?",
        {
            "A": "400.000 ve 0",
            "B": "300.000 ve 100.000",
            "C": "300.000 ve 75.000",
            "D": "200.000 ve 200.000",
            "E": "100.000 ve 300.000",
        },
        "B",
        "Normal kapasiteye göre sabit GÜG oranı 400.000 / 20.000 = 20 ₺/birimdir. 15.000 birime **300.000 ₺** yüklenebilir; kalan **100.000 ₺** düşük kapasite nedeniyle stok maliyetine eklenmez ve oluştuğu dönemde giderleştirilir.",
        "TMS 2 Stoklar, par. 13 - normal kapasite ve dağıtılmayan sabit genel üretim gideri",
    ),
    "finmuh-mlh-gen-0038": cost_accounts_patch(
        "7/B seçeneğinde 790-797 gider çeşidi hesaplarında toplam 800.000 ₺ gider birikmiştir. Yapılan gider yeri dağıtımında bu tutarın 600.000 ₺'sinin üretime, 120.000 ₺'sinin pazarlamaya ve 80.000 ₺'sinin genel yönetime ait olduğu belirlenmiştir.\n\nYansıtma kaydında 799 Üretim Maliyet Hesabına borç kaydedilecek tutar kaç ₺'dir?",
        {
            "A": "80.000",
            "B": "120.000",
            "C": "600.000",
            "D": "680.000",
            "E": "800.000",
        },
        "C",
        "799 hesap yalnız **üretim fonksiyonuna ait 600.000 ₺** için borçlandırılır. Pazarlama ve genel yönetim payları ilgili gelir tablosu fonksiyon hesaplarına aktarılır; gider çeşitlerinin toplamı ise 798 hesap aracılığıyla yansıtılır.",
        "1 Sıra No'lu MSUGT - 7/B gider çeşitlerinin fonksiyonlara dağıtımı",
    ),
    "finmuh-mlh-gen-0040": cost_accounts_patch(
        "Standart maliyet yöntemini uygulayan işletmede 721 Direkt İşçilik Giderleri Yansıtma Hesabı 600.000 ₺'dir. Dönemde 25.000 ₺ olumlu ücret farkı ve 40.000 ₺ olumsuz süre farkı oluşmuştur.\n\n720 Direkt İşçilik Giderleri hesabının fiilî tutarı kaç ₺'dir?",
        {
            "A": "615.000",
            "B": "575.000",
            "C": "600.000",
            "D": "640.000",
            "E": "665.000",
        },
        "A",
        "Fiilî direkt işçilik maliyeti = standart maliyet − olumlu ücret farkı + olumsuz süre farkıdır. 600.000 − 25.000 + 40.000 = **615.000 ₺** bulunur.",
        "1 Sıra No'lu MSUGT - 720/721/722/723; 2024-2026 SGS standart işçilik farkları soru örüntüsü",
    ),
    "finmuh-mlh-gen-0041": cost_accounts_patch(
        "Normal maliyet yöntemini kullanan bir işletmenin direkt ilk madde ve malzeme giderleri 500.000 ₺, direkt işçilik giderleri 300.000 ₺ ve sabit genel üretim giderleri 200.000 ₺'dir. Normal kapasite 10.000 birim, fiilî üretim 8.000 birimdir. Dönem başı ve sonu yarı mamulü bulunmayan işletmenin normal maliyete göre toplam üretim maliyeti 1.140.000 ₺'dir.\n\nDeğişken genel üretim giderleri kaç ₺'dir?",
        {
            "A": "100.000",
            "B": "140.000",
            "C": "160.000",
            "D": "200.000",
            "E": "180.000",
        },
        "E",
        "Maliyete yüklenen sabit GÜG 200.000 × 8.000/10.000 = 160.000 ₺'dir. Değişken GÜG = 1.140.000 − 500.000 − 300.000 − 160.000 = **180.000 ₺** bulunur.",
        "TMS 2 Stoklar, par. 12-13; 2025-2026 SGS normal maliyet ters hesaplama soru örüntüsü",
    ),
    "finmuh-mlh-gen-0042": cost_accounts_patch(
        "Bir üretim işletmesinin dönem başı yarı mamul maliyeti 80.000 ₺, dönemin üretim giderleri 520.000 ₺ ve dönem sonu yarı mamul maliyeti 100.000 ₺'dir. Dönemde 2.000 birim mamul tamamlanmıştır.\n\nTamamlanan mamullerin birim maliyeti kaç ₺'dir?",
        {
            "A": "200",
            "B": "220",
            "C": "240",
            "D": "250",
            "E": "300",
        },
        "D",
        "Tamamlanan mamul maliyeti = 80.000 + 520.000 − 100.000 = **500.000 ₺**'dir. 2.000 birim tamamlandığına göre birim maliyet 500.000 / 2.000 = **250 ₺** olur.",
        "1 Sıra No'lu MSUGT - 151/152 ve Satışların Maliyeti Tablosu",
    ),
    "finmuh-mlh-gen-0043": cost_accounts_patch(
        "Üretime verilen 300.000 ₺ tutarındaki ilk madde ve malzemenin %75'i mamule doğrudan yüklenebilmekte, kalanı endirekt nitelik taşımaktadır. İşletme 7/A seçeneğini kullanmaktadır.\n\nKayıtta 710 ve 730 hesaplarına borç yazılacak tutarlar sırasıyla kaç ₺'dir?",
        {
            "A": "300.000 ve 0",
            "B": "225.000 ve 75.000",
            "C": "75.000 ve 225.000",
            "D": "240.000 ve 60.000",
            "E": "150.000 ve 150.000",
        },
        "B",
        "Direkt kısım 300.000 × %75 = **225.000 ₺** olup 710 hesaba; kalan **75.000 ₺** endirekt malzeme ise 730 hesaba borç kaydedilir. Toplam 300.000 ₺ için 150 hesap alacaklandırılır.",
        "1 Sıra No'lu MSUGT - 150/710/730; 18 Temmuz 2026 SGS direkt-endirekt ayrımı soru örüntüsü",
    ),
    "finmuh-mlh-gen-0044": cost_accounts_patch(
        "Fabrika personeline ait 350.000 ₺ brüt ücretin %80'i mamullere doğrudan izlenebilmekte, %20'si bakım ve ustabaşı işçiliğinden oluşmaktadır.\n\n7/A seçeneğinde 720 Direkt İşçilik Giderleri ile 730 Genel Üretim Giderleri hesaplarına borç yazılacak tutarlar sırasıyla kaç ₺'dir?",
        {
            "A": "350.000 ve 0",
            "B": "210.000 ve 140.000",
            "C": "280.000 ve 70.000",
            "D": "70.000 ve 280.000",
            "E": "300.000 ve 50.000",
        },
        "C",
        "Doğrudan izlenebilen işçilik 350.000 × %80 = **280.000 ₺** olup 720 hesaba yazılır. Bakım ve ustabaşı işçiliği endirekttir; 350.000 × %20 = **70.000 ₺** 730 hesaba kaydedilir.",
        "1 Sıra No'lu MSUGT - 720/730",
    ),
    "finmuh-mlh-gen-0047": cost_accounts_patch(
        "Bir üretim işletmesinde direkt ilk madde ve malzeme giderleri 240.000 ₺, direkt işçilik giderleri 150.000 ₺ ve genel üretim giderleri 110.000 ₺'dir.\n\nDirekt (temel) maliyet ile şekillendirme (dönüştürme) maliyeti sırasıyla kaç ₺'dir?",
        {
            "A": "390.000 ve 260.000",
            "B": "240.000 ve 500.000",
            "C": "350.000 ve 390.000",
            "D": "390.000 ve 500.000",
            "E": "500.000 ve 260.000",
        },
        "A",
        "Direkt maliyet = direkt ilk madde ve malzeme + direkt işçilik = 240.000 + 150.000 = **390.000 ₺**'dir. Şekillendirme maliyeti = direkt işçilik + genel üretim giderleri = 150.000 + 110.000 = **260.000 ₺** olur.",
        "Maliyet muhasebesi - direkt maliyet ve şekillendirme maliyeti",
    ),
    "finmuh-mlh-gen-0048": cost_accounts_patch(
        "Bir üretim işletmesi dönem için 600.000 ₺ genel üretim gideri ve 30.000 makine saati öngörmüştür. GÜG mamullere makine saatine göre yüklenecektir. K45 siparişi 350 makine saati kullanmıştır.\n\nK45 siparişine yüklenecek genel üretim gideri kaç ₺'dir?",
        {
            "A": "3.500",
            "B": "5.250",
            "C": "6.000",
            "D": "6.500",
            "E": "7.000",
        },
        "E",
        "Tahminî GÜG yükleme oranı 600.000 / 30.000 = **20 ₺/makine saati**dir. K45 siparişine 350 × 20 = **7.000 ₺** genel üretim gideri yüklenir.",
        "Maliyet muhasebesi - tahminî genel üretim gideri yükleme oranı; 2024-2026 SGS soru örüntüsü",
    ),
    "finmuh-mlh-gen-0049": cost_accounts_patch(
        "Standart maliyet yöntemini kullanan işletmede dönem sonunda 50.000 ₺ olumsuz toplam maliyet farkı oluşmuştur. Fark dağıtılmadan önce standart maliyetle 151 Yarı Mamuller - Üretim 100.000 ₺, 152 Mamuller 150.000 ₺ ve 620 Satılan Mamuller Maliyeti 250.000 ₺ borç bakiyesi vermektedir. Fark bu hesaplara bakiyeleri oranında dağıtılacaktır.\n\nDağıtımda 620 hesaba borç yazılacak tutar kaç ₺'dir?",
        {
            "A": "10.000",
            "B": "12.500",
            "C": "15.000",
            "D": "25.000",
            "E": "35.000",
        },
        "D",
        "Toplam standart maliyet bakiyesi 100.000 + 150.000 + 250.000 = 500.000 ₺'dir. 620 hesabın payı %50 olduğundan olumsuz farkın 50.000 × %50 = **25.000 ₺** kısmı 620 hesaba borç yazılır.",
        "1 Sıra No'lu MSUGT - standart maliyet farklarının 151/152/620 hesaplarına dağıtımı; 18 Temmuz 2026 SGS soru örüntüsü",
    ),
    "finmuh-mlh-gen-0050": cost_accounts_patch(
        "Normal kapasitesi 10.000 birim olan işletmede sabit genel üretim gideri 250.000 ₺'dir. Dönemde 7.000 birim üretilmiştir.\n\nTam maliyet yöntemiyle normal maliyet yöntemine göre hesaplanan toplam üretim maliyetleri arasındaki fark kaç ₺'dir?",
        {
            "A": "50.000",
            "B": "75.000",
            "C": "100.000",
            "D": "175.000",
            "E": "250.000",
        },
        "B",
        "Tam maliyet sabit GÜG'nin tamamı olan 250.000 ₺'yı ürüne yükler. Normal maliyette yüklenen sabit GÜG 250.000 × 7.000/10.000 = 175.000 ₺'dir. Aradaki **75.000 ₺** dağıtılmayan sabit giderdir.",
        "TMS 2 Stoklar, par. 13; 26 Ekim 2024 SGS tam-normal maliyet farkı soru örüntüsü",
    ),
    "finmuh-mlh-gen-0051": cost_accounts_patch(
        "Normal maliyet yöntemini kullanan işletme dönemde 25.000 birim üretmiştir. Direkt ilk madde ve malzeme giderleri 400.000 ₺, direkt işçilik giderleri 250.000 ₺, değişken genel üretim giderleri 150.000 ₺ ve sabit genel üretim giderleri 300.000 ₺'dir. Dönemin kapasite kullanım oranı %80'dir.\n\nNormal maliyete göre birim üretim maliyeti kaç ₺'dir?",
        {
            "A": "32,00",
            "B": "38,40",
            "C": "41,60",
            "D": "44,00",
            "E": "46,40",
        },
        "C",
        "Sabit GÜG'nin maliyete yüklenecek kısmı 300.000 × %80 = 240.000 ₺'dir. Toplam normal maliyet 400.000 + 250.000 + 150.000 + 240.000 = 1.040.000 ₺; birim maliyet 1.040.000 / 25.000 = **41,60 ₺**'dir.",
        "TMS 2 Stoklar, par. 12-13; 18 Temmuz 2026 SGS normal maliyet ve kapasite soru örüntüsü",
    ),
    "finmuh-mlh-gen-0052": cost_accounts_patch(
        "Bir üretim işletmesinin dönemin üretim giderleri 780.000 ₺, dönem başı ve sonu yarı mamul stokları sırasıyla 90.000 ve 70.000 ₺, dönem başı ve sonu mamul stokları ise sırasıyla 60.000 ve 110.000 ₺'dir.\n\nTamamlanan mamul maliyeti ile satılan mamuller maliyeti sırasıyla kaç ₺'dir?",
        {
            "A": "800.000 ve 750.000",
            "B": "760.000 ve 810.000",
            "C": "780.000 ve 730.000",
            "D": "800.000 ve 850.000",
            "E": "820.000 ve 770.000",
        },
        "A",
        "Tamamlanan mamul maliyeti = 90.000 + 780.000 − 70.000 = **800.000 ₺**'dir. Satılan mamuller maliyeti = 60.000 + 800.000 − 110.000 = **750.000 ₺** olur.",
        "1 Sıra No'lu MSUGT - Satışların Maliyeti Tablosu; 18 Nisan 2026 SGS iki dönemli tablo soru örüntüsü",
    ),
    "finmuh-mlh-gen-0053": cost_accounts_patch(
        "Standart maliyet yöntemini kullanan işletmede 710 Direkt İlk Madde ve Malzeme Giderleri 520.000 ₺, 711 Direkt İlk Madde ve Malzeme Giderleri Yansıtma 500.000 ₺'dir. Ayrıca 15.000 ₺ olumlu fiyat farkı ve 35.000 ₺ olumsuz miktar farkı bulunmaktadır.\n\nDönem sonu kapanış kaydı hangisidir?",
        {
            "A": "710 hesabı 520.000 ₺ borç; 711 hesabı 500.000 ₺ ve 712 hesabı 20.000 ₺ alacak",
            "B": "711 hesabı 500.000 ₺ ve 712 hesabı 15.000 ₺ borç; 710 hesabı 480.000 ₺ ve 713 hesabı 35.000 ₺ alacak",
            "C": "711 hesabı 500.000 ₺ ve 712 hesabı 15.000 ₺ borç; 710 hesabı 520.000 ₺ alacak; 713 hesabı kullanılmaz",
            "D": "710 hesabı 520.000 ₺ ve 713 hesabı 35.000 ₺ borç; 711 hesabı 500.000 ₺ ve 712 hesabı 55.000 ₺ alacak",
            "E": "711 hesabı 500.000 ₺ ve 713 hesabı 35.000 ₺ borç; 710 hesabı 520.000 ₺ ve 712 hesabı 15.000 ₺ alacak",
        },
        "E",
        "Kapanışta yansıtma hesabı 711 **500.000 ₺ borç**, olumsuz miktar farkı 713 **35.000 ₺ borç** kaydedilir. Fiilî gider hesabı 710 **520.000 ₺ alacak**, olumlu fiyat farkı 712 ise **15.000 ₺ alacak** kaydedilir; borç ve alacak toplamı 535.000 ₺'dir.",
        "1 Sıra No'lu MSUGT - 710/711/712/713; standart maliyet kapanışı",
    ),
    "finmuh-mlh-gen-0054": cost_accounts_patch(
        "Dönem sonunda üretim makineleri için 40.000 ₺, genel yönetimde kullanılan demirbaşlar için 10.000 ₺ amortisman hesaplanmıştır. İşletme 7/A seçeneğini kullanmaktadır.\n\nAmortisman kaydında borçlandırılacak maliyet hesapları hangisidir?",
        {
            "A": "730 Genel Üretim Giderleri 50.000 ₺",
            "B": "770 Genel Yönetim Giderleri 50.000 ₺",
            "C": "730 Genel Üretim Giderleri 40.000 ₺ ve 770 Genel Yönetim Giderleri 10.000 ₺",
            "D": "720 Direkt İşçilik Giderleri 40.000 ₺ ve 760 Pazarlama, Satış ve Dağıtım Giderleri 10.000 ₺",
            "E": "796 Amortisman ve Tükenme Payları 50.000 ₺",
        },
        "C",
        "Üretim makinelerinin amortismanı üretimle ilgili endirekt giderdir ve **730 hesaba 40.000 ₺** yazılır. Genel yönetim demirbaşı amortismanı ise **770 hesaba 10.000 ₺** kaydedilir. 796 hesabı 7/B seçeneğinde kullanılır.",
        "1 Sıra No'lu MSUGT - 730/770/257",
    ),
    "finmuh-mlh-gen-0055": cost_accounts_patch(
        "7/A seçeneğini kullanan bir hizmet işletmesinde 740 Hizmet Üretim Maliyeti hesabında dönem boyunca 240.000 ₺ gider birikmiş ve hizmetlerin tamamı müşterilere sunulmuştur.\n\nHizmet maliyetinin gelir tablosuna yansıtılmasında yapılacak kayıt hangisidir?",
        {
            "A": "740 Hizmet Üretim Maliyeti borç / 622 Satılan Hizmet Maliyeti alacak",
            "B": "151 Yarı Mamuller - Üretim borç / 741 Hizmet Üretim Maliyeti Yansıtma alacak",
            "C": "741 Hizmet Üretim Maliyeti Yansıtma borç / 622 Satılan Hizmet Maliyeti alacak",
            "D": "622 Satılan Hizmet Maliyeti 240.000 ₺ borç / 741 Hizmet Üretim Maliyeti Yansıtma 240.000 ₺ alacak",
            "E": "621 Satılan Ticari Mallar Maliyeti 240.000 ₺ borç / 740 Hizmet Üretim Maliyeti 240.000 ₺ alacak",
        },
        "D",
        "Sunulmuş hizmetlerin maliyeti gelir tablosunda **622 Satılan Hizmet Maliyeti** hesabına borç, **741 Hizmet Üretim Maliyeti Yansıtma** hesabına alacak kaydedilir. Ayrı kapanış kaydında 741 borçlandırılıp 740 alacaklandırılır.",
        "1 Sıra No'lu MSUGT - 740/741/622",
    ),
    "finmuh-mlh-gen-0056": cost_accounts_patch(
        "7/B seçeneğinde gider çeşidi hesaplarında 790 İlk Madde ve Malzeme Giderleri 180.000 ₺, 791 İşçi Ücret ve Giderleri 120.000 ₺ ve 793 Dışarıdan Sağlanan Fayda ve Hizmetler 40.000 ₺ birikmiştir. Yapılan dağıtımda toplamın 300.000 ₺'si üretime, 40.000 ₺'si genel yönetime aittir.\n\nYansıtma kaydı hangisidir?",
        {
            "A": "798 Gider Çeşitleri Yansıtma 340.000 ₺ borç / 799 Üretim Maliyet Hesabı 300.000 ₺ ve 632 Genel Yönetim Giderleri 40.000 ₺ alacak",
            "B": "799 Üretim Maliyet Hesabı 300.000 ₺ ve 632 Genel Yönetim Giderleri 40.000 ₺ borç / 798 Gider Çeşitleri Yansıtma 340.000 ₺ alacak",
            "C": "799 Üretim Maliyet Hesabı 340.000 ₺ borç / 798 Gider Çeşitleri Yansıtma 340.000 ₺ alacak",
            "D": "151 Yarı Mamuller - Üretim 300.000 ₺ ve 770 Genel Yönetim Giderleri 40.000 ₺ borç / 790, 791 ve 793 hesapları 340.000 ₺ alacak",
            "E": "710, 720 ve 730 hesapları toplam 300.000 ₺ ve 770 hesap 40.000 ₺ borç / 798 hesap 340.000 ₺ alacak",
        },
        "B",
        "7/B'de gider çeşitleri 798 hesap aracılığıyla fonksiyonlara yansıtılır. Üretim payı **799 hesaba 300.000 ₺**, genel yönetim payı **632 hesaba 40.000 ₺ borç**; toplam **340.000 ₺ 798 hesaba alacak** kaydedilir.",
        "1 Sıra No'lu MSUGT - 7/B, 790-799 ve 632",
    ),
    "finmuh-mlh-gen-0057": cost_accounts_patch(
        "Fabrika makinelerinin elektrik tüketimine ait gider, 7/A ve 7/B seçeneklerinde sırasıyla hangi hesaplarda izlenir?",
        {
            "A": "730 Genel Üretim Giderleri; 793 Dışarıdan Sağlanan Fayda ve Hizmetler",
            "B": "710 Direkt İlk Madde ve Malzeme Giderleri; 790 İlk Madde ve Malzeme Giderleri",
            "C": "720 Direkt İşçilik Giderleri; 791 İşçi Ücret ve Giderleri",
            "D": "760 Pazarlama, Satış ve Dağıtım Giderleri; 794 Çeşitli Giderler",
            "E": "770 Genel Yönetim Giderleri; 797 Finansman Giderleri",
        },
        "A",
        "7/A giderleri fonksiyon esasına göre izlediğinden fabrika elektriği **730 Genel Üretim Giderleri** hesabındadır. 7/B gider çeşidi esasını kullandığından aynı gider **793 Dışarıdan Sağlanan Fayda ve Hizmetler** hesabında izlenir.",
        "1 Sıra No'lu MSUGT - 7/A ve 7/B hesap ayrımı, 730/793",
    ),
    "finmuh-mlh-gen-0058": cost_accounts_patch(
        "Bir üretim işletmesinde dönem başı ilk madde ve malzeme stoku 40.000 ₺, dönem içi alışlar 260.000 ₺ ve dönem sonu stok 50.000 ₺'dir. Kullanılan malzemenin tamamı direkt niteliktedir. Direkt işçilik 150.000 ₺, genel üretim giderleri 100.000 ₺, dönem başı ve sonu yarı mamul stokları 30.000 ve 20.000 ₺, dönem başı ve sonu mamul stokları ise 60.000 ve 70.000 ₺'dir.\n\nSatılan mamuller maliyeti kaç ₺'dir?",
        {
            "A": "470.000",
            "B": "480.000",
            "C": "490.000",
            "D": "510.000",
            "E": "500.000",
        },
        "E",
        "Kullanılan direkt malzeme 40.000 + 260.000 − 50.000 = 250.000 ₺; üretim giderleri 250.000 + 150.000 + 100.000 = 500.000 ₺'dir. Tamamlanan mamul maliyeti 30.000 + 500.000 − 20.000 = 510.000 ₺; satılan mamuller maliyeti 60.000 + 510.000 − 70.000 = **500.000 ₺** olur.",
        "1 Sıra No'lu MSUGT - Satışların Maliyeti Tablosu",
    ),
    "finmuh-mlh-gen-0059": cost_accounts_patch(
        "Dönemde üretimi tamamlanan mamullerin maliyeti 420.000 ₺, bunlardan satılanların maliyeti 300.000 ₺'dir.\n\nTamamlanma ve satış maliyeti kayıtları hangisidir?",
        {
            "A": "151 Yarı Mamuller - Üretim 420.000 ₺ borç / 152 Mamuller 420.000 ₺ alacak; 152 Mamuller 300.000 ₺ borç / 620 Satılan Mamuller Maliyeti 300.000 ₺ alacak",
            "B": "152 Mamuller 420.000 ₺ borç / 620 Satılan Mamuller Maliyeti 420.000 ₺ alacak; satışta ayrı maliyet kaydı yapılmaz",
            "C": "152 Mamuller 420.000 ₺ borç / 151 Yarı Mamuller - Üretim 420.000 ₺ alacak; 620 Satılan Mamuller Maliyeti 300.000 ₺ borç / 152 Mamuller 300.000 ₺ alacak",
            "D": "620 Satılan Mamuller Maliyeti 420.000 ₺ borç / 151 Yarı Mamuller - Üretim 420.000 ₺ alacak; 152 Mamuller 300.000 ₺ borç / 620 Satılan Mamuller Maliyeti 300.000 ₺ alacak",
            "E": "152 Mamuller 120.000 ₺ borç ve 620 Satılan Mamuller Maliyeti 300.000 ₺ borç / 151 Yarı Mamuller - Üretim 420.000 ₺ alacak",
        },
        "C",
        "Tamamlanan üretim **152 borç / 151 alacak 420.000 ₺** kaydıyla mamul stoklarına alınır. Satılan kısmın maliyeti ise **620 borç / 152 alacak 300.000 ₺** kaydıyla gelir tablosuna aktarılır.",
        "1 Sıra No'lu MSUGT - 151/152/620",
    ),
    "finmuh-mlh-gen-0060": cost_accounts_patch(
        "Maliyet hesaplarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Normal maliyet yönteminde değişken genel üretim giderleri fiilî üretime, sabit genel üretim giderleri normal kapasiteye göre maliyete yüklenir.\n\nII. Düşük kapasite nedeniyle dağıtılmayan sabit genel üretim gideri stok maliyetine eklenmez.\n\nIII. 7/A seçeneğinde 710, 720 ve 730 hesaplarda toplanan üretim giderleri 711, 721 ve 731 yansıtma hesapları aracılığıyla 151 hesaba aktarılır.\n\nIV. 7/B seçeneğinde giderler çeşit esasına göre 790-797 hesaplarda izlenir; 798 yansıtma ve 799 üretim maliyeti hesapları kullanılır.",
        {
            "A": "I ve II",
            "B": "II ve III",
            "C": "I, II ve III",
            "D": "I, II, III ve IV",
            "E": "Yalnız IV",
        },
        "D",
        "Dört ifade de doğrudur. Normal maliyet düşük kapasitenin stok maliyetini yapay biçimde artırmasını önler. 7/A fonksiyon ve ilgili yansıtma hesaplarını; 7/B ise gider çeşitleriyle 798 ve 799 hesaplarını kullanır.",
        "TMS 2 Stoklar, par. 12-13; 1 Sıra No'lu MSUGT - 7/A ve 7/B",
    ),
}


CURRENCY_DIFFERENCES_PATCHES = {
    'finmuh-kur-gen-0006': currency_differences_patch(
        "Ferhat Dış Ticaret A.Ş.'nin 40.000 USD tutarındaki döviz alacağı, işlem günü kuru 30,00 ₺/USD iken kaydedilmiştir. Alacağın yalnız 25.000 USD'lik kısmı, kurun 32,20 ₺/USD olduğu gün banka aracılığıyla tahsil edilmiştir. Bu kısmi tahsilatta oluşan kur farkı ve niteliği aşağıdakilerden hangisidir?",
        {
            'A': '88.000 ₺ kâr — 646 Kambiyo Kârları',
            'B': '55.000 ₺ kâr — 646 Kambiyo Kârları',
            'C': '33.000 ₺ kâr — 646 Kambiyo Kârları',
            'D': '55.000 ₺ zarar — 656 Kambiyo Zararları',
            'E': '2,20 ₺ kâr — 646 Kambiyo Kârları',
        },
        'B',
        'Kısmi tahsilat yalnız tahsil edilen tutar için kur farkı doğurur: 25.000 × (32,20 − 30,00) = 25.000 × 2,20 = **55.000 ₺**. Alacak + kur yükselişi → lehte **kâr (646)**. Kalan 15.000 USD henüz kapanmadığı için bu tutara girmez (40.000 üzerinden 88.000 ₺ hesaplamak yanlıştır).',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 646; 213 sayılı VUK md. 280",
    ),
    'finmuh-kur-gen-0007': currency_differences_patch(
        "Tuna Makine Ltd. Şti.'nin 30.000 EUR tutarındaki döviz borcu, işlem günü kuru 35,00 ₺/EUR iken kaydedilmiştir. Borcun 12.000 EUR'luk kısmı, kurun 36,50 ₺/EUR olduğu gün banka aracılığıyla ödenmiştir. Bu kısmi ödemede oluşan kur farkı ve hesabı aşağıdakilerden hangisidir?",
        {
            'A': '45.000 ₺ zarar — 656 Kambiyo Zararları',
            'B': '18.000 ₺ kâr — 646 Kambiyo Kârları',
            'C': '18.000 ₺ zarar — 780 Finansman Giderleri',
            'D': '18.000 ₺ zarar — 656 Kambiyo Zararları',
            'E': '1,50 ₺ zarar — 656 Kambiyo Zararları',
        },
        'D',
        'Kısmi ödeme yalnız ödenen 12.000 EUR için kur farkı doğurur: 12.000 × (36,50 − 35,00) = 12.000 × 1,50 = **18.000 ₺**. Borç + kur yükselişi → borcun TL karşılığı arttığından **zarar (656)**. Borcun tamamı (30.000 EUR) üzerinden 45.000 ₺ hesaplamak yanlıştır; bu bir kambiyo zararıdır, finansman gideri (780) değildir.',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 656; 213 sayılı VUK md. 280",
    ),
    'finmuh-kur-gen-0008': currency_differences_patch(
        "Deniz İthalat A.Ş.'nin 20.000 USD tutarındaki borcu işlem günü kuru 31,00 ₺/USD iken kaydedilmiş; birinci dönem sonunda MB döviz alış kuru 33,00 ₺/USD ile değerlenmiştir. Borç, ikinci dönemde kur 32,00 ₺/USD iken ödenmiştir. İKİNCİ dönemde oluşan kur farkı ve niteliği aşağıdakilerden hangisidir?",
        {
            'A': '20.000 ₺ zarar — 656 Kambiyo Zararları',
            'B': '20.000 ₺ kâr — 646 Kambiyo Kârları',
            'C': '40.000 ₺ zarar — 656 Kambiyo Zararları',
            'D': '60.000 ₺ zarar — 656 Kambiyo Zararları',
            'E': 'Kur farkı doğmaz',
        },
        'B',
        'İkinci dönemin kur farkı, o dönemin başlangıç değeri (birinci dönem sonu 33,00) ile ödeme kuru (32,00) arasından hesaplanır: 20.000 × (33,00 − 32,00) = **20.000 ₺**. Borç + kur düşüşü → borç daha az TL ile kapanır → **kâr (646)**. Birinci dönemde 20.000 × 2,00 = 40.000 ₺ zarar ayrıca yazılmıştı.',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 646",
    ),
    'finmuh-kur-gen-0009': currency_differences_patch(
        "Kuzey Enerji A.Ş. dönem sonunda kasasında 5.000 USD efektif (nakit döviz) ve bankada 5.000 USD döviz mevduatı tutmaktadır; ikisi de 30,00 ₺/USD ile kayıtlıdır. Dönem sonunda MB döviz alış kuru 32,00 ₺/USD, MB efektif alış kuru 31,60 ₺/USD'dir. İki kalemin değerlemesinden doğan toplam kur farkı kaç ₺'dir?",
        {
            'A': '20.000 ₺ kâr',
            'B': '16.000 ₺ kâr',
            'C': '8.000 ₺ kâr',
            'D': '10.000 ₺ zarar',
            'E': '18.000 ₺ kâr',
        },
        'E',
        'Kasadaki efektif **efektif alış kuruyla**, bankadaki döviz mevduatı **döviz alış kuruyla** değerlenir. Efektif: 5.000 × (31,60 − 30,00) = 8.000 ₺; mevduat: 5.000 × (32,00 − 30,00) = 10.000 ₺. Toplam = 8.000 + 10.000 = **18.000 ₺ kâr**. İki kaleme tek kur uygulamak (20.000 veya 16.000) yanlıştır.',
        '213 sayılı VUK md. 280',
    ),
    'finmuh-kur-gen-0013': currency_differences_patch(
        "Ege Tekstil A.Ş. 50.000 USD tutarında ihracat faturası düzenlemiştir (fatura ve mal çıkış günü kuru 30,00 ₺/USD). Dönem sonunda alacak MB döviz alış kuru 31,00 ₺/USD ile değerlenmiş; izleyen dönemde kur 33,50 ₺/USD iken tahsil edilmiştir. Bu alacaktan iki dönem toplamında doğan kur farkı kârı kaç ₺'dir?",
        {
            'A': '125.000',
            'B': '175.000',
            'C': '50.000',
            'D': '210.000',
            'E': '165.000',
        },
        'B',
        'İki dönemin toplam kur farkı, ilk kayıt kuru (30,00) ile tahsilat kuru (33,50) arasındaki değişimdir: 50.000 × (33,50 − 30,00) = 50.000 × 3,50 = **175.000 ₺**. (Birinci dönem 50.000 × 1,00 = 50.000 ₺ değerleme kârı, ikinci dönem 50.000 × 2,50 = 125.000 ₺ tahsilat kârı olarak yazılır.)',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 646",
    ),
    'finmuh-kur-gen-0014': currency_differences_patch(
        "Poyraz Ticaret A.Ş., daha önce 300.000 ₺ (10.000 USD × 30,00) olarak '320 Satıcılar'a kaydettiği ve malı işletmeye girmiş olan ithalat borcunu, kurun 31,50 ₺/USD olduğu gün banka aracılığıyla ödemiştir. Bu ödemenin yevmiye kaydında aşağıdakilerden hangisi yer alır?",
        {
            'A': '320 Satıcılar (B) 300.000 ve 656 Kambiyo Zararları (B) 15.000; 102 Bankalar (A) 315.000',
            'B': '320 Satıcılar (B) 300.000 ve 153 Ticari Mallar (B) 15.000; 102 Bankalar (A) 315.000',
            'C': '320 Satıcılar (B) 315.000; 102 Bankalar (A) 315.000',
            'D': '320 Satıcılar (B) 300.000 ve 780 Finansman Giderleri (B) 15.000; 102 Bankalar (A) 315.000',
            'E': '320 Satıcılar (B) 315.000; 102 Bankalar (A) 300.000 ve 646 Kambiyo Kârları (A) 15.000',
        },
        'A',
        "Ödenen tutar 10.000 × 31,50 = 315.000 ₺, kayıtlı borç 300.000 ₺; aradaki 10.000 × 1,50 = **15.000 ₺** borç + kur yükselişi olduğundan **kambiyo zararıdır**. Mal işletmeye girmiş (stok maliyeti kesinleşmiş) olduğundan fark 153 Ticari Mallar'a eklenmez; 320 Satıcılar (B) 300.000 ve 656 Kambiyo Zararları (B) 15.000 karşılığında 102 Bankalar (A) 315.000 yazılır.",
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 320/656/102; 213 sayılı VUK md. 280",
    ),
    'finmuh-kur-gen-0015': currency_differences_patch(
        'Arda Otomotiv A.Ş., üretim makinesini kullanıma hazır hâle getirip (aktifleştirip) kayıtlarına aldıktan SONRA, makine için 20.000 USD tutarındaki döviz satıcı borcunu ödemiştir. Borç işlem günü 30,00 ₺/USD ile kaydedilmiş, ödeme günü kur 32,00 ₺/USD olmuştur. Aktifleştirmeden sonra doğan bu kur farkı ne tutarda ve nasıl muhasebeleştirilir?',
        {
            'A': "40.000 ₺ — 253 Tesis, Makine ve Cihazlar'ın maliyetine eklenir",
            'B': "40.000 ₺ — 646 Kambiyo Kârları'na gelir yazılır",
            'C': "40.000 ₺ — 257 Birikmiş Amortismanlar'a eklenir",
            'D': "40.000 ₺ — 656 Kambiyo Zararları'na gider yazılır",
            'E': 'Kur farkı doğmaz; borç kayıtlı değeriyle kapanır',
        },
        'D',
        "Kur farkı = 20.000 × (32,00 − 30,00) = **40.000 ₺**. Varlık **aktifleştirildikten sonra** doğan kur farkları maliyete (253) eklenmez; dönemin kambiyo gider/geliri olarak izlenir. Borç + kur yükselişi olduğundan **656 Kambiyo Zararları**'na gider yazılır. (Aktifleştirmeden önce olsaydı maliyete eklenirdi.)",
        "213 sayılı VUK md. 280; 163 Sıra No'lu VUK Genel Tebliği (MDV kur farkı)",
    ),
    'finmuh-kur-gen-0021': currency_differences_patch(
        "Selen Gıda A.Ş., 30.000 USD tutarındaki döviz alacağının (işlem günü kuru 30,00 ₺/USD) 18.000 USD'lik kısmını, kurun 31,50 ₺/USD olduğu gün banka aracılığıyla tahsil etmiştir. Bu kısmi tahsilatın yevmiye kaydında aşağıdakilerden hangisi yer alır?",
        {
            'A': '102 Bankalar (B) 567.000; 120 Alıcılar (A) 567.000',
            'B': '102 Bankalar (B) 567.000; 120 Alıcılar (A) 540.000 ve 646 Kambiyo Kârları (A) 27.000',
            'C': '102 Bankalar (B) 540.000; 120 Alıcılar (A) 540.000',
            'D': '102 Bankalar (B) 567.000; 120 Alıcılar (A) 540.000 ve 656 Kambiyo Zararları (A) 27.000',
            'E': '120 Alıcılar (B) 567.000; 102 Bankalar (A) 540.000 ve 646 Kambiyo Kârları (A) 27.000',
        },
        'B',
        "Tahsil edilen 18.000 × 31,50 = 567.000 ₺ → 102 Bankalar (B). Kapanan alacak 18.000 × 30,00 = 540.000 ₺ → 120 Alıcılar (A). Aradaki 18.000 × 1,50 = **27.000 ₺** lehte fark → 646 Kambiyo Kârları (A). Kalan 12.000 USD 120 Alıcılar'da izlenmeye devam eder.",
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 102/120/646",
    ),
    'finmuh-kur-gen-0022': currency_differences_patch(
        "Bengi Kimya A.Ş.'nin bankadaki döviz mevduat hesabında 15.000 USD bulunmaktadır ve 30,00 ₺/USD ile kayıtlıdır. Dönem sonunda MB döviz alış kuru 31,20 ₺/USD olduğuna göre yapılacak değerleme kaydı aşağıdakilerden hangisidir?",
        {
            'A': '646 Kambiyo Kârları (B) 18.000; 102 Bankalar (A) 18.000',
            'B': '102 Bankalar (B) 468.000; 646 Kambiyo Kârları (A) 468.000',
            'C': '656 Kambiyo Zararları (B) 18.000; 102 Bankalar (A) 18.000',
            'D': '102 Bankalar (B) 18.000; 642 Faiz Gelirleri (A) 18.000',
            'E': '102 Bankalar (B) 18.000; 646 Kambiyo Kârları (A) 18.000',
        },
        'E',
        'Kur farkı = 15.000 × (31,20 − 30,00) = 15.000 × 1,20 = **18.000 ₺**. Döviz mevduatı (varlık) + kur yükselişi → hesabın TL değeri artar: 102 Bankalar (B) 18.000 / 646 Kambiyo Kârları (A) 18.000. Kaydedilen yalnız **fark**tır; toplam yeni değer (468.000) değil. Bu bir kambiyo kârıdır, faiz geliri (642) değil.',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 102/646",
    ),
    'finmuh-kur-gen-0023': currency_differences_patch(
        'Çınar Mobilya A.Ş. dönem sonunda 20.000 USD tutarında döviz alacağı (kayıt 30,00 ₺/USD; dönem sonu 31,50 ₺/USD) ve 10.000 EUR tutarında döviz borcu (kayıt 35,00 ₺/EUR; dönem sonu 36,00 ₺/EUR) taşımaktadır. Kur farklarının dönem sonucuna NET etkisi nedir?',
        {
            'A': '20.000 ₺ net kâr',
            'B': '40.000 ₺ net kâr',
            'C': '20.000 ₺ net zarar',
            'D': '30.000 ₺ net kâr',
            'E': '10.000 ₺ net zarar',
        },
        'A',
        'Her kalem kendi para birimiyle ayrı değerlenir. Alacak (USD, varlık): 20.000 × (31,50 − 30,00) = 30.000 ₺ **kâr**. Borç (EUR): 10.000 × (36,00 − 35,00) = 10.000 ₺ **zarar**. Net etki = 30.000 − 10.000 = **20.000 ₺ net kâr**. Kalemler farklı dövizde olsa da kayıtları ayrıdır; yalnız dönem sonucuna etkileri netleşir.',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 646/656",
    ),
    'finmuh-kur-gen-0024': currency_differences_patch(
        'Doruk Elektronik A.Ş., kasasındaki 6.000 USD efektifi (kayıt 30,00 ₺/USD) kurun 31,80 ₺/USD olduğu gün bankaya bozdurarak TL hesabına almıştır. Bu işlemin yevmiye kaydında aşağıdakilerden hangisi yer alır?',
        {
            'A': '102 Bankalar (B) 190.800; 100 Kasa (A) 190.800',
            'B': '102 Bankalar (B) 190.800; 100 Kasa (A) 180.000 ve 646 Kambiyo Kârları (A) 10.800',
            'C': '100 Kasa (B) 180.000; 102 Bankalar (A) 180.000',
            'D': '102 Bankalar (B) 180.000; 100 Kasa (A) 180.000',
            'E': '102 Bankalar (B) 190.800; 100 Kasa (A) 180.000 ve 656 Kambiyo Zararları (A) 10.800',
        },
        'B',
        'TL girişi 6.000 × 31,80 = 190.800 ₺ → 102 Bankalar (B). Kasadan çıkan döviz kayıtlı değeriyle 6.000 × 30,00 = 180.000 ₺ → 100 Kasa (A). Aradaki 6.000 × 1,80 = **10.800 ₺** kur yükselişi olduğundan lehte → 646 Kambiyo Kârları (A). Elden çıkarmada kur yükseldiği için kambiyo kârıdır (zarar değil).',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 100/102/646",
    ),
    'finmuh-kur-gen-0025': currency_differences_patch(
        "Efe Denizcilik A.Ş. dönem sonunda 30.000 USD döviz alacağı ve bir miktar USD döviz borcu taşımaktadır (ikisi de aynı kur değişimine tabidir). Dönem sonunda USD kuru 2,00 ₺ yükselmiş ve kur farklarının dönem sonucuna net etkisi 20.000 ₺ kâr olmuştur. Buna göre döviz borcunun tutarı kaç USD'dir?",
        {
            'A': '40.000',
            'B': '10.000',
            'C': '50.000',
            'D': '20.000',
            'E': '30.000',
        },
        'D',
        'Alacaktan (varlık, kur↑) doğan kâr = 30.000 × 2,00 = 60.000 ₺. Net kâr 20.000 ₺ olduğuna göre borçtan doğan zarar = 60.000 − 20.000 = 40.000 ₺. Borç zararı = tutar × 2,00 olduğundan tutar = 40.000 ÷ 2,00 = **20.000 USD**. (Borçta kur yükselişi zarar doğurur; alacak kârını azaltır.)',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 646/656",
    ),
    'finmuh-kur-gen-0026': currency_differences_patch(
        "Gökçe Tarım A.Ş.'nin 40.000 USD tutarındaki alacağı işlem günü 30,00 ₺/USD ile kaydedilmiş; birinci dönem sonunda MB döviz alış kuru 31,00 ₺/USD ile değerlenmiştir. İkinci dönemde alacağın 25.000 USD'lik kısmı, kur 32,00 ₺/USD iken tahsil edilmiştir. Bu kısmi tahsilatta (ikinci dönemde) oluşan kur farkı kârı kaç ₺'dir?",
        {
            'A': '25.000',
            'B': '50.000',
            'C': '40.000',
            'D': '75.000',
            'E': '30.000',
        },
        'A',
        'İkinci dönemin kur farkı, tahsil edilen kısım için dönem başı değeri (31,00) ile tahsilat kuru (32,00) arasından hesaplanır: 25.000 × (32,00 − 31,00) = **25.000 ₺ kâr**. Birinci dönemde 40.000 × 1,00 = 40.000 ₺ değerleme kârı ayrıca yazılmıştı; kalan 15.000 USD için tahsilat henüz yoktur.',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 646",
    ),
    'finmuh-kur-gen-0033': currency_differences_patch(
        "Işık Ambalaj A.Ş.'nin aynı dönemde 12.000 USD döviz kasası ve 12.000 USD döviz cinsi satıcı borcu bulunmaktadır (ikisi de aynı kurla kayıtlıdır). Bu iki kalemin muhasebeleştirilmesiyle ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Eşit tutarlı oldukları için netleştirilir; hiç kur farkı doğmaz.',
            'B': 'İki kalem ayrı hesaplarda izlenir; netleştirilmez, dönem sonunda her biri ayrı değerlenir.',
            'C': 'İkisi tek bir 320 Satıcılar hesabında birleştirilerek gösterilir.',
            'D': "Borç kasadan düşülüp yalnızca aradaki net fark 100 Kasa'da izlenir.",
            'E': 'Eşit oldukları için iki kalem de kayıtlardan çıkarılır.',
        },
        'B',
        'Döviz kasası (100) bir varlık, satıcı borcu (320) bir yabancı kaynaktır; tutarları eşit olsa da farklı hesaplarda **ayrı** izlenir ve netleştirilemez. Dönem sonunda her biri ayrı değerlenir: kasa lehte fark verirken borç aleyhte fark verebilir. Eşitlik, kur farkı doğmayacağı anlamına gelmez.',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 100/320",
    ),
    'finmuh-kur-gen-0034': currency_differences_patch(
        "Hera Kozmetik A.Ş. 8.000 USD tutarında ticari malı, fatura ve mal giriş günü kuru 30,00 ₺/USD iken ithal etmiştir. Borç, kurun 31,25 ₺/USD olduğu gün ödenmiştir. '153 Ticari Mallar' maliyeti ile ödeme sırasında oluşan kur farkı sırasıyla kaç ₺'dir?",
        {
            'A': '250.000 ₺ maliyet — 10.000 ₺ zarar',
            'B': '240.000 ₺ maliyet — 10.000 ₺ kâr',
            'C': '250.000 ₺ maliyet — kur farkı doğmaz',
            'D': '240.000 ₺ maliyet — 10.000 ₺ zarar',
            'E': '240.000 ₺ maliyet — 250.000 ₺ zarar',
        },
        'D',
        'Mal, giriş günü kuruyla stoklara alınır: 8.000 × 30,00 = **240.000 ₺** (153 Ticari Mallar). Ödeme mal girişinden sonra yapıldığından ödeme kur farkı maliyete eklenmez: 8.000 × (31,25 − 30,00) = 8.000 × 1,25 = **10.000 ₺**; borç + kur yükselişi → **zarar (656)**.',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 153/656",
    ),
    'finmuh-kur-gen-0037': currency_differences_patch(
        'Dönem sonu döviz değerlemesiyle ilgili aşağıdaki ifadelerden hangisi YANLIŞTIR?',
        {
            'A': 'Döviz cinsi alacak ve borçlar kural olarak MB döviz alış kuruyla değerlenir.',
            'B': 'Kasadaki efektif döviz, MB efektif alış kuruyla değerlenir.',
            'C': 'Döviz cinsi kalemler dönem sonunda MB döviz satış kuruyla değerlenir.',
            'D': 'Değerleme farkı lehteyse 646, aleyhteyse 656 hesabına yazılır.',
            'E': 'TL cinsi alacak ve borçlarda kur farkı doğmaz.',
        },
        'C',
        'VUK md. 280 uyarınca dövizler, borsa rayici yoksa kural olarak **Merkez Bankası döviz ALIŞ kuruyla** değerlenir; satış kuru esas alınmaz. Bu nedenle satış kurundan söz eden ifade yanlıştır. Kasadaki efektifte efektif alış kuru, lehte/aleyhte farkta 646/656 kullanılması ve TL kalemlerde kur farkı doğmaması doğrudur.',
        '213 sayılı VUK md. 280',
    ),
    'finmuh-kur-gen-0038': currency_differences_patch(
        "Bengisu Lojistik A.Ş.'nin dönem sonu değerlemesinde döviz cinsi alacağı için 40.000 ₺ kambiyo kârı, döviz cinsi borcu için 25.000 ₺ kambiyo zararı tahakkuk ettirilmiştir. Bu gerçekleşmemiş (değerleme) kur farklarının dönemin gelir tablosuna etkisi nedir?",
        {
            'A': '65.000 ₺ net artış',
            'B': '15.000 ₺ net azalış',
            'C': 'Etkisi yoktur; gerçekleşmediği için sonuç hesaplarına yansımaz.',
            'D': '25.000 ₺ net azalış',
            'E': '15.000 ₺ net artış',
        },
        'E',
        "Değerleme (gerçekleşmemiş) kur farkları da 646/656 sonuç hesaplarında izlenir ve dönem kâr/zararına yansır. Net etki = 40.000 (kâr) − 25.000 (zarar) = **15.000 ₺ net artış**. 'Gerçekleşmedi diye gelir tablosunu etkilemez' görüşü yanlıştır; tahsilat/ödemeyi beklemeden dönem sonucuna girer.",
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 646/656",
    ),
    'finmuh-kur-gen-0039': currency_differences_patch(
        "Lale İnşaat A.Ş.'nin kasasında 8.000 EUR efektif bulunmakta ve 36,00 ₺/EUR ile kayıtlıdır. Dönem sonunda MB efektif alış kuru 34,50 ₺/EUR olduğuna göre yapılacak değerleme kaydı aşağıdakilerden hangisidir?",
        {
            'A': '100 Kasa (B) 12.000; 646 Kambiyo Kârları (A) 12.000',
            'B': '656 Kambiyo Zararları (B) 12.000; 100 Kasa (A) 12.000',
            'C': '656 Kambiyo Zararları (B) 276.000; 100 Kasa (A) 276.000',
            'D': '100 Kasa (B) 12.000; 656 Kambiyo Zararları (A) 12.000',
            'E': '780 Finansman Giderleri (B) 12.000; 100 Kasa (A) 12.000',
        },
        'B',
        'Kur farkı = 8.000 × (36,00 − 34,50) = 8.000 × 1,50 = **12.000 ₺**. Döviz kasası (varlık) + kur düşüşü → kasanın TL değeri azalır: 656 Kambiyo Zararları (B) 12.000 / 100 Kasa (A) 12.000. Kaydedilen yalnız azalış tutarıdır (yeni toplam değer 276.000 değil); bu bir kambiyo zararıdır, finansman gideri değil.',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 100/656",
    ),
    'finmuh-kur-gen-0044': currency_differences_patch(
        'Maya Turizm A.Ş., bankadaki TL hesabından 20.000 USD satın alarak döviz mevduat hesabına aktarmıştır (işlem kuru 31,00 ₺/USD). Bu işlemin yevmiye kaydında aşağıdakilerden hangisi yer alır?',
        {
            'A': '102 Bankalar-Döviz (B) 620.000; 102 Bankalar-TL (A) 620.000',
            'B': '102 Bankalar-Döviz (B) 620.000; 646 Kambiyo Kârları (A) 620.000',
            'C': '656 Kambiyo Zararları (B) 620.000; 102 Bankalar-TL (A) 620.000',
            'D': '102 Bankalar-Döviz (B) 620.000; 102 Bankalar-TL (A) 600.000 ve 646 Kambiyo Kârları (A) 20.000',
            'E': '102 Bankalar-TL (B) 620.000; 102 Bankalar-Döviz (A) 620.000',
        },
        'A',
        'Döviz alımı yalnızca bir varlığın (TL) başka bir varlığa (döviz) dönüşmesidir; alım anında kur farkı **doğmaz**. TL hesabından 20.000 × 31,00 = 620.000 ₺ çıkar, döviz mevduatına aynı tutar girer: 102 Bankalar-Döviz (B) 620.000 / 102 Bankalar-TL (A) 620.000. Kur farkı ancak sonraki değerleme veya elden çıkarmada oluşur.',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 102",
    ),
    'finmuh-kur-gen-0045': currency_differences_patch(
        "Nazar Gıda A.Ş., 25.000 USD tutarındaki döviz borcunun (işlem günü kuru 30,00 ₺/USD) 15.000 USD'lik kısmını, kur 32,00 ₺/USD iken banka aracılığıyla ödemiştir. Bu kısmi ödemenin yevmiye kaydında aşağıdakilerden hangisi yer alır?",
        {
            'A': '320 Satıcılar (B) 480.000; 102 Bankalar (A) 480.000',
            'B': '320 Satıcılar (B) 450.000 ve 646 Kambiyo Kârları (B) 30.000; 102 Bankalar (A) 480.000',
            'C': '320 Satıcılar (B) 750.000 ve 656 Kambiyo Zararları (B) 50.000; 102 Bankalar (A) 800.000',
            'D': '320 Satıcılar (B) 450.000 ve 656 Kambiyo Zararları (B) 30.000; 102 Bankalar (A) 480.000',
            'E': '102 Bankalar (B) 480.000; 320 Satıcılar (A) 450.000 ve 656 Kambiyo Zararları (A) 30.000',
        },
        'D',
        'Ödenen 15.000 × 32,00 = 480.000 ₺ → 102 Bankalar (A). Kapanan borç 15.000 × 30,00 = 450.000 ₺ → 320 Satıcılar (B). Aradaki 15.000 × 2,00 = **30.000 ₺** borç + kur yükselişi → 656 Kambiyo Zararları (B). Yalnız ödenen kısım işleme girer; borcun tamamı (25.000) üzerinden hesaplamak yanlıştır.',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 320/656/102",
    ),
    'finmuh-kur-gen-0047': currency_differences_patch(
        "Orkun Madencilik A.Ş. döviz cinsi bir borcunu öderken 33.000 ₺ kambiyo zararı ile karşılaşmış; bu sırada kur 1,50 ₺ değişmiştir. Borcun döviz tutarı kaç USD'dir ve kur ne yönde değişmiştir?",
        {
            'A': '22.000 USD — kur düşmüştür',
            'B': '49.500 USD — kur yükselmiştir',
            'C': '14.667 USD — kur yükselmiştir',
            'D': '22.000 USD — kur değişmemiştir',
            'E': '22.000 USD — kur yükselmiştir',
        },
        'E',
        'Döviz tutarı = kur farkı ÷ birim kur değişimi = 33.000 ÷ 1,50 = **22.000 USD**. Borçta **zarar**, ancak kurun **yükselmesiyle** oluşur (borcun TL karşılığı artar). Dolayısıyla kur yükselmiştir. (Alacakta zarar için kurun düşmesi gerekirdi — yön çeldiricisi.)',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 656",
    ),
    'finmuh-kur-gen-0050': currency_differences_patch(
        "Pınar Tekstil A.Ş.'nin 30.000 USD tutarındaki borcu 30,00 ₺/USD ile kayıtlıdır. Borcun 10.000 USD'lik kısmı kur 31,00 ₺/USD iken ödenmiş; dönem sonunda kalan borç MB döviz alış kuru 32,00 ₺/USD ile değerlenmiştir. Yalnız dönem sonu değerlemesinde (kalan borç için) oluşan kur farkı kaç ₺'dir?",
        {
            'A': '40.000 ₺ zarar',
            'B': '60.000 ₺ zarar',
            'C': '40.000 ₺ kâr',
            'D': '20.000 ₺ zarar',
            'E': '10.000 ₺ zarar',
        },
        'A',
        "Ödemeden sonra kalan borç 30.000 − 10.000 = 20.000 USD'dir. Bu kalan borç kayıtlı 30,00'dan dönem sonu 32,00'a değerlenir: 20.000 × (32,00 − 30,00) = **40.000 ₺**. Borç + kur yükselişi → **zarar (656)**. Ödenen 10.000 USD'nin farkı ayrıca ödeme gününde hesaplanır; dönem sonu değerlemesine girmez.",
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 656",
    ),
    'finmuh-kur-gen-0052': currency_differences_patch(
        "Rüzgar Otomotiv A.Ş.'nin 20.000 USD tutarındaki alacağı 32,00 ₺/USD ile kayıtlıdır. Dönem sonunda MB döviz alış kuru 30,50 ₺/USD'ye gerilemiştir. Bu değerlemenin yevmiye kaydında aşağıdakilerden hangisi yer alır?",
        {
            'A': '120 Alıcılar (B) 30.000; 646 Kambiyo Kârları (A) 30.000',
            'B': '656 Kambiyo Zararları (B) 30.000; 120 Alıcılar (A) 30.000',
            'C': '656 Kambiyo Zararları (B) 610.000; 120 Alıcılar (A) 610.000',
            'D': '120 Alıcılar (B) 30.000; 656 Kambiyo Zararları (A) 30.000',
            'E': '656 Kambiyo Zararları (B) 30.000; 642 Faiz Gelirleri (A) 30.000',
        },
        'B',
        'Kur farkı = 20.000 × (32,00 − 30,50) = 20.000 × 1,50 = **30.000 ₺**. Alacak (varlık) + kur düşüşü → alacağın TL değeri azalır: 656 Kambiyo Zararları (B) 30.000 / 120 Alıcılar (A) 30.000. Alacak alacaklandırılarak azaltılır; kaydedilen yalnız fark tutarıdır (610.000 değil).',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 120/656",
    ),
    'finmuh-kur-gen-0053': currency_differences_patch(
        'Sıla Elektronik A.Ş. dönem sonunda 15.000 USD döviz alacağı, 15.000 USD döviz borcu ve kasasında 5.000 USD efektif taşımaktadır (hepsi 30,00 ₺/USD ile kayıtlı). Dönem sonu MB döviz alış kuru 32,00 ₺/USD olduğunda kur farklarının dönem sonucuna net etkisi nedir?',
        {
            'A': '70.000 ₺ net kâr',
            'B': '10.000 ₺ net zarar',
            'C': '40.000 ₺ net kâr',
            'D': '10.000 ₺ net kâr',
            'E': 'Net etki sıfırdır',
        },
        'D',
        'Kur artışı 2,00 ₺. Varlıklar kâr, borç zarar doğurur: alacak 15.000 × 2,00 = 30.000 ₺ kâr; efektif kasa 5.000 × 2,00 = 10.000 ₺ kâr; borç 15.000 × 2,00 = 30.000 ₺ zarar. Net = (30.000 + 10.000) − 30.000 = **10.000 ₺ net kâr**. Alacak ile borç eşit olduğundan birbirini götürür; net etkiyi kasa yaratır.',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 646/656",
    ),
    'finmuh-kur-gen-0055': currency_differences_patch(
        "Toros Mermer A.Ş., ihracattan gelen ve döviz mevduat hesabında 30,00 ₺/USD ile izlediği 20.000 USD'nin tamamını, kur 31,90 ₺/USD iken bozdurarak TL hesabına almıştır. Bu işlemde oluşan kambiyo kârı ile TL girişi sırasıyla kaç ₺'dir?",
        {
            'A': '38.000 ₺ kâr — 600.000 ₺ giriş',
            'B': '38.000 ₺ kâr — 638.000 ₺ giriş',
            'C': '38.000 ₺ zarar — 638.000 ₺ giriş',
            'D': '1,90 ₺ kâr — 638.000 ₺ giriş',
            'E': '380.000 ₺ kâr — 638.000 ₺ giriş',
        },
        'B',
        'TL girişi = 20.000 × 31,90 = **638.000 ₺**. Kayıtlı değer 20.000 × 30,00 = 600.000 ₺. Kambiyo kârı = 638.000 − 600.000 = 20.000 × 1,90 = **38.000 ₺**. Döviz elden çıkarılırken kur yükseldiği için kâr doğar (646).',
        "1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 102/646",
    ),
    'finmuh-kur-gen-0056': currency_differences_patch(
        "Umut Ambalaj A.Ş.'nin döviz cinsi bir alacağının dönem sonu değerlemesinde 27.000 ₺ kambiyo zararı doğmuş; kur 1,80 ₺ değişmiştir. Buna göre alacağın döviz tutarı kaç USD'dir ve kur ne yönde değişmiştir?",
        {
            'A': '15.000 USD — kur düşmüştür',
            'B': '15.000 USD — kur yükselmiştir',
            'C': '48.600 USD — kur düşmüştür',
            'D': '21.600 USD — kur düşmüştür',
            'E': '15.000 USD — kur değişmemiştir',
        },
        'A',
        'Döviz tutarı = 27.000 ÷ 1,80 = **15.000 USD**. Alacakta (varlık) **zarar**, kurun **düşmesiyle** oluşur (alacağın TL karşılığı azalır). Dolayısıyla kur düşmüştür. (Borçta zarar için kurun yükselmesi gerekirdi.)',
        "213 sayılı VUK md. 280; 1 Sıra No'lu MSUGT (Tekdüzen Hesap Planı) - 656",
    ),
}


PATCHES_BY_PATH = {
    RELATIVE_PATH: PATCHES,
    PROCESS_RELATIVE_PATH: PROCESS_PATCHES,
    INTANGIBLE_RELATIVE_PATH: INTANGIBLE_PATCHES,
    FINANCIAL_INVESTMENT_RELATIVE_PATH: FINANCIAL_INVESTMENT_PATCHES,
    INCOME_STATEMENT_RELATIVE_PATH: INCOME_STATEMENT_PATCHES,
    COST_ACCOUNTS_RELATIVE_PATH: COST_ACCOUNTS_PATCHES,
    CURRENCY_DIFFERENCES_RELATIVE_PATH: CURRENCY_DIFFERENCES_PATCHES,
}


def apply_or_check(path: Path, patches: dict[str, dict], write: bool) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    by_id = {question["id"]: question for question in questions}
    mismatches: list[str] = []
    for question_id, fields in patches.items():
        question = by_id.get(question_id)
        if question is None:
            raise SystemExit(f"Soru bulunamadı: {path}::{question_id}")
        for field, expected in fields.items():
            if question.get(field) != expected:
                mismatches.append(f"{path}::{question_id}.{field}")
                if write:
                    question[field] = expected
        if write and len(set(question["options"].values())) != 5:
            raise SystemExit(f"Seçenek çakışması: {path}::{question_id}")
    if write:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return mismatches


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()

    mismatches: list[str] = []
    for relative_path, patches in PATCHES_BY_PATH.items():
        for path in (ROOT / relative_path, APP_ROOT / relative_path):
            mismatches.extend(apply_or_check(path, patches, args.write))
    if args.check and mismatches:
        print("Bakım builder'ıyla eşleşmeyen alanlar:")
        for mismatch in mismatches:
            print(f"- {mismatch}")
        return 1
    total = sum(len(patches) for patches in PATCHES_BY_PATH.values())
    print(f"{len(PATCHES_BY_PATH)} paket / {total} soru iki repoda doğrulandı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
