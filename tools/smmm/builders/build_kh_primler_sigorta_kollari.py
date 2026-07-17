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

# Doğru seçeneğin uzunluğu cevap anahtarına dönüşmesin diye her bankada
# kısa, orta ve uzun; fakat aynı kazanım çevresinde kalan yanlışlar bulunur.
WRONG["kol"].extend([
    "Yalnız işsizlik sigortasıdır",
    "Sadece özel sağlık sigortasıdır",
    "Kısa vadeli tek kol yaşlılıktır",
    "Ölüm sigortası kısa vadelidir",
    "Genel sağlık sigortası bir emeklilik aylığı türüdür",
    "Analık sigortası uzun vadeli sigorta kolları içinde yer alır",
    "5510 bütün riskleri tek sigorta kolunda toplar; kısa ve uzun vadeli ayrım ile genel sağlık sigortası ayrımı yapmaz",
    "Kısa vadeli sigorta kolları yalnız sağlık hizmeti sunar; geçici ödenek, sürekli gelir veya hak sahiplerine gelir bağlanamaz",
])
WRONG["risk"].extend([
    "Her rahatsızlık meslek hastalığıdır",
    "Normal yolculuk daima iş kazasıdır",
    "Bildirim süresi otuz takvim günüdür",
    "İşyeri dışındaki hiçbir olay korunmaz",
    "İş kazasında prim günü şartı her durumda aranır",
    "Meslek hastalığında işle nedensellik bağı aranmaz",
    "İşverenin kontrolü dışındaki yerde gerçekleşen kazada üç iş günlük bildirim süresi yine kazanın olduğu anda başlar",
    "Sürekli iş göremezlik geliri için meslekte kazanma gücü kaybının yüzde altmışa ulaşması ve ayrıca yaş koşulunun sağlanması zorunludur",
])
WRONG["prim"].extend([
    "Bütün nakit ödemeler istisnadır",
    "Hak edilen ücret kapsam dışıdır",
    "Ayni yardım daima prime tabidir",
    "İkramiye hiçbir ayda prime girmez",
    "Nakit ödeme prime esas kazanç dışında kalır",
    "Nakit ödemenin yalnız yarısı prime tabi tutulur",
    "Nakit ödeme yalnız izleyen ay prime tabi tutulur",
    "Nakit ödeme ayni sayılır ve prime tabi tutulmaz",
    "2026 kısa vadeli prim oranı yüzde dokuzdur",
    "Ücret yalnız fiilen ödendiği aya mal edilir",
    "Ücret dışındaki ödemenin tavanı aşan kısmı hiçbir dönemde prime esas kazanca eklenmez ve kalıcı biçimde kapsam dışında kalır",
    "İşyerinde yemek verilmemesi hâlinde çalışılan gün başına yapılan her tutardaki yemek ödemesi 2026 yılında sınırsız olarak primden istisnadır",
])
WRONG["yukum"].extend([
    "Sigortalılık isteğe bağlıdır",
    "4/a primini yalnız işçi öder",
    "4/b primini işveren öder",
    "Asıl işveren hiç sorumlu değildir",
    "Kamu görevlileri 4/b kapsamında sayılır",
    "Prim borcu sözleşmeyle sigortalıya devredilebilir",
    "İşveren sigortalı payını kesmeden ve kendi payını eklemeden yalnız bordro düzenleyerek bütün prim yükümlülüğünü yerine getirmiş sayılır",
    "Alt işverenin Kuruma karşı yükümlülüklerinde asıl işveren, işin kendi işyerinde yürütülüp yürütülmediğine bakılmaksızın hiçbir koşulda birlikte sorumlu tutulamaz",
])


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


def F(correct, focus, focus_correct, focus_why, focus_ref=None, focus_difficulty=None):
    item = {
        "correct": correct,
        "focus": focus,
        "focus_correct": focus_correct,
        "focus_why": focus_why,
    }
    if focus_ref:
        item["focus_ref"] = focus_ref
    if focus_difficulty:
        item["focus_difficulty"] = focus_difficulty
    return item


