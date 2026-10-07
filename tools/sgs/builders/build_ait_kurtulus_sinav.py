#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kurtuluş Savaşı ve Cepheler — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

46 sağlam soru korundu; 14 soru değişti. Gerçek sınavda payı %10 olan Osmanlı son dönemi (havuzda %2) eklendi: milliyetçilik ve ilk bağımsız millet, I. Meşrutiyet ve meclisin tatili, 31 Mart Vakası ve Hareket Ordusu, Trablusgarp (Uşi, Derne), II. Balkan Savaşı, I. Dünya Savaşı'na giriş, taarruz cepheleri, Çanakkale'nin sonuçları, Wilson İlkeleri. Tekâlif-i Milliye 'gönüllü bağış' diye yanlış tanıtılıyordu; zorunlu yükümlülük olarak düzeltildi. Yinelenen sorular (iki ayrı Amasya Genelgesi sorusu, ilkeler paketiyle çakışan Hatay) çıkarıldı; Sevr için olumsuz köklü soru eklendi.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: SGS Atatürk İlkeleri ve İnkılap Tarihi 2021-2026 kitapçıkları — biçim kalibrasyonu
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/ataturk_ilkeleri/kurtulus_savasi.json"
STYLE_REF = 'SGS Atatürk İlkeleri (gerçek sınav 16-20 profili)'
ONEK = "ait-kurtulus-gen-"


