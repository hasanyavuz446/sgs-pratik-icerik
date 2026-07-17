# -*- coding: utf-8 -*-
"""borclar_hukuku/borcun_ifasi_sona_ermesi.json — şık boyu + ifade (%36 → ≤%30).

Borçlar Hukuku'nun son dosyası. 52 sorunun 20'sinde doğru şık en uzundu.

⚠ İKİ kusur birlikte: boy + yükümlülük dili (çeldiricide 17, doğruda 1). Bu
builder boyu düzeltir; ifade çeşitlendirmesi ardından ayrı geçişte yapılır.

Kasten DOKUNULMAYAN 5: 0018 (şıklar süre — "20 yıl" = 6 karakter; uzatmak
anlamsız) · 0003 · 0023 · 0059 · 0037 (fark zaten 0-3 karakter).

Uzatmalar doğrunun EN AZ 15 KARAKTER üstüne yazıldı (sozlesmenin_kurulmasi'nda
bu kural tek turda tutturdu).
"""
import json

P = ("/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/"
     "borclar_hukuku/borcun_ifasi_sona_ermesi.json")

YAMA = {
    "ifa-gen-0002": {"C": "Bütün borçlar her durumda yalnızca alacaklının seçip belirlediği üçüncü bir kişi tarafından ifa edilir; borçlunun bizzat ifası kabul edilmez"},
    "ifa-gen-0004": {"A": "Borcun henüz doğmamış olması ve ancak ileride belirli koşulların gerçekleşmesine bağlı olarak doğabilecek nitelikte bulunması"},
    "ifa-gen-0009": {"C": "Karşılıklı, muaccel ve aynı cinsten iki borcun birbirine sayışılarak sona erdirilmesi işlemi; buna ibra adı verilmektedir"},
    "ifa-gen-0013": {"B": "Alacaklının, mevcut alacağından tek taraflı ve karşılıksız biçimde vazgeçerek borçluyu borçtan kurtarması; buna yenileme denir"},
    "ifa-gen-0014": {"A": "İki ayrı borç ilişkisinin tek bir sözleşmede toplanarak birleştirilmesi ve böylece tek bir borç hâline getirilmesi işlemi"},
    "ifa-gen-0021": {"C": "Alacaklının, alacağından tek taraflı ve karşılıksız biçimde vazgeçerek borçluyu borçtan kurtarması; buna takas adı verilir"},
    "ifa-gen-0022": {"A": "Borçtan tümüyle vazgeçildiğini gösteren ve alacaklı ile borçlu arasında yapılan bir yenileme sözleşmesi niteliğindeki anlaşma"},
    "ifa-gen-0024": {"A": "Belirli bir vade kararlaştırılmış olsa dahi temerrüt için mutlaka ayrıca ihtar çekilmesi aranır; ihtar olmadıkça temerrüt hiç oluşmaz"},
    "ifa-gen-0032": {"A": "Zamanaşımı, sözleşmenin imzalandığı andan itibaren işlemeye başlar; borcun muaccel olup olmaması bu süreyi hiç etkilemez"},
    "ifa-gen-0038": {"A": "Faiz oranı önceden kararlaştırılmadığı için hiçbir temerrüt faizi istenemez; alacaklı yalnızca anapara tutarını tahsil edebilir"},
    "ifa-gen-0039": {"D": "İfa yerine edim yalnızca tacirler arasındaki ticari işlerde; ifa uğruna edim ise yalnızca tüketici işlemlerinde geçerli olur; tarafların sıfatı bu iki kurumu birbirinden kesin çizgilerle ayıran tek ölçüttür"},
    "ifa-gen-0050": {"C": "Asıl borcun sona ermesi kefaleti iki katına çıkarır; kefil bu durumda daha geniş biçimde sorumlu hâle gelir"},
    "ifa-gen-0053": {"B": "Satıcı, kaybolan tablonun aynısını piyasadan bulup teslim eder; parça borcunda imkânsızlık borcu hiçbir biçimde etkilemez"},
    "ifa-gen-0055": {"B": "Temlik yalnızca borçlunun onayı alınırsa geçerli olur; onay bulunmadıkça borç eski alacaklıya ödenmeye devam eder ve devir sonuç doğurmaz"},
    "ifa-gen-0056": {"D": "Borçlunun, borcunu zamanında ifa etmesi hâlinde alacaklıya ayrıca ödediği ek prim niteliğindeki tutar; buna cezai şart denir"},
}

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
        d = len(q["options"][q["answer"]])
        c = max(len(v) for k, v in q["options"].items() if k != q["answer"])
        if d >= c:
            kalan.append((qid, d, c))
    if kalan:
        print(f"⚠ {len(kalan)} soruda doğru şık hâlâ en uzun:")
        for qid, d, c in kalan:
            print(f"   {qid}: doğru {d} ↔ çeldirici {c}  (+{d - c + 1} gerek)")

    json.dump(qs, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"yamalanan: {len(YAMA)} | hedefe ulaşan: {len(YAMA) - len(kalan)}/{len(YAMA)} "
          f"| kasten dokunulmayan: 5")
