# -*- coding: utf-8 -*-
"""Yeterlilik — Sermaye Piyasası Mevzuatı Test 2 + Test 3 (2×19 = 38 soru).
6362 sayılı SPKn. Şıklar aynı kavramsal düzeyde ve doğal uzunlukta tutulur.
Yıla bağlı tutar/oran YOK (idari para cezaları her yıl değişir — sorulmadı).
explanation'da harf atıfı YOK."""
import json, random, re
from pathlib import Path

L = "sermaye_piyasasi_ve_finans"
Q = []
def q(topic, label, stem, correct, distractors, why, ref, difficulty="medium"):
    assert len(distractors) == 4, stem[:44]
    Q.append(dict(topic=topic, label=label, stem=stem, correct=correct,
                  distractors=distractors, why=why, ref=ref, difficulty=difficulty))

# ══ SPK VE DÜZENLEME (6) ══════════════════════════════════════════════════
q("spk_ve_duzenleme", "SPK ve Düzenleme",
  "6362 sayılı Sermaye Piyasası Kanunu'nun amacı bakımından aşağıdakilerden hangisi doğrudur?",
  "Sermaye piyasasının güvenilir, şeffaf, etkin, istikrarlı ve rekabetçi biçimde işleyişini sağlamak ve yatırımcıların hak ve menfaatlerini korumaktır",
  ["Yalnızca ihraççı şirketlerin kâr payı dağıtımını düzenlemeyi, şirketlerin finansman maliyetini azaltmayı ve ortaklara azami getiri sağlanmasını güvence altına almayı amaçlar",
   "Sermaye piyasasında işlem yapan yatırımcıların kâr etmesini devlet güvencesi altına almayı hedeflemektedir",
   "Bankacılık sisteminin denetimini düzenlemek ve mevduat toplama faaliyetini kurala bağlamak amacını taşır",
   "Yalnızca kamu iktisadi teşebbüslerinin özelleştirilmesine ilişkin usulleri belirlemek üzere düzenlenmiştir"],
  "6362 sayılı SPKn m.1: Kanunun amacı, sermaye piyasasının güvenilir, şeffaf, etkin, istikrarlı, adil ve rekabetçi biçimde işleyişini sağlamak ve yatırımcıların hak ve menfaatlerini korumaktır.",
  "6362 sayılı SPKn m.1", "easy")

q("spk_ve_duzenleme", "SPK ve Düzenleme",
  "Sermaye Piyasası Kurulunun hukuki konumu bakımından aşağıdakilerden hangisi doğrudur?",
  "Kurul, idari ve mali özerkliğe sahip, kamu tüzel kişiliğini haiz bir düzenleyici ve denetleyici kurumdur",
  ["Kurul, sermaye piyasasında işlem yapan aracı kurumların ortaklığıyla kurulmuş özel hukuk tüzel kişisidir",
   "Kurul, bir bakanlığın hiyerarşik denetimi altında bulunan ve özerkliği olmayan bir genel müdürlüktür",
   "Kurul, yalnızca borsada işlem gören şirketlerin oy çokluğuyla seçtiği bir meslek örgütü niteliğindedir",
   "Kurul, yargı yetkisini haiz olup sermaye piyasası uyuşmazlıklarında mahkeme sıfatıyla karar verebilir"],
  "6362 sayılı SPKn m.117: Sermaye Piyasası Kurulu, idari ve mali özerkliğe sahip, kamu tüzel kişiliğini haiz düzenleyici ve denetleyici bir kamu kurumudur.",
  "6362 sayılı SPKn m.117")

q("spk_ve_duzenleme", "SPK ve Düzenleme",
  "Kurulun düzenleme yetkisi bakımından aşağıdakilerden hangisi doğrudur?",
  "Kurul, Kanunun uygulanmasına ilişkin olarak tebliğ ve kararlarla ikincil düzenleme yapma yetkisine sahiptir",
  ["Kurulun hiçbir düzenleme yetkisi bulunmayıp yalnızca kanun metnini olduğu gibi uygulamakla görevlidir",
   "Kurul, Kanuna aykırı olsa dahi dilediği konuda ve sınırsız biçimde düzenleme yapma yetkisini haizdir",
   "Kurulun çıkardığı tebliğler yalnızca tavsiye niteliğinde olup ilgililer bakımından bağlayıcı değildir",
   "Kurul yalnızca kanun teklifi hazırlayabilir; ikincil mevzuat yapma yetkisi yalnızca Bakanlığa aittir"],
  "6362 sayılı SPKn m.128: Kurul, Kanunun uygulanmasına ilişkin tebliğ ve kararlarla ikincil düzenlemeler yapmakla yetkilidir; bu düzenlemeler ilgililer bakımından bağlayıcıdır.",
  "6362 sayılı SPKn m.128")

q("spk_ve_duzenleme", "SPK ve Düzenleme",
  "Kurul kararlarına karşı başvuru yolu bakımından aşağıdakilerden hangisi doğrudur?",
  "Kurulun idari yaptırım kararlarına karşı idari yargı yoluna başvurulabilir",
  ["Kurul kararları kesin ve nihai olup hiçbir biçimde yargı denetimine tabi tutulamamaktadır",
   "Kurul kararlarına karşı yalnızca Kurulun kendisine itiraz edilebilir; yargı yolu tümüyle kapalıdır",
   "Kurul kararlarına karşı yalnızca adli yargıda ceza davası açılabilir; iptal davası açılamaz",
   "Kurul kararlarına karşı başvuru yalnızca ihraççılara tanınmış olup yatırımcılar başvuramaz"],
  "Kurulun idari nitelikteki kararları idari işlem olduğundan idari yargı denetimine tabidir; ilgililer iptal davası açabilir.",
  "6362 sayılı SPKn - Kurul kararlarının denetimi")

