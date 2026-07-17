# -*- coding: utf-8 -*-
"""Yeterlilik KONU HAVUZU — Yönetim Muhasebesi / Maliyet-Hacim-Kâr.

60 özgün soru = 3×20. Maliyet davranışı, başabaş ve hedef kâr,
çok ürünlü satış karması, güvenlik payı, faaliyet kaldıracı ve duyarlılık.
Hesapların tamamı Python değişkenleriyle üretilir ve assert ile doğrulanır.
"""
import json
import random
import re
from pathlib import Path

L, T, LBL = "yonetim_muhasebesi", "maliyet_hacim_kar", "Maliyet-Hacim-Kâr Analizi"
PREFIX, SEED = "kh-yon-mhk", 20260908
CONTENT_ROOT = Path(__file__).resolve().parents[3]
PROJECTS_ROOT = CONTENT_ROOT.parent
FILENAME = "questions_topic_maliyet_hacim_kar_2026.json"
OUTS = (
    PROJECTS_ROOT / "smmm_sgs_pratik" / "assets" / "content" / "yeterlilik" / FILENAME,
    CONTENT_ROOT / "content" / "yeterlilik" / FILENAME,
)
UPDATED_AT = "2026-07-17T00:00:00Z"
LEGISLATION_VERSION = "2026 SMMM Yeterlilik Yönetim Muhasebesi kapsamı"

Q = []


def q(stem, correct, distractors, why, ref, difficulty="medium"):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors,
                  why=why, ref=ref, difficulty=difficulty))


def tr(value):
    if isinstance(value, float) and abs(value - round(value)) < 1e-9:
        value = round(value)
    return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".").removesuffix(",00")


# ── A. Model yapısı, maliyet davranışı ve seçenek karşılaştırması (15) ────
q("Maliyet-Hacim-Kâr modelinde 'geçerli faaliyet aralığı' sınırlaması neden önemlidir?",
  "Maliyet davranışı varsayımları yalnız belirli hacim aralığında geçerlidir",
  ["Satış fiyatı ile toplam sabit maliyetin bütün üretim düzeylerinde aynı tutarda olmasını zorunlu kılar",
   "İşletmenin yalnız başabaş noktasında üretim yapabileceğini ve başka hacim seçemeyeceğini gösterir",
   "Değişken maliyetlerin her hacim artışında mutlaka sıfıra ineceğini kabul etmeyi gerektirir",
   "Üretim kapasitesi değişse bile toplam ve birim maliyet ilişkilerinin sonsuza kadar aynı kalmasını sağlar"],
  "Birim değişken maliyetin ve toplam sabit maliyetin sabitliği, kapasite yapısının değişmediği belirli bir faaliyet aralığı için varsayılır.",
  "Yönetim muhasebesi - MHK analizinde geçerli faaliyet aralığı", "easy")

high_units, high_cost, low_units, low_cost = 9_000, 410_000, 5_000, 250_000
variable = (high_cost-low_cost)/(high_units-low_units)
fixed = high_cost-high_units*variable
assert (variable, fixed) == (40, 50_000)
q(f"Bakım gideri {tr(low_units)} makine saatinde {tr(low_cost)} TL, {tr(high_units)} saatte {tr(high_cost)} TL olmuştur. Yüksek-düşük noktalar yöntemiyle saat başına değişken bakım gideri kaç TL'dir?",
  f"{tr(variable)} TL",
  [f"{tr(high_cost/high_units)} TL yüksek hacimdeki toplam giderin yalnız yüksek saate bölündüğü tutar",
   f"{tr(low_cost/low_units)} TL düşük hacimdeki toplam giderin yalnız düşük saate bölündüğü tutar",
   f"{tr((high_cost-low_cost)/high_units)} TL gider farkının yalnız yüksek hacme bölündüğü tutar",
   f"{tr((high_cost+low_cost)/(high_units+low_units))} TL iki gözlemin toplamlarından ortalama oran üretildiği tutar"],
  f"Değişken gider, gider farkının hacim farkına bölünmesiyle bulunur: ({tr(high_cost)} − {tr(low_cost)}) / ({tr(high_units)} − {tr(low_units)}) = {tr(variable)} TL/saat.",
  "Yönetim muhasebesi - yüksek-düşük noktalar yöntemiyle değişken maliyet tahmini")

q(f"Önceki bakım gideri verilerinde saat başına değişken gider {tr(variable)} TL ise tahmini aylık sabit bakım gideri kaç TL'dir?",
  f"{tr(fixed)} TL",
  [f"{tr(low_cost-low_units)} TL düşük hacim ile toplam giderin doğrudan çıkarıldığı tutar",
   f"{tr(high_cost-low_cost)} TL iki faaliyet düzeyindeki toplam gider farkının sabit sayıldığı tutar",
   f"{tr(low_units*variable)} TL düşük hacimdeki toplam değişken giderin sabit gider kabul edildiği tutar",
   f"{tr(high_cost-high_units)} TL yüksek hacim ile giderin birimsiz biçimde çıkarıldığı tutar"],
  f"Yüksek düzey kullanılırsa sabit gider {tr(high_cost)} − ({tr(high_units)} × {tr(variable)}) = {tr(fixed)} TL'dir; düşük düzey de aynı sonucu verir.",
  "Yönetim muhasebesi - karma maliyet fonksiyonunda sabit bileşenin tahmini")

q("Doğrusal Maliyet-Hacim-Kâr modeline ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Birim satış fiyatının geçerli aralıkta sabit olduğu varsayılır\n\nII. Toplam sabit maliyetin geçerli aralıkta değişmediği varsayılır\n\nIII. Birim değişken maliyetin her ek birimde farklılaştığı varsayılır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Basit doğrusal model, geçerli aralıkta satış fiyatını ve birim değişken maliyeti sabit; toplam sabit maliyeti değişmez kabul eder. Üçüncü ifade bu varsayımın tersidir.",
  "Yönetim muhasebesi - doğrusal MHK analizinin temel varsayımları")

q("Katkı payı esaslı gelir tablosunda üretimle birlikte değişmeyen fabrika kirası hangi bölümde gösterilir?",
  "Toplam katkı payından sonra sabit maliyet olarak",
  ["Satış gelirinden önce değişken satış indirimi olarak ve hasılatın bir unsuru şeklinde",
   "Her mamulün birim değişken maliyetine faaliyet hacminden bağımsız biçimde eklenerek",
   "Yalnız dönem sonu stokuna dağıtılan değişken üretim maliyeti olarak ve kârdan sonra",
   "Satış miktarı arttıkça aynı oranda yükselen değişken yönetim gideri olarak"],
  "Katkı yaklaşımında satışlardan bütün değişken maliyetler çıkarılarak katkı payı; ardından sabit maliyetler çıkarılarak faaliyet kârı bulunur.",
  "Yönetim muhasebesi - katkı payı esaslı gelir tablosu sınıflandırması", "easy")

price, variable_unit, lower_fixed, threshold, upper_fixed = 100, 60, 220_000, 5_000, 260_000
cm = price-variable_unit
lower_candidate = lower_fixed/cm
upper_candidate = upper_fixed/cm
assert lower_candidate == 5_500 and upper_candidate == 6_500 and lower_candidate > threshold
q(f"Birim katkı payı {tr(cm)} TL'dir. Toplam sabit maliyet {tr(threshold)} birime kadar {tr(lower_fixed)} TL, bu düzey aşılırsa {tr(upper_fixed)} TL olacaktır. Basamaklı kapasite dikkate alındığında geçerli başabaş miktarı kaç birimdir?",
  f"{tr(upper_candidate)} birim",
  [f"{tr(lower_candidate)} birim düşük sabit giderle hesaplandığı hâlde kapasite eşiğini aşan geçersiz sonuç",
   f"{tr(threshold)} birim basamağın başladığı noktanın doğrudan başabaş kabul edildiği sonuç",
   f"{tr(upper_fixed/price)} birim üst basamak sabit giderinin satış fiyatına bölündüğü sonuç",
   f"{tr(lower_fixed/price)} birim alt basamak sabit giderinin katkı yerine satış fiyatına bölündüğü sonuç"],
  f"Alt basamak hesabı {tr(lower_candidate)} birimle {tr(threshold)} sınırını aştığı için tutarsızdır. Üst basamakta {tr(upper_fixed)} / {tr(cm)} = {tr(upper_candidate)} birim geçerlidir.",
  "Yönetim muhasebesi - basamaklı sabit maliyet altında başabaş analizi", "hard")

price, current_var, current_fixed, auto_var, auto_fixed = 130, 70, 300_000, 40, 480_000
indifference = (auto_fixed-current_fixed)/(current_var-auto_var)
assert indifference == 6_000
q(f"Mevcut süreçte birim değişken maliyet {tr(current_var)} TL ve sabit maliyet {tr(current_fixed)} TL'dir. Otomasyon seçeneğinde değişken maliyet {tr(auto_var)} TL'ye düşecek, sabit maliyet {tr(auto_fixed)} TL olacaktır. Satış fiyatı {tr(price)} TL iken iki süreç hangi hacimde aynı faaliyet kârını verir?",
  f"{tr(indifference)} birim",
  [f"{tr((auto_fixed-current_fixed)/(price-auto_var))} birim sabit farkının otomasyon katkısına bölündüğü sonuç",
   f"{tr(current_fixed/(price-current_var))} birim yalnız mevcut sürecin başabaş miktarının kullanıldığı sonuç",
   f"{tr(auto_fixed/(price-auto_var))} birim yalnız otomasyon sürecinin başabaş miktarının kullanıldığı sonuç",
   f"{tr((auto_fixed+current_fixed)/(current_var-auto_var))} birim sabit maliyet farkı yerine toplamının kullanıldığı sonuç"],
  f"Eşitlikte yalnız farklılaşan maliyetler kullanılır: ({tr(auto_fixed)} − {tr(current_fixed)}) / ({tr(current_var)} − {tr(auto_var)}) = {tr(indifference)} birim.",
  "Yönetim muhasebesi - maliyet yapıları arasında kayıtsızlık hacmi", "hard")

a_fixed, a_var, b_fixed, b_var = 90_000, 14, 150_000, 8
indifference = (b_fixed-a_fixed)/(a_var-b_var)
assert indifference == 10_000
q(f"Dağıtım seçeneği A'nın sabit gideri {tr(a_fixed)} TL, birim gideri {tr(a_var)} TL; B'nin sabit gideri {tr(b_fixed)} TL, birim gideri {tr(b_var)} TL'dir. İki seçeneğin toplam maliyetleri kaç birimde eşitlenir?",
  f"{tr(indifference)} birim",
  [f"{tr((b_fixed-a_fixed)/a_var)} birim sabit farkının yalnız A'nın birim giderine bölündüğü sonuç",
   f"{tr((b_fixed-a_fixed)/b_var)} birim sabit farkının yalnız B'nin birim giderine bölündüğü sonuç",
   f"{tr((b_fixed+a_fixed)/(a_var-b_var))} birim sabit giderlerin farkı yerine toplamının kullanıldığı sonuç",
   f"{tr(a_fixed/(a_var-b_var))} birim yalnız A'nın sabit giderinin birim farkına bölündüğü sonuç"],
  f"{tr(a_fixed)} + {tr(a_var)}Q = {tr(b_fixed)} + {tr(b_var)}Q eşitliğinden Q = {tr(b_fixed-a_fixed)} / {tr(a_var-b_var)} = {tr(indifference)} birimdir.",
  "Yönetim muhasebesi - alternatif maliyet fonksiyonlarının kayıtsızlık noktası")

