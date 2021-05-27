# * Написать программу проверяющую число на простоту

a = int(input())
is_prime = True
for i in range(2, a):
    if a % i == 0:
        is_prime = False
        break
    else:
        is_prime = True
print(f'проверка числа a на простоту: {is_prime}')
