# -*- coding: utf-8 -*-
"""Yeterlilik KONU HAVUZU — Hukuk / Ticari İşletme (60 soru = 3×20).

Doğru şık KISA, çeldiriciler UZUN. Açıklamada harf atfı YOK.
Sorular 16.07.2026 tarihinde doğrulanan 6102 sayılı TTK ve 6098 sayılı TBK
hükümlerine dayanır. Bölüm havuzu ile SGS havuzundaki temel tanım sorularından
kaçınmak için ağırlık uygulama, ayrım ve sonuç sorularındadır.
"""
import json
import random
import re

L, T, LBL = "ticaret_hukuku", "ticari_isletme", "Ticari İşletme"
PREFIX, SEED = "kh-tic-isletme", 20260910
OUT = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/yeterlilik/questions_topic_ticari_isletme_2026.json"

Q = []


def q(stem, correct, distractors, why, ref, difficulty="medium"):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(
        dict(
            stem=stem,
            correct=correct,
            distractors=distractors,
            why=why,
            ref=ref,
            difficulty=difficulty,
        )
    )


# ── A. Ticari hükümler, örf ve adet, ticari işler (15) ─────────────────────
q(
    "Bir ticari uyuşmazlıkta uygulanabilir kanun hükmü bulunmamakta, ancak konuya ilişkin yerleşmiş ticari örf ve adet bulunmaktadır. Hâkim öncelikle hangi kurala başvurur?",
    "Ticari örf ve adete",
    [
        "Genel hükümlere doğrudan başvurur; ticari örf ve adetin uyuşmazlıkta hiçbir uygulama alanı bulunmaz",
        "Yalnız tarafların ikisi de tacirse uygulanabilen mesleki kuruluş kararlarını bağlayıcı kural sayar",
        "Sadece tarafların sözleşme sonrasında benimsediği tek taraflı uygulamayı kanun hükmü yerine geçirir",
        "Uyuşmazlık ticari nitelikte olduğu için hakkaniyet dışında hiçbir tamamlayıcı kaynağa başvuramaz",
    ],
    "Ticari hüküm bulunmadığında ticari örf ve adet; o da yoksa genel hükümler uygulanır.",
    "6102 sayılı TTK m.1/2",
    "easy",
)

q(
    "Belirli bir sektörde bazı işletmelerin izlediği uygulama henüz ticari örf ve adet niteliği kazanmamıştır. Bu uygulamanın uyuşmazlıktaki işlevi nedir?",
    "İrade açıklamalarının yorumunda dikkate alınabilir",
    [
        "Uyuşmazlığın tarafları tacir olmasa bile tek başına bağlayıcı bir hukuk kuralı olarak doğrudan uygulanır",
        "Kanunda açık hüküm bulunsa dahi hükmü bertaraf ederek öncelikle uygulanması gereken kaynak hâline gelir",
        "Ticari örf ve adet sayılmadığı için sözleşmenin yorumunda dahi hiçbir koşulda dikkate alınamaz",
        "Yalnız ticaret sicili müdürlüğünce ilan edilirse kanunla eşit düzeyde bağlayıcı nitelik kazanmış olur",
    ],
    "Bir teamül, ticari örf ve adet olarak kabul edilmedikçe hükme esas olamaz; ancak irade açıklamalarının yorumuna yardımcı olabilir.",
    "6102 sayılı TTK m.2/1",
)

q(
    "Aynı ticari mesele hakkında ülke çapında genel bir ticari örf ve adet ile belirli bir bölgeye özgü yerel ticari örf ve adet çatışmaktadır. Kural olarak hangisi uygulanır?",
    "Bölgesel ticari örf ve adet",
    [
        "Genel ticari örf ve adet her durumda yerel düzenlemeye üstün olduğundan yalnız ülke çapındaki uygulama esas alınır",
        "Her iki uygulama birbirini hükümsüz kılar ve hâkim doğrudan genel hükümlere geçmek zorunda kalır",
        "Tarafların tacir olup olmadığına bakılmaksızın yalnız ticaret odasının sonradan yayımladığı görüş uygulanır",
        "Uyuşmazlığın açıldığı mahkemenin bulunduğu yerdeki uygulama, sözleşmenin ifa yerinden bağımsız olarak seçilir",
    ],
    "Kanunda aksi öngörülmedikçe bölgesel ve yerel ticari örf ve adet, genel olana üstün tutulur.",
    "6102 sayılı TTK m.2/2",
)

q(
    "Sözleşme tarafları farklı bölgelerde bulunmakta ve sözleşmede uygulanacak ticari örf ve adet belirlenmemektedir. Kanunda da özel hüküm yoksa hangi yerin ticari örf ve adeti esas alınır?",
    "İfa yerindeki ticari örf ve adet",
    [
        "Davacının merkezinin bulunduğu yerdeki ticari uygulama, ifa yeri dikkate alınmadan zorunlu olarak uygulanır",
        "Davalının yerleşim yerindeki genel uygulama, sözleşmedeki edimin nerede yerine getirileceğine bakılmadan seçilir",
        "Sözleşmenin imzalandığı yerdeki her türlü teamül, ticari örf niteliği aranmaksızın hükme esas alınır",
        "Tarafların bölgeleri farklı olduğundan ticari örf ve adetin uygulanması tamamen ortadan kalkmış sayılır",
    ],
    "Taraflar farklı bölgelerdeyse ve kanun veya sözleşmede aksi yoksa ifa yerindeki ticari örf ve adet uygulanır.",
    "6102 sayılı TTK m.2/2",
)

q(
    "Tacir olmayan bir taraf bakımından ticari örf ve adetin uygulanabilmesi için aranan temel koşul aşağıdakilerden hangisidir?",
    "Onun tarafından bilinmesi veya bilinmesinin gerekmesi",
    [
        "Ticari örf ve adetin mutlaka taraflarca imzalanmış ayrı bir metin içinde aynen tekrar edilmiş olması",
        "Tacir olmayan tarafın uyuşmazlıktan önce ticaret siciline geçici olarak tescil edilmiş bulunması",
        "Karşı tarafın da tacir olmaması ve sözleşmenin hiçbir şekilde ticari işletmeyle ilgili bulunmaması",
        "Uygulamanın yalnız yerel bir teamül olarak kalması ve ticari örf ve adet niteliğini kazanmamış olması",
    ],
    "Ticari örf ve adet, tacir olmayanlar hakkında ancak onlar tarafından bilindiği veya bilinmesi gerektiği takdirde uygulanır.",
    "6102 sayılı TTK m.2/3",
)

q(
    "Ticari örf ve adet hakkında aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Bölgesel ticari örf ve adet kural olarak genel olana üstün tutulur\n\nII. Ticari örf niteliği kazanmamış teamül hükme tek başına esas alınabilir\n\nIII. Teamül, irade açıklamalarının yorumunda dikkate alınabilir",
    "I ve III",
    [
        "I, II ve III; ticari hayatta yerleşmiş veya yerleşmemiş bütün uygulamalar aynı bağlayıcılığa sahiptir",
        "Yalnız I; teamülün yorum işlevi bulunmadığı gibi örf ve adet niteliği kazanması da önem taşımaz",
        "I ve II; ticari teamül her durumda hükme esas olurken irade açıklamalarının yorumunda kullanılamaz",
        "Yalnız III; bölgesel uygulama genel olana üstün tutulamaz ve teamül hükmün yerine doğrudan geçer",
    ],
    "Bölgesel ticari örf genel olana üstün tutulabilir ve teamül yorumda kullanılabilir. Ticari örf niteliği kazanmamış teamül tek başına hükme esas olamaz.",
    "6102 sayılı TTK m.2",
    "hard",
)

q(
    "Başka bir kanunda yer alan özel bir hüküm, bir ticari işletmeyi ilgilendiren işlem veya fiile ilişkindir. TTK bakımından bu hüküm nasıl nitelendirilir?",
    "Ticari hüküm sayılır",
    [
        "Yalnız TTK içinde yer alan kurallar ticari hüküm olabileceğinden genel hüküm olarak uygulanır",
        "Tarafların her ikisi tacir değilse hüküm ticari niteliğini kesin olarak kaybeder ve uygulanamaz",
        "Hüküm ancak ticaret siciline ayrıca tescil edilirse ticari nitelik kazanarak uyuşmazlığa uygulanır",
        "Başka kanundaki bütün hükümler konuya bakılmaksızın ticari hüküm sayıldığı için kapsam incelemesi yapılmaz",
    ],
    "Diğer kanunlardaki, bir ticari işletmeyi ilgilendiren işlem ve fiillere ilişkin özel hükümler de ticari hükümlerdendir.",
    "6102 sayılı TTK m.1/1",
)

