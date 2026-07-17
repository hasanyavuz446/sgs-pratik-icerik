# -*- coding: utf-8 -*-
"""Yeterlilik — Finansal Tablolar ve Analizi Test 2 + Test 3 (2×20 = 40 soru).
TÜM ARİTMETİK PYTHON'DA HESAPLANIR — kafadan sayı yazılmaz.
Çeldiriciler makul hata sonuçlarıdır (yanlış payda, ters oran, stok düşmeyi unutmak…).
Şıklar aynı kavramsal düzeyde ve doğal uzunlukta tutulur. Açıklamada harf atfı YOK."""
import json, random, re
from pathlib import Path

L = "mali_tablolar_analizi"
STIM = "yet-analiz-ghi-001"

# ══ ORTAK VERİ (bin TL) — tüm hesaplar buradan türetilir ══════════════════
D = {
    2025: dict(hazir=160, alacak=240, stok=200, diger_dv=40, dv=640, duran=960, toplam=1600,
               kvyk=500, uvyk=460, ozkaynak=640,
               satis=2000, smm=1300, brut=700, faal_gider=450, faal_kar=250, net_kar=150),
    2026: dict(hazir=180, alacak=300, stok=300, diger_dv=120, dv=900, duran=1100, toplam=2000,
               kvyk=600, uvyk=600, ozkaynak=800,
               satis=2400, smm=1500, brut=900, faal_gider=540, faal_kar=360, net_kar=240),
}
# Tablo tutarlılığı — yanlış veriyle soru üretmemek için
for y, d in D.items():
    assert d["hazir"] + d["alacak"] + d["stok"] + d["diger_dv"] == d["dv"], y
    assert d["dv"] + d["duran"] == d["toplam"], y
    assert d["kvyk"] + d["uvyk"] + d["ozkaynak"] == d["toplam"], y
    assert d["satis"] - d["smm"] == d["brut"], y
    assert d["brut"] - d["faal_gider"] == d["faal_kar"], y

def tr(v):
    """Türkçe sayı biçimi: 1234.5 → '1.234,5'"""
    if isinstance(v, float) and abs(v - round(v)) < 1e-9: v = round(v)
    s = f"{v:,.2f}".replace(",", "\x00").replace(".", ",").replace("\x00", ".")
    return s.rstrip("0").rstrip(",") if "," in s else s

def yuzde(v): return tr(round(v * 100, 2)) + "%"

STIM_BODY = (
    "| Kalem (bin TL) | 2025 | 2026 |\n|---|---:|---:|\n"
    + "\n".join(f"| {ad} | {tr(D[2025][k])} | {tr(D[2026][k])} |" for ad, k in [
        ("Hazır Değerler", "hazir"), ("Ticari Alacaklar", "alacak"), ("Stoklar", "stok"),
        ("Diğer Dönen Varlıklar", "diger_dv"), ("**Dönen Varlıklar**", "dv"),
        ("Duran Varlıklar", "duran"), ("**Toplam Varlıklar**", "toplam"),
        ("Kısa Vadeli Yabancı Kaynaklar", "kvyk"), ("Uzun Vadeli Yabancı Kaynaklar", "uvyk"),
        ("Özkaynaklar", "ozkaynak"), ("Net Satışlar", "satis"),
        ("Satışların Maliyeti", "smm"), ("**Brüt Kâr**", "brut"),
        ("Faaliyet Giderleri", "faal_gider"), ("**Faaliyet Kârı**", "faal_kar"),
        ("Net Dönem Kârı", "net_kar")])
)

Q = []
def q(topic, label, stem, correct, distractors, why, ref, stim=None, difficulty="medium"):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar ediyor: " + stem[:44]
    Q.append(dict(topic=topic, label=label, stem=stem, correct=correct, distractors=distractors,
                  why=why, ref=ref, stim=stim, difficulty=difficulty))

a, b = D[2025], D[2026]
G = "GHI İşletmesi'nin verilerine göre "

# ══ ORTAK TABLOYA BAĞLI (14) ══════════════════════════════════════════════
v = b["dv"] / b["kvyk"]
q("oran_analizi", "Oran Analizi", G + "2026 yılı cari oranı kaçtır?",
  tr(v), [tr(b["kvyk"]/b["dv"]), tr(b["toplam"]/b["kvyk"]), tr((b["dv"]-b["stok"])/b["kvyk"]), tr(b["dv"]/(b["kvyk"]+b["uvyk"]))],
  f"Cari oran = Dönen Varlıklar / KVYK = {tr(b['dv'])} / {tr(b['kvyk'])} = {tr(v)}.",
  "Oran analizi - cari oran", STIM)

v = (b["dv"] - b["stok"]) / b["kvyk"]
q("oran_analizi", "Oran Analizi", G + "2026 yılı asit-test (likidite) oranı kaçtır?",
  tr(v), [tr(b["dv"]/b["kvyk"]), tr(b["hazir"]/b["kvyk"]), tr((b["dv"]-b["stok"]-b["hazir"])/b["kvyk"]), tr(b["stok"]/b["kvyk"])],
  f"Asit-test oranı = (Dönen Varlıklar − Stoklar) / KVYK = ({tr(b['dv'])} − {tr(b['stok'])}) / {tr(b['kvyk'])} = {tr(v)}.",
  "Oran analizi - asit-test", STIM)

