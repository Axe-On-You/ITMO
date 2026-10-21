import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Настройка шрифтов для графиков
plt.rcParams['font.family'] = 'DejaVu Sans' # Чтобы кириллица отображалась корректно

# ==========================================
# Задание 1. Критерий Манна-Уитни
# ==========================================
data_old = np.array([62, 64, 66, 67, 69, 71, 73, 74, 76, 78])
data_new = np.array([58, 60, 61, 63, 65, 68, 70, 72, 75, 77])

# Проверка расчетов (должно быть U=35, p=0.2799)
stat_u, p_value_mw = stats.mannwhitneyu(data_old, data_new, alternative='two-sided')
print(f"Задание 1: U-статистика = {stat_u}, p-value = {p_value_mw:.4f}")

fig1, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# 1. Эмпирические функции распределения
x_old = np.sort(data_old)
y_old = np.arange(1, len(x_old) + 1) / len(x_old)
x_new = np.sort(data_new)
y_new = np.arange(1, len(x_new) + 1) / len(x_new)

ax1.step(np.concatenate(([x_old[0]-2], x_old)), np.concatenate(([0], y_old)), where='post', label='старые')
ax1.step(np.concatenate(([x_new[0]-2], x_new)), np.concatenate(([0], y_new)), where='post', label='новые')
ax1.set_title('Эмпирические функции распределения')
ax1.set_xlabel('Время обработки заявки, сек')
ax1.set_ylabel('F(x)')
ax1.set_ylim(0, 1.05)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend()

# 2. Гистограммы распределения
bins = np.arange(55, 85, 2.5) 
ax2.hist(data_old, bins=bins, alpha=0.5, label='старые', density=True, edgecolor='white')
ax2.hist(data_new, bins=bins, alpha=0.5, label='новые', density=True, edgecolor='white')
ax2.set_title('Гистограммы распределения')
ax2.set_xlabel('Время обработки заявки, сек')
ax2.set_ylabel('Плотность')
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend()

plt.tight_layout()
plt.savefig('task1_plot.png')

# ==========================================
# Задание 2. Критерий согласия Пирсона
# ==========================================
# Данные из методички (60 наблюдений)
data_exp = np.array([
    3.8, 24.1, 10.5, 7.3, 1.4, 1.4, 0.5, 16.1, 7.4, 9.9,
    0.2, 28.0, 14.3, 1.9, 1.6, 1.6, 2.9, 6.0, 4.5, 2.8,
    7.6, 1.2, 2.8, 3.7, 4.9, 12.3, 1.8, 5.8, 7.2, 0.4,
    7.5, 1.5, 0.5, 23.8, 27.0, 13.2, 2.9, 0.8, 9.2, 4.6,
    1.0, 5.5, 0.3, 19.2, 2.4, 8.7, 3.0, 5.9, 6.3, 1.6,
    27.9, 11.9, 22.4, 18.0, 7.3, 20.4, 0.7, 1.7, 0.4, 3.1
])

n = len(data_exp)
mean_val = np.mean(data_exp)
lmbda = 1 / mean_val

# Расчет границ интервалов (5 интервалов с равной вероятностью p=0.2)
k = 5
p_expected = 1/k
quantiles = [0.2, 0.4, 0.6, 0.8]
# Границы: -ln(1-p)/lambda
borders = [-np.log(1 - p) / lmbda for p in quantiles]
borders = [0] + borders + [np.inf]

# Наблюдаемые частоты
observed_freq, _ = np.histogram(data_exp, bins=borders)
expected_freq = np.full(k, n * p_expected)

# Статистика хи-квадрат
chi2_stat = np.sum((observed_freq - expected_freq)**2 / expected_freq)
df = k - 1 - 1 # k интервалов - 1 параметр - 1
p_value_chi2 = 1 - stats.chi2.cdf(chi2_stat, df)

print("\n--- Результаты Задания 2 ---")
print(f"Среднее: {mean_val:.4f}, lambda: {lmbda:.4f}")
print(f"Наблюдаемые частоты: {observed_freq}")
print(f"Ожидаемые частоты: {expected_freq}")
print(f"Хи-квадрат: {chi2_stat:.4f}, p-value: {p_value_chi2:.4f}")

# Построение графиков для Задания 2
fig2, (ax3, ax4) = plt.subplots(2, 1, figsize=(10, 6))

# Эмпирическая и теоретическая функции распределения
x_sorted = np.sort(data_exp)
y_ecdf = np.arange(1, n + 1) / n
x_theor = np.linspace(0, max(data_exp) + 2, 100)
y_theor_cdf = stats.expon.cdf(x_theor, scale=1/lmbda)

ax3.step(x_sorted, y_ecdf, label='Эмпирическая F(x)', where='post')
ax3.plot(x_theor, y_theor_cdf, label='Теоретическая F(x)', color='darkorange', alpha=0.8)
ax3.set_title('Функция распределения')
ax3.set_xlabel('Время между заявками, мин')
ax3.set_ylabel('F(x)')
ax3.grid(True, linestyle='--', alpha=0.5)
ax3.legend()

# Гистограмма и теоретическая плотность
ax4.hist(data_exp, bins=12, density=True, alpha=0.6, label='Гистограмма')
y_theor_pdf = stats.expon.pdf(x_theor, scale=1/lmbda)
ax4.plot(x_theor, y_theor_pdf, label='Теоретическая плотность', color='darkorange', alpha=0.8)
ax4.set_title('Гистограмма и теоретическая плотность')
ax4.set_xlabel('Время между заявками, мин')
ax4.set_ylabel('Плотность')
ax4.grid(True, linestyle='--', alpha=0.5)
ax4.legend()

plt.tight_layout()
plt.savefig('task2_plot.png')
print("График для задания 2 сохранен как 'task2_plot.png'")