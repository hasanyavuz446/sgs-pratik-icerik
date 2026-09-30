# -*- coding: utf-8 -*-
"""Finansal Tablolar ve Analizi builder'larının ortak modülü.

Gerçek 2026 kitapçıklarında bu dersin soruları çoğunlukla ortak bir bilanço + gelir tablosuna bağlıdır;
kök kısadır ("… yılının cari oranı kaçtır?"), şıklar artan sıralı sayılardır ve çeldiriciler tipik formül
hatalarından (dönem sonu yerine ortalama, yanlış baz yıl, net yerine brüt satış…) doğar. Bu modül:

  · Sirket  — girilen ham kalemlerden bilanço ve gelir tablosunu kurar, denkliği denetler,
              ortak tabloyu (stimulus) Markdown olarak çizer ve analiz ölçülerini hesaplar;
  · Hesap   — bir ölçünün doğru değeri, biçimi, hata-kaynaklı çeldirici adayları ve çözüm metni;
  · Fta     — Paket'in önüne geçer: sayısal soruların doğru şık sırasını (harfini) dengeli bir
              diziye göre çeldirici seçerek belirler, ortak tabloları stimuli.json'a yazar.

Ölçü tanımları (kökte ya da tablo açıklamasında belirtilir): devir hızı ve sürelerinde ortalama
değer, bir yıl 360 gün; kârlılık ve mali yapı oranlarında dönem sonu değerleri.
"""
import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yet_ortak import ROOT, APP, audit  # noqa: E402
from vergi_ortak import tl  # noqa: E402

STIMULI = os.path.join(ROOT, "content", "yeterlilik", "stimuli.json")
KONVANSIYON = ("Devir hızı ve sürelerinde ortalama değerleri kullanınız ve bir yılı 360 gün kabul ediniz; "
               "kârlılık ve mali yapı oranlarında dönem sonu değerlerini kullanınız.")


# ============================================================================ biçim
def bicimle(x, bicim):
    if bicim == "tutar":
        return tl(round(x))
    if bicim == "oran":        # 0,900
        return f"{x:.3f}".replace(".", ",")
    if bicim == "kat":         # 4,50
        return f"{x:.2f}".replace(".", ",")
    if bicim == "gun":         # 40,00
        return f"{x:.2f}".replace(".", ",")
    if bicim == "yuzde":       # 20,00 — kitapçıktaki gibi yüzde işareti kökte "(%)" olarak verilir
        return f"{x:.2f}".replace(".", ",")
    raise ValueError(bicim)


def yaz_sayi(x, bicim):
    """Çözüm metninde kullanılan sade biçim."""
    return bicimle(x, bicim)


class Hesap:
    def __init__(self, deger, bicim, hatalar, cozum):
        self.deger, self.bicim, self.hatalar, self.cozum = deger, bicim, list(hatalar), cozum


def secenekler_sirali(h, hedef, rng):
    """Doğru değer artan sıralı beş şıkta `hedef` (0=A … 4=E) sırasına düşecek biçimde dört çeldirici seçer.
    Önce formül hatalarından doğan adaylar, yetmezse doğru değerin makul katları kullanılır."""
    dogru = bicimle(h.deger, h.bicim)
    gor = {dogru}  # biçimlenmiş şıklar
    alt, ust = [], []

    def ekle(x, kaynak):
        s = bicimle(x, h.bicim)
        # Audit şık metnini işaretten arındırarak karşılaştırır: "-35.000" ile "35.000" aynı sayılır.
        if s.lstrip("-") in {g.lstrip("-") for g in gor} or x != x:  # NaN
            return
        if h.bicim != "tutar" and h.bicim != "yuzde" and x <= 0:
            return
        gor.add(s)
        (alt if x < h.deger else ust).append((kaynak, abs(x - h.deger), x, s))

    for x in h.hatalar:
        ekle(x, 0)
    for k in (0.8, 1.25, 0.9, 1.1, 0.75, 1.5, 0.6, 1.2, 0.5, 2.0, 0.85, 1.15, 0.7, 1.3, 0.4, 1.4):
        ekle(h.deger * k if h.deger else k * 10, 1)
    na, nu = hedef, 4 - hedef
    assert len(alt) >= na and len(ust) >= nu, (dogru, h.hatalar, hedef)
    # hata kaynaklı adaylar önce, aynı türde doğruya yakın olan önce
    alt.sort(key=lambda t: (t[0], t[1]))
    ust.sort(key=lambda t: (t[0], t[1]))
    sec_alt, sec_ust = alt[:na], ust[:nu]
    # Kör öğrenci "en uzun/en kısa şıkkı seç" stratejisiyle doğruyu bulmasın: doğru şık tek başına en uzun
    # (ya da en kısa) kalıyorsa, aynı taraftaki yedek adaylardan boyu uygun olanla bir çeldirici değiştirilir.
    for kosul, uygun in ((lambda L: len(dogru) > max(L), lambda t: len(t[3]) >= len(dogru)),
                         (lambda L: len(dogru) < min(L), lambda t: len(t[3]) <= len(dogru))):
        if not kosul([len(t[3]) for t in sec_alt + sec_ust]):
            continue
        for secili, yedek in ((sec_ust, ust[nu:]), (sec_alt, alt[na:])):
            aday = next((t for t in yedek if uygun(t)), None)
            if secili and aday:
                secili[-1] = aday
                break
    sec = [t[3] for t in sec_alt + sec_ust]
    rng.shuffle(sec)
    return dogru, sec


