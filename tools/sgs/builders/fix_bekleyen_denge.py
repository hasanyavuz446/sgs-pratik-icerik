#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""17 paket — leksik temizlik + elle boy dengesi (URETIM_KURALLARI §5).

İki grup:

(a) `fix_lexical_tell.py`'nin BEKLEYEN listesindeki 11 paket — mekanik temizlik
çeldiricilerden ~15 karakterlik kalıp-dolguyu aldığı için doğru şık sistematik
EN UZUN kalıyor ve kör öğrenci %26'dan %45'e kadar çıkıyordu. Bu builder aynı
temizliği uygular, ardından dengeyi ELLE kurar.

REÇETE (tms_21'de doğrulandı): doğru şıkkı kısaltma — **çeldiriciye gerçek
içerik ekle**. Eklenen metin dolgu değil, yanlış iddianın kendi mantıksal
sonucudur; bu yüzden çeldiriciyi daha inandırıcı yapar ve soruyu zorlaştırır.
İki dosyada (maliye/*) çeldiriciler ikinci bir dolgu ailesi taşıdığından
("…bu ilişki piyasa/politika koşulları ne olursa olsun değişmez" vb.) uzatma
yerine dolgu gerçek içerikle DEĞİŞTİRİLDİ.

Hangi adayın uygulanacağı ölçümle seçildi: adayların tamamı uygulanınca doğru
şık bu kez sistematik ORTADA kalıyor ve "iki ucu ele, ortadan tahmin et"
stratejisi öne geçiyor (temerrut_tazminat'ta kör %30). Bu yüzden her pakette
kör öğrenciyi en aza indiren alt küme seçildi ve burada DONDURULDU.

(b) Kombine ölçüt (işaretliyi ele + en uzunu seç) 2026-07-28'de açılınca eşiği
aşan 6 paket: kurumlar_vergisi %35, kambiyo_senetleri %33, gelir_vergisi %31,
sozlesme_turleri %31, haksiz_rekabet %31, kiymetli_evrak %31. Bunlarda kusur
şuydu: eleme adımı EN UZUN çeldiriciyi atıyor, doğru şık ikinciyken birinciye
çıkıyordu. Aynı reçete uygulandı.

Sonuç: kör öğrenci %21-35 → %20-25, boy dağılımı iki uçlu, kalıp-dolgu 0.

    --check : dosyalar işlenmiş hâlde mi (fark varsa çıkış 1)
    --write : içerik + uygulama repolarına yaz

⚠️ SAHIPLIK DEVRI (2026-08-14): meslek_hukuku/sorumluluk_ve_yasaklar.json blogu bu dosyadan CIKARILDI.
O paketin 60 sorusunun tamami yapisal kalibrasyon turunda yeniden yazildi ve
sahiplik ilgili build_hukuk_*_yapisal.py dosyasina gecti.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fix_lexical_tell import ROOT, APP_ROOT, guvenli, temizle

# {paket: {"<soru-son4>|<harf>": ["ek"|"yaz", metin]}}
YAMALAR = {
    "borclar_hukuku/haksiz_fiil.json": {
        "0005|B": [
            "ek",
            "; hafif ihmalde tazminat talebi doğrudan reddedilir"
        ],
        "0022|D": [
            "ek",
            "; kişilik hakkı ihlallerinde de aynı sınır geçerlidir"
        ],
        "0028|C": [
            "ek",
            "; rücu tutarı çalışanın kusuru oranında azaltılamaz"
        ],
        "0041|A": [
            "ek",
            "; yarışan talep kavramı Türk hukukunda benimsenmemiştir"
        ],
        "0054|B": [
            "ek",
            "; ceza davası açılmamışsa manevi tazminat istenemez"
        ],
        "0060|B": [
            "ek",
            "; yansıma yoluyla uğranan acı hukuken korunmaz"
        ]
    },
    "borclar_hukuku/ozel_durumlar.json": {
        "0016|C": [
            "ek",
            "; ceza ancak hükmün kesinleşmesinden sonra istenebilir"
        ],
        "0021|C": [
            "ek",
            "; taraflar bu oranı sözleşmeyle değiştiremez"
        ],
        "0023|A": [
            "ek",
            "; tacir sıfatı bu konuda bir fark yaratmaz"
        ],
        "0029|A": [
            "ek",
            "; devir işlemi ayrı bir sözleşmeyle yapılır"
        ],
        "0036|C": [
            "ek",
            "; yetkisiz temsilcinin sorumluluğu bu hâlde gündeme gelmez"
        ],
        "0057|D": [
            "ek",
            "; (Ü) iyiniyetli olsa dahi (S)'ye başvuramaz"
        ],
        "0058|D": [
            "ek",
            "; alacaklılardan birine yapılan ödeme borçluyu kurtarmaz"
        ]
    },
    "borclar_hukuku/sebepsiz_zenginlesme.json": {
        "0005|C": [
            "ek",
            "; iyiniyetli olsa dahi bu yol kapalıdır"
        ],
        "0011|A": [
            "yaz",
            "Hukuka ya da ahlaka aykırı bir sonucun gerçekleşmesi amacıyla verilen şey, veren kişi tarafından tam olarak geri istenebilir; verenin amacı bu talebi engellemez"
        ],
        "0014|A": [
            "ek",
            "; iade sırasında yapılan giderler de kapsam dışında kalır"
        ],
        "0029|D": [
            "ek",
            "; zamanaşımı def'i talebi tümüyle sona erdirir"
        ],
        "0036|D": [
            "ek",
            "; fakirleşenin durumu öğrenmesi süreyi başlatmaz"
        ],
        "0039|A": [
            "ek",
            "; zenginleşmenin ölçüsü yalnızca ispat kolaylığı sağlar"
        ],
        "0045|B": [
            "ek",
            "; öğrenme tarihi yalnızca on yıllık süre bakımından önem taşır"
        ],
        "0051|A": [
            "ek",
            "; kullanım karşılığı ayrı bir sebebe dayandırılamaz"
        ],
        "0056|B": [
            "ek",
            "; iyiniyet yalnızca yapılan giderlerin istenmesinde etkili olur"
        ]
    },
    "borclar_hukuku/temerrut_tazminat.json": {
        "0001|E": [
            "ek",
            "; kusursuz sorumluluk ilkesi bu ilişkide uygulanmaz"
        ],
        "0003|A": [
            "ek",
            "; alacaklı doğrudan yardımcı kişiye başvurur"
        ],
        "0004|B": [
            "ek",
            "; yazılılık yalnızca ispat kolaylığı sağlar"
        ],
        "0011|B": [
            "ek",
            "; gecikme tek başına yalnızca aynen ifa talebini doğurur"
        ],
        "0013|A": [
            "ek",
            "; temerrüde düşmüş olması bu sonucu değiştirmez"
        ],
        "0016|C": [
            "yaz",
            "Alacaklı aşkın zararını isteyebilmek için borçlunun bu zararda kusurlu olduğunu ayrıca ispat etmekle yükümlüdür; ispat edemezse talebi reddedilir"
        ],
        "0022|E": [
            "ek",
            "; tek taraflı fesih beyanı sonuç doğurmaz"
        ],
        "0025|B": [
            "ek",
            "; müspet zarar yalnızca aynen ifa talebinde gündeme gelir"
        ],
        "0035|E": [
            "ek",
            "; kusur derecesi tazminatın belirlenmesinde etkili olmaz"
        ],
        "0036|A": [
            "ek",
            "; seçtiği kalem dışındaki talebi dinlenmez"
        ],
        "0049|A": [
            "ek",
            "; kredi kullanılmış olması bu sonucu değiştirmez"
        ],
        "0055|C": [
            "yaz",
            "Borçlu, imkânsızlaşan bölümün parasal karşılığını (Z)'ye tazminat olarak öder; sözleşme geri kalan bölümüyle ayakta kalır ve (Z) başkaca bir hak ileri süremez"
        ],
        "0056|D": [
            "yaz",
            "Kesin vade kararlaştırılmadığı için (A2) temerrüde düşürülemez; (B2) yalnızca ifayı bekler ve geçen süreye katlanır, ayrıca faiz de isteyemez"
        ]
    },
    "maliye/butce_maliye_politikasi.json": {
        "0003|D": [
            "yaz",
            "Bütçenin birden fazla belgeye dağıtılması ve her kurumun kendi gelirini kendi gideri için kullanmasıdır; bu yolla mali saydamlığın arttığı kabul edilir"
        ],
        "0006|B": [
            "yaz",
            "Yürütmenin harcamaları yaptıktan sonra yasama organından onay almasıdır; bu nedenle bütçe kanunu harcama yılının sonunda çıkarılır"
        ],
        "0017|A": [
            "yaz",
            "Merkez Bankasının para arzını ve faiz oranlarını ayarlamasıdır; bu nedenle vergi ve kamu harcaması kararları maliye politikasının dışında kalır"
        ],
        "0020|A": [
            "yaz",
            "Durgunluk döneminde kamu harcamalarını artırarak ve vergileri indirerek uygulanır; böylece toplam talebin daraldığı kabul edilir"
        ],
        "0022|E": [
            "ek",
            "; kamu kesiminin ayrıca bir düzenleme yapması gerekmez"
        ],
        "0023|B": [
            "yaz",
            "İhtiyari politika kendiliğinden işler; otomatik stabilizatörler ise her seferinde ayrı bir karar gerektirir. Bu nedenle işsizlik sigortası ihtiyari politika aracı sayılır"
        ],
        "0029|B": [
            "yaz",
            "Bütçenin kaynak dağılımını düzenlemesi ve üretim faktörlerini kamu ile özel kesim arasında paylaştırmasıdır; bu işlev bütçenin hukuki değil iktisadi yönünü oluşturur"
        ],
        "0030|A": [
            "yaz",
            "Yürütmenin dilediği gibi harcama yapma hakkıdır; bu nedenle bütçe kanununun yasama organınca kabul edilmesi aranmaz ve kesin hesap denetimi yapılmaz"
        ],
        "0033|C": [
            "ek",
            "; genellik ilkesi ise bütçenin bir yılı kapsamasını anlatır"
        ],
        "0034|C": [
            "yaz",
            "Vadesi gelen kamu borçlarının ödeme yapılmaksızın kendiliğinden silinmesidir; bu nedenle borç servisi bütçede ayrı bir gider kalemi olarak yer almaz"
        ],
        "0039|A": [
            "yaz",
            "Borç yükü ve faiz ödemeleri azalır, gelecek nesillere yük kalmaz; bu nedenle borçlanma vergiye tercih edilen kalıcı bir finansman yöntemi sayılır"
        ],
        "0042|C": [
            "ek",
            "; ihtiyari politika ise kendiliğinden devreye girer"
        ],
        "0047|A": [
            "yaz",
            "Klasik anlayış açık bütçeyi, modern anlayış denk bütçeyi savunur; bu nedenle klasik maliyeciler bütçe açığını ekonomik canlanmanın aracı olarak görmüştür"
        ],
        "0052|A": [
            "yaz",
            "Gelecek yıla ait bütçe tahminlerini içeren kanundur; bu nedenle uygulama sonuçlarının yasama organınca ayrıca denetlenmesi gerekmez"
        ],
        "0054|E": [
            "yaz",
            "Maliye politikası gelir dağılımını kesin olarak bozar; bu nedenle artan oranlı vergiler ve sosyal transferler dağılımı daha da eşitsiz hâle getirir"
        ],
        "0056|A": [
            "yaz",
            "Devletin topladığı verginin adıdır; bu nedenle harcama yapabilmek için ayrıca yasama organından izin alınması gerekmez"
        ]
    },
    "maliye/kamu_gelir_gider.json": {
        "0002|B": [
            "yaz",
            "Gerçek harcamalar karşılıksızdır; transfer harcamaları mal-hizmet alımıdır. Bu nedenle transfer harcamaları millî gelire doğrudan katkı yapar, gerçek harcamalar ise yalnızca satın alma gücü aktarımı sağlar"
        ],
        "0003|A": [
            "yaz",
            "Cari harcamalar uzun ömürlü sermaye malı alımıdır; yatırım harcamaları ise günlük giderleri karşılar. Buna göre personel giderleri yatırım, bina yapımı ise cari harcama olarak sınıflandırılır"
        ],
        "0008|A": [
            "yaz",
            "Devletin bir malını satarak elde ettiği gelirdir; bu nedenle mülk ve teşebbüs gelirleri içinde yer alır ve sosyal güvenlik kurumlarının topladığı primler bu grubun dışında kalır"
        ],
        "0014|E": [
            "yaz",
            "Verginin yalnızca yabancılardan alınmasıdır; bu nedenle yerleşik mükellefler vergi yükünün dışında tutulur ve yansıma yalnızca uluslararası ticarette gündeme gelir"
        ],
        "0015|A": [
            "yaz",
            "Vergiden kaçınma yasa dışı, vergi kaçakçılığı yasaldır; bu nedenle kaçınma hâlinde vergi ziyaı cezası uygulanır, kaçakçılık ise yalnızca idari uyarıyla sonuçlanır"
        ],
        "0017|A": [
            "yaz",
            "Dolaysız vergiler harcama üzerinden, dolaylı vergiler gelir üzerinden alınır; bu nedenle katma değer vergisi dolaysız, gelir vergisi ise dolaylı vergi olarak sınıflandırılır"
        ],
        "0022|B": [
            "yaz",
            "Kişilerin devlete gönüllü olarak yaptığı bağış ve yardımlardan oluşan isteğe bağlı bir kamu geliridir; bu nedenle tahsili için cebrî icra yoluna başvurulamaz ve bütçede tahmini gelir olarak gösterilmez"
        ],
        "0023|C": [
            "ek",
            "; karşılıksız yapılan ödemeler ise transfer harcaması sayılır"
        ],
        "0024|C": [
            "ek",
            "; karşılıksız aktarımlar gerçek harcama grubunda toplanır"
        ],
        "0028|A": [
            "yaz",
            "İleri yansımada vergi üreticiye, geri yansımada tüketiciye aktarılır; bu nedenle talebin esnek olduğu piyasalarda yükü tüketici, esnek olmadığı piyasalarda ise üretici taşır"
        ],
        "0038|B": [
            "yaz",
            "Devletin sahip olduğu bir taşınmazı veya iktisadi işletmesini satarak gelir elde etmesidir; bu nedenle bir mülk (teşebbüs) geliri sayılır ve üreticiye yapılan karşılıksız ödemelerden ayrılır"
        ],
        "0044|E": [
            "yaz",
            "Olağan gelirler elde edilmez; kamu harcamaları yalnızca borçlanma ve para basımıyla karşılanır. Bu nedenle vergiler olağanüstü gelir grubunda sınıflandırılır"
        ],
        "0057|D": [
            "ek",
            "; bu oran yalnızca dolaylı vergiler için hesaplanır"
        ],
        "0058|B": [
            "yaz",
            "Genellik verginin yalnızca zenginlerden, eşitlik ise yalnızca fakirlerden alınmasını öngörür; bu nedenle asgari geçim indirimi genellik ilkesinin, artan oranlı tarife ise eşitlik ilkesinin gereği sayılır"
        ]
    },
    "ticaret_hukuku/limited_sahis_sirketleri.json": {
        "0038|C": [
            "ek",
            "; ortakların yönetim yetkisi esas sözleşmeyle dahi kurulamaz"
        ],
        "0040|D": [
            "ek",
            "; alacaklılara karşı bir sorumluluğu da doğmaz"
        ],
        "0041|A": [
            "ek",
            "; komandite ortaklar aynı işi serbestçe yapabilir"
        ],
        "0044|C": [
            "ek",
            "; bu işlemler sınırlı sorumluluğunu etkilemez"
        ],
        "0047|A": [
            "ek",
            "; kollektif şirket ortağı koyduğu sermaye kadar sorumlu tutulur"
        ],
        "0048|B": [
            "ek",
            "; yönetici olmayan ortakların şirkete koydukları sermaye de korunur"
        ],
        "0049|D": [
            "ek",
            "; sermayenin iade edilmiş olması bu genişlemeyi engellemez"
        ],
        "0051|C": [
            "ek",
            "; bu nedenle esas sermaye payıyla sınırlı sorumluluk ilkesi ortadan kalkar"
        ]
    },
    "vergi_hukuku/vergi_denetimi_ceza_uyusmazlik.json": {
        "0008|A": [
            "ek",
            "; eksik ödeme hâlinde ise ayrıca bir ceza doğmaz"
        ],
        "0016|C": [
            "ek",
            "; idarenin re'sen düzeltme yetkisi bulunmaz"
        ],
        "0026|B": [
            "ek",
            "; idari nitelikte ayrı bir usulsüzlük cezası öngörülmemiştir"
        ],
        "0027|D": [
            "ek",
            "; vergi müfettişlerinin inceleme yetkisi bulunmaz"
        ],
        "0029|B": [
            "ek",
            "; vergi mahkemesi yalnızca esas hakkında karar verebilir"
        ],
        "0031|B": [
            "ek",
            "; vergi dairesine yapılan başvuru hiç sonuç doğurmaz"
        ],
        "0032|D": [
            "ek",
            "; mükellefin beyanname vermemiş olması ise ceza gerektirmez"
        ],
        "0034|E": [
            "ek",
            "; ayrıca bu belgeler indirim hakkı sağlamaya devam eder"
        ],
        "0039|D": [
            "ek",
            "; uzlaşma ise yargısal bir çözüm yolu sayılır"
        ],
        "0042|B": [
            "ek",
            "; inceleme sonuçları ayrı bir belgeye bağlanmaz"
        ],
        "0044|D": [
            "ek",
            "; vergi ziyaı ve usulsüzlük cezalarında artırım uygulanmaz"
        ],
        "0057|C": [
            "ek",
            "; yoklamada tutanak düzenlenmesi de aranmaz"
        ]
    },
    "vergi_hukuku/vergi_hukuku_temel_kavramlar.json": {
        "0007|A": [
            "ek",
            "; verginin ödenmesinden başka bir kişi sorumlu tutulamaz"
        ],
        "0035|E": [
            "ek",
            "; idare bu sözleşmeye dayanarak alacağını devralan kişiden ister"
        ],
        "0041|D": [
            "ek",
            "; kanuni temsilcilerin takibi yalnızca özel hukuk alacaklarında mümkündür"
        ],
        "0046|C": [
            "ek",
            "; bu nedenle vergi yalnızca bir kayıt aracı olarak görülür"
        ],
        "0048|D": [
            "ek",
            "; sürenin uzaması yalnızca mücbir sebep hâlinde gündeme gelir"
        ],
        "0049|C": [
            "ek",
            "; vergi hukukunda süreler hiçbir olayla durmaz"
        ],
        "0051|E": [
            "ek",
            "; merkezi idarenin bu konuda bir yetkisi bulunmaz"
        ],
        "0056|A": [
            "ek",
            "; tarh ve tahakkuk aşamaları arasında bir fark bulunmaz"
        ]
    },
    "vergi_hukuku/kurumlar_vergisi.json": {
        "0006|A": [
            "ek",
            "; ortaklık ayrıca beyanname vermekle yükümlü tutulmaz"
        ],
        "0018|C": [
            "ek",
            "; bu tutarlar kanunen kabul edilmeyen gider sayılır"
        ],
        "0035|B": [
            "ek",
            "; yurt içi iştiraklerden gelen kâr payları istisnadan yararlanamaz"
        ],
        "0036|A": [
            "ek",
            "; ortaklık ilişkisinin varlığı faiz indirimini etkilemez"
        ],
        "0048|A": [
            "ek",
            "; uygulamada ikisi arasında bir ayrım gözetilmez"
        ],
        "0049|A": [
            "ek",
            "; yurt dışı iştirak kazancı istisnası kanunda yer almaz"
        ],
        "0059|B": [
            "ek",
            "; indirim beyannamede ayrıca gösterilir ve matrahı düşürür"
        ],
        "0060|E": [
            "ek",
            "; kurumların aktifindeki taşınmaz satışı bu istisnadan yararlanamaz"
        ]
    },
    "ticaret_hukuku/kambiyo_senetleri.json": {
        "0004|A": [
            "ek",
            "; ibare yoksa senet yalnızca alacağın temlikiyle devredilir"
        ],
        "0005|E": [
            "ek",
            "; önceki cirantalara başvurma imkânı bulunmaz"
        ],
        "0011|B": [
            "ek",
            "; muhatabın adı senedin gerekli unsurlarından sayılmaz"
        ],
        "0013|A": [
            "ek",
            "; görüldüğünde ödeme kaydı taşıyan poliçe geçersizdir"
        ],
        "0015|C": [
            "ek",
            "; protesto düzenlenmesi bu hâlde gereksiz sayılır"
        ],
        "0016|E": [
            "ek",
            "; bu kayıt senedin geçerliliğini etkilemez"
        ],
        "0018|E": [
            "ek",
            "; düzenleyenin sonradan itiraz hakkı bulunmaz"
        ],
        "0023|A": [
            "ek",
            "; senedin türü metinden anlaşıldığı sürece geçerli sayılır"
        ],
        "0039|C": [
            "ek",
            "; kabul şerhi bulunmayan çek geçersiz sayılır"
        ],
        "0045|B": [
            "ek",
            "; iki ciro türü arasında başka bir fark bulunmaz"
        ],
        "0055|B": [
            "ek",
            "; (A)'ya başvurulması artık mümkün olmaz"
        ],
        "0059|E": [
            "ek",
            "; düzenleyene karşı takip hakkı ibrazla birlikte düşer"
        ]
    },
    "vergi_hukuku/gelir_vergisi.json": {
        "0015|B": [
            "ek",
            "; işletmenin borçları ve alacakları hesaba katılmaz"
        ],
        "0016|A": [
            "ek",
            "; bu ödeme ücret gideri sayılarak kazançtan indirilir"
        ],
        "0017|E": [
            "ek",
            "; amortisman tutarı doğrudan matrahtan düşülür"
        ],
        "0032|A": [
            "ek",
            "; ayrı bir gelir unsuru olarak sayılmaz"
        ],
        "0045|C": [
            "ek",
            "; yapılan tevkifat bu beyan yükümlülüğünü ortadan kaldırmaz"
        ]
    },
    "borclar_hukuku/sozlesme_turleri.json": {
        "0006|B": [
            "ek",
            "; mülkiyetin devri bu sözleşmede gündeme gelmez"
        ],
        "0013|A": [
            "ek",
            "; alıcının iyiniyetli olması bu sonucu etkilemez"
        ],
        "0019|B": [
            "ek",
            "; sözlü verilen bağışlama sözü de aynen ifa edilir"
        ],
        "0022|E": [
            "ek",
            "; bağışlayanın kusur derecesi dikkate alınmaz"
        ]
    },
    "ticaret_hukuku/haksiz_rekabet.json": {
        "0006|D": [
            "ek",
            "; bu davranış dürüstlük kuralına aykırı sayılır"
        ],
        "0010|A": [
            "ek",
            "; fiyatın maliyetin altında olması aranmaz"
        ],
        "0041|A": [
            "ek",
            "; müşteri çevresine yönelik davranışlar denetim dışıdır"
        ],
        "0042|C": [
            "ek",
            "; müşteriler ve meslek kuruluşları dava açamaz"
        ],
        "0043|A": [
            "ek",
            "; fikri ürünün ayrıca korunması gündeme gelmez"
        ],
        "0044|D": [
            "ek",
            "; hukuk davasında kazancın devri istenemez"
        ],
        "0045|A": [
            "ek",
            "; tescilsiz işaretler bu korumadan yararlanamaz"
        ],
        "0047|A": [
            "ek",
            "; bilginin doğruluğu değerlendirmede dikkate alınmaz"
        ],
        "0048|B": [
            "ek",
            "; haberi yayımlayan basın kuruluşu sorumlu tutulmaz"
        ]
    },
    "ticaret_hukuku/kiymetli_evrak.json": {
        "0017|D": [
            "ek",
            "; muhatap bankanın kabul yetkisi bulunmaz"
        ],
        "0025|A": [
            "ek",
            "; devir için ayrıca senedin teslimi aranmaz"
        ],
        "0027|A": [
            "ek",
            "; hamiline yazılı senetler de aynı yolla devredilir"
        ],
        "0028|E": [
            "ek",
            "; bu hak senette gösterilmese dahi doğar"
        ],
        "0034|B": [
            "ek",
            "; koşulun gerçekleşmemesi senedin geçerliliğini etkilemez"
        ],
        "0035|B": [
            "ek",
            "; düzenleyenin imzası senedin unsurlarından sayılmaz"
        ]
    }
}


def _dosyayi_isle(path, yamalar, write):
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    degisen, kullanilan = 0, set()
    for q in questions:
        secenekler = dict(q["options"])
        for L, v in secenekler.items():
            yeni, kurallar = temizle(v, True)
            if kurallar and not guvenli(v, yeni):
                secenekler[L] = yeni
        for L in list(secenekler):
            anahtar = f"{q['id'][-4:]}|{L}"
            if anahtar not in yamalar:
                continue
            if L == q["answer"]:
                raise SystemExit(f"Dogru sikka dokunulamaz: {path}::{q['id']}.{L}")
            tur, metin = yamalar[anahtar]
            kullanilan.add(anahtar)
            # Idempotans: ek daha once uygulandiysa yeniden eklenmez.
            if tur == "ek" and secenekler[L].endswith(metin):
                continue
            secenekler[L] = (secenekler[L] + metin) if tur == "ek" else metin
        if secenekler == q["options"]:
            continue
        if len(set(secenekler.values())) != 5:
            raise SystemExit(f"Secenek cakismasi: {path}::{q['id']}")
        if q["answer"] not in secenekler:
            raise SystemExit(f"Cevap secenekte yok: {path}::{q['id']}")
        degisen += sum(1 for L in secenekler if secenekler[L] != q["options"][L])
        if write:
            q["options"] = secenekler
    artan = set(yamalar) - kullanilan
    if artan:
        raise SystemExit(f"Kullanilmayan yama: {path} {sorted(artan)}")
    if write and degisen:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return degisen


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--write", action="store_true")
    args = ap.parse_args()

    kalan, toplam = [], 0
    for rel, yamalar in YAMALAR.items():
        for kok in (ROOT / "content", APP_ROOT / "content"):
            path = kok / rel
            n = _dosyayi_isle(path, yamalar, args.write)
            toplam += n
            if n and args.check:
                kalan.append(f"{path} ({n} sik islenmemis)")
    if args.check and kalan:
        print("Islenmemis dosyalar:")
        for k in kalan:
            print(f"- {k}")
        return 1
    yama = sum(len(v) for v in YAMALAR.values())
    if args.write:
        print(f"{len(YAMALAR)} paket / {toplam} sik islendi ({yama} elle denge yamasi).")
    else:
        print(f"{len(YAMALAR)} paket dogrulandi ({yama} elle denge yamasi).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
