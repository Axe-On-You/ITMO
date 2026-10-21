import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from mpl_toolkits.mplot3d import Axes3D

# ==============================================================================
# ВАРИАНТ 2
# ==============================================================================
data = np.array([
    [1.01, 1.07, 1.04],
    [2.05, 1.75, 3.24],
    [2.99, 2.94, 4.60],
    [3.99, 4.06, 1.68],
    [5.27, 5.03, 0.38]
])

X = data[:, 0]  
Y = data[:, 1] 
Z = data[:, 2]

# --- ИСТОРИЯ ОШИБКИ ---
loss_history = []

def gauss_2d(x, y, A, x0, y0, sigma_x, sigma_y, theta=0, offset=0):
    if theta != 0:
        x_new = (x - x0) * np.cos(theta) + (y - y0) * np.sin(theta)
        y_new = -(x - x0) * np.sin(theta) + (y - y0) * np.cos(theta)
    else:
        x_new = x - x0  
        y_new = y - y0
    exp_part = np.exp(-(x_new**2 / (2 * sigma_x**2) + y_new**2 / (2 * sigma_y**2)))
    return A * exp_part + offset

def loss_function(model_params):
    A, x0, y0, sigma_x, sigma_y, theta, offset = model_params
    if sigma_x <= 0 or sigma_y <= 0 or A <= 0:
        return 1e10
    
    predictions = gauss_2d(X, Y, A, x0, y0, sigma_x, sigma_y, theta, offset)
    mse = 0.5 * np.mean((predictions - Z)**2)
    return mse

# Callback-функция для сохранения прогресса
def loss_callback(xk):
    loss_history.append(loss_function(xk))

# Начальное приближение
max_idx = np.argmax(Z)
params_start = [Z[max_idx]+0.1, X[max_idx], Y[max_idx], np.std(X)*0.5, np.std(Y)*0.5, 0.0, 0.0]

bounds = [
    (0.1, 10.0), (0.0, 6.0), (0.0, 6.0),
    (0.1, 5.0), (0.1, 5.0), (-np.pi/4, np.pi/4), (-1.0, 1.0)
]

# Добавляем callback в minimize
result = minimize(loss_function, params_start, method='L-BFGS-B', 
                  bounds=bounds, callback=loss_callback)

# ==============================================================================
# ОБНОВЛЕННАЯ ВИЗУАЛИЗАЦИЯ (3 ГРАФИКА)
# ==============================================================================
fig = plt.figure(figsize=(18, 5)) # Увеличили ширину для 3-х графиков

# 1. График Loss Function (Логарифмическая шкала)
ax_loss = fig.add_subplot(131)
ax_loss.plot(range(len(loss_history)), loss_history, marker='o', color='firebrick', markersize=4)
ax_loss.set_yscale('log') # Логарифмическая шкала лучше показывает сходимость
ax_loss.set_title('Кривая обучения (Loss history)')
ax_loss.set_xlabel('Итерация')
ax_loss.set_ylabel('MSE (log scale)')
ax_loss.grid(True, which="both", ls="-", alpha=0.2)

# 2. Поверхность 3D
x_grid = np.linspace(0, 6, 50)
y_grid = np.linspace(0, 6, 50)
X_grid, Y_grid = np.meshgrid(x_grid, y_grid)
Z_grid = gauss_2d(X_grid, Y_grid, *result.x)

ax1 = fig.add_subplot(132, projection='3d')
ax1.plot_surface(X_grid, Y_grid, Z_grid, cmap='viridis', alpha=0.7)
ax1.scatter(X, Y, Z, c='red', s=50, depthshade=False)
ax1.set_title('3D-аппроксимация')

# 3. Линии уровня
ax2 = fig.add_subplot(133)
contour = ax2.contourf(X_grid, Y_grid, Z_grid, levels=25, cmap='viridis', alpha=0.9)
ax2.scatter(X, Y, c=Z, s=100, edgecolors='black', cmap='viridis')
ax2.set_title('Линии уровня и данные')
plt.colorbar(contour, ax=ax2)

plt.tight_layout()
plt.show()