# -*- coding: utf-8 -*-
"""Yeterlilik KONU HAVUZU — Maliyet Muhasebesi / Maliyetleme Sistemleri.

60 özgün soru = 3×20. Sipariş ve safha maliyetleme uygulamaları birlikte,
ancak mevcut SGS sipariş/safha havuzlarından farklı vaka ve ölçüm düzeyinde.
Seçenekler doğal uzunlukta ve aynı kavramsal düzeydedir; çözümde harf atfı yoktur.
"""
import json
import random
import re
from pathlib import Path

L, T, LBL = "maliyet_muhasebesi", "maliyet_sistemleri", "Maliyetleme Sistemleri"
PREFIX, SEED = "kh-mal-sistem", 20260904
CONTENT_ROOT = Path(__file__).resolve().parents[3]
PROJECTS_ROOT = CONTENT_ROOT.parent
FILENAME = "questions_topic_maliyet_sistemleri_2026.json"
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


# ── A. Sistem seçimi, maliyet nesnesi ve belge akışı (15) ────────────────
q("Müşteriye özgü teknik şartnameyle üretilen endüstriyel kalıplarda her işin kaynak tüketimi ayrı izlenebiliyorsa hangi maliyetleme yaklaşımı öncelikle uygundur?",
  "Sipariş maliyetleme",
  ["Dönem üretiminin tamamını tek ortalama birim maliyetle değerlendiren safha maliyetleme yaklaşımı",
   "Yalnız satış fiyatlarını esas alıp üretim kaynaklarını maliyet nesnelerine bağlamayan yöntem",
   "Bütün özel işleri tek bir homojen üretim akışı sayarak farklılıkları dönem sonunda yok sayan yöntem",
   "Tamamlanma derecelerini her sipariş için eşdeğer birime çeviren toplu süreç maliyetleme yöntemi"],
  "Birbirinden ayırt edilebilen ve müşteri özelliklerine göre yürütülen işlerin maliyeti sipariş bazında izlenir.",
  "TMS 2 par. 10 ve 12 - dönüştürme maliyetlerinin maliyet nesnesine sistematik yüklenmesi", "easy")

q("Aynı nitelikte kimyasal ürünün kesintisiz ve birbirini izleyen reaktörlerde üretilmesinde dönem maliyetinin çıktılara yüklenmesi için hangi sistem daha uygundur?",
  "Safha maliyetleme",
  ["Her litre için bağımsız sipariş kartı açılmasını ve bütün giderlerin tek tek litreye yazılmasını gerektiren yöntem",
   "Üretim maliyetini yalnız müşterinin verdiği sipariş numarasına göre izleyen özel iş maliyetleme yöntemi",
   "Dönem sonu yarı mamulleri dikkate almadan bütün maliyeti sadece satılan ürünlere yükleyen yaklaşım",
   "Üretim sürecindeki maliyetleri stok dışında bırakıp doğrudan dönem gideri kabul eden uygulama"],
  "Homojen ürünün sürekli ve aşamalı üretiminde maliyetler safhalarda toplanır ve eşdeğer üretime göre ortalanır.",
  "TMS 2 par. 12 - sistematik üretim maliyeti dağıtımı; maliyet muhasebesi - safha sistemi", "easy")

q("Sipariş maliyetlemede bir özel üretimin direkt malzeme, direkt işçilik ve yüklenen genel üretim giderlerini bir araya getiren temel maliyet nesnesi hangisidir?",
  "Belirli sipariş veya üretim partisi",
  ["İşletmenin aynı dönemde tamamladığı bütün mamullerin satış değeri toplamı ve brüt kâr yüzdesi",
   "Fabrikanın tüm üretim bölümlerinde oluşan giderlerin tek bir dönemsel toplamı ve bütçe farkı",
   "Yalnız kullanılan hammaddenin satın alındığı tedarikçi ve ödeme vadesine göre oluşan grup",
   "Dönem sonunda henüz satılmamış bütün stokların tek kalemde birleştirildiği finansal tablo hesabı"],
  "Sipariş sisteminde maliyet nesnesi, diğer işlerden ayırt edilebilen belirli sipariş veya üretim partisidir.",
  "TMS 2 par. 10 ve 12 - stok maliyetinin üretimle ilişkilendirilmesi")

q("Maliyetleme sistemlerine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Sipariş sisteminde maliyetler ayırt edilebilir işler itibarıyla toplanır\n\nII. Safha sisteminde dönem sonu yarı mamuller eşdeğer üretimle ölçülebilir\n\nIII. Safha sisteminde her müşteri için zorunlu olarak ayrı maliyet kartı açılır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Sipariş sistemi işi, safha sistemi ise homojen süreç çıktısını maliyet nesnesi yapar. Safha sisteminde müşteri bazlı kart zorunlu değildir.",
  "TMS 2 par. 12 - sistematik dağıtım; maliyet muhasebesi - sipariş ve safha sistemleri")

q("Bir ayakkabı işletmesinde taban hazırlama tüm modeller için ortak ve sürekli, son montaj ise model partileri itibarıyla izleniyorsa hangi yaklaşım bilgi ihtiyacını daha iyi karşılar?",
  "Karma maliyetleme",
  ["Bütün üretim özelliklerini yok sayarak yalnız tek bir safha ortalaması hesaplayan saf süreç yöntemi",
   "Ortak işlemleri görmezden gelip her bir ayakkabı teki için bağımsız sipariş kartı açan yöntem",
   "Üretim giderlerini modele veya sürece bağlamadan yalnız satış bölümünde toplayan dönemsel yaklaşım",
   "Direkt maliyetleri stoklara almadan bütün üretim giderlerini gerçekleştiği anda sonuç hesabına aktaran yöntem"],
  "Ortak süreç maliyetlerinin ortalama, modele özgü maliyetlerin parti bazında izlendiği karma yaklaşım bu üretim yapısına uygundur.",
  "TMS 2 par. 10 ve 12 - üretim koşullarına uygun maliyet ölçümü", "hard")

q("Birbirinden ayrı yürütülen özel üretim işlerini karşılaştırmak isteyen yönetici, sipariş maliyet kartından öncelikle hangi bilgiyi elde eder?",
  "İşe yüklenen maliyetleri tek kayıtta toplamak",
  ["İşletmenin bütün dönem satışlarını müşteri vadelerine göre sınıflandırıp tahsilat planı oluşturmak",
   "Safha sonundaki tüm yarı mamulleri tamamlanma derecesinden bağımsız biçimde mamul kabul etmek",
   "Fabrikanın finansman giderlerini üretim siparişlerine hiçbir ölçü kullanmadan eşit dağıtmak",
   "Yalnız genel yönetim giderlerini ürün satış fiyatlarına göre bölüştürüp stoklara aktarmak"],
  "Maliyet kartı, belirli işe ait direkt malzeme, direkt işçilik ve yüklenen genel üretim giderlerini izlenebilir biçimde birleştirir.",
  "1 Sıra No.lu MSUGT - 151, 710, 720 ve 730 hesapları; sipariş maliyet kartı")

q("Safha üretim raporunda fiziksel miktar akışıyla maliyet akışının birlikte uzlaştırılmasının temel amacı nedir?",
  "Birimleri ve maliyetleri eksiksiz hesap vermek",
  ["Satış fiyatı değişimlerini üretim miktarından bağımsız olarak dönem kârına doğrudan aktarmak",
   "Dönem sonu yarı mamulleri tamamlanmış birim sayıp eşdeğer üretim hesabını tamamen kaldırmak",
   "Direkt malzeme ile dönüştürme maliyetlerini aynı tamamlanma derecesinde varsaymayı zorunlu kılmak",
   "Önceki safhadan devralınan maliyeti ikinci safhada oluşan maliyetlerden kalıcı olarak dışlamak"],
  "Üretime giren ve çıkan fiziksel birimler ile dağıtılacak ve dağıtılan maliyetlerin eşitliği raporun kontrol temelidir.",
  "TMS 2 par. 10 ve 12 - stok maliyetinin güvenilir ölçümü; safha maliyet raporu")

q("Üretimde kullanılan direkt maliyetler önce yarı mamul hesabında toplanmış, iş tamamlanınca mamullere, satış gerçekleşince satılan mamul maliyetine aktarılmıştır. Bu sıra neyi gösterir?",
  "Stok maliyetinin üretim ve satış akışını",
  ["Üretim giderlerinin oluştuğu anda tamamının finansman gideri sayılarak sonuç hesabına aktarılmasını",
   "Mamul tamamlanmadan bütün maliyetlerin satış hasılatıyla netleştirilip kayıtlardan çıkarılmasını",
   "Genel yönetim giderlerinin önce yarı mamule sonra mamule yüklenmesini zorunlu kılan bir akışı",
   "Sipariş veya safha ayrımı yapılmaksızın bütün üretim maliyetlerinin yalnız kasa hesabında izlenmesini"],
  "Üretim maliyeti devam eden işte 151, tamamlanınca 152, satılınca 620 hesabına akar.",
  "1 Sıra No.lu MSUGT - 151 Yarı Mamuller, 152 Mamuller ve 620 Satılan Mamuller Maliyeti")

q("İki ardışık safhalı üretimde birinci safhada tamamlanan birimlerin maliyeti ikinci safhada nasıl ele alınır?",
  "Devralınan maliyet olarak ikinci safhaya taşınır",
  ["Birinci safha tamamlandığı anda üretimle ilişkisi kesilerek genel yönetim gideri olarak kaydedilir",
   "İkinci safhanın yalnız direkt işçilik maliyetinden düşülerek net işçilik tutarı olarak raporlanır",
   "Satış gerçekleşmediği hâlde doğrudan satılan mamul maliyetine aktarılıp stok dışında bırakılır",
   "İkinci safhadaki birimlerden bağımsız biçimde finansman maliyeti olarak dönem sonucuna yüklenir"],
  "Önceki safhanın çıktısı sonraki safhanın girdisidir; birikmiş maliyet devralınan maliyet olarak süreci izler.",
  "TMS 2 par. 10 ve 12 - dönüştürme maliyetleri; çok safhalı maliyet akışı")

q("Homojen süreçte her bir birime fiilen harcanan işçilik süresini tek tek ölçmek ekonomik değilse safha sisteminin ortalama maliyet kullanması hangi gerekçeye dayanır?",
  "Benzer birimlerin ortak kaynak tüketimine",
  ["Üretim maliyetlerinin güvenilir ölçülememesi nedeniyle tamamının stoklardan çıkarılması gereğine",
   "Her birimin farklı müşteri talebine göre üretildiği ve ayrı fiyatlandırılması zorunluluğuna",
   "Direkt işçiliğin üretim maliyetine hiçbir koşulda alınamayarak dönem gideri yazılması ilkesine",
   "Dönem başı ve dönem sonu yarı mamullerin her zaman aynı fiziksel miktarda olması varsayımına"],
  "Birbirine benzer birimlerin aynı süreç kaynaklarını tüketmesi, safha maliyetlerinin eşdeğer birimler üzerinden ortalanmasını anlamlı kılar.",
  "TMS 2 par. 12 - sistematik ve tutarlı maliyet dağıtımı")

