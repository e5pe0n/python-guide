def eq_name(name1: str, name2: str, case_sensitive: bool = True) -> bool:
    if case_sensitive:
        return name1 == name2

    return name1.lower() == name2.lower()


print(eq_name("alice", "Alice"))    # False
print(eq_name("alice", "Alice", False))  # True


class User:
    def __init__(self, id: int, name: str, active: bool = True) -> None:
        self.id = id
        self.name = name
        self.active = active

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, active={self.active})"


alice = User(0, "alice")
print(alice)    # User(id=0, name=alice, active=True)

bob = User(1, "bob", False)
print(bob)  # User(id=1, name=bob, active=False)
