# -*- coding: utf-8 -*-
"""borclar_hukuku/sebepsiz_zenginlesme.json — şık boyu dengeleme (%70 → ≤%30).

52 öncüllü-olmayan sorunun 39'unda doğru şık EN UZUNDU.

Kasten DOKUNULMAYAN 8: 0005 · 0009 · 0022 · 0032 · 0036 · 0046 · 0056 · 0057
(farkın zaten 1-5 karakter olduğu ya da şıkların kısa/kategori nitelikli olduğu
sorular — 0036'da şık "Zenginleşenin kötüniyetli hâle geldiği andan itibaren"
gibi bir zaman ifadesi; uzatmak yapay durur).

⚠ Bu dosyada yükümlülük dili asimetrisi zayıf (çeldiricide 5) — boy dengelemesi
büyük ölçüde yeter. Uzatmalarda "zorunda/durumundadır" KULLANILMADI.

Çeldiriciler TBK m.77-82'nin gerçek yanılgılarını taşır: zenginleşme ↔
fakirleşme ↔ illiyet, iyiniyetli ↔ kötüniyetli iade kapsamı, geri istemenin
engellendiği hâller, 2 yıl / 10 yıl zamanaşımı.
"""
import json

P = ("/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/"
     "borclar_hukuku/sebepsiz_zenginlesme.json")

