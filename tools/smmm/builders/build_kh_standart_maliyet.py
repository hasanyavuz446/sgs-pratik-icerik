# -*- coding: utf-8 -*-
"""Yeterlilik KONU HAVUZU — Maliyet Muhasebesi / Standart Maliyet ve Sapmalar.

60 özgün soru = 3×20. Malzeme, işçilik, değişken ve sabit GÜG sapmaları;
karma/verim, boş zaman ve maliyet uzlaştırması dâhil. Aritmetik Python'da
hesaplanır. Seçenekler doğal uzunlukta, çözümde harf atfı yoktur.
"""
import json
import random
import re
from pathlib import Path

L, T, LBL = "maliyet_muhasebesi", "standart_maliyet", "Standart Maliyet ve Sapmalar"
PREFIX, SEED = "kh-mal-standart", 20260906
CONTENT_ROOT = Path(__file__).resolve().parents[3]
PROJECTS_ROOT = CONTENT_ROOT.parent
FILENAME = "questions_topic_standart_maliyet_2026.json"
OUTS = (
    CONTENT_ROOT / "content" / "yeterlilik" / FILENAME,
    PROJECTS_ROOT / "smmm_sgs_pratik" / "assets" / "content" / "yeterlilik" / FILENAME,
)
UPDATED_AT = "2026-07-17T00:00:00Z"
LEGISLATION_VERSION = (
    "KGK TFRS 2026 Seti (Mavi Kitap) – TMS 2; "
    "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı"
)

Q = []


def q(stem, correct, distractors, why, ref, difficulty="medium"):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why,
                  ref=ref, difficulty=difficulty))


def tr(value):
    if isinstance(value, float) and abs(value - round(value)) < 1e-9:
        value = round(value)
    return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".").removesuffix(",00")


# ── A. Standartların kurulması, güncellenmesi ve sorumluluk (15) ──────────
q("TMS 2 kapsamında standart maliyet tekniğinin stokların ölçümünde kullanılabilmesi için temel koşul nedir?",
  "Sonucun gerçek maliyete yakın olması",
  ["Standartların hiçbir dönemde gözden geçirilmeden ilk belirlendiği tutarda kalması",
   "Fiilî maliyet kayıtlarının tamamen kaldırılıp yalnız satış fiyatlarının izlenmesi",
   "Her maliyet unsurunda ideal ve erişilmesi imkânsız performansın zorunlu tutulması",
   "Standart maliyet ile net gerçekleşebilir değerin her koşulda aynı tutarda olması"],
  "TMS 2, standart maliyet tekniğine kolaylık amacıyla, sonuçlar maliyete yakınsa izin verir.",
  "TMS 2 par. 21 - standart maliyet tekniğinin gerçek maliyete yaklaşması", "easy")

q("Uygulanabilir bir standart maliyet kartında direkt malzeme için hangi iki unsur birlikte yer alır?",
  "Standart miktar ve standart fiyat",
  ["Fiilî satış miktarı ile müşterinin ortalama ödeme vadesi birlikte",
   "Bütçelenen kâr oranı ile işletmenin banka kredisi faiz oranı birlikte",
   "Mamulün piyasa değeri ile ortakların sermaye payları birlikte",
   "Yalnız geçmiş dönemin toplam maliyeti ve hiçbir fiziksel tüketim ölçüsü olmadan"],
  "Direkt malzeme standardı, birim çıktı için olması gereken fiziksel miktar ile standart birim fiyatın bileşimidir.",
  "TMS 2 par. 21 - normal malzeme düzeyleri; standart maliyet kartı", "easy")

q("Kusursuz çalışma varsayımıyla kurulan ölçü ile verimli koşullardaki kaçınılmaz duruşlara pay veren ölçü birbirinden hangi unsur nedeniyle ayrılır?",
  "Normal verimsizliklere tanınan pay",
  ["İdeal standardın yalnız satış gelirini, ulaşılabilir standardın yalnız nakit akışını ölçmesi",
   "İdeal standardın fiilî sonuçtan sonra, ulaşılabilir standardın ise satıştan sonra belirlenmesi",
   "Ulaşılabilir standardın hiçbir teknik veriye dayanmayıp bütünüyle rastgele seçilmesi",
   "İki standardın da aynı kayıp ve kapasite varsayımlarını zorunlu olarak taşıması"],
  "İdeal standart kusursuz koşulları varsayar; ulaşılabilir standart verimli çalışmada kaçınılmaz duruş ve normal kayıpları dikkate alabilir.",
  "TMS 2 par. 21 - normal malzeme, işçilik, verimlilik ve kapasite düzeyleri")

q("Standart maliyet sistemine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Standartlar teknik ve ekonomik verilere dayanmalıdır\n\nII. Fiilî sonuçlarla karşılaştırma sapmaları görünür kılar\n\nIII. Her aleyhte sapma tek başına ilgili yöneticinin kusurunu kesin kanıtlar",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Standartlar ölçülü hedeflerdir ve sapma kontrol sinyali üretir. Sorumluluk için neden, kontrol edilebilirlik ve bölümler arası etkiler ayrıca incelenir.",
  "TMS 2 par. 21; maliyet muhasebesi - standart maliyet ve sorumluluk analizi")

q("Hammadde teknolojisi değiştiği hâlde eski tüketim standardının kullanılmaya devam edilmesi hangi riski doğurur?",
  "Sapmaların performansı yanlış göstermesi",
  ["Bütün fiilî malzeme tüketiminin otomatik olarak satış hasılatına dönüşmesi",
   "Standartların eskimesiyle üretim miktarının fiziksel olarak sıfırlanması",
   "Direkt işçilik giderlerinin zorunlu olarak maddi duran varlık hesabına geçmesi",
   "Müşteri alacaklarının standart tüketim miktarı kadar kendiliğinden kapanması"],
  "Eski standart yeni süreçte olması gereken tüketimi temsil etmez; lehte veya aleyhte görünen fark gerçek performans sinyali olmayabilir.",
  "TMS 2 par. 21 - standartların düzenli gözden geçirilmesi ve gerekirse değiştirilmesi")

q("Standart maliyet kartının üretim başlamadan önce hazırlanmasının temel yönetim yararı nedir?",
  "Olması gereken kaynak tüketimini önceden tanımlamak",
  ["Fiilî maliyet kayıtlarına ihtiyaç bırakmadan bütün muhasebe belgelerini kaldırmak",
   "Satış fiyatını ve müşteri talebini üretim miktarından bağımsız biçimde garanti etmek",
   "Her sapmayı oluşmadan önce kesin olarak sıfırlayıp verimsizliği imkânsız kılmak",
   "Stokların net gerçekleşebilir değerini bütün dönemlerde maliyetle eşitlemek"],
  "Standart kart, çıktı başına olması gereken miktar, süre, fiyat ve oranları önceden tanımlar; fiilî sonuç için karşılaştırma tabanı oluşturur.",
  "TMS 2 par. 21 - standart maliyetlerin normal düzeylere göre önceden kurulması")

q("Aleyhte malzeme fiyat sapmasıyla birlikte lehte kullanım sapması görülmesi hangi olasılığı araştırmayı gerektirir?",
  "Daha kaliteli malzemenin verimi artırmış olmasını",
  ["Malzeme fiyatının üretim verimliliğiyle hiçbir koşulda ilişkili olamayacağı varsayımını",
   "Lehte kullanımın bütün satın alma kararlarını kendiliğinden hatasız hâle getirmesini",
   "Aleyhte fiyatın yalnız satış bölümünden kaynaklandığının kesin kabul edilmesini",
   "İki sapmanın ayrı dönemlere aitmiş gibi hiçbir ortak neden aranmadan raporlanmasını"],
  "Daha pahalı fakat kaliteli malzeme daha az tüketim veya fire yaratabilir; fiyat ve kullanım sapmaları birlikte yorumlanmalıdır.",
  "Maliyet muhasebesi - malzeme fiyat ve kullanım sapmalarının etkileşimi", "hard")

q("Bir sapmanın sorumluluk merkezine aktarılmasından önce hangi soru öncelikle yanıtlanmalıdır?",
  "Nedenin merkez tarafından kontrol edilip edilemediği",
  ["Merkez yöneticisinin satış hasılatının tamamını kişisel olarak tahsil edip etmediği",
   "İşletmenin dönem sonunda banka hesabında standart maliyet kadar para bulunup bulunmadığı",
   "Mamulün satış fiyatının standart direkt işçilik saatine eşit olup olmadığı",
   "Sorumluluk merkezinin bütün diğer bölümlerden daha yüksek bütçeye sahip olup olmadığı"],
  "Fiyat, kalite, makine arızası veya üretim planı başka merkezlerin kararlarından etkilenebilir; değerlendirme kontrol edilebilir nedene dayanmalıdır.",
  "Maliyet muhasebesi - sorumluluk muhasebesi ve kontrol edilebilirlik")

q("Fiilî faaliyet için hazırlanmış esnek bütçenin sabit bütçeye göre üstünlüğü nedir?",
  "Faaliyet hacmi etkisini harcama etkisinden ayırması",
  ["Fiilî maliyetleri hiç ölçmeden bütün sapmaları otomatik olarak lehte göstermesi",
   "Bütün sabit giderleri faaliyet arttıkça aynı oranda değişken kabul etmesi",
   "Standart miktar ve süreleri müşterilerin ödeme vadelerine göre yeniden yazması",
   "Üretim hacmi ne olursa olsun fiilî giderle aynı sonucu vermeyi garanti etmesi"],
  "Esnek bütçe değişken maliyeti fiilî faaliyet düzeyine uyarlar; böylece hacim değişimi ile gerçek harcama farkı ayrılabilir.",
  "TMS 2 par. 21; maliyet muhasebesi - esnek bütçe ve sapma analizi")