q("spk_ve_duzenleme", "SPK ve Düzenleme",
  "Yatırımcı Tazmin Merkezi bakımından aşağıdakilerden hangisi doğrudur?",
  "Yatırım kuruluşlarının nakit ödeme veya araç teslim yükümlülüğünü yerine getirememesi hâlinde tazminle görevli kamu tüzel kişisidir",
  ["Yatırımcıların borsada uğradığı her türlü fiyat kaybını karşılamak ve her yatırımcının anaparasıyla beklenen getirisini güvence altına almakla görevli bir fondur",
   "Yatırım kuruluşlarının kârlarından pay alarak ortaklarına dağıtan bir portföy yönetim kuruluşudur",
   "Yalnızca bankaların mevduat sahiplerine karşı yükümlülüklerini güvence altına alan bir kuruluştur",
   "İhraççı şirketlerin kâr payı dağıtmaması hâlinde ortaklara tazminat ödemekle yükümlü bir merkezdir"],
  "6362 sayılı SPKn m.83: Yatırımcı Tazmin Merkezi, yatırım kuruluşlarının yatırımcılara karşı nakit ödeme ve sermaye piyasası aracı teslim yükümlülüklerini yerine getirememesi hâlinde tazminle görevlidir; piyasa riski/fiyat kaybı kapsam dışıdır.",
  "6362 sayılı SPKn m.83")

q("spk_ve_duzenleme", "SPK ve Düzenleme",
  "Sermaye Piyasası Kurulu bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. İdari ve mali özerkliğe sahiptir\n\nII. Tebliğlerle ikincil düzenleme yapabilir\n\nIII. Sermaye piyasası uyuşmazlıklarında mahkeme sıfatıyla hüküm kurar",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Kurul idari ve mali özerkliğe sahiptir (I) ve tebliğlerle ikincil düzenleme yapar (II). Ancak yargı yetkisi yoktur; uyuşmazlıkları mahkemeler çözer, bu nedenle III yanlıştır.",
  "6362 sayılı SPKn m.117, 128")

# ══ SERMAYE PİYASASI ARAÇLARI (5) ═════════════════════════════════════════
q("sermaye_piyasasi_araclari", "Sermaye Piyasası Araçları",
  "Sermaye piyasası aracı kavramı bakımından aşağıdakilerden hangisi doğrudur?",
  "Menkul kıymetler ve türev araçlar ile Kurulca bu kapsamda sayılan diğer araçları ifade eder",
  ["Yalnızca anonim ortaklıkların çıkardığı pay senetlerini kapsayan dar bir kavram olarak tanımlanmıştır",
   "Bankaların topladığı her türlü vadeli ve vadesiz mevduatı da kapsayan geniş bir kavram niteliğindedir",
   "Yalnızca devletin çıkardığı borçlanma araçlarını ifade eder; özel sektör araçları kapsam dışıdır",
   "Her türlü taşınmaz ve taşınır malı kapsayan ve mülkiyet hakkını gösteren belgelerin genel adıdır"],
  "6362 sayılı SPKn m.3: sermaye piyasası araçları; menkul kıymetler ve türev araçlar ile yatırım sözleşmeleri de dâhil olmak üzere Kurulca bu kapsamda olduğu belirlenen diğer sermaye piyasası araçlarıdır.",
  "6362 sayılı SPKn m.3")

q("sermaye_piyasasi_araclari", "Sermaye Piyasası Araçları",
  "Pay ile borçlanma aracı arasındaki temel fark bakımından aşağıdakilerden hangisi doğrudur?",
  "Pay ortaklık hakkı verirken, borçlanma aracı ihraççıya karşı alacak hakkı sağlar",
  ["Pay ihraççıya karşı alacak hakkı verirken, borçlanma aracı ortaklık hakkı sağlayan bir araçtır",
   "İkisi de ortaklık hakkı verir; aralarında hukuki nitelik bakımından hiçbir fark bulunmamaktadır",
   "Pay sahibine sabit getiri garantisi verilirken, borçlanma aracı sahibine hiçbir getiri sağlanmaz",
   "Borçlanma aracı sahibi ihraççının genel kurulunda oy kullanma hakkına sahip olan bir ortaktır"],
  "Pay, ihraççıda ortaklık hakkı ve kâra katılma sağlar; borçlanma aracı ise ihraççıya karşı belirli bir alacak hakkı doğurur ve sahibine ortaklık hakkı vermez.",
  "6362 sayılı SPKn m.3 - pay/borçlanma aracı")

q("sermaye_piyasasi_araclari", "Sermaye Piyasası Araçları",
  "Borçlanma aracının ihraççı bakımından doğurduğu sonuç bakımından aşağıdakilerden hangisi doğrudur?",
  "İhraççı, aracın vadesinde anapara ve varsa getirisini ödemekle yükümlü hâle gelir",
  ["İhraççı, borçlanma aracı sahiplerini şirketin ortağı yapmak ve genel kurulda oy hakkı tanımakla yükümlenir",
   "İhraççının hiçbir geri ödeme yükümlülüğü doğmaz; borçlanma aracı bağış niteliğinde kabul edilmektedir",
   "İhraççı, yalnızca kâr ettiği yıllarda ödeme yapar; zarar hâlinde borç kendiliğinden ortadan kalkar",
   "İhraççı, borçlanma aracı sahiplerine şirket tasfiye edilmedikçe hiçbir ödeme yapmak zorunda değildir"],
  "Borçlanma aracı ihraççı bakımından bir borç ilişkisi doğurur; ihraççı vadesinde anaparayı ve varsa getirisini ödemekle yükümlüdür.",
  "6362 sayılı SPKn - borçlanma araçları")

q("sermaye_piyasasi_araclari", "Sermaye Piyasası Araçları",
  "Türev araçlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Değeri, dayanak bir varlığın veya göstergenin değerine bağlı olarak belirlenen sözleşmelerdir",
  ["Değeri hiçbir dayanak varlığa bağlı olmayan ve ihraççının ortaklık yapısını gösteren belgelerdir",
   "Yalnızca devlet tarafından ihraç edilebilen ve anapara garantisi taşıyan borçlanma senetleridir",
   "Sahibine ihraççı şirketin genel kurulunda oy kullanma hakkı veren ortaklık payı niteliğindedir",
   "Bankaların topladığı mevduatın karşılığında düzenlediği ve mevduat sahibine verdiği belgelerdir"],
  "Türev araç, değeri bir dayanak varlığın (pay, endeks, döviz, emtia vb.) veya göstergenin değerine bağlı olarak belirlenen sözleşmelerdir.",
  "6362 sayılı SPKn m.3 - türev araç")