v = b["hazir"] / b["kvyk"]
q("oran_analizi", "Oran Analizi", G + "2026 yılı nakit (hazır değerler) oranı kaçtır?",
  tr(v), [tr(b["dv"]/b["kvyk"]), tr((b["dv"]-b["stok"])/b["kvyk"]), tr(b["hazir"]/b["toplam"]), tr(b["hazir"]/b["dv"])],
  f"Nakit oranı = Hazır Değerler / KVYK = {tr(b['hazir'])} / {tr(b['kvyk'])} = {tr(v)}.",
  "Oran analizi - nakit oranı", STIM)

v = b["net_kar"] / b["satis"]
q("oran_analizi", "Oran Analizi", G + "2026 yılı net kâr marjı yüzde kaçtır?",
  yuzde(v), [yuzde(b["brut"]/b["satis"]), yuzde(b["faal_kar"]/b["satis"]), yuzde(b["net_kar"]/b["ozkaynak"]), yuzde(b["net_kar"]/b["toplam"])],
  f"Net kâr marjı = Net Kâr / Net Satışlar = {tr(b['net_kar'])} / {tr(b['satis'])} = {yuzde(v)}.",
  "Oran analizi - net kâr marjı", STIM)

v = b["net_kar"] / b["ozkaynak"]
q("oran_analizi", "Oran Analizi", G + "2026 yılı özkaynak kârlılığı yüzde kaçtır?",
  yuzde(v), [yuzde(b["net_kar"]/b["toplam"]), yuzde(b["net_kar"]/b["satis"]), yuzde(b["faal_kar"]/b["ozkaynak"]), yuzde(b["ozkaynak"]/b["toplam"])],
  f"Özkaynak kârlılığı = Net Kâr / Özkaynaklar = {tr(b['net_kar'])} / {tr(b['ozkaynak'])} = {yuzde(v)}.",
  "Oran analizi - özkaynak kârlılığı", STIM)

v = b["net_kar"] / b["toplam"]
q("oran_analizi", "Oran Analizi", G + "2026 yılı aktif kârlılığı (dönem sonu varlıklara göre) yüzde kaçtır?",
  yuzde(v), [yuzde(b["net_kar"]/b["ozkaynak"]), yuzde(b["net_kar"]/b["satis"]), yuzde(b["faal_kar"]/b["toplam"]), yuzde(b["brut"]/b["toplam"])],
  f"Aktif kârlılığı = Net Kâr / Toplam Varlıklar = {tr(b['net_kar'])} / {tr(b['toplam'])} = {yuzde(v)}.",
  "Oran analizi - aktif kârlılığı", STIM)

v = (b["kvyk"] + b["uvyk"]) / b["toplam"]
q("oran_analizi", "Oran Analizi", G + "2026 yılı kaldıraç (yabancı kaynak / toplam kaynak) oranı yüzde kaçtır?",
  yuzde(v), [yuzde(b["ozkaynak"]/b["toplam"]), yuzde(b["kvyk"]/b["toplam"]), yuzde(b["duran"]/b["toplam"]), yuzde((b["kvyk"]+b["uvyk"])/b["ozkaynak"])],
  f"Kaldıraç oranı = (KVYK + UVYK) / Toplam Kaynaklar = ({tr(b['kvyk'])} + {tr(b['uvyk'])}) / {tr(b['toplam'])} = {yuzde(v)}.",
  "Oran analizi - kaldıraç oranı", STIM)

v = b["satis"] / b["alacak"]
q("oran_analizi", "Oran Analizi", G + "2026 yılı alacak devir hızı (dönem sonu alacaklara göre) kaçtır?",
  tr(v), [tr(b["smm"]/b["alacak"]), tr(b["satis"]/b["dv"]), tr(b["alacak"]/b["satis"]), tr(b["satis"]/b["toplam"])],
  f"Alacak devir hızı = Net Satışlar / Ticari Alacaklar = {tr(b['satis'])} / {tr(b['alacak'])} = {tr(v)}.",
  "Oran analizi - alacak devir hızı", STIM)

ort_stok = (a["stok"] + b["stok"]) / 2
v = b["smm"] / ort_stok
q("oran_analizi", "Oran Analizi", G + "2026 yılı stok devir hızı (ortalama stoka göre) kaçtır?",
  tr(v), [tr(b["satis"]/ort_stok), tr(b["smm"]/b["stok"]), tr(ort_stok/b["smm"]), tr(b["smm"]/a["stok"])],
  f"Ortalama stok = ({tr(a['stok'])} + {tr(b['stok'])}) / 2 = {tr(ort_stok)}. Stok devir hızı = SMM / Ortalama Stok = {tr(b['smm'])} / {tr(ort_stok)} = {tr(v)}.",
  "Oran analizi - stok devir hızı", STIM)

v = b["satis"] / b["toplam"]
q("oran_analizi", "Oran Analizi", G + "2026 yılı aktif devir hızı (dönem sonu varlıklara göre) kaçtır?",
  tr(v), [tr(b["toplam"]/b["satis"]), tr(b["satis"]/b["ozkaynak"]), tr(b["satis"]/b["duran"]), tr(b["smm"]/b["toplam"])],
  f"Aktif devir hızı = Net Satışlar / Toplam Varlıklar = {tr(b['satis'])} / {tr(b['toplam'])} = {tr(v)}.",
  "Oran analizi - aktif devir hızı", STIM)