q("Bir standardın sürekli kolayca aşılması hangi iki olasılığı gündeme getirir?",
  "Standardın gevşek veya sürecin kalıcı olarak iyileşmiş olması",
  ["Fiilî maliyet kayıtlarının bütünüyle yanlış ve satışların gerçekleşmemiş olması",
   "Bütün lehte sapmaların anormal kayıp sayılması ve stoktan çıkarılması zorunluluğu",
   "Standart maliyet tekniğinin hiçbir üretim işletmesinde kullanılamayacağı sonucu",
   "Mamul fiyatının standart tutarın altında belirlenmesinin yasal olarak zorunlu olması"],
  "Tekrarlanan lehte sonuç gerçek iyileşmeden veya güncelliğini yitirmiş gevşek standarttan kaynaklanabilir; ikisi ayrıştırılmalıdır.",
  "TMS 2 par. 21 - standartların düzenli incelenmesi ve güncellenmesi")

q("Standart fiyat belirlenirken beklenen iskonto ve olağan taşıma maliyetlerinin dikkate alınması neyi sağlar?",
  "Satın alma koşullarını gerçekçi biçimde yansıtmayı",
  ["Malzeme kullanım sapmasının yalnız satış hacmine göre hesaplanmasını",
   "Direkt işçilik süresinin malzeme fiyatından otomatik olarak türetilmesini",
   "Bütün fiyat değişimlerinin üretim bölümüne yüklenmesini ve tedarikin dışlanmasını",
   "Fiilî alış belgelerinin hiçbir dönemde kaydedilmemesini ve karşılaştırmanın kaldırılmasını"],
  "Standart fiyat, verimli satın alma koşullarında beklenen net edinme maliyetini temsil etmelidir.",
  "TMS 2 par. 11 ve 21 - satın alma maliyeti ile gerçekçi standart fiyat")

q("Standartların oluşturulmasına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Mühendislik çalışmaları miktar ve süre standardını destekleyebilir\n\nII. Satın alma verileri standart fiyatı destekleyebilir\n\nIII. Normal kapasite sabit GÜG oranının kurulmasında kullanılabilir",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Teknik tüketim ve zaman etütleri fiziksel standartları, tedarik verileri fiyatı, normal kapasite ise sabit genel üretim gideri oranını destekler.",
  "TMS 2 par. 13 ve 21 - normal düzeyler, kapasite ve standart maliyet tekniği")

q("Standart maliyetin finansal raporlamada kullanılması, fiilî maliyetlerin izlenmesini neden ortadan kaldırmaz?",
  "Yakınlık ve sapmalar fiilî verilerle doğrulanır",
  ["Standart maliyet yalnız satış geliri hesabında kullanılabildiği ve stokla ilgisiz olduğu için",
   "Fiilî maliyetler her durumda standart maliyetle aynı çıkmak zorunda olduğu için",
   "TMS 2 fiilî üretim verilerinin kaydedilmesini açıkça yasakladığı için",
   "Standartların hiçbir dönemde gözden geçirilmesi gerekmediği ve fark oluşmadığı için"],
  "Standart tekniğin maliyete yaklaşması, fiilî sonuçların ölçülmesi, sapmaların analizi ve standartların güncellenmesiyle sınanır.",
  "TMS 2 par. 21 - standart maliyetlerin gerçek maliyete yakınlığının düzenli değerlendirilmesi")

q("Standart maliyet raporunda yalnız net toplam sapmanın gösterilmesi hangi bilgiyi gizleyebilir?",
  "Birbirini dengeleyen lehte ve aleyhte nedenleri",
  ["Fiilî üretim miktarının her durumda standart miktardan büyük olmasını",
   "Satış hasılatının standart maliyetle zorunlu olarak aynı tutarda bulunmasını",
   "Müşterilerin ödeme vadelerinin üretim saatlerine eşit olmasını",
   "Sabit genel üretim giderlerinin hiçbir zaman sapma üretmemesini"],
  "Örneğin lehte fiyat sapması aleyhte kullanım sapmasını örtebilir; bileşenler ayrı gösterilmeden kök neden görülmez.",
  "Maliyet muhasebesi - sapmaların bileşenlerine ayrılması")

q("Standart değiştirilirken geçmiş dönem sapmalarının yeni standarda göre geriye dönük silinmesi neden uygun değildir?",
  "Dönem performansı o dönemde geçerli hedefle ölçülmüştür",
  ["Geçmiş sapmaların yalnız satış fiyatına ait olması ve maliyetle ilgisinin bulunmaması nedeniyle",
   "Yeni standardın bütün geçmiş fiilî maliyetleri fiziksel olarak değiştirmesi nedeniyle",
   "Standart güncellemesinin muhasebe kayıtlarının tamamını kendiliğinden iptal etmesi nedeniyle",
   "Her standart değişikliğinin geçmiş satış hasılatını nakden geri almayı gerektirmesi nedeniyle"],
  "Yeni bilgi ileriye dönük standardı değiştirir; geçmiş dönemin fiilî sonucu o dönemde geçerli ve onaylı standartla karşılaştırılmıştır.",
  "TMS 2 par. 21 - standartların düzenli gözden geçirilmesi ve dönemsel tutarlılık", "hard")


# ── B. Direkt malzeme fiyat, kullanım, karma ve verim sapmaları (15) ─────
output, std_kg_per_unit, sp = 1_600, 4.5, 32
sq = output * std_kg_per_unit
std_mat_cost = sq * sp
assert (sq, std_mat_cost) == (7_200, 230_400)
q(f"Fiilî üretim {tr(output)} birim, birim başına izin verilen standart tüketim {tr(std_kg_per_unit)} kg ve standart fiyat {tr(sp)} TL/kg'dır. Fiilî üretim için standart malzeme miktarı kaç kg'dır?",
  f"{tr(sq)} kg",
  [f"{tr(output)} kg çıktı adedinin doğrudan standart miktar kabul edildiği sonuç",
   f"{tr(std_kg_per_unit)} kg yalnız tek mamulün standardının dönem toplamı sayıldığı miktar",
   f"{tr(output+std_kg_per_unit)} kg çıktı ile birim standardın toplanmasıyla bulunan sonuç",
   f"{tr(std_mat_cost)} kg standart fiyatla çarpılan parasal tutarın fiziksel miktar sayıldığı sonuç"],
  f"Fiilî üretime izin verilen miktar {tr(output)} × {tr(std_kg_per_unit)} = {tr(sq)} kg'dır.",
  "TMS 2 par. 21 - normal malzeme düzeyleri; fiilî üretim için standart miktar")

aq, ap = 7_500, 34
actual_mat_cost = aq * ap
price_var = (ap-sp)*aq
usage_var = (aq-sq)*sp
total_mat_var = actual_mat_cost-std_mat_cost
assert (actual_mat_cost, price_var, usage_var, total_mat_var) == (255_000, 15_000, 9_600, 24_600)
q(f"Fiilen kullanılan {tr(aq)} kg malzemenin fiyatı {tr(ap)} TL/kg, standart fiyatı {tr(sp)} TL/kg'dır. Fiyat sapması nedir?",
  f"{tr(price_var)} TL aleyhte",
  [f"{tr(usage_var)} TL aleyhte; miktar farkı standart fiyatla değerlenir",
   f"{tr(price_var)} TL lehte; standarttan yüksek fiyat olumlu kabul edilir",
   f"{tr(actual_mat_cost)} TL aleyhte; fiilî maliyetin tamamı sapma sayılır",
   f"{tr((ap-sp)*sq)} TL aleyhte; fiyat farkı fiilî yerine standart miktarla çarpılır"],
  f"Fiyat sapması ({tr(ap)} − {tr(sp)}) × {tr(aq)} = {tr(price_var)} TL'dir. Fiilî fiyat yüksek olduğundan aleyhtedir.",
  "Maliyet muhasebesi - direkt malzeme fiyat sapması")

q(f"Fiilî kullanım {tr(aq)} kg, fiilî üretim için standart miktar {tr(sq)} kg ve standart fiyat {tr(sp)} TL/kg'dır. Kullanım sapması nedir?",
  f"{tr(usage_var)} TL aleyhte",
  [f"{tr(price_var)} TL aleyhte; fiyat farkı kullanım sapması olarak raporlanır",
   f"{tr(usage_var)} TL lehte; standarttan fazla tüketim olumlu kabul edilir",
   f"{tr((aq-sq)*ap)} TL aleyhte; miktar farkı fiilî fiyatla değerlenir",
   f"{tr(actual_mat_cost)} TL aleyhte; fiilî malzeme maliyetinin tamamı sapma sayılır"],
  f"Kullanım sapması ({tr(aq)} − {tr(sq)}) × {tr(sp)} = {tr(usage_var)} TL aleyhtedir.",
  "Maliyet muhasebesi - direkt malzeme miktar/kullanım sapması")

q(f"Fiilî malzeme maliyeti {tr(actual_mat_cost)} TL ve fiilî üretimin standart malzeme maliyeti {tr(std_mat_cost)} TL'dir. Toplam direkt malzeme sapması nedir?",
  f"{tr(total_mat_var)} TL aleyhte",
  [f"{tr(total_mat_var)} TL lehte; yüksek fiilî maliyet olumlu kabul edilir",
   f"{tr(price_var)} TL aleyhte; yalnız fiyat bileşeni toplam sapma sayılır",
   f"{tr(usage_var)} TL aleyhte; yalnız kullanım bileşeni toplam sapma sayılır",
   f"{tr(actual_mat_cost+std_mat_cost)} TL aleyhte; fiilî ve standart maliyetler toplanır"],
  f"Toplam sapma {tr(actual_mat_cost)} − {tr(std_mat_cost)} = {tr(total_mat_var)} TL aleyhtedir. Ayrıca {tr(price_var)} + {tr(usage_var)} = {tr(total_mat_var)} TL'dir.",
  "Maliyet muhasebesi - toplam direkt malzeme sapmasının uzlaştırılması")

q("Direkt malzeme sapmalarına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Fiyat farkı fiilî miktarla değerlenebilir\n\nII. Kullanım farkı standart fiyatla değerlenebilir\n\nIII. Fiilî üretim değişse de standart miktar sabit bütçe miktarı olarak bırakılır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Fiyat ve kullanım etkileri ortak miktar/fiyat tabanlarıyla ayrılır. Standart miktar fiilî çıktı için izin verilen miktara uyarlanır.",
  "TMS 2 par. 21; maliyet muhasebesi - malzeme fiyat ve kullanım sapmaları")

