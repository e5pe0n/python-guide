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
