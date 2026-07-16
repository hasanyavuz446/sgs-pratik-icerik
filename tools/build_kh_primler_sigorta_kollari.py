#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Primler ve Sigorta Kolları — güncel 5510 yapısal hükümleri, 60 soru."""
from topic_pack_builder import write_topic


def R(scenario, focus, correct, bank, why, ref, difficulty="medium"):
    return locals()


WRONG = {
    "kol": [
        "Yalnız işsizlik sigortası ile bireysel emeklilikten oluşur ve 5510 kapsamındaki sosyal sigorta kollarıyla ilgisi yoktur",
        "Sadece sağlık hizmeti sunucularının ruhsatlandırılmasını düzenler; gelir, aylık veya ödenek sağlamaz",
        "İş kazası ile yaşlılığı aynı kısa vadeli kol içinde birleştirir ve ölüm sigortasını kapsam dışında bırakır",
        "Malullük, yaşlılık ve ölüm risklerini kısa vadeli; hastalık ve analığı uzun vadeli sigorta kolu sayar",
        "Genel sağlık sigortasını yalnız işverenin isteğine bağlı özel bir sigorta sözleşmesi olarak kabul eder",
        "Bütün sigorta kollarını tek bir olayın gerçekleşmesine bağlar ve risklerin niteliklerine göre hiçbir ayrım yapmaz",
        "İş kazası ve meslek hastalığında yalnız tedavi hizmeti sağlar; geçici veya sürekli gelir hakkı doğuramaz",
        "Ölüm sigortasından yalnız sigortalının kendisine yaşlılık aylığı bağlanır; hak sahiplerine hiçbir ödeme yapılmaz",
    ],
    "risk": [
        "Olayın sigortalıyı bedenen veya ruhen etkilemesi gerekmez; işyeri yakınındaki her olay otomatik iş kazasıdır",
        "Meslek hastalığı için işin niteliği veya yürütüm koşullarıyla bağlantı aranmaz; her rahatsızlık bu kapsamda sayılır",
        "İş kazası yalnız işverenin merkez binasında ve fiilen üretim yapılırken gerçekleşirse sigorta olayı kabul edilir",
        "İşverence sağlanan taşıtla işe gidiş geliş sırasında meydana gelen olay hiçbir koşulda iş kazası sayılamaz",
        "Görevle işyeri dışına gönderilen sigortalının asıl işini yapmadan geçen zamanı sigorta koruması dışında kalır",
        "Hastalık hâli, iş kazası ve meslek hastalığı dâhil bütün iş göremezlik nedenlerini tek kavram altında toplar",
        "Meslek hastalığının tespiti yalnız işverenin tek taraflı beyanıyla yapılır; sağlık kurulu incelemesi aranmaz",
        "4/a sigortalısının iş kazasını Kuruma bildirme yükümlülüğü yalnız sigortalıya aittir ve işveren sorumlu değildir",
    ],
    "prim": [
        "Hak edilmiş ücretler prime esas kazanca alınmaz; yalnız işçinin gönüllü olarak bildirdiği yardımlar dikkate alınır",
        "Ayni yardımın tamamı her durumda ücret sayılır ve istisna kapsamına girmesi kanunen mümkün değildir",
        "Ölüm, doğum ve evlenme yardımları adları ne olursa olsun zorunlu biçimde prime esas kazanca dâhil edilir",
        "Görev yollukları ile kıdem ve ihbar tazminatları ücret gibi değerlendirilerek istisnasız prime tabi tutulur",
        "Kanunda sayılan istisnalar dışındaki nakit ödemeler, adları değiştirilerek prime esas kazanç dışında bırakılabilir",
        "Ücret dışındaki bütün ödemeler yalnız ödemenin yapıldığı yıldan sonraki beşinci yılın kazancına eklenir",
        "Prime esas kazanç alt ve üst sınırı bulunmaz; işveren istediği herhangi bir tutarı kayıt dışında bırakabilir",
        "Ayni yardım yerine yapılan nakit ödeme, ayni yardım sayılarak kanundaki genel prime tabi olma kuralından çıkar",
    ],
    "yukum": [
        "Sigortalılık tarafların sözleşmesine bağlıdır; işçi yazılı beyanla bütün sosyal sigorta haklarından vazgeçebilir",
        "4/a sigortalısının primini yalnız işçi doğrudan Kuruma öder; işverenin kesme ve kendi payını ekleme görevi yoktur",
        "4/b kapsamındaki kişi bağımsız çalışmasına rağmen bütün primlerini yanında çalışan işçinin işverenine yükleyebilir",
        "Prim ödeme yükümlülüğü yalnız genel sağlık sigortası için vardır; kısa ve uzun vadeli kollar primsiz yürütülür",
        "Sigorta hakkını azaltan sözleşme hükümleri taraflarca imzalanınca Kurum yönünden de geçerli ve bağlayıcı olur",
        "Alt işverenin çalıştırdığı sigortalılar yönünden asıl işverenin hiçbir ortak sorumluluğu bulunmaz",
        "Hak edilen fakat henüz ödenmeyen ücretler üzerinden prim hesaplanması mümkün değildir",
        "Sigortalılık şartları kaybedilse bile sigortalılık süresiz devam eder ve ölüm hâlinde dahi sona ermez",
    ],
}


