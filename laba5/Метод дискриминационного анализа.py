import numpy as np

# Задание функций критериев fi(x)
def f1(x):
    return (x[0] - 2)**2 + 3 * (x[1] - 4)**2

def f2(x):
    return 2 * (x[0] + 3)**2 + 4 * (x[1] + 1)**2

def f3(x):
    return 3 * (x[0] + 4)**2 + 5 * (x[1] - 3)**2

# Задание параметров функций
a1, a2, a3 = 0.4, 0.3, 0.3

# Реализация метода дискриминационного анализа с весами
def discrimination_analysis(x):
    f_values = [a1 * f1(x), a2 * f2(x), a3 * f3(x)]
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
            index = discrimination_analysis((x1, x2))
            # Поиск минимального индекса
            if index < min_index:
                min_index = index
                optimal_point = (x1, x2)
    
    return optimal_point if optimal_point is not None else "No optimal point found"

# Вызов функции поиска оптимальной точки
optimal_point = find_optimal_point()
print("Оптимальная точка по методу дискриминационного анализа:", optimal_point)
