# -*- coding: utf-8 -*-
"""Yeterlilik KONU HAVUZU — Yönetim Muhasebesi / Karar Verme.

60 özgün soru = 3×20. İlgili maliyet, özel sipariş, üret–satın al,
bölüm kapatma, ileri işleme, yenileme, kısıtlı kaynak ve belirsizlik kararları.
Aritmetik Python'da hesaplanır; çözümde harf atfı yoktur.
"""
import json
import random
import re

L, T, LBL = "yonetim_muhasebesi", "karar_verme", "Karar Verme"
PREFIX, SEED = "kh-yon-karar", 20260907
OUTS = [
    "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/yeterlilik/questions_topic_karar_verme_2026.json",
    "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/yeterlilik/questions_topic_karar_verme_2026.json",
]

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


# ── A. İlgili maliyet ve özel sipariş kararları (15) ─────────────────────
q("Bir maliyet kaleminin kısa vadeli bir yönetim kararında ilgili sayılması için hangi iki niteliği birlikte taşıması gerekir?",
  "Gelecekte doğması ve seçenekler arasında değişmesi",
  ["Geçmişte muhasebeleştirilmiş olması ve bütün seçeneklere aynı tutarda yüklenmesi",
   "Finansal tablolarda sabit gider olarak sınıflandırılması ve nakit çıkışı yaratmaması",
   "Yalnız üretim hacmiyle değişmesi ve mutlaka direkt malzeme niteliğinde bulunması",
   "Bütçede öngörülmüş olması ve karar verildiğinde tutarının hiçbir biçimde değişmemesi"],
  "İlgili maliyet geleceğe yöneliktir ve alternatifler arasında farklılık yaratır. Geçmiş veya değişmeyen tutarlar kararı farklılaştırmaz.",
  "Yönetim muhasebesi - ilgili maliyetin geleceğe yönelik ve farklılaşan niteliği", "easy")

q("Beş yıl önce alınmış bir makinenin defter değeri, bugün makineyi yenileme kararında nasıl ele alınır?",
  "Batmış maliyet olarak karar dışında bırakılır",
  ["Yeni makinenin alış bedeline eklenerek iki varlığın toplam edinme maliyeti kabul edilir",
   "Eski makinenin kalan ömrüne bölünerek her alternatifin gelecekteki nakit gideri sayılır",
   "Makinenin satış olanağı bulunsa bile defter değerinin tamamı fırsat maliyeti kabul edilir",
   "Geçmişte amortisman ayrıldığı için yeni seçeneğin yıllık faaliyet tasarrufuna eklenir"],
  "Defter değeri geçmiş edinme maliyetinin dağıtılmamış kısmıdır ve karar onu değiştirmez. Olası satış bedeli ise gelecekte seçenekler arasında değiştiği için ilgilidir.",
  "Yönetim muhasebesi - batmış maliyet ile elden çıkarma değerinin ayrımı", "easy")

units, price, variable, setup = 1_800, 84, 57, 18_000
profit = units * (price - variable) - setup
assert profit == 30_600
q(f"İşletme, mevcut müşterilerden ayrı bir pazardaki tek seferlik sözleşmeyle {tr(units*price)} TL gelir elde edecektir. Sözleşme için {tr(units)} mamulün her biri {tr(variable)} TL ilgili üretim maliyeti ve ayrıca {tr(setup)} TL hat hazırlığı gerektirmektedir. Kullanılmayan kapasite yeterliyse sözleşmenin net getirisi kaç TL'dir?",
  f"{tr(profit)} TL",
  [f"{tr(units*(price-variable))} TL hazırlık giderinin dikkate alınmadığı katkı tutarı",
   f"{tr(units*price-setup)} TL yalnız satış geliri ile hazırlık giderinin karşılaştırıldığı sonuç",
   f"{tr(units*variable+setup)} TL ilgili maliyet toplamının kâr artışı kabul edildiği sonuç",
   f"{tr(units*(price-variable)+setup)} TL hazırlık giderinin katkıya yanlışlıkla eklendiği sonuç"],
  f"Sipariş katkısı {tr(units)} × ({tr(price)} − {tr(variable)}) = {tr(units*(price-variable))} TL'dir. {tr(setup)} TL hazırlık gideri düşünce artış {tr(profit)} TL olur.",
  "Yönetim muhasebesi - atıl kapasitede özel siparişin artan gelir ve maliyet analizi")

q("Karar analizine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Gelecekte doğacak ve seçenekler arasında değişecek maliyet ilgilidir\n\nII. Geçmişte katlanılmış geri alınamaz maliyet yeni kararda ilgilidir\n\nIII. Vazgeçilen en iyi alternatifin getirisi fırsat maliyetidir",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "Yalnız II"],
  "Gelecekte farklılaşan maliyet ile fırsat maliyeti kararı etkiler. Geçmişte katlanılmış ve geri alınamayan tutar batmış maliyettir.",
  "Yönetim muhasebesi - ilgili, batmış ve fırsat maliyetleri")

units, price, variable, lost_cm = 800, 92, 60, 26
impact = units * (price - variable - lost_cm)
assert impact == 4_800
q(f"Tam kapasitedeki işletme, {tr(units)} birim özel siparişi kabul ederse aynı miktarda normal satıştan vazgeçecektir. Sipariş fiyatı {tr(price)} TL, değişken maliyet {tr(variable)} TL ve normal satışın birim katkı payı {tr(lost_cm)} TL'dir. Sipariş kârı nasıl etkiler?",
  f"{tr(impact)} TL artar",
  [f"{tr(units*(price-variable))} TL artar; vazgeçilen normal satış katkısı karar dışında bırakılır",
   f"{tr(units*lost_cm)} TL azalır; özel siparişin sağladığı katkı hiç dikkate alınmaz",
   f"{tr(units*(price-variable+lost_cm))} TL artar; fırsat maliyeti sipariş katkısına eklenir",
   f"{tr(units*(variable+lost_cm))} TL azalır; gelir dikkate alınmadan iki maliyet toplanır"],
  f"Birim net yarar {tr(price)} − {tr(variable)} − {tr(lost_cm)} = {tr(price-variable-lost_cm)} TL'dir. {tr(units)} birimde kâr {tr(impact)} TL artar.",
  "Yönetim muhasebesi - tam kapasitede özel sipariş ve kaybedilen katkı payı", "hard")

variable, lost_cm, special_pack = 48, 19, 3
minimum = variable + lost_cm + special_pack
assert minimum == 70
q(f"Tam kapasitede bir özel sipariş, her birimde {tr(lost_cm)} TL normal katkı payı kaybına yol açacaktır. Siparişin birim değişken üretim maliyeti {tr(variable)} TL, özel ambalaj gideri {tr(special_pack)} TL'dir. Kârın azalmaması için asgari birim fiyat kaç TL olmalıdır?",
  f"{tr(minimum)} TL",
  [f"{tr(variable+special_pack)} TL yalnız nakit üretim ve ambalaj maliyetlerinin toplandığı fiyat",
   f"{tr(variable+lost_cm)} TL özel ambalaj giderinin ilgili maliyetten çıkarıldığı fiyat",
   f"{tr(lost_cm+special_pack)} TL değişken üretim maliyetinin tamamen göz ardı edildiği fiyat",
   f"{tr(variable-lost_cm+special_pack)} TL vazgeçilen katkının maliyetten düşüldüğü fiyat"],
  f"Asgari fiyat, ilgili üretim maliyeti ile fırsat maliyetini karşılamalıdır: {tr(variable)} + {tr(special_pack)} + {tr(lost_cm)} = {tr(minimum)} TL.",
  "Yönetim muhasebesi - özel siparişte asgari fiyat ve fırsat maliyeti", "hard")

units, price, variable = 2_500, 46, 34
max_fixed = units * (price - variable)
assert max_fixed == 30_000
q(f"Atıl kapasitedeki {tr(units)} birim siparişin birim fiyatı {tr(price)} TL, birim ilgili maliyeti {tr(variable)} TL'dir. Siparişin kârı azaltmaması için siparişe özgü sabit gider en çok kaç TL olabilir?",
  f"{tr(max_fixed)} TL",
  [f"{tr(units*price)} TL sipariş gelirinin tamamının sabit gider sınırı kabul edildiği tutar",
   f"{tr(units*variable)} TL toplam değişken maliyetin sabit gider sınırı sayıldığı tutar",
   f"{tr(units*(price+variable))} TL gelir ile maliyetin yanlışlıkla toplandığı tutar",
   f"{tr(price-variable)} TL yalnız birim katkının toplam sipariş sınırı kabul edildiği tutar"],
  f"Siparişin hazırlık gideri öncesi katkısı {tr(units)} × ({tr(price)} − {tr(variable)}) = {tr(max_fixed)} TL'dir; bundan büyük özel gider kârı azaltır.",
  "Yönetim muhasebesi - özel siparişe özgü sabit maliyet eşiği")

units, price, prod_var, inspection, setup = 1_400, 72, 49, 5, 14_000
profit = units * (price - prod_var - inspection) - setup
assert profit == 11_200
q(f"Boş kapasitedeki {tr(units)} birimlik sipariş için birim fiyat {tr(price)} TL, değişken üretim maliyeti {tr(prod_var)} TL, ek kalite kontrolü {tr(inspection)} TL ve parti hazırlığı {tr(setup)} TL'dir. Mevcut ortak sabit gider değişmeyeceğine göre siparişin kâr etkisi nedir?",
  f"{tr(profit)} TL artış",
  [f"{tr(units*(price-prod_var)-setup)} TL artış; ek kalite kontrolü maliyetinin dışlandığı sonuç",
   f"{tr(units*(price-prod_var-inspection))} TL artış; parti hazırlığı giderinin dışlandığı sonuç",
   f"{tr(units*(prod_var+inspection)+setup)} TL azalış; ilgili maliyetlerin kâr etkisi sayıldığı sonuç",
   f"{tr(units*price-setup)} TL artış; bütün birim maliyetlerin karar dışında bırakıldığı sonuç"],
  f"Birim katkı {tr(price)} − {tr(prod_var)} − {tr(inspection)} = {tr(price-prod_var-inspection)} TL; toplam katkıdan {tr(setup)} TL düşünce {tr(profit)} TL kalır.",
  "Yönetim muhasebesi - özel siparişte artan kalite ve hazırlık maliyetleri")

