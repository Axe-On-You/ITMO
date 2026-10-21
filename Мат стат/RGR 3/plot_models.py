"""
fig_models.png — Три регрессионные модели на фоне данных
  • Линейная:     y = 2.142160 + 0.566164 * x
  • Квадратичная: y = 2.956248 - 0.123285 * x + 0.131396 * x²
  • Степенная:    y = 2.562085 * x^0.361024
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ── данные ──────────────────────────────────────────────────────────────────
df = pd.read_csv("RGR3_A_10.csv")
x = df["x"].values
y = df["y"].values

X_STAR = 2.9672

# ── коэффициенты (из ключа) ──────────────────────────────────────────────────
a_lin, b_lin         = 2.142160, 0.566164
b0_q, b1_q, b2_q    = 2.956248, -0.123285, 0.131396
a_pow, b_pow         = 2.562085, 0.361024

# ── кривые ──────────────────────────────────────────────────────────────────
xc = np.linspace(x.min() - 0.05, x.max() + 0.05, 400)
y_lin  = a_lin + b_lin * xc
y_quad = b0_q + b1_q * xc + b2_q * xc**2
y_pow  = a_pow * xc**b_pow

# ── прогнозы при x* ─────────────────────────────────────────────────────────
yp_lin  = a_lin + b_lin * X_STAR
yp_quad = b0_q + b1_q * X_STAR + b2_q * X_STAR**2
yp_pow  = a_pow * X_STAR**b_pow

# ── график ──────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5.5))

ax.scatter(x, y,
           color="#94a3b8", edgecolors="#475569", linewidths=0.4,
           s=40, alpha=0.75, zorder=2, label="Наблюдения")

ax.plot(xc, y_lin,  color="#2563EB", linewidth=2.0, label=f"Линейная  ($R^2=0.437$)")
ax.plot(xc, y_quad, color="#16a34a", linewidth=2.0, label=f"Квадратичная  ($R^2=0.463$)")
ax.plot(xc, y_pow,  color="#dc2626", linewidth=2.0, linestyle="--",
        label=f"Степенная  ($R^2=0.384$)")

# пунктир x*
ax.axvline(X_STAR, color="#7c3aed", linestyle=":", linewidth=1.4,
           label=f"$x^* = {X_STAR}$ ГГц")

# точки прогноза
for yp, color in [(yp_lin, "#2563EB"), (yp_quad, "#16a34a"), (yp_pow, "#dc2626")]:
    ax.scatter(X_STAR, yp, color=color, marker="D", s=55, zorder=5)

# оформление
ax.set_xlabel("Базовая частота $x$, ГГц", fontsize=12)
ax.set_ylabel("Boost-частота $y$, ГГц", fontsize=12)
ax.set_title("Три регрессионные модели на фоне исходных данных", fontsize=13)
ax.legend(fontsize=10, loc="upper left")
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.grid(True, which="major", linestyle="--", linewidth=0.5, alpha=0.6)
ax.grid(True, which="minor", linestyle=":",  linewidth=0.3, alpha=0.4)

plt.tight_layout()
plt.savefig("fig_models.png", dpi=150)
print(f"Линейная    ŷ(x*)={yp_lin:.4f}")
print(f"Квадратичная ŷ(x*)={yp_quad:.4f}")
print(f"Степенная   ŷ(x*)={yp_pow:.4f}")
print("Сохранено: fig_models.png")
