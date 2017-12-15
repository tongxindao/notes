import sys

try:
    print a
    b = 0
    print(a/b)
except ZeroDivisionError:
    sys.exit("ZeroDivisionError: Can not division zero!")
