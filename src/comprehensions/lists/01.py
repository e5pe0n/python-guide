a = [1, 2, 3, 4, 5]

# imperative
b = []
for x in a:
    b.append(x ** 2)
print(b)    # [1, 4, 9, 16, 25]


# using map()
b = list(map(lambda x: x ** 2, a))
print(b)    # [1, 4, 9, 16, 25]


# comprehension style
b = [x ** 2 for x in a]
print(b)    # [1, 4, 9, 16, 25]
