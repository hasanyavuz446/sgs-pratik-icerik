# -*- coding: utf-8 -*-
"""vergi_hukuku/amme_alacaklari.json — şık boyu dengeleme (kör öğrenci %83 → ≤%30).

53 öncüllü-olmayan sorunun 49'unda doğru şık EN UZUNDU (%89). Reçete kdv/damga/mtv
ile aynı: çeldiriciler İÇERİKLE uzatılır, dolguyla değil.

★ Builder NİYETİ DOĞRULAR (mtv'de eklendi): yamadan sonra doğru şık hâlâ en uzunsa
kaç karakter eksik olduğunu söyler. Göz kararı uzunluk yazmak üç dosyada da tutmadı.
"""
import json

P = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/vergi_hukuku/amme_alacaklari.json"

YAMA = {
    "amme-gen-0001": {"E": "Yalnızca yabancı devletlerin Türkiye'deki alacaklarının tahsili bu Kanun'a göre yapılır; Türk kamu idarelerinin alacakları özel hukuk hükümlerine tabidir"},
    "amme-gen-0002": {"D": "Asli amme alacağı yalnızca para cezalarını, fer'i amme alacağı ise vergi ve resimleri ifade eder; gecikme zammı ise hiçbir sınıfa girmez"},
    "amme-gen-0004": {"A": "Kanun yalnızca amme alacağının nasıl hesaplanacağını ve hangi oran üzerinden alınacağını düzenler; tahsil usulüne ilişkin bir hüküm içermez"},
    "amme-gen-0005": {"B": "Amme borçlusu yalnızca amme alacağını tahsil etmekle görevli tahsil dairesidir; alacağı ödemekle yükümlü kişiler bu kavrama girmez"},
    "amme-gen-0007": {"A": "İhtiyati haciz yalnızca alacak kesinleştikten ve vadesi geçtikten çok sonra uygulanabilir; kesinleşmemiş alacak için hiçbir tedbir alınamaz"},
    "amme-gen-0009": {"C": "Amme alacağının önceliği yalnızca borçlu gerçek kişi olduğunda geçerlidir; borçlu tüzel kişi ise alacak diğerleriyle eşit sırada kalır ve öncelik tanınmaz"},
    "amme-gen-0010": {"C": "İhtiyati tahakkuk, borçlunun mallarının satılarak paraya çevrilmesi ve elde edilen tutarın alacağa mahsup edilmesi işlemidir"},
    "amme-gen-0011": {"B": "Amme alacağından mirasçılar, mirası reddetmiş olsalar dahi kendi kişisel malvarlıklarıyla ve sınırsız biçimde sorumlu tutulur"},
    "amme-gen-0012": {"E": "Kanuni temsilciler yalnızca tüzel kişinin ortaklarına karşı sorumludur; amme alacağı bakımından hiçbir kişisel sorumlulukları doğmaz ve takip edilemezler"},
    "amme-gen-0013": {"D": "Ortaklar yalnızca kâr payı aldıkları dönemin borçlarından ve aldıkları kâr payı tutarıyla sınırlı olarak sorumludur; sermaye payı ölçüt alınmaz"},
    "amme-gen-0014": {"D": "Tasfiye memurları yalnızca kendi ücretlerini tahsil etmekle yükümlü olup amme alacağından hiçbir biçimde şahsen sorumlu tutulamaz"},
    "amme-gen-0016": {"A": "Amme borcu hiçbir hâlde ertelenemez ve taksitlendirilemez; borçlunun durumu ne olursa olsun borç vadesinde ve tamamen ödenir"},

    # ↓ doğru EN KISA olsun
    "amme-gen-0017": {
        "B": "Amme alacağı vadesinde ödenmese dahi hiçbir ek yük uygulanmaz; borçludan yalnızca asıl borç tutarı istenir",
        "C": "Gecikme zammı yalnızca özel kişiler arasındaki alacaklara uygulanan bir yaptırımdır; amme alacaklarında uygulanmaz",
        "D": "Gecikme zammı, borç ödenene kadar her gün asıl borcun iki katına çıkacak biçimde katlanarak uygulanır",
        "E": "Gecikme zammı yalnızca borçlunun bunu kabul etmesi ve yazılı olarak taahhüt etmesi hâlinde uygulanabilir",
    },
    "amme-gen-0018": {"B": "Mahsup yalnızca özel kişiler arasındaki alacaklarda mümkündür; amme alacaklarında borçlunun idareden alacağı olsa dahi mahsup uygulanmaz"},
    "amme-gen-0019": {"A": "Vadesinde ödenmeyen amme alacağı hiçbir biçimde cebren tahsil edilemez; idare yalnızca borçludan ödeme yapmasını rica edebilir ve bekler"},
    "amme-gen-0020": {"C": "Ödeme emri, borçlunun mallarının derhâl haczedilip satıldığını ve alacağın tahsil edildiğini gösteren bir tutanaktır"},
    "amme-gen-0022": {"A": "Borçlunun mal bildiriminde bulunma gibi bir yükümlülüğü yoktur; idare borçlunun tüm mallarını kendi imkânlarıyla araştırıp tespit eder"},
    "amme-gen-0023": {"A": "Haciz, borçlunun tüm mallarının borç miktarına bakılmaksızın tamamına el konulması ve derhâl satılması işlemidir"},

    # ↓ doğru EN KISA olsun
    "amme-gen-0024": {
        "B": "Borçlunun istisnasız tüm malları, geçimi için gerekli olanlar ve mesleki aletleri dâhil her hâlde haczedilir",
        "C": "Haczedilemeyecek mal diye bir kavram yoktur; borçlunun her malı borç için satılabilir ve paraya çevrilebilir",
        "D": "Yalnızca borçlunun gayrimenkulleri haczedilemez; taşınır mallarının tamamı istisnasız haczedilebilir",
        "E": "Haczedilemeyecek mallar kanunda sayılmamıştır; bunlar yalnızca borçlu talep ederse mahkemece belirlenir",
    },
    "amme-gen-0025": {"A": "Haczedilen mallar hiçbir biçimde satılamaz; borçlu ödeme yapana kadar tahsil dairesince muhafaza edilerek saklanır"},
    "amme-gen-0026": {"B": "Aciz hâli, borçlunun tüm mallarının satılıp borcun tamamının ödendiği ve takibin sona erdiği durumu ifade eder"},
    "amme-gen-0027": {"D": "Üçüncü kişilerdeki mallar ve alacaklar yalnızca özel hukuk mahkemesinden alınacak bir kararla haczedilebilir"},
    "amme-gen-0029": {"A": "Mal bildiriminde bulunmayan borçluya hiçbir yaptırım uygulanmaz; bildirimde bulunmama hâlinde borç kendiliğinden silinir"},
    "amme-gen-0030": {"A": "Amme alacağının tahsilinde herhangi bir zamanaşımı süresi öngörülmemiştir; alacak aradan kaç yıl geçerse geçsin her zaman istenebilir"},
    "amme-gen-0031": {"C": "Zamanaşımını kesen bir işlem yapıldığında süre tümüyle ortadan kalkar ve alacak bundan sonra süresiz olarak istenebilir hâle gelir"},
    "amme-gen-0033": {"A": "(B)'nin ödeme emrine karşı yapabileceği hiçbir şey yoktur; ödediğini ispatlasa bile borcu ikinci kez ödemek durumundadır"},
    "amme-gen-0034": {"A": "Borçlunun böyle bir durumda yapabileceği hiçbir şey yoktur; ekonomik durumu ne olursa olsun borç her hâlde vadesinde ödenir"},
    "amme-gen-0035": {"E": "Ortaklara yalnızca şirket müdürü sıfatını taşıyan ortak ise ve yalnızca müdürlük yaptığı dönemin borcu için başvurulabilir"},
    "amme-gen-0036": {"A": "Amme borçlusunun ölümüyle takip her hâlde durur ve alacak mirasçılardan hiçbir biçimde istenemez; borç kendiliğinden sona erer"},
    "amme-gen-0037": {"A": "Kanun yalnızca tahsilden sonra uygulanan tedbirlerle alacağı korur; tahsilden önce alınabilecek hiçbir koruma tedbiri öngörülmemiştir"},

    # ↓ doğru EN KISA olsun
    "amme-gen-0040": {
        "B": "Tahsil dairesi, yalnızca özel hukuk alacaklarını tahsil etmekle görevli icra dairesini ifade eder",
        "C": "Tahsil dairesi, amme borçlusunun kendisidir; alacağı takip eden idare bu kavrama girmez",
        "D": "Tahsil dairesi yalnızca mahkemelerdir; idari birimler tahsil dairesi sayılmamaktadır",
        "E": "Tahsil dairesi, borçlunun alacaklı olduğu üçüncü kişileri ifade eden bir kavramdır",
    },
    "amme-gen-0041": {"C": "Teminat olarak yalnızca yabancı ülke parası ve altın kabul edilir; Türk lirası ve yerli değerler teminat olarak gösterilemez"},
    "amme-gen-0042": {"B": "Kefil gösterilmesi hâlinde borçlunun kendisi borçtan tümüyle kurtulur; bundan sonra yalnızca kefil takip edilir ve sorumlu olur"},
    "amme-gen-0043": {"A": "Borçlunun tüm tasarrufları geçerlidir; malvarlığını azaltsa ve alacağı tehlikeye düşürse dahi hiçbir tasarruf iptal edilemez"},
    "amme-gen-0044": {"A": "Amme alacağı hiçbir hâlde terkin edilemez; borçlunun durumu ne olursa olsun her koşulda tahsil edilir ve silinmez"},

    # ↓ doğru EN KISA olsun
    "amme-gen-0045": {
        "A": "Tahsil zamanaşımı hiçbir hâlde durmaz; borçlunun durumu ne olursa olsun süre kesintisiz işlemeye devam eder",
        "B": "Zamanaşımı yalnızca borçlunun rızası ve yazılı talebi üzerine durdurulabilir; kanuni bir durma hâli yoktur",
        "C": "Zamanaşımı durduğunda alacak kendiliğinden silinir; durma süresi sonunda takip yapılamaz hâle gelir",
        "D": "Zamanaşımı yalnızca amme alacaklısı idarenin talebiyle ve mahkeme kararı alınmasıyla durdurulabilir",
    },
    "amme-gen-0046": {"B": "Amme alacaklısı idare, yalnızca özel hukuk mahkemesinde dava açarak ve ilam alarak alacağını tahsil edebilir; iflas yolu kapalıdır"},
    "amme-gen-0047": {"B": "Satıştan elde edilen para, alacak miktarına ve sırasına bakılmaksızın bütün alacaklılara eşit paylarla dağıtılır"},
    "amme-gen-0049": {"A": "İdare bu bağışlara hiçbir biçimde müdahale edemez; borçlunun malvarlığını azaltan tasarrufları her hâlde geçerli sayılır"},
    "amme-gen-0050": {"A": "Beş yıl geçse dahi amme alacağı hiçbir hâlde zamanaşımına uğramaz; alacak aradan ne kadar süre geçerse geçsin tahsil edilebilir"},

    # ↓ doğru EN KISA olsun
    "amme-gen-0051": {
        "A": "İhtiyati hacze karşı borçlunun hiçbir dava açma veya itiraz etme hakkı bulunmamaktadır",
        "B": "İhtiyati hacze karşı yalnızca hakkı zarar gören üçüncü kişiler dava açabilir; borçlunun hakkı yoktur",
        "C": "İhtiyati hacze karşı ancak borcun tamamı ödendikten sonra ve iade istemiyle dava açılabilir",
        "D": "İhtiyati hacze itiraz yalnızca amme alacaklısı idarenin izin vermesi hâlinde mümkün olabilir",
    },
    "amme-gen-0052": {"C": "Takas yalnızca özel kişiler arasındaki borçlarda mümkündür; amme borcunda borçlunun idareden alacağı olsa bile takas yapılamaz"},
    "amme-gen-0053": {"A": "Tecil şartlarına uyulmasa da tecil aynen devam eder; şartların ihlali hiçbir hukuki sonuç doğurmaz ve takip başlamaz"},
    "amme-gen-0054": {"B": "Borçlunun yalnızca gayrimenkulleri haczedilebilir; taşınır malları ve banka hesapları hiçbir hâlde haczedilemez"},
    "amme-gen-0056": {"A": "Ödeme emri tebliğ edilen borçluya borcunu ödemesi için hiçbir süre tanınmaz; tebliğle birlikte malları derhâl haczedilip satılır"},
    "amme-gen-0057": {"A": "Amme alacağı da özel hukuk alacakları gibi ancak mahkemede dava açılıp ilam alındıktan sonra icra dairesince tahsil edilebilir; idarenin doğrudan takip yetkisi yoktur"},
    "amme-gen-0058": {"A": "Borçlunun bankadaki mevduatı hiçbir hâlde haczedilemez; banka hesapları haciz dışında tutulmuş bulunan değerlerdendir"},
    "amme-gen-0059": {"D": "Ödeme karşılığında makbuz verilmez; ödeme yalnızca banka dekontuyla ve yalnızca bir yıllık süre için ispatlanabilir"},
    "amme-gen-0060": {"D": "Ödenen tutarın hangi borca mahsup edileceğini yalnızca borçlu belirler; kanunda öngörülmüş bağlayıcı bir mahsup sırası bulunmaz"},
}

