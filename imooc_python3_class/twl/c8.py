import time

def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper

@decorator
def f1(func_name1):
    print("This is a function named " + func_name1)

@decorator
def f2(func_name1, func_name2):
    print("This is a function named " + func_name1)
    print("This is a function named " + func_name2)

f1("test func")
f2("test func1", "test func2")