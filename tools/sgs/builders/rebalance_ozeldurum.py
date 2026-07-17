# -*- coding: utf-8 -*-
"""borclar_hukuku/ozel_durumlar.json — şık boyu dengeleme (%71 → ≤%30).

52 öncüllü-olmayan sorunun 42'sinde doğru şık EN UZUNDU.

⚠ İKİ kusur birlikte (temerrut_tazminat'taki gibi): boy + yükümlülük dili
asimetrisi (çeldiricide 16, doğruda 0). Bu builder BOYU düzeltir; ifade
çeşitlendirmesi ardından ayrı geçişte yapılır.

Kasten DOKUNULMAYAN 8: 0008 · 0016 · 0022 · 0023 · 0029 · 0033 · 0035 · 0057
(farkın zaten 1-3 karakter olduğu sorular).

Çeldiriciler TBK m.40-48/155/162-182'nin gerçek yanılgılarını taşır:
müteselsil borçluluk ↔ alacaklılık, geciktirici ↔ bozucu şart, cezai şart
türleri, bağlanma ↔ cayma parası, temsil ↔ vekâlet, yetkisiz temsil.
"""
import json

P = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/borclar_hukuku/ozel_durumlar.json"

YAMA = {
    "ozeldurum-gen-0001": {"B": "Birden çok borçlunun bulunduğu her borç ilişkisi, ayrıca bir irade beyanına veya kanun hükmüne gerek olmaksızın kendiliğinden müteselsil sayılır"},
    "ozeldurum-gen-0002": {"B": "Alacaklı, borcu her bir borçludan yalnızca onun iç ilişkideki payı oranında isteyebilir; borcun tamamını tek bir borçludan talep etme hakkı bulunmaz"},
    "ozeldurum-gen-0004": {"D": "Müteselsil borçlu yalnızca kendi kişisel def'ilerini ileri sürebilir; borcun doğumuna veya sona ermesine ilişkin ortak def'ileri alacaklıya karşı ileri süremez"},
    "ozeldurum-gen-0005": {"D": "İç ilişkideki paylaşım her hâlde alacaklının belirlediği oranlara göre yapılır; borçluların aralarındaki anlaşma ve iradeleri dikkate alınmaz"},
    "ozeldurum-gen-0007": {"A": "Müteselsil alacaklılıkta borçlu, borcu ancak alacaklıların hepsine birlikte ifa ederek borçtan kurtulabilir; tek alacaklıya yapılan ödeme sonuç doğurmaz"},
    "ozeldurum-gen-0009": {"A": "(K), yalnızca kendi payını ödeyerek (M)'ye karşı borçtan tümüyle kurtulur; (M) kalan kısmı ayrıca (L)'den talep etmek üzere ona başvurur"},
    "ozeldurum-gen-0010": {"A": "Sözleşme baştan itibaren bütün hükümlerini doğurur; şart gerçekleştiğinde ise sözleşme kendiliğinden ve geçmişe etkili biçimde sona erer"},
    "ozeldurum-gen-0012": {"B": "Borçlu, askı döneminde borcun konusunu üçüncü kişilere devrederek borç ilişkisini istediği zaman tek taraflı olarak sona erdirebilir"},
    "ozeldurum-gen-0013": {"A": "Şart gerçekleşmediğinden sözleşme hüküm doğurmaz; şartın gerçekleşmesine dürüstlük kuralına aykırı biçimde engel olan tarafın davranışı sonucu değiştirmez"},
    "ozeldurum-gen-0015": {"D": "Bu taahhüt kesin ve şartsız bir borç niteliğindedir; (N) sınav sonucu ne olursa olsun arabayı devretmekle yükümlü kalır"},
    "ozeldurum-gen-0017": {"E": "Gecikme cezası yalnızca tarafların her ikisi de tacir olduğunda ifa ile birlikte istenebilir; adi işlerde alacaklı yalnızca ifayı talep edebilir"},
    "ozeldurum-gen-0019": {"C": "Cezai şart, asıl borç geçersiz olduğunda kendiliğinden asıl borcun yerine geçen ve bağımsız olarak istenebilen bir edime dönüşür"},
    "ozeldurum-gen-0020": {"E": "Alacaklı, uğradığı zarar kararlaştırılan cezayı aşsa bile yalnızca ceza ile yetinir; cezayı aşan zararını hiçbir koşulda talep edemez"},
    "ozeldurum-gen-0021": {"C": "Cezanın miktarı taraflarca serbestçe belirlenemez; her hâlde asıl alacağın kanunda önceden belirlenmiş bir yüzdesi olarak hesaplanır"},
    "ozeldurum-gen-0025": {"C": "İş sahibi bu cezayı ancak işin hiç tamamlanmaması hâlinde isteyebilir; işin gecikmeli tamamlanması hâlinde ceza hiç gündeme gelmez"},
    "ozeldurum-gen-0026": {"E": "Bağlanma parası, verildiği anda karşı tarafın mülkiyetine geçmeyen ve yalnızca güvence amacıyla bloke edilerek tutulan bir para niteliğindedir"},
    "ozeldurum-gen-0027": {"A": "Cayma parası taraflardan hiçbirine sözleşmeden dönme hakkı vermez; yalnızca sözleşmenin kurulduğunu kanıtlayan bir bağlanma parası işlevi görür"},
    "ozeldurum-gen-0028": {"C": "Bağlanma parası yalnızca taşınmaz satışlarında, cayma parası ise yalnızca taşınır satışlarında kararlaştırılabilir; başka sözleşmelerde geçersizdir"},
    "ozeldurum-gen-0031": {"A": "Temsil yetkisi ile vekâlet aynı hukuki kurumdur; temsil yetkisi olmadan vekâlet, vekâlet olmadan da temsil yetkisi düşünülemez ve ikisi hep birlikte doğar"},
    "ozeldurum-gen-0036": {"C": "Karşı taraf, işlem onanmasa dahi temsil olunanı işlemi aynen ifaya zorlayabilir; yalnızca yetkisiz temsilciden tazminat istemekle yetinmesi gerekmez"},
    "ozeldurum-gen-0037": {"D": "Sözleşme yalnızca (S) ile (Ü) arasında hüküm doğurur; (T)'nin sonradan verdiği onama bu ilişkiyi hiçbir biçimde etkilemez ve onu taraf yapmaz"},
    "ozeldurum-gen-0038": {"D": "Yetkisiz temsil yalnızca sözleşmesel ilişkilerde, vekâletsiz iş görme ise yalnızca haksız fiil alanında söz konusu olur; ikisi hiç kesişmez"},
    "ozeldurum-gen-0046": {"A": "(P), borcu ödemiş olsa da alacaklının haklarına halef olamaz; diğer borçlulara karşı alacaklının sahip olduğu güvencelerden yararlanamaz"},
    "ozeldurum-gen-0047": {"E": "Şartın gerçekleşmesi sözleşmeyi geçmişe etkili biçimde ortadan kaldırır; taraflar o güne kadar aldıkları bütün edimleri karşılıklı olarak geri verir"},
    "ozeldurum-gen-0048": {"A": "(K) sözleşmeden dönemez; cayma parası kararlaştırılmış olsa dahi taraflar sözleşmeyle kesin biçimde bağlı kalır ve dönme hakkı doğmaz"},
    "ozeldurum-gen-0049": {"D": "Bağlanma parası verilmesi sözleşmenin henüz kurulmadığını gösterir; taraflar bu aşamada diledikleri gibi ve serbestçe vazgeçebilir"},
    "ozeldurum-gen-0050": {"E": "Karşı taraf yetki sınırını bilmediği için sözleşme, şirketin ayrıca onamasına gerek olmaksızın doğrudan doğruya şirketi bağlar ve hüküm doğurur"},
    "ozeldurum-gen-0051": {"C": "Bu kayıt geçersizdir; borcun hiç ifa edilmemesi hâline bağlı bir ceza kararlaştırılması hukuken mümkün görülmemiştir"},
    "ozeldurum-gen-0053": {"A": "(X)'in kişisel def'ini, aynı ilişkideki bütün müteselsil borçlular da alacaklıya karşı ileri sürebilir; def'i kişiye özgü kalmaz"},
    "ozeldurum-gen-0054": {"C": "Karşı taraf uğradığı zararı yalnızca temsil olunan (Z)'den isteyebilir; yetkisiz temsilci (Y) hiçbir hâlde kişisel olarak sorumlu tutulamaz"},
    "ozeldurum-gen-0055": {"D": "Müteselsil alacaklılıkta borçlu, ödemeyi hangi alacaklıya yapacağını kendisi seçemez; bu nedenle (A1)'e yapılan ödeme geçersiz sayılır"},
    "ozeldurum-gen-0056": {"A": "Askı döneminde alacaklının korunmaya değer hiçbir menfaati bulunmaz; borçlu bu dönemde edim konusu üzerinde tümüyle serbest kalır"},
    "ozeldurum-gen-0058": {"D": "Müteselsil borçlulukta alacaklı borcun tamamını bir borçludan ister; müteselsil alacaklılıkta ise borçlu ödemeyi alacaklıların hepsine birlikte yapar"},
    "ozeldurum-gen-0060": {"B": "Alacaklı gecikmeli ifayı çekince koymadan kabul etmiş olsa dahi, kararlaştırılmış olan gecikme cezasını her hâlde ayrıca talep edebilir"},
}

