#!/usr/bin/env python3
"""Finansal Muhasebe için uzman incelemeli anlamsal kalite yamaları.

İlk sekiz konu paketindeki aynı kazanımı aynı yönden ölçen tekrarları daha
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
READY_RELATIVE_PATH = "content/finansal_muhasebe/hazir_degerler.json"
STOCK_RELATIVE_PATH = "content/finansal_muhasebe/stoklar.json"
RECEIVABLE_RELATIVE_PATH = "content/finansal_muhasebe/ticari_alacaklar.json"
SECURITIES_RELATIVE_PATH = "content/finansal_muhasebe/menkul_kiymetler.json"
PPE_RELATIVE_PATH = "content/finansal_muhasebe/maddi_duran_varliklar.json"
INTANGIBLE_RELATIVE_PATH = "content/finansal_muhasebe/maddi_olmayan_duran_varliklar.json"


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
            "A": "Yöntem değişikliği hiçbir koşulda yapılamayacağından kavrama aykırıdır.",
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
            "A": "Tutar toplam varlıklara göre küçük olduğu için hata hiçbir koşulda önemli değildir.",
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


READY_PATCHES = {
    "finmuh-hazirdeg-gen-0019": {
        "stem": "İşletmede 10.000 ₺ tutarında sabit kasa avansı oluşturulmuştur. Dönem sonundaki sayımda kasada 2.300 ₺ nakit ve toplam 7.500 ₺ tutarında geçerli harcama belgesi bulunmuştur. Fonun yeniden 10.000 ₺'ye tamamlanması istenmektedir.\n\nBuna göre kasa noksanı ve kasaya konulacak tamamlama tutarı sırasıyla kaç ₺'dir?",
        "options": {
            "A": "200 ₺ noksan; 7.700 ₺ tamamlama",
            "B": "200 ₺ fazla; 7.500 ₺ tamamlama",
            "C": "Noksan veya fazla yok; 7.500 ₺ tamamlama",
            "D": "2.300 ₺ noksan; 10.000 ₺ tamamlama",
            "E": "7.500 ₺ noksan; 2.300 ₺ tamamlama",
        },
        "answer": "A",
        "solution": "Nakit ve belgeler toplamı 2.300 + 7.500 = **9.800 ₺** olduğundan 10.000 − 9.800 = **200 ₺ kasa noksanı** vardır. Kasayı yeniden 10.000 ₺'ye çıkarmak için 10.000 − 2.300 = **7.700 ₺** konulmalıdır. Bu tutarın 7.500 ₺'si belgeli giderleri, 200 ₺'si noksanı karşılar.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (sabit kasa avansı; çok adımlı hesaplama)",
            "legislationRef": "1 Sıra No'lu MSUGT - 100 Kasa ve kasa sayım işlemleri",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-hazirdeg-gen-0020": {
        "stem": "Banka mutabakatında aşağıdaki işlemlerden hangisi doğrudur?",
        "options": {
            "A": "Henüz bankaya ulaşmamış mevduat, işletmenin defter bakiyesinden düşülür.",
            "B": "Henüz bankaya ibraz edilmemiş çekler, işletmenin defter bakiyesine eklenir.",
            "C": "Bankanın doğrudan tahsil ettiği müşteri borcu, banka hesap özetinden düşülür.",
            "D": "Yoldaki mevduat banka hesap özeti bakiyesine eklenir; ödenmemiş çekler bu bakiyeden düşülür.",
            "E": "Bankanın kestiği ve işletmenin kaydetmediği masraf, banka hesap özeti bakiyesine eklenir.",
        },
        "answer": "D",
        "solution": "**Yoldaki mevduat** işletmece kaydedilmiş fakat bankaca henüz kaydedilmemiştir; bu nedenle banka hesap özeti bakiyesine eklenir. **Ödenmemiş çekler** de işletmece kaydedilmiş fakat bankaca henüz ödenmemiştir; banka hesap özeti bakiyesinden düşülür. Banka masrafı ve bankanın doğrudan tahsilatı ise işletmenin defter bakiyesini düzeltir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (banka mutabakatı; sınıflandırma)",
            "legislationRef": "Muhasebe Süreci - 102 Bankalar hesabı ve banka mutabakatı",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-hazirdeg-gen-0024": {
        "stem": "İşletmenin 102 Bankalar hesabı bakiyesi 248.000 ₺'dir. Banka, işletme adına 12.000 ₺ müşteri borcu ile 1.000 ₺ mevduat faizi tahsil etmiş; ayrıca 1.200 ₺ hesap işletim ücreti kesmiştir. Bu üç işlem işletmece henüz kaydedilmemiştir. Yoldaki mevduat ve ödenmemiş çeklerin banka tarafında düzeltileceği dikkate alındığında, işletmenin düzeltilmiş defter bakiyesi kaç ₺'dir?",
        "options": {
            "A": "234.800 ₺",
            "B": "247.800 ₺",
            "C": "258.000 ₺",
            "D": "259.800 ₺",
            "E": "261.200 ₺",
        },
        "answer": "D",
        "solution": "İşletmenin defter bakiyesi; bankanın doğrudan tahsil ettiği 12.000 ₺ ve faiz geliri 1.000 ₺ kadar artırılır, 1.200 ₺ banka masrafı kadar azaltılır: 248.000 + 12.000 + 1.000 − 1.200 = **259.800 ₺**. Yoldaki mevduat ve ödenmemiş çekler banka hesap özeti tarafının düzeltmeleridir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (banka mutabakatı; çok adımlı hesaplama)",
            "legislationRef": "1 Sıra No'lu MSUGT - 102 Bankalar, 642 Faiz Gelirleri ve 653 Komisyon Giderleri",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-hazirdeg-gen-0025": {
        "stem": "İşletmenin dönem başı nakit mevcudu 80.000 ₺, dönem içi nakit tahsilatları 270.000 ₺ ve nakit ödemeleri 310.000 ₺'dir. İşletme dönem sonunda en az 60.000 ₺ nakit bulundurmak istemektedir. Başka bir finansman işlemi olmadığına göre ihtiyaç duyulan kısa vadeli borçlanma kaç ₺'dir?",
        "options": {
            "A": "0 ₺",
            "B": "10.000 ₺",
            "C": "40.000 ₺",
            "D": "60.000 ₺",
            "E": "20.000 ₺",
        },
        "answer": "E",
        "solution": "Finansman öncesi dönem sonu nakit mevcudu 80.000 + 270.000 − 310.000 = **40.000 ₺**dir. Hedeflenen asgari 60.000 ₺'ye ulaşmak için 60.000 − 40.000 = **20.000 ₺** kısa vadeli borçlanma gerekir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (nakit bütçesi; uygulama)",
            "legislationRef": "Nakit Yönetimi - dönem sonu nakit ihtiyacının belirlenmesi",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-hazirdeg-gen-0031": {
        "stem": "TMS 7'ye göre bir yatırımın nakit benzeri sayılabilmesi için aşağıdaki özelliklerden hangisinin birlikte bulunması gerekir?",
        "options": {
            "A": "Borsada işlem görmesi ve her durumda özkaynak aracı olması",
            "B": "Uzun vadeli getiri sağlamak amacıyla elde tutulması ve fiyatının sık değişmesi",
            "C": "Yalnız vadesiz banka hesabında izlenmesi ve faiz getirisi bulunmaması",
            "D": "Belirli bir nakit tutarına kolayca çevrilebilmesi, değer değişim riskinin önemsiz olması ve kısa vadeli nakit taahhütleri için tutulması",
            "E": "Edinim maliyetinin yüksek olması ve vadesinin bir yıldan uzun bulunması",
        },
        "answer": "D",
        "solution": "TMS 7'ye göre nakit benzerleri; **belirli bir nakit tutarına kolayca çevrilebilen**, **değerindeki değişim riski önemsiz** olan yüksek likiditeli kısa vadeli yatırımlardır. Yatırım amacıyla değil, kısa vadeli nakit taahhütlerini karşılamak için tutulurlar.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (TMS 7; kavramı uygulama)",
            "legislationRef": "TMS 7 Nakit Akış Tablosu, par. 6-7",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-hazirdeg-gen-0033": {
        "stem": "Bir işletmenin bankadaki kredili cari hesabı talep üzerine geri ödenebilmekte, işletmenin günlük nakit yönetiminin ayrılmaz bir parçasını oluşturmakta ve bakiyesi sık sık artıdan eksiye dönmektedir. TMS 7'ye göre bu hesabın nakit akış tablosundaki değerlendirmesi hangisidir?",
        "options": {
            "A": "Her durumda yatırım faaliyeti olarak sınıflandırılır.",
            "B": "Bu özellikleri taşıdığı için nakit ve nakit benzerlerinin bir unsuru kabul edilebilir.",
            "C": "Bakiyesi eksiye dönebildiği için finansal tablolardan tamamen çıkarılır.",
            "D": "Yalnız özkaynak hesabı olarak raporlanabilir.",
            "E": "Vadesi ne olursa olsun ticari alacak kabul edilir.",
        },
        "answer": "B",
        "solution": "Banka borçlanmaları normalde finansman faaliyetidir. Ancak **talep üzerine geri ödenebilen** ve işletmenin nakit yönetiminin ayrılmaz parçası olan, bakiyesi sık sık artıdan eksiye dönen kredili cari hesaplar TMS 7 uyarınca nakit ve nakit benzerlerinin bir unsuru kabul edilebilir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (TMS 7; istisna senaryosu)",
            "legislationRef": "TMS 7 Nakit Akış Tablosu, par. 8",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-hazirdeg-gen-0047": {
        "stem": "İşletme, bankadan ödenen bir çeki kendi kayıtlarına yanlışlıkla 9.800 ₺ olarak geçirmiştir. Banka hesap özetinde çekin doğru tutarı olan 8.900 ₺ yer almaktadır. Başka hata olmadığına göre banka mutabakatında işletmenin defter bakiyesi nasıl düzeltilmelidir?",
        "options": {
            "A": "900 ₺ azaltılmalıdır.",
            "B": "900 ₺ artırılmalıdır.",
            "C": "8.900 ₺ artırılmalıdır.",
            "D": "9.800 ₺ azaltılmalıdır.",
            "E": "İşletme kaydı banka bakiyesini etkilemediği için düzeltme yapılmamalıdır.",
        },
        "answer": "B",
        "solution": "İşletme 8.900 ₺ yerine 9.800 ₺ çıkış kaydederek banka hesabını **900 ₺ fazla azaltmıştır**. Defter bakiyesini doğru tutara getirmek için 102 Bankalar hesabı **900 ₺ artırılmalıdır**.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (banka mutabakatı; kayıt hatası)",
            "legislationRef": "Muhasebe Süreci - 102 Bankalar hesabı ve banka mutabakatı",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-hazirdeg-gen-0050": {
        "stem": "TMS 7'ye göre aşağıdaki kalemlerden hangisi nakit veya nakit benzeri kapsamında değerlendirilmez?",
        "options": {
            "A": "Kasadaki nakit para",
            "B": "Talep edildiğinde çekilebilen vadesiz banka mevduatı",
            "C": "Uzun vadeli getiri amacıyla elde tutulan ve değeri dalgalanan tahvil yatırımı",
            "D": "Edinildiği tarihte vadesi üç ay veya daha kısa olan, belirli tutara çevrilebilir ve değer değişim riski önemsiz yatırım",
            "E": "Serbestçe kullanılabilen vadesiz döviz mevduatı",
        },
        "answer": "C",
        "solution": "Uzun vadeli getiri amacıyla elde tutulan ve değeri dalgalanan tahvil, kısa vadeli nakit taahhütlerini karşılamaya yönelik bir nakit benzeri değildir. Nakit benzeri yatırım; **edinildiği tarihte genellikle üç ay veya daha kısa vadeli**, belirli nakit tutarına kolayca çevrilebilir ve değer değişim riski önemsiz olmalıdır.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (TMS 7; sınıflandırma)",
            "legislationRef": "TMS 7 Nakit Akış Tablosu, par. 6-7",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-hazirdeg-gen-0052": {
        "stem": "İşletme, on iki ay vadeli bir mevduatı açılış tarihinde yatırım amacıyla edinmiştir. Dönem sonunda mevduatın vadesine iki ay kalmıştır. Tutar belirli olsa ve risk değişmemiş olsa bile, yalnız kalan vadenin iki aya düşmesi TMS 7 bakımından hangi sonucu doğurur?",
        "options": {
            "A": "Mevduat geriye dönük olarak edinildiği tarihten itibaren nakit sayılır.",
            "B": "Mevduat zorunlu olarak özkaynak aracına dönüşür.",
            "C": "Kalan vade üç aydan az olduğu için başka ölçüt aranmadan kasa hesabına aktarılır.",
            "D": "Mevduatın vadesi dikkate alınmaz; yalnız faiz oranına bakılır.",
            "E": "Başlangıçta on iki aylık yatırım olarak edinildiğinden, kalan vadenin kısalması tek başına onu nakit benzerine dönüştürmez.",
        },
        "answer": "E",
        "solution": "TMS 7'de kısa vade değerlendirmesi yatırımın **edinildiği tarihten itibaren** yapılır; ayrıca elde tutma amacı ve değer değişim riski de dikkate alınır. Başlangıçta on iki aylık yatırım olarak edinilen mevduat, yalnız vadesine iki ay kalması nedeniyle kendiliğinden nakit benzeri olmaz.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (TMS 7; kalan vade tuzağı)",
            "legislationRef": "TMS 7 Nakit Akış Tablosu, par. 7",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-hazirdeg-gen-0059": {
        "stem": "İşletmenin vadesiz banka mevduatındaki 500.000 ₺, bir kredi sözleşmesi gereği on dört ay boyunca kullanılamayacak şekilde bloke edilmiştir. TMS 7 ve finansal tablo kullanıcılarının likidite değerlendirmesi açısından en uygun uygulama hangisidir?",
        "options": {
            "A": "Vadesiz hesapta bulunduğu için tutarı hiçbir açıklama yapmadan nakit olarak sunmak",
            "B": "Kullanım kısıtı nedeniyle tutarı nakit dışında uygun bir kalemde ayrı sunmak ve kısıtın niteliğiyle süresini açıklamak",
            "C": "Tutarı doğrudan dönem gideri yazmak",
            "D": "Bloke edilen tutarı işletmenin yabancı kaynağı olarak göstermek",
            "E": "Mevduatı ve ilgili kısıtı finansal tablolardan tamamen çıkarmak",
        },
        "answer": "B",
        "solution": "Talep edildiğinde serbestçe kullanılamayan mevduat, yalnız vadesiz hesapta yer aldığı için nakit kabul edilemez. On dört aylık kullanım kısıtı likidite değerlendirmesi için önemlidir; tutar **nakit dışında uygun bir kalemde ayrı sunulmalı**, kısıtın niteliği ve süresi açıklanmalıdır.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (TMS 7; kısıtlı mevduat)",
            "legislationRef": "TMS 7 Nakit Akış Tablosu; KGK 2022 Yıllık İnceleme Raporu, Nakit ve Nakit Benzerleri",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
}


STOCK_PATCHES = {
    "finmuh-stok-gen-0005": {
        "stem": "Bir sanat galerisi, maliyetleri sırasıyla 18.000 ₺, 22.000 ₺, 27.000 ₺ ve 33.000 ₺ olan ve her biri ayrı seri numarasıyla izlenen dört eserden 22.000 ₺ ve 33.000 ₺ maliyetli olanları satmıştır. TMS 2'deki gerçek parti maliyeti (özel maliyet) yöntemine göre satılan eserlerin maliyeti kaç ₺'dir?",
        "options": {
            "A": "40.000 ₺",
            "B": "45.000 ₺",
            "C": "49.000 ₺",
            "D": "55.000 ₺",
            "E": "60.000 ₺",
        },
        "answer": "D",
        "solution": "Birbirinin yerine kullanılamayan ve ayrı ayrı izlenebilen stoklarda maliyet, satılan belirli birimlerle eşleştirilir. Satılan iki eserin maliyeti 22.000 + 33.000 = **55.000 ₺**dir; diğer eserlerin ortalaması kullanılmaz.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (özel maliyet; sayısal uygulama)",
            "legislationRef": "TMS 2 Stoklar, par. 23",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-stok-gen-0006": {
        "solution": "Fiyatlar yükselirken FIFO'da satılan mallar **eski ve daha düşük maliyetli** birimlerden oluşur; bu nedenle ağırlıklı ortalamaya göre satılan malın maliyeti daha düşük, dönem kârı daha yüksek çıkar. Dönem sonu stok ise daha yeni ve pahalı birimlerden oluştuğu için daha yüksek değerlenir.",
    },
    "finmuh-stok-gen-0015": {
        "stem": "Bir işletme, liste fiyatı 200.000 ₺ olan ticari malı 10.000 ₺ ticari iskonto sonrası satın almıştır. Malın işletme stoklarına girdiği tarihe kadar 8.000 ₺ nakliye, 2.000 ₺ sigorta ve bu alımın finansmanında kullanılan krediye ilişkin 4.000 ₺ faiz gideri oluşmuştur. İndirilebilir KDV dikkate alınmayacaktır.\n\nVUK'un güncel 262 ve 274'üncü maddelerine göre emtianın maliyet bedeli kaç ₺'dir?",
        "options": {
            "A": "190.000 ₺",
            "B": "198.000 ₺",
            "C": "200.000 ₺",
            "D": "204.000 ₺",
            "E": "214.000 ₺",
        },
        "answer": "D",
        "solution": "Net alış bedeli 200.000 − 10.000 = 190.000 ₺'dir. VUK 262 uyarınca emtianın stoklara girdiği tarihe kadarki nakliye, sigorta ve kredi faizi maliyete dâhildir: 190.000 + 8.000 + 2.000 + 4.000 = **204.000 ₺**. Bu vergi değerlemesi, TMS 2'deki vadeli satın alma finansman unsurundan ayrı değerlendirilir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (VUK maliyet bedeli; güncel sayısal uygulama)",
            "legislationRef": "213 sayılı VUK md. 262 ve 274 (7338 sayılı Kanun sonrası güncel metin)",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-stok-gen-0029": {
        "stem": "Bir ticari mal kaleminde dönem başı stok 100 birim × 10 ₺, dönem içi alışlar 200 birim × 13 ₺ ve 100 birim × 16 ₺'dir. Dönemde 250 birim satılmıştır. FIFO yöntemine göre satılan malın maliyeti kaç ₺'dir?",
    },
    "finmuh-stok-gen-0031": {
        "stem": "Bir üretim sürecinde ana ürünle birlikte önemsiz nitelikte bir yan ürün elde edilmiştir. Ortak üretim maliyeti 300.000 ₺, yan ürünün net gerçekleşebilir değeri 20.000 ₺'dir. İşletme yan ürünü TMS 2'deki uygulama kolaylığı kapsamında net gerçekleşebilir değeriyle ölçmektedir.\n\nAna ürüne yüklenecek ortak maliyet kaç ₺'dir?",
        "options": {
            "A": "300.000 ₺",
            "B": "280.000 ₺",
            "C": "320.000 ₺",
            "D": "20.000 ₺",
            "E": "150.000 ₺",
        },
        "answer": "B",
        "solution": "Önemsiz yan ürün net gerçekleşebilir değeriyle ölçüldüğünde bu tutar ana ürünün maliyetinden düşülür. Ana ürüne yüklenecek maliyet 300.000 − 20.000 = **280.000 ₺**dir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (ortak ürün ve yan ürün; sayısal uygulama)",
            "legislationRef": "TMS 2 Stoklar, par. 14",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-stok-gen-0033": {
        "stem": "Bir işletmenin dönem sonu stokları 18.000 ₺ fazla sayılmıştır. Alışlar ve satışlar doğru kaydedilmiş, hata izleyen dönemde tekrarlanmamıştır. Bu hatanın cari ve izleyen dönem kârlarına etkisi hangisidir?",
        "options": {
            "A": "Cari dönem kârı 18.000 ₺ fazla, izleyen dönem kârı 18.000 ₺ eksik hesaplanır.",
            "B": "Her iki dönemin kârı da 18.000 ₺ fazla hesaplanır.",
            "C": "Cari dönem kârı 18.000 ₺ eksik, izleyen dönem kârı 18.000 ₺ fazla hesaplanır.",
            "D": "Yalnız cari dönem satış hasılatı 18.000 ₺ azalır; kâr etkilenmez.",
            "E": "Hata satılan malın maliyetini ve dönem kârlarını etkilemez.",
        },
        "answer": "A",
        "solution": "Dönem sonu stokunun 18.000 ₺ fazla gösterilmesi cari dönemde satılan malın maliyetini aynı tutarda **eksik**, kârı **fazla** gösterir. Hatalı dönem sonu stoku izleyen dönemin dönem başı stoku olduğundan, hata tekrarlanmazsa izleyen dönemin maliyeti 18.000 ₺ fazla ve kârı 18.000 ₺ eksik çıkar.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (stok hatası; dönemler arası etki)",
            "legislationRef": "Muhasebe Süreci - dönem başı stok + alışlar - dönem sonu stok eşitliği",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-stok-gen-0038": {
        "stem": "Satıcı, 28 Aralık'ta malları FOB varış (teslim) noktası koşuluyla müşteriye göndermiştir. Mallar 31 Aralık'ta hâlâ yolda olup müşteriye 3 Ocak'ta teslim edilmiştir. Dönem sonu stok kesimi bakımından en uygun işlem hangisidir?",
        "options": {
            "A": "Mallar 28 Aralık'ta müşterinin stoklarına alınır; satıcı stoktan çıkarır.",
            "B": "Mallar taşıma süresince hiçbir işletmenin stokunda gösterilmez.",
            "C": "Malların yarısı satıcının, yarısı müşterinin stokunda gösterilir.",
            "D": "Teslim 3 Ocak'ta gerçekleştiğinden mallar 31 Aralık'ta satıcının stoklarında kalır.",
            "E": "Nakliye işletmesi malları kendi ticari malı olarak kaydeder.",
        },
        "answer": "D",
        "solution": "FOB **varış noktası** koşulunda kontrol, risk ve mülkiyet teslim noktasına ulaşılıncaya kadar satıcıda kalır. Mallar 31 Aralık'ta henüz teslim edilmediği için satıcının dönem sonu stoklarına dâhil edilir; müşteri 3 Ocak'ta kaydeder.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (stok kesimi; FOB varış noktası)",
            "legislationRef": "Dönemsellik ve stok sayımı - FOB varış noktası teslim koşulu",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-stok-gen-0039": {
        "stem": "İşletme, liste fiyatı 100.000 ₺ olan ticari malı %10 ticari iskonto ve %20 KDV ile veresiye satın almıştır. KDV indirilebilir niteliktedir. Sürekli envanter yönteminde alış kaydı hangisidir?",
        "options": {
            "A": "153 Ticari Mallar (B) 100.000 + 191 İndirilecek KDV (B) 20.000 / 320 Satıcılar (A) 120.000",
            "B": "153 Ticari Mallar (B) 90.000 + 191 İndirilecek KDV (B) 18.000 / 320 Satıcılar (A) 108.000",
            "C": "153 Ticari Mallar (B) 90.000 + 191 İndirilecek KDV (B) 20.000 / 320 Satıcılar (A) 110.000",
            "D": "153 Ticari Mallar (B) 108.000 / 320 Satıcılar (A) 108.000",
            "E": "320 Satıcılar (B) 108.000 / 153 Ticari Mallar (A) 90.000 + 391 Hesaplanan KDV (A) 18.000",
        },
        "answer": "B",
        "solution": "Ticari iskonto alış fiyatından düşülür: 100.000 × %90 = **90.000 ₺** stok maliyeti. İndirilecek KDV 90.000 × %20 = **18.000 ₺**, satıcıya borç 108.000 ₺'dir. Kayıt: 153 (B) 90.000 + 191 (B) 18.000 / 320 (A) 108.000.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (ticari iskonto ve KDV; yevmiye kaydı)",
            "legislationRef": "TMS 2 Stoklar, par. 11; 1 Sıra No'lu MSUGT - 153, 191 ve 320 hesapları",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-stok-gen-0040": {
        "stem": "Bir üretim işletmesinin normal kapasitesi 10.000 birim, yıllık sabit genel üretim gideri 500.000 ₺'dir. Dönemde olağan koşullarda 8.000 birim üretilmiştir. TMS 2'ye göre stoklara yüklenecek sabit genel üretim gideri ve dönem gideri yazılacak dağıtılmamış tutar sırasıyla kaç ₺'dir?",
        "options": {
            "A": "500.000 ₺ ve 0 ₺",
            "B": "320.000 ₺ ve 180.000 ₺",
            "C": "400.000 ₺ ve 100.000 ₺",
            "D": "500.000 ₺ ve 100.000 ₺",
            "E": "400.000 ₺ ve 0 ₺",
        },
        "answer": "C",
        "solution": "Normal kapasiteye göre sabit gider yükleme oranı 500.000 / 10.000 = **50 ₺/birim**dir. 8.000 birime 8.000 × 50 = **400.000 ₺** yüklenir. Kullanılmayan kapasiteye düşen **100.000 ₺** stok maliyetine eklenmez, oluştuğu dönemde gider yazılır.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (normal kapasite; çok adımlı hesaplama)",
            "legislationRef": "TMS 2 Stoklar, par. 13",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-stok-gen-0044": {
        "stem": "Perakende yöntemini kullanan bir işletmede satışa hazır malların perakende satış değeri 600.000 ₺, maliyetin perakende satış değerine oranı %75 ve dönem içi satışların perakende değeri 440.000 ₺'dir. TMS 2'ye göre tahmini dönem sonu stok maliyeti kaç ₺'dir?",
        "options": {
            "A": "90.000 ₺",
            "B": "110.000 ₺",
            "C": "120.000 ₺",
            "D": "160.000 ₺",
            "E": "330.000 ₺",
        },
        "answer": "C",
        "solution": "Dönem sonu stokunun perakende değeri 600.000 − 440.000 = **160.000 ₺**dir. Maliyet oranı uygulanır: 160.000 × %75 = **120.000 ₺** tahmini stok maliyeti.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (perakende yöntemi; sayısal uygulama)",
            "legislationRef": "TMS 2 Stoklar, par. 22",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-stok-gen-0046": {
        "stem": "Dönem başı ticari mal stoku 60.000 ₺, net alışlar 340.000 ₺ ve net satışlar 500.000 ₺'dir. İşletmenin satışlar üzerinden brüt kâr oranı %30'dur. Brüt kâr yöntemine göre tahmini dönem sonu stok tutarı kaç ₺'dir?",
        "options": {
            "A": "50.000 ₺",
            "B": "90.000 ₺",
            "C": "150.000 ₺",
            "D": "350.000 ₺",
            "E": "400.000 ₺",
        },
        "answer": "A",
        "solution": "Tahmini brüt kâr 500.000 × %30 = 150.000 ₺; tahmini satılan malın maliyeti 500.000 − 150.000 = **350.000 ₺**dir. Satışa hazır mallar 60.000 + 340.000 = 400.000 ₺ olduğundan dönem sonu stok 400.000 − 350.000 = **50.000 ₺**dir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (brüt kâr yöntemi; çok adımlı hesaplama)",
            "legislationRef": "Stok Envanteri - brüt kâr yöntemiyle tahmini stok hesabı",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-stok-gen-0051": {
        "stem": "Maliyeti 200.000 ₺ olan bir stok önceki dönemde net gerçekleşebilir değeri 150.000 ₺ olduğu için bu tutara indirilmiştir. Cari dönemde net gerçekleşebilir değer 190.000 ₺'ye yükselmiştir. TMS 2'ye göre cari dönemde iptal edilecek değer düşüklüğü ve stokun yeni defter değeri sırasıyla kaç ₺'dir?",
        "options": {
            "A": "50.000 ₺ ve 200.000 ₺",
            "B": "10.000 ₺ ve 200.000 ₺",
            "C": "40.000 ₺ ve 190.000 ₺",
            "D": "40.000 ₺ ve 240.000 ₺",
            "E": "190.000 ₺ ve 190.000 ₺",
        },
        "answer": "C",
        "solution": "Önceki defter değeri 150.000 ₺, yeni net gerçekleşebilir değer 190.000 ₺ olduğundan **40.000 ₺** değer düşüklüğü iptal edilir. Yeni defter değeri **190.000 ₺** olur; iptal sonucunda stok ilk maliyeti olan 200.000 ₺'nin üzerine çıkarılamaz.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (değer düşüklüğü iptali; sayısal uygulama)",
            "legislationRef": "TMS 2 Stoklar, par. 33",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-stok-gen-0053": {
        "stem": "Dönem sonu stok sayımının güvenilirliğini en fazla güçlendiren uygulama hangisidir?",
        "options": {
            "A": "Depo sorumlusunun stokları tek başına sayması ve farkları açıklama yapmadan değiştirmesi",
            "B": "Sayım ekiplerine sistemdeki miktarların önceden verilmesi ve yalnız aynı rakamların doğrulatılması",
            "C": "Sayım sırasında mal giriş ve çıkışlarının belge numarası alınmadan sürdürülmesi",
            "D": "Kullanılmayan sayım etiketlerinin izlenmemesi ve sayım farklarının araştırılmaması",
            "E": "Sayımın stok muhafazasından bağımsız ekiplerce, numaralı tutanak ve giriş-çıkış kesim kontrolüyle yapılması; önemli farkların yeniden sayılması",
        },
        "answer": "E",
        "solution": "Bağımsız sayım ekipleri, önceden numaralandırılmış tutanakların eksiksiz takibi, sayım tarihindeki giriş-çıkışların kesim kontrolü ve farkların yeniden sayılması; hem hata hem de stokların gizlenmesi riskini azaltır. Diğer uygulamalar görevlerin ayrılığını ve sayım izini zayıflatır.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (stok sayımı; iç kontrol senaryosu)",
            "legislationRef": "Muhasebe Bilgi Sistemleri - fiziki stok sayımı ve kesim kontrolleri",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-stok-gen-0054": {
        "stem": "Maliyeti 100.000 ₺ olan stok önceki dönemde 72.000 ₺ net gerçekleşebilir değere indirilmiştir. Cari dönemde net gerçekleşebilir değer 110.000 ₺'ye yükselmiştir. TMS 2'ye göre iptal edilebilecek azami değer düşüklüğü ve stokun ulaşabileceği azami defter değeri sırasıyla kaç ₺'dir?",
        "options": {
            "A": "38.000 ₺ ve 110.000 ₺",
            "B": "10.000 ₺ ve 110.000 ₺",
            "C": "72.000 ₺ ve 100.000 ₺",
            "D": "28.000 ₺ ve 100.000 ₺",
            "E": "28.000 ₺ ve 128.000 ₺",
        },
        "answer": "D",
        "solution": "Önceki indirgeme 100.000 − 72.000 = **28.000 ₺**dir. Net gerçekleşebilir değer 110.000 ₺ olsa da iptal, önceki indirgeme tutarıyla sınırlıdır; stok maliyetinin üzerine çıkarılamaz. Bu nedenle en çok 28.000 ₺ iptal edilir ve defter değeri **100.000 ₺** olur.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (değer düşüklüğü iptal sınırı)",
            "legislationRef": "TMS 2 Stoklar, par. 33",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-stok-gen-0057": {
        "stem": "Bir üretim sürecine toplam maliyeti 90.000 ₺ olan 1.000 birim girdi verilmiştir. Sürecin normal fire oranı %10 ve firenin hurda değeri sıfırdır. Fiilî sağlam üretim de beklenen 900 birim olarak gerçekleşmiştir. Normal fire maliyeti sağlam birimlere dağıtıldığına göre bir sağlam birimin maliyeti kaç ₺'dir?",
        "options": {
            "A": "100 ₺",
            "B": "90 ₺",
            "C": "81 ₺",
            "D": "110 ₺",
            "E": "111,11 ₺",
        },
        "answer": "A",
        "solution": "Normal fire 1.000 × %10 = 100 birim, beklenen sağlam üretim **900 birim**dir. Normal fire ayrı bir dönem zararı yapılmayıp sağlam birimlerin maliyetine taşınır: 90.000 / 900 = **100 ₺/birim**.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (normal fire; sayısal uygulama)",
            "legislationRef": "TMS 2 Stoklar, par. 16(a) - normalin üstündeki kayıpların maliyet dışı bırakılması",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-stok-gen-0060": {
        "stem": "TMS 2'ye göre stok maliyet formüllerinin seçimiyle ilgili aşağıdaki ifadelerden hangisi doğrudur?",
        "options": {
            "A": "Aynı nitelik ve kullanıma sahip stoklarda her dönem rastgele farklı maliyet formülü seçilebilir.",
            "B": "Stokların yalnız farklı şehirlerde bulunması farklı maliyet formülü kullanmak için tek başına yeterlidir.",
            "C": "TMS 2 benzer stoklarda yalnız LIFO yönteminin kullanılmasını zorunlu tutar.",
            "D": "Benzer nitelik ve kullanıma sahip stoklar için aynı maliyet formülü tutarlı biçimde uygulanır; farklı nitelik veya kullanım farklı formülü haklı kılabilir.",
            "E": "Maliyet formülü seçimi finansal tablolardaki stok tutarını etkilemediğinden açıklanmaz.",
        },
        "answer": "D",
        "solution": "TMS 2, işletme açısından **benzer nitelik ve kullanıma** sahip stoklarda aynı maliyet formülünün tutarlı uygulanmasını ister. Nitelik veya kullanım farklılığı başka bir formülü haklı kılabilir; yalnız coğrafi konum farkı tek başına yeterli değildir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (maliyet formülü; tutarlılık)",
            "legislationRef": "TMS 2 Stoklar, par. 25",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
}


RECEIVABLE_PATCHES = {
    "finmuh-ticalacak-gen-0003": {
        "stem": "Bir işletme, nakit satış fiyatı 100.000 ₺ olan malı müşterisine iki yıl sonra tahsil edilmek üzere 121.000 ₺'ye satmıştır. Sözleşmedeki finansman etkisi önemlidir ve KDV ihmal edilecektir. TFRS 15'e göre malın devredildiği tarihte hasılat ve sonraki dönemlerde finansman geliri olarak muhasebeleştirilecek toplam tutarlar sırasıyla kaç ₺'dir?",
        "options": {
            "A": "121.000 ₺ hasılat; finansman geliri yok",
            "B": "100.000 ₺ hasılat; 100.000 ₺ finansman geliri",
            "C": "21.000 ₺ hasılat; 100.000 ₺ finansman geliri",
            "D": "100.000 ₺ hasılat; 21.000 ₺ finansman geliri",
            "E": "121.000 ₺ hasılat; 21.000 ₺ finansman gideri",
        },
        "answer": "D",
        "solution": "Önemli finansman bileşeni bulunan satışta hasılat, malın devrindeki **nakit satış fiyatı olan 100.000 ₺** üzerinden kaydedilir. Taahhüt edilen 121.000 ₺ ile nakit satış fiyatı arasındaki **21.000 ₺**, finansman süresi boyunca etkin faiz esasına göre finansman geliri olarak muhasebeleştirilir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (vadeli satış; finansman bileşeni)",
            "legislationRef": "TFRS 15 Müşteri Sözleşmelerinden Hasılat, par. 60-61",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-ticalacak-gen-0004": {
        "stem": "İşletme 100.000 ₺ tutarındaki ticari alacağını, borçlunun ödememesi hâlinde faktörün işletmeye başvurma hakkı bulunmayacak şekilde 96.000 ₺'ye devretmiştir. Alacağa ilişkin başlıca risk ve getiriler faktöre geçmiştir. TFRS 9'a göre en uygun muhasebeleştirme hangisidir?",
        "options": {
            "A": "Alacak finansal tablolardan çıkarılır; 96.000 ₺ nakit ve 4.000 ₺ devir zararı muhasebeleştirilir.",
            "B": "Alacak bilançoda aynen tutulur; alınan 96.000 ₺ satış hasılatı yazılır.",
            "C": "Alacağın yalnız 4.000 ₺'lik kısmı bilançodan çıkarılır.",
            "D": "Alacak 100.000 ₺ artırılır ve 96.000 ₺ finansman gideri kaydedilir.",
            "E": "Devir hiçbir kayıt doğurmaz; tahsilat yapılıncaya kadar beklenir.",
        },
        "answer": "A",
        "solution": "Rücusuz devirde başlıca kredi riski ve getiriler faktöre geçmişse finansal varlık bilanço dışı bırakılır. İşletme **96.000 ₺ nakit** alır ve alacağın 100.000 ₺ defter değeriyle arasındaki **4.000 ₺ farkı devir zararı** olarak muhasebeleştirir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (rücusuz faktoring; finansal tablo etkisi)",
            "legislationRef": "TFRS 9 Finansal Araçlar - finansal varlıkların bilanço dışı bırakılması",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-ticalacak-gen-0007": {
        "stem": "İşletme, sekiz ay sonra geri alınacak 30.000 ₺ kira depozitosu ile üç yıl sonra geri alınacak 80.000 ₺ teminat vermiştir. Tekdüzen Hesap Planı'na göre bu tutarlar sırasıyla hangi hesaplarda izlenir?",
        "options": {
            "A": "120 Alıcılar ve 220 Alıcılar",
            "B": "126 Verilen Depozito ve Teminatlar ve 126 Verilen Depozito ve Teminatlar",
            "C": "226 Verilen Depozito ve Teminatlar ve 126 Verilen Depozito ve Teminatlar",
            "D": "126 Verilen Depozito ve Teminatlar ve 226 Verilen Depozito ve Teminatlar",
            "E": "136 Diğer Çeşitli Alacaklar ve 236 Diğer Çeşitli Alacaklar",
        },
        "answer": "D",
        "solution": "Bir yıl içinde geri alınacak depozito **126 Verilen Depozito ve Teminatlar** hesabında dönen varlık; bir yıldan uzun vadeli olan ise **226 Verilen Depozito ve Teminatlar** hesabında duran varlık olarak izlenir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (depozito; vade sınıflaması)",
            "legislationRef": "1 Sıra No'lu MSUGT - 126 ve 226 Verilen Depozito ve Teminatlar",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-ticalacak-gen-0011": {
        "stem": "TFRS 9 kapsamında ticari alacaklar için kullanılan karşılık matrisinde; vadesi geçmemiş 200.000 ₺ alacağa %2, 1-90 gün gecikmiş 100.000 ₺ alacağa %8 ve 90 günden fazla gecikmiş 50.000 ₺ alacağa %30 beklenen kayıp oranı uygulanmaktadır. Toplam beklenen kredi zararı kaç ₺'dir?",
        "options": {
            "A": "27.000 ₺",
            "B": "23.000 ₺",
            "C": "19.000 ₺",
            "D": "31.000 ₺",
            "E": "35.000 ₺",
        },
        "answer": "A",
        "solution": "Beklenen kredi zararı; 200.000 × %2 = 4.000 ₺, 100.000 × %8 = 8.000 ₺ ve 50.000 × %30 = 15.000 ₺ olmak üzere toplam **27.000 ₺**dir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (ticari alacak yaşlandırması; hesaplama)",
            "legislationRef": "TFRS 9 Finansal Araçlar, par. 5.5.15-5.5.17",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-ticalacak-gen-0014": {
        "stem": "İşletme 1 Ekim'de, nominal değeri 120.000 ₺ olan ve yıllık %30 faiz taşıyan bir alacak senedi almıştır. Senedin anaparası ve faizi altı ay sonra birlikte tahsil edilecektir. 31 Aralık'ta üç aylık döneme ait tahakkuk etmiş faiz geliri kaç ₺'dir?",
        "options": {
            "A": "36.000 ₺",
            "B": "18.000 ₺",
            "C": "12.000 ₺",
            "D": "9.000 ₺",
            "E": "3.000 ₺",
        },
        "answer": "D",
        "solution": "Üç aylık faiz 120.000 × %30 × 3/12 = **9.000 ₺**dir. Dönemsellik gereği bu tutar 31 Aralık'ta faiz geliri olarak tahakkuk ettirilir; kalan üç aylık faiz izleyen döneme aittir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (faizli alacak senedi; tahakkuk)",
            "legislationRef": "Dönemsellik Kavramı; 1 Sıra No'lu MSUGT - 181 Gelir Tahakkukları ve 642 Faiz Gelirleri",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-ticalacak-gen-0017": {
        "stem": "İşletme 100.000 ₺ tutarındaki ticari alacağını 92.000 ₺ karşılığında faktöre devretmiştir. Sözleşmeye göre borçlu ödemezse faktör tutarın tamamını işletmeden isteyebilecektir; dolayısıyla başlıca kredi riski işletmede kalmaktadır. TFRS 9'a göre en uygun değerlendirme hangisidir?",
        "options": {
            "A": "Alacak tamamen bilanço dışı bırakılır ve 8.000 ₺ satış geliri yazılır.",
            "B": "Alacak bilanço dışı bırakılmaz; alınan tutar teminatlı finansman yükümlülüğü olarak değerlendirilir.",
            "C": "Alacak değersiz sayılarak tamamı gider yazılır.",
            "D": "Alacağın yalnız 92.000 ₺'lik kısmı bilançodan çıkarılır, kalan 8.000 ₺ stok hesabına alınır.",
            "E": "Faktoring sözleşmesi hiçbir finansal tablo kaydı doğurmaz.",
        },
        "answer": "B",
        "solution": "Rüculu faktoringde borçlunun ödememe riski önemli ölçüde işletmede kalıyorsa alacak bilanço dışı bırakılmaz. Faktörden alınan **92.000 ₺**, alacak teminat gösterilerek sağlanan bir finansman olarak ve buna karşılık bir yükümlülükle muhasebeleştirilir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (rüculu faktoring; risk değerlendirmesi)",
            "legislationRef": "TFRS 9 Finansal Araçlar - finansal varlıkların bilanço dışı bırakılması",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-ticalacak-gen-0023": {
        "stem": "TFRS 9'a göre beklenen kredi zararının ölçümünde aşağıdakilerden hangisi birlikte dikkate alınır?",
        "options": {
            "A": "Yalnız geçmişte gerçekleşen kesin zararlar; mevcut ve gelecekteki koşullar dikkate alınmaz.",
            "B": "Yalnız yönetimin en iyimser tahmini; paranın zaman değeri dikkate alınmaz.",
            "C": "Yalnız dava veya icra safhasına ulaşmış alacaklar; diğer olası kayıplar dışlanır.",
            "D": "Olasılıklara göre ağırlıklandırılmış tarafsız tutar, paranın zaman değeri ve makul şekilde desteklenebilir ileriye yönelik bilgi",
            "E": "Alacağın nominal tutarı ile işletmenin dönem kârı arasındaki fark",
        },
        "answer": "D",
        "solution": "Beklenen kredi zararı; mümkün sonuçları yansıtan **olasılık ağırlıklı ve tarafsız tutarı**, **paranın zaman değerini** ve geçmiş olaylarla mevcut şartların yanında makul ve desteklenebilir **ileriye yönelik bilgiyi** içerir. Yalnız gerçekleşmiş zarar veya dava şartı aranmaz.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (beklenen kredi zararı; ölçüm ilkeleri)",
            "legislationRef": "TFRS 9 Finansal Araçlar, par. 5.5.17",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-ticalacak-gen-0026": {
        "stem": "VUK'a göre vadesi gelmemiş bir alacak senedinin reeskontunda kullanılacak faiz oranıyla ilgili aşağıdaki ifadelerden hangisi doğrudur?",
        "options": {
            "A": "Senette oran yazsa bile her durumda işletmenin banka kredi faizi kullanılır.",
            "B": "Her durumda alacaklının serbestçe belirlediği oran kullanılır.",
            "C": "Faiz oranı bulunmayan senetlere reeskont uygulanamaz.",
            "D": "Senette yazılı oran dikkate alınmaz; yalnız enflasyon oranı kullanılır.",
            "E": "Senette faiz oranı açıklanmışsa bu oran, açıklanmamışsa Türkiye Cumhuriyet Merkez Bankasının resmî iskonto oranı kullanılır.",
        },
        "answer": "E",
        "solution": "VUK 281 uyarınca senette faiz oranı açıklanmışsa **senetteki oran** esas alınır. Oran açıklanmamışsa değerleme gününde geçerli **TCMB resmî iskonto oranı** kullanılır.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (VUK reeskont oranı; kural uygulama)",
            "legislationRef": "213 sayılı VUK md. 281",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-ticalacak-gen-0027": {
        "stem": "VUK 323'teki diğer koşulların oluştuğu 180.000 ₺ tutarındaki ticari alacağın 120.000 ₺'lik kısmı tahsil kabiliyeti bulunan ipotekle güvence altındadır. Buna göre ayrılabilecek azami şüpheli alacak karşılığı kaç ₺'dir?",
        "options": {
            "A": "180.000 ₺",
            "B": "120.000 ₺",
            "C": "60.000 ₺",
            "D": "300.000 ₺",
            "E": "Karşılık ayrılamaz",
        },
        "answer": "C",
        "solution": "Teminatlı alacaklarda şüpheli alacak karşılığı yalnız teminatla karşılanmayan kısım için ayrılır. Açık kısım 180.000 − 120.000 = **60.000 ₺**dir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (teminatlı şüpheli alacak; hesaplama)",
            "legislationRef": "213 sayılı VUK md. 323",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-ticalacak-gen-0032": {
        "stem": "Tamamı için karşılık ayrılmış 24.000 ₺ tutarındaki şüpheli ticari alacağın 9.000 ₺'si banka yoluyla tahsil edilmiştir. Kalan alacağın şüpheli niteliği sürmektedir. Tahsilat ve karşılık bakımından en uygun işlem hangisidir?",
        "options": {
            "A": "Karşılığın tamamı 24.000 ₺ gelir yazılarak iptal edilir; 128 hesabı değiştirilmez.",
            "B": "Yalnız 102 Bankalar borçlandırılır; 128 ve 129 hesapları değiştirilmez.",
            "C": "Kalan 15.000 ₺ de tahsil edilmiş sayılarak bütün hesaplar kapatılır.",
            "D": "Tahsil edilen 9.000 ₺ için yeniden 654 Karşılık Giderleri borçlandırılır.",
            "E": "102/128 kaydıyla 9.000 ₺ alacak kapatılır; aynı tutardaki karşılık 129/644 kaydıyla iptal edilir, kalan 15.000 ₺ 128 ve 129'da izlenir.",
        },
        "answer": "E",
        "solution": "Tahsil edilen bölüm için **102 Bankalar (B) 9.000 / 128 Şüpheli Ticari Alacaklar (A) 9.000** kaydı yapılır. Bu bölüme ait karşılık da **129 (B) 9.000 / 644 (A) 9.000** ile iptal edilir. Tahsil edilmeyen ve şüpheli niteliği süren 15.000 ₺ hem 128 hem 129 hesaplarında kalır.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (şüpheli alacak; kısmi tahsilat)",
            "legislationRef": "1 Sıra No'lu MSUGT - 128, 129 ve 644 hesaplarının işleyişi",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-ticalacak-gen-0039": {
        "stem": "TFRS 9'un basitleştirilmiş yaklaşımını önemli finansman bileşeni içermeyen ticari alacaklarına uygulayan bir işletme, zarar karşılığını hangi tutarda ölçer?",
        "options": {
            "A": "Yalnız dava açılmış alacakların nominal tutarında",
            "B": "Her durumda ticari alacakların tamamı kadar",
            "C": "Yalnız raporlama tarihinden sonraki bir ayda gerçekleşmesi beklenen zararda",
            "D": "Sadece vergi mevzuatınca gider kabul edilen tutarda",
            "E": "İlk finansal tablolara almadan itibaren ömür boyu beklenen kredi zararlarına eşit tutarda",
        },
        "answer": "E",
        "solution": "Basitleştirilmiş yaklaşımda önemli finansman bileşeni içermeyen ticari alacakların zarar karşılığı, kredi riskindeki artış ayrıca izlenmeden **her zaman ömür boyu beklenen kredi zararına** eşit tutarda ölçülür.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (TFRS 9; basitleştirilmiş yaklaşım)",
            "legislationRef": "TFRS 9 Finansal Araçlar, par. 5.5.15",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-ticalacak-gen-0040": {
        "stem": "Bir işletmenin 400.000 ₺ tutarındaki benzer riskli ticari alacakları için geçmiş kayıp oranı %3'tür. Raporlama tarihinde gelecekteki ekonomik koşullara ilişkin makul ve desteklenebilir bilgiler, bu oranın %25 artırılmasını gerektirmektedir. Başka düzeltme olmadığına göre beklenen kredi zararı kaç ₺'dir?",
        "options": {
            "A": "3.000 ₺",
            "B": "12.000 ₺",
            "C": "13.000 ₺",
            "D": "15.000 ₺",
            "E": "100.000 ₺",
        },
        "answer": "D",
        "solution": "İleriye yönelik düzeltilmiş kayıp oranı %3 × 1,25 = **%3,75**tir. Beklenen kredi zararı 400.000 × %3,75 = **15.000 ₺** olarak hesaplanır. TFRS 9 yalnız geçmiş veriyi değil, desteklenebilir ileriye yönelik bilgiyi de dikkate alır.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (beklenen kredi zararı; ileriye yönelik düzeltme)",
            "legislationRef": "TFRS 9 Finansal Araçlar, par. 5.5.17",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-ticalacak-gen-0054": {
        "stem": "Ticari alacaklarda tahsilat riskini azaltmaya yönelik en uygun iç kontrol bileşimi hangisidir?",
        "options": {
            "A": "Satış temsilcisinin kredi limiti belirleme, sevkiyat ve tahsilat kayıtlarını tek başına yürütmesi",
            "B": "Vadesi geçen alacakların yaşlandırma raporundan çıkarılması",
            "C": "Müşteri limitlerinin satış gerçekleştikten sonra belgesiz biçimde artırılması",
            "D": "Alacak mutabakatlarının yalnız kaydı yapan personelce hazırlanması ve farkların araştırılmaması",
            "E": "Kredi onayının satıştan ayrılması, müşteri limitlerinin sistemde izlenmesi, yaşlandırma raporlarının incelenmesi ve hesap ekstrelerinin müşterilere gönderilmesi",
        },
        "answer": "E",
        "solution": "Kredi onayının satış işlevinden ayrılması, tanımlı limitlerin sistemce izlenmesi, gecikmelerin yaşlandırma raporuyla takip edilmesi ve müşteri mutabakatı; hem yetkisiz satış hem de tahsil edilememe riskini azaltan birbirini tamamlayıcı kontrollerdir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (ticari alacaklar; iç kontrol senaryosu)",
            "legislationRef": "Muhasebe Bilgi Sistemleri - satış ve alacak döngüsü kontrolleri",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-ticalacak-gen-0056": {
        "stem": "Vadesi gelen 60.000 ₺ nominal değerli alacak senedi, borçluyla yapılan anlaşma sonucu 6.000 ₺ vade farkı eklenerek yeni bir senetle değiştirilmiştir. Yeni senedin nominal değeri ve yenileme tarihinde muhasebeleştirilecek finansman geliri sırasıyla kaç ₺'dir?",
        "options": {
            "A": "60.000 ₺ ve 0 ₺",
            "B": "60.000 ₺ ve 6.000 ₺",
            "C": "66.000 ₺ ve 6.000 ₺",
            "D": "66.000 ₺ ve 60.000 ₺",
            "E": "54.000 ₺ ve 6.000 ₺",
        },
        "answer": "C",
        "solution": "Eski 60.000 ₺ senet kapatılır; anapara ile 6.000 ₺ finansman gelirini içeren **66.000 ₺ nominal değerli yeni senet** alınır. Kayıt özünde yeni 121 (B) 66.000 / eski 121 (A) 60.000 + ilgili finansman geliri (A) 6.000 şeklindedir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (senet yenileme; vade farkı)",
            "legislationRef": "1 Sıra No'lu MSUGT - 121 Alacak Senetleri ve finansman gelirleri",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
}


SECURITIES_PATCHES = {
    "finmuh-menkul-gen-0004": {
        "stem": "Bir işletme, sözleşmeye bağlı nakit akışlarını tahsil etmek amacıyla elde tuttuğu bir borçlanma aracının yalnız belirli tarihlerde anapara ve anapara bakiyesine ilişkin faiz ödemeleri doğurduğunu belirlemiştir. TFRS 9'a göre bu finansal varlığın sonraki ölçüm sınıfı hangisidir?",
        "options": {
            "A": "İtfa edilmiş maliyet",
            "B": "Her durumda gerçeğe uygun değer farkı kâr veya zarara yansıtılan",
            "C": "Stok maliyeti",
            "D": "Maddi duran varlık maliyeti",
            "E": "Yalnız nominal değer",
        },
        "answer": "A",
        "solution": "Borçlanma aracı **sözleşmeye bağlı nakit akışlarını tahsil etme** iş modeli kapsamında tutuluyor ve nakit akışları yalnız **anapara ve faizden** oluşuyorsa TFRS 9 uyarınca **itfa edilmiş maliyetle** ölçülür.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (TFRS 9; sınıflandırma senaryosu)",
            "legislationRef": "TFRS 9 Finansal Araçlar, par. 4.1.2",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-menkul-gen-0005": {
        "stem": "İşletmenin VUK kayıtlarında 2.000.000 ₺ değerle izlenen 1 kilogram külçe altının değerleme günündeki kıymetli madenler borsası rayici 2.300.000 ₺'dir. VUK 274/A'ya göre dönem sonu değeri ve değerleme farkı sırasıyla kaç ₺'dir?",
        "options": {
            "A": "2.000.000 ₺ ve 0 ₺",
            "B": "2.000.000 ₺ ve 300.000 ₺ zarar",
            "C": "2.300.000 ₺ ve 300.000 ₺ gelir",
            "D": "2.300.000 ₺ ve 2.300.000 ₺ gelir",
            "E": "300.000 ₺ ve 2.000.000 ₺ gelir",
        },
        "answer": "C",
        "solution": "VUK 274/A uyarınca altın borsa rayiciyle değerlenir. Dönem sonu değer **2.300.000 ₺**, kayıtlı değere göre olumlu fark 2.300.000 − 2.000.000 = **300.000 ₺ gelir**dir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (VUK 274/A; güncel sayısal uygulama)",
            "legislationRef": "213 sayılı VUK md. 274/A (7524 sayılı Kanun, yürürlük 02.08.2024)",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-menkul-gen-0006": {
        "stem": "İşletmenin maliyeti 500.000 ₺ olan platin mevcudu için değerleme gününde güvenilir bir kıymetli madenler borsası rayici bulunmamaktadır. VUK 274/A'ya göre hangi değer esas alınır?",
        "options": {
            "A": "Her durumda nominal değer",
            "B": "500.000 ₺ maliyet bedeli",
            "C": "İşletme yönetiminin belirlediği tahmini satış değeri",
            "D": "Tasfiye değeri",
            "E": "Sıfır değer",
        },
        "answer": "B",
        "solution": "VUK 274/A'ya göre kıymetli maden borsa rayiciyle değerlenir; borsa rayici yoksa veya muvazaalı oluşmuşsa **maliyet bedeli** esas alınır. Bu nedenle değer **500.000 ₺**dir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (VUK 274/A; borsa rayici istisnası)",
            "legislationRef": "213 sayılı VUK md. 274/A",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-menkul-gen-0015": {
        "stem": "İşletmenin 100 gram altın cinsinden senetsiz alacağı kayıtlarda 300.000 ₺'dir. Değerleme gününde altının borsa rayici gram başına 3.200 ₺'dir. VUK 274/A'ya göre alacağın dönem sonu değeri ve olumlu değerleme farkı sırasıyla kaç ₺'dir?",
        "options": {
            "A": "320.000 ₺ ve 20.000 ₺",
            "B": "300.000 ₺ ve 0 ₺",
            "C": "320.000 ₺ ve 320.000 ₺",
            "D": "20.000 ₺ ve 300.000 ₺",
            "E": "280.000 ₺ ve 20.000 ₺",
        },
        "answer": "A",
        "solution": "VUK 274/A, kıymetli maden cinsinden senetli ve senetsiz alacaklara da uygulanır. Değer 100 × 3.200 = **320.000 ₺**, olumlu fark 320.000 − 300.000 = **20.000 ₺**dir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (kıymetli maden alacağı; hesaplama)",
            "legislationRef": "213 sayılı VUK md. 274/A",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-menkul-gen-0019": {
        "stem": "İşletme bir yıl sonra 100.000 ₺ tahsil edeceği kuponsuz tahvili 90.000 ₺'ye edinmiş ve itfa edilmiş maliyetle sınıflandırmıştır. Başka nakit akışı bulunmadığına göre bir yıllık toplam etkin faiz geliri ve vade sonundaki defter değeri sırasıyla kaç ₺'dir?",
        "options": {
            "A": "90.000 ₺ ve 100.000 ₺",
            "B": "10.000 ₺ ve 90.000 ₺",
            "C": "100.000 ₺ ve 100.000 ₺",
            "D": "10.000 ₺ ve 100.000 ₺",
            "E": "10.000 ₺ ve 110.000 ₺",
        },
        "answer": "D",
        "solution": "Kuponsuz tahvilin 90.000 ₺ ilk değeri ile 100.000 ₺ vade tutarı arasındaki **10.000 ₺ iskonto**, etkin faiz yöntemiyle faiz geliri olur. Bir yıl sonunda defter değeri 90.000 + 10.000 = **100.000 ₺**ye ulaşır.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (etkin faiz; kuponsuz tahvil)",
            "legislationRef": "TFRS 9 Finansal Araçlar, par. 5.4.1",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-menkul-gen-0024": {
        "stem": "İşletme, gerçeğe uygun değer farkı kâr veya zarara yansıtılan bir finansal varlığı 100.000 ₺ gerçeğe uygun değerle edinmiş ve ayrıca 2.000 ₺ işlem komisyonu ödemiştir. TFRS 9'a göre varlığın ilk defter değeri ve komisyonun muhasebeleştirilmesi hangisidir?",
        "options": {
            "A": "102.000 ₺; komisyon varlığın maliyetine eklenir.",
            "B": "100.000 ₺; 2.000 ₺ komisyon doğrudan gider yazılır.",
            "C": "98.000 ₺; komisyon varlıktan düşülür.",
            "D": "2.000 ₺; yalnız komisyon aktifleştirilir.",
            "E": "100.000 ₺; komisyon hiçbir kayda alınmaz.",
        },
        "answer": "B",
        "solution": "Gerçeğe uygun değer farkı kâr veya zarara yansıtılan finansal varlık ilk olarak **100.000 ₺ gerçeğe uygun değerle** ölçülür; bu sınıftaki varlığa ilişkin **2.000 ₺ işlem maliyeti doğrudan gider** yazılır.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (TFRS 9; işlem maliyeti)",
            "legislationRef": "TFRS 9 Finansal Araçlar, par. 5.1.1",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-menkul-gen-0025": {
        "stem": "İşletme, itfa edilmiş maliyetle ölçülecek bir borçlanma aracını 100.000 ₺ gerçeğe uygun değerle edinmiş ve doğrudan ilişkilendirilebilen 2.000 ₺ işlem maliyetine katlanmıştır. TFRS 9'a göre ilk defter değeri kaç ₺'dir?",
        "options": {
            "A": "98.000 ₺",
            "B": "100.000 ₺",
            "C": "102.000 ₺",
            "D": "2.000 ₺",
            "E": "104.000 ₺",
        },
        "answer": "C",
        "solution": "Gerçeğe uygun değer farkı kâr veya zarara yansıtılmayan finansal varlıklarda doğrudan işlem maliyetleri ilk değere eklenir. İlk defter değeri 100.000 + 2.000 = **102.000 ₺**dir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (itfa edilmiş maliyet; işlem maliyeti)",
            "legislationRef": "TFRS 9 Finansal Araçlar, par. 5.1.1",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-menkul-gen-0027": {
        "stem": "Bir borçlanma aracı, sözleşmeye bağlı nakit akışlarını hem tahsil etmeyi hem de uygun olduğunda aracı satmayı amaçlayan iş modeli kapsamında yönetilmektedir. Nakit akışları yalnız anapara ve faiz ödemeleridir. TFRS 9'a göre sonraki ölçüm sınıfı hangisidir?",
        "options": {
            "A": "Yalnız maliyet bedeli",
            "B": "Gerçeğe uygun değer farkı diğer kapsamlı gelire yansıtılan",
            "C": "Stok olarak net gerçekleşebilir değer",
            "D": "Maddi duran varlık olarak yeniden değerlenmiş tutar",
            "E": "Her durumda nominal değer",
        },
        "answer": "B",
        "solution": "İş modeli hem sözleşmeye bağlı nakit akışlarını **tahsil etmeyi hem satmayı** amaçlıyor ve nakit akışları yalnız anapara ile faizden oluşuyorsa borçlanma aracı **gerçeğe uygun değer farkı diğer kapsamlı gelire yansıtılarak** ölçülür.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (TFRS 9; tahsil et ve sat modeli)",
            "legislationRef": "TFRS 9 Finansal Araçlar, par. 4.1.2A",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-menkul-gen-0028": {
        "stem": "İşletme, alım satım amacıyla elde tutulmayan bir özkaynak aracını ilk defa finansal tablolara alırken gerçeğe uygun değer değişimlerini diğer kapsamlı gelire sunma yönünde geri dönülemez seçim yapmıştır. TFRS 9'a göre aşağıdakilerden hangisi doğrudur?",
        "options": {
            "A": "Araç bundan sonra maliyet bedelinde dondurulur.",
            "B": "Bütün temettüler doğrudan aracın maliyetinden düşülür.",
            "C": "Araç satıldığında birikmiş diğer kapsamlı gelir zorunlu olarak kâr veya zarara aktarılır.",
            "D": "Seçim her raporlama döneminde serbestçe değiştirilebilir.",
            "E": "Gerçeğe uygun değer değişimleri diğer kapsamlı gelirde kalır; satışta kâr veya zarara yeniden sınıflandırılmaz.",
        },
        "answer": "E",
        "solution": "Alım satım amacıyla tutulmayan özkaynak aracında ilk kayıtta yapılan seçim **geri dönülemez**. Gerçeğe uygun değer değişimleri diğer kapsamlı gelirde sunulur ve araç elden çıkarıldığında birikmiş tutar **kâr veya zarara yeniden sınıflandırılmaz**.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (özkaynak aracı; diğer kapsamlı gelir seçimi)",
            "legislationRef": "TFRS 9 Finansal Araçlar, par. 5.7.5-5.7.6",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-menkul-gen-0032": {
        "stem": "TFRS 9'daki 'yalnız anapara ve faiz ödemeleri' testinde faiz unsuru esas olarak aşağıdakilerden hangilerini karşılar?",
        "options": {
            "A": "Paranın zaman değeri, kredi riski, diğer temel borç verme risk ve maliyetleri ile kâr marjı",
            "B": "Borçlunun hisse fiyatındaki sınırsız artış ve emtia fiyatı riski",
            "C": "Yalnız ihraççının dönem kârından dağıtacağı temettü",
            "D": "Sadece aracın nominal değerindeki değişim",
            "E": "Alacaklının stok satışlarından elde edeceği brüt kâr",
        },
        "answer": "A",
        "solution": "Anapara bakiyesine ilişkin faiz; **paranın zaman değerini**, kredi riskini, diğer temel borç verme risk ve maliyetlerini ve bir kâr marjını karşılar. Hisse veya emtia fiyatına endeksli sınırsız getiri bu yapıyla uyumlu değildir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (TFRS 9; SPPI testi)",
            "legislationRef": "TFRS 9 Finansal Araçlar, par. 4.1.3",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-menkul-gen-0033": {
        "stem": "İşletme, 1 Temmuz'da vadesinde 100.000 ₺ ödenecek kuponsuz devlet bonosunu 90.000 ₺'ye almıştır. Vade 30 Haziran izleyen yıldır ve doğrusal kıst getiri varsayılacaktır. Borsa rayici bulunmadığına göre VUK 279 uyarınca 31 Aralık değerleme tutarı kaç ₺'dir?",
        "options": {
            "A": "90.000 ₺",
            "B": "95.000 ₺",
            "C": "100.000 ₺",
            "D": "105.000 ₺",
            "E": "110.000 ₺",
        },
        "answer": "B",
        "solution": "Toplam 10.000 ₺ getiri on iki aylık süreye aittir. İlk altı aya düşen kıst getiri 10.000 × 6/12 = **5.000 ₺**dir. Değerleme tutarı 90.000 + 5.000 = **95.000 ₺** olur.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (VUK 279; kıst getiri hesabı)",
            "legislationRef": "213 sayılı VUK md. 279",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-menkul-gen-0039": {
        "stem": "Gerçeğe uygun değer farkı kâr veya zarara yansıtılan bir finansal yatırımın dönem başı defter değeri 200.000 ₺, dönem sonu gerçeğe uygun değeri 225.000 ₺'dir. Dönem içinde alım, satım veya nakit getiri yoktur. TFRS 9'a göre dönem sonu değerleme kazancı kaç ₺'dir ve nerede raporlanır?",
        "options": {
            "A": "25.000 ₺; kâr veya zararda",
            "B": "25.000 ₺; yalnız özkaynakta, kâr veya zarara hiç yansımadan",
            "C": "225.000 ₺; satış hasılatında",
            "D": "200.000 ₺; finansman giderinde",
            "E": "Kazanç kaydedilmez.",
        },
        "answer": "A",
        "solution": "Gerçeğe uygun değer artışı 225.000 − 200.000 = **25.000 ₺**dir. Araç gerçeğe uygun değer farkı kâr veya zarara yansıtılan sınıfta olduğundan kazanç **dönem kâr veya zararında** muhasebeleştirilir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (TFRS 9; gerçeğe uygun değer kazancı)",
            "legislationRef": "TFRS 9 Finansal Araçlar, par. 5.7.1",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-menkul-gen-0041": {
        "stem": "İşletmenin 100 gram gümüş cinsinden mevduatı vardır. Değerleme gününe kadar 5 gram gümüş faiz tahakkuk etmiş, gümüşün borsa rayici gram başına 30 ₺ olmuştur. VUK 274/A'ya göre faiz dâhil mevduatın değerleme tutarı kaç ₺'dir?",
        "options": {
            "A": "150 ₺",
            "B": "3.000 ₺",
            "C": "3.100 ₺",
            "D": "3.150 ₺",
            "E": "3.500 ₺",
        },
        "answer": "D",
        "solution": "Kıymetli maden mevduatları değerleme gününe kadar hesaplanan faizleriyle birlikte dikkate alınır. Toplam 100 + 5 = **105 gram**, değer 105 × 30 = **3.150 ₺**dir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (kıymetli maden mevduatı; faiz dâhil değerleme)",
            "legislationRef": "213 sayılı VUK md. 274/A",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-menkul-gen-0043": {
        "stem": "Alım satım amacıyla alınan borsaya kayıtlı bir pay senedinin alış bedeli 100.000 ₺, dönem sonu gerçeğe uygun değeri 130.000 ₺'dir. VUK 279 ile TFRS 9'un gerçeğe uygun değer farkı kâr veya zarara yansıtılan sınıfı karşılaştırıldığında dönem sonu değerleri hangisidir?",
        "options": {
            "A": "VUK 130.000 ₺; TFRS 100.000 ₺",
            "B": "Her iki çerçevede 100.000 ₺",
            "C": "Her iki çerçevede 130.000 ₺ ancak fark gelir yazılmaz.",
            "D": "VUK 30.000 ₺; TFRS 130.000 ₺",
            "E": "VUK 100.000 ₺; TFRS 130.000 ₺ ve TFRS'de 30.000 ₺ değerleme kazancı",
        },
        "answer": "E",
        "solution": "VUK 279 uyarınca pay senedi **alış bedeli 100.000 ₺** ile kalır. TFRS 9'da alım satım amaçlı pay senedi gerçeğe uygun değer farkı kâr veya zarara yansıtılan sınıftadır; **130.000 ₺** ölçülür ve **30.000 ₺ kazanç** kâr veya zarara alınır.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (VUK/TFRS karşılaştırması; pay senedi)",
            "legislationRef": "213 sayılı VUK md. 279; TFRS 9 par. 5.7.1",
        },
        "validYear": 2026,
        "mockExamId": None,
    },
    "finmuh-menkul-gen-0052": {
        "stem": "VUK 279'a göre işletmenin elindeki pay senetlerinin dönem sonu borsa değerinin alış bedelinin üzerine çıkması durumunda vergi değerlemesinde ne yapılır?",
        "solution": "VUK 279 uyarınca pay senetleri **alış bedeliyle** değerlenir. Bu nedenle dönem sonundaki gerçekleşmemiş borsa değeri artışı vergi değerlemesinde gelir yazılmaz; fark, satış gerçekleşirse satış kazancı olarak ortaya çıkar. TFRS 9 kapsamındaki gerçeğe uygun değer uygulaması ayrı bir finansal raporlama çerçevesidir.",
        "source": {
            "kind": "generated",
            "styleRef": "SGS Finansal Muhasebe (VUK pay senedi değerlemesi; çerçeve ayrımı)",
            "legislationRef": "213 sayılı VUK md. 279",
        },
    },
}


PPE_PATCHES = {
    "finmuh-mdv-gen-0008": ppe_patch(
        "İşletme, aynı üretim hattında birlikte çalışacak beş adet cihazı 2026 yılında ayrı ayrı KDV hariç 3.000 ₺'ye satın almıştır. Cihazlar iktisadi ve teknik bakımdan bir bütün oluşturduğuna göre VUK 313'teki 12.000 ₺ doğrudan gider yazma sınırı bakımından nasıl işlem yapılır?",
        {
            "A": "Her cihaz ayrı değerlendirildiğinden 15.000 ₺'nin tamamı doğrudan gider yazılır.",
            "B": "Yalnız ilk dört cihaz doğrudan gider yazılır, beşinci cihaz amortismana tabi tutulur.",
            "C": "Toplam 15.000 ₺ sınırı aştığından cihazlar topluca amortismana tabi tutulur.",
            "D": "Sınır KDV dâhil 20.000 ₺ olduğundan doğrudan gider yazılır.",
            "E": "Teknik bütünlük yalnız binalarda dikkate alındığından cihazlar kayda alınmaz.",
        },
        "C",
        "VUK 313 uyarınca iktisadi ve teknik bakımdan bütünlük arz eden kıymetlerde had **topluca** dikkate alınır. Beş cihazın toplam değeri 5 × 3.000 = **15.000 ₺** olup 2026 yılı için 12.000 ₺ sınırını aştığından doğrudan gider yazılamaz; amortismana tabi tutulur.",
        "213 sayılı VUK md. 313; 588 Sıra No.lu VUK Genel Tebliği (2026 haddi: 12.000 TL)",
    ),
    "finmuh-mdv-gen-0009": ppe_patch(
        "TMS 16'ya göre bir maddi duran varlık kaleminin finansal tablolara alınabilmesi için aşağıdaki koşullardan hangilerinin birlikte sağlanması gerekir?",
        {
            "A": "Yalnız varlığın fiziken işletmeye teslim edilmiş olması",
            "B": "Varlığın bedelinin tamamen nakden ödenmiş olması ve hiç borç kalmaması",
            "C": "Varlığın mutlaka işletme tarafından üretilmiş olması",
            "D": "Varlığın piyasa fiyatının her gün yayımlanması ve satılmasının planlanması",
            "E": "Gelecekteki ekonomik yararların işletmeye aktarılmasının muhtemel olması ve maliyetin güvenilir ölçülebilmesi",
        },
        "E",
        "TMS 16'ya göre bir maddi duran varlık; ilgili gelecekteki ekonomik yararların işletmeye aktarılmasının **muhtemel olması** ve maliyetinin **güvenilir biçimde ölçülebilmesi** koşulları birlikte sağlandığında finansal tablolara alınır.",
        "TMS 16 Maddi Duran Varlıklar, par. 7",
    ),
    "finmuh-mdv-gen-0013": ppe_patch(
        "TMS 16 uygulayan işletme, maliyeti 150.000 ₺ ve tahmini kalıntı değeri 10.000 ₺ olan makineyi 5 yıl yararlı ömürle doğrusal amortismana tabi tutacaktır. Yıllık amortisman tutarı kaç ₺'dir?",
        {
            "A": "10.000",
            "B": "15.000",
            "C": "25.000",
            "D": "30.000",
            "E": "28.000",
        },
        "E",
        "Amortismana tabi tutar = Maliyet − Kalıntı değer = 150.000 − 10.000 = **140.000 ₺**. Doğrusal yöntemde yıllık amortisman 140.000 ÷ 5 = **28.000 ₺**dir.",
        "TMS 16, par. 6, 50 ve 53",
    ),
    "finmuh-mdv-gen-0014": ppe_patch(
        "Maliyeti 500.000 ₺, kalıntı değeri 20.000 ₺ ve toplam üretim kapasitesi 120.000 birim olan bir makineye TMS 16 kapsamında üretim miktarı yöntemi uygulanmaktadır. Dönemde 30.000 birim üretildiğine göre amortisman tutarı kaç ₺'dir?",
        {
            "A": "100.000",
            "B": "125.000",
            "C": "150.000",
            "D": "120.000",
            "E": "480.000",
        },
        "D",
        "Amortismana tabi tutar 500.000 − 20.000 = **480.000 ₺**dir. Dönemde kapasitenin 30.000/120.000 = %25'i kullanılmıştır. Amortisman 480.000 × %25 = **120.000 ₺** olur.",
        "TMS 16, par. 50 ve 62",
    ),
    "finmuh-mdv-gen-0016": ppe_patch(
        "Bir makinenin değer düşüklüğü öncesi defter değeri 100.000 ₺, TMS 36'ya göre belirlenen geri kazanılabilir tutarı 75.000 ₺'dir. Değer düşüklüğü zararı ve işlem sonrası defter değeri sırasıyla kaç ₺ olur?",
        {
            "A": "75.000; 25.000",
            "B": "100.000; 75.000",
            "C": "25.000; 100.000",
            "D": "25.000; 75.000",
            "E": "Zarar oluşmaz; 100.000",
        },
        "D",
        "Defter değeri geri kazanılabilir tutarı aştığında fark kadar değer düşüklüğü zararı doğar: 100.000 − 75.000 = **25.000 ₺**. Zarar sonrasında varlığın defter değeri **75.000 ₺** olur.",
        "TMS 16, par. 63; TMS 36 Varlıklarda Değer Düşüklüğü",
    ),
    "finmuh-mdv-gen-0019": ppe_patch(
        "Üretim tesisindeki bir makinenin dönem amortismanı, üretilen fakat henüz satılmamış mamullerle doğrudan ilgilidir. TMS 16 ve TMS 2'ye göre bu amortisman öncelikle nasıl muhasebeleştirilir?",
        {
            "A": "Daima finansman gideri olarak",
            "B": "Doğrudan geçmiş yıl zararlarına aktarılarak",
            "C": "Mamul stoklarının dönüştürme maliyetine dâhil edilerek",
            "D": "Makinenin maliyetinden doğrudan düşülerek",
            "E": "Satış gerçekleşene kadar hiç kaydedilmeyerek",
        },
        "C",
        "Bir varlığın ekonomik yararları başka bir varlığın üretiminde tüketiliyorsa amortisman o varlığın maliyetine dâhil edilir. Üretim makinesinin amortismanı, ilgili mamullerin **dönüştürme maliyetinin** bir unsurudur.",
        "TMS 16, par. 48-49; TMS 2 Stoklar",
    ),
    "finmuh-mdv-gen-0020": ppe_patch(
        "TMS 16'ya göre maddi duran varlıkların ilk muhasebeleştirmeden sonraki ölçümünde aşağıdaki politikalardan hangileri seçilebilir?",
        {
            "A": "Maliyet modeli veya yeniden değerleme modeli; seçilen politika ilgili varlık sınıfının tamamına uygulanır.",
            "B": "Yalnız nominal değer modeli",
            "C": "Her varlık için her yıl serbestçe değiştirilen piyasa modeli",
            "D": "Yalnız vergi değeri modeli",
            "E": "Sadece net gerçekleşebilir değer modeli",
        },
        "A",
        "TMS 16, muhasebe politikası olarak **maliyet modeli** ile **yeniden değerleme modeli** arasında seçim yapılmasına izin verir. Seçilen politika tek tek seçilmiş varlıklara değil, ilgili maddi duran varlık **sınıfının tamamına** uygulanır.",
        "TMS 16, par. 29-31 ve 36",
    ),
    "finmuh-mdv-gen-0021": ppe_patch(
        "İşletme 1 Ocak'ta 120.000 ₺'ye aldığı makineyi montaj tamamlandıktan sonra 1 Nisan'da yönetimin amaçladığı biçimde kullanıma hazır hâle getirmiştir. Kalıntı değer sıfır, yararlı ömür 5 yıldır. TMS 16'ya göre ilk yıl doğrusal amortisman tutarı kaç ₺'dir?",
        {
            "A": "24.000",
            "B": "18.000",
            "C": "12.000",
            "D": "9.000",
            "E": "Amortisman ayrılmaz.",
        },
        "B",
        "TMS 16'da amortisman satın alma tarihinde değil, varlık **kullanılabilir olduğunda** başlar. Yıllık amortisman 120.000 ÷ 5 = 24.000 ₺; 1 Nisan-31 Aralık arasındaki 9 ay için 24.000 × 9/12 = **18.000 ₺**dir.",
        "TMS 16, par. 55",
    ),
    "finmuh-mdv-gen-0024": ppe_patch(
        "Doğrusal amortisman uygulanan bir makine geçici olarak üretim dışında bırakılmış, ancak satış amaçlı elde tutulan varlık olarak sınıflandırılmamış ve tamamen itfa olmamıştır. TMS 16'ya göre aşağıdakilerden hangisi doğrudur?",
        {
            "A": "Makine atıl kaldığı gün finansal tablo dışı bırakılır.",
            "B": "Önceki dönem amortismanlarının tamamı iptal edilir.",
            "C": "Makine yeniden kullanılana kadar yararlı ömrü otomatik uzatılır.",
            "D": "Amortisman yalnız piyasa değeri düşerse ayrılır.",
            "E": "Geçici atıl kalma tek başına amortismanı durdurmaz.",
        },
        "E",
        "TMS 16'ya göre amortisman, varlık tamamen itfa olmadıkça yalnızca atıl kalması veya kullanımdan geçici çekilmesi nedeniyle durmaz. Üretim miktarı yöntemi kullanılıyorsa üretim olmayan dönemde tutar sıfır olabilir; soruda doğrusal yöntem uygulanmaktadır.",
        "TMS 16, par. 55",
    ),
    "finmuh-mdv-gen-0028": ppe_patch(
        "Bir makinenin önemli bir parçası yenilenmiştir. Yeni parçanın maliyeti 70.000 ₺, yenilenen eski parçanın defter değeri 40.000 ₺'dir ve eski parçadan tahsilat yoktur. TMS 16'ya göre işlemin etkisi hangisidir?",
        {
            "A": "Yeni parça gider yazılır, eski parça kayıtlarda bırakılır.",
            "B": "Yeni parça aktifleştirilir; eski parçanın 40.000 ₺ defter değeri finansal tablo dışı bırakılır.",
            "C": "Yalnız eski parçanın birikmiş amortismanı artırılır.",
            "D": "Yeni ve eski parçalar birlikte stok hesabına aktarılır.",
            "E": "Yenileme nedeniyle makinenin tamamı finansal tablo dışı bırakılır.",
        },
        "B",
        "Muhasebeleştirme koşulları sağlandığında yeni parçanın **70.000 ₺ maliyeti aktifleştirilir**. Yerine takılan eski parçanın **40.000 ₺ defter değeri** ise finansal tablo dışı bırakılır; tahsilat olmadığından bu tutar kayıp oluşturur.",
        "TMS 16, par. 13 ve 67-71",
    ),
    "finmuh-mdv-gen-0029": ppe_patch(
        "İşletme 500.000 ₺'ye aldığı bir tesisi kullanımı sonunda söküp alanı eski hâline getirmekle yükümlüdür. İlk kayıtta bu yükümlülüğün bugünkü değeri 60.000 ₺ olarak güvenilir biçimde ölçülmüştür. TMS 16'ya göre tesisin başlangıç maliyeti kaç ₺'dir?",
        {
            "A": "440.000",
            "B": "500.000",
            "C": "560.000",
            "D": "60.000",
            "E": "Yükümlülük yalnız ödeme tarihinde dikkate alınır.",
        },
        "C",
        "TMS 16'da sökme, taşıma ve alanı restore etme yükümlülüğünün başlangıçtaki tahmini maliyeti varlığın maliyetine dâhildir. Başlangıç maliyeti 500.000 + 60.000 = **560.000 ₺** olur; karşılığında bir yükümlülük muhasebeleştirilir.",
        "TMS 16, par. 16(c); TMS 37",
    ),
    "finmuh-mdv-gen-0031": ppe_patch(
        "İşletme, yeniden değerleme modelini makine sınıfına uygulamaktadır. Aynı sınıftaki on makineden yalnız piyasa değeri en çok artan iki makineyi yeniden değerlemek istemektedir. TMS 16'ya göre doğru işlem hangisidir?",
        {
            "A": "Yalnız iki makine yeniden değerlenir; diğerleri maliyette bırakılır.",
            "B": "Yeniden değerleme yalnız tamamen amorti edilmiş makinelerde yapılabilir.",
            "C": "Seçici değerleme yapılamaz; makine sınıfının tamamı yeniden değerlenir.",
            "D": "Değer artışı olan makineler stoklara aktarılır.",
            "E": "Yeniden değerleme modeli maddi duran varlıklarda hiçbir zaman kullanılamaz.",
        },
        "C",
        "Bir sınıf içinden yalnız değer artışı yüksek kalemleri seçmek finansal tabloları farklı tarihlere ait maliyet ve değerlerin karışımı hâline getirir. TMS 16'ya göre bir kalem yeniden değerlendiğinde ilgili **varlık sınıfının tamamı** yeniden değerlenir.",
        "TMS 16, par. 36 ve 38",
    ),
    "finmuh-mdv-gen-0034": ppe_patch(
        "İşletme, banka kredisiyle aldığı makineyi 2026 yılında envanterine kaydetmiştir. Kredi nedeniyle 2026 hesap döneminde 40.000 ₺, 2027 hesap döneminde 30.000 ₺ faiz oluşmuştur. VUK uygulamasında bu faizlerin maliyet veya gider olarak dikkate alınmasıyla ilgili doğru seçenek hangisidir?",
        {
            "A": "Her iki yılın faizi de zorunlu olarak doğrudan gider yazılır.",
            "B": "2026 faizi maliyete eklenir; 2027 faizi için doğrudan gider yazma veya maliyete ekleme seçeneği vardır.",
            "C": "Yalnız 2027 faizi maliyete eklenir, 2026 faizi kayda alınmaz.",
            "D": "Her iki yılın faizi de zorunlu olarak 257 Birikmiş Amortismanlar hesabına yazılır.",
            "E": "Faizler makinenin maliyetiyle hiçbir koşulda ilişkilendirilemez.",
        },
        "B",
        "Sabit kıymetin envantere alındığı hesap döneminin sonuna kadar oluşan kredi faizinin maliyete eklenmesi zorunludur; bu nedenle **2026 yılına ait 40.000 ₺ maliyete eklenir**. Sonraki dönem faizleri için mükellef, tercihini tutarlı uygulamak üzere doğrudan gider yazma veya maliyete ekleme yolunu seçebilir.",
        "213 sayılı VUK md. 262; 163 Sıra No.lu VUK Genel Tebliği",
    ),
    "finmuh-mdv-gen-0041": ppe_patch(
        "Daha önce yeniden değerleme azalışı bulunmayan bir binanın defter değeri, TMS 16 yeniden değerleme modeli kapsamında 800.000 ₺'den 950.000 ₺'ye çıkarılmıştır. 150.000 ₺ tutarındaki artış nasıl muhasebeleştirilir?",
        {
            "A": "Satış hasılatı olarak",
            "B": "Finansman geliri olarak",
            "C": "Binanın maliyetinden düşülerek",
            "D": "Tamamı geçmiş yıl zararlarına aktarılarak",
            "E": "Diğer kapsamlı gelirde ve özkaynakta yeniden değerleme artışı olarak",
        },
        "E",
        "Aynı varlıkla ilgili daha önce kâr veya zarara alınmış bir yeniden değerleme azalışı bulunmadığından 150.000 ₺ artış **diğer kapsamlı gelirde** muhasebeleştirilir ve özkaynakta **yeniden değerleme değer artışı** olarak birikir.",
        "TMS 16, par. 39",
    ),
    "finmuh-mdv-gen-0042": ppe_patch(
        "TMS 16 kapsamında ticari özü bulunan bir takas işleminde, verilen ve alınan varlığın gerçeğe uygun değerleri güvenilir biçimde ölçülebilmektedir. Alınan maddi duran varlığın maliyeti kural olarak hangi değerle ölçülür?",
        {
            "A": "Gerçeğe uygun değerle; ticari öz yoksa veya değer güvenilir ölçülemiyorsa verilen varlığın defter değeriyle",
            "B": "Yalnız alınan varlığın nominal değeriyle",
            "C": "Verilen varlığın ilk satın alma bedeliyle",
            "D": "Her durumda sıfır değerle",
            "E": "Yalnız vergi matrahıyla",
        },
        "A",
        "TMS 16'da ticari özü bulunan ve gerçeğe uygun değeri güvenilir ölçülebilen takaslarda alınan varlık **gerçeğe uygun değerle** ölçülür. İşlem ticari öz taşımıyorsa veya ne alınan ne verilen varlığın gerçeğe uygun değeri güvenilir ölçülebiliyorsa verilen varlığın defter değeri esas alınır.",
        "TMS 16, par. 24-26",
    ),
    "finmuh-mdv-gen-0043": ppe_patch(
        "TMS 16'ya göre aşağıdaki amortisman yöntemlerinden hangisi, varlığın ekonomik yararlarının tüketim biçimini genellikle yansıtmadığı için uygun kabul edilmez?",
        {
            "A": "Doğrusal amortisman yöntemi",
            "B": "Varlığın kullanıldığı faaliyetten elde edilen hasılata dayalı yöntem",
            "C": "Üretim miktarı yöntemi",
            "D": "Azalan bakiyeler yöntemi",
            "E": "Beklenen tüketim biçimini yansıtan sistematik yöntem",
        },
        "B",
        "Hasılat; satış fiyatı, diğer girdiler ve enflasyon gibi varlığın tüketiminden bağımsız unsurlardan etkilenir. Bu nedenle varlığın kullanımından elde edilen **hasılata dayalı amortisman yöntemi** TMS 16'ya göre uygun değildir.",
        "TMS 16, par. 62A",
    ),
    "finmuh-mdv-gen-0052": ppe_patch(
        "İşletme 400.000 ₺'ye aldığı makine için 30.000 ₺ montaj ve 20.000 ₺ çalışma testi maliyetine katlanmıştır. Test sırasında üretilen örneklerin satışından 8.000 ₺ gelir elde edilmiş, bu örneklerin maliyeti 5.000 ₺ olmuştur. TMS 16'ya göre makinenin maliyeti kaç ₺'dir?",
        {
            "A": "437.000",
            "B": "442.000",
            "C": "445.000",
            "D": "450.000",
            "E": "458.000",
        },
        "D",
        "Satın alma, montaj ve çalışma testi maliyetleri 400.000 + 30.000 + 20.000 = **450.000 ₺** olarak aktifleştirilir. Amaçlanan kullanım öncesinde üretilen örneklerden doğan **8.000 ₺ gelir ile 5.000 ₺ maliyet kâr veya zararda ayrı muhasebeleştirilir**; varlığın maliyetinden netleştirilmez.",
        "TMS 16, par. 17(e) ve 20A",
    ),
    "finmuh-mdv-gen-0054": ppe_patch(
        "Bir uçağın toplam maliyeti 10.000.000 ₺'dir. Maliyetin 4.000.000 ₺'lik motor kısmının yararlı ömrü 5 yıl, kalan gövde kısmının yararlı ömrü 10 yıldır; kalıntı değerler sıfırdır. TMS 16'ya göre yıllık toplam doğrusal amortisman kaç ₺'dir?",
        {
            "A": "600.000",
            "B": "800.000",
            "C": "1.000.000",
            "D": "2.000.000",
            "E": "1.400.000",
        },
        "E",
        "Önemli parçalar ayrı amortismana tabi tutulur. Motor: 4.000.000 ÷ 5 = **800.000 ₺**; gövde: 6.000.000 ÷ 10 = **600.000 ₺**. Toplam yıllık amortisman **1.400.000 ₺**dir.",
        "TMS 16, par. 43-44",
    ),
    "finmuh-mdv-gen-0055": ppe_patch(
        "Bir makinenin dönem başı defter değeri 120.000 ₺ ve kalıntı değeri sıfırdır. Yeni teknik bilgi nedeniyle kalan yararlı ömür 3 yıl olarak revize edilmiştir. TMS 16 ve TMS 8'e göre değişiklik nasıl uygulanır?",
        {
            "A": "Cari ve gelecek dönemlere ileriye yönelik uygulanır; cari yıl amortismanı 40.000 ₺ olur.",
            "B": "Geçmiş yılların tamamı geriye dönük düzeltilir; cari yıl amortisman ayrılmaz.",
            "C": "Yararlı ömür hiçbir koşulda değiştirilemez.",
            "D": "120.000 ₺'nin tamamı doğrudan gider yazılır.",
            "E": "Değişiklik yalnız dipnotta açıklanır, amortisman hesabını etkilemez.",
        },
        "A",
        "Yararlı ömür tahminindeki değişiklik bir muhasebe tahmini değişikliğidir ve **ileriye yönelik** uygulanır. Yeni yıllık amortisman 120.000 ÷ 3 = **40.000 ₺**dir; önceki dönemler geriye dönük değiştirilmez.",
        "TMS 16, par. 51; TMS 8",
    ),
    "finmuh-mdv-gen-0057": ppe_patch(
        "Bir kimya işletmesi, çevre mevzuatına uymadan üretime devam edemeyeceği için 300.000 ₺'lik arıtma tesisi kurmuştur. Tesis tek başına satışları artırmasa da diğer üretim varlıklarından ekonomik yarar elde edilmesini mümkün kılmaktadır. TMS 16'ya göre nasıl muhasebeleştirilir?",
        {
            "A": "Gelecekte yarar sağlamadığı kabul edilerek tamamı doğrudan gider yazılır.",
            "B": "Diğer varlıklardan yarar elde edilmesi için gerekli olduğundan maddi duran varlık olarak muhasebeleştirilir.",
            "C": "Yalnız nazım hesaplarda izlenir.",
            "D": "Çevresel amaçlı olduğu için stok hesabına alınır.",
            "E": "Ödeme tamamlanana kadar hiçbir kayıt yapılmaz.",
        },
        "B",
        "Güvenlik veya çevresel nedenlerle edinilen bir kıymet, doğrudan ek gelir yaratmasa bile işletmenin diğer varlıklarından ekonomik yarar elde etmesi için gerekli olabilir. Bu durumda arıtma tesisi **maddi duran varlık** olarak muhasebeleştirilir.",
        "TMS 16, par. 11",
    ),
    "finmuh-mdv-gen-0058": ppe_patch(
        "Bir uçağın faaliyetine devam edebilmesi için beş yılda bir büyük kontrol yapılması zorunludur. Yeni kontrolün maliyeti 90.000 ₺, önceki kontrolden kalan ve kayıtlarda ayrı izlenen defter değeri 20.000 ₺'dir. TMS 16'ya göre işlemin varlığın defter değerine net etkisi kaç ₺'dir?",
        {
            "A": "20.000 ₺ azalış",
            "B": "90.000 ₺ azalış",
            "C": "110.000 ₺ artış",
            "D": "70.000 ₺ artış",
            "E": "Etkisi yoktur.",
        },
        "D",
        "Muhasebeleştirme koşulları sağlandığında yeni büyük kontrol maliyeti **90.000 ₺ aktifleştirilir**; önceki kontrolün **20.000 ₺ defter değeri finansal tablo dışı bırakılır**. Net etki 90.000 − 20.000 = **70.000 ₺ artış**tır.",
        "TMS 16, par. 14",
    ),
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
            "E": "Sınırsız ömürlü varlık hiçbir zaman değer düşüklüğüne uğramaz.",
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
            "E": "Maddi olmayan duran varlıklar benzersiz kabul edildiğinden aktif piyasa bulunsa bile yeniden değerleme hiçbir koşulda mümkün değildir; bütün sınıf yalnız maliyet modelinde tutulur.",
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


PATCHES_BY_PATH = {
    RELATIVE_PATH: PATCHES,
    PROCESS_RELATIVE_PATH: PROCESS_PATCHES,
    READY_RELATIVE_PATH: READY_PATCHES,
    STOCK_RELATIVE_PATH: STOCK_PATCHES,
    RECEIVABLE_RELATIVE_PATH: RECEIVABLE_PATCHES,
    SECURITIES_RELATIVE_PATH: SECURITIES_PATCHES,
    PPE_RELATIVE_PATH: PPE_PATCHES,
    INTANGIBLE_RELATIVE_PATH: INTANGIBLE_PATCHES,
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
