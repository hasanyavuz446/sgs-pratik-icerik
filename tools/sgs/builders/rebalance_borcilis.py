# -*- coding: utf-8 -*-
"""borclar_hukuku/borc_iliskisi_kaynaklari.json — şık boyu dengeleme (%70 → ≤%30).

52 öncüllü-olmayan sorunun 41'inde doğru şık EN UZUNDU.

Kasten DOKUNULMAYAN 9: 0004 (kategori şıkları, 36 karakter — uzatmak yapay) ·
0002 · 0032 · 0050 (fark zaten 0) · 0009 · 0012 · 0028 · 0044 · 0054
(fark 1-2 karakter).

⚠ Yükümlülük dili asimetrisi zayıf (çeldiricide 6); boy dengelemesi yeter.
Uzatmalarda "zorunda/durumundadır" KULLANILMADI.

Çeldiriciler TBK'nın temel kavram yanılgılarını taşır: alacaklı ↔ borçlu,
nispi ↔ mutlak hak, borç kaynakları (sözleşme/haksız fiil/sebepsiz zenginleşme),
parça ↔ cins borcu, maddi ↔ manevi zarar, kusurlu ↔ kusursuz sorumluluk.
"""
import json

P = ("/Users/hasanyavuz/Desktop/projects/sgs-pratik-icerik/content/"
     "borclar_hukuku/borc_iliskisi_kaynaklari.json")