q("Aynı özellikte 500 parçadan oluşan tek bir müşteri partisi diğer partilerden ayrı izlenebiliyorsa maliyet kartı hangi düzeyde açılabilir?",
  "Parti düzeyinde",
  ["Her parçanın satılacağı tarihteki piyasa değeri düzeyinde ayrı finansal yatırım hesabı olarak",
   "İşletmenin bütün müşterilerini kapsayan yıllık satış hacmi düzeyinde tek bir toplu kart olarak",
   "Yalnız hammaddenin satın alındığı tedarikçi düzeyinde ve üretimden bağımsız bir kart olarak",
   "Fabrikanın bütün bölümlerini kapsayan genel yönetim gideri düzeyinde tek bir dönem kartı olarak"],
  "Aynı siparişe ait homojen parçalar tek üretim partisi olarak maliyet nesnesi yapılabilir; her parçaya ayrı kart gerekmez.",
  "TMS 2 par. 23 - özel projeler için maliyetlerin ayrı belirlenmesi; sipariş maliyetleme")

q("Sipariş sistemindeki belge akışına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Malzeme istek fişi kullanılan direkt malzemeyi işe bağlayabilir\n\nII. İşçi çalışma kartı direkt işçilik süresini işe bağlayabilir\n\nIII. Faaliyet ölçüsü genel üretim giderinin işe yüklenmesinde kullanılabilir",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Üç belge/veri de sipariş kartındaki maliyetlerin kaynağını ve yükleme temelini oluşturur.",
  "1 Sıra No.lu MSUGT - 710, 720 ve 730 hesapları; sipariş maliyet belgeleri")

q("Bir süreçte aynı makineler kullanılsa da ürünler yüksek ölçüde müşteri tasarımına göre farklılaşıyor ve malzeme tüketimi iş bazında ölçülebiliyorsa sistem seçiminde hangi özellik ağır basar?",
  "İşlerin ayırt edilebilir olması",
  ["Fabrikadaki makinelerin aynı renkte ve aynı ekonomik ömürde bulunması koşulu",
   "Ürünlerin satış vadelerinin aynı ay içinde sona ermesi ve müşterilerin benzer olması",
   "Dönem sonunda bütün siparişlerin mutlaka aynı günde tamamlanmış olması varsayımı",
   "İşletmenin yalnız tek bir üretim bölümüne sahip olması ve hiç yardımcı bölüm bulunmaması"],
  "Sistem seçiminin belirleyicisi fiziksel makine benzerliği değil, maliyet nesnelerinin ayırt edilebilirliği ve kaynakların ölçülebilmesidir.",
  "TMS 2 par. 10 ve 12 - stok maliyetinin üretim koşullarına uygun belirlenmesi", "hard")

q("Kesim bölümü makine yoğun, montaj bölümü emek yoğunken iki bölüm için ayrı genel üretim gideri oranı kullanılması ne sağlar?",
  "Bölümlerin farklı kaynak tüketimini yansıtır",
  ["Direkt malzeme ve direkt işçilik giderlerinin üretim maliyetinden tamamen çıkarılmasını sağlar",
   "Her siparişe kullanılan faaliyet miktarından bağımsız olarak aynı genel üretim giderini yükler",
   "Dönem sonu yarı mamullerin tamamlanma derecelerini ölçme ihtiyacını bütünüyle ortadan kaldırır",
   "Üretim maliyetlerini satış fiyatı yüksek olan siparişlerde otomatik olarak daha düşük gösterir"],
  "Bölüm oranları, siparişin makine ve işçilik faaliyetlerinden fiilen yararlanma biçimini ayrı ayrı maliyete dönüştürür.",
  "TMS 2 par. 12 - genel üretim giderlerinin sistematik dağıtımı")

q("Maliyetleme sisteminin yalnız sektör adına bakılarak seçilmesi yerine üretim akışının incelenmesi neden gereklidir?",
  "Aynı işletmede farklı üretim yapıları bulunabilir",
  ["Sektör bilgisi maliyet muhasebesinde hiçbir durumda kullanılamayan ve kayda alınması yasak bir veri olduğu için",
   "Bütün sektörlerde yalnız sipariş maliyetleme kullanılmasının finansal raporlama açısından zorunlu olması nedeniyle",
   "Safha maliyetlemenin yalnız hizmet işletmelerine, sipariş maliyetlemenin yalnız ticaret işletmelerine özgü olması nedeniyle",
   "Üretim akışının maliyet nesnesi ve kaynak tüketimi üzerinde herhangi bir etkisi bulunmadığı için"],
  "Aynı işletme sürekli ortak süreçler ile müşteriye özgü son işlemleri birlikte yürütebilir; seçim gerçek üretim ve ölçüm yapısına dayanmalıdır.",
  "TMS 2 par. 10 ve 12 - maliyetlerin koşullara uygun ve sistematik ölçümü", "hard")


# ── B. Sipariş maliyetleme — ileri uygulamalar (20) ──────────────────────
kesim_havuz, kesim_saat = 600_000, 30_000
montaj_havuz, montaj_saat = 360_000, 18_000
kesim_oran, montaj_oran = kesim_havuz / kesim_saat, montaj_havuz / montaj_saat
assert (kesim_oran, montaj_oran) == (20, 20)
q(f"İşletme Makine İşleme bölümü için {tr(kesim_havuz)} TL/{tr(kesim_saat)} makine saati, Son Montaj için {tr(montaj_havuz)} TL/{tr(montaj_saat)} işçilik saati bütçelemiştir. Her bölümde tek faaliyet birimine düşen GÜG çifti nedir?",
  f"{tr(kesim_oran)} TL/makine saati ve {tr(montaj_oran)} TL/işçilik saati",
  [f"{tr(kesim_havuz/montaj_saat)} TL/makine saati ve {tr(montaj_havuz/kesim_saat)} TL/işçilik saati",
   f"{tr((kesim_havuz+montaj_havuz)/(kesim_saat+montaj_saat))} TL olarak iki bölüme tek oran uygulanması",
   f"{tr(kesim_havuz/kesim_saat+montaj_havuz/montaj_saat)} TL/makine saati ve aynı tutarda işçilik saati",
   f"{tr(kesim_saat/kesim_havuz)} TL/makine saati ile {tr(montaj_saat/montaj_havuz)} TL/işçilik saati"],
  f"Kesim oranı {tr(kesim_havuz)} / {tr(kesim_saat)} = {tr(kesim_oran)}; Montaj oranı {tr(montaj_havuz)} / {tr(montaj_saat)} = {tr(montaj_oran)} TL'dir.",
  "TMS 2 par. 12 - bölüm bazında sistematik GÜG dağıtımı")

a_mh, a_lh = 450, 300
a_oh = a_mh * kesim_oran + a_lh * montaj_oran
assert a_oh == 15_000
q(f"A-17 iş kartında Makine İşleme için {tr(a_mh)} saat × {tr(kesim_oran)} TL; Son Montaj için {tr(a_lh)} saat × {tr(montaj_oran)} TL tüketim kaydı vardır. İki bölümden bu işe aktarılan GÜG toplamı nedir?",
  f"{tr(a_oh)} TL",
  [f"{tr(a_mh*kesim_oran)} TL yalnız Kesim bölümünün faaliyetini dikkate alan tutar",
   f"{tr(a_lh*montaj_oran)} TL yalnız Montaj bölümünün faaliyetini dikkate alan tutar",
   f"{tr((a_mh+a_lh)*(kesim_oran+montaj_oran))} TL iki faaliyet ile iki oranın çapraz çarpıldığı tutar",
   f"{tr((a_mh+a_lh)*kesim_oran/2)} TL toplam faaliyetin iki bölüme eşit paylaştırıldığı tutar"],
  f"Kesim payı {tr(a_mh)} × {tr(kesim_oran)} = {tr(a_mh*kesim_oran)} TL; Montaj payı {tr(a_lh)} × {tr(montaj_oran)} = {tr(a_lh*montaj_oran)} TL'dir. Toplam {tr(a_oh)} TL olur.",
  "TMS 2 par. 12 - siparişe bölüm faaliyetleriyle GÜG yüklenmesi")

a_dm, a_dl = 85_000, 42_000
a_total = a_dm + a_dl + a_oh
assert a_total == 142_000
q(f"A-17 maliyet kartının üç satırı {tr(a_dm)} TL doğrudan malzeme, {tr(a_dl)} TL doğrudan emek ve {tr(a_oh)} TL faaliyet oranlarıyla aktarılan fabrika gideridir. Kartın kapanış maliyeti nedir?",
  f"{tr(a_total)} TL",
  [f"{tr(a_dm+a_dl)} TL yalnız direkt maliyetlerin dikkate alındığı üretim maliyeti",
   f"{tr(a_dm+a_oh)} TL direkt işçiliğin maliyet dışında bırakıldığı toplam tutar",
   f"{tr(a_dl+a_oh)} TL direkt malzemenin maliyet dışında bırakıldığı toplam tutar",
   f"{tr(a_dm+a_dl-a_oh)} TL yüklenen genel üretim giderinin direkt maliyetlerden düşüldüğü tutar"],
  f"Toplam sipariş maliyeti {tr(a_dm)} + {tr(a_dl)} + {tr(a_oh)} = {tr(a_total)} TL'dir.",
  "TMS 2 par. 10 ve 12 - satın alma ve dönüştürme maliyetleri")

a_units = 400
a_unit = a_total / a_units
assert a_unit == 355
q(f"Toplam üretim maliyeti {tr(a_total)} TL olan A-17 siparişinde kalite kontrolünden geçen {tr(a_units)} mamul elde edilmiştir. Siparişin mamul başına maliyeti kaç TL'dir?",
  f"{tr(a_unit)} TL",
  [f"{tr(a_total/(a_units+100))} TL tamamlanmayan ilave birimlerin paydaya katıldığı sonuç",
   f"{tr((a_dm+a_dl)/a_units)} TL genel üretim giderinin birim maliyetten çıkarıldığı sonuç",
   f"{tr(a_total/(a_units-100))} TL yalnız satılacağı varsayılan birimlerin paydaya alındığı sonuç",
   f"{tr(a_total/a_units+a_oh/a_units)} TL yüklenen genel üretim giderinin ikinci kez eklendiği sonuç"],
  f"Birim maliyet {tr(a_total)} / {tr(a_units)} = {tr(a_unit)} TL'dir.",
  "TMS 2 par. 10 - üretim maliyetinin mamul birimlerine yüklenmesi")

