def ReturnTest(a):
    try:
        if a <= 0:
            raise ValueError("data can not be negative")
        else:
            return a
    except ValueError as e:
        print(e)
    finally:
        print("The End!")
        return -1


print(ReturnTest(0))
print(ReturnTest(2))