q("Faaliyet kaldıracı ve maliyet yapısına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Sabit maliyet ağırlığı arttıkça başabaş yakınında faaliyet kaldıracı yükselebilir\n\nII. Satışlar başabaş noktasının üzerine çıktıkça faaliyet kaldıracı genellikle azalır\n\nIII. Yüksek faaliyet kaldıracı satış dalgalanmasının kâra etkisini azaltır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Sabit maliyet ağırlığı kârı satış değişimine daha duyarlı kılar. Başabaştan uzaklaştıkça kâr büyür ve katkı payı/kâr oranı düşer; yüksek kaldıraç etkiyi azaltmaz, büyütür.",
  "Yönetim muhasebesi - maliyet yapısı ve faaliyet kaldıracı")

total_fixed, noncash_depr, cm_unit = 360_000, 120_000, 48
cash_fixed = total_fixed-noncash_depr
cash_be = cash_fixed/cm_unit
assert (cash_fixed, cash_be) == (240_000, 5_000)
q(f"Toplam sabit maliyet {tr(total_fixed)} TL olup bunun {tr(noncash_depr)} TL'si nakit çıkışı yaratmayan amortismandır. Birim katkı payı {tr(cm_unit)} TL ise nakit başabaş miktarı kaç birimdir?",
  f"{tr(cash_be)} birim",
  [f"{tr(total_fixed/cm_unit)} birim amortismanın da nakit sabit gider sayıldığı muhasebe başabaş miktarı",
   f"{tr(noncash_depr/cm_unit)} birim yalnız amortismanın katkı payına bölündüğü sonuç",
   f"{tr((total_fixed+noncash_depr)/cm_unit)} birim amortismanın sabit maliyete ikinci kez eklendiği sonuç",
   f"{tr(cash_fixed/(cm_unit/2))} birim katkı payının gerekçesiz biçimde yarıya indirildiği sonuç"],
  f"Nakit sabit gider {tr(total_fixed)} − {tr(noncash_depr)} = {tr(cash_fixed)} TL'dir. Nakit başabaş {tr(cash_fixed)} / {tr(cm_unit)} = {tr(cash_be)} birim olur.",
  "Yönetim muhasebesi - nakit başabaş noktası")

hours = 7_000
estimated_cost = fixed+variable*hours
assert estimated_cost == 330_000
q(f"Yüksek-düşük yöntemiyle bakım maliyeti Y = {tr(fixed)} + {tr(variable)}X biçiminde tahmin edilmiştir. {tr(hours)} makine saatindeki toplam bakım maliyeti kaç TL'dir?",
  f"{tr(estimated_cost)} TL",
  [f"{tr(variable*hours)} TL sabit giderin maliyet fonksiyonundan çıkarıldığı tutar",
   f"{tr(fixed*hours)} TL sabit giderin her makine saati için yeniden yüklendiği tutar",
   f"{tr((fixed+variable)*hours)} TL sabit gider ile birim giderin toplanıp hacimle çarpıldığı tutar",
   f"{tr(fixed+hours)} TL makine saati ile sabit giderin birimsiz biçimde toplandığı tutar"],
  f"Tahmini maliyet {tr(fixed)} + ({tr(variable)} × {tr(hours)}) = {tr(estimated_cost)} TL'dir.",
  "Yönetim muhasebesi - karma maliyet fonksiyonuyla maliyet tahmini")

old_price, variable_unit, old_units, new_price = 120, 72, 5_400, 108
old_contribution = (old_price-variable_unit)*old_units
new_cm = new_price-variable_unit
required_units = old_contribution/new_cm
assert old_contribution == 259_200 and required_units == 7_200
q(f"İşletme {tr(old_units)} birimi {tr(old_price)} TL'den satmakta, birim değişken maliyeti {tr(variable_unit)} TL'dir. Fiyat {tr(new_price)} TL'ye indirilirse aynı toplam katkı payını korumak için kaç birim satılmalıdır?",
  f"{tr(required_units)} birim",
  [f"{tr(old_units)} birim fiyat değişiminin katkı payını etkilemediği varsayılan sonuç",
   f"{tr(old_contribution/(old_price-variable_unit))} birim eski katkı payıyla yeniden bölme yapılan sonuç",
   f"{tr(old_contribution/new_price)} birim toplam katkının satış fiyatına bölündüğü sonuç",
   f"{tr(old_units*old_price/new_price)} birim yalnız satış gelirinin korunmasına dayanan sonuç"],
  f"Mevcut katkı {tr(old_units)} × ({tr(old_price)} − {tr(variable_unit)}) = {tr(old_contribution)} TL'dir. Yeni birim katkı {tr(new_cm)} TL; gerekli hacim {tr(old_contribution)} / {tr(new_cm)} = {tr(required_units)} birimdir.",
  "Yönetim muhasebesi - fiyat indirimi sonrası katkı payını koruyan satış hacmi", "hard")

old_price, new_price, variable_unit, old_units, new_units = 90, 96, 54, 8_000, 7_200
old_cm_total = (old_price-variable_unit)*old_units
new_cm_total = (new_price-variable_unit)*new_units
increase = new_cm_total-old_cm_total
assert (old_cm_total, new_cm_total, increase) == (288_000, 302_400, 14_400)
q(f"Fiyat {tr(old_price)} TL iken {tr(old_units)} birim satılmaktadır. Fiyat {tr(new_price)} TL'ye çıkarılırsa satışın {tr(new_units)} birime düşeceği tahmin edilmektedir. Birim değişken maliyet {tr(variable_unit)} TL ve sabit gider değişmiyorsa kâr nasıl etkilenir?",
  f"{tr(increase)} TL artar",
  [f"{tr(new_cm_total)} TL artar; yeni toplam katkının tamamı değişim kabul edilmiştir",
   f"{tr(old_cm_total)} TL azalır; eski toplam katkı doğrudan kayıp sayılmıştır",
   f"{tr((new_price-old_price)*new_units)} TL artar; hacim düşüşünün katkı etkisi dışlanmıştır",
   f"{tr((old_units-new_units)*(old_price-variable_unit))} TL azalır; fiyat artışının yararı dışlanmıştır"],
  f"Eski toplam katkı {tr(old_cm_total)} TL, yeni toplam katkı {tr(new_cm_total)} TL'dir. Sabit gider değişmediğinden kâr {tr(increase)} TL artar.",
  "Yönetim muhasebesi - fiyat-hacim değişiminin katkı payıyla değerlendirilmesi", "hard")

q("Maliyet-Hacim-Kâr modelinin kullanım sınırlarına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Geçerli aralık dışındaki kapasite değişimleri modeli bozabilir\n\nII. Satış karması değişse bile ağırlıklı katkı payı kesinlikle aynı kalır\n\nIII. Fiyat ve maliyetlerin doğrusal olmadığı durumda model uyarlanmalıdır",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "Yalnız II"],
  "Kapasite basamakları ile doğrusal olmayan fiyat ve maliyetler basit modeli sınırlar. Çok ürünlü işletmede satış karması değişirse ağırlıklı katkı payı da değişebilir.",
  "Yönetim muhasebesi - MHK analizinin sınırlılıkları")

q("Hacim indirimi nedeniyle birim satış fiyatının satış miktarı arttıkça düşmesi, basit doğrusal MHK modelinde hangi varsayımı ihlal eder?",
  "Birim satış fiyatının sabitliği varsayımını",
  ["Toplam sabit maliyetin yalnız nakit giderlerden oluştuğu varsayımını",
   "Üretim miktarının her zaman başabaş miktarına eşit olduğu varsayımını",
   "Katkı payı oranının yalnız sabit giderlerden hesaplandığı varsayımını",
   "Bütün maliyetlerin geçmişte oluşmuş batmış maliyet olduğu varsayımını"],
  "Doğrusal model geçerli aralıkta birim satış fiyatını sabit kabul eder. Miktara bağlı fiyat basamakları için parçalı veya senaryolu analiz gerekir.",
  "Yönetim muhasebesi - doğrusal MHK modelinde sabit satış fiyatı varsayımı")


# ── B. Başabaş, hedef kâr ve vergi etkisi (15) ────────────────────────────
price, production_var, commission_rate, fixed = 200, 110, 0.10, 350_000
commission = price*commission_rate
cm = price-production_var-commission
planned_units = 5_000
max_fixed = planned_units*cm
assert (commission, cm, max_fixed) == (20, 70, 350_000)
q(f"İşletme yeni satış kanalında {tr(planned_units)} mamul için toplam {tr(planned_units*price)} TL gelir beklemektedir. Mamul başına üretim gideri {tr(production_var)} TL, kanal komisyonu gelirin %{tr(commission_rate*100)}'udur. Kanalın zarar etmemesi için kanala özgü sabit gider en çok kaç TL olabilir?",
  f"{tr(max_fixed)} TL",
  [f"{tr(planned_units*(price-production_var))} TL satış komisyonunun ilgili maliyetten dışlandığı sınır",
   f"{tr(planned_units*production_var)} TL toplam değişken üretim giderinin sabit gider sınırı sayıldığı tutar",
   f"{tr(planned_units*(production_var+commission))} TL toplam değişken maliyetin katkı payı kabul edildiği tutar",
   f"{tr(planned_units*commission)} TL yalnız toplam komisyonun sabit gider sınırı sayıldığı tutar"],
  f"Mamul başına komisyon {tr(commission)} TL, katkı {tr(price)} − {tr(production_var)} − {tr(commission)} = {tr(cm)} TL'dir. {tr(planned_units)} mamulün {tr(max_fixed)} TL katkısı sabit giderin üst sınırıdır.",
  "Yönetim muhasebesi - satış komisyonu altında başabaş sabit gider sınırı")

fixed, cm, target = 420_000, 70, 140_000
required = (fixed+target)/cm
assert required == 8_000
q(f"Bir işletmenin sabit maliyeti {tr(fixed)} TL, birim katkı payı {tr(cm)} TL'dir. Vergi öncesi {tr(target)} TL faaliyet kârı için gereken satış miktarı kaç birimdir?",
  f"{tr(required)} birim",
  [f"{tr(fixed/cm)} birim yalnız sabit maliyeti karşılayan başabaş miktarı",
   f"{tr(target/cm)} birim yalnız hedef kârı karşılayan ve sabit maliyeti dışlayan miktar",
   f"{tr((fixed-target)/cm)} birim hedef kârın sabit maliyetten çıkarıldığı miktar",
   f"{tr((fixed+target)/(cm/2))} birim katkı payının gerekçesiz biçimde yarıya indirildiği miktar"],
  f"Gerekli toplam katkı {tr(fixed)} + {tr(target)} = {tr(fixed+target)} TL'dir. {tr(cm)} TL birim katkıyla {tr(required)} birim satılmalıdır.",
  "Yönetim muhasebesi - vergi öncesi hedef kâr için satış miktarı")

