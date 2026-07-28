#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kalıp-dolgu SÖZCÜK tell'i temizliği (URETIM_KURALLARI §5).

KUSUR: çeldiricilerde bol, doğru şıkta neredeyse hiç bulunmayan mutlak-dil
kalıpları kör öğrenciye eleme avantajı veriyordu. `zorunda` 39 çeldirici / 0
doğru şık (tms_21 örneği), `Her hâlde` 31/0, `hiçbir <pekiştireç>` 25/0,
`…bir ölçümü ifade eder` 29/0. Eleme stratejisi (işaretlileri at, kalandan seç)
en kötü paketlerde %34'e çıkıyordu; rastgele %20.

BU BİR ÜSLUP TERCİHİ DEĞİL, EV ARTEFAKTI: 2014-2026 arşivinden çıkarılan
12.436 GERÇEK sınav şıkkında `hiçbir` %0,2 · `Her hâlde` %0,0 · `zorunda` %0,0 ·
`ifade eder` %0,0 · `niteliğinde` %0,1. Bizim havuzda ~%9. Temizlik soruları
gerçek sınava YAKLAŞTIRIR.

KAPSAM: yalnız aşağıdaki dosya listesi. Liste, kuru çalıştırmada kör öğrenci
oranının yükselmediği (k1 < 31 ve k1 <= k0+3) paketlerden oluşur. Temizlik
çeldiricileri kısalttığı için bazı pakette doğru şık sistematik EN UZUN kalıyor
ve kör fırlıyor; o paketler bilerek DIŞARIDA bırakıldı ve elle boy dengesi
bekliyor (aşağıdaki BEKLEYEN listesi). Eşik düşürme değil, sıralama kararıdır.

DOKUNULMAYAN: `hiçbir istisna`, `hiçbir fark`, `hiçbir etkisi`, `hiçbir ilgisi`,
`hiçbir sorumluluk` gibi anlamın parçası olan kullanımlar.

    --check : dosyalar temizlenmiş hâlde mi (fark varsa çıkış 1)
    --write : içerik + uygulama repolarına yaz
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"

# ── Türkçe edilgen geniş zaman: -mek/-mak → -ir/-ır/-ur/-ür ────────────────────
_SON_UNLU = re.compile(r"[aeıioöuü](?=[^aeıioöuü]*$)")


def _cekimle(mastar: str) -> str | None:
    """'çevrilmek' → 'çevrilir'. Yalnız -ilmek/-ılmak/-ulmak/-ülmek/-nmak edilgenleri."""
    m = re.match(r"^(.*?)(ıl|il|ul|ül|n)(mak|mek)$", mastar)
    if not m:
        return None
    govde, ek = m.group(1), m.group(2)
    son = _SON_UNLU.search(govde + ek)
    if not son:
        return None
    v = son.group(0)
    ses = {"a": "ır", "ı": "ır", "o": "ur", "u": "ur",
           "e": "ir", "i": "ir", "ö": "ür", "ü": "ür"}[v]
    return govde + ek + ses


KUYRUK = re.compile(
    r"\s+(\w+?(?:ıl|il|ul|ül|n)m[ae]k)\s+zorunda\s+(?:olan|tutulan|bulunan|kalınan)\s+"
    r"(?:bir\s+)?(?:ölçüm[üu]|kalem[i]?|kalemleri|işlem[i]?|durum[u]?|varlığı|tutarı|hâli)\s*"
    r"(?:ifade eder|karşılar|olarak nitelendirilir)\.?$")
KUYRUK2 = re.compile(
    r"\s+(\w+?(?:ıl|il|ul|ül|n)m[ae]k)\s+zorunda\s+(?:olan|tutulan|bulunan)\s+bir\s+"
    r"(?:kalemdir|ölçümdür|işlemdir|durumdur)\.?$")