purchased_qty = 7_800
purchase_price_var = (ap-sp)*purchased_qty
used_price_var = (ap-sp)*aq
inventory_qty = purchased_qty-aq
deferred_price_effect = (ap-sp)*inventory_qty
assert (purchase_price_var, used_price_var, inventory_qty, deferred_price_effect) == (15_600, 15_000, 300, 600)
q(f"Fiyat sapması satın alma anında kaydediliyor. {tr(purchased_qty)} kg malzeme {tr(ap)} TL'den alınmış, standart fiyat {tr(sp)} TL'dir. Satın alma fiyat sapması nedir?",
  f"{tr(purchase_price_var)} TL aleyhte",
  [f"{tr(used_price_var)} TL aleyhte; satın alınan yerine kullanılan miktar esas alınır",
   f"{tr(purchase_price_var)} TL lehte; yüksek alış fiyatı olumlu kabul edilir",
   f"{tr(deferred_price_effect)} TL aleyhte; yalnız dönem sonu miktarı sapma sayılır",
   f"{tr(purchased_qty*ap)} TL aleyhte; alış maliyetinin tamamı fiyat sapması kabul edilir"],
  f"Satın alma anındaki sapma ({tr(ap)} − {tr(sp)}) × {tr(purchased_qty)} = {tr(purchase_price_var)} TL aleyhtedir.",
  "1 Sıra No.lu MSUGT - 712 Direkt İlk Madde ve Malzeme Fiyat Farkı")

q(f"Satın alma fiyat sapması {tr(purchase_price_var)} TL aleyhte, kullanılan miktara ilişkin fiyat etkisi {tr(used_price_var)} TL aleyhtedir. Stokta kalan {tr(inventory_qty)} kg'a ait fiyat etkisi kaç TL'dir?",
  f"{tr(deferred_price_effect)} TL aleyhte",
  [f"{tr(purchase_price_var)} TL aleyhte; toplam satın alma sapmasının tamamı stokta bırakılır",
   f"{tr(used_price_var)} TL aleyhte; üretimde kullanılan miktarın etkisi stokta kabul edilir",
   f"{tr(inventory_qty*ap)} TL aleyhte; stokun fiilî maliyetinin tamamı fiyat etkisi sayılır",
   f"{tr(deferred_price_effect)} TL lehte; yüksek alış fiyatının stok etkisi olumlu kabul edilir"],
  f"Stok fiyat etkisi {tr(inventory_qty)} × ({tr(ap)} − {tr(sp)}) = {tr(deferred_price_effect)} TL aleyhtedir; iki fiyat sapması arasındaki farkla da aynıdır.",
  "1 Sıra No.lu MSUGT - standart fiyatla stok izleme ve fiyat farkı", "hard")

std_a_share, std_b_share, total_actual_mix = 0.60, 0.40, 10_000
rsq_a, rsq_b = total_actual_mix*std_a_share, total_actual_mix*std_b_share
aq_a, aq_b, sp_a, sp_b = 6_500, 3_500, 20, 30
mix_a = (aq_a-rsq_a)*sp_a
mix_b = (aq_b-rsq_b)*sp_b
mix_var = mix_a+mix_b
assert (rsq_a, rsq_b, mix_a, mix_b, mix_var) == (6_000, 4_000, 10_000, -15_000, -5_000)
q(f"Standart karışım A için %60, B için %40'tır. Toplam fiilî girdi {tr(total_actual_mix)} kg; fiilî A {tr(aq_a)}, B {tr(aq_b)} kg'dır. Standart fiyatlar A {tr(sp_a)}, B {tr(sp_b)} TL ise malzeme karma sapması nedir?",
  f"{tr(abs(mix_var))} TL lehte",
  [f"{tr(abs(mix_var))} TL aleyhte; ucuz A'nın payının artması olumsuz kabul edilir",
   f"{tr(mix_a)} TL aleyhte; yalnız A malzemesinin karma etkisi toplam sayılır",
   f"{tr(abs(mix_b))} TL lehte; yalnız B malzemesinin karma etkisi toplam sayılır",
   f"{tr(aq_a*sp_a+aq_b*sp_b)} TL aleyhte; standart fiyatlı fiilî karışımın tamamı sapma sayılır"],
  f"Revize standart miktarlar A {tr(rsq_a)}, B {tr(rsq_b)} kg'dır. Karma etkileri {tr(mix_a)} TL aleyhte ve {tr(abs(mix_b))} TL lehte; net {tr(abs(mix_var))} TL lehtedir.",
  "Maliyet muhasebesi - direkt malzeme karma sapması", "hard")

sq_total_yield = 9_600
std_weighted_price = std_a_share*sp_a+std_b_share*sp_b
yield_var = (total_actual_mix-sq_total_yield)*std_weighted_price
usage_total_mix = (aq_a*sp_a+aq_b*sp_b)-sq_total_yield*std_weighted_price
assert (std_weighted_price, yield_var, usage_total_mix, mix_var+yield_var) == (24, 9_600, 4_600, 4_600)
q(f"Fiilî toplam girdi {tr(total_actual_mix)} kg, fiilî çıktı için standart toplam girdi {tr(sq_total_yield)} kg ve standart karışımın ağırlıklı fiyatı {tr(std_weighted_price)} TL/kg'dır. Malzeme verim sapması nedir?",
  f"{tr(yield_var)} TL aleyhte",
  [f"{tr(yield_var)} TL lehte; standarttan fazla toplam girdi olumlu kabul edilir",
   f"{tr(abs(mix_var))} TL lehte; karma etkisi verim sapması olarak raporlanır",
   f"{tr(usage_total_mix)} TL aleyhte; net kullanım sapması yalnız verim sayılır",
   f"{tr(total_actual_mix*std_weighted_price)} TL aleyhte; bütün fiilî girdinin maliyeti sapma kabul edilir"],
  f"Verim sapması ({tr(total_actual_mix)} − {tr(sq_total_yield)}) × {tr(std_weighted_price)} = {tr(yield_var)} TL aleyhtedir.",
  "Maliyet muhasebesi - direkt malzeme verim sapması", "hard")

q(f"Malzeme karma sapması {tr(abs(mix_var))} TL lehte, verim sapması {tr(yield_var)} TL aleyhtedir. Net kullanım sapması nedir?",
  f"{tr(usage_total_mix)} TL aleyhte",
  [f"{tr(abs(mix_var)+yield_var)} TL aleyhte; lehte sapma da aleyhte gibi toplanır",
   f"{tr(abs(mix_var))} TL lehte; verim etkisi net sonuçtan tamamen çıkarılır",
   f"{tr(yield_var)} TL aleyhte; karma etkisi net sonuçta dikkate alınmaz",
   f"{tr(abs(yield_var-abs(mix_var)))} TL lehte; büyük sapmanın yönü ters çevrilir"],
  f"Lehte sapma negatif, aleyhte sapma pozitif alınır: −{tr(abs(mix_var))} + {tr(yield_var)} = {tr(usage_total_mix)} TL aleyhte.",
  "Maliyet muhasebesi - karma ve verim sapmalarının kullanım sapmasına uzlaştırılması", "hard")

ap_a, ap_b = 21, 28
price_a = (ap_a-sp_a)*aq_a
price_b = (ap_b-sp_b)*aq_b
total_price_mix = price_a+price_b
actual_mix_cost = aq_a*ap_a+aq_b*ap_b
std_allowed_mix_cost = sq_total_yield*std_weighted_price
grand_mix_var = actual_mix_cost-std_allowed_mix_cost
assert (price_a, price_b, total_price_mix, actual_mix_cost, std_allowed_mix_cost, grand_mix_var) == (6_500, -7_000, -500, 234_500, 230_400, 4_100)
q(f"A'nın fiilî fiyatı {tr(ap_a)}, standardı {tr(sp_a)} TL; B'nin fiilî fiyatı {tr(ap_b)}, standardı {tr(sp_b)} TL'dir. Fiilî miktarlar A {tr(aq_a)}, B {tr(aq_b)} kg ise toplam fiyat sapması nedir?",
  f"{tr(abs(total_price_mix))} TL lehte",
  [f"{tr(abs(total_price_mix))} TL aleyhte; B'deki ucuz alım olumsuz kabul edilir",
   f"{tr(price_a)} TL aleyhte; yalnız A fiyat etkisi toplam sayılır",
   f"{tr(abs(price_b))} TL lehte; yalnız B fiyat etkisi toplam sayılır",
   f"{tr(actual_mix_cost)} TL aleyhte; fiilî karışım maliyetinin tamamı sapma kabul edilir"],
  f"A fiyat etkisi {tr(price_a)} TL aleyhte, B fiyat etkisi {tr(abs(price_b))} TL lehtedir. Net sonuç {tr(abs(total_price_mix))} TL lehtedir.",
  "Maliyet muhasebesi - çoklu malzeme fiyat sapması", "hard")

q(f"Toplam fiyat sapması {tr(abs(total_price_mix))} TL lehte ve toplam kullanım sapması {tr(usage_total_mix)} TL aleyhtedir. Fiilî maliyet ile standart maliyet arasındaki net fark nedir?",
  f"{tr(grand_mix_var)} TL aleyhte",
  [f"{tr(abs(total_price_mix)+usage_total_mix)} TL aleyhte; lehte fiyat etkisi de aleyhte toplanır",
   f"{tr(abs(total_price_mix))} TL lehte; kullanım etkisi toplamdan çıkarılır",
   f"{tr(usage_total_mix)} TL aleyhte; fiyat etkisi uzlaştırmada dikkate alınmaz",
   f"{tr(grand_mix_var)} TL lehte; net farkın yönü ters raporlanır"],
  f"Net sapma −{tr(abs(total_price_mix))} + {tr(usage_total_mix)} = {tr(grand_mix_var)} TL aleyhtedir. Ayrıca {tr(actual_mix_cost)} − {tr(std_allowed_mix_cost)} = {tr(grand_mix_var)} TL'dir.",
  "Maliyet muhasebesi - fiyat, karma ve verim sapmalarının toplam maliyetle uzlaştırılması", "hard")