# ============================================================================ şirket
BILANCO = [
    ("DÖNEN VARLIKLAR", None),
    ("Hazır Değerler", "hd"), ("Menkul Kıymetler", "mk"), ("Ticari Alacaklar", "ta"),
    ("Diğer Alacaklar", "da"), ("Stoklar", "stok"), ("Diğer Dönen Varlıklar", "ddv"),
    ("DURAN VARLIKLAR", None),
    ("Maddi Duran Varlıklar", "mdv"), ("Maddi Olmayan Duran Varlıklar", "modv"),
    ("AKTİF (VARLIKLAR) TOPLAMI", None),
    ("KISA VADELİ YAB. KAY.", None),
    ("Mali Borçlar", "kvmb"), ("Ticari Borçlar", "tb"), ("Diğer Borçlar", "db"),
    ("UZUN VADELİ YAB. KAY.", None),
    ("Mali Borçlar", "uvmb"),
    ("ÖZ KAYNAKLAR", None),
    ("Ödenmiş Sermaye", "sermaye"), ("Geçmiş Yıllar Kârları", "gyk"), ("Dönem Net Kârı (Zararı)", "nk"),
    ("PASİF (KAYNAKLAR) TOPLAMI", None),
]
GRUP = {"DÖNEN VARLIKLAR": "dv", "DURAN VARLIKLAR": "duran", "AKTİF (VARLIKLAR) TOPLAMI": "aktif",
        "KISA VADELİ YAB. KAY.": "kvyk", "UZUN VADELİ YAB. KAY.": "uvyk", "ÖZ KAYNAKLAR": "ok",
        "PASİF (KAYNAKLAR) TOPLAMI": "aktif"}
GELIR = [("Brüt Satışlar", "brut"), ("Satış İndirimleri (-)", "ind"), ("Net Satışlar", "ns"),
         ("Satışların Maliyeti (-)", "smm"), ("Brüt Satış Kârı", "bk"), ("Faaliyet Giderleri (-)", "fg"),
         ("Faaliyet Kârı", "fk"), ("Finansman Giderleri (-)", "fin"), ("Dönem Kârı", "dk"),
         ("Dönem Kârı Vergi Karşılığı (-)", "vergi"), ("Dönem Net Kârı", "nk")]
AD = {"hd": "hazır değerler", "mk": "menkul kıymetler", "ta": "ticari alacaklar", "da": "diğer alacaklar",
      "stok": "stoklar", "ddv": "diğer dönen varlıklar", "dv": "dönen varlıklar", "mdv": "maddi duran varlıklar",
      "modv": "maddi olmayan duran varlıklar", "duran": "duran varlıklar", "aktif": "aktif toplamı",
      "kvmb": "kısa vadeli mali borçlar", "tb": "ticari borçlar", "db": "diğer borçlar",
      "kvyk": "kısa vadeli yabancı kaynaklar", "uvmb": "uzun vadeli mali borçlar",
      "uvyk": "uzun vadeli yabancı kaynaklar", "ok": "öz kaynaklar", "sermaye": "ödenmiş sermaye",
      "gyk": "geçmiş yıllar kârları", "nk": "dönem net kârı", "brut": "brüt satışlar",
      "ind": "satış indirimleri", "ns": "net satışlar", "smm": "satışların maliyeti", "bk": "brüt satış kârı",
      "fg": "faaliyet giderleri", "fk": "faaliyet kârı", "fin": "finansman giderleri", "dk": "dönem kârı",
      "vergi": "vergi karşılığı", "yk": "toplam yabancı kaynaklar"}
GELIR_KALEM = {k for _, k in GELIR}


