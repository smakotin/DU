# Пользователь вводит ненулевые числа до тех пор пока не введет ноль. Найдите
# сумму этих чисел.

result = 0
while True:
    a = int(input())
    if a == 0:
        break
    else:
        result += a
print(result)
