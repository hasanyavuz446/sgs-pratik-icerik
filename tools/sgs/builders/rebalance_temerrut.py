# -*- coding: utf-8 -*-
"""borclar_hukuku/temerrut_tazminat.json — şık boyu dengeleme (%80 → ≤%30).

Borçlar Hukuku'nun en kötü dosyası. 52 öncüllü-olmayan sorunun 46'sında doğru şık
EN UZUNDU (%88). Reçete Vergi Hukuku'nda 7 dosyada kanıtlandı:
çeldiriciler İÇERİKLE uzatılır, dolguyla değil; ~%20'sine kasten dokunulmaz.

Kasten DOKUNULMAYAN 9: 0004 · 0011 · 0015 · 0016 · 0030 · 0037 · 0043 · 0051 · 0060
(farkın zaten dar olduğu sorular — doğru şık orada en uzun kalsın ki dağılım
iki uca da yayılsın; emlak_vergisi'nde hepsini düzeltip "doğru hep ortada" diye
yeni bir ipucu üretmiştim).

Çeldiriciler TBK'nın gerçek kavram yanılgılarını temsil eder: müspet ↔ menfi zarar,
kusursuz ↔ kusurlu imkânsızlık, borçlu ↔ alacaklı temerrüdü, dönme ↔ fesih,
temerrüt faizi ↔ aşkın zarar.
"""
import json

P = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/borclar_hukuku/temerrut_tazminat.json"