v = b["dv"] / b["toplam"]
q("dikey_analiz", "Dikey (Yüzde) Analiz", G + "dikey analize göre 2026 yılında dönen varlıkların toplam varlıklar içindeki payı yüzde kaçtır?",
  yuzde(v), [yuzde(b["duran"]/b["toplam"]), yuzde(b["dv"]/b["kvyk"]), yuzde(b["stok"]/b["toplam"]), yuzde(a["dv"]/a["toplam"])],
  f"Dikey analizde bilanço kalemleri toplam varlıklara oranlanır: {tr(b['dv'])} / {tr(b['toplam'])} = {yuzde(v)}.",
  "Dikey analiz - varlık yapısı", STIM)

v = b["smm"] / b["satis"]
q("dikey_analiz", "Dikey (Yüzde) Analiz", G + "dikey analize göre 2026 yılında satışların maliyetinin net satışlar içindeki payı yüzde kaçtır?",
  yuzde(v), [yuzde(b["brut"]/b["satis"]), yuzde(b["faal_gider"]/b["satis"]), yuzde(a["smm"]/a["satis"]), yuzde(b["smm"]/b["toplam"])],
  f"Gelir tablosunda dikey analizde kalemler net satışlara oranlanır: {tr(b['smm'])} / {tr(b['satis'])} = {yuzde(v)}.",
  "Dikey analiz - gelir tablosu", STIM)

v = (b["satis"] - a["satis"]) / a["satis"]
q("karsilastirmali_analiz", "Karşılaştırmalı Analiz (Yatay)", G + "karşılaştırmalı analize göre net satışlardaki 2025-2026 değişimi yüzde kaçtır?",
  yuzde(v), [yuzde((b["net_kar"]-a["net_kar"])/a["net_kar"]), yuzde((b["toplam"]-a["toplam"])/a["toplam"]),
             yuzde((b["satis"]-a["satis"])/b["satis"]), yuzde(b["satis"]/a["satis"])],
  f"Yüzde değişim = (Cari yıl − Önceki yıl) / Önceki yıl = ({tr(b['satis'])} − {tr(a['satis'])}) / {tr(a['satis'])} = {yuzde(v)}.",
  "Karşılaştırmalı analiz - yüzde değişim", STIM)

v = b["net_kar"] / a["net_kar"] * 100
q("trend_analizi", "Trend (Eğilim) Analizi", G + "2025 yılı baz (100) alındığında 2026 net dönem kârının eğilim yüzdesi kaçtır?",
  tr(v), [tr(b["satis"]/a["satis"]*100), tr(a["net_kar"]/b["net_kar"]*100), tr((b["net_kar"]-a["net_kar"])/a["net_kar"]*100), tr(b["toplam"]/a["toplam"]*100)],
  f"Eğilim yüzdesi = (Cari yıl / Baz yıl) × 100 = ({tr(b['net_kar'])} / {tr(a['net_kar'])}) × 100 = {tr(v)}.",
  "Trend analizi - eğilim yüzdesi", STIM)

# ══ FİNANSAL TABLOLAR (8) ═════════════════════════════════════════════════
q("finansal_tablolar", "Finansal Tablolar",
  "TMS 1'e göre tam bir finansal tablo seti bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal durum tablosu, kâr veya zarar ve diğer kapsamlı gelir tablosu, özkaynak değişim tablosu, nakit akış tablosu ve dipnotlardan oluşur",
  ["Yalnızca finansal durum tablosu ile kâr veya zarar tablosundan oluşur; diğerleri isteğe bağlıdır",
   "Yalnızca vergi dairesine verilen beyanname ve eklerinden oluşan bir belge setini ifade etmektedir",
   "Yalnızca nakit akış tablosundan oluşur; diğer tablolar yalnızca büyük işletmelerce hazırlanır",
   "Dipnotlar finansal tablo setinin parçası değildir; yalnızca isteğe bağlı bir açıklama metnidir"],
  "TMS 1: tam bir finansal tablo seti; finansal durum tablosu, kâr veya zarar ve diğer kapsamlı gelir tablosu, özkaynak değişim tablosu, nakit akış tablosu ve dipnotlardan oluşur.",
  "TMS 1 - finansal tablo seti", None, "easy")

q("finansal_tablolar", "Finansal Tablolar",
  "TMS 1'e göre varlık ve borçların mahsup edilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir standart izin vermedikçe veya zorunlu kılmadıkça varlıklar ile borçlar mahsup edilmez",
  ["Varlıklar ile borçlar her hâlde net tutar üzerinden mahsup edilerek gösterilmek zorundadır",
   "Mahsup tümüyle işletmenin takdirine bırakılmış olup standartlarda hiçbir kural bulunmamaktadır",
   "Mahsup yalnızca gelir ve giderler için yasaktır; varlık ve borçlar serbestçe netleştirilebilir",
   "Varlık ve borçların mahsubu yalnızca vergi idaresinin izniyle ve yıl sonunda yapılabilmektedir"],
  "TMS 1: bir TFRS zorunlu kılmadıkça veya izin vermedikçe varlıklar ile borçlar, gelirler ile giderler mahsup edilmez; brüt gösterim esastır.",
  "TMS 1 - mahsup yasağı")

