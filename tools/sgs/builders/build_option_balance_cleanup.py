#!/usr/bin/env python3
"""SGS seçenek kalitesi için uzman incelemeli bakım yamaları.

Bu yamalar doğru cevap, kök ve çözümü değiştirmez. Tekrarlanan yapay
çeldiricileri bağlama özgü seçeneklerle değiştirir; ayrıca bir pakette
``en uzun``/``en kısa`` seçeneğin sistematik biçimde doğru olmasını engeller.
``--check`` iki repodaki yayımlanan kopyaların bu kaynakla eşleştiğini sınar.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"


PATCHES: dict[str, dict[str, dict[str, str]]] = {
    "content/finansal_muhasebe/kdv_muhasebesi.json": {
        "finmuh-kdv-gen-0013": {
            "B": "Teslim istisna olduğu için yüklenilen KDV hiçbir biçimde dikkate alınmaz ve gider yazılır."
        },
    },
    "content/mali_tablolar_analizi/fon_akim_analizi.json": {
        "mta-fon-gen-0002": {"B": "Yalnızca kasadaki hazır nakit tutarını gösterir (dar anlamı)"},
        "mta-fon-gen-0014": {"B": "1.380.000"},
    },
    "content/turkce/yazim_noktalama_anlatim.json": {
        "turkce-yazim-gen-0023": {"C": "Zarf-fiil ekinin kullanımı anlatımı bozmuştur."},
        "turkce-yazim-gen-0027": {"D": "Sıralı yüklemler arasında zaman uyumsuzluğu vardır."},
        "turkce-yazim-gen-0033": {"B": "Neden-sonuç ilişkisi yanlış kurulmuştur."},
        "turkce-yazim-gen-0039": {"D": "“Dolayı” sözcüğü gereksiz kullanılmıştır."},
        "turkce-yazim-gen-0044": {"A": "“Çok geç” sözünde gereksiz sözcük vardır."},
        "turkce-yazim-gen-0057": {"D": "“Sık sık” sözü anlamca çelişkilidir."},
        "turkce-yazim-gen-0059": {"A": "Sıralı yüklemler arasında zaman uyumsuzluğu vardır."},
        "turkce-yazim-gen-0051": {
            "A": "Özne-yüklem uyumsuzluğu (öznenin yüklemle sayı ve kişi yönünden birbiriyle uymaması)"
        },
    },
    "content/mali_tablolar_analizi/trend_analizi.json": {
        "mta-trend-gen-0018": {"B": "30.800"},
        "mta-trend-gen-0025": {"B": "38.500"},
        "mta-trend-gen-0031": {"A": "60.000"},
        "mta-trend-gen-0043": {"A": "50.000"},
        "mta-trend-gen-0006": {"D": "%25"},
        "mta-trend-gen-0026": {"B": "%9"},
    },
    "content/maliyet_muhasebesi/maliyet_hacim_kar.json": {
        "mmuh-mhk-gen-0011": {"C": "Birim katkı payı ÷ sabit maliyet"},
    },
    "content/maliyet_muhasebesi/gider_dagitimi.json": {
        "mmuh-dagitim-gen-0006": {"B": "İkinci dağıtım (yardımcı gider yerlerinin dağıtımı)"},
    },
    "content/maliyet_muhasebesi/standart_maliyet.json": {
        "mmuh-standart-gen-0007": {"A": "Standart miktar + standart fiyat toplamı"},
    },
    "content/maliyet_muhasebesi/birlesik_maliyet.json": {
        "mmuh-birlesik-gen-0006": {"A": "Ayrım noktasına kadarki ortak üretim maliyeti"},
        "mmuh-birlesik-gen-0017": {"A": "Düşük değerli ikincil ürün"},
        "mmuh-birlesik-gen-0018": {"A": "Süreçten yalnızca tek ürün çıkar"},
        "mmuh-birlesik-gen-0041": {"B": "Nihai satış değeri + ilave işleme maliyeti"},
        "mmuh-birlesik-gen-0011": {"A": "Ayrım noktasındaki satış değeri payı"},
    },
    "content/denetim/denetim_kaniti.json": {
        "den-kanit-gen-0034": {
            "C": "Kontrol testleri yalnızca analitik prosedürle yapılır; belge incelemesi ve yeniden uygulama kullanılmaz"
        },
        "den-kanit-gen-0041": {
            "A": "Analitik prosedür (tutarın geçmiş dönem eğilimi ve önceki yıl tutarıyla karşılaştırılması)"
        },
    },
    "content/denetim/denetim_ornekleme.json": {
        "den-ornek-gen-0021": {
            "B": "Kütlenin tabakalanması (benzer birimlere göre alt gruplara ayrılması ve ayrı değerlendirilmesi)"
        },
        "den-ornek-gen-0053": {
            "C": "Çalışma kâğıtlarının kamuoyuna eksiksiz açıklanmasını ve herkesçe erişilebilir olmasını sağlamak"
        },
    },
    "content/ticaret_hukuku/kiymetli_evrak.json": {
        "tic-kiymetli-gen-0033": {"A": "Mülkiyeti devreden temlik cirosu"},
    },
    "content/ticaret_hukuku/haksiz_rekabet.json": {
        "hakrek-gen-0049": {
            "C": "Haksız rekabet davalarında görevli mahkeme yoktur; uyuşmazlık yalnızca idari makamların kararıyla çözülür"
        },
    },
    "content/ticaret_hukuku/anonim_sirket.json": {
        "as-gen-0033": {
            "E": "Anonim şirketin sona ermesine yalnızca mahkeme karar verebilir; kanunda başka hiçbir sona erme sebebi yoktur"
        },
        "as-gen-0053": {
            "B": "Yönetim kurulu üyesinin şirketle işlem yapması her hâlde kesin olarak yasaktır; genel kurul izniyle dahi istisnası yoktur"
        },
    },
    "content/ticaret_hukuku/kambiyo_senetleri.json": {
        "kmb-gen-0017": {
            "A": "Görüldüğünde ödenecek poliçe, düzenlenme tarihinden itibaren yalnızca on yıl sonra ödenmek üzere ibraz edilebilir; daha önce ibraz edilemez"
        },
        "kmb-gen-0038": {
            "A": "Çekin ibrazı için kanunda hiçbir süre öngörülmemiştir; hamil çeki dilediği zaman sınırsızca ibraz edebilir ve süre işlemez"
        },
    },
    "content/meslek_hukuku/meslek_orgutu_disiplin.json": {
        "mh-orgut-gen-0028": {"E": "Disiplin cezası meslek mensubunun gelirini artıran bir ödüldür"},
        "mh-orgut-gen-0007": {"E": "Disiplin kurulu oda başkanını atayan organdır"},
    },
    "content/meslek_hukuku/sorumluluk_ve_yasaklar.json": {
        "sorum-gen-0037": {
            "A": "Vergi idaresi bu borcu yalnızca mükelleften isteyebilir; meslek mensubuna hiçbir durumda başvuramaz"
        },
    },
    "content/is_ve_sosyal_guvenlik_hukuku/is_hukuku_is_sozlesmesi.json": {
        "ish-sozlesme-gen-0057": {"C": "İş sözleşmesi yalnız işverenin tek taraflı beyanıyla kurulur"},
        "ish-sozlesme-gen-0058": {"E": "Analık izni yalnızca işverenin takdirine bağlıdır"},
    },
    "content/vergi_hukuku/vergilendirme_sureci.json": {
        "vh-surec-gen-0020": {"E": "Gecikme zammı yalnızca vergi cezalarına uygulanır"},
        "vh-surec-gen-0041": {"E": "Takdir komisyonunun matrah takdiriyle ilgisi yoktur"},
    },
    "content/vergi_hukuku/vergi_denetimi_ceza_uyusmazlik.json": {
        "vh-denetim-gen-0019": {"A": "7 takvim günü"},
    },
    "content/vergi_hukuku/emlak_vergisi.json": {
        "emlak-gen-0005": {
            "C": "Bina vergisini belediye kendi bütçesinden öder"
        },
    },
    "content/ekonomi/mikroekonomi.json": {
        "eko-mikro-gen-0031": {"E": "Mikroekonomi yalnızca enflasyonu inceler"},
    },
    "content/ekonomi/para_banka_dis_ekonomi.json": {
        "eko-para-gen-0018": {
            "A": "İthal edilen mallar üzerine değerleri oranında konulan, bu malları pahalılaştırıp ithalat maliyetini artıran gümrük vergisidir"
        },
        "eko-para-gen-0031": {
            "A": "Yerli para değer kaybettiği için ihracatı yabancılar açısından pahalılaştırıp caydırır; ithalatı ise yerli için ucuzlatıp teşvik eder ve dış ticaret açığını mutlaka kapatır"
        },
    },
    "content/maliye/butce_maliye_politikasi.json": {
        "mal-butce-gen-0046": {
            "A": "Vergilerin artırılması harcanabilir geliri artırarak talebi yükseltir; bu ilişki geçmişteki gözlemlerde de aynen doğrulanmıştır ve toplam talebi her durumda büyütür"
        },
        "mal-butce-gen-0049": {
            "A": "Kamu harcamalarının sınırsız artırılması ve bütçe sınırlarının kaldırılması; bu yaklaşım piyasa koşullarından etkilenmez ve her dönemde aynen uygulanır"
        },
    },
    "content/turkce/sozcukte_cumlede_anlam.json": {
        "turkce-anlam-gen-0025": {"B": "İstek ve dilek"},
        "turkce-anlam-gen-0037": {"C": "Derin şaşkınlık"},
    },
    "content/turkce/dil_bilgisi.json": {
        "turkce-dilbilgisi-gen-0009": {"B": "Sınava kadar oldukça çok çalıştı."},
        "turkce-dilbilgisi-gen-0018": {"B": "Dolaylı yer tümleci"},
    },
    "content/ataturk_ilkeleri/ataturk_inkilaplari.json": {
        "ait-inkilap-gen-0010": {"A": "Millet Mektepleri teşkilatı"},
        "ait-inkilap-gen-0011": {"A": "1925 yılı"},
    },
    "content/ataturk_ilkeleri/ataturk_ilkeleri_dis_politika.json": {
        "ait-ilke-gen-0013": {"B": "Balkan Paktı"},
        "ait-ilke-gen-0045": {"C": "Din temelli ümmet düzenini yeniden kurmak"},
    },
}


def load_questions(path: Path) -> tuple[object, list[dict]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data, data["questions"] if isinstance(data, dict) else data


def apply_or_check(path: Path, patches: dict[str, dict[str, str]], write: bool) -> list[str]:
    data, questions = load_questions(path)
    by_id = {question["id"]: question for question in questions}
    mismatches: list[str] = []
    for question_id, option_patches in patches.items():
        question = by_id.get(question_id)
        if question is None:
            raise SystemExit(f"Soru bulunamadı: {path}::{question_id}")
        for letter, expected in option_patches.items():
            if letter == question["answer"]:
                raise SystemExit(f"Doğru seçeneğe dokunulamaz: {path}::{question_id}.{letter}")
            if question["options"].get(letter) != expected:
                mismatches.append(f"{path}::{question_id}.{letter}")
                if write:
                    question["options"][letter] = expected
        if len(set(question["options"].values())) != 5:
            raise SystemExit(f"Seçenek çakışması: {path}::{question_id}")
    if write:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return mismatches


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()

    mismatches: list[str] = []
    for relative_path, patches in PATCHES.items():
        content_path = ROOT / relative_path
        app_path = APP_ROOT / relative_path
        mismatches.extend(apply_or_check(content_path, patches, args.write))
        mismatches.extend(apply_or_check(app_path, patches, args.write))
    if args.check and mismatches:
        print("Bakım builder'ıyla eşleşmeyen alanlar:")
        for mismatch in mismatches:
            print(f"- {mismatch}")
        return 1
    count = sum(len(options) for questions in PATCHES.values() for options in questions.values())
    print(f"{len(PATCHES)} paket / {count} seçenek iki repoda doğrulandı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
