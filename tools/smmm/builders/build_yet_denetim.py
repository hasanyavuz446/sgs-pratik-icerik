# -*- coding: utf-8 -*-
"""Yeterlilik — Muhasebe Denetimi Test 2 + Test 3 (2×20 = 40 soru).
BDS/TDS dayanaklı. Doğru şık KISA, çeldiriciler UZUN.
explanation'da harf atıfı YOK. Yıla bağlı tutar/oran YOK."""
import json, random, re

L = "denetim"
Q = []
def q(topic, label, stem, correct, distractors, why, ref, difficulty="medium"):
    assert len(distractors) == 4, stem[:44]
    assert correct not in distractors, "doğru şık çeldiricide tekrar: " + stem[:44]
    Q.append(dict(topic=topic, label=label, stem=stem, correct=correct, distractors=distractors,
                  why=why, ref=ref, difficulty=difficulty))

# ══ DENETİM TEMELLERİ (5) ═════════════════════════════════════════════════
q("denetim_temelleri", "Denetim Temelleri",
  "Bağımsız denetimin amacı bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal tabloların raporlama çerçevesine uygunluğu hakkında makul güvence elde ederek görüş bildirmektir",
  ["Finansal tablolarda hiçbir yanlışlık bulunmadığına dair mutlak ve kesin bir güvence sağlamaktır",
   "İşletmenin gelecekteki kârlılığını ve nakit yaratma kapasitesini tahmin ederek yatırımcıya bildirmektir",
   "İşletmenin vergi borcunu hesaplamak ve beyannamesini idare adına denetleyerek onaylamaktır",
   "İşletme yönetiminin performansını ölçmek ve yöneticilere prim belirlemek üzere rapor hazırlamaktır"],
  "BDS 200: bağımsız denetimin amacı, finansal tabloların geçerli finansal raporlama çerçevesine uygun olarak tüm önemli yönleriyle hazırlanıp hazırlanmadığı konusunda makul güvence elde etmek ve görüş bildirmektir.",
  "BDS 200 - denetimin amacı", "easy")

q("denetim_temelleri", "Denetim Temelleri",
  "Makul güvence kavramı bakımından aşağıdakilerden hangisi doğrudur?",
  "Yüksek düzeyde bir güvencedir; ancak denetimin doğasındaki kısıtlar nedeniyle mutlak güvence değildir",
  ["Mutlak ve kesin bir güvencedir; denetimden geçen tablolarda hiçbir yanlışlık kalmadığını gösterir",
   "Düşük düzeyde bir güvence olup sınırlı bağımsız denetimde sağlanan güvenceyle tümüyle aynıdır",
   "Denetçinin kişisel kanaatini ifade eden ve hiçbir kanıta dayanmayan öznel bir değerlendirmedir",
   "İşletmenin gelecekte iflas etmeyeceğine dair denetçinin verdiği hukuki bir taahhüt niteliğindedir"],
  "BDS 200: makul güvence yüksek bir güvence düzeyidir; ancak örnekleme, muhasebe tahminlerinin doğası ve denetimin kanıt toplama kısıtları nedeniyle mutlak güvence sağlanamaz.",
  "BDS 200 - makul güvence")

q("denetim_temelleri", "Denetim Temelleri",
  "Finansal tabloların hazırlanmasından sorumluluk bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal tabloların hazırlanması ve sunulmasından işletme yönetimi sorumludur; denetçi bunlar hakkında görüş bildirir",
  ["Finansal tabloları denetçi hazırlar ve yönetim yalnızca bunları imzalayarak kamuya açıklamış olur",
   "Finansal tabloların hazırlanmasından denetçi ile yönetim müştereken ve eşit ölçüde sorumlu tutulur",
   "Finansal tabloların sorumluluğu yalnızca işletmenin bağlı olduğu meslek odasına ait bulunmaktadır",
   "Denetçi görüş bildirdiği andan itibaren tabloların hazırlanma sorumluluğu da kendisine geçmiş olur"],
  "BDS 200: finansal tabloların geçerli çerçeveye uygun hazırlanması ve sunulması yönetimin sorumluluğudur; denetçinin sorumluluğu bu tablolar hakkında görüş bildirmektir. Bu ayrım denetimin ön koşuludur.",
  "BDS 200 - sorumluluk ayrımı")

q("denetim_temelleri", "Denetim Temelleri",
  "Mesleki şüphecilik bakımından aşağıdakilerden hangisi doğrudur?",
  "Denetçinin sorgulayıcı bir yaklaşımla, kanıtları eleştirel biçimde değerlendirmesini gerektiren bir tutumdur",
  ["Denetçinin yönetimin her beyanını doğru kabul ederek kanıt aramaksızın kabul etmesini ifade eder",
   "Denetçinin yönetimin baştan dürüst olmadığını varsayması ve her işlemi hile olarak nitelemesidir",
   "Yalnızca hile riski yüksek işletmelerde uygulanan ve diğer denetimlerde aranmayan bir tutumdur",
   "Denetçinin denetim sözleşmesini imzalamadan önce yaptığı ve denetim sırasında aranmayan bir incelemedir"],
  "BDS 200: mesleki şüphecilik, olası bir yanlışlığa işaret edebilecek koşullara karşı dikkatli olmayı ve denetim kanıtlarını eleştirel biçimde değerlendirmeyi içeren sorgulayıcı bir yaklaşımdır. Ne körü körüne güven ne de peşin hükümlü kuşku anlamına gelir.",
  "BDS 200 - mesleki şüphecilik")

