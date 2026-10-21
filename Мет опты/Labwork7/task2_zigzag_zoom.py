import numpy as np
import matplotlib.pyplot as plt

# =========================
# ФУНКЦИЯ И ГРАДИЕНТ
# =========================

def objective(x, y):
    return 1e-2 * (8*x**2 + 2*x*y + 9*x + 2*y + 1)

def grad_objective(x, y):
    df_dx = 1e-2 * (16*x + 2*y + 9)
    df_dy = 1e-2 * (2*x + 2)
    return np.array([df_dx, df_dy])

# =========================
# ADAGRAD
# =========================

def run_adagrad(x0, y0, alpha, n_iter, eps_num=1e-8):

    params = np.array([x0, y0], dtype=float)

    G = np.zeros_like(params)

    traj = [params.copy()]

    for _ in range(n_iter):

        g = grad_objective(params[0], params[1])

        # Накопление квадратов градиентов
        G += g**2

        # Обновление параметров
        params -= alpha * g / (np.sqrt(G) + eps_num)

        traj.append(params.copy())

    return np.array(traj)

# =========================
# НАСТРОЙКИ
# =========================

x0, y0 = -10.0, 2.4

alpha_zigzag = 7.0

n_iter = 25

traj_zigzag = run_adagrad(
    x0,
    y0,
    alpha_zigzag,
    n_iter
)

# =========================
# СЕТКА ДЛЯ ЛИНИЙ УРОВНЯ
# =========================

x_arr = np.linspace(-12, 6, 600)
y_arr = np.linspace(-10, 8, 600)

X, Y = np.meshgrid(x_arr, y_arr)

Z = objective(X, Y)

# =========================
# ГРАФИК
# =========================

fig, ax = plt.subplots(figsize=(10, 8))

cf = ax.contourf(
    X,
    Y,
    Z,
    levels=80,
    cmap='RdYlGn_r'
)

ax.contour(
    X,
    Y,
    Z,
    levels=80,
    colors='black',
    linewidths=0.3,
    alpha=0.35
)

fig.colorbar(cf, ax=ax, label='$f(x,y)$')

# Траектория zigzag
ax.plot(
    traj_zigzag[:, 0],
    traj_zigzag[:, 1],
    'mo--',
    linewidth=2.5,
    markersize=5,
    label='Adagrad zigzag'
)

# Начальная точка
ax.plot(
    x0,
    y0,
    'co',
    markersize=10,
    label='Начальная точка'
)

# Седловая точка
ax.plot(
    -1,
    3.5,
    'ks',
    markersize=10,
    label='Седловая точка'
)

ax.set_xlim(-12, 6)
ax.set_ylim(-10, 8)

ax.set_xlabel('$x$', fontsize=13)
ax.set_ylabel('$y$', fontsize=13)

ax.set_title(
    'Пилообразная траектория Adagrad при $\\alpha = 7.0$',
    fontsize=14
)

ax.legend(fontsize=10)

plt.tight_layout()

plt.savefig(
    'task2_zigzag_zoom.png',
    dpi=250
)

plt.show()