q("Malzeme fiyat sapması lehteyken kullanım sapması aleyhteyse performans değerlendirmesinde hangi yaklaşım doğrudur?",
  "Malzeme kalitesi ve satın alma kararını birlikte incelemek",
  ["Lehte fiyat görüldüğü için kullanım verimsizliğini hiçbir araştırma yapmadan yok saymak",
   "Aleyhte kullanım görüldüğü için satın alma bölümünü tek başına kesin sorumlu ilan etmek",
   "İki sapmayı birbirinden bağımsız sayıp ortak kalite veya tedarik nedenini araştırmamak",
   "Net sapma küçükse fiziksel malzeme kayıtlarını ve standartları tamamen kaldırmak"],
  "Ucuz malzeme düşük kalite nedeniyle fazla tüketim yaratmış olabilir; nedenler bölümler arası ilişkiyle incelenmelidir.",
  "Maliyet muhasebesi - malzeme sapmalarında kök neden ve sorumluluk")

q("Malzeme sapmalarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Karma sapması toplam girdinin standart oranlardan sapmasını ölçer\n\nII. Verim sapması toplam girdi ile izin verilen toplam girdiyi karşılaştırır\n\nIII. Karma ve verim ayrımı yalnız tek malzemeli üretimde zorunludur",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Karma ayrımı birden çok girdinin oran değişimini, verim ise toplam girdi–çıktı ilişkisini ölçer. Tek malzemede karma sapması oluşmaz.",
  "Maliyet muhasebesi - malzeme karma ve verim sapmaları")

q("Normal fire oranı düşürüldüğü hâlde birim başına standart brüt girdi güncellenmemişse kullanım sapması nasıl etkilenebilir?",
  "Gerçek verimsizlik olduğundan küçük görünebilir",
  ["Standart miktar eski yüksek kaybı içerdiği için her zaman olduğundan büyük aleyhte çıkar",
   "Fiyat sapmasına dönüşerek fiziksel kullanım farkını tamamen ortadan kaldırır",
   "Fiilî miktardan bağımsız olarak mutlaka sıfır olur ve hiçbir sinyal üretmez",
   "Satış hacmini artırarak kullanım sapmasını otomatik olarak lehteye çevirir"],
  "Eski standart daha fazla girdiye izin verirse fiilî fazla kullanımın bir kısmı normal görünür; standart teknik iyileşmeyle güncellenmelidir.",
  "TMS 2 par. 21 - normal malzeme düzeyleri ve standartların güncellenmesi", "hard")


# ── C. Direkt işçilik ücret, verimlilik, boş zaman ve karma (15) ──────────
labor_output, sh_per_unit, sr = 1_200, 2.5, 240
sh = labor_output*sh_per_unit
std_labor_cost = sh*sr
assert (sh, std_labor_cost) == (3_000, 720_000)
q(f"Fiilî üretim {tr(labor_output)} birim, birim başına standart süre {tr(sh_per_unit)} saat ve standart ücret {tr(sr)} TL/saattir. Fiilî üretim için standart direkt işçilik saati kaçtır?",
  f"{tr(sh)} saat",
  [f"{tr(labor_output)} saat çıktı adedinin standart süre kabul edildiği sonuç",
   f"{tr(sh_per_unit)} saat yalnız bir mamul süresinin dönem toplamı sayıldığı miktar",
   f"{tr(labor_output+sh_per_unit)} saat çıktı ve birim sürenin toplanmasıyla bulunan sonuç",
   f"{tr(std_labor_cost)} saat parasal standart maliyetin fiziksel süre kabul edildiği sonuç"],
  f"Fiilî üretime izin verilen süre {tr(labor_output)} × {tr(sh_per_unit)} = {tr(sh)} saattir.",
  "TMS 2 par. 21 - normal işçilik ve verimlilik düzeyleri; standart saat")

ah, ar = 3_150, 260
actual_labor_cost = ah*ar
rate_var = (ar-sr)*ah
eff_var = (ah-sh)*sr
total_labor_var = actual_labor_cost-std_labor_cost
assert (actual_labor_cost, rate_var, eff_var, total_labor_var) == (819_000, 63_000, 36_000, 99_000)
q(f"Fiilî çalışma {tr(ah)} saat, fiilî ücret {tr(ar)} TL ve standart ücret {tr(sr)} TL/saattir. Direkt işçilik ücret sapması nedir?",
  f"{tr(rate_var)} TL aleyhte",
  [f"{tr(eff_var)} TL aleyhte; süre farkı ücret sapması sayılır",
   f"{tr(rate_var)} TL lehte; standarttan yüksek ücret olumlu kabul edilir",
   f"{tr((ar-sr)*sh)} TL aleyhte; ücret farkı fiilî yerine standart saatle çarpılır",
   f"{tr(actual_labor_cost)} TL aleyhte; fiilî işçilik maliyetinin tamamı sapma sayılır"],
  f"Ücret sapması ({tr(ar)} − {tr(sr)}) × {tr(ah)} = {tr(rate_var)} TL aleyhtedir.",
  "1 Sıra No.lu MSUGT - 722 Direkt İşçilik Ücret Farkı")

q(f"Fiilî çalışma {tr(ah)} saat, fiilî üretim için standart süre {tr(sh)} saat ve standart ücret {tr(sr)} TL/saattir. Verimlilik sapması nedir?",
  f"{tr(eff_var)} TL aleyhte",
  [f"{tr(rate_var)} TL aleyhte; ücret farkı verimlilik sapması sayılır",
   f"{tr(eff_var)} TL lehte; standarttan fazla süre olumlu kabul edilir",
   f"{tr((ah-sh)*ar)} TL aleyhte; süre farkı fiilî ücretle değerlenir",
   f"{tr(actual_labor_cost)} TL aleyhte; fiilî işçilik maliyetinin tamamı sapma sayılır"],
  f"Verimlilik sapması ({tr(ah)} − {tr(sh)}) × {tr(sr)} = {tr(eff_var)} TL aleyhtedir.",
  "1 Sıra No.lu MSUGT - 723 Direkt İşçilik Süre Farkı")

q(f"Fiilî direkt işçilik maliyeti {tr(actual_labor_cost)} TL, fiilî üretimin standart işçilik maliyeti {tr(std_labor_cost)} TL'dir. Toplam işçilik sapması nedir?",
  f"{tr(total_labor_var)} TL aleyhte",
  [f"{tr(total_labor_var)} TL lehte; yüksek fiilî maliyet olumlu kabul edilir",
   f"{tr(rate_var)} TL aleyhte; yalnız ücret bileşeni toplam sapma sayılır",
   f"{tr(eff_var)} TL aleyhte; yalnız verimlilik bileşeni toplam sapma sayılır",
   f"{tr(actual_labor_cost+std_labor_cost)} TL aleyhte; fiilî ve standart tutarlar toplanır"],
  f"Toplam sapma {tr(actual_labor_cost)} − {tr(std_labor_cost)} = {tr(total_labor_var)} TL aleyhtedir; {tr(rate_var)} + {tr(eff_var)} ile uzlaşır.",
  "Maliyet muhasebesi - toplam direkt işçilik sapmasının uzlaştırılması")

q("Direkt işçilik sapmalarına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Ücret sapması fiilî saat üzerinden hesaplanabilir\n\nII. Verimlilik sapması standart ücretle değerlenebilir\n\nIII. Standart saat fiilî üretim miktarından bağımsız sabit bırakılır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Ücret ve süre etkileri ayrı ortak tabanlarla ölçülür; standart saat fiilî çıktı için izin verilen süreye uyarlanır.",
  "TMS 2 par. 21; 1 Sıra No.lu MSUGT - 722 ve 723 işçilik farkları")

idle_hours = 120
productive_hours = ah-idle_hours
idle_var = idle_hours*sr
productive_eff_var = (productive_hours-sh)*sr
assert (productive_hours, idle_var, productive_eff_var, idle_var+productive_eff_var) == (3_030, 28_800, 7_200, eff_var)
q(f"Toplam fiilî {tr(ah)} saatin {tr(idle_hours)} saati makine arızası nedeniyle boş geçmiştir. Standart ücret {tr(sr)} TL ise boş zaman sapması kaç TL'dir?",
  f"{tr(idle_var)} TL aleyhte",
  [f"{tr(productive_eff_var)} TL aleyhte; yalnız üretken saat fazlası boş zaman sayılır",
   f"{tr(idle_var)} TL lehte; üretim yapılmayan süre olumlu kabul edilir",
   f"{tr(idle_hours*ar)} TL aleyhte; boş zaman yalnız fiilî ücretle değerlenir",
   f"{tr(ah*sr)} TL aleyhte; bütün fiilî saatler boş zaman kabul edilir"],
  f"Boş zaman sapması {tr(idle_hours)} × {tr(sr)} = {tr(idle_var)} TL aleyhtedir.",
  "Maliyet muhasebesi - direkt işçilik boş zaman sapması", "hard")

q(f"Boş zaman çıkarıldıktan sonra üretken süre {tr(productive_hours)} saat, standart süre {tr(sh)} saat ve standart ücret {tr(sr)} TL'dir. Üretken süre verimlilik sapması nedir?",
  f"{tr(productive_eff_var)} TL aleyhte",
  [f"{tr(eff_var)} TL aleyhte; boş zaman ayrıştırılmadan toplam süre farkı kullanılır",
   f"{tr(idle_var)} TL aleyhte; boş zaman tutarı üretken verimlilik sayılır",
   f"{tr(productive_eff_var)} TL lehte; standarttan fazla üretken süre olumlu kabul edilir",
   f"{tr((productive_hours-sh)*ar)} TL aleyhte; süre farkı fiilî ücretle değerlenir"],
  f"Üretken süre sapması ({tr(productive_hours)} − {tr(sh)}) × {tr(sr)} = {tr(productive_eff_var)} TL aleyhtedir.",
  "Maliyet muhasebesi - boş zaman sonrası işçilik verimlilik sapması", "hard")