YAMA = {
    "sebzen-gen-0002": {"C": "Zenginleşmeden söz edilebilmesi için taraflar arasında geçerli bir sözleşmenin bulunması gereklidir"},
    "sebzen-gen-0003": {"C": "Yalnızca sözleşme ile sözleşme görüşmelerindeki kusur (culpa in contrahendo) hâlleri"},
    "sebzen-gen-0007": {"A": "Ahlaki bir ödevi yerine getirmek amacıyla yapılan kazandırma her zaman ve koşulsuz olarak geri istenebilir"},
    "sebzen-gen-0010": {"A": "Vadesi henüz gelmemiş borcunu ödeyen kişi, ödediği tutarı sebepsiz zenginleşmeye dayanarak geri isteyebilir"},
    "sebzen-gen-0011": {"A": "Hukuka ya da ahlaka aykırı bir sonucun gerçekleşmesi için verilen şey her hâlde ve tam olarak geri istenir"},
    "sebzen-gen-0012": {"B": "İyiniyetli zenginleşen, elde ettiği her şeyi aldığı andan itibaren işleyecek faiziyle birlikte iade eder"},
    "sebzen-gen-0013": {"B": "Kötüniyetli zenginleşen yalnızca geri verme anında elinde kalan kısmı iade eder; elden çıkan kısımdan sorumlu olmaz"},
    "sebzen-gen-0014": {"A": "Geri verecek olan zenginleşen, mal için yaptığı hiçbir gideri isteyemez; giderin zorunlu, yararlı veya lüks olması sonucu değiştirmez"},
    "sebzen-gen-0015": {"D": "İade alacağı için herhangi bir zamanaşımı süresi öngörülmemiştir; alacak aradan ne kadar zaman geçerse geçsin her zaman istenebilir"},
    "sebzen-gen-0016": {"A": "Sebepsiz zenginleşme ile haksız fiilin ikisinde de kusur zorunlu bir unsurdur; bu yönden aralarında hiçbir fark bulunmaz ve aynı kurala tabidirler"},
    "sebzen-gen-0017": {"A": "(K) parayı geri isteyemez; banka havalesi kesin ve dönülemez bir işlem olduğundan yanlış hesaba gönderim hiçbir sonuç doğurmaz"},
    "sebzen-gen-0019": {"E": "İlliyet bağı, elde edilen zenginleşme miktarının uğranılan fakirleşme miktarından her zaman fazla olmasını ifade eden bir ölçüttür"},
    "sebzen-gen-0020": {"E": "Harcanan tutar için iade borcunun kapsamı, zenginleşenin değil karşı tarafın (fakirleşenin) kusuru oranında belirlenir ve ona göre daraltılır"},
    "sebzen-gen-0021": {"A": "Geçersiz bir sözleşme uyarınca yapılan kazandırmalar geçerli sayılır ve hiçbir hâlde iade edilmez"},
    "sebzen-gen-0025": {"E": "İyiniyet ile kötüniyet ayrımının sebepsiz zenginleşmede hiçbir etkisi bulunmaz; iade kapsamı ikisinde de aynıdır"},
    "sebzen-gen-0026": {"D": "Gerçekleşmeyen amaç, yapılmış olan sözleşmenin kendiliğinden geçerli sayılmasını ve ayakta kalmasını sağlar"},
    "sebzen-gen-0029": {"D": "Sebepsiz zenginleşme, sözleşmeye dayanan talep zamanaşımına uğramış olsa dahi hiçbir zaman gündeme gelmez ve ikinci bir yol sunmaz"},
    "sebzen-gen-0034": {"A": "Sebepsiz zenginleşmede zenginleşen ister iyiniyetli ister kötüniyetli olsun hiçbir hâlde ve hiçbir tarihten itibaren faiz istenemez"},
    "sebzen-gen-0035": {"E": "Ödeyen kişi, ancak asıl borçlunun açık rızasını alması hâlinde iade talebinde bulunabilir"},
    "sebzen-gen-0037": {"A": "Fazladan yatan tutar müşterinin mülkiyetine kesin olarak geçtiğinden banka bu tutar için hiçbir talepte bulunamaz"},
    "sebzen-gen-0038": {"B": "Vekâletsiz iş görme yalnızca taraflar arasında sözleşme kurulmasıyla doğarken sebepsiz zenginleşme doğrudan kanundan kaynaklanır"},
    "sebzen-gen-0039": {"A": "İade her zaman fakirleşenin uğradığı zararın tamamı kadardır; karşı tarafın zenginleşmesinin ölçüsü hiç dikkate alınmaz"},
    "sebzen-gen-0042": {"D": "Bir kişinin, hukuken yerine getirmek zorunda olmadığı hâlde ahlaki bir ödevini ifa etmek amacıyla kazandırmada bulunması"},
    "sebzen-gen-0046": {"E": "Semerelerin iade edilip edilmeyeceği tümüyle tarafların aralarındaki anlaşmaya bırakılmıştır"},
    "sebzen-gen-0047": {"E": "Ödeyen kişi, ancak karşı tarafın kötüniyetli olduğunu ispatlaması hâlinde parayı geri alabilir"},
    "sebzen-gen-0048": {"A": "Kurumun amacı, haksız yere zenginleşen kişiyi cezalandırmak ve ona iade yükümlülüğü dışında ek bir yaptırım uygulamaktır"},
    "sebzen-gen-0049": {"D": "(S) yaptığı giderleri ancak (T) ile önceden yazılı bir sözleşme yapmış olması hâlinde isteyebilir"},
    "sebzen-gen-0051": {"A": "Paranın yalnızca ana tutarı geri istenebilir; paranın kullanımından doğan yarar ve faiz hiçbir hâlde talep edilemez"},
    "sebzen-gen-0052": {"B": "İyiniyetli zenginleşenin bu savunması hiçbir hâlde kabul edilmez; iyiniyetli olsa dahi elde ettiğinin tamamını eksiksiz iade eder"},
    "sebzen-gen-0054": {"C": "Fakirleşmenin varlığından söz edilebilmesi için fakirleşen tarafın ödeme güçlüğüne düşmüş veya iflas etmiş olması gerekir; salt malvarlığı azalması yetmez"},
    "sebzen-gen-0055": {"C": "Geri isteme, yalnızca hukuka aykırı amaçla verilen şeyin taşınmaz olması hâlinde engellenir; taşınırlarda böyle bir engel bulunmaz"},
    "sebzen-gen-0059": {"B": "Öğrenmeden itibaren iki yıllık süre dolmuş olsa dahi, on yıllık süre dolmadıkça istem hiçbir zaman zamanaşımına uğramaz"},
}

