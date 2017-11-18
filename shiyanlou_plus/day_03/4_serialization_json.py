import json

courses = {1: "Linux", 2: "Vim", 3: "Git"}

print(json.dumps(courses))

with open("courses.json", "w") as file:
    file.write(json.dumps(courses))

with open("courses.json", "r") as file:
    new_courses = json.loads(file.read())

print(new_courses)
print(type(new_courses))