PEKISTIREC = re.compile(r"\s*\b[Hh]içbir\s+(?:biçimde|hâlde|halde|koşulda|şekilde|surette|zaman)\b\s*")
HERHALDE = re.compile(r"^[Hh]er\s+hâlde\s+|^[Hh]er\s+halde\s+")
# Cümle içinde de geçiyor (866 çeldirici / 5 doğru şık = 173x asimetri).
# Zarf tümleci olduğu için silinmesi dilbilgisel olarak güvenlidir.
HERHALDE_ICI = re.compile(r"\s+[Hh]er\s+(?:hâlde|halde)\s+")
NITELIK = re.compile(r"\s+niteliğinde(?:ki)?\s+\w+\s+kalemlerinin\s+(?:tümü|tamamı)\b")
NITELIK2 = re.compile(r"\s+niteliğinde(?:ki)?\s+(?:varlık|kaynak|kalem)\w*\s+(?:kalemler|kalemleri)?\s*")
ZORUNDA_SON = re.compile(r"\s+zorunda\s+(?:tutulmuş bulunur|bırakılmış bulunur|tutulmuştur|bırakılmıştır)\.?$")


def temizle(s: str, tam: bool = True) -> tuple[str, list[str]]:
    """Metni temizler; (yeni_metin, uygulanan_kural_listesi) döndürür."""
    kurallar = []
    o = s

    for kal, ad in ((KUYRUK, "kuyruk"), (KUYRUK2, "kuyruk2")):
        m = kal.search(o)
        if m:
            cekim = _cekimle(m.group(1))
            if cekim:
                o = o[:m.start()] + " " + cekim
                kurallar.append(ad)

    m = ZORUNDA_SON.search(o)
    if m:
        o = o[:m.start()]
        kurallar.append("zorunda-son")

    if PEKISTIREC.search(o):
        yeni = PEKISTIREC.sub(" ", o).strip()
        yeni = re.sub(r"\s{2,}", " ", yeni)
        yeni = re.sub(r"\s+([;,.])", r"\1", yeni)
        if yeni and yeni[0].islower():
            yeni = yeni[0].upper() + yeni[1:]
        o = yeni
        kurallar.append("pekiştireç")

    if HERHALDE.search(o):
        yeni = HERHALDE.sub("", o).strip()
        if yeni and yeni[0].islower():
            yeni = yeni[0].upper() + yeni[1:]
        o = yeni
        kurallar.append("her-hâlde")

    if tam and HERHALDE_ICI.search(o):
        o = HERHALDE_ICI.sub(" ", o).strip()
        kurallar.append("her-hâlde-içi")

    if NITELIK.search(o):
        o = NITELIK.sub("", o)
        kurallar.append("nitelik")
    elif NITELIK2.search(o):
        o = NITELIK2.sub(" ", o)
        kurallar.append("nitelik2")

    o = re.sub(r"\s{2,}", " ", o).strip()
    return o, kurallar


# ── Dilbilgisi/güvenlik korumaları ────────────────────────────────────────────
BITIS = re.compile(
    r"(ir|ır|ur|ür|dir|dır|dur|dür|maz|mez|ler|lar|tır|tir|tur|tür|di|dı|mış|miş|"
    r"lir|lır|lur|lür|nir|nır|nur|nür|ar|er|z|n|ı|i|u|ü|a|e|k|t|p|s|m|l|r|]|\))$",
    re.I)


def guvenli(eski: str, yeni: str) -> str | None:
    """Kabul edilemezse gerekçe döndürür, kabul edilirse None."""
    if yeni == eski:
        return "değişmedi"
    if len(yeni) < 18:
        return f"çok kısaldı ({len(yeni)})"
    if len(yeni) > len(eski):
        return "uzadı"
    if not yeni[0].isupper():
        return "büyük harfle başlamıyor"
    if re.search(r"\s(ve|ile|için|olarak|göre|kadar|gibi|de|da)$", yeni):
        return "bağlaçla bitiyor"
    if re.search(r"m[ae]k$", yeni):
        return "mastarla bitiyor"
    son = yeni.rstrip(".").split()[-1]
    if not BITIS.search(son):
        return f"şüpheli bitiş: …{son}"
    return None


