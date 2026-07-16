#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""İdari Yargıda Görev ve Yetki — 60 özgün konu havuzu sorusu."""
from topic_pack_builder import write_topic


def R(scenario, focus, correct, bank, why, ref, difficulty="medium"):
    return locals()


WRONG = {
    "merci": [
        "Uyuşmazlığın niteliğine bakılmaksızın bütün idari davaları ilk derece mahkemesi olarak Danıştay çözer",
        "İlk derece idari uyuşmazlıkların tamamı doğrudan bölge idare mahkemesinin tek hâkimince karara bağlanır",
        "Vergi, resim ve harç uyuşmazlıklarında görevli yargı yeri kural olarak genel görevli asliye hukuk mahkemesidir",
        "İdare mahkemeleri yalnız istinaf incelemesi yapar; iptal ve tam yargı davalarında ilk derece görevi bulunmaz",
        "Bölge idare mahkemesi yalnız danışma görüşü verir; istinaf başvurusu hakkında bağlayıcı karar veremez",
        "Tahkim yolu öngörülmeyen idari sözleşme uyuşmazlıkları her durumda iş mahkemesinin görev alanına girer",
        "Danıştayın temyiz görevi yerindelik denetimini de kapsar ve idarenin takdir yetkisini yeniden kullanmasına imkân verir",
        "Bir davanın vergi mahkemesinde görülmesi için taraflardan ikisinin de tacir ve uyuşmazlığın özel hukuk sözleşmesine dayalı olması gerekir",
    ],
    "yetki": [
        "Yetkili mahkeme her durumda davacının yerleşim yerindeki idare mahkemesidir; özel yetki kuralları uygulanmaz",
        "İdari davalarda yetki yalnız tarafların yapacağı sözleşmeyle belirlenir ve mahkemece kendiliğinden incelenemez",
        "Yetkili mahkeme idari işlemin uygulandığı her yerde seçimlik olarak belirlenir; işlemi yapan merciin yeri önem taşımaz",
        "Kamu görevlisine ilişkin bütün davalarda yetkili yer, görev yeriyle bağlantı aranmaksızın Ankara idare mahkemeleridir",
        "Taşınmazla ilgili idari davada taşınmazın bulunduğu yer yerine yalnız işlemi tebliğ eden birimin bulunduğu yer esas alınır",
        "Vergi uyuşmazlığında yetki, tarhiyatı yapan daireden bağımsız olarak mükellefin dilediği vergi mahkemesine aittir",
        "Tam yargı davasında zarar veya eylem yeri dikkate alınmaz; yalnız davalı idarenin merkezindeki mahkeme yetkilidir",
        "Yetki kamu düzeninden olmadığından davalı ilk itirazda bulunmazsa yetkisizlik hiçbir aşamada değerlendirilemez",
    ],
    "uyusmazlik": [
        "Aynı yargı çevresindeki idare ve vergi mahkemeleri arasındaki görev uyuşmazlığını ilk derece hukuk mahkemesi kesin çözer",
        "Mahkemeler arasındaki yetki tereddüdünde taraflar ortak bir mahkeme seçmedikçe dava kendiliğinden sona erer",
        "Bağlantı yalnız tarafların ve taleplerin tamamen aynı olması hâlinde kabul edilir; hukuki sebep ortaklığı yeterli değildir",
        "Görevsizlik kararı verildiğinde dosya hiçbir koşulda görevli idari yargı yerine gönderilemez ve yeniden dava açılamaz",
        "Merci tayini kararı yalnız tavsiye niteliğindedir; belirlenen mahkeme görevsizlik kararı vermekte serbesttir",
        "Farklı bölge idare mahkemesi çevrelerindeki yetki uyuşmazlığını uyuşmazlığa taraf belediye meclisi karara bağlar",
        "Bir davadaki hükmün diğer davayı etkilemesi bağlantı oluşturmaz; mutlaka dava konularının kelimesi kelimesine aynı olması gerekir",
        "Mahkeme görev ve yetkiyi yalnız tarafların açık talebi üzerine inceler; dosya üzerinden kendiliğinden inceleme yapamaz",
    ],
}


