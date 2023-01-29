from datetime import datetime


def partial_repr(obj: object, *args: str, **kwargs: str) -> str:
    """Return a string to represent the given `obj` partially.

    Args:
        obj (object): object to represent
        args (tuple[str]): attribute names to represent
        kwargs (dict[str, str]): representations for the attributes

    Returns:
        str: representation of `obj`
    """
    # attribute names and values of `obj` specified by `args`
    attr_ss = [f"{k}={v!r}" for k,
               v in obj.__dict__.items() if k in args and k not in kwargs]

    # use `kwargs` for the representation of the attributes
    additional_ss = [f"{k}={v}" for k, v in kwargs.items()]

    return f"{obj.__class__.__name__}({', '.join(attr_ss + additional_ss)})"


class User:
    def __init__(self, id: int, name: str, active: bool, type: str) -> None:
        self.id = id
        self.name = name
        self.active = active
        self.type = type
        self.created_at = datetime.now()


class UserGroup:
    def __init__(self, id: int, name: str, users: list[User]) -> None:
        self.id = id
        self.name = name
        self.users = list(users)
        self.created_at = datetime.now()


alice = User(0, "alice", True, "admin")
bob = User(1, "bob", False, "user")
eve = User(2, "eve", True, "user")

users = [alice, bob, eve]

user_group = UserGroup(0, "developers", users)

users_repr = f"{[partial_repr(user, 'id', 'name') for user in users]}"
print(partial_repr(user_group, "id", "name", users=users_repr))
# UserGroup(id=0, name='developers', users=["User(id=0, name='alice')", "User(id=1, name='bob')", "User(id=2, name='eve')"]) # noqa: E501
