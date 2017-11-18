class Test():
    # pass
    def __len__(self):
        print("len called")
        return 1
    # def __bool__(self):
    #     print("bool called")
    #     return False

# print(len(Test()))
print(bool(Test()))