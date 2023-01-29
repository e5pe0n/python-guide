# NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG NG
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