class Sirket:
    """Ham kalemlerden (liste: her dönem bir değer) finansal tabloları kurar.
    Kısa vadeli mali borçlar denkleştirici kalemdir: aktif − (diğer kaynaklar)."""

    def __init__(self, ad, yillar, *, vergi_orani=0.25, **k):
        self.ad, self.yillar = ad, list(yillar)
        n = len(self.yillar)
        v = {}
        for anahtar in ("hd", "mk", "ta", "da", "stok", "ddv", "mdv", "modv", "tb", "db", "uvmb", "sermaye",
                        "gyk", "brut", "ind", "smm", "fg", "fin"):
            x = k.pop(anahtar, [0] * n)
            assert len(x) == n, (ad, anahtar)
            v[anahtar] = list(x)
        assert not k, k
        v["dv"] = [sum(v[a][i] for a in ("hd", "mk", "ta", "da", "stok", "ddv")) for i in range(n)]
        v["duran"] = [v["mdv"][i] + v["modv"][i] for i in range(n)]
        v["aktif"] = [v["dv"][i] + v["duran"][i] for i in range(n)]
        v["ns"] = [v["brut"][i] - v["ind"][i] for i in range(n)]
        v["bk"] = [v["ns"][i] - v["smm"][i] for i in range(n)]
        v["fk"] = [v["bk"][i] - v["fg"][i] for i in range(n)]
        v["dk"] = [v["fk"][i] - v["fin"][i] for i in range(n)]
        v["vergi"] = [round(max(v["dk"][i], 0) * vergi_orani) for i in range(n)]
        v["nk"] = [v["dk"][i] - v["vergi"][i] for i in range(n)]
        v["uvyk"] = list(v["uvmb"])
        v["ok"] = [v["sermaye"][i] + v["gyk"][i] + v["nk"][i] for i in range(n)]
        v["kvmb"] = [v["aktif"][i] - v["tb"][i] - v["db"][i] - v["uvyk"][i] - v["ok"][i] for i in range(n)]
        for i in range(n):
            assert v["kvmb"][i] > 0, (ad, i, v["kvmb"][i])
        v["kvyk"] = [v["kvmb"][i] + v["tb"][i] + v["db"][i] for i in range(n)]
        v["yk"] = [v["kvyk"][i] + v["uvyk"][i] for i in range(n)]
        for i in range(n):
            assert v["kvyk"][i] + v["uvyk"][i] + v["ok"][i] == v["aktif"][i]
        self.v = v
        self.vergi_orani = vergi_orani

    # ------------------------------------------------------------------ çizim
    def i(self, yil):
        return self.yillar.index(str(yil))

    def tablo(self, gelir=True):
        bas = "| Kalem | " + " | ".join(f"31.12.{y}" for y in self.yillar) + " |\n|---|" + "---|" * len(self.yillar)
        satir = []
        for etiket, anahtar in BILANCO:
            a = anahtar or GRUP[etiket]
            if anahtar and not any(self.v[a]):
                continue
            satir.append(f"| {etiket} | " + " | ".join(tl(x) for x in self.v[a]) + " |")
        md = "**Bilanço**\n\n" + bas + "\n" + "\n".join(satir)
        if gelir:
            g = []
            for etiket, a in GELIR:
                if a == "ind" and not any(self.v[a]):
                    continue
                g.append(f"| {etiket} | " + " | ".join(tl(x) for x in self.v[a]) + " |")
            bas2 = "| Kalem | " + " | ".join(self.yillar) + " |\n|---|" + "---|" * len(self.yillar)
            md += "\n\n**Gelir Tablosu**\n\n" + bas2 + "\n" + "\n".join(g)
        return md

    def uyaran(self, sid, baslik=None, caption=None):
        return {"id": sid, "title": baslik or f"{self.ad} — Finansal Tablolar", "kind": "table",
                "bodyMarkdown": self.tablo(),
                "caption": caption or f"{self.ad}’ye ait soruları bu tablolara göre cevaplayınız. {KONVANSIYON}"}

    # ------------------------------------------------------------------ yardımcılar
    def x(self, a, yil):
        return self.v[a][self.i(yil)]

    def onceki(self, yil):
        """Önceki dönem. İlk dönemde (yalnız çeldirici üretiminde kullanılır) sonraki dönem döner:
        'yanlış yılın verisi' hatası."""
        j = self.i(yil)
        return self.yillar[j - 1] if j else self.yillar[1]

    def ort(self, a, yil):
        j = self.i(yil)
        k = j - 1 if j else 1
        return (self.v[a][k] + self.v[a][j]) / 2

    def _ilk_degil(self, yil):
        assert self.i(yil) >= 1, f"{self.ad} {yil}: bu ölçü önceki dönem verisi gerektirir"

    def _t(self, a, yil):
        return tl(self.x(a, yil))

    # ------------------------------------------------------------------ likidite
    def cari(self, y):
        dv, kv = self.x("dv", y), self.x("kvyk", y)
        return Hesap(dv / kv, "oran",
                     [(dv - self.x("stok", y)) / kv, self.x("hd", y) / kv, kv / dv, dv / self.x("yk", y),
                      self.x("dv", self.onceki(y)) / self.x("kvyk", self.onceki(y))],
                     f"{self.ad} {y} cari oranı = dönen varlıklar ÷ kısa vadeli yabancı kaynaklar = "
                     f"{tl(dv)} ÷ {tl(kv)} = {bicimle(dv / kv, 'oran')}.")

    def likidite(self, y):
        dv, st, kv = self.x("dv", y), self.x("stok", y), self.x("kvyk", y)
        d = (dv - st) / kv
        return Hesap(d, "oran",
                     [dv / kv, (self.x("hd", y) + self.x("mk", y)) / kv, (dv - st) / self.x("yk", y),
                      (dv - st - self.x("ta", y)) / kv, (self.x("dv", self.onceki(y)) - self.x("stok", self.onceki(y)))
                      / self.x("kvyk", self.onceki(y))],
                     f"{self.ad} {y} likidite (asit-test) oranı = (dönen varlıklar − stoklar) ÷ KVYK = "
                     f"({tl(dv)} − {tl(st)}) ÷ {tl(kv)} = {bicimle(d, 'oran')}.")

    def nakit_orani(self, y):
        n, kv = self.x("hd", y) + self.x("mk", y), self.x("kvyk", y)
        return Hesap(n / kv, "oran",
                     [(self.x("dv", y) - self.x("stok", y)) / kv, n / self.x("dv", y), n / self.x("yk", y),
                      self.x("hd", y) / self.x("aktif", y) * 10,
                      (self.x("hd", self.onceki(y)) + self.x("mk", self.onceki(y))) / self.x("kvyk", self.onceki(y))],
                     f"{self.ad} {y} nakit oranı = (hazır değerler + menkul kıymetler) ÷ KVYK = {tl(n)} ÷ {tl(kv)} = "
                     f"{bicimle(n / kv, 'oran')}.")

    def nis(self, y):
        dv, kv = self.x("dv", y), self.x("kvyk", y)
        return Hesap(dv - kv, "tutar",
                     [dv, dv - self.x("yk", y), kv - dv, self.x("dv", self.onceki(y)) - self.x("kvyk", self.onceki(y)),
                      dv - self.x("stok", y) - kv],
                     f"{self.ad} {y} net işletme sermayesi = dönen varlıklar − KVYK = {tl(dv)} − {tl(kv)} = "
                     f"{tl(dv - kv)} ₺.")

    # ------------------------------------------------------------------ faaliyet (devir)
    def _devir(self, pay, payda, y, ad_pay, ad_payda, sure, gun_ad):
        self._ilk_degil(y)
        o = self.ort(payda, y)
        hiz = self.x(pay, y) / o
        if not sure:
            return Hesap(hiz, "kat",
                         [self.x(pay, y) / self.x(payda, y), self.x(pay, y) / self.x(payda, self.onceki(y)),
                          (self.x("ns" if pay == "smm" else "smm", y)) / o, o / self.x(pay, y) * 10,
                          360 / hiz],
                         f"{self.ad} {y} {gun_ad} devir hızı = {ad_pay} ÷ ortalama {ad_payda} = {tl(self.x(pay, y))} ÷ "
                         f"[({tl(self.x(payda, self.onceki(y)))} + {tl(self.x(payda, y))}) ÷ 2] = {bicimle(hiz, 'kat')}.")
        s = 360 / hiz
        return Hesap(s, "gun",
                     [360 * self.x(payda, y) / self.x(pay, y), 365 / hiz,
                      360 * o / self.x("ns" if pay == "smm" else "smm", y),
                      360 * self.x(payda, self.onceki(y)) / self.x(pay, y), hiz],
                     f"{self.ad} {y} {gun_ad} devir hızı = {ad_pay} ÷ ortalama {ad_payda} = {tl(self.x(pay, y))} ÷ "
                     f"{tl(o)} = {bicimle(hiz, 'kat')}; süre = 360 ÷ {bicimle(hiz, 'kat')} = {bicimle(s, 'gun')} gün.")

    def stok_hiz(self, y):
        return self._devir("smm", "stok", y, "satışların maliyeti", "stok", False, "stok")

    def stok_sure(self, y):
        return self._devir("smm", "stok", y, "satışların maliyeti", "stok", True, "stok")

    def alacak_hiz(self, y):
        return self._devir("ns", "ta", y, "net satışlar", "ticari alacak", False, "ticari alacak")

    def alacak_sure(self, y):
        h = self._devir("ns", "ta", y, "net satışlar", "ticari alacak", True, "ticari alacak")
        h.hatalar.append(360 * self.ort("ta", y) / self.x("brut", y))
        return h

    def borc_sure(self, y):
        return self._devir("smm", "tb", y, "satışların maliyeti", "ticari borç", True, "ticari borç")

    def aktif_hiz(self, y):
        return self._devir("ns", "aktif", y, "net satışlar", "aktif toplamı", False, "aktif")

    def dv_hiz(self, y):
        return self._devir("ns", "dv", y, "net satışlar", "dönen varlıklar", False, "dönen varlık")

    # ------------------------------------------------------------------ kârlılık ve mali yapı (%)
    def _yuzde(self, pay, payda, y, hatalar, ad):
        d = self.x(pay, y) / self.x(payda, y) * 100
        return Hesap(d, "yuzde", hatalar,
                     f"{self.ad} {y} {ad} = {AD[pay]} ÷ {AD[payda]} = {tl(self.x(pay, y))} ÷ {tl(self.x(payda, y))} = "
                     f"{bicimle(d, 'yuzde')}.")

    def _ayni_onceki(self, pay, payda, y):
        p = self.onceki(y)
        return self.x(pay, p) / self.x(payda, p) * 100

    def brut_marj(self, y):
        x = self.x
        return self._yuzde("bk", "ns", y, [x("bk", y) / x("brut", y) * 100, x("fk", y) / x("ns", y) * 100,
                                          x("bk", y) / x("smm", y) * 100, x("nk", y) / x("ns", y) * 100,
                                          self._ayni_onceki("bk", "ns", y)], "brüt satış kârlılığı")

    def faal_marj(self, y):
        x = self.x
        return self._yuzde("fk", "ns", y, [x("fk", y) / x("brut", y) * 100, x("bk", y) / x("ns", y) * 100,
                                          x("dk", y) / x("ns", y) * 100, x("fk", y) / x("smm", y) * 100,
                                          self._ayni_onceki("fk", "ns", y)], "faaliyet kârlılığı")

    def net_marj(self, y):
        x = self.x
        return self._yuzde("nk", "ns", y, [x("nk", y) / x("brut", y) * 100, x("dk", y) / x("ns", y) * 100,
                                          x("fk", y) / x("ns", y) * 100, x("nk", y) / x("aktif", y) * 100,
                                          self._ayni_onceki("nk", "ns", y)], "net kâr marjı")

    def varlik_karl(self, y):
        x = self.x
        return self._yuzde("nk", "aktif", y, [x("nk", y) / self.ort("aktif", y) * 100, x("dk", y) / x("aktif", y) * 100,
                                             x("nk", y) / x("dv", y) * 100, x("fk", y) / x("aktif", y) * 100,
                                             self._ayni_onceki("nk", "aktif", y)], "varlıkların kârlılığı")

    def ozk_karl(self, y):
        x = self.x
        return self._yuzde("nk", "ok", y, [x("nk", y) / x("sermaye", y) * 100, x("dk", y) / x("ok", y) * 100,
                                          x("nk", y) / x("aktif", y) * 100, x("nk", y) / self.ort("ok", y) * 100,
                                          self._ayni_onceki("nk", "ok", y)], "öz kaynak kârlılığı")

    def kaldirac(self, y):
        x = self.x
        return self._yuzde("yk", "aktif", y, [x("kvyk", y) / x("aktif", y) * 100, x("ok", y) / x("aktif", y) * 100,
                                             x("yk", y) / x("ok", y) * 100, x("uvyk", y) / x("aktif", y) * 100,
                                             self._ayni_onceki("yk", "aktif", y)], "kaldıraç oranı")

    def ozk_oran(self, y):
        x = self.x
        return self._yuzde("ok", "aktif", y, [x("yk", y) / x("aktif", y) * 100, x("ok", y) / x("yk", y) * 100,
                                             x("sermaye", y) / x("aktif", y) * 100, x("ok", y) / x("duran", y) * 100,
                                             self._ayni_onceki("ok", "aktif", y)], "öz kaynakların aktif toplamına oranı")

    def ds_oran(self, y):
        x = self.x
        d = (x("uvyk", y) + x("ok", y)) / x("aktif", y) * 100
        return Hesap(d, "yuzde", [x("ok", y) / x("aktif", y) * 100, x("uvyk", y) / x("aktif", y) * 100,
                                  (x("kvyk", y) + x("ok", y)) / x("aktif", y) * 100,
                                  (x("uvyk", y) + x("ok", y)) / x("duran", y) * 100,
                                  (x("uvyk", self.onceki(y)) + x("ok", self.onceki(y))) / x("aktif", self.onceki(y)) * 100],
                     f"{self.ad} {y} devamlı sermaye oranı = (UVYK + öz kaynaklar) ÷ pasif toplamı = ({tl(x('uvyk', y))} + "
                     f"{tl(x('ok', y))}) ÷ {tl(x('aktif', y))} = {bicimle(d, 'yuzde')}.")

    def borc_ozk(self, y):
        x = self.x
        d = x("yk", y) / x("ok", y)
        return Hesap(d, "oran", [x("ok", y) / x("yk", y), x("yk", y) / x("aktif", y), x("kvyk", y) / x("ok", y),
                                 x("yk", self.onceki(y)) / x("ok", self.onceki(y)), x("uvyk", y) / x("ok", y)],
                     f"{self.ad} {y} yabancı kaynakların öz kaynaklara oranı = {tl(x('yk', y))} ÷ {tl(x('ok', y))} = "
                     f"{bicimle(d, 'oran')}.")

    # ------------------------------------------------------------------ dikey, trend, karşılaştırmalı
    def dikey(self, a, y):
        x = self.x
        gelir = a in GELIR_KALEM
        taban = "ns" if gelir else "aktif"
        d = x(a, y) / x(taban, y) * 100
        diger = [x(a, self.onceki(y)) / x(taban, self.onceki(y)) * 100,
                 100 - d if d < 100 else d - 100,
                 x(a, y) / x("brut" if gelir else "dv", y) * 100,
                 x(a, y) / x("smm" if gelir else "ok", y) * 100]
        return Hesap(d, "yuzde", diger,
                     f"{self.ad} {y} dikey analizinde {AD[a]}, {'net satışların' if gelir else 'aktif (pasif) toplamının'} "
                     f"yüzdesi olarak gösterilir: {tl(x(a, y))} ÷ {tl(x(taban, y))} × 100 = {bicimle(d, 'yuzde')}.")

    def trend(self, a, y, baz):
        x = self.x
        d = x(a, y) / x(a, baz) * 100
        yanlis = [y2 for y2 in self.yillar if y2 not in (str(y), str(baz))]
        diger = [(x(a, y) - x(a, baz)) / x(a, baz) * 100, x(a, baz) / x(a, y) * 100]
        diger += [x(a, y) / x(a, b) * 100 for b in yanlis]
        diger += [x(a, b) / x(a, baz) * 100 for b in yanlis]
        return Hesap(d, "yuzde", diger,
                     f"{self.ad} için {baz} baz yıl alındığında {AD[a]} {y} trend yüzdesi = {tl(x(a, y))} ÷ "
                     f"{tl(x(a, baz))} × 100 = {bicimle(d, 'yuzde')}.")

    def degisim(self, a, y):
        self._ilk_degil(y)
        x = self.x
        p = self.onceki(y)
        d = (x(a, y) - x(a, p)) / x(a, p) * 100
        taban = "ns" if a in GELIR_KALEM else "aktif"
        ilk = self.yillar[0]
        diger = [(x(a, y) - x(a, p)) / x(a, y) * 100, x(a, y) / x(a, p) * 100,
                 (x(a, y) - x(a, p)) / x(taban, p) * 100, (x(a, y) - x(a, p)) / ((x(a, y) + x(a, p)) / 2) * 100]
        if ilk != p:
            diger.append((x(a, y) - x(a, ilk)) / x(a, ilk) * 100)
        return Hesap(d, "yuzde", diger,
                     f"{self.ad} karşılaştırmalı tablolar analizinde {AD[a]} {p}-{y} değişim yüzdesi = ({tl(x(a, y))} − "
                     f"{tl(x(a, p))}) ÷ {tl(x(a, p))} × 100 = {bicimle(d, 'yuzde')}.")

    # ------------------------------------------------------------------ nakit
    def satis_nakit(self, y):
        self._ilk_degil(y)
        x = self.x
        p = self.onceki(y)
        d = x("ns", y) - (x("ta", y) - x("ta", p))
        return Hesap(d, "tutar", [x("ns", y) + (x("ta", y) - x("ta", p)), x("ns", y), x("brut", y) - (x("ta", y) - x("ta", p)),
                                  x("ns", y) - x("ta", y), x("ns", y) - x("ta", p)],
                     f"{self.ad} {y} satışlardan nakit girişi = net satışlar − ticari alacak artışı = {tl(x('ns', y))} − "
                     f"({tl(x('ta', y))} − {tl(x('ta', p))}) = {tl(d)} ₺.")

    def alim_nakit(self, y):
        self._ilk_degil(y)
        x = self.x
        p = self.onceki(y)
        ds, db = x("stok", y) - x("stok", p), x("tb", y) - x("tb", p)
        d = x("smm", y) + ds - db
        return Hesap(d, "tutar", [x("smm", y) - ds - db, x("smm", y) + ds + db, x("smm", y), x("smm", y) + ds,
                                  x("smm", y) - ds + db],
                     f"{self.ad} {y} mal alımları için nakit çıkışı = satışların maliyeti + stok artışı − ticari borç "
                     f"artışı = {tl(x('smm', y))} + ({tl(ds)}) − ({tl(db)}) = {tl(d)} ₺.")


