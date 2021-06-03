# Дан список. После каждого элемента добавьте предшествующую ему часть списка.

a = [10, 9, 8, 7, 6, 5]
b = []
c = []
for i in a:
    b.append(i)
    for j in range(len(b)):
        c.append(b[j - 1])
print(c)
