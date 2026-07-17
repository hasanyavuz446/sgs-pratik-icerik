#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ticaret Hukuku paketlerindeki şık-boy ipucunu doğal seçeneklerle giderir."""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
APP = ROOT.parent / "smmm_sgs_pratik" / "assets" / "content"


CORRECT = {
    "ticaret_hukuku/ticari_isletme_tacir.json": {
        "tic-isletme-gen-0002": "Mutlaka anonim veya limited şirket biçiminde kurulması",
        "tic-isletme-gen-0015": "Tescil ve ilan edilen hususların bilinmediği üçüncü kişilerce ileri sürülemez",
        "tic-isletme-gen-0016": "Tacirin ticari işlemlerde kullandığı ve imzaladığı ad",
    },
    "ticaret_hukuku/kiymetli_evrak.json": {
        "tic-kiymetli-gen-0006": "Yazılı temlik ve senedin teslimiyle",
        "tic-kiymetli-gen-0011": "Muhatap kabul imzasıyla poliçenin asıl borçlusu olur",
        "tic-kiymetli-gen-0016": "Çek ödeme aracıdır ve kural olarak görüldüğünde ödenir",
        "tic-kiymetli-gen-0017": "Çek kabule sunulamaz; kabul kaydı yazılmamış sayılır",
        "tic-kiymetli-gen-0021": "Hakkı ciro edilene mülkiyetiyle geçiren tam ciro",
    },
    "ticaret_hukuku/haksiz_rekabet.json": {
        "hakrek-gen-0002": "Aldatıcı veya dürüstlüğe aykırı ticari uygulamalar haksız rekabettir",
        "hakrek-gen-0006": "Başkalarını veya ürünlerini yanlış, yanıltıcı ya da gereksiz incitici açıklamalarla kötülemek",
        "hakrek-gen-0007": "Kendisini, işletmesini veya malını yanıltıcı açıklamalarla öne çıkarmak haksız rekabettir",
        "hakrek-gen-0008": "Başkasının malı, ürünü veya işletmesiyle karıştırılmaya yol açan önlem almak",
        "hakrek-gen-0009": "Sahip olunmayan unvan, diploma veya ödülle üstünlük sağlamaya çalışmak",
        "hakrek-gen-0010": "Maliyetin altındaki seçilmiş mallarla müşteri ve rakipleri yanıltmak haksız rekabet olabilir",
        "hakrek-gen-0011": "Saldırgan satış yöntemiyle müşterinin karar özgürlüğünü sınırlamak haksız rekabettir",
        "hakrek-gen-0013": "Ek edimin gerçek değeri konusunda müşteriyi yanıltmak haksız rekabet olabilir",
        "hakrek-gen-0014": "Çalışanı işvereninin üretim veya iş sırrını açıklamaya yöneltmek haksız rekabettir",
        "hakrek-gen-0015": "Müşteriyi sözleşmeye aykırılığa veya haksız feshe yöneltmek haksız rekabettir",
        "hakrek-gen-0016": "Emanet edilen teklif, hesap veya plandan yetkisiz yararlanmak haksız rekabettir",
        "hakrek-gen-0017": "Hukuka aykırı edinilen üretim veya iş sırrını kullanmak ya da açıklamak haksız rekabettir",
        "hakrek-gen-0018": "Ortak iş şartlarına uymamak veya dürüstlüğe aykırı şart kullanmak haksız rekabettir",
        "hakrek-gen-0020": "Tespit davası, davranışın haksız rekabet niteliğini belirler",
        "hakrek-gen-0021": "Men davası, haksız rekabet fiilinin durdurulmasını amaçlar",
        "hakrek-gen-0022": "Düzeltme davası, haksız rekabetin doğurduğu maddi durumu giderir",
        "hakrek-gen-0023": "Zarar gören, fail kusurluysa maddi zararının tazminini isteyebilir",
        "hakrek-gen-0024": "Koşulları varsa manevi tazminata ve failin kazancının devrine karar verilebilir",
        "hakrek-gen-0027": "Müşterisi, kredisi veya ticari itibarı zarar gören kişi dava açabilir",
        "hakrek-gen-0029": "Dava, öğrenmeden bir ve her hâlde fiilin doğumundan üç yıl sonra zamanaşımına uğrar",
        "hakrek-gen-0030": "Mahkeme, kazananın talebiyle ve karşı tarafın gideriyle kararın ilanına hükmedebilir",
        "hakrek-gen-0031": "Kanundaki fiiller, hak sahibinin şikâyeti üzerine cezai yaptırıma tabi olabilir",
        "hakrek-gen-0032": "Hak sahibi mahkemeden haksız rekabeti önleyici ihtiyati tedbir isteyebilir",
        "hakrek-gen-0034": "(A)'nın kötülemesi haksız rekabettir; (B) tespit, men ve düzeltme davaları açabilir",
        "hakrek-gen-0035": "(C)'nin iltibasa yol açan davranışı haksız rekabettir; (D) hukuki dava açabilir",
        "hakrek-gen-0036": "(E)'nin çalışanı iş sırrını açıklamaya yöneltmesi haksız rekabettir",
        "hakrek-gen-0037": "Öğrenmeden itibaren bir yıl geçtiği için zamanaşımı def'i davayı sonuçsuz bırakabilir",
        "hakrek-gen-0038": "Çalışanın görevdeki fiili nedeniyle (H), istihdam eden (G)'ye de dava açabilir",
        "hakrek-gen-0039": "(K)'nin sahip olmadığı ödülü kullanması haksız rekabettir; zarar görenler dava açabilir",
        "hakrek-gen-0040": "Kusur olmasa da tespit, men ve düzeltme davaları açılabilir",
        "hakrek-gen-0050": "(N)'nin yanıltıcı ve rakipleri dışlayıcı maliyet altı satışı haksız rekabet oluşturabilir",
        "hakrek-gen-0051": "Asılsız kötüleme haksız rekabettir; zarar gören rakip dava açabilir",
        "hakrek-gen-0052": "Kişilik hakkı zedelenmişse haksız rekabet nedeniyle manevi tazminat istenebilir",
        "hakrek-gen-0059": "Hükümler, dürüst rekabeti etkileyen davranışlara katılan herkesi kapsar",
    },
    "ticaret_hukuku/anonim_sirket.json": {
        "as-gen-0001": "Anonim şirket, paylara bölünmüş sermayesi bulunan ve borçlarından malvarlığıyla sorumlu şirkettir",
        "as-gen-0002": "Pay sahibi taahhüt ettiği sermayeyle sınırlı olup şirket borcundan şahsen sorumlu değildir",
        "as-gen-0003": "Anonim şirkette sermaye ön plandadır ve paylar kural olarak serbestçe devredilebilir",
        "as-gen-0004": "Esas sermaye kanuni asgari tutardan az olamaz ve paylara bölünür",
        "as-gen-0006": "Şirket, esas sözleşmenin düzenlenmesi ve ticaret siciline tescille tüzel kişilik kazanır",
        "as-gen-0007": "Esas sözleşme yazılı olup imzalar noter onaylı veya sicil müdürü huzurunda olmalıdır",
        "as-gen-0008": "Anonim şirket tek pay sahibiyle kurulabilir ve tek ortaklı olarak sürebilir",
        "as-gen-0009": "Nakdi payın kanuni kısmı tescilden önce, kalanı kanuni süresinde ödenir",
        "as-gen-0012": "Genel kurul, pay sahiplerinin şirket iradesini oluşturduğu en üst karar organıdır",
        "as-gen-0013": "Esas sözleşme değişikliği ve yönetim seçimi genel kurulun devredilemez yetkisidir",
        "as-gen-0014": "Olağan genel kurul faaliyet dönemi sonundan itibaren ilk üç ayda toplanır",
        "as-gen-0016": "Pay sahibi genel kurulda kural olarak paylarının sağladığı oy hakkını kullanır",
        "as-gen-0018": "Yönetim kurulu şirketi yönetir ve üçüncü kişilere karşı temsil eder",
        "as-gen-0019": "Yönetim kurulu esas sözleşmeyle atanmış veya genel kurulca seçilmiş kişilerden oluşur",
        "as-gen-0020": "Tüzel kişi yönetim kuruluna üye olabilir; belirlediği gerçek kişi toplantıya katılır",
        "as-gen-0022": "Üst yönetim ve muhasebe düzenini kurmak yönetim kurulunun devredilemez görevidir",
        "as-gen-0027": "Sermaye artırımında pay sahibinin payı oranında rüçhan hakkı vardır",
        "as-gen-0028": "Pay sahibi dağıtım kararı verilen net dönem kârından payı oranında kâr payı alır",
        "as-gen-0030": "Esas sermaye artırımı genel kurul kararı ve kanuni usulle yapılır",
        "as-gen-0031": "Sermaye azaltımında kanuni usulle alacaklıların hakları güvenceye alınır",
        "as-gen-0032": "Kanuni ölçütleri taşıyan anonim şirketler bağımsız denetime tabidir",
        "as-gen-0033": "Şirket süre bitimi, amaç imkânsızlığı, genel kurul kararı veya iflasla sona erebilir",
        "as-gen-0034": "Sermaye borcunu ödeyen pay sahibinin şahsi malvarlığına şirket borcu için başvurulamaz",
        "as-gen-0035": "Yönetim kurulu üyelerini seçme yetkisi genel kurulun devredilemez yetkisidir",
        "as-gen-0038": "Genel kurulu toplantıya çağırmak kural olarak yönetim kurulunun görevidir",
    },
    "ticaret_hukuku/limited_sahis_sirketleri.json": {
        "ltd-gen-0003": "Ortaklar şirket borcundan değil, yalnız taahhüt ettikleri sermaye payını ödemekten sorumludur",
        "ltd-gen-0009": "Pay devri yazılı ve onaylı sözleşmeyle, kural olarak genel kurul onayıyla yapılır",
        "ltd-gen-0011": "Esas sözleşme ortaklara para dışı yan edim yükümlülüğü getirebilir",
        "ltd-gen-0013": "Bir pay birden çok kişiye aitse haklar şirkete karşı ortak temsilciyle kullanılır",
        "ltd-gen-0014": "Pay, miras, mal rejimi veya cebri icrayla kanundaki özel hükümlere göre geçebilir",
        "ltd-gen-0017": "Yönetim ve temsil müdürlere aittir; en az bir ortak bu yetkiyi taşımalıdır",
        "ltd-gen-0019": "Müdürler şirkete bağlıdır ve genel kurul izni olmadan şirketle rekabet edemez",
        "ltd-gen-0021": "Aksi yoksa genel kurul kararı temsil edilen oyların salt çoğunluğuyla alınır",
        "ltd-gen-0022": "Müdürler özenle ve şirket menfaatini dürüstlükle gözeterek görev yapmalıdır",
        "ltd-gen-0024": "Kollektif şirket gerçek kişilerce ticari işletme için kurulur; ortakların sorumluluğu sınırsızdır",
        "ltd-gen-0027": "Alacaklı ortağın malvarlığına ancak alacağını şirketten alamazsa başvurabilir",
        "ltd-gen-0029": "Aksi kararlaştırılmadıkça her ortak şirketi ayrı ayrı yönetebilir",
        "ltd-gen-0030": "Ortak, izin olmadan şirket konusu işi kendi veya başkası hesabına yapamaz",
        "ltd-gen-0031": "Pay devri ve yeni ortak kabulü kural olarak tüm ortakların onayını gerektirir",
        "ltd-gen-0033": "Kâr ve zarar sözleşmeye, hüküm yoksa kanuni esasa göre paylaşılır",
        "ltd-gen-0035": "Komandite sınırsız, komanditer koyduğu sermayeyle sınırlı sorumludur",
        "ltd-gen-0037": "Komanditerin sorumluluğu koyduğu sermayeyle sınırlıdır; gerçek veya tüzel kişi olabilir",
    },
}