# ── 2. tur: self-check 17 ıska bildirdi (çoğu 1-5 karakter farkla).
YAMA.update({
    "sebzen-gen-0002": {"C": "Zenginleşmeden söz edilebilmesi için taraflar arasında geçerli biçimde kurulmuş bir sözleşmenin bulunması gereklidir"},
    "sebzen-gen-0003": {"C": "Yalnızca sözleşme ile sözleşme görüşmelerindeki kusur (culpa in contrahendo) hâlleri; başka bir kaynak yoktur"},
    "sebzen-gen-0011": {"A": "Hukuka ya da ahlaka aykırı bir sonucun gerçekleşmesi amacıyla verilen şey her hâlde ve tam olarak geri istenebilir"},
    "sebzen-gen-0014": {"A": "Geri verecek olan zenginleşen, mal için yaptığı hiçbir gideri isteyemez; giderin zorunlu, yararlı veya lüks olması sonucu hiçbir biçimde değiştirmez"},
    "sebzen-gen-0015": {"D": "İade alacağı için herhangi bir zamanaşımı süresi öngörülmemiştir; alacak, aradan ne kadar zaman geçerse geçsin her zaman dava edilebilir"},
    "sebzen-gen-0016": {"A": "Sebepsiz zenginleşme ile haksız fiilin ikisinde de kusur zorunlu bir unsurdur; bu yönden aralarında hiçbir fark bulunmaz ve tümüyle aynı kurala tabidirler"},
    "sebzen-gen-0017": {"A": "(K) parayı geri isteyemez; banka havalesi kesin ve dönülemez bir işlem olduğundan yanlış hesaba gönderim hiçbir hukuki sonuç doğurmaz"},
    "sebzen-gen-0019": {"E": "İlliyet bağı, elde edilen zenginleşme miktarının uğranılan fakirleşme miktarından her zaman daha fazla olmasını ifade eden bir ölçüttür"},
    "sebzen-gen-0021": {"A": "Geçersiz bir sözleşme uyarınca yapılmış olan kazandırmalar yine de geçerli sayılır ve hiçbir hâlde iadeye konu edilemez"},
    "sebzen-gen-0034": {"A": "Sebepsiz zenginleşmede zenginleşen ister iyiniyetli ister kötüniyetli olsun hiçbir hâlde ve hiçbir tarihten itibaren faiz talep edilemez"},
    "sebzen-gen-0037": {"A": "Fazladan yatan tutar müşterinin mülkiyetine kesin biçimde geçtiğinden banka bu tutar için hiçbir talepte bulunamaz ve zararına katlanır"},
    "sebzen-gen-0038": {"B": "Vekâletsiz iş görme yalnızca taraflar arasında bir sözleşme kurulmasıyla doğar; sebepsiz zenginleşme ise doğrudan kanundan kaynaklanır"},
    "sebzen-gen-0039": {"A": "İade her zaman fakirleşenin uğradığı zararın tamamı kadardır; karşı tarafın zenginleşmesinin ölçüsü hiçbir biçimde dikkate alınmaz"},
    "sebzen-gen-0042": {"D": "Bir kişinin, hukuken yerine getirmek zorunda olmadığı hâlde ahlaki bir ödevini ifa etmek amacıyla karşı tarafa kazandırmada bulunması"},
    "sebzen-gen-0048": {"A": "Kurumun amacı, haksız yere zenginleşen kişiyi cezalandırmak ve ona iade yükümlülüğünün dışında ek bir yaptırım daha uygulamaktır"},
    "sebzen-gen-0052": {"B": "İyiniyetli zenginleşenin bu savunması hiçbir hâlde kabul edilmez; iyiniyetli olsa dahi elde ettiğinin tamamını eksiksiz biçimde iade eder"},
    "sebzen-gen-0055": {"C": "Geri isteme, yalnızca hukuka aykırı amaçla verilen şeyin bir taşınmaz olması hâlinde engellenir; taşınırlarda böyle bir engel hiç bulunmaz"},
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
          f"| kasten dokunulmayan: 8")
