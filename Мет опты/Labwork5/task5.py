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

def rbf_network(x, y, c1x, c1y, c2x, c2y, sigma1, sigma2, w0, w1, w2):
    rbf1 = np.exp(-((x - c1x)**2 + (y - c1y)**2) / (2 * sigma1**2))
    rbf2 = np.exp(-((x - c2x)**2 + (y - c2y)**2) / (2 * sigma2**2))
    return w1 * rbf1 + w2 * rbf2 + w0

loss_history_rbf = []

def loss_function_rbf(params):
    c1x, c1y, c2x, c2y, sigma1, sigma2, w0, w1, w2 = params
    predictions = rbf_network(X, Y, *params)
    mse = 0.5 * np.mean((predictions - Z)**2)
    return mse

def callback_rbf(xk):
    loss_history_rbf.append(loss_function_rbf(xk))

# Начальное приближение (как в ручном задании)
params_start_rbf = [1.01, 1.07, 5.27, 5.03, 2.9, 2.9, 0.0, 0.1, -0.1]
bounds_rbf = [(0, 6), (0, 6), (0, 6), (0, 6), (0.1, 5), (0.1, 5), (-5, 5), (-10, 10), (-10, 10)]

result_rbf = minimize(loss_function_rbf, params_start_rbf, method='L-BFGS-B', bounds=bounds_rbf, callback=callback_rbf)
c1x_opt, c1y_opt, c2x_opt, c2y_opt, s1_opt, s2_opt, w0_opt, w1_opt, w2_opt = result_rbf.x

print("Аналитический вид RBF-модели:")
print(f"z = {w0_opt:.4f} + {w1_opt:.4f}*exp(-((x-{c1x_opt:.4f})^2 + (y-{c1y_opt:.4f})^2)/(2*{s1_opt:.4f}^2)) + {w2_opt:.4f}*exp(-((x-{c2x_opt:.4f})^2 + (y-{c2y_opt:.4f})^2)/(2*{s2_opt:.4f}^2))")

predictions_rbf = rbf_network(X, Y, *result_rbf.x)
residuals_rbf = predictions_rbf - Z
print("\nНевязки на каждом объекте (RBF):")
for i in range(len(X)):
    print(f"Точка {i}: реальное={Z[i]:.2f}, модель={predictions_rbf[i]:.2f}, невязка={residuals_rbf[i]:.4f}")

# Визуализация RBF
fig = plt.figure(figsize=(18, 5))

# 1. Кривая обучения
ax1 = fig.add_subplot(131)
ax1.plot(range(len(loss_history_rbf)), loss_history_rbf, marker='o', color='g')
ax1.set_yscale('log')
ax1.set_title('Кривая обучения RBF (Loss vs Iteration)')

# 2. Поверхность 3D
x_grid = np.linspace(0, 6, 50)
y_grid = np.linspace(0, 6, 50)
X_grid, Y_grid = np.meshgrid(x_grid, y_grid)
Z_grid = rbf_network(X_grid, Y_grid, *result_rbf.x)

ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(X_grid, Y_grid, Z_grid, cmap='viridis', alpha=0.8)
ax2.scatter(X, Y, Z, c='red', s=50)
ax2.set_title('3D RBF-сеть')

# 3. Линии уровня
ax3 = fig.add_subplot(133)
contour = ax3.contourf(X_grid, Y_grid, Z_grid, levels=20, cmap='viridis', alpha=0.9)
ax3.scatter(X, Y, c=Z, edgecolors='black', s=100, cmap='viridis')
# Отрисуем найденные центры звездочками
ax3.scatter([c1x_opt, c2x_opt], [c1y_opt, c2y_opt], marker='*', color='white', s=200, edgecolors='black')
ax3.contour(X_grid, Y_grid, Z_grid, levels=10, colors='white', alpha=0.5)
ax3.set_title('Линии уровня RBF')
plt.colorbar(contour, ax=ax3)

plt.tight_layout()
plt.show()