fixed, cm, after_tax_target, tax_rate = 360_000, 60, 126_000, 0.30
pretax_target = after_tax_target/(1-tax_rate)
planned_units = 9_000
pretax_profit = planned_units*cm-fixed
supported_after_tax = pretax_profit*(1-tax_rate)
assert abs(pretax_target-180_000) < 1e-6 and pretax_profit == 180_000 and abs(supported_after_tax-126_000) < 1e-6
q(f"Yönetim {tr(planned_units)} birimlik planı değerlendirmektedir. Bu hacimde toplam katkı payı {tr(planned_units*cm)} TL, dönem sabit maliyeti {tr(fixed)} TL ve vergi oranı kökte verilen %{tr(tax_rate*100)}'dur. Planın sağlayabileceği vergi sonrası faaliyet kârı kaç TL'dir?",
  f"{tr(supported_after_tax)} TL",
  [f"{tr(pretax_profit)} TL vergi öncesi faaliyet kârının net kâr kabul edildiği sonuç",
   f"{tr(planned_units*cm)} TL toplam katkı payının sabit maliyet ve vergi düşülmeden kullanıldığı sonuç",
   f"{tr(pretax_profit*tax_rate)} TL yalnız hesaplanan vergi giderinin net kâr sayıldığı sonuç",
   f"{tr(fixed*(1-tax_rate))} TL sabit maliyetin vergi sonrası kâr kabul edildiği sonuç"],
  f"Vergi öncesi kâr {tr(planned_units*cm)} − {tr(fixed)} = {tr(pretax_profit)} TL'dir. Vergi sonrası tutar {tr(pretax_profit)} × (1 − %{tr(tax_rate*100)}) = {tr(supported_after_tax)} TL olur.",
  "Yönetim muhasebesi - planlanan hacmin desteklediği vergi sonrası kâr", "hard")

fixed, cmr, after_tax_target, tax_rate = 500_000, 0.40, 210_000, 0.30
pretax_target = after_tax_target/(1-tax_rate)
sales = (fixed+pretax_target)/cmr
assert pretax_target == 300_000 and sales == 2_000_000
q(f"Sabit maliyet {tr(fixed)} TL, katkı payı oranı %{tr(cmr*100)} ve vergi oranı kökte verilen %{tr(tax_rate*100)}'dur. Vergi sonrası {tr(after_tax_target)} TL kâr için gerekli satış hasılatı kaç TL'dir?",
  f"{tr(sales)} TL",
  [f"{tr((fixed+after_tax_target)/cmr)} TL vergi sonrası hedefin brütleştirilmeden kullanıldığı satış",
   f"{tr(fixed/cmr)} TL yalnız başabaş satış hasılatını gösteren sonuç",
   f"{tr((fixed+pretax_target)*(1-cmr))} TL gerekli katkının değişken maliyet oranıyla çarpıldığı sonuç",
   f"{tr((fixed+after_tax_target/tax_rate)/cmr)} TL hedefin vergi oranına yanlış bölündüğü sonuç"],
  f"Vergi öncesi hedef {tr(pretax_target)} TL'dir. Gerekli satış ({tr(fixed)} + {tr(pretax_target)}) / %{tr(cmr*100)} = {tr(sales)} TL olur.",
  "Yönetim muhasebesi - vergi sonrası hedef kâr için satış tutarı", "hard")

q("Başabaş ve hedef kâr analizine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Vergi sonrası hedef kâr, verilen vergi oranıyla vergi öncesine çevrilir\n\nII. Başabaş noktasında toplam katkı payı toplam sabit maliyete eşittir\n\nIII. Hedef kâr hesabında sabit maliyet ile vergi öncesi hedef birlikte karşılanır",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Vergi sonrası hedef önce brütleştirilir; başabaşta kâr sıfır olduğundan katkı sabit maliyeti karşılar; pozitif hedefte gerekli katkıya hedef kâr da eklenir.",
  "Yönetim muhasebesi - başabaş ve vergi sonrası hedef kâr ilişkileri")

units, price, variable_unit, fixed = 11_500, 80, 48, 280_000
sales = units*price
variable_total = units*variable_unit
total_cm = sales-variable_total
cmr = total_cm/sales
be_sales = fixed/cmr
margin = sales-be_sales
profit = total_cm-fixed
assert (sales, variable_total, total_cm, cmr, be_sales, margin, profit) == (920_000, 552_000, 368_000, 0.40, 700_000, 220_000, 88_000)
q(f"Bütçelenen net satışlar {tr(sales)} TL, toplam değişken maliyet {tr(variable_total)} TL ve dönem sabit maliyeti {tr(fixed)} TL'dir. Bütçelenen satışların başabaş satış hasılatını aşan kısmı kaç TL'dir?",
  f"{tr(margin)} TL",
  [f"{tr(total_cm)} TL toplam katkı payının güvenlik payı kabul edildiği sonuç",
   f"{tr(be_sales)} TL başabaş satış hasılatının aşan kısım kabul edildiği sonuç",
   f"{tr(profit)} TL faaliyet kârının güvenlik payı tutarı sayıldığı sonuç",
   f"{tr(fixed)} TL dönem sabit maliyetinin güvenlik payı kabul edildiği sonuç"],
  f"Katkı oranı ({tr(sales)} − {tr(variable_total)}) / {tr(sales)} = %{tr(cmr*100)}'tır. Başabaş satış {tr(fixed)} / %{tr(cmr*100)} = {tr(be_sales)} TL; aşan kısım {tr(margin)} TL'dir.",
  "Yönetim muhasebesi - bütçelenen satışlardan güvenlik payı tutarı")

base_fixed, fixed_increase, target, cm = 300_000, 60_000, 90_000, 45
required = (base_fixed+fixed_increase+target)/cm
assert required == 10_000
q(f"Mevcut sabit maliyet {tr(base_fixed)} TL iken yeni kapasite yıllık {tr(fixed_increase)} TL ek sabit gider doğuracaktır. Birim katkı payı {tr(cm)} TL ve hedef kâr {tr(target)} TL ise gereken satış miktarı kaç birimdir?",
  f"{tr(required)} birim",
  [f"{tr((base_fixed+target)/cm)} birim kapasitenin ek sabit giderinin dışlandığı miktar",
   f"{tr((fixed_increase+target)/cm)} birim mevcut sabit maliyetin dışlandığı miktar",
   f"{tr((base_fixed+fixed_increase)/cm)} birim hedef kârın dışlandığı başabaş miktarı",
   f"{tr((base_fixed-fixed_increase+target)/cm)} birim ek sabit giderin toplamdan çıkarıldığı miktar"],
  f"Gerekli katkı {tr(base_fixed)} + {tr(fixed_increase)} + {tr(target)} = {tr(base_fixed+fixed_increase+target)} TL'dir. {tr(cm)} TL katkıyla {tr(required)} birim gerekir.",
  "Yönetim muhasebesi - kapasite artışı sonrası hedef kâr hacmi")

old_price, old_var, old_fixed = 150, 90, 360_000
new_price, new_var, new_fixed = 144, 84, 420_000
old_be = old_fixed/(old_price-old_var)
new_be = new_fixed/(new_price-new_var)
increase = new_be-old_be
assert (old_be, new_be, increase) == (6_000, 7_000, 1_000)
q(f"Eski yapıda fiyat {tr(old_price)} TL, değişken maliyet {tr(old_var)} TL, sabit maliyet {tr(old_fixed)} TL'dir. Yeni yapıda değerler sırasıyla {tr(new_price)}, {tr(new_var)} ve {tr(new_fixed)} TL olacaktır. Başabaş miktarı nasıl değişir?",
  f"{tr(increase)} birim artar",
  [f"{tr(old_be)} birim artar; eski başabaş miktarının tamamı değişim sayılmıştır",
   f"{tr(new_be)} birim artar; yeni başabaş miktarının tamamı değişim sayılmıştır",
   f"{tr(increase)} birim azalır; eski ve yeni sonuçlar ters yönde karşılaştırılmıştır",
   "Değişmez; fiyat ile değişken maliyet aynı tutarda azaldığı için sabit maliyet artışı dışlanmıştır"],
  f"Eski başabaş {tr(old_fixed)} / {tr(old_price-old_var)} = {tr(old_be)}; yeni başabaş {tr(new_fixed)} / {tr(new_price-new_var)} = {tr(new_be)} birimdir. Artış {tr(increase)} birimdir.",
  "Yönetim muhasebesi - fiyat, değişken ve sabit maliyet değişiminin başabaşa etkisi", "hard")

cash_fixed, cmr = 270_000, 0.45
cash_sales = cash_fixed/cmr
assert cash_sales == 600_000
q(f"İşletmenin nakit çıkışı yaratan sabit giderleri {tr(cash_fixed)} TL, katkı payı oranı %{tr(cmr*100)}'tir. Nakit başabaş satış hasılatı kaç TL'dir?",
  f"{tr(cash_sales)} TL",
  [f"{tr(cash_fixed/(1-cmr))} TL katkı payı yerine değişken maliyet oranının kullanıldığı sonuç",
   f"{tr(cash_fixed*cmr)} TL nakit sabit giderin katkı oranıyla çarpıldığı sonuç",
   f"{tr(cash_fixed)} TL sabit giderin doğrudan satış hasılatı kabul edildiği sonuç",
   f"{tr(cash_fixed/cmr+cash_fixed)} TL sabit giderin hesaplanan satışa ikinci kez eklendiği sonuç"],
  f"Nakit başabaş satışları {tr(cash_fixed)} / %{tr(cmr*100)} = {tr(cash_sales)} TL'dir.",
  "Yönetim muhasebesi - katkı payı oranıyla nakit başabaş satış tutarı")

fixed, investment, return_rate, cm = 240_000, 800_000, 0.15, 45
target = investment*return_rate
required = (fixed+target)/cm
assert target == 120_000 and required == 8_000
q(f"İşletme {tr(investment)} TL yatırımı üzerinden %{tr(return_rate*100)} faaliyet kârı hedeflemektedir. Sabit maliyet {tr(fixed)} TL, birim katkı payı {tr(cm)} TL ise hedef için kaç birim satılmalıdır?",
  f"{tr(required)} birim",
  [f"{tr(fixed/cm)} birim yatırım getirisi hedefinin dışlandığı başabaş miktarı",
   f"{tr(target/cm)} birim sabit maliyetin dışlandığı hedef kâr miktarı",
   f"{tr((fixed-target)/cm)} birim yatırım getirisi hedefinin sabit maliyetten çıkarıldığı miktar",
   f"{tr((fixed+investment)/cm)} birim hedef getiri yerine yatırımın tamamının kâr sayıldığı miktar"],
  f"Hedef kâr {tr(investment)} × %{tr(return_rate*100)} = {tr(target)} TL'dir. Gereken hacim ({tr(fixed)} + {tr(target)}) / {tr(cm)} = {tr(required)} birimdir.",
  "Yönetim muhasebesi - yatırım getirisi hedefi için satış hacmi")

price, prod_var, commission_rate, fixed, target = 125, 65, 0.08, 300_000, 100_000
commission = price*commission_rate
cm = price-prod_var-commission
required = (fixed+target)/cm
assert commission == 10 and cm == 50 and required == 8_000
q(f"Fiyat {tr(price)} TL, değişken üretim maliyeti {tr(prod_var)} TL ve satış komisyonu fiyatın %{tr(commission_rate*100)}'udur. Sabit maliyet {tr(fixed)} TL iken {tr(target)} TL hedef kâr için kaç birim satılmalıdır?",
  f"{tr(required)} birim",
  [f"{tr((fixed+target)/(price-prod_var))} birim değişken satış komisyonunun dışlandığı miktar",
   f"{tr(fixed/cm)} birim hedef kârın dışlandığı başabaş miktarı",
   f"{tr(target/cm)} birim sabit maliyetin dışlandığı yalnız hedef kâr miktarı",
   f"{tr((fixed+target)/(prod_var+commission))} birim toplam değişken maliyetin katkı sayıldığı miktar"],
  f"Komisyon {tr(commission)} TL ve birim katkı {tr(cm)} TL'dir. Gereken hacim ({tr(fixed)} + {tr(target)}) / {tr(cm)} = {tr(required)} birimdir.",
  "Yönetim muhasebesi - satış komisyonu altında hedef kâr hacmi")