q("denetim_temelleri", "Denetim Temelleri",
  "Mesleki muhakeme bakımından aşağıdakilerden hangisi doğrudur?",
  "Denetçinin ilgili bilgi ve tecrübesini kullanarak koşullara uygun kararlar almasıdır",
  ["Denetçinin hiçbir bilgi ve tecrübeye dayanmadan rastgele ve gelişigüzel karar vermesini ifade eder",
   "Denetçinin yönetimin talimatlarına uyarak onun istediği yönde karar almasını gerektiren bir ilkedir",
   "Yalnızca denetim ücreti belirlenirken kullanılan ve denetim çalışmasıyla ilgisi olmayan bir kavramdır",
   "Denetçinin standartları uygulamak yerine kendi kişisel kurallarını serbestçe belirlemesini ifade eder"],
  "BDS 200: mesleki muhakeme; denetim standartları, muhasebe standartları ve etik kurallar çerçevesinde, ilgili eğitim, bilgi ve tecrübenin kullanılarak denetimin koşullarına uygun kararlar alınmasıdır.",
  "BDS 200 - mesleki muhakeme")

# ══ BAĞIMSIZLIK VE ETİK (6) ═══════════════════════════════════════════════
q("bagimsizlik_ve_etik", "Bağımsızlık ve Etik",
  "Bağımsızlığın iki boyutu bakımından aşağıdakilerden hangisi doğrudur?",
  "Özde bağımsızlık denetçinin gerçek tutumunu, şekilde bağımsızlık ise üçüncü kişilerin algısını ifade eder",
  ["Özde bağımsızlık üçüncü kişilerin algısını, şekilde bağımsızlık ise denetçinin iç tutumunu ifade eder",
   "Bağımsızlığın tek bir boyutu vardır; özde ve şekilde ayrımı standartlarda yer almayan bir kavramdır",
   "Özde bağımsızlık yalnızca ücret ilişkisini, şekilde bağımsızlık ise yalnızca akrabalık ilişkisini kapsar",
   "Şekilde bağımsızlık sağlanmışsa özde bağımsızlığın ayrıca değerlendirilmesine hiç gerek kalmamaktadır"],
  "Etik Kurallar: özde bağımsızlık (zihinsel bağımsızlık) denetçinin mesleki muhakemesini etkilemeden görüş oluşturabilmesi; şekilde bağımsızlık ise makul ve bilgili üçüncü kişilerin bağımsızlığın zedelendiği sonucuna varmamasıdır. İkisi birlikte aranır.",
  "Etik Kurallar - bağımsızlığın boyutları")

q("bagimsizlik_ve_etik", "Bağımsızlık ve Etik",
  "Denetçinin daha önce hazırladığı kayıtları sonradan denetlemesi hâlinde ortaya çıkan tehdit bakımından aşağıdakilerden hangisi doğrudur?",
  "Kendi kendini denetleme tehdidi doğar",
  ["Yıldırma tehdidi doğar; denetçi müşteri tarafından baskı altına alınmış sayılmaktadır",
   "Taraf tutma tehdidi doğar; denetçi müşterinin görüşünü savunur duruma geçmiş olur",
   "Yakınlık tehdidi doğar; denetçi müşteriyle uzun süreli bir ilişki kurmuş kabul edilir",
   "Hiçbir tehdit doğmaz; denetçinin kendi hazırladığı kayıtları denetlemesi tümüyle serbesttir"],
  "Etik Kurallar: denetçinin daha önce kendisinin ürettiği bilgiyi/kaydı denetlemesi hâlinde kendi çalışmasını objektif değerlendiremeyeceği varsayıldığından kendi kendini denetleme tehdidi doğar.",
  "Etik Kurallar - kendi kendini denetleme tehdidi")

q("bagimsizlik_ve_etik", "Bağımsızlık ve Etik",
  "Denetçinin müşterisinin davasında onun lehine savunma yapması hâlinde doğan tehdit bakımından aşağıdakilerden hangisi doğrudur?",
  "Taraf tutma tehdidi doğar",
  ["Kendi kendini denetleme tehdidi doğar; denetçi kendi ürettiği bilgiyi değerlendirmiş sayılır",
   "Yakınlık tehdidi doğar; denetçi müşteriyle duygusal bir yakınlık kurmuş kabul edilmektedir",
   "Kişisel çıkar tehdidi doğar; denetçinin müşteride mali menfaati bulunduğu varsayılmaktadır",
   "Hiçbir tehdit doğmaz; denetçinin müşterisini temsil etmesi mesleki bir hak olarak kabul edilir"],
  "Etik Kurallar: denetçinin müşterisinin görüşünü veya konumunu savunması, objektifliğini zedeleyeceğinden taraf tutma (savunuculuk) tehdidi doğurur.",
  "Etik Kurallar - taraf tutma tehdidi")

q("bagimsizlik_ve_etik", "Bağımsızlık ve Etik",
  "Etik Kurallar'daki temel ilkeler bakımından aşağıdakilerden hangisi doğrudur?",
  "Dürüstlük, tarafsızlık, mesleki yeterlik ve özen, gizlilik ile mesleki davranış temel ilkelerdir",
  ["Tek temel ilke kârlılık olup meslek mensubunun azami geliri elde etmesi esas alınmaktadır",
   "Temel ilkeler yalnızca gizlilikten ibaret olup diğer hususlar tavsiye niteliği taşımaktadır",
   "Temel ilkeler yalnızca bağımsız denetçileri bağlar; diğer meslek mensuplarını hiç kapsamaz",
   "Temel ilkeler yalnızca müşteriyle sözleşmede kararlaştırıldığı ölçüde uygulama alanı bulur"],
  "Etik Kurallar: temel ilkeler dürüstlük, tarafsızlık, mesleki yeterlik ve özen, gizlilik ve mesleki davranıştır; meslek mensubu bu ilkelere uymakla yükümlüdür.",
  "Etik Kurallar - temel ilkeler")

q("bagimsizlik_ve_etik", "Bağımsızlık ve Etik",
  "Gizlilik ilkesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Meslek mensubu, mesleki ilişkiden edindiği bilgileri yetki olmadıkça açıklayamaz; kanuni yükümlülük hâlleri saklıdır",
  ["Meslek mensubu edindiği bilgileri hiçbir hâlde ve hiçbir mercie açıklayamaz; istisnası bulunmamaktadır",
   "Meslek mensubu müşteri ilişkisi sona erdikten sonra bilgileri serbestçe açıklayabilir duruma gelir",
   "Gizlilik yalnızca yazılı bilgileri kapsar; sözlü olarak öğrenilen bilgiler kapsam dışında kalır",
   "Gizlilik yalnızca rakip işletmelere karşı geçerli olup üçüncü kişilere bilgi verilmesi serbesttir"],
  "Etik Kurallar: gizlilik ilkesi gereği meslek mensubu, mesleki ve iş ilişkileri sonucu edindiği bilgileri uygun ve özel bir yetki olmadıkça açıklayamaz; ancak kanunen açıklama yükümlülüğü bulunan hâller saklıdır. Yükümlülük ilişki sona erdikten sonra da sürer.",
  "Etik Kurallar - gizlilik")

