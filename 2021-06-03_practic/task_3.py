# Найти количество строк матрицы, числа в которых возрастают.
import random

rows = 3
columns = 3
a = [[random.randrange(0, 20) for i in range(rows)] for j in range(columns)]
count = 0
for x in range(rows):
    if sorted(a[x]) == a[x]:
        count += 1
    print(a[x])

print(count)