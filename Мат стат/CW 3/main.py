import pandas as pd
import numpy as np
from scipy import stats

# 1. Чтение данных из CSV файлов
df_x = pd.read_csv('variant_10_sample_X.csv')
df_y = pd.read_csv('variant_10_sample_Y.csv')

# Извлекаем данные из соответствующих столбцов
x = df_x['x_i'].values
y = df_y['y_j'].values

# Размеры выборок
m = len(x)
n = len(y)
alpha = 0.05

# 2. Выборочные средние
mean_x = np.mean(x)
mean_y = np.mean(y)

# 3. Несмещенные выборочные дисперсии (ddof=1 для деления на N-1)
var_x = np.var(x, ddof=1)
var_y = np.var(y, ddof=1)

# 4. Объединенная дисперсия
pooled_var = ((m - 1) * var_x + (n - 1) * var_y) / (m + n - 2)

# 5. Наблюдаемое значение T-критерия
t_stat = (mean_x - mean_y) / np.sqrt(pooled_var * (1/m + 1/n))

# 6. Степени свободы и критическое значение
k = m + n - 2
t_crit = stats.t.ppf(1 - alpha/2, k)

# Вывод результатов для переноса в LaTeX
print(f"--- Выборочные характеристики ---")
print(f"Выборочное среднее X (mu1): {mean_x:.4f}")
print(f"Выборочное среднее Y (mu2): {mean_y:.4f}")
print(f"Выборочная дисперсия X (sigma1^2): {var_x:.4f}")
print(f"Выборочная дисперсия Y (sigma2^2): {var_y:.4f}")
print(f"--- Проверка гипотезы ---")
print(f"Объединенная дисперсия: {pooled_var:.4f}")
print(f"Наблюдаемое значение T: {t_stat:.4f}")
print(f"Степени свободы (k): {k}")
print(f"Критическое значение t (двустороннее): {t_crit:.4f}")

print(f"--- Вывод ---")
if abs(t_stat) > t_crit:
    print(f"|{t_stat:.4f}| > {t_crit:.4f}. Гипотеза H0 отвергается (различия значимы).")
else:
    print(f"|{t_stat:.4f}| <= {t_crit:.4f}. Гипотеза H0 не отвергается (различия незначимы).")