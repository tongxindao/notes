courses = ["Linux", "Python", "Vim", "C++"]
courses.append("PHP")

print("course count is: {0}".format(len(courses)))
print("courses is: {0}".format(courses))
print("courses is: {0}".format(courses[0]))
print("courses is: {0}".format(courses[-1]))
print("courses is: {0}".format(courses[-2]))

try:
    print("courses is: {0}".format(courses[9]))
except IndexError:
    print("IndexError: list index out of range!!!")

courses.insert(0, "Java")
print("after insert courses is: {0}".format(courses))
courses.insert(1, "Ruby")
print("after insert courses is: {0}".format(courses))

count = courses.count("Java")
print("Java count in courses: {0}".format(count))

courses.remove("Java")
print("after remove courses is: {0}".format(courses))

del courses[-1]
print("after del courses is: {0}".format(courses))

courses.append("PHP")
print("after append courses is: {0}".format(courses))

courses.reverse()
print("after reverse courses is: {0}".format(courses))

new_courses = ["BigData", "Cloud"]
courses.extend(new_courses)
print("after extend courses is: {0}".format(courses))

courses.sort()
print("after sort courses is: {0}".format(courses))

c = courses.pop()
print("courses pop\'s course is :{0}".format(c))
print("after pop courses is: {0}".format(courses))
courses.pop()
courses.pop()
print("after pop courses is: {0}".format(courses))
courses.pop(0)
print("after pop courses is: {0}".format(courses))
