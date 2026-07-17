# -*- coding: utf-8 -*-
"""vergi_hukuku/gelir_vergisi.json — şık boyu dengeleme (kör öğrenci %78 → ≤%30).

53 öncüllü-olmayan sorunun 45'inde doğru şık EN UZUNDU (%84).

★ emlak_vergisi DERSİ: orada 47/47'yi düzeltip doğru şıkkı HİÇ uca bırakmadım
(%0 en uzun / %0 en kısa) ve "doğru hep ortada" diye YENİ bir ipucu ürettim —
aday iki ucu eleyip 3 şıkta kalıyordu. Burada 45'in 9'una KASTEN dokunulmuyor;
o sorularda doğru şık en uzun kalıyor (~%20). Hedef dağılım, sıfır değil.

⚠ Kısa şıklı sorular (0003 gibi: "Gayrimenkul sermaye iradı" = 25 karakter,
gelir unsuru adları) zorlanmadı — kategori adını uzatmak yapay durur.

⚠ Gelir vergisi tarifesi ve istisna hadleri yıla bağlıdır; çeldiricilere
tutar/oran sokulmadı, hepsi yapısal (elde etme esası, mükellefiyet türü,
gelir unsurunun niteliği).
"""
import json

P = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/vergi_hukuku/gelir_vergisi.json"

