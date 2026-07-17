#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SMMM Finansal Tablolar ve Analizi — Oran Analizi, 3×20.

Likidite, mali yapı, faaliyet ve kârlılık oranları farklı veri setleriyle
uygulanır. Bütün sayısal sonuçlar builder çalışırken hesaplanır.
"""
from topic_pack_builder import write_topic


def tr(value):
    value = round(value, 2)
    if abs(value - round(value)) < 1e-9:
        return f"{int(round(value)):,}".replace(",", ".")
    return f"{value:,.2f}".replace(",", "\0").replace(".", ",").replace("\0", ".")


def num(value, unit=""):
    return f"{tr(value)}{unit}"


def c(scenario, focus, correct, focus_correct, distractors, focus_distractors,
      why, focus_why, ref, difficulty="medium"):
    return {
        "scenario": scenario, "focus": focus,
        "correct": correct, "focus_correct": focus_correct,
        "distractors": distractors, "focus_distractors": focus_distractors,
        "why": why, "focus_why": focus_why, "ref": ref,
        "difficulty": difficulty,
    }


def r(scenario, focus, correct, focus_correct, distractors, focus_distractors,
      why, focus_why, ref, difficulty="medium"):
    return c(scenario, focus, correct, focus_correct, distractors,
             focus_distractors, why, focus_why, ref, difficulty)


RULES = [
    c(
        "Dönen varlıkları 960 bin TL, kısa vadeli yabancı kaynakları 480 bin TL olan işletmenin cari oranı kaçtır?",
        "Cari oranı 1,80 ve kısa vadeli yabancı kaynakları 750 bin TL olan işletmenin dönen varlıkları kaç bin TL'dir?",
        num(960/480), num(1.8*750, " bin TL"),
        [num(.5), num(1.5), num(2.5), num(3)],
        [num(417, " bin TL"), num(750, " bin TL"), num(1080, " bin TL"), num(2100, " bin TL")],
        "Cari oran = Dönen Varlıklar / Kısa Vadeli Yabancı Kaynaklar = 960 / 480 = 2'dir.",
        "Dönen Varlıklar = Cari Oran × KVYK = 1,80 × 750 = 1.350 bin TL'dir.",
        "Finansal tablo analizi - cari oran", "easy",
    ),
    c(
        "Dönen varlıkları 820 bin TL, kısa vadeli yabancı kaynakları 510 bin TL olan işletmenin net işletme sermayesi kaç bin TL'dir?",
        "Net işletme sermayesi 480 bin TL ve kısa vadeli yabancı kaynakları 920 bin TL olan işletmenin dönen varlıkları kaç bin TL'dir?",
        num(820-510, " bin TL"), num(480+920, " bin TL"),
        [num(510, " bin TL"), num(820, " bin TL"), num(1330, " bin TL"), num(418.2, " bin TL")],
        [num(280, " bin TL"), num(920, " bin TL"), num(1880, " bin TL"), num(2320, " bin TL")],
        "Net işletme sermayesi = Dönen Varlıklar − Kısa Vadeli Yabancı Kaynaklar = 820 − 510 = 310 bin TL'dir.",
        "Dönen varlıklar = Net İşletme Sermayesi + KVYK = 480 + 920 = 1.400 bin TL'dir.",
        "Finansal tablo analizi - net işletme sermayesi", "easy",
    ),
    c(
        "Dönen varlıkları 960 bin TL, stokları 300 bin TL ve kısa vadeli yabancı kaynakları 480 bin TL olan işletmenin asit-test oranı kaçtır?",
        "Dönen varlıkları 1.350 bin TL, asit-test oranı 1,20 ve kısa vadeli yabancı kaynakları 750 bin TL olan işletmenin stokları kaç bin TL'dir?",
        num((960-300)/480), num(1350-1.2*750, " bin TL"),
        [num(.63), num(1), num(2), num(2.63)],
        [num(225, " bin TL"), num(600, " bin TL"), num(750, " bin TL"), num(900, " bin TL")],
        "Asit-test oranı = (Dönen Varlıklar − Stoklar) / KVYK = (960 − 300) / 480 = 1,38'dir.",
        "Stoklar = Dönen Varlıklar − Asit-test Oranı × KVYK = 1.350 − 1,20 × 750 = 450 bin TL'dir.",
        "Finansal tablo analizi - asit-test oranı", "medium",
    ),
    c(
        "Hazır değerleri ve menkul kıymetleri toplamı 210 bin TL, kısa vadeli yabancı kaynakları 600 bin TL olan işletmenin nakit oranı kaçtır?",
        "Nakit oranı 0,40 ve kısa vadeli yabancı kaynakları 800 bin TL olan işletmenin hazır değerleri ile menkul kıymetleri toplamı kaç bin TL'dir?",
        num(210/600), num(.4*800, " bin TL"),
        [num(.29), num(.6), num(2.86), num(3.5)],
        [num(200, " bin TL"), num(400, " bin TL"), num(480, " bin TL"), num(2000, " bin TL")],
        "Nakit oranı = (Hazır Değerler + Menkul Kıymetler) / KVYK = 210 / 600 = 0,35'tir.",
        "Hazır Değerler + Menkul Kıymetler = Nakit Oranı × KVYK = 0,40 × 800 = 320 bin TL'dir.",
        "Finansal tablo analizi - nakit oranı", "easy",
    ),
    c(
        "Net satışları 2.400 bin TL, ortalama net işletme sermayesi 400 bin TL olan işletmenin net işletme sermayesi devir hızı kaçtır?",
        "Net işletme sermayesi devir hızı 5 ve net satışları 3.500 bin TL olan işletmenin ortalama net işletme sermayesi kaç bin TL'dir?",
        num(2400/400), num(3500/5, " bin TL"),
        [num(.17), num(2.4), num(5), num(8)],
        [num(175, " bin TL"), num(500, " bin TL"), num(875, " bin TL"), num(17500, " bin TL")],
        "Net işletme sermayesi devir hızı = Net Satışlar / Ortalama Net İşletme Sermayesi = 2.400 / 400 = 6'dır.",
        "Ortalama net işletme sermayesi = Net Satışlar / Devir Hızı = 3.500 / 5 = 700 bin TL'dir.",
        "Finansal tablo analizi - işletme sermayesi devir hızı", "medium",
    ),
    c(
        "Toplam yabancı kaynakları 1.200 bin TL, toplam varlıkları 2.000 bin TL olan işletmenin finansal kaldıraç oranı kaçtır?",
        "Finansal kaldıraç oranı %50 ve toplam varlıkları 1.800 bin TL olan işletmenin toplam yabancı kaynakları kaç bin TL'dir?",
        num(1200/2000*100, "%"), num(.5*1800, " bin TL"),
        [num(40, "%"), num(66.67, "%"), num(80, "%"), num(166.67, "%")],
        [num(450, " bin TL"), num(800, " bin TL"), num(1000, " bin TL"), num(3600, " bin TL")],
        "Finansal kaldıraç oranı = Toplam Yabancı Kaynaklar / Toplam Varlıklar = 1.200 / 2.000 = %60'tır.",
        "Toplam Yabancı Kaynaklar = Kaldıraç Oranı × Toplam Varlıklar = %50 × 1.800 = 900 bin TL'dir.",
        "Finansal tablo analizi - finansal kaldıraç", "easy",
    ),
    c(
        "Toplam yabancı kaynakları 1.200 bin TL, özkaynakları 800 bin TL olan işletmenin borç/özkaynak oranı kaçtır?",
        "Borç/özkaynak oranı 1 ve toplam yabancı kaynakları 900 bin TL olan işletmenin özkaynakları kaç bin TL'dir?",
        num(1200/800), num(900/1, " bin TL"),
        [num(.67), num(.8), num(2), num(2.5)],
        [num(450, " bin TL"), num(810, " bin TL"), num(1000, " bin TL"), num(1800, " bin TL")],
        "Borç/özkaynak oranı = Toplam Yabancı Kaynaklar / Özkaynaklar = 1.200 / 800 = 1,50'dir.",
        "Özkaynaklar = Toplam Borç / Borç-Özkaynak Oranı = 900 / 1 = 900 bin TL'dir.",
        "Finansal tablo analizi - borç/özkaynak oranı", "easy",
    ),
    c(
        "Özkaynakları 800 bin TL, toplam kaynakları 2.000 bin TL olan işletmenin özkaynak oranı kaçtır?",
        "Özkaynak oranı %55 olan işletmenin kaynak yapısı için hangi yorum doğrudur?",
        num(800/2000*100, "%"), "Kaynakların %55'i özkaynak, %45'i yabancı kaynaktır",
        [num(25, "%"), num(60, "%"), num(80, "%"), num(250, "%")],
        ["Kaynakların %45'i özkaynak, %55'i yabancı kaynaktır", "Varlıkların %55'i duran, %45'i dönen varlıktır", "Satışların %55'i brüt kâr, %45'i faaliyet gideridir", "Kısa vadeli borçların %55'i nakitle karşılanmaktadır"],
        "Özkaynak oranı = Özkaynaklar / Toplam Kaynaklar = 800 / 2.000 = %40'tır.",
        "Özkaynak oranı %55 ise toplam kaynakların %55'i özkaynakla, kalan %45'i yabancı kaynakla finanse edilmiştir.",
        "Finansal tablo analizi - özkaynak oranı", "easy",
    ),
    c(
        "Duran varlıkları 900 bin TL, özkaynakları 1.200 bin TL olan işletmenin duran varlıklar/özkaynaklar oranı kaçtır?",
        "Duran varlıklar/özkaynaklar oranı 1,25 ve özkaynakları 1.200 bin TL olan işletmenin duran varlıkları kaç bin TL'dir?",
        num(900/1200), num(1.25*1200, " bin TL"),
        [num(.33), num(1.25), num(1.33), num(2.1)],
        [num(960, " bin TL"), num(1200, " bin TL"), num(1440, " bin TL"), num(2250, " bin TL")],
        "Duran varlıklar/özkaynaklar = 900 / 1.200 = 0,75'tir; özkaynaklar duran varlıkları karşılamaktadır.",
        "Duran Varlıklar = 1,25 × 1.200 = 1.500 bin TL'dir. Tutar özkaynakları aştığı için duran varlığın bir bölümü yabancı kaynakla finanse edilmiştir.",
        "Finansal tablo analizi - duran varlık finansmanı", "medium",
    ),
    c(
        "Faiz ve vergi öncesi kârı 600 bin TL, finansman gideri 120 bin TL olan işletmenin faiz karşılama oranı kaçtır?",
        "Faiz karşılama oranı 4 ve finansman gideri 180 bin TL olan işletmenin faiz ve vergi öncesi kârı kaç bin TL'dir?",
        num(600/120), num(4*180, " bin TL"),
        [num(.2), num(2), num(4), num(6)],
        [num(45, " bin TL"), num(176, " bin TL"), num(450, " bin TL"), num(900, " bin TL")],
        "Faiz karşılama oranı = Faiz ve Vergi Öncesi Kâr / Finansman Gideri = 600 / 120 = 5'tir.",
        "Faiz ve Vergi Öncesi Kâr = Faiz Karşılama Oranı × Finansman Gideri = 4 × 180 = 720 bin TL'dir.",
        "Finansal tablo analizi - faiz karşılama oranı", "medium",
    ),
    c(
        "Satışların maliyeti net satışların %70'i olan işletmenin brüt kâr marjı kaçtır?",
        "Brüt kâr marjı %28 ve net satışları 4.000 bin TL olan işletmenin brüt satış kârı kaç bin TL'dir?",
        num((1-.70)*100, "%"), num(.28*4000, " bin TL"),
        [num(23.33, "%"), num(33.33, "%"), num(42.86, "%"), num(70, "%")],
        [num(280, " bin TL"), num(1000, " bin TL"), num(1400, " bin TL"), num(2880, " bin TL")],
        "Brüt kâr marjı = 1 − Satışların Maliyeti Oranı = %100 − %70 = %30'dur.",
        "Brüt Satış Kârı = Brüt Kâr Marjı × Net Satışlar = %28 × 4.000 = 1.120 bin TL'dir.",
        "Finansal tablo analizi - brüt kâr marjı", "easy",
    ),
    c(
        "Net satışları 3.200 bin TL, brüt satış kârı 800 bin TL ve faaliyet giderleri 320 bin TL olan işletmenin faaliyet kâr marjı kaçtır?",
        "Faaliyet kârı 630 bin TL ve faaliyet kâr marjı %18 olan işletmenin net satışları kaç bin TL'dir?",
        num((800-320)/3200*100, "%"), num(630/.18, " bin TL"),
        [num(12, "%"), num(16.67, "%"), num(20, "%"), num(85, "%")],
        [num(113, " bin TL"), num(2867, " bin TL"), num(3810, " bin TL"), num(11340, " bin TL")],
        "Faaliyet kârı = 800 − 320 = 480 bin TL; faaliyet kâr marjı = 480 / 3.200 = %15'tir.",
        "Net Satışlar = Faaliyet Kârı / Faaliyet Kâr Marjı = 630 / 0,18 = 3.500 bin TL'dir.",
        "Finansal tablo analizi - faaliyet kâr marjı", "easy",
    ),
    c(
        "İşletme her 100 TL net satıştan 10 TL net dönem kârı elde ediyorsa net kâr marjı kaçtır?",
        "Net kâr marjı %12 olarak hesaplanan işletme için bu sonuç nasıl yorumlanır?",
        num(10/100*100, "%"), "Her 100 TL net satışın 12 TL'si net kâra dönüşmüştür",
        [num(8, "%"), num(11.11, "%"), num(30, "%"), num(90, "%")],
        ["Her 100 TL varlığın 12 TL'si nakit olarak tutulmuştur", "Her 100 TL borcun 12 TL'si özkaynakla karşılanmıştır", "Her 100 TL net satış için 12 TL faaliyet gideri oluşmuştur", "Her 100 TL özkaynak 12 TL net satış yaratmıştır"],
        "Net kâr marjı, her 100 TL satıştan kalan net kârı gösterir; 10 / 100 = %10'dur.",
        "Net kâr marjı %12 ise her 100 TL net satışın 12 TL'si bütün gider ve vergiler sonrasında net dönem kârı olarak kalmıştır.",
        "Finansal tablo analizi - net kâr marjı", "easy",
    ),
    c(
        "Net dönem kârı 360 bin TL; dönem başı varlıkları 2.400 bin TL, dönem sonu varlıkları 2.800 bin TL olan işletmenin ortalama aktife göre aktif kârlılığı kaçtır?",
        "Aktif kârlılığı %15 ve ortalama toplam varlıkları 3.000 bin TL olan işletmenin net dönem kârı kaç bin TL'dir?",
        num(360/((2400+2800)/2)*100, "%"), num(.15*3000, " bin TL"),
        [num(12.86, "%"), num(14.4, "%"), num(15, "%"), num(72.22, "%")],
        [num(200, " bin TL"), num(400, " bin TL"), num(500, " bin TL"), num(2000, " bin TL")],
        "Ortalama varlık = (2.400 + 2.800) / 2 = 2.600; aktif kârlılığı = 360 / 2.600 = %13,85'tir.",
        "Net Dönem Kârı = Aktif Kârlılığı × Ortalama Toplam Varlıklar = %15 × 3.000 = 450 bin TL'dir.",
        "Finansal tablo analizi - aktif kârlılığı", "medium",
    ),
    c(
        "Net dönem kârı 300 bin TL; dönem başı özkaynakları 1.000 bin TL, dönem sonu özkaynakları 1.400 bin TL olan işletmenin özkaynak kârlılığı kaçtır?",
        "Özkaynak kârlılığı %30 ve ortalama özkaynakları 1.400 bin TL olan işletmenin net dönem kârı kaç bin TL'dir?",
        num(300/((1000+1400)/2)*100, "%"), num(.30*1400, " bin TL"),
        [num(21.43, "%"), num(27.27, "%"), num(30, "%"), num(400, "%")],
        [num(280, " bin TL"), num(400, " bin TL"), num(467, " bin TL"), num(4200, " bin TL")],
        "Ortalama özkaynak = (1.000 + 1.400) / 2 = 1.200; özkaynak kârlılığı = 300 / 1.200 = %25'tir.",
        "Net Dönem Kârı = Özkaynak Kârlılığı × Ortalama Özkaynaklar = %30 × 1.400 = 420 bin TL'dir.",
        "Finansal tablo analizi - özkaynak kârlılığı", "medium",
    ),
    c(
        "Net satışları 3.600 bin TL, ortalama toplam varlıkları 2.400 bin TL olan işletmenin aktif devir hızı kaçtır?",
        "Aktif devir hızı 1,40 ve ortalama toplam varlıkları 3.000 bin TL olan işletmenin net satışları kaç bin TL'dir?",
        num(3600/2400), num(1.4*3000, " bin TL"),
        [num(.67), num(1.2), num(2.4), num(6)],
        [num(2143, " bin TL"), num(3000, " bin TL"), num(4400, " bin TL"), num(9000, " bin TL")],
        "Aktif devir hızı = Net Satışlar / Ortalama Toplam Varlıklar = 3.600 / 2.400 = 1,50'dir.",
        "Net Satışlar = Aktif Devir Hızı × Ortalama Toplam Varlıklar = 1,40 × 3.000 = 4.200 bin TL'dir.",
        "Finansal tablo analizi - aktif devir hızı", "easy",
    ),
    c(
        "Kredili net satışları 2.400 bin TL; dönem başı ticari alacakları 250 bin TL, dönem sonu ticari alacakları 350 bin TL olan işletmenin alacak devir hızı kaçtır?",
        "Alacak devir hızı 7 ve ortalama ticari alacakları 450 bin TL olan işletmenin kredili net satışları kaç bin TL'dir?",
        num(2400/((250+350)/2)), num(7*450, " bin TL"),
        [num(.13), num(4), num(6.86), num(9.6)],
        [num(64, " bin TL"), num(2250, " bin TL"), num(2700, " bin TL"), num(3600, " bin TL")],
        "Ortalama alacak 300 bin TL'dir; alacak devir hızı = 2.400 / 300 = 8'dir.",
        "Kredili Net Satışlar = Alacak Devir Hızı × Ortalama Alacaklar = 7 × 450 = 3.150 bin TL'dir.",
        "Finansal tablo analizi - alacak devir hızı", "medium",
    ),
    c(
        "Alacak devir hızı 8 olan işletmede yıl 360 gün kabul edilirse ortalama tahsil süresi kaç gündür?",
        "Yıl 365 gün ve ortalama tahsil süresi 36,5 gün kabul edilen işletmenin alacak devir hızı kaçtır?",
        num(360/8, " gün"), num(365/36.5),
        [num(8, " gün"), num(28.8, " gün"), num(40, " gün"), num(64, " gün")],
        [num(.1), num(5), num(8), num(12)],
        "Ortalama tahsil süresi = 360 / Alacak Devir Hızı = 360 / 8 = 45 gündür.",
        "Alacak devir hızı = 365 / Ortalama Tahsil Süresi = 365 / 36,50 = 10'dur.",
        "Finansal tablo analizi - alacak tahsil süresi", "easy",
    ),
    c(
        "Satışların maliyeti 1.800 bin TL; dönem başı stoku 250 bin TL, dönem sonu stoku 350 bin TL olan işletmenin stok devir hızı kaçtır?",
        "Stok devir hızı 7 ve ortalama stoku 400 bin TL olan işletmenin satışların maliyeti kaç bin TL'dir?",
        num(1800/((250+350)/2)), num(7*400, " bin TL"),
        [num(.17), num(5.14), num(7.2), num(8)],
        [num(57, " bin TL"), num(1600, " bin TL"), num(2450, " bin TL"), num(3200, " bin TL")],
        "Ortalama stok 300 bin TL'dir; stok devir hızı = Satışların Maliyeti / Ortalama Stok = 1.800 / 300 = 6'dır.",
        "Satışların Maliyeti = Stok Devir Hızı × Ortalama Stok = 7 × 400 = 2.800 bin TL'dir.",
        "Finansal tablo analizi - stok devir hızı", "medium",
    ),
    c(
        "Stok devir hızı 6 olan işletmede yıl 360 gün kabul edilirse stokların ortalama bekleme süresi kaç gündür?",
        "Yıl 365 gün ve stokta ortalama bekleme süresi 73 gün olan işletmenin stok devir hızı kaçtır?",
        num(360/6, " gün"), num(365/73),
        [num(6, " gün"), num(50, " gün"), num(66, " gün"), num(90, " gün")],
        [num(.2), num(4), num(6), num(73)],
        "Stok bekleme süresi = 360 / Stok Devir Hızı = 360 / 6 = 60 gündür.",
        "Stok devir hızı = 365 / Stokta Bekleme Süresi = 365 / 73 = 5'tir.",
        "Finansal tablo analizi - stokta bekleme süresi", "easy",
    ),
    c(
        "Kredili alışları 1.800 bin TL; dönem başı ticari borçları 250 bin TL, dönem sonu ticari borçları 350 bin TL olan işletmenin borç devir hızı kaçtır?",
        "Ticari borç devir hızı 5 ve ortalama ticari borçları 440 bin TL olan işletmenin kredili alışları kaç bin TL'dir?",
        num(1800/((250+350)/2)), num(5*440, " bin TL"),
        [num(.17), num(5.14), num(7.2), num(8)],
        [num(88, " bin TL"), num(1760, " bin TL"), num(2440, " bin TL"), num(2640, " bin TL")],
        "Ortalama ticari borç 300 bin TL'dir; borç devir hızı = Kredili Alışlar / Ortalama Ticari Borçlar = 6'dır.",
        "Kredili Alışlar = Borç Devir Hızı × Ortalama Ticari Borçlar = 5 × 440 = 2.200 bin TL'dir.",
        "Finansal tablo analizi - ticari borç devir hızı", "medium",
    ),
    c(
        "Yıl 360 gün kabul edildiğinde ticari borçlarını yılda 6 kez yenileyen işletme tedarikçilerine ortalama kaç günde ödeme yapmaktadır?",
        "Tedarikçilere ortalama 73 günde ödeme yapan işletmede yıl 365 günse ticari borçlar yıl içinde kaç kez devretmiştir?",
        num(360/6, " gün"), num(365/73),
        [num(6, " gün"), num(50, " gün"), num(66, " gün"), num(90, " gün")],
        [num(.2), num(4), num(6), num(73)],
        "Ortalama ödeme süresi = 360 / Borç Devir Hızı = 360 / 6 = 60 gündür.",
        "Ticari borç devir hızı = 365 / Ortalama Ödeme Süresi = 365 / 73 = 5'tir.",
        "Finansal tablo analizi - ticari borç ödeme süresi", "easy",
    ),
    c(
        "Stokta bekleme süresi 60 gün, alacak tahsil süresi 45 gün olan işletmenin faaliyet döngüsü kaç gündür?",
        "Faaliyet döngüsü 109,5 gün, alacak tahsil süresi 36,5 gün olan işletmenin stokta bekleme süresi kaç gündür?",
        num(60+45, " gün"), num(109.5-36.5, " gün"),
        [num(15, " gün"), num(45, " gün"), num(60, " gün"), num(270, " gün")],
        [num(36.5, " gün"), num(70, " gün"), num(100, " gün"), num(266.5, " gün")],
        "Faaliyet döngüsü = Stokta Bekleme Süresi + Alacak Tahsil Süresi = 60 + 45 = 105 gündür.",
        "Stokta Bekleme Süresi = Faaliyet Döngüsü − Tahsil Süresi = 109,50 − 36,50 = 73 gündür.",
        "Finansal tablo analizi - faaliyet döngüsü", "medium",
    ),
    c(
        "Faaliyet döngüsü 105 gün, ticari borç ödeme süresi 60 gün olan işletmenin nakit dönüşüm süresi kaç gündür?",
        "Nakit dönüşüm süresi 36,5 gün, ticari borç ödeme süresi 73 gün olan işletmenin faaliyet döngüsü kaç gündür?",
        num(105-60, " gün"), num(36.5+73, " gün"),
        [num(60, " gün"), num(105, " gün"), num(165, " gün"), num(270, " gün")],
        [num(36.5, " gün"), num(73, " gün"), num(146, " gün"), num(182.5, " gün")],
        "Nakit dönüşüm süresi = Faaliyet Döngüsü − Ticari Borç Ödeme Süresi = 105 − 60 = 45 gündür.",
        "Faaliyet Döngüsü = Nakit Dönüşüm Süresi + Borç Ödeme Süresi = 36,50 + 73 = 109,50 gündür.",
        "Finansal tablo analizi - nakit dönüşüm süresi", "medium",
    ),
    c(
        "Net kâr marjı %8, aktif devir hızı 1,5 olan işletmenin DuPont yaklaşımına göre aktif kârlılığı kaçtır?",
        "DuPont yaklaşımına göre aktif kârlılığı %18 ve net kâr marjı %10 olan işletmenin aktif devir hızı kaçtır?",
        num(.08*1.5*100, "%"), num(.18/.10),
        [num(5.33, "%"), num(8, "%"), num(9.5, "%"), num(20, "%")],
        [num(.56), num(1.2), num(2.8), num(8)],
        "DuPont yaklaşımında aktif kârlılığı = Net Kâr Marjı × Aktif Devir Hızı = %8 × 1,5 = %12'dir.",
        "Aktif Devir Hızı = Aktif Kârlılığı / Net Kâr Marjı = %18 / %10 = 1,80'dir.",
        "Finansal tablo analizi - DuPont eşitliği", "hard",
    ),
    r(
        "Cari oranı 2 olan işletme, kısa vadeli borcunun bir bölümünü nakitle ödediğinde diğer koşullar değişmiyorsa cari oran nasıl etkilenir?",
        "Cari oranı 2 olan işletme, kısa vadeli borçlanmayla aynı tutarda stok aldığında diğer koşullar değişmiyorsa cari oran nasıl etkilenir?",
        "Cari oran yükselir; pay ve payda aynı tutarda azalır",
        "Cari oran düşer; pay ve payda aynı tutarda artar",
        ["Cari oran değişmez; işlem yalnız duran varlığı etkiler", "Cari oran düşer; yalnız dönen varlıklar azalır", "Cari oran sıfırlanır; bütün borçlar uzun vadeli olur", "Cari oran yükselir; payda artarken pay değişmez"],
        ["Cari oran yükselir; yalnız dönen varlıklar artar", "Cari oran değişmez; eşit tutarlı artış oranı korur", "Cari oran sıfırlanır; stok likit kabul edilmez", "Cari oran düşer; pay azalırken payda değişmez"],
        "Oran 1'in üzerindeyken pay ve paydadan eşit tutar çıkarmak oranı yükseltir. Örneğin 200/100 oranında 50 TL ödeme sonrası 150/50 = 3 olur.",
        "Oran 1'in üzerindeyken pay ve paydaya eşit tutar eklemek oranı 1'e yaklaştırarak düşürür. Örneğin 200/100, 50 TL borçlu stok alışından sonra 250/150 olur.",
        "Finansal tablo analizi - oranların işlem etkisi", "hard",
    ),
]


PREMISES = [
    {
        "stem": "Likidite oranları bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Cari oran dönen varlıkları kısa vadeli borçlarla ilişkilendirir\n\nII. Asit-test oranında stoklar dışlanır\n\nIII. Nakit oranı en dar kapsamlı likidite ölçüsüdür",
        "correct": "I, II ve III",
        "why": "Cari oran bütün dönen varlıkları, asit-test stok dışındaki dönen varlıkları, nakit oranı ise en likit kalemleri kısa vadeli borçlarla karşılaştırır.",
        "ref": "Finansal tablo analizi - likidite oranları", "difficulty": "easy",
    },
    {
        "stem": "Faaliyet oranları bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Alacak devir hızı satışlarla ortalama alacağı ilişkilendirir\n\nII. Stok devir hızı satışların maliyetini ortalama stokla ilişkilendirir\n\nIII. Devir hızının yükselmesi ilgili sürenin kural olarak kısalması demektir",
        "correct": "I, II ve III",
        "why": "Alacak ve stok devir hızları ilgili ortalama bilanço kalemlerine göre hesaplanır; gün sayısı devir hızına bölündüğü için hız arttıkça süre kısalır.",
        "ref": "Finansal tablo analizi - faaliyet oranları", "difficulty": "medium",
    },
    {
        "stem": "Mali yapı oranları bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Finansal kaldıraç yabancı kaynakların toplam kaynaklara payını gösterir\n\nII. Borç/özkaynak oranı finansman bileşimini gösterir\n\nIII. Özkaynak oranı bir faaliyet devir hızıdır",
        "correct": "I ve II",
        "why": "Kaldıraç ile borç/özkaynak oranları mali yapıyı ölçer. Özkaynak oranı da mali yapı oranıdır; faaliyet devir hızı olmadığından III yanlıştır.",
        "ref": "Finansal tablo analizi - mali yapı oranları", "difficulty": "easy",
    },
    {
        "stem": "Kârlılık oranları bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Net kâr marjının paydası net satışlardır\n\nII. Aktif kârlılığının paydası özkaynaklardır\n\nIII. Özkaynak kârlılığının paydası ortalama özkaynak olabilir",
        "correct": "I ve III",
        "why": "Net kâr marjı satışlara, özkaynak kârlılığı ortalama özkaynaklara göre hesaplanır. Aktif kârlılığında payda toplam varlık olduğundan II yanlıştır.",
        "ref": "Finansal tablo analizi - kârlılık oranları", "difficulty": "medium",
    },
    {
        "stem": "Faaliyet döngüsü bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Stokta bekleme süresi ile tahsil süresi toplanır\n\nII. Ticari borç ödeme süresi faaliyet döngüsüne eklenir\n\nIII. Nakit dönüşümünde ödeme süresi faaliyet döngüsünden çıkarılır",
        "correct": "I ve III",
        "why": "Faaliyet döngüsü stok ve tahsil sürelerinin toplamıdır. Nakit dönüşüm süresinde borç ödeme süresi bu toplamdan çıkarıldığından II yanlıştır.",
        "ref": "Finansal tablo analizi - faaliyet ve nakit dönüşüm döngüsü", "difficulty": "medium",
    },
    {
        "stem": "Oran analizinin kullanımı bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Tek bir oran her işletme için tek başına kesin hüküm verir\n\nII. Sektör ve dönem karşılaştırması yorumu güçlendirir\n\nIII. Muhasebe politikası farklılıkları karşılaştırmayı etkileyebilir",
        "correct": "II ve III",
        "why": "Oranlar sektör, dönem ve işletme koşullarıyla birlikte yorumlanır. Muhasebe politikaları karşılaştırılabilirliği etkileyebilir; tek oran kesin hüküm vermediği için I yanlıştır.",
        "ref": "Finansal tablo analizi - yorumlama sınırlılıkları", "difficulty": "medium",
    },
    {
        "stem": "DuPont analizi bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Aktif kârlılığı net kâr marjı ile aktif devir hızının çarpımıdır\n\nII. Yalnız likidite oranlarını açıklar\n\nIII. Kârlılık ile varlık kullanım etkinliğini birlikte gösterir",
        "correct": "I ve III",
        "why": "DuPont eşitliği aktif kârlılığını marj ve devir hızı bileşenlerine ayırır. Likidite oranlarıyla sınırlı olmadığından II yanlıştır.",
        "ref": "Finansal tablo analizi - DuPont analizi", "difficulty": "hard",
    },
    {
        "stem": "Oranlarda ortalama değer kullanımı bakımından aşağıdaki ifadelerden hangileri doğrudur?\n\nI. Dönem akışı olan satışlar ortalama bilanço kalemiyle ilişkilendirilebilir\n\nII. Ortalama alacak dönem başı ve dönem sonu tutarlarından hesaplanabilir\n\nIII. Yalnız dönem sonu kullanımı mevsimselliğin etkisini her durumda yok eder",
        "correct": "I ve II",
        "why": "Dönem boyunca oluşan satış veya maliyet akışını ortalama bilanço kalemiyle eşleştirmek daha tutarlı olabilir. Dönem sonu tutarı mevsimselliği her durumda gidermez; III yanlıştır.",
        "ref": "Finansal tablo analizi - ortalama bilanço kalemleri", "difficulty": "hard",
    },
]


if __name__ == "__main__":
    write_topic(
        lesson_id="mali_tablolar_analizi",
        topic_id="oran_analizi",
        label="Oran Analizi",
        slug="oran_analizi",
        prefix="topic-ora",
        seed=2026071741,
        legislation_version=(
            "SMMM Finansal Tablolar ve Analizi müfredatı; finansal tablo analizi "
            "likidite, mali yapı, faaliyet ve kârlılık oranları (17.07.2026 kontrolü)"
        ),
        rules=RULES,
        premises=PREMISES,
        wrong_banks={},
    )
