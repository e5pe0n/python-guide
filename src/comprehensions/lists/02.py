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
active_users = []
for user in users:
    if user["active"]:
        active_users.append(user)
print(active_users)
# [
#   {'id': 0, 'name': 'alice', 'active': True},
#   {'id': 2, 'name': 'eve', 'active': True},
# ]


# using filter()
active_users = list(filter(lambda x: x["active"], users))
print(active_users)
# [
#   {'id': 0, 'name': 'alice', 'active': True},
#   {'id': 2, 'name': 'eve', 'active': True},
# ]


# comprehension style
active_users = [user for user in users if user["active"]]
print(active_users)
# [
#   {'id': 0, 'name': 'alice', 'active': True},
#   {'id': 2, 'name': 'eve', 'active': True},
# ]