price, variable_unit, lower_fixed, threshold, upper_fixed, target = 140, 80, 270_000, 6_000, 390_000, 120_000
cm = price-variable_unit
lower_candidate = (lower_fixed+target)/cm
upper_candidate = (upper_fixed+target)/cm
assert lower_candidate == 6_500 and upper_candidate == 8_500 and lower_candidate > threshold
q(f"Birim katkı {tr(cm)} TL'dir. Sabit maliyet {tr(threshold)} birime kadar {tr(lower_fixed)} TL, daha yüksek hacimde {tr(upper_fixed)} TL olacaktır. {tr(target)} TL hedef kâr için geçerli satış miktarı kaç birimdir?",
  f"{tr(upper_candidate)} birim",
  [f"{tr(lower_candidate)} birim alt basamakla hesaplandığı hâlde eşik üzerinde kalan geçersiz sonuç",
   f"{tr(upper_fixed/cm)} birim üst basamakta hedef kârın dışlandığı başabaş miktarı",
   f"{tr((lower_fixed+target)/price)} birim gerekli katkının satış fiyatına bölündüğü sonuç",
   f"{tr((upper_fixed-target)/cm)} birim hedef kârın sabit giderden çıkarıldığı sonuç"],
  f"Alt basamak sonucu {tr(lower_candidate)} birimle {tr(threshold)} eşiğini aşar. Üst basamakta ({tr(upper_fixed)} + {tr(target)}) / {tr(cm)} = {tr(upper_candidate)} birim gerekir.",
  "Yönetim muhasebesi - basamaklı sabit maliyet altında hedef kâr", "hard")

fixed, variable_ratio = 456_000, 0.62
cmr = 1-variable_ratio
be_sales = fixed/cmr
assert abs(cmr-0.38) < 1e-9 and be_sales == 1_200_000
q(f"Değişken maliyetler net satışların %{tr(variable_ratio*100)}'sidir ve toplam sabit maliyet {tr(fixed)} TL'dir. Başabaş net satış hasılatı kaç TL'dir?",
  f"{tr(be_sales)} TL",
  [f"{tr(fixed/variable_ratio)} TL katkı oranı yerine değişken maliyet oranının kullanıldığı sonuç",
   f"{tr(fixed*cmr)} TL sabit maliyetin katkı payı oranıyla çarpıldığı sonuç",
   f"{tr(fixed)} TL sabit maliyetin doğrudan satış tutarı kabul edildiği sonuç",
   f"{tr(fixed/(1+variable_ratio))} TL oranların toplamının paydada kullanıldığı sonuç"],
  f"Katkı payı oranı %100 − %{tr(variable_ratio*100)} = %{tr(cmr*100)}'dir. Başabaş satış {tr(fixed)} / %{tr(cmr*100)} = {tr(be_sales)} TL olur.",
  "Yönetim muhasebesi - değişken maliyet oranından başabaş satış tutarı")

q("Vergi ve hedef kâr analizine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Vergi sonrası hedef, oran kökte verildiğinde 1 eksi vergi oranına bölünür\n\nII. Vergi oranı yükseldikçe aynı net hedef için gereken vergi öncesi kâr artar\n\nIII. Vergi oranı değişikliği sıfır faaliyet kârlı temel başabaş miktarını artırır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Net hedefin brütleştirilmesi vergi oranına bağlıdır. Temel başabaş noktasında hedef faaliyet kârı sıfır olduğundan vergi sonrası hedef dönüşümü gerekmez.",
  "Yönetim muhasebesi - vergi sonrası hedef kârın brütleştirilmesi")

current_loss, target_profit, cm = 72_000, 96_000, 24
additional = (current_loss+target_profit)/cm
assert additional == 7_000
q(f"İşletme mevcut satış düzeyinde {tr(current_loss)} TL zarar etmektedir. Birim başına ek katkı {tr(cm)} TL olacaksa zararı kapatıp ayrıca {tr(target_profit)} TL kâra ulaşmak için kaç ek birim satılmalıdır?",
  f"{tr(additional)} birim",
  [f"{tr(current_loss/cm)} birim yalnız mevcut zararı kapatan ek hacim",
   f"{tr(target_profit/cm)} birim yalnız hedef kârı sağlayan ve zararı dışlayan hacim",
   f"{tr((target_profit-current_loss)/cm)} birim zararın hedef kârdan çıkarıldığı hacim",
   f"{tr((target_profit+current_loss)/(cm/2))} birim katkı payının yarıya indirildiği hacim"],
  f"Ek katkı önce {tr(current_loss)} TL zararı, sonra {tr(target_profit)} TL hedefi karşılamalıdır. ({tr(current_loss)} + {tr(target_profit)}) / {tr(cm)} = {tr(additional)} birim gerekir.",
  "Yönetim muhasebesi - mevcut zarardan hedef kâra ek satış hacmi")


# ── C. Çok ürünlü satış karması (15) ──────────────────────────────────────
a_ratio, a_cm, b_ratio, b_cm = 2, 30, 3, 20
bundle_cm = a_ratio*a_cm+b_ratio*b_cm
assert bundle_cm == 120
q(f"Satış karması her {tr(a_ratio)} adet A'ya karşı {tr(b_ratio)} adet B'dir. A'nın birim katkısı {tr(a_cm)} TL, B'nin {tr(b_cm)} TL olduğuna göre bileşik paketin katkı payı kaç TL'dir?",
  f"{tr(bundle_cm)} TL",
  [f"{tr(a_cm+b_cm)} TL ürün katkılarının karma adetleri dikkate alınmadan toplandığı sonuç",
   f"{tr((a_cm+b_cm)/(a_ratio+b_ratio))} TL katkıların basit ortalamasının paket katkısı sayıldığı sonuç",
   f"{tr(a_ratio*a_cm)} TL yalnız A ürünlerinin paket katkısının kullanıldığı sonuç",
   f"{tr(b_ratio*b_cm)} TL yalnız B ürünlerinin paket katkısının kullanıldığı sonuç"],
  f"Bir bileşik paket {tr(a_ratio)} A ve {tr(b_ratio)} B içerir. Paket katkısı {tr(a_ratio)} × {tr(a_cm)} + {tr(b_ratio)} × {tr(b_cm)} = {tr(bundle_cm)} TL'dir.",
  "Yönetim muhasebesi - birim satış karmasında bileşik katkı payı")

fixed = 600_000
bundles = fixed/bundle_cm
a_units, b_units = bundles*a_ratio, bundles*b_ratio
assert (bundles, a_units, b_units) == (5_000, 10_000, 15_000)
q(f"Önceki {tr(a_ratio)} A : {tr(b_ratio)} B satış karması korunacaktır. Bileşik katkı {tr(bundle_cm)} TL ve sabit maliyet {tr(fixed)} TL ise başabaşta A ve B satışları sırasıyla kaç birimdir?",
  f"{tr(a_units)} A ve {tr(b_units)} B",
  [f"{tr(bundles)} A ve {tr(bundles)} B; paket sayısının her üründe birer adet sayıldığı sonuç",
   f"{tr(b_units)} A ve {tr(a_units)} B; karma oranlarının ürünlere ters uygulandığı sonuç",
   f"{tr(fixed/a_cm)} A ve {tr(fixed/b_cm)} B; sabit maliyetin her ürün için ayrı ayrı karşılandığı sonuç",
   f"{tr(a_units+b_units)} A ve 0 B; bütün bileşik hacmin tek ürüne aktarıldığı sonuç"],
  f"Başabaş paket sayısı {tr(fixed)} / {tr(bundle_cm)} = {tr(bundles)}'dir. Bunun {tr(a_ratio)} ve {tr(b_ratio)} katı sırasıyla {tr(a_units)} A ile {tr(b_units)} B verir.",
  "Yönetim muhasebesi - bileşik birimle çok ürünlü başabaş miktarı", "hard")

a_sales_share, a_cmr, b_sales_share, b_cmr = 0.60, 0.50, 0.40, 0.25
weighted_cmr = a_sales_share*a_cmr+b_sales_share*b_cmr
assert abs(weighted_cmr-0.40) < 1e-9
q(f"Satış hasılatının %{tr(a_sales_share*100)}'ı katkı oranı %{tr(a_cmr*100)} olan A'dan, kalanı katkı oranı %{tr(b_cmr*100)} olan B'den gelmektedir. Ağırlıklı ortalama katkı payı oranı nedir?",
  f"%{tr(weighted_cmr*100)}",
  [f"%{tr((a_cmr+b_cmr)/2*100)} iki katkı oranının satış payları dikkate alınmadan basit ortalaması",
   f"%{tr(a_sales_share*a_cmr*100)} yalnız A ürününün ağırlıklı katkısının kullanıldığı sonuç",
   f"%{tr(b_sales_share*b_cmr*100)} yalnız B ürününün ağırlıklı katkısının kullanıldığı sonuç",
   f"%{tr((a_sales_share*a_cmr-b_sales_share*b_cmr)*100)} iki ağırlıklı katkının birbirinden çıkarıldığı sonuç"],
  f"Ağırlıklı oran %{tr(a_sales_share*100)} × %{tr(a_cmr*100)} + %{tr(b_sales_share*100)} × %{tr(b_cmr*100)} = %{tr(weighted_cmr*100)}'tır.",
  "Yönetim muhasebesi - satış hasılatı karmasında ağırlıklı katkı payı oranı")

fixed = 480_000
be_sales = fixed/weighted_cmr
assert be_sales == 1_200_000
q(f"Ağırlıklı katkı payı oranı %{tr(weighted_cmr*100)} ve toplam ortak sabit maliyet {tr(fixed)} TL'dir. Satış karması korunursa çok ürünlü başabaş satış hasılatı kaç TL'dir?",
  f"{tr(be_sales)} TL",
  [f"{tr(fixed/(1-weighted_cmr))} TL katkı yerine ağırlıklı değişken maliyet oranının kullanıldığı sonuç",
   f"{tr(fixed*weighted_cmr)} TL sabit maliyetin ağırlıklı katkı oranıyla çarpıldığı sonuç",
   f"{tr(fixed)} TL sabit maliyetin doğrudan başabaş satışı kabul edildiği sonuç",
   f"{tr(fixed/weighted_cmr+fixed)} TL sabit maliyetin satış tutarına ikinci kez eklendiği sonuç"],
  f"Çok ürünlü başabaş satış {tr(fixed)} / %{tr(weighted_cmr*100)} = {tr(be_sales)} TL'dir.",
  "Yönetim muhasebesi - ağırlıklı katkı oranıyla çok ürünlü başabaş satışı")

q("Çok ürünlü Maliyet-Hacim-Kâr analizine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Başabaş hesabı satış karmasının sabit kaldığını varsayar\n\nII. Adet karmasında bileşik birim katkısı kullanılabilir\n\nIII. Hasılat karmasında ağırlıklı katkı payı oranı kullanılabilir",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Çok ürünlü analiz, belirli satış karmasını temel alır. Karma adetle tanımlanıyorsa bileşik katkı; gelir paylarıyla tanımlanıyorsa ağırlıklı katkı oranı kullanılabilir.",
  "Yönetim muhasebesi - çok ürünlü MHK analizinde satış karması")