q("finansal_tablolar", "Finansal Tablolar",
  "Finansal durum tablosunda dönen varlık ayrımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Normal faaliyet döngüsü içinde veya raporlama tarihinden sonraki on iki ayda paraya çevrilmesi beklenen varlıklar dönen varlıktır",
  ["Bir varlığın dönen olarak sınıflandırılması yalnızca fiziki olarak taşınabilir olmasına bağlıdır",
   "Tüm varlıklar duran varlık olarak sınıflandırılır; dönen varlık ayrımı standartlarda yer almaz",
   "Dönen varlık ayrımı yalnızca stoklar için geçerli olup diğer kalemleri hiç kapsamamaktadır",
   "Varlıkların dönen ya da duran olması işletmenin her yıl serbestçe değiştirebileceği bir tercihtir"],
  "TMS 1: bir varlık, normal faaliyet döngüsü içinde paraya çevrilmesi/satılması/tüketilmesi bekleniyorsa, ticari amaçla elde tutuluyorsa veya raporlama döneminden sonra on iki ay içinde paraya çevrilmesi bekleniyorsa dönen varlık olarak sınıflandırılır.",
  "TMS 1 - dönen/duran ayrımı")

q("finansal_tablolar", "Finansal Tablolar",
  "Özkaynak değişim tablosunun işlevi bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönem başı ve dönem sonu özkaynak tutarları arasındaki değişimin kaynaklarını gösterir",
  ["İşletmenin dönem içindeki nakit giriş ve çıkışlarını faaliyet türlerine göre ayırarak gösterir",
   "İşletmenin varlık ve kaynaklarının belirli bir tarihteki durumunu özetleyerek raporlamaktadır",
   "Yalnızca işletmenin ödediği vergileri ve vergi karşılıklarını ayrıntılı biçimde göstermektedir",
   "İşletmenin gelecek dönemlere ilişkin kâr tahminlerini ve bütçesini ortaya koyan bir tablodur"],
  "Özkaynak değişim tablosu, dönem başı ve dönem sonu özkaynak tutarları arasındaki değişimi (kâr/zarar, sermaye artırımı, kâr dağıtımı, diğer kapsamlı gelir vb.) kalem bazında gösterir.",
  "TMS 1 - özkaynak değişim tablosu")

q("finansal_tablolar", "Finansal Tablolar",
  "Finansal tabloların hazırlanmasında tahakkuk esası bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit akış tablosu dışındaki finansal tablolar tahakkuk esasına göre hazırlanır",
  ["Tüm finansal tablolar nakit esasına göre, yalnızca tahsilat ve ödemeler dikkate alınarak hazırlanır",
   "Tahakkuk esası yalnızca vergi hesaplamasında kullanılır; finansal raporlamada uygulanmamaktadır",
   "Nakit akış tablosu tahakkuk esasına, diğer tüm tablolar ise nakit esasına göre düzenlenmektedir",
   "Tahakkuk ve nakit esası arasında hiçbir fark bulunmadığından ayrım pratikte anlamsızdır"],
  "TMS 1: işletmeler nakit akış tablosu hariç, finansal tablolarını muhasebenin tahakkuk esasına göre düzenler; gelir ve giderler tahsilat/ödemeden bağımsız olarak ait olduğu dönemde raporlanır.",
  "TMS 1 - tahakkuk esası")

q("finansal_tablolar", "Finansal Tablolar",
  "İşletmenin sürekliliği varsayımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal tablolar, işletmenin faaliyetini sürdüreceği varsayımıyla hazırlanır; aksi hâlde bu durum açıklanır",
  ["Finansal tablolar her hâlde işletmenin tasfiye edileceği varsayımıyla ve tasfiye değerleriyle hazırlanır",
   "Süreklilik varsayımı yalnızca büyük ölçekli şirketleri bağlar; küçük işletmeler bundan muaftır",
   "Süreklilik varsayımı ortadan kalksa dahi finansal tablolar hiçbir değişiklik olmaksızın aynen hazırlanır",
   "Süreklilik varsayımı yalnızca vergi mevzuatının konusu olup muhasebe standartlarında yer almaz"],
  "TMS 1: finansal tablolar, işletmenin sürekliliği esas alınarak hazırlanır. Süreklilik konusunda ciddi şüphe doğuran belirsizlikler varsa bu belirsizlikler açıklanır; süreklilik esası uygun değilse bu durum ve kullanılan esas açıklanır.",
  "TMS 1 - işletmenin sürekliliği")

q("finansal_tablolar", "Finansal Tablolar",
  "Aşağıdakilerden hangileri TMS 1'e göre tam bir finansal tablo setinde yer alır?\n\nI. Finansal durum tablosu\n\nII. Nakit akış tablosu\n\nIII. Dipnotlar",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 1'e göre tam set; finansal durum tablosu (I), nakit akış tablosu (II) ve dipnotların (III) yanı sıra kâr veya zarar ve diğer kapsamlı gelir tablosu ile özkaynak değişim tablosunu içerir. Üçü de sette yer alır.",
  "TMS 1 - finansal tablo seti")

