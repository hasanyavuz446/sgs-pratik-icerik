# -*- coding: utf-8 -*-
"""Yeterlilik KONU HAVUZU — Maliyet Muhasebesi / Üretim Kayıpları.

60 özgün soru = 3×20. Fire, artık, bozuk mamul ve kusurlu mamulün normal/anormal
ayrımı; miktar, maliyet ve kayıt etkileri birlikte sınanır. Aritmetik Python'da
hesaplanır. Seçenekler doğal uzunlukta, çözümde cevap harfi yoktur.
"""
import json
import random
import re
from pathlib import Path

L, T, LBL = "maliyet_muhasebesi", "uretim_kayiplari", "Üretim Kayıpları"
PREFIX, SEED = "kh-mal-kayip", 20260905
CONTENT_ROOT = Path(__file__).resolve().parents[3]
PROJECTS_ROOT = CONTENT_ROOT.parent
FILENAME = "questions_topic_uretim_kayiplari_2026.json"
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


# ── A. Kayıp türleri, normal/anormal ayrımı ve TMS 2 (15) ────────────────
q("Üretime giren sıvının teknik olarak kaçınılmaz kısmı buharlaşmış ve geriye satılabilir fiziksel parça kalmamıştır. Bu olay hangi üretim kaybına örnektir?",
  "Fire",
  ["Ek işlemle ekonomik biçimde standart kaliteye getirilebilecek kusurlu mamul oluşumuna",
   "Standart kaliteye getirilemeyen ancak düşük bedelle satılabilen bozuk mamul oluşumuna",
   "Kesim işleminden kalan ve başka üretimde kullanılabilen artık malzeme oluşumuna",
   "Müşterinin kalite şartlarını karşıladığı hâlde ambalajı değiştirilecek sağlam mamule"],
  "Buharlaşma nedeniyle fiziksel miktar kaybolmuş, ayrı bir satış veya kullanım değeri olan çıktı kalmamıştır; bu durum firedir.",
  "TMS 2 par. 16(a) - anormal üretim kayıpları; maliyet muhasebesi - fire tanımı", "easy")

q("Kesimden kalan metal parçaları düşük bedelle satılabiliyor veya başka işte kullanılabiliyorsa bu kalıntılar nasıl sınıflandırılır?",
  "Artık malzeme",
  ["Hiçbir fiziksel kalıntı bırakmayan ve ölçülemeyen normal buharlaşma kaybı olarak",
   "Ek işlemle standart mamule dönüştürülmesi ekonomik olan kusurlu üretim olarak",
   "Üretim sürecini tamamlamış fakat hiçbir ekonomik değeri bulunmayan bozuk mamul olarak",
   "Teknik standardı karşılayan ve esas satış fiyatından pazarlanabilen sağlam mamul olarak"],
  "Artık, üretimden kalan ve genellikle ana malzemeye göre düşük değeri olsa da satılabilen veya yeniden kullanılabilen fiziksel kalıntıdır.",
  "TMS 2 par. 10 ve 16 - stok maliyetinin ölçümü; maliyet muhasebesi - artık tanımı", "easy")

q("Kalite standardını karşılamayan bir ürün makul bir yeniden işleme maliyetiyle standart mamule dönüştürülebiliyorsa hangi kavram öncelikle kullanılır?",
  "Kusurlu mamul",
  ["Fiziksel varlığı tamamen ortadan kalkmış ve satış değeri bulunmayan üretim firesi",
   "Onarılması ekonomik olmayan, yalnız düşük hurda değeriyle elden çıkarılabilen bozuk mamul",
   "Üretimden kalan ve başka mamullerin girdisi olarak kullanılan artık malzeme",
   "Hiçbir ek işleme ihtiyaç duymadan teknik şartları karşılayan tamamlanmış sağlam mamul"],
  "Kusurlu mamul standardı karşılamaz; ancak ekonomik bir ek işlemle istenen kaliteye getirilebilir.",
  "TMS 2 par. 10 ve 12 - dönüştürme maliyetleri; maliyet muhasebesi - kusurlu mamul")

q("Üretim kayıplarına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Fire fiziksel miktar azalmasıdır\n\nII. Artık düşük de olsa kullanım veya satış değeri taşıyabilir\n\nIII. Kusurlu mamul hiçbir koşulda yeniden işlenemez",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Fire miktar kaybı, artık ise değer taşıyabilen kalıntıdır. Ekonomik biçimde yeniden işlenebilme kusurlu mamulün ayırt edici özelliğidir.",
  "TMS 2 par. 16(a); maliyet muhasebesi - fire, artık ve kusurlu mamul ayrımı")

q("Üretim sürecini tamamladığı hâlde teknik standardı karşılamayan ve ekonomik biçimde onarılamadığı için yalnız hurda bedeliyle satılabilen çıktı nedir?",
  "Bozuk mamul",
  ["Miktarı tamamen kaybolduğu için fiziksel olarak ölçülemeyen normal üretim firesi",
   "Ek işlemle standart kaliteye getirilebildiği için üretime geri alınan kusurlu mamul",
   "Kesim sırasında kalan ve malzeme olarak başka üretimde kullanılabilen artık parça",
   "Teknik standardı tam karşılayan fakat henüz müşteriye sevk edilmemiş sağlam mamul"],
  "Ekonomik onarım olanağı bulunmayan standart dışı fiziksel çıktı bozuk mamuldür; varsa hurda değeri geri kazanım sağlar.",
  "TMS 2 par. 16(a); maliyet muhasebesi - bozuk mamul tanımı")

q("Normal üretim kaybını anormal kayıptan ayırmada en güçlü ölçüt aşağıdakilerden hangisidir?",
  "Verimli üretim koşullarında kaçınılmaz olup olmaması",
  ["Kayıp ortaya çıktığında işletmenin aynı dönemde satış yapıp yapmamış olması",
   "Kayıp miktarının muhasebe kaydından önce nakit olarak tahsil edilip edilmemesi",
   "Üretilen mamulün müşteriye peşin veya vadeli satılması arasındaki finansman tercihi",
   "Kayıp malzemenin satın alındığı tedarikçinin aynı şehirde bulunup bulunmaması"],
  "Normal kayıp, verimli ve olağan üretim koşullarında teknik olarak beklenen düzeydedir; önlenebilir veya olağan dışı aşım anormaldir.",
  "TMS 2 par. 13 ve 16(a) - normal kapasite ve anormal kayıplar")

q("TMS 2'ye göre anormal miktardaki ilk madde, işçilik ve diğer üretim kayıplarının stok maliyeti dışında bırakılmasının sonucu nedir?",
  "Oluştuğu dönemde giderleştirilir",
  ["Sağlam mamullerin maliyetine hiçbir sınır olmadan dağıtılarak stoklarda ertelenir",
   "Üretimle ilgili olduğu için tamamı maddi duran varlık maliyetine eklenerek amortismana tabi tutulur",
   "Satış gerçekleşinceye kadar ayrı bir gelir hesabında bekletilip sonra hasılata aktarılır",
   "İşletmenin tercihine bağlı olarak özkaynakta süresiz biçimde izlenir ve sonuçtan çıkarılır"],
  "TMS 2, anormal miktardaki malzeme, işçilik ve diğer üretim kayıplarını stok maliyetine dâhil etmez; dönem gideri olarak muhasebeleştirir.",
  "TMS 2 par. 16(a) - stok maliyetine alınmayan anormal kayıplar")

q("Normal fire maliyetinin sağlam üretime yüklenmesi hangi ekonomik gerekçeye dayanır?",
  "Sağlam üretimi elde etmek için kaçınılmaz olması",
  ["Normal fireden bağımsız olarak her kaybın yöneticilerin kusurundan kaynaklandığı varsayımına",
   "Fire miktarının her durumda ayrı bir mamul gibi esas satış fiyatından satılabilmesine",
   "Üretim maliyetlerinin stoklara hiçbir koşulda alınamayarak doğrudan gider yazılması ilkesine",
   "Sağlam ürünlerin fireden hiçbir kaynak tüketmeden ve farklı bir süreçte elde edilmesine"],
  "Verimli üretimde kaçınılmaz normal kayıp, sağlam çıktıyı elde etmenin maliyetidir ve uygun biçimde sağlam birimlere yansır.",
  "TMS 2 par. 10, 12 ve 16(a) - normal üretim maliyeti ile anormal kayıp ayrımı")

q("Önlenebilir bir makine ayar hatası nedeniyle olağan sınırı aşan malzeme kaybının sağlam mamullere yüklenmesi neye yol açar?",
  "Stok maliyetinin gereksiz yükselmesine",
  ["Sağlam mamul maliyetinin kayıptan bağımsız olarak otomatik biçimde sıfırlanmasına",
   "Anormal kaybın nakit girişine dönüşerek satış hasılatını artırmasına",
   "Üretim miktarı değişmeden bütün genel üretim giderlerinin sabit kıymete dönüşmesine",
   "Kayıp tutarının özkaynakta gelir olarak raporlanıp dönem kârını artırmasına"],
  "Önlenebilir anormal kaybı sağlam çıktıya yüklemek, verimsizlik maliyetini stokta erteleyerek birim maliyeti şişirir.",
  "TMS 2 par. 16(a) - anormal kayıpların stok maliyeti dışında bırakılması")