q("Normal maliyetleme ile yürütülen sipariş sistemine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Direkt malzeme siparişe fiilî tutarıyla yüklenebilir\n\nII. Genel üretim gideri önceden belirlenen oranla yüklenebilir\n\nIII. Dönem içindeki fiilî GÜG her siparişe kesinlikle doğrudan izlenir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Normal maliyetlemede direkt maliyetler fiilî, genel üretim giderleri önceden belirlenmiş oranla yüklenebilir. Fiilî GÜG'ün tamamı siparişlere doğrudan izlenmez.",
  "TMS 2 par. 12 ve 13 - genel üretim giderlerinin sistematik yüklenmesi")

j1, j2 = 62_000, 48_000
wip = j1 + j2
assert wip == 110_000
q(f"Dönem sonunda tamamlanmamış J-21 ve J-22 sipariş kartlarında sırasıyla {tr(j1)} ve {tr(j2)} TL birikmiştir. Başka devam eden iş yoksa 151 Yarı Mamuller bakiyesi kaç TL olmalıdır?",
  f"{tr(wip)} TL",
  [f"{tr(j1)} TL yalnız yüksek maliyetli siparişin yarı mamul kabul edildiği bakiye",
   f"{tr(j2)} TL yalnız düşük maliyetli siparişin yarı mamul kabul edildiği bakiye",
   f"{tr(abs(j1-j2))} TL iki sipariş maliyeti arasındaki farkın stok sayıldığı bakiye",
   f"{tr(wip*2)} TL sipariş maliyetlerinin yansıtma hesabıyla ikinci kez toplandığı bakiye"],
  f"Tamamlanmamış işlerin kart toplamı {tr(j1)} + {tr(j2)} = {tr(wip)} TL'dir ve 151 hesabında izlenir.",
  "1 Sıra No.lu MSUGT - 151 Yarı Mamuller-Üretim")

j3, j4 = 132_000, 96_000
fg_add = j3 + j4
assert fg_add == 228_000
q(f"J-23 ve J-24 siparişleri dönemde tamamlanmış; kart maliyetleri {tr(j3)} ve {tr(j4)} TL'dir. Satış yapılmadan önce 152 Mamuller hesabına aktarılacak toplam kaç TL'dir?",
  f"{tr(fg_add)} TL",
  [f"{tr(j3)} TL yalnız ilk tamamlanan siparişin mamul hesabına aktarıldığı tutar",
   f"{tr(j4)} TL yalnız son tamamlanan siparişin mamul hesabına aktarıldığı tutar",
   f"{tr(abs(j3-j4))} TL sipariş kartları arasındaki farkın mamul maliyeti sayıldığı tutar",
   f"{tr(fg_add*2)} TL tamamlanan maliyetlerin hem yarı mamul hem mamulde bırakıldığı tutar"],
  f"Tamamlanan sipariş maliyetleri {tr(j3)} + {tr(j4)} = {tr(fg_add)} TL olarak 152 hesabına aktarılır.",
  "1 Sıra No.lu MSUGT - 151 ve 152 hesapları arasındaki tamamlanma aktarımı")

lot_cost, sold_share = 160_000, 0.75
cogs = lot_cost * sold_share
assert cogs == 120_000
q(f"Maliyeti {tr(lot_cost)} TL olan tamamlanmış bir sipariş partisinin %{int(sold_share*100)}'i satılmıştır. Birimlerin maliyeti eşitse satılan kısma aktarılacak maliyet kaç TL'dir?",
  f"{tr(cogs)} TL",
  [f"{tr(lot_cost-cogs)} TL yalnız stokta kalan kısmın maliyetinin satışa aktarıldığı tutar",
   f"{tr(lot_cost)} TL partinin satılmayan kısmı da satılmış kabul edilerek aktarılan tutar",
   f"{tr(lot_cost*(1+sold_share))} TL satış oranının maliyete ilave edildiği hesaplama sonucu",
   f"{tr(lot_cost/sold_share)} TL toplam maliyetin satış oranına bölünmesiyle bulunan tutar"],
  f"Satılan kısmın maliyeti {tr(lot_cost)} × %{int(sold_share*100)} = {tr(cogs)} TL'dir.",
  "1 Sıra No.lu MSUGT - 152 Mamuller ve 620 Satılan Mamuller Maliyeti")

dm, dl, oh = 72_000, 48_000, 36_000
prime, conversion = dm + dl, dl + oh
assert (prime, conversion) == (120_000, 84_000)
q(f"Bir siparişte direkt malzeme {tr(dm)} TL, direkt işçilik {tr(dl)} TL ve yüklenen GÜG {tr(oh)} TL'dir. Birincil maliyet ile dönüştürme maliyeti sırasıyla kaç TL'dir?",
  f"{tr(prime)} TL ve {tr(conversion)} TL",
  [f"{tr(dm+oh)} TL ve {tr(dl)} TL genel üretim giderinin birincil maliyete eklendiği sonuç",
   f"{tr(conversion)} TL ve {tr(prime)} TL iki maliyet kavramının yer değiştirdiği sonuç",
   f"{tr(dm+dl+oh)} TL ve {tr(dl)} TL toplam üretim maliyetinin birincil maliyet sayıldığı sonuç",
   f"{tr(dm)} TL ve {tr(dl+oh+dm)} TL direkt malzemenin yalnız dönüştürme maliyetine alındığı sonuç"],
  f"Birincil maliyet {tr(dm)} + {tr(dl)} = {tr(prime)} TL; dönüştürme maliyeti {tr(dl)} + {tr(oh)} = {tr(conversion)} TL'dir.",
  "TMS 2 par. 10 ve 12 - satın alma ve dönüştürme maliyetleri")

budget_oh, budget_mh, job_mh = 960_000, 48_000, 1_400
rate = budget_oh / budget_mh
job_oh = rate * job_mh
assert (rate, job_oh) == (20, 28_000)
q(f"Bütçelenen GÜG {tr(budget_oh)} TL ve bütçelenen makine saati {tr(budget_mh)} olan işletmede J-30 siparişi {tr(job_mh)} saat kullanmıştır. Önceden belirlenen oranla siparişe yüklenecek GÜG kaç TL'dir?",
  f"{tr(job_oh)} TL",
  [f"{tr(rate)} TL yalnız bir makine saatinin maliyetinin sipariş toplamı sayıldığı tutar",
   f"{tr(budget_oh/job_mh)} TL bütçelenen giderin yalnız sipariş saatine bölündüğü tutar",
   f"{tr(budget_oh*job_mh/budget_mh+rate)} TL yükleme oranının ayrıca ikinci kez eklendiği tutar",
   f"{tr(budget_oh-budget_mh*rate)} TL bütçe havuzundan toplam yüklemenin çıkarıldığı tutar"],
  f"Yükleme oranı {tr(budget_oh)} / {tr(budget_mh)} = {tr(rate)} TL/saattir. J-30 payı {tr(job_mh)} × {tr(rate)} = {tr(job_oh)} TL olur.",
  "TMS 2 par. 12 ve 13 - önceden belirlenen normal kapasite esaslı GÜG oranı")

actual_oh, actual_mh = 1_050_000, 52_000
applied_oh = actual_mh * rate
under = actual_oh - applied_oh
assert (applied_oh, under) == (1_040_000, 10_000)
q(f"Yükleme oranı {tr(rate)} TL/makine saati, fiilî faaliyet {tr(actual_mh)} saat ve fiilî GÜG {tr(actual_oh)} TL'dir. Dönem sonu yükleme farkı nedir?",
  f"{tr(under)} TL eksik yükleme",
  [f"{tr(under)} TL fazla yükleme; yüklenen gider fiilî giderden yüksek kabul edilir",
   f"{tr(applied_oh)} TL eksik yükleme; dönemde yüklenen giderin tamamı fark sayılır",
   f"{tr(actual_oh)} TL fazla yükleme; fiilî giderin tamamı sipariş maliyetinden çıkarılır",
   f"{tr(actual_oh+applied_oh)} TL eksik yükleme; fiilî ve yüklenen giderler toplanır"],
  f"Yüklenen GÜG {tr(actual_mh)} × {tr(rate)} = {tr(applied_oh)} TL'dir. Fiilî gider {tr(under)} TL daha yüksek olduğundan eksik yükleme vardır.",
  "TMS 2 par. 12 ve 13 - fiilî GÜG ile sistematik yükleme tutarının uzlaştırılması", "hard")

diff = 30_000
base_wip, base_fg, base_cogs = 150_000, 250_000, 600_000
base_total = base_wip + base_fg + base_cogs
cogs_diff = diff * base_cogs / base_total
assert base_total == 1_000_000 and cogs_diff == 18_000
q(f"{tr(diff)} TL eksik yükleme; 151, 152 ve 620 hesaplarındaki yüklenen GÜG bakiyeleri sırasıyla {tr(base_wip)}, {tr(base_fg)} ve {tr(base_cogs)} TL'dir. Fark oransal dağıtılırsa 620 hesabının payı kaç TL'dir?",
  f"{tr(cogs_diff)} TL",
  [f"{tr(diff/3)} TL farkın üç hesaba bakiye büyüklüğünden bağımsız eşit dağıtıldığı tutar",
   f"{tr(diff*base_wip/base_total)} TL yarı mamul oranının satılan mamule uygulandığı tutar",
   f"{tr(diff*base_fg/base_total)} TL mamul stoku oranının satılan mamule uygulandığı tutar",
   f"{tr(diff*base_cogs/(base_wip+base_fg))} TL paydanın satılan mamul bakiyesini dışladığı tutar"],
  f"Toplam dağıtım bazı {tr(base_total)} TL'dir. 620 payı {tr(diff)} × {tr(base_cogs)} / {tr(base_total)} = {tr(cogs_diff)} TL olur.",
  "TMS 2 par. 12 ve 13 - yükleme farkının stoklar ve satış maliyetiyle uzlaştırılması", "hard")

q("Bölüm oranlarıyla sipariş maliyetlemeye ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Makine yoğun bölümde makine saati uygun bir etken olabilir\n\nII. Emek yoğun bölümde direkt işçilik saati uygun bir etken olabilir\n\nIII. Bütün bölümlerde tek oran kullanmak her koşulda daha güvenilir sonuç verir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Faaliyet yapısına uygun bölüm etkenleri maliyet tüketimini yansıtabilir. Tek oranın her koşulda üstünlüğü yoktur.",
  "TMS 2 par. 12 - genel üretim giderlerinin sistematik ve uygun etkenlerle dağıtımı")