q("finansal_tablolar", "Finansal Tablolar",
  "TMS 1'e göre aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Nakit akış tablosu dışındaki tablolar tahakkuk esasına göre hazırlanır\n\nII. Cari dönem tutarları için önceki döneme ilişkin karşılaştırmalı bilgi sunulur\n\nIII. Varlıklar ile borçlar kural olarak mahsup edilerek net gösterilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Tablolar tahakkuk esasına göre hazırlanır (I) ve karşılaştırmalı bilgi sunulur (II). Ancak bir TFRS izin vermedikçe mahsup yapılmaz; brüt gösterim esastır, bu nedenle III yanlıştır.",
  "TMS 1 - genel ilkeler")

# ══ ORAN ANALİZİ — bağımsız (6) ═══════════════════════════════════════════
dv_, kv_ = 750, 500
q("oran_analizi", "Oran Analizi",
  f"Dönen varlıkları {tr(dv_)} bin TL, kısa vadeli yabancı kaynakları {tr(kv_)} bin TL olan bir işletmenin cari oranı kaçtır?",
  tr(dv_/kv_), [tr(kv_/dv_), tr(dv_-kv_), tr((dv_-kv_)/kv_), tr(dv_/(dv_+kv_))],
  f"Cari oran = Dönen Varlıklar / KVYK = {tr(dv_)} / {tr(kv_)} = {tr(dv_/kv_)}. Net işletme sermayesi ise farktır ({tr(dv_-kv_)} bin TL) ve oran değildir.",
  "Oran analizi - cari oran")

q("oran_analizi", "Oran Analizi",
  "Cari oranın yorumu bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin kısa vadeli borçlarını dönen varlıklarıyla karşılama gücünü gösterir",
  ["İşletmenin uzun vadeli borçlarını duran varlıklarıyla karşılama gücünü ölçen bir mali yapı oranıdır",
   "İşletmenin bir dönemde elde ettiği kârın satışlara oranını gösteren bir kârlılık ölçüsüdür",
   "İşletmenin varlıklarını ne kadar hızlı paraya çevirdiğini gösteren bir faaliyet oranıdır",
   "İşletmenin özkaynaklarının toplam kaynaklara oranını gösteren bir yapı göstergesidir"],
  "Cari oran bir likidite oranıdır; dönen varlıkların kısa vadeli yabancı kaynaklara oranı olarak kısa vadeli borç ödeme gücünü ölçer.",
  "Oran analizi - likidite oranları", None, "easy")

q("oran_analizi", "Oran Analizi",
  "Asit-test oranının cari orandan farkı bakımından aşağıdakilerden hangisi doğrudur?",
  "Asit-test oranında stoklar dönen varlıklardan düşülür; böylece daha temkinli bir likidite ölçüsü elde edilir",
  ["Asit-test oranında stoklar dönen varlıklara ayrıca eklenerek daha geniş bir likidite ölçüsü bulunur",
   "Asit-test oranı ile cari oran aynı formülle hesaplanır; aralarında hiçbir fark bulunmamaktadır",
   "Asit-test oranında hazır değerler dönen varlıklardan düşülür ve yalnızca stoklar dikkate alınır",
   "Asit-test oranı bir kârlılık oranı olup cari oran gibi likiditeyi ölçmek için kullanılmamaktadır"],
  "Asit-test oranı = (Dönen Varlıklar − Stoklar) / KVYK. Stoklar en az likit dönen varlık kabul edildiğinden dışlanır; bu nedenle cari orandan daha temkinli bir ölçüdür.",
  "Oran analizi - asit-test oranı")

sat_, ort_alacak = 1800, 225
v = sat_ / ort_alacak
q("oran_analizi", "Oran Analizi",
  f"Net satışları {tr(sat_)} bin TL, ortalama ticari alacakları {tr(ort_alacak)} bin TL olan bir işletmenin alacak devir hızı kaçtır?",
  tr(v), [tr(ort_alacak/sat_), tr(sat_/(ort_alacak*2)), tr(360/v), tr(sat_-ort_alacak)],
  f"Alacak devir hızı = Net Satışlar / Ortalama Ticari Alacaklar = {tr(sat_)} / {tr(ort_alacak)} = {tr(v)}. Alacakların ortalama tahsil süresi ise 360 / {tr(v)} = {tr(360/v)} gündür.",
  "Oran analizi - alacak devir hızı")

q("oran_analizi", "Oran Analizi",
  "Stok devir hızı bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Satışların maliyetinin ortalama stoka bölünmesiyle bulunur\n\nII. Oranın yükselmesi stokta bekleme süresinin kısaldığını gösterir\n\nIII. Bir likidite oranı olup kısa vadeli borç ödeme gücünü doğrudan ölçer",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Stok devir hızı SMM / Ortalama Stok ile bulunur (I) ve yükselmesi stokların daha hızlı tükendiğini gösterir (II). Ancak bu bir faaliyet (devir hızı) oranıdır; likidite oranı değildir, bu nedenle III yanlıştır.",
  "Oran analizi - stok devir hızı")

q("oran_analizi", "Oran Analizi",
  "Aşağıdakilerden hangileri likidite oranlarındandır?\n\nI. Cari oran\n\nII. Asit-test oranı\n\nIII. Özkaynak kârlılığı",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Cari oran (I) ve asit-test oranı (II) likidite oranlarıdır. Özkaynak kârlılığı (III) ise bir kârlılık oranıdır, likidite ölçmez.",
  "Oran analizi - oran grupları")

