#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Finansal Raporlamaya Iliskin Kavramsal Cerceve — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gercek sinav profiliyle yeniden yazim (senaryo kok + kisa terim/tutar sik). Eski surumde siklar ~80 karakterlik aciklamalardi ve 80 mutlak ifadeli celdirici tasiyordu (kor %46). Kapsam: Cerceve'nin statusu ve TMS 8 iliskisi, birincil kullanicilar ve raporlamanin amaci, temel ve destekleyici niteliksel ozellikler, ihtiyatlilik, raporlayan isletme ve sureklilik, varlik/borc/ozkaynak/gelir/gider tanimlari, kontrol ve mukellefiyet, hesap birimi, finansal tablolara alma ve cikarma, olcum esaslari (tarihi maliyet, GUD, kullanim/ifa degeri, cari maliyet), sunum ve aciklama, sermayenin korunmasi. 12 hesap sorusu modulde hesaplandi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Finansal Raporlamaya Iliskin Kavramsal Cerceve (KGK, 2018 surumu); TMS 8 p. 10-12
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/muhasebe_standartlari/kavramsal_cerceve.json"
STYLE_REF = 'SGS Muhasebe Standartlari (gercek sinav profiline kalibre: senaryo kok + kisa sik)'
ONEK = "std-cerceve-gen-"


