import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('RGR1_A-10_X1-X4.csv')
columns = ['X1', 'X2', 'X3']
n = len(df)

plt.figure(figsize=(15, 5))

for i, col in enumerate(columns, 1):
    data = df[col].values
    
    S = np.std(data, ddof=0)
    
    # Правило Скотта
    h = 3.5 * S * (n ** (-1/3))
    
    k = int(np.ceil((data.max() - data.min()) / h))
    
    plt.subplot(1, 3, i)
    plt.hist(data, bins=k, edgecolor='black', alpha=0.7, color='skyblue')
    plt.title(f'{col} (Скотт: k={k})')
    plt.xlabel('x')
    plt.ylabel('Частота')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('docs/gists/hist_scott.png', dpi=300)
plt.show()