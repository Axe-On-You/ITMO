import pandas as pd
import numpy as np

# Загрузка данных
df = pd.read_csv('RGR1_A-10_X1-X4.csv')

def calculate_estimates(data, name):
    n = len(data)
    mean_x = data.mean()
    s_std = data.std(ddof=0) # Смещенное СКО (как в ММП)
    min_x = data.min()
    max_x = data.max()

    results = {}

    if name == 'X1':  # Exp(lambda, c)
        # Метод моментов
        results['lambda_mm'] = 1 / s_std
        results['c_mm'] = mean_x - s_std
        # ММП
        results['c_ml'] = min_x
        results['lambda_ml'] = 1 / (mean_x - min_x)
        
    elif name == 'X2':  # N(a, sigma)
        # Метод моментов
        results['a_mm'] = mean_x
        results['sigma_mm'] = s_std
        # ММП
        results['a_ml'] = mean_x
        results['sigma_ml'] = s_std
        
    elif name == 'X3':  # U(a, b)
        # Метод моментов
        results['a_mm'] = mean_x - np.sqrt(3) * s_std
        results['b_mm'] = mean_x + np.sqrt(3) * s_std
        # ММП
        results['a_ml'] = min_x
        results['b_ml'] = max_x

    return results

print(f"{'Выборка':<8} | {'Параметр':<10} | {'Оценка ММ':<12} | {'Оценка ММП':<12} | {'Абс. расх.':<12}")
print("-" * 65)

for col in ['X1', 'X2', 'X3']:
    est = calculate_estimates(df[col], col)
    
    if col == 'X1':
        p1, p2 = 'lambda', 'c'
        m1_mm, m1_ml = est['lambda_mm'], est['lambda_ml']
        m2_mm, m2_ml = est['c_mm'], est['c_ml']
    elif col == 'X2':
        p1, p2 = 'a', 'sigma'
        m1_mm, m1_ml = est['a_mm'], est['a_ml']
        m2_mm, m2_ml = est['sigma_mm'], est['sigma_ml']
    else: # X3
        p1, p2 = 'a', 'b'
        m1_mm, m1_ml = est['a_mm'], est['a_ml']
        m2_mm, m2_ml = est['b_mm'], est['b_ml']

    diff1 = abs(m1_mm - m1_ml)
    diff2 = abs(m2_mm - m2_ml)

    print(f"{col:<8} | {p1:<10} | {m1_mm:<12.4f} | {m1_ml:<12.4f} | {diff1:<12.4e}")
    print(f"{'':<8} | {p2:<10} | {m2_mm:<12.4f} | {m2_ml:<12.4f} | {diff2:<12.4e}")
    print("-" * 65)