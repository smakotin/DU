# Поменять местами столбцы матрицы так, чтобы элементы первой строки
# оказались упорядоченными
import random

n = int(input('введите количество строк:  '))
m = int(input('введите количество столбцов:  '))

matrix = [[random.randrange(0, 100) for i in range(n)] for j in range(m)]
first_sorted = True
xx = {}
for i in range(m):
    if first_sorted:
        if sorted(matrix[i]) == matrix[i]:
            print(matrix[i])
            first_sorted = False
        else:
            print(sorted(matrix[i]))
            first_sorted = False
    print(matrix[i])
