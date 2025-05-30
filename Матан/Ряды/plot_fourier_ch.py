import numpy as np
import matplotlib.pyplot as plt

# Определение функции f(x) = ch(alpha*x)
def f(x, alpha):
    return np.cosh(alpha * x)

# Коэффициент a_0/2
def get_a0_half(alpha):
    if alpha == 0:
        return 1.0
    else:
        # Обработка случая alpha -> 0 для численной стабильности, хотя аналитически предел 1
        if np.isclose(alpha, 0.0):
             return 1.0 + (alpha**2 * np.pi**2)/6.0 # Первые два члена разложения sh(y)/y = (y + y^3/6 + ...)/y
        return np.sinh(alpha * np.pi) / (np.pi * alpha)

# Коэффициенты a_n для n >= 1
def get_an(n, alpha):
    if alpha == 0:
        return 0.0
    else:
        # Обработка случая alpha -> 0
        if np.isclose(alpha, 0.0):
            return 0.0 # так как alpha в числителе
        return (2 * alpha * ((-1)**n) * np.sinh(alpha * np.pi)) / (np.pi * (alpha**2 + n**2))

# Частичная сумма ряда Фурье S_N(x)
def S_N_fourier(x_vals, N, alpha):
    a0_half_val = get_a0_half(alpha)
    y_sum = np.full_like(x_vals, a0_half_val) # Начинаем с a_0/2

    # Если alpha = 0, то f(x)=1, и S_N(x) = 1 (a_n = 0 для n>=1)
    if alpha == 0:
        return y_sum

    for n_term in range(1, N + 1):
        an_val = get_an(n_term, alpha)
        y_sum += an_val * np.cos(n_term * x_vals)
    return y_sum

# Параметры для построения
alpha_val = 0.5  # Вы можете изменить это значение
x = np.linspace(-np.pi, np.pi, 500) # Диапазон x от -pi до pi

# Вычисление значений исходной функции
y_f = f(x, alpha_val)

# Значения N для частичных сумм
N_values = [1, 3, 10]

# Построение графиков
plt.figure(figsize=(12, 8))

# График исходной функции
plt.plot(x, y_f, label=f'$f(x) = \cosh({alpha_val}x)$', color='black', linewidth=2)

# Графики частичных сумм
colors = ['red', 'green', 'blue']
linestyles = [':', '--', '-.']

for i, N_val in enumerate(N_values):
    y_S_N = S_N_fourier(x, N_val, alpha_val)
    plt.plot(x, y_S_N, label=f'$S_{{{N_val}}}(x)$', color=colors[i % len(colors)], linestyle=linestyles[i % len(linestyles)], linewidth=1.5)

# Настройка графика
plt.title(f'Функция $f(x) = \cosh({alpha_val}x)$ и ее ряд Фурье на $[-\pi, \pi]$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.grid(True)
plt.ylim(bottom=0, top=np.cosh(alpha_val * np.pi) * 1.1 if alpha_val !=0 else 2) # Установка пределов по y для наглядности
plt.axvline(-np.pi, color='gray', linestyle='--', linewidth=0.8)
plt.axvline(np.pi, color='gray', linestyle='--', linewidth=0.8)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], ['$-\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$'])

# Показать график
plt.show()