RULES = [
    R("Bir idare mahkemesi kararına karşı olağan istinaf başvurusu yapılmıştır. Başvuruyu hangi merci inceler?", "Bölge idare mahkemesinin temel yargısal görevi aşağıdakilerden hangisidir?", "İstinaf başvurusunu bölge idare mahkemesi inceler", "merci", "Bölge idare mahkemeleri, yargı çevrelerindeki idare ve vergi mahkemesi kararlarına yönelik istinaf başvurularını karara bağlar.", "2576 sayılı Kanun m.3/A", "easy"),
    R("Bir uyuşmazlık vergi mahkemesinin veya Danıştayın ilk derece görevi kapsamında değildir ve idari işlemin iptali istenmektedir. Görevli mahkeme hangisidir?", "İdare mahkemelerinin genel ilk derece görevi bakımından doğru ifade hangisidir?", "İdare mahkemesi görevlidir", "merci", "İdare mahkemeleri; vergi mahkemesi ve Danıştayın ilk derece görevine girenler dışındaki iptal ve tam yargı davalarını çözer.", "2576 sayılı Kanun m.5", "easy"),
    R("Belediyeye ait bir harcın tarhı ve cezasına karşı dava açılacaktır. Uyuşmazlık hangi ilk derece mahkemesinin görevine girer?", "Vergi mahkemelerinin görev alanını doğru gösteren seçenek hangisidir?", "Vergi mahkemesi görevlidir", "merci", "Vergi, resim, harç ve benzeri mali yükümler ile bunların zam ve cezalarına ilişkin davalar vergi mahkemesinde görülür.", "2576 sayılı Kanun m.6", "easy"),
    R("Bir bakanlığın ülke çapında uygulanacak düzenleyici işlemine karşı iptal davası açılacaktır. İlk derece mahkemesi hangisidir?", "Danıştayın ilk derece görevlerinden biri aşağıdakilerden hangisidir?", "Dava ilk derece olarak Danıştayda görülür", "merci", "Bakanlıkların ülke çapında uygulanacak düzenleyici işlemlerine karşı davalar Danıştayda ilk derece olarak görülür.", "2575 sayılı Danıştay Kanunu m.24/1-c"),
    R("Bir Cumhurbaşkanı kararının iptali istenmektedir. Davanın ilk derece yargı yeri nasıl belirlenir?", "Cumhurbaşkanı kararlarına karşı açılan idari davalarda görevli ilk derece mercii hangisidir?", "İlk derece görevi Danıştaya aittir", "merci", "Cumhurbaşkanı kararlarına karşı iptal ve tam yargı davaları Danıştayın ilk derece görevleri arasındadır.", "2575 sayılı Danıştay Kanunu m.24/1-a"),
    R("Dava konusu işlem birden çok idare mahkemesinin yetki alanına girmektedir. İlk derece görevi hangi mercidedir?", "Birden çok idare veya vergi mahkemesinin yetki alanına giren işlerde görevli ilk derece mercii hangisidir?", "İlk derece incelemesini Danıştay yapar", "merci", "Birden çok idare veya vergi mahkemesinin yetki alanına giren işler Danıştayda ilk derece olarak görülür.", "2575 sayılı Danıştay Kanunu m.24/1-e", "hard"),
    R("Tahkim yolu öngörülmeyen bir kamu hizmeti imtiyaz sözleşmesinden idari uyuşmazlık doğmuştur. Yargılamayı hangi merci yapar?", "Tahkimsiz kamu hizmeti imtiyaz sözleşmelerinden doğan idari davalarda görevli merci hangisidir?", "Dava Danıştayda görülür", "merci", "Tahkim yolu öngörülmeyen kamu hizmeti imtiyaz şartlaşma ve sözleşmelerinden doğan idari davalar Danıştayın ilk derece görevindedir.", "2575 sayılı Danıştay Kanunu m.24"),
    R("İdare ve vergi mahkemeleri aynı yargı çevresinde görev konusunda farklı kararlar vermiştir. Uyuşmazlığı kim kesin karara bağlar?", "Aynı yargı çevresindeki idare ve vergi mahkemeleri arasındaki görev ve yetki uyuşmazlığını hangi merci çözer?", "İlgili bölge idare mahkemesi çözer", "uyusmazlik", "Bölge idare mahkemesi, kendi yargı çevresindeki idare ve vergi mahkemeleri arasındaki görev ve yetki uyuşmazlıklarını kesin karara bağlar.", "2576 sayılı Kanun m.3/A-b"),
    R("Kanunda özel bir yetki kuralı bulunmayan idari işleme karşı dava açılacaktır. İşlemi yapan merci Konya'dadır. Yetkili yer neresidir?", "İYUK'taki genel yetki kuralı aşağıdakilerden hangisidir?", "İşlemi yapan merciin bulunduğu yer mahkemesi", "yetki", "Özel yetki kuralı yoksa yetkili idare mahkemesi, dava konusu işlemi veya sözleşmeyi yapan idari merciin bulunduğu yerdedir.", "2577 sayılı İYUK m.32", "easy"),
    R("İdari sözleşmeyi yapan idari merci İzmir'dedir ve özel kanunda farklı yetki belirlenmemiştir. Dava nerede açılır?", "İdari sözleşmeden doğan davada özel hüküm yoksa genel yetki hangi bağlantıya dayanır?", "Sözleşmeyi yapan merciin bulunduğu yere", "yetki", "İYUK m.32, işlem yanında idari sözleşmeyi yapan merciin bulunduğu yeri de genel yetki ölçütü kabul eder.", "2577 sayılı İYUK m.32"),
    R("Kamu görevlisinin Ankara'dan Bursa'ya nakline karşı dava açılacaktır. Yetkili mahkeme nasıl belirlenir?", "Atama ve nakil davalarında kamu görevlisine tanınan yetki seçeneği hangisidir?", "Yeni veya eski görev yeri mahkemesi", "yetki", "Atama ve nakille ilgili davalar yeni veya eski görev yeri idare mahkemesinde açılabilir.", "2577 sayılı İYUK m.33/1"),
    R("Görevine son verilen kamu görevlisi son olarak Eskişehir'de çalışmıştır. Özel hüküm yoksa yetkili mahkeme neresidir?", "Göreve son verme ve emeklilik işlemlerinde yetkili idare mahkemesi hangi yere göre belirlenir?", "Son görev yerindeki idare mahkemesi", "yetki", "Göreve son verme, emekli etme ve görevden uzaklaştırma davalarında son görev yeri mahkemesi yetkilidir.", "2577 sayılı İYUK m.33/2"),
    R("Görevle ilişiği kesilmeyen memura verilen disiplin cezası dava konusu yapılacaktır. Yetkili mahkeme hangisidir?", "Görevle ilişiği kesmeyen disiplin cezasına karşı davada yetki hangi yere aittir?", "Görevli bulunduğu yer idare mahkemesine", "yetki", "Görevle ilişiği kesmeyen disiplin cezalarında ilgilinin görevli bulunduğu yer idare mahkemesi yetkilidir.", "2577 sayılı İYUK m.33/3"),
    R("Bir taşınmaza ilişkin imar planı uygulaması dava konusu edilmiştir. Yetkili idare mahkemesi nerededir?", "İmar ve kamulaştırma gibi taşınmaz uyuşmazlıklarında özel yetki kuralı hangisidir?", "Taşınmazın bulunduğu yer mahkemesi", "yetki", "Taşınmaz mevzuatının uygulanmasından doğan idari davalarda taşınmazın bulunduğu yer idare mahkemesi yetkilidir.", "2577 sayılı İYUK m.34"),
    R("İdarece el konulan belirli bir taşınır mal hakkında idari dava açılacaktır. Özel yetki kuralı hangi yeri gösterir?", "Taşınır mallara ilişkin idari davalarda yetki hangi bağlantıya göre belirlenir?", "Taşınırın bulunduğu yer mahkemesine göre", "yetki", "Taşınır mallara ilişkin davalarda taşınırın bulunduğu yer idare mahkemesi yetkilidir.", "2577 sayılı İYUK m.35"),
    R("Bir idari eylem Antalya'da gerçekleşmiş ve zarar burada doğmuştur. Tam yargı davasında öncelikli özel yetki hangi yere aittir?", "İdari eylemden doğan tam yargı davasında yetki için esas alınan yer hangisidir?", "Eylemin yapıldığı yer mahkemesi", "yetki", "İdari eylem veya hizmetten doğan zararda hizmetin görüldüğü ya da eylemin yapıldığı yer mahkemesi yetkilidir.", "2577 sayılı İYUK m.36/b"),
    R("Tam yargı davasında İYUK m.36'nın zarar doğuran uyuşmazlık ve eylem yeri ölçütleri uygulanamamaktadır. Sıradaki ölçüt nedir?", "Tam yargı davalarında diğer özel bağlantılar yoksa yetki hangi yere geçer?", "Davacının ikametgâhındaki mahkemeye", "yetki", "İdari sözleşme dışındaki tam yargı davalarında önceki özel ölçütler uygulanamazsa davacının ikametgâhı esas alınır.", "2577 sayılı İYUK m.36/c", "hard"),
    R("Bir vergi dairesinin yaptığı tarhiyat ve kestiği ceza dava konusu edilmiştir. Yetkili vergi mahkemesi nasıl belirlenir?", "Tarh ve ceza uyuşmazlığında vergi mahkemesinin yetkisi hangi dairenin yerine bağlanmıştır?", "Tarhı yapan ve cezayı kesen dairenin yerine", "yetki", "Vergi uyuşmazlığında tarh ve tahakkuk ettiren ya da ceza kesen dairenin bulunduğu yer vergi mahkemesi yetkilidir.", "2577 sayılı İYUK m.37/a"),
    R("6183 sayılı Kanun uyarınca düzenlenen ödeme emrine karşı dava açılacaktır. Yetkili vergi mahkemesi nerededir?", "Ödeme emri uyuşmazlığında özel yetkiyi belirleyen idari birim hangisidir?", "Ödeme emrini düzenleyen dairenin bulunduğu yer", "yetki", "Amme alacağının takibindeki ödeme emri uyuşmazlığında emri düzenleyen dairenin bulunduğu yerdeki vergi mahkemesi yetkilidir.", "2577 sayılı İYUK m.37/c"),
    R("Aynı hukuki sebepten doğan iki idari davadan biri hakkında verilecek hüküm diğerini etkileyecektir. Bu ilişki nasıl adlandırılır?", "İYUK'a göre bağlantılı davayı belirleyen ölçüt hangisidir?", "Davalar arasında bağlantı vardır", "uyusmazlik", "Aynı maddi veya hukuki sebepten doğan ya da birindeki hükmün diğerini etkileyeceği davalar bağlantılıdır.", "2577 sayılı İYUK m.38"),
    R("Aynı mahkemedeki iki dava arasında bağlantı bulunduğu düşünülmektedir. Mahkeme taraf talebi olmadan bağlantıyı değerlendirebilir mi?", "Bağlantının tespitinde mahkemenin kendiliğinden hareket yetkisi var mıdır?", "Mahkeme bağlantıya resen karar verebilir", "uyusmazlik", "Bağlantının varlığına taraf istemi üzerine veya doğrudan doğruya mahkemece karar verilebilir.", "2577 sayılı İYUK m.38/2"),
    R("İki mahkeme aynı davaya bakmaya kendisini yetkili saymıştır ve aynı bölge idare mahkemesi çevresindedir. Merci tayinini kim yapar?", "Aynı yargı çevresindeki olumlu yetki uyuşmazlığında merci tayini kime aittir?", "O yargı çevresindeki bölge idare mahkemesine", "uyusmazlik", "Aynı yargı çevresindeki mahkemeler için merci tayini o bölge idare mahkemesince yapılır.", "2577 sayılı İYUK m.44/1-a"),
    R("Yetki uyuşmazlığı farklı bölge idare mahkemelerinin yargı çevrelerindeki mahkemeler arasında çıkmıştır. Merci tayini nereye aittir?", "Aynı bölge idare mahkemesi çevresi dışında kalan merci tayininde görevli üst merci hangisidir?", "Danıştaya", "uyusmazlik", "Aynı yargı çevresi dışındaki hâllerde görevli ve yetkili mahkemeyi merci tayini yoluyla Danıştay belirler.", "2577 sayılı İYUK m.44/1-b"),
    R("Adli yargıda açılan dava görev yönünden reddedilmiş ve uyuşmazlık idari yargının görevine girmektedir. Başvuru tarihinin korunması için ne yapılır?", "Adli yargının görevsizlik kararından sonra idari yargıya başvuru bakımından temel kural hangisidir?", "Kesinleşmeden sonra otuz gün içinde dava açılır", "uyusmazlik", "Görevsizlik kararının kesinleşmesini izleyen günden başlayarak otuz gün içinde görevli idari mahkemede dava açılabilir; ilk başvuru tarihi korunur.", "2577 sayılı İYUK m.9"),
    R("İdari yargı mahkemesi görev alanı dışında kalan davayı ilk incelemede saptamıştır. Görev kamu düzenine ilişkin olduğundan nasıl hareket eder?", "İdari yargıda görev incelemesinin niteliğini doğru açıklayan ifade hangisidir?", "Görev hususu resen incelenir", "uyusmazlik", "Görev ve yetki, ilk incelemede mahkemece kendiliğinden değerlendirilen usul koşullarıdır.", "2577 sayılı İYUK m.14-15"),
    R("Yetkili mahkeme davaya bakmaya hukuki engel bulunduğunu bildirmiştir. Davanın görülebilmesi için hangi kurum işletilir?", "Mahkemenin davaya bakmasına fiili veya hukuki engel çıktığında başvurulan çözüm hangisidir?", "Merci tayini yapılır", "uyusmazlik", "Yetkili mahkemenin davaya bakmasına fiili veya hukuki engel çıkarsa dosya görevli üst mercie merci tayini için gönderilir.", "2577 sayılı İYUK m.44"),
]