q("Diğer koşullar sabitken satış karmasının katkı payı oranı daha yüksek ürüne yönelmesi hangi sonucu doğurur?",
  "Ağırlıklı katkı oranını yükseltip başabaş satışını düşürür",
  ["Ağırlıklı katkı oranını düşürüp başabaş satış hasılatını zorunlu olarak yükseltir",
   "Toplam sabit maliyeti otomatik olarak sıfırlayıp başabaş analizini gereksiz kılar",
   "Her ürünün birim değişken maliyetini aynı tutara getirip satış karmasını etkisiz kılar",
   "Katkı payı oranlarını değiştirmeden yalnız muhasebe kayıtlarının sırasını değiştirir"],
  "Yüksek katkı oranlı ürünün gelir payı arttığında ağırlıklı katkı oranı yükselir. Aynı sabit maliyet daha düşük toplam satışla karşılanabilir.",
  "Yönetim muhasebesi - satış karması değişiminin başabaşa etkisi")

a_sales, a_cmr, b_sales, b_cmr, fixed = 900_000, 0.40, 600_000, 0.30, 420_000
total_cm = a_sales*a_cmr+b_sales*b_cmr
profit = total_cm-fixed
assert total_cm == 540_000 and profit == 120_000
q(f"A ürününün satışları {tr(a_sales)} TL ve katkı oranı %{tr(a_cmr*100)}; B'nin satışları {tr(b_sales)} TL ve katkı oranı %{tr(b_cmr*100)}'dur. Ortak sabit maliyet {tr(fixed)} TL ise toplam faaliyet kârı kaç TL'dir?",
  f"{tr(profit)} TL",
  [f"{tr(total_cm)} TL ortak sabit maliyetin toplam katkıdan düşülmediği sonuç",
   f"{tr(a_sales*a_cmr)} TL yalnız A ürününün katkısının kullanıldığı sonuç",
   f"{tr(b_sales*b_cmr)} TL yalnız B ürününün katkısının kullanıldığı sonuç",
   f"{tr(total_cm+fixed)} TL ortak sabit maliyetin katkıya eklendiği sonuç"],
  f"A katkısı {tr(a_sales*a_cmr)} TL, B katkısı {tr(b_sales*b_cmr)} TL; toplam {tr(total_cm)} TL'dir. {tr(fixed)} TL sabit maliyet sonrası kâr {tr(profit)} TL olur.",
  "Yönetim muhasebesi - çok ürünlü katkı payı gelir tablosu")

x_ratio, x_cm, y_ratio, y_cm = 1, 50, 2, 25
bundle_cm = x_ratio*x_cm+y_ratio*y_cm
fixed, target = 500_000, 200_000
bundles = (fixed+target)/bundle_cm
y_units = bundles*y_ratio
assert bundle_cm == 100 and bundles == 7_000 and y_units == 14_000
q(f"Satış karması {tr(x_ratio)} X : {tr(y_ratio)} Y; birim katkılar sırasıyla {tr(x_cm)} ve {tr(y_cm)} TL'dir. Sabit maliyet {tr(fixed)} TL ve hedef kâr {tr(target)} TL ise kaç Y ürünü satılmalıdır?",
  f"{tr(y_units)} birim",
  [f"{tr(bundles)} birim paket sayısının Y satış miktarı kabul edildiği sonuç",
   f"{tr((fixed+target)/y_cm)} birim sabit maliyet ile hedefin yalnız Y tarafından karşılandığı sonuç",
   f"{tr(fixed/bundle_cm*y_ratio)} birim hedef kârın dışlandığı Y başabaş miktarı",
   f"{tr(bundles*(x_ratio+y_ratio))} birim toplam ürün sayısının Y miktarı kabul edildiği sonuç"],
  f"Bileşik katkı {tr(x_cm)} + 2 × {tr(y_cm)} = {tr(bundle_cm)} TL'dir. ({tr(fixed)} + {tr(target)}) / {tr(bundle_cm)} = {tr(bundles)} paket; Y miktarı {tr(y_units)} birimdir.",
  "Yönetim muhasebesi - bileşik birimle çok ürünlü hedef kâr", "hard")

a_cm, b_cm, fixed = 60, 30, 540_000
old_bundle = a_cm+b_cm
old_bundles = fixed/old_bundle
new_bundle = a_cm+2*b_cm
new_bundles = fixed/new_bundle
new_total_units = new_bundles*3
assert (old_bundle, old_bundles, new_bundle, new_bundles, new_total_units) == (90, 6_000, 120, 4_500, 13_500)
q(f"A ve B'nin birim katkıları {tr(a_cm)} ve {tr(b_cm)} TL, sabit maliyet {tr(fixed)} TL'dir. Satış karması 1 A : 1 B'den 1 A : 2 B'ye dönerse yeni karmadaki başabaş toplam ürün adedi kaç olur?",
  f"{tr(new_total_units)} birim",
  [f"{tr(new_bundles)} birim bileşik paket sayısının toplam fiziksel adet kabul edildiği sonuç",
   f"{tr(old_bundles*2)} birim eski karmanın başabaş toplam adedinin değişmediği sonuç",
   f"{tr(fixed/a_cm)} birim bütün sabit maliyetin yalnız A katkısıyla karşılandığı sonuç",
   f"{tr(fixed/b_cm)} birim bütün sabit maliyetin yalnız B katkısıyla karşılandığı sonuç"],
  f"Yeni paketin katkısı {tr(a_cm)} + 2 × {tr(b_cm)} = {tr(new_bundle)} TL; {tr(fixed)} / {tr(new_bundle)} = {tr(new_bundles)} paket gerekir. Her paket 3 ürün olduğundan toplam {tr(new_total_units)} birimdir.",
  "Yönetim muhasebesi - satış karması değişince toplam başabaş adedi", "hard")

a_ratio, a_cm, b_ratio, b_cm, fixed = 3, 28, 2, 18, 360_000
bundle_cm = a_ratio*a_cm+b_ratio*b_cm
bundles = fixed/bundle_cm
a_units, b_units = bundles*a_ratio, bundles*b_ratio
assert (bundle_cm, bundles, a_units, b_units) == (120, 3_000, 9_000, 6_000)
q(f"Satış karması {tr(a_ratio)} A : {tr(b_ratio)} B, katkılar {tr(a_cm)} ve {tr(b_cm)} TL, sabit maliyet {tr(fixed)} TL'dir. Başabaş satış miktarları hangi seçenekte doğru verilmiştir?",
  f"{tr(a_units)} A ve {tr(b_units)} B",
  [f"{tr(b_units)} A ve {tr(a_units)} B; karma oranlarının ürünlere ters uygulandığı sonuç",
   f"{tr(bundles)} A ve {tr(bundles)} B; paket sayısının her ürün miktarı sayıldığı sonuç",
   f"{tr(fixed/a_cm)} A ve {tr(fixed/b_cm)} B; sabit maliyetin iki kez karşılandığı sonuç",
   f"{tr(a_units+b_units)} A ve 0 B; toplam karma hacminin yalnız A'ya verildiği sonuç"],
  f"Bileşik katkı 3 × {tr(a_cm)} + 2 × {tr(b_cm)} = {tr(bundle_cm)} TL; başabaş {tr(bundles)} pakettir. Böylece {tr(a_units)} A ve {tr(b_units)} B satılır.",
  "Yönetim muhasebesi - adet satış karmasında ürün bazlı başabaş miktarları")

a_share, a_cmr, b_share, b_cmr = 0.70, 0.45, 0.30, 0.20
weighted_cmr = a_share*a_cmr+b_share*b_cmr
fixed, target = 450_000, 150_000
sales = (fixed+target)/weighted_cmr
assert abs(weighted_cmr-0.375) < 1e-9 and sales == 1_600_000
q(f"Hasılat karması %{tr(a_share*100)} A ve %{tr(b_share*100)} B; katkı oranları sırasıyla %{tr(a_cmr*100)} ve %{tr(b_cmr*100)}'dir. Sabit maliyet {tr(fixed)} TL, hedef kâr {tr(target)} TL ise toplam satış hedefi kaç TL'dir?",
  f"{tr(sales)} TL",
  [f"{tr((fixed+target)/((a_cmr+b_cmr)/2))} TL katkı oranlarının basit ortalamasıyla bulunan satış",
   f"{tr(fixed/weighted_cmr)} TL hedef kârı dışlayan çok ürünlü başabaş satışı",
   f"{tr(target/weighted_cmr)} TL sabit maliyeti dışlayan yalnız hedef kâr satışı",
   f"{tr((fixed+target)*(1-weighted_cmr))} TL gerekli katkının değişken maliyet oranıyla çarpıldığı sonuç"],
  f"Ağırlıklı oran %{tr(a_share*100)} × %{tr(a_cmr*100)} + %{tr(b_share*100)} × %{tr(b_cmr*100)} = %{tr(weighted_cmr*100)}'tir. Satış ({tr(fixed)} + {tr(target)}) / %{tr(weighted_cmr*100)} = {tr(sales)} TL'dir.",
  "Yönetim muhasebesi - hasılat karmasında çok ürünlü hedef kâr", "hard")

q("Çok ürünlü başabaş analizine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Satış karması değişirse ağırlıklı katkı payı değişebilir\n\nII. Toplam başabaş için ortak sabit giderin her ürüne keyfî dağıtılması zorunludur\n\nIII. Bileşik birim yaklaşımı adet bazlı sabit karmada kullanılabilir",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "Yalnız II"],
  "Karma, ağırlıklı katkıyı ve başabaşı etkiler. Toplam işletme başabaşı için ortak sabit gideri ürünlere keyfî dağıtmak gerekmez; sabit adet karmasında bileşik paket kullanılabilir.",
  "Yönetim muhasebesi - çok ürünlü başabaşta karma ve ortak sabit maliyet")

a_share, a_cm, b_share, b_cm = 0.40, 50, 0.60, 20
weighted_unit_cm = a_share*a_cm+b_share*b_cm
assert weighted_unit_cm == 32
q(f"Toplam birim satışların %{tr(a_share*100)}'ı birim katkısı {tr(a_cm)} TL olan A, kalanı katkısı {tr(b_cm)} TL olan B'dir. Ağırlıklı ortalama birim katkı payı kaç TL'dir?",
  f"{tr(weighted_unit_cm)} TL",
  [f"{tr((a_cm+b_cm)/2)} TL satış payları dikkate alınmadan basit ortalama alınan sonuç",
   f"{tr(a_share*a_cm)} TL yalnız A ürününün ağırlıklı katkısının kullanıldığı sonuç",
   f"{tr(b_share*b_cm)} TL yalnız B ürününün ağırlıklı katkısının kullanıldığı sonuç",
   f"{tr(a_cm+b_cm)} TL iki ürün katkısının bir bileşik adet tanımlanmadan toplandığı sonuç"],
  f"Ağırlıklı birim katkı %{tr(a_share*100)} × {tr(a_cm)} + %{tr(b_share*100)} × {tr(b_cm)} = {tr(weighted_unit_cm)} TL'dir.",
  "Yönetim muhasebesi - birim satış paylarıyla ağırlıklı katkı payı")

total_units, a_cm, b_cm = 10_000, 40, 20
old_a_share, new_a_share = 0.50, 0.30
old_total = total_units*(old_a_share*a_cm+(1-old_a_share)*b_cm)
new_total = total_units*(new_a_share*a_cm+(1-new_a_share)*b_cm)
decrease = old_total-new_total
assert (old_total, new_total, decrease) == (300_000, 260_000, 40_000)
q(f"Toplam satış {tr(total_units)} birimdir. A ve B katkıları {tr(a_cm)} ve {tr(b_cm)} TL'dir. A'nın satış payı %{tr(old_a_share*100)}'den %{tr(new_a_share*100)}'a düşerken toplam hacim ve sabit maliyet değişmezse faaliyet kârı nasıl etkilenir?",
  f"{tr(decrease)} TL azalır",
  [f"{tr(old_total)} TL azalır; eski toplam katkının tamamı kayıp sayılmıştır",
   f"{tr(new_total)} TL azalır; yeni toplam katkının tamamı değişim sayılmıştır",
   f"{tr(total_units*(old_a_share-new_a_share)*a_cm)} TL azalır; B'ye kayan birimlerin katkısı dışlanmıştır",
   "Değişmez; toplam birim sayısı aynı kaldığı için ürün katkılarının farklılığı göz ardı edilmiştir"],
  f"Eski katkı {tr(old_total)} TL, yeni katkı {tr(new_total)} TL'dir. Sabit maliyet değişmediğinden kâr {tr(decrease)} TL azalır.",
  "Yönetim muhasebesi - satış karması kaymasının faaliyet kârına etkisi", "hard")

