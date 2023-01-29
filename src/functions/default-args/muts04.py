class User:
    def __init__(
        self, id: int,
        name: str,
        permissions: list[str] | None = None
    ) -> None:
        self.id = id
        self.name = name
        self.permissions = list(permissions) if permissions else []

    def add_permission(self, permission: str) -> None:
        self.permissions.append(permission)


alice = User(0, "alice", ["read"])
print(alice.permissions)    # ['read']

bob = User(1, "bob", alice.permissions)

bob.add_permission("write")

print(bob.permissions)  # ['read', 'write']
print(alice.permissions)    # ['read']

# Now `bob.permissions` and `alice.permissions` refer to different objects.
print(id(bob.permissions))  # 140036616582336
print(id(alice.permissions))    # 140036616582208
