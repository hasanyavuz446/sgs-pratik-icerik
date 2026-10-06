#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ozkaynaklar — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

FM cok adimli tur. Hesaplama agirlikli 38 soru korundu; 'hangi hesapta izlenir' ezberi 13 soru, standart paketlerine ait 4 TMS 16/32 sorusu ve yoruma acik II. tertip yedek hesabi cikarildi. Yerine gercek sinav kalibinda 22 soru yazildi: kurulusta sermaye odemesi (TTK 344), ayni sermaye, sinirli I. tertip yedek akce (TTK 519/1), pay basina kar payi, ozkaynak degisiminden kar bulma, primli bedelli artirim, ic kaynakli artirim, gecmis yil zararinin yedeklerden kapatilmasi, kar dagitim ve stopajli odeme kayitlari, donem sonu kapanisi, zarari kapatmak icin sermaye azaltimi. Olumsuz kok %3 -> %15, kor ogrenci %19.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: 6102 sayili TTK m. 344, 473-474, 519 · Tekduzen Hesap Plani 5 Ozkaynaklar, 331, 360, 370, 69 · 1 Sira No'lu MSUGT
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/finansal_muhasebe/ozkaynaklar.json"
STYLE_REF = 'SGS Finansal Muhasebe (çok adımlı; gerçek sınav profiline kalibre)'
ONEK = "finmuh-ozk-gen-"


