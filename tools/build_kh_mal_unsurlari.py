# -*- coding: utf-8 -*-
"""Yeterlilik KONU HAVUZU — Maliyet Muhasebesi / Maliyet Unsurları (60 soru = 3×20).
Doğru şık KISA, çeldiriciler UZUN. explanation'da harf atıfı YOK.
Aritmetik python'da hesaplanır. Yıla bağlı oran/tutar YOK."""
import json, random, re

L, T, LBL = "maliyet_muhasebesi", "maliyet_unsurlari", "Maliyet Unsurları"
PREFIX, SEED = "kh-mal-unsur", 20260902
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/yeterlilik/questions_topic_maliyet_unsurlari_2026.json"

Q = []


def q(stem, correct, distractors, why, ref, difficulty="medium"):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(stem=stem, correct=correct, distractors=distractors, why=why,
                  ref=ref, difficulty=difficulty))


def tr(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9:
        v = round(v)
    return f"{v:,}".replace(",", ".")


# ── A. Direkt ilk madde ve malzeme (20) ──────────────────────────────────
q("Özel ölçülerle üretilen bir makinenin gövdesinde kullanılan ve hangi siparişte tüketildiği malzeme istek fişiyle izlenen çelik levha nasıl sınıflandırılır?",
  "Direkt ilk madde ve malzeme gideri",
  ["Üretimle bağlantısı bulunmayan genel yönetim gideri olarak doğrudan dönem sonucuna aktarılır",
   "Mamulle ilişkisi kurulamadığı için değişken genel üretim gideri içinde topluca izlenir",
   "Satış sürecinde tüketildiği kabul edilerek pazarlama, satış ve dağıtım giderine kaydedilir",
   "Finansman sağlama işlevinden doğduğu kabul edilerek finansman gideri hesabında izlenir"],
  "Çelik levha mamulün esas yapısını oluşturur ve tüketimi belirli siparişe ekonomik biçimde izlenebilir. Bu nedenle direkt ilk madde ve malzemedir.",
  "1 Sıra No.lu MSUGT - 7/A seçeneği, 710 Direkt İlk Madde ve Malzeme Giderleri", "easy")

q("Üretimde çok düşük tutarda kullanılan, mamul başına tüketimi güvenilir olsa bile izleme maliyeti sağlayacağı faydayı aşan bağlantı elemanları nasıl ele alınır?",
  "Endirekt malzeme olarak genel üretim giderlerine alınır",
  ["Mamulün bünyesine girdiği için tutarına bakılmaksızın her koşulda direkt malzeme kabul edilir",
   "Üretimde kullanıldığı hâlde satış faaliyetine ait olduğu varsayılarak pazarlama giderine kaydedilir",
   "Tüketim anında ortaklara dağıtım niteliğinde kabul edilerek doğrudan özkaynaklardan düşülür",
   "İzlenmesi güç olduğu için hiçbir maliyet veya gider hesabına kaydedilmeden stoktan çıkarılır"],
  "Direktlik yalnız fiziksel ilişkiye değil, ekonomik biçimde izlenebilirliğe de bağlıdır. Önemsiz bağlantı elemanları endirekt malzeme olarak genel üretim giderlerinde izlenir.",
  "TMS 2 par. 12 - değişken genel üretim giderleri; 1 Sıra No.lu MSUGT - 730 hesabı")

fiyat, nakliye, iadesiz_vergi, iskonto = 320_000, 18_000, 12_000, 20_000
satinalma_maliyeti = fiyat + nakliye + iadesiz_vergi - iskonto
assert satinalma_maliyeti == 330_000
q(f"Üretimde kullanılacak ana malzemenin liste fiyatı {tr(fiyat)} TL, taşıma gideri {tr(nakliye)} TL, iade alınamayan vergisi {tr(iadesiz_vergi)} TL ve ticari iskontosu {tr(iskonto)} TL'dir. TMS 2'ye göre satın alma maliyeti kaç TL'dir?",
  f"{tr(satinalma_maliyeti)} TL",
  [f"{tr(fiyat+nakliye+iadesiz_vergi+iskonto)} TL",
   f"{tr(fiyat+nakliye-iskonto)} TL",
   f"{tr(fiyat+iadesiz_vergi-iskonto)} TL",
   f"{tr(fiyat-iskonto)} TL"],
  f"Satın alma maliyeti; fiyat + taşıma + iade alınamayan vergi − ticari iskonto olarak hesaplanır: {tr(fiyat)} + {tr(nakliye)} + {tr(iadesiz_vergi)} − {tr(iskonto)} = {tr(satinalma_maliyeti)} TL.",
  "TMS 2 par. 10-11 - satın alma maliyetleri", "hard")

q("Üretimde kullanılacak hammaddenin alımında ödenen ve daha sonra vergi idaresinden indirilebilen vergi, malzeme maliyeti bakımından nasıl ele alınır?",
  "Satın alma maliyetine dâhil edilmez",
  ["İade veya indirim olanağı bulunsa da hammaddenin satın alma maliyetine mutlaka eklenir",
   "Üretim miktarına göre mamullere dağıtılacak sabit genel üretim gideri olarak kabul edilir",
   "Hammadde tüketilinceye kadar finansman gideri olarak aktifleştirilip sonradan maliyete eklenir",
   "Vergi niteliği nedeniyle doğrudan işçilik giderine aktarılır ve çalışma saatlerine göre yüklenir"],
  "TMS 2'ye göre işletmenin daha sonra vergi idaresinden iade veya indirim yoluyla geri alabileceği vergiler stokların satın alma maliyetine girmez.",
  "TMS 2 par. 11 - iade alınabilecek vergiler")

q("Normal kredi koşullarını aşan vadeli hammadde alımında peşin fiyat ile ödenecek toplam tutar arasındaki finansman bileşeni nasıl muhasebeleştirilir?",
  "Finansman süresi boyunca faiz gideri olarak",
  ["Hammaddenin satın alma maliyetine koşulsuz eklenip üretilecek tüm mamullere doğrudan yüklenerek",
   "Satın alma tarihinde değişken genel üretim gideri kabul edilip fiilî üretime dağıtılarak",
   "Hammadde kullanılmasa bile direkt işçilik giderine eklenip çalışma saatlerine göre paylaştırılarak",
   "Peşin fiyatla birlikte 710 hesabında izlenip mamul satışına kadar stokta aktifleştirilerek"],
  "Anlaşma etkin bir finansman bileşeni içeriyorsa peşin fiyatla vadeli tutar arasındaki fark stok maliyeti değil, finansman sağlanan dönem boyunca faiz gideridir.",
  "TMS 2 par. 18 - vadeli alımlardaki finansman bileşeni", "hard")

q("TMS 2'ye göre hammaddenin satın alma maliyetine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Edinimle doğrudan ilişkili taşıma gideri maliyete girer\n\nII. Ticari iskontolar satın alma maliyetinden indirilir\n\nIII. Sonradan iade alınabilecek vergiler satın alma maliyetine eklenir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Taşıma gideri edinimle doğrudan ilişkili olduğundan maliyete girer; ticari iskonto maliyetten düşülür. İade alınabilecek vergiler maliyet unsuru olmadığından üçüncü ifade yanlıştır.",
  "TMS 2 par. 11 - satın alma maliyetinin unsurları", "hard")

q("Üretim emrinde belirtilen ana malzemenin depodan alınarak belirli siparişe verilmesi 7/A seçeneğinde hangi gider hesabında izlenir?",
  "710 Direkt İlk Madde ve Malzeme Giderleri",
  ["720 Direkt İşçilik Giderleri hesabında işçilik maliyetinin bir parçası olarak izlenmesi gerekir",
   "730 Genel Üretim Giderleri hesabında tüm siparişler için ortak maliyet olarak toplanması gerekir",
   "760 Pazarlama Satış ve Dağıtım Giderleri hesabında satış faaliyetine bağlı olarak izlenmelidir",
   "770 Genel Yönetim Giderleri hesabında işletmenin bütünüyle ilgili gider olarak izlenmelidir"],
  "Belirli siparişe verilen ve mamulle doğrudan ilişkilendirilen ana malzeme tüketimi, 7/A seçeneğinde 710 Direkt İlk Madde ve Malzeme Giderleri hesabında izlenir.",
  "1 Sıra No.lu MSUGT - 7/A seçeneği, 710 hesabı", "easy")

q("Bir sipariş için depodan alınan ancak üretimde kullanılmadan depoya iade edilen ana malzeme, sipariş maliyeti açısından nasıl değerlendirilir?",
  "Siparişe yüklenen direkt malzeme maliyetinden düşülür",
  ["Fiziksel olarak depoya dönse bile sipariş maliyetinde bırakılarak mamul maliyetine dâhil edilir",
   "İade edilen tutar direkt işçilik giderine çevrilerek aynı siparişin çalışma süresine dağıtılır",
   "İade, satış işlemi kabul edilerek pazarlama gelirleriyle netleştirilip üretimden bağımsız izlenir",
   "Malzeme daha önce çıkış gördüğü için stok ve maliyet hesaplarında hiçbir düzeltme yapılmaz"],
  "Kullanılmadan depoya dönen malzeme sipariş tarafından tüketilmemiştir. Bu nedenle stok yeniden artırılır ve siparişe yüklenen direkt malzeme maliyeti azaltılır.",
  "1 Sıra No.lu MSUGT - 150 İlk Madde ve Malzeme ile 710 hesabının işleyişi")

donem_basi, alim, donem_sonu = 70_000, 410_000, 85_000
tuketim = donem_basi + alim - donem_sonu
assert tuketim == 395_000
q(f"Bir işletmede dönem başı ana malzeme stoku {tr(donem_basi)} TL, dönem içi net alışlar {tr(alim)} TL ve dönem sonu ana malzeme stoku {tr(donem_sonu)} TL'dir. Tamamı üretimde kullanılmışsa dönemin direkt malzeme tüketimi kaç TL'dir?",
  f"{tr(tuketim)} TL",
  [f"{tr(donem_basi+alim+donem_sonu)} TL",
   f"{tr(alim-donem_basi+donem_sonu)} TL",
   f"{tr(alim-donem_sonu)} TL",
   f"{tr(alim+donem_sonu)} TL"],
  f"Malzeme tüketimi = Dönem başı stok + Net alışlar − Dönem sonu stok = {tr(donem_basi)} + {tr(alim)} − {tr(donem_sonu)} = {tr(tuketim)} TL'dir.",
  "1 Sıra No.lu MSUGT - 150 ve 710 hesapları; TMS 2 par. 34", "hard")

aluminyum_adet, aluminyum_birim = 2_400, 75
iadeli_adet = 160
net_miktar = aluminyum_adet - iadeli_adet
net_maliyet = net_miktar * aluminyum_birim
assert net_maliyet == 168_000
q(f"Bir üretim emrine birim maliyeti {tr(aluminyum_birim)} TL olan {tr(aluminyum_adet)} kg ana malzeme verilmiş, kullanılmayan {tr(iadeli_adet)} kg depoya iade edilmiştir. Üretim emrine yüklenecek net direkt malzeme maliyeti kaç TL'dir?",
  f"{tr(net_maliyet)} TL",
  [f"{tr(aluminyum_adet*aluminyum_birim)} TL",
   f"{tr(iadeli_adet*aluminyum_birim)} TL",
   f"{tr((aluminyum_adet+iadeli_adet)*aluminyum_birim)} TL",
   f"{tr((aluminyum_adet-2*iadeli_adet)*aluminyum_birim)} TL"],
  f"Net tüketim {tr(aluminyum_adet)} − {tr(iadeli_adet)} = {tr(net_miktar)} kg; net direkt malzeme maliyeti {tr(net_miktar)} × {tr(aluminyum_birim)} = {tr(net_maliyet)} TL'dir.",
  "1 Sıra No.lu MSUGT - 150 ve 710 hesaplarının işleyişi")

m1, m2, endirekt = 96_000, 54_000, 8_000
direkt_toplam = m1 + m2
assert direkt_toplam == 150_000
q(f"Bir mamul partisinde doğrudan izlenebilen A malzemesi {tr(m1)} TL, B malzemesi {tr(m2)} TL ve mamul başına izlenmesi ekonomik olmayan yardımcı malzeme {tr(endirekt)} TL tüketilmiştir. Partinin direkt ilk madde ve malzeme maliyeti kaç TL'dir?",
  f"{tr(direkt_toplam)} TL",
  [f"{tr(m1+m2+endirekt)} TL",
   f"{tr(m1+endirekt)} TL",
   f"{tr(m2+endirekt)} TL",
   f"{tr(m1)} TL"],
  f"Direkt maliyet yalnız doğrudan izlenen A ve B malzemelerini kapsar: {tr(m1)} + {tr(m2)} = {tr(direkt_toplam)} TL. {tr(endirekt)} TL yardımcı malzeme genel üretim gideridir.",
  "TMS 2 par. 12 - direkt maliyet ve değişken genel üretim gideri ayrımı")

q("Ana malzemenin fabrikaya getirilmesi için katlanılan ve edinimle doğrudan ilişkilendirilen yükleme-boşaltma gideri nasıl ele alınır?",
  "Malzemenin satın alma maliyetine eklenir",
  ["Üretim hacminden bağımsız sabit genel üretim gideri kabul edilerek normal kapasiteye dağıtılır",
   "Malzeme maliyetinden tamamen ayrılarak satış faaliyetine ait pazarlama gideri olarak kaydedilir",
   "Finansman biçiminden doğduğu varsayılarak her koşulda faiz gideri olarak dönem sonucuna aktarılır",
   "Genel yönetim faaliyetiyle ilişkilendirilerek mamul maliyetinin dışında ve doğrudan gider yazılır"],
  "Mamul, malzeme veya hizmetlerin edinimiyle doğrudan ilişkilendirilebilen yükleme-boşaltma giderleri satın alma maliyetinin unsurudur.",
  "TMS 2 par. 11 - doğrudan ilişkilendirilebilen edinim maliyetleri")

q("Aşağıdaki malzeme tüketimlerinden hangileri direkt ilk madde ve malzeme olarak sınıflandırılır?\n\nI. Ürün reçetesinde yer alan ve her mamule miktar olarak izlenen ana bileşen\n\nII. Özel siparişe özgü, yalnız o sipariş için kullanılan değerli kaplama\n\nIII. Üretimde kullanılan ve her mamule ekonomik biçimde izlenebilen yardımcı parça",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Üç malzeme de mamulle doğrudan ilişkilendirilebilmekte ve ekonomik biçimde izlenebilmektedir. Malzemenin 'yardımcı' diye adlandırılması tek başına endirekt olmasını gerektirmez; izlenebilirlik belirleyicidir.",
  "TMS 2 par. 10 ve 12; 1 Sıra No.lu MSUGT - 710 hesabı", "hard")

q("Üretim hattındaki makinelerin temizliğinde kullanılan ve tek tek mamullere ekonomik biçimde izlenemeyen temizlik malzemesi hangi hesap grubuna alınır?",
  "Genel üretim giderleri içindeki endirekt malzeme",
  ["Mamulün fiziksel yapısına girmediği hâlde direkt ilk madde ve malzeme gideri olarak ürünlere yüklenir",
   "Fabrika içinde kullanıldığı için doğrudan genel yönetim gideri sayılarak üretim maliyetinden çıkarılır",
   "Üretimle ilgisi bulunmadığı kabul edilerek pazarlama, satış ve dağıtım giderine aktarılır",
   "Herhangi bir maliyet nesnesine yüklenmeden finansman gideri olarak dönem sonunda kapatılır"],
  "Üretim sürecine hizmet eden fakat mamulle doğrudan ve ekonomik biçimde ilişkilendirilemeyen temizlik malzemesi endirekt malzemedir ve genel üretim giderlerinde izlenir.",
  "TMS 2 par. 12 - değişken genel üretim giderleri; 1 Sıra No.lu MSUGT - 730 hesabı")

q("Bir malzemenin mamulün fiziksel bünyesine girmesi, direkt malzeme sayılması için tek başına neden yeterli değildir?",
  "Mamul bazında ekonomik biçimde izlenebilmesi de gerekir",
  ["Malzemenin mutlaka işletme içinde üretilmiş olması ve dışarıdan hiçbir şekilde satın alınmaması gerekir",
   "Malzemenin yalnız sabit maliyet niteliği taşıması ve üretim miktarından kesinlikle etkilenmemesi gerekir",
   "Malzemenin mamul satıldıktan sonra tüketilmesi ve satış faaliyetiyle doğrudan ilişkilendirilmesi gerekir",
   "Malzemenin ödeme vadesinin üretim tarihinden önce sona ermiş ve bedelinin nakden ödenmiş olması gerekir"],
  "Direktlik, fiziksel ilişki yanında maliyetin belirli mamule güvenilir ve ekonomik biçimde izlenebilmesini gerektirir. İzleme ekonomik değilse tüketim endirekt malzeme sayılır.",
  "TMS 2 par. 12 - doğrudan ve dolaylı üretim maliyetleri")

toplam_malzeme, endirekt_malzeme, fire_fazlasi = 285_000, 15_000, 10_000
direkt_tuketim = toplam_malzeme - endirekt_malzeme - fire_fazlasi
assert direkt_tuketim == 260_000
q(f"Üretime verilen toplam malzeme {tr(toplam_malzeme)} TL'dir. Bunun {tr(endirekt_malzeme)} TL'si endirekt malzeme, {tr(fire_fazlasi)} TL'si normalin üstündeki kayıptır. Kalan tutar mamullere doğrudan izlenebildiğine göre direkt malzeme maliyeti kaç TL'dir?",
  f"{tr(direkt_tuketim)} TL",
  [f"{tr(toplam_malzeme-endirekt_malzeme)} TL",
   f"{tr(toplam_malzeme-fire_fazlasi)} TL",
   f"{tr(toplam_malzeme)} TL",
   f"{tr(endirekt_malzeme+fire_fazlasi)} TL"],
  f"Direkt malzeme = Toplam verilen − Endirekt malzeme − Normalin üstündeki kayıp = {tr(toplam_malzeme)} − {tr(endirekt_malzeme)} − {tr(fire_fazlasi)} = {tr(direkt_tuketim)} TL'dir.",
  "TMS 2 par. 12 ve 16(a) - endirekt malzeme ve normal üstü kayıplar", "hard")

q("Üretime verilen ana malzemenin mamule dönüşmeden önce yarı mamul üzerinde işlem görmesi maliyet akışını nasıl etkiler?",
  "Tüketim önce yarı mamul maliyetine aktarılır",
  ["Ana malzeme üretime verildiği anda mamul satılmış sayılarak doğrudan satışların maliyetine aktarılır",
   "Malzeme yarı mamulde bulunduğu sürece genel yönetim gideri sayılır ve stoklarda hiçbir zaman izlenmez",
   "Üretim tamamlanıncaya kadar malzeme maliyeti finansman gideri olarak dönem sonucunda gösterilir",
   "Yarı mamul aşaması bulunduğu için malzeme tüketimi direkt niteliğini kaybedip genel üretim gideri olur"],
  "Üretime verilen direkt malzeme, üretim tamamlanana kadar yarı mamul maliyetinin parçasıdır; tamamlanınca mamul stokuna, satışta satışların maliyetine aktarılır.",
  "TMS 2 par. 1, 10 ve 34 - stok maliyetinin aktifleştirilmesi ve giderleştirilmesi")

liste, iskonto2, tasima2 = 250_000, 25_000, 9_000
net_edinim = liste - iskonto2 + tasima2
assert net_edinim == 234_000
q(f"Ana malzemenin liste fiyatı {tr(liste)} TL, ticari iskontosu {tr(iskonto2)} TL ve doğrudan taşıma gideri {tr(tasima2)} TL'dir. Başka maliyet yoksa stoklara alınacak net edinim maliyeti kaç TL'dir?",
  f"{tr(net_edinim)} TL",
  [f"{tr(liste+iskonto2+tasima2)} TL",
   f"{tr(liste-iskonto2-tasima2)} TL",
   f"{tr(liste+tasima2)} TL",
   f"{tr(liste-iskonto2)} TL"],
  f"Ticari iskonto maliyetten düşülür, doğrudan taşıma maliyete eklenir: {tr(liste)} − {tr(iskonto2)} + {tr(tasima2)} = {tr(net_edinim)} TL.",
  "TMS 2 par. 11 - ticari iskonto ve taşıma maliyeti")

q("Hammaddenin satın alma bedelinin borçlanılarak ödenmesi, hammaddeyi direkt veya endirekt sınıflandırma bakımından nasıl etkiler?",
  "Ödeme biçimi direktlik sınıflandırmasını değiştirmez",
  ["Borçlanılarak alınan tüm hammaddeler mamulle ilişkisine bakılmaksızın finansman gideri kabul edilir",
   "Nakit alınmayan hammaddeler stok olarak kaydedilemez ve doğrudan dönem giderine aktarılmak zorundadır",
   "Vadeli alınan her ana malzeme, mamule izlenebilse bile genel üretim gideri olarak sınıflandırılır",
   "Ödeme yapılıncaya kadar hammadde maliyeti oluşmadığından üretime verilen tutar sıfır kabul edilir"],
  "Direktlik, maliyetin mamulle ekonomik biçimde izlenmesine bağlıdır; nakit veya kredili edinim bu niteliği değiştirmez. Yalnız ayrı finansman bileşeni TMS 2 paragraf 18'e göre faiz gideridir.",
  "TMS 2 par. 12 ve 18 - doğrudan maliyet ve finansman bileşeni")

ilk_miktar, ilk_birim, ek_miktar, ek_birim = 1_200, 40, 800, 55
toplam_tutar = ilk_miktar * ilk_birim + ek_miktar * ek_birim
toplam_miktar = ilk_miktar + ek_miktar
ortalama = toplam_tutar / toplam_miktar
assert toplam_tutar == 92_000 and ortalama == 46
q(f"Aynı üretim emrinde {tr(ilk_miktar)} kg ana malzeme {tr(ilk_birim)} TL/kg ve {tr(ek_miktar)} kg ana malzeme {tr(ek_birim)} TL/kg maliyetle tüketilmiştir. Üretim emrinin toplam direkt malzeme maliyeti kaç TL'dir?",
  f"{tr(toplam_tutar)} TL",
  [f"{tr(toplam_miktar*ilk_birim)} TL",
   f"{tr(toplam_miktar*ek_birim)} TL",
   f"{tr((ilk_miktar-ek_miktar)*ek_birim)} TL",
   f"{tr(int(ortalama))} TL"],
  f"Toplam direkt malzeme maliyeti iki tüketimin tutarlarının toplamıdır: {tr(ilk_miktar)} × {tr(ilk_birim)} + {tr(ek_miktar)} × {tr(ek_birim)} = {tr(toplam_tutar)} TL.",
  "TMS 2 par. 10 ve 12 - stokların dönüştürülmesinde doğrudan maliyetler")


# ── B. Direkt işçilik (20) ────────────────────────────────────────────────
q("Bir montaj işçisinin çalışma süresi barkodlu iş emriyle belirli mamul partilerine güvenilir biçimde aktarılabiliyorsa ücret maliyeti nasıl sınıflandırılır?",
  "Direkt işçilik gideri",
  ["Üretim ortamında çalışsa bile tüm mamuller için ortak sabit genel üretim gideri olarak sınıflandırılır",
   "İş emriyle izlenebilmesine rağmen genel yönetim personeli maliyeti olarak dönem sonucuna aktarılır",
   "Ücret ödemesi nakit çıkışı doğurduğu için finansman gideri sayılarak mamul maliyetinden çıkarılır",
   "Montaj tamamlanmadan önce oluştuğu için stok maliyetiyle hiçbir ilişki kurulmadan gider yazılır"],
  "Mamul üzerinde çalışan işçinin süresi belirli partiye ekonomik biçimde izlenebildiğinden ücret maliyeti direkt işçiliktir ve dönüştürme maliyetine girer.",
  "TMS 2 par. 12 - üretimle doğrudan ilişkili işçilik; 1 Sıra No.lu MSUGT - 720 hesabı", "easy")

q("İşçilik maliyetleriyle ilgili aşağıdaki çalışanlardan hangileri direkt işçilik kapsamında değerlendirilir?\n\nI. Süresi belirli siparişe izlenen kaynakçı\n\nII. Üretim vardiyasını yöneten ve birden çok mamule hizmet veren ustabaşı\n\nIII. Tüm makinelerin bakımını yapan teknisyen",
  "Yalnız I",
  ["I, II ve III", "I ve II", "II ve III", "Yalnız III"],
  "Kaynakçının süresi belirli siparişe izlenebildiği için direkt işçiliktir. Birden çok mamule ortak hizmet veren ustabaşı ve bakım teknisyeni endirekt işçilik olarak genel üretim giderlerine girer.",
  "TMS 2 par. 12 - direkt işçilik ile endirekt işçilik ayrımı")

brut, isveren_payi, diger_fayda = 180_000, 39_600, 14_400
direkt_iscilik = brut + isveren_payi + diger_fayda
assert direkt_iscilik == 234_000
q(f"Tamamı mamuller üzerinde doğrudan çalışan işçilere ait brüt ücret {tr(brut)} TL, işveren payları {tr(isveren_payi)} TL ve üretime ilişkin diğer çalışan faydaları {tr(diger_fayda)} TL'dir. Tamamı doğrudan izlenebiliyorsa direkt işçilik maliyeti kaç TL'dir?",
  f"{tr(direkt_iscilik)} TL",
  [f"{tr(brut+isveren_payi)} TL",
   f"{tr(brut+diger_fayda)} TL",
   f"{tr(brut)} TL",
   f"{tr(isveren_payi+diger_fayda)} TL"],
  f"Doğrudan çalışanlara ilişkin ücret ve işverenin katlandığı ilgili faydalar birlikte işçilik maliyetini oluşturur: {tr(brut)} + {tr(isveren_payi)} + {tr(diger_fayda)} = {tr(direkt_iscilik)} TL.",
  "TMS 2 par. 12 - üretimle doğrudan ilişkili işçilik maliyetleri")

saat, saat_ucreti = 2_600, 85
parti_iscilik = saat * saat_ucreti
assert parti_iscilik == 221_000
q(f"Bir mamul partisinde doğrudan çalışan işçiler {tr(saat)} saat çalışmış ve kapsamlı saatlik işçilik maliyeti {tr(saat_ucreti)} TL olarak belirlenmiştir. Partiye yüklenecek direkt işçilik maliyeti kaç TL'dir?",
  f"{tr(parti_iscilik)} TL",
  [f"{tr((saat+400)*saat_ucreti)} TL",
   f"{tr(saat*(saat_ucreti-10))} TL",
   f"{tr(saat+saat_ucreti)} TL",
   f"{tr(saat_ucreti)} TL"],
  f"Direkt işçilik maliyeti = Doğrudan çalışma saati × Saatlik işçilik maliyeti = {tr(saat)} × {tr(saat_ucreti)} = {tr(parti_iscilik)} TL'dir.",
  "TMS 2 par. 12 - direkt işçilik giderleri")

x_saat, y_saat, oran = 900, 1_100, 120
x_maliyet, y_maliyet = x_saat * oran, y_saat * oran
assert x_maliyet == 108_000 and y_maliyet == 132_000
q(f"Aynı üretim bölümünde X mamulü {tr(x_saat)}, Y mamulü {tr(y_saat)} direkt işçilik saati kullanmıştır. Saatlik kapsamlı işçilik maliyeti {tr(oran)} TL ise X ve Y'ye yüklenecek direkt işçilik maliyetleri sırasıyla kaç TL'dir?",
  f"{tr(x_maliyet)} TL ve {tr(y_maliyet)} TL",
  [f"{tr(y_maliyet)} TL ve {tr(x_maliyet)} TL",
   f"{tr((x_saat+y_saat)*oran)} TL ve {tr(y_maliyet)} TL",
   f"{tr(x_maliyet)} TL ve {tr((x_saat+y_saat)*oran)} TL",
   f"{tr(x_saat+y_saat)} TL ve {tr(oran)} TL"],
  f"Her mamul kendi doğrudan saatleriyle yüklenir: X = {tr(x_saat)} × {tr(oran)} = {tr(x_maliyet)} TL; Y = {tr(y_saat)} × {tr(oran)} = {tr(y_maliyet)} TL.",
  "TMS 2 par. 12 - üretimle doğrudan ilişkili işçilik")

q("Üretim hattında planlı kısa ayarlamalar nedeniyle ortaya çıkan ve belirli mamule ekonomik biçimde izlenemeyen normal bekleme süresi ücretleri nasıl sınıflandırılır?",
  "Endirekt işçilik olarak genel üretim giderlerine",
  ["Hangi mamulün üretildiğine bakılmaksızın her durumda direkt işçilik giderine doğrudan yüklenerek",
   "Üretimle bağlantılı olduğu hâlde pazarlama, satış ve dağıtım giderine aktarılarak",
   "Çalışana ödeme yapıldığı için finansman gideri olarak dönem sonucunda gösterilerek",
   "Hiçbir maliyet hesabına alınmadan yalnızca nazım hesaplarda bilgi amacıyla izlenerek"],
  "Normal ve üretim sürecine bağlı bekleme süreleri belirli mamule doğrudan izlenemiyorsa endirekt işçilik niteliğindedir ve genel üretim giderlerine alınır.",
  "TMS 2 par. 12 - dolaylı üretim maliyetleri; 1 Sıra No.lu MSUGT - 730 hesabı")

q("Önlenebilir uzun süreli makine arızasının yol açtığı normalin üstündeki boş işçilik maliyeti TMS 2 bakımından nasıl ele alınır?",
  "Oluştuğu dönemde giderleştirilir",
  ["Normal kapasiteye göre mamullere dağıtılan sabit genel üretim giderine koşulsuz olarak eklenir",
   "Gelecek dönem üretimine ait olduğu varsayılarak diğer dönen varlıklar içinde aktifleştirilir",
   "Tamamı direkt işçilik kabul edilerek arıza sırasında üretilmeyen mamullerin maliyetine yüklenir",
   "Hammadde maliyetinin bir unsuru sayılarak üretime verilen malzeme miktarına göre dağıtılır"],
  "Normalin üstünde gerçekleşen işçilik maliyetleri stok maliyetine alınmaz; oluştukları dönemde gider olarak finansal tablolara yansıtılır.",
  "TMS 2 par. 16(a) - normalin üstündeki işçilik maliyetleri", "hard")

q("Yalnızca özel bir müşteri siparişinin olağan çalışma saatleri dışında tamamlanması için katlanılan fazla çalışma primi, açıkça o siparişe izlenebiliyorsa nasıl ele alınır?",
  "Özel siparişin direkt işçilik maliyetine yüklenir",
  ["Siparişle açık ilişkisine rağmen bütün mamuller için ortak genel üretim gideri olarak dağıtılır",
   "Üretimle ilgili olmadığı kabul edilerek pazarlama, satış ve dağıtım giderine aktarılır",
   "Çalışma saatleri dışında doğduğu için her durumda normalin üstünde kayıp sayılıp giderleştirilir",
   "Ücret niteliğinde olduğu hâlde direkt ilk madde ve malzeme maliyetine eklenerek izlenir"],
  "Fazla çalışma yalnız belirli özel sipariş nedeniyle yapılmış ve maliyet siparişe güvenilir biçimde izlenebilmişse prim o siparişin direkt işçilik maliyetidir.",
  "TMS 2 par. 12 - üretimle doğrudan ilişkili işçilik; 1 Sıra No.lu MSUGT - 720 hesabı", "hard")

q("İşçilik maliyetlerinin sınıflandırılmasına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Mamule fiilen harcanan ve izlenen çalışma süresi direkt işçiliktir\n\nII. Birden çok üretim bölümüne hizmet veren bakım personeli endirekt işçiliktir\n\nIII. Fabrika ustabaşının ücreti her durumda direkt ilk madde gideridir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Mamule izlenen fiilî çalışma direkt işçiliktir; ortak bakım hizmeti endirekt işçiliktir. Ustabaşı ücreti malzeme değil, genel üretim giderleri içindeki endirekt işçiliktir.",
  "TMS 2 par. 12 - direkt ve endirekt işçilik ayrımı")

q("Üretim işçilerinin belirli mamullere doğrudan izlenemeyen ücretli yıllık izin karşılıkları maliyet unsuru bakımından nasıl değerlendirilir?",
  "Endirekt işçilik niteliğinde genel üretim gideridir",
  ["İzin sırasında üretim yapılmadığı için her durumda direkt ilk madde ve malzeme giderine aktarılır",
   "Çalışanlara ilişkin olmasına rağmen üretimden bağımsız pazarlama gideri olarak muhasebeleştirilir",
   "Her bir mamule doğrudan izlenmiş kabul edilerek fiilî çalışma saatlerine bakılmadan direkt yüklenir",
   "Gelecekte ödeneceği için stok ve giderlerle ilişkilendirilmeden yalnızca finansman gideri sayılır"],
  "Belirli mamule doğrudan izlenemeyen üretim işçisi izin maliyetleri endirekt işçilik olarak genel üretim giderlerinde toplanır.",
  "TMS 2 par. 12 - dolaylı üretim maliyetleri; 1 Sıra No.lu MSUGT - 730 hesabı")

q("İşverenin üretim işçisi için katlandığı zorunlu payların direkt veya endirekt sınıflandırılması neye bağlıdır?",
  "İlgili işçinin emeğinin mamule izlenebilirliğine",
  ["Ödemenin ayın ilk veya son haftasında yapılmasına ve işletmenin nakit durumuna göre belirlenmesine",
   "İşveren payının tutarının brüt ücretten büyük ya da küçük olmasına göre sınıflandırılmasına",
   "İşçinin yalnız kıdemine bakılarak tüm deneyimli çalışanlar için direkt kabul edilmesine",
   "Yasal yükümlülük niteliği taşıdığı için üretimle ilişkisine bakılmadan finansman gideri sayılmasına"],
  "Ücrete bağlı işveren payları, ilgili emeğin sınıflandırmasını izler. İşçi mamule doğrudan izlenebiliyorsa paylar direkt; ortak üretim hizmeti veriyorsa endirekt işçilik maliyetidir.",
  "TMS 2 par. 12 - işçilik maliyetlerinin doğrudan/dolaylı niteliği")

toplam_ucret, endirekt_ucret, anormal_ucret = 360_000, 48_000, 12_000
net_direkt_ucret = toplam_ucret - endirekt_ucret - anormal_ucret
assert net_direkt_ucret == 300_000
q(f"Üretim bölümündeki toplam işçilik maliyeti {tr(toplam_ucret)} TL'dir. Bunun {tr(endirekt_ucret)} TL'si ustabaşı ve bakım personeline, {tr(anormal_ucret)} TL'si normalin üstündeki duruşa aittir. Kalan tutar mamullere doğrudan izleniyorsa direkt işçilik kaç TL'dir?",
  f"{tr(net_direkt_ucret)} TL",
  [f"{tr(toplam_ucret-endirekt_ucret)} TL",
   f"{tr(toplam_ucret-anormal_ucret)} TL",
   f"{tr(toplam_ucret)} TL",
   f"{tr(endirekt_ucret+anormal_ucret)} TL"],
  f"Direkt işçilik = Toplam işçilik − Endirekt işçilik − Normal üstü duruş = {tr(toplam_ucret)} − {tr(endirekt_ucret)} − {tr(anormal_ucret)} = {tr(net_direkt_ucret)} TL'dir.",
  "TMS 2 par. 12 ve 16(a) - işçilik maliyetlerinin ayrıştırılması", "hard")

q("Üretim sürecindeki tüm mamullere ortak hizmet veren kalite kontrol personelinin ücreti hangi maliyet unsurudur?",
  "Endirekt işçilik kapsamında genel üretim gideri",
  ["Kontrol edilen mamuller üretimde olduğu için her mamule doğrudan yüklenen direkt ilk madde maliyetidir",
   "Kalite satışları etkilediği için üretimle ilişkisi kesilerek pazarlama gideri olarak kaydedilmelidir",
   "Personel yönetim faaliyeti yürüttüğünden fabrika dışında genel yönetim gideri kabul edilmelidir",
   "Ücret borcu doğurduğu için mamul maliyetine girmeyen bir finansman gideri olarak izlenmelidir"],
  "Birden çok mamule ortak hizmet veren kalite kontrol emeği, belirli mamule ekonomik biçimde doğrudan izlenemediği için endirekt işçiliktir ve genel üretim giderlerine alınır.",
  "TMS 2 par. 12 - dolaylı üretim maliyetleri; 1 Sıra No.lu MSUGT - 730 hesabı")

aylik_maliyet, uretken_saat = 264_000, 3_300
saatlik = aylik_maliyet / uretken_saat
assert saatlik == 80
q(f"Doğrudan üretim işçilerinin aylık toplam maliyeti {tr(aylik_maliyet)} TL, mamullere izlenen üretken çalışma süresi {tr(uretken_saat)} saattir. Üretken saat başına direkt işçilik maliyeti kaç TL'dir?",
  f"{tr(saatlik)} TL/saat",
  [f"{tr(aylik_maliyet/(uretken_saat-300))} TL/saat",
   f"{tr(aylik_maliyet/(uretken_saat+300))} TL/saat",
   f"{tr(uretken_saat/aylik_maliyet)} TL/saat",
   f"{tr(aylik_maliyet-uretken_saat)} TL/saat"],
  f"Üretken saat başına maliyet = {tr(aylik_maliyet)} / {tr(uretken_saat)} = {tr(saatlik)} TL/saat olarak hesaplanır.",
  "TMS 2 par. 12 - direkt işçilik maliyetinin mamullere yüklenmesi")

q("Emek yoğun bir üretim bölümünün genel üretim giderlerini mamullere yüklerken neden direkt işçilik saati uygun bir dağıtım ölçüsü olabilir?",
  "Kaynak tüketimiyle neden-sonuç ilişkisi kurduğu için",
  ["Direkt işçilik saati her işletmede mevzuatla zorunlu tutulan tek dağıtım anahtarı olduğu için",
   "İşçilik saati kullanıldığında tüm genel üretim giderleri otomatik olarak direkt maliyete dönüştüğü için",
   "Bu ölçü sabit genel üretim giderlerini stok maliyetinden tamamen çıkarmayı sağladığı için",
   "İşçilik saati üretim miktarından bağımsız olduğundan maliyetleri her dönemde aynı tuttuğu için"],
  "Dağıtım ölçüsü, maliyetlerin oluşumuyla mümkün olduğunca neden-sonuç ilişkisi kurmalıdır. Emek yoğun bölümde işçilik saatleri kaynak kullanımını makul biçimde temsil edebilir.",
  "TMS 2 par. 12 - genel üretim giderlerinin sistematik dağıtımı")

q("Bir üretim işçisine yalnız belirli siparişin teknik güçlüğü nedeniyle ödenen ve sipariş bazında belgelenen prim nasıl sınıflandırılır?",
  "İlgili siparişin direkt işçilik maliyeti",
  ["Tüm fabrika üretimine ortak sabit genel üretim gideri olarak normal kapasiteye göre dağıtılması gerekir",
   "Üretimle doğrudan ilişkisine rağmen pazarlama, satış ve dağıtım gideri olarak dönem sonucuna aktarılır",
   "Prim niteliği taşıdığı için hiçbir durumda stok maliyetine alınmadan finansman gideri kabul edilir",
   "İşçilikle ilgili olduğu hâlde direkt ilk madde ve malzeme gideri hesabına eklenerek izlenir"],
  "Prim yalnız belirli siparişin üretimi nedeniyle doğmuş ve o siparişe doğrudan izlenebilmiştir. Bu nedenle siparişin direkt işçilik maliyetine dâhil edilir.",
  "TMS 2 par. 12 - üretimle doğrudan ilişkili işçilik")

q("Direkt işçilik maliyetlerinin mamule yüklenmesine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Yükleme, mamul için harcanan süreye dayanabilir\n\nII. Saatlik maliyet, işverenin katlandığı ilgili payları da içerebilir\n\nIII. Belirli mamule izlenemeyen ustabaşı ücreti her durumda direkt işçiliktir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Mamul için harcanan süre ve bu süreye ilişkin kapsamlı saatlik maliyet direkt yüklemede kullanılabilir. Belirli mamule izlenemeyen ustabaşı ücreti ise endirekt işçiliktir.",
  "TMS 2 par. 12 - direkt işçilik ve dolaylı üretim maliyetleri")

q("Fabrika güvenlik görevlisinin yalnız üretim tesisine hizmet eden ve mamul bazında izlenemeyen ücreti nasıl ele alınır?",
  "Sabit genel üretim gideri içinde endirekt işçilik",
  ["Mamul üzerinde fiziksel çalışma yapmadığı için üretimden bağımsız genel yönetim gideri kabul edilir",
   "Fabrika içinde bulunduğu için mamullere miktar üzerinden doğrudan yüklenen direkt işçilik sayılır",
   "Güvenlik hizmeti satışları koruduğu için pazarlama, satış ve dağıtım giderine aktarılır",
   "Ücret ödemesi borç doğurduğundan üretim maliyetiyle ilişkisiz finansman gideri olarak izlenir"],
  "Yalnız üretim tesisine hizmet veren güvenlik personeli üretimle ilgili fakat mamule doğrudan izlenemeyen bir işçilik maliyetidir; nispeten sabitse sabit genel üretim giderine girer.",
  "TMS 2 par. 12 - sabit genel üretim giderleri")

q("Üretim bölüm müdürünün birden çok mamul hattını yönettiği ve ücretinin tek bir mamule izlenemediği durumda maliyet sınıflandırması nedir?",
  "Fabrika yönetimine ait genel üretim gideri",
  ["Yönetici unvanı taşıdığı için faaliyet yerine bakılmadan doğrudan genel yönetim gideri kabul edilmelidir",
   "Üretim hattında bulunduğu için ücretinin tamamı tek tek mamullere direkt işçilik olarak yüklenmelidir",
   "Birden çok mamule hizmet ettiği için maliyet üretimden çıkarılıp pazarlama giderine aktarılmalıdır",
   "Mamul maliyetine girmeyen bir finansman gideri olarak faiz giderleriyle birlikte raporlanmalıdır"],
  "Fabrikanın yönetim ve idaresiyle ilgili, üretim miktarından bağımsız ve mamule doğrudan izlenemeyen maliyetler sabit genel üretim giderleri kapsamındadır.",
  "TMS 2 par. 12 - fabrikanın yönetim ve idaresiyle ilgili maliyetler")

direkt_saat, normal_bekleme, anormal_bekleme, ucret = 2_800, 200, 100, 90
direkt_tutar = direkt_saat * ucret
endirekt_tutar = normal_bekleme * ucret
anormal_tutar = anormal_bekleme * ucret
assert (direkt_tutar, endirekt_tutar, anormal_tutar) == (252_000, 18_000, 9_000)
q(f"Saatlik işçilik maliyeti {tr(ucret)} TL'dir. {tr(direkt_saat)} saat mamule doğrudan çalışma, {tr(normal_bekleme)} saat olağan ayar beklemesi ve {tr(anormal_bekleme)} saat önlenebilir arıza beklemesi vardır. Direkt işçilik, genel üretim gideri ve dönem gideri sırasıyla kaç TL'dir?",
  f"{tr(direkt_tutar)} TL, {tr(endirekt_tutar)} TL ve {tr(anormal_tutar)} TL",
  [f"{tr(direkt_tutar+endirekt_tutar)} TL, {tr(anormal_tutar)} TL ve 0 TL",
   f"{tr(direkt_tutar)} TL, {tr(endirekt_tutar+anormal_tutar)} TL ve 0 TL",
   f"{tr(direkt_tutar+endirekt_tutar+anormal_tutar)} TL, 0 TL ve 0 TL",
   f"{tr(direkt_tutar)} TL, {tr(anormal_tutar)} TL ve {tr(endirekt_tutar)} TL"],
  f"Doğrudan süre {tr(direkt_tutar)} TL direkt işçilik; olağan ayar beklemesi {tr(endirekt_tutar)} TL endirekt işçilik; normal üstü arıza beklemesi {tr(anormal_tutar)} TL dönem gideridir.",
  "TMS 2 par. 12 ve 16(a) - direkt, endirekt ve normal üstü işçilik", "hard")

q("Üretim tamamlanıp mamul stokuna alındığında, mamule yüklenmiş direkt işçilik maliyeti bakımından hangi işlem gerçekleşir?",
  "Yarı mamulden mamul maliyetine aktarılır",
  ["Üretim tamamlandığı anda satış yapılmasa bile doğrudan satışların maliyetine aktarılarak giderleştirilir",
   "Mamul stokuna yalnız malzeme aktarılır; direkt işçilik doğrudan genel yönetim gideri yazılır",
   "Direkt işçilik niteliğini kaybederek finansman gideri hesabına aktarılıp dönem sonucuna alınır",
   "Üretim tamamlanınca çalışanlardan tahsil edilecek bir alacak hesabına dönüştürülerek aktifleştirilir"],
  "Direkt işçilik dönüştürme maliyetinin parçasıdır. Üretim sırasında yarı mamulde, tamamlanınca mamul stokunda izlenir; mamul satıldığında giderleşir.",
  "TMS 2 par. 1, 10, 12 ve 34 - dönüştürme maliyetinin akışı")


# ── C. Genel üretim giderleri ve bütünleşik uygulamalar (20) ───────────────
q("Bir üretim işletmesinde mamulle doğrudan ilişkilendirilemeyen fabrika kirası, makine amortismanı ve ustabaşı ücretinin ortak niteliği nedir?",
  "Genel üretim gideri olmaları",
  ["Mamulün bünyesine girdikleri için direkt ilk madde ve malzeme gideri olarak sınıflandırılmaları",
   "Her biri satış faaliyeti için yapıldığından pazarlama, satış ve dağıtım gideri sayılmaları",
   "İşletmenin finansman politikasından doğdukları için finansman gideri olarak raporlanmaları",
   "Üretimle ilişkileri bulunmadığından genel yönetim gideri olarak doğrudan dönem sonucuna alınmaları"],
  "Üretimle ilgili olan fakat belirli mamule doğrudan izlenemeyen kira, amortisman ve ustabaşı ücreti genel üretim giderleridir.",
  "TMS 2 par. 12 - sabit genel üretim giderleri; 1 Sıra No.lu MSUGT - 730 hesabı", "easy")

q("TMS 2'de sabit genel üretim giderine verilen örneklerden hangisi üretim miktarından bağımsız olarak nispeten sabit kalan dolaylı üretim maliyetidir?",
  "Fabrika binası ve üretim teçhizatı amortismanı",
  ["Üretilen her bir mamule doğrudan ve aynı miktarda giren ana hammadde tüketim maliyeti",
   "Mamul üzerinde fiilen çalışılan saatlerle birebir artan direkt üretim işçisi ücret maliyeti",
   "Satılan mamul adedine göre hesaplanan satış temsilcisi primi ve dağıtım maliyeti",
   "İşletme merkezindeki insan kaynakları biriminin tüm işletmeye hizmet veren personel maliyeti"],
  "TMS 2, amortisman ile fabrika binası ve teçhizatının bakım-onarımı gibi üretim miktarından bağımsız nispeten sabit dolaylı maliyetleri sabit genel üretim giderlerine örnek verir.",
  "TMS 2 par. 12 - sabit genel üretim giderleri")

q("Üretim miktarıyla doğru orantılı değişen, mamul başına doğrudan izlenemeyen yağlama malzemesi ve destek işçiliği nasıl sınıflandırılır?",
  "Değişken genel üretim gideri",
  ["Mamul başına izlenemese de üretimle değiştiği için direkt ilk madde ve direkt işçilik olarak sınıflandırılır",
   "Üretim miktarıyla değiştiği hâlde sabit genel üretim gideri sayılarak normal kapasiteye göre dağıtılır",
   "Fabrika içinde tüketildiği için genel yönetim gideri kabul edilerek stok maliyetinden tamamen çıkarılır",
   "Üretimle bağlantılı olmasına rağmen satış gideri sayılarak satılan birimlere doğrudan yüklenir"],
  "Endirekt malzeme ve endirekt işçilik gibi üretimle doğru orantılı değişen dolaylı maliyetler, değişken genel üretim gideridir.",
  "TMS 2 par. 12 - değişken genel üretim giderleri")

q("TMS 2'ye göre dönüştürme maliyetleriyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Üretimle doğrudan ilişkili işçilik maliyetlerini kapsar\n\nII. Sabit genel üretim giderlerinden sistematik dağıtılan tutarı içerir\n\nIII. Değişken genel üretim giderlerinden sistematik dağıtılan tutarı içerir",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Dönüştürme maliyetleri direkt işçilik yanında sabit ve değişken genel üretim giderlerinden sistematik biçimde dağıtılan tutarları içerir. Üç ifade de doğrudur.",
  "TMS 2 par. 12 - dönüştürme maliyetlerinin kapsamı", "hard")

q("Sabit genel üretim giderlerinin mamullere dağıtımında normal kapasitenin kullanılmasının temel amacı nedir?",
  "Düşük üretimde stokların aşırı maliyetlenmesini önlemek",
  ["Sabit genel üretim giderlerinin tamamını üretim düzeyi ne olursa olsun stoklara yüklemeyi sağlamak",
   "Değişken genel üretim giderlerini fiilî kullanım yerine bütçelenmiş satışlara göre dağıtmak",
   "Üretim yapılmayan dönemlerde tüm sabit giderleri gelecek dönem stoklarına ertelemek",
   "Mamul maliyetinden direkt işçilik ve direkt malzemeyi çıkararak yalnız sabit gider bırakmak"],
  "Normal kapasite esası, düşük üretim veya atıl kapasite nedeniyle birim sabit genel gider payının artırılmasını ve stokların aşırı değerlenmesini engeller.",
  "TMS 2 par. 13 - normal kapasite ve sabit genel üretim giderleri")

sabit_yuksek, normal_yuksek, fiili_yuksek = 420_000, 14_000, 21_000
normal_birim_yuksek = sabit_yuksek / normal_yuksek
yuksek_birim = sabit_yuksek / fiili_yuksek
assert (normal_birim_yuksek, yuksek_birim) == (30, 20)
q(f"Bir tesiste sabit genel üretim gideri {tr(sabit_yuksek)} TL, normal kapasite {tr(normal_yuksek)} birimdir. Anormal derecede yüksek üretimle {tr(fiili_yuksek)} birim üretilmiştir. TMS 2 uyarınca toplam dağıtımın fiilî sabit gideri aşmaması için birim başına kaç TL yüklenir?",
  f"{tr(yuksek_birim)} TL/birim",
  [f"{tr(normal_birim_yuksek)} TL/birim",
   f"{tr(sabit_yuksek)} TL/birim",
   f"{tr(fiili_yuksek/normal_yuksek)} TL/birim",
   f"{tr((sabit_yuksek+fiili_yuksek)/normal_yuksek)} TL/birim"],
  f"Anormal yüksek üretimde toplam dağıtım fiilî {tr(sabit_yuksek)} TL'yi aşmamalıdır. Birim pay {tr(sabit_yuksek)} / {tr(fiili_yuksek)} = {tr(yuksek_birim)} TL'ye düşürülür; normal kapasite oranı olan {tr(normal_birim_yuksek)} TL kullanılmaz.",
  "TMS 2 par. 13 - anormal yüksek üretimde sabit genel giderin birim payı", "hard")

dusuk_sabit, dusuk_yuklenen = 540_000, 450_000
dagitilmayan = dusuk_sabit - dusuk_yuklenen
assert dagitilmayan == 90_000
q(f"Orkide Fabrikası düşük talep nedeniyle olağan üretim düzeyinin altında çalışmıştır. Dönemin {tr(dusuk_sabit)} TL sabit dolaylı üretim maliyetinin yalnız {tr(dusuk_yuklenen)} TL'si üretilen birimlere sistematik olarak dağıtılabilmiştir. Kalan tutar nasıl ele alınır?",
  f"{tr(dagitilmayan)} TL dönemde giderleştirilir",
  [f"{tr(dagitilmayan)} TL gelecek dönem stoklarına aktarılarak üretim yapılıncaya kadar bekletilir",
   f"{tr(dusuk_sabit)} TL'nin tamamı fiilî üretime yeniden dağıtılarak mamul maliyetine eklenir",
   f"{tr(dusuk_yuklenen)} TL dönem gideri yapılır, yalnız {tr(dagitilmayan)} TL stoklara yüklenir",
   f"{tr(dagitilmayan)} TL doğrudan maddi duran varlık maliyetine eklenerek amortismana tabi tutulur"],
  f"Dağıtılmayan tutar {tr(dusuk_sabit)} − {tr(dusuk_yuklenen)} = {tr(dagitilmayan)} TL'dir. Düşük üretim veya atıl kapasiteden kaynaklanan bu tutar oluştuğu dönemde giderleştirilir.",
  "TMS 2 par. 13 - dağıtılmayan sabit genel üretim giderleri", "hard")

q("Anormal derecede yüksek üretim gerçekleşen dönemde sabit genel üretim giderinin birim başına dağıtılan tutarı neden düşürülür?",
  "Stokların maliyet değerini aşan tutarla ölçülmemesi için",
  ["Sabit genel üretim giderlerinin tamamını üretimden çıkarıp genel yönetim giderine dönüştürmek için",
   "Değişken genel üretim giderlerini normal kapasite yerine satış miktarına göre dağıtmak için",
   "Yüksek üretimde mamullere hiçbir sabit üretim gideri yüklememek ve tamamını giderleştirmek için",
   "Direkt malzeme ile direkt işçilik toplamını azaltarak brüt kârı yapay biçimde yükseltmek için"],
  "Anormal yüksek üretimde normal oranı aynen kullanmak, dağıtılan toplam sabit gideri gerçekleşen giderin üzerine çıkarabilir. Birim pay düşürülerek stokların maliyetini aşması önlenir.",
  "TMS 2 par. 13 - anormal yüksek üretimde sabit genel gider dağıtımı", "hard")

degisken_birim, fiili_makine = 14, 22_000
degisken_yuklenen = degisken_birim * fiili_makine
assert degisken_yuklenen == 308_000
q(f"Değişken genel üretim gideri makine saati başına {tr(degisken_birim)} TL'dir ve üretim tesisleri fiilen {tr(fiili_makine)} makine saati kullanmıştır. TMS 2'ye göre mamullere dağıtılacak değişken genel üretim gideri kaç TL'dir?",
  f"{tr(degisken_yuklenen)} TL",
  [f"{tr((fiili_makine+3_000)*degisken_birim)} TL",
   f"{tr((fiili_makine-2_000)*degisken_birim)} TL",
   f"{tr(fiili_makine+degisken_birim)} TL",
   f"{tr(degisken_birim)} TL"],
  f"Değişken genel üretim giderleri tesislerin gerçek kullanımına göre dağıtılır: {tr(fiili_makine)} × {tr(degisken_birim)} = {tr(degisken_yuklenen)} TL.",
  "TMS 2 par. 13 - değişken genel üretim giderlerinin fiilî kullanıma göre dağıtımı")

butcelenen_gug, butcelenen_saat = 720_000, 24_000
onceden_oran = butcelenen_gug / butcelenen_saat
assert onceden_oran == 30
q(f"Bir üretim bölümünün bütçelenmiş genel üretim gideri {tr(butcelenen_gug)} TL ve bütçelenmiş faaliyet hacmi {tr(butcelenen_saat)} makine saatidir. Önceden belirlenmiş genel üretim gideri yükleme oranı kaç TL/makine saatidir?",
  f"{tr(onceden_oran)} TL/makine saati",
  [f"{tr(butcelenen_saat/butcelenen_gug)} TL/makine saati",
   f"{tr(butcelenen_gug/(butcelenen_saat-4_000))} TL/makine saati",
   f"{tr(butcelenen_gug/(butcelenen_saat+6_000))} TL/makine saati",
   f"{tr(butcelenen_gug-butcelenen_saat)} TL/makine saati"],
  f"Önceden belirlenmiş oran = Bütçelenmiş GÜG / Bütçelenmiş faaliyet = {tr(butcelenen_gug)} / {tr(butcelenen_saat)} = {tr(onceden_oran)} TL/makine saatidir.",
  "TMS 2 par. 12 - genel üretim giderlerinin sistematik dağıtımı")

fiili_saat2 = 20_500
yuklenen_gug = onceden_oran * fiili_saat2
assert yuklenen_gug == 615_000
q(f"Genel üretim gideri yükleme oranı {tr(onceden_oran)} TL/makine saati ve üretim için kullanılan fiilî süre {tr(fiili_saat2)} makine saatidir. Mamullere yüklenecek genel üretim gideri kaç TL'dir?",
  f"{tr(yuklenen_gug)} TL",
  [f"{tr(onceden_oran*butcelenen_saat)} TL",
   f"{tr((onceden_oran+5)*fiili_saat2)} TL",
   f"{tr((onceden_oran-5)*fiili_saat2)} TL",
   f"{tr(fiili_saat2+onceden_oran)} TL"],
  f"Yüklenen GÜG = Önceden belirlenmiş oran × Fiilî faaliyet = {tr(onceden_oran)} × {tr(fiili_saat2)} = {tr(yuklenen_gug)} TL'dir.",
  "TMS 2 par. 12 - sistematik genel üretim gideri dağıtımı")

q("Genel üretim giderlerinin yüklenmesine ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Fiilî GÜG yüklenen GÜG'den büyükse eksik yükleme vardır\n\nII. Yüklenen GÜG fiilî GÜG'den büyükse fazla yükleme vardır\n\nIII. Eksik veya fazla yükleme yalnız değişken genel üretim giderlerinden kaynaklanır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Fiilî gider yüklenenden büyükse eksik, yüklenen fiilîden büyükse fazla yükleme vardır. Fark sabit veya değişken genel üretim giderlerinden kaynaklanabileceği için üçüncü ifade yanlıştır.",
  "1 Sıra No.lu MSUGT - 730 ve 731 hesaplarının karşılaştırılması", "hard")

eksik_kapatma = 38_000
q(f"Dönem sonunda {tr(eksik_kapatma)} TL eksik yüklenmiş genel üretim gideri belirlenmiştir. Fark önemsizdir ve tamamı Satılan Mamuller Maliyeti hesabına kapatılacaktır. Bu işlem dönem sonucunu nasıl etkiler?",
  f"Satılan mamuller maliyetini {tr(eksik_kapatma)} TL artırır",
  [f"Satılan mamuller maliyetini {tr(eksik_kapatma)} TL azaltarak brüt kârı aynı tutarda yükseltir",
   f"Mamul stokunu {tr(eksik_kapatma)} TL azaltır; satılan mamuller maliyetini hiç etkilemez",
   f"Genel yönetim giderini {tr(eksik_kapatma)} TL azaltır; üretim hesapları değişmeden kalır",
   f"Finansman giderini {tr(eksik_kapatma)} TL artırır; satışların maliyeti aynı kalır"],
  f"Eksik yükleme, mamullere fiilî giderden {tr(eksik_kapatma)} TL daha az maliyet yüklendiğini gösterir. Önemsiz fark satışların maliyetine kapatıldığında Satılan Mamuller Maliyeti artar ve brüt kâr azalır.",
  "1 Sıra No.lu MSUGT - 730 Genel Üretim Giderleri ve 731 GÜG Yansıtma")

fazla_kapatma = 42_000
q(f"Dönem sonunda {tr(fazla_kapatma)} TL fazla yüklenmiş genel üretim gideri belirlenmiştir. Fark önemsizdir ve tamamı Satılan Mamuller Maliyeti hesabına kapatılacaktır. Bu işlem dönem sonucunu nasıl etkiler?",
  f"Satılan mamuller maliyetini {tr(fazla_kapatma)} TL azaltır",
  [f"Satılan mamuller maliyetini {tr(fazla_kapatma)} TL artırarak brüt kârı aynı tutarda düşürür",
   f"Yarı mamul stokunu {tr(fazla_kapatma)} TL artırır; satışların maliyetini hiç etkilemez",
   f"Genel yönetim giderini {tr(fazla_kapatma)} TL artırır; üretim hesapları değişmeden kalır",
   f"Finansman giderini {tr(fazla_kapatma)} TL azaltır; satışların maliyeti aynı kalır"],
  f"Fazla yükleme, mamullere fiilî giderden {tr(fazla_kapatma)} TL daha fazla maliyet yüklendiğini gösterir. Önemsiz fark satışların maliyetine kapatıldığında Satılan Mamuller Maliyeti azalır ve brüt kâr artar.",
  "1 Sıra No.lu MSUGT - 730 Genel Üretim Giderleri ve 731 GÜG Yansıtma")

q("Otomasyon düzeyi yüksek bir üretim bölümünde enerji, bakım ve amortismanın oluşumunu en iyi temsil eden ortak ölçü makine saatleri ise hangi yaklaşım uygundur?",
  "Genel üretim giderlerini makine saatine göre dağıtmak",
  ["Tüm genel üretim giderlerini mamullerin satış fiyatlarına göre ve üretimle ilişki kurmadan dağıtmak",
   "Maliyetlerin oluşumuyla ilgisi olmasa da giderleri yalnız direkt malzeme tutarına göre paylaştırmak",
   "Genel üretim giderlerini stok maliyetinden çıkarıp tamamını genel yönetim gideri olarak raporlamak",
   "Makine yoğun bölümdeki tüm dolaylı maliyetleri herhangi bir anahtar kullanmadan mamullere eşit bölmek"],
  "Sistematik dağıtımda maliyet oluşumuyla neden-sonuç ilişkisi kuran ölçü tercih edilir. Makine yoğun bölümde makine saatleri uygun bir dağıtım anahtarıdır.",
  "TMS 2 par. 12 - genel üretim giderlerinin sistematik dağıtımı")

q("Farklı üretim bölümlerinde kaynak tüketim yapıları önemli ölçüde farklıysa bölüm bazında ayrı genel üretim gideri oranı kullanmanın temel yararı nedir?",
  "Mamullerin bölüm kaynaklarını daha doğru yansıtması",
  ["Bölüm oranları kullanıldığında genel üretim giderlerinin tamamının doğrudan maliyete dönüşmesini sağlaması",
   "Her bölümde aynı dağıtım anahtarını zorunlu kılarak maliyet hesaplamasını tek biçime indirmesi",
   "Sabit genel üretim giderlerinin normal kapasite kuralından tamamen çıkarılmasına imkân vermesi",
   "Üretim maliyetlerini hesaplamadan yalnız satış fiyatlarına göre stok değerlemesi yapılmasını sağlaması"],
  "Bölümlerin maliyet yapısı ve faaliyet ölçüsü farklıysa ayrı oranlar, mamullerin her bölümde tükettiği kaynakları fabrika çapında tek orandan daha doğru yansıtabilir.",
  "TMS 2 par. 12 - sabit ve değişken genel üretim giderlerinin sistematik dağıtımı")

q("Üretimle ilgisi bulunmayan merkez ofis kirasının genel üretim giderleri içine alınmamasının nedeni nedir?",
  "Stokları mevcut konum ve durumuna getirmeye katkı sağlamaması",
  ["Kira giderlerinin hiçbir koşulda maliyet veya gider olarak finansal tablolara alınamaması",
   "Merkez ofis kirasının her durumda direkt ilk madde ve malzeme maliyeti olarak kabul edilmesi",
   "Yönetim giderlerinin yalnız nakden ödendiğinde stok maliyetine eklenebilmesi ve henüz ödenmemiş olması",
   "Üretim dışı giderlerin mamul satılıncaya kadar maddi duran varlık hesabında izlenmesinin gerekmesi"],
  "Stokların mevcut konumuna ve durumuna getirilmesine katkısı olmayan genel yönetim giderleri stok maliyetine girmez; oluştukları dönemde giderleştirilir.",
  "TMS 2 par. 15-16(c) - stok maliyetine girmeyen genel yönetim giderleri")

q("Genel üretim giderleri bakımından aşağıdaki kalemlerden hangileri üretim maliyetine dâhil edilebilir?\n\nI. Fabrika makinesinin amortismanı\n\nII. Üretim hattı ustabaşının ücreti\n\nIII. Merkez satış ekibinin primi",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Fabrika makinesi amortismanı ve üretim ustabaşı ücreti dolaylı üretim maliyetidir. Merkez satış ekibinin primi satış maliyetidir ve stok maliyetine alınmaz.",
  "TMS 2 par. 12 ve 16(d) - genel üretim giderleri ile satış maliyetleri ayrımı")

dimm3, dig3, sabit_yuklenen3, degisken_yuklenen3 = 420_000, 260_000, 150_000, 95_000
satis_gideri3, normal_ustu_kayip3 = 80_000, 15_000
toplam_uretim3 = dimm3 + dig3 + sabit_yuklenen3 + degisken_yuklenen3
asal3 = dimm3 + dig3
donusum3 = dig3 + sabit_yuklenen3 + degisken_yuklenen3
assert (toplam_uretim3, asal3, donusum3) == (925_000, 680_000, 505_000)
q(f"Bir dönemde direkt ilk madde {tr(dimm3)} TL, direkt işçilik {tr(dig3)} TL, mamullere sistematik dağıtılan sabit GÜG {tr(sabit_yuklenen3)} TL ve değişken GÜG {tr(degisken_yuklenen3)} TL'dir. Ayrıca {tr(satis_gideri3)} TL satış gideri ve {tr(normal_ustu_kayip3)} TL normalin üstünde üretim kaybı vardır. Stok maliyetine alınabilecek üretim tutarı kaç TL'dir?",
  f"{tr(toplam_uretim3)} TL",
  [f"{tr(toplam_uretim3+satis_gideri3+normal_ustu_kayip3)} TL",
   f"{tr(toplam_uretim3+satis_gideri3)} TL",
   f"{tr(toplam_uretim3+normal_ustu_kayip3)} TL",
   f"{tr(asal3)} TL"],
  f"Stok maliyetine DİMM, direkt işçilik ve sistematik dağıtılan GÜG alınır: {tr(dimm3)} + {tr(dig3)} + {tr(sabit_yuklenen3)} + {tr(degisken_yuklenen3)} = {tr(toplam_uretim3)} TL. Satış gideri ve normalin üstündeki kayıp dönem gideridir.",
  "TMS 2 par. 10, 12 ve 16(a),(d) - üretim maliyetleri ile maliyete alınmayan kalemler", "hard")


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
        ch = {ans: it["correct"]}
        for k, d in zip([k for k in "ABCDE" if k != ans], it["distractors"]):
            ch[k] = d
        assert len(set(ch.values())) == 5, f"{PREFIX}-{i+1}: şık tekrarı"
        out.append({
            "id": f"{PREFIX}-{i+1:04d}", "lessonId": L, "topicId": T,
            "question": it["stem"], "choices": ch, "correctAnswer": ans,
            "explanation": it["why"],
            "source": {"kind": "generated", "styleRef": "2026/1 test biçimi",
                       "legislationRef": it["ref"]},
            "tags": ["Demo Soru", "2026 Formatı", "Konu Havuzu", LBL],
            "difficulty": it["difficulty"], "updatedAt": "2026-07-16T00:00:00Z",
            "examPeriod": "2026/1 formatına uyumlu", "legislationVersion": "2026-07-16",
            "sourceUpdatedAt": "2026-07-16T00:00:00Z", "isPremium": False, "isActive": True,
        })
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = sum(1 for x in out if len(MARK.findall(x["question"])) >= 2)
    print(f"yazıldı: {len(out)} soru | öncüllü {onc} | harf {''.join(x['correctAnswer'] for x in out)[:40]}…")