YAMA = {
    "borc-iliski-gen-0001": {"B": "Yalnızca para borçlarını kapsayan ve tarafların birbirine yalnızca nakit ödeme yapmasını gerektiren finansal nitelikte bir düzenleme"},
    "borc-iliski-gen-0003": {"A": "Yalnızca bir miktar paranın ödenmesi biçiminde ortaya çıkan ve bunun dışında başka bir türü bulunmayan tek tip yükümlülük"},
    "borc-iliski-gen-0005": {"D": "Kanunun, tarafların iradesine hiç bakılmaksızın doğrudan öngördüğü ve kişiye yüklediği yasal nitelikteki yükümlülük"},
    "borc-iliski-gen-0006": {"C": "Geçerli bir hukuki sebep bulunmadan bir kişinin başkasının mal varlığı aleyhine zenginleşmesinden doğan iade borcu"},
    "borc-iliski-gen-0007": {"D": "Kişinin bir eşya üzerinde herkese karşı ileri sürebileceği, mutlak nitelikli ve ayni bir hak elde etmesi durumu"},
    "borc-iliski-gen-0008": {"C": "Kanundan doğan velayet ilişkisinden kaynaklanır; taraflar arasında yasal bir bağ bulunduğu için borç doğar"},
    "borc-iliski-gen-0011": {"A": "Alacak hakkı herkese karşı ileri sürülebilir ve sahibine bir eşya üzerinde doğrudan doğruya egemenlik sağlar"},
    "borc-iliski-gen-0013": {"D": "Yalnızca bir tarafın borç altına girdiği, diğer tarafın ise bundan hiçbir menfaat sağlamadığı nitelikteki sözleşme"},
    "borc-iliski-gen-0014": {"D": "Eser sözleşmesi; yüklenicinin eser meydana getirme, iş sahibinin ise bedel ödeme borcu altına girdiği sözleşme türü"},
    "borc-iliski-gen-0016": {"E": "Zarara uğrayan kişinin, uğradığı zararı belgelerle ispatlamak durumunda olduğunu gösteren usule ilişkin kural"},
    "borc-iliski-gen-0018": {"A": "Maddi zarar kişinin duygusal ve ruhsal kaybını; manevi zarar ise onun mal varlığındaki eksilmeyi ifade eden kavramdır"},
    "borc-iliski-gen-0019": {"E": "Bir kişinin, sokakta bulduğu ve sahibi belli olmayan bir eşyayı geçici bir süre yanında bulundurması durumu"},
    "borc-iliski-gen-0021": {"A": "Borçlunun hiçbir biçimde yerine getirmesi gerekmeyen ve hukuken tümüyle geçersiz sayılan nitelikteki yükümlülük"},
    "borc-iliski-gen-0022": {"B": "Asli edim yalnızca para borçlarını; yan edim ise yalnızca yapma borçlarını kapsayan bir edim türü ayrımıdır"},
    "borc-iliski-gen-0023": {"A": "Borçlunun tek ve belirli bir edimi yerine getirmekle yükümlü olduğu, başka hiçbir seçeneğinin bulunmadığı borç"},
    "borc-iliski-gen-0024": {"B": "Parça borcunda edimin konusu türüyle belirlenirken; cins borcunda ferden belirlenmiş tek bir şey borçlanılmış olur"},
    "borc-iliski-gen-0025": {"A": "Failin, zarara yol açan davranışını kasten ya da ihmalle gerçekleştirmiş olması gerektiğine ilişkin zorunlu koşul"},
    "borc-iliski-gen-0026": {"B": "Zararın maddi değil manevi nitelikte ortaya çıkmış ve kişilik değerlerini doğrudan etkilemiş olması koşulu"},
    "borc-iliski-gen-0033": {"A": "Bir kişinin, kendisine verilmiş geçerli bir vekâlete dayanarak başkası adına ve onun hesabına işlem yapması"},
    "borc-iliski-gen-0035": {"A": "Zenginleşen kişi, iyiniyetli olsa dahi her koşulda zenginleşmenin başlangıçtaki tam tutarını eksiksiz iade eder"},
    "borc-iliski-gen-0041": {"D": "Borç ilişkisinde tarafların yerine geçerek borcu tümüyle üstlenen ve her iki tarafı da borçtan kurtaran kişi"},
    "borc-iliski-gen-0043": {"A": "Aynen tazmin zararın para ödenerek; nakden tazmin ise zarardan önceki durumun fiilen sağlanması yoluyla giderilmesidir"},
    "borc-iliski-gen-0046": {"C": "Zenginleşme ile fakirleşme arasında doğrudan bir nedensellik ilişkisinin bulunması koşulu"},
    "borc-iliski-gen-0047": {"D": "Kusur yalnızca kasttan ibarettir; ihmalle gerçekleşen davranışlar hiçbir hâlde kusur kapsamına girmez"},
    "borc-iliski-gen-0048": {"A": "İki tacirin karşılıklı edim borçları içeren bir mal alım satım anlaşması yaparak ilişkiye girmesi durumu"},
    "borc-iliski-gen-0049": {"D": "Zarar görenin kendi kusuru tazminatı iki katına çıkarır ve fail zararın iki mislini ödemekle yükümlü kalır"},
    "borc-iliski-gen-0051": {"C": "Zarar görenin, uğradığı manevi acıyı gidermek amacıyla istediği ve maddi zarardan bağımsız olarak belirlenen tutar"},
    "borc-iliski-gen-0052": {"B": "Edimin baştan imkânsız olması sözleşmeyi hiçbir biçimde etkilemez; imkânsız bir edim de geçerli olarak borçlanılabilir"},
    "borc-iliski-gen-0055": {"C": "Alacaklı ile borçlunun aralarında anlaşarak borcu bütünüyle ortadan kaldırması ve alacağı sona erdirmesi"},
    "borc-iliski-gen-0056": {"B": "Borcun naklinde alacaklı, alacağın temlikinde ise borçlu değişir; iki kurumda da aynı taraf yer değiştirmiş olur"},
    "borc-iliski-gen-0057": {"B": "Her ikisinde de kusuru ispat yükü daima zarar görene (alacaklıya) aittir; borçluya hiçbir ispat yükü düşmez ve o savunma yapmaz"},
    "borc-iliski-gen-0058": {"E": "Kusursuz sorumlulukta, kanunun açıkça öngördüğü hâllerde kusur bulunmasa da sorumluluk doğabilir"},
}

