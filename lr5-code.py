import numpy as np
n, m = map(int, input('Размерность первого массива: ').split())
a, b = map(int, input('Размерность второго массива: ').split())
if n > 10 or m > 10:
    print('Массив n, m больше 10x10')
    exit()
if a > 10 or b > 10:
    print('Массив a, b больше 10x10')
    exit()
matrix1 = np.random.randint(-10, 10, (n, m))
matrix2 = np.random.randint(-10, 10, (a, b))
print('Первый массив: ')
print(matrix1)
print('Второй массив: ')
print(matrix2)
pos_cons = []
for i in range(m):
    product = 1
    has_negativ = False
    for j in range(n):
        if matrix1[j, i] < 0:
            product *= matrix1[j, i]
            has_negativ = True
    if has_negativ and product > 0:
        pos_cons.append(i)
pos_cons2 = []
for i in range(b):
    product = 1
    has_negativ = False
    for j in range(a):
        if matrix2[j, i] < 0:
            product *= matrix2[j, i]
            has_negativ = True
    if has_negativ and product > 0:
        pos_cons2.append(i)
if pos_cons:
    print("Номера столбцов с положительным произведением отрицательных элементов в первом массиве:", pos_cons)
else:
    print("Нет столбцов с положительным произведением отрицательных элементов в первом массиве.")
if pos_cons2:
    print("Номера столбцов с положительным произведением отрицательных элементов во втором массиве:", pos_cons2)
else:
    print("Нет столбцов с положительным произведением отрицательных элементов во втором массиве.")