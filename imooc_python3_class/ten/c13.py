import json

json_str = '[{"name":"tongxindao", "age":false}, {"name":"tongxindao", "age":25}, {"name":"tongxindao", "age":25}]'
student = json.loads(json_str)
print(type(student))
print(student)
# print(student["name"])
# print(student["age"])

# json   python
# object dict
# array  list
# string str
# number int
# number float
# true   True
# false  False
# null   None