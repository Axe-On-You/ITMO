import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

df = pd.read_csv('RGR1_A-10_X1-X4.csv')

# Настройки для шрифтов на графике
plt.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial', 'DejaVu Sans']})

results = []
for col in ['X1', 'X2', 'X3']:
    data = df[col]
    n = len(data)
    mean_x = data.mean()
    # Используем несмещенное СКО для порога x0, как в формуле
    std_unbiased = data.std(ddof=1) 
    x0 = mean_x + std_unbiased
    
    # Эмпирическая вероятность
    p_emp = (data > x0).sum() / n
    
    # Параметрическая вероятность (используем ММП оценки)
    if col == 'X1': # Экспоненциальное
        c = data.min()
        lam = 1 / (mean_x - c)
        p_par = np.exp(-lam * (x0 - c)) if x0 >= c else 1
    elif col == 'X2': # Нормальное
        std_mle = data.std(ddof=0) # ММП оценка СКО
        p_par = 1 - stats.norm.cdf(x0, loc=mean_x, scale=std_mle)
    elif col == 'X3': # Равномерное
        a = data.min()
        b = data.max()
        if x0 < a: p_par = 1
        elif x0 > b: p_par = 0
        else: p_par = (b - x0) / (b - a)
        
    results.append({
        'Выборка': col, 'mean': mean_x, 'std': std_unbiased, 
        'x0': x0, 'p_emp': p_emp, 'p_par': p_par
    })

# Вывод таблицы
print(f"{'Выборка':<8} | {'Среднее':<8} | {'СКО':<8} | {'x0':<8} | {'P_emp':<8} | {'P_par':<8}")
for r in results:
    print(f"{r['Выборка']:<8} | {r['mean']:<8.2f} | {r['std']:<8.2f} | {r['x0']:<8.2f} | {r['p_emp']:<8.4f} | {r['p_par']:<8.4f}")

# Построение графика
labels = ['X1 (Exp)', 'X2 (Normal)', 'X3 (Uniform)']
p_emp_vals = [r['p_emp'] for r in results]
p_par_vals = [r['p_par'] for r in results]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 5))
rects1 = ax.bar(x - width/2, p_emp_vals, width, label='Эмпирическая')
rects2 = ax.bar(x + width/2, p_par_vals, width, label='Параметрическая')

ax.set_ylabel('Вероятность P(X > x0)')
ax.set_title('Сравнение эмпирической и параметрической вероятностей')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig('prob_comparison.png', dpi=150)
print("\nГрафик сохранен как prob_comparison.png")