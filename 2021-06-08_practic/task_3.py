# 3. Создайте функцию, которая принимает строку и возвращает список неповторяющихся символов в ней.

def unic(s):
    return list(set(s))

print(unic('hello'))