YAMA = {
    "temerrut-gen-0001": {"E": "Borçlu yalnızca borca aykırılıkta kastı bulunuyorsa sorumlu olur; hafif veya ağır ihmal derecesindeki aykırılıklardan hiçbir biçimde sorumlu tutulamaz"},
    "temerrut-gen-0002": {"E": "Borçlunun kusuru karine sayılmaz; alacaklının zararı, illiyet bağını ve ayrıca borçlunun kusurlu olduğunu da kanıtlaması gerekir"},
    "temerrut-gen-0003": {"A": "Borçlu, ifada kullandığı yardımcı kişilerin verdiği zarardan hiçbir hâlde sorumlu değildir; sorumluluk yalnızca zararı doğuran yardımcıya aittir"},
    "temerrut-gen-0007": {"D": "Bu durumda alacaklı yalnızca sözleşme hiç yapılmasaydı bulunacağı durumu, yani menfi zararını isteyebilir; ifadan doğacak yararını talep edemez"},
    "temerrut-gen-0008": {"A": "Borçlunun imkânsızlığı bildirme ya da zararı artırmamak için önlem alma gibi bir yükümlülüğü yoktur; imkânsızlıkla borç kendiliğinden sona erer"},
    "temerrut-gen-0009": {"A": "Edimi imkânsızlaşan borçlu, karşı edimi istemeye devam eder; kendi edimini ifa etmemiş olsa da kararlaştırılan bedele tam olarak hak kazanır"},
    "temerrut-gen-0010": {"C": "Kısmi imkânsızlıkta borçlu, imkânsızlaşan kısmın parasal değerini her hâlde alacaklıya tazminat olarak öder; sözleşme aynen ayakta kalır"},
    "temerrut-gen-0012": {"A": "Kesin vade belirlenmiş olsa dahi borçlunun temerrüde düşmesi için alacaklının ayrıca ihtar çekmesi şarttır; vadenin geçmesi tek başına yetmez"},
    "temerrut-gen-0013": {"A": "Temerrüde düşen borçlu, beklenmedik hâlden doğan zarardan hiçbir hâlde sorumlu değildir; sorumluluğu yalnızca kendi kusuruyla sınırlı kalır ve genişlemez"},
    "temerrut-gen-0014": {"A": "Alacaklı temerrüt faizi isteyebilmek için, faiz tutarı kadar bir zarara fiilen uğradığını her hâlde ayrıca ispat etmek durumundadır"},
    "temerrut-gen-0020": {"D": "Alacaklı her üç hakkı da (aynen ifa, gecikme tazminatı ve sözleşmeden dönme) aynı anda birlikte kullanmak ve üçünü de tahsil etmek durumundadır"},
    "temerrut-gen-0021": {"C": "Sözleşmeden dönme, o güne kadar verilen edimlerin iadesini gerektirmez; her taraf kendisine verilmiş olanı mülkiyetinde tutmaya devam eder"},
    "temerrut-gen-0022": {"E": "Sürekli edimli sözleşmeler yalnızca hâkim kararıyla sona erdirilebilir; alacaklının tek taraflı beyanla fesih hakkı hiçbir hâlde bulunmaz"},
    "temerrut-gen-0023": {"B": "Alacaklının yalnızca sözleşmeyi kurmak için yaptığı masraflardan ve bu yüzden kaçırdığı diğer fırsatlardan doğan kayıplardan ibarettir"},
    "temerrut-gen-0024": {"D": "Borçlunun ifadan kaçınması sonucu alacaklının uğradığı ve kanun gereği iki katı olarak istenebilen cezai nitelikteki zarardır"},
    "temerrut-gen-0025": {"B": "Alacaklı hangi seçimlik hakkı kullanırsa kullansın yalnızca menfi zararını isteyebilir; müspet zarar hiçbir hâlde talep konusu yapılamaz"},
    "temerrut-gen-0027": {"D": "Alacaklı müspet zararını isteyebilmek için, borçlunun temerrütte kasıtlı davrandığını ayrıca ispat etmek durumundadır; ihmal yeterli olmaz"},
    "temerrut-gen-0028": {"A": "(A) sözleşmeden döndüğü için ödediği 100.000 TL'yi geri isteyemez; yalnızca ödediği tutar üzerinden gecikme faizi talep edebilir"},
    "temerrut-gen-0029": {"B": "Alacaklı, ancak borçluya yazılı bir bildirimde bulunup edimi kabul etmeyeceğini açıkça ihtar ederse temerrüde düşmüş sayılır"},
    "temerrut-gen-0034": {"E": "İkisi arasındaki tek fark faizdir; temerrütte faiz işler, imkânsızlıkta işlemez; bunun dışında hukuki sonuçları tümüyle aynıdır"},
    "temerrut-gen-0035": {"E": "Tazminatın belirlenmesinde haksız fiil hükümleri uygulanmaz; borca aykırılığın kendine özgü ve ayrı bir tazminat tarifesi bulunur"},
    "temerrut-gen-0036": {"A": "Alacaklı temerrüt faizi ile aşkın zararı hiçbir zaman birlikte isteyemez; ikisinden yalnızca birini seçmek ve ötekinden vazgeçmek durumundadır"},
    "temerrut-gen-0038": {"A": "Alacaklı yalnızca gerçekten uğradığı zarar kadar faiz isteyebilir; uğradığı zararı aşan faiz kısmını hiçbir biçimde talep edemez"},
    "temerrut-gen-0044": {"A": "(D), temerrüt faizi isteyebilmek için önce 50.000 TL kadar bir zarara uğradığını belgeyle ispat etmek durumundadır; aksi hâlde faiz istenemez"},
    "temerrut-gen-0045": {"A": "(F), teslim gerçekleşene kadar beklemek durumundadır; kesin vade geçmiş olsa bile ancak ihtar çekerek temerrüt oluşturabilir"},
    "temerrut-gen-0046": {"C": "(G) borcundan kurtulur; ancak aldığı bedeli, imkânsızlıkta kusuru bulunmadığı için (H)'ye iade etmek durumunda kalmaz ve elinde tutar"},
    "temerrut-gen-0047": {"D": "(K), imkânsızlaşan makineyi bir başka biçimde aynen ifa etmek üzere yeniden temin etmek ve alacaklıya teslim etmek durumundadır"},
    "temerrut-gen-0048": {"C": "(L)'nin teslim almaktan kaçınması borç ilişkisine hiçbir sonuç doğurmaz; temerrüt kurumu yalnızca borçlu bakımından söz konusu olur"},
    "temerrut-gen-0049": {"A": "(N), her hâlde yalnızca temerrüt faizini isteyebilir; faizi aşan finansman giderini hiçbir biçimde talep edemez ve bu zarara katlanır"},
    "temerrut-gen-0050": {"C": "(R) yalnızca sözleşmeden dönebilir; malın aynen ifasını isteme hakkını borçlunun temerrüde düşmesiyle birlikte kesin olarak yitirmiştir"},
    "temerrut-gen-0052": {"A": "Taraflar bu konuda serbestçe anlaşabildiğinden kayıt geçerlidir; borçlu ağır ihmaliyle verdiği zarardan da sorumlu tutulamaz hâle gelir"},
    "temerrut-gen-0053": {"A": "(U), zarar beklenmedik bir olaydan doğduğu için hiçbir hâlde sorumlu tutulamaz; temerrüde düşmüş olması bu sonucu değiştirmez"},
    "temerrut-gen-0054": {"C": "(V) ifadan vazgeçtiğinde yalnızca sözleşmeyi kurmak için yaptığı masrafları, yani menfi zararını isteyebilir; ifa menfaatini talep edemez"},
    "temerrut-gen-0055": {"C": "Borçlu, imkânsızlaşan bölümün parasal değerini (Z)'ye her hâlde tazminat olarak ödemek durumundadır; sözleşme aynen ayakta kalır"},
    "temerrut-gen-0056": {"D": "Kesin vade kararlaştırılmadığı için (A2) hiçbir biçimde temerrüde düşürülemez; (B2) yalnızca ifayı beklemek ve süreye katlanmak durumundadır"},
    "temerrut-gen-0057": {"B": "Dönmede sözleşme ileriye etkili, fesihte ise geçmişe etkili olarak sona erer; verilen edimlerin iadesi yalnızca fesih hâlinde istenebilir"},
    "temerrut-gen-0058": {"D": "Temerrütten sonra alacaklı yalnızca tazminat isteyebilir; aynen ifa talebinde bulunma hakkını temerrütle birlikte kesin olarak yitirir"},
}