q(f"Toplam süre sapması {tr(eff_var)} TL aleyhte; bunun {tr(idle_var)} TL'si boş zaman, {tr(productive_eff_var)} TL'si üretken verimsizliktir. Bu ayrımın temel yararı nedir?",
  "Arıza ile çalışma hızının etkisini ayırmak",
  ["Ücret sapmasını süre sapmasına ekleyerek toplam farkı iki kez büyütmek",
   "Boş zamanın üretimle ilgisini kesip bütün fiilî saat kayıtlarını iptal etmek",
   "Standart süreyi müşterilerin ödeme vadesine göre yeniden hesaplamak",
   "Makine arızası ile işçi çalışma hızını aynı nedene bağlayıp sorumluluğu gizlemek"],
  "Boş zaman çoğu kez bakım, planlama veya malzeme bekleme; üretken verimsizlik ise yöntem, eğitim veya kalite nedenlerini gösterir.",
  "Maliyet muhasebesi - işçilik süre sapmasının nedenlerine ayrılması")

skill_share, unskill_share, total_labor_hours = 0.40, 0.60, 2_000
rsh_skill, rsh_unskill = total_labor_hours*skill_share, total_labor_hours*unskill_share
ah_skill, ah_unskill, sr_skill, sr_unskill = 900, 1_100, 300, 180
labor_mix_var = (ah_skill-rsh_skill)*sr_skill+(ah_unskill-rsh_unskill)*sr_unskill
assert (rsh_skill, rsh_unskill, labor_mix_var) == (800, 1_200, 12_000)
q(f"Standart işçilik karması uzman %40, yardımcı %60'tır. Fiilî toplam {tr(total_labor_hours)} saatin {tr(ah_skill)} saati uzman, {tr(ah_unskill)} saati yardımcıdır. Standart ücretler {tr(sr_skill)} ve {tr(sr_unskill)} TL ise karma sapması nedir?",
  f"{tr(labor_mix_var)} TL aleyhte",
  [f"{tr(labor_mix_var)} TL lehte; pahalı uzman payının artması olumlu kabul edilir",
   f"{tr((ah_skill-rsh_skill)*sr_skill)} TL aleyhte; yalnız uzman etkisi toplam sayılır",
   f"{tr(abs((ah_unskill-rsh_unskill)*sr_unskill))} TL lehte; yalnız yardımcı etkisi toplam sayılır",
   f"{tr(ah_skill*sr_skill+ah_unskill*sr_unskill)} TL aleyhte; standart ücretli fiilî karmanın tamamı sapma sayılır"],
  f"Revize standart saatler uzman {tr(rsh_skill)}, yardımcı {tr(rsh_unskill)}'dır. Etkiler {tr((ah_skill-rsh_skill)*sr_skill)} TL aleyhte ve {tr(abs((ah_unskill-rsh_unskill)*sr_unskill))} TL lehte; net {tr(labor_mix_var)} TL aleyhtedir.",
  "Maliyet muhasebesi - direkt işçilik karma sapması", "hard")

allowed_total_hours = 1_950
std_avg_labor_rate = skill_share*sr_skill+unskill_share*sr_unskill
labor_yield_var = (total_labor_hours-allowed_total_hours)*std_avg_labor_rate
labor_usage_var = labor_mix_var+labor_yield_var
assert (std_avg_labor_rate, labor_yield_var, labor_usage_var) == (228, 11_400, 23_400)
q(f"Fiilî toplam işçilik {tr(total_labor_hours)} saat, fiilî çıktı için izin verilen süre {tr(allowed_total_hours)} saat ve standart karmanın ağırlıklı ücreti {tr(std_avg_labor_rate)} TL/saattir. İşçilik verim sapması nedir?",
  f"{tr(labor_yield_var)} TL aleyhte",
  [f"{tr(labor_yield_var)} TL lehte; standarttan fazla toplam süre olumlu kabul edilir",
   f"{tr(labor_mix_var)} TL aleyhte; karma etkisi verim sapması olarak raporlanır",
   f"{tr(labor_usage_var)} TL aleyhte; karma ile verim toplamı yalnız verim sayılır",
   f"{tr(total_labor_hours*std_avg_labor_rate)} TL aleyhte; bütün fiilî süre sapma kabul edilir"],
  f"Verim sapması ({tr(total_labor_hours)} − {tr(allowed_total_hours)}) × {tr(std_avg_labor_rate)} = {tr(labor_yield_var)} TL aleyhtedir.",
  "Maliyet muhasebesi - direkt işçilik verim/yield sapması", "hard")

q(f"İşçilik karma sapması {tr(labor_mix_var)} TL, verim sapması {tr(labor_yield_var)} TL aleyhtedir. Toplam kullanım etkisi nedir?",
  f"{tr(labor_usage_var)} TL aleyhte",
  [f"{tr(abs(labor_mix_var-labor_yield_var))} TL aleyhte; iki aleyhte sapma birbirinden çıkarılır",
   f"{tr(labor_mix_var)} TL aleyhte; verim etkisi toplamdan dışlanır",
   f"{tr(labor_yield_var)} TL aleyhte; karma etkisi toplamdan dışlanır",
   f"{tr(labor_usage_var)} TL lehte; iki aleyhte etkinin yönü ters çevrilir"],
  f"Her iki sapma aleyhte olduğundan {tr(labor_mix_var)} + {tr(labor_yield_var)} = {tr(labor_usage_var)} TL aleyhtedir.",
  "Maliyet muhasebesi - işçilik karma ve verim sapmalarının uzlaştırılması")

q("İşçilik sapmalarına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Boş zaman toplam süre sapmasının bir nedeni olarak ayrıştırılabilir\n\nII. İşçilik karması farklı ücret gruplarının oran değişimini ölçebilir\n\nIII. Ücret sapması yalnız üretim miktarı değiştiği için ortaya çıkar",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Boş zaman ve karma ayrımları neden analizini güçlendirir. Ücret sapması fiilî ve standart saat ücretinin farkından doğar.",
  "Maliyet muhasebesi - işçilik ücret, süre, boş zaman ve karma sapmaları")

q("Daha deneyimli işçi kullanımının ücret sapmasını aleyhte, verimlilik sapmasını lehte yapması hâlinde nasıl değerlendirme yapılmalıdır?",
  "Net maliyet ve kalite etkisi birlikte incelenmelidir",
  ["Ücret sapması aleyhte olduğu için deneyimli işçi kullanımı hiçbir analiz yapılmadan sonlandırılmalıdır",
   "Verimlilik sapması lehte olduğu için yüksek ücretin toplam maliyete etkisi tamamen yok sayılmalıdır",
   "İki sapmanın aynı iş gücü kararıyla ilişkisi bulunmadığı varsayılarak ayrı dönemlere aktarılmalıdır",
   "Standart saat ve ücret kayıtları kaldırılarak yalnız satış fiyatı performansı ölçülmelidir"],
  "Yüksek ücret daha hızlı çalışma, daha az hata veya düşük yeniden işleme sağlayabilir; toplam maliyet ve kalite sonucu ortak değerlendirilir.",
  "Maliyet muhasebesi - işçilik ücret ve verimlilik sapmalarının etkileşimi")

q("Yeni öğrenme etkisiyle üretim süresi kalıcı olarak azalmışsa standart süre için hangi işlem uygundur?",
  "Teknik doğrulama sonrası standardı güncellemek",
  ["Eski yüksek süreyi sonsuza kadar koruyup bütün gelecek lehte sapmaları performans saymak",
   "Fiilî süre azaldığı için standart ücret tutarını aynı oranda otomatik yükseltmek",
   "Geçmiş dönem fiilî saatlerini yeni standarda göre geriye dönük olarak silmek",
   "Üretim süresini artık ölçmeyip yalnız müşterilerin ödeme vadelerini izlemek"],
  "Kalıcı yöntem veya öğrenme iyileşmesi doğrulandıysa standart, güncel ulaşılabilir performansı yansıtacak şekilde ileriye dönük değiştirilmelidir.",
  "TMS 2 par. 21 - standart işçilik ve verimlilik düzeylerinin düzenli gözden geçirilmesi")

q("Üretim planlama hatası nedeniyle nitelikli işçi düşük beceri gerektiren işte çalıştırılmışsa ücret sapması sorumluluğu neden yalnız insan kaynaklarına verilemez?",
  "İş gücü atama kararı üretim planlamasından kaynaklanmıştır",
  ["Saat ücretlerinin hiçbir bölüm tarafından kontrol edilemeyen satış geliri olması nedeniyle",
   "Nitelikli işçinin fiilî çalışma süresinin muhasebede kaydedilememesi nedeniyle",
   "Ücret sapmasının yalnız malzeme kullanım miktarından hesaplanması nedeniyle",
   "Üretim planlamasının standart maliyet ve sapmalarla hiçbir ilgisi bulunmaması nedeniyle"],
  "Fiilî ücret karması işe atama kararından etkilenmiştir; kontrol edilebilir neden planlama merkezinde olabilir.",
  "Maliyet muhasebesi - işçilik sapmalarında sorumluluk ve kontrol edilebilirlik", "hard")

# ── D. Değişken/sabit GÜG sapmaları, kapasite ve kapanış (15) ─────────────
svor, actual_voh = 60, 201_600
voh_flex = ah*svor
voh_applied = sh*svor
voh_spending = actual_voh-voh_flex
voh_eff = (ah-sh)*svor
voh_total = actual_voh-voh_applied
assert (voh_flex, voh_applied, voh_spending, voh_eff, voh_total) == (189_000, 180_000, 12_600, 9_000, 21_600)
q(f"Değişken GÜG standart oranı {tr(svor)} TL/saat, fiilî süre {tr(ah)} saat ve fiilî değişken GÜG {tr(actual_voh)} TL'dir. Harcama sapması nedir?",
  f"{tr(voh_spending)} TL aleyhte",
  [f"{tr(voh_eff)} TL aleyhte; süre etkisi harcama sapması sayılır",
   f"{tr(voh_spending)} TL lehte; esnek bütçeyi aşan gider olumlu kabul edilir",
   f"{tr(voh_total)} TL aleyhte; harcama ve verimlilik birlikte yalnız harcama sayılır",
   f"{tr(actual_voh)} TL aleyhte; fiilî değişken giderin tamamı sapma kabul edilir"],
  f"Fiilî saatlerin esnek bütçesi {tr(ah)} × {tr(svor)} = {tr(voh_flex)} TL'dir. Harcama sapması {tr(actual_voh)} − {tr(voh_flex)} = {tr(voh_spending)} TL aleyhtedir.",
  "1 Sıra No.lu MSUGT - 732 GÜG Bütçe Farkı; değişken GÜG harcama sapması")