# NOT: muhasebe_standartlari/tms_21_kur_degisimi.json bilerek DIŞARIDA —
# o paketin sahibi build_standards_profile_calibration.py'dir ve metinleri
# zaten kalıp-dolgusuz yazılmıştır. İki builder aynı soruya yazarsa çalışma
# sırası sonucu belirler; her sorunun tek sahibi olmalıdır.

# Tüm kurallar uygulanır (cümle içi 'her hâlde' dâhil):
TAM = [
    "muhasebe_standartlari/tfrs_16_kiralamalar.json",
    "muhasebe_standartlari/tms_36_deger_dusuklugu.json",
    "borclar_hukuku/borc_iliskisi_kaynaklari.json",
    "borclar_hukuku/borcun_ifasi_sona_ermesi.json",
    "borclar_hukuku/sozlesmenin_kurulmasi.json",
    "denetim/denetim_kaniti.json",
    "denetim/denetim_kavrami.json",
    "denetim/denetim_ornekleme.json",
    "denetim/denetim_raporu.json",
    "denetim/denetim_riski.json",
    "denetim/denetim_standartlari_etik.json",
    "ekonomi/makroekonomi.json",
    "ekonomi/mikroekonomi.json",
    "ekonomi/para_banka_dis_ekonomi.json",
    "finansal_muhasebe/donem_sonu_islemleri.json",
    "finansal_muhasebe/hazir_degerler.json",
    "finansal_muhasebe/kdv_muhasebesi.json",
    "finansal_muhasebe/kur_farklari.json",
    "finansal_muhasebe/maddi_duran_varliklar.json",
    "finansal_muhasebe/maddi_olmayan_duran_varliklar.json",
    "finansal_muhasebe/mali_duran_varliklar.json",
    "finansal_muhasebe/menkul_kiymetler.json",
    "finansal_muhasebe/muhasebe_sureci_hesap_plani.json",
    "finansal_muhasebe/muhasebenin_temel_kavramlari.json",
    "finansal_muhasebe/ticari_alacaklar.json",
    "is_ve_sosyal_guvenlik_hukuku/is_hukuku_is_sozlesmesi.json",
    "is_ve_sosyal_guvenlik_hukuku/is_sozlesmesinin_sona_ermesi.json",
    "mali_tablolar_analizi/dikey_analiz.json",
    "mali_tablolar_analizi/fon_akim_analizi.json",
    "mali_tablolar_analizi/karsilastirmali_analiz.json",
    "maliye/kamu_maliyesi_temel.json",
    "maliyet_muhasebesi/birlesik_maliyet.json",
    "maliyet_muhasebesi/safha_maliyeti.json",
    "maliyet_muhasebesi/siparis_maliyeti.json",
    "maliyet_muhasebesi/standart_maliyet.json",
    "matematik/limit_turev_seri.json",
    "meslek_hukuku/meslek_hukuku_esaslari.json",
    "meslek_hukuku/meslek_orgutu_disiplin.json",
    "meslek_hukuku/mesleki_degerler_etik.json",
    "meslek_hukuku/staj_ve_sinavlar.json",
    "muhasebe_standartlari/kavramsal_cerceve.json",
    "muhasebe_standartlari/tfrs_9_finansal_arac.json",
    "muhasebe_standartlari/tms_10_sonraki_olaylar.json",
    "muhasebe_standartlari/tms_12_gelir_vergileri.json",
    "muhasebe_standartlari/tms_16_mdv.json",
    "muhasebe_standartlari/tms_1_sunulus.json",
    "muhasebe_standartlari/tms_20_devlet_tesvik.json",
    "muhasebe_standartlari/tms_23_borclanma_maliyetleri.json",
    "muhasebe_standartlari/tms_2_stoklar.json",
    "muhasebe_standartlari/tms_37_karsiliklar.json",
    "muhasebe_standartlari/tms_38_modv.json",
    "muhasebe_standartlari/tms_40_yatirim_amacli.json",
    "muhasebe_standartlari/tms_7_nakit_akis.json",
    "muhasebe_standartlari/tms_8_politikalar.json",
    "ticaret_hukuku/anonim_sirket.json",
    "ticaret_hukuku/ticaret_sirketleri.json",
    "ticaret_hukuku/ticari_isletme_tacir.json",
    "turkce/dil_bilgisi.json",
    "vergi_hukuku/amme_alacaklari.json",
    "vergi_hukuku/damga_vergisi.json",
    "vergi_hukuku/emlak_vergisi.json",
    "vergi_hukuku/kdv.json",
    "vergi_hukuku/mtv.json",
    "vergi_hukuku/vergi_usul_kanunu.json",
    "vergi_hukuku/vergilendirme_sureci.json"
]