q("sermaye_piyasasi_araclari", "Sermaye Piyasası Araçları",
  "Aşağıdakilerden hangileri 6362 sayılı Kanun'a göre sermaye piyasası aracı sayılır?\n\nI. Pay\n\nII. Borçlanma aracı\n\nIII. Vadeli banka mevduatı",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Pay (I) ve borçlanma aracı (II) menkul kıymet olarak sermaye piyasası aracıdır. Banka mevduatı (III) ise bankacılık mevzuatının konusudur ve sermaye piyasası aracı değildir.",
  "6362 sayılı SPKn m.3")

# ══ İHRAÇ VE HALKA ARZ (6) ════════════════════════════════════════════════
q("ihrac_ve_halka_arz", "İhraç ve Halka Arz",
  "İzahnamenin işlevi bakımından aşağıdakilerden hangisi doğrudur?",
  "Yatırımcıların ihraççıyı ve sermaye piyasası aracını değerlendirebilmesi için gerekli bilgileri içeren kamuyu aydınlatma belgesidir",
  ["İhraççının yalnız Kurula sunduğu, yatırımcılara hiçbir biçimde açıklanmayan ve ihraç tamamlandıktan sonra da sürekli gizli tutulması gereken bir iç değerlendirme raporudur",
   "Sermaye piyasası aracının gelecekteki fiyatını ve getirisini Kurulca garanti eden resmî bir taahhütnamedir",
   "İhraççının vergi dairesine sunmakla yükümlü olduğu ve mali durumu gösteren bir beyanname niteliğindedir",
   "Yalnızca borsanın iç işleyişini düzenleyen ve yatırımcıları ilgilendirmeyen teknik bir yönerge metnidir"],
  "6362 sayılı SPKn m.3, 4: izahname, yatırımcıların ihraççıyı ve sermaye piyasası aracını değerlendirmesine imkân verecek bilgileri içeren kamuyu aydınlatma belgesidir.",
  "6362 sayılı SPKn m.4")

q("ihrac_ve_halka_arz", "İhraç ve Halka Arz",
  "İzahnamenin Kurulca onaylanmasının anlamı bakımından aşağıdakilerden hangisi doğrudur?",
  "Onay, izahnamedeki bilgilerin tutarlı, anlaşılabilir ve mevzuata uygun olduğunun incelenmesidir; yatırımın kârlılığına ilişkin bir güvence değildir",
  ["Onay, Kurulun sermaye piyasası aracının kârlı bir yatırım olduğunu tasdik ettiği anlamına gelmektedir",
   "Onay, ihraççının gelecekteki mali başarısının ve aracın vade sonuna kadar sağlayacağı asgari getirinin Kurul tarafından garanti edildiğini gösteren bir belgedir",
   "Onay, izahnamedeki bilgilerin doğruluğundan ihraççının değil doğrudan Kurulun sorumlu olduğu sonucunu doğurur",
   "Onay, aracın borsada belirli bir fiyatın altına düşmeyeceğine ilişkin resmî bir taahhüt niteliğindedir"],
  "6362 sayılı SPKn m.6: izahnamenin Kurulca onaylanması, izahnamede yer alan bilgilerin tutarlı, anlaşılabilir ve mevzuata uygun olduğunun incelenmesi anlamına gelir; aracın veya ihraççının tekeffülü ya da yatırımın reklamı sayılmaz.",
  "6362 sayılı SPKn m.6")

q("ihrac_ve_halka_arz", "İhraç ve Halka Arz",
  "İzahnameden doğan sorumluluk bakımından aşağıdakilerden hangisi doğrudur?",
  "İzahnamedeki yanlış, yanıltıcı veya eksik bilgiden kaynaklanan zararlardan öncelikle ihraççı sorumludur",
  ["İzahnamedeki bilgilerden hiç kimse sorumlu tutulamaz; yatırımcı riski tümüyle kendisi üstlenmiş sayılır",
   "İzahnamedeki bilgilerin doğruluğundan yalnızca izahnameyi onaylayan Kurul sorumlu tutulmaktadır",
   "Sorumluluk yalnızca aracı kuruma aittir; ihraççının izahname bakımından hiçbir sorumluluğu bulunmaz",
   "İzahnameden doğan sorumluluk yalnızca ceza hukuku bakımından doğar; tazminat talep edilemez"],
  "6362 sayılı SPKn m.10: izahnamede yer alan yanlış, yanıltıcı veya eksik bilgilerden kaynaklanan zararlardan ihraççılar sorumludur; zararın ihraççıdan tazmin edilememesi hâlinde kanunda sayılan diğer kişiler de sorumlu tutulabilir.",
  "6362 sayılı SPKn m.10")

q("ihrac_ve_halka_arz", "İhraç ve Halka Arz",
  "Halka arz edilmeksizin yapılan ihraçlar bakımından aşağıdakilerden hangisi doğrudur?",
  "Bu ihraçlarda izahname yerine Kurulca onaylanan ihraç belgesi düzenlenir",
  ["Halka arz edilmeksizin ihraç kanunen yasak olup her ihraç mutlaka halka arz yoluyla yapılmak zorundadır",
   "Bu ihraçlarda da tıpkı halka arzdaki gibi izahname düzenlenmesi ve onaylanması zorunlu tutulmuştur",
   "Halka arz edilmeksizin yapılan ihraçlarda hiçbir belge düzenlenmez ve Kurul onayı da aranmamaktadır",
   "Bu ihraçlar yalnızca borsada işlem gören şirketler tarafından ve Kurul izni olmadan yapılabilmektedir"],
  "6362 sayılı SPKn m.11: sermaye piyasası araçlarının halka arz edilmeksizin ihracında izahname yerine Kurulca onaylanacak ihraç belgesi düzenlenir.",
  "6362 sayılı SPKn m.11")