RULES = [
    R("İş kazası, meslek hastalığı, hastalık ve analık risklerini birlikte ifade eden grup hangisidir?", "5510 sayılı Kanun'daki kısa vadeli sigorta kolları hangileridir?", "İş kazası ve meslek hastalığı, hastalık ve analık", "kol", "Kanun kısa vadeli sigorta kollarını iş kazası ve meslek hastalığı, hastalık ve analık sigortaları olarak tanımlar.", "5510 sayılı Kanun m.3/4", "easy"),
    R("Malullük, yaşlılık ve ölüm riskleri hangi sigorta kolu grubunda yer alır?", "5510 sayılı Kanun'daki uzun vadeli sigorta kolları hangileridir?", "Malullük, yaşlılık ve ölüm", "kol", "Malullük, yaşlılık ve ölüm sigortaları uzun vadeli sigorta kollarıdır.", "5510 sayılı Kanun m.3/5", "easy"),
    R("Sağlık hizmetlerinin finansmanı ve kişilerin sağlık riskine karşı korunması hangi sistemle ilişkilidir?", "Sosyal sigorta kollarından ayrı olarak sağlık hizmetine erişimi finanse eden yapı hangisidir?", "Genel sağlık sigortası", "kol", "Genel sağlık sigortası, kişilerin sağlık hizmetlerinden yararlanmasını sosyal güvenlik sistemi içinde finanse eder.", "5510 sayılı Kanun m.60 ve devamı", "easy"),
    R("Bir işverene hizmet akdiyle bağlı çalışan kişi 5510 m.4 kapsamında hangi statüdedir?", "Hizmet akdiyle çalışanların temel sigortalılık statüsü hangisidir?", "4/a sigortalılığı", "yukum", "Bir veya birden fazla işveren tarafından hizmet akdiyle çalıştırılanlar 4/a kapsamında sigortalıdır.", "5510 sayılı Kanun m.4/1-a", "easy"),
    R("Hizmet akdine bağlı olmadan kendi adına ve hesabına ticari faaliyette bulunan kişi hangi temel statüdedir?", "Kendi adına ve hesabına bağımsız çalışanların temel sigortalılık statüsü hangisidir?", "4/b sigortalılığı", "yukum", "Kanunda sayılan kendi adına ve hesabına bağımsız çalışanlar 4/b kapsamındadır.", "5510 sayılı Kanun m.4/1-b", "easy"),
    R("İşçi ve işveren sigorta haklarından karşılıklı sözleşmeyle vazgeçmek istemektedir. Bu hükmün sonucu nedir?", "5510 sayılı Kanun'da sigortalılığın hukuki niteliği hangisidir?", "Sigortalılık zorunludur; vazgeçme hükmü geçersizdir", "yukum", "Sigortalılık zorunludur; hak ve yükümlülükleri ortadan kaldıran, azaltan veya devreden sözleşme hükümleri geçersizdir.", "5510 sayılı Kanun m.92"),
    R("4/a sigortalısı işyerinde bulunduğu sırada düşerek bedenen zarar görmüştür. Olay hangi risk kapsamında değerlendirilir?", "Sigortalının işyerinde bulunduğu sırada onu bedenen veya ruhen etkileyen olayın niteliği hangisidir?", "İş kazası", "risk", "Sigortalının işyerinde bulunduğu sırada meydana gelen ve onu hemen veya sonradan bedenen ya da ruhen engelli hâle getiren olay iş kazasıdır.", "5510 sayılı Kanun m.13/a"),
    R("İşçi, işveren tarafından görevle başka şehre gönderilmiş ve asıl işini yapmadan geçen zamanda kazaya uğramıştır. Olayın niteliği nedir?", "Görevle işyeri dışına gönderilen sigortalının yolda geçen zamanındaki olay hangi kapsamda olabilir?", "İş kazası sayılabilir", "risk", "İşveren tarafından görevle başka yere gönderilme nedeniyle asıl iş yapılmadan geçen zamanda meydana gelen olay m.13 kapsamındadır.", "5510 sayılı Kanun m.13/c"),
    R("Sigortalı, işverenin sağladığı servisle işe giderken kazada yaralanmıştır. 5510 bakımından sonuç nedir?", "İşverence sağlanan taşıtla işe gidiş geliş sırasında meydana gelen olay hangi niteliktedir?", "İş kazası kapsamındadır", "risk", "İşverence sağlanan taşıtla işin yapıldığı yere gidiş geliş sırasında meydana gelen olay iş kazası hâllerindendir.", "5510 sayılı Kanun m.13/e"),
    R("Emziren 4/a sigortalısı kanuni süt izni sırasında kaza geçirmiştir. Olay nasıl değerlendirilir?", "Emziren sigortalının süt verme için ayrılan zamanındaki olay hangi kapsamda olabilir?", "İş kazası sayılır", "risk", "4/a kapsamındaki emziren sigortalının süt verme için ayrılan zamanda uğradığı olay iş kazası hâllerindendir.", "5510 sayılı Kanun m.13/d"),
    R("Çalışan, yaptığı işte tekrarlanan kimyasal maruziyet nedeniyle kalıcı rahatsızlığa uğramıştır. Riskin niteliği nedir?", "İşin niteliği veya yürütüm şartları yüzünden tekrarlanan sebeple doğan rahatsızlık hangisidir?", "Meslek hastalığı", "risk", "Meslek hastalığı işin niteliği veya yürütüm şartlarından doğan tekrarlanan sebeple oluşan geçici ya da sürekli hastalık veya engelliliktir.", "5510 sayılı Kanun m.14"),
    R("4/a sigortalısının iş kazasını öğrenen işveren Kuruma bildirim yapacaktır. Genel bildirim süresi nedir?", "4/a sigortalısının iş kazasının Kuruma bildirilmesindeki yapısal süre kaç iş günüdür?", "Kazadan sonraki üç iş günü", "risk", "4/a kapsamındaki iş kazası işveren tarafından Kuruma en geç kazadan sonraki üç iş günü içinde bildirilir; kontrol dışı yerde süre öğrenmeden başlar.", "5510 sayılı Kanun m.13"),
    R("İş kazası ve meslek hastalığı dışında kalan rahatsızlık sigortalıyı geçici olarak iş göremez hâle getirmiştir. Bu hangi hâldir?", "İş kazası ve meslek hastalığı dışındaki iş göremezlik yaratan rahatsızlık nasıl adlandırılır?", "Hastalık hâli", "risk", "4/a ve 4/b sigortalılarında iş kazası ve meslek hastalığı dışındaki iş göremezlik yaratan rahatsızlık hastalık hâlidir.", "5510 sayılı Kanun m.15"),
    R("Sigortalı kadının gebelik ve doğumla bağlantılı rahatsızlıkları hangi kısa vadeli riskle ilişkilidir?", "Gebelik ve doğumla ilgili kanuni koruma hâli hangisidir?", "Analık hâli", "risk", "Kanun, gebeliğin başlangıcından doğum sonrasındaki kanuni döneme kadar ilgili rahatsızlıkları analık hâli olarak tanımlar.", "5510 sayılı Kanun m.15"),
    R("İş kazası nedeniyle sigortalı geçici olarak çalışamamaktadır. Kısa vadeli sigortadan hangi ödeme gündeme gelir?", "Geçici iş göremezlik süresince sağlanan temel parasal hak hangisidir?", "Geçici iş göremezlik ödeneği", "kol", "İş kazası veya meslek hastalığında geçici iş göremezlik süresince günlük geçici iş göremezlik ödeneği verilir.", "5510 sayılı Kanun m.16/a"),
    R("İş kazası sigortalıda kalıcı çalışma gücü kaybına yol açmıştır. Kısa vadeli sigortadan hangi sürekli hak doğabilir?", "İş kazası veya meslek hastalığı nedeniyle kalıcı kayıpta bağlanan hak hangisidir?", "Sürekli iş göremezlik geliri", "kol", "Kanuni koşullar oluştuğunda iş kazası veya meslek hastalığı sigortasından sürekli iş göremezlik geliri bağlanır.", "5510 sayılı Kanun m.16/b"),
    R("Sigortalının çalışma gücü kanundaki ölçüde kaybolmuş ve Kurum Sağlık Kurulu tespiti yapılmıştır. İlgili uzun vadeli kol hangisidir?", "Çalışma gücü kaybına dayanan uzun vadeli sigorta kolu hangisidir?", "Malullük sigortası", "kol", "Malullük sigortası, Kurumca kanuni ölçütlerle belirlenen çalışma gücü kaybına karşı uzun vadeli koruma sağlar.", "5510 sayılı Kanun m.25-27"),
    R("Sigortalı çalışma yaşamının sonunda kanuni yaşlılık koşullarını sağlayarak aylık talep etmektedir. İlgili kol hangisidir?", "Uzun vadeli sigorta kollarından emeklilik dönemine yönelik olan hangisidir?", "Yaşlılık sigortası", "kol", "Yaşlılık sigortası, kanuni koşullar oluştuğunda yaşlılık aylığı veya toptan ödeme sağlar.", "5510 sayılı Kanun m.28-31"),
    R("Sigortalının ölümü üzerine hak sahiplerine aylık, toptan ödeme ve cenaze ödeneği gündeme gelmektedir. İlgili kol hangisidir?", "Hak sahiplerine ölüm aylığı ve diğer kanuni hakları sağlayan uzun vadeli kol hangisidir?", "Ölüm sigortası", "kol", "Ölüm sigortası; ölüm aylığı, ölüm toptan ödemesi, evlenme ve cenaze ödeneği gibi haklar sağlar.", "5510 sayılı Kanun m.32"),
    R("4/a sigortalısının aylık hak edilmiş çıplak ücreti belirlenmiştir. Prime esas kazanç bakımından temel işlem nedir?", "Hak edilen ücretlerin prime esas kazançtaki durumu hangisidir?", "Prime esas kazanca dâhil edilir", "prim", "Hak edilen ücretlerin brüt toplamı prime esas kazanç hesabına alınır.", "5510 sayılı Kanun m.80/1-a"),
    R("İşçiye o ay performans primi ve ikramiye ödenmiştir. Kanunda özel istisna yoksa prime esas kazançta ne yapılır?", "Prim, ikramiye ve benzeri istihkakların genel durumu hangisidir?", "Ödendiği ayın kazancına dâhil edilir", "prim", "Prim, ikramiye ve benzeri ödemeler kural olarak ödendiği ayın prime esas kazancına dâhil edilir.", "5510 sayılı Kanun m.80/1-a ve d"),
    R("İşveren işçiye para yerine doğrudan ayni yardım sağlamıştır. M.80'deki yapısal istisna nedir?", "Ayni yardımların prime esas kazanç bakımından genel durumu hangisidir?", "Prime esas kazanca tabi tutulmaz", "prim", "Kanunda ayni yardımlar prime esas kazanca tabi tutulmayan ödemeler arasında sayılmıştır.", "5510 sayılı Kanun m.80/1-b"),
    R("İşçiye ölüm, doğum veya evlenme nedeniyle yardım yapılmıştır. M.80 uyarınca yapısal sonuç nedir?", "Ölüm, doğum ve evlenme yardımlarının prime esas kazançtaki durumu hangisidir?", "Prime esas kazanç dışında bırakılır", "prim", "Ölüm, doğum ve evlenme yardımları m.80'de prime esas kazanca tabi tutulmayan ödemeler arasındadır.", "5510 sayılı Kanun m.80/1-b"),
    R("İşçiye görev yolluğu ile kıdem ve ihbar tazminatı ödenmiştir. Güncel m.80'in yapısal yaklaşımı nedir?", "Görev yolluğu ile kıdem ve ihbar tazminatının prime esas kazançtaki durumu hangisidir?", "Kanunda sayılan kapsamıyla prime tabi değildir", "prim", "Güncel m.80; görev yolluğu, kıdem, ihbar ve sayılan benzer tazminatları prime tabi tutulmayan ödemeler arasında düzenler.", "5510 sayılı Kanun m.80/1-b (7577 sayılı Kanunla güncel)"),
    R("Ayni yardım adı altında işçiye doğrudan nakit ödeme yapılmıştır ve özel istisna yoktur. Genel kural nedir?", "Ayni yardım yerine geçen nakit ödemenin prime esas kazanç bakımından durumu hangisidir?", "Prime esas kazanca dâhil edilir", "prim", "Kanunda sayılan istisnalar dışında bütün ödemeler ve ayni yardım yerine yapılan nakit ödemeler prime esas kazanca alınır.", "5510 sayılı Kanun m.80/1-c"),
    R("4/a sigortalısının primleri ödenecektir. İşverenin temel ödeme mekanizması nedir?", "4/a primlerinin tahsilinde işverenin yükümlülüğünü doğru açıklayan seçenek hangisidir?", "Sigortalı payını keser, işveren payını ekleyip Kuruma öder", "yukum", "İşveren sigortalı payını ücretten keser, kendi payını ekler ve primleri Kuruma öder.", "5510 sayılı Kanun m.88"),
]


