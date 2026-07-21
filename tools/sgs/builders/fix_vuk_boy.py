# -*- coding: utf-8 -*-
"""vergi_usul_kanunu.json — şık boyu dengeleme (kör %88 → ≤%30).

Tanım sorularında doğru şık (tam tanım) çeldiricilerden hep birkaç karakter uzun
çıkıyor → "en uzunu seç" %88. Düzeltme: ~45 soruda EN UZUN çeldiriciyi, aynı
YANLIŞ fikri koruyarak daha dolu bir cümleye çevir (doğrunun üstüne çıkar → doğru
sıra 4'e iner). ~15 soru (her 4'te 1) doğru-en-uzun bırakılır → boy-sırası uçlara
yayılır. Dolgu ("zorunda/…") YOK. Doğru/kök/çözüm/harf'e DOKUNULMAZ.

Anahtar: mevcut EN UZUN çeldiricinin METNİ (eşleşme ile bulunur) → yeni metin.
"""
import json
import re

P = "content/vergi_hukuku/vergi_usul_kanunu.json"
CP = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/vergi_hukuku/vergi_usul_kanunu.json"
DOLGU = re.compile(r"zorunda|durumundadır|bulunmaktadır|kalınmaktadır|tutulmaktadır")

# eski_çeldirici_metni → yeni (daha dolu, aynı yanlış fikir, aynı register)
YENI = {
 "Kendi kazancı üzerinden doğan vergiyi bizzat beyan edip ödeyen asıl borçludur":
   "Kendi kazancı üzerinden doğan vergiyi bizzat beyan edip ödeyen ve borç doğrudan kendisine düşen asıl mükelleftir",
 "Vergi alacağı, mükellefin beyanname vermesinden bağımsız olarak hiç doğmaz":
   "Vergi alacağı, vergiyi doğuran olay gerçekleşse dahi ancak mükellef beyannamesini verdiğinde doğar",
 "Tüzel kişiler ehliyet taşımadığından mükellefiyetleri kanunen mümkün değildir":
   "Mükellef olabilmek için medeni hakları kullanma ehliyeti şarttır; küçük ve kısıtlıların mükellefiyeti kurulamaz",
 "Alım-satıma taraf olanların birbirinin vergisinden sorumluluğu hiçbir hâlde doğmaz":
   "Alım-satıma taraf olanların birbirinin vergisinden sorumluluğu, aralarında açık anlaşma bulunsa dahi hiçbir hâlde doğmaz",
 "İşe başlama bildirimi yalnızca ticaret siciline yapılır, vergi dairesi ilgilenmez":
   "İşe başlama bildirimi yalnızca ticaret siciline yapılır; vergi dairesine ayrıca bir bildirimde bulunulmasına gerek yoktur",
 "Kanunla konulan süreler idarece dilendiği zaman geriye yürütülerek değiştirilir":
   "Kanunla konulan süreler, idarece gerekli görüldüğünde geriye yürütülerek dilendiği biçimde değiştirilebilir",
 "Ek süre yalnızca vergi mahkemesinin vereceği kararla tanınabilen bir haktır":
   "Zor durum ek süresi yalnızca vergi mahkemesinin vereceği kararla tanınır; idarenin bu konuda hiçbir takdir yetkisi yoktur",
 "Tüzel kişilere tebliğ, herhangi bir çalışana değil yalnızca kurucu ortağa yapılır":
   "Tüzel kişilere tebliğ yalnızca kurucu ortağa yapılabilir; şirketin başka bir çalışanına yapılan tebliğ geçersiz sayılır",
 "Elektronik tebliğ hukuken geçersiz olup yalnızca kâğıt tebligat sonuç doğurur":
   "Tebliğ yalnızca elden teslimle geçerli olup posta ve elektronik ortam yoluyla yapılan tebliğ hiçbir sonuç doğurmaz",
 "İlan tebliği yalnızca gazete yerine vergi dairesi kapısına asmakla yapılır":
   "İlan yoluyla tebliğ yalnızca vergi dairesinin kapısına yazı asılmasıyla yapılır; gazete veya başka bir araç kullanılamaz",
 "Süreler her hâlde başladığı gün dâhil edilerek ve tatiller de sayılarak hesaplanır":
   "Süreler her hâlde başladığı gün de hesaba katılarak ve araya giren resmî tatil günleri ayrıca gün olarak sayılarak hesaplanır",
 "Tarh, verginin ödenmesi gereken safhaya gelmesini ifade eden tahakkuktur":
   "Tarh, tarh ve tebliğ edilmiş olan verginin ödenmesi gereken safhaya gelmesini ifade eden tahakkuk işlemidir",
 "Vergi dairesinin maddi hatasını düzeltmek amacıyla yapılan düzeltme tarhıdır":
   "Vergi dairesinin kendi yaptığı maddi bir hesap hatasını gidermek amacıyla resen başvurduğu bir düzeltme tarhı türüdür",
 "Mükellefin başvurusu üzerine matrahı artırmak için isteğe bağlı yapılan tarhtır":
   "Mükellefin kendi başvurusu üzerine, beyan ettiği matrahı artırmak amacıyla isteğe bağlı olarak yapılan tarhtır",
 "Tahakkuk, kesinleşen vergiye karşı uzlaşma talebinde bulunulmasıdır":
   "Tahakkuk, kesinleşmiş bir vergiye karşı mükellefin uzlaşma ya da düzeltme talebinde bulunmasıdır",
 "Vergilendirme hataları yalnızca verginin oranında yapılan aritmetik yanlışlıklardır":
   "Vergilendirme hataları yalnızca vergi oranının ve vergi matrahının hesaplanmasında yapılan aritmetik yanlışlıklardan ibarettir",
 "Vergi borcu yalnızca ödeme ile sona erer; başka hiçbir sebep borcu kaldırmaz":
   "Vergi borcu yalnızca ödeme yoluyla sona erer; zamanaşımı, terkin veya uzlaşma borcu hiçbir hâlde kaldırmaz",
 "Zamanaşımı dolsa dahi vergi süresiz olarak tarh edilebilir, süre bağlayıcı değildir":
   "Zamanaşımı süresi dolsa dahi vergi süresiz olarak tarh edilebilir; kanundaki süre idare bakımından bağlayıcı değildir",
 "Uzlaşmada yalnızca verginin aslı görüşülür, cezalar hiçbir hâlde kapsama girmez":
   "Uzlaşmada yalnızca verginin aslı görüşülebilir; kesilen vergi cezaları hiçbir hâlde uzlaşma kapsamına girmez",
 "Uzlaşma talebi için tanınan süre her mükellef için ayrı ayrı belirlenir":
   "Uzlaşma talebi için kanunda ortak bir süre yoktur; tanınan süre her mükellef için idarece ayrı ayrı belirlenir",
 "Pişmanlık yalnızca usulsüzlük cezalarını kaldıran, vergiyi etkilemeyen kurumdur":
   "Pişmanlık yalnızca usulsüzlük cezalarını kaldıran bir kurum olup verginin aslını ve doğan vergi ziyaı cezasını hiç etkilemez",
 "Değerleme, iktisadi kıymetlerin yalnızca defterde gösterilen adının yazılmasıdır":
   "Değerleme, iktisadi kıymetlerin herhangi bir tutar takdir edilmeksizin yalnızca defterde adının yazılmasıdır",
 "Maliyet bedeli, kıymetin vergi dairesince belirlenen resmî vergi değeridir":
   "Maliyet bedeli, bir kıymetin edinilme gideri değil, tümüyle vergi dairesince belirlenen resmî vergi değeri esas alınarak bulunur",
 "Mukayyet değer, senedin ihraç anındaki üzerinde yazılı itibari değeridir":
   "Mukayyet değer, bir kıymetin muhasebe kaydındaki değeri değil, senedin üzerinde yazılı itibari değeridir",
 "Emsal bedel, yalnızca senetli alacaklar için hesaplanan tasarruf değeridir":
   "Emsal bedel, bir malın satılabilir değeri değil, yalnızca senede bağlı alacaklar için hesaplanan tasarruf değeridir",
 "Amortisman, stokların dönem sonunda toplu olarak gider yazılması işlemidir":
   "Amortisman, duran varlıkların yıpranması değil, dönem sonunda elde kalan stok mevcudunun toplu olarak gider yazılıp itfa edilmesi işlemidir",
 "Azalan bakiye yönteminde oran her yıl mükellefçe serbestçe yeniden belirlenir":
   "Azalan bakiye yönteminde uygulanacak oran kanunla bağlı olmayıp her yıl mükellef tarafından serbestçe belirlenir",
 "Yalnızca vadesi henüz gelmemiş ve tahsili beklenen alacaklar değersiz sayılır":
   "Yalnızca vadesi henüz gelmemiş, tahsili beklenen ve borçlusu sağlam olan alacaklar değersiz alacak sayılır",
 "Borçlunun hiç haberi olmadan alacaklının tek taraflı sildiği her alacaktır":
   "Borçlunun hiç haberi olmadan, alacaklının kendi defterinden tek taraflı olarak sildiği her türlü alacaktır",
 "Senede bağlı olmayan açık hesap alacakları da her hâlde reeskonta tabidir":
   "Senede bağlı olmayan açık hesap şeklindeki alacak ve borçlar da vadesi geldikçe her hâlde reeskonta tabi tutulur",
 "İşletme hesabı esası yalnızca büyük sermaye şirketlerine tanınan bir usuldür":
   "İşletme hesabı esası yalnızca büyük sermaye şirketlerine tanınan; küçük esnafın yararlanamadığı bir defter usulüdür",
 "Defterler yalnızca yıl bittikten sonra, izleyen yılın herhangi bir ayında tasdik edilir":
   "Defterler yalnızca ilgili yıl bittikten sonra, izleyen yılın herhangi bir ayında geriye dönük olarak tasdik edilir",
 "Defter ve belgeler yalnızca cari yıl boyunca saklanır, yıl bitince atılabilir":
   "Defter ve belgeler yalnızca ait olduğu cari yıl boyunca saklanır; yıl bittiğinde imha edilmeleri mümkündür",
 "Fatura, yalnızca malın taşınması sırasında araçta bulundurulan sevk belgesidir":
   "Fatura, müşterinin borcunu gösteren bir belge değil, yalnızca malın taşınmasında araçta bulundurulan sevk belgesidir",
 "Fatura, malın tesliminden itibaren en geç bir yıl içinde düzenlenebilir":
   "Fatura, malın teslimi veya hizmetin yapılmasından itibaren en geç bir yıllık süre içinde düzenlenebilir",
 "Sevk irsaliyesi, çiftçiden yapılan alımlarda düzenlenen müstahsil makbuzudur":
   "Sevk irsaliyesi, malın taşınmasında düzenlenen belge değil, çiftçiden yapılan alımlarda kullanılan müstahsil makbuzudur",
 "Serbest meslek makbuzu, çiftçiden alınan ürün için düzenlenen belgedir":
   "Serbest meslek makbuzu, mesleki tahsilat için değil, çiftçiden alınan ürün karşılığında düzenlenen bir belgedir",
 "Yoklama, yalnızca mahkeme kararıyla mükellefin iş yerinde arama yapılmasıdır":
   "Yoklama, maddi olayların tespiti değil, yalnızca mahkeme kararıyla mükellefin iş yerinde arama yapılmasıdır",
 "İnceleme, yalnızca kesinleşmiş cezanın mükelleften tahsil edilmesidir":
   "Vergi incelemesi, verginin doğruluğunun araştırılması değil, kesinleşmiş bir cezanın mükelleften tahsil edilmesidir",
 "Bilgi verme ödevi yalnızca mükellefin kendisiyle sınırlı olup üçüncü kişileri bağlamaz":
   "Bilgi verme ödevi yalnızca mükellefin kendisiyle sınırlıdır; üçüncü kişiler ve kamu idareleri bu ödevle bağlı değildir",
 "Vergi ziyaı, beyannamenin hiç verilmemiş ama verginin ödenmiş olmasıdır":
   "Vergi ziyaı, verginin eksik tahakkuk ettirilmesi değil, beyanname hiç verilmediği hâlde verginin tam ödenmiş olmasıdır",
 "Vergi ziyaı cezası, verginin aslından bağımsız maktu ve sabit bir tutardır":
   "Vergi ziyaı cezası, ziyaa uğratılan vergiden bağımsız, her olayda aynı olan maktu ve sabit bir tutar olarak kesilir",
 "Özel usulsüzlük cezası, yalnızca ilk derece usulsüzlükle aynı fiili cezalandırır":
   "Özel usulsüzlük cezası, belge düzenine aykırılığı değil, yalnızca birinci derece usulsüzlükle aynı fiili cezalandırır",
 "Kaçakçılık suçu yalnızca para cezasıyla karşılanan basit bir usulsüzlüktür":
   "Kaçakçılık suçu, hapis cezası gerektiren ağır bir fiil değil, yalnızca para cezasıyla karşılanan basit bir usulsüzlük türüdür",
 "Tekerrür, kesinleşmiş cezanın mükellef lehine indirilmesini sağlayan kurumdur":
   "Tekerrür, yeni bir fiille cezanın artırılması değil, daha önce kesinleşmiş cezanın mükellef lehine indirilmesini sağlayan kurumdur",
}

