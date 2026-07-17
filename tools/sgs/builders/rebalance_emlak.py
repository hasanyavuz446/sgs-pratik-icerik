# -*- coding: utf-8 -*-
"""vergi_hukuku/emlak_vergisi.json — şık boyu dengeleme (kör öğrenci %81 → ≤%30).

53 öncüllü-olmayan sorunun 47'sinde doğru şık EN UZUNDU (%90). Reçete kdv/damga/
mtv/amme ile aynı: çeldiriciler İÇERİKLE uzatılır, dolguyla değil.

★ Builder NİYETİ DOĞRULAR: yamadan sonra doğru şık hâlâ en uzunsa kaç karakter
eksik olduğunu söyler. Dört dosyada da göz kararı uzunluk yazmak tutmadı.

⚠ Emlak vergisi oranları (binde 1/2/4) ve istisna hadleri yıla/belediye türüne
bağlıdır; çeldiricilere tutar/oran sokulmadı, hepsi yapısal-kavramsal.
"""
import json

P = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/vergi_hukuku/emlak_vergisi.json"

YAMA = {
    "emlak-gen-0001": {"E": "Emlak vergisi, yalnızca gayrimenkul alım satımı sırasında el değiştiren bedel üzerinden bir defaya mahsus alınan bir işlem vergisidir"},
    "emlak-gen-0004": {"B": "Yalnızca betonarme olarak inşa edilmiş ve konut amacıyla kullanılan yapılardır; ahşap ve prefabrik yapılar bina sayılmaz"},
    "emlak-gen-0005": {"C": "Bina vergisini binanın bulunduğu belediye kendi bütçesinden karşılar; binanın malikinin hiçbir ödeme yükümlülüğü doğmaz"},
    "emlak-gen-0006": {"D": "İntifa hakkı sahibi yalnızca binada fiilen oturuyorsa mükellef olur; oturmuyorsa vergiyi çıplak mülkiyet sahibi öder"},
    "emlak-gen-0009": {"B": "Arsa, yalnızca tarımsal üretim yapılan ve belediye sınırları dışında kalan geniş arazi parçalarını ifade eder"},
    "emlak-gen-0010": {"E": "Arazi vergisini yalnızca arazinin tapudaki ilk maliki öder; araziyi sonradan devralan malikler hiçbir ödeme yapmaz"},
    "emlak-gen-0011": {"B": "Emlak vergisinde hiçbir muaflık öngörülmemiştir; sahibi ve kullanım amacı ne olursa olsun bütün bina ve araziler istisnasız vergilenir"},
    "emlak-gen-0012": {"A": "Yeni inşa edilen meskenler hiçbir hâlde muafiyetten yararlanamaz; inşaatın bittiği ilk günden itibaren tam olarak vergilendirilir"},
    "emlak-gen-0014": {"A": "Emlak vergisinin matrahı, gayrimenkulün o yıl içinde sahibine sağladığı toplam kira gelirinin tutarıdır"},
    "emlak-gen-0015": {"A": "Arsa ve arazilerin vergi değeri, malikin beyan ettiği tutarın hiçbir denetime tabi tutulmadan aynen kabul edilmesiyle belirlenir"},
    "emlak-gen-0016": {"A": "Binalar için vergi değeri, yalnızca binanın o yıl içinde getirdiği kira gelirine bakılarak ve başka ölçüt aranmadan belirlenir"},
    "emlak-gen-0017": {"A": "Mükellefiyet, vergi değerini tadil eden değişikliğin gerçekleştiği gün derhâl ve o günden itibaren başlar; izleyen yıl beklenmez"},
    "emlak-gen-0018": {"A": "Bina yıkılsa dahi mükellefiyet kesintisiz devam eder; malik artık var olmayan binanın vergisini ömür boyu ödemeyi sürdürür"},
    "emlak-gen-0019": {"A": "Vergi değerini tadil eden herhangi bir sebep kanunda sayılmamıştır; belirlenen vergi değeri hiçbir zaman değişmez ve sabit kalır"},
    "emlak-gen-0020": {"A": "Gayrimenkul satılsa dahi emlak vergisi mükellefiyeti her hâlde eski malikte kalmaya devam eder; yeni malik hiç ödeme yapmaz"},
    "emlak-gen-0021": {"A": "Emlak vergisinde hiçbir hâlde bildirim verilmez; belediye bütün tespit ve tarh işlemlerini kendiliğinden ve resen yürütür"},
    "emlak-gen-0023": {"E": "Emlak vergisi, mükellefin kendisi tarafından hesaplanıp tahakkuk ettirilir ve doğrudan Hazineye ödenir; belediyenin rolü yoktur"},
    "emlak-gen-0024": {"D": "Emlak vergisi mükellefin dilediği zaman, herhangi bir taksit dönemine veya süreye bağlı olmaksızın serbestçe ödenir"},
    "emlak-gen-0027": {"B": "Elbirliği mülkiyette her malik yalnızca kendi payına düşen eşit tutardan ve diğerlerinden bağımsız biçimde sorumludur"},
    "emlak-gen-0028": {"D": "Asgari birim değerlerini her mükellef kendi gayrimenkulü için, hiçbir ölçüye bağlı olmaksızın serbestçe belirler ve bildirir"},
    "emlak-gen-0029": {"A": "Daireyi fiilen kullandığı ve ondan yararlandığı için emlak vergisinin mükellefi kiracı (B) sayılır; malikin yükümlülüğü yoktur"},
    "emlak-gen-0030": {"D": "Bina vergisi mükellefiyeti yalnızca binanın satılmasıyla başlar; binayı inşa eden malik hiçbir dönem için vergi ödemez"},
    "emlak-gen-0031": {"A": "Belediyelere ait binalar da özel kişilerin binaları gibi hiçbir ayrım gözetilmeksizin tam olarak emlak vergisine tabi tutulur"},
    "emlak-gen-0032": {"C": "Emlak vergisi motorlu taşıtlardan, motorlu taşıtlar vergisi ise gayrimenkullerden alınır; iki verginin konusu birbirinin yerine geçmiştir"},
    "emlak-gen-0034": {"A": "Yalnızca konut olarak kullanılan bölüm bina vergisine tabidir; aynı binanın iş yeri olarak kullanılan bölümü vergi dışında kalır"},
    "emlak-gen-0035": {"A": "Arazinin arsa hâline gelmesi emlak vergisi bakımından hiçbir sonuç doğurmaz; vergi değeri ve mükellefiyet aynen devam eder"},
    "emlak-gen-0036": {"B": "Vergi değeri her yıl mükellefin kendi beyanına göre yeniden ve serbestçe belirlenir; belediyenin takdir yetkisi bulunmaz"},
    "emlak-gen-0038": {"A": "Bina yıkıldığında hem bina hem de altındaki arsa için hiçbir vergi mükellefiyeti kalmaz; taşınmaz tümüyle vergi dışına çıkar"},
    "emlak-gen-0039": {"B": "Emlak vergisinde belirlenen vergi değeri hiçbir hâlde düzeltilemez; hata bulunsa bile değer kesin ve değişmez sayılır"},
    "emlak-gen-0040": {"D": "Emlak vergisi, yalnızca gayrimenkulün satışında doğan değer artış kazancından alınan bir kazanç vergisi niteliğindedir"},
    "emlak-gen-0041": {"D": "Tarım arazilerinden yalnızca elde edilen zirai kazanç üzerinden gelir vergisi alınır; ayrıca arazi vergisi hesaplanmaz"},
    "emlak-gen-0042": {"B": "Bildirim verilmemesinin hiçbir sonucu yoktur; belediye zaten resen işlem yapacağından mükellefe ceza da kesilmez"},
    "emlak-gen-0044": {"B": "Emlak vergisi, yıl içinde gayrimenkulü en son kullanan kişinin o tarihteki durumu esas alınarak belirlenir ve ondan alınır"},
    "emlak-gen-0045": {"D": "Emlak vergisinin idaresi ve tahsili belediyeye ait olsa da elde edilen gelirin tamamı merkezi yönetim bütçesine aktarılır"},
    "emlak-gen-0046": {"B": "Emlak vergisi mükellefiyeti mirasçıya geçmez; vergi, ölen kişi adına tahakkuk ettirilerek ödenmeye devam eder"},
    "emlak-gen-0047": {"C": "Geçici muaflık, yalnızca kamu kurumlarına ait binaların vergisini kalıcı biçimde ortadan kaldırmayı amaçlayan bir düzenlemedir"},
    "emlak-gen-0048": {"B": "Daimi muaflık kanunda belirlenen belirli bir süreyle, geçici muaflık ise hiçbir süre sınırı olmaksızın süresiz tanınır"},
    "emlak-gen-0050": {"B": "Mükellef her hâlde çıplak mülkiyet sahibidir; gayrimenkulden fiilen yararlanan intifa hakkı sahibinin bir yükümlülüğü doğmaz"},
    "emlak-gen-0051": {"A": "Vergi değeri, gayrimenkulün maliki tarafından hiçbir asgari ölçüye bağlı olmaksızın ve tümüyle serbestçe belirlenip bildirilir; idare bu değeri aynen kabul eder"},
    "emlak-gen-0052": {"C": "Yurt dışında bulunan binalar, yalnızca maliki Türk vatandaşı olduğunda Türkiye'de bina vergisine tabi tutulur"},
    "emlak-gen-0053": {"A": "İzleyen yıldan başlama kuralının hiçbir istisnası bulunmaz; tadil sebebi ne olursa olsun her durumda aynı kural işletilir"},
    "emlak-gen-0054": {"A": "Kişi, sahip olduğu bütün gayrimenkuller için tek bir belediyeye tek bir toplu vergi öder; taşınmazların yeri önem taşımaz"},
    "emlak-gen-0055": {"A": "Bina vergisinde bütün binalar için tek ve aynı oran uygulanır; binanın mesken veya iş yeri olarak kullanılması hiç dikkate alınmaz"},
    "emlak-gen-0056": {"A": "Geçici muaflık süresi dolsa dahi mesken süresiz olarak muaf kalmaya devam eder; vergi hiçbir zaman doğmaz"},
    "emlak-gen-0057": {"A": "Süresinde ödenmeyen emlak vergisi için hiçbir yaptırım uygulanmaz; ödenmeyen borç bir süre sonra kendiliğinden düşer ve silinir"},
    "emlak-gen-0059": {"D": "Emlak vergisinde vergiyi doğuran olay, gayrimenkul için elektrik veya su aboneliğinin açılıp fiilen kullanıma başlanmasıdır"},
    "emlak-gen-0060": {"D": "Asgari birim değerlerini belediye meclisi her yıl hiçbir ölçüye bağlı olmaksızın serbestçe iki katına çıkarabilir"},
}

