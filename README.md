# python-guide

Personal guide to write practical code in Python.  

Assume Python version is >= 3.10.  

# Contents

- [Subscripting](#subscripting)
- [Slicing](#slicing)
- [Comprehensions](#comprehensions)
  - [List Comprehensions](#list-comprehensions)
  - [Dict Comprehensions](#dict-comprehensions)
  - [Set Comprehensions](#set-comprehensions)
- [Functions](#functions)
  - [Default Arguments](#default-arguments)
  - [Variadic Arguments](#variadic-arguments)
  - [Decorator](#decorator)
- [Special Methods (Dunder Methods)](#special-methods-dunder-methods)
- [Enums](#enums)

<br>

-[References](#references)
  - [Python documentation](https://docs.python.org/3.11/index.html)
  - [Fluent Python, 2nd Ed. / Luciano Ramalho / (O'Reilly)](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)

# Subscripting

Negative integer can be used as backward index.  

```py
# src/subscripting.py

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

first = a[0]
print(first)    # 0

second = a[1]
print(second)   # 1

last = a[-1]
print(last)  # 9

penaltimate = a[-2]
print(penaltimate)  # 8

```

# Slicing

## Tip: `length = stop - start`

For example, let say `start=2` and `stop=5` then `a[2:5]` evalutes to `[a[0], a[1], a[2]]`.  
The length is `stop - start = 5 - 2 = 3`.  
___

```py
# src/slicing.py

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# start=1, stop=8, step=2
print(a[1:8:2])  # [1, 3, 5, 7]

head2 = a[:2]
print(head2)    # [0, 1]

until_last = a[:-1]
print(until_last)   # [0, 1, 2, 3, 4, 5, 6, 7, 8]

tail2 = a[-2:]
print(tail2)    # [8, 9]

reversed_a = a[::-1]
print(reversed_a)   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


shallow_copy_a = a[:]
print(shallow_copy_a)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

shallow_copy_a[0] = 100
print(a)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(shallow_copy_a)   # [100, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```

# Comprehensions

Comprehensions are syntax to create `list`, `dict`, `set` and `generator` concisely.  
In many cases, comprehension style and using built-in function such as `map()` and `filter()` are better than imperative style using `for-loop` for performance.  
Choose appropriate notation from imperative style, using `map()` and comprehension style for readability and performance.  

### Tip: `map()` and `filter()` are evaluted lazily

`map()` and `filter()` return *map object* and *filter object* respectively, instread of creating a new *list object*/*dict object*/*set object* then returning it immediately.  
map objects and filter objects are evaluted just when their value are required.  

```py
# src/comprehensions/map_obj.py

a = [1, 2, 3, 4, 5]

m = map(lambda x: x ** 2, a)
print(m)    # <map object at 0x7ff4e2729ed0>

# m[0]    # TypeError: 'map' object is not subscriptable

m0 = next(m)
print(m0)   # 1

m1 = next(m)
print(m1)   # 4

```

```py
# src/comprehensions/filter_obj.py

a = [1, 2, 3, 4, 5]

f = filter(lambda x: x % 2 == 0, a)
print(f)    # <map object at 0x7ff4e2729ed0>

# f[0]    # TypeError: 'filter' object is not subscriptable

f0 = next(f)
print(f0)   # 2

f1 = next(f)
print(f1)   # 4

```

___

## List Comprehensions

```py
# src/comprehensions/lists/01.py

a = [1, 2, 3, 4, 5]

# imperative
b = []
for x in a:
    b.append(x ** 2)
print(b)


# using map()
b = list(map(lambda x: x ** 2, a))
print(b)


# comprehension style
b = [x ** 2 for x in a]
print(b)

```

```py
# src/comprehensions/lists/02.py

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

```

```py
# src/comprehensions/lists/03.py
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

```

### Tip: `next()` and `filter()` combo

`next()` accepts default value as the second argument, so one would consider that combination of `next()` and `filter()` might be good for the case where possibly no elements matche the condition but some value is necessary.  

```py
# src/comprehensions/filter_obj.py

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
print(user100)  # None


# using `next()` and `filter()`
user100 = next(filter(lambda user: user["id"] == 100, users), None)
print(user100)  # None


# comprehension style
user100 = user100s[0] if (
    user100s := [user for user in users if user["id"] == 100]) else None
print(user100)  # None

```


## Dict Comprehensions

```py
# src/comprehensions/dicts/01.py

en2ja = {
    "dog": "いぬ",
    "cat": "ねこ",
    "cow": "うし",
}


# imperative
ja2en = {}
for k, v in en2ja.items():
    ja2en[v] = k
print(ja2en)
# {'いぬ': 'dog', 'ねこ': 'cat', 'うし': 'cow'}

# using comprehension
ja2en = {v: k for k, v in en2ja.items()}
print(ja2en)
# {'いぬ': 'dog', 'ねこ': 'cat', 'うし': 'cow'}

```

```py
# src/comprehensions/dicts/02.py

fruits = {
    "apple": 100,
    "banana": 200,
    "orange": 300,
    "grape": 400,
}

my_wish_list = ["apple", "orange"]


# imperative
shopping_cart = {}
for k, v in fruits.items():
    if k in my_wish_list:
        shopping_cart[k] = v
print(shopping_cart)    # {'apple': 100, 'orange': 300}


# comprehension style
shifted_box = {k: v for k, v in fruits.items() if k in my_wish_list}
print(shopping_cart)    # {'apple': 100, 'orange': 300}

```

## Set Comprehensions

```py
shopping_cart = [
    {
        "name": "apple",
        "price": 100,
    },
    {
        "name": "orange",
        "price": 200,
    },
    {
        "name": "orange",
        "price": 200,
    },
    {
        "name": "grape",
        "price": 300,
    },
    {
        "name": "apple",
        "price": 100,
    },
]


# imperative
fruits = set()  # Don't write `{}` for empty sets; `{}` is the notation for empty dict
for item in shopping_cart:
    fruits.add(item["name"])
print(fruits)   # {'apple', 'orange', 'grape'}


# comprehension style
fruits = {item["name"] for item in shopping_cart}
print(fruits)   # {'apple', 'orange', 'grape'}

```


## Generator Expressions

*Generator expression* is a notation to create *generator object*s concisely.  

```py
# src/comprehensions/gen_exp.py

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

```

### Warning: No Tuple Comprehensions

There are no comprehensions for *tuple*s in Python.  
Pass generator expression to built-in function `tuple()` to create tuples for comprehension style.  

```py
# src/comprehensions/tuples.py

a = [1, 2, 3, 4, 5]

tpl = tuple(x ** 2 for x in a)
print(tpl)  # (1, 4, 9, 16, 25)

```

# Functions

## Default Arguments

We can set default value to the function arguments.  
**Be aware that default values are evaluted only once when the defined function is loaded**.  

```py
# src/functions/default-args/example.py

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

```

### Warning: Don't use `datetime.now()` as a default value

One of common mistakes about default arguments is to use `datetime.now()` as the default value.  
Default values are evaluted only once when the defined function is loaded.  
That means that actual arguments using `datetime.now()` as the default value are fixed at the time when the defined function was loaded.  


```py
# NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG

# src/functions/default-args/dt-now-ng.py
from datetime import datetime
from time import sleep


class User:
    loading_user_at = datetime.now()
    print(loading_user_at)   # 2023-01-29 09:32:27.381419

    def __init__(self, id: int, name: str, created_at=datetime.now()) -> None:
        self.id = id
        self.name = name
        self.created_at = created_at

    loaded_user_at = datetime.now()
    print(loaded_user_at)   # 2023-01-29 09:32:27.381470


alice = User(0, "alice")
print(alice.created_at)  # 2023-01-29 09:32:27.381467)
# loading_user_at < alice.created_at < loaded_user_at

sleep(3)


bob = User(1, "bob")
print(bob.created_at)   # 2023-01-29 09:32:27.381467
# bob.created_at == alice.created_at
# loading_user_at < bob.created_at < loaded_user_at

```


`None` is often used for the default value instead.  

```py
# src/functions/default-args/dt-now-ok.py

from datetime import datetime
from time import sleep


class User:
    def __init__(
        self,
        id: int,
        name: str,
        created_at: datetime | None = None
    ) -> None:
        self.id = id
        self.name = name
        self.created_at: datetime \
            = created_at if created_at else datetime.now()

    loaded_user_at = datetime.now()


alice = User(0, "alice")
print(alice.created_at)  # 2023-01-29 09:42:25.101599

sleep(3)


bob = User(1, "bob")
print(bob.created_at)   # 2023-01-29 09:42:28.101781

```

### Warning: Don't use mutable values as default values

Again, default values are evaluted only once when the defined function is loaded.  
If the default value is mutable, possibly mutating the value after initialization will cause unexpected behaviour.  

```py
# NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG

# src/functions/default-args/muts01.py

class User:
    def __init__(
        self, id: int,
        name: str,
        permissions: list[str] = []
    ) -> None:
        self.id = id
        self.name = name
        self.permissions = permissions

    def add_permission(self, permission: str) -> None:
        self.permissions.append(permission)


alice = User(0, "alice")
print(alice.permissions)    # []

alice.add_permission("read")
alice.add_permission("write")

print(alice.permissions)    # ['read', 'write']


bob = User(1, "bob")
print(bob.permissions)  # ['read', 'write'] <- ?!?!?!

```

As the same before, `None` can be used instead.  
Note that code below even has a problem due to mutability of the argument.  


```py
# NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG

# src/functions/default-args/muts02.py

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

```


In code below, `bob` is initialized with `alice.permissions`.  
When initializing a `User` object, `__init__()` method of `User` class is assigning the `permissions` argument to `self.permissions` attribute directly.  
This results in that `bob.permissions` and `alice.permissions` refer to the same `list` object, and if one of them is mutated then the other is also mutated.  

```py
# NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG

# src/functions/default-args/muts03.py

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


alice = User(0, "alice", ["read"])
print(alice.permissions)    # ['read']

bob = User(1, "bob", alice.permissions)

bob.add_permission("write")

print(bob.permissions)  # ['read', 'write']
print(alice.permissions)    # ['read', 'write'] <- ?!?!?!

# `bob.permissions` and `alice.permissions` refer to the same object.
print(id(bob.permissions))  # 139846030651520
print(id(alice.permissions))    # 139846030651520
```

To prevent this, create a new object copying elements in the mutable object then assign the new one.  

```py
# src/functions/default-args/muts04.py

class User:
    def __init__(
        self, id: int,
        name: str,
        permissions: list[str] | None = None
    ) -> None:
        self.id = id
        self.name = name
        # Don't use the recieved mutable object as is. Create new one.
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

```

## Variadic Positional Arguments

Prepending `*` to the variable name of the function parameter, the variable can receieve positional arguments of any number as a *tuple*.  
Variadic positional argument is named `*args` conventioanly.  


```py
# src/functions/args.py

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

```

## Variadic Keyword Arguments

Prepending `**` to the variable name of the function parameter, the variable can receieve keyword arguments of any number as a *dict*.  
Variadic keyword argument is named `**kwargs` conventioanly.  

```py
# src/functions/kwargs.py

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
print(partial_repr(user_group, "id" "name", users=users_repr))
# UserGroup(id=0, name='developers', users=["User(id=0, name='alice')", "User(id=1, name='bob')", "User(id=2, name='eve')"])

```


# Decorators

Let `callable` be a callable function which takes callable objects as the arguments.  
We can write `@callable` above definitions of other functions then modify their behaviours.  

```py
# src/functions/decorators/trace01.py

from typing import Callable, Any


def trace(f: Callable) -> Callable:
    """Modify the given function `f`
    to print the function name before calling
    and the return value after returned.

    Args:
        f (Callable): a function

    Returns:
        Callable: tracing function
    """
    def wrapper() -> Any:
        fname = f"{f.__name__}()"

        print(f"calling {fname}")
        res = f()
        print(f"{fname} returned `{res}`")

        return res
    return wrapper


@trace
def one() -> int:
    return 1


print(one.__name__)  # wrapper

one()
# calling one()
# one() returned `1`

```

`@callable` is just syntax sugar; we can modify `one()` directly passing `trace()`.  

```py
# src/functions/decorators/trace02.py

from typing import Callable, Any


def trace(f: Callable) -> Callable:
    """Modify the given function `f`
    to print the function name before calling
    and the return value after returned.

    Args:
        f (Callable): a function

    Returns:
        Callable: tracing function
    """
    def wrapper() -> Any:
        fname = f"{f.__name__}()"

        print(f"calling {fname}")
        res = f()
        print(f"{fname} returned `{res}`")

        return res
    return wrapper


def one() -> int:
    return 1


one = trace(one)

print(one.__name__)  # wrapper

one()
# calling one()
# one() returned `1`

```

An example of decorator wrapping a function which takes some arguments.  

```py
# src/functions/decorators/trace03.py

from typing import Callable, Any


def fmt_f_call(f: Callable, *args, **kwargs) -> str:
    args_s = ", ".join([str(arg) for arg in args])
    kwargs_s = ", ".join([f"{k}={v}" for k, v in kwargs.items()])

    return f"{f.__name__}({args_s if args else ''}"\
        f"{', ' if (args and kwargs) else '' }{kwargs_s if kwargs else ''})"


def trace(f: Callable) -> Callable:
    """Modify the given function `f`
    to print the function name before calling
    and the return value after returned.

    Args:
        f (Callable): a function

    Returns:
        Callable: tracing function
    """
    def wrapper(*args, **kwargs) -> Any:
        f_call_s = fmt_f_call(f, *args, **kwargs)

        print(f_call_s)
        res = f(*args, **kwargs)
        print(f"{f_call_s} returned `{res}`")

        return res
    return wrapper


@trace
def one() -> int:
    return 1


@trace
def eq_name(name1: str, name2: str, case_sensitive: bool = True) -> bool:
    if case_sensitive:
        return name1 == name2

    return name1.lower() == name2.lower()


one()
# one()
# one() returned `1`

eq_name("alice", "Alice", case_sensitive=False)
# eq_name(alice, Alice, case_sensitive=False)
# eq_name(alice, Alice, case_sensitive=False) returned `True`

```

Decorator itself can take arguments.  

```py
# src/functions/decorators/trace04.py

from typing import Callable, Any, ParamSpecArgs, ParamSpecKwargs
from datetime import datetime


def fmt_f_call(f: Callable, *args, **kwargs) -> str:
    args_s = ", ".join([str(arg) for arg in args])
    kwargs_s = ", ".join([f"{k}={v}" for k, v in kwargs.items()])

    return f"{f.__name__}({args_s if args else ''}"\
        f"{', ' if (args and kwargs) else '' }{kwargs_s if kwargs else ''})"


def fmt_f_return(f: Callable, return_value: Any, *args, **kwargs) -> str:
    return f"{fmt_f_call(f, *args, **kwargs)} returned `{return_value}`"


def fmt_f_call_with_dt(f: Callable, *args, **kwargs) -> str:
    return f"{datetime.now()} | {fmt_f_call(f, *args, **kwargs)}"


def fmt_f_return_with_dt(
    f: Callable, return_value: Any,
    *args,
    **kwargs,
) -> str:
    return f"{datetime.now()} |"\
        f" {fmt_f_return(f, return_value, *args, **kwargs)}"


def trace(
    f_call_fmter: Callable[[Callable, ParamSpecArgs, ParamSpecKwargs], str],
    f_return_fmter:
        Callable[[Callable, Any, ParamSpecArgs, ParamSpecKwargs], str],
) -> Callable:
    """Modify the given function `f`
    to print some information on the function
    before calling and after returned.

    Args:
        f_call_fmter
        (Callable[[Callable, ParamSpecArgs, ParamSpecKwargs], str]):
        a function to format information printed before function calling.
        the function should take `*args` and `*kwargs` and return a string.

        f_return_fmter
        (Callable[[Callable, Any, ParamSpecArgs, ParamSpecKwargs], str]):
        a function to format information printed after function returned.
        the function should take the return value, `*args` and `**kwargs`
        and return a string.

    Returns:
        Callable: a modified function
    """
    def wrapper(f: Callable) -> Callable:
        def _wrapper(*args, **kwargs) -> Any:
            print(f_call_fmter(f, *args, **kwargs))

            res = f(*args, **kwargs)

            print(f_return_fmter(f, res, *args, **kwargs))

            return res
        return _wrapper
    return wrapper


@trace(fmt_f_call, fmt_f_return)
def one() -> int:
    return 1


@trace(fmt_f_call_with_dt, fmt_f_return_with_dt)
def eq_name(name1: str, name2: str, case_sensitive: bool = True) -> bool:
    if case_sensitive:
        return name1 == name2

    return name1.lower() == name2.lower()


one()
# one()
# one() returned `1`

eq_name("alice", "Alice", case_sensitive=False)
# 2023-02-02 01:15:59.180540 | eq_name(alice, Alice, case_sensitive=False)
# 2023-02-02 01:15:59.180592 | eq_name(alice, Alice, case_sensitive=False) returned `True` # noqa: E501

```

## Tip: Using Collable Objects


The decorator in the code above includes multiple wrappers, that might make it hard to read.  
Remember that a decorator is a *callable object*.  
Functions in Python are just one of kind of *callable object*.  
Instead of using a function, one would use a class, which instantiates callable object, to reduce nesting of closures.  


```py
# src/functions/decorators/trace05.py

from typing import Callable, Any, ParamSpecArgs, ParamSpecKwargs
from datetime import datetime


def fmt_f_call(f: Callable, *args, **kwargs) -> str:
    args_s = ", ".join([str(arg) for arg in args])
    kwargs_s = ", ".join([f"{k}={v}" for k, v in kwargs.items()])

    return f"{f.__name__}({args_s if args else ''}"\
        f"{', ' if (args and kwargs) else '' }{kwargs_s if kwargs else ''})"


def fmt_f_return(f: Callable, return_value: Any, *args, **kwargs) -> str:
    return f"{fmt_f_call(f, *args, **kwargs)} returned `{return_value}`"


def fmt_f_call_with_dt(f: Callable, *args, **kwargs) -> str:
    return f"{datetime.now()} | {fmt_f_call(f, *args, **kwargs)}"


def fmt_f_return_with_dt(
    f: Callable, return_value: Any,
    *args,
    **kwargs,
) -> str:
    return f"{datetime.now()} |"\
        f" {fmt_f_return(f, return_value, *args, **kwargs)}"


class trace:
    """Modify the given function `f`
    to print some information on the function
    before calling and after returned.

    Args:
        f_call_fmter
        (Callable[[Callable, ParamSpecArgs, ParamSpecKwargs], str]):
        a function to format information printed before function calling.
        the function should take `*args` and `*kwargs` and return a string.

        f_return_fmter
        (Callable[[Callable, Any, ParamSpecArgs, ParamSpecKwargs], str]):
        a function to format information printed after function returned.
        the function should take the return value, `*args` and `**kwargs`
        and return a string.

    Returns:
        Callable: a modified function
    """

    def __init__(
        self,
        f_call_fmter: Callable[
            [Callable, ParamSpecArgs, ParamSpecKwargs], str],
        f_return_fmter:
        Callable[[Callable, Any, ParamSpecArgs, ParamSpecKwargs], str],
    ) -> None:
        self.f_call_fmter = f_call_fmter
        self.f_return_fmter = f_return_fmter

    def __call__(self, f: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            print(self.f_call_fmter(f, *args, **kwargs))

            res = f(*args, **kwargs)

            print(self.f_return_fmter(f, res, *args, **kwargs))

            return res
        return wrapper


@trace(fmt_f_call, fmt_f_return)
def one() -> int:
    return 1


@trace(fmt_f_call_with_dt, fmt_f_return_with_dt)
def eq_name(name1: str, name2: str, case_sensitive: bool = True) -> bool:
    if case_sensitive:
        return name1 == name2

    return name1.lower() == name2.lower()


one()
# one()
# one() returned `1`

eq_name("alice", "Alice", case_sensitive=False)
# 2023-02-02 01:15:59.180540 | eq_name(alice, Alice, case_sensitive=False)
# 2023-02-02 01:15:59.180592 | eq_name(alice, Alice, case_sensitive=False) returned `True` # noqa: E501

```


## Tip: `functools.wraps()`

See a simple decorator example again.  
Notice that `print(one.__name__)` prints `wrapper`, not `one` which is the function name before modification.   

```py
from typing import Callable, Any


def trace(f: Callable) -> Callable:
    """Modify the given function `f`
    to print the function name before calling
    and the return value after returned.

    Args:
        f (Callable): a function

    Returns:
        Callable: tracing function
    """
    def wrapper() -> Any:
        fname = f"{f.__name__}()"

        print(f"calling {fname}")
        res = f()
        print(f"{fname} returned `{res}`")

        return res
    return wrapper


@trace
def one() -> int:
    return 1


print(one.__name__)  # wrapper

one()
# calling one()
# one() returned `1`

```

Using `functools.wraps()`, we can use information of the original function instead of one of wrapper.  

```py
import functools
from typing import Callable, Any


def trace(f: Callable) -> Callable:
    """Modify the given function `f`
    to print the function name before calling
    and the return value after returned.

    Args:
        f (Callable): a function

    Returns:
        Callable: tracing function
    """
    @functools.wraps(f)
    def wrapper() -> Any:
        fname = f"{f.__name__}()"

        print(f"calling {fname}")
        res = f()
        print(f"{fname} returned `{res}`")

        return res
    return wrapper


@trace
def one() -> int:
    return 1


print(one.__name__)  # one

one()
# calling one()
# one() returned `1`

```


# Special Methods (Dunder Methods)

Special methods defineds how the object behaves when applied built-in methods.  
Special methods are also called *dunder-method*s due to duble under scores.  

See [documents](https://docs.python.org/3.11/reference/datamodel.html#special-method-names) more details.  


```py
# src/dunder_methods.py

from typing import Any


class User:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def __repr__(self) -> str:
        "defining the string to represent the object for debug"
        return f"{self.__class__.__name__}(id={self.id}, name={self.name})"

    def __str__(self) -> str:
        "defining the string used when the object is casted to `str`"
        return self.name

    def __eq__(self, other: Any) -> bool:
        "defining the equality of the object"
        if not ("id" in other.__dict__ and "name" in other.__dict__):
            other_cls_name = other.__class__.__name__
            raise TypeError(
                f"{self.__class__.__name__} cannot be compared "
                f"with {other_cls_name} objects; "
                f"{other_cls_name} objects do not have attributes "
                "`id` and `name`")

        return self.id == other.id and self.name == other.name


alice = User(id=1, name="alice")

print(repr(alice))  # User(id=1, name=alice)

print(str(alice))   # alice

# f-strings uses `__str__()` internally
print(f"{alice}")   # alice

# print() tries to use `__str__()` first and instead uses `__repr__()` if failed.
print(alice)    # alice


class Student:
    def __init__(self, id: int, student_no: int, name: str) -> None:
        self.id = id
        self.student_no = student_no
        self.name = name


student_alice = Student(1, 100, "alice")

# `==` uses `__eq__()` internally
print(alice == student_alice)   # True

```


# Enums

We can define *Enum*s for a set of counted values.  
A Enum consists of *member*s, and each member consists of *name* and *value*.  

For example, in code below *member*s of Enum `Permission` are `Permission.READ`, `Permission.WRITE` and `Permission.EXECUTE`.  
The member `Permission.READ` has the name `"READ"` and the value `"read"`

```py
# src/enums.py

from enum import Enum


class Permission(Enum):
    READ = "read"
    WRITE = "write"
    EXECUTE = "execute"


# get *member* through property access
r = Permission.READ

print(r == Permission.READ)  # True
print(r == Permission.WRITE)    # False

# get *member* using the *name*
print(r == Permission["READ"])  # True

# get *member* using the *value*
print(r == Permission("read"))  # True


print(r == "read")  # False; *member* vs. *value*

# get *name*
print(Permission.READ.name)  # "READ"

# get *value*
print(Permission.READ.value)    # "read"


# check if the object is one of `Permissino` enum
print(r in Permission)  # True


# listing *member*s
print(list(Permission))
# [<Permission.READ: 'read'>, <Permission.WRITE: 'write'>, <Permission.EXECUTE: 'execute'>] # noqa E501

# listing *name*s
print([p.name for p in Permission])  # ['READ', 'WRITE', 'EXECUTE']

# listing *value*s
print([p.value for p in Permission])    # ['read', 'write', 'execute']

```
