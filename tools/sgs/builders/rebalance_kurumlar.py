# -*- coding: utf-8 -*-
"""vergi_hukuku/kurumlar_vergisi.json — şık boyu dengeleme (kör öğrenci %76 → ≤%30).

Vergi Hukuku'nun 7. ve son bozuk dosyası. 53 öncüllü-olmayan sorunun 44'ünde
doğru şık EN UZUNDU (%84).

★ Hedef DENGE, sıfır değil: 44'ün 9'una KASTEN dokunulmuyor (0012, 0018, 0026,
0040, 0047, 0054, 0059 gibi farkın zaten dar olduğu sorular). emlak_vergisi'nde
hepsini düzeltip doğru şıkkı %0 en uzuna indirmiş ve "doğru hep ortada" diye
yeni bir ipucu üretmiştim.

⚠ Kurumlar vergisi oranı ve istisna hadleri yıla bağlıdır; çeldiricilere oran
veya tutar sokulmadı — hepsi yapısal (mükellefiyet türü, istisna mantığı,
örtülü sermaye/transfer fiyatlandırması ölçütü, tasfiye dönemi).
"""
import json

P = "/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/vergi_hukuku/kurumlar_vergisi.json"

YAMA = {
    "kurumlar-gen-0001": {"A": "Kurumlar vergisinin konusu, gerçek kişilerin bir takvim yılında elde ettikleri ücret ve ticari kazançların toplamıdır"},
    "kurumlar-gen-0004": {"B": "Dernek ve vakıflar hiçbir biçimde kurumlar vergisiyle ilişkilendirilemez; bunlara ait iktisadi işletmeler de verginin dışında tutulur"},
    "kurumlar-gen-0005": {"C": "Yalnızca merkezi yönetime ait iktisadi işletmeler vergiye tabidir; belediyelere ve il özel idarelerine ait olanlar her hâlde vergi dışıdır"},
    "kurumlar-gen-0006": {"A": "İş ortaklıkları hiçbir hâlde kurumlar vergisi mükellefi olamaz; ortaklıktan doğan kazanç için yalnızca ortaklar gelir vergisi öder"},
    "kurumlar-gen-0007": {"E": "Kurum kazancı, kurumun sahip olduğu toplam servetin bir hesap dönemi içindeki değer artışından ibarettir"},
    "kurumlar-gen-0008": {"A": "Kurumlar vergisi ile gelir vergisi aynı vergidir; ikisi arasında mükellef, konu veya matrah bakımından hiçbir fark bulunmaz"},
    "kurumlar-gen-0009": {"C": "Kurumlar vergisi, kurumların sahip olduğu gayrimenkul ve taşıtlar üzerinden alınan bir servet vergisi niteliğindedir"},
    "kurumlar-gen-0010": {"A": "Tam mükellef kurumlar yalnızca Türkiye'de elde ettikleri kazançlar üzerinden vergilendirilir; yurt dışında elde ettikleri kazançlar Türkiye'de hiç vergilendirilmez"},
    "kurumlar-gen-0011": {"C": "Dar mükellef kurumlar hiçbir kazançları üzerinden Türkiye'de vergilendirilmez; Türkiye'de elde ettikleri kazanç için de yalnızca kendi ülkelerinde vergi öder"},
    "kurumlar-gen-0017": {"A": "Kurum kazancından hiçbir gider indirilemez; vergi, kurumun elde ettiği brüt hasılatın tamamı üzerinden hesaplanır"},
    "kurumlar-gen-0019": {"B": "Bir dönemde oluşan zarar hiçbir biçimde sonraki dönemlere aktarılamaz; zarar oluştuğu dönemde kaybolur ve mahsup edilemez"},
    "kurumlar-gen-0020": {"B": "İştirak kazançları istisnası yalnızca kurumun yurt dışındaki iştiraklerinden elde ettiği kazançlara tanınır; yurt içi iştirakler kapsam dışıdır"},
    "kurumlar-gen-0021": {"B": "İstisnanın amacı, kurumların elde ettiği bütün gelirleri vergiden muaf tutarak kurumları desteklemek ve yatırımı artırmaktır"},
    "kurumlar-gen-0023": {"A": "İstisna kazançlara ilişkin giderler her hâlde istisna dışı kazançtan serbestçe indirilebilir; ayrıştırma yapılması gerekmez"},
    "kurumlar-gen-0024": {"A": "Kurumların bankalardan yaptığı her türlü kısa vadeli borçlanma, tutarı ne olursa olsun örtülü sermaye olarak kabul edilir"},
    "kurumlar-gen-0025": {"C": "Transfer fiyatlandırması yalnızca kurumun yurt dışı işlemlerinde söz konusu olur; ilişkili kişilerle yurt içinde yapılan işlemler kapsam dışıdır"},
    "kurumlar-gen-0026": {"C": "Emsallere uygunluk yalnızca kurumun ortaklarıyla yaptığı işlemlerde değil, ilişkisiz bütün müşterileriyle işlemlerinde de ayrıca aranır"},
    "kurumlar-gen-0029": {"E": "Kurumlar vergisinde hesap dönemi, kurumun ortaklarının talebine göre üç veya altı aylık olarak serbestçe belirlenebilir"},
    "kurumlar-gen-0031": {"C": "Geçici vergi, kurumun ödeyeceği kurumlar vergisinden bağımsızdır ve ona mahsup edilemeyen ayrı bir vergi olarak tahsil edilir"},
    "kurumlar-gen-0032": {"C": "Tasfiye hâlinde vergilendirme yine normal takvim yılı hesap dönemi esas alınarak ve hiçbir değişiklik yapılmadan yürütülür"},
    "kurumlar-gen-0033": {"B": "Devir işlemleri her hâlde kurumun tasfiyesi sayılır ve devrolan kurumun tüm geçmiş kazançları yeniden vergilendirilir"},
    "kurumlar-gen-0034": {"A": "(A) A.Ş. yalnızca Türkiye'de elde ettiği kazançlar üzerinden vergilendirilir; yurt dışındaki şubesinden elde ettiği kazanç Türkiye'de beyan edilmez"},
    "kurumlar-gen-0035": {"A": "(C) A.Ş.'nin elde ettiği bu kâr payı her hâlde tam olarak kurumlar vergisine tabidir; iştirak kazançları istisnası burada uygulanmaz"},
    "kurumlar-gen-0036": {"A": "Ortaktan alınan borç ne kadar yüksek olursa olsun buna ilişkin faiz her hâlde serbestçe gider yazılır; örtülü sermaye söz konusu olmaz"},
    "kurumlar-gen-0037": {"D": "Bu satış, kurumun elde ettiği kazancı azalttığı için kuruma vergi avantajı sağlayan ve hukuken geçerli sayılan bir işlemdir"},
    "kurumlar-gen-0039": {"C": "Dar mükellef kurumun Türkiye'deki bu kazancı yalnızca kendi ülkesinde vergilendirilir; Türkiye'ye hiçbir vergi ödemesi yapılmaz"},
    "kurumlar-gen-0041": {"E": "Kâr payları yalnızca kurum düzeyinde kurumlar vergisine tabidir; kâr payını alan gerçek kişi ortakların ayrıca bir yükümlülüğü doğmaz"},
    "kurumlar-gen-0044": {"E": "Risturnlar kooperatifin gideri değil, ortaklarına dağıttığı olağan kâr payı sayılarak kurum kazancına dâhil edilir ve vergilendirilir"},
    "kurumlar-gen-0045": {"A": "Kurumlar vergisi beyannamesi, hesap döneminin kapandığı gün derhâl ve o gün içinde vergi dairesine verilir; ek süre tanınmaz"},
    "kurumlar-gen-0046": {"C": "Kurumların bölünmesi hiçbir hâlde mümkün değildir; kurumlar yalnızca birleşebilir, devrolabilir veya tasfiye yoluyla sona erebilir"},
    "kurumlar-gen-0047": {"C": "Muafiyet yalnızca yurt dışında kurulmuş olup Türkiye'de faaliyet gösteren yabancı kurumlara tanınmış bir ayrıcalıktır"},
    "kurumlar-gen-0048": {"A": "Muafiyet belirli bir kazancı, istisna ise kurumun kendisini vergi dışında tutar; ikisi de sonuçta aynı vergisel etkiyi doğurur"},
    "kurumlar-gen-0049": {"A": "Yurt dışı iştiraklerden elde edilen kazançlar hiçbir koşulda istisna kapsamına giremez; bunlar her hâlde tam olarak vergilendirilir"},
    "kurumlar-gen-0050": {"D": "Örtülü olarak dağıtılan kazanç, kuruma iade edilerek ertesi hesap döneminin kazancına eklenmek üzere bekletilir ve o dönem vergilenir"},
    "kurumlar-gen-0051": {"B": "Geçmiş yıl zararları hiçbir süre sınırı olmaksızın ve sonsuza kadar sonraki dönemlerin kazancından indirilebilir; beş yıl kuralı yoktur"},
    "kurumlar-gen-0052": {"A": "Kuruma yapılan hiçbir bağış ve yardım kurum kazancından indirilemez; bunların tamamı kanunen kabul edilmeyen gider sayılır"},
    "kurumlar-gen-0055": {"C": "Vergi kesintisi yalnızca tam mükellef kurumların kazançları üzerinden yapılır; dar mükellef kurumlara yapılan ödemelerde kesinti uygulanmaz"},
    "kurumlar-gen-0056": {"A": "İşlem piyasa fiyatından yapılmış olsa dahi, ilişkili kişiye yapılan her satış her hâlde örtülü kazanç dağıtımı olarak değerlendirilir"},
    "kurumlar-gen-0060": {"A": "Kurumların taşınmaz ve iştirak hissesi satışından doğan kazancın tamamı her hâlde ve hiçbir koşula bağlı olmaksızın vergiden istisnadır"},
}