def patch(stem, options, answer, solution, ref='6102 sayili TTK m. 519'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        "Aşağıdaki hesaplardan hangisi '5 Özkaynaklar' grubunda yer almaz?",
        {
            'A': '500 Sermaye',
            'B': '590 Dönem Net Kârı',
            'C': '540 Yasal Yedekler',
            'D': '570 Geçmiş Yıllar Kârları',
            'E': '320 Satıcılar',
        },
        'E',
        '**320 Satıcılar** bir ticari borçtur (kısa vadeli yabancı kaynak), özkaynak değildir. Diğerleri (500, 540, 570, 590) özkaynak (5) grubundadır.',
        "1 Sıra No'lu MSUGT - 5 grubu",
    ),
    # düzey 2
    '0002': patch(
        "'580 Geçmiş Yıllar Zararları (-)' hesabının özkaynaklar üzerindeki etkisi ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'Bir yıl içinde ödenecek satıcı borçlarını izleyen kısa vadeli bir yabancı kaynaktır.',
            'B': 'Paraya çevrilebilir bir dönen varlık hesabıdır ve bilançonun aktifinde gösterilir.',
            'C': 'Özkaynakları azaltan (negatif) bir kalemdir; toplam özkaynaktan (-) düşülür.',
            'D': 'Dönem içi olağandışı gelirleri toplayan ve kârı artıran bir gelir hesabıdır.',
            'E': 'Geçmiş yıl kârlarını biriktirdiği için toplam özkaynakları artıran bir kalemdir.',
        },
        'C',
        '**580 Geçmiş Yıllar Zararları (-)**, özkaynakları **azaltan (negatif)** bir kalemdir; toplam özkaynak hesaplanırken **(-)** düşülür.',
        "1 Sıra No'lu MSUGT - 580",
    ),
    # düzey 2
    '0003': patch(
        "Ortak, 500.000 ₺ tutarındaki sermaye taahhüdünü yerine getirmediği için payları iptal edilmiştir. Aynı nominal tutarlı yeni paylar başka bir ortağa 575.000 ₺'ye satılmış ve bedel bankaya yatırılmıştır.\n\nYeni ortağın ödemesine ilişkin doğru kayıt hangisidir?",
        {
            'A': '501 Ödenmemiş Sermaye 500.000 ₺ ve 521 Hisse Senedi İptal Kârları 75.000 ₺ borçlu; 102 Bankalar 575.000 ₺ alacaklı',
            'B': '102 Bankalar 575.000 ₺ borçlu; 501 Ödenmemiş Sermaye 575.000 ₺ alacaklı',
            'C': '102 Bankalar 575.000 ₺ borçlu; 500 Sermaye 575.000 ₺ alacaklı',
            'D': '102 Bankalar 575.000 ₺ borçlu; 501 Ödenmemiş Sermaye 500.000 ₺ ve 521 Hisse Senedi İptal Kârları 75.000 ₺ alacaklı',
            'E': '102 Bankalar 575.000 ₺ borçlu; 501 Ödenmemiş Sermaye 500.000 ₺ ve 520 Hisse Senetleri İhraç Primleri 75.000 ₺ alacaklı',
        },
        'D',
        'Yeni payların satışında bankaya **575.000 ₺** girer. İptal edilen paylara ait **500.000 ₺** ödenmemiş sermaye kapatılır; aradaki **75.000 ₺** fark 521 Hisse Senedi İptal Kârları hesabına alacak kaydedilir. Bu fark, normal pay ihracından doğan 520 hesabı değildir.',
        "1 Sıra No'lu MSUGT - 102/501/521; 2025-2026 SGS ıskat soru örüntüsü",
    ),
    # düzey 3
    '0004': patch(
        "Geçmiş yıllar kârı 600.000 ₺ olan şirketin genel kurulu; 50.000 ₺ yasal yedek, 30.000 ₺ statü yedeği, 20.000 ₺ olağanüstü yedek ayırmış ve kalanını ortaklara dağıtmıştır.\n\nKâr dağıtım kaydında 331 Ortaklara Borçlar hesabına kaydedilecek tutar kaç ₺'dir?",
        {
            'A': '600.000',
            'B': '500.000',
            'C': '520.000',
            'D': '580.000',
            'E': '100.000',
        },
        'B',
        'Ortaklara ayrılan kâr payı = 600.000 − 50.000 − 30.000 − 20.000 = **500.000 ₺**dir. Kayıtta 570 Geçmiş Yıllar Kârları 600.000 ₺ borçlandırılır; yedek hesapları ve 331 Ortaklara Borçlar alacaklandırılır.',
        "1 Sıra No'lu MSUGT - 570/540/541/542/331",
    ),
    # düzey 3
    '0005': patch(
        "Türk Ticaret Kanunu'na göre I. tertip genel kanuni yedek akçe (yasal yedek), hangi tutara ulaşıncaya kadar ayrılır?",
        {
            'A': "Toplam varlıkların %50'sine ulaşıncaya kadar",
            'B': "Ödenmiş sermayenin %5'ine ulaşıncaya kadar",
            'C': "Ödenmiş sermayenin %20'sine ulaşıncaya kadar",
            'D': 'Sınır yoktur, her yıl ayrılır',
            'E': 'Dönem kârının tamamına ulaşıncaya kadar',
        },
        'C',
        "TTK md. 519'a göre I. tertip genel kanuni yedek akçe, yıllık kârın %5'i oranında, **ödenmiş sermayenin %20'sine** ulaşıncaya kadar ayrılır.",
        'TTK md. 519',
    ),
    # düzey 3
    '0006': patch(
        "Dönem başında özkaynak toplamı 1.500.000 ₺ olan bir anonim şirkette yıl içinde şu işlemler olmuştur: nominal değeri 250.000 ₺ olan paylar 300.000 ₺'ye nakden ihraç edilmiş ve bedel tahsil edilmiştir; olağanüstü yedeklerden 100.000 ₺ sermayeye eklenmiştir; geçmiş yıl kârından ortaklara 120.000 ₺ nakit kâr payı dağıtılmış ve ödenmiştir; yılın sonucu 80.000 ₺ dönem net zararıdır.\n\nBuna göre şirketin dönem sonu özkaynak toplamı kaç ₺'dir?",
        {
            'A': '1.700.000',
            'B': '1.720.000',
            'C': '1.550.000',
            'D': '1.600.000',
            'E': '1.760.000',
        },
        'D',
        'Nakdi artırım özkaynağı tahsil edilen tutar kadar artırır: +300.000 ₺ (250.000 sermaye + 50.000 ihraç primi). İç kaynaklardan artırım özkaynak içinde yer değiştirmedir: 0. Kâr payı dağıtımı −120.000 ₺, dönem net zararı −80.000 ₺. Dönem sonu özkaynak = 1.500.000 + 300.000 − 120.000 − 80.000 = 1.600.000 ₺.',
        "1 Sıra No'lu MSUGT - 5 grubu",
    ),
    # düzey 2
    '0007': patch(
        "Bir işletmenin '580 Geçmiş Yıllar Zararları (-)' hesabındaki tutarın, ayrılan olağanüstü yedeklerle kapatılmasına karar verilmiştir. Bu kapatma işleminde 580 hesabı nasıl işlem görür?",
        {
            'A': '580 Geçmiş Yıllar Zararları (-) kullanılmaz; zarar 100 Kasa hesabından nakit ödenerek kapatılır.',
            'B': '580 Geçmiş Yıllar Zararları (-) alacaklandırılarak kapatılır; karşılığında 590 Dönem Net Kârı borçlandırılıp azaltılır.',
            'C': '580 Geçmiş Yıllar Zararları (-) alacaklandırılarak kapatılır; karşılığında 320 Satıcılar hesabı borçlandırılıp azaltılır.',
            'D': '580 Geçmiş Yıllar Zararları (-) borçlandırılarak tutarı bir kat daha artırılır; karşılığında 542 Olağanüstü Yedekler alacaklandırılır.',
            'E': '580 Geçmiş Yıllar Zararları (-) alacaklandırılarak kapatılır; karşılığında 542 Olağanüstü Yedekler borçlandırılır.',
        },
        'E',
        'Geçmiş yıl zararı yedeklerle kapatılırken, negatif özkaynak kalemi **580 Geçmiş Yıllar Zararları (-) alacaklandırılarak kapatılır**; karşılığında **542 Olağanüstü Yedekler borçlandırılır** (yedek azalır).',
        "1 Sıra No'lu MSUGT - 580 / 542",
    ),
    # düzey 2
    '0008': patch(
        'İşletmenin dağıtmayıp sermayeye eklediği (iç kaynaklardan/bedelsiz) sermaye artırımı ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'Sermaye artırımı için işletmenin bir maddi duran varlığı satılır; bu nedenle varlıkları azalırken elde edilen tutar doğrudan 500 Sermaye hesabına aktarılır.',
            'B': 'İşletme dışarıdan uzun vadeli banka kredisi kullandığından yabancı kaynakları (borçları) artar ve karşılığında 500 Sermaye hesabı da aynı tutarda yükselir.',
            'C': 'Yedekler veya geçmiş yıl kârları gibi iç kaynaklar sermayeye eklenir; bu kaynak hesapları azalırken 500 Sermaye artar, toplam özkaynak değişmez.',
            'D': 'Ortaklardan sermaye taahhüdü karşılığı yeni nakit tahsil edilir; bu nedenle 102 Bankalar hesabı borçlandırılırken 500 Sermaye alacaklandırılır ve varlıklar artar.',
            'E': 'Sermayeye eklenen yedekler dönem sonucuna yansıtıldığından, artırım tutarı kadar bir faaliyet gideri doğar ve dönem kârı bu tutar kadar azalır.',
        },
        'C',
        'İç kaynaklardan (bedelsiz) sermaye artırımında **yedekler/geçmiş yıl kârları sermayeye eklenir**: bu kaynak hesapları azalırken **500 Sermaye artar**; bir varlık girişi olmadığından **toplam özkaynak değişmez** (özkaynak içinde yer değiştirir).',
        "1 Sıra No'lu MSUGT - 500 / 540 / 570",
    ),
    # düzey 3
    '0009': patch(
        "İşletme, nominal değeri toplam 1.000.000 ₺ olan payları 1.200.000 ₺'ye ihraç etmiş ve yalnız bu ihraca doğrudan bağlanabilen 30.000 ₺ işlem maliyetine katlanmıştır. Vergi etkisi dikkate alınmayacaktır.\n\nTMS 32'ye göre işlemin özkaynakta oluşturduğu net artış kaç ₺'dir?",
        {
            'A': '1.170.000',
            'B': '1.110.000',
            'C': '1.000.000',
            'D': '1.200.000',
            'E': '970.000',
        },
        'A',
        "Pay ihracından sağlanan 1.200.000 ₺ özkaynak işleminin doğrudan maliyeti olan 30.000 ₺, TMS 32'ye göre özkaynaktan indirilir. Net artış 1.200.000 − 30.000 = **1.170.000 ₺**dir; maliyet faaliyet gideri yapılmaz.",
        'TMS 32 Finansal Araçlar: Sunum, par. 35',
    ),
    # düzey 2
    '0010': patch(
        'Ortak, daha önce kaydedilmiş 400.000 ₺ tutarındaki ayni sermaye taahhüdünü, işletmede kullanılacak ve bu değer üzerinden kabul edilen bir makineyi teslim ederek yerine getirmiştir.\n\nTeslim kaydı hangisidir?',
        {
            'A': '253 Tesis, Makine ve Cihazlar borç / 500 Sermaye alacak',
            'B': '253 Tesis, Makine ve Cihazlar borç / 501 Ödenmemiş Sermaye alacak',
            'C': '253 Tesis, Makine ve Cihazlar borç / 520 Hisse Senetleri İhraç Primleri alacak',
            'D': '500 Sermaye borç / 253 Tesis, Makine ve Cihazlar alacak',
            'E': '501 Ödenmemiş Sermaye borç / 253 Tesis, Makine ve Cihazlar alacak',
        },
        'B',
        'Sermaye taahhüdü daha önce 501 borç / 500 alacak kaydıyla doğmuştur. Makine teslim edildiğinde varlık arttığı için **253 borçlandırılır**; yerine getirilen taahhüt nedeniyle **501 alacaklandırılarak** kapatılır.',
        "1 Sıra No'lu MSUGT - 253/501",
    ),
    # düzey 3
    '0011': patch(
        "Bir işletmenin özkaynak kalemleri şöyledir: 500 Sermaye 900.000 ₺, 501 Ödenmemiş Sermaye (-) 100.000 ₺, 520 Hisse Senetleri İhraç Primleri 60.000 ₺, 540 Yasal Yedekler 80.000 ₺, 570 Geçmiş Yıllar Kârları 40.000 ₺, 580 Geçmiş Yıllar Zararları (-) 30.000 ₺ ve 591 Dönem Net Zararı (-) 50.000 ₺.\n\nToplam özkaynak kaç ₺'dir?",
        {
            'A': '930.000',
            'B': '800.000',
            'C': '900.000',
            'D': '1.060.000',
            'E': '1.000.000',
        },
        'C',
        'Toplam özkaynak = 900.000 − 100.000 + 60.000 + 80.000 + 40.000 − 30.000 − 50.000 = **900.000 ₺**dir. 501, 580 ve 591 negatif özkaynak kalemleri olduğu için düşülür.',
        "1 Sıra No'lu MSUGT - 5 Özkaynaklar grubu",
    ),
    # düzey 3
    '0012': patch(
        "Bir anonim şirketin dönem sonu bilançosunda aktif toplamı 3.400.000 ₺, kısa vadeli yabancı kaynakları 900.000 ₺, uzun vadeli yabancı kaynakları 1.100.000 ₺'dir. Özkaynak kalemleri şunlardır: 500 Sermaye 1.000.000 ₺, 501 Ödenmemiş Sermaye 100.000 ₺, 540 Yasal Yedekler 60.000 ₺, 542 Olağanüstü Yedekler 90.000 ₺, 580 Geçmiş Yıllar Zararları 50.000 ₺ ve tutarı verilmeyen dönem net kârı.\n\nBuna göre şirketin dönem net kârı kaç ₺'dir?",
        {
            'A': '300.000',
            'B': '400.000',
            'C': '350.000',
            'D': '250.000',
            'E': '500.000',
        },
        'B',
        'Özkaynak toplamı = aktif − yabancı kaynaklar = 3.400.000 − 2.000.000 = 1.400.000 ₺. Bilinen özkaynak kalemleri: 1.000.000 − 100.000 + 60.000 + 90.000 − 50.000 = 1.000.000 ₺ (501 ve 580 özkaynakları azaltır). Dönem net kârı = 1.400.000 − 1.000.000 = 400.000 ₺.',
        "1 Sıra No'lu MSUGT - 5 grubu",
    ),
    # düzey 2
    '0013': patch(
        'İşletmenin geçmiş yıl kârlarını ortaklara nakit temettü olarak dağıtmasının özkaynaklar üzerindeki etkisi aşağıdakilerden hangisidir?',
        {
            'A': 'Dağıtılan kısım kadar özkaynağı (geçmiş yıl kârlarını) azaltır ve işletmeden nakit çıkışı olur.',
            'B': 'Dağıtılan kısım kadar geçmiş yıl kârlarını sermayeye ekleyerek toplam özkaynağı artırır ve varlıkları yükseltir.',
            'C': 'Dağıtılan kâr payı tutarı doğrudan 500 Sermaye hesabına aktarıldığından işletmenin ödenmiş sermayesini artırır.',
            'D': 'İşletmenin satıcılara olan borçlarını kapattığından, dağıtılan tutar kadar yabancı kaynakları (borçları) azaltır.',
            'E': 'Özkaynak kalemleri arasında yer değiştirme yarattığından toplam özkaynağı ve varlıkları etkilemez.',
        },
        'A',
        'Nakit temettü dağıtımı, dağıtılan kısım kadar **özkaynağı (geçmiş yıl kârlarını) azaltır** ve işletmeden **nakit çıkışına** yol açar (varlık ve özkaynak birlikte azalır).',
        "1 Sıra No'lu MSUGT - 570; TTK md. 509",
    ),
    # düzey 3
    '0014': patch(
        "(A, B ve C) Kollektif Şirketi'nin kuruluşunda sermaye taahhüt kaydı yapılmıştır. Ortak A taahhüdünü 60.000 ₺ değerindeki ticari mallarla, B 90.000 ₺ değerindeki bir kamyonetle, C ise 50.000 ₺'yi şirketin banka hesabına yatırarak yerine getirmiştir (KDV ihmal). Buna göre yapılacak kayıtta aşağıdakilerden hangisi yer almaz?",
        {
            'A': '102 Bankalar hesabı 50.000 ₺ borçlandırılır',
            'B': '501 Ödenmemiş Sermaye hesabı 200.000 ₺ alacaklandırılır',
            'C': '153 Ticari Mallar hesabı 60.000 ₺ borçlandırılır',
            'D': '254 Taşıtlar hesabı 90.000 ₺ borçlandırılır',
            'E': '500 Sermaye hesabı 200.000 ₺ borçlandırılır',
        },
        'E',
        'Taahhüdün yerine getirilmesi kaydı: 153 (borç) 60.000 + 254 (borç) 90.000 + 102 (borç) 50.000 / 501 Ödenmemiş Sermaye (alacak) 200.000. 500 Sermaye taahhüt kaydında alacaklandırılmıştır; bu aşamada borçlandırılmaz.',
        'THP 153, 254, 102, 501',
    ),
    # düzey 3
    '0015': patch(
        "Sermayesi, her biri 1 ₺ nominal değerli 2.000.000 paydan oluşan bir anonim şirketin kâr dağıtım tablosundan alınan bilgiler şöyledir: dönem kârı 900.000 ₺, I. tertip yasal yedek 45.000 ₺, I. temettü 100.000 ₺, statü yedeği 55.000 ₺, II. temettü 400.000 ₺ ve II. tertip yasal yedek 40.000 ₺. Buna göre pay başına düşen kâr payı kaç ₺'dir?",
        {
            'A': '0,25 ₺',
            'B': '0,45 ₺',
            'C': '0,35 ₺',
            'D': '0,50 ₺',
            'E': '0,30 ₺',
        },
        'A',
        'Ortaklara dağıtılan toplam kâr payı I. ve II. temettünün toplamıdır: 100.000 + 400.000 = 500.000 ₺. Pay başına kâr payı 500.000 / 2.000.000 = **0,25 ₺**. Yedek akçeler ortaklara dağıtılmaz.',
        '6102 sayılı TTK m. 519; kâr dağıtım tablosu',
    ),
    # düzey 3
    '0016': patch(
        "Bir anonim şirketin 580 Geçmiş Yıllar Zararları hesabında 70.000 ₺ bulunmaktadır. Genel kurul bu zararın önce 542 Olağanüstü Yedekler hesabındaki 50.000 ₺'nin tamamıyla, kalanının da 540 Yasal Yedekler hesabındaki 30.000 ₺'den karşılanmasına karar vermiştir. Buna göre yapılacak kayıtla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '580 Geçmiş Yıllar Zararları hesabı 70.000 ₺ borçlandırılır',
            'B': '540 Yasal Yedekler hesabı 30.000 ₺ borçlandırılır',
            'C': '570 Geçmiş Yıllar Kârları hesabı 70.000 ₺ borçlandırılır',
            'D': '542 Olağanüstü Yedekler hesabı 70.000 ₺ borçlandırılır',
            'E': '580 Geçmiş Yıllar Zararları hesabı 70.000 ₺ alacaklandırılır',
        },
        'E',
        'Kayıt: 542 (borç) 50.000 + 540 (borç) 20.000 / **580 (alacak) 70.000**. Borç kalanı veren 580 alacaklandırılarak kapatılır; yasal yedekten yalnız eksik kalan 20.000 ₺ kullanılır.',
        'THP 580, 542, 540; 6102 sayılı TTK m. 519/3',
    ),
    # düzey 3
    '0017': patch(
        'Bir anonim şirketin 331 Ortaklara Borçlar hesabında tam mükellef gerçek kişi ortaklara dağıtılmasına karar verilen 400.000 ₺ kâr payı bulunmaktadır. Ödeme sırasında kâr payı üzerinden %15 oranında gelir vergisi stopajı yapılmış, kalan tutar ortakların banka hesaplarına havale edilmiştir. Buna göre ödeme kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '770 Genel Yönetim Giderleri hesabı 60.000 ₺ borçlandırılır',
            'B': '360 Ödenecek Vergi ve Fonlar hesabı 60.000 ₺ alacaklandırılır',
            'C': '331 Ortaklara Borçlar hesabı 340.000 ₺ borçlandırılır',
            'D': '102 Bankalar hesabı 400.000 ₺ alacaklandırılır',
            'E': '360 Ödenecek Vergi ve Fonlar hesabı 60.000 ₺ borçlandırılır',
        },
        'B',
        "Kayıt: 331 (borç) 400.000 / **360 (alacak) 60.000** + 102 (alacak) 340.000. Stopaj ortağın vergisidir; şirket keserek vergi dairesine ödeyeceği için 360'ta borç olarak izlenir, gider yazılmaz.",
        'THP 331, 360, 102',
    ),
    # düzey 2
    '0018': patch(
        'Bir anonim şirketin bilançosundaki özkaynak kalemleri sınıflandırılmaktadır. Buna göre aşağıdaki hesaplardan hangisi 52 Sermaye Yedekleri grubunda yer almaz?',
        {
            'A': '542 Olağanüstü Yedekler',
            'B': '529 Diğer Sermaye Yedekleri',
            'C': '521 Hisse Senedi İptal Kârları',
            'D': '520 Hisse Senedi İhraç Primleri',
            'E': '522 MDV Yeniden Değerleme Artışları',
        },
        'A',
        '542 Olağanüstü Yedekler kârdan ayrıldığı için **54 Kâr Yedekleri** grubundadır. 520, 521, 522 ve 529 sermaye hareketlerinden veya değerleme farklarından doğan sermaye yedekleridir.',
        'THP 52 Sermaye Yedekleri, 54 Kâr Yedekleri',
    ),
    # düzey 2
    '0019': patch(
        'Aşağıdaki ifadelerden hangileri doğrudur?\n\nI. 580 Geçmiş Yıllar Zararları bilançoda özkaynaklarda pozitif tutar olarak gösterilir.\n\nII. 331 Ortaklara Borçlar bir yabancı kaynak hesabıdır.\n\nIII. 591 Dönem Net Zararı özkaynakları artırır.',
        {
            'A': 'I ve III',
            'B': 'II ve III',
            'C': 'I ve II',
            'D': 'Yalnız II',
            'E': 'Yalnız I',
        },
        'D',
        'Yalnız II doğrudur. 580 ve 591 özkaynaklarda **eksi** (−) olarak gösterilir ve özkaynağı azaltır. 331, ortaklara ödenecek tutarları izleyen kısa vadeli yabancı kaynak hesabıdır.',
        'THP 331, 580, 591',
    ),
    # düzey 3
    '0020': patch(
        "570 Geçmiş Yıllar Kârları hesabındaki 600.000 ₺'nin 30.000 ₺'si yasal yedeğe, 220.000 ₺'si olağanüstü yedeğe ayrılmış, 350.000 ₺'sinin ortaklara dağıtılmasına karar verilmiştir; kâr payları henüz ödenmemiştir. Buna göre bu karar toplam özkaynağı nasıl etkiler?",
        {
            'A': '350.000 ₺ artırır',
            'B': '600.000 ₺ azaltır',
            'C': 'Değiştirmez',
            'D': '350.000 ₺ azaltır',
            'E': '250.000 ₺ azaltır',
        },
        'D',
        "Yedeklere ayrılan 250.000 ₺ özkaynak içinde kalır. Ortaklara dağıtılmasına karar verilen **350.000 ₺** 331 Ortaklara Borçlar'a (yabancı kaynak) aktarıldığından özkaynak bu tutarda azalır; ödeme yapılmadığı için varlıklar değişmez.",
        'THP 570, 331; özkaynak hareketleri',
    ),
    # düzey 2
    '0021': patch(
        "'501 Ödenmemiş Sermaye (-)' hesabının niteliği ile ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': 'İşletmenin sahip olduğu bina, makine ve taşıtları maliyet bedeliyle izleyen, amortismana tabi tutulan bir maddi duran varlık hesabıdır.',
            'B': 'Ortaklara sermaye taahhüdü için yapılan ödemeleri gösteren, dönem sonunda sonuç hesaplarına aktarılan bir faaliyet gideri hesabıdır.',
            'C': 'Sermayeyi düzenleyen bir hesaptır; taahhüt edilip henüz ödenmemiş sermayeyi gösterir ve sermayeden düşülür.',
            'D': 'Dönem içinde elde edilen faiz ve kira gelirlerini toplayan, dönem sonunda 690 hesaba devredilerek kapatılan bir gelir hesabıdır.',
            'E': 'Ortakların işletmeden olan alacaklarını izleyen, bir yıl içinde nakden ödenecek kısa vadeli bir borç hesabıdır.',
        },
        'C',
        "**501 Ödenmemiş Sermaye (-)**, 500 Sermaye'yi düzenleyen bir hesaptır; ortakların taahhüt edip **henüz ödemedikleri** sermaye tutarını gösterir ve sermayeden **(-)** düşülür. Ödendikçe kapanır.",
        "1 Sıra No'lu MSUGT - 501",
    ),
    # düzey 2
    '0022': patch(
        'Bir anonim şirket kurulmuş; ortaklar 400.000 ₺ sermaye taahhüt etmiş ancak henüz ödeme yapmamıştır. Kuruluşta sermaye taahhüdüne ilişkin kayıt aşağıdakilerden hangisidir?',
        {
            'A': '501 Ödenmemiş Sermaye (-) (borç) 400.000 / 100 Kasa (alacak) 400.000',
            'B': '500 Sermaye (borç) 400.000 / 501 Ödenmemiş Sermaye (-) (alacak) 400.000',
            'C': '500 Sermaye (borç) 400.000 / 100 Kasa (alacak) 400.000',
            'D': '100 Kasa (borç) 400.000 / 500 Sermaye (alacak) 400.000',
            'E': '501 Ödenmemiş Sermaye (-) (borç) 400.000 / 500 Sermaye (alacak) 400.000',
        },
        'E',
        'Sermaye taahhüdünde: taahhüt edilen sermaye **500 Sermaye (alacak) 400.000** alacaklandırılır; henüz ödenmediğinden düzenleyici **501 Ödenmemiş Sermaye (-) (borç) 400.000** borçlandırılır.',
        "1 Sıra No'lu MSUGT - 500 / 501",
    ),
    # düzey 3
    '0023': patch(
        "Bir anonim şirketin bilançosunda 580 Geçmiş Yıllar Zararları 300.000 ₺, 542 Olağanüstü Yedekler 120.000 ₺ ve 590 Dönem Net Kârı 250.000 ₺ olarak yer almaktadır. Genel kurul, geçmiş yıllar zararının önce olağanüstü yedeklerin tamamıyla, kalanının da cari dönem net kârından karşılanmasına karar vermiş ve kayıtlar yapılmıştır.\n\nBuna göre bu işlemlerden sonra 590 Dönem Net Kârı hesabının kalanı kaç ₺'dir?",
        {
            'A': '250.000',
            'B': '70.000',
            'C': '30.000',
            'D': '130.000',
            'E': '50.000',
        },
        'B',
        "Olağanüstü yedeklerle kapatma: 542 120.000 ₺ borç / 580 120.000 ₺ alacak; zararın kalanı 180.000 ₺. Cari kârdan kapatma: 590 180.000 ₺ borç / 580 180.000 ₺ alacak. 590'da kalan 250.000 − 180.000 = 70.000 ₺. Bu işlemler toplam özkaynağı değiştirmez.",
        "1 Sıra No'lu MSUGT - 542/580",
    ),
    # düzey 2
    '0024': patch(
        'İşletme, nominal değeri 100.000 ₺ olan hisse senetlerini 140.000 ₺ bedelle ihraç etmiş ve tutarı banka hesabına almıştır. Bu işlemin kaydı aşağıdakilerden hangisidir?',
        {
            'A': '500 Sermaye (borç) 100.000, 520 Hisse Senetleri İhraç Primleri (borç) 40.000 / 102 Bankalar (alacak) 140.000',
            'B': '102 Bankalar (borç) 140.000 / 500 Sermaye (alacak) 100.000, 600 Yurtiçi Satışlar (alacak) 40.000',
            'C': '102 Bankalar (borç) 140.000 / 500 Sermaye (alacak) 100.000, 520 Hisse Senetleri İhraç Primleri (alacak) 40.000',
            'D': '102 Bankalar (borç) 140.000 / 500 Sermaye (alacak) 100.000, 549 Özel Fonlar (alacak) 40.000',
            'E': '102 Bankalar (borç) 140.000 / 540 Yasal Yedekler (alacak) 100.000, 520 Hisse Senetleri İhraç Primleri (alacak) 40.000',
        },
        'C',
        'Banka girişi **102 Bankalar (borç) 140.000**; nominal sermaye **500 Sermaye (alacak) 100.000**; nominalin üzerindeki kısım emisyon primi **520 Hisse Senetleri İhraç Primleri (alacak) 40.000**.',
        "1 Sıra No'lu MSUGT - 500 / 520 / 102",
    ),
    # düzey 3
    '0025': patch(
        "Önceki döneme ait 480.000 ₺ kâr, yeni dönemde 570 Geçmiş Yıllar Kârları hesabında izlenmektedir. Genel kurul bu tutarın 60.000 ₺'sini yasal yedeğe, 40.000 ₺'sini olağanüstü yedeğe ayırmış ve 380.000 ₺'sini ortaklara dağıtmıştır.\n\nDağıtım kaydında borçlandırılacak hesap hangisidir?",
        {
            'A': '590 Dönem Net Kârı, 480.000 ₺',
            'B': '540 Yasal Yedekler, 60.000 ₺',
            'C': '331 Ortaklara Borçlar, 380.000 ₺',
            'D': '542 Olağanüstü Yedekler, 40.000 ₺',
            'E': '570 Geçmiş Yıllar Kârları, 480.000 ₺',
        },
        'E',
        "Kâr önceki döneme ait olduğundan karar tarihinde **570 Geçmiş Yıllar Kârları 480.000 ₺ borçlandırılır**. Ayrılan yedekler ile ortaklara borç alacaklandırılır. 590 hesabı dönem kapandıktan sonra 570'e devredilmiş durumdadır.",
        "1 Sıra No'lu MSUGT - 570/540/542/331",
    ),
    # düzey 2
    '0026': patch(
        "Emisyon (hisse senetleri ihraç) priminin bir 'sermaye yedeği' sayılmasının nedeni aşağıdakilerden hangisidir?",
        {
            'A': 'Bir sermaye hareketi olan hisse senedi ihracından (nominalin üzerinde satıştan) doğması; faaliyet kârıyla ilgisi olmaması',
            'B': 'İşletmenin dönem içindeki olağan faaliyet kârından, tıpkı yasal yedekler gibi belirli bir oranda ayrılarak oluşması ve bir kâr yedeği olması',
            'C': 'İşletmenin zararla kapattığı dönemlerde, zararı telafi etmek amacıyla ortaklardan tahsil edilerek oluşması',
            'D': 'İşletmenin ana faaliyet konusu olan ticari mal alım satımından elde edilen brüt satış kârından kaynaklanması',
            'E': 'Ortaklara ileride ödenecek bir kâr payı taahhüdünü temsil etmesi ve bu nedenle bir yabancı kaynak (borç) niteliği taşıması',
        },
        'A',
        'Emisyon primi, bir **sermaye hareketi** olan hisse senedi ihracından (nominalin üzerinde satıştan) doğar; işletmenin faaliyet kârıyla ilgili değildir. Bu nedenle bir **sermaye yedeği** (52) olarak sınıflandırılır.',
        "1 Sıra No'lu MSUGT - 520 / 52 grubu",
    ),
    # düzey 3
    '0027': patch(
        "Sermaye taahhüdünü yerine getirmeyen ortağın 800.000 ₺ nominal değerli payları iptal edilmiş; aynı nominal tutarlı yeni paylar 900.000 ₺'ye başka bir ortağa satılmıştır. Aradaki 100.000 ₺ fark hangi hesapta izlenir?",
        {
            'A': '542 Olağanüstü Yedekler',
            'B': '590 Dönem Net Kârı',
            'C': '649 Diğer Olağan Gelir ve Kârlar',
            'D': '521 Hisse Senedi İptal Kârları',
            'E': '520 Hisse Senetleri İhraç Primleri',
        },
        'D',
        'Fark normal bir yeni pay ihracından değil, taahhüdünü yerine getirmeyen ortağın paylarının **iptal edilip yeniden satılmasından** doğmuştur. Bu nedenle **521 Hisse Senedi İptal Kârları** hesabında izlenir.',
        "1 Sıra No'lu MSUGT - 521; 2025-2026 SGS ıskat soru örüntüsü",
    ),
    # düzey 2
    '0028': patch(
        'Şirketin 300.000 ₺ sermaye azaltımı tescil edilmiş ve ortaklara ödenecek tutar 331 Ortaklara Borçlar hesabına aktarılmıştır. Tutar daha sonra şirketin banka hesabından ödenmiştir.\n\nÖdeme tarihinde yapılacak kayıt hangisidir?',
        {
            'A': '102 Bankalar borç / 331 Ortaklara Borçlar alacak',
            'B': '331 Ortaklara Borçlar borç / 102 Bankalar alacak',
            'C': '500 Sermaye borç / 102 Bankalar alacak',
            'D': '331 Ortaklara Borçlar borç / 500 Sermaye alacak',
            'E': '501 Ödenmemiş Sermaye borç / 102 Bankalar alacak',
        },
        'B',
        'Sermaye azaltımı tescil edildiğinde 500 Sermaye borçlandırılıp 331 Ortaklara Borçlar alacaklandırılmıştır. Sonraki ödeme, mevcut borcun kapatılmasıdır: **331 borç / 102 Bankalar alacak**.',
        "1 Sıra No'lu MSUGT - 500/331/102",
    ),
    # düzey 3
    '0029': patch(
        "Aşağıdaki hesaplardan hangileri 'kâr yedeği' (54) niteliğindedir?\n\nI. 520 Hisse Senetleri İhraç Primleri\n\nII. 540 Yasal Yedekler\n\nIII. 542 Olağanüstü Yedekler",
        {
            'A': 'Yalnız I',
            'B': 'I, II ve III',
            'C': 'I ve II',
            'D': 'II ve III',
            'E': 'I ve III',
        },
        'D',
        '**II (540 Yasal Yedekler)** ve **III (542 Olağanüstü Yedekler)** kâr yedekleridir (dönem kârından ayrılır). **I (520 Hisse Senetleri İhraç Primleri)** ise bir sermaye yedeğidir. Doğru cevap **II ve III**.',
        "1 Sıra No'lu MSUGT - 52 / 54 grupları",
    ),
    # düzey 3
    '0030': patch(
        '500 Sermaye hesabı 1.000.000 ₺, 501 Ödenmemiş Sermaye (-) hesabı 200.000 ₺ olan şirkette, henüz ödenmemiş kısım kadar sermaye azaltımı tescil edilmiştir.\n\nAzaltım kaydı ve toplam özkaynak etkisi hangisidir?',
        {
            'A': '501 borç / 500 alacak; toplam özkaynak 200.000 ₺ artar.',
            'B': '501 borç / 331 alacak; toplam özkaynak 200.000 ₺ azalır.',
            'C': '500 borç / 501 alacak; toplam özkaynak değişmez.',
            'D': '500 borç / 102 alacak; toplam özkaynak 200.000 ₺ azalır.',
            'E': '102 borç / 500 alacak; toplam özkaynak 200.000 ₺ artar.',
        },
        'C',
        'Ödenmemiş kısmın iptalinde **500 Sermaye 200.000 ₺ borçlandırılır**, **501 Ödenmemiş Sermaye 200.000 ₺ alacaklandırılarak** kapatılır. Pozitif sermaye ile negatif düzenleyici hesap aynı tutarda azaldığından net özkaynak değişmez.',
        "1 Sıra No'lu MSUGT - 500/501",
    ),
    # düzey 2
    '0031': patch(
        'Genel kanuni yedek akçesi sermayenin yarısını aşmamış bir anonim şirkette, TTK md. 519/3 uyarınca aşağıdaki kullanımlardan hangisi bu aşamada mümkündür?',
        {
            'A': 'Şirket çalışanlarına prim olarak ödenmesi',
            'B': 'Yönetim kurulunun uygun gördüğü yatırımların finansmanında kullanılması',
            'C': 'Pay sahiplerine olağan kâr payı olarak dağıtılması',
            'D': 'Yeni pay ihracının bedelini ortaklar adına karşılaması',
            'E': 'Şirket zararlarının kapatılmasında kullanılması',
        },
        'E',
        'Genel kanuni yedek akçe sermayenin yarısını aşmadıkça yalnız **zararların kapatılması**, işlerin iyi gitmediği zamanlarda işletmenin devamı veya işsizliğin önlenmesi ve sonuçlarının hafifletilmesi için kullanılabilir. Serbest kâr dağıtım kaynağı değildir.',
        'TTK md. 519/3',
    ),
    # düzey 3
    '0032': patch(
        '570 Geçmiş Yıllar Kârları hesabındaki 800.000 ₺ için genel kurul; 50.000 ₺ yasal yedek, 150.000 ₺ statü yedeği, 100.000 ₺ olağanüstü yedek ve 500.000 ₺ ortaklara kâr payı ayırmıştır.\n\nKâr dağıtım kaydıyla ilgili aşağıdakilerden hangisi yanlıştır?',
        {
            'A': '541 Statü Yedekleri hesabı 150.000 ₺ alacaklandırılır.',
            'B': '331 Ortaklara Borçlar hesabı 500.000 ₺ borçlandırılır.',
            'C': '542 Olağanüstü Yedekler hesabı 100.000 ₺ alacaklandırılır.',
            'D': '570 Geçmiş Yıllar Kârları hesabı 800.000 ₺ borçlandırılır.',
            'E': '540 Yasal Yedekler hesabı 50.000 ₺ alacaklandırılır.',
        },
        'B',
        'Dağıtılan geçmiş yıl kârı 570 hesabın borcuna; yedekler ile ortaklara ödenecek kâr payı ilgili hesapların **alacağına** yazılır. Bu nedenle 331 Ortaklara Borçlar hesabının borçlandırılacağı ifadesi yanlıştır; hesap **500.000 ₺ alacaklandırılır**.',
        "1 Sıra No'lu MSUGT - 570/540/541/542/331",
    ),
    # düzey 3
    '0033': patch(
        "Özkaynaklarla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. TMS 32'ye göre işletmenin geri satın aldığı kendi payları özkaynaktan düşülür ve alımdan dolayı kâr veya zarara kazanç ya da kayıp yansıtılmaz.\n\nII. Olağanüstü yedekler ve geçmiş yıllar kârlarının sermayeye eklenmesi toplam özkaynağı değiştirmez.\n\nIII. Nakit kâr payı dağıtım kararı verildiği anda, ödeme yapılmasa bile işletmenin varlıkları azalır.",
        {
            'A': 'Yalnız I',
            'B': 'Yalnız II',
            'C': 'I ve III',
            'D': 'I, II ve III',
            'E': 'I ve II',
        },
        'E',
        'I ve II doğrudur. Geri alınan kendi payları özkaynaktan düşülür; iç kaynaklardan sermaye artırımı yalnız özkaynak bileşimini değiştirir. III yanlıştır: kâr payı kararı özkaynağı azaltıp borç doğurur; **ödeme yapılıncaya kadar varlıklar değişmez**.',
        "TMS 32, par. 33 ve 35; 1 Sıra No'lu MSUGT - 542/570/500/331",
    ),
    # düzey 3
    '0034': patch(
        "Sermayesi 400.000 ₺ olan bir anonim şirkette sermayenin %25'i henüz ödenmemiştir. Önceki yıllarda ayrılan genel kanuni yedek akçe toplamı 57.000 ₺'dir. Şirketin yıllık net kârı 90.000 ₺ olup geçmiş yıl zararı yoktur. Buna göre bu yıl ayrılacak I. tertip genel kanuni yedek akçe kaç ₺'dir?",
        {
            'A': '4.500 ₺',
            'B': '23.000 ₺',
            'C': '3.000 ₺',
            'D': 'Yedek akçe ayrılmaz',
            'E': '15.000 ₺',
        },
        'C',
        "TTK m. 519/1: yıllık kârın %5'i, **ödenmiş sermayenin %20'sine** ulaşıncaya kadar ayrılır. Ödenmiş sermaye 400.000 × %75 = 300.000 ₺; üst sınır 60.000 ₺; kalan yer 60.000 − 57.000 = 3.000 ₺. Kârın %5'i (4.500 ₺) bu sınırı aştığından yalnız **3.000 ₺** ayrılır.",
        '6102 sayılı TTK m. 519/1',
    ),
    # düzey 3
    '0035': patch(
        "Sermayesi 700.000 ₺ olan bir anonim şirket sermayesini %40 oranında artırmış, artırım taahhüt kaydı yapılmıştır. Artırılan sermayeyi temsil eden payların tamamı 350.000 ₺'ye satılmış ve bedel banka hesabına yatırılmıştır. Buna göre payların satış kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '102 Bankalar hesabı 280.000 ₺ borçlandırılır',
            'B': '500 Sermaye hesabı 350.000 ₺ alacaklandırılır',
            'C': '520 Hisse Senedi İhraç Primleri hesabı 70.000 ₺ alacaklandırılır',
            'D': '501 Ödenmemiş Sermaye hesabı 350.000 ₺ alacaklandırılır',
            'E': '521 Hisse Senedi İptal Kârları hesabı 70.000 ₺ alacaklandırılır',
        },
        'C',
        'Artırılan nominal sermaye 700.000 × %40 = 280.000 ₺. Kayıt: 102 Bankalar (borç) 350.000 / 501 Ödenmemiş Sermaye (alacak) 280.000 + **520 Hisse Senedi İhraç Primleri (alacak) 70.000**. Nominal değeri aşan tutar emisyon primidir; 521 taahhüdünü yerine getirmeyen ortakların paylarının iptaliyle ilgilidir.',
        'THP 500, 501, 520; 6102 sayılı TTK m. 347',
    ),
    # düzey 2
    '0036': patch(
        "Genel kurul, 520 Hisse Senedi İhraç Primleri hesabındaki 150.000 ₺ ile 542 Olağanüstü Yedekler hesabındaki 100.000 ₺'nin sermayeye eklenmesine karar vermiş ve artırım tescil edilmiştir. Buna göre yapılacak kayıt aşağıdakilerden hangisidir?",
        {
            'A': '102 (borç) 250.000 / 500 (alacak) 250.000',
            'B': '520 (borç) 150.000 + 542 (borç) 100.000 / 500 (alacak) 250.000',
            'C': '500 (borç) 250.000 / 520 (alacak) 150.000 + 542 (alacak) 100.000',
            'D': '501 (borç) 250.000 / 500 (alacak) 250.000',
            'E': '520 (borç) 150.000 + 542 (borç) 100.000 / 501 (alacak) 250.000',
        },
        'B',
        'İç kaynaklardan artırımda yedek hesapları borçlandırılarak kapatılır, 500 Sermaye doğrudan alacaklandırılır; ortaklardan taahhüt alınmadığı için 501 kullanılmaz. İşletmeye nakit girmez ve toplam özkaynak değişmez.',
        'THP 520, 542, 500; iç kaynaklardan sermaye artırımı',
    ),
    # düzey 2
    '0037': patch(
        'Genel kurul, geçmiş yıllar zararlarının olağanüstü yedeklerden karşılanmasına karar vermiş ve kayıt yapılmıştır. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Toplam özkaynak kapatılan zarar kadar artar',
            'B': '542 Olağanüstü Yedekler borçlandırılır',
            'C': 'Varlık ve yabancı kaynaklar etkilenmez',
            'D': '580 Geçmiş Yıllar Zararları alacaklandırılır',
            'E': 'Toplam özkaynak tutarı değişmez',
        },
        'A',
        'İşlem özkaynak içinde bir aktarımdır: negatif kalem (580) ile pozitif kalem (542) aynı tutarda azalır; **toplam özkaynak değişmez**, varlık ve yabancı kaynaklar etkilenmez.',
        'THP 580; özkaynak içi aktarım',
    ),
    # düzey 3
    '0038': patch(
        'Bir işletmenin dönem sonunda 690 Dönem Kârı veya Zararı hesabı 500.000 ₺ alacak kalanı vermektedir. Dönem kârı üzerinden 125.000 ₺ vergi karşılığı ayrılmıştır. Dönem sonu kapanış işlemleriyle ilgilire aşağıdakilerden hangisi yanlıştır?',
        {
            'A': '691 hesabı 125.000 ₺ borçlandırılır',
            'B': '590 hesabı 375.000 ₺ alacaklandırılır',
            'C': "692'nin alacak kalanı 375.000 ₺ olarak belirlenir",
            'D': 'Net kâr 591 Dönem Net Zararı hesabına devredilir',
            'E': '370 hesabı 125.000 ₺ alacaklandırılır',
        },
        'D',
        "Vergi karşılığı: 691 (borç) / 370 (alacak) 125.000. 690 ve 691, 692'ye devredilir; 692'nin alacak kalanı 500.000 − 125.000 = 375.000 ₺ olur ve **590 Dönem Net Kârı**'na devredilir. 591 yalnız net zarar durumunda kullanılır.",
        'THP 690, 691, 692, 590, 370',
    ),
    # düzey 3
    '0039': patch(
        "Sermayesi 500.000 ₺ olan bir anonim şirket sermayesini 800.000 ₺'ye çıkarmıştır. Artırılan tutarın 100.000 ₺'si olağanüstü yedeklerden karşılanmış, 200.000 ₺'si ise ortaklarca nominal değerden nakden ödenmiştir. Buna göre bu işlemler sonucunda toplam özkaynaktaki artış kaç ₺'dir?",
        {
            'A': '800.000 ₺',
            'B': '100.000 ₺',
            'C': '200.000 ₺',
            'D': 'Özkaynak değişmez',
            'E': '300.000 ₺',
        },
        'C',
        'İç kaynaklardan (100.000 ₺) artırım yalnız aktarımdır, toplamı değiştirmez. Ortakların nakden ödediği **200.000 ₺** dışarıdan yeni kaynak getirdiği için toplam özkaynağı artırır.',
        'Özkaynak hareketleri; iç ve dış kaynaklı artırım',
    ),
    # düzey 2
    '0040': patch(
        'Bir anonim şirketin genel kanuni yedek akçe uygulaması değerlendirilmektedir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': 'Sermayenin yarısını aşmadıkça zararların kapatılmasında kullanılabilir',
            'B': '540 Yasal Yedekler hesabında izlenir',
            'C': "Yıllık kârın %5'i oranında ayrılır",
            'D': 'Sınır ödenmiş sermayeye göre belirlenir',
            'E': "Toplam sermayenin %20'sine ulaşıncaya kadar ayrılır",
        },
        'E',
        "TTK m. 519/1 uyarınca I. tertip genel kanuni yedek akçe yıllık kârın %5'i oranında ve **ödenmiş sermayenin** %20'sine ulaşıncaya kadar ayrılır; ödenmemiş sermaye sınır hesabına katılmaz. Sermayenin yarısını aşmadıkça yalnız zararların kapatılması gibi amaçlarla kullanılabilir (m. 519/3).",
        '6102 sayılı TTK m. 519',
    ),
    # düzey 2
    '0041': patch(
        'Sermayesi 600.000 ₺ olan anonim şirket, sermayesini %40 artırmıştır. Artırılan sermayeyi temsil eden paylar nominal değerlerinin %25 fazlasına satılmıştır. Sermaye taahhüt kaydı daha önce yapılmış, satış bedelinin tamamı banka hesabına yatırılmıştır.\n\nÖdemenin kaydında aşağıdakilerden hangisi doğrudur?',
        {
            'A': '102 Bankalar 300.000 ₺ borçlu; 501 Ödenmemiş Sermaye 240.000 ₺ ve 520 Hisse Senetleri İhraç Primleri 60.000 ₺ alacaklı',
            'B': '501 Ödenmemiş Sermaye 240.000 ₺ borçlu; 102 Bankalar 240.000 ₺ alacaklı',
            'C': '102 Bankalar 240.000 ₺ borçlu; 501 Ödenmemiş Sermaye 240.000 ₺ alacaklı',
            'D': '102 Bankalar 300.000 ₺ borçlu; 501 Ödenmemiş Sermaye 300.000 ₺ alacaklı',
            'E': '102 Bankalar 300.000 ₺ borçlu; 501 Ödenmemiş Sermaye 240.000 ₺ ve 649 Diğer Olağan Gelir ve Kârlar 60.000 ₺ alacaklı',
        },
        'A',
        'Artırılan nominal sermaye 600.000 × %40 = **240.000 ₺**; ihraç primi 240.000 × %25 = **60.000 ₺** ve tahsilat **300.000 ₺**dir. Taahhüt önceden kaydedildiği için ödeme tarihinde 102 Bankalar 300.000 ₺ borçlandırılır; 501 Ödenmemiş Sermaye 240.000 ₺ ve 520 Hisse Senetleri İhraç Primleri 60.000 ₺ alacaklandırılır.',
        "1 Sıra No'lu MSUGT - 102/501/520; 2024-2026 SGS sermaye artırımı soru örüntüsü",
    ),
    # düzey 3
    '0042': patch(
        "Dönem başı özkaynağı 900.000 ₺ olan işletmede dönem içinde ortaklar 120.000 ₺ nakit sermaye koymuş, 180.000 ₺ kapsamlı gelir oluşmuş ve ortaklara 70.000 ₺ kâr payı dağıtılmıştır. Başka özkaynak hareketi yoktur.\n\nDönem sonu özkaynak kaç ₺'dir?",
        {
            'A': '1.130.000',
            'B': '1.270.000',
            'C': '1.200.000',
            'D': '1.290.000',
            'E': '1.210.000',
        },
        'A',
        'Dönem sonu özkaynak = 900.000 + 120.000 + 180.000 − 70.000 = **1.130.000 ₺**dir. Ortak katkısı ve kapsamlı gelir artırıcı, ortaklara dağıtım azaltıcı özkaynak hareketidir.',
        'TMS 1, par. 106(d) - özkaynak değişimlerinin mutabakatı',
    ),
    # düzey 2
    '0043': patch(
        'Aşağıdaki özkaynak kalemlerinin oluşum kaynaklarıyla ilgili ifadelerden hangisi doğrudur?',
        {
            'A': '520 Hisse Senetleri İhraç Primleri ve 542 Olağanüstü Yedekler, ikisi de kanunen zorunlu kâr yedeğidir.',
            'B': '520 Hisse Senetleri İhraç Primleri ile 540 Yasal Yedekler, ikisi de satış hasılatından doğan gelir hesabıdır.',
            'C': '520 Hisse Senetleri İhraç Primleri sermaye işleminden; 540 ve 542 hesapları ise kârın ayrılmasından doğar.',
            'D': '540 Yasal Yedekler sermaye taahhüdünden, 501 Ödenmemiş Sermaye ise dönem kârından oluşur.',
            'E': '542 Olağanüstü Yedekler bir borçlanma işlemiyle, 520 Hisse Senetleri İhraç Primleri ise dönem zararından oluşur.',
        },
        'C',
        '**520 Hisse Senetleri İhraç Primleri** nominal değerin üzerindeki pay ihracından doğan sermaye yedeğidir. **540 Yasal Yedekler** ve **542 Olağanüstü Yedekler** ise kârın ayrılmasıyla oluşan kâr yedekleridir.',
        "1 Sıra No'lu MSUGT - 52 Sermaye Yedekleri ve 54 Kâr Yedekleri",
    ),
    # düzey 3
    '0044': patch(
        "Ödenmiş sermayesi 1.000.000 ₺ ve daha önce ayrılmış genel kanuni yedek akçesi 100.000 ₺ olan bir anonim şirketin dönem net kârı 400.000 ₺'dir. Genel kurul, TTK'ya göre ayrılması gereken birinci ve ikinci tertip genel kanuni yedek akçeleri ayırmaya, ortaklara (sermayenin %5'i oranındaki birinci kâr payı dâhil) toplam 150.000 ₺ kâr payı dağıtmaya ve kalan tutarı olağanüstü yedeklere aktarmaya karar vermiştir. Başka dağıtım yoktur.\n\nBuna göre '542 Olağanüstü Yedekler' hesabına aktarılacak tutar kaç ₺'dir?",
        {
            'A': '230.000',
            'B': '250.000',
            'C': '215.000',
            'D': '220.000',
            'E': '210.000',
        },
        'D',
        "Birinci tertip: kârın %5'i = 20.000 ₺ (mevcut 100.000 + 20.000, sermayenin %20'si olan 200.000 ₺'yi aşmaz). İkinci tertip: pay sahiplerine %5 kâr payı (50.000 ₺) ödendikten sonra kâr payı alacaklara dağıtılacak tutarın %10'u = (150.000 − 50.000) × %10 = 10.000 ₺. Olağanüstü yedek = 400.000 − 20.000 − 150.000 − 10.000 = 220.000 ₺.",
        "TTK md. 519 (I. tertip %5); 1 Sıra No'lu MSUGT - 540",
    ),
    # düzey 2
    '0045': patch(
        'Genel kurul 120.000 ₺ nakit kâr payı dağıtılmasına karar vermiş, ancak dönem sonuna kadar ödeme yapılmamıştır. Karar tarihinde bu işlemin finansal durum tablosuna etkisi hangisidir?',
        {
            'A': 'Karar tarihinde finansal tablolar değişmez; etki ödemede doğar.',
            'B': 'Özkaynak azalır, yabancı kaynak artar; varlıklar değişmez.',
            'C': 'Özkaynak ve varlıklar 120.000 ₺ azalır; yabancı kaynaklar değişmez.',
            'D': 'Özkaynak bileşenleri arasında aktarım olur; toplam özkaynak değişmez.',
            'E': 'Varlıklar 120.000 ₺ artar, özkaynak 120.000 ₺ azalır.',
        },
        'B',
        'Kâr payı kararıyla dağıtılacak kâr özkaynaktan çıkar ve ödeme yapılıncaya kadar **331 Ortaklara Borçlar** hesabında yükümlülük olur. Henüz nakit çıkmadığı için karar tarihinde varlıklar değişmez.',
        "TMS 32, par. 35; 1 Sıra No'lu MSUGT - 570/331",
    ),
    # düzey 3
    '0046': patch(
        "Ödenmiş sermayesi 1.000.000 ₺, daha önce ayrılmış genel kanuni yedek akçesi 195.000 ₺ ve yıllık kârı 200.000 ₺ olan anonim şirkette, üst sınıra ulaşılıncaya kadar ayrılması gereken I. tertip genel kanuni yedek akçe kaç ₺'dir?",
        {
            'A': '5.000',
            'B': '10.000',
            'C': '20.000',
            'D': '40.000',
            'E': '195.000',
        },
        'A',
        "Yıllık kârın %5'i 10.000 ₺ olsa da genel kanuni yedeğin ilk sınırı ödenmiş sermayenin %20'si, yani **200.000 ₺**dir. Mevcut yedek 195.000 ₺ olduğundan yalnız **5.000 ₺** ayrılır.",
        'TTK md. 519/1',
    ),
    # düzey 2
    '0047': patch(
        'Şirket, ortaklardan nakden karşılanmak üzere 450.000 ₺ sermaye artırmış; taahhüt ve ödeme işlemleri aynı dönem içinde tamamlanmıştır. İşlem öncesine göre finansal durum tablosundaki değişim hangisidir?',
        {
            'A': 'Varlıklar 450.000 ₺ azalır, özkaynak değişmez.',
            'B': 'Varlıklar ve yabancı kaynaklar 450.000 ₺ artar.',
            'C': 'Yabancı kaynaklar 450.000 ₺ azalır, özkaynak artar.',
            'D': 'Özkaynak hesapları arasında aktarım olur; toplam değişmez.',
            'E': 'Varlıklar ve özkaynak 450.000 ₺ artar; borçlar değişmez.',
        },
        'E',
        'Nakit sermaye artırımında banka mevcudu, dolayısıyla varlıklar **450.000 ₺ artar**. Aynı tutarda ödenmiş sermaye oluştuğu için özkaynak da artar; işlem borç doğurmadığından yabancı kaynaklar değişmez.',
        "Temel muhasebe eşitliği; 1 Sıra No'lu MSUGT - 102/500/501",
    ),
    # düzey 3
    '0048': patch(
        'Aşağıdaki hesaplardan hangileri özkaynak (5) niteliğindedir?\n\nI. 500 Sermaye\n\nII. 540 Yasal Yedekler\n\nIII. 320 Satıcılar',
        {
            'A': 'II ve III',
            'B': 'Yalnız III',
            'C': 'I ve II',
            'D': 'I, II ve III',
            'E': 'Yalnız I',
        },
        'C',
        '**I (500 Sermaye)** ve **II (540 Yasal Yedekler)** özkaynak kalemleridir. **III (320 Satıcılar)** ise bir ticari borçtur (yabancı kaynak). Doğru cevap **I ve II**.',
        "1 Sıra No'lu MSUGT - 5 vs 3 grubu",
    ),
    # düzey 3
    '0049': patch(
        "Dönem başı özkaynağı 1.200.000 ₺ olan işletmenin dönem içinde toplam kapsamlı geliri 220.000 ₺, ortakların sermaye katkısı 150.000 ₺ ve ortaklara dağıtımı 90.000 ₺'dir. Ayrıca 40.000 ₺ ödenerek işletmenin kendi payları geri alınmıştır.\n\nDönem sonu özkaynak kaç ₺'dir?",
        {
            'A': '1.440.000',
            'B': '1.400.000',
            'C': '1.480.000',
            'D': '1.350.000',
            'E': '1.520.000',
        },
        'A',
        'Dönem sonu özkaynak = 1.200.000 + 220.000 + 150.000 − 90.000 − 40.000 = **1.440.000 ₺**dir. Toplam kapsamlı gelir ve ortak katkısı artırır; dağıtım ve geri alınan kendi payları azaltır.',
        'TMS 1, par. 106(d); TMS 32, par. 33',
    ),
    # düzey 2
    '0050': patch(
        'Nakit (bedelli) sermaye artırımı ile iç kaynaklardan (bedelsiz) sermaye artırımı arasındaki fark ile ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': 'İkisi de bir yabancı kaynak hareketi olarak kaydedilir; çünkü sermaye artırımı işletmenin ortaklara olan uzun vadeli borcunu temsil eden bir yükümlülük doğurur.',
            'B': 'İkisinde de ortaklardan işletmeye dışarıdan nakit girer; bu nedenle her iki artırım türünde de 102 Bankalar hesabı borçlandırılır ve işletmenin varlıkları aynı tutarda artar.',
            'C': 'İkisi de toplam özkaynağı azaltır; çünkü sermaye artırımı sırasında ayrılan yedekler ve dağıtılan kâr payları özkaynak hesaplarından düşülerek ortaklara aktarılır.',
            'D': 'Bedelli artırımda ortaklardan yeni kaynak (nakit) gelir ve özkaynak artar; bedelsiz artırımda ise mevcut yedek/kârlar sermayeye eklenir, toplam özkaynak değişmez.',
            'E': 'Bedelsiz artırımda işletmeye dışarıdan nakit girer, bedelli artırımda ise mevcut yedekler sermayeye aktarılır.',
        },
        'D',
        '**Bedelli (nakit) artırımda** ortaklardan yeni kaynak gelir, **toplam özkaynak artar**. **Bedelsiz (iç kaynaklardan) artırımda** yedek/kârlar sermayeye aktarılır; işletmeye nakit girmediğinden **toplam özkaynak değişmez**.',
        "1 Sıra No'lu MSUGT - 500 / 540 / 570",
    ),
    # düzey 3
    '0051': patch(
        "Sermayesi 1.000.000 ₺ olan bir anonim şirket sermayesini 1.600.000 ₺'ye çıkarmıştır. Artırılan tutarın 200.000 ₺'si olağanüstü yedeklerden (iç kaynaklardan), 400.000 ₺'si nakden karşılanmıştır. Nakden karşılanan kısım için 400.000 ₺ nominal değerli paylar 500.000 ₺'ye ihraç edilmiş ve bedelin tamamı bankaya yatırılmıştır.\n\nBuna göre bu işlemler sonucunda şirketin toplam özkaynakları kaç ₺ artar?",
        {
            'A': '600.000',
            'B': '700.000',
            'C': '500.000',
            'D': '400.000',
            'E': '800.000',
        },
        'C',
        'İç kaynaklardan artırım (542 borç / 500 alacak) özkaynak içinde yer değiştirmedir, toplamı değiştirmez. Nakdi artırımda bankaya giren 500.000 ₺ özkaynağı artırır: 500 Sermaye 400.000 ₺ ve 520 Hisse Senedi İhraç Primleri 100.000 ₺ alacak. Toplam artış 500.000 ₺.',
        "1 Sıra No'lu MSUGT - 542/570/500; TTK md. 462",
    ),
    # düzey 2
    '0052': patch(
        "Sermayesi 1.500.000 ₺ olan anonim şirket sermayesini %20 artırmıştır. Artırılan sermayeyi temsil eden payların tamamı nominal değerinin %10 fazlasına satılmış ve bedel banka hesabına yatırılmıştır.\n\nBanka hesabına yatırılan toplam tutar kaç ₺'dir?",
        {
            'A': '150.000',
            'B': '300.000',
            'C': '450.000',
            'D': '315.000',
            'E': '330.000',
        },
        'E',
        'Artırılan nominal sermaye 1.500.000 × %20 = **300.000 ₺**dir. İhraç primi 300.000 × %10 = **30.000 ₺** olduğundan bankaya yatırılan tutar 300.000 + 30.000 = **330.000 ₺**dir.',
        "1 Sıra No'lu MSUGT - 102/501/520",
    ),
    # düzey 3
    '0053': patch(
        "Yeni kurulan bir anonim şirketin ortakları 1.000.000 ₺ nakdi sermaye taahhüt etmiş ve taahhüt kaydı yapılmıştır. Ortaklar tescilden önce taahhüt ettikleri sermayenin %40'ını şirketin banka hesabına yatırmıştır. Bu ödemenin kaydıyla ilgili aşağıdakilerden hangisi doğrudur?",
        {
            'A': '501 Ödenmemiş Sermaye hesabı 400.000 ₺ alacaklandırılır',
            'B': '501 Ödenmemiş Sermaye hesabı 1.000.000 ₺ alacaklandırılır',
            'C': '500 Sermaye hesabı 400.000 ₺ borçlandırılır',
            'D': '102 Bankalar hesabı 1.000.000 ₺ borçlandırılır',
            'E': '500 Sermaye hesabı 600.000 ₺ alacaklandırılır',
        },
        'A',
        "Taahhütte 501 (borç) / 500 (alacak) 1.000.000 yazılmıştır. Ödemede ödenmemiş sermaye azalır: 102 Bankalar (borç) 400.000 / **501 Ödenmemiş Sermaye (alacak) 400.000**. 500 Sermaye taahhüt edilen tutarla kalır; kalan 600.000 ₺ 501'de izlenmeye devam eder.",
        '6102 sayılı TTK m. 344; THP 500, 501',
    ),
    # düzey 2
    '0054': patch(
        'Bir anonim şirketin kuruluşunda ortaklar nakdi sermaye taahhüt etmiştir. Buna göre aşağıdakilerden hangisi yanlıştır?',
        {
            'A': '501 bilançoda sermayeden indirilerek gösterilir',
            'B': "Nakdi payların en az %25'i tescilden önce ödenir",
            'C': 'Taahhüt edilen sermaye tutarı 500 Sermaye hesabının alacağına yazılır',
            'D': 'Nakdi payların itibari değerinin tamamı tescilden önce ödenir',
            'E': "Taahhüt tutarı 501 Ödenmemiş Sermaye'nin borcuna yazılır",
        },
        'D',
        "TTK m. 344 uyarınca nakden taahhüt edilen payların itibari değerlerinin **en az %25'i** tescilden önce ödenir; kalan tutar tescili izleyen yirmi dört ay içinde ödenir. Tamamının tescilden önce ödenmesi zorunlu değildir.",
        '6102 sayılı TTK m. 344; THP 500, 501',
    ),
    # düzey 3
    '0055': patch(
        "Bir işletmenin dönem başında varlık toplamı 800.000 ₺, yabancı kaynak toplamı 300.000 ₺; dönem sonunda varlık toplamı 1.100.000 ₺, yabancı kaynak toplamı 420.000 ₺'dir. Dönem içinde ortaklar 60.000 ₺ nakit sermaye koymuş, ortaklara 40.000 ₺ kâr payı ödenmiştir. Başka özkaynak hareketi yoktur. Buna göre işletmenin dönem kâr veya zararı aşağıdakilerden hangisidir?",
        {
            'A': '120.000 ₺ kâr',
            'B': '220.000 ₺ kâr',
            'C': '180.000 ₺ kâr',
            'D': '80.000 ₺ zarar',
            'E': '160.000 ₺ kâr',
        },
        'E',
        'Özkaynak: dönem başı 800.000 − 300.000 = 500.000 ₺; dönem sonu 1.100.000 − 420.000 = 680.000 ₺; artış 180.000 ₺. Sermaye katkısı kârdan kaynaklanmadığından düşülür, dağıtılan kâr payı ise eklenir: 180.000 − 60.000 + 40.000 = **160.000 ₺ kâr**.',
        'Temel bilanço eşitliği; özkaynak hareketleri',
    ),
    # düzey 2
    '0056': patch(
        'Bir anonim şirketin yıl içindeki işlemleri değerlendirilmektedir. Buna göre aşağıdaki işlemlerden hangisi şirketin toplam özkaynaklarını artırmaz?',
        {
            'A': 'Dönem net kârı elde edilmesi',
            'B': 'Olağanüstü yedeklerin sermayeye eklenmesi',
            'C': 'Ortağın üretimde kullanılacak makine ile sermaye koyması',
            'D': 'Ortakların nakit sermaye koyması',
            'E': 'Payların primli olarak satılması',
        },
        'B',
        'Olağanüstü yedeklerin sermayeye eklenmesi özkaynak kalemleri arasında **aktarımdır**; toplam özkaynak değişmez. Nakit veya ayni sermaye konması, primli pay satışı ve net kâr toplam özkaynağı artırır.',
        'Özkaynak hareketleri',
    ),
    # düzey 3
    '0057': patch(
        '570 Geçmiş Yıllar Kârları hesabındaki 800.000 ₺ için genel kurul; 40.000 ₺ yasal yedek, 60.000 ₺ statü yedeği ayrılmasına, ortaklara 450.000 ₺ kâr payı dağıtılmasına ve kalanın olağanüstü yedek olarak şirkette bırakılmasına karar vermiştir. Buna göre kâr dağıtım kaydıyla ilgili aşağıdakilerden hangisi doğrudur?',
        {
            'A': '542 Olağanüstü Yedekler hesabı 250.000 ₺ alacaklandırılır',
            'B': '542 Olağanüstü Yedekler hesabı 350.000 ₺ alacaklandırılır',
            'C': '331 Ortaklara Borçlar hesabı 450.000 ₺ borçlandırılır',
            'D': '540 Yasal Yedekler hesabı 60.000 ₺ alacaklandırılır',
            'E': '570 Geçmiş Yıllar Kârları hesabı 800.000 ₺ alacaklandırılır',
        },
        'A',
        "Kayıt: 570 (borç) 800.000 / 540 (alacak) 40.000 + 541 (alacak) 60.000 + 331 (alacak) 450.000 + **542 (alacak) 250.000**. Olağanüstü yedek 800.000 − 40.000 − 60.000 − 450.000 = 250.000 ₺'dir.",
        'THP 570, 540, 541, 542, 331',
    ),
    # düzey 2
    '0058': patch(
        'Sermayesi 1.000.000 ₺ olan bir anonim şirketin 580 Geçmiş Yıllar Zararları hesabında 250.000 ₺ bulunmaktadır. Zararın kapatılması amacıyla sermayenin 250.000 ₺ azaltılmasına karar verilmiş ve azaltım tescil edilmiştir. Buna göre yapılacak kayıt aşağıdakilerden hangisidir?',
        {
            'A': '500 (borç) 250.000 / 102 (alacak) 250.000',
            'B': '500 (borç) 250.000 / 331 (alacak) 250.000',
            'C': '501 (borç) 250.000 / 580 (alacak) 250.000',
            'D': '500 (borç) 250.000 / 580 (alacak) 250.000',
            'E': '580 (borç) 250.000 / 500 (alacak) 250.000',
        },
        'D',
        'Zararı kapatmak için yapılan sermaye azaltımında ortaklara ödeme yapılmaz; sermaye azaltılan tutar kadar borçlandırılır ve **580 alacaklandırılarak** kapatılır. Toplam özkaynak değişmez.',
        '6102 sayılı TTK m. 473-474; THP 500, 580',
    ),
    # düzey 3
    '0059': patch(
        'Özkaynak hesaplarıyla ilgili aşağıdaki ifadelerden hangileri doğrudur?\n\nI. 501 Ödenmemiş Sermaye, sermayeyi düzenleyen ve özkaynağı azaltan bir hesaptır.\n\nII. Hisse senedi ihraç primi bir kâr yedeğidir.\n\nIII. İç kaynaklardan sermaye artırımı toplam özkaynağı değiştirmez.',
        {
            'A': 'Yalnız III',
            'B': 'I ve III',
            'C': 'II ve III',
            'D': 'I ve II',
            'E': 'Yalnız I',
        },
        'B',
        'I ve III doğrudur. II yanlıştır: ihraç primi faaliyet kârından değil pay satışından doğar; **52 Sermaye Yedekleri** grubundadır.',
        'THP 500, 501, 520',
    ),
    # düzey 2
    '0060': patch(
        'Bir kollektif şirketin yevmiye defterinde şu kayıt yer almaktadır: 153 Ticari Mallar (borç) 20.000, 254 Taşıtlar (borç) 20.000, 255 Demirbaşlar (borç) 20.000 / 501 Ödenmemiş Sermaye (alacak) 60.000 (KDV ihmal). Buna göre bu kayıt aşağıdaki işlemlerden hangisine aittir?',
        {
            'A': 'Şirketin varlıklarını vadeli satın alması',
            'B': 'İç kaynaklardan sermaye artırılması',
            'C': 'Şirketin varlıklarını ortaklara kâr payı olarak vermesi',
            'D': 'Ortakların sermaye taahhüdünü ayni olarak yerine getirmesi',
            'E': "Ortakların sermaye taahhüdünde bulunması ve 500'ün alacaklandırılması",
        },
        'D',
        "501 Ödenmemiş Sermaye'nin alacaklandırılması taahhüt edilen sermayenin ödendiğini gösterir; borç tarafında nakit yerine ticari mal, taşıt ve demirbaş bulunduğundan taahhüt **ayni olarak** yerine getirilmiştir. Taahhüt kaydında 501 borçlandırılır, 500 alacaklandırılır.",
        'THP 153, 254, 255, 501',
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
    print(f"1 paket / {len(PATCHES)} soru ('Ozkaynaklar' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