q("ihrac_ve_halka_arz", "İhraç ve Halka Arz",
  "Halka açık ortaklık kavramı bakımından aşağıdakilerden hangisi doğrudur?",
  "Payları halka arz edilmiş olan veya halka arz edilmiş sayılan anonim ortaklıklar halka açık ortaklıktır",
  ["Yalnızca payları borsada fiilen işlem gören şirketler halka açık ortaklık olarak kabul edilmektedir",
   "Her anonim şirket kuruluşundan itibaren kendiliğinden halka açık ortaklık statüsünü kazanmış sayılır",
   "Halka açık ortaklık statüsü yalnızca kamu kurumlarının ortak olduğu şirketlere tanınan bir niteliktir",
   "Limited şirketler de payları halka arz edildiğinde halka açık ortaklık statüsü kazanabilmektedir"],
  "6362 sayılı SPKn m.16: payları halka arz olunmuş olan veya halka arz olunmuş sayılan anonim ortaklıklar halka açık ortaklıktır. Pay sahibi sayısı kanunda belirlenen sayıyı aşan ortaklıkların payları halka arz olunmuş sayılır.",
  "6362 sayılı SPKn m.16")

q("ihrac_ve_halka_arz", "İhraç ve Halka Arz",
  "İhraç ve halka arza ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Halka arzda kural olarak izahname düzenlenir\n\nII. Halka arz edilmeksizin ihraçta ihraç belgesi düzenlenir\n\nIII. Kurulun izahnameyi onaylaması yatırımın kârlılığını garanti eder",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Halka arzda izahname (I), halka arz edilmeksizin ihraçta ihraç belgesi (II) düzenlenir. Kurul onayı ise yalnızca bilgilerin tutarlı ve mevzuata uygun olduğunun incelenmesidir; kârlılık garantisi vermez, bu nedenle III yanlıştır.",
  "6362 sayılı SPKn m.4, 6, 11")

# ══ KAMUYU AYDINLATMA (6) ═════════════════════════════════════════════════
q("kamuyu_aydinlatma", "Kamuyu Aydınlatma",
  "Kamuyu Aydınlatma Platformu bakımından aşağıdakilerden hangisi doğrudur?",
  "Mevzuat uyarınca kamuya açıklanması gereken bilgilerin elektronik ortamda imzalanarak yayımlandığı sistemdir",
  ["Yalnızca Kurul personelinin erişebildiği ve kamuya kapalı tutulan gizli bir iç bilgi sistemidir",
   "Yatırımcıların birbirleriyle pay alım satımı yaptığı ve emirlerin eşleştiği bir işlem platformudur",
   "İhraççıların vergi beyannamelerini elektronik ortamda verdikleri resmî bir maliye uygulamasıdır",
   "Yalnızca borsa şirketinin kendi iç yönetim kararlarını duyurduğu kurumsal bir duyuru panosudur"],
  "6362 sayılı SPKn m.15: mevzuat uyarınca kamuya açıklanması gereken bilgiler, elektronik imza kullanılarak Kamuyu Aydınlatma Platformu üzerinden kamuya duyurulur.",
  "6362 sayılı SPKn m.15", "easy")

q("kamuyu_aydinlatma", "Kamuyu Aydınlatma",
  "İçsel bilgi kavramı bakımından aşağıdakilerden hangisi doğrudur?",
  "Henüz kamuya açıklanmamış, açıklandığında sermaye piyasası aracının fiyatını etkileyebilecek nitelikteki kesin bilgidir",
  ["Daha önce KAP'ta açıklanmış, piyasadaki bütün yatırımcıların erişimine açılmış ve fiyat üzerindeki etkisini tamamen göstermiş her türlü genel nitelikli bilgidir",
   "İhraççının fiyat üzerinde hiçbir etkisi bulunmayan ve önemsiz kabul edilen sıradan iç yazışmalarıdır",
   "Yalnızca gelecekte gerçekleşmesi belirsiz olan söylenti ve tahminleri ifade eden bir bilgi türüdür",
   "İhraççının vergi dairesine bildirdiği ve kamuoyuyla hiçbir ilgisi bulunmayan mali kayıtlarıdır"],
  "İçsel bilgi; henüz kamuya açıklanmamış, doğrudan veya dolaylı olarak ihraççıya ya da sermaye piyasası aracına ilişkin, açıklandığında aracın fiyatını veya yatırımcıların kararlarını etkileyebilecek nitelikteki kesin bir bilgidir.",
  "6362 sayılı SPKn m.106 - içsel bilgi")

q("kamuyu_aydinlatma", "Kamuyu Aydınlatma",
  "İçsel bilginin açıklanmasının ertelenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "İhraççı, meşru menfaatlerinin zarar görmemesi için sorumluluğu kendisine ait olmak üzere ve yatırımcıları yanıltmamak koşuluyla açıklamayı erteleyebilir",
  ["İçsel bilginin açıklanması hiçbir hâlde ertelenemez; her bilgi öğrenildiği anda derhâl açıklanmalıdır",
   "İhraççı içsel bilgiyi, fiyat üzerindeki etkisi tümüyle ortadan kalkıncaya kadar hiçbir kayıt veya bildirim yükümlülüğü olmaksızın süresiz olarak erteleyebilmektedir",
   "Erteleme kararını yalnızca Kurul verebilir; ihraççının bu konuda hiçbir takdir yetkisi bulunmamaktadır",
   "Erteleme hâlinde ihraççının hiçbir sorumluluğu doğmaz; sorumluluk tümüyle Kurula geçmiş sayılır"],
  "İhraççılar, meşru menfaatlerinin zarar görmemesi için, yatırımcıların yanıltılmasına yol açmamak ve bilginin gizliliğini sağlamak koşuluyla, sorumluluğu kendilerine ait olmak üzere içsel bilginin açıklanmasını erteleyebilir.",
  "6362 sayılı SPKn m.15 - erteleme")

