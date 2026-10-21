import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('RGR1_A-10_X1-X4.csv')
columns = ['X1', 'X2', 'X3']

plt.figure(figsize=(15, 5))

for i, col in enumerate(columns, 1):
    data = df[col].dropna().values
    n = len(data)
    
    # Сортировка для ЭФР
    x = np.sort(data)
    y = np.arange(1, n + 1) / n
    
    plt.subplot(1, 3, i)
    plt.step(x, y, where='post', color='b', linewidth=1.5)
    plt.title(f'ЭФР для {col}')
    plt.xlabel('x')
    plt.ylabel('Fn(x)')
    plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('docs/gists/ecdf_plots.png', dpi=300)
plt.show()