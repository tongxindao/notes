def FinallyTest():
    print("I am starting...")
    while True:
        try:
            print("I am running")
            raise IndexError("r")
        except NameError as e:
            print("NameError happened %s" % e)
            break
        finally:
            print("finally executed")
            break


FinallyTest()