q("kamuyu_aydinlatma", "Kamuyu Aydınlatma",
  "Halka açık ortaklıkların finansal raporları bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal raporlar Kurulca belirlenen standartlara uygun hazırlanır ve bağımsız denetimden geçirilir",
  ["Halka açık ortaklıklar finansal rapor hazırlamak ve kamuya açıklamakla hiçbir biçimde yükümlü değildir",
   "Finansal raporların bağımsız denetimden geçirilmesi tümüyle ortaklığın takdirine bırakılmış bir tercihtir",
   "Finansal raporlar yalnızca Kurula sunulur ve hiçbir koşulda kamuya açıklanmaz; gizli tutulur",
   "Finansal raporları ortaklık değil, doğrudan Kurul hazırlar ve ortaklık adına kamuya duyurur"],
  "6362 sayılı SPKn m.14: ihraççılar ve sermaye piyasası kurumları finansal raporlarını Kurulca belirlenen standartlara uygun olarak hazırlar, bağımsız denetimden geçirir ve kamuya açıklar.",
  "6362 sayılı SPKn m.14")

q("kamuyu_aydinlatma", "Kamuyu Aydınlatma",
  "Bağımsız denetim kuruluşunun sorumluluğu bakımından aşağıdakilerden hangisi doğrudur?",
  "Denetim kuruluşu, hazırladığı raporlardaki yanlış ve yanıltıcı bilgiler nedeniyle doğan zararlardan sorumludur",
  ["Bağımsız denetim kuruluşunun raporu nedeniyle hiçbir hukuki sorumluluğu doğmaz; sorumluluk yalnızca ihraççıdadır",
   "Denetim kuruluşu yalnızca ihraççıya karşı sorumlu olup üçüncü kişilere karşı hiçbir sorumluluk taşımaz",
   "Denetim kuruluşunun sorumluluğu yalnızca ihraççının iflas etmesi hâlinde ve iflas masasına karşı doğar",
   "Bağımsız denetim raporu yalnızca tavsiye niteliğinde olduğundan hiçbir bağlayıcılığı bulunmamaktadır"],
  "6362 sayılı SPKn m.16 vd.: bağımsız denetim kuruluşları, denetledikleri finansal tablolara ilişkin hazırladıkları raporlardaki yanlış ve yanıltıcı bilgi ve kanaatler nedeniyle doğan zararlardan sorumludur.",
  "6362 sayılı SPKn - bağımsız denetim sorumluluğu")

q("kamuyu_aydinlatma", "Kamuyu Aydınlatma",
  "Kamuyu aydınlatmaya ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Açıklamalar KAP üzerinden elektronik imzayla yapılır\n\nII. İçsel bilgi, açıklandığında fiyatı etkileyebilecek nitelikte bilgidir\n\nIII. İçsel bilginin açıklanması hiçbir koşulda ertelenemez",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Açıklamalar KAP üzerinden elektronik imzayla yapılır (I) ve içsel bilgi fiyatı etkileyebilecek nitelikte kesin bilgidir (II). Ancak ihraççı, meşru menfaatlerini korumak için koşullara uyarak açıklamayı erteleyebilir; bu nedenle III yanlıştır.",
  "6362 sayılı SPKn m.15")

# ══ KOLEKTİF YATIRIM (5) ══════════════════════════════════════════════════
q("kolektif_yatirim", "Kolektif Yatırım Kuruluşları",
  "Yatırım fonu ile yatırım ortaklığı arasındaki temel fark bakımından aşağıdakilerden hangisi doğrudur?",
  "Yatırım ortaklığı anonim ortaklık olarak tüzel kişiliğe sahipken, yatırım fonunun tüzel kişiliği yoktur",
  ["Yatırım fonu tüzel kişiliğe sahipken, yatırım ortaklığının ayrı bir tüzel kişiliği bulunmamaktadır",
   "İkisi de tüzel kişiliğe sahip olup aralarında hukuki yapı bakımından hiçbir fark bulunmamaktadır",
   "İkisinin de tüzel kişiliği yoktur; ikisi de yalnızca bir sözleşme ilişkisinden ibaret sayılmaktadır",
   "Yatırım ortaklığı yalnızca gerçek kişilerce, yatırım fonu ise yalnızca bankalarca kurulabilmektedir"],
  "6362 sayılı SPKn m.48, 52: yatırım ortaklıkları anonim ortaklık şeklinde kurulur ve tüzel kişiliğe sahiptir; yatırım fonu ise tüzel kişiliği bulunmayan, inançlı mülkiyet esasına dayalı bir malvarlığıdır.",
  "6362 sayılı SPKn m.48, 52")

q("kolektif_yatirim", "Kolektif Yatırım Kuruluşları",
  "Yatırım fonunun hukuki niteliği bakımından aşağıdakilerden hangisi doğrudur?",
  "Katılma payı sahiplerinin hesabına, inançlı mülkiyet esaslarına göre portföy işletmek amacıyla oluşturulan malvarlığıdır",
  ["Ortaklarına genel kurulda oy hakkı veren ve pay sahiplerine portföydeki varlıklar üzerinde doğrudan mülkiyet sağlayan bir anonim ortaklık türü olarak kurulmaktadır",
   "Bankaların topladığı mevduatı yönetmek amacıyla kurulan ve mevduat garantisi taşıyan bir kuruluştur",
   "Kurucusunun kendi malvarlığıyla tümüyle birleşen ve ondan ayrılamayan bir hesap kalemi niteliğindedir",
   "Yalnızca gayrimenkul alım satımı yapmak üzere kurulabilen ve menkul kıymete yatırım yapamayan bir yapıdır"],
  "6362 sayılı SPKn m.52: yatırım fonu, katılma payı sahiplerinin hesabına inançlı mülkiyet esaslarına göre portföy işletmek amacıyla portföy yönetim şirketlerince oluşturulan malvarlığıdır; tüzel kişiliği yoktur.",
  "6362 sayılı SPKn m.52")

