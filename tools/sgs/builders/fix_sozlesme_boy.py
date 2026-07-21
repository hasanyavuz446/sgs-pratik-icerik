# -*- coding: utf-8 -*-
"""sozlesme_turleri.json — şık boyu dengeleme (kör %91 → ≤%30).

build_sozlesme_turleri.py'yi bu oturumun dersini UNUTARAK yazdım: doğru şıklar
çeldiricilerden uzun çıktı (%91 en uzun). Düzeltme: her hedef soruda BİR çeldiriciyi
doğrunun üstüne çıkar — dolgu değil, hukuken tutarlı YANLIŞ bir ikinci cümle ekle
(soruyu da zenginleştirir). ~%20 soru kasten doğru-en-uzun bırakılır.

Doğru cevaba/köke/çözüme DOKUNULMAZ (0/0/0/0). Uzatma doğrunun ≥8 karakter üstünde.
"""
import json

P = "content/borclar_hukuku/sozlesme_turleri.json"
CP = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/borclar_hukuku/sozlesme_turleri.json"

# {id_son4: {harf: yeni_uzun_çeldirici}}  — mevcut çeldiriciyi yanlış bir sonuç
# cümlesiyle uzat. Hedef: doğrunun ≥8 karakter üstü.
UZ = {
 "0003": ("C", "Bir tarafın edimine karşılık diğer tarafın para ödemeyi üstlendiği ve bu yönüyle her zaman karşılıklı borç doğuran sözleşmedir"),
 "0004": ("C", "Tarafların iradesine bakılmaksızın kanun gereği kendiliğinden kurulan ve kurulması için irade açıklaması aranmayan sözleşmedir"),
 "0005": ("A", "Edimin tek bir anda, bir defada yerine getirilerek tükendiği ve süreye yayılması hiçbir hâlde mümkün olmayan sözleşmedir"),
 "0006": ("B", "Satıcının yalnızca malı kullandırma, alıcının ise dönemsel kira ödeme borcu altına girdiği ve mülkiyetin hiç geçmediği sözleşmedir"),
 "0007": ("B", "Kiracının hiçbir bedel ödemeksizin malı kullanmasına izin verilen ve bu yönüyle satış niteliği taşıdığı kabul edilen sözleşmedir"),
 "0008": ("A", "Taraflar yalnızca kanunda ad verilmiş sözleşme tiplerinden birini seçmek zorunda olup kanun dışı bir tip kararlaştıramaz"),
 "0009": ("C", "Tarafların tacir sıfatını taşıyıp taşımadığına bakılarak belirlenir; taraflar tacir değilse sözleşme her hâlde ivazsız sayılır"),
 "0010": ("C", "Yarar ve hasar, mal satıcının elinde kaldığı sürece dahi her hâlde alıcıya ait olup teslimin bu konuda hiçbir etkisi yoktur"),
 "0011": ("B", "Satıcı yalnızca satılanın hiç teslim edilememesinden sorumlu olup teslimden sonraki ayıplardan hiçbir hâlde sorumlu tutulamaz"),
 "0012": ("B", "Ayıp bildirimi yalnızca satıştan tam bir yıl sonra yapılabilir; bu süreden önce yapılan her bildirim baştan geçersiz sayılır"),
 "0013": ("A", "Satıcı, satıştan sonra doğan haklara dayanan zapttan da her hâlde sorumlu olup sorumluluğun doğduğu tarih hiç önem taşımaz"),
 "0014": ("E", "Satıcı malı, ancak alıcı bedelin iki katını depozito olarak yatırdığında teslim eder; aksi hâlde teslimden kaçınabilir"),
 "0016": ("A", "Taksitle satış hiçbir şekil koşuluna tabi olmayıp yalnızca sözlü anlaşmayla geçerli olur; yazılılık ve zorunlu kayıt aranmaz"),
 "0017": ("A", "Bedelin sözleşmede rakamla açıkça belirtilmemesi hâlinde satış her durumda kesin olarak geçersiz sayılır ve taraflar arasında hiçbir hüküm doğurmaz"),
 "0018": ("A", "Bağışlananın, aldığı mal karşılığında bağışlayana denk bir bedel ödediği ve bu yönüyle satışa yaklaşan bir sözleşmedir"),
 "0019": ("B", "Bağışlama sözü verme hiçbir şekil koşuluna tabi olmayıp sözlü de geçerlidir; yazılılık yalnızca ispat için aranan bir usuldür"),
 "0020": ("E", "Elden bağışlama her hâlde bağışlayanın mirasçılarının önceden verdiği yazılı onaya bağlı olup onaysız yapılan bağış geçersizdir"),
 "0021": ("A", "Bağışlayan, hiçbir sebep göstermeksizin ve bağışlananın kusuru aranmaksızın her zaman bağışlamadan serbestçe dönebilir"),
 "0022": ("B", "Bağışlayan, bağışladığı malın her türlü ayıbından kusuru aranmaksızın tıpkı bir satıcı gibi tam olarak sorumlu tutulur"),
 "0023": ("A", "Kiracı belirli süreli sözleşmeyi hiçbir hâlde süresinden önce veya süre bitiminde sona erdiremez; süre dolsa dahi sözleşmeyle bağlı kalmaya devam eder"),
 "0024": ("A", "Kiraya veren, hiçbir sebep göstermeksizin yalnızca süre bitiminde yapacağı bir bildirimle sözleşmeyi serbestçe sona erdirebilir"),
 "0025": ("B", "Kiraya veren, kiracıya süre vermeksizin ilk gecikmede sözleşmeyi kendiliğinden ve derhâl sona erdirmiş sayılır; ihtar gerekmez"),
 "0026": ("B", "Alt kira için kiraya verenin onayı hiçbir hâlde gerekmez ve kiraya verene zarar verilmemesi gibi bir koşul aranmadan kiracı kiralananı dilediğine bırakabilir"),
 "0027": ("B", "Kiraya verenin kiralananı kullanıma elverişli durumda bulundurma gibi bir borcu yoktur; bu külfetin tamamı kiracıya aittir"),
 "0028": ("D", "Kira sözleşmesi, ancak kiracının yeni malikle baştan yeni bir sözleşme yapması hâlinde devam eder; aksi hâlde kendiliğinden düşer"),
 "0029": ("B", "Kiracı, kiralananı dilediği gibi kullanıp tahrip edebilir; bundan ve komşulara verdiği rahatsızlıktan hiçbir sorumluluğu doğmaz"),
 "0030": ("E", "Kira, bir malın karşılıksız kullandırılmasını konu alan ve kiracıya hiçbir ödeme yükü getirmeyen ivazsız bir sözleşmedir"),
 "0031": ("B", "Ödünç alanın, aldığı şeyi tüketip yerine aynı nitelikte başka bir şey iade ettiği ve mülkiyetin ödünç alana hiçbir zaman geçmediği sözleşmedir"),
 "0034": ("D", "İki sözleşme arasında mülkiyetin geçip geçmemesi bakımından hiçbir fark bulunmaz; her ikisinde de yalnızca kullanım devredilir ve şeyin aynısı geri verilir"),
 "0035": ("A", "İşçinin bir eseri meydana getirmeyi, işverenin de bu eser karşılığında götürü bir bedel ödemeyi üstlendiği bir sonuç sözleşmesi olarak tanımlanır"),
 "0036": ("E", "Hizmet sözleşmesi yalnızca işçi ve işverenin tacir sıfatını taşıması hâlinde geçerli olup tacir olmayanlar arasında kurulamaz"),
 "0037": ("A", "Her iki sözleşmede de yalnızca belirli bir sonucun meydana getirilmesi esas olup bağımlı iş görme unsuru hiçbirinde aranmaz ve ikisi de sonuç borcu doğurur"),
 "0038": ("A", "İşverenin, işçinin sağlığını veya iş güvenliğini gözetme gibi bir yükümü bulunmaz; bu önlemlerin tamamı işçinin sorumluluğundadır"),
 "0039": ("D", "İşçi, işverenin haklı menfaatine aykırı davranışlarından hiçbir hâlde sorumlu tutulamaz; sadakat borcu ancak yazılıysa doğar"),
 "0040": ("C", "Yüklenicinin, meydana getirdiği bir malın mülkiyetini iş sahibine devretmeyi üstlendiği ve bu yönüyle satışa dönüşen sözleşmedir"),
 "0041": ("C", "Yüklenici, iş sahibinin açık onayı olmadan eseri hiçbir yardımcıya veya alt yükleniciye yaptıramaz; işi bizzat yapmak zorundadır"),
 "0042": ("D", "Eser ayıplı olsa dahi iş sahibi yalnızca yükleniciyi değiştirmeyi isteyebilir; onarım, indirim veya ret gibi bir hakkı yoktur"),
 "0043": ("B", "Götürü bedelde yüklenici, harcadığı emek ve malzeme arttıkça kararlaştırılan bedeli her zaman tek taraflı olarak artırabilir"),
 "0045": ("E", "Sözleşmeyi tamamlanmadan feshetme hakkı yalnızca yükleniciye tanınmıştır; iş sahibinin böyle bir fesih hakkı hiçbir hâlde yoktur"),
 "0046": ("A", "Vekilin, vekâlet verene belirli bir malın mülkiyetini devretmeyi üstlendiği ve bu yönüyle satış niteliği taşıyan sözleşmedir"),
 "0047": ("D", "Azil ve istifa yalnızca sözleşmede bu yönde açık bir kayıt bulunması hâlinde mümkündür; aksi hâlde vekâlet süresince bağlılık sürer"),
 "0048": ("A", "Vekil, vekâlet verenin açık talimatlarını hiçbir hâlde dikkate almak zorunda değildir; her koşulda tümüyle kendi bildiği gibi serbestçe hareket eder"),
 "0049": ("D", "Vekilin göstereceği özenin ölçüsü, yalnızca kendi işlerinde gösterdiği özenle sınırlı olup basiretli bir vekilin özeni aranmaz"),
 "0050": ("A", "Vekilin, vekâlet verene yaptığı işin hesabını verme veya iş dolayısıyla edindiklerini kendisine teslim etme gibi herhangi bir yükümü bulunmaz"),
 "0051": ("D", "Vekâlet yalnızca vekilin ölümüyle sona erer; vekâlet verenin ölümü, ehliyetini yitirmesi veya iflası vekâleti hiç etkilemez"),
 "0052": ("A", "Kefilin, borçlunun borcunu bizzat üstlenerek asıl borçlunun yerine geçtiği ve fer'i değil asli borç altına girdiği sözleşmedir"),
 "0053": ("B", "Kefalet için yalnızca alacaklının imzası yeterli olup kefilin el yazısı, azami miktar ve tarih gibi kayıtlar aranmadan sözleşme geçerli sayılır"),
 "0054": ("B", "Adi kefalette alacaklı, asıl borçluya hiç başvurmadan ve onu takip etmeden doğrudan doğruya kefile başvurup ödemeyi ondan isteyebilir"),
 "0056": ("D", "Kefaletin geçerliliği asıl borcun geçerliliğinden hiçbir biçimde etkilenmez; asıl borç geçersiz olsa dahi kefalet ayakta kalır"),
 "0057": ("A", "Simsarın, iş sahibi adına ve hesabına üçüncü kişilerle doğrudan sözleşme yapmayı üstlendiği ve onu temsil ettiği sözleşmedir"),
 "0058": ("B", "Bir kimsenin, kendi işini bizzat görmesini ifade eden ve üçüncü kişinin işine karışmasını dışlayan bir hukuki kavramdır"),
 "0059": ("A", "Saklayanın, kendisine bırakılan malın mülkiyetini kazandığı ve onu serbestçe kullanıp tüketebildiği bir sözleşmedir"),
 "0060": ("B", "Karşılıksız olarak yalnızca bir defalık bir edim taahhüdünü içeren ve sürekli bakma veya gelir sağlama borcu doğurmayan sözleşmelerdir"),
}

