import pandas as pd
import numpy as np

# Загрузка данных
df = pd.read_csv('RGR1_A-10_X1-X4.csv')
columns = ['X1', 'X2', 'X3']

print("=== Числовые характеристики (Пункт 4.1.4) ===")

for col in columns:
    data = df[col].dropna().values
    
    # Выборочное среднее
    mean_val = np.mean(data)
    
    # Дисперсии
    var_biased = np.var(data, ddof=0)     # S^2 (смещённая)
    var_unbiased = np.var(data, ddof=1)   # \hat{\sigma}^2 (несмещённая)
    
    # Стандартные отклонения
    std_biased = np.std(data, ddof=0)     # S
    std_unbiased = np.std(data, ddof=1)   # \hat{\sigma}
    
    # Медиана
    median_val = np.median(data)          # m_e
    
    # Квартили
    q1, q2, q3 = np.percentile(data, [25, 50, 75])
    
    print(f"\n--- Столбец {col} ---")
    print(f"Выборочное среднее (\\overline{{x}}): {mean_val:.4f}")
    print(f"Смещённая дисперсия (S^2): {var_biased:.4f}")
    print(f"Несмещённая дисперсия (\\hat{{\\sigma}}^2): {var_unbiased:.4f}")
    print(f"Смещённое ст. отклонение (S): {std_biased:.4f}")
    print(f"Несмещённое ст. отклонение (\\hat{{\\sigma}}): {std_unbiased:.4f}")
    print(f"Медиана (m_e): {median_val:.4f}")
    print(f"Квартили:")
    print(f"  Q1 (25% квантиль): {q1:.4f}")
    print(f"  Q2 (50% квантиль / медиана): {q2:.4f}")
    print(f"  Q3 (75% квантиль): {q3:.4f}")