DISTRACTORS = {
    "ticaret_hukuku/ticari_isletme_tacir.json": {
        "tic-isletme-gen-0012": {"A": "Sulh hukuk mahkemesi"},
    },
    "ticaret_hukuku/kambiyo_senetleri.json": {
        "kmb-gen-0001": {"B": "Yalnız ispat aracı olan sıradan bir belgedir"},
        "kmb-gen-0002": {"A": "Poliçe, bono, çek, hisse senedi ve tahvil"},
        "kmb-gen-0006": {"C": "Geçersizlik yalnız sonraki cirantaları sorumsuz bırakır"},
        "kmb-gen-0010": {"A": "Yalnız düzenleyen ve lehtar vardır"},
        "kmb-gen-0012": {"B": "Vadesiz poliçe kesin olarak geçersizdir"},
        "kmb-gen-0014": {"B": "Poliçede kabul kurumu yoktur"},
        "kmb-gen-0024": {"A": "Düzenleyen senedi verince sorumluluktan kurtulur"},
        "kmb-gen-0026": {"A": "Vadesiz bono kesin olarak geçersizdir"},
    },
    "ticaret_hukuku/limited_sahis_sirketleri.json": {
        "ltd-gen-0005": {"B": "Yalnız gerçek kişiler ortak olabilir"},
        "ltd-gen-0011": {"A": "Yan edim yükümlülüğü kararlaştırılamaz"},
        "ltd-gen-0012": {"A": "Limited şirkette pay defteri tutulmaz"},
        "ltd-gen-0017": {"A": "Yönetim ve temsil yalnız genel kurula aittir"},
        "ltd-gen-0022": {"D": "Özen borcu ancak sözleşmeyle doğar"},
        "ltd-gen-0025": {"A": "Tüzel kişiler de ortak olabilir"},
        "ltd-gen-0026": {"A": "Ortakların sorumluluğu sermaye paylarıyla sınırlıdır"},
        "ltd-gen-0029": {"B": "Yalnız sermayesi en yüksek ortak yönetebilir"},
        "ltd-gen-0030": {"C": "Yasak yalnız yönetici ortağı bağlar"},
        "ltd-gen-0033": {"A": "Kâr sadece yönetici ortağa aittir"},
        "ltd-gen-0035": {"A": "Bütün ortaklar sınırlı sorumludur"},
        "ltd-gen-0039": {"A": "Kişisel emek sermaye olarak konulabilir"},
    },
}


def fix(rel: str) -> int:
    source = ROOT / "content" / rel
    data = json.loads(source.read_text(encoding="utf-8"))
    by_id = {q["id"]: q for q in data}
    changed = 0
    for qid, new in CORRECT.get(rel, {}).items():
        q = by_id[qid]
        if q["options"][q["answer"]] != new:
            q["options"][q["answer"]] = new
            changed += 1
    for qid, replacements in DISTRACTORS.get(rel, {}).items():
        q = by_id[qid]
        for letter, new in replacements.items():
            assert letter != q["answer"], qid
            if q["options"][letter] != new:
                q["options"][letter] = new
                changed += 1
    for q in data:
        assert set(q["options"]) == set("ABCDE"), q["id"]
        assert len(set(q["options"].values())) == 5, q["id"]
    payload = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    source.write_text(payload, encoding="utf-8")
    target = APP / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(payload, encoding="utf-8")
    return changed


if __name__ == "__main__":
    for rel in sorted(set(CORRECT) | set(DISTRACTORS)):
        print(f"{rel}: {fix(rel)} doğal şık düzeltmesi")
