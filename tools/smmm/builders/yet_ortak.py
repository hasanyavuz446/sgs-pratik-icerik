# -*- coding: utf-8 -*-
"""SMMM Yeterlilik paket üreticisi — tasarım anında kalite kapıları.

Her paket builder'ı bu modülü kullanır; kusurlar JSON yazılmadan ÖNCE yakalanır:

    from yet_ortak import Paket
    P = Paket("questions_topic_disiplin_2026.json", lesson="meslek_hukuku",
              topic="disiplin", konu_adi="Disiplin", seed=20260928,
              surum="3568 s. Kanun ve TÜRMOB Disiplin Yönetmeliği, 28.09.2026 kontrolü")
    P.q("3568 s. Kanun m. 48", "3568 sayılı Kanun’a göre, … biri değildir?",
        "doğru şık", ["çeldirici 1", "çeldirici 2", "çeldirici 3", "çeldirici 4"],
        "Çözüm …", zorluk="medium")
    P.oncul(...)   # öncüllü soru: seçici şıklar gerçek sınavdaki gibi sabit sırada
    P.sayisal(...) # sayısal şıklar gerçek sınavdaki gibi artan sırada
    P.yaz()        # kapılar + JSON (içerik ve uygulama deposu) ; --check ile karşılaştırır

Kapılar (hepsi DURDURUR):
  · şıkta mutlak dil (ELEME_ISARETI) · çözümde harf atfı · tekrar eden şık
  · §5 boy: doğru şık tek-en-uzun ya da tek-en-kısa oranı > 1/3
  · kör öğrenci ≥ %32 (hedef ≤ %30)
  · paket sadakati: olumsuz kök ve mevzuat atfı gerçek sınav bandının dışında (FATAL)
  · audit.py sonucu FATAL
Kimlikler mevcut dosyadan alınır (uygulama silinen soruyu telefondan silmez; aynı
kimliğin üzerine yazmak eski sürümü temizler).
"""
import argparse
import collections
import datetime as dt
import itertools
import json
import os
import random
import re
import shutil
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
APP = os.path.abspath(os.path.join(ROOT, "..", "smmm_sgs_pratik", "assets", "content", "yeterlilik"))
sys.path.insert(0, os.path.join(ROOT, "tools", "smmm", "audit"))
import audit  # noqa: E402
import profil  # noqa: E402

SECICI = re.compile(r"^(Yalnız\s+)?(I{1,3}|IV|V)(\s*(,|ve)\s*(I{1,3}|IV|V))*$")
HARF_ATFI = re.compile(r"(?<![/\w])[A-E]\)|\b[A-E]\s+şıkkı|\bşık(?:kı)?\s+[A-E]\b|\*\*[A-E]\s+(?:yanlış|doğru)")
SAYI = re.compile(r"-?[\d.]+(?:,\d+)?")


def sayi_degeri(metin):
    m = SAYI.search(metin.replace("−", "-"))
    if not m:
        raise ValueError(f"sayısal şık değil: {metin!r}")
    return float(m.group(0).replace(".", "").replace(",", "."))


