def merge_dict(a: dict, b: dict, *args) -> dict:
    res = a | b
    for arg in args:
        res |= arg

    return res


d1 = {
    "id": 0,
    "name": "alice",
}

d2 = {
    "active": True,
}

d3 = {
    "type": "admin"
}

d4 = {
    "permissions": ["read", "write"]
}

d = merge_dict(d1, d2)
print(d)    # {'id': 0, 'name': 'alice', 'active': True}

d = merge_dict(d1, d2, d3, d4)
print(d)
# {
#   'id': 0,
#   'name': 'alice',
#   'active': True,
#   'type': 'admin',
#   'permissions': ['read', 'write'],
# }

ds = [d3, d4]
d = merge_dict(d1, d2, *ds)  # same with `merge_dict(d1, d2, d3, d4)`
print(d)
# {
#   'id': 0,
#   'name': 'alice',
#   'active': True,
#   'type': 'admin',
#   'permissions': ['read', 'write'],
# }
