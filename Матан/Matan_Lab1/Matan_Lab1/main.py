from BISECT import bisect
from function import func


# Задаем параметры для метода бисекций
a = 0.5
b = 1.0
eps = 5 * 10**(-16)

# Находим корень функции с помощью метода бисекций
root, k = bisect(a, b, eps, func)

# Выводим результат
print("Корень функции:", root)
print("Произошло итераций:", k)