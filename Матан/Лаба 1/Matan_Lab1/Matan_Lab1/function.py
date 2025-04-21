from numpy import arccos  # Используем библиотеку math для импорта функции arccos


def func(x):
    y = arccos(x**2) - x  # Исходная функция, для которой ищем корень
    return y