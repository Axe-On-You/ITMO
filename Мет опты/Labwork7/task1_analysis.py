import matplotlib.pyplot as plt

from functions import (
    objective,
    X,
    Y,
    Z,
    SADDLE_POINT,
    GLOBAL_MIN
)


# ==========================================
# Построение линий уровня
# ==========================================

fig, ax = plt.subplots(figsize=(10, 8))

cf = ax.contourf(
    X,
    Y,
    Z,
    levels=60,
    cmap='RdYlGn_r'
)

fig.colorbar(cf, ax=ax, label='$f(x,y)$')

ax.contour(
    X,
    Y,
    Z,
    levels=60,
    colors='black',
    linewidths=0.3,
    alpha=0.35
)

# Седловая точка
ax.plot(
    SADDLE_POINT[0],
    SADDLE_POINT[1],
    'ko',
    markersize=9,
    label='Седловая точка'
)

# Глобальный минимум
ax.plot(
    GLOBAL_MIN[0],
    GLOBAL_MIN[1],
    'b*',
    markersize=14,
    label='Глобальный минимум'
)

ax.set_xlabel('$x$', fontsize=13)
ax.set_ylabel('$y$', fontsize=13)

ax.set_title(
    r'Линии уровня $f(x,y)=10^{-2}(8x^2+2xy+9x+2y+1)$',
    fontsize=13
)

ax.legend(fontsize=11)

plt.tight_layout()

plt.savefig('task1_contours.png', dpi=200)

plt.show()