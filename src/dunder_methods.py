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

# print() try to use `__str__()` first and instead use `__repr__()` if failed.
print(alice)    # alice


class Student:
    def __init__(self, id: int, student_no: int, name: str) -> None:
        self.id = id
        self.student_no = student_no
        self.name = name


student_alice = Student(1, 100, "alice")

# `==` uses `__eq__()` internally
print(alice == student_alice)   # True
