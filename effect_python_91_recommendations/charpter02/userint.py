import types

class UserInt(int):
    def __init__(self, val=0):
        self._val = int(val)
    def __add__(self, val):
        if isinstance(val, UserInt):
            return UserInt(self._val + val._val)
        return self._val + val
    def __iadd__(self, val):
        raise NotImplementedError("not support operation")
    def __str__(self):
        return str(self._val)
    def __repr__(self):
        return "Integer(%s)" % self._val


n = UserInt()
print(n)
m = UserInt(2)
print(m)
print(n+m)
print(type(n) is int)
print(isinstance(n, int))