q("bagimsizlik_ve_etik", "Bağımsızlık ve Etik",
  "Aşağıdakilerden hangileri bağımsızlığı zedeleyen tehditlerdendir?\n\nI. Kişisel çıkar tehdidi\n\nII. Kendi kendini denetleme tehdidi\n\nIII. Yakınlık tehdidi",
  "I, II ve III",
  ["Yalnız I", "I ve II", "II ve III", "Yalnız III"],
  "Etik Kurallar tehditleri beş grupta sayar: kişisel çıkar (I), kendi kendini denetleme (II), taraf tutma, yakınlık (III) ve yıldırma. Üçü de bağımsızlığı zedeleyen tehditlerdendir.",
  "Etik Kurallar - tehdit türleri")

# ══ RİSK DEĞERLENDİRME (6) ════════════════════════════════════════════════
q("risk_degerlendirme", "Risk Değerlendirme",
  "Denetim riskinin bileşenleri bakımından aşağıdakilerden hangisi doğrudur?",
  "Denetim riski, önemli yanlışlık riski ile tespit edememe riskinin bir fonksiyonudur",
  ["Denetim riski yalnızca denetçinin ücretine bağlı olup kanıt toplama süreciyle hiç ilgisi yoktur",
   "Denetim riski yalnızca kontrol riskinden oluşur; yapısal risk ve tespit riski dikkate alınmaz",
   "Denetim riski işletmenin iflas etme olasılığını ölçen ve finansal tablolarla ilgisi olmayan bir risktir",
   "Denetim riski her denetimde sabittir; denetçi bu riski hiçbir biçimde etkileyemez ve yönetemez"],
  "BDS 200: denetim riski, finansal tablolar önemli bir yanlışlık içerirken denetçinin uygun olmayan bir görüş vermesi riskidir ve önemli yanlışlık riski ile tespit edememe riskinin fonksiyonudur.",
  "BDS 200 - denetim riski")

q("risk_degerlendirme", "Risk Değerlendirme",
  "Yapısal (doğal) risk bakımından aşağıdakilerden hangisi doğrudur?",
  "İç kontroller dikkate alınmaksızın, bir açıklamanın niteliği gereği yanlışlığa açık olma ihtimalidir",
  ["İşletmenin iç kontrol sisteminin bir yanlışlığı önleyememesi veya tespit edememesi ihtimalini ifade eder",
   "Denetçinin uyguladığı prosedürlerin mevcut bir yanlışlığı tespit edememesi olasılığını göstermektedir",
   "Denetçinin denetim ücretini tahsil edememe riskini ifade eden ve mali nitelik taşıyan bir kavramdır",
   "Yalnızca hile hâlinde ortaya çıkan ve olağan hata olasılığını hiç kapsamayan özel bir risk türüdür"],
  "BDS 315: yapısal risk, ilgili kontroller dikkate alınmaksızın bir işlem sınıfı, hesap bakiyesi veya açıklamaya ilişkin bir yanlışlığın ortaya çıkma ihtimalidir; işlemin karmaşıklığı, tahmin içermesi gibi etkenlerden doğar.",
  "BDS 315 - yapısal risk")

q("risk_degerlendirme", "Risk Değerlendirme",
  "Kontrol riski bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmenin iç kontrol sisteminin bir yanlışlığı zamanında önleyememesi veya tespit edip düzeltememesi riskidir",
  ["Denetçinin uyguladığı denetim prosedürlerinin mevcut bir yanlışlığı bulamaması olasılığını ifade eder",
   "İç kontroller dikkate alınmaksızın bir açıklamanın niteliği gereği yanlışlığa açık olmasını ifade eder",
   "Kontrol riski denetçi tarafından belirlenir ve denetçinin çalışmasıyla doğrudan azaltılabilmektedir",
   "Kontrol riski işletmenin borçlarını ödeyememe olasılığını gösteren bir mali yapı göstergesidir"],
  "BDS 315: kontrol riski, bir yanlışlığın işletmenin iç kontrolü tarafından zamanında önlenememesi ya da tespit edilip düzeltilememesi riskidir. Yapısal risk ile birlikte önemli yanlışlık riskini oluşturur ve işletmeye aittir.",
  "BDS 315 - kontrol riski")

q("risk_degerlendirme", "Risk Değerlendirme",
  "Tespit edememe riski ile denetçinin çalışması arasındaki ilişki bakımından aşağıdakilerden hangisi doğrudur?",
  "Önemli yanlışlık riski yüksek değerlendirildiğinde denetçi, tespit edememe riskini düşürmek için daha fazla ve uygun kanıt toplar",
  ["Önemli yanlışlık riski yüksek olduğunda denetçi kanıt miktarını azaltarak denetimi hızlandırmalıdır",
   "Tespit edememe riski işletmeye ait olup denetçinin çalışmasıyla hiçbir biçimde değiştirilememektedir",
   "Tespit edememe riski her denetimde sıfırdır; denetçi tüm yanlışlıkları her hâlde bulmak zorundadır",
   "Önemli yanlışlık riski ile tespit edememe riski arasında hiçbir ilişki bulunmamaktadır"],
  "BDS 200/330: denetim riskini kabul edilebilir düzeye indirmek için denetçi, değerlendirdiği önemli yanlışlık riskiyle ters yönde tespit edememe riski belirler; risk yüksekse daha fazla, uygun ve güvenilir kanıt toplayarak tespit edememe riskini düşürür.",
  "BDS 330 - riske karşılık verme")

