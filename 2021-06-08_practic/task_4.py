#  Создайте функцию create_dict, которая принимает любое количество именованных аргументов, создает словарь,
# ключами которого являются значения этих аргументов, а значениями длина значения аргумента.
# Например:
# create_dict(arg1=“first_key“, arg2=“second_key“)
# должна вернуть
# {„first_key“: 9, „second_key“: 10}

def create_dict(**kwargs):
    dct = {}
    for key, value in kwargs.items():
        dct[value] = len(value)
    return dct

print(create_dict(arg1='first_key', arg2='second_key'))