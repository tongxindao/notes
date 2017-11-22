import pickle

courses = {1: "Linux", 2: "Vim", 3: "Git"}

with open("./courses.data", "wb") as file:
    pickle.dump(courses, file)

with open("./courses.data", "rb") as file:
    new_courses = pickle.load(file)

print(new_courses)
print(type(new_courses))
