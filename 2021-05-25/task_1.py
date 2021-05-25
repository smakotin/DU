# Ввести два числа. Присвоить их переменным a и b. Сравнить а и b. Присвоить переменной
# result бОльшую из них. Вывести result

a = int(input())
b = int(input())
result = a if a > b else b
print(result)