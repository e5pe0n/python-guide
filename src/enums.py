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
