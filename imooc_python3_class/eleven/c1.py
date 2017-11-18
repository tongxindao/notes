from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

class VIP1(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

# print(type(VIP.GREEN))
# print(type(VIP.GREEN.name))
# print(VIP["GREEN"])

# for v in VIP:
#     print(v)
#     print(v.value)

# print(VIP.GREEN == VIP1.GREEN)

# for v in VIP.__members__:
#     print(v)

a = 1
print(VIP(a))