q("Bir üretim kaybının normal sınırının belirlenmesinde hangi veri en güvenilir başlangıç noktasıdır?",
  "Teknik standartlarla doğrulanmış verimli üretim verisi",
  ["En yüksek kaybın yaşandığı dönemin hiçbir düzeltme yapılmadan kalıcı ölçü kabul edilmesi",
   "Müşterilerin ödeme vadeleri ile satış personelinin prim oranlarının birlikte kullanılması",
   "Bütçede hedeflenen satış fiyatının üretim miktarından bağımsız olarak kayıp oranına çevrilmesi",
   "Dönem sonu banka bakiyesinin kullanılan hammadde miktarına bölünmesiyle bulunan ölçü"],
  "Normal sınır teknik özellik, geçmişteki verimli çalışma, mühendislik analizi ve gerçekçi üretim koşullarıyla desteklenmelidir.",
  "TMS 2 par. 13 ve 16(a) - normal üretim koşulları ve anormal kayıp ayrımı")

q("Kalite kontrol noktasının üretim sürecinde geç bir aşamada bulunması kayıp raporlamasında neden önemlidir?",
  "Kayıp birimlerin daha fazla maliyet unsuru tüketmiş olabilmesi",
  ["Geç kontrol edilen bütün birimlerin otomatik olarak sağlam mamul sayılmasını zorunlu kılması",
   "Kontrol noktasından önce oluşan direkt malzeme ve işçiliğin muhasebe kayıtlarından silinmesi",
   "Kalite kontrolünün yalnız satış fiyatını belirleyip üretim maliyetini hiç etkilememesi",
   "Geç aşamada bulunan her kaybın normal kabul edilerek dönem gideri olamaması"],
  "Kayıp tespit edilene kadar malzeme ve dönüştürme faaliyetleri tüketilmiş olabilir; eşdeğer üretim ve kayıp maliyeti buna göre ölçülür.",
  "TMS 2 par. 10 ve 12 - dönüştürme maliyetlerinin güvenilir ölçümü", "hard")

q("TMS 2 ve üretim kaybı ayrımına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Normal kayıp sağlam üretimin maliyetine yansıyabilir\n\nII. Anormal kayıp stok maliyetinin dışında bırakılır\n\nIII. Kayıp sınıflandırması teknik ve fiilî verilerle belgelenmelidir",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Kaçınılmaz normal kayıp üretim maliyetinin parçası olabilir; anormal kayıp giderleştirilir ve ayrımın denetlenebilir veriye dayanması gerekir.",
  "TMS 2 par. 13 ve 16(a) - normal kapasite, normal ve anormal üretim kayıpları")

q("Aynı miktardaki kayıp bir ayda teknik nedenlerle kaçınılmaz, başka ayda bakımsızlık nedeniyle önlenebilir olmuşsa nasıl değerlendirilmelidir?",
  "Neden ve koşullara göre ayrı sınıflandırılmalıdır",
  ["Miktarlar aynı olduğu için iki kayıp da gerekçe aranmadan normal kabul edilmelidir",
   "Bakımsızlıktan doğan kayıp daha yüksek satış fiyatıyla telafi edilebildiği için gelir sayılmalıdır",
   "Teknik kayıp da önlenebilir kayıp da daima maddi duran varlık maliyetine eklenmelidir",
   "Kayıp nedenleri maliyet sınıflandırmasını etkilemediğinden ikisi de özkaynakta izlenmelidir"],
  "Yalnız miktar değil, kaybın verimli çalışma koşullarında kaçınılmaz olup olmadığı değerlendirilir; aynı miktar farklı nedenlerle farklı sınıflanabilir.",
  "TMS 2 par. 16(a) - anormal kayıpların niteliğe göre belirlenmesi", "hard")

q("Normal kayıp oranının yıllarca güncellenmeden kullanılması hangi riski doğurur?",
  "Verimsizliğin normal maliyet içinde gizlenmesi",
  ["Bütün üretim kayıplarının otomatik olarak satış hasılatına dönüşmesi ve kârı artırması",
   "Direkt malzeme tüketiminin fiziksel kayıtlardan bağımsız olarak tamamen ortadan kalkması",
   "Stokların her durumda net gerçekleşebilir değerinin üzerinde satılmasının garanti edilmesi",
   "Mamul miktarı değişmese bile banka bakiyesinin üretim maliyetiyle eşitlenmesi"],
  "Teknoloji ve süreç iyileştikçe gerçekçi normal kayıp düzeyi değişebilir; eski yüksek standart önlenebilir kaybı normal gösterir.",
  "TMS 2 par. 13 ve 16(a) - normal üretim koşullarının güncel ve gerçekçi belirlenmesi")

q("Üretim kaybının türü ve nedeni ayrı kodlarla izleniyorsa bunun temel yönetim yararı nedir?",
  "Önlenebilir kaybın sorumluluk ve eğilimini görmek",
  ["Her kayıp türünü hiçbir analiz yapmadan aynı maliyet hesabında birleştirip farkları ortadan kaldırmak",
   "Satış birimlerinin tahsilat performansını üretim miktarından bağımsız olarak ölçmek",
   "Üretim giderlerini yalnız müşteri ödeme vadelerine göre sınıflandırıp stok hesaplarını kaldırmak",
   "Bütün normal ve anormal kayıpları sağlam ürün kabul ederek fiziksel uzlaştırmayı gereksiz kılmak"],
  "Tür, neden, bölüm ve sorumluluk kodları; tekrar eden arıza, hatalı ayar veya malzeme sorununun kaynağını görünür kılar.",
  "1 Sıra No.lu MSUGT - gider yerleri ve çeşitleri itibarıyla izleme; üretim kaybı kontrolü")


# ── B. Fire miktarı, normal maliyet ve anormal kayıp (15) ────────────────
input_qty, normal_rate = 20_000, 0.04
normal_loss = input_qty * normal_rate
expected_good = input_qty - normal_loss
assert (normal_loss, expected_good) == (800, 19_200)
q(f"Bir safhaya {tr(input_qty)} kg malzeme girmiştir. Verimli üretim koşullarında normal fire girdinin %{int(normal_rate*100)}'üdür. Dönem için normal fire miktarı kaç kg'dır?",
  f"{tr(normal_loss)} kg",
  [f"{tr(expected_good)} kg fire dışındaki beklenen sağlam üretimin kayıp sayıldığı miktar",
   f"{tr(input_qty/(normal_rate*100))} kg girdi miktarının yüzde oranına bölündüğü sonuç",
   f"{tr(input_qty*normal_rate*2)} kg normal fire oranının iki kez uygulandığı miktar",
   f"{tr(input_qty-normal_rate*100)} kg yüzde değerinin kilogram olarak girdiden çıkarıldığı sonuç"],
  f"Normal fire {tr(input_qty)} × %{int(normal_rate*100)} = {tr(normal_loss)} kg'dır.",
  "TMS 2 par. 16(a) - normal ve anormal üretim kayıplarının ayrılması")

actual_loss = 1_100
abnormal_loss = actual_loss - normal_loss
actual_good = input_qty - actual_loss
assert (abnormal_loss, actual_good) == (300, 18_900)
q(f"Aynı safhada fiilî fire {tr(actual_loss)} kg, normal sınır {tr(normal_loss)} kg'dır. Normal sınırı aşan anormal fire kaç kg'dır?",
  f"{tr(abnormal_loss)} kg",
  [f"{tr(actual_loss)} kg fiilî kaybın tamamının anormal sayıldığı miktar",
   f"{tr(normal_loss)} kg normal sınırın anormal kayıp olarak raporlandığı miktar",
   f"{tr(actual_good)} kg sağlam üretimin anormal fire kabul edildiği miktar",
   f"{tr(input_qty-normal_loss)} kg beklenen sağlam üretimin kayıp sayıldığı miktar"],
  f"Anormal fire fiilî kaybın normal sınırı aşan kısmıdır: {tr(actual_loss)} − {tr(normal_loss)} = {tr(abnormal_loss)} kg.",
  "TMS 2 par. 16(a) - normalin üzerindeki üretim kayıpları")

q(f"Üretime giren {tr(input_qty)} kg malzemeden {tr(actual_loss)} kg fiilî fire çıkmıştır. Başka miktar farkı yoksa sağlam üretim kaç kg'dır?",
  f"{tr(actual_good)} kg",
  [f"{tr(expected_good)} kg yalnız normal fire düşülerek fiilî kayıp aşımının dışlandığı miktar",
   f"{tr(input_qty+actual_loss)} kg fire miktarının girdiye eklenmesiyle bulunan sonuç",
   f"{tr(actual_loss)} kg kayıp miktarının sağlam üretim olarak kabul edildiği sonuç",
   f"{tr(input_qty-normal_loss+abnormal_loss)} kg anormal firenin sağlam üretime geri eklendiği sonuç"],
  f"Fiziksel uzlaştırmada sağlam üretim {tr(input_qty)} − {tr(actual_loss)} = {tr(actual_good)} kg'dır.",
  "TMS 2 par. 10 ve 12 - üretim miktarı ile maliyet akışının uzlaştırılması")

total_cost = 768_000
normal_unit_cost = total_cost / expected_good
assert normal_unit_cost == 40
q(f"Toplam safha maliyeti {tr(total_cost)} TL, normal fire sonrası beklenen sağlam üretim {tr(expected_good)} kg'dır. Normal kaybın maliyeti sağlam üretime yüklenirse kg başına maliyet kaç TL'dir?",
  f"{tr(normal_unit_cost)} TL/kg",
  [f"{tr(total_cost/input_qty)} TL/kg normal fireyi maliyetsiz sağlam çıktı gibi paydaya alan sonuç",
   f"{tr(total_cost/normal_loss)} TL/kg yalnız fire miktarını payda kabul eden sonuç",
   f"{tr(expected_good/total_cost)} TL/kg maliyet ile miktarın ters bölündüğü sonuç",
   f"{tr(total_cost/actual_loss)} TL/kg fiilî kaybın tamamını sağlam üretim paydası yapan sonuç"],
  f"Normal fire ayrı çıktı taşımaz; maliyet beklenen sağlam miktara yayılır: {tr(total_cost)} / {tr(expected_good)} = {tr(normal_unit_cost)} TL/kg.",
  "TMS 2 par. 10, 12 ve 16(a) - normal kaybın sağlam üretim maliyetine yansıması")