issued, returned, indirect = 90_000, 12_000, 8_000
direct_used = issued - returned
assert direct_used == 78_000
q(f"Bir işe {tr(issued)} TL malzeme verilmiş, kullanılmayan {tr(returned)} TL depoya iade edilmiştir. Ayrıca {tr(indirect)} TL endirekt malzeme bölüm için tüketilmiştir. Sipariş kartına yazılacak direkt malzeme kaç TL'dir?",
  f"{tr(direct_used)} TL",
  [f"{tr(issued)} TL depoya iade edilen malzemenin de siparişte tüketilmiş sayıldığı tutar",
   f"{tr(issued+indirect)} TL bölümün endirekt malzemesinin siparişe doğrudan eklendiği tutar",
   f"{tr(direct_used+indirect)} TL direkt ve endirekt tüketimin aynı sipariş kartında birleştirildiği tutar",
   f"{tr(returned+indirect)} TL yalnız iade ile endirekt malzemenin maliyet kabul edildiği tutar"],
  f"Siparişin direkt tüketimi verilen malzemeden iade çıkarılarak {tr(issued)} − {tr(returned)} = {tr(direct_used)} TL bulunur. Endirekt malzeme GÜG havuzuna gider.",
  "1 Sıra No.lu MSUGT - 710 Direkt İlk Madde ve Malzeme ile 730 Genel Üretim Giderleri")

direct_hours, idle_hours, wage = 120, 10, 320
direct_labor, idle_cost = direct_hours * wage, idle_hours * wage
assert (direct_labor, idle_cost) == (38_400, 3_200)
q(f"Bir işçi J-40 siparişinde {tr(direct_hours)} saat çalışmış, ayrıca üretim kesintisi nedeniyle {tr(idle_hours)} saat boş kalmıştır. Saat ücreti {tr(wage)} TL ise siparişe direkt işçilik olarak kaç TL yazılır?",
  f"{tr(direct_labor)} TL",
  [f"{tr((direct_hours+idle_hours)*wage)} TL boş zamanın da siparişe doğrudan yüklendiği toplam ücret",
   f"{tr(idle_cost)} TL yalnız üretim kesintisindeki boş zamanın direkt işçilik sayıldığı tutar",
   f"{tr((direct_hours-idle_hours)*wage)} TL boş zaman süresinin çalışılan süreden ikinci kez düşüldüğü tutar",
   f"{tr(direct_labor+idle_cost*2)} TL boş zaman maliyetinin siparişe iki defa eklendiği tutar"],
  f"Siparişe doğrudan izlenen süre {tr(direct_hours)} saattir; {tr(direct_hours)} × {tr(wage)} = {tr(direct_labor)} TL yazılır. Boş zaman uygun GÜG değerlendirmesine tabidir.",
  "1 Sıra No.lu MSUGT - 720 Direkt İşçilik ve 730 Genel Üretim Giderleri")

q("Tamamlanan bir sipariş henüz satılmamışsa maliyet akışında hangi işlem yapılmalıdır?",
  "151'den 152 Mamuller hesabına aktarılmalıdır",
  ["Sipariş satılmadığı için 151 Yarı Mamuller hesabında süresiz olarak bırakılmalıdır",
   "Satış gerçekleşmemiş olsa da maliyet doğrudan 620 Satılan Mamuller Maliyetine aktarılmalıdır",
   "Tamamlanan maliyet üretimle ilişkisini kaybettiği için genel yönetim gideri yazılmalıdır",
   "Müşteriden tahsilat yapılıncaya kadar maliyet 120 Alıcılar hesabında izlenmelidir"],
  "Üretimi tamamlanan fakat satılmayan sipariş yarı mamul değil mamuldür; maliyeti 152 hesabında stoklanır.",
  "1 Sıra No.lu MSUGT - 151 Yarı Mamuller ve 152 Mamuller")

d1_rate, d2_rate = 30, 18
j_mh, j_lh = 300, 400
j_dept_oh = d1_rate*j_mh + d2_rate*j_lh
assert j_dept_oh == 16_200
q(f"J-50 siparişi D1'de {tr(j_mh)} makine saati, D2'de {tr(j_lh)} işçilik saati kullanmıştır. D1 oranı {tr(d1_rate)} TL/makine saati, D2 oranı {tr(d2_rate)} TL/işçilik saati ise toplam GÜG payı kaç TL'dir?",
  f"{tr(j_dept_oh)} TL",
  [f"{tr(d1_rate*(j_mh+j_lh))} TL iki bölümün de yalnız makine saati oranıyla değerlendirildiği tutar",
   f"{tr(d2_rate*(j_mh+j_lh))} TL iki bölümün de yalnız işçilik saati oranıyla değerlendirildiği tutar",
   f"{tr((d1_rate+d2_rate)*(j_mh+j_lh))} TL bütün oran ve faaliyetlerin çapraz çarpıldığı tutar",
   f"{tr(d1_rate*j_mh)} TL ikinci bölümde kullanılan işçilik saatlerinin tamamen dışlandığı tutar"],
  f"D1 payı {tr(j_mh)} × {tr(d1_rate)} = {tr(d1_rate*j_mh)} TL; D2 payı {tr(j_lh)} × {tr(d2_rate)} = {tr(d2_rate*j_lh)} TL'dir. Toplam {tr(j_dept_oh)} TL olur.",
  "TMS 2 par. 12 - bölüm oranlarıyla siparişe GÜG yüklenmesi")

revenue, job_cost = 250_000, 185_000
job_profit = revenue - job_cost
assert job_profit == 65_000
q(f"Bir özel siparişin satış hasılatı {tr(revenue)} TL, sipariş maliyet kartındaki üretim maliyeti {tr(job_cost)} TL'dir. Siparişin üretim maliyeti üzerinden brüt sonucu kaç TL'dir?",
  f"{tr(job_profit)} TL kâr",
  [f"{tr(job_cost)} TL kâr; üretim maliyetinin tamamı dönem sonucu kabul edilir",
   f"{tr(revenue)} TL kâr; satış hasılatından üretim maliyeti düşülmeden sonuç bulunur",
   f"{tr(revenue+job_cost)} TL kâr; hasılat ile üretim maliyeti toplanarak sonuç hesaplanır",
   f"{tr(job_cost-revenue)} TL kâr; maliyetten hasılat çıkarılıp negatif işaret göz ardı edilir"],
  f"Siparişin brüt sonucu {tr(revenue)} − {tr(job_cost)} = {tr(job_profit)} TL kârdır.",
  "1 Sıra No.lu MSUGT - 600 Yurtiçi Satışlar ve 620 Satılan Mamuller Maliyeti")

q("Ortak standart işlemlerden geçen fakat modele özgü direkt malzemeler kullanan seri üretimde işlem maliyetleme yaklaşımı nasıl uygulanır?",
  "Ortak işlem maliyetleri ortalanır, özgü malzeme modele yüklenir",
  ["Bütün ortak ve modele özgü maliyetler yalnız satış fiyatı oranında müşterilere dağıtılır",
   "Modele özgü direkt malzemeler de hiçbir izleme yapılmadan bütün ürünlere eşit ortalanır",
   "Ortak işlem maliyetleri stok dışında bırakılır, yalnız direkt malzeme üretim maliyeti sayılır",
   "Her ürün birimi için tüm fabrika giderlerini kapsayan bağımsız sipariş kartı açılması zorunludur"],
  "İşlem maliyetleme, ortak süreç maliyetlerinin ortalanmasını ve ayırt edilebilir maliyetlerin ürün/model bazında izlenmesini birleştirir.",
  "TMS 2 par. 10 ve 12 - karma üretim yapısında uygun maliyet ölçümü", "hard")

q("Sipariş maliyet kartı ile yardımcı belgeler arasındaki uzlaştırma yapılmadığında en önemli risk aşağıdakilerden hangisidir?",
  "Maliyetin yanlış işe veya döneme yüklenmesi",
  ["Bütün siparişlerin fiziksel olarak aynı ürüne dönüşmesi ve üretim farklılıklarının ortadan kalkması",
   "Satış hasılatının üretim miktarıyla otomatik olarak eşitlenmesi ve alacakların tamamen kapanması",
   "Dönem sonu yarı mamullerin mevzuat gereği hiçbir zaman stok olarak raporlanamaması",
   "Genel üretim giderlerinin her koşulda direkt ilk madde maliyeti niteliği kazanması"],
  "Malzeme fişi, zaman kaydı, faaliyet ölçüsü ve kart toplamı uzlaştırılmazsa maliyet başka işe, yanlış döneme veya iki kez yüklenebilir.",
  "1 Sıra No.lu MSUGT - maliyet hesaplarının belgeye dayanması ve hesaplar arası tutarlılık", "hard")

# ── C. Safha maliyetleme — ağırlıklı ortalama ve FIFO (25) ───────────────
q("Safha maliyetlemede eşdeğer üretim hesabına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Malzeme ve dönüştürme için ayrı tamamlanma derecesi kullanılabilir\n\nII. Ağırlıklı ortalama yöntemi dönem başı ile cari dönem maliyetlerini birleştirir\n\nIII. FIFO yöntemi dönem başı maliyetini cari dönem birim maliyetine katar",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Malzeme ile dönüştürme farklı aşamalarda eklenebilir. Ağırlıklı ortalama maliyetleri birleştirir; FIFO cari dönem birim maliyetini ayrı hesaplar.",
  "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - safha maliyetleme ve eşdeğer üretim")

beg_units, started, completed, end_units = 1_000, 9_000, 8_200, 1_800
assert beg_units + started == completed + end_units
wa_mat_eu = completed + end_units
assert wa_mat_eu == 10_000
q(f"Ağırlıklı ortalama yönteminde dönem başı {tr(beg_units)} birim, başlanıp üretime alınan {tr(started)} birim, tamamlanan {tr(completed)} birim ve dönem sonu {tr(end_units)} birimdir. Malzeme safha başında ekleniyorsa malzeme eşdeğer birimi kaçtır?",
  f"{tr(wa_mat_eu)} birim",
  [f"{tr(completed)} birim yalnız tamamlanıp devredilenlerin malzeme eşdeğeri sayıldığı miktar",
   f"{tr(started)} birim dönem başı yarı mamulün ve tamamlanma akışının dışlandığı miktar",
   f"{tr(end_units)} birim yalnız dönem sonu yarı mamulün malzeme eşdeğeri sayıldığı miktar",
   f"{tr(completed+end_units*0.40)} birim dönüştürme derecesinin malzemeye de uygulandığı miktar"],
  f"Malzeme başlangıçta eklendiği için tamamlanan {tr(completed)} ve son stoktaki {tr(end_units)} birimin tümü malzeme yönünden tamdır: {tr(wa_mat_eu)} eşdeğer birim.",
  "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - ağırlıklı ortalama eşdeğer üretim")