# ── 2. tur: builder'ın self-check'i 8 sorunun hedefi tutturamadığını söyledi ──
YAMA.update({
    "emlak-gen-0010": {"E": "Arazi vergisini yalnızca arazinin tapudaki ilk maliki öder; araziyi sonradan devralan malikler hiçbir dönem için ödeme yapmaz"},
    "emlak-gen-0014": {"A": "Emlak vergisinin matrahı, gayrimenkulün o yıl içinde sahibine sağladığı toplam kira ve işletme gelirinin tutarıdır"},
    "emlak-gen-0042": {"B": "Bildirim verilmemesinin hiçbir sonucu yoktur; belediye zaten resen işlem yapacağı için mükellefe ayrıca ceza da kesilmez"},
    "emlak-gen-0045": {"D": "Emlak vergisinin idaresi ve tahsili belediyeye ait olsa da elde edilen gelirin tamamı genel bütçeye ve merkezi yönetime aktarılır"},
    "emlak-gen-0046": {"B": "Emlak vergisi mükellefiyeti mirasçıya geçmez; vergi, ölen kişi adına tahakkuk ettirilerek onun adına ödenmeye devam eder"},
    "emlak-gen-0050": {"B": "Mükellef her hâlde çıplak mülkiyet sahibidir; gayrimenkulden fiilen yararlanan intifa hakkı sahibinin hiçbir vergi yükümlülüğü doğmaz"},
    "emlak-gen-0052": {"C": "Yurt dışında bulunan binalar, yalnızca maliki Türk vatandaşı olduğu takdirde Türkiye'de bina vergisine tabi tutulur"},
    "emlak-gen-0057": {"A": "Süresinde ödenmeyen emlak vergisi için hiçbir yaptırım uygulanmaz; ödenmeyen borç bir süre sonra kendiliğinden düşer ve kayıtlardan silinir"},
})

if __name__ == "__main__":
    qs = json.load(open(P, encoding="utf-8"))
    idx = {q["id"]: q for q in qs}
    for qid, degisim in YAMA.items():
        q = idx[qid]
        for harf, yeni in degisim.items():
            assert harf != q["answer"], f"{qid}: DOĞRU şıkka dokunulamaz ({harf})"
            q["options"][harf] = yeni
        assert len(set(q["options"].values())) == 5, f"{qid}: şık çakışması"

    kalan = []
    for qid in YAMA:
        q = idx[qid]
        dogru = len(q["options"][q["answer"]])
        enuzun = max(len(v) for k, v in q["options"].items() if k != q["answer"])
        if dogru >= enuzun:
            kalan.append((qid, dogru, enuzun))
    if kalan:
        print(f"⚠ {len(kalan)} soruda doğru şık hâlâ en uzun:")
        for qid, d, c in kalan:
            print(f"   {qid}: doğru {d} ↔ çeldirici {c}  (+{d - c + 1} gerek)")

    json.dump(qs, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"yamalanan: {len(YAMA)} soru | hedefe ulaşan: {len(YAMA) - len(kalan)}/{len(YAMA)}")