q("Özel sipariş değerlendirmesine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Atıl kapasitede artan değişken maliyet dikkate alınır\n\nII. Değişmeyecek ortak sabit gider dağıtımı her zaman ilgili maliyettir\n\nIII. Siparişin mevcut müşterilerin fiyat beklentisine etkisi değerlendirilmelidir",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "Yalnız II"],
  "Artan değişken maliyet sayısal analize girer; değişmeyen ortak gider ilgisizdir. Fiyat ayrımının müşteri ilişkisi ve pazar üzerindeki etkisi nitel değerlendirmedir.",
  "Yönetim muhasebesi - özel siparişte nicel ve nitel etkenler")

units, price, variable, hours, alt_cm_hour = 900, 76, 50, 0.4, 45
opportunity_unit = hours * alt_cm_hour
impact = units * (price - variable - opportunity_unit)
assert opportunity_unit == 18 and impact == 7_200
q(f"Bir özel sipariş {tr(units)} birimdir; fiyatı {tr(price)} TL, değişken maliyeti {tr(variable)} TL ve birim başına kapasite kullanımı {tr(hours)} saattir. Aynı kapasite alternatif üründe saat başına {tr(alt_cm_hour)} TL katkı sağlayacaktır. Siparişin toplam kâr etkisi nedir?",
  f"{tr(impact)} TL artış",
  [f"{tr(units*(price-variable))} TL artış; kapasitenin alternatif getirisi dikkate alınmayan sonuç",
   f"{tr(units*opportunity_unit)} TL azalış; siparişin kendi katkısı dikkate alınmayan sonuç",
   f"{tr(units*(price-variable+opportunity_unit))} TL artış; fırsat maliyetinin katkıya eklendiği sonuç",
   f"{tr(hours*alt_cm_hour)} TL artış; birim net yararın toplam siparişe uygulanmadığı sonuç"],
  f"Kapasitenin birim fırsat maliyeti {tr(hours)} × {tr(alt_cm_hour)} = {tr(opportunity_unit)} TL'dir. Net yarar {tr(units)} × ({tr(price)} − {tr(variable)} − {tr(opportunity_unit)}) = {tr(impact)} TL'dir.",
  "Yönetim muhasebesi - özel siparişte kapasitenin fırsat maliyeti", "hard")

units, price, prod_var, shipping, package, fixed = 1_200, 65, 41, 7, 3, 9_000
profit = units * (price - prod_var - shipping - package) - fixed
assert profit == 7_800
q(f"Yurt dışı özel sipariş {tr(units)} birim, fiyat {tr(price)} TL'dir. Birim değişken üretim maliyeti {tr(prod_var)} TL, ek taşıma {tr(shipping)} TL, özel paket {tr(package)} TL ve sertifika gideri toplam {tr(fixed)} TL'dir. Atıl kapasitede kâr etkisi kaç TL'dir?",
  f"{tr(profit)} TL artış",
  [f"{tr(units*(price-prod_var))} TL artış; siparişe özgü dağıtım ve sertifika giderleri dışlanmıştır",
   f"{tr(units*(price-prod_var-shipping-package))} TL artış; sertifika gideri dışlanmıştır",
   f"{tr(units*(prod_var+shipping+package)+fixed)} TL azalış; satış geliri hesaba katılmamıştır",
   f"{tr(units*price-fixed)} TL artış; bütün birim bazlı ilgili maliyetler dışlanmıştır"],
  f"Birim artan maliyet {tr(prod_var)} + {tr(shipping)} + {tr(package)} = {tr(prod_var+shipping+package)} TL'dir. Toplam katkıdan {tr(fixed)} TL çıkınca {tr(profit)} TL artış bulunur.",
  "Yönetim muhasebesi - özel siparişte üretim, dağıtım ve sertifika maliyetleri")

resale, conversion, final_revenue = 52_000, 18_000, 88_000
benefit = final_revenue - conversion - resale
assert benefit == 18_000
q(f"Stokta geçmiş maliyeti {tr(70_000)} TL olan malzeme bugün {tr(resale)} TL net bedelle satılabilir. Malzeme {tr(conversion)} TL ek işlemle {tr(final_revenue)} TL hasılat sağlayacak siparişte kullanılabilir. Kullanım seçeneğinin satışa göre net üstünlüğü kaç TL'dir?",
  f"{tr(benefit)} TL",
  [f"{tr(final_revenue-conversion)} TL vazgeçilen net satış bedelinin dışlandığı üretim sonucu",
   f"{tr(final_revenue-70_000-conversion)} TL geçmiş kayıtlı maliyetin ilgili sayıldığı sonuç",
   f"{tr(final_revenue-resale)} TL ek işlem maliyetinin dikkate alınmadığı sonuç",
   f"{tr(resale+conversion)} TL fırsat ve dönüştürme maliyetlerinin yarar kabul edildiği sonuç"],
  f"Geçmiş maliyet batmıştır. Kullanımın net yararı {tr(final_revenue)} − {tr(conversion)} − vazgeçilen {tr(resale)} = {tr(benefit)} TL'dir.",
  "Yönetim muhasebesi - eldeki malzemenin fırsat maliyeti ve özel kullanım kararı", "hard")

units, contribution_unit, batches, setup_batch = 3_200, 14, 4, 5_000
profit = units * contribution_unit - batches * setup_batch
assert profit == 24_800
q(f"Bir özel sipariş {tr(units)} birim için hazırlık öncesi birim katkı payı {tr(contribution_unit)} TL sağlayacaktır. Üretim {tr(batches)} ayrı partide yapılacak ve her parti {tr(setup_batch)} TL hazırlık gideri doğuracaktır. Siparişin toplam kâr katkısı kaç TL'dir?",
  f"{tr(profit)} TL",
  [f"{tr(units*contribution_unit)} TL parti hazırlıklarının tamamının dışlandığı katkı tutarı",
   f"{tr(units*contribution_unit-setup_batch)} TL yalnız bir partinin hazırlık giderinin düşüldüğü tutar",
   f"{tr(batches*setup_batch)} TL toplam hazırlık giderinin kâr katkısı kabul edildiği tutar",
   f"{tr(units*contribution_unit+batches*setup_batch)} TL hazırlık giderinin katkıya eklendiği tutar"],
  f"Hazırlık öncesi katkı {tr(units)} × {tr(contribution_unit)} = {tr(units*contribution_unit)} TL; dört partinin gideri {tr(batches*setup_batch)} TL olduğundan net katkı {tr(profit)} TL'dir.",
  "Yönetim muhasebesi - parti düzeyindeki maliyetle özel sipariş analizi")

q("Karar modelinin değerlendirilmesine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Duyarlılık analizi temel varsayımlardaki değişimin sonucu nasıl etkilediğini inceler\n\nII. Değişmeyecek dağıtılmış ortak gider sipariş kabul edilince kaçınılabilir hâle gelir\n\nIII. Yalnız sipariş kabul edilirse doğacak sabit hazırlık gideri ilgili maliyettir",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "Yalnız II"],
  "Duyarlılık analizi varsayım riskini görünür kılar. Değişmeyen ortak gider ilgisiz; siparişe özgü ve gelecekte doğacak hazırlık gideri ilgilidir.",
  "Yönetim muhasebesi - duyarlılık analizi ve kaçınılabilir maliyet")

units, variable, special_pack, special_fixed, target_profit = 2_000, 42, 3, 12_000, 18_000
minimum_price = (units*(variable+special_pack)+special_fixed+target_profit) / units
assert minimum_price == 60
q(f"Satış bölümü, boş kapasitede karşılanacak {tr(units)} birimlik tek seferlik sözleşme için fiyat teklifi hazırlamaktadır. Her birim {tr(variable)} TL üretim ve {tr(special_pack)} TL paket gideri; sözleşme toplam {tr(special_fixed)} TL başlangıç gideri doğuracaktır. Teklifin {tr(target_profit)} TL net getiri sağlaması için birim bedel en az kaç TL olmalıdır?",
  f"{tr(minimum_price)} TL",
  [f"{tr(variable+special_pack)} TL yalnız birim maliyetleri karşılayan ve sabit giderle hedef kârı dışlayan fiyat",
   f"{tr((units*(variable+special_pack)+special_fixed)/units)} TL hedef kârı karşılamayan başabaş fiyatı",
   f"{tr((units*variable+target_profit)/units)} TL paket ve siparişe özgü sabit gideri dışlayan fiyat",
   f"{tr((special_fixed+target_profit)/units)} TL değişken üretim ile paket giderini dışlayan fiyat"],
  f"Gerekli gelir; birim maliyetler, {tr(special_fixed)} TL özel gider ve {tr(target_profit)} TL hedef kârı karşılar. Birim fiyat ({tr(units*(variable+special_pack))} + {tr(special_fixed)} + {tr(target_profit)}) / {tr(units)} = {tr(minimum_price)} TL'dir.",
  "Yönetim muhasebesi - özel siparişte hedef kâra dayalı asgari fiyat", "hard")


# ── B. Üretme veya satın alma ve dış kaynak kullanımı (15) ────────────────
units, unit_var, avoidable_fixed = 6_000, 26, 48_000
make_relevant = units * unit_var + avoidable_fixed
assert make_relevant == 204_000
q(f"Bir parçadan yıllık {tr(units)} adet üretilmektedir. Birim değişken maliyet {tr(unit_var)} TL, üretim bırakılırsa kaçınılabilecek sabit gider {tr(avoidable_fixed)} TL'dir. Dağıtılan ortak gider değişmeyeceğine göre üretmenin toplam ilgili maliyeti kaç TL'dir?",
  f"{tr(make_relevant)} TL",
  [f"{tr(units*unit_var)} TL kaçınılabilir sabit giderin karar dışında bırakıldığı maliyet",
   f"{tr(avoidable_fixed)} TL değişken üretim maliyetlerinin tamamen dışlandığı tutar",
   f"{tr(units*(unit_var)+avoidable_fixed*2)} TL kaçınılabilir giderin iki kez eklendiği sonuç",
   f"{tr(units*(unit_var+avoidable_fixed))} TL toplam sabit giderin her birime ayrı ayrı yüklendiği sonuç"],
  f"İlgili üretim maliyeti {tr(units)} × {tr(unit_var)} + {tr(avoidable_fixed)} = {tr(make_relevant)} TL'dir. Değişmeyecek ortak gider iki seçenekte de aynıdır.",
  "Yönetim muhasebesi - üretme veya satın almada ilgili üretim maliyeti")