q(f"Değişken GÜG standart oranı {tr(svor)} TL/saat, fiilî süre {tr(ah)} ve standart süre {tr(sh)} saattir. Verimlilik sapması nedir?",
  f"{tr(voh_eff)} TL aleyhte",
  [f"{tr(voh_spending)} TL aleyhte; gider fiyat etkisi verimlilik sayılır",
   f"{tr(voh_eff)} TL lehte; standarttan fazla süre olumlu kabul edilir",
   f"{tr((ah-sh)*actual_voh/ah)} TL aleyhte; süre farkı fiilî gider oranıyla değerlenir",
   f"{tr(actual_voh)} TL aleyhte; fiilî değişken giderin tamamı sapma kabul edilir"],
  f"Verimlilik sapması ({tr(ah)} − {tr(sh)}) × {tr(svor)} = {tr(voh_eff)} TL aleyhtedir.",
  "1 Sıra No.lu MSUGT - 733 GÜG Verimlilik Farkı")

q(f"Fiilî değişken GÜG {tr(actual_voh)} TL, üretime standart olarak yüklenen değişken GÜG {tr(voh_applied)} TL'dir. Toplam değişken GÜG sapması nedir?",
  f"{tr(voh_total)} TL aleyhte",
  [f"{tr(voh_total)} TL lehte; fiilî giderin yüklenenden yüksek olması olumlu kabul edilir",
   f"{tr(voh_spending)} TL aleyhte; yalnız harcama bileşeni toplam sayılır",
   f"{tr(voh_eff)} TL aleyhte; yalnız verimlilik bileşeni toplam sayılır",
   f"{tr(actual_voh+voh_applied)} TL aleyhte; fiilî ve yüklenen giderler toplanır"],
  f"Toplam sapma {tr(actual_voh)} − {tr(voh_applied)} = {tr(voh_total)} TL aleyhtedir; {tr(voh_spending)} + {tr(voh_eff)} ile uzlaşır.",
  "Maliyet muhasebesi - değişken GÜG toplam sapmasının uzlaştırılması")

budget_foh, actual_foh, denom_hours = 480_000, 495_000, 4_000
foh_rate = budget_foh/denom_hours
foh_applied = sh*foh_rate
foh_budget_var = actual_foh-budget_foh
foh_volume_var = budget_foh-foh_applied
foh_total_var = actual_foh-foh_applied
assert (foh_rate, foh_applied, foh_budget_var, foh_volume_var, foh_total_var) == (120, 360_000, 15_000, 120_000, 135_000)
q(f"Bütçelenen sabit GÜG {tr(budget_foh)} TL, fiilî sabit GÜG {tr(actual_foh)} TL'dir. Sabit GÜG bütçe sapması nedir?",
  f"{tr(foh_budget_var)} TL aleyhte",
  [f"{tr(foh_volume_var)} TL aleyhte; kapasite etkisi bütçe sapması sayılır",
   f"{tr(foh_budget_var)} TL lehte; bütçeyi aşan sabit gider olumlu kabul edilir",
   f"{tr(foh_total_var)} TL aleyhte; bütçe ve hacim farkı yalnız bütçe sayılır",
   f"{tr(actual_foh)} TL aleyhte; fiilî sabit giderin tamamı sapma kabul edilir"],
  f"Bütçe sapması {tr(actual_foh)} − {tr(budget_foh)} = {tr(foh_budget_var)} TL aleyhtedir.",
  "1 Sıra No.lu MSUGT - 732 GÜG Bütçe Farkı; sabit GÜG bütçe sapması")

q(f"Sabit GÜG bütçesi {tr(budget_foh)} TL ve normal kapasite paydası {tr(denom_hours)} saattir. Standart sabit GÜG oranı kaç TL/saattir?",
  f"{tr(foh_rate)} TL/saat",
  [f"{tr(actual_foh/denom_hours)} TL/saat fiilî sabit giderin normal kapasiteye bölündüğü sonuç",
   f"{tr(budget_foh/sh)} TL/saat bütçenin fiilî üretim standart saatine bölündüğü sonuç",
   f"{tr(denom_hours/budget_foh)} TL/saat kapasite ile bütçenin ters bölündüğü sonuç",
   f"{tr(budget_foh+denom_hours)} TL/saat bütçe ile saatlerin toplanmasıyla bulunan sonuç"],
  f"Standart oran {tr(budget_foh)} / {tr(denom_hours)} = {tr(foh_rate)} TL/saattir.",
  "TMS 2 par. 13 - sabit genel üretim giderlerinin normal kapasiteye göre dağıtılması")

q(f"Fiilî üretime izin verilen standart süre {tr(sh)} saat ve sabit GÜG oranı {tr(foh_rate)} TL/saattir. Üretime yüklenen sabit GÜG kaç TL'dir?",
  f"{tr(foh_applied)} TL",
  [f"{tr(budget_foh)} TL bütçenin tamamının düşük faaliyet düzeyine rağmen üretime yüklendiği tutar",
   f"{tr(actual_foh)} TL fiilî sabit giderin tamamının standart yükleme sayıldığı tutar",
   f"{tr(sh)} TL standart saatin parasal yükleme tutarı kabul edildiği sonuç",
   f"{tr(denom_hours*foh_rate)} TL normal kapasite saatlerinin fiilî üretim gibi yüklendiği tutar"],
  f"Üretime yüklenen sabit GÜG {tr(sh)} × {tr(foh_rate)} = {tr(foh_applied)} TL'dir.",
  "TMS 2 par. 13 - normal kapasite oranıyla sabit GÜG yüklenmesi")

q(f"Normal kapasite {tr(denom_hours)} saatken fiilî çıktının standart süresi {tr(sh)} saatte kalmıştır. Sabit GÜG oranı {tr(foh_rate)} TL/saat olduğuna göre kullanılmayan kapasitenin sabit gider etkisi nedir?",
  f"{tr(foh_volume_var)} TL aleyhte",
  [f"{tr(foh_budget_var)} TL aleyhte; fiilî gider ile bütçe farkı hacim sapması sayılır",
   f"{tr(foh_volume_var)} TL lehte; normal kapasitenin altında üretim olumlu kabul edilir",
   f"{tr(foh_total_var)} TL aleyhte; bütçe ve hacim birlikte yalnız hacim sayılır",
   f"{tr(budget_foh+foh_applied)} TL aleyhte; bütçe ile yüklenen gider toplanır"],
  f"Hacim sapması {tr(budget_foh)} − {tr(foh_applied)} = {tr(foh_volume_var)} TL aleyhtedir; kapasite yeterince kullanılamamıştır.",
  "1 Sıra No.lu MSUGT - 734 GÜG Kapasite Farkı; TMS 2 par. 13")

q(f"Fiilî sabit GÜG {tr(actual_foh)} TL, üretime yüklenen sabit GÜG {tr(foh_applied)} TL'dir. Toplam sabit GÜG sapması nedir?",
  f"{tr(foh_total_var)} TL aleyhte",
  [f"{tr(foh_total_var)} TL lehte; fiilî giderin yüklenenden yüksek olması olumlu kabul edilir",
   f"{tr(foh_budget_var)} TL aleyhte; yalnız bütçe farkı toplam sayılır",
   f"{tr(foh_volume_var)} TL aleyhte; yalnız hacim farkı toplam sayılır",
   f"{tr(actual_foh+foh_applied)} TL aleyhte; fiilî ve yüklenen giderler toplanır"],
  f"Toplam sabit GÜG sapması {tr(actual_foh)} − {tr(foh_applied)} = {tr(foh_total_var)} TL aleyhtedir. {tr(foh_budget_var)} + {tr(foh_volume_var)} ile uzlaşır.",
  "Maliyet muhasebesi - sabit GÜG bütçe ve hacim sapmalarının uzlaştırılması")

q("Genel üretim gideri sapmalarına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Değişken GÜG harcama sapması esnek bütçeyle karşılaştırılabilir\n\nII. Sabit GÜG hacim sapması kapasite kullanımını yansıtır\n\nIII. Sabit GÜG bütçesi fiilî saat arttıkça aynı oranda değişir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Değişken gider esnek bütçeye uyarlanır, sabit hacim farkı kapasite etkisidir. İlgili aralıkta toplam sabit gider faaliyetle aynı oranda değişmez.",
  "TMS 2 par. 13 ve 21; maliyet muhasebesi - değişken ve sabit GÜG sapmaları")

q("Üretim düşük olduğu için dağıtılmayan sabit genel üretim giderinin mamul birim maliyetini yükseltmek amacıyla stoklara yüklenmemesi hangi ilkeye dayanır?",
  "Normal kapasite esasına",
  ["Bütün sabit giderlerin üretimden bağımsız olarak finansman geliri sayılması ilkesine",
   "Düşük üretimde stokların her zaman satış fiyatıyla değerlenmesi zorunluluğuna",
   "Fiilî kapasite düştüğünde standart sabit gider oranının sınırsız artırılması ilkesine",
   "Genel üretim giderlerinin hiçbir koşulda stok maliyetine alınmaması kuralına"],
  "TMS 2, düşük üretim nedeniyle birim başına sabit GÜG'ü artırmaz; dağıtılmayan kısım dönemin gideridir.",
  "TMS 2 par. 13 - düşük üretimde dağıtılmayan sabit genel üretim giderleri")

q("Fiilî üretim normal kapasiteyi aştığında sabit genel üretim giderinin birimlere dağıtılan tutarı neden azaltılabilir?",
  "Stokların maliyetin üzerinde ölçülmesini önlemek için",
  ["Toplam sabit gider üretim arttıkça zorunlu olarak aynı oranda sıfıra düştüğü için",
   "Yüksek üretimde bütün sabit giderlerin satış hasılatı sayılması gerektiği için",
   "Standart maliyet tekniği yüksek kapasitede hiçbir biçimde kullanılamadığı için",
   "Fiilî üretim arttığında direkt malzeme ve işçilik maliyetleri ortadan kalktığı için"],
  "TMS 2'ye göre olağandışı yüksek üretimde birim sabit GÜG payı, stokların maliyetin üzerinde değerlenmemesi için azaltılır.",
  "TMS 2 par. 13 - olağandışı yüksek üretimde sabit GÜG dağıtımı")