q("Fire miktar analizine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Beklenen sağlam miktar girdiden normal fire çıkarılarak bulunabilir\n\nII. Anormal fire fiilî kaybın normal sınırı aşan kısmıdır\n\nIII. Fiilî fire normal sınırdan düşükse mutlaka anormal kayıp vardır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Beklenen sağlam çıktı normal kayıp sonrası miktardır; aşım anormal kayıptır. Fiilî kaybın sınırın altında olması anormal kayıp oluşturmaz.",
  "TMS 2 par. 16(a) - normal ve anormal kayıp ölçümü")

abnormal_cost = abnormal_loss * normal_unit_cost
good_cost = actual_good * normal_unit_cost
assert (abnormal_cost, good_cost, abnormal_cost + good_cost) == (12_000, 756_000, total_cost)
q(f"Normal maliyet {tr(normal_unit_cost)} TL/kg ve anormal fire {tr(abnormal_loss)} kg ise stok maliyeti dışında bırakılacak anormal fire tutarı kaç TL'dir?",
  f"{tr(abnormal_cost)} TL",
  [f"{tr(actual_loss*normal_unit_cost)} TL normal ve anormal firenin tamamının dönem gideri sayıldığı tutar",
   f"{tr(normal_loss*normal_unit_cost)} TL yalnız normal fire miktarının giderleştirildiği tutar",
   f"{tr(actual_good*normal_unit_cost)} TL sağlam üretim maliyetinin kayıp tutarı sayıldığı sonuç",
   f"{tr(total_cost/abnormal_loss)} TL toplam maliyetin anormal miktara bölündüğü sonuç"],
  f"Anormal kayıp tutarı {tr(abnormal_loss)} × {tr(normal_unit_cost)} = {tr(abnormal_cost)} TL'dir.",
  "TMS 2 par. 16(a) - anormal üretim kayıplarının dönem gideri olması")

q(f"Fiilî sağlam üretim {tr(actual_good)} kg ve normal birim maliyet {tr(normal_unit_cost)} TL/kg ise sağlam üretime verilecek maliyet kaç TL'dir?",
  f"{tr(good_cost)} TL",
  [f"{tr(total_cost)} TL anormal kaybın da sağlam stok maliyetinde bırakıldığı tutar",
   f"{tr(abnormal_cost)} TL yalnız anormal kayıp tutarının sağlam üretime verildiği sonuç",
   f"{tr(expected_good*normal_unit_cost)} TL fiilî yerine beklenen sağlam miktarın stoklandığı tutar",
   f"{tr(actual_loss*normal_unit_cost)} TL kayıp miktarının sağlam mamul maliyeti sayıldığı sonuç"],
  f"Sağlam çıktı maliyeti {tr(actual_good)} × {tr(normal_unit_cost)} = {tr(good_cost)} TL'dir; kalan {tr(abnormal_cost)} TL anormal kayıptır.",
  "TMS 2 par. 10 ve 16(a) - sağlam stok ve anormal kayıp maliyetinin ayrılması")

q(f"Toplam maliyet {tr(total_cost)} TL; sağlam üretim maliyeti {tr(good_cost)} TL ve anormal fire maliyeti {tr(abnormal_cost)} TL olarak hesaplanmıştır. Uzlaştırma sonucu nedir?",
  "Toplam maliyet eksiksiz ayrıştırılmıştır",
  ["Sağlam üretime 12.000 TL fazla yüklenmiş ve toplam maliyet aşılmıştır",
   "Anormal kayıp maliyeti hesap dışı bırakıldığı için 12.000 TL dağıtılmamış bakiye vardır",
   "Yalnız sağlam üretim maliyeti toplamla karşılaştırılabildiğinden uzlaştırma kurulamaz",
   "İki tutar toplam maliyetten 756.000 TL fazla olduğu için kayıtların tamamı ters çevrilmelidir"],
  f"{tr(good_cost)} + {tr(abnormal_cost)} = {tr(total_cost)} TL'dir; sağlam stok ile dönem kaybı toplam maliyeti açıklar.",
  "TMS 2 par. 10 ve 16(a) - maliyet uzlaştırması")

gross_cost, scrap_value, expected_units = 500_000, 20_000, 12_000
net_cost = gross_cost - scrap_value
unit_after_recovery = net_cost / expected_units
assert (net_cost, unit_after_recovery) == (480_000, 40)
q(f"Normal bozuk mamullerden beklenen hurda geri kazanımı {tr(scrap_value)} TL, brüt süreç maliyeti {tr(gross_cost)} TL ve beklenen sağlam çıktı {tr(expected_units)} birimdir. Geri kazanım düşülürse sağlam birim maliyeti kaç TL'dir?",
  f"{tr(unit_after_recovery)} TL/birim",
  [f"{tr(gross_cost/expected_units)} TL/birim kalıntı geri kazanımının maliyetten düşülmediği sonuç",
   f"{tr((gross_cost+scrap_value)/expected_units)} TL/birim geri kazanımın maliyete eklendiği sonuç",
   f"{tr(scrap_value/expected_units)} TL/birim yalnız kalıntı değerinin dağıtıldığı sonuç",
   f"{tr(net_cost/scrap_value)} TL/birim net maliyetin sağlam miktar yerine kalıntı değerine bölündüğü sonuç"],
  f"Net dağıtılacak maliyet {tr(gross_cost)} − {tr(scrap_value)} = {tr(net_cost)} TL; birim maliyet {tr(net_cost)} / {tr(expected_units)} = {tr(unit_after_recovery)} TL'dir.",
  "TMS 2 par. 10 ve 12 - üretim maliyetinin geri kazanım sonrası sistematik dağıtımı", "hard")

actual_units2, abnormal_units2 = 11_700, 300
good_cost2 = actual_units2 * unit_after_recovery
abnormal_cost2 = abnormal_units2 * unit_after_recovery
assert (good_cost2, abnormal_cost2, good_cost2 + abnormal_cost2) == (468_000, 12_000, net_cost)
q(f"Geri kazanım sonrası dağıtılacak maliyet {tr(net_cost)} TL ve normal birim maliyet {tr(unit_after_recovery)} TL'dir. Fiilî sağlam çıktı {tr(actual_units2)}, anormal kayıp {tr(abnormal_units2)} birimse sağlam çıktıya ayrılacak tutar kaç TL'dir?",
  f"{tr(good_cost2)} TL",
  [f"{tr(net_cost)} TL anormal kaybın da sağlam çıktı maliyetine bırakıldığı tutar",
   f"{tr(abnormal_cost2)} TL yalnız anormal kayıp tutarının sağlam çıktı sayıldığı sonuç",
   f"{tr(expected_units*unit_after_recovery)} TL fiilî yerine beklenen miktarın stoklandığı sonuç",
   f"{tr(gross_cost)} TL geri kazanım ve anormal kayıp ayrımı yapılmadan aktarılan brüt tutar"],
  f"Sağlam üretim maliyeti {tr(actual_units2)} × {tr(unit_after_recovery)} = {tr(good_cost2)} TL'dir.",
  "TMS 2 par. 10 ve 16(a) - geri kazanım sonrası sağlam stok ve anormal kayıp ayrımı", "hard")

q("Normal bozulma ve geri kazanıma ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Güvenilir hurda değeri dağıtılacak net maliyeti azaltabilir\n\nII. Normal bozulmanın net maliyeti sağlam üretimce taşınabilir\n\nIII. Anormal bozulma da stokta bırakılmalıdır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Hurda geri kazanımı maliyet yükünü azaltabilir ve normal bozulma sağlam çıktı maliyetine yansır. Anormal bozulma stok dışında bırakılır.",
  "TMS 2 par. 10, 12 ve 16(a) - geri kazanım, normal ve anormal kayıp")

planned_input, actual_input, output_qty = 15_000, 15_300, 14_400
planned_loss = planned_input - output_qty
actual_loss3 = actual_input - output_qty
excess_usage = actual_input - planned_input
assert (planned_loss, actual_loss3, excess_usage) == (600, 900, 300)
q(f"{tr(output_qty)} kg sağlam çıktı için teknik reçete {tr(planned_input)} kg girdi öngörürken fiilî girdi {tr(actual_input)} kg olmuştur. Çıktı aynıysa standart üzerindeki ek malzeme kaybı kaç kg'dır?",
  f"{tr(excess_usage)} kg",
  [f"{tr(planned_loss)} kg teknik reçetedeki toplam normal kaybın tamamı",
   f"{tr(actual_loss3)} kg fiilî toplam kaybın normal kısım ayrılmadan raporlanan miktarı",
   f"{tr(output_qty)} kg sağlam üretimin ek kayıp olarak kabul edildiği miktar",
   f"{tr(actual_input+planned_input-output_qty)} kg iki girdi miktarının birlikte kullanıldığı sonuç"],
  f"Aynı çıktı için fiilî girdi standart girdiyi {tr(actual_input)} − {tr(planned_input)} = {tr(excess_usage)} kg aşmıştır.",
  "TMS 2 par. 16(a) - anormal malzeme kullanımının ayrılması", "hard")

