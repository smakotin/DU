# Даны три числа. Вывести на экран “yes”, если среди них есть одинаковые, иначе вывести
# “ERROR”

a = int(input())
b = int(input())
c = int(input())
if a == b or a == c or b == c:
    print('yes')
else:
    print('ERROR')
