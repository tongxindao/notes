courses = set()
print("courses\'s type is: {0}".format(type(courses)))

courses = {"Linux", "C++", "Vim", "Linux"}
print("courses is: {0}".format(courses))

nameset = set("shiyanlou.com")
print("nameset is: {0}".format(nameset))

print("\'Linux\' in courses: {0}".format("Linux" in courses))
print("\'Python\' in courses: {0}".format("Python" in courses))
print("\'Python\' not in courses: {0}".format("Python" not in courses))

print("courses is: {0}".format(courses))

courses.add("Python")
print("courses.add(\'Python\'): {0}".format(courses))
print("\'Python\' in courses: {0}".format("Python" in courses))

courses.remove("Python")
print("courses.remove(\'Python\'): {0}".format(courses))
print("\'Python\' in courses: {0}".format("Python" in courses))

try:
    courses.remove("Python")
except KeyError:
    print("KeyError: \'Python\'")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("set1 = {0}\nset2 = {1}".format(set1, set2))
print("\'set1 | set2\' result is: {0}".format(set1 | set2))
print("\'set1.union(set2)\' result is: {0}".format(set1.union(set2)))

print("\'set1 & set2\' result is: {0}".format(set1 & set2))

print("\'set1 - set2\' result is: {0}".format(set1 - set2))

print("\'set1 ^ set2\' result is: {0}".format(set1 ^ set2))

course = {}
print("\'course = {}\' type is: %s" % type(course))
course = {1}
print("\'course = {1}\' type is: %s" % type(course))
