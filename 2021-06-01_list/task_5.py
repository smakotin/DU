# Создать пустой словарь двумя способами. Проинициализируйте словарь person с ключами first_name и last_name и
# значением по умолчанию None. Присвойте значения ключам first_name и last_name. Добавьте ключ age со значением
# возраста. Выведите список всех ключей словаря person. Выведите список всех значений словаря person

a = {}
person = dict()
person = {'first_name': None, 'last_name': None}
person['first_name'] = 'Garry'
person['last_name'] = 'Grand'
person['age'] = 55
print(person.keys())
print(person.values())
