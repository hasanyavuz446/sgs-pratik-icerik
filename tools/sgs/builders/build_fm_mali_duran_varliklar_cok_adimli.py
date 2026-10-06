#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mali Duran Varliklar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

FM cok adimli tur (hafif). TMS 27/28 ve TFRS 10 sorulari korundu: bu standartlarin ayri paketi yok ve gercek sinavda ~6 soru geciyor. Ilk turdan kalan 44 mutlak ifadeli celdirici yanlisligi korunarak yeniden yazildi. 6 'hangi hesapta izlenir' ezberi yerine: istirake kismen odenen sermaye taahhudu (243), payi %50 altina dusen bagli ortakligin 242'ye aktarilmasi, net mali duran varlik toplami, ozkaynak yonteminde temettunun etkisi, kar+temettu+DKG ile ozkaynak yontemi defter degeri, olumsuz siniflandirma. Kor ogrenci %23.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Tekduzen Hesap Plani 24 Mali Duran Varliklar · TMS 27, TMS 28, TFRS 10 · VUK m. 279
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/finansal_muhasebe/mali_duran_varliklar.json"
STYLE_REF = 'SGS Finansal Muhasebe (çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "finmuh-malidv-gen-"


def patch(stem, options, answer, solution, ref='Tekduzen Hesap Plani 24; TMS 28'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Aşağıdaki hesaplardan hangisi '24 Mali Duran Varlıklar' grubunda yer almaz?",
        {
            'A': '248 Diğer Mali Duran Varlıklar',
            'B': '245 Bağlı Ortaklıklar',
            'C': '242 İştirakler',
            'D': '110 Hisse Senetleri',
            'E': '240 Bağlı Menkul Kıymetler',
        },
        'D',
        "**110 Hisse Senetleri**, kısa vadeli (bir yıl içinde elden çıkarılmak üzere tutulan) menkul kıymetleri izler ve '11 Menkul Kıymetler' grubundadır. Diğerleri (240, 242, 245, 248) uzun vadeli olup 24 grubundadır.",
        "1 Sıra No'lu MSUGT - 11 / 24 grupları",
    ),
    # düzey 2
    '0002': patch(
        "İştirak ve bağlı ortaklık kapsamına girmeyen, uzun vadeli amaçla elde tutulan ve sermaye payı %10'un altında olan menkul kıymetler Tekdüzen Hesap Planı'nda hangi hesapta izlenir?",
        {
            'A': '110 Hisse Senetleri',
            'B': '240 Bağlı Menkul Kıymetler',
            'C': '245 Bağlı Ortaklıklar',
            'D': '108 Diğer Hazır Değerler',
            'E': '242 İştirakler',
        },
        'B',
        "İştirak/bağlı ortaklık kapsamı dışında, **uzun vadeli** elde tutulan ve payı **%10'un altında** olan menkul kıymetler **240 Bağlı Menkul Kıymetler** hesabında izlenir (kısa vadeli olsaydı 110 Hisse Senetleri'nde izlenirdi).",
        "1 Sıra No'lu MSUGT - 240 Bağlı Menkul Kıymetler",
    ),
    # düzey 2
    '0003': patch(
        "İşletme dönem içinde şu ortaklık paylarını uzun süre elde tutmak amacıyla edinmiştir: X A.Ş.'nin sermayesinin %4'ü için 50.000 ₺, Y A.Ş.'nin %20'si için 300.000 ₺, Z A.Ş.'nin %70'i için 900.000 ₺ ve W A.Ş.'nin %35'i için 450.000 ₺. Ayrıca borsada kısa sürede satmak üzere V A.Ş.'nin %8'ini temsil eden hisseler 60.000 ₺'ye alınmıştır.\n\nTekdüzen Hesap Planı'na göre '242 İştirakler' hesabına kaydedilecek toplam tutar kaç ₺'dir?",
        {
            'A': '1.700.000',
            'B': '800.000',
            'C': '750.000',
            'D': '1.200.000',
            'E': '1.650.000',
        },
        'C',
        "Sermayesine %10 ile %50 arasında katılınan işletmeler iştiraktir: Y (%20) 300.000 ₺ + W (%35) 450.000 ₺ = 750.000 ₺. %50'nin üzerindeki Z payı 245 Bağlı Ortaklıklar, %10'un altındaki uzun vadeli X payı 240 Bağlı Menkul Kıymetler, kısa vadeli satış amaçlı V hisseleri 110 Hisse Senetleri hesabında izlenir.",
        "1 Sıra No'lu MSUGT - 240 Bağlı Menkul Kıymetler",
    ),
    # düzey 2
    '0004': patch(
        "Bir işletme başka bir şirketin oy haklarının %22'sini elinde tutmaktadır. Aksini açıkça gösteren herhangi bir kanıt bulunmamaktadır. TMS 28'e göre bu yatırım için öncelikle hangi sonuca ulaşılır?",
        {
            'A': 'Aksi açıkça ortaya konulmadıkça önemli etkinin bulunduğu varsayılır.',
            'B': "Oy hakkı %50'yi aşmadığından önemli etki yoktur.",
            'C': 'Önemli etki ancak payların uzun vadeli tutulması hâlinde vardır.',
            'D': "Oy hakkı %10'u aştığı için sözleşmeler ve diğer haklar ayrıca incelenmeden kontrolün bulunduğu kesin kabul edilir.",
            'E': 'Yatırım doğrudan TFRS 10 kapsamında bağlı ortaklık sayılır.',
        },
        'A',
        "TMS 28'e göre doğrudan veya dolaylı **%20 ya da daha fazla oy hakkı**, aksi açıkça ortaya konulmadıkça önemli etkinin bulunduğuna ilişkin bir varsayım oluşturur. Bu varsayım kesin ve çürütülemez değildir.",
        'TMS 28 İştiraklerdeki ve İş Ortaklıklarındaki Yatırımlar, par. 5',
    ),
    # düzey 3
    '0005': patch(
        'Aşağıdakilerden hangisi mali duran varlık niteliğinde değildir?',
        {
            'A': 'Bağlı ortaklık payı',
            'B': 'Uzun vadeli amaçla alınan iştirak payı',
            'C': 'Diğer uzun vadeli menkul kıymet yatırımı',
            'D': 'Uzun vadeli elde tutulan bağlı menkul kıymet',
            'E': 'İşletmenin üretimde kullandığı makine',
        },
        'E',
        'İşletmenin üretimde kullandığı **makine**, fiziki bir **maddi duran varlıktır** (253); mali duran varlık değildir. Diğerleri uzun vadeli finansal yatırımlardır (24 grubu).',
        "1 Sıra No'lu MSUGT - 24 / 25 ayrımı",
    ),
    # düzey 2
    '0006': patch(
        "Bir işletme yatırım yapılan şirketin oy haklarının %15'ine sahiptir. Buna karşılık yönetim kurulunda temsil edilmekte, temettü politikası kararlarına katılmakta ve şirkete gerekli teknik bilgiyi sağlamaktadır. TMS 28'e göre en uygun değerlendirme hangisidir?",
        {
            'A': 'Bu koşullar müşterek kontrol bulunduğunu gösterir.',
            'B': 'Sermaye payı dikkate alınır; yönetim kurulundaki temsil önemsizdir.',
            'C': 'Teknik bilgi sağlanması yatırımcıyı ana ortaklık yapar.',
            'D': "Oy hakkı %20'nin altında olsa da mevcut göstergeler önemli etkinin bulunduğunu açıkça ortaya koyabilir.",
            'E': "Oy hakkı %20'nin altında olduğundan yönetim kurulundaki temsil, politika kararlarına katılma ve teknik bilgi sağlama kanıtları incelenmeden önemli etki reddedilir.",
        },
        'D',
        "%20'nin altındaki oy hakkı önemli etkinin bulunmadığına ilişkin bir varsayımdır; fakat aksi açıkça kanıtlanabilir. **Yönetim kurulunda temsil, politika belirleme süreçlerine katılma ve gerekli teknik bilginin sağlanması** TMS 28'de önemli etki göstergeleri arasında sayılmıştır.",
        'TMS 28, par. 5-6',
    ),
    # düzey 3
    '0007': patch(
        "İşletme, %30 pay sahibi olduğu iştirak yatırımını özkaynak yöntemiyle 500.000 ₺ maliyetle kaydetmiştir. İştirak dönem içinde 200.000 ₺ kâr açıklamış ve toplam 100.000 ₺ temettü dağıtmıştır. Başka değişiklik yoksa yatırımın dönem sonu defter değeri kaç ₺'dir?",
        {
            'A': '530.000',
            'B': '560.000',
            'C': '500.000',
            'D': '620.000',
            'E': '590.000',
        },
        'A',
        'Kârdan pay 200.000 × %30 = **60.000 ₺** olup yatırımın defter değerini artırır. Dağıtılan temettüden pay 100.000 × %30 = **30.000 ₺** olup defter değerini azaltır. Son değer 500.000 + 60.000 − 30.000 = **530.000 ₺**dir.',
        'TMS 28, par. 10',
    ),
    # düzey 2
    '0008': patch(
        "İşletme kısa vadeli amaçla aldığı ve '110 Hisse Senetleri'nde izlediği bir yatırımı, artık uzun vadeli/ortaklık amacıyla elde tutmaya karar vermiştir (pay %30). Bu durumda ne yapılır?",
        {
            'A': "Yatırımın niteliği değiştiğinden kayıtlı değeri 654 Karşılık Giderleri'ne borç yazılarak dönem gideri olarak muhasebeleştirilir.",
            'B': "Pay oranı kontrol sağlayacak düzeye ulaştığından yatırım 110 Hisse Senetleri'nden çıkarılıp doğrudan 245 Bağlı Ortaklıklar hesabına aktarılmalıdır.",
            'C': "Yatırım bir yıl içinde satılacak stok kalemine dönüştüğünden 110 Hisse Senetleri'nden çıkarılıp 153 Ticari Mallar hesabına aktarılmalıdır.",
            'D': 'Hesaplar arasında aktarma yapılmaz; elde tutma amacı değişse de yatırım 110 Hisse Senetleri hesabında izlenmeye devam eder.',
            'E': "Yatırım, uzun vadeli ve %10–%50 pay niteliğine geçtiğinden 110 Hisse Senetleri'nden çıkarılıp 242 İştirakler hesabına aktarılır.",
        },
        'E',
        "Elde tutma amacı kısa vadeliden uzun vadeliye (ve pay %10–%50'ye) dönüştüğünden yatırım **110 Hisse Senetleri'nden 242 İştirakler**'e aktarılır. Sınıflama, amaç ve orana göre belirlenir.",
        "1 Sıra No'lu MSUGT - 110 / 242",
    ),
    # düzey 2
    '0009': patch(
        'İştirakler ve bağlı ortaklıklar için ayrılan değer düşüklüğü karşılığı hesaplarının (244, 247) ortak niteliği aşağıdakilerden hangisidir?',
        {
            'A': 'İştiraklerden sağlanan temettüleri gösteren gelir hesaplarıdır; alacak kalanı verir ve gelir tablosuna aktarılır.',
            'B': 'Bir yıl içinde ödenecek kısa vadeli borç hesaplarıdır; alacak kalanı verir ve bilançonun pasifinde yer alır.',
            'C': 'Aktifi düzenleyici (kontr aktif) hesaplardır; alacak kalanı verir ve ilgili mali duran varlıktan (-) düşülür.',
            'D': 'İşletme sahiplerinin haklarını gösteren özkaynak hesaplarıdır; alacak kalanı verir ve bilançonun pasifinde sunulur.',
            'E': 'Üretim maliyetine yüklenen maliyet hesaplarıdır; borç kalanı verir ve dönem sonunda ilgili stoklara devredilir.',
        },
        'C',
        '**244 ve 247** değer düşüklüğü karşılıkları, aktifi düzenleyici (kontr aktif) hesaplardır; **alacak kalanı** verir ve ilgili iştirak/bağlı ortaklık tutarından **(-)** düşülerek net değeri gösterir.',
        "1 Sıra No'lu MSUGT - 244 / 247",
    ),
    # düzey 2
    '0010': patch(
        'Bir işletme TMS 27 kapsamında bireysel finansal tablo hazırlamakta ve aynı yatırım kategorisinde iki iştirak bulundurmaktadır. İşletme ilk iştiraki maliyet bedeliyle, ikinci iştiraki ise geçerli bir neden göstermeksizin özkaynak yöntemiyle izlemek istemektedir. En uygun değerlendirme hangisidir?',
        {
            'A': "Bireysel finansal tablolarda iştirakler TFRS 9'a göre ölçülür, başka yöntem seçilemez.",
            'B': 'Aynı yatırım kategorisi için aynı muhasebeleştirme esası uygulanmalıdır.',
            'C': 'Her iki iştirak farklı şirkete ait olduğundan yöntemler farklı olabilir.',
            'D': 'Yöntem tutarlılığı bağlı ortaklıklar için aranır, iştirakler için aranmaz.',
            'E': "İkinci iştirakin oy hakkı %20'yi aşıyorsa mutlaka maliyet yöntemi uygulanır.",
        },
        'B',
        'TMS 27 üç muhasebeleştirme esasına izin verse de işletme **her bir yatırım kategorisi için aynı esası** uygular. Aynı kategoride bulunan iki iştirak için yatırım bazında maliyet ve özkaynak yöntemlerinin keyfî biçimde farklılaştırılması uygun değildir.',
        'TMS 27, par. 10',
    ),
    # düzey 2
    '0011': patch(
        "Aşağıdakilerden hangisi Tekdüzen Hesap Planı'nda '248 Diğer Mali Duran Varlıklar' hesabının kapsamına en uygun kalemdir?",
        {
            'A': 'İşletmenin bankalardan sağladığı ve bir yıl içinde geri ödenecek kısa vadeli kredi borçları',
            'B': 'İşletmenin faaliyetlerinde fiilen kullandığı demirbaş, döşeme ve büro donanımı gibi maddi varlıklar',
            'C': 'İşletmenin bir yıl içinde satmak amacıyla elde tuttuğu kısa vadeli nitelikli hisse senetleri',
            'D': '240–247 hesaplarının kapsamına girmeyen, uzun vadeli diğer mali (finansal) duran varlıklar',
            'E': 'İşletmenin bir yıl içinde satacağı ticari malları ile üretimde kullanacağı ilk madde ve malzemeleri',
        },
        'D',
        '**248 Diğer Mali Duran Varlıklar**; 240–247 hesaplarının kapsamına girmeyen, uzun vadeli **diğer mali (finansal) duran varlıkları** izlemek için kullanılır.',
        "1 Sıra No'lu MSUGT - 248",
    ),
    # düzey 2
    '0012': patch(
        "İştirak payında daha önce ayrılan değer düşüklüğü karşılığının, değer düşüklüğünün ortadan kalkması nedeniyle iptal edilmesi durumunda oluşan gelir Tekdüzen Hesap Planı'nda hangi hesapta izlenir?",
        {
            'A': '242 İştirakler',
            'B': '644 Konusu Kalmayan Karşılıklar',
            'C': '600 Yurt İçi Satışlar',
            'D': '640 İştiraklerden Temettü Gelirleri',
            'E': '654 Karşılık Giderleri',
        },
        'B',
        'Daha önce ayrılan karşılığın konusunun kalmaması nedeniyle iptalinde oluşan gelir **644 Konusu Kalmayan Karşılıklar** hesabına alacak yazılır (244 borçlandırılarak kapatılır).',
        "1 Sıra No'lu MSUGT - 644 / 244",
    ),
    # düzey 3
    '0013': patch(
        "İşletme, %30 pay sahibi olduğu iştirak yatırımını özkaynak yöntemiyle 600.000 ₺'den izlemektedir. İştirak 300.000 ₺ dönem kârı, 50.000 ₺ diğer kapsamlı gelir açıklamış ve toplam 100.000 ₺ temettü dağıtmıştır. Başka değişiklik yoksa aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Yatırımın defter değeri 705.000 ₺ olur; kâr payı 90.000 ₺, diğer kapsamlı gelir payı 15.000 ₺ ve temettü geliri 30.000 ₺ ayrıca raporlanır.',
            'B': 'Yatırımın defter değeri 660.000 ₺, diğer kapsamlı gelir payı dikkate alınmaz.',
            'C': "Yatırımın defter değeri 645.000 ₺, diğer kapsamlı gelire alınan pay 30.000 ₺'dir.",
            'D': "Yatırımın defter değeri 690.000 ₺, kâr veya zarara alınan pay 60.000 ₺'dir.",
            'E': 'Yatırımın defter değeri 675.000 ₺; kâr veya zarara 90.000 ₺, diğer kapsamlı gelire 15.000 ₺ pay yansıtılır.',
        },
        'E',
        'Kâr payı 300.000 × %30 = **90.000 ₺**, diğer kapsamlı gelir payı 50.000 × %30 = **15.000 ₺** ve temettü payı 100.000 × %30 = **30.000 ₺**dir. Defter değeri 600.000 + 90.000 + 15.000 − 30.000 = **675.000 ₺** olur.',
        'TMS 28, par. 10',
    ),
    # düzey 2
    '0014': patch(
        "Bir işletmenin dönem sonu kalanlarından bazıları şöyledir: 252 Binalar 900.000 ₺, 257 Birikmiş Amortismanlar 300.000 ₺, 260 Haklar 120.000 ₺, 268 Birikmiş Amortismanlar 40.000 ₺, 242 İştirakler 500.000 ₺, 240 Bağlı Menkul Kıymetler 100.000 ₺, 280 Gelecek Yıllara Ait Giderler 30.000 ₺, 110 Hisse Senetleri 80.000 ₺, 153 Ticari Mallar 200.000 ₺.\n\nBuna göre bu kalemlerden bilançonun duran varlıklar bölümünde yer alanların net toplamı kaç ₺'dir?",
        {
            'A': '1.280.000',
            'B': '1.350.000',
            'C': '1.390.000',
            'D': '1.210.000',
            'E': '1.310.000',
        },
        'E',
        'Duran varlıklar: maddi duran varlık 900.000 − 300.000 = 600.000 ₺; maddi olmayan duran varlık 120.000 − 40.000 = 80.000 ₺; mali duran varlıklar 500.000 + 100.000 = 600.000 ₺; gelecek yıllara ait giderler 30.000 ₺. Toplam 1.310.000 ₺. 110 Hisse Senetleri ve 153 Ticari Mallar dönen varlıktır.',
        "1 Sıra No'lu MSUGT - 24/25/26",
    ),
    # düzey 2
    '0015': patch(
        "Bir yatırımcı, hâlen kullanılabilir durumda olan ve kullanıldığında yatırım yapılan işletmede ilave oy hakkı sağlayacak pay alım opsiyonlarına sahiptir. TMS 28'e göre önemli etki değerlendirmesinde bu haklar için hangi işlem yapılır?",
        {
            'A': 'Opsiyonlar yatırımcıya kontrol sağlar.',
            'B': 'Potansiyel oy hakları dikkate alınmaz.',
            'C': 'Mevcut durumda kullanılabilir potansiyel oy haklarının varlığı ve etkisi değerlendirmede dikkate alınır.',
            'D': 'Potansiyel oy hakları raporlama tarihinde kullanılabilir durumda olsa bile ancak fiilen kullanıldıktan sonraki hesap döneminin önemli etki değerlendirmesine alınır.',
            'E': 'Önemli etki ancak yönetimin opsiyonu kullanma niyeti varsa doğar.',
        },
        'C',
        'TMS 28, **hâlen kullanılabilir veya dönüştürülebilir** potansiyel oy haklarının önemli etki değerlendirmesinde dikkate alınmasını ister. Yönetimin bu hakları kullanma isteği veya finansal yeterliliği tek başına belirleyici değildir.',
        'TMS 28, par. 7-8',
    ),
    # düzey 2
    '0016': patch(
        'İşletme, özkaynak yöntemiyle izlediği iştirakte %25 pay sahibidir. İştirak dönem içinde 120.000 ₺ tutarında diğer kapsamlı gelir muhasebeleştirmiştir. Başka değişiklik yoksa yatırımcı hangi işlemi yapar?',
        {
            'A': 'Diğer kapsamlı gelir yatırımcıyı etkilemediği için kayıt yapmaz.',
            'B': "30.000 ₺'yi kendi diğer kapsamlı gelirine yansıtır ve yatırımın defter değerini aynı tutarda artırır.",
            'C': "120.000 ₺'nin tamamını temettü geliri yazar.",
            'D': "120.000 ₺'yi yatırımın defter değerinden düşer.",
            'E': "30.000 ₺'yi kâr veya zararda iştirak kazancı olarak muhasebeleştirir; diğer kapsamlı gelire pay yansıtmaz ve yatırımın defter değerini değiştirmez.",
        },
        'B',
        'Yatırımcı, iştirakin diğer kapsamlı gelirinden payına düşen 120.000 × %25 = **30.000 ₺**yi kendi diğer kapsamlı gelirinde muhasebeleştirir. Bu tutar aynı zamanda özkaynak yöntemiyle izlenen yatırımın defter değerini artırır.',
        'TMS 28, par. 10',
    ),
    # düzey 3
    '0017': patch(
        "İşletme aynı iştirake ait paylardan önce 100 adedini birim 80 ₺'ye, daha sonra 100 adedini birim 100 ₺'ye almıştır. Payların 120 adedi birim 130 ₺'ye satılmıştır. Kısmi satışta ilk giren ilk çıkar yöntemi uygulandığına göre satılan payların maliyeti kaç ₺'dir?",
        {
            'A': '10.800',
            'B': '15.600',
            'C': '9.600',
            'D': '10.000',
            'E': '12.000',
        },
        'D',
        'İlk giren ilk çıkar yönteminde önce ilk alınan 100 payın 100 × 80 = **8.000 ₺**, sonra ikinci partiden 20 payın 20 × 100 = **2.000 ₺** maliyeti satışa verilir. Toplam maliyet **10.000 ₺**dir.',
        'VUK m. 279; GİB iştirak hissesi kısmi satışlarında maliyet tespiti görüşü',
    ),
    # düzey 2
    '0018': patch(
        "Bir ana ortaklık, bağlı ortaklığının kontrolünü 1 Nisan'da elde etmiş ve 30 Eylül'de kaybetmiştir. TFRS 10'a göre bağlı ortaklığın gelir ve giderleri hangi dönem için konsolide finansal tablolara dâhil edilir?",
        {
            'A': 'Pay oranı %100 ise 1 Nisan-30 Eylül arası için',
            'B': '30 Eylül tarihindeki bir günlük dönem için',
            'C': 'Kontrol kaybedildikten sonraki dönem için',
            'D': 'Kontrol yılın bir bölümünde bulunmuş olsa da 1 Ocak-31 Aralık arasındaki tüm hesap dönemi için',
            'E': "Kontrolün elde edildiği 1 Nisan'dan kaybedildiği 30 Eylül'e kadar",
        },
        'E',
        "TFRS 10'a göre bağlı ortaklığın gelir ve giderleri, ana ortaklığın **kontrol sahibi olduğu tarihten kontrolü kaybettiği tarihe kadar** konsolide finansal tablolara alınır. Bu nedenle dönem 1 Nisan-30 Eylül'dür.",
        'TFRS 10, B88',
    ),
    # düzey 3
    '0019': patch(
        "İşletme yeni kurulan bir şirkete %30 oranında iştirak etmek üzere 500.000 ₺ sermaye taahhüt etmiş ve taahhüdün %40'ını hemen banka havalesiyle ödemiştir. Kalan tutar izleyen yıl ödenecektir. Buna göre bu işlemin kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '331 Ortaklara Borçlar hesabı 300.000 ₺ alacaklandırılır',
            'B': '243 İştiraklere Sermaye Taahhütleri hesabı 500.000 ₺ alacaklandırılır',
            'C': '243 İştiraklere Sermaye Taahhütleri hesabı 300.000 ₺ alacaklandırılır',
            'D': '102 Bankalar hesabı 500.000 ₺ alacaklandırılır',
            'E': '242 İştirakler hesabı 200.000 ₺ borçlandırılır',
        },
        'C',
        "Kayıt: 242 (borç) 500.000 / 102 (alacak) 200.000 + **243 (alacak) 300.000**. İştirak payı taahhüt edilen tutarla kaydedilir; ödenmeyen kısım aktifi düzenleyen 243'te izlenir ve bilançoda 242'den düşülür.",
        'THP 242, 243, 102',
    ),
    # düzey 3
    '0020': patch(
        "İşletme %40 pay sahibi olduğu iştirakini TMS 28'e göre özkaynak yöntemiyle izlemektedir. İştirak dönem içinde ortaklarına toplam 200.000 ₺ nakit temettü dağıtmıştır. Buna göre temettünün işletmenin finansal tablolarına etkisi aşağıdakilerden hangisidir?",
        {
            'A': 'Yatırımın defter değeri 80.000 ₺ azalır',
            'B': 'Yatırımın defter değeri değişmez',
            'C': 'Yatırımın defter değeri 200.000 ₺ azalır',
            'D': '80.000 ₺ temettü geliri kâr veya zarara yazılır',
            'E': 'Yatırımın defter değeri 80.000 ₺ artar',
        },
        'A',
        'Özkaynak yönteminde yatırımcının payına düşen kâr yatırımı artırarak gelir yazılır; dağıtılan temettü ise yatırımın bir kısmının geri alınmasıdır ve **defter değerini azaltır**: 200.000 × %40 = 80.000 ₺. Temettü ayrıca gelir yazılmaz (gelir, kârın payı olarak zaten alınmıştır).',
        'TMS 28 p. 10 (özkaynak yöntemi)',
    ),
    # düzey 2
    '0021': patch(
        "Tekdüzen Hesap Planı'ndaki 242 İştirakler hesabının kapsamı ile TMS 28'deki önemli etki değerlendirmesi karşılaştırıldığında aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Tekdüzen Hesap Planı'ndaki %10 eşiği aşıldığında yatırım bağlı ortaklık sayılır.",
            'B': '242 hesabı oy hakkının %20 ile %50 arasında olduğu yatırımları kapsar; yönetim kurulunda temsil gibi başka kanıtlar dikkate alınmaz.',
            'C': "Tekdüzen Hesap Planı'nda en az %10 oy veya yönetime katılma hakkı aranır; TMS 28'de %20 oy hakkı aksi kanıtlanabilir önemli etki varsayımıdır.",
            'D': "Sermaye payı %50'yi aşmayan bütün uzun vadeli paylar, yönetime katılma hakkı aranmaksızın 242 hesabında izlenir.",
            'E': 'Tekdüzen Hesap Planı ile TMS 28 aynı yüzdeyi ve aynı değerlendirme ölçütünü kullanır.',
        },
        'C',
        "İki düzenlemenin eşiği aynı değildir. Tekdüzen Hesap Planı açıklamasında **242 İştirakler** için yönetim ve politikaya katılma ile en az **%10 oy veya yönetime katılma hakkı** aranır; pay en çok %50 olabilir. TMS 28'de ise **%20 oy hakkı**, aksi açıkça ortaya konulabilen bir **önemli etki varsayımıdır**; tek başına kesin sınıflama değildir.",
        "1 Sıra No'lu MSUGT - 242 İştirakler; TMS 28, par. 5-6",
    ),
    # düzey 2
    '0022': patch(
        "Bir hisse senedi yatırımının '11 Menkul Kıymetler' (kısa vadeli) grubunda mı yoksa '24 Mali Duran Varlıklar' (uzun vadeli) grubunda mı izleneceğini belirleyen temel ölçüt aşağıdakilerden hangisidir?",
        {
            'A': 'Hisse senedinin üzerinde yazılı olan nominal (itibari) değerinin büyüklüğü ile ihraç priminin tutarı',
            'B': 'Hisse senedini temsil eden belgenin fiziki basımı, kâğıt kalitesi ve üzerindeki renk ile desenler',
            'C': 'Hisse senedinin borsadan satın alınması sırasında ödenen alış bedeli ile komisyon tutarı',
            'D': 'Hisse senedini çıkaran şirketin ticaret unvanı ile faaliyet gösterdiği sektörün türü ve büyüklüğü',
            'E': 'İşletmenin elde tutma amacı ve süresi (kısa vadeli kâr amaçlı mı, uzun vadeli/ortaklık amaçlı mı)',
        },
        'E',
        'Belirleyici ölçüt, işletmenin **elde tutma amacı ve süresidir**: kısa vadeli kâr amacıyla tutuluyorsa 11 Menkul Kıymetler; uzun vadeli/ortaklık amacıyla tutuluyorsa 24 Mali Duran Varlıklar grubunda izlenir.',
        "1 Sıra No'lu MSUGT - 11 / 24 ayrımı",
    ),
    # düzey 2
    '0023': patch(
        "'242 İştirakler' hesabının işleyişi ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Bir gelir hesabıdır; iştirakten sağlanan temettüler tahsil edildikçe alacaklandırılır ve gelir tablosuna aktarılır.',
            'B': 'Bir pasif (kaynak) hesabıdır; iştirak payı edinildiğinde alacaklandırılır ve dönem sonunda alacak kalanı verir.',
            'C': 'Bir gider hesabıdır; iştirak payı edinildiğinde borçlandırılır ve dönem sonunda sonuç hesaplarına devredilir.',
            'D': 'Bir nazım hesaptır; izleme amacıyla tutulur ve işletmenin bilançosunda yer almaz.',
            'E': 'Bir aktif hesabıdır; iştirak payı edinildiğinde borçlandırılır, elden çıkarıldığında alacaklandırılır.',
        },
        'E',
        '**242 İştirakler** bir **aktif** hesabıdır; iştirak payı edinildiğinde **borçlandırılır (borç)**, elden çıkarıldığında **alacaklandırılır (alacak)**. Borç kalanı verir.',
        "1 Sıra No'lu MSUGT - 242",
    ),
    # düzey 3
    '0024': patch(
        "TMS 27'ye göre bireysel finansal tablolarda bağlı ortaklık, iş ortaklığı ve iştirak yatırımlarının muhasebeleştirilmesiyle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': 'Yatırımlar TFRS 9 hükümlerine göre muhasebeleştirilebilir.',
            'B': 'Aynı kategorideki her yatırım için dönemden döneme farklı bir yöntem seçilebilir.',
            'C': 'Seçilen esas, her bir yatırım kategorisi içinde tutarlı uygulanır.',
            'D': "Yatırımlar, TMS 28'de tanımlanan özkaynak yöntemi kullanılarak da bireysel finansal tablolarda muhasebeleştirilebilir.",
            'E': 'Yatırımlar maliyet bedeliyle muhasebeleştirilebilir.',
        },
        'B',
        'TMS 27; bireysel finansal tablolarda maliyet, TFRS 9 veya özkaynak yöntemine izin verir. Ancak işletme seçtiği muhasebeleştirme esasını **her bir yatırım kategorisi için aynı şekilde** uygulamalıdır; aynı kategoride yatırım bazında keyfî yöntem değişikliği yapılamaz.',
        'TMS 27 Bireysel Finansal Tablolar, par. 10',
    ),
    # düzey 2
    '0025': patch(
        'Mali duran varlıklar bilançoda hangi değerle (net) gösterilir?',
        {
            'A': 'Maliyet (kayıtlı) bedeli − Ayrılan değer düşüklüğü karşılığı (244/247 vb.)',
            'B': 'Payların ihraç sırasındaki nominal (itibari) değerleri toplamı üzerinden',
            'C': 'Maliyet (kayıtlı) bedeli + Ayrılan değer düşüklüğü karşılığı (244/247 vb.)',
            'D': 'Dönem içinde iştirakten tahsil edilen temettü geliri tutarı kadar',
            'E': 'Ayrılan değer düşüklüğü karşılığı (244/247) tutarı kadar, brüt hariç',
        },
        'A',
        'Mali duran varlıklar bilançoda **kayıtlı (maliyet) bedelinden ayrılan değer düşüklüğü karşılığı (244/247 vb.) düşülerek** net değerle gösterilir; karşılık hesapları aktifi düzenleyicidir.',
        "1 Sıra No'lu MSUGT - 24 net gösterim",
    ),
    # düzey 2
    '0026': patch(
        "İşletme, iştiraki olan şirketin dağıttığı kâr payından payına düşen 40.000 ₺'yi banka hesabına tahsil etmiştir. Bu işlemin kaydı aşağıdakilerden hangisidir?",
        {
            'A': '640 İştiraklerden Temettü Gelirleri (borç) 40.000 / 102 Bankalar (alacak) 40.000',
            'B': '102 Bankalar (borç) 40.000 / 640 İştiraklerden Temettü Gelirleri (alacak) 40.000',
            'C': '102 Bankalar (borç) 40.000 / 242 İştirakler (alacak) 40.000',
            'D': '242 İştirakler (borç) 40.000 / 102 Bankalar (alacak) 40.000',
            'E': '102 Bankalar (borç) 40.000 / 600 Yurt İçi Satışlar (alacak) 40.000',
        },
        'B',
        'Banka girişi → **102 Bankalar (borç) 40.000**; iştirakten elde edilen kâr payı bir gelirdir → **640 İştiraklerden Temettü Gelirleri (alacak) 40.000**.',
        "1 Sıra No'lu MSUGT - 640 / 102",
    ),
    # düzey 2
    '0027': patch(
        "'243 İştiraklere Sermaye Taahhütleri (-)' hesabı ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İştirak edilen şirkete verilen ve bir yıl içinde ödenecek avanslar ile borçları izleyen kısa vadeli bir yabancı kaynak (pasif) hesabıdır.',
            'B': 'İştirakten sağlanan kâr paylarını izleyen bir gelir hesabıdır; temettüye hak kazanıldığında alacaklandırılır ve dönem sonunda gelir tablosuna aktarılır.',
            'C': 'İştirak edilen şirketin genel kurulunca dağıtımına karar verilen ve işletmenin payına düşen temettü tutarını dönem boyunca gösteren bir hesaptır.',
            'D': "242 İştirakler'i düzenleyen (aktifi düzenleyici) bir hesaptır; taahhüt edilip henüz ödenmeyen sermaye tutarını gösterir, ödeme yapıldıkça azalır.",
            'E': 'İştirak amacıyla edinilen ve işletmede fiilen kullanılan bina ile makineleri izleyen bir maddi duran varlık hesabıdır; ayrıca amortismana tabi tutulur.',
        },
        'D',
        "**243 İştiraklere Sermaye Taahhütleri (-)**, 242 İştirakler'i düzenleyen (aktifi düzenleyici) bir hesaptır; iştirake taahhüt edilip **henüz ödenmemiş** sermaye kısmını gösterir ve ödeme yapıldıkça kapanır.",
        "1 Sıra No'lu MSUGT - 243",
    ),
    # düzey 2
    '0028': patch(
        "Bir banka, kredi verdiği işletmede yalnızca borçlunun olağan faaliyetini kökten değiştiren işlemleri engelleme hakkına sahiptir. Bu hak kredinin tahsilini korumak için tasarlanmış olup bankaya günlük faaliyetleri yönetme imkânı vermemektedir. TFRS 10'a göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İşletmenin yönetimi veto hakkını kullanmamışsa hak asli hakka dönüşür.',
            'B': 'Her veto hakkı, alacaklının menfaatini korumak için tasarlanmış olsa ve olağan kararları kapsamasa bile ilgili faaliyetleri yönetme gücü verir.',
            'C': 'Banka kredi getirisine maruz kaldığı için işletmeyi mutlaka kontrol eder.',
            'D': 'Hak koruyucu niteliktedir; bu hak tek başına bankaya güç ve kontrol sağlamaz.',
            'E': 'Koruyucu hak, bankayı yatırım işletmesi yapar.',
        },
        'D',
        'İşletmenin faaliyetlerine ilişkin temel değişikliklerde alacaklının menfaatini koruyan, fakat ilgili faaliyetleri yönetme imkânı vermeyen haklar **koruyucu hak** niteliğindedir. Sadece koruyucu haklara sahip olmak TFRS 10 anlamında güç ve kontrol doğurmaz.',
        'TFRS 10, par. 14 ve B26-B28',
    ),
    # düzey 2
    '0029': patch(
        "İşletme, iştirak amacıyla edindiği hisse senetleri için satıcıya 400.000 ₺, aracı kuruma ayrıca 12.000 ₺ komisyon ödemiştir. VUK'a göre hisse senetlerinin değerlemesine esas alış bedeli kaç ₺'dir?",
        {
            'A': '400.000',
            'B': '388.000',
            'C': '412.000',
            'D': '12.000',
            'E': 'Gerçeğe uygun değeri bilinmediği için belirlenemez.',
        },
        'A',
        "VUK'ta alış bedeli, iktisadi kıymetin satın alma bedelidir; iktisapla ilgili diğer giderler alış bedeline dahil değildir. Bu nedenle hisse senetlerinin değerlemesine esas tutar **400.000 ₺**dir; ayrıca ödenen 12.000 ₺ komisyon bu tutara eklenmez.",
        'VUK m. 268/A ve 279',
    ),
    # düzey 2
    '0030': patch(
        "İşletme, bir bağlı ortaklığın 400.000 ₺'lik paylarını satın almayı taahhüt etmiş; bu tutarın 250.000 ₺'sini peşin ödemiş, kalanını sonra ödeyecektir. Kalan ödenmemiş taahhüt tutarı hangi hesapta ve kaç ₺ olarak izlenir?",
        {
            'A': '501 Ödenmemiş Sermaye (-) — 150.000 ₺',
            'B': '331 Ortaklara Borçlar — 400.000 ₺',
            'C': '245 Bağlı Ortaklıklar — 150.000 ₺',
            'D': '247 Bağlı Ortaklıklar Değer Düşüklüğü Karşılığı (-) — 250.000 ₺',
            'E': '246 Bağlı Ortaklıklara Sermaye Taahhütleri (-) — 150.000 ₺',
        },
        'E',
        'Ödenmemiş taahhüt = 400.000 − 250.000 = 150.000 ₺. Bu tutar, bağlı ortaklık payını düzenleyen **246 Bağlı Ortaklıklara Sermaye Taahhütleri (-)** hesabında **150.000 ₺** olarak izlenir; ödendikçe kapanır.',
        "1 Sıra No'lu MSUGT - 246",
    ),
    # düzey 3
    '0031': patch(
        "İşletme %25 pay sahibi olduğu iştirak yatırımını özkaynak yöntemiyle 400.000 ₺'den izlemeye başlamıştır. İştirak 160.000 ₺ dönem kârı açıklamış ve daha sonra toplam 80.000 ₺ temettü dağıtmıştır. Başka değişiklik yoksa yatırımın yeni defter değeri kaç ₺ olur?",
        {
            'A': '400.000',
            'B': '420.000',
            'C': '360.000',
            'D': '340.000',
            'E': '380.000',
        },
        'B',
        'Kârdan pay 160.000 × %25 = **40.000 ₺** ile yatırım artar; temettü payı 80.000 × %25 = **20.000 ₺** ile yatırım azalır. Yeni defter değeri 400.000 + 40.000 − 20.000 = **420.000 ₺**dir.',
        'TMS 28, par. 10',
    ),
    # düzey 2
    '0032': patch(
        "Bir işletme yatırım yapılan şirketin oy haklarının %18'ine sahiptir. İşletmenin yönetim kurulunda daimi temsilcisi bulunmakta ve iki şirket arasında önemli hacimde işlemler yapılmaktadır. TMS 28'e göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Önemli işlemlerin bulunması kontrolün kanıtıdır, önemli etkinin değil.',
            'B': 'Yönetim kurulunda temsil edilme, önemli etki değerlendirmesinde dikkate alınmaz.',
            'C': "%20'nin altındaki oy oranına rağmen mevcut kanıtlar önemli etkinin bulunduğunu gösterebilir.",
            'D': '%18 oy hakkı yatırımcıyı bağlı ortaklık sahibi yapar.',
            'E': "%20'nin altında kalındığı için yönetim kurulunda temsil ve işletmeler arasındaki önemli işlem hacmi gibi kanıtlar dikkate alınmadan önemli etki reddedilir.",
        },
        'C',
        "%20'nin altında oy hakkı bulunması önemli etkinin olmadığına ilişkin aksi ispat edilebilir bir varsayımdır. **Yönetim kurulunda temsil** ve yatırım yapılan işletmeyle **önemli işlemler** bulunması, önemli etkinin varlığını açıkça gösterebilir.",
        'TMS 28, par. 5-6',
    ),
    # düzey 2
    '0033': patch(
        "Özkaynak yöntemiyle izlenen bir iştirak yatırımının defter değerine edinimde ortaya çıkan şerefiye de dâhildir. Değer düşüklüğüne ilişkin tarafsız kanıt bulunduğunda TMS 28'e göre nasıl test yapılır?",
        {
            'A': "Değer düşüklüğü testi ancak oy oranı %50'yi aşarsa yapılır.",
            'B': 'Şerefiye ayrıca ayrıştırılmadan yatırımın net tamamı TMS 36 kapsamında tek bir varlık gibi test edilir.',
            'C': 'İştirakin dağıttığı temettü tutarı test edilir.',
            'D': 'Yatırımın defter değeri azaltılmadan sadece dipnot açıklaması yapılır.',
            'E': 'Şerefiye yatırımdan ayrıştırılarak ayrı bir varlık gibi her yıl amortismana ve ayrıca bağımsız değer düşüklüğü testine tabi tutulur.',
        },
        'B',
        'İştirakle ilgili şerefiye yatırımın defter değerine dâhildir ve ayrı olarak muhasebeleştirilmez. Değer düşüklüğü göstergesi varsa yatırımın **net tamamı**, şerefiye ayrıştırılmadan TMS 36 kapsamında tek bir varlık gibi test edilir.',
        'TMS 28, par. 32 ve 40-42; TMS 36',
    ),
    # düzey 3
    '0034': patch(
        "İşletmenin özkaynak yöntemiyle izlediği iştirak yatırımının defter değeri 100.000 ₺, net yatırımın parçası olan uzun vadeli alacağının defter değeri 30.000 ₺'dir. İştirak zararından işletmeye düşen pay 150.000 ₺ olup işletmenin iştirak adına ödeme yükümlülüğü yoktur. TMS 28'e göre kaç ₺ zarar finansal tablolara yansıtılır?",
        {
            'A': '100.000',
            'B': '20.000',
            'C': '30.000',
            'D': '130.000',
            'E': '150.000',
        },
        'D',
        'Zarar payı önce iştirak yatırımına, sonra net yatırımın parçası olan diğer uzun vadeli haklara uygulanır. Toplam net yatırım **130.000 ₺** olduğundan bu tutara kadar zarar yansıtılır. İşletmenin yasal veya zımni yükümlülüğü bulunmadığı için kalan **20.000 ₺** muhasebeleştirilmez.',
        'TMS 28, par. 38-39',
    ),
    # düzey 2
    '0035': patch(
        "TFRS 10'a göre kontrolün değerlendirilmesiyle ilgili aşağıdaki ifadelerden hangisi doğrudur?",
        {
            'A': 'Yatırım yapılan işletmenin değişken getirilerine maruz kalmak, ilgili faaliyetleri yönetme gücü veya bu gücü getirileri etkilemekte kullanma imkânı bulunmasa da tek başına kontrol için yeterlidir.',
            'B': 'Yatırımın uzun vadeli tutulması kontrolün kesin kanıtıdır.',
            'C': "Kontrol ancak sermaye payı %50'yi aştığında doğabilir.",
            'D': 'En az %20 oy hakkı bulunan bütün yatırımlar bağlı ortaklıktır.',
            'E': 'Güç sözleşmeden de doğabilir; güç, değişken getiriler ve gücü getirileri etkilemekte kullanabilme birlikte aranır.',
        },
        'E',
        'TFRS 10 kontrolü tek bir sahiplik eşiğine indirgemez. Güç oy haklarından veya **sözleşmeye dayalı mevcut haklardan** doğabilir; güç, değişken getiriler ve gücü bu getirileri etkilemek için kullanabilme unsurları birlikte bulunmalıdır.',
        'TFRS 10, par. 6-7 ve 10-11',
    ),
    # düzey 2
    '0036': patch(
        "VUK'un menkul kıymetlerin değerlemesine ilişkin hükmüne göre, iştirak amacıyla elde tutulan hisse senetleri dönem sonunda hangi değerle değerlenir?",
        {
            'A': 'Tasarruf değeriyle',
            'B': 'Borsa rayiciyle',
            'C': 'Alış bedeliyle',
            'D': 'İtfa edilmiş maliyetle',
            'E': 'Nominal değerle',
        },
        'C',
        'VUK 279 uyarınca **hisse senetleri alış bedeliyle** değerlenir. Bu vergi değerleme kuralı, TFRS finansal tablolarında uygulanabilecek ölçüm esaslarıyla karıştırılmamalıdır.',
        'VUK m. 279',
    ),
    # düzey 3
    '0037': patch(
        "Kayıtlı (maliyet) değeri 600.000 ₺ olan bir bağlı ortaklık payı için 90.000 ₺ değer düşüklüğü karşılığı (247) ayrılmıştır. Bilançoda görünecek net değer kaç ₺'dir?",
        {
            'A': '0',
            'B': '600.000',
            'C': '90.000',
            'D': '510.000',
            'E': '690.000',
        },
        'D',
        'Net değer = 600.000 − 90.000 = **510.000 ₺** (245 Bağlı Ortaklıklar − 247 Değer Düşüklüğü Karşılığı).',
        "1 Sıra No'lu MSUGT - 245 / 247",
    ),
    # düzey 3
    '0038': patch(
        'Aşağıdakilerden hangisi mali duran varlıkların ortak özelliklerinden biri değildir?',
        {
            'A': 'İşletmenin bir yıl içinde satmak için elde tuttuğu ticari mallardır.',
            'B': 'Finansal nitelikli varlıklardır (pay/menkul kıymet, ortaklık payı).',
            'C': 'Genellikle amortismana tabi tutulmazlar.',
            'D': 'Değerlerinde kalıcı düşüş olursa karşılık ayrılabilir.',
            'E': 'Uzun vadeli (bir yıldan uzun) amaçlarla elde tutulurlar.',
        },
        'A',
        'Mali duran varlıklar **ticari mal (stok) değildir**; uzun vadeli finansal yatırımlardır. Diğer seçenekler mali duran varlıkların ortak özellikleridir.',
        "1 Sıra No'lu MSUGT - 24 grubu",
    ),
    # düzey 3
    '0039': patch(
        "İşletmenin 250.000 ₺ ile kayıtlı ve %55 oranında pay sahibi olduğu bağlı ortaklığı sermaye artırımına gitmiş, işletme artırıma katılmamıştır. Bunun sonucunda işletmenin payı %35'e düşmüş ve yönetimde önemli etkisi devam etmektedir. Buna göre yapılacak kayıt aşağıdakilerden hangisidir?",
        {
            'A': '242 (borç) 250.000 / 245 (alacak) 250.000',
            'B': '240 (borç) 250.000 / 245 (alacak) 250.000',
            'C': '110 (borç) 250.000 / 245 (alacak) 250.000',
            'D': '654 (borç) 250.000 / 247 (alacak) 250.000',
            'E': '245 (borç) 250.000 / 242 (alacak) 250.000',
        },
        'A',
        "Pay oranı %50'nin altına inip %10-%50 aralığına girdiği için yatırım bağlı ortaklık değil **iştirak** niteliği kazanır; kayıtlı değer 245'ten 242'ye aktarılır. Pay satılmadığından kâr veya zarar doğmaz.",
        'THP 242, 245',
    ),
    # düzey 2
    '0040': patch(
        'Bir işletmenin mali duran varlıkları sınıflandırılmaktadır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "İştiraklerden alınan temettü 640'ta gelir yazılır",
            'B': "Pay oranı %50'yi aşan yatırımlar 245 Bağlı Ortaklıklar'da izlenir",
            'C': "Oy hakkının %10-%50'si iştirak payı olarak 242'de izlenir",
            'D': '244 İştirakler Sermaye Payları Değer Düşüklüğü Karşılığı aktifi düzenler',
            'E': '243 İştiraklere Sermaye Taahhütleri pasifte borç olarak gösterilir',
        },
        'E',
        "243 İştiraklere Sermaye Taahhütleri **aktifi düzenleyici** bir hesaptır; bilançoda 242 İştirakler'den indirilerek gösterilir, pasifte borç olarak yer almaz.",
        'THP 24 Mali Duran Varlıklar',
    ),
    # düzey 2
    '0041': patch(
        "Tekdüzen Hesap Planı'na göre '245 Bağlı Ortaklıklar' hesabında izlenen ortaklık payları için sahiplik (sermaye payı) oranı genel olarak nasıldır?",
        {
            'A': "%50'nin üzerinde (işletmenin kontrol/hâkimiyet sağladığı durumlar)",
            'B': '%10 ile %50 arasında (önemli etkinin sağlandığı iştirak niteliği)',
            'C': 'Sahiplik oranından bağımsızdır; elde tutma süresine göre belirlenir',
            'D': "%10'un altında (kontrol veya önemli etkinin bulunmadığı pay yatırımları)",
            'E': 'Tam olarak %5 (kanunen sabitlenmiş bir asgari sahiplik oranı)',
        },
        'A',
        "**Bağlı ortaklık**; işletmenin sermaye payının **%50'nin üzerinde** olduğu (doğrudan/dolaylı olarak yönetimi ve politikaları kontrol ettiği, hâkimiyet sağladığı) ortaklıkları ifade eder.",
        "1 Sıra No'lu MSUGT - 245 Bağlı Ortaklıklar",
    ),
    # düzey 3
    '0042': patch(
        "İşletme banka hesabından; kısa sürede fiyat farkından yararlanmak amacıyla 120.000 ₺'lik borsa payı ve yönetimine katılmak amacıyla başka bir şirketin oy haklarının %25'ini temsil eden 360.000 ₺'lik pay satın almıştır. Ayrıca alış bedellerinden ayrı 8.000 ₺ aracı kurum komisyonu ödemiştir. VUK esaslı yasal kayıtta doğru kayıt aşağıdakilerden hangisidir?",
        {
            'A': '110 Hisse Senetleri 128.000 ve 242 İştirakler 360.000 borç; 102 Bankalar 488.000 alacak',
            'B': '240 Bağlı Menkul Kıymetler 488.000 borç; 102 Bankalar 488.000 alacak',
            'C': '110 Hisse Senetleri 120.000, 245 Bağlı Ortaklıklar 360.000 ve 653 Komisyon Giderleri 8.000 borç; 102 Bankalar 488.000 alacak',
            'D': '242 İştirakler 488.000 borç; 102 Bankalar 488.000 alacak',
            'E': '110 Hisse Senetleri 120.000, 242 İştirakler 360.000 ve 653 Komisyon Giderleri 8.000 borç; 102 Bankalar 488.000 alacak',
        },
        'E',
        "Kısa vadeli alım **110 Hisse Senetleri**ne, yönetime katılma amacı taşıyan %25'lik uzun vadeli pay **242 İştirakler**e kaydedilir. VUK'ta hisse senetlerinin alış bedeli, satın alma tutarıdır; alışla ilgili diğer giderler bu bedele dahil edilmez. Ayrı ödenen 8.000 ₺ komisyon gider yazılır ve bankadan toplam **488.000 ₺** çıkar.",
        "1 Sıra No'lu MSUGT - 110/242/653; VUK m. 268/A ve 279",
    ),
    # düzey 2
    '0043': patch(
        "İşletme, ödenmiş sermayesi 400.000 ₺ olan bir şirketin paylarının 240.000 ₺'lik kısmını satın alarak yönetim kontrolünü ele geçirmiştir. Bu pay hangi hesapta izlenmelidir?",
        {
            'A': '110 Hisse Senetleri',
            'B': '245 Bağlı Ortaklıklar',
            'C': '248 Diğer Mali Duran Varlıklar',
            'D': '242 İştirakler',
            'E': '240 Bağlı Menkul Kıymetler',
        },
        'B',
        "Sahiplik oranı = 240.000 ÷ 400.000 = **%60**. %50'nin üzerinde olduğundan (kontrol/hâkimiyet) pay **245 Bağlı Ortaklıklar** hesabında izlenir.",
        "1 Sıra No'lu MSUGT - 245 Bağlı Ortaklıklar",
    ),
    # düzey 2
    '0044': patch(
        "TFRS 10'a göre bir yatırımcının yatırım yaptığı işletmeyi kontrol ettiğinin kabul edilmesi için aşağıdaki unsurlardan hangilerinin birlikte bulunması gerekir?",
        {
            'A': 'Uzun vadeli yatırım amacı ve payların borsada işlem görmemesi',
            'B': 'En az %20 oy hakkına ve yönetim kurulunda bir üyeye sahip olma',
            'C': "Sermayenin en az %10'una sahip olma ve önemli ticari işlemler gerçekleştirme",
            'D': 'Güç, değişken getirilere maruz kalma veya hak ve gücü getirileri etkilemekte kullanabilme',
            'E': 'Oy haklarının salt çoğunluğuna sahip olma, yönetim kurulunun çoğunu atama, yatırımı uzun süre elde tutma ve düzenli temettü tahsil etme',
        },
        'D',
        "TFRS 10'da kontrol üç unsurun **birlikte** bulunmasına bağlıdır: yatırım yapılan işletme üzerinde güç, değişken getirilere maruz kalma veya bu getirilerde hak sahibi olma ve mevcut gücü getirileri etkilemek amacıyla kullanabilme. Tek bir sahiplik yüzdesi kontrolün evrensel tanımı değildir.",
        'TFRS 10 Konsolide Finansal Tablolar, par. 6-7',
    ),
    # düzey 2
    '0045': patch(
        "Bir yatırımcı, bir şirketin oy haklarının yalnız %35'ine sahiptir. Ancak yürürlükteki sözleşme yatırımcıya şirketin getirilerini en çok etkileyen üretim ve fiyatlama kararlarını tek başına yönetme hakkı vermektedir. Yatırımcı değişken getirilere maruzdur ve bu hakkını getirileri etkilemek için kullanabilmektedir. TFRS 10'a göre sonuç nedir?",
        {
            'A': "Üç kontrol unsuru birlikte bulunduğundan, oy hakkı %50'nin altında olsa da yatırımcı kontrol sahibidir.",
            'B': 'Sözleşmeden doğan haklar ancak bilanço tarihinde kullanılmışsa kontrol doğar.',
            'C': 'Değişken getirilere maruz kalmak tek başına müşterek kontrol yaratır.',
            'D': "Oy hakkı %50'nin altında olduğundan kontrol kurulamaz.",
            'E': 'Yatırımcı %10 eşiğini geçtiği için iştirak sayılır; sözleşmeden doğan yönetim hakkı ve getirileri etkileme imkânı dikkate alınmaz.',
        },
        'A',
        "Kontrol yalnız sermaye veya oy oranıyla belirlenmez. Sözleşmeden doğan mevcut haklar yatırımcıya ilgili faaliyetleri yönetme **gücü** veriyor, yatırımcı **değişken getirilere** maruz kalıyor ve gücünü bu getirileri etkilemek için kullanabiliyorsa TFRS 10'daki kontrol koşulları sağlanır.",
        'TFRS 10, par. 7 ve 10-11',
    ),
    # düzey 3
    '0046': patch(
        "TMS 28'e göre aşağıdakilerden hangisi tek başına önemli etkinin varlığına ilişkin standartta sayılan göstergelerden biri değildir?",
        {
            'A': 'Yatırım yapılan işletmenin yönetim kurulunda temsil edilme',
            'B': 'İşletmeler arasında yönetici personel değişimi yapılması',
            'C': 'İki işletmenin uzun yıllardır aynı reklam ajansıyla çalışması',
            'D': 'Temettü kararları dâhil politika belirleme süreçlerine katılma',
            'E': 'Yatırımcı ile yatırım yapılan işletme arasında önemli işlemler bulunması',
        },
        'C',
        'TMS 28; yönetim kurulunda temsil, politika süreçlerine katılma, önemli işlemler, yönetici personel değişimi ve gerekli teknik bilgi sağlanmasını önemli etki göstergeleri olarak sayar. **Aynı reklam ajansıyla çalışmak** bu göstergelerden biri değildir.',
        'TMS 28, par. 6',
    ),
    # düzey 2
    '0047': patch(
        'İşletmenin maliyeti 400.000 ₺ olan iştirak payında dönem sonu itibarıyla toplam 30.000 ₺, maliyeti 900.000 ₺ olan bağlı ortaklık payında 50.000 ₺ kalıcı değer düşüklüğü belirlenmiştir. İştirak payı için önceki dönemde 10.000 ₺ karşılık ayrılmıştır; bağlı ortaklık için daha önce karşılık ayrılmamıştır.\n\nDönem sonu karşılık kaydı aşağıdakilerden hangisidir?',
        {
            'A': '654 Karşılık Giderleri 80.000 ₺ borç / 244 30.000 ₺ ve 247 50.000 ₺ alacak',
            'B': '654 Karşılık Giderleri 70.000 ₺ borç / 242 20.000 ₺ ve 245 50.000 ₺ alacak',
            'C': '654 Karşılık Giderleri 70.000 ₺ borç / 244 20.000 ₺ ve 247 50.000 ₺ alacak',
            'D': '654 Karşılık Giderleri 70.000 ₺ borç / 244 70.000 ₺ alacak',
            'E': '244 20.000 ₺ ve 247 50.000 ₺ borç / 654 Karşılık Giderleri 70.000 ₺ alacak',
        },
        'C',
        'İştirak için gereken toplam karşılık 30.000 ₺, mevcut 10.000 ₺; ek karşılık 20.000 ₺ (244 İştirakler Sermaye Payları Değer Düşüklüğü Karşılığı). Bağlı ortaklık için 50.000 ₺ (247). Kayıt: 654 70.000 ₺ borç / 244 20.000 ₺ ve 247 50.000 ₺ alacak.',
        "1 Sıra No'lu MSUGT - 654 / 244",
    ),
    # düzey 2
    '0048': patch(
        "İşletmenin uzun vadeli amaçla edindiği üç yatırım şöyledir: K şirketinde yönetime katılma hakkı bulunmayan %8 pay, L şirketinde yönetime katılma amacı taşıyan %30 pay ve M şirketinde kontrol sağlayan %70 pay. Tekdüzen Hesap Planı'na göre doğru hesap sıralaması hangisidir?",
        {
            'A': '240 Bağlı Menkul Kıymetler - 245 Bağlı Ortaklıklar - 242 İştirakler',
            'B': '110 Hisse Senetleri - 240 Bağlı Menkul Kıymetler - 242 İştirakler',
            'C': '110 Hisse Senetleri - 242 İştirakler - 245 Bağlı Ortaklıklar',
            'D': '240 Bağlı Menkul Kıymetler - 242 İştirakler - 245 Bağlı Ortaklıklar',
            'E': '242 İştirakler - 245 Bağlı Ortaklıklar - 248 Diğer Mali Duran Varlıklar',
        },
        'D',
        "Yönetime katılma hakkı vermeyen %8'lik uzun vadeli pay **240**, yönetime katılma amacı taşıyan %30'luk pay **242**, kontrol sağlayan %70'lik pay ise **245** hesabında izlenir.",
        "1 Sıra No'lu MSUGT - 240/242/245 hesap açıklamaları",
    ),
    # düzey 2
    '0049': patch(
        "Hesap dönemi takvim yılı olan işletme, X A.Ş.'nin sermayesinin %25'ine sahiptir ve payı '242 İştirakler' hesabında maliyetle izlemektedir. X A.Ş.'nin genel kurulu 20 Mart 2026'da 2025 yılı kârından toplam 400.000 ₺ nakit kâr payı dağıtılmasına karar vermiş; ödeme 15 Mayıs 2026'da yapılmıştır.\n\nBuna göre işletmenin bu kâr payını muhasebeleştirmesiyle ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': "20 Mart 2026'da 100.000 ₺ temettü geliri kaydedilir",
            'B': "31 Aralık 2025'te 100.000 ₺ gelir tahakkuk ettirilir",
            'C': "Gelir 15 Mayıs 2026'da tahsil edildiğinde kaydedilir",
            'D': "20 Mart 2026'da 400.000 ₺ temettü geliri kaydedilir",
            'E': "X A.Ş. kârının %25'i 2025 yılında gelir yazılır",
        },
        'A',
        'Kâr payı alacağı, iştirak edilen şirketin genel kurulunun dağıtım kararıyla doğar; gelir bu tarihte ve payı oranında kaydedilir: 400.000 × %25 = 100.000 ₺ (640 İştiraklerden Temettü Gelirleri). Bilanço tarihinde henüz dağıtım kararı olmadığından tahakkuk yapılmaz; tahsil tarihi gelirin doğuşunu belirlemez.',
        "1 Sıra No'lu MSUGT - 640; dönemsellik",
    ),
    # düzey 2
    '0050': patch(
        "'240 Bağlı Menkul Kıymetler' ile '110 Hisse Senetleri' arasındaki temel fark aşağıdakilerden hangisidir?",
        {
            'A': 'İki hesap birbirinin tamamen aynısıdır; aralarında vade veya amaç yönünden bir fark bulunmadığından biri diğerinin yerine kullanılabilir.',
            'B': '240 bir yabancı kaynak (borç) hesabı, 110 ise bir gelir hesabıdır; ikisi de bilançonun aktifinde değil, farklı bölümlerinde raporlanır.',
            'C': '240 hesabı tahvil ve bono türü borçlanma araçları, 110 hesabı ise dağıtılacak kâr payı alacakları için kullanılan hesaplardır.',
            'D': '240 kısa vadeli (bir yıl içinde elden çıkarma), 110 ise uzun vadeli (duran varlık) amaçla tutulan menkul kıymetleri izler; vade ilişkisi terstir.',
            'E': '240 uzun vadeli (duran varlık) amaçla, 110 ise kısa vadeli (bir yıl içinde elden çıkarma) amaçla tutulan menkul kıymetleri izler.',
        },
        'E',
        '**240 Bağlı Menkul Kıymetler** uzun vadeli (duran varlık) amaçla; **110 Hisse Senetleri** ise kısa vadeli (bir yıl içinde elden çıkarma) amaçla tutulan menkul kıymetleri izler. Temel fark **vade/amaç**tır.',
        "1 Sıra No'lu MSUGT - 240 / 110",
    ),
    # düzey 3
    '0051': patch(
        "İşletmenin maliyeti 300.000 ₺ olan iştirak payı için daha önce 40.000 ₺ değer düşüklüğü karşılığı ayrılmıştır. İşletme bu payın yarısını 170.000 ₺'ye satmış ve bedeli banka hesabına almıştır. Satılan paya isabet eden karşılık da satış kaydında kapatılmaktadır. Vergi istisnaları ve satış giderleri ihmal edilecektir.\n\nBuna göre bu satıştan doğan kâr kaç ₺'dir?",
        {
            'A': '20.000',
            'B': '60.000',
            'C': '40.000',
            'D': '170.000',
            'E': '30.000',
        },
        'C',
        'Satılan yarının maliyeti 150.000 ₺, buna isabet eden karşılık 20.000 ₺; net defter değeri 130.000 ₺. Satış kârı = 170.000 − 130.000 = 40.000 ₺. Kayıt: 102 170.000 ₺ ve 244 20.000 ₺ borç / 242 150.000 ₺ ve satış kârı 40.000 ₺ alacak.',
        "1 Sıra No'lu MSUGT - 242 / 244",
    ),
    # düzey 2
    '0052': patch(
        "TFRS 10'a göre bir yatırımcının elinde yalnız yatırım yaptığı işletmedeki payını korumaya yönelik koruyucu hakların bulunması hangi sonucu doğurur?",
        {
            'A': 'Koruyucu haklar tek başına yatırım yapılan işletme üzerinde güç sağlamaz.',
            'B': 'Yatırımcı önemli faaliyetleri yönetmiş sayılır.',
            'C': 'Yatırım doğrudan bağlı ortaklık olarak konsolide edilir.',
            'D': 'Koruyucu haklar müşterek kontrolün kesin kanıtıdır.',
            'E': 'Yatırımcının oy oranı ne olursa olsun kontrol bulunduğu kabul edilir.',
        },
        'A',
        'Koruyucu haklar, sahibinin menfaatini korumak üzere tasarlanır; ilgili faaliyetleri yönetme imkânı vermez. Bu nedenle yalnız koruyucu haklara sahip bir yatırımcı, bu haklar nedeniyle yatırım yapılan işletme üzerinde **güç sahibi olmaz**.',
        'TFRS 10, par. 14 ve B27',
    ),
    # düzey 2
    '0053': patch(
        'TMS 27 kapsamında bireysel finansal tablo hazırlayan bir işletme, bağlı ortaklık yatırımlarını maliyet bedeliyle; iştirak yatırımlarını ise özkaynak yöntemiyle muhasebeleştirmeyi seçmiştir. Bu uygulama için en uygun ifade hangisidir?',
        {
            'A': 'İştirak yatırımlarında özkaynak yöntemi TMS 27 tarafından yasaklanmıştır.',
            'B': 'Maliyet bedeli iş ortaklıklarına özgüdür.',
            'C': 'Bağlı ortaklık, iş ortaklığı ve iştiraklerin tamamında tek bir yöntem uygulanması zorunlu olduğundan kategoriler ayrı ayrı tutarlı olsa bile bu uygulama mümkün değildir.',
            'D': 'Her yatırım kategorisi kendi içinde tutarlı olmak şartıyla farklı kategoriler için farklı esaslar seçilebilir.',
            'E': 'Bağlı ortaklıklar bireysel finansal tablolarda konsolide edilerek gösterilir.',
        },
        'D',
        "TMS 27'de tutarlılık **her bir yatırım kategorisi** bakımından aranır. Bu nedenle bağlı ortaklık kategorisinin tamamında maliyet, iştirak kategorisinin tamamında özkaynak yöntemi uygulanması mümkündür.",
        'TMS 27, par. 10',
    ),
    # düzey 3
    '0054': patch(
        "İşletme özkaynak yöntemiyle izlediği %30'luk iştirak payının bir bölümünü satmış ve kalan %8 pay üzerinde önemli etkisini kaybetmiştir. Kalan pay bağlı ortaklık veya iş ortaklığı niteliğinde değildir. TMS 28'e göre kalan pay için nasıl işlem yapılır?",
        {
            'A': 'Kalan pay sıfır bedelle kayıtlardan çıkarılır.',
            'B': 'Kalan pay nominal değerle 242 İştirakler hesabında tutulur.',
            'C': "Kalan pay gerçeğe uygun değerle ölçülür; ilgili fark TMS 28'de belirtilen esaslarla kâr veya zarara yansıtılır.",
            'D': 'Kalan pay %8 olmasına ve önemli etki sona ermesine rağmen önceki defter değeri üzerinden özkaynak yöntemine devam edilir.',
            'E': 'Önemli etki kaybı ancak pay sıfıra indiğinde muhasebeleştirilir.',
        },
        'C',
        'Yatırım iştirak niteliğini kaybettiğinde özkaynak yöntemi bırakılır. Kalan pay bir finansal varlıksa **gerçeğe uygun değerle** ölçülür; elden çıkarma geliri ile kalan payın gerçeğe uygun değeri toplamının önceki defter değeriyle farkı kâr veya zarara yansıtılır.',
        'TMS 28, par. 22',
    ),
    # düzey 2
    '0055': patch(
        'TMS 27 kapsamında bireysel finansal tablolarda bir iştirak yatırımından alınan temettünün muhasebeleştirilmesi, seçilen yönteme göre nasıl farklılaşır?',
        {
            'A': 'Özkaynak yöntemi seçilmemişse hak doğduğunda kâr veya zarara alınır; özkaynak yönteminde yatırımın defter değerini azaltır.',
            'B': 'Her iki yöntemde de doğrudan diğer kapsamlı gelire alınır.',
            'C': 'Hem maliyet hem özkaynak yönteminde yatırımın defter değerini artırır.',
            'D': 'Maliyet yönteminde yatırımın defter değeri azaltılıp temettü ayrıca diğer kapsamlı gelire alınır; özkaynak yönteminde ise dağıtımın tamamı hasılat yazılır.',
            'E': 'Temettü finansal tablolara yansıtılmaz, dipnotta açıklanır.',
        },
        'A',
        "TMS 27'ye göre temettü alma hakkı doğduğunda, **özkaynak yöntemi seçilmemişse** temettü kâr veya zarara yansıtılır. **Özkaynak yöntemi seçilmişse** dağıtım yatırımın defter değerini azaltır; ayrıca temettü geliri olarak ikinci kez kâr yazılmaz.",
        'TMS 27, par. 12; TMS 28, par. 10',
    ),
    # düzey 2
    '0056': patch(
        "TMS 28'deki önemli etki kavramını en doğru açıklayan ifade hangisidir?",
        {
            'A': 'Yatırım yapılan işletmenin getirilerini önemli ölçüde etkileyen faaliyetlere ilişkin kararların iki veya daha fazla tarafın oy birliğiyle alınmasını gerektiren müşterek kontroldür.',
            'B': 'Yatırım yapılan işletmenin bütün ilgili faaliyetlerini tek başına yönetme gücüdür.',
            'C': 'Sermaye payının %10 ile %50 arasında olmasıdır.',
            'D': 'Yatırım yapılan işletmenin borçlarını ödeme yükümlülüğüdür.',
            'E': 'Finansal ve faaliyet politikası kararlarına katılma gücüdür; tek başına veya müşterek kontrol değildir.',
        },
        'E',
        "Önemli etki, yatırım yapılan işletmenin finansal ve faaliyet politikalarıyla ilgili kararlarına **katılma gücüdür**; bu politikaları tek başına veya bir başka tarafla müştereken kontrol etme gücü değildir. Tekdüzen Hesap Planı'ndaki hesap eşiği, TMS 28 tanımının yerine geçmez.",
        'TMS 28, par. 3',
    ),
    # düzey 2
    '0057': patch(
        "İşletme, bir iştirakine olan 400.000 ₺'lik sermaye taahhüdünün kalan son 120.000 ₺'lik kısmını bankadan ödemiştir. Bu ödeme kaydında hangi hesap borçlandırılır (kapatılır)?",
        {
            'A': '640 İştiraklerden Temettü Gelirleri',
            'B': '243 İştiraklere Sermaye Taahhütleri (-)',
            'C': '102 Bankalar',
            'D': '242 İştirakler',
            'E': '654 Karşılık Giderleri',
        },
        'B',
        'Taahhüt ödemesinde, ödenmemiş taahhüdü gösteren düzenleyici hesap **243 İştiraklere Sermaye Taahhütleri (-) borçlandırılarak kapatılır**; karşılığında 102 Bankalar alacaklandırılır.',
        "1 Sıra No'lu MSUGT - 243 / 102",
    ),
    # düzey 3
    '0058': patch(
        "Mali duran varlık sınıflaması ve finansal raporlama standartlarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Tekdüzen Hesap Planı'nda 242 İştirakler hesabı için en az %10 oy veya yönetime katılma hakkı ölçütü bulunur.\n\nII. TMS 28'de %20 veya daha fazla oy hakkı, aksi açıkça ortaya konulmadıkça önemli etki varsayımı oluşturur.\n\nIII. TFRS 10'da kontrol yalnız oy haklarının %50'yi aşmasıyla kurulabilir.",
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'I ve II',
            'D': 'Yalnız III',
            'E': 'Yalnız II',
        },
        'C',
        "I ve II doğrudur. Tekdüzen Hesap Planı'nın **hesap sınıflama ölçütü** ile TMS 28'in **aksi kanıtlanabilir önemli etki varsayımı** farklıdır. III yanlıştır; TFRS 10'da kontrol güç, değişken getiriler ve gücü getirileri etkilemek için kullanabilme unsurlarına bağlıdır ve sözleşmeye dayalı haklardan da doğabilir.",
        "1 Sıra No'lu MSUGT - 242; TMS 28, par. 5; TFRS 10, par. 6-7",
    ),
    # düzey 3
    '0059': patch(
        "Bir işletmenin dönem sonu mizanında şu kalanlar vardır: 240 Bağlı Menkul Kıymetler 150.000 ₺, 242 İştirakler 500.000 ₺, 243 İştiraklere Sermaye Taahhütleri 200.000 ₺, 244 İştirakler Sermaye Payları Değer Düşüklüğü Karşılığı 50.000 ₺, 245 Bağlı Ortaklıklar 800.000 ₺ ve 110 Hisse Senetleri 90.000 ₺. Buna göre bilançoda gösterilecek mali duran varlıklar toplamı kaç ₺'dir?",
        {
            'A': '1.700.000 ₺',
            'B': '1.200.000 ₺',
            'C': '1.290.000 ₺',
            'D': '1.400.000 ₺',
            'E': '1.250.000 ₺',
        },
        'B',
        '150.000 + 500.000 − 200.000 (243) − 50.000 (244) + 800.000 = **1.200.000 ₺**. 243 ve 244 aktifi düzenleyici hesaplardır; 110 Hisse Senetleri dönen varlıktır.',
        'THP 24 Mali Duran Varlıklar',
    ),
    # düzey 3
    '0060': patch(
        "İşletme %30 pay sahibi olduğu iştirakini özkaynak yöntemiyle 900.000 ₺ ile kayda almıştır. İştirak dönem içinde 400.000 ₺ net kâr elde etmiş, 150.000 ₺ temettü dağıtmış ve 50.000 ₺ diğer kapsamlı gelir muhasebeleştirmiştir. Buna göre dönem sonunda yatırımın defter değeri kaç ₺'dir?",
        {
            'A': '1.005.000 ₺',
            'B': '1.035.000 ₺',
            'C': '1.110.000 ₺',
            'D': '990.000 ₺',
            'E': '1.020.000 ₺',
        },
        'D',
        'Kâr payı +120.000, temettü −45.000, diğer kapsamlı gelir payı +15.000: 900.000 + 120.000 − 45.000 + 15.000 = **990.000 ₺**.',
        'TMS 28 p. 10 (özkaynak yöntemi)',
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
    print(f"1 paket / {len(PATCHES)} soru ('Mali Duran Varliklar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
