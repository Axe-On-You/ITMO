import math

# === 1. ЦЕЛЕВАЯ ФУНКЦИЯ И ГРАДИЕНТ ===
def f(x):
    x1, x2 = x
    return 4*x1**2 + 3*x1*x2 + 5*x2**2 + 2*x1 - 17*x2 + 18

def grad_f(x):
    x1, x2 = x
    g1 = 8*x1 + 3*x2 + 2
    g2 = 3*x1 + 10*x2 - 17
    return [g1, g2]

# Вспомогательная функция для проверки сходимости по x
def vec_max_abs_diff_2(v1, v2):
    return max(abs(v1[0] - v2[0]), abs(v1[1] - v2[1]))

# Универсальный метод одномерного поиска (Золотое сечение)
def golden_section_search(func, a, b, eps=1e-6):
    phi = (1 + math.sqrt(5)) / 2
    res_phi = 2 - phi
    
    x1 = a + res_phi * (b - a)
    x2 = b - res_phi * (b - a)
    f1, f2 = func(x1), func(x2)
    
    while abs(b - a) > eps:
        if f1 < f2:
            b, x2, f2 = x2, x1, f1
            x1 = a + res_phi * (b - a)
            f1 = func(x1)
        else:
            a, x1, f1 = x1, x2, f2
            x2 = b - res_phi * (b - a)
            f2 = func(x2)
            
    return (a + b) / 2


# === 2. МЕТОДЫ ОПТИМИЗАЦИИ ===

# 2.1 Метод покоординатного спуска
def coordinate_descent(x0, eps, max_iter):
    x = x0.copy()
    history_x, history_f = [x.copy()], [f(x)]
    
    for _ in range(max_iter):
        x_old = x.copy()
        f_old = f(x_old)
        
        # Минимизация по x1 (ищем в окрестности текущей точки)
        def f_x1(val): return f([val, x[1]])
        x[0] = golden_section_search(f_x1, x[0] - 10, x[0] + 10, eps)
        
        # Минимизация по x2
        def f_x2(val): return f([x[0], val])
        x[1] = golden_section_search(f_x2, x[1] - 10, x[1] + 10, eps)
        
        history_x.append(x.copy())
        history_f.append(f(x))
        
        # Критерий останова
        if vec_max_abs_diff_2(x, x_old) < eps and abs(f(x) - f_old) < eps:
            break
            
    return x, history_x, history_f

# 2.2 Метод градиентного спуска (с постоянным шагом)
def gradient_descent(x0, eps, lambda_step, max_iter):
    x = x0.copy()
    history_x, history_f = [x.copy()], [f(x)]
    
    for _ in range(max_iter):
        grad = grad_f(x)
        grad_norm = math.sqrt(grad[0]**2 + grad[1]**2)
        
        if grad_norm < eps:
            break
            
        x[0] -= lambda_step * grad[0]
        x[1] -= lambda_step * grad[1]
        
        history_x.append(x.copy())
        history_f.append(f(x))
            
    return x, history_x, history_f

# 2.3 Метод наискорейшего спуска
def steepest_descent(x0, eps, max_iter):
    x = x0.copy()
    history_x, history_f = [x.copy()], [f(x)]
    
    for _ in range(max_iter):
        grad = grad_f(x)
        grad_norm = math.sqrt(grad[0]**2 + grad[1]**2)
        
        if grad_norm < eps:
            break
            
        # Ищем оптимальный шаг h
        def f_h(h): return f([x[0] - h * grad[0], x[1] - h * grad[1]])
        h_opt = golden_section_search(f_h, 0, 2, eps)
        
        x[0] -= h_opt * grad[0]
        x[1] -= h_opt * grad[1]
        
        history_x.append(x.copy())
        history_f.append(f(x))
            
    return x, history_x, history_f


# === 3. ЗАПУСК И ВЫВОД РЕЗУЛЬТАТОВ ===
if __name__ == "__main__":
    max_iter = 1000
    x_start = [2.0, -3.0]
    epsilon = 0.0001
    lambda_step = 0.05

    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №4. ВАРИАНТ 2")
    print(f"Функция: 4*x1^2 + 3*x1*x2 + 5*x2^2 + 2*x1 - 17*x2 + 18")
    print(f"Начальное приближение: {x_start}, eps = {epsilon}")
    print("=" * 60)

    # 1. Покоординатный
    x_opt, hist_x, hist_f = coordinate_descent(x_start, epsilon, max_iter)
    print("\n[1] МЕТОД ПОКООРДИНАТНОГО СПУСКА")
    print(f"Точка минимума: x* = [{x_opt[0]:.6f}, {x_opt[1]:.6f}]")
    print(f"f(x*) = {f(x_opt):.6f} | Итераций: {len(hist_f) - 1}")

    # 2. Градиентный
    x_opt, hist_x, hist_f = gradient_descent(x_start, epsilon, lambda_step, max_iter)
    print(f"\n[2] МЕТОД ГРАДИЕНТНОГО СПУСКА (λ = {lambda_step})")
    print(f"Точка минимума: x* = [{x_opt[0]:.6f}, {x_opt[1]:.6f}]")
    print(f"f(x*) = {f(x_opt):.6f} | Итераций: {len(hist_f) - 1}")

    # 3. Наискорейший
    x_opt, hist_x, hist_f = steepest_descent(x_start, epsilon, max_iter)
    print("\n[3] МЕТОД НАИСКОРЕЙШЕГО СПУСКА")
    print(f"Точка минимума: x* = [{x_opt[0]:.6f}, {x_opt[1]:.6f}]")
    print(f"f(x*) = {f(x_opt):.6f} | Итераций: {len(hist_f) - 1}")
    print("-" * 60)