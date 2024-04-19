import numpy as np

# Задание функций критериев fi(x)
def f1(x):
    return a1 * (x[0] - b1)**2 + c1 * (x[1] - d1)**2

def f2(x):
    return a2 * (x[0] - b2)**2 + c2 * (x[1] - d2)**2

def f3(x):
    return a3 * (x[0] - b3)**2 + c3 * (x[1] - d3)**2

# Задание параметров функций
a1, b1, c1, d1 = 1, 2, 3, 4
a2, b2, c2, d2 = 2, 3, 4, 5
a3, b3, c3, d3 = 3, 4, 5, 6

# Реализация метода аддитивной свертки
def additive_convolution(x):
    return a1 * f1(x) + a2 * f2(x) + a3 * f3(x)

# Поиск оптимальной точки
def find_optimal_point():
    # Реализация алгоритма поиска оптимальной точки
    pass

# Вызов функции поиска оптимальной точки
optimal_point = find_optimal_point()
print("Оптимальная точка по методу аддитивной свертки:", optimal_point)