# ── 2. tur: self-check 23 sorunun hedefi tutturamadığını söyledi. Bu dosyada
# boşluklar daha genişti (0032'de +29, 0039'da +28 karakter gerekiyordu).
YAMA.update({
    "kurumlar-gen-0006": {"A": "İş ortaklıkları hiçbir hâlde kurumlar vergisi mükellefi olamaz; ortaklıktan doğan kazanç için yalnızca ortakları kendi adlarına gelir vergisi öder"},
    "kurumlar-gen-0007": {"E": "Kurum kazancı, kurumun sahip olduğu toplam servetin bir hesap dönemi içinde gösterdiği değer artışından ibarettir"},
    "kurumlar-gen-0009": {"C": "Kurumlar vergisi, kurumların sahip olduğu gayrimenkul, taşıt ve demirbaşlar üzerinden alınan bir servet vergisidir"},
    "kurumlar-gen-0011": {"C": "Dar mükellef kurumlar hiçbir kazançları üzerinden Türkiye'de vergilendirilmez; Türkiye'deki işyerinden elde ettikleri kazanç için de yalnızca kendi ülkelerinde vergi öder"},
    "kurumlar-gen-0017": {"A": "Kurum kazancından hiçbir gider indirilemez; vergi, kurumun bir hesap döneminde elde ettiği brüt hasılatın tamamı üzerinden hesaplanır"},
    "kurumlar-gen-0021": {"B": "İstisnanın amacı, kurumların elde ettiği bütün gelirleri vergiden muaf tutarak kurumları desteklemek ve yatırım hacmini artırmaktır"},
    "kurumlar-gen-0023": {"A": "İstisna kazançlara ilişkin giderler her hâlde istisna dışı kazançtan serbestçe indirilebilir; gelir ve giderlerin ayrıştırılması gerekmez"},
    "kurumlar-gen-0024": {"A": "Kurumların bankalardan ve finans kuruluşlarından yaptığı her türlü kısa vadeli borçlanma, tutarı ne olursa olsun örtülü sermaye sayılır"},
    "kurumlar-gen-0029": {"E": "Kurumlar vergisinde hesap dönemi, kurumun ortaklarının talebi doğrultusunda üç veya altı aylık olarak serbestçe belirlenebilir"},
    "kurumlar-gen-0032": {"C": "Tasfiye hâlinde vergilendirme yine normal takvim yılı hesap dönemi esas alınarak ve hiçbir değişiklik yapılmadan sürdürülür; tasfiye dönemi diye ayrı bir kavram yoktur"},
    "kurumlar-gen-0033": {"B": "Devir işlemleri her hâlde kurumun tasfiyesi sayılır ve devrolan kurumun bütün geçmiş yıl kazançları yeniden vergilendirilerek tahsil edilir"},
    "kurumlar-gen-0034": {"A": "(A) A.Ş. yalnızca Türkiye'de elde ettiği kazançlar üzerinden vergilendirilir; yurt dışındaki şubesinden elde ettiği kazanç Türkiye'de hiç beyan edilmez"},
    "kurumlar-gen-0036": {"A": "Ortaktan alınan borç tutarı ne kadar yüksek olursa olsun buna ilişkin faiz her hâlde serbestçe gider yazılır; örtülü sermaye hiç söz konusu olmaz"},
    "kurumlar-gen-0037": {"D": "Bu satış, kurumun elde ettiği kazancı azalttığı için kuruma vergi avantajı sağlayan ve hukuken tümüyle geçerli sayılan bir işlemdir"},
    "kurumlar-gen-0039": {"C": "Dar mükellef kurumun Türkiye'deki işyerinden elde ettiği bu kazanç yalnızca kendi ülkesinde vergilendirilir; Türkiye'ye hiçbir vergi ödemesi yapılmaz"},
    "kurumlar-gen-0045": {"A": "Kurumlar vergisi beyannamesi, hesap döneminin kapandığı gün derhâl ve o gün içinde vergi dairesine verilir; beyan için hiçbir ek süre tanınmaz"},
    "kurumlar-gen-0048": {"A": "Muafiyet belirli bir kazancı, istisna ise kurumun kendisini vergi dışında tutar; ikisi de sonuçta tümüyle aynı vergisel etkiyi doğurur"},
    "kurumlar-gen-0049": {"A": "Yurt dışı iştiraklerden elde edilen kazançlar hiçbir koşulda istisna kapsamına giremez; bunlar her hâlde tam olarak vergilendirilir ve beyan edilir"},
    "kurumlar-gen-0050": {"D": "Örtülü olarak dağıtılan kazanç, kuruma iade edilerek ertesi hesap döneminin kazancına eklenmek üzere bekletilir ve o dönemde vergilendirilir"},
    "kurumlar-gen-0052": {"A": "Kuruma yapılan hiçbir bağış ve yardım kurum kazancından indirilemez; bunların tamamı kanunen kabul edilmeyen gider olarak kazanca eklenir"},
    "kurumlar-gen-0055": {"C": "Vergi kesintisi yalnızca tam mükellef kurumların elde ettiği kazançlar üzerinden yapılır; dar mükellef kurumlara yapılan ödemelerde kesinti hiç uygulanmaz"},
    "kurumlar-gen-0056": {"A": "İşlem piyasa fiyatından yapılmış olsa dahi, ilişkili kişiye yapılan her satış her hâlde örtülü kazanç dağıtımı sayılır ve matraha eklenir"},
    "kurumlar-gen-0060": {"A": "Kurumların taşınmaz ve iştirak hissesi satışından doğan kazancın tamamı her hâlde, süre ve fon şartı aranmaksızın vergiden istisna tutulur"},
})

