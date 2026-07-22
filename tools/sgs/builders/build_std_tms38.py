# -*- coding: utf-8 -*-
"""SGS — Muhasebe Standartları / TMS 38 Maddi Olmayan Duran Varlıklar — 60 soru.
Kaynak: KGK TMS 38. Aritmetik python'da hesaplanır, bağımsız doğrulanır.
KURAL: doğru şık KISA (≤~110), çeldiriciler UZUN (~90-115) → length-tell sıfır.
ÖNCÜLLÜ hedefi: 8-9 soru, "hepsi" cevabı ~2 (%25)."""
import json, random, re

DERS, KONU = "muhasebe_standartlari", "tms_38_modv"
PREFIX, SEED = "std-tms38-gen", 20260227
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/muhasebe_standartlari/tms_38_modv.json"

Q = []
def q(stem, correct, distractors, why, ref):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why, ref=ref))

def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9: v = round(v)
    return f"{v:,}".replace(",", ".")

# ── A. Tanım, tanımlanabilirlik, kontrol (14) ──────────────────────────────
q("TMS 38'e göre maddi olmayan duran varlık bakımından aşağıdakilerden hangisi doğrudur?",
  "Fiziksel niteliği olmayan, tanımlanabilir, parasal olmayan varlıktır",
  ["Fiziksel niteliği bulunan ve bir dönemden fazla kullanımı öngörülen varlıkları ifade etmektedir",
   "İşletmenin bir yıl içinde paraya çevirmeyi planladığı parasal nitelikli varlıkları kapsamaktadır",
   "İşletmenin kira geliri veya değer artışı amacıyla elde tuttuğu gayrimenkulleri ifade eden kalemdir",
   "Maddi olmayan duran varlık kavramı TMS 38'de tanımlanmamış olup uygulamada kullanılmamaktadır"],
  "TMS 38: maddi olmayan duran varlık, fiziksel niteliği olmayan, tanımlanabilir, parasal olmayan varlıktır.",
  "TMS 38 - MODV tanımı")

q("Maddi olmayan duran varlığın tanımını oluşturan unsurlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Tanımlanabilirlik, kontrol ve gelecekteki ekonomik yararların varlığı gerekir",
  ["Yalnızca fiziksel bir varlığın bulunmaması yeterli olup başka hiçbir unsur aranmamaktadır",
   "Yalnızca varlığın bedelinin ödenmiş olması yeterli olup başka bir koşul aranmamaktadır",
   "Yalnızca varlığın hukuken tescil edilmiş olması yeterli olup diğer unsurlar aranmaz",
   "Tanımın unsurları TMS 38'de düzenlenmemiş olup işletmenin takdirine bırakılmış bulunmaktadır"],
  "TMS 38: maddi olmayan duran varlık tanımı, varlığın tanımlanabilir olmasını, üzerinde kontrol bulunmasını ve gelecekte ekonomik yarar sağlamasını gerektirir.",
  "TMS 38 - tanımın unsurları")

q("Maddi olmayan duran varlığın tanımlanabilirliği bakımından aşağıdakilerden hangisi doğrudur?",
  "Ayrılabilir olması veya sözleşmeye bağlı ya da diğer yasal haklardan kaynaklanması hâlinde tanımlanabilirdir",
  ["Yalnızca hukuken tescil edilmiş varlıklar tanımlanabilir sayılır; sözleşmesel haklar kapsam dışıdır",
   "Yalnızca satın alınmış varlıklar tanımlanabilir sayılır; ayrılabilirlik ölçütü aranmamaktadır",
   "Her maddi olmayan kalem her hâlde tanımlanabilir sayılır; ayrıca bir ölçüt aranmamaktadır",
   "Tanımlanabilirlik ölçütü TMS 38'de düzenlenmemiş olup uygulamada dikkate alınmamaktadır"],
  "TMS 38: bir varlık, (a) ayrılabilir olması, yani işletmeden ayrılabilmesi veya bölünebilmesi ve satılabilmesi, devredilebilmesi, lisans altına konulabilmesi, kiralanabilmesi ya da değiştirilebilmesi veya (b) sözleşmeye bağlı haklardan ya da diğer yasal haklardan kaynaklanması durumunda tanımlanabilirdir.",
  "TMS 38 - tanımlanabilirlik")

q("Maddi olmayan duran varlık üzerindeki kontrol bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelecekteki ekonomik yararları elde etme ve başkalarının bu yararlara erişimini kısıtlama gücüdür",
  ["Yalnızca varlığın fiziken elde bulundurulmasını ifade eden bir kavramı karşılamaktadır",
   "Yalnızca varlığın bedelinin tamamının ödenmiş olmasını ifade eden bir kavram niteliğindedir",
   "Yalnızca varlığın bilançoda gösterilmiş olmasını ifade eden biçimsel bir kavramı karşılar",
   "Kontrol kavramı TMS 38'de tanımlanmamış olup uygulamada dikkate alınmayan bir husustur"],
  "TMS 38: işletme, bir varlıktan kaynaklanan gelecekteki ekonomik yararları elde etme ve başkalarının bu yararlara erişimini kısıtlama gücüne sahipse söz konusu varlığı kontrol ediyordur.",
  "TMS 38 - kontrol")

q("Nitelikli personelden oluşan ekip ve personelin becerileri bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme genellikle yeterli kontrole sahip olmadığından maddi olmayan duran varlık olarak muhasebeleştirilmez",
  ["Nitelikli personel ekibi her hâlde maddi olmayan duran varlık olarak aktifleştirilmek zorundadır",
   "Nitelikli personel ekibi her hâlde maddi duran varlık olarak sınıflandırılmak zorunda tutulur",
   "Nitelikli personel ekibi her hâlde şerefiye olarak ayrı biçimde muhasebeleştirilmek zorundadır",
   "Personelin becerilerinin ele alınışı TMS 38'de düzenlenmemiş bir husus niteliğindedir"],
  "TMS 38: işletme, nitelikli personelden oluşan bir ekibe sahip olabilir ve eğitimle personelin becerilerinin artacağını belirleyebilir. Ancak işletme, bu personelin kendisinde çalışmaya devam edeceği konusunda genellikle yeterli kontrole sahip olmadığından bu kalemler maddi olmayan duran varlık tanımını karşılamaz.",
  "TMS 38 - personel ve kontrol")

q("Maddi olmayan duran varlığın muhasebeleştirilme ölçütleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Gelecekteki ekonomik yararların işletmeye akışının muhtemel olması ve maliyetin güvenilir ölçülebilmesi gerekir",
  ["Yalnızca varlığın hukuken tescil edilmiş olması yeterli olup başka bir koşul aranmamaktadır",
   "Yalnızca varlığın bedelinin nakit olarak ödenmiş olması yeterli olup başka koşul aranmaz",
   "Yalnızca yönetimin varlık olarak kaydetmeye karar vermiş olması yeterli görülmektedir",
   "Muhasebeleştirme ölçütü bulunmayıp işletme dilediği kalemi serbestçe aktifleştirebilmektedir"],
  "TMS 38: bir maddi olmayan duran varlık, ancak (a) varlıkla ilişkilendirilen beklenilen gelecekteki ekonomik yararların işletme için gerçekleşmesinin muhtemel olması ve (b) varlığın maliyetinin güvenilir biçimde ölçülebilmesi durumunda muhasebeleştirilir.",
  "TMS 38 - muhasebeleştirme ölçütleri")

q("Maddi olmayan duran varlığın ilk muhasebeleştirilmesindeki ölçüm bakımından aşağıdakilerden hangisi doğrudur?",
  "Maliyet bedeliyle ölçülür",
  ["Gerçeğe uygun değeriyle ölçülür; maliyet bedeli hiçbir hâlde dikkate alınmamaktadır",
   "Net gerçekleşebilir değeriyle ölçülür; bu değer maliyetten her hâlde düşük olmaktadır",
   "Kullanım değeriyle ölçülür; bu değer beklenen nakit akışlarının bugünkü değerine dayanır",
   "İlk ölçüm esası TMS 38'de düzenlenmemiş olup işletmenin takdirine bırakılmış bir husustur"],
  "TMS 38: bir maddi olmayan duran varlık ilk muhasebeleştirilmesi sırasında maliyet bedeliyle ölçülür.",
  "TMS 38 - ilk ölçüm")

