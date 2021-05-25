# Вводятся три числа. Вывести на экран "yes", если можно взять какие-то два из них и в
# сумме получить третье. В противном случае вывести "no"

a = int(input())
b = int(input())
c = int(input())
if a + b == c or a + c == b or b + c == a:
    print('yes')
else:
    print('no')