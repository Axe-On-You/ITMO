import pandas as pd

df = pd.read_csv('RGR1_A-10_X1-X4.csv')
columns = ['X1', 'X2', 'X3']

print("=== Вариационные ряды ===")
for col in columns:
    # Сортировка данных по возрастанию
    var_series = df[col].sort_values().reset_index(drop=True)
    
    print(f"\nСтолбец {col}:")
    print(f"Минимум: {var_series.iloc[0]}, Максимум: {var_series.iloc[-1]}")
    print(f"Первые 5 элементов:\n{var_series.head()}")
    print(f"Последние 5 элементов:\n{var_series.tail()}")
    
    # var_series.to_csv(f'var_series_{col}.txt', index=False, header=False)