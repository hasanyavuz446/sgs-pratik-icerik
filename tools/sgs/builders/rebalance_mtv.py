# -*- coding: utf-8 -*-
"""vergi_hukuku/mtv.json — şık boyu dengeleme (kör öğrenci %85 → hedef ≤%30).

53 öncüllü-olmayan sorunun 49'unda doğru şık EN UZUNDU (%94). Reçete kdv/damga
ile aynı: çeldiriciler İÇERİKLE uzatılır, dolguyla değil.

⚠ Bu dosyada fark DAR (çeldiriciler zaten 84–113, doğru 107–160). Uzatmalar da
kısa: çoğu soruda tek çeldiriciye bir yan cümle yetiyor. Gereksiz şişirmek
şıkları birbirine benzetip soruyu bulanıklaştırır.

⚠⚠ MTV TARİFE TUTARLARI HER YIL DEĞİŞİR. Çeldiricilere yıla bağlı tutar/oran
sokulmadı; hepsi yapısal-kavramsal (ölçüt, mükellefiyet başlangıcı, istisna
mantığı). Bkz. URETIM_KURALLARI §9.
"""
import json

P = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/vergi_hukuku/mtv.json"

YAMA = {
    "mtv-gen-0001": {"C": "Motoru bulunsun bulunmasın her türlü kara, deniz ve hava taşıtı ayrım gözetilmeksizin verginin konusuna girer; motorsuz araçlar da kapsamdadır"},
    "mtv-gen-0002": {"A": "Motorlu taşıtlar vergisi, taşıtın bir yıl içinde sahibine sağladığı gelir üzerinden alınan ve beyanname ile ödenen bir gelir vergisidir"},
    "mtv-gen-0005": {"A": "Vergi, her taşıt için taşıtın güncel piyasa satış değerine sabit bir oran uygulanmak suretiyle nispi olarak hesaplanır ve her yıl yeniden belirlenir"},
    "mtv-gen-0007": {"A": "Motorlu taşıtı fiilen kullanan ancak adına kayıt ve tescil bulunmayan sürücüler verginin mükellefi sayılır; sicildeki malik sorumlu tutulmaz"},

    # ↓ doğru EN KISA olsun
    "mtv-gen-0008": {
        "B": "Vergiyi doğuran olay, motorlu taşıtın fabrikadan çıkıp satılmak üzere ilk kez bir galeriye teslim edilmesidir",
        "C": "Vergiyi doğuran olay, motorlu taşıtın trafiğe çıkarılıp yolda ilk kez fiilen kullanılmaya başlanmasıdır",
        "D": "Vergiyi doğuran olay, motorlu taşıt için bir yıllık zorunlu trafik sigortasının yaptırılıp poliçenin düzenlenmesidir",
        "E": "Vergiyi doğuran olay, motorlu taşıtın periyodik fenni muayenesinin yaptırılıp uygunluk belgesinin alınmasıdır",
    },
    "mtv-gen-0009": {"A": "Mükellefiyet, taşıt hangi ayda kayıt ve tescil edilirse edilsin her hâlde kaydı izleyen takvim yılının başından itibaren başlar"},
    "mtv-gen-0010": {"B": "Motorlu taşıtın vergisi bir kez ödendikten sonra mükellefiyet, taşıt satılsa veya hurdaya ayrılsa bile hiçbir zaman sona ermez"},
    "mtv-gen-0011": {"A": "Taşıt satılsa da mükellefiyet eski malikte kalmaya devam eder; sicile tescil edilen yeni malik hiçbir zaman verginin mükellefi olmaz"},
    "mtv-gen-0013": {"B": "Otomobillerde vergi, yalnızca taşıtın rengine ve markasının prestij değerine göre belirlenen maktu tutarlar üzerinden alınır"},

    # ↓ doğru EN KISA olsun
    "mtv-gen-0014": {
        "A": "Taşıtın yaşının vergiye hiçbir etkisi yoktur; sıfır ve yirmi yaşındaki taşıt için tamamen aynı tutar uygulanır",
        "B": "Taşıtın yaşı arttıkça vergi kademeli olarak sürekli artar; en yaşlı taşıtlar tarifedeki en yüksek vergiyi öder",
        "C": "Taşıtın yaşı yalnızca deniz taşıtlarında dikkate alınır; kara taşıtlarında yaş ölçütü tarifede hiç kullanılmaz",
        "D": "Taşıtın yaşı yalnızca taşıt ilk kez tescil edilirken önem taşır; sonraki yıllarda tarifede hiç dikkate alınmaz",
    },
    "mtv-gen-0015": {"A": "Uçak ve helikopterlerde vergi, taşıtın bir yıl içinde gerçekleştirdiği toplam uçuş saati üzerinden değişken olarak alınır"},
    "mtv-gen-0016": {"B": "Kanundaki maktu vergi tutarları bir kez belirlenmiştir; aradan yıllar geçse ve para değeri düşse de hiçbir zaman değişmez"},
    "mtv-gen-0017": {"A": "Motorlu taşıtlar vergisinde hiçbir istisna veya muafiyet öngörülmemiştir; taşıtı ne olursa olsun her sahip istisnasız vergi öder"},
    "mtv-gen-0018": {"A": "Engellilere ait taşıtlar da diğer taşıtlar gibi her hâlde ve tam olarak motorlu taşıtlar vergisine tabi tutulur; ayrık bir düzenleme yoktur"},
    "mtv-gen-0021": {"C": "Motorlu taşıtın devri, yalnızca alıcının o taşıtın geçmiş yıllara ait tüm trafik cezalarını da ayrıca üstlenmesi hâlinde mümkün olabilir"},
    "mtv-gen-0022": {"D": "Fenni muayene, taşıtın vergi borcuna değil yalnızca taşıtın yaşının kanunda belirlenen sınırın altında kalmasına bağlı tutulmuştur"},
    "mtv-gen-0024": {"A": "Taşıt Şubat ayında tescil edildiği için (A)'nın mükellefiyeti ancak bir sonraki takvim yılının başından itibaren doğar ve o yıl vergi alınmaz"},
    "mtv-gen-0025": {"B": "Taşıt Eylül ayında tescil edildiği için (B)'nin mükellefiyeti ancak bir sonraki takvim yılının başından itibaren doğar; o yıl için vergi alınmaz"},
    "mtv-gen-0026": {"B": "Taşıt sicilden silinse dahi (C)'nin mükellefiyeti kesintisiz devam eder; hurdaya ayrılan taşıtın vergisini ödemeyi sürdürür"},
    "mtv-gen-0027": {"C": "Taşıtın devri, (E)'nin taşıta ilişkin geçmiş yıllara ait tüm trafik cezalarını da ayrıca üstlenmesi koşuluyla gerçekleştirilebilir"},
    "mtv-gen-0028": {"B": "Motorlu taşıtlar vergisi gayrimenkuller üzerinden, emlak vergisi ise motorlu taşıtlar üzerinden alınır; ikisinin konusu birbirinin yerine geçer"},
    "mtv-gen-0029": {"B": "Taşıt yıl içinde el değiştirdiğinde o yıla ait verginin tamamı ilk malikte kalır; sonraki malikler o yıl için hiçbir ödeme yapmaz"},
    "mtv-gen-0030": {"A": "İki özdeş otomobilden, sahibinin yıllık geliri daha yüksek olanı artan oranlı tarife nedeniyle diğerinden daha fazla vergi öder"},
    "mtv-gen-0031": {"B": "Elçilik ve konsolosluk taşıtları da diğer taşıtlar gibi her hâlde tam olarak motorlu taşıtlar vergisine tabidir; ayrık bir hüküm bulunmaz"},

    # ↓ doğru EN KISA olsun
    "mtv-gen-0032": {
        "A": "Bütün taşıt cinsleri için tek ve aynı maktu tutar uygulanır; taşıtın cinsi tarifede hiçbir biçimde dikkate alınmaz",
        "B": "Vergi yalnızca otomobiller için öngörülmüştür; motosiklet, kamyon ve otobüs gibi taşıtlar verginin kapsamı dışında kalır",
        "C": "Taşıt cinsi yalnızca deniz taşıtlarında dikkate alınır; bütün kara taşıtları için tek ve ortak bir tarife uygulanır",
        "D": "Taşıt cinsinin vergiye bir etkisi bulunmaz; vergi yalnızca taşıt sahibinin mesleğine ve unvanına göre belirlenir",
    },
    "mtv-gen-0034": {"A": "Vergi, taşıtı o dönemde fiilen ve en çok kullanan kişiden alınır; sicildeki kayıt ve tescil bilgisi dikkate alınmaz"},
}