q("risk_degerlendirme", "Risk Değerlendirme",
  "Risk değerlendirme prosedürleri bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletmeyi ve çevresini, iç kontrolü dâhil anlamak amacıyla uygulanır; tek başına görüşe dayanak oluşturmaz",
  ["Tek başına denetim görüşüne yeterli ve uygun dayanak oluşturur; başka prosedüre gerek kalmaz",
   "Yalnızca denetim tamamlandıktan sonra uygulanan ve rapor aşamasına ait prosedürleri ifade eder",
   "Yalnızca hile tespit edildiğinde uygulanan ve olağan denetimlerde yer verilmeyen prosedürlerdir",
   "Yalnızca işletmenin vergi beyannamelerinin incelenmesinden oluşan sınırlı bir çalışmayı kapsar"],
  "BDS 315: risk değerlendirme prosedürleri işletmeyi ve çevresini (iç kontrol dâhil) anlayarak önemli yanlışlık risklerini belirlemek için uygulanır; tek başına görüşe dayanak oluşturmaz, ilave prosedürlerle desteklenir.",
  "BDS 315 - risk değerlendirme prosedürleri")

q("risk_degerlendirme", "Risk Değerlendirme",
  "Aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Önemli yanlışlık riski, yapısal risk ile kontrol riskinden oluşur\n\nII. Tespit edememe riski denetçinin çalışmasıyla yönetilir\n\nIII. Kontrol riski denetçinin belirlediği ve doğrudan azaltabildiği bir risktir",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Önemli yanlışlık riski yapısal ve kontrol riskinden oluşur (I); tespit edememe riski denetçinin prosedürleriyle yönetilir (II). Kontrol riski ise işletmenin iç kontrolüne ait olup denetçi bunu değerlendirir, doğrudan azaltamaz; bu nedenle III yanlıştır.",
  "BDS 200, 315 - risk bileşenleri")

# ══ DENETİM KANITI (7) ════════════════════════════════════════════════════
q("denetim_kaniti", "Denetim Kanıtı",
  "Denetim kanıtının niteliği bakımından aşağıdakilerden hangisi doğrudur?",
  "Kanıtın yeterli (miktar) ve uygun (kalite: ilgililik ve güvenilirlik) olması gerekir",
  ["Yalnızca kanıtın miktarı önemlidir; kanıtın güvenilirliği ve ilgililiği hiç değerlendirilmez",
   "Yalnızca kanıtın kalitesi önemlidir; toplanan kanıtın miktarının hiçbir önemi bulunmamaktadır",
   "Kanıtın niteliği denetçinin takdirine bırakılmamış olup her denetimde sabit sayıda kanıt aranır",
   "Denetim kanıtı yalnızca yönetimin yazılı beyanlarından oluşur; başka kanıt türü kabul edilmez"],
  "BDS 500: denetçi, görüşüne dayanak oluşturacak yeterli ve uygun denetim kanıtı elde etmelidir. Yeterlilik kanıtın miktarını, uygunluk ise kalitesini (ilgililik ve güvenilirlik) ifade eder.",
  "BDS 500 - yeterli ve uygun kanıt", "easy")

q("denetim_kaniti", "Denetim Kanıtı",
  "Denetim kanıtının güvenilirliği bakımından aşağıdakilerden hangisi doğrudur?",
  "İşletme dışı bağımsız kaynaklardan elde edilen kanıt, işletme içi kaynaklardan elde edilene göre daha güvenilirdir",
  ["İşletme içinden elde edilen kanıt, dış bağımsız kaynaklardan elde edilene göre her hâlde daha güvenilirdir",
   "Kanıtın kaynağı güvenilirliği hiç etkilemez; tüm kanıtlar eşit güvenilirlikte kabul edilmektedir",
   "Sözlü olarak alınan beyanlar, yazılı belgelere göre daha güvenilir kanıt olarak değerlendirilir",
   "Fotokopi belgeler asıllarına göre daha güvenilir sayılır; asıl belgeler kanıt olarak kullanılmaz"],
  "BDS 500: kanıtın güvenilirliği kaynağına ve niteliğine bağlıdır. Dış bağımsız kaynaklardan elde edilen, denetçinin doğrudan elde ettiği, yazılı ve asıl nüsha olan kanıtlar daha güvenilirdir.",
  "BDS 500 - kanıtın güvenilirliği")

q("denetim_kaniti", "Denetim Kanıtı",
  "Dış teyit (doğrulama) prosedürü bakımından aşağıdakilerden hangisi doğrudur?",
  "Denetçinin üçüncü taraftan doğrudan yazılı cevap alarak elde ettiği kanıttır",
  ["Denetçinin işletme personeline sözlü soru sorarak elde ettiği ve teyit sayılan bir kanıt türüdür",
   "Denetçinin işletmenin kendi kayıtlarını yeniden hesaplayarak elde ettiği bir doğrulama işlemidir",
   "İşletmenin üçüncü taraftan alıp denetçiye ilettiği belgelerden oluşan dolaylı bir kanıt türüdür",
   "Denetçinin işletmenin fiziki sayımını gözlemleyerek elde ettiği ve dış teyit sayılan bir kanıttır"],
  "BDS 505: dış teyit, denetçinin üçüncü bir taraftan (banka, müşteri, satıcı) yazılı olarak ve doğrudan elde ettiği kanıttır. Kanıtın işletme üzerinden dolaşmaması güvenilirliğini artırır.",
  "BDS 505 - dış teyit")

q("denetim_kaniti", "Denetim Kanıtı",
  "Analitik prosedürler bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal veriler arasındaki makul ilişkilerin incelenmesi yoluyla finansal bilgilerin değerlendirilmesidir",
  ["Yalnızca her bir belgenin tek tek ve ayrıntılı olarak incelenmesinden oluşan bir kanıt tekniğidir",
   "Yalnızca stok sayımının fiziki olarak gözlemlenmesini ifade eden bir denetim prosedürüdür",
   "Yalnızca yönetimden yazılı beyan alınmasını ifade eden ve veri analizi içermeyen bir tekniktir",
   "Yalnızca denetim sonunda rapor yazılırken uygulanan ve kanıt niteliği taşımayan bir işlemdir"],
  "BDS 520: analitik prosedürler, finansal ve finansal olmayan veriler arasındaki makul ilişkilerin değerlendirilmesi yoluyla finansal bilgilerin incelenmesidir; beklenen değerlerden önemli sapmalar araştırılır.",
  "BDS 520 - analitik prosedürler")

