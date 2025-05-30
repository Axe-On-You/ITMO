import numpy as np
import matplotlib.pyplot as plt

# Параметры функции и ряда
T = 4.0  # Период
omega0 = 2 * np.pi / T  # Основная угловая частота (pi/2)

# Комплексные коэффициенты Фурье c_k
def get_ck(k):
    if k == 0:
        return 0.5
    else:
        term1 = (1 - (-1)**k) / ((k * np.pi)**2)
        term2 = -1j / (k * np.pi) # 1j это i
        return term1 + term2

# Частичная сумма ряда Фурье в комплексной форме S_N(t)
# S_N(t) = sum_{k=-N}^{N} c_k * exp(i * k * omega0 * t)
def S_N_fourier_complex(t_vals, N):
    s_sum = np.zeros_like(t_vals, dtype=np.complex128)
    for k_val in range(-N, N + 1):
        ck = get_ck(k_val)
        s_sum += ck * np.exp(1j * k_val * omega0 * t_vals)
    return np.real(s_sum) # Сумма должна быть вещественной, берем реальную часть

# Целевая функция S_target(t), к которой сходится ряд Фурье
def S_target(t_val_array):
    results = np.zeros_like(t_val_array, dtype=float)
    for i, t_val in enumerate(t_val_array):
        # Нормализуем t к одному периоду [0, T) для основного анализа,
        # но точки разрыва обрабатываем точно по t_val
        
        # Точки разрыва t = n*T
        if np.isclose(t_val % T, 0.0) and not (np.isclose(t_val, 0.0) and t_val < 0): # t=0, T, 2T, -T, -2T...
             # Для t=0, если t_val отрицателен, t_val % T может дать 0, но это не начало периода [0,T)
             # Например, -4 % 4 = 0. Для таких случаев значение 1.
             # Для положительных t или t=0, t%T=0 означает точку разрыва nT.
            results[i] = 1.0
        else:
            t_mod = t_val % T
            if t_mod < 0: # Гарантируем, что t_mod находится в [0, T)
                t_mod += T
            
            if 0.0 < t_mod < 2.0:
                results[i] = 2.0 - t_mod
            elif np.isclose(t_mod, 2.0): # Точка непрерывности, но конец одного линейного сегмента
                results[i] = 0.0
            elif 2.0 < t_mod < T:
                results[i] = 0.0
            # Случай t_mod -> 0 (но не сам 0) уже покрыт выше.
            # Случай t_mod -> T (но не сам T) уже покрыт выше.
    return results

# Параметры для построения
N_sum_terms = 50  # Количество членов в сумме (от -N до N)
t_plot = np.linspace(-T, 2*T, 1000) # Диапазон t для графика (например, 3 периода: от -4 до 8)

# Вычисление значений частичной суммы ряда Фурье
y_S_N = S_N_fourier_complex(t_plot, N_sum_terms)

# Вычисление значений целевой функции S_target(t)
y_S_target = S_target(t_plot)

# Построение графиков
plt.figure(figsize=(15, 7))

# График частичной суммы S_N(t)
plt.plot(t_plot, y_S_N, label=f'$S_{{{N_sum_terms}}}(t)$ (сумма ряда Фурье, N={N_sum_terms})', color='blue', linewidth=1.5)

# График целевой функции S_target(t)
# Для более точного отображения разрывов, можно построить сегментами
# или использовать S_target и отдельно отметить точки разрыва.
plt.plot(t_plot, y_S_target, label='$S_{target}(t)$ (предельная сумма)', color='red', linestyle='--', linewidth=2.0, alpha=0.7)

# Отметим значения в точках разрыва для S_target
discontinuity_points_t = np.arange(-T, 2*T + T/10, T) # точки 0, +/-T, +/-2T ...
s_at_discontinuities = [S_target(np.array([tp]))[0] for tp in discontinuity_points_t] # S_target уже возвращает 1.0
plt.plot(discontinuity_points_t, s_at_discontinuities, 'o', color='red', markersize=8, label='Значения $S(t)$ в точках $t=nT$')


# Настройка графика
plt.title('График суммы ряда Фурье в комплексной форме для заданной функции')
plt.xlabel('$t$')
plt.ylabel('$S(t)$')
plt.legend(loc='upper right')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
# Вертикальные линии для обозначения периодов
for i in range(int(t_plot[0]/T) -1, int(t_plot[-1]/T) + 2):
    plt.axvline(i * T, color='gray', linestyle=':', linewidth=0.8)

plt.xticks(np.arange(-T, 2*T + 1, T/2)) # Метки на оси X
plt.ylim(-0.5, 2.5)

# Показать график
plt.show()