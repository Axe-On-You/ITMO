import numpy as np
import pandas as pd
from scipy import stats

SIGMA_0_SQ = 63.53 
LAMBDA_0 = 0.109

def load_data(filename):
    # Учитываем, что разделитель ';' и числа с точкой
    df = pd.read_csv(filename, sep=';', decimal='.')
    return df['X1'].values, df['X2'].values, df['X3'].values, df['X4'].values

def test_equal_means(x1, x2):
    n1, n2 = len(x1), len(x2)
    m1, m2 = np.mean(x1), np.mean(x2)
    s1, s2 = np.var(x1, ddof=1), np.var(x2, ddof=1)
    
    # Объединенная оценка дисперсии
    sp2 = ((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2)
    
    # Статистика Стьюдента
    h = (m1 - m2) / np.sqrt(sp2 * (1/n1 + 1/n2))
    df = n1 + n2 - 2
    
    # Двусторонний p-value
    p = 2 * min(stats.t.cdf(h, df), 1 - stats.t.cdf(h, df))
    
    print("X1 и X2: параметрический критерий")
    print(f"  x̄1 = {m1:.2f}, x̄2 = {m2:.2f}")
    print(f"  s1² = {s1:.2f}, s2² = {s2:.2f}")
    print(f"  s̄² = {sp2:.2f}")
    print(f"  h_набл = {h:.3f}, p-value ≈ {p:.4f}")
    print(f"  Решение при α = 0.05: {'H0 отвергается.' if p < 0.05 else 'нет оснований отвергнуть H0.'}\n")

def test_mann_whitney(x1, x2):
    res = stats.mannwhitneyu(x1, x2, alternative='two-sided', method='asymptotic', use_continuity=False)
    
    n1, n2 = len(x1), len(x2)
    U1 = res.statistic
    
    muU = n1 * n2 / 2
    varU = (n1 * n2 * (n1 + n2 + 1)) / 12
    z = (U1 - muU) / np.sqrt(varU)
    
    print("X1 и X2: непараметрический критерий Манна–Уитни")
    print(f"  U = {U1:.2f}, z ≈ {z:.3f}, p-value ≈ {res.pvalue:.4f}")
    print(f"  Решение при α = 0.05: {'H0 отвергается.' if res.pvalue < 0.05 else 'нет оснований отвергнуть H0.'}\n")

def test_variance(x3, sigma0_sq):
    n = len(x3)
    s2 = np.var(x3, ddof=1)
    h = (n - 1) * s2 / sigma0_sq
    df = n - 1
    
    # Двусторонний p-value для хи-квадрат
    cdf = stats.chi2.cdf(h, df)
    p = 2 * min(cdf, 1 - cdf)
    
    print("X3: проверка гипотезы о дисперсии нормального распределения")
    print(f"  H0: σ² = {sigma0_sq:.2f}")
    print(f"  s² = {s2:.2f}")
    print(f"  h_набл = {h:.3f}, p-value ≈ {p:.4f}")
    print(f"  Решение при α = 0.05: {'H0 отвергается.' if p < 0.05 else 'нет оснований отвергнуть H0.'}\n")

def test_pearson_exp(x4, lambda0):
    n = len(x4)
    # Разбиваем на 5 интервалов с равной вероятностью 0.2
    probs = [0.2, 0.2, 0.2, 0.2, 0.2]
    # Квантили экспоненциального распределения
    q = [-np.log(1 - p) / lambda0 for p in [0.2, 0.4, 0.6, 0.8]]
    
    obs = [0] * 5
    for v in x4:
        if v < q[0]: obs[0] += 1
        elif v < q[1]: obs[1] += 1
        elif v < q[2]: obs[2] += 1
        elif v < q[3]: obs[3] += 1
        else: obs[4] += 1
        
    exp = [n * p for p in probs]
    
    chi2 = sum(((o - e)**2) / e for o, e in zip(obs, exp))
    df = 4 # k=5 интервалов, s=0 оцененных параметров, k - s - 1 = 4
    p = 1 - stats.chi2.cdf(chi2, df)
    
    print("X4: критерий согласия Пирсона")
    print(f"  H0: X4 ~ Exp(λ0), λ0 = {lambda0:.3f}")
    print(f"  Наблюдаемые частоты: {obs}")
    print(f"  Ожидаемые частоты: {[round(e, 1) for e in exp]}")
    print(f"  χ²_набл = {chi2:.3f}, p-value ≈ {p:.4f}")
    print(f"  Решение при α = 0.05: {'H0 отвергается.' if p < 0.05 else 'нет оснований отвергнуть H0.'}\n")

if __name__ == "__main__":
    X1, X2, X3, X4 = load_data("RGR2_A-10_X1-X4.csv")
    
    print(f"Объем выборки n = {len(X1)}\n")
    
    test_equal_means(X1, X2)
    test_mann_whitney(X1, X2)
    test_variance(X3, SIGMA_0_SQ)
    test_pearson_exp(X4, LAMBDA_0)