expected_sales, weighted_cmr, fixed = 2_400_000, 0.35, 630_000
be_sales = fixed/weighted_cmr
margin = expected_sales-be_sales
assert be_sales == 1_800_000 and margin == 600_000
q(f"Çok ürünlü işletmenin beklenen toplam satışı {tr(expected_sales)} TL, ağırlıklı katkı oranı %{tr(weighted_cmr*100)} ve sabit maliyeti {tr(fixed)} TL'dir. Satış karması korunursa güvenlik payı tutarı kaç TL'dir?",
  f"{tr(margin)} TL",
  [f"{tr(be_sales)} TL başabaş satış tutarının güvenlik payı kabul edildiği sonuç",
   f"{tr(expected_sales*weighted_cmr)} TL beklenen toplam katkı payının güvenlik tutarı sayıldığı sonuç",
   f"{tr(expected_sales-fixed)} TL satışlardan yalnız sabit maliyetin çıkarıldığı sonuç",
   f"{tr(expected_sales-be_sales+fixed)} TL sabit maliyetin güvenlik payına yeniden eklendiği sonuç"],
  f"Başabaş satış {tr(fixed)} / %{tr(weighted_cmr*100)} = {tr(be_sales)} TL'dir. Güvenlik payı {tr(expected_sales)} − {tr(be_sales)} = {tr(margin)} TL olur.",
  "Yönetim muhasebesi - çok ürünlü işletmede güvenlik payı")


# ── D. Güvenlik payı, faaliyet kaldıracı ve duyarlılık (15) ───────────────
be_sales, desired_margin_rate = 1_200_000, 0.25
required_sales = be_sales/(1-desired_margin_rate)
assert required_sales == 1_600_000
q(f"Başabaş satış hasılatı {tr(be_sales)} TL'dir. İşletme satışlarının %{tr(desired_margin_rate*100)}'i kadar güvenlik payı oranı istiyorsa toplam satış hasılatı kaç TL olmalıdır?",
  f"{tr(required_sales)} TL",
  [f"{tr(be_sales/(desired_margin_rate))} TL başabaş satışın güvenlik oranına doğrudan bölündüğü sonuç",
   f"{tr(be_sales*(1+desired_margin_rate))} TL başabaş satışa yalnız yüzde eklenerek bulunan sonuç",
   f"{tr(be_sales*desired_margin_rate)} TL güvenlik tutarının toplam satış kabul edildiği sonuç",
   f"{tr(be_sales/(1+desired_margin_rate))} TL başabaş satışın bir artı oranına bölündüğü sonuç"],
  f"Güvenlik oranı = 1 − Başabaş/Satış olduğundan satış = {tr(be_sales)} / (1 − %{tr(desired_margin_rate*100)}) = {tr(required_sales)} TL'dir.",
  "Yönetim muhasebesi - hedef güvenlik payı oranından satış tutarı", "hard")

be_units, desired_margin_rate = 6_000, 0.40
required_units = be_units/(1-desired_margin_rate)
assert required_units == 10_000
q(f"Başabaş miktarı {tr(be_units)} birim olan işletme, fiilî miktarın %{tr(desired_margin_rate*100)}'i kadar güvenlik payı hedeflemektedir. Bu oran için kaç birim satmalıdır?",
  f"{tr(required_units)} birim",
  [f"{tr(be_units/desired_margin_rate)} birim başabaş miktarının güvenlik oranına bölündüğü sonuç",
   f"{tr(be_units*(1+desired_margin_rate))} birim başabaşa yalnız yüzde eklenerek bulunan sonuç",
   f"{tr(be_units*desired_margin_rate)} birim güvenlik miktarının toplam satış sayıldığı sonuç",
   f"{tr(be_units/(1+desired_margin_rate))} birim başabaşın bir artı oranına bölündüğü sonuç"],
  f"Başabaş, satışların %{tr((1-desired_margin_rate)*100)}'ına eşit olmalıdır. {tr(be_units)} / %{tr((1-desired_margin_rate)*100)} = {tr(required_units)} birimdir.",
  "Yönetim muhasebesi - hedef güvenlik payı oranından satış miktarı", "hard")

contribution, profit, sales_change = 420_000, 140_000, 0.08
dol = contribution/profit
profit_change_rate = dol*sales_change
profit_increase = profit*profit_change_rate
assert dol == 3 and abs(profit_change_rate-0.24) < 1e-9 and profit_increase == 33_600
q(f"Toplam katkı payı {tr(contribution)} TL, faaliyet kârı {tr(profit)} TL'dir. İlgili aralıkta satışların %{tr(sales_change*100)} artması beklenirse faaliyet kaldıracı yaklaşımıyla kâr artışı kaç TL olur?",
  f"{tr(profit_increase)} TL",
  [f"{tr(profit*sales_change)} TL satış değişiminin kaldıraç uygulanmadan doğrudan kâra uygulandığı sonuç",
   f"{tr(contribution*sales_change)} TL katkı payındaki artışın tamamının ayrı bir hesap olmadan kullanıldığı sonuç",
   f"{tr(dol*sales_change*100)} TL yüzde değişimin parasal kâr artışı sayıldığı sonuç",
   f"{tr(contribution/profit)} TL yalnız faaliyet kaldıracı derecesinin kâr artışı kabul edildiği sonuç"],
  f"Faaliyet kaldıracı {tr(contribution)} / {tr(profit)} = {tr(dol)}'tür. Kâr %{tr(dol)} × %{tr(sales_change*100)} = %{tr(profit_change_rate*100)}; yani {tr(profit_increase)} TL artar.",
  "Yönetim muhasebesi - faaliyet kaldıracıyla kâr duyarlılığı", "hard")

margin_rate = 0.20
dol = 1/margin_rate
assert dol == 5
q(f"Doğrusal ve tek ürünlü modelde güvenlik payı oranı %{tr(margin_rate*100)} olan işletmenin faaliyet kaldıracı derecesi kaçtır?",
  f"{tr(dol)}",
  [f"{tr(margin_rate*100)} güvenlik payı yüzdesinin doğrudan kaldıraç derecesi sayıldığı sonuç",
   f"{tr(1-margin_rate)} bir eksi güvenlik payı oranının kaldıraç kabul edildiği sonuç",
   f"{tr(1/(1-margin_rate))} başabaş satış oranının tersinin kullanıldığı sonuç",
   f"{tr(margin_rate)} güvenlik payı oranının ondalık değerinin derece sayıldığı sonuç"],
  f"Tek ürünlü doğrusal modelde faaliyet kaldıracı derecesi güvenlik payı oranının tersidir: 1 / %{tr(margin_rate*100)} = {tr(dol)}.",
  "Yönetim muhasebesi - faaliyet kaldıracı ile güvenlik payı ilişkisi", "hard")

q("Faaliyet kaldıracına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Faaliyet kaldıracı derecesi toplam katkı payının faaliyet kârına oranıdır\n\nII. Başabaş noktasına yaklaşıldıkça faaliyet kaldıracı yükselir\n\nIII. Yüksek sabit maliyetli işletmede faaliyet kaldıracı her durumda birden küçüktür",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Faaliyet kaldıracı katkı/kâr oranıdır ve kâr sıfıra yaklaştıkça büyür. Yüksek sabit maliyet satış değişiminin kâra etkisini artırır; üçüncü ifade yanlıştır.",
  "Yönetim muhasebesi - faaliyet kaldıracı derecesinin yorumu")

old_price, variable_unit, old_units, new_price = 100, 60, 9_000, 92
old_total_cm = (old_price-variable_unit)*old_units
new_cm = new_price-variable_unit
required_units = old_total_cm/new_cm
additional = required_units-old_units
assert old_total_cm == 360_000 and required_units == 11_250 and additional == 2_250
q(f"Fiyat {tr(old_price)} TL'den {tr(new_price)} TL'ye indirilecektir. Birim değişken maliyet {tr(variable_unit)} TL ve mevcut hacim {tr(old_units)} birimdir. Sabit maliyet değişmezse aynı kârı korumak için toplam satış kaç birim olmalıdır?",
  f"{tr(required_units)} birim",
  [f"{tr(old_units)} birim fiyat indiriminin toplam katkıyı etkilemediği varsayılan sonuç",
   f"{tr(additional)} birim yalnız ek hacmin toplam satış miktarı kabul edildiği sonuç",
   f"{tr(old_total_cm/new_price)} birim toplam katkının yeni satış fiyatına bölündüğü sonuç",
   f"{tr(old_units*old_price/new_price)} birim yalnız satış gelirini koruyan hacim"],
  f"Eski katkı {tr(old_total_cm)} TL, yeni birim katkı {tr(new_cm)} TL'dir. Aynı toplam katkı için {tr(old_total_cm)} / {tr(new_cm)} = {tr(required_units)} birim gerekir.",
  "Yönetim muhasebesi - fiyat indiriminde kârı koruyan satış hacmi", "hard")

price, old_var, new_var, fixed = 160, 100, 96, 480_000
old_be = fixed/(price-old_var)
new_be = fixed/(price-new_var)
reduction = old_be-new_be
assert (old_be, new_be, reduction) == (8_000, 7_500, 500)
q(f"Birim değişken maliyet {tr(old_var)} TL'den {tr(new_var)} TL'ye düşecektir. Satış fiyatı {tr(price)} TL ve sabit maliyet {tr(fixed)} TL değişmezse başabaş miktarı kaç birim azalır?",
  f"{tr(reduction)} birim",
  [f"{tr(new_be)} birim yeni başabaş miktarının azalış tutarı kabul edildiği sonuç",
   f"{tr(old_be)} birim eski başabaş miktarının azalış tutarı kabul edildiği sonuç",
   f"{tr(fixed/(old_var-new_var))} birim sabit maliyetin değişken maliyet tasarrufuna bölündüğü sonuç",
   f"{tr(reduction)} birim artar; eski ve yeni başabaş sonuçlarının yönü ters yorumlanmıştır"],
  f"Eski başabaş {tr(old_be)}, yeni başabaş {tr(new_be)} birimdir. Azalış {tr(old_be)} − {tr(new_be)} = {tr(reduction)} birimdir.",
  "Yönetim muhasebesi - değişken maliyet tasarrufunun başabaşa etkisi")