q("İşletme birleşmesinde edinilen maddi olmayan duran varlık bakımından aşağıdakilerden hangisi doğrudur?",
  "Birleşme tarihindeki gerçeğe uygun değeriyle ölçülür ve şerefiyeden ayrı muhasebeleştirilir",
  ["Her hâlde şerefiyenin içinde bırakılır; ayrı olarak muhasebeleştirilmesi mümkün olmamaktadır",
   "Her hâlde edinen işletmenin defterlerindeki maliyet bedeliyle ölçülmek zorunda tutulmaktadır",
   "Hiçbir biçimde muhasebeleştirilmez; yalnızca dipnotlarda açıklanmakla yetinilen bir kalemdir",
   "İşletme birleşmelerinde edinilen varlıklar TMS 38 kapsamı dışında olup düzenlenmemişlerdir"],
  "TMS 38: bir işletme birleşmesinde edinilen maddi olmayan duran varlığın maliyeti, birleşme tarihindeki gerçeğe uygun değeridir. Tanımlanabilirlik ölçütünü karşılıyorsa şerefiyeden ayrı olarak muhasebeleştirilir.",
  "TMS 38 - işletme birleşmesinde edinim")

q("Devlet teşviki yoluyla bedelsiz veya düşük bedelle edinilen maddi olmayan duran varlık bakımından aşağıdakilerden hangisi doğrudur?",
  "TMS 20 uyarınca gerçeğe uygun değeriyle veya nominal tutarla muhasebeleştirilebilir",
  ["Her hâlde sıfır değerle kaydedilmek zorunda olup hiçbir tutar aktifleştirilememektedir",
   "Her hâlde piyasa değerinin iki katı üzerinden kaydedilmek zorunda tutulan bir kalemdir",
   "Hiçbir biçimde muhasebeleştirilmez; yalnızca dipnotlarda açıklanmakla yetinilmektedir",
   "Devlet teşvikiyle edinim TMS 38 kapsamı dışında olup hiçbir standartta düzenlenmemiştir"],
  "TMS 38: bir maddi olmayan duran varlık, devlet teşviki yoluyla bedelsiz veya çok düşük bir bedelle edinilebilir. İşletme, hem varlığı hem teşviki gerçeğe uygun değeri üzerinden veya TMS 20 uyarınca nominal tutar ile muhasebeleştirmeyi seçebilir.",
  "TMS 38 - devlet teşvikiyle edinim")

q("Maddi olmayan duran varlığın maliyetine giren unsurlar bakımından aşağıdakilerden hangisi doğrudur?",
  "İndirimler düşülmüş alış fiyatı ile varlığı amaçlanan kullanıma hazır hâle getirmenin doğrudan maliyetleri dâhildir",
  ["Yalnızca alış fiyatı maliyete dâhil edilir; diğer tüm harcamalar gider yazılmak zorundadır",
   "İşletmenin tüm genel yönetim giderleri de maliyete dâhil edilmek zorunda tutulmuş bulunur",
   "Yalnızca nakit olarak ödenen tutarlar maliyete dâhil edilir; diğerleri dikkate alınmamaktadır",
   "Maliyet unsurları TMS 38'de düzenlenmemiş olup işletmenin takdirine bırakılmış bir husustur"],
  "TMS 38: ayrı olarak edinilen maddi olmayan duran varlığın maliyeti, ticari iskontolar ve indirimler düşüldükten sonra ithalat vergileri ve iade edilmeyen alış vergileri dâhil alış fiyatı ile varlığı amaçlanan kullanıma hazır hâle getirmeye ilişkin doğrudan atfedilebilir maliyetlerden oluşur.",
  "TMS 38 - maliyet unsurları")

q("Aşağıdakilerden hangisi maddi olmayan duran varlığın maliyetine DÂHİL EDİLMEZ?",
  "Yeni ürünün tanıtımına ilişkin reklam maliyetleri",
  ["Varlığı amaçlanan kullanıma hazır hâle getirmeye ilişkin doğrudan atfedilebilir nitelikteki maliyetler",
   "İndirimler ve ticari iskontolar düşüldükten sonra kalan alış fiyatı niteliğindeki tutarların tamamı",
   "Varlığın düzgün biçimde çalışıp çalışmadığının sınanmasına ilişkin test niteliğindeki maliyetler",
   "Varlığın oluşturulmasında görev alan çalışanlara sağlanan faydalardan doğan maliyet tutarları"],
  "TMS 38: yeni bir ürün veya hizmetin tanıtılmasına ilişkin maliyetler (reklam ve tanıtım faaliyetleri maliyetleri dâhil) maddi olmayan duran varlığın maliyetine dâhil edilmez; gider olarak muhasebeleştirilir.",
  "TMS 38 - maliyete girmeyen unsurlar")

q("Bir işletme, çalışanlarına verdiği mesleki eğitim için önemli tutarda harcama yapmıştır. TMS 38 bakımından aşağıdakilerden hangisi doğrudur?",
  "Eğitim harcamaları gider olarak muhasebeleştirilir",
  ["Eğitim harcamaları maddi olmayan duran varlık olarak aktifleştirilmek zorunda tutulmaktadır",
   "Eğitim harcamaları şerefiye olarak ayrı biçimde muhasebeleştirilmek zorunda bulunmaktadır",
   "Eğitim harcamaları doğrudan özkaynaklardan indirilmek zorunda olan bir kalemi ifade eder",
   "Eğitim harcamaları hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmaktadır"],
  "TMS 38: eğitim faaliyetlerine ilişkin harcamalar oluştuklarında gider olarak muhasebeleştirilir. İşletme, eğitilen personel üzerinde yeterli kontrole sahip olmadığından bu harcamalar varlık tanımını karşılamaz.",
  "TMS 38 - eğitim harcamaları (senaryo)")

q("Aşağıdakilerden hangileri TMS 38'e göre gider olarak muhasebeleştirilir?\n\nI. Reklam ve tanıtım harcamaları\n\nII. Personel eğitim harcamaları\n\nIII. İşletmenin kuruluş ve örgütlenme harcamaları",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 38 üçünü de gider olarak sayar: reklam ve tanıtım (I), eğitim (II) ve işletmenin kuruluş ve örgütlenme (kuruluş giderleri) harcamaları (III). Bunlar tanımlanabilir bir varlık oluşturmaz.",
  "TMS 38 - gider yazılan harcamalar")

q("Aşağıdaki ifadelerden hangileri TMS 38 bakımından doğrudur?\n\nI. Maddi olmayan duran varlık ilk olarak maliyetle ölçülür\n\nII. İşletme birleşmesinde edinilen varlık her durumda maliyet bedeliyle ölçülür\n\nIII. Nitelikli personel ekibi maddi olmayan duran varlık olarak muhasebeleştirilir",
  "Yalnız I",
  ["I, II ve III", "I ve II", "II ve III", "Yalnız III"],
  "Maddi olmayan duran varlık ilk olarak maliyetle ölçülür (I). İşletme birleşmesinde edinilen varlık edinme tarihindeki gerçeğe uygun değeriyle ölçüldüğünden II; personel üzerinde yeterli kontrol bulunmadığından III yanlıştır. Yalnız I doğrudur.",
  "TMS 38 - tanım ve ölçüm")

