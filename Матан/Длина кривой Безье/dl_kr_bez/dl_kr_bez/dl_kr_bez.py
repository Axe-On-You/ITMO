import numpy as np
from scipy.optimize import minimize
from scipy.integrate import quad
import matplotlib.pyplot as plt

# =============================================
# 1. Входные данные
# =============================================
P0 = np.array([0.0, 0.0])   # Начальная точка
P2 = np.array([10.0, 0.0])  # Конечная точка
K = np.array([3.0, 8.0])     # Точка, через которую проходит кривая

# =============================================
# 2. Вспомогательные функции
# =============================================

def calculate_P1(tk):
    """Вычисляет контрольную точку P1 для заданного tk."""
    if tk <= 0 or tk >= 1:
        raise ValueError("tk должен быть в (0, 1)")
    
    numerator = K - (1 - tk)**2 * P0 - tk**2 * P2
    denominator = 2 * tk * (1 - tk)
    
    if abs(denominator) < 1e-9:
        raise ValueError("Деление на ноль")
    
    return numerator / denominator

def bezier_curve(t, P1):
    """Возвращает точку на кривой Безье для параметра t."""
    return (1 - t)**2 * P0 + 2 * t * (1 - t) * P1 + t**2 * P2

def bezier_derivative(t, P1):
    """Вычисляет производную кривой Безье в точке t."""
    return 2 * (1 - t) * (P1 - P0) + 2 * t * (P2 - P1)

def curve_length(P1):
    """Вычисляет длину кривой Безье."""
    integrand = lambda t: np.linalg.norm(bezier_derivative(t, P1))
    length, _ = quad(integrand, 0, 1, epsabs=1e-9)
    return length

# =============================================
# 3. Функция для оптимизации
# =============================================

def objective(tk):
    """Целевая функция для минимизации."""
    try:
        P1 = calculate_P1(tk)
        return curve_length(P1)
    except ValueError:
        return float('inf')  # Штраф за недопустимые значения

# =============================================
# 4. Поиск оптимального tk
# =============================================

# Начальное приближение и границы
initial_guess = 0.4
bounds=[(1e-3, 1 - 1e-3)]

# Запуск оптимизации
result = minimize(lambda x: objective(x[0]),
                  x0=[0.4],
                  bounds=[(1e-3, 1-1e-3)],
                  method='SLSQP',
                  options={'ftol': 1e-10, 'maxiter': 1000})

optimal_tk = result.x[0]
optimal_P1 = calculate_P1(optimal_tk)
optimal_length = curve_length(optimal_P1)

# =============================================
# 5. Визуализация
# =============================================

# Генерация точек кривой
t_values = np.linspace(0, 1, 100)
curve_points = np.array([bezier_curve(t, optimal_P1) for t in t_values])

# Настройка графика
plt.figure(figsize=(10, 6))
plt.title(f'Кривая Безье\nДлина: {optimal_length:.6f}, tk: {optimal_tk:.6f}')
plt.grid(True, linestyle='--', alpha=0.7)

# Отображение кривой и точек
plt.plot(curve_points[:, 0], curve_points[:, 1], 'b-', label='Кривая Безье')
plt.scatter([P0[0], K[0], P2[0]], [P0[1], K[1], P2[1]], 
           c='red', s=100, zorder=3, label='Опорные точки')
plt.scatter([optimal_P1[0]], [optimal_P1[1]], 
           c='green', s=100, marker='X', label='Контрольная точка (P1)')

# Аннотации
plt.annotate(f'P0 {P0}', (P0[0]+0.5, P0[1]+0.5))
plt.annotate(f'K {K}', (K[0]+0.5, K[1]+0.5))
plt.annotate(f'P2 {P2}', (P2[0]-2.5, P2[1]+0.5))
plt.annotate(f'P1 ({optimal_P1[0]:.6f}, {optimal_P1[1]:.6f})', 
            (optimal_P1[0]+0.5, optimal_P1[1]+0.5))

plt.legend()
plt.axis('equal')
plt.show()

# =============================================
# 6. Вывод результатов
# =============================================

print("\nРезультаты оптимизации:")
print(f"Оптимальный параметр tk: {optimal_tk:.6f}")
print(f"Контрольная точка P1: ({optimal_P1[0]:.6f}, {optimal_P1[1]:.6f})")
print(f"Минимальная длина кабеля: {optimal_length:.6f}")
print(f"Количество итераций: {result.nit}")
print(f"Статус оптимизации: {result.message}")
