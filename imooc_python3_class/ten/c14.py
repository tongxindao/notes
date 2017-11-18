import json

student = [
    {"name":"tongxindao", "age":False}, 
    {"name":"tongxindao", "age":25}, 
    {"name":"tongxindao", "age":25}
]

json_str = json.dumps(student)
print(type(json_str))
print(json_str)