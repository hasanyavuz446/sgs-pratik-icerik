#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TMS 40 Yatırım Amaçlı Gayrimenkuller — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Eylül standart turunun reçetesiyle baştan yazıldı (kalan iki paketten ikincisi, kör %31). Olay anlatan kök, kısa şık (terim/tutar). Kapsam: sınıflama (kısımların ayrı satılabilirliği, ek hizmetler, grup içi kiralama, kullanım hakkı varlığı, lojman, inşa hâlindeki gayrimenkul), ilk ölçüm (doğrudan giderler, vadeli alım, takas, bedelsiz edinim), sonraki ölçüm (gerçeğe uygun değer ve maliyet modeli, model tutarlılığı ve değişikliği, değer düşüklüğü), transferler (MDV, stok ve inşaat tamamlanması), elden çıkarma ve açıklama. Hesap soruları her biri farklı bağlamla yazıldı; tutarlar kesirli aritmetikle hesaplandı.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: TMS 40 Yatırım Amaçlı Gayrimenkuller
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/tms_40_yatirim_amacli.json"
STYLE_REF = 'SGS Muhasebe Standartları (senaryo kök + kısa şık; gerçek sınav profili)'
ONEK = "std-tms40-gen-"


def patch(stem, options, answer, solution, ref='TMS 40 Yatırım Amaçlı Gayrimenkuller'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        'Bir müteahhit, bir belediye adına onun sahipliğine geçecek bir hizmet binası inşa etmektedir.\n\nBu binanın muhasebeleştirilmesinde hangi standart esas alınır?',
        {
            'A': 'TMS 2',
            'B': 'TFRS 5',
            'C': 'TFRS 15',
            'D': 'TMS 16',
            'E': 'TMS 40',
        },
        'C',
        "Üçüncü kişiler adına inşa edilen gayrimenkuller TMS 40'ın kapsamı dışındadır; müşteri sözleşmesi olarak TFRS 15'e göre muhasebeleştirilir.",
    ),
    # düzey 2
    '0002': patch(
        "TMS 40'a göre aşağıdakilerden hangisi gerçeğe uygun değer modelini uygulayan işletmelerin açıklaması gereken bilgilerden biri değildir?",
        {
            'A': 'Gerçeğe uygun değer ölçüm yöntemi',
            'B': 'Dönem başı-sonu mutabakatı',
            'C': 'Değer değişiminden doğan kazanç',
            'D': 'Kira gelirleri',
            'E': 'Binaların fiziksel yaşı',
        },
        'E',
        'Standart; uygulanan model, gerçeğe uygun değer yöntemleri, kira gelirleri, doğrudan giderler, gerçeğe uygun değer değişimleri ve defter değeri mutabakatı gibi bilgilerin açıklanmasını ister.',
    ),
    # düzey 3
    '0003': patch(
        "Kiraya verdiği bir binası yangında hasar gören şirket, sigorta şirketinden 300.000 ₺ tazminat alacağını kesinleştirmiştir.\n\nTMS 40'a göre bu tazminat nasıl muhasebeleştirilir?",
        {
            'A': 'Binanın maliyetinden düşülür',
            'B': 'Özkaynakta izlenir',
            'C': 'Alacak hâline gelince kâr veya zararda',
            'D': 'Değer düşüklüğüyle netleştirilir',
            'E': 'Ertelenmiş gelir olur',
        },
        'C',
        'Değer düşüklüğüne uğrayan, kaybolan ya da terk edilen gayrimenkuller için üçüncü kişilerden alınacak tazminatlar, alacak hâline geldiğinde kâr veya zararda muhasebeleştirilir.',
    ),
    # düzey 3
    '0004': patch(
        "Elif A.Ş. yatırım amaçlı gayrimenkullerini gerçeğe uygun değerle ölçmektedir. Şirketin depo binası 2026'da 600.000 ₺ kira geliri getirmiş, 150.000 ₺ işletme gideri doğurmuştur. Deponun değeri yıl başında 7.000.000 ₺, yıl sonunda 6.700.000 ₺ olarak belirlenmiştir.\n\nBu deponun 2026 kâr veya zararına toplam etkisi kaç ₺'dir?",
        {
            'A': '-300.000 ₺',
            'B': '150.000 ₺',
            'C': '750.000 ₺',
            'D': '450.000 ₺',
            'E': '300.000 ₺',
        },
        'B',
        'Kira geliri ve giderler kâr veya zarara yansır; gerçeğe uygun değer değişimi (6.700.000 ₺ − 7.000.000 ₺ = -300.000 ₺) de kâr veya zarara alınır; amortisman ayrılmaz. Net etki: 600.000 ₺ − 150.000 ₺ + (-300.000 ₺) = 150.000 ₺.',
    ),
    # düzey 2
    '0005': patch(
        "Bir gıda şirketi merkez binasının iki katını kendi yönetim birimleri için kullanmakta, diğer üç katını ise başka şirketlere faaliyet kiralamasıyla kiraya vermektedir. Katlar ayrı ayrı satılabilmektedir.\n\nTMS 40'a göre kiraya verilen katlar nasıl sınıflandırılır?",
        {
            'A': 'Kullanım hakkı varlığı',
            'B': 'Maddi duran varlık',
            'C': 'Satış amaçlı varlık',
            'D': 'Stok',
            'E': 'Yatırım amaçlı gayrimenkul',
        },
        'E',
        'Gayrimenkulün kısımları ayrı satılabiliyorsa her kısım ayrı muhasebeleştirilir. Kiraya verilen katlar yatırım amaçlı gayrimenkul, yönetim için kullanılan katlar maddi duran varlıktır.',
    ),
    # düzey 3
    '0006': patch(
        "Gerçeğe uygun değer modelini uygulayan Mert A.Ş.'nin kiraya verdiği arsanın 31 Aralık 2025'teki gerçeğe uygun değeri 6.000.000 ₺'dir. Şirket 1 Temmuz 2026'da arsa üzerinde satmak amacıyla konut projesi geliştirmeye başlamıştır; bu tarihte arsanın gerçeğe uygun değeri 6.450.000 ₺'dir.\n\nTMS 40'a göre arsanın stoklara aktarılan maliyeti kaç ₺'dir?",
        {
            'A': '5.850.000 ₺',
            'B': '450.000 ₺',
            'C': '6.000.000 ₺',
            'D': '6.450.000 ₺',
            'E': '5.550.000 ₺',
        },
        'D',
        'Gerçeğe uygun değerle izlenen yatırım amaçlı gayrimenkul stoklara aktarılırken sonraki muhasebeleştirmede esas alınacak tahmini maliyet, kullanım değişikliği tarihindeki gerçeğe uygun değerdir: 6.450.000 ₺. Aradaki 450.000 ₺ artış kâr veya zarara yansıtılır.',
    ),
    # düzey 2
    '0007': patch(
        'TMS 40 ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
        {
            'A': 'Maliyet modelinde gerçeğe uygun değer açıklanır',
            'B': 'Model tüm gayrimenkullere uygulanır',
            'C': 'İlk ölçüm maliyetle yapılır',
            'D': 'Değer artışları özkaynağa alınır',
            'E': 'Elden çıkarma kazancı kâr veya zarara yansır',
        },
        'D',
        'Gerçeğe uygun değer modelinde değer artışları özkaynağa değil kâr veya zarara alınır. Diğer ifadeler doğrudur.',
    ),
    # düzey 3
    '0008': patch(
        "Ada A.Ş. kiraya vermek amacıyla bir iş merkezi satın almıştır. Bilgiler:\n\n- Satın alma bedeli: 8.000.000 ₺\n- Tapu harcı: 240.000 ₺\n- Hukuki danışmanlık ücreti: 60.000 ₺\n- Binanın açılış töreni gideri: 50.000 ₺\n- Kiracı bulunana kadar boş kalan sürede oluşan işletme zararı: 120.000 ₺\n\nTMS 40'a göre iş merkezinin ilk maliyeti kaç ₺'dir?",
        {
            'A': '8.000.000 ₺',
            'B': '8.360.000 ₺',
            'C': '8.300.000 ₺',
            'D': '8.350.000 ₺',
            'E': '8.470.000 ₺',
        },
        'C',
        'İlk ölçüm maliyetle yapılır; maliyet, satın alma bedeli ile doğrudan ilişkilendirilebilen işlem maliyetlerini (tapu harcı, hukuki ücretler, komisyon) içerir: 8.000.000 ₺ + 240.000 ₺ + 60.000 ₺ = 8.300.000 ₺. Açılış, tanıtım ve başlangıç dönemi işletme zararları maliyete eklenmez.',
    ),
    # düzey 3
    '0009': patch(
        'Maliyet modelini uygulayan bir şirket bir yatırım amaçlı gayrimenkulünü satış amaçlı elde tutulan duran varlık olarak sınıflandırma ölçütlerini karşılamaktadır.\n\nBu gayrimenkul için hangi standart uygulanır?',
        {
            'A': 'TFRS 5',
            'B': 'TMS 16',
            'C': 'TMS 2',
            'D': 'TFRS 15',
            'E': 'TMS 36',
        },
        'A',
        "Maliyet modelinde, satış amaçlı sınıflandırma ölçütlerini karşılayan yatırım amaçlı gayrimenkuller TFRS 5'e göre ölçülür.",
    ),
    # düzey 3
    '0010': patch(
        "Gerçeğe uygun değer modelini uygulayan Pınar A.Ş., kiraya verdiği binayı 1 Ocak 2026'da kendi genel müdürlüğü olarak kullanmaya başlamıştır. Bina 2018'de 3.000.000 ₺'ye alınmış olup bedelin tamamı binaya aittir. Transfer tarihindeki gerçeğe uygun değeri 3.600.000 ₺, kalan faydalı ömrü 30 yıl, kalıntı değeri sıfırdır.\n\nTMS 16'ya göre binanın 2026 yılı amortismanı kaç ₺'dir?",
        {
            'A': '600.000 ₺',
            'B': '220.000 ₺',
            'C': '120.000 ₺',
            'D': '140.000 ₺',
            'E': '0 ₺',
        },
        'C',
        'Gerçeğe uygun değerle izlenen gayrimenkul sahibi kullanımına geçince tahmini maliyeti transfer tarihindeki gerçeğe uygun değerdir. Amortisman 3.600.000 ₺ / 30 = 120.000 ₺.',
    ),
    # düzey 3
    '0011': patch(
        "Rüzgâr A.Ş. değer artışı amacıyla tuttuğu bir arsayı, ticari özü bulunan bir takasla kiraya vermek üzere bir dükkânla değiştirmiştir. Verilen arsanın defter değeri 1.200.000 ₺, gerçeğe uygun değeri 1.800.000 ₺'dir; alınan dükkânın gerçeğe uygun değeri güvenilir biçimde ölçülememektedir.\n\nTMS 40'a göre dükkânın ilk ölçümdeki maliyeti kaç ₺'dir?",
        {
            'A': '1.500.000 ₺',
            'B': '1.800.000 ₺',
            'C': '1.200.000 ₺',
            'D': '600.000 ₺',
            'E': '3.000.000 ₺',
        },
        'B',
        'Ticari özü olan takasla edinilen yatırım amaçlı gayrimenkul gerçeğe uygun değerle ölçülür. Alınan varlığın gerçeğe uygun değeri güvenilir ölçülemediğinden verilen arsanın gerçeğe uygun değeri esas alınır: 1.800.000 ₺.',
    ),
    # düzey 3
    '0012': patch(
        'I. Kiraya verilen bina için ayrılan amortisman\nII. Gerçeğe uygun değer artışı\nIII. Elde edilen kira geliri\n\nGerçeğe uygun değer modelini uygulayan bir şirkette yukarıdakilerden hangileri kâr veya zararı etkiler?',
        {
            'A': 'I, II ve III',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'Yalnız I',
            'E': 'I ve III',
        },
        'C',
        'Gerçeğe uygun değer modelinde amortisman ayrılmaz; değer değişimleri ve kira geliri kâr veya zarara yansır.',
    ),
    # düzey 3
    '0013': patch(
        "Bir şirket yatırım amaçlı gayrimenkulü bağışlama yoluyla bedelsiz olarak edinmiş ve bunun için yalnız 30.000 ₺ tapu masrafı ödemiştir. Gayrimenkulün gerçeğe uygun değeri 2.000.000 ₺'dir.\n\nTMS 40 bakımından ilk ölçümle ilgili hangisi doğrudur?",
        {
            'A': 'Maliyetle ölçülür',
            'B': 'Sıfır tutarla ölçülür',
            'C': 'Ölçüm ertelenir',
            'D': 'Tapu masrafı gider yazılır',
            'E': 'Özkaynağa bağış fonu açılır',
        },
        'A',
        'TMS 40 ilk ölçümün maliyetle yapılmasını ister; maliyet unsurlarının belirlenmesinde edinim biçimine (takas, bağış vb.) göre ilgili hükümler uygulanır. İlk ölçüm maliyet esasıdır.',
    ),
    # düzey 3
    '0014': patch(
        "Gerçeğe uygun değer modelini benimsemiş Funda A.Ş.'nin ofis binası için yıl sonu değerlemesi 15.500.000 ₺, yıl başı değeri 15.000.000 ₺'dir. Yıl içinde binadan 1.200.000 ₺ kira tahsil edilmiş ve 300.000 ₺ gider yapılmıştır.\n\nTMS 40'a göre binanın dönem kârına etkisi kaç ₺'dir?",
        {
            'A': '1.400.000 ₺',
            'B': '500.000 ₺',
            'C': '400.000 ₺',
            'D': '1.700.000 ₺',
            'E': '900.000 ₺',
        },
        'A',
        'Kira geliri ve giderler kâr veya zarara yansır; gerçeğe uygun değer değişimi (15.500.000 ₺ − 15.000.000 ₺ = 500.000 ₺) de kâr veya zarara alınır; amortisman ayrılmaz. Net etki: 1.200.000 ₺ − 300.000 ₺ + (500.000 ₺) = 1.400.000 ₺.',
    ),
    # düzey 3
    '0015': patch(
        "Gerçeğe uygun değer modelini uygulayan bir şirket, kiraya verdiği binayı boşaltarak kendi idari birimleri için kullanmaya başlamıştır. Transfer tarihinde binanın gerçeğe uygun değeri 3.500.000 ₺'dir.\n\nTMS 40'a göre binanın TMS 16'daki maliyeti kaç ₺ olur?",
        {
            'A': 'Vergi değeri',
            'B': '3.500.000 ₺',
            'C': '3.150.000 ₺',
            'D': '0 ₺',
            'E': 'Önceki maliyeti',
        },
        'B',
        'Gerçeğe uygun değerle izlenen yatırım amaçlı gayrimenkulden sahibi tarafından kullanılan gayrimenkule transferde, sonraki muhasebeleştirme için tahmini maliyet transfer tarihindeki gerçeğe uygun değerdir.',
    ),
    # düzey 3
    '0016': patch(
        "Gerçeğe uygun değer modelini uygulayan Okyanus A.Ş.'nin kiralık alışveriş merkezinin yıl başındaki gerçeğe uygun değeri 8.000.000 ₺'dir. Yıl içinde merkeze yürüyen merdiven eklenmiş ve 600.000 ₺ tutarındaki harcama gayrimenkulün defter değerine eklenmiştir. Yıl sonunda gerçeğe uygun değer 9.000.000 ₺ olarak belirlenmiştir.\n\nYıl sonu değerlemesinde kâr veya zarara yansıyan kazanç kaç ₺'dir?",
        {
            'A': '1.000.000 ₺',
            'B': '600.000 ₺',
            'C': '1.600.000 ₺',
            'D': '8.600.000 ₺',
            'E': '400.000 ₺',
        },
        'E',
        'Aktifleştirilen harcamayla defter değeri 8.000.000 ₺ + 600.000 ₺ = 8.600.000 ₺ olur. Yıl sonu gerçeğe uygun değeriyle fark 9.000.000 ₺ − 8.600.000 ₺ = 400.000 ₺ kazanç olarak kâr veya zarara yansıtılır.',
    ),
    # düzey 2
    '0017': patch(
        "Bir şirket yatırım amaçlı gayrimenkulleri için maliyet modelini seçmiştir.\n\nTMS 40'a göre şirketin dipnotlarda ayrıca açıklaması gereken bilgi aşağıdakilerden hangisidir?",
        {
            'A': 'Vergi değeri',
            'B': 'Sigorta değeri',
            'C': 'Gerçeğe uygun değer',
            'D': 'Tapu değeri',
            'E': 'Belediye rayiç değeri',
        },
        'C',
        'Maliyet modelini seçen işletmeler de yatırım amaçlı gayrimenkullerinin gerçeğe uygun değerini dipnotlarda açıklar.',
    ),
    # düzey 3
    '0018': patch(
        "Bir şirket bir binayı üçüncü kişilere faaliyet kiralamasıyla kiraya vermek amacıyla inşa etmektedir; inşaat sürmektedir.\n\nTMS 40'a göre inşa hâlindeki bina nasıl sınıflandırılır?",
        {
            'A': 'Maddi duran varlık',
            'B': 'Satış amaçlı varlık',
            'C': 'Yapılmakta olan yatırım',
            'D': 'Stok',
            'E': 'Yatırım amaçlı gayrimenkul',
        },
        'E',
        'Gelecekte yatırım amaçlı gayrimenkul olarak kullanılmak üzere inşa edilen ya da geliştirilen gayrimenkuller TMS 40 kapsamındadır.',
    ),
    # düzey 2
    '0019': patch(
        "Gerçeğe uygun değer modelini uygulayan bir şirket, yatırım amaçlı gayrimenkulünün değerinin yıl içinde 250.000 ₺ azaldığını belirlemiştir.\n\nTMS 40'a göre bu azalış nasıl muhasebeleştirilir?",
        {
            'A': 'Ertelenmiş vergiden',
            'B': 'Geçmiş yıl kârından',
            'C': 'Kâr veya zararda gider',
            'D': 'Yeniden değerleme fonundan',
            'E': 'Diğer kapsamlı gelirden',
        },
        'C',
        'Gerçeğe uygun değer modelinde değer azalışı da dönemin kâr veya zararına yansıtılır.',
    ),
    # düzey 2
    '0020': patch(
        "Bir şirket gelecekte nasıl kullanacağına henüz karar vermediği bir arsayı elinde tutmaktadır.\n\nTMS 40'a göre bu arsa nasıl sınıflandırılır?",
        {
            'A': 'Satış amaçlı varlık',
            'B': 'Yatırım amaçlı gayrimenkul',
            'C': 'Stok',
            'D': 'Maddi duran varlık',
            'E': 'Peşin ödenmiş gider',
        },
        'B',
        'Gelecekteki kullanımı belirlenmemiş arazinin değer artış kazancı amacıyla elde tutulduğu kabul edilir ve yatırım amaçlı gayrimenkul olarak sınıflandırılır.',
    ),
    # düzey 3
    '0021': patch(
        "Fabrikasını yeni bir bölgeye taşıyan Jale A.Ş., eski fabrika binasını faaliyet kiralamasıyla kiraya vermeye başlamıştır. Binanın transfer tarihindeki defter değeri 5.000.000 ₺, gerçeğe uygun değeri 4.400.000 ₺'dir. Şirket yatırım amaçlı gayrimenkuller için gerçeğe uygun değer modelini kullanmaktadır ve binada daha önce yeniden değerleme yapılmamıştır.\n\nTransfer farkı TMS 40'a göre hangi kalemde muhasebeleştirilir?",
        {
            'A': 'Yeniden değerleme fonu',
            'B': 'Ertelenmiş gelir',
            'C': 'Kâr veya zararda gelir',
            'D': 'Geçmiş yıl kârı',
            'E': 'Kâr veya zararda gider',
        },
        'E',
        'Gerçeğe uygun değer (4.400.000 ₺) defter değerinin (5.000.000 ₺) altında kaldığından 600.000 ₺ fark (önceden oluşmuş bir yeniden değerleme fonu yoksa) kâr veya zararda gider olarak muhasebeleştirilir.',
    ),
    # düzey 3
    '0022': patch(
        "Bir şirket yatırım amaçlı gayrimenkuller için bağımsız ve mesleki yeterliliğe sahip bir değerleme uzmanının değerlemesini kullanmamıştır.\n\nTMS 40'a göre bu durumla ilgili hangisi doğrudur?",
        {
            'A': 'Değerleme geçersizdir',
            'B': 'Maliyet modeline geçilmelidir',
            'C': 'Gayrimenkul gider yazılır',
            'D': 'Bu durum açıklanmalıdır',
            'E': 'Değer sıfırlanır',
        },
        'D',
        'Uzman değerlemesi zorunlu tutulmamakla birlikte teşvik edilir; bağımsız uzman değerlemesi kullanılmadıysa bu durum açıklanır.',
    ),
    # düzey 2
    '0023': patch(
        "I. Kira geliri elde etmek amacıyla tutulan bina\nII. Değer artışı amacıyla tutulan arsa\nIII. Üretimde kullanılan fabrika binası\n\nYukarıdakilerden hangileri TMS 40'a göre yatırım amaçlı gayrimenkuldür?",
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'I, II ve III',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'D',
        'Kira geliri ya da değer artışı (veya her ikisi) amacıyla tutulan gayrimenkuller yatırım amaçlı gayrimenkuldür. Üretimde kullanılan bina TMS 16 kapsamındadır.',
    ),
    # düzey 2
    '0024': patch(
        "TMS 40'a göre yatırım amaçlı gayrimenkulün elden çıkarılmasından doğan kazanç nerede muhasebeleştirilir?",
        {
            'A': 'Yeniden değerleme fonunda',
            'B': 'Diğer kapsamlı gelirde',
            'C': 'Kâr veya zararda',
            'D': 'Geçmiş yıl kârında',
            'E': 'Ertelenmiş gelirde',
        },
        'C',
        'Elden çıkarma kazanç ya da kayıpları elden çıkarma döneminde kâr veya zararda muhasebeleştirilir.',
    ),
    # düzey 3
    '0025': patch(
        "I. Satış\nII. Finansal kiralama yoluyla kiraya verme\nIII. Faaliyet kiralamasıyla kiraya verme\n\nYukarıdakilerden hangileri TMS 40'a göre yatırım amaçlı gayrimenkulün elden çıkarılması sonucunu doğurur?",
        {
            'A': 'II ve III',
            'B': 'Yalnız I',
            'C': 'I ve III',
            'D': 'I, II ve III',
            'E': 'I ve II',
        },
        'E',
        'Satış ve finansal kiralama yoluyla kiraya verme elden çıkarma sonucunu doğurur; faaliyet kiralaması gayrimenkulün yatırım amaçlı niteliğini sürdürür.',
    ),
    # düzey 3
    '0026': patch(
        "I. Kira geliri elde edilen gayrimenkullerin doğrudan işletme giderleri\nII. Kira geliri elde edilmeyen gayrimenkullerin doğrudan işletme giderleri\nIII. Gerçeğe uygun değer değişiminden doğan net kazanç veya kayıp\n\nTMS 40'a göre yukarıdakilerden hangileri açıklanması gereken bilgiler arasındadır?",
        {
            'A': 'II ve III',
            'B': 'I, II ve III',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'I ve III',
        },
        'B',
        'Standart, kira geliri doğuran ve doğurmayan gayrimenkullerin doğrudan işletme giderlerini ayrı ayrı; gerçeğe uygun değer değişimlerinden doğan net kazanç veya kaybı ise defter değeri mutabakatında açıklatır.',
    ),
    # düzey 3
    '0027': patch(
        "Bir şirket kiraya verdiği binayı geliştirme yapmadan olduğu gibi satmaya karar vermiştir.\n\nTMS 40'a göre bina için hangisi doğrudur?",
        {
            'A': 'Değeri sıfırlanır',
            'B': "MDV'ye aktarılır",
            'C': 'Özkaynağa aktarılır',
            'D': 'Hemen stoka aktarılır',
            'E': "Bilanço dışı kalana dek TMS 40'ta kalır",
        },
        'E',
        'Yatırım amaçlı gayrimenkulü geliştirme yapmadan elden çıkarmaya karar veren işletme, gayrimenkul bilanço dışı bırakılana kadar onu yatırım amaçlı gayrimenkul olarak izlemeye devam eder (maliyet modelinde TFRS 5 koşulları ayrıca değerlendirilir).',
    ),
    # düzey 3
    '0028': patch(
        "Hilal A.Ş. yatırım amaçlı gayrimenkullerinde maliyet modelini seçmiştir. Yıl başında edinilen kiralık depo için toplam bedelin 2.000.000 ₺'si araziye, 4.000.000 ₺'si yapıya aittir; yapı 40 yılda doğrusal amortismana tabidir. Yıllık kira geliri 300.000 ₺'dir.\n\nDeponun yıl kârına etkisi kaç ₺'dir?",
        {
            'A': '400.000 ₺',
            'B': '150.000 ₺',
            'C': '300.000 ₺',
            'D': '200.000 ₺',
            'E': '100.000 ₺',
        },
        'D',
        'Maliyet modelinde TMS 16 hükümleri uygulanır: arsa amortismana tabi değildir. Bina amortismanı 4.000.000 ₺ / 40 = 100.000 ₺. Net etki 300.000 ₺ − 100.000 ₺ = 200.000 ₺.',
    ),
    # düzey 2
    '0029': patch(
        "Gerçeğe uygun değer modelini seçen bir şirket, yatırım amaçlı gayrimenkulleri için amortisman ayırmayı da düşünmektedir.\n\nTMS 40'a göre bu konuda hangisi doğrudur?",
        {
            'A': 'Amortisman ayrılmaz',
            'B': 'Normal amortisman ayrılır',
            'C': 'Hızlandırılmış amortisman ayrılır',
            'D': 'Vergi amortismanı ayrılır',
            'E': 'Binaya ayrılır, arsaya ayrılmaz',
        },
        'A',
        'Gerçeğe uygun değer modelinde gayrimenkul her raporlama döneminde gerçeğe uygun değerle ölçülür; amortisman ayrılmaz.',
    ),
    # düzey 3
    '0030': patch(
        "Leyla A.Ş. yatırım amaçlı arsasını 2.600.000 ₺'ye satmış; ilan ve tapu devri için 60.000 ₺ ödemiştir. Arsanın satış anındaki defter değeri 2.200.000 ₺'dir.\n\nBu satışın kâr veya zarara etkisi kaç ₺'dir?",
        {
            'A': '400.000 ₺',
            'B': '2.540.000 ₺',
            'C': '340.000 ₺',
            'D': '680.000 ₺',
            'E': '460.000 ₺',
        },
        'C',
        'Elden çıkarma kazancı, net elden çıkarma geliri ile defter değeri arasındaki farktır: 2.600.000 ₺ − 60.000 ₺ − 2.200.000 ₺ = 340.000 ₺; kâr veya zarara yansıtılır.',
    ),
    # düzey 3
    '0031': patch(
        "Maliyet modelini uygulayan Gül A.Ş., 1 Ocak 2026'da kiraya vermek üzere arsa payı 3.000.000 ₺, bina payı 5.000.000 ₺ olan bir gayrimenkul almıştır. Binanın faydalı ömrü 50 yıl, kalıntı değeri sıfırdır. Gayrimenkulden 2026'da 400.000 ₺ kira geliri elde edilmiştir.\n\nTMS 40'a göre gayrimenkulün 2026 kârına net etkisi kaç ₺'dir?",
        {
            'A': '400.000 ₺',
            'B': '240.000 ₺',
            'C': '300.000 ₺',
            'D': '500.000 ₺',
            'E': '160.000 ₺',
        },
        'C',
        'Maliyet modelinde TMS 16 hükümleri uygulanır: arsa amortismana tabi değildir. Bina amortismanı 5.000.000 ₺ / 50 = 100.000 ₺. Net etki 400.000 ₺ − 100.000 ₺ = 300.000 ₺.',
    ),
    # düzey 3
    '0032': patch(
        "Bir şirketin sahip olduğu bina, çalışanlarına piyasa fiyatıyla kiraya verilen lojmanlardan oluşmaktadır.\n\nTMS 40'a göre bu bina nasıl sınıflandırılır?",
        {
            'A': 'Yatırım amaçlı gayrimenkul',
            'B': 'Finansal kiralama alacağı',
            'C': 'Stok',
            'D': 'Satış amaçlı varlık',
            'E': 'Maddi duran varlık',
        },
        'E',
        'Çalışanların kullandığı gayrimenkul, çalışanlar piyasa fiyatıyla kira ödese de sahibi tarafından kullanılan gayrimenkul sayılır.',
    ),
    # düzey 3
    '0033': patch(
        "Gerçeğe uygun değer modelini uygulayan bir şirket, stoklarında izlediği bir binayı satmak yerine kiraya vermeye karar vermiş ve faaliyet kiralaması başlamıştır. Binanın stoktaki değeri 2.000.000 ₺, gerçeğe uygun değeri 2.600.000 ₺'dir.\n\nTMS 40'a göre 600.000 ₺ fark nasıl muhasebeleştirilir?",
        {
            'A': 'Ertelenmiş gelir',
            'B': 'Stok değer artış fonu',
            'C': 'Kâr veya zararda gelir',
            'D': 'Diğer kapsamlı gelir',
            'E': 'Yeniden değerleme fonu',
        },
        'C',
        'Stoktan gerçeğe uygun değerle izlenecek yatırım amaçlı gayrimenkule transferde, transfer tarihindeki gerçeğe uygun değer ile önceki defter değeri arasındaki fark kâr veya zarara yansıtılır.',
    ),
    # düzey 3
    '0034': patch(
        "Ceyhan A.Ş. kiraya vermek üzere bir binayı iki yıl vadeli olarak 7.200.000 ₺ bedelle satın almıştır. Binanın peşin satış fiyatı 6.000.000 ₺'dir.\n\nTMS 40'a göre binanın ilk maliyeti kaç ₺'dir?",
        {
            'A': '6.600.000 ₺',
            'B': '1.200.000 ₺',
            'C': '7.200.000 ₺',
            'D': '6.000.000 ₺',
            'E': '4.800.000 ₺',
        },
        'D',
        'Ödemenin ertelendiği durumda maliyet, peşin fiyat eşdeğeridir: 6.000.000 ₺. Toplam ödemeyle aradaki 1.200.000 ₺ fark, kredi süresince faiz gideri olarak muhasebeleştirilir.',
    ),
    # düzey 3
    '0035': patch(
        "Ana ortaklık, sahip olduğu bir binayı bağlı ortaklığına ofis olarak kiraya vermektedir.\n\nTMS 40'a göre bina konsolide finansal tablolarda nasıl sınıflandırılır?",
        {
            'A': 'Finansal varlık',
            'B': 'Maddi duran varlık',
            'C': 'Stok',
            'D': 'Yatırım amaçlı gayrimenkul',
            'E': 'Satış amaçlı varlık',
        },
        'B',
        'Grup içinde kiraya verilen gayrimenkul, grup açısından sahibi tarafından kullanıldığından konsolide tablolarda yatırım amaçlı gayrimenkul sayılmaz.',
    ),
    # düzey 2
    '0036': patch(
        "Gerçeğe uygun değer modelini uygulayan bir şirketin yatırım amaçlı gayrimenkulünün değeri yıl içinde 400.000 ₺ artmıştır.\n\nTMS 40'a göre bu artış nasıl muhasebeleştirilir?",
        {
            'A': 'Ertelenmiş gelir olarak',
            'B': 'Kâr veya zararda',
            'C': 'Yeniden değerleme fonunda',
            'D': 'Diğer kapsamlı gelirde',
            'E': 'Doğrudan geçmiş yıl kârında',
        },
        'B',
        'Gerçeğe uygun değer modelinde değer değişimlerinden doğan kazanç ya da kayıplar oluştukları dönemin kâr veya zararına yansıtılır.',
    ),
    # düzey 2
    '0037': patch(
        "Bir şirket, kiraya vermek üzere elde tuttuğu ancak şu an kiracısı olmayan bir iş hanına sahiptir.\n\nTMS 40'a göre bu iş hanı nasıl sınıflandırılır?",
        {
            'A': 'Stok',
            'B': 'Ertelenmiş gider',
            'C': 'Satış amaçlı varlık',
            'D': 'Maddi duran varlık',
            'E': 'Yatırım amaçlı gayrimenkul',
        },
        'E',
        'Faaliyet kiralamasıyla kiraya verilmek üzere elde tutulan boş bina da yatırım amaçlı gayrimenkuldür.',
    ),
    # düzey 3
    '0038': patch(
        "Gerçeğe uygun değer modelini uygulayan bir şirket, inşasını kendi yaptığı ve yatırım amaçlı gayrimenkul olarak kullanacağı binanın inşaatını tamamlamıştır. Binanın tamamlanma tarihindeki gerçeğe uygun değeri önceki defter değerinden 500.000 ₺ fazladır.\n\nTMS 40'a göre bu fark nasıl muhasebeleştirilir?",
        {
            'A': 'Ertelenmiş gelir olarak',
            'B': 'Kâr veya zararda gelir',
            'C': 'Yeniden değerleme fonunda',
            'D': 'Binanın maliyetinden düşülerek',
            'E': 'Diğer kapsamlı gelirde',
        },
        'B',
        'Kendisi tarafından inşa edilen ve gerçeğe uygun değerle izlenecek yatırım amaçlı gayrimenkulün tamamlanma tarihindeki gerçeğe uygun değeri ile önceki defter değeri arasındaki fark kâr veya zarara yansıtılır.',
    ),
    # düzey 3
    '0039': patch(
        "Gerçeğe uygun değer modelini uygulayan bir şirket, gelecek yıldan itibaren maliyet modeline geçmeyi düşünmektedir.\n\nTMS 40'a göre bu geçişle ilgili hangisi doğrudur?",
        {
            'A': 'Gerekçelendirilmesi pek olası değildir',
            'B': 'Geriye dönük düzeltme gerektirmez',
            'C': 'Vergi idaresinin onayına bağlıdır',
            'D': 'Bağımsız değerleme uzmanının kararıyla yapılır',
            'E': 'Her raporlama döneminde yapılabilir',
        },
        'A',
        "Model değişikliği TMS 8'e göre ancak daha uygun sunum sağlıyorsa yapılabilir; gerçeğe uygun değer modelinden maliyet modeline geçişin daha uygun sunum sağlaması pek olası değildir.",
    ),
    # düzey 3
    '0040': patch(
        "TMS 40'a göre aşağıdakilerden hangisi bir transferi gerektiren kullanım değişikliğinin kanıtı değildir?",
        {
            'A': 'Satış için geliştirmeye başlanması',
            'B': 'Yönetimin niyetinin değişmesi',
            'C': 'Başkasına faaliyet kiralamasının başlaması',
            'D': 'Sahibi kullanımının sona ermesi',
            'E': 'Sahibi kullanımına başlanması',
        },
        'B',
        'Transfer ancak kullanımda gerçek bir değişiklik olduğunda yapılır; yönetimin niyetindeki değişiklik tek başına kullanım değişikliğinin kanıtı değildir.',
    ),
    # düzey 3
    '0041': patch(
        "Bir şirket sahip olduğu bir binayı finansal kiralama yoluyla başka bir şirkete kiraya vermiştir.\n\nTMS 40'a göre kiraya verenin bu bina için hangisi doğrudur?",
        {
            'A': 'TMS 40 kapsamı dışındadır',
            'B': 'Satış amaçlı varlıktır',
            'C': 'MDV olarak kalır',
            'D': 'Yatırım amaçlı gayrimenkuldür',
            'E': 'Stok olarak izlenir',
        },
        'A',
        'Finansal kiralamayla kiraya verilen gayrimenkul kiraya veren için TMS 40 kapsamında değildir; kiraya veren bir kira alacağı muhasebeleştirir.',
    ),
    # düzey 2
    '0042': patch(
        "Bir emlak şirketi, normal iş akışında satmak amacıyla inşa ettiği konutları stokta tutmaktadır.\n\nTMS 40'a göre bu konutlar için aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Stok olarak izlenir',
            'B': 'Yatırım amaçlı gayrimenkuldür',
            'C': 'Maddi duran varlıktır',
            'D': 'Finansal varlıktır',
            'E': "Özellikli değildir ama TMS 40'tadır",
        },
        'A',
        'Normal iş akışında satış amacıyla elde tutulan gayrimenkuller TMS 2 kapsamında stoktur.',
    ),
    # düzey 2
    '0043': patch(
        "TMS 40'a göre yatırım amaçlı gayrimenkul aşağıdaki durumlardan hangisinde finansal durum tablosu dışı bırakılır?",
        {
            'A': 'Bakıma alındığında',
            'B': 'Kira geliri azaldığında',
            'C': 'Kiracısı ayrıldığında',
            'D': 'Değeri düştüğünde',
            'E': 'Elden çıkarıldığında',
        },
        'E',
        'Yatırım amaçlı gayrimenkul elden çıkarıldığında ya da kullanımdan çekilip elden çıkarılmasından gelecekte ekonomik yarar beklenmediğinde bilanço dışı bırakılır.',
    ),
    # düzey 2
    '0044': patch(
        'Maliyet modelini uygulayan bir şirket, kiraya verdiği binanın bulunduğu bölgede kiraların sert biçimde düştüğünü ve binanın geri kazanılabilir tutarının defter değerinin altına indiğini belirlemiştir.\n\nBu değer düşüklüğü hangi standarda göre muhasebeleştirilir?',
        {
            'A': 'TMS 37',
            'B': 'TMS 2',
            'C': 'TMS 36',
            'D': 'TFRS 13',
            'E': 'TFRS 9',
        },
        'C',
        'Maliyet modelinde TMS 16 hükümleri uygulanır; değer düşüklüğü TMS 36 Varlıklarda Değer Düşüklüğü standardına göre belirlenir ve muhasebeleştirilir.',
    ),
    # düzey 3
    '0045': patch(
        "Bir şirket bir binanın büyük bölümünü kiraya vermekte, binanın küçük ve önemsiz bir kısmını ise bina görevlileri için kullanmaktadır. Kısımlar ayrı ayrı satılamamaktadır.\n\nTMS 40'a göre bina nasıl sınıflandırılır?",
        {
            'A': 'Kısmen stok kısmen MDV',
            'B': 'Maddi duran varlık',
            'C': 'Finansal varlık',
            'D': 'Yatırım amaçlı gayrimenkul',
            'E': 'Stok',
        },
        'D',
        'Kısımlar ayrı satılamıyorsa, sahibi tarafından kullanılan kısım önemsiz olduğunda gayrimenkulün tamamı yatırım amaçlı gayrimenkuldür.',
    ),
    # düzey 2
    '0046': patch(
        "Bir şirket yatırım amaçlı gayrimenkullerinden bazılarına gerçeğe uygun değer modelini, bazılarına maliyet modelini uygulamak istemektedir (yükümlülüklere bağlı özel fonlar söz konusu değildir).\n\nTMS 40'a göre bu konuda hangisi doğrudur?",
        {
            'A': 'Tek model seçilmelidir',
            'B': 'Vergi mevzuatına göre seçilir',
            'C': 'Bina-arsa ayrımı yapılır',
            'D': 'Gayrimenkul bazında seçilebilir',
            'E': 'Her yıl değiştirilebilir',
        },
        'A',
        'Seçilen muhasebe politikası (gerçeğe uygun değer ya da maliyet modeli) tüm yatırım amaçlı gayrimenkullere uygulanır.',
    ),
    # düzey 2
    '0047': patch(
        "Bir şirket kiraya verdiği bir binanın bozulan asansörünü değiştirmiş ve bu değişim binanın gelecekteki ekonomik yararlarını artırmıştır.\n\nTMS 40'a göre asansör değişim maliyeti için hangisi doğrudur?",
        {
            'A': 'Kira gelirinden düşülür',
            'B': 'Ertelenmiş vergi olur',
            'C': 'Doğrudan gider yazılır',
            'D': 'Defter değerine eklenir',
            'E': 'Özkaynağa alınır',
        },
        'D',
        'Bir parçanın değiştirilme maliyeti, varlık tanımını ve muhasebeleştirme ölçütlerini karşılıyorsa defter değerine eklenir; değiştirilen parçanın defter değeri bilanço dışı bırakılır.',
    ),
    # düzey 3
    '0048': patch(
        "Gerçeğe uygun değer modelini uygulayan Deniz A.Ş.'nin kiraya verdiği AVM'ye ilişkin 2026 bilgileri şöyledir:\n\n- Kira geliri: 900.000 ₺\n- Bakım ve sigorta giderleri: 200.000 ₺\n- 1 Ocak gerçeğe uygun değer: 10.000.000 ₺\n- 31 Aralık gerçeğe uygun değer: 10.600.000 ₺\n\nAVM'nin 2026 dönem kârına net etkisi kaç ₺'dir?",
        {
            'A': '1.300.000 ₺',
            'B': '100.000 ₺',
            'C': '700.000 ₺',
            'D': '1.500.000 ₺',
            'E': '600.000 ₺',
        },
        'A',
        'Kira geliri ve giderler kâr veya zarara yansır; gerçeğe uygun değer değişimi (10.600.000 ₺ − 10.000.000 ₺ = 600.000 ₺) de kâr veya zarara alınır; amortisman ayrılmaz. Net etki: 900.000 ₺ − 200.000 ₺ + (600.000 ₺) = 1.300.000 ₺.',
    ),
    # düzey 3
    '0049': patch(
        "Bir şirket TFRS 16 kapsamında kiraladığı bir binayı, aldığı kullanım hakkıyla birlikte başka bir şirkete faaliyet kiralamasıyla kiraya vermektedir.\n\nTMS 40'a göre kiracının bu kullanım hakkı varlığı için hangisi doğrudur?",
        {
            'A': 'Finansal varlıktır',
            'B': 'Yatırım amaçlı gayrimenkul olabilir',
            'C': 'Stok sayılır',
            'D': 'Gider olarak yazılır',
            'E': 'MDV olarak izlenir',
        },
        'B',
        'Kiracı tarafından kullanım hakkı varlığı olarak elde tutulan gayrimenkul, yatırım amaçlı gayrimenkul tanımını karşılıyorsa TMS 40 kapsamındadır.',
    ),
    # düzey 2
    '0050': patch(
        "Aşağıdakilerden hangisi TMS 40'a göre yatırım amaçlı gayrimenkul değildir?",
        {
            'A': 'Kiralanmak üzere inşa edilen AVM',
            'B': 'Boş durumdaki kiralık bina',
            'C': 'Değer artışı için tutulan arsa',
            'D': 'Kiraya verilen depo',
            'E': 'Satış için geliştirilen arsa',
        },
        'E',
        'Normal iş akışında satmak amacıyla geliştirilen gayrimenkul TMS 2 kapsamında stoktur. Diğerleri yatırım amaçlı gayrimenkuldür.',
    ),
    # düzey 3
    '0051': patch(
        "Nehir A.Ş. yönetim binası olarak kullandığı binayı 1 Ekim 2026'da boşaltıp kiraya vermiştir; yatırım amaçlı gayrimenkullerde gerçeğe uygun değer modelini uygulamaktadır. Binanın maliyeti 2.000.000 ₺, birikmiş amortismanı 400.000 ₺, transfer tarihindeki gerçeğe uygun değeri 2.300.000 ₺'dir. Binada daha önce yeniden değerleme yapılmamıştır.\n\nBu transfer nedeniyle yeniden değerleme fonuna alınacak tutar kaç ₺'dir?",
        {
            'A': '700.000 ₺',
            'B': '1.600.000 ₺',
            'C': '2.300.000 ₺',
            'D': '400.000 ₺',
            'E': '300.000 ₺',
        },
        'A',
        'Transfer tarihine kadar TMS 16 uygulanır; defter değeri 2.000.000 ₺ − 400.000 ₺ = 1.600.000 ₺. Gerçeğe uygun değer bunu 2.300.000 ₺ − 1.600.000 ₺ = 700.000 ₺ aştığından fark diğer kapsamlı gelirde yeniden değerleme fonuna alınır.',
    ),
    # düzey 3
    '0052': patch(
        "Maliyet modelini uygulayan bir şirket, kendi kullandığı binayı kiraya vermeye başlamıştır.\n\nTMS 40'a göre bu transferin muhasebeleştirilmesinde hangisi doğrudur?",
        {
            'A': 'Bina yeniden değerlenir',
            'B': 'Defter değeri değişmez',
            'C': 'Fark özkaynağa alınır',
            'D': 'Amortisman iptal edilir',
            'E': 'Fark kâr veya zarara alınır',
        },
        'B',
        'Maliyet modelinde yatırım amaçlı gayrimenkul, sahibi tarafından kullanılan gayrimenkul ve stoklar arasındaki transferler defter değerini değiştirmez; ölçüm ve açıklama amaçlı maliyet aynen aktarılır.',
    ),
    # düzey 3
    '0053': patch(
        "Gerçeğe uygun değer modelini uygulayan Kartal A.Ş., defter değeri 3.500.000 ₺ olan kiralık bir mağazayı 4.000.000 ₺ bedelle satmıştır. Satış için 100.000 ₺ emlakçı komisyonu ödenmiştir.\n\nTMS 40'a göre satıştan doğan kazanç kaç ₺'dir?",
        {
            'A': '400.000 ₺',
            'B': '500.000 ₺',
            'C': '3.900.000 ₺',
            'D': '600.000 ₺',
            'E': '800.000 ₺',
        },
        'A',
        'Elden çıkarma kazancı, net elden çıkarma geliri ile defter değeri arasındaki farktır: 4.000.000 ₺ − 100.000 ₺ − 3.500.000 ₺ = 400.000 ₺; kâr veya zarara yansıtılır.',
    ),
    # düzey 2
    '0054': patch(
        "Bir şirket kiraya verdiği binanın günlük bakım ve onarımı için 80.000 ₺ harcamıştır.\n\nTMS 40'a göre bu harcama nasıl muhasebeleştirilir?",
        {
            'A': 'Gider olarak',
            'B': 'Ertelenmiş gider olarak',
            'C': 'Binanın maliyetine',
            'D': 'Özkaynakta',
            'E': 'Kira alacağına',
        },
        'A',
        'Günlük bakım ve onarım maliyetleri gayrimenkulün defter değerine eklenmez; oluştukları dönemde kâr veya zararda gider olarak muhasebeleştirilir.',
    ),
    # düzey 3
    '0055': patch(
        "Değer artışı amacıyla bir arsa alan Bahar A.Ş., 5.000.000 ₺ satın alma bedelinin yanında 150.000 ₺ tapu harcı ve 100.000 ₺ emlakçı komisyonu ödemiştir. Arsanın tanıtımı için 40.000 ₺ reklam gideri yapılmış, arsanın ilk aylarında oluşan güvenlik giderleri ise 30.000 ₺ tutmuştur.\n\nArsa TMS 40'a göre ilk kayda hangi tutarla alınır?",
        {
            'A': '5.180.000 ₺',
            'B': '5.000.000 ₺',
            'C': '5.210.000 ₺',
            'D': '5.250.000 ₺',
            'E': '5.150.000 ₺',
        },
        'D',
        'İlk ölçüm maliyetle yapılır; maliyet, satın alma bedeli ile doğrudan ilişkilendirilebilen işlem maliyetlerini (tapu harcı, hukuki ücretler, komisyon) içerir: 5.000.000 ₺ + 150.000 ₺ + 100.000 ₺ = 5.250.000 ₺. Açılış, tanıtım ve başlangıç dönemi işletme zararları maliyete eklenmez.',
    ),
    # düzey 2
    '0056': patch(
        "Bir otel işletmesi sahip olduğu oteli işletmekte; konaklayanlara temizlik, yemek ve resepsiyon hizmetleri sunmaktadır.\n\nTMS 40'a göre otel nasıl sınıflandırılır?",
        {
            'A': 'Finansal kiralama alacağı',
            'B': 'Yatırım amaçlı gayrimenkul',
            'C': 'Satış amaçlı varlık',
            'D': 'Maddi duran varlık',
            'E': 'Stok',
        },
        'D',
        'Kiracılara sunulan ek hizmetler bütün içinde önemliyse gayrimenkul sahibi tarafından kullanılan gayrimenkuldür; işletilen otel TMS 16 kapsamında maddi duran varlıktır.',
    ),
    # düzey 3
    '0057': patch(
        "İnci A.Ş. bugüne kadar yönetim binası olarak kullandığı ve TMS 16'ya göre izlediği binayı boşaltarak kiraya vermiştir. Şirket yatırım amaçlı gayrimenkullerinde gerçeğe uygun değer modelini uygulamaktadır. Transfer tarihinde binanın defter değeri 3.000.000 ₺, gerçeğe uygun değeri 4.200.000 ₺'dir; daha önce binaya ilişkin yeniden değerleme ya da değer düşüklüğü kaydı yoktur.\n\nTMS 40'a göre aradaki fark nasıl muhasebeleştirilir?",
        {
            'A': 'Kâr veya zararda gelir',
            'B': 'Yeniden değerleme fonu',
            'C': 'Kâr veya zararda gider',
            'D': 'Ertelenmiş gelir',
            'E': 'Geçmiş yıl kârı',
        },
        'B',
        "Gerçeğe uygun değer (4.200.000 ₺) defter değerini (3.000.000 ₺) 1.200.000 ₺ aştığından fark, TMS 16'daki yeniden değerleme gibi diğer kapsamlı gelirde yeniden değerleme fonu olarak muhasebeleştirilir.",
    ),
    # düzey 3
    '0058': patch(
        "Bir şirket kiraya verdiği bir dükkânı iki yıl vadeyle satmıştır. Vadeli satış bedeli, satış tarihindeki peşin fiyat eşdeğerinin üzerindedir.\n\nTMS 40'a göre vadeli bedel ile peşin fiyat eşdeğeri arasındaki fark nasıl muhasebeleştirilir?",
        {
            'A': 'Yeniden değerleme fonu',
            'B': 'Satış anında elden çıkarma kazancı',
            'C': 'Diğer kapsamlı gelir',
            'D': 'Vade boyunca faiz geliri',
            'E': 'Satılan dükkânın maliyetine ekleme',
        },
        'D',
        'Elden çıkarma bedeli peşin fiyat eşdeğeriyle muhasebeleştirilir; vadeli bedel ile aradaki fark, etkin faiz yöntemiyle vade boyunca faiz geliri olarak tanınır.',
    ),
    # düzey 3
    '0059': patch(
        "Bir şirket kiraya verdiği bir arsayı satmak amacıyla üzerinde konut projesi geliştirmeye başlamıştır.\n\nTMS 40'a göre bu arsa hangi varlık grubuna transfer edilir?",
        {
            'A': 'Peşin ödenmiş giderler',
            'B': 'Satış amaçlı varlıklar',
            'C': 'Stoklar',
            'D': 'Finansal varlıklar',
            'E': 'Maddi duran varlıklar',
        },
        'C',
        'Satış amacıyla geliştirmeye başlanması, kullanım değişikliğinin kanıtıdır; gayrimenkul yatırım amaçlı gayrimenkulden stoka transfer edilir.',
    ),
    # düzey 3
    '0060': patch(
        "Gerçeğe uygun değer modelini uygulayan bir şirket inşa hâlindeki bir yatırım amaçlı gayrimenkulün gerçeğe uygun değerini güvenilir biçimde ölçememekte, ancak tamamlandığında ölçebileceğini beklemektedir.\n\nTMS 40'a göre inşa süresince bu gayrimenkul nasıl ölçülür?",
        {
            'A': 'Maliyetle',
            'B': 'Sıfır değerle',
            'C': 'Vergi değeriyle',
            'D': 'Satış fiyatıyla',
            'E': 'Gerçeğe uygun değerle',
        },
        'A',
        'İnşa hâlindeki gayrimenkulün gerçeğe uygun değeri güvenilir ölçülemiyor ancak inşaat tamamlanınca ölçülebilecekse, gayrimenkul gerçeğe uygun değer ölçülebilir hâle gelene ya da inşaat bitene kadar maliyetle ölçülür.',
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
    print(f"1 paket / {len(PATCHES)} soru ('TMS 40 Yatırım Amaçlı Gayrimenkuller' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