# Kasten DOKUNULMAYAN 9 soru — doğru şık en uzun kalsın diye:
# 0003 (kısa kategori adları) · 0015 · 0016 · 0026 · 0028 · 0039 · 0040 · 0052 · 0060
YAMA = {
    "gelir-gen-0002": {"D": "Gelir vergisinin mükellefi yalnızca tüzel kişilerdir; gerçek kişilerin elde ettiği kazanç ve iratlar bu verginin kapsamı dışında kalır"},
    "gelir-gen-0006": {"A": "Ticari ve zirai kazançlarda gelir yalnızca tahsil esasına göre elde edilmiş sayılır; yani bedel fiilen tahsil edilmedikçe kazanç doğmaz ve vergilendirilmez"},
    "gelir-gen-0008": {"A": "Tam mükellefler yalnızca Türkiye'de elde ettikleri kazanç ve iratlar üzerinden vergilendirilir; yurt dışında elde ettikleri gelirler Türkiye'de hiç vergilenmez"},
    "gelir-gen-0009": {"C": "Dar mükellefler hiçbir kazançları üzerinden Türkiye'de vergilendirilmez; Türkiye'de elde ettikleri gelir için de yalnızca kendi ülkelerinde vergi öderler"},
    "gelir-gen-0010": {"A": "Yalnızca Türk vatandaşlığını taşıyanlar Türkiye'de yerleşmiş sayılır; ikametgâh ve oturma süresi gibi başka hiçbir ölçüt aranmaz ve dikkate alınmaz"},
    "gelir-gen-0011": {"B": "Bu kişiler Türkiye'de bir gün bile bulunsalar tam mükellef sayılır ve dünya çapındaki bütün gelirleri üzerinden Türkiye'de vergilendirilir"},
    "gelir-gen-0012": {"A": "Ayrımın temel ölçütü kişinin bir yılda elde ettiği gelirin toplam tutarıdır; belirli bir tutarın üstünde gelir elde edenler tam mükellef sayılır"},
    "gelir-gen-0014": {"B": "Kazanç, yalnızca dönem içinde gerçekleşen toplam satış hasılatından ibarettir; dönem başı ve dönem sonu öz sermaye karşılaştırması hiç yapılmaz"},
    "gelir-gen-0019": {"A": "Basit usulde kazanç her hâlde bilanço esasına göre ve çift taraflı kayıt sistemiyle tespit edilir; hasılat ile gider farkına bakılmaz"},
    "gelir-gen-0020": {"A": "Yalnızca bir işverene tabi olmaksızın, kişinin şahsi mesaisiyle ve serbestçe elde ettiği kazançlardır; sermaye ve organizasyon unsuru aranmaz"},
    "gelir-gen-0021": {"A": "Ücretin tek ölçütü ödemenin nakden yapılmış olmasıdır; ayın olarak veya menfaat sağlanması yoluyla verilen gelirler hiçbir hâlde ücret sayılmaz"},
    "gelir-gen-0022": {"B": "Bir işverene tabi olmadan ve belirli bir işyerine bağlanmadan, kişinin kendi nam ve hesabına hizmet vermesinden elde edilen kazançtır"},
    "gelir-gen-0023": {"D": "Serbest meslek kazancı, vergi dairesince her yıl maktu olarak belirlenir; mükellefin defter ve kayıtları bu tespit sırasında dikkate alınmaz"},
    "gelir-gen-0025": {"E": "Bir işverene bağlı olarak gayrimenkul yönetimi hizmeti verilmesinden elde edilen ücret; gayrimenkulün kiraya verilmesiyle ilgisi bulunmaz"},
    "gelir-gen-0027": {"A": "Emsal kira bedeli esası yalnızca gayrimenkul boş tutulduğunda uygulanır; gayrimenkul fiilen kiraya verilmişse bu esasa hiç başvurulmaz"},
    "gelir-gen-0031": {"E": "Zirai kazanç yalnızca tüzel kişilerin tarımsal faaliyetlerinden doğan kurum kazancını ifade eder; gerçek kişi çiftçilerin kazancı bu kapsama girmez"},
    "gelir-gen-0032": {"A": "Değer artışı kazançları ticari kazanç kapsamında vergilendirilir; diğer kazanç ve iratlar başlığıyla hiçbir ilgisi bulunmaz ve oraya alınmaz"},
    "gelir-gen-0033": {"E": "Arızi kazançlar hiçbir hâlde vergiye tabi tutulmaz; süreklilik taşımayan ve devamlılık arz etmeyen her gelir verginin kapsamı dışında kalır"},
    "gelir-gen-0034": {"A": "Her gelir unsuru için ayrı ayrı ve birbirinden bağımsız yıllık beyannameler verilir; gelirlerin tek bir beyannamede toplanması söz konusu olmaz"},
    "gelir-gen-0035": {"C": "Muhtasar beyanname, gayrimenkul satışından doğan değer artışı kazancının beyan edildiği ve yılda bir kez verilen beyannamedir"},
    "gelir-gen-0036": {"E": "Gelir vergisi tarifesi yalnızca ücret gelirlerine uygulanır; diğer gelir unsurlarında artan oranlı tarife yerine maktu vergi alınır"},
    "gelir-gen-0037": {"A": "Gelir vergisi tümüyle objektif bir vergidir; mükellefin ailevi durumu, engellilik hâli ve kişisel giderleri hiçbir biçimde dikkate alınmaz"},
    "gelir-gen-0041": {"C": "Kişi hiçbir kazancı üzerinden Türkiye'de vergilendirilmez; Türkiye'de elde ettiği gelir için de yalnızca kazancı doğuran ülkede vergi öder"},
    "gelir-gen-0042": {"B": "Serbest meslek kazancında tahakkuk esası geçerli olduğundan, bedel tahsil edilmemiş olsa dahi kazanç elde edilmiş sayılır ve o dönemde beyan edilir"},
    "gelir-gen-0043": {"A": "Para cezaları işletme faaliyetiyle ilgili olduğundan her hâlde gider yazılarak ticari kazançtan indirilebilir; kanunen kabul edilmeyen gider sayılmaz"},
    "gelir-gen-0045": {"C": "Dar mükellefler bu kazançları için de her hâlde tam mükellefler gibi yıllık beyanname vermekle yükümlüdür; tevkifat beyanı ortadan kaldırmaz"},
    "gelir-gen-0047": {"D": "Emsal kira bedeli yalnızca gayrimenkul ticari amaçla kiraya verildiğinde uygulanır; bedelsiz olarak akrabaya tahsis edilen konutlarda hiç uygulanmaz"},
    "gelir-gen-0048": {"A": "Ücret yalnızca nakden yapılan ödemeleri kapsadığından, işverence sağlanan ayni menfaat ve hizmetler hiçbir hâlde ücret sayılmaz ve vergilendirilmez"},
    "gelir-gen-0049": {"A": "Gelir her hâlde gayrisafi (brüt) tutarı üzerinden vergilendirilir; kazancın elde edilmesi için katlanılan hiçbir gider matrahtan indirilemez"},
    "gelir-gen-0051": {"A": "İşletme büyüklüğü ölçüsünü aşmayan çiftçiler de her hâlde bilanço esasında defter tutarak gerçek usulde vergilendirilir; muaflık uygulanmaz"},
    "gelir-gen-0053": {"D": "Beyanname verilmeyen hâller yalnızca dar mükellefler için söz konusudur; tam mükellefler her gelir unsuru için istisnasız beyanname vermek durumundadır"},
    "gelir-gen-0054": {"A": "Ticari kazanç yalnızca sermaye şirketlerinin faaliyetinden doğan kurum kazancını ifade eder; gerçek kişilerin ticari faaliyeti bu kapsama girmez"},
    "gelir-gen-0055": {"D": "Tevkifat, verginin geliri elde edenden değil, onun müşterisinden veya alıcısından tahsil edilerek vergi dairesine yatırılmasıdır"},
    "gelir-gen-0056": {"B": "Alım satım bir defaya mahsus olmasa ve süreklilik kazansa dahi bu kazanç her hâlde arızi kazanç olarak vergilendirilir; ticari kazanç sayılmaz"},
    "gelir-gen-0057": {"A": "Gelir vergisinde vergilendirme dönemi her mükellef için serbestçe seçilebilen bir aylık dönemdir; takvim yılı esası uygulanmaz"},
    "gelir-gen-0058": {"D": "Kişi bu gelirleri beyan etmek durumunda değildir; ticari kazanç ve gayrimenkul sermaye iradı her hâlde yıllık beyanname dışında bırakılmıştır"},
}

