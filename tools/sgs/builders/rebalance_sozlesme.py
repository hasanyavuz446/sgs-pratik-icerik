# -*- coding: utf-8 -*-
"""borclar_hukuku/sozlesmenin_kurulmasi.json — şık boyu dengeleme (%50 → ≤%30).

52 öncüllü-olmayan sorunun 29'unda doğru şık EN UZUNDU.

★ Bu builder, önceki üç dosyada üç tur yaktıran hatayı baştan önlüyor: her uzatma
doğrunun EN AZ 15 KARAKTER üstüne yazıldı. Kıl payı uzatmak (122 ↔ 123) göz
kararıyla fark edilmiyor ve dosyayı sessizce FATAL bırakıyor.

Kasten DOKUNULMAYAN 6: 0007 · 0031 · 0050 · 0053 · 0002 · 0042
(farkın zaten 3-10 karakter olduğu sorular).

⚠ Yükümlülük dili asimetrisi çok zayıf (çeldiricide 3); boy dengelemesi yeter.

Çeldiriciler TBK m.1-48'in gerçek yanılgılarını taşır: öneri ↔ icaba davet,
hak ehliyeti ↔ fiil ehliyeti, muvazaa ↔ hata/hile/korkutma, kesin hükümsüzlük
↔ iptal edilebilirlik ↔ askıda hükümsüzlük, doğrudan ↔ dolaylı temsil.
"""
import json

P = ("/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/"
     "borclar_hukuku/sozlesmenin_kurulmasi.json")

YAMA = {
    "sozlesme-gen-0001": {"A": "Yalnızca tek bir kişinin, karşı tarafın iradesine hiç ihtiyaç duymadan ve onun katılımı olmadan tek taraflı olarak yaptığı hukuki işlem türü"},
    "sozlesme-gen-0008": {"A": "Kişinin sağ doğmuş olmak koşuluyla haklara ve borçlara sahip olabilme yeteneği; buna hak ehliyeti denir ve herkeste eşit biçimde bulunur"},
    "sozlesme-gen-0011": {"A": "Ayırt etme gücüne sahip, ergin ve kısıtlı olmayan; her türlü hukuki işlemi tek başına ve geçerli biçimde yapabilen kişi; buna sınırlı ehliyetli denir"},
    "sozlesme-gen-0012": {"C": "İşlem, yasal temsilcinin onayına kadar askıda kalır; onay verilirse işlem geçmişe etkili biçimde geçerlilik kazanır ve baştan doğmuş sayılır"},
    "sozlesme-gen-0013": {"D": "Tarafların gerçek iradelerini gizleyerek görünüşte başka bir işlem yapmış gibi davranması; buna danışıklılık (muvazaa) adı verilmektedir"},
    "sozlesme-gen-0014": {"B": "Tarafların, gerçek iradelerini gizleyip görünüşte başka bir işlem yapıyormuş gibi davranması durumu; buna danışıklı işlem denir ve geçersizdir"},
    "sozlesme-gen-0015": {"D": "Tarafların, gerçek iradelerini gizleyip görünüşte başka bir işlem yapıyormuş gibi davranması hâli; bu duruma muvazaa denir ve işlem geçersiz olur"},
    "sozlesme-gen-0017": {"D": "Bir tarafın, karşı tarafın zor durumundan ya da deneyimsizliğinden yararlanarak edimler arasında aşırı bir dengesizlik yaratması; buna gabin denir"},
    "sozlesme-gen-0023": {"D": "Sözleşme, yasal temsilcinin onayına kadar askıda kalır; onay verildiğinde geçmişe etkili biçimde geçerli hâle gelir ve baştan kurulmuş sayılır"},
    "sozlesme-gen-0024": {"A": "Sözleşme baştan itibaren kesin geçersizdir; aldatma sözleşmeyi ilgili herkesçe ileri sürülebilir biçimde geçersiz kılar ve hâkim resen dikkate alır"},
    "sozlesme-gen-0026": {"B": "Sözleşme özgürlüğü sınırsızdır; taraflar hukuka, ahlaka ve kamu düzenine aykırı her türlü sözleşmeyi de geçerli biçimde yapabilir ve bunlarla bağlı kalır"},
    "sozlesme-gen-0027": {"C": "Sözleşme yalnızca taraflardan biri talep ederse iptal edilebilir; böyle bir talep gelmediği sürece sözleşme her hâlde geçerli kalmayı sürdürür"},
    "sozlesme-gen-0028": {"B": "Öneren, kabul için bir süre belirlemiş olsa dahi önerisinden her an serbestçe dönebilir; belirlediği süre önereni hiçbir biçimde bağlamaz"},
    "sozlesme-gen-0032": {"C": "Sözleşme baştan itibaren kesin geçersizdir; korkutma sözleşmeyi ilgili herkesçe ileri sürülebilir biçimde geçersiz kılar ve hâkim resen gözetir"},
    "sozlesme-gen-0034": {"D": "Bu cevap sözleşmeyi kesin hükümsüz kılar; değiştirilerek verilen kabul, sözleşmeyi baştan itibaren geçersiz yapar ve yeni bir öneri sayılmaz"},
    "sozlesme-gen-0038": {"E": "Dolaylı temsilde işlemin sonuçları hiçbir zaman temsil olunana geçemez; işlem yalnızca temsilciyi bağlar ve bu husus ancak yetkili mahkemenin vereceği kararla, resmi bir belgeye dayanılarak belirlenebilir"},
    "sozlesme-gen-0039": {"A": "Sözleşme geçerlidir; satıcının ayırt etme gücüne sahip olup olmaması sözleşmenin geçerliliğini hiçbir biçimde etkilemez ve işlem ayakta kalır"},
    "sozlesme-gen-0044": {"E": "İptal hakkı yalnızca karşı taraf bu iptali açıkça kabul ederse kullanılabilir; iradesi sakatlanan tarafın tek taraflı beyanıyla sözleşmeyi iptal etmesi hiçbir biçimde mümkün olmaz ve mahkeme kararı aranır"},
    "sozlesme-gen-0049": {"A": "Sözleşme yorumlanırken yalnızca kullanılan sözcüklerin sözlük anlamı esas alınır; tarafların gerçek ve ortak iradesi hiçbir biçimde dikkate alınmaz"},
    "sozlesme-gen-0051": {"E": "İşlem, yalnızca bir yıl içinde malik tarafından iptal edilmezse kendiliğinden geçerli hâle gelir ve sonradan hiçbir biçimde ileri sürülemez"},
    "sozlesme-gen-0054": {"A": "Alacaklının, borçludan borcun aslına ek olarak hiçbir durumda talep edemeyeceği ve kararlaştırılmış olsa dahi hukuken geçersiz sayılan bir tutar"},
    "sozlesme-gen-0057": {"D": "Esasen ehliyetli olduğu hâlde ehliyeti belirli işlemler bakımından sınırlanmış olan kişi; buna yasal danışman atanmış kişi adı verilmektedir"},
    "sozlesme-gen-0058": {"B": "Konusu başlangıçtan itibaren objektif olarak imkânsız olan sözleşme → iptal edilebilir sözleşme"},
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
          f"| kasten dokunulmayan: 6")
