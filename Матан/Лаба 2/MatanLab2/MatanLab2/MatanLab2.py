import numpy as np
import sympy as sp

def f(x):
    return np.cos(x**3)

a, b = 0, 1
reference = 0.931704440591544

# Вычисление производных с помощью SymPy
x = sp.Symbol('x')
f_sym = sp.cos(x**3)

# Вторая производная
f2_sym = sp.diff(f_sym, x, 2)
f2_lambda = sp.lambdify(x, f2_sym, 'numpy')

# Четвертая производная
f4_sym = sp.diff(f_sym, x, 4)
f4_lambda = sp.lambdify(x, f4_sym, 'numpy')

# Находим максимумы производных на [0, 1]
x_vals = np.linspace(0, 1, 1000)
M2 = max(abs(f2_lambda(x_vals)))
M4 = max(abs(f4_lambda(x_vals)))

# Функция для ввода чисел с плавающей точкой
def input_epsilon():
    while True:
        try:
            value = input("Введите точность ε (формат: 1e-5, 0.00001; по умолчанию 1e-5): ").strip()
            if not value:
                return 1e-5
            return float(value)
        except ValueError:
            print("Ошибка: введите число в формате 0.0001 или 1e-4!")

# Функция для безопасного ввода целых чисел
def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Ошибка: введите целое положительное число!")

# Ввод параметров
epsilon = input_epsilon()
print(f"\nУстановленная точность: ε = {epsilon:.0e}" if epsilon < 0.001 else f"\nУстановленная точность: ε = {epsilon}")

n_rect = input_int("Введите количество интервалов n для метода прямоугольников: ")
n_trap = input_int("Введите количество интервалов n для метода трапеций: ")
m_simp = input_int("Введите количество пар интервалов m для метода Симпсона (n = 2m): ")

# Метод прямоугольников
def rectangle_method(n):
    h = (b - a) / n
    total = 0.0
    for i in range(n):
        x_mid = a + (i + 0.5) * h
        total += f(x_mid)
    return h * total

# Проверка точности для прямоугольников
h_rect = (b - a)/n_rect
error_rect = (b - a)/24 * M2 * h_rect**2
print("\n" + "═"*75)
if error_rect > epsilon:
    print(f"Для метода прямоугольников (n = {n_rect}) теоретическая погрешность {error_rect:.2e} > ε!")
else:
    I_rect = rectangle_method(n_rect)
    print(f"Метод прямоугольников (n = {n_rect}): {I_rect:.10f}")
    print(f"Отклонение от эталона: {abs(I_rect - reference):.2e}")

# Метод трапеций
def trapezoid_method(n):
    h = (b - a) / n
    total = (f(a) + f(b)) / 2
    for i in range(1, n):
        total += f(a + i * h)
    return h * total

# Проверка точности для трапеций
h_trap = (b - a)/n_trap
error_trap = (b - a)/12 * M2 * h_trap**2
print("\n" + "═"*75)
if error_trap > epsilon:
    print(f"Для метода трапеций (n={n_trap}) теоретическая погрешность {error_trap:.2e} > ε!")
else:
    I_trap = trapezoid_method(n_trap)
    print(f"Метод трапеций (n = {n_trap}): {I_trap:.10f}")
    print(f"Отклонение от эталона: {abs(I_trap - reference):.2e}")

# Метод Симпсона
def simpson_method(m):
    n = 2 * m
    h = (b - a) / n
    total = f(a) + f(b)
    # Сумма нечётных узлов
    for i in range(1, m + 1):
        total += 4 * f(a + (2 * i - 1) * h)
    # Сумма чётных узлов
    for i in range(1, m):
        total += 2 * f(a + 2 * i * h)
    return (h / 3) * total

# Проверка точности для Симпсона
h_simp = (b - a)/(2*m_simp)
error_simp = (b - a)/180 * M4 * h_simp**4
print("\n" + "═"*75)
if error_simp > epsilon:
    print(f"Для метода Симпсона (m = {m_simp}) теоретическая погрешность {error_simp:.2e} > ε!")
else:
    I_simp = simpson_method(m_simp)
    print(f"Метод Симпсона (m = {m_simp}): {I_simp:.10f}")
    print(f"Отклонение от эталона: {abs(I_simp - reference):.2e}")

# Итоговое сравнение (Вывод эталонного значения)
print("\n" + "═"*75)
print(f"\nЭталонное значение: {reference:.15f}")