q("Önemsiz toplam sapmanın dönem sonunda satılan mamul maliyetine kapatılması neyi amaçlar?",
  "Standart maliyeti fiilî sonuca yaklaştırmayı",
  ["Bütün dönem sonu stoklarını hiçbir değerlendirme yapmadan sıfır maliyetli göstermeyi",
   "Sapmanın üretimle ilişkisini kesip satış hasılatını aynı tutarda artırmayı",
   "Fiilî maliyet kayıtlarını geçmiş dönemlerle birlikte kalıcı olarak silmeyi",
   "Standartların güncellenmesine hiçbir zaman gerek kalmamasını sağlamayı"],
  "Önemsiz farkın satış maliyetine kapatılması, dönem sonucunu fiilî maliyet etkisine yaklaştıran pratik bir işlemdir.",
  "1 Sıra No.lu MSUGT - maliyet farklarının dönem sonunda kapatılması")

variance_to_allocate = 60_000
wip_base, fg_base, cogs_base = 100_000, 200_000, 700_000
allocation_base = wip_base+fg_base+cogs_base
wip_share = variance_to_allocate*wip_base/allocation_base
fg_share = variance_to_allocate*fg_base/allocation_base
cogs_share = variance_to_allocate*cogs_base/allocation_base
assert (allocation_base, wip_share, fg_share, cogs_share) == (1_000_000, 6_000, 12_000, 42_000)
q(f"{tr(variance_to_allocate)} TL aleyhte sapma; yarı mamul, mamul ve satılan mamul maliyetindeki standart maliyetler sırasıyla {tr(wip_base)}, {tr(fg_base)} ve {tr(cogs_base)} TL'dir. Oransal dağıtımda satılan mamul maliyetinin payı kaç TL'dir?",
  f"{tr(cogs_share)} TL",
  [f"{tr(variance_to_allocate/3)} TL sapmanın üç hesaba bakiye büyüklüğünden bağımsız eşit dağıtıldığı tutar",
   f"{tr(wip_share)} TL yarı mamul oranının satılan mamul maliyetine uygulandığı tutar",
   f"{tr(fg_share)} TL mamul stoku oranının satılan mamul maliyetine uygulandığı tutar",
   f"{tr(variance_to_allocate*cogs_base/(wip_base+fg_base))} TL paydanın satış maliyetini dışladığı tutar"],
  f"Toplam baz {tr(allocation_base)} TL'dir. Satılan mamul payı {tr(variance_to_allocate)} × {tr(cogs_base)} / {tr(allocation_base)} = {tr(cogs_share)} TL olur.",
  "1 Sıra No.lu MSUGT - önemli maliyet farklarının stoklar ve satış maliyetine dağıtılması", "hard")

q("Sapmaların dönem sonu kapatılmasına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Önemsiz fark doğrudan satış maliyetine kapatılabilir\n\nII. Önemli fark ilgili stoklar ve satış maliyetine dağıtılabilir\n\nIII. Dağıtım yöntemi tutarlı ve belgeli olmalıdır",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Önemlilik ve farkın ilgili hesaplarda bulunan üretimle ilişkisi kapanış yöntemini belirler; seçilen yöntem belgeli ve tutarlı uygulanmalıdır.",
  "1 Sıra No.lu MSUGT - maliyet farklarının dönem sonu işlemleri")

all_variances = [total_mat_var, total_labor_var, voh_total, foh_total_var]
integrated_total = sum(all_variances)
std_total = 2_000_000
actual_total = std_total+integrated_total
assert integrated_total == 280_200 and actual_total == 2_280_200
q(f"Malzeme {tr(total_mat_var)}, işçilik {tr(total_labor_var)}, değişken GÜG {tr(voh_total)} ve sabit GÜG {tr(foh_total_var)} TL aleyhte sapma vermiştir. Toplam standart üretim maliyeti {tr(std_total)} TL ise fiilî üretim maliyeti kaç TL'dir?",
  f"{tr(actual_total)} TL",
  [f"{tr(std_total)} TL sapmaların fiilî maliyeti hiç etkilemediği sonuç",
   f"{tr(integrated_total)} TL yalnız sapmalar toplamının fiilî maliyet sayıldığı sonuç",
   f"{tr(std_total-integrated_total)} TL aleyhte sapmaların standart maliyetten düşüldüğü sonuç",
   f"{tr(std_total+integrated_total*2)} TL sapmaların fiilî maliyete iki kez eklendiği sonuç"],
  f"Toplam aleyhte sapma {tr(total_mat_var)} + {tr(total_labor_var)} + {tr(voh_total)} + {tr(foh_total_var)} = {tr(integrated_total)} TL'dir. Fiilî maliyet {tr(std_total)} + {tr(integrated_total)} = {tr(actual_total)} TL olur.",
  "TMS 2 par. 21; maliyet muhasebesi - standart maliyet ile fiilî maliyetin bütünleşik uzlaştırılması", "hard")


