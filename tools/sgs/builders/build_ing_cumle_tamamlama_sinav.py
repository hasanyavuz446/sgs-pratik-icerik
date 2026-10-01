#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Okuma ve Boşluk Doldurma (Reading & Cloze) — YAPISAL kalibrasyon (kalip kok -> kural uygulamasi).

Hukuk ailesi yapisal kalibrasyon turu. Paketin 60 sorusunun TAMAMI yeniden
yazildi. tools/sgs/yapisal_pipeline.py ile uretildi.

Gerçek SGS 28-30 cümle tamamlama profiline göre baştan yazıldı: yan cümle ya da temel cümle şıkları; anlam ilişkisi (neden, karşıtlık, amaç, sonuç), zaman uyumu, koşul tipleri, bağlayıcılar (however, therefore, nevertheless...), ilgi cümlesi ve 'the more ... the more' yapısı. Eski paketteki kısa okuma/çeviri soruları (sınavda yok) kaldırıldı. Doğru şıkkın boy sırası bilerek dağıtıldı (en kısa 10, en uzun 12).

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
RELATIVE_PATH = "content/yabanci_dil/reading_cloze.json"
STYLE_REF = 'SGS Yabancı Dil (gerçek sınav 28-30 cümle tamamlama profili)'
ONEK = "eng-reading-gen-"


def patch(stem, options, answer, solution, ref='SGS İngilizce cümle tamamlama'):
    return {
        "stem": stem, "options": options, "answer": answer, "solution": solution,
        "source": {"kind": "generated", "styleRef": STYLE_REF,
                   "legislationRef": ref},
        "validYear": 2026, "mockExamId": None,
    }


