# Написать функцию, принимает в качестве аргумента список и которая должна поменять местами самый большой и
# самый маленький элементы этого списка и вернуть новый список.


def change_pos(lst):
    mx = max(lst)
    mn = min(lst)
    for i in range(len(lst)):
        if lst[i] == mx:
            lst[i] = mn
        elif lst[i] == mn:
            lst[i] = mx
    return lst