cost_per_kg = 28
excess_cost = excess_usage * cost_per_kg
assert excess_cost == 8_400
q(f"Standart üzerindeki ek malzeme kaybı {tr(excess_usage)} kg, malzeme maliyeti {tr(cost_per_kg)} TL/kg ise anormal kullanımın maliyet etkisi kaç TL'dir?",
  f"{tr(excess_cost)} TL",
  [f"{tr(actual_loss3*cost_per_kg)} TL fiilî kaybın normal kısmıyla birlikte giderleştirildiği tutar",
   f"{tr(planned_loss*cost_per_kg)} TL teknik normal kaybın anormal kullanım sayıldığı tutar",
   f"{tr(actual_input*cost_per_kg)} TL üretime giren tüm malzemenin kayıp kabul edildiği tutar",
   f"{tr(output_qty*cost_per_kg)} TL sağlam üretimin anormal kayıp maliyeti sayıldığı sonuç"],
  f"Anormal kullanım maliyeti {tr(excess_usage)} × {tr(cost_per_kg)} = {tr(excess_cost)} TL'dir.",
  "TMS 2 par. 16(a) - anormal ilk madde kaybının dönem gideri")

q("Fiilî fire oranı teknik normal sınırı aştığında yöneticinin ilk yapması gereken nedir?",
  "Aşımın nedenini bölüm ve süreç bazında araştırmak",
  ["Normal sınırı fiilî kayıp oranına yükselterek her aşımı otomatik olarak normalleştirmek",
   "Kayıp verisini üretim raporundan çıkarıp yalnız satış bölümünün performansına eklemek",
   "Aşım tutarını hiçbir inceleme yapmadan sağlam ürün stokuna eşit dağıtmak",
   "Fiziksel girdi ve çıktı kayıtlarını uzlaştırmadan kaybı tahsilat hesabına aktarmak"],
  "Kök neden analizi; malzeme kalitesi, makine ayarı, bakım, işçilik ve ölçüm hatasını ayırarak önlenebilir kaybı yönetir.",
  "TMS 2 par. 16(a); 1 Sıra No.lu MSUGT - gider yerleri itibarıyla kayıp izleme")

q("Fire maliyeti normal sınırdan hesaplanırken fiilî sağlam miktarın fiziksel üretim raporuyla uyuşmaması hangi riske işaret eder?",
  "Kayıp veya çıktı kaydının eksik olmasına",
  ["Bütün stokların satış fiyatının otomatik olarak yanlış belirlendiğine ve tahsilatın imkânsız olduğuna",
   "Normal fire oranının her durumda sıfır olması gerektiğine ve teknik kaybın bulunmadığına",
   "Genel üretim giderlerinin maddi duran varlık hesabına aktarılmasının zorunlu olduğuna",
   "Mamul maliyetinin yalnız banka bakiyesinden hesaplanabileceğine ve miktarın önemsiz olduğuna"],
  "Girdi = sağlam çıktı + kayıplar fiziksel eşitliği sağlanmıyorsa ölçüm, kayıt, sayım veya yetkisiz çıkış araştırılmalıdır.",
  "TMS 2 par. 10 ve 12 - güvenilir stok maliyeti ve fiziksel miktar uzlaştırması")


# ── C. Bozuk ve kusurlu mamul, yeniden işleme (15) ───────────────────────
q("Standart dışı bir birimin yeniden işleme maliyeti, yeniden işleme sonrası sağlayacağı ekonomik faydadan yüksekse nasıl sınıflandırılması daha uygundur?",
  "Bozuk mamul",
  ["Ek işlem maliyeti ekonomik olduğu için üretime geri alınacak kusurlu mamul olarak",
   "Fiziksel miktarı tamamen yok olduğu için hiçbir kalıntı bırakmayan fire olarak",
   "Ana üretimden kalan ve başka işte girdi olarak kullanılacak artık malzeme olarak",
   "Standart kaliteyi karşıladığı için doğrudan mamul stokuna alınacak sağlam ürün olarak"],
  "Ekonomik olarak düzeltilemeyen standart dışı çıktı bozuk mamuldür; varsa geri kazanım değeri dikkate alınır.",
  "TMS 2 par. 16(a); maliyet muhasebesi - bozuk ve kusurlu mamul ayrımı", "easy")

q("Belirli bir müşterinin olağan dışı tasarım talebinden doğan, normal kabul edilen yeniden işleme maliyeti başka siparişlerle ilişkili değilse nereye yüklenmelidir?",
  "İlgili siparişin maliyetine",
  ["Bütün siparişlere satış tutarları oranında dağıtılmak üzere genel yönetim giderlerine",
   "Üretimle ilişkisi kesilerek finansman gideri olarak dönem sonucuna doğrudan",
   "Yalnız kusursuz çalışan diğer üretim bölümlerinin genel üretim gideri havuzuna",
   "Müşteriden tahsil edilinceye kadar üretim stoklarından bağımsız alacak hesabına"],
  "Yeniden işleme belirli işin özelliklerinden kaynaklanıyor ve normal kabul ediliyorsa maliyet o siparişe izlenebilir.",
  "TMS 2 par. 10 ve 12 - belirli maliyet nesnesine doğrudan izlenebilen dönüştürme maliyeti")

q("Birçok siparişte olağan düzeyde ortaya çıkan ve belirli işe güvenilir biçimde bağlanamayan yeniden işleme maliyeti nasıl ele alınabilir?",
  "Genel üretim gideri havuzunda",
  ["Yalnız en yüksek kârlı siparişe doğrudan yüklenip diğer işlerden tamamen çıkarılarak",
   "Üretimle ilgisi yokmuş gibi satış ve pazarlama giderlerine eşit paylaştırılarak",
   "Tamamı maddi duran varlık hesabına eklenip uzun yıllar boyunca amorti edilerek",
   "Hiçbir mamule veya döneme bağlanmadan özkaynak hesabında süresiz bekletilerek"],
  "Ortak ve normal yeniden işleme maliyeti uygun bir genel üretim gideri havuzunda toplanıp yararlanan üretime sistematik dağıtılabilir.",
  "TMS 2 par. 12 - genel üretim giderlerinin sistematik dağıtımı")

q("Önlenebilir operatör hatasından doğan olağan dışı yeniden işleme maliyeti için hangi yaklaşım uygundur?",
  "Anormal kayıp olarak giderleştirmek",
  ["Sağlam mamullere yükleyip verimsizliği stok maliyeti içinde sonraki dönemlere ertelemek",
   "Müşteri talebinden bağımsız olsa da yalnız en son tamamlanan siparişe doğrudan yüklemek",
   "Üretimle ilgili olduğu için bina maliyetine ekleyip amortisman yoluyla dağıtmak",
   "Satış gerçekleşmediği sürece gelir hesabında bekletip daha sonra hasılat yapmak"],
  "Önlenebilir ve olağan sınırı aşan yeniden işleme, stokların elde edilmesi için normal maliyet değildir; dönem kaybıdır.",
  "TMS 2 par. 16(a) - anormal işçilik ve diğer üretim maliyetleri")

q("Bozuk ve kusurlu mamul maliyetlerine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Belirli işe özgü normal yeniden işleme o işe yüklenebilir\n\nII. Ortak normal yeniden işleme GÜG üzerinden dağıtılabilir\n\nIII. Anormal yeniden işleme sağlam stok maliyetinde ertelenmelidir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Normal maliyet nedensellik ilişkisine göre işe veya GÜG havuzuna yüklenebilir. Anormal yeniden işleme stok dışında bırakılır.",
  "TMS 2 par. 12 ve 16(a) - normal ve anormal yeniden işleme maliyetleri")

rework_dm, rework_dl, rework_oh = 6_000, 8_000, 4_000
rework_total = rework_dm + rework_dl + rework_oh
assert rework_total == 18_000
q(f"Belirli siparişe ait kusurlu birimlerin düzeltilmesinde {tr(rework_dm)} TL malzeme, {tr(rework_dl)} TL işçilik ve {tr(rework_oh)} TL GÜG tüketilmiştir. Normal ve işe özgü yeniden işleme maliyeti kaç TL'dir?",
  f"{tr(rework_total)} TL",
  [f"{tr(rework_dm+rework_dl)} TL genel üretim giderinin yeniden işleme dışında bırakıldığı tutar",
   f"{tr(rework_dl+rework_oh)} TL düzeltme malzemesinin maliyete alınmadığı sonuç",
   f"{tr(rework_dm+rework_oh)} TL yeniden işleme işçiliğinin maliyet dışında bırakıldığı tutar",
   f"{tr(rework_dm+rework_dl-rework_oh)} TL genel üretim giderinin toplamdan çıkarıldığı sonuç"],
  f"Yeniden işleme maliyeti {tr(rework_dm)} + {tr(rework_dl)} + {tr(rework_oh)} = {tr(rework_total)} TL'dir.",
  "TMS 2 par. 10 ve 12 - yeniden işlemede tüketilen dönüştürme maliyetleri")

job_before = 150_000
job_after = job_before + rework_total
assert job_after == 168_000
q(f"Sipariş kartında yeniden işleme öncesi {tr(job_before)} TL vardır. İşe özgü normal yeniden işleme {tr(rework_total)} TL ise düzeltilen siparişin yeni toplam maliyeti kaç TL'dir?",
  f"{tr(job_after)} TL",
  [f"{tr(job_before)} TL yeniden işleme maliyetinin hiçbir maliyet nesnesine yüklenmediği tutar",
   f"{tr(job_before-rework_total)} TL düzeltme maliyetinin sipariş kartından indirildiği sonuç",
   f"{tr(rework_total)} TL yalnız yeniden işleme maliyetinin sipariş toplamı kabul edildiği tutar",
   f"{tr(job_before+rework_total*2)} TL yeniden işleme maliyetinin karta iki kez eklendiği sonuç"],
  f"İşe özgü normal yeniden işleme karta eklenir: {tr(job_before)} + {tr(rework_total)} = {tr(job_after)} TL.",
  "TMS 2 par. 10 ve 12 - belirli siparişe ait normal yeniden işleme maliyeti")

