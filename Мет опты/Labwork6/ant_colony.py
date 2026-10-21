import numpy as np
import random

INF = float('inf')

# Матрица смежности графа. Индексы: 0:A, 1:B, 2:C, 3:D, 4:E, 5:F, 6:G
graph = np.array([
    [INF, 4, 16, INF, 7, INF, INF],     # A
    [4, INF, INF, 16, INF, INF, 39],    # B
    [16, INF, INF, INF, INF, INF, INF], # C
    [INF, 16, INF, INF, 10, 11, 19],    # D
    [7, INF, INF, 10, INF, 17, INF],    # E
    [INF, INF, INF, 11, 17, INF, 8],    # F
    [INF, 39, INF, 19, INF, 8, INF]     # G
])

NUM_NODES = len(graph)
NODE_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
START_NODE = 0 # A
END_NODE = 6   # G

# Параметры алгоритма
NUM_ANTS = 10
ITERATIONS = 50
ALPHA = 1.0       # Влияние феромона
BETA = 2.0        # Влияние эвристики (видимости)
EVAPORATION = 0.5 # Коэффициент испарения феромона
Q = 100           # Константа отложения феромона

# Инициализация матрицы феромонов
pheromones = np.ones((NUM_NODES, NUM_NODES))

def run_aco():
    global pheromones
    best_path = None
    best_path_length = INF

    print(f"{'Итерация':<10} | {'Лучший путь в итерации':<30} | {'Длина':<10}")
    print("-" * 55)

    for iteration in range(1, ITERATIONS + 1):
        all_paths = []
        all_lengths = []
        iter_best_length = INF
        iter_best_path = None

        for ant in range(NUM_ANTS):
            current_node = START_NODE
            path = [current_node]
            path_length = 0
            reached_target = False

            while current_node != END_NODE:
                unvisited_neighbors = []
                for neighbor in range(NUM_NODES):
                    if graph[current_node][neighbor] != INF and neighbor not in path:
                        unvisited_neighbors.append(neighbor)

                if not unvisited_neighbors:
                    break

                probabilities = []
                for neighbor in unvisited_neighbors:
                    tau = pheromones[current_node][neighbor] ** ALPHA
                    eta = (1.0 / graph[current_node][neighbor]) ** BETA
                    probabilities.append(tau * eta)

                prob_sum = sum(probabilities)
                probabilities = [p / prob_sum for p in probabilities]

                next_node = random.choices(unvisited_neighbors, weights=probabilities, k=1)[0]
                
                path.append(next_node)
                path_length += graph[current_node][next_node]
                current_node = next_node

                if current_node == END_NODE:
                    reached_target = True

            if reached_target:
                all_paths.append(path)
                all_lengths.append(path_length)
                
                if path_length < iter_best_length:
                    iter_best_length = path_length
                    iter_best_path = path
                
                if path_length < best_path_length:
                    best_path_length = path_length
                    best_path = path

        # Логирование текущей итерации
        if iter_best_path:
            path_str = "->".join([NODE_NAMES[i] for i in iter_best_path])
            if iteration <= 5 or iteration % 10 == 0 or iteration == ITERATIONS:
                print(f"{iteration:<10} | {path_str:<30} | {iter_best_length:<10}")

        # Обновление феромонов
        pheromones *= (1 - EVAPORATION)
        for path, length in zip(all_paths, all_lengths):
            pheromone_to_add = Q / length
            for i in range(len(path) - 1):
                u, v = path[i], path[i+1]
                pheromones[u][v] += pheromone_to_add
                pheromones[v][u] += pheromone_to_add

    return best_path, best_path_length

def brute_force_verification(current_node, end_node, visited, current_path, current_length):
    """Рекурсивный поиск всех простых путей для нахождения эталона"""
    if current_node == end_node:
        return current_path[:], current_length

    best_p = None
    best_l = INF

    for neighbor in range(NUM_NODES):
        weight = graph[current_node][neighbor]
        if weight != INF and neighbor not in visited:
            visited.add(neighbor)
            current_path.append(neighbor)
            
            p, l = brute_force_verification(neighbor, end_node, visited, current_path, current_length + weight)
            
            if l < best_l:
                best_l = l
                best_p = p
            
            current_path.pop()
            visited.remove(neighbor)
            
    return best_p, best_l

def main():
    # 1. Запуск муравьиного алгоритма
    print("=== Запуск Алгоритма Муравьиной Колонии ===")
    aco_path, aco_length = run_aco()
    
    # 2. Запуск проверки полным перебором
    print("\n=== Проверка оптимальности (Полный перебор всех путей) ===")
    bf_path, bf_length = brute_force_verification(START_NODE, END_NODE, {START_NODE}, [START_NODE], 0)
    
    # Вывод результатов
    if aco_path:
        aco_named = " -> ".join([NODE_NAMES[i] for i in aco_path])
        print(f"Результат ACO:  {aco_named} | Длина: {aco_length}")
    
    bf_named = " -> ".join([NODE_NAMES[i] for i in bf_path])
    print(f"Эталон (Min):  {bf_named} | Длина: {bf_length}")

    if aco_length <= bf_length:
        print("\nИтог: Муравьи нашли оптимальный путь!")
    else:
        print(f"\nИтог: Найден субтитмальный путь (отклонение: {aco_length - bf_length})")

if __name__ == "__main__":
    main()