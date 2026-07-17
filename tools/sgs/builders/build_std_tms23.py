# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / TMS 23 Borçlanma Maliyetleri — 60 soru.
Kaynak: KGK TMS 23.

★ Gerçek sınav kalibrasyonu (çıkmış sorulardan):
  · 2026/1 s.50 — aktifleştirme oranı × harcama × süre hesabı (kredi 10.000.000,
    faiz 1.000.000 → oran %10; 1 Temmuz'da 6.000.000 harcama → 6.000.000×%10×6/12)
  · 2025      — öncüllü: "hangileri özellikli varlıktır?" (barajlar ↔ turşular)
  · 2014-16   — inşaata uzun süre ara verilmesi → aktifleştirmeye ara verme

KURAL: doğru şık KISA (≤~110), çeldiriciler UZUN (~90-115) → length-tell sıfır.
⚠ Faiz/aktifleştirme oranı SÖZLEŞMEYE özgüdür ve soru kökünde verilir → yıla bağlı değil.
"""
import json, random, re

DERS, KONU = "muhasebe_standartlari", "tms_23_borclanma_maliyetleri"
PREFIX, SEED = "std-tms23-gen", 20260721
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/tms_23_borclanma_maliyetleri.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9: v = round(v)
    return f"{v:,}".replace(",", ".")

# ── A. Tanım, kapsam, özellikli varlık (16) ────────────────────────────────
q("TMS 23'e göre borçlanma maliyetleri bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin borçlanmalarıyla ilgili katlandığı faiz ve diğer giderlerdir",
  ["İşletmenin ortaklarına dağıttığı kâr payı tutarlarını ifade eden bir kavram niteliğindedir",
   "İşletmenin satın aldığı stoklar için ödediği bedelleri ifade eden bir kavramı karşılamaktadır",
   "İşletmenin çalışanlarına ödediği ücret ve benzeri faydaları ifade eden bir kavramdır",
   "Borçlanma maliyeti kavramı TMS 23'te tanımlanmamış olup uygulamada kullanılmamaktadır"],
  "TMS 23: borçlanma maliyetleri, bir işletme tarafından yapılan borçlanmalarla ilgili olarak katlanılan faiz ve diğer giderlerdir.",
  "TMS 23 - borçlanma maliyeti tanımı")

q("TMS 23'ün temel ilkesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Özellikli varlıkla doğrudan ilişkilendirilebilen borçlanma maliyetleri varlığın maliyetine dâhil edilir; diğerleri gider yazılır",
  ["Tüm borçlanma maliyetleri her hâlde aktifleştirilmek zorunda olup gider yazılamamaktadır",
   "Tüm borçlanma maliyetleri her hâlde gider yazılmak zorunda olup aktifleştirilememektedir",
   "Borçlanma maliyetleri her hâlde doğrudan özkaynaklardan indirilmek zorunda tutulmaktadır",
   "TMS 23'ün belirlenmiş bir temel ilkesi bulunmayıp uygulama serbest bırakılmış bulunmaktadır"],
  "TMS 23: bir özellikli varlığın satın alınması, inşası veya üretimi ile doğrudan ilişkilendirilebilen borçlanma maliyetleri, ilgili özellikli varlığın maliyetinin bir parçasını oluşturur. Diğer borçlanma maliyetleri gider olarak muhasebeleştirilir.",
  "TMS 23 - temel ilke")

q("TMS 23'e göre özellikli varlık bakımından aşağıdakilerden hangisi doğrudur?",
  "Amaçlanan kullanıma veya satışa hazır duruma getirilebilmesi zorunlu olarak önemli bir zaman dilimini gerektiren varlıktır",
  ["İşletmenin sahip olduğu tüm duran varlıkları kapsayan geniş bir kavramı ifade etmektedir",
   "İşletmenin kısa sürede üretip sattığı tüm stokları kapsayan bir kavramı karşılamaktadır",
   "İşletmenin yalnızca finansal varlıklarını kapsayan dar bir kavramı ifade etmek durumundadır",
   "Özellikli varlık kavramı TMS 23'te tanımlanmamış olup uygulamada kullanılmamaktadır"],
  "TMS 23: özellikli varlık, amaçlanan kullanıma veya satışa hazır duruma getirilebilmesi zorunlu olarak önemli bir zaman dilimini gerektiren varlıklardır.",
  "TMS 23 - özellikli varlık tanımı")

q("Aşağıdakilerden hangisi TMS 23'e göre özellikli varlık olabilir?",
  "İnşası birkaç yıl süren bir baraj",
  ["Kısa bir üretim döneminde çok sayıda ve tekrarlanan biçimde imal edilen seri üretim mamulleri",
   "Edinildiği anda amaçlanan kullanıma hazır olan ve hemen faaliyete alınan bir taşıt aracı",
   "Elde edildiğinde satışa hazır durumda bulunan ve beklemeden elden çıkarılan ticari mallar",
   "İşletmenin kısa vadeli nakit yönetimi amacıyla elde tuttuğu likit finansal yatırım araçları"],
  "TMS 23: koşullara bağlı olarak stoklar, imalat tesisleri, enerji üretim tesisleri, maddi olmayan duran varlıklar ve yatırım amaçlı gayrimenkuller özellikli varlık olabilir. Belirleyici olan, hazır duruma getirilmesinin ZORUNLU olarak önemli bir zaman dilimini gerektirmesidir. Baraj bu ölçütü karşılar.",
  "TMS 23 - özellikli varlık örneği")

q("Aşağıdakilerden hangisi TMS 23'e göre özellikli varlık DEĞİLDİR?",
  "Kısa sürede ve tekrarlanan biçimde çok sayıda üretilen stoklar",
  ["İnşası zorunlu olarak birkaç yıl süren ve bu süre boyunca kullanılamayan enerji üretim tesisi",
   "Geliştirilmesi uzun bir zaman dilimini zorunlu kılan ve o süre içinde kullanılamayan yazılım",
   "İnşaatı önemli bir zaman dilimi gerektiren ve tamamlanmadan kullanılamayan imalat tesisi",
   "Olgunlaşması zorunlu olarak uzun süre alan ve o süreden önce satılamayan nitelikteki stoklar"],
  "TMS 23: kısa bir zaman diliminde ve tekrarlanan biçimde çok sayıda üretilen stoklar özellikli varlık DEĞİLDİR. Aynı biçimde, elde edildiğinde amaçlanan kullanıma veya satışa hazır olan varlıklar da özellikli varlık değildir.",
  "TMS 23 - özellikli varlık olmayan")

q("Finansal varlıklar ve gerçeğe uygun değerle ölçülen biyolojik varlıklar bakımından aşağıdakilerden hangisi doğrudur?",
  "Bu varlıklar özellikli varlık değildir; borçlanma maliyeti aktifleştirilmez",
  ["Bu varlıklar her hâlde özellikli varlık sayılıp borçlanma maliyeti aktifleştirilmek zorundadır",
   "Bu varlıklar için borçlanma maliyeti her hâlde iki katı olarak aktifleştirilmek zorunda kalınır",
   "Bu varlıklar hiçbir hâlde muhasebeleştirilemez; yalnızca dipnotlarda açıklanmaktadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: finansal varlıklar ve kısa sürede üretilen/imal edilen stoklar özellikli varlık değildir. Ayrıca gerçeğe uygun değerinden ölçülen varlıklar (canlı varlıklar gibi) için borçlanma maliyetlerinin aktifleştirilmesi zorunlu değildir.",
  "TMS 23 - kapsam dışı varlıklar")

q("Borçlanma maliyetlerinin kapsamına giren unsurlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Etkin faiz yöntemiyle hesaplanan faiz gideri, kira yükümlülüğü faizi ve faiz düzeltmesi sayılan kur farkları dâhildir",
  ["Yalnızca sözleşmede yazılı nominal faiz tutarı kapsama girer; başka hiçbir unsur dâhil değildir",
   "Yalnızca bankalara ödenen komisyon giderleri kapsama girer; faiz hiçbir hâlde dâhil edilmez",
   "İşletmenin tüm genel yönetim giderleri de borçlanma maliyeti sayılarak kapsama alınmaktadır",
   "Borçlanma maliyetlerinin kapsamı TMS 23'te düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 23: borçlanma maliyetleri; TFRS 9'daki etkin faiz yöntemi kullanılarak hesaplanan faiz giderini, TFRS 16 uyarınca kira yükümlülüklerine ilişkin faizi ve yabancı para borçlanmalarında faiz maliyetlerine ilişkin düzeltme olarak dikkate alınan kur farklarını içerir.",
  "TMS 23 - kapsam")

q("Yabancı para borçlanmalarından doğan kur farkları bakımından aşağıdakilerden hangisi doğrudur?",
  "Faiz maliyetlerine ilişkin bir düzeltme olarak dikkate alındıkları ölçüde borçlanma maliyetidir",
  ["Kur farklarının tamamı her hâlde borçlanma maliyeti sayılıp aktifleştirilmek zorundadır",
   "Kur farkları hiçbir hâlde borçlanma maliyeti sayılamaz; tamamı gider yazılmak zorundadır",
   "Kur farkları her hâlde doğrudan özkaynaklardan indirilmek zorunda olan kalemleri ifade eder",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: yabancı para ile borçlanmalarda, faiz maliyetleri ile ilgili düzeltme olarak dikkate alındıkları ölçüde kur farkları borçlanma maliyetlerine dâhildir. Kur farkının tamamı değil, yalnız bu ölçüdeki kısmı.",
  "TMS 23 - kur farkları")

q("Özellikli varlıkla doğrudan ilişkilendirilebilen borçlanma maliyeti bakımından aşağıdakilerden hangisi doğrudur?",
  "Özellikli varlığa yapılan harcama olmasaydı katlanılmayacak olan borçlanma maliyetleridir",
  ["İşletmenin tüm borçlanmalarından doğan maliyetlerin tamamını kapsayan bir kavramı ifade eder",
   "Yalnızca banka kredilerinden doğan maliyetleri kapsayan ve tahvilleri dışlayan bir kavramdır",
   "Yalnızca yabancı para borçlanmalarından doğan maliyetleri kapsayan dar bir kavram niteliğindedir",
   "Bu kavram TMS 23'te tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmış bulunmaktadır"],
  "TMS 23: bir özellikli varlıkla doğrudan ilişkilendirilebilen borçlanma maliyetleri, özellikli varlığa ilişkin harcama yapılmamış olsaydı katlanılmayacak olan borçlanma maliyetleridir.",
  "TMS 23 - doğrudan ilişkilendirme")

q("Aşağıdakilerden hangileri TMS 23'e göre özellikli varlık tanımını karşılar?\n\nI. İnşası zorunlu olarak iki yıl süren baraj\n\nII. İki ayda fermantasyonu tamamlanan turşular\n\nIII. Kurulumu birkaç yıl alan enerji üretim tesisi",
  "I ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "Yalnız III"],
  "Özellikli varlık, hazır duruma getirilmesi ZORUNLU olarak önemli bir zaman dilimini gerektiren varlıktır. Baraj (I) ve enerji üretim tesisi (III) bu ölçütü karşılar. İki ayda fermantasyonu tamamlanan turşular (II) ise kısa sürede üretilen stoktur; özellikli varlık değildir.",
  "TMS 23 - özellikli varlık ölçütü")

q("Aşağıdakilerden hangileri TMS 23'e göre borçlanma maliyeti sayılır?\n\nI. Etkin faiz yöntemiyle hesaplanan faiz gideri\n\nII. TFRS 16 kira yükümlülüğüne ilişkin faiz\n\nIII. Faiz düzeltmesi olarak dikkate alınan kur farkları",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 23 üçünü de borçlanma maliyeti sayar: etkin faiz yöntemiyle hesaplanan faiz gideri (I), TFRS 16 uyarınca kira yükümlülüklerine ilişkin faiz (II) ve faiz maliyetlerine düzeltme olarak dikkate alındığı ölçüde kur farkları (III).",
  "TMS 23 - kapsam")

q("Bir işletme, elde ettiği anda kullanıma hazır olan bir makineyi kredi ile satın almıştır. TMS 23 bakımından aşağıdakilerden hangisi doğrudur?",
  "Makine özellikli varlık olmadığından borçlanma maliyeti gider yazılır",
  ["Makine her hâlde özellikli varlık sayılır ve borçlanma maliyeti maliyete eklenmek zorundadır",
   "Borçlanma maliyeti her hâlde doğrudan özkaynaklardan indirilmek zorunda olan bir kalemdir",
   "Borçlanma maliyeti hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmaktadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: elde edildiklerinde amaçlanan kullanıma veya satışa hazır durumda olan varlıklar özellikli varlık değildir. Bu nedenle ilgili borçlanma maliyeti aktifleştirilmez; oluştuğu dönemde gider olarak muhasebeleştirilir.",
  "TMS 23 - özellikli olmayan varlık (senaryo)")

q("Özellikli varlığın maliyetine dâhil edilecek borçlanma maliyetinin muhasebeleştirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlığın maliyetine eklenerek aktifleştirilir; gider yazılmaz",
  ["Her hâlde dönem gideri yazılır; varlığın maliyetine hiçbir hâlde eklenmemektedir",
   "Her hâlde diğer kapsamlı gelirde muhasebeleştirilmek zorunda olan bir kalemi ifade eder",
   "Her hâlde ertelenmiş gelir olarak yabancı kaynaklarda gösterilmek zorunda tutulmaktadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 23: özellikli varlığın satın alınması, inşası veya üretimi ile doğrudan ilişkilendirilebilen borçlanma maliyetleri, ilgili varlığın maliyetinin bir parçasını oluşturur; aktifleştirilir.",
  "TMS 23 - aktifleştirme")

q("Diğer borçlanma maliyetleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Oluştukları dönemde gider olarak muhasebeleştirilir",
  ["Her hâlde varlıkların maliyetine eklenerek aktifleştirilmek zorunda tutulmaktadır",
   "Her hâlde gelecek dönemlere yayılarak itfa edilmek zorunda olan kalemleri ifade eder",
   "Hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmakla yetinilmektedir",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: özellikli varlıkla doğrudan ilişkilendirilemeyen diğer borçlanma maliyetleri, oluştukları dönemde gider olarak muhasebeleştirilir.",
  "TMS 23 - diğer borçlanma maliyetleri")

q("Yüksek enflasyonlu ekonomilerde borçlanma maliyetleri bakımından aşağıdakilerden hangisi doğrudur?",
  "TMS 29 uyarınca aynı dönemin enflasyonunu karşılayan kısım gider yazılır; aktifleştirilmez",
  ["Borçlanma maliyetlerinin tamamı her hâlde aktifleştirilmek zorunda tutulan bir durumu ifade eder",
   "Yüksek enflasyon hâlinde borçlanma maliyeti hiçbir hâlde gider yazılamamak durumundadır",
   "Yüksek enflasyon TMS 23 bakımından hiçbir özel durum doğurmayan bir olguyu ifade etmektedir",
   "Bu husus hiçbir standartta düzenlenmemiş olup uygulamada serbest bırakılmış bulunmaktadır"],
  "TMS 23: TMS 29 uygulanan yüksek enflasyonlu ekonomilerde, borçlanma maliyetlerinin aynı dönemdeki enflasyonu karşılayan kısmı, TMS 29 uyarınca gider olarak muhasebeleştirilir; aktifleştirilmez.",
  "TMS 23 - yüksek enflasyon")

q("Aşağıdaki ifadelerden hangileri TMS 23 bakımından doğrudur?\n\nI. Özellikli varlıkla doğrudan ilişkili borçlanma maliyetleri aktifleştirilir\n\nII. Diğer borçlanma maliyetleri gider yazılır\n\nIII. Finansal varlıklar özellikli varlıktır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Özellikli varlıkla doğrudan ilişkili borçlanma maliyetleri aktifleştirilir (I) ve diğerleri gider yazılır (II). Finansal varlıklar (III) ise TMS 23'te açıkça özellikli varlık SAYILMAZ; bu nedenle yanlıştır.",
  "TMS 23 - temel ilke")

# ── B. Aktifleştirilecek tutar: özel ve genel borçlanma (16) ───────────────
q("Özellikli varlık için özel olarak yapılan borçlanmada aktifleştirilecek tutar bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönemde oluşan fiili borçlanma maliyetinden, fonların geçici yatırımından sağlanan gelir düşülür",
  ["Fiili borçlanma maliyetinin tamamı aktifleştirilir; geçici yatırım geliri hiç dikkate alınmaz",
   "Yalnızca geçici yatırımdan sağlanan gelir aktifleştirilir; faiz maliyeti dikkate alınmamaktadır",
   "Aktifleştirilecek tutar her hâlde harcamanın tamamına eşit olmak zorunda bulunmaktadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: bir özellikli varlığın elde edilmesi amacıyla özel olarak borçlanılmış olması durumunda aktifleştirilebilir borçlanma maliyeti, ilgili dönemde bu borçlanmaya ilişkin olarak oluşan gerçek borçlanma maliyetinden, söz konusu fonların geçici yatırımlardan elde edilen gelirlerin düşülmesi suretiyle belirlenir.",
  "TMS 23 - özel borçlanma")

q("Genel amaçlı borçlanmaların özellikli varlık için kullanılması hâlinde aşağıdakilerden hangisi doğrudur?",
  "Varlığa ilişkin harcamalara aktifleştirme oranı uygulanarak aktifleştirilecek tutar bulunur",
  ["Genel borçlanmalardan hiçbir hâlde borçlanma maliyeti aktifleştirilememek zorunda kalınır",
   "Genel borçlanmaların tüm maliyeti her hâlde aktifleştirilmek zorunda tutulmaktadır",
   "Genel borçlanmalarda her hâlde en yüksek faizli kredinin oranı kullanılmak zorundadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: özellikli varlığın finansmanı genel amaçlı borçlanmalardan sağlandığında, aktifleştirilebilir borçlanma maliyeti tutarı, varlığa ilişkin yapılan harcamalara bir aktifleştirme oranı uygulanmak suretiyle belirlenir.",
  "TMS 23 - genel borçlanma")

q("TMS 23'e göre aktifleştirme oranı bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin genel amaçlı borçlanmalarına ilişkin borçlanma maliyetlerinin ağırlıklı ortalamasıdır",
  ["İşletmenin en yüksek faizli kredisinin faiz oranını ifade eden bir ölçüyü karşılamaktadır",
   "İşletmenin en düşük faizli kredisinin faiz oranını ifade eden bir ölçüyü karşılamak zorundadır",
   "Merkez bankasının ilan ettiği politika faizini ifade eden bir ölçüyü karşılamak durumundadır",
   "Aktifleştirme oranı TMS 23'te tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmıştır"],
  "TMS 23: aktifleştirme oranı, işletmenin ilgili dönem boyunca mevcut olan borçlarına ilişkin borçlanma maliyetlerinin ağırlıklı ortalamasıdır. Özellikli varlık elde etmek amacıyla yapılan özel borçlanmalar bu hesaplamanın dışında tutulur.",
  "TMS 23 - aktifleştirme oranı")

q("Aktifleştirme oranı hesabında özel borçlanmalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Özellikli varlık için yapılan özel borçlanmalar aktifleştirme oranı hesabına dâhil edilmez",
  ["Özel borçlanmalar her hâlde aktifleştirme oranı hesabına dâhil edilmek zorunda tutulmaktadır",
   "Aktifleştirme oranı hesabında yalnızca özel borçlanmalar dikkate alınmak zorunda kalınır",
   "Aktifleştirme oranı hesabında hiçbir borçlanma dikkate alınmaz; oran sabit kabul edilmektedir",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 23: aktifleştirme oranı, işletmenin dönem boyunca mevcut borçlarına ilişkin maliyetlerin ağırlıklı ortalamasıdır. Ancak bir özellikli varlık elde etmek amacıyla YAPILAN ÖZEL borçlanmalar bu hesaplamanın dışında tutulur; onlar kendi fiili maliyetiyle ele alınır.",
  "TMS 23 - oranın kapsamı")

q("Aktifleştirilecek borçlanma maliyetinin üst sınırı bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönem boyunca aktifleştirilen tutar, o dönemde oluşan toplam borçlanma maliyetini aşamaz",
  ["Aktifleştirilecek tutar için hiçbir üst sınır bulunmayıp sınırsızca aktifleştirilebilmektedir",
   "Aktifleştirilecek tutar her hâlde harcamanın tamamına eşit olmak zorunda bulunmaktadır",
   "Aktifleştirilecek tutar her hâlde toplam borçlanma maliyetinin iki katı olmak zorundadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: bir dönem boyunca aktifleştirilen borçlanma maliyetleri tutarı, ilgili dönem boyunca oluşan borçlanma maliyetleri tutarını AŞAMAZ. Bu, aktifleştirmenin mutlak tavanıdır.",
  "TMS 23 - aktifleştirme tavanı")

# ★ 2026/1 s.50 kalıbı: aktifleştirme oranı × harcama × süre
anapara, faiz, harcama, ay = 10_000_000, 1_000_000, 6_000_000, 6
oran = faiz / anapara
akt = harcama * oran * ay / 12
q(f"Bir inşaat işletmesinin dönemdeki genel amaçlı kredi anapara bakiyesi {tr(anapara)} ₺, bu kredilere katlanılan faiz tutarı ise {tr(faiz)} ₺'dir. İşletme aynı dönemin 1 Temmuz tarihinde inşaatına başladığı alışveriş merkezi ile ilgili {tr(harcama)} ₺ harcama yapmıştır. TMS 23'e göre aktifleştirilecek finansman (faiz) gideri kaç ₺'dir?",
  f"{tr(akt)} ₺",
  [f"{tr(harcama * oran)} ₺", f"{tr(faiz)} ₺", f"{tr(faiz * ay / 12)} ₺", f"{tr(harcama)} ₺"],
  f"Aktifleştirme oranı = Faiz ÷ Anapara = {tr(faiz)} ÷ {tr(anapara)} = %{oran*100:.0f}. Harcama 1 Temmuz'da yapıldığından yılın {ay} ayı için aktifleştirilir: {tr(harcama)} × %{oran*100:.0f} × {ay}/12 = {tr(akt)} ₺. Süre oranı unutulursa {tr(harcama*oran)} ₺ bulunur ki bu yanlıştır.",
  "TMS 23 - aktifleştirme oranı hesabı")

ozel_faiz, gecici_gelir = 800_000, 120_000
ozel_net = ozel_faiz - gecici_gelir
q(f"Bir işletme, özellikli varlık inşası için özel olarak kredi kullanmıştır. Dönemde bu krediye ilişkin oluşan fiili faiz maliyeti {tr(ozel_faiz)} ₺'dir. Henüz harcanmayan kredi fonlarının geçici yatırımından {tr(gecici_gelir)} ₺ gelir elde edilmiştir. TMS 23'e göre aktifleştirilecek borçlanma maliyeti kaç ₺'dir?",
  f"{tr(ozel_net)} ₺",
  [f"{tr(ozel_faiz)} ₺", f"{tr(ozel_faiz + gecici_gelir)} ₺", f"{tr(gecici_gelir)} ₺", "0 ₺"],
  f"Özel borçlanmada aktifleştirilecek tutar = Fiili borçlanma maliyeti − Fonların geçici yatırımından sağlanan gelir = {tr(ozel_faiz)} − {tr(gecici_gelir)} = {tr(ozel_net)} ₺. Geçici yatırım geliri düşülmezse {tr(ozel_faiz)} ₺ bulunur ki bu yanlıştır.",
  "TMS 23 - özel borçlanma hesabı")

# Sayılar bilerek seçildi: ağırlıklı ortalama %9 (tam sayı) ≠ basit ortalama %10.
# İkisi eşit çıkarsa soru öğretmek istediği ayrımı ölçemez.
k1, f1 = 4_000_000, 600_000        # %15
k2, f2 = 6_000_000, 300_000        # %5
top_k, top_f = k1 + k2, f1 + f2    # 10.000.000 / 900.000 → %9
o1 = f1 * 100 // k1
o2 = f2 * 100 // k2
agirlikli = top_f * 100 // top_k
basit = (o1 + o2) // 2
assert agirlikli != basit, "ağırlıklı ve basit ortalama aynı çıkarsa soru ayrımı ölçemez"
q(f"Bir işletmenin genel amaçlı iki kredisi vardır: {tr(k1)} ₺ anaparalı krediye {tr(f1)} ₺, {tr(k2)} ₺ anaparalı krediye {tr(f2)} ₺ faiz katlanılmıştır. Özel borçlanma yoktur. TMS 23'e göre aktifleştirme oranı yüzde kaçtır?",
  f"%{agirlikli}",
  [f"%{o1}", f"%{o2}", f"%{basit}", f"%{o1 + o2}"],
  f"Aktifleştirme oranı, genel borçlanmaların AĞIRLIKLI ORTALAMASIDIR: Toplam faiz ÷ Toplam anapara = ({tr(f1)} + {tr(f2)}) ÷ ({tr(k1)} + {tr(k2)}) = {tr(top_f)} ÷ {tr(top_k)} = %{agirlikli}. Kredilerin ayrı oranlarının (%{o1} ve %{o2}) basit ortalaması %{basit} alınmaz; farklı büyüklükteki krediler eşit ağırlık taşıyamaz, anaparalarla ağırlıklandırılır.",
  "TMS 23 - ağırlıklı ortalama oran")

harc3, oran3, top_faiz3 = 5_000_000, 12, 400_000
ham3 = harc3 * oran3 / 100
q(f"Bir işletmenin özellikli varlığa ilişkin ağırlıklı ortalama harcaması {tr(harc3)} ₺, aktifleştirme oranı %{oran3}'dir. İşletmenin dönemde katlandığı TOPLAM borçlanma maliyeti ise {tr(top_faiz3)} ₺'dir. TMS 23'e göre aktifleştirilecek tutar kaç ₺'dir?",
  f"{tr(top_faiz3)} ₺",
  [f"{tr(ham3)} ₺", f"{tr(ham3 + top_faiz3)} ₺", f"{tr(ham3 - top_faiz3)} ₺", f"{tr(harc3)} ₺"],
  f"Oran uygulaması {tr(harc3)} × %{oran3} = {tr(ham3)} ₺ verir. Ancak TMS 23'e göre aktifleştirilen tutar, dönemde OLUŞAN toplam borçlanma maliyetini AŞAMAZ. Toplam maliyet {tr(top_faiz3)} ₺ olduğundan aktifleştirilecek tutar {tr(top_faiz3)} ₺ ile sınırlıdır.",
  "TMS 23 - tavan uygulaması")

q("Özellikli varlığa ilişkin harcamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Nakit ödenen, diğer varlıkların transfer edildiği veya faiz içeren borç üstlenilen harcamalarla sınırlıdır; alınan hakediş ve teşvikler düşülür",
  ["Varlıkla ilgili her türlü tahakkuk her hâlde harcama sayılıp orana tabi tutulmak zorundadır",
   "Yalnızca dönem sonunda yapılan ödemeler harcama sayılır; yıl içi ödemeler dikkate alınmaz",
   "Harcama kavramı TMS 23'te hiçbir biçimde ele alınmamış olup serbest bırakılmış bulunmaktadır",
   "Harcama tutarı her hâlde varlığın gerçeğe uygun değerine eşit kabul edilmek zorundadır"],
  "TMS 23: bir özellikli varlığa ilişkin harcamalar; yalnızca nakit ödemelerini, diğer varlıkların transferini ve faiz içeren borçların üstlenilmesini içerir. Varlığa ilişkin alınan hakedişler ve devlet teşvikleri harcamalardan düşülür.",
  "TMS 23 - harcama kavramı")

q("Aktifleştirme oranı uygulanacak harcama tutarı bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönem içindeki harcamaların ağırlıklı ortalaması esas alınır",
  ["Dönem sonundaki harcama bakiyesinin tamamı her hâlde esas alınmak zorunda tutulmaktadır",
   "Dönem başındaki harcama bakiyesinin tamamı her hâlde esas alınmak zorunda bulunmaktadır",
   "Harcamanın tutarı hiç dikkate alınmaz; oran doğrudan kredi anaparasına uygulanmaktadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 23: aktifleştirme oranı, özellikli varlığa ilişkin harcamaların ağırlıklı ortalamasına uygulanır. Bu nedenle yıl ortasında yapılan bir harcama, yılın kalan süresiyle ağırlıklandırılır.",
  "TMS 23 - ağırlıklı ortalama harcama")

q("Bir işletme özellikli varlık için aldığı özel kredinin henüz harcanmayan kısmını mevduatta değerlendirmiştir. TMS 23 bakımından aşağıdakilerden hangisi doğrudur?",
  "Elde edilen faiz geliri, aktifleştirilecek borçlanma maliyetinden düşülür",
  ["Elde edilen faiz geliri aktifleştirilecek borçlanma maliyetine eklenmek zorunda tutulmaktadır",
   "Elde edilen faiz geliri her hâlde doğrudan özkaynağa kaydedilmek zorunda bulunmaktadır",
   "Elde edilen faiz geliri hiçbir biçimde kayda alınmaz; yalnızca dipnotta açıklanmaktadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: özel borçlanmada aktifleştirilebilir borçlanma maliyeti, dönemde oluşan gerçek borçlanma maliyetinden söz konusu fonların GEÇİCİ YATIRIMLARDAN elde edilen gelirlerinin DÜŞÜLMESİ suretiyle belirlenir.",
  "TMS 23 - geçici yatırım geliri (senaryo)")

q("Aşağıdaki ifadelerden hangileri aktifleştirilecek tutar bakımından doğrudur?\n\nI. Özel borçlanmada geçici yatırım geliri düşülür\n\nII. Genel borçlanmada harcamalara aktifleştirme oranı uygulanır\n\nIII. Aktifleştirilen tutar dönemde oluşan toplam borçlanma maliyetini aşabilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Özel borçlanmada geçici yatırım geliri düşülür (I) ve genel borçlanmada harcamalara aktifleştirme oranı uygulanır (II). Ancak aktifleştirilen tutar, dönemde oluşan toplam borçlanma maliyetini AŞAMAZ; bu nedenle III yanlıştır.",
  "TMS 23 - aktifleştirilecek tutar")

q("Aktifleştirme oranının hesaplanamadığı karmaşık durumlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Ana ortaklık ve bağlı ortaklıkların çok sayıda borçlanması varsa oranın belirlenmesinde muhakeme gerekir",
  ["Böyle durumlarda hiçbir hâlde aktifleştirme yapılamaz; tüm maliyet gider yazılmak zorundadır",
   "Böyle durumlarda oran her hâlde sıfır kabul edilmek zorunda olan bir durumu ifade etmektedir",
   "Böyle durumlarda her hâlde en yüksek faizli kredinin oranı kullanılmak zorunda kalınmaktadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: bir ana ortaklık ve bağlı ortaklıklarının farklı faiz oranlarıyla çok sayıda borçlanması olması gibi durumlarda, borçlanma maliyetlerinin ağırlıklı ortalamasının belirlenmesi muhakeme gerektirir.",
  "TMS 23 - oranın belirlenmesinde muhakeme")

# ── C. Başlama, ara verme, sona erme (16) ──────────────────────────────────
q("Borçlanma maliyetlerinin aktifleştirilmesine başlanması bakımından aşağıdakilerden hangisi doğrudur?",
  "Harcama yapılması, borçlanma maliyeti oluşması ve hazır hâle getirme faaliyetinin başlaması koşullarının ÜÇÜ birlikte sağlandığında başlanır",
  ["Yalnızca borçlanmanın yapılmış olması yeterli olup başka bir koşul aranmamak durumundadır",
   "Yalnızca inşaat faaliyetinin başlamış olması yeterli olup harcama aranmamak zorundadır",
   "Koşullardan herhangi birinin sağlanması yeterli olup üçünün birlikte bulunması aranmaz",
   "Aktifleştirmenin başlangıcı TMS 23'te düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 23: aktifleştirme, (a) varlık için harcama yapıldığında, (b) borçlanma maliyetleri oluştuğunda ve (c) varlığın amaçlanan kullanıma veya satışa hazır hâle getirilmesi için gerekli işlemler başladığında başlar. Üç koşul BİRLİKTE aranır.",
  "TMS 23 - aktifleştirmenin başlaması")

q("Varlığı hazır hâle getirmeye yönelik faaliyetler bakımından aşağıdakilerden hangisi doğrudur?",
  "Fiziki inşaatın yanı sıra izin alma gibi öncesindeki teknik ve idari çalışmaları da kapsar",
  ["Yalnızca fiziki inşaat faaliyetlerini kapsar; idari ve teknik çalışmalar hiç dâhil değildir",
   "Yalnızca izin alma işlemlerini kapsar; fiziki inşaat faaliyetleri hiçbir hâlde dâhil edilmez",
   "Varlığın sadece elde tutulduğu dönemleri de kapsayan geniş bir kavramı ifade etmektedir",
   "Bu kavram TMS 23'te tanımlanmamış bir husus niteliğinde olup belirsiz bırakılmış bulunur"],
  "TMS 23: varlığın amaçlanan kullanıma hazır hâle getirilmesi için gerekli işlemler, sadece fiziki inşaatı değil, öncesindeki teknik ve idari çalışmaları da (izin alınması gibi) kapsar. Ancak varlığın üretim veya gelişimini sağlayacak işlem olmaksızın sadece elde tutulması bu kapsamda değildir.",
  "TMS 23 - hazır hâle getirme faaliyeti")

q("Bir arsanın üzerinde inşaat yapılmaksızın sadece elde tutulması bakımından aşağıdakilerden hangisi doğrudur?",
  "Bu dönemde oluşan borçlanma maliyetleri aktifleştirilmez",
  ["Bu dönemde oluşan borçlanma maliyetleri her hâlde aktifleştirilmek zorunda tutulmaktadır",
   "Bu dönemde oluşan borçlanma maliyetleri her hâlde iki katı olarak aktifleştirilmek zorundadır",
   "Bu dönemde oluşan borçlanma maliyetleri her hâlde özkaynaktan indirilmek zorunda kalınır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 23: inşaat için kullanılacak arsa üzerinde geliştirme faaliyeti sürüyorsa bu dönemde oluşan borçlanma maliyetleri aktifleştirilir. Ancak inşaat amacıyla alınan arsa, üzerinde herhangi bir geliştirme faaliyeti olmaksızın SADECE elde tutuluyorsa bu dönemde oluşan borçlanma maliyetleri aktifleştirilmeye uygun değildir.",
  "TMS 23 - sadece elde tutma")

q("Borçlanma maliyetlerinin aktifleştirilmesine ara verilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Faaliyete ara verilen uzun süreli dönemlerde aktifleştirmeye ara verilir",
  ["Faaliyete ara verilse dahi aktifleştirme her hâlde kesintisiz sürdürülmek zorunda kalınmaktadır",
   "Faaliyete ara verildiğinde aktifleştirme tümüyle ve kalıcı olarak sona ermek zorundadır",
   "Ara verme hâlinde önceden aktifleştirilen tutarlar her hâlde iptal edilmek zorunda tutulur",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: özellikli varlığın amaçlanan kullanıma veya satışa hazır hâle getirilmesine yönelik faaliyetlere ara verilen UZUN SÜRELİ dönemlerde, borçlanma maliyetlerinin aktifleştirilmesine ara verilir.",
  "TMS 23 - aktifleştirmeye ara verme")

q("Bir inşaat işletmesi projesini uzun süreli olarak durdurmuştur. TMS 23 bakımından durdurma süresinde oluşan borçlanma maliyetleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Bu sürede oluşan borçlanma maliyetleri aktifleştirilmez; gider yazılır",
  ["Bu sürede oluşan borçlanma maliyetleri her hâlde aktifleştirilmeye devam edilmek zorundadır",
   "Bu sürede oluşan borçlanma maliyetleri her hâlde diğer kapsamlı gelire yansıtılmak zorundadır",
   "Bu sürede oluşan borçlanma maliyetleri hiçbir biçimde kayda alınmamak zorunda kalınmaktadır",
   "Durdurma hâlinde önceden aktifleştirilen tutarların tamamı her hâlde iptal edilmek zorundadır"],
  "TMS 23: faaliyetlere ara verilen uzun süreli dönemlerde aktifleştirmeye ara verilir; bu sürede oluşan borçlanma maliyetleri gider olarak muhasebeleştirilir. Önceden aktifleştirilenler iptal edilmez; aktifleştirme yalnızca durur.",
  "TMS 23 - uzun süreli durdurma (senaryo)")

q("Aktifleştirmeye ara verilmeyecek hâller bakımından aşağıdakilerden hangisi doğrudur?",
  "Önemli teknik ve idari çalışmaların sürdüğü ya da gecikmenin sürecin kaçınılmaz parçası olduğu dönemlerde ara verilmez",
  ["Her türlü gecikmede aktifleştirmeye her hâlde ara verilmek zorunda tutulan bir durumdur",
   "Hiçbir gecikmede aktifleştirmeye ara verilmez; aktifleştirme kesintisiz sürmek zorundadır",
   "Ara verilip verilmeyeceği tümüyle işletmenin serbest takdirine bırakılmış bir husustur",
   "Bu husus TMS 23'te düzenlenmemiş bir konu niteliğinde olup belirsiz bırakılmış bulunmaktadır"],
  "TMS 23: işletme önemli teknik ve idari çalışmalar yürütüyorsa borçlanma maliyetlerinin aktifleştirilmesine ara verilmez. Ayrıca geçici gecikme, varlığın hazır hâle getirilmesi için gerekli sürecin kaçınılmaz bir parçası ise (yüksek su seviyesinin köprü inşaatını geciktirmesi gibi) ara verilmez.",
  "TMS 23 - ara verilmeyen hâller")

q("Borçlanma maliyetlerinin aktifleştirilmesinin sona ermesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlığın amaçlanan kullanıma veya satışa hazır duruma getirilmesi için gerekli tüm işlemler esas itibarıyla tamamlandığında sona erer",
  ["Varlığın bedeli tamamen ödendiğinde sona erer; fiziki tamamlanma hiç dikkate alınmamaktadır",
   "Varlık fiilen kullanılmaya başlandığında sona erer; hazır olması yeterli sayılmamaktadır",
   "Aktifleştirme hiçbir hâlde sona ermez; varlığın ömrü boyunca sürdürülmek zorunda kalınır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: bir özellikli varlığın amaçlanan kullanıma veya satışa hazır duruma getirilmesi için gerekli tüm işlemler esas itibarıyla tamamlandığında, borçlanma maliyetlerinin aktifleştirilmesine son verilir.",
  "TMS 23 - aktifleştirmenin sona ermesi")

q("Yalnızca rutin idari işlerin kaldığı ve varlığın fiziken tamamlandığı durum bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlık esas itibarıyla tamamlanmış sayılır; aktifleştirme sona erer",
  ["Rutin işler bitene kadar aktifleştirme her hâlde sürdürülmek zorunda tutulan bir durumdur",
   "Varlık hiçbir hâlde tamamlanmış sayılamaz; aktifleştirme süresiz olarak devam etmektedir",
   "Rutin idari işlerin varlığı aktifleştirmenin iptal edilmesini gerektirmek zorunda kalmaktadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 23: bir varlığın fiziki yapımının tamamlanmasına rağmen rutin idari işlemler devam ediyorsa, bu durum işlemlerin esas itibarıyla tamamlandığını gösterir ve aktifleştirme sona erer. Küçük değişiklikler için bekleniyorsa da esas itibarıyla tamamlanmış sayılır.",
  "TMS 23 - esas itibarıyla tamamlanma")

q("Kısımlar hâlinde tamamlanan özellikli varlıklar bakımından aşağıdakilerden hangisi doğrudur?",
  "Tamamlanan ve diğerleri sürerken kullanılabilen her kısım için aktifleştirme ayrı ayrı sona erer",
  ["Tüm kısımlar tamamlanana kadar hiçbir kısım için aktifleştirme sona ermemek zorundadır",
   "İlk kısım tamamlandığında tüm varlık için aktifleştirme her hâlde sona ermek zorundadır",
   "Kısımlar hâlinde tamamlama TMS 23'te hiçbir biçimde ele alınmamış bir husus niteliğindedir",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: bir özellikli varlığın inşası kısımlar hâlinde tamamlanıyor ve diğer kısımların inşası devam ederken her bir kısım kullanılabiliyorsa, ilgili kısmın hazır hâle getirilmesi için gerekli işlemler esas itibarıyla tamamlandığında o kısma ilişkin aktifleştirme sona erer.",
  "TMS 23 - kısmi tamamlanma")

q("Bütün olarak tamamlanması gereken özellikli varlıklar bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir bütün olarak tamamlanması gerekiyorsa aktifleştirme ancak tamamının bitmesiyle sona erer",
  ["Her hâlde ilk kısmın tamamlanmasıyla aktifleştirme sona ermek zorunda tutulmaktadır",
   "Her hâlde her kısım için ayrı ayrı aktifleştirme sona ermek zorunda bulunmaktadır",
   "Bu tür varlıklarda aktifleştirme hiçbir hâlde sona ermez; süresiz olarak sürmektedir",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 23: bütün olarak tamamlanması gereken özellikli varlıklarda (birden fazla işlem aşaması olan bir çelik fabrikası gibi), aktifleştirme ancak varlığın TAMAMININ hazır duruma getirilmesi için gerekli işlemler tamamlandığında sona erer.",
  "TMS 23 - bütün olarak tamamlanma")

q("Bir iş merkezinin bağımsız bölümleri sırayla tamamlanmakta ve her biri diğerleri inşa hâlindeyken kullanılabilmektedir. TMS 23 bakımından aşağıdakilerden hangisi doğrudur?",
  "Tamamlanan her bağımsız bölüm için aktifleştirme ayrı ayrı sona erer",
  ["Tüm iş merkezi bitene kadar hiçbir bölüm için aktifleştirme sona ermemek zorunda kalınır",
   "İlk bölüm bitince tüm iş merkezi için aktifleştirme her hâlde sona ermek zorunda tutulur",
   "Bu durumda önceden aktifleştirilen tutarların tamamı her hâlde iptal edilmek zorundadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: her biri ayrı ayrı kullanılabilen bölümlerden oluşan bir iş merkezinde (birden çok bina), diğer bölümlerin inşası sürerken kullanılabilen her bir bölüm için aktifleştirme ayrı ayrı sona erer.",
  "TMS 23 - bağımsız bölümler (senaryo)")

q("Aşağıdakilerden hangileri TMS 23'e göre aktifleştirmenin BAŞLAMASI için birlikte aranır?\n\nI. Varlık için harcama yapılması\n\nII. Borçlanma maliyeti oluşması\n\nIII. Varlığı hazır hâle getirme işlemlerinin başlaması",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 23 üç koşulu da BİRLİKTE arar: varlık için harcama yapılması (I), borçlanma maliyeti oluşması (II) ve varlığın amaçlanan kullanıma/satışa hazır hâle getirilmesi için gerekli işlemlerin başlaması (III).",
  "TMS 23 - aktifleştirmenin başlaması")

q("Aşağıdaki ifadelerden hangileri TMS 23 bakımından doğrudur?\n\nI. Faaliyete uzun süre ara verilirse aktifleştirmeye ara verilir\n\nII. Önemli teknik ve idari çalışmalar sürerken ara verilmez\n\nIII. Ara verme hâlinde önceden aktifleştirilen tutarlar iptal edilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Uzun süreli ara verilen dönemlerde aktifleştirmeye ara verilir (I) ve önemli teknik/idari çalışmalar sürerken ara verilmez (II). Ara verme hâlinde önceden aktifleştirilen tutarlar İPTAL EDİLMEZ; aktifleştirme yalnızca durur. Bu nedenle III yanlıştır.",
  "TMS 23 - ara verme")

q("Bir köprü inşaatı, yüksek su seviyesi nedeniyle geçici olarak gecikmiştir ve bu durum bölgede inşaat döneminde olağandır. TMS 23 bakımından aşağıdakilerden hangisi doğrudur?",
  "Gecikme sürecin kaçınılmaz parçası olduğundan aktifleştirmeye ara verilmez",
  ["Her gecikmede olduğu gibi burada da aktifleştirmeye her hâlde ara verilmek zorunda kalınır",
   "Bu durumda aktifleştirme tümüyle ve kalıcı olarak sona ermek zorunda tutulmaktadır",
   "Bu durumda önceden aktifleştirilen tutarların tamamı iptal edilmek zorunda bulunmaktadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: geçici gecikme, varlığın amaçlanan kullanıma hazır hâle getirilmesi için gerekli sürecin kaçınılmaz bir parçası ise aktifleştirmeye ara verilmez. Standart bu duruma köprü inşaatında yüksek su seviyesinin yol açtığı ve o bölgede olağan sayılan gecikmeyi örnek gösterir.",
  "TMS 23 - kaçınılmaz gecikme (senaryo)")

q("Özellikli varlığın defter değerinin geri kazanılabilir tutarı aşması bakımından aşağıdakilerden hangisi doğrudur?",
  "Diğer standartlar uyarınca değer düşüklüğü zararı yazılır veya kayıt değeri düşürülür",
  ["Bu durumda hiçbir işlem yapılmaz; defter değeri olduğu gibi korunmak zorunda kalınmaktadır",
   "Bu durumda aktifleştirme her hâlde geriye dönük olarak iptal edilmek zorunda tutulmaktadır",
   "Bu durumda varlık her hâlde bilanço dışı bırakılmak zorunda olan bir kalemi ifade etmektedir",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: özellikli varlığın defter değerinin veya nihai maliyetinin geri kazanılabilir tutarını ya da net gerçekleşebilir değerini aşması durumunda, defter değeri diğer standartların hükümleri uyarınca düşürülür veya kayıtlardan çıkarılır (TMS 36 / TMS 2).",
  "TMS 23 - değer düşüklüğüyle ilişki")

q("Aşağıdaki ifadelerden hangileri aktifleştirmenin sona ermesi bakımından doğrudur?\n\nI. Gerekli tüm işlemler esas itibarıyla tamamlandığında sona erer\n\nII. Fiziki yapım bitip yalnız rutin idari işler kalmışsa tamamlanmış sayılır\n\nIII. Kısımlar hâlinde tamamlanan varlıkta her kısım için ayrı ayrı sona erebilir",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Üçü de doğrudur: aktifleştirme gerekli işlemler esas itibarıyla tamamlandığında sona erer (I), fiziki yapım bitip yalnız rutin idari işler kalmışsa esas itibarıyla tamamlanmış sayılır (II) ve her biri ayrı kullanılabilen kısımlarda aktifleştirme kısım kısım sona erer (III).",
  "TMS 23 - sona erme")

# ── D. Açıklamalar ve karma (12) ───────────────────────────────────────────
q("TMS 23'e göre yapılacak açıklamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönem boyunca aktifleştirilen borçlanma maliyeti tutarı ve kullanılan aktifleştirme oranı açıklanır",
  ["Borçlanma maliyetleri hakkında hiçbir açıklama yapılmasına gerek bulunmamak durumundadır",
   "Yalnızca gider yazılan tutar açıklanır; aktifleştirilen tutar hiçbir hâlde açıklanmamaktadır",
   "Yalnızca vergi idaresine bildirim yapılır; finansal tablo kullanıcılarına açıklama yapılmaz",
   "Açıklama yalnızca özellikli varlığı bulunmayan işletmeler için zorunlu tutulmuş bulunmaktadır"],
  "TMS 23: işletme (a) dönem boyunca aktifleştirilen borçlanma maliyetinin tutarını ve (b) aktifleştirilebilir borçlanma maliyeti tutarının belirlenmesinde kullanılan aktifleştirme oranını açıklar.",
  "TMS 23 - açıklamalar")

q("Bir işletme, özellikli varlık için katlandığı borçlanma maliyetlerinin tamamını gider yazmıştır. TMS 23 bakımından aşağıdakilerden hangisi doğrudur?",
  "Uygulama yanlıştır; doğrudan ilişkilendirilebilen kısım aktifleştirilmeliydi",
  ["Uygulama doğrudur; borçlanma maliyetleri her hâlde gider yazılmak zorunda tutulmaktadır",
   "Uygulama doğrudur; aktifleştirme işletmenin serbest tercihine bırakılmış bir husustur",
   "Uygulama yanlıştır; borçlanma maliyetlerinin tamamı her hâlde aktifleştirilmek zorundadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: özellikli varlığın satın alınması, inşası veya üretimiyle DOĞRUDAN İLİŞKİLENDİRİLEBİLEN borçlanma maliyetleri varlığın maliyetinin bir parçasını oluşturur; aktifleştirilmesi zorunludur, tercih değildir. Yalnız diğer borçlanma maliyetleri gider yazılır.",
  "TMS 23 - zorunlu aktifleştirme (senaryo)")

q("TMS 23 ile TMS 16'nın ilişkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Aktifleştirilen borçlanma maliyeti maddi duran varlığın maliyetine girer; sonra TMS 16'ya göre amortismana tabi tutulur",
  ["İki standart arasında hiçbir ilişki bulunmayıp birbirinden bağımsız uygulanmak zorundadır",
   "Aktifleştirilen borçlanma maliyeti hiçbir hâlde amortismana tabi tutulamamak durumundadır",
   "Aktifleştirilen borçlanma maliyeti her hâlde ayrı bir varlık olarak izlenmek zorunda kalınır",
   "Bu husus hiçbir standartta düzenlenmemiş olup uygulamada serbest bırakılmış bulunmaktadır"],
  "TMS 23 uyarınca aktifleştirilen borçlanma maliyeti, özellikli varlığın maliyetinin bir parçasını oluşturur. Varlık maddi duran varlıksa bu tutar TMS 16 kapsamında amortismana tabi tutarın içindedir; ayrı bir varlık olarak izlenmez.",
  "TMS 23 - TMS 16 ile ilişki")

q("Gerçeğe uygun değerle ölçülen özellikli varlıklarda borçlanma maliyeti bakımından aşağıdakilerden hangisi doğrudur?",
  "Aktifleştirme zorunlu değildir",
  ["Aktifleştirme her hâlde ve istisnasız zorunlu olan bir uygulamayı ifade etmek durumundadır",
   "Aktifleştirme her hâlde yasak olup borçlanma maliyeti gider yazılmak zorunda kalınmaktadır",
   "Bu varlıklar için borçlanma maliyeti hiçbir biçimde kayda alınmamak zorunda bulunmaktadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: işletmenin, gerçeğe uygun değerinden ölçülen bir özellikli varlıkla (canlı varlık gibi) doğrudan ilişkilendirilebilen borçlanma maliyetlerini aktifleştirmesi zorunlu değildir.",
  "TMS 23 - GUD ile ölçülen özellikli varlık")

q("Tekrarlanan biçimde çok sayıda üretilen stoklarda borçlanma maliyeti bakımından aşağıdakilerden hangisi doğrudur?",
  "Aktifleştirme zorunlu değildir; bu stoklar özellikli varlık sayılmaz",
  ["Bu stoklar için aktifleştirme her hâlde zorunlu olan bir uygulamayı ifade etmek durumundadır",
   "Bu stoklar her hâlde özellikli varlık sayılıp aktifleştirme yapılmak zorunda kalınmaktadır",
   "Bu stoklar için borçlanma maliyeti hiçbir biçimde kayda alınmamak zorunda bulunmaktadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunur"],
  "TMS 23: kısa bir zaman diliminde ve tekrarlanan biçimde çok sayıda üretilen stoklar özellikli varlık değildir; bu stoklarla ilişkili borçlanma maliyetlerinin aktifleştirilmesi zorunlu değildir.",
  "TMS 23 - tekrarlanan üretim stokları")

harc4, oran4, ay4 = 3_000_000, 8, 9
akt4 = harc4 * oran4 / 100 * ay4 / 12
q(f"Bir işletme özellikli varlık inşaatına yılın 1 Nisan tarihinde başlamış ve o tarihte {tr(harc4)} ₺ harcama yapmıştır. Genel borçlanmalar için aktifleştirme oranı %{oran4}'dir ve inşaat yıl sonunda hâlâ sürmektedir. TMS 23'e göre bu yıl aktifleştirilecek borçlanma maliyeti kaç ₺'dir?",
  f"{tr(akt4)} ₺",
  [f"{tr(harc4 * oran4 / 100)} ₺", f"{tr(harc4 * oran4 / 100 * 3 / 12)} ₺", f"{tr(harc4)} ₺", "0 ₺"],
  f"Harcama 1 Nisan'da yapıldığından yılın {ay4} ayı boyunca finanse edilmiştir: {tr(harc4)} × %{oran4} × {ay4}/12 = {tr(akt4)} ₺. Tüm yıl varsayılırsa {tr(harc4*oran4/100)} ₺ bulunur ki bu, harcamanın yıl başında yapılmadığını göz ardı eder.",
  "TMS 23 - kısmi yıl aktifleştirmesi")

q("Bir işletme, özellikli varlık inşaatı için hem özel kredi hem genel amaçlı krediler kullanmaktadır. TMS 23 bakımından aşağıdakilerden hangisi doğrudur?",
  "Özel krediye fiili maliyet (geçici gelir düşülerek), özel kredinin aşıldığı harcama kısmına aktifleştirme oranı uygulanır",
  ["Tüm borçlanmalar için her hâlde tek bir aktifleştirme oranı kullanılmak zorunda tutulmaktadır",
   "Yalnızca özel kredi dikkate alınır; genel amaçlı krediler hiçbir hâlde hesaba katılmamaktadır",
   "Yalnızca genel krediler dikkate alınır; özel kredi hiçbir hâlde hesaba katılmamak zorundadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: özel borçlanma kendi fiili maliyetiyle (geçici yatırım geliri düşülerek) ele alınır ve aktifleştirme oranı hesabının dışında tutulur. Harcamanın özel borçlanmayı aşan kısmı için genel borçlanmaların ağırlıklı ortalaması olan aktifleştirme oranı uygulanır.",
  "TMS 23 - özel ve genel borçlanmanın birlikte kullanımı")

q("Aşağıdaki ifadelerden hangileri TMS 23 bakımından doğrudur?\n\nI. Aktifleştirilen tutar ve aktifleştirme oranı açıklanır\n\nII. Aktifleştirme, doğrudan ilişkilendirilebilen maliyetlerde zorunludur\n\nIII. Aktifleştirme her hâlde işletmenin tercihine bağlıdır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Aktifleştirilen tutar ve oran açıklanır (I) ve doğrudan ilişkilendirilebilen borçlanma maliyetlerinin aktifleştirilmesi ZORUNLUDUR (II). Aktifleştirme genel olarak tercihe bağlı DEĞİLDİR; yalnız gerçeğe uygun değerle ölçülen özellikli varlıklar ile tekrarlanan üretim stoklarında zorunlu değildir. Bu nedenle III yanlıştır.",
  "TMS 23 - genel")

q("Aşağıdakilerden hangileri TMS 23'e göre borçlanma maliyetinin aktifleştirilmesinin zorunlu OLMADIĞI hâllerdendir?\n\nI. Gerçeğe uygun değerle ölçülen özellikli varlıklar\n\nII. Kısa sürede tekrarlanan biçimde çok sayıda üretilen stoklar\n\nIII. İnşası birkaç yıl süren imalat tesisi",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Gerçeğe uygun değerle ölçülen özellikli varlıklarda (I) ve kısa sürede tekrarlanan biçimde üretilen stoklarda (II) aktifleştirme zorunlu değildir. İnşası birkaç yıl süren imalat tesisi (III) ise tipik bir özellikli varlıktır; doğrudan ilişkili borçlanma maliyetinin aktifleştirilmesi ZORUNLUDUR.",
  "TMS 23 - aktifleştirmenin zorunlu olmadığı hâller")

q("Aktifleştirme oranı ile aktifleştirilecek tutar arasındaki ilişki bakımından aşağıdakilerden hangisi doğrudur?",
  "Oran, özellikli varlığa ilişkin ağırlıklı ortalama harcamaya uygulanır; kredi anaparasına değil",
  ["Oran her hâlde kredi anaparasının tamamına uygulanmak zorunda olan bir hesabı ifade eder",
   "Oran her hâlde varlığın gerçeğe uygun değerine uygulanmak zorunda tutulan bir hesaptır",
   "Oran her hâlde işletmenin toplam varlıklarına uygulanmak zorunda bulunan bir hesabı karşılar",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: aktifleştirilecek borçlanma maliyeti, özellikli varlığa ilişkin HARCAMALARA aktifleştirme oranı uygulanmak suretiyle belirlenir. Oran kredi anaparasına değil, varlığa yapılan (ağırlıklı ortalama) harcamaya uygulanır.",
  "TMS 23 - oranın uygulanacağı taban")

q("Bir işletme özellikli varlık inşaatına başlamış ancak henüz hiç harcama yapmamıştır; kredi kullanımı ise başlamıştır. TMS 23 bakımından aşağıdakilerden hangisi doğrudur?",
  "Harcama koşulu sağlanmadığından aktifleştirmeye henüz başlanmaz",
  ["Kredi kullanımı başladığından aktifleştirmeye her hâlde başlanmak zorunda tutulmaktadır",
   "İnşaat başladığından aktifleştirmeye her hâlde başlanmak zorunda bulunan bir durumu ifade eder",
   "Bu durumda borçlanma maliyeti hiçbir biçimde kayda alınmamak zorunda kalınmaktadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: aktifleştirme, üç koşulun BİRLİKTE sağlandığı tarihte başlar: harcama yapılması, borçlanma maliyeti oluşması ve hazır hâle getirme işlemlerinin başlaması. Harcama yapılmadıkça diğer iki koşul sağlansa da aktifleştirmeye başlanmaz; oluşan borçlanma maliyeti gider yazılır.",
  "TMS 23 - başlangıç koşulu eksik (senaryo)")

q("Aşağıdaki ifadelerden hangileri aktifleştirme oranı bakımından doğrudur?\n\nI. Genel borçlanma maliyetlerinin ağırlıklı ortalamasıdır\n\nII. Özellikli varlık için yapılan özel borçlanmalar hesaba dâhil edilmez\n\nIII. Kredilerin faiz oranlarının basit ortalaması alınır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Aktifleştirme oranı genel borçlanma maliyetlerinin AĞIRLIKLI ortalamasıdır (I) ve özellikli varlık için yapılan özel borçlanmalar hesabın dışında tutulur (II). Basit ortalama (III) alınmaz; anaparalarla ağırlıklandırılır — farklı büyüklükteki krediler eşit ağırlık taşıyamaz.",
  "TMS 23 - aktifleştirme oranı")

q("Bir işletme, özellikli varlığı için aldığı özel kredinin faizini aktifleştirirken, aynı dönemde genel amaçlı kredilerinin faizini de aynı varlığa aktifleştirmiştir; oysa varlığa yapılan harcama özel kredi tutarının altındadır. TMS 23 bakımından aşağıdakilerden hangisi doğrudur?",
  "Harcama özel krediyi aşmadığından genel borçlanmadan aktifleştirme yapılmaz",
  ["Genel kredilerin faizi de her hâlde aktifleştirilmek zorunda olan bir tutarı ifade etmektedir",
   "Bu durumda özel kredinin faizi hiçbir hâlde aktifleştirilememek zorunda kalınmaktadır",
   "Bu durumda iki kredinin faizi de her hâlde gider yazılmak zorunda bulunmaktadır",
   "Bu husus TMS 23'te düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 23: aktifleştirme oranı, harcamanın ÖZEL borçlanmayı AŞAN kısmına uygulanır. Harcama özel kredi tutarının altındaysa genel borçlanmalardan finanse edilen bir kısım yoktur; genel kredilerin faizi bu varlığa aktifleştirilmez, gider yazılır. Aksi hâlde aynı harcama iki kez finanse edilmiş sayılırdı.",
  "TMS 23 - özel borçlanmanın aşılmaması (senaryo)")

q("Aşağıdaki ifadelerden hangileri TMS 23'ün diğer standartlarla ilişkisi bakımından doğrudur?\n\nI. Aktifleştirilen tutar özellikli varlığın maliyetine girer\n\nII. Varlığın defter değeri geri kazanılabilir tutarı aşarsa TMS 36 uygulanır\n\nIII. Yüksek enflasyonda enflasyonu karşılayan kısım da aktifleştirilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Aktifleştirilen tutar varlığın maliyetine girer (I) ve defter değeri geri kazanılabilir tutarı aşarsa TMS 36 uyarınca değer düşüklüğü yazılır (II). Yüksek enflasyonlu ekonomilerde borçlanma maliyetinin aynı dönem enflasyonunu karşılayan kısmı ise TMS 29 uyarınca GİDER yazılır, aktifleştirilmez. Bu nedenle III yanlıştır.",
  "TMS 23 - diğer standartlarla ilişki")

print("TOPLAM:", len(Q))

# ══ BUILD ═════════════════════════════════════════════════════════════════
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
    for i, it in enumerate(Q):
        ans = letters[i]
        opts = {ans: it["correct"]}
        for k, d in zip([k for k in "ABCDE" if k != ans], it["distractors"]):
            opts[k] = d
        assert len(set(opts.values())) == 5, f"{PREFIX}-{i+1}: şık tekrarı"
        out.append({
            "id": f"{PREFIX}-{i+1:04d}", "ders": DERS, "konu": KONU,
            "stem": it["stem"], "options": opts, "answer": ans,
            "solution": it["why"] + f" Doğru cevap {ans}.",
            "source": {"kind": "generated",
                       "styleRef": "SGS Muhasebe Standartları (TMS 23; 2026/1 kalıbına kalibre)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    hepsi = sum(1 for x in onc if x["options"][x["answer"]].strip() == "I, II ve III")
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} hepsi {hepsi} ({hepsi*100//max(len(onc),1)}%) | harf {''.join(x['answer'] for x in out)[:40]}…")
