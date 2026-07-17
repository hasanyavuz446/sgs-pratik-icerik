# -*- coding: utf-8 -*-
"""borclar_hukuku/haksiz_fiil.json — şık boyu dengeleme (%71 → ≤%30).

52 öncüllü-olmayan sorunun 42'sinde doğru şık EN UZUNDU (%82).

Kasten DOKUNULMAYAN 8: 0005 · 0018 · 0019 · 0028 · 0031 · 0037 · 0042 · 0060
(farkın zaten 1-3 karakter olduğu sorular — doğru şık orada en uzun kalsın ki
dağılım iki uca da yayılsın).

⚠ borclar_hukuku'nda İKİ kusur birlikte: boy + yükümlülük dili asimetrisi.
Burada asimetri zayıf (çeldiricide 8, doğruda 0) — temerrut'taki 30'a kıyasla
küçük; yine de uzatmalarda "zorunda/durumundadır" KULLANILMADI.

Çeldiriciler TBK m.49-76'nın gerçek kavram yanılgılarını temsil eder:
kusur ↔ kusursuz sorumluluk, maddi ↔ manevi zarar, adam çalıştıran ↔ hayvan
bulunduran ↔ yapı maliki, iki yıllık ↔ on yıllık zamanaşımı.
"""
import json

P = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/borclar_hukuku/haksiz_fiil.json"

