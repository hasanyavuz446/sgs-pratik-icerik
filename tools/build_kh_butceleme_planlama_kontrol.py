#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bütçeleme, Planlama ve Kontrol — 3 × 20 özgün soru.

Eski builder aynı 26 bilgiyi iki farklı kökle tekrar ediyordu. Bu sürümde ikinci
26 soru farklı bilinmeyen, karar veya performans değerlendirmesi ölçer; son sekiz
soru da beş bağımsız uygulama ve üç öncüllü sorudan oluşur.
"""
import json
from pathlib import Path

from topic_pack_builder import balanced_letters


def R(scenario, focus, correct, bank, why, ref, difficulty="medium", distractors=None):
    return locals()


def tl(value):
    return f"{value:,.0f} TL".replace(",", ".")


WRONG = {
    "butce": [
        "Geçmiş yıl rakamlarını hiçbir faaliyet değişikliği dikkate almadan zorunlu olarak aynen tekrar eden bütçedir",
        "Yalnız gerçekleşen muhasebe kayıtlarını dönem sonunda sınıflandırır; geleceğe yönelik planlama işlevi bulunmaz",
        "Satış tahmininden bağımsız hazırlanır ve üretim, satın alma ile nakit planları arasında hiçbir bağlantı kurulmaz",
        "Yöneticilerin sorumluluk alanları ayrılmadan tüm sapmaları tek merkeze yükleyen geçmişe dönük bir raporlama aracıdır",
        "Sadece finansal tablolar yayımlandıktan sonra düzenlenir ve işletme kararlarından önce kullanılması mümkün değildir",
        "Faaliyet hacmi değişse bile karşılaştırma için bütçelenmiş giderleri uyarlamayı kesin olarak yasaklayan yöntemdir",
        "Her harcama kalemini önceki dönemden kazanılmış değişmez hak kabul eder ve yeniden gerekçelendirme istemez",
        "Bütçe dönemi içinde ortaya çıkan yeni bilgilerin tahmin ve kontrol sürecine alınmasını tamamen engeller",
    ],
    "kontrol": [
        "Yöneticiyi kontrol edemediği bütün dışsal etkilerden koşulsuz sorumlu tutarak performansı yalnız toplam sapmayla ölçer",
        "Gerçekleşen sonuçları bütçeyle karşılaştırmadan yalnız geçmiş yıl kârını esas alan tek aşamalı değerlendirme yapar",
        "Olumlu sapmaların daima iyi, olumsuz sapmaların daima kötü olduğunu neden analizi yapmadan kabul eder",
        "Maliyet, kâr ve yatırım merkezleri arasındaki yetki farkını yok sayarak her birini yalnız satış tutarıyla değerlendirir",
        "Bütçe hedeflerine ulaşmak için etik dışı veri saklamayı kabul edilebilir sayan ve amaç uyumunu önemsemeyen yaklaşımdır",
        "Düzeltici eylemi dönem sonuna kadar erteleyip sapmanın kaynağını araştırmayı gereksiz gören kontrol anlayışıdır",
        "Esnek bütçe yerine farklı faaliyet düzeylerini aynı statik tutarla karşılaştırarak hacim etkisini yöneticiye yükler",
        "Yatırım merkezi performansında kullanılan varlıkları ve sermaye maliyetini tamamen dışarıda bırakan ölçüm yaklaşımıdır",
    ],
}


# Bütün hesaplar soru verilerinden Python ile üretilir.
sales_units, price = 1_200, 250
sales_revenue = sales_units * price
prod_sales, end_fg, begin_fg = 10_000, 1_800, 1_200
production = prod_sales + end_fg - begin_fg
units, kg_per, end_dm, begin_dm = 5_000, 3, 2_000, 1_500
dm_purchase = units * kg_per + end_dm - begin_dm
dm_price = 40
dm_cost = dm_purchase * dm_price
labor_units, hours_per, wage = 6_000, 0.4, 180
labor_hours = labor_units * hours_per
labor_cost = labor_hours * wage
activity, var_oh, fixed_oh = 8_000, 35, 150_000
flex_oh = activity * var_oh + fixed_oh
current_sales, prior_receivable = 500_000, 200_000
collections = current_sales * 60 // 100 + prior_receivable * 40 // 100
current_purchases, prior_payable = 400_000, 150_000
payments = current_purchases * 70 // 100 + prior_payable * 30 // 100
begin_cash, cash_in, cash_out, min_cash = 100_000, 500_000, 650_000, 80_000
pre_finance = begin_cash + cash_in - cash_out
financing = min_cash - pre_finance
actual_cost, flex_cost = 470_000, 450_000
spending_variance = actual_cost - flex_cost
actual_price, budget_price, actual_qty = 22, 20, 5_000
price_variance = (actual_price - budget_price) * actual_qty
actual_volume, budget_volume, unit_price = 11_000, 10_000, 50
sales_volume_variance = (actual_volume - budget_volume) * unit_price
actual_units, variable_per_unit, fixed_cost = 9_000, 28, 120_000
flex_total = actual_units * variable_per_unit + fixed_cost
investment_profit, investment_base = 360_000, 2_400_000
roi = investment_profit / investment_base * 100
required_return = 12 / 100
residual_income = investment_profit - investment_base * required_return

assert sales_revenue == 300_000 and production == 10_600
assert dm_purchase == 15_500 and dm_cost == 620_000
assert labor_hours == 2_400 and labor_cost == 432_000
assert flex_oh == 430_000 and collections == 380_000 and payments == 325_000
assert pre_finance == -50_000 and financing == 130_000
assert spending_variance == 20_000 and price_variance == 10_000
assert sales_volume_variance == 50_000 and flex_total == 372_000
assert roi == 15 and residual_income == 72_000


RULES = [
    R(f"Bir işletme {sales_units:,} birim satış ve birim başına {price} TL fiyat öngörmektedir. Satış bütçesi kaç TL'dir?".replace(",", "."), f"{sales_units:,} birimin {price} TL'den bütçelenmesi hâlinde planlanan satış geliri nedir?".replace(",", "."), tl(sales_revenue), "butce", "Satış bütçesi, bütçelenen satış miktarı ile birim satış fiyatının çarpımıdır.", "Yönetim muhasebesi - satış bütçesi", "easy", [tl(250_000), tl(275_000), tl(325_000), tl(360_000)]),
    R(f"Satış bütçesi {prod_sales:,} birim, istenen dönem sonu mamul stoku {end_fg:,} ve dönem başı stok {begin_fg:,} birimdir. Üretim bütçesi kaç birimdir?".replace(",", "."), f"{prod_sales:,} birim satış, {end_fg:,} birim son stok ve {begin_fg:,} birim ilk stok için üretilecek miktar nedir?".replace(",", "."), f"{production:,.0f} birim".replace(",", "."), "butce", "Üretim = satış + hedef dönem sonu mamul stoku - dönem başı mamul stokudur.", "Yönetim muhasebesi - üretim bütçesi", "easy", ["9.400 birim", "10.000 birim", "11.200 birim", "13.000 birim"]),
    R(f"{units:,} birim üretimde birim başına {kg_per} kg madde kullanılacak; son madde stoku {end_dm:,}, ilk stok {begin_dm:,} kg'dır. Satın alma miktarı kaç kg'dır?".replace(",", "."), f"Üretim ihtiyacı {units * kg_per:,} kg iken {end_dm:,} kg hedef son stok ve {begin_dm:,} kg ilk stok varsa kaç kg madde alınır?".replace(",", "."), f"{dm_purchase:,.0f} kg".replace(",", "."), "butce", "Satın alma = üretimde kullanılacak madde + hedef son stok - ilk stoktur.", "Yönetim muhasebesi - direkt ilk madde bütçesi", "medium", ["13.500 kg", "14.500 kg", "16.500 kg", "18.500 kg"]),
    R(f"Bütçelenen madde alımı {dm_purchase:,} kg ve kilogram fiyatı {dm_price} TL'dir. Satın alma bütçesi kaç TL'dir?".replace(",", "."), f"{dm_purchase:,} kg doğrudan maddenin {dm_price} TL'den bütçelenen maliyeti nedir?".replace(",", "."), tl(dm_cost), "butce", "Satın alma bütçesi miktar ile bütçelenen birim alış fiyatının çarpımıdır.", "Yönetim muhasebesi - direkt ilk madde bütçesi", "medium", [tl(580_000), tl(600_000), tl(640_000), tl(660_000)]),
    R(f"{labor_units:,} birim üretim, birim başına {hours_per} direkt işçilik saati ve saat ücreti {wage} TL'dir. İşçilik bütçesi kaç TL'dir?".replace(",", "."), f"Toplam {labor_hours:,.0f} saatin saat başına {wage} TL'den bütçelenen direkt işçilik maliyeti nedir?".replace(",", "."), tl(labor_cost), "butce", "Önce üretim miktarıyla standart saat çarpılır; bulunan toplam saat bütçelenen ücretle çarpılır.", "Yönetim muhasebesi - direkt işçilik bütçesi", "medium", [tl(388_800), tl(405_000), tl(450_000), tl(480_000)]),
    R(f"Fiilî faaliyet {activity:,} birim, değişken genel üretim gideri birim başına {var_oh} TL ve sabit gider {fixed_oh:,} TL'dir. Esnek bütçe toplamı nedir?".replace(",", "."), f"{activity:,} birim faaliyet için {var_oh} TL değişken ve {fixed_oh:,} TL sabit gider içeren esnek bütçe kaç TL'dir?".replace(",", "."), tl(flex_oh), "butce", "Esnek bütçede değişken gider fiilî hacme göre uyarlanır; sabit gider ilgili aralıkta aynı kalır.", "Yönetim muhasebesi - esnek bütçe", "medium", [tl(280_000), tl(395_000), tl(465_000), tl(550_000)]),
    R(f"Cari ay satışlarının %60'ı olan {current_sales:,} TL ile önceki aydan kalan {prior_receivable:,} TL'nin %40'ı tahsil edilecektir. Nakit tahsilatı kaç TL'dir?".replace(",", "."), f"{tl(current_sales)} cari satışın %60'ı ve {tl(prior_receivable)} eski alacağın %40'ı tahsil edilirse toplam giriş nedir?", tl(collections), "butce", "Cari dönem tahsilatı ile önceki alacaklardan tahsil edilecek tutar toplanır; oranlar kökte verilmiştir.", "Yönetim muhasebesi - nakit bütçesi", "medium", [tl(300_000), tl(340_000), tl(420_000), tl(480_000)]),
    R(f"Cari alımlar {current_purchases:,} TL ve bunun %70'i; önceki borç {prior_payable:,} TL ve bunun %30'u ödenecektir. Toplam nakit çıkışı nedir?".replace(",", "."), f"{tl(current_purchases)} cari alımın %70'i ile {tl(prior_payable)} eski borcun %30'u ödenirse toplam ödeme kaç TL'dir?", tl(payments), "butce", "Cari alımların ödenecek kısmı ile önceki borçların ödenecek kısmı toplanır.", "Yönetim muhasebesi - nakit ödemeleri bütçesi", "medium", [tl(280_000), tl(295_000), tl(355_000), tl(400_000)]),
    R(f"Başlangıç nakdi {begin_cash:,}, girişler {cash_in:,}, çıkışlar {cash_out:,} TL; hedef asgari nakit {min_cash:,} TL'dir. Gereken finansman kaç TL'dir?".replace(",", "."), f"Finansman öncesi nakit {tl(pre_finance)} iken hedef bakiye {tl(min_cash)} ise borçlanma gereği nedir?", tl(financing), "butce", "Finansman öncesi bakiye başlangıç artı girişler eksi çıkışlardır. Bu bakiyeyi hedef asgari tutara çıkaracak finansman gerekir.", "Yönetim muhasebesi - nakit bütçesi", "hard", [tl(50_000), tl(80_000), tl(100_000), tl(180_000)]),
    R(f"Fiilî hacme göre esnek bütçe gideri {flex_cost:,} TL, gerçekleşen gider {actual_cost:,} TL'dir. Harcama sapması nedir?".replace(",", "."), f"Gerçekleşen {tl(actual_cost)} gider ile {tl(flex_cost)} esnek bütçe arasındaki sapma nasıl raporlanır?", f"{tl(spending_variance)} olumsuz", "kontrol", "Gerçek gider esnek bütçeyi aştığı için fark olumsuz harcama sapmasıdır.", "Yönetim muhasebesi - esnek bütçe sapması", "medium", [f"{tl(spending_variance)} olumlu", f"{tl(40_000)} olumsuz", f"{tl(450_000)} olumlu", "Sapma yoktur"]),
    R(f"Fiilî fiyat {actual_price} TL, bütçe fiyatı {budget_price} TL ve fiilî miktar {actual_qty:,} birimdir. Fiyat sapması nedir?".replace(",", "."), f"Fiilî fiyat bütçeyi {actual_price-budget_price} TL aşmış ve {actual_qty:,} birim alınmıştır. Fiyat etkisi nasıl raporlanır?".replace(",", "."), f"{tl(price_variance)} olumsuz", "kontrol", "Fiyat sapması, fiilî miktar ile fiilî ve bütçe fiyatı farkının çarpımıdır; yüksek fiilî fiyat olumsuzdur.", "Yönetim muhasebesi - fiyat sapması", "hard", [f"{tl(price_variance)} olumlu", f"{tl(20_000)} olumsuz", f"{tl(100_000)} olumlu", "Sapma yoktur"]),
    R(f"Fiilî satış {actual_volume:,}, bütçelenen satış {budget_volume:,} birim ve bütçe fiyatı {unit_price} TL'dir. Hacim kaynaklı gelir sapması nedir?".replace(",", "."), f"Bütçeyi {actual_volume-budget_volume:,} birim aşan satışın {unit_price} TL bütçe fiyatıyla etkisi nasıl raporlanır?".replace(",", "."), f"{tl(sales_volume_variance)} olumlu", "kontrol", "Fiilî hacim bütçeyi aştığından fark ile bütçe fiyatının çarpımı olumlu satış hacmi etkisidir.", "Yönetim muhasebesi - satış hacmi sapması", "medium", [f"{tl(sales_volume_variance)} olumsuz", f"{tl(5_000)} olumlu", f"{tl(500_000)} olumlu", "Sapma yoktur"]),
    R(f"Fiilî faaliyet {actual_units:,} birim, birim değişken gider {variable_per_unit} TL ve sabit gider {fixed_cost:,} TL'dir. Esnek bütçe toplamı nedir?".replace(",", "."), f"{actual_units:,} birime uyarlanmış değişken gider ile {tl(fixed_cost)} sabit giderin toplamı kaç TL'dir?".replace(",", "."), tl(flex_total), "butce", "Değişken gider fiilî hacme uyarlanır ve ilgili aralıktaki sabit gider eklenir.", "Yönetim muhasebesi - esnek bütçe", "medium", [tl(252_000), tl(344_000), tl(400_000), tl(492_000)]),
    R(f"Bir yatırım merkezi {investment_profit:,} TL faaliyet kârı ve {investment_base:,} TL yatırım tabanı raporlamıştır. Yatırım getirisi kaçtır?".replace(",", "."), f"{tl(investment_profit)} kârın {tl(investment_base)} yatırım tabanına oranı nedir?", f"%{roi:.0f}", "kontrol", "Yatırım getirisi faaliyet kârının kullanılan yatırım tabanına bölünmesiyle hesaplanır.", "Yönetim muhasebesi - yatırım merkezi", "medium", ["%10", "%12", "%18", "%24"]),
    R(f"Yatırım merkezi kârı {investment_profit:,} TL, yatırım tabanı {investment_base:,} TL ve kökte verilen asgari getiri %12'dir. Artık gelir kaç TL'dir?".replace(",", "."), f"{tl(investment_profit)} kârdan {tl(investment_base)} yatırımın %12 sermaye yükü çıkarılırsa artık gelir nedir?", tl(residual_income), "kontrol", "Artık gelir, faaliyet kârından yatırım tabanının kökte verilen asgari getiri oranıyla çarpımının çıkarılmasıdır.", "Yönetim muhasebesi - artık gelir", "hard", [tl(24_000), tl(48_000), tl(288_000), tl(432_000)]),
    R("Satış bütçesinin üretim ve satın alma bütçelerinden önce hazırlanmasının temel nedeni nedir?", "Ana bütçe akışını başlatan işletme bütçesi kural olarak hangisidir?", "Satış bütçesi diğer faaliyet bütçelerine temel oluşturur", "butce", "Beklenen satış miktarı, üretilecek miktarı ve buna bağlı kaynak gereksinimlerini belirlediği için ana bütçe satış bütçesiyle başlar.", "Yönetim muhasebesi - ana bütçe", "easy"),
    R("Faaliyet hacmi değiştiğinde değişken giderleri gerçekleşen hacme uyarlayan karşılaştırma aracı hangisidir?", "Statik bütçeden farklı olarak fiilî faaliyet düzeyine uyarlanan bütçe hangisidir?", "Esnek bütçe", "butce", "Esnek bütçe, maliyet davranışını kullanarak bütçe tutarlarını fiilî faaliyet düzeyine uyarlar.", "Yönetim muhasebesi - esnek bütçe", "easy"),
    R("Her bütçe kaleminin yeni dönemde sıfırdan gerekçelendirilmesini isteyen yaklaşım hangisidir?", "Önceki dönem ödeneğini otomatik başlangıç kabul etmeyen bütçeleme yöntemi hangisidir?", "Sıfır tabanlı bütçeleme", "butce", "Sıfır tabanlı bütçelemede faaliyet ve kaynak talepleri önceki ödenekten bağımsız yeniden gerekçelendirilir.", "Yönetim muhasebesi - sıfır tabanlı bütçeleme"),
    R("Kaynak tüketimini faaliyet sürücüleri üzerinden bütçelemeyi amaçlayan yöntem hangisidir?", "Faaliyetler ile maliyet sürücülerini bütçenin merkezine alan yaklaşım hangisidir?", "Faaliyet tabanlı bütçeleme", "butce", "Faaliyet tabanlı bütçeleme, çıktılar için gereken faaliyetleri ve bu faaliyetlerin kaynak tüketimini planlar.", "Yönetim muhasebesi - faaliyet tabanlı bütçeleme"),
    R("Bütçe ufkuna her dönem yeni bir ay veya çeyrek eklenerek sabit uzunluk korunmaktadır. Bu yöntem hangisidir?", "Planlama ufkunu sürekli ileri taşıyan bütçe türü hangisidir?", "Kayan bütçe", "butce", "Kayan bütçede tamamlanan dönem çıkarılır ve ufka yeni dönem eklenerek plan güncel tutulur.", "Yönetim muhasebesi - sürekli bütçeleme"),
    R("Alt kademe yöneticilerinin kendi sorumluluk alanlarındaki hedeflerin hazırlanmasına katılması hangi yaklaşımı ifade eder?", "Bilgi paylaşımı ve hedef benimsemeyi artırabilen bütçeleme yaklaşımı hangisidir?", "Katılımcı bütçeleme", "butce", "Katılımcı bütçeleme, bütçeden sorumlu yöneticilerin hedef belirleme sürecine dâhil edilmesidir.", "Yönetim muhasebesi - katılımcı bütçeleme"),
    R("Bir bölüm yöneticisi yalnız kendi bölümündeki maliyetlerin düzeyi üzerinde yetki sahibidir. Bu birim nasıl sınıflanır?", "Yöneticisinin temel sorumluluğu maliyetleri kontrol etmek olan sorumluluk merkezi hangisidir?", "Maliyet merkezi", "kontrol", "Maliyet merkezinde yönetici esas olarak kendi kontrol alanındaki maliyetlerden sorumludur.", "Yönetim muhasebesi - sorumluluk muhasebesi", "easy"),
    R("Bir bölüm yöneticisi hem gelirler hem bölüm maliyetleri üzerinde yetkilidir, fakat kullanılan yatırım tabanını belirlememektedir. Birim hangisidir?", "Gelir ve maliyetlerden sorumlu, yatırım varlıkları üzerinde tam yetkisi olmayan merkez hangisidir?", "Kâr merkezi", "kontrol", "Kâr merkezinin yöneticisi gelir ve maliyet kararlarından sorumludur; yatırım merkezi ayrıca kullanılan varlıklardan sorumludur.", "Yönetim muhasebesi - sorumluluk merkezleri"),
    R("Bölüm yöneticisi gelir, maliyet ve faaliyette kullanılan varlıklar üzerinde karar yetkisine sahiptir. Birim nasıl sınıflanır?", "Kârın yanında yatırım tabanı üzerinde de yetki taşıyan sorumluluk merkezi hangisidir?", "Yatırım merkezi", "kontrol", "Yatırım merkezi yöneticisi kâr unsurlarının yanında kullanılan varlık ve yatırım kararlarından da sorumludur.", "Yönetim muhasebesi - yatırım merkezi"),
    R("Bir yönetici performans raporunda kur ve mevzuat etkisi gibi kontrol edemediği sonuçlardan ayrıştırılmaktadır. Hangi ilke uygulanır?", "Performansın yalnız yöneticinin etkileyebildiği unsurlara dayanmasını isteyen ilke hangisidir?", "Kontrol edilebilirlik ilkesi", "kontrol", "Sorumluluk muhasebesinde yönetici esas olarak önemli ölçüde etkileyebildiği gelir, gider ve varlıklardan sorumlu tutulur.", "Yönetim muhasebesi - kontrol edilebilirlik"),
    R("Yönetici ulaşılması kolay hedef yaratmak için beklenen giderleri bilinçli biçimde yüksek göstermiştir. Bu davranış nasıl adlandırılır?", "Katılımcı bütçelemede tahminlerin kasıtlı gevşetilmesiyle oluşan sorun hangisidir?", "Bütçe gevşekliği", "kontrol", "Bütçe gevşekliği, hedefi kolaylaştırmak amacıyla gelirlerin düşük veya giderlerin yüksek tahmin edilmesidir.", "Yönetim muhasebesi - bütçe davranışı"),
]


def I(stem, correct, distractors, why, ref, difficulty="medium"):
    """Tek, bağımsız bir soru taslağı oluşturur."""
    assert len(distractors) == 4 and len(set(distractors)) == 4
    assert correct not in distractors
    return {
        "stem": stem,
        "correct": correct,
        "distractors": distractors,
        "why": why,
        "ref": ref,
        "difficulty": difficulty,
    }


BASE_CONCEPT_DISTRACTORS = {
    15: [
        "Nakit bütçesi bütün faaliyet bütçelerinden önce hazırlanır",
        "Üretim bütçesi satış tahmininden tamamen bağımsız belirlenir",
        "Direkt işçilik bütçesi satış miktarını tek başına belirler",
        "Finansal tablo bütçeleri yalnız gerçekleşen sonuçları sınıflandırır",
    ],
    16: ["Statik bütçe", "Nakit bütçesi", "Sermaye bütçesi", "Satın alma bütçesi"],
    17: ["Geleneksel artımlı bütçeleme", "Kayan bütçeleme", "Kaizen bütçeleme", "Katılımcı bütçeleme"],
    18: ["Geleneksel artımlı bütçeleme", "Sıfır tabanlı bütçeleme", "Kaizen bütçeleme", "Statik bütçeleme"],
    19: ["Sabit bütçe", "Nakit bütçesi", "Proje bütçesi", "Sermaye bütçesi"],
    20: ["Merkezî bütçeleme", "Statik bütçeleme", "Artımlı bütçeleme", "Sıfır tabanlı bütçeleme"],
    21: ["Gelir merkezi", "Kâr merkezi", "Yatırım merkezi", "Harcama dışı merkez"],
    22: ["Gelir merkezi", "Maliyet merkezi", "Yatırım merkezi", "Harcama merkezi"],
    23: ["Gelir merkezi", "Maliyet merkezi", "Kâr merkezi", "Hizmet merkezi"],
    24: ["Tam maliyet ilkesi", "Dönemsellik ilkesi", "İhtiyatlılık ilkesi", "Tutarlılık ilkesi"],
    25: ["Bütçe fazlası", "Olumlu sapma", "Faaliyet kaldıracı", "Kapasite fazlası"],
}


# İlk 26 sorudan farklı bilinmeyenleri, kararları ve performans yorumlarını ölçer.
FOCUS_VARIANTS = [
    I("Satış bütçesi 480.000 TL ve satış miktarı 1.600 birimdir. Bütçelenen birim satış fiyatı kaç TL'dir?", "300 TL", ["240 TL", "280 TL", "320 TL", "360 TL"], "Birim satış fiyatı, toplam satış bütçesinin bütçelenen satış miktarına bölünmesiyle 480.000 / 1.600 = 300 TL bulunur.", "Yönetim muhasebesi - satış bütçesi", "easy"),
    I("Üretim bütçesi 12.400 birim, satış bütçesi 12.000 birim ve dönem başı mamul stoku 900 birimdir. Hedef dönem sonu mamul stoku kaç birimdir?", "1.300 birim", ["500 birim", "900 birim", "1.700 birim", "2.100 birim"], "Üretim = satış + son stok - ilk stok eşitliğinden son stok 12.400 - 12.000 + 900 = 1.300 birimdir.", "Yönetim muhasebesi - üretim bütçesi"),
    I("Dönemde 18.200 kg direkt madde satın alınmıştır. Dönem başı madde stoku 1.000 kg, hedef dönem sonu stok 2.200 kg ise üretimde kullanılacak madde kaç kg'dır?", "17.000 kg", ["15.000 kg", "16.000 kg", "18.400 kg", "19.400 kg"], "Kullanım = satın alma + ilk stok - son stok olduğundan 18.200 + 1.000 - 2.200 = 17.000 kg'dır.", "Yönetim muhasebesi - direkt ilk madde bütçesi"),
    I("18.600 kg direkt maddenin satın alma bütçesi 744.000 TL'dir. Bütçelenen kilogram fiyatı kaç TL'dir?", "40 TL", ["36 TL", "38 TL", "42 TL", "44 TL"], "Bütçelenen birim alış fiyatı 744.000 TL'nin 18.600 kg'a bölünmesiyle 40 TL olarak hesaplanır.", "Yönetim muhasebesi - direkt ilk madde bütçesi", "easy"),
    I("4.000 birim üretimin direkt işçilik bütçesi 504.000 TL, saatlik ücret 210 TL'dir. Birim başına standart işçilik süresi kaç saattir?", "0,60 saat", ["0,40 saat", "0,50 saat", "0,70 saat", "0,80 saat"], "Toplam işçilik süresi 504.000 / 210 = 2.400 saattir; birim başına süre 2.400 / 4.000 = 0,60 saattir.", "Yönetim muhasebesi - direkt işçilik bütçesi", "hard"),
    I("12.000 birim faaliyet için esnek bütçe gideri 516.000 TL, toplam sabit gider 180.000 TL'dir. Birim başına değişken gider kaç TL'dir?", "28 TL", ["24 TL", "26 TL", "30 TL", "43 TL"], "Toplam değişken gider 516.000 - 180.000 = 336.000 TL; birim değişken gider 336.000 / 12.000 = 28 TL'dir.", "Yönetim muhasebesi - esnek bütçe"),
    I("Cari ayın 600.000 TL'lik satışının %60'ı ve önceki ay alacağının %25'i tahsil edilmiştir. Toplam tahsilat 410.000 TL ise önceki ay alacağı kaç TL'dir?", "200.000 TL", ["160.000 TL", "180.000 TL", "220.000 TL", "250.000 TL"], "Cari satıştan 360.000 TL tahsil edilir. Kalan 50.000 TL önceki alacağın %25'i olduğundan alacak 200.000 TL'dir.", "Yönetim muhasebesi - nakit tahsilat bütçesi", "hard"),
    I("Cari ayın 500.000 TL'lik alımının %70'i ve önceki ay borcunun %35'i ödenmiştir. Toplam ödeme 420.000 TL ise önceki ay borcu kaç TL'dir?", "200.000 TL", ["150.000 TL", "180.000 TL", "220.000 TL", "250.000 TL"], "Cari alımlar için 350.000 TL ödenir. Kalan 70.000 TL önceki borcun %35'i olduğundan borç 200.000 TL'dir.", "Yönetim muhasebesi - nakit ödemeleri bütçesi", "hard"),
    I("Başlangıç nakdi 120.000 TL, dönem içi nakit girişi 560.000 TL ve sağlanan finansman 90.000 TL'dir. Dönem sonu nakdi 100.000 TL olduğuna göre nakit çıkışları kaç TL'dir?", "670.000 TL", ["570.000 TL", "590.000 TL", "650.000 TL", "770.000 TL"], "Nakit eşitliği 120.000 + 560.000 + 90.000 - çıkış = 100.000 biçimindedir; buradan çıkış 670.000 TL olur.", "Yönetim muhasebesi - nakit bütçesi", "hard"),
    I("Gerçekleşen gider 525.000 TL ve harcama sapması 25.000 TL olumsuzdur. Fiilî hacme göre esnek bütçe gideri kaç TL'dir?", "500.000 TL", ["475.000 TL", "525.000 TL", "550.000 TL", "575.000 TL"], "Olumsuz harcama sapması, gerçekleşen giderin esnek bütçeyi aştığını gösterir; esnek bütçe 525.000 - 25.000 = 500.000 TL'dir.", "Yönetim muhasebesi - esnek bütçe sapması"),
    I("Fiilî alış fiyatı 33 TL, fiilî miktar 6.000 birim ve fiyat sapması 18.000 TL olumsuzdur. Bütçelenen birim fiyat kaç TL'dir?", "30 TL", ["27 TL", "29 TL", "31 TL", "36 TL"], "Birim fiyat farkı 18.000 / 6.000 = 3 TL'dir. Sapma olumsuz olduğundan bütçe fiyatı fiilî fiyattan 3 TL düşük, yani 30 TL'dir.", "Yönetim muhasebesi - fiyat sapması", "hard"),
    I("Fiilî satış 14.400 birim, bütçe fiyatı 70 TL ve satış hacmi sapması 84.000 TL olumludur. Bütçelenen satış miktarı kaç birimdir?", "13.200 birim", ["12.000 birim", "12.600 birim", "13.800 birim", "15.600 birim"], "Olumlu hacim farkı 84.000 / 70 = 1.200 birimdir; bütçelenen miktar 14.400 - 1.200 = 13.200 birimdir.", "Yönetim muhasebesi - satış hacmi sapması", "hard"),
    I("10.000 birim fiilî faaliyet için esnek bütçe toplamı 470.000 TL ve birim değişken gider 32 TL'dir. İlgili aralıktaki toplam sabit gider kaç TL'dir?", "150.000 TL", ["120.000 TL", "140.000 TL", "170.000 TL", "320.000 TL"], "Fiilî hacme uyarlanmış değişken gider 10.000 × 32 = 320.000 TL'dir; sabit gider 470.000 - 320.000 = 150.000 TL'dir.", "Yönetim muhasebesi - esnek bütçe"),
    I("Bir yatırım merkezinin yatırım tabanı 3.000.000 TL ve yatırım getirisi %18'dir. Faaliyet kârı kaç TL'dir?", "540.000 TL", ["360.000 TL", "450.000 TL", "600.000 TL", "660.000 TL"], "Faaliyet kârı yatırım tabanı ile yatırım getirisi oranının çarpımıdır: 3.000.000 × %18 = 540.000 TL.", "Yönetim muhasebesi - yatırım getirisi"),
    I("Bir yatırım merkezinin kârı 390.000 TL, yatırım tabanı 2.500.000 TL ve artık geliri 90.000 TL'dir. Kullanılan asgari getiri oranı kaçtır?", "%12", ["%8", "%10", "%15", "%18"], "Sermaye yükü 390.000 - 90.000 = 300.000 TL'dir; 300.000 / 2.500.000 = %12 asgari getiri oranını verir.", "Yönetim muhasebesi - artık gelir", "hard"),
    I("Satış tahmini 2.000 birim azaltılmış, hedef dönem sonu ve dönem başı mamul stokları değiştirilmemiştir. Üretim bütçesi nasıl etkilenir?", "2.000 birim azalır", ["Değişmez", "1.000 birim azalır", "2.000 birim artar", "Stok bilgisi olmadan belirlenemez"], "Stok hedefleri sabitken üretim bütçesindeki değişim satış bütçesindeki değişime eşittir; bu nedenle üretim 2.000 birim azalır.", "Yönetim muhasebesi - ana bütçe ilişkileri"),
    I("Fiilî üretim bütçelenenden yüksek gerçekleşmiştir. Maliyet yöneticisinin harcama performansını hacim etkisinden ayırmak için hangi karşılaştırma kullanılmalıdır?", "Fiilî hacme göre hazırlanmış esnek bütçe ile gerçekleşen gider", ["Statik bütçe ile önceki yıl gideri", "Satış bütçesi ile nakit tahsilatı", "Fiilî üretim ile bütçelenen satış fiyatı", "Sabit gider ile toplam satış geliri"], "Esnek bütçe fiilî hacimde izin verilen gideri gösterir; gerçekleşen giderle karşılaştırılması hacim etkisini ayırarak harcama performansını ortaya koyar.", "Yönetim muhasebesi - esnek bütçe kontrolü"),
    I("Sıfır tabanlı bütçelemeye geçen bir işletmede yönetsel iş yükünü en çok artırması beklenen uygulama hangisidir?", "Faaliyetler için karar paketlerinin hazırlanıp önceliklendirilmesi", ["Önceki yıl bütçesinin otomatik olarak aynen aktarılması", "Yalnız nakit girişlerinin aylık toplamının alınması", "Sabit giderlerin bütün bölümlere eşit dağıtılması", "Gerçekleşen satışların dönem sonunda kaydedilmesi"], "Sıfır tabanlı bütçeleme her faaliyetin gerekliliğini ve kaynak talebini karar paketleriyle yeniden savunmayı gerektirdiğinden zaman ve analiz yükünü artırır.", "Yönetim muhasebesi - sıfır tabanlı bütçeleme"),
    I("Faaliyet tabanlı bütçelemede bir süreç iyileştirmesi işlem sayısını azaltmıştır. Diğer koşullar aynıysa bütçeye ilk yansıması hangisidir?", "Faaliyet sürücüsü miktarı ve buna bağlı kaynak ihtiyacı azalır", ["Bütün sabit maliyetler kendiliğinden ortadan kalkar", "Satış fiyatı işlem sayısıyla aynı oranda zorunlu olarak artar", "Geçmiş dönem bütçesi hiçbir değişiklik olmadan korunur", "Yalnız finansman bütçesindeki faiz oranı değişir"], "Faaliyet tabanlı bütçeleme kaynak ihtiyacını faaliyet sürücüsü miktarından türetir; işlem sayısındaki azalma ilgili faaliyet ve kaynak talebini düşürür.", "Yönetim muhasebesi - faaliyet tabanlı bütçeleme"),
    I("On iki aylık kayan bütçede temmuz ayı tamamlanmış ve bütçe ufkunun uzunluğu korunmak istenmiştir. Yapılması gereken işlem hangisidir?", "Tamamlanan temmuz çıkarılıp sonraki yılın temmuz ayı bütçeye eklenir", ["Kalan on bir ay değiştirilmeden bütçe dönemi kısaltılır", "Bütün bütçe gerçekleşen temmuz rakamlarına eşitlenir", "Yalnız tamamlanan aya ilişkin giderler yeniden tahmin edilir", "Bir sonraki bütçe hazırlığı on iki ay boyunca ertelenir"], "Kayan bütçede tamamlanan dönem ufuktan çıkarılır ve en sona aynı uzunlukta yeni bir dönem eklenerek planlama ufku sürekli korunur.", "Yönetim muhasebesi - kayan bütçe"),
    I("Bölüm yöneticileri bütçe hedeflerinin hazırlanmasına katılmaktadır. Bu yöntemin birlikte doğurabileceği sonuç hangisidir?", "Yerel bilginin kullanılması ve bütçe gevşekliği riskinin ortaya çıkması", ["Bilgi paylaşımının azalması ve bütün hedeflerin merkezden dayatılması", "Yöneticilerin hedefleri benimsemesiyle sapmaların tamamen ortadan kalkması", "Sorumluluk merkezlerinin ve performans ölçümünün gereksiz hâle gelmesi", "Geçmiş yıl rakamlarının her koşulda değişmeden kabul edilmesi"], "Katılım, işi bilen yöneticilerin bilgisini ve hedef benimsemeyi artırabilir; aynı zamanda kolay hedef oluşturmak için bütçe gevşekliği yaratma riski taşır.", "Yönetim muhasebesi - katılımcı bütçeleme"),
    I("Bir maliyet merkezi, bütçelenenden daha yüksek faaliyet hacminde çalışmıştır. Yöneticinin maliyet performansı öncelikle hangi ölçütle değerlendirilmelidir?", "Kontrol edilebilir fiilî maliyetlerin fiilî hacme göre esnek bütçeyle karşılaştırılması", ["Toplam fiilî maliyetin statik bütçeyle doğrudan karşılaştırılması", "Bölüm satış gelirinin yatırım tabanına bölünmesi", "Şirket net kârının geçen yılın satış adediyle karşılaştırılması", "Kontrol edilemeyen kur farklarının yöneticiye bütünüyle yüklenmesi"], "Maliyet merkezi yöneticisi, faaliyet hacmi uyarlanmış bütçeye göre ve etkileyebildiği maliyetler üzerinden değerlendirilmelidir.", "Yönetim muhasebesi - maliyet merkezi performansı"),
    I("Bir bölüm yöneticisi satış fiyatı, satış miktarı ve bölüm giderleri üzerinde yetkili; yatırım varlıkları üzerinde yetkisizdir. En uygun performans ölçüsü hangisidir?", "Kontrol edilebilir bölüm kârı", ["Yalnız üretim miktarı", "Şirketin toplam aktif kârlılığı", "Yalnız yatırım tabanı", "Merkez bankası faiz oranı"], "Yetki alanı gelir ve maliyetleri kapsayan, fakat yatırımları kapsamayan birim kâr merkezidir; performans kontrol edilebilir bölüm kârıyla ilişkilendirilir.", "Yönetim muhasebesi - kâr merkezi performansı"),
    I("Mevcut yatırım getirisi %18 olan bir bölüm, getirisi %14 ve sermaye maliyeti %12 olan projeyi yalnız bölüm oranını düşüreceği için reddetmektedir. Bu sorunu azaltan ölçü hangisidir?", "Artık gelir", ["Satış adedi", "Brüt satışlar", "Direkt işçilik saati", "Statik bütçe sapması"], "Proje asgari getiriyi aşsa da bölümün mevcut oranını düşürür. Artık gelir, asgari sermaye yükünün üzerindeki tutarı ölçerek bu tür eksik yatırım eğilimini azaltabilir.", "Yönetim muhasebesi - yatırım merkezi performansı", "hard"),
    I("Bir bölümün olumsuz sapmasının tamamı, yöneticinin etkileyemediği beklenmedik yasal düzenleme maliyetinden kaynaklanmıştır. Sorumluluk raporunda ne yapılmalıdır?", "Dışsal etki ayrı gösterilip yönetici performansı kontrol edilebilir unsurlarla değerlendirilmelidir", ["Sapmanın tamamı koşulsuz olarak bölüm yöneticisine yüklenmelidir", "Olumsuz sapma olduğu için neden incelemesi yapılmamalıdır", "Bölümün bütün bütçe hedefleri geçmiş yıl rakamlarına çevrilmelidir", "Yalnız şirket satışları kullanılarak maliyet sapması yok sayılmalıdır"], "Kontrol edilebilirlik ilkesi, yöneticinin önemli ölçüde etkileyemediği dışsal sonuçların raporda ayrıştırılmasını gerektirir.", "Yönetim muhasebesi - kontrol edilebilirlik ilkesi"),
    I("Satış yöneticisi hedefe kolay ulaşmak için güvenilir piyasa tahmininden daha düşük satış bütçesi önermiştir. Bu davranışın sonucu hangisidir?", "Gelir tahmininde bütçe gevşekliği oluşur", ["Olumlu fiyat sapması kendiliğinden kesinleşir", "Sıfır tabanlı bütçeleme uygulanmış olur", "Üretim kapasitesi zorunlu olarak artar", "Kontrol edilebilirlik ilkesi tamamen sağlanır"], "Beklenen geliri bilinçli olarak düşük göstermek, ulaşılması kolay bir hedef yaratarak bütçe gevşekliğine neden olur.", "Yönetim muhasebesi - bütçe davranışı"),
]


EXTRAS = [
    I("Ana bütçe hazırlanırken faaliyet bütçeleri tamamlandıktan sonra bu verileri finansal sonuçlara dönüştüren bütçeler grubu hangisidir?", "Nakit bütçesi ile bütçelenmiş finansal tablolar", ["Yalnız satış ve üretim bütçeleri", "Yalnız direkt madde ve işçilik bütçeleri", "Yalnız stok sayım ve mutabakat çizelgeleri", "Yalnız geçmiş dönem gerçekleşme raporları"], "Faaliyet bütçelerinin sonuçları nakit bütçesine ve bütçelenmiş gelir tablosu ile bilanço gibi finansal bütçelere aktarılır.", "Yönetim muhasebesi - ana bütçe"),
    I("Bütçelenmiş gelir tablosunda dönem kârı, bütçelenmiş bilançoda ise dönem sonu nakdi hesaplanmıştır. İki tablo arasındaki nakit tutarı farklıysa ilk kontrol edilmesi gereken yer neresidir?", "Nakit bütçesi ile bütçelenmiş bilanço arasındaki aktarım", ["Satış bütçesindeki birim satış fiyatının alfabetik sırası", "Üretim bütçesindeki mamul adlarının yazım biçimi", "Geçmiş yılın denetim görüşünün paragraf uzunluğu", "Sorumluluk merkezlerinin organizasyon şemasındaki rengi"], "Dönem sonu nakdi nakit bütçesinden bütçelenmiş bilançoya taşındığından farklılık, iki bütçe arasındaki bağlantı ve aktarım kayıtlarında aranır.", "Yönetim muhasebesi - bütçelenmiş finansal tablolar"),
    I("Talep 20.000 birim olmasına karşın darboğaz kapasitesi en çok 16.000 birim üretime izin vermektedir. Ana bütçede hangi yaklaşım izlenmelidir?", "Üretim ve bağlantılı bütçeler uygulanabilir 16.000 birim kapasiteye göre eşgüdümlenmelidir", ["Kapasite kısıtı yokmuş gibi bütün bütçeler 20.000 birimde bırakılmalıdır", "Satış tahmini doğrudan sıfırlanıp bütçe hazırlığı sona erdirilmelidir", "Yalnız sabit gider bütçesi 20.000 birimle çarpılmalıdır", "Darboğaz yalnız dönem sonunda gerçekleşen rapora eklenmelidir"], "Bütçe uygulanabilir olmalıdır; darboğaz üretim, madde, işçilik, satış zamanlaması ve nakit planlarını birlikte etkiler.", "Yönetim muhasebesi - kapasite kısıtı ve bütçeleme"),
    I("Satış bölümü yüksek stok isterken üretim bölümü kapasite kısıtını gerekçe göstermektedir. Ana bütçenin tutarlılığını sağlama görevi öncelikle hangi yapıya aittir?", "Bütçe komitesi", ["Yalnız kasa sorumlusu", "Yalnız dış denetçi", "Yalnız stok sayım ekibi", "Yalnız bilgi işlem servisi"], "Bütçe komitesi, bölümler arası varsayımları ve çatışan hedefleri uzlaştırarak ana bütçenin eşgüdümünü sağlar.", "Yönetim muhasebesi - bütçe organizasyonu"),
    I("Hammadde fiyatındaki beklenen artış daha gerçekleşmeden alternatif tedarik planı hazırlanmıştır. Bu uygulama hangi kontrol türüne örnektir?", "İleriye yönelik kontrol", ["Geri bildirim kontrolü", "Dönem sonu kayıt kontrolü", "Yalnız sonuç raporlaması", "Tarihsel maliyet sınıflaması"], "Sonuç ortaya çıkmadan önce tahmin edilen sapmaya yönelik önlem alınması, ileriye yönelik kontrolün tipik özelliğidir.", "Yönetim muhasebesi - bütçe kontrolü"),
    I("Ana bütçe süreciyle ilgili hangileri doğrudur?\n\nI. Satış bütçesi üretim planını etkiler\n\nII. Üretim planı madde ve işçilik gereksinimlerine temel olur\n\nIII. Nakit bütçesi tahsilat ve ödeme zamanlamasını birleştirir", "I, II ve III", ["Yalnız I", "Yalnız II", "I ve II", "II ve III"], "Satış tahmini üretim ihtiyacını, üretim de kaynak bütçelerini belirler; nakit bütçesi bu planların tahsilat ve ödeme zamanlarını bütünleştirir.", "Yönetim muhasebesi - ana bütçe", "hard"),
    I("Esnek bütçeyle ilgili hangileri doğrudur?\n\nI. Fiilî faaliyet düzeyine uyarlanır\n\nII. Değişken maliyet davranışını dikkate alır\n\nIII. Toplam sabit gider her faaliyet değişiminde aynı oranda değişir", "I ve II", ["Yalnız I", "Yalnız III", "I ve III", "I, II ve III"], "İlk iki öncül esnek bütçeyi tanımlar. Toplam sabit gider, ilgili faaliyet aralığında hacimle orantılı değişmez.", "Yönetim muhasebesi - esnek bütçe", "hard"),
    I("Sorumluluk merkezleriyle ilgili hangileri doğrudur?\n\nI. Maliyet merkezi yöneticisi kontrol edebildiği maliyetlerden sorumludur\n\nII. Kâr merkezi gelir ve maliyetleri birlikte dikkate alır\n\nIII. Yatırım merkezi kullanılan varlıkları da performans ölçümüne katar", "I, II ve III", ["Yalnız I", "Yalnız II", "I ve II", "II ve III"], "Maliyet, kâr ve yatırım merkezleri artan yetki alanlarını yansıtır; yatırım merkezinde gelir ve maliyetlere ek olarak kullanılan varlıklar da değerlendirilir.", "Yönetim muhasebesi - sorumluluk merkezleri", "hard"),
]


def build():
    raw = []
    for idx, rule in enumerate(RULES):
        distractors = rule.get("distractors") or BASE_CONCEPT_DISTRACTORS[idx]
        raw.append(I(
            rule["scenario"], rule["correct"], distractors, rule["why"],
            rule["ref"], rule.get("difficulty", "medium"),
        ))
    raw.extend(FOCUS_VARIANTS)
    raw.extend(EXTRAS)
    assert len(raw) == 60

    letters = balanced_letters(20261004)
    result = []
    for number, (item, answer) in enumerate(zip(raw, letters), 1):
        choices = {answer: item["correct"]}
        other_letters = [letter for letter in "ABCDE" if letter != answer]
        choices.update(dict(zip(other_letters, item["distractors"])))
        assert set(choices) == set("ABCDE") and len(set(choices.values())) == 5
        result.append({
            "id": f"kh-butce-{number:04d}",
            "lessonId": "yonetim_muhasebesi",
            "topicId": "butceleme_planlama_kontrol",
            "question": item["stem"],
            "choices": choices,
            "correctAnswer": answer,
            "explanation": item["why"],
            "source": {
                "kind": "generated",
                "styleRef": "2026 SMMM beş seçenekli test",
                "legislationRef": item["ref"],
            },
            "tags": ["Özgün Soru", "2026 Formatı", "Konu Havuzu", "Bütçeleme, Planlama ve Kontrol"],
            "difficulty": item["difficulty"],
            "updatedAt": "2026-07-17T00:00:00Z",
            "examPeriod": "2026 test sistemine uyumlu özgün soru",
            "legislationVersion": "SMMM kapsamına uyarlanmış yönetim muhasebesi esasları (2026)",
            "sourceUpdatedAt": "2026-07-17T00:00:00Z",
            "isPremium": False,
            "isActive": True,
        })
    return result


def write():
    data = build()
    payload = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    project_root = Path(__file__).resolve().parents[1]
    targets = [
        project_root / "content/yeterlilik/questions_topic_butceleme_planlama_kontrol_2026.json",
        project_root.parent / "smmm_sgs_pratik/assets/content/yeterlilik/questions_topic_butceleme_planlama_kontrol_2026.json",
    ]
    for target in targets:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(payload, encoding="utf-8")
        print(f"yazıldı: {target} ({len(data)} soru)")


if __name__ == "__main__":
    write()