VARIANTS = [
    F(
        "İş kazası ve meslek hastalığı, hastalık ve analık kısa vadeli sigorta kollarıdır",
        "SGK'nın 2026 standart 4/a prim tablosuna göre kısa vadeli sigorta kolları prim oranı ve pay dağılımı hangisidir?",
        "Toplam yüzde 2,25'tir ve tamamı işveren payıdır",
        "2026 standart 4/a tablosunda kısa vadeli sigorta kolları primi yüzde 2,25 olup çalışan payı bulunmaz.",
        "5510 sayılı Kanun m.81; SGK 2026 İşveren Prim Oranları",
        "hard",
    ),
    F(
        "Malullük, yaşlılık ve ölüm sigortaları uzun vadeli sigorta kollarıdır",
        "2026 standart 4/a bordrosunda malullük, yaşlılık ve ölüm priminin çalışan ile işveren arasındaki dağılımı nasıldır?",
        "Yüzde 9 çalışan ve yüzde 12 işveren payı olmak üzere toplam yüzde 21'dir",
        "2026 standart 4/a tablosunda MYÖ primi yüzde 9 çalışan ve yüzde 12 işveren payı olmak üzere toplam yüzde 21'dir.",
        "5510 sayılı Kanun m.81; SGK 2026 İşveren Prim Oranları",
        "hard",
    ),
    F(
        "Sağlık hizmetlerine erişimin finansmanı genel sağlık sigortasıyla sağlanır",
        "SGK'nın 2026 standart 4/a prim tablosuna göre genel sağlık sigortası toplam prim oranı hangisidir?",
        "Yüzde 12,5; yüzde 7,5 işveren ve yüzde 5 çalışan payıdır",
        "2026 standart 4/a tablosunda GSS primi yüzde 7,5 işveren ve yüzde 5 çalışan payı olmak üzere toplam yüzde 12,5'tir.",
        "5510 sayılı Kanun m.81; SGK 2026 İşveren Prim Oranları",
        "hard",
    ),
    F(
        "Hizmet akdiyle bir işverene bağlı çalışan kişi 4/a kapsamında sigortalıdır",
        "Kamu idarelerinde Kanunun saydığı kadro ve görevlerde çalışan kamu görevlilerinin temel sigortalılık statüsü hangisidir?",
        "Kanunda sayılan kamu görevlileri 4/c kapsamında sigortalıdır",
        "5510 m.4/1-c kapsamındaki kamu görevlileri, Kanunda belirtilen koşullarla 4/c statüsünde sigortalı sayılır.",
        "5510 sayılı Kanun m.4/1-c",
        "easy",
    ),
    F(
        "Kendi adına ve hesabına bağımsız çalışan kişi 4/b kapsamında sigortalıdır",
        "4/b kapsamındaki bağımsız çalışanın kendi sigortalılığına ilişkin prim ödeme yükümlülüğü kural olarak kime aittir?",
        "Bağımsız çalışanın kendisine aittir",
        "4/b sigortalısı, kendi sigortalılığından doğan primleri Kanunda öngörülen süre ve usule göre kendisi öder.",
        "5510 sayılı Kanun m.88",
    ),
    F(
        "Sigortalılık zorunludur; sosyal sigorta haklarından vazgeçmeye ilişkin sözleşme hükmü geçersizdir",
        "Tarafların sosyal sigorta hak ve yükümlülüklerini azaltan ya da başka kişiye devreden sözleşme hükmünün sonucu nedir?",
        "Kanunun uygulanmasında geçersizdir",
        "Zorunlu sigortalılığa ilişkin hak ve yükümlülükleri ortadan kaldıran, azaltan veya devreden sözleşme hükümleri geçersizdir.",
        "5510 sayılı Kanun m.92",
    ),
    F(
        "Sigortalının işyerinde bulunduğu sırada bedenen zarar gördüğü olay iş kazasıdır",
        "Bir olayın 5510 anlamında iş kazası sayılması için sigortalının olay anında mutlaka fiilen üretim yapması gerekir mi?",
        "Hayır; sigortalının işyerinde bulunduğu sırada gerçekleşmesi yeterli kanuni bağlantılardan biridir",
        "M.13, sigortalının işyerinde bulunduğu sıradaki olayı ayrıca sayar; olay anında mutlaka asıl işin yapılıyor olması aranmaz.",
        "5510 sayılı Kanun m.13/1-a",
        "hard",
    ),
    F(
        "Görevle başka yere gönderilme nedeniyle asıl iş yapılmadan geçen zamandaki olay iş kazası sayılabilir",
        "İşverenin görevlendirmesiyle işyeri dışına çıkan sigortalının koruması yalnız görevi fiilen yaptığı anlarla mı sınırlıdır?",
        "Hayır; görevlendirme nedeniyle asıl işi yapmadan geçen zaman da m.13 kapsamına girebilir",
        "İşveren tarafından görevle başka yere gönderilme nedeniyle asıl iş yapılmadan geçen zamanda meydana gelen olay da iş kazası hâlidir.",
        "5510 sayılı Kanun m.13/1-c",
        "hard",
    ),
    F(
        "İşverenin sağladığı servisle işe gidiş sırasında gerçekleşen olay iş kazası kapsamındadır",
        "Sigortalının kendi aracıyla olağan şekilde işe giderken geçirdiği her kaza yalnız yolculuk nedeniyle otomatik olarak iş kazası sayılır mı?",
        "Hayır; m.13'teki taşıma bağlantısı işverence sağlanan taşıtla gidiş gelişi kapsar",
        "M.13/1-e işverence sağlanan taşıtla işe gidiş gelişi sayar; her kişisel yolculuk bu bent uyarınca otomatik iş kazası değildir.",
        "5510 sayılı Kanun m.13/1-e",
        "hard",
    ),
    F(
        "4/a kapsamındaki emziren sigortalının süt izninde uğradığı olay iş kazası sayılır",
        "Süt verme için ayrılan zamandaki iş kazası bağlantısı Kanunda hangi sigortalı grubu için açıkça düzenlenmiştir?",
        "4/a kapsamındaki emziren kadın sigortalı için",
        "M.13/1-d, 4/a kapsamındaki emziren kadın sigortalının süt verme için ayrılan zamanda uğradığı olayı iş kazası sayar.",
        "5510 sayılı Kanun m.13/1-d",
    ),
    F(
        "İşin niteliği veya yürütüm şartlarından doğan tekrarlanan maruziyet meslek hastalığı oluşturabilir",
        "Bir rahatsızlığın meslek hastalığı sayılmasında iş ile rahatsızlık arasında nasıl bir bağlantı aranır?",
        "İşin niteliği veya yürütüm şartlarıyla uygun nedensellik bağlantısı aranır",
        "Meslek hastalığı, sigortalının çalıştığı ya da yaptığı işin niteliğinden veya yürütüm şartlarından kaynaklanmalıdır.",
        "5510 sayılı Kanun m.14",
    ),
    F(
        "4/a iş kazası genel olarak kazadan sonraki üç iş günü içinde Kuruma bildirilir",
        "4/a sigortalısının kazası işverenin kontrolü dışındaki yerde olmuşsa üç iş günlük bildirim süresi ne zaman başlar?",
        "İşverenin kazayı öğrendiği tarihten başlar",
        "İşverenin kontrolü dışındaki yerdeki kazada üç iş günlük süre, kazanın öğrenildiği tarihten itibaren işlemeye başlar.",
        "5510 sayılı Kanun m.13/2-a",
        "hard",
    ),
    F(
        "İş kazası ve meslek hastalığı dışında kalan, iş göremezliğe yol açan rahatsızlık hastalık hâlidir",
        "4/a sigortalısına hastalık nedeniyle geçici iş göremezlik ödeneği verilebilmesi için temel prim ve ödeme başlangıcı kuralı hangisidir?",
        "Önceki bir yılda en az doksan gün kısa vadeli prim ve üçüncü günden başlayan ödeme",
        "Hastalık hâlinde önceki bir yılda en az doksan gün kısa vadeli sigorta primi gerekir ve ödenek iş göremezliğin üçüncü gününden başlar.",
        "5510 sayılı Kanun m.18/1-b",
        "hard",
    ),
    F(
        "Gebelik ve doğumla bağlantılı kanuni koruma, analık sigortası kapsamındadır",
        "4/a sigortalısına analık nedeniyle geçici iş göremezlik ödeneği için doğumdan önceki bir yılda en az kaç gün kısa vadeli prim gerekir?",
        "En az doksan gün kısa vadeli sigorta primi gerekir",
        "Analık nedeniyle geçici iş göremezlik ödeneğinde doğumdan önceki bir yıl içinde en az doksan gün kısa vadeli sigorta primi aranır.",
        "5510 sayılı Kanun m.18/1-c",
        "hard",
    ),
    F(
        "İş kazası nedeniyle geçici çalışamama hâlinde geçici iş göremezlik ödeneği gündeme gelir",
        "İş kazası nedeniyle geçici iş göremezlik ödeneğinde ödeme günü ve prim günü koşulu bakımından genel kural hangisidir?",
        "Her gün için ödenir; belirli bir prim ödeme gün sayısı aranmaz",
        "İş kazasında geçici iş göremezlik ödeneği her gün için verilir; yararlanmak için belirli sigortalılık süresi veya prim günü aranmaz.",
        "5510 sayılı Kanun m.18; SGK İş Kazası açıklaması",
        "hard",
    ),
    F(
        "İş kazası veya meslek hastalığından doğan kalıcı kayıpta sürekli iş göremezlik geliri bağlanabilir",
        "Sürekli iş göremezlik geliri için meslekte kazanma gücü kaybının Kurum Sağlık Kurulunca en az hangi oranda tespiti gerekir?",
        "Meslekte kazanma gücü kaybı en az yüzde 10 olmalıdır",
        "İş kazası veya meslek hastalığı sonucu meslekte kazanma gücü en az yüzde 10 azalan sigortalıya sürekli iş göremezlik geliri bağlanır.",
        "5510 sayılı Kanun m.19",
        "hard",
    ),
    F(
        "Kanuni düzeydeki çalışma gücü kaybı Kurum Sağlık Kurulunca saptanırsa malullük sigortası gündeme gelir",
        "4/a ve 4/b sigortalısının 5510 anlamında malul sayılmasında aranan genel kayıp oranı ve tespit mercii hangisidir?",
        "En az yüzde 60 kayıp ve Kurum Sağlık Kurulu tespiti",
        "4/a ve 4/b sigortalısında en az yüzde 60 çalışma gücü veya ilgili meslekte kazanma gücü kaybını Kurum Sağlık Kurulu tespit etmelidir.",
        "5510 sayılı Kanun m.25; SGK Malullük açıklaması",
        "hard",
    ),
    F(
        "Kanuni koşulları sağlayan sigortalının emeklilik dönemindeki koruması yaşlılık sigortasıdır",
        "Yaşlılık sigortasından sağlanan temel haklar hangileridir?",
        "Yaşlılık aylığı bağlanması veya yaşlılık toptan ödemesi yapılması",
        "Yaşlılık sigortası, koşulları oluştuğunda yaşlılık aylığı; aylığa hak kazanılamayan kanuni hâllerde yaşlılık toptan ödemesi sağlar.",
        "5510 sayılı Kanun m.28 ve m.31",
    ),
    F(
        "Sigortalının ölümünde hak sahiplerine yönelik koruma ölüm sigortası kapsamında sağlanır",
        "Aşağıdakilerden hangisi ölüm sigortasından sağlanan haklar arasında yer alır?",
        "Koşulları varsa hak sahiplerine ölüm aylığı bağlanması",
        "Ölüm sigortası kapsamında hak sahiplerine ölüm aylığı bağlanması, toptan ödeme, evlenme ve cenaze ödeneği gibi haklar sağlanabilir.",
        "5510 sayılı Kanun m.32 ve m.37",
    ),
    F(
        "Hak edilmiş brüt ücret, henüz ödenmemiş olsa da ait olduğu ayın prime esas kazancına dâhil edilir",
        "Ücretler prime esas kazanç bakımından hangi döneme mal edilir?",
        "Ücretler hak edildikleri aya mal edilir",
        "M.80/1-d uyarınca ücretler, fiilen daha sonra ödense bile hak edildikleri aya mal edilerek prime tabi tutulur.",
        "5510 sayılı Kanun m.80/1-d",
    ),
    F(
        "Prim ve ikramiye kural olarak ödendiği ayın prime esas kazancına dâhil edilir",
        "Ücret dışındaki ödeme yapıldığı ayda prime esas kazanç üst sınırını aşarsa prime alınamayan kısım nasıl izlenir?",
        "İzleyen aydan başlayarak en çok iki ayın üst sınır altı kazançlarına eklenir",
        "Ücret dışındaki ödemenin tavan nedeniyle prime alınamayan kısmı, izleyen aydan başlayarak en çok iki ay boyunca üst sınır altı kazanca eklenir.",
        "5510 sayılı Kanun m.80/1-d",
        "hard",
    ),
    F(
        "İşçiye doğrudan sağlanan ayni yardım, m.80'deki istisna kapsamında prime esas kazanca alınmaz",
        "Ayni yardım yerine aynı değer işçiye nakit olarak ödenmiş ve özel bir istisna bulunmuyorsa sonuç nedir?",
        "Nakit ödeme prime esas kazanca dâhil edilir",
        "Ayni yardımın kendisi istisna olsa da onun yerine yapılan nakit ödeme, özel istisna yoksa m.80/1-c uyarınca prime tabidir.",
        "5510 sayılı Kanun m.80/1-b-c",
    ),
    F(
        "Ölüm, doğum ve evlenme yardımları güncel m.80'de prime tabi tutulmayan ödemeler arasındadır",
        "2026 yılında işverenin özel sağlık sigortası ve bireysel emeklilik için ödediği tutarlarda aylık prime esas kazanç istisnasının ortak sınırı nedir?",
        "Aylık toplamı asgari ücretin yüzde 30'unu aşmayan kısım",
        "İşverenin özel sağlık sigortası ve bireysel emeklilik ödemelerinin aylık toplamının asgari ücretin yüzde 30'unu aşmayan kısmı prime tabi değildir.",
        "5510 sayılı Kanun m.80/1-b-8",
        "hard",
    ),
    F(
        "Görev yolluğu ile Kanunda sayılan kıdem ve ihbar tazminatları prime tabi tutulmayan ödemelerdendir",
        "2026 yılında işyerinde yemek verilmeyen bir 4/a sigortalısına çalıştığı günler için yapılan yemek ödemesinde günlük prim istisnası üst sınırı nedir?",
        "Çalışılan gün başına 300 Türk lirası",
        "7577 sayılı Kanunla güncellenen m.80'e göre 2026'da işyerinde yemek verilmiyorsa çalışılan gün başına 300 lirayı aşmayan yemek ödemesi prime tabi değildir.",
        "5510 sayılı Kanun m.80/1-b-9; 7577 sayılı Kanun m.10",
        "hard",
    ),
    F(
        "Ayni yardım yerine yapılan nakit ödeme özel bir istisna yoksa prime esas kazanca dâhil edilir",
        "Başka bir kanunda bir ödemenin prime tabi olmadığı yazıyor; ancak 5510 m.80'de bu ödeme için istisna yoktur. Sonuç nedir?",
        "Diğer kanundaki muafiyet dikkate alınmaz ve ödeme prime tabi olur",
        "M.80/1-c, başka kanunlardaki prime tabi olmama hükümlerinin 5510 uygulamasında dikkate alınmayacağını düzenler.",
        "5510 sayılı Kanun m.80/1-c",
        "hard",
    ),
    F(
        "İşveren sigortalı payını keser, kendi payını ekler ve toplam primi Kuruma öder",
        "Alt işveren, asıl işverenin işyerinde aldığı işte sigortalı çalıştırıyorsa Kuruma karşı yükümlülüklerden kim sorumludur?",
        "Alt işverenle birlikte asıl işveren de sorumludur",
        "Asıl işveren, alt işverenin Kanundan doğan yükümlülüklerinden alt işverenle birlikte sorumludur.",
        "5510 sayılı Kanun m.12/6",
        "hard",
    ),
]

