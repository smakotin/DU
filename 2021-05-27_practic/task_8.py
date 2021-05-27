# 8. * Написать программу выводящую разложение числа на простые множители

a = int(input('Введите число: '))
result = []
div = 2
while a > 1:
    while a % div == 0:
        result.append(div)
        a /= div
    div += 1
print(f'Простые множители этого числа: {result}')