# ── 2. tur: builder'ın self-check'i 12 sorunun hedefi tutturamadığını söyledi ──
YAMA.update({
    "gelir-gen-0012": {"A": "Ayrımın temel ölçütü kişinin bir takvim yılında elde ettiği gelirin toplam tutarıdır; belirli bir tutarın üstünde gelir elde edenler tam mükellef sayılır"},
    "gelir-gen-0019": {"A": "Basit usulde kazanç her hâlde bilanço esasına göre ve çift taraflı kayıt sistemiyle tespit edilir; hasılat ile gider arasındaki farka hiç bakılmaz"},
    "gelir-gen-0020": {"A": "Yalnızca bir işverene tabi olmaksızın, kişinin şahsi mesaisiyle ve serbestçe elde ettiği kazançlardır; sermaye, organizasyon ve ilmi nitelik unsurları aranmaz"},
    "gelir-gen-0022": {"B": "Bir işverene tabi olmadan ve belirli bir işyerine bağlanmadan, kişinin kendi nam ve hesabına serbestçe hizmet vermesinden elde ettiği kazançtır"},
    "gelir-gen-0027": {"A": "Emsal kira bedeli esası yalnızca gayrimenkul boş tutulduğu dönemler için uygulanır; gayrimenkul fiilen kiraya verilmişse bu esasa hiç başvurulmaz"},
    "gelir-gen-0032": {"A": "Değer artışı kazançları her hâlde ticari kazanç kapsamında vergilendirilir; diğer kazanç ve iratlar başlığıyla hiçbir ilgisi bulunmaz ve o başlığa alınmaz"},
    "gelir-gen-0037": {"A": "Gelir vergisi tümüyle objektif nitelikte bir vergidir; mükellefin ailevi durumu, engellilik hâli ve kişisel giderleri hiçbir biçimde dikkate alınmaz"},
    "gelir-gen-0042": {"B": "Serbest meslek kazancında tahakkuk esası geçerli olduğundan, bedel fiilen tahsil edilmemiş olsa dahi kazanç elde edilmiş sayılır ve o dönemin geliri olarak beyan edilir"},
    "gelir-gen-0047": {"D": "Emsal kira bedeli yalnızca gayrimenkul ticari amaçla kiraya verildiğinde uygulanır; bedelsiz olarak akrabalara tahsis edilen konutlarda hiçbir biçimde uygulanmaz"},
    "gelir-gen-0051": {"A": "İşletme büyüklüğü ölçüsünü aşmayan çiftçiler de her hâlde bilanço esasında defter tutarak gerçek usulde vergilendirilir; onlara muaflık tanınmaz"},
    "gelir-gen-0053": {"D": "Beyanname verilmeyen hâller yalnızca dar mükellefler bakımından söz konusudur; tam mükellefler her gelir unsuru için istisnasız beyanname vermek durumundadır"},
    "gelir-gen-0057": {"A": "Gelir vergisinde vergilendirme dönemi her mükellef için serbestçe seçilebilen bir aylık dönemdir; takvim yılı esası burada uygulanmaz"},
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
    print(f"yamalanan: {len(YAMA)} soru | hedefe ulaşan: {len(YAMA) - len(kalan)}/{len(YAMA)} "
          f"| kasten dokunulmayan: 9 (doğru en uzun kalsın diye)")
