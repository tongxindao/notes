coursesdict = {1: "Linux", 2: "Vim"}
print("coursesdict is: {0}".format(coursesdict))
print("coursesdict[1] is: {0}".format(coursesdict[1]))
print("coursesdict[2] is: {0}".format(coursesdict[2]))

try:
    print("coursesdict[4] is: {0}".format(coursesdict[4]))
except KeyError:
    print("KeyError: 4")

print("coursesdict[2] is: {0}".format(coursesdict[2]))
print("coursesdict.get(4) is: {0}".format(coursesdict.get(4)))
print("coursesdict.get(2) is: {0}".format(coursesdict.get(2)))
print("coursesdict.get(4, \'default\') is: {0}".format(
    coursesdict.get(4, 'default')))

dict_from_tuple = dict(((1, "Linux"), (2, "Vim")))
print("dict_from_tuple is: {0}".format(dict_from_tuple))

coursesdict[5] = "Bash"
coursesdict[6] = "Python"
print("coursesdict is: {0}".format(coursesdict))

del coursesdict[1]
print("coursesdict is: {0}".format(coursesdict))

try:
    del coursesdict[1]
except KeyError:
    print("KeyError: 1")

for key, value in coursesdict.items():
    print("key = {0}, value = {1}".format(key, value))

print("coursesdict is: {0}".format(coursesdict))
print("coursesdict keys is: {0}".format(coursesdict.keys()))
print("coursesdict values is: {0}".format(coursesdict.values()))

print("coursesdict is: {0}".format(coursesdict))
coursesdict.pop(2)
print("after pop 2 coursesdict is: {0}".format(coursesdict))