buy_price, capacity_benefit = 36, 30_000
buy_net = units * buy_price - capacity_benefit
advantage = make_relevant - buy_net
assert buy_net == 186_000 and advantage == 18_000
q(f"Önceki parçanın dış alım fiyatı birim başına {tr(buy_price)} TL'dir. Satın alma kapasiteyi serbest bırakacak ve yıllık {tr(capacity_benefit)} TL ek katkı sağlayacaktır. Üretmenin ilgili maliyeti {tr(make_relevant)} TL ise hangi seçenek ne kadar avantajlıdır?",
  f"Satın alma {tr(advantage)} TL avantajlıdır",
  [f"Üretim {tr(units*buy_price-make_relevant)} TL avantajlıdır; kapasite getirisi dışarıda bırakılmıştır",
   f"Satın alma {tr(capacity_benefit)} TL avantajlıdır; üretim ve alış maliyetleri karşılaştırılmamıştır",
   f"Üretim {tr(make_relevant-buy_net+capacity_benefit)} TL avantajlıdır; kapasite getirisi ters yönde kullanılmıştır",
   f"İki seçenek eşittir; serbest kapasitenin alternatif getirisi karar açısından ilgisiz kabul edilmiştir"],
  f"Satın almanın net maliyeti {tr(units)} × {tr(buy_price)} − {tr(capacity_benefit)} = {tr(buy_net)} TL'dir. Üretim {tr(make_relevant)} TL olduğundan satın alma {tr(advantage)} TL daha avantajlıdır.",
  "Yönetim muhasebesi - dış alım ve serbest kalan kapasitenin alternatif getirisi", "hard")

q("Üretme veya satın alma kararına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Üretimden vazgeçilince ortadan kalkacak sabit gider ilgilidir\n\nII. Satın almayla serbest kalacak kapasitenin alternatif getirisi dikkate alınır\n\nIII. Tedarik kalitesi ve sürekliliği sayısal sonucun yanında değerlendirilir",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Kaçınılabilir gider ve kapasite fırsatı seçenekler arasında değişir. Kalite, teslimat, bağımlılık ve gizlilik de kararın nitel boyutlarıdır.",
  "Yönetim muhasebesi - üretme veya satın almada nicel ve nitel değerlendirme")

q("Dış alım seçeneği sayısal olarak daha ucuz görünse de hangi durum işletme içinde üretimin sürdürülmesini destekleyebilir?",
  "Tedarikçinin kritik kaliteyi güvence altına alamaması",
  ["Dağıtılmış ortak yönetim giderinin satın alma seçeneğinde de aynı tutarda devam etmesi",
   "Parçanın geçmiş yıllardaki üretim maliyetinin bugünkü iki seçenekten de etkilenmemesi",
   "Üretim makinesinin geçmiş edinme bedelinin finansal tablolarda kayıtlı bulunması",
   "Satın alma halinde kaçınılabilir bütün maliyetlerin gerçekten ortadan kalkacak olması"],
  "Kritik kalite, teslimat sürekliliği, fikrî bilgi ve tedarikçiye bağımlılık gibi nitel riskler salt maliyet üstünlüğünü dengeleyebilir.",
  "Yönetim muhasebesi - dış kaynak kullanımında kalite ve tedarik riski")

units, make_var, avoid_unit, buy_unit, alt_benefit = 5_000, 22, 3, 28, 22_000
make = units * (make_var + avoid_unit)
buy_net = units * buy_unit - alt_benefit
advantage = make - buy_net
assert (make, buy_net, advantage) == (125_000, 118_000, 7_000)
q(f"Yıllık {tr(units)} parça için üretmenin birim değişken maliyeti {tr(make_var)} TL, kaçınılabilir sabit payı {tr(avoid_unit)} TL; dış alım fiyatı {tr(buy_unit)} TL'dir. Dış alımla kapasiteden {tr(alt_benefit)} TL katkı sağlanacaktır. Kâr açısından sonuç nedir?",
  f"Satın alma {tr(advantage)} TL avantajlıdır",
  [f"Üretim {tr(units*(buy_unit-make_var-avoid_unit))} TL avantajlıdır; alternatif katkı dışlanmıştır",
   f"Satın alma {tr(alt_benefit)} TL avantajlıdır; iki seçeneğin doğrudan maliyet farkı dışlanmıştır",
   f"Üretim {tr(make-buy_net+alt_benefit)} TL avantajlıdır; kapasite getirisi üretim lehine eklenmiştir",
   f"Seçenekler eşittir; kaçınılabilir sabit gider ile alternatif kapasite getirisi dışlanmıştır"],
  f"Üretim {tr(make)} TL'dir. Satın almanın fırsat sonrası net maliyeti {tr(units*buy_unit)} − {tr(alt_benefit)} = {tr(buy_net)} TL; fark {tr(advantage)} TL satın alma lehinedir.",
  "Yönetim muhasebesi - dış alımda kaçınılabilir sabit gider ve kapasite fırsatı", "hard")

make_var, avoid_fixed_unit, opportunity_unit = 19, 5, 6
max_buy = make_var + avoid_fixed_unit + opportunity_unit
assert max_buy == 30
q(f"Bir parçayı üretmenin birim değişken maliyeti {tr(make_var)} TL, kaçınılabilir sabit maliyeti {tr(avoid_fixed_unit)} TL'dir. Dış alım serbest kapasiteden birim başına {tr(opportunity_unit)} TL yarar sağlayacaktır. Satın alma fiyatının başabaş üst sınırı kaç TL'dir?",
  f"{tr(max_buy)} TL",
  [f"{tr(make_var+avoid_fixed_unit)} TL kapasitenin alternatif yararının dışarıda bırakıldığı sınır",
   f"{tr(make_var+opportunity_unit)} TL kaçınılabilir sabit maliyetin dışarıda bırakıldığı sınır",
   f"{tr(make_var-avoid_fixed_unit+opportunity_unit)} TL kaçınılabilir maliyetin üretimden düşüldüğü sınır",
   f"{tr(avoid_fixed_unit+opportunity_unit)} TL değişken üretim maliyetinin dikkate alınmadığı sınır"],
  f"Dış alım fiyatı, kaçınılan {tr(make_var)} + {tr(avoid_fixed_unit)} TL maliyet ile sağlanan {tr(opportunity_unit)} TL kapasite yararının toplamına, yani {tr(max_buy)} TL'ye kadar çıkabilir.",
  "Yönetim muhasebesi - üretme veya satın almada başabaş alış fiyatı")

units, quote, inspection, defect_rate, rework, make_cost = 8_000, 25, 2, 0.10, 15, 30
expected_buy_unit = quote + inspection + defect_rate * rework
advantage = units * (make_cost - expected_buy_unit)
assert expected_buy_unit == 28.5 and advantage == 12_000
q(f"Tedarikçi bir parçayı {tr(quote)} TL'ye sunmaktadır. Her parça için {tr(inspection)} TL kontrol yapılacak; parçaların %{tr(defect_rate*100)}'unun {tr(rework)} TL yeniden işleme gerektirmesi beklenmektedir. İç üretimin ilgili maliyeti {tr(make_cost)} TL, ihtiyaç {tr(units)} adettir. Beklenen maliyete göre dış alımın üstünlüğü kaç TL'dir?",
  f"{tr(advantage)} TL",
  [f"{tr(units*(make_cost-quote))} TL kontrol ve beklenen yeniden işleme maliyetlerinin dışlandığı fark",
   f"{tr(units*(make_cost-quote-inspection))} TL kusurlu parçaların beklenen maliyetinin dışlandığı fark",
   f"{tr(units*(expected_buy_unit-quote))} TL ek kalite maliyetlerinin tasarruf kabul edildiği fark",
   f"{tr(units*expected_buy_unit)} TL toplam beklenen dış alım maliyetinin üstünlük sayıldığı sonuç"],
  f"Beklenen dış alım maliyeti {tr(quote)} + {tr(inspection)} + %{tr(defect_rate*100)} × {tr(rework)} = {tr(expected_buy_unit)} TL'dir. Birim {tr(make_cost-expected_buy_unit)} TL tasarruf, {tr(units)} adette {tr(advantage)} TL olur.",
  "Yönetim muhasebesi - tedarik kalitesi için beklenen maliyetli dış alım analizi", "hard")

prod_var, supervisor, cancellable_lease, common = 180_000, 40_000, 30_000, 25_000
relevant = prod_var + supervisor + cancellable_lease
assert relevant == 250_000
q(f"Bir faaliyetin değişken üretim maliyeti {tr(prod_var)} TL, faaliyet kapanırsa sona erecek yönetici ücreti {tr(supervisor)} TL, iptal edilebilir ekipman kirası {tr(cancellable_lease)} TL ve devam edecek ortak gider payı {tr(common)} TL'dir. İç üretimin ilgili maliyeti kaç TL'dir?",
  f"{tr(relevant)} TL",
  [f"{tr(prod_var)} TL yalnız değişken maliyetin ilgili kabul edildiği tutar",
   f"{tr(prod_var+supervisor)} TL iptal edilebilir ekipman kirasının dışlandığı tutar",
   f"{tr(relevant+common)} TL değişmeyecek ortak giderin de karara eklendiği tutar",
   f"{tr(supervisor+cancellable_lease+common)} TL değişken üretim maliyetinin dışlandığı tutar"],
  f"Değişken maliyet, sona erecek ücret ve iptal edilebilir kira kaçınılabilir: {tr(prod_var)} + {tr(supervisor)} + {tr(cancellable_lease)} = {tr(relevant)} TL. Ortak gider devam eder.",
  "Yönetim muhasebesi - dış kaynak kararında kaçınılabilir faaliyet maliyetleri")