q(
    "Tarafların tacir olup olmadığına bakılmaksızın TTK'da düzenlenen bir hususla ilgili işlem kural olarak nasıl nitelendirilir?",
    "Ticari iş sayılır",
    [
        "Taraflardan en az ikisinin ticaret siciline kayıtlı olması aranır; aksi hâlde işlem adi iş olarak kalır",
        "İşlemin ayrıca her iki tarafın ticari işletmesiyle ilgili olması zorunludur; TTK'da düzenlenmesi yeterli değildir",
        "İşlem yalnız bir gerçek kişi tarafından yapılmışsa kanuni düzenleme ne olursa olsun tüketici işlemi sayılır",
        "TTK'da düzenlenen hususlar ancak bir ticari dava açıldıktan sonra ticari iş niteliğini kazanabilir",
    ],
    "TTK'da düzenlenen hususlar, tarafların sıfatından bağımsız olarak ticari iş sayılır.",
    "6102 sayılı TTK m.3",
    "easy",
)

q(
    "TTK'da özel olarak düzenlenmemiş bir fiil, doğrudan bir ticari işletmenin faaliyetiyle ilgilidir. Bu fiilin niteliği nedir?",
    "Ticari iştir",
    [
        "TTK'da adıyla düzenlenmediğinden tarafların tacir sıfatına bakılmaksızın mutlaka adi iş olarak kabul edilir",
        "Fiilin ticari sayılması için ayrıca bir mahkeme kararıyla ticari iş olduğunun önceden tespit edilmesi gerekir",
        "Sadece ticaret sicili müdürlüğü fiili ilan ederse ticari iş niteliği doğar; işletmeyle bağlantı yeterli değildir",
        "Ticari işletmeyle ilgili fiiller yalnız sözleşmeden doğarsa ticari sayılır; haksız fiiller kapsam dışında kalır",
    ],
    "Bir ticari işletmeyi ilgilendiren bütün işlem ve fiiller, TTK m.3 uyarınca ticari iş niteliğindedir.",
    "6102 sayılı TTK m.3",
)

q(
    "Ticari uyuşmazlıkta ne uygulanabilir ticari hüküm ne de ticari örf ve adet bulunmaktadır. Hâkim hangi kaynağa başvurur?",
    "Genel hükümlere",
    [
        "Ticari uyuşmazlıkta genel hükümlere hiçbir zaman başvurulamayacağından davayı hukuki boşluk nedeniyle reddeder",
        "Uyuşmazlığın konusuyla ilgisiz olsa da ticaret odasının tavsiye kararını emredici hukuk kuralı olarak uygular",
        "Tarafların sonradan tek taraflı hazırladığı iç yönetmeliği ticari örf yerine geçirerek hükme esas alır",
        "Sadece hakkaniyete göre karar verir ve yürürlükteki genel hukuk hükümlerini tamamen değerlendirme dışı bırakır",
    ],
    "Ticari hüküm ve ticari örf ve adet bulunmazsa hâkim genel hükümlere göre karar verir.",
    "6102 sayılı TTK m.1/2",
)

q(
    "Bir sözleşme ifadesinin sektördeki yerleşik kullanım nedeniyle iki farklı anlama gelebilmesi hâlinde, henüz ticari örf sayılmayan uygulamadan nasıl yararlanılabilir?",
    "Sözleşme iradesini yorumlamak için",
    [
        "Kanunun açık hükmünü bertaraf ederek taraflar için yeni bir asli borç yaratmak amacıyla doğrudan uygulanabilir",
        "Uygulama henüz ticari örf olmadığından sözleşme yorumu dâhil hiçbir hukuki değerlendirmede kullanılamaz",
        "Yalnız cezai sorumluluk doğurmak üzere maddi ceza normunun yerine geçen bir kaynak olarak değerlendirilebilir",
        "Ticaret sicili kaydını kendiliğinden değiştirmek ve üçüncü kişilere karşı yeni bir ayni hak kurmak için kullanılabilir",
    ],
    "Ticari örf niteliği kazanmamış teamül hükme esas olamaz; fakat irade açıklamalarının yorumunda dikkate alınabilir.",
    "6102 sayılı TTK m.2/1",
)

q(
    "Aşağıdakilerden hangisi TTK anlamında ticari hüküm kapsamının belirlenmesinde doğru ölçüttür?",
    "Düzenlemenin ticari işletmeyi ilgilendiren işlem veya fiile özgü olması",
    [
        "Bir hükmün yalnızca kanunun başlığında ticaret kelimesi geçmesi hâlinde ticari hüküm sayılması yeterlidir",
        "Her özel hukuk hükmünün taraflardan biri tacir olmasa bile kendiliğinden ticari hüküm olarak kabul edilmesi gerekir",
        "Yalnız ticaret mahkemesinin daha önce uyguladığı hükümler ticari nitelik kazanır; kanuni kapsam önem taşımaz",
        "Hükmün ticari sayılabilmesi için tüm tarafların anonim veya limited şirket biçiminde örgütlenmesi zorunludur",
    ],
    "TTK hükümleri ile diğer kanunların ticari işletmeyi ilgilendiren işlem ve fiillere ilişkin özel hükümleri ticari hükümlerdir.",
    "6102 sayılı TTK m.1/1",
)

q(
    "Bir ticari işletmenin üretim faaliyetinden kaynaklanan çevreye zarar verme fiili, sözleşmeye dayanmamasına rağmen TTK m.3 yönünden nasıl değerlendirilir?",
    "Ticari işletmeyi ilgilendirdiği için ticari iş sayılır",
    [
        "Haksız fiiller hiçbir koşulda ticari iş olamayacağından yalnız genel hükümlere tabi adi iş sayılır",
        "Fiilin ticari sayılması için zarar görenin de tacir olması ve aynı sektörde faaliyet göstermesi zorunludur",
        "Yalnız işletme sahibinin kastı kanıtlanırsa ticari iş olur; kusur derecesi ticari niteliği belirler",
        "Ticari işletmeyle bağlantı yeterli değildir; fiilin ayrıca TTK'da özel olarak adıyla düzenlenmesi gerekir",
    ],
    "TTK m.3, ticari işletmeyi ilgilendiren yalnız işlemleri değil fiilleri de ticari iş kabul eder.",
    "6102 sayılı TTK m.3",
    "hard",
)

q(
    "Ticari hükümlerin uygulanma sırasına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Sözleşme hükmü emredici kurallara aykırı değilse öncelikle dikkate alınır\n\nII. Uygulanabilir ticari hüküm yoksa ticari örf ve adete başvurulur\n\nIII. Ticari örf ve adet de yoksa hâkim uyuşmazlığı çözmekten kaçınır",
    "I ve II",
    [
        "I, II ve III; ticari örf ve adet bulunmadığında hâkim genel hükümlere başvurmadan davayı reddetmelidir",
        "Yalnız I; ticari örf ve adet ticari uyuşmazlıklarda hiçbir koşulda tamamlayıcı kaynak olarak uygulanamaz",
        "II ve III; tarafların geçerli sözleşme hükümleri kaynak sıralamasında dikkate alınamaz ve uygulanamaz",
        "Yalnız III; ticari hüküm ile ticari örf aynı düzeyde bulunduğundan hâkim uyuşmazlığı çözmekten kaçınır",
    ],
    "Emredici kurallara aykırı olmayan sözleşme hükmü bağlayıcıdır. Kanuni boşlukta ticari örf ve adet, o da yoksa genel hükümler uygulanır; hâkim çözümden kaçınamaz.",
    "6102 sayılı TTK m.1-2",
    "hard",
)

q(
    "Bir sektörde genel uygulama ile alt sektöre özgü ticari örf ve adet farklı sonuçlar doğuruyorsa, özel uygulamanın tercih edilmesinin dayanağı nedir?",
    "Özel ticari örf ve adetin genel olana üstün tutulması",
    [
        "Genel ticari örf ve adetin her durumda özel sektörel uygulamayı hükümsüz bırakması gerektiği ilkesi",
        "Ticari örf ve adetler arasında kapsam farkı gözetilemeyeceği için hâkimin yalnız genel hükümleri uygulaması",
        "Alt sektördeki her tekrarlanan davranışın örf niteliği araştırılmadan kanun hükmü sayılması zorunluluğu",
        "Özel uygulamanın yalnız taraflardan birinin iç talimatında yer almasının bağlayıcılık için yeterli olması",
    ],
    "Özel veya sektörel ticari örf ve adet, kanunda aksi öngörülmedikçe genel ticari örf ve adete üstün tutulur.",
    "6102 sayılı TTK m.2/2",
)

