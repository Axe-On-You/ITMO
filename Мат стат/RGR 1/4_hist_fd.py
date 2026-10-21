import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('RGR1_A-10_X1-X4.csv')
columns = ['X1', 'X2', 'X3']
n = len(df)

plt.figure(figsize=(15, 5))

for i, col in enumerate(columns, 1):
    data = df[col].values
    
    # Межквартильный размах
    q75, q25 = np.percentile(data, [75, 25])
    iqr = q75 - q25
    
    # Правило Фридмана-Диакониса
    h = 2 * iqr * (n ** (-1/3))
    
    k = int(np.ceil((data.max() - data.min()) / h))
    
    plt.subplot(1, 3, i)
    plt.hist(data, bins=k, edgecolor='black', alpha=0.7, color='lightgreen')
    plt.title(f'{col} (Фридман-Диаконис: k={k})')
    plt.xlabel('x')
    plt.ylabel('Частота')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('docs/gists/hist_fd.png', dpi=300)
plt.show()