common_rework, total_driver, order_driver = 24_000, 1_200, 180
common_rate = common_rework / total_driver
order_share = common_rate * order_driver
assert (common_rate, order_share) == (20, 3_600)
q(f"Ortak normal yeniden işleme havuzu {tr(common_rework)} TL, toplam yükleme ölçüsü {tr(total_driver)} saattir. Bir sipariş {tr(order_driver)} saat kullanmışsa bu siparişin havuz payı kaç TL'dir?",
  f"{tr(order_share)} TL",
  [f"{tr(common_rate)} TL yalnız bir saatlik havuz oranının sipariş toplamı sayıldığı tutar",
   f"{tr(common_rework/order_driver)} TL havuzun yalnız sipariş saatine bölündüğü sonuç",
   f"{tr(common_rework-order_share)} TL diğer siparişlerin payının bu işe yüklendiği tutar",
   f"{tr(total_driver*order_driver)} TL maliyet yerine iki faaliyet miktarının çarpıldığı sonuç"],
  f"Saat başına havuz oranı {tr(common_rework)} / {tr(total_driver)} = {tr(common_rate)} TL'dir. Sipariş payı {tr(order_driver)} × {tr(common_rate)} = {tr(order_share)} TL olur.",
  "TMS 2 par. 12 - ortak normal yeniden işleme maliyetinin sistematik dağıtımı")

abnormal_rework = 15_000
q(f"Önlenebilir ayar hatasından doğan {tr(abnormal_rework)} TL yeniden işleme maliyetinin tamamı olağan sınırın üzerindedir. Stok maliyetine alınacak tutar kaç TL'dir?",
  "0 TL",
  [f"{tr(abnormal_rework)} TL anormal maliyetin tamamının sağlam stoklara yüklendiği tutar",
   f"{tr(abnormal_rework/2)} TL dayanak olmadan kaybın yarısının stokta bırakıldığı tutar",
   f"{tr(abnormal_rework*2)} TL anormal maliyetin iki kez stok maliyetine eklendiği tutar",
   f"{tr(abnormal_rework+rework_total)} TL farklı yeniden işleme vakalarının birlikte stoklandığı tutar"],
  "Anormal yeniden işleme TMS 2 uyarınca stok maliyeti dışında bırakılır; verilen tutarın tamamı dönem gideridir.",
  "TMS 2 par. 16(a) - anormal işçilik ve diğer üretim maliyetlerinin giderleştirilmesi")

spoiled_cost, recovery = 50_000, 8_000
net_spoilage = spoiled_cost - recovery
assert net_spoilage == 42_000
q(f"Normal bozuk mamullere tespit noktasına kadar {tr(spoiled_cost)} TL maliyet yüklenmiş, hurda satışından {tr(recovery)} TL geri kazanım beklenmektedir. Sağlam üretimin taşıyacağı net bozulma maliyeti kaç TL'dir?",
  f"{tr(net_spoilage)} TL",
  [f"{tr(spoiled_cost)} TL geri kazanım değeri hiç dikkate alınmadan yüklenen brüt tutar",
   f"{tr(recovery)} TL yalnız hurda değerinin bozulma maliyeti kabul edildiği sonuç",
   f"{tr(spoiled_cost+recovery)} TL geri kazanımın maliyete ilave edildiği sonuç",
   f"{tr(spoiled_cost-recovery*2)} TL hurda değerinin maliyetten iki kez indirildiği sonuç"],
  f"Net normal bozulma maliyeti {tr(spoiled_cost)} − {tr(recovery)} = {tr(net_spoilage)} TL'dir.",
  "TMS 2 par. 10 ve 12 - normal üretim maliyeti ve geri kazanımın netleştirilmesi", "hard")

good_units3 = 700
spoilage_per_good = net_spoilage / good_units3
assert spoilage_per_good == 60
q(f"Net normal bozulma maliyeti {tr(net_spoilage)} TL ve bu maliyeti taşıyan sağlam üretim {tr(good_units3)} birimdir. Sağlam birim başına bozulma payı kaç TL'dir?",
  f"{tr(spoilage_per_good)} TL/birim",
  [f"{tr(spoiled_cost/good_units3)} TL/birim hurda geri kazanımının düşülmediği sonuç",
   f"{tr(recovery/good_units3)} TL/birim yalnız geri kazanım tutarının dağıtıldığı sonuç",
   f"{tr(net_spoilage/(good_units3+100))} TL/birim bozuk birimlerin de sağlam paydaya eklendiği sonuç",
   f"{tr(good_units3/net_spoilage)} TL/birim miktar ile maliyetin ters bölündüğü sonuç"],
  f"Birim pay {tr(net_spoilage)} / {tr(good_units3)} = {tr(spoilage_per_good)} TL'dir.",
  "TMS 2 par. 10 ve 12 - normal bozuk mamul maliyetinin sağlam üretime dağıtımı")

bad_units, full_cost_each, salvage_each = 30, 120, 20
abnormal_spoilage_loss = bad_units * (full_cost_each - salvage_each)
assert abnormal_spoilage_loss == 3_000
q(f"Anormal bozuk mamul {tr(bad_units)} birimdir. Birim başına tespit noktasına kadarki maliyet {tr(full_cost_each)} TL, geri kazanım {tr(salvage_each)} TL ise net anormal kayıp kaç TL'dir?",
  f"{tr(abnormal_spoilage_loss)} TL",
  [f"{tr(bad_units*full_cost_each)} TL geri kazanımın anormal kayıptan düşülmediği brüt tutar",
   f"{tr(bad_units*salvage_each)} TL yalnız geri kazanımın kayıp sayıldığı sonuç",
   f"{tr(bad_units*(full_cost_each+salvage_each))} TL geri kazanımın kayba eklendiği sonuç",
   f"{tr(full_cost_each-salvage_each)} TL yalnız bir bozuk birimin net kaybının toplam sayıldığı tutar"],
  f"Birim net kayıp {tr(full_cost_each)} − {tr(salvage_each)} = {tr(full_cost_each-salvage_each)} TL; toplam {tr(bad_units)} × {tr(full_cost_each-salvage_each)} = {tr(abnormal_spoilage_loss)} TL'dir.",
  "TMS 2 par. 16(a) - anormal bozuk mamul maliyetinin giderleştirilmesi", "hard")

q("Yeniden işleme kararında aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Ek işlem maliyeti geri kazanılacak faydayla karşılaştırılır\n\nII. Normal ve anormal nedenler ayrı raporlanır\n\nIII. Ekonomik düzeltme mümkünse çıktı kusurlu mamul olarak izlenebilir",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Yeniden işleme ekonomik faydaya göre kararlaştırılır; kaybın nedeni maliyet işlemini belirler ve ekonomik düzeltilebilirlik kusurlu mamulü ayırır.",
  "TMS 2 par. 10, 12 ve 16(a) - normal/anormal yeniden işleme ve güvenilir maliyet ölçümü")

q("Kalite kontrolünde kusurlu bulunan birimler yeniden işlendikten sonra aynı kontrolü tekrar geçiyorsa ikinci kontrol maliyeti nasıl değerlendirilmelidir?",
  "Yeniden işleme maliyetinin parçası olarak",
  ["Üretimle hiçbir ilişkisi bulunmadığı için yalnız finansman gideri olarak",
   "Satış hasılatından bağımsız bir özkaynak hareketi olarak dönem dışında",
   "Müşteri ödeme yapıncaya kadar üretim maliyetinden bağımsız bir alacak olarak",
   "İlk kontrol yapılmış olduğu için hiçbir maliyet nesnesine kaydedilmeden"],
  "Düzeltmenin başarılı olup olmadığını belirlemek için gereken tekrar kontrolü, yeniden işleme faaliyetinin maliyetidir; normal/anormal niteliğine göre yüklenir.",
  "TMS 2 par. 10, 12 ve 16(a) - yeniden işleme faaliyetinin maliyet unsurları")

q("Bozuk mamul miktarı sağlam mamul olarak raporlanırsa hangi iki bilgi birlikte bozulur?",
  "Fiziksel çıktı ve birim maliyet",
  ["Yalnız müşteri ödeme vadesi ile banka hesabının faiz oranı bilgileri",
   "Yalnız işletmenin sermaye tutarı ile ortakların oy hakkı bilgileri",
   "Yalnız satış personelinin primleri ile genel yönetim kira bilgileri",
   "Yalnız tedarikçinin adresi ile malzemenin satın alma vadesi bilgileri"],
  "Bozuk birimi sağlam saymak sağlam miktarı fazla, sağlam birim başına maliyeti hatalı gösterir ve stok değerini etkiler.",
  "TMS 2 par. 10 ve 12 - stok miktarı ve maliyetinin güvenilir raporlanması")


# ── D. Artık malzeme, geri kazanım ve bütünleşik kontrol (15) ────────────
q("Belirli bir siparişin özel kesiminden çıkan artık malzemenin satış değeri güvenilir biçimde o işe bağlanabiliyorsa hangi işlem nedensellik ilişkisini en iyi yansıtır?",
  "İlgili sipariş maliyetini azaltmak",
  ["Satış değerini bütün siparişlere üretim miktarından bağımsız olarak eşit dağıtmak",
   "Artık gelirini üretimle ilişkisiz finansman geliri sayarak sipariş kartını değiştirmemek",
   "Geri kazanımı yalnız en yüksek maliyetli başka siparişin direkt işçiliğinden düşmek",
   "Artık değerini maddi duran varlık hesabına ekleyip yıllar boyunca amorti etmek"],
  "Artık belirli işten doğmuşsa güvenilir net gerçekleşebilir değeri o işin malzeme veya üretim maliyetini azaltabilir.",
  "TMS 2 par. 10 ve 12 - maliyetin ilgili stok kalemine güvenilir biçimde yüklenmesi")