# ── B. Ticari davalar, arabuluculuk, teselsül ve faiz (15) ─────────────────
q(
    "İki tacirin ticari işletmelerini ilgilendiren bir tedarik sözleşmesinden doğan uyuşmazlık, TTK m.4 bakımından nasıl nitelendirilir?",
    "Nispi ticari dava",
    [
        "Tarafların tacir olması yeterli görülmediğinden her durumda adi hukuk davası olarak genel mahkemede görülür",
        "TTK'da tedarik sözleşmesi adıyla düzenlenmediği için çekişmesiz yargı işi sayılarak dava konusu yapılamaz",
        "Yalnız sözleşmenin bedeli ödenmişse ticari dava niteliği doğar; alacak uyuşmazlıkları kapsam dışında kalır",
        "Tarafların işletmeleriyle bağlantı kurulsa da uyuşmazlık sadece vergi mahkemesinin görev alanına girer",
    ],
    "Her iki tarafın ticari işletmesini ilgilendiren hususlardan doğan hukuk davaları nispi ticari davadır.",
    "6102 sayılı TTK m.4/1",
    "easy",
)

q(
    "TTK'da düzenlenen bir husustan doğan hukuk davasında taraflardan hiçbiri tacir değildir. Davanın niteliği nedir?",
    "Mutlak ticari davadır",
    [
        "Tarafların tacir olmaması nedeniyle dava hiçbir koşulda ticari sayılamaz ve yalnız tüketici davası kabul edilir",
        "Uyuşmazlığın ticari sayılması için taraflardan en az birinin ticaret siciline kayıtlı bulunması zorunludur",
        "Dava ancak iki tarafın da ticari işletmesiyle ilgiliyse ticari olur; TTK'da düzenlenmiş olması etkisizdir",
        "Tarafların sıfatı nedeniyle uyuşmazlık idari dava hâline gelir ve adli yargıda incelenemez",
    ],
    "TTK'da düzenlenen hususlardan doğan davalar, tarafların tacir olup olmadığına bakılmaksızın ticari davadır.",
    "6102 sayılı TTK m.4/1-a",
)

q(
    "Bir ticari işletmenin aktif ve pasifleriyle devrinden doğan TBK m.202 kapsamındaki uyuşmazlıkta taraflar tacir değilse dava nasıl değerlendirilir?",
    "Mutlak ticari dava sayılır",
    [
        "Taraflar tacir olmadığı için uyuşmazlık ticari nitelik kazanamaz ve görev bakımından yalnız sulh hukukta görülür",
        "Davanın ticari sayılması için devralanın ayrıca anonim şirket olması ve sicile önceden tescil edilmesi gerekir",
        "TBK'dan doğan hiçbir uyuşmazlık TTK kapsamında ticari dava sayılamayacağından genel dava olarak kalır",
        "İşletme devri ancak taşınmaz içeriyorsa ticari dava olur; aktif ve pasiflerin devri tek başına yeterli değildir",
    ],
    "TTK m.4, TBK m.202 ve 203'te düzenlenen işletme veya malvarlığı devri uyuşmazlıklarını taraf sıfatından bağımsız olarak ticari dava sayar.",
    "6102 sayılı TTK m.4/1-c; 6098 sayılı TBK m.202",
    "hard",
)

q(
    "Konusu bir miktar para olan ticari alacak davası açılmadan önce hangi usulün yerine getirilmesi dava şartıdır?",
    "Arabulucuya başvuru",
    [
        "Ticaret sicili müdürlüğünden alacağın kesinliğini gösteren bağlayıcı bir uygunluk belgesi alınması",
        "Alacak tutarının tamamının mahkeme veznesine teminat olarak önceden yatırılması ve ilan edilmesi",
        "Tarafların uyuşmazlığı önce zorunlu tahkime götürüp hakem kararının iptalini talep etmiş olması",
        "Alacağın her durumda noter senedine bağlanması ve borçlu tarafından ayrıca yazılı kabul edilmesi",
    ],
    "Konusu bir miktar para olan ticari alacak davalarında dava açılmadan önce arabulucuya başvurulması dava şartıdır.",
    "6102 sayılı TTK m.5/A-1",
    "easy",
)

q(
    "Konusu bir miktar para olan ticari menfi tespit davası bakımından 2023 değişikliği sonrasında hangi sonuç geçerlidir?",
    "Dava öncesi arabuluculuk dava şartıdır",
    [
        "Menfi tespit davaları para konusu taşısa bile arabuluculuğun açıkça dışında bırakıldığından doğrudan açılır",
        "Arabuluculuk yalnız davalı isterse dava şartına dönüşür; başvuru zorunluluğu kanundan doğmaz",
        "Uyuşmazlık ticari olsa dahi menfi tespit talebi yalnız icra mahkemesinde ve arabulucusuz ileri sürülebilir",
        "Dava şartı yalnız aynen ifa taleplerinde uygulanır; para borcuna ilişkin tespit davalarında uygulanamaz",
    ],
    "TTK m.5/A'nın güncel metni, konusu bir miktar para olan menfi tespit davalarını da zorunlu arabuluculuk kapsamına alır.",
    "6102 sayılı TTK m.5/A-1 (7445 sayılı Kanun değişikliği)",
)

q(
    "Ticari davalarda dava şartı arabuluculuğa ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Konusu bir miktar para olan itirazın iptali davasını kapsar\n\nII. Konusu bir miktar para olan istirdat davasını kapsar\n\nIII. Arabulucu dosyayı kural olarak altı hafta içinde sonuçlandırır",
    "I, II ve III",
    [
        "Yalnız I; istirdat davası ile arabulucunun kanuni sonuçlandırma süresi TTK'da düzenlenmemiştir",
        "I ve II; arabuluculuk için herhangi bir sonuçlandırma süresi bulunmadığından üçüncü önerme yanlıştır",
        "II ve III; itirazın iptali davaları para konusu taşısa bile zorunlu arabuluculuk dışında bırakılmıştır",
        "Yalnız III; para konusu taşıyan tespit ve iade davaları ticari arabuluculuk kapsamına hiçbir zaman girmez",
    ],
    "Para konulu itirazın iptali ve istirdat davaları kapsamdadır. Arabulucunun olağan sonuçlandırma süresi görevlendirmeden itibaren altı haftadır.",
    "6102 sayılı TTK m.5/A",
    "hard",
)

q(
    "Ticari dava şartı arabuluculukta arabulucunun dosyayı sonuçlandırma süresi ve uzatma olanağı hangisidir?",
    "Altı hafta; zorunlu hâlde en çok iki hafta uzatma",
    [
        "Dört hafta; taraflardan birinin tek taraflı bildirimiyle ayrıca dört hafta sınırsız uzatma olanağı",
        "Sekiz hafta; zorunlu hâl aranmaksızın arabulucunun her defasında sekiz hafta daha uzatabilmesi",
        "İki hafta; yalnız mahkeme kararıyla ve tarafların tamamı kabul ederse altı ay süreyle uzatılması",
        "Bir ay; ticaret sicili müdürlüğünün izniyle herhangi bir üst sınır olmadan uzatma yapılabilmesi",
    ],
    "Arabulucu başvuruyu görevlendirildiği tarihten itibaren altı haftada sonuçlandırır; zorunlu hâllerde en fazla iki hafta uzatabilir.",
    "6102 sayılı TTK m.5/A-2",
)

q(
    "Asliye ticaret mahkemesi bulunmayan bir yargı çevresinde açılan ticari davada görev kuralına dayanılmamışsa asliye hukuk mahkemesi ne yapar?",
    "Davaya devam eder",
    [
        "Asliye ticaret mahkemesi bulunmadığı için davayı görev yönünden kesin olarak reddedip dosyayı kapatır",
        "Dosyayı kendiliğinden en yakın ilin vergi mahkemesine gönderir ve adli yargının görevini sona erdirir",
        "Tarafların tacir olup olmadığını incelemeden uyuşmazlığı zorunlu tahkime sevk ederek yargılamayı bitirir",
        "Görev itirazı ileri sürülmemiş olsa bile görevsizlik kararı verip davacının yeniden dava açmasını bekler",
    ],
    "Ticaret mahkemesi bulunmayan yerde görev kuralına dayanılmaması görevsizlik kararı verilmesini gerektirmez; asliye hukuk mahkemesi davaya devam eder.",
    "6102 sayılı TTK m.5/4",
)