# ============================================================================ çok yıllı özet seri
class Seri:
    """Trend ve karşılaştırmalı analiz için birkaç kalemin çok yıllı özet tablosu (gerçek kitapçıktaki
    '31 Aralık 2022 … 2025 · Ticari Alacaklar · Stoklar · Net Satışlar' biçimi)."""

    def __init__(self, ad, yillar, kalemler):
        self.ad, self.yillar = ad, [str(y) for y in yillar]
        self.etiket = {}
        self.v = {}
        for etiket, anahtar, degerler in kalemler:
            assert len(degerler) == len(self.yillar), (ad, anahtar)
            self.etiket[anahtar] = etiket
            self.v[anahtar] = list(degerler)

    def i(self, yil):
        return self.yillar.index(str(yil))

    def x(self, a, yil):
        return self.v[a][self.i(yil)]

    def onceki(self, yil):
        j = self.i(yil)
        return self.yillar[j - 1] if j else self.yillar[1]

    def adi(self, a):
        return self.etiket[a].lower().replace("(-)", "").strip()

    def tablo(self):
        bas = "| Kalem | " + " | ".join(f"31.12.{y}" for y in self.yillar) + " |\n|---|" + "---|" * len(self.yillar)
        return bas + "\n" + "\n".join(f"| {self.etiket[a]} | " + " | ".join(tl(x) for x in self.v[a]) + " |"
                                       for a in self.v)

    def uyaran(self, sid, caption=None):
        return {"id": sid, "title": f"{self.ad} — Özet Finansal Veriler", "kind": "table", "bodyMarkdown": self.tablo(),
                "caption": caption or f"{self.ad}’ye ait soruları bu tabloya göre cevaplayınız."}

    def trend(self, a, y, baz):
        x = self.x
        y, baz = str(y), str(baz)
        d = x(a, y) / x(a, baz) * 100
        diger = [(x(a, y) - x(a, baz)) / x(a, baz) * 100, x(a, baz) / x(a, y) * 100]
        diger += [x(a, y) / x(a, b) * 100 for b in self.yillar if b not in (y, baz)]
        diger += [x(a, b) / x(a, baz) * 100 for b in self.yillar if b not in (y, baz)]
        return Hesap(d, "yuzde", diger,
                     f"{self.ad} için {baz} baz yıl alındığında {self.adi(a)} {y} trend yüzdesi = {tl(x(a, y))} ÷ "
                     f"{tl(x(a, baz))} × 100 = {bicimle(d, 'yuzde')}.")

    def degisim(self, a, y):
        x = self.x
        y = str(y)
        assert self.i(y) >= 1
        p = self.onceki(y)
        d = (x(a, y) - x(a, p)) / x(a, p) * 100
        return Hesap(d, "yuzde", [(x(a, y) - x(a, p)) / x(a, y) * 100, x(a, y) / x(a, p) * 100,
                                  (x(a, p) - x(a, y)) / x(a, y) * 100,
                                  (x(a, y) - x(a, self.yillar[0])) / x(a, self.yillar[0]) * 100],
                     f"{self.ad} karşılaştırmalı analizinde {self.adi(a)} {p}-{y} değişim yüzdesi = ({tl(x(a, y))} − "
                     f"{tl(x(a, p))}) ÷ {tl(x(a, p))} × 100 = {bicimle(d, 'yuzde')}.")

    def degisim_tutar(self, a, y):
        x = self.x
        y = str(y)
        p = self.onceki(y)
        d = x(a, y) - x(a, p)
        return Hesap(d, "tutar", [x(a, y) - x(a, self.yillar[0]), d / 2, x(a, y), x(a, p), d * 2],
                     f"{self.ad} karşılaştırmalı analizinde {self.adi(a)} {p}-{y} değişim tutarı = {tl(x(a, y))} − "
                     f"{tl(x(a, p))} = {tl(d)} ₺.")


