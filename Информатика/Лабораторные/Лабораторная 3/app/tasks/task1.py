import re

def solve(string):
    """ Возвращает количество смайликов вида X-{/ в строке
    466730 % 6 = 2 => Глаза: X
    466730 % 4 = 2 => Нос: -{
    466730 % 7 = 5 => Рот: /
    """
    pattern = r'X-{/'
    return len(re.findall(pattern, string))