if __name__ == "__main__":
    qs = json.load(open(P, encoding="utf-8"))
    eslesen = 0
    eksik = []
    for q in qs:
        cor = q["options"][q["answer"]]
        for k, v in list(q["options"].items()):
            if k == q["answer"]:
                continue
            if v in YENI:
                yeni = YENI[v]
                assert not DOLGU.search(yeni), f"{q['id']}: DEFILLER'da dolgu"
                if len(yeni) < len(cor) + 2:
                    eksik.append((q["id"], k, len(yeni), len(cor), len(cor) + 2 - len(yeni)))
                q["options"][k] = yeni
                eslesen += 1
        assert len(set(q["options"].values())) == 5, f"{q['id']}: şık tekrarı"
    assert eslesen == len(YENI), f"eşleşen {eslesen} ≠ {len(YENI)} (metin tutmadı)"
    if eksik:
        print(f"KISA ({len(eksik)}):")
        for i, k, ly, d, gap in sorted(eksik, key=lambda x: -x[4]):
            print(f"  {i}/{k}: {ly} < doğru {d}+2 ({gap} eksik)")
        raise SystemExit(1)

    import sys
    sys.path.insert(0, "tools/sgs")
    from audit import kor_ogrenci
    from collections import Counter
    puan, strateji = kor_ogrenci(qs)
    rank = Counter()
    for q0 in qs:
        lens = sorted((len(v), k) for k, v in q0["options"].items())
        rank[[k for _, k in lens].index(q0["answer"]) + 1] += 1
    print(f"kör: {puan}% ← {strateji} | boy-sırası {dict((r, rank[r]) for r in range(1,6))}")
    assert puan <= 30, f"kör {puan}% > 30"

    for path in (P, CP):
        json.dump(qs, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"dengelendi: {eslesen} çeldirici → iki repo")