# ── 2. tur: scriptin kendi denetimi 14 sorunun hedefi tutturamadığını söyledi ──
# Göz kararı uzatmak yetmiyor; gereken karakter kadar açıldı.
YAMA.update({
    "mtv-gen-0001": {"C": "Motoru bulunsun bulunmasın her türlü kara, deniz ve hava taşıtı ayrım gözetilmeksizin verginin konusuna girer; motorsuz römork ve bisikletler de kapsamdadır"},
    "mtv-gen-0002": {"A": "Motorlu taşıtlar vergisi, taşıtın bir yıl içinde sahibine sağladığı kira ve işletme geliri üzerinden alınan ve beyanname ile ödenen bir gelir vergisidir"},
    "mtv-gen-0009": {"A": "Mükellefiyet, taşıt hangi ayda kayıt ve tescil edilirse edilsin her hâlde kaydı izleyen takvim yılının Ocak ayı başından itibaren başlar; tescil yılı için vergi doğmaz"},
    "mtv-gen-0010": {"B": "Motorlu taşıtın vergisi bir kez ödendikten sonra mükellefiyet, taşıt satılsa, hurdaya ayrılsa veya sicilden silinse bile hiçbir zaman sona ermez; kayıt ömür boyu sürer"},
    "mtv-gen-0013": {"B": "Otomobillerde vergi, yalnızca taşıtın rengine, kasa tipine ve markasının piyasadaki prestij değerine göre belirlenen maktu tutarlar üzerinden alınır; motor ve yaş ölçütü kullanılmaz"},
    "mtv-gen-0014": {"B": "Taşıtın yaşı arttıkça vergi kademeli olarak sürekli artar; tarifede en yaşlı taşıtlar en yüksek, sıfır taşıtlar ise en düşük vergiyi öder"},
    "mtv-gen-0016": {"B": "Kanundaki maktu vergi tutarları bir kez belirlenmiştir; aradan yıllar geçse, para değeri düşse ve enflasyon yaşansa da bu tutarlar hiçbir zaman değişmez"},
    "mtv-gen-0017": {"A": "Motorlu taşıtlar vergisinde hiçbir istisna veya muafiyet öngörülmemiştir; taşıtın sahibi ve kullanım amacı ne olursa olsun her malik istisnasız vergi öder"},
    "mtv-gen-0018": {"A": "Engellilere ait taşıtlar da diğer bütün taşıtlar gibi her hâlde ve tam olarak motorlu taşıtlar vergisine tabi tutulur; bu kişiler için ayrık bir düzenleme öngörülmemiştir"},
    "mtv-gen-0021": {"C": "Motorlu taşıtın devri, yalnızca alıcının o taşıta ilişkin geçmiş yıllara ait bütün trafik cezalarını da ayrıca üstlenmesi hâlinde mümkün olabilir; vergi borcu aranmaz"},
    "mtv-gen-0026": {"B": "Taşıt sicilden silinse dahi (C)'nin mükellefiyeti kesintisiz olarak devam eder; hurdaya ayrılmış olsa bile taşıtın vergisini her yıl ödemeyi sürdürür"},
    "mtv-gen-0029": {"B": "Taşıt yıl içinde el değiştirdiğinde o yıla ait verginin tamamı ilk malikte kalır; sonraki malikler o takvim yılı için hiçbir ödeme yapmaz ve sorumlu tutulmaz"},
    "mtv-gen-0030": {"A": "İki özdeş otomobilden, sahibinin yıllık geliri daha yüksek olanı artan oranlı tarife nedeniyle diğerinden belirgin biçimde daha fazla motorlu taşıtlar vergisi öder"},
    "mtv-gen-0032": {"B": "Vergi yalnızca otomobiller için öngörülmüştür; motosiklet, kamyon, otobüs ve minibüs gibi taşıtlar verginin kapsamı dışında kalır"},
})

