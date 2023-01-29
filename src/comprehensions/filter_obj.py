a = [1, 2, 3, 4, 5]

f = filter(lambda x: x % 2 != 0, a)
print(f)    # <map object at 0x7ff4e2729ed0>

# f[0]    # TypeError: 'filter' object is not subscriptable

f0 = next(f)
print(f0)   # 1

f1 = next(f)
print(f1)   # 3

rest = list(f)
print(rest)  # [5]

# next(f) # StopIteration


users = [
    {
        "id": 0,
        "name": "alice",
        "active": True,
    },
    {
        "id": 1,
        "name": "bob",
        "active": False,
    },
    {
        "id": 2,
        "name": "eve",
        "active": True,
    },
]


# imperative
user100 = None
for user in users:
    if user["id"] == 100:
        user100 = user
        break
print(user100)


# using `next()` and `filter()`
user100 = next(filter(lambda user: user["id"] == 100, users), None)
print(user100)  # None


# comprehension style
user100 = user100s[0] if (
    user100s := [user for user in users if user["id"] == 100]) else None
print(user100)  # None