def patch(stem, options, answer, solution, ref='Atatürk İlkeleri ve İnkılap Tarihi'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "30 Ekim 1918'de imzalanan Mondros Ateşkes Antlaşması ile ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Osmanlı Devleti'nin I. Dünya Savaşı'ndan çekilmesini sağladı.",
            'B': "İtilaf Devletleri'ne Anadolu'da hiçbir yeri işgal etme hakkı tanımadı.",
            'C': '7. maddesi, güvenliği tehdit eden durumlarda stratejik noktaların işgaline olanak verdi.',
            'D': 'Osmanlı ordusunun terhis edilmesini öngördü.',
            'E': "Boğazların İtilaf Devletleri'nin gemilerine açılmasını öngördü.",
        },
        'B',
        "Mondros Ateşkes Antlaşması, özellikle 7. maddesiyle İtilaf Devletleri'ne güvenliklerini tehdit eden durumlarda istedikleri stratejik noktayı işgal etme hakkı tanıdı; bu nedenle Anadolu'nun işgaline zemin hazırladı. Diğer ifadeler antlaşmanın hükümleriyle örtüşür.",
    ),
    # düzey 2
    '0002': patch(
        "Fransız İhtilali'nin yaydığı milliyetçilik akımının etkisiyle Osmanlı Devleti'nden ilk olarak bağımsızlığını kazanan millet aşağıdakilerden hangisidir?",
        {
            'A': 'Yunanlılar',
            'B': 'Sırplar',
            'C': 'Arnavutlar',
            'D': 'Romenler',
            'E': 'Bulgarlar',
        },
        'A',
        "Milliyetçilik akımının etkisiyle ilk isyan eden Sırplar özerklik kazanmış, ilk bağımsız devleti ise 1830'da Yunanlılar kurmuştur.",
    ),
    # düzey 2
    '0003': patch(
        '"Milletin bağımsızlığını yine milletin azim ve kararı kurtaracaktır" ifadesi ilk kez aşağıdakilerin hangisinde yer almıştır?',
        {
            'A': 'Erzurum Kongresi',
            'B': 'Amasya Genelgesi',
            'C': 'Sivas Kongresi',
            'D': 'Misak-ı Millî',
            'E': 'Havza Genelgesi',
        },
        'B',
        '22 Haziran 1919 tarihli Amasya Genelgesi\'nde "Milletin bağımsızlığını yine milletin azim ve kararı kurtaracaktır" denilerek Kurtuluş Savaşı\'nın amacı ve gerekçesi ilk kez açıklanmıştır.',
    ),
    # düzey 3
    '0004': patch(
        "Yalnızca Doğu Anadolu'nun kurtuluşunu değil, bütün vatanın kurtuluşunu amaçlayan kararların alındığı, bölgesel toplanmasına karşın millî nitelikli kararlar veren kongre aşağıdakilerden hangisidir?",
        {
            'A': 'Edirne Kongresi',
            'B': 'Nazilli Kongresi',
            'C': 'Erzurum Kongresi',
            'D': 'Alaşehir Kongresi',
            'E': 'Balıkesir Kongresi',
        },
        'C',
        '23 Temmuz 1919\'da toplanan Erzurum Kongresi bölgesel amaçla toplanmış; ancak "Millî sınırlar içinde vatan bir bütündür, parçalanamaz" gibi kararlarıyla millî nitelik taşımıştır.',
    ),
    # düzey 3
    '0005': patch(
        'Ülke genelinden gelen delegelerin katıldığı ve dağınık millî cemiyetlerin "Anadolu ve Rumeli Müdafaa-i Hukuk Cemiyeti" adı altında birleştirildiği kongre aşağıdakilerden hangisidir?',
        {
            'A': 'İzmir Kongresi',
            'B': 'Konya Kongresi',
            'C': 'Sivas Kongresi',
            'D': 'Erzurum Kongresi',
            'E': 'Amasya Kongresi',
        },
        'C',
        "4-11 Eylül 1919'daki Sivas Kongresi'nde tüm yararlı cemiyetler tek çatı altında birleştirilmiştir. Bu kongre millî birliğin sağlanması yönünden önemlidir.",
    ),
    # düzey 2
    '0006': patch(
        "Millî sınırları ve tam bağımsızlığı belirleyen, son Osmanlı Mebusan Meclisi'nde kabul edilen belge aşağıdakilerden hangisidir?",
        {
            'A': 'Amasya Genelgesi',
            'B': 'Teşkilat-ı Esasiye',
            'C': 'Sevr Antlaşması',
            'D': 'Wilson İlkeleri',
            'E': 'Misak-ı Millî',
        },
        'E',
        "Son Osmanlı Mebusan Meclisi 28 Ocak 1920'de Misak-ı Millî (Millî Ant) kararlarını kabul etmiştir. Bu kararlar, ulusal sınırları ve bağımsızlık ilkesini belirlemiştir.",
    ),
    # düzey 2
    '0007': patch(
        "I. Meşrutiyet'in ilanıyla aşağıdakilerden hangisi gerçekleşmiştir?",
        {
            'A': 'Kanun-i Esasi adlı ilk anayasa yürürlüğe girmiştir.',
            'B': 'Halifelik makamı kaldırılmıştır.',
            'C': 'Çok partili siyasi hayata geçilmiştir.',
            'D': 'Saltanat kaldırılmıştır.',
            'E': 'Kapitülasyonlar kaldırılmıştır.',
        },
        'A',
        "1876'da ilan edilen I. Meşrutiyet ile Osmanlı Devleti'nin ilk anayasası Kanun-i Esasi yürürlüğe girmiş ve ilk kez meclis açılmıştır.",
    ),
    # düzey 2
    '0008': patch(
        "İtilaf Devletleri'nin Osmanlı Devleti'ne imzalattığı, ağır koşullar içeren ve TBMM'ce tanınmayan antlaşma aşağıdakilerden hangisidir?",
        {
            'A': 'Kars Antlaşması',
            'B': 'Moskova Antlaşması',
            'C': 'Lozan Antlaşması',
            'D': 'Sevr Antlaşması',
            'E': 'Mudanya Ateşkesi',
        },
        'D',
        "10 Ağustos 1920'de imzalanan Sevr Antlaşması, Osmanlı topraklarını paylaşan çok ağır bir antlaşmadır. TBMM bu antlaşmayı tanımamış, Kurtuluş Savaşı ile geçersiz kılmıştır.",
    ),
    # düzey 3
    '0009': patch(
        "Doğu Cephesi'nde Ermenilerle yapılan savaşlar sonunda imzalanan ve TBMM'nin uluslararası alandaki ilk siyasi başarısı sayılan antlaşma aşağıdakilerden hangisidir?",
        {
            'A': 'Ankara Antlaşması',
            'B': 'Sevr Antlaşması',
            'C': 'Mudanya Antlaşması',
            'D': 'Lozan Antlaşması',
            'E': 'Gümrü Antlaşması',
        },
        'E',
        "Doğu Cephesi'nde Kâzım Karabekir komutasındaki birlikler Ermenileri yenmiş; 3 Aralık 1920'de imzalanan Gümrü Antlaşması TBMM'nin ilk siyasi-askerî başarısı olmuştur.",
    ),
    # düzey 3
    '0010': patch(
        'Güney Cephesi\'nde Fransızlara ve işbirlikçilerine karşı direniş gösteren; kahramanlıkları nedeniyle sonradan "Kahraman", "Gazi", "Şanlı" unvanları verilen iller aşağıdakilerden hangisidir?',
        {
            'A': 'Bursa, Balıkesir, Çanakkale',
            'B': 'İzmir, Aydın, Manisa',
            'C': 'Edirne, Kırklareli, Tekirdağ',
            'D': 'Maraş, Antep, Urfa',
            'E': 'Kars, Ardahan, Artvin',
        },
        'D',
        "Güney Cephesi'nde Fransızlara karşı Maraş, Antep ve Urfa halkı düzenli ordu olmadan direnmiştir. Bu kahramanlıkları nedeniyle Kahramanmaraş, Gaziantep ve Şanlıurfa unvanlarını almışlardır.",
    ),
    # düzey 2
    '0011': patch(
        "Batı Cephesi'nde düzenli ordunun Yunanlılara karşı kazandığı ilk savaş aşağıdakilerden hangisidir?",
        {
            'A': 'Dumlupınar Muharebesi',
            'B': 'Çanakkale Savaşı',
            'C': 'Sakarya Meydan Muharebesi',
            'D': 'Büyük Taarruz',
            'E': 'I. İnönü Muharebesi',
        },
        'E',
        "10 Ocak 1921'de kazanılan I. İnönü Muharebesi, düzenli ordunun Batı Cephesi'ndeki ilk zaferidir. Bu zafer TBMM'ye ve düzenli orduya olan güveni artırmıştır.",
    ),
    # düzey 2
    '0012': patch(
        "TBMM'nin kabul ettiği ilk anayasa (Teşkilat-ı Esasiye Kanunu) I. İnönü zaferinin hemen ardından hangi yıl kabul edilmiştir?",
        {
            'A': '1919',
            'B': '1920',
            'C': '1921',
            'D': '1923',
            'E': '1924',
        },
        'C',
        '20 Ocak 1921\'de kabul edilen Teşkilat-ı Esasiye Kanunu, TBMM\'nin ilk anayasasıdır. "Egemenlik kayıtsız şartsız milletindir" ilkesini temel almıştır.',
    ),
    # düzey 3
    '0013': patch(
        'Sovyet Rusya ile TBMM arasında imzalanan, iki ülke ilişkilerini düzenleyen ve Doğu sınırını büyük ölçüde belirleyen antlaşma aşağıdakilerden hangisidir?',
        {
            'A': 'Moskova Antlaşması',
            'B': 'Sevr Antlaşması',
            'C': 'Londra Antlaşması',
            'D': 'Ankara Antlaşması',
            'E': 'Mudanya Antlaşması',
        },
        'A',
        "16 Mart 1921'de imzalanan Moskova Antlaşması ile Sovyet Rusya, TBMM hükûmetini ve Misak-ı Millî'yi tanımıştır. Bu, TBMM'nin batılı olmayan büyük bir devletle imzaladığı önemli bir antlaşmadır.",
    ),
    # düzey 2
    '0014': patch(
        'Mustafa Kemal\'in "Hattı müdafaa yoktur, sathı müdafaa vardır. O satıh bütün vatandır" emrini verdiği savaş aşağıdakilerden hangisidir?',
        {
            'A': 'Gümrü Savaşı',
            'B': 'Sakarya Meydan Muharebesi',
            'C': 'Çaldıran Savaşı',
            'D': 'II. İnönü Muharebesi',
            'E': 'I. İnönü Muharebesi',
        },
        'B',
        '23 Ağustos-13 Eylül 1921\'deki Sakarya Meydan Muharebesi\'nde Mustafa Kemal bu ünlü emri vermiştir. Zaferin ardından kendisine "Gazi" unvanı ve mareşal rütbesi verilmiştir.',
    ),
    # düzey 2
    '0015': patch(
        "Sakarya Meydan Muharebesi'nin kazanılmasının ardından Mustafa Kemal'e verilen unvan ve rütbe aşağıdakilerden hangisidir?",
        {
            'A': 'Sadrazam unvanı',
            'B': 'Halife unvanı',
            'C': 'Paşa unvanı ve albay rütbesi',
            'D': 'Gazi unvanı ve mareşal rütbesi',
            'E': 'Başkomutan unvanı ve general rütbesi',
        },
        'D',
        'Sakarya zaferinden sonra TBMM, Mustafa Kemal\'e "Gazi" unvanını ve mareşal (müşir) rütbesini vermiştir.',
    ),
    # düzey 3
    '0016': patch(
        "Fransa ile TBMM arasında imzalanan ve Güney Cephesi'ni kapatan, Fransızların Anadolu'dan çekilmesini sağlayan antlaşma aşağıdakilerden hangisidir?",
        {
            'A': 'Kars Antlaşması',
            'B': 'Moskova Antlaşması',
            'C': 'Gümrü Antlaşması',
            'D': 'Ankara Antlaşması',
            'E': 'Mudanya Antlaşması',
        },
        'D',
        "20 Ekim 1921'de imzalanan Ankara Antlaşması ile Fransa, TBMM'yi tanımış ve Güney Cephesi'nden çekilmiştir. Böylece bu cephedeki savaş sona ermiştir.",
    ),
    # düzey 2
    '0017': patch(
        "Kurtuluş Savaşı'nın son büyük taarruzu olan ve düşmanın Anadolu'dan atılmasını sağlayan zafer aşağıdakilerden hangisidir?",
        {
            'A': 'Türk ordusunun savunmada zafere ulaştığı Sakarya Meydan Muharebesi',
            'B': 'Düzenli ordunun ilk kez sınandığı I. İnönü Muharebesi',
            'C': 'Büyük Taarruz ve Başkomutanlık Meydan Muharebesi',
            'D': 'Eskişehir ve Kütahya çevresindeki savunma muharebeleri',
            'E': 'I. Dünya Savaşı yıllarında kazanılan Çanakkale Savaşı',
        },
        'C',
        "26 Ağustos 1922'de başlayan Büyük Taarruz, 30 Ağustos'ta Başkomutanlık Meydan Muharebesi ile zaferle sonuçlanmıştır. Bu, Yunan ordusunun kesin yenilgisidir.",
    ),
    # düzey 2
    '0018': patch(
        'I. Meşrutiyet dönemiyle ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "Kanun-i Esasi, Osmanlı Devleti'nin ilk anayasası olarak 1876'da ilan edildi.",
            'B': "Meclis-i Mebusan ve Ayan Meclisi'nden oluşan iki kanatlı bir meclis kuruldu.",
            'C': "II. Abdülhamit, 1877-1878 Osmanlı-Rus Savaşı'nı gerekçe göstererek meclisi tatil etti.",
            'D': 'Meclis-i Mebusan üyelerinin tamamı padişah tarafından atanıyordu.',
            'E': 'Anayasaya rağmen padişahın yetkileri geniş tutuldu.',
        },
        'D',
        "I. Meşrutiyet'te Ayan Meclisi üyeleri padişah tarafından atanır, Meclis-i Mebusan üyeleri ise seçimle belirlenirdi. Kanun-i Esasi 1876'da ilan edilmiş, II. Abdülhamit 93 Harbi'ni gerekçe göstererek meclisi tatil etmiştir; padişahın yetkileri geniş tutulmuştur.",
    ),
    # düzey 3
    '0019': patch(
        "Kurtuluş Savaşı'nın askerî bölümünü sona erdiren ve İstanbul, Boğazlar ile Doğu Trakya'nın savaşılmadan geri alınmasını sağlayan ateşkes aşağıdakilerden hangisidir?",
        {
            'A': 'Mudanya Ateşkes Antlaşması',
            'B': 'Gümrü Antlaşması',
            'C': 'Ankara Antlaşması',
            'D': 'Mondros Ateşkes Antlaşması',
            'E': 'Moskova Antlaşması',
        },
        'A',
        "11 Ekim 1922'de imzalanan Mudanya Ateşkesi ile savaş fiilen bitmiş; İstanbul, Boğazlar ve Doğu Trakya savaşılmadan TBMM'ye bırakılmıştır.",
    ),
    # düzey 2
    '0020': patch(
        "Yeni Türk Devleti'nin bağımsızlığını dünyaya kabul ettiren ve bir barış antlaşması olan belge aşağıdakilerden hangisidir?",
        {
            'A': 'Lozan Barış Antlaşması',
            'B': 'Moskova Antlaşması',
            'C': 'Sevr Antlaşması',
            'D': 'Mondros Ateşkesi',
            'E': 'Londra Konferansı',
        },
        'A',
        "24 Temmuz 1923'te imzalanan Lozan Barış Antlaşması, yeni Türk Devleti'nin bağımsızlığını uluslararası alanda tanıtan barış antlaşmasıdır.",
    ),
    # düzey 3
    '0021': patch(
        "Mustafa Kemal'in 19 Mayıs 1919'da Samsun'a çıkmasından sonraki gelişmelerle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Havza'da halkı mitinglerle işgallere karşı tepki göstermeye çağırdı.",
            'B': "Samsun'dan doğrudan Ankara'ya geçerek aynı ay içinde TBMM'yi açtı.",
            'C': "Amasya'da yayımlanan genelgeyle Sivas'ta bir kongre toplanacağını duyurdu.",
            'D': "Erzurum Kongresi'ne katılabilmek için askerlik görevinden istifa etti.",
            'E': "Sivas Kongresi'nde Temsil Heyeti'nin başkanlığına seçildi.",
        },
        'B',
        "Mustafa Kemal Samsun'dan sonra Havza ve Amasya'ya geçmiş, Erzurum ve Sivas kongrelerine katılmış, Ankara'ya ancak Aralık 1919'da gelmiştir. TBMM 23 Nisan 1920'de açılmıştır.",
    ),
    # düzey 2
    '0022': patch(
        "31 Mart Vakası'nı bastırmak için Selanik'ten İstanbul'a gelen Hareket Ordusu'nun kurmay başkanı aşağıdakilerden hangisidir?",
        {
            'A': 'Enver Bey',
            'B': 'Kâzım Karabekir',
            'C': 'Mustafa Kemal',
            'D': 'Ali Fuat Paşa',
            'E': 'Cemal Paşa',
        },
        'C',
        "Mahmut Şevket Paşa komutasındaki Hareket Ordusu'nun kurmay başkanı Mustafa Kemal'dir.",
    ),
    # düzey 2
    '0023': patch(
        "Kurtuluş Savaşı'nda Doğu Cephesi komutanı aşağıdakilerden hangisidir?",
        {
            'A': 'Fevzi Çakmak',
            'B': 'İsmet İnönü',
            'C': 'Kâzım Karabekir',
            'D': 'Ali Fuat Cebesoy',
            'E': 'Refet Bele',
        },
        'C',
        "Doğu Cephesi komutanı Kâzım Karabekir Paşa'dır. Ermenilere karşı kazanılan zaferler ve Gümrü Antlaşması onun komutasında gerçekleşmiştir.",
    ),
    # düzey 2
    '0024': patch(
        'I. ve II. İnönü Muharebelerinde Batı Cephesi komutanı olan ve daha sonra cumhurbaşkanı olan kişi aşağıdakilerden hangisidir?',
        {
            'A': 'İsmet (İnönü) Paşa',
            'B': 'Kâzım Karabekir',
            'C': 'Fevzi Çakmak',
            'D': 'Celal Bayar',
            'E': 'Rauf Orbay',
        },
        'A',
        'Batı Cephesi komutanı İsmet Paşa\'dır. İnönü Muharebelerindeki başarıları nedeniyle sonradan "İnönü" soyadını almıştır.',
    ),
    # düzey 2
    '0025': patch(
        "Kurtuluş Savaşı'nda düzenli ordu kurulmadan önce bölgesel direnişi yürüten silahlı halk güçlerine ne ad verilir?",
        {
            'A': 'Yeniçeri Ocağı',
            'B': 'Kuva-yi İnzibatiye',
            'C': 'Kuva-yi Milliye',
            'D': 'Hilafet Ordusu',
            'E': 'Redd-i İlhak',
        },
        'C',
        'Düzenli ordu kurulmadan önce işgallere karşı halkın oluşturduğu silahlı direniş birliklerine Kuva-yi Milliye denir. Düzenli ordunun kurulmasıyla önemini yitirmiştir.',
    ),
    # düzey 2
    '0026': patch(
        'Amasya Genelgesi\'nde yer alan "Sivas\'ta millî bir kongre toplanması" kararının amacı aşağıdakilerden hangisidir?',
        {
            'A': 'Manda ve himayeyi benimsemek',
            'B': 'Saltanatı güçlendirmek',
            'C': 'Padişahın yetkilerini artırmak',
            'D': 'Ulusal direnişi tek merkezden yönetmek',
            'E': 'İşgalleri resmen kabul etmek',
        },
        'D',
        "Amasya Genelgesi, dağınık direnişi birleştirmek ve millî iradeyi tek merkezde toplamak için Sivas'ta bir kongre toplanmasını öngörmüştür. Amaç, ulusal direnişi ortak bir yönetime kavuşturmaktır.",
    ),
    # düzey 2
    '0027': patch(
        "Sivas Kongresi'nde kesin olarak reddedilen, bir devletin koruyuculuğunu kabul etme anlamına gelen görüş aşağıdakilerden hangisidir?",
        {
            'A': 'Millî egemenlik',
            'B': 'Tam bağımsızlık',
            'C': 'Cumhuriyet',
            'D': 'Misak-ı Millî',
            'E': 'Manda ve himaye',
        },
        'E',
        "Sivas Kongresi'nde bir devletin (özellikle ABD'nin) koruyuculuğunu kabul etme anlamındaki manda ve himaye fikri tartışılmış ve kesin olarak reddedilmiştir. Tam bağımsızlık ilkesi benimsenmiştir.",
    ),
    # düzey 2
    '0028': patch(
        "Aşağıdakilerden hangisi 31 Mart Vakası'nın sonuçlarından biridir?",
        {
            'A': "Osmanlı Devleti'nin I. Dünya Savaşı'na girmesi",
            'B': "I. Meşrutiyet'in ilan edilmesi",
            'C': "II. Abdülhamit'in tahttan indirilmesi",
            'D': "Kanun-i Esasi'nin ilk kez kabul edilmesi",
            'E': "Trablusgarp'ın İtalya'ya bırakılması",
        },
        'C',
        "1909'daki 31 Mart Vakası Hareket Ordusu'nca bastırılmış ve II. Abdülhamit tahttan indirilmiştir. I. Meşrutiyet ve Kanun-i Esasi 1876 tarihlidir.",
    ),
    # düzey 2
    '0029': patch(
        "Türk ordusunun Sakarya'ya kadar çekilmesine yol açan, Yunanlıların ilerlediği muharebeler aşağıdakilerden hangisidir?",
        {
            'A': 'Birinci İnönü Meydan Muharebesi (Ocak 1921)',
            'B': 'Kütahya-Eskişehir Muharebeleri',
            'C': 'II. İnönü Muharebesi',
            'D': 'Gümrü Muharebesi',
            'E': 'Büyük Taarruz',
        },
        'B',
        "Temmuz 1921'deki Kütahya-Eskişehir Muharebelerinde Yunan ordusu ilerlemiş, Türk ordusu Sakarya Nehri'nin doğusuna çekilmek zorunda kalmıştır.",
    ),
    # düzey 2
    '0030': patch(
        "TBMM'nin açılışından kısa süre sonra, Meclis'e karşı yapılan eylemleri vatana ihanet sayarak iç ayaklanmalara karşı otoritesini korumak amacıyla çıkarılan kanun aşağıdakilerden hangisidir?",
        {
            'A': 'Takrir-i Sükûn Kanunu',
            'B': 'Teşkilat-ı Esasiye Kanunu',
            'C': 'Hıyanet-i Vataniye Kanunu',
            'D': 'Tevhid-i Tedrisat Kanunu',
            'E': 'Kabotaj Kanunu',
        },
        'C',
        "TBMM, kendisine karşı çıkan ayaklanmalar karşısında 29 Nisan 1920'de Hıyanet-i Vataniye Kanunu'nu çıkarmış ve Meclis'in meşruiyetine karşı yapılan eylemleri vatana ihanet saymıştır. İstiklal Mahkemeleri ise Eylül 1920'de, asker kaçaklarına ilişkin ayrı bir kanunla kurulmuştur. Takrir-i Sükûn Kanunu 1925, Tevhid-i Tedrisat ve Teşkilat-ı Esasiye ise farklı amaçlı düzenlemelerdir.",
    ),
    # düzey 2
    '0031': patch(
        '1911-1912 Trablusgarp Savaşı ile ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "İtalya'nın Osmanlı Devleti'nin Kuzey Afrika'daki son toprağına saldırmasıyla başladı.",
            'B': 'Osmanlı Devleti bölgeye kara yoluyla yeterli asker gönderemedi.',
            'C': "Savaş, Osmanlı Devleti'nin bölgeyi geri almasıyla sona erdi.",
            'D': 'Mustafa Kemal gibi gönüllü subaylar bölgede yerel halkı örgütledi.',
            'E': "Savaş sırasında İtalya, On İki Ada'yı işgal etti.",
        },
        'C',
        "Savaş, Balkan Savaşları'nın başlaması üzerine imzalanan Uşi Antlaşması ile sona ermiş ve Trablusgarp İtalya'ya bırakılmıştır. Diğer ifadeler doğrudur.",
    ),
    # düzey 3
    '0032': patch(
        "Ermenistan ve Gürcistan ile imzalanan antlaşmalarla kesinleşen; bugünkü Türkiye'nin doğu sınırını belirleyen antlaşma aşağıdakilerden hangisidir?",
        {
            'A': 'Lozan Antlaşması',
            'B': 'Sevr Antlaşması',
            'C': 'Ankara Antlaşması',
            'D': 'Mudanya Antlaşması',
            'E': 'Kars Antlaşması',
        },
        'E',
        "13 Ekim 1921'de imzalanan Kars Antlaşması ile Doğu sınırı kesin biçimde belirlenmiştir. Bu antlaşma bugünkü Türkiye-Ermenistan/Gürcistan sınırının temelini oluşturur.",
    ),
    # düzey 2
    '0033': patch(
        'Mustafa Kemal\'e ordunun başına geçme ve TBMM\'nin yetkilerini kullanma imkânı veren "Başkomutanlık Kanunu" hangi savaştan hemen önce çıkarılmıştır?',
        {
            'A': 'Dumlupınar Muharebesi',
            'B': 'Gümrü Muharebesi',
            'C': 'I. İnönü Muharebesi',
            'D': 'Sakarya Meydan Muharebesi',
            'E': 'Çanakkale Savaşı',
        },
        'D',
        "Kütahya-Eskişehir yenilgisinin ardından, 5 Ağustos 1921'de çıkarılan Başkomutanlık Kanunu ile Mustafa Kemal ordunun başına geçmiştir. Bu, Sakarya Meydan Muharebesi'nden hemen öncedir.",
    ),
    # düzey 2
    '0034': patch(
        "Sivas Kongresi'nde alınan kararlar doğrultusunda temsil yetkisini elinde bulunduran kurul aşağıdakilerden hangisidir?",
        {
            'A': 'Heyet-i Vükela',
            'B': 'Meclis-i Mebusan',
            'C': 'Divan-ı Hümayun',
            'D': 'Ayan Meclisi',
            'E': 'Temsil Heyeti',
        },
        'E',
        "Sivas Kongresi'nde oluşturulan Temsil Heyeti, ulusal iradeyi temsil etmiş ve TBMM açılana kadar bir tür yürütme görevi görmüştür. Başkanı Mustafa Kemal'dir.",
    ),
    # düzey 2
    '0035': patch(
        "Mustafa Kemal'in Kurtuluş Savaşı öncesinde görev yaptığı yerlerle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Çanakkale Savaşı'nda Anafartalar'da önemli bir başarı kazandı.",
            'B': "Balkan Savaşları sırasında Kanal Cephesi'nde Süveyş'e saldırı düzenledi.",
            'C': "I. Dünya Savaşı'nda Kafkas Cephesi'nde Muş ve Bitlis'i geri aldı.",
            'D': "Trablusgarp Savaşı'nda Tobruk ve Derne'de görev yaptı.",
            'E': "Suriye-Filistin Cephesi'nde Yıldırım Orduları Grubu'na bağlı bir orduya komuta etti.",
        },
        'B',
        "Kanal Cephesi I. Dünya Savaşı'nda açılmıştır ve Mustafa Kemal bu cephede görev almamıştır. Anafartalar, Muş ve Bitlis, Tobruk ve Derne ile Suriye-Filistin Cephesi'ndeki görevleri doğrudur.",
    ),
    # düzey 2
    '0036': patch(
        'Balkan Savaşları ile ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': "I. Balkan Savaşı'nda Osmanlı Devleti Rumeli'deki topraklarının büyük bölümünü kaybetti.",
            'B': 'II. Balkan Savaşı, Balkan devletleri arasındaki toprak paylaşımı anlaşmazlığından çıktı.',
            'C': "Osmanlı Devleti II. Balkan Savaşı'nda Selanik'i geri aldı.",
            'D': "Osmanlı Devleti II. Balkan Savaşı sırasında Edirne'yi geri aldı.",
            'E': 'Balkan Savaşları sürecinde Arnavutluk bağımsızlığını kazandı.',
        },
        'C',
        "Osmanlı Devleti II. Balkan Savaşı'nda yalnızca Edirne ve Kırklareli'yi geri alabilmiştir; Selanik Yunanistan'da kalmıştır. Diğer ifadeler doğrudur.",
    ),
    # düzey 3
    '0037': patch(
        "Osmanlı Devleti'nin I. Dünya Savaşı'na girmesine yol açan olay aşağıdakilerden hangisidir?",
        {
            'A': "Sarıkamış Harekâtı'nın başlatılması",
            'B': "Kut'ül Amare kuşatmasının başlaması",
            'C': "Mondros Ateşkesi'nin imzalanması",
            'D': 'Yavuz ve Midilli gemilerinin Rus limanlarını bombalaması',
            'E': "Çanakkale Boğazı'nın İtilaf donanmasınca zorlanması",
        },
        'D',
        "Ekim 1914'te Yavuz ve Midilli gemilerinin Karadeniz'deki Rus limanlarını bombalaması Osmanlı Devleti'ni savaşa sokmuştur. Diğer olaylar savaşa girildikten sonradır.",
    ),
    # düzey 3
    '0038': patch(
        'Mondros Ateşkesi\'nin hangi maddesi, İtilaf Devletleri\'ne "güvenliklerini tehdit eden bir durumda herhangi bir stratejik noktayı işgal etme" hakkı tanıyarak işgallerin dayanağı olmuştur?',
        {
            'A': '7. madde',
            'B': '5. madde',
            'C': '1. madde',
            'D': '11. madde',
            'E': '24. madde',
        },
        'A',
        "Mondros Ateşkesi'nin 7. maddesi, İtilaf Devletleri'ne güvenliklerini tehdit gördükleri her yeri işgal etme hakkı tanımıştır. Bu madde, işgallerin hukuki gerekçesi olarak kullanılmıştır.",
    ),
    # düzey 2
    '0039': patch(
        "Osmanlı Devleti'nin I. Dünya Savaşı'nda savaştığı cephelerle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Kafkas Cephesi'nde Sarıkamış Harekâtı ağır kayıplarla sonuçlandı.",
            'B': 'Kanal Cephesi, İngilizlerin Hindistan ile bağlantısını kesmek amacıyla açıldı.',
            'C': "Çanakkale Cephesi, Osmanlı Devleti'nin taarruz amacıyla açtığı bir cepheydi.",
            'D': "Irak Cephesi'nde Kut'ül Amare'de bir İngiliz birliği teslim alındı.",
            'E': "Çanakkale'deki başarı, savaşın uzamasında etkili oldu.",
        },
        'C',
        "Çanakkale Cephesi, İtilaf Devletleri'nin Boğazları geçme girişimine karşı açılmış bir savunma cephesidir. Kafkas ve Kanal cepheleri taarruz amaçlıdır; diğer ifadeler doğrudur.",
    ),
    # düzey 2
    '0040': patch(
        "Erzurum Kongresi'nin toplanmasında öncülük eden ve Doğu illerini temsil eden cemiyet aşağıdakilerden hangisidir?",
        {
            'A': 'Trakya-Paşaeli Cemiyeti',
            'B': 'Mavri Mira Cemiyeti',
            'C': 'İzmir Müdafaa-i Hukuk Cemiyeti',
            'D': 'Doğu Anadolu Müdafaa-i Hukuk Cemiyeti',
            'E': 'Kilikyalılar Cemiyeti',
        },
        'D',
        "Erzurum Kongresi, Doğu Anadolu Müdafaa-i Hukuk Cemiyeti'nin öncülüğünde toplanmıştır. Amaç, Doğu illerinin Ermenilere verilmesini önlemekti.",
    ),
    # düzey 2
    '0041': patch(
        "Yunan ordusunun İzmir'e çıkmasına tepki olarak kurulan ve işgale karşı direnişi örgütleyen cemiyetlerden biri aşağıdakilerden hangisidir?",
        {
            'A': 'Taşnak Cemiyeti',
            'B': 'Etnik-i Eterya Cemiyeti',
            'C': 'Pontus Rum Cemiyeti',
            'D': 'Redd-i İlhak Cemiyeti',
            'E': 'Mavri Mira Cemiyeti',
        },
        'D',
        "Redd-i İlhak Cemiyeti, İzmir'in Yunanlılarca işgaline karşı kurulan yararlı bir cemiyettir. Diğer seçeneklerdeki cemiyetler azınlıkların kurduğu zararlı cemiyetlerdir.",
    ),
    # düzey 2
    '0042': patch(
        "Aşağıdakilerden hangisi azınlıkların kurduğu, Osmanlı'yı parçalamayı amaçlayan zararlı cemiyetlerden biridir?",
        {
            'A': 'Doğu Anadolu Müdafaa-i Hukuk Cemiyeti',
            'B': 'Redd-i İlhak Cemiyeti',
            'C': 'Trakya-Paşaeli Cemiyeti',
            'D': 'Kilikyalılar Cemiyeti',
            'E': 'Mavri Mira Cemiyeti',
        },
        'E',
        "Rumların kurduğu Mavri Mira Cemiyeti, Batı Anadolu ve Trakya'yı Yunanistan'a katmayı amaçlamıştır; bu yönüyle zararlı bir cemiyettir. Diğer seçenekler yararlı (millî) cemiyetlerdir.",
    ),
    # düzey 3
    '0043': patch(
        'Mustafa Kemal\'in Temmuz 1919\'da askerlik görevinden istifa ederek mücadeleye sivil olarak devam edeceğini açıklamasının ardından katıldığı ve başkanlığına seçildiği ilk kongre aşağıdakilerden hangisidir?',
        {
            'A': 'Amasya görüşmeleri',
            'B': 'Erzurum Kongresi',
            'C': 'Lozan Konferansı',
            'D': 'Sivas Kongresi',
            'E': 'Balıkesir Kongresi',
        },
        'B',
        'Mustafa Kemal, 8-9 Temmuz 1919 gecesi Erzurum\'da askerlik görevinden istifa etmiş ve mücadeleye sivil olarak devam edeceğini açıklamıştır. İstifa, 23 Temmuz\'da toplanan Erzurum Kongresi\'ne katılıp başkanlığına seçilmesinin önünü açmıştır.',
    ),
    # düzey 2
    '0044': patch(
        "TBMM'nin açılmasından sonra çıkan iç ayaklanmaları yargılamak ve düzeni sağlamak için kurulan mahkemeler aşağıdakilerden hangisidir?",
        {
            'A': 'İstiklal Mahkemeleri',
            'B': 'Şûra-yı Devlet',
            'C': 'Divan-ı Harp',
            'D': 'Temyiz Mahkemesi',
            'E': 'Nizamiye Mahkemeleri',
        },
        'A',
        "TBMM, iç isyanları bastırmak ve asker kaçaklarını yargılamak için İstiklal Mahkemeleri'ni kurmuştur. Bu mahkemeler, Millî Mücadele döneminde düzenin sağlanmasında etkili olmuştur.",
    ),
    # düzey 2
    '0045': patch(
        "Sevr Antlaşması'nın TBMM tarafından tanınmamasının temel gerekçesi aşağıdakilerden hangisidir?",
        {
            'A': 'Doğu Anadolu illerinin bölünmeden Türkiye sınırları içinde bırakılması',
            'B': 'Yabancılara tanınan kapitülasyonların kaldırılıp ekonomik bağımsızlığın sağlanması',
            'C': "İzmir ve çevresindeki toprakların Osmanlı Devleti'ne bırakılması",
            'D': 'Türk milletinin bağımsızlığını ve toprak bütünlüğünü ortadan kaldırması',
            'E': 'Boğazların hiçbir kısıtlama olmadan tümüyle Türk egemenliğine bırakılması',
        },
        'D',
        'Sevr, Osmanlı topraklarını paylaşarak Türk milletine bağımsız yaşama hakkı tanımayan çok ağır bir antlaşmadır. Bu nedenle millî iradeyi temsil eden TBMM onu tanımamıştır.',
    ),
    # düzey 3
    '0046': patch(
        'Sevr Antlaşması ile ilgili aşağıdakilerden hangisi söylenemez?',
        {
            'A': 'Kapitülasyonların genişletilmesini öngörmüştür.',
            'B': "Osmanlı Mebusan Meclisi'nce onaylanmamıştır.",
            'C': "10 Ağustos 1920'de imzalanmıştır.",
            'D': 'TBMM tarafından onaylanarak yürürlüğe girmiştir.',
            'E': 'Boğazların uluslararası bir komisyona bırakılmasını öngörmüştür.',
        },
        'D',
        'Sevr, TBMM tarafından tanınmamış ve hiçbir zaman yürürlüğe girmemiştir. Mebusan Meclisi kapatıldığı için onaylanmamıştır.',
    ),
    # düzey 2
    '0047': patch(
        "9 Eylül 1922'de Türk ordusunun girmesiyle kurtarılan ve Kurtuluş Savaşı'nın simgelerinden biri olan kent aşağıdakilerden hangisidir?",
        {
            'A': 'Erzurum',
            'B': 'İzmir',
            'C': 'Konya',
            'D': 'Ankara',
            'E': 'Bursa',
        },
        'B',
        "Büyük Taarruz'un ardından 9 Eylül 1922'de İzmir'e girilmesiyle Batı Anadolu'nun işgali sona ermiştir. İzmir'in kurtuluşu, savaşın simgelerinden biridir.",
    ),
    # düzey 2
    '0048': patch(
        "Lozan Antlaşması'nda Türkiye lehine kaldırılan ve Osmanlı ekonomisini yabancılara bağımlı kılan ayrıcalıklar aşağıdakilerden hangisidir?",
        {
            'A': 'Kapitülasyonlar',
            'B': 'Aşar vergisi',
            'C': 'Duyun-u Umumiye',
            'D': 'Reji İdaresi',
            'E': 'Tımar sistemi',
        },
        'A',
        'Yabancılara tanınan ekonomik ve hukuki ayrıcalıklar olan kapitülasyonlar, Lozan Antlaşması ile kaldırılmıştır. Bu, ekonomik bağımsızlık yönünden önemli bir kazanımdır.',
    ),
    # düzey 3
    '0049': patch(
        "Sakarya Meydan Muharebesi öncesinde ordunun ihtiyaçlarını karşılamak için Başkomutan Mustafa Kemal'in yayımladığı ve halktan belirli oranlarda mal, araç ve gereç istenmesini öngören emirler aşağıdakilerden hangisidir?",
        {
            'A': 'Teşkilat-ı Esasiye Kanunu',
            'B': 'Hıyanet-i Vataniye Kanunu',
            'C': 'Başkomutanlık Kanunu',
            'D': 'Takrir-i Sükûn Kanunu',
            'E': 'Tekâlif-i Milliye Emirleri',
        },
        'E',
        "Ağustos 1921'de yayımlanan Tekâlif-i Milliye Emirleri ile halktan elindeki giyecek, yiyecek, hayvan ve araçların belirli oranları ordu için istenmiştir; bunlar gönüllü bağış değil, zorunlu yükümlülüklerdir.",
    ),
    # düzey 2
    '0050': patch(
        'Erzurum ve Sivas kongrelerinde alınan kararların ortak noktası aşağıdakilerden hangisidir?',
        {
            'A': 'Devletin yönetim biçimi olarak cumhuriyetin ilan edilmesi',
            'B': 'Millî sınırlar içinde vatanın bir bütün olduğu ve bölünemeyeceği',
            'C': 'Halifelik kurumunun kaldırılıp yetkilerinin meclise verilmesi',
            'D': 'Osmanlı saltanatının hemen kaldırılıp yönetim biçiminin değiştirilmesi',
            'E': 'Bir büyük devletin manda ve himayesinin mutlaka kabul edilmesi gerektiği',
        },
        'B',
        'Her iki kongrede de "Millî sınırlar içinde vatan bir bütündür, parçalanamaz" ilkesi vurgulanmıştır. Vatanın bütünlüğü ve bağımsızlık her iki kongrenin ortak kararıdır.',
    ),
    # düzey 2
    '0051': patch(
        "Lozan Konferansı'nda Türk heyetine başkanlık eden devlet adamı aşağıdakilerden hangisidir?",
        {
            'A': 'İsmet İnönü',
            'B': 'Fevzi Çakmak',
            'C': 'Rauf Orbay',
            'D': 'Kâzım Karabekir',
            'E': 'Mustafa Kemal',
        },
        'A',
        "Lozan Konferansı'nda Türk heyetine, dönemin Dışişleri Bakanı İsmet (İnönü) Paşa başkanlık etmiştir.",
    ),
    # düzey 3
    '0052': patch(
        "Lozan Antlaşması'nda çözümlenerek nüfus esasına göre gerçekleştirilen ve Türkiye ile Yunanistan arasında yapılan uygulama aşağıdakilerden hangisidir?",
        {
            'A': 'Doğu sınırının belirlenmesi',
            'B': 'Nüfus (ahali) mübadelesi',
            'C': 'Boğazların kapatılması',
            'D': "Musul'un Türkiye'ye verilmesi",
            'E': 'Kapitülasyonların sürdürülmesi',
        },
        'B',
        "Lozan'da Türkiye ile Yunanistan arasında bir nüfus (ahali) mübadelesi kararlaştırılmıştır. Belirli istisnalar dışında Türkiye'deki Rumlarla Yunanistan'daki Türkler karşılıklı yer değiştirmiştir.",
    ),
    # düzey 2
    '0053': patch(
        "Batı Cephesi'nde 1921-1922 yılları arasındaki savaşların genel sıralaması aşağıdakilerden hangisidir?",
        {
            'A': 'Sakarya → I. İnönü → Büyük Taarruz → II. İnönü',
            'B': 'I. İnönü → II. İnönü → Sakarya → Büyük Taarruz',
            'C': 'Büyük Taarruz → Sakarya → II. İnönü → I. İnönü',
            'D': 'Sakarya → Büyük Taarruz → I. İnönü → II. İnönü',
            'E': 'II. İnönü → I. İnönü → Büyük Taarruz → Sakarya',
        },
        'B',
        'Batı Cephesi savaşları sırasıyla I. İnönü (Ocak 1921), II. İnönü (Mart-Nisan 1921), Sakarya (Ağustos-Eylül 1921) ve Büyük Taarruz (Ağustos 1922) biçiminde gerçekleşmiştir.',
    ),
    # düzey 3
    '0054': patch(
        "Aşağıdakilerden hangisi Çanakkale Savaşları'nın sonuçlarından biri değildir?",
        {
            'A': "Mustafa Kemal'in askerî başarısıyla tanınması",
            'B': "Rusya'ya deniz yoluyla yardım ulaştırılamaması",
            'C': "I. Dünya Savaşı'nın uzaması",
            'D': "Bulgaristan'ın İttifak Devletleri safında savaşa katılması",
            'E': "Osmanlı Devleti'nin I. Dünya Savaşı'ndan galip çıkması",
        },
        'E',
        "Çanakkale'de kazanılan başarı Rusya'ya yardımı engellemiş, savaşı uzatmış, Mustafa Kemal'i tanıtmış ve Bulgaristan'ın İttifak Devletleri'ne katılmasında etkili olmuştur. Osmanlı Devleti savaştan yenik çıkmıştır.",
    ),
    # düzey 2
    '0055': patch(
        "Wilson İlkeleri'nin Osmanlı Devleti'ni ilgilendiren maddesinde aşağıdakilerden hangisi öngörülmüştür?",
        {
            'A': 'Kapitülasyonların genişletilmesi',
            'B': 'Türklerin çoğunlukta olduğu bölgelerde Türk egemenliğinin tanınması',
            'C': 'Osmanlı topraklarının tamamının manda yönetimine bırakılması',
            'D': "Boğazların Rusya'ya bırakılması",
            'E': "İstanbul'un uluslararası yönetime verilmesi",
        },
        'B',
        "Wilson İlkeleri'nin 12. maddesi, Türklerin çoğunlukta olduğu yerlerde Türk egemenliğinin tanınmasını ve Boğazlardan serbest geçişi öngörür.",
    ),
    # düzey 2
    '0056': patch(
        '"Egemenlik kayıtsız şartsız milletindir" ilkesini benimseyerek millî egemenliği hukuki temele oturtan ilk belge aşağıdakilerden hangisidir?',
        {
            'A': '1921 Teşkilat-ı Esasiye Kanunu',
            'B': 'Gümrü Antlaşması',
            'C': '1920 Sevr (paylaşım) Antlaşması',
            'D': 'Amasya Genelgesi',
            'E': 'Mondros Ateşkesi',
        },
        'A',
        '1921 Teşkilat-ı Esasiye Kanunu (ilk anayasa), "Egemenlik kayıtsız şartsız milletindir" ilkesini benimseyerek millî egemenliği hukuki güvenceye almıştır.',
    ),
    # düzey 2
    '0057': patch(
        "Sivas Kongresi'nde çıkarılmasına karar verilen ve millî mücadelenin sesini duyuran gazete aşağıdakilerden hangisidir?",
        {
            'A': 'Servet-i Fünun',
            'B': 'Takvim-i Vekayi',
            'C': 'Tercüman-ı Ahval',
            'D': 'Ceride-i Havadis',
            'E': 'İrade-i Milliye',
        },
        'E',
        "Sivas Kongresi'nde, millî mücadelenin görüşlerini yaymak amacıyla İrade-i Milliye gazetesinin çıkarılmasına karar verilmiştir.",
    ),
    # düzey 3
    '0058': patch(
        "İstanbul'un İtilaf Devletleri tarafından resmen işgal edilmesi ve Mebusan Meclisi'nin dağıtılması, aşağıdaki gelişmelerden hangisinin doğrudan nedeni olmuştur?",
        {
            'A': "Ankara'da TBMM'nin açılması",
            'B': "Sivas Kongresi'nin toplanması",
            'C': "Sevr'in imzalanması",
            'D': "Mondros'un imzalanması",
            'E': "Erzurum Kongresi'nin toplanması",
        },
        'A',
        "16 Mart 1920'de İstanbul'un resmen işgali ve Mebusan Meclisi'nin dağıtılması üzerine, millî iradeyi temsil edecek yeni bir meclis olarak 23 Nisan 1920'de Ankara'da TBMM açılmıştır.",
    ),
    # düzey 2
    '0059': patch(
        "Kurtuluş Savaşı'nda düzenli orduya geçişle ilgili aşağıdakilerden hangisi yanlıştır?",
        {
            'A': "Kuva-yi Milliye'nin disiplin ve koordinasyon eksiklikleri bu kararda etkili oldu.",
            'B': 'Çerkez Ethem gibi bazı Kuva-yi Milliye liderleri düzenli orduya katılmayı reddetti.',
            'C': "Düzenli ordunun kurulması TBMM'nin otoritesini güçlendirdi.",
            'D': 'Düzenli ordu, cephelerde merkezî bir komuta altında savaştı.',
            'E': "Düzenli orduya geçiş kararı Büyük Taarruz'dan sonra alındı.",
        },
        'E',
        "Düzenli orduya geçiş TBMM'nin açılmasından sonra, 1920 sonlarında başlamış; düzenli ordu ilk başarısını 1921 başında kazanmıştır. Büyük Taarruz ise 1922'dedir; bu nedenle karar Büyük Taarruz'dan sonra alınmış olamaz.",
    ),
    # düzey 2
    '0060': patch(
        "Aşağıdakilerden hangisi Kurtuluş Savaşı'nın hazırlık dönemi gelişmelerinden biri değildir?",
        {
            'A': 'Havza Genelgesi',
            'B': 'Amasya Genelgesi',
            'C': 'Erzurum Kongresi',
            'D': 'Sivas Kongresi',
            'E': "Cumhuriyet'in ilanı",
        },
        'E',
        "Cumhuriyet'in ilanı (29 Ekim 1923) savaş sonrası döneme, inkılaplar aşamasına aittir; hazırlık dönemi gelişmesi değildir. Havza-Amasya genelgeleri ile Erzurum ve Sivas kongreleri hazırlık dönemine aittir.",
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
    print(f"1 paket / {len(PATCHES)} soru ('Kurtuluş Savaşı ve Cepheler' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
