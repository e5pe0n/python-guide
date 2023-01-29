a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# start=1, stop=8, step=2
print(a[1:8:2])  # [1, 3, 5, 7]

head2 = a[:2]
print(head2)    # [0, 1]

until_last = a[:-1]
print(until_last)   # [0, 1, 2, 3, 4, 5, 6, 7, 8]

tail2 = a[-2:]
print(tail2)    # [8, 9]

reversed_a = a[::-1]
print(reversed_a)   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


shallow_copy_a = a[:]
print(shallow_copy_a)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

shallow_copy_a[0] = 100
print(a)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(shallow_copy_a)   # [100, 1, 2, 3, 4, 5, 6, 7, 8, 9]