def grafik(sid, ad, baslik, labels, seriler, alt, aciklama):
    """Grafik uyaranı (uygulama çizgi grafiği olarak çizer; altText erişilebilirlik açıklamasıdır)."""
    return {"id": sid, "title": f"{ad} — {baslik}", "kind": "graph", "bodyMarkdown": aciklama,
            "chart": {"labels": list(labels), "series": [{"name": n, "values": list(v)} for n, v in seriler],
                      "altText": alt},
            "caption": "Grafiği yorumlayarak soruyu cevaplayınız."}


# ============================================================================ kök kalıpları
# Aynı ölçü farklı şirketlerde sorulduğunda kökler sözcük düzeyinde de ayrışsın diye (audit yakın-tekrar
# denetimi) üç kalıp dönüşümlü kullanılır.
ONEK = ("{ad}’nin", "Tablolara göre {ad}’nin", "{ad} verilerine göre", "{ad} tablolarına göre")
SONEK = {"oran": ("aşağıdakilerden hangisidir?", "kaçtır?", "hangi değeri alır?"),
         "kat": ("aşağıdakilerden hangisidir?", "kaçtır?", "hangi değeri alır?"),
         "yuzde": ("yüzde (%) kaçtır?", "yüzde (%) kaç olarak hesaplanır?", "yüzde (%) kaç olur?"),
         "gun": ("kaç gündür?", "kaç gün olarak hesaplanır?", "kaç gün olur?"),
         "tutar": ("kaç ₺’dir?", "kaç ₺ olarak hesaplanır?", "kaç ₺ olur?")}


