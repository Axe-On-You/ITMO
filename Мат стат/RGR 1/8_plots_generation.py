import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

df = pd.read_csv('RGR1_A-10_X1-X4.csv')

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Liberation Sans', 'DejaVu Sans'],
    'axes.unicode_minus': False,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10
})

# Функция для генерации графиков плотности с динамическим расчетом оценок
def plot_hist_and_fits(data, col_name, dist_type):
    plt.figure(figsize=(10, 6))
    
    # Базовые статистики для расчета оценок
    mean_x = data.mean()
    s_std = data.std(ddof=0)
    min_x = data.min()
    max_x = data.max()
    
    # Строим нормированную гистограмму
    plt.hist(data, bins=15, density=True, alpha=0.6, color='gray', edgecolor='black', label='Гистограмма данных')
    
    # Создаем ось X для графиков плотности
    x = np.linspace(data.min() - (data.max()-data.min())*0.1, data.max() + (data.max()-data.min())*0.1, 1000)
    
    if dist_type == 'exp': # Shifted Exponential (X1)
        # Оценки
        lambda_mm, c_mm = 1 / s_std, mean_x - s_std
        c_ml, lambda_ml = min_x, 1 / (mean_x - min_x)
        
        pdf_mm = st.expon.pdf(x, loc=c_mm, scale=1/lambda_mm)
        pdf_ml = st.expon.pdf(x, loc=c_ml, scale=1/lambda_ml)
        dist_label = f'Экспоненциальное ($Exp_{{\\lambda, c}}$)'
        
        plt.plot(x, pdf_mm, 'b--', lw=2, label='Плотность (Метод Моментов)')
        plt.plot(x, pdf_ml, 'r-', lw=2, label='Плотность (ММП)')
        
    elif dist_type == 'norm': # Normal (X2)
        # Оценки (совпадают)
        a_val, sigma_val = mean_x, s_std
        
        pdf_val = st.norm.pdf(x, loc=a_val, scale=sigma_val)
        dist_label = f'Нормальное ($N_{{a, \\sigma}}$)'
        
        plt.plot(x, pdf_val, 'r-', lw=2.5, label='Плотность (ММ и ММП совпадают)')
        
    elif dist_type == 'uniform': # Uniform (X3)
        # Оценки
        a_mm, b_mm = mean_x - np.sqrt(3) * s_std, mean_x + np.sqrt(3) * s_std
        a_ml, b_ml = min_x, max_x
        
        pdf_mm = st.uniform.pdf(x, loc=a_mm, scale=(b_mm - a_mm))
        pdf_ml = st.uniform.pdf(x, loc=a_ml, scale=(b_ml - a_ml))
        dist_label = f'Равномерное ($U_{{a, b}}$)'
        
        plt.plot(x, pdf_mm, 'b--', lw=2, label='Плотность (Метод Моментов)')
        plt.plot(x, pdf_ml, 'r-', lw=2, label='Плотность (ММП)')

    plt.title(f'Выборка {col_name}: Сравнение гистограммы и оценок\nРаспределение: {dist_label}')
    plt.xlabel('Значение')
    plt.ylabel('Плотность')
    plt.legend()
    plt.grid(axis='y', alpha=0.5, linestyle='--')
    
    filename = f'fit_comparison_{col_name}.png'
    plt.savefig(filename, dpi=150)
    print(f'Создан файл: {filename}')
    plt.close()

# Функция для генерации диаграмм размаха
def plot_boxplot(data, col_name):
    plt.figure(figsize=(6, 8))
    
    plt.boxplot(data, vert=True, patch_artist=True,
                boxprops=dict(facecolor='lightblue', color='black'),
                capprops=dict(color='black'),
                whiskerprops=dict(color='black'),
                flierprops=dict(marker='o', markerfacecolor='red', markersize=6, linestyle='none'),
                medianprops=dict(color='darkblue', linewidth=2))
    
    plt.title(f'Выборка {col_name}: Диаграмма размаха («ящик с усами»)')
    plt.ylabel('Значение')
    plt.grid(axis='y', alpha=0.5, linestyle='--')
    
    filename = f'boxplot_{col_name}.png'
    plt.savefig(filename, dpi=150)
    print(f'Создан файл: {filename}')
    plt.close()

# Генерация графиков
print("=== Генерация 6 новых графиков (пункт 4.3) ===")

# X1 - Exp
plot_hist_and_fits(df['X1'], 'X1', 'exp')
plot_boxplot(df['X1'], 'X1')

# X2 - Normal
plot_hist_and_fits(df['X2'], 'X2', 'norm')
plot_boxplot(df['X2'], 'X2')

# X3 - Uniform
plot_hist_and_fits(df['X3'], 'X3', 'uniform')
plot_boxplot(df['X3'], 'X3')

print("=== Готово ===")