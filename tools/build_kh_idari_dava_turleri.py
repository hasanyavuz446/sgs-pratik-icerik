#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""İdari Dava Türleri — İYUK m.2, m.7, m.10, m.12-13 odaklı 60 soru."""
from topic_pack_builder import write_topic


def R(scenario, focus, correct, bank, why, ref, difficulty="medium"):
    return locals()


WRONG = {
    "tur": [
        "Dava yalnız idarenin cezalandırılmasını amaçlayan bir ceza davası olarak adli yargıda açılabilir",
        "İdari işlemin hukuka uygunluğu incelenmeden yalnız ekonomik yararlılığı hakkında bağlayıcı görüş verilir",
        "Davacıdan menfaat veya hak bağlantısı aranmadan herkes adına soyut norm denetimi yapılması zorunludur",
        "Uyuşmazlık idari nitelikte olsa bile sadece tarafların seçtiği özel hakem kurulu kesin karar verebilir",
        "Mahkeme idari işlemin yerine geçerek aynı konuda yeni bir işlem kurar ve idarenin takdirini doğrudan kullanır",
        "Dava türü ne olursa olsun tek mümkün sonuç yalnız parasal tazminattır; işlemin iptali istenemez",
        "İdari eylem ve işlemlerden doğan uyuşmazlıkların tamamı görev ayrımı yapılmadan tüketici mahkemesinde görülür",
        "İdari sözleşmelerden doğan her uyuşmazlık tahkim şartı bulunup bulunmadığına bakılmadan idari yargıda görülür",
    ],
    "unsur": [
        "İşlemi yapan makamın kamu yararı bakımından daha kârlı bir seçeneği tercih etmemiş olması tek başına bu unsuru sakatlar",
        "İdarenin işlemden sonra bütçe imkânının azalması, kanuni unsurlardan bağımsız olarak işlemi kendiliğinden yok hükmünde kılar",
        "Davacının işlemi beğenmemesi, somut hukuka aykırılık aranmadan bu unsur yönünden iptal için yeterlidir",
        "Mahkemenin idare yerine geçerek yeni gerekçe üretmesi ve işlemi bu gerekçeyle sürdürmesi bu unsurun denetimidir",
        "İşlemin sonuçlarının siyasal bakımdan elverişsiz görülmesi, hukuki ölçüt aranmadan bu unsurun ihlali sayılır",
        "Yetkili makamın işlem yapmış olması hâlinde diğer bütün unsurların kanuna aykırılığı önemini tamamen kaybeder",
        "İşlemin sözlü veya yazılı olmasından bağımsız olarak bütün usul kuralları yalnız tavsiye niteliğindedir",
        "İdari işlemin amacı, sebebi ve konusu arasında hiçbir hukuki bağ kurulamaz; unsurlar ayrı davalarda incelenir",
    ],
    "sonuc": [
        "İptal kararı yalnız davacıya gelecekte uygulanır; işlemin tesis edildiği tarihe ve diğer ilgililere hiçbir etkisi olmaz",
        "Tam yargı davasında zarar ve nedensellik bağı araştırılmaz; idarenin her işleminde otomatik tazminata hükmedilir",
        "İptal davası açılması işlemin yürütmesini kendiliğinden durdurur ve ayrıca karar verilmesine gerek bırakmaz",
        "İptal ve tam yargı talepleri hiçbir koşulda aynı dilekçede ileri sürülemez; kanun bunu mutlak olarak yasaklar",
        "İdari eylemden doğan zarar için idareye ön başvuru yapılmadan her zaman doğrudan tam yargı davası açılması zorunludur",
        "Düzenleyici işlem süresinde dava edilmemişse daha sonra uygulama işlemiyle birlikte hiçbir şekilde ileri sürülemez",
        "Mahkeme iptal davasında hukuka uygunluk yerine yalnız yerindelik incelemesi yaparak en yararlı işlemi seçer",
        "İdari işlemden doğan zarar için önce iptal davası açılması mutlak şarttır; doğrudan tam yargı yolu kapalıdır",
    ],
}