IFADE = {
    "cari": "{y} yılı cari oranı", "likidite": "{y} yılı likidite (asit-test) oranı", "nakit_orani": "{y} yılı nakit oranı",
    "nis": "{y} yılı net işletme sermayesi", "stok_hiz": "{y} yılı stok devir hızı",
    "stok_sure": "{y} yılı ortalama stok devir süresi", "alacak_hiz": "{y} yılı ticari alacak devir hızı",
    "alacak_sure": "{y} yılı ortalama ticari alacak tahsil süresi",
    "borc_sure": "{y} yılı ortalama ticari borç ödeme süresi", "aktif_hiz": "{y} yılı aktif (varlık) devir hızı",
    "dv_hiz": "{y} yılı dönen varlık devir hızı", "brut_marj": "{y} yılı brüt satış kârlılığı oranı",
    "faal_marj": "{y} yılı faaliyet kârlılığı oranı", "net_marj": "{y} yılı net kâr marjı",
    "varlik_karl": "{y} yılı varlıkların kârlılığı oranı", "ozk_karl": "{y} yılı öz kaynak kârlılığı oranı",
    "kaldirac": "{y} yılı kaldıraç oranı", "ozk_oran": "{y} yılı öz kaynakların aktif toplamına oranı",
    "ds_oran": "{y} yılı devamlı sermaye oranı (pasif toplamına göre)",
    "borc_ozk": "{y} yılı yabancı kaynaklarının öz kaynaklarına oranı",
    "satis_nakit": "{y} yılında satışlardan sağladığı nakit girişi",
    "alim_nakit": "{y} yılında mal alımları için yaptığı nakit çıkışı",
}