# ── 3. tur: kalan 23 soru ────────────────────────────────────────────────────
YAMA.update({
    "mtv-gen-0035": {"A": "Kişi, adına kayıtlı taşıt sayısı birden fazla olsa da yalnızca en değerli taşıtı için tek bir vergi öder; diğer taşıtları için mükellefiyet doğmaz ve vergi aranmaz"},
    "mtv-gen-0036": {"B": "Motorlu taşıtlar vergisi, yalnızca taşıt satıldığında ve noterde devir işlemi yapılırken bir defaya mahsus olmak üzere tahakkuk ettirilir; sonraki yıllarda vergi doğmaz"},
    "mtv-gen-0037": {"C": "Motorlu taşıtlar vergisi akaryakıt tüketimi üzerinden, akaryakıttan alınan vergiler ise taşıta sahip olma üzerinden alınır; ikisinin konusu birbirinin yerine geçmiş durumdadır"},
    "mtv-gen-0039": {"C": "Süresinde ödenmeyen motorlu taşıtlar vergisi, ödenene kadar her ay iki katına çıkarak katlanarak artar; gecikme zammı yerine bu katlanma uygulanır"},

    # ↓ doğru EN KISA olsun
    "mtv-gen-0040": {
        "A": "Taşıt değeri hiçbir tarifede dikkate alınmaz; vergi yalnızca taşıtın rengine, kasa tipine ve model yılına göre belirlenir",
        "B": "Taşıt değeri dikkate alınan taşıtlarda vergi, değere sabit bir oran uygulanarak tümüyle nispi hâle gelir ve maktu tutar kalmaz",
        "D": "Taşıt değeri yalnızca uçak ve helikopterlerde dikkate alınır; kara taşıtlarında değer ölçütü tarifede hiç kullanılmaz",
        "E": "Taşıt değeri dikkate alınan taşıtlarda vergi, taşıt sahibinin yıllık gelirine göre artan oranlı olarak belirlenir",
    },
    "mtv-gen-0041": {"A": "Taşıt devredilse de sonraki dönemlerin vergisi eski malik (F)'de kalmaya devam eder; sicile tescil edilen yeni malik (G) hiçbir dönem için vergi ödemez"},
    "mtv-gen-0042": {"A": "Bu taşıtlarda vergi, yalnızca taşıtın güncel piyasa satış değerine sabit bir oran uygulanarak nispi biçimde alınır; motor gücü ve yaş ölçütleri kullanılmaz"},
    "mtv-gen-0043": {"B": "Motosikletlerde vergi, yalnızca taşıtın rengine ve markasının piyasadaki prestij değerine göre belirlenen maktu tutarlar üzerinden alınır; motor silindir hacmi dikkate alınmaz"},
    "mtv-gen-0044": {"A": "Motorlu deniz taşıtlarında vergi, yalnızca taşıtın bir yıl içinde denizde geçirdiği toplam saat üzerinden hesaplanır; motor gücü ve boy ölçütleri kullanılmaz"},
    "mtv-gen-0045": {"A": "Taşıt çalınsa da kaydı sicilden silinene kadar mükellefiyet devam eder; kayıt silinse bile taşıtın vergisi malikten ömür boyu istenmeye devam eder"},

    # ↓ doğru EN KISA olsun
    "mtv-gen-0046": {
        "B": "Vergi, mükellefin ailevi ve kişisel durumuna göre indirim ve istisnalarla belirlenen, kişiye göre değişen şahsi bir vergidir",
        "C": "Vergi, mükellefin yıllık gelirine artan oranlı bir tarife uygulanarak belirlenen ve kişiselleştirilen sübjektif bir vergidir",
        "D": "Vergi, mükellefin sahip olduğu toplam servetin büyüklüğüne göre değişen ve kişiselleştirilen bir servet vergisi niteliğindedir",
        "E": "Vergi, mükellefin mesleğine ve sosyal statüsüne göre farklılaştırılarak belirlenen ve kişiye özgü hesaplanan bir vergidir",
    },
    "mtv-gen-0047": {"A": "Yeni kayıt ve tescil edilen taşıtın vergisi, tescil hangi ayda yapılırsa yapılsın ancak bir sonraki takvim yılının Ocak ayında ödenmeye başlanır"},
    "mtv-gen-0048": {"C": "Taşıtı geçici olarak kullanan kişi, kullanım süresi boyunca taşıtın motorlu taşıtlar vergisinin mükellefi hâline gelir ve o dönemin vergisini öder"},
    "mtv-gen-0049": {"A": "Motorlu taşıtlar vergisi, satıcının alıcıya yansıttığı ve zincirin sonunda nihai tüketici üzerinde kalan dolaylı nitelikte bir vergidir; malik yük taşımaz"},

    # ↓ doğru EN KISA olsun
    "mtv-gen-0051": {
        "A": "İkisi de devlete ödenen ve aynı hukuki nitelikte olan zorunlu kamu yükümlülükleridir; aralarında amaç ve muhatap farkı bulunmaz",
        "C": "Motorlu taşıtlar vergisi sigorta şirketine, zorunlu trafik sigortası primi ise doğrudan vergi dairesine ödenir ve gelir kaydedilir",
        "D": "İkisi de sigorta şirketiyle yapılan bir sözleşmeden doğar; ikisi de vergi niteliği taşımayan özel hukuk borcudur",
        "E": "Motorlu taşıtlar vergisi üçüncü kişilerin zararını, zorunlu trafik sigortası ise devletin gelir ihtiyacını karşılamayı amaçlar",
    },
    "mtv-gen-0052": {"A": "Vergi her gün için ayrı ayrı hesaplandığından, dönem içinde el değiştiren taşıtın vergisi gün sayısına bölünerek maliklere paylaştırılır"},
    "mtv-gen-0053": {"A": "Vergi tutarları her yıl mükellefin taşıtı için beyan ettiği değere göre yeniden ve serbestçe belirlenir; kanundaki tarife bağlayıcı değildir"},
    "mtv-gen-0054": {"A": "Bir taşıt satın alınırken vergi ödenmişse, o taşıta sahip olunduğu süre boyunca ayrıca hiç motorlu taşıtlar vergisi doğmaz; iki vergi birbirinin yerine geçer"},
    "mtv-gen-0055": {"A": "Noter, taşıtın vergi borcunu hiç dikkate almadan satış ve devir işlemini her hâlde serbestçe gerçekleştirir; borç sorgulama yükümlülüğü bulunmaz"},
    # ⚠ Bu sorunun A, C ve D şıklarında dolgu kalıbı ("…zorundadır") ZATEN vardı —
    # bu turda ben eklemedim, orijinal yazımdan geliyordu. Doğru şık (E) taşımadığı
    # için kalıp bu soruda "yanlış" işareti oluyordu. Üçü de yeniden yazıldı.
    "mtv-gen-0056": {
        "A": "Mükellef, motorlu taşıtlar vergisi için her yıl ayrı bir beyanname verir ve ödeyeceği vergiyi tarifeye göre kendisi hesaplayıp bildirir",
        "C": "Mükellef, motorlu taşıtlar vergisini ayrı bir beyanname yerine yıllık gelir vergisi beyannamesi içinde ayrıca beyan eder",
        "D": "Mükellef, vergiyi tahakkuk ettirebilmek için her yıl taşıtın güncel değerini yeniden takdir ettirir ve idareye sunar",
    },

    # ↓ doğru EN KISA olsun
    "mtv-gen-0058": {
        "A": "Her ikisi de kişinin bir takvim yılı içinde elde ettiği kazanç ve iratlar üzerinden alınan dolaysız gelir vergileridir",
        "B": "Her ikisi de mal ve hizmet teslimleri üzerinden alınan ve nihai tüketiciye yansıyan harcama vergisi niteliğindedir",
        "C": "Her ikisi de yalnızca söz konusu malın alım satımı sırasında bir defaya mahsus alınan işlem vergisi niteliğindedir",
        "E": "Her ikisi de kişinin toplam malvarlığının tamamı üzerinden alınan genel nitelikli servet vergisi sayılmaktadır",
    },
    "mtv-gen-0059": {"A": "Taşıt bir dönem boyunca hiç kullanılmaz ve garajda bekletilirse o döneme ait motorlu taşıtlar vergisi kendiliğinden silinir; malikten vergi istenmez"},
    "mtv-gen-0060": {"A": "Motorlu taşıtlar vergisi, yalnızca taşıt ilk kez satın alınıp trafiğe tescil edildiğinde bir defaya mahsus ödenir; sonraki yıllar için mükellefiyet doğmaz"},
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

    # ★ NİYETİ DOĞRULA, yazdığımla yetinme. Bu ders üç kez ısırdı: kdv'de iki,
    # damga'da bir, mtv'de ON DÖRT soruda uzattığım çeldirici doğrunun ALTINDA
    # kaldı (0001'de 142 ↔ 143 — kıl payı). Göz kararı uzunluk yazmak işe yaramıyor.
    kalan = []
    for qid in YAMA:
        q = idx[qid]
        dogru = len(q["options"][q["answer"]])
        enuzun_celdirici = max(len(v) for k, v in q["options"].items() if k != q["answer"])
        if dogru >= enuzun_celdirici:
            kalan.append((qid, dogru, enuzun_celdirici))
    if kalan:
        print(f"⚠ {len(kalan)} soruda doğru şık HÂLÂ en uzun — uzatma yetmedi:")
        for qid, d, c in kalan:
            print(f"   {qid}: doğru {d} ↔ en uzun çeldirici {c}  (+{d - c + 1} karakter gerek)")

    json.dump(qs, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"yamalanan: {len(YAMA)} soru / {sum(len(v) for v in YAMA.values())} çeldirici "
          f"| hedefe ulaşan: {len(YAMA) - len(kalan)}/{len(YAMA)}")