PREMISES = [
    {"stem": "Sigorta kolları bakımından hangileri doğrudur?\n\nI. İş kazası ve meslek hastalığı kısa vadelidir\n\nII. Malullük, yaşlılık ve ölüm uzun vadelidir\n\nIII. Genel sağlık sigortası sağlık hizmetlerinin finansmanıyla ilgilidir", "correct": "I, II ve III", "why": "Üç ifade de 5510'daki sigorta korumasının temel ayrımını doğru gösterir.", "ref": "5510 sayılı Kanun m.3 ve m.60"},
    {"stem": "Sigortalılık statüleri bakımından hangileri doğrudur?\n\nI. Hizmet akdiyle çalışanlar 4/a kapsamındadır\n\nII. Kendi adına bağımsız çalışanlar 4/b kapsamında olabilir\n\nIII. Taraflar sözleşmeyle zorunlu sigortalılığı kaldırabilir", "correct": "I ve II", "why": "İlk iki ifade doğrudur; zorunlu sigortalılıktan sözleşmeyle vazgeçilemez.", "ref": "5510 sayılı Kanun m.4 ve m.92"},
    {"stem": "İş kazası hâlleri bakımından hangileri doğrudur?\n\nI. Sigortalının işyerinde bulunduğu sıra kapsama girebilir\n\nII. Görevle başka yere gönderilme zamanı kapsama girebilir\n\nIII. İşverence sağlanan taşıtla gidiş geliş kapsama girebilir", "correct": "I, II ve III", "why": "Üç hâl de m.13'te iş kazasının gerçekleşebileceği kanuni bağlantılar arasında sayılmıştır.", "ref": "5510 sayılı Kanun m.13"},
    {"stem": "Meslek hastalığı bakımından hangileri doğrudur?\n\nI. İşin niteliğinden doğabilir\n\nII. Tekrarlanan sebeple oluşabilir\n\nIII. İşle hiçbir bağlantısı olmayan her hastalık bu kapsamdadır", "correct": "I ve II", "why": "Meslek hastalığında işin niteliği veya yürütüm koşullarıyla bağlantı aranır; ilgisiz her hastalık kapsamda değildir.", "ref": "5510 sayılı Kanun m.14"},
    {"stem": "Kısa vadeli sigorta hakları bakımından hangileri doğrudur?\n\nI. Geçici iş göremezlik ödeneği verilebilir\n\nII. Sürekli iş göremezlik geliri bağlanabilir\n\nIII. İş kazası sonucu ölümde hak sahiplerine gelir bağlanamaz", "correct": "I ve II", "why": "İlk iki hak sağlanabilir; iş kazası veya meslek hastalığı sonucu ölümde hak sahiplerine gelir bağlanması da mümkündür.", "ref": "5510 sayılı Kanun m.16"},
    {"stem": "Prime esas kazanç bakımından hangileri doğrudur?\n\nI. Hak edilen ücretler kural olarak dâhildir\n\nII. Prim ve ikramiye kural olarak dâhildir\n\nIII. Kanunda sayılan ayni yardımlar kapsam dışında olabilir", "correct": "I ve II", "why": "Üç ifade de doğrudur; hedef cevap dağılımı için üçüncü öncül aşağıda değiştirilecektir.", "ref": "5510 sayılı Kanun m.80"},
    {"stem": "M.80'deki istisnalar bakımından hangileri doğrudur?\n\nI. Ölüm, doğum ve evlenme yardımları sayılmıştır\n\nII. Görev yollukları sayılmıştır\n\nIII. Kanunda sayılmayan her nakit ödeme adı değiştirilerek istisna olur", "correct": "I ve II", "why": "İlk iki ödeme kanunda sayılır; ad değişikliği kanunda bulunmayan nakit ödemeyi istisna hâline getirmez.", "ref": "5510 sayılı Kanun m.80/1-b-c"},
    {"stem": "Prim yükümlülüğü bakımından hangileri doğrudur?\n\nI. İşveren 4/a sigortalı payını ücretten keser\n\nII. İşveren kendi payını ekler\n\nIII. Hak edilmiş fakat ödenmemiş ücretler hiçbir zaman prime tabi olmaz", "correct": "I ve II", "why": "İşveren sigortalı payını kesip kendi payını ekler; hak edilmiş ancak ödenmemiş ücretler için de prim hükümleri uygulanır.", "ref": "5510 sayılı Kanun m.88"},
]

PREMISES[5]["stem"] = "Prime esas kazanç bakımından hangileri doğrudur?\n\nI. Hak edilen ücretler kural olarak dâhildir\n\nII. Prim ve ikramiye kural olarak dâhildir\n\nIII. Ayni yardım yerine yapılan bütün nakit ödemeler otomatik istisnadır"
PREMISES[5]["why"] = "Ücret, prim ve ikramiye kural olarak kapsamdadır; ayni yardım yerine nakit ödeme özel istisna yoksa prime tabidir."


if __name__ == "__main__":
    write_topic(
        lesson_id="sosyal_guvenlik_mevzuati", topic_id="primler_ve_sigorta_kollari",
        label="Primler ve Sigorta Kolları", slug="primler_ve_sigorta_kollari",
        prefix="kh-sg-prim", seed=20261006,
        legislation_version="5510 sayılı Kanun (16.07.2026 güncel metin)",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG,
    )
