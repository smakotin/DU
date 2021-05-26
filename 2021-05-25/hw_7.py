# * Вводится 2 числа: a и b. Вывести колличество простых чисел в диапазоне [a; b].

a = int(input())
b = int(input())
count = 0
for n in range(a, b + 1):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
print(count)
