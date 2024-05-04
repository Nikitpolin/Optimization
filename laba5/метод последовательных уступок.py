import numpy as np

# Задание функций критериев fi(x)
def f1(x):
    return a1 * (x[0] - b1)**2 + c1 * (x[1] - d1)**2

def f2(x):
    return a2 * (x[0] - b2)**2 + c2 * (x[1] - d2)**2

def f3(x):
    return a3 * (x[0] - b3)**2 + c3 * (x[1] - d3)**2

# Задание параметров функций
a1, b1, c1, d1 = 0.4, 2, 3, 4
a2, b2, c2, d2 = 0.3, -3, 4, -1
a3, b3, c3, d3 = 0.3, 4, 5, -3

# Реализация метода последовательных уступок
def successive_concessions(x):
    f_values = [f1(x), f2(x), f3(x)]
    min_index = np.argmin(f_values)
    return min_index + 1

# Поиск оптимальной точки
def find_optimal_point():
    # Инициализация оптимальной точки и минимального индекса
    optimal_point = None
    min_index = np.inf
    
    # Перебор всех возможных точек
    for x1 in np.linspace(0, 10, num=100):
        for x2 in np.linspace(0, 10, num=100):
            # Вычисление индекса минимальной функции
            index = successive_concessions((x1, x2))
            # Поиск минимального индекса
            if index < min_index:
                min_index = index
                optimal_point = (x1, x2)
    
    return optimal_point if optimal_point is not None else "No optimal point found"

# Вызов функции поиска оптимальной точки
optimal_point = find_optimal_point()
print("Оптимальная точка по методу последовательных уступок:", optimal_point)