q("kolektif_yatirim", "Kolektif Yatırım Kuruluşları",
  "Yatırım fonu malvarlığının korunması bakımından aşağıdakilerden hangisi doğrudur?",
  "Fon malvarlığı kurucunun ve portföy saklayıcısının malvarlığından ayrıdır; haczedilemez ve rehnedilemez",
  ["Fon malvarlığı kurucunun malvarlığıyla birleşir ve kurucunun borçları için serbestçe haczedilebilir",
   "Fon malvarlığı üzerinde katılma payı sahiplerinin hiçbir hakkı bulunmaz; malvarlığı tümüyle kurucuya aittir",
   "Fon malvarlığı yalnızca kurucunun iflası hâlinde ayrılır; normal koşullarda kurucunun malvarlığındadır",
   "Fon malvarlığının ayrılığı yalnızca sözleşmeyle kararlaştırılabilir; kanunda böyle bir koruma yoktur"],
  "6362 sayılı SPKn m.52-54: fon malvarlığı kurucunun ve portföy saklayıcısının malvarlığından ayrıdır; fon malvarlığı rehnedilemez, teminat gösterilemez ve haczedilemez.",
  "6362 sayılı SPKn m.52-54")

q("kolektif_yatirim", "Kolektif Yatırım Kuruluşları",
  "Portföy saklama hizmeti bakımından aşağıdakilerden hangisi doğrudur?",
  "Fon portföyündeki varlıklar, Kurulca yetkilendirilmiş bir portföy saklayıcısı nezdinde saklanır",
  ["Fon portföyündeki varlıklar kurucunun kendi kasasında saklanır; ayrı bir saklayıcı aranmamaktadır",
   "Portföy saklama hizmeti tümüyle isteğe bağlı olup fonlar bu hizmeti almadan da faaliyet gösterebilir",
   "Portföy saklayıcısı fonun yatırım kararlarını da alır ve portföyü kendi takdirine göre yönetir",
   "Portföy saklama görevi doğrudan Sermaye Piyasası Kurulu tarafından yerine getirilmektedir"],
  "6362 sayılı SPKn m.56: fon portföyündeki varlıklar Kurulca yetkilendirilmiş portföy saklayıcısı nezdinde saklanır; saklayıcı yatırım kararı almaz, saklama ve kontrol görevini yürütür.",
  "6362 sayılı SPKn m.56")

q("kolektif_yatirim", "Kolektif Yatırım Kuruluşları",
  "Katılma payı bakımından aşağıdakilerden hangisi doğrudur?",
  "Katılma payı, sahibinin fon portföyüne ve bundan doğan haklara sahip olduğunu gösteren sermaye piyasası aracıdır",
  ["Katılma payı, sahibine fonu kuran şirketin genel kurulunda oy kullanma hakkı veren bir ortaklık payıdır",
   "Katılma payı, fona yatırılan anaparanın ve belirli bir getirinin geri ödenmesini garanti eden bir senettir",
   "Katılma payı, sahibine fon portföyündeki belirli bir varlığın mülkiyetini doğrudan veren bir belgedir",
   "Katılma payı bir sermaye piyasası aracı sayılmaz; yalnızca fonla yapılan bir kredi sözleşmesidir"],
  "6362 sayılı SPKn m.52: katılma payı, yatırımcının fon portföyüne ve bundan doğan haklara sahip olduğunu gösteren, kayden izlenen bir sermaye piyasası aracıdır; ortaklık hakkı vermez ve getiri garantisi taşımaz.",
  "6362 sayılı SPKn m.52")

# ══ KAYDİ SİSTEM (5) ══════════════════════════════════════════════════════
q("kaydi_sistem", "Kaydi Sistem ve MKK",
  "Merkezi Kayıt Kuruluşu bakımından aşağıdakilerden hangisi doğrudur?",
  "Kaydileştirilen sermaye piyasası araçlarını ve bunlara ilişkin hakları izleyen merkezi saklama kuruluşudur",
  ["Sermaye piyasası araçlarının alım satım emirlerini eşleştiren ve fiyat oluşturan borsa kuruluşudur",
   "İhraççı şirketlerin bağımsız denetimini yapmakla görevli ve Kurula bağlı bir denetim kuruluşudur",
   "Yatırımcıların uğradığı her türlü zararı tazmin etmekle yükümlü bir güvence fonu niteliğindedir",
   "Yalnızca kâğıt üzerinde basılı pay senetlerini fiziki olarak arşivleyen bir depolama merkezidir"],
  "6362 sayılı SPKn m.80: Merkezi Kayıt Kuruluşu, kaydileştirilen sermaye piyasası araçlarını ve bunlara ilişkin hakları, üyeler ve hak sahipleri itibarıyla kayden izleyen merkezi saklama kuruluşudur.",
  "6362 sayılı SPKn m.80")

q("kaydi_sistem", "Kaydi Sistem ve MKK",
  "Kaydileştirme bakımından aşağıdakilerden hangisi doğrudur?",
  "Sermaye piyasası araçları senede bağlanmaksızın elektronik ortamda kayden ihraç edilir ve izlenir",
  ["Kaydileştirilen araçlar yine de kâğıt üzerine basılır ve fiziki senet hak sahibine teslim edilmek zorundadır",
   "Kaydileştirme yalnızca borsada işlem gören araçlar için geçerli olup diğer araçları hiç kapsamamaktadır",
   "Kaydileştirme, hak sahipliğinin ispatını imkânsız kılar; bu nedenle uygulamada tercih edilmemektedir",
   "Kaydileştirilen araçlarda hak sahipliği yalnızca ihraççının kendi tuttuğu özel defterden izlenmektedir"],
  "6362 sayılı SPKn m.13: sermaye piyasası araçları kaydileştirilerek senede bağlanmaksızın elektronik ortamda ihraç edilir ve MKK tarafından kayden izlenir.",
  "6362 sayılı SPKn m.13")

