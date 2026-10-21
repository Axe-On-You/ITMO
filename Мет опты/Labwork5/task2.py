import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

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

def paraboloid_2d(x, y, a, b, c, x0, y0, z0):
    return a*(x - x0)**2 + b*(y - y0)**2 + c*(x - x0)*(y - y0) + z0

loss_history = []

def loss_function_parab(params):
    a, b, c, x0, y0, z0 = params
    # Штраф за нарушение условия эллиптичности ab > c^2
    if a * b <= c**2:
        return 1e10
    
    predictions = paraboloid_2d(X, Y, a, b, c, x0, y0, z0)
    mse = 0.5 * np.mean((predictions - Z)**2)
    return mse

def callback_func(xk):
    loss_history.append(loss_function_parab(xk))

# Начальное приближение
max_idx = np.argmax(Z)
params_start = [-1.0, -1.0, 0.0, X[max_idx], Y[max_idx], Z[max_idx]]

# Границы для параметров (a и b должны быть отрицательными, чтобы ветви были вниз, так как ищем максимум)
bounds = [(-10, -0.01), (-10, -0.01), (-5, 5), (0, 6), (0, 6), (0, 10)]

result = minimize(loss_function_parab, params_start, method='L-BFGS-B', bounds=bounds, callback=callback_func)
a_opt, b_opt, c_opt, x0_opt, y0_opt, z0_opt = result.x

print("Аналитический вид модели:")
print(f"z = {a_opt:.4f}(x - {x0_opt:.4f})^2 + {b_opt:.4f}(y - {y0_opt:.4f})^2 + {c_opt:.4f}(x - {x0_opt:.4f})(y - {y0_opt:.4f}) + {z0_opt:.4f}")

predictions = paraboloid_2d(X, Y, *result.x)
residuals = predictions - Z
print("\nНевязки на каждом объекте:")
for i in range(len(X)):
    print(f"Точка {i}: реальное={Z[i]:.2f}, модель={predictions[i]:.2f}, невязка={residuals[i]:.4f}")

# Визуализация
fig = plt.figure(figsize=(18, 5))

# 1. Кривая обучения
ax1 = fig.add_subplot(131)
ax1.plot(range(len(loss_history)), loss_history, marker='o', color='b')
ax1.set_yscale('log')
ax1.set_title('Кривая обучения (Loss vs Iteration)')
ax1.set_xlabel('Итерация')
ax1.set_ylabel('Loss (MSE)')

# 2. Поверхность 3D
x_grid = np.linspace(0, 6, 50)
y_grid = np.linspace(0, 6, 50)
X_grid, Y_grid = np.meshgrid(x_grid, y_grid)
Z_grid = paraboloid_2d(X_grid, Y_grid, *result.x)

ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(X_grid, Y_grid, Z_grid, cmap='plasma', alpha=0.8)
ax2.scatter(X, Y, Z, c='red', s=50)
ax2.set_title('3D Эллиптический параболоид')

# 3. Линии уровня
ax3 = fig.add_subplot(133)
contour = ax3.contourf(X_grid, Y_grid, Z_grid, levels=20, cmap='plasma', alpha=0.9)
ax3.scatter(X, Y, c=Z, edgecolors='black', s=100, cmap='plasma')
ax3.contour(X_grid, Y_grid, Z_grid, levels=10, colors='white', alpha=0.5)
ax3.set_title('Линии уровня')
plt.colorbar(contour, ax=ax3)

plt.tight_layout()
plt.show()