end_conv = 0.40
wa_conv_eu = completed + end_units * end_conv
assert wa_conv_eu == 8_920
q(f"Aynı safhada {tr(completed)} birim tamamlanmış, dönem sonu {tr(end_units)} birim dönüştürme bakımından %{int(end_conv*100)} tamamlanmıştır. Ağırlıklı ortalama yönteminde dönüştürme eşdeğer birimi kaçtır?",
  f"{tr(wa_conv_eu)} birim",
  [f"{tr(completed+end_units)} birim dönem sonu yarı mamulün tamamen bitmiş kabul edildiği miktar",
   f"{tr(completed)} birim dönem sonu yarı mamulün dönüştürme emeğinin bütünüyle dışlandığı miktar",
   f"{tr(end_units*end_conv)} birim yalnız dönem sonu yarı mamulün eşdeğer üretim sayıldığı miktar",
   f"{tr((completed+end_units)*end_conv)} birim tamamlananlara da yüzde kırk uygulandığı miktar"],
  f"Dönüştürme eşdeğer birimi {tr(completed)} + {tr(end_units)} × %{int(end_conv*100)} = {tr(wa_conv_eu)} birimdir.",
  "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - dönüştürme eşdeğer üretimi")

beg_mat_cost, current_mat_cost = 30_000, 170_000
wa_mat_cost = (beg_mat_cost + current_mat_cost) / wa_mat_eu
assert wa_mat_cost == 20
q(f"Dönem başı yarı mamulde {tr(beg_mat_cost)} TL malzeme maliyeti, cari dönemde {tr(current_mat_cost)} TL malzeme maliyeti vardır. Malzeme eşdeğer birimi {tr(wa_mat_eu)} ise ağırlıklı ortalama malzeme maliyeti kaç TL/birimdir?",
  f"{tr(wa_mat_cost)} TL/birim",
  [f"{tr(current_mat_cost/wa_mat_eu)} TL/birim yalnız cari dönem maliyetinin paya alındığı sonuç",
   f"{tr(beg_mat_cost/wa_mat_eu)} TL/birim yalnız dönem başı maliyetinin paya alındığı sonuç",
   f"{tr((beg_mat_cost+current_mat_cost)/completed)} TL/birim yalnız tamamlananların paydaya alındığı sonuç",
   f"{tr((beg_mat_cost+current_mat_cost)/end_units)} TL/birim yalnız dönem sonu miktarının paydaya alındığı sonuç"],
  f"Ağırlıklı ortalamada maliyetler birleştirilir: ({tr(beg_mat_cost)} + {tr(current_mat_cost)}) / {tr(wa_mat_eu)} = {tr(wa_mat_cost)} TL/birim.",
  "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - ağırlıklı ortalama birim maliyeti")

beg_conv_cost, current_conv_cost = 16_000, 162_400
wa_conv_cost = (beg_conv_cost + current_conv_cost) / wa_conv_eu
assert wa_conv_cost == 20
q(f"Dönem başı yarı mamulde {tr(beg_conv_cost)} TL, cari dönemde {tr(current_conv_cost)} TL dönüştürme maliyeti vardır. Eşdeğer üretim {tr(wa_conv_eu)} ise ağırlıklı ortalama dönüştürme maliyeti kaç TL/birimdir?",
  f"{tr(wa_conv_cost)} TL/birim",
  [f"{tr(current_conv_cost/wa_conv_eu)} TL/birim dönem başı maliyetinin paydan çıkarıldığı sonuç",
   f"{tr(beg_conv_cost/wa_conv_eu)} TL/birim yalnız dönem başı maliyetinin dağıtıldığı sonuç",
   f"{tr((beg_conv_cost+current_conv_cost)/wa_mat_eu)} TL/birim malzeme eşdeğer biriminin kullanıldığı sonuç",
   f"{tr((beg_conv_cost+current_conv_cost)/completed)} TL/birim yarı mamul eşdeğerinin dışlandığı sonuç"],
  f"Toplam dönüştürme maliyeti {tr(beg_conv_cost+current_conv_cost)} TL'dir. {tr(wa_conv_eu)} eşdeğer birime bölününce {tr(wa_conv_cost)} TL/birim bulunur.",
  "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - ağırlıklı ortalama birim maliyeti")

wa_full_unit = wa_mat_cost + wa_conv_cost
completed_cost = completed * wa_full_unit
assert (wa_full_unit, completed_cost) == (40, 328_000)
q(f"Malzeme ve dönüştürme eşdeğer birim maliyetleri ayrı ayrı {tr(wa_mat_cost)} TL'dir. Tamamlanan {tr(completed)} birimin bir sonraki safhaya aktarılacak toplam maliyeti kaç TL'dir?",
  f"{tr(completed_cost)} TL",
  [f"{tr(completed*wa_mat_cost)} TL yalnız malzeme maliyetinin tamamlananlara aktarıldığı tutar",
   f"{tr(completed*wa_conv_cost)} TL yalnız dönüştürme maliyetinin tamamlananlara aktarıldığı tutar",
   f"{tr(wa_full_unit)} TL yalnız bir tamamlanmış birimin maliyetinin toplam sayıldığı tutar",
   f"{tr((completed+end_units)*wa_full_unit)} TL dönem sonu yarı mamullerin de tam birim sayıldığı tutar"],
  f"Tam birim maliyeti {tr(wa_mat_cost)} + {tr(wa_conv_cost)} = {tr(wa_full_unit)} TL'dir. {tr(completed)} × {tr(wa_full_unit)} = {tr(completed_cost)} TL aktarılır.",
  "TMS 2 par. 10 ve 12 - tamamlanan üretimin maliyetinin sonraki safhaya aktarımı")

ending_cost = end_units*wa_mat_cost + end_units*end_conv*wa_conv_cost
assert ending_cost == 50_400
q(f"Dönem sonu {tr(end_units)} birim malzeme yönünden tam, dönüştürme yönünden %{int(end_conv*100)} tamamlanmıştır. Her iki eşdeğer birim maliyeti {tr(wa_mat_cost)} TL ise dönem sonu yarı mamul maliyeti kaç TL'dir?",
  f"{tr(ending_cost)} TL",
  [f"{tr(end_units*wa_full_unit)} TL yarı mamullerin her iki unsur yönünden tamamen bitmiş sayıldığı tutar",
   f"{tr(end_units*end_conv*wa_full_unit)} TL yüzde kırkın malzeme maliyetine de uygulandığı tutar",
   f"{tr(end_units*wa_mat_cost)} TL yalnız malzeme maliyetinin yarı mamule verildiği tutar",
   f"{tr(end_units*end_conv*wa_conv_cost)} TL yalnız dönüştürme payının yarı mamul maliyeti sayıldığı tutar"],
  f"Malzeme payı {tr(end_units)} × {tr(wa_mat_cost)} = {tr(end_units*wa_mat_cost)} TL; dönüştürme payı {tr(end_units)} × %{int(end_conv*100)} × {tr(wa_conv_cost)} = {tr(end_units*end_conv*wa_conv_cost)} TL'dir. Toplam {tr(ending_cost)} TL olur.",
  "TMS 2 par. 10 ve 12 - dönem sonu yarı mamul maliyetinin eşdeğer üretimle ölçümü")

total_wa_cost = beg_mat_cost + current_mat_cost + beg_conv_cost + current_conv_cost
assert total_wa_cost == completed_cost + ending_cost == 378_400
q(f"Safhada dağıtılacak toplam maliyet {tr(total_wa_cost)} TL; tamamlananlara {tr(completed_cost)} TL ve dönem sonu yarı mamule {tr(ending_cost)} TL verilmiştir. Maliyet uzlaştırmasının sonucu nedir?",
  "Maliyetlerin tamamı dağıtılmıştır",
  ["Dağıtılan maliyet toplam maliyetten 50.400 TL eksik olduğu için bakiye bulunmaktadır",
   "Dağıtılan maliyet toplam maliyetten 328.000 TL fazla olduğu için aktarım ters çevrilmelidir",
   "Yalnız tamamlanan birim maliyeti toplamla karşılaştırılabileceğinden uzlaştırma yapılamaz",
   "Dönem sonu yarı mamul maliyeti dağıtım dışında bırakılmalı ve doğrudan gider yazılmalıdır"],
  f"Dağıtılan tutar {tr(completed_cost)} + {tr(ending_cost)} = {tr(total_wa_cost)} TL olup dağıtılacak toplamla aynıdır.",
  "TMS 2 par. 10 ve 12 - stok maliyetlerinin güvenilir ölçümü ve uzlaştırılması")

q("Ağırlıklı ortalama yöntemine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Dönem başı yarı mamul maliyeti cari maliyetle havuzlanır\n\nII. Malzeme ve dönüştürme için ayrı eşdeğer birim hesaplanabilir\n\nIII. Tamamlanıp devredilen birimler ilgili maliyet unsuru yönünden tam kabul edilir",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Ağırlıklı ortalamada dönem başı ve cari maliyetler birleşir; maliyet unsurlarının tamamlanma dereceleri ayrı ölçülebilir ve devredilen birimler tamdır.",
  "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - ağırlıklı ortalama yöntemi")

d2_completed, d2_ending = 7_000, 1_500
trans_eu = d2_completed + d2_ending
assert trans_eu == 8_500
q(f"İkinci safhada {tr(d2_completed)} birim tamamlanmış, {tr(d2_ending)} birim dönem sonunda kalmıştır. Birimler önceki safhadan bu safhaya girerken devralınan maliyeti taşıyorsa devralınan maliyet eşdeğer birimi kaçtır?",
  f"{tr(trans_eu)} birim",
  [f"{tr(d2_completed)} birim dönem sonu yarı mamulün devralınan maliyetinin dışlandığı miktar",
   f"{tr(d2_ending)} birim yalnız dönem sonu yarı mamulün devralınan maliyet taşıdığı varsayımı",
   f"{tr(d2_completed+d2_ending*0.50)} birim dönüştürme yüzdesinin devralınan maliyete uygulandığı miktar",
   f"{tr((d2_completed+d2_ending)*0.50)} birim tamamlananlara da yüzde elli uygulandığı miktar"],
  "Önceki safhadan gelen maliyet ikinci safhaya girişte birimlerin tümünde mevcuttur; tamamlanan ve son stoktaki birimler tam eşdeğer sayılır.",
  "TMS 2 par. 10 ve 12 - safhalar arası devralınan maliyet")

trans_cost = 255_000
trans_unit = trans_cost / trans_eu
assert trans_unit == 30
q(f"İkinci safhada dağıtılacak devralınan maliyet {tr(trans_cost)} TL ve devralınan maliyet eşdeğer birimi {tr(trans_eu)} ise birim başına devralınan maliyet kaç TL'dir?",
  f"{tr(trans_unit)} TL/birim",
  [f"{tr(trans_cost/d2_completed)} TL/birim dönem sonu birimlerin paydadan çıkarıldığı sonuç",
   f"{tr(trans_cost/d2_ending)} TL/birim yalnız dönem sonu birimlerin paydaya alındığı sonuç",
   f"{tr(trans_eu/trans_cost)} TL/birim maliyet ile eşdeğer birimin ters bölündüğü sonuç",
   f"{tr(trans_cost/(d2_completed+d2_ending*0.50))} TL/birim dönüştürme derecesinin devralınana uygulandığı sonuç"],
  f"Birim devralınan maliyet {tr(trans_cost)} / {tr(trans_eu)} = {tr(trans_unit)} TL'dir.",
  "TMS 2 par. 10 ve 12 - devralınan maliyetin ikinci safha birimlerine dağıtılması")

