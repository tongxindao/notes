courses = ("C++", "Cloud", "Linux", "PHP")
print("courses is: {0}".format(courses))
print("courses[0] is: {0}".format(courses[0]))

try:
    print("courses.sort() is: {0}".format(courses.sort()))
except AttributeError:
    print("AttributeError: \'tuple\' object has no attribute \'sort\'")

try:
    del courses[0]
    print("after courses[0] is: {0}".format(courses))
except TypeError:
    print("\'tuple\' object doesn\'t support item deletion")

new_courses = ("Linux", ["BigData1", "BigData2", "BigData3"], "Vim")
print("new_courses[1] is: {0}".format(new_courses[1]))

new_courses[1].append("BigData4")
print("new_courses[1].append(\"BigData4\") is: {0}".format(new_courses))

course = ("Linux")
print("course is {0}, and it\'s type: {1}".format(course, type(course)))

course = ("Linux",)
print("course is {0}, and it\'s type: {1}".format(course, type(course)))