# ── 2. tur: self-check 20 ıska bildirdi.
YAMA.update({
    "borc-iliski-gen-0006": {"C": "Geçerli bir hukuki sebep bulunmaksızın bir kişinin başkasının mal varlığı aleyhine zenginleşmesinden doğan iade yükümlülüğü"},
    "borc-iliski-gen-0007": {"D": "Kişinin bir eşya üzerinde herkese karşı ileri sürebileceği, mutlak nitelikli ve ayni bir hak elde etmiş olması durumu"},
    "borc-iliski-gen-0013": {"D": "Yalnızca bir tarafın borç altına girdiği, karşı tarafın ise bundan hiçbir menfaat sağlamadığı nitelikteki sözleşme türü"},
    "borc-iliski-gen-0016": {"E": "Zarara uğrayan kişinin, uğradığı zararı belgelerle ve tanıkla ispatlaması gerektiğini gösteren usule ilişkin kural"},
    "borc-iliski-gen-0018": {"A": "Maddi zarar kişinin duygusal ve ruhsal kaybını; manevi zarar ise onun mal varlığındaki ölçülebilir eksilmeyi ifade eder"},
    "borc-iliski-gen-0021": {"A": "Borçlunun hiçbir biçimde yerine getirmesi gerekmeyen ve hukuk düzenince tümüyle geçersiz sayılan nitelikteki yükümlülük"},
    "borc-iliski-gen-0022": {"B": "Asli edim yalnızca para borçlarını; yan edim ise yalnızca yapma borçlarını kapsayan bir edim türü ayrımını ifade eder"},
    "borc-iliski-gen-0023": {"A": "Borçlunun tek ve belirli bir edimi yerine getirmekle yükümlü olduğu, bunun dışında hiçbir seçeneğinin bulunmadığı borç"},
    "borc-iliski-gen-0024": {"B": "Parça borcunda edimin konusu türüyle belirlenirken; cins borcunda ise ferden belirlenmiş tek bir şey borçlanılmış olur"},
    "borc-iliski-gen-0025": {"A": "Failin, zarara yol açan davranışını kasten ya da ihmalle gerçekleştirmiş olması gerektiğine ilişkin zorunlu unsur"},
    "borc-iliski-gen-0033": {"A": "Bir kişinin, kendisine verilmiş geçerli bir vekâlete dayanarak başkası adına ve onun hesabına hukuki işlem yapması"},
    "borc-iliski-gen-0035": {"A": "Zenginleşen kişi, iyiniyetli olsa dahi her koşulda zenginleşmenin başlangıçtaki tam tutarını eksiksiz olarak iade eder"},
    "borc-iliski-gen-0043": {"A": "Aynen tazmin zararın para ödenerek; nakden tazmin ise zarardan önceki durumun fiilen geri getirilmesiyle giderilmesidir"},
    "borc-iliski-gen-0047": {"D": "Kusur yalnızca kasttan ibarettir; ihmalle gerçekleşen davranışlar hiçbir hâlde kusur kapsamına dâhil edilmez"},
    "borc-iliski-gen-0049": {"D": "Zarar görenin kendi kusuru tazminatı iki katına çıkarır; fail bu durumda zararın iki mislini ödemekle yükümlü kalır"},
    "borc-iliski-gen-0052": {"B": "Edimin baştan imkânsız olması sözleşmeyi hiçbir biçimde etkilemez; imkânsız bir edim de geçerli olarak borçlanılabilir"},
    "borc-iliski-gen-0055": {"C": "Alacaklı ile borçlunun aralarında anlaşarak borcu bütünüyle ortadan kaldırması ve alacağı kesin olarak sona erdirmesi"},
    "borc-iliski-gen-0056": {"B": "Borcun naklinde alacaklı, alacağın temlikinde ise borçlu değişir; iki kurumda da aynı taraf yer değiştirmiş olur"},
    "borc-iliski-gen-0057": {"B": "Her ikisinde de kusuru ispat yükü daima zarar görene (alacaklıya) aittir; borçluya hiçbir ispat yükü düşmez ve o savunma yapmakla yükümlü olmaz"},
    "borc-iliski-gen-0058": {"E": "Kusursuz sorumlulukta, kanunun açıkça öngördüğü hâllerde failin kusuru bulunmasa da sorumluluk doğabilir"},
})