def patch(stem, options, answer, solution, ref='Finansal Raporlamaya Iliskin Kavramsal Cerceve'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Bir işletmenin muhasebe müdürü, bir standardın belirli bir işlemi Kavramsal Çerçeve'deki varlık tanımından farklı biçimde ele aldığını fark etmiş ve Çerçeve'nin standarda üstün geleceğini savunmuştur. Bu görüş hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Denetçinin tercihi uygulanır',
            'B': 'Çerçeve hükmü uygulanır',
            'C': 'İşletme dilediğini seçer',
            'D': 'İki hükmün ortalaması alınır',
            'E': 'Standart hükmü uygulanır',
        },
        'E',
        "Kavramsal Çerçeve SP1.2'ye göre Çerçeve **bir standart değildir** ve hiçbir standardı veya standarttaki bir hükmü geçersiz kılmaz; çelişki hâlinde **standart** uygulanır.",
        'Kavramsal Çerçeve (2018) SP1.2',
    ),
    # düzey 3
    '0002': patch(
        'Bir yatırımcı, halka açık bir işletmenin genel amaçlı finansal raporlarını incelerken raporlardan işletmenin piyasa değerini doğrudan okuyabilmeyi beklemektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Raporlar kullanıcıların ihtiyaç duyduğu bütün bilgiyi sağlamaz',
            'B': 'Raporlar büyük ölçüde tahmin ve yargılara dayanır',
            'C': 'Kullanıcılar başka kaynaklardaki bilgileri de dikkate alır',
            'D': 'Raporlar işletmenin değerini tahmin etmeye yardımcı bilgi sağlar',
            'E': 'Finansal raporlar işletmenin değerini göstermek için tasarlanır',
        },
        'E',
        "Kavramsal Çerçeve 1.6-1.7'ye göre genel amaçlı finansal raporlar **raporlayan işletmenin değerini göstermek için tasarlanmamıştır**; kullanıcıların değeri tahmin etmesine yardımcı bilgi sağlar. 1.11'e göre raporlar büyük ölçüde tahmin, yargı ve modellere dayanır.",
        'Kavramsal Çerçeve (2018) 1.7',
    ),
    # düzey 2
    '0003': patch(
        'Bir işletmenin yayımladığı yıllık satış hasılatı bilgisi, analistlerin gelecek yıl satışlarını tahmin etmesinde kullanılmakta; aynı bilgi, analistlerin geçen yıl yaptıkları tahminlerin doğru olup olmadığını görmelerini de sağlamaktadır. Bu bilginin ikinci işlevi hangi kavramla ifade edilir?',
        {
            'A': 'Doğrulanabilirlik',
            'B': 'Teyit değeri',
            'C': 'Karşılaştırılabilirlik',
            'D': 'Tahmin değeri',
            'E': 'Zamanında sunum',
        },
        'B',
        "Kavramsal Çerçeve 2.9'a göre finansal bilgi, önceki değerlendirmeler hakkında geri bildirim sağlıyorsa (onları teyit ediyor veya değiştiriyorsa) **teyit değerine** sahiptir; gelecek sonuçların tahmininde kullanılabiliyorsa tahmin değerine sahiptir.",
        'Kavramsal Çerçeve (2018) 2.7-2.10',
    ),
    # düzey 3
    '0004': patch(
        "Bir işletme, sonucu belirsiz davalar için ayırdığı karşılığı, 'ne olur ne olmaz' düşüncesiyle en olası tutarın çok üzerinde belirlemiş ve bunu ihtiyatlılık gereği yaptığını açıklamıştır. Buna göre aşağıdakilerden hangisi söylenemez?",
        {
            'A': 'Borçlar kasıtlı olarak fazla gösterilmez',
            'B': 'İhtiyatlılık tarafsızlığı destekler',
            'C': 'Kasıtlı fazla karşılık ihtiyatlılığın gereğidir',
            'D': 'Bu uygulama tarafsızlıkla bağdaşmaz',
            'E': 'Belirsizlik altında yargıda bulunurken dikkatli olunur',
        },
        'C',
        "Kavramsal Çerçeve 2.16'ya göre ihtiyatlılık, belirsizlik koşullarında yargıda bulunurken dikkatli olmaktır ve tarafsızlığı destekler; ancak **varlık ve gelirlerin eksik, borç ve giderlerin fazla gösterilmesine izin vermez**, çünkü bu tür yanlış gösterimler tarafsız değildir.",
        'Kavramsal Çerçeve (2018) 2.15-2.16',
    ),
    # düzey 3
    '0005': patch(
        "Bir işletme bir ekonomik olgu hakkında en ihtiyaca uygun bilgiyi belirlemiş, ancak bu bilginin gerçeğe uygun sunumu mümkün olmamıştır. Kavramsal Çerçeve'ye göre işletmenin izleyeceği süreçte bir sonraki adım aşağıdakilerden hangisidir?",
        {
            'A': 'Olguyu yalın bir dipnot cümlesiyle geçiştirmek',
            'B': 'Bilgiyi sunmamak',
            'C': 'Tahmini tutarı gizlemek',
            'D': 'Bir sonraki en uygun bilgi türüne bakmak',
            'E': 'Nakit esasına geçmek',
        },
        'D',
        "Kavramsal Çerçeve 2.21'e göre en ihtiyaca uygun bilgi gerçeğe uygun sunulamıyorsa işlem, **bir sonraki en ihtiyaca uygun bilgi türü** için tekrarlanır. Temel niteliksel özelliklerin birlikte sağlanması gerekir.",
        'Kavramsal Çerçeve (2018) 2.21',
    ),
    # düzey 2
    '0006': patch(
        "Bir işletme, çok küçük bir yan faaliyetinin ayrıntılı bölümlere göre raporlanmasının hazırlanma maliyetinin, kullanıcılara sağlayacağı faydadan çok daha yüksek olacağını belirlemiştir. Kavramsal Çerçeve'de faydalı finansal raporlamayı sınırlayan bu unsur hangisidir?",
        {
            'A': 'Maliyet kısıtı',
            'B': 'Önemlilik eşiği',
            'C': 'İhtiyatlılık',
            'D': 'Tarafsızlık',
            'E': 'Zamanında sunum',
        },
        'A',
        "Kavramsal Çerçeve 2.39'a göre **maliyet**, finansal raporlamanın sağlayabileceği bilgi üzerinde yaygın bir kısıttır; bilginin raporlanmasının maliyetleri, faydalarıyla gerekçelendirilmelidir.",
        'Kavramsal Çerçeve (2018) 2.39-2.43',
    ),
    # düzey 3
    '0007': patch(
        'Bir işletme, yıllık finansal tablolarını yasal süre içinde ancak dönem sonundan 11 ay sonra yayımlamaktadır; bu gecikme nedeniyle yatırımcılar kararlarını çoğunlukla diğer kaynaklardan edindikleri bilgiye göre vermektedir. Bu durum en çok hangi destekleyici niteliksel özelliği zayıflatır?',
        {
            'A': 'Zamanında sunum',
            'B': 'Tarafsızlık',
            'C': 'Hatasızlık',
            'D': 'Karşılaştırılabilirlik',
            'E': 'Doğrulanabilirlik',
        },
        'A',
        "Kavramsal Çerçeve 2.33'e göre **zamanında sunum**, bilginin karar alıcıların kararlarını etkileyebilecek zamanda mevcut olmasıdır; genel olarak bilgi eskidikçe faydası azalır.",
        'Kavramsal Çerçeve (2018) 2.33',
    ),
    # düzey 2
    '0008': patch(
        "Bir işletmenin yönetimi, faaliyetlerine son verme niyeti veya zorunluluğu bulunmadığını belirlemiştir. Kavramsal Çerçeve'ye göre finansal tablolar hazırlanırken normalde hangi varsayım yapılır?",
        {
            'A': 'Sabit satın alma gücü',
            'B': 'Tasfiye değeri',
            'C': 'İşletmenin sürekliliği',
            'D': 'Nakit esası',
            'E': 'Dönemsellik dışı sunum',
        },
        'C',
        "Kavramsal Çerçeve 3.9'a göre finansal tablolar normalde raporlayan işletmenin **süreklilik** gösterdiği ve öngörülebilir gelecekte faaliyetlerine devam edeceği varsayımıyla hazırlanır; tasfiye niyeti veya zorunluluğu varsa farklı bir esas kullanılır ve açıklanır.",
        'Kavramsal Çerçeve (2018) 3.9',
    ),
    # düzey 3
    '0009': patch(
        'Bir işletme, yalnızca kendisinin bildiği ve gizli tuttuğu bir üretim tekniği geliştirmiştir. Teknik patentli değildir; ancak işletme bu bilgiyi gizli tutarak başkalarının ondan yararlanmasını engelleyebilmekte ve faydalarını kendisi elde edebilmektedir. Bu durum varlık tanımının hangi unsurunu karşılar?',
        {
            'A': 'Kontrol',
            'B': 'Mevcut mükellefiyet',
            'C': 'Ölçüm güvenilirliği',
            'D': 'Hukuki mülkiyet',
            'E': 'Kesin fayda',
        },
        'A',
        "Kavramsal Çerçeve 4.20-4.22'ye göre **kontrol**, işletmenin bir ekonomik kaynağın kullanımını yönlendirme ve ondan akabilecek ekonomik faydaları elde etme konusundaki **mevcut yeteneğidir**; kontrol hukuki haklardan doğabileceği gibi bilginin gizli tutulması gibi başka yollarla da sağlanabilir.",
        'Kavramsal Çerçeve (2018) 4.19-4.20',
    ),
    # düzey 3
    '0010': patch(
        "Bir işletmenin özkaynağı dönem başında 400.000 ₺, dönem sonunda 520.000 ₺'dir. Dönem içinde ortaklardan 30.000 ₺ sermaye katkısı alınmış, ortaklara 45.000 ₺ kâr payı dağıtılmıştır. Kavramsal Çerçeve'deki gelir ve gider tanımlarına göre dönemin gelirleri ile giderleri arasındaki fark kaç ₺'dir?",
        {
            'A': '45.000',
            'B': '150.000',
            'C': '135.000',
            'D': '90.000',
            'E': '195.000',
        },
        'C',
        "Kavramsal Çerçeve 4.68-4.69'a göre gelir ve gider, özkaynaktaki değişimin **ortakların katkıları ve ortaklara dağıtımlar dışındaki** kısmıdır: 520.000 − 400.000 − 30.000 + 45.000 = **135.000 ₺**.",
        'Kavramsal Çerçeve (2018) 4.68-4.69',
    ),
    # düzey 2
    '0011': patch(
        "Bir işletme, finansal tablo unsurlarını tanımlarken bir alacak sözleşmesindeki hakları tek tek mi yoksa birlikte mi değerlendireceğine karar vermektedir. Kavramsal Çerçeve'de, tanım ve ölçüm kavramlarının uygulandığı hak veya mükellefiyet grubunu ifade eden kavram hangisidir?",
        {
            'A': 'Ölçüm esası',
            'B': 'Hesap birimi',
            'C': 'Nakit yaratan birim',
            'D': 'Raporlama birimi',
            'E': 'Sınıflandırma birimi',
        },
        'B',
        "Kavramsal Çerçeve 4.48'e göre **hesap birimi**, finansal tablolara alma ölçütleri ve ölçüm kavramlarının uygulandığı hak veya hak grubu, mükellefiyet veya mükellefiyet grubu ya da hak ve mükellefiyet grubudur.",
        'Kavramsal Çerçeve (2018) 4.48-4.55',
    ),
    # düzey 2
    '0012': patch(
        "Bir banka, kredi vermeden önce başvuran işletmenin likiditesini ve ödeme gücünü, ek finansman ihtiyacını ve bu finansmanı ne kadar kolay sağlayabileceğini değerlendirmek istemektedir. Kavramsal Çerçeve'ye göre bu değerlendirmede en doğrudan kullanılacak bilgi hangisidir?",
        {
            'A': 'Sektör büyüme raporları',
            'B': 'Rakiplerin fiyat politikaları',
            'C': 'Hisse fiyatlarının geçmişi',
            'D': 'Ekonomik kaynaklar ve talep hakları',
            'E': 'Yönetim kurulu üyelerinin özgeçmiş listesi',
        },
        'D',
        "Kavramsal Çerçeve 1.13'e göre raporlayan işletmenin **ekonomik kaynakları ve ona yönelik talep hakları** hakkındaki bilgi, kullanıcıların işletmenin finansal güçlü ve zayıf yönlerini, **likidite ve ödeme gücünü**, ek finansman ihtiyacını belirlemesine yardımcı olur.",
        'Kavramsal Çerçeve (2018) 1.12-1.13',
    ),
    # düzey 3
    '0013': patch(
        "Bir işletme, ticari alacaklarını bir faktoring şirketine devretmiş; ancak alacaklar tahsil edilemezse faktoring şirketine bütün zararı karşılamayı taahhüt ederek alacaklara ilişkin risklerin önemli kısmını üzerinde tutmuştur. Kavramsal Çerçeve'ye göre finansal tablo dışı bırakmanın amacı aşağıdakilerden hangisiyle ilgilidir?",
        {
            'A': 'Dönemin vergi yükünün mümkün olduğunca azaltılması',
            'B': 'Elde tutulan hak ve mükellefiyetlerin gösterilmesi',
            'C': 'Hasılatın artırılması',
            'D': 'Riskin gizlenmesi',
            'E': 'Nakdin artırılması',
        },
        'B',
        "Kavramsal Çerçeve 5.26'ya göre finansal tablo dışı bırakma, işlemden **sonra elde tutulan varlık ve borçları** ve bu işlemle işletmenin bunlarda meydana gelen değişikliği gerçeğe uygun sunmayı amaçlar; önemli riskler elde tutuluyorsa devir tümüyle tablo dışı bırakma sonucunu doğurmayabilir.",
        'Kavramsal Çerçeve (2018) 5.26-5.28',
    ),
    # düzey 3
    '0014': patch(
        "Bir varlık ölçüm tarihinde piyasa katılımcıları arasındaki olağan bir işlemde 520.000 ₺'ye satılabilecektir; satış için 15.000 ₺ işlem maliyetine katlanılacaktır. Kavramsal Çerçeve'ye göre varlığın gerçeğe uygun değeri kaç ₺'dir?",
        {
            'A': '505.000',
            'B': '520.000',
            'C': '15.000',
            'D': '535.000',
            'E': '490.000',
        },
        'B',
        "Kavramsal Çerçeve 6.12 ve 6.14'e göre gerçeğe uygun değer bir **çıkış fiyatıdır** ve varlığın satışında katlanılacak **işlem maliyetleri düşülmez**: **520.000 ₺**.",
        'Kavramsal Çerçeve (2018) 6.12-6.14',
    ),
    # düzey 3
    '0015': patch(
        "Bir işletmenin elindeki makinenin eşdeğerini ölçüm tarihinde edinmek için ödenecek bedel 700.000 ₺, bu edinmeye ilişkin işlem maliyetleri 30.000 ₺'dir. Makinenin piyasa satış fiyatı 610.000 ₺'dir. Makinenin cari maliyeti kaç ₺'dir?",
        {
            'A': '730.000',
            'B': '700.000',
            'C': '670.000',
            'D': '610.000',
            'E': '580.000',
        },
        'A',
        "Kavramsal Çerçeve 6.21'e göre bir varlığın **cari maliyeti**, ölçüm tarihinde eşdeğer bir varlığın maliyetidir; ödenecek bedel ile o tarihte katlanılacak **işlem maliyetlerini içerir** (giriş değeri): 700.000 + 30.000 = **730.000 ₺**.",
        'Kavramsal Çerçeve (2018) 6.21',
    ),
    # düzey 3
    '0016': patch(
        'Bir işletme, piyasada benzeri olmayan ve ölçüm belirsizliği çok yüksek bir finansal olmayan varlık için ölçüm esası seçmektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Ölçüm belirsizliği seçimi etkileyebilir',
            'B': 'Ölçüm esası seçilirken maliyet kısıtı dikkate alınmaz',
            'C': 'Ölçüm esası ihtiyaca uygun bilgi sağlamalıdır',
            'D': 'Seçimde varlığın gelecekteki nakit akışlarına katkısı önemlidir',
            'E': 'Seçilen esas gerçeğe uygun sunum sağlamalıdır',
        },
        'B',
        "Kavramsal Çerçeve 6.43 ve 6.63'e göre ölçüm esası seçilirken sağlanan bilginin ihtiyaca uygunluğu ve gerçeğe uygun sunumu, varlığın gelecekteki nakit akışlarına nasıl katkıda bulunduğu ve ölçüm belirsizliği dikkate alınır; **maliyet kısıtı** diğer finansal raporlama kararlarında olduğu gibi ölçüm esası seçimini de sınırlar.",
        'Kavramsal Çerçeve (2018) 6.43-6.48',
    ),
    # düzey 2
    '0017': patch(
        "Bir işletme, finansal durum tablosunda binlerce müşterisine ait alacakları tek satırda 'ticari alacaklar' olarak göstermiştir. Kavramsal Çerçeve'de ortak özelliklere sahip varlıkların aynı sınıfa dâhil edilmesi hangi kavramla ifade edilir?",
        {
            'A': 'Netleştirme',
            'B': 'Tablo dışı bırakma',
            'C': 'Yeniden sınıflandırma',
            'D': 'Sınıflandırma',
            'E': 'Ölçüm',
        },
        'D',
        "Kavramsal Çerçeve 7.7'ye göre **sınıflandırma**, varlık, borç, özkaynak, gelir veya giderin sunum ve açıklama amacıyla **ortak özellikler temelinde** gruplanmasıdır; özellikler arasında kalemin niteliği, işletmedeki rolü ve nasıl ölçüldüğü bulunur.",
        'Kavramsal Çerçeve (2018) 7.20',
    ),
    # düzey 3
    '0018': patch(
        "Dönem başı özkaynağı 10.000 ₺ olan bir işletme, bu tutarla aldığı stokun tamamını 15.000 ₺'ye satmıştır. Dönem içinde genel fiyat düzeyi %10 artmıştır; ortaklarla işlem yoktur. Sabit satın alma gücü birimiyle ölçülen finansal sermayenin korunması yaklaşımına göre dönem kârı kaç ₺'dir?",
        {
            'A': '7.000',
            'B': '5.000',
            'C': '4.000',
            'D': '6.000',
            'E': '14.000',
        },
        'C',
        "Kavramsal Çerçeve 8.5'e göre finansal sermaye sabit satın alma gücü birimiyle ölçülürse kâr, dönem boyunca **yatırılan satın alma gücündeki artışı** gösterir: dönem başı sermaye 10.000 × 1,10 = 11.000 ₺; kâr 15.000 − 11.000 = **4.000 ₺**.",
        'Kavramsal Çerçeve (2018) 8.3-8.5',
    ),
    # düzey 2
    '0019': patch(
        'Aşağıdakilerden hangileri destekleyici niteliksel özelliklerdendir?\n\nI. Doğrulanabilirlik\n\nII. Gerçeğe uygun sunum\n\nIII. Zamanında sunum',
        {
            'A': 'Yalnız III',
            'B': 'I ve III',
            'C': 'Yalnız I',
            'D': 'I ve II',
            'E': 'I, II ve III',
        },
        'B',
        "Kavramsal Çerçeve 2.23'e göre doğrulanabilirlik (I) ve zamanında sunum (III) destekleyici niteliksel özelliklerdir. Gerçeğe uygun sunum (II) **temel** niteliksel özelliktir.",
        'Kavramsal Çerçeve (2018) 2.5, 2.23',
    ),
    # düzey 3
    '0020': patch(
        "Aşağıdakilerden hangileri Kavramsal Çerçeve'ye göre doğrudur?\n\nI. Vergi idaresi genel amaçlı finansal raporların birincil kullanıcılarındandır\n\nII. İhtiyatlılık tarafsızlığı destekler\n\nIII. Finansal tablolar normalde işletmenin sürekliliği varsayımıyla hazırlanır",
        {
            'A': 'II ve III',
            'B': 'I, II ve III',
            'C': 'I ve II',
            'D': 'Yalnız II',
            'E': 'Yalnız III',
        },
        'A',
        "Kavramsal Çerçeve 2.16'ya göre ihtiyatlılık tarafsızlığı destekler (II); 3.9'a göre tablolar süreklilik varsayımıyla hazırlanır (III). 1.5 ve 1.10'a göre birincil kullanıcılar yatırımcılar, borç verenler ve diğer alacaklılardır; **vergi idaresi gibi düzenleyiciler birincil kullanıcı değildir** (I yanlış).",
        'Kavramsal Çerçeve (2018) 1.5, 2.16, 3.9',
    ),
    # düzey 2
    '0021': patch(
        "Bir işletme, hiçbir TFRS'nin doğrudan düzenlemediği yeni tür bir işlem için muhasebe politikası belirlemek zorundadır. Benzer konuları düzenleyen bir standart da yoktur. TMS 8'e göre yönetim bu durumda öncelikle aşağıdakilerden hangisindeki tanım ve ölçütleri dikkate alır?",
        {
            'A': 'Kavramsal Çerçeve',
            'B': 'Yönetim kurulu kararı',
            'C': 'Denetim standartları',
            'D': 'Sektör uygulamaları',
            'E': 'Vergi mevzuatı',
        },
        'A',
        "TMS 8 p. 11'e göre yönetim yargıda bulunurken önce benzer konuları düzenleyen TFRS'lere, sonra **Kavramsal Çerçeve'deki varlık, borç, gelir ve gider tanımlarına, finansal tablolara alma ölçütlerine ve ölçüm kavramlarına** başvurur. Sektör uygulamaları ancak bunlarla çelişmedikçe dikkate alınabilir (p. 12).",
        'Kavramsal Çerçeve (2018) SP1.1; TMS 8 p. 10-11',
    ),
    # düzey 3
    '0022': patch(
        'Bir işletmenin 2025 yılında sattığı malların bedelinin önemli bir kısmı 2026 yılında tahsil edilecektir. İşletmenin finansal performansını en iyi yansıtan muhasebe esası hangisidir?',
        {
            'A': 'Nakit esası',
            'B': 'Tahakkuk esası',
            'C': 'Bütçe esası',
            'D': 'Vergi esası',
            'E': 'Tahsil esası',
        },
        'B',
        "Kavramsal Çerçeve 1.17'ye göre **tahakkuk esaslı muhasebe**, işlemlerin etkilerini nakit tahsilat ve ödemeleri farklı dönemlerde olsa bile gerçekleştikleri dönemde gösterir ve performansın değerlendirilmesi için yalnız nakit tahsilat ve ödemelere ilişkin bilgiden daha iyi bir temel sağlar.",
        'Kavramsal Çerçeve (2018) 1.17',
    ),
    # düzey 3
    '0023': patch(
        'Bir işletme, yasal olarak bir leasing şirketine ait olan ve tüm yararlı ömrü boyunca kendisinin kullanacağı bir makineyi, hukuki mülkiyeti bulunmadığı gerekçesiyle finansal tablolarında hiç göstermemiştir. Bu uygulama öncelikle hangi niteliksel özelliğe aykırıdır?',
        {
            'A': 'Doğrulanabilirlik',
            'B': 'Anlaşılabilirlik',
            'C': 'Karşılaştırılabilirlik',
            'D': 'Gerçeğe uygun sunum',
            'E': 'Zamanında sunum',
        },
        'D',
        "Kavramsal Çerçeve 2.12'ye göre gerçeğe uygun sunum, bir ekonomik olgunun **yalnızca hukuki şeklinin değil özünün** sunulmasını gerektirir. Hukuki şekle dayanarak ekonomik özü gizlemek bu temel niteliksel özelliğe aykırıdır.",
        'Kavramsal Çerçeve (2018) 2.12-2.16',
    ),
    # düzey 2
    '0024': patch(
        "Bir sigorta şirketi, ölçüm belirsizliği çok yüksek olan bir tahmin ile ölçüm belirsizliği düşük ancak ekonomik olguyla daha az ilişkili bir tutar arasında seçim yapmaktadır. Kavramsal Çerçeve'ye göre ölçüm belirsizliği hangi temel niteliksel özelliği etkileyen bir faktördür?",
        {
            'A': 'Tutarlılık',
            'B': 'Toplulaştırma',
            'C': 'Anlaşılabilirlik',
            'D': 'Gerçeğe uygun sunum',
            'E': 'Zamanında sunum',
        },
        'D',
        "Kavramsal Çerçeve 2.19'a göre parasal tutarlar doğrudan gözlemlenemeyip tahmin edildiğinde ölçüm belirsizliği doğar ve Çerçeve bunu **gerçeğe uygun sunum** başlığı altında ele alır; tahmin açıkça tanımlanıp açıklandıkça bilginin faydasını zedelemez. 2.22'ye göre belirsizlik çok yüksekse tahminin olguyu yeterince gerçeğe uygun sunup sunmadığı sorgulanır ve daha az ihtiyaca uygun ama belirsizliği düşük bilgiyle arada denge kurulur. Tutarlılık karşılaştırılabilirliğe yardım eder; anlaşılabilirlik ve zamanında sunum destekleyici özelliklerdir, toplulaştırma ise bir sunum kararıdır.",
        'Kavramsal Çerçeve (2018) 2.19',
    ),
    # düzey 3
    '0025': patch(
        'Bağımsız ve bilgili iki gözlemci, bir işletmenin stok sayım sonuçlarını ve birim maliyetlerini ayrı ayrı inceleyerek stok tutarının gerçeğe uygun sunulduğu konusunda tam olarak aynı tutarda olmasa da uzlaşmaya varmıştır. Bu durum hangi destekleyici niteliksel özelliği gösterir?',
        {
            'A': 'Anlaşılabilirlik',
            'B': 'Tarafsızlık',
            'C': 'Doğrulanabilirlik',
            'D': 'Zamanında sunum',
            'E': 'Önemlilik',
        },
        'C',
        "Kavramsal Çerçeve 2.30'a göre doğrulanabilirlik, **birbirinden bağımsız bilgili gözlemcilerin**, belirli bir tasvirin gerçeğe uygun sunum olduğu konusunda **tam olarak olmasa da uzlaşmaya varabilmesidir**; doğrudan (sayım) veya dolaylı (girdi ve hesaplama kontrolü) olabilir.",
        'Kavramsal Çerçeve (2018) 2.30-2.31',
    ),
    # düzey 2
    '0026': patch(
        'Bir öğretim üyesi öğrencilerine niteliksel özellikleri iki gruba ayırmalarını istemiştir. Aşağıdakilerden hangisi temel niteliksel özelliklerden biridir?',
        {
            'A': 'Anlaşılabilirlik',
            'B': 'Doğrulanabilirlik',
            'C': 'Zamanında sunum',
            'D': 'İhtiyaca uygunluk',
            'E': 'Karşılaştırılabilirlik',
        },
        'D',
        "Kavramsal Çerçeve 2.5'e göre temel niteliksel özellikler **ihtiyaca uygunluk ve gerçeğe uygun sunumdur**. 2.23'e göre karşılaştırılabilirlik, doğrulanabilirlik, zamanında sunum ve anlaşılabilirlik destekleyici niteliksel özelliklerdir.",
        'Kavramsal Çerçeve (2018) 2.4, 2.23',
    ),
    # düzey 3
    '0027': patch(
        "Bir işletme, rakip firmanın yakında iflas edeceğini ve pazar payının kendisine geçeceğini düşünerek bu beklentiyi 'gelecekteki pazar payı' adıyla varlık olarak göstermek istemektedir. Beklenti herhangi bir hak veya sözleşmeye dayanmamaktadır. Kavramsal Çerçeve'ye göre bu beklenti hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Maddi olmayan varlıktır',
            'B': 'Varlık tanımını karşılamaz',
            'C': 'Gelir olarak gösterilir',
            'D': 'Koşullu varlıktır',
            'E': 'Şerefiye olarak gösterilir',
        },
        'B',
        "Kavramsal Çerçeve 4.3-4.4'e göre varlık, **geçmiş olayların sonucu olarak işletmenin kontrolündeki mevcut ekonomik kaynaktır**; ekonomik kaynak ekonomik fayda sağlama potansiyeline sahip bir **haktır**. Bir hakka dayanmayan beklenti varlık değildir.",
        'Kavramsal Çerçeve (2018) 4.3-4.4',
    ),
    # düzey 3
    '0028': patch(
        'Bir işletme, çevre mevzuatı zorunlu kılmamasına rağmen yıllardır kamuoyuna yaptığı açıklamalarla, faaliyet gösterdiği bölgede yol açtığı kirliliği temizleyeceğini ilan etmiş ve bunu hep uygulamıştır. Yönetim bu uygulamadan vazgeçmenin pratik olarak mümkün olmadığını düşünmektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Mükellefiyet uygulamadan doğabilir',
            'B': 'İşletmenin kaçınma konusunda pratik yeteneği yoktur',
            'C': 'Hukuki zorunluluk olmadığından mükellefiyet yoktur',
            'D': 'Mükellefiyet başka bir tarafa karşıdır',
            'E': 'Borç tanımının unsurları sağlanabilir',
        },
        'C',
        "Kavramsal Çerçeve 4.29-4.31'e göre mükellefiyet, işletmenin **kaçınma konusunda pratik yeteneğinin olmadığı** bir görev veya sorumluluktur; yalnızca sözleşme veya mevzuattan değil **işletmenin geleneksel uygulamaları, yayımlanmış politikaları veya açıklamalarından** da doğabilir. Mükellefiyet her zaman başka bir tarafa karşıdır.",
        'Kavramsal Çerçeve (2018) 4.29-4.35',
    ),
    # düzey 2
    '0029': patch(
        "Bir işletmenin dönem sonu itibarıyla toplam varlıkları 1.850.000 ₺, toplam borçları 1.130.000 ₺'dir. Kavramsal Çerçeve'ye göre işletmenin özkaynağı kaç ₺'dir?",
        {
            'A': '1.850.000',
            'B': '720.000',
            'C': '410.000',
            'D': '2.980.000',
            'E': '1.130.000',
        },
        'B',
        "Kavramsal Çerçeve 4.63'e göre özkaynak, işletmenin **varlıklarından bütün borçları düşüldükten sonra kalan paydır**: 1.850.000 − 1.130.000 = **720.000 ₺**.",
        'Kavramsal Çerçeve (2018) 4.63',
    ),
    # düzey 2
    '0030': patch(
        "Bir işletme bir tedarikçiyle, gelecek ay belirli bir fiyattan hammadde almak üzere sözleşme yapmıştır. Tarafların hiçbiri henüz kendi yükümlülüğünü yerine getirmemiştir. Kavramsal Çerçeve'de bu tür sözleşmeler nasıl adlandırılır?",
        {
            'A': 'Garanti sözleşmesi',
            'B': 'Koşullu sözleşme',
            'C': 'İfa edilmemiş sözleşme',
            'D': 'Kiralama sözleşmesi',
            'E': 'Türev sözleşme',
        },
        'C',
        "Kavramsal Çerçeve 4.56'ya göre **ifa edilmemiş sözleşme**, taraflardan hiçbirinin yükümlülüklerini yerine getirmediği veya her iki tarafın yükümlülüklerini eşit ölçüde kısmen yerine getirdiği sözleşme ya da sözleşmenin bir kısmıdır; ekonomik kaynağı değiştirme hakkı ve mükellefiyeti birlikte bir varlık veya borç oluşturur.",
        'Kavramsal Çerçeve (2018) 4.56-4.57',
    ),
    # düzey 3
    '0031': patch(
        "Bir işletme, üç yıllık sözleşmeyle kiraladığı binayı sözleşme süresince kullanma hakkına sahiptir; binanın hukuki mülkiyeti kiraya verendedir. Kavramsal Çerçeve'ye göre bu ilişkide işletmenin ekonomik kaynağı aşağıdakilerden hangisidir?",
        {
            'A': 'Binayı kullanma hakkı',
            'B': 'Binanın kendisi',
            'C': 'Kiraya verenin alacağı',
            'D': 'Binanın gelecekteki değeri',
            'E': 'Kira ödeme mükellefiyeti',
        },
        'A',
        "Kavramsal Çerçeve 4.4 ve 4.12'ye göre ekonomik kaynak, ekonomik fayda sağlama potansiyeline sahip bir **haktır**; işletmenin kontrol ettiği şey fiziki nesnenin tamamı değil, sözleşmeden doğan **binayı kullanma hakkıdır**.",
        'Kavramsal Çerçeve (2018) 4.3-4.14',
    ),
    # düzey 3
    '0032': patch(
        "Bir işletme, müşterisine karşı açtığı davadan 300.000 ₺ tazminat almayı ummaktadır; ancak davanın sonucu ve tahsil edilecek tutar son derece belirsizdir. Kavramsal Çerçeve'ye göre bir varlığın finansal tablolara alınıp alınmayacağına karar verilirken esas alınan ölçüt hangisidir?",
        {
            'A': 'Denetçinin onayı',
            'B': 'Tahsilatın kesinleşmesi',
            'C': 'Tutarın güvenilir ölçümü',
            'D': 'İhtiyaca uygun ve gerçeğe uygun bilgi',
            'E': "Ekonomik fayda olasılığının %50'yi aşması",
        },
        'D',
        "Kavramsal Çerçeve 5.7'ye göre bir unsur, finansal tablolara alınması **kullanıcılara ihtiyaca uygun bilgi ve gerçeğe uygun sunum** sağlıyorsa alınır. 2018 Çerçevesi sabit bir olasılık eşiği koymaz; düşük olasılık ve yüksek ölçüm belirsizliği bu ölçütlerin değerlendirilmesinde dikkate alınır (5.12-5.24).",
        'Kavramsal Çerçeve (2018) 5.7, 5.12-5.17',
    ),
    # düzey 2
    '0033': patch(
        "Bir işletme bir makineyi 500.000 ₺'ye satın almış ve edinmeyle doğrudan ilgili 25.000 ₺ işlem maliyeti ödemiştir. Makine tarihî maliyet esasıyla ölçülecektir. Makinenin ilk ölçüm tutarı kaç ₺'dir?",
        {
            'A': '25.000',
            'B': '550.000',
            'C': '500.000',
            'D': '475.000',
            'E': '525.000',
        },
        'E',
        "Kavramsal Çerçeve 6.5'e göre tarihî maliyet, varlığın edinilmesi için katlanılan maliyetlerin değeridir; **ödenen bedel ile işlem maliyetlerini** kapsar: 500.000 + 25.000 = **525.000 ₺**.",
        'Kavramsal Çerçeve (2018) 6.5',
    ),
    # düzey 3
    '0034': patch(
        'Bir işletmenin yükümlülüğünü yerine getirmek için ileride yapacağı nakit ödemelerin bugünkü değerini gösteren işletmeye özgü ölçüm, bir varlığın kullanım değerinin borçlar tarafındaki karşılığıdır. Aşağıdaki durumlardan hangisinde bu ölçüm kullanılmış olur?',
        {
            'A': 'Makinenin satış fiyatıyla ölçülmesi',
            'B': 'Stokun alış bedeliyle ölçülmesi',
            'C': 'Hisse senedinin borsa fiyatıyla ölçülmesi',
            'D': 'Binanın bugün yeniden inşa edilme maliyetiyle ölçülmesi',
            'E': 'Garanti yükümlülüğünün beklenen ödemelerle ölçülmesi',
        },
        'E',
        "Kavramsal Çerçeve 6.17'ye göre borçlar için **ifa değeri**, işletmenin bir borcu yerine getirirken devretmek zorunda olduğu nakit veya diğer ekonomik kaynakların bugünkü değeridir ve **işletmeye özgü** varsayımlara dayanır; garanti yükümlülüğünün işletmenin beklediği ödemelerle ölçülmesi buna örnektir.",
        'Kavramsal Çerçeve (2018) 6.17',
    ),
    # düzey 2
    '0035': patch(
        "Bir öğrenci, Kavramsal Çerçeve'deki ölçüm esaslarını 'geçmiş fiyat' ve 'güncel koşullar' bakımından sınıflandırmaktadır. Aşağıdakilerden hangisi cari değer ölçüm esaslarından biri değildir?",
        {
            'A': 'Kullanım değeri',
            'B': 'Tarihî maliyet',
            'C': 'Cari maliyet',
            'D': 'İfa değeri',
            'E': 'Gerçeğe uygun değer',
        },
        'B',
        "Kavramsal Çerçeve 6.11'e göre cari değer ölçüm esasları **gerçeğe uygun değer, varlıklar için kullanım değeri ve borçlar için ifa değeri ile cari maliyettir**. Tarihî maliyet ayrı bir ölçüm esasıdır.",
        'Kavramsal Çerçeve (2018) 6.10-6.11',
    ),
    # düzey 3
    '0036': patch(
        "Bir analist, bir varlığın ölçümünde 'giriş değeri' ile 'çıkış değeri' kavramlarını karşılaştırmaktadır. Aşağıdakilerden hangisi giriş değeri niteliğinde bir cari değer ölçüm esasıdır?",
        {
            'A': 'Gerçeğe uygun değer',
            'B': 'Kullanım değeri',
            'C': 'Net gerçekleşebilir değer',
            'D': 'Cari maliyet',
            'E': 'İfa değeri',
        },
        'D',
        "Kavramsal Çerçeve 6.21'e göre gerçeğe uygun değer, kullanım değeri ve ifa değerinden farklı olarak **cari maliyet bir giriş değeridir**; ölçüm tarihinde varlığın edinileceği piyasadaki fiyatları yansıtır.",
        'Kavramsal Çerçeve (2018) 6.20-6.21',
    ),
    # düzey 3
    '0037': patch(
        "Bir işletme, aynı bankaya olan kredi borcunu o bankadaki mevduatıyla düşerek finansal durum tablosunda net tutarı göstermiştir; iki kalem farklı hesap birimleridir ve aralarında mahsup hakkı yoktur. Kavramsal Çerçeve'ye göre bu uygulama hangi kavramla adlandırılır?",
        {
            'A': 'Tablo dışı bırakma',
            'B': 'Sınıflandırma',
            'C': 'Netleştirme',
            'D': 'Yeniden ölçüm',
            'E': 'Toplulaştırma',
        },
        'C',
        "Kavramsal Çerçeve 7.10'a göre **netleştirme**, ayrı hesap birimleri olarak finansal tablolara alınan ve ölçülen bir varlık ile bir borcun finansal durum tablosunda tek bir net tutar olarak gösterilmesidir; farklı kalemleri birlikte sınıflandırdığından genellikle uygun değildir.",
        'Kavramsal Çerçeve (2018) 7.10',
    ),
    # düzey 3
    '0038': patch(
        'Bir işletme, dönemin bütün gelir ve giderlerini diğer kapsamlı gelirde gösterip kâr veya zararı yalnız nakit işlemlerle sınırlamak istemektedir. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Gelir ve giderler kural olarak diğer kapsamlı gelirde gösterilir',
            'B': 'Kâr veya zarar performansla ilgili temel bilgi kaynağıdır',
            'C': 'Diğer kapsamlı gelire alma istisnai durumlarda standartlarca yapılır',
            'D': 'Gelir ve giderler ilke olarak kâr veya zarara dâhil edilir',
            'E': "DKG'deki tutarlar ilke olarak sonradan kâr veya zarara aktarılır",
        },
        'A',
        "Kavramsal Çerçeve 7.15-7.19'a göre kâr veya zarar tablosu işletmenin finansal performansı hakkında **temel bilgi kaynağıdır**; ilke olarak bütün gelir ve giderler kâr veya zarara dâhil edilir. Standartlar istisnai durumlarda cari değerdeki değişimlerden doğan bazı gelir ve giderlerin DKG'ye alınmasını öngörebilir ve bunlar ilke olarak sonraki dönemlerde yeniden sınıflandırılır.",
        'Kavramsal Çerçeve (2018) 7.15-7.19',
    ),
    # düzey 3
    '0039': patch(
        "Kavramsal Çerçeve'deki unsur tanımlarına ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Varlık, işletmenin kontrolündeki mevcut ekonomik kaynaktır\n\nII. Borç tanımı için hukuki bir zorunluluk bulunması şarttır\n\nIII. Özkaynak, varlıklar ile borçların toplamıdır",
        {
            'A': 'I, II ve III',
            'B': 'I ve III',
            'C': 'I ve II',
            'D': 'Yalnız III',
            'E': 'Yalnız I',
        },
        'E',
        "Kavramsal Çerçeve 4.3'e göre varlık tanımı (I) doğrudur. 4.31'e göre mükellefiyet geleneksel uygulama veya açıklamalardan da doğabilir; **hukuki zorunluluk şart değildir** (II yanlış). 4.63'e göre özkaynak, varlıklardan **bütün borçlar düşüldükten sonra kalan paydır** (III yanlış).",
        'Kavramsal Çerçeve (2018) 4.3, 4.26, 4.63',
    ),
    # düzey 2
    '0040': patch(
        'Aşağıdakilerden hangileri doğrudur?\n\nI. Teyit değeri, bilginin gelecek sonuçların tahmininde kullanılabilmesidir\n\nII. Doğrulanabilirlik, gözlemcilerin tam olarak aynı tutarda uzlaşmasını gerektirir\n\nIII. Genel olarak bilgi eskidikçe faydası azalır',
        {
            'A': 'I, II ve III',
            'B': 'Yalnız I',
            'C': 'II ve III',
            'D': 'Yalnız III',
            'E': 'I ve II',
        },
        'D',
        "Kavramsal Çerçeve 2.33'e göre bilgi eskidikçe faydası azalır (III). 2.8-2.9'a göre gelecek sonuçların tahmininde kullanılabilme **tahmin değeridir**, teyit değeri önceki değerlendirmelere geri bildirimdir (I yanlış); 2.30'a göre doğrulanabilirlik **tam uzlaşma gerektirmez** (II yanlış).",
        'Kavramsal Çerçeve (2018) 2.9, 2.30, 2.33',
    ),
    # düzey 2
    '0041': patch(
        "Bir işletmenin genel amaçlı finansal raporlarıyla ilgilenen kişiler şunlardır: hissedarlar, işletmeye kredi veren bankalar, tedarikçiler, vergi idaresi ve işletmeyi denetleyen kamu otoritesi. Kavramsal Çerçeve'ye göre aşağıdakilerden hangisi genel amaçlı finansal raporların birincil kullanıcıları arasında yer almaz?",
        {
            'A': 'Vergi idaresi',
            'B': 'Kredi veren bankalar',
            'C': 'Tedarikçiler',
            'D': 'Hissedarlar',
            'E': 'Potansiyel yatırımcılar',
        },
        'A',
        "Kavramsal Çerçeve 1.5'e göre birincil kullanıcılar **mevcut ve potansiyel yatırımcılar, borç verenler ve diğer alacaklılardır**. 1.10'a göre düzenleyici kurumlar ve kamu gibi diğer taraflar raporları faydalı bulabilir, ancak raporlar öncelikle bu gruplara yönelik değildir.",
        'Kavramsal Çerçeve (2018) 1.5',
    ),
    # düzey 2
    '0042': patch(
        "Bir işletmenin yöneticileri, işletmenin ekonomik kaynaklarını ne ölçüde etkin ve verimli kullandıklarını yatırımcılara göstermek istemektedir. Kavramsal Çerçeve'ye göre bu bilgi, genel amaçlı finansal raporlamanın hangi amacına hizmet eder?",
        {
            'A': 'Vergi matrahının belirlenmesi',
            'B': 'İşletme değerinin ölçülmesi',
            'C': 'Kâr dağıtım sınırının saptanması',
            'D': 'Ücret politikasının belirlenmesi',
            'E': 'Yönetimin hesap verebilirliği',
        },
        'E',
        "Kavramsal Çerçeve 1.4 ve 1.22-1.23'e göre kullanıcılar, **yönetimin işletmenin ekonomik kaynaklarını kullanma sorumluluğunu ne ölçüde yerine getirdiğini** değerlendirmek için bilgiye ihtiyaç duyar.",
        'Kavramsal Çerçeve (2018) 1.4, 1.22-1.23',
    ),
    # düzey 3
    '0043': patch(
        "Toplam varlıkları 20 milyon ₺ olan A işletmesinde 150.000 ₺'lik bir hata kullanıcı kararlarını etkilemezken, toplam varlıkları 900.000 ₺ olan B işletmesinde aynı tutardaki hata kararları etkileyebilecektir. Bu durum önemlilik kavramı hakkında neyi gösterir?",
        {
            'A': 'Önemlilik niteliksel belirlenir',
            'B': 'Tek bir sayısal eşik vardır',
            'C': 'Hata tutarı belirleyici değildir',
            'D': 'Önemlilik standartlarca sabitlenir',
            'E': 'Önemlilik işletmeye özgüdür',
        },
        'E',
        "Kavramsal Çerçeve 2.11'e göre önemlilik, bilginin ilişkili olduğu kalemlerin niteliği veya büyüklüğüne ya da her ikisine dayanan, **ihtiyaca uygunluğun işletmeye özgü bir yönüdür**; bu nedenle Çerçeve tek tip bir sayısal eşik belirlemez.",
        'Kavramsal Çerçeve (2018) 2.11',
    ),
    # düzey 3
    '0044': patch(
        "Bir işletmenin yatırım amaçlı gayrimenkullerinin gerçeğe uygun değeri, gözlemlenebilir piyasa verisi olmadığı için yönetimin geliştirdiği bir modelle tahmin edilmiştir; tahmin ve dayandığı varsayımlar açıkça açıklanmıştır. Kavramsal Çerçeve'ye göre bu bilgi hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Hatalı sayılır',
            'B': 'Hatasız sayılabilir',
            'C': 'Sunulamaz',
            'D': 'Dipnotta verilir',
            'E': 'Güvenilir değildir',
        },
        'B',
        "Kavramsal Çerçeve 2.18'e göre hatasız olmak her bakımdan tam doğru olmak değildir; bir tahmin, **tahmin olduğu açıkça belirtilmiş, tahmin sürecinin niteliği ve sınırları açıklanmış ve süreçte hata yapılmamışsa** hatasız sayılabilir.",
        'Kavramsal Çerçeve (2018) 2.18',
    ),
    # düzey 2
    '0045': patch(
        "Bir işletme, stoklarında her yıl aynı maliyet yöntemini uygulayarak finansal tablolarının dönemler arasında benzerlik ve farklılıkların görülebilmesini sağlamaktadır. Kavramsal Çerçeve'ye göre aynı yöntemin tutarlı kullanılması hangi niteliksel özelliğe ulaşmaya yardımcı olur?",
        {
            'A': 'Tahmin değeri',
            'B': 'Tarafsızlık',
            'C': 'Önemlilik',
            'D': 'Karşılaştırılabilirlik',
            'E': 'Doğrulanabilirlik',
        },
        'D',
        "Kavramsal Çerçeve 2.26'ya göre **tutarlılık**, aynı yöntemlerin kullanılmasıdır ve **karşılaştırılabilirliğe ulaşılmasına yardımcı olur**, ancak karşılaştırılabilirlik ile aynı şey değildir; karşılaştırılabilirlik amaç, tutarlılık araçtır.",
        'Kavramsal Çerçeve (2018) 2.24-2.26',
    ),
    # düzey 3
    '0046': patch(
        'Bir işletme, türev işlemleri çok karmaşık olduğu ve kullanıcıların anlamakta zorlanacağı gerekçesiyle bu işlemlere ilişkin bilgileri finansal raporlarına koymamıştır. Buna göre aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Raporlar iş ve ekonomik faaliyetler hakkında makul bilgiye sahip kullanıcılar için hazırlanır',
            'B': 'Karmaşık bilgiler açık ve öz sunulmalıdır',
            'C': 'Karmaşık bilgilerin raporlardan çıkarılması anlaşılabilirliği sağlar',
            'D': 'Kullanıcılar gerektiğinde danışmana başvurabilir',
            'E': 'Bu uygulama raporları eksik bırakır',
        },
        'C',
        "Kavramsal Çerçeve 2.35-2.36'ya göre bazı olgular doğası gereği karmaşıktır; **bunlara ilişkin bilgilerin raporlardan çıkarılması raporları eksik ve yanıltıcı yapar**. Raporlar iş ve ekonomik faaliyetler hakkında makul bilgiye sahip kullanıcılar için hazırlanır; gerekirse danışmandan yardım alınabilir.",
        'Kavramsal Çerçeve (2018) 2.34-2.36',
    ),
    # düzey 2
    '0047': patch(
        "A işletmesi B işletmesini kontrol etmektedir. A ve B ile arasında ana ortaklık-bağlı ortaklık ilişkisi bulunmayan C işletmesinin de aynı raporlama setine dâhil edilmesi istenmektedir. Kavramsal Çerçeve'ye göre aralarında ana ortaklık-bağlı ortaklık ilişkisi bulunmayan işletmelerin finansal tabloları nasıl adlandırılır?",
        {
            'A': 'Birleşik finansal tablolar',
            'B': 'Bireysel finansal tablolar',
            'C': 'Konsolide finansal tablolar',
            'D': 'Özet finansal tablolar',
            'E': 'Ara dönem finansal tablolar',
        },
        'A',
        "Kavramsal Çerçeve 3.12'ye göre raporlayan işletme, aralarında ana ortaklık-bağlı ortaklık ilişkisiyle bağlantı bulunmayan iki veya daha fazla işletmeden oluşuyorsa bu işletmenin finansal tabloları **birleşik finansal tablolar** olarak adlandırılır; ana ortaklık ve bağlı ortaklıklar birlikte konsolide tablo hazırlar.",
        'Kavramsal Çerçeve (2018) 3.10-3.11',
    ),
    # düzey 3
    '0048': patch(
        "Bir işletmenin 2025 yılı finansal tablolarında, 2027'de kurmayı planladığı fabrika için beklenen yatırım tutarı ve bu yatırımdan beklenen kârlar ayrıntılı biçimde yer almaktadır. Plan henüz hiçbir sözleşmeye bağlanmamıştır. Kavramsal Çerçeve'ye göre bu bilgi hakkında aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Varlık olarak gösterilir',
            'B': 'Borç olarak gösterilir',
            'C': 'Karşılık olarak gösterilir',
            'D': 'Gelir olarak gösterilir',
            'E': 'Tablolara dâhil edilmez',
        },
        'E',
        "Kavramsal Çerçeve 3.6'ya göre geleceğe yönelik bilgi, ancak **raporlama dönemindeki veya dönem sonundaki varlık, borç ve özkaynak unsurlarıyla ya da dönemin gelir ve giderleriyle ilgili** ise ve kullanıcılar için ihtiyaca uygunsa dâhil edilir. Yönetimin gelecek planları genellikle finansal tablolarda yer almaz.",
        'Kavramsal Çerçeve (2018) 3.6',
    ),
    # düzey 3
    '0049': patch(
        'Bir işletme gelecek yıl işe alacağı çalışanlara ücret ödemeyi planlamakta ve bunun için bütçe ayırmaktadır. Henüz hiçbir çalışanla sözleşme yapılmamış ve bir hizmet alınmamıştır. Bu plan borç tanımının hangi unsurunu karşılamaz?',
        {
            'A': 'Nakit ödeme',
            'B': 'Ekonomik kaynak devri',
            'C': 'Ölçülebilirlik',
            'D': 'Başka tarafa karşı olma',
            'E': 'Geçmiş olayların sonucu olma',
        },
        'E',
        "Kavramsal Çerçeve 4.43'e göre mevcut mükellefiyet ancak işletme **ekonomik faydalar elde etmiş veya bir işlem yapmış** ve bunun sonucunda devretmek zorunda kalacağı bir durumdaysa geçmiş olayların sonucu olarak var olur. Henüz hizmet alınmadığından mükellefiyet doğmamıştır.",
        'Kavramsal Çerçeve (2018) 4.43-4.47',
    ),
    # düzey 3
    '0050': patch(
        "Bir işletmede dönem içinde varlıklar 260.000 ₺ artmış, borçlar 90.000 ₺ artmıştır. Aynı dönemde ortaklardan 50.000 ₺ nakit sermaye katkısı alınmış ve ortaklara 20.000 ₺ kâr payı ödenmiştir. Dönemin net geliri (gelirler eksi giderler) kaç ₺'dir?",
        {
            'A': '300.000',
            'B': '80.000',
            'C': '140.000',
            'D': '120.000',
            'E': '170.000',
        },
        'C',
        'Özkaynaktaki değişim: 260.000 − 90.000 = 170.000 ₺. Bunun içinden ortakların katkısı çıkarılır, dağıtım geri eklenir: 170.000 − 50.000 + 20.000 = **140.000 ₺**.',
        'Kavramsal Çerçeve (2018) 4.68-4.69',
    ),
    # düzey 2
    '0051': patch(
        "Bir işletmenin dönem içindeki işlemleri şunlardır: satış hasılatı, banka mevduatından faiz geliri, bir tedarikçinin borcun bir kısmını silmesinden doğan kazanç, deposunu kiraya vermesinden kira geliri ve ortakların nakit sermaye koyması. Kavramsal Çerçeve'ye göre bunlardan hangisi gelir değildir?",
        {
            'A': 'Ortakların sermaye koyması',
            'B': 'Faiz geliri',
            'C': 'Tedarikçi borcunun silinmesinden doğan kazanç',
            'D': 'Kira geliri',
            'E': 'Satış hasılatı',
        },
        'A',
        "Kavramsal Çerçeve 4.68'e göre gelir, özkaynakta artışla sonuçlanan varlık artışları veya borç azalışlarıdır; ancak **ortakların katkılarıyla ilgili olanlar gelir değildir**.",
        'Kavramsal Çerçeve (2018) 4.68',
    ),
    # düzey 3
    '0052': patch(
        "Bir işletmenin tedarikçiye 120.000 ₺ borcu vardır. İşletme 90.000 ₺ ödemiş, tedarikçi de kalan tutar için işletmeyi yazılı olarak borçtan kurtarmıştır. Bu işlem sonucunda kâr veya zarara yansıyacak gelir kaç ₺'dir?",
        {
            'A': '210.000',
            'B': '30.000',
            'C': '90.000',
            'D': '120.000',
            'E': '0',
        },
        'B',
        "Kavramsal Çerçeve 5.26'ya göre borç, işletmenin **mevcut mükellefiyeti kalmadığında** tablo dışı bırakılır. 90.000 ₺ ödemeyle, kalan 30.000 ₺ ise borçtan kurtarılmayla kapanır; ödeme yapılmadan azalan borç 4.68 uyarınca **30.000 ₺ gelir** doğurur.",
        'Kavramsal Çerçeve (2018) 5.26, 4.68',
    ),
    # düzey 2
    '0053': patch(
        "Defter değeri 260.000 ₺ olan bir makineyi işletme 300.000 ₺'ye satmış ve makine üzerindeki kontrolünü tümüyle alıcıya devretmiştir. Makine finansal durum tablosundan çıkarıldığında kâr veya zarara yansıyacak kazanç kaç ₺'dir?",
        {
            'A': '0',
            'B': '40.000',
            'C': '300.000',
            'D': '560.000',
            'E': '260.000',
        },
        'B',
        "Kavramsal Çerçeve 5.26'ya göre varlık, işletme **kontrolünü kaybettiğinde** finansal tablo dışı bırakılır; çıkarılan varlık ile alınan bedel arasındaki fark kazanç olarak tanınır: 300.000 − 260.000 = **40.000 ₺**.",
        'Kavramsal Çerçeve (2018) 5.26',
    ),
    # düzey 3
    '0054': patch(
        "Bir makine 800.000 ₺'ye edinilmiştir; bugüne kadar 240.000 ₺ birikmiş amortisman ayrılmış ve 60.000 ₺ değer düşüklüğü zararı tanınmıştır. Makinenin piyasadaki satış fiyatı 650.000 ₺'dir. Tarihî maliyet esasına göre makinenin güncellenmiş defter değeri kaç ₺'dir?",
        {
            'A': '650.000',
            'B': '740.000',
            'C': '800.000',
            'D': '560.000',
            'E': '500.000',
        },
        'E',
        "Kavramsal Çerçeve 6.7'ye göre tarihî maliyet, zamanla **amortisman, itfa ve değer düşüklüğü** gibi unsurları yansıtacak şekilde güncellenir; piyasa fiyatı dikkate alınmaz: 800.000 − 240.000 − 60.000 = **500.000 ₺**.",
        'Kavramsal Çerçeve (2018) 6.7',
    ),
    # düzey 3
    '0055': patch(
        "Bir işletme, sahip olduğu özel amaçlı makineden gelecek üç yılın sonunda sırasıyla 200.000 ₺, 180.000 ₺ ve 150.000 ₺ net nakit girişi beklemektedir; makinenin kalıntı değeri yoktur ve işletmeye özgü iskonto oranı %10'dur. Makinenin kullanım değeri yaklaşık kaç ₺'dir?",
        {
            'A': '443.000',
            'B': '530.000',
            'C': '482.000',
            'D': '488.000',
            'E': '398.000',
        },
        'A',
        'Kullanım değeri beklenen nakit akışlarının bugünkü değeridir: 200.000/1,1 + 180.000/1,21 + 150.000/1,331 ≈ 181.818 + 148.760 + 112.697 ≈ **443.000 ₺**.',
        'Kavramsal Çerçeve (2018) 6.17',
    ),
    # düzey 3
    '0056': patch(
        "Bir varlığın gerçeğe uygun değeri 520.000 ₺, kullanım değeri 585.000 ₺'dir. İki ölçüm arasındaki farkın temel nedeni aşağıdakilerden hangisidir?",
        {
            'A': 'Gerçeğe uygun değerin giriş değeri olması',
            'B': 'Gerçeğe uygun değerin amortisman içermesi',
            'C': 'Kullanım değerinin işletmeye özgü olması',
            'D': 'Kullanım değerinin vergi mevzuatına dayanması',
            'E': 'Kullanım değerinin tarihî maliyete dayanması',
        },
        'C',
        "Kavramsal Çerçeve 6.12 ve 6.17'ye göre gerçeğe uygun değer **piyasa katılımcılarının** bakış açısını, kullanım değeri ise **işletmeye özgü** varsayımları yansıtır; işletmenin varlığı kullanma biçimi piyasa katılımcılarından farklıysa iki değer farklılaşır. Her ikisi de çıkış değeridir.",
        'Kavramsal Çerçeve (2018) 6.12, 6.17',
    ),
    # düzey 3
    '0057': patch(
        "Dönem başı özkaynağı 10.000 ₺ olan ve bu tutarla 100 birim stok almış bir işletme, stokun tamamını dönem içinde 15.000 ₺'ye satmıştır. Dönem sonunda aynı stokun yeniden edinme maliyeti birim başına 120 ₺'ye çıkmış, genel fiyat düzeyi ise %10 artmıştır. Fiziki sermayenin korunması yaklaşımına göre dönem kârı kaç ₺'dir?",
        {
            'A': '5.000',
            'B': '3.000',
            'C': '4.000',
            'D': '13.000',
            'E': '15.000',
        },
        'B',
        "Kavramsal Çerçeve 8.3'e göre fiziki sermayenin korunmasında kâr, işletmenin dönem başındaki **fiziki üretim kapasitesinin** korunmasından sonra kalan tutardır: 15.000 − (100 × 120) = **3.000 ₺**. Nominal finansal sermaye kârı 5.000 ₺, sabit satın alma gücüyle ölçülen finansal sermaye kârı 4.000 ₺ olurdu.",
        'Kavramsal Çerçeve (2018) 8.3-8.7',
    ),
    # düzey 2
    '0058': patch(
        "Bir işletmenin kullanıcıları, öncelikle işletmenin üretim kapasitesinin korunmasıyla ilgilenmektedir. Kavramsal Çerçeve'ye göre bu durumda hangi sermaye kavramı benimsenmelidir?",
        {
            'A': 'Nominal sermaye',
            'B': 'Kayıtlı sermaye',
            'C': 'Ödenmiş sermaye',
            'D': 'Fiziki sermaye',
            'E': 'Finansal sermaye',
        },
        'D',
        "Kavramsal Çerçeve 8.2'ye göre kullanıcılar öncelikle nominal sermayenin veya yatırılan sermayenin satın alma gücünün korunmasıyla ilgileniyorsa finansal sermaye; **işletmenin faaliyet kapasitesiyle** ilgileniyorsa **fiziki sermaye** kavramı benimsenmelidir.",
        'Kavramsal Çerçeve (2018) 8.1',
    ),
    # düzey 2
    '0059': patch(
        'Ölçüm esaslarına ilişkin aşağıdakilerden hangileri doğrudur?\n\nI. Gerçeğe uygun değerden işlem maliyetleri düşülmez\n\nII. Tarihî maliyet amortisman ve değer düşüklüğüyle güncellenir\n\nIII. Cari maliyet bir giriş değeridir',
        {
            'A': 'II ve III',
            'B': 'I ve II',
            'C': 'I, II ve III',
            'D': 'I ve III',
            'E': 'Yalnız I',
        },
        'C',
        "Kavramsal Çerçeve 6.14'e göre gerçeğe uygun değerden işlem maliyetleri düşülmez (I); 6.7'ye göre tarihî maliyet amortisman, itfa ve değer düşüklüğüyle güncellenir (II); 6.21'e göre cari maliyet giriş değeridir (III).",
        'Kavramsal Çerçeve (2018) 6.4-6.7, 6.14, 6.21',
    ),
    # düzey 3
    '0060': patch(
        "Aşağıdakilerden hangileri Kavramsal Çerçeve'ye göre doğrudur?\n\nI. Varlık, işletme kontrolünü kaybettiğinde tablo dışı bırakılır\n\nII. Netleştirme, farklı kalemleri birlikte sınıflandırdığı için genellikle uygun değildir\n\nIII. Fiziki sermaye kavramı nominal para tutarının korunmasına odaklanır",
        {
            'A': 'I ve III',
            'B': 'I, II ve III',
            'C': 'Yalnız II',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'D',
        "Kavramsal Çerçeve 5.26'ya göre kontrol kaybında tablo dışı bırakma (I) ve 7.10'a göre netleştirmenin genellikle uygun olmaması (II) doğrudur. 8.2'ye göre fiziki sermaye **faaliyet kapasitesine** odaklanır; nominal tutar finansal sermaye kavramıdır (III yanlış).",
        'Kavramsal Çerçeve (2018) 5.26, 7.10, 8.2',
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
    print(f"1 paket / {len(PATCHES)} soru ('Finansal Raporlamaya Iliskin Kavramsal Cerceve' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
