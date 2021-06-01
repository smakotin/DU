# Сколько существует четырехзначных чисел, которые ровно в 600 раз больше
# суммы своих цифр?

count = 0
for i in range(1000, 10000):
    temp = i
    sum = 0
    while temp > 0:
        sum += temp % 10
        temp //= 10
    if i / 600 == sum:
        count += 1
print(count)