q("kaydi_sistem", "Kaydi Sistem ve MKK",
  "Kaydi sistemde hak sahipliğinin ispatı bakımından aşağıdakilerden hangisi doğrudur?",
  "Hak sahipliği, Merkezi Kayıt Sistemindeki kayıtlarla tespit edilir",
  ["Hak sahipliği yalnızca fiziki senedin zilyetliğiyle ispatlanabilir; kayıtların hiçbir ispat gücü yoktur",
   "Hak sahipliği yalnızca ihraççının vereceği bir yazıyla ispatlanır; MKK kayıtları dikkate alınmaz",
   "Kaydi sistemde hak sahipliği hiçbir biçimde ispat edilemez; bu nedenle uyuşmazlıklar çözümsüz kalır",
   "Hak sahipliği yalnızca noterde düzenlenen bir tespit tutanağıyla ve mahkeme kararıyla belirlenebilir"],
  "6362 sayılı SPKn m.13 ve m.80: kaydileştirilen araçlarda hak sahipliği Merkezi Kayıt Sistemindeki kayıtlarla tespit edilir; kayıtlar hak sahipliğinin ispatına esas alınır.",
  "6362 sayılı SPKn m.13 ve m.80")

q("kaydi_sistem", "Kaydi Sistem ve MKK",
  "Kaydi sistemin sağladığı yarar bakımından aşağıdakilerden hangisi doğrudur?",
  "Senetlerin kaybolma, çalınma ve sahtecilik riskini ortadan kaldırarak devir işlemlerini hızlandırır",
  ["Yatırımcının uğrayacağı fiyat kaybını önleyerek sermaye piyasası araçlarına getiri garantisi sağlar",
   "İhraççının borçlarını ortadan kaldırarak yatırımcıya karşı yükümlülüklerinden kurtulmasını sağlar",
   "Sermaye piyasası araçlarının devrini imkânsız hâle getirerek piyasadaki işlem hacmini azaltmaktadır",
   "Kurulun denetim yetkisini ortadan kaldırarak ihraççılara tam bir serbesti tanımış olmaktadır"],
  "Kaydi sistem, fiziki senet bulunmadığından kaybolma, çalınma ve sahtecilik risklerini ortadan kaldırır; devir ve hak kullanımı elektronik kayıtla hızlı biçimde gerçekleşir.",
  "6362 sayılı SPKn m.13 - kaydi sistemin yararı")

q("kaydi_sistem", "Kaydi Sistem ve MKK",
  "Kaydi sisteme ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Araçlar senede bağlanmaksızın kayden ihraç edilir\n\nII. Hak sahipliği MKS kayıtlarıyla tespit edilir\n\nIII. Kaydileştirilen araçlar için ayrıca fiziki senet basılması zorunludur",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Kaydileştirilen araçlar senede bağlanmaksızın kayden ihraç edilir (I) ve hak sahipliği MKS kayıtlarıyla tespit edilir (II). Kaydi sistemin özü fiziki senedin bulunmamasıdır; bu nedenle III yanlıştır.",
  "6362 sayılı SPKn m.13 ve m.80")

# ══ PİYASA SUÇLARI (5) ════════════════════════════════════════════════════
q("piyasa_suclari", "Piyasa Suçları ve Bozucu Eylemler",
  "Bilgi suistimali (içeriden öğrenenlerin ticareti) suçu bakımından aşağıdakilerden hangisi doğrudur?",
  "Kamuya açıklanmamış etkili bilgiyi sermaye piyasası işleminde kullanıp menfaat sağlanmasıyla oluşur",
  ["Kamuya açıklanmış ve herkesin bildiği bilgilere dayanarak işlem yapılmasıyla oluşan bir suç türüdür",
   "Yalnızca ihraççının yönetim kurulu başkanı tarafından işlenebilen ve diğer kişileri kapsamayan bir suçtur",
   "Sermaye piyasası aracının fiyatının düşmesi hâlinde kendiliğinden oluştuğu kabul edilen bir suçtur",
   "Yalnızca yabancı yatırımcıların işleyebileceği ve yerli yatırımcıları hiç ilgilendirmeyen bir fiildir"],
  "6362 sayılı SPKn m.105: araç veya ihraççı hakkında fiyatı, değeri ya da yatırımcı kararını etkileyebilecek ve henüz kamuya duyurulmamış bilgiyi kullanarak menfaat sağlamak bilgi suistimali suçudur.",
  "6362 sayılı SPKn m.105")

q("piyasa_suclari", "Piyasa Suçları ve Bozucu Eylemler",
  "Piyasa dolandırıcılığı suçu bakımından aşağıdakilerden hangisi doğrudur?",
  "Fiyat, arz veya talep hakkında yanıltıcı görünüm yaratan işlem, emir veya hesap hareketleriyle işlenebilir",
  ["Yalnızca yatırımcının fiilen zarar etmesi ve failin bu zarardan doğrudan ekonomik yarar sağlaması hâlinde oluşan; zarar doğmazsa işlenmemiş sayılan bir suçtur",
   "Sermaye piyasasında kâr elde edilmesi hâlinde kendiliğinden oluşan ve kastı aranmayan bir suç türüdür",
   "Yalnızca aracı kurumlar tarafından işlenebilen ve gerçek kişileri hiçbir biçimde kapsamayan bir suçtur",
   "İhraççının izahname düzenlememesi hâlinde oluşan ve piyasa işlemleriyle ilgisi bulunmayan bir suçtur"],
  "6362 sayılı SPKn m.106: meşru gerekçe olmadan fiyat, fiyat değişimi, arz veya talep hakkında yanlış ya da yanıltıcı izlenim yaratacak işlem, emir, emir iptali ve hesap hareketleri piyasa dolandırıcılığı kapsamında olabilir.",
  "6362 sayılı SPKn m.106")