own_mat_total, own_mat_eu = 102_000, trans_eu
own_conv_total = 139_500
own_conv_eu = d2_completed + d2_ending*0.50
own_mat_unit = own_mat_total/own_mat_eu
own_conv_unit = own_conv_total/own_conv_eu
d2_full_unit = trans_unit + own_mat_unit + own_conv_unit
assert (own_conv_eu, own_mat_unit, own_conv_unit, d2_full_unit) == (7_750, 12, 18, 60)
q(f"İkinci safhada birim devralınan maliyet {tr(trans_unit)} TL, bu safhada eklenen malzeme {tr(own_mat_unit)} TL ve dönüştürme {tr(own_conv_unit)} TL'dir. Tamamlanan birimin toplam maliyeti kaç TL'dir?",
  f"{tr(d2_full_unit)} TL",
  [f"{tr(own_mat_unit+own_conv_unit)} TL önceki safhadan devralınan maliyetin dışlandığı sonuç",
   f"{tr(trans_unit+own_mat_unit)} TL bu safhanın dönüştürme maliyetinin dışlandığı sonuç",
   f"{tr(trans_unit+own_conv_unit)} TL bu safhada eklenen malzeme maliyetinin dışlandığı sonuç",
   f"{tr(trans_unit*own_mat_unit+own_conv_unit)} TL maliyet unsurlarının toplanmak yerine çarpıldığı sonuç"],
  f"Tamamlanan birim maliyeti {tr(trans_unit)} + {tr(own_mat_unit)} + {tr(own_conv_unit)} = {tr(d2_full_unit)} TL'dir.",
  "TMS 2 par. 10 ve 12 - ardışık safhalarda biriken üretim maliyeti")

d2_completed_cost = d2_completed*d2_full_unit
assert d2_completed_cost == 420_000
q(f"İkinci safhada tamamlanan {tr(d2_completed)} birimin tam maliyeti {tr(d2_full_unit)} TL/birimdir. Sonraki safhaya veya mamule aktarılacak tutar kaç TL'dir?",
  f"{tr(d2_completed_cost)} TL",
  [f"{tr(d2_completed*trans_unit)} TL yalnız devralınan maliyetin tamamlananlara verildiği tutar",
   f"{tr(d2_completed*(own_mat_unit+own_conv_unit))} TL yalnız ikinci safhada eklenen maliyetlerin aktarıldığı tutar",
   f"{tr(d2_full_unit)} TL birim maliyetin toplam aktarım tutarı kabul edildiği sonuç",
   f"{tr(trans_eu*d2_full_unit)} TL dönem sonu yarı mamullerin de tam birim sayıldığı tutar"],
  f"Aktarılacak maliyet {tr(d2_completed)} × {tr(d2_full_unit)} = {tr(d2_completed_cost)} TL'dir.",
  "TMS 2 par. 10 ve 12 - tamamlanan safha maliyetinin aktarımı")

d2_end_cost = d2_ending*trans_unit + d2_ending*own_mat_unit + d2_ending*0.50*own_conv_unit
d2_total = trans_cost + own_mat_total + own_conv_total
assert d2_end_cost == 76_500 and d2_total == d2_completed_cost+d2_end_cost == 496_500
q(f"İkinci safha sonundaki {tr(d2_ending)} birim; devralınan ve malzeme yönünden tam, dönüştürme yönünden %50'dir. Birim maliyetler sırasıyla {tr(trans_unit)}, {tr(own_mat_unit)} ve {tr(own_conv_unit)} TL ise yarı mamul maliyeti kaç TL'dir?",
  f"{tr(d2_end_cost)} TL",
  [f"{tr(d2_ending*d2_full_unit)} TL yarı mamullerin dönüştürme yönünden tam sayıldığı tutar",
   f"{tr(d2_ending*0.50*d2_full_unit)} TL yüzde ellinin bütün maliyet unsurlarına uygulandığı tutar",
   f"{tr(d2_ending*(trans_unit+own_mat_unit))} TL dönüştürme payının tamamen dışlandığı tutar",
   f"{tr(d2_ending*own_conv_unit)} TL yalnız dönüştürme maliyetinin yarı mamule verildiği tutar"],
  f"Devralınan pay {tr(d2_ending*trans_unit)}, malzeme payı {tr(d2_ending*own_mat_unit)}, dönüştürme payı {tr(d2_ending*0.50*own_conv_unit)} TL'dir. Toplam {tr(d2_end_cost)} TL olur.",
  "TMS 2 par. 10 ve 12 - ikinci safha dönem sonu yarı mamul maliyeti", "hard")

fifo_beg, fifo_started, fifo_completed, fifo_end = 1_200, 8_800, 9_000, 1_000
started_completed = fifo_completed - fifo_beg
assert fifo_beg + fifo_started == fifo_completed + fifo_end and started_completed == 7_800
q(f"FIFO safha maliyetinde dönem başı yarı mamul {tr(fifo_beg)} birim, dönemde başlanan {tr(fifo_started)} birim ve tamamlanan {tr(fifo_completed)} birimdir. Dönemde başlanıp tamamlanan birim sayısı kaçtır?",
  f"{tr(started_completed)} birim",
  [f"{tr(fifo_completed)} birim dönem başı yarı mamullerin de cari dönemde başlanmış sayıldığı miktar",
   f"{tr(fifo_started)} birim dönem sonunda kalan birimlerin de tamamlanmış sayıldığı miktar",
   f"{tr(fifo_beg)} birim yalnız dönem başı yarı mamullerin başlanıp tamamlandığı kabulü",
   f"{tr(fifo_completed+fifo_beg)} birim dönem başı yarı mamulün tamamlananlara ikinci kez eklendiği miktar"],
  f"Tamamlanan {tr(fifo_completed)} birimin {tr(fifo_beg)} birimi dönem başından gelir. Cari dönemde başlanıp tamamlanan = {tr(fifo_completed)} − {tr(fifo_beg)} = {tr(started_completed)} birimdir.",
  "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - safha maliyetleme (FIFO yöntemi)")

beg_conv_degree, end_fifo_conv = 0.30, 0.50
finish_beg_conv_eu = fifo_beg*(1-beg_conv_degree)
end_fifo_conv_eu = fifo_end*end_fifo_conv
fifo_conv_eu = finish_beg_conv_eu + started_completed + end_fifo_conv_eu
assert (finish_beg_conv_eu, end_fifo_conv_eu, fifo_conv_eu) == (840, 500, 9_140)
q(f"FIFO yönteminde dönem başı {tr(fifo_beg)} birim dönüştürme yönünden %{int(beg_conv_degree*100)}, dönem sonu {tr(fifo_end)} birim %{int(end_fifo_conv*100)} tamamdır; dönemde başlanıp tamamlanan {tr(started_completed)} birimdir. Cari dönem dönüştürme eşdeğer birimi kaçtır?",
  f"{tr(fifo_conv_eu)} birim",
  [f"{tr(fifo_completed+end_fifo_conv_eu)} birim dönem başının önceki dönemde yapılan kısmının da cari döneme alındığı miktar",
   f"{tr(started_completed+end_fifo_conv_eu)} birim dönem başı yarı mamulü tamamlama emeğinin dışlandığı miktar",
   f"{tr(finish_beg_conv_eu+started_completed)} birim dönem sonu yarı mamul emeğinin dışlandığı miktar",
   f"{tr(fifo_beg+started_completed+fifo_end)} birim bütün birimlerin tamamlanma derecesiz toplandığı miktar"],
  f"Dönem başını tamamlama {tr(fifo_beg)} × %70 = {tr(finish_beg_conv_eu)}; başlanıp tamamlanan {tr(started_completed)}; son stok {tr(fifo_end)} × %50 = {tr(end_fifo_conv_eu)} eşdeğer birimdir. Toplam {tr(fifo_conv_eu)} olur.",
  "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - FIFO eşdeğer üretimi", "hard")

q("FIFO safha maliyetine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Dönem başı yarı mamulü tamamlamak için cari dönemde yapılan iş ayrı ölçülür\n\nII. Dönemde başlanıp tamamlanan birimler cari dönem eşdeğer üretimine tam girer\n\nIII. Dönem başı maliyeti cari dönem birim maliyeti hesabına dâhil edilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "FIFO cari dönemin işini ayırır; dönem başı maliyeti cari dönem eşdeğer birim maliyetinin payına katılmaz.",
  "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - FIFO yönteminin dönem ayrımı")

fifo_mat_eu = started_completed + fifo_end
assert fifo_mat_eu == 8_800
q(f"FIFO yönteminde malzeme safha başında eklenmektedir. Dönem başı {tr(fifo_beg)} birim malzemeyi önceki dönemde almış, dönemde başlanıp tamamlanan {tr(started_completed)} ve dönem sonu {tr(fifo_end)} birim vardır. Cari dönem malzeme eşdeğer birimi kaçtır?",
  f"{tr(fifo_mat_eu)} birim",
  [f"{tr(fifo_beg+started_completed+fifo_end)} birim dönem başı birimlere malzemenin cari dönemde yeniden verildiği miktar",
   f"{tr(started_completed)} birim dönem sonu yarı mamulün cari malzeme tüketiminin dışlandığı miktar",
   f"{tr(fifo_completed+fifo_end)} birim tamamlanan dönem başı birimlerin cari malzemeye katıldığı miktar",
   f"{tr(fifo_started+fifo_beg)} birim dönem başı miktarın dönemde başlanana ikinci kez eklendiği miktar"],
  f"Dönem başı birimler malzemeyi önceki dönemde almıştır. Cari malzeme eşdeğeri {tr(started_completed)} + {tr(fifo_end)} = {tr(fifo_mat_eu)} birimdir.",
  "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - FIFO malzeme eşdeğer üretimi", "hard")

