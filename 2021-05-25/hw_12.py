# Вывести на экран 20 строк. В строках с четными номерами вывести по 10 чисел, равных
# номеру строки. В строках с нечетными номерами вывести десять единиц. Числа выводить
# через пробел.

for i in range(1, 21):
    print()
    for j in range(10):
        if i % 2 != 0:
            print(1, end=' ')
        else:
            print(i, end=' ')