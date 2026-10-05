#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vergi Usul Kanunu — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Vergiye ozgu profille yeniden yazim (hukuk bandindaki uzun sikli surum mutlak ifadeli celdiriciler nedeniyle FATAL veriyordu): yoklama-inceleme-arama-bilgi toplama, bildirimler, defter tutma ve tasdik, belge duzeni, muhafaza-ibraz, degerleme ve amortisman, vergi ziyai-usulsuzluk-kacakcilik. 7338, 7394, 7524 ve 7555 degisiklikleri dahil; yila bagli had sorulmadi; 17 hesap sorusu bagimsiz dogrulandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 213 sayili Vergi Usul Kanunu guncel metni (mevzuat.gov.tr)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/vergi_hukuku/vergi_usul_kanunu.json"
STYLE_REF = 'SGS Vergi Hukuku (gercek sinav profiline kalibre: kanun bilgisi + olay uygulamasi)'
ONEK = "vuk-gen-"


def patch(stem, options, answer, solution, ref='213 sayili Vergi Usul Kanunu'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Yoklama memurları bir mükellefin işyerine önceden haber vermeden gelmiş, mükellef işyerinde bulunmadığından yoklama fişini imzalayacak kimse olmamıştır. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Fiş tek nüsha düzenlenir ve vergi dairesinde saklanır',
            'B': 'Yoklama ancak mükellefin rızasıyla tekrarlanabilir',
            'C': 'Durum fişe yazılır; fiş polis, jandarma veya muhtara imzalatılır',
            'D': 'Yoklama ertelenir; mükellefe yazılı bildirim yapılarak yeni bir yoklama günü belirlenir',
            'E': 'Yoklama, önceden haber verilmediği için geçersizdir',
        },
        'C',
        "m. 130'a göre yoklama her zaman yapılabilir ve **ne zaman yapılacağı ilgiliye haber verilmez**. m. 131'e göre fiş iki nüsha düzenlenir; ilgili bulunmaz veya imzadan çekinirse **keyfiyet fişe yazılır ve fiş polis, jandarma, muhtar veya ihtiyar meclisi üyelerinden birine imzalatılır**.",
        '213 sayılı Vergi Usul Kanunu m. 130, 131',
    ),
    # düzey 3
    '0002': patch(
        'Tam inceleme olarak başlatılan bir vergi incelemesi kanuni sürede bitirilememiş ve azami ek süre verilmiştir. İnceleme, başladığı tarihten itibaren en geç kaç ayda tamamlanmalıdır?',
        {
            'A': '9',
            'B': '12',
            'C': '6',
            'D': '15',
            'E': '18',
        },
        'E',
        "m. 140/6'ya göre incelemeye başlanılan tarihten itibaren **tam incelemede en fazla bir yıl**, sınırlı incelemede altı ay içinde bitirilmesi esastır; tam ve sınırlı incelemelerde **altı ayı geçmemek üzere ek süre** verilebilir: 12 + 6 = **18 ay**.",
        '213 sayılı Vergi Usul Kanunu m. 140/6',
    ),
    # düzey 2
    '0003': patch(
        "Aşağıdakilerden hangisi Vergi Usul Kanunu'na göre vergi incelemesi yapmaya yetkili değildir?",
        {
            'A': 'Vergi dairesi müdürü',
            'B': 'Vergi müfettiş yardımcısı',
            'C': 'Yoklama memuru',
            'D': 'Vergi müfettişi',
            'E': 'İlin en büyük mal memuru',
        },
        'C',
        "m. 135'e göre vergi incelemesi **vergi müfettişleri, vergi müfettiş yardımcıları, ilin en büyük mal memuru veya vergi dairesi müdürleri** tarafından yapılır; GİB merkez ve taşra teşkilatında müdür kadrolarında görev yapanlar da yetkilidir. Yoklama memurları yoklamaya yetkilidir (m. 128), incelemeye değil.",
        '213 sayılı Vergi Usul Kanunu m. 135',
    ),
    # düzey 3
    '0004': patch(
        'Vergi dairesi, bir hekimden ve bir avukattan bilgi istemiştir. Aşağıdaki bilgilerden hangisi istenebilir?',
        {
            'A': 'Avukatın müvekkilinin davası nedeniyle dosyadan öğrendiği ticari sırlar',
            'B': 'Hekimin hastalarının hastalık türleri',
            'C': 'Avukatın müvekkil adları ve aldığı vekâlet ücretleri',
            'D': 'Hekimin hastalarına koyduğu teşhisler',
            'E': "PTT'nin tuttuğu haberleşme içerikleri",
        },
        'C',
        "m. 151'e göre özel kanunlardaki mahremiyet hükümleri ileri sürülerek bilgi vermekten kaçınılamaz; ancak hekimlerden **hastalık türüne** ilişkin bilgi, avukatlardan **görevleri dolayısıyla öğrendikleri hususlar** istenemez. Bu yasak **müvekkil adlarıyla vekâlet ücretlerine ve giderlerine** şamil değildir.",
        '213 sayılı Vergi Usul Kanunu m. 151',
    ),
    # düzey 2
    '0005': patch(
        'Bir limited şirketin kuruluş aşamasındaki işe başlama bildirimi vergi dairesine kim tarafından yapılır?',
        {
            'A': 'Ticaret sicili müdürlüğü',
            'B': 'Şirket müdürü',
            'C': 'Ortaklardan en büyük paya sahip olan',
            'D': 'Noter',
            'E': 'Şirketin muhasebecisi',
        },
        'A',
        "m. 168'e göre **şirketlerin kuruluş aşamasında işe başlama bildirimleri, işe başlama tarihinden itibaren on gün içinde ticaret sicili memurluğunca** ilgili vergi dairesine yapılır; m. 153'e göre bu mükelleflerin işe başlamayı bildirme ödevi yerine getirilmiş sayılır.",
        '213 sayılı Vergi Usul Kanunu m. 168',
    ),
    # düzey 1
    '0006': patch(
        'Aşağıdaki defterlerden hangisine işlemlerin günü gününe kaydedilmesi zorunludur?',
        {
            'A': 'İşletme hesabı defteri',
            'B': 'Yevmiye defteri',
            'C': 'Defterikebir',
            'D': 'Serbest meslek kazanç defteri',
            'E': 'Envanter defteri',
        },
        'D',
        "m. 219/c'ye göre **günlük kasa, günlük, perakende satış ve hasılat defterleri ile serbest meslek kazanç defterine** muameleler günü gününe kaydedilir. Diğer defterlerde kayıtlar on günden fazla geciktirilemez.",
        '213 sayılı Vergi Usul Kanunu m. 219/c',
    ),
    # düzey 3
    '0007': patch(
        "Öteden beri işe devam eden bir mükellef 2027 yılı yevmiye defterini 20 Ocak 2027'de tasdik ettirmiştir. Bu fiil için hangi ceza uygulanır?",
        {
            'A': 'II. derece usulsüzlük cezası',
            'B': 'Özel usulsüzlük cezası',
            'C': 'Vergi ziyaı cezası',
            'D': 'Ceza uygulanmaz',
            'E': 'I. derece usulsüzlük cezası',
        },
        'A',
        "Tasdikin kanuni süresi Aralık 2026 sonunda bitmiştir. m. 352'ye göre tasdik muamelesinin **süresinin sonundan başlayarak bir ay içinde** yaptırılması **II. derece** usulsüzlüktür; **bir ay geçtikten sonra** tasdik ettirilen defterler ise tasdik ettirilmemiş sayılır ve I. derece usulsüzlük oluşur.",
        '213 sayılı Vergi Usul Kanunu m. 221, 352',
    ),
    # düzey 2
    '0008': patch(
        'Defter tutma kurallarına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Yevmiye defterindeki yanlışlar muhasebe kaidelerine göre düzeltilir',
            'B': 'Kayıtlar arasında boş satır çizilmeden bırakılamaz',
            'C': 'Toplamlar hesaplar kapanıncaya kadar kurşun kalemle yapılabilir',
            'D': 'Ciltli defterlerin sayfaları koparılamaz',
            'E': 'Yanlış kayıt, silinerek okunamaz hâle getirilip düzeltilebilir',
        },
        'E',
        "m. 217'ye göre defterlere geçirilen bir kaydı **kazımak, çizmek veya silmek suretiyle okunamaz hâle getirmek yasaktır**; yevmiye defterindeki yanlışlar muhasebe kaidelerine göre düzeltilir. m. 218 boş satır bırakmayı ve sayfa koparmayı yasaklar; m. 216 geçici toplamların kurşun kalemle yapılmasına izin verir.",
        '213 sayılı Vergi Usul Kanunu m. 217, 218',
    ),
    # düzey 2
    '0009': patch(
        'Birinci sınıf bir tüccar, vergiden muaf bir esnaftan mal satın almış ve gider pusulası düzenlemiştir. Bu gider pusulası hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Gider yazılabilmesi için ayrıca fatura alınmalıdır',
            'B': 'Esnafın imzası aranmaz',
            'C': 'Sadece bedeli nakden ödenmişse geçerlidir',
            'D': 'Esnaf tarafından verilmiş fatura hükmündedir',
            'E': 'Tek nüsha düzenlenir',
        },
        'D',
        "m. 234'e göre tüccarlar, belge düzenleme zorunluluğu bulunmayanlardan satın aldıkları mallar için satana imzalatacakları **iki nüsha** gider pusulası düzenler; **vergiden muaf esnaf için düzenlenen gider pusulası, bu kişiler tarafından verilmiş fatura hükmündedir**.",
        '213 sayılı Vergi Usul Kanunu m. 234',
    ),
    # düzey 2
    '0010': patch(
        'Bir mükellefin 2025 yılına ait defter ve belgelerinin muhafaza süresi hangi yılın sonunda dolar?',
        {
            'A': '2031',
            'B': '2032',
            'C': '2030',
            'D': '2027',
            'E': '2035',
        },
        'C',
        "m. 253'e göre defter tutmak zorunda olanlar defter ve vesikalarını **ilgili bulundukları yılı takip eden takvim yılından başlayarak beş yıl** süreyle muhafaza eder: 2026-2030 yılları, yani süre **2030 yılı sonunda** dolar.",
        '213 sayılı Vergi Usul Kanunu m. 253',
    ),
    # düzey 3
    '0011': patch(
        'Vergi incelemesinde mükelleften, elektronik ortamda tuttuğu kayıtlar ile bunlara erişim için gerekli şifreler istenmiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sadece kâğıt ortamındaki belgeler ibraz edilir',
            'B': 'Kayıtlarla birlikte erişim bilgi ve şifreleri de ibraz edilmelidir',
            'C': 'Şifre yerine kayıtların çıktısı verilmesi yeterlidir',
            'D': 'Elektronik kayıtlar ancak mahkeme kararıyla istenebilir',
            'E': 'Şifreler kişisel veri olduğundan verilmez',
        },
        'B',
        "m. 256'ya göre muhafaza zorunluluğu olanlar, defter ve belgeleri ile manyetik ve benzeri ortamlardaki kayıtlarını ve **bu kayıtlara erişim veya kayıtları okunabilir hâle getirmek için gerekli tüm bilgi ve şifreleri** muhafaza süresi içinde yetkililerin talebi üzerine ibraz etmek zorundadır.",
        '213 sayılı Vergi Usul Kanunu m. 256',
    ),
    # düzey 3
    '0012': patch(
        "Maliyet bedeli 100 ₺ olan bir emtianın değerleme günündeki satış bedeli 88 ₺'ye düşmüştür. Mükellefin değerlemede başvurabileceği ölçü hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Maliyet bedeli yerine emsal bedeli uygulanabilir',
            'B': 'Emtia tasarruf değeriyle değerlenir',
            'C': 'Emsal bedelinin maliyet bedeli esası uygulanmalıdır',
            'D': 'Değer düşüklüğü dikkate alınamaz',
            'E': 'Emtia borsa rayici ile değerlenir',
        },
        'A',
        "m. 274'e göre emtia maliyet bedeliyle değerlenir; satış bedeli maliyet bedeline göre **%10 ve daha fazla** düşüklük gösterirse mükellef, **m. 267'nin ikinci sırasındaki usul hariç** olmak üzere emsal bedeli uygulayabilir. Düşüş (100 − 88) / 100 = **%12** olduğundan emsal bedeli uygulanabilir.",
        '213 sayılı Vergi Usul Kanunu m. 274',
    ),
    # düzey 3
    '0013': patch(
        'Bir işletme, vadesi gelmemiş alacak senetlerini değerleme gününün değerine indirgemiş (reeskont) ancak borç senetlerine aynı işlemi uygulamamıştır. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Alacak senedi reeskontu da geçersiz hâle gelir',
            'B': 'Borç senetleri itibari değerle değerlenir',
            'C': 'Borç senetlerine de reeskont uygulanması zorunludur',
            'D': 'Alacak ve borç senetleri birbirinden bağımsız olarak ayrı ayrı değerlenebilir',
            'E': 'Reeskont sadece bankalar için mümkündür',
        },
        'C',
        "m. 281'e göre vadesi gelmemiş senetli alacaklar değerleme günü kıymetine irca olunabilir. m. 285'e göre **alacak senetlerini değerleme gününün kıymetine irca eden mükellefler, borç senetlerini de aynı şekilde işleme tabi tutmak zorundadır**.",
        '213 sayılı Vergi Usul Kanunu m. 281, 285',
    ),
    # düzey 2
    '0014': patch(
        'Bir işletme, faaliyetinde kullanmak üzere satın aldığı binek otomobili hesap döneminin Ekim ayında aktifine almıştır. Otomobilin aktife girdiği yıl için amortisman hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Kalan ay süresi kadar (kıst) amortisman ayrılır',
            'B': 'O yıl için amortisman ayrılamaz',
            'C': 'Tam yıl amortisman ayrılır',
            'D': 'Yarım yıl amortisman ayrılır',
            'E': 'Mükellef tam yıl ile kıst arasında tercih yapar',
        },
        'A',
        "m. 320'ye göre amortisman süresi kıymetlerin aktife girdiği yıldan başlar; **binek otomobillerinde (kiralama işletmelerinin bu amaçla kullandıkları hariç) aktife girdiği dönem için ay kesri tam ay sayılarak kalan ay süresi kadar** amortisman ayrılır, ayrılmayan kısım son yılda yok edilir.",
        '213 sayılı Vergi Usul Kanunu m. 320',
    ),
    # düzey 3
    '0015': patch(
        "Hiç mükellefiyet kaydı yaptırmadan ticari faaliyette bulunan bir kişinin tespit edilen faaliyeti nedeniyle 100.000 ₺ vergi ziyaı oluşmuştur. Fiil m. 359 kapsamında değildir. Kesilecek vergi ziyaı cezası kaç ₺'dir?",
        {
            'A': '150.000',
            'B': '50.000',
            'C': '100.000',
            'D': '200.000',
            'E': '300.000',
        },
        'A',
        "7524 sayılı Kanunla m. 344'e eklenen fıkraya göre **mükellefiyet tesis ettirilmesi gerektiği hâlde vergi dairesinin ıttılaı dışında faaliyette bulunarak** vergi ziyaına sebebiyet verilmesi durumunda vergi ziyaı cezası **%50 artırılarak** uygulanır: 100.000 × 1,5 = **150.000 ₺**.",
        '213 sayılı Vergi Usul Kanunu m. 344 (7524 sayılı Kanunla eklenen fıkra)',
    ),
    # düzey 2
    '0016': patch(
        "Bir usulsüzlük fiili, matrahın re'sen takdirini gerektirmiştir. Cetvelde bu fiil için öngörülen ceza 3.000 ₺ ise kesilecek usulsüzlük cezası kaç ₺'dir?",
        {
            'A': '3.000',
            'B': '1.500',
            'C': '9.000',
            'D': '4.500',
            'E': '6.000',
        },
        'E',
        "m. 352'ye göre **usulsüzlük fiili re'sen takdiri gerektirirse, 1 sayılı cetvelde yazılı cezalar iki kat olarak** kesilir: 3.000 × 2 = **6.000 ₺**.",
        '213 sayılı Vergi Usul Kanunu m. 352',
    ),
    # düzey 2
    '0017': patch(
        "Bir mükellef aynı takvim yılında aynı nevi ikinci derece usulsüzlüğü üç kez işlemiştir. İlk fiil için ceza 1.200 ₺'dir. Üç fiil için kesilecek toplam ceza kaç ₺'dir?",
        {
            'A': '1.800',
            'B': '1.500',
            'C': '900',
            'D': '1.200',
            'E': '300',
        },
        'A',
        "m. 337'ye göre ayrı ayrı yapılan usulsüzlüklerden ayrı ayrı ceza kesilir; ancak m. 352'deki usulsüzlüklerden **aynı takvim yılında aynı neviden birden fazla yapılırsa, birden fazlasının her biri için birincisine ait cezanın dörtte biri** kesilir: 1.200 + 300 + 300 = **1.800 ₺**.",
        '213 sayılı Vergi Usul Kanunu m. 337',
    ),
    # düzey 3
    '0018': patch(
        "Hakkında 2024'te kesilen 40.000 ₺ vergi ziyaı cezası 2024'te kesinleşen bir mükellefe, 2026'da yeni bir fiil için 100.000 ₺ vergi ziyaı cezası kesilecektir. Tekerrür uygulandığında kesilecek ceza kaç ₺'dir?",
        {
            'A': '125.000',
            'B': '140.000',
            'C': '100.000',
            'D': '150.000',
            'E': '200.000',
        },
        'B',
        "m. 339'a göre vergi ziyaı cezası kesinleşenlere, kesinleşmeyi izleyen günden itibaren **beşinci yılın isabet ettiği takvim yılı sonuna kadar** tekrar ceza kesilirse ceza **%50 artırılır**; ancak **artırım tutarı kesinleşen cezadan fazla olamaz**. Artırım 100.000 × %50 = 50.000 ₺, sınır 40.000 ₺ olduğundan ceza 100.000 + 40.000 = **140.000 ₺**'dir.",
        '213 sayılı Vergi Usul Kanunu m. 339 (7338 sayılı Kanunla değişik)',
    ),
    # düzey 3
    '0019': patch(
        'Aşağıdaki alacaklardan hangileri şüpheli alacak sayılabilir?\n\nI. Ticari faaliyetle ilgili, dava safhasındaki alacak\n\nII. Ortağa verilen, icra takibindeki kişisel borç\n\nIII. Mahkeme kararıyla tahsili imkânsız hâle gelen alacak',
        {
            'A': 'Yalnız I',
            'B': 'I ve III',
            'C': 'Yalnız III',
            'D': 'I, II ve III',
            'E': 'I ve II',
        },
        'A',
        "m. 323'e göre şüpheli alacak için alacağın **ticari ve zirai kazancın elde edilmesi ve idame ettirilmesi ile ilgili olması** ve dava veya icra safhasında bulunması gerekir (I). Ortağa verilen kişisel borç ticari faaliyetle ilgili olmadığından (II) şüpheli alacak sayılmaz. Kazai hükme göre tahsili imkânsız alacak (III) şüpheli değil **değersiz alacaktır** (m. 322).",
        '213 sayılı Vergi Usul Kanunu m. 322, 323',
    ),
    # düzey 2
    '0020': patch(
        'Yoklama ve incelemeye yetkili olanlara ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Gelir uzmanları yoklama yapabilir',
            'B': 'Vergi incelemesine yetkili olanlar yoklama da yapabilir',
            'C': 'Vergi dairesi müdürleri inceleme yapabilir',
            'D': 'Gelir uzmanları vergi incelemesine yetkilidir',
            'E': 'Vergi dairesi müdürleri yoklama yapabilir',
        },
        'D',
        "m. 128'e göre yoklama; vergi dairesi müdürleri, yoklama memurları, görevlendirilenler, **vergi incelemesine yetkili olanlar** ve **gelir uzmanları** tarafından yapılır. m. 135'te inceleme yetkisi sayılanlar arasında **gelir uzmanları yer almaz**.",
        '213 sayılı Vergi Usul Kanunu m. 128, 135',
    ),
    # düzey 3
    '0021': patch(
        'Yoklama fişi, koordinat bazlı konum bilgisi ve yoklama yerinin fotoğraflarını içerecek şekilde elektronik ortamda düzenlenmiştir. Nezdinde yoklama yapılan kişi imzadan çekinmiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Polis, jandarma veya muhtar imzası aranmaz',
            'B': 'Yoklama hükümsüz sayılır',
            'C': 'İki tanık imzası zorunludur',
            'D': 'Fiş kâğıda dökülerek muhtara imzalatılır',
            'E': 'Fiş vergi dairesi müdürünce onaylanmadıkça geçersizdir',
        },
        'A',
        "7555 sayılı Kanunla m. 131'e eklenen cümleye göre yoklama fişinin m. 132/A kapsamında **koordinat bazlı konum bilgisi ve yoklama yerine ilişkin fotoğrafları içerecek şekilde elektronik ortamda** düzenlendiği durumlarda **polis, jandarma, muhtar veya ihtiyar meclisi üyelerinin imzası aranmaz**.",
        '213 sayılı Vergi Usul Kanunu m. 131, 132/A (7555 sayılı Kanunla değişik)',
    ),
    # düzey 2
    '0022': patch(
        '7338 sayılı Kanun değişikliğinden sonra vergi incelemesinin yapılacağı yer hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İncelemeyi yapanın uygun gördüğü yerde yapılır',
            'B': 'Esas olarak mükellefin işyerinde yapılır',
            'C': 'Sadece mükellefin ikametgâhında yapılır',
            'D': 'Mahkeme kararıyla belirlenen yerde yapılır',
            'E': 'Esas olarak dairede yapılır; talep ve uygunluk varsa işyerinde yapılabilir',
        },
        'E',
        "7338 sayılı Kanunla değişen m. 139'a göre vergi incelemeleri **esas itibarıyla dairede** yapılır; **mükellef veya vergi sorumlusunun talep etmesi ve işyerinin müsait olması** hâlinde işyerinde de yapılabilir. Dairede yapılması, işyerinde tespit yapılmasına engel değildir.",
        '213 sayılı Vergi Usul Kanunu m. 139 (7338 sayılı Kanunla değişik)',
    ),
    # düzey 2
    '0023': patch(
        "Vergi Usul Kanunu'ndaki bilgi toplama hükümlerine ilişkin aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Diplomatik muafiyeti olan yabancı devlet memurları bilgi vermekle yükümlü değildir',
            'B': 'Sözlü bilgi isteğine uymayan kişi vergi dairesine zorla getirilir',
            'C': 'Toplanan bilgiler istihbarat arşivlerinde gizli olarak saklanır',
            'D': 'Özel kanunlardaki mahremiyet hükümleri bilgi vermemeye gerekçe olamaz',
            'E': 'Bilgiler yazı veya sözle istenebilir',
        },
        'B',
        "m. 148'e göre sözle istenen bilgiyi vermeyenlere keyfiyet **yazıyla tekit edilir ve münasip bir mühlet** verilir; **bilgi istenmek üzere ilgililer vergi dairesine zorla getirilemez**. Memleket dışı imtiyazlarından faydalanan yabancı devlet memurları bilgi verme mecburiyetine tabi değildir; m. 151 mahremiyet itirazını, m. 152 istihbarat arşivini düzenler.",
        '213 sayılı Vergi Usul Kanunu m. 148-152',
    ),
    # düzey 2
    '0024': patch(
        "Bir kişi 3 Mart'ta serbest meslek faaliyetine başlamıştır. İşe başlamayı vergi dairesine en geç hangi tarihe kadar bildirmelidir?",
        {
            'A': '10 Mart',
            'B': '31 Mart',
            'C': '18 Mart',
            'D': '13 Mart',
            'E': '3 Nisan',
        },
        'D',
        "m. 153'e göre serbest meslek erbabı işe başlamayı bildirmek zorundadır; m. 168'e göre **gerçek kişilerde işe başlama bildirimi işe başlama tarihinden itibaren on gün içinde** yapılır: 3 Mart + 10 gün = **13 Mart**. Diğer bildirimler (işi bırakma, değişiklik) bir ay içinde yapılır.",
        '213 sayılı Vergi Usul Kanunu m. 153, 168',
    ),
    # düzey 3
    '0025': patch(
        'Bir lokanta işletmecisi tadilat nedeniyle işyerini üç ay kapatmış, bu sürede hiç satış yapmamıştır. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yeniden açılışta işe başlama bildirimi verilir',
            'B': 'Faaliyet durdurulduğu için defter tutma ödevi kalkar',
            'C': 'İşi bırakma sayılır; bir ay içinde bildirilir',
            'D': 'Geçici durdurma olduğundan işi bırakma sayılmaz',
            'E': "Mükellefiyet re'sen terkin edilir",
        },
        'D',
        "m. 161'e göre işi bırakma, vergiye tabi olmayı gerektiren muamelelerin **tamamen durdurulması ve sona ermesidir**; **işlerin herhangi bir sebeple geçici bir süre için durdurulması işi bırakma sayılmaz**.",
        '213 sayılı Vergi Usul Kanunu m. 161',
    ),
    # düzey 2
    '0026': patch(
        "Aşağıdaki defterlerden hangisinin Vergi Usul Kanunu'na göre tasdik ettirilmesi zorunlu değildir?",
        {
            'A': 'Serbest meslek kazanç defteri',
            'B': 'Envanter defteri',
            'C': 'Defterikebir',
            'D': 'İşletme defteri',
            'E': 'Yevmiye defteri',
        },
        'C',
        "m. 220'ye göre **yevmiye ve envanter defterleri, işletme defteri, çiftçi işletme defteri, serbest meslek kazanç defteri** gibi defterlerin tasdiki mecburidir. **Defterikebir** bu sayımda yer almaz.",
        '213 sayılı Vergi Usul Kanunu m. 220',
    ),
    # düzey 3
    '0027': patch(
        'Öteden beri işe devam eden bir mükellef, 2027 yılında kullanacağı yevmiye defterini hangi ay içinde tasdik ettirmelidir?',
        {
            'A': 'Temmuz 2026',
            'B': 'Aralık 2026',
            'C': 'Ocak 2027',
            'D': 'Kasım 2026',
            'E': 'Şubat 2027',
        },
        'B',
        "m. 221'e göre **öteden beri işe devam etmekte olanlar**, defteri **kullanacakları yıldan önce gelen son ayda** tasdik ettirir: 2027 defteri için **Aralık 2026**. Defterini ertesi yılda da kullanmak isteyenler ise tasdiki Ocak ayında yeniletir (m. 222).",
        '213 sayılı Vergi Usul Kanunu m. 221',
    ),
    # düzey 2
    '0028': patch(
        "Bir tüccar 4 Mart'ta teslim ettiği mal için en geç hangi tarihte fatura düzenlemelidir? (Bakanlıkça süre kısaltılmadığı varsayılsın.)",
        {
            'A': '10 Mart',
            'B': '14 Mart',
            'C': '7 Mart',
            'D': '11 Mart',
            'E': '4 Nisan',
        },
        'D',
        "m. 231/5'e göre fatura, **malın teslimi veya hizmetin yapıldığı tarihten itibaren azami yedi gün içinde** düzenlenir: 4 Mart + 7 gün = **11 Mart**. Bakanlık bu süreyi kısaltmaya veya anında düzenleme zorunluluğu getirmeye yetkilidir; süresinde düzenlenmeyen fatura hiç düzenlenmemiş sayılır.",
        '213 sayılı Vergi Usul Kanunu m. 231/5',
    ),
    # düzey 3
    '0029': patch(
        'Bir faturada, Bakanlığın belirlediği zorunlu bilgilerden alıcının vergi kimlik numarası yer almamaktadır. Bu fatura vergi kanunları bakımından nasıl değerlendirilir?',
        {
            'A': 'Geçerlidir; eksiklik sonradan tamamlanabilir',
            'B': 'Yarı değerinde belge sayılır',
            'C': 'Gelir vergisi bakımından geçerli, KDV indirimi bakımından geçersizdir',
            'D': 'Vergi kanunları bakımından düzenlenmemiş sayılır',
            'E': 'Alıcı onaylarsa geçerlidir',
        },
        'D',
        "m. 227'ye göre VUK'a göre kullanılan veya Bakanlıkça kullanma mecburiyeti getirilen belgelerin **öngörülen zorunlu bilgileri taşımaması hâlinde, bu belgeler vergi kanunları bakımından hiç düzenlenmemiş sayılır**.",
        '213 sayılı Vergi Usul Kanunu m. 227',
    ),
    # düzey 2
    '0030': patch(
        'Bir işletme makine satın almış; satış bedeli dışında nakliye, montaj ve noter giderleri ödemiştir. Bu giderler hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Mükellef tercihine göre gider yazılır',
            'B': 'Ayrı bir kıymet olarak amorti edilir',
            'C': 'Sadece nakliye gideri maliyete eklenir',
            'D': 'Doğrudan dönem gideri yazılır',
            'E': 'Maliyet bedeline dâhil edilir',
        },
        'E',
        "7338 sayılı Kanunla eklenen m. 262/2'ye göre iktisadi kıymetin iktisabıyla doğrudan ilgili **gümrük vergileri, yükleme, boşaltma, nakliye ve montaj giderleri** ile **resim ve harçlar, noter, tapu, danışmanlık, komisyon** giderleri **maliyet bedeline dâhil edilir**.",
        '213 sayılı Vergi Usul Kanunu m. 262 (7338 sayılı Kanunla değişik)',
    ),
    # düzey 3
    '0031': patch(
        "Bir işletme, finansmanını krediyle sağladığı makineyi 2026 Mayıs'ında aktifine almıştır. Kredi faizinin hangi kısmının maliyete eklenmesi zorunludur?",
        {
            'A': 'Faiz, finansman gideri olarak doğrudan gider yazılır',
            'B': 'Sadece makinenin teslim tarihine kadarki faiz',
            'C': 'Kredinin tamamına ait faiz',
            'D': 'Kredinin vadesi sonuna kadar tahakkuk edecek faiz ve kur farklarının tamamı',
            'E': 'Makinenin envantere alındığı hesap dönemi sonuna kadarki kısmı',
        },
        'E',
        "m. 262/2-c'ye göre finansman kredilerinin faiz ve kur farkları **emtiada stoklara girdiği tarihe kadar, diğer iktisadi kıymetlerde envantere alındığı hesap döneminin sonuna kadar** olan kısmıyla maliyete dâhil edilir; sonraki kısmı maliyete eklemek veya gider yazmak mükellefin tercihine bırakılmıştır.",
        '213 sayılı Vergi Usul Kanunu m. 262/2-c',
    ),
    # düzey 2
    '0032': patch(
        'İmal edilen emtianın maliyet bedelini oluşturan unsurlardan hangisinin maliyete katılması mükellefin tercihine bırakılmıştır?',
        {
            'A': 'Mamule isabet eden işçilik',
            'B': 'Genel idare giderlerinden mamule düşen pay',
            'C': 'Genel imal giderlerinden mamule düşen pay',
            'D': 'Zorunlu ambalaj malzemesinin bedeli',
            'E': 'Direkt ilk madde ve malzeme bedeli',
        },
        'B',
        "m. 275'e göre imal edilen emtianın maliyet bedeli; ilk madde, işçilik, genel imal giderlerinden düşen pay ve zorunlu ambalaj bedelini içerir. **Genel idare giderlerinden mamule düşen hissenin maliyete katılması ihtiyaridir**.",
        '213 sayılı Vergi Usul Kanunu m. 275',
    ),
    # düzey 3
    '0033': patch(
        "Ticari faaliyetle ilgili 200.000 ₺'lik bir alacak için borçlu aleyhine icra takibi başlatılmıştır. Alacak için borçludan alınmış 50.000 ₺'lik ipotek teminatı bulunmaktadır. Ayrılabilecek şüpheli alacak karşılığı en fazla kaç ₺'dir?",
        {
            'A': '200.000',
            'B': '50.000',
            'C': '100.000',
            'D': '250.000',
            'E': '150.000',
        },
        'E',
        "m. 323'e göre ticari kazancın elde edilmesiyle ilgili ve **dava veya icra safhasındaki** alacaklar şüpheli alacak sayılır ve karşılık ayrılabilir; **teminatlı alacaklarda karşılık teminattan geri kalan miktara inhisar eder**: 200.000 − 50.000 = **150.000 ₺**.",
        '213 sayılı Vergi Usul Kanunu m. 323',
    ),
    # düzey 2
    '0034': patch(
        "Aşağıdakilerden hangisi Vergi Usul Kanunu'nda sayılan değerleme ölçülerinden biri değildir?",
        {
            'A': 'Emsal bedeli',
            'B': 'Tasarruf değeri',
            'C': 'Net gerçekleşebilir değer',
            'D': 'Rayiç bedel',
            'E': 'İtibari değer',
        },
        'C',
        "m. 261'e göre değerleme ölçüleri: **maliyet bedeli, borsa rayici, tasarruf değeri, mukayyet değer, itibari değer, vergi değeri, rayiç bedel, emsal bedeli ve ücreti**. Net gerçekleşebilir değer muhasebe standartlarında kullanılan bir ölçüdür.",
        '213 sayılı Vergi Usul Kanunu m. 261',
    ),
    # düzey 3
    '0035': patch(
        "Bir mükellef sahte fatura kullanarak 80.000 ₺ vergi ziyaına sebebiyet vermiş; bu faturayı düzenleyen kişi de fiile iştirak etmiştir. Mükellefe ve iştirak edene kesilecek vergi ziyaı cezaları sırasıyla kaç ₺'dir?",
        {
            'A': '160.000 ve 80.000',
            'B': '80.000 ve 80.000',
            'C': '240.000 ve 80.000',
            'D': '240.000 ve 40.000',
            'E': '240.000 ve 240.000',
        },
        'C',
        "m. 344/2'ye göre vergi ziyaına **m. 359'daki fiillerle** (sahte belge kullanma dâhil) sebebiyet verilmesi hâlinde ceza **üç kat**, bu fiillere **iştirak edenlere bir kat** uygulanır: mükellefe 80.000 × 3 = **240.000 ₺**, iştirak edene **80.000 ₺**.",
        '213 sayılı Vergi Usul Kanunu m. 344/2',
    ),
    # düzey 3
    '0036': patch(
        "Bir tüccar, 400.000 ₺'lik satışı için fatura düzenlememiştir. Özel usulsüzlük cezası kanuni asgari tutarın altında kalmıyorsa satıcıya kesilecek ceza kaç ₺'dir?",
        {
            'A': '20.000',
            'B': '40.000',
            'C': '120.000',
            'D': '80.000',
            'E': '400.000',
        },
        'B',
        "m. 353/1'e göre verilmesi gereken faturanın verilmemesi hâlinde, her bir belge için asgari tutarlardan aşağı olmamak üzere **belgeye yazılması gereken meblağın %10'u** nispetinde özel usulsüzlük cezası kesilir: 400.000 × %10 = **40.000 ₺**. Aynı ceza belgeyi almayan alıcıya da ayrıca kesilir.",
        '213 sayılı Vergi Usul Kanunu m. 353/1',
    ),
    # düzey 2
    '0037': patch(
        'Bir satıcı, fatura düzenlemesi gereken satışında VUK kapsamında olmayan bir belge (proforma) düzenlemiştir. Satıcıya kesilecek özel usulsüzlük cezası hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Ceza üç kat uygulanır',
            'B': 'Ceza iki kat uygulanır',
            'C': 'Ceza kesilmez',
            'D': 'Sadece usulsüzlük cezası kesilir',
            'E': 'Ceza yarı oranda uygulanır',
        },
        'B',
        "7524 sayılı Kanunla m. 353/1'e eklenen hükme göre **bu bent kapsamındaki belgeler yerine VUK kapsamında olmayan belgelerin düzenlenmesi hâlinde**, belgeleri düzenlemek zorunda olanlar adına özel usulsüzlük cezası **iki kat** uygulanır; alıcı beş iş günü içinde bildirirse ceza altı kat olur.",
        '213 sayılı Vergi Usul Kanunu m. 353/1 (7524 sayılı Kanunla değişik)',
    ),
    # düzey 3
    '0038': patch(
        'Sahte belge kullanan bir mükellef, tarh edilen vergi, gecikme faizi ve gecikme zammının tamamı ile kesilen cezaların yarısını ve buna isabet eden gecikme zammını soruşturma evresinde ödemiştir. Verilecek hapis cezası hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tamamen kaldırılır',
            'B': 'Üçte bir oranında indirilir',
            'C': 'Dörtte bir oranında indirilir',
            'D': 'İndirim yapılmaz',
            'E': 'Yarı oranında indirilir',
        },
        'E',
        "7394 sayılı Kanunla m. 359'a eklenen fıkraya göre bu ödemenin **soruşturma evresinde** yapılması hâlinde verilecek ceza **yarı oranında**, **kovuşturma evresinde hüküm verilinceye kadar** yapılması hâlinde **üçte bir oranında** indirilir.",
        '213 sayılı Vergi Usul Kanunu m. 359 (7394 sayılı Kanunla eklenen fıkra)',
    ),
    # düzey 2
    '0039': patch(
        'Aşağıdaki fiillerden hangileri birinci derece usulsüzlüktür?\n\nI. Vergi beyannamesinin süresinde verilmemesi\n\nII. İşe başlamanın zamanında bildirilmemesi\n\nIII. Adres değişikliğinin zamanında bildirilmemesi',
        {
            'A': 'I ve III',
            'B': 'Yalnız II',
            'C': 'I ve II',
            'D': 'Yalnız I',
            'E': 'I, II ve III',
        },
        'C',
        "m. 352'ye göre **beyannamelerin süresinde verilmemesi** (I/1) ve **işe başlamanın zamanında bildirilmemesi** (I/7) birinci derece usulsüzlüktür. **Vergi kanunlarında yazılı bildirmelerin zamanında yapılmaması (işe başlama hariç)** ise ikinci derece usulsüzlüktür (II/4).",
        '213 sayılı Vergi Usul Kanunu m. 352',
    ),
    # düzey 2
    '0040': patch(
        'Perakende satış vesikalarına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Fişte işletmenin adı, tarih ve alınan para miktarı gösterilir',
            'B': 'Fişler kopyalı iki nüsha düzenlenir, biri müşteriye verilir',
            'C': 'Perakende satış fişinde alıcının adı ve adresi zorunludur',
            'D': 'Perakende satış fişleri seri ve sıra numaralı olur',
            'E': 'Giriş ve yolcu taşıma biletleri perakende satış vesikasıdır',
        },
        'C',
        "m. 233'e göre perakende satış fişi, makineli kasa kayıt ruloları ve biletlerde **işletme veya mükellefin adı, düzenlenme tarihi ve alınan paranın miktarı** gösterilir; alıcının adı ve adresi zorunlu bilgiler arasında değildir. Fiş ve biletler seri-sıra numaralı, kopyalı iki nüsha düzenlenir.",
        '213 sayılı Vergi Usul Kanunu m. 233',
    ),
    # düzey 2
    '0041': patch(
        'Bir mükellefin 2024 hesap dönemi daha önce incelenmiş ve matrah farkı bulunmuştur. Aynı dönem için yeni bir ihbar üzerine ikinci kez inceleme yapılmak istenmektedir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Yeniden inceleme için mahkeme kararı gerekir',
            'B': 'İkinci inceleme mükellefin iznine bağlıdır',
            'C': 'Aynı dönem, önceki rapor kesinleştiği için tarh zamanaşımı içinde ikinci kez incelenemez',
            'D': 'Önceki raporda değinilmeyen hesaplarla sınırlı inceleme yapılır',
            'E': 'Önceki inceleme, yeniden inceleme ve ikmal tarhiyatına engel değildir',
        },
        'E',
        "m. 138'e göre inceleme, tarh zamanaşımı süresi sonuna kadar her zaman yapılabilir ve **evvelce inceleme yapılmış veya matrahın re'sen takdir edilmiş olması yeniden inceleme yapılmasına ve gerekirse tarhiyatın ikmaline mani değildir**.",
        '213 sayılı Vergi Usul Kanunu m. 138',
    ),
    # düzey 3
    '0042': patch(
        'İşyerinde yürütülen bir vergi incelemesine ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Tutanak düzenlenmesi mesai dışında da yapılabilir',
            'B': 'Mükellef rıza göstermese de mesai dışında incelemeye devam edilebilir',
            'C': 'İnceleme bitince yapıldığını gösteren bir belge verilir',
            'D': 'İnceleme elemanı gerektiğinde işyerinin her tarafını gezip görebilir',
            'E': 'Mükellef inceleme elemanına çalışma yeri göstermekle yükümlüdür',
        },
        'B',
        "m. 140/3'e göre incelemenin işyerinde yapılması hâlinde, nezdinde inceleme yapılanın **muvafakatı olmadıkça resmî çalışma saatleri dışında inceleme yapılamaz veya devam edilemez**; tutanak düzenlenmesi ve emniyet tedbirleri bu hükmün dışındadır. m. 140/4 inceleme bitince belge verilmesini, m. 257 çalışma yeri gösterme ve işyerini gezdirme ödevlerini düzenler.",
        '213 sayılı Vergi Usul Kanunu m. 140, 257',
    ),
    # düzey 3
    '0043': patch(
        'Bir ihbar üzerine mükellefin işyerinde arama yapılmış, ancak ihbarın doğru olmadığı anlaşılmıştır. Mükellef ihbarı yapanın adını öğrenmek istemektedir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Muhbirin adı istihbarat arşivinde saklanır ve verilmez',
            'B': 'Mükellef isterse vergi dairesi muhbirin adını bildirir',
            'C': 'Muhbirin adı mahkeme kararıyla açıklanabilir',
            'D': 'Muhbirin kimliği vergi mahremiyeti gereği gizli tutulur',
            'E': 'Muhbir adı ancak ceza soruşturmasında açıklanır',
        },
        'B',
        "m. 142'ye göre arama, vergi incelemesine yetkili olanın gerekçeli yazıyla istemi ve **sulh ceza hâkiminin kararıyla** yapılır. **İhbar üzerine yapılan aramada ihbar sabit olmazsa**, nezdinde arama yapılan kimse muhbirin adının bildirilmesini isteyebilir ve **vergi dairesi muhbirin ismini bildirmeye mecburdur**.",
        '213 sayılı Vergi Usul Kanunu m. 142',
    ),
    # düzey 2
    '0044': patch(
        'Bir banka, Mart ayında mevduat sahiplerinden birinin öldüğünü öğrenmiştir. Banka bu durumu vergi dairesine en geç ne zamana kadar bildirmelidir?',
        {
            'A': "15 Mart'a kadar",
            'B': "31 Mart'a kadar",
            'C': '15 Nisan akşamına kadar',
            'D': "30 Nisan'a kadar",
            'E': 'Ölümden itibaren 10 gün içinde',
        },
        'C',
        "m. 150'ye göre sulh yargıçları, icra, nüfus ve tapu memurları, muhtarlar ile **bankalar**, her ay muttali oldukları ölüm vakalarını ve intikalleri **ertesi ayın 15. günü akşamına kadar** vergi dairesine yazıyla bildirmek zorundadır.",
        '213 sayılı Vergi Usul Kanunu m. 150',
    ),
    # düzey 3
    '0045': patch(
        'Kazancı bilanço esasına göre tespit edilen bir tüccar ölmüş; üç mirasçısından biri mirası reddetmiştir. Ölüm bildirimi hakkında aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Bildirimi nüfus müdürlüğü yaptığından mirasçıların ödevi yoktur',
            'B': 'Mirası reddeden mirasçı da bildirimle yükümlüdür',
            'C': 'Ölüm işi bırakma sayılmadığından bildirim gerekmez',
            'D': 'Reddetmeyen mirasçılardan birinin bildirimi diğerini de bu ödevden kurtarır',
            'E': 'Mirası reddeden dâhil üç mirasçı da bildirimi ayrı ayrı ve kendi adlarına yapmalıdır',
        },
        'D',
        "m. 164'e göre **ölüm işi bırakma hükmündedir** ve mükellefin **mirası reddetmemiş mirasçıları** tarafından bildirilir; **mirasçılardan herhangi birinin ölümü bildirmesi diğer mirasçıları bu ödevden kurtarır**.",
        '213 sayılı Vergi Usul Kanunu m. 164',
    ),
    # düzey 2
    '0046': patch(
        'Bilanço esasına göre defter tutan bir işletme, muhasebe fişlerine dayanarak kayıt yapmaktadır. Fişlere işlenen işlemler esas defterlere en geç kaç gün içinde intikal ettirilmelidir?',
        {
            'A': '15',
            'B': '60',
            'C': '30',
            'D': '45',
            'E': '10',
        },
        'D',
        "m. 219'a göre kayıtların **on günden fazla geciktirilmesi caiz değildir**; ancak kayıtlarını **muhasebe fişleri, primanota, bordro** gibi mazbut vesikalara dayanarak yürüten müesseselerde bunlara işlenmesi deftere işlenmesi hükmündedir ve işlemler esas defterlere **45 günden** daha geç intikal ettirilemez.",
        '213 sayılı Vergi Usul Kanunu m. 219',
    ),
    # düzey 2
    '0047': patch(
        'Bir anonim şirketin kuruluş aşamasında kullanacağı defterler aşağıdakilerden hangisi tarafından tasdik edilir?',
        {
            'A': 'Şirket merkezinin bulunduğu yer ticaret sicili müdürlüğü',
            'B': 'Şirketin bağlı olduğu meslek odası',
            'C': 'Şirket merkezinin bulunduğu yerdeki vergi dairesi müdürlüğü',
            'D': 'Serbest muhasebeci mali müşavir',
            'E': 'İl defterdarlığı',
        },
        'A',
        "m. 223'e göre defterler kural olarak iş yerinin bulunduğu yerdeki **noter** tarafından tasdik edilir; **anonim ve limited şirketler ile kooperatiflerin kuruluş aşamasında** ise defterler **şirket merkezinin bulunduğu yer ticaret sicili müdürlüğünce** tasdik edilir.",
        '213 sayılı Vergi Usul Kanunu m. 223',
    ),
    # düzey 3
    '0048': patch(
        'Satıcı, sattığı malı alıcıya teslim edilmek üzere kendi aracıyla taşımaktadır. Sevk irsaliyesini kim düzenlemelidir?',
        {
            'A': 'Taşıma irsaliyesi düzenlendiği için gerek yoktur',
            'B': 'Alıcı',
            'C': 'Alıcı ile satıcı birlikte',
            'D': 'Taşımayı yapan şoför',
            'E': 'Satıcı',
        },
        'E',
        "m. 230/5'e göre malın alıcıya teslim edilmek üzere **satıcı tarafından taşındığı veya taşıttırıldığı** hâllerde **satıcının**, alıcı tarafından taşınması hâlinde **alıcının** sevk irsaliyesi düzenlemesi ve taşıtta bulundurması şarttır.",
        '213 sayılı Vergi Usul Kanunu m. 230/5',
    ),
    # düzey 2
    '0049': patch(
        'Bir tüccar, gerçek usulde vergilendirilmeyen bir çiftçiden zirai ürün satın almıştır. Tüccarın düzenlemesi gereken belge aşağıdakilerden hangisidir?',
        {
            'A': 'Fatura',
            'B': 'Gider pusulası',
            'C': 'Serbest meslek makbuzu',
            'D': 'Müstahsil makbuzu',
            'E': 'Perakende satış fişi',
        },
        'D',
        "m. 235'e göre tüccarlar ve defter tutmak zorunda olan çiftçiler, **gerçek usulde vergiye tabi olmayan çiftçilerden** satın aldıkları malların bedelini öderken iki nüsha **müstahsil makbuzu** düzenler; makbuzun alıcıda kalan nüshası fatura yerine geçer. m. 234 bu alımları gider pusulasının dışında tutar.",
        '213 sayılı Vergi Usul Kanunu m. 235',
    ),
    # düzey 2
    '0050': patch(
        'Aşağıdaki belge-düzenleyen eşleştirmelerinden hangisi yanlıştır?',
        {
            'A': 'Gider pusulası — malı satın alan tüccar',
            'B': 'Serbest meslek makbuzu — alıcı tüccar',
            'C': 'Müstahsil makbuzu — ürünü satın alan tüccar',
            'D': 'Fatura — malı satan tüccar',
            'E': 'Sevk irsaliyesi — malı taşıyan satıcı',
        },
        'B',
        "m. 236'ya göre **serbest meslek makbuzunu, tahsilatı yapan serbest meslek erbabı** düzenler ve müşteriye verir. Müstahsil makbuzu (m. 235) ve gider pusulası (m. 234) **alıcı tarafından**, fatura (m. 229) satıcı tarafından düzenlenir; sevk irsaliyesini malı taşıyan taraf düzenler.",
        '213 sayılı Vergi Usul Kanunu m. 229-236',
    ),
    # düzey 2
    '0051': patch(
        "Vergi Usul Kanunu'nda 7338 sayılı Kanunla tanımlanan 'alış bedeli' aşağıdakilerden hangisini ifade eder?",
        {
            'A': 'Senet üzerinde yazılı değeri',
            'B': 'Değerleme günündeki borsa fiyatını',
            'C': 'Satın alma bedeli ile tüm iktisap giderlerini',
            'D': 'Muhasebe kayıtlarındaki hesap değerini',
            'E': 'İktisap giderleri hariç satın alma bedelini',
        },
        'E',
        "m. 268/A'ya göre **alış bedeli, bir iktisadi kıymetin satın alma bedelidir; iktisapla ilgili diğer giderler alış bedeline dâhil değildir**. İktisap giderleriyle birlikte toplam maliyet bedelidir (m. 262); muhasebe kaydındaki değer mukayyet değer, senet üzerindeki değer itibari değerdir.",
        '213 sayılı Vergi Usul Kanunu m. 268/A (7338 sayılı Kanunla eklendi)',
    ),
    # düzey 3
    '0052': patch(
        'Değerleme günündeki mevcudu 1.000 adet olan bir malın emsal bedeli belirlenecektir. Birinci sıradaki ortalama fiyat esasının uygulanabilmesi için ilgili ayda en az kaç adet satış yapılmış olmalıdır?',
        {
            'A': '350',
            'B': '400',
            'C': '1.000',
            'D': '500',
            'E': '250',
        },
        'E',
        "m. 267'ye göre emsal bedeli sırayla ortalama fiyat, maliyet bedeli ve takdir esasına göre belirlenir. Ortalama fiyat esasının uygulanması için **aylık satış miktarının, emsal bedeli tayin olunacak malın miktarına nazaran %25'ten az olmaması** şarttır: 1.000 × %25 = **250 adet**.",
        '213 sayılı Vergi Usul Kanunu m. 267',
    ),
    # düzey 3
    '0053': patch(
        'Bir işletme Eylül ayında aktifine aldığı üretim makinesi için kıst amortisman uygulamak istemektedir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Dileyen mükellef kullanıma hazır olduğu tarihten itibaren kıst amortisman ayırabilir',
            'B': 'Kıst amortisman için Bakanlık izni gerekir',
            'C': 'Makine için ilk yıl amortisman ayrılamaz',
            'D': 'Makinede kıst amortisman zorunludur',
            'E': 'Kıst amortisman sadece binek otomobillerinde uygulanabilir; makinelerde tam yıl ayrılır',
        },
        'A',
        "7338 sayılı Kanunla m. 320'ye eklenen fıkraya göre **dileyen mükellefler**, aktife yeni kaydedilen iktisadi kıymetler için amortismana **kullanıma hazır olduğu tarihte başlayıp** ay kesrini tam ay sayarak kalan ay süresi kadar ayırabilir. Binek otomobillerinde kıst uygulama ise zorunludur.",
        '213 sayılı Vergi Usul Kanunu m. 320 (7338 sayılı Kanunla eklenen fıkra)',
    ),
    # düzey 2
    '0054': patch(
        "Bir mükellef inceleme sonucu 120.000 ₺ vergi ziyaına sebebiyet vermiş; fiil sahte belge kullanma niteliğinde değildir. Kesilecek vergi ziyaı cezası kaç ₺'dir?",
        {
            'A': '180.000',
            'B': '360.000',
            'C': '120.000',
            'D': '60.000',
            'E': '240.000',
        },
        'C',
        "m. 344/1'e göre m. 341'deki hâllerde vergi ziyaına sebebiyet verilirse **ziyaa uğratılan verginin bir katı** tutarında vergi ziyaı cezası kesilir: **120.000 ₺**. m. 359'daki fiillerle ziyaa sebebiyet verilseydi ceza üç kat (360.000 ₺) olurdu.",
        '213 sayılı Vergi Usul Kanunu m. 344',
    ),
    # düzey 3
    '0055': patch(
        "Beyannamesini kanuni süresinde vermeyen bir mükellef, hakkında vergi incelemesine başlandıktan sonra beyannamesini vermiştir. Beyanname üzerine 40.000 ₺ vergi tahakkuk etmiştir. Kesilecek vergi ziyaı cezası kaç ₺'dir?",
        {
            'A': '40.000',
            'B': '120.000',
            'C': '20.000',
            'D': '30.000',
            'E': '10.000',
        },
        'A',
        "m. 344/3'e göre **vergi incelemesine başlanılmasından veya takdir komisyonuna sevkten sonra verilenler hariç**, kanuni süresi geçtikten sonra verilen beyannameler için vergi ziyaı cezası **%50 oranında** uygulanır. Beyanname **inceleme başladıktan sonra** verildiğinden indirimli oran uygulanmaz; ceza bir kat: **40.000 ₺**. İnceleme başlamadan verilseydi 20.000 ₺ olurdu.",
        '213 sayılı Vergi Usul Kanunu m. 344/3',
    ),
    # düzey 3
    '0056': patch(
        'Bir alıcı, satıcının kendisine fatura düzenlemediğini idare bu durumu öğrenmeden önce, faturanın düzenlenmesi gereken süreyi takip eden beş iş günü içinde vergi dairesine bildirmiştir. Aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Satıcıya ceza kesilmez, alıcıya kesilir',
            'B': 'Alıcıya ceza yarı oranda kesilir, satıcıya ise cetveldeki tutarın tamamı uygulanır',
            'C': 'Her iki tarafa da ceza kesilmez',
            'D': 'Alıcıya ceza kesilmez; satıcıya ceza üç kat uygulanır',
            'E': 'Her iki tarafa ceza iki kat uygulanır',
        },
        'D',
        "7524 sayılı Kanunla m. 353/1'e eklenen hükümlere göre belgenin düzenlenmediğinin **belgeyi almak zorunda olanlarca, idarenin bilgisine girmeden önce, düzenleme süresini takip eden beş iş günü içinde** bildirilmesi hâlinde **alıcı adına ceza kesilmez**, belgeyi düzenlemek zorunda olan adına ceza **üç kat** uygulanır.",
        '213 sayılı Vergi Usul Kanunu m. 353/1 (7524 sayılı Kanunla değişik)',
    ),
    # düzey 2
    '0057': patch(
        "Vergi Usul Kanunu'na göre sahte belge ile muhteviyatı itibarıyla yanıltıcı belge arasındaki farka ilişkin aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Her iki belgede de muamele gerçektir',
            'B': 'Sahte belgede ortada gerçek bir muamele yoktur',
            'C': 'Yanıltıcı belge kullanmak suç değildir',
            'D': 'Yanıltıcı belgede ortada gerçek bir muamele yoktur',
            'E': 'İkisi için de aynı hapis cezası öngörülmüştür',
        },
        'B',
        "m. 359'a göre **gerçek bir muamele veya durum olmadığı hâlde bunlar varmış gibi düzenlenen belge sahte**; **gerçek bir muameleye dayanmakla birlikte bunu mahiyet veya miktar itibarıyla gerçeğe aykırı yansıtan belge yanıltıcı** belgedir. Yanıltıcı belge (359/a) 18 ay-5 yıl, sahte belge (359/b) 3-8 yıl hapisle cezalandırılır.",
        '213 sayılı Vergi Usul Kanunu m. 359',
    ),
    # düzey 2
    '0058': patch(
        'Kaçakçılık suçlarına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'İzinsiz belge basmak hapis cezasını gerektirir',
            'B': 'Hapis cezasına hükmedilmesi vergi ziyaı cezası kesilmesine engeldir',
            'C': 'Varlığı noter tasdikiyle sabit defterlerin incelemede ibraz edilmemesi gizleme sayılır',
            'D': 'Defter ve belgeleri yok etmek kaçakçılık suçudur',
            'E': 'Pişmanlık şartlarına uygun bildirimde m. 359 uygulanmaz',
        },
        'B',
        "m. 359'un son fıkrasına göre **kaçakçılık suçlarını işleyenler hakkında hapis cezasının uygulanması, m. 344'teki vergi ziyaı cezasının ayrıca uygulanmasına engel teşkil etmez**. Diğer ifadeler m. 359'un (a), (b), (c) bentleri ve pişmanlık fıkrasına uygundur.",
        '213 sayılı Vergi Usul Kanunu m. 359, 344',
    ),
    # düzey 3
    '0059': patch(
        'Aşağıdaki bildirimlerden hangileri bir ay içinde yapılmalıdır?\n\nI. Gerçek kişinin işe başlama bildirimi\n\nII. İşi bırakma bildirimi\n\nIII. İşyeri adres değişikliği bildirimi',
        {
            'A': 'Yalnız III',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'II ve III',
            'E': 'Yalnız II',
        },
        'D',
        "m. 168'e göre **gerçek kişilerde işe başlama bildirimi on gün içinde** (I); **işi bırakma ve değişiklik bildirimleri** ise olayın vukuundan itibaren **bir ay içinde** (II, III) yapılır. m. 163'e göre işin başka yere nakli adres değişikliği sayılır.",
        '213 sayılı Vergi Usul Kanunu m. 163, 168',
    ),
    # düzey 2
    '0060': patch(
        'Defter tutma zorunluluğu olmayan bir ücretli, aldığı faturaları hangi süreyle saklamakla yükümlüdür?',
        {
            'A': 'Düzenlendikleri yılı izleyen yıldan itibaren beş yıl',
            'B': 'Beyanname verme süresi sonuna kadar',
            'C': 'On yıl',
            'D': 'Düzenlendikleri yıl sonuna kadar',
            'E': 'Saklama yükümlülüğü yoktur',
        },
        'A',
        "m. 254'e göre **defter tutmak zorunda olmayanlar**, m. 232, 234 ve 235'e göre almak zorunda oldukları fatura, gider pusulası ve müstahsil makbuzlarını **tanzim tarihlerini takip eden takvim yılından başlayarak beş yıl** süreyle muhafaza eder.",
        '213 sayılı Vergi Usul Kanunu m. 254',
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
    print(f"1 paket / {len(PATCHES)} soru ('Vergi Usul Kanunu' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