q("denetim_kaniti", "Denetim Kanıtı",
  "Yönetimin yazılı beyanları bakımından aşağıdakilerden hangisi doğrudur?",
  "Denetim kanıtı sayılır; ancak tek başına yeterli ve uygun kanıt oluşturmaz",
  ["Tek başına yeterli ve uygun kanıt oluşturur; başka kanıt toplanmasına gerek bırakmamaktadır",
   "Denetim kanıtı sayılmaz; hiçbir denetim değeri bulunmayan biçimsel bir belgedir",
   "Yalnızca hile tespit edildiğinde alınır; olağan denetimlerde yazılı beyan aranmamaktadır",
   "Yönetimin yazılı beyanı denetçinin sorumluluğunu tümüyle ortadan kaldıran bir belgedir"],
  "BDS 580: yazılı beyanlar gerekli denetim kanıtıdır; ancak tek başına ilgili konular hakkında yeterli ve uygun kanıt oluşturmaz ve denetçinin diğer kanıtları toplama sorumluluğunu ortadan kaldırmaz.",
  "BDS 580 - yazılı beyanlar")

q("denetim_kaniti", "Denetim Kanıtı",
  "Stok sayımının gözlemlenmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Stokların varlığı ve durumu hakkında kanıt sağlar; gözlem denetçinin doğrudan elde ettiği bir kanıttır",
  ["Stokların değerleme doğruluğu hakkında tek başına tam bir kanıt sağlar; başka prosedüre gerek yoktur",
   "Yalnızca işletmenin borçlarının varlığı hakkında kanıt sağlar; stoklarla doğrudan ilgisi bulunmaz",
   "Gözlem bir denetim prosedürü değildir; denetçi yalnızca kayıtları inceleyerek kanıt toplayabilir",
   "Stok sayımının gözlemlenmesi yalnızca hile şüphesi bulunan işletmelerde zorunlu tutulmaktadır"],
  "BDS 501: stoklar finansal tablolar açısından önemliyse denetçi, fiziki stok sayımına katılarak stokların varlığı ve durumu hakkında kanıt elde eder. Gözlem doğrudan elde edilen kanıt olduğundan güvenilirdir; ancak değerleme için ayrıca prosedür gerekir.",
  "BDS 501 - stok sayımının gözlemlenmesi")

q("denetim_kaniti", "Denetim Kanıtı",
  "Aşağıdaki kanıtlardan hangileri güvenilirlik bakımından daha üstün kabul edilir?\n\nI. Dış bağımsız kaynaktan doğrudan alınan yazılı teyit\n\nII. Denetçinin bizzat gözlemleyerek elde ettiği kanıt\n\nIII. İşletme personelinden sözlü olarak alınan beyan",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "BDS 500: dış bağımsız kaynaktan doğrudan alınan yazılı teyit (I) ve denetçinin bizzat elde ettiği kanıt (II) güvenilirlik sıralamasında üsttedir. İşletme içinden alınan sözlü beyan (III) ise en zayıf kanıtlardandır.",
  "BDS 500 - kanıt güvenilirlik sıralaması")

# ══ HİLE (6) ══════════════════════════════════════════════════════════════
q("hile", "Hile ve Denetçinin Sorumluluğu",
  "Hile ile hata arasındaki temel fark bakımından aşağıdakilerden hangisi doğrudur?",
  "Hilede kasıt bulunur; hata ise kasıt içermeyen istem dışı yanlışlıktır",
  ["Hatada kasıt bulunur; hile ise kasıt içermeyen ve istem dışı gerçekleşen bir yanlışlıktır",
   "İkisi arasında hiçbir fark yoktur; standartlar hile ile hatayı eş anlamlı olarak kullanmaktadır",
   "Fark yalnızca tutarın büyüklüğündedir; büyük yanlışlıklar hile, küçükler hata olarak nitelenir",
   "Hile yalnızca yönetim tarafından, hata ise yalnızca çalışanlar tarafından yapılabilen fiillerdir"],
  "BDS 240: hile ile hatayı ayıran temel unsur, finansal tablolardaki yanlışlığa yol açan fiilin kasıtlı olup olmadığıdır. Hile kasıtlıdır, hata kasıt içermez.",
  "BDS 240 - hile/hata ayrımı", "easy")

q("hile", "Hile ve Denetçinin Sorumluluğu",
  "Hilenin önlenmesi ve tespitinden birincil sorumluluk bakımından aşağıdakilerden hangisi doğrudur?",
  "Hilenin önlenmesi ve tespitinden birincil sorumluluk üst yönetimden sorumlu olanlar ile yönetime aittir",
  ["Hilenin önlenmesi ve tespitinden birincil sorumluluk bağımsız denetçiye ait bulunmaktadır",
   "Hilenin önlenmesinden hiç kimse sorumlu değildir; hile kaçınılmaz bir işletme riski sayılır",
   "Hilenin önlenmesi sorumluluğu yalnızca işletmenin bağlı olduğu meslek odasına ait bulunmaktadır",
   "Hilenin tespitinden yalnızca vergi idaresi sorumlu olup işletme yönetiminin bir görevi yoktur"],
  "BDS 240: hilenin önlenmesi ve tespit edilmesine ilişkin birincil sorumluluk üst yönetimden sorumlu olanlar ile yönetimdedir. Denetçi ise hileden kaynaklanan önemli yanlışlıklar konusunda makul güvence elde etmekle sorumludur.",
  "BDS 240 - hilede sorumluluk")

