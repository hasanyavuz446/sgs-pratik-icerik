#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM Hukuk — Borcun İfası konu havuzu (3×20).

Dayanak, 17.07.2026 tarihinde mevzuat.gov.tr'den alınan güncel 6098 sayılı
TBK m.83–126 metnidir. Paket ifa, muacceliyet, alacaklı ve borçlu temerrüdü
ile sözleşmeye aykırılığın sonuçlarını birlikte kapsar.
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
        "Borçlu, kişisel becerisinin önem taşımadığı bir teslim borcunu çalışanı aracılığıyla yerine getirmiştir. Alacaklı sırf ifayı borçlunun yapmadığı gerekçesiyle kabulden kaçınmıştır. Hangisi doğrudur?",
        "Borcun borçlu tarafından şahsen ifası hangi durumda zorunludur?",
        "Alacaklının borçlunun şahsen ifasında menfaati varsa şahsen ifa gerekir",
        ["Her borç yalnız borçlunun kendisi tarafından ve hiçbir yardımcı kullanılmadan ifa edilir", "Şahsen ifa hiçbir borçta aranmaz", "Üçüncü kişinin ifası borcu her durumda iki katına çıkararak devam ettirir", "Alacaklının menfaati bulunsa bile borçlu daima ilgisiz bir kişiyi gönderebilir"],
        "TBK m.83'e göre alacaklının borcun bizzat borçlu tarafından ifasında menfaati yoksa borçlu şahsen ifayla yükümlü değildir.",
        "Şahsen ifa istisnadır ve edimin niteliğiyle alacaklının menfaatine bağlıdır. Kişisel yetenek veya güven önem taşıyorsa borçlu edimi başkasına bırakamaz.",
        "6098 sayılı TBK m.83", "easy",
    ),
    r(
        "Tamamı belli ve muaccel 100.000 TL borcun 30.000 TL'si önerilmiş; alacaklı kısmi ödemeyi kabul etmemiştir. Taraflar aksini kararlaştırmamıştır. Sonuç nedir?",
        "Tamamı belli ve muaccel bir borçta alacaklının kısmen ifayı reddetme yetkisi nasıldır?",
        "Alacaklı kısmen ifayı reddedebilir; kabul ederse ikrar edilen kısım ifa edilmelidir",
        ["Alacaklı her kısmi ifayı kabul etmek ve kalan borcu bağışlamak zorundadır", "Kısmi ifa önerisi borcun tamamını kendiliğinden sona erdiren bir ödeme sayılır", "Borçlu dilediği miktarı önerince alacaklının bütün teminatları hükümsüz olur", "Kısmi ifanın reddi yalnız borcun vadesinden on yıl sonra mümkün hâle gelir"],
        "TBK m.84 tamamı belli ve muaccel borçta alacaklıya kısmen ifayı reddetme hakkı verir. Kabul hâlinde borçlu ikrar ettiği kısmı ifadan kaçınamaz.",
        "Kısmi ifayı kabul zorunluluğu yoktur. Bununla birlikte alacaklı kabul etmişse borçlu artık kabul edilen ve ikrar olunan kısmı ödemekten kaçınamaz.",
        "6098 sayılı TBK m.84", "medium",
    ),
    r(
        "Bölünemeyen tek bir tablonun teslimi borcunda üç alacaklı bulunmaktadır. Alacaklılardan biri tablonun yalnız kendisine verilmesini istemiştir. Kanuni düzenleme bakımından hangisi doğrudur?",
        "Bölünemeyen borcun birden çok alacaklısı varsa ifa talebi ve ifa kime yönelir?",
        "Her alacaklı tamamına ifayı isteyebilir; edim alacaklıların hepsine birlikte ifa edilir",
        ["Her alacaklı bölünemeyen edimin yalnız hayalî üçte bir parçasını isteyebilir", "Borçlu edimi rastgele seçtiği tek alacaklıya vererek kesin olarak kurtulur", "Alacaklı çokluğu bölünemeyen borcu kendiliğinden geçersiz ve imkânsız kılar", "Edim sadece en genç alacaklıya ifa edilir ve diğerlerinin hakkı sona erer"],
        "TBK m.85 uyarınca her alacaklı borcun alacaklıların tamamına ifasını isteyebilir; borçlu edimi hepsine birden ifa etmek zorundadır.",
        "Bölünemeyen edim paylaştırılamadığı için talep bütün alacaklılar yararına kullanılır. Çok borçlu varsa her biri edimin tamamından sorumludur.",
        "6098 sayılı TBK m.85", "medium",
    ),
    r(
        "Sözleşme yalnız cinsiyle belirlenen 100 birim ürünün teslimini öngörmekte ve kaliteyi ayrıca düzenlememektedir. Borçlu en düşük kaliteli ürünleri seçmiştir. Hangisi doğrudur?",
        "Çeşit borcunda seçim borçluya aitse seçilen edimin asgari niteliği nasıl belirlenir?",
        "Borçlu seçim yapabilir fakat ortalama nitelikten daha düşük edim seçemez",
        ["Borçlu yalnız piyasadaki en düşük nitelikli ürünü seçmekle yükümlüdür", "Çeşit borcunda seçim mutlaka alacaklıya aittir ve değiştirilemez", "Ortalama nitelik ölçütü yalnız para borçlarında ve faizde uygulanabilir", "Cins belirlenmişse borcun konusu seçim yapılmadan kendiliğinden yok olur"],
        "TBK m.86'ya göre aksi anlaşılmadıkça çeşit borcunda seçim borçluya aittir; ancak edim ortalama nitelikten düşük olamaz.",
        "Seçim yetkisi borçluya kalitesiz edim sunma serbestisi vermez. İlişki veya işin özelliği seçimi başka tarafa da bırakabilir.",
        "6098 sayılı TBK m.86", "easy",
    ),
    r(
        "Taraflar ifa yerini kararlaştırmamıştır. Borcun konusu bir miktar paradır. Ödeme zamanı geldiğinde alacaklının yerleşim yeri İzmir'dir. Kural olarak ifa yeri neresidir?",
        "Aksine anlaşma yoksa para borçlarının kanuni ifa yeri neresidir?",
        "Para borcu alacaklının ödeme zamanındaki yerleşim yerinde ifa edilir",
        ["Para borcu yalnız sözleşmenin imzalandığı noterliğin bulunduğu yerde ifa edilir", "Para borcu borç konusu paranın basıldığı ülkedeki merkez bankasında ifa edilir", "Para borcunda ifa yeri daima borçlunun doğduğu yer ve aile konutudur", "Para borcu alacaklının önceki bütün yerleşim yerlerinde ayrı ayrı ödenir"],
        "TBK m.89, aksine anlaşma yoksa para borcunu alacaklının ödeme zamanındaki yerleşim yerinde ifa ettirir.",
        "Para borcu götürülecek borçtur. Alacaklının sonradan yer değiştirmesi ifayı önemli ölçüde güçleştirirse önceki yerleşim yerinde ifa imkânı doğabilir.",
        "6098 sayılı TBK m.89", "easy",
    ),
    r(
        "Taraflar, sözleşme kurulurken Ankara'daki depoda bulunan belirli makinenin teslimini kararlaştırmış fakat ifa yerini yazmamıştır. Makine borcu nerede ifa edilir?",
        "Aksine anlaşma yoksa parça borcu ve diğer borçlar için kanuni ifa yeri nasıl ayrılır?",
        "Parça borcu şeyin sözleşme kurulurken bulunduğu yerde ifa edilir",
        ["Parça borcu alacaklının evinde ifa edilir", "Belirli şey yalnız üreticinin daha sonra seçeceği yabancı ülkede teslim edilir", "Parça borcunun ifa yeri borç doğduktan sonra rastgele kura ile belirlenir", "Belirli şey borcu ifa yeri yazılmadığı için kendiliğinden hükümsüz olur"],
        "TBK m.89 belirli bir şeye ilişkin parça borcunu sözleşme kurulurken şeyin bulunduğu yerde ifa ettirir. Diğer borçlarda doğum anındaki borçlu yerleşim yeri esastır.",
        "Parça borcunda başlangıçtaki somut konum, diğer borçlarda borçlunun borç doğarken bulunduğu yerleşim yeri kanuni ölçüttür.",
        "6098 sayılı TBK m.89", "medium",
    ),
    r(
        "Bir borcun ifa zamanı ne sözleşmede kararlaştırılmış ne de ilişkinin özelliğinden anlaşılmaktadır. Alacaklı borç doğar doğmaz ifa istemiştir. Hangisi doğrudur?",
        "İfa zamanı kararlaştırılmamış ve ilişkinin özelliğinden de anlaşılmıyorsa borç ne zaman muaccel olur?",
        "Borç doğduğu anda muaccel olur",
        ["Vadesiz borç muaccel olmaz", "Vade yoksa alacaklının ifa istemesi sonsuza kadar kesin olarak yasaktır", "Borç yalnız borçlunun dilediği bir tarihte tek taraflı bildirimle doğar", "İfa zamanı yazılmadığında borç ilişkisi geçmişe etkili olarak yok sayılır"],
        "TBK m.90, tarafların anlaşması veya ilişkinin özelliği başka bir zaman göstermiyorsa her borcu doğumu anında muaccel kılar.",
        "Vade kararlaştırılmaması borcu ertelenmiş hâle getirmez. Muacceliyet doğumla birlikte gerçekleşir; temerrüdün diğer koşulları ayrıca değerlendirilir.",
        "6098 sayılı TBK m.90", "easy",
    ),
    r(
        "Sözleşmeden başlayan sekiz günlük sürenin hesabında borçlu bunu bir hafta olarak kabul etmiş ve yedinci günün sonunda sürenin dolduğunu savunmuştur. Hangisi doğrudur?",
        "TBK'ya göre 'sekiz gün' veya 'on beş gün' olarak belirlenen süre nasıl anlaşılır?",
        "Sekiz veya on beş gün ifadesi tam gün sayısını belirtir; hafta anlamına gelmez",
        ["Sekiz gün her durumda bir hafta, on beş gün de kesin olarak iki hafta demektir", "Günle belirlenen sürede sözleşmenin kurulduğu gün daima birinci gün sayılır", "On beş gün ifadesi yalnız takvim ayının son iş gününü ifade eder", "Günle belirlenen süre sadece borçlunun sözlü tahminine göre hesaplanır"],
        "TBK m.92, sekiz ve on beş günü bir veya iki hafta değil tam sekiz ve on beş gün sayar; sözleşmenin kurulduğu gün hesaba katılmaz.",
        "Gün sayısı ile hafta kavramı eşitlenmez. Süre başlangıç günü dışarıda bırakılarak son günün sonunda tamamlanır.",
        "6098 sayılı TBK m.92", "medium",
    ),
    r(
        "İfa süresinin son günü kanunen tatil kabul edilen bir güne rastlamıştır. Taraflar bunun aksini kararlaştırmamıştır. Vade bakımından sonuç nedir?",
        "İfa zamanı veya sürenin son günü kanuni tatile rastlarsa süre nasıl tamamlanır?",
        "Vade kendiliğinden tatili izleyen ilk tatil olmayan güne geçer",
        ["Tatil günü vade değişmez", "Tatil günü borcu kesin olarak sona erdirir ve ifayı tamamen gereksiz kılar", "Süre yalnız alacaklının tek taraflı seçtiği bir ayın sonuna kadar uzar", "Kanuni tatilin vadeye hiçbir etkisi olamaz ve aksine anlaşma da yasaktır"],
        "TBK m.93 uyarınca son gün kanuni tatile rastlarsa vade izleyen ilk tatil olmayan güne geçer; taraflar aksini kararlaştırabilir.",
        "Öteleme kanundan doğar ve sonraki ilk çalışma gününü hedefler. Hüküm yedek nitelikte olduğundan aksine anlaşma geçerlidir.",
        "6098 sayılı TBK m.93", "easy",
    ),
    r(
        "Borçlu vadesinden önce ödeme yapmış ve sırf erken ifa ettiği için borç tutarından indirim istemiştir. Kanun, sözleşme ve âdette indirim dayanağı yoktur. Sonuç nedir?",
        "Erken ifada borçlunun indirim yapabilmesi hangi koşula bağlıdır?",
        "Erken ifa mümkündür fakat indirim için kanun, sözleşme veya âdet dayanağı gerekir",
        ["Erken ifa her durumda yasaktır ve borçlu temerrüdüyle aynı sonucu doğurur", "Borçlu erken ifada borcun yarısını kendiliğinden ve gerekçesiz indirebilir", "İndirim yalnız alacaklının bütün alacağından vazgeçmesiyle değil otomatik oluşur", "Vadesinden önce ödeme borcun aynı tutarda ikinci kez doğmasına neden olur"],
        "TBK m.96 kural olarak erken ifaya izin verir; ancak kanun, sözleşme veya âdet olmadıkça borçlu erken ifa nedeniyle indirim yapamaz.",
        "Erken ifa serbestisi bedeli tek taraflı azaltma yetkisi değildir. İndirimin ayrıca geçerli bir hukuki dayanağı bulunmalıdır.",
        "6098 sayılı TBK m.96", "medium",
    ),
    r(
        "Karşılıklı borç yükleyen sözleşmede önce ifa etmesi gereken taraf kendi edimini yerine getirmeden karşı taraftan ifa talep etmiştir. Karşı tarafın savunması nedir?",
        "Karşılıklı borç yükleyen sözleşmede ifa isteyen tarafın kural olarak önce ne yapması gerekir?",
        "Kendi borcunu ifa etmeli veya gereği gibi ifasını önermelidir",
        ["İfa isteyen kendi borcunu sunmaz", "İfa talebinden önce sözleşmeyi üçüncü kişiye karşılıksız devretmek zorundadır", "Karşı tarafın borcunu iki katına çıkaran tek taraflı bir belge düzenlemelidir", "Kendi edimini ancak karşı tarafın bütün hakları sona erdikten sonra sunabilir"],
        "TBK m.97, daha sonra ifa hakkı yoksa karşı edimi isteyen tarafın kendi borcunu ifa etmiş veya ifasını önermiş olmasını arar.",
        "Ödemezlik def'i edimler arasındaki karşılıklılığı korur. Sözleşme veya işin özelliği sonraki ifa hakkı tanıyorsa sıra farklılaşabilir.",
        "6098 sayılı TBK m.97", "medium",
    ),
    r(
        "Karşılıklı sözleşmede borçlulardan biri iflasa düşmüş ve diğer tarafın karşı edimi tehlikeye girmiştir. İstendiği hâlde uygun sürede güvence de verilmemiştir. Diğer taraf ne yapabilir?",
        "Karşı edimi tehlikeye düşüren ifa güçsüzlüğünde hakkı tehlikede olan tarafın koruması nedir?",
        "Güvenceye kadar ifadan kaçınabilir; uygun sürede güvence verilmezse dönebilir",
        ["Kendi edimini derhâl iki katıyla ifa edip hiçbir güvence isteyemez", "İfa güçsüzlüğü yalnız sözleşme bedelini otomatik olarak yarıya indirir", "Karşı tarafın iflası sözleşmeyi her durumda hiçbir işleme gerek kalmadan yeniler", "Güvence verilmemesi tehlikedeki tarafın bütün savunmalarını kendiliğinden kaldırır"],
        "TBK m.98, ifa güçsüzlüğü nedeniyle hakkı tehlikeye düşen tarafa güvence verilene kadar ifadan kaçınma ve süresinde güvence yoksa dönme hakkı tanır.",
        "Koruma, karşı edimin gerçekleşmeme riskini dengeler. Dönme için güvence talebi ve uygun sürenin sonuçsuz kalması aranır.",
        "6098 sayılı TBK m.98", "hard",
    ),
    r(
        "Yabancı para borcunda sözleşmede aynen ödeme kaydı yoktur. Borçlu vade gününde borcu ödemek istemektedir. Ödeme biçimi bakımından hangisi doğrudur?",
        "Yabancı para borcunda aynen ödeme kaydı bulunmadığında borçlu hangi imkâna sahiptir?",
        "Borç ödeme günündeki rayiç üzerinden ülke parasıyla da ödenebilir",
        ["Yabancı para ülke parasıyla ödenemez", "Yabancı para kaydı borcu herhangi bir ifa olmadan kendiliğinden sona erdirir", "Borçlu rayici kendi belirlediği geçmiş bir tarihe göre tek taraflı hesaplayabilir", "Ülke parasıyla ödeme bütün yabancı para borçlarında kesin olarak yasaktır"],
        "TBK m.99, aynen ödeme kaydı yoksa yabancı para borcunun ödeme günündeki rayiçle ülke parası üzerinden ifasına izin verir.",
        "Aynen ödeme kaydı para türünü kesinleştirir. Bu kayıt yoksa borçlu ödeme gününde ülke parasıyla ifa seçeneğini kullanabilir.",
        "6098 sayılı TBK m.99", "medium",
    ),
    r(
        "Borçlu faiz ve giderlerde gecikmemişken borcun bir kısmını ödemiştir. Ödemenin ana borca mahsubunu istemektedir. Alacaklı bunun aksini kararlaştırdıklarını ileri sürmüştür. Hangisi doğrudur?",
        "Faiz veya giderlerde gecikme yoksa kısmi ödemenin ana borca mahsubu bakımından kural nedir?",
        "Borçlu kısmi ödemeyi ana borçtan düşebilir ve bunun aksine anlaşma yapılamaz",
        ["Kısmi ödeme yalnız gelecekte doğabilecek belirsiz giderlere mahsup edilebilir", "Alacaklı her durumda ödemeyi borçla ilgisiz üçüncü kişinin hesabına yazabilir", "Borçlu kısmi ödemenin hiçbir borca mahsup edilmemesini zorunlu olarak kabul eder", "Ana borca mahsup ancak borcun tamamı zamanaşımına uğradıktan sonra mümkündür"],
        "TBK m.100, faiz veya giderlerde gecikme yoksa borçluya kısmi ödemeyi ana borçtan düşme hakkı verir ve aksine anlaşmayı yasaklar.",
        "Kural emredicidir. Ancak borçlu, kısmi ödemeyi güvence altındaki veya daha iyi güvenceli kısma yöneltemez.",
        "6098 sayılı TBK m.100", "hard",
    ),
    r(
        "Aynı alacaklıya birden çok borcu olan borçlu, ödeme gününde ödemenin hangi borç için yapıldığını açıkça bildirmiştir. Mahsup nasıl yapılır?",
        "Birden çok borçta borçlunun ödeme anındaki geçerli mahsup bildiriminin etkisi nedir?",
        "Ödeme borçlunun bildirdiği borca mahsup edilir",
        ["Borçlunun bildirimi dikkate alınmaz", "Mahsup yalnız alacaklının yıllar sonra seçeceği ilgisiz borca yapılabilir", "Borçlunun bildirimi bütün borçları aynı anda ve karşılıksız sona erdirir", "Birden çok borç bulunması yapılan ödemenin hukuken geçersiz olmasına yol açar"],
        "TBK m.101 borçluya ödeme gününde hangi borcu ödediğini bildirme yetkisi verir. Bildirim yoksa ve itiraz edilmezse makbuz açıklaması önem kazanır.",
        "Mahsup sırasının ilk belirleyicisi borçlunun ödeme anındaki açıklamasıdır. Bu açıklama yoksa alacaklının makbuzdaki belirlemesine derhâl itiraz edilip edilmediğine bakılır.",
        "6098 sayılı TBK m.101", "easy",
    ),
    r(
        "Borçlu ve alacaklı mahsup açıklaması yapmamış; borçlardan birinin vadesi gelmiş, diğerlerininki gelmemiştir. Yapılan ödeme öncelikle hangi borca sayılır?",
        "Geçerli mahsup açıklaması ve makbuzda açıklık yoksa kanuni sıra ilk olarak hangi borcu esas alır?",
        "Ödeme öncelikle muaccel borca yapılmış sayılır",
        ["Ödeme en uzak vadeli borca sayılır", "Açıklama yokluğu bütün borçların karşılıksız olarak yenilenmesine neden olur", "Ödeme hiçbir borca mahsup edilmez ve alacaklının bağışı kabul edilir", "Kanuni sıra borçlunun doğum tarihine en yakın sözleşmeyi esas alır"],
        "TBK m.102 uyarınca açıklama yoksa ödeme önce muaccel borca; birden çok muaccel borç varsa ilk takip edilene yönelir.",
        "Takip yoksa vadesi önce gelen, vadeler aynıysa orantılı mahsup uygulanır. Hiçbiri muaccel değilse güvencesi en az borç öne çıkar.",
        "6098 sayılı TBK m.102", "medium",
    ),
    r(
        "Borçlu borcun tamamını ödemiş ve borç senedinin hâlen alacaklıda bulunduğunu görmüştür. Borçlunun belge yönünden hakkı nedir?",
        "Borcun tamamını ödeyen borçlu alacaklıdan hangi belgeleri isteyebilir?",
        "Makbuz ile borç senedinin geri verilmesini veya iptalini isteyebilir",
        ["Yalnız yeni bir borç senedi düzenlenmesini ve eski senedin saklanmasını isteyebilir", "Ödeme belgesi istemesi borcun aynı tutarda yeniden doğmasına neden olur", "Borçlu hiçbir makbuz veya senet işlemi isteme hakkına sahip değildir", "Alacaklı borç senedini üçüncü kişiye bağışlamakla yükümlü hâle gelir"],
        "TBK m.103, borcu ödeyen borçluya makbuz; tam ödemede ayrıca borç senedinin iadesi veya iptalini isteme hakkı tanır.",
        "Kısmi ödemede makbuz ve ödemenin senede işlenmesi istenebilir. Tam ödeme senet üzerindeki görünüşteki alacak riskini kaldırmayı amaçlar.",
        "6098 sayılı TBK m.103", "easy",
    ),
    r(
        "Borçlu edimi gereği gibi önermiş; alacaklı haklı sebep olmadan kabulden ve gerekli hazırlık işlemini yapmaktan kaçınmıştır. Alacaklı hangi duruma düşer?",
        "Alacaklının temerrüdü için kabulden veya hazırlık fiilinden kaçınma hangi nitelikte olmalıdır?",
        "Haklı sebep olmaksızın gereği gibi önerilen edimi kabulden kaçınmalıdır",
        ["Haklı ret de temerrüt yaratır", "Borçlu edimi hiç önermese de alacaklı her durumda temerrüt sorumlusu olur", "Kabulden kaçınma haklı nedene dayanıyorsa alacaklı kesin biçimde temerrüde düşer", "Alacaklı temerrüdü yalnız borçlunun borcu inkâr etmesiyle ve ifasız oluşur"],
        "TBK m.106 gereği gibi önerilen yapma veya verme edimini haklı sebep olmadan kabul etmeyen ya da gerekli hazırlığı yapmayan alacaklıyı temerrüde düşürür.",
        "Borçlunun uygun ifa önerisi ve alacaklının haksız iş birliği eksikliği birlikte aranır. Haklı ret temerrüt oluşturmaz.",
        "6098 sayılı TBK m.106", "medium",
    ),
    r(
        "Alacaklı teslim edilecek malı haklı sebep olmaksızın kabul etmemiştir. Borçlu malı hâkimin belirlediği yere, hasar ve giderler alacaklıya ait olmak üzere tevdi etmiştir. Sonuç nedir?",
        "Alacaklının temerrüdünde teslim konusu şeyin tevdi edilmesinin temel sonucu nedir?",
        "Borçlu şeyi usulüne uygun tevdi ederek borcundan kurtulabilir",
        ["Tevdi borcu sona erdirmez", "Borçlu malı tevdi edince alacaklının bütün başka haklarını kendisi kazanır", "Tevdi yalnız alacaklının önceden yazılı kabulü varsa temerrüt yaratır", "Teslim konusu şey hiçbir koşulda tevdi edilemez ve borç sonsuza kadar sürer"],
        "TBK m.107 alacaklı temerrüdünde borçluya, hasar ve giderleri alacaklıya ait olmak üzere şeyi tevdi ederek borçtan kurtulma imkânı verir.",
        "Tevdi yerini ifa yerindeki hâkim belirler; ticari mallar hâkim kararı olmadan ardiyeye bırakılabilir.",
        "6098 sayılı TBK m.107", "medium",
    ),
    r(
        "Alacaklının kabul etmediği teslim konusu mal hızla bozulmaktadır. Borçlu önceden ihtar vermiş ve hâkimden izin almıştır. Borçlunun başvurabileceği yol nedir?",
        "Tevdiye uygun olmayan veya bozulabilir teslim konusu şey alacaklı temerrüdünde nasıl değerlendirilebilir?",
        "Şey açık artırmayla sattırılıp bedeli tevdi edilebilir",
        ["Bozulabilir mal satılamaz", "Bozulabilir malın değeri alacaklının bütün borçlarına otomatik mahsup edilir", "Mal yalnız on yıl saklandıktan sonra karşılıksız olarak üçüncü kişiye bırakılır", "Tevdiye uygun olmama borçluyu aynı maldan iki kez teslimle yükümlü kılar"],
        "TBK m.108, uygun olmayan, bozulabilir veya önemli gider gerektiren şeyi kural olarak ihtar ve hâkim izniyle açık artırmada sattırıp bedeli tevdiye izin verir.",
        "Borsa veya piyasa fiyatı bulunan ya da değeri giderine göre az olan şeylerde açık artırma zorunlu olmayabilir; hâkim ihtar koşulunu da kaldırabilir.",
        "6098 sayılı TBK m.108", "hard",
    ),
    r(
        "Borç hiç ifa edilmemiş ve alacaklı zarara uğramıştır. Borçlu, kusuru bulunmadığını ispat edememektedir. Tazmin yükümlülüğü bakımından hangisi doğrudur?",
        "Sözleşmeye aykırılıkta borçlunun zararı gidermekten kurtulması için neyi ispat etmesi gerekir?",
        "Kendisine hiçbir kusur yüklenemeyeceğini ispat etmelidir",
        ["Kusursuzluk borçluyu kurtarmaz", "Borçlu yalnız borcun varlığını inkâr ederek tazmin yükümlülüğünü kaldırabilir", "İfa etmeyen borçlu kusur durumundan bağımsız olarak daima sorumsuz kabul edilir", "Borçlunun başka alacaklılara ödeme yapması bu zararı kendiliğinden sona erdirir"],
        "TBK m.112, hiç veya gereği gibi ifa etmeyen borçluyu kusursuzluğunu ispat etmedikçe alacaklının zararını gidermekle yükümlü tutar.",
        "Sözleşmeye aykırılık ve zarar ortaya konduğunda kusursuzluk ispatı borçluya düşer. Bu yönüyle haksız fiildeki genel ispat düzeninden ayrılır.",
        "6098 sayılı TBK m.112", "medium",
    ),
    r(
        "Borçlu yapma borcunu yerine getirmemiştir. Alacaklı edimin başka biri tarafından yapılmasını ve masrafın borçluya yükletilmesini istemektedir. Bu talep mümkün müdür?",
        "İfa edilmeyen yapma borcunda alacaklının aynen ifaya yönelik özel imkânı nedir?",
        "Masrafı borçluya ait olmak üzere edimi yapmaya veya yaptırmaya izin isteyebilir",
        ["Alacaklı yalnız edimi tamamen bağışlayabilir ve hiçbir giderim talep edemez", "Yapma borcu ifa edilmezse alacaklı borçlunun bütün malvarlığını kendiliğinden kazanır", "Edim ancak borçlunun ölümünden sonra ve masrafı alacaklıya ait olarak yapılabilir", "Yapma borcuna aykırılık her durumda sözleşmeyi yeni bir kira ilişkisine dönüştürür"],
        "TBK m.113, yapma borcu ifa edilmezse alacaklıya masrafı borçluya ait olmak üzere kendisinin veya başkasının ifasına izin isteme hakkı verir.",
        "Bu yol giderim taleplerini ortadan kaldırmaz. Yapmama borcuna aykırılıkta zarar giderimi ve aykırı durumun kaldırılması istenebilir.",
        "6098 sayılı TBK m.113", "hard",
    ),
    r(
        "Taraflar borçlunun ağır kusurundan sorumlu olmayacağını sözleşme kurulmadan önce kararlaştırmıştır. Daha sonra zarar ağır kusurla doğmuştur. Sorumsuzluk kaydının durumu nedir?",
        "Borçlunun ağır kusuruna ilişkin önceden yapılan sorumsuzluk anlaşması nasıl değerlendirilir?",
        "Ağır kusurdan sorumsuzluk kaydı kesin hükümsüzdür",
        ["Kayıt ağır kusuru her durumda geçerli bir ifa biçimine dönüştürür", "Sorumsuzluk kaydı yalnız alacaklının zararını otomatik olarak iki katına çıkarır", "Ağır kusur için önceden sorumsuzluk anlaşması kanunen zorunlu tutulmuştur", "Kayıt borçlunun yardımcı kişilerini alacaklının çalışanı hâline getirir"],
        "TBK m.115, borçlunun ağır kusurundan sorumlu olmayacağına ilişkin önceden yapılan anlaşmayı kesin hükümsüz sayar.",
        "Hizmet sözleşmesinden doğan borçlarda önceden her türlü sorumsuzluk kaydı da hükümsüzdür. İzinli uzmanlık faaliyetlerinde hafif kusur kaydı dahi geçersiz olabilir.",
        "6098 sayılı TBK m.114-115", "easy",
    ),
    r(
        "Borçlu, ifayı çalışanına bırakmış; çalışan işi yürütürken alacaklıya zarar vermiştir. Faaliyet kanuna uygun biçimde yardımcıya bırakılmıştır. Borçlunun sorumluluğu nedir?",
        "Borcun ifası yardımcı kişiye bırakıldığında yardımcı iş sırasında zarar verirse temel kural nedir?",
        "Borçlu yardımcı kişinin işi yürütürken verdiği zararı gidermekle yükümlüdür",
        ["Kanuna uygun bırakma borçluyu yardımcı fiilinden her durumda tamamen kurtarır", "Zarar yalnız yardımcının ailesi tarafından ve borçtan bağımsız olarak karşılanır", "Yardımcı kullanılması alacaklının tazminat haklarını kendiliğinden sona erdirir", "Borçlu yardımcı seçtiği anda asıl borç ilişkisi hiçbir işleme gerek kalmadan yenilenir"],
        "TBK m.116, ifayı veya hakkın kullanımını yardımcıya bırakan borçluyu, yardımcının işi yürütürken verdiği zarardan sorumlu tutar.",
        "Sorumluluk bazı durumlarda anlaşmayla sınırlandırılabilir; ancak izinle yürütülen uzmanlık faaliyetlerinde yardımcı fiili için sorumsuzluk anlaşması hükümsüzdür.",
        "6098 sayılı TBK m.116", "medium",
    ),
    r(
        "Muaccel borç için vade günü taraflarca belirlenmemiş ve ihtarsız temerrüt oluşturan başka bir hâl yoktur. Alacaklı hiçbir bildirim yapmadan temerrüt sonuçlarını istemiştir. Hangisi doğrudur?",
        "Muaccel borçta özel bir ihtarsız temerrüt hâli yoksa borçlu kural olarak nasıl temerrüde düşer?",
        "Alacaklının borçluya ifa ihtarında bulunması gerekir",
        ["Borçlu borç doğmadan önce kendiliğinden ve sürekli biçimde temerrüde düşer", "Temerrüt yalnız alacaklının alacağından vazgeçtiği anda gerçekleşebilir", "Muacceliyet hiçbir zaman temerrütle birlikte değerlendirilemez ve ihtar yasaktır", "Borçlu başka bir sözleşme yaptığında bu borç için otomatik temerrüde düşer"],
        "TBK m.117'de muaccel borcun borçlusu kural olarak alacaklının ihtarıyla temerrüde düşer. Belirli vade ve kanundaki özel hâller ihtarsız temerrüt doğurabilir.",
        "Muacceliyet ifanın istenebilirliğidir; tek başına her durumda temerrüt yaratmaz. İhtar borçluya son ve açık ifa çağrısıdır.",
        "6098 sayılı TBK m.117", "easy",
    ),
    r(
        "Karşılıklı borç yükleyen sözleşmede borçlu verilen uygun sürede de ifa etmemiştir. Alacaklı ifadan vazgeçtiğini hemen bildirerek olumlu zararını istemek istemektedir. Bu seçim mümkün müdür?",
        "Borçlunun temerrüdünde ek süre sonuçsuz kalırsa alacaklının temel seçimlik hakları nelerdir?",
        "İfa ve gecikme tazminatı, ifa yerine zarar giderimi veya sözleşmeden dönme seçilebilir",
        ["Alacaklı yalnız borcu bağışlayabilir ve hiçbir tazminat ya da dönme hakkı kullanamaz", "Ek sürenin dolması sözleşmeyi zorunlu olarak belirsiz süreli hizmet sözleşmesine çevirir", "Alacaklı sadece borçlunun başka bir borcunu üstlenerek temerrüt sonuçlarını kaldırabilir", "Temerrüt alacaklıyı sözleşme bedelinin iki katını borçluya ödemekle yükümlü kılar"],
        "TBK m.125, alacaklıya ifa ve gecikme tazminatı yanında ifadan vazgeçip olumlu zararını isteme veya sözleşmeden dönme seçeneklerini tanır.",
        "İfa yerine tazminat veya dönme için vazgeçme iradesi hemen bildirilmelidir. Süre verilmesini gerektirmeyen m.124 hâllerinde seçim ek süresiz yapılabilir.",
        "6098 sayılı TBK m.123-125", "hard",
    ),
]