_PATCHES = {
    # düzey 3
    '0001': patch(
        '----, the new product became a great success.',
        {
            'A': 'So that customers could not afford it',
            'B': 'Although it was launched without much advertising',
            'C': 'Before it will be launched in other countries next month',
            'D': 'Unless it is advertised on television',
            'E': 'Because nobody wanted to buy it at such a high price',
        },
        'B',
        "Az reklamla piyasaya sürülmesine karşın başarılı olması karşıtlıktır; 'Although' uyar.",
    ),
    # düzey 3
    '0002': patch(
        'The bridge was closed to traffic for repairs, ----.',
        {
            'A': 'so drivers had to take a much longer route',
            'B': 'so drivers could cross it much more quickly than before',
            'C': 'unless drivers will pay a higher toll to use it',
            'D': 'although it urgently needed repairs to its supports',
            'E': 'because drivers had to take a longer route home',
        },
        'A',
        "Köprünün kapanmasının sonucu sürücülerin uzun yol kullanmasıdır. 'Because' aynı bilgiyi neden gibi sunar ve neden-sonuç ilişkisini ters çevirir.",
    ),
    # düzey 3
    '0003': patch(
        'Ever since online shopping became popular, ----.',
        {
            'A': 'people will prefer to visit physical stores',
            'B': 'many small shops in city centres have had to close',
            'C': 'the first website was created in the early 1990s',
            'D': 'customers were paying with cash only',
            'E': 'delivery companies hire more drivers next year',
        },
        'B',
        "'Ever since + geçmiş' yapısı, o andan bugüne süren durumu anlatır; ana cümle Present Perfect olmalıdır: 'have had to close'.",
    ),
    # düzey 2
    '0004': patch(
        "The company's profits fell sharply last year, ----.",
        {
            'A': 'which will be announced last week',
            'B': 'although demand for its products fell in all its markets',
            'C': 'mainly due to a large increase in raw material costs',
            'D': 'mainly because its costs decreased considerably during the year',
            'E': 'so it paid higher dividends than ever before',
        },
        'C',
        "Kârın düşmesinin nedeni hammadde maliyetlerindeki artıştır; 'due to + isim öbeği' uyar.",
    ),
    # düzey 3
    '0005': patch(
        'The museum was closed for renovation last month; ----.',
        {
            'A': 'in contrast, the renovation will start next year',
            'B': 'similarly, its entrance fee is quite low',
            'C': 'therefore, the school trip had to be postponed',
            'D': 'otherwise, the paintings will be moved to another city',
            'E': 'for example, it attracts thousands of visitors every year',
        },
        'C',
        "Müzenin kapalı olması gezinin ertelenmesinin nedenidir; sonuç bildiren 'therefore' ile kurulan seçenek anlamca uyar. Diğer bağlayıcılar (örnek, karşıtlık, benzerlik) ilişkiyi bozar.",
    ),
    # düzey 3
    '0006': patch(
        '----, the government decided to raise the minimum wage.',
        {
            'A': 'When the economy will grow faster than expected next year',
            'B': 'So that all prices in the country would fall immediately',
            'C': 'Unless workers demand higher salaries',
            'D': 'If inflation had been lower',
            'E': 'As the cost of living had risen sharply',
        },
        'E',
        "Asgari ücretin artırılmasının nedeni hayat pahalılığının artmasıdır; geçmişte önceki olayı veren 'As ... had risen' uyar.",
    ),
    # düzey 2
    '0007': patch(
        'If I had known about the traffic jam, ----.',
        {
            'A': 'I would have taken the metro instead',
            'B': 'I take the metro to work on most days',
            'C': 'I would take the metro to work every single day',
            'D': 'I will take the metro to work tomorrow morning',
            'E': 'I had taken the metro to work that morning',
        },
        'A',
        "Üçüncü tip koşul ('If + Past Perfect') ana cümlede 'would have + V3' ister: 'I would have taken the metro'.",
    ),
    # düzey 2
    '0008': patch(
        'Since the new manager took over the department, ----.',
        {
            'A': 'productivity increased by 25 percent in 2010',
            'B': 'productivity had been decreasing for many years before that',
            'C': 'productivity will increase next year',
            'D': 'productivity has increased by nearly 25 percent',
            'E': 'productivity was increasing steadily even before he came',
        },
        'D',
        "'Since + geçmiş' yan cümlesi ana cümlede Present Perfect ister: 'has increased'.",
    ),
    # düzey 2
    '0009': patch(
        'The factory was built near the river ----.',
        {
            'A': 'although it needed large amounts of water',
            'B': 'because the river had dried up completely',
            'C': 'unless the city council allows it',
            'D': 'so that the river will be polluted',
            'E': 'so that it could use the water for its cooling systems',
        },
        'E',
        "Fabrikanın nehir kenarına kurulmasının amacı suyu kullanmaktır; amaç bildiren 'so that ... could' zaman ve anlamca uyar.",
    ),
    # düzey 3
    '0010': patch(
        '----, it is difficult to make accurate predictions about the economy.',
        {
            'A': 'Unless the economy had been stable',
            'B': 'Since predictions are correct in most cases',
            'C': 'Because all economic factors are easy to measure and control',
            'D': 'As there are so many factors that can change suddenly',
            'E': 'So that economists can work more easily and earn higher salaries',
        },
        'D',
        'Tahmin yapmanın zorluğunun nedeni birden değişebilecek çok sayıda etkendir; diğer seçenekler bu zorlukla çelişir.',
    ),
    # düzey 2
    '0011': patch(
        'Small companies often find it hard to compete with large ones, ----.',
        {
            'A': 'unless large companies had closed',
            'B': 'since they can buy materials more cheaply than large firms',
            'C': 'although they usually have fewer resources and fewer employees',
            'D': 'so large companies often close their factories in small towns',
            'E': 'since they cannot buy materials in bulk at low prices',
        },
        'E',
        'Küçük firmaların zorlanmasının nedeni büyük miktarda ucuz alım yapamamalarıdır; diğer seçenekler bu nedenle çelişir.',
    ),
    # düzey 2
    '0012': patch(
        'If the government reduces the tax on fuel, ----.',
        {
            'A': 'tax revenues were higher than expected',
            'B': 'many drivers had already sold their cars',
            'C': 'transport costs for many businesses will fall',
            'D': 'transport costs would have fallen last year',
            'E': 'the price of bread rose sharply in 2010',
        },
        'C',
        "Birinci tip koşul ('If + Simple Present') ana cümlede 'will + yalın fiil' ister: 'transport costs ... will fall'. Diğerleri zaman bakımından uyumsuzdur.",
    ),
    # düzey 2
    '0013': patch(
        'Many people now prefer to work from home, ----.',
        {
            'A': 'since it saves them the time they would spend commuting',
            'B': 'although it saves them a lot of the time they would spend in traffic',
            'C': 'even if their internet connection is fast',
            'D': 'so that their offices in the city centre were larger and quieter',
            'E': 'while the first computers were very large',
        },
        'A',
        "Evden çalışmanın tercih edilme nedeni yol süresinden tasarruftur; neden bildiren 'since' uygundur. 'Although' aynı bilgiyi karşıtlık gibi sunar ve mantığı bozar.",
    ),
    # düzey 3
    '0014': patch(
        'Although he had studied accounting for four years, ----.',
        {
            'A': 'he graduated with excellent grades',
            'B': 'he had never prepared a real set of financial statements',
            'C': 'he had learned a great many accounting rules and standards at university',
            'D': 'he found a job in a large accounting firm very easily after graduating',
            'E': 'he knew a great deal about financial statements',
        },
        'B',
        "'Although' karşıtlık ister: dört yıl muhasebe okumasına karşın gerçek bir tablo hazırlamamıştır. Diğerleri eğitimle uyumlu sonuçlardır.",
    ),
    # düzey 3
    '0015': patch(
        'The longer the meeting continued, ----.',
        {
            'A': 'the participants have become tired',
            'B': 'and so the participants gradually became more tired',
            'C': 'the most tired were the participants',
            'D': 'the more tired the participants became',
            'E': 'the participants became more tired',
        },
        'D',
        "'The + karşılaştırma ..., the + karşılaştırma ...' kalıbının ikinci yarısı da 'the more ...' ile başlar: 'the more tired the participants became'.",
    ),
    # düzey 2
    '0016': patch(
        'Unless the company improves the quality of its products, ----.',
        {
            'A': 'it has won several international awards for design',
            'B': 'its customers will be very satisfied',
            'C': 'it would have opened a new factory',
            'D': 'it will lose many of its loyal customers',
            'E': 'its sales increased by 10 percent last year',
        },
        'D',
        "'Unless' (-medikçe) olumsuz bir sonuç bekletir: kaliteyi artırmazsa müşteri kaybedecektir. Zaman olarak da 'will + yalın fiil' gerekir.",
    ),
    # düzey 3
    '0017': patch(
        'Not only did the new manager reduce costs, ----.',
        {
            'A': 'and she was criticised for wasting money',
            'B': 'so the costs went up considerably',
            'C': "but she also increased the company's market share",
            'D': 'although profits had already fallen',
            'E': 'but she will be replaced next year',
        },
        'C',
        "'Not only ...' ile başlayan devrik yapı 'but ... also' ile tamamlanır ve iki olumlu sonucu ekler: 'but she also increased ...'.",
    ),
    # düzey 2
    '0018': patch(
        'Before you sign any contract, ----.',
        {
            'A': 'the contract had been cancelled',
            'B': 'the lawyer reads it after you sign',
            'C': 'you would have read it carefully',
            'D': 'read every clause carefully',
            'E': 'you signed it without reading it',
        },
        'D',
        "Zaman yan cümlesi ('Before you sign') bir öğütle (emir kipi) tamamlanır: imzalamadan önce her maddeyi dikkatle oku.",
    ),
    # düzey 2
    '0019': patch(
        'When the central bank cut interest rates last year, ----.',
        {
            'A': 'many families took out loans to buy new homes',
            'B': 'the banks are lending less money to small firms',
            'C': 'loans became much more expensive for most families',
            'D': 'many families will take out loans to buy new cars',
            'E': 'many families have been saving more since then',
        },
        'A',
        "Faiz indirimi geçmişte borçlanmayı artırır; 'When + Simple Past' ile uyumlu, geçmiş zamanlı ve mantıklı sonuç 'took out loans'tır.",
    ),
    # düzey 2
    '0020': patch(
        'The board meeting has been postponed ----.',
        {
            'A': 'because several board members are abroad this week',
            'B': 'although none of the members can attend the meeting this week',
            'C': 'because all the board members are available this week',
            'D': 'so that the board members could not attend the meeting',
            'E': 'unless the board members had been abroad on business trips',
        },
        'A',
        'Toplantının ertelenme nedeni üyelerin yurt dışında olmasıdır.',
    ),
    # düzey 3
    '0021': patch(
        'The new phone sold out within hours, ----.',
        {
            'A': 'where people had waited outside the shops all night',
            'B': 'which shows how much demand there was for it',
            'C': 'who were waiting in long queues outside the shops',
            'D': 'which shows that nobody was really interested in it',
            'E': 'that it was much more expensive than older models',
        },
        'B',
        "Virgülden sonraki 'which' bütün cümleye gönderme yapar; birkaç saatte tükenmesi talebin büyüklüğünü gösterir.",
    ),
    # düzey 3
    '0022': patch(
        'Had the company invested in new technology earlier, ----.',
        {
            'A': 'it will not lose any customers to its rivals next year',
            'B': 'it does not lose customers to its competitors',
            'C': 'it would not have lost so many customers',
            'D': 'it had not lost customers',
            'E': 'it has not lost any of its customers so far',
        },
        'C',
        "'Had the company invested ...' devrik üçüncü tip koşuldur ('If the company had invested'); ana cümle 'would have + V3' ister.",
    ),
    # düzey 2
    '0023': patch(
        'The teacher spoke very slowly and clearly ----.',
        {
            'A': 'although the students needed help',
            'B': 'unless the students ask her questions',
            'C': 'so that all the foreign students could follow her',
            'D': 'as soon as the lesson will finish',
            'E': 'so that nobody could understand the lesson',
        },
        'C',
        "Yavaş ve açık konuşmanın amacı yabancı öğrencilerin anlayabilmesidir; 'so that ... could follow' uyar.",
    ),
    # düzey 2
    '0024': patch(
        'If you need any further information, ----.',
        {
            'A': 'please do not hesitate to contact our office',
            'B': 'you would have contacted our office',
            'C': 'our office was closed yesterday afternoon',
            'D': 'you had to contact our office before the deadline',
            'E': 'we sent you an email with all the details last week',
        },
        'A',
        "Geniş zamanlı koşul cümlesi bir rica/öneri ile tamamlanabilir: 'please do not hesitate to contact ...'. Diğerleri geçmiş zamanlıdır.",
    ),
    # düzey 3
    '0025': patch(
        'In order to attract more foreign investors, ----.',
        {
            'A': 'the procedures will have been simplified last year',
            'B': 'the government made it harder to set up a business',
            'C': 'the government simplified the rules for starting a business',
            'D': 'foreign investors have already left the country in large numbers',
            'E': 'taxes on foreign companies were increased sharply for two years',
        },
        'C',
        "Amaç yabancı yatırımcı çekmektir; bunu sağlayan eylem iş kurma kurallarının kolaylaştırılmasıdır. 'In order to'nun öznesi ana cümlenin öznesiyle (hükûmet) aynı olmalıdır.",
    ),
    # düzey 3
    '0026': patch(
        'The more you practise speaking English, ----.',
        {
            'A': 'more confident you became',
            'B': 'you will gradually become more confident when speaking',
            'C': 'the most confident you become',
            'D': 'the more confident you will become',
            'E': 'the less you will need to speak it in class',
        },
        'D',
        "'The more ..., the more ...' kalıbının ikinci yarısı da 'the + karşılaştırma' ile başlar: 'the more confident you will become'.",
    ),
    # düzey 3
    '0027': patch(
        'The report was written in a hurry; ----.',
        {
            'A': 'otherwise, it will be published tomorrow',
            'B': 'for example, it was checked by three experts',
            'C': 'in contrast, it was prepared very carefully',
            'D': 'nevertheless, it had a few mistakes in the tables',
            'E': 'consequently, it contained several calculation errors',
        },
        'E',
        "Aceleyle yazılmanın beklenen sonucu hatadır; 'consequently' uygundur. 'Nevertheless' beklenen sonucu karşıtlık gibi sunar.",
    ),
    # düzey 2
    '0028': patch(
        'Online courses have become very popular, ----.',
        {
            'A': 'so most universities stopped teaching students in classrooms',
            'B': 'partly because students must attend them in person',
            'C': 'partly because students can study at their own pace',
            'D': 'although students can study whenever and wherever they like',
            'E': 'unless the internet had been invented',
        },
        'C',
        'Çevrim içi derslerin yaygınlaşmasının nedeni öğrencinin kendi hızında ilerleyebilmesidir.',
    ),
    # düzey 3
    '0029': patch(
        'Even though she had no previous experience in sales, ----.',
        {
            'A': 'she found the job very difficult during her first few months',
            'B': 'she soon became the top seller in her team',
            'C': 'the company did not offer her the job after the interview',
            'D': 'she made many mistakes in her first month',
            'E': 'she needed some training before starting',
        },
        'B',
        "'Even though' karşıtlık ister: deneyimsiz olmasına karşın kısa sürede ekibin en çok satış yapanı olmuştur. Diğerleri deneyimsizlikle uyumlu sonuçlardır.",
    ),
    # düzey 2
    '0030': patch(
        'Our flight was cancelled because of the storm, ----.',
        {
            'A': 'so we arrived at our destination earlier than planned',
            'B': 'although the weather at the airport was terrible all day',
            'C': 'so we had to spend the night at the airport hotel',
            'D': 'unless the storm will stop before midnight tonight',
            'E': 'where we were planning to spend our summer holiday',
        },
        'C',
        'Uçuşun iptalinin sonucu geceyi otelde geçirmektir.',
    ),
    # düzey 3
    '0031': patch(
        '----, the students had already left the classroom.',
        {
            'A': 'As soon as the teacher returns',
            'B': 'When the teacher will return with the papers',
            'C': 'By the time the teacher returned with the exam papers',
            'D': 'Before the lesson starts tomorrow',
            'E': 'While the teacher is preparing the exam',
        },
        'C',
        "Ana cümledeki Past Perfect ('had already left') başka bir geçmiş olaydan önce tamamlanmayı anlatır; 'By the time + Simple Past' gerekir.",
    ),
    # düzey 2
    '0032': patch(
        'Companies must keep their accounting records for a certain period, ----.',
        {
            'A': 'so that the records could be destroyed immediately',
            'B': 'because the tax office is not allowed to check them',
            'C': 'although the tax office may ask to see them during an inspection',
            'D': 'unless they had already been audited',
            'E': 'so that the tax office can examine them if necessary',
        },
        'E',
        "Kayıtların saklanmasının amacı vergi dairesinin gerektiğinde incelemesidir; 'so that ... can' uyar.",
    ),
    # düzey 2
    '0033': patch(
        '----, you will not be allowed to enter the exam hall.',
        {
            'A': 'Since you have your identity card',
            'B': 'When you arrived at the exam building early in the morning',
            'C': 'Although you bring your identity card and exam entry document',
            'D': 'If you arrive after the exam has started',
            'E': 'If you arrived on time yesterday',
        },
        'D',
        "Ana cümle gelecekteki bir yasağı anlatır; birinci tip koşul 'If + Simple Present' gerekir ve anlamca da geç kalmak giriş yasağının nedenidir.",
    ),
    # düzey 2
    '0034': patch(
        'As the population of the city grew rapidly, ----.',
        {
            'A': 'fewer people needed buses and other public transport services',
            'B': 'the city will build new schools in the 1950s',
            'C': 'the demand for housing and public services decreased dramatically',
            'D': 'the city has been very quiet and empty',
            'E': 'the demand for housing and public services increased',
        },
        'E',
        'Nüfus artışının doğal sonucu konut ve kamu hizmeti talebinin artmasıdır.',
    ),
    # düzey 2
    '0035': patch(
        '----, the shop owner decided to stay open until midnight.',
        {
            'A': 'Although the shop was full of customers waiting to pay',
            'B': 'Since there were still many customers waiting inside',
            'C': 'Unless more customers arrive',
            'D': "Because there were no customers left in the shop after nine o'clock",
            'E': 'As soon as all the customers have gone',
        },
        'B',
        'Dükkânı gece yarısına kadar açık tutmanın nedeni içeride bekleyen müşterilerdir.',
    ),
    # düzey 2
    '0036': patch(
        'The company has been losing money for three years, ----.',
        {
            'A': 'because its profits have been increasing every quarter',
            'B': 'so the shareholders paid themselves record dividends this year',
            'C': 'so the shareholders have decided to replace the management',
            'D': 'although its sales have fallen dramatically',
            'E': 'and it will celebrate its record profits with a big party',
        },
        'C',
        'Üç yıldır zarar etmenin mantıklı sonucu yönetimin değiştirilmesidir. Diğerleri zarar ile çelişir ya da ilişkiyi ters kurar.',
    ),
    # düzey 2
    '0037': patch(
        'The company was fined by the authorities ----.',
        {
            'A': 'because it had paid all its taxes earlier than required',
            'B': 'unless it pays its taxes',
            'C': 'although it broke several rules',
            'D': 'because it had not paid its taxes on time',
            'E': 'so that it paid its taxes on time',
        },
        'D',
        'Para cezasının nedeni vergilerin zamanında ödenmemesidir; ceza olayından önceki eylem Past Perfect ile verilir.',
    ),
    # düzey 2
    '0038': patch(
        'When the auditors examined the warehouse, ----.',
        {
            'A': 'they found that some of the recorded goods were missing',
            'B': 'the company is going to hire a new accountant',
            'C': 'they will count all the items again',
            'D': 'they find that everything is in order',
            'E': 'they have been checking the cash book since morning',
        },
        'A',
        "'When + Simple Past' yan cümlesi ana cümlede de geçmiş zaman ister: 'they found that ...'.",
    ),
    # düzey 2
    '0039': patch(
        'When interest rates are low, ----.',
        {
            'A': 'saving money in banks becomes much more profitable for families',
            'B': 'people borrowed more in 1990',
            'C': 'people tend to borrow more money to buy houses and cars',
            'D': 'banks had refused to give loans',
            'E': 'people tend to stop borrowing money and start saving instead',
        },
        'C',
        'Düşük faiz borçlanmayı cazip kılar; genel doğruyu geniş zamanla anlatan seçenek uyar.',
    ),
    # düzey 3
    '0040': patch(
        'While some experts believe that prices will continue to rise, ----.',
        {
            'A': 'others agree that prices will rise further in the coming months',
            'B': 'the experts were invited to a conference',
            'C': 'prices rose sharply in the previous year',
            'D': 'others expect them to stabilise in the coming months',
            'E': 'they also think prices will keep rising for a long time',
        },
        'D',
        "'While' burada karşılaştırma/karşıtlık kurar; bazı uzmanların görüşüne karşıt görüş 'others expect them to stabilise'dir.",
    ),
    # düzey 3
    '0041': patch(
        'The company did not meet its sales target this year; ----.',
        {
            'A': 'as a result, its customers were very satisfied',
            'B': "in other words, its sales exceeded all of the managers' expectations",
            'C': 'therefore, it paid record bonuses to its sales staff',
            'D': 'nevertheless, it managed to reduce its costs significantly',
            'E': 'for example, it sold more products than ever before in its history',
        },
        'D',
        "Hedefi tutturamamakla maliyeti düşürebilmek arasında karşıtlık var; 'nevertheless' uyar. Diğerleri ilk cümleyle çelişir ya da ilgisiz sonuç kurar.",
    ),
    # düzey 3
    '0042': patch(
        'Although electric cars are becoming more popular, ----.',
        {
            'A': 'more and more people are buying them every year',
            'B': 'they produce no exhaust emissions while driving',
            'C': 'their batteries have become cheaper in recent years',
            'D': 'many governments support them with tax reductions',
            'E': 'their high prices still prevent many people from buying them',
        },
        'E',
        "'Although' karşıtlık ister: yaygınlaşmalarına rağmen yüksek fiyat almayı engellemektedir. Diğer seçenekler yaygınlaşmayı destekler, karşıtlık kurmaz.",
    ),
    # düzey 3
    '0043': patch(
        "Although the company's revenue increased by 20 percent last year, ----.",
        {
            'A': 'it will open two new stores in the coming spring',
            'B': 'its net profit decreased because of rising financial expenses',
            'C': 'many customers bought its products online',
            'D': 'its sales team received large bonuses for the strong growth in revenue',
            'E': 'the increase was mainly due to higher export sales in European markets',
        },
        'B',
        "'Although' karşıtlık ister: gelir arttığı hâlde kârın düşmesi beklenenin tersidir. Diğer seçenekler gelir artışıyla uyumlu ya da ilgisiz bilgi verir, karşıtlık kurmaz.",
    ),
    # düzey 3
    '0044': patch(
        'It was such a difficult exam ----.',
        {
            'A': 'that only a few students managed to finish it on time',
            'B': 'so that only a few students could finish it',
            'C': 'that most students finished it easily in less than half an hour',
            'D': 'as only a few students managed to finish',
            'E': 'than the students had expected',
        },
        'A',
        "'Such ... that' kalıbı sonuç bildirir; sınavın zorluğuyla uyumlu sonuç az öğrencinin bitirebilmesidir.",
    ),
    # düzey 3
    '0045': patch(
        '----, the number of tourists visiting the city has doubled.',
        {
            'A': 'Although the airport attracted more airlines',
            'B': 'When the new airport will be opened in the north of the city',
            'C': 'Until the airport was closed last year',
            'D': 'Since the new airport was opened five years ago',
            'E': 'Unless the new airport is opened',
        },
        'D',
        "Ana cümle Present Perfect'tir ('has doubled'); başlangıç noktasını veren 'Since + geçmiş' gerekir.",
    ),
    # düzey 3
    '0046': patch(
        'The company introduced flexible working hours; ----.',
        {
            'A': 'on the contrary, working hours remained exactly the same as before',
            'B': 'otherwise, its employees had been happier',
            'C': 'for instance, its competitors will do the same thing next year',
            'D': 'as a result, employee satisfaction improved significantly',
            'E': 'in other words, it closed several of its branches',
        },
        'D',
        "Esnek çalışma saatlerinin doğal sonucu çalışan memnuniyetinin artmasıdır; sonuç bildiren 'as a result' uyar. 'On the contrary' ilk cümleyle çelişir.",
    ),
    # düzey 2
    '0047': patch(
        'If the weather is good this weekend, ----.',
        {
            'A': 'we have been having picnics since May',
            'B': 'we are going to have a picnic by the lake',
            'C': 'we will stay at home because of the rain',
            'D': 'we had a picnic by the lake last weekend',
            'E': 'we would have had a picnic in the park with friends',
        },
        'B',
        "Gelecekle ilgili olası koşul gelecek zamanlı bir planla tamamlanır: 'we are going to have a picnic'.",
    ),
    # düzey 3
    '0048': patch(
        'The price of gold usually rises during times of crisis, ----.',
        {
            'A': 'as investors see it as a safe place for their savings',
            'B': 'although nobody wants to buy it',
            'C': 'but investors consider it a safe place to keep money',
            'D': 'so the demand for gold falls dramatically',
            'E': 'when the first coins were made in Lydia',
        },
        'A',
        "Kriz dönemlerinde altının yükselmesinin nedeni güvenli liman görülmesidir; neden bildiren 'as' uyar. 'But' karşıtlık kurar, ama iki bilgi çelişmez.",
    ),
    # düzey 3
    '0049': patch(
        'Even if the company receives the new investment, ----.',
        {
            'A': 'it would have needed much more money to survive',
            'B': 'it will no longer need to worry about its costs',
            'C': 'because it has enough cash in its bank accounts',
            'D': 'it received the investment from foreign partners last year',
            'E': 'it will still need to cut some of its costs',
        },
        'E',
        "'Even if' (-se bile) koşul gerçekleşse de sonucun değişmeyeceğini anlatır: yatırım gelse bile maliyet kısmak gerekecektir. 'No longer need to worry' bu anlamla çelişir.",
    ),
    # düzey 3
    '0050': patch(
        'Scientists have discovered a new species of fish in the Black Sea, ----.',
        {
            'A': 'whose was unknown before',
            'B': 'which had not been recorded there before',
            'C': 'that it lives in very deep water',
            'D': 'who has lived in those cold waters for centuries',
            'E': 'where had not been recorded by scientists before',
        },
        'B',
        "Virgülle ayrılan ilgi cümlesinde nesne/hayvan için 'which' kullanılır ve ardından fiil gelir; diğerleri yapıca bozuktur.",
    ),
    # düzey 3
    '0051': patch(
        'Many young people move to big cities, ----.',
        {
            'A': 'where there are more job opportunities',
            'B': 'although there are more opportunities there',
            'C': 'whose job opportunities are rather limited',
            'D': 'who offers more jobs and better education',
            'E': 'which there are more job and education opportunities',
        },
        'A',
        "Yer bildiren 'big cities' ardından tam cümle geldiği için 'where' gerekir; 'which/who' yapıca, 'although' anlamca uymaz.",
    ),
    # düzey 2
    '0052': patch(
        'The new metro line will reduce traffic in the city centre, ----.',
        {
            'A': 'unless it has been opened in 2010',
            'B': 'as many commuters will leave their cars at home',
            'C': 'but fewer people will use public transport',
            'D': 'so that more cars entered the city centre',
            'E': 'since more people bought cars last year',
        },
        'B',
        'Trafiğin azalmasının nedeni insanların arabalarını evde bırakmasıdır; zaman olarak da gelecek uyar.',
    ),
    # düzey 2
    '0053': patch(
        "Because the company's main warehouse was damaged in the flood, ----.",
        {
            'A': 'its sales reached a record level in the same month',
            'B': 'deliveries to customers were delayed for several weeks',
            'C': 'deliveries will be delayed if it rains heavily again next year',
            'D': 'customers received their orders much earlier than usual',
            'E': 'the warehouse has been built in 1998',
        },
        'B',
        'Depo hasarının doğal sonucu teslimatların gecikmesidir; geçmiş zamanlı sonuç cümlesi uyar.',
    ),
    # düzey 2
    '0054': patch(
        'Some people prefer to shop at local markets, ----.',
        {
            'A': 'unless the local markets are open on Sundays and holidays',
            'B': 'although the products there are often fresher and cheaper too',
            'C': 'so the products there were bought online by most families',
            'D': 'because the products there are much more expensive than in shops',
            'E': 'as the products there are often fresher and cheaper',
        },
        'E',
        "Pazarı tercih etmenin nedeni ürünlerin taze ve ucuz olmasıdır; neden bildiren 'as' uyar.",
    ),
    # düzey 3
    '0055': patch(
        '----, the bank refused to give the company a loan.',
        {
            'A': 'Unless the firm submits its financial statements',
            'B': 'Since the firm could not provide any collateral',
            'C': 'As soon as the firm has paid back all of its old debts to other banks',
            'D': 'If the manager had signed the loan documents a few weeks earlier',
            'E': 'So that the firm could expand its production',
        },
        'B',
        "Ana cümle geçmişte bir reddi anlatır; nedenini veren 'Since the firm could not provide any collateral' anlam ve zaman bakımından uyar. 'If ... had signed' üçüncü tip koşuldur ve ana cümlede 'would have' ister.",
    ),
    # düzey 2
    '0056': patch(
        '----, he was able to pay off his student loan in just three years.',
        {
            'A': 'By saving a large part of his monthly salary',
            'B': 'Although his parents supported him financially',
            'C': 'Despite having a well-paid and secure job',
            'D': 'Unless he finds a part-time job',
            'E': 'Because he lost his job soon after graduating',
        },
        'A',
        'Borcunu üç yılda kapatabilmesinin yolu maaşının büyük kısmını biriktirmesidir. Diğerleri ya karşıtlık/neden ilişkisini ters kurar ya da zaman bakımından uymaz.',
    ),
    # düzey 2
    '0057': patch(
        'Unless we leave the office now, ----.',
        {
            'A': 'we will catch the last train easily',
            'B': 'we missed the last train home yesterday evening',
            'C': 'we would have caught the train',
            'D': 'we are arriving home much earlier than usual',
            'E': 'we will miss the last train home',
        },
        'E',
        "'Unless' olumsuz bir sonuç bekletir: şimdi çıkmazsak son treni kaçıracağız.",
    ),
    # düzey 2
    '0058': patch(
        'Credit cards are convenient for shoppers; ----.',
        {
            'A': 'however, they can lead to serious debt if used carelessly',
            'B': 'for example, they were invented in the 1950s',
            'C': 'therefore, many banks refuse to issue them',
            'D': 'similarly, cash is no longer accepted in shops',
            'E': 'in addition, nobody uses them online',
        },
        'A',
        "Kolaylık ile borç riski arasında karşıtlık vardır; 'however' ile kurulan seçenek anlamca uyar.",
    ),
    # düzey 3
    '0059': patch(
        'Despite working long hours every day, ----.',
        {
            'A': 'she had to work at weekends too',
            'B': 'she was very tired when she got home in the evenings',
            'C': 'she earned a high salary',
            'D': 'she finished all her tasks easily and went home early',
            'E': 'she still could not finish her tasks on time',
        },
        'E',
        "'Despite' karşıtlık ister: uzun saatler çalışmasına karşın işlerini yetiştirememiştir. Diğerleri uzun çalışmayla uyumlu sonuçlardır.",
    ),
    # düzey 2
    '0060': patch(
        'Prices in the restaurant are quite high; ----.',
        {
            'A': 'in addition, it is the cheapest restaurant in town',
            'B': 'therefore, university students eat there almost every day',
            'C': 'in other words, it is very affordable',
            'D': 'for instance, a main course costs very little compared with other places',
            'E': 'on the other hand, the food and service are excellent',
        },
        'E',
        "Yüksek fiyatın karşısına olumlu bir özellik koyan 'on the other hand' uyar; diğerleri ilk cümleyle çelişir.",
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
    print(f"1 paket / {len(PATCHES)} soru ('Okuma ve Boşluk Doldurma (Reading & Cloze)' yapisal kalibrasyon) iki repoda dogrulandi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
