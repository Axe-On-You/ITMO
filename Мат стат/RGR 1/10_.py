import pandas as pd
import numpy as np
import scipy.stats as stats

# Загрузка данных
df = pd.read_csv('RGR1_A-10_X1-X4.csv')
n = len(df)
alpha = 0.05 # Уровень значимости для ДИ 95%

print(f"{'Выборка':<8} | {'X_grp':<10} | {'S2_grp':<10} | {'CI Low':<10} | {'CI High':<10}")
print("-" * 60)

grouped_results = []

for col in ['X1', 'X2', 'X3']:
    data = df[col]
    
    # --- 4.5. Оценки по сгруппированной выборке ---
    # Используем правило Стерджеса для определения количества интервалов
    counts, bins = np.histogram(data, bins='sturges')
    m = len(counts)
    
    # Середины интервалов (X_k_hat)
    bin_centers = (bins[:-1] + bins[1:]) / 2
    
    # Формулы из методички (стр. 8)
    x_grp = (1/n) * np.sum(counts * bin_centers)
    s2_grp = (1/(n-1)) * np.sum(counts * (bin_centers - x_grp)**2)
    
    # --- 4.6. Доверительные интервалы (Асимптотический для EX) ---
    # Квантиль нормального распределения z(1 - alpha/2)
    z = stats.norm.ppf(1 - alpha/2)
    
    # Стандартная ошибка на основе несмещенного СКО исходной выборки
    std_x = data.std(ddof=1)
    mean_x = data.mean()
    
    margin_of_error = z * (std_x / np.sqrt(n))
    ci_low = mean_x - margin_of_error
    ci_high = mean_x + margin_of_error
    
    print(f"{col:<8} | {x_grp:<10.4f} | {s2_grp:<10.4f} | {ci_low:<10.4f} | {ci_high:<10.4f}")
    
    grouped_results.append({
        'col': col, 'x_grp': x_grp, 's2_grp': s2_grp, 
        'ci': (ci_low, ci_high), 'mean': mean_x
    })