q("hile", "Hile ve Denetçinin Sorumluluğu",
  "Denetçinin hileye ilişkin sorumluluğu bakımından aşağıdakilerden hangisi doğrudur?",
  "Finansal tabloların hileden kaynaklanan önemli yanlışlık içermediğine dair makul güvence elde etmekle sorumludur",
  ["Her türlü hileyi mutlak biçimde tespit etmekle ve hiçbirini kaçırmamakla yükümlü tutulmuştur",
   "Hile denetçiyi hiç ilgilendirmez; denetçinin hileye ilişkin hiçbir sorumluluğu bulunmamaktadır",
   "Denetçi yalnızca hileyi işleyen kişiyi tespit edip cezalandırmakla görevlendirilmiş bulunmaktadır",
   "Denetçi hile bulursa raporunu yazmaktan kaçınır ve konuyu hiçbir mercie bildirmeksizin ayrılır"],
  "BDS 240: denetçi, finansal tabloların hile veya hatadan kaynaklanan önemli yanlışlık içerip içermediği konusunda makul güvence elde etmekle sorumludur. Denetimin doğasındaki kısıtlar nedeniyle mutlak güvence sağlanamaz; özellikle gizlenmiş hilelerde tespit riski daha yüksektir.",
  "BDS 240 - denetçinin sorumluluğu")

q("hile", "Hile ve Denetçinin Sorumluluğu",
  "Hile üçgeni bakımından aşağıdakilerden hangisi doğrudur?",
  "Baskı (teşvik), fırsat ve haklı gösterme (rasyonelleştirme) unsurlarından oluşur",
  ["Yalnızca fırsat unsurundan oluşur; baskı ve haklı gösterme hile için gerekli görülmemektedir",
   "Denetim riski, kontrol riski ve tespit edememe riski unsurlarından oluşan bir modeldir",
   "Yeterlilik, uygunluk ve güvenilirlik unsurlarından oluşan bir kanıt değerlendirme modelidir",
   "Dürüstlük, tarafsızlık ve gizlilik unsurlarından oluşan bir mesleki etik çerçevesidir"],
  "BDS 240: hile riski etkenleri genellikle baskı/teşvik, fırsat ve haklı gösterme (hile üçgeni) unsurlarıyla açıklanır; bu unsurların varlığı hile riskinin göstergesidir.",
  "BDS 240 - hile üçgeni")

q("hile", "Hile ve Denetçinin Sorumluluğu",
  "Hileli finansal raporlama ile varlıkların kötüye kullanılması ayrımı bakımından aşağıdakilerden hangisi doğrudur?",
  "Hileli finansal raporlama tabloların kasten yanıltıcı sunulmasıdır; varlıkların kötüye kullanılması ise işletme varlıklarının çalınmasıdır",
  ["Hileli finansal raporlama varlıkların çalınmasını, varlıkların kötüye kullanılması ise tabloların yanıltıcı sunulmasını ifade eder",
   "İkisi arasında hiçbir fark bulunmayıp standartlarda eş anlamlı kavramlar olarak kullanılmaktadır",
   "Hileli finansal raporlama yalnızca çalışanlarca, varlıkların kötüye kullanılması yalnızca yönetimce yapılır",
   "İki kavram da hile değil hata kapsamında değerlendirilir; kasıt unsuru hiçbirinde aranmamaktadır"],
  "BDS 240: denetçiyi ilgilendiren iki tür kasıtlı yanlışlık vardır: hileli finansal raporlama (tabloların kasten yanıltıcı hazırlanması) ve varlıkların kötüye kullanılması (işletme varlıklarının çalınması).",
  "BDS 240 - hile türleri")

q("hile", "Hile ve Denetçinin Sorumluluğu",
  "Aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Hile ile hatayı ayıran unsur kasıttır\n\nII. Hilenin önlenmesinden birincil sorumluluk yönetimdedir\n\nIII. Denetçi her türlü hileyi mutlak biçimde tespit etmekle yükümlüdür",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Hile ile hatayı ayıran unsur kasıttır (I) ve hileyi önleme sorumluluğu birincil olarak yönetimdedir (II). Denetçi ise mutlak değil makul güvence sağlar; bu nedenle III yanlıştır.",
  "BDS 240 - hile temel ilkeler")

# ══ ÖNEMLİLİK VE ÖRNEKLEME (6) ════════════════════════════════════════════
q("onemlilik_ve_ornekleme", "Önemlilik ve Örnekleme",
  "Önemlilik kavramı bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir yanlışlığın, kullanıcıların finansal tablolara dayanarak alacağı ekonomik kararları etkilemesi bekleniyorsa o yanlışlık önemlidir",
  ["Önemlilik yalnızca tutarın büyüklüğüne bakılarak belirlenir; niteliksel etkenler hiç dikkate alınmaz",
   "Önemlilik her denetimde kanunla belirlenmiş sabit bir tutar olup denetçinin takdirine bırakılmamıştır",
   "Önemlilik yalnızca denetim tamamlandıktan sonra belirlenir; planlama aşamasında hiç kullanılmaz",
   "Önemlilik işletmenin kâr etme olasılığını ölçen ve yanlışlıklarla ilgisi bulunmayan bir kavramdır"],
  "BDS 320: yanlışlıklar, tek başına veya toplu olarak finansal tablo kullanıcılarının bu tablolara dayanarak alacakları ekonomik kararları etkilemesi makul ölçüde bekleniyorsa önemli kabul edilir. Önemlilik mesleki muhakemeyle belirlenir ve niteliksel etkenleri de içerir.",
  "BDS 320 - önemlilik")