units, unit_var, avoidable_fixed, quote, capacity_benefit = 4_000, 30, 20_000, 39, 28_000
make = units * unit_var + avoidable_fixed
buy_net = units * quote - capacity_benefit
advantage = make - buy_net
assert (make, buy_net, advantage) == (140_000, 128_000, 12_000)
q(f"İşletme {tr(units)} bileşeni birim {tr(unit_var)} TL değişken maliyet ve {tr(avoidable_fixed)} TL kaçınılabilir sabit giderle üretmektedir. Tedarikçi fiyatı {tr(quote)} TL'dir; boşalacak kapasite {tr(capacity_benefit)} TL katkı yaratacaktır. Dış alımın yıllık net etkisi nedir?",
  f"Kâr {tr(advantage)} TL artar",
  [f"Kâr {tr(units*(quote-unit_var)-avoidable_fixed)} TL azalır; kapasite yararı dışarıda bırakılır",
   f"Kâr {tr(capacity_benefit)} TL artar; üretim ve dış alım maliyet farkı dışarıda bırakılır",
   f"Kâr {tr(make-buy_net+capacity_benefit)} TL azalır; kapasite katkısı ters yönde kullanılır",
   f"Kâr değişmez; tedarik fiyatı ile üretim maliyeti karşılaştırılmadan karar verilir"],
  f"Üretim {tr(make)} TL'dir. Dış alımın kapasite sonrası net maliyeti {tr(units*quote)} − {tr(capacity_benefit)} = {tr(buy_net)} TL; kâr {tr(advantage)} TL artar.",
  "Yönetim muhasebesi - dış alım ve kapasitenin başka üründe kullanılması", "hard")

q("Dış kaynak kararına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Üretim bırakıldığında da sürecek amortisman dağıtımı ilgisizdir\n\nII. Serbest kapasiteden sağlanacak katkı dış alım lehine bir etkidir\n\nIII. Mevcut makinenin geçmiş alış bedeli dış alımın ilgili maliyetidir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Değişmeyen amortisman ve geçmiş alış bedeli kararı farklılaştırmaz. Serbest kapasitenin getirisi dış alımla doğan fırsat yararıdır.",
  "Yönetim muhasebesi - dış kaynak kararında kaçınılabilirlik ve fırsat etkisi")

years, annual_make, annual_outsource, severance = 3, 240_000, 220_000, 35_000
make_total = years * annual_make
out_total = years * annual_outsource + severance
benefit = make_total - out_total
assert (make_total, out_total, benefit) == (720_000, 695_000, 25_000)
q(f"Bir destek hizmetinin ilgili iç maliyeti yılda {tr(annual_make)} TL, dış kaynak bedeli yılda {tr(annual_outsource)} TL'dir. Dış kaynak seçilirse bir kez {tr(severance)} TL çıkış tazminatı ödenecektir. Paranın zaman değeri ihmal edilirse {years} yıllık dış kaynak avantajı kaç TL'dir?",
  f"{tr(benefit)} TL",
  [f"{tr(years*(annual_make-annual_outsource))} TL tek seferlik çıkış maliyetinin dışlandığı tasarruf",
   f"{tr(annual_make-annual_outsource-severance)} TL üç yıllık fark hesaplanmadan bulunan sonuç",
   f"{tr(out_total)} TL dış kaynağın toplam maliyetinin tasarruf kabul edildiği sonuç",
   f"{tr(make_total-out_total+severance)} TL çıkış tazminatının toplam farktan iki kez düşülmediği sonuç"],
  f"İç seçenek {tr(make_total)} TL; dış kaynak {tr(years)} × {tr(annual_outsource)} + {tr(severance)} = {tr(out_total)} TL'dir. Dış kaynak {tr(benefit)} TL tasarruf sağlar.",
  "Yönetim muhasebesi - çok dönemli dış kaynak kararında tek seferlik maliyet", "hard")

book, net_sale = 70_000, 44_000
q(f"Başka kullanım alanı bulunmayan bir malzemenin defter değeri {tr(book)} TL, bugün net satış değeri {tr(net_sale)} TL'dir. Malzeme yeni bir bileşenin iç üretiminde kullanılacaksa karara giren ilgili malzeme maliyeti kaç TL'dir?",
  f"{tr(net_sale)} TL",
  [f"{tr(book)} TL geçmiş kayıtlı maliyetin değiştirilmeden ilgili kabul edildiği tutar",
   f"{tr(book-net_sale)} TL defter değeri ile satış değeri farkının fırsat maliyeti sayıldığı tutar",
   f"{tr(book+net_sale)} TL geçmiş maliyetle vazgeçilen satışın birlikte sayıldığı tutar",
   "0 TL; eldeki malzemenin hiçbir alternatif kullanım değeri bulunmadığı varsayılan tutar"],
  f"Malzeme üretimde kullanılırsa {tr(net_sale)} TL net satış geliri kaybedilir. Defter değeri geçmiş maliyettir; ilgili tutar vazgeçilen satış bedelidir.",
  "Yönetim muhasebesi - eldeki malzemenin dış satışa dayalı fırsat maliyeti")

q("Parça üretimi sona erse de makineye ilişkin dönem amortismanı aynen sürecekse bu amortisman dış alım kararında nasıl değerlendirilir?",
  "Seçenekler arasında değişmediği için ilgisizdir",
  ["Dış alım fiyatına eklenerek tedarikçinin toplam maliyetinin bir parçası kabul edilir",
   "Üretim bırakıldığında nakit olarak geri alınacağı varsayılarak dış alım geliri sayılır",
   "Makinenin geçmiş alış bedeliyle birlikte kapasitenin saatlik fırsat maliyetine dönüştürülür",
   "Sabit maliyet olduğu için üretim miktarı ne olursa olsun yalnız üretim lehine değerlendirilir"],
  "Amortisman dağıtımı üretme ve satın alma seçeneklerinde değişmiyorsa kararı farklılaştırmaz; nakit çıkışı veya kaçınılabilir tasarruf yaratmaz.",
  "Yönetim muhasebesi - değişmeyen amortismanın üretme veya satın alma kararındaki yeri")

variable, avoid_fixed, opportunity = 18, 4, 5
max_quote = variable + avoid_fixed + opportunity
assert max_quote == 27
q(f"İç üretimin birim değişken maliyeti {tr(variable)} TL, kaçınılabilir sabit maliyeti {tr(avoid_fixed)} TL ve dış alımla doğacak kapasite yararı birim {tr(opportunity)} TL'dir. İşletmenin kabul edebileceği en yüksek tedarikçi fiyatı kaç TL'dir?",
  f"{tr(max_quote)} TL",
  [f"{tr(variable+avoid_fixed)} TL kapasite yararının hesaba katılmadığı fiyat sınırı",
   f"{tr(variable+opportunity)} TL kaçınılabilir sabit maliyetin dışlandığı fiyat sınırı",
   f"{tr(variable-avoid_fixed+opportunity)} TL kaçınılabilir giderin üretim maliyetinden düşüldüğü sınır",
   f"{tr(avoid_fixed+opportunity)} TL değişken üretim maliyetinin dışlandığı fiyat sınırı"],
  f"Dış alımın üst sınırı kaçınılan {tr(variable)} + {tr(avoid_fixed)} TL maliyet ile sağlanan {tr(opportunity)} TL kapasite yararının toplamı {tr(max_quote)} TL'dir.",
  "Yönetim muhasebesi - dış alım için azami kabul edilebilir fiyat")

units, make_var, avoidable_fixed, hours_per_unit, alt_cm_hour = 3_000, 58, 30_000, 2, 8
opportunity = units * hours_per_unit * alt_cm_hour
max_total_buy = units * make_var + avoidable_fixed + opportunity
max_unit_buy = max_total_buy / units
assert opportunity == 48_000 and max_unit_buy == 84
q(f"İşletme {tr(units)} parçayı birim {tr(make_var)} TL değişken maliyetle üretmekte, {tr(avoidable_fixed)} TL kaçınılabilir sabit gider taşımaktadır. Her parça {tr(hours_per_unit)} makine saati kullanır; dış alımla boşalacak saatler {tr(alt_cm_hour)} TL/saat katkı sağlayacaktır. Başabaş dış alım fiyatı kaç TL/birimdir?",
  f"{tr(max_unit_buy)} TL",
  [f"{tr((units*make_var+avoidable_fixed)/units)} TL kapasite fırsatının dışlandığı birim maliyet",
   f"{tr(make_var+hours_per_unit*alt_cm_hour)} TL kaçınılabilir sabit giderin dışlandığı birim sınır",
   f"{tr(make_var+avoidable_fixed)} TL toplam sabit giderin her birime tam tutarla yüklendiği sonuç",
   f"{tr(max_unit_buy-hours_per_unit*alt_cm_hour)} TL boşalan saatlerin getirisi ikinci kez çıkarılan sonuç"],
  f"Kaçınılan maliyet {tr(units*make_var+avoidable_fixed)} TL, kapasite yararı {tr(opportunity)} TL'dir. Toplam {tr(max_total_buy)} TL / {tr(units)} = {tr(max_unit_buy)} TL/birimdir.",
  "Yönetim muhasebesi - kapasite fırsatı dâhil başabaş dış alım fiyatı", "hard")