assert len(VARIANTS) == len(RULES) == 26
for rule, variant in zip(RULES, VARIANTS):
    rule.update(variant)


def length_balanced_distractors(correct, bank):
    """Doğru cevabın iki yanında ikişer uzunlukta çeldirici seçer."""
    shorter = sorted((x for x in bank if len(x) < len(correct)), key=len, reverse=True)
    longer = sorted((x for x in bank if len(x) > len(correct)), key=len)
    assert len(shorter) >= 2 and len(longer) >= 2, correct
    return shorter[:2] + longer[:2]


for rule in RULES:
    bank = WRONG[rule["bank"]]
    rule["scenario_distractors"] = length_balanced_distractors(rule["correct"], bank)
    rule["focus_distractors"] = length_balanced_distractors(rule["focus_correct"], bank)


PREMISES = [
    {"stem": "Sigorta kolları bakımından hangileri doğrudur?\n\nI. İş kazası ve meslek hastalığı kısa vadelidir\n\nII. Malullük, yaşlılık ve ölüm uzun vadelidir\n\nIII. Genel sağlık sigortası sağlık hizmetlerinin finansmanıyla ilgilidir", "correct": "I, II ve III", "why": "Üç ifade de 5510'daki kısa ve uzun vadeli kollar ile genel sağlık sigortası ayrımını doğru gösterir.", "ref": "5510 sayılı Kanun m.3 ve m.60"},
    {"stem": "SGK'nın 2026 standart 4/a prim tablosuna göre hangileri doğrudur?\n\nI. Kısa vadeli sigorta kolları toplam oranı yüzde 2,25'tir\n\nII. MYÖ toplam oranı yüzde 21'dir\n\nIII. GSS toplam oranı yüzde 12,5'tir", "correct": "I, II ve III", "why": "2026 standart 4/a tablosunda kısa vadeli kollar yüzde 2,25, MYÖ yüzde 21 ve GSS yüzde 12,5'tir.", "ref": "5510 sayılı Kanun m.81; SGK 2026 İşveren Prim Oranları"},
    {"stem": "Sigortalılık statüleri bakımından hangileri doğrudur?\n\nI. Hizmet akdiyle çalışanlar 4/a kapsamındadır\n\nII. Kamu görevlilerinin temel statüsü 4/b'dir\n\nIII. Kendi adına bağımsız çalışanlar 4/b kapsamında olabilir", "correct": "I ve III", "why": "Hizmet akdiyle çalışanlar 4/a, bağımsız çalışanlar 4/b kapsamında olabilir; Kanunda sayılan kamu görevlilerinin temel statüsü 4/c'dir.", "ref": "5510 sayılı Kanun m.4"},
    {"stem": "İş kazası hâlleri bakımından hangileri doğrudur?\n\nI. İşverenin sağladığı taşıtla işe gidiş geliş kapsama girebilir\n\nII. Görevle başka yere gönderilme nedeniyle asıl iş yapılmadan geçen zaman kapsama girebilir\n\nIII. Kişinin kendi aracıyla her olağan işe gidişi kendiliğinden iş kazasıdır", "correct": "I ve II", "why": "İlk iki bağlantı m.13'te açıkça sayılır; kişisel araçla yapılan her olağan yolculuk yalnız bu nedenle otomatik iş kazası olmaz.", "ref": "5510 sayılı Kanun m.13/1-c ve e"},
    {"stem": "Kısa vadeli sigorta yardımları bakımından hangileri doğrudur?\n\nI. İş kazasında geçici ödenek için doksan prim günü zorunludur\n\nII. Meslekte kazanma gücü en az yüzde 10 azalan sigortalıya sürekli iş göremezlik geliri bağlanabilir\n\nIII. Hastalık ödeneği kural olarak iş göremezliğin üçüncü gününden başlar", "correct": "II ve III", "why": "İş kazasında belirli prim günü aranmaz; sürekli gelir için en az yüzde 10 kayıp aranır ve hastalık ödeneği üçüncü günden başlar.", "ref": "5510 sayılı Kanun m.18-19"},
    {"stem": "Prime esas kazanç bakımından hangileri doğrudur?\n\nI. Ücret hak edildiği aya mal edilir\n\nII. Ayni yardım yerine yapılan her nakit ödeme otomatik istisnadır\n\nIII. Ücret dışı ödemenin tavanı aşan kısmı en çok izleyen iki ayda dikkate alınabilir", "correct": "I ve III", "why": "Ücret hak edildiği aya aittir; ücret dışı ödemenin tavanı aşan kısmı en çok iki ay izlenir. Nakit ikame özel istisna yoksa prime tabidir.", "ref": "5510 sayılı Kanun m.80/1-c-d"},
    {"stem": "Güncel m.80 istisnaları bakımından hangileri doğrudur?\n\nI. Kanunda sayılmayan her nakit ödeme adı değiştirilerek istisna olur\n\nII. Ölüm, doğum ve evlenme yardımları istisnalar arasındadır\n\nIII. Görev yolluğu ile Kanunda sayılan kıdem ve ihbar tazminatları istisnalar arasındadır", "correct": "II ve III", "why": "İkinci ve üçüncü gruplar m.80'de sayılır; ödemenin adını değiştirmek yeni bir istisna yaratmaz.", "ref": "5510 sayılı Kanun m.80/1-b-c; 7577 sayılı Kanun m.10"},
    {"stem": "Prim yükümlülüğü bakımından hangileri doğrudur?\n\nI. 4/a primlerinin tamamını yalnız sigortalı doğrudan Kuruma öder\n\nII. İşveren sigortalı payını kesip kendi payını ekleyerek Kuruma öder\n\nIII. Alt işverenin yükümlülüklerinden asıl işveren hiçbir durumda sorumlu olmaz", "correct": "Yalnız II", "why": "4/a primini işveren sigortalı payını kesip kendi payını ekleyerek öder; asıl işveren de m.12 koşullarında alt işverenle birlikte sorumludur.", "ref": "5510 sayılı Kanun m.12/6 ve m.88"},
]


if __name__ == "__main__":
    write_topic(
        lesson_id="sosyal_guvenlik_mevzuati", topic_id="primler_ve_sigorta_kollari",
        label="Primler ve Sigorta Kolları", slug="primler_ve_sigorta_kollari",
        prefix="kh-sg-prim", seed=20261006,
        legislation_version="5510 sayılı Kanun ve 7577 sayılı değişiklik (17.07.2026 güncel metin)",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG,
    )