PREMISES = [
    {"stem": "İdari yargı mercileri hakkında hangileri doğrudur?\n\nI. Bölge idare mahkemesi istinaf başvurularını inceler\n\nII. Vergi mahkemesi vergi cezalarına ilişkin davaları çözer\n\nIII. İdare mahkemesi kanundaki sınırlar içinde genel görevli ilk derece mahkemesidir", "correct": "I, II ve III", "why": "Üç ifade de idari yargı düzenindeki temel görev paylaşımını doğru gösterir.", "ref": "2575 m.24; 2576 m.3/A, m.5-6"},
    {"stem": "İYUK'taki yetki kuralları bakımından hangileri doğrudur?\n\nI. Yetki kamu düzenindendir\n\nII. Özel hüküm yoksa işlemi yapan merciin yeri esas alınır\n\nIII. Taraflar anlaşarak kanuni yetkiyi her durumda değiştirebilir", "correct": "I ve II", "why": "İdari yargıda yetki kamu düzenindendir ve özel hüküm yoksa işlemi yapan merciin bulunduğu yer esas alınır; taraf anlaşması kanuni yetkiyi değiştiremez.", "ref": "2577 sayılı İYUK m.32"},
    {"stem": "Kamu görevlilerine ilişkin yetki bakımından hangileri doğrudur?\n\nI. Nakil davası yeni veya eski görev yerinde açılabilir\n\nII. Göreve son verme davasında son görev yeri esas alınır\n\nIII. Görevle ilişiği kesmeyen disiplin cezasında görevli bulunulan yer esas alınır", "correct": "I, II ve III", "why": "Üç ifade de kamu görevlileri için İYUK m.33'te öngörülen özel yetki kurallarını yansıtır.", "ref": "2577 sayılı İYUK m.33"},
    {"stem": "Özel yetki kuralları hakkında hangileri doğrudur?\n\nI. İmar davasında taşınmazın bulunduğu yer esastır\n\nII. Taşınır mal davasında davacının yerleşim yeri zorunludur\n\nIII. Ödeme emrinde emri düzenleyen dairenin yeri esastır", "correct": "I ve III", "why": "Taşınmazın bulunduğu yer ve ödeme emrini düzenleyen dairenin bulunduğu yer özel yetkidir. Taşınırda ise malın bulunduğu yer esas alınır.", "ref": "2577 sayılı İYUK m.34-35, m.37"},
    {"stem": "Bağlantılı davalar bakımından hangileri doğrudur?\n\nI. Aynı maddi sebepten doğma bağlantı oluşturabilir\n\nII. Bir davadaki hükmün diğerini etkilemesi bağlantı oluşturabilir\n\nIII. Bağlantıya yalnız tarafların ortak talebiyle karar verilebilir", "correct": "I ve II", "why": "Aynı maddi veya hukuki sebep ya da hükümlerin birbirini etkilemesi bağlantı ölçütüdür. Mahkeme resen de karar verebilir.", "ref": "2577 sayılı İYUK m.38"},
    {"stem": "Merci tayini hakkında hangileri doğrudur?\n\nI. Aynı yargı çevresindeki uyuşmazlıkta bölge idare mahkemesi yetkilidir\n\nII. Diğer hâllerde Danıştay yetkilidir\n\nIII. Merci tayini kararı yalnız tavsiye niteliğindedir", "correct": "I ve II", "why": "İYUK m.44, aynı yargı çevresinde bölge idare mahkemesini, diğer hâllerde Danıştayı yetkilendirir; verilen karar kesindir, tavsiye değildir.", "ref": "2577 sayılı İYUK m.44"},
    {"stem": "Danıştayın ilk derece görevi bakımından hangileri doğrudur?\n\nI. Cumhurbaşkanı kararlarına karşı davalar kapsamdadır\n\nII. Ülke çapında uygulanacak bakanlık düzenleyici işlemleri kapsamdadır\n\nIII. Her belediye encümeni kararı doğrudan Danıştayda dava edilir", "correct": "I ve II", "why": "Cumhurbaşkanı kararları ve ülke çapındaki bakanlık düzenleyici işlemleri Danıştayın ilk derece görevindedir; belediye encümeni kararları için böyle genel bir kural yoktur.", "ref": "2575 sayılı Danıştay Kanunu m.24"},
    {"stem": "İdari yargıda görev bakımından hangileri doğrudur?\n\nI. İdare mahkemeleri genel görevli ilk derece mahkemeleridir\n\nII. Vergi mahkemelerinin görev alanı kanunda ayrıca belirlenmiştir\n\nIII. Bölge idare mahkemesi olağan olarak istinaf incelemesi yapar", "correct": "I ve III", "why": "İdare mahkemeleri, Danıştay ve vergi mahkemesi dışındaki idari davalarda genel görevli; bölge idare mahkemesi istinaf merciidir. İkinci ifade de gerçekte doğrudur; bu nedenle doğru küme I, II ve III olmalıydı ifadesi bu soruda bilinçli olarak kapsam dışı değildir.", "ref": "2576 sayılı Kanun m.3/A, m.5-6"},
]

# Son öncüllü soruda üç ifade de doğrudur; hedef dağılımı korumak için II yanlış olmalı.
PREMISES[-1]["stem"] = "İdari yargıda görev bakımından hangileri doğrudur?\n\nI. İdare mahkemeleri kanunda belirtilen kapsamda genel görevli ilk derece mahkemeleridir\n\nII. Vergi mahkemeleri özel hukuk sözleşmelerinden doğan bütün alacak davalarını çözer\n\nIII. Bölge idare mahkemesi olağan olarak istinaf incelemesi yapar"
PREMISES[-1]["why"] = "İdare mahkemeleri genel görevli ilk derece mahkemeleridir ve bölge idare mahkemesi istinaf merciidir. Özel hukuk sözleşmelerinden doğan bütün alacak davaları vergi mahkemesinin görevi değildir."


if __name__ == "__main__":
    write_topic(
        lesson_id="idari_yargilama_hukuku", topic_id="idari_yargi_gorev_yetki",
        label="İdari Yargıda Görev ve Yetki", slug="idari_yargi_gorev_yetki",
        prefix="kh-iy-gorev", seed=20261001, legislation_version="2575, 2576 ve 2577 sayılı Kanunlar (16.07.2026)",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG,
    )