# ── 2. tur: self-check 18 ıska bildirdi. Bu dosyada doğru şıklar uzun (130-164),
# çünkü TBK kavramları niteleme istiyor; uzatmalar da ona göre açıldı.
YAMA.update({
    "temerrut-gen-0008": {"A": "Borçlunun imkânsızlığı alacaklıya bildirme ya da zararı artırmamak için önlem alma gibi bir yükümlülüğü yoktur; imkânsızlıkla borç kendiliğinden ve tümüyle sona erer"},
    "temerrut-gen-0009": {"A": "Edimi imkânsızlaşan borçlu, karşı edimi istemeye devam eder; kendi edimini hiç ifa etmemiş olsa dahi sözleşmede kararlaştırılan bedelin tamamına hak kazanır"},
    "temerrut-gen-0013": {"A": "Temerrüde düşen borçlu, beklenmedik hâlden doğan zarardan hiçbir hâlde sorumlu değildir; sorumluluğu yalnızca kendi kusuruyla sınırlı kalır ve temerrütle genişlemez"},
    "temerrut-gen-0020": {"D": "Alacaklı her üç seçimlik hakkı da (aynen ifa, gecikme tazminatı ve sözleşmeden dönme) aynı anda birlikte kullanmak ve üçünü de tahsil etmek durumundadır"},
    "temerrut-gen-0023": {"B": "Alacaklının yalnızca sözleşmeyi kurmak için yaptığı masraflardan ve bu sözleşme yüzünden kaçırdığı diğer fırsatlardan doğan kayıplardan ibarettir"},
    "temerrut-gen-0028": {"A": "(A) sözleşmeden döndüğü için ödemiş olduğu 100.000 TL'yi geri isteyemez; yalnızca bu tutar üzerinden işleyen gecikme faizini talep edebilir"},
    "temerrut-gen-0029": {"B": "Alacaklı, ancak borçluya yazılı bir bildirimde bulunup kendisine sunulan edimi kabul etmeyeceğini açıkça ihtar ederse temerrüde düşmüş sayılır"},
    "temerrut-gen-0035": {"E": "Tazminatın belirlenmesinde haksız fiil hükümleri hiçbir biçimde uygulanmaz; borca aykırılığın kendine özgü ve bağımsız bir tazminat tarifesi bulunur"},
    "temerrut-gen-0038": {"A": "Alacaklı yalnızca gerçekten uğradığı zarar tutarı kadar faiz isteyebilir; uğradığı zararı aşan faiz kısmını hiçbir biçimde talep edemez"},
    "temerrut-gen-0045": {"A": "(F), teslim gerçekleşene kadar beklemek durumundadır; kesin vade geçmiş olsa bile ancak ayrıca ihtar çekerek borçluyu temerrüde düşürebilir"},
    "temerrut-gen-0047": {"D": "(K), imkânsızlaşan makineyi bir başka biçimde aynen ifa etmek üzere yeniden temin etmek ve sözleşmedeki süre içinde alacaklıya teslim etmek durumundadır"},
    "temerrut-gen-0048": {"C": "(L)'nin teslim almaktan kaçınması borç ilişkisine hiçbir sonuç doğurmaz; temerrüt kurumu yalnızca borçlu bakımından söz konusu olabilir"},
    "temerrut-gen-0049": {"A": "(N), her hâlde yalnızca temerrüt faizini isteyebilir; faizi aşan finansman giderini hiçbir biçimde talep edemez ve bu zarara kendisi katlanır"},
    "temerrut-gen-0050": {"C": "(R) yalnızca sözleşmeden dönme hakkını kullanabilir; malın aynen ifasını isteme hakkını borçlunun temerrüde düşmesiyle birlikte kesin olarak yitirmiştir"},
    "temerrut-gen-0052": {"A": "Taraflar sorumsuzluk konusunda serbestçe anlaşabildiğinden bu kayıt geçerlidir; borçlu ağır ihmaliyle verdiği zarardan da sorumlu tutulamaz hâle gelir"},
    "temerrut-gen-0053": {"A": "(U), zarar beklenmedik bir olaydan doğduğu için hiçbir hâlde sorumlu tutulamaz; temerrüde düşmüş olması onun sorumluluğunu genişletmez"},
    "temerrut-gen-0055": {"C": "Borçlu, imkânsızlaşan bölümün parasal karşılığını (Z)'ye her hâlde tazminat olarak ödemek durumundadır; sözleşme geri kalanıyla ayakta kalır"},
    "temerrut-gen-0058": {"D": "Temerrütten sonra alacaklı yalnızca tazminat isteyebilir; aynen ifa talebinde bulunma hakkını borçlunun temerrüdüyle birlikte kesin olarak yitirir"},
})

