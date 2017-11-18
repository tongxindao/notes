class MyContextManger(object):
    def __enter__(self):
        print("Entering...")
    def __exit__(self, exception_type, exception_value, traceback):
        print("Leaving...")
        if exception_type is None:
            print("No Exceptions!")
            return False
        elif exception_type is ValueError:
            print("Value Error!")
            return True
        else:
            print("Other Error!")
            return True


with MyContextManger():
    print("Testing...")
    raise(ValueError)

print("=" * 30)

with MyContextManger():
    print("Testing...")
