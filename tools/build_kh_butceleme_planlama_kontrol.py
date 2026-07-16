#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bütçeleme, Planlama ve Kontrol — 60 soru; hesaplar Python ile doğrulanır."""
from topic_pack_builder import write_topic


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


PREMISES = [
    {"stem": "Ana bütçe ilişkileri bakımından hangileri doğrudur?\n\nI. Satış bütçesi üretim ihtiyacını etkiler\n\nII. Üretim bütçesi madde ve işçilik bütçelerine temel olur\n\nIII. Nakit bütçesi tahsilat ve ödeme planlarını birleştirir", "correct": "I, II ve III", "why": "Üç ifade de faaliyet bütçeleri ile finansal bütçeler arasındaki ana bütçe akışını doğru gösterir.", "ref": "Yönetim muhasebesi - ana bütçe"},
    {"stem": "Esnek bütçe bakımından hangileri doğrudur?\n\nI. Fiilî faaliyet düzeyine uyarlanır\n\nII. Değişken maliyet davranışını dikkate alır\n\nIII. Sabit gideri her faaliyet değişiminde birimle aynı oranda değiştirir", "correct": "I ve II", "why": "Esnek bütçe değişken gideri hacme uyarlar; sabit gider ilgili faaliyet aralığında toplam olarak sabit kabul edilir.", "ref": "Yönetim muhasebesi - esnek bütçe"},
    {"stem": "Nakit bütçesi bakımından hangileri doğrudur?\n\nI. Tahsilat zamanını dikkate alır\n\nII. Ödeme zamanını dikkate alır\n\nIII. Finansman gereğini belirlemeye yardımcı olur", "correct": "I, II ve III", "why": "Nakit bütçesi dönemsel giriş ve çıkışları zamanlamasıyla gösterir, hedef bakiye için finansman veya fazlayı belirler.", "ref": "Yönetim muhasebesi - nakit bütçesi"},
    {"stem": "Sorumluluk merkezleri bakımından hangileri doğrudur?\n\nI. Maliyet merkezi yöneticisi esas olarak maliyetlerden sorumludur\n\nII. Kâr merkezi gelir ve maliyetleri birlikte izler\n\nIII. Yatırım merkezi kullanılan varlıkları da dikkate alır", "correct": "I ve II", "why": "Üçüncü ifade de doğrudur; hedef cevap dağılımı için üçüncü öncül aşağıda değiştirilecektir.", "ref": "Yönetim muhasebesi - sorumluluk merkezleri"},
    {"stem": "Bütçeleme yöntemleri bakımından hangileri doğrudur?\n\nI. Sıfır tabanlı bütçe kalemleri yeniden gerekçelendirir\n\nII. Faaliyet tabanlı bütçe kaynak tüketimini faaliyetlerle ilişkilendirir\n\nIII. Kayan bütçe planlama ufkunu sabit bir bitiş tarihinde dondurur", "correct": "I ve II", "why": "İlk iki ifade doğrudur; kayan bütçe ufku yeni dönem ekleyerek ileri taşır.", "ref": "Yönetim muhasebesi - bütçeleme yaklaşımları"},
    {"stem": "Bütçe kontrolü bakımından hangileri doğrudur?\n\nI. Sapmanın nedeni araştırılır\n\nII. Kontrol edilebilirlik gözetilir\n\nIII. Her olumlu sapma nedenine bakılmadan başarılı sayılır", "correct": "I ve II", "why": "Kontrol süreci sapmanın nedenini ve yöneticinin etkisini değerlendirir; sapmanın işareti tek başına performans hükmü için yeterli değildir.", "ref": "Yönetim muhasebesi - bütçe kontrolü"},
    {"stem": "Katılımcı bütçeleme bakımından hangileri doğrudur?\n\nI. Yerel bilgiyi planlamaya taşıyabilir\n\nII. Hedef benimsemeyi artırabilir\n\nIII. Bütçe gevşekliği riskini tamamen ortadan kaldırır", "correct": "I ve II", "why": "Katılım bilgi ve benimsemeyi güçlendirebilir; ancak bütçe gevşekliği riskini ortadan kaldırmaz.", "ref": "Yönetim muhasebesi - bütçe davranışı"},
    {"stem": "Yatırım merkezi performansı bakımından hangileri doğrudur?\n\nI. Yatırım getirisi kâr ile yatırım tabanını ilişkilendirir\n\nII. Artık gelir sermaye yükünü dikkate alabilir\n\nIII. Yalnız satış adedi tüm yatırım kararlarını ölçmeye yeterlidir", "correct": "I ve II", "why": "Yatırım getirisi ve artık gelir, kârı kullanılan varlıklarla ilişkilendirir; satış adedi tek başına yeterli değildir.", "ref": "Yönetim muhasebesi - yatırım merkezi performansı"},
]

PREMISES[3]["stem"] = "Sorumluluk merkezleri bakımından hangileri doğrudur?\n\nI. Maliyet merkezi yöneticisi esas olarak maliyetlerden sorumludur\n\nII. Kâr merkezi gelir ve maliyetleri birlikte izler\n\nIII. Yatırım merkezi kullanılan varlıkları değerlendirme dışı bırakır"
PREMISES[3]["why"] = "Maliyet ve kâr merkezlerine ilişkin ilk iki ifade doğrudur; yatırım merkezi kullanılan varlıkları da değerlendirir."


if __name__ == "__main__":
    write_topic(
        lesson_id="yonetim_muhasebesi", topic_id="butceleme_planlama_kontrol",
        label="Bütçeleme, Planlama ve Kontrol", slug="butceleme_planlama_kontrol",
        prefix="kh-butce", seed=20261004, legislation_version="Yapısal yönetim muhasebesi esasları (2026)",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG,
    )