q(
    "Asliye ticaret mahkemesi ile asliye hukuk mahkemesi arasındaki ilişki TTK'ya göre nasıl nitelendirilir?",
    "Görev ilişkisi",
    [
        "Yalnız iş bölümü ilişkisi olup taraflar itiraz etmedikçe mahkeme tarafından hiçbir biçimde dikkate alınamaz",
        "Kesin yetki ilişkisi olup uyuşmazlığın ticari olup olmadığı görev bakımından hiçbir sonuç doğurmaz",
        "İdari vesayet ilişkisi olup asliye hukuk mahkemesi ticaret mahkemesinin tüm kararlarını denetler",
        "Tahkim ilişkisi olup ticari uyuşmazlıkların tamamı devlet mahkemeleri dışında hakemlerce çözülür",
    ],
    "Asliye ticaret ile asliye hukuk ve diğer hukuk mahkemeleri arasındaki ilişki görev ilişkisidir.",
    "6102 sayılı TTK m.5/3",
    "easy",
)

q(
    "Ticari hükümler koyan kanunda öngörülmüş bir zamanaşımı süresi, kanunda izin veren özel düzenleme yoksa taraf sözleşmesiyle nasıl değiştirilebilir?",
    "Değiştirilemez",
    [
        "Tacirler sözleşme serbestisi gereğince her türlü zamanaşımı süresini sınırsız biçimde uzatıp kısaltabilir",
        "Yalnız noter onayı alınarak süre yarıya indirilebilir ve mahkemenin bunu denetleme yetkisi bulunmaz",
        "Taraflardan biri tacir olduğu anda süre kendiliğinden iki katına çıkar ve sözleşmeyle yeniden belirlenebilir",
        "Süre yalnız ticaret sicilinde ilan edilirse tamamen kaldırılabilir ve alacak süresiz hâle getirilebilir",
    ],
    "Ticari kanunlardaki zamanaşımı süreleri, kanunda aksi düzenlenmedikçe sözleşmeyle değiştirilemez.",
    "6102 sayılı TTK m.6",
)

q(
    "Üç kişi, içlerinden yalnız biri için ticari nitelik taşıyan bir iş nedeniyle alacaklıya karşı birlikte borçlanmıştır. Kanun ve sözleşmede aksi yoksa sorumlulukları nasıldır?",
    "Müteselsildir",
    [
        "Her borçlu yalnız eşit payından sorumludur; işin biri bakımından ticari olması teselsül karinesi doğurmaz",
        "Yalnız tacir olan borçlu borcun tamamından, diğerleri ise hiçbir tutardan sorumlu tutulamaz",
        "Alacaklı önce ticari işi olmayan borçlulara başvurmak zorundadır; tacire en son başvurabilir",
        "Teselsül ancak borçluların tamamı için iş ticariyse doğar; bir kişi bakımından ticari nitelik yetersizdir",
    ],
    "Birlikte borçlanılan iş içlerinden yalnız biri için ticari olsa bile, aksi kararlaştırılmadıkça müteselsil sorumluluk karinesi geçerlidir.",
    "6102 sayılı TTK m.7/1",
)

q(
    "Ticari borca kefil olan kişiye, asıl borcun ödenmediği bildirilmeden hangi ferî alacak yürütülemez?",
    "Temerrüt faizi",
    [
        "Asıl borcun muaccel olması bütünüyle engellenir ve alacaklı borcun kendisini de hiçbir zaman isteyemez",
        "Kefalet sözleşmesi bildirim yapılmadığı anda kesin hükümsüz olur ve sonradan bildirimle geçerli hâle gelemez",
        "Asıl borçlu yönünden sözleşme faizi kendiliğinden silinir ve kefilin sorumluluğundan bağımsız olarak sona erer",
        "Alacaklının bütün teminatları bildirim yapılmadığı için geriye etkili biçimde ortadan kalkmış kabul edilir",
    ],
    "Kefile taahhüt veya ödemenin yerine getirilmediği ihbar edilmeden kefil hakkında temerrüt faizi yürütülemez.",
    "6102 sayılı TTK m.7/1",
)

q(
    "Ticari borçlara kefalette teselsül karinesi hangi ilişkilerde uygulanır?",
    "Hem asıl borçlu-kefil hem de kefiller arasında",
    [
        "Yalnız alacaklı ile asıl borçlu arasında uygulanır; kefillerin ticari borç bakımından hiçbir sorumluluğu doğmaz",
        "Sadece birden fazla kefilin kendi aralarındaki iç ilişkide uygulanır; asıl borçlu ile kefil kapsam dışıdır",
        "Yalnız kefil tacir değilse uygulanır; tacir kefiller bakımından her durumda adi paylı sorumluluk geçerlidir",
        "Hiçbir kefalet ilişkisinde uygulanmaz; ticari borçlarda dahi teselsülün açıkça ayrıca yazılması zorunludur",
    ],
    "Ticari borçlara kefalette teselsül karinesi hem asıl borçlu ile kefil hem de kefiller arasındaki ilişkilerde uygulanır.",
    "6102 sayılı TTK m.7/2",
)

q(
    "Faizin anaparaya eklenerek yeniden faiz yürütülmesine ilişkin bir kayıt hangi durumda TTK m.8'e uygun olabilir?",
    "Üç aydan kısa olmayan dönemli cari hesapta",
    [
        "Taraflardan hiçbiri tacir olmasa bile bir aylık dönemlerle yapılan her türlü adi tüketim ödüncünde",
        "Tüketici işleminde tarafların yazılı anlaşması varsa iki aylık dönemlerle sınırsız bileşik faiz uygulanmasında",
        "Her iki taraf için de ticari olmayan ödünç sözleşmesinde haftalık dönemlerle faiz anaparaya eklenmesinde",
        "Cari hesap veya ticari ödünç dışında kalan tüm sözleşmelerde yalnız alacaklının tek taraflı bildirimiyle",
    ],
    "Bileşik faiz, üç aydan aşağı olmayan dönemlerle cari hesaplarda veya iki taraf için de ticari olan ödünçlerde ve tacir taraflar bakımından geçerli olabilir.",
    "6102 sayılı TTK m.8/2",
    "hard",
)

q(
    "Ticari işlerde faiz hakkında aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Faiz oranı kural olarak serbestçe belirlenebilir\n\nII. Bileşik faiz her sözleşmede ve bir aylık dönemlerle kararlaştırılabilir\n\nIII. Vade yoksa aksi kararlaştırılmadıkça faiz ihtar gününden başlar",
    "I ve III",
    [
        "I, II ve III; ticari işlerde bileşik faiz bakımından sözleşme türü ve dönem yönünden hiçbir sınırlama yoktur",
        "Yalnız I; vadesiz ticari borçta faiz ihtarla başlamaz ve bileşik faize ilişkin kanuni sınır bulunmamaktadır",
        "I ve II; vadesiz ticari borçta faiz hiçbir zaman işlemeye başlamaz ve ihtar hukuki sonuç doğurmaz",
        "Yalnız III; ticari işlerde faiz oranı taraflarca belirlenemez ve her durumda tek bir kanuni oran uygulanır",
    ],
    "Ticari faiz oranı kural olarak serbesttir. Bileşik faiz yalnız sınırlı sözleşmelerde ve en az üç aylık dönemlerle geçerlidir. Vade yoksa faiz ihtar gününde başlar.",
    "6102 sayılı TTK m.8 ve m.10",
    "hard",
)

# ── C. Ticari işletmenin unsurları ve bütün hâlinde devri (15) ─────────────
q(
    "Bir faaliyet yüksek ciro yaratmasına karşın gelir sağlamayı hedeflemiyor ve sürekli bağış amacıyla yürütülüyorsa TTK m.11'deki ticari işletme tanımının hangi unsuru eksiktir?",
    "Gelir sağlama hedefi",
    [
        "Faaliyetin mutlaka anonim şirket tarafından yürütülmesi şartı gerçekleşmediğinden tüzel kişilik unsuru eksiktir",
        "İşletmenin her takvim yılında fiilen kâr dağıtması gerektiğinden ortaklara temettü ödeme unsuru eksiktir",
        "Ticari işletmenin yalnız taşınmaz sahibi olabilmesi nedeniyle ayni hak edinme kapasitesi unsuru eksiktir",
        "Her işletmenin kamu kurumu tarafından ruhsatlandırılması zorunlu olduğundan idari kuruluş işlemi unsuru eksiktir",
    ],
    "Ticari işletme tanımı fiilen kâr elde etmeyi değil, esnaf sınırını aşan düzeyde gelir sağlamayı hedeflemeyi arar.",
    "6102 sayılı TTK m.11/1",
)

