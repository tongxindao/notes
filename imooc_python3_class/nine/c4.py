from c5 import Human

class Student(Human):
    # sum = 0
    def __init__(self, school, name, age):
        self.school = school
        super(Student, self).__init__(name, age)
        # Human.__init__(self, name, age)

    def do_homework(self):
        # super(Student, self).get_name()
        # print("homework")
        super(Student, self).do_homework()


student1 = Student("TJTC", "toby", 10)
student1.do_homework()
# print(student1.sum)
# print(Student.sum)
# print(student1.name)
# print(student1.age)
# student1.get_name()