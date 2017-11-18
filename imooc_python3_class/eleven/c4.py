def f1():
    a = 10
    def f2():
        # a = 20
        return a
    return f2

f = f1()
print(f.__closure__)
print(f)