# ── 2. tur: builder'ın kendi denetimi 22 sorunun hedefi tutturamadığını söyledi ──
YAMA.update({
    "amme-gen-0012": {"E": "Kanuni temsilciler yalnızca tüzel kişinin ortaklarına ve alacaklılarına karşı sorumludur; amme alacağı bakımından hiçbir kişisel sorumlulukları doğmaz ve takip edilemezler"},
    "amme-gen-0014": {"D": "Tasfiye memurları yalnızca kendi ücretlerini ve masraflarını tahsil etmekle yükümlü olup amme alacağından hiçbir biçimde şahsen sorumlu tutulamaz"},
    "amme-gen-0016": {"A": "Amme borcu hiçbir hâlde ertelenemez ve taksitlendirilemez; borçlunun ekonomik durumu ne olursa olsun borç vadesinde ve tamamen ödenir"},
    "amme-gen-0017": {"D": "Gecikme zammı, borç ödenene kadar her gün asıl borcun iki katına çıkacak biçimde ve sınırsız olarak katlanarak uygulanır"},
    "amme-gen-0019": {"A": "Vadesinde ödenmeyen amme alacağı hiçbir biçimde cebren tahsil edilemez; idare yalnızca borçludan ödeme yapmasını yazıyla rica edebilir ve bekler"},
    "amme-gen-0023": {"A": "Haciz, borçlunun tüm mallarının borç miktarına bakılmaksızın tamamına el konulması ve bunların derhâl satılıp paraya çevrilmesi işlemidir"},
    "amme-gen-0025": {"A": "Haczedilen mallar hiçbir biçimde satılamaz; borçlu ödeme yapana kadar tahsil dairesince muhafaza edilerek saklanır ve sonra iade edilir"},
    "amme-gen-0027": {"D": "Üçüncü kişilerdeki mallar ve alacaklar yalnızca özel hukuk mahkemesinden alınacak bir kararla ve icra yoluyla haczedilebilir"},
    "amme-gen-0033": {"A": "(B) ödeme emrine karşı hiçbir yola başvuramaz; borcu ödediğini belgeyle ispatlasa bile aynı borcu ikinci kez ödemekle yükümlü kalır"},
    "amme-gen-0034": {"A": "Borçlunun böyle bir durumda başvurabileceği hiçbir yol yoktur; ekonomik durumu ne olursa olsun borç her hâlde vadesinde ve peşin ödenir"},
    "amme-gen-0036": {"A": "Amme borçlusunun ölümüyle takip her hâlde durur ve alacak mirasçılardan hiçbir biçimde istenemez; borç ölümle kendiliğinden sona erer"},
    "amme-gen-0040": {"B": "Tahsil dairesi, yalnızca özel hukuk alacaklarını tahsil etmekle görevli olan icra ve iflas dairesini ifade eder"},
    "amme-gen-0042": {"B": "Kefil gösterilmesi hâlinde borçlunun kendisi borçtan tümüyle kurtulur; bundan sonra alacak yalnızca kefilden takip edilir ve tahsil edilir"},
    "amme-gen-0043": {"A": "Borçlunun bütün tasarrufları geçerlidir; malvarlığını azaltsa ve amme alacağını tehlikeye düşürse dahi hiçbir tasarruf iptal edilemez"},
    "amme-gen-0045": {"A": "Tahsil zamanaşımı hiçbir hâlde durmaz; borçlunun durumu ne olursa olsun süre kesintisiz olarak işlemeye devam eder"},
    "amme-gen-0046": {"B": "Amme alacaklısı idare, yalnızca özel hukuk mahkemesinde dava açıp ilam alarak alacağını tahsil edebilir; iflas yoluyla takip yolu kapalıdır"},
    "amme-gen-0047": {"B": "Satıştan elde edilen para, alacak miktarına ve kanuni sıraya bakılmaksızın bütün alacaklılara eşit paylarla bölüştürülerek dağıtılır"},
    "amme-gen-0049": {"A": "İdare bu bağışlara hiçbir biçimde müdahale edemez; borçlunun malvarlığını azaltan tasarrufları alacağı tehlikeye düşürse de geçerli sayılır"},
    "amme-gen-0050": {"A": "Beş yıl geçse dahi amme alacağı hiçbir hâlde zamanaşımına uğramaz; aradan ne kadar süre geçerse geçsin alacak tahsil edilebilir durumdadır"},
    "amme-gen-0051": {"B": "İhtiyati hacze karşı yalnızca hakkı zarar gören üçüncü kişiler dava açabilir; borçlunun kendisine böyle bir hak tanınmamıştır"},
    "amme-gen-0054": {"B": "Borçlunun yalnızca gayrimenkulleri haczedilebilir; taşınır malları, banka hesapları ve üçüncü kişilerdeki alacakları haciz dışındadır"},
    "amme-gen-0059": {"D": "Ödeme karşılığında makbuz verilmez; yapılan ödeme yalnızca banka dekontuyla ve yalnızca bir yıllık süre boyunca ispatlanabilir"},
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
    print(f"yamalanan: {len(YAMA)} soru / {sum(len(v) for v in YAMA.values())} çeldirici "
          f"| hedefe ulaşan: {len(YAMA) - len(kalan)}/{len(YAMA)}")
