# Вводится число N, далее N чисел по одному в строке – элементы списка. Затем
# вводится
# число K. Выполнить циклический сдвиг элменетов списка вправо на K позиций. Вывести
# результат в одной строке, числа разделить пробелом. Гаранитируется что K <= N.
# Сдвиг на одну позицию, означает, что элемент с индексом 0 стенет первым, второй –
# третим и т.д. Циклический означает что последний элемент станет первым.
# Смотри примеры для лучшего понимания.

lst = []
n = int(input('Введите количество элементов списка: '))
for i in range(n):
    lst.append(int(input('Введите элемент списка: ')))
print(lst)
k = int(input('Выполнить циклический сдвиг на K элементов, введите K: '))
for j in range(k):
    lst.insert(0, lst.pop(-1))
print(lst)