q("Birçok ürünün ortak üretiminden çıkan ve belirli mamule izlenemeyen artık satış değerinin üretim maliyetine etkisi nasıl gösterilebilir?",
  "Ortak GÜG maliyetini azaltarak",
  ["Yalnız bir müşterinin sipariş kartına rastgele alacak yazıp diğer ürünleri etkilemeden",
   "Üretimle ilişkisi olmadığı varsayımıyla sermaye hesabına doğrudan eklenerek",
   "Bütün artık tutarı satış personelinin ücretlerinden düşüp stokları değiştirmeden",
   "Geri kazanım gerçekleştiği hâlde hiçbir hesapta göstermeyip maliyeti brüt bırakarak"],
  "Belirli işe izlenemeyen ortak artık geri kazanımı, uygun ortak üretim/GÜG havuzunun net maliyetini azaltabilir.",
  "TMS 2 par. 12 - ortak üretim maliyetlerinin sistematik dağıtımı")

scrap_qty, scrap_price = 1_250, 16
scrap_recovery = scrap_qty * scrap_price
assert scrap_recovery == 20_000
q(f"Kesimden çıkan {tr(scrap_qty)} kg artık malzeme {tr(scrap_price)} TL/kg bedelle satılabilecektir. Tahmini geri kazanım değeri kaç TL'dir?",
  f"{tr(scrap_recovery)} TL",
  [f"{tr(scrap_qty+scrap_price)} TL miktar ile birim değerin toplanmasıyla bulunan sonuç",
   f"{tr(scrap_qty/scrap_price)} TL miktarın birim satış değerine bölündüğü sonuç",
   f"{tr(scrap_price)} TL yalnız bir kilogramlık artık değerinin toplam sayıldığı tutar",
   f"{tr(scrap_qty*scrap_price*2)} TL artık değerinin iki kez hesaplandığı sonuç"],
  f"Geri kazanım değeri {tr(scrap_qty)} × {tr(scrap_price)} = {tr(scrap_recovery)} TL'dir.",
  "TMS 2 par. 10 ve 12 - artık malzeme geri kazanımının maliyet ölçümünde dikkate alınması")

job_material_before = 180_000
job_material_net = job_material_before - scrap_recovery
assert job_material_net == 160_000
q(f"Belirli siparişin brüt malzeme maliyeti {tr(job_material_before)} TL, yalnız bu işten doğan artık geri kazanımı {tr(scrap_recovery)} TL'dir. Net malzeme maliyeti kaç TL olur?",
  f"{tr(job_material_net)} TL",
  [f"{tr(job_material_before)} TL geri kazanımın sipariş maliyetini hiç etkilemediği tutar",
   f"{tr(job_material_before+scrap_recovery)} TL artık değerinin maliyete eklendiği sonuç",
   f"{tr(scrap_recovery)} TL yalnız artık değerinin sipariş maliyeti sayıldığı tutar",
   f"{tr(job_material_before-scrap_recovery*2)} TL geri kazanımın maliyetten iki kez düşüldüğü sonuç"],
  f"İşe izlenebilen artık geri kazanımı maliyeti azaltır: {tr(job_material_before)} − {tr(scrap_recovery)} = {tr(job_material_net)} TL.",
  "TMS 2 par. 10 ve 12 - belirli siparişe ait artık değerinin netleştirilmesi")

q("Artık malzeme işlemlerine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Belirli işe izlenen artık o işin maliyetini azaltabilir\n\nII. Ortak artık uygun GÜG havuzunu azaltabilir\n\nIII. Artık geri kazanımı üretim maliyetiyle hiçbir zaman ilişkilendirilemez",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Artık geri kazanımı kaynağına göre iş veya ortak havuzla ilişkilendirilebilir; üretim maliyetinden daima bağımsız olduğu söylenemez.",
  "TMS 2 par. 10 ve 12; 1 Sıra No.lu MSUGT - stok ve üretim maliyeti belge düzeni")

returned_material, reusable_scrap = 14_000, 6_000
gross_issue = 120_000
net_consumed = gross_issue - returned_material - reusable_scrap
assert net_consumed == 100_000
q(f"Bir işe {tr(gross_issue)} TL malzeme verilmiş; {tr(returned_material)} TL kullanılmamış malzeme depoya, {tr(reusable_scrap)} TL değerinde yeniden kullanılabilir artık da artık deposuna alınmıştır. Net tüketim kaç TL'dir?",
  f"{tr(net_consumed)} TL",
  [f"{tr(gross_issue-returned_material)} TL yeniden kullanılabilir artığın tüketimde bırakıldığı tutar",
   f"{tr(gross_issue-reusable_scrap)} TL kullanılmamış malzeme iadesinin düşülmediği tutar",
   f"{tr(gross_issue+returned_material+reusable_scrap)} TL iadelerin maliyete eklendiği sonuç",
   f"{tr(returned_material+reusable_scrap)} TL yalnız iade ve artığın net tüketim sayıldığı tutar"],
  f"Net tüketim {tr(gross_issue)} − {tr(returned_material)} − {tr(reusable_scrap)} = {tr(net_consumed)} TL'dir.",
  "1 Sıra No.lu MSUGT - 150 İlk Madde ve Malzeme ile 710 Direkt İlk Madde ve Malzeme")

needed_material, scrap_reused = 50_000, 7_500
new_requisition = needed_material - scrap_reused
assert new_requisition == 42_500
q(f"Yeni bir üretim için toplam {tr(needed_material)} TL malzeme gerekmektedir. Depodaki uygun artıkların {tr(scrap_reused)} TL'si yeniden kullanılacaktır. Yeni malzeme çıkışı kaç TL olmalıdır?",
  f"{tr(new_requisition)} TL",
  [f"{tr(needed_material)} TL yeniden kullanılan artığın ihtiyaçtan düşülmediği çıkış tutarı",
   f"{tr(needed_material+scrap_reused)} TL artık kullanımının yeni çıkışa eklendiği sonuç",
   f"{tr(scrap_reused)} TL yalnız yeniden kullanılan artığın yeni çıkış sayıldığı tutar",
   f"{tr(needed_material-scrap_reused*2)} TL artık değerinin ihtiyaçtan iki kez düşüldüğü sonuç"],
  f"Toplam ihtiyacın {tr(scrap_reused)} TL'si artıkla karşılandığından yeni çıkış {tr(needed_material)} − {tr(scrap_reused)} = {tr(new_requisition)} TL'dir.",
  "TMS 2 par. 10 - stokların üretimde kullanımı; artık malzemenin yeniden değerlendirilmesi")

q("Artık malzeme deposuna miktar girişi yapılmadan yalnız satış geliri kaydedilmesi hangi kontrol riskini artırır?",
  "Artıkların kaybolması veya yetkisiz satılması",
  ["Sağlam mamullerin otomatik olarak maddi duran varlık hesabına aktarılması riskini",
   "Bütün üretim giderlerinin finansman geliri kabul edilerek kârın azalması riskini",
   "Müşteri alacaklarının üretim miktarından bağımsız olarak tamamen kapanması riskini",
   "Direkt işçilik saatlerinin banka bakiyesiyle zorunlu olarak eşit çıkması riskini"],
  "Miktar, teslim, depolama ve satış kayıtları birbirine bağlanmazsa düşük değerli görülen artıklar üzerinde suistimal ve eksik gelir riski doğar.",
  "1 Sıra No.lu MSUGT - belgeye dayalı stok hareketleri; artık malzeme iç kontrolü")

q("Artık satış fiyatı geçici olarak yükseldiğinde teknik fire standardının da yükseltilmesi neden yanlıştır?",
  "Değer değişimi fiziksel kayıp standardını belirlemez",
  ["Artık fiyatı yükseldiğinde her üretim kaybının otomatik olarak sağlam mamule dönüşmesi nedeniyle",
   "Satış fiyatları maliyet muhasebesinde hiçbir biçimde kaydedilemediği ve yasak olduğu için",
   "Fiziksel fire standardının yalnız müşterilerin ödeme vadelerinden hesaplanması gerektiği için",
   "Yüksek artık fiyatının direkt işçilik saatlerini fiziksel olarak azaltması zorunlu olduğu için"],
  "Normal fire teknik ve verimli üretim koşullarına dayanır. Artığın piyasa değeri geri kazanımı etkiler, fiziksel kayıp standardını değil.",
  "TMS 2 par. 13 ve 16(a) - normal üretim koşulları ile geri kazanım değerinin ayrılması", "hard")

physical_input, fire_qty, spoiled_qty = 10_000, 400, 200
sound_qty = physical_input - fire_qty - spoiled_qty
assert sound_qty == 9_400
q(f"Bir sürece {tr(physical_input)} birim girmiş; {tr(fire_qty)} birim fire ve {tr(spoiled_qty)} birim fiziksel bozuk mamul belirlenmiştir. Başka stok farkı yoksa sağlam çıktı kaç birimdir?",
  f"{tr(sound_qty)} birim",
  [f"{tr(physical_input-fire_qty)} birim bozuk mamullerin sağlam çıktı içinde bırakıldığı miktar",
   f"{tr(physical_input-spoiled_qty)} birim firenin fiziksel uzlaştırmadan çıkarılmadığı miktar",
   f"{tr(fire_qty+spoiled_qty)} birim toplam kaybın sağlam çıktı sayıldığı miktar",
   f"{tr(physical_input+fire_qty+spoiled_qty)} birim kayıpların girdiye eklendiği sonuç"],
  f"Sağlam çıktı {tr(physical_input)} − {tr(fire_qty)} − {tr(spoiled_qty)} = {tr(sound_qty)} birimdir.",
  "TMS 2 par. 10 ve 12 - fiziksel üretim akışının uzlaştırılması")

