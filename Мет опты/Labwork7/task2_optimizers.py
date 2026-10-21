import numpy as np
import matplotlib.pyplot as plt
import torch

from functions import (
    objective,
    grad_objective,
    X,
    Y,
    Z,
    SADDLE_POINT,
    GLOBAL_MIN
)


# =========================================================
# SGD (обычный gradient descent)
# =========================================================

alpha_sgd = 0.35

eps_function = 1e-6
eps_grad = 1e-4

x0, y0 = -10.0, 2.4

x, y = x0, y0

traj_gd = [(x, y)]

n_iter_gd = 0


for i in range(500):

    g = grad_objective(x, y)

    xn = x - alpha_sgd * g[0]
    yn = y - alpha_sgd * g[1]

    n_iter_gd = i + 1

    function_diff = abs(
        objective(xn, yn) - objective(x, y)
    )

    grad_norm = np.linalg.norm(g)

    if function_diff < eps_function and grad_norm < eps_grad:

        x, y = xn, yn

        traj_gd.append((x, y))

        break

    x, y = xn, yn

    traj_gd.append((x, y))


traj_gd = np.array(traj_gd)

print('=' * 60)
print('SGD')
print('=' * 60)

print(f'Итераций: {n_iter_gd}')
print(f'Конечная точка: ({x:.6f}, {y:.6f})')

print(f'Значение функции: {objective(x, y):.10f}')

print(f'Норма градиента: {np.linalg.norm(grad_objective(x, y)):.10f}')


# =========================================================
# Собственная реализация Adagrad
# =========================================================

def run_adagrad(x0, y0, alpha, n_iter, eps_num=1e-8):

    params = np.array([x0, y0], dtype=float)

    G = np.zeros_like(params)

    traj = [params.copy()]

    for _ in range(n_iter):

        g = grad_objective(params[0], params[1])

        G += g**2

        params -= alpha * g / (np.sqrt(G) + eps_num)

        traj.append(params.copy())

    return np.array(traj)


alpha_adagrad = 2.0

traj_ada = run_adagrad(
    x0,
    y0,
    alpha_adagrad,
    n_iter_gd
)

print('\n' + '=' * 60)
print('CUSTOM ADAGRAD')
print('=' * 60)

print(
    f'Конечная точка: '
    f'({traj_ada[-1,0]:.6f}, {traj_ada[-1,1]:.6f})'
)

print(
    f'Значение функции: '
    f'{objective(traj_ada[-1,0], traj_ada[-1,1]):.10f}'
)


# =========================================================
# Adagrad с большим learning rate (zigzag)
# =========================================================

alpha_zigzag = 7.0

traj_zigzag = run_adagrad(
    x0,
    y0,
    alpha_zigzag,
    n_iter_gd
)


# =========================================================
# Реализация PyTorch Adagrad
# =========================================================

def objective_torch(sol):

    x, y = sol[0], sol[1]

    return 1e-2 * (
        8 * x**2 +
        2 * x * y +
        9 * x +
        2 * y +
        1
    )


solution = torch.tensor(
    [-10.0, 2.4],
    requires_grad=True
)

optimizer = torch.optim.Adagrad(
    [solution],
    lr=alpha_adagrad
)

trace = []


for _ in range(n_iter_gd):

    optimizer.zero_grad()

    score = objective_torch(solution)

    score.backward()

    trace.append(
        solution.clone().detach().numpy()
    )

    optimizer.step()


traj_pt = np.array(trace)

print('\n' + '=' * 60)
print('PYTORCH ADAGRAD')
print('=' * 60)

print(
    f'Конечная точка: '
    f'({traj_pt[-1,0]:.6f}, {traj_pt[-1,1]:.6f})'
)

print(
    f'Значение функции: '
    f'{objective(traj_pt[-1,0], traj_pt[-1,1]):.10f}'
)


# =========================================================
# ВИЗУАЛИЗАЦИЯ ТРАЕКТОРИЙ
# =========================================================

fig, ax = plt.subplots(figsize=(11, 8))

cf = ax.contourf(
    X,
    Y,
    Z,
    levels=60,
    cmap='RdYlGn_r'
)

ax.contour(
    X,
    Y,
    Z,
    levels=60,
    colors='black',
    linewidths=0.3,
    alpha=0.35
)

fig.colorbar(cf, ax=ax)


# SGD
ax.plot(
    traj_gd[:, 0],
    traj_gd[:, 1],
    'wo-',
    linewidth=2,
    markersize=4,
    label='SGD'
)

# Adagrad smooth
ax.plot(
    traj_ada[:, 0],
    traj_ada[:, 1],
    'bo-',
    linewidth=2,
    markersize=4,
    label='Adagrad smooth'
)

# Adagrad zigzag
ax.plot(
    traj_zigzag[:, 0],
    traj_zigzag[:, 1],
    'mo--',
    linewidth=2,
    markersize=4,
    label='Adagrad zigzag'
)

# PyTorch
ax.plot(
    traj_pt[:, 0],
    traj_pt[:, 1],
    'k--',
    linewidth=2,
    label='PyTorch Adagrad'
)

# Седловая точка
ax.plot(
    SADDLE_POINT[0],
    SADDLE_POINT[1],
    'ks',
    markersize=10,
    label='Седловая точка'
)

# Глобальный минимум
ax.plot(
    GLOBAL_MIN[0],
    GLOBAL_MIN[1],
    'r*',
    markersize=15,
    label='Глобальный минимум'
)

ax.set_xlim(-15, 10)
ax.set_ylim(-55, 55)

ax.set_xlabel('$x$', fontsize=13)
ax.set_ylabel('$y$', fontsize=13)

ax.set_title(
    'Траектории SGD и Adagrad',
    fontsize=14
)

ax.legend(fontsize=10)

plt.tight_layout()

plt.savefig(
    'task2_trajectories.png',
    dpi=200
)

plt.show()