old_units, new_units, price, variable_unit, ad_fixed = 6_000, 7_200, 150, 90, 90_000
incremental_cm = (new_units-old_units)*(price-variable_unit)
impact = incremental_cm-ad_fixed
assert incremental_cm == 72_000 and impact == -18_000
q(f"{tr(ad_fixed)} TL reklam harcamasının satışları {tr(old_units)} birimden {tr(new_units)} birime çıkaracağı beklenmektedir. Fiyat {tr(price)} TL, birim değişken maliyet {tr(variable_unit)} TL ise reklamın faaliyet kârına net etkisi nedir?",
  f"{tr(-impact)} TL azalış",
  [f"{tr(incremental_cm)} TL artış; ek reklam sabit gideri dışlanmıştır",
   f"{tr(ad_fixed)} TL azalış; artan satışların katkı payı dışlanmıştır",
   f"{tr((new_units-old_units)*price-ad_fixed)} TL artış; ek birimlerin değişken maliyeti dışlanmıştır",
   f"{tr(-impact)} TL artış; hesaplanan negatif net etkinin yönü ters yorumlanmıştır"],
  f"Ek katkı ({tr(new_units)} − {tr(old_units)}) × ({tr(price)} − {tr(variable_unit)}) = {tr(incremental_cm)} TL'dir. {tr(ad_fixed)} TL reklam sonrası kâr {tr(-impact)} TL azalır.",
  "Yönetim muhasebesi - reklam kararının artan katkı payıyla analizi", "hard")

units, variable_unit, fixed, target = 8_000, 72, 320_000, 80_000
required_price = variable_unit+(fixed+target)/units
assert required_price == 122
q(f"İşletme {tr(units)} birim satmayı, birim değişken maliyetin {tr(variable_unit)} TL ve sabit maliyetin {tr(fixed)} TL olmasını beklemektedir. {tr(target)} TL hedef kâr için gerekli asgari birim fiyat kaç TL'dir?",
  f"{tr(required_price)} TL",
  [f"{tr(variable_unit+fixed/units)} TL yalnız başabaş fiyatı olup hedef kârı dışlayan sonuç",
   f"{tr((fixed+target)/units)} TL değişken maliyetin fiyat hesabından çıkarıldığı sonuç",
   f"{tr(variable_unit+target/units)} TL sabit maliyetin fiyat hesabından çıkarıldığı sonuç",
   f"{tr(variable_unit+(fixed-target)/units)} TL hedef kârın sabit maliyetten çıkarıldığı sonuç"],
  f"Birim fiyat {tr(variable_unit)} + ({tr(fixed)} + {tr(target)}) / {tr(units)} = {tr(required_price)} TL olmalıdır.",
  "Yönetim muhasebesi - hedef kâra dayalı başabaş satış fiyatı", "hard")

price, units, fixed, target = 140, 10_000, 360_000, 240_000
required_cm = (fixed+target)/units
max_variable = price-required_cm
assert required_cm == 60 and max_variable == 80
q(f"Fiyat {tr(price)} TL, satış hacmi {tr(units)} birim ve sabit maliyet {tr(fixed)} TL'dir. {tr(target)} TL hedef faaliyet kârını korumak için birim değişken maliyet en çok kaç TL olabilir?",
  f"{tr(max_variable)} TL",
  [f"{tr(price-fixed/units)} TL yalnız sabit maliyeti karşılayan ve hedefi dışlayan sınır",
   f"{tr(price-target/units)} TL yalnız hedef kârı karşılayan ve sabit maliyeti dışlayan sınır",
   f"{tr(required_cm)} TL gerekli katkı payının değişken maliyet sınırı sayıldığı sonuç",
   f"{tr(price+(fixed+target)/units)} TL gerekli katkının satış fiyatına eklendiği sonuç"],
  f"Gerekli birim katkı ({tr(fixed)} + {tr(target)}) / {tr(units)} = {tr(required_cm)} TL'dir. Değişken maliyet en çok {tr(price)} − {tr(required_cm)} = {tr(max_variable)} TL olabilir.",
  "Yönetim muhasebesi - hedef kâr için azami değişken maliyet", "hard")

q("Duyarlılık analizinde başabaş sonucunun en kritik değişkenini belirlemek için hangi yaklaşım kullanılır?",
  "Her girdiyi makul aralıkta değiştirip sonuç etkisini karşılaştırmak",
  ["Bütün fiyat, maliyet ve hacim varsayımlarını aynı anda sabitleyerek yalnız tek sonuç üretmek",
   "Geçmişte oluşmuş sabit maliyetleri satış gelirine ekleyip yeni katkı payı tanımlamak",
   "Yalnız en yüksek satış hacmini seçip değişken maliyet ile kapasiteyi değerlendirme dışında bırakmak",
   "Başabaş miktarını hiçbir girdiyi değiştirmeden farklı harflerle yeniden ifade etmek"],
  "Duyarlılık analizi, fiyat, hacim, değişken ve sabit maliyet gibi girdileri ayrı senaryolarda değiştirerek sonucun hangi varsayıma daha duyarlı olduğunu gösterir.",
  "Yönetim muhasebesi - MHK modelinde duyarlılık analizi")

price, units = 100, 10_000
manual_fixed, manual_var = 200_000, 70
auto_fixed, auto_var = 400_000, 50
manual_cm = units*(price-manual_var)
auto_cm = units*(price-auto_var)
manual_profit = manual_cm-manual_fixed
auto_profit = auto_cm-auto_fixed
manual_dol, auto_dol = manual_cm/manual_profit, auto_cm/auto_profit
assert (manual_profit, auto_profit, manual_dol, auto_dol) == (100_000, 100_000, 3, 5)
q(f"{tr(units)} birim satışta manuel yapının katkısı {tr(manual_cm)} TL ve kârı {tr(manual_profit)} TL; otomasyon yapısının katkısı {tr(auto_cm)} TL ve kârı {tr(auto_profit)} TL'dir. Hangi yapının faaliyet kaldıracı daha yüksektir?",
  f"Otomasyon yapısı; derece {tr(auto_dol)}",
  [f"Manuel yapı; derece {tr(manual_dol)} çünkü sabit maliyeti daha düşüktür",
   "İki yapı; faaliyet kârları eşit olduğu için kaldıraç dereceleri de zorunlu olarak eşittir",
   f"Manuel yapı; derece {tr(auto_dol)} çünkü otomasyonun katkı payı manuel yapıya aktarılmalıdır",
   f"Otomasyon yapısı; derece {tr(manual_dol)} çünkü katkı payı yerine yalnız sabit maliyet kullanılır"],
  f"Faaliyet kaldıracı katkı/kârdır. Manuel yapıda {tr(manual_cm)} / {tr(manual_profit)} = {tr(manual_dol)}, otomasyonda {tr(auto_cm)} / {tr(auto_profit)} = {tr(auto_dol)} olduğundan otomasyon daha duyarlıdır.",
  "Yönetim muhasebesi - alternatif maliyet yapılarında faaliyet kaldıracı", "hard")

a_fixed, a_cmr, b_fixed, b_cmr = 180_000, 0.30, 300_000, 0.45
indifference_sales = (b_fixed-a_fixed)/(b_cmr-a_cmr)
assert abs(indifference_sales-800_000) < 1e-6
q(f"Plan A'nın sabit maliyeti {tr(a_fixed)} TL, katkı oranı %{tr(a_cmr*100)}; Plan B'nin sabit maliyeti {tr(b_fixed)} TL, katkı oranı %{tr(b_cmr*100)}'tir. İki plan hangi satış hasılatında aynı faaliyet kârını verir?",
  f"{tr(indifference_sales)} TL",
  [f"{tr((b_fixed-a_fixed)/a_cmr)} TL sabit farkının yalnız A katkı oranına bölündüğü sonuç",
   f"{tr((b_fixed-a_fixed)/b_cmr)} TL sabit farkının yalnız B katkı oranına bölündüğü sonuç",
   f"{tr((b_fixed+a_fixed)/(b_cmr-a_cmr))} TL sabit maliyet farkı yerine toplamının kullanıldığı sonuç",
   f"{tr(a_fixed/(b_cmr-a_cmr))} TL yalnız A sabit maliyetinin oran farkına bölündüğü sonuç"],
  f"Eşitlik {tr(a_cmr)}S − {tr(a_fixed)} = {tr(b_cmr)}S − {tr(b_fixed)} biçimindedir. Satış ({tr(b_fixed)} − {tr(a_fixed)}) / (%{tr(b_cmr*100)} − %{tr(a_cmr*100)}) = {tr(indifference_sales)} TL'dir.",
  "Yönetim muhasebesi - katkı oranları farklı planlarda kayıtsızlık satışı", "hard")

sales, cmr, old_fixed, new_fixed = 1_500_000, 0.40, 420_000, 480_000
old_be, new_be = old_fixed/cmr, new_fixed/cmr
old_margin, new_margin = sales-old_be, sales-new_be
decrease = old_margin-new_margin
assert (old_be, new_be, old_margin, new_margin, decrease) == (1_050_000, 1_200_000, 450_000, 300_000, 150_000)
q(f"Satışlar {tr(sales)} TL ve katkı oranı %{tr(cmr*100)} iken sabit maliyet {tr(old_fixed)} TL'den {tr(new_fixed)} TL'ye çıkacaktır. Satışlar değişmezse güvenlik payı tutarı kaç TL azalır?",
  f"{tr(decrease)} TL",
  [f"{tr(new_margin)} TL yeni güvenlik payının azalış tutarı kabul edildiği sonuç",
   f"{tr(old_margin)} TL eski güvenlik payının tamamının azalış kabul edildiği sonuç",
   f"{tr(new_fixed-old_fixed)} TL sabit maliyet artışının satış etkisine dönüştürülmeden kullanıldığı sonuç",
   f"{tr(new_be-old_be+new_fixed-old_fixed)} TL sabit maliyet artışının iki kez sayıldığı sonuç"],
  f"Eski başabaş {tr(old_be)}, yeni başabaş {tr(new_be)} TL'dir. Güvenlik payı {tr(old_margin)} TL'den {tr(new_margin)} TL'ye iner; azalış {tr(decrease)} TL'dir.",
  "Yönetim muhasebesi - sabit maliyet artışının güvenlik payına etkisi", "hard")

x_share, x_cmr, y_share, y_cmr = 0.70, 0.45, 0.30, 0.30
weighted_cmr = x_share*x_cmr+y_share*y_cmr
fixed, after_tax_target, tax_rate = 567_000, 170_100, 0.30
pretax_target = after_tax_target/(1-tax_rate)
sales = (fixed+pretax_target)/weighted_cmr
assert abs(weighted_cmr-0.405) < 1e-9 and abs(pretax_target-243_000) < 1e-6 and abs(sales-2_000_000) < 1e-6
q(f"Hasılat karması %{tr(x_share*100)} X ve %{tr(y_share*100)} Y; katkı oranları %{tr(x_cmr*100)} ve %{tr(y_cmr*100)}'dur. Sabit maliyet {tr(fixed)} TL, vergi oranı kökte verilen %{tr(tax_rate*100)} ve vergi sonrası hedef {tr(after_tax_target)} TL ise gereken toplam satış kaç TL'dir?",
  f"{tr(sales)} TL",
  [f"{tr((fixed+after_tax_target)/weighted_cmr)} TL net hedefin vergi öncesine çevrilmeden kullanıldığı sonuç",
   f"{tr(fixed/weighted_cmr)} TL hedef kârı dışlayan çok ürünlü başabaş satışı",
   f"{tr((fixed+pretax_target)/((x_cmr+y_cmr)/2))} TL katkı oranlarının basit ortalamasıyla bulunan sonuç",
   f"{tr((fixed+pretax_target)*(1-weighted_cmr))} TL gerekli katkının değişken maliyet oranıyla çarpıldığı sonuç"],
  f"Ağırlıklı katkı oranı %{tr(weighted_cmr*100)}, vergi öncesi hedef {tr(after_tax_target)} / (1 − %{tr(tax_rate*100)}) = {tr(pretax_target)} TL'dir. Satış ({tr(fixed)} + {tr(pretax_target)}) / %{tr(weighted_cmr*100)} = {tr(sales)} TL olur.",
  "Yönetim muhasebesi - çok ürünlü vergi sonrası hedef kâr satışı", "hard")