q(
    "Bir şirketin merkez örgütüne bağlı, kendi kararlarını alamayan ve tüm işlemleri merkez adına yürüten iç departman neden tek başına ticari işletme sayılmaz?",
    "Bağımsızlık unsuru yoktur",
    [
        "Departmanın ayrı bir ticaret unvanı seçmemesi her durumda gelir hedefini ve devamlılığı ortadan kaldırır",
        "Ticari işletmenin yalnız gerçek kişilerce işletilebilmesi nedeniyle şirket bünyesindeki birim kapsam dışında kalır",
        "Departmanın çalışan sayısı kanunda belirtilen asgari sayıya ulaşmadığından ticari işletme niteliği doğmaz",
        "Ticari işletme için mutlaka taşınmaz mülkiyeti gerektiğinden kiralanan yerde çalışan birim bağımsız olamaz",
    ],
    "Ticari işletmede faaliyetlerin devamlı ve bağımsız yürütülmesi gerekir. Merkezin iç örgütüne tamamen bağlı departman bağımsız değildir.",
    "6102 sayılı TTK m.11/1",
)

q(
    "Yalnız bir defaya özgü ve tekrar amacı taşımayan münferit mal satışı, ticari işletme tanımında öncelikle hangi unsur yönünden yetersizdir?",
    "Devamlılık",
    [
        "Her satışın noter huzurunda yapılması zorunlu olduğundan resmi şekil unsuru yönünden yetersiz kabul edilir",
        "Satıcının mutlaka ticaret şirketi olması gerektiğinden tüzel kişilik unsuru yönünden yetersiz sayılır",
        "Satılan mal taşınır olduğu için ticari işletmenin yalnız taşınmazlara ilişkin faaliyet koşulu gerçekleşmez",
        "Satış bedeli peşin tahsil edildiğinden ticari faaliyetin zorunlu kredi kullanma unsuru meydana gelmemiştir",
    ],
    "Ticari işletme faaliyeti devamlı yürütülmelidir. Tekrar amacı taşımayan münferit işlem devamlılık unsurunu karşılamaz.",
    "6102 sayılı TTK m.11/1",
    "easy",
)

q(
    "Ticari işletmenin unsurlarına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Faaliyetler gelir sağlamayı hedeflemelidir\n\nII. Faaliyetler devamlı yürütülmelidir\n\nIII. Faaliyetler bağımsız yürütülmelidir",
    "I, II ve III",
    [
        "Yalnız I; devamlılık ve bağımsızlık ticari işletme tanımında aranan kanuni unsurlar arasında bulunmaz",
        "I ve II; işletmenin mutlaka başka bir merkeze bağımlı yürütülmesi gerektiğinden bağımsızlık aranmaz",
        "II ve III; gelir sağlama hedefi yerine yalnız kamu hizmeti amacı taşıyan her faaliyet ticari işletmedir",
        "Yalnız III; gelir hedefi ve devamlılık bulunmasa bile bağımsız yürütülen her münferit işlem yeterlidir",
    ],
    "TTK m.11; esnaf sınırını aşan gelir hedefi, devamlılık ve bağımsızlığı birlikte ticari işletme tanımının unsurları olarak düzenler.",
    "6102 sayılı TTK m.11/1",
)

q(
    "Ticari işletme ile esnaf işletmesi arasındaki gelir sınırını belirleme yetkisi kime aittir?",
    "Cumhurbaşkanına",
    [
        "Her belediye meclisi kendi bölgesi için bağlayıcı bir sınır belirleyerek ülke çapında farklı ölçütler oluşturur",
        "Yargıtay her uyuşmazlıkta yeni bir parasal sınır belirler ve bu sınır geçmişe etkili olarak uygulanır",
        "Ticaret sicili müdürleri işletme bazında takdirî sınır belirler; merkezi bir karar alınması mümkün değildir",
        "Taraflar sözleşmeyle esnaf sınırını serbestçe belirler ve kamu makamlarının buna müdahale yetkisi bulunmaz",
    ],
    "Ticari işletme ile esnaf işletmesi arasındaki sınır Cumhurbaşkanı kararıyla belirlenir.",
    "6102 sayılı TTK m.11/2",
    "easy",
)

q(
    "Ticari işletmenin bütün hâlinde devrinde, içerdiği malvarlığı unsurları için ayrı ayrı zorunlu tasarruf işlemi yapılması gerekir mi?",
    "Gerekmez",
    [
        "Her unsur için mutlaka ayrı sözleşme yapılmadıkça ticari işletmenin bütün hâlinde devri kesin hükümsüzdür",
        "Yalnız taşınırlar topluca devredilebilir; diğer bütün unsurlar için ayrı tasarruf işlemi zorunludur",
        "Bütünlük ilkesi yalnız kamu işletmelerinde geçerli olup özel ticari işletmelerde hiçbir sonuç doğurmaz",
        "Ayrı tasarruf işlemleri ancak devralanın tacir olmadığı durumda gereksizdir; tacir devralanda zorunludur",
    ],
    "TTK m.11/3, ticari işletmenin malvarlığı unsurları için ayrı ayrı zorunlu tasarruf işlemleri yapılmadan bütün hâlinde devrine izin verir.",
    "6102 sayılı TTK m.11/3",
)

q(
    "Aksi kararlaştırılmamış bir ticari işletme devri sözleşmesinin kapsamına kural olarak hangisi girer?",
    "İşletme değeri",
    [
        "Devredenin işletmeyle ilgisiz kişisel konutu ve aile kullanımına ayrılmış bütün taşınır malları",
        "Devreden tacirin gelecekte kurabileceği başka işletmelerde doğacak henüz mevcut olmayan tüm hakları",
        "İşletmenin faaliyetine özgülenmemiş ve devredenin özel yatırım amacıyla edindiği kişisel varlıkları",
        "Devredenin işletme dışındaki kişisel borçlarının tamamı ile aile bireylerinin özel yükümlülükleri",
    ],
    "Aksi öngörülmemişse devir; duran malvarlığını, işletme değerini, kiracılık hakkını, ticaret unvanı ve diğer fikrî hakları ve sürekli özgülenen unsurları kapsar.",
    "6102 sayılı TTK m.11/3",
)

q(
    "Taraflar, ticari işletme devrinde işletmeye sürekli özgülenmiş belirli bir makinenin kapsam dışında kalacağını açıkça kararlaştırabilir mi?",
    "Evet, aksi kararlaştırılabilir",
    [
        "Hayır, işletmeye özgülenen hiçbir unsur taraf iradesiyle devir kapsamı dışında bırakılamaz",
        "Yalnız devralan tacir değilse kapsam daraltılabilir; tacirler arasında bütün unsurlar zorunlu olarak geçer",
        "Makinenin kapsam dışında kalması için işletme devrinin tamamının sözlü yapılması ve tescilden kaçınılması gerekir",
        "Kapsamı değiştirme yetkisi yalnız ticaret sicili müdürüne ait olup tarafların bu konuda söz hakkı bulunmaz",
    ],
    "TTK m.11/3'te sayılan unsurlar 'aksi öngörülmemişse' devir kapsamında kabul edilir; taraflar belirli unsurları kapsam dışında bırakabilir.",
    "6102 sayılı TTK m.11/3",
)

q(
    "Ticari işletmeyi bütün hâlinde konu alan devir sözleşmesinin şekli ve sicil işlemi bakımından doğru ifade hangisidir?",
    "Yazılı yapılır, ticaret siciline tescil ve ilan edilir",
    [
        "Sözlü yapılması yeterlidir; ticaret siciline tescil veya ilan edilmesine hiçbir durumda gerek bulunmaz",
        "Yalnız noterlikte düzenleme biçiminde yapılabilir ve ticaret sicili yerine tapu siciline kaydedilir",
        "Tarafların elektronik posta yazışması olmadan geçersizdir; yazılı sözleşme ve sicil işlemi yasaklanmıştır",
        "Sadece ticaret odasının yönetim kurulu kararıyla kurulur; taraflar arasında sözleşme yapılmasına gerek yoktur",
    ],
    "Ticari işletme devir sözleşmesi yazılı yapılır; ticaret siciline tescil ve ilan edilir.",
    "6102 sayılı TTK m.11/3",
)

