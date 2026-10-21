import numpy as np
import matplotlib.pyplot as plt

# 1. Данные для полупроводникового образца
T_sem = np.array([307, 312, 317, 322, 327, 332, 337, 342, 347, 352, 357])
I_sem = np.array([1054, 1165, 1302, 1442, 1535, 1618, 1689, 1757, 1813, 1860, 1895]) # мкА
U_sem = np.array([0.886, 0.781, 0.667, 0.567, 0.462, 0.410, 0.350, 0.303, 0.250, 0.224, 0.193]) # В

R_sem = U_sem / (I_sem * 1e-6) # Ом
ln_R_sem = np.log(R_sem)
inv_T103 = 1000.0 / T_sem

# 2. Данные для металлического образца
T_met = np.array([355, 350, 345, 340, 335, 330, 325, 320, 315, 310, 307])
I_met = np.array([1026, 1043, 1057, 1063, 1076, 1083, 1096, 1108, 1119, 1131, 1138]) # мкА
U_met = np.array([1.365, 1.357, 1.347, 1.340, 1.330, 1.321, 1.313, 1.303, 1.294, 1.282, 1.273]) # В

R_met = (U_met / (I_met * 1e-6)) / 1000.0 # кОм
t_met = T_met - 273.15 # градусы Цельсия

print("Полупроводник R (Ом):", np.round(R_sem, 2))
print("Металл R (кОм):", np.round(R_met, 4))

# Построение графика для металла
plt.figure(figsize=(7, 4.5))
plt.plot(t_met, R_met, 'ro-', label='$R_M(t)$ эксперимент')
plt.xlabel(r'Температура $t$, $^\circ$C')
plt.ylabel('Сопротивление $R$, кОм')
plt.title('Зависимость сопротивления металла от температуры')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('metal_plot.png', dpi=300)
plt.close()

# Построение графика для полупроводника
plt.figure(figsize=(7, 4.5))
plt.plot(inv_T103, ln_R_sem, 'bo-', label=r'$\ln R(10^3/T)$ эксперимент')
plt.xlabel(r'Обратная температура $10^3/T$, K$^{-1}$')
plt.ylabel(r'Логарифм сопротивления $\ln R$')
plt.title(r'Зависимость $\ln R$ полупроводника от обратной температуры')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('semiconductor_plot.png', dpi=300)
plt.close()