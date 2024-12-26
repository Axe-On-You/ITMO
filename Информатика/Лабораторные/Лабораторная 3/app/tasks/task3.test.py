import unittest
import task3

class TestTask3(unittest.TestCase):
    def test_example(self):
        data = '<meta name="daily_volume" content="В суточным объемом торгов' \
        '₽2,835,029,974,960.63 RUB."/> <meta name="daily_price" content="Мы обновляем' \
        'нашу цену BTC к RUB в режиме реального времени."/> <meta name="daily_price"' \
        'content=" Цена Bitcoin в реальном времени сегодня составляет ₽5,797,806.88' \
        'RUB."/><meta name="daily_price" content="Ethereum стоит на данный момент' \
        '₽229,590,78 RUB."/>'
        result = '5,797,806.88' #0
        self.assertEqual(result, task3.solve(data))

    def test_numbers_between(self):
        data = '<meta name="daily_price content=" Цена Bitcoin в реальном времени сегодня"' \
        'составляет ₽5,797,806.88 RUB."/><meta name="daily_price" content="Ethereum' \
        'стоит на данный момент ₽229,590,78 RUB."/><<meta name="real_time_price"' \
        'content="Реальная стоимость Bitcoin на момент написания лабораторной работы' \
        'номер 3 (18.10.2024 19:28) составляет ₽6,541,918.55 RUB>' # Числа между словом "Bitcoin" и ценой биткоина
        result = '6,541,918.55' #1
        self.assertEqual(result, task3.solve(data))

    def test_simbols_between(self):
        data = '<meta name="market_info" content="По последним данным, стоимость Bitcoin' \
        'на данный момент ¯\_(ツ)_/¯ (づ｡◕‿‿◕｡)づ  ! "" №;%:? ...        составляет' \
        '₽6,540,337.00 RUB и продолжает расти."/>' # Символы между словом "Bitcoin" и ценой биткоина
        result = '6,540,337.00' #2
        self.assertEqual(result, task3.solve(data))

    def test_many_coincidences(self):
        data = '<meta name="description" content="Bitcoin - это криптовалюта,' \
        'которая в 2013 году стоила всего $70,15 USD, что равнялось по тому курсу' \
        '₽2,104.50 RUB, но сегодня Bitcoin стоит ₽6,540,337.52 RUB. На момент' \
        'написания статьи, Bitcoin стоил ₽3,333,333.33 RUB, что являлось отличной' \
        'возможностью для инвестиций. Хотя автор bitcoin бы и за ₽5,252.52 RUB не взял"/>' # Много совадений
        result = '6,540,337.52' #3
        self.assertEqual(result, task3.solve(data))

    def test_lot_of_extra_stuff(self):
        data = '<meta name="lazy" content="Мне стало лень придумывать всякое, так' \
        'что теперь в ход идут "голые" примеры. bitcoin = ₽555,555.77 RUB' \
        'TON = ₽3,152.11 RUB NOT ₽555,555.77 RUB Bitcoin = ₽556,555.77 RUB"/>' # Много всякой всячины
        result = '556,555.77'  #4
        self.assertEqual(result, task3.solve(data))
    
    def test_incorrect_input(self):
        data = 'Bitcoin = ₽555555.77 RUB или же Bitcoin = ₽557555.77 RUB,' \
        'а может лучше Bitcoin = ₽666,666,666.66 RUB' # Ввод первых двух чисел неверен
        result = '666,666,666.66' #5
        self.assertEqual(result, task3.solve(data))

if __name__ == '__main__':
    unittest.main()