RULES = [
    R("Bir ruhsat iptalinin hukuka aykırı olduğunu ileri süren ve işlemle güncel menfaati zedelenen kişi hangi dava türüne başvurur?", "İdari işlemin hukuka aykırılığı nedeniyle hukuk düzeninden kaldırılmasını amaçlayan dava hangisidir?", "İptal davası", "tur", "İptal davası, menfaati ihlal edilen kişinin idari işlemin hukuka aykırılığı nedeniyle ortadan kaldırılmasını istemesidir.", "2577 sayılı İYUK m.2/1-a", "easy"),
    R("İdari eylem nedeniyle bedensel zarara uğrayan kişinin maddi ve manevi kaybını gidermek için açacağı dava hangisidir?", "Kişisel hakkı doğrudan ihlal edilen kişinin zararının giderilmesini amaçlayan idari dava hangisidir?", "Tam yargı davası", "tur", "İdari eylem veya işlem nedeniyle kişisel hakkı doğrudan ihlal edilen kişi tam yargı davası açabilir.", "2577 sayılı İYUK m.2/1-b", "easy"),
    R("Tahkim yolu öngörülmeyen kamu hizmeti idari sözleşmesinden taraflar arasında uyuşmazlık çıkmıştır. Dava türü nasıl nitelendirilir?", "İYUK m.2'de üçüncü idari dava türü olarak düzenlenen uyuşmazlık hangisidir?", "İdari sözleşmeden doğan dava", "tur", "Kamu hizmetinin yürütülmesi için yapılan idari sözleşmelerden doğan taraf uyuşmazlıkları, tahkim istisnası dışında idari dava türüdür.", "2577 sayılı İYUK m.2/1-c"),
    R("Bir idari işlem davacının yalnız meşru, kişisel ve güncel menfaatini zedelemiştir; doğrudan kişisel hak ihlali kanıtlanamamıştır. Hangi dava uygundur?", "İptal davasında davacı ile işlem arasındaki bağ için aranan temel ölçüt nedir?", "Menfaat ihlali yeterlidir", "tur", "İptal davasında kişisel hakkın doğrudan ihlali değil, meşru ve güncel menfaat ilişkisinin bulunması aranır.", "2577 sayılı İYUK m.2/1-a"),
    R("İdarenin eylemi kişinin malvarlığında doğrudan kayba yol açmıştır. Tam yargı davası ehliyeti bakımından hangi bağ aranır?", "Tam yargı davasını iptal davasından ayıran davacı bağlantısı hangisidir?", "Kişisel hakkın doğrudan ihlali", "tur", "Tam yargı davası, idari eylem veya işlem nedeniyle kişisel hakkı doğrudan ihlal edilenlerce açılır.", "2577 sayılı İYUK m.2/1-b"),
    R("Bir işlemin kanunen başka makama ait olmasına rağmen yetkisiz bir birimce tesis edildiği ileri sürülmektedir. İptal sebebi hangi unsura ilişkindir?", "İşlemi tesis eden makamın kanuni görev alanını ifade eden idari işlem unsuru hangisidir?", "Yetki unsuru", "unsur", "Yetki unsuru, idari işlemi hangi makamın ve hangi görev alanında tesis edebileceğini gösterir.", "2577 sayılı İYUK m.2/1-a", "easy"),
    R("Kanunun zorunlu tuttuğu kurul görüşü alınmadan idari işlem yapılmıştır. Hukuka aykırılık öncelikle hangi unsurdadır?", "İdari işlemin hazırlanması ve açıklanmasında uyulacak usul kurallarını ifade eden unsur hangisidir?", "Şekil unsuru", "unsur", "Zorunlu usul ve biçim kurallarına uyulmaması işlemin şekil unsurunu sakatlar.", "2577 sayılı İYUK m.2/1-a"),
    R("Disiplin cezasına dayanak gösterilen olay gerçekte hiç gerçekleşmemiştir. İptal denetimi hangi unsura yönelir?", "İdareyi işlem yapmaya sevk eden maddi ve hukuki olguları ifade eden unsur hangisidir?", "Sebep unsuru", "unsur", "İdari işlemin sebebi, işlemi doğuran maddi olay ile hukuki dayanağın gerçek ve hukuka uygun olmasını gerektirir.", "2577 sayılı İYUK m.2/1-a"),
    R("Kanunun izin verdiğinden farklı bir hukuki sonuç doğuran idari karar alınmıştır. İptal sebebi hangi unsurla ilgilidir?", "İdari işlemin hukuk âleminde meydana getirdiği sonucu ifade eden unsur hangisidir?", "Konu unsuru", "unsur", "Konu, işlemin doğurduğu hukuki sonuçtur; kanunun öngörmediği sonuç konu yönünden hukuka aykırılık oluşturur.", "2577 sayılı İYUK m.2/1-a"),
    R("Kamu yararı yerine belirli bir kişiye çıkar sağlamak amacıyla yetki kullanılmıştır. Hangi unsur sakatlanmıştır?", "İdari işlemin kamu yararı doğrultusundaki nihai yönelimini ifade eden unsur hangisidir?", "Maksat unsuru", "unsur", "İdari işlemlerde genel amaç kamu yararıdır; yetkinin kişisel çıkar için kullanılması maksat sakatlığıdır.", "2577 sayılı İYUK m.2/1-a"),
    R("Mahkeme, idari işlemin hukuka uygunluğunu denetlemek yerine hangi seçeneğin ekonomik olarak daha yararlı olduğuna karar vermek istemektedir. Bu mümkün müdür?", "İdari yargı yetkisinin sınırlarından biri aşağıdakilerden hangisidir?", "Yerindelik denetimi yapılamaz", "tur", "İdari yargı hukuka uygunluğu denetler; idarenin tercihinin yararlılığına ilişkin yerindelik denetimi yapamaz.", "2577 sayılı İYUK m.2/2"),
    R("Mahkeme iptal ettiği işlemin yerine geçecek yeni ruhsat koşullarını kendisi belirlemek istemektedir. İYUK bakımından sonuç nedir?", "İdari yargı merciinin idari işlem niteliğinde karar vermesine ilişkin kural hangisidir?", "İdari işlem niteliğinde karar veremez", "tur", "Mahkeme hukuka uygunluğu denetler; idare yerine geçerek idari eylem veya işlem niteliğinde karar kuramaz.", "2577 sayılı İYUK m.2/2"),
    R("Kanunun idareye bıraktığı iki hukuka uygun seçenekten hangisinin kullanılacağını mahkeme doğrudan belirlemek istemektedir. Bu yaklaşım nasıldır?", "İdari yargı kararının idarenin takdir yetkisi üzerindeki sınırı hangisidir?", "Takdir yetkisini kaldıracak karar verilemez", "tur", "Yargı, takdirin hukuka uygunluğunu denetleyebilir; fakat idarenin takdir yetkisini tümüyle kaldıracak biçimde karar veremez.", "2577 sayılı İYUK m.2/2"),
    R("Hak ihlaline yol açan idari işleme karşı kişi hem işlemin kaldırılmasını hem zararının giderilmesini istemektedir. Talepler nasıl ileri sürülebilir?", "İdari işlemden doğan iptal ve tam yargı taleplerinin birlikte ileri sürülmesi mümkün müdür?", "İptal ve tam yargı davaları birlikte açılabilir", "sonuc", "İlgili, hak ihlal eden işlem nedeniyle iptal ve tam yargı davalarını birlikte açabilir.", "2577 sayılı İYUK m.12"),
    R("Hak ihlal eden idari işlem nedeniyle kişi zararının giderilmesini istiyor ancak işlemin iptalini talep etmiyor. İYUK m.12 hangi yolu tanır?", "İdari işlemden doğan zarar için önce iptal davası açılması zorunlu mudur?", "Doğrudan tam yargı davası açılabilir", "sonuc", "İYUK m.12, ilgiliye doğrudan tam yargı davası açma seçeneği tanır; önce iptal davası zorunlu değildir.", "2577 sayılı İYUK m.12"),
    R("Kişi önce iptal davası açmış ve karar kendisine tebliğ edilmiştir. İşlemden doğan zarar için hangi imkân korunur?", "Önce iptal davası açan kişinin sonradan tam yargı davası açmasına ilişkin kural hangisidir?", "Kararın tebliğinden sonra süresinde tam yargı davası açabilir", "sonuc", "İptal davasının karara bağlanmasından sonra kararın veya kanun yolu kararının tebliğinden itibaren dava süresi içinde tam yargı davası açılabilir.", "2577 sayılı İYUK m.12"),
    R("İdari işlem uygulanmış ve zarar uygulama tarihinde doğmuştur. Önce iptal davası açan kişi tam yargı talebini hangi olaya bağlayabilir?", "İşlemin icrası nedeniyle doğan zararda sonraki tam yargı davası için süre hangi tarihle ilişkilendirilebilir?", "İcra tarihinden itibaren", "sonuc", "İşlemin icrası nedeniyle zarar doğmuşsa tam yargı davası icra tarihinden başlayarak dava süresi içinde açılabilir.", "2577 sayılı İYUK m.12"),
    R("Belediyenin fiilî çalışması bir taşınmaza zarar vermiş, önceden dava edilebilir yazılı işlem bulunmamaktadır. Dava öncesinde ne yapılır?", "İdari eylemden doğan tam yargı davasında kural olarak zorunlu ilk adım hangisidir?", "İdareye hakların yerine getirilmesi için başvurulur", "sonuc", "İdari eylemden doğan zarar için dava açmadan önce ilgili idareye hakkın yerine getirilmesi amacıyla ön başvuru yapılır.", "2577 sayılı İYUK m.13"),
    R("İdari eylemden zarar gören kişi eylemi ve faili öğrendiği tarihten sonra başvuru yapacaktır. Kanun hangi iki üst sınırı birlikte öngörür?", "İdari eylemden doğan ön başvurunun yapısal süreleri hangileridir?", "Öğrenmeden itibaren bir yıl, eylemden itibaren beş yıl", "sonuc", "İYUK m.13 başvuruyu, eylemin öğrenilmesinden itibaren bir yıl ve her hâlde eylem tarihinden itibaren beş yıl ile sınırlar.", "2577 sayılı İYUK m.13", "hard"),
    R("İdari eylem başvurusuna idare kısmen olumsuz cevap vermiştir. Zarar gören ne yapabilir?", "İdari eylem ön başvurusunun kısmen reddi sonrasında tanınan yol hangisidir?", "Ret kısmı için dava açabilir", "sonuc", "İstek kısmen veya tamamen reddedilirse ret işleminin tebliğinden sonra dava süresi içinde tam yargı davası açılabilir.", "2577 sayılı İYUK m.13"),
    R("İdari eylem nedeniyle yapılan zorunlu ön başvuruya idare süresinde cevap vermemiştir. Bu susma hangi sonucu doğurur?", "İYUK m.13 başvurusunda idarenin sessiz kalması dava yolunu nasıl etkiler?", "İstek reddedilmiş sayılır ve dava yolu açılır", "sonuc", "Kanuni cevap süresinde yanıt verilmemesi zımni ret oluşturur; ilgili dava açma süresi içinde tam yargı davasına başvurabilir.", "2577 sayılı İYUK m.13"),
    R("İlan edilen düzenleyici işlem süresinde dava edilmemiş, daha sonra kişiye bu düzenlemeye dayalı uygulama işlemi yapılmıştır. Hangi yol mümkündür?", "Düzenleyici işlemin uygulanması üzerine dava hakkına ilişkin kural hangisidir?", "Uygulama işlemiyle birlikte düzenleyici işlem de dava edilebilir", "sonuc", "Uygulama üzerine ilgili, düzenleyici işleme, uygulama işlemine veya her ikisine birlikte dava açabilir.", "2577 sayılı İYUK m.7/4"),
    R("Düzenleyici işlem daha önce iptal edilmemiştir; buna dayanan bireysel uygulama işleminde hukuka aykırılık ileri sürülmektedir. Bu durum davayı engeller mi?", "Düzenleyici işlemin iptal edilmemiş olmasının uygulama işlemine etkisi hangisidir?", "Uygulama işleminin iptaline engel olmaz", "sonuc", "Düzenleyici işlemin daha önce iptal edilmemiş olması, ona dayalı uygulama işleminin hukuka aykırılık nedeniyle iptaline engel değildir.", "2577 sayılı İYUK m.7/4"),
    R("İptal davası sonucunda işlem hukuka aykırı bulunarak kaldırılmıştır. Kararın temel işlevi nedir?", "İptal davasının objektif hukuka uygunluk denetimindeki sonucu hangisidir?", "Hukuka aykırı işlemi hukuk düzeninden kaldırmak", "sonuc", "İptal davasının temel işlevi hukuka aykırı idari işlemi hukuk düzeninden çıkarmaktır; tazminat tam yargının konusudur.", "2577 sayılı İYUK m.2/1-a"),
    R("Tam yargı davasında zarar kanıtlanmış ancak idari eylem ile zarar arasında bağ kurulamamıştır. Tazminat için eksik olan unsur hangisidir?", "İdarenin tazmin sorumluluğunda zarar ile idari faaliyet arasında aranan bağ hangisidir?", "Nedensellik bağı", "sonuc", "Tam yargı davasında gerçek zarar yanında zararın idari faaliyetle uygun nedensellik bağı içinde olması gerekir.", "2577 sayılı İYUK m.2/1-b; idari sorumluluğun genel esasları"),
    R("İmtiyaz sözleşmesinde uyuşmazlık için geçerli tahkim yolu açıkça öngörülmüştür. İYUK m.2/1-c kapsamı bakımından sonuç nedir?", "İdari sözleşme davaları bakımından kanunda belirtilen tahkim istisnası hangisidir?", "Uyuşmazlık idari sözleşme davası kapsamı dışında kalır", "tur", "Tahkim yolu öngörülen imtiyaz şartlaşma ve sözleşmelerinden doğan uyuşmazlıklar İYUK m.2/1-c kapsamındaki idari sözleşme davalarından ayrılmıştır.", "2577 sayılı İYUK m.2/1-c", "hard"),
]