CHOICE_OVERRIDES = {
    1: (
        "Maliyet davranışı varsayımları yalnız belirli hacim aralığında geçerlidir",
        ["Satış fiyatı ve sabit maliyet her üretim düzeyinde aynı kalır",
         "İşletme yalnız başabaş noktasında üretim yapabilir",
         "Değişken maliyetler hacim arttıkça sıfıra iner",
         "Maliyet ilişkileri bütün kapasite düzeylerinde değişmez"],
    ),
    2: ("40 TL", ["45,56 TL", "50 TL", "17,78 TL", "47,14 TL"]),
    3: ("50.000 TL", ["245.000 TL", "160.000 TL", "200.000 TL", "401.000 TL"]),
    5: (
        "Toplam katkı payından sonra sabit maliyet olarak",
        ["Satış gelirinden önce değişken satış indirimi olarak",
         "Birim değişken üretim maliyetinin içinde",
         "Yalnız dönem sonu stok maliyetinin içinde",
         "Değişken yönetim giderleri arasında"],
    ),
    6: ("6.500 birim", ["5.500 birim", "5.000 birim", "2.600 birim", "2.200 birim"]),
    7: ("6.000 birim", ["2.000 birim", "5.000 birim", "5.333,33 birim", "26.000 birim"]),
    8: ("10.000 birim", ["4.285,71 birim", "7.500 birim", "40.000 birim", "15.000 birim"]),
    10: ("5.000 birim", ["7.500 birim", "2.500 birim", "10.000 birim", "3.750 birim"]),
    11: ("330.000 TL", ["280.000 TL", "350.000 TL", "400.000 TL", "57.000 TL"]),
    12: ("7.200 birim", ["5.400 birim", "2.400 birim", "6.000 birim", "9.000 birim"]),
    13: (
        "14.400 TL artar",
        ["302.400 TL artar", "288.000 TL azalır", "43.200 TL artar", "28.800 TL azalır"],
    ),
    15: (
        "Birim satış fiyatının sabitliği varsayımını",
        ["Toplam sabit maliyetin nakit giderlerden oluşması varsayımını",
         "Üretim miktarının başabaşa eşit olması varsayımını",
         "Katkı oranının sabit giderlerden hesaplanması varsayımını",
         "Bütün maliyetlerin batmış olması varsayımını"],
    ),
    16: ("350.000 TL", ["450.000 TL", "550.000 TL", "650.000 TL", "100.000 TL"]),
    17: ("8.000 birim", ["6.000 birim", "2.000 birim", "4.000 birim", "16.000 birim"]),
    18: ("126.000 TL", ["180.000 TL", "540.000 TL", "54.000 TL", "252.000 TL"]),
    19: ("2.000.000 TL", ["1.775.000 TL", "1.250.000 TL", "480.000 TL", "3.000.000 TL"]),
    21: ("220.000 TL", ["368.000 TL", "700.000 TL", "88.000 TL", "280.000 TL"]),
    22: ("10.000 birim", ["8.666,67 birim", "3.333,33 birim", "8.000 birim", "7.333,33 birim"]),
    23: (
        "1.000 birim artar",
        ["6.000 birim artar", "7.000 birim artar", "1.000 birim azalır", "Değişmez"],
    ),
    24: ("600.000 TL", ["490.909,09 TL", "121.500 TL", "270.000 TL", "870.000 TL"]),
    25: ("8.000 birim", ["5.333,33 birim", "2.666,67 birim", "10.666,67 birim", "23.111,11 birim"]),
    26: ("8.000 birim", ["6.666,67 birim", "6.000 birim", "2.000 birim", "5.333,33 birim"]),
    27: ("8.500 birim", ["6.500 birim", "7.500 birim", "2.785,71 birim", "4.500 birim"]),
    28: ("1.200.000 TL", ["735.483,87 TL", "173.280 TL", "456.000 TL", "281.481,48 TL"]),
    30: ("7.000 birim", ["3.000 birim", "4.000 birim", "1.000 birim", "14.000 birim"]),
    31: ("120 TL", ["50 TL", "10 TL", "60 TL", "100 TL"]),
    32: (
        "10.000 A ve 15.000 B",
        ["5.000 A ve 5.000 B", "15.000 A ve 10.000 B", "20.000 A ve 30.000 B", "25.000 A ve 0 B"],
    ),
    33: ("%40", ["%37,50", "%30", "%10", "%20"]),
    34: ("1.200.000 TL", ["800.000 TL", "192.000 TL", "480.000 TL", "1.680.000 TL"]),
    36: (
        "Ağırlıklı katkı oranını yükseltip başabaş satışını düşürür",
        ["Ağırlıklı katkı oranını düşürüp başabaş satışını yükseltir",
         "Sabit maliyeti sıfırlayıp başabaş analizini gereksiz kılar",
         "Birim değişken maliyetleri eşitleyip karmayı etkisiz kılar",
         "Katkı oranlarını değiştirmeden yalnız kayıt sırasını değiştirir"],
    ),
    37: ("120.000 TL", ["540.000 TL", "360.000 TL", "180.000 TL", "960.000 TL"]),
    38: ("14.000 birim", ["7.000 birim", "28.000 birim", "10.000 birim", "21.000 birim"]),
    39: ("13.500 birim", ["4.500 birim", "12.000 birim", "9.000 birim", "18.000 birim"]),
    40: (
        "9.000 A ve 6.000 B",
        ["6.000 A ve 9.000 B", "3.000 A ve 3.000 B", "12.857 A ve 20.000 B", "15.000 A ve 0 B"],
    ),
    41: ("1.600.000 TL", ["1.846.153,85 TL", "1.200.000 TL", "400.000 TL", "375.000 TL"]),
    43: ("32 TL", ["35 TL", "20 TL", "12 TL", "70 TL"]),
    44: (
        "40.000 TL azalır",
        ["300.000 TL azalır", "260.000 TL azalır", "80.000 TL azalır", "Değişmez"],
    ),
    45: ("600.000 TL", ["1.800.000 TL", "840.000 TL", "1.770.000 TL", "1.230.000 TL"]),
    46: ("1.600.000 TL", ["4.800.000 TL", "1.500.000 TL", "300.000 TL", "960.000 TL"]),
    47: ("10.000 birim", ["15.000 birim", "8.400 birim", "2.400 birim", "4.285,71 birim"]),
    48: ("33.600 TL", ["11.200 TL", "24.000 TL", "140.000 TL", "3.360 TL"]),
    49: ("5", ["20", "0,80", "1,25", "0,20"]),
    51: ("11.250 birim", ["9.000 birim", "2.250 birim", "3.913,04 birim", "9.782,61 birim"]),
    52: ("500 birim", ["7.500 birim", "8.000 birim", "120.000 birim", "1.000 birim"]),
    53: (
        "18.000 TL azalır",
        ["72.000 TL artar", "90.000 TL azalır", "90.000 TL artar", "18.000 TL artar"],
    ),
    54: ("122 TL", ["112 TL", "50 TL", "82 TL", "102 TL"]),
    55: ("80 TL", ["104 TL", "116 TL", "60 TL", "200 TL"]),
    56: (
        "Her girdiyi makul aralıkta değiştirip sonuç etkisini karşılaştırmak",
        ["Bütün varsayımları sabitleyip yalnız tek sonuç üretmek",
         "Batmış maliyetleri satış gelirine ekleyip katkıyı değiştirmek",
         "Yalnız en yüksek hacmi seçip maliyetleri dışlamak",
         "Başabaşı girdileri değiştirmeden yeniden ifade etmek"],
    ),
    57: (
        "Otomasyon yapısı; derece 5",
        ["Manuel yapı; derece 3", "İki yapının derecesi eşittir", "Manuel yapı; derece 5", "Otomasyon yapısı; derece 3"],
    ),
    58: ("800.000 TL", ["400.000 TL", "266.666,67 TL", "3.200.000 TL", "1.200.000 TL"]),
    59: ("150.000 TL", ["300.000 TL", "450.000 TL", "60.000 TL", "210.000 TL"]),
    60: ("2.000.000 TL", ["1.820.000 TL", "1.400.000 TL", "2.160.000 TL", "481.950 TL"]),
}

STEM_OVERRIDES = {
    18: (
        "Yönetim 9.000 birimlik planı değerlendirmektedir. Bu hacimde toplam katkı payı "
        "540.000 TL, dönem sabit maliyeti 360.000 TL ve vergi oranı kökte verilen %30'dur. "
        "Planın sağlayabileceği vergi sonrası kâr kaç TL'dir?"
    ),
    47: (
        "Başabaş miktarı 6.000 birim olan işletme, fiilî satış miktarının %40'ı kadar "
        "güvenlik payı hedeflemektedir. Bu oran için kaç birim satmalıdır?"
    ),
}

EXPLANATION_OVERRIDES = {
    48: (
        "Faaliyet kaldıracı derecesi 420.000 / 140.000 = 3'tür. Satışlardaki %8 artış, "
        "faaliyet kârını 3 × %8 = %24 artırır; 140.000 × %24 = 33.600 TL'dir."
    ),
}

for number, (correct, distractors) in CHOICE_OVERRIDES.items():
    Q[number - 1]["correct"] = correct
    Q[number - 1]["distractors"] = distractors

for number, stem in STEM_OVERRIDES.items():
    Q[number - 1]["stem"] = stem

for number, explanation in EXPLANATION_OVERRIDES.items():
    Q[number - 1]["why"] = explanation


print("TOPLAM:", len(Q))


def gen_letters(n, seed):
    r = random.Random(seed)
    base = ["ABCDE"[i % 5] for i in range(n)]
    while True:
        r.shuffle(base)
        if all(not (base[i] == base[i-1] == base[i-2]) for i in range(2, len(base))):
            return base


if __name__ == "__main__":
    assert len(Q) == 60, f"60 olmalı, şu an {len(Q)}"
    letters = gen_letters(len(Q), SEED)
    out = []
    for i, item in enumerate(Q):
        ans = letters[i]
        choices = {ans: item["correct"]}
        for key, distractor in zip([key for key in "ABCDE" if key != ans], item["distractors"]):
            choices[key] = distractor
        assert len(set(choices.values())) == 5, f"{PREFIX}-{i+1}: şık tekrarı"
        out.append({
            "id": f"{PREFIX}-{i+1:04d}",
            "lessonId": L,
            "topicId": T,
            "question": item["stem"],
            "choices": choices,
            "correctAnswer": ans,
            "explanation": item["why"],
            "source": {
                "kind": "generated",
                "styleRef": "2026/1 beş seçenekli test biçimi",
                "legislationRef": item["ref"],
            },
            "tags": ["Özgün Soru", "2026 Formatı", "Konu Havuzu", LBL],
            "difficulty": item["difficulty"],
            "updatedAt": UPDATED_AT,
            "examPeriod": "2026/1 formatına uyumlu",
            "legislationVersion": LEGISLATION_VERSION,
            "sourceUpdatedAt": UPDATED_AT,
            "isPremium": False,
            "isActive": True,
        })
    assert all("demo soru" not in item["question"].casefold() for item in out)
    assert all("demo açıklama" not in item["explanation"].casefold() for item in out)
    for output_path in OUTS:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8") as handle:
            json.dump(out, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
    marker = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    premises = sum(1 for item in out if len(marker.findall(item["question"])) >= 2)
    print(f"yazıldı: {len(out)} soru | öncüllü {premises} | harf {''.join(item['correctAnswer'] for item in out)[:40]}…")
