# -*- coding: utf-8 -*-
"""Finansal Muhasebe paketleri için ortak yardımcılar: Tekdüzen Hesap Planı adları,
yevmiye kaydı şıkkı ve "… hesabının borç tarafına … ₺ kaydedilir" biçimi.

Yevmiye şıkkı uygulamadaki `OptionTile` biçimini kullanır: kod çitli metin; borçlu satırlar
solda, alacaklı satırlar dört boşluk girintili. Doğru kaydın borç/alacak toplamları eşit
olmak zorundadır (kayit() denetler); çeldirici kayıtlar da gerçek sınavdaki gibi dengelidir,
dengesiz çeldirici ancak `dengesiz=True` ile bilerek kurulur.
"""
from decimal import Decimal

from vergi_ortak import tl

HESAP = {
    100: "Kasa", 101: "Alınan Çekler", 102: "Bankalar", 103: "Verilen Çekler ve Ödeme Emirleri",
    108: "Diğer Hazır Değerler", 110: "Hisse Senetleri", 111: "Özel Kesim Tahvil, Senet ve Bonoları",
    112: "Kamu Kesimi Tahvil, Senet ve Bonoları", 118: "Diğer Menkul Kıymetler",
    119: "Menkul Kıymetler Değer Düşüklüğü Karşılığı", 120: "Alıcılar", 121: "Alacak Senetleri",
    122: "Alacak Senetleri Reeskontu", 126: "Verilen Depozito ve Teminatlar", 127: "Diğer Ticari Alacaklar",
    128: "Şüpheli Ticari Alacaklar", 129: "Şüpheli Ticari Alacaklar Karşılığı", 131: "Ortaklardan Alacaklar",
    132: "İştiraklerden Alacaklar", 133: "Bağlı Ortaklıklardan Alacaklar", 135: "Personelden Alacaklar",
    136: "Diğer Çeşitli Alacaklar", 150: "İlk Madde ve Malzeme", 151: "Yarı Mamuller - Üretim",
    152: "Mamuller", 153: "Ticari Mallar", 157: "Diğer Stoklar", 158: "Stok Değer Düşüklüğü Karşılığı",
    159: "Verilen Sipariş Avansları", 180: "Gelecek Aylara Ait Giderler", 181: "Gelir Tahakkukları",
    190: "Devreden KDV", 191: "İndirilecek KDV", 193: "Peşin Ödenen Vergiler ve Fonlar",
    195: "İş Avansları", 196: "Personel Avansları", 197: "Sayım ve Tesellüm Noksanları",
    198: "Diğer Çeşitli Dönen Varlıklar",
    220: "Alıcılar", 221: "Alacak Senetleri", 240: "Bağlı Menkul Kıymetler", 242: "İştirakler", 245: "Bağlı Ortaklıklar", 250: "Arazi ve Arsalar",
    251: "Yeraltı ve Yerüstü Düzenleri", 252: "Binalar", 253: "Tesis, Makine ve Cihazlar", 254: "Taşıtlar",
    255: "Demirbaşlar", 257: "Birikmiş Amortismanlar", 258: "Yapılmakta Olan Yatırımlar",
    259: "Verilen Avanslar", 260: "Haklar", 263: "Araştırma ve Geliştirme Giderleri",
    264: "Özel Maliyetler", 268: "Birikmiş Amortismanlar", 280: "Gelecek Yıllara Ait Giderler",
    300: "Banka Kredileri", 303: "Uzun Vadeli Kredilerin Anapara Taksitleri ve Faizleri",
    305: "Çıkarılmış Bonolar ve Senetler", 308: "Menkul Kıymetler İhraç Farkı", 320: "Satıcılar",
    321: "Borç Senetleri", 322: "Borç Senetleri Reeskontu", 326: "Alınan Depozito ve Teminatlar",
    329: "Diğer Ticari Borçlar", 331: "Ortaklara Borçlar", 335: "Personele Borçlar",
    336: "Diğer Çeşitli Borçlar", 340: "Alınan Sipariş Avansları", 360: "Ödenecek Vergi ve Fonlar",
    361: "Ödenecek Sosyal Güvenlik Kesintileri",
    370: "Dönem Kârı Vergi ve Diğer Yasal Yükümlülük Karşılıkları",
    371: "Dönem Kârının Peşin Ödenen Vergi ve Diğer Yükümlülükleri", 372: "Kıdem Tazminatı Karşılığı",
    379: "Diğer Borç ve Gider Karşılıkları",
    380: "Gelecek Aylara Ait Gelirler", 381: "Gider Tahakkukları", 391: "Hesaplanan KDV",
    397: "Sayım ve Tesellüm Fazlaları",
    400: "Banka Kredileri", 405: "Çıkarılmış Tahviller", 407: "Çıkarılmış Diğer Menkul Kıymetler",
    472: "Kıdem Tazminatı Karşılığı", 480: "Gelecek Yıllara Ait Gelirler",
    500: "Sermaye", 501: "Ödenmemiş Sermaye", 520: "Hisse Senedi İhraç Primleri",
    522: "MDV Yeniden Değerleme Artışları", 540: "Yasal Yedekler", 541: "Statü Yedekleri",
    542: "Olağanüstü Yedekler", 549: "Özel Fonlar", 570: "Geçmiş Yıllar Kârları",
    580: "Geçmiş Yıllar Zararları", 590: "Dönem Net Kârı", 591: "Dönem Net Zararı",
    600: "Yurt İçi Satışlar", 601: "Yurt Dışı Satışlar", 602: "Diğer Gelirler", 610: "Satıştan İadeler",
    611: "Satış İskontoları", 620: "Satılan Mamuller Maliyeti", 621: "Satılan Ticari Mallar Maliyeti",
    622: "Satılan Hizmet Maliyeti", 631: "Pazarlama, Satış ve Dağıtım Giderleri",
    632: "Genel Yönetim Giderleri", 640: "İştiraklerden Temettü Gelirleri",
    641: "Bağlı Ortaklıklardan Temettü Gelirleri", 642: "Faiz Gelirleri", 643: "Komisyon Gelirleri",
    644: "Konusu Kalmayan Karşılıklar", 645: "Menkul Kıymet Satış Kârları", 646: "Kambiyo Kârları",
    647: "Reeskont Faiz Gelirleri", 649: "Diğer Olağan Gelir ve Kârlar", 653: "Komisyon Giderleri",
    654: "Karşılık Giderleri", 655: "Menkul Kıymet Satış Zararları", 656: "Kambiyo Zararları",
    657: "Reeskont Faiz Giderleri", 659: "Diğer Olağan Gider ve Zararlar",
    660: "Kısa Vadeli Borçlanma Giderleri", 661: "Uzun Vadeli Borçlanma Giderleri",
    671: "Önceki Dönem Gelir ve Kârları", 679: "Diğer Olağandışı Gelir ve Kârlar",
    680: "Çalışmayan Kısım Gider ve Zararları", 681: "Önceki Dönem Gider ve Zararları",
    689: "Diğer Olağandışı Gider ve Zararlar", 690: "Dönem Kârı veya Zararı",
    691: "Dönem Kârı Vergi ve Diğer Yasal Yükümlülük Karşılıkları", 692: "Dönem Net Kârı veya Zararı",
    710: "Direkt İlk Madde ve Malzeme Giderleri", 711: "Direkt İlk Madde ve Malzeme Yansıtma Hesabı",
    712: "Direkt İlk Madde ve Malzeme Fiyat Farkı", 713: "Direkt İlk Madde ve Malzeme Miktar Farkı",
    720: "Direkt İşçilik Giderleri", 721: "Direkt İşçilik Giderleri Yansıtma Hesabı",
    722: "Direkt İşçilik Ücret Farkları", 723: "Direkt İşçilik Süre Farkları",
    731: "Genel Üretim Giderleri Yansıtma Hesabı", 732: "Genel Üretim Giderleri Bütçe Farkları",
    733: "Genel Üretim Giderleri Verimlilik Farkları", 734: "Genel Üretim Giderleri Kapasite Farkları",
    730: "Genel Üretim Giderleri", 740: "Hizmet Üretim Maliyeti",
    741: "Hizmet Üretim Maliyeti Yansıtma Hesabı", 750: "Araştırma ve Geliştirme Giderleri",
    760: "Pazarlama, Satış ve Dağıtım Giderleri", 761: "Pazarlama, Satış ve Dağıtım Giderleri Yansıtma Hesabı",
    770: "Genel Yönetim Giderleri", 771: "Genel Yönetim Giderleri Yansıtma Hesabı",
    780: "Finansman Giderleri", 781: "Finansman Giderleri Yansıtma Hesabı",
}


