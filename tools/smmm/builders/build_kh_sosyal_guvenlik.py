#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM Sosyal Güvenlik — Sigortalılık Statüleri (4/a ve 4/b), 3×20.

Dayanak, 17.07.2026 tarihinde doğrulanan güncel 5510 sayılı Kanunun
4–10 ve 53 üncü maddeleridir. Prim ve sigorta yardımı ayrıntıları,
ayrı ``primler_ve_sigorta_kollari`` konu havuzunun kapsamındadır.
"""
from topic_pack_builder import write_topic


def r(scenario, focus, correct, distractors, why, focus_why, ref, difficulty="medium"):
    return {
        "scenario": scenario, "focus": focus, "correct": correct,
        "distractors": distractors,
        "focus_distractors": distractors[2:] + distractors[:2],
        "why": why, "focus_why": focus_why, "ref": ref,
        "difficulty": difficulty,
    }


RULES = [
    r(
        "Bir kişi, özel bir işletmede işverene bağımlı olarak hizmet akdiyle çalışmaya başlamıştır. Temel sigortalılık statüsü hangisidir?",
        "Bir veya birden fazla işveren tarafından hizmet akdiyle çalıştırılanlar hangi statüde sigortalıdır?",
        "5510 sayılı Kanun m.4/1-a kapsamında sigortalıdır",
        ["Yalnız isteğe bağlı sigortalıdır", "Her durumda 4/b kapsamında sayılır", "Hizmet akdi sosyal sigortalılık doğurmaz ve çalışanın Kuruma bildirimi yapılamaz", "İşveren sayısı birden fazlaysa kişi hiçbir zorunlu sigortalılık statüsüne giremez"],
        "5510 sayılı Kanun m.4/1-a, bir veya birden fazla işveren tarafından hizmet akdiyle çalıştırılanları 4/a kapsamında sigortalı sayar.",
        "İşveren sayısının bir ya da birden çok olması statüyü değiştirmez; belirleyici bağ hizmet akdidir.",
        "5510 sayılı Kanun m.4/1-a", "easy",
    ),
    r(
        "Bir işçi sendikasının yönetim kuruluna seçilen kişi, seçilmiş görevi nedeniyle sosyal sigorta kapsamının dışında olduğunu düşünmektedir. Hangisi doğrudur?",
        "İşçi sendikası, konfederasyon veya sendika şubesinin başkanlığına ya da yönetim kuruluna seçilenlere hangi statü hükümleri uygulanır?",
        "4/a sigortalılarına ilişkin hükümler uygulanır",
        ["Hiçbir sigorta hükmü uygulanmaz", "Yalnız 4/b statüsü uygulanır", "Seçilmek bütün sosyal güvenlik haklarını sona erdirir", "Görev süresince yalnız genel sağlık sigortası dışında kalan özel bir statü uygulanır"],
        "5510 m.4'ün ikinci fıkrası, işçi sendikaları ve konfederasyonları ile şubelerinin başkan ve yönetim kurulu üyelerine 4/a hükümlerini uygular.",
        "Görevin seçimle kazanılması, Kanunun açık yollaması nedeniyle 4/a korumasını ortadan kaldırmaz.",
        "5510 sayılı Kanun m.4/2-a", "medium",
    ),
    r(
        "Kendi adına serbest meslek faaliyeti yürüten kişi bu kazanç nedeniyle gerçek usulde gelir vergisi mükellefidir ve hizmet akdiyle çalışmamaktadır. Statüsü nedir?",
        "Ticari veya serbest meslek kazancı nedeniyle gerçek ya da basit usulde gelir vergisi mükellefi olan bağımsız çalışan hangi statüdedir?",
        "4/b kapsamında bağımsız çalışan sigortalıdır",
        ["Gelir vergisi mükellefiyeti sigortalılığı engeller", "Yalnız 4/c kapsamında sayılır", "Vergi mükellefi olan bağımsız çalışan zorunlu sigortalı değildir", "Bağımsız faaliyeti işverenin işyerindeki ücretsiz eş statüsüne dönüştürülür"],
        "5510 m.4/1-b-1, hizmet akdine bağlı olmaksızın kendi adına çalışan gelir vergisi mükelleflerini 4/b kapsamında sigortalı sayar.",
        "Ticari veya serbest meslek kazancından doğan gerçek ya da basit usulde mükellefiyet, bu bentteki temel tescil bağlantısıdır.",
        "5510 sayılı Kanun m.4/1-b-1", "easy",
    ),
    r(
        "Kendi adına çalışan kişi gelir vergisinden muaftır; buna karşılık esnaf ve sanatkâr siciline kayıtlıdır ve m.6'daki düşük gelir istisnasını belgelememiştir. Statüsü nedir?",
        "Gelir vergisinden muaf bağımsız çalışanın 4/b kapsamında sayılmasında hangi kayıt önem taşır?",
        "Esnaf ve sanatkâr sicili kaydı 4/b sigortalılığına dayanak olur",
        ["Vergi muafiyeti her durumda sigortasızlık yaratır", "Yalnız ticaret sicili kaydı 4/a doğurur", "Esnaf siciline kayıt sosyal güvenlik bakımından hiçbir sonuç doğurmaz", "Vergiden muaf bağımsız çalışan yalnız işverenin isteğiyle kamu görevlisi statüsüne alınabilir"],
        "5510 m.4/1-b-2, gelir vergisinden muaf olup esnaf ve sanatkâr siciline kayıtlı bağımsız çalışanı, m.6/k istisnası yoksa 4/b kapsamına alır.",
        "Vergi muafiyeti tek başına kapsam dışılık sağlamaz; sicil kaydı ve kanuni gelir istisnası birlikte değerlendirilir.",
        "5510 sayılı Kanun m.4/1-b-2 ve m.6/k", "medium",
    ),
    r(
        "Bir anonim şirket ortağı yönetim kurulu üyesi değildir. Sadece ortaklık sıfatının 4/b sigortalılığı için yeterli olduğu ileri sürülmektedir. Hangisi doğrudur?",
        "Anonim şirket ortaklarının 4/b kapsamında sayılması için hangi ek sıfat aranır?",
        "Ortağın aynı zamanda yönetim kurulu üyesi olması gerekir",
        ["Bütün pay sahipleri kendiliğinden 4/b'lidir", "Yönetim kurulu üyeliği hiçbir zaman önem taşımaz", "Yalnız şirket alacaklıları ve düzenli müşterileri 4/b kapsamında sayılır", "Anonim şirket ortağı olmak kişiyi ortaklık oranına bakılmaksızın doğrudan 4/c kamu görevlisine dönüştürür"],
        "5510 m.4/1-b-3, anonim şirketlerde yalnız yönetim kurulu üyesi olan ortakları 4/b kapsamında sayar.",
        "Sırf pay sahipliği yeterli değildir; ortaklık ile yönetim kurulu üyeliğinin birlikte bulunması gerekir.",
        "5510 sayılı Kanun m.4/1-b-3", "medium",
    ),
    r(
        "Limited şirket ortağı, yönetim kurulu üyesi olmadığı gerekçesiyle 4/b kapsamında bulunmadığını savunmaktadır. Değerlendirme nedir?",
        "Limited şirket ortaklarının 4/b sigortalılığında anonim şirketteki yönetim kurulu üyeliği koşulu aranır mı?",
        "Limited şirket ortaklığı 4/b kapsamı için yeterlidir; bu koşul aranmaz",
        ["Limited şirket ortakları pay oranları ne olursa olsun hiçbir zaman zorunlu sigortalı değildir", "Yalnız yüzde yüz pay sahibi 4/a'lıdır", "Her limited ortak doğrudan 4/c kapsamında sayılır", "Limited şirket ortağının sigortalılığı yalnız şirketin müşterilerinin ortak kararıyla başlayabilir"],
        "5510 m.4/1-b-3, diğer şirketlerin ortaklarını 4/b kapsamında sayar; anonim şirkete özgü yönetim kurulu üyeliği sınırlaması limited ortağa uygulanmaz.",
        "Limited şirket ortaklığının ticaret sicilinde tescili, m.7 uyarınca sigortalılık başlangıcında da esas alınır.",
        "5510 sayılı Kanun m.4/1-b-3 ve m.7", "medium",
    ),
    r(
        "Hizmet akdi bulunmayan kişi kendi adına tarımsal faaliyette bulunmaktadır ve m.6/ı'daki muafiyeti belgelememiştir. Temel statüsü nedir?",
        "Kendi adına ve hesabına tarımsal faaliyette bulunanlar kural olarak hangi statüde sigortalıdır?",
        "4/b kapsamında sigortalıdır",
        ["Tarımsal faaliyet sigorta kapsamı dışındadır", "Yalnız 4/a statüsü uygulanır", "Her çiftçi kamu görevlisi sayılır", "Tarımsal çalışan ancak yanında yüz işçi varsa 4/b kapsamında olabilir"],
        "5510 m.4/1-b-4, kendi adına ve hesabına tarımsal faaliyette bulunanları, m.6/ı koşullarıyla kapsam dışında kalmadıkça 4/b sigortalısı sayar.",
        "Faaliyetin bağımsız niteliği 4/b bağlantısını kurar; düşük gelir ve yaşa bağlı istisnalar ayrıca incelenir.",
        "5510 sayılı Kanun m.4/1-b-4 ve m.6/ı", "easy",
    ),
    r(
        "Köy muhtarı, yanında işçi çalıştırmadığı için sigortalı sayılamayacağını düşünmektedir. 5510 bakımından temel sonuç nedir?",
        "Köy ve mahalle muhtarları hangi temel sigortalılık statüsünde yer alır?",
        "4/b kapsamında sigortalı sayılır",
        ["Muhtarlar yalnız 4/a kapsamında sayılır", "Muhtarlık hiçbir sigortalılık doğurmaz", "Muhtarlar sadece isteğe bağlı sigortalıdır", "Muhtar ancak anonim şirket ortağı olursa 4/c kapsamında sayılır"],
        "5510 m.4/1-b, köy ve mahalle muhtarlarını açıkça 4/b kapsamına alır.",
        "Muhtarın ayrıca işveren olması aranmaz; m.7 uyarınca sigortalılık seçildiği tarihten başlar.",
        "5510 sayılı Kanun m.4/1-b ve m.7", "easy",
    ),
    r(
        "İşverenin eşi, eşine ait işyerinde herhangi bir ücret almadan çalışmaktadır. Kısa ve uzun vadeli sigorta kolları bakımından sonucu nedir?",
        "İşverenin işyerinde ücretsiz çalışan eşi 5510 m.6 uyarınca sigortalı sayılır mı?",
        "Ücretsiz çalışan eş 4 ve 5 inci maddeler kapsamında sigortalı sayılmaz",
        ["Her durumda 4/a sigortalısıdır", "Ücretsiz eş yalnız 4/c kapsamında sayılır", "Evlilik bağı ücretsiz çalışmayı otomatik olarak iki ayrı 4/a sigortalılığına dönüştürür", "Ücretsiz eş bağımsız ticari kazanç sahibi sayılarak zorunlu 4/b'li olur"],
        "5510 m.6/a, işverenin işyerinde ücretsiz çalışan eşini kısa ve uzun vadeli sigorta kolları bakımından sigortalı sayılmayanlar arasında düzenler.",
        "İstisnanın anahtar unsuru ücretsiz çalışmadır; ücretli hizmet ilişkisi ayrıca 4/a yönünden değerlendirilir.",
        "5510 sayılı Kanun m.6/a", "medium",
    ),
    r(
        "Aynı konutta yaşayan ikinci derece hısımlar, dışarıdan kimse katılmadan ev içinde el işi üretmektedir. Aralarındaki bu çalışma bakımından hangisi doğrudur?",
        "Aynı konutta yaşayan üçüncü dereceye kadar hısımların dışarıdan kimse katılmaksızın konut içinde yaptıkları işte statü nedir?",
        "Bu koşullardaki kişiler 4 ve 5 inci maddelere göre sigortalı sayılmaz",
        ["Konut içindeki herkes 4/c'lidir", "Hısımlık sigortalılığı zorunlu olarak 4/b yapar", "Dışarıdan kimse katılmasa da aynı konuttaki bütün hısımlar zorunlu 4/a sayılır", "Ev içi çalışma gündüz yapılırsa bütün hısımlar 4/c kapsamında sayılır"],
        "5510 m.6/b; aynı konutta yaşayan, üçüncü derece dâhil hısımlar arasında, dışarıdan kimse katılmadan konut içinde yapılan çalışmayı kapsam dışında bırakır.",
        "Konut, hısımlık derecesi ve dışarıdan çalışan bulunmaması koşulları birlikte aranır.",
        "5510 sayılı Kanun m.6/b", "hard",
    ),
    r(
        "Bir kişi aynı ev işvereninin yanında ay içinde on iki gün ücretle ev hizmeti görmektedir. 5510 bakımından hangisi doğrudur?",
        "Ev hizmetinde aynı kişi yanında ayda on gün veya daha fazla ücretle çalışan hangi temel statüye tabidir?",
        "4/a kapsamında sigortalı sayılır",
        ["Ev hizmeti hiçbir zaman sigortalılık doğurmaz", "Yalnız 4/b statüsü uygulanır", "On gün ve üzeri çalışma ücretsiz aile yardımı sayılır", "Ev hizmetinde çalışan gün sayısına bakılmadan yalnız özel sigortaya tabidir"],
        "5510 m.6/c ve ek m.9, aynı kişi yanında ayda on gün veya daha fazla ücretle ev hizmetinde çalışanı 4/a kapsamında sigortalı sayar.",
        "On günden az çalışma ek m.9'un ayrı kısa vadeli koruma rejimine tabidir; iki durum birbirine karıştırılmaz.",
        "5510 sayılı Kanun m.6/c ve ek m.9", "medium",
    ),
    r(
        "Kişi askerlik hizmetini er olarak yapmaktadır. Bu dönem için m.4 ve m.5 kapsamında zorunlu sigortalı sayılmayı istemektedir. Sonuç nedir?",
        "Askerlik hizmetini er veya erbaş olarak yapanlar ile yedek subay ve yedek astsubay okulu öğrencileri zorunlu sigortalı sayılır mı?",
        "Bu dönemlerde 4 ve 5 inci maddelere göre sigortalı sayılmazlar",
        ["Tamamı 4/a sigortalısıdır", "Yalnız 4/b statüsü uygulanır", "Askerlik hizmeti doğrudan şirket ortaklığı ve zorunlu 4/b faaliyeti sayılır", "Er ve erbaşların her biri hizmet süresince özel bir işverenin yönetim kurulu üyesi kabul edilir"],
        "5510 m.6/d, er ve erbaş olarak askerlik yapanlarla yedek subay ve yedek astsubay okulu öğrencilerini zorunlu sigortalı sayılmayanlar arasında düzenler.",
        "Bu dönemlerin sonradan borçlanılabilmesi, dönem içinde zorunlu sigortalı sayılma sonucuyla aynı değildir.",
        "5510 sayılı Kanun m.6/d", "easy",
    ),
    r(
        "Yabancı bir kuruluş, kendi adına çalışan ve yabancı ülkede sosyal sigortalı olduğunu belgeleyen personelini iki aylık iş için Türkiye'ye göndermiştir. Sözleşme hükmü saklıdır. Sonuç nedir?",
        "Yabancı kuruluşça Türkiye'ye üç ayı geçmeyen iş için gönderilen ve yabancı sigortalılığını belgeleyen kişi zorunlu sigortalı sayılır mı?",
        "Uluslararası sözleşmeler saklı kalmak üzere 4 ve 5 inci maddelere göre sigortalı sayılmaz",
        ["Her durumda 4/c kapsamındadır", "Üç aylık süre koşulu bulunmaz ve daima 4/a'lıdır", "Yabancı sigortalılık belgesi hiçbir değer taşımaz", "Türkiye'de bir gün bulunması kişinin yabancı ülkedeki bütün sigorta kayıtlarını silerek zorunlu 4/b doğurur"],
        "5510 m.6/e, yabancı kuruluş adına üç ayı geçmemek üzere gönderilen ve yabancı ülkede sosyal sigortaya tabi olduğunu belgeleyen kişiyi, sözleşmeler saklı kalmak üzere kapsam dışında bırakır.",
        "Gönderen kuruluş, süre ve yabancı sigortalılığı belgesi birlikte aranır.",
        "5510 sayılı Kanun m.6/e", "hard",
    ),
    r(
        "On yedi yaşındaki kişi kendi adına ticari faaliyeti nedeniyle normalde 4/b kapsamında olacaktır; meslek okulu ve mahkemece ergin kılınma istisnası yoktur. Sonuç nedir?",
        "4/b veya 4/c kapsamında olması gereken on sekiz yaşını doldurmamış kişiler için genel kural nedir?",
        "On sekiz yaş dolmadıkça 4 ve 5 inci maddelere göre sigortalı sayılmaz",
        ["Doğrudan 4/c kapsamında sayılır", "Yaşın 4/b ve 4/c sigortalılığına hiçbir etkisi yoktur ve yeni doğan kişi dahi tescil edilir", "On yaşını doldurmak 4/b için yeterlidir", "On sekiz yaşından küçük her kişi çalışmasa bile hizmet akdiyle çalışan 4/a sigortalısı kabul edilir"],
        "5510 m.6/h, 4/b ve 4/c kapsamında olması gerekenlerden on sekiz yaşını doldurmayanları genel olarak kapsam dışında bırakır.",
        "Meslek veya sanat okulunu bitirip mahkemece ergin kılınan ve öğrenimiyle ilgili işte çalışanlar için Kanunda özel istisna vardır.",
        "5510 sayılı Kanun m.6/h", "medium",
    ),
    r(
        "Ceza infaz kurumu atölyesinde hizmet akdi olmaksızın çalıştırılan hükümlü bakımından hangi sigorta kolları uygulanır?",
        "Ceza infaz kurumu veya tutukevi atölyesinde çalıştırılan hükümlü ve tutuklunun kısmi sigortalılığı hangi kolları kapsar?",
        "İş kazası ve meslek hastalığı ile analık sigortası uygulanır; 4/a kapsamında sayılır",
        ["Hiçbir sigorta kolu uygulanmaz", "Yalnız yaşlılık ve ölüm sigortası uygulanır", "Bütün uzun vadeli kollar zorunlu uygulanır", "Hükümlü yalnız genel sağlık sigortası kapsamında 4/c kamu görevlisi olarak tescil edilir"],
        "5510 m.5/a, bu tesislerde çalıştırılan hükümlü ve tutuklulara iş kazası ve meslek hastalığı ile analık sigortası uygular ve onları 4/a kapsamında sayar.",
        "Bu kısmi sigortalılık, bütün kısa ve uzun vadeli sigorta kollarının uygulanması anlamına gelmez.",
        "5510 sayılı Kanun m.5/a", "hard",
    ),
    r(
        "Aday çırak ile zorunlu staj yapan yükseköğrenim öğrencisinin tabi olduğu sigorta kollarının aynı olduğu ileri sürülmektedir. Hangisi doğrudur?",
        "Aday çırak ve çıraklarla zorunlu stajyerlerin kısmi sigorta kapsamı nasıl farklılaşır?",
        "Çırağa iş kazası-meslek hastalığı ile hastalık; stajyere ilk iki sigorta uygulanır",
        ["Her ikisine yalnız yaşlılık sigortası uygulanır", "Stajyerler hiçbir sigorta koluna tabi değildir", "Çıraklara sadece ölüm sigortası uygulanır", "Çırak ve stajyerlerin tümü eğitim koşulu aranmadan uzun vadeli kollara tabidir"],
        "5510 m.5/b; aday çırak ve çıraklara iş kazası-meslek hastalığı ile hastalık, sayılan stajyer ve öğrencilere iş kazası-meslek hastalığı sigortası uygular.",
        "Bu kişiler 4/a kapsamında sayılır; bakmakla yükümlü kişi olmayanlara ayrıca genel sağlık sigortası hükümleri uygulanır.",
        "5510 sayılı Kanun m.5/b", "hard",
    ),
    r(
        "Türkiye İş Kurumunun meslek edindirme kursuna katılan kişi bakımından hangi sosyal sigorta hükümleri uygulanır?",
        "İŞKUR meslek edindirme, geliştirme ve değiştirme eğitimine katılan kursiyerin statüsü ve koruması nedir?",
        "4/a kapsamında sayılır; iş kazası-meslek hastalığı ve genel sağlık sigortası uygulanır",
        ["Kursiyer hiçbir sigorta kapsamına girmez", "Yalnız malullük ve yaşlılık sigortası uygulanır", "Kursiyer doğrudan 4/b şirket ortağı sayılır", "Bütün primleri kursiyerin müşterileri öder ve Türkiye İş Kurumunun hiçbir yükümlülüğü bulunmaz"],
        "5510 m.5/e, İŞKUR kursiyerini 4/a kapsamında sayar; iş kazası-meslek hastalığı ve genel sağlık sigortası hükümlerini uygular.",
        "Türkiye İş Kurumu prim ödeme yükümlüsüdür; bu nedenle Kanun kapsamında işyeri veya işveren sayılmaz.",
        "5510 sayılı Kanun m.5/e", "medium",
    ),
    r(
        "4/a kapsamındaki işçi pazartesi fiilen çalışmaya başlamış, işe giriş bildirgesi daha sonra verilmiştir. Sigorta hak ve yükümlülükleri ne zaman başlar?",
        "4/a sigortalılığının başlangıcı bildirim tarihine mi, fiilen çalışmaya başlama tarihine mi bağlanmıştır?",
        "Fiilen çalışmaya başladığı tarihten başlar",
        ["İşverenin istediği tarihten başlar", "İlk ücret zammından sonra başlar", "Bildirge verilmezse hiçbir zaman başlamaz", "Çalışmaya başlanmasından beş yıl sonra kendiliğinden geriye yürümeksizin başlar"],
        "5510 m.7/a, 4/a sigorta hak ve yükümlülüklerini çalışmaya, eğitime, staja veya bursiyer göreve başlanılan tarihten başlatır.",
        "Bildirim yükümlülüğü başlangıcı yaratmaz; mevcut başlangıcın Kuruma zamanında bildirilmesini sağlar.",
        "5510 sayılı Kanun m.7/a", "easy",
    ),
    r(
        "Limited şirket ortağının ortaklığı ticaret sicilinde tescil edilmiştir. 4/b sigortalılığı hangi tarihte başlar?",
        "Limited şirket ortağı ile yönetim kurulu üyesi anonim şirket ortağının 4/b başlangıç bağlantıları nelerdir?",
        "Limited ortakta tescil; anonim ortakta yönetim kuruluna seçilme tarihi esas alınır",
        ["Her ikisinde ilk kâr dağıtımı beklenir", "Yalnız şirketin tasfiye tarihi esas alınır", "Ortaklık tescili hiçbir sigortalılık doğurmaz", "Limited ortakta kapanış, anonim ortakta pay devri başlangıç sayılır"],
        "5510 m.7/b, limited ortak için ticaret sicili tescilini; yönetim kurulu üyesi anonim şirket ortağı için yönetim kuruluna seçilmeyi başlangıç sayar.",
        "Şirket türüne ve ortaklık sıfatına göre başlangıç olayı farklılaştırılmıştır.",
        "5510 sayılı Kanun m.7/b", "hard",
    ),
    r(
        "Kendi adına tarımsal faaliyeti meslek kuruluşuna kaydedilen kişi, faaliyeti bir yıl içinde Kuruma bildirmiştir. 4/b başlangıcı nasıl belirlenir?",
        "Tarımsal faaliyetin bir yıl içinde veya bu süre geçtikten sonra bildirilmesi 4/b başlangıcını nasıl etkiler?",
        "Bir yıl içinde bildirilirse kayıt; geç bildirilirse Kuruma bildirim tarihi esas alınır",
        ["Her durumda doğum tarihi esas alınır", "Tarımsal faaliyette 4/b hiç başlamaz", "Geç bildirim başlangıcı on yıl geriye götürür", "Meslek kuruluşu kaydı yalnız 4/c kamu görevliliği doğurur ve bildirim zamanının hiçbir etkisi olmaz"],
        "5510 m.7/b, tarımsal faaliyetin bir yıl içinde bildirilmesinde kayıt tarihini; süre geçerse Kuruma bildirim tarihini başlangıç kabul eder.",
        "Bir yıllık bildirim süresi, tarımsal 4/b tescilinin geriye yürüyüp yürümeyeceğini belirler.",
        "5510 sayılı Kanun m.7/b", "hard",
    ),
    r(
        "Genel bir özel sektör işyerinde 4/a sigortalısı işe alınacaktır. Özel istisnalardan hiçbiri yoktur. İşe giriş bildirgesi ne zaman verilmelidir?",
        "4/a sigortalısı için genel işe giriş bildirimi süresi nedir?",
        "Fiilen çalışmaya başlamadan önce Kuruma verilmelidir",
        ["İşten ayrıldıktan sonra verilir", "Beşinci çalışma yılının sonunda verilir", "Yalnız işçinin noter aracılığıyla yazılı izin vermesi hâlinde bildirge düzenlenir", "İşveren bildirgeyi sigortalı emekli olduktan sonra verebilir"],
        "5510 m.8, işvereni 4/a sigortalısının işe giriş bildirgesini kural olarak sigortalılık başlangıcından önce vermekle yükümlü tutar.",
        "İnşaat, balıkçılık ve tarım gibi işyerleri için Kanunda özel zamanlama istisnaları vardır.",
        "5510 sayılı Kanun m.8", "easy",
    ),
    r(
        "İnşaat işyerinde işçi bugün çalışmaya başlatılmıştır. İşveren bildirgeyi bugün Kuruma vermiştir. Zamanında bildirim yapılmış sayılır mı?",
        "İnşaat, balıkçılık ve tarım işyerlerinde işe giriş bildirgesi en geç ne zaman verilebilir?",
        "Çalışmaya başlatıldığı gün verilmesi zamanında bildirim sayılır",
        ["Mutlaka bir yıl önce verilmelidir", "Çalışılan ayı izleyen beşinci yıl verilir", "Bu işyerlerinde bildirim tamamen isteğe bağlıdır", "Aynı gün bildirim yalnız işçi o gün hiç çalışmamış ve iş sözleşmesi sona ermişse geçerli olabilir"],
        "5510 m.8/a, inşaat, balıkçılık ve tarım işyerlerinde bildirgenin en geç çalışmaya başlatıldığı gün verilmesine izin verir.",
        "Bu hüküm, genel çalışmadan önce bildirim kuralının sektörlere özgü istisnasıdır.",
        "5510 sayılı Kanun m.8/a", "medium",
    ),
    r(
        "İlk defa işyeri bildirgesi verilecek işyerinde, ilk sigortalı çalıştırılmaya başlandıktan yirmi gün sonra yeni işçi işe alınmıştır. İşe giriş bildiriminin son günü nasıl belirlenir?",
        "Kuruma ilk defa işyeri bildirgesi verilen işyerinde ilk bir ay içinde işe alınanların bildirimi için özel süre nedir?",
        "İlk sigortalıdan itibaren bir aylık sürenin sonuna kadar verilebilir",
        ["İşe alınan herkes beş yıl sonra bildirilir", "Yeni işyeri için hiçbir bildirim yapılmaz", "Süre işyerinin tasfiye edildiği gün başlar", "İlk ayda işe alınanlar yalnız ortaksa on yıl içinde bildirilir"],
        "5510 m.8/b, ilk defa işyeri bildirgesi verilecek işyerinde ilk bir ay içinde işe başlayanların bildirgesini bu bir aylık sürenin sonuna kadar zamanında sayar.",
        "Özel süre, işyerinde ilk sigortalı çalıştırılmaya başlanan tarihten hesaplanır.",
        "5510 sayılı Kanun m.8/b", "hard",
    ),
    r(
        "4/a sigortalısı işe başladığını bir ay içinde Kuruma bildirmemiştir. İşverenin fiilî çalışmayı gösteren kayıtları vardır. Bildirmeme nasıl değerlendirilir?",
        "Sigortalının işe başladığını bir ay içinde kendisinin bildirmemesi aleyhine delil oluşturur mu?",
        "Kişisel bildirim yapılmaması sigortalı aleyhine delil oluşturmaz",
        ["Sigortalılık kendiliğinden tamamen silinir", "İşverenin yükümlülüğü işçiye geçer", "Bildirmeyen işçi bütün geçmiş ücretlerini kaybeder", "Bir aylık kişisel bildirim yapılmazsa fiilî çalışma kesin olarak yok sayılır ve aksinin kanıtlanması yasaktır"],
        "5510 m.8, sigortalıya işe başladığını bir ay içinde bildirme ödevi verir; ancak bu bildirimin yapılmamasını sigortalı aleyhine delil saymaz.",
        "İşverenin işe giriş bildirimi yükümlülüğü ayrıca devam eder ve işçinin ödeviyle ortadan kalkmaz.",
        "5510 sayılı Kanun m.8", "medium",
    ),
    r(
        "4/a sigortalısının hizmet akdi cuma günü sona ermiştir. İşveren ayrılışı Kuruma yirmi gün sonra bildirmiştir. Hangisi doğrudur?",
        "4/a sigortalılığının sona erme tarihi ve Kuruma bildirim süresi nedir?",
        "Hizmet akdinin sona erdiği tarihte biter ve durum en geç on gün içinde bildirilir",
        ["Emeklilik yaşında biter ve bildirim gerekmez", "İşveren istediği tarihte sona erdirir", "Bildirim yapılana kadar hizmet akdi fiilen devam eder", "Ayrılış bildirimi yalnız sigortalının mirasçılarınca yapılır"],
        "5510 m.9/a, 4/a sigortalılığını hizmet akdinin sona erdiği tarihte bitirir; sona erme durumu işverence en geç on gün içinde Kuruma bildirilir.",
        "Geç bildirim, hizmet akdinin sona erdiği maddi tarihi kendiliğinden ileri taşımaz.",
        "5510 sayılı Kanun m.9", "medium",
    ),
    r(
        "Bir kişi aynı anda hem kamu görevlisi 4/c hem hizmet akdiyle 4/a kapsamına girecek şekilde çalışmaktadır. Hangi statü önceliklidir?",
        "4/a ile 4/b aynı anda; bunlardan biriyle 4/c aynı anda doğduğunda m.53 hangi öncelik sırasını uygular?",
        "4/c diğerlerine; 4/a ise 4/b'ye göre önceliklidir",
        ["Her durumda yalnız 4/b uygulanır", "Statüler arasında hiçbir öncelik yoktur", "İlk prim ödenen statü daima değişmeden sürer", "Çakışan statüler aynı gün için ayrı ayrı tam hizmet kazandırır"],
        "5510 m.53, 4/c ile çakışmada 4/c'yi; 4/a ile 4/b çakışmasında 4/a'yı esas alır.",
        "Ayrıca 4/b kapsamındakiler kendilerine ait veya ortak oldukları işyerinden dolayı 4/a kapsamında bildirilemez.",
        "5510 sayılı Kanun m.53", "hard",
    ),
]


PREMISES = [
    {
        "stem": "Sigortalılık statüleriyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Hizmet akdiyle çalışanlar kural olarak 4/a kapsamındadır.\n\nII. Kendi adına ticari kazanç nedeniyle gelir vergisi mükellefi olan bağımsız çalışan 4/b kapsamında olabilir.\n\nIII. Köy ve mahalle muhtarları 4/b kapsamında sayılır.",
        "correct": "I, II ve III", "why": "5510 m.4 uyarınca üç ifade de ilgili temel statü bağlantılarını doğru gösterir.",
        "ref": "5510 sayılı Kanun m.4", "difficulty": "easy",
    },
    {
        "stem": "Şirket ortaklarının 4/b statüsüyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Limited şirket ortakları 4/b kapsamında olabilir.\n\nII. Anonim şirkette ortaklık yanında yönetim kurulu üyeliği aranır.\n\nIII. Sermayesi paylara bölünmüş komandit şirkette komandite ortak 4/b kapsamında olabilir.",
        "correct": "I, II ve III", "why": "5510 m.4/1-b-3 şirket türleri ve ortak sıfatları bakımından üç ifadeyi de kapsar.",
        "ref": "5510 sayılı Kanun m.4/1-b-3", "difficulty": "medium",
    },
    {
        "stem": "Sigortalı sayılmayanlarla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İşverenin işyerinde ücretsiz çalışan eşi kapsam dışındadır.\n\nII. Er olarak askerlik yapan kişi bu dönem için m.4 ve m.5'e göre sigortalı sayılmaz.\n\nIII. Ücretle aynı kişi yanında ayda on gün ev hizmetinde çalışan kişi kapsam dışındadır.",
        "correct": "I ve II", "why": "5510 m.6 nedeniyle I ve II uygulanır. Aynı kişi yanında ayda on gün veya daha fazla ücretle ev hizmeti gören m.6/c istisnası gereği kapsam dışı değildir.",
        "ref": "5510 sayılı Kanun m.6", "difficulty": "medium",
    },
    {
        "stem": "Kısmi sigortalılıkla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Hükümlü ve tutukluya bütün uzun vadeli sigorta kolları uygulanır.\n\nII. Aday çırak ve çırağa iş kazası-meslek hastalığı ile hastalık sigortası uygulanır.\n\nIII. Zorunlu stajyere iş kazası ve meslek hastalığı sigortası uygulanır.",
        "correct": "II ve III", "why": "5510 m.5/b nedeniyle II ve III uygulanır. Hükümlü ve tutuklu m.5/a'daki sınırlı kollara tabidir; bütün uzun vadeli kollar uygulanmaz.",
        "ref": "5510 sayılı Kanun m.5/a-b", "difficulty": "hard",
    },
    {
        "stem": "Sigortalılığın başlangıcıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. 4/a sigortalılığı fiilen çalışmaya başlanan tarihte başlar.\n\nII. Limited şirket ortağında ticaret sicili tescili başlangıç bağlantısıdır.\n\nIII. Muhtarın sigortalılığı görevi sona erdiği tarihte başlar.",
        "correct": "I ve II", "why": "5510 m.7 uyarınca I ve II uygulanır. Muhtarın başlangıcı seçildiği tarihtir; görevin sona ermesi m.9 kapsamında bitiş nedenidir.",
        "ref": "5510 sayılı Kanun m.7", "difficulty": "medium",
    },
    {
        "stem": "İşe giriş bildirimiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Genel kural, 4/a bildirgesinin çalışmaya başlamadan önce verilmesidir.\n\nII. İnşaat işyerinde bildirge mutlaka bir ay önce verilmelidir.\n\nIII. Sigortalının kendisini bir ay içinde bildirmemesi aleyhine delil oluşturmaz.",
        "correct": "I ve III", "why": "5510 m.8 uyarınca I ve III uygulanır. İnşaat işyerinde bildirge en geç çalışmaya başlatıldığı gün verilebilir.",
        "ref": "5510 sayılı Kanun m.8", "difficulty": "medium",
    },
    {
        "stem": "Sigortalılığın sona ermesiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. 4/a sigortalılığı hizmet akdinin sona erdiği tarihte biter.\n\nII. Sona erme durumu kural olarak en geç on gün içinde bildirilir.\n\nIII. Bildirimin gecikmesi hizmet akdini kendiliğinden devam ettirir.",
        "correct": "I ve II", "why": "5510 m.9 uyarınca I ve II uygulanır. Bildirim gecikmesi fiilî sona erme tarihini kendiliğinden değiştirmez.",
        "ref": "5510 sayılı Kanun m.9", "difficulty": "medium",
    },
    {
        "stem": "Sigortalılık statülerinin çakışmasıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. 4/c ile çakışmada kural olarak 4/c önceliklidir.\n\nII. 4/a ile 4/b çakışmasında kural olarak 4/a önceliklidir.\n\nIII. 4/b kapsamındaki kişi kendi ortak olduğu işyerinden 4/a bildirilebilir.",
        "correct": "I ve II", "why": "5510 m.53 nedeniyle I ve II uygulanır. 4/b kapsamındakiler kendilerine ait veya ortak oldukları işyerinden 4/a bildirilemez.",
        "ref": "5510 sayılı Kanun m.53", "difficulty": "hard",
    },
]


WRONG_BANKS = {"unused": ["a", "b", "c", "d", "e", "f"]}


if __name__ == "__main__":
    write_topic(
        lesson_id="sosyal_guvenlik_mevzuati", topic_id="sosyal_guvenlik",
        label="Sigortalılık Statüleri (4/a ve 4/b)", slug="sosyal_guvenlik",
        prefix="kh-sg-status", seed=20260801,
        legislation_version="5510 sayılı Kanun m.4–10 ve 53 — 17.07.2026 güncel metin",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG_BANKS,
    )