# ══ KARŞILAŞTIRMALI / DİKEY / TREND — bağımsız (6) ════════════════════════
e1, e2 = 480, 600
q("karsilastirmali_analiz", "Karşılaştırmalı Analiz (Yatay)",
  f"Bir kalemin tutarı önceki dönemde {tr(e1)} bin TL, cari dönemde {tr(e2)} bin TL'dir. Karşılaştırmalı analizde yüzde değişim kaçtır?",
  yuzde((e2-e1)/e1), [yuzde((e2-e1)/e2), yuzde(e2/e1), yuzde(e1/e2), yuzde((e2-e1)/(e1+e2))],
  f"Yüzde değişim = (Cari − Önceki) / Önceki = ({tr(e2)} − {tr(e1)}) / {tr(e1)} = {yuzde((e2-e1)/e1)}. Payda daima önceki dönem tutarıdır.",
  "Karşılaştırmalı analiz - yüzde değişim")

q("karsilastirmali_analiz", "Karşılaştırmalı Analiz (Yatay)",
  "Karşılaştırmalı tablolar analizinin amacı bakımından aşağıdakilerden hangisi doğrudur?",
  "Aynı kalemin dönemler arasındaki mutlak ve yüzde değişimini inceleyerek eğilimi ortaya koyar",
  ["Aynı dönemde farklı kalemlerin toplam içindeki yüzde paylarını hesaplayarak yapıyı ortaya koyar",
   "Bir baz yıl seçerek tüm dönemleri bu yıla göre endeksleyip uzun dönemli eğilimi hesaplamaktadır",
   "İki kalemin birbirine bölünmesiyle elde edilen oranlar aracılığıyla mali durumu değerlendirir",
   "İşletmenin gelecek dönemdeki nakit akışlarını tahmin ederek bütçe hazırlamayı amaçlamaktadır"],
  "Karşılaştırmalı (yatay) analizde aynı kalemin ardışık dönemlerdeki tutarları karşılaştırılır; mutlak ve yüzde değişim hesaplanarak eğilim değerlendirilir. Yüzde payları dikey analizin, baz yıl endeksleri trend analizinin konusudur.",
  "Karşılaştırmalı analiz - amaç")

k_, t_ = 360, 1200
q("dikey_analiz", "Dikey (Yüzde) Analiz",
  f"Toplam varlıkları {tr(t_)} bin TL olan bir işletmede stoklar {tr(k_)} bin TL'dir. Dikey analize göre stokların payı yüzde kaçtır?",
  yuzde(k_/t_), [yuzde(t_/k_), yuzde(k_/(t_-k_)), yuzde((t_-k_)/t_), yuzde(k_/t_/2)],
  f"Stokların toplam varlıklar içindeki payı {tr(k_)} / {tr(t_)} = {k_/t_:.2f} hesabıyla bulunur; bu oran {yuzde(k_/t_)}'tir.",
  "Dikey analiz - yüzde pay")

q("dikey_analiz", "Dikey (Yüzde) Analiz",
  "Analiz teknikleri bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Dikey analizde bilançoda toplam varlıklar 100 kabul edilir\n\nII. Dikey analizde gelir tablosunda net satışlar 100 kabul edilir\n\nIII. Dikey analizde bir baz yıl seçilerek diğer yıllar ona endekslenir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Dikey analizde bilançoda toplam varlıklar (I), gelir tablosunda net satışlar (II) 100 kabul edilir. Baz yıl seçip endeksleme (III) ise trend analizinin yöntemidir, dikey analizin değil.",
  "Dikey analiz - temel kalem")

bz, cr = 250, 400
q("trend_analizi", "Trend (Eğilim) Analizi",
  f"Baz yılda {tr(bz)} bin TL olan bir kalem cari yılda {tr(cr)} bin TL'dir. Baz yıl 100 kabul edildiğinde cari yılın eğilim yüzdesi kaçtır?",
  tr(cr/bz*100), [tr(bz/cr*100), tr((cr-bz)/bz*100), tr((cr-bz)/cr*100), tr(cr-bz)],
  f"Eğilim yüzdesi = (Cari yıl / Baz yıl) × 100 = ({tr(cr)} / {tr(bz)}) × 100 = {tr(cr/bz*100)}. Artış oranı ise {tr((cr-bz)/bz*100)}%'tir; ikisi karıştırılmamalıdır.",
  "Trend analizi - eğilim yüzdesi")

q("trend_analizi", "Trend (Eğilim) Analizi",
  "Trend (eğilim yüzdeleri) analizinde baz yıl seçimi bakımından aşağıdakilerden hangisi doğrudur?",
  "Baz yıl, işletme açısından olağan (normal) kabul edilen bir yıl olmalıdır; aksi hâlde eğilim yanıltıcı olur",
  ["Baz yıl her hâlde en yüksek kârın elde edildiği yıl olarak seçilmek zorunda tutulmaktadır",
   "Baz yıl seçiminin sonuç üzerinde hiçbir etkisi bulunmadığından rastgele belirlenebilmektedir",
   "Baz yıl daima analiz edilen dönemin son yılı olarak alınır; ilk yıl baz olarak kullanılamaz",
   "Trend analizinde baz yıl kavramı yoktur; her yıl bir öncekiyle ayrı ayrı karşılaştırılmaktadır"],
  "Trend analizinde baz yıl 100 kabul edilir ve diğer yıllar buna endekslenir. Baz yılın olağanüstü (çok iyi veya çok kötü) bir yıl olması tüm eğilimi yanıltıcı hâle getirir; bu nedenle normal bir yıl seçilmelidir.",
  "Trend analizi - baz yıl seçimi")

