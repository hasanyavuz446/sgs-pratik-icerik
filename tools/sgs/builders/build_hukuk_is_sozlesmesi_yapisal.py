#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Is Hukuku / Is Sozlesmesi — YAPISAL kalibrasyon (tanim sorusu -> kural uygulamasi).

OLCULEN ACIK (2026-08-13). Bu tur, kullanicinin avukat arkadasinin "sorular cok
basit" degerlendirmesi uzerine acildi ve degerlendirme OLCUMLE dogrulandi.
Karsilastirma tabani: 2014-2026 arsivinden cikarilan 629 GERCEK sinav hukuk sorusu
(telif geregi yalnizca bicim olculdu, metin kopyalanmadi).

    olcut                gercek sinav   bu paket (once)
    medyan kok                    257                98
    olumsuz kok                 %41,5              %4,4
    duz tanim sorusu             %6,2             %66,7   <- ASIL KUSUR
    olay orgulu kok             %16,2                %0

Kusur bicimsel degil YAPISAL idi: 40/60 soru "...bakimindan dogru ifade
asagidakilerden hangisidir?" kalibindaydi ve tek kavrami taniyan adayi
odullendiriyordu. Gercek sinav kurali OLAYA uygulatir ve cogunlukla "hangisi
yanlistir" diye sorar. Bu builder paketin 57 sorusunu somut olay + "Buna gore"
koprusu + olumsuz kok yapisina tasir (kalan 3 soru zaten senaryo yapisindaydi).

⚠️ §5 TASARIM ZAMANI BOY DENETIMI uygulandi: ilk tasarim 27/42 (%64) tek-en-uzun
cikip uretimi DURDURDU; 40 celdiriciye gercek hukuki icerik (yanlis iddianin kendi
sonucu) eklenerek 57 yamada %30'a indirildi. Dogru sik KISALTILMADI.

§6 notu: her yamanin dogru cevap HARFI mevcut JSON'daki harfle ayni birakildi;
paketin harf dagilimi ve run ozelligi degismez.

Duzeltilen icerik hatasi: 0010'un kokunde "TTK ve Is Kanunu uyarinca" ifadesi
vardi; belirli/belirsiz sureli is sozlesmesi ayrimiyla Turk Ticaret Kanunu'nun
ilgisi yoktur.

Dayanak: 4857 sayili Is Kanunu md. 2, 4, 5, 6, 8, 11, 13, 14, 15, 22, 28, 32, 34,
35, 38, 41, 44, 46, 47, 53, 54, 56, 57, 58, 63, 68, 69, 71, 73, 74 · TBK md. 30 vd.,
396, 399, 400, 417, 444-447 · 6331 sayili Kanun md. 13.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/is_ve_sosyal_guvenlik_hukuku/is_hukuku_is_sozlesmesi.json"
STYLE_REF = "SGS Is Hukuku (gercek sinav yapisina kalibre: olay + kural uygulamasi)"
ONEK = "ish-sozlesme-gen-"


