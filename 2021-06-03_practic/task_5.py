# Матрица состоит из нулей и единиц. Найдите в ней самую длинную цепочку подряд
# идущих нулей по горизонтали, вертикали или диагонали.
import random

rows = 5
columns = 5
matrix = [[random.randint(0, 1) for i in range(rows)] for j in range(columns)]

# количество нулей подряд по горизонтали
count_zero = 0
temp = 0
for i in range(rows):
    temp = 0
    for j in range(columns):
        if matrix[i][j] == 0:
            temp += 1
            if temp > count_zero:
                count_zero = temp
                horizontal = i + 1
        else:
            temp = 0

# максимальное кол-во нулей по вертикали
count_zero_vert = 0
temp2 = 0
for i in range(columns):
    temp2 = 0
    for j in range(rows):
        if matrix[j][i] == 0:
            temp2 += 1
            if temp2 > count_zero_vert:
                count_zero_vert = temp2
                vertical = i + 1
        else:
            temp2 = 0


print(f'Максимальное количество нулей по горизонтали {count_zero} в строке {horizontal}')
print(f'Максимальное количество нулей по вертикали {count_zero_vert} в столбце {vertical}')
for _ in matrix:
    print(_)