# ── 3. tur. ⚠ İKİ turdur aynı hatayı yaptım: uzatmaları kıl payı kısa yazdım
# (0006'da 122 ↔ 123, 0007'de 117 ↔ 117). Bu turda her uzatma doğrunun en az
# 15 karakter ÜSTÜNE çıkacak biçimde ikinci bir yan cümleyle açıldı.
YAMA.update({
    "borc-iliski-gen-0006": {"C": "Geçerli bir hukuki sebep bulunmaksızın bir kişinin başkasının mal varlığı aleyhine zenginleşmesinden doğan ve kanunla düzenlenmiş iade yükümlülüğü"},
    "borc-iliski-gen-0007": {"D": "Kişinin bir eşya üzerinde herkese karşı ileri sürebileceği, mutlak nitelikli ve ayni bir hak elde etmiş olması; alacak hakkı bu niteliktedir"},
    "borc-iliski-gen-0013": {"D": "Yalnızca bir tarafın borç altına girdiği, karşı tarafın ise bundan hiçbir menfaat sağlamadığı ve karşılık vermediği nitelikteki sözleşme"},
    "borc-iliski-gen-0016": {"E": "Zarara uğrayan kişinin, uğradığı zararı belgelerle ve tanıkla ispatlaması gerektiğini gösteren, ispat yükünü ona bırakan usul kuralı"},
    "borc-iliski-gen-0018": {"A": "Maddi zarar kişinin duygusal ve ruhsal kaybını; manevi zarar ise mal varlığındaki ölçülebilir eksilmeyi ifade eder ve ikisi bu yönden ayrılır"},
    "borc-iliski-gen-0021": {"A": "Borçlunun hiçbir biçimde yerine getirmesi gerekmeyen ve hukuk düzenince baştan itibaren tümüyle geçersiz sayılan nitelikteki yükümlülük"},
    "borc-iliski-gen-0022": {"B": "Asli edim yalnızca para borçlarını, yan edim ise yalnızca yapma borçlarını kapsar; bu ayrım edimin konusuna göre yapılmış bulunur"},
    "borc-iliski-gen-0024": {"B": "Parça borcunda edimin konusu türüyle belirlenirken; cins borcunda ferden belirlenmiş tek bir şey borçlanılır ve bu yüzden ikisi birbirinin tersidir"},
    "borc-iliski-gen-0025": {"A": "Failin, zarara yol açan davranışını kasten ya da ihmalle gerçekleştirmiş olması gerektiğine ilişkin ve aranması zorunlu olan unsur"},
    "borc-iliski-gen-0033": {"A": "Bir kişinin, kendisine verilmiş geçerli bir vekâlete dayanarak başkası adına ve onun hesabına hukuki işlem yapması; buna vekâletsiz iş görme denir"},
    "borc-iliski-gen-0035": {"A": "Zenginleşen kişi, iyiniyetli olsa dahi her koşulda zenginleşmenin başlangıçtaki tam tutarını eksiksiz iade eder; elden çıkan kısım indirilmez"},
    "borc-iliski-gen-0043": {"A": "Aynen tazmin zararın para ödenerek, nakden tazmin ise zarardan önceki durumun fiilen geri getirilmesiyle giderilmesidir; iki kavram bu yönden ayrılır"},
    "borc-iliski-gen-0049": {"D": "Zarar görenin kendi kusuru tazminatı iki katına çıkarır; fail bu durumda zararın iki mislini ödemekle yükümlü kalır ve indirim istenemez"},
    "borc-iliski-gen-0052": {"B": "Edimin baştan imkânsız olması sözleşmeyi hiçbir biçimde etkilemez; imkânsız bir edim de geçerli olarak borçlanılır ve ifası istenebilir"},
    "borc-iliski-gen-0055": {"C": "Alacaklı ile borçlunun aralarında anlaşarak borcu bütünüyle ortadan kaldırması ve alacağı kesin biçimde sona erdirmesi; buna takas denir"},
    "borc-iliski-gen-0056": {"B": "Borcun naklinde alacaklı, alacağın temlikinde ise borçlu değişir; iki kurumda da aynı taraf yer değiştirdiğinden ikisi eş anlamlıdır"},
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
