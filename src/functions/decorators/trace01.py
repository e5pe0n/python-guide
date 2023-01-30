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