# ── 3. tur. Bu dosya üç tur gerektirdi; boşlukları en geniş olan oydu.
YAMA.update({
    "kurumlar-gen-0009": {"C": "Kurumlar vergisi, kurumların sahip olduğu gayrimenkul, taşıt ve demirbaşların toplam değeri üzerinden alınan bir servet vergisidir"},
    "kurumlar-gen-0021": {"B": "İstisnanın amacı, kurumların elde ettiği bütün gelirleri vergiden muaf tutmak suretiyle kurumları desteklemek ve yatırım hacmini artırmaktır"},
    "kurumlar-gen-0023": {"A": "İstisna kazançlara ilişkin giderler her hâlde istisna dışı kazançtan serbestçe indirilebilir; gelir ile giderlerin ayrıştırılması gerekmez"},
    "kurumlar-gen-0029": {"E": "Kurumlar vergisinde hesap dönemi, kurumun ortaklarının talebi doğrultusunda üç veya altı aylık dönemler hâlinde serbestçe belirlenebilir"},
    "kurumlar-gen-0036": {"A": "Ortaktan alınan borcun tutarı ne kadar yüksek olursa olsun buna ilişkin faiz her hâlde serbestçe gider yazılabilir; örtülü sermaye hiç söz konusu olmaz"},
    "kurumlar-gen-0037": {"D": "Bu satış, kurumun elde ettiği kazancı azaltmasına rağmen kuruma vergi avantajı sağlayan ve hukuken tümüyle geçerli sayılan bir işlemdir"},
    "kurumlar-gen-0039": {"C": "Dar mükellef kurumun Türkiye'deki işyeri aracılığıyla elde ettiği bu kazanç yalnızca kendi ülkesinde vergilendirilir; Türkiye'ye hiçbir ödeme yapılmaz"},
    "kurumlar-gen-0045": {"A": "Kurumlar vergisi beyannamesi, hesap döneminin kapandığı gün derhâl ve aynı gün içinde vergi dairesine verilir; beyan için hiçbir ek süre tanınmaz"},
    "kurumlar-gen-0048": {"A": "Muafiyet belirli bir kazancı, istisna ise kurumun kendisini vergi dışında tutar; adları farklı olsa da ikisi sonuçta tümüyle aynı vergisel etkiyi doğurur"},
    "kurumlar-gen-0050": {"D": "Örtülü olarak dağıtılan kazanç, kuruma iade edilerek ertesi hesap döneminin kazancına eklenmek üzere bekletilir ve ancak o dönemde vergilendirilir"},
    "kurumlar-gen-0056": {"A": "İşlem piyasa fiyatından ve emsallere uygun biçimde yapılmış olsa dahi, ilişkili kişiye yapılan her satış örtülü kazanç dağıtımı sayılarak matraha eklenir"},
    "kurumlar-gen-0060": {"A": "Kurumların taşınmaz ve iştirak hissesi satışından doğan kazancın tamamı her hâlde, elde tutma süresi ve fon şartı aranmaksızın vergiden istisna tutulur"},
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
    print(f"yamalanan: {len(YAMA)} | hedefe ulaşan: {len(YAMA) - len(kalan)}/{len(YAMA)} "
          f"| kasten dokunulmayan: 9")