def kok(ad, ifade, bicim, v):
    return f"{ONEK[v % 4].format(ad=ad)} {ifade} {SONEK[bicim][v % 3]}"


# ============================================================================ paket sarmalayıcı
class Fta:
    """Sayısal soruların doğru şık sırasını dengeli planlar; ortak tabloları stimuli.json'a yazar."""

    def __init__(self, P, onek):
        self.P, self.onek = P, onek
        self.ogeler = []
        self.uyaranlar = []
        self.rng = random.Random(P.seed + 7)

    def uyaran(self, u):
        assert u["id"].startswith(self.onek), u["id"]
        assert all(x["id"] != u["id"] for x in self.uyaranlar)
        self.uyaranlar.append(u)
        return u["id"]

    def ifade(self, sirket, sid, h, ifade, v, ref, **kw):
        """Ortak tabloya bağlı, ölçü ifadesi elle verilen soru (dikey, trend, karşılaştırmalı, nakit).
        `ifade` bir dize ya da dize listesi olabilir; liste verilirse 12 soruda bir sonraki kalıba geçilir."""
        self.sayac = getattr(self, "sayac", 0) + 1
        k = v + self.sayac
        if not isinstance(ifade, str):
            ifade = ifade[(k // 12) % len(ifade)]
        self.hesap(ref, kok(sirket.ad, ifade, h.bicim, k), h, stimulus_id=sid, **kw)

    def olcu(self, sirket, sid, metrik, yil, v, ref, **kw):
        """Ortak tabloya bağlı tek ölçü sorusu: kök kalıbı, hesap ve çözüm şirketten türetilir."""
        h = getattr(sirket, metrik)(str(yil))
        # Aynı şirketin art arda gelen soruları da farklı kalıpla kurulur (v: şirket ofseti + sıra).
        self.sayac = getattr(self, "sayac", 0) + 1
        stem = kok(sirket.ad, IFADE[metrik].format(y=yil), h.bicim, v + self.sayac)
        self.hesap(ref, stem, h, stimulus_id=sid, **kw)

    def hesap(self, ref, stem, h, **kw):
        self.ogeler.append(("h", ref, stem, h, kw))

    def q(self, *a, **kw):
        self.ogeler.append(("q", a, kw))

    def sayisal(self, *a, **kw):
        self.ogeler.append(("s", a, kw))

    def oncul(self, *a, **kw):
        self.ogeler.append(("o", a, kw))

    def _dizi(self, n):
        """Dengeli, üçlü tekrarsız harf dizisi. Sıralı sayısal şıklarda eşit boylu şıklar arasında kör öğrencinin
        'en uzun/en kısa' stratejisi uçtaki harflere (A, E) düşer; bu yüzden A ve E olabildiğince serbest şıklı
        sorulara bırakılır (serbest soruların harfini Paket kalan havuzdan yeniden dağıtır)."""
        harf = [h for h in "ABCDE" for _ in range(n // 5)] + list("ABCDE"[: n % 5])
        sabit = [t in ("h", "s") for t, *_ in self.ogeler]
        en_iyi = None
        for _ in range(4000):
            self.rng.shuffle(harf)
            s = "".join(harf)
            if any(s[i] == s[i + 1] == s[i + 2] for i in range(len(s) - 2)):
                continue
            if any(l == "FATAL" for l, *_ in audit.letter_pattern(s)):
                continue
            puan = sum(1 for c, sb in zip(s, sabit) if sb and c in "AE")
            if en_iyi is None or puan < en_iyi[0]:
                en_iyi = (puan, s)
        if en_iyi is None:
            raise SystemExit("harf dizisi kurulamadı")
        return en_iyi[1]

    def bitir(self):
        dizi = self._dizi(len(self.ogeler))
        for (tur, *geri), harf in zip(self.ogeler, dizi):
            if tur == "h":
                ref, stem, h, kw = geri
                dogru, cel = secenekler_sirali(h, "ABCDE".index(harf), self.rng)
                self.P.sayisal(ref, stem, dogru, cel, kw.pop("cozum", h.cozum), **kw)
            elif tur == "q":
                a, kw = geri
                self.P.q(*a, **kw)
            elif tur == "s":
                a, kw = geri
                self.P.sayisal(*a, **kw)
            else:
                a, kw = geri
                self.P.oncul(*a, **kw)

    def yaz(self, argv=None):
        argv = sys.argv[1:] if argv is None else argv
        self.bitir()
        mevcut = json.load(open(STIMULI, encoding="utf-8"))
        yeni = [u for u in mevcut if not u["id"].startswith(self.onek)]
        for u in self.uyaranlar:
            yeni.append({**u, "updatedAt": f"{self.P.kontrol}T00:00:00Z"})
        tarihsiz = lambda L: [{k: v for k, v in u.items() if k != "updatedAt"} for u in L]  # noqa: E731
        eski = {u["id"]: u for u in mevcut}
        # İçeriği değişmeyen uyaranın tarihi korunur.
        for u in yeni:
            e = eski.get(u["id"])
            if e and tarihsiz([e]) == tarihsiz([u]):
                u["updatedAt"] = e.get("updatedAt", u["updatedAt"])
        # Dosya kimliğe göre sıralı tutulur: builder'ların çalışma sırası içeriği değiştirmesin (--check deterministik).
        yeni.sort(key=lambda u: u["id"])
        ayni = tarihsiz(mevcut) == tarihsiz(yeni)
        if "--check" in argv:
            if not ayni:
                print(f"FARKLI: stimuli.json ({self.onek}*)")
                return 1 | self.P.yaz(argv)
            return self.P.yaz(argv)
        if not ayni:
            metin = json.dumps(yeni, ensure_ascii=False, indent=2) + "\n"
            open(STIMULI, "w", encoding="utf-8").write(metin)
            if os.path.isdir(APP):
                open(os.path.join(APP, "stimuli.json"), "w", encoding="utf-8").write(metin)
        return self.P.yaz(argv)