class Paket:
    def __init__(self, dosya, *, lesson, topic, konu_adi, seed, surum,
                 havuz="konu", kontrol=None, style="2026 SMMM beş seçenekli test"):
        assert havuz in ("konu", "bolum")
        self.dosya = dosya
        self.lesson, self.topic, self.konu_adi = lesson, topic, konu_adi
        self.seed, self.surum, self.havuz, self.style = seed, surum, havuz, style
        self.kontrol = kontrol or dt.date.today().isoformat()
        self.S = []

    # ------------------------------------------------------------------ girdi
    def _ortak(self, ref, stem, cozum, zorluk, lesson, topic, stimulus_id):
        assert zorluk in ("easy", "medium", "hard"), zorluk
        assert ref and len(ref) >= 6, f"dayanak zayıf: {ref!r}"
        assert not HARF_ATFI.search(cozum), f"çözümde harf atfı: {stem[:60]}"
        assert len(cozum) >= 60, f"çözüm kısa: {stem[:60]}"
        return dict(ref=ref, stem=stem.strip(), cozum=cozum.strip(), zorluk=zorluk,
                    lesson=lesson or self.lesson, topic=topic or self.topic, stimulus_id=stimulus_id)

    def _siklar_denetle(self, stem, siklar):
        assert len(siklar) == 5 and len(set(siklar)) == 5, f"5 farklı şık yok: {stem[:60]}"
        for s in siklar:
            assert s.strip() == s and s, f"boş/boşluklu şık: {stem[:60]}"
            m = audit.ELEME_ISARETI.search(s)
            assert not m, f"MUTLAK DİL '{m.group(0)}' şıkta: {s[:70]} | kök: {stem[:50]}"

    def q(self, ref, stem, dogru, celdiriciler, cozum, *, zorluk="medium",
          lesson=None, topic=None, stimulus_id=None):
        """Serbest şıklı soru: doğru şıkkın harfi dengeli dağıtılır."""
        assert len(celdiriciler) == 4, f"4 çeldirici gerekli: {stem[:60]}"
        self._siklar_denetle(stem, [dogru, *celdiriciler])
        d = self._ortak(ref, stem, cozum, zorluk, lesson, topic, stimulus_id)
        d.update(tur="serbest", dogru=dogru, celdirici=list(celdiriciler))
        self.S.append(d)

    def sayisal(self, ref, stem, dogru, celdiriciler, cozum, **kw):
        """Sayısal şıklar gerçek sınavdaki gibi artan sırada dizilir; harf değerden çıkar."""
        assert len(celdiriciler) == 4
        siklar = [dogru, *celdiriciler]
        self._siklar_denetle(stem, siklar)
        degerler = [sayi_degeri(s) for s in siklar]
        assert len(set(degerler)) == 5, f"eşit sayısal şık: {stem[:60]}"
        sirali = [s for _, s in sorted(zip(degerler, siklar))]
        d = self._ortak(ref, stem, kw.pop("cozum", cozum), kw.pop("zorluk", "medium"),
                        kw.pop("lesson", None), kw.pop("topic", None), kw.pop("stimulus_id", None))
        assert not kw, kw
        d.update(tur="sabit", siklar=sirali, dogru=dogru)
        self.S.append(d)

    def oncul(self, ref, giris, onculler, soru, dogru_kume, secenekler, cozum, **kw):
        """Öncüllü soru. onculler: ["…", "…", …]; dogru_kume: "II ve III" gibi.
        secenekler: 5 seçici, gerçek sınavdaki gibi yazıldığı sırayla (A→E)."""
        assert 3 <= len(onculler) <= 6
        assert dogru_kume in secenekler and len(secenekler) == 5
        for s in secenekler:
            assert SECICI.match(s), f"seçici biçimi: {s}"
        romen = ["I", "II", "III", "IV", "V", "VI"]
        govde = "\n\n".join(f"{romen[i]}. {o}" for i, o in enumerate(onculler))
        stem = (giris.strip() + "\n\n" if giris else "") + govde + "\n\n" + soru.strip()
        self._siklar_denetle(stem, list(secenekler))
        d = self._ortak(ref, stem, cozum, kw.pop("zorluk", "medium"),
                        kw.pop("lesson", None), kw.pop("topic", None), kw.pop("stimulus_id", None))
        assert not kw, kw
        d.update(tur="sabit", siklar=list(secenekler), dogru=dogru_kume, oncul=True)
        self.S.append(d)

    # ------------------------------------------------------------------ harfler
    def _harfler(self):
        n = len(self.S)
        sabit = {i: "ABCDE"[s["siklar"].index(s["dogru"])] for i, s in enumerate(self.S) if s["tur"] == "sabit"}
        hedef = collections.Counter({h: n // 5 for h in "ABCDE"})
        for h in "ABCDE"[: n % 5]:
            hedef[h] += 1
        rng = random.Random(self.seed)
        for _ in range(20000):
            kalan = hedef.copy()
            kalan.subtract(sabit.values())
            havuz = []
            for h, c in kalan.items():
                havuz += [h] * max(c, 0)
            # Sabit harfler bir harfin hedefini aştıysa kalan (pozitif) havuz serbest
            # soru sayısından uzundur; karıştırıp keserek fazlayı rastgele düşür.
            rng.shuffle(havuz)
            havuz = havuz[: n - len(sabit)]
            it = iter(havuz)
            seq = [sabit[i] if i in sabit else next(it) for i in range(n)]
            s = "".join(seq)
            if re.search(r"(.)\1\1", s):
                continue
            if any(lvl == "FATAL" for lvl, *_ in audit.letter_pattern(s)):
                continue
            return seq
        raise SystemExit("harf dizisi kurulamadı (sabit harfler çok yığılmış olabilir)")

    # ------------------------------------------------------------------ çıktı
    def _mevcut_idler(self):
        yol = os.path.join(ROOT, "content", "yeterlilik", self.dosya)
        if not os.path.exists(yol):
            return None
        return [q["id"] for q in json.load(open(yol, encoding="utf-8"))]

    def sorular(self, idler=None):
        idler = idler or self._mevcut_idler()
        assert idler and len(idler) == len(self.S), (
            f"{self.dosya}: mevcut {len(idler or [])} kimlik, tasarım {len(self.S)} soru")
        harf = self._harfler()
        zaman = f"{self.kontrol}T00:00:00Z"
        etiket_havuz = "Konu Havuzu" if self.havuz == "konu" else "Bölüm Havuzu"
        out = []
        for i, (s, h) in enumerate(zip(self.S, harf)):
            if s["tur"] == "sabit":
                choices = dict(zip("ABCDE", s["siklar"]))
                assert choices[h] == s["dogru"]
            else:
                choices = {h: s["dogru"]}
                for k, v in zip([k for k in "ABCDE" if k != h], s["celdirici"]):
                    choices[k] = v
                choices = {k: choices[k] for k in "ABCDE"}
            q = {
                "id": idler[i],
                "lessonId": s["lesson"],
                "topicId": s["topic"],
                "question": s["stem"],
                "choices": choices,
                "correctAnswer": h,
                "explanation": s["cozum"],
                "source": {"kind": "generated", "styleRef": self.style, "legislationRef": s["ref"]},
                "tags": ["Özgün Soru", "2026 Formatı", etiket_havuz, self.konu_adi],
                "difficulty": s["zorluk"],
                "updatedAt": zaman,
                "examPeriod": "2026 test sistemine uyumlu özgün soru",
                "legislationVersion": self.surum,
                "sourceUpdatedAt": zaman,
                "isPremium": False,
                "isActive": True,
            }
            if s["stimulus_id"]:
                q["stimulusId"] = s["stimulus_id"]
            out.append(q)
        return out

    def kapilar(self, sorular):
        rapor = []
        # §5 boy (öncüllü ve sabit sıralı hariç)
        olcum = [s for s in self.S if s["tur"] == "serbest"]
        if olcum:
            uzun = sum(len(s["dogru"]) > max(map(len, s["celdirici"])) for s in olcum)
            kisa = sum(len(s["dogru"]) < min(map(len, s["celdirici"])) for s in olcum)
            rapor.append(f"boy: tek-en-uzun {uzun}/{len(olcum)} · tek-en-kısa {kisa}/{len(olcum)}")
            # İki uç da kural öğretir: "en uzunu seç" kadar "en uzunu asla seçme" de ipucudur.
            if len(olcum) >= 20 and min(uzun, kisa) / len(olcum) < 0.08:
                raise SystemExit(f"§5 TEK YÖNLÜ DAĞILIM {self.dosya}: " + rapor[-1] + " (iki uç da ≥%8 olmalı)")
            if len(olcum) >= 12 and (uzun / len(olcum) > 0.25 or kisa / len(olcum) > 0.25):  # audit UYARI eşiği
                for s in olcum:
                    if len(s["dogru"]) > max(map(len, s["celdirici"])):
                        print("   UZUN:", s["dogru"][:70])
                raise SystemExit(f"§5 BOY TUZAĞI {self.dosya}: " + rapor[-1])
            # ortalama uzunluk sırası (1=en kısa … 5=en uzun); audit 2,4–3,6 dışını uyarır
            sira = []
            for s in olcum:
                d, c = len(s["dogru"]), list(map(len, s["celdirici"]))
                sira.append(1 + sum(x < d for x in c) + sum(x == d for x in c) / 2)
            ort = sum(sira) / len(sira)
            rapor.append(f"ortalama uzunluk sırası {ort:.2f}/5")
            if len(olcum) >= 15 and not 2.45 <= ort <= 3.55:
                raise SystemExit(f"§5 SIRA EĞİLİMİ {self.dosya}: ortalama {ort:.2f}/5 (hedef 3 çevresi)")
        # öncül seçici dağılımı
        sec = collections.Counter(s["dogru"] for s in self.S if s.get("oncul"))
        if sum(sec.values()) >= 4:
            assert sec.most_common(1)[0][1] / sum(sec.values()) <= 0.4, f"öncül yığılması {sec}"
        # kör öğrenci
        rows = [(q["choices"], q["correctAnswer"]) for q, s in zip(sorular, self.S) if not s.get("oncul")]
        kor, strateji = audit.kor_ogrenci(rows)
        rapor.append(f"kör öğrenci %{kor} ({strateji})")
        if len(rows) >= 20 and kor >= 32:
            raise SystemExit(f"KÖR ÖĞRENCİ %{kor} ({strateji}) — {self.dosya}")
        # profil
        olc = [profil.olc(q["question"], q["choices"], stimulus_id=q.get("stimulusId")) for q in sorular]
        oz = profil.ozet(olc)
        rapor.append("profil: kök {} · olumsuz %{:.0f} · atıf %{:.0f} · öncül %{:.0f} · sayısal %{:.0f} · veri %{:.0f}".format(
            oz["kok_medyan"], oz["olumsuz"] * 100, oz["atif"] * 100, oz["oncul"] * 100,
            oz["sayisal_sik"] * 100, oz["veri"] * 100))
        return rapor

    def yaz(self, argv=None):
        ap = argparse.ArgumentParser()
        ap.add_argument("--check", action="store_true", help="yazmadan karşılaştır")
        args = ap.parse_args(argv)
        sorular = self.sorular()
        rapor = self.kapilar(sorular)
        metin = json.dumps(sorular, ensure_ascii=False, indent=2) + "\n"
        hedef = os.path.join(ROOT, "content", "yeterlilik", self.dosya)
        if args.check:
            mevcut = open(hedef, encoding="utf-8").read() if os.path.exists(hedef) else ""
            if mevcut != metin:
                print(f"FARKLI: {self.dosya}")
                return 1
            print(f"aynı: {self.dosya}")
            return 0
        with open(hedef, "w", encoding="utf-8") as f:
            f.write(metin)
        if os.path.isdir(APP):
            shutil.copyfile(hedef, os.path.join(APP, self.dosya))
        n, oncul, sorunlar = audit.audit(hedef)
        sev = collections.Counter(x[0] for x in sorunlar)
        print(f"yazıldı: {self.dosya} ({n} soru, öncüllü {oncul})")
        for r in rapor:
            print("  ", r)
        for lvl, kod, msg in sorunlar:
            if lvl in ("FATAL", "UYARI"):
                print(f"   [{lvl}] {kod}: {msg}")
        print(f"   audit: FATAL {sev['FATAL']} · UYARI {sev['UYARI']}")
        return 1 if sev["FATAL"] else 0