q(
    "Ticari işletme, devir dışında rehin veya benzeri başka bir hukuki işleme bütün olarak konu edilebilir mi?",
    "Kanunen mümkündür",
    [
        "Ticari işletme yalnız satılabilir; devir dışındaki hiçbir hukuki işleme konu edilmesi mümkün değildir",
        "Bütün olarak işlem yapılması sadece tasfiye hâlindeki kamu işletmeleri için kabul edilen istisnai bir yoldur",
        "İşletmenin hukuki işleme konu olabilmesi için bütün malvarlığı unsurlarının önce ayrı tüzel kişilik kazanması gerekir",
        "Devir dışındaki işlemler ancak işletme faaliyeti tamamen sona erdikten ve sicil kaydı silindikten sonra yapılabilir",
    ],
    "TTK m.11/3, ticari işletmenin bütün hâlinde devredilebilmesinin yanında diğer hukuki işlemlere de konu olabileceğini açıkça düzenler.",
    "6102 sayılı TTK m.11/3",
)

q(
    "Ticari işletmenin kiracılık hakkı, devir sözleşmesinde aksi kararlaştırılmamışsa kural olarak ne olur?",
    "Devir kapsamına dâhil kabul edilir",
    [
        "Kiracılık hakkı işletmeyle birlikte hiçbir zaman devredilemez ve tarafların aksi yöndeki iradesi de geçersizdir",
        "Kiracılık hakkı kendiliğinden sona erer; devralan aynı yerde faaliyet göstermek için mutlaka yeni taşınmaz satın alır",
        "Kiracılık hakkı yalnız devredenin kişisel malvarlığında kalır ve işletmeyle bağlantısı kanunen yok sayılır",
        "Devir sözleşmesinde hiçbir hüküm yoksa kiracılık hakkı doğrudan belediyeye geçer ve kamu malı hâline gelir",
    ],
    "Aksi öngörülmemişse kiracılık hakkı ticari işletme devir sözleşmesinin kapsamına dâhil kabul edilir.",
    "6102 sayılı TTK m.11/3",
)

q(
    "Bir ticari işletmeyi aktif ve pasifleriyle devralan kişinin işletme borçlarına karşı sorumluluğu alacaklılara bildirim veya ilan bakımından ne zaman doğar?",
    "Bildirim veya Ticaret Sicili Gazetesi ilanı tarihinde",
    [
        "Devir sözleşmesi görüşülmeye başlandığı anda, devralanın kabulü aranmadan ve geriye etkili biçimde doğar",
        "Yalnız bütün alacaklılar noter huzurunda ayrı ayrı muvafakat verdikten sonra sorumluluk meydana gelir",
        "Ticari işletme faaliyeti sona erdikten ve sicil kaydı silindikten sonra geçmişe etkili olarak ortaya çıkar",
        "Devirden beş yıl sonra kendiliğinden doğar; bildirim veya ilanın sorumluluğun başlangıcına hiçbir etkisi yoktur",
    ],
    "Devralan, devri alacaklılara bildirdiği veya ticari işletmeler için Ticaret Sicili Gazetesinde ilan ettiği tarihten itibaren borçlardan sorumlu olur.",
    "6098 sayılı TBK m.202/1",
)

q(
    "Ticari işletmenin aktif ve pasifleriyle devrinde önceki borçlunun sorumluluğu kural olarak nasıl devam eder?",
    "Devralanla birlikte iki yıl müteselsil sorumlu kalır",
    [
        "Devir sözleşmesi imzalanır imzalanmaz bütün borçlardan kesin olarak kurtulur ve hiçbir geçiş dönemi uygulanmaz",
        "Devralanın sorumluluğu hiç doğmaz; önceki borçlu işletme borçlarından süresiz ve tek başına sorumlu kalır",
        "Önceki borçlu yalnız devralanın ödeme gücü bulunmadığı mahkeme kararıyla tespit edilirse tali sorumlu olur",
        "Sorumluluk yalnız bir ay devam eder ve alacaklılara bildirim yapılmasa da süre devir tarihinde işlemeye başlar",
    ],
    "TBK m.202 uyarınca önceki borçlu, iki yıl boyunca devralanla birlikte müteselsil borçlu olarak sorumlu kalır.",
    "6098 sayılı TBK m.202/2",
)

q(
    "İşletme devrinde önceki borçlunun iki yıllık müteselsil sorumluluk süresi, devir tarihinde henüz muaccel olmayan borç bakımından ne zaman başlar?",
    "Borcun muaccel olduğu tarihte",
    [
        "Her durumda devir sözleşmesinin ilk görüşüldüğü tarihte başlar ve bildirim ile muacceliyet dikkate alınmaz",
        "İşletme sicilden silindiği tarihte başlar; borcun muaccel olduğu tarih sürenin hesabını hiçbir şekilde etkilemez",
        "Alacaklının dava açtığı tarihte başlar ve dava açılmazsa önceki borçlunun sorumluluğu hiçbir zaman sona ermez",
        "Devralanın ilk kez kâr elde ettiği tarihte başlar; borcun ifa zamanı sorumluluk süresinden bağımsızdır",
    ],
    "İki yıllık süre, muaccel borçlarda bildirim veya ilandan; sonradan muaccel olacak borçlarda muacceliyet tarihinden işlemeye başlar.",
    "6098 sayılı TBK m.202/2",
)

q(
    "İşletme devri ve borçlar hakkında aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Devralan bildirim veya ilanla borçlardan sorumlu olur\n\nII. Önceki borçlunun iki yıllık sorumluluk süresi her borç için devir tarihinde başlar\n\nIII. Bildirim veya ilan yapılmadıkça iki yıllık süre işlemeye başlamaz",
    "I ve III",
    [
        "I, II ve III; muacceliyet ve bildirim ayrımı yapılmaksızın bütün süreler devir sözleşmesi tarihinde başlar",
        "Yalnız I; önceki borçlunun iki yıllık sorumluluğu ve sürenin başlamaması TBK'da düzenlenmemiştir",
        "I ve II; bildirim yapılmasa da iki yıllık süre her durumda devir tarihinde kendiliğinden işlemeye başlar",
        "Yalnız III; devralanın işletme borçlarına karşı sorumluluğu bildirim veya ilanla hiçbir zaman doğmaz",
    ],
    "Devralanın sorumluluğu bildirim veya ilanla doğar. Süre, muaccel borçta bildirim/ilandan; sonradan muaccel borçta muacceliyetten başlar. Bildirim veya ilan yoksa iki yıl işlemez.",
    "6098 sayılı TBK m.202",
    "hard",
)

# ── D. Tacir sıfatının kazanılması ve özel kişi grupları (15) ──────────────
q(
    "Bir kişi ticari işletmeyi başka ortaklarla birlikte, ancak kısmen kendi adına işletmektedir. TTK m.12 bakımından sıfatı nedir?",
    "Tacirdir",
    [
        "İşletmenin tamamını tek başına kendi adına işletmediği için hiçbir koşulda tacir sıfatını kazanamaz",
        "Yalnız çalışan sayısı belirli bir eşiği aşarsa tacir sayılır; kendi adına işletme ölçütü önem taşımaz",
        "Ticaret siciline kayıt yapılmasa bile sadece esnaf sayılır; ticari işletmeyle bağlantısı sonuç doğurmaz",
        "Ortaklık ilişkisi bulunduğu için işletmeyi kendi adına yürütse dahi yalnız tüketici sıfatına sahip olur",
    ],
    "Bir ticari işletmeyi kısmen de olsa kendi adına işleten gerçek kişi tacirdir.",
    "6102 sayılı TTK m.12/1",
    "easy",
)

q(
    "Bir kişi kurduğu ticari işletmeyi halka duyurmuş, fakat henüz fiilen faaliyete başlamamıştır. Tacir sıfatı bakımından sonuç nedir?",
    "Tacir sayılır",
    [
        "Fiilen ilk satış gerçekleşmedikçe halka yapılan ilan hiçbir sonuç doğurmaz ve kişi tacir sayılamaz",
        "Yalnız işletme bir ticaret şirketine dönüştürülürse tacir sıfatı doğar; gerçek kişi ilanı yetersizdir",
        "Halka duyuru kişiyi sadece esnaf yapar ve işletmenin gelir düzeyi ne olursa olsun tacirlik doğurmaz",
        "Tacir sıfatı ancak işletme beş yıl kesintisiz çalıştıktan sonra geçmişe etkili olarak kazanılabilir",
    ],
    "Ticari işletmeyi kurup açtığını ilan araçlarıyla halka bildiren kişi, fiilen işletmeye başlamasa bile tacir sayılır.",
    "6102 sayılı TTK m.12/2",
)