q("onemlilik_ve_ornekleme", "Önemlilik ve Örnekleme",
  "Performans önemliliği bakımından aşağıdakilerden hangisi doğrudur?",
  "Yanlışlıkların toplamının önemliliği aşma olasılığını düşürmek için önemlilikten daha düşük belirlenen tutardır",
  ["Finansal tablolar bütünü için belirlenen önemlilikle tümüyle aynı tutar olup ondan hiç farklı değildir",
   "Önemlilikten daha yüksek belirlenen ve denetçinin daha az kanıt toplamasını sağlayan bir tutardır",
   "Yalnızca denetim raporunda açıklanan ve denetim çalışmasında hiç kullanılmayan bir gösterge tutardır",
   "İşletmenin performansını ölçmek için kullanılan ve yanlışlıklarla ilgisi bulunmayan bir ölçüttür"],
  "BDS 320: performans önemliliği, düzeltilmemiş ve tespit edilmemiş yanlışlıkların toplamının finansal tablolar bütünü için belirlenen önemliliği aşma olasılığını uygun biçimde düşük bir düzeye indirmek amacıyla önemlilikten daha düşük olarak belirlenen tutardır.",
  "BDS 320 - performans önemliliği")

q("onemlilik_ve_ornekleme", "Önemlilik ve Örnekleme",
  "Denetimde örnekleme bakımından aşağıdakilerden hangisi doğrudur?",
  "Bir kitle içindeki birimlerin tamamından azına prosedür uygulanarak kitlenin tamamı hakkında sonuç çıkarılmasıdır",
  ["Kitledeki tüm birimlerin istisnasız incelenmesini ifade eden ve seçim içermeyen bir yöntemdir",
   "Yalnızca tutarı en büyük olan tek bir işlemin incelenmesinden oluşan sınırlı bir inceleme türüdür",
   "Denetçinin hiçbir prosedür uygulamadan yönetimin beyanına dayanarak sonuç çıkarmasını ifade eder",
   "Yalnızca hile şüphesi bulunan denetimlerde kullanılabilen ve olağan denetimde yasak olan bir tekniktir"],
  "BDS 530: denetimde örnekleme, denetim prosedürlerinin bir kitle içindeki birimlerin tamamından azına uygulanmasıdır; amaç, seçilen örneklem üzerinden kitlenin tamamı hakkında sonuç çıkarmaktır.",
  "BDS 530 - örnekleme")

q("onemlilik_ve_ornekleme", "Önemlilik ve Örnekleme",
  "Örnekleme riski bakımından aşağıdakilerden hangisi doğrudur?",
  "Örneklemden ulaşılan sonucun, kitlenin tamamına aynı prosedür uygulansaydı ulaşılacak sonuçtan farklı olması riskidir",
  ["Denetçinin örneklem dışındaki nedenlerle yanlış sonuca ulaşması riskini ifade eden bir kavramdır",
   "Örnekleme riski hiçbir zaman doğmaz; örneklem her hâlde kitleyi kusursuz biçimde temsil etmektedir",
   "Yalnızca istatistiki olmayan örneklemede doğar; istatistiki örneklemede bu risk tümüyle ortadan kalkar",
   "Örneklem büyüklüğü artırıldıkça örnekleme riski de artar; bu nedenle küçük örneklem tercih edilir"],
  "BDS 530: örnekleme riski, örnekleme dayanılarak ulaşılan sonucun, kitlenin tamamına aynı prosedür uygulanması hâlinde ulaşılacak sonuçtan farklı olması riskidir. Örneklem büyüklüğü artırılarak azaltılabilir.",
  "BDS 530 - örnekleme riski")

q("onemlilik_ve_ornekleme", "Önemlilik ve Örnekleme",
  "Önemliliğin denetim boyunca gözden geçirilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Denetim sırasında yeni bilgiler edinildiğinde önemlilik gözden geçirilir ve gerekirse revize edilir",
  ["Önemlilik planlama aşamasında bir kez belirlenir ve hiçbir koşulda değiştirilemez duruma gelir",
   "Önemlilik yalnızca denetim tamamlandıktan sonra belirlenir; planlamada hiç kullanılmamaktadır",
   "Önemlilik her yıl kanunla ilan edilir; denetçinin bu tutarı değiştirme yetkisi bulunmamaktadır",
   "Önemliliğin revize edilmesi denetim raporunun geçersiz sayılması sonucunu doğurmaktadır"],
  "BDS 320: denetçi, denetim sırasında başlangıçta belirlediği önemliliğin farklı bir tutar olması gerektiğine işaret eden bilgiler edinirse önemliliği revize eder; bu, uygulanacak prosedürlerin niteliğini ve kapsamını etkiler.",
  "BDS 320 - önemliliğin revizyonu")

q("onemlilik_ve_ornekleme", "Önemlilik ve Örnekleme",
  "Aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Önemlilik yalnızca niceliksel (tutar) etkenlere göre belirlenir\n\nII. Performans önemliliği, önemlilikten daha düşük belirlenir\n\nIII. Örnekleme riski örneklem büyüklüğü artırılarak azaltılabilir",
  "II ve III",
  ["I, II ve III", "Yalnız I", "I ve II", "Yalnız III"],
  "Performans önemliliği önemlilikten düşüktür (II) ve örnekleme riski örneklem büyütülerek azaltılır (III). Önemlilik ise yalnız tutara değil, niteliksel etkenlere de (mevzuata aykırılık, ilişkili taraf işlemi gibi) göre belirlenir; bu nedenle I yanlıştır.",
  "BDS 320, 530 - önemlilik ve örnekleme")

# ══ DENETÇİ RAPORU (4) ════════════════════════════════════════════════════
q("denetci_raporu", "Denetçi Raporu ve Görüşler",
  "Olumsuz görüş verilmesi bakımından aşağıdakilerden hangisi doğrudur?",
  "Yeterli ve uygun kanıt elde edilmiş, yanlışlıklar hem önemli hem de yaygın ise olumsuz görüş verilir",
  ["Denetçi yeterli kanıt elde edememişse ve kapsam sınırlaması yaygınsa olumsuz görüş verilmektedir",
   "Yanlışlık önemli ancak yaygın değilse olumsuz görüş verilir; yaygınlık olumsuz görüşü engeller",
   "Finansal tablolar çerçeveye tümüyle uygunsa denetçi teşekkür amacıyla olumsuz görüş vermektedir",
   "Olumsuz görüş yalnızca işletme zarar ettiğinde verilen ve yanlışlıkla ilgisi bulunmayan bir görüştür"],
  "BDS 705: denetçi yeterli ve uygun kanıt elde etmiş ve yanlışlıkların finansal tablolar açısından hem önemli hem de yaygın olduğu sonucuna varmışsa olumsuz görüş verir. Kanıt elde edilememesi hâlinde ise görüş vermekten kaçınılır.",
  "BDS 705 - olumsuz görüş")