# ── C. Bölüm, ileri işleme ve ekipman yenileme kararları (15) ─────────────
contribution, avoidable_fixed, allocated_common = 150_000, 110_000, 45_000
decrease = contribution - avoidable_fixed
assert decrease == 40_000
q(f"Yıllık {tr(contribution)} TL katkı sağlayan bir hattın sona erdirilmesi {tr(avoidable_fixed)} TL gider tasarrufu yaratacaktır. Hatta yüklenen {tr(allocated_common)} TL merkez gideri ise işletmede kalacaktır. Boşalacak alanın başka kullanımı en az kaç TL katkı sağlarsa hattı kapatmak toplam kârı azaltmaz?",
  f"{tr(decrease)} TL",
  [f"{tr(avoidable_fixed)} TL yalnız kaçınılabilir sabit giderin başabaş katkısı sayıldığı tutar",
   f"{tr(contribution)} TL gider tasarrufunun dikkate alınmadığı gerekli alternatif katkı",
   f"{tr(contribution-avoidable_fixed+allocated_common)} TL devam eden merkez giderinin gereksinime eklendiği tutar",
   "0 TL; devam edecek merkez giderinin de hat kapanınca tasarruf edileceği varsayılan sonuç"],
  f"Kapatmayla {tr(contribution)} TL kaybedilir ve {tr(avoidable_fixed)} TL tasarruf edilir. Aradaki {tr(decrease)} TL, alanın sağlaması gereken asgari alternatif katkıdır; merkez gideri değişmez.",
  "Yönetim muhasebesi - ürün hattını kapatmada başabaş alternatif kullanım getirisi")

q("Bir bölüme dağıtılan genel merkez gideri, bölüm kapatılsa da aynı toplam tutarda diğer bölümlere dağıtılacaksa karar analizinde nasıl ele alınır?",
  "Toplam işletme giderini değiştirmediği için dışlanır",
  ["Bölüm gelirinden ikinci kez düşülerek kapatma seçeneğinin tasarrufu kabul edilir",
   "Bölüm yöneticisinin kontrolünde olmasa da bütünüyle kaçınılabilir gider sayılır",
   "Dağıtım anahtarı değişeceği için tamamı bölümün kaybedilecek katkı payına eklenir",
   "Sabit nitelikte olduğu için her koşulda kapatma kararının tek belirleyicisi kabul edilir"],
  "Yalnız muhasebe dağıtımı değişir; toplam ortak gider devam ettiği için seçenekler arasında farklılaşmaz ve ilgili değildir.",
  "Yönetim muhasebesi - dağıtılmış ortak sabit giderin bölüm kararındaki yeri", "easy")

q("Bir faaliyet bölümünün kapatılmasına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Kaybedilecek katkı payı kapatmanın maliyetidir\n\nII. Ortadan kalkacak sabit gider kapatmanın yararıdır\n\nIII. Serbest alanın alternatif kullanım getirisi kapatma lehine dikkate alınır",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Kapatma; katkı kaybı, kaçınılabilir gider tasarrufu ve serbest kaynağın alternatif getirisi birlikte karşılaştırılarak değerlendirilir.",
  "Yönetim muhasebesi - bölüm kapatma kararının katkı, tasarruf ve fırsat unsurları")

contribution, avoidable_fixed, reuse = 120_000, 70_000, 80_000
benefit = avoidable_fixed + reuse - contribution
assert benefit == 30_000
q(f"Bir bölüm kapatılırsa {tr(contribution)} TL katkı kaybedilecek, {tr(avoidable_fixed)} TL sabit giderden kaçınılacak ve alanın başka kullanımından {tr(reuse)} TL katkı sağlanacaktır. Kapatmanın toplam kâr etkisi nedir?",
  f"{tr(benefit)} TL artış",
  [f"{tr(contribution-avoidable_fixed)} TL azalış; alanın alternatif getirisi dışlanmıştır",
   f"{tr(reuse)} TL artış; kaybedilen katkı ile gider tasarrufu karşılaştırılmamıştır",
   f"{tr(contribution+reuse-avoidable_fixed)} TL azalış; alternatif getiri maliyet sayılmıştır",
   f"{tr(avoidable_fixed+reuse)} TL artış; kaybedilecek bölüm katkısı dikkate alınmamıştır"],
  f"Kapatma yararı {tr(avoidable_fixed)} + {tr(reuse)} − {tr(contribution)} = {tr(benefit)} TL'dir.",
  "Yönetim muhasebesi - bölüm kapatmada alanın alternatif kullanım değeri", "hard")

revenue, variable_service, specific_fixed, common = 240_000, 155_000, 48_000, 35_000
segment_margin = revenue - variable_service - specific_fixed
assert segment_margin == 37_000
q(f"Bir müşteri grubunun geliri {tr(revenue)} TL, değişken hizmet maliyeti {tr(variable_service)} TL, müşteri grubuna özgü kaçınılabilir sabit gideri {tr(specific_fixed)} TL ve değişmeyecek ortak gider payı {tr(common)} TL'dir. Grup bırakılırsa kâr nasıl değişir?",
  f"{tr(segment_margin)} TL azalır",
  [f"{tr(revenue-variable_service)} TL azalır; kaçınılabilir sabit gider tasarrufu dışlanmıştır",
   f"{tr(segment_margin-common)} TL azalır; devam edecek ortak gider tasarruf gibi kullanılmıştır",
   f"{tr(specific_fixed+common)} TL artar; iki sabit giderin de ortadan kalkacağı varsayılmıştır",
   f"{tr(revenue-variable_service-specific_fixed-common)} TL artar; segment marjının yönü ters çevrilmiştir"],
  f"Grubun ortak gider öncesi segment marjı {tr(revenue)} − {tr(variable_service)} − {tr(specific_fixed)} = {tr(segment_margin)} TL'dir. Grup bırakılırsa bu tutar kaybedilir.",
  "Yönetim muhasebesi - müşteri kârlılığı ve kaçınılabilir sabit maliyet")

split_sale, final_sale, further_cost = 75_000, 104_000, 21_000
benefit = final_sale - split_sale - further_cost
max_further_cost = final_sale - split_sale
assert benefit == 8_000 and max_further_cost == 29_000
q(f"Bir ortak ürün ayrılma anında {tr(split_sale)} TL net bedelle elden çıkarılabilecek, nihai forma dönüştürüldüğünde ise {tr(final_sale)} TL gelir sağlayacaktır. Ayrılma öncesi ortak maliyet değişmeyeceğine göre dönüştürme giderinin başabaş üst sınırı kaç TL'dir?",
  f"{tr(max_further_cost)} TL",
  [f"{tr(final_sale)} TL nihai satış gelirinin tamamının işlem maliyeti sınırı kabul edildiği tutar",
   f"{tr(split_sale)} TL vazgeçilen ara ürün satış bedelinin tek başına sınır kabul edildiği tutar",
   f"{tr(benefit)} TL mevcut {tr(further_cost)} TL işlem gideri sonrası net yararın üst sınır sayıldığı tutar",
   f"{tr(final_sale+split_sale)} TL iki alternatif satış gelirinin yanlışlıkla toplandığı tutar"],
  f"Dönüştürmeyle artan gelir {tr(final_sale)} − {tr(split_sale)} = {tr(max_further_cost)} TL'dir. İşlem gideri bu tutara eşit olduğunda iki seçenek başabaş olur.",
  "Yönetim muhasebesi - ileri işlem maliyetinin başabaş üst sınırı")

q("Ortak maliyetin ayrılma noktasında satma veya ileri işleme kararında genellikle ilgisiz olmasının nedeni nedir?",
  "Karar anına kadar her iki seçenekte de katlanılmış olması",
  ["Ortak maliyetlerin hiçbir zaman stok maliyetine dâhil edilmemesi ve kayda alınmaması",
   "İleri işlem seçildiğinde geçmiş ortak maliyetin tamamının nakden geri alınabilmesi",
   "Ortak maliyetin yalnız satış fiyatına bağlı olarak gelecekte ortaya çıkacak olması",
   "Ayrılma noktasından sonra oluşan her ek maliyetin de ortak maliyet sayılması"],
  "Ayrılma noktasına kadar oluşan ortak maliyet batmıştır. Karar, yalnız ayrılma sonrası artan gelir ile artan maliyeti karşılaştırır.",
  "Yönetim muhasebesi - ortak maliyetin ileri işleme kararında batmış olması", "easy")

a_inc_rev, a_inc_cost = 64_000, 49_000
b_inc_rev, b_inc_cost = 45_000, 37_000
a_benefit, b_benefit = a_inc_rev-a_inc_cost, b_inc_rev-b_inc_cost
assert (a_benefit, b_benefit) == (15_000, 8_000)
q(f"A ürününün ileri işlem artan geliri {tr(a_inc_rev)} TL, artan maliyeti {tr(a_inc_cost)} TL; B ürününün artan geliri {tr(b_inc_rev)} TL, artan maliyeti {tr(b_inc_cost)} TL'dir. Kapasite sorunu yoksa uygun karar hangisidir?",
  "Her iki ürün de ileri işlenmelidir",
  [f"Yalnız A işlenmelidir; B'nin {tr(b_benefit)} TL pozitif artan yararı göz ardı edilmelidir",
   f"Yalnız B işlenmelidir; A'nın {tr(a_benefit)} TL pozitif artan yararı göz ardı edilmelidir",
   "İki ürün de ayrılma noktasında satılmalıdır; ortak maliyet karar için yeniden dağıtılmalıdır",
   "Yalnız ortak maliyetten daha büyük satış geliri olan ürün işlenmeli, artan maliyetler dışlanmalıdır"],
  f"A'da net artış {tr(a_benefit)} TL, B'de {tr(b_benefit)} TL'dir. Kapasite kısıtı olmadığından pozitif artan yarar sağlayan iki ürün de işlenir.",
  "Yönetim muhasebesi - birden çok ortak üründe ileri işleme analizi")

q("İleri işleme kararına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Ayrılma noktasına kadar oluşan ortak maliyet karar açısından batmıştır\n\nII. Ayrılma sonrası ek işlem maliyeti ilgili maliyettir\n\nIII. Karar için ortak maliyetin ürünlere dağıtılması zorunludur",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Karar ayrılma sonrası artan gelir ve maliyete dayanır. Geçmiş ortak maliyetin dağıtımı ürün kârlılığı raporunda kullanılabilir, ancak karar sonucunu değiştirmez.",
  "Yönetim muhasebesi - ortak ürünlerde ilgili gelir ve maliyetler")