# ── 2. tur: self-check 19 ıska bildirdi. Bu dosyanın doğru şıkları çok uzun
# (122-183) — müteselsil borçluluk ve temsil kavramları çok koşul taşıyor.
YAMA.update({
    "ozeldurum-gen-0001": {"B": "Birden çok borçlunun bulunduğu her borç ilişkisi, taraflar ayrıca kararlaştırmasa ve kanunda bir hüküm bulunmasa dahi kendiliğinden müteselsil borçluluk sayılır"},
    "ozeldurum-gen-0002": {"B": "Alacaklı, borcu her bir borçludan yalnızca onun iç ilişkideki payı oranında isteyebilir; borcun tamamını tek bir borçludan talep etme hakkı hiçbir hâlde bulunmaz"},
    "ozeldurum-gen-0004": {"D": "Müteselsil borçlu yalnızca kendi kişisel def'ilerini ileri sürebilir; borcun doğumuna, geçersizliğine veya sona ermesine ilişkin ortak def'ileri alacaklıya karşı hiç ileri süremez"},
    "ozeldurum-gen-0005": {"D": "İç ilişkideki paylaşım her hâlde alacaklının tek taraflı belirlediği oranlara göre yapılır; borçluların aralarındaki anlaşma ve iradeleri hiç dikkate alınmaz"},
    "ozeldurum-gen-0009": {"A": "(K), yalnızca kendi payını ödeyerek (M)'ye karşı borçtan tümüyle kurtulur; (M) kalan kısım için ayrıca (L)'ye başvurur ve ondan talep eder"},
    "ozeldurum-gen-0015": {"D": "Bu taahhüt kesin ve şartsız bir borç niteliğindedir; (N) sınav sonucu ne olursa olsun ve şart gerçekleşmese bile arabayı devretmekle yükümlü kalır"},
    "ozeldurum-gen-0019": {"C": "Cezai şart, asıl borç geçersiz olduğunda kendiliğinden asıl borcun yerine geçen ve ondan bağımsız olarak istenebilen ayrı bir edime dönüşür"},
    "ozeldurum-gen-0021": {"C": "Cezanın miktarı taraflarca serbestçe belirlenemez; ceza her hâlde asıl alacağın kanunda önceden belirlenmiş bir yüzdesi olarak hesaplanır"},
    "ozeldurum-gen-0025": {"C": "İş sahibi bu cezayı ancak işin hiç tamamlanmaması hâlinde isteyebilir; işin gecikmeli olarak tamamlanması hâlinde ceza hiçbir biçimde gündeme gelmez"},
    "ozeldurum-gen-0027": {"A": "Cayma parası taraflardan hiçbirine sözleşmeden dönme hakkı vermez; yalnızca sözleşmenin kurulduğunu kanıtlayan bir bağlanma parası işlevi görür ve iade edilir"},
    "ozeldurum-gen-0036": {"C": "Karşı taraf, işlem temsil olunan tarafından onanmasa dahi onu işlemi aynen ifaya zorlayabilir; yetkisiz temsilciden tazminat istemekle yetinmesi gerekmez"},
    "ozeldurum-gen-0038": {"D": "Yetkisiz temsil yalnızca sözleşmesel ilişkilerde, vekâletsiz iş görme ise yalnızca haksız fiil alanında söz konusu olur; iki kurum hiçbir noktada kesişmez"},
    "ozeldurum-gen-0046": {"A": "(P), borcun tamamını ödemiş olsa da alacaklının haklarına halef olamaz; diğer borçlulara karşı alacaklının sahip olduğu rehin ve kefalet güvencelerinden yararlanamaz"},
    "ozeldurum-gen-0049": {"D": "Bağlanma parası verilmesi sözleşmenin henüz kurulmadığını ve görüşmelerin sürdüğünü gösterir; taraflar bu aşamada diledikleri gibi serbestçe vazgeçebilir"},
    "ozeldurum-gen-0051": {"C": "Bu kayıt geçersiz sayılır; borcun hiç ifa edilmemesi hâline bağlanan bir ceza kararlaştırılması hukuken mümkün görülmemiştir"},
    "ozeldurum-gen-0054": {"C": "Karşı taraf uğradığı zararı yalnızca temsil olunan (Z)'den isteyebilir; yetkisiz temsilci (Y) işlemi kendi adına yapmış olsa bile kişisel olarak sorumlu tutulamaz"},
    "ozeldurum-gen-0055": {"D": "Müteselsil alacaklılıkta borçlu, ödemeyi hangi alacaklıya yapacağını kendisi seçemez; bu nedenle yalnız (A1)'e yapılan ödeme geçersiz sayılır ve borç sona ermez"},
    "ozeldurum-gen-0056": {"A": "Askı döneminde alacaklının korunmaya değer hiçbir menfaati bulunmaz; borçlu bu dönemde edimin konusu üzerinde tümüyle serbest kalır ve dilediğini yapabilir"},
    "ozeldurum-gen-0058": {"D": "Müteselsil borçlulukta alacaklı borcun tamamını dilediği bir borçludan ister; müteselsil alacaklılıkta ise borçlu ödemeyi alacaklıların hepsine birlikte yapmakla kurtulur"},
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
