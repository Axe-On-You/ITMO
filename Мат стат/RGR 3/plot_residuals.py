"""
fig_residuals.png — Анализ остатков линейной модели
  Слева:  остатки eᵢ vs прогнозные значения ŷᵢ
  Справа: Q-Q график остатков
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import scipy.stats as stats

# ── данные ──────────────────────────────────────────────────────────────────
df = pd.read_csv("RGR3_A_10.csv")
x = df["x"].values
y = df["y"].values

# ── линейная модель ──────────────────────────────────────────────────────────
a, b   = 2.142160, 0.566164
y_hat  = a + b * x
resid  = y - y_hat

# проверка RSS
rss = np.sum(resid**2)
s2  = rss / (len(x) - 2)
s   = np.sqrt(s2)
print(f"RSS  = {rss:.6f}")
print(f"s²   = {s2:.6f}")
print(f"s    = {s:.6f}")

# ── субплоты ────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

# ── левый: остатки vs ŷ ──────────────────────────────────────────────────────
ax = axes[0]
ax.scatter(y_hat, resid,
           color="#2563EB", edgecolors="#1e3a8a", linewidths=0.4,
           s=40, alpha=0.80, zorder=3)
ax.axhline(0, color="#DC2626", linewidth=1.3, linestyle="--")

# полоса ±s
ax.axhline( s, color="#94a3b8", linewidth=0.8, linestyle=":")
ax.axhline(-s, color="#94a3b8", linewidth=0.8, linestyle=":")

ax.set_xlabel("Прогнозные значения $\\hat{y}$, ГГц", fontsize=11)
ax.set_ylabel("Остатки $e_i$, ГГц", fontsize=11)
ax.set_title("Остатки vs прогнозные значения", fontsize=12)
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.grid(True, which="major", linestyle="--", linewidth=0.5, alpha=0.6)
ax.grid(True, which="minor", linestyle=":",  linewidth=0.3, alpha=0.4)

# ── правый: Q-Q ─────────────────────────────────────────────────────────────
ax2 = axes[1]
(osm, osr), (slope, intercept, _) = stats.probplot(resid, dist="norm")
ax2.scatter(osm, osr,
            color="#2563EB", edgecolors="#1e3a8a", linewidths=0.4,
            s=40, alpha=0.80, zorder=3)
# теоретическая прямая
xq = np.array([osm.min(), osm.max()])
ax2.plot(xq, slope * xq + intercept, color="#DC2626", linewidth=1.5)

ax2.set_xlabel("Теоретические квантили", fontsize=11)
ax2.set_ylabel("Выборочные квантили остатков", fontsize=11)
ax2.set_title("Q-Q график остатков", fontsize=12)
ax2.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax2.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax2.grid(True, which="major", linestyle="--", linewidth=0.5, alpha=0.6)
ax2.grid(True, which="minor", linestyle=":",  linewidth=0.3, alpha=0.4)

plt.tight_layout()
plt.savefig("fig_residuals.png", dpi=150)
print("Сохранено: fig_residuals.png")
