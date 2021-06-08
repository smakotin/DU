# Создайте функцию get_data, которая просит ввести first_name, last_name, age и возвращает кортеж из этих трех
# значений.

def get_data():
    first_name = input('input first_name: ')
    last_name = input('input last_name: ')
    age = input('input age: ')
    person = (first_name, last_name, age)
    return person

print(get_data())