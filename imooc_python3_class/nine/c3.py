class Student():
    name = "this is class variable"
    age = 0
    sum = 0

    def __init__(self, name, age):
        # print("student")
        self.name = name
        self.age = age
        self.__score = 11

    def marking(self, score):
        if score < 0:
            print("no no no!")
        self.__score = score
        print("Score: " + str(self.__score))

    def do_homework(self):
        print("homework")

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        # print(cls.sum)

    @staticmethod
    def add(x, y):
        print("this is a static method")


class Printer():
    def print_file(self):
        print("name: " + self.name)
        print("age: " + str(self.age))

    
a = Student("tony", 10)
b = Student("tony", 10)
# c = Student("tony", 10)
# Student.plus_sum()
# a.add(1, 2)
# Student.add(1, 3)
a.__score = 1
print(a.__score)
print(a.__dict__)
# a.marking(88)
print(b.__dict__)
print(b._Student__score)