# ── B. İşletme içi yaratılan varlıklar, araştırma-geliştirme (16) ──────────
q("İşletme içinde yaratılan şerefiye bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlık olarak muhasebeleştirilmez",
  ["Her hâlde varlık olarak muhasebeleştirilip itfa edilmek zorunda tutulan bir kalemi ifade eder",
   "Her hâlde varlık olarak muhasebeleştirilir; ancak sınırsız ömürlü sayıldığından itfa edilmez",
   "Yalnızca güvenilir ölçülebildiğinde varlık olarak muhasebeleştirilmek zorunda bulunmaktadır",
   "İşletme içi yaratılan şerefiye TMS 38'de düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 38: işletme içinde yaratılan şerefiye varlık olarak muhasebeleştirilmez. İşletme tarafından kontrol edilen, tanımlanabilir ve maliyeti güvenilir biçimde ölçülebilen bir kaynak değildir.",
  "TMS 38 - işletme içi şerefiye")

q("İşletme içinde yaratılan marka, isim hakkı ve müşteri listeleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlık olarak muhasebeleştirilmez",
  ["Her hâlde varlık olarak muhasebeleştirilip itfa edilmek zorunda tutulan kalemleri ifade eder",
   "Yalnızca reklam harcaması yapılmışsa varlık olarak muhasebeleştirilmek zorunda bulunmaktadır",
   "Her hâlde şerefiye olarak ayrı biçimde muhasebeleştirilmek zorunda olan kalemleri ifade eder",
   "İşletme içi yaratılan bu kalemler TMS 38'de hiçbir biçimde ele alınmamış bulunmaktadır"],
  "TMS 38: işletme içi yaratılan markalar, yayın başlıkları, yayın hakları, müşteri listeleri ve özü itibarıyla benzer olan kalemler maddi olmayan duran varlık olarak muhasebeleştirilmez; bunların maliyeti işletmenin bir bütün olarak geliştirilmesinden ayırt edilemez.",
  "TMS 38 - işletme içi marka ve müşteri listesi")

q("Araştırma aşamasındaki harcamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Gider olarak muhasebeleştirilir; araştırma aşamasında hiçbir maddi olmayan duran varlık muhasebeleştirilmez",
  ["Her hâlde aktifleştirilip faydalı ömrü boyunca itfa edilmek zorunda tutulan harcamalardır",
   "Yalnızca proje başarıyla sonuçlanırsa geriye dönük olarak aktifleştirilmek zorunda kalınır",
   "Her hâlde doğrudan özkaynaklardan indirilmek zorunda olan bir harcama niteliğindedir",
   "Araştırma harcamalarının ele alınışı TMS 38'de düzenlenmemiş olup serbest bırakılmıştır"],
  "TMS 38: araştırmadan (veya işletme içi bir projenin araştırma safhasından) kaynaklanan hiçbir maddi olmayan duran varlık muhasebeleştirilmez. Araştırma harcamaları gerçekleştiğinde gider olarak muhasebeleştirilir.",
  "TMS 38 - araştırma harcamaları")

q("Geliştirme aşamasındaki harcamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Standartta sayılan koşulların tamamı sağlanıyorsa maddi olmayan duran varlık olarak muhasebeleştirilir",
  ["Her hâlde ve istisnasız gider olarak muhasebeleştirilmek zorunda olan harcamaları ifade eder",
   "Hiçbir koşul aranmaksızın her hâlde aktifleştirilmek zorunda tutulan harcamaları ifade eder",
   "Yalnızca vergi idaresi izin verdiğinde aktifleştirilebilen bir harcama niteliğinde bulunur",
   "Geliştirme harcamalarının ele alınışı TMS 38'de düzenlenmemiş bir husus niteliğindedir"],
  "TMS 38: geliştirmeden (veya işletme içi bir projenin geliştirme safhasından) kaynaklanan bir maddi olmayan duran varlık, ancak Standartta sayılan koşulların TAMAMININ varlığı hâlinde muhasebeleştirilir.",
  "TMS 38 - geliştirme harcamaları")

q("Geliştirme harcamalarının aktifleştirilme koşulları bakımından aşağıdakilerden hangisi doğrudur?",
  "Standartta sayılan altı koşulun tamamının birlikte sağlanması aranır",
  ["Yalnızca yönetimin projeyi tamamlama niyetinin bulunması yeterli olup diğer koşullar aranmaz",
   "Yalnızca harcamanın güvenilir biçimde ölçülebilmesi yeterli olup başka bir koşul aranmamaktadır",
   "Koşullardan herhangi birinin sağlanması yeterli olup tamamının birlikte bulunması aranmaz",
   "Aktifleştirme koşulları TMS 38'de sayılmamış olup işletmenin takdirine bırakılmış bulunur"],
  "TMS 38: geliştirme harcamalarının aktifleştirilebilmesi için altı koşulun TAMAMI sağlanmalıdır: teknik olarak tamamlanabilirlik, tamamlama ve kullanma/satma niyeti, kullanma veya satma imkânı, gelecekteki ekonomik yararı nasıl sağlayacağı, tamamlamak için yeterli teknik/mali kaynak ve harcamaların güvenilir ölçülebilmesi.",
  "TMS 38 - aktifleştirme koşulları")

q("Daha önce gider olarak muhasebeleştirilmiş bir harcama bakımından aşağıdakilerden hangisi doğrudur?",
  "Sonraki bir tarihte maddi olmayan duran varlığın maliyeti olarak aktifleştirilemez",
  ["Proje başarıyla sonuçlandığında geriye dönük olarak aktifleştirilmek zorunda tutulmaktadır",
   "Koşullar sonradan sağlandığında her hâlde varlığın maliyetine eklenmek zorunda kalınır",
   "İşletmenin talebi üzerine her zaman aktifleştirilebilen bir harcama niteliğinde bulunmaktadır",
   "Bu husus TMS 38'de düzenlenmemiş olup işletmenin takdirine bırakılmış bir konudur"],
  "TMS 38: bir maddi olmayan duran varlık kaleminde başlangıçta gider olarak muhasebeleştirilen harcamalar, daha sonraki bir tarihte maddi olmayan duran varlığın maliyetinin bir parçası olarak muhasebeleştirilmez.",
  "TMS 38 - gider yazılanın geri alınamaması")

q("Bir işletme, işletme içi bir projede araştırma ve geliştirme safhalarını birbirinden ayırt edemiyorsa aşağıdakilerden hangisi doğrudur?",
  "Harcamaların tamamı yalnızca araştırma safhasında yapılmış gibi değerlendirilir",
  ["Harcamaların tamamı yalnızca geliştirme safhasında yapılmış gibi değerlendirilip aktifleştirilir",
   "Harcamalar iki safha arasında her hâlde eşit olarak paylaştırılmak zorunda tutulmaktadır",
   "Bu durumda işletme projeyi hiçbir biçimde kayda alamaz; harcamalar dipnotta açıklanır",
   "Bu husus TMS 38'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 38: işletme içi bir projenin araştırma safhasını geliştirme safhasından ayırt edemediği durumlarda, söz konusu projeye ilişkin harcamalar sadece araştırma safhasında yapılmış gibi değerlendirilir; yani gider yazılır.",
  "TMS 38 - safhaların ayırt edilememesi")

ara, gel = 200_000, 300_000
q(f"Bir işletme yeni bir üretim yöntemi için toplam {tr(ara + gel)} TL harcamıştır. Bunun {tr(ara)} TL'si araştırma safhasına, {tr(gel)} TL'si ise TMS 38'deki koşulların tamamının sağlandığı geliştirme safhasına aittir. Aktifleştirilecek tutar kaç TL'dir?",
  f"{tr(gel)} TL",
  [f"{tr(ara + gel)} TL", f"{tr(ara)} TL", f"{tr((ara + gel) / 2)} TL", "0 TL"],
  f"TMS 38: araştırma harcamaları ({tr(ara)} TL) gider yazılır; araştırmadan hiçbir varlık muhasebeleştirilmez. Koşulların tamamı sağlanan geliştirme harcamaları ({tr(gel)} TL) ise aktifleştirilir. Aktifleştirilecek tutar = {tr(gel)} TL.",
  "TMS 38 - araştırma-geliştirme ayrımı")

once, sonra = 120_000, 360_000
q(f"Bir işletmenin geliştirme projesinde TMS 38'deki aktifleştirme koşulları yıl içinde belirli bir tarihte sağlanmıştır. Koşullar sağlanmadan önce {tr(once)} TL, sağlandıktan sonra {tr(sonra)} TL harcama yapılmıştır. Aktifleştirilecek tutar kaç TL'dir?",
  f"{tr(sonra)} TL",
  [f"{tr(once + sonra)} TL", f"{tr(once)} TL", f"{tr((once + sonra) / 2)} TL", "0 TL"],
  f"TMS 38: yalnızca aktifleştirme koşullarının sağlandığı tarihten SONRAKİ harcamalar varlığın maliyetine dâhil edilir. Koşullar sağlanmadan önce gider yazılan {tr(once)} TL sonradan geri alınıp aktifleştirilemez. Aktifleştirilecek tutar = {tr(sonra)} TL.",
  "TMS 38 - aktifleştirme tarihi")

q("İşletme içi yaratılan maddi olmayan duran varlığın maliyetine giren unsurlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Aktifleştirme koşullarının ilk kez sağlandığı tarihten sonra yapılan doğrudan ilişkilendirilebilir harcamalardır",
  ["Projenin başlangıcından itibaren yapılan tüm harcamalar her hâlde maliyete dâhil edilmektedir",
   "İşletmenin tüm genel yönetim giderleri de her hâlde maliyete dâhil edilmek zorunda kalınır",
   "Yalnızca projede kullanılan malzeme bedeli maliyete girer; işçilik hiçbir hâlde dâhil edilmez",
   "İşletme içi yaratılan varlığın maliyeti TMS 38'de düzenlenmemiş bir husus niteliğindedir"],
  "TMS 38: işletme içi yaratılan maddi olmayan duran varlığın maliyeti, varlığın muhasebeleştirme kriterlerini ilk kez karşıladığı tarihten sonra yapılan harcamaların toplamıdır. Satış, yönetim ve genel giderler ile başlangıçtaki faaliyet zararları maliyete dâhil edilmez.",
  "TMS 38 - işletme içi varlığın maliyeti")

q("Aşağıdakilerden hangisi TMS 38'e göre araştırma faaliyeti örneğidir?",
  "Yeni bilgi elde etmeye yönelik faaliyetler",
  ["Üretim öncesi prototipin tasarlanması, oluşturulması ve test edilmesi niteliğindeki faaliyetler",
   "Yeni teknolojiyi içeren araç, gereç ve kalıpların tasarımına ilişkin nitelikteki faaliyetler",
   "Ticari üretim için ekonomik olmayan bir pilot tesisin tasarlanıp kurulması niteliğinde faaliyet",
   "Yeni süreçler için seçilen bir alternatifin tasarlanıp test edilmesi niteliğindeki faaliyetler"],
  "TMS 38: araştırma faaliyeti örnekleri, yeni bilgi elde etmeye yönelik faaliyetler, araştırma bulgularının uygulanmasına yönelik araştırma ve alternatif arayışlarıdır. Diğer şıklardaki prototip, kalıp tasarımı, pilot tesis ve alternatif tasarımı GELİŞTİRME faaliyeti örnekleridir.",
  "TMS 38 - araştırma faaliyeti")

q("Aşağıdakilerden hangisi TMS 38'e göre geliştirme faaliyeti örneğidir?",
  "Üretim öncesi prototipin tasarlanması ve test edilmesi",
  ["Yeni bilgi elde etmek amacıyla yürütülen ve belirli bir ürüne yönelmemiş nitelikteki faaliyetler",
   "Araştırma bulgularının uygulanmasına yönelik olarak yürütülen araştırma niteliğindeki faaliyetler",
   "Ürün ve süreçler için alternatif arayışına yönelik olarak yürütülen nitelikteki faaliyetlerin tümü",
   "Yeni bilginin elde edilmesine yönelik olarak yapılan temel nitelikteki bilimsel çalışmalar"],
  "TMS 38: geliştirme faaliyeti örnekleri, üretim öncesi prototiplerin tasarımı/yapımı/test edilmesi, yeni teknolojili araç-gereç ve kalıpların tasarımı, ticari üretim için ekonomik olmayan pilot tesisin tasarımı ve seçilmiş alternatiflerin tasarlanıp test edilmesidir.",
  "TMS 38 - geliştirme faaliyeti")

q("Aşağıdakilerden hangileri TMS 38'e göre varlık olarak muhasebeleştirilMEZ?\n\nI. İşletme içinde yaratılan şerefiye\n\nII. İşletme içinde yaratılan marka\n\nIII. Araştırma safhası harcamaları",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "TMS 38 üçünü de varlık olarak muhasebeleştirmez: işletme içi yaratılan şerefiye (I), işletme içi yaratılan marka (II) ve araştırma safhası harcamaları (III). Bunlar gider yazılır.",
  "TMS 38 - muhasebeleştirilmeyen kalemler")

q("Aşağıdaki ifadelerden hangileri araştırma ve geliştirme bakımından doğrudur?\n\nI. Araştırma harcamaları gider yazılır\n\nII. Geliştirme harcamaları koşulların tamamı sağlanırsa aktifleştirilir\n\nIII. Gider yazılan harcama sonradan aktifleştirilebilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Araştırma harcamaları gider yazılır (I) ve geliştirme harcamaları altı koşulun tamamı sağlanırsa aktifleştirilir (II). Ancak başlangıçta gider olarak muhasebeleştirilen bir harcama sonraki bir tarihte varlığın maliyetine EKLENEMEZ; bu nedenle III yanlıştır.",
  "TMS 38 - araştırma-geliştirme")

q("Aşağıdaki ifadelerden hangileri TMS 38 bakımından doğrudur?\n\nI. Araştırma ve geliştirme safhaları ayırt edilemiyorsa harcama araştırma sayılır\n\nII. Satış ve genel yönetim giderleri işletme içi varlığın maliyetine dâhil edilmez\n\nIII. Prototip tasarımı bir araştırma faaliyetidir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Safhalar ayırt edilemiyorsa harcama araştırma safhasında yapılmış sayılır (I) ve satış/genel yönetim giderleri işletme içi varlığın maliyetine dâhil edilmez (II). Üretim öncesi prototipin tasarlanması ise bir GELİŞTİRME faaliyetidir; bu nedenle III yanlıştır.",
  "TMS 38 - araştırma-geliştirme")

# ── C. Faydalı ömür ve itfa (16) ───────────────────────────────────────────
q("Maddi olmayan duran varlığın faydalı ömrü bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme, faydalı ömrün sınırlı mı yoksa sınırsız mı olduğunu değerlendirir",
  ["Faydalı ömür her hâlde sınırlı kabul edilir; sınırsız ömür TMS 38'de öngörülmemiş bulunmaktadır",
   "Faydalı ömür her hâlde sınırsız kabul edilir; sınırlı ömür TMS 38'de öngörülmemiş bulunmaktadır",
   "Faydalı ömür her hâlde ve istisnasız beş yıl olarak kabul edilmek zorunda tutulmaktadır",
   "Faydalı ömrün değerlendirilmesi TMS 38'de düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 38: işletme, bir maddi olmayan duran varlığın faydalı ömrünün sınırlı mı sınırsız mı olduğunu değerlendirir; sınırlıysa faydalı ömrün uzunluğunu veya varlığı oluşturan üretim ya da benzer birim sayısını belirler.",
  "TMS 38 - faydalı ömür değerlendirmesi")

q("Sınırsız faydalı ömürlü maddi olmayan duran varlık bakımından aşağıdakilerden hangisi doğrudur?",
  "İtfa edilmez; her yıl ve değer düşüklüğü belirtisi olduğunda değer düşüklüğü testine tabi tutulur",
  ["Her hâlde ve istisnasız beş yılda itfa edilmek zorunda olan bir varlığı ifade etmektedir",
   "Her hâlde itfa edilir; ancak itfa süresi işletmenin serbest takdirine bırakılmış bulunmaktadır",
   "İtfa edilmez ve hiçbir hâlde değer düşüklüğü testine de tabi tutulmamaktadır",
   "Sınırsız ömürlü varlıklar her hâlde bilanço dışı bırakılmak zorunda tutulan kalemleri ifade eder"],
  "TMS 38: sınırsız faydalı ömre sahip bir maddi olmayan duran varlık itfaya tabi tutulmaz. İşletme, TMS 36 uyarınca bu varlığın değer düşüklüğüne uğrayıp uğramadığını yıllık olarak ve değer düşüklüğü belirtisi bulunduğunda test eder.",
  "TMS 38 - sınırsız ömür")

q("'Sınırsız faydalı ömür' ifadesinin anlamı bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlığın ömrünün sonsuz olduğu değil, öngörülebilir bir sınırının bulunmadığı anlamına gelir",
  ["Varlığın ömrünün matematiksel olarak sonsuz olduğu ve hiç tükenmeyeceği anlamına gelmektedir",
   "Varlığın ömrünün en az yüz yıl olduğu ve bu süre içinde tükenmeyeceği anlamına gelmektedir",
   "Varlığın hiçbir hâlde değer kaybetmeyeceği ve değerinin sürekli artacağı anlamına gelmektedir",
   "Bu ifade TMS 38'de tanımlanmamış olup uygulamada hiçbir anlam taşımayan bir kavramdır"],
  "TMS 38: 'sınırsız' terimi 'sonsuz' anlamına gelmez. Bir varlığın faydalı ömrü, ilgili tüm faktörlerin analizi sonucunda işletmeye net nakit girişi sağlaması beklenen sürenin öngörülebilir bir sınırı bulunmadığında sınırsız kabul edilir.",
  "TMS 38 - sınırsız kavramı")

q("Sınırsız ömür değerlendirmesinin gözden geçirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Her dönem gözden geçirilir; ömür sınırlıya dönerse bu bir muhasebe tahmini değişikliğidir",
  ["Sınırsız ömür değerlendirmesi bir kez yapıldıktan sonra hiçbir hâlde değiştirilememektedir",
   "Ömrün sınırlıya dönmesi bir muhasebe politikası değişikliği olup geriye dönük uygulanmaktadır",
   "Ömrün sınırlıya dönmesi önceki dönem hatası sayılıp geriye dönük düzeltilmek zorundadır",
   "Sınırsız ömrün gözden geçirilmesi TMS 38'de düzenlenmemiş bir husus niteliğinde bulunur"],
  "TMS 38: itfaya tabi tutulmayan bir maddi olmayan duran varlığın faydalı ömrü, olayların ve şartların sınırsız faydalı ömür değerlendirmesini desteklemeye devam edip etmediğini belirlemek için her dönem gözden geçirilir. Sınırsızdan sınırlıya değişim, TMS 8 uyarınca muhasebe tahminindeki değişikliktir.",
  "TMS 38 - sınırsızdan sınırlıya geçiş")

q("Sınırlı faydalı ömürlü maddi olmayan duran varlığın itfası bakımından aşağıdakilerden hangisi doğrudur?",
  "İtfaya tabi tutulur; itfa edilebilir tutar faydalı ömrü boyunca sistematik olarak dağıtılır",
  ["İtfa edilmez; sınırlı ömürlü varlıklar yalnızca değer düşüklüğü testine tabi tutulmaktadır",
   "Her hâlde ve istisnasız tek seferde tümüyle gider yazılmak zorunda olan bir varlığı ifade eder",
   "Yalnızca satıldığında itfa edilir; elde tutulduğu sürece hiçbir itfa payı ayrılmamaktadır",
   "Sınırlı ömürlü varlıkların itfası TMS 38'de düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 38: sınırlı faydalı ömre sahip bir maddi olmayan duran varlığın itfaya tabi tutarı, faydalı ömrü boyunca sistematik olarak dağıtılır.",
  "TMS 38 - sınırlı ömür itfası")

q("İtfaya başlanacak tarih bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlık kullanıma hazır olduğunda, yani yönetimin amaçladığı biçimde faaliyet gösterebildiğinde başlar",
  ["Varlığın bedelinin tamamı ödendiğinde başlar; ödeme tamamlanmadıkça itfa ayrılmamaktadır",
   "Varlığın hukuki tescili tamamlandığında başlar; kullanıma hazır olması yeterli sayılmaz",
   "Varlık fiilen gelir getirmeye başladığında başlar; hazır olması hiç dikkate alınmamaktadır",
   "İtfaya başlama tarihi TMS 38'de düzenlenmemiş olup işletmenin takdirine bırakılmıştır"],
  "TMS 38: itfa, varlık kullanıma hazır olduğunda, yani yönetimin amaçladığı biçimde faaliyet gösterebilmesi için gerekli konum ve durumda olduğunda başlar.",
  "TMS 38 - itfaya başlama")

q("Maddi olmayan duran varlığın kalıntı değeri bakımından aşağıdakilerden hangisi doğrudur?",
  "Üçüncü kişinin satın alma taahhüdü veya aktif piyasa bulunmadıkça sıfır kabul edilir",
  ["Her hâlde maliyetin belirli bir yüzdesi olarak hesaplanmak zorunda tutulan bir tutarı ifade eder",
   "Her hâlde varlığın gerçeğe uygun değerine eşit kabul edilmek zorunda olan bir tutarı ifade eder",
   "Kalıntı değer hiçbir hâlde sıfır olamaz; her varlık için mutlaka pozitif bir tutar belirlenir",
   "Maddi olmayan duran varlıklarda kalıntı değer TMS 38'de düzenlenmemiş bir husustur"],
  "TMS 38: sınırlı faydalı ömre sahip bir maddi olmayan duran varlığın kalıntı değeri, (a) üçüncü bir kişinin varlığı faydalı ömrünün sonunda satın alma taahhüdü bulunmadıkça veya (b) varlık için aktif bir piyasa bulunmadıkça sıfır kabul edilir.",
  "TMS 38 - kalıntı değer")

q("İtfa süresi ve itfa yönteminin gözden geçirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "En az her hesap dönemi sonunda gözden geçirilir; değişiklik tahmin değişikliği olarak ele alınır",
  ["İtfa süresi ve yöntemi bir kez belirlendikten sonra hiçbir hâlde değiştirilememektedir",
   "İtfa süresi ve yöntemi değişikliği muhasebe politikası değişikliği sayılıp geriye dönük uygulanır",
   "İtfa süresi ve yöntemi yalnızca vergi idaresi talep ettiğinde gözden geçirilmek zorundadır",
   "İtfa süresi ve yönteminin gözden geçirilmesi TMS 38'de düzenlenmemiş bir husus niteliğindedir"],
  "TMS 38: sınırlı faydalı ömürlü bir maddi olmayan duran varlığın itfa süresi ve itfa yöntemi, en az her hesap dönemi sonunda gözden geçirilir. Değişiklikler TMS 8 uyarınca muhasebe tahminindeki değişiklik olarak muhasebeleştirilir.",
  "TMS 38 - itfa süresi ve yönteminin gözden geçirilmesi")

q("Hasılata dayalı itfa yöntemi bakımından aşağıdakilerden hangisi doğrudur?",
  "Uygun olmadığına ilişkin bir karine bulunur; yalnızca sınırlı hâllerde bu karine çürütülebilir",
  ["Hasılata dayalı yöntem her hâlde ve tercihen kullanılması gereken bir yöntemi ifade etmektedir",
   "Hasılata dayalı yöntem doğrusal itfa yöntemiyle her bakımdan eşdeğer kabul edilen bir yöntemdir",
   "Hasılata dayalı yöntem yalnızca büyük ölçekli işletmelerce kullanılabilen bir yöntemi ifade eder",
   "Hasılata dayalı itfa yöntemi TMS 38'de hiçbir biçimde ele alınmamış olup serbest bırakılmıştır"],
  "TMS 38: varlığın kullanımını içeren bir faaliyetten elde edilen hasılata dayalı bir itfa yönteminin uygun olmadığına ilişkin bir karine vardır. Bu karine yalnızca sınırlı durumlarda çürütülebilir (maddi olmayan duran varlığın hasılatın ölçüsü olarak ifade edilmesi veya hasılat ile tüketimin yakından ilişkili olduğunun gösterilmesi).",
  "TMS 38 - hasılata dayalı itfa")

q("İtfa yöntemleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Doğrusal, azalan bakiyeler ve üretim birimi yöntemleri kullanılabilir",
  ["Yalnızca doğrusal itfa yöntemi kullanılabilir; diğer yöntemler kabul edilmemiş bulunmaktadır",
   "Yalnızca azalan bakiyeler yöntemi kullanılabilir; doğrusal yöntem kesin olarak yasaklanmıştır",
   "İtfa yöntemi her hâlde vergi mevzuatına göre seçilir; TMS 38'in bir hükmü bulunmamaktadır",
   "İtfa yöntemleri TMS 38'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmıştır"],
  "TMS 38: kullanılabilecek itfa yöntemleri doğrusal itfa yöntemi, azalan bakiyeler yöntemi ve üretim birimi yöntemidir. Tüketim biçimi güvenilir olarak belirlenemiyorsa doğrusal yöntem kullanılır.",
  "TMS 38 - itfa yöntemleri")

q("Ekonomik yararların tüketim biçiminin güvenilir olarak belirlenememesi hâlinde aşağıdakilerden hangisi doğrudur?",
  "Doğrusal itfa yöntemi kullanılır",
  ["Azalan bakiyeler yöntemi kullanılmak zorunda olup başka bir yöntem uygulanamamaktadır",
   "Varlık itfa edilmeden bırakılır; tüketim biçimi belirlenene kadar itfa payı ayrılmamaktadır",
   "Varlık tek seferde tümüyle gider yazılmak zorunda olup itfa söz konusu olmamaktadır",
   "Bu husus TMS 38'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmış bulunmaktadır"],
  "TMS 38: gelecekteki ekonomik yararların tüketim biçimi güvenilir olarak belirlenemiyorsa doğrusal itfa yöntemi kullanılır.",
  "TMS 38 - tüketim biçimi belirlenemezse")

mal38, om38 = 480_000, 8
itfa38 = mal38 / om38
q(f"Bir işletme {tr(mal38)} TL'ye bir lisans satın almıştır. Lisansın faydalı ömrü {om38} yıl olup kalıntı değeri sıfırdır. Doğrusal yönteme göre yıllık itfa payı kaç TL'dir?",
  f"{tr(itfa38)} TL",
  [f"{tr(mal38 / 5)} TL", f"{tr(mal38 / 10)} TL", f"{tr(mal38)} TL", f"{tr(mal38 / om38 / 2)} TL"],
  f"Doğrusal itfada yıllık itfa payı = (Maliyet − Kalıntı değer) ÷ Faydalı ömür. Kalıntı değer sıfır olduğundan = {tr(mal38)} ÷ {om38} = {tr(itfa38)} TL.",
  "TMS 38 - itfa hesabı")

pat, tsc, rek38 = 400_000, 30_000, 50_000
malp = pat + tsc
q(f"Bir işletme bir patenti {tr(pat)} TL'ye satın almış; devir ve tescil işlemleri için {tr(tsc)} TL hukuki masraf, patentli ürünün tanıtımı için de {tr(rek38)} TL reklam harcaması yapmıştır. Patentin TMS 38'e göre maliyeti kaç TL'dir?",
  f"{tr(malp)} TL",
  [f"{tr(pat + tsc + rek38)} TL", f"{tr(pat + rek38)} TL", f"{tr(pat)} TL", f"{tr(tsc + rek38)} TL"],
  f"Maliyet = Alış fiyatı + Varlığı amaçlanan kullanıma hazır hâle getirmenin doğrudan maliyetleri = {tr(pat)} + {tr(tsc)} = {tr(malp)} TL. Reklam harcaması ({tr(rek38)} TL) TMS 38 uyarınca maliyete dâhil edilmez; gider yazılır.",
  "TMS 38 - maliyet hesabı")

q("Bir işletmenin sınırsız faydalı ömürlü olarak değerlendirdiği bir marka hakkı bulunmaktadır. TMS 38 bakımından aşağıdakilerden hangisi doğrudur?",
  "Marka itfa edilmez; yıllık olarak değer düşüklüğü testine tabi tutulur",
  ["Marka her hâlde beş yılda itfa edilmek zorunda olup değer düşüklüğü testi uygulanmamaktadır",
   "Marka her hâlde on yılda itfa edilmek zorunda olup ayrıca test yapılmasına gerek bulunmaz",
   "Marka itfa edilmez ve hiçbir hâlde değer düşüklüğü testine de tabi tutulmamaktadır",
   "Marka her hâlde bilanço dışı bırakılmak zorunda olup aktifte tutulması mümkün değildir"],
  "TMS 38: sınırsız faydalı ömürlü maddi olmayan duran varlık itfaya tabi tutulmaz. Bunun yerine TMS 36 uyarınca yıllık olarak ve değer düşüklüğü belirtisi bulunduğunda değer düşüklüğü testine tabi tutulur.",
  "TMS 38 - sınırsız ömür (senaryo)")

q("Aşağıdakilerden hangileri TMS 38'e göre itfa yöntemi olarak kullanılabilir?\n\nI. Doğrusal itfa yöntemi\n\nII. Azalan bakiyeler yöntemi\n\nIII. Varlığın kullanımını içeren faaliyetten elde edilen hasılata dayalı yöntem",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "TMS 38 doğrusal itfa (I) ve azalan bakiyeler (II) yöntemlerini sayar; üçüncü yöntem ise üretim birimi yöntemidir. Varlığın kullanımını içeren faaliyetten elde edilen hasılata dayalı yöntemin (III) uygun OLMADIĞINA ilişkin bir karine bulunur; bu nedenle yanlıştır.",
  "TMS 38 - itfa yöntemleri")

q("Aşağıdaki ifadelerden hangileri faydalı ömür ve itfa bakımından doğrudur?\n\nI. Sınırsız ömürlü varlık itfa edilmez\n\nII. Sınırsız ömürlü varlık yıllık değer düşüklüğü testine tabidir\n\nIII. 'Sınırsız' ifadesi ömrün sonsuz olduğu anlamına gelir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Sınırsız ömürlü varlık itfa edilmez (I) ve yıllık olarak değer düşüklüğü testine tabi tutulur (II). Ancak 'sınırsız' terimi 'SONSUZ' anlamına gelmez; net nakit girişi süresinin öngörülebilir bir sınırının bulunmadığını ifade eder. Bu nedenle III yanlıştır.",
  "TMS 38 - faydalı ömür")

# ── D. Sonraki ölçüm, bilanço dışı bırakma, açıklamalar (14) ───────────────
q("Maddi olmayan duran varlığın sonraki ölçümü bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme maliyet modelini veya yeniden değerleme modelini muhasebe politikası olarak seçer",
  ["Yalnızca maliyet modeli kullanılabilir; yeniden değerleme modeli TMS 38'de öngörülmemiştir",
   "Yalnızca yeniden değerleme modeli kullanılabilir; maliyet modeli kesin olarak yasaklanmıştır",
   "İki model de aynı anda ve birlikte kullanılmak zorunda olup tek model yeterli görülmemektedir",
   "Sonraki ölçüm esası TMS 38'de düzenlenmemiş olup işletmenin serbest takdirine bırakılmıştır"],
  "TMS 38: işletme, muhasebe politikası olarak maliyet modelini veya yeniden değerleme modelini seçer ve bu politikayı ilgili maddi olmayan duran varlık sınıfının tamamına uygular.",
  "TMS 38 - sonraki ölçüm modelleri")

q("Maddi olmayan duran varlıklarda yeniden değerleme modelinin uygulanabilme koşulu bakımından aşağıdakilerden hangisi doğrudur?",
  "Gerçeğe uygun değerin aktif bir piyasaya göre belirlenmesi gerekir",
  ["Yeniden değerleme modeli hiçbir koşul aranmaksızın her varlığa uygulanabilmektedir",
   "Yeniden değerleme modeli yalnızca yönetimin tahminine dayanılarak uygulanabilmektedir",
   "Yeniden değerleme modeli yalnızca vergi idaresinin belirlediği değerlerle uygulanabilir",
   "Yeniden değerleme modelinin koşulu TMS 38'de düzenlenmemiş bir husus niteliğindedir"],
  "TMS 38: yeniden değerleme modelinde gerçeğe uygun değer aktif bir piyasaya göre belirlenir. Maddi olmayan duran varlıklar için aktif piyasa bulunması alışılmış bir durum olmadığından bu model nadiren uygulanır.",
  "TMS 38 - aktif piyasa koşulu")

q("Maliyet modeli bakımından aşağıdakilerden hangisi doğrudur?",
  "Varlık, maliyetinden birikmiş itfa ve birikmiş değer düşüklüğü zararları indirilerek gösterilir",
  ["Varlık her hâlde gerçeğe uygun değeriyle gösterilir; birikmiş itfa dikkate alınmamaktadır",
   "Varlık her hâlde ilk maliyetiyle gösterilir; birikmiş itfa hiçbir hâlde indirilmemektedir",
   "Varlık net gerçekleşebilir değeriyle gösterilir; maliyet bilgisi hiç dikkate alınmamaktadır",
   "Maliyet modeli TMS 38'de tanımlanmamış olup uygulamada kullanılmayan bir modeli ifade eder"],
  "TMS 38: maliyet modelinde bir maddi olmayan duran varlık, ilk muhasebeleştirmeden sonra maliyetinden birikmiş itfa ve birikmiş değer düşüklüğü zararları indirilerek gösterilir.",
  "TMS 38 - maliyet modeli")

q("Maddi olmayan duran varlığın bilanço dışı bırakılması bakımından aşağıdakilerden hangisi doğrudur?",
  "Elden çıkarıldığında veya kullanımından ya da elden çıkarılmasından gelecekte ekonomik yarar beklenmediğinde bilanço dışı bırakılır",
  ["Varlık yalnızca hukuki koruma süresi dolduğunda bilanço dışı bırakılabilen bir kalemdir",
   "Varlık hiçbir hâlde bilanço dışı bırakılamaz; faydalı ömür sonunda dahi kayıtlarda kalmaktadır",
   "Varlık yalnızca vergi idaresi izin verdiğinde bilanço dışı bırakılabilen bir kalem niteliğindedir",
   "Bilanço dışı bırakma koşulları TMS 38'de düzenlenmemiş olup serbest bırakılmış bulunmaktadır"],
  "TMS 38: bir maddi olmayan duran varlık, (a) elden çıkarıldığında veya (b) kullanımından ya da elden çıkarılmasından gelecekte ekonomik yarar beklenmediğinde finansal durum tablosu dışı bırakılır.",
  "TMS 38 - bilanço dışı bırakma")

q("Maddi olmayan duran varlığın bilanço dışı bırakılmasından doğan kazanç veya kayıp bakımından aşağıdakilerden hangisi doğrudur?",
  "Kâr veya zarara dâhil edilir; ancak kazanç hasılat olarak sınıflandırılmaz",
  ["Kazanç her hâlde hasılat olarak sınıflandırılıp gelir tablosunun en üstünde gösterilmektedir",
   "Kazanç veya kayıp her hâlde diğer kapsamlı gelirde muhasebeleştirilmek zorunda tutulmuştur",
   "Kazanç veya kayıp hiçbir biçimde kayda alınmaz; yalnızca dipnotlarda açıklanmaktadır",
   "Kazanç veya kayıp doğrudan özkaynaklardan indirilmek zorunda olan bir kalemi ifade eder"],
  "TMS 38: bir maddi olmayan duran varlığın bilanço dışı bırakılmasından doğan kazanç veya kayıp, net elden çıkarma hasılatı ile varlığın defter değeri arasındaki fark olarak belirlenir ve kâr veya zarara dâhil edilir. Kazançlar hasılat olarak sınıflandırılmaz.",
  "TMS 38 - bilanço dışı bırakma kazancı")

malb, itfab, satb = 300_000, 180_000, 150_000
nddb = malb - itfab
karb = satb - nddb
q(f"Maliyeti {tr(malb)} TL ve birikmiş itfası {tr(itfab)} TL olan bir lisans {tr(satb)} TL'ye satılmıştır. Bu satıştan doğan kazanç veya kayıp kaç TL'dir?",
  f"{tr(karb)} TL kazanç",
  [f"{tr(satb)} TL kazanç; satış bedelinin tamamı kazanç olarak kâr veya zarara yansıtılmaktadır",
   f"{tr(malb - satb)} TL kayıp; maliyet ile satış bedeli arasındaki fark kayıp olarak kaydedilir",
   f"{tr(karb)} TL kayıp; net defter değeri satış bedelinin üzerinde olduğundan kayıp doğmaktadır",
   f"{tr(itfab - satb)} TL kazanç; birikmiş itfa ile satış bedeli karşılaştırılarak bulunmaktadır"],
  f"Net defter değeri = Maliyet − Birikmiş itfa = {tr(malb)} − {tr(itfab)} = {tr(nddb)} TL. Kazanç = Satış bedeli − Net defter değeri = {tr(satb)} − {tr(nddb)} = {tr(karb)} TL kazanç. Kâr veya zarara dâhil edilir; hasılat sayılmaz.",
  "TMS 38 - satış kazancı hesabı")

q("Maddi olmayan duran varlıklarda değer düşüklüğü bakımından aşağıdakilerden hangisi doğrudur?",
  "Değer düşüklüğünün belirlenmesinde TMS 36 uygulanır",
  ["Değer düşüklüğü TMS 38'de ayrıntılı düzenlenmiş olup başka bir standarda başvurulmamaktadır",
   "Maddi olmayan duran varlıklarda hiçbir hâlde değer düşüklüğü söz konusu olmamaktadır",
   "Değer düşüklüğü yalnızca stoklar için söz konusu olup duran varlıklara uygulanmamaktadır",
   "Değer düşüklüğü yalnızca vergi mevzuatına göre belirlenir; hiçbir standart hükmü yoktur"],
  "TMS 38: bir maddi olmayan duran varlığın değer düşüklüğüne uğrayıp uğramadığının belirlenmesinde işletme TMS 36 Varlıklarda Değer Düşüklüğü Standardını uygular.",
  "TMS 38 - değer düşüklüğü")

q("Henüz kullanıma hazır olmayan maddi olmayan duran varlıklar bakımından aşağıdakilerden hangisi doğrudur?",
  "İtfa edilmez; yıllık olarak değer düşüklüğü testine tabi tutulur",
  ["Her hâlde itfa edilmeye başlanır; kullanıma hazır olması hiç dikkate alınmamaktadır",
   "Her hâlde tek seferde tümüyle gider yazılmak zorunda olan kalemleri ifade etmektedir",
   "Hiçbir biçimde aktifleştirilemez; yalnızca dipnotlarda açıklanmakla yetinilmektedir",
   "Bu varlıkların ele alınışı TMS 38'de düzenlenmemiş bir husus niteliğinde bulunmaktadır"],
  "TMS 38 ve TMS 36: henüz kullanıma hazır olmayan bir maddi olmayan duran varlık itfaya başlanmamıştır ve yıllık olarak değer düşüklüğü testine tabi tutulur.",
  "TMS 38 - kullanıma hazır olmayan varlık")

q("Maddi olmayan duran varlıklara ilişkin açıklamalar bakımından aşağıdakilerden hangisi doğrudur?",
  "Her varlık sınıfı için ömrün sınırlı mı sınırsız mı olduğu, itfa süreleri, yöntemleri ve defter değeri hareketleri açıklanır",
  ["Maddi olmayan duran varlıklar hakkında hiçbir açıklama yapılmaz; yalnızca tutar gösterilir",
   "Yalnızca varlıkların toplam tutarı açıklanır; sınıf bazında hiçbir bilgi verilmemektedir",
   "Yalnızca vergi idaresine bildirim yapılır; finansal tablo kullanıcılarına açıklama yapılmaz",
   "Açıklama yalnızca yeniden değerleme modeli uygulayan işletmeler için zorunlu tutulmuştur"],
  "TMS 38: işletme, işletme içi yaratılanlar ile diğerlerini ayırarak her bir maddi olmayan duran varlık sınıfı için faydalı ömrün sınırlı mı sınırsız mı olduğunu, sınırlıysa faydalı ömürleri veya itfa oranlarını, kullanılan itfa yöntemlerini ve defter değeri mutabakatını açıklar.",
  "TMS 38 - açıklamalar")

q("Araştırma ve geliştirme harcamalarının açıklanması bakımından aşağıdakilerden hangisi doğrudur?",
  "Dönem içinde gider olarak muhasebeleştirilen araştırma ve geliştirme harcamalarının toplam tutarı açıklanır",
  ["Araştırma ve geliştirme harcamaları hakkında hiçbir açıklama yapılmasına gerek bulunmamaktadır",
   "Yalnızca aktifleştirilen tutar açıklanır; gider yazılan tutar hiçbir hâlde açıklanmamaktadır",
   "Yalnızca vergi idaresine bildirim yapılır; finansal tablo kullanıcılarına açıklama yapılmaz",
   "Açıklama yalnızca araştırma harcaması bulunan işletmeler için zorunlu tutulmuş bulunmaktadır"],
  "TMS 38: işletme, dönem boyunca gider olarak muhasebeleştirilen araştırma ve geliştirme harcamalarının toplam tutarını açıklar.",
  "TMS 38 - araştırma-geliştirme açıklaması")

q("Bir işletme, sınırsız ömürlü olarak değerlendirdiği bir varlığın ömrünün artık sınırlı olduğu sonucuna varmıştır. TMS 38 bakımından aşağıdakilerden hangisi doğrudur?",
  "Değişiklik tahmin değişikliğidir; varlık ileriye dönük olarak itfa edilmeye başlanır",
  ["Değişiklik muhasebe politikası değişikliği olup geriye dönük uygulanmak zorunda tutulmuştur",
   "Değişiklik önceki dönem hatası sayılır ve geçmiş dönem tabloları yeniden düzenlenmektedir",
   "Varlık sınırsız ömürlü olarak değerlendirildiğinden hiçbir hâlde itfa edilememektedir",
   "Bu durumda varlık her hâlde bilanço dışı bırakılmak zorunda olup itfa söz konusu olmaz"],
  "TMS 38: sınırsız faydalı ömür değerlendirmesinin sınırlı faydalı ömre değiştirilmesi, TMS 8 uyarınca muhasebe tahminindeki değişikliktir; ileriye dönük uygulanır. Bu değişim aynı zamanda TMS 36 uyarınca değer düşüklüğü testi yapılmasını gerektiren bir göstergedir.",
  "TMS 38 - sınırsızdan sınırlıya (senaryo)")

q("Aşağıdaki ifadelerden hangileri TMS 38 bakımından doğrudur?\n\nI. Yeniden değerleme modeli aktif piyasa varlığını gerektirir\n\nII. Bilanço dışı bırakmadan doğan kazanç hasılat sayılmaz\n\nIII. Sınırsız faydalı ömürlü varlık her yıl itfa edilir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Yeniden değerleme modelinde gerçeğe uygun değer aktif piyasaya göre belirlenir (I) ve bilanço dışı bırakma kazancı kâr/zarara dâhil edilir ancak hasılat sayılmaz (II). Sınırsız faydalı ömürlü varlık ise İTFA EDİLMEZ; yıllık değer düşüklüğü testine tabi tutulur. Bu nedenle III yanlıştır.",
  "TMS 38 - genel")

q("Aşağıdaki ifadelerden hangileri TMS 38 bakımından doğrudur?\n\nI. Kalıntı değer kural olarak sıfır kabul edilir\n\nII. İtfa varlık kullanıma hazır olduğunda başlar\n\nIII. Maddi olmayan duran varlıklarda aktif piyasa bulunması olağan bir durumdur",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Kalıntı değer, üçüncü kişi taahhüdü veya aktif piyasa yoksa sıfır kabul edilir (I) ve itfa varlık kullanıma hazır olduğunda başlar (II). Maddi olmayan duran varlıklar için aktif piyasa bulunması ise ALIŞILMIŞ bir durum DEĞİLDİR; bu nedenle III yanlıştır.",
  "TMS 38 - genel")

q("Bir işletme, satın aldığı bir işletmenin müşteri listesini işletme birleşmesi kapsamında edinmiştir. TMS 38 bakımından aşağıdakilerden hangisi doğrudur?",
  "Tanımlanabilirlik ölçütünü karşılıyorsa şerefiyeden ayrı olarak gerçeğe uygun değeriyle muhasebeleştirilir",
  ["Müşteri listesi her hâlde şerefiyenin içinde bırakılır; ayrı muhasebeleştirilmesi mümkün değildir",
   "Müşteri listesi her hâlde gider yazılır; edinilmiş olması hiçbir biçimde değiştirmemektedir",
   "Müşteri listesi hiçbir hâlde varlık sayılamaz; yalnızca dipnotlarda açıklanmakla yetinilir",
   "Müşteri listesi her hâlde maddi duran varlık olarak sınıflandırılmak zorunda tutulmaktadır"],
  "TMS 38: İŞLETME İÇİNDE yaratılan müşteri listeleri varlık olarak muhasebeleştirilmez. Ancak işletme birleşmesinde EDİNİLEN müşteri listesi, tanımlanabilirlik ölçütünü karşılıyorsa birleşme tarihindeki gerçeğe uygun değeriyle şerefiyeden ayrı muhasebeleştirilir. Ayrım, kalemin işletme içi yaratılmış olup olmamasındadır.",
  "TMS 38 - edinilen müşteri listesi (senaryo)")

q("Maddi olmayan duran varlık sınıfı bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin faaliyetlerinde benzer nitelikte ve kullanıma sahip varlıkların gruplandırılmasıdır",
  ["İşletmenin en pahalı maddi olmayan varlıklarının bir araya getirilmesini ifade eden kavramdır",
   "İşletmenin aynı yılda edindiği varlıkların bir araya getirilmesini ifade eden bir kavramdır",
   "İşletmenin aynı kişiden edindiği varlıkların gruplandırılmasını ifade eden bir kavramdır",
   "Varlık sınıfı kavramı TMS 38'de tanımlanmamış olup uygulamada kullanılmamaktadır"],
  "TMS 38: maddi olmayan duran varlık sınıfı, bir işletmenin faaliyetlerinde benzer nitelik ve kullanıma sahip varlıkların gruplandırılmasıdır (marka, yazılım, lisans, telif hakkı, patent gibi).",
  "TMS 38 - varlık sınıfı")

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
                       "styleRef": "SGS Muhasebe Standartları (TMS 38; yapısal)",
                       "legislationRef": it["ref"]},
            "validYear": 2026, "mockExamId": None,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in out if len(MARK.findall(x["stem"])) >= 2]
    hepsi = sum(1 for x in onc if x["options"][x["answer"]].strip() == "I, II ve III")
    print(f"yazıldı {len(out)} | öncüllü {len(onc)} hepsi {hepsi} ({hepsi*100//max(len(onc),1)}%) | harf {''.join(x['answer'] for x in out)[:40]}…")
