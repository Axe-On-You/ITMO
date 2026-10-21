import random
import numpy as np
import itertools

# Матрица расстояний (Города 1-5, индексы 0-4)
distances = np.array([
    [0, 1, 6, 4, 2],
    [1, 0, 6, 10, 5],
    [6, 6, 0, 6, 5],
    [4, 10, 6, 0, 7],
    [2, 5, 5, 7, 0]
])

POPULATION_SIZE = 4
MUTATION_RATE = 0.01
GENERATIONS = 100
NUM_CITIES = len(distances)

# Вычисление целевой функции (длины замкнутого маршрута)
def calculate_fitness(route):
    total_dist = 0
    for i in range(NUM_CITIES):
        from_city = route[i]
        to_city = route[(i + 1) % NUM_CITIES]
        total_dist += distances[from_city][to_city]
    return total_dist

# Создание начальной случайной популяции
def create_population():
    population = []
    for _ in range(POPULATION_SIZE):
        route = list(range(NUM_CITIES))
        random.shuffle(route)
        population.append(route)
    return population

# Скрещивание (Order Crossover - OX1)
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(NUM_CITIES), 2))
    child = [-1] * NUM_CITIES
    child[start:end] = parent1[start:end]
    
    p2_idx = 0
    for i in range(NUM_CITIES):
        if child[i] == -1:
            while parent2[p2_idx] in child:
                p2_idx += 1
            child[i] = parent2[p2_idx]
    return child

# Мутация: перестановка двух случайных городов
def mutate(route):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(NUM_CITIES), 2)
        route[i], route[j] = route[j], route[i]
    return route

# Проверка оптимальности через полный перебор
def brute_force_optimal():
    cities = list(range(NUM_CITIES))
    best_dist = float('inf')
    best_route = None
    
    # Перебираем все возможные перестановки
    for p in itertools.permutations(cities):
        d = calculate_fitness(p)
        if d < best_dist:
            best_dist = d
            best_route = p
    return best_route, best_dist

def main():
    population = create_population()
    best_overall_route = None
    best_overall_dist = float('inf')

    print(f"{'Поколение':<12} | {'Лучший путь в популяции':<25} | {'Дистанция':<10}")
    print("-" * 55)

    for gen in range(1, GENERATIONS + 1):
        fitness_scores = [(route, calculate_fitness(route)) for route in population]
        fitness_scores.sort(key=lambda x: x[1])
        
        current_best_route, current_best_dist = fitness_scores[0]
        
        if current_best_dist < best_overall_dist:
            best_overall_dist = current_best_dist
            best_overall_route = current_best_route

        # Вывод каждой итерации
        if gen <= 10 or gen % 10 == 0: # Выводим первые 10 и каждое десятое, чтобы не спамить (можно убрать условие для всех)
            readable_route = [c + 1 for c in current_best_route]
            print(f"Ген {gen:<8} | {str(readable_route):<25} | {current_best_dist:<10}")

        parent1, parent2 = random.sample(population, 2)
        new_population = [parent1, parent2]
        while len(new_population) < POPULATION_SIZE:
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        population = new_population

    print("-" * 55)
    print("=== Итоги Генетического Алгоритма ===")
    print(f"Найденный маршрут: {[c + 1 for c in best_overall_route]}")
    print(f"Его длина: {best_overall_dist}")

    print("\n=== Проверка оптимальности (Полный перебор) ===")
    bf_route, bf_dist = brute_force_optimal()
    print(f"Эталонный кратчайший путь: {[c + 1 for c in bf_route]}")
    print(f"Минимально возможная длина: {bf_dist}")

    if best_overall_dist <= bf_dist:
        print("\nРезультат: ГА нашел глобальный оптимум.")
    else:
        print(f"\nРезультат: ГА остановился на локальном минимуме (разница {best_overall_dist - bf_dist}).")

if __name__ == "__main__":
    main()