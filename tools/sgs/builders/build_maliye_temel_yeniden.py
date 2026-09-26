#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kamu Maliyesi Temel Kavramlar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gercek sinav profiline gore yeniden yazim (2019-2026, 108 gercek maliye sorusu): kisa terim siklari, kucuk olay ve hesap sorulari; mutlak ifade (yalniz/hicbir...) ve sacma celdirici yok. Eski paket: kor ogrenci (genisletilmis olcut) %63.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: Kamu maliyesi teorisi (Musgrave, Samuelson, Coase, Pigou, kamu tercihi, gelir dagilimi olcumu, maliye dusunce okullari)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/maliye/kamu_maliyesi_temel.json"
STYLE_REF = 'SGS Maliye (gercek sinav profiline kalibre: kisa sik + olay/hesap)'
ONEK = "mal-temel-gen-"


def patch(stem, options, answer, solution, ref='Kamu maliyesi teorisi'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 1
    '0001': patch(
        "Musgrave'in devletin ekonomik fonksiyonlarına ilişkin üçlü sınıflandırmasında, piyasanın yeterince üretmediği kamusal malların sunulması hangi fonksiyonun kapsamındadır?",
        {
            'A': 'Ekonomik istikrar',
            'B': 'Kaynak tahsisi',
            'C': 'Gelir bölüşümü',
            'D': 'Ekonomik kalkınma',
            'E': 'Düzenleme ve denetim',
        },
        'B',
        'Musgrave devletin ekonomik fonksiyonlarını **kaynak tahsisi**, **gelir bölüşümü** ve **ekonomik istikrar** olarak üçe ayırır. Piyasanın yetersiz sunduğu kamusal ve yarı kamusal malların sağlanması kaynakların kamu ile özel kesim arasında yeniden dağıtılması, yani kaynak tahsisi fonksiyonudur. Kalkınma ve düzenleme bu üçlü sınıflandırmada ayrı birer fonksiyon değildir.',
        "Kamu maliyesi teorisi: Musgrave'in fonksiyonlar ayrımı",
    ),
    # düzey 2
    '0002': patch(
        'Tüketiminde rakiplik bulunan ancak kullanıcıların dışlanması güç olan mallara aşağıdakilerden hangisi örnek gösterilebilir?',
        {
            'A': 'Açık denizlerdeki balık stoku',
            'B': 'Tıkanıklık olmayan ücretli otoyol',
            'C': 'Deniz feneri hizmeti',
            'D': 'Şifreli uydu yayını',
            'E': 'Fırından alınan ekmek',
        },
        'A',
        "Rakip olup dışlanamayan mallar **ortak mülkiyet kaynaklarıdır**. Açık denizdeki balığı bir kişinin avlaması diğerlerine kalan stoku azaltır (rakiplik), ama kimsenin avlanması kolayca engellenemez; bu yapı 'ortak kaynakların trajedisine' yol açar. Şifreli yayın ve tıkanıklık olmayan ücretli otoyol kulüp malı, deniz feneri tam kamusal mal, ekmek özel maldır.",
        'Kamu maliyesi teorisi: mal türleri',
    ),
    # düzey 0
    '0003': patch(
        'Kamusal malın finansmanında her bireyin maldan sağladığı marjinal fayda oranında pay (vergi-fiyat) ödediği gönüllü mübadele yaklaşımı aşağıdakilerden hangisidir?',
        {
            'A': 'Ramsey fiyatlandırması',
            'B': 'Pigou vergisi',
            'C': 'Lindahl fiyatlandırması',
            'D': 'Marjinal maliyet fiyatlandırması',
            'E': 'Tepe yük fiyatlandırması',
        },
        'C',
        '**Lindahl** modelinde her birey, kamusal maldan sağladığı marjinal fayda ölçüsünde kişiye özel bir vergi-fiyat öder; bu payların toplamı maliyeti karşılar. Ramsey fiyatlandırması talep esnekliğiyle ters orantılı fiyatlamadır; Pigou vergisi dışsallığı düzeltir.',
        'Kamu maliyesi teorisi: Lindahl modeli',
    ),
    # düzey 2
    '0004': patch(
        'Aşağıdakilerden hangisi tam kamusal malların özelliklerinden biri değildir?',
        {
            'A': 'Tüketimde rakibin bulunmaması',
            'B': 'Ek tüketicinin marjinal maliyetinin sıfır olması',
            'C': 'Bireysel talep eğrilerinin dikey toplanması',
            'D': 'Bireylerin maldan farklı miktarlarda yararlanabilmesi',
            'E': 'Bedelini ödemeyenin dışlanamaması',
        },
        'D',
        'Tam kamusal mal herkes tarafından **aynı miktarda** tüketilir; milli savunmadan her vatandaş aynı ölçüde yararlanır. Bu nedenle talepler miktar yönünde değil, fiyat (marjinal fayda) yönünde, yani dikey toplanır. Rakipsizlik, dışlanamama ve ek tüketicinin sıfır marjinal maliyeti tam kamusal malın tanımlayıcı özellikleridir.',
        'Kamu maliyesi teorisi: tam kamusal malın özellikleri',
    ),
    # düzey 3
    '0005': patch(
        'Bir nehrin yukarısındaki fabrika ile aşağısındaki balıkçılar arasındaki kirlilik sorununda işlem maliyetlerinin sıfır olduğu varsayılmaktadır. Coase teoremine göre kirletme hakkının fabrikaya ya da balıkçılara verilmesinin sonuçlarına ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Hak fabrikaya verilirse pazarlık sonucunda kirlilik sıfıra iner',
            'B': 'Hak balıkçılara verilirse pazarlık sonucunda fabrika üretimini durdurur',
            'C': 'Etkin kirlilik düzeyine ancak Pigou vergisiyle ulaşılabilir',
            'D': 'Gelir dağılımı değişmez; kirlilik düzeyi hakkın sahibine göre değişir',
            'E': 'Kirlilik düzeyi aynı olur; hakkın sahibi gelir dağılımını belirler',
        },
        'E',
        "Coase'a göre işlem maliyeti yoksa hak kime verilirse verilsin taraflar marjinal fayda ve maliyetleri eşitleyen **aynı etkin kirlilik düzeyine** ulaşır. Değişen, pazarlıkta kimin kime ödeme yaptığı, yani **gelir dağılımıdır**: hak fabrikadaysa balıkçılar fabrikaya azaltım için ödeme yapar, hak balıkçılardaysa fabrika kirletme izni için balıkçılara öder.",
        'Kamu maliyesi teorisi: Coase teoremi',
    ),
    # düzey 2
    '0006': patch(
        'Bir bireyin aşı olması, başkalarının hastalanma riskini de azaltmaktadır. Aşı kararlarının yalnız piyasaya bırakılmasının sonucuna ilişkin aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Aşı tüketimi toplumsal optimumun altında kalır; sübvansiyon gerekçelendirilebilir',
            'B': 'Dışsallık, aşının fiyatına yansıdığı için etkinlik kaybı doğmaz',
            'C': 'Piyasa dengesi toplumsal optimuma eşit olur; müdahale gerekmez',
            'D': 'Aşı tüketimi toplumsal optimumun üstüne çıkar; vergi gerekçelendirilebilir',
            'E': 'Özel marjinal fayda toplumsal marjinal faydayı aşar',
        },
        'A',
        'Pozitif dışsallıkta toplumsal marjinal fayda, bireyin kendi marjinal faydasından (özel marjinal fayda) büyüktür. Birey yalnız kendi faydasını dikkate aldığından piyasa tüketimi toplumsal optimumun **altında** kalır; aradaki fark kadar Pigou sübvansiyonu tüketimi optimuma yaklaştırır.',
        'Kamu maliyesi teorisi: pozitif dışsallık',
    ),
    # düzey 2
    '0007': patch(
        'Bir arıcının arıları komşu elma bahçesinin tozlaşmasına, elma bahçesi de balın verimine katkı sağlamaktadır. İki işletmenin tek bir sahip altında birleştirilmesiyle karşılıklı dışsallıkların hesaba katılması hangi çözüm yoludur?',
        {
            'A': 'Kamu mülkiyetine geçirme',
            'B': 'Emisyon standardı getirilmesi',
            'C': 'Karşılıklı Pigou sübvansiyonları',
            'D': 'Birleşme yoluyla içselleştirme',
            'E': 'Lindahl fiyatlaması',
        },
        'D',
        "Dışsallık yaratan ve dışsallıktan etkilenen birimler tek karar biriminde birleştiğinde dışsal etki iç maliyet ya da fayda hâline gelir ve karar alıcı bunu hesaba katar. Buna **birleşme yoluyla içselleştirme** denir (Meade'in arıcı-elma bahçesi örneği).",
        'Kamu maliyesi teorisi: dışsallıkların içselleştirilmesi',
    ),
    # düzey 2
    '0008': patch(
        'Tam kasko sigortası yaptıran bir sürücünün, olası hasarın sigortacı tarafından karşılanacağını bildiği için aracını daha az özenle kullanması hangi kavramla açıklanır?',
        {
            'A': 'Mali yanılsama',
            'B': 'Ahlaki tehlike',
            'C': 'Bedavacılık',
            'D': 'Ters seçim',
            'E': 'Sinyal verme',
        },
        'B',
        'Sözleşme yapıldıktan sonra, davranışı karşı tarafça gözlemlenemeyen tarafın riskli davranışı artırmasına **ahlaki tehlike** denir. Ters seçim sözleşme öncesi gizli bilgiden, sinyal verme ise bilgili tarafın bilgisini karşı tarafa aktarma çabasından kaynaklanır.',
        'Kamu maliyesi teorisi: asimetrik bilgi',
    ),
    # düzey 1
    '0009': patch(
        'Birden çok hizmet sunan ve zarar eden bir kamu tekelinde, zararı kapatmak için fiyatları marjinal maliyetin üzerine hizmetlerin talep esnekliğiyle ters orantılı olarak artıran fiyatlandırma kuralı hangisidir?',
        {
            'A': 'Ramsey fiyatlandırması',
            'B': 'Tepe yük fiyatlandırması',
            'C': 'Marjinal maliyet fiyatlandırması',
            'D': 'İki parçalı tarife',
            'E': 'Lindahl fiyatlandırması',
        },
        'A',
        '**Ramsey** kuralında fiyatın marjinal maliyetten sapma oranı talep esnekliğiyle ters orantılıdır: talebi esnek olmayan hizmete daha yüksek pay yüklenir, böylece gelir ihtiyacı en az refah kaybıyla karşılanır. Tepe yük fiyatlaması ise talebin zamana göre dalgalandığı hizmetlerde yoğun dönem fiyatını yükseltir.',
        'Kamu maliyesi teorisi: doğal tekel fiyatlaması',
    ),
    # düzey 2
    '0010': patch(
        'Üç seçmenin üç seçeneğe ilişkin tercihleri A>B>C, B>C>A ve C>A>B biçimindedir. İkili çoğunluk oylamasında ortaya çıkan durum aşağıdakilerden hangisidir?',
        {
            'A': 'Rasyonel cehalet',
            'B': 'Lindahl dengesi',
            'C': 'Oylama paradoksu',
            'D': 'Oy ticareti',
            'E': 'Medyan seçmen dengesi',
        },
        'C',
        "A, B'yi (1. ve 3. seçmen); B, C'yi (1. ve 2. seçmen); C ise A'yı (2. ve 3. seçmen) 2-1 yener. Toplumsal tercih geçişsiz olduğundan kalıcı bir kazanan yoktur; sonucu oylama sırası belirler. Bu **Condorcet'nin oylama paradoksudur**; tercihlerden biri tek tepeli olmadığı için medyan seçmen dengesi oluşmaz.",
        'Kamu maliyesi teorisi: oylama paradoksu',
    ),
    # düzey 1
    '0011': patch(
        'Mükelleflerin dolaylı vergiler ve borçlanmayla finanse edilen kamu hizmetlerinin maliyetini olduğundan düşük algılaması sonucunda kamu harcamalarının artmasını açıklayan kavram hangisidir?',
        {
            'A': 'Vergi gayreti',
            'B': 'Rasyonel beklentiler',
            'C': 'Mali rant',
            'D': 'Ricardo denkliği',
            'E': 'Mali yanılsama',
        },
        'E',
        "**Puviani'nin mali yanılsama** kavramına göre vergi yükü dolaylı vergiler, stopaj ve borçlanmayla daha az hissedilir kılındığında mükellefler kamu hizmetlerinin maliyetini düşük algılar ve daha fazla harcamayı destekler. Ricardo denkliği ise tersine, mükelleflerin borçlanmanın gelecekteki vergi yükünü tam öngördüğünü varsayar.",
        'Kamu maliyesi teorisi: mali yanılsama',
    ),
    # düzey 2
    '0012': patch(
        'Aşağıdaki kavram–açıklama eşleştirmelerinden hangisi yanlıştır?',
        {
            'A': 'Rasyonel cehalet – Bilgi edinme maliyetinden kaçınılması',
            'B': 'Leviathan modeli – Bürokratın yönettiği bütçeyi maksimize etmesi',
            'C': 'Medyan seçmen – Çoğunluk oylamasında belirleyici tercih',
            'D': 'Oy ticareti – Karşılıklı destek anlaşmasıyla önerge geçirilmesi',
            'E': 'Rant kollama – Siyasi rant elde etmek için kaynak harcanması',
        },
        'B',
        'Bürokratın bütçeyi maksimize etmesi **Niskanen** modelidir. Leviathan modeli (Brennan-Buchanan) devletin bütün olarak vergi gelirini maksimize eden bir tekel gibi davrandığını ileri sürer. Diğer eşleştirmeler kavramların doğru açıklamalarıdır.',
        'Kamu maliyesi teorisi: kamu tercihi kavramları',
    ),
    # düzey 2
    '0013': patch(
        "Bir ülkede Lorenz eğrisi ile tam eşitlik doğrusu arasında kalan alan 0,15'tir. Birim karelik Lorenz diyagramında bu ülkenin Gini katsayısı kaçtır?",
        {
            'A': '0,30',
            'B': '0,35',
            'C': '0,15',
            'D': '0,70',
            'E': '0,85',
        },
        'A',
        'Gini katsayısı, Lorenz eğrisi ile tam eşitlik doğrusu arasındaki alanın, tam eşitlik doğrusunun altındaki toplam üçgen alana (birim karede 0,5) oranıdır: 0,15 / 0,5 = **0,30**. 0,15 bu alanın kendisidir, bölmenin yapılmadığı hatalı sonuçtur.',
        'Kamu maliyesi teorisi: Gini katsayısı',
    ),
    # düzey 1
    '0014': patch(
        'Geliri 90 bin ₺ olan bir kişiden geliri 30 bin ₺ olan kişiye, sıralamalarını değiştirmeyecek biçimde 10 bin ₺ aktarılması hâlinde iyi bir eşitsizlik ölçüsünün değerinin düşmesi gerektiğini ifade eden ilke hangisidir?',
        {
            'A': 'Pareto ilkesi',
            'B': 'Kuznets hipotezi',
            'C': 'Lorenz baskınlığı',
            'D': 'Pigou-Dalton transfer ilkesi',
            'E': "Rawls'un maksimin (farklılık) ilkesi",
        },
        'D',
        '**Pigou-Dalton transfer ilkesi**, zenginden yoksula sıralamayı değiştirmeyen bir aktarımın eşitsizliği azalttığını kabul eden ölçütün sağlaması gereken temel koşuldur. Gini ve Atkinson endeksleri bu ilkeyi sağlar. Aktarım zengini kötüleştirdiği için Pareto iyileştirmesi değildir.',
        'Kamu maliyesi teorisi: Pigou-Dalton ilkesi',
    ),
    # düzey 0
    '0015': patch(
        'Kalkınmanın ilk aşamalarında gelir eşitsizliğinin arttığını, ileri aşamalarda azaldığını ileri süren ve kişi başı gelir ile eşitsizlik arasında ters U biçimli ilişki öngören yaklaşım hangisidir?',
        {
            'A': 'Artan devlet faaliyetleri kanunu',
            'B': 'Lorenz eğrisi',
            'C': 'Kuznets hipotezi',
            'D': 'Laffer eğrisi',
            'E': 'Engel kanunu',
        },
        'C',
        '**Kuznets hipotezi** gelir eşitsizliği ile kalkınma arasında ters U ilişkisi öngörür. Laffer eğrisi de ters U biçimlidir ancak vergi oranı ile vergi hasılatı arasındaki ilişkiyi gösterir; Wagner kanunu kamu harcamalarının gelirle birlikte artışını açıklar.',
        'Kamu maliyesi teorisi: Kuznets hipotezi',
    ),
    # düzey 0
    '0016': patch(
        "Yoksulluk sınırının ülkedeki medyan gelirin belirli bir oranı (örneğin %60'ı) olarak belirlendiği yaklaşım aşağıdakilerden hangisidir?",
        {
            'A': 'Göreli yoksulluk',
            'B': 'Gıda yoksulluğu',
            'C': 'Kronik yoksulluk',
            'D': 'Mutlak yoksulluk',
            'E': 'Öznel yoksulluk',
        },
        'A',
        "**Göreli yoksulluk**, kişinin gelirini toplumun genel gelir düzeyiyle (çoğunlukla medyan gelirin %50 veya %60'ı) karşılaştırır. Mutlak yoksulluk ise temel ihtiyaçları karşılayacak sabit bir tüketim sepetinin maliyetine dayanır.",
        'Kamu maliyesi teorisi: yoksulluk ölçümü',
    ),
    # düzey 2
    '0017': patch(
        'Klasik maliye anlayışına ilişkin aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Vergilerin ekonomik kararları etkilememesini öngörür',
            'B': 'Devletin görevlerini adalet, güvenlik ve savunmada toplar',
            'C': 'Durgunlukta bütçe açığının bilinçli olarak artırılmasını savunur',
            'D': 'Say yasasına dayanarak kalıcı talep yetersizliği beklemez',
            'E': 'Bütçenin denk olmasını mali disiplinin temeli sayar',
        },
        'C',
        'Klasik anlayış tarafsız ve sınırlı devleti, denk bütçeyi ve ekonomik kararları bozmayan (tarafsız) vergileri savunur; Say yasası gereği arzın kendi talebini yaratacağını, kalıcı talep yetersizliği olmayacağını kabul eder. Durgunlukta bilinçli bütçe açığı ise **Keynesyen** (fonksiyonel maliye) anlayışın önerisidir.',
        'Kamu maliyesi teorisi: klasik maliye anlayışı',
    ),
    # düzey 3
    '0018': patch(
        'Hükümet, harcamalarını değiştirmeden bu yıl vergileri indirmekte ve oluşan açığı borçlanmayla finanse etmektedir. Ricardo denkliği geçerliyse hanehalklarının tepkisi aşağıdakilerden hangisi olur?',
        {
            'A': 'Artan faizler nedeniyle yatırımların bir kısmı dışlanır',
            'B': 'Gelecekteki vergi artışını öngörüp tasarrufu artırır, toplam talep değişmez',
            'C': 'Borçlanma para arzını artırdığından enflasyon yükselir',
            'D': 'Tasarrufunu azaltıp servetini tüketime yöneltir',
            'E': 'Tüketimi vergi indirimi kadar artırır, toplam talep genişler',
        },
        'B',
        '**Ricardo denkliğine** (Barro) göre rasyonel ve ileriye bakan hanehalkları, bugünkü borcun gelecekte vergiyle ödeneceğini bilir; vergi indirimini harcamak yerine gelecekteki vergi yükünü karşılamak için **tasarruf** eder. Özel tasarruf artışı kamu tasarrufundaki düşüşü dengeler; faiz ve toplam talep değişmez. Dışlama etkisi Keynesyen IS-LM çerçevesinin sonucudur.',
        'Kamu maliyesi teorisi: Ricardo denkliği',
    ),
    # düzey 1
    '0019': patch(
        'Bir değişiklik sonucunda kimsenin durumu kötüleşmeden en az bir kişinin durumu iyileşiyorsa bu değişiklik aşağıdakilerden hangisiyle ifade edilir?',
        {
            'A': 'Kaldor-Hicks iyileştirmesi',
            'B': 'Rawlsçı iyileştirme',
            'C': 'Nash dengesi',
            'D': 'Pareto optimumu',
            'E': 'Pareto iyileştirmesi',
        },
        'E',
        'Kimseyi kötüleştirmeden en az bir kişiyi iyileştiren değişiklik **Pareto iyileştirmesidir**. Pareto optimumu ise artık böyle bir iyileştirmenin mümkün olmadığı durumdur. Kaldor-Hicks ölçütü, kazananların kaybedenleri potansiyel olarak tazmin edebilmesini yeterli sayar.',
        'Kamu maliyesi teorisi: Pareto ölçütü',
    ),
    # düzey 0
    '0020': patch(
        'Faydası belirli bir bölgeyle sınırlı kamusal malların merkezi yönetim yerine o bölgenin yerel yönetimi tarafından sunulmasının daha etkin olacağını ileri süren yaklaşım hangisidir?',
        {
            'A': "Oates'in ademi merkeziyet teoremi",
            'B': 'Samuelson koşulu',
            'C': 'Coase teoremi',
            'D': 'Wagner kanunu',
            'E': "Musgrave'in mali fonksiyonlar ayrımı",
        },
        'A',
        "**Oates'in ademi merkeziyet teoremine** göre faydası bölgesel olan kamusal mallarda, yerel tercihlere göre farklılaştırılmış sunum, merkezden tek tip sunuma göre toplumsal refahı daha fazla artırır. Samuelson koşulu kamusal malın etkin miktarını, Coase teoremi dışsallıkların pazarlıkla çözümünü açıklar.",
        'Kamu maliyesi teorisi: mali federalizm',
    ),
    # düzey 2
    '0021': patch(
        'Aşağıdaki kamu uygulaması–Musgrave fonksiyonu eşleştirmelerinden hangisi yanlıştır?',
        {
            'A': 'Aşılama kampanyasının kamuca finanse edilmesi – Kaynak tahsisi',
            'B': 'Aşırı talep döneminde bütçe fazlası verilmesi – İstikrar',
            'C': 'Milli savunma hizmetinin sunulması – Kaynak tahsisi',
            'D': 'Negatif gelir vergisi uygulanması – Gelir bölüşümü',
            'E': 'Durgunlukta kamu yatırımlarının artırılması – Gelir bölüşümü',
        },
        'E',
        'Durgunlukta toplam talebi desteklemek için kamu yatırımlarının artırılması **istikrar** fonksiyonuna girer; gelir bölüşümü fonksiyonu vergi ve transferlerle kişisel gelir dağılımının düzeltilmesidir. Savunma ve dışsallık yaratan aşılama kaynak tahsisi, negatif gelir vergisi gelir bölüşümü, aşırı talepte bütçe fazlası ise istikrar fonksiyonunun araçlarıdır.',
        "Kamu maliyesi teorisi: Musgrave'in fonksiyonlar ayrımı",
    ),
    # düzey 3
    '0022': patch(
        "Bir kamusal malın belirli bir üretim düzeyinde üç bireyin marjinal faydası (ek birim için ödemeye razı oldukları tutar) sırasıyla 20 ₺, 30 ₺ ve 50 ₺'dir. Bu düzeyde malın marjinal maliyeti 100 ₺ ise Samuelson koşuluna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': "Etkinlik için her bireyin marjinal faydası 100 ₺'ye ulaşmalıdır",
            'B': 'Marjinal faydalar yatay toplanınca talep yetersiz kalır, üretim azaltılmalıdır',
            'C': 'Marjinal faydaların toplamı maliyete eşit olduğundan üretim etkin düzeydedir',
            'D': 'Ortalama marjinal fayda maliyetin altında kaldığından üretim fazladır',
            'E': 'En yüksek marjinal fayda maliyetin altında kaldığından üretim fazladır',
        },
        'C',
        'Kamusal malı herkes aynı miktarda tükettiği için bireysel talepler **dikey** toplanır. Samuelson koşulu: bireysel marjinal faydaların toplamı marjinal maliyete eşit olmalıdır. 20 + 30 + 50 = 100 ₺ = marjinal maliyet olduğundan bu düzey etkindir. Tek bir bireyin ya da ortalamanın maliyetle karşılaştırılması özel mallar için geçerli yatay toplama mantığıdır.',
        'Kamu maliyesi teorisi: Samuelson koşulu',
    ),
    # düzey 2
    '0023': patch(
        'Bir mahallede sokak aydınlatması gönüllü bağışla finanse edilmek istenmiş, ancak sakinlerin çoğu komşuları öderse kendilerinin de aydınlatmadan yararlanacağını düşünerek bağış yapmamıştır. Bu durum aşağıdaki kavramlardan hangisiyle açıklanır?',
        {
            'A': 'Bedavacılık sorunu',
            'B': 'Mali yanılsama',
            'C': 'Ahlaki tehlike',
            'D': 'Ters seçim',
            'E': 'Ortak kaynakların trajedisi',
        },
        'A',
        'Dışlanamayan bir maldan ödeme yapmadan yararlanılabildiği için bireylerin gerçek tercihlerini gizleyip ödemekten kaçınması **bedavacılık** sorunudur; kamusal malların gönüllü katkıyla yetersiz sunulmasının temel nedenidir. Ortak kaynakların trajedisi rakip bir kaynağın aşırı kullanımıdır; ahlaki tehlike ve ters seçim asimetrik bilgiyle ilgilidir.',
        'Kamu maliyesi teorisi: bedavacılık',
    ),
    # düzey 2
    '0024': patch(
        'Aşağıdakilerden hangileri kamusal malların piyasada yetersiz sunulmasının nedenlerindendir?\n\nI. Dışlama maliyetinin yüksek olması\n\nII. Bireylerin maldan sağladıkları faydayı gizleme eğilimi\n\nIII. Ek tüketicinin marjinal maliyetinin sıfır olması\n\nIV. Tüketimde rakipliğin bulunması',
        {
            'A': 'II ve IV',
            'B': 'I, III ve IV',
            'C': 'I, II ve III',
            'D': 'I ve II',
            'E': 'I, II, III ve IV',
        },
        'C',
        'Dışlama güç olduğunda satıcı bedel toplayamaz (I); bireyler bedavacılık için tercihlerini gizler (II); ek kullanıcının maliyeti sıfır olduğundan etkin fiyat sıfırdır ve özel üretici bu fiyattan maliyetini karşılayamaz (III). Tüketimde rakiplik ise özel malların özelliğidir; rakiplik piyasa başarısızlığı değil, piyasa mübadelesinin olağan koşuludur (IV).',
        'Kamu maliyesi teorisi: kamusal malların yetersiz sunumu',
    ),
    # düzey 0
    '0025': patch(
        'Mülkiyet haklarının açıkça tanımlandığı ve pazarlık maliyetlerinin ihmal edilebilir olduğu durumlarda dışsallık sorununun taraflar arasındaki pazarlıkla etkin biçimde çözülebileceğini ileri süren yaklaşım hangisidir?',
        {
            'A': 'Pigou yaklaşımı',
            'B': 'Samuelson koşulu',
            'C': 'Tiebout modeli',
            'D': 'Coase teoremi',
            'E': 'Lindahl modeli',
        },
        'D',
        '**Coase teoremi**, işlem (pazarlık) maliyetlerinin sıfıra yakın ve mülkiyet haklarının açık olduğu durumda tarafların pazarlıkla etkin sonuca ulaşacağını, dolayısıyla vergi veya sübvansiyona gerek kalmayabileceğini savunur. Pigou yaklaşımı ise dışsallığın vergi veya sübvansiyonla düzeltilmesini öngörür.',
        'Kamu maliyesi teorisi: Coase teoremi',
    ),
    # düzey 2
    '0026': patch(
        'Negatif dışsallık yaratan bir faaliyete marjinal dışsal maliyet kadar Pigou vergisi konulduğunda aşağıdakilerden hangisi beklenir?',
        {
            'A': 'Firmanın özel maliyeti toplumsal maliyete eşitlenir, üretim azalır',
            'B': 'Dışsal maliyet tüketicilerden üçüncü kişilere aktarılır',
            'C': 'Toplumsal marjinal fayda yükselir, üretim değişmez',
            'D': 'Firmanın ortalama maliyeti düşer, kârı artar',
            'E': 'Üretim artar ve piyasa fiyatı düşer',
        },
        'A',
        'Pigou vergisi dışsal maliyeti firmanın maliyetine ekler (içselleştirme). Özel marjinal maliyet toplumsal marjinal maliyete eşitlenince firma üretimi toplumsal optimum düzeyine indirir; fiyat yükselir, üretim azalır.',
        'Kamu maliyesi teorisi: Pigou vergisinin etkisi',
    ),
    # düzey 2
    '0027': patch(
        'Sağlık sigortası piyasasında sigortacı, bireylerin risk düzeyini bilemediği için primi ortalama riske göre belirlemekte; bu da düşük riskli bireylerin sigortadan çekilmesine yol açmaktadır. Bu durum hangi kavramla ifade edilir?',
        {
            'A': 'Ahlaki tehlike',
            'B': 'Bedavacılık',
            'C': 'Dışlama etkisi',
            'D': 'Rant kollama',
            'E': 'Ters seçim',
        },
        'E',
        'Sözleşme **öncesinde** bir tarafın (sigortalı) risk bilgisine sahip olup diğerinin sahip olmaması, ortalama primin düşük riskliler için pahalı kalmasına ve havuzun yüksek risklilere kaymasına yol açar: **ters seçim**. Ahlaki tehlike ise sözleşme **sonrası** davranış değişikliğidir.',
        'Kamu maliyesi teorisi: asimetrik bilgi',
    ),
    # düzey 1
    '0028': patch(
        'Eğitim düzeyinin, işverene adayın verimliliği hakkında bilgi aktardığı ve böylece iş piyasasındaki bilgi asimetrisini azalttığı yaklaşım aşağıdakilerden hangisidir?',
        {
            'A': 'Rant kollama',
            'B': 'Ahlaki tehlike',
            'C': 'Tarama',
            'D': 'Sinyal verme',
            'E': 'Bedavacılık',
        },
        'D',
        '**Sinyal verme** yaklaşımında bilgili taraf (iş arayan), maliyetli bir gösterge (eğitim) edinerek niteliğini bilgisiz tarafa aktarır. Tarama ise bilgisiz tarafın (işveren), farklı sözleşme seçenekleri sunarak karşı tarafı ayrıştırmasıdır.',
        'Kamu maliyesi teorisi: asimetrik bilgi',
    ),
    # düzey 0
    '0029': patch(
        'Tek boyutlu bir konuda tercihleri tek tepeli olan seçmenlerin ikili çoğunluk oylamasında sonucu hangi seçmenin tercihi belirler?',
        {
            'A': 'Tercihi en yoğun seçmen',
            'B': 'Gündemi belirleyen seçmen',
            'C': 'Medyan seçmen',
            'D': 'Ortalama gelirli seçmen',
            'E': 'Kararsız seçmen',
        },
        'C',
        '**Medyan seçmen teoremine** göre tek boyutlu ve tek tepeli tercihlerde, tercih sıralamasının tam ortasındaki seçmenin ideal noktası ikili çoğunluk oylamasında diğer her seçeneği yener. Tercih yoğunluğu çoğunluk oylamasında hesaba katılmaz.',
        'Kamu maliyesi teorisi: medyan seçmen',
    ),
    # düzey 1
    '0030': patch(
        'İki milletvekilinin, her birinin kendi seçim bölgesindeki projeye diğerinin destek vermesi karşılığında birbirinin önergesine oy vermesi hangi kavramla açıklanır?',
        {
            'A': 'Rant kollama',
            'B': 'Medyan seçmen',
            'C': 'Rasyonel cehalet',
            'D': 'Oylama paradoksu',
            'E': 'Oy ticareti',
        },
        'E',
        '**Oy ticaretinde** (logrolling) tercih yoğunluğu yüksek taraflar karşılıklı destek anlaşmasıyla kendileri için önemli projeleri çoğunluktan geçirir. Bu durum toplam maliyeti faydasını aşan projelerin kabulüne ve kamu harcamalarının genişlemesine yol açabilir.',
        'Kamu maliyesi teorisi: oy ticareti',
    ),
    # düzey 1
    '0031': patch(
        'Yerli üreticilerin, kendilerine tekel gücü sağlayacak bir ithalat kotası çıkarılması için karar alıcılar nezdinde lobi harcaması yapması hangi kavramla açıklanır?',
        {
            'A': 'Bedavacılık',
            'B': 'Rasyonel cehalet',
            'C': 'Oy ticareti',
            'D': 'Rant kollama',
            'E': 'Ters seçim',
        },
        'D',
        'Kaynakların yeni bir değer üretmek yerine siyasi süreçle sağlanacak bir ranttan (kota, lisans, tekel hakkı) pay almak için harcanmasına **rant kollama** denir (Tullock, Krueger). Bu harcamalar toplum açısından israftır ve devlet başarısızlığının kaynaklarındandır.',
        'Kamu maliyesi teorisi: rant kollama',
    ),
    # düzey 2
    '0032': patch(
        "Seçmen Ayşe, bütçe kanununun ayrıntılarını öğrenmek için gereken zamanın, tek oyunun seçim sonucunu değiştirme olasılığı karşısında değmeyeceğini düşünerek bilgilenmemeyi tercih etmektedir. Ayşe'nin davranışı hangi kavramla açıklanır?",
        {
            'A': 'Mali yanılsama',
            'B': 'Rasyonel cehalet',
            'C': 'Oylama paradoksu',
            'D': 'Oy ticareti',
            'E': 'Bedavacılık',
        },
        'B',
        '**Rasyonel cehalet** (Downs), bilgi edinmenin maliyeti beklenen faydasını aştığında seçmenin bilgisiz kalmayı rasyonel olarak tercih etmesidir. Mali yanılsamada ise birey bilgilenmeye çalışsa bile vergi yükünü sistemin yapısı nedeniyle yanlış algılar.',
        'Kamu maliyesi teorisi: rasyonel cehalet',
    ),
    # düzey 2
    '0033': patch(
        'Hükümetin seçim öncesinde harcamaları artırıp vergileri düşürmesi, seçimden sonra ise daraltıcı politikalara yönelmesiyle oluşan ekonomik dalgalanma aşağıdakilerden hangisidir?',
        {
            'A': 'Mali sürüklenme',
            'B': 'Reel konjonktür teorisindeki dalgalanma',
            'C': 'Örümcek ağı dalgalanması',
            'D': 'Kuznets dalgası',
            'E': 'Politik konjonktür dalgalanması',
        },
        'E',
        "**Nordhaus'un politik konjonktür** modeline göre iktidar, seçmenlerin kısa hafızasından yararlanmak için seçim öncesi genişletici, seçim sonrası daraltıcı politika izler ve bu seçim takvimine bağlı dalgalanmalar üretir. Reel konjonktür teorisi dalgalanmaları teknoloji şoklarıyla açıklar.",
        'Kamu maliyesi teorisi: politik konjonktür',
    ),
    # düzey 1
    '0034': patch(
        'Aşağıdakilerden hangisi fonksiyonel gelir dağılımında pay alan faktör gelirlerinden biri değildir?',
        {
            'A': 'Sosyal yardım transferleri',
            'B': 'Girişimcilik karşılığı kâr',
            'C': 'Emek karşılığı ücret',
            'D': 'Toprak karşılığı rant',
            'E': 'Sermaye karşılığı faiz',
        },
        'A',
        '**Fonksiyonel gelir dağılımı**, milli gelirin üretime katılan faktörler arasında ücret (emek), rant (toprak), faiz (sermaye) ve kâr (girişimci) olarak paylaşımını inceler. Sosyal yardım transferleri üretime katkı karşılığı değildir; kişisel gelir dağılımını etkileyen karşılıksız aktarımlardır.',
        'Kamu maliyesi teorisi: fonksiyonel gelir dağılımı',
    ),
    # düzey 2
    '0035': patch(
        'Bir hükümet, toplam refahı en çok artıran politika yerine toplumdaki en düşük gelirli grubun refahını en çok artıran politikayı tercih etmektedir. Bu tercih hangi sosyal refah anlayışıyla uyumludur?',
        {
            'A': 'Faydacı (Bentham) anlayış',
            'B': 'Pareto ölçütü',
            'C': 'Kaldor-Hicks ölçütü',
            'D': 'Nash (çarpımsal) refah fonksiyonu',
            'E': 'Rawlsçı (maksimin) anlayış',
        },
        'E',
        "**Rawls'a** göre toplumsal refah, en kötü durumdaki bireyin refahıyla ölçülür (maksimin). Faydacı (Bentham) anlayış bireysel faydaların toplamını, Nash fonksiyonu faydaların çarpımını maksimize eder; Kaldor-Hicks ölçütü potansiyel tazmin ilkesine dayanır.",
        'Kamu maliyesi teorisi: sosyal refah fonksiyonları',
    ),
    # düzey 2
    '0036': patch(
        'Gini katsayısına ilişkin aşağıdaki ifadelerden hangileri doğrudur?\n\nI. 0 ile 1 arasında değer alır.\n\nII. Lorenz eğrisi tam eşitlik doğrusundan uzaklaştıkça küçülür.\n\nIII. Birbirini kesen farklı Lorenz eğrileri aynı Gini değerini verebilir.',
        {
            'A': 'Yalnız I',
            'B': 'I ve II',
            'C': 'II ve III',
            'D': 'I ve III',
            'E': 'I, II ve III',
        },
        'D',
        "Gini katsayısı tam eşitlikte 0, tam eşitsizlikte 1'dir (I). Lorenz eğrisi eşitlik doğrusundan uzaklaştıkça aradaki alan ve dolayısıyla Gini **büyür** (II yanlış). Kesişen iki Lorenz eğrisi farklı dağılımları gösterdiği hâlde aynı alanı, yani aynı Gini değerini verebilir (III).",
        'Kamu maliyesi teorisi: Gini katsayısı',
    ),
    # düzey 0
    '0037': patch(
        'Merkantilizmin 17-18. yüzyıllarda Alman ve Avusturya devletlerinde gelişen; devlet hazinesinin güçlendirilmesini, kamu yönetimi ve kamu gelirleri düzenini merkeze alan kolu hangisidir?',
        {
            'A': 'Kameralizm',
            'B': 'Fizyokrasi',
            'C': 'Liberalizm',
            'D': 'Tarihçi okul',
            'E': 'Kurumsalcılık',
        },
        'A',
        '**Kameralizm**, merkantilizmin Alman ve Avusturya versiyonudur; hükümdarın hazinesini (kamera) güçlendirmeyi, devlet mülk ve teşebbüs gelirlerini ve kamu yönetimi bilgisini ön plana çıkarır. Kamu maliyesinin ayrı bir disiplin olarak gelişmesinin öncülerinden sayılır.',
        'Kamu maliyesi teorisi: kameralizm',
    ),
    # düzey 1
    '0038': patch(
        'Paranın uzun dönemde reel değişkenler üzerinde etkisiz olduğunu, genişletici maliye politikasının dışlama etkisi nedeniyle etkisiz kalacağını ve para arzı artışının sabit bir kurala bağlanmasını savunan okul hangisidir?',
        {
            'A': 'Keynesyen okul',
            'B': 'Arz yönlü iktisat',
            'C': 'Monetarizm',
            'D': 'Kamu tercihi okulu',
            'E': 'Fizyokrasi',
        },
        'C',
        '**Monetaristler** (Friedman), enflasyonun parasal bir olgu olduğunu, uzun dönemde paranın yansız kaldığını ve maliye politikasının faizleri yükselterek özel harcamaları dışlayacağını savunur; para arzının sabit oranda büyümesini (kurallı para politikası) önerirler.',
        'Kamu maliyesi teorisi: monetarizm',
    ),
    # düzey 3
    '0039': patch(
        'Bir baraj projesi, su altında kalacak köyün halkına toplam 40 milyon ₺ zarar verirken şehir halkına toplam 100 milyon ₺ fayda sağlamaktadır; köylülere tazminat fiilen ödenmemektedir. Bu proje için aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Tazminat ödenmediği için fayda-maliyet analizine konu olamaz',
            'B': 'Kaldor-Hicks ölçütüne göre etkindir, Pareto iyileştirmesi değildir',
            'C': 'İki ölçüte göre de etkin değildir',
            'D': 'Hem Pareto iyileştirmesi hem Kaldor-Hicks ölçütüne göre etkindir',
            'E': 'Pareto iyileştirmesidir, Kaldor-Hicks ölçütüne göre etkin değildir',
        },
        'B',
        'Kazananların faydası (100 milyon ₺) kaybedenlerin zararından (40 milyon ₺) büyük olduğundan kaybedenler **potansiyel olarak** tazmin edilebilir: proje **Kaldor-Hicks** ölçütüne göre etkindir. Tazminat fiilen ödenmediği için köylülerin durumu kötüleşir; bu nedenle proje Pareto iyileştirmesi değildir.',
        'Kamu maliyesi teorisi: Kaldor-Hicks ölçütü',
    ),
    # düzey 2
    '0040': patch(
        'Aşağıdakilerden hangileri negatif dışsallığı azaltmaya yönelik uygun araçlardandır?\n\nI. Kirleten firmanın üretimine sübvansiyon verilmesi\n\nII. Emisyon izinlerinin alınıp satılabilmesi\n\nIII. Mülkiyet haklarının tanımlanıp taraflara pazarlık imkânı verilmesi\n\nIV. Faaliyete marjinal dışsal maliyet kadar vergi konması',
        {
            'A': 'I ve II',
            'B': 'I ve IV',
            'C': 'I, II, III ve IV',
            'D': 'II, III ve IV',
            'E': 'I, II ve III',
        },
        'D',
        'Pazarlanabilir izinler (II), Coase pazarlığı (III) ve Pigou vergisi (IV) negatif dışsallığı içselleştirmeye yönelik araçlardır. Kirleten firmanın **üretimine** sübvansiyon vermek (I) üretimi ve dolayısıyla kirliliği artırır. Kirliliği azaltmaya (azaltım teknolojisine) verilen destek ise ayrı bir araçtır ve bu öncülde söz konusu değildir.',
        'Kamu maliyesi teorisi: dışsallığa çözüm araçları',
    ),
    # düzey 0
    '0041': patch(
        'Tüketiminde rakiplik bulunmayan ve bedelini ödemeyenlerin tüketimden dışlanması mümkün olmayan ya da çok maliyetli olan mallar aşağıdakilerden hangisidir?',
        {
            'A': 'Özel mallar',
            'B': 'Tam kamusal mallar',
            'C': 'Ortak mülkiyet kaynakları',
            'D': 'Erdemli (merit) mallar',
            'E': 'Kulüp malları',
        },
        'B',
        '**Tam kamusal mal** tüketimde rakip olmayan ve dışlanamayan maldır (ör. milli savunma). Kulüp malları dışlanabilir ama belli bir kapasiteye kadar rakip değildir; ortak mülkiyet kaynakları rakip ama dışlanamaz. Erdemli mal ayrımı bu iki özelliğe değil, tercihlere müdahale gerekçesine dayanır.',
        'Kamu maliyesi teorisi: mal türleri',
    ),
    # düzey 2
    '0042': patch(
        'Normal saatlerde rahat kullanılan ücretsiz bir şehir içi yol, trafiğin yoğunlaştığı saatlerde bir aracın eklenmesi diğerlerinin yolculuğunu yavaşlatacak kadar sıkışmaktadır. Yoğun saatlerde bu yol hangi mal türüne yaklaşır?',
        {
            'A': 'Ortak mülkiyet kaynağı',
            'B': 'Özel mal',
            'C': 'Kulüp malı',
            'D': 'Rakipsiz ve dışlanamaz tam kamusal mal',
            'E': 'Erdemli mal',
        },
        'A',
        'Ücretsiz yolda kimse dışlanmaz. Tıkanıklık başladığında ek aracın diğer kullanıcılara maliyet yüklemesi tüketimi **rakip** hâle getirir; rakip ve dışlanamayan mal ortak mülkiyet kaynağıdır. Yolun kulüp malı sayılması için ücretle dışlama gerekir; tam kamusal mal ise rakip değildir.',
        'Kamu maliyesi teorisi: mal türleri',
    ),
    # düzey 2
    '0043': patch(
        'Devletin zorunlu temel eğitimi ücretsiz sunması ve emniyet kemeri kullanımını zorunlu kılması, bireylerin tercihlerine müdahaleyi hangi mal kategorisine dayanarak gerekçelendirir?',
        {
            'A': 'Tam kamusal mallar',
            'B': 'Kulüp malları',
            'C': 'Erdemsiz (demerit) mallar',
            'D': 'Ortak mülkiyet kaynakları',
            'E': 'Erdemli (merit) mallar',
        },
        'E',
        "Musgrave'in **erdemli mal** kavramı, bireylerin faydasını tam değerlendiremedikleri için toplumsal açıdan istenenden az tükettikleri mallarda devletin tüketimi teşvik etmesini ya da zorunlu kılmasını açıklar. Erdemsiz mallarda (alkol, tütün) tüketim kısılmak istenir; eğitim ve emniyet kemeri dışlanabilir olduğundan tam kamusal mal değildir.",
        'Kamu maliyesi teorisi: erdemli mallar',
    ),
    # düzey 2
    '0044': patch(
        "Bir fabrikanın ürettiği her ton ürün, çevreye üretim düzeyinden bağımsız olarak 40 ₺'lik marjinal dışsal maliyet yüklemektedir. Pigou yaklaşımına göre üretime konulacak birim vergi ne olmalıdır?",
        {
            'A': 'Ton başına 0 ₺',
            'B': 'Ton başına 80 ₺',
            'C': 'Ton başına 40 ₺',
            'D': 'Ton başına 60 ₺',
            'E': 'Ton başına 20 ₺',
        },
        'C',
        "**Pigou vergisi**, toplumsal optimum üretim düzeyindeki marjinal dışsal maliyete eşit belirlenir; böylece firmanın özel marjinal maliyeti toplumsal marjinal maliyete eşitlenir. Dışsal maliyet sabit 40 ₺ olduğundan birim vergi 40 ₺'dir.",
        'Kamu maliyesi teorisi: Pigou vergisi',
    ),
    # düzey 0
    '0045': patch(
        'Kirlilik için toplam bir üst sınır belirlenip bu sınır kadar iznin firmalar arasında alınıp satılabilmesine dayanan çevre politikası aracı aşağıdakilerden hangisidir?',
        {
            'A': 'Pigou vergisi',
            'B': 'Pazarlanabilir kirlilik izinleri',
            'C': 'Emisyon standardı',
            'D': 'Coase pazarlığı',
            'E': 'Kirletene sübvansiyon',
        },
        'B',
        '**Pazarlanabilir kirlilik izinlerinde** (sınırla ve ticaret yap) toplam emisyon miktarı devletçe belirlenir, fiyatı izin piyasası oluşturur; azaltım maliyeti düşük firmalar izin satar, yüksek olanlar alır. Pigou vergisinde fiyat devletçe belirlenir, miktar piyasada oluşur; emisyon standardı ise her firmaya doğrudan sınır koyar.',
        'Kamu maliyesi teorisi: çevre politikası araçları',
    ),
    # düzey 3
    '0046': patch(
        "Bir malın piyasa fiyatı ve özel marjinal maliyeti 50 ₺'dir. Üretimin topluma yüklediği maliyet dahil toplumsal marjinal maliyet ise 70 ₺'dir. Buna göre aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Fiyat özel maliyete eşit olduğundan dışsallık bulunmaz',
            'B': 'Birim başına 20 ₺ negatif dışsallık vardır; üretim optimumun üzerindedir',
            'C': 'Dışsallığı düzeltmek için birim başına 70 ₺ vergi konmalıdır',
            'D': 'Birim başına 20 ₺ pozitif dışsallık vardır; üretim optimumun altındadır',
            'E': 'Üretim optimumun altındadır; birim başına 20 ₺ sübvansiyon gerekir',
        },
        'B',
        'Toplumsal marjinal maliyet (70 ₺) özel marjinal maliyeti (50 ₺) aştığından aradaki 20 ₺ üçüncü kişilere yüklenen **negatif dışsallıktır**. Firma yalnız özel maliyete baktığı için toplumsal optimumdan **fazla** üretir. Düzeltici vergi 70 ₺ değil, dışsal maliyet kadar (20 ₺) olmalıdır.',
        'Kamu maliyesi teorisi: dışsallığın ölçülmesi',
    ),
    # düzey 2
    '0047': patch(
        'Ortalama maliyetin geniş bir üretim aralığında azaldığı bir doğal tekelde fiyat marjinal maliyete eşit belirlenirse aşağıdakilerden hangisi ortaya çıkar?',
        {
            'A': 'Ortalama maliyet yükselmeye başlar',
            'B': 'Üretim toplumsal optimumun altında kalır',
            'C': 'Tüketici rantı ortadan kalkar',
            'D': 'Firma olağanüstü kâr elde eder',
            'E': 'Firma zarar eder; açık sübvansiyonla karşılanmalıdır',
        },
        'E',
        'Ortalama maliyet azalıyorsa marjinal maliyet ortalama maliyetin altındadır. Fiyat marjinal maliyete eşitlenince etkin miktar üretilir, ancak fiyat ortalama maliyeti karşılamadığından firma **zarar** eder. Bu nedenle ya açık sübvansiyonla kapatılır ya da ortalama maliyet veya Ramsey fiyatlandırmasına başvurulur.',
        'Kamu maliyesi teorisi: doğal tekel',
    ),
    # düzey 1
    '0048': patch(
        'Aşağıdakilerden hangisi bir piyasa başarısızlığı nedeni değildir?',
        {
            'A': 'Dışsallıklar',
            'B': 'Alıcı ve satıcı arasında asimetrik bilgi bulunması',
            'C': 'Mülkiyet haklarının açıkça tanımlanmış olması',
            'D': 'Ölçeğe göre artan getiri',
            'E': 'Eksik piyasaların bulunması',
        },
        'C',
        "Eksik piyasalar, asimetrik bilgi, ölçeğe göre artan getiri (doğal tekel) ve dışsallıklar piyasanın kaynakları etkin dağıtamamasının nedenleridir. Mülkiyet haklarının açık tanımlanması ise Coase'a göre dışsallıkların pazarlıkla çözülmesine imkân veren, etkinliği destekleyen bir koşuldur.",
        'Kamu maliyesi teorisi: piyasa başarısızlıkları',
    ),
    # düzey 2
    '0049': patch(
        "Beş kişilik bir belediye meclisi park bütçesini oylamaktadır. Üyelerin tek tepeli tercihlerine göre ideal bütçeleri 10, 20, 35, 60 ve 90 bin ₺'dir. İkili çoğunluk oylamasıyla kabul edilecek bütçe kaç bin ₺'dir?",
        {
            'A': '43',
            'B': '60',
            'C': '20',
            'D': '35',
            'E': '90',
        },
        'D',
        "Tek tepeli tercihlerde çoğunluk oylaması **medyan** üyenin ideal noktasını seçer: sıralı değerlerde ortadaki üçüncü değer 35'tir. 35, herhangi bir alternatife karşı en az üç oy alır. 43 bin ₺ aritmetik ortalamadır ((10+20+35+60+90)/5); çoğunluk oylaması ortalamayı değil medyanı öne çıkarır.",
        'Kamu maliyesi teorisi: medyan seçmen',
    ),
    # düzey 2
    '0050': patch(
        'Bir genel müdürlüğün yöneticileri, birimin çıktısı değişmediği hâlde her yıl daha büyük ödenek talep etmekte ve bunu birimin prestiji ile personel sayısıyla gerekçelendirmektedir. Bu davranışı açıklayan model hangisidir?',
        {
            'A': 'Niskanen bürokrasi modeli',
            'B': 'Peacock-Wiseman yaklaşımı',
            'C': 'Leviathan modeli',
            'D': 'Baumol hastalığı',
            'E': 'Mali yanılsama modeli',
        },
        'A',
        "**Niskanen'e** göre bürokratların fayda fonksiyonunda maaş, prestij ve güç yer alır ve bunlar yönetilen bütçeyle artar; bu nedenle bürokratlar bütçeyi **en yüksek** düzeye çıkarmaya çalışır ve kamu hizmeti etkin düzeyin üzerinde üretilir. Leviathan modeli bürokratı değil, vergi gelirini maksimize eden devleti esas alır.",
        'Kamu maliyesi teorisi: bürokrasi teorisi',
    ),
    # düzey 1
    '0051': patch(
        'Devleti vergi gelirini en yüksek düzeye çıkarmaya çalışan tekelci bir yapı olarak gören ve bu nedenle anayasal vergi sınırları gibi mali kısıtları savunan yaklaşım aşağıdakilerden hangisidir?',
        {
            'A': 'Niskanen bürokrasi modeli',
            'B': "Musgrave'in fonksiyonlar ayrımı",
            'C': 'Leviathan modeli',
            'D': "Downs'un seçmen modeli",
            'E': 'Wagner kanunu',
        },
        'C',
        "**Brennan ve Buchanan'ın Leviathan modeli** devleti gelir maksimize eden bir tekel olarak modeller; vergi tabanının daraltılması, anayasal vergi limitleri ve mali ademi merkeziyet gibi kısıtlar bu eğilimi sınırlamak için önerilir.",
        'Kamu maliyesi teorisi: Leviathan modeli',
    ),
    # düzey 1
    '0052': patch(
        "Aşağıdakilerden hangisi Arrow'un imkânsızlık teoreminde toplumsal tercih kuralının sağlaması istenen koşullardan biri değildir?",
        {
            'A': 'Diktatörlüğün olmaması',
            'B': 'İlgisiz seçeneklerden bağımsızlık',
            'C': 'Pareto ilkesi',
            'D': 'Sınırsız tercih alanı',
            'E': 'Medyan seçmen kuralı',
        },
        'E',
        'Arrow, bireysel tercihleri toplumsal tercihe dönüştüren bir kuralın **sınırsız tercih alanı**, **Pareto ilkesi**, **ilgisiz seçeneklerden bağımsızlık** ve **diktatörlüğün olmaması** koşullarını (geçişlilikle birlikte) aynı anda sağlayamayacağını gösterir. Medyan seçmen bir koşul değil, tek tepeli tercihlerde çoğunluk kuralının sonucudur.',
        "Kamu maliyesi teorisi: Arrow'un imkânsızlık teoremi",
    ),
    # düzey 2
    '0053': patch(
        'Aşağıdakilerden hangileri devlet (kamu) başarısızlığının nedenleri arasında sayılır?\n\nI. Bürokratların bütçe maksimizasyonu eğilimi\n\nII. Baskı gruplarının rant kollama faaliyetleri\n\nIII. Üretimde dışsallıkların bulunması\n\nIV. Kamu hizmetinin maliyeti ile faydası arasındaki bağın zayıf olması',
        {
            'A': 'I, II ve IV',
            'B': 'I, II ve III',
            'C': 'I, II, III ve IV',
            'D': 'I ve II',
            'E': 'II ve III',
        },
        'A',
        'Bürokratik bütçe maksimizasyonu (I), rant kollama (II) ve kamu kesiminde hizmetin maliyetini ödeyenlerle faydalananların ayrışması nedeniyle maliyet-fayda bağının zayıflaması (IV) devlet başarısızlığının nedenleridir. Dışsallıklar (III) ise devlet müdahalesini gerekçelendiren **piyasa** başarısızlığı nedenidir.',
        'Kamu maliyesi teorisi: devlet başarısızlığı',
    ),
    # düzey 2
    '0054': patch(
        "Ortalama geliri 50.000 ₺ olan bir toplumda, mevcut dağılımla aynı toplumsal refahı sağlayacak eşit dağılımlı eşdeğer gelir 40.000 ₺'dir. Dalton-Atkinson eşitsizlik endeksi kaçtır?",
        {
            'A': '1,25',
            'B': '0,20',
            'C': '0,10',
            'D': '0,80',
            'E': '0,25',
        },
        'B',
        "Atkinson endeksi = 1 − (eşit dağılımlı eşdeğer gelir / ortalama gelir) = 1 − 40.000 / 50.000 = **0,20**. Toplum, tam eşitliğe geçebilmek için toplam gelirinin %20'sinden vazgeçmeye razıdır. 0,80 oranın kendisi, 1,25 ise ters orandır.",
        'Kamu maliyesi teorisi: Atkinson endeksi',
    ),
    # düzey 3
    '0055': patch(
        "Bir negatif gelir vergisi uygulamasında garanti gelir 30.000 ₺, vergi (kesinti) oranı %50'dir. Yıllık kazancı 20.000 ₺ olan bir birey devletten ne kadar ödeme alır?",
        {
            'A': '40.000 ₺',
            'B': '15.000 ₺',
            'C': '10.000 ₺',
            'D': '20.000 ₺',
            'E': '30.000 ₺',
        },
        'D',
        "Negatif gelir vergisinde ödeme = garanti gelir − (oran × kazanç) = 30.000 − (0,50 × 20.000) = **20.000 ₺**. Bireyin toplam geliri 40.000 ₺ olur; ödeme, kazancın 60.000 ₺'ye (başa baş gelir = 30.000 / 0,50) ulaştığı noktada sıfırlanır. 40.000 ₺ ödeme değil, bireyin toplam gelirdir.",
        'Kamu maliyesi teorisi: negatif gelir vergisi',
    ),
    # düzey 0
    '0056': patch(
        'Yalnız tarımın net ürün (produit net) yarattığını ileri sürerek toprak üzerinden tek vergi alınmasını savunan iktisadi düşünce okulu hangisidir?',
        {
            'A': 'Tarihçi okul',
            'B': 'Fizyokratlar',
            'C': 'Klasik iktisatçılar',
            'D': 'Kameralistler',
            'E': 'Merkantilistler',
        },
        'B',
        "Quesnay'nin öncülüğündeki **fizyokratlar**, net ürünün yalnız tarımda (toprakta) yaratıldığını savunur; bu nedenle bütün vergilerin sonunda toprak sahiplerine yansıyacağını düşünerek arazi üzerinden **tek vergi** (impôt unique) önerirler.",
        'Kamu maliyesi teorisi: fizyokratlar',
    ),
    # düzey 0
    '0057': patch(
        'Bütçe denkliğini değil tam istihdam ve fiyat istikrarı gibi ekonomik sonuçları esas alan ve kamu gelir ve harcamalarının bu hedeflere göre ayarlanmasını savunan fonksiyonel maliye yaklaşımı hangi iktisatçıyla özdeşleşmiştir?',
        {
            'A': 'Arthur Laffer',
            'B': 'Adam Smith',
            'C': 'Milton Friedman',
            'D': 'David Ricardo',
            'E': 'Abba Lerner',
        },
        'E',
        '**Fonksiyonel maliye** kavramını Keynesyen çizgide Abba Lerner geliştirmiştir: bütçe açığı veya fazlası kendi başına amaç değildir; önemli olan maliye politikasının ekonomideki işlevidir. Smith ve Ricardo klasik, Friedman monetarist, Laffer arz yanlı iktisatla özdeşleşir.',
        'Kamu maliyesi teorisi: fonksiyonel maliye',
    ),
    # düzey 1
    '0058': patch(
        'Bir hükümet, yüksek marjinal vergi oranlarını düşürmenin çalışma, tasarruf ve yatırım isteğini artırarak vergi tabanını genişleteceğini ve vergi gelirini azaltmayacağını savunmaktadır. Bu görüş hangi yaklaşımla uyumludur?',
        {
            'A': 'Arz yönlü iktisat',
            'B': 'Post-Keynesyen iktisat',
            'C': 'Monetarizm',
            'D': 'Kurumsalcı iktisat',
            'E': 'Keynesyen iktisat',
        },
        'A',
        '**Arz yönlü iktisat**, vergilerin talep üzerindeki etkisinden çok çalışma, tasarruf ve yatırım üzerindeki teşvik etkisine odaklanır; Laffer eğrisine dayanarak yüksek oranlarda vergi indiriminin hasılatı artırabileceğini savunur. Keynesyen yaklaşım vergi indirimini toplam talep kanalıyla değerlendirir.',
        'Kamu maliyesi teorisi: arz yanlı iktisat',
    ),
    # düzey 2
    '0059': patch(
        'Çocuklu aileler, okul hizmetleri daha nitelikli ancak emlak vergisi daha yüksek olan ilçelere taşınmaktadır. Bireylerin yerel kamu hizmeti tercihlerini bu biçimde açığa vurmasını açıklayan model hangisidir?',
        {
            'A': 'Medyan seçmen modeli',
            'B': 'Lindahl modeli',
            'C': 'Tiebout modeli',
            'D': "Oates'in ademi merkeziyet teoremi",
            'E': 'Leviathan modeli',
        },
        'C',
        "**Tiebout modeline** göre bireyler tercih ettikleri vergi-hizmet bileşimini sunan yerel yönetimin bölgesine taşınarak tercihlerini 'ayaklarıyla oy vererek' açığa vurur; bu hareketlilik yerel kamusal mallarda tercih açığa vurma sorununu hafifletir. Oates teoremi ise hizmetin hangi yönetim düzeyinde sunulması gerektiğiyle ilgilidir.",
        'Kamu maliyesi teorisi: Tiebout modeli',
    ),
    # düzey 2
    '0060': patch(
        "Buchanan'ın kulüp teorisine göre bir yüzme havuzu gibi kulüp malında optimal üye sayısı hangi noktada belirlenir?",
        {
            'A': 'Üye başına aidat sıfıra indiğinde',
            'B': 'Tıkanıklık maliyeti ortaya çıkmadan hemen önce',
            'C': 'Havuzun fiziki kapasitesinin tamamı dolduğunda',
            'D': 'Ek üyenin sağladığı maliyet tasarrufu, yol açtığı tıkanıklık maliyetine eşit olduğunda',
            'E': 'Üye sayısının çoğunluk oylamasında medyan üyenin tercih ettiği düzeye ulaştığı noktada',
        },
        'D',
        'Kulüp malında yeni üye, sabit maliyetin daha çok kişiye bölünmesiyle mevcut üyelerin payını düşürür (fayda), ama kalabalık arttıkça tıkanıklık maliyeti doğurur. **Optimal üye sayısı** ek üyenin sağladığı marjinal maliyet tasarrufunun, yarattığı marjinal tıkanıklık maliyetine eşit olduğu noktadır; bu nokta tıkanıklığın hiç olmadığı ya da kapasitenin tamamen dolduğu uç noktalar değildir.',
        'Kamu maliyesi teorisi: kulüp teorisi',
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
    print(f"1 paket / {len(PATCHES)} soru ('Kamu Maliyesi Temel Kavramlar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
