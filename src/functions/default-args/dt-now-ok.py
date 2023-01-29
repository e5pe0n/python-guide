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