fifo_current_mat, fifo_current_conv = 176_000, 182_800
fifo_mat_unit = fifo_current_mat/fifo_mat_eu
fifo_conv_unit = fifo_current_conv/fifo_conv_eu
assert (fifo_mat_unit, fifo_conv_unit) == (20, 20)
q(f"FIFO yönteminde cari malzeme maliyeti {tr(fifo_current_mat)} TL/{tr(fifo_mat_eu)} eşdeğer birim; cari dönüştürme maliyeti {tr(fifo_current_conv)} TL/{tr(fifo_conv_eu)} eşdeğer birimdir. Cari birim maliyetler sırasıyla kaç TL'dir?",
  f"{tr(fifo_mat_unit)} TL ve {tr(fifo_conv_unit)} TL",
  [f"{tr(fifo_current_mat/fifo_conv_eu)} TL ve {tr(fifo_current_conv/fifo_mat_eu)} TL paydaların yer değiştirdiği sonuç",
   f"{tr((fifo_current_mat+fifo_current_conv)/fifo_mat_eu)} TL ve aynı tutarda iki unsurun tek paydada toplandığı sonuç",
   f"{tr(fifo_current_mat/fifo_completed)} TL ve {tr(fifo_current_conv/fifo_completed)} TL yalnız tamamlananların paydaya alındığı sonuç",
   f"{tr(fifo_mat_eu/fifo_current_mat)} TL ve {tr(fifo_conv_eu/fifo_current_conv)} TL maliyet ve birimlerin ters bölündüğü sonuç"],
  f"Malzeme {tr(fifo_current_mat)} / {tr(fifo_mat_eu)} = {tr(fifo_mat_unit)} TL; dönüştürme {tr(fifo_current_conv)} / {tr(fifo_conv_eu)} = {tr(fifo_conv_unit)} TL/birimdir.",
  "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - FIFO cari dönem birim maliyeti", "hard")

finish_beg_cost = finish_beg_conv_eu*fifo_conv_unit
assert finish_beg_cost == 16_800
q(f"Dönem başı {tr(fifo_beg)} birim dönüştürme yönünden %30 tamamdır. FIFO cari dönüştürme maliyeti {tr(fifo_conv_unit)} TL/eşdeğer birim ise bu stoku cari dönemde tamamlamak için eklenecek maliyet kaç TL'dir?",
  f"{tr(finish_beg_cost)} TL",
  [f"{tr(fifo_beg*fifo_conv_unit)} TL dönem başı birimlerin cari dönemde baştan sona işlendiği varsayımı",
   f"{tr(fifo_beg*beg_conv_degree*fifo_conv_unit)} TL önceki dönemde yapılmış yüzde otuzluk kısmın yeniden yüklendiği tutar",
   f"{tr(started_completed*fifo_conv_unit)} TL dönemde başlanıp tamamlananların maliyetinin dönem başına verildiği tutar",
   f"{tr(fifo_end*end_fifo_conv*fifo_conv_unit)} TL dönem sonu yarı mamul dönüşümünün dönem başına yüklendiği tutar"],
  f"Cari dönemde kalan iş %70'tir: {tr(fifo_beg)} × %70 × {tr(fifo_conv_unit)} = {tr(finish_beg_cost)} TL.",
  "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - FIFO dönem başı yarı mamul maliyeti", "hard")

started_completed_cost = started_completed*(fifo_mat_unit+fifo_conv_unit)
assert started_completed_cost == 312_000
q(f"FIFO yönteminde dönemde başlanıp tamamlanan {tr(started_completed)} birim için cari malzeme ve dönüştürme maliyetleri ayrı ayrı {tr(fifo_mat_unit)} TL/birimdir. Bu birimlerin maliyeti kaç TL'dir?",
  f"{tr(started_completed_cost)} TL",
  [f"{tr(started_completed*fifo_mat_unit)} TL yalnız cari malzeme maliyetinin dikkate alındığı tutar",
   f"{tr(started_completed*fifo_conv_unit)} TL yalnız cari dönüştürme maliyetinin dikkate alındığı tutar",
   f"{tr((fifo_started)*(fifo_mat_unit+fifo_conv_unit))} TL dönem sonu yarı mamulün de tamamlandığı varsayımı",
   f"{tr((fifo_completed)*(fifo_mat_unit+fifo_conv_unit))} TL dönem başı birimlere cari malzemenin yeniden yüklendiği tutar"],
  f"Tam cari birim maliyeti {tr(fifo_mat_unit+fifo_conv_unit)} TL'dir. {tr(started_completed)} × {tr(fifo_mat_unit+fifo_conv_unit)} = {tr(started_completed_cost)} TL olur.",
  "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - FIFO başlanıp tamamlanan birim maliyeti")

fifo_end_cost = fifo_end*fifo_mat_unit + fifo_end*end_fifo_conv*fifo_conv_unit
assert fifo_end_cost == 30_000
q(f"FIFO dönem sonu {tr(fifo_end)} birim malzeme yönünden tam, dönüştürme yönünden %{int(end_fifo_conv*100)}'dir. Cari birim maliyetler her unsur için {tr(fifo_mat_unit)} TL ise dönem sonu yarı mamul maliyeti kaç TL'dir?",
  f"{tr(fifo_end_cost)} TL",
  [f"{tr(fifo_end*(fifo_mat_unit+fifo_conv_unit))} TL yarı mamullerin dönüştürme yönünden tam sayıldığı tutar",
   f"{tr(fifo_end*end_fifo_conv*(fifo_mat_unit+fifo_conv_unit))} TL yüzde ellinin malzemeye de uygulandığı tutar",
   f"{tr(fifo_end*fifo_mat_unit)} TL yalnız malzeme payının yarı mamul maliyeti sayıldığı tutar",
   f"{tr(fifo_end*end_fifo_conv*fifo_conv_unit)} TL yalnız dönüştürme payının yarı mamul maliyeti sayıldığı tutar"],
  f"Malzeme {tr(fifo_end*fifo_mat_unit)} TL, dönüştürme {tr(fifo_end*end_fifo_conv*fifo_conv_unit)} TL'dir; toplam {tr(fifo_end_cost)} TL olur.",
  "TMS 2 par. 10-13; 2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - FIFO yarı mamul maliyeti")

beg_total_cost = 39_600
completed_beg_cost = beg_total_cost + finish_beg_cost
fifo_total_cost = beg_total_cost + fifo_current_mat + fifo_current_conv
fifo_allocated = completed_beg_cost + started_completed_cost + fifo_end_cost
assert completed_beg_cost == 56_400 and fifo_total_cost == fifo_allocated == 398_400
q(f"FIFO raporunda dönem başı maliyeti {tr(beg_total_cost)} TL, bu birimleri tamamlama maliyeti {tr(finish_beg_cost)} TL, başlanıp tamamlananların maliyeti {tr(started_completed_cost)} TL ve son stok maliyeti {tr(fifo_end_cost)} TL'dir. Toplam dağıtılan maliyet kaç TL'dir?",
  f"{tr(fifo_allocated)} TL",
  [f"{tr(started_completed_cost+fifo_end_cost)} TL dönem başı ve tamamlama maliyetlerinin dışlandığı tutar",
   f"{tr(beg_total_cost+started_completed_cost+fifo_end_cost)} TL dönem başını tamamlama maliyetinin dışlandığı tutar",
   f"{tr(completed_beg_cost+fifo_end_cost)} TL başlanıp tamamlanan birimlerin maliyetinin dışlandığı tutar",
   f"{tr(beg_total_cost+finish_beg_cost+started_completed_cost)} TL dönem sonu yarı mamul maliyetinin dışlandığı tutar"],
  f"Dönem başından tamamlananların maliyeti {tr(beg_total_cost)} + {tr(finish_beg_cost)} = {tr(completed_beg_cost)} TL'dir. Buna {tr(started_completed_cost)} ve {tr(fifo_end_cost)} eklenince {tr(fifo_allocated)} TL bulunur.",
  "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - FIFO maliyet uzlaştırması", "hard")

q("Ağırlıklı ortalama ile FIFO karşılaştırmasına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Fiyatlar değiştiğinde iki yöntemin birim maliyetleri farklılaşabilir\n\nII. FIFO cari dönem performansını önceki dönem maliyetinden daha çok ayırır\n\nIII. Dönem başı yarı mamul yokken yöntemler mutlaka farklı sonuç verir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Maliyet düzeyi değiştiğinde havuzlama fark yaratabilir ve FIFO cari dönemi ayırır. Dönem başı yarı mamul yoksa yöntem sonuçları aynılaşabilir.",
  "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - ağırlıklı ortalama ve FIFO karşılaştırması", "hard")

q("Dönem başı yarı mamulün birim maliyeti cari dönem maliyetinden belirgin düşükse, diğer veriler aynı olmak üzere ağırlıklı ortalama yönteminin cari dönem FIFO maliyetine göre genel etkisi ne olabilir?",
  "Birim maliyeti aşağı doğru yumuşatabilir",
  ["Dönem başı maliyetini tamamen yok saydığı için birim maliyeti her durumda cari FIFO ile eşitler",
   "Dönem başı düşük maliyeti yalnız satış hasılatına eklediği için üretim maliyetini zorunlu olarak artırır",
   "Cari dönem maliyetini kullanmadığı için tüm tamamlanan birimleri yalnız dönem başı maliyetiyle değerler",
   "Yarı mamul tamamlanma derecelerini kaldırdığı için maliyet uzlaştırmasını matematiksel olarak imkânsız yapar"],
  "Ağırlıklı ortalama düşük dönem başı maliyetini daha yüksek cari maliyetle birleştirdiğinden, birleşik birim maliyet cari dönem FIFO maliyetinin altında kalabilir.",
  "2026 SMMM Yeterlilik Maliyet Muhasebesi kapsamı - ağırlıklı ortalama ve FIFO maliyet davranışı", "hard")


