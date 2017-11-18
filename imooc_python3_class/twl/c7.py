# import time

# def f1():
#     print("This is a function f1")

# def f2():
#     print("This is a function f2")

# def print_current_time(func):
#     print(time.time())
#     func()

# print_current_time(f1)
# print_current_time(f2)

import time

def decorator(func):
    def wrapper():
        print(time.time)
        func()
    return wrapper

@decorator
def f1():
    print("This is a function")

f1()