q(
    "Ticari işletmesini sicile tescil ettirip durumu ilan eden kişi henüz işletmeyi fiilen çalıştırmıyorsa TTK m.12'ye göre nasıl değerlendirilir?",
    "Tacir sayılır",
    [
        "Fiilî faaliyetin başlamaması nedeniyle sicil ve ilan işlemleri yok sayılır; tacir sıfatı hiçbir biçimde doğmaz",
        "Sicil işlemi yalnız vergi mükellefiyeti doğurur; ticaret hukuku bakımından herhangi bir sonuç yaratmaz",
        "Kişi sadece tacir yardımcısı sayılır ve işletmenin bütün borçlarından başka bir tacir sorumlu tutulur",
        "Tescilden sonra ayrıca ilk faturanın kesilmesi ve ticaret odasının yeni bir karar vermesi zorunludur",
    ],
    "İşletmesini ticaret siciline tescil ettirip ilan eden kişi, fiilen işletmeye başlamasa da tacir sayılır.",
    "6102 sayılı TTK m.12/2",
)

q(
    "Hukuken var olmayan bir şirket adına ortak sıfatıyla ticari işletme açmış gibi işlem yapan kişi, iyi niyetli üçüncü kişilere karşı nasıl sorumlu olur?",
    "Tacir gibi sorumlu olur",
    [
        "Hukuken var olmayan şirket bütün borçlardan sorumlu tutulur; işlemi yapan kişiye hiçbir sorumluluk yüklenemez",
        "Kişi kendiliğinden tam anlamıyla tacir sıfatını kazanır ve yalnız iyi niyetli olmayan üçüncü kişilere karşı sorumlu olur",
        "İşlem baştan yok sayılır; iyi niyetli üçüncü kişiler dâhil hiç kimse işlemi yapana karşı talepte bulunamaz",
        "Sorumluluk yalnız ticaret sicili müdürüne aittir ve işlemi yapan kişi her türlü hukuki sonuçtan bağışıktır",
    ],
    "Ticari işletme açmış gibi veya hukuken var olmayan şirket adına ortak sıfatıyla işlem yapan kişi, iyi niyetli üçüncü kişilere karşı tacir gibi sorumludur.",
    "6102 sayılı TTK m.12/3",
    "hard",
)

q(
    "Gerçek kişilerde tacir sıfatı hakkında aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İşletmeyi kısmen kendi adına işleten kişi tacirdir\n\nII. Halka açılış ilanı yapan kişi fiilen başlamadıkça tacir sayılamaz\n\nIII. Var olmayan şirket adına işlem yapan kişi iyi niyetli üçüncü kişilere karşı tacir gibi sorumludur",
    "I ve III",
    [
        "I, II ve III; tacir sıfatının kazanılması için her durumda fiilî faaliyetin başlaması zorunlu kabul edilir",
        "Yalnız I; halka ilan ve var olmayan şirket adına işlem yapılması TTK'da hiçbir sonuca bağlanmamıştır",
        "I ve II; hukuken var olmayan şirket adına işlem yapan kişi iyi niyetli üçüncü kişilere karşı sorumsuzdur",
        "Yalnız III; işletmeyi kısmen kendi adına işletmek tacirlik için yetersiz, ilan ise fiilî başlangıçtan önce etkisizdir",
    ],
    "Kısmen kendi adına işletme tacirlik için yeterlidir. Halka ilan, fiilî başlangıçtan önce de tacir sayılmayı doğurur. Var olmayan şirket adına işlem yapan kişi tacir gibi sorumludur.",
    "6102 sayılı TTK m.12",
    "hard",
)

q(
    "On yedi yaşındaki işletme sahibinin ticari işletmesini veli, temsil edilen adına yönetmektedir. Tarafların tacir sıfatı bakımından doğru sonuç hangisidir?",
    "İşletme sahibi tacirdir; veli tacir değildir",
    [
        "Veli tacirdir; temsil edilen işletme sahibi ticari işletmeyle ilgili hiçbir sıfat kazanamaz",
        "Her ikisi de ayrı ayrı tacirdir ve tek işletmenin yönetimi nedeniyle iki bağımsız ticari işletme doğar",
        "Hiçbiri tacir değildir; ergin olmayan kişiye ait bir faaliyetin ticari işletme olması hukuken mümkün değildir",
        "Tacir sıfatı vesayet makamına geçer ve işletmenin bütün özel hukuk borçlarından mahkeme sorumlu olur",
    ],
    "Küçük veya kısıtlıya ait işletmeyi onun adına yöneten yasal temsilci tacir sayılmaz; tacir sıfatı temsil edilene aittir.",
    "6102 sayılı TTK m.13",
)

q(
    "Küçüğe ait ticari işletmeyi onun adına işleten yasal temsilci, tacirlere ilişkin ceza hükümleri bakımından nasıl sorumludur?",
    "Tacir gibi sorumludur",
    [
        "Tacir olmadığı için ceza hükümleri bakımından da mutlak biçimde sorumsuzdur ve temsil edilen tek başına sorumludur",
        "Ticari işletmenin bütün özel hukuk borçlarından sınırsız sorumlu olur; ceza hükümleri ise hiçbir şekilde uygulanmaz",
        "Yalnız küçüğün açık yazılı talimatına uyduğunu kanıtlarsa ceza hükümleri bakımından tacir sıfatını kazanır",
        "Ceza sorumluluğu ticaret sicili müdürüne geçer; yasal temsilcinin davranışları hukuken dikkate alınmaz",
    ],
    "Yasal temsilci tacir sayılmaz; ancak ceza hükümlerinin uygulanması yönünden tacir gibi sorumlu olur.",
    "6102 sayılı TTK m.13",
)

q(
    "Kanundan doğan ticaret yapma yasağına rağmen kendi adına ticari işletme işleten kişi için tacir sıfatı bakımından hangi sonuç doğar?",
    "Tacir sayılır",
    [
        "Yasağa aykırılık ticari işletmeyi yok saydırır ve kişi üçüncü kişilere karşı hiçbir ticari sorumluluk taşımaz",
        "Kişi yalnız esnaf sayılır; işletmenin gelir düzeyi ile kendi adına işletilmesi hukuken dikkate alınmaz",
        "Tacir sıfatı ancak yasağın sonradan kaldırılmasıyla ve geçmişe yürümeksizin ilk kez kazanılabilir",
        "Yasağa aykırı işletme bütün borçlarıyla kendiliğinden Devlete geçer ve işleten kişi tüketici kabul edilir",
    ],
    "Ticaret yapma yasağına aykırı olarak ticari işletme işleten kişi de tacir sayılır; yasağa aykırılıktan doğan diğer sorumluluklar saklıdır.",
    "6102 sayılı TTK m.14",
)

q(
    "Resmî makam izni gereken bir faaliyette izin almadan ticari işletme işleten kişinin tacir sıfatı ve diğer sorumlulukları bakımından doğru sonuç hangisidir?",
    "Tacir sayılır; hukuki, cezai ve disiplin sorumluluğu saklıdır",
    [
        "İzin bulunmadığından tacir sayılmaz ve yaptığı bütün işlemler iyi niyetli üçüncü kişilere karşı da sonuç doğurmaz",
        "Yalnız disiplin sorumluluğu doğar; hukuki ve cezai sorumluluk izin eksikliği nedeniyle tamamen ortadan kalkar",
        "İzin sonradan alınırsa yalnız o tarihten sonraki işlemler için esnaf sayılır ve tacir sıfatı hiçbir zaman doğmaz",
        "Tacir sıfatı izin veren resmî makama geçer; işletmeyi fiilen kendi adına yürüten kişi sorumsuz kabul edilir",
    ],
    "İzin veya onay almadan ticari işletme işleten kişi de tacirdir. Yasağa aykırılığın hukuki, cezai ve disiplin sonuçları ayrıca devam eder.",
    "6102 sayılı TTK m.14",
    "hard",
)

