import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('RGR1_A-10_X1-X4.csv')
columns = ['X1', 'X2', 'X3']
n = len(df)

plt.figure(figsize=(15, 5))

# Правило Стерджеса (количество интервалов зависит только от n)
k = int(1 + np.floor(np.log2(n)))

for i, col in enumerate(columns, 1):
    data = df[col].values
    
    plt.subplot(1, 3, i)
    plt.hist(data, bins=k, edgecolor='black', alpha=0.7, color='salmon')
    plt.title(f'{col} (Стерджес: k={k})')
    plt.xlabel('x')
    plt.ylabel('Частота')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('docs/gists/hist_sturges.png', dpi=300)
plt.show()