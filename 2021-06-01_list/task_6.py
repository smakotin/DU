# Даны два кортежа:
# subdivision = („Brest“, „Homel“, „Grodno“, „Mogilev“, „Minsk“, „Vitebsk“)
# population = (1401177, 1440718, 1072381, 1099074, 1422528, 1230821)
# Создайте словарь population_dict, где каждой области в качестве ключа соответствует население в качестве значения.
# Выведите результат. Выведите сумму численности населения из всех областей. Выведите область с самым большим
# населением в виде «Область: <key>, Население: <value>». Найти среднее арифметическое всех значений. Вывести название
# области, население которой ближе всех к среднему.

subdivision = ('Brest', 'Homel', 'Grodno', 'Mogilev', 'Minsk', 'Vitebsk')
population = (1401177, 1440718, 1072381, 1099074, 1422528, 1230821)
population_dict = {}
for i in range(len(subdivision)):
    population_dict[subdivision[i]] = population[i]
print(population_dict)
print(f'сумма численности населения из всех областей: {sum(population_dict.values())}')

max_population_city = ''

for key, value in population_dict.items():
    if value == max(population_dict.values()):
        max_population_city = key

print(f'Самое большое население: Область: {max_population_city}, Население {max(population_dict.values())}')

population_average = sum(population) / len(population)
middle_city = ''

for k, v in population_dict.items():
    middle = v
    if abs(v - population_average) < middle:
        middle = v
        middle_city = k

print(f'{population_average} - среднее количество жителей, а область ближе к среднему значению: {middle_city}')
