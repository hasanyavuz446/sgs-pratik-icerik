# -*- coding: utf-8 -*-
"""vergi_hukuku/damga_vergisi.json — şık boyu dengeleme (kör öğrenci %88 → hedef ≤%30).

53 öncüllü-olmayan sorunun 51'inde doğru şık EN UZUNDU (%96). Reçete kdv.json ile
aynı: çeldiriciler İÇERİKLE uzatılır, dolguyla değil; her uzatma o çeldiricinin
temsil ettiği yanlış kavramın kendi içinde tutarlı açılımıdır.

⚠ Bu dosyada şıklar kdv'ye göre KISA (35–121 karakter). Uzatmalar orantılı tutuldu;
kdv'deki 150 karakterlik cümleleri buraya taşımak kökle uyumsuz, yapay durur.

★ Yön çeşitliliği: bir kısmında dört çeldirici birden uzatılıp doğru şık EN KISA'ya
indirilir. Hepsinde tek yönde çalışmak "doğru hep ortada" ipucu üretir.
"""
import json

P = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/vergi_hukuku/damga_vergisi.json"

YAMA = {
    # doğru C=70 → A doğruyu geçsin
    "damga-gen-0001": {
        "A": "Kişilerin bir takvim yılı içinde elde ettiği kazanç ve iratlar damga vergisine tabidir",
    },
    # doğru B=88 → doğru EN KISA olsun (dördü de geçsin)
    "damga-gen-0002": {
        "A": "Yalnızca resmî daireler tarafından bastırılan matbu evrak; özel kişilerin düzenlediği kâğıtlar kapsam dışıdır",
        "C": "Yalnızca üzerinde belli bir para tutarı yazılı olan ticari senetler; tutar içermeyen kâğıtlar kapsam dışında kalır",
        "D": "Yalnızca noter huzurunda düzenlenen resmî senetler; adi yazılı belgeler kâğıt sayılmaz ve vergiye tabi olmaz",
        "E": "Yalnızca elle yazılmış ve imza taşımayan özel notlar; imzalı ve basılı belgeler bu kapsama girmez",
    },
    # doğru B=99 → D doğruyu geçsin
    "damga-gen-0003": {
        "D": "Damga vergisi, mal ve hizmet tüketimi üzerinden alınan bir harcama vergisidir; her teslimde matrah üzerinden hesaplanır",
    },
    # doğru C=66 → doğru EN KISA olsun
    "damga-gen-0004": {
        "A": "Henüz imzalanmamış, taslak hâlinde bulunan ve taraflarca kabul edilmemiş bir metin",
        "B": "Kişinin kendi kendine tuttuğu, kimseye ibraz edilmeyen ve hüküm doğurmayan özel notlar",
        "D": "Bir malın fiziki tesliminin kendisi; teslime ilişkin hiçbir belge düzenlenmemiş olması",
        "E": "Sözlü olarak yapılan, hiçbir belgeye bağlanmayan ve ispatı tanıkla sağlanan anlaşma",
    },
    # doğru B=107 → A ve C doğruyu geçsin
    "damga-gen-0006": {
        "A": "Elektronik ortamdaki belgeler hiçbir hâlde damga vergisine tabi değildir; vergi yalnızca fiziki kâğıtta doğar",
        "C": "Yalnızca kâğıda basılıp ıslak imza atılan belgeler damga vergisine tabidir; elektronik imza vergiyi doğurmaz",
    },
    # doğru D=89 → A ve B doğruyu geçsin
    "damga-gen-0008": {
        "A": "Resmî dairelerle kişiler arasındaki kâğıtların vergisini her hâlde resmî daire öder; kişinin bir yükümlülüğü doğmaz",
        "B": "Resmî dairelerle kişiler arasında düzenlenen kâğıtlar her hâlde damga vergisinden istisnadır; taraflardan vergi aranmaz",
    },
    # doğru A=74 → doğru EN KISA olsun
    "damga-gen-0009": {
        "B": "Yalnızca özel hukuk hükümlerine göre kurulan şirketler resmî daire sayılır",
        "C": "Yalnızca bankalar ve finans kuruluşları resmî daire kapsamında değerlendirilir",
        "D": "Sermaye şirketleri, kamu payı bulunmasa bile her hâlde resmî daire sayılır",
        "E": "Resmî daire kavramı yalnızca mahkemeleri ve yargı organlarını kapsar",
    },
    # doğru E=98 → B doğruyu geçsin
    "damga-gen-0010": {
        "B": "Vergisi ödenmemiş kâğıttan yalnızca onu ilk düzenleyen resmî daire sorumludur; imzalayan kişilere gidilemez",
    },
    # doğru A=111 → B doğruyu geçsin
    "damga-gen-0011": {
        "B": "Damga vergisi yalnızca maktu, yani her kâğıt için sabit tutar olarak alınır; nispi vergi uygulaması bulunmaz",
    },
    # doğru B=75 → doğru EN KISA olsun
    "damga-gen-0012": {
        "A": "Nispi vergide matrah, kâğıdı imzalayan kişi sayısıdır; kâğıtta yazılı tutar dikkate alınmaz",
        "C": "Nispi vergide matrah, kâğıdın düzenlendiği tarihteki yeniden değerleme oranıdır",
        "D": "Nispi vergide matrah, kâğıdın sayfa ve nüsha sayısının çarpımıyla bulunur",
        "E": "Nispi vergide matrah, mükellefin o yılki beyan ettiği toplam geliridir",
    },
    # doğru A=121 → D doğruyu geçsin
    "damga-gen-0013": {
        "D": "Kâğıtta para tutarını göstermek tümüyle tarafların isteğine bırakılmıştır; gösterilse de gösterilmese de vergiyi etkilemez",
    },
    # doğru B=82 → A ve C doğruyu geçsin
    "damga-gen-0014": {
        "A": "Kâğıttaki her imza için ayrı ayrı damga vergisi alınır; imza sayısı arttıkça vergi katlanarak artar",
        "C": "İmza sayısı ikiden fazlaysa damga vergisi iki katına çıkar; ikiye kadar olan imzalarda tek vergi alınır",
    },
    # doğru D=103 → C doğruyu geçsin
    "damga-gen-0015": {
        "C": "Yalnızca en son düzenlenen nüsha için vergi alınır; önceki nüshalar için ödenen tutar mükellefe iade edilir",
    },
    # doğru D=76 → doğru EN KISA olsun
    "damga-gen-0016": {
        "A": "Her işlem için ayrı ayrı vergi hesaplanır ve bulunan tutarlar toplanarak tahsil edilir",
        "B": "Birden fazla işlem içeren kâğıt, karmaşıklığı nedeniyle damga vergisinden istisna tutulur",
        "C": "Vergi, kâğıttaki en düşük vergiyi gerektiren işlem üzerinden hesaplanarak alınır",
        "E": "Vergi, kâğıttaki toplam tutarın işlem sayısına bölünmesiyle bulunan ortalamadan alınır",
    },
    # doğru E=90 → A doğruyu geçsin
    "damga-gen-0017": {
        "A": "Kâğıtta birbirinden bağımsız işlemler bulunsa da vergi yalnızca tek bir işlem üzerinden alınır",
    },
    # doğru E=83 → A doğruyu geçsin
    "damga-gen-0018": {
        "A": "Kefalet ve rehin, asıl işlemden ayrı sayılarak her hâlde ek bir damga vergisine tabi tutulur",
    },
    # doğru B=83 → A doğruyu geçsin
    "damga-gen-0021": {
        "A": "Kişiler arasında düzenlenen ve belli bir para tutarı içeren ticari nitelikteki sözleşmeler",
    },

    # ── 2. tur ──────────────────────────────────────────────────────────────
    # ⚠ 0011'de ilk turda B'yi 108'e çıkardım ama doğru 111'di — ölçmesem kaçardı.
    "damga-gen-0011": {
        "C": "Damga vergisi yalnızca nispi, yani kâğıtta yazılı tutarın binde oranı olarak alınır; maktu vergi uygulaması bulunmaz",
    },
    "damga-gen-0022": {"B": "Aynı işlem için düzenlenen her belge, sayısına bakılmaksızın sınırsız biçimde ayrı ayrı vergilendirilir ve vergiler toplanır"},
    "damga-gen-0024": {"A": "Vergiyi doğuran olay, kâğıdın konusunu oluşturan malın alıcıya fiilen teslim edilmesidir; kâğıdın imzalanması yeterli değildir"},

    # ↓ doğru EN KISA olsun
    "damga-gen-0025": {
        "A": "Damga vergisi yalnızca kâğıda pul yapıştırılarak ödenir; makbuz karşılığı veya istihkaktan kesinti yoluyla ödeme yapılamaz",
        "B": "Damga vergisi yalnızca takvim yılı sonunda verilen tek bir beyanname ile toplu olarak ödenir; aylık beyan söz konusu değildir",
        "C": "Damga vergisi yalnızca gayrimenkul satışlarında ve tapu müdürlüğüne yapılan ödemeyle tahsil edilir; diğer kâğıtlarda alınmaz",
        "E": "Damga vergisi hiçbir hâlde nakden ödenemez; ödeme yalnızca pul veya damga kullanılarak gerçekleştirilebilir",
    },
    "damga-gen-0026": {"D": "Ücret bordrolarından doğan damga vergisi yalnızca işçinin kendisi tarafından yıllık beyanname verilerek ödenir; işverenin sorumluluğu bulunmaz"},
    "damga-gen-0027": {"D": "Kira sözleşmesinden damga vergisi yalnızca kiralanan taşınmaz üçüncü bir kişiye satılırsa ve sözleşme devredilirse alınır"},

    # ↓ doğru EN KISA olsun
    "damga-gen-0028": {
        "A": "Taslak hâlindeki metinler de, taraflarca imzalanmamış olsalar bile düzenlendikleri anda damga vergisine tabi olur",
        "B": "İmza, kâğıdın vergilendirilmesinde hiçbir rol oynamaz; vergi kâğıdın yalnızca yazılı hâle gelmesiyle doğar",
        "D": "Sözlü olarak yapılan anlaşmalar da taraflar arasında hüküm doğurduğundan damga vergisine tabi tutulur",
        "E": "Kâğıt imzalanmasa bile tarafların anlaşma yönündeki niyeti tek başına vergiyi doğurmaya yeter",
    },
    "damga-gen-0029": {"A": "Bu kâğıdın damga vergisini, işleme taraf olan resmî daire kendi bütçesinden öder; kişiden vergi aranmaz"},
    "damga-gen-0030": {"A": "Damga vergisi, mükellefin ailevi ve kişisel durumu göz önüne alınarak belirlenen şahsi nitelikte bir vergidir"},
    "damga-gen-0031": {"C": "Kâğıtta yazılı para tutarı yalnızca gelir vergisi matrahını etkiler; damga vergisinin hesabıyla hiçbir ilgisi bulunmaz"},
    "damga-gen-0032": {"B": "Bu sözleşmeden yalnızca maktu ve çok düşük tutarlı bir vergi alınır; sözleşmede yazılı bedelin büyüklüğü sonucu değiştirmez"},

    # ↓ doğru EN KISA olsun
    "damga-gen-0033": {
        "A": "Her iki nüsha için de ayrı ayrı tam damga vergisi hesaplanır ve iki tutar toplanarak tahsil edilir",
        "B": "İki nüsha düzenlendiği için kâğıt mükerrer vergilemeye girmemek adına tümüyle vergiden istisna tutulur",
        "C": "Yalnızca alıcıda kalan nüsha vergiye tabidir; satıcıdaki nüsha için hiçbir vergi doğmaz ve aranmaz",
        "E": "İki nüsha düzenlenmesi nedeniyle her nüshaya düşen vergi yarı yarıya azaltılarak hesaplanır",
    },
    "damga-gen-0034": {"A": "Satış ve kefalet ayrı işlemler sayılarak her biri için tam vergi hesaplanır ve bulunan tutarlar toplanır"},

    # ↓ doğru EN KISA olsun
    "damga-gen-0035": {
        "B": "İkisi de mal ve hizmet teslimleri üzerinden alınan, matrahı ve konusu bakımından özdeş vergilerdir",
        "C": "Damga vergisi mal teslimlerinden, katma değer vergisi ise düzenlenen kâğıtlardan alınır",
        "D": "İkisi de kişilerin geliri üzerinden alınan ve yansıtılamayan dolaysız nitelikte vergilerdir",
        "E": "Damga vergisi bir servet vergisi, katma değer vergisi ise bir gelir vergisi niteliğindedir",
    },
    "damga-gen-0036": {"D": "Belli para içermeyen kâğıtlar için vergi, mükellefin o yılki beyan ettiği geliriyle orantılı olarak hesaplanır"},
    "damga-gen-0038": {"B": "Noterde düzenlenen kâğıtlar resmî nitelik kazandığından her hâlde damga vergisinden istisna tutulur"},
    "damga-gen-0039": {"B": "Aynı işlem için düzenlenen belge sayısı vergiyi hiç etkilemez; belge kaç olursa olsun vergi hiç alınmaz"},
    "damga-gen-0040": {"A": "Yabancı ülkede düzenlenen kâğıtlar, Türkiye'de resmî daireye ibraz edilse veya hüküm ifade etse bile vergiye tabi olmaz"},
    "damga-gen-0041": {"B": "Kefalet ayrı bir kâğıtta düzenlense bile asıl sözleşmenin vergisi hiç değişmez; kefalet kâğıdı vergi dışında kalır"},
    "damga-gen-0042": {"C": "Damga vergisi yalnızca kâğıdı ilk imzalayan kişiden alınır; sonradan imza atanların bir sorumluluğu doğmaz"},
    "damga-gen-0043": {"D": "Katma değer vergisi ve damga vergisi her zaman aynı matrah üzerinden hesaplanıp tek bir vergi olarak birlikte tahsil edilir"},

    # ↓ doğru EN KISA olsun
    "damga-gen-0045": {
        "A": "Damga vergisi, geliri belediyelere ait olan ve belediyelerce tarh edilen bir mahalli idare vergisidir",
        "C": "Damga vergisi, geliri köy tüzel kişiliğine bırakılan ve muhtarlıkça toplanan bir vergidir",
        "D": "Damga vergisinin geliri yalnızca il özel idarelerine aittir; genel bütçeye bir aktarım yapılmaz",
        "E": "Damga vergisi hiçbir kamu idaresine gelir sağlamaz; yalnızca kâğıtların hukuki geçerliliğini sağlar",
    },
    "damga-gen-0046": {"C": "Zeyilname yalnızca asıl sözleşmeyi tümüyle iptal ettiği hâllerde vergilendirilir; tutar artıran ekler vergi dışıdır"},
    "damga-gen-0047": {"A": "Kâğıttaki işlem yerine getirilmezse doğmuş olan damga vergisi her hâlde mükellefe geri verilir ve iade edilir"},

    # ↓ doğru EN KISA olsun
    "damga-gen-0048": {
        "B": "Maaş bordrosundan damga vergisi alınmaz; ücret ödemeleri kâğıt sayılmadığından tümüyle vergi dışında kalır",
        "C": "Maaş bordrosunun damga vergisini, ücreti alan memur yıl sonunda beyanname vererek kendisi öder",
        "D": "Maaş bordrosu yalnızca özel sektörde damga vergisine tabidir; kamu kurumlarının bordroları istisnadır",
        "E": "Maaş bordrosundan damga vergisi değil, ödenen ücret üzerinden yalnızca katma değer vergisi alınır",
    },
    "damga-gen-0050": {"A": "Asıl işlemin yanında yer alan kefalet ve rehin gibi fer'i işlemlerden her zaman ayrıca ve tam olarak vergi alınır"},

    # ↓ doğru EN KISA olsun
    "damga-gen-0051": {
        "A": "Resmî daire taraf olduğunda kâğıdın vergisini tümüyle resmî daire kendi bütçesinden karşılar",
        "B": "Resmî daire taraf olduğunda düzenlenen kâğıt niteliği gereği damga vergisinden istisna sayılır",
        "D": "Vergiyi resmî daire ile karşı taraftaki kişi eşit paylarla bölüşerek öder ve ayrı ayrı öderler",
        "E": "Resmî daire taraf olduğunda kâğıdın resmî niteliği nedeniyle vergi iki katına çıkarılarak alınır",
    },
    "damga-gen-0052": {"B": "Sözlü olarak yapılan işlem, tarafların anlaşma niyeti nedeniyle yazılı bir kâğıt gibi kabul edilerek vergilendirilir"},
    "damga-gen-0053": {"B": "Nispi damga vergisinde herhangi bir üst sınır bulunmaz; kâğıttaki tutar büyüdükçe vergi sınırsız biçimde artar"},
    "damga-gen-0054": {"E": "İhale kararlarından damga vergisi yalnızca ihale sonrası sözleşme imzalanırsa alınır; kararın kendisi vergi doğurmaz"},
    "damga-gen-0055": {"A": "Vergisi ödenmemiş kâğıt için hiçbir ceza uygulanmaz; kâğıt geçersiz sayılır ve taraflardan vergi aranmaz"},
    "damga-gen-0056": {"B": "Damga vergisi ayrı bir beyanname ile değil, yalnızca yıllık gelir vergisi beyannamesinin bir satırında beyan edilir"},
    "damga-gen-0057": {"B": "Alınan her fotokopi ve suret için, asıl kâğıtla aynı tutarda tam nispi damga vergisi ayrıca hesaplanır"},
    "damga-gen-0058": {"D": "Damga vergisi hiçbir kurum tarafından idare edilmez; mükellefler vergiyi kendiliğinden hesaplayıp öder"},
    "damga-gen-0060": {"B": "Kâğıtta yapılan her tadil, kâğıdın tamamı için baştan yeniden tam vergi hesaplanmasını gerektirir"},
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
    json.dump(qs, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"yamalanan: {len(YAMA)} soru / {sum(len(v) for v in YAMA.values())} çeldirici")