# ── 3. tur: kalan 8 ıska. Bu dosyanın doğru şıkları uzun (144-164) çünkü TBK
# kavramları koşul ve istisna taşıyor; uzatmalar da o kadar açıldı.
YAMA.update({
    "temerrut-gen-0009": {"A": "Edimi imkânsızlaşan borçlu, karşı edimi istemeye devam eder; kendi edimini hiç ifa etmemiş olsa dahi sözleşmede kararlaştırılan bedelin tamamına eksiksiz hak kazanır"},
    "temerrut-gen-0029": {"B": "Alacaklı, ancak borçluya yazılı bir bildirimde bulunup kendisine usulüne uygun sunulan edimi kabul etmeyeceğini açıkça ihtar ederse temerrüde düşmüş sayılır"},
    "temerrut-gen-0035": {"E": "Tazminatın belirlenmesinde haksız fiil hükümleri hiçbir biçimde uygulanmaz; borca aykırılığın kendine özgü, bağımsız ve ayrı bir tazminat tarifesi bulunur"},
    "temerrut-gen-0045": {"A": "(F), teslim fiilen gerçekleşene kadar beklemek durumundadır; kesin vade geçmiş olsa bile ancak ayrıca ihtar çekerek borçluyu temerrüde düşürebilir"},
    "temerrut-gen-0048": {"C": "(L)'nin teslim almaktan kaçınması borç ilişkisine hiçbir sonuç doğurmaz; temerrüt kurumu yalnızca borçlu bakımından söz konusu olabilen bir hâldir"},
    "temerrut-gen-0049": {"A": "(N), her hâlde yalnızca temerrüt faizini isteyebilir; faizi aşan finansman giderini hiçbir biçimde talep edemez ve doğan bu zarara kendisi katlanır"},
    "temerrut-gen-0052": {"A": "Taraflar sorumsuzluk konusunda serbestçe anlaşabildiğinden bu kayıt tümüyle geçerlidir; borçlu ağır ihmaliyle verdiği zarardan dahi sorumlu tutulamaz hâle gelir"},
    "temerrut-gen-0053": {"A": "(U), zarar beklenmedik bir olaydan doğduğu için hiçbir hâlde sorumlu tutulamaz; daha önce temerrüde düşmüş olması onun sorumluluk alanını genişletmez"},
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
          f"| kasten dokunulmayan: 9")
