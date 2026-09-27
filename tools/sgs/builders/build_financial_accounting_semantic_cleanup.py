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
# maddi_olmayan_duran_varliklar.json -> build_fm_modv_cok_adimli.py (tek sahip)
# mali_duran_varliklar.json -> build_fm_mali_duran_varliklar_cok_adimli.py (tek sahip)
# yabanci_kaynaklar.json -> build_fm_yabanci_kaynaklar_cok_adimli.py (tek sahip)
# ozkaynaklar.json -> build_fm_ozkaynaklar_cok_adimli.py (tek sahip)
# gelir_tablosu_hesaplari.json -> build_fm_gelir_tablosu_cok_adimli.py (tek sahip)
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