q("piyasa_suclari", "Piyasa Suçları ve Bozucu Eylemler",
  "Piyasa bozucu eylem bakımından aşağıdakilerden hangisi doğrudur?",
  "Suç oluşturmamakla birlikte piyasanın güven ve işleyişini bozan eylemler olup idari yaptırıma tabidir",
  ["Piyasa bozucu eylemler her hâlde suç oluşturur ve yalnızca hapis cezasıyla yaptırıma bağlanmaktadır",
   "Piyasa bozucu eylemlerin hiçbir yaptırımı bulunmayıp yalnızca etik bir sorun olarak değerlendirilir",
   "Piyasa bozucu eylem yalnızca ihraççılar bakımından söz konusu olup yatırımcıları hiç kapsamamaktadır",
   "Piyasa bozucu eylemler yalnızca borsa tarafından tespit edilir; Kurulun bu konuda yetkisi yoktur"],
  "6362 sayılı SPKn m.103: meşru bir ekonomik veya finansal gerekçeyle açıklanamayan, borsanın güven, açıklık ve istikrar içinde çalışmasını bozacak eylemler suç oluşturmamak kaydıyla piyasa bozucu sayılır ve idari para cezası uygulanır.",
  "6362 sayılı SPKn m.103")

q("piyasa_suclari", "Piyasa Suçları ve Bozucu Eylemler",
  "Sermaye piyasasında güveni kötüye kullanma suçu bakımından aşağıdakilerden hangisi doğrudur?",
  "Yatırımcılara ait varlıkları görevi kötüye kullanarak kendisi veya başkası yararına kullanan kişilerce işlenir",
  ["Yalnızca yatırımcının kâr elde edememesi hâlinde oluşan ve kasıt aranmayan bir suç türü niteliğindedir",
   "Sermaye piyasası araçlarının borsada fiyatının düşmesi hâlinde kendiliğinden oluşmuş kabul edilir",
   "Yalnızca ihraççı şirketin ortakları tarafından işlenebilen ve aracı kurumları kapsamayan bir suçtur",
   "İzahnamenin geç düzenlenmesi hâlinde oluşan ve varlıkların kullanımıyla ilgisi bulunmayan bir fiildir"],
  "6362 sayılı SPKn m.109: yatırım kuruluşuna veya Kanunda sayılan diğer sorumlulara teslim edilen sermaye piyasası aracı, nakit ve diğer kıymetleri kendisi ya da başkası menfaatine kullanmak güveni kötüye kullanma suçunu oluşturur.",
  "6362 sayılı SPKn m.109")

q("piyasa_suclari", "Piyasa Suçları ve Bozucu Eylemler",
  "Piyasa suçları ve bozucu eylemlere ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Bilgi suistimali kamuya açıklanmamış etkili bilginin kullanılmasıyla menfaat sağlanmasını gerektirir\n\nII. Piyasa bozucu eylem, suç oluşturmamak kaydıyla idari yaptırıma tabidir\n\nIII. Piyasa dolandırıcılığı için yatırımcının fiilen zarar etmiş olması şarttır",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Bilgi suistimali nitelikli bilginin kullanılmasıyla menfaat sağlanmasını gerektirir; piyasa bozucu eylem suç oluşturmamak kaydıyla idari para cezasına tabidir. Piyasa dolandırıcılığında yatırımcının fiilen zarar etmesi şart olmadığından III yanlıştır.",
  "6362 sayılı SPKn m.103, m.105 ve m.106")

print("TOPLAM:", len(Q))

# ══ BUILD ═════════════════════════════════════════════════════════════════
def gen_letters(n, seed):
    r = random.Random(seed)
    base = ["ABCDE"[i % 5] for i in range(n)]
    while True:
        r.shuffle(base)
        if all(not (base[i] == base[i-1] == base[i-2]) for i in range(2, len(base))):
            return base

def emit(items, prefix, seed):
    letters = gen_letters(len(items), seed)
    out = []
    for i, it in enumerate(items):
        ans = letters[i]
        choices = {ans: it["correct"]}
        for k, d in zip([k for k in "ABCDE" if k != ans], it["distractors"]):
            choices[k] = d
        out.append({
            "id": f"{prefix}-{i+1:04d}", "lessonId": L, "topicId": it["topic"],
            "question": it["stem"], "choices": choices, "correctAnswer": ans,
            "explanation": it["why"],
            "source": {"kind": "generated", "styleRef": "2026/1 test biçimi",
                       "legislationRef": it["ref"]},
            "tags": ["Özgün Soru", "2026 Formatı", "Bölüm Havuzu", it["label"]],
            "difficulty": it["difficulty"], "updatedAt": "2026-07-15T00:00:00Z",
            "examPeriod": "2026/1 formatına uyumlu", "legislationVersion": "2026-07-15",
            "sourceUpdatedAt": "2026-07-15T00:00:00Z", "isPremium": False, "isActive": True,
        })
    return out

if __name__ == "__main__":
    assert len(Q) == 38, f"38 olmalı, şu an {len(Q)}"
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in Q if len(MARK.findall(x["stem"])) >= 2]
    duz = [x for x in Q if len(MARK.findall(x["stem"])) < 2]
    t2 = [x for i, x in enumerate(duz) if i % 2 == 0] + [x for i, x in enumerate(onc) if i % 2 == 0]
    t3 = [x for i, x in enumerate(duz) if i % 2 == 1] + [x for i, x in enumerate(onc) if i % 2 == 1]
    print(f"öncüllü {len(onc)} → t2:{len([x for x in t2 if x in onc])} t3:{len([x for x in t3 if x in onc])}")
    root = Path(__file__).resolve().parents[3]
    targets = (
        root / "content" / "yeterlilik",
        root.parent / "smmm_sgs_pratik" / "assets" / "content" / "yeterlilik",
    )
    for items, name, prefix, seed in ((t2, "questions_sermaye_piyasasi_test2_2026.json", "spk-t2", 20260803),
                                      (t3, "questions_sermaye_piyasasi_test3_2026.json", "spk-t3", 20260804)):
        data = emit(items, prefix, seed)
        for target in targets:
            target.mkdir(parents=True, exist_ok=True)
            with (target / name).open("w", encoding="utf-8") as handle:
                json.dump(data, handle, ensure_ascii=False, indent=2)
                handle.write("\n")
        print(f"{name}: {len(data)} soru | harf {''.join(x['correctAnswer'] for x in data)}")