# Seçenekler, ilk taslaktaki sistematik "doğru şık kısa" kalıbını kaldırmak
# üzere aynı kavramsal düzeyde yeniden kurulmuştur. Sayısal sorularda gerekçe
# metni seçeneğe değil çözüme bırakılır; böylece seçenekler gerçek sınavdaki
# gibi yalnız sonuçları karşılaştırır.
CHOICE_OVERRIDES = {
    1: (
        "Sipariş maliyetleme sistemi",
        ["Safha maliyetleme sistemi", "Karma maliyetleme sistemi",
         "İşlem maliyetleme sistemi", "Standart maliyetleme sistemi"],
    ),
    2: (
        "Safha maliyetleme sistemi",
        ["Sipariş maliyetleme sistemi", "Karma maliyetleme sistemi",
         "Proje maliyetleme sistemi", "Parti maliyetleme sistemi"],
    ),
    3: (
        "Belirli sipariş veya üretim partisi",
        ["Üretim bölümünün dönemlik gider toplamı",
         "Tedarikçiye göre gruplanan hammadde alımları",
         "İşletmenin dönemlik toplam satış hacmi",
         "Dönem sonundaki bütün stokların toplamı"],
    ),
    5: (
        "Ortak süreç ve modele özgü maliyetleri birleştiren karma maliyetleme",
        ["Bütün üretimi tek safha ortalamasıyla ölçen safha maliyetleme",
         "Her ayakkabı teki için ayrı kart açan sipariş maliyetleme",
         "Üretim giderlerini yalnız satış bölümünde toplayan dönem yaklaşımı",
         "Bütün üretim maliyetlerini doğrudan giderleştiren dönem yaklaşımı"],
    ),
    6: (
        "İşe yüklenen üç maliyet unsurunu bir kayıtta toplamak",
        ["Satışları tahsilat vadelerine göre sınıflandırmak",
         "Yarı mamulleri doğrudan mamul kabul etmek",
         "Finansman giderlerini işlere eşit dağıtmak",
         "Genel yönetim giderlerini ürünlere yüklemek"],
    ),
    7: (
        "Birim ve maliyet akışının eksiksizliğini doğrulamak",
        ["Satış fiyatlarındaki değişimi dönem kârına aktarmak",
         "Yarı mamulleri tamamlanmış birim kabul etmek",
         "Bütün maliyet unsurlarında aynı tamamlanma oranını kullanmak",
         "Devralınan maliyeti sonraki safhadan ayrı tutmak"],
    ),
    8: (
        "Stok maliyetinin üretim ve satış akışını",
        ["Üretim giderlerinin doğrudan dönem giderine aktarılmasını",
         "Maliyetlerin satış hasılatıyla netleştirilmesini",
         "Genel yönetim giderlerinin mamullere yüklenmesini",
         "Üretim maliyetlerinin kasa hesabında izlenmesini"],
    ),
    9: (
        "Devralınan maliyet olarak ikinci safhaya taşınır",
        ["Birinci safhanın dönem gideri olarak kaydedilir",
         "İkinci safhanın direkt işçilik maliyetinden düşülür",
         "Doğrudan satılan mamul maliyetine aktarılır",
         "Finansman maliyeti olarak dönem sonucuna yüklenir"],
    ),
    10: (
        "Benzer birimlerin ortak kaynak tüketimine",
        ["Maliyetlerin güvenilir biçimde ölçülememesine",
         "Birimlerin müşteri talebine göre farklılaşmasına",
         "Direkt işçiliğin dönem gideri kabul edilmesine",
         "Yarı mamul miktarlarının dönemler boyunca eşit kalmasına"],
    ),
    11: (
        "Parti düzeyinde",
        ["Birim düzeyinde", "Bölüm düzeyinde", "İşletme düzeyinde", "Tedarikçi düzeyinde"],
    ),
    13: (
        "İşlerin ayırt edilebilir olması",
        ["Makinelerin aynı özellikte olması", "Satış vadelerinin benzer olması",
         "Siparişlerin aynı gün tamamlanması", "Üretimin tek bölümde yürütülmesi"],
    ),
    14: (
        "Bölümlerin farklı kaynak tüketimini yansıtır",
        ["Direkt maliyetleri üretim maliyetinden çıkarır",
         "Her siparişe aynı tutarda genel gider yükler",
         "Yarı mamul tamamlanma derecesini gereksiz kılar",
         "Satış fiyatı yüksek siparişin maliyetini düşürür"],
    ),
    15: (
        "Aynı işletmede farklı üretim yapıları bulunabilir",
        ["Sektör bilgisi maliyetlemede kullanılamayabilir",
         "Bütün sektörlerde yalnız sipariş sistemi uygulanabilir",
         "Safha sistemi yalnız hizmet işletmelerine uygun olabilir",
         "Üretim akışı maliyet nesnesini her zaman etkilemeyebilir"],
    ),
    16: (
        "20 TL/makine saati ve 20 TL/işçilik saati",
        ["33,33 TL/makine saati ve 12 TL/işçilik saati",
         "20 TL/makine saati ve 12 TL/işçilik saati",
         "40 TL/makine saati ve 20 TL/işçilik saati",
         "12 TL/makine saati ve 33,33 TL/işçilik saati"],
    ),
    17: ("15.000 TL", ["9.000 TL", "6.000 TL", "30.000 TL", "7.500 TL"]),
    18: ("142.000 TL", ["127.000 TL", "100.000 TL", "57.000 TL", "112.000 TL"]),
    19: ("355 TL", ["284 TL", "317,50 TL", "473,33 TL", "392,50 TL"]),
    21: ("110.000 TL", ["62.000 TL", "48.000 TL", "14.000 TL", "220.000 TL"]),
    22: ("228.000 TL", ["132.000 TL", "96.000 TL", "36.000 TL", "456.000 TL"]),
    23: ("120.000 TL", ["40.000 TL", "160.000 TL", "280.000 TL", "213.333,33 TL"]),
    24: (
        "120.000 TL / 84.000 TL",
        ["108.000 TL / 48.000 TL", "84.000 TL / 120.000 TL",
         "156.000 TL / 48.000 TL", "72.000 TL / 156.000 TL"],
    ),
    25: ("28.000 TL", ["20 TL", "685,71 TL", "28.020 TL", "0 TL"]),
    26: (
        "10.000 TL eksik yükleme",
        ["10.000 TL fazla yükleme", "1.040.000 TL eksik yükleme",
         "1.050.000 TL fazla yükleme", "2.090.000 TL eksik yükleme"],
    ),
    27: ("18.000 TL", ["10.000 TL", "4.500 TL", "7.500 TL", "45.000 TL"]),
    29: ("78.000 TL", ["90.000 TL", "98.000 TL", "86.000 TL", "20.000 TL"]),
    30: ("38.400 TL", ["41.600 TL", "3.200 TL", "35.200 TL", "44.800 TL"]),
    31: (
        "151'den 152 Mamuller hesabına aktarılmalıdır",
        ["151 Yarı Mamuller hesabında bırakılmalıdır",
         "620 Satılan Mamuller Maliyetine aktarılmalıdır",
         "770 Genel Yönetim Giderlerine aktarılmalıdır",
         "120 Alıcılar hesabında izlenmelidir"],
    ),
    32: ("16.200 TL", ["21.000 TL", "12.600 TL", "33.600 TL", "9.000 TL"]),
    33: (
        "65.000 TL kâr",
        ["185.000 TL kâr", "250.000 TL kâr", "435.000 TL kâr", "65.000 TL zarar"],
    ),
    34: (
        "Ortak işlem maliyetleri ortalanır, özgü malzeme modele yüklenir",
        ["Bütün maliyetler satış fiyatına göre müşterilere dağıtılır",
         "Modele özgü malzeme bütün ürünlere eşit ortalanır",
         "Ortak işlem maliyetleri giderleştirilip yalnız malzeme stoklanır",
         "Her mamul birimi için bağımsız bir sipariş maliyet kartı açılır"],
    ),
    35: (
        "Maliyetin yanlış işe veya döneme yüklenmesi",
        ["Siparişlerin aynı ürüne dönüşmesi", "Satış hasılatının üretime eşitlenmesi",
         "Yarı mamullerin stok olarak raporlanamaması",
         "Genel giderlerin direkt malzeme niteliği kazanması"],
    ),
    37: ("10.000", ["8.200", "9.000", "1.800", "8.920"]),
    38: ("8.920", ["10.000", "8.200", "720", "4.000"]),
    39: ("20 TL", ["17 TL", "3 TL", "24,39 TL", "111,11 TL"]),
    40: ("20 TL", ["18,21 TL", "1,79 TL", "17,84 TL", "21,76 TL"]),
    41: ("328.000 TL", ["164.000 TL", "40 TL", "400.000 TL", "378.400 TL"]),
    42: ("50.400 TL", ["72.000 TL", "28.800 TL", "36.000 TL", "14.400 TL"]),
    43: (
        "Maliyetlerin tamamı dağıtılmıştır",
        ["50.400 TL dağıtılmadan kalmıştır", "328.000 TL fazla dağıtılmıştır",
         "Yalnız tamamlanan birimler uzlaştırılmıştır",
         "Yarı mamul maliyeti dönem giderine aktarılmıştır"],
    ),
    45: ("8.500", ["7.000", "1.500", "7.750", "4.250"]),
    46: ("30 TL", ["36,43 TL", "170 TL", "0,03 TL", "32,90 TL"]),
    47: ("60 TL", ["30 TL", "42 TL", "48 TL", "378 TL"]),
    48: ("420.000 TL", ["210.000 TL", "60 TL", "510.000 TL", "496.500 TL"]),
    49: ("76.500 TL", ["90.000 TL", "45.000 TL", "63.000 TL", "27.000 TL"]),
    50: ("7.800", ["9.000", "8.800", "1.200", "10.200"]),
    51: ("9.140", ["9.500", "8.300", "8.640", "10.000"]),
    53: ("8.800", ["10.000", "7.800", "9.000", "1.000"]),
    54: (
        "20 TL / 20 TL",
        ["19,26 TL / 20,77 TL", "40,77 TL / 40,77 TL",
         "19,56 TL / 20,31 TL", "0,05 TL / 0,05 TL"],
    ),
    55: ("16.800 TL", ["24.000 TL", "7.200 TL", "156.000 TL", "10.000 TL"]),
    56: ("312.000 TL", ["156.000 TL", "352.000 TL", "360.000 TL", "342.000 TL"]),
    57: ("30.000 TL", ["40.000 TL", "20.000 TL", "10.000 TL", "50.000 TL"]),
    58: ("398.400 TL", ["342.000 TL", "381.600 TL", "86.400 TL", "368.400 TL"]),
    60: (
        "Birim maliyeti aşağı doğru yumuşatabilir",
        ["Birim maliyeti cari FIFO maliyetine eşitleyebilir",
         "Üretim maliyetini zorunlu olarak artırabilir",
         "Tamamlananları yalnız dönem başı maliyetiyle değerleyebilir",
         "Maliyet uzlaştırmasını matematiksel olarak engelleyebilir"],
    ),
}

STEM_OVERRIDES = {
    36: (
        "Safha maliyetlemede eşdeğer üretim hesabına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\n"
        "I. Malzeme ve dönüştürme için ayrı tamamlanma derecesi kullanılabilir\n\n"
        "II. Ağırlıklı ortalama yöntemi dönem başı ile cari dönem maliyetlerini birleştirir\n\n"
        "III. FIFO cari dönemin birim maliyetini dönem başı maliyetinden ayırır"
    ),
    52: (
        "FIFO safha maliyetine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\n"
        "I. Dönem başı yarı mamulü tamamlamak için cari dönemde yapılan iş ayrı ölçülür\n\n"
        "II. Dönemde başlanıp tamamlanan birimler cari dönem eşdeğer üretimine tam girer\n\n"
        "III. Dönem başı maliyeti cari dönem eşdeğer birim maliyetinin payına alınmaz"
    ),
}

PREMISE_OVERRIDES = {
    36: (
        "I, II ve III",
        ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
        "Malzeme ve dönüştürme farklı tamamlanma derecelerinde olabilir; ağırlıklı ortalama maliyetleri birleştirirken FIFO cari dönem maliyetini önceki dönemden ayırır.",
    ),
    52: (
        "I, II ve III",
        ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
        "FIFO cari dönemin işini ve maliyetini ayırır; dönem başı maliyeti cari dönem eşdeğer birim maliyetinin payına katılmaz.",
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
        for key, distractor in zip([k for k in "ABCDE" if k != ans], item["distractors"]):
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