q("denetci_raporu", "Denetçi Raporu ve Görüşler",
  "Görüş vermekten kaçınma bakımından aşağıdakilerden hangisi doğrudur?",
  "Denetçi yeterli ve uygun kanıt elde edemediğinde ve olası etkiler hem önemli hem yaygın olduğunda görüş vermekten kaçınır",
  ["Denetçi yeterli kanıt elde etmiş ancak yanlışlık bulmuşsa görüş vermekten kaçınmak zorundadır",
   "Görüş vermekten kaçınma, finansal tabloların tümüyle doğru olduğunun bir başka ifade biçimidir",
   "Denetçi görüş vermekten kaçındığında rapor düzenlemez ve müşteriye hiçbir bildirimde bulunmaz",
   "Görüş vermekten kaçınma yalnızca denetim ücreti ödenmediğinde başvurulan bir yaptırım yoludur"],
  "BDS 705: denetçi yeterli ve uygun denetim kanıtı elde edemediğinde ve tespit edilmemiş olası yanlışlıkların etkilerinin hem önemli hem yaygın olabileceği sonucuna vardığında görüş vermekten kaçınır.",
  "BDS 705 - görüş vermekten kaçınma")

q("denetci_raporu", "Denetçi Raporu ve Görüşler",
  "Kilit denetim konuları bakımından aşağıdakilerden hangisi doğrudur?",
  "Denetçinin mesleki muhakemesine göre cari dönem denetiminde en çok önem arz eden konulardır ve görüşü değiştirmez",
  ["Kilit denetim konuları denetçi görüşünü kendiliğinden olumlu görüşten sınırlı olumluya dönüştürür",
   "Kilit denetim konuları işletmenin ticari sırlarını ifşa ettiğinden hiçbir raporda yer alamaz",
   "Kilit denetim konuları yalnızca denetçinin tespit ettiği hileleri açıkladığı bir bölümü ifade eder",
   "Kilit denetim konuları yönetim tarafından belirlenir ve denetçinin bu konuda takdiri bulunmaz"],
  "BDS 701: kilit denetim konuları, denetçinin mesleki muhakemesine göre cari döneme ait finansal tabloların denetiminde en çok önem arz eden konulardır. Bunların bildirilmesi görüşün yerine geçmez ve görüşü değiştirmez.",
  "BDS 701 - kilit denetim konuları")

q("denetci_raporu", "Denetçi Raporu ve Görüşler",
  "Aşağıdaki ifadelerden hangileri denetçi raporu bakımından doğrudur?\n\nI. Yanlışlık önemli ancak yaygın değilse sınırlı olumlu görüş verilir\n\nII. Kanıt elde edilememesi ve etkinin yaygın olması hâlinde görüş vermekten kaçınılır\n\nIII. Kilit denetim konularının bildirilmesi görüşün yerine geçer",
  "I ve II",
  ["I, II ve III", "Yalnız I", "II ve III", "Yalnız III"],
  "Önemli ancak yaygın olmayan yanlışlıkta sınırlı olumlu görüş verilir (I); kanıt elde edilemiyorsa ve etki yaygınsa görüş vermekten kaçınılır (II). Kilit denetim konuları ise görüşün yerine geçmez, onu değiştirmez; bu nedenle III yanlıştır.",
  "BDS 701, 705 - görüş türleri")

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
        ch = {ans: it["correct"]}
        for k, d in zip([k for k in "ABCDE" if k != ans], it["distractors"]):
            ch[k] = d
        assert len(set(ch.values())) == 5, f"{prefix}-{i+1}: şık tekrarı"
        out.append({
            "id": f"{prefix}-{i+1:04d}", "lessonId": L, "topicId": it["topic"],
            "question": it["stem"], "choices": ch, "correctAnswer": ans,
            "explanation": it["why"],
            "source": {"kind": "generated", "styleRef": "2026/1 test biçimi",
                       "legislationRef": it["ref"]},
            "tags": ["Demo Soru", "2026 Formatı", it["label"]],
            "difficulty": it["difficulty"], "updatedAt": "2026-07-15T00:00:00Z",
            "examPeriod": "2026/1 formatına uyumlu", "legislationVersion": "TDS 2026 Seti",
            "sourceUpdatedAt": "2026-07-15T00:00:00Z", "isPremium": False, "isActive": True,
        })
    return out

if __name__ == "__main__":
    assert len(Q) == 40, f"40 olmalı, şu an {len(Q)}"
    MARK = re.compile(r"(?m)^\s*(IV|I{1,3}|V)[\.\)]\s")
    onc = [x for x in Q if len(MARK.findall(x["stem"])) >= 2]
    duz = [x for x in Q if len(MARK.findall(x["stem"])) < 2]
    t2 = [x for i, x in enumerate(duz) if i % 2 == 0] + [x for i, x in enumerate(onc) if i % 2 == 0]
    t3 = [x for i, x in enumerate(duz) if i % 2 == 1] + [x for i, x in enumerate(onc) if i % 2 == 1]
    print(f"öncüllü {len(onc)} → t2:{len([x for x in t2 if x in onc])} t3:{len([x for x in t3 if x in onc])}")
    APP = "/Users/hasanyavuz/Desktop/projects/smmm_sgs_pratik/assets/content/yeterlilik"
    for items, name, prefix, seed in ((t2, "questions_muhasebe_denetimi_test2_2026.json", "den-t2", 20260807),
                                      (t3, "questions_muhasebe_denetimi_test3_2026.json", "den-t3", 20260808)):
        data = emit(items, prefix, seed)
        json.dump(data, open(f"{APP}/{name}", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"{name}: {len(data)} soru | harf {''.join(x['correctAnswer'] for x in data)}")
