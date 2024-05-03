def f1(x1, x2):
    return a1 * (x1 - b1)**2 + c1 * (x2 - d1)**2

def f2(x1, x2):
    return a2 * (x1 - b2)**2 + c2 * (x2 - d2)**2

def f3(x1, x2):
    return a3 * (x1 - b3)**2 + c3 * (x2 - d3)**2

# Задание параметров функций
a1, b1, c1, d1 = 1, 2, 3, 4
a2, b2, c2, d2 = 2, -3, 4, -1
a3, b3, c3, d3 = 3, 4, 5, -3

def Discrimination_Method(x1_range, x2_range):
    optimal_point = None
    min_f_val = float('inf')
    
    for x1 in x1_range:
        for x2 in x2_range:
            f1_val = f1(x1, x2)
            f2_val = f2(x1, x2)
            f3_val = f3(x1, x2)
            
            min_val = min(f1_val, f2_val, f3_val)
            
            if min_val < min_f_val:
                min_f_val = min_val
                optimal_point = (x1, x2, min_val)
    
    return optimal_point

# Задание диапазонов переменных x1 и x2
x1_range = range(-10, 11)
x2_range = range(-10, 11)

# Поиск оптимальной точки методом дискриминационного анализа
optimal_point = Discrimination_Method(x1_range, x2_range)

# Вывод результата
print("Оптимальная точка методом дискриминационного анализа:")
print("Точка:", optimal_point[:2], "Значение функции:", optimal_point[2])