# Cümle içi 'her hâlde' kaldırılırsa doğru şık sistematik en uzun kalıyor;
# bu pakette yalnız temel kurallar uygulanır:
TEMEL: list[str] = []   # şu an boş; 2026-07-28'de son paket de TAM'a yükseltildi

# Mekanik temizlik kör öğrenci oranını UYARI bölgesine taşıdığı için burada
# İŞLENMEZ; bu paketlerin tamamı `fix_bekleyen_denge.py` tarafından işlenir
# (aynı temizlik + elle çeldirici genişletmesi). Sahiplik orada.
# Kombine ölçüt açılınca eşiği aşan 6 paket de oraya devredildi:
BEKLEYEN = [
    "borclar_hukuku/haksiz_fiil.json",
    "borclar_hukuku/ozel_durumlar.json",
    "borclar_hukuku/sebepsiz_zenginlesme.json",
    "borclar_hukuku/temerrut_tazminat.json",
    "is_ve_sosyal_guvenlik_hukuku/sosyal_guvenlik_hukuku.json",
    "maliye/butce_maliye_politikasi.json",
    "maliye/kamu_gelir_gider.json",
    "meslek_hukuku/sorumluluk_ve_yasaklar.json",
    "ticaret_hukuku/limited_sahis_sirketleri.json",
    "vergi_hukuku/vergi_denetimi_ceza_uyusmazlik.json",
    "vergi_hukuku/vergi_hukuku_temel_kavramlar.json"
]


def _dosyayi_isle(path, write, tam):
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data["questions"] if isinstance(data, dict) else data
    degisen = 0
    atlanan = []
    for q in questions:
        secenekler = dict(q["options"])
        for L, v in secenekler.items():
            yeni, kurallar = temizle(v, tam)
            if not kurallar or guvenli(v, yeni):
                continue
            secenekler[L] = yeni
        if secenekler == q["options"]:
            continue
        # Temizlik iki secenegi ayni yapiyorsa o soru DOKUNULMADAN birakilir;
        # tur iptal edilmez. (tms_21::0021 bu duruma dustu ve tum yaziyi kesmisti.)
        if len(set(secenekler.values())) != 5:
            atlanan.append(q["id"])
            continue
        if q["answer"] not in secenekler:
            atlanan.append(q["id"])
            continue
        degisen += sum(1 for L in secenekler if secenekler[L] != q["options"][L])
        if write:
            q["options"] = secenekler
    if write and degisen:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if write and atlanan:
        print(f"  atlandi (secenek cakismasi): {', '.join(atlanan)}")
    return degisen


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--write", action="store_true")
    args = ap.parse_args()

    kalan, toplam = [], 0
    for rel, tam in [(r, True) for r in TAM] + [(r, False) for r in TEMEL]:
        for kok in (ROOT / "content", APP_ROOT / "content"):
            path = kok / rel
            n = _dosyayi_isle(path, args.write, tam)
            toplam += n
            if n and args.check:
                kalan.append(f"{path} ({n} sik temizlenmemis)")
    if args.check and kalan:
        print("Temizlenmemis dosyalar:")
        for k in kalan:
            print(f"- {k}")
        return 1
    if args.write:
        print(f"{len(TAM) + len(TEMEL)} paket / {toplam} sik temizlendi (iki repo).")
    else:
        print(f"{len(TAM)} tam + {len(TEMEL)} temel paket temiz; {len(BEKLEYEN)} paket elle boy dengesi bekliyor.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