years, old_operating, new_cost, old_sale, new_operating = 4, 75_000, 260_000, 40_000, 25_000
keep = years * old_operating
replace = new_cost - old_sale + years * new_operating
difference = replace - keep
assert (keep, replace, difference) == (300_000, 320_000, 20_000)
q(f"Eski makine {years} yıl daha kullanılabilir ve yıllık {tr(old_operating)} TL işletme gideri doğurur. Yeni makine {tr(new_cost)} TL, eski makinenin bugünkü satış bedeli {tr(old_sale)} TL ve yeni makinenin yıllık gideri {tr(new_operating)} TL'dir. Paranın zaman değeri ihmal edilirse uygun karar nedir?",
  f"Eski makineyi tutmak {tr(difference)} TL avantajlıdır",
  [f"Yeni makineyi almak {tr(keep-replace+2*difference)} TL avantajlıdır; satış geliri ters yönde kullanılmıştır",
   f"Yeni makineyi almak {tr(years*(old_operating-new_operating))} TL avantajlıdır; net yatırım maliyeti dışlanmıştır",
   f"Eski makineyi tutmak {tr(new_cost-old_sale)} TL avantajlıdır; faaliyet giderleri karşılaştırılmamıştır",
   "İki seçenek eşittir; eski makinenin satış bedeli ile faaliyet tasarrufu karar dışında bırakılmıştır"],
  f"Tutma maliyeti {tr(keep)} TL'dir. Yenileme maliyeti {tr(new_cost)} − {tr(old_sale)} + {years} × {tr(new_operating)} = {tr(replace)} TL; eski makine {tr(difference)} TL avantajlıdır.",
  "Yönetim muhasebesi - ekipman yenilemede net yatırım ve faaliyet maliyeti", "hard")

years, repair_now, old_annual, new_cost, disposal_cost, new_annual = 3, 50_000, 90_000, 220_000, 10_000, 40_000
keep = repair_now + years * old_annual
replace = new_cost + disposal_cost + years * new_annual
advantage = replace - keep
assert (keep, replace, advantage) == (320_000, 350_000, 30_000)
q(f"Eski ekipmanı tutmak için hemen {tr(repair_now)} TL bakım ve {years} yıl boyunca yıllık {tr(old_annual)} TL işletme gideri gerekir. Yeni ekipman {tr(new_cost)} TL, eskiyi sökme {tr(disposal_cost)} TL ve yıllık gider {tr(new_annual)} TL'dir. Uygun seçenek hangisidir?",
  f"Eski ekipmanı tutmak {tr(advantage)} TL avantajlıdır",
  [f"Yeni ekipmanı almak {tr(years*(old_annual-new_annual))} TL avantajlıdır; yatırım ve söküm maliyeti dışlanmıştır",
   f"Eski ekipmanı tutmak {tr(repair_now)} TL avantajlıdır; yıllık faaliyet farkları dışlanmıştır",
   f"Yeni ekipmanı almak {tr(replace-keep+advantage)} TL avantajlıdır; toplam maliyet farkının yönü ters çevrilmiştir",
   "İki seçenek eşittir; bakım, söküm ve yıllık işletme maliyetleri birbirini götürür kabul edilmiştir"],
  f"Tutma maliyeti {tr(repair_now)} + {years} × {tr(old_annual)} = {tr(keep)} TL; yenileme {tr(new_cost)} + {tr(disposal_cost)} + {years} × {tr(new_annual)} = {tr(replace)} TL'dir. Tutma {tr(advantage)} TL ucuzdur.",
  "Yönetim muhasebesi - ekipman yenilemede bakım ve söküm giderleri", "hard")

new_cost, old_sale, years = 300_000, 50_000, 5
required_annual_saving = (new_cost-old_sale)/years
assert required_annual_saving == 50_000
q(f"Yeni makinenin maliyeti {tr(new_cost)} TL, eski makinenin bugünkü satış bedeli {tr(old_sale)} TL ve karşılaştırma süresi {years} yıldır. Paranın zaman değeri ile dönem sonu değerleri ihmal edilirse yenilemenin başabaş yıllık faaliyet tasarrufu kaç TL'dir?",
  f"{tr(required_annual_saving)} TL",
  [f"{tr(new_cost/years)} TL eski makinenin satış bedelinin net yatırımdan düşülmediği tutar",
   f"{tr(old_sale/years)} TL yalnız eski makinenin yıllıklaştırılmış satış değerinin kullanıldığı tutar",
   f"{tr((new_cost+old_sale)/years)} TL satış bedelinin net yatırımdan düşülmek yerine eklendiği tutar",
   f"{tr(new_cost-old_sale)} TL net yatırımın yıllara bölünmeden yıllık tasarruf sayıldığı tutar"],
  f"Net yatırım {tr(new_cost)} − {tr(old_sale)} = {tr(new_cost-old_sale)} TL'dir. {years} yıla bölündüğünde yıllık başabaş tasarrufu {tr(required_annual_saving)} TL olur.",
  "Yönetim muhasebesi - yenileme yatırımında başabaş faaliyet tasarrufu")

lost_contribution, avoidable_fixed, restart = 210_000, 260_000, 25_000
benefit = avoidable_fixed - lost_contribution - restart
assert benefit == 25_000
q(f"Bir tesis geçici olarak kapatılırsa {tr(lost_contribution)} TL katkı kaybedilecek, {tr(avoidable_fixed)} TL sabit giderden kaçınılacak ve yeniden açılışta {tr(restart)} TL maliyet oluşacaktır. Geçici kapatmanın kâr etkisi nedir?",
  f"{tr(benefit)} TL artış",
  [f"{tr(avoidable_fixed-lost_contribution)} TL artış; yeniden açılış maliyeti dışlanmıştır",
   f"{tr(lost_contribution+restart-avoidable_fixed)} TL artış; hesaplanan net etkinin yönü ters çevrilmiştir",
   f"{tr(avoidable_fixed)} TL artış; katkı kaybı ve yeniden açılış maliyeti dışlanmıştır",
   f"{tr(lost_contribution+restart)} TL azalış; kaçınılabilir sabit gider tasarrufu dikkate alınmamıştır"],
  f"Kapatma yararı {tr(avoidable_fixed)} − {tr(lost_contribution)} − {tr(restart)} = {tr(benefit)} TL'dir.",
  "Yönetim muhasebesi - geçici durdurma kararında kaçınılabilir gider ve yeniden açılış maliyeti")

new_contribution, specific_fixed, cannibalized = 180_000, 70_000, 45_000
increase = new_contribution - specific_fixed - cannibalized
assert increase == 65_000
q(f"Yeni ürün hattı {tr(new_contribution)} TL katkı sağlayacak, {tr(specific_fixed)} TL hatta özgü sabit gider doğuracak ve mevcut ürünün katkısını {tr(cannibalized)} TL azaltacaktır. Ortak gider değişmiyorsa hattın kâr etkisi nedir?",
  f"{tr(increase)} TL artış",
  [f"{tr(new_contribution-specific_fixed)} TL artış; mevcut ürünün katkı kaybı dışlanmıştır",
   f"{tr(new_contribution-cannibalized)} TL artış; hatta özgü sabit gider dışlanmıştır",
   f"{tr(specific_fixed+cannibalized)} TL azalış; yeni hattın katkısı dikkate alınmamıştır",
   f"{tr(new_contribution+specific_fixed-cannibalized)} TL artış; yeni sabit gider katkıya eklenmiştir"],
  f"Net artış {tr(new_contribution)} − {tr(specific_fixed)} − {tr(cannibalized)} = {tr(increase)} TL'dir.",
  "Yönetim muhasebesi - yeni ürün hattında yamyamlaşma ve artan sabit gider", "hard")

q("Ekipman yenileme ve faaliyet kararlarına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Eski ekipmanın defter değeri batmış maliyettir\n\nII. Eski ekipmanın bugün vazgeçilecek satış bedeli ilgilidir\n\nIII. Dağıtılan bütün sabit giderler faaliyet kapanınca mutlaka ortadan kalkar",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Geçmiş defter değeri batmıştır; bugünkü satış bedeli seçenekler arasında değişen fırsat değeridir. Sabit giderin niteliği değil, kaçınılabilir olup olmadığı belirleyicidir.",
  "Yönetim muhasebesi - yenileme ve kapatma kararlarında ilgili maliyetler")


