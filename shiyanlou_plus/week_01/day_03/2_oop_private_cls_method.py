class Shiyanlou:
    __private_name = "shiyanlou"

    def __get_private_name(self):
        return self.__private_name


try:
    s = Shiyanlou()
    print(s.__private_name)
    print("=" * 55)
    print(s.__get_private_name())
    print("=" * 55)
except AttributeError:
    print("\'Shiyanlou\' object has no attribute!")

print("=" * 55)
print("If you use like this\n\
obj._Classname__privateAttributeOrMethod,\n\
you can access private attribute or method.")
print("=" * 55)
print(s._Shiyanlou__private_name)
print("=" * 55)
print(s._Shiyanlou__get_private_name())
