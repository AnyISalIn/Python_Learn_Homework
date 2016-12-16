lst = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

transpose = zip(*lst)

for i in transpose:
    print(i)