PREMISES = [
    {"stem": "İdari dava türleri bakımından hangileri doğrudur?\n\nI. İptal davası idari işlemin hukuka aykırılığına yönelir\n\nII. Tam yargı davası kişisel hak ihlalinin giderilmesini amaçlar\n\nIII. Tahkim istisnası dışındaki idari sözleşme uyuşmazlıkları İYUK'ta sayılmıştır", "correct": "I, II ve III", "why": "Üç ifade de İYUK m.2'de düzenlenen idari dava türlerini doğru açıklar.", "ref": "2577 sayılı İYUK m.2"},
    {"stem": "İptal davası bakımından hangileri doğrudur?\n\nI. Menfaat ihlali aranır\n\nII. Yalnız idari işlemlere yönelir\n\nIII. Tek amacı parasal zararı hesaplamaktır", "correct": "I ve II", "why": "İptal davasında menfaat ihlali ve dava konusu yapılabilir idari işlem aranır; parasal zararın giderimi tam yargı davasının işlevidir.", "ref": "2577 sayılı İYUK m.2/1-a"},
    {"stem": "Tam yargı davası bakımından hangileri doğrudur?\n\nI. İdari eylemden doğabilir\n\nII. İdari işlemden doğabilir\n\nIII. Kişisel hakkın doğrudan ihlali aranır", "correct": "I, II ve III", "why": "Tam yargı davası idari eylem veya işlemden doğabilir ve kişisel hakkı doğrudan ihlal edilenlerce açılır.", "ref": "2577 sayılı İYUK m.2/1-b"},
    {"stem": "İptal sebepleri bakımından hangileri doğrudur?\n\nI. Yetkisiz makamın işlem yapması yetki unsuruyla ilgilidir\n\nII. Zorunlu usulün atlanması maksat unsuruyla ilgilidir\n\nIII. Kamu yararı dışındaki amaç maksat unsuruyla ilgilidir", "correct": "I ve III", "why": "Yetkisiz makam yetki, kamu yararı dışındaki amaç maksat unsurunu sakatlar. Zorunlu usulün atlanması maksat değil şekil unsuruyla ilgilidir.", "ref": "2577 sayılı İYUK m.2/1-a"},
    {"stem": "İdari yargı yetkisinin sınırları bakımından hangileri doğrudur?\n\nI. Hukuka uygunluk denetimi yapılır\n\nII. Yerindelik denetimi yapılamaz\n\nIII. Mahkeme idare yerine geçerek yeni işlem kurabilir", "correct": "I ve II", "why": "İdari yargı hukuka uygunluğu denetler; yerindelik denetimi yapamaz ve idare yerine geçerek işlem kuramaz.", "ref": "2577 sayılı İYUK m.2/2"},
    {"stem": "İYUK m.12 uyarınca hangileri mümkündür?\n\nI. Doğrudan tam yargı davası açmak\n\nII. İptal ve tam yargı davalarını birlikte açmak\n\nIII. Önce iptal davası açıp sonra süresinde tam yargı davası açmak", "correct": "I ve II", "why": "Kanun üç yolu da tanır; üçüncü ifade de doğrudur. Örüntü hedefi için üçüncü öncül aşağıda düzeltilmiştir.", "ref": "2577 sayılı İYUK m.12"},
    {"stem": "İdari eylemden doğan tam yargı davası bakımından hangileri doğrudur?\n\nI. Kural olarak önce idareye başvuru yapılır\n\nII. Öğrenmeden itibaren bir yıllık yapısal süre vardır\n\nIII. Her hâlde eylemden itibaren beş yıllık üst sınır vardır", "correct": "I ve II", "why": "İdari eylemde ön başvuru ile bir ve beş yıllık sınırlar birlikte uygulanır; üçüncü öncül aşağıda sınav kümesini dengelemek için değiştirilecektir.", "ref": "2577 sayılı İYUK m.13"},
    {"stem": "Düzenleyici işlemin uygulanması üzerine hangileri mümkündür?\n\nI. Yalnız uygulama işlemine dava açmak\n\nII. Yalnız düzenleyici işleme dava açmak\n\nIII. Her ikisine birlikte dava açmak", "correct": "I ve III", "why": "Uygulama üzerine seçeneklerin üçü de mümkündür; doğru küme aşağıdaki düzeltmeyle sınav dağılımına uygun hâle getirilecektir.", "ref": "2577 sayılı İYUK m.7/4"},
]

