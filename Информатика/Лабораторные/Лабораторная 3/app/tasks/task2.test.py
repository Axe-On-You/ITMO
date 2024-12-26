import unittest
import task2

class TestTask2(unittest.TestCase):
    def test_example(self):
        data = 'А ты знал, что ВТ - лучшая кафедра в ИТМО?'
        result = ['ВТ лучшая кафедра в ИТМО'] #0
        self.assertEqual(result, task2.solve(data))

    def test_example_multiply(self):
        data = 'А ты знал, что ВТ - лучшая кафедра ИТМО?\nА ты знал, что ВТ - лучшая кафедра ИТМО?\nИТМО ВТ Спросил Он спокойно'
        result = ['ВТ лучшая кафедра ИТМО', 'ВТ лучшая кафедра ИТМО', 'ВТ лучшая кафедра ИТМО ИТМО'] #1
        self.assertEqual(result, task2.solve(data))

    def test_simple(self):
        data = 'ВТ тут было написано ИТМО ВТ это ИТМО'
        result = ['ВТ тут было написано ИТМО', 'ВТ это ИТМО'] #2
        self.assertEqual(result, task2.solve(data))

    def test_all_occurrences(self):
        data = 'ВТ ВТ ВТ мяу гав мууу ИТМО ИТМО'
        result = ['ВТ ВТ мяу гав мууу ИТМО', 'ВТ мяу гав мууу ИТМО', 'ВТ мяу гав мууу ИТМО ИТМО'] # Все вхождения 3
        self.assertEqual(result, task2.solve(data))
    
    def test_many_vt_together(self):
        data = 'ВТВТВТВТ ВТВТВТ lorem ipsum ИТМО ИТМО ИТМО' # Так как нет слова "ВТ", то и выводить нечего
        result = []  #4.1
        self.assertEqual(result, task2.solve(data))

    def test_many_itmo_together(self):
        data = 'ВТ ИТМОИТМОИТМОИТМО' # Так как нет слова "ИТМО", то и выводить нечего
        result = [] #4.2
        self.assertEqual(result, task2.solve(data))

    def test_simbols(self):
        data = 'ВТ слово ??? ?*( ! {} [] )-... ^^@ ;%; "%"%"% ___ тоже слово ИТМО' # Проверка на символы (!?@{}[]...)
        result = ['ВТ слово ___ тоже слово ИТМО'] #5
        self.assertEqual(result, task2.solve(data)) 

    def test_all_together(self):
        data = 'ВТ ВТ ВТ - это :-(    Мы любим   ;=)  ИТМО ИТМО' # Всё вместе
        result = ['ВТ ВТ это Мы любим ИТМО', 'ВТ это Мы любим ИТМО', 'ВТ это Мы любим ИТМО ИТМО'] #6
        self.assertEqual(result, task2.solve(data))

if __name__ == '__main__':
    unittest.main()