#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gramer (Grammar) — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gerçek SGS 21-27 profiline göre baştan yazıldı: akademik/iş bağlamlı cümle içinde '----' boşluk; zaman-kip-edilgen, ilgi zamiri, koşul, bağlaç, 11 çift boşluk (edat/bağlaç çifti), fiilimsi, karşılaştırma. Eski paketteki tanım/çeviri tipi kısa sorular kaldırıldı.

IKI KAPI: §5 boy (beraberlik + oncul secicileri DAHIL) · §1 bilissel duzey
(60'lik pakette duzey 0 <=6, duzey 0+1 <=24, duzey 2 >=24, duzey 3 >=12).

Dayanak: SGS Yabancı Dil (İngilizce) 2021-2026 kitapçıkları — yalnız biçim kalibrasyonu, cümleler özgün
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = ROOT.parent / "smmm_sgs_pratik" / "assets"
RELATIVE_PATH = "content/yabanci_dil/grammar.json"
STYLE_REF = 'SGS Yabancı Dil (gerçek sınav 21-27 cümle içi boşluk profili)'
ONEK = "eng-grammar-gen-"


def patch(stem, options, answer, solution, ref='SGS İngilizce dil bilgisi'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        'The new factory will ---- create jobs ---- increase tax revenue for the local government.',
        {
            'A': 'both / or',
            'B': 'not only / but also',
            'C': 'rather / and',
            'D': 'either / but',
            'E': 'neither / or',
        },
        'B',
        "İki olumlu sonucu ekleyen kalıp 'not only ... but also'dur; diğer çiftlerin eşleri yanlıştır.",
    ),
    # düzey 2
    '0002': patch(
        'Thanks to the new software, the team ---- finish the annual report two weeks earlier than planned last year.',
        {
            'A': 'was able to',
            'B': 'can',
            'C': 'has been able to',
            'D': 'will be able to',
            'E': 'is able to',
        },
        'A',
        "'Last year' geçmişte belirli bir durumda başarılan işi gösterir; 'was able to' kullanılır. 'Has been able to' belirli geçmiş zaman ifadesiyle uyuşmaz.",
    ),
    # düzey 2
    '0003': patch(
        'The first credit cards ---- in the United States roughly seventy years ago, mainly for use in restaurants.',
        {
            'A': 'have appeared',
            'B': 'appeared',
            'C': 'had appeared',
            'D': 'are appearing',
            'E': 'will appear',
        },
        'B',
        "'Seventy years ago' bitmiş bir geçmiş zamanı belirtir; Simple Past gerekir: 'appeared'. 'Ago' Present Perfect ile kullanılmaz.",
    ),
    # düzey 3
    '0004': patch(
        'The report focuses ---- the effects of high inflation ---- the purchasing power of retired people.',
        {
            'A': 'to / from',
            'B': 'with / for',
            'C': 'on / on',
            'D': 'in / at',
            'E': 'at / of',
        },
        'C',
        "'Focus on' ve 'the effect(s) on' kalıpları gerekir: 'focuses on ... effects ... on'.",
    ),
    # düzey 3
    '0005': patch(
        'The company had its accounts ---- by an external firm to make sure that there were no serious errors.',
        {
            'A': 'checking',
            'B': 'be checked',
            'C': 'checked',
            'D': 'to check',
            'E': 'check',
        },
        'C',
        "Ettirgen yapı 'have something + V3' biçimindedir (bir işi başkasına yaptırmak): 'had its accounts checked'.",
    ),
    # düzey 2
    '0006': patch(
        'The company ---- its first overseas branch in 2009, two years after its shares were listed on the stock exchange.',
        {
            'A': 'opens',
            'B': 'had been opening',
            'C': 'has opened',
            'D': 'will have opened',
            'E': 'opened',
        },
        'E',
        "Cümlede belirli bir geçmiş zaman ifadesi ('in 2009') var; bitmiş geçmiş olay Simple Past ile anlatılır: 'opened'. Present Perfect belirli geçmiş tarihle kullanılmaz.",
    ),
    # düzey 2
    '0007': patch(
        "The new product was very expensive to develop; ----, it became the company's best-selling item within a year.",
        {
            'A': 'however',
            'B': 'similarly',
            'C': 'for example',
            'D': 'therefore',
            'E': 'otherwise',
        },
        'A',
        "Pahalıya mal olması ile en çok satan ürün olması arasında karşıtlık var; 'however' gerekir. 'Therefore' neden-sonuç kurar ve mantık bozulur.",
    ),
    # düzey 2
    '0008': patch(
        'If you want to avoid late-payment penalties, you ---- your tax return well before the official deadline.',
        {
            'A': 'would have submitted',
            'B': 'submitted',
            'C': 'must have submitted',
            'D': 'should submit',
            'E': 'had submitted',
        },
        'D',
        "Öneri/tavsiye 'should + yalın fiil' ile verilir: 'should submit'. 'Must have submitted' geçmişe dair çıkarımdır, tavsiye değildir.",
    ),
    # düzey 2
    '0009': patch(
        'After ---- the contract carefully, the lawyer advised her client not to sign it.',
        {
            'A': 'to read',
            'B': 'read',
            'C': 'reads',
            'D': 'been read',
            'E': 'reading',
        },
        'E',
        "Edattan ('after') sonra fiil '-ing' biçimini alır: 'after reading'.",
    ),
    # düzey 2
    '0010': patch(
        'Online shopping has become much ---- than it was ten years ago, especially among older people.',
        {
            'A': 'the more common',
            'B': 'as common',
            'C': 'most common',
            'D': 'more common',
            'E': 'common',
        },
        'D',
        "'Than' karşılaştırma yapısı ister; 'much' ile güçlendirilen karşılaştırma sıfatı 'more common' gerekir.",
    ),
    # düzey 3
    '0011': patch(
        '---- the heavy snow, most employees managed to arrive at work on time this morning.',
        {
            'A': 'However',
            'B': 'Although',
            'C': 'Because of',
            'D': 'Unless',
            'E': 'Despite',
        },
        'E',
        "Boşluktan sonra cümle değil isim öbeği ('the heavy snow') gelir ve anlam karşıtlıktır; 'despite' gerekir. 'Although' cümle ister, 'because of' anlamı ters çevirir.",
    ),
    # düzey 2
    '0012': patch(
        'The first modern stock exchange ---- in Amsterdam at the beginning of the seventeenth century.',
        {
            'A': 'had established',
            'B': 'has established',
            'C': 'was established',
            'D': 'established',
            'E': 'is establishing',
        },
        'C',
        "Borsa kendisi kurmaz, kurulur; geçmişte bitmiş olay için Simple Past edilgen gerekir: 'was established'.",
    ),
    # düzey 2
    '0013': patch(
        'The new tax regulation, ---- was announced in March, mainly affects self-employed people.',
        {
            'A': 'which',
            'B': 'who',
            'C': 'that',
            'D': 'where',
            'E': 'whose',
        },
        'A',
        "Virgüllerle ayrılan (tanımlamayan) ilgi cümlesinde nesneler için 'which' kullanılır; 'that' bu yapıda kullanılmaz.",
    ),
    # düzey 2
    '0014': patch(
        'The economy ---- steadily for the past three years, and most experts expect this trend to continue.',
        {
            'A': 'will grow',
            'B': 'has been growing',
            'C': 'had grown',
            'D': 'was growing',
            'E': 'grew',
        },
        'B',
        "'For the past three years' geçmişte başlayıp hâlâ süren eylemi gösterir ve cümlenin devamı eğilimin sürdüğünü söyler; Present Perfect Continuous gerekir: 'has been growing'.",
    ),
    # düzey 2
    '0015': patch(
        'Before calculators became cheap and widely available, accountants ---- long columns of figures by hand.',
        {
            'A': 'are adding up',
            'B': 'will add up',
            'C': 'have added up',
            'D': 'used to add up',
            'E': 'are used to adding up',
        },
        'D',
        "Geçmişte düzenli yapılan ama artık yapılmayan alışkanlık 'used to + yalın fiil' ile anlatılır: 'used to add up'. 'Be used to + -ing' (bir şeye alışkın olmak) şimdiki zamandadır ve anlamı farklıdır.",
    ),
    # düzey 2
    '0016': patch(
        'If I ---- enough savings, I would start my own accounting office instead of working for a large firm.',
        {
            'A': 'have',
            'B': 'will have',
            'C': 'would have',
            'D': 'had',
            'E': 'have had',
        },
        'D',
        "Ana cümledeki 'would start' şu anki gerçek dışı durumu (ikinci tip) gösterir; koşul cümlesinde Simple Past gerekir: 'had'.",
    ),
    # düzey 2
    '0017': patch(
        'These days, more and more consumers ---- online banking services instead of visiting a branch in person.',
        {
            'A': 'used',
            'B': 'had used',
            'C': 'are using',
            'D': 'were used',
            'E': 'will have used',
        },
        'C',
        "'These days' şu sıralar süren ve gelişen bir eğilimi anlatır; Present Continuous uygundur: 'are using'. 'Were used' edilgendir ve özne tüketicilerdir.",
    ),
    # düzey 2
    '0018': patch(
        'Some economists support lower taxes to encourage investment, ---- others argue that public services would suffer.',
        {
            'A': 'unless',
            'B': 'as long as',
            'C': 'so that',
            'D': 'whereas',
            'E': 'because',
        },
        'D',
        "İki grubun görüşü karşılaştırılıyor; karşılaştırma/karşıtlık bağlacı 'whereas' gerekir.",
    ),
    # düzey 3
    '0019': patch(
        'Small businesses are responsible ---- keeping their own records and paying their taxes ---- time.',
        {
            'A': 'for / on',
            'B': 'at / of',
            'C': 'to / by',
            'D': 'of / in',
            'E': 'with / at',
        },
        'A',
        "'Be responsible for' kalıbı ve 'zamanında' anlamındaki 'on time' birlikte gerekir.",
    ),
    # düzey 2
    '0020': patch(
        'Accountants ---- work for international firms often need to follow more than one set of reporting standards.',
        {
            'A': 'who',
            'B': 'which',
            'C': 'whose',
            'D': 'where',
            'E': 'when',
        },
        'A',
        "İlgi cümlesinin öznesi kişidir ('accountants') ve boşluktan sonra doğrudan fiil gelir; 'who' gerekir.",
    ),
    # düzey 2
    '0021': patch(
        'Your application will not be processed ---- you attach a certified copy of your diploma.',
        {
            'A': 'because',
            'B': 'unless',
            'C': 'although',
            'D': 'if',
            'E': 'so that',
        },
        'B',
        "Anlam 'diploma eklemedikçe başvuru işleme alınmaz'dır; 'unless' (-medikçe) gerekir. 'If' cümleye ters anlam verir.",
    ),
    # düzey 3
    '0022': patch(
        'The training programme helps ---- newly hired graduates ---- experienced staff to understand the latest standards.',
        {
            'A': 'either / nor',
            'B': 'neither / or',
            'C': 'both / and',
            'D': 'not only / and',
            'E': 'so / that',
        },
        'C',
        "İki grubu birlikte kapsayan bağlaç çifti 'both ... and'dir. 'Either' 'or' ile, 'neither' 'nor' ile, 'not only' 'but also' ile kullanılır.",
    ),
    # düzey 3
    '0023': patch(
        'The instructions were ---- complicated ---- most users needed help to install the program.',
        {
            'A': 'such / as',
            'B': 'too / to',
            'C': 'so / that',
            'D': 'enough / for',
            'E': 'as / as',
        },
        'C',
        "Sıfattan önce 'so', sonuç cümlesinden önce 'that' gelir: 'so complicated that'. 'Too ... to' ardından mastar ister.",
    ),
    # düzey 3
    '0024': patch(
        'Many investors are interested ---- renewable energy projects because they are less dependent ---- oil prices.',
        {
            'A': 'in / on',
            'B': 'on / of',
            'C': 'at / from',
            'D': 'with / in',
            'E': 'for / to',
        },
        'A',
        "'Be interested in' ve 'be dependent on' kalıpları gerekir.",
    ),
    # düzey 3
    '0025': patch(
        'We ---- so much food for the meeting; in the end, only half of the invited guests came.',
        {
            'A': "don't have to order",
            'B': "mustn't order",
            'C': "needn't have ordered",
            'D': "can't order",
            'E': "won't order",
        },
        'C',
        "Geçmişte yapılan ama gereksiz olduğu sonradan anlaşılan eylem 'needn't have + V3' ile anlatılır: 'needn't have ordered'.",
    ),
    # düzey 3
    '0026': patch(
        'Experts predict that by 2035 most banks ---- paper statements with fully digital records.',
        {
            'A': 'replaced',
            'B': 'have replaced',
            'C': 'had replaced',
            'D': 'will have replaced',
            'E': 'were replacing',
        },
        'D',
        "'By 2035' gelecekteki bir noktaya kadar tamamlanmış olacak eylemi anlatır; Future Perfect gerekir: 'will have replaced'.",
    ),
    # düzey 2
    '0027': patch(
        'The town ---- the first cooperative bank in the region was founded now hosts a small museum about its history.',
        {
            'A': 'whose',
            'B': 'who',
            'C': 'what',
            'D': 'which',
            'E': 'where',
        },
        'E',
        "Boşluktan sonra öznesi ve fiili tam bir cümle gelir ('the bank was founded'); yer bildiren 'the town' için 'where' kullanılır.",
    ),
    # düzey 3
    '0028': patch(
        'The museum is open ---- 9 a.m. ---- 5 p.m. on weekdays, but it closes earlier on Sundays.',
        {
            'A': 'since / for',
            'B': 'at / on',
            'C': 'from / to',
            'D': 'in / at',
            'E': 'by / until',
        },
        'C',
        "Başlangıç ve bitiş saatleri 'from ... to' ile verilir.",
    ),
    # düzey 2
    '0029': patch(
        'Because the computer system was down, the employees ---- all the customer orders manually yesterday.',
        {
            'A': 'have to enter',
            'B': 'had to enter',
            'C': 'will enter',
            'D': 'can enter',
            'E': 'are entering',
        },
        'B',
        "'Yesterday' geçmişi, 'because the system was down' zorunluluğu gösterir; geçmişteki zorunluluk 'had to' ile anlatılır.",
    ),
    # düzey 2
    '0030': patch(
        'The new accounting software is not ---- the old one, so many users still prefer to work with the previous version.',
        {
            'A': 'more reliable as',
            'B': 'so reliable than',
            'C': 'as reliable as',
            'D': 'reliable as',
            'E': 'the most reliable as',
        },
        'C',
        "Eşitlik karşılaştırması 'as + sıfat + as' ile kurulur; olumsuzunda 'not as ... as' kullanılır.",
    ),
    # düzey 2
    '0031': patch(
        'Many experienced managers avoid ---- important decisions late on Friday afternoons.',
        {
            'A': 'make',
            'B': 'to make',
            'C': 'making',
            'D': 'made',
            'E': 'to have made',
        },
        'C',
        "'Avoid' fiilinden sonra '-ing' biçimi gelir: 'avoid making'.",
    ),
    # düzey 2
    '0032': patch(
        'The flight to Ankara was delayed for three hours ---- a technical problem with one of the engines.',
        {
            'A': 'in spite of',
            'B': 'so that',
            'C': 'instead of',
            'D': 'in addition to',
            'E': 'due to',
        },
        'E',
        "Gecikmenin nedeni bir isim öbeğiyle verilir; neden bildiren edat 'due to' gerekir.",
    ),
    # düzey 2
    '0033': patch(
        'If the central bank raises interest rates again, borrowing ---- more expensive for most households.',
        {
            'A': 'has become',
            'B': 'had become',
            'C': 'would have become',
            'D': 'will become',
            'E': 'became',
        },
        'D',
        "Gerçekleşmesi olası koşul (birinci tip): 'If + Simple Present, will + yalın fiil' → 'will become'.",
    ),
    # düzey 2
    '0034': patch(
        'There is ---- information in the report to make a reliable decision, so the committee has asked for more data.',
        {
            'A': 'plenty of',
            'B': 'a lot of',
            'C': 'too much',
            'D': 'a great deal of',
            'E': 'not enough',
        },
        'E',
        "Cümlenin devamı daha fazla veri istendiğini söyler; bilgi yetersizdir: 'not enough'. Diğer seçenekler bilginin bol olduğunu anlatır ve sonuçla çelişir.",
    ),
    # düzey 2
    '0035': patch(
        "According to the latest figures, this year's budget deficit is ---- of the last decade.",
        {
            'A': 'as large',
            'B': 'the largest',
            'C': 'the larger',
            'D': 'larger',
            'E': 'large',
        },
        'B',
        "'Of the last decade' bir grup içinde en üst dereceyi gösterir; üstünlük sıfatı 'the largest' gerekir.",
    ),
    # düzey 3
    '0036': patch(
        'By the time the auditors arrived at the factory, the finance team ---- all the invoices for the previous year.',
        {
            'A': 'will already check',
            'B': 'has already checked',
            'C': 'had already checked',
            'D': 'already checks',
            'E': 'is already checking',
        },
        'C',
        "'By the time + Simple Past' yapısı, başka bir geçmiş olaydan önce tamamlanmış eylemi gösterir; Past Perfect gerekir: 'had already checked'.",
    ),
    # düzey 3
    '0037': patch(
        'Customers can pay ---- by credit card ---- by bank transfer, but cash is not accepted at this store.',
        {
            'A': 'neither / or',
            'B': 'as / than',
            'C': 'so / that',
            'D': 'either / or',
            'E': 'both / nor',
        },
        'D',
        "İki seçenekten birini anlatan çift 'either ... or'dur; 'neither' 'nor' ile, 'both' 'and' ile kullanılır.",
    ),
    # düzey 2
    '0038': patch(
        'All receipts must ---- for at least five years in case the tax office asks to see them during an inspection.',
        {
            'A': 'be kept',
            'B': 'have kept',
            'C': 'keep',
            'D': 'kept',
            'E': 'be keeping',
        },
        'A',
        "Özne 'receipts' saklanan şeydir; kipten sonra edilgen 'be + V3' gelir: 'must be kept'.",
    ),
    # düzey 3
    '0039': patch(
        'The auditor told us that the company ---- its inventory records the month before the inspection.',
        {
            'A': 'will update',
            'B': 'updates',
            'C': 'had updated',
            'D': 'is updating',
            'E': 'has updated',
        },
        'C',
        "Dolaylı anlatımda ('told us that') ve 'the month before' ifadesiyle, söylemeden önce tamamlanmış eylem Past Perfect'e kayar: 'had updated'.",
    ),
    # düzey 2
    '0040': patch(
        'While the manager ---- the quarterly results to the board, the power went out and the meeting had to stop.',
        {
            'A': 'has presented',
            'B': 'had been presented',
            'C': 'will present',
            'D': 'was presenting',
            'E': 'presents',
        },
        'D',
        "'While' ile verilen süregelen geçmiş eylemi başka bir geçmiş olay ('the power went out') böler; Past Continuous gerekir: 'was presenting'. Edilgen 'had been presented' özne olan 'the manager' ile uyuşmaz.",
    ),
    # düzey 3
    '0041': patch(
        'The method by ---- the shared costs are divided among departments should be clearly explained in the report.',
        {
            'A': 'whose',
            'B': 'where',
            'C': 'whom',
            'D': 'which',
            'E': 'that',
        },
        'D',
        "Edattan sonra ('by') nesneler için 'which' gelir; 'that' edattan sonra kullanılmaz, 'whom' kişiler içindir.",
    ),
    # düzey 2
    '0042': patch(
        'You may use the company car for personal trips ---- you pay for the fuel yourself.',
        {
            'A': 'unless',
            'B': 'so as to',
            'C': 'in order that',
            'D': 'instead of',
            'E': 'as long as',
        },
        'E',
        "Anlam 'yakıtı kendin ödediğin sürece'dir; şart bildiren 'as long as' gerekir. 'Unless' anlamı tersine çevirir.",
    ),
    # düzey 2
    '0043': patch(
        'The economist, ---- latest book explains inflation in simple language, will speak at the conference.',
        {
            'A': 'whom',
            'B': 'whose',
            'C': 'that',
            'D': 'who',
            'E': 'which',
        },
        'B',
        "Boşluktan sonraki isim ('latest book') ekonomiste aittir; iyelik bildiren ilgi zamiri 'whose' gerekir.",
    ),
    # düzey 3
    '0044': patch(
        'The more carefully you plan your monthly budget, ---- you are to face serious financial problems.',
        {
            'A': 'the less likely',
            'B': 'the least likely',
            'C': 'less likely',
            'D': 'more likely than',
            'E': 'as less likely',
        },
        'A',
        "'The more ..., the less ...' (ne kadar ... o kadar az) kalıbında ikinci yarı da 'the + karşılaştırma' ile kurulur: 'the less likely'.",
    ),
    # düzey 2
    '0045': patch(
        'Since the new tax law came into force, many small firms ---- their accounting software to meet the new reporting rules.',
        {
            'A': 'update',
            'B': 'will update',
            'C': 'were updating',
            'D': 'have updated',
            'E': 'had updated',
        },
        'D',
        "'Since + geçmişteki başlangıç' yapısı, geçmişte başlayıp etkisi bugüne uzanan eylemi anlatır; ana cümlede Present Perfect gerekir: 'have updated'. Geçmiş, gelecek ya da geniş zaman 'since' ile kurulan bu anlamı karşılamaz.",
    ),
    # düzey 2
    '0046': patch(
        'The results of the customer survey ---- next month, after all the data has been checked carefully.',
        {
            'A': 'are announcing',
            'B': 'will announce',
            'C': 'announced',
            'D': 'will be announced',
            'E': 'have been announced',
        },
        'D',
        "Sonuçlar duyurulan şeydir ve 'next month' geleceği gösterir; gelecek zaman edilgen gerekir: 'will be announced'.",
    ),
    # düzey 2
    '0047': patch(
        'The manager reorganised the office layout ---- employees could communicate with each other more easily.',
        {
            'A': 'as if',
            'B': 'so that',
            'C': 'whereas',
            'D': 'even though',
            'E': 'unless',
        },
        'B',
        "Boşluktan sonra amaç bildiren cümle var ('could communicate more easily'); amaç bağlacı 'so that' gerekir.",
    ),
    # düzey 3
    '0048': patch(
        'The new branch differs ---- the old one mainly ---- its size and the number of staff it employs.',
        {
            'A': 'from / in',
            'B': 'of / by',
            'C': 'to / at',
            'D': 'with / on',
            'E': 'than / for',
        },
        'A',
        "'Differ from' (bir şeyden farklı olmak) ve 'differ in' (bir bakımdan farklı olmak) kalıpları gerekir.",
    ),
    # düzey 2
    '0049': patch(
        'Every year, the financial statements of listed companies ---- by independent auditors before they are published.',
        {
            'A': 'have examined',
            'B': 'examine',
            'C': 'examined',
            'D': 'are examining',
            'E': 'are examined',
        },
        'E',
        "Tablolar denetimi yapan değil, denetlenen taraftır ve 'by independent auditors' eylemi yapanı gösterir; her yıl tekrarlanan iş için geniş zaman edilgen gerekir: 'are examined'.",
    ),
    # düzey 2
    '0050': patch(
        "---- the company's sales rose sharply last year, its profit fell because of much higher energy costs.",
        {
            'A': 'So that',
            'B': 'Although',
            'C': 'As soon as',
            'D': 'Unless',
            'E': 'Because',
        },
        'B',
        "İki cümle arasında karşıtlık var (satış arttı, kâr düştü); karşıtlık bağlacı 'although' gerekir.",
    ),
    # düzey 2
    '0051': patch(
        'The company is considering ---- a second office in another city in order to reach more customers.',
        {
            'A': 'opening',
            'B': 'to be opened',
            'C': 'opened',
            'D': 'open',
            'E': 'to open',
        },
        'A',
        "'Consider' fiilinden sonra '-ing' biçimi gelir: 'considering opening'.",
    ),
    # düzey 2
    '0052': patch(
        'The board decided ---- the launch of the new product until market conditions improve.',
        {
            'A': 'postponed',
            'B': 'to postpone',
            'C': 'postpone',
            'D': 'having postponed',
            'E': 'postponing',
        },
        'B',
        "'Decide' fiilinden sonra mastar ('to + yalın fiil') gelir: 'decided to postpone'.",
    ),
    # düzey 3
    '0053': patch(
        'Several new safety rules ---- since the accident, so all factory workers now receive regular training.',
        {
            'A': 'have introduced',
            'B': 'have been introduced',
            'C': 'were introducing',
            'D': 'had been introducing',
            'E': 'introduce',
        },
        'B',
        "Kurallar getirilen şeydir (edilgen) ve 'since the accident' etkisi bugüne süren eylemi gösterir; Present Perfect edilgen gerekir: 'have been introduced'.",
    ),
    # düzey 3
    '0054': patch(
        'The company would not have lost so much money last year if it ---- its foreign currency risk more carefully.',
        {
            'A': 'would manage',
            'B': 'managed',
            'C': 'has managed',
            'D': 'manages',
            'E': 'had managed',
        },
        'E',
        "Geçmişe ait gerçek dışı koşul (üçüncü tip): ana cümle 'would not have lost', koşul cümlesi Past Perfect: 'had managed'.",
    ),
    # düzey 3
    '0055': patch(
        'The office lights are still on at midnight; someone ---- to switch them off before leaving the building.',
        {
            'A': 'would forget',
            'B': 'must have forgotten',
            'C': 'should forget',
            'D': 'has to forget',
            'E': 'is forgetting',
        },
        'B',
        "Şimdiki bir kanıttan ('lights are still on') geçmişe dair güçlü çıkarım 'must have + V3' ile yapılır: 'must have forgotten'.",
    ),
    # düzey 3
    '0056': patch(
        '---- the manager ---- his assistant could explain the difference in the figures, so an expert was called in.',
        {
            'A': 'Neither / nor',
            'B': 'Whether / and',
            'C': 'Either / and',
            'D': 'Not only / nor',
            'E': 'Both / or',
        },
        'A',
        "Cümlenin devamı ('so an expert was called in') ikisinin de açıklayamadığını gösterir; olumsuz çift 'neither ... nor' gerekir.",
    ),
    # düzey 2
    '0057': patch(
        'Very ---- people attended the seminar because it had been announced only a day in advance.',
        {
            'A': 'little',
            'B': 'much',
            'C': 'many',
            'D': 'a lot',
            'E': 'few',
        },
        'E',
        "Sayılabilir 'people' için az anlamı 'few' ile verilir; neden cümlesi katılımın düşük olduğunu gösterir. 'Little/much' sayılamayan isimler içindir.",
    ),
    # düzey 3
    '0058': patch(
        'It was ---- successful campaign ---- the company decided to repeat it the following year.',
        {
            'A': 'such a / that',
            'B': 'too / to',
            'C': 'so / as',
            'D': 'such / as',
            'E': 'as a / so',
        },
        'A',
        "Sıfat + tekil isimden önce 'such a', sonuç cümlesinden önce 'that' gelir: 'such a successful campaign that'.",
    ),
    # düzey 2
    '0059': patch(
        'Many people in Türkiye still remember the day ---- the national currency lost six zeros in 2005.',
        {
            'A': 'what',
            'B': 'whose',
            'C': 'who',
            'D': 'where',
            'E': 'when',
        },
        'E',
        "Zaman bildiren 'the day' ve ardından gelen tam cümle için 'when' kullanılır.",
    ),
    # düzey 3
    '0060': patch(
        "Many students wish they ---- more time to prepare before last week's exam started.",
        {
            'A': 'will have',
            'B': 'are having',
            'C': 'have had',
            'D': 'have',
            'E': 'had had',
        },
        'E',
        "Geçmişe ilişkin pişmanlık 'wish + Past Perfect' ile anlatılır; 'have' fiilinin Past Perfect biçimi 'had had'dir.",
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
    print(f"1 paket / {len(PATCHES)} soru ('Gramer (Grammar)' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
