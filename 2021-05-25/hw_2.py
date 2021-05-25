# Вводится три числа. Вывести количество положительных среди них

count = 0
a = int(input())
if a > 0:
    count += 1
b = int(input())
if b > 0:
    count += 1
c = int(input())
if c > 0:
    count += 1

print(f'Положительных чисел введено: {count}')
