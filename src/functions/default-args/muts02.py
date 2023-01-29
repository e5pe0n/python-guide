# NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG

class User:
    def __init__(
        self, id: int,
        name: str,
        permissions: list[str] | None = None
    ) -> None:
        self.id = id
        self.name = name
        self.permissions = permissions if permissions else []

    def add_permission(self, permission: str) -> None:
        self.permissions.append(permission)


alice = User(0, "alice")
print(alice.permissions)    # []

alice.add_permission("read")
alice.add_permission("write")

print(alice.permissions)    # ['read', 'write']


bob = User(1, "bob")
print(bob.permissions)  # []
