from itertools import chain


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

email_settings = [
    {
        "id": 2,
        "email": "eve@example.com",
    },
    {
        "id": 0,
        "email": "alice@example.com",
    },
    {
        "id": 1,
        "email": "bob@example.com",
    },
]


# imperative
name_and_email_pairs = []
for user in users:
    for email_setting in email_settings:
        if user["id"] == email_setting["id"]:
            name_and_email_pairs.append((user["name"], email_setting["email"]))
print(name_and_email_pairs)
# [
#   ('alice', 'alice@example.com'),
#   ('bob', 'bob@example.com'),
#   ('eve', 'eve@example.com'),
# ]


# using `map()` and `filter()`
name_and_email_pairs = list(chain.from_iterable(
    map(
        lambda user: map(
            lambda email_setting: (user["name"], email_setting["email"]),
            filter(
                lambda email_setting: email_setting["id"] == user["id"],
                email_settings
            )
        ),
        users
    )
))
print(name_and_email_pairs)
# [
#   ('alice', 'alice@example.com'),
#   ('bob', 'bob@example.com'),
#   ('eve', 'eve@example.com'),
# ]


# comprehension style
name_and_email_pairs = [
    (user["name"], email_setting["email"])
    for user in users
    for email_setting in email_settings
    if user["id"] == email_setting["id"]
]
print(name_and_email_pairs)
# [
#   ('alice', 'alice@example.com'),
#   ('bob', 'bob@example.com'),
#   ('eve', 'eve@example.com'),
# ]