def buyuk(metin):
    """Türkçe büyük harf: 'İndirilecek KDV' -> 'İNDİRİLECEK KDV'."""
    return metin.replace("i", "İ").replace("ı", "I").upper()


def ad(kod):
    """Hesabın başlık biçimli adı (kodsuz): 'İndirilecek KDV'."""
    return HESAP[kod]


def hk(kod):
    """Kodlu başlık biçimi: '191 İndirilecek KDV'."""
    return f"{kod} {HESAP[kod]}"


def _tutar(x):
    assert Decimal(str(x)) > 0, f"kayıtta sıfır/negatif tutar: {x}"
    return tl(x)


def kayit(borc, alacak, *, dengesiz=False):
    """Yevmiye kaydı şıkkı. borc/alacak: [(hesap_kodu, tutar), …]."""
    assert borc and alacak
    kurus = Decimal("0.01")  # float kur çarpımlarının 0,999… artıkları kuruşta eşitlenir
    b = sum(Decimal(str(t)).quantize(kurus) for _, t in borc)
    a = sum(Decimal(str(t)).quantize(kurus) for _, t in alacak)
    if not dengesiz:
        assert b == a, f"kayıt dengesiz: borç {b} ≠ alacak {a} ({borc} / {alacak})"
    satir = [f"{k} {buyuk(HESAP[k])} {_tutar(t)}" for k, t in borc]
    satir += [f"    {k} {buyuk(HESAP[k])} {_tutar(t)}" for k, t in alacak]
    return "```text\n" + "\n".join(satir) + "\n```"


# Adı birebir aynı olan hesap çiftleri (257/268, 263/750, 370/691, 120/220, 121/221, 300/400, 372/472):
# kodsuz "taraf" şıklarında aynı metne düşerler; aynı soruda birlikte kullanılmamalıdır.
AYNI_ADLI = {}
for _k, _v in HESAP.items():
    AYNI_ADLI.setdefault(_v, []).append(_k)


def taraf(kod, yon, tutar):
    """'Faiz Gelirleri hesabının alacak tarafına 200 ₺ kaydedilir.'"""
    assert yon in ("borç", "alacak")
    return f"{HESAP[kod]} hesabının {yon} tarafına {_tutar(tutar)} ₺ kaydedilir."
