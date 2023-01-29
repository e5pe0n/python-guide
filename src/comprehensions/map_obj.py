a = [1, 2, 3, 4, 5]

m = map(lambda x: x ** 2, a)
print(m)    # <map object at 0x7ff4e2729ed0>

# m[0]    # TypeError: 'map' object is not subscriptable

m0 = next(m)
print(m0)   # 1

m1 = next(m)
print(m1)   # 4

rest = list(m)
print(rest)  # [9, 16, 25]

# next(m) # StopIteration