# Bu sorularda uzatmayı UYGULAMA — doğru şık EN UZUN kalsın (uç). Böylece
# "iki ucu ele, ortadan tahmin et" stratejisi doğruyu orta kümede bulamaz;
# doğru şıkkın boy-sırası uçlara (~%20 en uzun) yayılır. Kalan ~39 soruda doğru
# 2.en uzun (sıra 4) → "en uzunu seç" yanlış çeldiriciyi getirir (babanın şikâyeti).
REVERT = {"0003","0006","0009","0012","0016","0019","0022","0028",
          "0036","0040","0043","0047","0052"}

# DOLGU ("zorunda/…") temizliği — audit'in "dolguluyu ele" stratejisi bu kelimeleri
# eleyip doğruyu en uzun bırakıyordu. Aynı yanlış anlamı DOLGU'suz, aynı boyda yaz.
DEFILLER = {
 ("0008", "A"): "Taraflar yalnızca kanunda ad verilmiş sözleşme tiplerinden birini seçebilir; kanunda düzenlenmeyen bir tip hiçbir hâlde kararlaştıramaz",
 ("0028", "E"): "El değiştirme hâlinde kiracı kiralananı derhâl boşaltıp teslim eder",
 ("0041", "A"): "Yüklenici eseri her hâlde bir başkasına devretmekle yükümlüdür",
 ("0041", "C"): "Yüklenici, iş sahibinin açık onayı olmadan eseri hiçbir yardımcıya veya alt yükleniciye yaptıramaz; eseri her hâlde bizzat kendisi meydana getirir",
 ("0048", "A"): "Vekil, vekâlet verenin açık talimatlarıyla hiçbir hâlde bağlı değildir; her koşulda tümüyle kendi bildiği gibi serbestçe hareket eder",
 ("0055", "A"): "Müteselsil kefalette alacaklı her hâlde önce asıl borçluya başvurur",
}

