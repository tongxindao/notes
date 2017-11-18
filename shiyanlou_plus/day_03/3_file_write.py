filename = "test.txt"
with open(filename, "w") as file:
    file.write("testline1")
    file.write("testline2")

with open(filename, "r") as file:
    print(file.readlines())

with open(filename, "a") as file:
    file.write("testline3")
    file.write("testline4")

with open(filename, "r") as file:
    print(file.readlines())