PREMISES = [
    {
        "stem": "İfanın konusu ve kişisiyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Alacaklının menfaati yoksa borçlu kural olarak şahsen ifaya zorunlu değildir.\n\nII. Çeşit borcunda seçilen edim ortalama nitelikten düşük olamaz.\n\nIII. Seçimlik borçta aksi anlaşılmadıkça seçim borçluya aittir.",
        "correct": "I, II ve III", "why": "TBK m.83, 86 ve 87 uyarınca üç ifade de doğrudur.",
        "ref": "6098 sayılı TBK m.83, 86 ve 87", "difficulty": "medium",
    },
    {
        "stem": "İfa yeri ve zamanıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Para borcu kural olarak alacaklının ödeme zamanındaki yerleşim yerinde ifa edilir.\n\nII. Vade kararlaştırılmamışsa borç doğduğu anda muaccel olur.\n\nIII. Son gün kanuni tatile rastlarsa kural olarak ilk tatil olmayan güne geçer.",
        "correct": "I, II ve III", "why": "TBK m.89, 90 ve 93 uyarınca üç ifade de doğrudur.",
        "ref": "6098 sayılı TBK m.89, 90 ve 93", "difficulty": "medium",
    },
    {
        "stem": "Karşılıklı borç yükleyen sözleşmeyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Önce ifa etmesi gereken taraf, karşı edimi isterken kendi ifasını sunmalıdır.\n\nII. İfa güçsüzlüğünde hakkı tehlikeye düşen taraf güvenceye kadar ifadan kaçınamaz.\n\nIII. Uygun sürede güvence verilmezse hakkı tehlikeye düşen taraf sözleşmeden dönebilir.",
        "correct": "I ve III", "why": "TBK m.97 nedeniyle I, m.98 nedeniyle III doğrudur. Güvence verilinceye kadar ifadan kaçınılabildiği için II yanlıştır.",
        "ref": "6098 sayılı TBK m.97-98", "difficulty": "medium",
    },
    {
        "stem": "Mahsupla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Birden çok borçta borçlu ödeme anında mahsup edilecek borcu bildiremez.\n\nII. Geçerli açıklama yoksa ödeme öncelikle muaccel borca sayılır.\n\nIII. Hiçbir borç muaccel değilse ödeme güvencesi en az olan borca sayılır.",
        "correct": "II ve III", "why": "TBK m.102 nedeniyle II ve III doğrudur. Borçlu m.101 uyarınca ödeme anında mahsup edilecek borcu bildirebildiğinden I yanlıştır.",
        "ref": "6098 sayılı TBK m.101-102", "difficulty": "hard",
    },
    {
        "stem": "Alacaklının temerrüdüyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Gereği gibi önerilen edimin haklı sebep olmadan reddi temerrüt oluşturabilir.\n\nII. Teslim konusu şeyin tevdi edilmesi borçluyu hiçbir durumda borçtan kurtaramaz.\n\nIII. Bozulabilir şey kanuni koşullarla sattırılıp bedeli tevdi edilebilir.",
        "correct": "I ve III", "why": "TBK m.106 nedeniyle I, m.108 nedeniyle III doğrudur. Usulüne uygun tevdi m.107 uyarınca borçluyu kurtarabildiğinden II yanlıştır.",
        "ref": "6098 sayılı TBK m.106-108", "difficulty": "medium",
    },
    {
        "stem": "Sözleşmeye aykırılıkla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Borçlu kusursuzluğunu ispat ederse TBK m.112 sorumluluğundan kurtulabilir.\n\nII. Yapma borcunda alacaklı masrafı borçluya ait olmak üzere ifaya izin isteyebilir.\n\nIII. Ağır kusurdan sorumsuzluk için önceden yapılan kayıt geçerlidir.",
        "correct": "I ve II", "why": "TBK m.112 ve 113 nedeniyle I ve II doğrudur. Ağır kusura ilişkin önceden sorumsuzluk kaydı m.115 gereği kesin hükümsüzdür; III yanlıştır.",
        "ref": "6098 sayılı TBK m.112-115", "difficulty": "hard",
    },
    {
        "stem": "Borçlunun temerrüdüyle ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Muaccel borçta kural olarak ihtar aranır.\n\nII. Vade günü taraflarca birlikte belirlenmişse günün geçmesi temerrüt doğurabilir.\n\nIII. Temerrüde düşen borçlu beklenmedik hâlden hiçbir koşulda sorumlu olmaz.",
        "correct": "I ve II", "why": "TBK m.117 nedeniyle I ve II doğrudur. Temerrüt borçlusu m.119 uyarınca kural olarak beklenmedik hâlden de sorumludur; III yanlıştır.",
        "ref": "6098 sayılı TBK m.117 ve 119", "difficulty": "medium",
    },
    {
        "stem": "Temerrütte alacaklının haklarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Süre verilmesi etkisiz olacaksa ek süre gerekmeyebilir.\n\nII. İfa alacaklı için yararsız kalmışsa ek süre gerekmeyebilir.\n\nIII. Dönmede daha önceki karşılıklı edimler hiçbir zaman geri istenemez.",
        "correct": "I ve II", "why": "TBK m.124 nedeniyle I ve II doğrudur. Dönmede taraflar önceki edimleri geri isteyebildiğinden III yanlıştır.",
        "ref": "6098 sayılı TBK m.124-125", "difficulty": "hard",
    },
]


WRONG_BANKS = {"unused": ["a", "b", "c", "d", "e", "f"]}


if __name__ == "__main__":
    write_topic(
        lesson_id="borclar_hukuku", topic_id="borcun_ifasi",
        label="Borcun İfası", slug="borcun_ifasi",
        prefix="kh-borc-ifa", seed=20260726,
        legislation_version="6098 sayılı TBK m.83–126 — 17.07.2026 güncel metin",
        rules=RULES, premises=PREMISES, wrong_banks=WRONG_BANKS,
    )