def patch(stem, options, answer, solution):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": "4857 sayili Is Kanunu"},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    '0001': patch(
        "Bir fabrikada üretim bandında çalışan Ahmet, işverenle yaptığı sözleşmeye dayanarak ücret karşılığı ve işverenin talimatları altında çalışmaktadır. Aynı fabrikanın muhasebe işlerini, kendi bürosunda ve kendi çalışanlarıyla, aylık maktu bedel karşılığında bağımsız olarak yürüten bir serbest muhasebeci mali müşavir de bulunmaktadır. Buna göre 4857 sayılı İş Kanunu'nun uygulama alanı bakımından aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'İşçi sıfatı yalnızca gerçek kişiler için söz konusu olur',
            'B': 'Muhasebe işlerini bağımsız yürüten meslek mensubu da bağımlılık unsuru gerçekleştiği için işçi sayılır',
            'C': 'Meslek mensubu işi kendi bürosunda ve kendi belirlediği düzende gördüğünden aralarındaki ilişki iş sözleşmesi değil vekâlet ilişkisidir',
            'D': 'Ahmet, bir iş sözleşmesine dayanarak çalıştığı için işçidir',
            'E': 'Bağımlılık unsuru, iş sözleşmesini vekâlet ve eser sözleşmesinden ayıran temel ölçüttür',
        },
        'B',
        "4857 md. 2: işçi, bir iş sözleşmesine dayanarak çalışan gerçek kişidir. Ayırt edici ölçüt BAĞIMLILIK'tır; işi işverenin emir ve talimatı altında görmek. Meslek mensubu işi kendi bürosunda, kendi düzeninde ve kendi çalışanlarıyla gördüğünden bağımlılık yoktur; ilişki iş sözleşmesi değil vekâlet ilişkisidir.",
    ),
    '0002': patch(
        'Bir şirket, bir kişiyle aylık maktu bedel karşılığında sözleşme yapmıştır. Kişi işi kendi ofisinde, kendi belirlediği saatlerde ve kendi ekipmanıyla görmekte; şirketin günlük talimatlarına tabi bulunmamaktadır. Aynı şirkette bir başka kişi ise şirketin belirlediği mesai saatlerinde, şirket araçlarıyla ve amirinin talimatları altında çalışmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İkinci kişi işçidir; birincisiyle kurulan ilişki bağımlılık bulunmadığı için iş sözleşmesi sayılmaz',
            'B': 'Birinci kişi işçidir; ikinci kişi ise şirket aracı kullandığı için bağımsız çalışan sayılır',
            'C': 'Her ikisi de bir iş görüp karşılığında ücret aldığından işçi sayılır ve haklarında İş Kanunu hükümleri uygulanır',
            'D': 'İşçi sıfatı için ücretin maktu ödenmesi yeterlidir; bağımlılık ölçütü aranmaz',
            'E': 'İkisi de tüzel kişi adına çalıştığı için işveren vekili konumundadır',
        },
        'A',
        "4857 md. 2: işçi, bir iş sözleşmesine dayanarak çalışan gerçek kişidir. Ayırt edici unsur BAĞIMLILIK'tır; işin işverenin emir, talimat ve denetimi altında görülmesi. İşi kendi ofisinde, kendi saatlerinde ve kendi araçlarıyla gören kişide bağımlılık yoktur; ilişki iş sözleşmesi değildir. Ücretin maktu ödenmesi tek başına işçilik göstermez.",
    ),
    '0003': patch(
        'Bir belediyeye ait tüzel kişiliği bulunmayan işletme, kendi adına işçi çalıştırmaktadır. Bu işletmede genel müdür sıfatıyla görev yapan kişi, işveren adına hareket ederek işin ve işyerinin yönetiminde karar almakta, ayrıca kendisi de bir iş sözleşmesiyle çalışmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İşçi çalıştıran tüzel kişiliği olmayan kurum ve kuruluşlar da işveren sayılır',
            'B': 'İşveren vekilliği, işverene ait yetkilerin kullanılmasına dayanan bir temsil ilişkisidir',
            'C': 'İşveren vekili sıfatını taşıyan genel müdür, bu sıfatı nedeniyle işçilik haklarından yararlanamaz',
            'D': 'İşveren vekilinin bu sıfatla yaptığı işlem ve davranışlardan, işçilere karşı doğrudan doğruya işveren sorumlu olur',
            'E': 'İşveren vekili aynı zamanda bir iş sözleşmesiyle çalışıyorsa işçi sıfatını da taşır',
        },
        'C',
        '4857 md. 2: işveren, işçi çalıştıran gerçek veya tüzel kişi ya da tüzel kişiliği olmayan kurum ve kuruluştur. İşveren vekili, işveren adına hareket eden ve işin, işyerinin ve işletmenin yönetiminde görev alan kişidir; bu sıfatı işçilik haklarını ORTADAN KALDIRMAZ. Vekilin bu sıfatla yaptığı işlemlerden işveren sorumludur.',
    ),
    '0004': patch(
        'Bir anonim şirkette insan kaynakları direktörü, işveren adına işe alım ve fesih kararı vermekte, işyerinin yönetiminde görev almaktadır. Bu direktör bir işçiye, işverenin bilgisi dışında ve hukuka aykırı biçimde ağır bir ceza uygulamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sorumluluk için vekile ayrıca yazılı yetki belgesi verilmiş olması gerekir',
            'B': 'Direktör bu sıfatı nedeniyle işveren sayılır ve doğan sorumluluk yalnızca kendi malvarlığına aittir',
            'C': 'İşveren vekili sıfatı taşıyan kişi, bir iş sözleşmesiyle çalışsa dahi işçi sayılmaz ve işçilik haklarından yararlanamaz',
            'D': 'Direktör işveren vekilidir; bu sıfatla yaptığı işlemlerden işçilere karşı doğrudan işveren sorumlu olur',
            'E': 'İşveren, vekilin bilgisi dışındaki işlemlerinden sorumlu tutulamaz',
        },
        'D',
        '4857 md. 2: işveren adına hareket eden ve işin, işyerinin ve işletmenin yönetiminde görev alan kimseye işveren vekili denir. İşveren vekilinin bu sıfatla işçilere karşı yaptığı işlem ve üstlendiği yükümlülüklerden DOĞRUDAN İŞVEREN sorumludur. İşveren vekilliği işçi sıfatını ortadan kaldırmaz ve vekile işveren sıfatı kazandırmaz.',
    ),
    '0005': patch(
        'Bir tekstil fabrikasının işvereni, üretimin boyama bölümünü yardımcı iş olarak bir alt işverene vermiştir. Alt işveren, bu bölümde çalıştırdığı işçilerin üç aylık ücretlerini ve kıdem tazminatlarını ödememiştir. Buna göre 4857 sayılı Kanun uyarınca aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Asıl işveren ancak yazılı olarak kefil olmuşsa sorumlu tutulabilir',
            'B': 'Sorumluluk yalnızca alt işverene aittir; asıl işverene başvurulamaz',
            'C': 'Asıl işveren yalnızca ücretten sorumlu olup kıdem tazminatından sorumlu değildir',
            'D': 'Asıl işverenin sorumluluğu ikinci derecededir; ancak alt işverenin malvarlığı tükendikten sonra ona başvurulabilir',
            'E': 'Asıl işveren, alt işverenin işçilerine karşı alt işverenle birlikte müteselsilen sorumludur',
        },
        'E',
        '4857 md. 2/6: asıl işveren, alt işverenin işçilerine karşı o işyeriyle ilgili olarak bu Kanundan, iş sözleşmesinden veya toplu iş sözleşmesinden doğan yükümlülüklerden alt işverenle birlikte SORUMLUDUR. Sorumluluk müteselsildir; işçi doğrudan asıl işverene başvurabilir, önce alt işverene gitmesi ya da yazılı kefalet aranmaz.',
    ),
    '0006': patch(
        'İki kişi arasında yapılan sözleşmede, taraflardan biri belirli bir sonucu (bir binanın projesini) teslim etmeyi, diğeri ise karşılığında bedel ödemeyi üstlenmiştir. Başka bir sözleşmede ise taraflardan biri işverenin belirlediği çalışma düzeni içinde iş görmeyi, diğeri ücret ödemeyi üstlenmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İkinci sözleşme iş sözleşmesidir; birincisi sonuç borcu doğurduğu için eser sözleşmesidir',
            'B': 'İş sözleşmesinin kurulması için sonucun taahhüt edilmiş olması gerekir',
            'C': 'Birinci sözleşme iş sözleşmesi, ikincisi ise bağımsız iş görme borcu doğuran vekâlet sözleşmesidir',
            'D': 'İki sözleşme arasındaki tek fark bedelin ödenme biçimidir',
            'E': 'Her iki sözleşme de ücret unsuru taşıdığından iş sözleşmesidir',
        },
        'A',
        "İş sözleşmesi, işçinin bağımlı olarak iş görmeyi, işverenin de ücret ödemeyi üstlendiği sözleşmedir (4857 md. 8). Unsurları iş görme, ücret ve BAĞIMLILIK'tır. Eser sözleşmesinde yüklenici bir SONUCU meydana getirmeyi üstlenir ve işi kendi düzeninde görür; bağımlılık yoktur. Vekâlette de iş görme vardır ama bağımlılık bulunmaz.",
    ),
    '0007': patch(
        'Bir mahkeme, taraflar arasındaki ilişkinin iş sözleşmesi sayılıp sayılmayacağını belirlemek için sözleşmenin kurucu unsurlarını incelemektedir. Sözleşmede bir işin görülmesi, karşılığında bir bedel ödenmesi ve işin işverenin talimatları altında yapılması öngörülmüştür. Buna göre aşağıdakilerden hangisi iş sözleşmesinin unsurlarından biri değildir?',
        {
            'A': 'Anlaşma; tarafların karşılıklı ve birbirine uygun irade beyanı',
            'B': 'Ücret; iş görme karşılığında sağlanan ve para ile ödenen bedel',
            'C': 'İş görme; işçinin bir işi bizzat yerine getirmesi',
            'D': 'İşçinin işletmeye sermaye koyarak ortak olması',
            'E': 'Bağımlılık; işin işverenin emir ve talimatı altında görülmesi',
        },
        'D',
        '4857 md. 8: iş sözleşmesi, bir tarafın (işçi) bağımlı olarak iş görmeyi, diğer tarafın (işveren) da ücret ödemeyi üstlenmesinden oluşan sözleşmedir. Kurucu unsurlar iş görme, ücret, bağımlılık ve tarafların anlaşmasıdır. İşletmeye sermaye koyarak ORTAK OLMAK bir şirket ilişkisi doğurur; iş sözleşmesinin unsuru değildir.',
    ),
    '0008': patch(
        'Bir uyuşmazlıkta, taraflar arasındaki ilişkinin iş sözleşmesi mi yoksa vekâlet ya da eser sözleşmesi mi olduğu tartışılmaktadır. Sözleşmede ücret kararlaştırılmış ve bir iş görülmesi öngörülmüştür. Buna göre nitelendirmede belirleyici olan ölçüt bakımından aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Nitelendirmede belirleyici ölçüt, işin işverenin emir ve talimatı altında görülmesidir',
            'B': 'Ücretin aylık ve maktu biçimde kararlaştırılmış olması ilişkiyi iş sözleşmesi hâline getirir',
            'C': 'Eser sözleşmesinde yüklenici belirli bir sonucu meydana getirmeyi üstlenir',
            'D': 'İşin, işverenin belirlediği yer, zaman ve çalışma düzeni içinde görülmesi bağımlılığın göstergesidir',
            'E': 'Vekâlette iş görme borcu vardır ancak bağımlılık ilişkisi bulunmaz',
        },
        'B',
        "İş sözleşmesini diğer iş görme sözleşmelerinden ayıran unsur BAĞIMLILIK'tır: işin işverenin emir, talimat ve denetimi altında, onun belirlediği yer, zaman ve düzende görülmesi. Ücretin aylık ve maktu ödenmesi tek başına nitelendirmeyi değiştirmez; bağımsız çalışanlara da maktu bedel ödenebilir.",
    ),
    '0009': patch(
        "Bir işveren, bir işçisiyle 6 ay süreli, başka bir işçisiyle ise 2 yıl süreli iş sözleşmesi yapmış; her ikisini de sözlü olarak kurmuştur. Buna göre 4857 sayılı Kanun'un şekle ilişkin kuralları bakımından aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Her iki sözleşme de yazılı yapılmadığı için geçersizdir',
            'B': 'Altı aylık sözleşme de bir yıldan kısa olduğu için yazılı yapılmalıydı',
            'C': 'İki yıllık sözleşme yazılı yapılmadığı için kendiliğinden belirsiz süreli sözleşmeye dönüşür ve süre kaydı hükümsüz kalır',
            'D': 'Süresi ne olursa olsun iş sözleşmelerinde yazılı şekil geçerlilik koşuludur',
            'E': 'İki yıllık sözleşmenin yazılı yapılması gerekirdi; ancak yazılı yapılmaması sözleşmeyi geçersiz kılmaz',
        },
        'E',
        '4857 md. 8: iş sözleşmesi kanunda aksi belirtilmedikçe özel bir şekle bağlı değildir. Süresi bir yıl ve daha fazla olan sözleşmelerin yazılı yapılması gerekir; ancak bu İSPAT şartıdır, geçerlilik şartı değildir. Yazılı yapılmaması sözleşmeyi geçersiz kılmaz ve belirsiz süreliye dönüştürmez. Yazılı sözleşme yapılmayan hâllerde işveren, iki ay içinde çalışma koşullarını gösteren bir belge vermekle yükümlüdür.',
    ),
    '0010': patch(
        'Bir işveren, sürekli nitelik taşıyan ve her yıl aynı biçimde yürütülen bir işte çalıştırdığı işçisiyle, objektif bir neden göstermeksizin bir yıllık belirli süreli iş sözleşmesi yapmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sözleşme geçersizdir ve taraflar arasında hiçbir iş ilişkisi doğmaz',
            'B': 'Belirli süreli sözleşme yapmak işverenin serbest takdirindedir',
            'C': 'Objektif neden bulunmadığı için sözleşme baştan itibaren belirsiz süreli kabul edilir',
            'D': 'Sözleşme ancak ikinci kez yenilendiğinde belirsiz süreliye dönüşür',
            'E': 'Sözleşme belirli süreli olarak geçerlidir ve süre sonunda fesih bildirimine gerek olmaksızın kendiliğinden sona erer',
        },
        'C',
        '4857 md. 11: belirli süreli iş sözleşmesi, süresi belirli bir işe veya belirli bir olgunun ortaya çıkmasına bağlanan objektif koşulların varlığında yapılabilir. Kural BELİRSİZ süreli sözleşmedir. Objektif neden yoksa sözleşme baştan itibaren belirsiz süreli sayılır; geçersiz olmaz.',
    ),
    '0011': patch(
        'Bir işyerinde tam süreli emsal işçinin haftalık çalışma süresi 45 saattir. İşveren, bir işçisiyle haftada 25 saat, başka bir işçisiyle haftada 40 saat çalışma öngören sözleşmeler yapmıştır. Buna göre kısmi süreli iş sözleşmesi bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kısmi süreli sayılabilmek için haftalık sürenin 20 saati aşmaması gerekir',
            'B': 'Kısmi süreli işçi, tam süreli işçiye göre ayrı bir hukuki rejime tabidir ve yıllık izne hak kazanamaz',
            'C': 'Kısmi süreli çalışma yalnızca belirli süreli sözleşmelerde kararlaştırılabilir',
            'D': 'Her iki sözleşme de 45 saatin altında kaldığı için kısmi sürelidir',
            'E': 'Haftada 25 saatlik sözleşme kısmi sürelidir; 40 saatlik sözleşme kısmi süreli sayılmaz',
        },
        'E',
        '4857 md. 13: işçinin normal haftalık çalışma süresi, tam süreli emsal işçiye göre ÖNEMLİ ÖLÇÜDE daha az belirlenmişse sözleşme kısmi sürelidir. Uygulamada ölçüt emsal işçinin süresinin üçte ikisidir: 45 × 2/3 = 30 saat. 25 saat bu sınırın altında kalır (kısmi süreli), 40 saat kalmaz. Kısmi süreli işçiye ayrım yapılamaz; süreye orantılı olarak bölünebilen haklardan payı oranında yararlanır.',
    ),
    '0012': patch(
        'Bir işveren, işçisiyle yaptığı iş sözleşmesine üç aylık deneme süresi koymuş; ikinci ayın sonunda, bildirim süresine uymaksızın ve tazminat ödemeksizin sözleşmeyi feshetmiştir. İşyerinde uygulanan bir toplu iş sözleşmesi bulunmamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Üç aylık deneme süresi tarafların anlaşmasıyla geçerli biçimde kararlaştırıldığından, bildirim süresine uyulmaksızın yapılan fesih her bakımından hukuka uygundur',
            'B': 'Deneme süresi en çok iki ay olabileceğinden üçüncü aya ilişkin kayıt geçersizdir; fesih ikinci ayın sonunda yapıldığı için deneme süresi içindedir',
            'C': 'Deneme süresi kaydı tümüyle geçersizdir; fesih bildirim süresine tabidir',
            'D': 'Deneme süresi ancak belirsiz süreli sözleşmelerde kararlaştırılabilir',
            'E': 'Deneme süresi içinde de bildirim süresine uyulması gerekir',
        },
        'B',
        '4857 md. 15: taraflarca iş sözleşmesine deneme kaydı konulduğunda süre en çok İKİ AY olabilir; ancak toplu iş sözleşmesiyle dört aya kadar uzatılabilir. İki ayı aşan kısım geçersizdir, kaydın tamamı değil. Deneme süresi içinde taraflar bildirim süresine gerek olmaksızın ve tazminatsız feshedebilir; işçinin çalıştığı günlerin ücreti saklıdır. Olayda fesih ikinci ayın sonunda, yani geçerli deneme süresi içinde yapılmıştır.',
    ),
    '0013': patch(
        'Bir işveren, on dört yaşını doldurmuş ve ilköğretimini tamamlamış bir çocuğu, bedensel gelişimine uygun hafif bir işte çalıştırmak istemektedir. Aynı işyerinde on üç yaşında bir çocuğun da sanat eğitimi kapsamı dışında çalıştırılması gündeme gelmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'On dört yaşını doldurmuş çocuk hafif işlerde çalıştırılabilir; on üç yaşındaki çocuğun çalıştırılması yasaktır',
            'B': 'On dört yaşını doldurmuş çocuk yalnızca gece işlerinde çalıştırılabilir',
            'C': 'Her iki çocuk da on beş yaşını doldurmadığı için çalıştırılamaz',
            'D': 'Çalıştırma yaşı bakımından ilköğretimin tamamlanmış olması aranmaz',
            'E': 'Her iki çocuk da yasal temsilcilerinin yazılı izni ve hekim raporu bulunması koşuluyla hafif işlerde çalıştırılabilir',
        },
        'A',
        '4857 md. 71: on beş yaşını doldurmamış çocukların çalıştırılması kural olarak yasaktır. Ancak on dört yaşını doldurmuş ve zorunlu ilköğretimini tamamlamış çocuklar, bedensel, zihinsel, sosyal ve ahlaki gelişmelerine engel olmayacak hafif işlerde çalıştırılabilir. On üç yaşındaki çocuk bu istisnaya girmez. Ayrıca 18 yaşını doldurmamış çocuk ve genç işçilerin gece çalıştırılması yasaktır.',
    ),
    '0014': patch(
        'Bir işçi hakkında açılan davada, işçinin iş sözleşmesinden doğan yükümlülüklerini yerine getirip getirmediği tartışılmaktadır. İşveren, işçinin kendisine karşı bazı borçları bulunduğunu ileri sürmektedir. Buna göre aşağıdakilerden hangisi işçinin iş sözleşmesinden doğan borçlarından biri değildir?',
        {
            'A': 'İtaat; işverenin hukuka uygun talimatlarına uyma',
            'B': 'İş görme; işi bizzat ve özenle yerine getirme',
            'C': 'Özen; kendisine teslim edilen araç ve gereçleri gerektiği gibi kullanma',
            'D': 'İşverenin ticari işlerini kendi çıkarına engelleme',
            'E': 'Sadakat; işverenin haklı çıkarlarını koruma ve ona zarar vermekten kaçınma',
        },
        'D',
        'İşçinin başlıca borçları iş görme, sadakat, özen ve itaattir (TBK md. 395-399). İşverenin işlerini KENDİ ÇIKARINA ENGELLEMEK bir borç değil, tam tersine sadakat borcunun AĞIR İHLALİDİR ve 4857 md. 25/II uyarınca işverene haklı nedenle derhal fesih hakkı verebilir.',
    ),
    '0015': patch(
        'Bir işçi, çalıştığı işyerinin üretim yöntemine ilişkin gizli bilgileri, henüz iş sözleşmesi devam ederken rakip bir firmaya aktarmıştır. İşçi, bu davranışının mesai saatleri dışında gerçekleştiğini ileri sürmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Bu davranış, işverene haklı nedenle derhal fesih hakkı verebilir',
            'B': 'İşverenin meslek sırlarını açıklamak sadakat borcunun ihlalidir',
            'C': 'Sadakat borcu yalnızca çalışma saatleriyle sınırlı olduğundan mesai dışındaki davranış bu borcu ihlal etmez',
            'D': 'Sadakat borcu iş sözleşmesinin sürdüğü dönem boyunca devam eder',
            'E': 'Sadakat borcu, işçinin işverenin çıkarlarını koruma ve zarar verecek davranışlardan kaçınma yükümlülüğünü kapsar',
        },
        'C',
        'Sadakat borcu (TBK md. 396, 4857 md. 25/II-e ile bağlantılı), işçinin işverenin haklı çıkarlarını korumasını ve ona zarar verecek davranışlardan kaçınmasını gerektirir; MESAİ SAATLERİYLE SINIRLI DEĞİLDİR. İşverenin meslek sırlarını ortaya atmak, 4857 md. 25/II-e uyarınca işverene haklı nedenle derhal fesih hakkı verir.',
    ),
    '0016': patch(
        'Bir işçi, işvereninin kendisine karşı yükümlülüklerini yerine getirmediğini ileri sürerek dava açmıştır. Mahkeme, işverenin iş sözleşmesinden doğan borçlarını belirlemektedir. Buna göre aşağıdakilerden hangisi işverenin iş sözleşmesinden doğan borçlarından biri değildir?',
        {
            'A': 'İşçinin işyeri dışındaki özel yaşamını yönlendirme',
            'B': 'Ücret ödeme; kararlaştırılan ücreti en geç ayda bir ödeme',
            'C': 'İş sağlığı ve güvenliği; gerekli önlemleri alma ve araçları eksiksiz bulundurma',
            'D': 'Eşit davranma; haklı neden olmadıkça işçiler arasında ayrım yapmama',
            'E': 'Gözetme; işçinin yaşamını ve sağlığını korumak için önlem alma',
        },
        'A',
        'İşverenin başlıca borçları ücret ödeme (4857 md. 32), işçiyi gözetme (TBK md. 417), eşit davranma (4857 md. 5) ve iş sağlığı ve güvenliği önlemlerini almadır (6331 md. 4). İşverenin yönetim yetkisi İŞİN GÖRÜLMESİYLE sınırlıdır; işçinin işyeri dışındaki özel yaşamını yönlendirme yetkisi bulunmaz ve bu bir borç da değildir.',
    ),
    '0017': patch(
        'Bir işveren, aynı işi yapan ve nitelikleri eşit olan işçilerinden kadın olanlara, haklı bir neden bulunmaksızın erkek işçilere göre daha düşük ücret ödemektedir. Bir işçi bu durumu ileri sürerek dava açmıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İşçi, dört aya kadar ücreti tutarındaki tazminat dışında yoksun bırakıldığı haklarını da talep edebilir',
            'B': 'İşçi ihlali güçlü biçimde gösteren bir durumu ortaya koyarsa ispat yükü işverene geçer',
            'C': 'Ayrımcılığın ispat yükü tümüyle işçide olup işveren hiçbir açıklama yapmakla yükümlü değildir',
            'D': 'Aynı veya eşit değerde bir iş için cinsiyet nedeniyle daha düşük ücret kararlaştırılamaz',
            'E': 'İşveren, esaslı sebepler olmadıkça tam süreli–kısmi süreli işçi arasında farklı işlem yapamaz',
        },
        'C',
        '4857 md. 5: işveren, esaslı sebepler olmadıkça tam süreli–kısmi süreli veya belirli süreli–belirsiz süreli işçi arasında farklı işlem yapamaz; aynı veya eşit değerde bir iş için cinsiyet nedeniyle daha düşük ücret kararlaştırılamaz. İhlalde işçi dört aya kadar ücreti tutarında tazminat ve yoksun bırakıldığı hakları talep edebilir. İSPAT YÜKÜ: işçi ihlali güçlü biçimde gösteren bir durumu ortaya koyduğunda, böyle bir ihlalin bulunmadığını ispat yükümlülüğü İŞVERENE geçer.',
    ),
    '0018': patch(
        'Bir işveren, işçisine aylık ücretin bir bölümünü ayni olarak (konut tahsisi ve yemek bedeli) sağlamakta, kalan bölümünü ise banka aracılığıyla ödemektedir. İşçi, ayni yardımların ücret sayılmadığını ileri sürmektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yemek ve konut gibi ayni yardımlar ücretin hesabında hiç dikkate alınmayan, tümüyle sosyal nitelikli yardımlardır',
            'B': 'Ücret kural olarak para ile ödenir; ancak ayni yardımlar geniş anlamda ücretin ekidir ve ücret niteliği taşıyabilir',
            'C': 'İşveren, işçinin rızası bulunmak koşuluyla ücretin tamamını ayni olarak ödemekte serbesttir',
            'D': 'Ücretin banka aracılığıyla ödenmesi hiçbir işyerinde zorunlu değildir',
            'E': 'Ücret yalnızca üçüncü kişiler tarafından sağlanan tutarları kapsar',
        },
        'B',
        '4857 md. 32: ücret, bir kimseye bir iş karşılığında işveren veya üçüncü kişiler tarafından sağlanan ve PARA İLE ÖDENEN tutardır. Ücret yabancı para ya da ayın olarak kararlaştırılamaz; ancak yemek, konut ve yol yardımı gibi ayni sağlamalar geniş anlamda ücretin ekleri sayılır. Ayrıca belirlenen sayının üzerinde işçi çalıştıran işyerlerinde ücretin bankadan ödenmesi zorunludur.',
    ),
    '0019': patch(
        'Bir işyerinde haftalık çalışma süresi 45 saat olarak uygulanmakta ve işyeri haftada altı gün faaliyet göstermektedir. İşveren, günlük çalışma süresini bir gün 12 saat olacak biçimde düzenlemek istemektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Haftalık süre, aksi kararlaştırılmadıkça işyerinde çalışılan günlere eşit olmayan biçimde bölünemez',
            'B': 'Günlük çalışma süresi en çok dokuz saat olup taraf anlaşmasıyla dahi artırılamaz',
            'C': 'Haftalık 45 saat aşılmadığı sürece günlük sürede bir sınır bulunmaz',
            'D': 'Günlük on bir saatlik sınır yalnızca denkleştirme uygulanan işyerlerinde geçerlidir',
            'E': 'Günlük çalışma süresi on bir saati aşamayacağından bu düzenleme yapılamaz',
        },
        'E',
        '4857 md. 63: genel bakımdan çalışma süresi haftada en çok 45 saattir. Aksi kararlaştırılmamışsa bu süre işyerinde haftanın çalışılan günlerine EŞİT ÖLÇÜDE bölünerek uygulanır; ancak tarafların anlaşmasıyla farklı da bölünebilir. Bu hâlde iki aylık süre içinde haftalık ortalama süre aşılmamak koşuluyla günlük çalışma süresi ON BİR SAATİ aşamaz. Altı günlük eşit bölüşümde günlük süre 7,5 saattir.',
    ),
    '0020': patch(
        'İş hukuku ve iş sözleşmesi ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. İşçi, bir iş sözleşmesine dayanarak bağımlı olarak çalışan gerçek kişidir. II. İş sözleşmesinin unsurları iş görme, ücret ve bağımlılıktır. III. Kural olan, belirli süreli iş sözleşmesidir.',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'I, II ve III',
            'E': 'I ve III',
        },
        'B',
        'I doğrudur (4857 md. 2). II doğrudur (md. 8). III YANLIŞTIR: md. 11 uyarınca kural BELİRSİZ süreli iş sözleşmesidir; belirli süreli sözleşme ancak objektif koşulların varlığında yapılabilir.',
    ),
    '0021': patch(
        'Bir işçinin haftalık normal çalışma süresi 45 saat olup, bir hafta 51 saat çalışmıştır. İşçi, fazla çalışma karşılığında ücret yerine serbest zaman kullanmak istediğini bildirmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Fazla çalışma, haftalık kırk beş saati aşan çalışmadır',
            'B': 'Fazla çalışma süresi yılda iki yüz yetmiş saatten fazla olamaz',
            'C': 'Fazla çalışma ücreti normal saat ücretinin yüzde elli fazlasıyla ödenir',
            'D': 'İşçi isterse her fazla çalışma saati için bir saat otuz dakika serbest zaman kullanabilir',
            'E': 'İşçi, fazla çalıştığı her saat karşılığında bir saat serbest zaman kullanır',
        },
        'E',
        '4857 md. 41: fazla çalışma, haftalık 45 saati aşan çalışmalardır ve her saat için normal saat ücretinin YÜZDE ELLİ fazlası ödenir. Ücret yerine serbest zaman seçen işçi, fazla çalıştığı her saat karşılığında BİR SAAT OTUZ DAKİKA serbest zaman kullanır. Fazla çalışma süresi yılda 270 saati aşamaz ve işçinin onayı gerekir.',
    ),
    '0022': patch(
        'Bir işyerinde haftalık çalışma süresi sözleşmeyle 40 saat olarak belirlenmiştir. Bir işçi o hafta toplam 48 saat çalışmıştır. Buna göre işçinin hak edeceği zamlı ücret bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sekiz saatin tamamı yüzde elli zamlı ödenir',
            'B': 'Sözleşmeyle 45 saatin altında süre belirlendiği için fazla çalışma hükümleri uygulanmaz',
            'C': '40–45 saat arasındaki 5 saat yüzde yirmi beş, 45 saati aşan 3 saat yüzde elli zamlı ödenir',
            'D': 'Yalnızca 45 saati aşan 3 saat zamlı ödenir; 40–45 saat arasındaki 5 saat normal ücrete dâhil sayılır',
            'E': 'Sekiz saatin tamamı yüzde yirmi beş zamlı ödenir',
        },
        'C',
        '4857 md. 41: haftalık çalışma süresi sözleşmeyle 45 saatin altında belirlenmişse, bu süreyi aşan ve 45 saate kadar yapılan çalışma FAZLA SÜRELERLE ÇALIŞMA sayılır ve saat ücretinin yüzde YİRMİ BEŞ fazlasıyla ödenir. 45 saati aşan kısım ise fazla çalışmadır ve yüzde ELLİ fazlasıyla ödenir. Olayda 40→45 arası 5 saat %25, 45→48 arası 3 saat %50.',
    ),
    '0023': patch(
        'Bir işçi, aynı işverene ait iki ayrı işyerinde aralıklı olarak toplam 11 ay 20 gün çalışmıştır. İşçi yıllık ücretli izin talep etmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Deneme süresi de dâhil en az bir yıl çalışma koşulu gerçekleşmediğinden işçi henüz yıllık izne hak kazanmamıştır',
            'B': 'Aynı işverene ait farklı işyerlerinde geçen süreler birleştirilmez',
            'C': 'Deneme süresi yıllık izne esas kıdemden düşülür',
            'D': 'İşçi bir yılı doldurmaya yaklaştığı için çalıştığı süreyle orantılı biçimde kısmi yıllık ücretli izne hak kazanmış sayılır',
            'E': 'Yıllık izne hak kazanmak için altı ay çalışmış olmak yeterlidir',
        },
        'A',
        '4857 md. 53-54: işyerinde işe başladığı günden itibaren, deneme süresi de içinde olmak üzere EN AZ BİR YIL çalışmış olan işçilere yıllık ücretli izin verilir. İşçinin aynı işverenin bir veya çeşitli işyerlerinde çalıştığı süreler BİRLEŞTİRİLEREK hesaplanır. Bir yıl dolmadan orantılı izin hakkı doğmaz; niteliği gereği bir yıldan az süren mevsimlik ve kampanya işleri bu hükümlerin dışındadır.',
    ),
    '0024': patch(
        'Bir işyerinde üç işçinin kıdemi sırasıyla 3 yıl, 9 yıl ve 17 yıldır. Üçü de 18 yaşından büyük ve 50 yaşından küçüktür. Buna göre bu işçilerin yıllık ücretli izin süreleri sırasıyla kaç gündür?',
        {
            'A': '15 – 20 – 26',
            'B': '14 – 20 – 26',
            'C': '12 – 18 – 24',
            'D': '14 – 20 – 24',
            'E': '14 – 22 – 26',
        },
        'B',
        '4857 md. 53: hizmet süresi bir yıldan beş yıla kadar (beş yıl dâhil) olanlara 14 günden, beş yıldan fazla on beş yıldan az olanlara 20 günden, on beş yıl ve daha fazla olanlara 26 günden az yıllık ücretli izin verilemez. 3 yıl → 14, 9 yıl → 20, 17 yıl → 26 gün. Ayrıca 18 ve daha küçük yaştaki işçilerle 50 ve daha yukarı yaştaki işçilere verilecek izin 20 günden az olamaz; yer altı işlerinde süreler dörder gün artırılır.',
    ),
    '0025': patch(
        'Bir işçinin işyerindeki kıdemi 8 yıldır ve işçi 42 yaşındadır. İşveren, bu işçinin yıllık iznini iki bölüme ayırarak kullandırmak istemekte; birinci bölümü 8 gün, ikinci bölümü 12 gün olarak planlamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşçinin izin süresi 20 gündür; bölümlerin sayısı taraf iradesine bırakıldığından planlama hukuka uygundur',
            'B': 'İşçinin izin süresi 14 gündür ve planlama hukuka uygundur',
            'C': 'Yıllık izin, tarafların anlaşması olsa da bölümler hâlinde kullandırılamaz',
            'D': 'İşçinin izin süresi 20 gündür; ancak bölümlerden biri 10 günden az olamayacağı için bu planlama yapılamaz',
            'E': 'İşçinin izin süresi 26 gündür ve bölümlerin sayısında sınır yoktur',
        },
        'D',
        '4857 md. 53: beş yıldan fazla on beş yıldan az kıdemi olan işçiye en az 20 gün izin verilir (8 yıl → 20 gün). md. 56: izin, tarafların anlaşmasıyla bölümler hâlinde kullandırılabilir; ancak bölümlerden BİRİ on günden aşağı olamaz. 8 + 12 planında hiçbir bölüm on günün altında görünmese de birinci bölüm 8 gündür ve bu sınırı ihlal eder.',
    ),
    '0026': patch(
        'Bir işyerinde bir işçinin günlük çalışma süresi 7,5 saat, diğer bir işçinin ise 4 saattir. İşveren her iki işçiye de günde 15 dakika ara dinlenmesi vermektedir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Dört saatlik çalışma için 15 dakika yeterlidir; 7,5 saatlik çalışma için ara dinlenmesi en az yarım saat olmalıdır',
            'B': 'Her iki işçi için de 15 dakika yeterlidir',
            'C': 'Ara dinlenmeleri çalışma süresinden sayıldığı için bu sürelerin ücreti işveren tarafından günlük ücrete ek olarak ayrıca ödenir',
            'D': 'Her iki işçi için de ara dinlenmesi en az bir saat olmalıdır',
            'E': 'Ara dinlenmesi süresi işveren tarafından serbestçe belirlenir ve alt sınır yoktur',
        },
        'A',
        '4857 md. 68: ara dinlenmesi, günlük çalışma süresi dört saat veya daha kısa işlerde 15 dakika, dört saatten fazla ve yedi buçuk saate kadar (yedi buçuk saat dâhil) olan işlerde yarım saat, yedi buçuk saatten fazla süreli işlerde bir saattir. Bu süreler en azdır ve aralıksız verilir. Ara dinlenmeleri çalışma süresinden SAYILMAZ.',
    ),
    '0027': patch(
        'Bir işveren, gece döneminde çalışan işçilerini bazı günlerde 9 saat çalıştırmakta, ayrıca 17 yaşındaki bir genç işçiyi de gece postasında görevlendirmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Gece dönemi, en geç saat 20.00'de başlayarak en erken saat 06.00'ya kadar geçen süreyi ifade eder",
            'B': 'İşçilerin gece çalışmaları günde yedi buçuk saati geçemez',
            'C': 'Gece ve gündüz postalarında çalışan işçilerin posta değişiminde kesintisiz en az on bir saat dinlendirilmesi gerekir',
            'D': 'On sekiz yaşını doldurmamış çocuk ve genç işçilerin gece çalıştırılması yasaktır',
            'E': 'Gece çalışmasında günlük süre, işin niteliği gerektiriyorsa işçinin onayı aranmaksızın dokuz saate kadar uzatılabilir',
        },
        'E',
        "4857 md. 69: çalışma hayatında gece, en geç saat 20.00'de başlayarak en erken 06.00'ya kadar geçen ve her hâlde en fazla on bir saat süren dönemdir. İşçilerin gece çalışmaları YEDİ BUÇUK SAATİ GEÇEMEZ (turizm, özel güvenlik ve sağlık hizmeti gibi işlerde işçinin yazılı onayıyla istisna öngörülmüştür); genel bir 'dokuz saate uzatma' kuralı yoktur. md. 73: 18 yaşını doldurmamış çocuk ve genç işçilerin gece çalıştırılması yasaktır.",
    ),
    '0028': patch(
        'Bir işyerinde risk değerlendirmesi yapılmamış, çalışanlara iş sağlığı ve güvenliği eğitimi verilmemiş ve koruyucu donanım temin edilmemiştir. İşveren, çalışanların da kendi güvenliklerinden sorumlu olduğunu, bu nedenle yükümlülüğün paylaşıldığını ileri sürmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İşveren, çalışanlara iş sağlığı ve güvenliği eğitimi vermekle yükümlüdür',
            'B': 'İşveren, çalışanların iş sağlığı ve güvenliğini sağlamak için gerekli her türlü önlemi almakla yükümlüdür',
            'C': 'İşveren risk değerlendirmesi yapmak ve yaptırmakla yükümlüdür',
            'D': 'Çalışanların kendi güvenliklerine ilişkin yükümlülükleri, işverenin sorumluluğunu bu oranda azaltır',
            'E': 'İş sağlığı ve güvenliği önlemlerinin maliyeti çalışanlara yansıtılamaz',
        },
        'D',
        '6331 sayılı İş Sağlığı ve Güvenliği Kanunu md. 4 ve 19: işveren çalışanların sağlık ve güvenliğini sağlamak için gerekli her türlü önlemi almak, risk değerlendirmesi yapmak ve eğitim vermekle yükümlüdür; md. 4/2 uyarınca çalışanların yükümlülükleri işverenin sorumluluğunu ETKİLEMEZ. md. 19/3: önlemlerin maliyeti çalışanlara yansıtılamaz.',
    ),
    '0029': patch(
        'Çalışma süreleri ve izinler ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Yıllık ücretli izne hak kazanmak için en az altı ay çalışmış olmak yeterlidir. II. Genel bakımdan haftalık çalışma süresi en çok kırk beş saattir. III. Fazla çalışma, haftalık kırk beş saati aşan çalışmadır. IV. Ara dinlenmeleri çalışma süresinden sayılır.',
        {
            'A': 'Yalnız I',
            'B': 'I, II ve IV',
            'C': 'II ve III',
            'D': 'III ve IV',
            'E': 'I ve IV',
        },
        'E',
        'I YANLIŞ: 4857 md. 53 uyarınca yıllık izne hak kazanmak için deneme süresi dâhil EN AZ BİR YIL çalışmış olmak gerekir. IV YANLIŞ: md. 68 uyarınca ara dinlenmeleri çalışma süresinden SAYILMAZ. II (md. 63) ve III (md. 41) doğrudur.',
    ),
    '0030': patch(
        'Bir işveren, işçisiyle çağrı üzerine çalışmaya dayalı yazılı bir iş sözleşmesi yapmış; ancak sözleşmede işçinin haftalık ne kadar süreyle çalışacağını belirlememiştir. İşveren, işçiyi çalışacağı günden bir gün önce telefonla çağırmıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Çağrı üzerine çalışmada sözleşmenin yazılı yapılması gerekir',
            'B': 'Haftalık süre belirlenmediğinden işçi yalnızca fiilen çağrıldığı saatlerin ücretine hak kazanır',
            'C': 'Aksi kararlaştırılmadıkça işçi, çağrının kendisine en az dört gün önceden yapılmasını isteme hakkına sahiptir',
            'D': 'Haftalık çalışma süresi belirlenmemişse haftada yirmi saat kararlaştırılmış sayılır',
            'E': 'İşçi, çağrılmadığı hâlde bu sürenin ücretine hak kazanır',
        },
        'B',
        '4857 md. 14: çağrı üzerine çalışmada sözleşme yazılı yapılır. Hafta, ay veya yıl gibi bir zaman dilimi içinde çalışacağı süre belirlenmemişse haftalık çalışma süresi YİRMİ SAAT kararlaştırılmış sayılır ve işçi çağrılsın çağrılmasın bu sürenin ücretine hak kazanır. Çağrı, aksi kararlaştırılmadıkça dört gün önce yapılır.',
    ),
    '0031': patch(
        'Bir işverenin işçisine ait ücreti ödemesi 25 gün gecikmiştir. İşçi, ücreti ödenene kadar iş görme borcunu yerine getirmeyeceğini bildirmiştir. İşveren ise bu davranışı devamsızlık sayarak sözleşmeyi feshetmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşçi ücret ödenmese de iş görme borcunu yerine getirmelidir',
            'B': 'İşçi yalnızca dava açabilir; çalışmaktan kaçınma hakkı bulunmaz',
            'C': 'Bu hakkın doğması için gecikmenin en az iki ay sürmesi gerekir',
            'D': 'Ücreti ödeme gününden itibaren yirmi gün içinde ödenmeyen işçi iş görmekten kaçınabilir; bu davranış devamsızlık sayılmaz',
            'E': 'İşçinin iş görmekten kaçınma hakkı ancak toplu hâlde kullanılırsa geçerli olur; bireysel olarak kullanılması devamsızlık sayılır',
        },
        'D',
        '4857 md. 34: ücreti ödeme gününden itibaren YİRMİ GÜN içinde mücbir bir neden dışında ödenmeyen işçi, iş görme borcunu yerine getirmekten kaçınabilir. Bu nedenle kişisel kararlarına dayanarak iş görme borcunu yerine getirmemeleri sayısal olarak toplu bir nitelik kazansa dahi GREV SAYILMAZ ve bu işçilerin sözleşmeleri çalışmadıkları için feshedilemez. Ayrıca md. 32 uyarınca ücret en geç ayda bir ödenir.',
    ),
    '0032': patch(
        'Bir işveren, işten ayrılan işçisiyle, ülke genelinde ve beş yıl süreyle aynı sektörde çalışmamasını öngören yazılı bir rekabet yasağı sözleşmesi yapmıştır. İşçi, müşteri çevresine nüfuz edebilecek bir pozisyonda çalışmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yazılı yapıldığı için sözleşme her koşulda geçerlidir',
            'B': 'Rekabet yasağı süre, yer ve konu bakımından aşırıdır; hâkim yasağı sınırlayabilir ve süre özel durum yoksa iki yılı aşamaz',
            'C': 'Rekabet yasağı sözleşmesi işçinin ehliyeti aranmaksızın geçerli olur',
            'D': 'Rekabet yasağı ancak işçi haklı nedenle istifa etmişse hüküm ifade eder',
            'E': "Rekabet yasağı 4857 sayılı İş Kanunu'nda düzenlenmiş olup süresi özel durumlarda beş yıla kadar serbestçe kararlaştırılabilir",
        },
        'B',
        "Rekabet yasağı 4857 sayılı Kanun'da DEĞİL, TBK md. 444-447'de düzenlenmiştir. Geçerlilik için işçinin fiil ehliyeti, yazılı şekil ve işçinin müşteri çevresine ya da üretim sırlarına nüfuz edebilmesi aranır. Yasak, işçinin ekonomik geleceğini hakkaniyete aykırı biçimde tehlikeye düşürecek biçimde sınırlandırılamaz; süre, yer ve işlerin türü bakımından uygun sınırı aşamaz ve özel durum yoksa İKİ YILI aşamaz. Hâkim aşırı yasağı sınırlayabilir (md. 445).",
    ),
    '0033': patch(
        'Bir işveren, işçisine sözleşmede ve işyeri uygulamasında yer almayan, ayrıca işçinin sağlığı bakımından tehlike doğuran bir işi yapmasını emretmiştir. İşçi bu talimata uymamıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşçi talimata uymayarak devamsızlık yapmış sayılır',
            'B': 'İşçi ancak talimatın yazılı verilmesi hâlinde itiraz edebilir',
            'C': 'İtaat borcu yalnızca belirsiz süreli sözleşmelerde geçerlidir',
            'D': 'İtaat borcu mutlak niteliktedir; işçi, işverenin verdiği her talimata içeriğine ve sonuçlarına bakmaksızın uymakla yükümlüdür',
            'E': 'İşçi, hukuka ve sözleşmeye aykırı ya da sağlığı için tehlike doğuran talimatlara uymak yükümlülüğünde değildir',
        },
        'E',
        'İtaat borcu (TBK md. 399), işverenin işin görülmesi ve işçilerin davranışlarına ilişkin genel düzenlemelerine ve özel talimatlarına uymayı kapsar; ancak talimat yetkisi HUKUKA, sözleşmeye ve dürüstlük kuralına uygun olmakla sınırlıdır. İşçinin sağlığını tehlikeye düşüren ya da sözleşme kapsamı dışındaki talimatlar bağlayıcı değildir; ayrıca 6331 sayılı Kanun md. 13 işçiye çalışmaktan kaçınma hakkı tanır.',
    ),
    '0035': patch(
        'Bir işçi, ulusal bayram günü işverenin talebi ve kendi onayıyla çalışmıştır. İşveren, o gün için işçiye yalnızca normal günlük ücretini ödemiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşçiye yalnızca yüzde elli zamlı ücret ödenir',
            'B': 'Ulusal bayram günü çalışması fazla çalışma sayılır ve yıllık 270 saatlik sınıra dâhildir',
            'C': 'İşçi, çalışmasa da alacağı bir günlük ücretin yanında çalıştığı her gün için ayrıca bir günlük ücrete daha hak kazanır',
            'D': 'Ödeme doğrudur; ulusal bayram günü çalışan işçiye tek günlük ücret ödenir',
            'E': 'Ulusal bayram ve genel tatil günlerinde işçinin onayı aranmaksızın çalıştırma yapılabilir; onay yalnızca fazla çalışmada gerekir',
        },
        'C',
        '4857 md. 44 ve 47: ulusal bayram ve genel tatil günlerinde işyerlerinde çalışılıp çalışılmayacağı sözleşmelerle belirlenir; sözleşmede hüküm yoksa çalışılması için işçinin ONAYI gerekir. Bu günlerde çalışılmazsa bir iş karşılığı olmaksızın o günün ücreti tam ödenir; çalışılırsa AYRICA çalışılan her gün için bir günlük ücret daha ödenir. Bu çalışma fazla çalışma sayılmaz.',
    ),
    '0036': patch(
        'İşçinin ve işverenin borçları ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. İşçinin aylık ücretinin dörtte birinden fazlası haczedilemez ve takas edilemez. II. Ücret kesme cezası bir ayda iki gündelikten fazla olamaz. III. İşveren, işçinin ücretini en geç üç ayda bir ödemekle yükümlüdür. IV. İşverenin gözetme borcu, işçinin birlikte kusuru bulunduğunda tümüyle ortadan kalkar.',
        {
            'A': 'III ve IV',
            'B': 'I, III ve IV',
            'C': 'I, II ve III',
            'D': 'I ve II',
            'E': 'II ve IV',
        },
        'D',
        "I doğrudur (4857 md. 35), II doğrudur (md. 38). III YANLIŞ: md. 32'ye göre ücret en geç AYDA BİR ödenir; iş sözleşmeleri veya toplu iş sözleşmeleriyle ödeme süresi bir haftaya kadar indirilebilir. IV YANLIŞ: işçinin birlikte kusuru tazminatta indirim nedenidir, işverenin gözetme borcunu ortadan kaldırmaz.",
    ),
    '0037': patch(
        "Bir üretim işletmesinin fabrika binası, aynı işverene ait ve fabrikaya bağlı olarak kullanılan depo, dinlenme yeri ve yemekhane ile birlikte faaliyet göstermektedir. Buna göre 4857 sayılı Kanun'un 'işyeri' tanımı bakımından aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'İşyeri kavramı yalnızca işin fiilen görüldüğü üretim binasını kapsar',
            'B': 'İşyeri, işveren tarafından mal veya hizmet üretmek amacıyla maddi ve maddi olmayan unsurlarla işçinin birlikte örgütlendiği birimdir',
            'C': 'Dinlenme yeri, yemekhane ve depo gibi eklentiler işyerinden sayılır',
            'D': 'İşyeri, bağlı yerler ve eklentilerle bir bütün olarak değerlendirilir',
            'E': 'İşin niteliği ve yürütümü bakımından işyerine bağlı yerler işyerinden sayılır',
        },
        'A',
        '4857 md. 2: işyeri, işveren tarafından mal veya hizmet üretmek amacıyla maddi olan ve olmayan unsurlar ile işçinin birlikte örgütlendiği birimdir. İşyerine bağlı yerler, eklentiler ve araçlar da işyerinden sayılır ve işyeri bu unsurlarla BİR BÜTÜNDÜR; kavram yalnızca üretim binasıyla sınırlı değildir.',
    ),
    '0038': patch(
        'Bir işçi, kendisine teslim edilen makineyi kullanım talimatına aykırı biçimde çalıştırarak arızalanmasına yol açmıştır. İşveren, zararın tamamının işçiden tahsil edilmesi gerektiğini ileri sürmektedir. Buna göre işçinin özen borcu bakımından aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İşçinin özen borcu yalnızca kendisine ait araçlar bakımından söz konusu olur',
            'B': 'Zararın tamamı, işçinin kusur derecesine bakılmaksızın ücretinden kesilir',
            'C': 'İşçi, işi özenle görmek ve işverene verdiği kusurlu zarardan sorumlu olmakla birlikte sorumluluğun ölçüsü işin tehlikesi ve işçinin niteliği gözetilerek belirlenir',
            'D': 'İşçi, ağır kusuru bulunsa bile verdiği zarardan sorumlu tutulamaz',
            'E': 'İşçi, kendisine teslim edilen araç ve gereçler bakımından kusursuz sorumluluk esasına tabi olduğundan meydana gelen her zarardan kusuru aranmaksızın sorumludur',
        },
        'C',
        "TBK md. 396 ve 400: işçi, yüklendiği işi özenle yapmak ve işverenin haklı çıkarını korumakla yükümlüdür; işverene kusuruyla verdiği zarardan sorumludur. Sorumluluğun belirlenmesinde işin tehlikeli olup olmadığı, uzmanlığı ve işçiden beklenen yetenek gözetilir. Kusursuz sorumluluk söz konusu değildir; ayrıca ücretten kesinti 4857 md. 35'teki dörtte bir sınırına tabidir.",
    ),
    '0039': patch(
        'İş sözleşmesi türleri ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. Belirli süreli iş sözleşmesi, objektif bir neden bulunmasa da tarafların anlaşmasıyla yapılabilir. II. Kısmi süreli iş sözleşmesiyle çalışan işçi, ayrımı haklı kılan bir neden olmadıkça tam süreli emsal işçiye göre farklı işleme tabi tutulamaz. III. Çağrı üzerine çalışmada sözleşmenin yazılı yapılması gerekir. IV. Deneme süresi, toplu iş sözleşmesi bulunmayan işyerlerinde dört aya kadar kararlaştırılabilir.',
        {
            'A': 'II, III ve IV',
            'B': 'I ve IV',
            'C': 'Yalnız I',
            'D': 'II ve III',
            'E': 'I, II ve IV',
        },
        'B',
        "I YANLIŞ: 4857 md. 11 belirli süreli sözleşme için objektif koşul arar; kural belirsiz süreli sözleşmedir. IV YANLIŞ: md. 15'e göre deneme süresi en çok iki aydır ve dört aya kadar uzatma yalnızca TOPLU İŞ SÖZLEŞMESİYLE mümkündür. II doğrudur (md. 13), III doğrudur (md. 14). Bu nedenle yanlış olanlar I ve IV'tür.",
    ),
    '0040': patch(
        'İşçinin ve işverenin borçları ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. İşçinin borçları arasında sadakat ve özen borcu yer alır. II. İşverenin borçları arasında ücret ödeme ve işçiyi gözetme yer alır. III. İşveren, haklı bir neden olmadıkça işçileri arasında ayrım yapamaz.',
        {
            'A': 'I ve II',
            'B': 'Yalnız I',
            'C': 'I ve III',
            'D': 'II ve III',
            'E': 'I, II ve III',
        },
        'E',
        'Üç ifade de doğrudur. İşçinin borçları iş görme, sadakat, özen ve itaattir (TBK md. 395-399); işverenin borçları ücret ödeme (4857 md. 32), gözetme (TBK md. 417), eşit davranma (4857 md. 5) ve iş sağlığı ve güvenliği önlemlerini almadır (6331 md. 4).',
    ),
    '0041': patch(
        'Bir işveren, işçisinin aylık net 30.000 ₺ tutarındaki ücretinden, işyerinde verdiği zarar gerekçesiyle 12.000 ₺ kesinti yapmış; ayrıca aynı ay içinde işçiye disiplin gerekçesiyle üç günlük ücreti tutarında ücret kesme cezası uygulamıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Ücret kesme cezasının işçiye derhâl ve nedenleriyle birlikte bildirilmesi gerekir',
            'B': 'İşveren, işçinin verdiği zarar tutarını ücretten sınırsız biçimde takas edebilir',
            'C': 'Kesilen ücret cezaları işçilerin eğitimi ve sosyal hizmetleri için kullanılır',
            'D': 'İşçi ücretinin dörtte birinden fazlası haczedilemez, başkasına devredilemez ve takas edilemez',
            'E': 'Ücret kesme cezası bir ayda iki gündelikten fazla olamaz',
        },
        'B',
        "4857 md. 35: işçinin aylık ücretinin DÖRTTE BİRİNDEN fazlası haczedilemez, başkasına devredilemez ve takas edilemez (nafaka borcu ayrıktır). 12.000 ₺ kesinti, 30.000 ₺'nin dörtte biri olan 7.500 ₺'yi aşar. md. 38: ücret kesme cezası bir ayda iki gündelikten fazla olamaz ve işçiye derhâl nedenleriyle bildirilir; kesilen tutarlar Çalışma ve Sosyal Güvenlik Bakanlığı hesabına yatırılarak işçilerin eğitimi ve sosyal hizmetleri için kullanılır.",
    ),
    '0042': patch(
        'Bir işveren, işin niteliği süreklilik gösterdiği hâlde işçisiyle art arda üç kez birer yıllık belirli süreli iş sözleşmesi yapmış, her defasında esaslı bir neden göstermemiştir. Üçüncü yılın sonunda sözleşmenin süresinin dolduğunu bildirerek ilişkiyi sona erdirmiştir. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sözleşmeler başlangıçtan itibaren belirsiz süreli kabul edilir; sona erdirme fesih niteliğindedir',
            'B': 'Zincirleme sözleşme yasağı yalnızca yazılı sözleşmeler için uygulanır',
            'C': 'Her sözleşme kendi süresiyle bağlı olduğundan süre bitiminde ilişki kendiliğinden sona erer ve işçi kıdem tazminatına hak kazanmaz',
            'D': 'Yalnızca son sözleşme belirsiz süreliye dönüşür, önceki iki yıl kıdemden sayılmaz',
            'E': 'İşçi itiraz etmediği için sözleşmeler belirli süreli niteliğini korur',
        },
        'A',
        '4857 md. 11/2-3: belirli süreli iş sözleşmesi esaslı bir neden olmadıkça birden fazla üst üste (zincirleme) yapılamaz; aksi hâlde sözleşme BAŞLANGIÇTAN İTİBAREN belirsiz süreli kabul edilir. Bunun sonucu olarak işçinin kıdemi ilk sözleşmeden itibaren hesaplanır ve ilişkinin sona erdirilmesi süre bitimi değil FESİH sayılır.',
    ),
    '0043': patch(
        'Bir işyerinde taraflar yazılı olarak denkleştirme uygulaması kararlaştırmıştır. İşçi ilk hafta 52 saat, ikinci hafta 38 saat çalışmıştır. İşyerinde toplu iş sözleşmesi bulunmamaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Denkleştirme yalnızca işverenin tek taraflı kararıyla uygulanabilir',
            'B': 'Denkleştirmede günlük çalışma süresi sınırlaması uygulanmaz',
            'C': 'İlk haftada 45 saati aşan 7 saat için yüzde elli zamlı fazla çalışma ücreti ödenmelidir',
            'D': 'Denkleştirme süresi toplu iş sözleşmesi olmasa da dört aydır',
            'E': 'Denkleştirme süresi içinde haftalık ortalama 45 saati aşmadığından fazla çalışma doğmaz',
        },
        'E',
        '4857 md. 63: tarafların yazılı anlaşmasıyla haftalık normal çalışma süresi işyerinde haftanın çalışılan günlerine farklı biçimde dağıtılabilir. Bu hâlde İKİ AYLIK süre içinde işçinin haftalık ortalama çalışma süresi normal haftalık süreyi aşamaz (denkleştirme süresi toplu iş sözleşmesiyle dört aya kadar artırılabilir). Ortalama (52 + 38) / 2 = 45 saat olduğundan fazla çalışma doğmaz. Günlük 11 saat sınırı burada da geçerlidir.',
    ),
    '0044': patch(
        'İş hukukunun niteliği ve yorum yöntemi tartışılırken, bir sözleşme hükmünün hem işçi hem işveren lehine yorumlanabilecek biçimde açık olmadığı görülmüştür. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tereddüt hâlinde hüküm işçi yararına yorumlanır',
            'B': 'İş hukuku, hem kamu hukuku hem de özel hukuk özellikleri taşıyan karma nitelikte bir hukuk dalıdır',
            'C': 'İşçi lehine yorum ilkesi, hükmü açık olan kurallarda da işçi yararına sonuç doğuracak biçimde uygulanır',
            'D': 'İş hukuku, işçinin korunması amacına dayanan bir hukuk dalıdır',
            'E': 'Kanunun işçi lehine getirdiği kurallar nispi emredici nitelikte olup sözleşmeyle işçi lehine değiştirilebilir',
        },
        'C',
        'İş hukuku, işçinin korunması amacına dayanan ve kamu hukuku–özel hukuk özelliklerini birlikte taşıyan karma bir daldır. İŞÇİ LEHİNE YORUM ilkesi, ancak hükmün anlamı TEREDDÜTLÜ olduğunda devreye girer; açık ve tereddütsüz bir hükmün işçi yararına eğilip bükülmesine izin vermez. Nispi emredici kurallar sözleşmeyle işçi lehine değiştirilebilir, aleyhine değiştirilemez.',
    ),
    '0045': patch(
        'Bir iş sözleşmesinde, işçinin yıllık ücretli izin süresinin kanunda öngörülenden 4 gün az olacağı; buna karşılık işçiye kanunda öngörülenden yüksek bir ücret ödeneceği kararlaştırılmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sözleşmenin tamamı geçersiz olur',
            'B': 'İşçiye yüksek ücret ödendiği için izin hükmü de geçerli sayılır',
            'C': 'Sözleşme, işçi itiraz etmediği sürece bütünüyle uygulanır',
            'D': 'İzne ilişkin hüküm işçi aleyhine olduğu için geçersizdir ve yerine kanunun emredici hükmü uygulanır; yüksek ücrete ilişkin hüküm geçerliliğini korur',
            'E': 'İzin hükmü geçerlidir; işçiye sağlanan yüksek ücret karşılığında taraflar sözleşme serbestisi içinde izin süresini kanunun altında kararlaştırabilir',
        },
        'D',
        "İş hukukunda kanunun işçi lehine öngördüğü kurallar NİSPİ EMREDİCİ niteliktedir: sözleşmeyle işçi LEHİNE değiştirilebilir, aleyhine değiştirilemez. Aleyhe olan hüküm geçersiz sayılır ve yerini kanunun asgari kuralı alır (kısmi geçersizlik); sözleşmenin tamamı ayakta kalır. Lehe olan yüksek ücret kaydı geçerlidir. Yıllık izin süresinin azaltılması 4857 md. 53'e aykırıdır.",
    ),
    '0046': patch(
        'İş sözleşmesi sona eren bir işçi, işvereninden yaptığı işin türünü ve süresini gösteren bir belge istemiştir. İşveren, belgeyi vermemiş ve işçinin bu talebini reddetmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Belgenin vaktinde verilmemesinden zarar gören işçi tazminat isteyebilir',
            'B': 'Çalışma belgesi yalnızca işveren tarafından haklı nedenle feshedilen işçilere verilir',
            'C': 'Belgede doğru olmayan bilgi bulunmasından zarar gören üçüncü kişiler de tazminat isteyebilir',
            'D': 'İşten ayrılan işçiye, işinin türünü ve süresini gösteren bir çalışma belgesi verilir',
            'E': 'Çalışma belgesi düzenlenmesi işverenin yükümlülüğüdür',
        },
        'B',
        '4857 md. 28: işten ayrılan işçiye, işveren tarafından işinin çeşidinin ne olduğunu ve süresini gösteren bir belge verilir. Belge her türlü resim ve harçtan muaftır. Belgenin vaktinde verilmemesinden veya belgede doğru olmayan bilgi bulunmasından zarar gören işçi ya da işçiyi işine alan yeni işveren, eski işverenden tazminat isteyebilir. Belge, fesih türüne veya kime ait olduğuna bakılmaksızın verilir.',
    ),
    '0048': patch(
        'Bir işyeri, tüm bölümleriyle birlikte bir başka işverene devredilmiştir. Devir tarihinde işyerinde çalışan bir işçinin birikmiş kıdem tazminatı ve ücret alacakları bulunmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Devirden önce doğmuş ve muaccel olmuş borçlardan devreden işveren devralanla birlikte iki yıl sorumludur',
            'B': 'İşçinin kıdemi, devreden işveren yanındaki çalışmasının başlangıcına göre hesaplanır',
            'C': 'Devir, işçi veya işveren için başlı başına haklı ya da geçerli fesih nedeni oluşturur',
            'D': 'İş sözleşmeleri bütün hak ve borçlarıyla birlikte devralana geçer',
            'E': 'Devir nedeniyle iş sözleşmesinin devamı için işçinin ayrıca onayı aranmaz',
        },
        'C',
        '4857 md. 6: işyeri devredildiğinde devir tarihinde mevcut olan iş sözleşmeleri bütün hak ve borçlarıyla devralana geçer; işçinin kıdemi devreden yanındaki işe başlama tarihine göre hesaplanır. Devirden önce doğmuş ve devir tarihinde ödenmesi gereken borçlardan devreden işveren devralanla birlikte İKİ YIL süreyle müteselsilen sorumludur. Devir, işçi veya işveren bakımından BAŞLI BAŞINA fesih nedeni OLUŞTURMAZ.',
    ),
    '0049': patch(
        "Aşağıdakilerden hangisi 4857 sayılı İş Kanunu'nun uygulama alanı dışında kalır?",
        {
            'A': 'Elli işçi çalıştıran ve üç vardiya usulüyle üretim yapan bir tekstil fabrikasındaki dokuma işleri',
            'B': 'Bir inşaat şirketinin şantiyesinde çalışan düz işçiler ve kalıp ustaları',
            'C': 'Bir otelin mutfak bölümünde çalışan aşçılar',
            'D': 'Bir ailenin üyeleri arasında, dışarıdan kimse katılmaksızın evde yapılan el sanatları işi',
            'E': 'Bir market zincirinin lojistik merkezindeki depo biriminde çalışan yükleme işçileri',
        },
        'D',
        "4857 md. 4: aile ekonomisi sınırları içinde kalan tarımla ilgili her çeşit yapı işleri, bir ailenin üyeleri ve üçüncü dereceye kadar hısımları arasında dışarıdan başka biri katılmayarak evlerde ve el sanatlarının yapıldığı işler bu Kanunun kapsamı dışındadır. Diğer seçenekler İş Kanunu'na tabi işyerleridir.",
    ),
    '0050': patch(
        'İş sözleşmesi ve çalışma koşulları ile ilgili aşağıdaki ifadelerden hangileri doğrudur? I. Fazla çalışma ücreti, normal saat ücretinin yüzde elli fazlasıyla ödenir. II. Deneme süresi en çok dört ay olarak kararlaştırılabilir. III. İşyeri devrinde iş sözleşmeleri bütün hak ve borçlarıyla devralana geçer. IV. Çalışma koşullarında esaslı değişiklik işçiye sözlü olarak bildirilebilir.',
        {
            'A': 'I, II ve III',
            'B': 'III ve IV',
            'C': 'Yalnız I',
            'D': 'I ve III',
            'E': 'II ve IV',
        },
        'D',
        'I doğrudur (4857 md. 41). III doğrudur (md. 6). II YANLIŞ: md. 15 uyarınca deneme süresi en çok İKİ AY olup yalnızca toplu iş sözleşmesiyle dört aya kadar uzatılabilir. IV YANLIŞ: md. 22 esaslı değişikliğin YAZILI bildirilmesini arar; aksi hâlde değişiklik işçiyi bağlamaz.',
    ),
    '0051': patch(
        'Bir işyerinde çalışan işçi, yedi günlük bir zaman dilimi içinde kesintisiz 20 saat dinlendirilmiş; işveren bu sürenin yeterli olduğunu ileri sürmüştür. İşçi o hafta kanunen çalışması gereken günlerde çalışmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Hafta tatilinde çalışılmadığı için ücret ödenmez',
            'B': 'Hafta tatilinin kesintisiz olması gerekmez; yedi günlük dilim içinde parçalar hâlinde de verilebilir',
            'C': 'Hafta tatili en az kesintisiz yirmi dört saat olmalıdır; işçi çalışmasa da bir günlük ücrete hak kazanır',
            'D': 'Yedi günlük dilim içinde verilen yirmi saatlik kesintisiz dinlenme hafta tatili yükümlülüğünü karşılar',
            'E': 'Hafta tatili ücreti yalnızca o hafta fazla çalışma yapan işçilere ödenir',
        },
        'C',
        '4857 md. 46: bu Kanun kapsamına giren işyerlerinde işçilere, tatil gününden önce belirlenen iş günlerinde çalışmış olmaları koşuluyla yedi günlük bir zaman dilimi içinde KESİNTİSİZ EN AZ YİRMİ DÖRT SAAT dinlenme (hafta tatili) verilir. Çalışılmayan hafta tatili günü için işveren bir iş karşılığı olmaksızın o günün ücretini tam olarak öder.',
    ),
    '0052': patch(
        'Bir işveren, işçisinin yıllık ücretli izin süresine denk gelen ulusal bayram ve hafta tatili günlerini izin süresinden saymış; ayrıca izin dönemine ilişkin ücreti izin bitiminde ödemiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İşçi, izin süresi içinde ücret karşılığı bir işte çalışırsa işveren ödediği izin ücretini geri isteyebilir',
            'B': 'İzin süresine rastlayan hafta tatili ve genel tatil günleri izin süresinden sayılmaz ve süre o kadar uzar',
            'C': 'Yıllık ücretli izin işveren tarafından bölünemez; kural olarak sürekli kullandırılır',
            'D': 'İşveren, izin ücretini ilgili işçinin izne başlamasından önce peşin ödemek veya avans olarak vermekle yükümlüdür',
            'E': 'İzin süresine rastlayan ulusal bayram ve hafta tatili günleri izin süresinden sayılır',
        },
        'E',
        '4857 md. 56: yıllık ücretli izin işveren tarafından bölünemez ve sürekli olarak kullandırılır. İzin süresine rastlayan hafta tatili, ulusal bayram ve genel tatil günleri izin süresinden SAYILMAZ; süre bu kadar uzar. md. 57: işveren izin ücretini izne başlamadan ÖNCE peşin ödemek veya avans olarak vermekle yükümlüdür. md. 58: izinde ücretli işte çalışan işçinin izin ücreti geri alınabilir.',
    ),
    '0053': patch(
        'Bir işveren, işyerinde asıl iş olan montaj bölümünü, işletmenin ve işin gereği ile teknolojik nedenlerle uzmanlık gerektiren bir iş bulunmamasına rağmen alt işverene vermiştir. Alt işverenin çalıştırdığı işçiler, daha önce asıl işverenin işçisi olarak aynı işi yapan kişilerdir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Muvazaanın tespiti hâlinde işçiler alt işverenin işçisi sayılmaya devam eder ve yalnızca tazminat isteyebilir',
            'B': 'Daha önce o işyerinde çalışmış olanlar, hakları kısıtlanmak amacıyla alt işveren işçisi olarak yeniden çalıştırılamaz',
            'C': 'Muvazaanın tespiti hâlinde işçiler başlangıçtan itibaren asıl işverenin işçisi sayılır',
            'D': 'Asıl işin bölünerek alt işverene verilmesi kural olarak yasaktır',
            'E': 'İşçilerin hakları kısıtlanamaz; aksi düzenleme muvazaa karinesi doğurur',
        },
        'A',
        '4857 md. 2/7: asıl işin bölünerek alt işverene verilmesi, işletmenin ve işin gereği ile teknolojik nedenlerle uzmanlık gerektirme koşulu yoksa mümkün değildir. Daha önce o işyerinde çalışmış olanlar alt işveren işçisi olarak çalıştırılamaz. Muvazaa tespit edilirse işçiler BAŞLANGIÇTAN İTİBAREN asıl işverenin işçisi sayılır.',
    ),
    '0055': patch(
        'Bir işyerinde gerekli iş sağlığı ve güvenliği önlemleri alınmamış, bu nedenle bir işçi iş kazası geçirerek yaralanmıştır. İşveren, işçinin de dikkatsiz davrandığını ve koruyucu ekipmanı kullanmadığını ileri sürmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Gözetme borcunun ihlali işverenin maddi ve manevi tazminat sorumluluğunu doğurabilir',
            'B': 'İşveren araç ve gereçleri noksansız bulundurmak ve kullanımını denetlemekle yükümlüdür',
            'C': 'İşveren, işçinin sağlığını ve güvenliğini korumak için gerekli her türlü önlemi almakla yükümlüdür',
            'D': 'İşçinin kusuru bulunduğunda işverenin gözetme borcu tümüyle ortadan kalkar',
            'E': 'İşçinin birlikte kusuru tazminattan indirim nedeni olabilir',
        },
        'D',
        'İşverenin gözetme (koruma) borcu TBK md. 417 ve 6331 sayılı Kanun uyarınca, işçinin yaşamını, sağlığını ve bedensel bütünlüğünü korumak için gerekli her türlü önlemi almayı kapsar. İşçinin birlikte kusuru tazminatta İNDİRİM nedeni olabilir; ancak işverenin yükümlülüğünü tümüyle ortadan kaldırmaz.',
    ),
    '0056': patch(
        'Bir uyuşmazlıkta uygulanacak toplu iş sözleşmesi hükmünün anlamı tereddütlüdür; hüküm hem işçi hem işveren yararına yorumlanmaya elverişlidir. Aynı uyuşmazlıkta, anlamı tereddüde yer bırakmayacak biçimde açık olan ikinci bir hüküm daha bulunmaktadır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tereddütlü hüküm geçersiz sayılarak uyuşmazlık dışında bırakılır',
            'B': 'Tereddütlü hüküm işçi lehine yorumlanır; açık olan hüküm ise yorum yoluyla değiştirilemez',
            'C': 'Her iki hüküm de işçi lehine yorumlanır',
            'D': 'Tereddüt hâlinde hüküm, sözleşmeyi kaleme alan taraf aleyhine yorumlanamaz',
            'E': 'İşçi lehine yorum ilkesi yalnızca iş sözleşmelerinde geçerli olup toplu iş sözleşmelerinde uygulanmaz',
        },
        'B',
        'İşçi lehine yorum ilkesi, iş hukukunun işçiyi koruma amacının bir sonucudur; ancak yalnızca hükmün anlamı TEREDDÜTLÜ olduğunda devreye girer. Açık ve tereddütsüz bir hüküm yorum yoluyla işçi yararına eğilip bükülemez; aksi hâlde yorum değil kural koyma söz konusu olur. İlke iş sözleşmelerinde olduğu gibi toplu iş sözleşmelerinde de geçerlidir.',
    ),
    '0057': patch(
        'Bir işveren, on altı yaşındaki bir genç işçiyle yasal temsilcisinin izni olmaksızın iş sözleşmesi yapmış; ayrıca sözleşmenin kurulmasında işçiyi ücret konusunda yanıltmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'On altı yaşındaki kişi, yasal temsilcisi izin verse dahi iş sözleşmesi yapma ehliyetinden yoksundur',
            'B': 'Ücret konusunda yanıltma, iş sözleşmesinin baştan itibaren kesin hükümsüz sayılması sonucunu doğurur ve ayrıca iptal davası açılamaz',
            'C': 'İş sözleşmesi yalnızca tam ehliyetli kişilerle kurulabilir',
            'D': 'İş sözleşmesinde irade sakatlığı hükümleri uygulanmaz',
            'E': 'Sınırlı ehliyetsizin sözleşmesi yasal temsilcinin iznine bağlıdır ve irade sakatlığı hâlinde işçi sözleşmeyi iptal ettirebilir',
        },
        'E',
        "İş sözleşmesine TBK'nın genel hükümleri uygulanır. Ayırt etme gücüne sahip küçük (sınırlı ehliyetsiz) yasal temsilcisinin izniyle iş sözleşmesi yapabilir; 4857 md. 71 çalışma yaşı sınırlarını ayrıca belirler. Hile (aldatma) ve hata gibi irade sakatlığı hâllerinde sözleşme kesin hükümsüz değil İPTAL EDİLEBİLİR niteliktedir (TBK md. 30 vd.); iptale kadar geçen dönemde iş görülmüşse işçinin ücret hakkı korunur.",
    ),
    '0058': patch(
        'Bir kadın işçinin doğumu 10 Mart tarihinde gerçekleşmiş, hekim raporunda çoğul gebelik bulunmadığı belirtilmiştir. İşveren, işçiyi doğumdan sonraki dördüncü haftada işbaşı yapmaya çağırmıştır. Buna göre aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kadın işçinin doğumdan önce sekiz, doğumdan sonra sekiz hafta çalıştırılmaması esastır; bu nedenle çağrı hukuka aykırıdır',
            'B': 'Çoğul gebelik bulunmadığı için doğum sonrası izin altı haftaya iner',
            'C': 'Doğum sonrası izin dört hafta olduğundan çağrı hukuka uygundur',
            'D': 'İşçi isterse hekim onayıyla doğum sonrası sekiz haftalık sürenin bir bölümünden vazgeçerek dördüncü haftada erken işbaşı yapabilir',
            'E': 'Doğum öncesi ve sonrası toplam izin süresi on hafta olarak uygulanır',
        },
        'A',
        '4857 md. 74: kadın işçilerin doğumdan önce sekiz ve doğumdan sonra sekiz hafta olmak üzere toplam on altı haftalık süre için çalıştırılmamaları esastır. Çoğul gebelikte doğumdan önceki süreye iki hafta eklenir. Sağlık durumu uygunsa hekim onayıyla işçi isterse doğumdan önceki üç haftaya kadar çalışabilir ve çalışılan süre doğum SONRASINA eklenir; doğum sonrası sekiz haftalık süre kısaltılamaz.',
    ),
    '0059': patch(
        'İş sözleşmesinin kurulması ve çalışma koşulları ile ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Çalışma koşullarındaki esaslı değişiklik işçiye yazılı olarak bildirilir',
            'B': 'İşçi değişikliği altı iş günü içinde yazılı olarak kabul etmezse değişiklik bağlayıcı olmaz',
            'C': 'Çalışma koşullarında esaslı değişiklik, işverenin tek taraflı bildirimiyle işçiyi bağlar',
            'D': 'İşçinin kabul etmediği değişikliği uygulamak işçiye haklı fesih imkânı verebilir',
            'E': 'İşveren, değişikliğin geçerli bir nedene dayandığını yazılı olarak açıklarsa sözleşmeyi feshedebilir',
        },
        'C',
        '4857 md. 22: işveren, iş sözleşmesiyle veya eklerine dayanan çalışma koşullarında esaslı bir değişikliği ancak durumu işçiye YAZILI olarak bildirmek suretiyle yapabilir. Bu şekle uygun olmayan ve işçi tarafından altı iş günü içinde yazılı olarak kabul edilmeyen değişiklikler işçiyi BAĞLAMAZ. İşçi değişikliği kabul etmezse işveren, değişikliğin geçerli bir nedene dayandığını yazılı olarak açıklayarak bildirim süresine uymak suretiyle sözleşmeyi feshedebilir.',
    ),
    '0060': patch(
        'İş hukuku ve iş sözleşmesi ile ilgili aşağıdaki ifadelerden hangileri yanlıştır? I. İş sözleşmesinin ayırt edici temel unsuru bağımlılıktır. II. İşveren, haklı bir neden olmadıkça işçileri arasında ayrım yapamaz. III. Belirli süreli iş sözleşmesi, objektif bir neden bulunmasa da serbestçe yapılabilir. IV. İşçinin aylık ücretinin yarısına kadar olan bölümü haczedilebilir.',
        {
            'A': 'I ve II',
            'B': 'III ve IV',
            'C': 'Yalnız III',
            'D': 'I, III ve IV',
            'E': 'II ve III',
        },
        'B',
        'III YANLIŞ: 4857 md. 11 belirli süreli sözleşme için objektif koşul arar. IV YANLIŞ: md. 35 uyarınca işçi ücretlerinin ayda DÖRTTE BİRİNDEN fazlası haczedilemez (nafaka borcu ayrıktır). I (md. 8) ve II (md. 5) doğrudur.',
    ),
}

PATCHES = {ONEK + k: v for k, v in _PATCHES.items()}


def apply_or_check(path, write):
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    by_id = {q["id"]: q for q in questions}
    fark = []
    for qid, alanlar in PATCHES.items():
        q = by_id.get(qid)
        if q is None:
            raise SystemExit(f"Soru bulunamadi: {path}::{qid}")
        for alan, beklenen in alanlar.items():
            if q.get(alan) != beklenen:
                fark.append(f"{path}::{qid}.{alan}")
                if write:
                    q[alan] = beklenen
        if write:
            if len(set(q["options"].values())) != 5:
                raise SystemExit(f"Secenek cakismasi: {path}::{qid}")
            if q["answer"] not in q["options"]:
                raise SystemExit(f"Cevap secenekte yok: {path}::{qid}")
    if write:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return fark


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--write", action="store_true")
    args = ap.parse_args()
    fark = []
    for path in (ROOT / RELATIVE_PATH, APP_ROOT / RELATIVE_PATH):
        fark.extend(apply_or_check(path, args.write))
    if args.check and fark:
        print("Eslesmeyen alanlar:")
        for f in fark[:20]:
            print(f"- {f}")
        return 1
    print(f"1 paket / {len(PATCHES)} soru (Is Hukuku yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