q(
    "Bir kişinin ekonomik faaliyeti sermayesinden fazla bedenî çalışmasına dayanıyor ve geliri belirlenen sınırı aşmıyorsa TTK bakımından temel sıfatı nedir?",
    "Esnaftır",
    [
        "Faaliyetin bedensel çalışmaya dayanması önem taşımadığından gelir sınırına bakılmaksızın her durumda tacirdir",
        "Yalnız sabit dükkânda çalışanlar esnaf olabilir; gezici çalışanların herhangi bir ticari sıfat kazanması mümkün değildir",
        "Geliri sınırı aşmasa bile sermayesi bulunduğu için kendiliğinden ticaret şirketi ve tüzel kişi kabul edilir",
        "Esnaf sıfatı yalnız kamu görevlilerine özgüdür; özel kişiler bu kanuni kategoride hiçbir zaman yer alamaz",
    ],
    "Bedenî çalışması sermayesinden baskın olan ve geliri TTK m.11/2 sınırını aşmayan sanat veya ticaret erbabı esnaftır.",
    "6102 sayılı TTK m.15/1",
    "easy",
)

q(
    "Tacirin ticari işletmesiyle ilgili iş veya hizmet için uygun ücret istemesine ilişkin TTK m.20 hükmü esnafa uygulanır mı?",
    "Evet, esnafa da uygulanır",
    [
        "Hayır, tacire özgü hiçbir hüküm esnaf bakımından uygulanamaz ve esnaf yaptığı hizmet için ücret isteyemez",
        "Yalnız esnaf ticaret siciline tacir olarak tescil edilirse uygulanır; esnaf sıfatıyla uygulanması yasaktır",
        "Hüküm yalnız kamu yararına çalışan derneklere uygulanır; gerçek kişi esnaf bakımından sonuç doğurmaz",
        "Esnaf yalnız yazılı ücret sözleşmesi varsa bedel isteyebilir; TTK m.20 hiçbir tamamlayıcı hak sağlamaz",
    ],
    "TTK m.15, tacirlere özgü m.20 ve m.53 ile TMK m.950/2 hükümlerinin esnafa da uygulanacağını açıkça belirtir.",
    "6102 sayılı TTK m.15/1 ve m.20",
)

q(
    "Bir anonim şirketin henüz ticari faaliyete başlamamış olması, tüzel kişi tacir sıfatını ortadan kaldırır mı?",
    "Hayır, ticaret şirketleri tacirdir",
    [
        "Evet, bütün ticaret şirketlerinin tacir sayılması için ayrıca fiilen en az bir yıl faaliyet göstermesi gerekir",
        "Evet, yalnız gerçek kişiler tacir olabilir; ticaret şirketleri hiçbir zaman tacir sıfatı kazanamaz",
        "Şirket ancak bütün ortakları ayrı ayrı tacirse tacir sayılır; ortakların sıfatı şirket sıfatını belirler",
        "Şirket sadece kamu kurumu tarafından işletilirse tacir sayılır; özel hukuk şirketleri kapsam dışındadır",
    ],
    "Ticaret şirketleri kanun gereği tacirdir; tacir sıfatı ortakların sıfatına veya fiilî faaliyetin belirli süre sürmesine bağlanmamıştır.",
    "6102 sayılı TTK m.16/1",
)

q(
    "Bir dernek, amacına ulaşmak için ticari işletme işletmektedir ve kamu yararına çalışan dernek statüsünde değildir. TTK bakımından sıfatı nedir?",
    "Tacir sayılır",
    [
        "Dernekler tüzel kişi olduğundan ticari işletme işletse dahi hiçbir koşulda tacir sıfatı kazanamaz",
        "Yalnız dernek üyeleri ayrı ayrı tacir olur; ticari işletmeyi işleten derneğin kendisi sorumsuz kalır",
        "Dernek yalnız işletmeden zarar ederse tacir sayılır; gelir elde etmesi tacir sıfatını ortadan kaldırır",
        "Tacir sıfatı otomatik olarak belediyeye geçer ve dernek yalnız tüketici işlemi yapabilen kişi kabul edilir",
    ],
    "Amacına varmak için ticari işletme işleten dernekler, kamu yararına çalışan dernek istisnası dışında tacir sayılır.",
    "6102 sayılı TTK m.16/1-2",
)

q(
    "Bir belediye tarafından özel hukuk hükümlerine göre yönetilmek ve ticari şekilde işletilmek üzere kurulan ayrı kurumun TTK bakımından sıfatı nedir?",
    "Tacir sayılır",
    [
        "Kurucusu belediye olduğu için kurumun yönetim biçimine bakılmaksızın tacir sıfatı hiçbir zaman doğamaz",
        "Tacir sıfatı kuruma değil doğrudan belediyeye aittir ve kurumun özel hukuk tüzel kişiliği sonuç doğurmaz",
        "Kurum ancak ortaklarının tamamı gerçek kişi olduğunda tacir olabilir; kamu kuruluşları kapsam dışındadır",
        "Özel hukuk hükümlerine göre yönetilmesi kurumu esnaf yapar ve ticari işletme niteliğini kesin olarak kaldırır",
    ],
    "Kamu tüzel kişilerince özel hukuk hükümlerine göre yönetilmek veya ticari şekilde işletilmek üzere kurulan kurum ve kuruluşlar tacir sayılır.",
    "6102 sayılı TTK m.16/1",
)

q(
    "Tüzel kişilerde tacir sıfatı hakkında aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Ticaret şirketleri tacirdir\n\nII. Devlet, doğrudan ticari işletme işletirse kendisi tacir sayılır\n\nIII. Kamu yararına çalışan dernek, ticari işletme işletse de kendisi tacir sayılmaz",
    "I ve III",
    [
        "I, II ve III; kamu tüzel kişilerinin doğrudan işlettiği ticari işletme onların kendisini de tacir yapar",
        "Yalnız I; kamu yararına çalışan dernek istisnası bulunmadığından işletme işleten her dernek tacirdir",
        "I ve II; kamu yararına çalışan dernek ticari işletme işlettiği anda istisnasız biçimde tacir sayılır",
        "Yalnız III; ticaret şirketleri kuruluş biçimleri nedeniyle tacir olamaz ve yalnız ortakları tacir sayılır",
    ],
    "Ticaret şirketleri tacirdir. Devlet ve diğer kamu tüzel kişileri doğrudan ticari işletme işletseler de kendileri tacir sayılmaz. Kamu yararına çalışan dernek de istisna kapsamındadır.",
    "6102 sayılı TTK m.16",
    "hard",
)


print("TOPLAM:", len(Q))


# ══ BUILD ═════════════════════════════════════════════════════════════════
def gen_letters(n, seed):
    r = random.Random(seed)
    base = ["ABCDE"[i % 5] for i in range(n)]
    while True:
        r.shuffle(base)
        if all(not (base[i] == base[i - 1] == base[i - 2]) for i in range(2, len(base))):
            return base


if __name__ == "__main__":
    assert len(Q) == 60, f"60 olmalı, şu an {len(Q)}"
    letters = gen_letters(len(Q), SEED)
    out = []
    for i, it in enumerate(Q):
        ans = letters[i]
        choices = {ans: it["correct"]}
        for key, distractor in zip(
            [key for key in "ABCDE" if key != ans], it["distractors"]
        ):
            choices[key] = distractor
        assert len(set(choices.values())) == 5, f"{PREFIX}-{i + 1}: şık tekrarı"
        out.append(
            {
                "id": f"{PREFIX}-{i + 1:04d}",
                "lessonId": L,
                "topicId": T,
                "question": it["stem"],
                "choices": choices,
                "correctAnswer": ans,
                "explanation": it["why"],
                "source": {
                    "kind": "generated",
                    "styleRef": "2026/1 test biçimi",
                    "legislationRef": it["ref"],
                },
                "tags": ["Demo Soru", "2026 Formatı", "Konu Havuzu", LBL],
                "difficulty": it["difficulty"],
                "updatedAt": "2026-07-16T00:00:00Z",
                "examPeriod": "2026/1 formatına uyumlu",
                "legislationVersion": "6102 sayılı TTK ve 6098 sayılı TBK - 16.07.2026",
                "sourceUpdatedAt": "2026-07-16T00:00:00Z",
                "isPremium": False,
                "isActive": True,
            }
        )
    with open(OUT, "w", encoding="utf-8") as output_file:
        json.dump(out, output_file, ensure_ascii=False, indent=2)
    marker = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    premise_count = sum(
        1 for item in out if len(marker.findall(item["question"])) >= 2
    )
    print(
        f"yazıldı: {len(out)} soru | öncüllü {premise_count} | "
        f"harf {''.join(item['correctAnswer'] for item in out)[:40]}…"
    )
