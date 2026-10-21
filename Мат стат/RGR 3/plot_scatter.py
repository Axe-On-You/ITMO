"""
fig_scatter.png — Диаграмма рассеяния с пунктиром x* = 2.9672
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ── данные ──────────────────────────────────────────────────────────────────
df = pd.read_csv("RGR3_A_10.csv")
x = df["x"].values
y = df["y"].values

X_STAR = 2.9672   # 108% от среднего

# ── график ──────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(x, y,
           color="#2563EB", edgecolors="#1e3a8a", linewidths=0.5,
           s=45, alpha=0.85, zorder=3, label="Наблюдения")

ax.axvline(X_STAR, color="#DC2626", linestyle="--", linewidth=1.4,
           label=f"$x^* = {X_STAR}$ ГГц")

# оформление
ax.set_xlabel("Базовая частота $x$, ГГц", fontsize=12)
ax.set_ylabel("Boost-частота $y$, ГГц", fontsize=12)
ax.set_title("Диаграмма рассеяния: boost-частота vs базовая частота", fontsize=13)
ax.legend(fontsize=11)
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.grid(True, which="major", linestyle="--", linewidth=0.5, alpha=0.6)
ax.grid(True, which="minor", linestyle=":",  linewidth=0.3, alpha=0.4)

plt.tight_layout()
plt.savefig("fig_scatter.png", dpi=150)
print("Сохранено: fig_scatter.png")