# İlk taslaktaki sistematik "doğru şık kısa" kalıbı kaldırılır. Sapma
# sorularında hesap gerekçesi çözüme taşınır; seçenekler tutar ve yönü doğal,
# karşılaştırılabilir biçimde gösterir.
CHOICE_OVERRIDES = {
    1: (
        "Standart maliyetin gerçek maliyete yakın sonuç vermesi",
        ["Standartların hiçbir dönemde değiştirilmemesi",
         "Fiilî maliyet kayıtlarının tamamen kaldırılması",
         "Yalnız ideal performans düzeyinin kullanılması",
         "Standart maliyetin net gerçekleşebilir değere eşit olması"],
    ),
    2: (
        "Standart miktar ve standart fiyat",
        ["Fiilî satış miktarı ve ödeme vadesi", "Bütçelenen kâr ve kredi faizi",
         "Piyasa değeri ve sermaye payı", "Geçmiş toplam maliyet ve satış hacmi"],
    ),
    3: (
        "Normal verimsizliklere tanınan pay",
        ["Satış geliri ile nakit akışı ayrımı", "Standartların belirlenme tarihi",
         "Teknik verilerin kullanılma düzeyi", "Kayıp ve kapasite varsayımlarının eşitliği"],
    ),
    5: (
        "Sapmaların performansı yanlış göstermesi",
        ["Malzeme tüketiminin satış hasılatına dönüşmesi",
         "Üretim miktarının fiziksel olarak sıfırlanması",
         "İşçilik giderinin duran varlığa aktarılması",
         "Müşteri alacaklarının kendiliğinden kapanması"],
    ),
    6: (
        "Olması gereken kaynak tüketimini önceden tanımlamak",
        ["Fiilî maliyet belgelerini tamamen kaldırmak",
         "Satış fiyatıyla müşteri talebini garanti etmek",
         "Bütün sapmaları oluşmadan sıfırlamak",
         "Net gerçekleşebilir değeri maliyete eşitlemek"],
    ),
    7: (
        "Daha kaliteli malzemenin verimi artırmış olmasını",
        ["Fiyat ile verim arasında hiçbir ilişki bulunmamasını",
         "Lehte kullanımın bütün satın alma kararlarını doğrulamasını",
         "Aleyhte fiyatın yalnız satış bölümünden kaynaklanmasını",
         "İki sapmanın farklı dönemlere ait olmasını"],
    ),
    8: (
        "Nedenin merkez tarafından kontrol edilip edilemediği",
        ["Yöneticinin satış hasılatını tahsil edip etmediği",
         "Banka bakiyesinin standart maliyete eşit olup olmadığı",
         "Satış fiyatının işçilik saatine eşit olup olmadığı",
         "Merkezin diğer bölümlerden yüksek bütçesi olup olmadığı"],
    ),
    9: (
        "Faaliyet hacmi etkisini harcama etkisinden ayırması",
        ["Fiilî maliyetleri ölçmeden sapmaları lehte göstermesi",
         "Sabit giderleri tamamen değişken kabul etmesi",
         "Standartları müşteri vadelerine göre değiştirmesi",
         "Her faaliyet düzeyinde fiilî gideri vermesi"],
    ),
    10: (
        "Standardın gevşek veya sürecin kalıcı olarak iyileşmiş olması",
        ["Fiilî kayıtların bütünüyle yanlış olması",
         "Lehte sapmaların anormal kayıp sayılması",
         "Standart maliyet tekniğinin kullanılamaması",
         "Mamul fiyatının standarttan düşük belirlenmesi"],
    ),
    11: (
        "Satın alma koşullarını gerçekçi biçimde yansıtmayı",
        ["Kullanım sapmasını satış hacmiyle hesaplamayı",
         "İşçilik süresini malzeme fiyatından türetmeyi",
         "Fiyat değişimini yalnız üretime yüklemeyi",
         "Fiilî alış belgelerini kaydetmemeyi"],
    ),
    13: (
        "Yakınlık ve sapmalar fiilî verilerle doğrulanır",
        ["Standart maliyet yalnız satış gelirinde kullanılır",
         "Fiilî maliyet her zaman standarda eşit çıkar",
         "Fiilî üretim verilerinin kaydı yasaktır",
         "Standartların gözden geçirilmesi gerekmez"],
    ),
    14: (
        "Birbirini dengeleyen lehte ve aleyhte nedenleri",
        ["Fiilî üretimin standardı her zaman aşmasını",
         "Satış hasılatının standart maliyete eşit olmasını",
         "Ödeme vadelerinin üretim saatlerine eşitliğini",
         "Sabit GÜG'ün hiç sapma üretmemesini"],
    ),
    15: (
        "Dönem performansı o dönemde geçerli hedefle ölçülmüştür",
        ["Geçmiş sapmalar yalnız satış fiyatına aittir",
         "Yeni standart geçmiş fiilî maliyeti değiştirir",
         "Güncelleme bütün muhasebe kayıtlarını iptal eder",
         "Standart değişimi geçmiş hasılatı geri aldırır"],
    ),
    16: ("7.200", ["1.600", "4,50", "1.604,50", "230.400"]),
    17: (
        "15.000 TL aleyhte",
        ["9.600 TL aleyhte", "15.000 TL lehte", "255.000 TL aleyhte", "14.400 TL aleyhte"],
    ),
    18: (
        "9.600 TL aleyhte",
        ["15.000 TL aleyhte", "9.600 TL lehte", "10.200 TL aleyhte", "255.000 TL aleyhte"],
    ),
    19: (
        "24.600 TL aleyhte",
        ["24.600 TL lehte", "15.000 TL aleyhte", "9.600 TL aleyhte", "485.400 TL aleyhte"],
    ),
    21: (
        "15.600 TL aleyhte",
        ["15.000 TL aleyhte", "15.600 TL lehte", "600 TL aleyhte", "265.200 TL aleyhte"],
    ),
    22: (
        "600 TL aleyhte",
        ["15.600 TL aleyhte", "15.000 TL aleyhte", "10.200 TL aleyhte", "600 TL lehte"],
    ),
    23: (
        "5.000 TL lehte",
        ["5.000 TL aleyhte", "10.000 TL aleyhte", "15.000 TL lehte", "235.000 TL aleyhte"],
    ),
    24: (
        "9.600 TL aleyhte",
        ["9.600 TL lehte", "5.000 TL lehte", "4.600 TL aleyhte", "240.000 TL aleyhte"],
    ),
    25: (
        "4.600 TL aleyhte",
        ["14.600 TL aleyhte", "5.000 TL lehte", "9.600 TL aleyhte", "4.600 TL lehte"],
    ),
    26: (
        "500 TL lehte",
        ["500 TL aleyhte", "6.500 TL aleyhte", "7.000 TL lehte", "234.500 TL aleyhte"],
    ),
    27: (
        "4.100 TL aleyhte",
        ["5.100 TL aleyhte", "500 TL lehte", "4.600 TL aleyhte", "4.100 TL lehte"],
    ),
    28: (
        "Malzeme kalitesi ve satın alma kararını birlikte incelemek",
        ["Lehte fiyat nedeniyle kullanım farkını yok saymak",
         "Satın alma bölümünü tek başına sorumlu tutmak",
         "Sapmalar arasında ortak neden aramamak",
         "Net fark küçükse fiziksel kayıtları kaldırmak"],
    ),
    30: (
        "Gerçek verimsizlik olduğundan küçük görünebilir",
        ["Her zaman olduğundan büyük aleyhte görünebilir",
         "Fiyat sapmasına dönüşerek tamamen kaybolabilir",
         "Fiilî miktardan bağımsız olarak sıfır olabilir",
         "Satış hacmi nedeniyle otomatik lehte olabilir"],
    ),
    31: ("3.000", ["1.200", "2,50", "1.202,50", "720.000"]),
    32: (
        "63.000 TL aleyhte",
        ["36.000 TL aleyhte", "63.000 TL lehte", "60.000 TL aleyhte", "819.000 TL aleyhte"],
    ),
    33: (
        "36.000 TL aleyhte",
        ["63.000 TL aleyhte", "36.000 TL lehte", "39.000 TL aleyhte", "819.000 TL aleyhte"],
    ),
    34: (
        "99.000 TL aleyhte",
        ["99.000 TL lehte", "63.000 TL aleyhte", "36.000 TL aleyhte", "1.539.000 TL aleyhte"],
    ),
    36: (
        "28.800 TL aleyhte",
        ["7.200 TL aleyhte", "28.800 TL lehte", "31.200 TL aleyhte", "756.000 TL aleyhte"],
    ),
    37: (
        "7.200 TL aleyhte",
        ["36.000 TL aleyhte", "28.800 TL aleyhte", "7.200 TL lehte", "7.800 TL aleyhte"],
    ),
    38: (
        "Arıza ile çalışma hızının etkisini ayırmak",
        ["Ücret sapmasını süre sapmasına tekrar eklemek",
         "Bütün fiilî saat kayıtlarını iptal etmek",
         "Standart süreyi ödeme vadesine göre belirlemek",
         "Arıza ile çalışma hızını aynı nedene bağlamak"],
    ),
    39: (
        "12.000 TL aleyhte",
        ["12.000 TL lehte", "30.000 TL aleyhte", "18.000 TL lehte", "468.000 TL aleyhte"],
    ),
    40: (
        "11.400 TL aleyhte",
        ["11.400 TL lehte", "12.000 TL aleyhte", "23.400 TL aleyhte", "456.000 TL aleyhte"],
    ),
    41: (
        "23.400 TL aleyhte",
        ["600 TL aleyhte", "12.000 TL aleyhte", "11.400 TL aleyhte", "23.400 TL lehte"],
    ),
    43: (
        "Net maliyet ve kalite etkisi birlikte incelenmelidir",
        ["Yüksek ücret nedeniyle deneyimli işçi bırakılmalıdır",
         "Lehte verim nedeniyle ücret etkisi yok sayılmalıdır",
         "İki sapma farklı dönemlere aktarılmalıdır",
         "Yalnız satış fiyatı performansı ölçülmelidir"],
    ),
    44: (
        "Teknik doğrulama sonrası standardı güncellemek",
        ["Eski süreyi koruyup lehte farkları performans saymak",
         "Standart ücreti süre azalması kadar yükseltmek",
         "Geçmiş fiilî saatleri geriye dönük silmek",
         "Üretim süresini ölçmeyi tamamen bırakmak"],
    ),
    45: (
        "İş gücü atama kararı üretim planlamasından kaynaklanmıştır",
        ["Saat ücretleri satış geliri niteliğindedir",
         "Nitelikli işçinin çalışma süresi kaydedilemez",
         "Ücret sapması malzeme miktarından hesaplanır",
         "Üretim planlaması sapmaları hiç etkilemez"],
    ),
    46: (
        "12.600 TL aleyhte",
        ["9.000 TL aleyhte", "12.600 TL lehte", "21.600 TL aleyhte", "201.600 TL aleyhte"],
    ),
    47: (
        "9.000 TL aleyhte",
        ["12.600 TL aleyhte", "9.000 TL lehte", "9.600 TL aleyhte", "201.600 TL aleyhte"],
    ),
    48: (
        "21.600 TL aleyhte",
        ["21.600 TL lehte", "12.600 TL aleyhte", "9.000 TL aleyhte", "381.600 TL aleyhte"],
    ),
    49: (
        "15.000 TL aleyhte",
        ["120.000 TL aleyhte", "15.000 TL lehte", "135.000 TL aleyhte", "495.000 TL aleyhte"],
    ),
    50: ("120 TL", ["123,75 TL", "160 TL", "0,01 TL", "484.000 TL"]),
    51: ("360.000 TL", ["480.000 TL", "495.000 TL", "3.000 TL", "600.000 TL"]),
    52: (
        "120.000 TL aleyhte",
        ["15.000 TL aleyhte", "120.000 TL lehte", "135.000 TL aleyhte", "840.000 TL aleyhte"],
    ),
    53: (
        "135.000 TL aleyhte",
        ["135.000 TL lehte", "15.000 TL aleyhte", "120.000 TL aleyhte", "855.000 TL aleyhte"],
    ),
    55: (
        "Normal kapasite esasına",
        ["Finansman geliri yaklaşımına", "Satış fiyatıyla değerleme yaklaşımına",
         "Sınırsız oran artırımı yaklaşımına", "Bütün GÜG'ü dışlama yaklaşımına"],
    ),
    56: (
        "Stokların maliyetin üzerinde ölçülmesini önlemek için",
        ["Toplam sabit gider üretimle sıfıra düştüğü için",
         "Sabit giderlerin satış hasılatı sayılması için",
         "Standart maliyet tekniği kullanılamadığı için",
         "Direkt maliyetler yüksek üretimde yok olduğu için"],
    ),
    57: (
        "Standart maliyeti fiilî sonuca yaklaştırmayı",
        ["Dönem sonu stoklarını sıfır maliyetli göstermeyi",
         "Satış hasılatını sapma kadar artırmayı",
         "Fiilî maliyet kayıtlarını kalıcı olarak silmeyi",
         "Standart güncellemesini gereksiz kılmayı"],
    ),
    58: ("42.000 TL", ["20.000 TL", "6.000 TL", "12.000 TL", "140.000 TL"]),
    60: ("2.280.200 TL", ["2.000.000 TL", "280.200 TL", "1.719.800 TL", "2.560.400 TL"]),
}

STEM_OVERRIDES = {
    20: (
        "Direkt malzeme sapmalarına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\n"
        "I. Fiyat farkı fiilî miktarla değerlenebilir\n\n"
        "II. Kullanım farkı standart fiyatla değerlenebilir\n\n"
        "III. Standart miktar fiilî üretim için izin verilen miktara uyarlanır"
    ),
    54: (
        "Genel üretim gideri sapmalarına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\n"
        "I. Değişken GÜG harcama sapması esnek bütçeyle karşılaştırılabilir\n\n"
        "II. Sabit GÜG hacim sapması kapasite kullanımını yansıtır\n\n"
        "III. Sabit GÜG bütçesi ilgili aralıkta fiilî saat arttıkça aynı oranda değişmez"
    ),
}

PREMISE_OVERRIDES = {
    20: (
        "I, II ve III",
        ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
        "Fiyat etkisi fiilî miktar, kullanım etkisi standart fiyat üzerinden ölçülebilir; izin verilen standart miktar fiilî çıktı düzeyine uyarlanır.",
    ),
    54: (
        "I, II ve III",
        ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
        "Değişken GÜG harcama farkı esnek bütçeyle, sabit GÜG hacim farkı kapasiteyle ilişkilidir; toplam sabit bütçe ilgili aralıkta saatle aynı oranda değişmez.",
    ),
}

for number, (correct, distractors) in CHOICE_OVERRIDES.items():
    Q[number - 1]["correct"] = correct
    Q[number - 1]["distractors"] = distractors

for number, stem in STEM_OVERRIDES.items():
    Q[number - 1]["stem"] = stem

for number, (correct, distractors, why) in PREMISE_OVERRIDES.items():
    Q[number - 1]["correct"] = correct
    Q[number - 1]["distractors"] = distractors
    Q[number - 1]["why"] = why


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