YAMA = {
    "hakfiil-gen-0003": {"E": "Zarar veren ile zarar gören arasında haksız fiilden önce geçerli bir borç ilişkisinin kurulmuş olması"},
    "hakfiil-gen-0004": {"E": "Yalnızca kişinin malvarlığına yönelen ihlaller hukuka aykırı sayılır; yaşam, sağlık ve şeref gibi kişilik değerlerine yönelenler kapsam dışında kalır"},
    "hakfiil-gen-0007": {"A": "Maddi zarar yalnızca malvarlığında fiilen ortaya çıkan azalmayı kapsar; yoksun kalınan kazanç ile artması engellenen değerler zarar sayılmaz"},
    "hakfiil-gen-0010": {"A": "Zorunluluk hâlinde hareket eden kişi, verdiği zarardan hiçbir koşulda sorumlu tutulamaz; hâkimin hakkaniyete göre tazminata hükmetme yetkisi yoktur"},
    "hakfiil-gen-0012": {"D": "Zarar görenin rızası, kişinin yaşamı ve vücut bütünlüğü dâhil her türlü değer üzerinde sınırsızca geçerlidir; ahlaka aykırılık bu rızayı etkilemez"},
    "hakfiil-gen-0016": {"B": "Hâkim her durumda zararın tamamına hükmeder; kusurun ağırlığı ile zarar görenin durumu tazminat miktarını hiçbir biçimde etkilemez"},
    "hakfiil-gen-0017": {"E": "Zarar görenin kusuru hâlinde tazminat kanunen yarı yarıya azaltılır; hâkimin kusurun ağırlığına göre takdir yetkisi bulunmaz"},
    "hakfiil-gen-0020": {"C": "Destekten yoksun kalma tazminatı, ölenin sağlığında geride bıraktığı mirasın değerine göre hesaplanır; desteğin süresi ve ölçüsü aranmaz"},
    "hakfiil-gen-0021": {"B": "Bedensel zarara uğrayan kişi ancak çalışma gücünü tamamen yitirmişse tazminat isteyebilir; kısmi güç kayıpları ile ekonomik geleceğin sarsılması kapsam dışıdır"},
    "hakfiil-gen-0022": {"D": "Manevi tazminat yalnızca para ödenmesi biçiminde olabilir; kınama, özür veya kararın yayımlanması gibi başka bir giderim biçimi kabul edilmez"},
    "hakfiil-gen-0023": {"E": "Bu tazminatın miktarı, zarar görenin sosyal ve ekonomik durumuna bakılmaksızın kanunda maktu bir tutar olarak önceden belirlenmiştir"},
    "hakfiil-gen-0025": {"B": "Ayırt etme gücü bulunmayan kişi de tıpkı temyiz gücü olan kişi gibi verdiği zararın tamamından sorumludur; hakkaniyet indirimi uygulanmaz"},
    "hakfiil-gen-0026": {"E": "Adam çalıştıran yalnızca çalışanının kasten verdiği zararlardan sorumludur; çalışanın ihmaliyle doğan zararlarda sorumluluğu doğmaz"},
    "hakfiil-gen-0027": {"D": "Sorumluluktan kurtulmak için zararı üçüncü bir kişinin ağır kusurunun doğurduğunu ispat etmesi tek başına yeterlidir; özen gösterdiğini ayrıca kanıtlaması aranmaz"},
    "hakfiil-gen-0029": {"D": "Hayvan bulunduran yalnızca hayvanın maliki olduğu hâllerde sorumlu olur; hayvanı geçici olarak yanında bulunduran kişilerin sorumluluğu doğmaz"},
    "hakfiil-gen-0030": {"C": "Yapı eserinin verdiği zarardan yalnızca o eseri yapan yüklenici sorumludur; yapının maliki ile intifa hakkı sahibinin sorumluluğu bulunmaz"},
    "hakfiil-gen-0032": {"B": "İşletme sahibi ancak faaliyetin yürütülmesinde kendisinin kişisel bir kusuru bulunduğu ispat edilirse sorumlu olur; kusursuz sorumluluk söz konusu değildir"},
    "hakfiil-gen-0035": {"E": "Objektif özen sorumluluğu yalnızca sözleşmeden doğan borç ilişkilerinde söz konusu olur; haksız fiil alanında böyle bir ölçüt hiç uygulanmaz"},
    "hakfiil-gen-0038": {"D": "Fiilin işlendiği tarihten başlayan tek bir on yıllık süre söz konusudur; zararın ve failin öğrenildiği anın süreye herhangi bir etkisi bulunmaz"},
    "hakfiil-gen-0041": {"A": "Taraflar arasında sözleşme bulunduğu için zarar gören yalnızca sözleşmeye aykırılık hükümlerine dayanabilir; haksız fiil hükümleri hiçbir biçimde uygulanmaz"},
    "hakfiil-gen-0043": {"C": "Tazminatın hangi biçimde ve hangi ölçüde ödeneceğini yalnızca zarar veren belirler; hâkimin bu konuda bir takdir yetkisi bulunmaz"},
    "hakfiil-gen-0044": {"B": "Her iki sorumlulukta da kusursuzluğunu ispat yükü zarar verene aittir; ispat yükü bakımından ikisi tümüyle aynı kurala tabi olur"},
    "hakfiil-gen-0048": {"D": "(K) yalnızca köpeği ısırması için kasten kışkırttığı ispatlanırsa sorumlu olur; aksi hâlde hayvanı bulunduran sıfatıyla sorumluluğu doğmaz"},
    "hakfiil-gen-0049": {"D": "Bu zarardan yalnızca binanın vaktiyle yapımını üstlenen müteahhit sorumlu olur; binanın maliki ile intifa hakkı sahibinin sorumluluğu bulunmaz"},
    "hakfiil-gen-0050": {"A": "Ayırt etme gücü bulunmayan çocuk hiçbir koşulda sorumlu tutulamaz; hâkimin hakkaniyet gereği tazminata hükmetme yetkisi de bulunmaz"},
    "hakfiil-gen-0051": {"B": "Hangi taşın hangi hasarı verdiği belirlenemediğinden (S) hiçbirinden tazminat isteyemez; doğan zarar kendi üzerinde kalır ve giderilmez"},
    "hakfiil-gen-0052": {"A": "İki yıllık süre kazanın olduğu tarihte başladığından, zararı ve faili daha sonra öğrenmiş olsa bile istem zamanaşımına uğramış sayılır"},
    "hakfiil-gen-0053": {"B": "(V)'nin fiili hukuka aykırıdır; bu nedenle çitte doğan zararın tamamını kusuru oranında tazmin etmesi gerekir ve zorunluluk hâli sonucu değiştirmez"},
    "hakfiil-gen-0054": {"B": "(Z)'nin manevi tazminat isteyebilmesi ancak haberin aynı zamanda bir suç oluşturması ve failin ceza mahkemesince mahkûm edilmiş olması hâlinde mümkün olur"},
    "hakfiil-gen-0055": {"E": "İşletme yalnızca patlamadan zarar gören kendi çalışanlarına karşı sorumludur; çevredeki üçüncü kişilere karşı bir sorumluluğu doğmaz"},
    "hakfiil-gen-0056": {"B": "Yayanın kusuru yalnızca tazminattan bir miktar indirim yapılmasını sağlar; kusur ne kadar ağır olursa olsun sürücünün sorumluluğunu kaldırmaz"},
    "hakfiil-gen-0057": {"C": "Yangın bir kez çıktıktan sonra doğal olayla yayıldığından, doğan zarardan (A) dâhil hiç kimse sorumlu tutulamaz ve zarar giderilmez"},
    "hakfiil-gen-0058": {"D": "Zarar bir çalışanın eliyle doğduğu için sorumluluk doğrudan doğruya ve yalnızca zarar gören üçüncü kişinin üzerinde kalır; işveren sorumlu olmaz"},
    "hakfiil-gen-0059": {"B": "Fiilin üzerinden on yıl geçmediğinden istem zamanaşımına uğramaz; zararın öğrenilmesine bağlı iki yıllık sürenin burada bir önemi bulunmaz"},
}

