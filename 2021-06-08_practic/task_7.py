# Написать функцию, которая определяет, есть ли в списке повторяющиеся элементы, если да, то возвращает список с
# повторяющимися элементами

a = [5, 5, 2, 2, 3, 4, 7, 7]


def repetitive(lst):
    return [x for x, j in enumerate(lst) if lst.count(x) > 1]


print(repetitive(a))
