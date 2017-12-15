class A:
    def __nonzero__(self): # python2
        print("test A.__nonzero__()")
        return True
    def __len__(self): # python3
        print("get length")
        return False


if A():
    print("not empty")
else:
    print("empty")
