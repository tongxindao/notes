class Student(object):

    def __init__(self, name, course=None):
        self.name = name
        if course is None:
            course = []
        self.course = course

    def addcourse(self, coursename):
        self.course.append(coursename)

    def printcourse(self):
        for item in self.course:
            print(item)


stuA = Student("Wang yi")
stuA.addcourse("English")
stuA.addcourse("Math")
print(stuA.name + "'s course:")
print("stuA course's id: " + str(id(stuA.course)))
stuA.printcourse()
print("=" * 40)
stuB = Student("Li san")
stuB.addcourse("Chinese")
stuB.addcourse("Physics")
print(stuB.name + "'s course:")
print("stuB course's id: " + str(id(stuB.course)))
stuB.printcourse()