# ══ NAKİT AKIM ANALİZİ (6) ════════════════════════════════════════════════
q("nakit_akim_analizi", "Nakit Akım Analizi",
  "Nakit akış tablosunun bölümleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit akışları işletme, yatırım ve finansman faaliyetleri olarak üç bölümde raporlanır",
  ["Nakit akışları yalnızca tahsilat ve ödeme olmak üzere iki bölümde toplanarak raporlanmaktadır",
   "Nakit akışları dönen ve duran varlıklar biçiminde ikiye ayrılarak bilanço düzeninde sunulur",
   "Nakit akış tablosunda bölüm ayrımı yapılmaz; tüm hareketler tek bir toplam hâlinde gösterilir",
   "Nakit akışları kısa vadeli ve uzun vadeli olmak üzere vade esasına göre iki bölümde raporlanır"],
  "TMS 7: nakit akış tablosu, dönem içindeki nakit akışlarını işletme, yatırım ve finansman faaliyetleri bazında sınıflandırarak raporlar.",
  "TMS 7 - nakit akış tablosu bölümleri", None, "easy")

q("nakit_akim_analizi", "Nakit Akım Analizi",
  "Maddi duran varlık satın alınması bakımından nakit akış tablosunda hangi bölümde raporlanır?",
  "Maddi duran varlık alımı, yatırım faaliyetlerinden kaynaklanan nakit çıkışı olarak raporlanır",
  ["İşletme faaliyetlerinden nakit çıkışı olarak raporlanır; yatırım bölümüyle ilgisi bulunmamaktadır",
   "Finansman faaliyetlerinden nakit çıkışı olarak raporlanır; yatırım faaliyeti sayılmamaktadır",
   "Nakit akış tablosunda hiç raporlanmaz; yalnızca bilançoda gösterilmesi yeterli görülmektedir",
   "İşletme faaliyetlerinden nakit girişi olarak raporlanır; varlık edinimi giriş doğurmaktadır"],
  "TMS 7: uzun vadeli varlıkların edinimi ve elden çıkarılmasına ilişkin nakit akışları yatırım faaliyetlerinde sınıflandırılır; MDV alımı yatırım faaliyetlerinden nakit çıkışıdır.",
  "TMS 7 - yatırım faaliyetleri")

q("nakit_akim_analizi", "Nakit Akım Analizi",
  "İşletmenin kredi kullanması ve kredi anaparası ödemesi bakımından nakit akış tablosunda hangi bölümde raporlanır?",
  "Kredi kullanımı nakit girişi, anapara ödemesi nakit çıkışı olarak finansman faaliyetlerinde raporlanır",
  ["İşletme faaliyetlerinde raporlanır; borçlanma işletmenin olağan faaliyeti sayılmaktadır",
   "Yatırım faaliyetlerinde raporlanır; kredi kullanımı bir yatırım hareketi kabul edilmektedir",
   "Nakit akış tablosunda gösterilmez; yalnızca dipnotlarda açıklanması yeterli görülmektedir",
   "Kredi kullanımı finansman, anapara ödemesi ise işletme faaliyetlerinde ayrı ayrı raporlanır"],
  "TMS 7: işletmenin özkaynak ve borçlanma yapısında değişiklik doğuran nakit akışları finansman faaliyetlerinde sınıflandırılır; kredi kullanımı nakit girişi, anapara ödemesi nakit çıkışıdır.",
  "TMS 7 - finansman faaliyetleri")

q("nakit_akim_analizi", "Nakit Akım Analizi",
  "İşletme faaliyetlerinden nakit akışlarının sunumunda dolaylı yöntem bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönem kâr veya zararı; nakit çıkışı gerektirmeyen kalemler ve işletme sermayesi değişimleri için düzeltilir",
  ["Brüt nakit tahsilat ve ödemeler ayrı ayrı gösterilir; dönem kârından hareket edilmemektedir",
   "Yalnızca yatırım faaliyetleri düzeltilir; işletme faaliyetleri için dolaylı yöntem kullanılmaz",
   "Dolaylı yöntemde amortisman gibi nakit çıkışı gerektirmeyen giderler kârdan ayrıca düşülür",
   "Dolaylı yöntem TMS 7'de düzenlenmemiş olup yalnızca doğrudan yöntem kullanılabilmektedir"],
  "TMS 7: dolaylı yöntemde işletme faaliyetlerinden nakit akışı, dönem kâr/zararının amortisman gibi gayrinakdi kalemler ile işletme sermayesi kalemlerindeki değişimler için düzeltilmesiyle bulunur. Amortisman nakit çıkışı gerektirmediğinden kâra eklenir.",
  "TMS 7 - dolaylı yöntem")