normal_fire4, actual_fire4, unit_cost4 = 250, 400, 50
abnormal_fire4 = actual_fire4 - normal_fire4
abnormal_fire_cost4 = abnormal_fire4 * unit_cost4
assert (abnormal_fire4, abnormal_fire_cost4) == (150, 7_500)
q(f"Toplam {tr(actual_fire4)} birim firenin {tr(normal_fire4)} birimi normaldir. Normal üretim birim maliyeti {tr(unit_cost4)} TL ise anormal fire maliyeti kaç TL'dir?",
  f"{tr(abnormal_fire_cost4)} TL",
  [f"{tr(actual_fire4*unit_cost4)} TL normal ve anormal firenin tamamının dönem kaybı sayıldığı tutar",
   f"{tr(normal_fire4*unit_cost4)} TL yalnız normal firenin anormal kayıp kabul edildiği tutar",
   f"{tr(abnormal_fire4)} TL anormal miktarın maliyetle çarpılmadan tutar sayıldığı sonuç",
   f"{tr((actual_fire4+normal_fire4)*unit_cost4)} TL normal miktarın fiilî kayba eklendiği sonuç"],
  f"Anormal miktar {tr(actual_fire4)} − {tr(normal_fire4)} = {tr(abnormal_fire4)} birim; maliyeti {tr(abnormal_fire4)} × {tr(unit_cost4)} = {tr(abnormal_fire_cost4)} TL'dir.",
  "TMS 2 par. 16(a) - normal sınırı aşan fire maliyetinin giderleştirilmesi")

normal_bad, bad_unit_cost, bad_recovery = 200, 50, 10
normal_bad_net = normal_bad * (bad_unit_cost - bad_recovery)
assert normal_bad_net == 8_000
q(f"Normal bozuk mamul {tr(normal_bad)} birimdir. Tespit noktasındaki birim maliyet {tr(bad_unit_cost)} TL, birim geri kazanım {tr(bad_recovery)} TL ise sağlam üretimin taşıyacağı net bozulma maliyeti kaç TL'dir?",
  f"{tr(normal_bad_net)} TL",
  [f"{tr(normal_bad*bad_unit_cost)} TL geri kazanımın düşülmediği brüt bozulma maliyeti",
   f"{tr(normal_bad*bad_recovery)} TL yalnız geri kazanım tutarının bozulma maliyeti sayıldığı sonuç",
   f"{tr(normal_bad*(bad_unit_cost+bad_recovery))} TL geri kazanımın maliyete eklendiği sonuç",
   f"{tr(bad_unit_cost-bad_recovery)} TL yalnız bir bozuk birimin net maliyetinin toplam sayıldığı tutar"],
  f"Birim net kayıp {tr(bad_unit_cost)} − {tr(bad_recovery)} = {tr(bad_unit_cost-bad_recovery)} TL; {tr(normal_bad)} birim için {tr(normal_bad_net)} TL'dir.",
  "TMS 2 par. 10 ve 12 - normal bozuk mamul geri kazanımı ve sağlam çıktı maliyeti", "hard")

q("Üretim kaybı raporunda aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Girdi, sağlam çıktı ve fiziksel kayıplar uzlaştırılır\n\nII. Normal sınırı aşan tutar ayrı gösterilir\n\nIII. Geri kazanım değeri kayıp maliyetinden bağımsız bırakılmalıdır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Fiziksel akış ve normal/anormal maliyet ayrımı raporlanır. Güvenilir geri kazanım değeri net kayıp maliyetini etkiler.",
  "TMS 2 par. 10, 12 ve 16(a) - fiziksel ve maliyet akışının uzlaştırılması")

q("Aynı bölümde fire azalırken kusurlu mamul artıyorsa yalnız toplam kayıp miktarına bakmak neden yetersizdir?",
  "Kayıp türlerinin maliyet ve düzeltme etkileri farklıdır",
  ["Fire ile kusurlu mamulün her koşulda aynı fiziksel ve ekonomik niteliğe sahip olması nedeniyle",
   "Toplam kayıp miktarının muhasebede hiçbir zaman ölçülemeyen bir veri olması nedeniyle",
   "Kusurlu mamul arttığında bütün birimlerin otomatik olarak sağlam sayılması gerektiği için",
   "Fire azaldığında artık satış değerinin zorunlu olarak sıfıra düşmesi nedeniyle"],
  "Firede fiziksel miktar yok olur; kusurlu mamul ise yeniden işleme maliyeti ve başarı oranı taşır. Tür bazlı eğilim kök nedeni gösterir.",
  "TMS 2 par. 10 ve 16(a); üretim kayıplarında tür bazlı yönetim kontrolü", "hard")

q("Kayıp raporunda miktar sorumluluğu üretim bölümüne, satış değeri sorumluluğu artık satış birimine veriliyorsa hangi kontrol ilkesi güçlenir?",
  "Görev ve sorumlulukların ayrılması",
  ["Aynı kişinin üretim, depolama, satış ve tahsilatın tamamını tek başına yürütmesi ilkesi",
   "Fiziksel miktarların belgeye bağlanmadan yalnız sözlü bildirimle izlenmesi ilkesi",
   "Normal ve anormal kayıpların tek hesapta neden belirtilmeden birleştirilmesi ilkesi",
   "Artık satışlarının üretim maliyetinden bağımsız olarak hiç kaydedilmemesi ilkesi"],
  "Üretim, teslim alma, satış ve tahsilat sorumluluklarının ayrılması kayıp verisinin değiştirilmesi ve artık suistimali riskini azaltır.",
  "1 Sıra No.lu MSUGT - belge düzeni; üretim kayıpları ve artıklar için iç kontrol")


