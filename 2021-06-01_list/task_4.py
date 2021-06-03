# Вводится N, затем N элементов списка по одному в строке. Определите, есть ли в списке повторяющиеся элементы.

a = []
n = int(input())
for i in range(n):
    a.append(input())
if len(a) == len(set(a)):
    print('NO')
else:
    print('YES')