if __name__ == "__main__":
    qs = json.load(open(P, encoding="utf-8"))
    idx = {q["id"][-4:]: q for q in qs}
    eksik = []
    for tag, (harf, yeni) in UZ.items():
        if tag in REVERT:
            continue
        q = idx[tag]
        d = len(q["options"][q["answer"]])
        assert harf != q["answer"], f"{tag}: DOĞRU şıkka dokunulamaz"
        if len(yeni) < d + 8:  # hedef: doğrunun ≥8 üstü
            eksik.append((tag, harf, len(yeni), d, d + 8 - len(yeni)))
        q["options"][harf] = yeni
    if eksik:
        print(f"KISA UZATMA ({len(eksik)}):")
        for tag, harf, ly, d, gap in sorted(eksik, key=lambda x: -x[4]):
            print(f"  {tag}/{harf}: {ly} < doğru {d}+8 ({gap} eksik)")
        raise SystemExit(1)
    import re
    DOLGU = re.compile(r"zorunda|durumundadır|bulunmaktadır|kalınmaktadır|tutulmaktadır")
    for (tag, harf), yeni in DEFILLER.items():
        q = idx[tag]
        assert harf != q["answer"], f"{tag}: DOĞRU şıkka dokunulamaz"
        assert not DOLGU.search(yeni), f"{tag}/{harf}: DEFILLER'da hâlâ dolgu var"
        q["options"][harf] = yeni
    for q in qs:
        assert len(set(q["options"].values())) == 5, f"{q['id']}: şık çakışması"
    for path in (P, CP):
        json.dump(qs, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"uzatıldı: {len(UZ)} soru")
