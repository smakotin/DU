# Вводится N, затем N элементов списка по одному в строке. Найти сумму наибольшего и наименьшего элементов.

a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
a.sort()
print(a[0] + a[-1])