# ── 2. tur: self-check 13 ıska bildirdi. Bu dosyanın doğru şıkları uzun
# (125-171); TBK m.49-76 kavramları koşul ve istisna taşıyor.
YAMA.update({
    "hakfiil-gen-0003": {"E": "Zarar veren ile zarar gören arasında haksız fiilden önce kurulmuş, geçerli ve hâlen ayakta duran bir sözleşmesel borç ilişkisinin bulunması"},
    "hakfiil-gen-0017": {"E": "Zarar görenin kendi kusuru bulunduğunda tazminat kanun gereği yarı yarıya azaltılır; hâkimin kusurun ağırlığına ve olayın koşullarına göre takdir yetkisi bulunmaz"},
    "hakfiil-gen-0020": {"C": "Destekten yoksun kalma tazminatı, ölenin sağlığında geride bıraktığı mirasın değerine göre hesaplanır; desteğin süresi, ölçüsü ve düzenliliği aranmaz"},
    "hakfiil-gen-0022": {"D": "Manevi tazminat yalnızca para ödenmesi biçiminde hükmedilebilir; kınama, özür veya kararın yayımlanması gibi paradan başka bir giderim biçimine hiçbir hâlde başvurulamaz"},
    "hakfiil-gen-0023": {"E": "Bu tazminatın miktarı, zarar görenin sosyal ve ekonomik durumu ile olayın ağırlığına bakılmaksızın kanunda maktu bir tutar olarak önceden belirlenmiştir"},
    "hakfiil-gen-0025": {"B": "Ayırt etme gücü bulunmayan kişi de tıpkı temyiz gücü yerinde olan kişi gibi verdiği zararın tamamından sorumludur; hakkaniyet gereği indirim yapılamaz"},
    "hakfiil-gen-0035": {"E": "Objektif özen sorumluluğu yalnızca sözleşmeden doğan borç ilişkilerinde söz konusu olur; haksız fiil alanında böyle bir ölçüt kabul edilmemiş ve hiç uygulanmamıştır"},
    "hakfiil-gen-0044": {"B": "Her iki sorumlulukta da kusursuz olduğunu ispat yükü zarar verene aittir; ispat yükünün dağılımı bakımından ikisi arasında hiçbir fark bulunmaz ve aynı kurala tabidirler"},
    "hakfiil-gen-0048": {"D": "(K) yalnızca köpeği ısırması için kasten kışkırttığı ispatlanırsa sorumlu olur; aksi hâlde hayvanı bulunduran sıfatıyla bir sorumluluğu doğmaz"},
    "hakfiil-gen-0050": {"A": "Ayırt etme gücü bulunmayan çocuk hiçbir koşulda sorumlu tutulamaz; hâkimin hakkaniyet gereği tazminata hükmetme yetkisi de bulunmamaktadır"},
    "hakfiil-gen-0052": {"A": "İki yıllık süre kazanın meydana geldiği tarihte işlemeye başladığından, zararı ve faili çok daha sonra öğrenmiş olsa bile istem zamanaşımına uğramış sayılır"},
    "hakfiil-gen-0053": {"B": "(V)'nin fiili hukuka aykırıdır; bu nedenle çitte doğan zararın tamamını kusuru oranında tazmin etmesi gerekir ve zorunluluk hâli bu sonucu değiştirmez"},
    "hakfiil-gen-0054": {"B": "(Z)'nin manevi tazminat isteyebilmesi ancak yayımlanan haberin aynı zamanda bir suç oluşturması ve failin ceza mahkemesince kesin olarak mahkûm edilmesi hâlinde mümkündür"},
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
