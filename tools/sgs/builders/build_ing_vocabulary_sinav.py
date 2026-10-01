#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kelime Bilgisi (Vocabulary) — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gerçek SGS 21-27 profiline göre baştan yazıldı: akademik/iş bağlamlı cümlede '----' boşluk, beş seçenek aynı sözcük türünden (fiil, sıfat, isim, zarf); eşdizim (take effect, purchasing power, terms and conditions) ve öbek fiiller. Eski paketteki 'The opposite of ... is' tipi tanım soruları (sınavda hiç yok) kaldırıldı. Dört çeldiricinin eş anlamlı olduğu (doğruyu 'farklı olan' yapan) küme kullanılmadı.

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
RELATIVE_PATH = "content/yabanci_dil/vocabulary.json"
STYLE_REF = 'SGS Yabancı Dil (gerçek sınav 21-27 cümle içi boşluk profili)'
ONEK = "eng-vocab-gen-"


def patch(stem, options, answer, solution, ref='SGS İngilizce sözcük bilgisi'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 2
    '0001': patch(
        'Many households ---- part of their monthly income to protect themselves against unexpected expenses.',
        {
            'A': 'forgive',
            'B': 'save',
            'C': 'breathe',
            'D': 'steal',
            'E': 'ignore',
        },
        'B',
        "Beklenmedik harcamalara karşı gelirin bir kısmı 'biriktirilir': 'save'.",
    ),
    # düzey 3
    '0002': patch(
        'Fossil fuels are not ----: once they have been used, they cannot be replaced by nature.',
        {
            'A': 'renewable',
            'B': 'flammable',
            'C': 'portable',
            'D': 'visible',
            'E': 'expensive',
        },
        'A',
        "Kullanıldıktan sonra yerine konamayan kaynaklar 'yenilenebilir' değildir: 'renewable'.",
    ),
    # düzey 2
    '0003': patch(
        'It is ---- to drive without a valid licence, and drivers who do so can be fined by the police.',
        {
            'A': 'compulsory',
            'B': 'illegal',
            'C': 'legal',
            'D': 'polite',
            'E': 'healthy',
        },
        'B',
        "Para cezası gerektiren davranış 'yasa dışı'dır: 'illegal'.",
    ),
    # düzey 2
    '0004': patch(
        'The bank charges a small ---- for every international money transfer made through its website.',
        {
            'A': 'prize',
            'B': 'grade',
            'C': 'fee',
            'D': 'wage',
            'E': 'rent',
        },
        'C',
        "Bir hizmet karşılığında alınan ücret 'fee'dir; 'wage' çalışana ödenen ücrettir.",
    ),
    # düzey 2
    '0005': patch(
        'The company responded ---- to the customer complaints and solved most of them within a single day.',
        {
            'A': 'rudely',
            'B': 'reluctantly',
            'C': 'quickly',
            'D': 'lazily',
            'E': 'slowly',
        },
        'C',
        "Şikâyetlerin bir günde çözülmesi 'hızlı' yanıt verildiğini gösterir: 'quickly'.",
    ),
    # düzey 2
    '0006': patch(
        "Before granting a loan, the bank carefully ---- the applicant's income and existing debts.",
        {
            'A': 'celebrates',
            'B': 'borrows',
            'C': 'decorates',
            'D': 'destroys',
            'E': 'evaluates',
        },
        'E',
        "Banka kredi vermeden önce başvuranın gelirini ve borçlarını 'değerlendirir': 'evaluates'. Diğer fiiller (süslemek, ödünç almak, kutlamak, yok etmek) bu bağlama uymaz.",
    ),
    # düzey 2
    '0007': patch(
        'Tourism in the region is highly ---- on good weather, so a rainy summer can seriously harm the sector.',
        {
            'A': 'dependent',
            'B': 'careful',
            'C': 'jealous',
            'D': 'independent',
            'E': 'proud',
        },
        'A',
        "Yağmurlu yazın sektöre zarar vermesi turizmin havaya 'bağlı' olduğunu gösterir: 'dependent on'.",
    ),
    # düzey 3
    '0008': patch(
        'The manager ---- the staff that the office would be closed during the national holiday.',
        {
            'A': 'said',
            'B': 'explained',
            'C': 'spoke',
            'D': 'informed',
            'E': 'talked',
        },
        'D',
        "'Birine bir şeyi bildirmek' doğrudan nesne alan 'inform someone that' ile kurulur. 'Say' ve 'explain' kişiyi doğrudan nesne almaz; 'speak/talk' 'that' cümlesi almaz.",
    ),
    # düzey 3
    '0009': patch(
        'During the economic crisis, many companies had to ---- staff in order to reduce their costs.',
        {
            'A': 'put on',
            'B': 'take off',
            'C': 'look after',
            'D': 'give up',
            'E': 'lay off',
        },
        'E',
        "Maliyet düşürmek için personelin 'işten çıkarılması' 'lay off' ile anlatılır.",
    ),
    # düzey 3
    '0010': patch(
        'Investors tend to ---- their money from risky markets when political uncertainty increases.',
        {
            'A': 'imitate',
            'B': 'applaud',
            'C': 'attract',
            'D': 'withdraw',
            'E': 'pronounce',
        },
        'D',
        "Belirsizlik artınca yatırımcılar parayı riskli piyasalardan 'çeker': 'withdraw money from'.",
    ),
    # düzey 2
    '0011': patch(
        'Rising energy prices have ---- many factories to cut their production in recent months.',
        {
            'A': 'invented',
            'B': 'admired',
            'C': 'described',
            'D': 'repaired',
            'E': 'forced',
        },
        'E',
        "Artan enerji fiyatları fabrikaları üretimi azaltmaya 'zorlamıştır': 'force someone to do something'.",
    ),
    # düzey 2
    '0012': patch(
        "This year's survey results were ---- to last year's, with only a few small differences.",
        {
            'A': 'unknown',
            'B': 'opposite',
            'C': 'similar',
            'D': 'different',
            'E': 'unrelated',
        },
        'C',
        "Yalnızca küçük farklar olması sonuçların 'benzer' olduğunu gösterir: 'similar to'.",
    ),
    # düzey 3
    '0013': patch(
        'The firm hired an energy consultant to give expert ---- on how to reduce its electricity bills.',
        {
            'A': 'advice',
            'B': 'advise',
            'C': 'evidence',
            'D': 'advices',
            'E': 'permission',
        },
        'A',
        "Tavsiye anlamındaki isim 'advice'tır ve sayılamaz; 'advices' kullanılmaz, 'advise' fiildir.",
    ),
    # düzey 3
    '0014': patch(
        'Customers expect ---- answers to their questions, not long explanations full of technical terms.',
        {
            'A': 'lengthy',
            'B': 'straightforward',
            'C': 'confusing',
            'D': 'vague',
            'E': 'complicated',
        },
        'B',
        "Uzun ve teknik açıklamaların karşıtı 'açık ve dolambaçsız' yanıttır: 'straightforward'.",
    ),
    # düzey 2
    '0015': patch(
        'Prices have increased ---- this year, so many families are spending less on non-essential goods.',
        {
            'A': 'happily',
            'B': 'loudly',
            'C': 'carelessly',
            'D': 'considerably',
            'E': 'politely',
        },
        'D',
        "Ailelerin harcamayı kısması fiyatların 'önemli ölçüde' arttığını gösterir: 'considerably'.",
    ),
    # düzey 2
    '0016': patch(
        'The auditor asked the accountant to ---- the difference between the bank statement and the cash book.',
        {
            'A': 'whisper',
            'B': 'decorate',
            'C': 'swallow',
            'D': 'explain',
            'E': 'imitate',
        },
        'D',
        "Denetçi, banka ekstresi ile kasa defteri arasındaki farkın 'açıklanmasını' ister: 'explain'.",
    ),
    # düzey 2
    '0017': patch(
        'The figures in the report must be ----, because even a small error can lead to a wrong decision.',
        {
            'A': 'approximate',
            'B': 'colourful',
            'C': 'accurate',
            'D': 'attractive',
            'E': 'fashionable',
        },
        'C',
        "Küçük bir hata bile yanlış karara yol açabileceği için rakamlar 'doğru/kesin' olmalıdır: 'accurate'.",
    ),
    # düzey 2
    '0018': patch(
        'Interest rates are ---- higher in countries with high inflation, because lenders want to protect the value of their money.',
        {
            'A': 'accidentally',
            'B': 'barely',
            'C': 'secretly',
            'D': 'usually',
            'E': 'rarely',
        },
        'D',
        "Neden cümlesi yüksek enflasyonlu ülkelerde faizin 'genellikle' yüksek olduğunu açıklar: 'usually'.",
    ),
    # düzey 3
    '0019': patch(
        'Before the meeting, please ---- the attached document so that you can share your opinion on it.',
        {
            'A': 'go through',
            'B': 'come across',
            'C': 'run out',
            'D': 'get along',
            'E': 'break down',
        },
        'A',
        "Toplantıdan önce belgenin 'gözden geçirilmesi' istenir: 'go through'.",
    ),
    # düzey 2
    '0020': patch(
        'Keeping accurate records is ---- for any business that wants to avoid problems with the tax office.',
        {
            'A': 'crucial',
            'B': 'optional',
            'C': 'harmful',
            'D': 'useless',
            'E': 'illegal',
        },
        'A',
        "Vergi dairesiyle sorun yaşamamak için doğru kayıt tutmak 'çok önemlidir': 'crucial'.",
    ),
    # düzey 2
    '0021': patch(
        'The ---- of the new airport is expected to create thousands of jobs in the region.',
        {
            'A': 'description',
            'B': 'construction',
            'C': 'decoration',
            'D': 'destruction',
            'E': 'prediction',
        },
        'B',
        "Binlerce iş yaratacak olan şey havalimanının 'inşası'dır: 'construction'.",
    ),
    # düzey 2
    '0022': patch(
        'Strict new rules have been introduced to ---- the personal data of online customers.',
        {
            'A': 'expose',
            'B': 'decorate',
            'C': 'protect',
            'D': 'pronounce',
            'E': 'abandon',
        },
        'C',
        "Sıkı kuralların amacı kişisel verileri 'korumaktır': 'protect'. 'Expose' (açığa çıkarmak) amaçla çelişir.",
    ),
    # düzey 2
    '0023': patch(
        'The new sales manager speaks English ----, so he has no difficulty working with foreign partners.',
        {
            'A': 'poorly',
            'B': 'rarely',
            'C': 'fluently',
            'D': 'badly',
            'E': 'nervously',
        },
        'C',
        "Yabancı ortaklarla zorluk çekmemesi İngilizceyi 'akıcı' konuştuğunu gösterir: 'fluently'.",
    ),
    # düzey 2
    '0024': patch(
        'There is a growing ---- for skilled accountants who can work with data analysis tools.',
        {
            'A': 'demand',
            'B': 'silence',
            'C': 'distance',
            'D': 'permission',
            'E': 'fashion',
        },
        'A',
        "Nitelikli muhasebecilere artan 'talep' 'demand for' ile anlatılır.",
    ),
    # düzey 3
    '0025': patch(
        'The contract can be ---- terminated if either party fails to meet its obligations.',
        {
            'A': 'accidentally',
            'B': 'politely',
            'C': 'legally',
            'D': 'physically',
            'E': 'musically',
        },
        'C',
        "Yükümlülüğün yerine getirilmemesi sözleşmenin 'hukuken' feshine yol açar: 'legally terminated'.",
    ),
    # düzey 2
    '0026': patch(
        'The museum offers ---- entry to students, so they do not have to pay anything to visit it.',
        {
            'A': 'heavy',
            'B': 'expensive',
            'C': 'late',
            'D': 'free',
            'E': 'narrow',
        },
        'D',
        "Öğrencilerin hiçbir şey ödememesi girişin 'ücretsiz' olduğunu gösterir: 'free entry'.",
    ),
    # düzey 3
    '0027': patch(
        'Although the risk was ----, the investors decided to put a large amount of money into the project.',
        {
            'A': 'calculated',
            'B': 'familiar',
            'C': 'acceptable',
            'D': 'negligible',
            'E': 'considerable',
        },
        'E',
        "'Although' karşıtlık kurar: risk büyük olduğu hâlde yatırım yapılmıştır; 'considerable' gerekir. Riskin küçük, bilinen ya da kabul edilebilir olduğunu anlatan seçenekler karşıtlık kurmaz.",
    ),
    # düzey 3
    '0028': patch(
        'The new flexible working policy had a positive ---- on employee motivation and productivity.',
        {
            'A': 'reason',
            'B': 'affect',
            'C': 'effect',
            'D': 'cause',
            'E': 'advice',
        },
        'C',
        "'Bir şey üzerinde etkisi olmak' 'have an effect on' ile kurulur; 'affect' fiildir ve isim yerinde kullanılmaz.",
    ),
    # düzey 2
    '0029': patch(
        'Bank statements are usually considered ---- evidence because they are prepared by an independent third party.',
        {
            'A': 'careless',
            'B': 'reliable',
            'C': 'hungry',
            'D': 'noisy',
            'E': 'temporary',
        },
        'B',
        "Bağımsız üçüncü kişi hazırladığı için banka ekstresi 'güvenilir' kanıttır: 'reliable'.",
    ),
    # düzey 2
    '0030': patch(
        'Online banking has become popular because of its ----: customers can make payments at any time from home.',
        {
            'A': 'danger',
            'B': 'expense',
            'C': 'convenience',
            'D': 'difficulty',
            'E': 'slowness',
        },
        'C',
        "İstenen zamanda evden ödeme yapabilmek 'kolaylık/rahatlık'tır: 'convenience'.",
    ),
    # düzey 2
    '0031': patch(
        'Sales fell ---- after the price increase, and the company had to lower its prices again.',
        {
            'A': 'brightly',
            'B': 'warmly',
            'C': 'sharply',
            'D': 'kindly',
            'E': 'softly',
        },
        'C',
        "Fiyatları yeniden düşürmek zorunda kalınması satışların 'keskin biçimde' düştüğünü gösterir: 'fell sharply'.",
    ),
    # düzey 3
    '0032': patch(
        'The project was only ---- completed, so the team had to work extra hours to finish the remaining tasks.',
        {
            'A': 'fully',
            'B': 'smoothly',
            'C': 'quickly',
            'D': 'successfully',
            'E': 'partially',
        },
        'E',
        "Kalan görevlerin bulunması projenin 'kısmen' tamamlandığını gösterir: 'partially'.",
    ),
    # düzey 3
    '0033': patch(
        'House prices have ---- sharply in recent years, making it difficult for young people to buy a home.',
        {
            'A': 'slept',
            'B': 'remained',
            'C': 'raised',
            'D': 'risen',
            'E': 'fallen',
        },
        'D',
        "Fiyatların artması gençlerin ev almasını zorlaştırır; nesne almayan 'rise' fiilinin üçüncü hâli 'risen' gerekir. 'Raise' nesne ister, 'fallen' sonuçla çelişir.",
    ),
    # düzey 2
    '0034': patch(
        "The company's ---- growth has made it one of the largest employers in the region within a few years.",
        {
            'A': 'former',
            'B': 'sleepy',
            'C': 'slight',
            'D': 'silent',
            'E': 'rapid',
        },
        'E',
        "Birkaç yılda bölgenin en büyük işverenlerinden biri olmak 'hızlı' büyümeyle açıklanır: 'rapid growth'.",
    ),
    # düzey 2
    '0035': patch(
        'Since the instructions on the form were ----, many applicants could not understand how to complete it.',
        {
            'A': 'helpful',
            'B': 'unclear',
            'C': 'accurate',
            'D': 'obvious',
            'E': 'simple',
        },
        'B',
        "Başvuranların formu anlayamamasının nedeni talimatların 'belirsiz' olmasıdır: 'unclear'. Diğerleri sonuçla çelişir.",
    ),
    # düzey 2
    '0036': patch(
        'The new software can ---- thousands of invoices in just a few minutes without any human help.',
        {
            'A': 'persuade',
            'B': 'digest',
            'C': 'process',
            'D': 'pronounce',
            'E': 'forgive',
        },
        'C',
        "Yazılım faturaları 'işler': 'process invoices'.",
    ),
    # düzey 3
    '0037': patch(
        'The new law will take ---- on 1 January, so companies have three months to prepare for it.',
        {
            'A': 'place',
            'B': 'turns',
            'C': 'care',
            'D': 'effect',
            'E': 'part',
        },
        'D',
        "Bir yasanın 'yürürlüğe girmesi' 'take effect' ile anlatılır; 'take place' olaylar için kullanılır.",
    ),
    # düzey 2
    '0038': patch(
        'After paying all its expenses and taxes, the company made a ---- of two million liras.',
        {
            'A': 'profit',
            'B': 'salary',
            'C': 'receipt',
            'D': 'discount',
            'E': 'budget',
        },
        'A',
        "Tüm giderler ve vergiler ödendikten sonra elde edilen tutar 'kâr'dır: 'make a profit'.",
    ),
    # düzey 3
    '0039': patch(
        'The two audit reports were prepared ----, so their conclusions do not depend on each other.',
        {
            'A': 'similarly',
            'B': 'carelessly',
            'C': 'independently',
            'D': 'accidentally',
            'E': 'jointly',
        },
        'C',
        "Sonuçların birbirine bağlı olmaması raporların 'bağımsız olarak' hazırlandığını gösterir: 'independently'.",
    ),
    # düzey 2
    '0040': patch(
        'Unemployment is a ---- problem that affects not only individuals but also the whole economy.',
        {
            'A': 'tiny',
            'B': 'private',
            'C': 'funny',
            'D': 'serious',
            'E': 'minor',
        },
        'D',
        "Tüm ekonomiyi etkileyen bir sorun 'ciddi'dir: 'serious'. 'Minor/tiny' cümlenin devamıyla çelişir.",
    ),
    # düzey 3
    '0041': patch(
        'High inflation reduces the purchasing ---- of people who live on a fixed income.',
        {
            'A': 'voice',
            'B': 'list',
            'C': 'speed',
            'D': 'power',
            'E': 'habit',
        },
        'D',
        "'Satın alma gücü' İngilizcede 'purchasing power' eşdizimiyle ifade edilir.",
    ),
    # düzey 2
    '0042': patch(
        'The population of large cities in Türkiye has grown ---- over the last fifty years.',
        {
            'A': 'politely',
            'B': 'silently',
            'C': 'honestly',
            'D': 'nervously',
            'E': 'steadily',
        },
        'E',
        "Uzun bir dönemdeki nüfus artışı 'istikrarlı biçimde' olarak nitelenir: 'steadily'.",
    ),
    # düzey 2
    '0043': patch(
        "The main ---- of the meeting was to discuss next year's budget and investment plans.",
        {
            'A': 'length',
            'B': 'purpose',
            'C': 'colour',
            'D': 'weather',
            'E': 'price',
        },
        'B',
        "Toplantının 'amacı' bütçeyi görüşmektir: 'purpose'.",
    ),
    # düzey 2
    '0044': patch(
        'Turkish is the ---- language of the Republic of Türkiye, as stated in the Constitution.',
        {
            'A': 'official',
            'B': 'honest',
            'C': 'annual',
            'D': 'accidental',
            'E': 'elderly',
        },
        'A',
        "Anayasada belirtilen dil devletin 'resmî' dilidir: 'official language'.",
    ),
    # düzey 2
    '0045': patch(
        'The company plans to ---- its operations into neighbouring countries over the next five years.',
        {
            'A': 'pronounce',
            'B': 'apologise',
            'C': 'hesitate',
            'D': 'expand',
            'E': 'translate',
        },
        'D',
        "Faaliyetleri komşu ülkelere 'genişletmek' anlamında 'expand ... into' kullanılır.",
    ),
    # düzey 3
    '0046': patch(
        'Thanks to strong export sales, the company ---- its annual profit target by 15 percent.',
        {
            'A': 'exploded',
            'B': 'exhausted',
            'C': 'excluded',
            'D': 'exceeded',
            'E': 'expelled',
        },
        'D',
        "Hedefin yüzde 15 'aşılması' 'exceed' ile anlatılır; seçenekler yazımca benzer ama anlamca uyumsuzdur.",
    ),
    # düzey 2
    '0047': patch(
        'Small businesses often ---- difficulties in obtaining loans because they cannot offer enough collateral.',
        {
            'A': 'deliver',
            'B': 'face',
            'C': 'measure',
            'D': 'solve',
            'E': 'admire',
        },
        'B',
        "Teminat gösteremedikleri için güçlükle 'karşılaşırlar': 'face difficulties'. 'Solve' neden cümlesiyle çelişir.",
    ),
    # düzey 2
    '0048': patch(
        'The committee will ---- the final decision until all members have had time to read the report.',
        {
            'A': 'postpone',
            'B': 'invite',
            'C': 'celebrate',
            'D': 'measure',
            'E': 'rescue',
        },
        'A',
        "'Until' ile birlikte kararın 'ertelenmesi' anlatılır: 'postpone'.",
    ),
    # düzey 2
    '0049': patch(
        'The new model is far more ---- than the old one: it uses 30 percent less fuel for the same distance.',
        {
            'A': 'ancient',
            'B': 'expensive',
            'C': 'fragile',
            'D': 'dangerous',
            'E': 'efficient',
        },
        'E',
        "Aynı mesafe için daha az yakıt harcamak 'verimli' olmaktır: 'efficient'.",
    ),
    # düzey 2
    '0050': patch(
        'Before signing the contract, both parties carefully read all of its terms and ----.',
        {
            'A': 'temperatures',
            'B': 'conditions',
            'C': 'invitations',
            'D': 'reactions',
            'E': 'decorations',
        },
        'B',
        "Sözleşme hükümleri 'terms and conditions' kalıbıyla anlatılır.",
    ),
    # düzey 2
    '0051': patch(
        'Please check the figures ---- before sending the report, because the board will rely on them.',
        {
            'A': 'carefully',
            'B': 'hardly',
            'C': 'loudly',
            'D': 'rarely',
            'E': 'carelessly',
        },
        'A',
        "Yönetim kurulu rakamlara güveneceği için 'dikkatle' kontrol edilmelidir: 'carefully'.",
    ),
    # düzey 2
    '0052': patch(
        'The government ---- a new campaign last month to reduce plastic waste in coastal areas.',
        {
            'A': 'folded',
            'B': 'launched',
            'C': 'frightened',
            'D': 'painted',
            'E': 'landed',
        },
        'B',
        "Bir kampanya 'başlatılır': 'launch a campaign'.",
    ),
    # düzey 2
    '0053': patch(
        'Exports to Europe increased last year, but this ---- was not enough to close the trade deficit.',
        {
            'A': 'fall',
            'B': 'rise',
            'C': 'loss',
            'D': 'shortage',
            'E': 'delay',
        },
        'B',
        "İhracattaki artışa 'this' ile gönderme yapılır; artış anlamındaki isim 'rise'dır.",
    ),
    # düzey 2
    '0054': patch(
        'The two companies ---- to merge after months of negotiations over the value of their shares.',
        {
            'A': 'apologised',
            'B': 'pretended',
            'C': 'wondered',
            'D': 'borrowed',
            'E': 'agreed',
        },
        'E',
        "Aylarca süren müzakereden sonra şirketler birleşmeyi 'kabul etmiştir': 'agree to do something'.",
    ),
    # düzey 3
    '0055': patch(
        'The summary was so ---- that the board members were able to read it in less than ten minutes.',
        {
            'A': 'complicated',
            'B': 'concise',
            'C': 'lengthy',
            'D': 'detailed',
            'E': 'comprehensive',
        },
        'B',
        "On dakikadan kısa sürede okunabilen özet 'kısa ve öz'dür: 'concise'. Diğer seçenekler uzun ya da ayrıntılı metni anlatır.",
    ),
    # düzey 3
    '0056': patch(
        'Under Turkish labour law, employees are entitled to a paid annual ---- of at least fourteen days.',
        {
            'A': 'leave',
            'B': 'debt',
            'C': 'loan',
            'D': 'tax',
            'E': 'fine',
        },
        'A',
        "Ücretli yıllık izin İngilizcede 'paid annual leave' olarak ifade edilir.",
    ),
    # düzey 2
    '0057': patch(
        'The new regulation ---- companies to publish their sustainability reports on their websites.',
        {
            'A': 'forgets',
            'B': 'imagines',
            'C': 'delivers',
            'D': 'suffers',
            'E': 'requires',
        },
        'E',
        "Yönetmelik şirketlerin raporlarını yayımlamasını 'zorunlu kılar': 'require someone to do something'.",
    ),
    # düzey 3
    '0058': patch(
        'The central bank intervened in the foreign exchange market in order to ---- the value of the currency.',
        {
            'A': 'stabilise',
            'B': 'memorise',
            'C': 'dramatise',
            'D': 'sympathise',
            'E': 'apologise',
        },
        'A',
        "Merkez bankasının piyasaya müdahalesinin amacı kur değerini 'istikrara kavuşturmak'tır: 'stabilise'.",
    ),
    # düzey 3
    '0059': patch(
        'To reduce costs, the firm ---- some of its customer services to a specialised company abroad.',
        {
            'A': 'overheard',
            'B': 'overslept',
            'C': 'outgrew',
            'D': 'underlined',
            'E': 'outsourced',
        },
        'E',
        "Bir hizmetin dışarıdaki bir şirkete gördürülmesi 'outsource' fiiliyle anlatılır.",
    ),
    # düzey 3
    '0060': patch(
        'The government is trying to ---- unemployment by supporting small and medium-sized businesses.',
        {
            'A': 'run into',
            'B': 'put up with',
            'C': 'take after',
            'D': 'look up',
            'E': 'bring down',
        },
        'E',
        "İşsizliği 'azaltmak' 'bring down' öbek fiiliyle anlatılır.",
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
    print(f"1 paket / {len(PATCHES)} soru ('Kelime Bilgisi (Vocabulary)' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