# ── D. Kısıtlı kaynak, ürün karması ve belirsizlik (15) ───────────────────
a_cm, a_hours, b_cm, b_hours = 56, 4, 48, 3
a_per, b_per = a_cm/a_hours, b_cm/b_hours
comparison_hours = 12
a_total = (comparison_hours//a_hours)*a_cm
b_total = (comparison_hours//b_hours)*b_cm
opportunity_loss = b_total-a_total
assert (a_per, b_per, a_total, b_total, opportunity_loss) == (14, 16, 168, 192, 24)
q(f"A mamulü birimde {tr(a_hours)} darboğaz saati kullanıp {tr(a_cm)} TL, B mamulü {tr(b_hours)} saat kullanıp {tr(b_cm)} TL katkı sağlamaktadır. Her iki üründe karşılanmamış talep varken {tr(comparison_hours)} saatin B yerine A'ya ayrılmasının fırsat kaybı kaç TL'dir?",
  f"{tr(opportunity_loss)} TL",
  [f"{tr(a_total)} TL A mamullerinin toplam katkısının fırsat kaybı sayıldığı tutar",
   f"{tr(b_total)} TL B mamullerinin toplam katkısının fırsat kaybı sayıldığı tutar",
   f"{tr(b_cm-a_cm)} TL yalnız birim katkı farkının saat kullanımından bağımsız hesaplandığı tutar",
   f"{tr(comparison_hours*(b_per+a_per))} TL iki ürünün saatlik katkılarının toplanıp kapasiteyle çarpıldığı tutar"],
  f"{tr(comparison_hours)} saatte {tr(comparison_hours//a_hours)} A, {tr(comparison_hours//b_hours)} B üretilebilir. Katkılar {tr(a_total)} ve {tr(b_total)} TL; A'yı seçmenin fırsat kaybı {tr(opportunity_loss)} TL'dir.",
  "Yönetim muhasebesi - darboğaz kapasitesinin ürünler arası fırsat maliyeti", "hard")

total_hours, b_demand = 1_800, 300
b_used = b_demand * b_hours
remaining = total_hours - b_used
a_units = remaining // a_hours
total_cm = b_demand*b_cm + a_units*a_cm
assert (b_used, remaining, a_units, total_cm) == (900, 900, 225, 27_000)
q(f"Toplam {tr(total_hours)} makine saati vardır. A ürünü {tr(a_hours)} saat ve {tr(a_cm)} TL katkı, B ürünü {tr(b_hours)} saat ve {tr(b_cm)} TL katkı sağlar; B talebi en çok {tr(b_demand)} birimdir. Talep sınırları içinde azami toplam katkı kaç TL'dir?",
  f"{tr(total_cm)} TL",
  [f"{tr((total_hours//a_hours)*a_cm)} TL bütün kapasitenin birim katkısı yüksek A'ya ayrıldığı sonuç",
   f"{tr((total_hours//b_hours)*b_cm)} TL B talep üst sınırının göz ardı edildiği sonuç",
   f"{tr(b_demand*b_cm)} TL B talebi karşılandıktan sonra kalan kapasitenin kullanılmadığı sonuç",
   f"{tr(b_demand*b_cm+(remaining//b_hours)*b_cm)} TL kalan kapasitenin B talep sınırı aşılarak kullanıldığı sonuç"],
  f"Saat başına katkısı yüksek B'den {tr(b_demand)} birim üretilir ve {tr(b_used)} saat kullanılır. Kalan {tr(remaining)} saatte {tr(a_units)} A üretilir; toplam katkı {tr(total_cm)} TL'dir.",
  "Yönetim muhasebesi - talep sınırı altında optimal ürün karması", "hard")

c_cm, c_kg, d_cm, d_kg = 36, 3, 28, 2
c_per, d_per = c_cm/c_kg, d_cm/d_kg
assert (c_per, d_per) == (12, 14)
q(f"Hammadde kısıtlıdır. C ürünü birimde {tr(c_cm)} TL katkı için {tr(c_kg)} kg; D ürünü {tr(d_cm)} TL katkı için {tr(d_kg)} kg kullanmaktadır. Diğer koşullar eşitse hangisine öncelik verilmelidir?",
  "D ürününe öncelik verilmelidir",
  [f"C ürününe öncelik verilmelidir; yalnız {tr(c_cm)} TL birim katkı payı karşılaştırılmalıdır",
   "İki ürün aynı önceliktedir; kilogram başına katkı yerine yalnız kullanılan toplam malzeme izlenmelidir",
   "C ürününe öncelik verilmelidir; daha fazla malzeme tüketmesi daha yüksek verimlilik kabul edilmelidir",
   "Yalnız birim satış fiyatı karşılaştırılmalı, katkı payı ve malzeme tüketimi karar dışında bırakılmalıdır"],
  f"Kilogram başına katkı C'de {tr(c_cm)} / {tr(c_kg)} = {tr(c_per)} TL, D'de {tr(d_cm)} / {tr(d_kg)} = {tr(d_per)} TL'dir. Kıt hammadde önce D'ye ayrılır.",
  "Yönetim muhasebesi - kısıtlı hammadde birimi başına katkı")

q("Kısıtlı kaynak altında ürün karmasına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Ürünler darboğaz birimi başına katkıya göre sıralanır\n\nII. Birim katkı payı en yüksek ürün her durumda önce üretilir\n\nIII. Talep üst sınırları kapasite dağıtımında dikkate alınır",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "Yalnız II"],
  "Birim katkı tek başına yeterli değildir; katkı kısıtlı kaynak tüketimine bölünür. En yüksek oranlı ürüne talebi kadar kaynak ayrıldıktan sonra sıradakine geçilir.",
  "Yönetim muhasebesi - darboğaz katkısı ve talep sınırı")

extra_hours, cm_hour, purchase_hour = 400, 16, 11
benefit = extra_hours * (cm_hour-purchase_hour)
assert benefit == 2_000
q(f"Darboğaz kapasitesine ek {tr(extra_hours)} saat alınabilir. Bu saatler birim saat başına {tr(cm_hour)} TL ek katkı yaratacak, satın alma maliyeti {tr(purchase_hour)} TL/saat olacaktır. Talep yeterliyse ek kapasitenin net yararı kaç TL'dir?",
  f"{tr(benefit)} TL",
  [f"{tr(extra_hours*cm_hour)} TL kapasiteyi edinme maliyetinin dışlandığı brüt katkı",
   f"{tr(extra_hours*purchase_hour)} TL kapasite maliyetinin net yarar kabul edildiği sonuç",
   f"{tr(extra_hours*(cm_hour+purchase_hour))} TL katkı ile kapasite maliyetinin toplandığı sonuç",
   f"{tr(cm_hour-purchase_hour)} TL yalnız saatlik net yararın toplam dönem sonucu sayıldığı tutar"],
  f"Saatlik net yarar {tr(cm_hour)} − {tr(purchase_hour)} = {tr(cm_hour-purchase_hour)} TL; {tr(extra_hours)} saatte {tr(benefit)} TL'dir.",
  "Yönetim muhasebesi - ek darboğaz kapasitesinin gölge değeri")

q(f"Darboğazdaki ek bir makine saati, karşılanmamış talep bulunan üründe {tr(cm_hour)} TL katkı yaratıyorsa ek saatin toplam edinme maliyeti en çok kaç TL olabilir?",
  f"{tr(cm_hour)} TL",
  [f"{tr(cm_hour*2)} TL katkının iki kez sayıldığı azami maliyet",
   f"{tr(cm_hour-purchase_hour)} TL mevcut teklifin net yararının azami maliyet kabul edildiği tutar",
   f"{tr(purchase_hour)} TL yalnız mevcut tedarikçi fiyatının ekonomik üst sınır kabul edildiği tutar",
   "0 TL; darboğaz kapasitesinin hiçbir koşulda ekonomik değeri bulunmadığı varsayımı"],
  f"Karşılanmamış talep sürdüğü sürece ek saatin marjinal yararı {tr(cm_hour)} TL'dir. Maliyet bu tutara eşit olduğunda başabaş olunur.",
  "Yönetim muhasebesi - darboğaz kaynağının marjinal değeri")

material, f_demand, f_kg, f_cm, e_kg, e_cm = 2_400, 800, 2, 22, 5, 30
f_used = f_demand*f_kg
remaining = material-f_used
e_units = remaining//e_kg
total = f_demand*f_cm + e_units*e_cm
assert (f_used, remaining, e_units, total) == (1_600, 800, 160, 22_400)
q(f"Toplam {tr(material)} kg malzeme vardır. E ürünü {tr(e_kg)} kg ile {tr(e_cm)} TL, F ürünü {tr(f_kg)} kg ile {tr(f_cm)} TL katkı sağlar. F talebi en çok {tr(f_demand)} birimdir. Azami toplam katkı payı kaç TL'dir?",
  f"{tr(total)} TL",
  [f"{tr((material//e_kg)*e_cm)} TL bütün malzemenin birim katkısı yüksek E'ye ayrıldığı sonuç",
   f"{tr((material//f_kg)*f_cm)} TL F ürününün talep sınırının göz ardı edildiği sonuç",
   f"{tr(f_demand*f_cm)} TL F talebi karşılandıktan sonra kalan malzemenin kullanılmadığı sonuç",
   f"{tr(f_demand*f_cm+(remaining//f_kg)*f_cm)} TL kalan malzemenin F talebi aşılarak kullanıldığı sonuç"],
  f"Kg başına katkısı F'de {tr(f_cm/f_kg)} TL, E'de {tr(e_cm/e_kg)} TL'dir. Önce {tr(f_demand)} F, kalan {tr(remaining)} kg ile {tr(e_units)} E üretilir; toplam {tr(total)} TL'dir.",
  "Yönetim muhasebesi - hammadde kısıtı ve talep üst sınırı", "hard")

high_p, high_profit, low_p, low_loss = 0.60, 150_000, 0.40, 30_000
expected = high_p*high_profit-low_p*low_loss
assert expected == 78_000
q(f"Bir proje yüksek talepte %{tr(high_p*100)} olasılıkla {tr(high_profit)} TL kâr, düşük talepte %{tr(low_p*100)} olasılıkla {tr(low_loss)} TL zarar sağlayacaktır. Projenin beklenen parasal değeri kaç TL'dir?",
  f"{tr(expected)} TL kâr",
  [f"{tr(high_p*high_profit)} TL kâr; düşük talepteki beklenen zarar dışlanmıştır",
   f"{tr(high_p*high_profit+low_p*low_loss)} TL kâr; zarar tutarı pozitif getiri gibi eklenmiştir",
   f"{tr(high_profit-low_loss)} TL kâr; olasılıklar tamamen göz ardı edilmiştir",
   f"{tr(low_p*low_loss)} TL zarar; yüksek talepteki beklenen kâr dışlanmıştır"],
  f"Beklenen değer %{tr(high_p*100)} × {tr(high_profit)} − %{tr(low_p*100)} × {tr(low_loss)} = {tr(expected)} TL kârdır.",
  "Yönetim muhasebesi - belirsizlik altında beklenen parasal değer", "hard")

high_p, low_p = 0.40, 0.60
x_high, x_low, y_high, y_low = 180_000, 20_000, 120_000, 70_000
x_ev = high_p*x_high+low_p*x_low
y_ev = high_p*y_high+low_p*y_low
advantage = y_ev-x_ev
assert (x_ev, y_ev, advantage) == (84_000, 90_000, 6_000)
q(f"Yüksek talep olasılığı %{tr(high_p*100)}, düşük talep olasılığı %{tr(low_p*100)}'tır. X seçeneğinin kârları sırasıyla {tr(x_high)} ve {tr(x_low)} TL; Y'nin kârları {tr(y_high)} ve {tr(y_low)} TL'dir. Beklenen değere göre sonuç nedir?",
  f"Y seçeneği {tr(advantage)} TL üstün",
  [f"X seçeneği {tr(x_high-y_high)} TL üstün; yalnız yüksek talep durumu karşılaştırılmıştır",
   f"Y seçeneği {tr(y_low-x_low)} TL üstün; yalnız düşük talep durumu karşılaştırılmıştır",
   f"X seçeneği {tr(y_ev-x_ev)} TL üstün; beklenen değer farkının yönü ters çevrilmiştir",
   "İki seçenek eşittir; durum olasılıkları kâr sonuçlarına uygulanmadan ortalama alınmıştır"],
  f"X'in beklenen değeri {tr(x_ev)} TL, Y'nin {tr(y_ev)} TL'dir. Y seçeneği {tr(advantage)} TL daha yüksek beklenen değer sağlar.",
  "Yönetim muhasebesi - alternatiflerin olasılık ağırlıklı beklenen değerle seçimi", "hard")

units, price, variable, fixed = 1_000, 70, 52, 12_000
base_profit = units*(price-variable)-fixed
max_variable = price-fixed/units
assert base_profit == 6_000 and max_variable == 58
q(f"Bir sipariş {tr(units)} birim, birim fiyatı {tr(price)} TL, tahmini değişken maliyeti {tr(variable)} TL ve özel sabit gideri {tr(fixed)} TL'dir. Diğer veriler sabitken siparişin başabaş olacağı en yüksek birim değişken maliyet kaç TL'dir?",
  f"{tr(max_variable)} TL",
  [f"{tr(variable)} TL yalnız temel tahminin başabaş değeri kabul edildiği tutar",
   f"{tr(price)} TL satış fiyatının tamamının değişken maliyet sınırı kabul edildiği tutar",
   f"{tr(price+fixed/units)} TL özel sabit gider payının satış fiyatına eklendiği tutar",
   f"{tr(fixed/units)} TL yalnız birim sabit gider payının değişken maliyet sınırı sayıldığı tutar"],
  f"Başabaşta {tr(units)} × ({tr(price)} − değişken maliyet) = {tr(fixed)} olur. Değişken maliyet {tr(price)} − {tr(fixed/units)} = {tr(max_variable)} TL'dir.",
  "Yönetim muhasebesi - özel sipariş duyarlılığı ve başabaş değişken maliyeti", "hard")

q("Duyarlılık analizinin belirsizlik altındaki bir yönetim kararına temel katkısı nedir?",
  "Kritik varsayımlardaki değişimin sonucu nasıl etkilediğini göstermek",
  ["Her olası durumun gerçekleşme olasılığını kesin olarak belirleyip belirsizliği bütünüyle kaldırmak",
   "Geçmişte katlanılmış maliyetleri gelecekteki nakit akışlarına dönüştürerek karara yeniden eklemek",
   "Bütün değişkenleri aynı anda sabitleyip yalnız tek bir sonuç bulunmasını zorunlu hâle getirmek",
   "En yüksek satış gelirli seçeneği maliyet ve kapasite koşullarından bağımsız biçimde seçmek"],
  "Duyarlılık analizi; fiyat, maliyet, talep veya kapasite gibi kritik varsayımlar değiştiğinde karar sonucunun ne ölçüde değiştiğini gösterir.",
  "Yönetim muhasebesi - karar modellerinde duyarlılık analizi")

q("Doğrusal ürün karması modelinde bir kapasite kısıtının bağlayıcı olması neyi ifade eder?",
  "Optimal çözümde kaynağın tamamen kullanıldığını",
  ["Kaynağın optimal çözümde hiç kullanılmadığını ve sınırsız boş kapasite bulunduğunu",
   "Ürünlerin katkı paylarının her üretim düzeyinde zorunlu olarak birbirine eşit olduğunu",
   "Kısıta ait kapasitenin artırılmasının hiçbir aralıkta ekonomik değer yaratamayacağını",
   "Bütün talep sınırlarının kaldırıldığını ve sınırsız satış yapılabileceğini"],
  "Bağlayıcı kısıtta kullanılabilir kaynak bütünüyle tüketilir. Geçerli aralıkta ek birimin değeri gölge fiyatla ölçülebilir.",
  "Yönetim muhasebesi - doğrusal programlamada bağlayıcı kısıt ve gölge fiyat")

offered_hours, cost, useful_hours, benefit_hour = 600, 8_000, 400, 14
incremental_benefit = useful_hours*benefit_hour
net = incremental_benefit-cost
assert incremental_benefit == 5_600 and net == -2_400
q(f"Paket halinde {tr(offered_hours)} ek kapasite saati {tr(cost)} TL'ye alınabilir; ancak mevcut talep nedeniyle yalnız {tr(useful_hours)} saat kullanılabilecektir. Kullanılabilen her saat {tr(benefit_hour)} TL katkı yaratır. Satın almanın net etkisi nedir?",
  f"Kâr {tr(-net)} TL azalır",
  [f"Kâr {tr(offered_hours*benefit_hour-cost)} TL artar; kullanılmayacak saatler de katkı yaratmış sayılmıştır",
   f"Kâr {tr(incremental_benefit)} TL artar; kapasite paketinin satın alma maliyeti dışlanmıştır",
   f"Kâr {tr(cost)} TL azalır; kullanılabilir saatlerin sağladığı katkı dışlanmıştır",
   "Kâr değişmez; kapasite maliyeti ile yararlı saatlerin katkısı karşılaştırılmamıştır"],
  f"Yalnız kullanılabilecek {tr(useful_hours)} saat yarar üretir: {tr(incremental_benefit)} TL. {tr(cost)} TL maliyet sonrası kâr {tr(-net)} TL azalır; paket alınmamalıdır.",
  "Yönetim muhasebesi - talep sınırı altında ek kapasite satın alma kararı", "hard")

high_p, low_p = 0.50, 0.50
x_high, x_low, y_high, y_low = 160_000, 40_000, 110_000, 80_000
x_ev = high_p*x_high + low_p*x_low
y_ev = high_p*y_high + low_p*y_low
perfect_ev = high_p*max(x_high, y_high) + low_p*max(x_low, y_low)
evpi = perfect_ev - max(x_ev, y_ev)
assert (x_ev, y_ev, perfect_ev, evpi) == (100_000, 95_000, 120_000, 20_000)
q(f"Yüksek ve düşük talep olasılıkları ayrı ayrı %{tr(high_p*100)}'dir. X seçeneğinin kârları {tr(x_high)} ve {tr(x_low)} TL; Y'nin kârları {tr(y_high)} ve {tr(y_low)} TL'dir. Tam bilginin beklenen değeri en çok kaç TL'dir?",
  f"{tr(evpi)} TL",
  [f"{tr(perfect_ev)} TL durum önceden bilindiğindeki toplam beklenen değerin bilgi değeri sayıldığı sonuç",
   f"{tr(x_ev)} TL en yüksek mevcut beklenen seçeneğin bilgi değeri kabul edildiği sonuç",
   f"{tr(y_ev)} TL daha düşük beklenen seçeneğin bilgi değeri kabul edildiği sonuç",
   f"{tr(x_ev-y_ev)} TL yalnız iki seçeneğin beklenen değer farkının bilgi değeri sayıldığı sonuç"],
  f"Bilgi olmadan en yüksek beklenen değer {tr(max(x_ev,y_ev))} TL'dir. Durum önceden bilinse beklenen değer {tr(perfect_ev)} TL olur; fark {tr(evpi)} TL tam bilgi için azami bedeldir.",
  "Yönetim muhasebesi - tam bilginin beklenen değeri", "hard")

units, price, variable, special_pack, displaced, lost_cm = 500, 66, 46, 4, 200, 24
special_cm = units*(price-variable-special_pack)
opportunity = displaced*lost_cm
impact = special_cm-opportunity
assert (special_cm, opportunity, impact) == (8_000, 4_800, 3_200)
q(f"İşletmenin {tr(300)} birim atıl kapasitesi vardır. {tr(units)} birim özel siparişin fiyatı {tr(price)} TL, değişken maliyeti {tr(variable)} TL ve özel paket gideri {tr(special_pack)} TL'dir. Fazla {tr(displaced)} birim normal satışı birim {tr(lost_cm)} TL katkıyla azaltacaktır. Siparişin kâr etkisi nedir?",
  f"{tr(impact)} TL artış",
  [f"{tr(special_cm)} TL artış; kaybedilen normal satış katkısı dışlanmıştır",
   f"{tr(opportunity)} TL azalış; özel siparişin kendi katkısı dışlanmıştır",
   f"{tr(units*(price-variable)-opportunity)} TL artış; özel paket gideri dışlanmıştır",
   f"{tr(special_cm+opportunity)} TL artış; fırsat maliyeti sipariş katkısına eklenmiştir"],
  f"Sipariş katkısı {tr(units)} × ({tr(price)} − {tr(variable)} − {tr(special_pack)}) = {tr(special_cm)} TL'dir. Kaybedilen katkı {tr(displaced)} × {tr(lost_cm)} = {tr(opportunity)} TL; net artış {tr(impact)} TL'dir.",
  "Yönetim muhasebesi - kısmen atıl kapasitede özel sipariş ve yer değiştiren satış", "hard")


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
                "styleRef": "2026/1 test biçimi",
                "legislationRef": item["ref"],
            },
            "tags": ["Demo Soru", "2026 Formatı", "Konu Havuzu", LBL],
            "difficulty": item["difficulty"],
            "updatedAt": "2026-07-16T00:00:00Z",
            "examPeriod": "2026/1 formatına uyumlu",
            "legislationVersion": "2026-07-16",
            "sourceUpdatedAt": "2026-07-16T00:00:00Z",
            "isPremium": False,
            "isActive": True,
        })
    for output_path in OUTS:
        with open(output_path, "w", encoding="utf-8") as fh:
            json.dump(out, fh, ensure_ascii=False, indent=2)
    marker = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    premises = sum(1 for item in out if len(marker.findall(item["question"])) >= 2)
    print(f"yazıldı: {len(out)} soru | öncüllü {premises} | harf {''.join(item['correctAnswer'] for item in out)[:40]}…")