nk, amort, alacak_artis = 200, 60, 40
v = nk + amort - alacak_artis
q("nakit_akim_analizi", "Nakit Akım Analizi",
  f"Dönem net kârı {tr(nk)} bin TL, amortisman gideri {tr(amort)} bin TL ve ticari alacaklardaki artış {tr(alacak_artis)} bin TL'dir. Başka düzeltme yoksa dolaylı yönteme göre işletme faaliyetlerinden nakit akışı kaç bin TL'dir?",
  tr(v), [tr(nk - amort - alacak_artis), tr(nk + amort + alacak_artis), tr(nk - amort + alacak_artis), tr(nk)],
  f"Amortisman nakit çıkışı gerektirmediğinden kâra eklenir; ticari alacaklardaki artış nakde dönüşmemiş hasılatı gösterdiğinden düşülür: {tr(nk)} + {tr(amort)} − {tr(alacak_artis)} = {tr(v)} bin TL.",
  "TMS 7 - dolaylı yöntem hesabı")

q("nakit_akim_analizi", "Nakit Akım Analizi",
  "Aşağıdakilerden hangileri nakit akış tablosunda yatırım faaliyeti olarak sınıflandırılır?\n\nI. Maddi duran varlık satın alınması\n\nII. Maddi duran varlık satılması\n\nIII. Kredi anaparasının ödenmesi",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Uzun vadeli varlıkların edinimi (I) ve elden çıkarılması (II) yatırım faaliyetidir. Kredi anaparasının ödenmesi (III) ise borçlanma yapısını değiştirdiğinden finansman faaliyetidir.",
  "TMS 7 - faaliyet sınıflandırması")

print("TOPLAM:", len(Q))

# ══ BUILD ═════════════════════════════════════════════════════════════════
def gen_letters(n, seed):
    r = random.Random(seed)
    base = ["ABCDE"[i % 5] for i in range(n)]
    while True:
        r.shuffle(base)
        if all(not (base[i] == base[i-1] == base[i-2]) for i in range(2, len(base))):
            return base

def emit(items, prefix, seed):
    letters = gen_letters(len(items), seed)
    out = []
    for i, it in enumerate(items):
        ans = letters[i]
        ch = {ans: it["correct"]}
        for k, d in zip([k for k in "ABCDE" if k != ans], it["distractors"]):
            ch[k] = d
        assert len(set(ch.values())) == 5, f"{prefix}-{i+1}: şıklar tekrarlanıyor"
        row = {
            "id": f"{prefix}-{i+1:04d}", "lessonId": L, "topicId": it["topic"],
            "question": it["stem"], "choices": ch, "correctAnswer": ans,
            "explanation": it["why"],
            "source": {"kind": "generated", "styleRef": "2026/1 test biçimi",
                       "legislationRef": it["ref"]},
            "tags": ["Özgün Soru", "2026 Formatı", "Bölüm Havuzu", it["label"]],
            "difficulty": it["difficulty"], "updatedAt": "2026-07-15T00:00:00Z",
            "examPeriod": "2026/1 formatına uyumlu", "legislationVersion": "2026-07-15",
            "sourceUpdatedAt": "2026-07-15T00:00:00Z", "isPremium": False, "isActive": True,
        }
        if it["stim"]: row["stimulusId"] = it["stim"]
        out.append(row)
    return out

if __name__ == "__main__":
    assert len(Q) == 40, f"40 olmalı, şu an {len(Q)}"
    root = Path(__file__).resolve().parents[3]
    targets = (
        root / "content" / "yeterlilik",
        root.parent / "smmm_sgs_pratik" / "assets" / "content" / "yeterlilik",
    )

    # stimulus'u iki içerik kopyasında da ekle/güncelle
    for target in targets:
        target.mkdir(parents=True, exist_ok=True)
        stimulus_path = target / "stimuli.json"
        st = json.loads(stimulus_path.read_text(encoding="utf-8"))
        st = [s for s in st if s["id"] != STIM]
        st.append({"id": STIM, "title": "GHI İşletmesi — Karşılaştırmalı Finansal Veriler",
                   "kind": "table", "bodyMarkdown": STIM_BODY,
                   "caption": "Tutarlar bin TL'dir.", "updatedAt": "2026-07-15T00:00:00Z"})
        stimulus_path.write_text(json.dumps(st, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"stimulus yazıldı: {STIM} ({len(st)} stimulus)")

    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in Q if len(MARK.findall(x["stem"])) >= 2]
    duz = [x for x in Q if len(MARK.findall(x["stem"])) < 2]
    t2 = [x for i, x in enumerate(duz) if i % 2 == 0] + [x for i, x in enumerate(onc) if i % 2 == 0]
    t3 = [x for i, x in enumerate(duz) if i % 2 == 1] + [x for i, x in enumerate(onc) if i % 2 == 1]
    print(f"öncüllü {len(onc)} → t2:{len([x for x in t2 if x in onc])} t3:{len([x for x in t3 if x in onc])}")
    for items, name, prefix, seed in ((t2, "questions_analiz_test2_2026.json", "analiz-t2", 20260805),
                                      (t3, "questions_analiz_test3_2026.json", "analiz-t3", 20260806)):
        data = emit(items, prefix, seed)
        for target in targets:
            (target / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        ns = sum(1 for x in data if x.get("stimulusId"))
        print(f"{name}: {len(data)} soru ({ns} ortak tabloya bağlı) | harf {''.join(x['correctAnswer'] for x in data)}")
