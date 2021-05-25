# Ввести число. Вывести произведение его цифр

a = input()
result = 1
for i in a:
    result *= int(i)
print(result)