# İlk taslaktaki sistematik "doğru şık kısa" kalıbı kaldırılır. Sayısal
# sorularda işlem açıklaması şıkta değil çözümde tutulur; kavramsal sorularda
# ise seçeneklerin tümü aynı sınıflandırma veya muhasebe düzeyinde kurulur.
CHOICE_OVERRIDES = {
    1: (
        "Üretim firesi",
        ["Artık malzeme", "Kusurlu mamul", "Bozuk mamul", "Sağlam mamul"],
    ),
    2: (
        "Artık malzeme",
        ["Normal fire", "Kusurlu mamul", "Bozuk mamul", "Sağlam mamul"],
    ),
    3: (
        "Kusurlu mamul",
        ["Üretim firesi", "Bozuk mamul", "Artık malzeme", "Sağlam mamul"],
    ),
    5: (
        "Bozuk mamul",
        ["Normal fire", "Kusurlu mamul", "Artık malzeme", "Sağlam mamul"],
    ),
    6: (
        "Verimli üretimde teknik olarak kaçınılmaz olması",
        ["Kayıbın gerçekleştiği dönemde satış yapılması",
         "Kayıp karşılığında nakit tahsil edilmesi",
         "Mamulün peşin veya vadeli satılması",
         "Tedarikçinin üretim yerine yakın olması"],
    ),
    7: (
        "Oluştuğu dönemde giderleştirilir",
        ["Sağlam mamul maliyetine eklenir", "Maddi duran varlık maliyetine alınır",
         "Satış gerçekleşene kadar ertelenir", "Doğrudan özkaynakta muhasebeleştirilir"],
    ),
    8: (
        "Sağlam üretim için teknik olarak kaçınılmaz olması",
        ["Her kaybın yönetici kusurundan kaynaklanması",
         "Firenin esas satış fiyatından satılabilmesi",
         "Üretim maliyetlerinin doğrudan giderleştirilmesi",
         "Sağlam ürünün farklı bir süreçte elde edilmesi"],
    ),
    9: (
        "Stok maliyetinin gereksiz yükselmesine",
        ["Sağlam mamul maliyetinin sıfırlanmasına", "Satış hasılatının artmasına",
         "Genel üretim giderinin duran varlığa dönüşmesine",
         "Kayıp tutarının özkaynakta gelir yazılmasına"],
    ),
    10: (
        "Teknik standartlarla doğrulanmış verimli üretim verisi",
        ["En yüksek kaybın yaşandığı dönemin ham verisi",
         "Müşteri vadeleriyle satış primlerinin toplamı",
         "Bütçelenen satış fiyatından türetilen oran",
         "Banka bakiyesinin hammadde miktarına oranı"],
    ),
    11: (
        "Kayıp birimlerin daha fazla maliyet unsuru tüketmiş olabilmesi",
        ["Geç kontrol edilen birimlerin sağlam sayılması",
         "Önceki direkt maliyetlerin kayıtlardan silinmesi",
         "Kontrolün yalnız satış fiyatını belirlemesi",
         "Geç tespit edilen kaybın daima normal olması"],
    ),
    13: (
        "Neden ve koşullara göre ayrı sınıflandırılmalıdır",
        ["Miktarlar eşit olduğu için ikisi de normal sayılmalıdır",
         "Bakımsızlık kaybı satış geliri olarak yazılmalıdır",
         "İki kayıp da duran varlık maliyetine alınmalıdır",
         "Nedenleri farklı olsa da özkaynakta izlenmelidir"],
    ),
    14: (
        "Verimsizliğin normal maliyet içinde gizlenmesi",
        ["Kayıpların satış hasılatına dönüşmesi",
         "Direkt malzeme tüketiminin ortadan kalkması",
         "Stok satış değerinin garanti edilmesi",
         "Banka bakiyesinin üretim maliyetine eşitlenmesi"],
    ),
    15: (
        "Önlenebilir kaybın sorumluluk ve eğilimini görmek",
        ["Bütün kayıpları tek maliyet hesabında birleştirmek",
         "Satış biriminin tahsilat başarısını ölçmek",
         "Üretim giderlerini müşteri vadelerine göre ayırmak",
         "Kayıpları sağlam ürün olarak raporlamak"],
    ),
    16: ("800", ["19.200", "5.000", "1.600", "19.996"]),
    17: ("300", ["1.100", "800", "18.900", "19.200"]),
    18: ("18.900", ["19.200", "21.100", "1.100", "19.500"]),
    19: ("40 TL", ["38,40 TL", "960 TL", "0,03 TL", "698,18 TL"]),
    21: ("12.000 TL", ["44.000 TL", "32.000 TL", "756.000 TL", "2.560 TL"]),
    22: ("756.000 TL", ["768.000 TL", "12.000 TL", "44.000 TL", "744.000 TL"]),
    23: (
        "Toplam maliyet eksiksiz ayrıştırılmıştır",
        ["12.000 TL dağıtılmadan kalmıştır", "12.000 TL fazla dağıtılmıştır",
         "Yalnız sağlam üretim maliyeti açıklanmıştır",
         "Toplam maliyet 756.000 TL aşılmıştır"],
    ),
    24: ("40 TL", ["41,67 TL", "43,33 TL", "1,67 TL", "24 TL"]),
    25: ("468.000 TL", ["480.000 TL", "12.000 TL", "500.000 TL", "456.000 TL"]),
    27: ("300", ["600", "900", "14.400", "15.900"]),
    28: ("8.400 TL", ["25.200 TL", "16.800 TL", "428.400 TL", "403.200 TL"]),
    29: (
        "Aşımın nedenini bölüm ve süreç bazında araştırmak",
        ["Normal sınırı fiilî kayıp düzeyine yükseltmek",
         "Kayıp verisini satış performansına aktarmak",
         "Aşımı sağlam ürün stokuna eşit dağıtmak",
         "Fiziksel kayıtları uzlaştırmadan kaybı kapatmak"],
    ),
    30: (
        "Kayıp veya çıktı kaydının eksik olmasına",
        ["Bütün stokların satış fiyatının hatalı olmasına",
         "Normal fire oranının mutlaka sıfır olmasına",
         "Genel giderlerin duran varlığa aktarılmasına",
         "Maliyetin banka bakiyesinden hesaplanmasına"],
    ),
    31: (
        "Bozuk mamul",
        ["Kusurlu mamul", "Üretim firesi", "Artık malzeme", "Sağlam mamul"],
    ),
    32: (
        "İlgili siparişin maliyetine",
        ["Genel yönetim giderlerine", "Finansman giderlerine",
         "Başka bölümün GÜG havuzuna", "Müşteri alacakları hesabına"],
    ),
    33: (
        "Genel üretim gideri havuzunda",
        ["En yüksek kârlı sipariş üzerinde", "Satış ve pazarlama giderlerinde",
         "Maddi duran varlık maliyetinde", "Doğrudan özkaynak hesabında"],
    ),
    34: (
        "Anormal kayıp olarak giderleştirmek",
        ["Sağlam mamullerin maliyetine yüklemek", "Son tamamlanan siparişe yüklemek",
         "Bina maliyetine ekleyip amorti etmek", "Satışa kadar gelir hesabında bekletmek"],
    ),
    36: ("18.000 TL", ["14.000 TL", "12.000 TL", "10.000 TL", "22.000 TL"]),
    37: ("168.000 TL", ["150.000 TL", "132.000 TL", "18.000 TL", "186.000 TL"]),
    38: ("3.600 TL", ["20 TL", "133,33 TL", "20.400 TL", "216.000 TL"]),
    39: ("0 TL", ["15.000 TL", "7.500 TL", "30.000 TL", "33.000 TL"]),
    40: ("42.000 TL", ["50.000 TL", "8.000 TL", "58.000 TL", "34.000 TL"]),
    41: ("60 TL", ["71,43 TL", "11,43 TL", "52,50 TL", "0,02 TL"]),
    42: ("3.000 TL", ["3.600 TL", "600 TL", "4.200 TL", "100 TL"]),
    44: (
        "Yeniden işleme maliyetinin parçası olarak",
        ["Finansman giderinin bir parçası olarak", "Özkaynak hareketi olarak",
         "Müşteri alacağı olarak", "Hiçbir maliyet nesnesine kaydedilmeden"],
    ),
    45: (
        "Fiziksel çıktı ve birim maliyet",
        ["Ödeme vadesi ve faiz oranı", "Sermaye tutarı ve oy hakkı",
         "Satış primi ve yönetim kirası", "Tedarikçi adresi ve alış vadesi"],
    ),
    46: (
        "İlgili sipariş maliyetini azaltmak",
        ["Bütün siparişlere eşit dağıtmak", "Finansman geliri olarak kaydetmek",
         "Başka siparişin işçiliğinden düşmek", "Duran varlık maliyetine eklemek"],
    ),
    47: (
        "Ortak GÜG maliyetini azaltarak",
        ["Tek bir siparişe rastgele yazarak", "Doğrudan sermayeye ekleyerek",
         "Satış personeli ücretinden düşerek", "Hiçbir hesapta göstermeyerek"],
    ),
    48: ("20.000 TL", ["1.266 TL", "78,12 TL", "16 TL", "40.000 TL"]),
    49: ("160.000 TL", ["180.000 TL", "200.000 TL", "20.000 TL", "140.000 TL"]),
    51: ("100.000 TL", ["106.000 TL", "114.000 TL", "140.000 TL", "20.000 TL"]),
    52: ("42.500 TL", ["50.000 TL", "57.500 TL", "7.500 TL", "35.000 TL"]),
    53: (
        "Artıkların kaybolması veya yetkisiz satılması",
        ["Sağlam mamullerin duran varlığa aktarılması",
         "Üretim giderlerinin finansman geliri sayılması",
         "Müşteri alacaklarının kendiliğinden kapanması",
         "İşçilik saatlerinin banka bakiyesine eşitlenmesi"],
    ),
    54: (
        "Değer değişimi fiziksel kayıp standardını belirlemez",
        ["Fiyat artışı kaybı sağlam mamule dönüştürür",
         "Satış fiyatları maliyet kayıtlarında kullanılamaz",
         "Fire standardı müşteri vadelerinden hesaplanır",
         "Artık fiyatı işçilik saatlerini fiziksel olarak azaltır"],
    ),
    55: ("9.400", ["9.600", "9.800", "600", "10.600"]),
    56: ("7.500 TL", ["20.000 TL", "12.500 TL", "150 TL", "32.500 TL"]),
    57: ("8.000 TL", ["10.000 TL", "2.000 TL", "12.000 TL", "40 TL"]),
    59: (
        "Kayıp türlerinin maliyet ve düzeltme etkileri farklıdır",
        ["Fire ile kusurlu mamul aynı ekonomik niteliğe sahiptir",
         "Toplam kayıp miktarı hiçbir zaman ölçülemez",
         "Kusurlu mamuller otomatik olarak sağlam sayılır",
         "Fire azalınca artık satış değeri sıfırlanır"],
    ),
    60: (
        "Görev ve sorumlulukların ayrılması",
        ["Bütün işlemlerin tek kişide toplanması", "Sözlü bildirimle miktar izlenmesi",
         "Kayıpların tek hesapta birleştirilmesi", "Artık satışlarının kaydedilmemesi"],
    ),
}

STEM_OVERRIDES = {
    20: (
        "Fire miktar analizine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\n"
        "I. Beklenen sağlam miktar girdiden normal fire çıkarılarak bulunabilir\n\n"
        "II. Anormal fire fiilî kaybın normal sınırı aşan kısmıdır\n\n"
        "III. Fiilî fire normal sınırın altındaysa anormal fire oluşmaz"
    ),
    58: (
        "Üretim kaybı raporunda aşağıdaki ifadelerden hangileri doğrudur?\n\n"
        "I. Girdi, sağlam çıktı ve fiziksel kayıplar uzlaştırılır\n\n"
        "II. Normal sınırı aşan tutar ayrı gösterilir\n\n"
        "III. Güvenilir geri kazanım değeri net kayıp maliyetini etkiler"
    ),
}

PREMISE_OVERRIDES = {
    20: (
        "I, II ve III",
        ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
        "Beklenen sağlam çıktı normal kayıp sonrası miktardır; sınırı aşan kısım anormal fireyi oluşturur. Fiilî fire sınırın altındaysa anormal fire yoktur.",
    ),
    58: (
        "I, II ve III",
        ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
        "Üretim kaybı raporu fiziksel akışı ve normal/anormal ayrımını uzlaştırır; güvenilir geri kazanım değeri net kayıp maliyetini azaltır.",
    ),
}

REF_OVERRIDES = {
    1: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - fire",
    2: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - artık malzeme",
    3: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - kusurlu mamul",
    4: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - fire, artık ve kusurlu mamul ayrımı",
    5: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - bozuk mamul",
    11: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - kaybın tespit noktası ve eşdeğer üretim",
    15: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - üretim kaybı kontrolü",
    30: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - fiziksel miktar uzlaştırması",
    31: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - bozuk ve kusurlu mamul ayrımı",
    44: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - yeniden işleme ve kalite kontrol maliyeti",
    45: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - fiziksel çıktı ve birim maliyet kontrolü",
    46: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - işe özgü artık malzeme",
    47: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - ortak artık malzeme",
    48: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - artık malzeme geri kazanımı",
    49: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - artık değerinin sipariş maliyetinden indirilmesi",
    50: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - artık malzemenin maliyet etkisi",
    53: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - artık malzeme iç kontrolü",
    60: "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - üretim kayıplarında görevlerin ayrılığı",
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

for number, ref in REF_OVERRIDES.items():
    Q[number - 1]["ref"] = ref


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