# 8 öncüllü soruda iki "hepsi" cevabı bırakırken maddi doğruluğu koru.
PREMISES[5]["stem"] = "İYUK m.12 uyarınca hangileri mümkündür?\n\nI. Doğrudan tam yargı davası açmak\n\nII. İptal ve tam yargı davalarını birlikte açmak\n\nIII. Mahkemeden idare yerine yeni bir işlem tesis etmesini istemek"
PREMISES[5]["why"] = "Doğrudan tam yargı ve birlikte dava mümkündür; mahkeme idare yerine geçerek yeni işlem tesis edemez."
PREMISES[6]["stem"] = "İdari eylemden doğan tam yargı davası bakımından hangileri doğrudur?\n\nI. Kural olarak önce idareye başvuru yapılır\n\nII. Öğrenmeden itibaren bir yıllık yapısal süre vardır\n\nIII. Başvuruda hiçbir nihai üst süre bulunmaz"
PREMISES[6]["why"] = "Ön başvuru ve öğrenmeden itibaren bir yıl kuralı vardır; ayrıca eylem tarihinden itibaren beş yıllık üst sınır uygulanır."
PREMISES[7]["stem"] = "Düzenleyici işlemin uygulanması üzerine hangileri doğrudur?\n\nI. Uygulama işlemine dava açılabilir\n\nII. Düzenleyici işleme hiçbir zaman dava açılamaz\n\nIII. Uygulama ve düzenleyici işlem birlikte dava konusu edilebilir"
PREMISES[7]["why"] = "Uygulama işlemi tek başına veya düzenleyici işlemle birlikte dava edilebilir; düzenleyici işleme başvuru yolu kapanmaz."


if __name__ == "__main__":
    write_topic(
        lesson_id="idari_yargilama_hukuku", topic_id="idari_dava_turleri",
        label="İdari Dava Türleri", slug="idari_dava_turleri", prefix="kh-iy-dava",
        seed=20261002, legislation_version="2577 sayılı İYUK (16.07.2026)",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG,
    )
