# Вводится число N, далее N чисел по одному в строке – элементы списка 1. Затем
# вводится число M, далее M чисел по одному в строке – элементы списка 2. Используя
# множества для решения, выведите на экран в строку через пробел общие элементы
# списков. Элементы должны быть отсортированы по возрастанию. Если общих элементов
# нет, ничего выводить не требуется

lst1 = []
n = int(input())
for i in range(n):
    lst1.append(int(input()))
lst2 = []
m = int(input())
for i in range(m):
    lst2.append(int(input()))
for j in sorted(set.intersection(set(lst1), set(lst2))):
    print(j, end=' ')