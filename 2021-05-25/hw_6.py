# Вводится число. Удалить 3ю цифру. Нумерация начинается слева с 1. Гарантируется что
# количество цифр в числе не менее 3. Не используйте строки, только циклы, if'ы и
# целочисленные переменные

a = int(input())
b = a
result = 0
count = 0
while b // 100 >= 1:
    b = b // 10
    count += 1
b = b * 10 ** (count - 1)
result = b + (a % 10 ** (count - 1))
print(result)
