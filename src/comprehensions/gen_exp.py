a = [1, 2, 3, 4, 5]

g = (x ** 2 for x in a)
print(g)

# g[0]    # TypeError: 'generator' object is not subscriptable


g0 = next(g)
print(g0)   # 1

g1 = next(g)
print(g1)   # 4

rest = list(g)
print(rest)  # [9, 16, 25]

# next(g) # StopIteration
