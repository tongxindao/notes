import sys
sys.setrecursionlimit(100)

def add(x, y):
    result = x + y
    return result


def output(code):
    print(code)

a = add(1, 2)
b = output('d')

print(a, b)