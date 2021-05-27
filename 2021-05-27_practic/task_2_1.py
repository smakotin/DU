# Дано число. Если оно меньше 7, то вывести Yes, если больше 10, то вывести No,
# если равно 9, то вывести Error.

a = int(input())
if a < 7:
    print('Yes')
elif a > 10:
    print('No')
elif a == 9:
    print('Error')
