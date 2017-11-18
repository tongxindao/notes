students = {
    "Tony": 18,
    "Jerry": 19,
    "Carry": 20
}

# b = {value:key for key,value in students.items()}
# print(b)

b = (key for key,value in students.items())
for x in b:
    print(x)